#!/usr/bin/env python
from drv2605 import DRV2605, PlayWaveform, WaitMillis
import sys
import time
import math

print("""test-pattern.py - Test a DRV2605 built-in haptic pattern

Usage: {} <pattern number>

""".format(sys.argv[0]))

enable_calibration = True

drv2605 = DRV2605()
drv2605.reset()

drv2605.set_feedback_mode('LRA')
drv2605.set_library('LRA')

if enable_calibration:
    print("Calibrating...")
    drv2605.auto_calibrate()
    time.sleep(0.5)

if len(sys.argv) > 1:
    drv2605.set_mode('Internal Trigger')
    pattern = int(sys.argv[1])

    print("Playing pattern: {}".format(sys.argv[1]))

    drv2605.set_sequence(
        PlayWaveform(pattern),
        WaitMillis(100),
        PlayWaveform(pattern),
        WaitMillis(100),
        PlayWaveform(pattern)
    )

    drv2605.go()
    while drv2605.busy():
        time.sleep(0.01)

else:
    drv2605.set_mode('Real-time Playback')
    drv2605.set_realtime_data_format('Unsigned')
    drv2605.go()
    try:
        while True:
            d = time.time() * 10
            x = (math.sin(d) + 1) / 2
            x = int(x * 255)
            drv2605.set_realtime_input(x)
            print("Waveform: {}".format(x))
            time.sleep(0.01)
    except KeyboardInterrupt:
        pass
    finally:
        drv2605.set_realtime_input(0)
        drv2605.stop()
