from win32more import *
import win32more.Foundation
import win32more.System.DeveloperLicensing

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
def _define_CheckDeveloperLicense():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(("CheckDeveloperLicense", windll["WSClient"]), ((1, 'pExpiration'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AcquireDeveloperLicense():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(("AcquireDeveloperLicense", windll["WSClient"]), ((1, 'hwndParent'),(1, 'pExpiration'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveDeveloperLicense():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND, use_last_error=False)(("RemoveDeveloperLicense", windll["WSClient"]), ((1, 'hwndParent'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "CheckDeveloperLicense",
    "AcquireDeveloperLicense",
    "RemoveDeveloperLicense",
]
