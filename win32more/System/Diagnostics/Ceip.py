from win32more import *
import win32more.Foundation
import win32more.System.Diagnostics.Ceip

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
def _define_CeipIsOptedIn():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(("CeipIsOptedIn", windll["KERNEL32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "CeipIsOptedIn",
]
