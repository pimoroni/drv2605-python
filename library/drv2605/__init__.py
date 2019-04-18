from i2cdevice import Device, Register, BitField, _int_to_bytes
from i2cdevice.adapter import Adapter, LookupAdapter, U16ByteSwapAdapter

DRV2605_ADDR = 0x5a


class DRV2605():
    def __init__(self, i2c_addr=DRV2605_ADDR, i2c_dev=None):
        self._i2c_addr = i2c_addr
        self._i2c_dev = i2c_dev
        self._drv2605 = Device(
            Register('STATUS', 0x00, fields=(
                BitField('device_id', 0b11100000),
                BitField('diagnostic', 0b00001000),
                BitField('over_temp', 0b00000010),
                BitField('over_current', 0b00000001),
            )),
            Register('MODE', 0x01, fields=(
                BitField('reset', 0b10000000),
                BitField('standby', 0b01000000),
                BitField('mode', 0b00000111),
            )),
            Register('REALTIME_PLAYBACK', 0x02, fields=(
                BitField('input', 0xff)
            )),
            Register('LIBRARY_SELECTION', 0x03, fields=(
                BitField('high_impedance', 0b00010000),
                BitField('library', 0b00000111, adapter=LookupAdapter({
                    'Empty': 0,
                    'TS2200 A': 1,
                    'TS2200 B': 2,
                    'TS2200 C': 3,
                    'TS2200 D': 4,
                    'TS2200 E': 5,
                    'LRA': 6,
                    'TS2200 F': 7
                })),
            )),
            """
            When the wait bit is set, the value of its corresponding
            waveform becomes a timed delay.
            Delay time = 10 ms x waveformN
            """
            Register('WAVEFORM_SEQUENCER', 0x04, fields=(
                BitField('wait1', 1 << 55),
                BitField('waveform1', 0x7f << 55),
                BitField('wait2', 1 << 47),
                BitField('waveform2', 0x7f << 47),
                BitField('wait3', 1 << 39),
                BitField('waveform3', 0x7f << 39),
                BitField('wait4', 1 << 31),
                BitField('waveform4', 0x7f << 31),
                BitField('wait5', 1 << 23),
                BitField('waveform5', 0x7f << 23),
                BitField('wait6', 1 << 15),
                BitField('waveform6', 0x7f << 15),
                BitField('wait7', 1 << 7),
                BitField('waveform7', 0x7f << 7),
                BitField('wait8', 1 << 0),
                BitField('waveform8', 0x7f << 0),
            ), bit_width=8 * 8),
            Register('GO', 0x0C),
        )

