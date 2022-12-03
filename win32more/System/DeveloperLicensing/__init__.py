from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.DeveloperLicensing
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
def _define_CheckDeveloperLicense():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.FILETIME_head))(('CheckDeveloperLicense', windll['WSClient.dll']), ((1, 'pExpiration'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AcquireDeveloperLicense():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.Foundation.FILETIME_head))(('AcquireDeveloperLicense', windll['WSClient.dll']), ((1, 'hwndParent'),(1, 'pExpiration'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveDeveloperLicense():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND)(('RemoveDeveloperLicense', windll['WSClient.dll']), ((1, 'hwndParent'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "AcquireDeveloperLicense",
    "CheckDeveloperLicense",
    "RemoveDeveloperLicense",
]
