from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
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
GetModuleBaseName = UnicodeAlias('GetModuleBaseNameW')
@winfunctype('PSAPI.dll')
def GetModuleFileNameExA(hProcess: win32more.Windows.Win32.Foundation.HANDLE, hModule: win32more.Windows.Win32.Foundation.HMODULE, lpFilename: win32more.Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('PSAPI.dll')
def GetModuleFileNameExW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, hModule: win32more.Windows.Win32.Foundation.HMODULE, lpFilename: win32more.Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
GetModuleFileNameEx = UnicodeAlias('GetModuleFileNameExW')
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
GetMappedFileName = UnicodeAlias('GetMappedFileNameW')
@winfunctype('PSAPI.dll')
def GetMappedFileNameA(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpv: VoidPtr, lpFilename: win32more.Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('PSAPI.dll')
def EnumDeviceDrivers(lpImageBase: POINTER(VoidPtr), cb: UInt32, lpcbNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('PSAPI.dll')
def GetDeviceDriverBaseNameA(ImageBase: VoidPtr, lpFilename: win32more.Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('PSAPI.dll')
def GetDeviceDriverBaseNameW(ImageBase: VoidPtr, lpBaseName: win32more.Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
GetDeviceDriverBaseName = UnicodeAlias('GetDeviceDriverBaseNameW')
@winfunctype('PSAPI.dll')
def GetDeviceDriverFileNameA(ImageBase: VoidPtr, lpFilename: win32more.Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('PSAPI.dll')
def GetDeviceDriverFileNameW(ImageBase: VoidPtr, lpFilename: win32more.Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
GetDeviceDriverFileName = UnicodeAlias('GetDeviceDriverFileNameW')
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
EnumPageFiles = UnicodeAlias('EnumPageFilesW')
@winfunctype('PSAPI.dll')
def EnumPageFilesA(pCallBackRoutine: win32more.Windows.Win32.System.ProcessStatus.PENUM_PAGE_FILE_CALLBACKA, pContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('PSAPI.dll')
def GetProcessImageFileNameA(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpImageFileName: win32more.Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('PSAPI.dll')
def GetProcessImageFileNameW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpImageFileName: win32more.Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
GetProcessImageFileName = UnicodeAlias('GetProcessImageFileNameW')
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
K32GetModuleBaseName = UnicodeAlias('K32GetModuleBaseNameW')
@winfunctype('KERNEL32.dll')
def K32GetModuleFileNameExA(hProcess: win32more.Windows.Win32.Foundation.HANDLE, hModule: win32more.Windows.Win32.Foundation.HMODULE, lpFilename: win32more.Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def K32GetModuleFileNameExW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, hModule: win32more.Windows.Win32.Foundation.HMODULE, lpFilename: win32more.Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
K32GetModuleFileNameEx = UnicodeAlias('K32GetModuleFileNameExW')
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
K32GetMappedFileName = UnicodeAlias('K32GetMappedFileNameW')
@winfunctype('KERNEL32.dll')
def K32GetMappedFileNameA(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpv: VoidPtr, lpFilename: win32more.Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def K32EnumDeviceDrivers(lpImageBase: POINTER(VoidPtr), cb: UInt32, lpcbNeeded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32GetDeviceDriverBaseNameA(ImageBase: VoidPtr, lpFilename: win32more.Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def K32GetDeviceDriverBaseNameW(ImageBase: VoidPtr, lpBaseName: win32more.Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
K32GetDeviceDriverBaseName = UnicodeAlias('K32GetDeviceDriverBaseNameW')
@winfunctype('KERNEL32.dll')
def K32GetDeviceDriverFileNameA(ImageBase: VoidPtr, lpFilename: win32more.Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def K32GetDeviceDriverFileNameW(ImageBase: VoidPtr, lpFilename: win32more.Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
K32GetDeviceDriverFileName = UnicodeAlias('K32GetDeviceDriverFileNameW')
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
K32EnumPageFiles = UnicodeAlias('K32EnumPageFilesW')
@winfunctype('KERNEL32.dll')
def K32EnumPageFilesA(pCallBackRoutine: win32more.Windows.Win32.System.ProcessStatus.PENUM_PAGE_FILE_CALLBACKA, pContext: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def K32GetProcessImageFileNameA(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpImageFileName: win32more.Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def K32GetProcessImageFileNameW(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpImageFileName: win32more.Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
K32GetProcessImageFileName = UnicodeAlias('K32GetProcessImageFileNameW')
class ENUM_PAGE_FILE_INFORMATION(Structure):
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
class MODULEINFO(Structure):
    lpBaseOfDll: VoidPtr
    SizeOfImage: UInt32
    EntryPoint: VoidPtr
@winfunctype_pointer
def PENUM_PAGE_FILE_CALLBACKA(pContext: VoidPtr, pPageFileInfo: POINTER(win32more.Windows.Win32.System.ProcessStatus.ENUM_PAGE_FILE_INFORMATION), lpFilename: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PENUM_PAGE_FILE_CALLBACKW(pContext: VoidPtr, pPageFileInfo: POINTER(win32more.Windows.Win32.System.ProcessStatus.ENUM_PAGE_FILE_INFORMATION), lpFilename: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PENUM_PAGE_FILE_CALLBACK = UnicodeAlias('PENUM_PAGE_FILE_CALLBACKW')
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
class PROCESS_MEMORY_COUNTERS_EX2(Structure):
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
    PrivateWorkingSetSize: UIntPtr
    SharedCommitUsage: UInt64
class PSAPI_WORKING_SET_BLOCK(Union):
    Flags: UIntPtr
    Anonymous: _Anonymous_e__Struct
    class _Anonymous_e__Struct(Structure):
        Protection: Annotated[UIntPtr, 5]
        ShareCount: Annotated[UIntPtr, 3]
        Shared: Annotated[UIntPtr, 1]
        Reserved: Annotated[UIntPtr, 3]
        VirtualPage: Annotated[UIntPtr, 20]
class PSAPI_WORKING_SET_EX_BLOCK(Union):
    Flags: UIntPtr
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        Invalid: _Invalid_e__Struct
        class _Anonymous_e__Struct(Structure):
            Valid: Annotated[UIntPtr, 1]
            ShareCount: Annotated[UIntPtr, 3]
            Win32Protection: Annotated[UIntPtr, 11]
            Shared: Annotated[UIntPtr, 1]
            Node: Annotated[UIntPtr, 6]
            Locked: Annotated[UIntPtr, 1]
            LargePage: Annotated[UIntPtr, 1]
            Reserved: Annotated[UIntPtr, 7]
            Bad: Annotated[UIntPtr, 1]
        class _Invalid_e__Struct(Structure):
            Valid: Annotated[UIntPtr, 1]
            Reserved0: Annotated[UIntPtr, 14]
            Shared: Annotated[UIntPtr, 1]
            Reserved1: Annotated[UIntPtr, 15]
            Bad: Annotated[UIntPtr, 1]
class PSAPI_WORKING_SET_EX_INFORMATION(Structure):
    VirtualAddress: VoidPtr
    VirtualAttributes: win32more.Windows.Win32.System.ProcessStatus.PSAPI_WORKING_SET_EX_BLOCK
class PSAPI_WORKING_SET_INFORMATION(Structure):
    NumberOfEntries: UIntPtr
    WorkingSetInfo: win32more.Windows.Win32.System.ProcessStatus.PSAPI_WORKING_SET_BLOCK * 1
class PSAPI_WS_WATCH_INFORMATION(Structure):
    FaultingPc: VoidPtr
    FaultingVa: VoidPtr
class PSAPI_WS_WATCH_INFORMATION_EX(Structure):
    BasicInfo: win32more.Windows.Win32.System.ProcessStatus.PSAPI_WS_WATCH_INFORMATION
    FaultingThreadId: UIntPtr
    Flags: UIntPtr


make_ready(__name__)
