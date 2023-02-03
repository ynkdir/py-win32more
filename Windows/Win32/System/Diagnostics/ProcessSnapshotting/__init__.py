from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.System.Diagnostics.Debug
import Windows.Win32.System.Diagnostics.ProcessSnapshotting
import Windows.Win32.System.Memory
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
PSS_PERF_RESOLUTION: UInt32 = 1000000
@winfunctype('KERNEL32.dll')
def PssCaptureSnapshot(ProcessHandle: Windows.Win32.Foundation.HANDLE, CaptureFlags: Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_CAPTURE_FLAGS, ThreadContextFlags: UInt32, SnapshotHandle: POINTER(Windows.Win32.System.Diagnostics.ProcessSnapshotting.HPSS)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def PssFreeSnapshot(ProcessHandle: Windows.Win32.Foundation.HANDLE, SnapshotHandle: Windows.Win32.System.Diagnostics.ProcessSnapshotting.HPSS) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def PssQuerySnapshot(SnapshotHandle: Windows.Win32.System.Diagnostics.ProcessSnapshotting.HPSS, InformationClass: Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_QUERY_INFORMATION_CLASS, Buffer: c_void_p, BufferLength: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def PssWalkSnapshot(SnapshotHandle: Windows.Win32.System.Diagnostics.ProcessSnapshotting.HPSS, InformationClass: Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_WALK_INFORMATION_CLASS, WalkMarkerHandle: Windows.Win32.System.Diagnostics.ProcessSnapshotting.HPSSWALK, Buffer: c_void_p, BufferLength: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def PssDuplicateSnapshot(SourceProcessHandle: Windows.Win32.Foundation.HANDLE, SnapshotHandle: Windows.Win32.System.Diagnostics.ProcessSnapshotting.HPSS, TargetProcessHandle: Windows.Win32.Foundation.HANDLE, TargetSnapshotHandle: POINTER(Windows.Win32.System.Diagnostics.ProcessSnapshotting.HPSS), Flags: Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_DUPLICATE_FLAGS) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def PssWalkMarkerCreate(Allocator: POINTER(Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_ALLOCATOR_head), WalkMarkerHandle: POINTER(Windows.Win32.System.Diagnostics.ProcessSnapshotting.HPSSWALK)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def PssWalkMarkerFree(WalkMarkerHandle: Windows.Win32.System.Diagnostics.ProcessSnapshotting.HPSSWALK) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def PssWalkMarkerGetPosition(WalkMarkerHandle: Windows.Win32.System.Diagnostics.ProcessSnapshotting.HPSSWALK, Position: POINTER(UIntPtr)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def PssWalkMarkerSetPosition(WalkMarkerHandle: Windows.Win32.System.Diagnostics.ProcessSnapshotting.HPSSWALK, Position: UIntPtr) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def PssWalkMarkerSeekToBeginning(WalkMarkerHandle: Windows.Win32.System.Diagnostics.ProcessSnapshotting.HPSSWALK) -> UInt32: ...
HPSS = IntPtr
HPSSWALK = IntPtr
class PSS_ALLOCATOR(Structure):
    Context: c_void_p
    AllocRoutine: IntPtr
    FreeRoutine: IntPtr
class PSS_AUXILIARY_PAGES_INFORMATION(Structure):
    AuxPagesCaptured: UInt32
class PSS_AUXILIARY_PAGE_ENTRY(Structure):
    Address: c_void_p
    BasicInformation: Windows.Win32.System.Memory.MEMORY_BASIC_INFORMATION
    CaptureTime: Windows.Win32.Foundation.FILETIME
    PageContents: c_void_p
    PageSize: UInt32
PSS_CAPTURE_FLAGS = UInt32
PSS_CAPTURE_NONE: PSS_CAPTURE_FLAGS = 0
PSS_CAPTURE_VA_CLONE: PSS_CAPTURE_FLAGS = 1
PSS_CAPTURE_RESERVED_00000002: PSS_CAPTURE_FLAGS = 2
PSS_CAPTURE_HANDLES: PSS_CAPTURE_FLAGS = 4
PSS_CAPTURE_HANDLE_NAME_INFORMATION: PSS_CAPTURE_FLAGS = 8
PSS_CAPTURE_HANDLE_BASIC_INFORMATION: PSS_CAPTURE_FLAGS = 16
PSS_CAPTURE_HANDLE_TYPE_SPECIFIC_INFORMATION: PSS_CAPTURE_FLAGS = 32
PSS_CAPTURE_HANDLE_TRACE: PSS_CAPTURE_FLAGS = 64
PSS_CAPTURE_THREADS: PSS_CAPTURE_FLAGS = 128
PSS_CAPTURE_THREAD_CONTEXT: PSS_CAPTURE_FLAGS = 256
PSS_CAPTURE_THREAD_CONTEXT_EXTENDED: PSS_CAPTURE_FLAGS = 512
PSS_CAPTURE_RESERVED_00000400: PSS_CAPTURE_FLAGS = 1024
PSS_CAPTURE_VA_SPACE: PSS_CAPTURE_FLAGS = 2048
PSS_CAPTURE_VA_SPACE_SECTION_INFORMATION: PSS_CAPTURE_FLAGS = 4096
PSS_CAPTURE_IPT_TRACE: PSS_CAPTURE_FLAGS = 8192
PSS_CAPTURE_RESERVED_00004000: PSS_CAPTURE_FLAGS = 16384
PSS_CREATE_BREAKAWAY_OPTIONAL: PSS_CAPTURE_FLAGS = 67108864
PSS_CREATE_BREAKAWAY: PSS_CAPTURE_FLAGS = 134217728
PSS_CREATE_FORCE_BREAKAWAY: PSS_CAPTURE_FLAGS = 268435456
PSS_CREATE_USE_VM_ALLOCATIONS: PSS_CAPTURE_FLAGS = 536870912
PSS_CREATE_MEASURE_PERFORMANCE: PSS_CAPTURE_FLAGS = 1073741824
PSS_CREATE_RELEASE_SECTION: PSS_CAPTURE_FLAGS = 2147483648
PSS_DUPLICATE_FLAGS = UInt32
PSS_DUPLICATE_NONE: PSS_DUPLICATE_FLAGS = 0
PSS_DUPLICATE_CLOSE_SOURCE: PSS_DUPLICATE_FLAGS = 1
class PSS_HANDLE_ENTRY(Structure):
    Handle: Windows.Win32.Foundation.HANDLE
    Flags: Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_HANDLE_FLAGS
    ObjectType: Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_OBJECT_TYPE
    CaptureTime: Windows.Win32.Foundation.FILETIME
    Attributes: UInt32
    GrantedAccess: UInt32
    HandleCount: UInt32
    PointerCount: UInt32
    PagedPoolCharge: UInt32
    NonPagedPoolCharge: UInt32
    CreationTime: Windows.Win32.Foundation.FILETIME
    TypeNameLength: UInt16
    TypeName: Windows.Win32.Foundation.PWSTR
    ObjectNameLength: UInt16
    ObjectName: Windows.Win32.Foundation.PWSTR
    TypeSpecificInformation: _TypeSpecificInformation_e__Union
    class _TypeSpecificInformation_e__Union(Union):
        Process: _Process_e__Struct
        Thread: _Thread_e__Struct
        Mutant: _Mutant_e__Struct
        Event: _Event_e__Struct
        Section: _Section_e__Struct
        Semaphore: _Semaphore_e__Struct
        class _Process_e__Struct(Structure):
            ExitStatus: UInt32
            PebBaseAddress: c_void_p
            AffinityMask: UIntPtr
            BasePriority: Int32
            ProcessId: UInt32
            ParentProcessId: UInt32
            Flags: UInt32
        class _Thread_e__Struct(Structure):
            ExitStatus: UInt32
            TebBaseAddress: c_void_p
            ProcessId: UInt32
            ThreadId: UInt32
            AffinityMask: UIntPtr
            Priority: Int32
            BasePriority: Int32
            Win32StartAddress: c_void_p
        class _Mutant_e__Struct(Structure):
            CurrentCount: Int32
            Abandoned: Windows.Win32.Foundation.BOOL
            OwnerProcessId: UInt32
            OwnerThreadId: UInt32
        class _Event_e__Struct(Structure):
            ManualReset: Windows.Win32.Foundation.BOOL
            Signaled: Windows.Win32.Foundation.BOOL
        class _Section_e__Struct(Structure):
            BaseAddress: c_void_p
            AllocationAttributes: UInt32
            MaximumSize: Windows.Win32.Foundation.LARGE_INTEGER
        class _Semaphore_e__Struct(Structure):
            CurrentCount: Int32
            MaximumCount: Int32
PSS_HANDLE_FLAGS = UInt32
PSS_HANDLE_NONE: PSS_HANDLE_FLAGS = 0
PSS_HANDLE_HAVE_TYPE: PSS_HANDLE_FLAGS = 1
PSS_HANDLE_HAVE_NAME: PSS_HANDLE_FLAGS = 2
PSS_HANDLE_HAVE_BASIC_INFORMATION: PSS_HANDLE_FLAGS = 4
PSS_HANDLE_HAVE_TYPE_SPECIFIC_INFORMATION: PSS_HANDLE_FLAGS = 8
class PSS_HANDLE_INFORMATION(Structure):
    HandlesCaptured: UInt32
class PSS_HANDLE_TRACE_INFORMATION(Structure):
    SectionHandle: Windows.Win32.Foundation.HANDLE
    Size: UInt32
PSS_OBJECT_TYPE = Int32
PSS_OBJECT_TYPE_UNKNOWN: PSS_OBJECT_TYPE = 0
PSS_OBJECT_TYPE_PROCESS: PSS_OBJECT_TYPE = 1
PSS_OBJECT_TYPE_THREAD: PSS_OBJECT_TYPE = 2
PSS_OBJECT_TYPE_MUTANT: PSS_OBJECT_TYPE = 3
PSS_OBJECT_TYPE_EVENT: PSS_OBJECT_TYPE = 4
PSS_OBJECT_TYPE_SECTION: PSS_OBJECT_TYPE = 5
PSS_OBJECT_TYPE_SEMAPHORE: PSS_OBJECT_TYPE = 6
class PSS_PERFORMANCE_COUNTERS(Structure):
    TotalCycleCount: UInt64
    TotalWallClockPeriod: UInt64
    VaCloneCycleCount: UInt64
    VaCloneWallClockPeriod: UInt64
    VaSpaceCycleCount: UInt64
    VaSpaceWallClockPeriod: UInt64
    AuxPagesCycleCount: UInt64
    AuxPagesWallClockPeriod: UInt64
    HandlesCycleCount: UInt64
    HandlesWallClockPeriod: UInt64
    ThreadsCycleCount: UInt64
    ThreadsWallClockPeriod: UInt64
PSS_PROCESS_FLAGS = UInt32
PSS_PROCESS_FLAGS_NONE: PSS_PROCESS_FLAGS = 0
PSS_PROCESS_FLAGS_PROTECTED: PSS_PROCESS_FLAGS = 1
PSS_PROCESS_FLAGS_WOW64: PSS_PROCESS_FLAGS = 2
PSS_PROCESS_FLAGS_RESERVED_03: PSS_PROCESS_FLAGS = 4
PSS_PROCESS_FLAGS_RESERVED_04: PSS_PROCESS_FLAGS = 8
PSS_PROCESS_FLAGS_FROZEN: PSS_PROCESS_FLAGS = 16
class PSS_PROCESS_INFORMATION(Structure):
    ExitStatus: UInt32
    PebBaseAddress: c_void_p
    AffinityMask: UIntPtr
    BasePriority: Int32
    ProcessId: UInt32
    ParentProcessId: UInt32
    Flags: Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_PROCESS_FLAGS
    CreateTime: Windows.Win32.Foundation.FILETIME
    ExitTime: Windows.Win32.Foundation.FILETIME
    KernelTime: Windows.Win32.Foundation.FILETIME
    UserTime: Windows.Win32.Foundation.FILETIME
    PriorityClass: UInt32
    PeakVirtualSize: UIntPtr
    VirtualSize: UIntPtr
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
    ExecuteFlags: UInt32
    ImageFileName: Char * 260
PSS_QUERY_INFORMATION_CLASS = Int32
PSS_QUERY_PROCESS_INFORMATION: PSS_QUERY_INFORMATION_CLASS = 0
PSS_QUERY_VA_CLONE_INFORMATION: PSS_QUERY_INFORMATION_CLASS = 1
PSS_QUERY_AUXILIARY_PAGES_INFORMATION: PSS_QUERY_INFORMATION_CLASS = 2
PSS_QUERY_VA_SPACE_INFORMATION: PSS_QUERY_INFORMATION_CLASS = 3
PSS_QUERY_HANDLE_INFORMATION: PSS_QUERY_INFORMATION_CLASS = 4
PSS_QUERY_THREAD_INFORMATION: PSS_QUERY_INFORMATION_CLASS = 5
PSS_QUERY_HANDLE_TRACE_INFORMATION: PSS_QUERY_INFORMATION_CLASS = 6
PSS_QUERY_PERFORMANCE_COUNTERS: PSS_QUERY_INFORMATION_CLASS = 7
class PSS_THREAD_ENTRY(Structure):
    ExitStatus: UInt32
    TebBaseAddress: c_void_p
    ProcessId: UInt32
    ThreadId: UInt32
    AffinityMask: UIntPtr
    Priority: Int32
    BasePriority: Int32
    LastSyscallFirstArgument: c_void_p
    LastSyscallNumber: UInt16
    CreateTime: Windows.Win32.Foundation.FILETIME
    ExitTime: Windows.Win32.Foundation.FILETIME
    KernelTime: Windows.Win32.Foundation.FILETIME
    UserTime: Windows.Win32.Foundation.FILETIME
    Win32StartAddress: c_void_p
    CaptureTime: Windows.Win32.Foundation.FILETIME
    Flags: Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_THREAD_FLAGS
    SuspendCount: UInt16
    SizeOfContextRecord: UInt16
    ContextRecord: POINTER(Windows.Win32.System.Diagnostics.Debug.CONTEXT_head)
PSS_THREAD_FLAGS = UInt32
PSS_THREAD_FLAGS_NONE: PSS_THREAD_FLAGS = 0
PSS_THREAD_FLAGS_TERMINATED: PSS_THREAD_FLAGS = 1
class PSS_THREAD_INFORMATION(Structure):
    ThreadsCaptured: UInt32
    ContextLength: UInt32
class PSS_VA_CLONE_INFORMATION(Structure):
    VaCloneHandle: Windows.Win32.Foundation.HANDLE
class PSS_VA_SPACE_ENTRY(Structure):
    BaseAddress: c_void_p
    AllocationBase: c_void_p
    AllocationProtect: UInt32
    RegionSize: UIntPtr
    State: UInt32
    Protect: UInt32
    Type: UInt32
    TimeDateStamp: UInt32
    SizeOfImage: UInt32
    ImageBase: c_void_p
    CheckSum: UInt32
    MappedFileNameLength: UInt16
    MappedFileName: Windows.Win32.Foundation.PWSTR
class PSS_VA_SPACE_INFORMATION(Structure):
    RegionCount: UInt32
PSS_WALK_INFORMATION_CLASS = Int32
PSS_WALK_AUXILIARY_PAGES: PSS_WALK_INFORMATION_CLASS = 0
PSS_WALK_VA_SPACE: PSS_WALK_INFORMATION_CLASS = 1
PSS_WALK_HANDLES: PSS_WALK_INFORMATION_CLASS = 2
PSS_WALK_THREADS: PSS_WALK_INFORMATION_CLASS = 3
make_head(_module, 'PSS_ALLOCATOR')
make_head(_module, 'PSS_AUXILIARY_PAGES_INFORMATION')
make_head(_module, 'PSS_AUXILIARY_PAGE_ENTRY')
make_head(_module, 'PSS_HANDLE_ENTRY')
make_head(_module, 'PSS_HANDLE_INFORMATION')
make_head(_module, 'PSS_HANDLE_TRACE_INFORMATION')
make_head(_module, 'PSS_PERFORMANCE_COUNTERS')
make_head(_module, 'PSS_PROCESS_INFORMATION')
make_head(_module, 'PSS_THREAD_ENTRY')
make_head(_module, 'PSS_THREAD_INFORMATION')
make_head(_module, 'PSS_VA_CLONE_INFORMATION')
make_head(_module, 'PSS_VA_SPACE_ENTRY')
make_head(_module, 'PSS_VA_SPACE_INFORMATION')
__all__ = [
    "HPSS",
    "HPSSWALK",
    "PSS_ALLOCATOR",
    "PSS_AUXILIARY_PAGES_INFORMATION",
    "PSS_AUXILIARY_PAGE_ENTRY",
    "PSS_CAPTURE_FLAGS",
    "PSS_CAPTURE_HANDLES",
    "PSS_CAPTURE_HANDLE_BASIC_INFORMATION",
    "PSS_CAPTURE_HANDLE_NAME_INFORMATION",
    "PSS_CAPTURE_HANDLE_TRACE",
    "PSS_CAPTURE_HANDLE_TYPE_SPECIFIC_INFORMATION",
    "PSS_CAPTURE_IPT_TRACE",
    "PSS_CAPTURE_NONE",
    "PSS_CAPTURE_RESERVED_00000002",
    "PSS_CAPTURE_RESERVED_00000400",
    "PSS_CAPTURE_RESERVED_00004000",
    "PSS_CAPTURE_THREADS",
    "PSS_CAPTURE_THREAD_CONTEXT",
    "PSS_CAPTURE_THREAD_CONTEXT_EXTENDED",
    "PSS_CAPTURE_VA_CLONE",
    "PSS_CAPTURE_VA_SPACE",
    "PSS_CAPTURE_VA_SPACE_SECTION_INFORMATION",
    "PSS_CREATE_BREAKAWAY",
    "PSS_CREATE_BREAKAWAY_OPTIONAL",
    "PSS_CREATE_FORCE_BREAKAWAY",
    "PSS_CREATE_MEASURE_PERFORMANCE",
    "PSS_CREATE_RELEASE_SECTION",
    "PSS_CREATE_USE_VM_ALLOCATIONS",
    "PSS_DUPLICATE_CLOSE_SOURCE",
    "PSS_DUPLICATE_FLAGS",
    "PSS_DUPLICATE_NONE",
    "PSS_HANDLE_ENTRY",
    "PSS_HANDLE_FLAGS",
    "PSS_HANDLE_HAVE_BASIC_INFORMATION",
    "PSS_HANDLE_HAVE_NAME",
    "PSS_HANDLE_HAVE_TYPE",
    "PSS_HANDLE_HAVE_TYPE_SPECIFIC_INFORMATION",
    "PSS_HANDLE_INFORMATION",
    "PSS_HANDLE_NONE",
    "PSS_HANDLE_TRACE_INFORMATION",
    "PSS_OBJECT_TYPE",
    "PSS_OBJECT_TYPE_EVENT",
    "PSS_OBJECT_TYPE_MUTANT",
    "PSS_OBJECT_TYPE_PROCESS",
    "PSS_OBJECT_TYPE_SECTION",
    "PSS_OBJECT_TYPE_SEMAPHORE",
    "PSS_OBJECT_TYPE_THREAD",
    "PSS_OBJECT_TYPE_UNKNOWN",
    "PSS_PERFORMANCE_COUNTERS",
    "PSS_PERF_RESOLUTION",
    "PSS_PROCESS_FLAGS",
    "PSS_PROCESS_FLAGS_FROZEN",
    "PSS_PROCESS_FLAGS_NONE",
    "PSS_PROCESS_FLAGS_PROTECTED",
    "PSS_PROCESS_FLAGS_RESERVED_03",
    "PSS_PROCESS_FLAGS_RESERVED_04",
    "PSS_PROCESS_FLAGS_WOW64",
    "PSS_PROCESS_INFORMATION",
    "PSS_QUERY_AUXILIARY_PAGES_INFORMATION",
    "PSS_QUERY_HANDLE_INFORMATION",
    "PSS_QUERY_HANDLE_TRACE_INFORMATION",
    "PSS_QUERY_INFORMATION_CLASS",
    "PSS_QUERY_PERFORMANCE_COUNTERS",
    "PSS_QUERY_PROCESS_INFORMATION",
    "PSS_QUERY_THREAD_INFORMATION",
    "PSS_QUERY_VA_CLONE_INFORMATION",
    "PSS_QUERY_VA_SPACE_INFORMATION",
    "PSS_THREAD_ENTRY",
    "PSS_THREAD_FLAGS",
    "PSS_THREAD_FLAGS_NONE",
    "PSS_THREAD_FLAGS_TERMINATED",
    "PSS_THREAD_INFORMATION",
    "PSS_VA_CLONE_INFORMATION",
    "PSS_VA_SPACE_ENTRY",
    "PSS_VA_SPACE_INFORMATION",
    "PSS_WALK_AUXILIARY_PAGES",
    "PSS_WALK_HANDLES",
    "PSS_WALK_INFORMATION_CLASS",
    "PSS_WALK_THREADS",
    "PSS_WALK_VA_SPACE",
    "PssCaptureSnapshot",
    "PssDuplicateSnapshot",
    "PssFreeSnapshot",
    "PssQuerySnapshot",
    "PssWalkMarkerCreate",
    "PssWalkMarkerFree",
    "PssWalkMarkerGetPosition",
    "PssWalkMarkerSeekToBeginning",
    "PssWalkMarkerSetPosition",
    "PssWalkSnapshot",
]
_arch_optional = [
]
