from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.Diagnostics.Debug
import win32more.System.Kernel
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
def RtlInitializeSListHead(ListHead: POINTER(win32more.System.Kernel.SLIST_HEADER_head)) -> Void: ...
@winfunctype('ntdll.dll')
def RtlFirstEntrySList(ListHead: POINTER(win32more.System.Kernel.SLIST_HEADER_head)) -> POINTER(win32more.System.Kernel.SLIST_ENTRY_head): ...
@winfunctype('ntdll.dll')
def RtlInterlockedPopEntrySList(ListHead: POINTER(win32more.System.Kernel.SLIST_HEADER_head)) -> POINTER(win32more.System.Kernel.SLIST_ENTRY_head): ...
@winfunctype('ntdll.dll')
def RtlInterlockedPushEntrySList(ListHead: POINTER(win32more.System.Kernel.SLIST_HEADER_head), ListEntry: POINTER(win32more.System.Kernel.SLIST_ENTRY_head)) -> POINTER(win32more.System.Kernel.SLIST_ENTRY_head): ...
@winfunctype('ntdll.dll')
def RtlInterlockedPushListSListEx(ListHead: POINTER(win32more.System.Kernel.SLIST_HEADER_head), List: POINTER(win32more.System.Kernel.SLIST_ENTRY_head), ListEnd: POINTER(win32more.System.Kernel.SLIST_ENTRY_head), Count: UInt32) -> POINTER(win32more.System.Kernel.SLIST_ENTRY_head): ...
@winfunctype('ntdll.dll')
def RtlInterlockedFlushSList(ListHead: POINTER(win32more.System.Kernel.SLIST_HEADER_head)) -> POINTER(win32more.System.Kernel.SLIST_ENTRY_head): ...
@winfunctype('ntdll.dll')
def RtlQueryDepthSList(ListHead: POINTER(win32more.System.Kernel.SLIST_HEADER_head)) -> UInt16: ...
COMPARTMENT_ID = Int32
UNSPECIFIED_COMPARTMENT_ID: COMPARTMENT_ID = 0
DEFAULT_COMPARTMENT_ID: COMPARTMENT_ID = 1
class CSTRING(Structure):
    Length: UInt16
    MaximumLength: UInt16
    Buffer: win32more.Foundation.PSTR
EVENT_TYPE = Int32
EVENT_TYPE_NotificationEvent: EVENT_TYPE = 0
EVENT_TYPE_SynchronizationEvent: EVENT_TYPE = 1
EXCEPTION_DISPOSITION = Int32
EXCEPTION_DISPOSITION_ExceptionContinueExecution: EXCEPTION_DISPOSITION = 0
EXCEPTION_DISPOSITION_ExceptionContinueSearch: EXCEPTION_DISPOSITION = 1
EXCEPTION_DISPOSITION_ExceptionNestedException: EXCEPTION_DISPOSITION = 2
EXCEPTION_DISPOSITION_ExceptionCollidedUnwind: EXCEPTION_DISPOSITION = 3
class EXCEPTION_REGISTRATION_RECORD(Structure):
    Next: POINTER(win32more.System.Kernel.EXCEPTION_REGISTRATION_RECORD_head)
    Handler: win32more.System.Kernel.EXCEPTION_ROUTINE
@winfunctype_pointer
def EXCEPTION_ROUTINE(ExceptionRecord: POINTER(win32more.System.Diagnostics.Debug.EXCEPTION_RECORD_head), EstablisherFrame: c_void_p, ContextRecord: POINTER(win32more.System.Diagnostics.Debug.CONTEXT_head), DispatcherContext: c_void_p) -> win32more.System.Kernel.EXCEPTION_DISPOSITION: ...
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
if ARCH in 'X86':
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
    Flink: POINTER(win32more.System.Kernel.LIST_ENTRY_head)
    Blink: POINTER(win32more.System.Kernel.LIST_ENTRY_head)
class LIST_ENTRY32(Structure):
    Flink: UInt32
    Blink: UInt32
class LIST_ENTRY64(Structure):
    Flink: UInt64
    Blink: UInt64
NT_PRODUCT_TYPE = Int32
NT_PRODUCT_TYPE_NtProductWinNt: NT_PRODUCT_TYPE = 1
NT_PRODUCT_TYPE_NtProductLanManNt: NT_PRODUCT_TYPE = 2
NT_PRODUCT_TYPE_NtProductServer: NT_PRODUCT_TYPE = 3
class NT_TIB(Structure):
    ExceptionList: POINTER(win32more.System.Kernel.EXCEPTION_REGISTRATION_RECORD_head)
    StackBase: c_void_p
    StackLimit: c_void_p
    SubSystemTib: c_void_p
    Anonymous: _Anonymous_e__Union
    ArbitraryUserPointer: c_void_p
    Self: POINTER(win32more.System.Kernel.NT_TIB_head)
    class _Anonymous_e__Union(Union):
        FiberData: c_void_p
        Version: UInt32
class OBJECTID(Structure):
    Lineage: Guid
    Uniquifier: UInt32
class OBJECT_ATTRIBUTES32(Structure):
    Length: UInt32
    RootDirectory: UInt32
    ObjectName: UInt32
    Attributes: UInt32
    SecurityDescriptor: UInt32
    SecurityQualityOfService: UInt32
class OBJECT_ATTRIBUTES64(Structure):
    Length: UInt32
    RootDirectory: UInt64
    ObjectName: UInt64
    Attributes: UInt32
    SecurityDescriptor: UInt64
    SecurityQualityOfService: UInt64
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
        Children: POINTER(win32more.System.Kernel.RTL_BALANCED_NODE_head) * 2
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            Left: POINTER(win32more.System.Kernel.RTL_BALANCED_NODE_head)
            Right: POINTER(win32more.System.Kernel.RTL_BALANCED_NODE_head)
    class _Anonymous2_e__Union(Union):
        _bitfield: Byte
        ParentValue: UIntPtr
class SINGLE_LIST_ENTRY(Structure):
    Next: POINTER(win32more.System.Kernel.SINGLE_LIST_ENTRY_head)
class SINGLE_LIST_ENTRY32(Structure):
    Next: UInt32
class SLIST_ENTRY(Structure):
    Next: POINTER(win32more.System.Kernel.SLIST_ENTRY_head)
if ARCH in 'ARM64':
    class SLIST_HEADER(Union):
        Anonymous: _Anonymous_e__Struct
        HeaderArm64: _HeaderArm64_e__Struct
        class _Anonymous_e__Struct(Structure):
            Alignment: UInt64
            Region: UInt64
        class _HeaderArm64_e__Struct(Structure):
            _bitfield1: UInt64
            _bitfield2: UInt64
if ARCH in 'X64':
    class SLIST_HEADER(Union):
        Anonymous: _Anonymous_e__Struct
        HeaderX64: _HeaderX64_e__Struct
        class _Anonymous_e__Struct(Structure):
            Alignment: UInt64
            Region: UInt64
        class _HeaderX64_e__Struct(Structure):
            _bitfield1: UInt64
            _bitfield2: UInt64
if ARCH in 'X86':
    class SLIST_HEADER(Union):
        Alignment: UInt64
        Anonymous: _Anonymous_e__Struct
        class _Anonymous_e__Struct(Structure):
            Next: win32more.System.Kernel.SINGLE_LIST_ENTRY
            Depth: UInt16
            CpuId: UInt16
class STRING(Structure):
    Length: UInt16
    MaximumLength: UInt16
    Buffer: win32more.Foundation.PSTR
class STRING32(Structure):
    Length: UInt16
    MaximumLength: UInt16
    Buffer: UInt32
class STRING64(Structure):
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
class WNF_STATE_NAME(Structure):
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
make_head(_module, 'OBJECT_ATTRIBUTES32')
make_head(_module, 'OBJECT_ATTRIBUTES64')
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
__all__ = [
    "COMPARTMENT_ID",
    "CSTRING",
    "DEFAULT_COMPARTMENT_ID",
    "EVENT_TYPE",
    "EVENT_TYPE_NotificationEvent",
    "EVENT_TYPE_SynchronizationEvent",
    "EXCEPTION_DISPOSITION",
    "EXCEPTION_DISPOSITION_ExceptionCollidedUnwind",
    "EXCEPTION_DISPOSITION_ExceptionContinueExecution",
    "EXCEPTION_DISPOSITION_ExceptionContinueSearch",
    "EXCEPTION_DISPOSITION_ExceptionNestedException",
    "EXCEPTION_REGISTRATION_RECORD",
    "EXCEPTION_ROUTINE",
    "FLOATING_SAVE_AREA",
    "LIST_ENTRY",
    "LIST_ENTRY32",
    "LIST_ENTRY64",
    "MAXUCHAR",
    "MAXULONG",
    "MAXUSHORT",
    "NT_PRODUCT_TYPE",
    "NT_PRODUCT_TYPE_NtProductLanManNt",
    "NT_PRODUCT_TYPE_NtProductServer",
    "NT_PRODUCT_TYPE_NtProductWinNt",
    "NT_TIB",
    "NULL64",
    "OBJECTID",
    "OBJECT_ATTRIBUTES32",
    "OBJECT_ATTRIBUTES64",
    "OBJ_CASE_INSENSITIVE",
    "OBJ_DONT_REPARSE",
    "OBJ_EXCLUSIVE",
    "OBJ_FORCE_ACCESS_CHECK",
    "OBJ_HANDLE_TAGBITS",
    "OBJ_IGNORE_IMPERSONATED_DEVICEMAP",
    "OBJ_INHERIT",
    "OBJ_KERNEL_HANDLE",
    "OBJ_OPENIF",
    "OBJ_OPENLINK",
    "OBJ_PERMANENT",
    "OBJ_VALID_ATTRIBUTES",
    "PROCESSOR_NUMBER",
    "QUAD",
    "RTL_BALANCED_NODE",
    "RTL_BALANCED_NODE_RESERVED_PARENT_MASK",
    "RtlFirstEntrySList",
    "RtlInitializeSListHead",
    "RtlInterlockedFlushSList",
    "RtlInterlockedPopEntrySList",
    "RtlInterlockedPushEntrySList",
    "RtlInterlockedPushListSListEx",
    "RtlQueryDepthSList",
    "SINGLE_LIST_ENTRY",
    "SINGLE_LIST_ENTRY32",
    "SLIST_ENTRY",
    "SLIST_HEADER",
    "STRING",
    "STRING32",
    "STRING64",
    "SUITE_TYPE",
    "SUITE_TYPE_BackOffice",
    "SUITE_TYPE_Blade",
    "SUITE_TYPE_CommunicationServer",
    "SUITE_TYPE_ComputeServer",
    "SUITE_TYPE_DataCenter",
    "SUITE_TYPE_EmbeddedNT",
    "SUITE_TYPE_EmbeddedRestricted",
    "SUITE_TYPE_Enterprise",
    "SUITE_TYPE_MaxSuiteType",
    "SUITE_TYPE_MultiUserTS",
    "SUITE_TYPE_Personal",
    "SUITE_TYPE_PhoneNT",
    "SUITE_TYPE_SecurityAppliance",
    "SUITE_TYPE_SingleUserTS",
    "SUITE_TYPE_SmallBusiness",
    "SUITE_TYPE_SmallBusinessRestricted",
    "SUITE_TYPE_StorageServer",
    "SUITE_TYPE_TerminalServer",
    "SUITE_TYPE_WHServer",
    "TIMER_TYPE",
    "TIMER_TYPE_NotificationTimer",
    "TIMER_TYPE_SynchronizationTimer",
    "UNSPECIFIED_COMPARTMENT_ID",
    "WAIT_TYPE",
    "WAIT_TYPE_WaitAll",
    "WAIT_TYPE_WaitAny",
    "WAIT_TYPE_WaitDequeue",
    "WAIT_TYPE_WaitDpc",
    "WAIT_TYPE_WaitNotification",
    "WNF_STATE_NAME",
]
_arch_optional = [
]
