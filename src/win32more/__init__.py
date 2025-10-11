# ruff: noqa: F401
from . import _win32api
from ._boxing import box_value, unbox_value
from ._comclass import ComClass
from ._comerror import ComError
from ._win32 import (
    FAILED,
    SUCCEEDED,
    WINFUNCTYPE,
    Boolean,
    Byte,
    Bytes,
    Char,
    Double,
    Guid,
    Int16,
    Int32,
    Int64,
    IntPtr,
    SByte,
    Single,
    String,
    UInt16,
    UInt32,
    UInt64,
    UIntPtr,
    Void,
    VoidPtr,
    WinError,
    windll,
)

# Initialize COM Multithreaded Apartment.
# Call CoInitializeEx(None, COINIT_APARTMENTTHREADED) explicitly for Single-Threaded Apartment.
if FAILED(_win32api.CoIncrementMTAUsage(VoidPtr())):
    raise WinError()
