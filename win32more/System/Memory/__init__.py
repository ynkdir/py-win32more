from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Security
import win32more.System.Memory
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
FILE_CACHE_MAX_HARD_ENABLE: UInt32 = 1
FILE_CACHE_MAX_HARD_DISABLE: UInt32 = 2
FILE_CACHE_MIN_HARD_ENABLE: UInt32 = 4
FILE_CACHE_MIN_HARD_DISABLE: UInt32 = 8
MEHC_PATROL_SCRUBBER_PRESENT: UInt32 = 1
@winfunctype('KERNEL32.dll')
def HeapCreate(flOptions: win32more.System.Memory.HEAP_FLAGS, dwInitialSize: UIntPtr, dwMaximumSize: UIntPtr) -> win32more.System.Memory.HeapHandle: ...
@winfunctype('KERNEL32.dll')
def HeapDestroy(hHeap: win32more.System.Memory.HeapHandle) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def HeapAlloc(hHeap: win32more.System.Memory.HeapHandle, dwFlags: win32more.System.Memory.HEAP_FLAGS, dwBytes: UIntPtr) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def HeapReAlloc(hHeap: win32more.System.Memory.HeapHandle, dwFlags: win32more.System.Memory.HEAP_FLAGS, lpMem: c_void_p, dwBytes: UIntPtr) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def HeapFree(hHeap: win32more.System.Memory.HeapHandle, dwFlags: win32more.System.Memory.HEAP_FLAGS, lpMem: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def HeapSize(hHeap: win32more.System.Memory.HeapHandle, dwFlags: win32more.System.Memory.HEAP_FLAGS, lpMem: c_void_p) -> UIntPtr: ...
@winfunctype('KERNEL32.dll')
def GetProcessHeap() -> win32more.System.Memory.HeapHandle: ...
@winfunctype('KERNEL32.dll')
def HeapCompact(hHeap: win32more.System.Memory.HeapHandle, dwFlags: win32more.System.Memory.HEAP_FLAGS) -> UIntPtr: ...
@winfunctype('KERNEL32.dll')
def HeapSetInformation(HeapHandle: win32more.System.Memory.HeapHandle, HeapInformationClass: win32more.System.Memory.HEAP_INFORMATION_CLASS, HeapInformation: c_void_p, HeapInformationLength: UIntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def HeapValidate(hHeap: win32more.System.Memory.HeapHandle, dwFlags: win32more.System.Memory.HEAP_FLAGS, lpMem: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def HeapSummary(hHeap: win32more.Foundation.HANDLE, dwFlags: UInt32, lpSummary: POINTER(win32more.System.Memory.HEAP_SUMMARY_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProcessHeaps(NumberOfHeaps: UInt32, ProcessHeaps: POINTER(win32more.System.Memory.HeapHandle)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def HeapLock(hHeap: win32more.System.Memory.HeapHandle) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def HeapUnlock(hHeap: win32more.System.Memory.HeapHandle) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def HeapWalk(hHeap: win32more.System.Memory.HeapHandle, lpEntry: POINTER(win32more.System.Memory.PROCESS_HEAP_ENTRY_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def HeapQueryInformation(HeapHandle: win32more.System.Memory.HeapHandle, HeapInformationClass: win32more.System.Memory.HEAP_INFORMATION_CLASS, HeapInformation: c_void_p, HeapInformationLength: UIntPtr, ReturnLength: POINTER(UIntPtr)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def VirtualAlloc(lpAddress: c_void_p, dwSize: UIntPtr, flAllocationType: win32more.System.Memory.VIRTUAL_ALLOCATION_TYPE, flProtect: win32more.System.Memory.PAGE_PROTECTION_FLAGS) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def VirtualProtect(lpAddress: c_void_p, dwSize: UIntPtr, flNewProtect: win32more.System.Memory.PAGE_PROTECTION_FLAGS, lpflOldProtect: POINTER(win32more.System.Memory.PAGE_PROTECTION_FLAGS)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def VirtualFree(lpAddress: c_void_p, dwSize: UIntPtr, dwFreeType: win32more.System.Memory.VIRTUAL_FREE_TYPE) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def VirtualQuery(lpAddress: c_void_p, lpBuffer: POINTER(win32more.System.Memory.MEMORY_BASIC_INFORMATION_head), dwLength: UIntPtr) -> UIntPtr: ...
@winfunctype('KERNEL32.dll')
def VirtualAllocEx(hProcess: win32more.Foundation.HANDLE, lpAddress: c_void_p, dwSize: UIntPtr, flAllocationType: win32more.System.Memory.VIRTUAL_ALLOCATION_TYPE, flProtect: win32more.System.Memory.PAGE_PROTECTION_FLAGS) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def VirtualProtectEx(hProcess: win32more.Foundation.HANDLE, lpAddress: c_void_p, dwSize: UIntPtr, flNewProtect: win32more.System.Memory.PAGE_PROTECTION_FLAGS, lpflOldProtect: POINTER(win32more.System.Memory.PAGE_PROTECTION_FLAGS)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def VirtualQueryEx(hProcess: win32more.Foundation.HANDLE, lpAddress: c_void_p, lpBuffer: POINTER(win32more.System.Memory.MEMORY_BASIC_INFORMATION_head), dwLength: UIntPtr) -> UIntPtr: ...
@winfunctype('KERNEL32.dll')
def CreateFileMappingW(hFile: win32more.Foundation.HANDLE, lpFileMappingAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), flProtect: win32more.System.Memory.PAGE_PROTECTION_FLAGS, dwMaximumSizeHigh: UInt32, dwMaximumSizeLow: UInt32, lpName: win32more.Foundation.PWSTR) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def OpenFileMappingW(dwDesiredAccess: UInt32, bInheritHandle: win32more.Foundation.BOOL, lpName: win32more.Foundation.PWSTR) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def MapViewOfFile(hFileMappingObject: win32more.Foundation.HANDLE, dwDesiredAccess: win32more.System.Memory.FILE_MAP, dwFileOffsetHigh: UInt32, dwFileOffsetLow: UInt32, dwNumberOfBytesToMap: UIntPtr) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def MapViewOfFileEx(hFileMappingObject: win32more.Foundation.HANDLE, dwDesiredAccess: win32more.System.Memory.FILE_MAP, dwFileOffsetHigh: UInt32, dwFileOffsetLow: UInt32, dwNumberOfBytesToMap: UIntPtr, lpBaseAddress: c_void_p) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def VirtualFreeEx(hProcess: win32more.Foundation.HANDLE, lpAddress: c_void_p, dwSize: UIntPtr, dwFreeType: win32more.System.Memory.VIRTUAL_FREE_TYPE) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FlushViewOfFile(lpBaseAddress: c_void_p, dwNumberOfBytesToFlush: UIntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def UnmapViewOfFile(lpBaseAddress: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetLargePageMinimum() -> UIntPtr: ...
@winfunctype('KERNEL32.dll')
def GetProcessWorkingSetSizeEx(hProcess: win32more.Foundation.HANDLE, lpMinimumWorkingSetSize: POINTER(UIntPtr), lpMaximumWorkingSetSize: POINTER(UIntPtr), Flags: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetProcessWorkingSetSizeEx(hProcess: win32more.Foundation.HANDLE, dwMinimumWorkingSetSize: UIntPtr, dwMaximumWorkingSetSize: UIntPtr, Flags: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def VirtualLock(lpAddress: c_void_p, dwSize: UIntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def VirtualUnlock(lpAddress: c_void_p, dwSize: UIntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetWriteWatch(dwFlags: UInt32, lpBaseAddress: c_void_p, dwRegionSize: UIntPtr, lpAddresses: POINTER(c_void_p), lpdwCount: POINTER(UIntPtr), lpdwGranularity: POINTER(UInt32)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def ResetWriteWatch(lpBaseAddress: c_void_p, dwRegionSize: UIntPtr) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def CreateMemoryResourceNotification(NotificationType: win32more.System.Memory.MEMORY_RESOURCE_NOTIFICATION_TYPE) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def QueryMemoryResourceNotification(ResourceNotificationHandle: win32more.Foundation.HANDLE, ResourceState: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetSystemFileCacheSize(lpMinimumFileCacheSize: POINTER(UIntPtr), lpMaximumFileCacheSize: POINTER(UIntPtr), lpFlags: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetSystemFileCacheSize(MinimumFileCacheSize: UIntPtr, MaximumFileCacheSize: UIntPtr, Flags: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateFileMappingNumaW(hFile: win32more.Foundation.HANDLE, lpFileMappingAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), flProtect: win32more.System.Memory.PAGE_PROTECTION_FLAGS, dwMaximumSizeHigh: UInt32, dwMaximumSizeLow: UInt32, lpName: win32more.Foundation.PWSTR, nndPreferred: UInt32) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def PrefetchVirtualMemory(hProcess: win32more.Foundation.HANDLE, NumberOfEntries: UIntPtr, VirtualAddresses: POINTER(win32more.System.Memory.WIN32_MEMORY_RANGE_ENTRY_head), Flags: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateFileMappingFromApp(hFile: win32more.Foundation.HANDLE, SecurityAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), PageProtection: win32more.System.Memory.PAGE_PROTECTION_FLAGS, MaximumSize: UInt64, Name: win32more.Foundation.PWSTR) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def MapViewOfFileFromApp(hFileMappingObject: win32more.Foundation.HANDLE, DesiredAccess: win32more.System.Memory.FILE_MAP, FileOffset: UInt64, NumberOfBytesToMap: UIntPtr) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def UnmapViewOfFileEx(BaseAddress: c_void_p, UnmapFlags: win32more.System.Memory.UNMAP_VIEW_OF_FILE_FLAGS) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def AllocateUserPhysicalPages(hProcess: win32more.Foundation.HANDLE, NumberOfPages: POINTER(UIntPtr), PageArray: POINTER(UIntPtr)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FreeUserPhysicalPages(hProcess: win32more.Foundation.HANDLE, NumberOfPages: POINTER(UIntPtr), PageArray: POINTER(UIntPtr)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def MapUserPhysicalPages(VirtualAddress: c_void_p, NumberOfPages: UIntPtr, PageArray: POINTER(UIntPtr)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def AllocateUserPhysicalPagesNuma(hProcess: win32more.Foundation.HANDLE, NumberOfPages: POINTER(UIntPtr), PageArray: POINTER(UIntPtr), nndPreferred: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def VirtualAllocExNuma(hProcess: win32more.Foundation.HANDLE, lpAddress: c_void_p, dwSize: UIntPtr, flAllocationType: win32more.System.Memory.VIRTUAL_ALLOCATION_TYPE, flProtect: UInt32, nndPreferred: UInt32) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def GetMemoryErrorHandlingCapabilities(Capabilities: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def RegisterBadMemoryNotification(Callback: win32more.System.Memory.PBAD_MEMORY_CALLBACK_ROUTINE) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def UnregisterBadMemoryNotification(RegistrationHandle: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def OfferVirtualMemory(VirtualAddress: c_void_p, Size: UIntPtr, Priority: win32more.System.Memory.OFFER_PRIORITY) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def ReclaimVirtualMemory(VirtualAddress: c_void_p, Size: UIntPtr) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def DiscardVirtualMemory(VirtualAddress: c_void_p, Size: UIntPtr) -> UInt32: ...
@winfunctype('api-ms-win-core-memory-l1-1-3.dll')
def SetProcessValidCallTargets(hProcess: win32more.Foundation.HANDLE, VirtualAddress: c_void_p, RegionSize: UIntPtr, NumberOfOffsets: UInt32, OffsetInformation: POINTER(win32more.System.Memory.CFG_CALL_TARGET_INFO_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-memory-l1-1-7.dll')
def SetProcessValidCallTargetsForMappedView(Process: win32more.Foundation.HANDLE, VirtualAddress: c_void_p, RegionSize: UIntPtr, NumberOfOffsets: UInt32, OffsetInformation: POINTER(win32more.System.Memory.CFG_CALL_TARGET_INFO_head), Section: win32more.Foundation.HANDLE, ExpectedFileOffset: UInt64) -> win32more.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-memory-l1-1-3.dll')
def VirtualAllocFromApp(BaseAddress: c_void_p, Size: UIntPtr, AllocationType: win32more.System.Memory.VIRTUAL_ALLOCATION_TYPE, Protection: UInt32) -> c_void_p: ...
@winfunctype('api-ms-win-core-memory-l1-1-3.dll')
def VirtualProtectFromApp(Address: c_void_p, Size: UIntPtr, NewProtection: UInt32, OldProtection: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-memory-l1-1-3.dll')
def OpenFileMappingFromApp(DesiredAccess: UInt32, InheritHandle: win32more.Foundation.BOOL, Name: win32more.Foundation.PWSTR) -> win32more.Foundation.HANDLE: ...
@winfunctype('api-ms-win-core-memory-l1-1-4.dll')
def QueryVirtualMemoryInformation(Process: win32more.Foundation.HANDLE, VirtualAddress: c_void_p, MemoryInformationClass: win32more.System.Memory.WIN32_MEMORY_INFORMATION_CLASS, MemoryInformation: c_void_p, MemoryInformationSize: UIntPtr, ReturnSize: POINTER(UIntPtr)) -> win32more.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-memory-l1-1-5.dll')
def MapViewOfFileNuma2(FileMappingHandle: win32more.Foundation.HANDLE, ProcessHandle: win32more.Foundation.HANDLE, Offset: UInt64, BaseAddress: c_void_p, ViewSize: UIntPtr, AllocationType: UInt32, PageProtection: UInt32, PreferredNode: UInt32) -> c_void_p: ...
@winfunctype('api-ms-win-core-memory-l1-1-5.dll')
def UnmapViewOfFile2(Process: win32more.Foundation.HANDLE, BaseAddress: c_void_p, UnmapFlags: win32more.System.Memory.UNMAP_VIEW_OF_FILE_FLAGS) -> win32more.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-memory-l1-1-5.dll')
def VirtualUnlockEx(Process: win32more.Foundation.HANDLE, Address: c_void_p, Size: UIntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-memory-l1-1-6.dll')
def VirtualAlloc2(Process: win32more.Foundation.HANDLE, BaseAddress: c_void_p, Size: UIntPtr, AllocationType: win32more.System.Memory.VIRTUAL_ALLOCATION_TYPE, PageProtection: UInt32, ExtendedParameters: POINTER(win32more.System.Memory.MEM_EXTENDED_PARAMETER_head), ParameterCount: UInt32) -> c_void_p: ...
@winfunctype('api-ms-win-core-memory-l1-1-6.dll')
def MapViewOfFile3(FileMapping: win32more.Foundation.HANDLE, Process: win32more.Foundation.HANDLE, BaseAddress: c_void_p, Offset: UInt64, ViewSize: UIntPtr, AllocationType: win32more.System.Memory.VIRTUAL_ALLOCATION_TYPE, PageProtection: UInt32, ExtendedParameters: POINTER(win32more.System.Memory.MEM_EXTENDED_PARAMETER_head), ParameterCount: UInt32) -> c_void_p: ...
@winfunctype('api-ms-win-core-memory-l1-1-6.dll')
def VirtualAlloc2FromApp(Process: win32more.Foundation.HANDLE, BaseAddress: c_void_p, Size: UIntPtr, AllocationType: win32more.System.Memory.VIRTUAL_ALLOCATION_TYPE, PageProtection: UInt32, ExtendedParameters: POINTER(win32more.System.Memory.MEM_EXTENDED_PARAMETER_head), ParameterCount: UInt32) -> c_void_p: ...
@winfunctype('api-ms-win-core-memory-l1-1-6.dll')
def MapViewOfFile3FromApp(FileMapping: win32more.Foundation.HANDLE, Process: win32more.Foundation.HANDLE, BaseAddress: c_void_p, Offset: UInt64, ViewSize: UIntPtr, AllocationType: win32more.System.Memory.VIRTUAL_ALLOCATION_TYPE, PageProtection: UInt32, ExtendedParameters: POINTER(win32more.System.Memory.MEM_EXTENDED_PARAMETER_head), ParameterCount: UInt32) -> c_void_p: ...
@winfunctype('api-ms-win-core-memory-l1-1-7.dll')
def CreateFileMapping2(File: win32more.Foundation.HANDLE, SecurityAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), DesiredAccess: UInt32, PageProtection: win32more.System.Memory.PAGE_PROTECTION_FLAGS, AllocationAttributes: UInt32, MaximumSize: UInt64, Name: win32more.Foundation.PWSTR, ExtendedParameters: POINTER(win32more.System.Memory.MEM_EXTENDED_PARAMETER_head), ParameterCount: UInt32) -> win32more.Foundation.HANDLE: ...
@winfunctype('api-ms-win-core-memory-l1-1-8.dll')
def AllocateUserPhysicalPages2(ObjectHandle: win32more.Foundation.HANDLE, NumberOfPages: POINTER(UIntPtr), PageArray: POINTER(UIntPtr), ExtendedParameters: POINTER(win32more.System.Memory.MEM_EXTENDED_PARAMETER_head), ExtendedParameterCount: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-memory-l1-1-8.dll')
def OpenDedicatedMemoryPartition(Partition: win32more.Foundation.HANDLE, DedicatedMemoryTypeId: UInt64, DesiredAccess: UInt32, InheritHandle: win32more.Foundation.BOOL) -> win32more.Foundation.HANDLE: ...
@winfunctype('api-ms-win-core-memory-l1-1-8.dll')
def QueryPartitionInformation(Partition: win32more.Foundation.HANDLE, PartitionInformationClass: win32more.System.Memory.WIN32_MEMORY_PARTITION_INFORMATION_CLASS, PartitionInformation: c_void_p, PartitionInformationLength: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def RtlCompareMemory(Source1: c_void_p, Source2: c_void_p, Length: UIntPtr) -> UIntPtr: ...
@winfunctype('ntdll.dll')
def RtlCrc32(Buffer: c_void_p, Size: UIntPtr, InitialCrc: UInt32) -> UInt32: ...
@winfunctype('ntdll.dll')
def RtlCrc64(Buffer: c_void_p, Size: UIntPtr, InitialCrc: UInt64) -> UInt64: ...
@winfunctype('ntdll.dll')
def RtlIsZeroMemory(Buffer: c_void_p, Length: UIntPtr) -> win32more.Foundation.BOOLEAN: ...
@winfunctype('KERNEL32.dll')
def GlobalAlloc(uFlags: win32more.System.Memory.GLOBAL_ALLOC_FLAGS, dwBytes: UIntPtr) -> IntPtr: ...
@winfunctype('KERNEL32.dll')
def GlobalReAlloc(hMem: IntPtr, dwBytes: UIntPtr, uFlags: UInt32) -> IntPtr: ...
@winfunctype('KERNEL32.dll')
def GlobalSize(hMem: IntPtr) -> UIntPtr: ...
@winfunctype('KERNEL32.dll')
def GlobalUnlock(hMem: IntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GlobalLock(hMem: IntPtr) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def GlobalFlags(hMem: IntPtr) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GlobalHandle(pMem: c_void_p) -> IntPtr: ...
@winfunctype('KERNEL32.dll')
def GlobalFree(hMem: IntPtr) -> IntPtr: ...
@winfunctype('KERNEL32.dll')
def LocalAlloc(uFlags: win32more.System.Memory.LOCAL_ALLOC_FLAGS, uBytes: UIntPtr) -> IntPtr: ...
@winfunctype('KERNEL32.dll')
def LocalReAlloc(hMem: IntPtr, uBytes: UIntPtr, uFlags: UInt32) -> IntPtr: ...
@winfunctype('KERNEL32.dll')
def LocalLock(hMem: IntPtr) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def LocalHandle(pMem: c_void_p) -> IntPtr: ...
@winfunctype('KERNEL32.dll')
def LocalUnlock(hMem: IntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def LocalSize(hMem: IntPtr) -> UIntPtr: ...
@winfunctype('KERNEL32.dll')
def LocalFlags(hMem: IntPtr) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def LocalFree(hMem: IntPtr) -> IntPtr: ...
@winfunctype('KERNEL32.dll')
def CreateFileMappingA(hFile: win32more.Foundation.HANDLE, lpFileMappingAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), flProtect: win32more.System.Memory.PAGE_PROTECTION_FLAGS, dwMaximumSizeHigh: UInt32, dwMaximumSizeLow: UInt32, lpName: win32more.Foundation.PSTR) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateFileMappingNumaA(hFile: win32more.Foundation.HANDLE, lpFileMappingAttributes: POINTER(win32more.Security.SECURITY_ATTRIBUTES_head), flProtect: win32more.System.Memory.PAGE_PROTECTION_FLAGS, dwMaximumSizeHigh: UInt32, dwMaximumSizeLow: UInt32, lpName: win32more.Foundation.PSTR, nndPreferred: UInt32) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def OpenFileMappingA(dwDesiredAccess: UInt32, bInheritHandle: win32more.Foundation.BOOL, lpName: win32more.Foundation.PSTR) -> win32more.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def MapViewOfFileExNuma(hFileMappingObject: win32more.Foundation.HANDLE, dwDesiredAccess: win32more.System.Memory.FILE_MAP, dwFileOffsetHigh: UInt32, dwFileOffsetLow: UInt32, dwNumberOfBytesToMap: UIntPtr, lpBaseAddress: c_void_p, nndPreferred: UInt32) -> c_void_p: ...
@winfunctype('KERNEL32.dll')
def IsBadReadPtr(lp: c_void_p, ucb: UIntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def IsBadWritePtr(lp: c_void_p, ucb: UIntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def IsBadCodePtr(lpfn: win32more.Foundation.FARPROC) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def IsBadStringPtrA(lpsz: win32more.Foundation.PSTR, ucchMax: UIntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def IsBadStringPtrW(lpsz: win32more.Foundation.PWSTR, ucchMax: UIntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def MapUserPhysicalPagesScatter(VirtualAddresses: POINTER(c_void_p), NumberOfPages: UIntPtr, PageArray: POINTER(UIntPtr)) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def AddSecureMemoryCacheCallback(pfnCallBack: win32more.System.Memory.PSECURE_MEMORY_CACHE_CALLBACK) -> win32more.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def RemoveSecureMemoryCacheCallback(pfnCallBack: win32more.System.Memory.PSECURE_MEMORY_CACHE_CALLBACK) -> win32more.Foundation.BOOL: ...
class CFG_CALL_TARGET_INFO(Structure):
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
class HEAP_SUMMARY(Structure):
    cb: UInt32
    cbAllocated: UIntPtr
    cbCommitted: UIntPtr
    cbReserved: UIntPtr
    cbMaxReserve: UIntPtr
HeapHandle = IntPtr
LOCAL_ALLOC_FLAGS = UInt32
LHND: LOCAL_ALLOC_FLAGS = 66
LMEM_FIXED: LOCAL_ALLOC_FLAGS = 0
LMEM_MOVEABLE: LOCAL_ALLOC_FLAGS = 2
LMEM_ZEROINIT: LOCAL_ALLOC_FLAGS = 64
LPTR: LOCAL_ALLOC_FLAGS = 64
NONZEROLHND: LOCAL_ALLOC_FLAGS = 2
NONZEROLPTR: LOCAL_ALLOC_FLAGS = 0
if ARCH in 'X64,ARM64':
    class MEMORY_BASIC_INFORMATION(Structure):
        BaseAddress: c_void_p
        AllocationBase: c_void_p
        AllocationProtect: win32more.System.Memory.PAGE_PROTECTION_FLAGS
        PartitionId: UInt16
        RegionSize: UIntPtr
        State: win32more.System.Memory.VIRTUAL_ALLOCATION_TYPE
        Protect: win32more.System.Memory.PAGE_PROTECTION_FLAGS
        Type: win32more.System.Memory.PAGE_TYPE
if ARCH in 'X86':
    class MEMORY_BASIC_INFORMATION(Structure):
        BaseAddress: c_void_p
        AllocationBase: c_void_p
        AllocationProtect: win32more.System.Memory.PAGE_PROTECTION_FLAGS
        RegionSize: UIntPtr
        State: win32more.System.Memory.VIRTUAL_ALLOCATION_TYPE
        Protect: win32more.System.Memory.PAGE_PROTECTION_FLAGS
        Type: win32more.System.Memory.PAGE_TYPE
class MEMORY_BASIC_INFORMATION32(Structure):
    BaseAddress: UInt32
    AllocationBase: UInt32
    AllocationProtect: win32more.System.Memory.PAGE_PROTECTION_FLAGS
    RegionSize: UInt32
    State: win32more.System.Memory.VIRTUAL_ALLOCATION_TYPE
    Protect: win32more.System.Memory.PAGE_PROTECTION_FLAGS
    Type: win32more.System.Memory.PAGE_TYPE
class MEMORY_BASIC_INFORMATION64(Structure):
    BaseAddress: UInt64
    AllocationBase: UInt64
    AllocationProtect: win32more.System.Memory.PAGE_PROTECTION_FLAGS
    __alignment1: UInt32
    RegionSize: UInt64
    State: win32more.System.Memory.VIRTUAL_ALLOCATION_TYPE
    Protect: win32more.System.Memory.PAGE_PROTECTION_FLAGS
    Type: win32more.System.Memory.PAGE_TYPE
    __alignment2: UInt32
MEMORY_RESOURCE_NOTIFICATION_TYPE = Int32
MEMORY_RESOURCE_NOTIFICATION_TYPE_LowMemoryResourceNotification: MEMORY_RESOURCE_NOTIFICATION_TYPE = 0
MEMORY_RESOURCE_NOTIFICATION_TYPE_HighMemoryResourceNotification: MEMORY_RESOURCE_NOTIFICATION_TYPE = 1
class MEM_ADDRESS_REQUIREMENTS(Structure):
    LowestStartingAddress: c_void_p
    HighestEndingAddress: c_void_p
    Alignment: UIntPtr
class MEM_EXTENDED_PARAMETER(Structure):
    Anonymous1: _Anonymous1_e__Struct
    Anonymous2: _Anonymous2_e__Union
    class _Anonymous1_e__Struct(Structure):
        _bitfield: UInt64
    class _Anonymous2_e__Union(Union):
        ULong64: UInt64
        Pointer: c_void_p
        Size: UIntPtr
        Handle: win32more.Foundation.HANDLE
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
class PROCESS_HEAP_ENTRY(Structure):
    lpData: c_void_p
    cbData: UInt32
    cbOverhead: Byte
    iRegionIndex: Byte
    wFlags: UInt16
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Block: _Block_e__Struct
        Region: _Region_e__Struct
        class _Block_e__Struct(Structure):
            hMem: win32more.Foundation.HANDLE
            dwReserved: UInt32 * 3
        class _Region_e__Struct(Structure):
            dwCommittedSize: UInt32
            dwUnCommittedSize: UInt32
            lpFirstBlock: c_void_p
            lpLastBlock: c_void_p
@winfunctype_pointer
def PSECURE_MEMORY_CACHE_CALLBACK(Addr: c_void_p, Range: UIntPtr) -> win32more.Foundation.BOOLEAN: ...
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
class WIN32_MEMORY_PARTITION_INFORMATION(Structure):
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
class WIN32_MEMORY_RANGE_ENTRY(Structure):
    VirtualAddress: c_void_p
    NumberOfBytes: UIntPtr
class WIN32_MEMORY_REGION_INFORMATION(Structure):
    AllocationBase: c_void_p
    AllocationProtect: UInt32
    Anonymous: _Anonymous_e__Union
    RegionSize: UIntPtr
    CommitSize: UIntPtr
    class _Anonymous_e__Union(Union):
        Flags: UInt32
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            _bitfield: UInt32
make_head(_module, 'CFG_CALL_TARGET_INFO')
make_head(_module, 'HEAP_SUMMARY')
if ARCH in 'X64,ARM64':
    make_head(_module, 'MEMORY_BASIC_INFORMATION')
if ARCH in 'X86':
    make_head(_module, 'MEMORY_BASIC_INFORMATION')
make_head(_module, 'MEMORY_BASIC_INFORMATION32')
make_head(_module, 'MEMORY_BASIC_INFORMATION64')
make_head(_module, 'MEM_ADDRESS_REQUIREMENTS')
make_head(_module, 'MEM_EXTENDED_PARAMETER')
make_head(_module, 'PBAD_MEMORY_CALLBACK_ROUTINE')
make_head(_module, 'PROCESS_HEAP_ENTRY')
make_head(_module, 'PSECURE_MEMORY_CACHE_CALLBACK')
make_head(_module, 'WIN32_MEMORY_PARTITION_INFORMATION')
make_head(_module, 'WIN32_MEMORY_RANGE_ENTRY')
make_head(_module, 'WIN32_MEMORY_REGION_INFORMATION')
__all__ = [
    "AddSecureMemoryCacheCallback",
    "AllocateUserPhysicalPages",
    "AllocateUserPhysicalPages2",
    "AllocateUserPhysicalPagesNuma",
    "CFG_CALL_TARGET_INFO",
    "CreateFileMapping2",
    "CreateFileMappingA",
    "CreateFileMappingFromApp",
    "CreateFileMappingNumaA",
    "CreateFileMappingNumaW",
    "CreateFileMappingW",
    "CreateMemoryResourceNotification",
    "DiscardVirtualMemory",
    "FILE_CACHE_MAX_HARD_DISABLE",
    "FILE_CACHE_MAX_HARD_ENABLE",
    "FILE_CACHE_MIN_HARD_DISABLE",
    "FILE_CACHE_MIN_HARD_ENABLE",
    "FILE_MAP",
    "FILE_MAP_ALL_ACCESS",
    "FILE_MAP_COPY",
    "FILE_MAP_EXECUTE",
    "FILE_MAP_LARGE_PAGES",
    "FILE_MAP_READ",
    "FILE_MAP_RESERVE",
    "FILE_MAP_TARGETS_INVALID",
    "FILE_MAP_WRITE",
    "FlushViewOfFile",
    "FreeUserPhysicalPages",
    "GHND",
    "GLOBAL_ALLOC_FLAGS",
    "GMEM_FIXED",
    "GMEM_MOVEABLE",
    "GMEM_ZEROINIT",
    "GPTR",
    "GetLargePageMinimum",
    "GetMemoryErrorHandlingCapabilities",
    "GetProcessHeap",
    "GetProcessHeaps",
    "GetProcessWorkingSetSizeEx",
    "GetSystemFileCacheSize",
    "GetWriteWatch",
    "GlobalAlloc",
    "GlobalFlags",
    "GlobalFree",
    "GlobalHandle",
    "GlobalLock",
    "GlobalReAlloc",
    "GlobalSize",
    "GlobalUnlock",
    "HEAP_CREATE_ALIGN_16",
    "HEAP_CREATE_ENABLE_EXECUTE",
    "HEAP_CREATE_ENABLE_TRACING",
    "HEAP_CREATE_HARDENED",
    "HEAP_CREATE_SEGMENT_HEAP",
    "HEAP_DISABLE_COALESCE_ON_FREE",
    "HEAP_FLAGS",
    "HEAP_FREE_CHECKING_ENABLED",
    "HEAP_GENERATE_EXCEPTIONS",
    "HEAP_GROWABLE",
    "HEAP_INFORMATION_CLASS",
    "HEAP_INFORMATION_CLASS_HeapCompatibilityInformation",
    "HEAP_INFORMATION_CLASS_HeapEnableTerminationOnCorruption",
    "HEAP_INFORMATION_CLASS_HeapOptimizeResources",
    "HEAP_INFORMATION_CLASS_HeapTag",
    "HEAP_MAXIMUM_TAG",
    "HEAP_NONE",
    "HEAP_NO_SERIALIZE",
    "HEAP_PSEUDO_TAG_FLAG",
    "HEAP_REALLOC_IN_PLACE_ONLY",
    "HEAP_SUMMARY",
    "HEAP_TAG_SHIFT",
    "HEAP_TAIL_CHECKING_ENABLED",
    "HEAP_ZERO_MEMORY",
    "HeapAlloc",
    "HeapCompact",
    "HeapCreate",
    "HeapDestroy",
    "HeapFree",
    "HeapHandle",
    "HeapLock",
    "HeapQueryInformation",
    "HeapReAlloc",
    "HeapSetInformation",
    "HeapSize",
    "HeapSummary",
    "HeapUnlock",
    "HeapValidate",
    "HeapWalk",
    "IsBadCodePtr",
    "IsBadReadPtr",
    "IsBadStringPtrA",
    "IsBadStringPtrW",
    "IsBadWritePtr",
    "LHND",
    "LMEM_FIXED",
    "LMEM_MOVEABLE",
    "LMEM_ZEROINIT",
    "LOCAL_ALLOC_FLAGS",
    "LPTR",
    "LocalAlloc",
    "LocalFlags",
    "LocalFree",
    "LocalHandle",
    "LocalLock",
    "LocalReAlloc",
    "LocalSize",
    "LocalUnlock",
    "MEHC_PATROL_SCRUBBER_PRESENT",
    "MEMORY_BASIC_INFORMATION",
    "MEMORY_BASIC_INFORMATION32",
    "MEMORY_BASIC_INFORMATION64",
    "MEMORY_RESOURCE_NOTIFICATION_TYPE",
    "MEMORY_RESOURCE_NOTIFICATION_TYPE_HighMemoryResourceNotification",
    "MEMORY_RESOURCE_NOTIFICATION_TYPE_LowMemoryResourceNotification",
    "MEM_ADDRESS_REQUIREMENTS",
    "MEM_COMMIT",
    "MEM_DECOMMIT",
    "MEM_EXTENDED_PARAMETER",
    "MEM_EXTENDED_PARAMETER_TYPE",
    "MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterAddressRequirements",
    "MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterAttributeFlags",
    "MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterImageMachine",
    "MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterInvalidType",
    "MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterMax",
    "MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterNumaNode",
    "MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterPartitionHandle",
    "MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterUserPhysicalHandle",
    "MEM_FREE",
    "MEM_IMAGE",
    "MEM_LARGE_PAGES",
    "MEM_MAPPED",
    "MEM_PRESERVE_PLACEHOLDER",
    "MEM_PRIVATE",
    "MEM_RELEASE",
    "MEM_REPLACE_PLACEHOLDER",
    "MEM_RESERVE",
    "MEM_RESERVE_PLACEHOLDER",
    "MEM_RESET",
    "MEM_RESET_UNDO",
    "MEM_UNMAP_NONE",
    "MEM_UNMAP_WITH_TRANSIENT_BOOST",
    "MapUserPhysicalPages",
    "MapUserPhysicalPagesScatter",
    "MapViewOfFile",
    "MapViewOfFile3",
    "MapViewOfFile3FromApp",
    "MapViewOfFileEx",
    "MapViewOfFileExNuma",
    "MapViewOfFileFromApp",
    "MapViewOfFileNuma2",
    "NONZEROLHND",
    "NONZEROLPTR",
    "OFFER_PRIORITY",
    "OFFER_PRIORITY_VmOfferPriorityBelowNormal",
    "OFFER_PRIORITY_VmOfferPriorityLow",
    "OFFER_PRIORITY_VmOfferPriorityNormal",
    "OFFER_PRIORITY_VmOfferPriorityVeryLow",
    "OfferVirtualMemory",
    "OpenDedicatedMemoryPartition",
    "OpenFileMappingA",
    "OpenFileMappingFromApp",
    "OpenFileMappingW",
    "PAGE_ENCLAVE_DECOMMIT",
    "PAGE_ENCLAVE_MASK",
    "PAGE_ENCLAVE_SS_FIRST",
    "PAGE_ENCLAVE_SS_REST",
    "PAGE_ENCLAVE_THREAD_CONTROL",
    "PAGE_ENCLAVE_UNVALIDATED",
    "PAGE_EXECUTE",
    "PAGE_EXECUTE_READ",
    "PAGE_EXECUTE_READWRITE",
    "PAGE_EXECUTE_WRITECOPY",
    "PAGE_GRAPHICS_COHERENT",
    "PAGE_GRAPHICS_EXECUTE",
    "PAGE_GRAPHICS_EXECUTE_READ",
    "PAGE_GRAPHICS_EXECUTE_READWRITE",
    "PAGE_GRAPHICS_NOACCESS",
    "PAGE_GRAPHICS_NOCACHE",
    "PAGE_GRAPHICS_READONLY",
    "PAGE_GRAPHICS_READWRITE",
    "PAGE_GUARD",
    "PAGE_NOACCESS",
    "PAGE_NOCACHE",
    "PAGE_PROTECTION_FLAGS",
    "PAGE_READONLY",
    "PAGE_READWRITE",
    "PAGE_REVERT_TO_FILE_MAP",
    "PAGE_TARGETS_INVALID",
    "PAGE_TARGETS_NO_UPDATE",
    "PAGE_TYPE",
    "PAGE_WRITECOMBINE",
    "PAGE_WRITECOPY",
    "PBAD_MEMORY_CALLBACK_ROUTINE",
    "PROCESS_HEAP_ENTRY",
    "PSECURE_MEMORY_CACHE_CALLBACK",
    "PrefetchVirtualMemory",
    "QueryMemoryResourceNotification",
    "QueryPartitionInformation",
    "QueryVirtualMemoryInformation",
    "ReclaimVirtualMemory",
    "RegisterBadMemoryNotification",
    "RemoveSecureMemoryCacheCallback",
    "ResetWriteWatch",
    "RtlCompareMemory",
    "RtlCrc32",
    "RtlCrc64",
    "RtlIsZeroMemory",
    "SEC_64K_PAGES",
    "SEC_COMMIT",
    "SEC_FILE",
    "SEC_IMAGE",
    "SEC_IMAGE_NO_EXECUTE",
    "SEC_LARGE_PAGES",
    "SEC_NOCACHE",
    "SEC_PARTITION_OWNER_HANDLE",
    "SEC_PROTECTED_IMAGE",
    "SEC_RESERVE",
    "SEC_WRITECOMBINE",
    "SetProcessValidCallTargets",
    "SetProcessValidCallTargetsForMappedView",
    "SetProcessWorkingSetSizeEx",
    "SetSystemFileCacheSize",
    "UNMAP_VIEW_OF_FILE_FLAGS",
    "UnmapViewOfFile",
    "UnmapViewOfFile2",
    "UnmapViewOfFileEx",
    "UnregisterBadMemoryNotification",
    "VIRTUAL_ALLOCATION_TYPE",
    "VIRTUAL_FREE_TYPE",
    "VirtualAlloc",
    "VirtualAlloc2",
    "VirtualAlloc2FromApp",
    "VirtualAllocEx",
    "VirtualAllocExNuma",
    "VirtualAllocFromApp",
    "VirtualFree",
    "VirtualFreeEx",
    "VirtualLock",
    "VirtualProtect",
    "VirtualProtectEx",
    "VirtualProtectFromApp",
    "VirtualQuery",
    "VirtualQueryEx",
    "VirtualUnlock",
    "VirtualUnlockEx",
    "WIN32_MEMORY_INFORMATION_CLASS",
    "WIN32_MEMORY_INFORMATION_CLASS_MemoryRegionInfo",
    "WIN32_MEMORY_PARTITION_INFORMATION",
    "WIN32_MEMORY_PARTITION_INFORMATION_CLASS",
    "WIN32_MEMORY_PARTITION_INFORMATION_CLASS_MemoryPartitionDedicatedMemoryInfo",
    "WIN32_MEMORY_PARTITION_INFORMATION_CLASS_MemoryPartitionInfo",
    "WIN32_MEMORY_RANGE_ENTRY",
    "WIN32_MEMORY_REGION_INFORMATION",
]
_arch_optional = [
]
