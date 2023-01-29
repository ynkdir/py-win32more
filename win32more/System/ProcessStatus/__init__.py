from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.ProcessStatus
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
PSAPI_VERSION: UInt32 = 2
@winfunctype('KERNEL32.dll')
def K32EnumProcesses(lpidProcess: POINTER(UInt32), cb: UInt32, lpcbNeeded: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32EnumProcessModules(hProcess: win32more.Foundation.HANDLE, lphModule: POINTER(win32more.Foundation.HINSTANCE), cb: UInt32, lpcbNeeded: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32EnumProcessModulesEx(hProcess: win32more.Foundation.HANDLE, lphModule: POINTER(win32more.Foundation.HINSTANCE), cb: UInt32, lpcbNeeded: POINTER(UInt32), dwFilterFlag: win32more.System.ProcessStatus.ENUM_PROCESS_MODULES_EX_FLAGS) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32GetModuleBaseNameA(hProcess: win32more.Foundation.HANDLE, hModule: win32more.Foundation.HINSTANCE, lpBaseName: win32more.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def K32GetModuleBaseNameW(hProcess: win32more.Foundation.HANDLE, hModule: win32more.Foundation.HINSTANCE, lpBaseName: win32more.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def K32GetModuleFileNameExA(hProcess: win32more.Foundation.HANDLE, hModule: win32more.Foundation.HINSTANCE, lpFilename: win32more.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def K32GetModuleFileNameExW(hProcess: win32more.Foundation.HANDLE, hModule: win32more.Foundation.HINSTANCE, lpFilename: win32more.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def K32GetModuleInformation(hProcess: win32more.Foundation.HANDLE, hModule: win32more.Foundation.HINSTANCE, lpmodinfo: POINTER(win32more.System.ProcessStatus.MODULEINFO_head), cb: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32EmptyWorkingSet(hProcess: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32InitializeProcessForWsWatch(hProcess: win32more.Foundation.HANDLE) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32GetWsChanges(hProcess: win32more.Foundation.HANDLE, lpWatchInfo: POINTER(win32more.System.ProcessStatus.PSAPI_WS_WATCH_INFORMATION_head), cb: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32GetWsChangesEx(hProcess: win32more.Foundation.HANDLE, lpWatchInfoEx: POINTER(win32more.System.ProcessStatus.PSAPI_WS_WATCH_INFORMATION_EX_head), cb: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32GetMappedFileNameW(hProcess: win32more.Foundation.HANDLE, lpv: c_void_p, lpFilename: win32more.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def K32GetMappedFileNameA(hProcess: win32more.Foundation.HANDLE, lpv: c_void_p, lpFilename: win32more.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def K32EnumDeviceDrivers(lpImageBase: POINTER(c_void_p), cb: UInt32, lpcbNeeded: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32GetDeviceDriverBaseNameA(ImageBase: c_void_p, lpFilename: win32more.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def K32GetDeviceDriverBaseNameW(ImageBase: c_void_p, lpBaseName: win32more.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def K32GetDeviceDriverFileNameA(ImageBase: c_void_p, lpFilename: win32more.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def K32GetDeviceDriverFileNameW(ImageBase: c_void_p, lpFilename: win32more.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def K32QueryWorkingSet(hProcess: win32more.Foundation.HANDLE, pv: c_void_p, cb: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32QueryWorkingSetEx(hProcess: win32more.Foundation.HANDLE, pv: c_void_p, cb: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32GetProcessMemoryInfo(Process: win32more.Foundation.HANDLE, ppsmemCounters: POINTER(win32more.System.ProcessStatus.PROCESS_MEMORY_COUNTERS_head), cb: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32GetPerformanceInfo(pPerformanceInformation: POINTER(win32more.System.ProcessStatus.PERFORMANCE_INFORMATION_head), cb: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32EnumPageFilesW(pCallBackRoutine: win32more.System.ProcessStatus.PENUM_PAGE_FILE_CALLBACKW, pContext: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32EnumPageFilesA(pCallBackRoutine: win32more.System.ProcessStatus.PENUM_PAGE_FILE_CALLBACKA, pContext: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32GetProcessImageFileNameA(hProcess: win32more.Foundation.HANDLE, lpImageFileName: win32more.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def K32GetProcessImageFileNameW(hProcess: win32more.Foundation.HANDLE, lpImageFileName: win32more.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
class ENUM_PAGE_FILE_INFORMATION(Structure):
    cb: UInt32
    Reserved: UInt32
    TotalSize: UIntPtr
    TotalInUse: UIntPtr
    PeakUsage: UIntPtr
ENUM_PROCESS_MODULES_EX_FLAGS = UInt32
LIST_MODULES_ALL: ENUM_PROCESS_MODULES_EX_FLAGS = 3
LIST_MODULES_DEFAULT: ENUM_PROCESS_MODULES_EX_FLAGS = 0
LIST_MODULES_32BIT: ENUM_PROCESS_MODULES_EX_FLAGS = 1
LIST_MODULES_64BIT: ENUM_PROCESS_MODULES_EX_FLAGS = 2
class MODULEINFO(Structure):
    lpBaseOfDll: c_void_p
    SizeOfImage: UInt32
    EntryPoint: c_void_p
@winfunctype_pointer
def PENUM_PAGE_FILE_CALLBACKA(pContext: c_void_p, pPageFileInfo: POINTER(win32more.System.ProcessStatus.ENUM_PAGE_FILE_INFORMATION_head), lpFilename: win32more.Foundation.PSTR) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def PENUM_PAGE_FILE_CALLBACKW(pContext: c_void_p, pPageFileInfo: POINTER(win32more.System.ProcessStatus.ENUM_PAGE_FILE_INFORMATION_head), lpFilename: win32more.Foundation.PWSTR) -> win32more.Foundation.BOOL: ...
class PERFORMANCE_INFORMATION(Structure):
    cb: UInt32
    CommitTotal: UIntPtr
    CommitLimit: UIntPtr
    CommitPeak: UIntPtr
    PhysicalTotal: UIntPtr
    PhysicalAvailable: UIntPtr
    SystemCache: UIntPtr
    KernelTotal: UIntPtr
    KernelPaged: UIntPtr
    KernelNonpaged: UIntPtr
    PageSize: UIntPtr
    HandleCount: UInt32
    ProcessCount: UInt32
    ThreadCount: UInt32
class PROCESS_MEMORY_COUNTERS(Structure):
    cb: UInt32
    PageFaultCount: UInt32
    PeakWorkingSetSize: UIntPtr
    WorkingSetSize: UIntPtr
    QuotaPeakPagedPoolUsage: UIntPtr
    QuotaPagedPoolUsage: UIntPtr
    QuotaPeakNonPagedPoolUsage: UIntPtr
    QuotaNonPagedPoolUsage: UIntPtr
    PagefileUsage: UIntPtr
    PeakPagefileUsage: UIntPtr
class PROCESS_MEMORY_COUNTERS_EX(Structure):
    cb: UInt32
    PageFaultCount: UInt32
    PeakWorkingSetSize: UIntPtr
    WorkingSetSize: UIntPtr
    QuotaPeakPagedPoolUsage: UIntPtr
    QuotaPagedPoolUsage: UIntPtr
    QuotaPeakNonPagedPoolUsage: UIntPtr
    QuotaNonPagedPoolUsage: UIntPtr
    PagefileUsage: UIntPtr
    PeakPagefileUsage: UIntPtr
    PrivateUsage: UIntPtr
class PSAPI_WORKING_SET_BLOCK(Union):
    Flags: UIntPtr
    Anonymous: _Anonymous_e__Struct
    class _Anonymous_e__Struct(Structure):
        _bitfield: UIntPtr
class PSAPI_WORKING_SET_EX_BLOCK(Union):
    Flags: UIntPtr
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        Invalid: _Invalid_e__Struct
        class _Anonymous_e__Struct(Structure):
            _bitfield: UIntPtr
        class _Invalid_e__Struct(Structure):
            _bitfield: UIntPtr
class PSAPI_WORKING_SET_EX_INFORMATION(Structure):
    VirtualAddress: c_void_p
    VirtualAttributes: win32more.System.ProcessStatus.PSAPI_WORKING_SET_EX_BLOCK
class PSAPI_WORKING_SET_INFORMATION(Structure):
    NumberOfEntries: UIntPtr
    WorkingSetInfo: win32more.System.ProcessStatus.PSAPI_WORKING_SET_BLOCK * 1
class PSAPI_WS_WATCH_INFORMATION(Structure):
    FaultingPc: c_void_p
    FaultingVa: c_void_p
class PSAPI_WS_WATCH_INFORMATION_EX(Structure):
    BasicInfo: win32more.System.ProcessStatus.PSAPI_WS_WATCH_INFORMATION
    FaultingThreadId: UIntPtr
    Flags: UIntPtr
make_head(_module, 'ENUM_PAGE_FILE_INFORMATION')
make_head(_module, 'MODULEINFO')
make_head(_module, 'PENUM_PAGE_FILE_CALLBACKA')
make_head(_module, 'PENUM_PAGE_FILE_CALLBACKW')
make_head(_module, 'PERFORMANCE_INFORMATION')
make_head(_module, 'PROCESS_MEMORY_COUNTERS')
make_head(_module, 'PROCESS_MEMORY_COUNTERS_EX')
make_head(_module, 'PSAPI_WORKING_SET_BLOCK')
make_head(_module, 'PSAPI_WORKING_SET_EX_BLOCK')
make_head(_module, 'PSAPI_WORKING_SET_EX_INFORMATION')
make_head(_module, 'PSAPI_WORKING_SET_INFORMATION')
make_head(_module, 'PSAPI_WS_WATCH_INFORMATION')
make_head(_module, 'PSAPI_WS_WATCH_INFORMATION_EX')
__all__ = [
    "ENUM_PAGE_FILE_INFORMATION",
    "ENUM_PROCESS_MODULES_EX_FLAGS",
    "K32EmptyWorkingSet",
    "K32EnumDeviceDrivers",
    "K32EnumPageFilesA",
    "K32EnumPageFilesW",
    "K32EnumProcessModules",
    "K32EnumProcessModulesEx",
    "K32EnumProcesses",
    "K32GetDeviceDriverBaseNameA",
    "K32GetDeviceDriverBaseNameW",
    "K32GetDeviceDriverFileNameA",
    "K32GetDeviceDriverFileNameW",
    "K32GetMappedFileNameA",
    "K32GetMappedFileNameW",
    "K32GetModuleBaseNameA",
    "K32GetModuleBaseNameW",
    "K32GetModuleFileNameExA",
    "K32GetModuleFileNameExW",
    "K32GetModuleInformation",
    "K32GetPerformanceInfo",
    "K32GetProcessImageFileNameA",
    "K32GetProcessImageFileNameW",
    "K32GetProcessMemoryInfo",
    "K32GetWsChanges",
    "K32GetWsChangesEx",
    "K32InitializeProcessForWsWatch",
    "K32QueryWorkingSet",
    "K32QueryWorkingSetEx",
    "LIST_MODULES_32BIT",
    "LIST_MODULES_64BIT",
    "LIST_MODULES_ALL",
    "LIST_MODULES_DEFAULT",
    "MODULEINFO",
    "PENUM_PAGE_FILE_CALLBACKA",
    "PENUM_PAGE_FILE_CALLBACKW",
    "PERFORMANCE_INFORMATION",
    "PROCESS_MEMORY_COUNTERS",
    "PROCESS_MEMORY_COUNTERS_EX",
    "PSAPI_VERSION",
    "PSAPI_WORKING_SET_BLOCK",
    "PSAPI_WORKING_SET_EX_BLOCK",
    "PSAPI_WORKING_SET_EX_INFORMATION",
    "PSAPI_WORKING_SET_INFORMATION",
    "PSAPI_WS_WATCH_INFORMATION",
    "PSAPI_WS_WATCH_INFORMATION_EX",
]
_arch_optional = [
]
