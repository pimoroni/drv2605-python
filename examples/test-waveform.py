#!/usr/bin/env python

from drv2605 import DRV2605, PlayWaveform, WaitMillis
import argparse
import time
import math

waveforms = {
    'sine': lambda x: (math.sin(x) + 1) / 2,
    'square': lambda x: int(x % 2),
    'saw': lambda x: x % 1,
    'triangle': lambda x: 1 - abs(x % 2 - 1)
}

print("""test-waveform.py - Test DRV2605 real-time waveform mode
""")

parser = argparse.ArgumentParser()
parser.add_argument('--type', type=str, default='sine', choices=waveforms.keys(),
                    help='waveform to use')
parser.add_argument('--speed', type=float, default=10,
                    help='speed of waveform mode')
parser.add_argument('--intensity', type=int, default=122,
                    help='intensity of waveform mode')
parser.add_argument('--calibrate', action='store_true', default=False,
                    help='perform calibration first')

args = parser.parse_args()

if args.speed < 1 or args.speed > 127:
    parser.error("Speed should be between 1 and 127")

if args.intensity not in range(1, 123):
    parser.error("Intensity should be between 1 and 122")

drv2605 = DRV2605()
drv2605.reset()

drv2605.set_feedback_mode('LRA')
drv2605.set_library('LRA')

if args.calibrate:
    print("Calibrating...")
    drv2605.auto_calibrate()
    time.sleep(0.5)

print("Playing waveform at speed {} with intensity {}".format(
      args.speed, args.intensity))

drv2605.set_mode('Real-time Playback')
drv2605.set_realtime_data_format('Unsigned')
drv2605.go()

waveform = waveforms[args.type]

try:
    while True:
        d = time.time() * args.speed
        x = waveform(d)
        x = int(x * (132 + args.intensity))
        print(x)
        drv2605.set_realtime_input(x)
        time.sleep(0.01 / args.speed)
except KeyboardInterrupt:
    pass
finally:
    drv2605.set_realtime_input(0)
    drv2605.stop()
