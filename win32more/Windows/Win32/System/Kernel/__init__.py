from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Diagnostics.Debug
import win32more.Windows.Win32.System.Kernel
OBJ_HANDLE_TAGBITS: Int32 = 3
RTL_BALANCED_NODE_RESERVED_PARENT_MASK: UInt32 = 3
NULL64: UInt32 = 0
MAXUCHAR: UInt32 = 255
MAXUSHORT: UInt32 = 65535
MAXULONG: UInt32 = 4294967295
@winfunctype('ntdll.dll')
def RtlInitializeSListHead(ListHead: POINTER(win32more.Windows.Win32.System.Kernel.SLIST_HEADER)) -> Void: ...
@winfunctype('ntdll.dll')
def RtlFirstEntrySList(ListHead: POINTER(win32more.Windows.Win32.System.Kernel.SLIST_HEADER)) -> POINTER(win32more.Windows.Win32.System.Kernel.SLIST_ENTRY): ...
@winfunctype('ntdll.dll')
def RtlInterlockedPopEntrySList(ListHead: POINTER(win32more.Windows.Win32.System.Kernel.SLIST_HEADER)) -> POINTER(win32more.Windows.Win32.System.Kernel.SLIST_ENTRY): ...
@winfunctype('ntdll.dll')
def RtlInterlockedPushEntrySList(ListHead: POINTER(win32more.Windows.Win32.System.Kernel.SLIST_HEADER), ListEntry: POINTER(win32more.Windows.Win32.System.Kernel.SLIST_ENTRY)) -> POINTER(win32more.Windows.Win32.System.Kernel.SLIST_ENTRY): ...
@winfunctype('ntdll.dll')
def RtlInterlockedPushListSListEx(ListHead: POINTER(win32more.Windows.Win32.System.Kernel.SLIST_HEADER), List: POINTER(win32more.Windows.Win32.System.Kernel.SLIST_ENTRY), ListEnd: POINTER(win32more.Windows.Win32.System.Kernel.SLIST_ENTRY), Count: UInt32) -> POINTER(win32more.Windows.Win32.System.Kernel.SLIST_ENTRY): ...
@winfunctype('ntdll.dll')
def RtlInterlockedFlushSList(ListHead: POINTER(win32more.Windows.Win32.System.Kernel.SLIST_HEADER)) -> POINTER(win32more.Windows.Win32.System.Kernel.SLIST_ENTRY): ...
@winfunctype('ntdll.dll')
def RtlQueryDepthSList(ListHead: POINTER(win32more.Windows.Win32.System.Kernel.SLIST_HEADER)) -> UInt16: ...
COMPARTMENT_ID = Int32
UNSPECIFIED_COMPARTMENT_ID: win32more.Windows.Win32.System.Kernel.COMPARTMENT_ID = 0
DEFAULT_COMPARTMENT_ID: win32more.Windows.Win32.System.Kernel.COMPARTMENT_ID = 1
class CSTRING(Structure):
    Length: UInt16
    MaximumLength: UInt16
    Buffer: win32more.Windows.Win32.Foundation.PSTR
EVENT_TYPE = Int32
NotificationEvent: win32more.Windows.Win32.System.Kernel.EVENT_TYPE = 0
SynchronizationEvent: win32more.Windows.Win32.System.Kernel.EVENT_TYPE = 1
EXCEPTION_DISPOSITION = Int32
ExceptionContinueExecution: win32more.Windows.Win32.System.Kernel.EXCEPTION_DISPOSITION = 0
ExceptionContinueSearch: win32more.Windows.Win32.System.Kernel.EXCEPTION_DISPOSITION = 1
ExceptionNestedException: win32more.Windows.Win32.System.Kernel.EXCEPTION_DISPOSITION = 2
ExceptionCollidedUnwind: win32more.Windows.Win32.System.Kernel.EXCEPTION_DISPOSITION = 3
class EXCEPTION_REGISTRATION_RECORD(Structure):
    Next: POINTER(win32more.Windows.Win32.System.Kernel.EXCEPTION_REGISTRATION_RECORD)
    Handler: win32more.Windows.Win32.System.Kernel.EXCEPTION_ROUTINE
@winfunctype_pointer
def EXCEPTION_ROUTINE(ExceptionRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.EXCEPTION_RECORD), EstablisherFrame: VoidPtr, ContextRecord: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.CONTEXT), DispatcherContext: VoidPtr) -> win32more.Windows.Win32.System.Kernel.EXCEPTION_DISPOSITION: ...
if ARCH in 'X64,ARM64':
    class FLOATING_SAVE_AREA(Structure):
        ControlWord: UInt32
        StatusWord: UInt32
        TagWord: UInt32
        ErrorOffset: UInt32
        ErrorSelector: UInt32
        DataOffset: UInt32
        DataSelector: UInt32
        RegisterArea: Byte * 80
        Cr0NpxState: UInt32
elif ARCH in 'X86':
    class FLOATING_SAVE_AREA(Structure):
        ControlWord: UInt32
        StatusWord: UInt32
        TagWord: UInt32
        ErrorOffset: UInt32
        ErrorSelector: UInt32
        DataOffset: UInt32
        DataSelector: UInt32
        RegisterArea: Byte * 80
        Spare0: UInt32
class LIST_ENTRY(Structure):
    Flink: POINTER(win32more.Windows.Win32.System.Kernel.LIST_ENTRY)
    Blink: POINTER(win32more.Windows.Win32.System.Kernel.LIST_ENTRY)
class LIST_ENTRY32(Structure):
    Flink: UInt32
    Blink: UInt32
class LIST_ENTRY64(Structure):
    Flink: UInt64
    Blink: UInt64
NT_PRODUCT_TYPE = Int32
NtProductWinNt: win32more.Windows.Win32.System.Kernel.NT_PRODUCT_TYPE = 1
NtProductLanManNt: win32more.Windows.Win32.System.Kernel.NT_PRODUCT_TYPE = 2
NtProductServer: win32more.Windows.Win32.System.Kernel.NT_PRODUCT_TYPE = 3
class NT_TIB(Structure):
    ExceptionList: POINTER(win32more.Windows.Win32.System.Kernel.EXCEPTION_REGISTRATION_RECORD)
    StackBase: VoidPtr
    StackLimit: VoidPtr
    SubSystemTib: VoidPtr
    Anonymous: _Anonymous_e__Union
    ArbitraryUserPointer: VoidPtr
    Self: POINTER(win32more.Windows.Win32.System.Kernel.NT_TIB)
    class _Anonymous_e__Union(Union):
        FiberData: VoidPtr
        Version: UInt32
class OBJECTID(Structure):
    Lineage: Guid
    Uniquifier: UInt32
class PROCESSOR_NUMBER(Structure):
    Group: UInt16
    Number: Byte
    Reserved: Byte
class QUAD(Structure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        UseThisFieldToCopy: Int64
        DoNotUseThisField: Double
class RTL_BALANCED_NODE(Structure):
    Anonymous1: _Anonymous1_e__Union
    Anonymous2: _Anonymous2_e__Union
    class _Anonymous1_e__Union(Union):
        Children: POINTER(win32more.Windows.Win32.System.Kernel.RTL_BALANCED_NODE) * 2
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            Left: POINTER(win32more.Windows.Win32.System.Kernel.RTL_BALANCED_NODE)
            Right: POINTER(win32more.Windows.Win32.System.Kernel.RTL_BALANCED_NODE)
    class _Anonymous2_e__Union(Union):
        Red: Annotated[Byte, 1]
        Balance: Annotated[Byte, 2]
        ParentValue: UIntPtr
class SINGLE_LIST_ENTRY(Structure):
    Next: POINTER(win32more.Windows.Win32.System.Kernel.SINGLE_LIST_ENTRY)
class SINGLE_LIST_ENTRY32(Structure):
    Next: UInt32
class SLIST_ENTRY(Structure):
    Next: POINTER(win32more.Windows.Win32.System.Kernel.SLIST_ENTRY)
if ARCH in 'ARM64':
    class SLIST_HEADER(Union):
        Anonymous: _Anonymous_e__Struct
        HeaderArm64: _HeaderArm64_e__Struct
        class _Anonymous_e__Struct(Structure):
            Alignment: UInt64
            Region: UInt64
        class _HeaderArm64_e__Struct(Structure):
            Depth: Annotated[UInt64, 16]
            Sequence: Annotated[UInt64, 48]
            Reserved: Annotated[UInt64, 4]
            NextEntry: Annotated[UInt64, 60]
elif ARCH in 'X64':
    class SLIST_HEADER(Union):
        Anonymous: _Anonymous_e__Struct
        HeaderX64: _HeaderX64_e__Struct
        class _Anonymous_e__Struct(Structure):
            Alignment: UInt64
            Region: UInt64
        class _HeaderX64_e__Struct(Structure):
            Depth: Annotated[UInt64, 16]
            Sequence: Annotated[UInt64, 48]
            Reserved: Annotated[UInt64, 4]
            NextEntry: Annotated[UInt64, 60]
elif ARCH in 'X86':
    class SLIST_HEADER(Union):
        Alignment: UInt64
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            Next: win32more.Windows.Win32.System.Kernel.SINGLE_LIST_ENTRY
            Depth: UInt16
            CpuId: UInt16
class STRING(Structure):
    Length: UInt16
    MaximumLength: UInt16
    Buffer: win32more.Windows.Win32.Foundation.PSTR
class STRING32(Structure):
    Length: UInt16
    MaximumLength: UInt16
    Buffer: UInt32
class STRING64(Structure):
    Length: UInt16
    MaximumLength: UInt16
    Buffer: UInt64
SUITE_TYPE = Int32
SmallBusiness: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 0
Enterprise: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 1
BackOffice: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 2
CommunicationServer: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 3
TerminalServer: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 4
SmallBusinessRestricted: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 5
EmbeddedNT: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 6
DataCenter: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 7
SingleUserTS: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 8
Personal: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 9
Blade: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 10
EmbeddedRestricted: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 11
SecurityAppliance: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 12
StorageServer: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 13
ComputeServer: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 14
WHServer: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 15
PhoneNT: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 16
MultiUserTS: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 17
MaxSuiteType: win32more.Windows.Win32.System.Kernel.SUITE_TYPE = 18
TIMER_TYPE = Int32
NotificationTimer: win32more.Windows.Win32.System.Kernel.TIMER_TYPE = 0
SynchronizationTimer: win32more.Windows.Win32.System.Kernel.TIMER_TYPE = 1
WAIT_TYPE = Int32
WaitAll: win32more.Windows.Win32.System.Kernel.WAIT_TYPE = 0
WaitAny: win32more.Windows.Win32.System.Kernel.WAIT_TYPE = 1
WaitNotification: win32more.Windows.Win32.System.Kernel.WAIT_TYPE = 2
WaitDequeue: win32more.Windows.Win32.System.Kernel.WAIT_TYPE = 3
WaitDpc: win32more.Windows.Win32.System.Kernel.WAIT_TYPE = 4
class WNF_STATE_NAME(Structure):
    Data: UInt32 * 2


make_ready(__name__)
