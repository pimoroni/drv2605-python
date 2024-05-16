# DRV2605 Haptic Driver

[![Build Status](https://img.shields.io/github/actions/workflow/status/pimoroni/drv2605-python/test.yml?branch=main)](https://github.com/pimoroni/drv2605-python/actions/workflows/test.yml)
[![Coverage Status](https://coveralls.io/repos/github/pimoroni/drv2605-python/badge.svg?branch=main)](https://coveralls.io/github/pimoroni/drv2605-python?branch=main)
[![PyPi Package](https://img.shields.io/pypi/v/drv2605.svg)](https://pypi.python.org/pypi/drv2605)
[![Python Versions](https://img.shields.io/pypi/pyversions/drv2605.svg)](https://pypi.python.org/pypi/drv2605)

# Installing

If you've already set up a Python virtual environment, you can also install the stable library manually from PyPi:

```
pip install drv2605
```

Otherwise our install script will set one up for you.

Stable library from GitHub:

```
git clone https://github.com/pimoroni/drv2605-python
cd drv2605-python
./install.sh
```

Latest/development library from GitHub:

```
git clone https://github.com/pimoroni/drv2605-python
cd drv2605-python
./install.sh --unstable
```

**Note** Libraries will be installed in the "pimoroni" virtual environment, you will need to activate it to run examples:

```
source ~/.virtualenvs/pimoroni/bin/activate
```

# Vibration Patterns

The DRV2605 has a library of built-in vibration patterns great for haptic feedback, notifications and more. For the complete list see:

http://www.ti.com/document-viewer/DRV2605/datasheet/waveform-library-effects-list-slos854718

