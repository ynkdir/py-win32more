from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.System.Memory.NonVolatile
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
def _define_RtlGetNonVolatileToken():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UIntPtr,POINTER(c_void_p))(('RtlGetNonVolatileToken', windll['ntdll.dll']), ((1, 'NvBuffer'),(1, 'Size'),(1, 'NvToken'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlFreeNonVolatileToken():
    try:
        return WINFUNCTYPE(UInt32,c_void_p)(('RtlFreeNonVolatileToken', windll['ntdll.dll']), ((1, 'NvToken'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlFlushNonVolatileMemory():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,c_void_p,UIntPtr,UInt32)(('RtlFlushNonVolatileMemory', windll['ntdll.dll']), ((1, 'NvToken'),(1, 'NvBuffer'),(1, 'Size'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlDrainNonVolatileFlush():
    try:
        return WINFUNCTYPE(UInt32,c_void_p)(('RtlDrainNonVolatileFlush', windll['ntdll.dll']), ((1, 'NvToken'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlWriteNonVolatileMemory():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,c_void_p,c_void_p,UIntPtr,UInt32)(('RtlWriteNonVolatileMemory', windll['ntdll.dll']), ((1, 'NvToken'),(1, 'NvDestination'),(1, 'Source'),(1, 'Size'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlFillNonVolatileMemory():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,c_void_p,UIntPtr,Byte,UInt32)(('RtlFillNonVolatileMemory', windll['ntdll.dll']), ((1, 'NvToken'),(1, 'NvDestination'),(1, 'Size'),(1, 'Value'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlFlushNonVolatileMemoryRanges():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,POINTER(win32more.System.Memory.NonVolatile.NV_MEMORY_RANGE_head),UIntPtr,UInt32)(('RtlFlushNonVolatileMemoryRanges', windll['ntdll.dll']), ((1, 'NvToken'),(1, 'NvRanges'),(1, 'NumRanges'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NV_MEMORY_RANGE_head():
    class NV_MEMORY_RANGE(Structure):
        pass
    return NV_MEMORY_RANGE
def _define_NV_MEMORY_RANGE():
    NV_MEMORY_RANGE = win32more.System.Memory.NonVolatile.NV_MEMORY_RANGE_head
    NV_MEMORY_RANGE._fields_ = [
        ('BaseAddress', c_void_p),
        ('Length', UIntPtr),
    ]
    return NV_MEMORY_RANGE
__all__ = [
    "NV_MEMORY_RANGE",
    "RtlDrainNonVolatileFlush",
    "RtlFillNonVolatileMemory",
    "RtlFlushNonVolatileMemory",
    "RtlFlushNonVolatileMemoryRanges",
    "RtlFreeNonVolatileToken",
    "RtlGetNonVolatileToken",
    "RtlWriteNonVolatileMemory",
]
