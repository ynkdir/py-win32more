from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.System.Memory.NonVolatile
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
if ARCH in 'X64,ARM64':
    @winfunctype('ntdll.dll')
    def RtlGetNonVolatileToken(NvBuffer: c_void_p, Size: UIntPtr, NvToken: POINTER(c_void_p)) -> UInt32: ...
if ARCH in 'X64,ARM64':
    @winfunctype('ntdll.dll')
    def RtlFreeNonVolatileToken(NvToken: c_void_p) -> UInt32: ...
if ARCH in 'X64,ARM64':
    @winfunctype('ntdll.dll')
    def RtlFlushNonVolatileMemory(NvToken: c_void_p, NvBuffer: c_void_p, Size: UIntPtr, Flags: UInt32) -> UInt32: ...
if ARCH in 'X64,ARM64':
    @winfunctype('ntdll.dll')
    def RtlDrainNonVolatileFlush(NvToken: c_void_p) -> UInt32: ...
if ARCH in 'X64,ARM64':
    @winfunctype('ntdll.dll')
    def RtlWriteNonVolatileMemory(NvToken: c_void_p, NvDestination: c_void_p, Source: c_void_p, Size: UIntPtr, Flags: UInt32) -> UInt32: ...
if ARCH in 'X64,ARM64':
    @winfunctype('ntdll.dll')
    def RtlFillNonVolatileMemory(NvToken: c_void_p, NvDestination: c_void_p, Size: UIntPtr, Value: Byte, Flags: UInt32) -> UInt32: ...
if ARCH in 'X64,ARM64':
    @winfunctype('ntdll.dll')
    def RtlFlushNonVolatileMemoryRanges(NvToken: c_void_p, NvRanges: POINTER(Windows.Win32.System.Memory.NonVolatile.NV_MEMORY_RANGE_head), NumRanges: UIntPtr, Flags: UInt32) -> UInt32: ...
class NV_MEMORY_RANGE(EasyCastStructure):
    BaseAddress: c_void_p
    Length: UIntPtr
make_head(_module, 'NV_MEMORY_RANGE')
