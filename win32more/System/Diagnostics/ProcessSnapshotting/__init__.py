from win32more.base import *
import win32more.Foundation
import win32more.System.Diagnostics.Debug
import win32more.System.Diagnostics.ProcessSnapshotting
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
PSS_PERF_RESOLUTION = 1000000
HPSS = IntPtr
HPSSWALK = IntPtr
PSS_HANDLE_FLAGS = UInt32
PSS_HANDLE_NONE = 0
PSS_HANDLE_HAVE_TYPE = 1
PSS_HANDLE_HAVE_NAME = 2
PSS_HANDLE_HAVE_BASIC_INFORMATION = 4
PSS_HANDLE_HAVE_TYPE_SPECIFIC_INFORMATION = 8
PSS_OBJECT_TYPE = Int32
PSS_OBJECT_TYPE_UNKNOWN = 0
PSS_OBJECT_TYPE_PROCESS = 1
PSS_OBJECT_TYPE_THREAD = 2
PSS_OBJECT_TYPE_MUTANT = 3
PSS_OBJECT_TYPE_EVENT = 4
PSS_OBJECT_TYPE_SECTION = 5
PSS_OBJECT_TYPE_SEMAPHORE = 6
PSS_CAPTURE_FLAGS = UInt32
PSS_CAPTURE_NONE = 0
PSS_CAPTURE_VA_CLONE = 1
PSS_CAPTURE_RESERVED_00000002 = 2
PSS_CAPTURE_HANDLES = 4
PSS_CAPTURE_HANDLE_NAME_INFORMATION = 8
PSS_CAPTURE_HANDLE_BASIC_INFORMATION = 16
PSS_CAPTURE_HANDLE_TYPE_SPECIFIC_INFORMATION = 32
PSS_CAPTURE_HANDLE_TRACE = 64
PSS_CAPTURE_THREADS = 128
PSS_CAPTURE_THREAD_CONTEXT = 256
PSS_CAPTURE_THREAD_CONTEXT_EXTENDED = 512
PSS_CAPTURE_RESERVED_00000400 = 1024
PSS_CAPTURE_VA_SPACE = 2048
PSS_CAPTURE_VA_SPACE_SECTION_INFORMATION = 4096
PSS_CAPTURE_IPT_TRACE = 8192
PSS_CAPTURE_RESERVED_00004000 = 16384
PSS_CREATE_BREAKAWAY_OPTIONAL = 67108864
PSS_CREATE_BREAKAWAY = 134217728
PSS_CREATE_FORCE_BREAKAWAY = 268435456
PSS_CREATE_USE_VM_ALLOCATIONS = 536870912
PSS_CREATE_MEASURE_PERFORMANCE = 1073741824
PSS_CREATE_RELEASE_SECTION = 2147483648
PSS_QUERY_INFORMATION_CLASS = Int32
PSS_QUERY_PROCESS_INFORMATION = 0
PSS_QUERY_VA_CLONE_INFORMATION = 1
PSS_QUERY_AUXILIARY_PAGES_INFORMATION = 2
PSS_QUERY_VA_SPACE_INFORMATION = 3
PSS_QUERY_HANDLE_INFORMATION = 4
PSS_QUERY_THREAD_INFORMATION = 5
PSS_QUERY_HANDLE_TRACE_INFORMATION = 6
PSS_QUERY_PERFORMANCE_COUNTERS = 7
PSS_WALK_INFORMATION_CLASS = Int32
PSS_WALK_AUXILIARY_PAGES = 0
PSS_WALK_VA_SPACE = 1
PSS_WALK_HANDLES = 2
PSS_WALK_THREADS = 3
PSS_DUPLICATE_FLAGS = UInt32
PSS_DUPLICATE_NONE = 0
PSS_DUPLICATE_CLOSE_SOURCE = 1
PSS_PROCESS_FLAGS = UInt32
PSS_PROCESS_FLAGS_NONE = 0
PSS_PROCESS_FLAGS_PROTECTED = 1
PSS_PROCESS_FLAGS_WOW64 = 2
PSS_PROCESS_FLAGS_RESERVED_03 = 4
PSS_PROCESS_FLAGS_RESERVED_04 = 8
PSS_PROCESS_FLAGS_FROZEN = 16
def _define_PSS_PROCESS_INFORMATION_head():
    class PSS_PROCESS_INFORMATION(Structure):
        pass
    return PSS_PROCESS_INFORMATION
def _define_PSS_PROCESS_INFORMATION():
    PSS_PROCESS_INFORMATION = win32more.System.Diagnostics.ProcessSnapshotting.PSS_PROCESS_INFORMATION_head
    PSS_PROCESS_INFORMATION._fields_ = [
        ("ExitStatus", UInt32),
        ("PebBaseAddress", c_void_p),
        ("AffinityMask", UIntPtr),
        ("BasePriority", Int32),
        ("ProcessId", UInt32),
        ("ParentProcessId", UInt32),
        ("Flags", win32more.System.Diagnostics.ProcessSnapshotting.PSS_PROCESS_FLAGS),
        ("CreateTime", win32more.Foundation.FILETIME),
        ("ExitTime", win32more.Foundation.FILETIME),
        ("KernelTime", win32more.Foundation.FILETIME),
        ("UserTime", win32more.Foundation.FILETIME),
        ("PriorityClass", UInt32),
        ("PeakVirtualSize", UIntPtr),
        ("VirtualSize", UIntPtr),
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
        ("ExecuteFlags", UInt32),
        ("ImageFileName", Char * 260),
    ]
    return PSS_PROCESS_INFORMATION
def _define_PSS_VA_CLONE_INFORMATION_head():
    class PSS_VA_CLONE_INFORMATION(Structure):
        pass
    return PSS_VA_CLONE_INFORMATION
def _define_PSS_VA_CLONE_INFORMATION():
    PSS_VA_CLONE_INFORMATION = win32more.System.Diagnostics.ProcessSnapshotting.PSS_VA_CLONE_INFORMATION_head
    PSS_VA_CLONE_INFORMATION._fields_ = [
        ("VaCloneHandle", win32more.Foundation.HANDLE),
    ]
    return PSS_VA_CLONE_INFORMATION
def _define_PSS_AUXILIARY_PAGES_INFORMATION_head():
    class PSS_AUXILIARY_PAGES_INFORMATION(Structure):
        pass
    return PSS_AUXILIARY_PAGES_INFORMATION
def _define_PSS_AUXILIARY_PAGES_INFORMATION():
    PSS_AUXILIARY_PAGES_INFORMATION = win32more.System.Diagnostics.ProcessSnapshotting.PSS_AUXILIARY_PAGES_INFORMATION_head
    PSS_AUXILIARY_PAGES_INFORMATION._fields_ = [
        ("AuxPagesCaptured", UInt32),
    ]
    return PSS_AUXILIARY_PAGES_INFORMATION
def _define_PSS_VA_SPACE_INFORMATION_head():
    class PSS_VA_SPACE_INFORMATION(Structure):
        pass
    return PSS_VA_SPACE_INFORMATION
def _define_PSS_VA_SPACE_INFORMATION():
    PSS_VA_SPACE_INFORMATION = win32more.System.Diagnostics.ProcessSnapshotting.PSS_VA_SPACE_INFORMATION_head
    PSS_VA_SPACE_INFORMATION._fields_ = [
        ("RegionCount", UInt32),
    ]
    return PSS_VA_SPACE_INFORMATION
def _define_PSS_HANDLE_INFORMATION_head():
    class PSS_HANDLE_INFORMATION(Structure):
        pass
    return PSS_HANDLE_INFORMATION
def _define_PSS_HANDLE_INFORMATION():
    PSS_HANDLE_INFORMATION = win32more.System.Diagnostics.ProcessSnapshotting.PSS_HANDLE_INFORMATION_head
    PSS_HANDLE_INFORMATION._fields_ = [
        ("HandlesCaptured", UInt32),
    ]
    return PSS_HANDLE_INFORMATION
def _define_PSS_THREAD_INFORMATION_head():
    class PSS_THREAD_INFORMATION(Structure):
        pass
    return PSS_THREAD_INFORMATION
def _define_PSS_THREAD_INFORMATION():
    PSS_THREAD_INFORMATION = win32more.System.Diagnostics.ProcessSnapshotting.PSS_THREAD_INFORMATION_head
    PSS_THREAD_INFORMATION._fields_ = [
        ("ThreadsCaptured", UInt32),
        ("ContextLength", UInt32),
    ]
    return PSS_THREAD_INFORMATION
def _define_PSS_HANDLE_TRACE_INFORMATION_head():
    class PSS_HANDLE_TRACE_INFORMATION(Structure):
        pass
    return PSS_HANDLE_TRACE_INFORMATION
def _define_PSS_HANDLE_TRACE_INFORMATION():
    PSS_HANDLE_TRACE_INFORMATION = win32more.System.Diagnostics.ProcessSnapshotting.PSS_HANDLE_TRACE_INFORMATION_head
    PSS_HANDLE_TRACE_INFORMATION._fields_ = [
        ("SectionHandle", win32more.Foundation.HANDLE),
        ("Size", UInt32),
    ]
    return PSS_HANDLE_TRACE_INFORMATION
def _define_PSS_PERFORMANCE_COUNTERS_head():
    class PSS_PERFORMANCE_COUNTERS(Structure):
        pass
    return PSS_PERFORMANCE_COUNTERS
def _define_PSS_PERFORMANCE_COUNTERS():
    PSS_PERFORMANCE_COUNTERS = win32more.System.Diagnostics.ProcessSnapshotting.PSS_PERFORMANCE_COUNTERS_head
    PSS_PERFORMANCE_COUNTERS._fields_ = [
        ("TotalCycleCount", UInt64),
        ("TotalWallClockPeriod", UInt64),
        ("VaCloneCycleCount", UInt64),
        ("VaCloneWallClockPeriod", UInt64),
        ("VaSpaceCycleCount", UInt64),
        ("VaSpaceWallClockPeriod", UInt64),
        ("AuxPagesCycleCount", UInt64),
        ("AuxPagesWallClockPeriod", UInt64),
        ("HandlesCycleCount", UInt64),
        ("HandlesWallClockPeriod", UInt64),
        ("ThreadsCycleCount", UInt64),
        ("ThreadsWallClockPeriod", UInt64),
    ]
    return PSS_PERFORMANCE_COUNTERS
def _define_PSS_AUXILIARY_PAGE_ENTRY_head():
    class PSS_AUXILIARY_PAGE_ENTRY(Structure):
        pass
    return PSS_AUXILIARY_PAGE_ENTRY
def _define_PSS_AUXILIARY_PAGE_ENTRY():
    PSS_AUXILIARY_PAGE_ENTRY = win32more.System.Diagnostics.ProcessSnapshotting.PSS_AUXILIARY_PAGE_ENTRY_head
    PSS_AUXILIARY_PAGE_ENTRY._fields_ = [
        ("Address", c_void_p),
        ("BasicInformation", win32more.System.Memory.MEMORY_BASIC_INFORMATION),
        ("CaptureTime", win32more.Foundation.FILETIME),
        ("PageContents", c_void_p),
        ("PageSize", UInt32),
    ]
    return PSS_AUXILIARY_PAGE_ENTRY
def _define_PSS_VA_SPACE_ENTRY_head():
    class PSS_VA_SPACE_ENTRY(Structure):
        pass
    return PSS_VA_SPACE_ENTRY
def _define_PSS_VA_SPACE_ENTRY():
    PSS_VA_SPACE_ENTRY = win32more.System.Diagnostics.ProcessSnapshotting.PSS_VA_SPACE_ENTRY_head
    PSS_VA_SPACE_ENTRY._fields_ = [
        ("BaseAddress", c_void_p),
        ("AllocationBase", c_void_p),
        ("AllocationProtect", UInt32),
        ("RegionSize", UIntPtr),
        ("State", UInt32),
        ("Protect", UInt32),
        ("Type", UInt32),
        ("TimeDateStamp", UInt32),
        ("SizeOfImage", UInt32),
        ("ImageBase", c_void_p),
        ("CheckSum", UInt32),
        ("MappedFileNameLength", UInt16),
        ("MappedFileName", win32more.Foundation.PWSTR),
    ]
    return PSS_VA_SPACE_ENTRY
def _define_PSS_HANDLE_ENTRY_head():
    class PSS_HANDLE_ENTRY(Structure):
        pass
    return PSS_HANDLE_ENTRY
def _define_PSS_HANDLE_ENTRY():
    PSS_HANDLE_ENTRY = win32more.System.Diagnostics.ProcessSnapshotting.PSS_HANDLE_ENTRY_head
    class PSS_HANDLE_ENTRY__TypeSpecificInformation_e__Union(Union):
        pass
    class PSS_HANDLE_ENTRY__TypeSpecificInformation_e__Union__Semaphore_e__Struct(Structure):
        pass
    PSS_HANDLE_ENTRY__TypeSpecificInformation_e__Union__Semaphore_e__Struct._fields_ = [
        ("CurrentCount", Int32),
        ("MaximumCount", Int32),
    ]
    class PSS_HANDLE_ENTRY__TypeSpecificInformation_e__Union__Event_e__Struct(Structure):
        pass
    PSS_HANDLE_ENTRY__TypeSpecificInformation_e__Union__Event_e__Struct._fields_ = [
        ("ManualReset", win32more.Foundation.BOOL),
        ("Signaled", win32more.Foundation.BOOL),
    ]
    class PSS_HANDLE_ENTRY__TypeSpecificInformation_e__Union__Thread_e__Struct(Structure):
        pass
    PSS_HANDLE_ENTRY__TypeSpecificInformation_e__Union__Thread_e__Struct._fields_ = [
        ("ExitStatus", UInt32),
        ("TebBaseAddress", c_void_p),
        ("ProcessId", UInt32),
        ("ThreadId", UInt32),
        ("AffinityMask", UIntPtr),
        ("Priority", Int32),
        ("BasePriority", Int32),
        ("Win32StartAddress", c_void_p),
    ]
    class PSS_HANDLE_ENTRY__TypeSpecificInformation_e__Union__Section_e__Struct(Structure):
        pass
    PSS_HANDLE_ENTRY__TypeSpecificInformation_e__Union__Section_e__Struct._fields_ = [
        ("BaseAddress", c_void_p),
        ("AllocationAttributes", UInt32),
        ("MaximumSize", win32more.Foundation.LARGE_INTEGER),
    ]
    class PSS_HANDLE_ENTRY__TypeSpecificInformation_e__Union__Process_e__Struct(Structure):
        pass
    PSS_HANDLE_ENTRY__TypeSpecificInformation_e__Union__Process_e__Struct._fields_ = [
        ("ExitStatus", UInt32),
        ("PebBaseAddress", c_void_p),
        ("AffinityMask", UIntPtr),
        ("BasePriority", Int32),
        ("ProcessId", UInt32),
        ("ParentProcessId", UInt32),
        ("Flags", UInt32),
    ]
    class PSS_HANDLE_ENTRY__TypeSpecificInformation_e__Union__Mutant_e__Struct(Structure):
        pass
    PSS_HANDLE_ENTRY__TypeSpecificInformation_e__Union__Mutant_e__Struct._fields_ = [
        ("CurrentCount", Int32),
        ("Abandoned", win32more.Foundation.BOOL),
        ("OwnerProcessId", UInt32),
        ("OwnerThreadId", UInt32),
    ]
    PSS_HANDLE_ENTRY__TypeSpecificInformation_e__Union._fields_ = [
        ("Process", PSS_HANDLE_ENTRY__TypeSpecificInformation_e__Union__Process_e__Struct),
        ("Thread", PSS_HANDLE_ENTRY__TypeSpecificInformation_e__Union__Thread_e__Struct),
        ("Mutant", PSS_HANDLE_ENTRY__TypeSpecificInformation_e__Union__Mutant_e__Struct),
        ("Event", PSS_HANDLE_ENTRY__TypeSpecificInformation_e__Union__Event_e__Struct),
        ("Section", PSS_HANDLE_ENTRY__TypeSpecificInformation_e__Union__Section_e__Struct),
        ("Semaphore", PSS_HANDLE_ENTRY__TypeSpecificInformation_e__Union__Semaphore_e__Struct),
    ]
    PSS_HANDLE_ENTRY._fields_ = [
        ("Handle", win32more.Foundation.HANDLE),
        ("Flags", win32more.System.Diagnostics.ProcessSnapshotting.PSS_HANDLE_FLAGS),
        ("ObjectType", win32more.System.Diagnostics.ProcessSnapshotting.PSS_OBJECT_TYPE),
        ("CaptureTime", win32more.Foundation.FILETIME),
        ("Attributes", UInt32),
        ("GrantedAccess", UInt32),
        ("HandleCount", UInt32),
        ("PointerCount", UInt32),
        ("PagedPoolCharge", UInt32),
        ("NonPagedPoolCharge", UInt32),
        ("CreationTime", win32more.Foundation.FILETIME),
        ("TypeNameLength", UInt16),
        ("TypeName", win32more.Foundation.PWSTR),
        ("ObjectNameLength", UInt16),
        ("ObjectName", win32more.Foundation.PWSTR),
        ("TypeSpecificInformation", PSS_HANDLE_ENTRY__TypeSpecificInformation_e__Union),
    ]
    return PSS_HANDLE_ENTRY
PSS_THREAD_FLAGS = UInt32
PSS_THREAD_FLAGS_NONE = 0
PSS_THREAD_FLAGS_TERMINATED = 1
def _define_PSS_THREAD_ENTRY_head():
    class PSS_THREAD_ENTRY(Structure):
        pass
    return PSS_THREAD_ENTRY
def _define_PSS_THREAD_ENTRY():
    PSS_THREAD_ENTRY = win32more.System.Diagnostics.ProcessSnapshotting.PSS_THREAD_ENTRY_head
    PSS_THREAD_ENTRY._fields_ = [
        ("ExitStatus", UInt32),
        ("TebBaseAddress", c_void_p),
        ("ProcessId", UInt32),
        ("ThreadId", UInt32),
        ("AffinityMask", UIntPtr),
        ("Priority", Int32),
        ("BasePriority", Int32),
        ("LastSyscallFirstArgument", c_void_p),
        ("LastSyscallNumber", UInt16),
        ("CreateTime", win32more.Foundation.FILETIME),
        ("ExitTime", win32more.Foundation.FILETIME),
        ("KernelTime", win32more.Foundation.FILETIME),
        ("UserTime", win32more.Foundation.FILETIME),
        ("Win32StartAddress", c_void_p),
        ("CaptureTime", win32more.Foundation.FILETIME),
        ("Flags", win32more.System.Diagnostics.ProcessSnapshotting.PSS_THREAD_FLAGS),
        ("SuspendCount", UInt16),
        ("SizeOfContextRecord", UInt16),
        ("ContextRecord", POINTER(win32more.System.Diagnostics.Debug.CONTEXT_head)),
    ]
    return PSS_THREAD_ENTRY
def _define_PSS_ALLOCATOR_head():
    class PSS_ALLOCATOR(Structure):
        pass
    return PSS_ALLOCATOR
def _define_PSS_ALLOCATOR():
    PSS_ALLOCATOR = win32more.System.Diagnostics.ProcessSnapshotting.PSS_ALLOCATOR_head
    PSS_ALLOCATOR._fields_ = [
        ("Context", c_void_p),
        ("AllocRoutine", IntPtr),
        ("FreeRoutine", IntPtr),
    ]
    return PSS_ALLOCATOR
def _define_PssCaptureSnapshot():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.System.Diagnostics.ProcessSnapshotting.PSS_CAPTURE_FLAGS,UInt32,POINTER(win32more.System.Diagnostics.ProcessSnapshotting.HPSS), use_last_error=False)(("PssCaptureSnapshot", windll["KERNEL32"]), ((1, 'ProcessHandle'),(1, 'CaptureFlags'),(1, 'ThreadContextFlags'),(1, 'SnapshotHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PssFreeSnapshot():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.System.Diagnostics.ProcessSnapshotting.HPSS, use_last_error=False)(("PssFreeSnapshot", windll["KERNEL32"]), ((1, 'ProcessHandle'),(1, 'SnapshotHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PssQuerySnapshot():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Diagnostics.ProcessSnapshotting.HPSS,win32more.System.Diagnostics.ProcessSnapshotting.PSS_QUERY_INFORMATION_CLASS,c_void_p,UInt32, use_last_error=False)(("PssQuerySnapshot", windll["KERNEL32"]), ((1, 'SnapshotHandle'),(1, 'InformationClass'),(1, 'Buffer'),(1, 'BufferLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PssWalkSnapshot():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Diagnostics.ProcessSnapshotting.HPSS,win32more.System.Diagnostics.ProcessSnapshotting.PSS_WALK_INFORMATION_CLASS,win32more.System.Diagnostics.ProcessSnapshotting.HPSSWALK,POINTER(Void),UInt32, use_last_error=False)(("PssWalkSnapshot", windll["KERNEL32"]), ((1, 'SnapshotHandle'),(1, 'InformationClass'),(1, 'WalkMarkerHandle'),(1, 'Buffer'),(1, 'BufferLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PssDuplicateSnapshot():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.System.Diagnostics.ProcessSnapshotting.HPSS,win32more.Foundation.HANDLE,POINTER(win32more.System.Diagnostics.ProcessSnapshotting.HPSS),win32more.System.Diagnostics.ProcessSnapshotting.PSS_DUPLICATE_FLAGS, use_last_error=False)(("PssDuplicateSnapshot", windll["KERNEL32"]), ((1, 'SourceProcessHandle'),(1, 'SnapshotHandle'),(1, 'TargetProcessHandle'),(1, 'TargetSnapshotHandle'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PssWalkMarkerCreate():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Diagnostics.ProcessSnapshotting.PSS_ALLOCATOR_head),POINTER(win32more.System.Diagnostics.ProcessSnapshotting.HPSSWALK), use_last_error=False)(("PssWalkMarkerCreate", windll["KERNEL32"]), ((1, 'Allocator'),(1, 'WalkMarkerHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PssWalkMarkerFree():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Diagnostics.ProcessSnapshotting.HPSSWALK, use_last_error=False)(("PssWalkMarkerFree", windll["KERNEL32"]), ((1, 'WalkMarkerHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PssWalkMarkerGetPosition():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Diagnostics.ProcessSnapshotting.HPSSWALK,POINTER(UIntPtr), use_last_error=False)(("PssWalkMarkerGetPosition", windll["KERNEL32"]), ((1, 'WalkMarkerHandle'),(1, 'Position'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PssWalkMarkerSetPosition():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Diagnostics.ProcessSnapshotting.HPSSWALK,UIntPtr, use_last_error=False)(("PssWalkMarkerSetPosition", windll["KERNEL32"]), ((1, 'WalkMarkerHandle'),(1, 'Position'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PssWalkMarkerSeekToBeginning():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Diagnostics.ProcessSnapshotting.HPSSWALK, use_last_error=False)(("PssWalkMarkerSeekToBeginning", windll["KERNEL32"]), ((1, 'WalkMarkerHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "PSS_PERF_RESOLUTION",
    "HPSS",
    "HPSSWALK",
    "PSS_HANDLE_FLAGS",
    "PSS_HANDLE_NONE",
    "PSS_HANDLE_HAVE_TYPE",
    "PSS_HANDLE_HAVE_NAME",
    "PSS_HANDLE_HAVE_BASIC_INFORMATION",
    "PSS_HANDLE_HAVE_TYPE_SPECIFIC_INFORMATION",
    "PSS_OBJECT_TYPE",
    "PSS_OBJECT_TYPE_UNKNOWN",
    "PSS_OBJECT_TYPE_PROCESS",
    "PSS_OBJECT_TYPE_THREAD",
    "PSS_OBJECT_TYPE_MUTANT",
    "PSS_OBJECT_TYPE_EVENT",
    "PSS_OBJECT_TYPE_SECTION",
    "PSS_OBJECT_TYPE_SEMAPHORE",
    "PSS_CAPTURE_FLAGS",
    "PSS_CAPTURE_NONE",
    "PSS_CAPTURE_VA_CLONE",
    "PSS_CAPTURE_RESERVED_00000002",
    "PSS_CAPTURE_HANDLES",
    "PSS_CAPTURE_HANDLE_NAME_INFORMATION",
    "PSS_CAPTURE_HANDLE_BASIC_INFORMATION",
    "PSS_CAPTURE_HANDLE_TYPE_SPECIFIC_INFORMATION",
    "PSS_CAPTURE_HANDLE_TRACE",
    "PSS_CAPTURE_THREADS",
    "PSS_CAPTURE_THREAD_CONTEXT",
    "PSS_CAPTURE_THREAD_CONTEXT_EXTENDED",
    "PSS_CAPTURE_RESERVED_00000400",
    "PSS_CAPTURE_VA_SPACE",
    "PSS_CAPTURE_VA_SPACE_SECTION_INFORMATION",
    "PSS_CAPTURE_IPT_TRACE",
    "PSS_CAPTURE_RESERVED_00004000",
    "PSS_CREATE_BREAKAWAY_OPTIONAL",
    "PSS_CREATE_BREAKAWAY",
    "PSS_CREATE_FORCE_BREAKAWAY",
    "PSS_CREATE_USE_VM_ALLOCATIONS",
    "PSS_CREATE_MEASURE_PERFORMANCE",
    "PSS_CREATE_RELEASE_SECTION",
    "PSS_QUERY_INFORMATION_CLASS",
    "PSS_QUERY_PROCESS_INFORMATION",
    "PSS_QUERY_VA_CLONE_INFORMATION",
    "PSS_QUERY_AUXILIARY_PAGES_INFORMATION",
    "PSS_QUERY_VA_SPACE_INFORMATION",
    "PSS_QUERY_HANDLE_INFORMATION",
    "PSS_QUERY_THREAD_INFORMATION",
    "PSS_QUERY_HANDLE_TRACE_INFORMATION",
    "PSS_QUERY_PERFORMANCE_COUNTERS",
    "PSS_WALK_INFORMATION_CLASS",
    "PSS_WALK_AUXILIARY_PAGES",
    "PSS_WALK_VA_SPACE",
    "PSS_WALK_HANDLES",
    "PSS_WALK_THREADS",
    "PSS_DUPLICATE_FLAGS",
    "PSS_DUPLICATE_NONE",
    "PSS_DUPLICATE_CLOSE_SOURCE",
    "PSS_PROCESS_FLAGS",
    "PSS_PROCESS_FLAGS_NONE",
    "PSS_PROCESS_FLAGS_PROTECTED",
    "PSS_PROCESS_FLAGS_WOW64",
    "PSS_PROCESS_FLAGS_RESERVED_03",
    "PSS_PROCESS_FLAGS_RESERVED_04",
    "PSS_PROCESS_FLAGS_FROZEN",
    "PSS_PROCESS_INFORMATION",
    "PSS_VA_CLONE_INFORMATION",
    "PSS_AUXILIARY_PAGES_INFORMATION",
    "PSS_VA_SPACE_INFORMATION",
    "PSS_HANDLE_INFORMATION",
    "PSS_THREAD_INFORMATION",
    "PSS_HANDLE_TRACE_INFORMATION",
    "PSS_PERFORMANCE_COUNTERS",
    "PSS_AUXILIARY_PAGE_ENTRY",
    "PSS_VA_SPACE_ENTRY",
    "PSS_HANDLE_ENTRY",
    "PSS_THREAD_FLAGS",
    "PSS_THREAD_FLAGS_NONE",
    "PSS_THREAD_FLAGS_TERMINATED",
    "PSS_THREAD_ENTRY",
    "PSS_ALLOCATOR",
    "PssCaptureSnapshot",
    "PssFreeSnapshot",
    "PssQuerySnapshot",
    "PssWalkSnapshot",
    "PssDuplicateSnapshot",
    "PssWalkMarkerCreate",
    "PssWalkMarkerFree",
    "PssWalkMarkerGetPosition",
    "PssWalkMarkerSetPosition",
    "PssWalkMarkerSeekToBeginning",
]
