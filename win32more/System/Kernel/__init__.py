from win32more.base import *
import win32more.Foundation
import win32more.System.Diagnostics.Debug
import win32more.System.Kernel

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
OBJ_HANDLE_TAGBITS = 3
RTL_BALANCED_NODE_RESERVED_PARENT_MASK = 3
OBJ_INHERIT = 2
OBJ_PERMANENT = 16
OBJ_EXCLUSIVE = 32
OBJ_CASE_INSENSITIVE = 64
OBJ_OPENIF = 128
OBJ_OPENLINK = 256
OBJ_KERNEL_HANDLE = 512
OBJ_FORCE_ACCESS_CHECK = 1024
OBJ_IGNORE_IMPERSONATED_DEVICEMAP = 2048
OBJ_DONT_REPARSE = 4096
OBJ_VALID_ATTRIBUTES = 8178
NULL64 = 0
MAXUCHAR = 255
MAXUSHORT = 65535
MAXULONG = 4294967295
EXCEPTION_DISPOSITION = Int32
EXCEPTION_DISPOSITION_ExceptionContinueExecution = 0
EXCEPTION_DISPOSITION_ExceptionContinueSearch = 1
EXCEPTION_DISPOSITION_ExceptionNestedException = 2
EXCEPTION_DISPOSITION_ExceptionCollidedUnwind = 3
def _define_SLIST_ENTRY_head():
    class SLIST_ENTRY(Structure):
        pass
    return SLIST_ENTRY
def _define_SLIST_ENTRY():
    SLIST_ENTRY = win32more.System.Kernel.SLIST_ENTRY_head
    SLIST_ENTRY._fields_ = [
        ("Next", POINTER(win32more.System.Kernel.SLIST_ENTRY_head)),
    ]
    return SLIST_ENTRY
def _define_QUAD_head():
    class QUAD(Structure):
        pass
    return QUAD
def _define_QUAD():
    QUAD = win32more.System.Kernel.QUAD_head
    class QUAD__Anonymous_e__Union(Union):
        pass
    QUAD__Anonymous_e__Union._fields_ = [
        ("UseThisFieldToCopy", Int64),
        ("DoNotUseThisField", Double),
    ]
    QUAD._anonymous_ = [
        'Anonymous',
    ]
    QUAD._fields_ = [
        ("Anonymous", QUAD__Anonymous_e__Union),
    ]
    return QUAD
def _define_PROCESSOR_NUMBER_head():
    class PROCESSOR_NUMBER(Structure):
        pass
    return PROCESSOR_NUMBER
def _define_PROCESSOR_NUMBER():
    PROCESSOR_NUMBER = win32more.System.Kernel.PROCESSOR_NUMBER_head
    PROCESSOR_NUMBER._fields_ = [
        ("Group", UInt16),
        ("Number", Byte),
        ("Reserved", Byte),
    ]
    return PROCESSOR_NUMBER
EVENT_TYPE = Int32
EVENT_TYPE_NotificationEvent = 0
EVENT_TYPE_SynchronizationEvent = 1
TIMER_TYPE = Int32
TIMER_TYPE_NotificationTimer = 0
TIMER_TYPE_SynchronizationTimer = 1
WAIT_TYPE = Int32
WAIT_TYPE_WaitAll = 0
WAIT_TYPE_WaitAny = 1
WAIT_TYPE_WaitNotification = 2
WAIT_TYPE_WaitDequeue = 3
WAIT_TYPE_WaitDpc = 4
def _define_STRING_head():
    class STRING(Structure):
        pass
    return STRING
def _define_STRING():
    STRING = win32more.System.Kernel.STRING_head
    STRING._fields_ = [
        ("Length", UInt16),
        ("MaximumLength", UInt16),
        ("Buffer", win32more.Foundation.PSTR),
    ]
    return STRING
def _define_CSTRING_head():
    class CSTRING(Structure):
        pass
    return CSTRING
def _define_CSTRING():
    CSTRING = win32more.System.Kernel.CSTRING_head
    CSTRING._fields_ = [
        ("Length", UInt16),
        ("MaximumLength", UInt16),
        ("Buffer", win32more.Foundation.PSTR),
    ]
    return CSTRING
def _define_LIST_ENTRY_head():
    class LIST_ENTRY(Structure):
        pass
    return LIST_ENTRY
def _define_LIST_ENTRY():
    LIST_ENTRY = win32more.System.Kernel.LIST_ENTRY_head
    LIST_ENTRY._fields_ = [
        ("Flink", POINTER(win32more.System.Kernel.LIST_ENTRY_head)),
        ("Blink", POINTER(win32more.System.Kernel.LIST_ENTRY_head)),
    ]
    return LIST_ENTRY
def _define_SINGLE_LIST_ENTRY_head():
    class SINGLE_LIST_ENTRY(Structure):
        pass
    return SINGLE_LIST_ENTRY
def _define_SINGLE_LIST_ENTRY():
    SINGLE_LIST_ENTRY = win32more.System.Kernel.SINGLE_LIST_ENTRY_head
    SINGLE_LIST_ENTRY._fields_ = [
        ("Next", POINTER(win32more.System.Kernel.SINGLE_LIST_ENTRY_head)),
    ]
    return SINGLE_LIST_ENTRY
def _define_RTL_BALANCED_NODE_head():
    class RTL_BALANCED_NODE(Structure):
        pass
    return RTL_BALANCED_NODE
def _define_RTL_BALANCED_NODE():
    RTL_BALANCED_NODE = win32more.System.Kernel.RTL_BALANCED_NODE_head
    class RTL_BALANCED_NODE__Anonymous2_e__Union(Union):
        pass
    RTL_BALANCED_NODE__Anonymous2_e__Union._fields_ = [
        ("_bitfield", Byte),
        ("ParentValue", UIntPtr),
    ]
    class RTL_BALANCED_NODE__Anonymous1_e__Union(Union):
        pass
    class RTL_BALANCED_NODE__Anonymous1_e__Union__Anonymous_e__Struct(Structure):
        pass
    RTL_BALANCED_NODE__Anonymous1_e__Union__Anonymous_e__Struct._fields_ = [
        ("Left", POINTER(win32more.System.Kernel.RTL_BALANCED_NODE_head)),
        ("Right", POINTER(win32more.System.Kernel.RTL_BALANCED_NODE_head)),
    ]
    RTL_BALANCED_NODE__Anonymous1_e__Union._anonymous_ = [
        'Anonymous',
    ]
    RTL_BALANCED_NODE__Anonymous1_e__Union._fields_ = [
        ("Children", POINTER(win32more.System.Kernel.RTL_BALANCED_NODE_head) * 2),
        ("Anonymous", RTL_BALANCED_NODE__Anonymous1_e__Union__Anonymous_e__Struct),
    ]
    RTL_BALANCED_NODE._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    RTL_BALANCED_NODE._fields_ = [
        ("Anonymous1", RTL_BALANCED_NODE__Anonymous1_e__Union),
        ("Anonymous2", RTL_BALANCED_NODE__Anonymous2_e__Union),
    ]
    return RTL_BALANCED_NODE
def _define_LIST_ENTRY32_head():
    class LIST_ENTRY32(Structure):
        pass
    return LIST_ENTRY32
def _define_LIST_ENTRY32():
    LIST_ENTRY32 = win32more.System.Kernel.LIST_ENTRY32_head
    LIST_ENTRY32._fields_ = [
        ("Flink", UInt32),
        ("Blink", UInt32),
    ]
    return LIST_ENTRY32
def _define_LIST_ENTRY64_head():
    class LIST_ENTRY64(Structure):
        pass
    return LIST_ENTRY64
def _define_LIST_ENTRY64():
    LIST_ENTRY64 = win32more.System.Kernel.LIST_ENTRY64_head
    LIST_ENTRY64._fields_ = [
        ("Flink", UInt64),
        ("Blink", UInt64),
    ]
    return LIST_ENTRY64
def _define_SINGLE_LIST_ENTRY32_head():
    class SINGLE_LIST_ENTRY32(Structure):
        pass
    return SINGLE_LIST_ENTRY32
def _define_SINGLE_LIST_ENTRY32():
    SINGLE_LIST_ENTRY32 = win32more.System.Kernel.SINGLE_LIST_ENTRY32_head
    SINGLE_LIST_ENTRY32._fields_ = [
        ("Next", UInt32),
    ]
    return SINGLE_LIST_ENTRY32
def _define_WNF_STATE_NAME_head():
    class WNF_STATE_NAME(Structure):
        pass
    return WNF_STATE_NAME
def _define_WNF_STATE_NAME():
    WNF_STATE_NAME = win32more.System.Kernel.WNF_STATE_NAME_head
    WNF_STATE_NAME._fields_ = [
        ("Data", UInt32 * 2),
    ]
    return WNF_STATE_NAME
def _define_STRING32_head():
    class STRING32(Structure):
        pass
    return STRING32
def _define_STRING32():
    STRING32 = win32more.System.Kernel.STRING32_head
    STRING32._fields_ = [
        ("Length", UInt16),
        ("MaximumLength", UInt16),
        ("Buffer", UInt32),
    ]
    return STRING32
def _define_STRING64_head():
    class STRING64(Structure):
        pass
    return STRING64
def _define_STRING64():
    STRING64 = win32more.System.Kernel.STRING64_head
    STRING64._fields_ = [
        ("Length", UInt16),
        ("MaximumLength", UInt16),
        ("Buffer", UInt64),
    ]
    return STRING64
def _define_OBJECT_ATTRIBUTES64_head():
    class OBJECT_ATTRIBUTES64(Structure):
        pass
    return OBJECT_ATTRIBUTES64
def _define_OBJECT_ATTRIBUTES64():
    OBJECT_ATTRIBUTES64 = win32more.System.Kernel.OBJECT_ATTRIBUTES64_head
    OBJECT_ATTRIBUTES64._fields_ = [
        ("Length", UInt32),
        ("RootDirectory", UInt64),
        ("ObjectName", UInt64),
        ("Attributes", UInt32),
        ("SecurityDescriptor", UInt64),
        ("SecurityQualityOfService", UInt64),
    ]
    return OBJECT_ATTRIBUTES64
def _define_OBJECT_ATTRIBUTES32_head():
    class OBJECT_ATTRIBUTES32(Structure):
        pass
    return OBJECT_ATTRIBUTES32
def _define_OBJECT_ATTRIBUTES32():
    OBJECT_ATTRIBUTES32 = win32more.System.Kernel.OBJECT_ATTRIBUTES32_head
    OBJECT_ATTRIBUTES32._fields_ = [
        ("Length", UInt32),
        ("RootDirectory", UInt32),
        ("ObjectName", UInt32),
        ("Attributes", UInt32),
        ("SecurityDescriptor", UInt32),
        ("SecurityQualityOfService", UInt32),
    ]
    return OBJECT_ATTRIBUTES32
def _define_OBJECTID_head():
    class OBJECTID(Structure):
        pass
    return OBJECTID
def _define_OBJECTID():
    OBJECTID = win32more.System.Kernel.OBJECTID_head
    OBJECTID._fields_ = [
        ("Lineage", Guid),
        ("Uniquifier", UInt32),
    ]
    return OBJECTID
def _define_EXCEPTION_ROUTINE():
    return CFUNCTYPE(win32more.System.Kernel.EXCEPTION_DISPOSITION,POINTER(win32more.System.Diagnostics.Debug.EXCEPTION_RECORD_head),c_void_p,POINTER(win32more.System.Diagnostics.Debug.CONTEXT_head),c_void_p, use_last_error=False)
NT_PRODUCT_TYPE = Int32
NT_PRODUCT_TYPE_NtProductWinNt = 1
NT_PRODUCT_TYPE_NtProductLanManNt = 2
NT_PRODUCT_TYPE_NtProductServer = 3
SUITE_TYPE = Int32
SUITE_TYPE_SmallBusiness = 0
SUITE_TYPE_Enterprise = 1
SUITE_TYPE_BackOffice = 2
SUITE_TYPE_CommunicationServer = 3
SUITE_TYPE_TerminalServer = 4
SUITE_TYPE_SmallBusinessRestricted = 5
SUITE_TYPE_EmbeddedNT = 6
SUITE_TYPE_DataCenter = 7
SUITE_TYPE_SingleUserTS = 8
SUITE_TYPE_Personal = 9
SUITE_TYPE_Blade = 10
SUITE_TYPE_EmbeddedRestricted = 11
SUITE_TYPE_SecurityAppliance = 12
SUITE_TYPE_StorageServer = 13
SUITE_TYPE_ComputeServer = 14
SUITE_TYPE_WHServer = 15
SUITE_TYPE_PhoneNT = 16
SUITE_TYPE_MultiUserTS = 17
SUITE_TYPE_MaxSuiteType = 18
COMPARTMENT_ID = Int32
UNSPECIFIED_COMPARTMENT_ID = 0
DEFAULT_COMPARTMENT_ID = 1
def _define_EXCEPTION_REGISTRATION_RECORD_head():
    class EXCEPTION_REGISTRATION_RECORD(Structure):
        pass
    return EXCEPTION_REGISTRATION_RECORD
def _define_EXCEPTION_REGISTRATION_RECORD():
    EXCEPTION_REGISTRATION_RECORD = win32more.System.Kernel.EXCEPTION_REGISTRATION_RECORD_head
    EXCEPTION_REGISTRATION_RECORD._fields_ = [
        ("Next", POINTER(win32more.System.Kernel.EXCEPTION_REGISTRATION_RECORD_head)),
        ("Handler", win32more.System.Kernel.EXCEPTION_ROUTINE),
    ]
    return EXCEPTION_REGISTRATION_RECORD
def _define_NT_TIB_head():
    class NT_TIB(Structure):
        pass
    return NT_TIB
def _define_NT_TIB():
    NT_TIB = win32more.System.Kernel.NT_TIB_head
    class NT_TIB__Anonymous_e__Union(Union):
        pass
    NT_TIB__Anonymous_e__Union._fields_ = [
        ("FiberData", c_void_p),
        ("Version", UInt32),
    ]
    NT_TIB._anonymous_ = [
        'Anonymous',
    ]
    NT_TIB._fields_ = [
        ("ExceptionList", POINTER(win32more.System.Kernel.EXCEPTION_REGISTRATION_RECORD_head)),
        ("StackBase", c_void_p),
        ("StackLimit", c_void_p),
        ("SubSystemTib", c_void_p),
        ("Anonymous", NT_TIB__Anonymous_e__Union),
        ("ArbitraryUserPointer", c_void_p),
        ("Self", POINTER(win32more.System.Kernel.NT_TIB_head)),
    ]
    return NT_TIB
def _define_SLIST_HEADER_head():
    class SLIST_HEADER(Union):
        pass
    return SLIST_HEADER
def _define_SLIST_HEADER():
    SLIST_HEADER = win32more.System.Kernel.SLIST_HEADER_head
    class SLIST_HEADER__Anonymous_e__Struct(Structure):
        pass
    SLIST_HEADER__Anonymous_e__Struct._fields_ = [
        ("Alignment", UInt64),
        ("Region", UInt64),
    ]
    class SLIST_HEADER__HeaderX64_e__Struct(Structure):
        pass
    SLIST_HEADER__HeaderX64_e__Struct._fields_ = [
        ("_bitfield1", UInt64),
        ("_bitfield2", UInt64),
    ]
    SLIST_HEADER._anonymous_ = [
        'Anonymous',
    ]
    SLIST_HEADER._fields_ = [
        ("Anonymous", SLIST_HEADER__Anonymous_e__Struct),
        ("HeaderX64", SLIST_HEADER__HeaderX64_e__Struct),
    ]
    return SLIST_HEADER
def _define_FLOATING_SAVE_AREA_head():
    class FLOATING_SAVE_AREA(Structure):
        pass
    return FLOATING_SAVE_AREA
def _define_FLOATING_SAVE_AREA():
    FLOATING_SAVE_AREA = win32more.System.Kernel.FLOATING_SAVE_AREA_head
    FLOATING_SAVE_AREA._fields_ = [
        ("ControlWord", UInt32),
        ("StatusWord", UInt32),
        ("TagWord", UInt32),
        ("ErrorOffset", UInt32),
        ("ErrorSelector", UInt32),
        ("DataOffset", UInt32),
        ("DataSelector", UInt32),
        ("RegisterArea", Byte * 80),
        ("Cr0NpxState", UInt32),
    ]
    return FLOATING_SAVE_AREA
def _define_RtlInitializeSListHead():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Kernel.SLIST_HEADER_head), use_last_error=False)(("RtlInitializeSListHead", windll["ntdll"]), ((1, 'ListHead'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlFirstEntrySList():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.Kernel.SLIST_ENTRY_head),POINTER(win32more.System.Kernel.SLIST_HEADER_head), use_last_error=False)(("RtlFirstEntrySList", windll["ntdll"]), ((1, 'ListHead'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlInterlockedPopEntrySList():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.Kernel.SLIST_ENTRY_head),POINTER(win32more.System.Kernel.SLIST_HEADER_head), use_last_error=False)(("RtlInterlockedPopEntrySList", windll["ntdll"]), ((1, 'ListHead'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlInterlockedPushEntrySList():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.Kernel.SLIST_ENTRY_head),POINTER(win32more.System.Kernel.SLIST_HEADER_head),POINTER(win32more.System.Kernel.SLIST_ENTRY_head), use_last_error=False)(("RtlInterlockedPushEntrySList", windll["ntdll"]), ((1, 'ListHead'),(1, 'ListEntry'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlInterlockedPushListSListEx():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.Kernel.SLIST_ENTRY_head),POINTER(win32more.System.Kernel.SLIST_HEADER_head),POINTER(win32more.System.Kernel.SLIST_ENTRY_head),POINTER(win32more.System.Kernel.SLIST_ENTRY_head),UInt32, use_last_error=False)(("RtlInterlockedPushListSListEx", windll["ntdll"]), ((1, 'ListHead'),(1, 'List'),(1, 'ListEnd'),(1, 'Count'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlInterlockedFlushSList():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.Kernel.SLIST_ENTRY_head),POINTER(win32more.System.Kernel.SLIST_HEADER_head), use_last_error=False)(("RtlInterlockedFlushSList", windll["ntdll"]), ((1, 'ListHead'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RtlQueryDepthSList():
    try:
        return WINFUNCTYPE(UInt16,POINTER(win32more.System.Kernel.SLIST_HEADER_head), use_last_error=False)(("RtlQueryDepthSList", windll["ntdll"]), ((1, 'ListHead'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "OBJ_HANDLE_TAGBITS",
    "RTL_BALANCED_NODE_RESERVED_PARENT_MASK",
    "OBJ_INHERIT",
    "OBJ_PERMANENT",
    "OBJ_EXCLUSIVE",
    "OBJ_CASE_INSENSITIVE",
    "OBJ_OPENIF",
    "OBJ_OPENLINK",
    "OBJ_KERNEL_HANDLE",
    "OBJ_FORCE_ACCESS_CHECK",
    "OBJ_IGNORE_IMPERSONATED_DEVICEMAP",
    "OBJ_DONT_REPARSE",
    "OBJ_VALID_ATTRIBUTES",
    "NULL64",
    "MAXUCHAR",
    "MAXUSHORT",
    "MAXULONG",
    "EXCEPTION_DISPOSITION",
    "EXCEPTION_DISPOSITION_ExceptionContinueExecution",
    "EXCEPTION_DISPOSITION_ExceptionContinueSearch",
    "EXCEPTION_DISPOSITION_ExceptionNestedException",
    "EXCEPTION_DISPOSITION_ExceptionCollidedUnwind",
    "SLIST_ENTRY",
    "QUAD",
    "PROCESSOR_NUMBER",
    "EVENT_TYPE",
    "EVENT_TYPE_NotificationEvent",
    "EVENT_TYPE_SynchronizationEvent",
    "TIMER_TYPE",
    "TIMER_TYPE_NotificationTimer",
    "TIMER_TYPE_SynchronizationTimer",
    "WAIT_TYPE",
    "WAIT_TYPE_WaitAll",
    "WAIT_TYPE_WaitAny",
    "WAIT_TYPE_WaitNotification",
    "WAIT_TYPE_WaitDequeue",
    "WAIT_TYPE_WaitDpc",
    "STRING",
    "CSTRING",
    "LIST_ENTRY",
    "SINGLE_LIST_ENTRY",
    "RTL_BALANCED_NODE",
    "LIST_ENTRY32",
    "LIST_ENTRY64",
    "SINGLE_LIST_ENTRY32",
    "WNF_STATE_NAME",
    "STRING32",
    "STRING64",
    "OBJECT_ATTRIBUTES64",
    "OBJECT_ATTRIBUTES32",
    "OBJECTID",
    "EXCEPTION_ROUTINE",
    "NT_PRODUCT_TYPE",
    "NT_PRODUCT_TYPE_NtProductWinNt",
    "NT_PRODUCT_TYPE_NtProductLanManNt",
    "NT_PRODUCT_TYPE_NtProductServer",
    "SUITE_TYPE",
    "SUITE_TYPE_SmallBusiness",
    "SUITE_TYPE_Enterprise",
    "SUITE_TYPE_BackOffice",
    "SUITE_TYPE_CommunicationServer",
    "SUITE_TYPE_TerminalServer",
    "SUITE_TYPE_SmallBusinessRestricted",
    "SUITE_TYPE_EmbeddedNT",
    "SUITE_TYPE_DataCenter",
    "SUITE_TYPE_SingleUserTS",
    "SUITE_TYPE_Personal",
    "SUITE_TYPE_Blade",
    "SUITE_TYPE_EmbeddedRestricted",
    "SUITE_TYPE_SecurityAppliance",
    "SUITE_TYPE_StorageServer",
    "SUITE_TYPE_ComputeServer",
    "SUITE_TYPE_WHServer",
    "SUITE_TYPE_PhoneNT",
    "SUITE_TYPE_MultiUserTS",
    "SUITE_TYPE_MaxSuiteType",
    "COMPARTMENT_ID",
    "UNSPECIFIED_COMPARTMENT_ID",
    "DEFAULT_COMPARTMENT_ID",
    "EXCEPTION_REGISTRATION_RECORD",
    "NT_TIB",
    "SLIST_HEADER",
    "FLOATING_SAVE_AREA",
    "RtlInitializeSListHead",
    "RtlFirstEntrySList",
    "RtlInterlockedPopEntrySList",
    "RtlInterlockedPushEntrySList",
    "RtlInterlockedPushListSListEx",
    "RtlInterlockedFlushSList",
    "RtlQueryDepthSList",
]
