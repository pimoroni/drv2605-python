#!/usr/bin/env python

import time

from trackball import TrackBall

from drv2605 import DRV2605

print("""haptic-trackball.py

Add haptic feedback to the Trackball breakout.

Press Ctrl+C to exit.

""")

trackball = TrackBall(interrupt_pin=4)
drv2605 = DRV2605()

x = 0
y = 0

delta_x = 0
delta_y = 0
last_state = 0

drv2605.reset()
drv2605.set_realtime_data_format('Unsigned')
drv2605.set_feedback_mode('LRA')
drv2605.set_mode('Real-time Playback')
# drv2605.set_mode('Internal Trigger')
# drv2605.set_sequence(PlayWaveform(24))
drv2605.go()

try:
    while True:
        up, down, left, right, switch, state = trackball.read()
        y += up
        y -= down
        x += right
        x -= left

        delta_x += right
        delta_x -= left

        delta_y += up
        delta_y -= down

        x = max(0, min(x, 255))
        y = max(0, min(y, 255))

        print(delta_x, delta_y)

        if state != last_state:
            drv2605.set_realtime_input(255)
            time.sleep(0.01)
            drv2605.set_realtime_input(0)
            last_state = state

        if abs(delta_x) > 2:
            drv2605.set_realtime_input(255)
            time.sleep(0.005)
            drv2605.set_realtime_input(0)
            delta_x = 0

        elif abs(delta_y) > 2:
            drv2605.set_realtime_input(255)
            time.sleep(0.005)
            drv2605.set_realtime_input(0)
            delta_y = 0

        # drv2605.set_realtime_input(x)

        time.sleep(0.001)

except KeyboardInterrupt:
    pass
