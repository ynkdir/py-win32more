from win32more import *
import win32more.System.ProcessStatus
import win32more.Foundation

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.System.ProcessStatus, name, eval(f"_define_{name}()"))
    return getattr(win32more.System.ProcessStatus, name)
PSAPI_VERSION = 2
ENUM_PROCESS_MODULES_EX_FLAGS = UInt32
LIST_MODULES_ALL = 3
LIST_MODULES_DEFAULT = 0
LIST_MODULES_32BIT = 1
LIST_MODULES_64BIT = 2
def _define_MODULEINFO_head():
    class MODULEINFO(Structure):
        pass
    return MODULEINFO
def _define_MODULEINFO():
    MODULEINFO = win32more.System.ProcessStatus.MODULEINFO_head
    MODULEINFO._fields_ = [
        ("lpBaseOfDll", c_void_p),
        ("SizeOfImage", UInt32),
        ("EntryPoint", c_void_p),
    ]
    return MODULEINFO
def _define_PSAPI_WS_WATCH_INFORMATION_head():
    class PSAPI_WS_WATCH_INFORMATION(Structure):
        pass
    return PSAPI_WS_WATCH_INFORMATION
def _define_PSAPI_WS_WATCH_INFORMATION():
    PSAPI_WS_WATCH_INFORMATION = win32more.System.ProcessStatus.PSAPI_WS_WATCH_INFORMATION_head
    PSAPI_WS_WATCH_INFORMATION._fields_ = [
        ("FaultingPc", c_void_p),
        ("FaultingVa", c_void_p),
    ]
    return PSAPI_WS_WATCH_INFORMATION
def _define_PSAPI_WS_WATCH_INFORMATION_EX_head():
    class PSAPI_WS_WATCH_INFORMATION_EX(Structure):
        pass
    return PSAPI_WS_WATCH_INFORMATION_EX
def _define_PSAPI_WS_WATCH_INFORMATION_EX():
    PSAPI_WS_WATCH_INFORMATION_EX = win32more.System.ProcessStatus.PSAPI_WS_WATCH_INFORMATION_EX_head
    PSAPI_WS_WATCH_INFORMATION_EX._fields_ = [
        ("BasicInfo", win32more.System.ProcessStatus.PSAPI_WS_WATCH_INFORMATION),
        ("FaultingThreadId", UIntPtr),
        ("Flags", UIntPtr),
    ]
    return PSAPI_WS_WATCH_INFORMATION_EX
def _define_PSAPI_WORKING_SET_BLOCK_head():
    class PSAPI_WORKING_SET_BLOCK(Union):
        pass
    return PSAPI_WORKING_SET_BLOCK
def _define_PSAPI_WORKING_SET_BLOCK():
    PSAPI_WORKING_SET_BLOCK = win32more.System.ProcessStatus.PSAPI_WORKING_SET_BLOCK_head
    class PSAPI_WORKING_SET_BLOCK__Anonymous_e__Struct(Structure):
        pass
    PSAPI_WORKING_SET_BLOCK__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UIntPtr),
    ]
    PSAPI_WORKING_SET_BLOCK._anonymous_ = [
        'Anonymous',
    ]
    PSAPI_WORKING_SET_BLOCK._fields_ = [
        ("Flags", UIntPtr),
        ("Anonymous", PSAPI_WORKING_SET_BLOCK__Anonymous_e__Struct),
    ]
    return PSAPI_WORKING_SET_BLOCK
def _define_PSAPI_WORKING_SET_INFORMATION_head():
    class PSAPI_WORKING_SET_INFORMATION(Structure):
        pass
    return PSAPI_WORKING_SET_INFORMATION
def _define_PSAPI_WORKING_SET_INFORMATION():
    PSAPI_WORKING_SET_INFORMATION = win32more.System.ProcessStatus.PSAPI_WORKING_SET_INFORMATION_head
    PSAPI_WORKING_SET_INFORMATION._fields_ = [
        ("NumberOfEntries", UIntPtr),
        ("WorkingSetInfo", win32more.System.ProcessStatus.PSAPI_WORKING_SET_BLOCK * 0),
    ]
    return PSAPI_WORKING_SET_INFORMATION
def _define_PSAPI_WORKING_SET_EX_BLOCK_head():
    class PSAPI_WORKING_SET_EX_BLOCK(Union):
        pass
    return PSAPI_WORKING_SET_EX_BLOCK
def _define_PSAPI_WORKING_SET_EX_BLOCK():
    PSAPI_WORKING_SET_EX_BLOCK = win32more.System.ProcessStatus.PSAPI_WORKING_SET_EX_BLOCK_head
    class PSAPI_WORKING_SET_EX_BLOCK__Anonymous_e__Union(Union):
        pass
    class PSAPI_WORKING_SET_EX_BLOCK__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    PSAPI_WORKING_SET_EX_BLOCK__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UIntPtr),
    ]
    class PSAPI_WORKING_SET_EX_BLOCK__Anonymous_e__Union__Invalid_e__Struct(Structure):
        pass
    PSAPI_WORKING_SET_EX_BLOCK__Anonymous_e__Union__Invalid_e__Struct._fields_ = [
        ("_bitfield", UIntPtr),
    ]
    PSAPI_WORKING_SET_EX_BLOCK__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    PSAPI_WORKING_SET_EX_BLOCK__Anonymous_e__Union._fields_ = [
        ("Anonymous", PSAPI_WORKING_SET_EX_BLOCK__Anonymous_e__Union__Anonymous_e__Struct),
        ("Invalid", PSAPI_WORKING_SET_EX_BLOCK__Anonymous_e__Union__Invalid_e__Struct),
    ]
    PSAPI_WORKING_SET_EX_BLOCK._anonymous_ = [
        'Anonymous',
    ]
    PSAPI_WORKING_SET_EX_BLOCK._fields_ = [
        ("Flags", UIntPtr),
        ("Anonymous", PSAPI_WORKING_SET_EX_BLOCK__Anonymous_e__Union),
    ]
    return PSAPI_WORKING_SET_EX_BLOCK
def _define_PSAPI_WORKING_SET_EX_INFORMATION_head():
    class PSAPI_WORKING_SET_EX_INFORMATION(Structure):
        pass
    return PSAPI_WORKING_SET_EX_INFORMATION
def _define_PSAPI_WORKING_SET_EX_INFORMATION():
    PSAPI_WORKING_SET_EX_INFORMATION = win32more.System.ProcessStatus.PSAPI_WORKING_SET_EX_INFORMATION_head
    PSAPI_WORKING_SET_EX_INFORMATION._fields_ = [
        ("VirtualAddress", c_void_p),
        ("VirtualAttributes", win32more.System.ProcessStatus.PSAPI_WORKING_SET_EX_BLOCK),
    ]
    return PSAPI_WORKING_SET_EX_INFORMATION
def _define_PROCESS_MEMORY_COUNTERS_head():
    class PROCESS_MEMORY_COUNTERS(Structure):
        pass
    return PROCESS_MEMORY_COUNTERS
def _define_PROCESS_MEMORY_COUNTERS():
    PROCESS_MEMORY_COUNTERS = win32more.System.ProcessStatus.PROCESS_MEMORY_COUNTERS_head
    PROCESS_MEMORY_COUNTERS._fields_ = [
        ("cb", UInt32),
        ("PageFaultCount", UInt32),
        ("PeakWorkingSetSize", UIntPtr),
        ("WorkingSetSize", UIntPtr),
        ("QuotaPeakPagedPoolUsage", UIntPtr),
        ("QuotaPagedPoolUsage", UIntPtr),
        ("QuotaPeakNonPagedPoolUsage", UIntPtr),
        ("QuotaNonPagedPoolUsage", UIntPtr),
        ("PagefileUsage", UIntPtr),
        ("PeakPagefileUsage", UIntPtr),
    ]
    return PROCESS_MEMORY_COUNTERS
def _define_PROCESS_MEMORY_COUNTERS_EX_head():
    class PROCESS_MEMORY_COUNTERS_EX(Structure):
        pass
    return PROCESS_MEMORY_COUNTERS_EX
def _define_PROCESS_MEMORY_COUNTERS_EX():
    PROCESS_MEMORY_COUNTERS_EX = win32more.System.ProcessStatus.PROCESS_MEMORY_COUNTERS_EX_head
    PROCESS_MEMORY_COUNTERS_EX._fields_ = [
        ("cb", UInt32),
        ("PageFaultCount", UInt32),
        ("PeakWorkingSetSize", UIntPtr),
        ("WorkingSetSize", UIntPtr),
        ("QuotaPeakPagedPoolUsage", UIntPtr),
        ("QuotaPagedPoolUsage", UIntPtr),
        ("QuotaPeakNonPagedPoolUsage", UIntPtr),
        ("QuotaNonPagedPoolUsage", UIntPtr),
        ("PagefileUsage", UIntPtr),
        ("PeakPagefileUsage", UIntPtr),
        ("PrivateUsage", UIntPtr),
    ]
    return PROCESS_MEMORY_COUNTERS_EX
def _define_PERFORMANCE_INFORMATION_head():
    class PERFORMANCE_INFORMATION(Structure):
        pass
    return PERFORMANCE_INFORMATION
def _define_PERFORMANCE_INFORMATION():
    PERFORMANCE_INFORMATION = win32more.System.ProcessStatus.PERFORMANCE_INFORMATION_head
    PERFORMANCE_INFORMATION._fields_ = [
        ("cb", UInt32),
        ("CommitTotal", UIntPtr),
        ("CommitLimit", UIntPtr),
        ("CommitPeak", UIntPtr),
        ("PhysicalTotal", UIntPtr),
        ("PhysicalAvailable", UIntPtr),
        ("SystemCache", UIntPtr),
        ("KernelTotal", UIntPtr),
        ("KernelPaged", UIntPtr),
        ("KernelNonpaged", UIntPtr),
        ("PageSize", UIntPtr),
        ("HandleCount", UInt32),
        ("ProcessCount", UInt32),
        ("ThreadCount", UInt32),
    ]
    return PERFORMANCE_INFORMATION
def _define_ENUM_PAGE_FILE_INFORMATION_head():
    class ENUM_PAGE_FILE_INFORMATION(Structure):
        pass
    return ENUM_PAGE_FILE_INFORMATION
def _define_ENUM_PAGE_FILE_INFORMATION():
    ENUM_PAGE_FILE_INFORMATION = win32more.System.ProcessStatus.ENUM_PAGE_FILE_INFORMATION_head
    ENUM_PAGE_FILE_INFORMATION._fields_ = [
        ("cb", UInt32),
        ("Reserved", UInt32),
        ("TotalSize", UIntPtr),
        ("TotalInUse", UIntPtr),
        ("PeakUsage", UIntPtr),
    ]
    return ENUM_PAGE_FILE_INFORMATION
def _define_PENUM_PAGE_FILE_CALLBACKW():
    return CFUNCTYPE(win32more.Foundation.BOOL,c_void_p,POINTER(win32more.System.ProcessStatus.ENUM_PAGE_FILE_INFORMATION_head),win32more.Foundation.PWSTR, use_last_error=False)
def _define_PENUM_PAGE_FILE_CALLBACKA():
    return CFUNCTYPE(win32more.Foundation.BOOL,c_void_p,POINTER(win32more.System.ProcessStatus.ENUM_PAGE_FILE_INFORMATION_head),win32more.Foundation.PSTR, use_last_error=False)
def _define_K32EnumProcesses():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(UInt32),UInt32,POINTER(UInt32), use_last_error=False)(("K32EnumProcesses", windll["KERNEL32"]), ((1, 'lpidProcess'),(1, 'cb'),(1, 'lpcbNeeded'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_K32EnumProcessModules():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.HINSTANCE),UInt32,POINTER(UInt32), use_last_error=False)(("K32EnumProcessModules", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'lphModule'),(1, 'cb'),(1, 'lpcbNeeded'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_K32EnumProcessModulesEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.HINSTANCE),UInt32,POINTER(UInt32),win32more.System.ProcessStatus.ENUM_PROCESS_MODULES_EX_FLAGS, use_last_error=False)(("K32EnumProcessModulesEx", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'lphModule'),(1, 'cb'),(1, 'lpcbNeeded'),(1, 'dwFilterFlag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_K32GetModuleBaseNameA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.HINSTANCE,POINTER(Byte),UInt32, use_last_error=False)(("K32GetModuleBaseNameA", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'hModule'),(1, 'lpBaseName'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_K32GetModuleBaseNameW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.HINSTANCE,POINTER(Char),UInt32, use_last_error=False)(("K32GetModuleBaseNameW", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'hModule'),(1, 'lpBaseName'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_K32GetModuleBaseName():
    return win32more.System.ProcessStatus.K32GetModuleBaseNameW
def _define_K32GetModuleFileNameExA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.HINSTANCE,POINTER(Byte),UInt32, use_last_error=False)(("K32GetModuleFileNameExA", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'hModule'),(1, 'lpFilename'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_K32GetModuleFileNameExW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.HINSTANCE,POINTER(Char),UInt32, use_last_error=False)(("K32GetModuleFileNameExW", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'hModule'),(1, 'lpFilename'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_K32GetModuleFileNameEx():
    return win32more.System.ProcessStatus.K32GetModuleFileNameExW
def _define_K32GetModuleInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.HINSTANCE,POINTER(win32more.System.ProcessStatus.MODULEINFO_head),UInt32, use_last_error=False)(("K32GetModuleInformation", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'hModule'),(1, 'lpmodinfo'),(1, 'cb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_K32EmptyWorkingSet():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE, use_last_error=False)(("K32EmptyWorkingSet", windll["KERNEL32"]), ((1, 'hProcess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_K32InitializeProcessForWsWatch():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE, use_last_error=False)(("K32InitializeProcessForWsWatch", windll["KERNEL32"]), ((1, 'hProcess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_K32GetWsChanges():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.ProcessStatus.PSAPI_WS_WATCH_INFORMATION_head),UInt32, use_last_error=False)(("K32GetWsChanges", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'lpWatchInfo'),(1, 'cb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_K32GetWsChangesEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.ProcessStatus.PSAPI_WS_WATCH_INFORMATION_EX_head),POINTER(UInt32), use_last_error=False)(("K32GetWsChangesEx", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'lpWatchInfoEx'),(1, 'cb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_K32GetMappedFileNameW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,c_void_p,POINTER(Char),UInt32, use_last_error=False)(("K32GetMappedFileNameW", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'lpv'),(1, 'lpFilename'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_K32GetMappedFileName():
    return win32more.System.ProcessStatus.K32GetMappedFileNameW
def _define_K32GetMappedFileNameA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,c_void_p,POINTER(Byte),UInt32, use_last_error=False)(("K32GetMappedFileNameA", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'lpv'),(1, 'lpFilename'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_K32EnumDeviceDrivers():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(c_void_p),UInt32,POINTER(UInt32), use_last_error=False)(("K32EnumDeviceDrivers", windll["KERNEL32"]), ((1, 'lpImageBase'),(1, 'cb'),(1, 'lpcbNeeded'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_K32GetDeviceDriverBaseNameA():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,POINTER(Byte),UInt32, use_last_error=False)(("K32GetDeviceDriverBaseNameA", windll["KERNEL32"]), ((1, 'ImageBase'),(1, 'lpFilename'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_K32GetDeviceDriverBaseNameW():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,POINTER(Char),UInt32, use_last_error=False)(("K32GetDeviceDriverBaseNameW", windll["KERNEL32"]), ((1, 'ImageBase'),(1, 'lpBaseName'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_K32GetDeviceDriverBaseName():
    return win32more.System.ProcessStatus.K32GetDeviceDriverBaseNameW
def _define_K32GetDeviceDriverFileNameA():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,POINTER(Byte),UInt32, use_last_error=False)(("K32GetDeviceDriverFileNameA", windll["KERNEL32"]), ((1, 'ImageBase'),(1, 'lpFilename'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_K32GetDeviceDriverFileNameW():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,POINTER(Char),UInt32, use_last_error=False)(("K32GetDeviceDriverFileNameW", windll["KERNEL32"]), ((1, 'ImageBase'),(1, 'lpFilename'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_K32GetDeviceDriverFileName():
    return win32more.System.ProcessStatus.K32GetDeviceDriverFileNameW
def _define_K32QueryWorkingSet():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,UInt32, use_last_error=False)(("K32QueryWorkingSet", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'pv'),(1, 'cb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_K32QueryWorkingSetEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,UInt32, use_last_error=False)(("K32QueryWorkingSetEx", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'pv'),(1, 'cb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_K32GetProcessMemoryInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.System.ProcessStatus.PROCESS_MEMORY_COUNTERS_head),UInt32, use_last_error=False)(("K32GetProcessMemoryInfo", windll["KERNEL32"]), ((1, 'Process'),(1, 'ppsmemCounters'),(1, 'cb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_K32GetPerformanceInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.ProcessStatus.PERFORMANCE_INFORMATION_head),UInt32, use_last_error=False)(("K32GetPerformanceInfo", windll["KERNEL32"]), ((1, 'pPerformanceInformation'),(1, 'cb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_K32EnumPageFilesW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.ProcessStatus.PENUM_PAGE_FILE_CALLBACKW,c_void_p, use_last_error=False)(("K32EnumPageFilesW", windll["KERNEL32"]), ((1, 'pCallBackRoutine'),(1, 'pContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_K32EnumPageFiles():
    return win32more.System.ProcessStatus.K32EnumPageFilesW
def _define_K32EnumPageFilesA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.ProcessStatus.PENUM_PAGE_FILE_CALLBACKA,c_void_p, use_last_error=False)(("K32EnumPageFilesA", windll["KERNEL32"]), ((1, 'pCallBackRoutine'),(1, 'pContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_K32GetProcessImageFileNameA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(Byte),UInt32, use_last_error=False)(("K32GetProcessImageFileNameA", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'lpImageFileName'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_K32GetProcessImageFileNameW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(Char),UInt32, use_last_error=False)(("K32GetProcessImageFileNameW", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'lpImageFileName'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_K32GetProcessImageFileName():
    return win32more.System.ProcessStatus.K32GetProcessImageFileNameW
__all__ = [
    "PSAPI_VERSION",
    "ENUM_PROCESS_MODULES_EX_FLAGS",
    "LIST_MODULES_ALL",
    "LIST_MODULES_DEFAULT",
    "LIST_MODULES_32BIT",
    "LIST_MODULES_64BIT",
    "MODULEINFO",
    "PSAPI_WS_WATCH_INFORMATION",
    "PSAPI_WS_WATCH_INFORMATION_EX",
    "PSAPI_WORKING_SET_BLOCK",
    "PSAPI_WORKING_SET_INFORMATION",
    "PSAPI_WORKING_SET_EX_BLOCK",
    "PSAPI_WORKING_SET_EX_INFORMATION",
    "PROCESS_MEMORY_COUNTERS",
    "PROCESS_MEMORY_COUNTERS_EX",
    "PERFORMANCE_INFORMATION",
    "ENUM_PAGE_FILE_INFORMATION",
    "PENUM_PAGE_FILE_CALLBACKW",
    "PENUM_PAGE_FILE_CALLBACKA",
    "K32EnumProcesses",
    "K32EnumProcessModules",
    "K32EnumProcessModulesEx",
    "K32GetModuleBaseNameA",
    "K32GetModuleBaseNameW",
    "K32GetModuleBaseName",
    "K32GetModuleFileNameExA",
    "K32GetModuleFileNameExW",
    "K32GetModuleFileNameEx",
    "K32GetModuleInformation",
    "K32EmptyWorkingSet",
    "K32InitializeProcessForWsWatch",
    "K32GetWsChanges",
    "K32GetWsChangesEx",
    "K32GetMappedFileNameW",
    "K32GetMappedFileName",
    "K32GetMappedFileNameA",
    "K32EnumDeviceDrivers",
    "K32GetDeviceDriverBaseNameA",
    "K32GetDeviceDriverBaseNameW",
    "K32GetDeviceDriverBaseName",
    "K32GetDeviceDriverFileNameA",
    "K32GetDeviceDriverFileNameW",
    "K32GetDeviceDriverFileName",
    "K32QueryWorkingSet",
    "K32QueryWorkingSetEx",
    "K32GetProcessMemoryInfo",
    "K32GetPerformanceInfo",
    "K32EnumPageFilesW",
    "K32EnumPageFiles",
    "K32EnumPageFilesA",
    "K32GetProcessImageFileNameA",
    "K32GetProcessImageFileNameW",
    "K32GetProcessImageFileName",
]
