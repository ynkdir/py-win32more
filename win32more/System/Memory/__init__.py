from win32more import *
import win32more.Foundation
import win32more.Security
import win32more.System.Memory

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
FILE_CACHE_MAX_HARD_ENABLE = 1
FILE_CACHE_MAX_HARD_DISABLE = 2
FILE_CACHE_MIN_HARD_ENABLE = 4
FILE_CACHE_MIN_HARD_DISABLE = 8
MEHC_PATROL_SCRUBBER_PRESENT = 1
FILE_MAP = UInt32
FILE_MAP_WRITE = 2
FILE_MAP_READ = 4
FILE_MAP_ALL_ACCESS = 983071
FILE_MAP_EXECUTE = 32
FILE_MAP_COPY = 1
FILE_MAP_RESERVE = 2147483648
FILE_MAP_TARGETS_INVALID = 1073741824
FILE_MAP_LARGE_PAGES = 536870912
HEAP_FLAGS = UInt32
HEAP_NONE = 0
HEAP_NO_SERIALIZE = 1
HEAP_GROWABLE = 2
HEAP_GENERATE_EXCEPTIONS = 4
HEAP_ZERO_MEMORY = 8
HEAP_REALLOC_IN_PLACE_ONLY = 16
HEAP_TAIL_CHECKING_ENABLED = 32
HEAP_FREE_CHECKING_ENABLED = 64
HEAP_DISABLE_COALESCE_ON_FREE = 128
HEAP_CREATE_ALIGN_16 = 65536
HEAP_CREATE_ENABLE_TRACING = 131072
HEAP_CREATE_ENABLE_EXECUTE = 262144
HEAP_MAXIMUM_TAG = 4095
HEAP_PSEUDO_TAG_FLAG = 32768
HEAP_TAG_SHIFT = 18
HEAP_CREATE_SEGMENT_HEAP = 256
HEAP_CREATE_HARDENED = 512
PAGE_PROTECTION_FLAGS = UInt32
PAGE_NOACCESS = 1
PAGE_READONLY = 2
PAGE_READWRITE = 4
PAGE_WRITECOPY = 8
PAGE_EXECUTE = 16
PAGE_EXECUTE_READ = 32
PAGE_EXECUTE_READWRITE = 64
PAGE_EXECUTE_WRITECOPY = 128
PAGE_GUARD = 256
PAGE_NOCACHE = 512
PAGE_WRITECOMBINE = 1024
PAGE_GRAPHICS_NOACCESS = 2048
PAGE_GRAPHICS_READONLY = 4096
PAGE_GRAPHICS_READWRITE = 8192
PAGE_GRAPHICS_EXECUTE = 16384
PAGE_GRAPHICS_EXECUTE_READ = 32768
PAGE_GRAPHICS_EXECUTE_READWRITE = 65536
PAGE_GRAPHICS_COHERENT = 131072
PAGE_GRAPHICS_NOCACHE = 262144
PAGE_ENCLAVE_THREAD_CONTROL = 2147483648
PAGE_REVERT_TO_FILE_MAP = 2147483648
PAGE_TARGETS_NO_UPDATE = 1073741824
PAGE_TARGETS_INVALID = 1073741824
PAGE_ENCLAVE_UNVALIDATED = 536870912
PAGE_ENCLAVE_MASK = 268435456
PAGE_ENCLAVE_DECOMMIT = 268435456
PAGE_ENCLAVE_SS_FIRST = 268435457
PAGE_ENCLAVE_SS_REST = 268435458
SEC_PARTITION_OWNER_HANDLE = 262144
SEC_64K_PAGES = 524288
SEC_FILE = 8388608
SEC_IMAGE = 16777216
SEC_PROTECTED_IMAGE = 33554432
SEC_RESERVE = 67108864
SEC_COMMIT = 134217728
SEC_NOCACHE = 268435456
SEC_WRITECOMBINE = 1073741824
SEC_LARGE_PAGES = 2147483648
SEC_IMAGE_NO_EXECUTE = 285212672
UNMAP_VIEW_OF_FILE_FLAGS = UInt32
MEM_UNMAP_NONE = 0
MEM_UNMAP_WITH_TRANSIENT_BOOST = 1
MEM_PRESERVE_PLACEHOLDER = 2
VIRTUAL_FREE_TYPE = UInt32
MEM_DECOMMIT = 16384
MEM_RELEASE = 32768
VIRTUAL_ALLOCATION_TYPE = UInt32
MEM_COMMIT = 4096
MEM_RESERVE = 8192
MEM_RESET = 524288
MEM_RESET_UNDO = 16777216
MEM_REPLACE_PLACEHOLDER = 16384
MEM_LARGE_PAGES = 536870912
MEM_RESERVE_PLACEHOLDER = 262144
MEM_FREE = 65536
LOCAL_ALLOC_FLAGS = UInt32
LHND = 66
LMEM_FIXED = 0
LMEM_MOVEABLE = 2
LMEM_ZEROINIT = 64
LPTR = 64
NONZEROLHND = 2
NONZEROLPTR = 0
GLOBAL_ALLOC_FLAGS = UInt32
GHND = 66
GMEM_FIXED = 0
GMEM_MOVEABLE = 2
GMEM_ZEROINIT = 64
GPTR = 64
PAGE_TYPE = UInt32
MEM_PRIVATE = 131072
MEM_MAPPED = 262144
MEM_IMAGE = 16777216
HeapHandle = IntPtr
def _define_PROCESS_HEAP_ENTRY_head():
    class PROCESS_HEAP_ENTRY(Structure):
        pass
    return PROCESS_HEAP_ENTRY
def _define_PROCESS_HEAP_ENTRY():
    PROCESS_HEAP_ENTRY = win32more.System.Memory.PROCESS_HEAP_ENTRY_head
    class PROCESS_HEAP_ENTRY__Anonymous_e__Union(Union):
        pass
    class PROCESS_HEAP_ENTRY__Anonymous_e__Union__Block_e__Struct(Structure):
        pass
    PROCESS_HEAP_ENTRY__Anonymous_e__Union__Block_e__Struct._fields_ = [
        ("hMem", win32more.Foundation.HANDLE),
        ("dwReserved", UInt32 * 3),
    ]
    class PROCESS_HEAP_ENTRY__Anonymous_e__Union__Region_e__Struct(Structure):
        pass
    PROCESS_HEAP_ENTRY__Anonymous_e__Union__Region_e__Struct._fields_ = [
        ("dwCommittedSize", UInt32),
        ("dwUnCommittedSize", UInt32),
        ("lpFirstBlock", c_void_p),
        ("lpLastBlock", c_void_p),
    ]
    PROCESS_HEAP_ENTRY__Anonymous_e__Union._fields_ = [
        ("Block", PROCESS_HEAP_ENTRY__Anonymous_e__Union__Block_e__Struct),
        ("Region", PROCESS_HEAP_ENTRY__Anonymous_e__Union__Region_e__Struct),
    ]
    PROCESS_HEAP_ENTRY._anonymous_ = [
        'Anonymous',
    ]
    PROCESS_HEAP_ENTRY._fields_ = [
        ("lpData", c_void_p),
        ("cbData", UInt32),
        ("cbOverhead", Byte),
        ("iRegionIndex", Byte),
        ("wFlags", UInt16),
        ("Anonymous", PROCESS_HEAP_ENTRY__Anonymous_e__Union),
    ]
    return PROCESS_HEAP_ENTRY
def _define_HEAP_SUMMARY_head():
    class HEAP_SUMMARY(Structure):
        pass
    return HEAP_SUMMARY
def _define_HEAP_SUMMARY():
    HEAP_SUMMARY = win32more.System.Memory.HEAP_SUMMARY_head
    HEAP_SUMMARY._fields_ = [
        ("cb", UInt32),
        ("cbAllocated", UIntPtr),
        ("cbCommitted", UIntPtr),
        ("cbReserved", UIntPtr),
        ("cbMaxReserve", UIntPtr),
    ]
    return HEAP_SUMMARY
MEMORY_RESOURCE_NOTIFICATION_TYPE = Int32
MEMORY_RESOURCE_NOTIFICATION_TYPE_LowMemoryResourceNotification = 0
MEMORY_RESOURCE_NOTIFICATION_TYPE_HighMemoryResourceNotification = 1
def _define_WIN32_MEMORY_RANGE_ENTRY_head():
    class WIN32_MEMORY_RANGE_ENTRY(Structure):
        pass
    return WIN32_MEMORY_RANGE_ENTRY
def _define_WIN32_MEMORY_RANGE_ENTRY():
    WIN32_MEMORY_RANGE_ENTRY = win32more.System.Memory.WIN32_MEMORY_RANGE_ENTRY_head
    WIN32_MEMORY_RANGE_ENTRY._fields_ = [
        ("VirtualAddress", c_void_p),
        ("NumberOfBytes", UIntPtr),
    ]
    return WIN32_MEMORY_RANGE_ENTRY
def _define_PBAD_MEMORY_CALLBACK_ROUTINE():
    return CFUNCTYPE(Void, use_last_error=False)
OFFER_PRIORITY = Int32
OFFER_PRIORITY_VmOfferPriorityVeryLow = 1
OFFER_PRIORITY_VmOfferPriorityLow = 2
OFFER_PRIORITY_VmOfferPriorityBelowNormal = 3
OFFER_PRIORITY_VmOfferPriorityNormal = 4
WIN32_MEMORY_INFORMATION_CLASS = Int32
WIN32_MEMORY_INFORMATION_CLASS_MemoryRegionInfo = 0
def _define_WIN32_MEMORY_REGION_INFORMATION_head():
    class WIN32_MEMORY_REGION_INFORMATION(Structure):
        pass
    return WIN32_MEMORY_REGION_INFORMATION
def _define_WIN32_MEMORY_REGION_INFORMATION():
    WIN32_MEMORY_REGION_INFORMATION = win32more.System.Memory.WIN32_MEMORY_REGION_INFORMATION_head
    class WIN32_MEMORY_REGION_INFORMATION__Anonymous_e__Union(Union):
        pass
    class WIN32_MEMORY_REGION_INFORMATION__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    WIN32_MEMORY_REGION_INFORMATION__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("_bitfield", UInt32),
    ]
    WIN32_MEMORY_REGION_INFORMATION__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    WIN32_MEMORY_REGION_INFORMATION__Anonymous_e__Union._fields_ = [
        ("Flags", UInt32),
        ("Anonymous", WIN32_MEMORY_REGION_INFORMATION__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    WIN32_MEMORY_REGION_INFORMATION._anonymous_ = [
        'Anonymous',
    ]
    WIN32_MEMORY_REGION_INFORMATION._fields_ = [
        ("AllocationBase", c_void_p),
        ("AllocationProtect", UInt32),
        ("Anonymous", WIN32_MEMORY_REGION_INFORMATION__Anonymous_e__Union),
        ("RegionSize", UIntPtr),
        ("CommitSize", UIntPtr),
    ]
    return WIN32_MEMORY_REGION_INFORMATION
WIN32_MEMORY_PARTITION_INFORMATION_CLASS = Int32
WIN32_MEMORY_PARTITION_INFORMATION_CLASS_MemoryPartitionInfo = 0
WIN32_MEMORY_PARTITION_INFORMATION_CLASS_MemoryPartitionDedicatedMemoryInfo = 1
def _define_WIN32_MEMORY_PARTITION_INFORMATION_head():
    class WIN32_MEMORY_PARTITION_INFORMATION(Structure):
        pass
    return WIN32_MEMORY_PARTITION_INFORMATION
def _define_WIN32_MEMORY_PARTITION_INFORMATION():
    WIN32_MEMORY_PARTITION_INFORMATION = win32more.System.Memory.WIN32_MEMORY_PARTITION_INFORMATION_head
    WIN32_MEMORY_PARTITION_INFORMATION._fields_ = [
        ("Flags", UInt32),
        ("NumaNode", UInt32),
        ("Channel", UInt32),
        ("NumberOfNumaNodes", UInt32),
        ("ResidentAvailablePages", UInt64),
        ("CommittedPages", UInt64),
        ("CommitLimit", UInt64),
        ("PeakCommitment", UInt64),
        ("TotalNumberOfPages", UInt64),
        ("AvailablePages", UInt64),
        ("ZeroPages", UInt64),
        ("FreePages", UInt64),
        ("StandbyPages", UInt64),
        ("Reserved", UInt64 * 16),
        ("MaximumCommitLimit", UInt64),
        ("Reserved2", UInt64),
        ("PartitionId", UInt32),
    ]
    return WIN32_MEMORY_PARTITION_INFORMATION
def _define_MEMORY_BASIC_INFORMATION_head():
    class MEMORY_BASIC_INFORMATION(Structure):
        pass
    return MEMORY_BASIC_INFORMATION
def _define_MEMORY_BASIC_INFORMATION():
    MEMORY_BASIC_INFORMATION = win32more.System.Memory.MEMORY_BASIC_INFORMATION_head
    MEMORY_BASIC_INFORMATION._fields_ = [
        ("BaseAddress", c_void_p),
        ("AllocationBase", c_void_p),
        ("AllocationProtect", win32more.System.Memory.PAGE_PROTECTION_FLAGS),
        ("PartitionId", UInt16),
        ("RegionSize", UIntPtr),
        ("State", win32more.System.Memory.VIRTUAL_ALLOCATION_TYPE),
        ("Protect", win32more.System.Memory.PAGE_PROTECTION_FLAGS),
        ("Type", win32more.System.Memory.PAGE_TYPE),
    ]
    return MEMORY_BASIC_INFORMATION
def _define_MEMORY_BASIC_INFORMATION32_head():
    class MEMORY_BASIC_INFORMATION32(Structure):
        pass
    return MEMORY_BASIC_INFORMATION32
def _define_MEMORY_BASIC_INFORMATION32():
    MEMORY_BASIC_INFORMATION32 = win32more.System.Memory.MEMORY_BASIC_INFORMATION32_head
    MEMORY_BASIC_INFORMATION32._fields_ = [
        ("BaseAddress", UInt32),
        ("AllocationBase", UInt32),
        ("AllocationProtect", win32more.System.Memory.PAGE_PROTECTION_FLAGS),
        ("RegionSize", UInt32),
        ("State", win32more.System.Memory.VIRTUAL_ALLOCATION_TYPE),
        ("Protect", win32more.System.Memory.PAGE_PROTECTION_FLAGS),
        ("Type", win32more.System.Memory.PAGE_TYPE),
    ]
    return MEMORY_BASIC_INFORMATION32
def _define_MEMORY_BASIC_INFORMATION64_head():
    class MEMORY_BASIC_INFORMATION64(Structure):
        pass
    return MEMORY_BASIC_INFORMATION64
def _define_MEMORY_BASIC_INFORMATION64():
    MEMORY_BASIC_INFORMATION64 = win32more.System.Memory.MEMORY_BASIC_INFORMATION64_head
    MEMORY_BASIC_INFORMATION64._fields_ = [
        ("BaseAddress", UInt64),
        ("AllocationBase", UInt64),
        ("AllocationProtect", win32more.System.Memory.PAGE_PROTECTION_FLAGS),
        ("__alignment1", UInt32),
        ("RegionSize", UInt64),
        ("State", win32more.System.Memory.VIRTUAL_ALLOCATION_TYPE),
        ("Protect", win32more.System.Memory.PAGE_PROTECTION_FLAGS),
        ("Type", win32more.System.Memory.PAGE_TYPE),
        ("__alignment2", UInt32),
    ]
    return MEMORY_BASIC_INFORMATION64
def _define_CFG_CALL_TARGET_INFO_head():
    class CFG_CALL_TARGET_INFO(Structure):
        pass
    return CFG_CALL_TARGET_INFO
def _define_CFG_CALL_TARGET_INFO():
    CFG_CALL_TARGET_INFO = win32more.System.Memory.CFG_CALL_TARGET_INFO_head
    CFG_CALL_TARGET_INFO._fields_ = [
        ("Offset", UIntPtr),
        ("Flags", UIntPtr),
    ]
    return CFG_CALL_TARGET_INFO
MEM_EXTENDED_PARAMETER_TYPE = Int32
MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterInvalidType = 0
MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterAddressRequirements = 1
MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterNumaNode = 2
MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterPartitionHandle = 3
MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterUserPhysicalHandle = 4
MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterAttributeFlags = 5
MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterImageMachine = 6
MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterMax = 7
def _define_MEM_EXTENDED_PARAMETER_head():
    class MEM_EXTENDED_PARAMETER(Structure):
        pass
    return MEM_EXTENDED_PARAMETER
def _define_MEM_EXTENDED_PARAMETER():
    MEM_EXTENDED_PARAMETER = win32more.System.Memory.MEM_EXTENDED_PARAMETER_head
    class MEM_EXTENDED_PARAMETER__Anonymous2_e__Union(Union):
        pass
    MEM_EXTENDED_PARAMETER__Anonymous2_e__Union._fields_ = [
        ("ULong64", UInt64),
        ("Pointer", c_void_p),
        ("Size", UIntPtr),
        ("Handle", win32more.Foundation.HANDLE),
        ("ULong", UInt32),
    ]
    class MEM_EXTENDED_PARAMETER__Anonymous1_e__Struct(Structure):
        pass
    MEM_EXTENDED_PARAMETER__Anonymous1_e__Struct._fields_ = [
        ("_bitfield", UInt64),
    ]
    MEM_EXTENDED_PARAMETER._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    MEM_EXTENDED_PARAMETER._fields_ = [
        ("Anonymous1", MEM_EXTENDED_PARAMETER__Anonymous1_e__Struct),
        ("Anonymous2", MEM_EXTENDED_PARAMETER__Anonymous2_e__Union),
    ]
    return MEM_EXTENDED_PARAMETER
HEAP_INFORMATION_CLASS = Int32
HEAP_INFORMATION_CLASS_HeapCompatibilityInformation = 0
HEAP_INFORMATION_CLASS_HeapEnableTerminationOnCorruption = 1
HEAP_INFORMATION_CLASS_HeapOptimizeResources = 3
HEAP_INFORMATION_CLASS_HeapTag = 7
def _define_PSECURE_MEMORY_CACHE_CALLBACK():
    return CFUNCTYPE(win32more.Foundation.BOOLEAN,c_void_p,UIntPtr, use_last_error=False)
def _define_HeapCreate():
    try:
        return WINFUNCTYPE(win32more.System.Memory.HeapHandle,win32more.System.Memory.HEAP_FLAGS,UIntPtr,UIntPtr, use_last_error=True)(("HeapCreate", windll["KERNEL32"]), ((1, 'flOptions'),(1, 'dwInitialSize'),(1, 'dwMaximumSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HeapDestroy():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Memory.HeapHandle, use_last_error=True)(("HeapDestroy", windll["KERNEL32"]), ((1, 'hHeap'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HeapAlloc():
    try:
        return WINFUNCTYPE(c_void_p,win32more.System.Memory.HeapHandle,win32more.System.Memory.HEAP_FLAGS,UIntPtr, use_last_error=False)(("HeapAlloc", windll["KERNEL32"]), ((1, 'hHeap'),(1, 'dwFlags'),(1, 'dwBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HeapReAlloc():
    try:
        return WINFUNCTYPE(c_void_p,win32more.System.Memory.HeapHandle,win32more.System.Memory.HEAP_FLAGS,c_void_p,UIntPtr, use_last_error=False)(("HeapReAlloc", windll["KERNEL32"]), ((1, 'hHeap'),(1, 'dwFlags'),(1, 'lpMem'),(1, 'dwBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HeapFree():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Memory.HeapHandle,win32more.System.Memory.HEAP_FLAGS,c_void_p, use_last_error=True)(("HeapFree", windll["KERNEL32"]), ((1, 'hHeap'),(1, 'dwFlags'),(1, 'lpMem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HeapSize():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.System.Memory.HeapHandle,win32more.System.Memory.HEAP_FLAGS,c_void_p, use_last_error=False)(("HeapSize", windll["KERNEL32"]), ((1, 'hHeap'),(1, 'dwFlags'),(1, 'lpMem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProcessHeap():
    try:
        return WINFUNCTYPE(win32more.System.Memory.HeapHandle, use_last_error=True)(("GetProcessHeap", windll["KERNEL32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_HeapCompact():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.System.Memory.HeapHandle,win32more.System.Memory.HEAP_FLAGS, use_last_error=True)(("HeapCompact", windll["KERNEL32"]), ((1, 'hHeap'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HeapSetInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Memory.HeapHandle,win32more.System.Memory.HEAP_INFORMATION_CLASS,c_void_p,UIntPtr, use_last_error=True)(("HeapSetInformation", windll["KERNEL32"]), ((1, 'HeapHandle'),(1, 'HeapInformationClass'),(1, 'HeapInformation'),(1, 'HeapInformationLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HeapValidate():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Memory.HeapHandle,win32more.System.Memory.HEAP_FLAGS,c_void_p, use_last_error=False)(("HeapValidate", windll["KERNEL32"]), ((1, 'hHeap'),(1, 'dwFlags'),(1, 'lpMem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HeapSummary():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,POINTER(win32more.System.Memory.HEAP_SUMMARY_head), use_last_error=False)(("HeapSummary", windll["KERNEL32"]), ((1, 'hHeap'),(1, 'dwFlags'),(1, 'lpSummary'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProcessHeaps():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(win32more.System.Memory.HeapHandle), use_last_error=True)(("GetProcessHeaps", windll["KERNEL32"]), ((1, 'NumberOfHeaps'),(1, 'ProcessHeaps'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HeapLock():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Memory.HeapHandle, use_last_error=True)(("HeapLock", windll["KERNEL32"]), ((1, 'hHeap'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HeapUnlock():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Memory.HeapHandle, use_last_error=True)(("HeapUnlock", windll["KERNEL32"]), ((1, 'hHeap'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HeapWalk():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Memory.HeapHandle,POINTER(win32more.System.Memory.PROCESS_HEAP_ENTRY_head), use_last_error=True)(("HeapWalk", windll["KERNEL32"]), ((1, 'hHeap'),(1, 'lpEntry'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HeapQueryInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Memory.HeapHandle,win32more.System.Memory.HEAP_INFORMATION_CLASS,c_void_p,UIntPtr,POINTER(UIntPtr), use_last_error=True)(("HeapQueryInformation", windll["KERNEL32"]), ((1, 'HeapHandle'),(1, 'HeapInformationClass'),(1, 'HeapInformation'),(1, 'HeapInformationLength'),(1, 'ReturnLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VirtualAlloc():
    try:
        return WINFUNCTYPE(c_void_p,c_void_p,UIntPtr,win32more.System.Memory.VIRTUAL_ALLOCATION_TYPE,win32more.System.Memory.PAGE_PROTECTION_FLAGS, use_last_error=True)(("VirtualAlloc", windll["KERNEL32"]), ((1, 'lpAddress'),(1, 'dwSize'),(1, 'flAllocationType'),(1, 'flProtect'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VirtualProtect():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,UIntPtr,win32more.System.Memory.PAGE_PROTECTION_FLAGS,POINTER(win32more.System.Memory.PAGE_PROTECTION_FLAGS), use_last_error=True)(("VirtualProtect", windll["KERNEL32"]), ((1, 'lpAddress'),(1, 'dwSize'),(1, 'flNewProtect'),(1, 'lpflOldProtect'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VirtualFree():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,UIntPtr,win32more.System.Memory.VIRTUAL_FREE_TYPE, use_last_error=True)(("VirtualFree", windll["KERNEL32"]), ((1, 'lpAddress'),(1, 'dwSize'),(1, 'dwFreeType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VirtualQuery():
    try:
        return WINFUNCTYPE(UIntPtr,c_void_p,POINTER(win32more.System.Memory.MEMORY_BASIC_INFORMATION_head),UIntPtr, use_last_error=True)(("VirtualQuery", windll["KERNEL32"]), ((1, 'lpAddress'),(1, 'lpBuffer'),(1, 'dwLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VirtualAllocEx():
    try:
        return WINFUNCTYPE(c_void_p,win32more.Foundation.HANDLE,c_void_p,UIntPtr,win32more.System.Memory.VIRTUAL_ALLOCATION_TYPE,win32more.System.Memory.PAGE_PROTECTION_FLAGS, use_last_error=True)(("VirtualAllocEx", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'lpAddress'),(1, 'dwSize'),(1, 'flAllocationType'),(1, 'flProtect'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VirtualProtectEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,UIntPtr,win32more.System.Memory.PAGE_PROTECTION_FLAGS,POINTER(win32more.System.Memory.PAGE_PROTECTION_FLAGS), use_last_error=True)(("VirtualProtectEx", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'lpAddress'),(1, 'dwSize'),(1, 'flNewProtect'),(1, 'lpflOldProtect'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VirtualQueryEx():
    try:
        return WINFUNCTYPE(UIntPtr,win32more.Foundation.HANDLE,c_void_p,POINTER(win32more.System.Memory.MEMORY_BASIC_INFORMATION_head),UIntPtr, use_last_error=True)(("VirtualQueryEx", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'lpAddress'),(1, 'lpBuffer'),(1, 'dwLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateFileMappingW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.System.Memory.PAGE_PROTECTION_FLAGS,UInt32,UInt32,win32more.Foundation.PWSTR, use_last_error=True)(("CreateFileMappingW", windll["KERNEL32"]), ((1, 'hFile'),(1, 'lpFileMappingAttributes'),(1, 'flProtect'),(1, 'dwMaximumSizeHigh'),(1, 'dwMaximumSizeLow'),(1, 'lpName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateFileMapping():
    return win32more.System.Memory.CreateFileMappingW
def _define_OpenFileMappingW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,UInt32,win32more.Foundation.BOOL,win32more.Foundation.PWSTR, use_last_error=True)(("OpenFileMappingW", windll["KERNEL32"]), ((1, 'dwDesiredAccess'),(1, 'bInheritHandle'),(1, 'lpName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenFileMapping():
    return win32more.System.Memory.OpenFileMappingW
def _define_MapViewOfFile():
    try:
        return WINFUNCTYPE(c_void_p,win32more.Foundation.HANDLE,win32more.System.Memory.FILE_MAP,UInt32,UInt32,UIntPtr, use_last_error=True)(("MapViewOfFile", windll["KERNEL32"]), ((1, 'hFileMappingObject'),(1, 'dwDesiredAccess'),(1, 'dwFileOffsetHigh'),(1, 'dwFileOffsetLow'),(1, 'dwNumberOfBytesToMap'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MapViewOfFileEx():
    try:
        return WINFUNCTYPE(c_void_p,win32more.Foundation.HANDLE,win32more.System.Memory.FILE_MAP,UInt32,UInt32,UIntPtr,c_void_p, use_last_error=True)(("MapViewOfFileEx", windll["KERNEL32"]), ((1, 'hFileMappingObject'),(1, 'dwDesiredAccess'),(1, 'dwFileOffsetHigh'),(1, 'dwFileOffsetLow'),(1, 'dwNumberOfBytesToMap'),(1, 'lpBaseAddress'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VirtualFreeEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,UIntPtr,win32more.System.Memory.VIRTUAL_FREE_TYPE, use_last_error=True)(("VirtualFreeEx", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'lpAddress'),(1, 'dwSize'),(1, 'dwFreeType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FlushViewOfFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,UIntPtr, use_last_error=True)(("FlushViewOfFile", windll["KERNEL32"]), ((1, 'lpBaseAddress'),(1, 'dwNumberOfBytesToFlush'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnmapViewOfFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p, use_last_error=True)(("UnmapViewOfFile", windll["KERNEL32"]), ((1, 'lpBaseAddress'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetLargePageMinimum():
    try:
        return WINFUNCTYPE(UIntPtr, use_last_error=False)(("GetLargePageMinimum", windll["KERNEL32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetProcessWorkingSetSizeEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UIntPtr),POINTER(UIntPtr),POINTER(UInt32), use_last_error=False)(("GetProcessWorkingSetSizeEx", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'lpMinimumWorkingSetSize'),(1, 'lpMaximumWorkingSetSize'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetProcessWorkingSetSizeEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UIntPtr,UIntPtr,UInt32, use_last_error=True)(("SetProcessWorkingSetSizeEx", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'dwMinimumWorkingSetSize'),(1, 'dwMaximumWorkingSetSize'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VirtualLock():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,UIntPtr, use_last_error=True)(("VirtualLock", windll["KERNEL32"]), ((1, 'lpAddress'),(1, 'dwSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VirtualUnlock():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,UIntPtr, use_last_error=True)(("VirtualUnlock", windll["KERNEL32"]), ((1, 'lpAddress'),(1, 'dwSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetWriteWatch():
    try:
        return WINFUNCTYPE(UInt32,UInt32,c_void_p,UIntPtr,POINTER(c_void_p),POINTER(UIntPtr),POINTER(UInt32), use_last_error=False)(("GetWriteWatch", windll["KERNEL32"]), ((1, 'dwFlags'),(1, 'lpBaseAddress'),(1, 'dwRegionSize'),(1, 'lpAddresses'),(1, 'lpdwCount'),(1, 'lpdwGranularity'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ResetWriteWatch():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UIntPtr, use_last_error=False)(("ResetWriteWatch", windll["KERNEL32"]), ((1, 'lpBaseAddress'),(1, 'dwRegionSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateMemoryResourceNotification():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.System.Memory.MEMORY_RESOURCE_NOTIFICATION_TYPE, use_last_error=True)(("CreateMemoryResourceNotification", windll["KERNEL32"]), ((1, 'NotificationType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryMemoryResourceNotification():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.BOOL), use_last_error=True)(("QueryMemoryResourceNotification", windll["KERNEL32"]), ((1, 'ResourceNotificationHandle'),(1, 'ResourceState'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSystemFileCacheSize():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(UIntPtr),POINTER(UIntPtr),POINTER(UInt32), use_last_error=True)(("GetSystemFileCacheSize", windll["KERNEL32"]), ((1, 'lpMinimumFileCacheSize'),(1, 'lpMaximumFileCacheSize'),(1, 'lpFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetSystemFileCacheSize():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UIntPtr,UIntPtr,UInt32, use_last_error=True)(("SetSystemFileCacheSize", windll["KERNEL32"]), ((1, 'MinimumFileCacheSize'),(1, 'MaximumFileCacheSize'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateFileMappingNumaW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.System.Memory.PAGE_PROTECTION_FLAGS,UInt32,UInt32,win32more.Foundation.PWSTR,UInt32, use_last_error=True)(("CreateFileMappingNumaW", windll["KERNEL32"]), ((1, 'hFile'),(1, 'lpFileMappingAttributes'),(1, 'flProtect'),(1, 'dwMaximumSizeHigh'),(1, 'dwMaximumSizeLow'),(1, 'lpName'),(1, 'nndPreferred'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateFileMappingNuma():
    return win32more.System.Memory.CreateFileMappingNumaW
def _define_PrefetchVirtualMemory():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UIntPtr,POINTER(win32more.System.Memory.WIN32_MEMORY_RANGE_ENTRY),UInt32, use_last_error=True)(("PrefetchVirtualMemory", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'NumberOfEntries'),(1, 'VirtualAddresses'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateFileMappingFromApp():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.System.Memory.PAGE_PROTECTION_FLAGS,UInt64,win32more.Foundation.PWSTR, use_last_error=True)(("CreateFileMappingFromApp", windll["KERNEL32"]), ((1, 'hFile'),(1, 'SecurityAttributes'),(1, 'PageProtection'),(1, 'MaximumSize'),(1, 'Name'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MapViewOfFileFromApp():
    try:
        return WINFUNCTYPE(c_void_p,win32more.Foundation.HANDLE,win32more.System.Memory.FILE_MAP,UInt64,UIntPtr, use_last_error=True)(("MapViewOfFileFromApp", windll["KERNEL32"]), ((1, 'hFileMappingObject'),(1, 'DesiredAccess'),(1, 'FileOffset'),(1, 'NumberOfBytesToMap'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnmapViewOfFileEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,win32more.System.Memory.UNMAP_VIEW_OF_FILE_FLAGS, use_last_error=True)(("UnmapViewOfFileEx", windll["KERNEL32"]), ((1, 'BaseAddress'),(1, 'UnmapFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AllocateUserPhysicalPages():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UIntPtr),POINTER(UIntPtr), use_last_error=True)(("AllocateUserPhysicalPages", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'NumberOfPages'),(1, 'PageArray'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FreeUserPhysicalPages():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UIntPtr),POINTER(UIntPtr), use_last_error=True)(("FreeUserPhysicalPages", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'NumberOfPages'),(1, 'PageArray'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MapUserPhysicalPages():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,UIntPtr,POINTER(UIntPtr), use_last_error=True)(("MapUserPhysicalPages", windll["KERNEL32"]), ((1, 'VirtualAddress'),(1, 'NumberOfPages'),(1, 'PageArray'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AllocateUserPhysicalPagesNuma():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UIntPtr),POINTER(UIntPtr),UInt32, use_last_error=True)(("AllocateUserPhysicalPagesNuma", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'NumberOfPages'),(1, 'PageArray'),(1, 'nndPreferred'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VirtualAllocExNuma():
    try:
        return WINFUNCTYPE(c_void_p,win32more.Foundation.HANDLE,c_void_p,UIntPtr,win32more.System.Memory.VIRTUAL_ALLOCATION_TYPE,UInt32,UInt32, use_last_error=True)(("VirtualAllocExNuma", windll["KERNEL32"]), ((1, 'hProcess'),(1, 'lpAddress'),(1, 'dwSize'),(1, 'flAllocationType'),(1, 'flProtect'),(1, 'nndPreferred'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetMemoryErrorHandlingCapabilities():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(UInt32), use_last_error=True)(("GetMemoryErrorHandlingCapabilities", windll["KERNEL32"]), ((1, 'Capabilities'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterBadMemoryNotification():
    try:
        return WINFUNCTYPE(c_void_p,win32more.System.Memory.PBAD_MEMORY_CALLBACK_ROUTINE, use_last_error=False)(("RegisterBadMemoryNotification", windll["KERNEL32"]), ((1, 'Callback'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnregisterBadMemoryNotification():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p, use_last_error=True)(("UnregisterBadMemoryNotification", windll["KERNEL32"]), ((1, 'RegistrationHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OfferVirtualMemory():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Void),UIntPtr,win32more.System.Memory.OFFER_PRIORITY, use_last_error=False)(("OfferVirtualMemory", windll["KERNEL32"]), ((1, 'VirtualAddress'),(1, 'Size'),(1, 'Priority'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReclaimVirtualMemory():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Void),UIntPtr, use_last_error=False)(("ReclaimVirtualMemory", windll["KERNEL32"]), ((1, 'VirtualAddress'),(1, 'Size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DiscardVirtualMemory():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Void),UIntPtr, use_last_error=False)(("DiscardVirtualMemory", windll["KERNEL32"]), ((1, 'VirtualAddress'),(1, 'Size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetProcessValidCallTargets():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,UIntPtr,UInt32,POINTER(win32more.System.Memory.CFG_CALL_TARGET_INFO), use_last_error=True)(("SetProcessValidCallTargets", windll["api-ms-win-core-memory-l1-1-3"]), ((1, 'hProcess'),(1, 'VirtualAddress'),(1, 'RegionSize'),(1, 'NumberOfOffsets'),(1, 'OffsetInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetProcessValidCallTargetsForMappedView():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,UIntPtr,UInt32,POINTER(win32more.System.Memory.CFG_CALL_TARGET_INFO),win32more.Foundation.HANDLE,UInt64, use_last_error=False)(("SetProcessValidCallTargetsForMappedView", windll["api-ms-win-core-memory-l1-1-7"]), ((1, 'Process'),(1, 'VirtualAddress'),(1, 'RegionSize'),(1, 'NumberOfOffsets'),(1, 'OffsetInformation'),(1, 'Section'),(1, 'ExpectedFileOffset'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VirtualAllocFromApp():
    try:
        return WINFUNCTYPE(c_void_p,c_void_p,UIntPtr,win32more.System.Memory.VIRTUAL_ALLOCATION_TYPE,UInt32, use_last_error=True)(("VirtualAllocFromApp", windll["api-ms-win-core-memory-l1-1-3"]), ((1, 'BaseAddress'),(1, 'Size'),(1, 'AllocationType'),(1, 'Protection'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VirtualProtectFromApp():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,UIntPtr,UInt32,POINTER(UInt32), use_last_error=True)(("VirtualProtectFromApp", windll["api-ms-win-core-memory-l1-1-3"]), ((1, 'Address'),(1, 'Size'),(1, 'NewProtection'),(1, 'OldProtection'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenFileMappingFromApp():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,UInt32,win32more.Foundation.BOOL,win32more.Foundation.PWSTR, use_last_error=True)(("OpenFileMappingFromApp", windll["api-ms-win-core-memory-l1-1-3"]), ((1, 'DesiredAccess'),(1, 'InheritHandle'),(1, 'Name'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryVirtualMemoryInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,win32more.System.Memory.WIN32_MEMORY_INFORMATION_CLASS,c_void_p,UIntPtr,POINTER(UIntPtr), use_last_error=True)(("QueryVirtualMemoryInformation", windll["api-ms-win-core-memory-l1-1-4"]), ((1, 'Process'),(1, 'VirtualAddress'),(1, 'MemoryInformationClass'),(1, 'MemoryInformation'),(1, 'MemoryInformationSize'),(1, 'ReturnSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MapViewOfFileNuma2():
    try:
        return WINFUNCTYPE(c_void_p,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,UInt64,c_void_p,UIntPtr,UInt32,UInt32,UInt32, use_last_error=True)(("MapViewOfFileNuma2", windll["api-ms-win-core-memory-l1-1-5"]), ((1, 'FileMappingHandle'),(1, 'ProcessHandle'),(1, 'Offset'),(1, 'BaseAddress'),(1, 'ViewSize'),(1, 'AllocationType'),(1, 'PageProtection'),(1, 'PreferredNode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnmapViewOfFile2():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,win32more.System.Memory.UNMAP_VIEW_OF_FILE_FLAGS, use_last_error=True)(("UnmapViewOfFile2", windll["api-ms-win-core-memory-l1-1-5"]), ((1, 'Process'),(1, 'BaseAddress'),(1, 'UnmapFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VirtualUnlockEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,UIntPtr, use_last_error=False)(("VirtualUnlockEx", windll["api-ms-win-core-memory-l1-1-5"]), ((1, 'Process'),(1, 'Address'),(1, 'Size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VirtualAlloc2():
    try:
        return WINFUNCTYPE(c_void_p,win32more.Foundation.HANDLE,c_void_p,UIntPtr,win32more.System.Memory.VIRTUAL_ALLOCATION_TYPE,UInt32,POINTER(win32more.System.Memory.MEM_EXTENDED_PARAMETER),UInt32, use_last_error=True)(("VirtualAlloc2", windll["api-ms-win-core-memory-l1-1-6"]), ((1, 'Process'),(1, 'BaseAddress'),(1, 'Size'),(1, 'AllocationType'),(1, 'PageProtection'),(1, 'ExtendedParameters'),(1, 'ParameterCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MapViewOfFile3():
    try:
        return WINFUNCTYPE(c_void_p,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,c_void_p,UInt64,UIntPtr,win32more.System.Memory.VIRTUAL_ALLOCATION_TYPE,UInt32,POINTER(win32more.System.Memory.MEM_EXTENDED_PARAMETER),UInt32, use_last_error=True)(("MapViewOfFile3", windll["api-ms-win-core-memory-l1-1-6"]), ((1, 'FileMapping'),(1, 'Process'),(1, 'BaseAddress'),(1, 'Offset'),(1, 'ViewSize'),(1, 'AllocationType'),(1, 'PageProtection'),(1, 'ExtendedParameters'),(1, 'ParameterCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VirtualAlloc2FromApp():
    try:
        return WINFUNCTYPE(c_void_p,win32more.Foundation.HANDLE,c_void_p,UIntPtr,win32more.System.Memory.VIRTUAL_ALLOCATION_TYPE,UInt32,POINTER(win32more.System.Memory.MEM_EXTENDED_PARAMETER),UInt32, use_last_error=True)(("VirtualAlloc2FromApp", windll["api-ms-win-core-memory-l1-1-6"]), ((1, 'Process'),(1, 'BaseAddress'),(1, 'Size'),(1, 'AllocationType'),(1, 'PageProtection'),(1, 'ExtendedParameters'),(1, 'ParameterCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MapViewOfFile3FromApp():
    try:
        return WINFUNCTYPE(c_void_p,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,c_void_p,UInt64,UIntPtr,win32more.System.Memory.VIRTUAL_ALLOCATION_TYPE,UInt32,POINTER(win32more.System.Memory.MEM_EXTENDED_PARAMETER),UInt32, use_last_error=True)(("MapViewOfFile3FromApp", windll["api-ms-win-core-memory-l1-1-6"]), ((1, 'FileMapping'),(1, 'Process'),(1, 'BaseAddress'),(1, 'Offset'),(1, 'ViewSize'),(1, 'AllocationType'),(1, 'PageProtection'),(1, 'ExtendedParameters'),(1, 'ParameterCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateFileMapping2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),UInt32,win32more.System.Memory.PAGE_PROTECTION_FLAGS,UInt32,UInt64,win32more.Foundation.PWSTR,POINTER(win32more.System.Memory.MEM_EXTENDED_PARAMETER),UInt32, use_last_error=True)(("CreateFileMapping2", windll["api-ms-win-core-memory-l1-1-7"]), ((1, 'File'),(1, 'SecurityAttributes'),(1, 'DesiredAccess'),(1, 'PageProtection'),(1, 'AllocationAttributes'),(1, 'MaximumSize'),(1, 'Name'),(1, 'ExtendedParameters'),(1, 'ParameterCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AllocateUserPhysicalPages2():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UIntPtr),POINTER(UIntPtr),POINTER(win32more.System.Memory.MEM_EXTENDED_PARAMETER),UInt32, use_last_error=False)(("AllocateUserPhysicalPages2", windll["api-ms-win-core-memory-l1-1-8"]), ((1, 'ObjectHandle'),(1, 'NumberOfPages'),(1, 'PageArray'),(1, 'ExtendedParameters'),(1, 'ExtendedParameterCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenDedicatedMemoryPartition():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,UInt64,UInt32,win32more.Foundation.BOOL, use_last_error=False)(("OpenDedicatedMemoryPartition", windll["api-ms-win-core-memory-l1-1-8"]), ((1, 'Partition'),(1, 'DedicatedMemoryTypeId'),(1, 'DesiredAccess'),(1, 'InheritHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryPartitionInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.System.Memory.WIN32_MEMORY_PARTITION_INFORMATION_CLASS,c_void_p,UInt32, use_last_error=False)(("QueryPartitionInformation", windll["api-ms-win-core-memory-l1-1-8"]), ((1, 'Partition'),(1, 'PartitionInformationClass'),(1, 'PartitionInformation'),(1, 'PartitionInformationLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlCompareMemory():
    try:
        return WINFUNCTYPE(UIntPtr,c_void_p,c_void_p,UIntPtr, use_last_error=False)(("RtlCompareMemory", windll["KERNEL32"]), ((1, 'Source1'),(1, 'Source2'),(1, 'Length'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlCrc32():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UIntPtr,UInt32, use_last_error=False)(("RtlCrc32", windll["ntdll"]), ((1, 'Buffer'),(1, 'Size'),(1, 'InitialCrc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlCrc64():
    try:
        return WINFUNCTYPE(UInt64,c_void_p,UIntPtr,UInt64, use_last_error=False)(("RtlCrc64", windll["ntdll"]), ((1, 'Buffer'),(1, 'Size'),(1, 'InitialCrc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlIsZeroMemory():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,c_void_p,UIntPtr, use_last_error=False)(("RtlIsZeroMemory", windll["ntdll"]), ((1, 'Buffer'),(1, 'Length'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalAlloc():
    try:
        return WINFUNCTYPE(IntPtr,win32more.System.Memory.GLOBAL_ALLOC_FLAGS,UIntPtr, use_last_error=True)(("GlobalAlloc", windll["KERNEL32"]), ((1, 'uFlags'),(1, 'dwBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalReAlloc():
    try:
        return WINFUNCTYPE(IntPtr,IntPtr,UIntPtr,UInt32, use_last_error=True)(("GlobalReAlloc", windll["KERNEL32"]), ((1, 'hMem'),(1, 'dwBytes'),(1, 'uFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalSize():
    try:
        return WINFUNCTYPE(UIntPtr,IntPtr, use_last_error=True)(("GlobalSize", windll["KERNEL32"]), ((1, 'hMem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalUnlock():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr, use_last_error=True)(("GlobalUnlock", windll["KERNEL32"]), ((1, 'hMem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalLock():
    try:
        return WINFUNCTYPE(c_void_p,IntPtr, use_last_error=True)(("GlobalLock", windll["KERNEL32"]), ((1, 'hMem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalFlags():
    try:
        return WINFUNCTYPE(UInt32,IntPtr, use_last_error=True)(("GlobalFlags", windll["KERNEL32"]), ((1, 'hMem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalHandle():
    try:
        return WINFUNCTYPE(IntPtr,c_void_p, use_last_error=True)(("GlobalHandle", windll["KERNEL32"]), ((1, 'pMem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalFree():
    try:
        return WINFUNCTYPE(IntPtr,IntPtr, use_last_error=True)(("GlobalFree", windll["KERNEL32"]), ((1, 'hMem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LocalAlloc():
    try:
        return WINFUNCTYPE(IntPtr,win32more.System.Memory.LOCAL_ALLOC_FLAGS,UIntPtr, use_last_error=True)(("LocalAlloc", windll["KERNEL32"]), ((1, 'uFlags'),(1, 'uBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LocalReAlloc():
    try:
        return WINFUNCTYPE(IntPtr,IntPtr,UIntPtr,UInt32, use_last_error=True)(("LocalReAlloc", windll["KERNEL32"]), ((1, 'hMem'),(1, 'uBytes'),(1, 'uFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LocalLock():
    try:
        return WINFUNCTYPE(c_void_p,IntPtr, use_last_error=True)(("LocalLock", windll["KERNEL32"]), ((1, 'hMem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LocalHandle():
    try:
        return WINFUNCTYPE(IntPtr,c_void_p, use_last_error=True)(("LocalHandle", windll["KERNEL32"]), ((1, 'pMem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LocalUnlock():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr, use_last_error=True)(("LocalUnlock", windll["KERNEL32"]), ((1, 'hMem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LocalSize():
    try:
        return WINFUNCTYPE(UIntPtr,IntPtr, use_last_error=True)(("LocalSize", windll["KERNEL32"]), ((1, 'hMem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LocalFlags():
    try:
        return WINFUNCTYPE(UInt32,IntPtr, use_last_error=True)(("LocalFlags", windll["KERNEL32"]), ((1, 'hMem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LocalFree():
    try:
        return WINFUNCTYPE(IntPtr,IntPtr, use_last_error=True)(("LocalFree", windll["KERNEL32"]), ((1, 'hMem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateFileMappingA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.System.Memory.PAGE_PROTECTION_FLAGS,UInt32,UInt32,win32more.Foundation.PSTR, use_last_error=True)(("CreateFileMappingA", windll["KERNEL32"]), ((1, 'hFile'),(1, 'lpFileMappingAttributes'),(1, 'flProtect'),(1, 'dwMaximumSizeHigh'),(1, 'dwMaximumSizeLow'),(1, 'lpName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateFileMappingNumaA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.System.Memory.PAGE_PROTECTION_FLAGS,UInt32,UInt32,win32more.Foundation.PSTR,UInt32, use_last_error=True)(("CreateFileMappingNumaA", windll["KERNEL32"]), ((1, 'hFile'),(1, 'lpFileMappingAttributes'),(1, 'flProtect'),(1, 'dwMaximumSizeHigh'),(1, 'dwMaximumSizeLow'),(1, 'lpName'),(1, 'nndPreferred'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenFileMappingA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,UInt32,win32more.Foundation.BOOL,win32more.Foundation.PSTR, use_last_error=True)(("OpenFileMappingA", windll["KERNEL32"]), ((1, 'dwDesiredAccess'),(1, 'bInheritHandle'),(1, 'lpName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MapViewOfFileExNuma():
    try:
        return WINFUNCTYPE(c_void_p,win32more.Foundation.HANDLE,win32more.System.Memory.FILE_MAP,UInt32,UInt32,UIntPtr,c_void_p,UInt32, use_last_error=True)(("MapViewOfFileExNuma", windll["KERNEL32"]), ((1, 'hFileMappingObject'),(1, 'dwDesiredAccess'),(1, 'dwFileOffsetHigh'),(1, 'dwFileOffsetLow'),(1, 'dwNumberOfBytesToMap'),(1, 'lpBaseAddress'),(1, 'nndPreferred'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsBadReadPtr():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,UIntPtr, use_last_error=False)(("IsBadReadPtr", windll["KERNEL32"]), ((1, 'lp'),(1, 'ucb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsBadWritePtr():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,UIntPtr, use_last_error=False)(("IsBadWritePtr", windll["KERNEL32"]), ((1, 'lp'),(1, 'ucb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsBadCodePtr():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.FARPROC, use_last_error=True)(("IsBadCodePtr", windll["KERNEL32"]), ((1, 'lpfn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsBadStringPtrA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,UIntPtr, use_last_error=False)(("IsBadStringPtrA", windll["KERNEL32"]), ((1, 'lpsz'),(1, 'ucchMax'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsBadStringPtrW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UIntPtr, use_last_error=False)(("IsBadStringPtrW", windll["KERNEL32"]), ((1, 'lpsz'),(1, 'ucchMax'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsBadStringPtr():
    return win32more.System.Memory.IsBadStringPtrW
def _define_MapUserPhysicalPagesScatter():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(c_void_p),UIntPtr,POINTER(UIntPtr), use_last_error=True)(("MapUserPhysicalPagesScatter", windll["KERNEL32"]), ((1, 'VirtualAddresses'),(1, 'NumberOfPages'),(1, 'PageArray'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddSecureMemoryCacheCallback():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Memory.PSECURE_MEMORY_CACHE_CALLBACK, use_last_error=True)(("AddSecureMemoryCacheCallback", windll["KERNEL32"]), ((1, 'pfnCallBack'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveSecureMemoryCacheCallback():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Memory.PSECURE_MEMORY_CACHE_CALLBACK, use_last_error=False)(("RemoveSecureMemoryCacheCallback", windll["KERNEL32"]), ((1, 'pfnCallBack'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "FILE_CACHE_MAX_HARD_ENABLE",
    "FILE_CACHE_MAX_HARD_DISABLE",
    "FILE_CACHE_MIN_HARD_ENABLE",
    "FILE_CACHE_MIN_HARD_DISABLE",
    "MEHC_PATROL_SCRUBBER_PRESENT",
    "FILE_MAP",
    "FILE_MAP_WRITE",
    "FILE_MAP_READ",
    "FILE_MAP_ALL_ACCESS",
    "FILE_MAP_EXECUTE",
    "FILE_MAP_COPY",
    "FILE_MAP_RESERVE",
    "FILE_MAP_TARGETS_INVALID",
    "FILE_MAP_LARGE_PAGES",
    "HEAP_FLAGS",
    "HEAP_NONE",
    "HEAP_NO_SERIALIZE",
    "HEAP_GROWABLE",
    "HEAP_GENERATE_EXCEPTIONS",
    "HEAP_ZERO_MEMORY",
    "HEAP_REALLOC_IN_PLACE_ONLY",
    "HEAP_TAIL_CHECKING_ENABLED",
    "HEAP_FREE_CHECKING_ENABLED",
    "HEAP_DISABLE_COALESCE_ON_FREE",
    "HEAP_CREATE_ALIGN_16",
    "HEAP_CREATE_ENABLE_TRACING",
    "HEAP_CREATE_ENABLE_EXECUTE",
    "HEAP_MAXIMUM_TAG",
    "HEAP_PSEUDO_TAG_FLAG",
    "HEAP_TAG_SHIFT",
    "HEAP_CREATE_SEGMENT_HEAP",
    "HEAP_CREATE_HARDENED",
    "PAGE_PROTECTION_FLAGS",
    "PAGE_NOACCESS",
    "PAGE_READONLY",
    "PAGE_READWRITE",
    "PAGE_WRITECOPY",
    "PAGE_EXECUTE",
    "PAGE_EXECUTE_READ",
    "PAGE_EXECUTE_READWRITE",
    "PAGE_EXECUTE_WRITECOPY",
    "PAGE_GUARD",
    "PAGE_NOCACHE",
    "PAGE_WRITECOMBINE",
    "PAGE_GRAPHICS_NOACCESS",
    "PAGE_GRAPHICS_READONLY",
    "PAGE_GRAPHICS_READWRITE",
    "PAGE_GRAPHICS_EXECUTE",
    "PAGE_GRAPHICS_EXECUTE_READ",
    "PAGE_GRAPHICS_EXECUTE_READWRITE",
    "PAGE_GRAPHICS_COHERENT",
    "PAGE_GRAPHICS_NOCACHE",
    "PAGE_ENCLAVE_THREAD_CONTROL",
    "PAGE_REVERT_TO_FILE_MAP",
    "PAGE_TARGETS_NO_UPDATE",
    "PAGE_TARGETS_INVALID",
    "PAGE_ENCLAVE_UNVALIDATED",
    "PAGE_ENCLAVE_MASK",
    "PAGE_ENCLAVE_DECOMMIT",
    "PAGE_ENCLAVE_SS_FIRST",
    "PAGE_ENCLAVE_SS_REST",
    "SEC_PARTITION_OWNER_HANDLE",
    "SEC_64K_PAGES",
    "SEC_FILE",
    "SEC_IMAGE",
    "SEC_PROTECTED_IMAGE",
    "SEC_RESERVE",
    "SEC_COMMIT",
    "SEC_NOCACHE",
    "SEC_WRITECOMBINE",
    "SEC_LARGE_PAGES",
    "SEC_IMAGE_NO_EXECUTE",
    "UNMAP_VIEW_OF_FILE_FLAGS",
    "MEM_UNMAP_NONE",
    "MEM_UNMAP_WITH_TRANSIENT_BOOST",
    "MEM_PRESERVE_PLACEHOLDER",
    "VIRTUAL_FREE_TYPE",
    "MEM_DECOMMIT",
    "MEM_RELEASE",
    "VIRTUAL_ALLOCATION_TYPE",
    "MEM_COMMIT",
    "MEM_RESERVE",
    "MEM_RESET",
    "MEM_RESET_UNDO",
    "MEM_REPLACE_PLACEHOLDER",
    "MEM_LARGE_PAGES",
    "MEM_RESERVE_PLACEHOLDER",
    "MEM_FREE",
    "LOCAL_ALLOC_FLAGS",
    "LHND",
    "LMEM_FIXED",
    "LMEM_MOVEABLE",
    "LMEM_ZEROINIT",
    "LPTR",
    "NONZEROLHND",
    "NONZEROLPTR",
    "GLOBAL_ALLOC_FLAGS",
    "GHND",
    "GMEM_FIXED",
    "GMEM_MOVEABLE",
    "GMEM_ZEROINIT",
    "GPTR",
    "PAGE_TYPE",
    "MEM_PRIVATE",
    "MEM_MAPPED",
    "MEM_IMAGE",
    "HeapHandle",
    "PROCESS_HEAP_ENTRY",
    "HEAP_SUMMARY",
    "MEMORY_RESOURCE_NOTIFICATION_TYPE",
    "MEMORY_RESOURCE_NOTIFICATION_TYPE_LowMemoryResourceNotification",
    "MEMORY_RESOURCE_NOTIFICATION_TYPE_HighMemoryResourceNotification",
    "WIN32_MEMORY_RANGE_ENTRY",
    "PBAD_MEMORY_CALLBACK_ROUTINE",
    "OFFER_PRIORITY",
    "OFFER_PRIORITY_VmOfferPriorityVeryLow",
    "OFFER_PRIORITY_VmOfferPriorityLow",
    "OFFER_PRIORITY_VmOfferPriorityBelowNormal",
    "OFFER_PRIORITY_VmOfferPriorityNormal",
    "WIN32_MEMORY_INFORMATION_CLASS",
    "WIN32_MEMORY_INFORMATION_CLASS_MemoryRegionInfo",
    "WIN32_MEMORY_REGION_INFORMATION",
    "WIN32_MEMORY_PARTITION_INFORMATION_CLASS",
    "WIN32_MEMORY_PARTITION_INFORMATION_CLASS_MemoryPartitionInfo",
    "WIN32_MEMORY_PARTITION_INFORMATION_CLASS_MemoryPartitionDedicatedMemoryInfo",
    "WIN32_MEMORY_PARTITION_INFORMATION",
    "MEMORY_BASIC_INFORMATION",
    "MEMORY_BASIC_INFORMATION32",
    "MEMORY_BASIC_INFORMATION64",
    "CFG_CALL_TARGET_INFO",
    "MEM_EXTENDED_PARAMETER_TYPE",
    "MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterInvalidType",
    "MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterAddressRequirements",
    "MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterNumaNode",
    "MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterPartitionHandle",
    "MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterUserPhysicalHandle",
    "MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterAttributeFlags",
    "MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterImageMachine",
    "MEM_EXTENDED_PARAMETER_TYPE_MemExtendedParameterMax",
    "MEM_EXTENDED_PARAMETER",
    "HEAP_INFORMATION_CLASS",
    "HEAP_INFORMATION_CLASS_HeapCompatibilityInformation",
    "HEAP_INFORMATION_CLASS_HeapEnableTerminationOnCorruption",
    "HEAP_INFORMATION_CLASS_HeapOptimizeResources",
    "HEAP_INFORMATION_CLASS_HeapTag",
    "PSECURE_MEMORY_CACHE_CALLBACK",
    "HeapCreate",
    "HeapDestroy",
    "HeapAlloc",
    "HeapReAlloc",
    "HeapFree",
    "HeapSize",
    "GetProcessHeap",
    "HeapCompact",
    "HeapSetInformation",
    "HeapValidate",
    "HeapSummary",
    "GetProcessHeaps",
    "HeapLock",
    "HeapUnlock",
    "HeapWalk",
    "HeapQueryInformation",
    "VirtualAlloc",
    "VirtualProtect",
    "VirtualFree",
    "VirtualQuery",
    "VirtualAllocEx",
    "VirtualProtectEx",
    "VirtualQueryEx",
    "CreateFileMappingW",
    "CreateFileMapping",
    "OpenFileMappingW",
    "OpenFileMapping",
    "MapViewOfFile",
    "MapViewOfFileEx",
    "VirtualFreeEx",
    "FlushViewOfFile",
    "UnmapViewOfFile",
    "GetLargePageMinimum",
    "GetProcessWorkingSetSizeEx",
    "SetProcessWorkingSetSizeEx",
    "VirtualLock",
    "VirtualUnlock",
    "GetWriteWatch",
    "ResetWriteWatch",
    "CreateMemoryResourceNotification",
    "QueryMemoryResourceNotification",
    "GetSystemFileCacheSize",
    "SetSystemFileCacheSize",
    "CreateFileMappingNumaW",
    "CreateFileMappingNuma",
    "PrefetchVirtualMemory",
    "CreateFileMappingFromApp",
    "MapViewOfFileFromApp",
    "UnmapViewOfFileEx",
    "AllocateUserPhysicalPages",
    "FreeUserPhysicalPages",
    "MapUserPhysicalPages",
    "AllocateUserPhysicalPagesNuma",
    "VirtualAllocExNuma",
    "GetMemoryErrorHandlingCapabilities",
    "RegisterBadMemoryNotification",
    "UnregisterBadMemoryNotification",
    "OfferVirtualMemory",
    "ReclaimVirtualMemory",
    "DiscardVirtualMemory",
    "SetProcessValidCallTargets",
    "SetProcessValidCallTargetsForMappedView",
    "VirtualAllocFromApp",
    "VirtualProtectFromApp",
    "OpenFileMappingFromApp",
    "QueryVirtualMemoryInformation",
    "MapViewOfFileNuma2",
    "UnmapViewOfFile2",
    "VirtualUnlockEx",
    "VirtualAlloc2",
    "MapViewOfFile3",
    "VirtualAlloc2FromApp",
    "MapViewOfFile3FromApp",
    "CreateFileMapping2",
    "AllocateUserPhysicalPages2",
    "OpenDedicatedMemoryPartition",
    "QueryPartitionInformation",
    "RtlCompareMemory",
    "RtlCrc32",
    "RtlCrc64",
    "RtlIsZeroMemory",
    "GlobalAlloc",
    "GlobalReAlloc",
    "GlobalSize",
    "GlobalUnlock",
    "GlobalLock",
    "GlobalFlags",
    "GlobalHandle",
    "GlobalFree",
    "LocalAlloc",
    "LocalReAlloc",
    "LocalLock",
    "LocalHandle",
    "LocalUnlock",
    "LocalSize",
    "LocalFlags",
    "LocalFree",
    "CreateFileMappingA",
    "CreateFileMappingNumaA",
    "OpenFileMappingA",
    "MapViewOfFileExNuma",
    "IsBadReadPtr",
    "IsBadWritePtr",
    "IsBadCodePtr",
    "IsBadStringPtrA",
    "IsBadStringPtrW",
    "IsBadStringPtr",
    "MapUserPhysicalPagesScatter",
    "AddSecureMemoryCacheCallback",
    "RemoveSecureMemoryCacheCallback",
]
