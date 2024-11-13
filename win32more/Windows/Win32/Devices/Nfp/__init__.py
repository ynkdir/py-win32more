from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Devices.Nfp
import win32more.Windows.Win32.Foundation
GUID_DEVINTERFACE_NFP: Guid = Guid('{fb3842cd-9e2a-4f83-8fcc-4b0761139ae9}')
DEVPKEY_NFP_Capabilities: win32more.Windows.Win32.Foundation.DEVPROPKEY = ConstantLazyLoader(fmtid=Guid('{fb3842cd-9e2a-4f83-8fcc-4b0761139ae9}'), pid=2)
IOCTL_NFP_GET_NEXT_SUBSCRIBED_MESSAGE: UInt32 = 5308480
IOCTL_NFP_SET_PAYLOAD: UInt32 = 5308484
IOCTL_NFP_GET_NEXT_TRANSMITTED_MESSAGE: UInt32 = 5308488
IOCTL_NFP_DISABLE: UInt32 = 5308492
IOCTL_NFP_ENABLE: UInt32 = 5308496
IOCTL_NFP_GET_MAX_MESSAGE_BYTES: UInt32 = 5308544
IOCTL_NFP_GET_KILO_BYTES_PER_SECOND: UInt32 = 5308548
class SUBSCRIBED_MESSAGE(Structure):
    cbPayloadHint: UInt32
    payload: Byte * 1


make_ready(__name__)
