from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Storage.StructuredStorage
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
JET_API_PTR = UIntPtr
JET_HANDLE = UIntPtr
JET_INSTANCE = UIntPtr
JET_SESID = UIntPtr
JET_TABLEID = UIntPtr
__all__ = [
    "JET_API_PTR",
    "JET_HANDLE",
    "JET_INSTANCE",
    "JET_SESID",
    "JET_TABLEID",
]
