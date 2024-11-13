from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
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
