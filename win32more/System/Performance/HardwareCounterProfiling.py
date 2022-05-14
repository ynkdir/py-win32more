from win32more import *
import win32more.System.Performance.HardwareCounterProfiling
import win32more.Foundation

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.System.Performance.HardwareCounterProfiling, name, eval(f"_define_{name}()"))
    return getattr(win32more.System.Performance.HardwareCounterProfiling, name)
HARDWARE_COUNTER_TYPE = Int32
HARDWARE_COUNTER_TYPE_PMCCounter = 0
HARDWARE_COUNTER_TYPE_MaxHardwareCounterType = 1
def _define_HARDWARE_COUNTER_DATA_head():
    class HARDWARE_COUNTER_DATA(Structure):
        pass
    return HARDWARE_COUNTER_DATA
def _define_HARDWARE_COUNTER_DATA():
    HARDWARE_COUNTER_DATA = win32more.System.Performance.HardwareCounterProfiling.HARDWARE_COUNTER_DATA_head
    HARDWARE_COUNTER_DATA._fields_ = [
        ("Type", win32more.System.Performance.HardwareCounterProfiling.HARDWARE_COUNTER_TYPE),
        ("Reserved", UInt32),
        ("Value", UInt64),
    ]
    return HARDWARE_COUNTER_DATA
def _define_PERFORMANCE_DATA_head():
    class PERFORMANCE_DATA(Structure):
        pass
    return PERFORMANCE_DATA
def _define_PERFORMANCE_DATA():
    PERFORMANCE_DATA = win32more.System.Performance.HardwareCounterProfiling.PERFORMANCE_DATA_head
    PERFORMANCE_DATA._fields_ = [
        ("Size", UInt16),
        ("Version", Byte),
        ("HwCountersCount", Byte),
        ("ContextSwitchCount", UInt32),
        ("WaitReasonBitMap", UInt64),
        ("CycleTime", UInt64),
        ("RetryCount", UInt32),
        ("Reserved", UInt32),
        ("HwCounters", win32more.System.Performance.HardwareCounterProfiling.HARDWARE_COUNTER_DATA * 16),
    ]
    return PERFORMANCE_DATA
def _define_EnableThreadProfiling():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,UInt64,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("EnableThreadProfiling", windll["KERNEL32"]), ((1, 'ThreadHandle'),(1, 'Flags'),(1, 'HardwareCounters'),(1, 'PerformanceDataHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DisableThreadProfiling():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE, use_last_error=False)(("DisableThreadProfiling", windll["KERNEL32"]), ((1, 'PerformanceDataHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryThreadProfiling():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.BOOLEAN), use_last_error=False)(("QueryThreadProfiling", windll["KERNEL32"]), ((1, 'ThreadHandle'),(1, 'Enabled'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadThreadProfilingData():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,POINTER(win32more.System.Performance.HardwareCounterProfiling.PERFORMANCE_DATA_head), use_last_error=False)(("ReadThreadProfilingData", windll["KERNEL32"]), ((1, 'PerformanceDataHandle'),(1, 'Flags'),(1, 'PerformanceData'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "HARDWARE_COUNTER_TYPE",
    "HARDWARE_COUNTER_TYPE_PMCCounter",
    "HARDWARE_COUNTER_TYPE_MaxHardwareCounterType",
    "HARDWARE_COUNTER_DATA",
    "PERFORMANCE_DATA",
    "EnableThreadProfiling",
    "DisableThreadProfiling",
    "QueryThreadProfiling",
    "ReadThreadProfilingData",
]
