from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Performance.HardwareCounterProfiling
@winfunctype('KERNEL32.dll')
def EnableThreadProfiling(ThreadHandle: win32more.Windows.Win32.Foundation.HANDLE, Flags: UInt32, HardwareCounters: UInt64, PerformanceDataHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def DisableThreadProfiling(PerformanceDataHandle: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def QueryThreadProfiling(ThreadHandle: win32more.Windows.Win32.Foundation.HANDLE, Enabled: POINTER(win32more.Windows.Win32.Foundation.BOOLEAN)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def ReadThreadProfilingData(PerformanceDataHandle: win32more.Windows.Win32.Foundation.HANDLE, Flags: UInt32, PerformanceData: POINTER(win32more.Windows.Win32.System.Performance.HardwareCounterProfiling.PERFORMANCE_DATA)) -> UInt32: ...
class HARDWARE_COUNTER_DATA(Structure):
    Type: win32more.Windows.Win32.System.Performance.HardwareCounterProfiling.HARDWARE_COUNTER_TYPE
    Reserved: UInt32
    Value: UInt64
HARDWARE_COUNTER_TYPE = Int32
PMCCounter: win32more.Windows.Win32.System.Performance.HardwareCounterProfiling.HARDWARE_COUNTER_TYPE = 0
MaxHardwareCounterType: win32more.Windows.Win32.System.Performance.HardwareCounterProfiling.HARDWARE_COUNTER_TYPE = 1
class PERFORMANCE_DATA(Structure):
    Size: UInt16
    Version: Byte
    HwCountersCount: Byte
    ContextSwitchCount: UInt32
    WaitReasonBitMap: UInt64
    CycleTime: UInt64
    RetryCount: UInt32
    Reserved: UInt32
    HwCounters: win32more.Windows.Win32.System.Performance.HardwareCounterProfiling.HARDWARE_COUNTER_DATA * 16


make_ready(__name__)
