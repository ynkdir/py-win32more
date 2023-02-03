from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Networking.WinSock
import Windows.Win32.System.UserAccessLogging
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
@winfunctype('ualapi.dll')
def UalStart(Data: POINTER(Windows.Win32.System.UserAccessLogging.UAL_DATA_BLOB_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ualapi.dll')
def UalStop(Data: POINTER(Windows.Win32.System.UserAccessLogging.UAL_DATA_BLOB_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ualapi.dll')
def UalInstrument(Data: POINTER(Windows.Win32.System.UserAccessLogging.UAL_DATA_BLOB_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ualapi.dll')
def UalRegisterProduct(wszProductName: Windows.Win32.Foundation.PWSTR, wszRoleName: Windows.Win32.Foundation.PWSTR, wszGuid: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class UAL_DATA_BLOB(Structure):
    Size: UInt32
    RoleGuid: Guid
    TenantId: Guid
    Address: Windows.Win32.Networking.WinSock.SOCKADDR_STORAGE
    UserName: Char * 260
make_head(_module, 'UAL_DATA_BLOB')
__all__ = [
    "UAL_DATA_BLOB",
    "UalInstrument",
    "UalRegisterProduct",
    "UalStart",
    "UalStop",
]
_arch_optional = [
]
