from win32more import *
import win32more.Storage.StructuredStorage

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.Storage.StructuredStorage, name, eval(f"_define_{name}()"))
    return getattr(win32more.Storage.StructuredStorage, name)
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
