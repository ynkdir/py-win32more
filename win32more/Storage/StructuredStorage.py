from win32more.base import *
import win32more.Storage.StructuredStorage

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
JET_HANDLE = UIntPtr
JET_INSTANCE = UIntPtr
JET_SESID = UIntPtr
JET_TABLEID = UIntPtr
JET_API_PTR = UIntPtr
__all__ = [
    "JET_HANDLE",
    "JET_INSTANCE",
    "JET_SESID",
    "JET_TABLEID",
    "JET_API_PTR",
]
