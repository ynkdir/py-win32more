from win32more import *
import win32more.Storage.StructuredStorage

def __getattr__(name):
    if f"_define_{name}" not in globals():
        raise AttributeError()
    setattr(win32more.Storage.StructuredStorage, name, globals()[f"_define_{name}"]())
    return getattr(win32more.Storage.StructuredStorage, name)
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
