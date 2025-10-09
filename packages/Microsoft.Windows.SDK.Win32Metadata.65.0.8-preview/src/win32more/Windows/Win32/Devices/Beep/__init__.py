from __future__ import annotations
from win32more.win32.prelude import *
import win32more.Windows.Win32.Devices.Beep
DD_BEEP_DEVICE_NAME: String = '\\Device\\Beep'
DD_BEEP_DEVICE_NAME_U: String = '\\Device\\Beep'
IOCTL_BEEP_SET: UInt32 = 65536
BEEP_FREQUENCY_MINIMUM: UInt32 = 37
BEEP_FREQUENCY_MAXIMUM: UInt32 = 32767
class BEEP_SET_PARAMETERS(Structure):
    Frequency: UInt32
    Duration: UInt32


make_ready(__name__)
