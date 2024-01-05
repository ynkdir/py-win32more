from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.ProcessStatus
PSAPI_VERSION: UInt32 = 2
@winfunctype('PSAPI.dll')
def EnumProcesses(lpidProcess: POINTER(UInt32), cb: UInt32, lpcbNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('PSAPI.dll')
def EnumProcessModules(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lphModule: POINTER(win32more.Windows.Win32.Foundation.HMODULE), cb: UInt32, lpcbNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('PSAPI.dll')
def EnumProcessModulesEx(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lphModule: POINTER(win32more.Windows.Win32.Foundation.HMODULE), cb: UInt32, lpcbNeeded: POINTER(UInt32), dwFilterFlag: win32more.Windows.Win32.System.ProcessStatus.ENUM_PROCESS_MODULES_EX_FLAGS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('PSAPI.dll')
def GetModuleBaseNameA(hProcess: win32more.Windows.Win32.Foundation.HANDLE, hModule: win32more.Windows.Win32.Foundation.HMODULE, lpBaseName: win32more.Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('PSAPI.dll')
def GetModuleBaseNameW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, hModule: win32more.Windows.Win32.Foundation.HMODULE, lpBaseName: win32more.Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('PSAPI.dll')
def GetModuleFileNameExA(hProcess: win32more.Windows.Win32.Foundation.HANDLE, hModule: win32more.Windows.Win32.Foundation.HMODULE, lpFilename: win32more.Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('PSAPI.dll')
def GetModuleFileNameExW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, hModule: win32more.Windows.Win32.Foundation.HMODULE, lpFilename: win32more.Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('PSAPI.dll')
def GetModuleInformation(hProcess: win32more.Windows.Win32.Foundation.HANDLE, hModule: win32more.Windows.Win32.Foundation.HMODULE, lpmodinfo: POINTER(win32more.Windows.Win32.System.ProcessStatus.MODULEINFO), cb: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('PSAPI.dll')
def EmptyWorkingSet(hProcess: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('PSAPI.dll')
def InitializeProcessForWsWatch(hProcess: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('PSAPI.dll')
def GetWsChanges(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpWatchInfo: POINTER(win32more.Windows.Win32.System.ProcessStatus.PSAPI_WS_WATCH_INFORMATION), cb: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('PSAPI.dll')
def GetWsChangesEx(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpWatchInfoEx: POINTER(win32more.Windows.Win32.System.ProcessStatus.PSAPI_WS_WATCH_INFORMATION_EX), cb: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('PSAPI.dll')
def GetMappedFileNameW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpv: VoidPtr, lpFilename: win32more.Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('PSAPI.dll')
def GetMappedFileNameA(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpv: VoidPtr, lpFilename: win32more.Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('PSAPI.dll')
def EnumDeviceDrivers(lpImageBase: POINTER(VoidPtr), cb: UInt32, lpcbNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('PSAPI.dll')
def GetDeviceDriverBaseNameA(ImageBase: VoidPtr, lpFilename: win32more.Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('PSAPI.dll')
def GetDeviceDriverBaseNameW(ImageBase: VoidPtr, lpBaseName: win32more.Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('PSAPI.dll')
def GetDeviceDriverFileNameA(ImageBase: VoidPtr, lpFilename: win32more.Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('PSAPI.dll')
def GetDeviceDriverFileNameW(ImageBase: VoidPtr, lpFilename: win32more.Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('PSAPI.dll')
def QueryWorkingSet(hProcess: win32more.Windows.Win32.Foundation.HANDLE, pv: VoidPtr, cb: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('PSAPI.dll')
def QueryWorkingSetEx(hProcess: win32more.Windows.Win32.Foundation.HANDLE, pv: VoidPtr, cb: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('PSAPI.dll')
def GetProcessMemoryInfo(Process: win32more.Windows.Win32.Foundation.HANDLE, ppsmemCounters: POINTER(win32more.Windows.Win32.System.ProcessStatus.PROCESS_MEMORY_COUNTERS), cb: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('PSAPI.dll')
def GetPerformanceInfo(pPerformanceInformation: POINTER(win32more.Windows.Win32.System.ProcessStatus.PERFORMANCE_INFORMATION), cb: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('PSAPI.dll')
def EnumPageFilesW(pCallBackRoutine: win32more.Windows.Win32.System.ProcessStatus.PENUM_PAGE_FILE_CALLBACKW, pContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('PSAPI.dll')
def EnumPageFilesA(pCallBackRoutine: win32more.Windows.Win32.System.ProcessStatus.PENUM_PAGE_FILE_CALLBACKA, pContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('PSAPI.dll')
def GetProcessImageFileNameA(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpImageFileName: win32more.Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('PSAPI.dll')
def GetProcessImageFileNameW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpImageFileName: win32more.Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def K32EnumProcesses(lpidProcess: POINTER(UInt32), cb: UInt32, lpcbNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32EnumProcessModules(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lphModule: POINTER(win32more.Windows.Win32.Foundation.HMODULE), cb: UInt32, lpcbNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32EnumProcessModulesEx(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lphModule: POINTER(win32more.Windows.Win32.Foundation.HMODULE), cb: UInt32, lpcbNeeded: POINTER(UInt32), dwFilterFlag: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32GetModuleBaseNameA(hProcess: win32more.Windows.Win32.Foundation.HANDLE, hModule: win32more.Windows.Win32.Foundation.HMODULE, lpBaseName: win32more.Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def K32GetModuleBaseNameW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, hModule: win32more.Windows.Win32.Foundation.HMODULE, lpBaseName: win32more.Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def K32GetModuleFileNameExA(hProcess: win32more.Windows.Win32.Foundation.HANDLE, hModule: win32more.Windows.Win32.Foundation.HMODULE, lpFilename: win32more.Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def K32GetModuleFileNameExW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, hModule: win32more.Windows.Win32.Foundation.HMODULE, lpFilename: win32more.Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def K32GetModuleInformation(hProcess: win32more.Windows.Win32.Foundation.HANDLE, hModule: win32more.Windows.Win32.Foundation.HMODULE, lpmodinfo: POINTER(win32more.Windows.Win32.System.ProcessStatus.MODULEINFO), cb: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32EmptyWorkingSet(hProcess: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32InitializeProcessForWsWatch(hProcess: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32GetWsChanges(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpWatchInfo: POINTER(win32more.Windows.Win32.System.ProcessStatus.PSAPI_WS_WATCH_INFORMATION), cb: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32GetWsChangesEx(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpWatchInfoEx: POINTER(win32more.Windows.Win32.System.ProcessStatus.PSAPI_WS_WATCH_INFORMATION_EX), cb: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32GetMappedFileNameW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpv: VoidPtr, lpFilename: win32more.Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def K32GetMappedFileNameA(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpv: VoidPtr, lpFilename: win32more.Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def K32EnumDeviceDrivers(lpImageBase: POINTER(VoidPtr), cb: UInt32, lpcbNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32GetDeviceDriverBaseNameA(ImageBase: VoidPtr, lpFilename: win32more.Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def K32GetDeviceDriverBaseNameW(ImageBase: VoidPtr, lpBaseName: win32more.Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def K32GetDeviceDriverFileNameA(ImageBase: VoidPtr, lpFilename: win32more.Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def K32GetDeviceDriverFileNameW(ImageBase: VoidPtr, lpFilename: win32more.Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def K32QueryWorkingSet(hProcess: win32more.Windows.Win32.Foundation.HANDLE, pv: VoidPtr, cb: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32QueryWorkingSetEx(hProcess: win32more.Windows.Win32.Foundation.HANDLE, pv: VoidPtr, cb: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32GetProcessMemoryInfo(Process: win32more.Windows.Win32.Foundation.HANDLE, ppsmemCounters: POINTER(win32more.Windows.Win32.System.ProcessStatus.PROCESS_MEMORY_COUNTERS), cb: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32GetPerformanceInfo(pPerformanceInformation: POINTER(win32more.Windows.Win32.System.ProcessStatus.PERFORMANCE_INFORMATION), cb: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32EnumPageFilesW(pCallBackRoutine: win32more.Windows.Win32.System.ProcessStatus.PENUM_PAGE_FILE_CALLBACKW, pContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32EnumPageFilesA(pCallBackRoutine: win32more.Windows.Win32.System.ProcessStatus.PENUM_PAGE_FILE_CALLBACKA, pContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32GetProcessImageFileNameA(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpImageFileName: win32more.Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def K32GetProcessImageFileNameW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpImageFileName: win32more.Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
class ENUM_PAGE_FILE_INFORMATION(EasyCastStructure):
    cb: UInt32
    Reserved: UInt32
    TotalSize: UIntPtr
    TotalInUse: UIntPtr
    PeakUsage: UIntPtr
ENUM_PROCESS_MODULES_EX_FLAGS = UInt32
LIST_MODULES_ALL: win32more.Windows.Win32.System.ProcessStatus.ENUM_PROCESS_MODULES_EX_FLAGS = 3
LIST_MODULES_DEFAULT: win32more.Windows.Win32.System.ProcessStatus.ENUM_PROCESS_MODULES_EX_FLAGS = 0
LIST_MODULES_32BIT: win32more.Windows.Win32.System.ProcessStatus.ENUM_PROCESS_MODULES_EX_FLAGS = 1
LIST_MODULES_64BIT: win32more.Windows.Win32.System.ProcessStatus.ENUM_PROCESS_MODULES_EX_FLAGS = 2
class MODULEINFO(EasyCastStructure):
    lpBaseOfDll: VoidPtr
    SizeOfImage: UInt32
    EntryPoint: VoidPtr
@winfunctype_pointer
def PENUM_PAGE_FILE_CALLBACKA(pContext: VoidPtr, pPageFileInfo: POINTER(win32more.Windows.Win32.System.ProcessStatus.ENUM_PAGE_FILE_INFORMATION), lpFilename: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PENUM_PAGE_FILE_CALLBACKW(pContext: VoidPtr, pPageFileInfo: POINTER(win32more.Windows.Win32.System.ProcessStatus.ENUM_PAGE_FILE_INFORMATION), lpFilename: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
class PERFORMANCE_INFORMATION(EasyCastStructure):
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
class PROCESS_MEMORY_COUNTERS(EasyCastStructure):
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
class PROCESS_MEMORY_COUNTERS_EX(EasyCastStructure):
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
class PSAPI_WORKING_SET_BLOCK(EasyCastUnion):
    Flags: UIntPtr
    Anonymous: _Anonymous_e__Struct
    class _Anonymous_e__Struct(EasyCastStructure):
        _bitfield: UIntPtr
class PSAPI_WORKING_SET_EX_BLOCK(EasyCastUnion):
    Flags: UIntPtr
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        Invalid: _Invalid_e__Struct
        class _Anonymous_e__Struct(EasyCastStructure):
            _bitfield: UIntPtr
        class _Invalid_e__Struct(EasyCastStructure):
            _bitfield: UIntPtr
class PSAPI_WORKING_SET_EX_INFORMATION(EasyCastStructure):
    VirtualAddress: VoidPtr
    VirtualAttributes: win32more.Windows.Win32.System.ProcessStatus.PSAPI_WORKING_SET_EX_BLOCK
class PSAPI_WORKING_SET_INFORMATION(EasyCastStructure):
    NumberOfEntries: UIntPtr
    WorkingSetInfo: win32more.Windows.Win32.System.ProcessStatus.PSAPI_WORKING_SET_BLOCK * 1
class PSAPI_WS_WATCH_INFORMATION(EasyCastStructure):
    FaultingPc: VoidPtr
    FaultingVa: VoidPtr
class PSAPI_WS_WATCH_INFORMATION_EX(EasyCastStructure):
    BasicInfo: win32more.Windows.Win32.System.ProcessStatus.PSAPI_WS_WATCH_INFORMATION
    FaultingThreadId: UIntPtr
    Flags: UIntPtr


make_ready(__name__)
