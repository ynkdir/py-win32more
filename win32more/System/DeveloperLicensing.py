from win32more import *
import win32more.Foundation

def __getattr__(name):
    module = globals()
    try:
        f = module[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    module[name] = f()
    return module[name]
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
