from win32more import *
import win32more.System.Diagnostics.Ceip
import win32more.Foundation

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.System.Diagnostics.Ceip, name, eval(f"_define_{name}()"))
    return getattr(win32more.System.Diagnostics.Ceip, name)
def _define_CeipIsOptedIn():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(("CeipIsOptedIn", windll["KERNEL32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "CeipIsOptedIn",
]
