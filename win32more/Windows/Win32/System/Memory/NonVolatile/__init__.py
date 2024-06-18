from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.System.Memory.NonVolatile
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
    def RtlFlushNonVolatileMemoryRanges(NvToken: VoidPtr, NvRanges: POINTER(win32more.Windows.Win32.System.Memory.NonVolatile.NV_MEMORY_RANGE), NumRanges: UIntPtr, Flags: UInt32) -> UInt32: ...
class NV_MEMORY_RANGE(Structure):
    BaseAddress: VoidPtr
    Length: UIntPtr


make_ready(__name__)
