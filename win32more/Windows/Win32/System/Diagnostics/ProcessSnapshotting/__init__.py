from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Diagnostics.Debug
import win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting
import win32more.Windows.Win32.System.Memory
PSS_PERF_RESOLUTION: UInt32 = 1000000
@winfunctype('KERNEL32.dll')
def PssCaptureSnapshot(ProcessHandle: win32more.Windows.Win32.Foundation.HANDLE, CaptureFlags: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_CAPTURE_FLAGS, ThreadContextFlags: UInt32, SnapshotHandle: POINTER(win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.HPSS)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def PssFreeSnapshot(ProcessHandle: win32more.Windows.Win32.Foundation.HANDLE, SnapshotHandle: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.HPSS) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def PssQuerySnapshot(SnapshotHandle: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.HPSS, InformationClass: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_QUERY_INFORMATION_CLASS, Buffer: VoidPtr, BufferLength: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def PssWalkSnapshot(SnapshotHandle: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.HPSS, InformationClass: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_WALK_INFORMATION_CLASS, WalkMarkerHandle: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.HPSSWALK, Buffer: VoidPtr, BufferLength: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def PssDuplicateSnapshot(SourceProcessHandle: win32more.Windows.Win32.Foundation.HANDLE, SnapshotHandle: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.HPSS, TargetProcessHandle: win32more.Windows.Win32.Foundation.HANDLE, TargetSnapshotHandle: POINTER(win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.HPSS), Flags: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_DUPLICATE_FLAGS) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def PssWalkMarkerCreate(Allocator: POINTER(win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_ALLOCATOR), WalkMarkerHandle: POINTER(win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.HPSSWALK)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def PssWalkMarkerFree(WalkMarkerHandle: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.HPSSWALK) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def PssWalkMarkerGetPosition(WalkMarkerHandle: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.HPSSWALK, Position: POINTER(UIntPtr)) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def PssWalkMarkerSetPosition(WalkMarkerHandle: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.HPSSWALK, Position: UIntPtr) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def PssWalkMarkerSeekToBeginning(WalkMarkerHandle: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.HPSSWALK) -> UInt32: ...
HPSS = VoidPtr
HPSSWALK = VoidPtr
class PSS_ALLOCATOR(Structure):
    Context: VoidPtr
    AllocRoutine: IntPtr
    FreeRoutine: IntPtr
class PSS_AUXILIARY_PAGES_INFORMATION(Structure):
    AuxPagesCaptured: UInt32
class PSS_AUXILIARY_PAGE_ENTRY(Structure):
    Address: VoidPtr
    BasicInformation: win32more.Windows.Win32.System.Memory.MEMORY_BASIC_INFORMATION
    CaptureTime: win32more.Windows.Win32.Foundation.FILETIME
    PageContents: VoidPtr
    PageSize: UInt32
PSS_CAPTURE_FLAGS = UInt32
PSS_CAPTURE_NONE: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_CAPTURE_FLAGS = 0
PSS_CAPTURE_VA_CLONE: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_CAPTURE_FLAGS = 1
PSS_CAPTURE_RESERVED_00000002: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_CAPTURE_FLAGS = 2
PSS_CAPTURE_HANDLES: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_CAPTURE_FLAGS = 4
PSS_CAPTURE_HANDLE_NAME_INFORMATION: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_CAPTURE_FLAGS = 8
PSS_CAPTURE_HANDLE_BASIC_INFORMATION: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_CAPTURE_FLAGS = 16
PSS_CAPTURE_HANDLE_TYPE_SPECIFIC_INFORMATION: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_CAPTURE_FLAGS = 32
PSS_CAPTURE_HANDLE_TRACE: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_CAPTURE_FLAGS = 64
PSS_CAPTURE_THREADS: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_CAPTURE_FLAGS = 128
PSS_CAPTURE_THREAD_CONTEXT: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_CAPTURE_FLAGS = 256
PSS_CAPTURE_THREAD_CONTEXT_EXTENDED: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_CAPTURE_FLAGS = 512
PSS_CAPTURE_RESERVED_00000400: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_CAPTURE_FLAGS = 1024
PSS_CAPTURE_VA_SPACE: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_CAPTURE_FLAGS = 2048
PSS_CAPTURE_VA_SPACE_SECTION_INFORMATION: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_CAPTURE_FLAGS = 4096
PSS_CAPTURE_IPT_TRACE: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_CAPTURE_FLAGS = 8192
PSS_CAPTURE_RESERVED_00004000: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_CAPTURE_FLAGS = 16384
PSS_CREATE_BREAKAWAY_OPTIONAL: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_CAPTURE_FLAGS = 67108864
PSS_CREATE_BREAKAWAY: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_CAPTURE_FLAGS = 134217728
PSS_CREATE_FORCE_BREAKAWAY: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_CAPTURE_FLAGS = 268435456
PSS_CREATE_USE_VM_ALLOCATIONS: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_CAPTURE_FLAGS = 536870912
PSS_CREATE_MEASURE_PERFORMANCE: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_CAPTURE_FLAGS = 1073741824
PSS_CREATE_RELEASE_SECTION: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_CAPTURE_FLAGS = 2147483648
PSS_DUPLICATE_FLAGS = Int32
PSS_DUPLICATE_NONE: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_DUPLICATE_FLAGS = 0
PSS_DUPLICATE_CLOSE_SOURCE: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_DUPLICATE_FLAGS = 1
class PSS_HANDLE_ENTRY(Structure):
    Handle: win32more.Windows.Win32.Foundation.HANDLE
    Flags: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_HANDLE_FLAGS
    ObjectType: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_OBJECT_TYPE
    CaptureTime: win32more.Windows.Win32.Foundation.FILETIME
    Attributes: UInt32
    GrantedAccess: UInt32
    HandleCount: UInt32
    PointerCount: UInt32
    PagedPoolCharge: UInt32
    NonPagedPoolCharge: UInt32
    CreationTime: win32more.Windows.Win32.Foundation.FILETIME
    TypeNameLength: UInt16
    TypeName: win32more.Windows.Win32.Foundation.PWSTR
    ObjectNameLength: UInt16
    ObjectName: win32more.Windows.Win32.Foundation.PWSTR
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
            PebBaseAddress: VoidPtr
            AffinityMask: UIntPtr
            BasePriority: Int32
            ProcessId: UInt32
            ParentProcessId: UInt32
            Flags: UInt32
        class _Thread_e__Struct(Structure):
            ExitStatus: UInt32
            TebBaseAddress: VoidPtr
            ProcessId: UInt32
            ThreadId: UInt32
            AffinityMask: UIntPtr
            Priority: Int32
            BasePriority: Int32
            Win32StartAddress: VoidPtr
        class _Mutant_e__Struct(Structure):
            CurrentCount: Int32
            Abandoned: win32more.Windows.Win32.Foundation.BOOL
            OwnerProcessId: UInt32
            OwnerThreadId: UInt32
        class _Event_e__Struct(Structure):
            ManualReset: win32more.Windows.Win32.Foundation.BOOL
            Signaled: win32more.Windows.Win32.Foundation.BOOL
        class _Section_e__Struct(Structure):
            BaseAddress: VoidPtr
            AllocationAttributes: UInt32
            MaximumSize: Int64
        class _Semaphore_e__Struct(Structure):
            CurrentCount: Int32
            MaximumCount: Int32
PSS_HANDLE_FLAGS = Int32
PSS_HANDLE_NONE: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_HANDLE_FLAGS = 0
PSS_HANDLE_HAVE_TYPE: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_HANDLE_FLAGS = 1
PSS_HANDLE_HAVE_NAME: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_HANDLE_FLAGS = 2
PSS_HANDLE_HAVE_BASIC_INFORMATION: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_HANDLE_FLAGS = 4
PSS_HANDLE_HAVE_TYPE_SPECIFIC_INFORMATION: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_HANDLE_FLAGS = 8
class PSS_HANDLE_INFORMATION(Structure):
    HandlesCaptured: UInt32
class PSS_HANDLE_TRACE_INFORMATION(Structure):
    SectionHandle: win32more.Windows.Win32.Foundation.HANDLE
    Size: UInt32
PSS_OBJECT_TYPE = Int32
PSS_OBJECT_TYPE_UNKNOWN: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_OBJECT_TYPE = 0
PSS_OBJECT_TYPE_PROCESS: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_OBJECT_TYPE = 1
PSS_OBJECT_TYPE_THREAD: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_OBJECT_TYPE = 2
PSS_OBJECT_TYPE_MUTANT: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_OBJECT_TYPE = 3
PSS_OBJECT_TYPE_EVENT: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_OBJECT_TYPE = 4
PSS_OBJECT_TYPE_SECTION: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_OBJECT_TYPE = 5
PSS_OBJECT_TYPE_SEMAPHORE: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_OBJECT_TYPE = 6
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
PSS_PROCESS_FLAGS = Int32
PSS_PROCESS_FLAGS_NONE: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_PROCESS_FLAGS = 0
PSS_PROCESS_FLAGS_PROTECTED: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_PROCESS_FLAGS = 1
PSS_PROCESS_FLAGS_WOW64: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_PROCESS_FLAGS = 2
PSS_PROCESS_FLAGS_RESERVED_03: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_PROCESS_FLAGS = 4
PSS_PROCESS_FLAGS_RESERVED_04: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_PROCESS_FLAGS = 8
PSS_PROCESS_FLAGS_FROZEN: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_PROCESS_FLAGS = 16
class PSS_PROCESS_INFORMATION(Structure):
    ExitStatus: UInt32
    PebBaseAddress: VoidPtr
    AffinityMask: UIntPtr
    BasePriority: Int32
    ProcessId: UInt32
    ParentProcessId: UInt32
    Flags: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_PROCESS_FLAGS
    CreateTime: win32more.Windows.Win32.Foundation.FILETIME
    ExitTime: win32more.Windows.Win32.Foundation.FILETIME
    KernelTime: win32more.Windows.Win32.Foundation.FILETIME
    UserTime: win32more.Windows.Win32.Foundation.FILETIME
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
PSS_QUERY_PROCESS_INFORMATION: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_QUERY_INFORMATION_CLASS = 0
PSS_QUERY_VA_CLONE_INFORMATION: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_QUERY_INFORMATION_CLASS = 1
PSS_QUERY_AUXILIARY_PAGES_INFORMATION: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_QUERY_INFORMATION_CLASS = 2
PSS_QUERY_VA_SPACE_INFORMATION: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_QUERY_INFORMATION_CLASS = 3
PSS_QUERY_HANDLE_INFORMATION: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_QUERY_INFORMATION_CLASS = 4
PSS_QUERY_THREAD_INFORMATION: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_QUERY_INFORMATION_CLASS = 5
PSS_QUERY_HANDLE_TRACE_INFORMATION: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_QUERY_INFORMATION_CLASS = 6
PSS_QUERY_PERFORMANCE_COUNTERS: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_QUERY_INFORMATION_CLASS = 7
class PSS_THREAD_ENTRY(Structure):
    ExitStatus: UInt32
    TebBaseAddress: VoidPtr
    ProcessId: UInt32
    ThreadId: UInt32
    AffinityMask: UIntPtr
    Priority: Int32
    BasePriority: Int32
    LastSyscallFirstArgument: VoidPtr
    LastSyscallNumber: UInt16
    CreateTime: win32more.Windows.Win32.Foundation.FILETIME
    ExitTime: win32more.Windows.Win32.Foundation.FILETIME
    KernelTime: win32more.Windows.Win32.Foundation.FILETIME
    UserTime: win32more.Windows.Win32.Foundation.FILETIME
    Win32StartAddress: VoidPtr
    CaptureTime: win32more.Windows.Win32.Foundation.FILETIME
    Flags: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_THREAD_FLAGS
    SuspendCount: UInt16
    SizeOfContextRecord: UInt16
    ContextRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT)
PSS_THREAD_FLAGS = Int32
PSS_THREAD_FLAGS_NONE: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_THREAD_FLAGS = 0
PSS_THREAD_FLAGS_TERMINATED: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_THREAD_FLAGS = 1
class PSS_THREAD_INFORMATION(Structure):
    ThreadsCaptured: UInt32
    ContextLength: UInt32
class PSS_VA_CLONE_INFORMATION(Structure):
    VaCloneHandle: win32more.Windows.Win32.Foundation.HANDLE
class PSS_VA_SPACE_ENTRY(Structure):
    BaseAddress: VoidPtr
    AllocationBase: VoidPtr
    AllocationProtect: UInt32
    RegionSize: UIntPtr
    State: UInt32
    Protect: UInt32
    Type: UInt32
    TimeDateStamp: UInt32
    SizeOfImage: UInt32
    ImageBase: VoidPtr
    CheckSum: UInt32
    MappedFileNameLength: UInt16
    MappedFileName: win32more.Windows.Win32.Foundation.PWSTR
class PSS_VA_SPACE_INFORMATION(Structure):
    RegionCount: UInt32
PSS_WALK_INFORMATION_CLASS = Int32
PSS_WALK_AUXILIARY_PAGES: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_WALK_INFORMATION_CLASS = 0
PSS_WALK_VA_SPACE: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_WALK_INFORMATION_CLASS = 1
PSS_WALK_HANDLES: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_WALK_INFORMATION_CLASS = 2
PSS_WALK_THREADS: win32more.Windows.Win32.System.Diagnostics.ProcessSnapshotting.PSS_WALK_INFORMATION_CLASS = 3


make_ready(__name__)
