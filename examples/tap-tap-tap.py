#!/usr/bin/env python

from drv2605 import DRV2605, PlayWaveform, WaitMillis
import time

print("""tap-tap-tap.py - Mimics a tap tap tap

""")

enable_calibration = False

drv2605 = DRV2605()
drv2605.reset()

drv2605.set_feedback_mode("LRA")
drv2605.set_library("LRA")

pattern = 1

try:
    while True:
        drv2605.set_sequence(
            PlayWaveform(pattern),
            WaitMillis(200),
            PlayWaveform(pattern),
            WaitMillis(200),
            PlayWaveform(pattern)
        )
        drv2605.go()
        while drv2605.busy():
            time.sleep(0.01)
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    drv2605.set_realtime_input(0)
    drv2605.stop()
