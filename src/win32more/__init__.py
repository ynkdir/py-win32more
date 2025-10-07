# ruff: noqa: F401
from ._win32 import (
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
)
from ._win32api import FAILED, SUCCEEDED
from ._win32api import CoIncrementMTAUsage as _CoIncrementMTAUsage

# Initialize COM Multithreaded Apartment.
# Call CoInitializeEx(None, COINIT_APARTMENTTHREADED) explicitly for Single-Threaded Apartment.
if FAILED(_CoIncrementMTAUsage(VoidPtr())):
    raise WinError()
