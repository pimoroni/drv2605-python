import sys
import mock


def test_setup():
    sys.modules['smbus'] = mock.Mock()
    import drv2605
    device = drv2605.DRV2605()
    del device
