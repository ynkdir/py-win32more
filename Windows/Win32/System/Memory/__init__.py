from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Foundation
import Windows.Win32.Security
import Windows.Win32.System.Memory
import Windows.Win32.UI.WindowsAndMessaging
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
FILE_CACHE_MAX_HARD_ENABLE: UInt32 = 1
FILE_CACHE_MAX_HARD_DISABLE: UInt32 = 2
FILE_CACHE_MIN_HARD_ENABLE: UInt32 = 4
FILE_CACHE_MIN_HARD_DISABLE: UInt32 = 8
MEHC_PATROL_SCRUBBER_PRESENT: UInt32 = 1
@winfunctype('KERNEL32.dll')
def HeapCreate(flOptions: Windows.Win32.System.Memory.HEAP_FLAGS, dwInitialSize: UIntPtr, dwMaximumSize: UIntPtr) -> Windows.Win32.System.Memory.HeapHandle: ...
@winfunctype('KERNEL32.dll')
def HeapDestroy(hHeap: Windows.Win32.System.Memory.HeapHandle) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def HeapAlloc(hHeap: Windows.Win32.System.Memory.HeapHandle, dwFlags: Windows.Win32.System.Memory.HEAP_FLAGS, dwBytes: UIntPtr) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def HeapReAlloc(hHeap: Windows.Win32.System.Memory.HeapHandle, dwFlags: Windows.Win32.System.Memory.HEAP_FLAGS, lpMem: c_void_p, dwBytes: UIntPtr) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def HeapFree(hHeap: Windows.Win32.System.Memory.HeapHandle, dwFlags: Windows.Win32.System.Memory.HEAP_FLAGS, lpMem: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def HeapSize(hHeap: Windows.Win32.System.Memory.HeapHandle, dwFlags: Windows.Win32.System.Memory.HEAP_FLAGS, lpMem: c_void_p) -> UIntPtr: ...
@winfunctype('KERNEL32.dll')
def GetProcessHeap() -> Windows.Win32.System.Memory.HeapHandle: ...
@winfunctype('KERNEL32.dll')
def HeapCompact(hHeap: Windows.Win32.System.Memory.HeapHandle, dwFlags: Windows.Win32.System.Memory.HEAP_FLAGS) -> UIntPtr: ...
@winfunctype('KERNEL32.dll')
def HeapSetInformation(HeapHandle: Windows.Win32.System.Memory.HeapHandle, HeapInformationClass: Windows.Win32.System.Memory.HEAP_INFORMATION_CLASS, HeapInformation: c_void_p, HeapInformationLength: UIntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def HeapValidate(hHeap: Windows.Win32.System.Memory.HeapHandle, dwFlags: Windows.Win32.System.Memory.HEAP_FLAGS, lpMem: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def HeapSummary(hHeap: Windows.Win32.Foundation.HANDLE, dwFlags: UInt32, lpSummary: POINTER(Windows.Win32.System.Memory.HEAP_SUMMARY_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProcessHeaps(NumberOfHeaps: UInt32, ProcessHeaps: POINTER(Windows.Win32.System.Memory.HeapHandle_head)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def HeapLock(hHeap: Windows.Win32.System.Memory.HeapHandle) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def HeapUnlock(hHeap: Windows.Win32.System.Memory.HeapHandle) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def HeapWalk(hHeap: Windows.Win32.System.Memory.HeapHandle, lpEntry: POINTER(Windows.Win32.System.Memory.PROCESS_HEAP_ENTRY_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def HeapQueryInformation(HeapHandle: Windows.Win32.System.Memory.HeapHandle, HeapInformationClass: Windows.Win32.System.Memory.HEAP_INFORMATION_CLASS, HeapInformation: c_void_p, HeapInformationLength: UIntPtr, ReturnLength: POINTER(UIntPtr)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def VirtualAlloc(lpAddress: c_void_p, dwSize: UIntPtr, flAllocationType: Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE, flProtect: Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def VirtualProtect(lpAddress: c_void_p, dwSize: UIntPtr, flNewProtect: Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS, lpflOldProtect: POINTER(Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def VirtualFree(lpAddress: c_void_p, dwSize: UIntPtr, dwFreeType: Windows.Win32.System.Memory.VIRTUAL_FREE_TYPE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def VirtualQuery(lpAddress: c_void_p, lpBuffer: POINTER(Windows.Win32.System.Memory.MEMORY_BASIC_INFORMATION_head), dwLength: UIntPtr) -> UIntPtr: ...
@winfunctype('KERNEL32.dll')
def VirtualAllocEx(hProcess: Windows.Win32.Foundation.HANDLE, lpAddress: c_void_p, dwSize: UIntPtr, flAllocationType: Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE, flProtect: Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def VirtualProtectEx(hProcess: Windows.Win32.Foundation.HANDLE, lpAddress: c_void_p, dwSize: UIntPtr, flNewProtect: Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS, lpflOldProtect: POINTER(Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def VirtualQueryEx(hProcess: Windows.Win32.Foundation.HANDLE, lpAddress: c_void_p, lpBuffer: POINTER(Windows.Win32.System.Memory.MEMORY_BASIC_INFORMATION_head), dwLength: UIntPtr) -> UIntPtr: ...
@winfunctype('KERNEL32.dll')
def CreateFileMappingW(hFile: Windows.Win32.Foundation.HANDLE, lpFileMappingAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), flProtect: Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS, dwMaximumSizeHigh: UInt32, dwMaximumSizeLow: UInt32, lpName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def OpenFileMappingW(dwDesiredAccess: UInt32, bInheritHandle: Windows.Win32.Foundation.BOOL, lpName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def MapViewOfFile(hFileMappingObject: Windows.Win32.Foundation.HANDLE, dwDesiredAccess: Windows.Win32.System.Memory.FILE_MAP, dwFileOffsetHigh: UInt32, dwFileOffsetLow: UInt32, dwNumberOfBytesToMap: UIntPtr) -> Windows.Win32.System.Memory.MEMORY_MAPPED_VIEW_ADDRESS: ...
@winfunctype('KERNEL32.dll')
def MapViewOfFileEx(hFileMappingObject: Windows.Win32.Foundation.HANDLE, dwDesiredAccess: Windows.Win32.System.Memory.FILE_MAP, dwFileOffsetHigh: UInt32, dwFileOffsetLow: UInt32, dwNumberOfBytesToMap: UIntPtr, lpBaseAddress: c_void_p) -> Windows.Win32.System.Memory.MEMORY_MAPPED_VIEW_ADDRESS: ...
@winfunctype('KERNEL32.dll')
def VirtualFreeEx(hProcess: Windows.Win32.Foundation.HANDLE, lpAddress: c_void_p, dwSize: UIntPtr, dwFreeType: Windows.Win32.System.Memory.VIRTUAL_FREE_TYPE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FlushViewOfFile(lpBaseAddress: c_void_p, dwNumberOfBytesToFlush: UIntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def UnmapViewOfFile(lpBaseAddress: Windows.Win32.System.Memory.MEMORY_MAPPED_VIEW_ADDRESS) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetLargePageMinimum() -> UIntPtr: ...
@winfunctype('KERNEL32.dll')
def GetProcessWorkingSetSizeEx(hProcess: Windows.Win32.Foundation.HANDLE, lpMinimumWorkingSetSize: POINTER(UIntPtr), lpMaximumWorkingSetSize: POINTER(UIntPtr), Flags: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetProcessWorkingSetSizeEx(hProcess: Windows.Win32.Foundation.HANDLE, dwMinimumWorkingSetSize: UIntPtr, dwMaximumWorkingSetSize: UIntPtr, Flags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def VirtualLock(lpAddress: c_void_p, dwSize: UIntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def VirtualUnlock(lpAddress: c_void_p, dwSize: UIntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetWriteWatch(dwFlags: UInt32, lpBaseAddress: c_void_p, dwRegionSize: UIntPtr, lpAddresses: POINTER(c_void_p), lpdwCount: POINTER(UIntPtr), lpdwGranularity: POINTER(UInt32)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def ResetWriteWatch(lpBaseAddress: c_void_p, dwRegionSize: UIntPtr) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def CreateMemoryResourceNotification(NotificationType: Windows.Win32.System.Memory.MEMORY_RESOURCE_NOTIFICATION_TYPE) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def QueryMemoryResourceNotification(ResourceNotificationHandle: Windows.Win32.Foundation.HANDLE, ResourceState: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetSystemFileCacheSize(lpMinimumFileCacheSize: POINTER(UIntPtr), lpMaximumFileCacheSize: POINTER(UIntPtr), lpFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetSystemFileCacheSize(MinimumFileCacheSize: UIntPtr, MaximumFileCacheSize: UIntPtr, Flags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateFileMappingNumaW(hFile: Windows.Win32.Foundation.HANDLE, lpFileMappingAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), flProtect: Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS, dwMaximumSizeHigh: UInt32, dwMaximumSizeLow: UInt32, lpName: Windows.Win32.Foundation.PWSTR, nndPreferred: UInt32) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def PrefetchVirtualMemory(hProcess: Windows.Win32.Foundation.HANDLE, NumberOfEntries: UIntPtr, VirtualAddresses: POINTER(Windows.Win32.System.Memory.WIN32_MEMORY_RANGE_ENTRY_head), Flags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateFileMappingFromApp(hFile: Windows.Win32.Foundation.HANDLE, SecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), PageProtection: Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS, MaximumSize: UInt64, Name: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def MapViewOfFileFromApp(hFileMappingObject: Windows.Win32.Foundation.HANDLE, DesiredAccess: Windows.Win32.System.Memory.FILE_MAP, FileOffset: UInt64, NumberOfBytesToMap: UIntPtr) -> Windows.Win32.System.Memory.MEMORY_MAPPED_VIEW_ADDRESS: ...
@winfunctype('KERNEL32.dll')
def UnmapViewOfFileEx(BaseAddress: Windows.Win32.System.Memory.MEMORY_MAPPED_VIEW_ADDRESS, UnmapFlags: Windows.Win32.System.Memory.UNMAP_VIEW_OF_FILE_FLAGS) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def AllocateUserPhysicalPages(hProcess: Windows.Win32.Foundation.HANDLE, NumberOfPages: POINTER(UIntPtr), PageArray: POINTER(UIntPtr)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FreeUserPhysicalPages(hProcess: Windows.Win32.Foundation.HANDLE, NumberOfPages: POINTER(UIntPtr), PageArray: POINTER(UIntPtr)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def MapUserPhysicalPages(VirtualAddress: c_void_p, NumberOfPages: UIntPtr, PageArray: POINTER(UIntPtr)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def AllocateUserPhysicalPagesNuma(hProcess: Windows.Win32.Foundation.HANDLE, NumberOfPages: POINTER(UIntPtr), PageArray: POINTER(UIntPtr), nndPreferred: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def VirtualAllocExNuma(hProcess: Windows.Win32.Foundation.HANDLE, lpAddress: c_void_p, dwSize: UIntPtr, flAllocationType: Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE, flProtect: UInt32, nndPreferred: UInt32) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def GetMemoryErrorHandlingCapabilities(Capabilities: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def RegisterBadMemoryNotification(Callback: Windows.Win32.System.Memory.PBAD_MEMORY_CALLBACK_ROUTINE) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def UnregisterBadMemoryNotification(RegistrationHandle: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def OfferVirtualMemory(VirtualAddress: c_void_p, Size: UIntPtr, Priority: Windows.Win32.System.Memory.OFFER_PRIORITY) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def ReclaimVirtualMemory(VirtualAddress: c_void_p, Size: UIntPtr) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def DiscardVirtualMemory(VirtualAddress: c_void_p, Size: UIntPtr) -> UInt32: ...
@winfunctype('api-ms-win-core-memory-l1-1-3.dll')
def SetProcessValidCallTargets(hProcess: Windows.Win32.Foundation.HANDLE, VirtualAddress: c_void_p, RegionSize: UIntPtr, NumberOfOffsets: UInt32, OffsetInformation: POINTER(Windows.Win32.System.Memory.CFG_CALL_TARGET_INFO_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-memory-l1-1-7.dll')
def SetProcessValidCallTargetsForMappedView(Process: Windows.Win32.Foundation.HANDLE, VirtualAddress: c_void_p, RegionSize: UIntPtr, NumberOfOffsets: UInt32, OffsetInformation: POINTER(Windows.Win32.System.Memory.CFG_CALL_TARGET_INFO_head), Section: Windows.Win32.Foundation.HANDLE, ExpectedFileOffset: UInt64) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-memory-l1-1-3.dll')
def VirtualAllocFromApp(BaseAddress: c_void_p, Size: UIntPtr, AllocationType: Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE, Protection: UInt32) -> c_void_p: ...
@winfunctype('api-ms-win-core-memory-l1-1-3.dll')
def VirtualProtectFromApp(Address: c_void_p, Size: UIntPtr, NewProtection: UInt32, OldProtection: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-memory-l1-1-3.dll')
def OpenFileMappingFromApp(DesiredAccess: UInt32, InheritHandle: Windows.Win32.Foundation.BOOL, Name: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('api-ms-win-core-memory-l1-1-4.dll')
def QueryVirtualMemoryInformation(Process: Windows.Win32.Foundation.HANDLE, VirtualAddress: c_void_p, MemoryInformationClass: Windows.Win32.System.Memory.WIN32_MEMORY_INFORMATION_CLASS, MemoryInformation: c_void_p, MemoryInformationSize: UIntPtr, ReturnSize: POINTER(UIntPtr)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-memory-l1-1-5.dll')
def MapViewOfFileNuma2(FileMappingHandle: Windows.Win32.Foundation.HANDLE, ProcessHandle: Windows.Win32.Foundation.HANDLE, Offset: UInt64, BaseAddress: c_void_p, ViewSize: UIntPtr, AllocationType: UInt32, PageProtection: UInt32, PreferredNode: UInt32) -> Windows.Win32.System.Memory.MEMORY_MAPPED_VIEW_ADDRESS: ...
@winfunctype('api-ms-win-core-memory-l1-1-5.dll')
def UnmapViewOfFile2(Process: Windows.Win32.Foundation.HANDLE, BaseAddress: Windows.Win32.System.Memory.MEMORY_MAPPED_VIEW_ADDRESS, UnmapFlags: Windows.Win32.System.Memory.UNMAP_VIEW_OF_FILE_FLAGS) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-memory-l1-1-5.dll')
def VirtualUnlockEx(Process: Windows.Win32.Foundation.HANDLE, Address: c_void_p, Size: UIntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-memory-l1-1-6.dll')
def VirtualAlloc2(Process: Windows.Win32.Foundation.HANDLE, BaseAddress: c_void_p, Size: UIntPtr, AllocationType: Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE, PageProtection: UInt32, ExtendedParameters: POINTER(Windows.Win32.System.Memory.MEM_EXTENDED_PARAMETER_head), ParameterCount: UInt32) -> c_void_p: ...
@winfunctype('api-ms-win-core-memory-l1-1-6.dll')
def MapViewOfFile3(FileMapping: Windows.Win32.Foundation.HANDLE, Process: Windows.Win32.Foundation.HANDLE, BaseAddress: c_void_p, Offset: UInt64, ViewSize: UIntPtr, AllocationType: Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE, PageProtection: UInt32, ExtendedParameters: POINTER(Windows.Win32.System.Memory.MEM_EXTENDED_PARAMETER_head), ParameterCount: UInt32) -> Windows.Win32.System.Memory.MEMORY_MAPPED_VIEW_ADDRESS: ...
@winfunctype('api-ms-win-core-memory-l1-1-6.dll')
def VirtualAlloc2FromApp(Process: Windows.Win32.Foundation.HANDLE, BaseAddress: c_void_p, Size: UIntPtr, AllocationType: Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE, PageProtection: UInt32, ExtendedParameters: POINTER(Windows.Win32.System.Memory.MEM_EXTENDED_PARAMETER_head), ParameterCount: UInt32) -> c_void_p: ...
@winfunctype('api-ms-win-core-memory-l1-1-6.dll')
def MapViewOfFile3FromApp(FileMapping: Windows.Win32.Foundation.HANDLE, Process: Windows.Win32.Foundation.HANDLE, BaseAddress: c_void_p, Offset: UInt64, ViewSize: UIntPtr, AllocationType: Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE, PageProtection: UInt32, ExtendedParameters: POINTER(Windows.Win32.System.Memory.MEM_EXTENDED_PARAMETER_head), ParameterCount: UInt32) -> Windows.Win32.System.Memory.MEMORY_MAPPED_VIEW_ADDRESS: ...
@winfunctype('api-ms-win-core-memory-l1-1-7.dll')
def CreateFileMapping2(File: Windows.Win32.Foundation.HANDLE, SecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), DesiredAccess: UInt32, PageProtection: Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS, AllocationAttributes: UInt32, MaximumSize: UInt64, Name: Windows.Win32.Foundation.PWSTR, ExtendedParameters: POINTER(Windows.Win32.System.Memory.MEM_EXTENDED_PARAMETER_head), ParameterCount: UInt32) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('api-ms-win-core-memory-l1-1-8.dll')
def AllocateUserPhysicalPages2(ObjectHandle: Windows.Win32.Foundation.HANDLE, NumberOfPages: POINTER(UIntPtr), PageArray: POINTER(UIntPtr), ExtendedParameters: POINTER(Windows.Win32.System.Memory.MEM_EXTENDED_PARAMETER_head), ExtendedParameterCount: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-memory-l1-1-8.dll')
def OpenDedicatedMemoryPartition(Partition: Windows.Win32.Foundation.HANDLE, DedicatedMemoryTypeId: UInt64, DesiredAccess: UInt32, InheritHandle: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('api-ms-win-core-memory-l1-1-8.dll')
def QueryPartitionInformation(Partition: Windows.Win32.Foundation.HANDLE, PartitionInformationClass: Windows.Win32.System.Memory.WIN32_MEMORY_PARTITION_INFORMATION_CLASS, PartitionInformation: c_void_p, PartitionInformationLength: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('Atlthunk.dll')
def AtlThunk_AllocateData() -> POINTER(Windows.Win32.System.Memory.AtlThunkData_t): ...
@winfunctype('Atlthunk.dll')
def AtlThunk_InitData(Thunk: POINTER(Windows.Win32.System.Memory.AtlThunkData_t), Proc: c_void_p, FirstParameter: UIntPtr) -> Void: ...
@winfunctype('Atlthunk.dll')
def AtlThunk_DataToCode(param0: POINTER(Windows.Win32.System.Memory.AtlThunkData_t)) -> Windows.Win32.UI.WindowsAndMessaging.WNDPROC: ...
@winfunctype('Atlthunk.dll')
def AtlThunk_FreeData(Thunk: POINTER(Windows.Win32.System.Memory.AtlThunkData_t)) -> Void: ...
@winfunctype('KERNEL32.dll')
def RtlCompareMemory(Source1: c_void_p, Source2: c_void_p, Length: UIntPtr) -> UIntPtr: ...
@winfunctype('ntdll.dll')
def RtlCrc32(Buffer: c_void_p, Size: UIntPtr, InitialCrc: UInt32) -> UInt32: ...
@winfunctype('ntdll.dll')
def RtlCrc64(Buffer: c_void_p, Size: UIntPtr, InitialCrc: UInt64) -> UInt64: ...
@winfunctype('ntdll.dll')
def RtlIsZeroMemory(Buffer: c_void_p, Length: UIntPtr) -> Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('KERNEL32.dll')
def GlobalAlloc(uFlags: Windows.Win32.System.Memory.GLOBAL_ALLOC_FLAGS, dwBytes: UIntPtr) -> Windows.Win32.Foundation.HGLOBAL: ...
@winfunctype('KERNEL32.dll')
def GlobalReAlloc(hMem: Windows.Win32.Foundation.HGLOBAL, dwBytes: UIntPtr, uFlags: UInt32) -> Windows.Win32.Foundation.HGLOBAL: ...
@winfunctype('KERNEL32.dll')
def GlobalSize(hMem: Windows.Win32.Foundation.HGLOBAL) -> UIntPtr: ...
@winfunctype('KERNEL32.dll')
def GlobalUnlock(hMem: Windows.Win32.Foundation.HGLOBAL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GlobalLock(hMem: Windows.Win32.Foundation.HGLOBAL) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def GlobalFlags(hMem: Windows.Win32.Foundation.HGLOBAL) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GlobalHandle(pMem: c_void_p) -> Windows.Win32.Foundation.HGLOBAL: ...
@winfunctype('KERNEL32.dll')
def GlobalFree(hMem: Windows.Win32.Foundation.HGLOBAL) -> Windows.Win32.Foundation.HGLOBAL: ...
@winfunctype('KERNEL32.dll')
def LocalAlloc(uFlags: Windows.Win32.System.Memory.LOCAL_ALLOC_FLAGS, uBytes: UIntPtr) -> Windows.Win32.Foundation.HLOCAL: ...
@winfunctype('KERNEL32.dll')
def LocalReAlloc(hMem: Windows.Win32.Foundation.HLOCAL, uBytes: UIntPtr, uFlags: UInt32) -> Windows.Win32.Foundation.HLOCAL: ...
@winfunctype('KERNEL32.dll')
def LocalLock(hMem: Windows.Win32.Foundation.HLOCAL) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def LocalHandle(pMem: c_void_p) -> Windows.Win32.Foundation.HLOCAL: ...
@winfunctype('KERNEL32.dll')
def LocalUnlock(hMem: Windows.Win32.Foundation.HLOCAL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def LocalSize(hMem: Windows.Win32.Foundation.HLOCAL) -> UIntPtr: ...
@winfunctype('KERNEL32.dll')
def LocalFlags(hMem: Windows.Win32.Foundation.HLOCAL) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def LocalFree(hMem: Windows.Win32.Foundation.HLOCAL) -> Windows.Win32.Foundation.HLOCAL: ...
@winfunctype('KERNEL32.dll')
def CreateFileMappingA(hFile: Windows.Win32.Foundation.HANDLE, lpFileMappingAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), flProtect: Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS, dwMaximumSizeHigh: UInt32, dwMaximumSizeLow: UInt32, lpName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateFileMappingNumaA(hFile: Windows.Win32.Foundation.HANDLE, lpFileMappingAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), flProtect: Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS, dwMaximumSizeHigh: UInt32, dwMaximumSizeLow: UInt32, lpName: Windows.Win32.Foundation.PSTR, nndPreferred: UInt32) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def OpenFileMappingA(dwDesiredAccess: UInt32, bInheritHandle: Windows.Win32.Foundation.BOOL, lpName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def MapViewOfFileExNuma(hFileMappingObject: Windows.Win32.Foundation.HANDLE, dwDesiredAccess: Windows.Win32.System.Memory.FILE_MAP, dwFileOffsetHigh: UInt32, dwFileOffsetLow: UInt32, dwNumberOfBytesToMap: UIntPtr, lpBaseAddress: c_void_p, nndPreferred: UInt32) -> Windows.Win32.System.Memory.MEMORY_MAPPED_VIEW_ADDRESS: ...
@winfunctype('KERNEL32.dll')
def IsBadReadPtr(lp: c_void_p, ucb: UIntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def IsBadWritePtr(lp: c_void_p, ucb: UIntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def IsBadCodePtr(lpfn: Windows.Win32.Foundation.FARPROC) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def IsBadStringPtrA(lpsz: Windows.Win32.Foundation.PSTR, ucchMax: UIntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def IsBadStringPtrW(lpsz: Windows.Win32.Foundation.PWSTR, ucchMax: UIntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def MapUserPhysicalPagesScatter(VirtualAddresses: POINTER(c_void_p), NumberOfPages: UIntPtr, PageArray: POINTER(UIntPtr)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def AddSecureMemoryCacheCallback(pfnCallBack: Windows.Win32.System.Memory.PSECURE_MEMORY_CACHE_CALLBACK) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def RemoveSecureMemoryCacheCallback(pfnCallBack: Windows.Win32.System.Memory.PSECURE_MEMORY_CACHE_CALLBACK) -> Windows.Win32.Foundation.BOOL: ...
AtlThunkData_t = IntPtr
class CFG_CALL_TARGET_INFO(EasyCastStructure):
    Offset: UIntPtr
    Flags: UIntPtr
FILE_MAP = UInt32
FILE_MAP_WRITE: FILE_MAP = 2
FILE_MAP_READ: FILE_MAP = 4
FILE_MAP_ALL_ACCESS: FILE_MAP = 983071
FILE_MAP_EXECUTE: FILE_MAP = 32
FILE_MAP_COPY: FILE_MAP = 1
FILE_MAP_RESERVE: FILE_MAP = 2147483648
FILE_MAP_TARGETS_INVALID: FILE_MAP = 1073741824
FILE_MAP_LARGE_PAGES: FILE_MAP = 536870912
GLOBAL_ALLOC_FLAGS = UInt32
GHND: GLOBAL_ALLOC_FLAGS = 66
GMEM_FIXED: GLOBAL_ALLOC_FLAGS = 0
GMEM_MOVEABLE: GLOBAL_ALLOC_FLAGS = 2
GMEM_ZEROINIT: GLOBAL_ALLOC_FLAGS = 64
GPTR: GLOBAL_ALLOC_FLAGS = 64
HEAP_FLAGS = UInt32
HEAP_NONE: HEAP_FLAGS = 0
HEAP_NO_SERIALIZE: HEAP_FLAGS = 1
HEAP_GROWABLE: HEAP_FLAGS = 2
HEAP_GENERATE_EXCEPTIONS: HEAP_FLAGS = 4
HEAP_ZERO_MEMORY: HEAP_FLAGS = 8
HEAP_REALLOC_IN_PLACE_ONLY: HEAP_FLAGS = 16
HEAP_TAIL_CHECKING_ENABLED: HEAP_FLAGS = 32
HEAP_FREE_CHECKING_ENABLED: HEAP_FLAGS = 64
HEAP_DISABLE_COALESCE_ON_FREE: HEAP_FLAGS = 128
HEAP_CREATE_ALIGN_16: HEAP_FLAGS = 65536
HEAP_CREATE_ENABLE_TRACING: HEAP_FLAGS = 131072
HEAP_CREATE_ENABLE_EXECUTE: HEAP_FLAGS = 262144
HEAP_MAXIMUM_TAG: HEAP_FLAGS = 4095
HEAP_PSEUDO_TAG_FLAG: HEAP_FLAGS = 32768
HEAP_TAG_SHIFT: HEAP_FLAGS = 18
HEAP_CREATE_SEGMENT_HEAP: HEAP_FLAGS = 256
HEAP_CREATE_HARDENED: HEAP_FLAGS = 512
HEAP_INFORMATION_CLASS = Int32
HEAP_INFORMATION_CLASS_HeapCompatibilityInformation: HEAP_INFORMATION_CLASS = 0
HEAP_INFORMATION_CLASS_HeapEnableTerminationOnCorruption: HEAP_INFORMATION_CLASS = 1
HEAP_INFORMATION_CLASS_HeapOptimizeResources: HEAP_INFORMATION_CLASS = 3
HEAP_INFORMATION_CLASS_HeapTag: HEAP_INFORMATION_CLASS = 7
class HEAP_SUMMARY(EasyCastStructure):
    cb: UInt32
    cbAllocated: UIntPtr
    cbCommitted: UIntPtr
    cbReserved: UIntPtr
    cbMaxReserve: UIntPtr
class HeapHandle(EasyCastStructure):
    Value: IntPtr
LOCAL_ALLOC_FLAGS = UInt32
LHND: LOCAL_ALLOC_FLAGS = 66
LMEM_FIXED: LOCAL_ALLOC_FLAGS = 0
LMEM_MOVEABLE: LOCAL_ALLOC_FLAGS = 2
LMEM_ZEROINIT: LOCAL_ALLOC_FLAGS = 64
LPTR: LOCAL_ALLOC_FLAGS = 64
NONZEROLHND: LOCAL_ALLOC_FLAGS = 2
NONZEROLPTR: LOCAL_ALLOC_FLAGS = 0
if ARCH in 'X64,ARM64':
    class MEMORY_BASIC_INFORMATION(EasyCastStructure):
        BaseAddress: c_void_p
        AllocationBase: c_void_p
        AllocationProtect: Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS
        PartitionId: UInt16
        RegionSize: UIntPtr
        State: Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE
        Protect: Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS
        Type: Windows.Win32.System.Memory.PAGE_TYPE
if ARCH in 'X86':
    class MEMORY_BASIC_INFORMATION(EasyCastStructure):
        BaseAddress: c_void_p
        AllocationBase: c_void_p
        AllocationProtect: Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS
        RegionSize: UIntPtr
        State: Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE
        Protect: Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS
        Type: Windows.Win32.System.Memory.PAGE_TYPE
class MEMORY_BASIC_INFORMATION32(EasyCastStructure):
    BaseAddress: UInt32
    AllocationBase: UInt32
    AllocationProtect: Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS
    RegionSize: UInt32
    State: Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE
    Protect: Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS
    Type: Windows.Win32.System.Memory.PAGE_TYPE
class MEMORY_BASIC_INFORMATION64(EasyCastStructure):
    BaseAddress: UInt64
    AllocationBase: UInt64
    AllocationProtect: Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS
    __alignment1: UInt32
    RegionSize: UInt64
    State: Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE
    Protect: Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS
    Type: Windows.Win32.System.Memory.PAGE_TYPE
    __alignment2: UInt32
class MEMORY_MAPPED_VIEW_ADDRESS(EasyCastStructure):
    Value: c_void_p
class MEMORY_PARTITION_DEDICATED_MEMORY_ATTRIBUTE(EasyCastStructure):
    Type: Windows.Win32.System.Memory.MEM_DEDICATED_ATTRIBUTE_TYPE
    Reserved: UInt32
    Value: UInt64
class MEMORY_PARTITION_DEDICATED_MEMORY_INFORMATION(EasyCastStructure):
    NextEntryOffset: UInt32
    SizeOfInformation: UInt32
    Flags: UInt32
    AttributesOffset: UInt32
    AttributeCount: UInt32
    Reserved: UInt32
    TypeId: UInt64
MEMORY_RESOURCE_NOTIFICATION_TYPE = Int32
MEMORY_RESOURCE_NOTIFICATION_TYPE_LowMemoryResourceNotification: MEMORY_RESOURCE_NOTIFICATION_TYPE = 0
MEMORY_RESOURCE_NOTIFICATION_TYPE_HighMemoryResourceNotification: MEMORY_RESOURCE_NOTIFICATION_TYPE = 1
class MEM_ADDRESS_REQUIREMENTS(EasyCastStructure):
    LowestStartingAddress: c_void_p
    HighestEndingAddress: c_void_p
    Alignment: UIntPtr
MEM_DEDICATED_ATTRIBUTE_TYPE = Int32
MEM_DEDICATED_ATTRIBUTE_TYPE_MemDedicatedAttributeReadBandwidth: MEM_DEDICATED_ATTRIBUTE_TYPE = 0
MEM_DEDICATED_ATTRIBUTE_TYPE_MemDedicatedAttributeReadLatency: MEM_DEDICATED_ATTRIBUTE_TYPE = 1
MEM_DEDICATED_ATTRIBUTE_TYPE_MemDedicatedAttributeWriteBandwidth: MEM_DEDICATED_ATTRIBUTE_TYPE = 2
MEM_DEDICATED_ATTRIBUTE_TYPE_MemDedicatedAttributeWriteLatency: MEM_DEDICATED_ATTRIBUTE_TYPE = 3
MEM_DEDICATED_ATTRIBUTE_TYPE_MemDedicatedAttributeMax: MEM_DEDICATED_ATTRIBUTE_TYPE = 4
class MEM_EXTENDED_PARAMETER(EasyCastStructure):
    Anonymous1: _Anonymous1_e__Struct
    Anonymous2: _Anonymous2_e__Union
    class _Anonymous1_e__Struct(EasyCastStructure):
        _bitfield: UInt64
    class _Anonymous2_e__Union(EasyCastUnion):
        ULong64: UInt64
        Pointer: c_void_p
        Size: UIntPtr
        Handle: Windows.Win32.Foundation.HANDLE
        ULong: UInt32
MEM_EXTENDED_PARAMETER_TYPE = Int32
MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterInvalidType: MEM_EXTENDED_PARAMETER_TYPE = 0
MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterAddressRequirements: MEM_EXTENDED_PARAMETER_TYPE = 1
MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterNumaNode: MEM_EXTENDED_PARAMETER_TYPE = 2
MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterPartitionHandle: MEM_EXTENDED_PARAMETER_TYPE = 3
MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterUserPhysicalHandle: MEM_EXTENDED_PARAMETER_TYPE = 4
MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterAttributeFlags: MEM_EXTENDED_PARAMETER_TYPE = 5
MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterImageMachine: MEM_EXTENDED_PARAMETER_TYPE = 6
MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterMax: MEM_EXTENDED_PARAMETER_TYPE = 7
MEM_SECTION_EXTENDED_PARAMETER_TYPE = Int32
MEM_SECTION_EXTENDED_PARAMETER_TYPE_MemSectionExtendedParameterInvalidType: MEM_SECTION_EXTENDED_PARAMETER_TYPE = 0
MEM_SECTION_EXTENDED_PARAMETER_TYPE_MemSectionExtendedParameterUserPhysicalFlags: MEM_SECTION_EXTENDED_PARAMETER_TYPE = 1
MEM_SECTION_EXTENDED_PARAMETER_TYPE_MemSectionExtendedParameterNumaNode: MEM_SECTION_EXTENDED_PARAMETER_TYPE = 2
MEM_SECTION_EXTENDED_PARAMETER_TYPE_MemSectionExtendedParameterSigningLevel: MEM_SECTION_EXTENDED_PARAMETER_TYPE = 3
MEM_SECTION_EXTENDED_PARAMETER_TYPE_MemSectionExtendedParameterMax: MEM_SECTION_EXTENDED_PARAMETER_TYPE = 4
OFFER_PRIORITY = Int32
OFFER_PRIORITY_VmOfferPriorityVeryLow: OFFER_PRIORITY = 1
OFFER_PRIORITY_VmOfferPriorityLow: OFFER_PRIORITY = 2
OFFER_PRIORITY_VmOfferPriorityBelowNormal: OFFER_PRIORITY = 3
OFFER_PRIORITY_VmOfferPriorityNormal: OFFER_PRIORITY = 4
PAGE_PROTECTION_FLAGS = UInt32
PAGE_NOACCESS: PAGE_PROTECTION_FLAGS = 1
PAGE_READONLY: PAGE_PROTECTION_FLAGS = 2
PAGE_READWRITE: PAGE_PROTECTION_FLAGS = 4
PAGE_WRITECOPY: PAGE_PROTECTION_FLAGS = 8
PAGE_EXECUTE: PAGE_PROTECTION_FLAGS = 16
PAGE_EXECUTE_READ: PAGE_PROTECTION_FLAGS = 32
PAGE_EXECUTE_READWRITE: PAGE_PROTECTION_FLAGS = 64
PAGE_EXECUTE_WRITECOPY: PAGE_PROTECTION_FLAGS = 128
PAGE_GUARD: PAGE_PROTECTION_FLAGS = 256
PAGE_NOCACHE: PAGE_PROTECTION_FLAGS = 512
PAGE_WRITECOMBINE: PAGE_PROTECTION_FLAGS = 1024
PAGE_GRAPHICS_NOACCESS: PAGE_PROTECTION_FLAGS = 2048
PAGE_GRAPHICS_READONLY: PAGE_PROTECTION_FLAGS = 4096
PAGE_GRAPHICS_READWRITE: PAGE_PROTECTION_FLAGS = 8192
PAGE_GRAPHICS_EXECUTE: PAGE_PROTECTION_FLAGS = 16384
PAGE_GRAPHICS_EXECUTE_READ: PAGE_PROTECTION_FLAGS = 32768
PAGE_GRAPHICS_EXECUTE_READWRITE: PAGE_PROTECTION_FLAGS = 65536
PAGE_GRAPHICS_COHERENT: PAGE_PROTECTION_FLAGS = 131072
PAGE_GRAPHICS_NOCACHE: PAGE_PROTECTION_FLAGS = 262144
PAGE_ENCLAVE_THREAD_CONTROL: PAGE_PROTECTION_FLAGS = 2147483648
PAGE_REVERT_TO_FILE_MAP: PAGE_PROTECTION_FLAGS = 2147483648
PAGE_TARGETS_NO_UPDATE: PAGE_PROTECTION_FLAGS = 1073741824
PAGE_TARGETS_INVALID: PAGE_PROTECTION_FLAGS = 1073741824
PAGE_ENCLAVE_UNVALIDATED: PAGE_PROTECTION_FLAGS = 536870912
PAGE_ENCLAVE_MASK: PAGE_PROTECTION_FLAGS = 268435456
PAGE_ENCLAVE_DECOMMIT: PAGE_PROTECTION_FLAGS = 268435456
PAGE_ENCLAVE_SS_FIRST: PAGE_PROTECTION_FLAGS = 268435457
PAGE_ENCLAVE_SS_REST: PAGE_PROTECTION_FLAGS = 268435458
SEC_PARTITION_OWNER_HANDLE: PAGE_PROTECTION_FLAGS = 262144
SEC_64K_PAGES: PAGE_PROTECTION_FLAGS = 524288
SEC_FILE: PAGE_PROTECTION_FLAGS = 8388608
SEC_IMAGE: PAGE_PROTECTION_FLAGS = 16777216
SEC_PROTECTED_IMAGE: PAGE_PROTECTION_FLAGS = 33554432
SEC_RESERVE: PAGE_PROTECTION_FLAGS = 67108864
SEC_COMMIT: PAGE_PROTECTION_FLAGS = 134217728
SEC_NOCACHE: PAGE_PROTECTION_FLAGS = 268435456
SEC_WRITECOMBINE: PAGE_PROTECTION_FLAGS = 1073741824
SEC_LARGE_PAGES: PAGE_PROTECTION_FLAGS = 2147483648
SEC_IMAGE_NO_EXECUTE: PAGE_PROTECTION_FLAGS = 285212672
PAGE_TYPE = UInt32
MEM_PRIVATE: PAGE_TYPE = 131072
MEM_MAPPED: PAGE_TYPE = 262144
MEM_IMAGE: PAGE_TYPE = 16777216
@winfunctype_pointer
def PBAD_MEMORY_CALLBACK_ROUTINE() -> Void: ...
class PROCESS_HEAP_ENTRY(EasyCastStructure):
    lpData: c_void_p
    cbData: UInt32
    cbOverhead: Byte
    iRegionIndex: Byte
    wFlags: UInt16
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Block: _Block_e__Struct
        Region: _Region_e__Struct
        class _Block_e__Struct(EasyCastStructure):
            hMem: Windows.Win32.Foundation.HANDLE
            dwReserved: UInt32 * 3
        class _Region_e__Struct(EasyCastStructure):
            dwCommittedSize: UInt32
            dwUnCommittedSize: UInt32
            lpFirstBlock: c_void_p
            lpLastBlock: c_void_p
@winfunctype_pointer
def PSECURE_MEMORY_CACHE_CALLBACK(Addr: c_void_p, Range: UIntPtr) -> Windows.Win32.Foundation.BOOLEAN: ...
SECTION_FLAGS = UInt32
SECTION_ALL_ACCESS: SECTION_FLAGS = 983071
SECTION_QUERY: SECTION_FLAGS = 1
SECTION_MAP_WRITE: SECTION_FLAGS = 2
SECTION_MAP_READ: SECTION_FLAGS = 4
SECTION_MAP_EXECUTE: SECTION_FLAGS = 8
SECTION_EXTEND_SIZE: SECTION_FLAGS = 16
SECTION_MAP_EXECUTE_EXPLICIT: SECTION_FLAGS = 32
UNMAP_VIEW_OF_FILE_FLAGS = UInt32
MEM_UNMAP_NONE: UNMAP_VIEW_OF_FILE_FLAGS = 0
MEM_UNMAP_WITH_TRANSIENT_BOOST: UNMAP_VIEW_OF_FILE_FLAGS = 1
MEM_PRESERVE_PLACEHOLDER: UNMAP_VIEW_OF_FILE_FLAGS = 2
VIRTUAL_ALLOCATION_TYPE = UInt32
MEM_COMMIT: VIRTUAL_ALLOCATION_TYPE = 4096
MEM_RESERVE: VIRTUAL_ALLOCATION_TYPE = 8192
MEM_RESET: VIRTUAL_ALLOCATION_TYPE = 524288
MEM_RESET_UNDO: VIRTUAL_ALLOCATION_TYPE = 16777216
MEM_REPLACE_PLACEHOLDER: VIRTUAL_ALLOCATION_TYPE = 16384
MEM_LARGE_PAGES: VIRTUAL_ALLOCATION_TYPE = 536870912
MEM_RESERVE_PLACEHOLDER: VIRTUAL_ALLOCATION_TYPE = 262144
MEM_FREE: VIRTUAL_ALLOCATION_TYPE = 65536
VIRTUAL_FREE_TYPE = UInt32
MEM_DECOMMIT: VIRTUAL_FREE_TYPE = 16384
MEM_RELEASE: VIRTUAL_FREE_TYPE = 32768
WIN32_MEMORY_INFORMATION_CLASS = Int32
WIN32_MEMORY_INFORMATION_CLASS_MemoryRegionInfo: WIN32_MEMORY_INFORMATION_CLASS = 0
class WIN32_MEMORY_PARTITION_INFORMATION(EasyCastStructure):
    Flags: UInt32
    NumaNode: UInt32
    Channel: UInt32
    NumberOfNumaNodes: UInt32
    ResidentAvailablePages: UInt64
    CommittedPages: UInt64
    CommitLimit: UInt64
    PeakCommitment: UInt64
    TotalNumberOfPages: UInt64
    AvailablePages: UInt64
    ZeroPages: UInt64
    FreePages: UInt64
    StandbyPages: UInt64
    Reserved: UInt64 * 16
    MaximumCommitLimit: UInt64
    Reserved2: UInt64
    PartitionId: UInt32
WIN32_MEMORY_PARTITION_INFORMATION_CLASS = Int32
WIN32_MEMORY_PARTITION_INFORMATION_CLASS_MemoryPartitionInfo: WIN32_MEMORY_PARTITION_INFORMATION_CLASS = 0
WIN32_MEMORY_PARTITION_INFORMATION_CLASS_MemoryPartitionDedicatedMemoryInfo: WIN32_MEMORY_PARTITION_INFORMATION_CLASS = 1
class WIN32_MEMORY_RANGE_ENTRY(EasyCastStructure):
    VirtualAddress: c_void_p
    NumberOfBytes: UIntPtr
class WIN32_MEMORY_REGION_INFORMATION(EasyCastStructure):
    AllocationBase: c_void_p
    AllocationProtect: UInt32
    Anonymous: _Anonymous_e__Union
    RegionSize: UIntPtr
    CommitSize: UIntPtr
    class _Anonymous_e__Union(EasyCastUnion):
        Flags: UInt32
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(EasyCastStructure):
            _bitfield: UInt32
make_head(_module, 'CFG_CALL_TARGET_INFO')
make_head(_module, 'HEAP_SUMMARY')
make_head(_module, 'HeapHandle')
if ARCH in 'X64,ARM64':
    make_head(_module, 'MEMORY_BASIC_INFORMATION')
if ARCH in 'X86':
    make_head(_module, 'MEMORY_BASIC_INFORMATION')
make_head(_module, 'MEMORY_BASIC_INFORMATION32')
make_head(_module, 'MEMORY_BASIC_INFORMATION64')
make_head(_module, 'MEMORY_MAPPED_VIEW_ADDRESS')
make_head(_module, 'MEMORY_PARTITION_DEDICATED_MEMORY_ATTRIBUTE')
make_head(_module, 'MEMORY_PARTITION_DEDICATED_MEMORY_INFORMATION')
make_head(_module, 'MEM_ADDRESS_REQUIREMENTS')
make_head(_module, 'MEM_EXTENDED_PARAMETER')
make_head(_module, 'PBAD_MEMORY_CALLBACK_ROUTINE')
make_head(_module, 'PROCESS_HEAP_ENTRY')
make_head(_module, 'PSECURE_MEMORY_CACHE_CALLBACK')
make_head(_module, 'WIN32_MEMORY_PARTITION_INFORMATION')
make_head(_module, 'WIN32_MEMORY_RANGE_ENTRY')
make_head(_module, 'WIN32_MEMORY_REGION_INFORMATION')
