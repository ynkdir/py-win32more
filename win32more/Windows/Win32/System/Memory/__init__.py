from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.System.Memory
FILE_CACHE_MAX_HARD_ENABLE: UInt32 = 1
FILE_CACHE_MAX_HARD_DISABLE: UInt32 = 2
FILE_CACHE_MIN_HARD_ENABLE: UInt32 = 4
FILE_CACHE_MIN_HARD_DISABLE: UInt32 = 8
MEHC_PATROL_SCRUBBER_PRESENT: UInt32 = 1
@winfunctype('KERNEL32.dll')
def HeapCreate(flOptions: win32more.Windows.Win32.System.Memory.HEAP_FLAGS, dwInitialSize: UIntPtr, dwMaximumSize: UIntPtr) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def HeapDestroy(hHeap: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def HeapAlloc(hHeap: win32more.Windows.Win32.Foundation.HANDLE, dwFlags: win32more.Windows.Win32.System.Memory.HEAP_FLAGS, dwBytes: UIntPtr) -> VoidPtr: ...
@winfunctype('KERNEL32.dll')
def HeapReAlloc(hHeap: win32more.Windows.Win32.Foundation.HANDLE, dwFlags: win32more.Windows.Win32.System.Memory.HEAP_FLAGS, lpMem: VoidPtr, dwBytes: UIntPtr) -> VoidPtr: ...
@winfunctype('KERNEL32.dll')
def HeapFree(hHeap: win32more.Windows.Win32.Foundation.HANDLE, dwFlags: win32more.Windows.Win32.System.Memory.HEAP_FLAGS, lpMem: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def HeapSize(hHeap: win32more.Windows.Win32.Foundation.HANDLE, dwFlags: win32more.Windows.Win32.System.Memory.HEAP_FLAGS, lpMem: VoidPtr) -> UIntPtr: ...
@winfunctype('KERNEL32.dll')
def GetProcessHeap() -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def HeapCompact(hHeap: win32more.Windows.Win32.Foundation.HANDLE, dwFlags: win32more.Windows.Win32.System.Memory.HEAP_FLAGS) -> UIntPtr: ...
@winfunctype('KERNEL32.dll')
def HeapSetInformation(HeapHandle: win32more.Windows.Win32.Foundation.HANDLE, HeapInformationClass: win32more.Windows.Win32.System.Memory.HEAP_INFORMATION_CLASS, HeapInformation: VoidPtr, HeapInformationLength: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def HeapValidate(hHeap: win32more.Windows.Win32.Foundation.HANDLE, dwFlags: win32more.Windows.Win32.System.Memory.HEAP_FLAGS, lpMem: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def HeapSummary(hHeap: win32more.Windows.Win32.Foundation.HANDLE, dwFlags: UInt32, lpSummary: POINTER(win32more.Windows.Win32.System.Memory.HEAP_SUMMARY)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProcessHeaps(NumberOfHeaps: UInt32, ProcessHeaps: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def HeapLock(hHeap: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def HeapUnlock(hHeap: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def HeapWalk(hHeap: win32more.Windows.Win32.Foundation.HANDLE, lpEntry: POINTER(win32more.Windows.Win32.System.Memory.PROCESS_HEAP_ENTRY)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def HeapQueryInformation(HeapHandle: win32more.Windows.Win32.Foundation.HANDLE, HeapInformationClass: win32more.Windows.Win32.System.Memory.HEAP_INFORMATION_CLASS, HeapInformation: VoidPtr, HeapInformationLength: UIntPtr, ReturnLength: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def VirtualAlloc(lpAddress: VoidPtr, dwSize: UIntPtr, flAllocationType: win32more.Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE, flProtect: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS) -> VoidPtr: ...
@winfunctype('KERNEL32.dll')
def VirtualProtect(lpAddress: VoidPtr, dwSize: UIntPtr, flNewProtect: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS, lpflOldProtect: POINTER(win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def VirtualFree(lpAddress: VoidPtr, dwSize: UIntPtr, dwFreeType: win32more.Windows.Win32.System.Memory.VIRTUAL_FREE_TYPE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def VirtualQuery(lpAddress: VoidPtr, lpBuffer: POINTER(win32more.Windows.Win32.System.Memory.MEMORY_BASIC_INFORMATION), dwLength: UIntPtr) -> UIntPtr: ...
@winfunctype('KERNEL32.dll')
def VirtualAllocEx(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpAddress: VoidPtr, dwSize: UIntPtr, flAllocationType: win32more.Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE, flProtect: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS) -> VoidPtr: ...
@winfunctype('KERNEL32.dll')
def VirtualProtectEx(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpAddress: VoidPtr, dwSize: UIntPtr, flNewProtect: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS, lpflOldProtect: POINTER(win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def VirtualQueryEx(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpAddress: VoidPtr, lpBuffer: POINTER(win32more.Windows.Win32.System.Memory.MEMORY_BASIC_INFORMATION), dwLength: UIntPtr) -> UIntPtr: ...
@winfunctype('KERNEL32.dll')
def CreateFileMappingW(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpFileMappingAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), flProtect: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS, dwMaximumSizeHigh: UInt32, dwMaximumSizeLow: UInt32, lpName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
CreateFileMapping = UnicodeAlias('CreateFileMappingW')
@winfunctype('KERNEL32.dll')
def OpenFileMappingW(dwDesiredAccess: UInt32, bInheritHandle: win32more.Windows.Win32.Foundation.BOOL, lpName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
OpenFileMapping = UnicodeAlias('OpenFileMappingW')
@winfunctype('KERNEL32.dll')
def MapViewOfFile(hFileMappingObject: win32more.Windows.Win32.Foundation.HANDLE, dwDesiredAccess: win32more.Windows.Win32.System.Memory.FILE_MAP, dwFileOffsetHigh: UInt32, dwFileOffsetLow: UInt32, dwNumberOfBytesToMap: UIntPtr) -> win32more.Windows.Win32.System.Memory.MEMORY_MAPPED_VIEW_ADDRESS: ...
@winfunctype('KERNEL32.dll')
def MapViewOfFileEx(hFileMappingObject: win32more.Windows.Win32.Foundation.HANDLE, dwDesiredAccess: win32more.Windows.Win32.System.Memory.FILE_MAP, dwFileOffsetHigh: UInt32, dwFileOffsetLow: UInt32, dwNumberOfBytesToMap: UIntPtr, lpBaseAddress: VoidPtr) -> win32more.Windows.Win32.System.Memory.MEMORY_MAPPED_VIEW_ADDRESS: ...
@winfunctype('KERNEL32.dll')
def VirtualFreeEx(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpAddress: VoidPtr, dwSize: UIntPtr, dwFreeType: win32more.Windows.Win32.System.Memory.VIRTUAL_FREE_TYPE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FlushViewOfFile(lpBaseAddress: VoidPtr, dwNumberOfBytesToFlush: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def UnmapViewOfFile(lpBaseAddress: win32more.Windows.Win32.System.Memory.MEMORY_MAPPED_VIEW_ADDRESS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetLargePageMinimum() -> UIntPtr: ...
@winfunctype('KERNEL32.dll')
def GetProcessWorkingSetSizeEx(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpMinimumWorkingSetSize: POINTER(UIntPtr), lpMaximumWorkingSetSize: POINTER(UIntPtr), Flags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetProcessWorkingSetSizeEx(hProcess: win32more.Windows.Win32.Foundation.HANDLE, dwMinimumWorkingSetSize: UIntPtr, dwMaximumWorkingSetSize: UIntPtr, Flags: win32more.Windows.Win32.System.Memory.SETPROCESSWORKINGSETSIZEEX_FLAGS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def VirtualLock(lpAddress: VoidPtr, dwSize: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def VirtualUnlock(lpAddress: VoidPtr, dwSize: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetWriteWatch(dwFlags: UInt32, lpBaseAddress: VoidPtr, dwRegionSize: UIntPtr, lpAddresses: POINTER(VoidPtr), lpdwCount: POINTER(UIntPtr), lpdwGranularity: POINTER(UInt32)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def ResetWriteWatch(lpBaseAddress: VoidPtr, dwRegionSize: UIntPtr) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def CreateMemoryResourceNotification(NotificationType: win32more.Windows.Win32.System.Memory.MEMORY_RESOURCE_NOTIFICATION_TYPE) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def QueryMemoryResourceNotification(ResourceNotificationHandle: win32more.Windows.Win32.Foundation.HANDLE, ResourceState: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetSystemFileCacheSize(lpMinimumFileCacheSize: POINTER(UIntPtr), lpMaximumFileCacheSize: POINTER(UIntPtr), lpFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetSystemFileCacheSize(MinimumFileCacheSize: UIntPtr, MaximumFileCacheSize: UIntPtr, Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateFileMappingNumaW(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpFileMappingAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), flProtect: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS, dwMaximumSizeHigh: UInt32, dwMaximumSizeLow: UInt32, lpName: win32more.Windows.Win32.Foundation.PWSTR, nndPreferred: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
CreateFileMappingNuma = UnicodeAlias('CreateFileMappingNumaW')
@winfunctype('KERNEL32.dll')
def PrefetchVirtualMemory(hProcess: win32more.Windows.Win32.Foundation.HANDLE, NumberOfEntries: UIntPtr, VirtualAddresses: POINTER(win32more.Windows.Win32.System.Memory.WIN32_MEMORY_RANGE_ENTRY), Flags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def CreateFileMappingFromApp(hFile: win32more.Windows.Win32.Foundation.HANDLE, SecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), PageProtection: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS, MaximumSize: UInt64, Name: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def MapViewOfFileFromApp(hFileMappingObject: win32more.Windows.Win32.Foundation.HANDLE, DesiredAccess: win32more.Windows.Win32.System.Memory.FILE_MAP, FileOffset: UInt64, NumberOfBytesToMap: UIntPtr) -> win32more.Windows.Win32.System.Memory.MEMORY_MAPPED_VIEW_ADDRESS: ...
@winfunctype('KERNEL32.dll')
def UnmapViewOfFileEx(BaseAddress: win32more.Windows.Win32.System.Memory.MEMORY_MAPPED_VIEW_ADDRESS, UnmapFlags: win32more.Windows.Win32.System.Memory.UNMAP_VIEW_OF_FILE_FLAGS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def AllocateUserPhysicalPages(hProcess: win32more.Windows.Win32.Foundation.HANDLE, NumberOfPages: POINTER(UIntPtr), PageArray: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FreeUserPhysicalPages(hProcess: win32more.Windows.Win32.Foundation.HANDLE, NumberOfPages: POINTER(UIntPtr), PageArray: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def MapUserPhysicalPages(VirtualAddress: VoidPtr, NumberOfPages: UIntPtr, PageArray: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def AllocateUserPhysicalPagesNuma(hProcess: win32more.Windows.Win32.Foundation.HANDLE, NumberOfPages: POINTER(UIntPtr), PageArray: POINTER(UIntPtr), nndPreferred: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def VirtualAllocExNuma(hProcess: win32more.Windows.Win32.Foundation.HANDLE, lpAddress: VoidPtr, dwSize: UIntPtr, flAllocationType: win32more.Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE, flProtect: UInt32, nndPreferred: UInt32) -> VoidPtr: ...
@winfunctype('KERNEL32.dll')
def GetMemoryErrorHandlingCapabilities(Capabilities: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def RegisterBadMemoryNotification(Callback: win32more.Windows.Win32.System.Memory.PBAD_MEMORY_CALLBACK_ROUTINE) -> VoidPtr: ...
@winfunctype('KERNEL32.dll')
def UnregisterBadMemoryNotification(RegistrationHandle: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def OfferVirtualMemory(VirtualAddress: VoidPtr, Size: UIntPtr, Priority: win32more.Windows.Win32.System.Memory.OFFER_PRIORITY) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def ReclaimVirtualMemory(VirtualAddress: VoidPtr, Size: UIntPtr) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def DiscardVirtualMemory(VirtualAddress: VoidPtr, Size: UIntPtr) -> UInt32: ...
@winfunctype('api-ms-win-core-memory-l1-1-3.dll')
def SetProcessValidCallTargets(hProcess: win32more.Windows.Win32.Foundation.HANDLE, VirtualAddress: VoidPtr, RegionSize: UIntPtr, NumberOfOffsets: UInt32, OffsetInformation: POINTER(win32more.Windows.Win32.System.Memory.CFG_CALL_TARGET_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-memory-l1-1-7.dll')
def SetProcessValidCallTargetsForMappedView(Process: win32more.Windows.Win32.Foundation.HANDLE, VirtualAddress: VoidPtr, RegionSize: UIntPtr, NumberOfOffsets: UInt32, OffsetInformation: POINTER(win32more.Windows.Win32.System.Memory.CFG_CALL_TARGET_INFO), Section: win32more.Windows.Win32.Foundation.HANDLE, ExpectedFileOffset: UInt64) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-memory-l1-1-3.dll')
def VirtualAllocFromApp(BaseAddress: VoidPtr, Size: UIntPtr, AllocationType: win32more.Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE, Protection: UInt32) -> VoidPtr: ...
@winfunctype('api-ms-win-core-memory-l1-1-3.dll')
def VirtualProtectFromApp(Address: VoidPtr, Size: UIntPtr, NewProtection: UInt32, OldProtection: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-memory-l1-1-3.dll')
def OpenFileMappingFromApp(DesiredAccess: UInt32, InheritHandle: win32more.Windows.Win32.Foundation.BOOL, Name: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('api-ms-win-core-memory-l1-1-4.dll')
def QueryVirtualMemoryInformation(Process: win32more.Windows.Win32.Foundation.HANDLE, VirtualAddress: VoidPtr, MemoryInformationClass: win32more.Windows.Win32.System.Memory.WIN32_MEMORY_INFORMATION_CLASS, MemoryInformation: VoidPtr, MemoryInformationSize: UIntPtr, ReturnSize: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-memory-l1-1-5.dll')
def MapViewOfFileNuma2(FileMappingHandle: win32more.Windows.Win32.Foundation.HANDLE, ProcessHandle: win32more.Windows.Win32.Foundation.HANDLE, Offset: UInt64, BaseAddress: VoidPtr, ViewSize: UIntPtr, AllocationType: UInt32, PageProtection: UInt32, PreferredNode: UInt32) -> win32more.Windows.Win32.System.Memory.MEMORY_MAPPED_VIEW_ADDRESS: ...
@winfunctype('api-ms-win-core-memory-l1-1-5.dll')
def UnmapViewOfFile2(Process: win32more.Windows.Win32.Foundation.HANDLE, BaseAddress: win32more.Windows.Win32.System.Memory.MEMORY_MAPPED_VIEW_ADDRESS, UnmapFlags: win32more.Windows.Win32.System.Memory.UNMAP_VIEW_OF_FILE_FLAGS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-memory-l1-1-5.dll')
def VirtualUnlockEx(Process: win32more.Windows.Win32.Foundation.HANDLE, Address: VoidPtr, Size: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-memory-l1-1-6.dll')
def VirtualAlloc2(Process: win32more.Windows.Win32.Foundation.HANDLE, BaseAddress: VoidPtr, Size: UIntPtr, AllocationType: win32more.Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE, PageProtection: UInt32, ExtendedParameters: POINTER(win32more.Windows.Win32.System.Memory.MEM_EXTENDED_PARAMETER), ParameterCount: UInt32) -> VoidPtr: ...
@winfunctype('api-ms-win-core-memory-l1-1-6.dll')
def MapViewOfFile3(FileMapping: win32more.Windows.Win32.Foundation.HANDLE, Process: win32more.Windows.Win32.Foundation.HANDLE, BaseAddress: VoidPtr, Offset: UInt64, ViewSize: UIntPtr, AllocationType: win32more.Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE, PageProtection: UInt32, ExtendedParameters: POINTER(win32more.Windows.Win32.System.Memory.MEM_EXTENDED_PARAMETER), ParameterCount: UInt32) -> win32more.Windows.Win32.System.Memory.MEMORY_MAPPED_VIEW_ADDRESS: ...
@winfunctype('api-ms-win-core-memory-l1-1-6.dll')
def VirtualAlloc2FromApp(Process: win32more.Windows.Win32.Foundation.HANDLE, BaseAddress: VoidPtr, Size: UIntPtr, AllocationType: win32more.Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE, PageProtection: UInt32, ExtendedParameters: POINTER(win32more.Windows.Win32.System.Memory.MEM_EXTENDED_PARAMETER), ParameterCount: UInt32) -> VoidPtr: ...
@winfunctype('api-ms-win-core-memory-l1-1-6.dll')
def MapViewOfFile3FromApp(FileMapping: win32more.Windows.Win32.Foundation.HANDLE, Process: win32more.Windows.Win32.Foundation.HANDLE, BaseAddress: VoidPtr, Offset: UInt64, ViewSize: UIntPtr, AllocationType: win32more.Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE, PageProtection: UInt32, ExtendedParameters: POINTER(win32more.Windows.Win32.System.Memory.MEM_EXTENDED_PARAMETER), ParameterCount: UInt32) -> win32more.Windows.Win32.System.Memory.MEMORY_MAPPED_VIEW_ADDRESS: ...
@winfunctype('api-ms-win-core-memory-l1-1-7.dll')
def CreateFileMapping2(File: win32more.Windows.Win32.Foundation.HANDLE, SecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), DesiredAccess: UInt32, PageProtection: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS, AllocationAttributes: UInt32, MaximumSize: UInt64, Name: win32more.Windows.Win32.Foundation.PWSTR, ExtendedParameters: POINTER(win32more.Windows.Win32.System.Memory.MEM_EXTENDED_PARAMETER), ParameterCount: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('api-ms-win-core-memory-l1-1-8.dll')
def AllocateUserPhysicalPages2(ObjectHandle: win32more.Windows.Win32.Foundation.HANDLE, NumberOfPages: POINTER(UIntPtr), PageArray: POINTER(UIntPtr), ExtendedParameters: POINTER(win32more.Windows.Win32.System.Memory.MEM_EXTENDED_PARAMETER), ExtendedParameterCount: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-memory-l1-1-8.dll')
def OpenDedicatedMemoryPartition(Partition: win32more.Windows.Win32.Foundation.HANDLE, DedicatedMemoryTypeId: UInt64, DesiredAccess: UInt32, InheritHandle: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('api-ms-win-core-memory-l1-1-8.dll')
def QueryPartitionInformation(Partition: win32more.Windows.Win32.Foundation.HANDLE, PartitionInformationClass: win32more.Windows.Win32.System.Memory.WIN32_MEMORY_PARTITION_INFORMATION_CLASS, PartitionInformation: VoidPtr, PartitionInformationLength: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def RtlCompareMemory(Source1: VoidPtr, Source2: VoidPtr, Length: UIntPtr) -> UIntPtr: ...
@winfunctype('ntdll.dll')
def RtlCrc32(Buffer: VoidPtr, Size: UIntPtr, InitialCrc: UInt32) -> UInt32: ...
@winfunctype('ntdll.dll')
def RtlCrc64(Buffer: VoidPtr, Size: UIntPtr, InitialCrc: UInt64) -> UInt64: ...
@winfunctype('ntdll.dll')
def RtlIsZeroMemory(Buffer: VoidPtr, Length: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype('KERNEL32.dll')
def GlobalAlloc(uFlags: win32more.Windows.Win32.System.Memory.GLOBAL_ALLOC_FLAGS, dwBytes: UIntPtr) -> win32more.Windows.Win32.Foundation.HGLOBAL: ...
@winfunctype('KERNEL32.dll')
def GlobalReAlloc(hMem: win32more.Windows.Win32.Foundation.HGLOBAL, dwBytes: UIntPtr, uFlags: UInt32) -> win32more.Windows.Win32.Foundation.HGLOBAL: ...
@winfunctype('KERNEL32.dll')
def GlobalSize(hMem: win32more.Windows.Win32.Foundation.HGLOBAL) -> UIntPtr: ...
@winfunctype('KERNEL32.dll')
def GlobalUnlock(hMem: win32more.Windows.Win32.Foundation.HGLOBAL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GlobalLock(hMem: win32more.Windows.Win32.Foundation.HGLOBAL) -> VoidPtr: ...
@winfunctype('KERNEL32.dll')
def GlobalFlags(hMem: win32more.Windows.Win32.Foundation.HGLOBAL) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GlobalHandle(pMem: VoidPtr) -> win32more.Windows.Win32.Foundation.HGLOBAL: ...
@winfunctype('KERNEL32.dll')
def LocalAlloc(uFlags: win32more.Windows.Win32.System.Memory.LOCAL_ALLOC_FLAGS, uBytes: UIntPtr) -> win32more.Windows.Win32.Foundation.HLOCAL: ...
@winfunctype('KERNEL32.dll')
def LocalReAlloc(hMem: win32more.Windows.Win32.Foundation.HLOCAL, uBytes: UIntPtr, uFlags: UInt32) -> win32more.Windows.Win32.Foundation.HLOCAL: ...
@winfunctype('KERNEL32.dll')
def LocalLock(hMem: win32more.Windows.Win32.Foundation.HLOCAL) -> VoidPtr: ...
@winfunctype('KERNEL32.dll')
def LocalHandle(pMem: VoidPtr) -> win32more.Windows.Win32.Foundation.HLOCAL: ...
@winfunctype('KERNEL32.dll')
def LocalUnlock(hMem: win32more.Windows.Win32.Foundation.HLOCAL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def LocalSize(hMem: win32more.Windows.Win32.Foundation.HLOCAL) -> UIntPtr: ...
@winfunctype('KERNEL32.dll')
def LocalFlags(hMem: win32more.Windows.Win32.Foundation.HLOCAL) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def CreateFileMappingA(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpFileMappingAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), flProtect: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS, dwMaximumSizeHigh: UInt32, dwMaximumSizeLow: UInt32, lpName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def CreateFileMappingNumaA(hFile: win32more.Windows.Win32.Foundation.HANDLE, lpFileMappingAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), flProtect: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS, dwMaximumSizeHigh: UInt32, dwMaximumSizeLow: UInt32, lpName: win32more.Windows.Win32.Foundation.PSTR, nndPreferred: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def OpenFileMappingA(dwDesiredAccess: UInt32, bInheritHandle: win32more.Windows.Win32.Foundation.BOOL, lpName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def MapViewOfFileExNuma(hFileMappingObject: win32more.Windows.Win32.Foundation.HANDLE, dwDesiredAccess: win32more.Windows.Win32.System.Memory.FILE_MAP, dwFileOffsetHigh: UInt32, dwFileOffsetLow: UInt32, dwNumberOfBytesToMap: UIntPtr, lpBaseAddress: VoidPtr, nndPreferred: UInt32) -> win32more.Windows.Win32.System.Memory.MEMORY_MAPPED_VIEW_ADDRESS: ...
@winfunctype('KERNEL32.dll')
def IsBadReadPtr(lp: VoidPtr, ucb: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def IsBadWritePtr(lp: VoidPtr, ucb: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def IsBadCodePtr(lpfn: win32more.Windows.Win32.Foundation.FARPROC) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def IsBadStringPtrA(lpsz: win32more.Windows.Win32.Foundation.PSTR, ucchMax: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def IsBadStringPtrW(lpsz: win32more.Windows.Win32.Foundation.PWSTR, ucchMax: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
IsBadStringPtr = UnicodeAlias('IsBadStringPtrW')
@winfunctype('KERNEL32.dll')
def MapUserPhysicalPagesScatter(VirtualAddresses: POINTER(VoidPtr), NumberOfPages: UIntPtr, PageArray: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def AddSecureMemoryCacheCallback(pfnCallBack: win32more.Windows.Win32.System.Memory.PSECURE_MEMORY_CACHE_CALLBACK) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def RemoveSecureMemoryCacheCallback(pfnCallBack: win32more.Windows.Win32.System.Memory.PSECURE_MEMORY_CACHE_CALLBACK) -> win32more.Windows.Win32.Foundation.BOOL: ...
AtlThunkData_t = IntPtr
class CFG_CALL_TARGET_INFO(Structure):
    Offset: UIntPtr
    Flags: UIntPtr
FILE_MAP = UInt32
FILE_MAP_WRITE: win32more.Windows.Win32.System.Memory.FILE_MAP = 2
FILE_MAP_READ: win32more.Windows.Win32.System.Memory.FILE_MAP = 4
FILE_MAP_ALL_ACCESS: win32more.Windows.Win32.System.Memory.FILE_MAP = 983071
FILE_MAP_EXECUTE: win32more.Windows.Win32.System.Memory.FILE_MAP = 32
FILE_MAP_COPY: win32more.Windows.Win32.System.Memory.FILE_MAP = 1
FILE_MAP_RESERVE: win32more.Windows.Win32.System.Memory.FILE_MAP = 2147483648
FILE_MAP_TARGETS_INVALID: win32more.Windows.Win32.System.Memory.FILE_MAP = 1073741824
FILE_MAP_LARGE_PAGES: win32more.Windows.Win32.System.Memory.FILE_MAP = 536870912
GLOBAL_ALLOC_FLAGS = UInt32
GHND: win32more.Windows.Win32.System.Memory.GLOBAL_ALLOC_FLAGS = 66
GMEM_FIXED: win32more.Windows.Win32.System.Memory.GLOBAL_ALLOC_FLAGS = 0
GMEM_MOVEABLE: win32more.Windows.Win32.System.Memory.GLOBAL_ALLOC_FLAGS = 2
GMEM_ZEROINIT: win32more.Windows.Win32.System.Memory.GLOBAL_ALLOC_FLAGS = 64
GPTR: win32more.Windows.Win32.System.Memory.GLOBAL_ALLOC_FLAGS = 64
HEAP_FLAGS = UInt32
HEAP_NONE: win32more.Windows.Win32.System.Memory.HEAP_FLAGS = 0
HEAP_NO_SERIALIZE: win32more.Windows.Win32.System.Memory.HEAP_FLAGS = 1
HEAP_GROWABLE: win32more.Windows.Win32.System.Memory.HEAP_FLAGS = 2
HEAP_GENERATE_EXCEPTIONS: win32more.Windows.Win32.System.Memory.HEAP_FLAGS = 4
HEAP_ZERO_MEMORY: win32more.Windows.Win32.System.Memory.HEAP_FLAGS = 8
HEAP_REALLOC_IN_PLACE_ONLY: win32more.Windows.Win32.System.Memory.HEAP_FLAGS = 16
HEAP_TAIL_CHECKING_ENABLED: win32more.Windows.Win32.System.Memory.HEAP_FLAGS = 32
HEAP_FREE_CHECKING_ENABLED: win32more.Windows.Win32.System.Memory.HEAP_FLAGS = 64
HEAP_DISABLE_COALESCE_ON_FREE: win32more.Windows.Win32.System.Memory.HEAP_FLAGS = 128
HEAP_CREATE_ALIGN_16: win32more.Windows.Win32.System.Memory.HEAP_FLAGS = 65536
HEAP_CREATE_ENABLE_TRACING: win32more.Windows.Win32.System.Memory.HEAP_FLAGS = 131072
HEAP_CREATE_ENABLE_EXECUTE: win32more.Windows.Win32.System.Memory.HEAP_FLAGS = 262144
HEAP_MAXIMUM_TAG: win32more.Windows.Win32.System.Memory.HEAP_FLAGS = 4095
HEAP_PSEUDO_TAG_FLAG: win32more.Windows.Win32.System.Memory.HEAP_FLAGS = 32768
HEAP_TAG_SHIFT: win32more.Windows.Win32.System.Memory.HEAP_FLAGS = 18
HEAP_CREATE_SEGMENT_HEAP: win32more.Windows.Win32.System.Memory.HEAP_FLAGS = 256
HEAP_CREATE_HARDENED: win32more.Windows.Win32.System.Memory.HEAP_FLAGS = 512
HEAP_INFORMATION_CLASS = Int32
HeapCompatibilityInformation: win32more.Windows.Win32.System.Memory.HEAP_INFORMATION_CLASS = 0
HeapEnableTerminationOnCorruption: win32more.Windows.Win32.System.Memory.HEAP_INFORMATION_CLASS = 1
HeapOptimizeResources: win32more.Windows.Win32.System.Memory.HEAP_INFORMATION_CLASS = 3
HeapTag: win32more.Windows.Win32.System.Memory.HEAP_INFORMATION_CLASS = 7
class HEAP_SUMMARY(Structure):
    cb: UInt32
    cbAllocated: UIntPtr
    cbCommitted: UIntPtr
    cbReserved: UIntPtr
    cbMaxReserve: UIntPtr
LOCAL_ALLOC_FLAGS = UInt32
LHND: win32more.Windows.Win32.System.Memory.LOCAL_ALLOC_FLAGS = 66
LMEM_FIXED: win32more.Windows.Win32.System.Memory.LOCAL_ALLOC_FLAGS = 0
LMEM_MOVEABLE: win32more.Windows.Win32.System.Memory.LOCAL_ALLOC_FLAGS = 2
LMEM_ZEROINIT: win32more.Windows.Win32.System.Memory.LOCAL_ALLOC_FLAGS = 64
LPTR: win32more.Windows.Win32.System.Memory.LOCAL_ALLOC_FLAGS = 64
NONZEROLHND: win32more.Windows.Win32.System.Memory.LOCAL_ALLOC_FLAGS = 2
NONZEROLPTR: win32more.Windows.Win32.System.Memory.LOCAL_ALLOC_FLAGS = 0
if ARCH in 'X64,ARM64':
    class MEMORY_BASIC_INFORMATION(Structure):
        BaseAddress: VoidPtr
        AllocationBase: VoidPtr
        AllocationProtect: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS
        PartitionId: UInt16
        RegionSize: UIntPtr
        State: win32more.Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE
        Protect: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS
        Type: win32more.Windows.Win32.System.Memory.PAGE_TYPE
elif ARCH in 'X86':
    class MEMORY_BASIC_INFORMATION(Structure):
        BaseAddress: VoidPtr
        AllocationBase: VoidPtr
        AllocationProtect: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS
        RegionSize: UIntPtr
        State: win32more.Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE
        Protect: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS
        Type: win32more.Windows.Win32.System.Memory.PAGE_TYPE
class MEMORY_BASIC_INFORMATION32(Structure):
    BaseAddress: UInt32
    AllocationBase: UInt32
    AllocationProtect: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS
    RegionSize: UInt32
    State: win32more.Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE
    Protect: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS
    Type: win32more.Windows.Win32.System.Memory.PAGE_TYPE
class MEMORY_BASIC_INFORMATION64(Structure):
    BaseAddress: UInt64
    AllocationBase: UInt64
    AllocationProtect: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS
    __alignment1: UInt32
    RegionSize: UInt64
    State: win32more.Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE
    Protect: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS
    Type: win32more.Windows.Win32.System.Memory.PAGE_TYPE
    __alignment2: UInt32
class MEMORY_MAPPED_VIEW_ADDRESS(Structure):
    Value: VoidPtr
class MEMORY_PARTITION_DEDICATED_MEMORY_ATTRIBUTE(Structure):
    Type: win32more.Windows.Win32.System.Memory.MEM_DEDICATED_ATTRIBUTE_TYPE
    Reserved: UInt32
    Value: UInt64
class MEMORY_PARTITION_DEDICATED_MEMORY_INFORMATION(Structure):
    NextEntryOffset: UInt32
    SizeOfInformation: UInt32
    Flags: UInt32
    AttributesOffset: UInt32
    AttributeCount: UInt32
    Reserved: UInt32
    TypeId: UInt64
MEMORY_RESOURCE_NOTIFICATION_TYPE = Int32
LowMemoryResourceNotification: win32more.Windows.Win32.System.Memory.MEMORY_RESOURCE_NOTIFICATION_TYPE = 0
HighMemoryResourceNotification: win32more.Windows.Win32.System.Memory.MEMORY_RESOURCE_NOTIFICATION_TYPE = 1
class MEM_ADDRESS_REQUIREMENTS(Structure):
    LowestStartingAddress: VoidPtr
    HighestEndingAddress: VoidPtr
    Alignment: UIntPtr
MEM_DEDICATED_ATTRIBUTE_TYPE = Int32
MemDedicatedAttributeReadBandwidth: win32more.Windows.Win32.System.Memory.MEM_DEDICATED_ATTRIBUTE_TYPE = 0
MemDedicatedAttributeReadLatency: win32more.Windows.Win32.System.Memory.MEM_DEDICATED_ATTRIBUTE_TYPE = 1
MemDedicatedAttributeWriteBandwidth: win32more.Windows.Win32.System.Memory.MEM_DEDICATED_ATTRIBUTE_TYPE = 2
MemDedicatedAttributeWriteLatency: win32more.Windows.Win32.System.Memory.MEM_DEDICATED_ATTRIBUTE_TYPE = 3
MemDedicatedAttributeMax: win32more.Windows.Win32.System.Memory.MEM_DEDICATED_ATTRIBUTE_TYPE = 4
class MEM_EXTENDED_PARAMETER(Structure):
    Anonymous1: _Anonymous1_e__Struct
    Anonymous2: _Anonymous2_e__Union
    class _Anonymous1_e__Struct(Structure):
        Type: Annotated[UInt64, 8]
        Reserved: Annotated[UInt64, 56]
    class _Anonymous2_e__Union(Union):
        ULong64: UInt64
        Pointer: VoidPtr
        Size: UIntPtr
        Handle: win32more.Windows.Win32.Foundation.HANDLE
        ULong: UInt32
MEM_EXTENDED_PARAMETER_TYPE = Int32
MemExtendedParameterInvalidType: win32more.Windows.Win32.System.Memory.MEM_EXTENDED_PARAMETER_TYPE = 0
MemExtendedParameterAddressRequirements: win32more.Windows.Win32.System.Memory.MEM_EXTENDED_PARAMETER_TYPE = 1
MemExtendedParameterNumaNode: win32more.Windows.Win32.System.Memory.MEM_EXTENDED_PARAMETER_TYPE = 2
MemExtendedParameterPartitionHandle: win32more.Windows.Win32.System.Memory.MEM_EXTENDED_PARAMETER_TYPE = 3
MemExtendedParameterUserPhysicalHandle: win32more.Windows.Win32.System.Memory.MEM_EXTENDED_PARAMETER_TYPE = 4
MemExtendedParameterAttributeFlags: win32more.Windows.Win32.System.Memory.MEM_EXTENDED_PARAMETER_TYPE = 5
MemExtendedParameterImageMachine: win32more.Windows.Win32.System.Memory.MEM_EXTENDED_PARAMETER_TYPE = 6
MemExtendedParameterMax: win32more.Windows.Win32.System.Memory.MEM_EXTENDED_PARAMETER_TYPE = 7
MEM_SECTION_EXTENDED_PARAMETER_TYPE = Int32
MemSectionExtendedParameterInvalidType: win32more.Windows.Win32.System.Memory.MEM_SECTION_EXTENDED_PARAMETER_TYPE = 0
MemSectionExtendedParameterUserPhysicalFlags: win32more.Windows.Win32.System.Memory.MEM_SECTION_EXTENDED_PARAMETER_TYPE = 1
MemSectionExtendedParameterNumaNode: win32more.Windows.Win32.System.Memory.MEM_SECTION_EXTENDED_PARAMETER_TYPE = 2
MemSectionExtendedParameterSigningLevel: win32more.Windows.Win32.System.Memory.MEM_SECTION_EXTENDED_PARAMETER_TYPE = 3
MemSectionExtendedParameterMax: win32more.Windows.Win32.System.Memory.MEM_SECTION_EXTENDED_PARAMETER_TYPE = 4
OFFER_PRIORITY = Int32
VmOfferPriorityVeryLow: win32more.Windows.Win32.System.Memory.OFFER_PRIORITY = 1
VmOfferPriorityLow: win32more.Windows.Win32.System.Memory.OFFER_PRIORITY = 2
VmOfferPriorityBelowNormal: win32more.Windows.Win32.System.Memory.OFFER_PRIORITY = 3
VmOfferPriorityNormal: win32more.Windows.Win32.System.Memory.OFFER_PRIORITY = 4
PAGE_PROTECTION_FLAGS = UInt32
PAGE_NOACCESS: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 1
PAGE_READONLY: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 2
PAGE_READWRITE: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 4
PAGE_WRITECOPY: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 8
PAGE_EXECUTE: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 16
PAGE_EXECUTE_READ: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 32
PAGE_EXECUTE_READWRITE: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 64
PAGE_EXECUTE_WRITECOPY: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 128
PAGE_GUARD: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 256
PAGE_NOCACHE: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 512
PAGE_WRITECOMBINE: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 1024
PAGE_GRAPHICS_NOACCESS: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 2048
PAGE_GRAPHICS_READONLY: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 4096
PAGE_GRAPHICS_READWRITE: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 8192
PAGE_GRAPHICS_EXECUTE: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 16384
PAGE_GRAPHICS_EXECUTE_READ: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 32768
PAGE_GRAPHICS_EXECUTE_READWRITE: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 65536
PAGE_GRAPHICS_COHERENT: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 131072
PAGE_GRAPHICS_NOCACHE: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 262144
PAGE_ENCLAVE_THREAD_CONTROL: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 2147483648
PAGE_REVERT_TO_FILE_MAP: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 2147483648
PAGE_TARGETS_NO_UPDATE: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 1073741824
PAGE_TARGETS_INVALID: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 1073741824
PAGE_ENCLAVE_UNVALIDATED: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 536870912
PAGE_ENCLAVE_MASK: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 268435456
PAGE_ENCLAVE_DECOMMIT: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 268435456
PAGE_ENCLAVE_SS_FIRST: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 268435457
PAGE_ENCLAVE_SS_REST: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 268435458
SEC_PARTITION_OWNER_HANDLE: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 262144
SEC_64K_PAGES: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 524288
SEC_FILE: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 8388608
SEC_IMAGE: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 16777216
SEC_PROTECTED_IMAGE: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 33554432
SEC_RESERVE: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 67108864
SEC_COMMIT: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 134217728
SEC_NOCACHE: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 268435456
SEC_WRITECOMBINE: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 1073741824
SEC_LARGE_PAGES: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 2147483648
SEC_IMAGE_NO_EXECUTE: win32more.Windows.Win32.System.Memory.PAGE_PROTECTION_FLAGS = 285212672
PAGE_TYPE = UInt32
MEM_PRIVATE: win32more.Windows.Win32.System.Memory.PAGE_TYPE = 131072
MEM_MAPPED: win32more.Windows.Win32.System.Memory.PAGE_TYPE = 262144
MEM_IMAGE: win32more.Windows.Win32.System.Memory.PAGE_TYPE = 16777216
@winfunctype_pointer
def PBAD_MEMORY_CALLBACK_ROUTINE() -> Void: ...
class PROCESS_HEAP_ENTRY(Structure):
    lpData: VoidPtr
    cbData: UInt32
    cbOverhead: Byte
    iRegionIndex: Byte
    wFlags: UInt16
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Block: _Block_e__Struct
        Region: _Region_e__Struct
        class _Block_e__Struct(Structure):
            hMem: win32more.Windows.Win32.Foundation.HANDLE
            dwReserved: UInt32 * 3
        class _Region_e__Struct(Structure):
            dwCommittedSize: UInt32
            dwUnCommittedSize: UInt32
            lpFirstBlock: VoidPtr
            lpLastBlock: VoidPtr
@winfunctype_pointer
def PSECURE_MEMORY_CACHE_CALLBACK(Addr: VoidPtr, Range: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
SECTION_FLAGS = UInt32
SECTION_ALL_ACCESS: win32more.Windows.Win32.System.Memory.SECTION_FLAGS = 983071
SECTION_QUERY: win32more.Windows.Win32.System.Memory.SECTION_FLAGS = 1
SECTION_MAP_WRITE: win32more.Windows.Win32.System.Memory.SECTION_FLAGS = 2
SECTION_MAP_READ: win32more.Windows.Win32.System.Memory.SECTION_FLAGS = 4
SECTION_MAP_EXECUTE: win32more.Windows.Win32.System.Memory.SECTION_FLAGS = 8
SECTION_EXTEND_SIZE: win32more.Windows.Win32.System.Memory.SECTION_FLAGS = 16
SECTION_MAP_EXECUTE_EXPLICIT: win32more.Windows.Win32.System.Memory.SECTION_FLAGS = 32
SETPROCESSWORKINGSETSIZEEX_FLAGS = UInt32
QUOTA_LIMITS_HARDWS_MIN_ENABLE: win32more.Windows.Win32.System.Memory.SETPROCESSWORKINGSETSIZEEX_FLAGS = 1
QUOTA_LIMITS_HARDWS_MIN_DISABLE: win32more.Windows.Win32.System.Memory.SETPROCESSWORKINGSETSIZEEX_FLAGS = 2
QUOTA_LIMITS_HARDWS_MAX_ENABLE: win32more.Windows.Win32.System.Memory.SETPROCESSWORKINGSETSIZEEX_FLAGS = 4
QUOTA_LIMITS_HARDWS_MAX_DISABLE: win32more.Windows.Win32.System.Memory.SETPROCESSWORKINGSETSIZEEX_FLAGS = 8
UNMAP_VIEW_OF_FILE_FLAGS = UInt32
MEM_UNMAP_NONE: win32more.Windows.Win32.System.Memory.UNMAP_VIEW_OF_FILE_FLAGS = 0
MEM_UNMAP_WITH_TRANSIENT_BOOST: win32more.Windows.Win32.System.Memory.UNMAP_VIEW_OF_FILE_FLAGS = 1
MEM_PRESERVE_PLACEHOLDER: win32more.Windows.Win32.System.Memory.UNMAP_VIEW_OF_FILE_FLAGS = 2
VIRTUAL_ALLOCATION_TYPE = UInt32
MEM_COMMIT: win32more.Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE = 4096
MEM_RESERVE: win32more.Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE = 8192
MEM_RESET: win32more.Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE = 524288
MEM_RESET_UNDO: win32more.Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE = 16777216
MEM_REPLACE_PLACEHOLDER: win32more.Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE = 16384
MEM_LARGE_PAGES: win32more.Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE = 536870912
MEM_RESERVE_PLACEHOLDER: win32more.Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE = 262144
MEM_FREE: win32more.Windows.Win32.System.Memory.VIRTUAL_ALLOCATION_TYPE = 65536
VIRTUAL_FREE_TYPE = UInt32
MEM_DECOMMIT: win32more.Windows.Win32.System.Memory.VIRTUAL_FREE_TYPE = 16384
MEM_RELEASE: win32more.Windows.Win32.System.Memory.VIRTUAL_FREE_TYPE = 32768
WIN32_MEMORY_INFORMATION_CLASS = Int32
MemoryRegionInfo: win32more.Windows.Win32.System.Memory.WIN32_MEMORY_INFORMATION_CLASS = 0
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
MemoryPartitionInfo: win32more.Windows.Win32.System.Memory.WIN32_MEMORY_PARTITION_INFORMATION_CLASS = 0
MemoryPartitionDedicatedMemoryInfo: win32more.Windows.Win32.System.Memory.WIN32_MEMORY_PARTITION_INFORMATION_CLASS = 1
class WIN32_MEMORY_RANGE_ENTRY(Structure):
    VirtualAddress: VoidPtr
    NumberOfBytes: UIntPtr
class WIN32_MEMORY_REGION_INFORMATION(Structure):
    AllocationBase: VoidPtr
    AllocationProtect: UInt32
    Anonymous: _Anonymous_e__Union
    RegionSize: UIntPtr
    CommitSize: UIntPtr
    class _Anonymous_e__Union(Union):
        Flags: UInt32
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            Private: Annotated[UInt32, 1]
            MappedDataFile: Annotated[UInt32, 1]
            MappedImage: Annotated[UInt32, 1]
            MappedPageFile: Annotated[UInt32, 1]
            MappedPhysical: Annotated[UInt32, 1]
            DirectMapped: Annotated[UInt32, 1]
            Reserved: Annotated[UInt32, 26]


make_ready(__name__)
