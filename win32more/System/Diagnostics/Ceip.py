from win32more import *
import win32more.System.Diagnostics.Ceip
import win32more.Foundation

def __getattr__(name):
    if f"_define_{name}" not in globals():
        raise AttributeError()
    setattr(win32more.System.Diagnostics.Ceip, name, globals()[f"_define_{name}"]())
    return getattr(win32more.System.Diagnostics.Ceip, name)
def __dir__():
    return __all__
def _define_CeipIsOptedIn():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(("CeipIsOptedIn", windll["KERNEL32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "CeipIsOptedIn",
]
