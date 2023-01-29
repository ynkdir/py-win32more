from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.DeveloperLicensing
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
@winfunctype('WSClient.dll')
def CheckDeveloperLicense(pExpiration: POINTER(win32more.Foundation.FILETIME_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WSClient.dll')
def AcquireDeveloperLicense(hwndParent: win32more.Foundation.HWND, pExpiration: POINTER(win32more.Foundation.FILETIME_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('WSClient.dll')
def RemoveDeveloperLicense(hwndParent: win32more.Foundation.HWND) -> win32more.Foundation.HRESULT: ...
__all__ = [
    "AcquireDeveloperLicense",
    "CheckDeveloperLicense",
    "RemoveDeveloperLicense",
]
_arch_optional = [
]
