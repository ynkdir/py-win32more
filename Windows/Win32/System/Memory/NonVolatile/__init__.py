from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
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
    def RtlGetNonVolatileToken(NvBuffer: VoidPtr, Size: UIntPtr, NvToken: POINTER(VoidPtr)) -> UInt32: ...
if ARCH in 'X64,ARM64':
    @winfunctype('ntdll.dll')
    def RtlFreeNonVolatileToken(NvToken: VoidPtr) -> UInt32: ...
if ARCH in 'X64,ARM64':
    @winfunctype('ntdll.dll')
    def RtlFlushNonVolatileMemory(NvToken: VoidPtr, NvBuffer: VoidPtr, Size: UIntPtr, Flags: UInt32) -> UInt32: ...
if ARCH in 'X64,ARM64':
    @winfunctype('ntdll.dll')
    def RtlDrainNonVolatileFlush(NvToken: VoidPtr) -> UInt32: ...
if ARCH in 'X64,ARM64':
    @winfunctype('ntdll.dll')
    def RtlWriteNonVolatileMemory(NvToken: VoidPtr, NvDestination: VoidPtr, Source: VoidPtr, Size: UIntPtr, Flags: UInt32) -> UInt32: ...
if ARCH in 'X64,ARM64':
    @winfunctype('ntdll.dll')
    def RtlFillNonVolatileMemory(NvToken: VoidPtr, NvDestination: VoidPtr, Size: UIntPtr, Value: Byte, Flags: UInt32) -> UInt32: ...
if ARCH in 'X64,ARM64':
    @winfunctype('ntdll.dll')
    def RtlFlushNonVolatileMemoryRanges(NvToken: VoidPtr, NvRanges: POINTER(Windows.Win32.System.Memory.NonVolatile.NV_MEMORY_RANGE_head), NumRanges: UIntPtr, Flags: UInt32) -> UInt32: ...
class NV_MEMORY_RANGE(EasyCastStructure):
    BaseAddress: VoidPtr
    Length: UIntPtr
make_head(_module, 'NV_MEMORY_RANGE')
