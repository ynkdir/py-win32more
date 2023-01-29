from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Networking.WinSock
import win32more.System.UserAccessLogging
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
def UalStart(Data: POINTER(win32more.System.UserAccessLogging.UAL_DATA_BLOB_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('ualapi.dll')
def UalStop(Data: POINTER(win32more.System.UserAccessLogging.UAL_DATA_BLOB_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('ualapi.dll')
def UalInstrument(Data: POINTER(win32more.System.UserAccessLogging.UAL_DATA_BLOB_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('ualapi.dll')
def UalRegisterProduct(wszProductName: win32more.Foundation.PWSTR, wszRoleName: win32more.Foundation.PWSTR, wszGuid: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
class UAL_DATA_BLOB(Structure):
    Size: UInt32
    RoleGuid: Guid
    TenantId: Guid
    Address: win32more.Networking.WinSock.SOCKADDR_STORAGE
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
