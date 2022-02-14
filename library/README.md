# DRV2605 Haptic Driver

[![Build Status](https://shields.io/github/workflow/status/pimoroni/drv2605-python/Python%20Tests.svg)](https://github.com/pimoroni/drv2605-python/actions/workflows/test.yml)
[![Coverage Status](https://coveralls.io/repos/github/pimoroni/drv2605-python/badge.svg?branch=master)](https://coveralls.io/github/pimoroni/drv2605-python?branch=master)
[![PyPi Package](https://img.shields.io/pypi/v/drv2605.svg)](https://pypi.python.org/pypi/drv2605)
[![Python Versions](https://img.shields.io/pypi/pyversions/drv2605.svg)](https://pypi.python.org/pypi/drv2605)


# Installing

Stable library from PyPi:

* Just run `python3 -m pip install drv2605`

Latest/development library from GitHub:

* `git clone https://github.com/pimoroni/drv2605-python`
* `cd drv2605-python`
* `sudo ./install.sh --unstable`

# Vibration Patterns

The DRV2605 has a library of built-in vibration patterns great for haptic feedback, notifications and more. For the complete list see:

http://www.ti.com/document-viewer/DRV2605/datasheet/waveform-library-effects-list-slos854718

# Changelog
0.0.3
-----

* Fix set_sequence, issue #2

0.0.2
-----

* Port to i2cdevice>=0.0.6 set/get API

0.0.1
-----

* Initial Release
