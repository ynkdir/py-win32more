from __future__ import annotations
from win32more._prelude import *
import win32more.Windows.Wdk.Foundation
import win32more.Windows.Wdk.Storage.FileSystem
import win32more.Windows.Wdk.System.SystemServices
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.System.IO
import win32more.Windows.Win32.System.Kernel
import win32more.Windows.Win32.System.Power
class ACCESS_STATE(Structure):
    OperationID: win32more.Windows.Win32.Foundation.LUID
    SecurityEvaluated: win32more.Windows.Win32.Foundation.BOOLEAN
    GenerateAudit: win32more.Windows.Win32.Foundation.BOOLEAN
    GenerateOnClose: win32more.Windows.Win32.Foundation.BOOLEAN
    PrivilegesAllocated: win32more.Windows.Win32.Foundation.BOOLEAN
    Flags: UInt32
    RemainingDesiredAccess: UInt32
    PreviouslyGrantedAccess: UInt32
    OriginalDesiredAccess: UInt32
    SubjectSecurityContext: win32more.Windows.Wdk.Foundation.SECURITY_SUBJECT_CONTEXT
    SecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR
    AuxData: VoidPtr
    Privileges: _Privileges_e__Union
    AuditPrivileges: win32more.Windows.Win32.Foundation.BOOLEAN
    ObjectName: win32more.Windows.Win32.Foundation.UNICODE_STRING
    ObjectTypeName: win32more.Windows.Win32.Foundation.UNICODE_STRING
    class _Privileges_e__Union(Union):
        InitialPrivilegeSet: win32more.Windows.Wdk.System.SystemServices.INITIAL_PRIVILEGE_SET
        PrivilegeSet: win32more.Windows.Win32.Security.PRIVILEGE_SET
NTSTRSAFE_UNICODE_STRING_MAX_CCH: UInt32 = 32767
NTSTRSAFE_USE_SECURE_CRT: UInt32 = 0
NTSTRSAFE_MAX_CCH: UInt32 = 2147483647
NTSTRSAFE_MAX_LENGTH: UInt32 = 2147483646
STRSAFE_IGNORE_NULLS: UInt32 = 256
STRSAFE_FILL_BEHIND_NULL: UInt32 = 512
STRSAFE_FILL_ON_FAILURE: UInt32 = 1024
STRSAFE_NULL_ON_FAILURE: UInt32 = 2048
STRSAFE_NO_TRUNCATION: UInt32 = 4096
STRSAFE_FILL_BEHIND: UInt32 = 512
STRSAFE_ZERO_LENGTH_ON_FAILURE: UInt32 = 2048
__WARNING_CYCLOMATIC_COMPLEXITY: UInt32 = 28734
__WARNING_USING_UNINIT_VAR: UInt32 = 6001
__WARNING_RETURN_UNINIT_VAR: UInt32 = 6101
__WARNING_DEREF_NULL_PTR: UInt32 = 6011
__WARNING_MISSING_ZERO_TERMINATION2: UInt32 = 6054
__WARNING_INVALID_PARAM_VALUE_1: UInt32 = 6387
__WARNING_INCORRECT_ANNOTATION: UInt32 = 26007
__WARNING_POTENTIAL_BUFFER_OVERFLOW_HIGH_PRIORITY: UInt32 = 26015
__WARNING_PRECONDITION_NULLTERMINATION_VIOLATION: UInt32 = 26035
__WARNING_POSTCONDITION_NULLTERMINATION_VIOLATION: UInt32 = 26036
__WARNING_HIGH_PRIORITY_OVERFLOW_POSTCONDITION: UInt32 = 26045
__WARNING_RANGE_POSTCONDITION_VIOLATION: UInt32 = 26061
__WARNING_POTENTIAL_RANGE_POSTCONDITION_VIOLATION: UInt32 = 26071
__WARNING_INVALID_PARAM_VALUE_3: UInt32 = 28183
__WARNING_RETURNING_BAD_RESULT: UInt32 = 28196
__WARNING_BANNED_API_USAGE: UInt32 = 28719
__WARNING_POST_EXPECTED: UInt32 = 28210
@winfunctype('ntdll.dll')
def NtQueryObject(Handle: win32more.Windows.Win32.Foundation.HANDLE, ObjectInformationClass: win32more.Windows.Wdk.Foundation.OBJECT_INFORMATION_CLASS, ObjectInformation: VoidPtr, ObjectInformationLength: UInt32, ReturnLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype('ntdll.dll')
def NtClose(Handle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
class DEVICE_OBJECT(Structure):
    Type: Int16
    Size: UInt16
    ReferenceCount: Int32
    DriverObject: POINTER(win32more.Windows.Wdk.Foundation.DRIVER_OBJECT)
    NextDevice: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)
    AttachedDevice: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)
    CurrentIrp: POINTER(win32more.Windows.Wdk.Foundation.IRP)
    Timer: win32more.Windows.Wdk.Foundation.PIO_TIMER
    Flags: UInt32
    Characteristics: UInt32
    Vpb: POINTER(win32more.Windows.Wdk.Foundation.VPB)
    DeviceExtension: VoidPtr
    DeviceType: UInt32
    StackSize: SByte
    Queue: _Queue_e__Union
    AlignmentRequirement: UInt32
    DeviceQueue: win32more.Windows.Wdk.Foundation.KDEVICE_QUEUE
    Dpc: win32more.Windows.Wdk.Foundation.KDPC
    ActiveThreadCount: UInt32
    SecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR
    DeviceLock: win32more.Windows.Wdk.Foundation.KEVENT
    SectorSize: UInt16
    Spare1: UInt16
    DeviceObjectExtension: POINTER(win32more.Windows.Wdk.Foundation.DEVOBJ_EXTENSION)
    Reserved: VoidPtr
    class _Queue_e__Union(Union):
        ListEntry: win32more.Windows.Win32.System.Kernel.LIST_ENTRY
        Wcb: win32more.Windows.Wdk.System.SystemServices.WAIT_CONTEXT_BLOCK
class DEVOBJ_EXTENSION(Structure):
    Type: Int16
    Size: UInt16
    DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)
    PowerFlags: UInt32
    Dope: POINTER(win32more.Windows.Wdk.Foundation._DEVICE_OBJECT_POWER_EXTENSION)
    ExtensionFlags: UInt32
    DeviceNode: VoidPtr
    AttachedTo: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)
    StartIoCount: Int32
    StartIoKey: Int32
    StartIoFlags: UInt32
    Vpb: POINTER(win32more.Windows.Wdk.Foundation.VPB)
    DependencyNode: VoidPtr
    InterruptContext: VoidPtr
    InterruptCount: Int32
    VerifierContext: VoidPtr
class DISPATCHER_HEADER(Structure):
    Anonymous: _Anonymous_e__Union
    SignalState: Int32
    WaitListHead: win32more.Windows.Win32.System.Kernel.LIST_ENTRY
    _anonymous_ = ('Anonymous',)
    class _Anonymous_e__Union(Union):
        Anonymous1: _Anonymous1_e__Union
        Anonymous2: _Anonymous2_e__Struct
        Anonymous3: _Anonymous3_e__Struct
        Anonymous4: _Anonymous4_e__Struct
        Anonymous5: _Anonymous5_e__Struct
        Anonymous6: _Anonymous6_e__Struct
        Anonymous7: _Anonymous7_e__Struct
        _anonymous_ = ('Anonymous1', 'Anonymous2', 'Anonymous3', 'Anonymous4', 'Anonymous5', 'Anonymous6', 'Anonymous7')
        class _Anonymous1_e__Union(Union):
            Lock: Int32
            LockNV: Int32
        class _Anonymous2_e__Struct(Structure):
            Type: Byte
            Signalling: Byte
            Size: Byte
            Reserved1: Byte
        class _Anonymous3_e__Struct(Structure):
            TimerType: Byte
            Anonymous1: _Anonymous1_e__Union
            Hand: Byte
            Anonymous2: _Anonymous2_e__Union
            _anonymous_ = ('Anonymous1', 'Anonymous2')
            class _Anonymous1_e__Union(Union):
                TimerControlFlags: Byte
                Anonymous: _Anonymous_e__Struct
                _anonymous_ = ('Anonymous',)
                class _Anonymous_e__Struct(Structure):
                    Absolute: Annotated[Byte, NativeBitfieldAttribute(1)]
                    Wake: Annotated[Byte, NativeBitfieldAttribute(1)]
                    EncodedTolerableDelay: Annotated[Byte, NativeBitfieldAttribute(6)]
            class _Anonymous2_e__Union(Union):
                TimerMiscFlags: Byte
                Anonymous: _Anonymous_e__Struct
                _anonymous_ = ('Anonymous',)
                class _Anonymous_e__Struct(Structure):
                    Index: Annotated[Byte, NativeBitfieldAttribute(1)]
                    Processor: Annotated[Byte, NativeBitfieldAttribute(5)]
                    Inserted: Annotated[Byte, NativeBitfieldAttribute(1)]
                    Expired: Annotated[Byte, NativeBitfieldAttribute(1)]
        class _Anonymous4_e__Struct(Structure):
            Timer2Type: Byte
            Anonymous: _Anonymous_e__Union
            Timer2ComponentId: Byte
            Timer2RelativeId: Byte
            _anonymous_ = ('Anonymous',)
            class _Anonymous_e__Union(Union):
                Timer2Flags: Byte
                Anonymous: _Anonymous_e__Struct
                _anonymous_ = ('Anonymous',)
                class _Anonymous_e__Struct(Structure):
                    Timer2Inserted: Annotated[Byte, NativeBitfieldAttribute(1)]
                    Timer2Expiring: Annotated[Byte, NativeBitfieldAttribute(1)]
                    Timer2CancelPending: Annotated[Byte, NativeBitfieldAttribute(1)]
                    Timer2SetPending: Annotated[Byte, NativeBitfieldAttribute(1)]
                    Timer2Running: Annotated[Byte, NativeBitfieldAttribute(1)]
                    Timer2Disabled: Annotated[Byte, NativeBitfieldAttribute(1)]
                    Timer2ReservedFlags: Annotated[Byte, NativeBitfieldAttribute(2)]
        class _Anonymous5_e__Struct(Structure):
            QueueType: Byte
            Anonymous: _Anonymous_e__Union
            QueueSize: Byte
            QueueReserved: Byte
            _anonymous_ = ('Anonymous',)
            class _Anonymous_e__Union(Union):
                QueueControlFlags: Byte
                Anonymous: _Anonymous_e__Struct
                _anonymous_ = ('Anonymous',)
                class _Anonymous_e__Struct(Structure):
                    Abandoned: Annotated[Byte, NativeBitfieldAttribute(1)]
                    DisableIncrement: Annotated[Byte, NativeBitfieldAttribute(1)]
                    QueueReservedControlFlags: Annotated[Byte, NativeBitfieldAttribute(6)]
        class _Anonymous6_e__Struct(Structure):
            ThreadType: Byte
            ThreadReserved: Byte
            Anonymous1: _Anonymous1_e__Union
            Anonymous2: _Anonymous2_e__Union
            _anonymous_ = ('Anonymous1', 'Anonymous2')
            class _Anonymous1_e__Union(Union):
                ThreadControlFlags: Byte
                Anonymous: _Anonymous_e__Struct
                _anonymous_ = ('Anonymous',)
                class _Anonymous_e__Struct(Structure):
                    CycleProfiling: Annotated[Byte, NativeBitfieldAttribute(1)]
                    CounterProfiling: Annotated[Byte, NativeBitfieldAttribute(1)]
                    GroupScheduling: Annotated[Byte, NativeBitfieldAttribute(1)]
                    AffinitySet: Annotated[Byte, NativeBitfieldAttribute(1)]
                    Tagged: Annotated[Byte, NativeBitfieldAttribute(1)]
                    EnergyProfiling: Annotated[Byte, NativeBitfieldAttribute(1)]
                    SchedulerAssist: Annotated[Byte, NativeBitfieldAttribute(1)]
                    Instrumented: Annotated[Byte, NativeBitfieldAttribute(1)]
            class _Anonymous2_e__Union(Union):
                DebugActive: Byte
        class _Anonymous7_e__Struct(Structure):
            MutantType: Byte
            MutantSize: Byte
            DpcActive: win32more.Windows.Win32.Foundation.BOOLEAN
            MutantReserved: Byte
DMA_COMMON_BUFFER_VECTOR = IntPtr
@winfunctype_pointer
def DRIVER_ADD_DEVICE(DriverObject: POINTER(win32more.Windows.Wdk.Foundation.DRIVER_OBJECT), PhysicalDeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype_pointer
def DRIVER_CANCEL(DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT), Irp: POINTER(win32more.Windows.Wdk.Foundation.IRP)) -> Void: ...
@winfunctype_pointer
def DRIVER_CONTROL(DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT), Irp: POINTER(win32more.Windows.Wdk.Foundation.IRP), MapRegisterBase: VoidPtr, Context: VoidPtr) -> win32more.Windows.Wdk.System.SystemServices.IO_ALLOCATION_ACTION: ...
@winfunctype_pointer
def DRIVER_DISPATCH(DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT), Irp: POINTER(win32more.Windows.Wdk.Foundation.IRP)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype_pointer
def DRIVER_DISPATCH_PAGED(DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT), Irp: POINTER(win32more.Windows.Wdk.Foundation.IRP)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
class DRIVER_EXTENSION(Structure):
    DriverObject: POINTER(win32more.Windows.Wdk.Foundation.DRIVER_OBJECT)
    AddDevice: win32more.Windows.Wdk.Foundation.DRIVER_ADD_DEVICE
    Count: UInt32
    ServiceKeyName: win32more.Windows.Win32.Foundation.UNICODE_STRING
@winfunctype_pointer
def DRIVER_FS_NOTIFICATION(DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT), FsActive: win32more.Windows.Win32.Foundation.BOOLEAN) -> Void: ...
@winfunctype_pointer
def DRIVER_INITIALIZE(DriverObject: POINTER(win32more.Windows.Wdk.Foundation.DRIVER_OBJECT), RegistryPath: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype_pointer
def DRIVER_NOTIFICATION_CALLBACK_ROUTINE(NotificationStructure: VoidPtr, Context: VoidPtr) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
class DRIVER_OBJECT(Structure):
    Type: Int16
    Size: Int16
    DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)
    Flags: UInt32
    DriverStart: VoidPtr
    DriverSize: UInt32
    DriverSection: VoidPtr
    DriverExtension: POINTER(win32more.Windows.Wdk.Foundation.DRIVER_EXTENSION)
    DriverName: win32more.Windows.Win32.Foundation.UNICODE_STRING
    HardwareDatabase: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING)
    FastIoDispatch: POINTER(win32more.Windows.Wdk.Foundation.FAST_IO_DISPATCH)
    DriverInit: win32more.Windows.Wdk.Foundation.DRIVER_INITIALIZE
    DriverStartIo: win32more.Windows.Wdk.Foundation.DRIVER_STARTIO
    DriverUnload: win32more.Windows.Wdk.Foundation.DRIVER_UNLOAD
    MajorFunction: win32more.Windows.Wdk.Foundation.DRIVER_DISPATCH * 28
@winfunctype_pointer
def DRIVER_REINITIALIZE(DriverObject: POINTER(win32more.Windows.Wdk.Foundation.DRIVER_OBJECT), Context: VoidPtr, Count: UInt32) -> Void: ...
@winfunctype_pointer
def DRIVER_STARTIO(DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT), Irp: POINTER(win32more.Windows.Wdk.Foundation.IRP)) -> Void: ...
@winfunctype_pointer
def DRIVER_UNLOAD(DriverObject: POINTER(win32more.Windows.Wdk.Foundation.DRIVER_OBJECT)) -> Void: ...
ECP_HEADER = IntPtr
ECP_LIST = IntPtr
class ERESOURCE(Structure):
    SystemResourcesList: win32more.Windows.Win32.System.Kernel.LIST_ENTRY
    OwnerTable: POINTER(win32more.Windows.Wdk.Foundation.OWNER_ENTRY)
    ActiveCount: Int16
    Anonymous1: _Anonymous1_e__Union
    SharedWaiters: VoidPtr
    ExclusiveWaiters: VoidPtr
    OwnerEntry: win32more.Windows.Wdk.Foundation.OWNER_ENTRY
    ActiveEntries: UInt32
    ContentionCount: UInt32
    NumberOfSharedWaiters: UInt32
    NumberOfExclusiveWaiters: UInt32
    Anonymous2: _Anonymous2_e__Union
    SpinLock: UIntPtr
    _anonymous_ = ('Anonymous1', 'Anonymous2')
    class _Anonymous1_e__Union(Union):
        Flag: UInt16
        Anonymous: _Anonymous_e__Struct
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            ReservedLowFlags: Byte
            WaiterPriority: Byte
    class _Anonymous2_e__Union(Union):
        Address: VoidPtr
        CreatorBackTraceIndex: UIntPtr
@winfunctype_pointer
def FAST_IO_ACQUIRE_FILE(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT)) -> Void: ...
@winfunctype_pointer
def FAST_IO_ACQUIRE_FOR_CCFLUSH(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype_pointer
def FAST_IO_ACQUIRE_FOR_MOD_WRITE(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), EndingOffset: POINTER(Int64), ResourceToRelease: POINTER(POINTER(win32more.Windows.Wdk.Foundation.ERESOURCE)), DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype_pointer
def FAST_IO_CHECK_IF_POSSIBLE(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), FileOffset: POINTER(Int64), Length: UInt32, Wait: win32more.Windows.Win32.Foundation.BOOLEAN, LockKey: UInt32, CheckForReadOperation: win32more.Windows.Win32.Foundation.BOOLEAN, IoStatus: POINTER(win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK), DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype_pointer
def FAST_IO_DETACH_DEVICE(SourceDevice: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT), TargetDevice: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)) -> Void: ...
@winfunctype_pointer
def FAST_IO_DEVICE_CONTROL(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), Wait: win32more.Windows.Win32.Foundation.BOOLEAN, InputBuffer: VoidPtr, InputBufferLength: UInt32, OutputBuffer: VoidPtr, OutputBufferLength: UInt32, IoControlCode: UInt32, IoStatus: POINTER(win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK), DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
class FAST_IO_DISPATCH(Structure):
    SizeOfFastIoDispatch: UInt32
    FastIoCheckIfPossible: win32more.Windows.Wdk.Foundation.FAST_IO_CHECK_IF_POSSIBLE
    FastIoRead: win32more.Windows.Wdk.Foundation.FAST_IO_READ
    FastIoWrite: win32more.Windows.Wdk.Foundation.FAST_IO_WRITE
    FastIoQueryBasicInfo: win32more.Windows.Wdk.Foundation.FAST_IO_QUERY_BASIC_INFO
    FastIoQueryStandardInfo: win32more.Windows.Wdk.Foundation.FAST_IO_QUERY_STANDARD_INFO
    FastIoLock: win32more.Windows.Wdk.Foundation.FAST_IO_LOCK
    FastIoUnlockSingle: win32more.Windows.Wdk.Foundation.FAST_IO_UNLOCK_SINGLE
    FastIoUnlockAll: win32more.Windows.Wdk.Foundation.FAST_IO_UNLOCK_ALL
    FastIoUnlockAllByKey: win32more.Windows.Wdk.Foundation.FAST_IO_UNLOCK_ALL_BY_KEY
    FastIoDeviceControl: win32more.Windows.Wdk.Foundation.FAST_IO_DEVICE_CONTROL
    AcquireFileForNtCreateSection: win32more.Windows.Wdk.Foundation.FAST_IO_ACQUIRE_FILE
    ReleaseFileForNtCreateSection: win32more.Windows.Wdk.Foundation.FAST_IO_RELEASE_FILE
    FastIoDetachDevice: win32more.Windows.Wdk.Foundation.FAST_IO_DETACH_DEVICE
    FastIoQueryNetworkOpenInfo: win32more.Windows.Wdk.Foundation.FAST_IO_QUERY_NETWORK_OPEN_INFO
    AcquireForModWrite: win32more.Windows.Wdk.Foundation.FAST_IO_ACQUIRE_FOR_MOD_WRITE
    MdlRead: win32more.Windows.Wdk.Foundation.FAST_IO_MDL_READ
    MdlReadComplete: win32more.Windows.Wdk.Foundation.FAST_IO_MDL_READ_COMPLETE
    PrepareMdlWrite: win32more.Windows.Wdk.Foundation.FAST_IO_PREPARE_MDL_WRITE
    MdlWriteComplete: win32more.Windows.Wdk.Foundation.FAST_IO_MDL_WRITE_COMPLETE
    FastIoReadCompressed: win32more.Windows.Wdk.Foundation.FAST_IO_READ_COMPRESSED
    FastIoWriteCompressed: win32more.Windows.Wdk.Foundation.FAST_IO_WRITE_COMPRESSED
    MdlReadCompleteCompressed: win32more.Windows.Wdk.Foundation.FAST_IO_MDL_READ_COMPLETE_COMPRESSED
    MdlWriteCompleteCompressed: win32more.Windows.Wdk.Foundation.FAST_IO_MDL_WRITE_COMPLETE_COMPRESSED
    FastIoQueryOpen: win32more.Windows.Wdk.Foundation.FAST_IO_QUERY_OPEN
    ReleaseForModWrite: win32more.Windows.Wdk.Foundation.FAST_IO_RELEASE_FOR_MOD_WRITE
    AcquireForCcFlush: win32more.Windows.Wdk.Foundation.FAST_IO_ACQUIRE_FOR_CCFLUSH
    ReleaseForCcFlush: win32more.Windows.Wdk.Foundation.FAST_IO_RELEASE_FOR_CCFLUSH
@winfunctype_pointer
def FAST_IO_LOCK(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), FileOffset: POINTER(Int64), Length: POINTER(Int64), ProcessId: win32more.Windows.Wdk.Foundation.PEPROCESS, Key: UInt32, FailImmediately: win32more.Windows.Win32.Foundation.BOOLEAN, ExclusiveLock: win32more.Windows.Win32.Foundation.BOOLEAN, IoStatus: POINTER(win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK), DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype_pointer
def FAST_IO_MDL_READ(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), FileOffset: POINTER(Int64), Length: UInt32, LockKey: UInt32, MdlChain: POINTER(POINTER(win32more.Windows.Wdk.Foundation.MDL)), IoStatus: POINTER(win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK), DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype_pointer
def FAST_IO_MDL_READ_COMPLETE(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), MdlChain: POINTER(win32more.Windows.Wdk.Foundation.MDL), DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype_pointer
def FAST_IO_MDL_READ_COMPLETE_COMPRESSED(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), MdlChain: POINTER(win32more.Windows.Wdk.Foundation.MDL), DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype_pointer
def FAST_IO_MDL_WRITE_COMPLETE(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), FileOffset: POINTER(Int64), MdlChain: POINTER(win32more.Windows.Wdk.Foundation.MDL), DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype_pointer
def FAST_IO_MDL_WRITE_COMPLETE_COMPRESSED(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), FileOffset: POINTER(Int64), MdlChain: POINTER(win32more.Windows.Wdk.Foundation.MDL), DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype_pointer
def FAST_IO_PREPARE_MDL_WRITE(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), FileOffset: POINTER(Int64), Length: UInt32, LockKey: UInt32, MdlChain: POINTER(POINTER(win32more.Windows.Wdk.Foundation.MDL)), IoStatus: POINTER(win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK), DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype_pointer
def FAST_IO_QUERY_BASIC_INFO(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), Wait: win32more.Windows.Win32.Foundation.BOOLEAN, Buffer: POINTER(win32more.Windows.Wdk.Storage.FileSystem.FILE_BASIC_INFORMATION), IoStatus: POINTER(win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK), DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype_pointer
def FAST_IO_QUERY_NETWORK_OPEN_INFO(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), Wait: win32more.Windows.Win32.Foundation.BOOLEAN, Buffer: POINTER(win32more.Windows.Wdk.Storage.FileSystem.FILE_NETWORK_OPEN_INFORMATION), IoStatus: POINTER(win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK), DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype_pointer
def FAST_IO_QUERY_OPEN(Irp: POINTER(win32more.Windows.Wdk.Foundation.IRP), NetworkInformation: POINTER(win32more.Windows.Wdk.Storage.FileSystem.FILE_NETWORK_OPEN_INFORMATION), DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype_pointer
def FAST_IO_QUERY_STANDARD_INFO(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), Wait: win32more.Windows.Win32.Foundation.BOOLEAN, Buffer: POINTER(win32more.Windows.Wdk.Storage.FileSystem.FILE_STANDARD_INFORMATION), IoStatus: POINTER(win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK), DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype_pointer
def FAST_IO_READ(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), FileOffset: POINTER(Int64), Length: UInt32, Wait: win32more.Windows.Win32.Foundation.BOOLEAN, LockKey: UInt32, Buffer: VoidPtr, IoStatus: POINTER(win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK), DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype_pointer
def FAST_IO_READ_COMPRESSED(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), FileOffset: POINTER(Int64), Length: UInt32, LockKey: UInt32, Buffer: VoidPtr, MdlChain: POINTER(POINTER(win32more.Windows.Wdk.Foundation.MDL)), IoStatus: POINTER(win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK), CompressedDataInfo: POINTER(win32more.Windows.Wdk.Storage.FileSystem.COMPRESSED_DATA_INFO), CompressedDataInfoLength: UInt32, DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype_pointer
def FAST_IO_RELEASE_FILE(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT)) -> Void: ...
@winfunctype_pointer
def FAST_IO_RELEASE_FOR_CCFLUSH(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype_pointer
def FAST_IO_RELEASE_FOR_MOD_WRITE(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), ResourceToRelease: POINTER(win32more.Windows.Wdk.Foundation.ERESOURCE), DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)) -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
@winfunctype_pointer
def FAST_IO_UNLOCK_ALL(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), ProcessId: win32more.Windows.Wdk.Foundation.PEPROCESS, IoStatus: POINTER(win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK), DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype_pointer
def FAST_IO_UNLOCK_ALL_BY_KEY(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), ProcessId: VoidPtr, Key: UInt32, IoStatus: POINTER(win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK), DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype_pointer
def FAST_IO_UNLOCK_SINGLE(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), FileOffset: POINTER(Int64), Length: POINTER(Int64), ProcessId: win32more.Windows.Wdk.Foundation.PEPROCESS, Key: UInt32, IoStatus: POINTER(win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK), DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype_pointer
def FAST_IO_WRITE(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), FileOffset: POINTER(Int64), Length: UInt32, Wait: win32more.Windows.Win32.Foundation.BOOLEAN, LockKey: UInt32, Buffer: VoidPtr, IoStatus: POINTER(win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK), DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
@winfunctype_pointer
def FAST_IO_WRITE_COMPRESSED(FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT), FileOffset: POINTER(Int64), Length: UInt32, LockKey: UInt32, Buffer: VoidPtr, MdlChain: POINTER(POINTER(win32more.Windows.Wdk.Foundation.MDL)), IoStatus: POINTER(win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK), CompressedDataInfo: POINTER(win32more.Windows.Wdk.Storage.FileSystem.COMPRESSED_DATA_INFO), CompressedDataInfoLength: UInt32, DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)) -> win32more.Windows.Win32.Foundation.BOOLEAN: ...
class FAST_MUTEX(Structure):
    Count: Int32
    Owner: VoidPtr
    Contention: UInt32
    Event: win32more.Windows.Wdk.Foundation.KEVENT
    OldIrql: UInt32
class FILE_OBJECT(Structure):
    Type: Int16
    Size: Int16
    DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)
    Vpb: POINTER(win32more.Windows.Wdk.Foundation.VPB)
    FsContext: VoidPtr
    FsContext2: VoidPtr
    SectionObjectPointer: POINTER(win32more.Windows.Wdk.Foundation.SECTION_OBJECT_POINTERS)
    PrivateCacheMap: VoidPtr
    FinalStatus: win32more.Windows.Win32.Foundation.NTSTATUS
    RelatedFileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT)
    LockOperation: win32more.Windows.Win32.Foundation.BOOLEAN
    DeletePending: win32more.Windows.Win32.Foundation.BOOLEAN
    ReadAccess: win32more.Windows.Win32.Foundation.BOOLEAN
    WriteAccess: win32more.Windows.Win32.Foundation.BOOLEAN
    DeleteAccess: win32more.Windows.Win32.Foundation.BOOLEAN
    SharedRead: win32more.Windows.Win32.Foundation.BOOLEAN
    SharedWrite: win32more.Windows.Win32.Foundation.BOOLEAN
    SharedDelete: win32more.Windows.Win32.Foundation.BOOLEAN
    Flags: UInt32
    FileName: win32more.Windows.Win32.Foundation.UNICODE_STRING
    CurrentByteOffset: Int64
    Waiters: UInt32
    Busy: UInt32
    LastLock: VoidPtr
    Lock: win32more.Windows.Wdk.Foundation.KEVENT
    Event: win32more.Windows.Wdk.Foundation.KEVENT
    CompletionContext: POINTER(win32more.Windows.Wdk.Foundation.IO_COMPLETION_CONTEXT)
    IrpListLock: UIntPtr
    IrpList: win32more.Windows.Win32.System.Kernel.LIST_ENTRY
    FileObjectExtension: VoidPtr
IOMMU_DMA_DEVICE = IntPtr
IOMMU_DMA_DOMAIN = IntPtr
class IO_COMPLETION_CONTEXT(Structure):
    Port: VoidPtr
    Key: VoidPtr
    UsageCount: IntPtr
IO_PRIORITY_HINT = Int32
IoPriorityVeryLow: win32more.Windows.Wdk.Foundation.IO_PRIORITY_HINT = 0
IoPriorityLow: win32more.Windows.Wdk.Foundation.IO_PRIORITY_HINT = 1
IoPriorityNormal: win32more.Windows.Wdk.Foundation.IO_PRIORITY_HINT = 2
IoPriorityHigh: win32more.Windows.Wdk.Foundation.IO_PRIORITY_HINT = 3
IoPriorityCritical: win32more.Windows.Wdk.Foundation.IO_PRIORITY_HINT = 4
MaxIoPriorityTypes: win32more.Windows.Wdk.Foundation.IO_PRIORITY_HINT = 5
class IO_SECURITY_CONTEXT(Structure):
    SecurityQos: POINTER(win32more.Windows.Win32.Security.SECURITY_QUALITY_OF_SERVICE)
    AccessState: POINTER(win32more.Windows.Wdk.Foundation.ACCESS_STATE)
    DesiredAccess: UInt32
    FullCreateOptions: UInt32
class IO_STACK_LOCATION(Structure):
    MajorFunction: Byte
    MinorFunction: Byte
    Flags: Byte
    Control: Byte
    Parameters: _Parameters_e__Union
    DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)
    FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT)
    CompletionRoutine: win32more.Windows.Wdk.Foundation.PIO_COMPLETION_ROUTINE
    Context: VoidPtr
    class _Parameters_e__Union(Union):
        Create: _Create_e__Struct
        CreatePipe: _CreatePipe_e__Struct
        CreateMailslot: _CreateMailslot_e__Struct
        Read: _Read_e__Struct
        Write: _Write_e__Struct
        QueryDirectory: _QueryDirectory_e__Struct
        NotifyDirectory: _NotifyDirectory_e__Struct
        NotifyDirectoryEx: _NotifyDirectoryEx_e__Struct
        QueryFile: _QueryFile_e__Struct
        SetFile: _SetFile_e__Struct
        QueryEa: _QueryEa_e__Struct
        SetEa: _SetEa_e__Struct
        QueryVolume: _QueryVolume_e__Struct
        SetVolume: _SetVolume_e__Struct
        FileSystemControl: _FileSystemControl_e__Struct
        LockControl: _LockControl_e__Struct
        DeviceIoControl: _DeviceIoControl_e__Struct
        QuerySecurity: _QuerySecurity_e__Struct
        SetSecurity: _SetSecurity_e__Struct
        MountVolume: _MountVolume_e__Struct
        VerifyVolume: _VerifyVolume_e__Struct
        Scsi: _Scsi_e__Struct
        QueryQuota: _QueryQuota_e__Struct
        SetQuota: _SetQuota_e__Struct
        QueryDeviceRelations: _QueryDeviceRelations_e__Struct
        QueryInterface: _QueryInterface_e__Struct
        DeviceCapabilities: _DeviceCapabilities_e__Struct
        FilterResourceRequirements: _FilterResourceRequirements_e__Struct
        ReadWriteConfig: _ReadWriteConfig_e__Struct
        SetLock: _SetLock_e__Struct
        QueryId: _QueryId_e__Struct
        QueryDeviceText: _QueryDeviceText_e__Struct
        UsageNotification: _UsageNotification_e__Struct
        WaitWake: _WaitWake_e__Struct
        PowerSequence: _PowerSequence_e__Struct
        Power: _Power_e__Struct
        StartDevice: _StartDevice_e__Struct
        WMI: _WMI_e__Struct
        Others: _Others_e__Struct
        class _Create_e__Struct(Structure):
            SecurityContext: POINTER(win32more.Windows.Wdk.Foundation.IO_SECURITY_CONTEXT)
            Options: UInt32
            FileAttributes: UInt16
            ShareAccess: UInt16
            EaLength: UInt32
        class _CreatePipe_e__Struct(Structure):
            SecurityContext: POINTER(win32more.Windows.Wdk.Foundation.IO_SECURITY_CONTEXT)
            Options: UInt32
            Reserved: UInt16
            ShareAccess: UInt16
            Parameters: POINTER(win32more.Windows.Wdk.System.SystemServices.NAMED_PIPE_CREATE_PARAMETERS)
        class _CreateMailslot_e__Struct(Structure):
            SecurityContext: POINTER(win32more.Windows.Wdk.Foundation.IO_SECURITY_CONTEXT)
            Options: UInt32
            Reserved: UInt16
            ShareAccess: UInt16
            Parameters: POINTER(win32more.Windows.Wdk.System.SystemServices.MAILSLOT_CREATE_PARAMETERS)
        class _Read_e__Struct(Structure):
            Length: UInt32
            Key: UInt32
            ByteOffset: Int64
            _pack_ = 4
        class _Write_e__Struct(Structure):
            Length: UInt32
            Key: UInt32
            ByteOffset: Int64
            _pack_ = 4
        class _QueryDirectory_e__Struct(Structure):
            Length: UInt32
            FileName: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING)
            FileInformationClass: win32more.Windows.Wdk.Storage.FileSystem.FILE_INFORMATION_CLASS
            FileIndex: UInt32
        class _NotifyDirectory_e__Struct(Structure):
            Length: UInt32
            CompletionFilter: UInt32
        class _NotifyDirectoryEx_e__Struct(Structure):
            Length: UInt32
            CompletionFilter: UInt32
            DirectoryNotifyInformationClass: win32more.Windows.Wdk.System.SystemServices.DIRECTORY_NOTIFY_INFORMATION_CLASS
        class _QueryFile_e__Struct(Structure):
            Length: UInt32
            FileInformationClass: win32more.Windows.Wdk.Storage.FileSystem.FILE_INFORMATION_CLASS
        class _SetFile_e__Struct(Structure):
            Length: UInt32
            FileInformationClass: win32more.Windows.Wdk.Storage.FileSystem.FILE_INFORMATION_CLASS
            FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT)
            Anonymous: _Anonymous_e__Union
            _anonymous_ = ('Anonymous',)
            class _Anonymous_e__Union(Union):
                Anonymous: _Anonymous_e__Struct
                ClusterCount: UInt32
                DeleteHandle: win32more.Windows.Win32.Foundation.HANDLE
                _anonymous_ = ('Anonymous',)
                class _Anonymous_e__Struct(Structure):
                    ReplaceIfExists: win32more.Windows.Win32.Foundation.BOOLEAN
                    AdvanceOnly: win32more.Windows.Win32.Foundation.BOOLEAN
        class _QueryEa_e__Struct(Structure):
            Length: UInt32
            EaList: VoidPtr
            EaListLength: UInt32
            EaIndex: UInt32
        class _SetEa_e__Struct(Structure):
            Length: UInt32
        class _QueryVolume_e__Struct(Structure):
            Length: UInt32
            FsInformationClass: win32more.Windows.Wdk.Storage.FileSystem.FS_INFORMATION_CLASS
        class _SetVolume_e__Struct(Structure):
            Length: UInt32
            FsInformationClass: win32more.Windows.Wdk.Storage.FileSystem.FS_INFORMATION_CLASS
        class _FileSystemControl_e__Struct(Structure):
            OutputBufferLength: UInt32
            InputBufferLength: UInt32
            FsControlCode: UInt32
            Type3InputBuffer: VoidPtr
        class _LockControl_e__Struct(Structure):
            Length: POINTER(Int64)
            Key: UInt32
            ByteOffset: Int64
            _pack_ = 4
        class _DeviceIoControl_e__Struct(Structure):
            OutputBufferLength: UInt32
            InputBufferLength: UInt32
            IoControlCode: UInt32
            Type3InputBuffer: VoidPtr
        class _QuerySecurity_e__Struct(Structure):
            SecurityInformation: UInt32
            Length: UInt32
        class _SetSecurity_e__Struct(Structure):
            SecurityInformation: UInt32
            SecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR
        class _MountVolume_e__Struct(Structure):
            Vpb: POINTER(win32more.Windows.Wdk.Foundation.VPB)
            DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)
        class _VerifyVolume_e__Struct(Structure):
            Vpb: POINTER(win32more.Windows.Wdk.Foundation.VPB)
            DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)
        class _Scsi_e__Struct(Structure):
            Srb: POINTER(win32more.Windows.Wdk.Foundation._SCSI_REQUEST_BLOCK)
        class _QueryQuota_e__Struct(Structure):
            Length: UInt32
            StartSid: win32more.Windows.Win32.Security.PSID
            SidList: POINTER(win32more.Windows.Wdk.Storage.FileSystem.FILE_GET_QUOTA_INFORMATION)
            SidListLength: UInt32
        class _SetQuota_e__Struct(Structure):
            Length: UInt32
        class _QueryDeviceRelations_e__Struct(Structure):
            Type: win32more.Windows.Wdk.System.SystemServices.DEVICE_RELATION_TYPE
        class _QueryInterface_e__Struct(Structure):
            InterfaceType: POINTER(Guid)
            Size: UInt16
            Version: UInt16
            Interface: POINTER(win32more.Windows.Wdk.System.SystemServices.INTERFACE)
            InterfaceSpecificData: VoidPtr
        class _DeviceCapabilities_e__Struct(Structure):
            Capabilities: POINTER(win32more.Windows.Wdk.System.SystemServices.DEVICE_CAPABILITIES)
        class _FilterResourceRequirements_e__Struct(Structure):
            IoResourceRequirementList: POINTER(win32more.Windows.Wdk.System.SystemServices.IO_RESOURCE_REQUIREMENTS_LIST)
        class _ReadWriteConfig_e__Struct(Structure):
            WhichSpace: UInt32
            Buffer: VoidPtr
            Offset: UInt32
            Length: UInt32
        class _SetLock_e__Struct(Structure):
            Lock: win32more.Windows.Win32.Foundation.BOOLEAN
        class _QueryId_e__Struct(Structure):
            IdType: win32more.Windows.Wdk.System.SystemServices.BUS_QUERY_ID_TYPE
        class _QueryDeviceText_e__Struct(Structure):
            DeviceTextType: win32more.Windows.Wdk.System.SystemServices.DEVICE_TEXT_TYPE
            LocaleId: UInt32
        class _UsageNotification_e__Struct(Structure):
            InPath: win32more.Windows.Win32.Foundation.BOOLEAN
            Reserved: win32more.Windows.Win32.Foundation.BOOLEAN * 3
            Type: win32more.Windows.Wdk.System.SystemServices.DEVICE_USAGE_NOTIFICATION_TYPE
        class _WaitWake_e__Struct(Structure):
            PowerState: win32more.Windows.Win32.System.Power.SYSTEM_POWER_STATE
        class _PowerSequence_e__Struct(Structure):
            PowerSequence: POINTER(win32more.Windows.Wdk.System.SystemServices.POWER_SEQUENCE)
        class _Power_e__Struct(Structure):
            Anonymous: _Anonymous_e__Union
            Type: win32more.Windows.Wdk.System.SystemServices.POWER_STATE_TYPE
            State: win32more.Windows.Wdk.System.SystemServices.POWER_STATE
            ShutdownType: win32more.Windows.Win32.System.Power.POWER_ACTION
            _anonymous_ = ('Anonymous',)
            class _Anonymous_e__Union(Union):
                SystemContext: UInt32
                SystemPowerStateContext: win32more.Windows.Wdk.System.SystemServices.SYSTEM_POWER_STATE_CONTEXT
        class _StartDevice_e__Struct(Structure):
            AllocatedResources: POINTER(win32more.Windows.Wdk.System.SystemServices.CM_RESOURCE_LIST)
            AllocatedResourcesTranslated: POINTER(win32more.Windows.Wdk.System.SystemServices.CM_RESOURCE_LIST)
        class _WMI_e__Struct(Structure):
            ProviderId: UIntPtr
            DataPath: VoidPtr
            BufferSize: UInt32
            Buffer: VoidPtr
        class _Others_e__Struct(Structure):
            Argument1: VoidPtr
            Argument2: VoidPtr
            Argument3: VoidPtr
            Argument4: VoidPtr
class IRP(Structure):
    Type: Int16
    Size: UInt16
    MdlAddress: POINTER(win32more.Windows.Wdk.Foundation.MDL)
    Flags: UInt32
    AssociatedIrp: _AssociatedIrp_e__Union
    ThreadListEntry: win32more.Windows.Win32.System.Kernel.LIST_ENTRY
    IoStatus: win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK
    RequestorMode: SByte
    PendingReturned: win32more.Windows.Win32.Foundation.BOOLEAN
    StackCount: win32more.Windows.Win32.Foundation.CHAR
    CurrentLocation: win32more.Windows.Win32.Foundation.CHAR
    Cancel: win32more.Windows.Win32.Foundation.BOOLEAN
    CancelIrql: Byte
    ApcEnvironment: SByte
    AllocationFlags: Byte
    Anonymous: _Anonymous_e__Union
    UserEvent: POINTER(win32more.Windows.Wdk.Foundation.KEVENT)
    Overlay: _Overlay_e__Union
    CancelRoutine: win32more.Windows.Wdk.Foundation.DRIVER_CANCEL
    UserBuffer: VoidPtr
    Tail: _Tail_e__Union
    _anonymous_ = ('Anonymous',)
    class _AssociatedIrp_e__Union(Union):
        MasterIrp: POINTER(win32more.Windows.Wdk.Foundation.IRP)
        IrpCount: Int32
        SystemBuffer: VoidPtr
    class _Anonymous_e__Union(Union):
        UserIosb: POINTER(win32more.Windows.Win32.System.IO.IO_STATUS_BLOCK)
        IoRingContext: VoidPtr
    class _Overlay_e__Union(Union):
        AsynchronousParameters: _AsynchronousParameters_e__Struct
        AllocationSize: Int64
        class _AsynchronousParameters_e__Struct(Structure):
            Anonymous1: _Anonymous1_e__Union
            Anonymous2: _Anonymous2_e__Union
            _anonymous_ = ('Anonymous1', 'Anonymous2')
            class _Anonymous1_e__Union(Union):
                UserApcRoutine: win32more.Windows.Win32.System.IO.PIO_APC_ROUTINE
                IssuingProcess: VoidPtr
            class _Anonymous2_e__Union(Union):
                UserApcContext: VoidPtr
                IoRing: POINTER(win32more.Windows.Wdk.Foundation._IORING_OBJECT)
    class _Tail_e__Union(Union):
        Overlay: _Overlay_e__Struct
        Apc: win32more.Windows.Wdk.System.SystemServices.KAPC
        CompletionKey: VoidPtr
        class _Overlay_e__Struct(Structure):
            Anonymous1: _Anonymous1_e__Union
            Thread: win32more.Windows.Wdk.Foundation.PETHREAD
            AuxiliaryBuffer: win32more.Windows.Win32.Foundation.PSTR
            Anonymous2: _Anonymous2_e__Struct
            OriginalFileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT)
            _anonymous_ = ('Anonymous1', 'Anonymous2')
            class _Anonymous1_e__Union(Union):
                DeviceQueueEntry: win32more.Windows.Wdk.System.SystemServices.KDEVICE_QUEUE_ENTRY
                Anonymous: _Anonymous_e__Struct
                _anonymous_ = ('Anonymous',)
                class _Anonymous_e__Struct(Structure):
                    DriverContext: VoidPtr * 4
            class _Anonymous2_e__Struct(Structure):
                ListEntry: win32more.Windows.Win32.System.Kernel.LIST_ENTRY
                Anonymous: _Anonymous_e__Union
                _anonymous_ = ('Anonymous',)
                class _Anonymous_e__Union(Union):
                    CurrentStackLocation: POINTER(win32more.Windows.Wdk.Foundation.IO_STACK_LOCATION)
                    PacketType: UInt32
class KDEVICE_QUEUE(Structure):
    Type: Int16
    Size: Int16
    DeviceListHead: win32more.Windows.Win32.System.Kernel.LIST_ENTRY
    Lock: UIntPtr
    Busy: win32more.Windows.Win32.Foundation.BOOLEAN
class KDPC(Structure):
    Anonymous: _Anonymous_e__Union
    DpcListEntry: win32more.Windows.Win32.System.Kernel.SINGLE_LIST_ENTRY
    ProcessorHistory: UIntPtr
    DeferredRoutine: win32more.Windows.Wdk.Foundation.PKDEFERRED_ROUTINE
    DeferredContext: VoidPtr
    SystemArgument1: VoidPtr
    SystemArgument2: VoidPtr
    DpcData: VoidPtr
    _anonymous_ = ('Anonymous',)
    class _Anonymous_e__Union(Union):
        TargetInfoAsUlong: UInt32
        Anonymous: _Anonymous_e__Struct
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            Type: Byte
            Importance: Byte
            Number: UInt16
KENLISTMENT = IntPtr
class KEVENT(Structure):
    Header: win32more.Windows.Wdk.Foundation.DISPATCHER_HEADER
KGDT = IntPtr
KIDT = IntPtr
class KMUTANT(Structure):
    Header: win32more.Windows.Wdk.Foundation.DISPATCHER_HEADER
    MutantListEntry: win32more.Windows.Win32.System.Kernel.LIST_ENTRY
    OwnerThread: POINTER(IntPtr)
    Anonymous: _Anonymous_e__Union
    ApcDisable: Byte
    _anonymous_ = ('Anonymous',)
    class _Anonymous_e__Union(Union):
        MutantFlags: Byte
        Anonymous: _Anonymous_e__Struct
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            Abandoned: Annotated[Byte, NativeBitfieldAttribute(1)]
            Spare1: Annotated[Byte, NativeBitfieldAttribute(7)]
KPCR = IntPtr
KPRCB = IntPtr
class KQUEUE(Structure):
    Header: win32more.Windows.Wdk.Foundation.DISPATCHER_HEADER
    EntryListHead: win32more.Windows.Win32.System.Kernel.LIST_ENTRY
    CurrentCount: UInt32
    MaximumCount: UInt32
    ThreadListHead: win32more.Windows.Win32.System.Kernel.LIST_ENTRY
KRESOURCEMANAGER = IntPtr
KSPIN_LOCK_QUEUE_NUMBER = Int32
LockQueueUnusedSpare0: win32more.Windows.Wdk.Foundation.KSPIN_LOCK_QUEUE_NUMBER = 0
LockQueueUnusedSpare1: win32more.Windows.Wdk.Foundation.KSPIN_LOCK_QUEUE_NUMBER = 1
LockQueueUnusedSpare2: win32more.Windows.Wdk.Foundation.KSPIN_LOCK_QUEUE_NUMBER = 2
LockQueueUnusedSpare3: win32more.Windows.Wdk.Foundation.KSPIN_LOCK_QUEUE_NUMBER = 3
LockQueueVacbLock: win32more.Windows.Wdk.Foundation.KSPIN_LOCK_QUEUE_NUMBER = 4
LockQueueMasterLock: win32more.Windows.Wdk.Foundation.KSPIN_LOCK_QUEUE_NUMBER = 5
LockQueueNonPagedPoolLock: win32more.Windows.Wdk.Foundation.KSPIN_LOCK_QUEUE_NUMBER = 6
LockQueueIoCancelLock: win32more.Windows.Wdk.Foundation.KSPIN_LOCK_QUEUE_NUMBER = 7
LockQueueUnusedSpare8: win32more.Windows.Wdk.Foundation.KSPIN_LOCK_QUEUE_NUMBER = 8
LockQueueIoVpbLock: win32more.Windows.Wdk.Foundation.KSPIN_LOCK_QUEUE_NUMBER = 9
LockQueueIoDatabaseLock: win32more.Windows.Wdk.Foundation.KSPIN_LOCK_QUEUE_NUMBER = 10
LockQueueIoCompletionLock: win32more.Windows.Wdk.Foundation.KSPIN_LOCK_QUEUE_NUMBER = 11
LockQueueNtfsStructLock: win32more.Windows.Wdk.Foundation.KSPIN_LOCK_QUEUE_NUMBER = 12
LockQueueAfdWorkQueueLock: win32more.Windows.Wdk.Foundation.KSPIN_LOCK_QUEUE_NUMBER = 13
LockQueueBcbLock: win32more.Windows.Wdk.Foundation.KSPIN_LOCK_QUEUE_NUMBER = 14
LockQueueUnusedSpare15: win32more.Windows.Wdk.Foundation.KSPIN_LOCK_QUEUE_NUMBER = 15
LockQueueUnusedSpare16: win32more.Windows.Wdk.Foundation.KSPIN_LOCK_QUEUE_NUMBER = 16
LockQueueMaximumLock: win32more.Windows.Wdk.Foundation.KSPIN_LOCK_QUEUE_NUMBER = 17
KTM = IntPtr
KTRANSACTION = IntPtr
KTSS = IntPtr
class KWAIT_BLOCK(Structure):
    WaitListEntry: win32more.Windows.Win32.System.Kernel.LIST_ENTRY
    WaitType: Byte
    BlockState: Byte
    WaitKey: UInt16
    Anonymous: _Anonymous_e__Union
    Object: VoidPtr
    SparePtr: VoidPtr
    _anonymous_ = ('Anonymous',)
    class _Anonymous_e__Union(Union):
        Thread: POINTER(IntPtr)
        NotificationQueue: POINTER(win32more.Windows.Wdk.Foundation.KQUEUE)
        Dpc: POINTER(win32more.Windows.Wdk.Foundation.KDPC)
LOADER_PARAMETER_BLOCK = IntPtr
class MDL(Structure):
    Next: POINTER(win32more.Windows.Wdk.Foundation.MDL)
    Size: Int16
    MdlFlags: Int16
    Process: POINTER(IntPtr)
    MappedSystemVa: VoidPtr
    StartVa: VoidPtr
    ByteCount: UInt32
    ByteOffset: UInt32
class OBJECT_ATTRIBUTES(Structure):
    Length: UInt32
    RootDirectory: win32more.Windows.Win32.Foundation.HANDLE
    ObjectName: POINTER(win32more.Windows.Win32.Foundation.UNICODE_STRING)
    Attributes: win32more.Windows.Win32.Foundation.OBJECT_ATTRIBUTE_FLAGS
    SecurityDescriptor: POINTER(win32more.Windows.Win32.Security.SECURITY_DESCRIPTOR)
    SecurityQualityOfService: POINTER(win32more.Windows.Win32.Security.SECURITY_QUALITY_OF_SERVICE)
class OBJECT_ATTRIBUTES32(Structure):
    Length: UInt32
    RootDirectory: UInt32
    ObjectName: UInt32
    Attributes: win32more.Windows.Win32.Foundation.OBJECT_ATTRIBUTE_FLAGS
    SecurityDescriptor: POINTER(win32more.Windows.Win32.Security.SECURITY_DESCRIPTOR)
    SecurityQualityOfService: POINTER(win32more.Windows.Win32.Security.SECURITY_QUALITY_OF_SERVICE)
class OBJECT_ATTRIBUTES64(Structure):
    Length: UInt32
    RootDirectory: UInt64
    ObjectName: UInt64
    Attributes: win32more.Windows.Win32.Foundation.OBJECT_ATTRIBUTE_FLAGS
    SecurityDescriptor: POINTER(win32more.Windows.Win32.Security.SECURITY_DESCRIPTOR)
    SecurityQualityOfService: POINTER(win32more.Windows.Win32.Security.SECURITY_QUALITY_OF_SERVICE)
OBJECT_INFORMATION_CLASS = Int32
ObjectBasicInformation: win32more.Windows.Wdk.Foundation.OBJECT_INFORMATION_CLASS = 0
ObjectTypeInformation: win32more.Windows.Wdk.Foundation.OBJECT_INFORMATION_CLASS = 2
class OBJECT_NAME_INFORMATION(Structure):
    Name: win32more.Windows.Win32.Foundation.UNICODE_STRING
class OWNER_ENTRY(Structure):
    OwnerThread: UIntPtr
    Anonymous: _Anonymous_e__Union
    _anonymous_ = ('Anonymous',)
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        TableSize: UInt32
        _anonymous_ = ('Anonymous',)
        class _Anonymous_e__Struct(Structure):
            IoPriorityBoosted: Annotated[UInt32, NativeBitfieldAttribute(1)]
            OwnerReferenced: Annotated[UInt32, NativeBitfieldAttribute(1)]
            IoQoSPriorityBoosted: Annotated[UInt32, NativeBitfieldAttribute(1)]
            OwnerCount: Annotated[UInt32, NativeBitfieldAttribute(29)]
PAFFINITY_TOKEN = IntPtr
PBUS_HANDLER = IntPtr
PCALLBACK_OBJECT = IntPtr
PDEVICE_HANDLER_OBJECT = IntPtr
PEJOB = IntPtr
PEPROCESS = IntPtr
PESILO = IntPtr
PETHREAD = IntPtr
PEX_RUNDOWN_REF_CACHE_AWARE = IntPtr
PEX_TIMER = IntPtr
@winfunctype_pointer
def PFREE_FUNCTION() -> Void: ...
@winfunctype_pointer
def PIO_COMPLETION_ROUTINE() -> win32more.Windows.Win32.Foundation.NTSTATUS: ...
PIO_REMOVE_LOCK_TRACKING_BLOCK = IntPtr
PIO_TIMER = IntPtr
PIO_WORKITEM = IntPtr
@winfunctype_pointer
def PKDEFERRED_ROUTINE() -> Void: ...
PKINTERRUPT = IntPtr
PKPROCESS = IntPtr
PKTHREAD = IntPtr
PNOTIFY_SYNC = IntPtr
POBJECT_TYPE = IntPtr
POHANDLE = VoidPtr
POOL_TYPE = Int32
NonPagedPool: win32more.Windows.Wdk.Foundation.POOL_TYPE = 0
NonPagedPoolExecute: win32more.Windows.Wdk.Foundation.POOL_TYPE = 0
PagedPool: win32more.Windows.Wdk.Foundation.POOL_TYPE = 1
NonPagedPoolMustSucceed: win32more.Windows.Wdk.Foundation.POOL_TYPE = 2
DontUseThisType: win32more.Windows.Wdk.Foundation.POOL_TYPE = 3
NonPagedPoolCacheAligned: win32more.Windows.Wdk.Foundation.POOL_TYPE = 4
PagedPoolCacheAligned: win32more.Windows.Wdk.Foundation.POOL_TYPE = 5
NonPagedPoolCacheAlignedMustS: win32more.Windows.Wdk.Foundation.POOL_TYPE = 6
MaxPoolType: win32more.Windows.Wdk.Foundation.POOL_TYPE = 7
NonPagedPoolBase: win32more.Windows.Wdk.Foundation.POOL_TYPE = 0
NonPagedPoolBaseMustSucceed: win32more.Windows.Wdk.Foundation.POOL_TYPE = 2
NonPagedPoolBaseCacheAligned: win32more.Windows.Wdk.Foundation.POOL_TYPE = 4
NonPagedPoolBaseCacheAlignedMustS: win32more.Windows.Wdk.Foundation.POOL_TYPE = 6
NonPagedPoolSession: win32more.Windows.Wdk.Foundation.POOL_TYPE = 32
PagedPoolSession: win32more.Windows.Wdk.Foundation.POOL_TYPE = 33
NonPagedPoolMustSucceedSession: win32more.Windows.Wdk.Foundation.POOL_TYPE = 34
DontUseThisTypeSession: win32more.Windows.Wdk.Foundation.POOL_TYPE = 35
NonPagedPoolCacheAlignedSession: win32more.Windows.Wdk.Foundation.POOL_TYPE = 36
PagedPoolCacheAlignedSession: win32more.Windows.Wdk.Foundation.POOL_TYPE = 37
NonPagedPoolCacheAlignedMustSSession: win32more.Windows.Wdk.Foundation.POOL_TYPE = 38
NonPagedPoolNx: win32more.Windows.Wdk.Foundation.POOL_TYPE = 512
NonPagedPoolNxCacheAligned: win32more.Windows.Wdk.Foundation.POOL_TYPE = 516
NonPagedPoolSessionNx: win32more.Windows.Wdk.Foundation.POOL_TYPE = 544
PPCW_BUFFER = IntPtr
PPCW_INSTANCE = IntPtr
PPCW_REGISTRATION = IntPtr
PRKPROCESS = IntPtr
PRKTHREAD = IntPtr
PSILO_MONITOR = IntPtr
@winfunctype_pointer
def PWORKER_THREAD_ROUTINE() -> Void: ...
class RTL_SPLAY_LINKS(Structure):
    Parent: POINTER(win32more.Windows.Wdk.Foundation.RTL_SPLAY_LINKS)
    LeftChild: POINTER(win32more.Windows.Wdk.Foundation.RTL_SPLAY_LINKS)
    RightChild: POINTER(win32more.Windows.Wdk.Foundation.RTL_SPLAY_LINKS)
class SECTION_OBJECT_POINTERS(Structure):
    DataSectionObject: VoidPtr
    SharedCacheMap: VoidPtr
    ImageSectionObject: VoidPtr
class SECURITY_SUBJECT_CONTEXT(Structure):
    ClientToken: VoidPtr
    ImpersonationLevel: win32more.Windows.Win32.Security.SECURITY_IMPERSONATION_LEVEL
    PrimaryToken: VoidPtr
    ProcessAuditId: VoidPtr
SspiAsyncContext = IntPtr
class TARGET_DEVICE_CUSTOM_NOTIFICATION(Structure):
    Version: UInt16
    Size: UInt16
    Event: Guid
    FileObject: POINTER(win32more.Windows.Wdk.Foundation.FILE_OBJECT)
    NameBufferOffset: Int32
    CustomDataBuffer: FlexibleArray[Byte]
class VPB(Structure):
    Type: Int16
    Size: Int16
    Flags: UInt16
    VolumeLabelLength: UInt16
    DeviceObject: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)
    RealDevice: POINTER(win32more.Windows.Wdk.Foundation.DEVICE_OBJECT)
    SerialNumber: UInt32
    ReferenceCount: UInt32
    VolumeLabel: Char * 32
class WORK_QUEUE_ITEM(Structure):
    List: win32more.Windows.Win32.System.Kernel.LIST_ENTRY
    WorkerRoutine: win32more.Windows.Wdk.Foundation.PWORKER_THREAD_ROUTINE
    Parameter: VoidPtr
_DEVICE_OBJECT_POWER_EXTENSION = IntPtr
_IORING_OBJECT = IntPtr
_SCSI_REQUEST_BLOCK = IntPtr


make_ready(__name__)
