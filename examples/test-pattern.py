#!/usr/bin/env python

import argparse
import time

from drv2605 import DRV2605, PlayWaveform, WaitMillis

print("""test-pattern.py - Test a DRV2605 built-in haptic pattern
""")

parser = argparse.ArgumentParser()
parser.add_argument("--pattern", type=int, default=1,
                    help="number of pattern to play")
parser.add_argument("--repeat", type=int, default=1,
                    help="number of times to repeat")
parser.add_argument("--delay", type=int, default=100,
                    help="delay between repeats")
parser.add_argument("--calibrate", action="store_true", default=False,
                    help="perform calibration first")

args = parser.parse_args()

if args.repeat not in range(1, 5):
    parser.error("Repeat should be between 1 and 4")

if args.pattern not in range(1, 124):
    parser.error("Pattern should be between 1 and 123")

if args.delay not in range(0, 128):
    parser.error("Delay should be between 0 and 127")

drv2605 = DRV2605()
drv2605.reset()

drv2605.set_feedback_mode("LRA")
drv2605.set_library("LRA")

if args.calibrate:
    print("Calibrating...")
    drv2605.auto_calibrate()
    time.sleep(0.5)

drv2605.set_mode("Internal Trigger")

print("""Pattern: {}
Repeat: {} time(s)
Delay: {}ms""".format(
    args.pattern,
    args.repeat,
    args.delay
))

sequence = []

for x in range(args.repeat):
    sequence.append(PlayWaveform(args.pattern))
    sequence.append(WaitMillis(args.delay))

drv2605.set_sequence(
    *sequence
)

drv2605.go()
while drv2605.busy():
    time.sleep(0.01)
