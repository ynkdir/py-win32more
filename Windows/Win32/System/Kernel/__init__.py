from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.System.Diagnostics.Debug
import Windows.Win32.System.Kernel
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
OBJ_HANDLE_TAGBITS: Int32 = 3
RTL_BALANCED_NODE_RESERVED_PARENT_MASK: UInt32 = 3
OBJ_INHERIT: Int32 = 2
OBJ_PERMANENT: Int32 = 16
OBJ_EXCLUSIVE: Int32 = 32
OBJ_CASE_INSENSITIVE: Int32 = 64
OBJ_OPENIF: Int32 = 128
OBJ_OPENLINK: Int32 = 256
OBJ_KERNEL_HANDLE: Int32 = 512
OBJ_FORCE_ACCESS_CHECK: Int32 = 1024
OBJ_IGNORE_IMPERSONATED_DEVICEMAP: Int32 = 2048
OBJ_DONT_REPARSE: Int32 = 4096
OBJ_VALID_ATTRIBUTES: Int32 = 8178
NULL64: UInt32 = 0
MAXUCHAR: UInt32 = 255
MAXUSHORT: UInt32 = 65535
MAXULONG: UInt32 = 4294967295
@winfunctype('ntdll.dll')
def RtlInitializeSListHead(ListHead: POINTER(Windows.Win32.System.Kernel.SLIST_HEADER_head)) -> Void: ...
@winfunctype('ntdll.dll')
def RtlFirstEntrySList(ListHead: POINTER(Windows.Win32.System.Kernel.SLIST_HEADER_head)) -> POINTER(Windows.Win32.System.Kernel.SLIST_ENTRY_head): ...
@winfunctype('ntdll.dll')
def RtlInterlockedPopEntrySList(ListHead: POINTER(Windows.Win32.System.Kernel.SLIST_HEADER_head)) -> POINTER(Windows.Win32.System.Kernel.SLIST_ENTRY_head): ...
@winfunctype('ntdll.dll')
def RtlInterlockedPushEntrySList(ListHead: POINTER(Windows.Win32.System.Kernel.SLIST_HEADER_head), ListEntry: POINTER(Windows.Win32.System.Kernel.SLIST_ENTRY_head)) -> POINTER(Windows.Win32.System.Kernel.SLIST_ENTRY_head): ...
@winfunctype('ntdll.dll')
def RtlInterlockedPushListSListEx(ListHead: POINTER(Windows.Win32.System.Kernel.SLIST_HEADER_head), List: POINTER(Windows.Win32.System.Kernel.SLIST_ENTRY_head), ListEnd: POINTER(Windows.Win32.System.Kernel.SLIST_ENTRY_head), Count: UInt32) -> POINTER(Windows.Win32.System.Kernel.SLIST_ENTRY_head): ...
@winfunctype('ntdll.dll')
def RtlInterlockedFlushSList(ListHead: POINTER(Windows.Win32.System.Kernel.SLIST_HEADER_head)) -> POINTER(Windows.Win32.System.Kernel.SLIST_ENTRY_head): ...
@winfunctype('ntdll.dll')
def RtlQueryDepthSList(ListHead: POINTER(Windows.Win32.System.Kernel.SLIST_HEADER_head)) -> UInt16: ...
COMPARTMENT_ID = Int32
UNSPECIFIED_COMPARTMENT_ID: COMPARTMENT_ID = 0
DEFAULT_COMPARTMENT_ID: COMPARTMENT_ID = 1
class CSTRING(EasyCastStructure):
    Length: UInt16
    MaximumLength: UInt16
    Buffer: Windows.Win32.Foundation.PSTR
EVENT_TYPE = Int32
EVENT_TYPE_NotificationEvent: EVENT_TYPE = 0
EVENT_TYPE_SynchronizationEvent: EVENT_TYPE = 1
EXCEPTION_DISPOSITION = Int32
EXCEPTION_DISPOSITION_ExceptionContinueExecution: EXCEPTION_DISPOSITION = 0
EXCEPTION_DISPOSITION_ExceptionContinueSearch: EXCEPTION_DISPOSITION = 1
EXCEPTION_DISPOSITION_ExceptionNestedException: EXCEPTION_DISPOSITION = 2
EXCEPTION_DISPOSITION_ExceptionCollidedUnwind: EXCEPTION_DISPOSITION = 3
class EXCEPTION_REGISTRATION_RECORD(EasyCastStructure):
    Next: POINTER(Windows.Win32.System.Kernel.EXCEPTION_REGISTRATION_RECORD_head)
    Handler: Windows.Win32.System.Kernel.EXCEPTION_ROUTINE
@winfunctype_pointer
def EXCEPTION_ROUTINE(ExceptionRecord: POINTER(Windows.Win32.System.Diagnostics.Debug.EXCEPTION_RECORD_head), EstablisherFrame: c_void_p, ContextRecord: POINTER(Windows.Win32.System.Diagnostics.Debug.CONTEXT_head), DispatcherContext: c_void_p) -> Windows.Win32.System.Kernel.EXCEPTION_DISPOSITION: ...
if ARCH in 'X64,ARM64':
    class FLOATING_SAVE_AREA(EasyCastStructure):
        ControlWord: UInt32
        StatusWord: UInt32
        TagWord: UInt32
        ErrorOffset: UInt32
        ErrorSelector: UInt32
        DataOffset: UInt32
        DataSelector: UInt32
        RegisterArea: Byte * 80
        Cr0NpxState: UInt32
if ARCH in 'X86':
    class FLOATING_SAVE_AREA(EasyCastStructure):
        ControlWord: UInt32
        StatusWord: UInt32
        TagWord: UInt32
        ErrorOffset: UInt32
        ErrorSelector: UInt32
        DataOffset: UInt32
        DataSelector: UInt32
        RegisterArea: Byte * 80
        Spare0: UInt32
class LIST_ENTRY(EasyCastStructure):
    Flink: POINTER(Windows.Win32.System.Kernel.LIST_ENTRY_head)
    Blink: POINTER(Windows.Win32.System.Kernel.LIST_ENTRY_head)
class LIST_ENTRY32(EasyCastStructure):
    Flink: UInt32
    Blink: UInt32
class LIST_ENTRY64(EasyCastStructure):
    Flink: UInt64
    Blink: UInt64
NT_PRODUCT_TYPE = Int32
NT_PRODUCT_TYPE_NtProductWinNt: NT_PRODUCT_TYPE = 1
NT_PRODUCT_TYPE_NtProductLanManNt: NT_PRODUCT_TYPE = 2
NT_PRODUCT_TYPE_NtProductServer: NT_PRODUCT_TYPE = 3
class NT_TIB(EasyCastStructure):
    ExceptionList: POINTER(Windows.Win32.System.Kernel.EXCEPTION_REGISTRATION_RECORD_head)
    StackBase: c_void_p
    StackLimit: c_void_p
    SubSystemTib: c_void_p
    Anonymous: _Anonymous_e__Union
    ArbitraryUserPointer: c_void_p
    Self: POINTER(Windows.Win32.System.Kernel.NT_TIB_head)
    class _Anonymous_e__Union(EasyCastUnion):
        FiberData: c_void_p
        Version: UInt32
class OBJECTID(EasyCastStructure):
    Lineage: Guid
    Uniquifier: UInt32
class PROCESSOR_NUMBER(EasyCastStructure):
    Group: UInt16
    Number: Byte
    Reserved: Byte
class QUAD(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        UseThisFieldToCopy: Int64
        DoNotUseThisField: Double
class RTL_BALANCED_NODE(EasyCastStructure):
    Anonymous1: _Anonymous1_e__Union
    Anonymous2: _Anonymous2_e__Union
    class _Anonymous1_e__Union(EasyCastUnion):
        Children: POINTER(Windows.Win32.System.Kernel.RTL_BALANCED_NODE_head) * 2
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(EasyCastStructure):
            Left: POINTER(Windows.Win32.System.Kernel.RTL_BALANCED_NODE_head)
            Right: POINTER(Windows.Win32.System.Kernel.RTL_BALANCED_NODE_head)
    class _Anonymous2_e__Union(EasyCastUnion):
        _bitfield: Byte
        ParentValue: UIntPtr
class SINGLE_LIST_ENTRY(EasyCastStructure):
    Next: POINTER(Windows.Win32.System.Kernel.SINGLE_LIST_ENTRY_head)
class SINGLE_LIST_ENTRY32(EasyCastStructure):
    Next: UInt32
class SLIST_ENTRY(EasyCastStructure):
    Next: POINTER(Windows.Win32.System.Kernel.SLIST_ENTRY_head)
if ARCH in 'ARM64':
    class SLIST_HEADER(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        HeaderArm64: _HeaderArm64_e__Struct
        class _Anonymous_e__Struct(EasyCastStructure):
            Alignment: UInt64
            Region: UInt64
        class _HeaderArm64_e__Struct(EasyCastStructure):
            _bitfield1: UInt64
            _bitfield2: UInt64
if ARCH in 'X64':
    class SLIST_HEADER(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        HeaderX64: _HeaderX64_e__Struct
        class _Anonymous_e__Struct(EasyCastStructure):
            Alignment: UInt64
            Region: UInt64
        class _HeaderX64_e__Struct(EasyCastStructure):
            _bitfield1: UInt64
            _bitfield2: UInt64
if ARCH in 'X86':
    class SLIST_HEADER(EasyCastUnion):
        Alignment: UInt64
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(EasyCastStructure):
            Next: Windows.Win32.System.Kernel.SINGLE_LIST_ENTRY
            Depth: UInt16
            CpuId: UInt16
class STRING(EasyCastStructure):
    Length: UInt16
    MaximumLength: UInt16
    Buffer: Windows.Win32.Foundation.PSTR
class STRING32(EasyCastStructure):
    Length: UInt16
    MaximumLength: UInt16
    Buffer: UInt32
class STRING64(EasyCastStructure):
    Length: UInt16
    MaximumLength: UInt16
    Buffer: UInt64
SUITE_TYPE = Int32
SUITE_TYPE_SmallBusiness: SUITE_TYPE = 0
SUITE_TYPE_Enterprise: SUITE_TYPE = 1
SUITE_TYPE_BackOffice: SUITE_TYPE = 2
SUITE_TYPE_CommunicationServer: SUITE_TYPE = 3
SUITE_TYPE_TerminalServer: SUITE_TYPE = 4
SUITE_TYPE_SmallBusinessRestricted: SUITE_TYPE = 5
SUITE_TYPE_EmbeddedNT: SUITE_TYPE = 6
SUITE_TYPE_DataCenter: SUITE_TYPE = 7
SUITE_TYPE_SingleUserTS: SUITE_TYPE = 8
SUITE_TYPE_Personal: SUITE_TYPE = 9
SUITE_TYPE_Blade: SUITE_TYPE = 10
SUITE_TYPE_EmbeddedRestricted: SUITE_TYPE = 11
SUITE_TYPE_SecurityAppliance: SUITE_TYPE = 12
SUITE_TYPE_StorageServer: SUITE_TYPE = 13
SUITE_TYPE_ComputeServer: SUITE_TYPE = 14
SUITE_TYPE_WHServer: SUITE_TYPE = 15
SUITE_TYPE_PhoneNT: SUITE_TYPE = 16
SUITE_TYPE_MultiUserTS: SUITE_TYPE = 17
SUITE_TYPE_MaxSuiteType: SUITE_TYPE = 18
TIMER_TYPE = Int32
TIMER_TYPE_NotificationTimer: TIMER_TYPE = 0
TIMER_TYPE_SynchronizationTimer: TIMER_TYPE = 1
WAIT_TYPE = Int32
WAIT_TYPE_WaitAll: WAIT_TYPE = 0
WAIT_TYPE_WaitAny: WAIT_TYPE = 1
WAIT_TYPE_WaitNotification: WAIT_TYPE = 2
WAIT_TYPE_WaitDequeue: WAIT_TYPE = 3
WAIT_TYPE_WaitDpc: WAIT_TYPE = 4
class WNF_STATE_NAME(EasyCastStructure):
    Data: UInt32 * 2
make_head(_module, 'CSTRING')
make_head(_module, 'EXCEPTION_REGISTRATION_RECORD')
make_head(_module, 'EXCEPTION_ROUTINE')
if ARCH in 'X64,ARM64':
    make_head(_module, 'FLOATING_SAVE_AREA')
if ARCH in 'X86':
    make_head(_module, 'FLOATING_SAVE_AREA')
make_head(_module, 'LIST_ENTRY')
make_head(_module, 'LIST_ENTRY32')
make_head(_module, 'LIST_ENTRY64')
make_head(_module, 'NT_TIB')
make_head(_module, 'OBJECTID')
make_head(_module, 'PROCESSOR_NUMBER')
make_head(_module, 'QUAD')
make_head(_module, 'RTL_BALANCED_NODE')
make_head(_module, 'SINGLE_LIST_ENTRY')
make_head(_module, 'SINGLE_LIST_ENTRY32')
make_head(_module, 'SLIST_ENTRY')
if ARCH in 'ARM64':
    make_head(_module, 'SLIST_HEADER')
if ARCH in 'X64':
    make_head(_module, 'SLIST_HEADER')
if ARCH in 'X86':
    make_head(_module, 'SLIST_HEADER')
make_head(_module, 'STRING')
make_head(_module, 'STRING32')
make_head(_module, 'STRING64')
make_head(_module, 'WNF_STATE_NAME')
