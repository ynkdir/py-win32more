from win32more import *
import win32more.System.Memory.NonVolatile

def __getattr__(name):
    module = globals()
    try:
        f = module[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    module[name] = f()
    return module[name]
def __dir__():
    return __all__
def _define_NV_MEMORY_RANGE_head():
    class NV_MEMORY_RANGE(Structure):
        pass
    return NV_MEMORY_RANGE
def _define_NV_MEMORY_RANGE():
    NV_MEMORY_RANGE = win32more.System.Memory.NonVolatile.NV_MEMORY_RANGE_head
    NV_MEMORY_RANGE._fields_ = [
        ("BaseAddress", c_void_p),
        ("Length", UIntPtr),
    ]
    return NV_MEMORY_RANGE
def _define_RtlGetNonVolatileToken():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UIntPtr,POINTER(c_void_p), use_last_error=False)(("RtlGetNonVolatileToken", windll["ntdll"]), ((1, 'NvBuffer'),(1, 'Size'),(1, 'NvToken'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlFreeNonVolatileToken():
    try:
        return WINFUNCTYPE(UInt32,c_void_p, use_last_error=False)(("RtlFreeNonVolatileToken", windll["ntdll"]), ((1, 'NvToken'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlFlushNonVolatileMemory():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,c_void_p,UIntPtr,UInt32, use_last_error=False)(("RtlFlushNonVolatileMemory", windll["ntdll"]), ((1, 'NvToken'),(1, 'NvBuffer'),(1, 'Size'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlDrainNonVolatileFlush():
    try:
        return WINFUNCTYPE(UInt32,c_void_p, use_last_error=False)(("RtlDrainNonVolatileFlush", windll["ntdll"]), ((1, 'NvToken'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlWriteNonVolatileMemory():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,c_void_p,c_void_p,UIntPtr,UInt32, use_last_error=False)(("RtlWriteNonVolatileMemory", windll["ntdll"]), ((1, 'NvToken'),(1, 'NvDestination'),(1, 'Source'),(1, 'Size'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlFillNonVolatileMemory():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,c_void_p,UIntPtr,Byte,UInt32, use_last_error=False)(("RtlFillNonVolatileMemory", windll["ntdll"]), ((1, 'NvToken'),(1, 'NvDestination'),(1, 'Size'),(1, 'Value'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlFlushNonVolatileMemoryRanges():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,POINTER(win32more.System.Memory.NonVolatile.NV_MEMORY_RANGE),UIntPtr,UInt32, use_last_error=False)(("RtlFlushNonVolatileMemoryRanges", windll["ntdll"]), ((1, 'NvToken'),(1, 'NvRanges'),(1, 'NumRanges'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "NV_MEMORY_RANGE",
    "RtlGetNonVolatileToken",
    "RtlFreeNonVolatileToken",
    "RtlFlushNonVolatileMemory",
    "RtlDrainNonVolatileFlush",
    "RtlWriteNonVolatileMemory",
    "RtlFillNonVolatileMemory",
    "RtlFlushNonVolatileMemoryRanges",
]
