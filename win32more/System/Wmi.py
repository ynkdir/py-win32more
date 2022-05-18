from win32more import *
import win32more.Foundation
import win32more.System.Com
import win32more.System.Wmi

def __getattr__(name):
    module = globals()
    try:
        f = module[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    module[name] = f()
    return module[name]
def __dir__():
    return __all__
MI_FLAG_ANY = 127
MI_FLAG_VERSION = 469762048
MI_FLAG_ADOPT = 2147483648
MI_FLAG_CLASS = 1
MI_FLAG_METHOD = 2
MI_FLAG_PROPERTY = 4
MI_FLAG_PARAMETER = 8
MI_FLAG_ASSOCIATION = 16
MI_FLAG_INDICATION = 32
MI_FLAG_REFERENCE = 64
MI_FLAG_ENABLEOVERRIDE = 128
MI_FLAG_DISABLEOVERRIDE = 256
MI_FLAG_RESTRICTED = 512
MI_FLAG_TOSUBCLASS = 1024
MI_FLAG_TRANSLATABLE = 2048
MI_FLAG_KEY = 4096
MI_FLAG_IN = 8192
MI_FLAG_OUT = 16384
MI_FLAG_REQUIRED = 32768
MI_FLAG_STATIC = 65536
MI_FLAG_ABSTRACT = 131072
MI_FLAG_TERMINAL = 262144
MI_FLAG_EXPENSIVE = 524288
MI_FLAG_STREAM = 1048576
MI_FLAG_READONLY = 2097152
MI_FLAG_EXTENDED = 4096
MI_FLAG_NOT_MODIFIED = 33554432
MI_FLAG_NULL = 536870912
MI_FLAG_BORROW = 1073741824
MI_MODULE_FLAG_STANDARD_QUALIFIERS = 1
MI_MODULE_FLAG_DESCRIPTIONS = 2
MI_MODULE_FLAG_VALUES = 4
MI_MODULE_FLAG_MAPPING_STRINGS = 8
MI_MODULE_FLAG_BOOLEANS = 16
MI_MODULE_FLAG_CPLUSPLUS = 32
MI_MODULE_FLAG_LOCALIZED = 64
MI_MODULE_FLAG_FILTER_SUPPORT = 128
MI_MAX_LOCALE_SIZE = 128
MI_WRITEMESSAGE_CHANNEL_WARNING = 0
MI_WRITEMESSAGE_CHANNEL_VERBOSE = 1
MI_WRITEMESSAGE_CHANNEL_DEBUG = 2
MI_CALL_VERSION = 1
MI_OPERATIONFLAGS_MANUAL_ACK_RESULTS = 1
MI_OPERATIONFLAGS_NO_RTTI = 1024
MI_OPERATIONFLAGS_BASIC_RTTI = 2
MI_OPERATIONFLAGS_STANDARD_RTTI = 2048
MI_OPERATIONFLAGS_FULL_RTTI = 4
MI_OPERATIONFLAGS_DEFAULT_RTTI = 0
MI_OPERATIONFLAGS_LOCALIZED_QUALIFIERS = 8
MI_OPERATIONFLAGS_EXPENSIVE_PROPERTIES = 64
MI_OPERATIONFLAGS_POLYMORPHISM_SHALLOW = 128
MI_OPERATIONFLAGS_POLYMORPHISM_DEEP_BASE_PROPS_ONLY = 384
MI_OPERATIONFLAGS_REPORT_OPERATION_STARTED = 512
MI_SERIALIZER_FLAGS_CLASS_DEEP = 1
MI_SERIALIZER_FLAGS_INSTANCE_WITH_CLASS = 1
WBEMS_DISPID_DERIVATION = 23
WBEMS_DISPID_OBJECT_READY = 1
WBEMS_DISPID_COMPLETED = 2
WBEMS_DISPID_PROGRESS = 3
WBEMS_DISPID_OBJECT_PUT = 4
WBEMS_DISPID_CONNECTION_READY = 5
MI_Result = Int32
MI_RESULT_OK = 0
MI_RESULT_FAILED = 1
MI_RESULT_ACCESS_DENIED = 2
MI_RESULT_INVALID_NAMESPACE = 3
MI_RESULT_INVALID_PARAMETER = 4
MI_RESULT_INVALID_CLASS = 5
MI_RESULT_NOT_FOUND = 6
MI_RESULT_NOT_SUPPORTED = 7
MI_RESULT_CLASS_HAS_CHILDREN = 8
MI_RESULT_CLASS_HAS_INSTANCES = 9
MI_RESULT_INVALID_SUPERCLASS = 10
MI_RESULT_ALREADY_EXISTS = 11
MI_RESULT_NO_SUCH_PROPERTY = 12
MI_RESULT_TYPE_MISMATCH = 13
MI_RESULT_QUERY_LANGUAGE_NOT_SUPPORTED = 14
MI_RESULT_INVALID_QUERY = 15
MI_RESULT_METHOD_NOT_AVAILABLE = 16
MI_RESULT_METHOD_NOT_FOUND = 17
MI_RESULT_NAMESPACE_NOT_EMPTY = 20
MI_RESULT_INVALID_ENUMERATION_CONTEXT = 21
MI_RESULT_INVALID_OPERATION_TIMEOUT = 22
MI_RESULT_PULL_HAS_BEEN_ABANDONED = 23
MI_RESULT_PULL_CANNOT_BE_ABANDONED = 24
MI_RESULT_FILTERED_ENUMERATION_NOT_SUPPORTED = 25
MI_RESULT_CONTINUATION_ON_ERROR_NOT_SUPPORTED = 26
MI_RESULT_SERVER_LIMITS_EXCEEDED = 27
MI_RESULT_SERVER_IS_SHUTTING_DOWN = 28
MI_ErrorCategory = Int32
MI_ERRORCATEGORY_NOT_SPECIFIED = 0
MI_ERRORCATEGORY_OPEN_ERROR = 1
MI_ERRORCATEGORY_CLOS_EERROR = 2
MI_ERRORCATEGORY_DEVICE_ERROR = 3
MI_ERRORCATEGORY_DEADLOCK_DETECTED = 4
MI_ERRORCATEGORY_INVALID_ARGUMENT = 5
MI_ERRORCATEGORY_INVALID_DATA = 6
MI_ERRORCATEGORY_INVALID_OPERATION = 7
MI_ERRORCATEGORY_INVALID_RESULT = 8
MI_ERRORCATEGORY_INVALID_TYPE = 9
MI_ERRORCATEGORY_METADATA_ERROR = 10
MI_ERRORCATEGORY_NOT_IMPLEMENTED = 11
MI_ERRORCATEGORY_NOT_INSTALLED = 12
MI_ERRORCATEGORY_OBJECT_NOT_FOUND = 13
MI_ERRORCATEGORY_OPERATION_STOPPED = 14
MI_ERRORCATEGORY_OPERATION_TIMEOUT = 15
MI_ERRORCATEGORY_SYNTAX_ERROR = 16
MI_ERRORCATEGORY_PARSER_ERROR = 17
MI_ERRORCATEGORY_ACCESS_DENIED = 18
MI_ERRORCATEGORY_RESOURCE_BUSY = 19
MI_ERRORCATEGORY_RESOURCE_EXISTS = 20
MI_ERRORCATEGORY_RESOURCE_UNAVAILABLE = 21
MI_ERRORCATEGORY_READ_ERROR = 22
MI_ERRORCATEGORY_WRITE_ERROR = 23
MI_ERRORCATEGORY_FROM_STDERR = 24
MI_ERRORCATEGORY_SECURITY_ERROR = 25
MI_ERRORCATEGORY_PROTOCOL_ERROR = 26
MI_ERRORCATEGORY_CONNECTION_ERROR = 27
MI_ERRORCATEGORY_AUTHENTICATION_ERROR = 28
MI_ERRORCATEGORY_LIMITS_EXCEEDED = 29
MI_ERRORCATEGORY_QUOTA_EXCEEDED = 30
MI_ERRORCATEGORY_NOT_ENABLED = 31
MI_PromptType = Int32
MI_PROMPTTYPE_NORMAL = 0
MI_PROMPTTYPE_CRITICAL = 1
MI_CallbackMode = Int32
MI_CALLBACKMODE_REPORT = 0
MI_CALLBACKMODE_INQUIRE = 1
MI_CALLBACKMODE_IGNORE = 2
MI_ProviderArchitecture = Int32
MI_PROVIDER_ARCHITECTURE_32BIT = 0
MI_PROVIDER_ARCHITECTURE_64BIT = 1
MI_Type = Int32
MI_BOOLEAN = 0
MI_UINT8 = 1
MI_SINT8 = 2
MI_UINT16 = 3
MI_SINT16 = 4
MI_UINT32 = 5
MI_SINT32 = 6
MI_UINT64 = 7
MI_SINT64 = 8
MI_REAL32 = 9
MI_REAL64 = 10
MI_CHAR16 = 11
MI_DATETIME = 12
MI_STRING = 13
MI_REFERENCE = 14
MI_INSTANCE = 15
MI_BOOLEANA = 16
MI_UINT8A = 17
MI_SINT8A = 18
MI_UINT16A = 19
MI_SINT16A = 20
MI_UINT32A = 21
MI_SINT32A = 22
MI_UINT64A = 23
MI_SINT64A = 24
MI_REAL32A = 25
MI_REAL64A = 26
MI_CHAR16A = 27
MI_DATETIMEA = 28
MI_STRINGA = 29
MI_REFERENCEA = 30
MI_INSTANCEA = 31
MI_ARRAY = 16
def _define_MI_Timestamp_head():
    class MI_Timestamp(Structure):
        pass
    return MI_Timestamp
def _define_MI_Timestamp():
    MI_Timestamp = win32more.System.Wmi.MI_Timestamp_head
    MI_Timestamp._fields_ = [
        ("year", UInt32),
        ("month", UInt32),
        ("day", UInt32),
        ("hour", UInt32),
        ("minute", UInt32),
        ("second", UInt32),
        ("microseconds", UInt32),
        ("utc", Int32),
    ]
    return MI_Timestamp
def _define_MI_Interval_head():
    class MI_Interval(Structure):
        pass
    return MI_Interval
def _define_MI_Interval():
    MI_Interval = win32more.System.Wmi.MI_Interval_head
    MI_Interval._fields_ = [
        ("days", UInt32),
        ("hours", UInt32),
        ("minutes", UInt32),
        ("seconds", UInt32),
        ("microseconds", UInt32),
        ("__padding1", UInt32),
        ("__padding2", UInt32),
        ("__padding3", UInt32),
    ]
    return MI_Interval
def _define_MI_Datetime_head():
    class MI_Datetime(Structure):
        pass
    return MI_Datetime
def _define_MI_Datetime():
    MI_Datetime = win32more.System.Wmi.MI_Datetime_head
    class MI_Datetime__u_e__Union(Union):
        pass
    MI_Datetime__u_e__Union._fields_ = [
        ("timestamp", win32more.System.Wmi.MI_Timestamp),
        ("interval", win32more.System.Wmi.MI_Interval),
    ]
    MI_Datetime._fields_ = [
        ("isTimestamp", UInt32),
        ("u", MI_Datetime__u_e__Union),
    ]
    return MI_Datetime
def _define_MI_BooleanA_head():
    class MI_BooleanA(Structure):
        pass
    return MI_BooleanA
def _define_MI_BooleanA():
    MI_BooleanA = win32more.System.Wmi.MI_BooleanA_head
    MI_BooleanA._fields_ = [
        ("data", c_char_p_no),
        ("size", UInt32),
    ]
    return MI_BooleanA
def _define_MI_Uint8A_head():
    class MI_Uint8A(Structure):
        pass
    return MI_Uint8A
def _define_MI_Uint8A():
    MI_Uint8A = win32more.System.Wmi.MI_Uint8A_head
    MI_Uint8A._fields_ = [
        ("data", c_char_p_no),
        ("size", UInt32),
    ]
    return MI_Uint8A
def _define_MI_Sint8A_head():
    class MI_Sint8A(Structure):
        pass
    return MI_Sint8A
def _define_MI_Sint8A():
    MI_Sint8A = win32more.System.Wmi.MI_Sint8A_head
    MI_Sint8A._fields_ = [
        ("data", POINTER(SByte)),
        ("size", UInt32),
    ]
    return MI_Sint8A
def _define_MI_Uint16A_head():
    class MI_Uint16A(Structure):
        pass
    return MI_Uint16A
def _define_MI_Uint16A():
    MI_Uint16A = win32more.System.Wmi.MI_Uint16A_head
    MI_Uint16A._fields_ = [
        ("data", POINTER(UInt16)),
        ("size", UInt32),
    ]
    return MI_Uint16A
def _define_MI_Sint16A_head():
    class MI_Sint16A(Structure):
        pass
    return MI_Sint16A
def _define_MI_Sint16A():
    MI_Sint16A = win32more.System.Wmi.MI_Sint16A_head
    MI_Sint16A._fields_ = [
        ("data", POINTER(Int16)),
        ("size", UInt32),
    ]
    return MI_Sint16A
def _define_MI_Uint32A_head():
    class MI_Uint32A(Structure):
        pass
    return MI_Uint32A
def _define_MI_Uint32A():
    MI_Uint32A = win32more.System.Wmi.MI_Uint32A_head
    MI_Uint32A._fields_ = [
        ("data", POINTER(UInt32)),
        ("size", UInt32),
    ]
    return MI_Uint32A
def _define_MI_Sint32A_head():
    class MI_Sint32A(Structure):
        pass
    return MI_Sint32A
def _define_MI_Sint32A():
    MI_Sint32A = win32more.System.Wmi.MI_Sint32A_head
    MI_Sint32A._fields_ = [
        ("data", POINTER(Int32)),
        ("size", UInt32),
    ]
    return MI_Sint32A
def _define_MI_Uint64A_head():
    class MI_Uint64A(Structure):
        pass
    return MI_Uint64A
def _define_MI_Uint64A():
    MI_Uint64A = win32more.System.Wmi.MI_Uint64A_head
    MI_Uint64A._fields_ = [
        ("data", POINTER(UInt64)),
        ("size", UInt32),
    ]
    return MI_Uint64A
def _define_MI_Sint64A_head():
    class MI_Sint64A(Structure):
        pass
    return MI_Sint64A
def _define_MI_Sint64A():
    MI_Sint64A = win32more.System.Wmi.MI_Sint64A_head
    MI_Sint64A._fields_ = [
        ("data", POINTER(Int64)),
        ("size", UInt32),
    ]
    return MI_Sint64A
def _define_MI_Real32A_head():
    class MI_Real32A(Structure):
        pass
    return MI_Real32A
def _define_MI_Real32A():
    MI_Real32A = win32more.System.Wmi.MI_Real32A_head
    MI_Real32A._fields_ = [
        ("data", POINTER(Single)),
        ("size", UInt32),
    ]
    return MI_Real32A
def _define_MI_Real64A_head():
    class MI_Real64A(Structure):
        pass
    return MI_Real64A
def _define_MI_Real64A():
    MI_Real64A = win32more.System.Wmi.MI_Real64A_head
    MI_Real64A._fields_ = [
        ("data", POINTER(Double)),
        ("size", UInt32),
    ]
    return MI_Real64A
def _define_MI_Char16A_head():
    class MI_Char16A(Structure):
        pass
    return MI_Char16A
def _define_MI_Char16A():
    MI_Char16A = win32more.System.Wmi.MI_Char16A_head
    MI_Char16A._fields_ = [
        ("data", POINTER(UInt16)),
        ("size", UInt32),
    ]
    return MI_Char16A
def _define_MI_DatetimeA_head():
    class MI_DatetimeA(Structure):
        pass
    return MI_DatetimeA
def _define_MI_DatetimeA():
    MI_DatetimeA = win32more.System.Wmi.MI_DatetimeA_head
    MI_DatetimeA._fields_ = [
        ("data", POINTER(win32more.System.Wmi.MI_Datetime_head)),
        ("size", UInt32),
    ]
    return MI_DatetimeA
def _define_MI_StringA_head():
    class MI_StringA(Structure):
        pass
    return MI_StringA
def _define_MI_StringA():
    MI_StringA = win32more.System.Wmi.MI_StringA_head
    MI_StringA._fields_ = [
        ("data", POINTER(POINTER(UInt16))),
        ("size", UInt32),
    ]
    return MI_StringA
def _define_MI_ReferenceA_head():
    class MI_ReferenceA(Structure):
        pass
    return MI_ReferenceA
def _define_MI_ReferenceA():
    MI_ReferenceA = win32more.System.Wmi.MI_ReferenceA_head
    MI_ReferenceA._fields_ = [
        ("data", POINTER(POINTER(win32more.System.Wmi.MI_Instance_head))),
        ("size", UInt32),
    ]
    return MI_ReferenceA
def _define_MI_InstanceA_head():
    class MI_InstanceA(Structure):
        pass
    return MI_InstanceA
def _define_MI_InstanceA():
    MI_InstanceA = win32more.System.Wmi.MI_InstanceA_head
    MI_InstanceA._fields_ = [
        ("data", POINTER(POINTER(win32more.System.Wmi.MI_Instance_head))),
        ("size", UInt32),
    ]
    return MI_InstanceA
def _define_MI_Array_head():
    class MI_Array(Structure):
        pass
    return MI_Array
def _define_MI_Array():
    MI_Array = win32more.System.Wmi.MI_Array_head
    MI_Array._fields_ = [
        ("data", c_void_p),
        ("size", UInt32),
    ]
    return MI_Array
def _define_MI_ConstBooleanA_head():
    class MI_ConstBooleanA(Structure):
        pass
    return MI_ConstBooleanA
def _define_MI_ConstBooleanA():
    MI_ConstBooleanA = win32more.System.Wmi.MI_ConstBooleanA_head
    MI_ConstBooleanA._fields_ = [
        ("data", c_char_p_no),
        ("size", UInt32),
    ]
    return MI_ConstBooleanA
def _define_MI_ConstUint8A_head():
    class MI_ConstUint8A(Structure):
        pass
    return MI_ConstUint8A
def _define_MI_ConstUint8A():
    MI_ConstUint8A = win32more.System.Wmi.MI_ConstUint8A_head
    MI_ConstUint8A._fields_ = [
        ("data", c_char_p_no),
        ("size", UInt32),
    ]
    return MI_ConstUint8A
def _define_MI_ConstSint8A_head():
    class MI_ConstSint8A(Structure):
        pass
    return MI_ConstSint8A
def _define_MI_ConstSint8A():
    MI_ConstSint8A = win32more.System.Wmi.MI_ConstSint8A_head
    MI_ConstSint8A._fields_ = [
        ("data", POINTER(SByte)),
        ("size", UInt32),
    ]
    return MI_ConstSint8A
def _define_MI_ConstUint16A_head():
    class MI_ConstUint16A(Structure):
        pass
    return MI_ConstUint16A
def _define_MI_ConstUint16A():
    MI_ConstUint16A = win32more.System.Wmi.MI_ConstUint16A_head
    MI_ConstUint16A._fields_ = [
        ("data", POINTER(UInt16)),
        ("size", UInt32),
    ]
    return MI_ConstUint16A
def _define_MI_ConstSint16A_head():
    class MI_ConstSint16A(Structure):
        pass
    return MI_ConstSint16A
def _define_MI_ConstSint16A():
    MI_ConstSint16A = win32more.System.Wmi.MI_ConstSint16A_head
    MI_ConstSint16A._fields_ = [
        ("data", POINTER(Int16)),
        ("size", UInt32),
    ]
    return MI_ConstSint16A
def _define_MI_ConstUint32A_head():
    class MI_ConstUint32A(Structure):
        pass
    return MI_ConstUint32A
def _define_MI_ConstUint32A():
    MI_ConstUint32A = win32more.System.Wmi.MI_ConstUint32A_head
    MI_ConstUint32A._fields_ = [
        ("data", POINTER(UInt32)),
        ("size", UInt32),
    ]
    return MI_ConstUint32A
def _define_MI_ConstSint32A_head():
    class MI_ConstSint32A(Structure):
        pass
    return MI_ConstSint32A
def _define_MI_ConstSint32A():
    MI_ConstSint32A = win32more.System.Wmi.MI_ConstSint32A_head
    MI_ConstSint32A._fields_ = [
        ("data", POINTER(Int32)),
        ("size", UInt32),
    ]
    return MI_ConstSint32A
def _define_MI_ConstUint64A_head():
    class MI_ConstUint64A(Structure):
        pass
    return MI_ConstUint64A
def _define_MI_ConstUint64A():
    MI_ConstUint64A = win32more.System.Wmi.MI_ConstUint64A_head
    MI_ConstUint64A._fields_ = [
        ("data", POINTER(UInt64)),
        ("size", UInt32),
    ]
    return MI_ConstUint64A
def _define_MI_ConstSint64A_head():
    class MI_ConstSint64A(Structure):
        pass
    return MI_ConstSint64A
def _define_MI_ConstSint64A():
    MI_ConstSint64A = win32more.System.Wmi.MI_ConstSint64A_head
    MI_ConstSint64A._fields_ = [
        ("data", POINTER(Int64)),
        ("size", UInt32),
    ]
    return MI_ConstSint64A
def _define_MI_ConstReal32A_head():
    class MI_ConstReal32A(Structure):
        pass
    return MI_ConstReal32A
def _define_MI_ConstReal32A():
    MI_ConstReal32A = win32more.System.Wmi.MI_ConstReal32A_head
    MI_ConstReal32A._fields_ = [
        ("data", POINTER(Single)),
        ("size", UInt32),
    ]
    return MI_ConstReal32A
def _define_MI_ConstReal64A_head():
    class MI_ConstReal64A(Structure):
        pass
    return MI_ConstReal64A
def _define_MI_ConstReal64A():
    MI_ConstReal64A = win32more.System.Wmi.MI_ConstReal64A_head
    MI_ConstReal64A._fields_ = [
        ("data", POINTER(Double)),
        ("size", UInt32),
    ]
    return MI_ConstReal64A
def _define_MI_ConstChar16A_head():
    class MI_ConstChar16A(Structure):
        pass
    return MI_ConstChar16A
def _define_MI_ConstChar16A():
    MI_ConstChar16A = win32more.System.Wmi.MI_ConstChar16A_head
    MI_ConstChar16A._fields_ = [
        ("data", POINTER(UInt16)),
        ("size", UInt32),
    ]
    return MI_ConstChar16A
def _define_MI_ConstDatetimeA_head():
    class MI_ConstDatetimeA(Structure):
        pass
    return MI_ConstDatetimeA
def _define_MI_ConstDatetimeA():
    MI_ConstDatetimeA = win32more.System.Wmi.MI_ConstDatetimeA_head
    MI_ConstDatetimeA._fields_ = [
        ("data", POINTER(win32more.System.Wmi.MI_Datetime_head)),
        ("size", UInt32),
    ]
    return MI_ConstDatetimeA
def _define_MI_ConstStringA_head():
    class MI_ConstStringA(Structure):
        pass
    return MI_ConstStringA
def _define_MI_ConstStringA():
    MI_ConstStringA = win32more.System.Wmi.MI_ConstStringA_head
    MI_ConstStringA._fields_ = [
        ("data", POINTER(POINTER(UInt16))),
        ("size", UInt32),
    ]
    return MI_ConstStringA
def _define_MI_ConstReferenceA_head():
    class MI_ConstReferenceA(Structure):
        pass
    return MI_ConstReferenceA
def _define_MI_ConstReferenceA():
    MI_ConstReferenceA = win32more.System.Wmi.MI_ConstReferenceA_head
    MI_ConstReferenceA._fields_ = [
        ("data", POINTER(POINTER(win32more.System.Wmi.MI_Instance_head))),
        ("size", UInt32),
    ]
    return MI_ConstReferenceA
def _define_MI_ConstInstanceA_head():
    class MI_ConstInstanceA(Structure):
        pass
    return MI_ConstInstanceA
def _define_MI_ConstInstanceA():
    MI_ConstInstanceA = win32more.System.Wmi.MI_ConstInstanceA_head
    MI_ConstInstanceA._fields_ = [
        ("data", POINTER(POINTER(win32more.System.Wmi.MI_Instance_head))),
        ("size", UInt32),
    ]
    return MI_ConstInstanceA
def _define_MI_Value_head():
    class MI_Value(Union):
        pass
    return MI_Value
def _define_MI_Value():
    MI_Value = win32more.System.Wmi.MI_Value_head
    MI_Value._fields_ = [
        ("boolean", Byte),
        ("uint8", Byte),
        ("sint8", SByte),
        ("uint16", UInt16),
        ("sint16", Int16),
        ("uint32", UInt32),
        ("sint32", Int32),
        ("uint64", UInt64),
        ("sint64", Int64),
        ("real32", Single),
        ("real64", Double),
        ("char16", UInt16),
        ("datetime", win32more.System.Wmi.MI_Datetime),
        ("string", POINTER(UInt16)),
        ("instance", POINTER(win32more.System.Wmi.MI_Instance_head)),
        ("reference", POINTER(win32more.System.Wmi.MI_Instance_head)),
        ("booleana", win32more.System.Wmi.MI_BooleanA),
        ("uint8a", win32more.System.Wmi.MI_Uint8A),
        ("sint8a", win32more.System.Wmi.MI_Sint8A),
        ("uint16a", win32more.System.Wmi.MI_Uint16A),
        ("sint16a", win32more.System.Wmi.MI_Sint16A),
        ("uint32a", win32more.System.Wmi.MI_Uint32A),
        ("sint32a", win32more.System.Wmi.MI_Sint32A),
        ("uint64a", win32more.System.Wmi.MI_Uint64A),
        ("sint64a", win32more.System.Wmi.MI_Sint64A),
        ("real32a", win32more.System.Wmi.MI_Real32A),
        ("real64a", win32more.System.Wmi.MI_Real64A),
        ("char16a", win32more.System.Wmi.MI_Char16A),
        ("datetimea", win32more.System.Wmi.MI_DatetimeA),
        ("stringa", win32more.System.Wmi.MI_StringA),
        ("referencea", win32more.System.Wmi.MI_ReferenceA),
        ("instancea", win32more.System.Wmi.MI_InstanceA),
        ("array", win32more.System.Wmi.MI_Array),
    ]
    return MI_Value
def _define_MI_BooleanField_head():
    class MI_BooleanField(Structure):
        pass
    return MI_BooleanField
def _define_MI_BooleanField():
    MI_BooleanField = win32more.System.Wmi.MI_BooleanField_head
    MI_BooleanField._fields_ = [
        ("value", Byte),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_BooleanField
def _define_MI_Sint8Field_head():
    class MI_Sint8Field(Structure):
        pass
    return MI_Sint8Field
def _define_MI_Sint8Field():
    MI_Sint8Field = win32more.System.Wmi.MI_Sint8Field_head
    MI_Sint8Field._fields_ = [
        ("value", SByte),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_Sint8Field
def _define_MI_Uint8Field_head():
    class MI_Uint8Field(Structure):
        pass
    return MI_Uint8Field
def _define_MI_Uint8Field():
    MI_Uint8Field = win32more.System.Wmi.MI_Uint8Field_head
    MI_Uint8Field._fields_ = [
        ("value", Byte),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_Uint8Field
def _define_MI_Sint16Field_head():
    class MI_Sint16Field(Structure):
        pass
    return MI_Sint16Field
def _define_MI_Sint16Field():
    MI_Sint16Field = win32more.System.Wmi.MI_Sint16Field_head
    MI_Sint16Field._fields_ = [
        ("value", Int16),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_Sint16Field
def _define_MI_Uint16Field_head():
    class MI_Uint16Field(Structure):
        pass
    return MI_Uint16Field
def _define_MI_Uint16Field():
    MI_Uint16Field = win32more.System.Wmi.MI_Uint16Field_head
    MI_Uint16Field._fields_ = [
        ("value", UInt16),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_Uint16Field
def _define_MI_Sint32Field_head():
    class MI_Sint32Field(Structure):
        pass
    return MI_Sint32Field
def _define_MI_Sint32Field():
    MI_Sint32Field = win32more.System.Wmi.MI_Sint32Field_head
    MI_Sint32Field._fields_ = [
        ("value", Int32),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_Sint32Field
def _define_MI_Uint32Field_head():
    class MI_Uint32Field(Structure):
        pass
    return MI_Uint32Field
def _define_MI_Uint32Field():
    MI_Uint32Field = win32more.System.Wmi.MI_Uint32Field_head
    MI_Uint32Field._fields_ = [
        ("value", UInt32),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_Uint32Field
def _define_MI_Sint64Field_head():
    class MI_Sint64Field(Structure):
        pass
    return MI_Sint64Field
def _define_MI_Sint64Field():
    MI_Sint64Field = win32more.System.Wmi.MI_Sint64Field_head
    MI_Sint64Field._fields_ = [
        ("value", Int64),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_Sint64Field
def _define_MI_Uint64Field_head():
    class MI_Uint64Field(Structure):
        pass
    return MI_Uint64Field
def _define_MI_Uint64Field():
    MI_Uint64Field = win32more.System.Wmi.MI_Uint64Field_head
    MI_Uint64Field._fields_ = [
        ("value", UInt64),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_Uint64Field
def _define_MI_Real32Field_head():
    class MI_Real32Field(Structure):
        pass
    return MI_Real32Field
def _define_MI_Real32Field():
    MI_Real32Field = win32more.System.Wmi.MI_Real32Field_head
    MI_Real32Field._fields_ = [
        ("value", Single),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_Real32Field
def _define_MI_Real64Field_head():
    class MI_Real64Field(Structure):
        pass
    return MI_Real64Field
def _define_MI_Real64Field():
    MI_Real64Field = win32more.System.Wmi.MI_Real64Field_head
    MI_Real64Field._fields_ = [
        ("value", Double),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_Real64Field
def _define_MI_Char16Field_head():
    class MI_Char16Field(Structure):
        pass
    return MI_Char16Field
def _define_MI_Char16Field():
    MI_Char16Field = win32more.System.Wmi.MI_Char16Field_head
    MI_Char16Field._fields_ = [
        ("value", UInt16),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_Char16Field
def _define_MI_DatetimeField_head():
    class MI_DatetimeField(Structure):
        pass
    return MI_DatetimeField
def _define_MI_DatetimeField():
    MI_DatetimeField = win32more.System.Wmi.MI_DatetimeField_head
    MI_DatetimeField._fields_ = [
        ("value", win32more.System.Wmi.MI_Datetime),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_DatetimeField
def _define_MI_StringField_head():
    class MI_StringField(Structure):
        pass
    return MI_StringField
def _define_MI_StringField():
    MI_StringField = win32more.System.Wmi.MI_StringField_head
    MI_StringField._fields_ = [
        ("value", POINTER(UInt16)),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_StringField
def _define_MI_ReferenceField_head():
    class MI_ReferenceField(Structure):
        pass
    return MI_ReferenceField
def _define_MI_ReferenceField():
    MI_ReferenceField = win32more.System.Wmi.MI_ReferenceField_head
    MI_ReferenceField._fields_ = [
        ("value", POINTER(win32more.System.Wmi.MI_Instance_head)),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ReferenceField
def _define_MI_InstanceField_head():
    class MI_InstanceField(Structure):
        pass
    return MI_InstanceField
def _define_MI_InstanceField():
    MI_InstanceField = win32more.System.Wmi.MI_InstanceField_head
    MI_InstanceField._fields_ = [
        ("value", POINTER(win32more.System.Wmi.MI_Instance_head)),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_InstanceField
def _define_MI_BooleanAField_head():
    class MI_BooleanAField(Structure):
        pass
    return MI_BooleanAField
def _define_MI_BooleanAField():
    MI_BooleanAField = win32more.System.Wmi.MI_BooleanAField_head
    MI_BooleanAField._fields_ = [
        ("value", win32more.System.Wmi.MI_BooleanA),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_BooleanAField
def _define_MI_Uint8AField_head():
    class MI_Uint8AField(Structure):
        pass
    return MI_Uint8AField
def _define_MI_Uint8AField():
    MI_Uint8AField = win32more.System.Wmi.MI_Uint8AField_head
    MI_Uint8AField._fields_ = [
        ("value", win32more.System.Wmi.MI_Uint8A),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_Uint8AField
def _define_MI_Sint8AField_head():
    class MI_Sint8AField(Structure):
        pass
    return MI_Sint8AField
def _define_MI_Sint8AField():
    MI_Sint8AField = win32more.System.Wmi.MI_Sint8AField_head
    MI_Sint8AField._fields_ = [
        ("value", win32more.System.Wmi.MI_Sint8A),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_Sint8AField
def _define_MI_Uint16AField_head():
    class MI_Uint16AField(Structure):
        pass
    return MI_Uint16AField
def _define_MI_Uint16AField():
    MI_Uint16AField = win32more.System.Wmi.MI_Uint16AField_head
    MI_Uint16AField._fields_ = [
        ("value", win32more.System.Wmi.MI_Uint16A),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_Uint16AField
def _define_MI_Sint16AField_head():
    class MI_Sint16AField(Structure):
        pass
    return MI_Sint16AField
def _define_MI_Sint16AField():
    MI_Sint16AField = win32more.System.Wmi.MI_Sint16AField_head
    MI_Sint16AField._fields_ = [
        ("value", win32more.System.Wmi.MI_Sint16A),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_Sint16AField
def _define_MI_Uint32AField_head():
    class MI_Uint32AField(Structure):
        pass
    return MI_Uint32AField
def _define_MI_Uint32AField():
    MI_Uint32AField = win32more.System.Wmi.MI_Uint32AField_head
    MI_Uint32AField._fields_ = [
        ("value", win32more.System.Wmi.MI_Uint32A),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_Uint32AField
def _define_MI_Sint32AField_head():
    class MI_Sint32AField(Structure):
        pass
    return MI_Sint32AField
def _define_MI_Sint32AField():
    MI_Sint32AField = win32more.System.Wmi.MI_Sint32AField_head
    MI_Sint32AField._fields_ = [
        ("value", win32more.System.Wmi.MI_Sint32A),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_Sint32AField
def _define_MI_Uint64AField_head():
    class MI_Uint64AField(Structure):
        pass
    return MI_Uint64AField
def _define_MI_Uint64AField():
    MI_Uint64AField = win32more.System.Wmi.MI_Uint64AField_head
    MI_Uint64AField._fields_ = [
        ("value", win32more.System.Wmi.MI_Uint64A),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_Uint64AField
def _define_MI_Sint64AField_head():
    class MI_Sint64AField(Structure):
        pass
    return MI_Sint64AField
def _define_MI_Sint64AField():
    MI_Sint64AField = win32more.System.Wmi.MI_Sint64AField_head
    MI_Sint64AField._fields_ = [
        ("value", win32more.System.Wmi.MI_Sint64A),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_Sint64AField
def _define_MI_Real32AField_head():
    class MI_Real32AField(Structure):
        pass
    return MI_Real32AField
def _define_MI_Real32AField():
    MI_Real32AField = win32more.System.Wmi.MI_Real32AField_head
    MI_Real32AField._fields_ = [
        ("value", win32more.System.Wmi.MI_Real32A),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_Real32AField
def _define_MI_Real64AField_head():
    class MI_Real64AField(Structure):
        pass
    return MI_Real64AField
def _define_MI_Real64AField():
    MI_Real64AField = win32more.System.Wmi.MI_Real64AField_head
    MI_Real64AField._fields_ = [
        ("value", win32more.System.Wmi.MI_Real64A),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_Real64AField
def _define_MI_Char16AField_head():
    class MI_Char16AField(Structure):
        pass
    return MI_Char16AField
def _define_MI_Char16AField():
    MI_Char16AField = win32more.System.Wmi.MI_Char16AField_head
    MI_Char16AField._fields_ = [
        ("value", win32more.System.Wmi.MI_Char16A),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_Char16AField
def _define_MI_DatetimeAField_head():
    class MI_DatetimeAField(Structure):
        pass
    return MI_DatetimeAField
def _define_MI_DatetimeAField():
    MI_DatetimeAField = win32more.System.Wmi.MI_DatetimeAField_head
    MI_DatetimeAField._fields_ = [
        ("value", win32more.System.Wmi.MI_DatetimeA),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_DatetimeAField
def _define_MI_StringAField_head():
    class MI_StringAField(Structure):
        pass
    return MI_StringAField
def _define_MI_StringAField():
    MI_StringAField = win32more.System.Wmi.MI_StringAField_head
    MI_StringAField._fields_ = [
        ("value", win32more.System.Wmi.MI_StringA),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_StringAField
def _define_MI_ReferenceAField_head():
    class MI_ReferenceAField(Structure):
        pass
    return MI_ReferenceAField
def _define_MI_ReferenceAField():
    MI_ReferenceAField = win32more.System.Wmi.MI_ReferenceAField_head
    MI_ReferenceAField._fields_ = [
        ("value", win32more.System.Wmi.MI_ReferenceA),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ReferenceAField
def _define_MI_InstanceAField_head():
    class MI_InstanceAField(Structure):
        pass
    return MI_InstanceAField
def _define_MI_InstanceAField():
    MI_InstanceAField = win32more.System.Wmi.MI_InstanceAField_head
    MI_InstanceAField._fields_ = [
        ("value", win32more.System.Wmi.MI_InstanceA),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_InstanceAField
def _define_MI_ArrayField_head():
    class MI_ArrayField(Structure):
        pass
    return MI_ArrayField
def _define_MI_ArrayField():
    MI_ArrayField = win32more.System.Wmi.MI_ArrayField_head
    MI_ArrayField._fields_ = [
        ("value", win32more.System.Wmi.MI_Array),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ArrayField
def _define_MI_ConstBooleanField_head():
    class MI_ConstBooleanField(Structure):
        pass
    return MI_ConstBooleanField
def _define_MI_ConstBooleanField():
    MI_ConstBooleanField = win32more.System.Wmi.MI_ConstBooleanField_head
    MI_ConstBooleanField._fields_ = [
        ("value", Byte),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstBooleanField
def _define_MI_ConstSint8Field_head():
    class MI_ConstSint8Field(Structure):
        pass
    return MI_ConstSint8Field
def _define_MI_ConstSint8Field():
    MI_ConstSint8Field = win32more.System.Wmi.MI_ConstSint8Field_head
    MI_ConstSint8Field._fields_ = [
        ("value", SByte),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstSint8Field
def _define_MI_ConstUint8Field_head():
    class MI_ConstUint8Field(Structure):
        pass
    return MI_ConstUint8Field
def _define_MI_ConstUint8Field():
    MI_ConstUint8Field = win32more.System.Wmi.MI_ConstUint8Field_head
    MI_ConstUint8Field._fields_ = [
        ("value", Byte),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstUint8Field
def _define_MI_ConstSint16Field_head():
    class MI_ConstSint16Field(Structure):
        pass
    return MI_ConstSint16Field
def _define_MI_ConstSint16Field():
    MI_ConstSint16Field = win32more.System.Wmi.MI_ConstSint16Field_head
    MI_ConstSint16Field._fields_ = [
        ("value", Int16),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstSint16Field
def _define_MI_ConstUint16Field_head():
    class MI_ConstUint16Field(Structure):
        pass
    return MI_ConstUint16Field
def _define_MI_ConstUint16Field():
    MI_ConstUint16Field = win32more.System.Wmi.MI_ConstUint16Field_head
    MI_ConstUint16Field._fields_ = [
        ("value", UInt16),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstUint16Field
def _define_MI_ConstSint32Field_head():
    class MI_ConstSint32Field(Structure):
        pass
    return MI_ConstSint32Field
def _define_MI_ConstSint32Field():
    MI_ConstSint32Field = win32more.System.Wmi.MI_ConstSint32Field_head
    MI_ConstSint32Field._fields_ = [
        ("value", Int32),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstSint32Field
def _define_MI_ConstUint32Field_head():
    class MI_ConstUint32Field(Structure):
        pass
    return MI_ConstUint32Field
def _define_MI_ConstUint32Field():
    MI_ConstUint32Field = win32more.System.Wmi.MI_ConstUint32Field_head
    MI_ConstUint32Field._fields_ = [
        ("value", UInt32),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstUint32Field
def _define_MI_ConstSint64Field_head():
    class MI_ConstSint64Field(Structure):
        pass
    return MI_ConstSint64Field
def _define_MI_ConstSint64Field():
    MI_ConstSint64Field = win32more.System.Wmi.MI_ConstSint64Field_head
    MI_ConstSint64Field._fields_ = [
        ("value", Int64),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstSint64Field
def _define_MI_ConstUint64Field_head():
    class MI_ConstUint64Field(Structure):
        pass
    return MI_ConstUint64Field
def _define_MI_ConstUint64Field():
    MI_ConstUint64Field = win32more.System.Wmi.MI_ConstUint64Field_head
    MI_ConstUint64Field._fields_ = [
        ("value", UInt64),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstUint64Field
def _define_MI_ConstReal32Field_head():
    class MI_ConstReal32Field(Structure):
        pass
    return MI_ConstReal32Field
def _define_MI_ConstReal32Field():
    MI_ConstReal32Field = win32more.System.Wmi.MI_ConstReal32Field_head
    MI_ConstReal32Field._fields_ = [
        ("value", Single),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstReal32Field
def _define_MI_ConstReal64Field_head():
    class MI_ConstReal64Field(Structure):
        pass
    return MI_ConstReal64Field
def _define_MI_ConstReal64Field():
    MI_ConstReal64Field = win32more.System.Wmi.MI_ConstReal64Field_head
    MI_ConstReal64Field._fields_ = [
        ("value", Double),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstReal64Field
def _define_MI_ConstChar16Field_head():
    class MI_ConstChar16Field(Structure):
        pass
    return MI_ConstChar16Field
def _define_MI_ConstChar16Field():
    MI_ConstChar16Field = win32more.System.Wmi.MI_ConstChar16Field_head
    MI_ConstChar16Field._fields_ = [
        ("value", UInt16),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstChar16Field
def _define_MI_ConstDatetimeField_head():
    class MI_ConstDatetimeField(Structure):
        pass
    return MI_ConstDatetimeField
def _define_MI_ConstDatetimeField():
    MI_ConstDatetimeField = win32more.System.Wmi.MI_ConstDatetimeField_head
    MI_ConstDatetimeField._fields_ = [
        ("value", win32more.System.Wmi.MI_Datetime),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstDatetimeField
def _define_MI_ConstStringField_head():
    class MI_ConstStringField(Structure):
        pass
    return MI_ConstStringField
def _define_MI_ConstStringField():
    MI_ConstStringField = win32more.System.Wmi.MI_ConstStringField_head
    MI_ConstStringField._fields_ = [
        ("value", POINTER(UInt16)),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstStringField
def _define_MI_ConstReferenceField_head():
    class MI_ConstReferenceField(Structure):
        pass
    return MI_ConstReferenceField
def _define_MI_ConstReferenceField():
    MI_ConstReferenceField = win32more.System.Wmi.MI_ConstReferenceField_head
    MI_ConstReferenceField._fields_ = [
        ("value", POINTER(win32more.System.Wmi.MI_Instance_head)),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstReferenceField
def _define_MI_ConstInstanceField_head():
    class MI_ConstInstanceField(Structure):
        pass
    return MI_ConstInstanceField
def _define_MI_ConstInstanceField():
    MI_ConstInstanceField = win32more.System.Wmi.MI_ConstInstanceField_head
    MI_ConstInstanceField._fields_ = [
        ("value", POINTER(win32more.System.Wmi.MI_Instance_head)),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstInstanceField
def _define_MI_ConstBooleanAField_head():
    class MI_ConstBooleanAField(Structure):
        pass
    return MI_ConstBooleanAField
def _define_MI_ConstBooleanAField():
    MI_ConstBooleanAField = win32more.System.Wmi.MI_ConstBooleanAField_head
    MI_ConstBooleanAField._fields_ = [
        ("value", win32more.System.Wmi.MI_ConstBooleanA),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstBooleanAField
def _define_MI_ConstUint8AField_head():
    class MI_ConstUint8AField(Structure):
        pass
    return MI_ConstUint8AField
def _define_MI_ConstUint8AField():
    MI_ConstUint8AField = win32more.System.Wmi.MI_ConstUint8AField_head
    MI_ConstUint8AField._fields_ = [
        ("value", win32more.System.Wmi.MI_ConstUint8A),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstUint8AField
def _define_MI_ConstSint8AField_head():
    class MI_ConstSint8AField(Structure):
        pass
    return MI_ConstSint8AField
def _define_MI_ConstSint8AField():
    MI_ConstSint8AField = win32more.System.Wmi.MI_ConstSint8AField_head
    MI_ConstSint8AField._fields_ = [
        ("value", win32more.System.Wmi.MI_ConstSint8A),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstSint8AField
def _define_MI_ConstUint16AField_head():
    class MI_ConstUint16AField(Structure):
        pass
    return MI_ConstUint16AField
def _define_MI_ConstUint16AField():
    MI_ConstUint16AField = win32more.System.Wmi.MI_ConstUint16AField_head
    MI_ConstUint16AField._fields_ = [
        ("value", win32more.System.Wmi.MI_ConstUint16A),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstUint16AField
def _define_MI_ConstSint16AField_head():
    class MI_ConstSint16AField(Structure):
        pass
    return MI_ConstSint16AField
def _define_MI_ConstSint16AField():
    MI_ConstSint16AField = win32more.System.Wmi.MI_ConstSint16AField_head
    MI_ConstSint16AField._fields_ = [
        ("value", win32more.System.Wmi.MI_ConstSint16A),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstSint16AField
def _define_MI_ConstUint32AField_head():
    class MI_ConstUint32AField(Structure):
        pass
    return MI_ConstUint32AField
def _define_MI_ConstUint32AField():
    MI_ConstUint32AField = win32more.System.Wmi.MI_ConstUint32AField_head
    MI_ConstUint32AField._fields_ = [
        ("value", win32more.System.Wmi.MI_ConstUint32A),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstUint32AField
def _define_MI_ConstSint32AField_head():
    class MI_ConstSint32AField(Structure):
        pass
    return MI_ConstSint32AField
def _define_MI_ConstSint32AField():
    MI_ConstSint32AField = win32more.System.Wmi.MI_ConstSint32AField_head
    MI_ConstSint32AField._fields_ = [
        ("value", win32more.System.Wmi.MI_ConstSint32A),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstSint32AField
def _define_MI_ConstUint64AField_head():
    class MI_ConstUint64AField(Structure):
        pass
    return MI_ConstUint64AField
def _define_MI_ConstUint64AField():
    MI_ConstUint64AField = win32more.System.Wmi.MI_ConstUint64AField_head
    MI_ConstUint64AField._fields_ = [
        ("value", win32more.System.Wmi.MI_ConstUint64A),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstUint64AField
def _define_MI_ConstSint64AField_head():
    class MI_ConstSint64AField(Structure):
        pass
    return MI_ConstSint64AField
def _define_MI_ConstSint64AField():
    MI_ConstSint64AField = win32more.System.Wmi.MI_ConstSint64AField_head
    MI_ConstSint64AField._fields_ = [
        ("value", win32more.System.Wmi.MI_ConstSint64A),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstSint64AField
def _define_MI_ConstReal32AField_head():
    class MI_ConstReal32AField(Structure):
        pass
    return MI_ConstReal32AField
def _define_MI_ConstReal32AField():
    MI_ConstReal32AField = win32more.System.Wmi.MI_ConstReal32AField_head
    MI_ConstReal32AField._fields_ = [
        ("value", win32more.System.Wmi.MI_ConstReal32A),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstReal32AField
def _define_MI_ConstReal64AField_head():
    class MI_ConstReal64AField(Structure):
        pass
    return MI_ConstReal64AField
def _define_MI_ConstReal64AField():
    MI_ConstReal64AField = win32more.System.Wmi.MI_ConstReal64AField_head
    MI_ConstReal64AField._fields_ = [
        ("value", win32more.System.Wmi.MI_ConstReal64A),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstReal64AField
def _define_MI_ConstChar16AField_head():
    class MI_ConstChar16AField(Structure):
        pass
    return MI_ConstChar16AField
def _define_MI_ConstChar16AField():
    MI_ConstChar16AField = win32more.System.Wmi.MI_ConstChar16AField_head
    MI_ConstChar16AField._fields_ = [
        ("value", win32more.System.Wmi.MI_ConstChar16A),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstChar16AField
def _define_MI_ConstDatetimeAField_head():
    class MI_ConstDatetimeAField(Structure):
        pass
    return MI_ConstDatetimeAField
def _define_MI_ConstDatetimeAField():
    MI_ConstDatetimeAField = win32more.System.Wmi.MI_ConstDatetimeAField_head
    MI_ConstDatetimeAField._fields_ = [
        ("value", win32more.System.Wmi.MI_ConstDatetimeA),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstDatetimeAField
def _define_MI_ConstStringAField_head():
    class MI_ConstStringAField(Structure):
        pass
    return MI_ConstStringAField
def _define_MI_ConstStringAField():
    MI_ConstStringAField = win32more.System.Wmi.MI_ConstStringAField_head
    MI_ConstStringAField._fields_ = [
        ("value", win32more.System.Wmi.MI_ConstStringA),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstStringAField
def _define_MI_ConstReferenceAField_head():
    class MI_ConstReferenceAField(Structure):
        pass
    return MI_ConstReferenceAField
def _define_MI_ConstReferenceAField():
    MI_ConstReferenceAField = win32more.System.Wmi.MI_ConstReferenceAField_head
    MI_ConstReferenceAField._fields_ = [
        ("value", win32more.System.Wmi.MI_ConstReferenceA),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstReferenceAField
def _define_MI_ConstInstanceAField_head():
    class MI_ConstInstanceAField(Structure):
        pass
    return MI_ConstInstanceAField
def _define_MI_ConstInstanceAField():
    MI_ConstInstanceAField = win32more.System.Wmi.MI_ConstInstanceAField_head
    MI_ConstInstanceAField._fields_ = [
        ("value", win32more.System.Wmi.MI_ConstInstanceA),
        ("exists", Byte),
        ("flags", Byte),
    ]
    return MI_ConstInstanceAField
def _define_MI_ServerFT_head():
    class MI_ServerFT(Structure):
        pass
    return MI_ServerFT
def _define_MI_ServerFT():
    MI_ServerFT = win32more.System.Wmi.MI_ServerFT_head
    MI_ServerFT._fields_ = [
        ("GetVersion", IntPtr),
        ("GetSystemName", IntPtr),
    ]
    return MI_ServerFT
def _define_MI_Server_head():
    class MI_Server(Structure):
        pass
    return MI_Server
def _define_MI_Server():
    MI_Server = win32more.System.Wmi.MI_Server_head
    MI_Server._fields_ = [
        ("serverFT", POINTER(win32more.System.Wmi.MI_ServerFT_head)),
        ("contextFT", POINTER(win32more.System.Wmi.MI_ContextFT_head)),
        ("instanceFT", POINTER(win32more.System.Wmi.MI_InstanceFT_head)),
        ("propertySetFT", POINTER(win32more.System.Wmi.MI_PropertySetFT_head)),
        ("filterFT", POINTER(win32more.System.Wmi.MI_FilterFT_head)),
    ]
    return MI_Server
def _define_MI_FilterFT_head():
    class MI_FilterFT(Structure):
        pass
    return MI_FilterFT
def _define_MI_FilterFT():
    MI_FilterFT = win32more.System.Wmi.MI_FilterFT_head
    MI_FilterFT._fields_ = [
        ("Evaluate", IntPtr),
        ("GetExpression", IntPtr),
    ]
    return MI_FilterFT
def _define_MI_Filter_head():
    class MI_Filter(Structure):
        pass
    return MI_Filter
def _define_MI_Filter():
    MI_Filter = win32more.System.Wmi.MI_Filter_head
    MI_Filter._fields_ = [
        ("ft", POINTER(win32more.System.Wmi.MI_FilterFT_head)),
        ("reserved", IntPtr * 3),
    ]
    return MI_Filter
def _define_MI_PropertySetFT_head():
    class MI_PropertySetFT(Structure):
        pass
    return MI_PropertySetFT
def _define_MI_PropertySetFT():
    MI_PropertySetFT = win32more.System.Wmi.MI_PropertySetFT_head
    MI_PropertySetFT._fields_ = [
        ("GetElementCount", IntPtr),
        ("ContainsElement", IntPtr),
        ("AddElement", IntPtr),
        ("GetElementAt", IntPtr),
        ("Clear", IntPtr),
        ("Destruct", IntPtr),
        ("Delete", IntPtr),
        ("Clone", IntPtr),
    ]
    return MI_PropertySetFT
def _define_MI_PropertySet_head():
    class MI_PropertySet(Structure):
        pass
    return MI_PropertySet
def _define_MI_PropertySet():
    MI_PropertySet = win32more.System.Wmi.MI_PropertySet_head
    MI_PropertySet._fields_ = [
        ("ft", POINTER(win32more.System.Wmi.MI_PropertySetFT_head)),
        ("reserved", IntPtr * 3),
    ]
    return MI_PropertySet
def _define_MI_ObjectDecl_head():
    class MI_ObjectDecl(Structure):
        pass
    return MI_ObjectDecl
def _define_MI_ObjectDecl():
    MI_ObjectDecl = win32more.System.Wmi.MI_ObjectDecl_head
    MI_ObjectDecl._fields_ = [
        ("flags", UInt32),
        ("code", UInt32),
        ("name", POINTER(UInt16)),
        ("qualifiers", POINTER(POINTER(win32more.System.Wmi.MI_Qualifier_head))),
        ("numQualifiers", UInt32),
        ("properties", POINTER(POINTER(win32more.System.Wmi.MI_PropertyDecl_head))),
        ("numProperties", UInt32),
        ("size", UInt32),
    ]
    return MI_ObjectDecl
def _define_MI_ClassDecl_head():
    class MI_ClassDecl(Structure):
        pass
    return MI_ClassDecl
def _define_MI_ClassDecl():
    MI_ClassDecl = win32more.System.Wmi.MI_ClassDecl_head
    MI_ClassDecl._fields_ = [
        ("flags", UInt32),
        ("code", UInt32),
        ("name", POINTER(UInt16)),
        ("qualifiers", POINTER(POINTER(win32more.System.Wmi.MI_Qualifier_head))),
        ("numQualifiers", UInt32),
        ("properties", POINTER(POINTER(win32more.System.Wmi.MI_PropertyDecl_head))),
        ("numProperties", UInt32),
        ("size", UInt32),
        ("superClass", POINTER(UInt16)),
        ("superClassDecl", POINTER(win32more.System.Wmi.MI_ClassDecl_head)),
        ("methods", POINTER(POINTER(win32more.System.Wmi.MI_MethodDecl_head))),
        ("numMethods", UInt32),
        ("schema", POINTER(win32more.System.Wmi.MI_SchemaDecl_head)),
        ("providerFT", POINTER(win32more.System.Wmi.MI_ProviderFT_head)),
        ("owningClass", POINTER(win32more.System.Wmi.MI_Class_head)),
    ]
    return MI_ClassDecl
def _define_MI_FeatureDecl_head():
    class MI_FeatureDecl(Structure):
        pass
    return MI_FeatureDecl
def _define_MI_FeatureDecl():
    MI_FeatureDecl = win32more.System.Wmi.MI_FeatureDecl_head
    MI_FeatureDecl._fields_ = [
        ("flags", UInt32),
        ("code", UInt32),
        ("name", POINTER(UInt16)),
        ("qualifiers", POINTER(POINTER(win32more.System.Wmi.MI_Qualifier_head))),
        ("numQualifiers", UInt32),
    ]
    return MI_FeatureDecl
def _define_MI_ParameterDecl_head():
    class MI_ParameterDecl(Structure):
        pass
    return MI_ParameterDecl
def _define_MI_ParameterDecl():
    MI_ParameterDecl = win32more.System.Wmi.MI_ParameterDecl_head
    MI_ParameterDecl._fields_ = [
        ("flags", UInt32),
        ("code", UInt32),
        ("name", POINTER(UInt16)),
        ("qualifiers", POINTER(POINTER(win32more.System.Wmi.MI_Qualifier_head))),
        ("numQualifiers", UInt32),
        ("type", UInt32),
        ("className", POINTER(UInt16)),
        ("subscript", UInt32),
        ("offset", UInt32),
    ]
    return MI_ParameterDecl
def _define_MI_PropertyDecl_head():
    class MI_PropertyDecl(Structure):
        pass
    return MI_PropertyDecl
def _define_MI_PropertyDecl():
    MI_PropertyDecl = win32more.System.Wmi.MI_PropertyDecl_head
    MI_PropertyDecl._fields_ = [
        ("flags", UInt32),
        ("code", UInt32),
        ("name", POINTER(UInt16)),
        ("qualifiers", POINTER(POINTER(win32more.System.Wmi.MI_Qualifier_head))),
        ("numQualifiers", UInt32),
        ("type", UInt32),
        ("className", POINTER(UInt16)),
        ("subscript", UInt32),
        ("offset", UInt32),
        ("origin", POINTER(UInt16)),
        ("propagator", POINTER(UInt16)),
        ("value", c_void_p),
    ]
    return MI_PropertyDecl
def _define_MI_MethodDecl_Invoke():
    return CFUNCTYPE(Void,c_void_p,POINTER(win32more.System.Wmi.MI_Context_head),POINTER(UInt16),POINTER(UInt16),POINTER(UInt16),POINTER(win32more.System.Wmi.MI_Instance_head),POINTER(win32more.System.Wmi.MI_Instance_head), use_last_error=False)
def _define_MI_MethodDecl_head():
    class MI_MethodDecl(Structure):
        pass
    return MI_MethodDecl
def _define_MI_MethodDecl():
    MI_MethodDecl = win32more.System.Wmi.MI_MethodDecl_head
    MI_MethodDecl._fields_ = [
        ("flags", UInt32),
        ("code", UInt32),
        ("name", POINTER(UInt16)),
        ("qualifiers", POINTER(POINTER(win32more.System.Wmi.MI_Qualifier_head))),
        ("numQualifiers", UInt32),
        ("parameters", POINTER(POINTER(win32more.System.Wmi.MI_ParameterDecl_head))),
        ("numParameters", UInt32),
        ("size", UInt32),
        ("returnType", UInt32),
        ("origin", POINTER(UInt16)),
        ("propagator", POINTER(UInt16)),
        ("schema", POINTER(win32more.System.Wmi.MI_SchemaDecl_head)),
        ("function", win32more.System.Wmi.MI_MethodDecl_Invoke),
    ]
    return MI_MethodDecl
def _define_MI_QualifierDecl_head():
    class MI_QualifierDecl(Structure):
        pass
    return MI_QualifierDecl
def _define_MI_QualifierDecl():
    MI_QualifierDecl = win32more.System.Wmi.MI_QualifierDecl_head
    MI_QualifierDecl._fields_ = [
        ("name", POINTER(UInt16)),
        ("type", UInt32),
        ("scope", UInt32),
        ("flavor", UInt32),
        ("subscript", UInt32),
        ("value", c_void_p),
    ]
    return MI_QualifierDecl
def _define_MI_Qualifier_head():
    class MI_Qualifier(Structure):
        pass
    return MI_Qualifier
def _define_MI_Qualifier():
    MI_Qualifier = win32more.System.Wmi.MI_Qualifier_head
    MI_Qualifier._fields_ = [
        ("name", POINTER(UInt16)),
        ("type", UInt32),
        ("flavor", UInt32),
        ("value", c_void_p),
    ]
    return MI_Qualifier
def _define_MI_SchemaDecl_head():
    class MI_SchemaDecl(Structure):
        pass
    return MI_SchemaDecl
def _define_MI_SchemaDecl():
    MI_SchemaDecl = win32more.System.Wmi.MI_SchemaDecl_head
    MI_SchemaDecl._fields_ = [
        ("qualifierDecls", POINTER(POINTER(win32more.System.Wmi.MI_QualifierDecl_head))),
        ("numQualifierDecls", UInt32),
        ("classDecls", POINTER(POINTER(win32more.System.Wmi.MI_ClassDecl_head))),
        ("numClassDecls", UInt32),
    ]
    return MI_SchemaDecl
def _define_MI_Module_Self_head():
    class MI_Module_Self(Structure):
        pass
    return MI_Module_Self
def _define_MI_Module_Self():
    MI_Module_Self = win32more.System.Wmi.MI_Module_Self_head
    return MI_Module_Self
def _define_MI_ProviderFT_Load():
    return CFUNCTYPE(Void,POINTER(c_void_p),POINTER(win32more.System.Wmi.MI_Module_Self_head),POINTER(win32more.System.Wmi.MI_Context_head), use_last_error=False)
def _define_MI_ProviderFT_Unload():
    return CFUNCTYPE(Void,c_void_p,POINTER(win32more.System.Wmi.MI_Context_head), use_last_error=False)
def _define_MI_ProviderFT_GetInstance():
    return CFUNCTYPE(Void,c_void_p,POINTER(win32more.System.Wmi.MI_Context_head),POINTER(UInt16),POINTER(UInt16),POINTER(win32more.System.Wmi.MI_Instance_head),POINTER(win32more.System.Wmi.MI_PropertySet_head), use_last_error=False)
def _define_MI_ProviderFT_EnumerateInstances():
    return CFUNCTYPE(Void,c_void_p,POINTER(win32more.System.Wmi.MI_Context_head),POINTER(UInt16),POINTER(UInt16),POINTER(win32more.System.Wmi.MI_PropertySet_head),Byte,POINTER(win32more.System.Wmi.MI_Filter_head), use_last_error=False)
def _define_MI_ProviderFT_CreateInstance():
    return CFUNCTYPE(Void,c_void_p,POINTER(win32more.System.Wmi.MI_Context_head),POINTER(UInt16),POINTER(UInt16),POINTER(win32more.System.Wmi.MI_Instance_head), use_last_error=False)
def _define_MI_ProviderFT_ModifyInstance():
    return CFUNCTYPE(Void,c_void_p,POINTER(win32more.System.Wmi.MI_Context_head),POINTER(UInt16),POINTER(UInt16),POINTER(win32more.System.Wmi.MI_Instance_head),POINTER(win32more.System.Wmi.MI_PropertySet_head), use_last_error=False)
def _define_MI_ProviderFT_DeleteInstance():
    return CFUNCTYPE(Void,c_void_p,POINTER(win32more.System.Wmi.MI_Context_head),POINTER(UInt16),POINTER(UInt16),POINTER(win32more.System.Wmi.MI_Instance_head), use_last_error=False)
def _define_MI_ProviderFT_AssociatorInstances():
    return CFUNCTYPE(Void,c_void_p,POINTER(win32more.System.Wmi.MI_Context_head),POINTER(UInt16),POINTER(UInt16),POINTER(win32more.System.Wmi.MI_Instance_head),POINTER(UInt16),POINTER(UInt16),POINTER(UInt16),POINTER(win32more.System.Wmi.MI_PropertySet_head),Byte,POINTER(win32more.System.Wmi.MI_Filter_head), use_last_error=False)
def _define_MI_ProviderFT_ReferenceInstances():
    return CFUNCTYPE(Void,c_void_p,POINTER(win32more.System.Wmi.MI_Context_head),POINTER(UInt16),POINTER(UInt16),POINTER(win32more.System.Wmi.MI_Instance_head),POINTER(UInt16),POINTER(win32more.System.Wmi.MI_PropertySet_head),Byte,POINTER(win32more.System.Wmi.MI_Filter_head), use_last_error=False)
def _define_MI_ProviderFT_EnableIndications():
    return CFUNCTYPE(Void,c_void_p,POINTER(win32more.System.Wmi.MI_Context_head),POINTER(UInt16),POINTER(UInt16), use_last_error=False)
def _define_MI_ProviderFT_DisableIndications():
    return CFUNCTYPE(Void,c_void_p,POINTER(win32more.System.Wmi.MI_Context_head),POINTER(UInt16),POINTER(UInt16), use_last_error=False)
def _define_MI_ProviderFT_Subscribe():
    return CFUNCTYPE(Void,c_void_p,POINTER(win32more.System.Wmi.MI_Context_head),POINTER(UInt16),POINTER(UInt16),POINTER(win32more.System.Wmi.MI_Filter_head),POINTER(UInt16),UInt64,POINTER(c_void_p), use_last_error=False)
def _define_MI_ProviderFT_Unsubscribe():
    return CFUNCTYPE(Void,c_void_p,POINTER(win32more.System.Wmi.MI_Context_head),POINTER(UInt16),POINTER(UInt16),UInt64,c_void_p, use_last_error=False)
def _define_MI_ProviderFT_Invoke():
    return CFUNCTYPE(Void,c_void_p,POINTER(win32more.System.Wmi.MI_Context_head),POINTER(UInt16),POINTER(UInt16),POINTER(UInt16),POINTER(win32more.System.Wmi.MI_Instance_head),POINTER(win32more.System.Wmi.MI_Instance_head), use_last_error=False)
def _define_MI_ProviderFT_head():
    class MI_ProviderFT(Structure):
        pass
    return MI_ProviderFT
def _define_MI_ProviderFT():
    MI_ProviderFT = win32more.System.Wmi.MI_ProviderFT_head
    MI_ProviderFT._fields_ = [
        ("Load", win32more.System.Wmi.MI_ProviderFT_Load),
        ("Unload", win32more.System.Wmi.MI_ProviderFT_Unload),
        ("GetInstance", win32more.System.Wmi.MI_ProviderFT_GetInstance),
        ("EnumerateInstances", win32more.System.Wmi.MI_ProviderFT_EnumerateInstances),
        ("CreateInstance", win32more.System.Wmi.MI_ProviderFT_CreateInstance),
        ("ModifyInstance", win32more.System.Wmi.MI_ProviderFT_ModifyInstance),
        ("DeleteInstance", win32more.System.Wmi.MI_ProviderFT_DeleteInstance),
        ("AssociatorInstances", win32more.System.Wmi.MI_ProviderFT_AssociatorInstances),
        ("ReferenceInstances", win32more.System.Wmi.MI_ProviderFT_ReferenceInstances),
        ("EnableIndications", win32more.System.Wmi.MI_ProviderFT_EnableIndications),
        ("DisableIndications", win32more.System.Wmi.MI_ProviderFT_DisableIndications),
        ("Subscribe", win32more.System.Wmi.MI_ProviderFT_Subscribe),
        ("Unsubscribe", win32more.System.Wmi.MI_ProviderFT_Unsubscribe),
        ("Invoke", win32more.System.Wmi.MI_ProviderFT_Invoke),
    ]
    return MI_ProviderFT
def _define_MI_Module_Load():
    return CFUNCTYPE(Void,POINTER(POINTER(win32more.System.Wmi.MI_Module_Self_head)),POINTER(win32more.System.Wmi.MI_Context_head), use_last_error=False)
def _define_MI_Module_Unload():
    return CFUNCTYPE(Void,POINTER(win32more.System.Wmi.MI_Module_Self_head),POINTER(win32more.System.Wmi.MI_Context_head), use_last_error=False)
def _define_MI_Module_head():
    class MI_Module(Structure):
        pass
    return MI_Module
def _define_MI_Module():
    MI_Module = win32more.System.Wmi.MI_Module_head
    MI_Module._fields_ = [
        ("version", UInt32),
        ("generatorVersion", UInt32),
        ("flags", UInt32),
        ("charSize", UInt32),
        ("schemaDecl", POINTER(win32more.System.Wmi.MI_SchemaDecl_head)),
        ("Load", win32more.System.Wmi.MI_Module_Load),
        ("Unload", win32more.System.Wmi.MI_Module_Unload),
        ("dynamicProviderFT", POINTER(win32more.System.Wmi.MI_ProviderFT_head)),
    ]
    return MI_Module
def _define_MI_InstanceFT_head():
    class MI_InstanceFT(Structure):
        pass
    return MI_InstanceFT
def _define_MI_InstanceFT():
    MI_InstanceFT = win32more.System.Wmi.MI_InstanceFT_head
    MI_InstanceFT._fields_ = [
        ("Clone", IntPtr),
        ("Destruct", IntPtr),
        ("Delete", IntPtr),
        ("IsA", IntPtr),
        ("GetClassNameA", IntPtr),
        ("SetNameSpace", IntPtr),
        ("GetNameSpace", IntPtr),
        ("GetElementCount", IntPtr),
        ("AddElement", IntPtr),
        ("SetElement", IntPtr),
        ("SetElementAt", IntPtr),
        ("GetElement", IntPtr),
        ("GetElementAt", IntPtr),
        ("ClearElement", IntPtr),
        ("ClearElementAt", IntPtr),
        ("GetServerName", IntPtr),
        ("SetServerName", IntPtr),
        ("GetClass", IntPtr),
    ]
    return MI_InstanceFT
def _define_MI_InstanceExFT_head():
    class MI_InstanceExFT(Structure):
        pass
    return MI_InstanceExFT
def _define_MI_InstanceExFT():
    MI_InstanceExFT = win32more.System.Wmi.MI_InstanceExFT_head
    MI_InstanceExFT._fields_ = [
        ("parent", win32more.System.Wmi.MI_InstanceFT),
        ("Normalize", IntPtr),
    ]
    return MI_InstanceExFT
def _define_MI_Instance_head():
    class MI_Instance(Structure):
        pass
    return MI_Instance
def _define_MI_Instance():
    MI_Instance = win32more.System.Wmi.MI_Instance_head
    MI_Instance._fields_ = [
        ("ft", POINTER(win32more.System.Wmi.MI_InstanceFT_head)),
        ("classDecl", POINTER(win32more.System.Wmi.MI_ClassDecl_head)),
        ("serverName", POINTER(UInt16)),
        ("nameSpace", POINTER(UInt16)),
        ("reserved", IntPtr * 4),
    ]
    return MI_Instance
MI_LocaleType = Int32
MI_LOCALE_TYPE_REQUESTED_UI = 0
MI_LOCALE_TYPE_REQUESTED_DATA = 1
MI_LOCALE_TYPE_CLOSEST_UI = 2
MI_LOCALE_TYPE_CLOSEST_DATA = 3
MI_CancellationReason = Int32
MI_REASON_NONE = 0
MI_REASON_TIMEOUT = 1
MI_REASON_SHUTDOWN = 2
MI_REASON_SERVICESTOP = 3
def _define_MI_CancelCallback():
    return CFUNCTYPE(Void,win32more.System.Wmi.MI_CancellationReason,c_void_p, use_last_error=False)
def _define_MI_ContextFT_head():
    class MI_ContextFT(Structure):
        pass
    return MI_ContextFT
def _define_MI_ContextFT():
    MI_ContextFT = win32more.System.Wmi.MI_ContextFT_head
    MI_ContextFT._fields_ = [
        ("PostResult", IntPtr),
        ("PostInstance", IntPtr),
        ("PostIndication", IntPtr),
        ("ConstructInstance", IntPtr),
        ("ConstructParameters", IntPtr),
        ("NewInstance", IntPtr),
        ("NewDynamicInstance", IntPtr),
        ("NewParameters", IntPtr),
        ("Canceled", IntPtr),
        ("GetLocale", IntPtr),
        ("RegisterCancel", IntPtr),
        ("RequestUnload", IntPtr),
        ("RefuseUnload", IntPtr),
        ("GetLocalSession", IntPtr),
        ("SetStringOption", IntPtr),
        ("GetStringOption", IntPtr),
        ("GetNumberOption", IntPtr),
        ("GetCustomOption", IntPtr),
        ("GetCustomOptionCount", IntPtr),
        ("GetCustomOptionAt", IntPtr),
        ("WriteMessage", IntPtr),
        ("WriteProgress", IntPtr),
        ("WriteStreamParameter", IntPtr),
        ("WriteCimError", IntPtr),
        ("PromptUser", IntPtr),
        ("ShouldProcess", IntPtr),
        ("ShouldContinue", IntPtr),
        ("PostError", IntPtr),
        ("PostCimError", IntPtr),
        ("WriteError", IntPtr),
    ]
    return MI_ContextFT
def _define_MI_Context_head():
    class MI_Context(Structure):
        pass
    return MI_Context
def _define_MI_Context():
    MI_Context = win32more.System.Wmi.MI_Context_head
    MI_Context._fields_ = [
        ("ft", POINTER(win32more.System.Wmi.MI_ContextFT_head)),
        ("reserved", IntPtr * 3),
    ]
    return MI_Context
def _define_MI_MainFunction():
    return CFUNCTYPE(POINTER(win32more.System.Wmi.MI_Module_head),POINTER(win32more.System.Wmi.MI_Server_head), use_last_error=False)
def _define_MI_QualifierSetFT_head():
    class MI_QualifierSetFT(Structure):
        pass
    return MI_QualifierSetFT
def _define_MI_QualifierSetFT():
    MI_QualifierSetFT = win32more.System.Wmi.MI_QualifierSetFT_head
    MI_QualifierSetFT._fields_ = [
        ("GetQualifierCount", IntPtr),
        ("GetQualifierAt", IntPtr),
        ("GetQualifier", IntPtr),
    ]
    return MI_QualifierSetFT
def _define_MI_QualifierSet_head():
    class MI_QualifierSet(Structure):
        pass
    return MI_QualifierSet
def _define_MI_QualifierSet():
    MI_QualifierSet = win32more.System.Wmi.MI_QualifierSet_head
    MI_QualifierSet._fields_ = [
        ("reserved1", UInt64),
        ("reserved2", IntPtr),
        ("ft", POINTER(win32more.System.Wmi.MI_QualifierSetFT_head)),
    ]
    return MI_QualifierSet
def _define_MI_ParameterSetFT_head():
    class MI_ParameterSetFT(Structure):
        pass
    return MI_ParameterSetFT
def _define_MI_ParameterSetFT():
    MI_ParameterSetFT = win32more.System.Wmi.MI_ParameterSetFT_head
    MI_ParameterSetFT._fields_ = [
        ("GetMethodReturnType", IntPtr),
        ("GetParameterCount", IntPtr),
        ("GetParameterAt", IntPtr),
        ("GetParameter", IntPtr),
    ]
    return MI_ParameterSetFT
def _define_MI_ParameterSet_head():
    class MI_ParameterSet(Structure):
        pass
    return MI_ParameterSet
def _define_MI_ParameterSet():
    MI_ParameterSet = win32more.System.Wmi.MI_ParameterSet_head
    MI_ParameterSet._fields_ = [
        ("reserved1", UInt64),
        ("reserved2", IntPtr),
        ("ft", POINTER(win32more.System.Wmi.MI_ParameterSetFT_head)),
    ]
    return MI_ParameterSet
def _define_MI_ClassFT_head():
    class MI_ClassFT(Structure):
        pass
    return MI_ClassFT
def _define_MI_ClassFT():
    MI_ClassFT = win32more.System.Wmi.MI_ClassFT_head
    MI_ClassFT._fields_ = [
        ("GetClassNameA", IntPtr),
        ("GetNameSpace", IntPtr),
        ("GetServerName", IntPtr),
        ("GetElementCount", IntPtr),
        ("GetElement", IntPtr),
        ("GetElementAt", IntPtr),
        ("GetClassQualifierSet", IntPtr),
        ("GetMethodCount", IntPtr),
        ("GetMethodAt", IntPtr),
        ("GetMethod", IntPtr),
        ("GetParentClassName", IntPtr),
        ("GetParentClass", IntPtr),
        ("Delete", IntPtr),
        ("Clone", IntPtr),
    ]
    return MI_ClassFT
def _define_MI_Class_head():
    class MI_Class(Structure):
        pass
    return MI_Class
def _define_MI_Class():
    MI_Class = win32more.System.Wmi.MI_Class_head
    MI_Class._fields_ = [
        ("ft", POINTER(win32more.System.Wmi.MI_ClassFT_head)),
        ("classDecl", POINTER(win32more.System.Wmi.MI_ClassDecl_head)),
        ("namespaceName", POINTER(UInt16)),
        ("serverName", POINTER(UInt16)),
        ("reserved", IntPtr * 4),
    ]
    return MI_Class
MI_OperationCallback_ResponseType = Int32
MI_OperationCallback_ResponseType_No = 0
MI_OperationCallback_ResponseType_Yes = 1
MI_OperationCallback_ResponseType_NoToAll = 2
MI_OperationCallback_ResponseType_YesToAll = 3
def _define_MI_OperationCallback_PromptUser():
    return CFUNCTYPE(Void,POINTER(win32more.System.Wmi.MI_Operation_head),c_void_p,POINTER(UInt16),win32more.System.Wmi.MI_PromptType,IntPtr, use_last_error=False)
def _define_MI_OperationCallback_WriteError():
    return CFUNCTYPE(Void,POINTER(win32more.System.Wmi.MI_Operation_head),c_void_p,POINTER(win32more.System.Wmi.MI_Instance_head),IntPtr, use_last_error=False)
def _define_MI_OperationCallback_WriteMessage():
    return CFUNCTYPE(Void,POINTER(win32more.System.Wmi.MI_Operation_head),c_void_p,UInt32,POINTER(UInt16), use_last_error=False)
def _define_MI_OperationCallback_WriteProgress():
    return CFUNCTYPE(Void,POINTER(win32more.System.Wmi.MI_Operation_head),c_void_p,POINTER(UInt16),POINTER(UInt16),POINTER(UInt16),UInt32,UInt32, use_last_error=False)
def _define_MI_OperationCallback_Instance():
    return CFUNCTYPE(Void,POINTER(win32more.System.Wmi.MI_Operation_head),c_void_p,POINTER(win32more.System.Wmi.MI_Instance_head),Byte,win32more.System.Wmi.MI_Result,POINTER(UInt16),POINTER(win32more.System.Wmi.MI_Instance_head),IntPtr, use_last_error=False)
def _define_MI_OperationCallback_StreamedParameter():
    return CFUNCTYPE(Void,POINTER(win32more.System.Wmi.MI_Operation_head),c_void_p,POINTER(UInt16),win32more.System.Wmi.MI_Type,POINTER(win32more.System.Wmi.MI_Value_head),IntPtr, use_last_error=False)
def _define_MI_OperationCallback_Indication():
    return CFUNCTYPE(Void,POINTER(win32more.System.Wmi.MI_Operation_head),c_void_p,POINTER(win32more.System.Wmi.MI_Instance_head),POINTER(UInt16),POINTER(UInt16),Byte,win32more.System.Wmi.MI_Result,POINTER(UInt16),POINTER(win32more.System.Wmi.MI_Instance_head),IntPtr, use_last_error=False)
def _define_MI_OperationCallback_Class():
    return CFUNCTYPE(Void,POINTER(win32more.System.Wmi.MI_Operation_head),c_void_p,POINTER(win32more.System.Wmi.MI_Class_head),Byte,win32more.System.Wmi.MI_Result,POINTER(UInt16),POINTER(win32more.System.Wmi.MI_Instance_head),IntPtr, use_last_error=False)
def _define_MI_OperationCallbacks_head():
    class MI_OperationCallbacks(Structure):
        pass
    return MI_OperationCallbacks
def _define_MI_OperationCallbacks():
    MI_OperationCallbacks = win32more.System.Wmi.MI_OperationCallbacks_head
    MI_OperationCallbacks._fields_ = [
        ("callbackContext", c_void_p),
        ("promptUser", win32more.System.Wmi.MI_OperationCallback_PromptUser),
        ("writeError", win32more.System.Wmi.MI_OperationCallback_WriteError),
        ("writeMessage", win32more.System.Wmi.MI_OperationCallback_WriteMessage),
        ("writeProgress", win32more.System.Wmi.MI_OperationCallback_WriteProgress),
        ("instanceResult", win32more.System.Wmi.MI_OperationCallback_Instance),
        ("indicationResult", win32more.System.Wmi.MI_OperationCallback_Indication),
        ("classResult", win32more.System.Wmi.MI_OperationCallback_Class),
        ("streamedParameterResult", win32more.System.Wmi.MI_OperationCallback_StreamedParameter),
    ]
    return MI_OperationCallbacks
def _define_MI_SessionCallbacks_head():
    class MI_SessionCallbacks(Structure):
        pass
    return MI_SessionCallbacks
def _define_MI_SessionCallbacks():
    MI_SessionCallbacks = win32more.System.Wmi.MI_SessionCallbacks_head
    MI_SessionCallbacks._fields_ = [
        ("callbackContext", c_void_p),
        ("writeMessage", IntPtr),
        ("writeError", IntPtr),
    ]
    return MI_SessionCallbacks
def _define_MI_UsernamePasswordCreds_head():
    class MI_UsernamePasswordCreds(Structure):
        pass
    return MI_UsernamePasswordCreds
def _define_MI_UsernamePasswordCreds():
    MI_UsernamePasswordCreds = win32more.System.Wmi.MI_UsernamePasswordCreds_head
    MI_UsernamePasswordCreds._fields_ = [
        ("domain", POINTER(UInt16)),
        ("username", POINTER(UInt16)),
        ("password", POINTER(UInt16)),
    ]
    return MI_UsernamePasswordCreds
def _define_MI_UserCredentials_head():
    class MI_UserCredentials(Structure):
        pass
    return MI_UserCredentials
def _define_MI_UserCredentials():
    MI_UserCredentials = win32more.System.Wmi.MI_UserCredentials_head
    class MI_UserCredentials__credentials_e__Union(Union):
        pass
    MI_UserCredentials__credentials_e__Union._fields_ = [
        ("usernamePassword", win32more.System.Wmi.MI_UsernamePasswordCreds),
        ("certificateThumbprint", POINTER(UInt16)),
    ]
    MI_UserCredentials._fields_ = [
        ("authenticationType", POINTER(UInt16)),
        ("credentials", MI_UserCredentials__credentials_e__Union),
    ]
    return MI_UserCredentials
MI_SubscriptionDeliveryType = Int32
MI_SubscriptionDeliveryType_Pull = 1
MI_SubscriptionDeliveryType_Push = 2
def _define_MI_SubscriptionDeliveryOptionsFT_head():
    class MI_SubscriptionDeliveryOptionsFT(Structure):
        pass
    return MI_SubscriptionDeliveryOptionsFT
def _define_MI_SubscriptionDeliveryOptionsFT():
    MI_SubscriptionDeliveryOptionsFT = win32more.System.Wmi.MI_SubscriptionDeliveryOptionsFT_head
    MI_SubscriptionDeliveryOptionsFT._fields_ = [
        ("SetString", IntPtr),
        ("SetNumber", IntPtr),
        ("SetDateTime", IntPtr),
        ("SetInterval", IntPtr),
        ("AddCredentials", IntPtr),
        ("Delete", IntPtr),
        ("GetString", IntPtr),
        ("GetNumber", IntPtr),
        ("GetDateTime", IntPtr),
        ("GetInterval", IntPtr),
        ("GetOptionCount", IntPtr),
        ("GetOptionAt", IntPtr),
        ("GetOption", IntPtr),
        ("GetCredentialsCount", IntPtr),
        ("GetCredentialsAt", IntPtr),
        ("GetCredentialsPasswordAt", IntPtr),
        ("Clone", IntPtr),
    ]
    return MI_SubscriptionDeliveryOptionsFT
def _define_MI_SubscriptionDeliveryOptions_head():
    class MI_SubscriptionDeliveryOptions(Structure):
        pass
    return MI_SubscriptionDeliveryOptions
def _define_MI_SubscriptionDeliveryOptions():
    MI_SubscriptionDeliveryOptions = win32more.System.Wmi.MI_SubscriptionDeliveryOptions_head
    MI_SubscriptionDeliveryOptions._fields_ = [
        ("reserved1", UInt64),
        ("reserved2", IntPtr),
        ("ft", POINTER(win32more.System.Wmi.MI_SubscriptionDeliveryOptionsFT_head)),
    ]
    return MI_SubscriptionDeliveryOptions
def _define_MI_Serializer_head():
    class MI_Serializer(Structure):
        pass
    return MI_Serializer
def _define_MI_Serializer():
    MI_Serializer = win32more.System.Wmi.MI_Serializer_head
    MI_Serializer._fields_ = [
        ("reserved1", UInt64),
        ("reserved2", IntPtr),
    ]
    return MI_Serializer
def _define_MI_Deserializer_head():
    class MI_Deserializer(Structure):
        pass
    return MI_Deserializer
def _define_MI_Deserializer():
    MI_Deserializer = win32more.System.Wmi.MI_Deserializer_head
    MI_Deserializer._fields_ = [
        ("reserved1", UInt64),
        ("reserved2", IntPtr),
    ]
    return MI_Deserializer
def _define_MI_SerializerFT_head():
    class MI_SerializerFT(Structure):
        pass
    return MI_SerializerFT
def _define_MI_SerializerFT():
    MI_SerializerFT = win32more.System.Wmi.MI_SerializerFT_head
    MI_SerializerFT._fields_ = [
        ("Close", IntPtr),
        ("SerializeClass", IntPtr),
        ("SerializeInstance", IntPtr),
    ]
    return MI_SerializerFT
def _define_MI_Deserializer_ClassObjectNeeded():
    return CFUNCTYPE(win32more.System.Wmi.MI_Result,c_void_p,POINTER(UInt16),POINTER(UInt16),POINTER(UInt16),POINTER(POINTER(win32more.System.Wmi.MI_Class_head)), use_last_error=False)
def _define_MI_DeserializerFT_head():
    class MI_DeserializerFT(Structure):
        pass
    return MI_DeserializerFT
def _define_MI_DeserializerFT():
    MI_DeserializerFT = win32more.System.Wmi.MI_DeserializerFT_head
    MI_DeserializerFT._fields_ = [
        ("Close", IntPtr),
        ("DeserializeClass", IntPtr),
        ("Class_GetClassName", IntPtr),
        ("Class_GetParentClassName", IntPtr),
        ("DeserializeInstance", IntPtr),
        ("Instance_GetClassName", IntPtr),
    ]
    return MI_DeserializerFT
def _define_MI_ApplicationFT_head():
    class MI_ApplicationFT(Structure):
        pass
    return MI_ApplicationFT
def _define_MI_ApplicationFT():
    MI_ApplicationFT = win32more.System.Wmi.MI_ApplicationFT_head
    MI_ApplicationFT._fields_ = [
        ("Close", IntPtr),
        ("NewSession", IntPtr),
        ("NewHostedProvider", IntPtr),
        ("NewInstance", IntPtr),
        ("NewDestinationOptions", IntPtr),
        ("NewOperationOptions", IntPtr),
        ("NewSubscriptionDeliveryOptions", IntPtr),
        ("NewSerializer", IntPtr),
        ("NewDeserializer", IntPtr),
        ("NewInstanceFromClass", IntPtr),
        ("NewClass", IntPtr),
    ]
    return MI_ApplicationFT
def _define_MI_HostedProviderFT_head():
    class MI_HostedProviderFT(Structure):
        pass
    return MI_HostedProviderFT
def _define_MI_HostedProviderFT():
    MI_HostedProviderFT = win32more.System.Wmi.MI_HostedProviderFT_head
    MI_HostedProviderFT._fields_ = [
        ("Close", IntPtr),
        ("GetApplication", IntPtr),
    ]
    return MI_HostedProviderFT
def _define_MI_SessionFT_head():
    class MI_SessionFT(Structure):
        pass
    return MI_SessionFT
def _define_MI_SessionFT():
    MI_SessionFT = win32more.System.Wmi.MI_SessionFT_head
    MI_SessionFT._fields_ = [
        ("Close", IntPtr),
        ("GetApplication", IntPtr),
        ("GetInstance", IntPtr),
        ("ModifyInstance", IntPtr),
        ("CreateInstance", IntPtr),
        ("DeleteInstance", IntPtr),
        ("Invoke", IntPtr),
        ("EnumerateInstances", IntPtr),
        ("QueryInstances", IntPtr),
        ("AssociatorInstances", IntPtr),
        ("ReferenceInstances", IntPtr),
        ("Subscribe", IntPtr),
        ("GetClass", IntPtr),
        ("EnumerateClasses", IntPtr),
        ("TestConnection", IntPtr),
    ]
    return MI_SessionFT
def _define_MI_OperationFT_head():
    class MI_OperationFT(Structure):
        pass
    return MI_OperationFT
def _define_MI_OperationFT():
    MI_OperationFT = win32more.System.Wmi.MI_OperationFT_head
    MI_OperationFT._fields_ = [
        ("Close", IntPtr),
        ("Cancel", IntPtr),
        ("GetSession", IntPtr),
        ("GetInstance", IntPtr),
        ("GetIndication", IntPtr),
        ("GetClass", IntPtr),
    ]
    return MI_OperationFT
def _define_MI_DestinationOptionsFT_head():
    class MI_DestinationOptionsFT(Structure):
        pass
    return MI_DestinationOptionsFT
def _define_MI_DestinationOptionsFT():
    MI_DestinationOptionsFT = win32more.System.Wmi.MI_DestinationOptionsFT_head
    MI_DestinationOptionsFT._fields_ = [
        ("Delete", IntPtr),
        ("SetString", IntPtr),
        ("SetNumber", IntPtr),
        ("AddCredentials", IntPtr),
        ("GetString", IntPtr),
        ("GetNumber", IntPtr),
        ("GetOptionCount", IntPtr),
        ("GetOptionAt", IntPtr),
        ("GetOption", IntPtr),
        ("GetCredentialsCount", IntPtr),
        ("GetCredentialsAt", IntPtr),
        ("GetCredentialsPasswordAt", IntPtr),
        ("Clone", IntPtr),
        ("SetInterval", IntPtr),
        ("GetInterval", IntPtr),
    ]
    return MI_DestinationOptionsFT
def _define_MI_OperationOptionsFT_head():
    class MI_OperationOptionsFT(Structure):
        pass
    return MI_OperationOptionsFT
def _define_MI_OperationOptionsFT():
    MI_OperationOptionsFT = win32more.System.Wmi.MI_OperationOptionsFT_head
    MI_OperationOptionsFT._fields_ = [
        ("Delete", IntPtr),
        ("SetString", IntPtr),
        ("SetNumber", IntPtr),
        ("SetCustomOption", IntPtr),
        ("GetString", IntPtr),
        ("GetNumber", IntPtr),
        ("GetOptionCount", IntPtr),
        ("GetOptionAt", IntPtr),
        ("GetOption", IntPtr),
        ("GetEnabledChannels", IntPtr),
        ("Clone", IntPtr),
        ("SetInterval", IntPtr),
        ("GetInterval", IntPtr),
    ]
    return MI_OperationOptionsFT
def _define_MI_Application_head():
    class MI_Application(Structure):
        pass
    return MI_Application
def _define_MI_Application():
    MI_Application = win32more.System.Wmi.MI_Application_head
    MI_Application._fields_ = [
        ("reserved1", UInt64),
        ("reserved2", IntPtr),
        ("ft", POINTER(win32more.System.Wmi.MI_ApplicationFT_head)),
    ]
    return MI_Application
def _define_MI_Session_head():
    class MI_Session(Structure):
        pass
    return MI_Session
def _define_MI_Session():
    MI_Session = win32more.System.Wmi.MI_Session_head
    MI_Session._fields_ = [
        ("reserved1", UInt64),
        ("reserved2", IntPtr),
        ("ft", POINTER(win32more.System.Wmi.MI_SessionFT_head)),
    ]
    return MI_Session
def _define_MI_Operation_head():
    class MI_Operation(Structure):
        pass
    return MI_Operation
def _define_MI_Operation():
    MI_Operation = win32more.System.Wmi.MI_Operation_head
    MI_Operation._fields_ = [
        ("reserved1", UInt64),
        ("reserved2", IntPtr),
        ("ft", POINTER(win32more.System.Wmi.MI_OperationFT_head)),
    ]
    return MI_Operation
def _define_MI_HostedProvider_head():
    class MI_HostedProvider(Structure):
        pass
    return MI_HostedProvider
def _define_MI_HostedProvider():
    MI_HostedProvider = win32more.System.Wmi.MI_HostedProvider_head
    MI_HostedProvider._fields_ = [
        ("reserved1", UInt64),
        ("reserved2", IntPtr),
        ("ft", POINTER(win32more.System.Wmi.MI_HostedProviderFT_head)),
    ]
    return MI_HostedProvider
def _define_MI_DestinationOptions_head():
    class MI_DestinationOptions(Structure):
        pass
    return MI_DestinationOptions
def _define_MI_DestinationOptions():
    MI_DestinationOptions = win32more.System.Wmi.MI_DestinationOptions_head
    MI_DestinationOptions._fields_ = [
        ("reserved1", UInt64),
        ("reserved2", IntPtr),
        ("ft", POINTER(win32more.System.Wmi.MI_DestinationOptionsFT_head)),
    ]
    return MI_DestinationOptions
def _define_MI_OperationOptions_head():
    class MI_OperationOptions(Structure):
        pass
    return MI_OperationOptions
def _define_MI_OperationOptions():
    MI_OperationOptions = win32more.System.Wmi.MI_OperationOptions_head
    MI_OperationOptions._fields_ = [
        ("reserved1", UInt64),
        ("reserved2", IntPtr),
        ("ft", POINTER(win32more.System.Wmi.MI_OperationOptionsFT_head)),
    ]
    return MI_OperationOptions
def _define_MI_UtilitiesFT_head():
    class MI_UtilitiesFT(Structure):
        pass
    return MI_UtilitiesFT
def _define_MI_UtilitiesFT():
    MI_UtilitiesFT = win32more.System.Wmi.MI_UtilitiesFT_head
    MI_UtilitiesFT._fields_ = [
        ("MapErrorToMiErrorCategory", IntPtr),
        ("CimErrorFromErrorCode", IntPtr),
    ]
    return MI_UtilitiesFT
def _define_MI_ClientFT_V1_head():
    class MI_ClientFT_V1(Structure):
        pass
    return MI_ClientFT_V1
def _define_MI_ClientFT_V1():
    MI_ClientFT_V1 = win32more.System.Wmi.MI_ClientFT_V1_head
    MI_ClientFT_V1._fields_ = [
        ("applicationFT", POINTER(win32more.System.Wmi.MI_ApplicationFT_head)),
        ("sessionFT", POINTER(win32more.System.Wmi.MI_SessionFT_head)),
        ("operationFT", POINTER(win32more.System.Wmi.MI_OperationFT_head)),
        ("hostedProviderFT", POINTER(win32more.System.Wmi.MI_HostedProviderFT_head)),
        ("serializerFT", POINTER(win32more.System.Wmi.MI_SerializerFT_head)),
        ("deserializerFT", POINTER(win32more.System.Wmi.MI_DeserializerFT_head)),
        ("subscribeDeliveryOptionsFT", POINTER(win32more.System.Wmi.MI_SubscriptionDeliveryOptionsFT_head)),
        ("destinationOptionsFT", POINTER(win32more.System.Wmi.MI_DestinationOptionsFT_head)),
        ("operationOptionsFT", POINTER(win32more.System.Wmi.MI_OperationOptionsFT_head)),
        ("utilitiesFT", POINTER(win32more.System.Wmi.MI_UtilitiesFT_head)),
    ]
    return MI_ClientFT_V1
MI_DestinationOptions_ImpersonationType = Int32
MI_DestinationOptions_ImpersonationType_Default = 0
MI_DestinationOptions_ImpersonationType_None = 1
MI_DestinationOptions_ImpersonationType_Identify = 2
MI_DestinationOptions_ImpersonationType_Impersonate = 3
MI_DestinationOptions_ImpersonationType_Delegate = 4
WbemDefPath = Guid('cf4cc405-e2c5-4ddd-b3ce-5e7582d8c9fa')
WbemQuery = Guid('eac8a024-21e2-4523-ad73-a71a0aa2f56a')
WBEM_PATH_STATUS_FLAG = Int32
WBEMPATH_INFO_ANON_LOCAL_MACHINE = 1
WBEMPATH_INFO_HAS_MACHINE_NAME = 2
WBEMPATH_INFO_IS_CLASS_REF = 4
WBEMPATH_INFO_IS_INST_REF = 8
WBEMPATH_INFO_HAS_SUBSCOPES = 16
WBEMPATH_INFO_IS_COMPOUND = 32
WBEMPATH_INFO_HAS_V2_REF_PATHS = 64
WBEMPATH_INFO_HAS_IMPLIED_KEY = 128
WBEMPATH_INFO_CONTAINS_SINGLETON = 256
WBEMPATH_INFO_V1_COMPLIANT = 512
WBEMPATH_INFO_V2_COMPLIANT = 1024
WBEMPATH_INFO_CIM_COMPLIANT = 2048
WBEMPATH_INFO_IS_SINGLETON = 4096
WBEMPATH_INFO_IS_PARENT = 8192
WBEMPATH_INFO_SERVER_NAMESPACE_ONLY = 16384
WBEMPATH_INFO_NATIVE_PATH = 32768
WBEMPATH_INFO_WMI_PATH = 65536
WBEMPATH_INFO_PATH_HAD_SERVER = 131072
WBEM_PATH_CREATE_FLAG = Int32
WBEMPATH_CREATE_ACCEPT_RELATIVE = 1
WBEMPATH_CREATE_ACCEPT_ABSOLUTE = 2
WBEMPATH_CREATE_ACCEPT_ALL = 4
WBEMPATH_TREAT_SINGLE_IDENT_AS_NS = 8
WBEM_GET_TEXT_FLAGS = Int32
WBEMPATH_COMPRESSED = 1
WBEMPATH_GET_RELATIVE_ONLY = 2
WBEMPATH_GET_SERVER_TOO = 4
WBEMPATH_GET_SERVER_AND_NAMESPACE_ONLY = 8
WBEMPATH_GET_NAMESPACE_ONLY = 16
WBEMPATH_GET_ORIGINAL = 32
WBEM_GET_KEY_FLAGS = Int32
WBEMPATH_TEXT = 1
WBEMPATH_QUOTEDTEXT = 2
def _define_IWbemPathKeyList_head():
    class IWbemPathKeyList(win32more.System.Com.IUnknown_head):
        Guid = Guid('9ae62877-7544-4bb0-aa26-a13824659ed6')
    return IWbemPathKeyList
def _define_IWbemPathKeyList():
    IWbemPathKeyList = win32more.System.Wmi.IWbemPathKeyList_head
    IWbemPathKeyList.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetCount', ((1, 'puKeyCount'),)))
    IWbemPathKeyList.SetKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,c_void_p, use_last_error=False)(4, 'SetKey', ((1, 'wszName'),(1, 'uFlags'),(1, 'uCimType'),(1, 'pKeyVal'),)))
    IWbemPathKeyList.SetKey2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(5, 'SetKey2', ((1, 'wszName'),(1, 'uFlags'),(1, 'uCimType'),(1, 'pKeyVal'),)))
    IWbemPathKeyList.GetKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(UInt32),POINTER(Char),POINTER(UInt32),c_void_p,POINTER(UInt32), use_last_error=False)(6, 'GetKey', ((1, 'uKeyIx'),(1, 'uFlags'),(1, 'puNameBufSize'),(1, 'pszKeyName'),(1, 'puKeyValBufSize'),(1, 'pKeyVal'),(1, 'puApparentCimType'),)))
    IWbemPathKeyList.GetKey2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(UInt32),POINTER(Char),POINTER(win32more.System.Com.VARIANT_head),POINTER(UInt32), use_last_error=False)(7, 'GetKey2', ((1, 'uKeyIx'),(1, 'uFlags'),(1, 'puNameBufSize'),(1, 'pszKeyName'),(1, 'pKeyValue'),(1, 'puApparentCimType'),)))
    IWbemPathKeyList.RemoveKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(8, 'RemoveKey', ((1, 'wszName'),(1, 'uFlags'),)))
    IWbemPathKeyList.RemoveAllKeys = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(9, 'RemoveAllKeys', ((1, 'uFlags'),)))
    IWbemPathKeyList.MakeSingleton = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Byte, use_last_error=False)(10, 'MakeSingleton', ((1, 'bSet'),)))
    IWbemPathKeyList.GetInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt64), use_last_error=False)(11, 'GetInfo', ((1, 'uRequestedInfo'),(1, 'puResponse'),)))
    IWbemPathKeyList.GetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(UInt32),POINTER(Char), use_last_error=False)(12, 'GetText', ((1, 'lFlags'),(1, 'puBuffLength'),(1, 'pszText'),)))
    return IWbemPathKeyList
def _define_IWbemPath_head():
    class IWbemPath(win32more.System.Com.IUnknown_head):
        Guid = Guid('3bc15af2-736c-477e-9e51-238af8667dcc')
    return IWbemPath
def _define_IWbemPath():
    IWbemPath = win32more.System.Wmi.IWbemPath_head
    IWbemPath.SetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(3, 'SetText', ((1, 'uMode'),(1, 'pszPath'),)))
    IWbemPath.GetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(UInt32),POINTER(Char), use_last_error=False)(4, 'GetText', ((1, 'lFlags'),(1, 'puBuffLength'),(1, 'pszText'),)))
    IWbemPath.GetInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt64), use_last_error=False)(5, 'GetInfo', ((1, 'uRequestedInfo'),(1, 'puResponse'),)))
    IWbemPath.SetServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(6, 'SetServer', ((1, 'Name'),)))
    IWbemPath.GetServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(Char), use_last_error=False)(7, 'GetServer', ((1, 'puNameBufLength'),(1, 'pName'),)))
    IWbemPath.GetNamespaceCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(8, 'GetNamespaceCount', ((1, 'puCount'),)))
    IWbemPath.SetNamespaceAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(9, 'SetNamespaceAt', ((1, 'uIndex'),(1, 'pszName'),)))
    IWbemPath.GetNamespaceAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(Char), use_last_error=False)(10, 'GetNamespaceAt', ((1, 'uIndex'),(1, 'puNameBufLength'),(1, 'pName'),)))
    IWbemPath.RemoveNamespaceAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(11, 'RemoveNamespaceAt', ((1, 'uIndex'),)))
    IWbemPath.RemoveAllNamespaces = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'RemoveAllNamespaces', ()))
    IWbemPath.GetScopeCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(13, 'GetScopeCount', ((1, 'puCount'),)))
    IWbemPath.SetScope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(14, 'SetScope', ((1, 'uIndex'),(1, 'pszClass'),)))
    IWbemPath.SetScopeFromText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(15, 'SetScopeFromText', ((1, 'uIndex'),(1, 'pszText'),)))
    IWbemPath.GetScope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(Char),POINTER(win32more.System.Wmi.IWbemPathKeyList_head), use_last_error=False)(16, 'GetScope', ((1, 'uIndex'),(1, 'puClassNameBufSize'),(1, 'pszClass'),(1, 'pKeyList'),)))
    IWbemPath.GetScopeAsText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(Char), use_last_error=False)(17, 'GetScopeAsText', ((1, 'uIndex'),(1, 'puTextBufSize'),(1, 'pszText'),)))
    IWbemPath.RemoveScope = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(18, 'RemoveScope', ((1, 'uIndex'),)))
    IWbemPath.RemoveAllScopes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(19, 'RemoveAllScopes', ()))
    IWbemPath.SetClassName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(20, 'SetClassName', ((1, 'Name'),)))
    IWbemPath.GetClassName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(Char), use_last_error=False)(21, 'GetClassName', ((1, 'puBuffLength'),(1, 'pszName'),)))
    IWbemPath.GetKeyList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.IWbemPathKeyList_head), use_last_error=False)(22, 'GetKeyList', ((1, 'pOut'),)))
    IWbemPath.CreateClassPart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.PWSTR, use_last_error=False)(23, 'CreateClassPart', ((1, 'lFlags'),(1, 'Name'),)))
    IWbemPath.DeleteClassPart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(24, 'DeleteClassPart', ((1, 'lFlags'),)))
    IWbemPath.IsRelative = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(25, 'IsRelative', ((1, 'wszMachine'),(1, 'wszNamespace'),)))
    IWbemPath.IsRelativeOrChild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Int32, use_last_error=False)(26, 'IsRelativeOrChild', ((1, 'wszMachine'),(1, 'wszNamespace'),(1, 'lFlags'),)))
    IWbemPath.IsLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR, use_last_error=False)(27, 'IsLocal', ((1, 'wszMachine'),)))
    IWbemPath.IsSameClassName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR, use_last_error=False)(28, 'IsSameClassName', ((1, 'wszClass'),)))
    return IWbemPath
def _define_IWbemQuery_head():
    class IWbemQuery(win32more.System.Com.IUnknown_head):
        Guid = Guid('81166f58-dd98-11d3-a120-00105a1f515a')
    return IWbemQuery
def _define_IWbemQuery():
    IWbemQuery = win32more.System.Wmi.IWbemQuery_head
    IWbemQuery.Empty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Empty', ()))
    IWbemQuery.SetLanguageFeatures = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(UInt32), use_last_error=False)(4, 'SetLanguageFeatures', ((1, 'uFlags'),(1, 'uArraySize'),(1, 'puFeatures'),)))
    IWbemQuery.TestLanguageFeatures = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(5, 'TestLanguageFeatures', ((1, 'uFlags'),(1, 'uArraySize'),(1, 'puFeatures'),)))
    IWbemQuery.Parse = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(6, 'Parse', ((1, 'pszLang'),(1, 'pszQuery'),(1, 'uFlags'),)))
    IWbemQuery.GetAnalysis = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(c_void_p), use_last_error=False)(7, 'GetAnalysis', ((1, 'uAnalysisType'),(1, 'uFlags'),(1, 'pAnalysis'),)))
    IWbemQuery.FreeMemory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(8, 'FreeMemory', ((1, 'pMem'),)))
    IWbemQuery.GetQueryInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,c_void_p, use_last_error=False)(9, 'GetQueryInfo', ((1, 'uAnalysisType'),(1, 'uInfoId'),(1, 'uBufSize'),(1, 'pDestBuf'),)))
    return IWbemQuery
WMIQ_ANALYSIS_TYPE = Int32
WMIQ_ANALYSIS_RPN_SEQUENCE = 1
WMIQ_ANALYSIS_ASSOC_QUERY = 2
WMIQ_ANALYSIS_PROP_ANALYSIS_MATRIX = 3
WMIQ_ANALYSIS_QUERY_TEXT = 4
WMIQ_ANALYSIS_RESERVED = 134217728
WMIQ_RPN_TOKEN_FLAGS = Int32
WMIQ_RPN_TOKEN_EXPRESSION = 1
WMIQ_RPN_TOKEN_AND = 2
WMIQ_RPN_TOKEN_OR = 3
WMIQ_RPN_TOKEN_NOT = 4
WMIQ_RPN_OP_UNDEFINED = 0
WMIQ_RPN_OP_EQ = 1
WMIQ_RPN_OP_NE = 2
WMIQ_RPN_OP_GE = 3
WMIQ_RPN_OP_LE = 4
WMIQ_RPN_OP_LT = 5
WMIQ_RPN_OP_GT = 6
WMIQ_RPN_OP_LIKE = 7
WMIQ_RPN_OP_ISA = 8
WMIQ_RPN_OP_ISNOTA = 9
WMIQ_RPN_OP_ISNULL = 10
WMIQ_RPN_OP_ISNOTNULL = 11
WMIQ_RPN_LEFT_PROPERTY_NAME = 1
WMIQ_RPN_RIGHT_PROPERTY_NAME = 2
WMIQ_RPN_CONST2 = 4
WMIQ_RPN_CONST = 8
WMIQ_RPN_RELOP = 16
WMIQ_RPN_LEFT_FUNCTION = 32
WMIQ_RPN_RIGHT_FUNCTION = 64
WMIQ_RPN_GET_TOKEN_TYPE = 1
WMIQ_RPN_GET_EXPR_SHAPE = 2
WMIQ_RPN_GET_LEFT_FUNCTION = 3
WMIQ_RPN_GET_RIGHT_FUNCTION = 4
WMIQ_RPN_GET_RELOP = 5
WMIQ_RPN_NEXT_TOKEN = 1
WMIQ_RPN_FROM_UNARY = 1
WMIQ_RPN_FROM_PATH = 2
WMIQ_RPN_FROM_CLASS_LIST = 4
WMIQ_RPN_FROM_MULTIPLE = 8
WMIQ_ASSOCQ_FLAGS = Int32
WMIQ_ASSOCQ_ASSOCIATORS = 1
WMIQ_ASSOCQ_REFERENCES = 2
WMIQ_ASSOCQ_RESULTCLASS = 4
WMIQ_ASSOCQ_ASSOCCLASS = 8
WMIQ_ASSOCQ_ROLE = 16
WMIQ_ASSOCQ_RESULTROLE = 32
WMIQ_ASSOCQ_REQUIREDQUALIFIER = 64
WMIQ_ASSOCQ_REQUIREDASSOCQUALIFIER = 128
WMIQ_ASSOCQ_CLASSDEFSONLY = 256
WMIQ_ASSOCQ_KEYSONLY = 512
WMIQ_ASSOCQ_SCHEMAONLY = 1024
WMIQ_ASSOCQ_CLASSREFSONLY = 2048
def _define_SWbemQueryQualifiedName_head():
    class SWbemQueryQualifiedName(Structure):
        pass
    return SWbemQueryQualifiedName
def _define_SWbemQueryQualifiedName():
    SWbemQueryQualifiedName = win32more.System.Wmi.SWbemQueryQualifiedName_head
    SWbemQueryQualifiedName._fields_ = [
        ("m_uVersion", UInt32),
        ("m_uTokenType", UInt32),
        ("m_uNameListSize", UInt32),
        ("m_ppszNameList", POINTER(win32more.Foundation.PWSTR)),
        ("m_bArraysUsed", win32more.Foundation.BOOL),
        ("m_pbArrayElUsed", POINTER(win32more.Foundation.BOOL)),
        ("m_puArrayIndex", POINTER(UInt32)),
    ]
    return SWbemQueryQualifiedName
def _define_SWbemRpnConst_head():
    class SWbemRpnConst(Union):
        pass
    return SWbemRpnConst
def _define_SWbemRpnConst():
    SWbemRpnConst = win32more.System.Wmi.SWbemRpnConst_head
    SWbemRpnConst._fields_ = [
        ("m_pszStrVal", win32more.Foundation.PWSTR),
        ("m_bBoolVal", win32more.Foundation.BOOL),
        ("m_lLongVal", Int32),
        ("m_uLongVal", UInt32),
        ("m_dblVal", Double),
        ("m_lVal64", Int64),
        ("m_uVal64", Int64),
    ]
    return SWbemRpnConst
def _define_SWbemRpnQueryToken_head():
    class SWbemRpnQueryToken(Structure):
        pass
    return SWbemRpnQueryToken
def _define_SWbemRpnQueryToken():
    SWbemRpnQueryToken = win32more.System.Wmi.SWbemRpnQueryToken_head
    SWbemRpnQueryToken._fields_ = [
        ("m_uVersion", UInt32),
        ("m_uTokenType", UInt32),
        ("m_uSubexpressionShape", UInt32),
        ("m_uOperator", UInt32),
        ("m_pRightIdent", POINTER(win32more.System.Wmi.SWbemQueryQualifiedName_head)),
        ("m_pLeftIdent", POINTER(win32more.System.Wmi.SWbemQueryQualifiedName_head)),
        ("m_uConstApparentType", UInt32),
        ("m_Const", win32more.System.Wmi.SWbemRpnConst),
        ("m_uConst2ApparentType", UInt32),
        ("m_Const2", win32more.System.Wmi.SWbemRpnConst),
        ("m_pszRightFunc", win32more.Foundation.PWSTR),
        ("m_pszLeftFunc", win32more.Foundation.PWSTR),
    ]
    return SWbemRpnQueryToken
def _define_SWbemRpnTokenList_head():
    class SWbemRpnTokenList(Structure):
        pass
    return SWbemRpnTokenList
def _define_SWbemRpnTokenList():
    SWbemRpnTokenList = win32more.System.Wmi.SWbemRpnTokenList_head
    SWbemRpnTokenList._fields_ = [
        ("m_uVersion", UInt32),
        ("m_uTokenType", UInt32),
        ("m_uNumTokens", UInt32),
    ]
    return SWbemRpnTokenList
WMIQ_LANGUAGE_FEATURES = Int32
WMIQ_LF1_BASIC_SELECT = 1
WMIQ_LF2_CLASS_NAME_IN_QUERY = 2
WMIQ_LF3_STRING_CASE_FUNCTIONS = 3
WMIQ_LF4_PROP_TO_PROP_TESTS = 4
WMIQ_LF5_COUNT_STAR = 5
WMIQ_LF6_ORDER_BY = 6
WMIQ_LF7_DISTINCT = 7
WMIQ_LF8_ISA = 8
WMIQ_LF9_THIS = 9
WMIQ_LF10_COMPEX_SUBEXPRESSIONS = 10
WMIQ_LF11_ALIASING = 11
WMIQ_LF12_GROUP_BY_HAVING = 12
WMIQ_LF13_WMI_WITHIN = 13
WMIQ_LF14_SQL_WRITE_OPERATIONS = 14
WMIQ_LF15_GO = 15
WMIQ_LF16_SINGLE_LEVEL_TRANSACTIONS = 16
WMIQ_LF17_QUALIFIED_NAMES = 17
WMIQ_LF18_ASSOCIATONS = 18
WMIQ_LF19_SYSTEM_PROPERTIES = 19
WMIQ_LF20_EXTENDED_SYSTEM_PROPERTIES = 20
WMIQ_LF21_SQL89_JOINS = 21
WMIQ_LF22_SQL92_JOINS = 22
WMIQ_LF23_SUBSELECTS = 23
WMIQ_LF24_UMI_EXTENSIONS = 24
WMIQ_LF25_DATEPART = 25
WMIQ_LF26_LIKE = 26
WMIQ_LF27_CIM_TEMPORAL_CONSTRUCTS = 27
WMIQ_LF28_STANDARD_AGGREGATES = 28
WMIQ_LF29_MULTI_LEVEL_ORDER_BY = 29
WMIQ_LF30_WMI_PRAGMAS = 30
WMIQ_LF31_QUALIFIER_TESTS = 31
WMIQ_LF32_SP_EXECUTE = 32
WMIQ_LF33_ARRAY_ACCESS = 33
WMIQ_LF34_UNION = 34
WMIQ_LF35_COMPLEX_SELECT_TARGET = 35
WMIQ_LF36_REFERENCE_TESTS = 36
WMIQ_LF37_SELECT_INTO = 37
WMIQ_LF38_BASIC_DATETIME_TESTS = 38
WMIQ_LF39_COUNT_COLUMN = 39
WMIQ_LF40_BETWEEN = 40
WMIQ_LF_LAST = 40
WMIQ_RPNQ_FEATURE = Int32
WMIQ_RPNF_WHERE_CLAUSE_PRESENT = 1
WMIQ_RPNF_QUERY_IS_CONJUNCTIVE = 2
WMIQ_RPNF_QUERY_IS_DISJUNCTIVE = 4
WMIQ_RPNF_PROJECTION = 8
WMIQ_RPNF_FEATURE_SELECT_STAR = 16
WMIQ_RPNF_EQUALITY_TESTS_ONLY = 32
WMIQ_RPNF_COUNT_STAR = 64
WMIQ_RPNF_QUALIFIED_NAMES_USED = 128
WMIQ_RPNF_SYSPROP_CLASS_USED = 256
WMIQ_RPNF_PROP_TO_PROP_TESTS = 512
WMIQ_RPNF_ORDER_BY = 1024
WMIQ_RPNF_ISA_USED = 2048
WMIQ_RPNF_GROUP_BY_HAVING = 4096
WMIQ_RPNF_ARRAY_ACCESS_USED = 8192
def _define_SWbemRpnEncodedQuery_head():
    class SWbemRpnEncodedQuery(Structure):
        pass
    return SWbemRpnEncodedQuery
def _define_SWbemRpnEncodedQuery():
    SWbemRpnEncodedQuery = win32more.System.Wmi.SWbemRpnEncodedQuery_head
    SWbemRpnEncodedQuery._fields_ = [
        ("m_uVersion", UInt32),
        ("m_uTokenType", UInt32),
        ("m_uParsedFeatureMask", UInt64),
        ("m_uDetectedArraySize", UInt32),
        ("m_puDetectedFeatures", POINTER(UInt32)),
        ("m_uSelectListSize", UInt32),
        ("m_ppSelectList", POINTER(POINTER(win32more.System.Wmi.SWbemQueryQualifiedName_head))),
        ("m_uFromTargetType", UInt32),
        ("m_pszOptionalFromPath", win32more.Foundation.PWSTR),
        ("m_uFromListSize", UInt32),
        ("m_ppszFromList", POINTER(win32more.Foundation.PWSTR)),
        ("m_uWhereClauseSize", UInt32),
        ("m_ppRpnWhereClause", POINTER(POINTER(win32more.System.Wmi.SWbemRpnQueryToken_head))),
        ("m_dblWithinPolling", Double),
        ("m_dblWithinWindow", Double),
        ("m_uOrderByListSize", UInt32),
        ("m_ppszOrderByList", POINTER(win32more.Foundation.PWSTR)),
        ("m_uOrderDirectionEl", POINTER(UInt32)),
    ]
    return SWbemRpnEncodedQuery
def _define_SWbemAnalysisMatrix_head():
    class SWbemAnalysisMatrix(Structure):
        pass
    return SWbemAnalysisMatrix
def _define_SWbemAnalysisMatrix():
    SWbemAnalysisMatrix = win32more.System.Wmi.SWbemAnalysisMatrix_head
    SWbemAnalysisMatrix._fields_ = [
        ("m_uVersion", UInt32),
        ("m_uMatrixType", UInt32),
        ("m_pszProperty", win32more.Foundation.PWSTR),
        ("m_uPropertyType", UInt32),
        ("m_uEntries", UInt32),
        ("m_pValues", POINTER(c_void_p)),
        ("m_pbTruthTable", POINTER(win32more.Foundation.BOOL)),
    ]
    return SWbemAnalysisMatrix
def _define_SWbemAnalysisMatrixList_head():
    class SWbemAnalysisMatrixList(Structure):
        pass
    return SWbemAnalysisMatrixList
def _define_SWbemAnalysisMatrixList():
    SWbemAnalysisMatrixList = win32more.System.Wmi.SWbemAnalysisMatrixList_head
    SWbemAnalysisMatrixList._fields_ = [
        ("m_uVersion", UInt32),
        ("m_uMatrixType", UInt32),
        ("m_uNumMatrices", UInt32),
        ("m_pMatrices", POINTER(win32more.System.Wmi.SWbemAnalysisMatrix_head)),
    ]
    return SWbemAnalysisMatrixList
def _define_SWbemAssocQueryInf_head():
    class SWbemAssocQueryInf(Structure):
        pass
    return SWbemAssocQueryInf
def _define_SWbemAssocQueryInf():
    SWbemAssocQueryInf = win32more.System.Wmi.SWbemAssocQueryInf_head
    SWbemAssocQueryInf._fields_ = [
        ("m_uVersion", UInt32),
        ("m_uAnalysisType", UInt32),
        ("m_uFeatureMask", UInt32),
        ("m_pPath", win32more.System.Wmi.IWbemPath_head),
        ("m_pszPath", win32more.Foundation.PWSTR),
        ("m_pszQueryText", win32more.Foundation.PWSTR),
        ("m_pszResultClass", win32more.Foundation.PWSTR),
        ("m_pszAssocClass", win32more.Foundation.PWSTR),
        ("m_pszRole", win32more.Foundation.PWSTR),
        ("m_pszResultRole", win32more.Foundation.PWSTR),
        ("m_pszRequiredQualifier", win32more.Foundation.PWSTR),
        ("m_pszRequiredAssocQualifier", win32more.Foundation.PWSTR),
    ]
    return SWbemAssocQueryInf
WbemLocator = Guid('4590f811-1d3a-11d0-891f-00aa004b2e24')
WbemContext = Guid('674b6698-ee92-11d0-ad71-00c04fd8fdff')
UnsecuredApartment = Guid('49bd2028-1523-11d1-ad79-00c04fd8fdff')
WbemClassObject = Guid('9a653086-174f-11d2-b5f9-00104b703efd')
MofCompiler = Guid('6daf9757-2e37-11d2-aec9-00c04fb68820')
WbemStatusCodeText = Guid('eb87e1bd-3233-11d2-aec9-00c04fb68820')
WbemBackupRestore = Guid('c49e32c6-bc8b-11d2-85d4-00105a1f8304')
WbemRefresher = Guid('c71566f2-561e-11d1-ad87-00c04fd8fdff')
WbemObjectTextSrc = Guid('8d1c559d-84f0-4bb3-a7d5-56a7435a9ba6')
WBEM_GENUS_TYPE = Int32
WBEM_GENUS_CLASS = 1
WBEM_GENUS_INSTANCE = 2
WBEM_CHANGE_FLAG_TYPE = Int32
WBEM_FLAG_CREATE_OR_UPDATE = 0
WBEM_FLAG_UPDATE_ONLY = 1
WBEM_FLAG_CREATE_ONLY = 2
WBEM_FLAG_UPDATE_COMPATIBLE = 0
WBEM_FLAG_UPDATE_SAFE_MODE = 32
WBEM_FLAG_UPDATE_FORCE_MODE = 64
WBEM_MASK_UPDATE_MODE = 96
WBEM_FLAG_ADVISORY = 65536
WBEM_GENERIC_FLAG_TYPE = Int32
WBEM_FLAG_RETURN_IMMEDIATELY = 16
WBEM_FLAG_RETURN_WBEM_COMPLETE = 0
WBEM_FLAG_BIDIRECTIONAL = 0
WBEM_FLAG_FORWARD_ONLY = 32
WBEM_FLAG_NO_ERROR_OBJECT = 64
WBEM_FLAG_RETURN_ERROR_OBJECT = 0
WBEM_FLAG_SEND_STATUS = 128
WBEM_FLAG_DONT_SEND_STATUS = 0
WBEM_FLAG_ENSURE_LOCATABLE = 256
WBEM_FLAG_DIRECT_READ = 512
WBEM_FLAG_SEND_ONLY_SELECTED = 0
WBEM_RETURN_WHEN_COMPLETE = 0
WBEM_RETURN_IMMEDIATELY = 16
WBEM_MASK_RESERVED_FLAGS = 126976
WBEM_FLAG_USE_AMENDED_QUALIFIERS = 131072
WBEM_FLAG_STRONG_VALIDATION = 1048576
WBEM_STATUS_TYPE = Int32
WBEM_STATUS_COMPLETE = 0
WBEM_STATUS_REQUIREMENTS = 1
WBEM_STATUS_PROGRESS = 2
WBEM_STATUS_LOGGING_INFORMATION = 256
WBEM_STATUS_LOGGING_INFORMATION_PROVIDER = 512
WBEM_STATUS_LOGGING_INFORMATION_HOST = 1024
WBEM_STATUS_LOGGING_INFORMATION_REPOSITORY = 2048
WBEM_STATUS_LOGGING_INFORMATION_ESS = 4096
WBEM_TIMEOUT_TYPE = Int32
WBEM_NO_WAIT = 0
WBEM_INFINITE = -1
WBEM_CONDITION_FLAG_TYPE = Int32
WBEM_FLAG_ALWAYS = 0
WBEM_FLAG_ONLY_IF_TRUE = 1
WBEM_FLAG_ONLY_IF_FALSE = 2
WBEM_FLAG_ONLY_IF_IDENTICAL = 3
WBEM_MASK_PRIMARY_CONDITION = 3
WBEM_FLAG_KEYS_ONLY = 4
WBEM_FLAG_REFS_ONLY = 8
WBEM_FLAG_LOCAL_ONLY = 16
WBEM_FLAG_PROPAGATED_ONLY = 32
WBEM_FLAG_SYSTEM_ONLY = 48
WBEM_FLAG_NONSYSTEM_ONLY = 64
WBEM_MASK_CONDITION_ORIGIN = 112
WBEM_FLAG_CLASS_OVERRIDES_ONLY = 256
WBEM_FLAG_CLASS_LOCAL_AND_OVERRIDES = 512
WBEM_MASK_CLASS_CONDITION = 768
WBEM_FLAVOR_TYPE = Int32
WBEM_FLAVOR_DONT_PROPAGATE = 0
WBEM_FLAVOR_FLAG_PROPAGATE_TO_INSTANCE = 1
WBEM_FLAVOR_FLAG_PROPAGATE_TO_DERIVED_CLASS = 2
WBEM_FLAVOR_MASK_PROPAGATION = 15
WBEM_FLAVOR_OVERRIDABLE = 0
WBEM_FLAVOR_NOT_OVERRIDABLE = 16
WBEM_FLAVOR_MASK_PERMISSIONS = 16
WBEM_FLAVOR_ORIGIN_LOCAL = 0
WBEM_FLAVOR_ORIGIN_PROPAGATED = 32
WBEM_FLAVOR_ORIGIN_SYSTEM = 64
WBEM_FLAVOR_MASK_ORIGIN = 96
WBEM_FLAVOR_NOT_AMENDED = 0
WBEM_FLAVOR_AMENDED = 128
WBEM_FLAVOR_MASK_AMENDED = 128
WBEM_QUERY_FLAG_TYPE = Int32
WBEM_FLAG_DEEP = 0
WBEM_FLAG_SHALLOW = 1
WBEM_FLAG_PROTOTYPE = 2
WBEM_SECURITY_FLAGS = Int32
WBEM_ENABLE = 1
WBEM_METHOD_EXECUTE = 2
WBEM_FULL_WRITE_REP = 4
WBEM_PARTIAL_WRITE_REP = 8
WBEM_WRITE_PROVIDER = 16
WBEM_REMOTE_ACCESS = 32
WBEM_RIGHT_SUBSCRIBE = 64
WBEM_RIGHT_PUBLISH = 128
WBEM_LIMITATION_FLAG_TYPE = Int32
WBEM_FLAG_EXCLUDE_OBJECT_QUALIFIERS = 16
WBEM_FLAG_EXCLUDE_PROPERTY_QUALIFIERS = 32
WBEM_TEXT_FLAG_TYPE = Int32
WBEM_FLAG_NO_FLAVORS = 1
WBEM_COMPARISON_FLAG = Int32
WBEM_COMPARISON_INCLUDE_ALL = 0
WBEM_FLAG_IGNORE_QUALIFIERS = 1
WBEM_FLAG_IGNORE_OBJECT_SOURCE = 2
WBEM_FLAG_IGNORE_DEFAULT_VALUES = 4
WBEM_FLAG_IGNORE_CLASS = 8
WBEM_FLAG_IGNORE_CASE = 16
WBEM_FLAG_IGNORE_FLAVOR = 32
WBEM_LOCKING = Int32
WBEM_FLAG_ALLOW_READ = 1
CIMTYPE_ENUMERATION = Int32
CIM_ILLEGAL = 4095
CIM_EMPTY = 0
CIM_SINT8 = 16
CIM_UINT8 = 17
CIM_SINT16 = 2
CIM_UINT16 = 18
CIM_SINT32 = 3
CIM_UINT32 = 19
CIM_SINT64 = 20
CIM_UINT64 = 21
CIM_REAL32 = 4
CIM_REAL64 = 5
CIM_BOOLEAN = 11
CIM_STRING = 8
CIM_DATETIME = 101
CIM_REFERENCE = 102
CIM_CHAR16 = 103
CIM_OBJECT = 13
CIM_FLAG_ARRAY = 8192
WBEM_BACKUP_RESTORE_FLAGS = Int32
WBEM_FLAG_BACKUP_RESTORE_DEFAULT = 0
WBEM_FLAG_BACKUP_RESTORE_FORCE_SHUTDOWN = 1
WBEM_REFRESHER_FLAGS = Int32
WBEM_FLAG_REFRESH_AUTO_RECONNECT = 0
WBEM_FLAG_REFRESH_NO_AUTO_RECONNECT = 1
WBEM_SHUTDOWN_FLAGS = Int32
WBEM_SHUTDOWN_UNLOAD_COMPONENT = 1
WBEM_SHUTDOWN_WMI = 2
WBEM_SHUTDOWN_OS = 3
WBEMSTATUS_FORMAT = Int32
WBEMSTATUS_FORMAT_NEWLINE = 0
WBEMSTATUS_FORMAT_NO_NEWLINE = 1
WBEM_LIMITS = Int32
WBEM_MAX_IDENTIFIER = 4096
WBEM_MAX_QUERY = 16384
WBEM_MAX_PATH = 8192
WBEM_MAX_OBJECT_NESTING = 64
WBEM_MAX_USER_PROPERTIES = 1024
WBEMSTATUS = Int32
WBEM_NO_ERROR = 0
WBEM_S_NO_ERROR = 0
WBEM_S_SAME = 0
WBEM_S_FALSE = 1
WBEM_S_ALREADY_EXISTS = 262145
WBEM_S_RESET_TO_DEFAULT = 262146
WBEM_S_DIFFERENT = 262147
WBEM_S_TIMEDOUT = 262148
WBEM_S_NO_MORE_DATA = 262149
WBEM_S_OPERATION_CANCELLED = 262150
WBEM_S_PENDING = 262151
WBEM_S_DUPLICATE_OBJECTS = 262152
WBEM_S_ACCESS_DENIED = 262153
WBEM_S_PARTIAL_RESULTS = 262160
WBEM_S_SOURCE_NOT_AVAILABLE = 262167
WBEM_E_FAILED = -2147217407
WBEM_E_NOT_FOUND = -2147217406
WBEM_E_ACCESS_DENIED = -2147217405
WBEM_E_PROVIDER_FAILURE = -2147217404
WBEM_E_TYPE_MISMATCH = -2147217403
WBEM_E_OUT_OF_MEMORY = -2147217402
WBEM_E_INVALID_CONTEXT = -2147217401
WBEM_E_INVALID_PARAMETER = -2147217400
WBEM_E_NOT_AVAILABLE = -2147217399
WBEM_E_CRITICAL_ERROR = -2147217398
WBEM_E_INVALID_STREAM = -2147217397
WBEM_E_NOT_SUPPORTED = -2147217396
WBEM_E_INVALID_SUPERCLASS = -2147217395
WBEM_E_INVALID_NAMESPACE = -2147217394
WBEM_E_INVALID_OBJECT = -2147217393
WBEM_E_INVALID_CLASS = -2147217392
WBEM_E_PROVIDER_NOT_FOUND = -2147217391
WBEM_E_INVALID_PROVIDER_REGISTRATION = -2147217390
WBEM_E_PROVIDER_LOAD_FAILURE = -2147217389
WBEM_E_INITIALIZATION_FAILURE = -2147217388
WBEM_E_TRANSPORT_FAILURE = -2147217387
WBEM_E_INVALID_OPERATION = -2147217386
WBEM_E_INVALID_QUERY = -2147217385
WBEM_E_INVALID_QUERY_TYPE = -2147217384
WBEM_E_ALREADY_EXISTS = -2147217383
WBEM_E_OVERRIDE_NOT_ALLOWED = -2147217382
WBEM_E_PROPAGATED_QUALIFIER = -2147217381
WBEM_E_PROPAGATED_PROPERTY = -2147217380
WBEM_E_UNEXPECTED = -2147217379
WBEM_E_ILLEGAL_OPERATION = -2147217378
WBEM_E_CANNOT_BE_KEY = -2147217377
WBEM_E_INCOMPLETE_CLASS = -2147217376
WBEM_E_INVALID_SYNTAX = -2147217375
WBEM_E_NONDECORATED_OBJECT = -2147217374
WBEM_E_READ_ONLY = -2147217373
WBEM_E_PROVIDER_NOT_CAPABLE = -2147217372
WBEM_E_CLASS_HAS_CHILDREN = -2147217371
WBEM_E_CLASS_HAS_INSTANCES = -2147217370
WBEM_E_QUERY_NOT_IMPLEMENTED = -2147217369
WBEM_E_ILLEGAL_NULL = -2147217368
WBEM_E_INVALID_QUALIFIER_TYPE = -2147217367
WBEM_E_INVALID_PROPERTY_TYPE = -2147217366
WBEM_E_VALUE_OUT_OF_RANGE = -2147217365
WBEM_E_CANNOT_BE_SINGLETON = -2147217364
WBEM_E_INVALID_CIM_TYPE = -2147217363
WBEM_E_INVALID_METHOD = -2147217362
WBEM_E_INVALID_METHOD_PARAMETERS = -2147217361
WBEM_E_SYSTEM_PROPERTY = -2147217360
WBEM_E_INVALID_PROPERTY = -2147217359
WBEM_E_CALL_CANCELLED = -2147217358
WBEM_E_SHUTTING_DOWN = -2147217357
WBEM_E_PROPAGATED_METHOD = -2147217356
WBEM_E_UNSUPPORTED_PARAMETER = -2147217355
WBEM_E_MISSING_PARAMETER_ID = -2147217354
WBEM_E_INVALID_PARAMETER_ID = -2147217353
WBEM_E_NONCONSECUTIVE_PARAMETER_IDS = -2147217352
WBEM_E_PARAMETER_ID_ON_RETVAL = -2147217351
WBEM_E_INVALID_OBJECT_PATH = -2147217350
WBEM_E_OUT_OF_DISK_SPACE = -2147217349
WBEM_E_BUFFER_TOO_SMALL = -2147217348
WBEM_E_UNSUPPORTED_PUT_EXTENSION = -2147217347
WBEM_E_UNKNOWN_OBJECT_TYPE = -2147217346
WBEM_E_UNKNOWN_PACKET_TYPE = -2147217345
WBEM_E_MARSHAL_VERSION_MISMATCH = -2147217344
WBEM_E_MARSHAL_INVALID_SIGNATURE = -2147217343
WBEM_E_INVALID_QUALIFIER = -2147217342
WBEM_E_INVALID_DUPLICATE_PARAMETER = -2147217341
WBEM_E_TOO_MUCH_DATA = -2147217340
WBEM_E_SERVER_TOO_BUSY = -2147217339
WBEM_E_INVALID_FLAVOR = -2147217338
WBEM_E_CIRCULAR_REFERENCE = -2147217337
WBEM_E_UNSUPPORTED_CLASS_UPDATE = -2147217336
WBEM_E_CANNOT_CHANGE_KEY_INHERITANCE = -2147217335
WBEM_E_CANNOT_CHANGE_INDEX_INHERITANCE = -2147217328
WBEM_E_TOO_MANY_PROPERTIES = -2147217327
WBEM_E_UPDATE_TYPE_MISMATCH = -2147217326
WBEM_E_UPDATE_OVERRIDE_NOT_ALLOWED = -2147217325
WBEM_E_UPDATE_PROPAGATED_METHOD = -2147217324
WBEM_E_METHOD_NOT_IMPLEMENTED = -2147217323
WBEM_E_METHOD_DISABLED = -2147217322
WBEM_E_REFRESHER_BUSY = -2147217321
WBEM_E_UNPARSABLE_QUERY = -2147217320
WBEM_E_NOT_EVENT_CLASS = -2147217319
WBEM_E_MISSING_GROUP_WITHIN = -2147217318
WBEM_E_MISSING_AGGREGATION_LIST = -2147217317
WBEM_E_PROPERTY_NOT_AN_OBJECT = -2147217316
WBEM_E_AGGREGATING_BY_OBJECT = -2147217315
WBEM_E_UNINTERPRETABLE_PROVIDER_QUERY = -2147217313
WBEM_E_BACKUP_RESTORE_WINMGMT_RUNNING = -2147217312
WBEM_E_QUEUE_OVERFLOW = -2147217311
WBEM_E_PRIVILEGE_NOT_HELD = -2147217310
WBEM_E_INVALID_OPERATOR = -2147217309
WBEM_E_LOCAL_CREDENTIALS = -2147217308
WBEM_E_CANNOT_BE_ABSTRACT = -2147217307
WBEM_E_AMENDED_OBJECT = -2147217306
WBEM_E_CLIENT_TOO_SLOW = -2147217305
WBEM_E_NULL_SECURITY_DESCRIPTOR = -2147217304
WBEM_E_TIMED_OUT = -2147217303
WBEM_E_INVALID_ASSOCIATION = -2147217302
WBEM_E_AMBIGUOUS_OPERATION = -2147217301
WBEM_E_QUOTA_VIOLATION = -2147217300
WBEM_E_RESERVED_001 = -2147217299
WBEM_E_RESERVED_002 = -2147217298
WBEM_E_UNSUPPORTED_LOCALE = -2147217297
WBEM_E_HANDLE_OUT_OF_DATE = -2147217296
WBEM_E_CONNECTION_FAILED = -2147217295
WBEM_E_INVALID_HANDLE_REQUEST = -2147217294
WBEM_E_PROPERTY_NAME_TOO_WIDE = -2147217293
WBEM_E_CLASS_NAME_TOO_WIDE = -2147217292
WBEM_E_METHOD_NAME_TOO_WIDE = -2147217291
WBEM_E_QUALIFIER_NAME_TOO_WIDE = -2147217290
WBEM_E_RERUN_COMMAND = -2147217289
WBEM_E_DATABASE_VER_MISMATCH = -2147217288
WBEM_E_VETO_DELETE = -2147217287
WBEM_E_VETO_PUT = -2147217286
WBEM_E_INVALID_LOCALE = -2147217280
WBEM_E_PROVIDER_SUSPENDED = -2147217279
WBEM_E_SYNCHRONIZATION_REQUIRED = -2147217278
WBEM_E_NO_SCHEMA = -2147217277
WBEM_E_PROVIDER_ALREADY_REGISTERED = -2147217276
WBEM_E_PROVIDER_NOT_REGISTERED = -2147217275
WBEM_E_FATAL_TRANSPORT_ERROR = -2147217274
WBEM_E_ENCRYPTED_CONNECTION_REQUIRED = -2147217273
WBEM_E_PROVIDER_TIMED_OUT = -2147217272
WBEM_E_NO_KEY = -2147217271
WBEM_E_PROVIDER_DISABLED = -2147217270
WBEMESS_E_REGISTRATION_TOO_BROAD = -2147213311
WBEMESS_E_REGISTRATION_TOO_PRECISE = -2147213310
WBEMESS_E_AUTHZ_NOT_PRIVILEGED = -2147213309
WBEMMOF_E_EXPECTED_QUALIFIER_NAME = -2147205119
WBEMMOF_E_EXPECTED_SEMI = -2147205118
WBEMMOF_E_EXPECTED_OPEN_BRACE = -2147205117
WBEMMOF_E_EXPECTED_CLOSE_BRACE = -2147205116
WBEMMOF_E_EXPECTED_CLOSE_BRACKET = -2147205115
WBEMMOF_E_EXPECTED_CLOSE_PAREN = -2147205114
WBEMMOF_E_ILLEGAL_CONSTANT_VALUE = -2147205113
WBEMMOF_E_EXPECTED_TYPE_IDENTIFIER = -2147205112
WBEMMOF_E_EXPECTED_OPEN_PAREN = -2147205111
WBEMMOF_E_UNRECOGNIZED_TOKEN = -2147205110
WBEMMOF_E_UNRECOGNIZED_TYPE = -2147205109
WBEMMOF_E_EXPECTED_PROPERTY_NAME = -2147205108
WBEMMOF_E_TYPEDEF_NOT_SUPPORTED = -2147205107
WBEMMOF_E_UNEXPECTED_ALIAS = -2147205106
WBEMMOF_E_UNEXPECTED_ARRAY_INIT = -2147205105
WBEMMOF_E_INVALID_AMENDMENT_SYNTAX = -2147205104
WBEMMOF_E_INVALID_DUPLICATE_AMENDMENT = -2147205103
WBEMMOF_E_INVALID_PRAGMA = -2147205102
WBEMMOF_E_INVALID_NAMESPACE_SYNTAX = -2147205101
WBEMMOF_E_EXPECTED_CLASS_NAME = -2147205100
WBEMMOF_E_TYPE_MISMATCH = -2147205099
WBEMMOF_E_EXPECTED_ALIAS_NAME = -2147205098
WBEMMOF_E_INVALID_CLASS_DECLARATION = -2147205097
WBEMMOF_E_INVALID_INSTANCE_DECLARATION = -2147205096
WBEMMOF_E_EXPECTED_DOLLAR = -2147205095
WBEMMOF_E_CIMTYPE_QUALIFIER = -2147205094
WBEMMOF_E_DUPLICATE_PROPERTY = -2147205093
WBEMMOF_E_INVALID_NAMESPACE_SPECIFICATION = -2147205092
WBEMMOF_E_OUT_OF_RANGE = -2147205091
WBEMMOF_E_INVALID_FILE = -2147205090
WBEMMOF_E_ALIASES_IN_EMBEDDED = -2147205089
WBEMMOF_E_NULL_ARRAY_ELEM = -2147205088
WBEMMOF_E_DUPLICATE_QUALIFIER = -2147205087
WBEMMOF_E_EXPECTED_FLAVOR_TYPE = -2147205086
WBEMMOF_E_INCOMPATIBLE_FLAVOR_TYPES = -2147205085
WBEMMOF_E_MULTIPLE_ALIASES = -2147205084
WBEMMOF_E_INCOMPATIBLE_FLAVOR_TYPES2 = -2147205083
WBEMMOF_E_NO_ARRAYS_RETURNED = -2147205082
WBEMMOF_E_MUST_BE_IN_OR_OUT = -2147205081
WBEMMOF_E_INVALID_FLAGS_SYNTAX = -2147205080
WBEMMOF_E_EXPECTED_BRACE_OR_BAD_TYPE = -2147205079
WBEMMOF_E_UNSUPPORTED_CIMV22_QUAL_VALUE = -2147205078
WBEMMOF_E_UNSUPPORTED_CIMV22_DATA_TYPE = -2147205077
WBEMMOF_E_INVALID_DELETEINSTANCE_SYNTAX = -2147205076
WBEMMOF_E_INVALID_QUALIFIER_SYNTAX = -2147205075
WBEMMOF_E_QUALIFIER_USED_OUTSIDE_SCOPE = -2147205074
WBEMMOF_E_ERROR_CREATING_TEMP_FILE = -2147205073
WBEMMOF_E_ERROR_INVALID_INCLUDE_FILE = -2147205072
WBEMMOF_E_INVALID_DELETECLASS_SYNTAX = -2147205071
def _define_IWbemClassObject_head():
    class IWbemClassObject(win32more.System.Com.IUnknown_head):
        Guid = Guid('dc12a681-737f-11cf-884d-00aa004b2e24')
    return IWbemClassObject
def _define_IWbemClassObject():
    IWbemClassObject = win32more.System.Wmi.IWbemClassObject_head
    IWbemClassObject.GetQualifierSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.IWbemQualifierSet_head), use_last_error=False)(3, 'GetQualifierSet', ((1, 'ppQualSet'),)))
    IWbemClassObject.Get = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Int32,POINTER(win32more.System.Com.VARIANT_head),POINTER(Int32),POINTER(Int32), use_last_error=False)(4, 'Get', ((1, 'wszName'),(1, 'lFlags'),(1, 'pVal'),(1, 'pType'),(1, 'plFlavor'),)))
    IWbemClassObject.Put = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Int32,POINTER(win32more.System.Com.VARIANT_head),Int32, use_last_error=False)(5, 'Put', ((1, 'wszName'),(1, 'lFlags'),(1, 'pVal'),(1, 'Type'),)))
    IWbemClassObject.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(6, 'Delete', ((1, 'wszName'),)))
    IWbemClassObject.GetNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Int32,POINTER(win32more.System.Com.VARIANT_head),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(7, 'GetNames', ((1, 'wszQualifierName'),(1, 'lFlags'),(1, 'pQualifierVal'),(1, 'pNames'),)))
    IWbemClassObject.BeginEnumeration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(8, 'BeginEnumeration', ((1, 'lEnumFlags'),)))
    IWbemClassObject.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR),POINTER(win32more.System.Com.VARIANT_head),POINTER(Int32),POINTER(Int32), use_last_error=False)(9, 'Next', ((1, 'lFlags'),(1, 'strName'),(1, 'pVal'),(1, 'pType'),(1, 'plFlavor'),)))
    IWbemClassObject.EndEnumeration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'EndEnumeration', ()))
    IWbemClassObject.GetPropertyQualifierSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Wmi.IWbemQualifierSet_head), use_last_error=False)(11, 'GetPropertyQualifierSet', ((1, 'wszProperty'),(1, 'ppQualSet'),)))
    IWbemClassObject.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.IWbemClassObject_head), use_last_error=False)(12, 'Clone', ((1, 'ppCopy'),)))
    IWbemClassObject.GetObjectText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'GetObjectText', ((1, 'lFlags'),(1, 'pstrObjectText'),)))
    IWbemClassObject.SpawnDerivedClass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Wmi.IWbemClassObject_head), use_last_error=False)(14, 'SpawnDerivedClass', ((1, 'lFlags'),(1, 'ppNewClass'),)))
    IWbemClassObject.SpawnInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Wmi.IWbemClassObject_head), use_last_error=False)(15, 'SpawnInstance', ((1, 'lFlags'),(1, 'ppNewInstance'),)))
    IWbemClassObject.CompareTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Wmi.IWbemClassObject_head, use_last_error=False)(16, 'CompareTo', ((1, 'lFlags'),(1, 'pCompareTo'),)))
    IWbemClassObject.GetPropertyOrigin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(17, 'GetPropertyOrigin', ((1, 'wszName'),(1, 'pstrClassName'),)))
    IWbemClassObject.InheritsFrom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(18, 'InheritsFrom', ((1, 'strAncestor'),)))
    IWbemClassObject.GetMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Int32,POINTER(win32more.System.Wmi.IWbemClassObject_head),POINTER(win32more.System.Wmi.IWbemClassObject_head), use_last_error=False)(19, 'GetMethod', ((1, 'wszName'),(1, 'lFlags'),(1, 'ppInSignature'),(1, 'ppOutSignature'),)))
    IWbemClassObject.PutMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Int32,win32more.System.Wmi.IWbemClassObject_head,win32more.System.Wmi.IWbemClassObject_head, use_last_error=False)(20, 'PutMethod', ((1, 'wszName'),(1, 'lFlags'),(1, 'pInSignature'),(1, 'pOutSignature'),)))
    IWbemClassObject.DeleteMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(21, 'DeleteMethod', ((1, 'wszName'),)))
    IWbemClassObject.BeginMethodEnumeration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(22, 'BeginMethodEnumeration', ((1, 'lEnumFlags'),)))
    IWbemClassObject.NextMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR),POINTER(win32more.System.Wmi.IWbemClassObject_head),POINTER(win32more.System.Wmi.IWbemClassObject_head), use_last_error=False)(23, 'NextMethod', ((1, 'lFlags'),(1, 'pstrName'),(1, 'ppInSignature'),(1, 'ppOutSignature'),)))
    IWbemClassObject.EndMethodEnumeration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(24, 'EndMethodEnumeration', ()))
    IWbemClassObject.GetMethodQualifierSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Wmi.IWbemQualifierSet_head), use_last_error=False)(25, 'GetMethodQualifierSet', ((1, 'wszMethod'),(1, 'ppQualSet'),)))
    IWbemClassObject.GetMethodOrigin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BSTR), use_last_error=False)(26, 'GetMethodOrigin', ((1, 'wszMethodName'),(1, 'pstrClassName'),)))
    return IWbemClassObject
def _define_IWbemObjectAccess_head():
    class IWbemObjectAccess(win32more.System.Wmi.IWbemClassObject_head):
        Guid = Guid('49353c9a-516b-11d1-aea6-00c04fb68820')
    return IWbemObjectAccess
def _define_IWbemObjectAccess():
    IWbemObjectAccess = win32more.System.Wmi.IWbemObjectAccess_head
    IWbemObjectAccess.GetPropertyHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Int32),POINTER(Int32), use_last_error=False)(27, 'GetPropertyHandle', ((1, 'wszPropertyName'),(1, 'pType'),(1, 'plHandle'),)))
    IWbemObjectAccess.WritePropertyValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(Byte), use_last_error=False)(28, 'WritePropertyValue', ((1, 'lHandle'),(1, 'lNumBytes'),(1, 'aData'),)))
    IWbemObjectAccess.ReadPropertyValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(Int32),POINTER(Byte), use_last_error=False)(29, 'ReadPropertyValue', ((1, 'lHandle'),(1, 'lBufferSize'),(1, 'plNumBytes'),(1, 'aData'),)))
    IWbemObjectAccess.ReadDWORD = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(UInt32), use_last_error=False)(30, 'ReadDWORD', ((1, 'lHandle'),(1, 'pdw'),)))
    IWbemObjectAccess.WriteDWORD = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,UInt32, use_last_error=False)(31, 'WriteDWORD', ((1, 'lHandle'),(1, 'dw'),)))
    IWbemObjectAccess.ReadQWORD = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(UInt64), use_last_error=False)(32, 'ReadQWORD', ((1, 'lHandle'),(1, 'pqw'),)))
    IWbemObjectAccess.WriteQWORD = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,UInt64, use_last_error=False)(33, 'WriteQWORD', ((1, 'lHandle'),(1, 'pw'),)))
    IWbemObjectAccess.GetPropertyInfoByHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR),POINTER(Int32), use_last_error=False)(34, 'GetPropertyInfoByHandle', ((1, 'lHandle'),(1, 'pstrName'),(1, 'pType'),)))
    IWbemObjectAccess.Lock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(35, 'Lock', ((1, 'lFlags'),)))
    IWbemObjectAccess.Unlock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(36, 'Unlock', ((1, 'lFlags'),)))
    return IWbemObjectAccess
def _define_IWbemQualifierSet_head():
    class IWbemQualifierSet(win32more.System.Com.IUnknown_head):
        Guid = Guid('dc12a680-737f-11cf-884d-00aa004b2e24')
    return IWbemQualifierSet
def _define_IWbemQualifierSet():
    IWbemQualifierSet = win32more.System.Wmi.IWbemQualifierSet_head
    IWbemQualifierSet.Get = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Int32,POINTER(win32more.System.Com.VARIANT_head),POINTER(Int32), use_last_error=False)(3, 'Get', ((1, 'wszName'),(1, 'lFlags'),(1, 'pVal'),(1, 'plFlavor'),)))
    IWbemQualifierSet.Put = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.VARIANT_head),Int32, use_last_error=False)(4, 'Put', ((1, 'wszName'),(1, 'pVal'),(1, 'lFlavor'),)))
    IWbemQualifierSet.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(5, 'Delete', ((1, 'wszName'),)))
    IWbemQualifierSet.GetNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(6, 'GetNames', ((1, 'lFlags'),(1, 'pNames'),)))
    IWbemQualifierSet.BeginEnumeration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(7, 'BeginEnumeration', ((1, 'lFlags'),)))
    IWbemQualifierSet.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR),POINTER(win32more.System.Com.VARIANT_head),POINTER(Int32), use_last_error=False)(8, 'Next', ((1, 'lFlags'),(1, 'pstrName'),(1, 'pVal'),(1, 'plFlavor'),)))
    IWbemQualifierSet.EndEnumeration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'EndEnumeration', ()))
    return IWbemQualifierSet
def _define_IWbemServices_head():
    class IWbemServices(win32more.System.Com.IUnknown_head):
        Guid = Guid('9556dc99-828c-11cf-a37e-00aa003240c7')
    return IWbemServices
def _define_IWbemServices():
    IWbemServices = win32more.System.Wmi.IWbemServices_head
    IWbemServices.OpenNamespace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.System.Wmi.IWbemContext_head,POINTER(win32more.System.Wmi.IWbemServices_head),POINTER(win32more.System.Wmi.IWbemCallResult_head), use_last_error=False)(3, 'OpenNamespace', ((1, 'strNamespace'),(1, 'lFlags'),(1, 'pCtx'),(1, 'ppWorkingNamespace'),(1, 'ppResult'),)))
    IWbemServices.CancelAsyncCall = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Wmi.IWbemObjectSink_head, use_last_error=False)(4, 'CancelAsyncCall', ((1, 'pSink'),)))
    IWbemServices.QueryObjectSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Wmi.IWbemObjectSink_head), use_last_error=False)(5, 'QueryObjectSink', ((1, 'lFlags'),(1, 'ppResponseHandler'),)))
    IWbemServices.GetObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.System.Wmi.IWbemContext_head,POINTER(win32more.System.Wmi.IWbemClassObject_head),POINTER(win32more.System.Wmi.IWbemCallResult_head), use_last_error=False)(6, 'GetObject', ((1, 'strObjectPath'),(1, 'lFlags'),(1, 'pCtx'),(1, 'ppObject'),(1, 'ppCallResult'),)))
    IWbemServices.GetObjectAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.System.Wmi.IWbemContext_head,win32more.System.Wmi.IWbemObjectSink_head, use_last_error=False)(7, 'GetObjectAsync', ((1, 'strObjectPath'),(1, 'lFlags'),(1, 'pCtx'),(1, 'pResponseHandler'),)))
    IWbemServices.PutClass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Wmi.IWbemClassObject_head,Int32,win32more.System.Wmi.IWbemContext_head,POINTER(win32more.System.Wmi.IWbemCallResult_head), use_last_error=False)(8, 'PutClass', ((1, 'pObject'),(1, 'lFlags'),(1, 'pCtx'),(1, 'ppCallResult'),)))
    IWbemServices.PutClassAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Wmi.IWbemClassObject_head,Int32,win32more.System.Wmi.IWbemContext_head,win32more.System.Wmi.IWbemObjectSink_head, use_last_error=False)(9, 'PutClassAsync', ((1, 'pObject'),(1, 'lFlags'),(1, 'pCtx'),(1, 'pResponseHandler'),)))
    IWbemServices.DeleteClass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.System.Wmi.IWbemContext_head,POINTER(win32more.System.Wmi.IWbemCallResult_head), use_last_error=False)(10, 'DeleteClass', ((1, 'strClass'),(1, 'lFlags'),(1, 'pCtx'),(1, 'ppCallResult'),)))
    IWbemServices.DeleteClassAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.System.Wmi.IWbemContext_head,win32more.System.Wmi.IWbemObjectSink_head, use_last_error=False)(11, 'DeleteClassAsync', ((1, 'strClass'),(1, 'lFlags'),(1, 'pCtx'),(1, 'pResponseHandler'),)))
    IWbemServices.CreateClassEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.System.Wmi.IWbemContext_head,POINTER(win32more.System.Wmi.IEnumWbemClassObject_head), use_last_error=False)(12, 'CreateClassEnum', ((1, 'strSuperclass'),(1, 'lFlags'),(1, 'pCtx'),(1, 'ppEnum'),)))
    IWbemServices.CreateClassEnumAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.System.Wmi.IWbemContext_head,win32more.System.Wmi.IWbemObjectSink_head, use_last_error=False)(13, 'CreateClassEnumAsync', ((1, 'strSuperclass'),(1, 'lFlags'),(1, 'pCtx'),(1, 'pResponseHandler'),)))
    IWbemServices.PutInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Wmi.IWbemClassObject_head,Int32,win32more.System.Wmi.IWbemContext_head,POINTER(win32more.System.Wmi.IWbemCallResult_head), use_last_error=False)(14, 'PutInstance', ((1, 'pInst'),(1, 'lFlags'),(1, 'pCtx'),(1, 'ppCallResult'),)))
    IWbemServices.PutInstanceAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Wmi.IWbemClassObject_head,Int32,win32more.System.Wmi.IWbemContext_head,win32more.System.Wmi.IWbemObjectSink_head, use_last_error=False)(15, 'PutInstanceAsync', ((1, 'pInst'),(1, 'lFlags'),(1, 'pCtx'),(1, 'pResponseHandler'),)))
    IWbemServices.DeleteInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.System.Wmi.IWbemContext_head,POINTER(win32more.System.Wmi.IWbemCallResult_head), use_last_error=False)(16, 'DeleteInstance', ((1, 'strObjectPath'),(1, 'lFlags'),(1, 'pCtx'),(1, 'ppCallResult'),)))
    IWbemServices.DeleteInstanceAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.System.Wmi.IWbemContext_head,win32more.System.Wmi.IWbemObjectSink_head, use_last_error=False)(17, 'DeleteInstanceAsync', ((1, 'strObjectPath'),(1, 'lFlags'),(1, 'pCtx'),(1, 'pResponseHandler'),)))
    IWbemServices.CreateInstanceEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.System.Wmi.IWbemContext_head,POINTER(win32more.System.Wmi.IEnumWbemClassObject_head), use_last_error=False)(18, 'CreateInstanceEnum', ((1, 'strFilter'),(1, 'lFlags'),(1, 'pCtx'),(1, 'ppEnum'),)))
    IWbemServices.CreateInstanceEnumAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.System.Wmi.IWbemContext_head,win32more.System.Wmi.IWbemObjectSink_head, use_last_error=False)(19, 'CreateInstanceEnumAsync', ((1, 'strFilter'),(1, 'lFlags'),(1, 'pCtx'),(1, 'pResponseHandler'),)))
    IWbemServices.ExecQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,win32more.System.Wmi.IWbemContext_head,POINTER(win32more.System.Wmi.IEnumWbemClassObject_head), use_last_error=False)(20, 'ExecQuery', ((1, 'strQueryLanguage'),(1, 'strQuery'),(1, 'lFlags'),(1, 'pCtx'),(1, 'ppEnum'),)))
    IWbemServices.ExecQueryAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,win32more.System.Wmi.IWbemContext_head,win32more.System.Wmi.IWbemObjectSink_head, use_last_error=False)(21, 'ExecQueryAsync', ((1, 'strQueryLanguage'),(1, 'strQuery'),(1, 'lFlags'),(1, 'pCtx'),(1, 'pResponseHandler'),)))
    IWbemServices.ExecNotificationQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,win32more.System.Wmi.IWbemContext_head,POINTER(win32more.System.Wmi.IEnumWbemClassObject_head), use_last_error=False)(22, 'ExecNotificationQuery', ((1, 'strQueryLanguage'),(1, 'strQuery'),(1, 'lFlags'),(1, 'pCtx'),(1, 'ppEnum'),)))
    IWbemServices.ExecNotificationQueryAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,win32more.System.Wmi.IWbemContext_head,win32more.System.Wmi.IWbemObjectSink_head, use_last_error=False)(23, 'ExecNotificationQueryAsync', ((1, 'strQueryLanguage'),(1, 'strQuery'),(1, 'lFlags'),(1, 'pCtx'),(1, 'pResponseHandler'),)))
    IWbemServices.ExecMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,win32more.System.Wmi.IWbemContext_head,win32more.System.Wmi.IWbemClassObject_head,POINTER(win32more.System.Wmi.IWbemClassObject_head),POINTER(win32more.System.Wmi.IWbemCallResult_head), use_last_error=False)(24, 'ExecMethod', ((1, 'strObjectPath'),(1, 'strMethodName'),(1, 'lFlags'),(1, 'pCtx'),(1, 'pInParams'),(1, 'ppOutParams'),(1, 'ppCallResult'),)))
    IWbemServices.ExecMethodAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,win32more.System.Wmi.IWbemContext_head,win32more.System.Wmi.IWbemClassObject_head,win32more.System.Wmi.IWbemObjectSink_head, use_last_error=False)(25, 'ExecMethodAsync', ((1, 'strObjectPath'),(1, 'strMethodName'),(1, 'lFlags'),(1, 'pCtx'),(1, 'pInParams'),(1, 'pResponseHandler'),)))
    return IWbemServices
def _define_IWbemLocator_head():
    class IWbemLocator(win32more.System.Com.IUnknown_head):
        Guid = Guid('dc12a687-737f-11cf-884d-00aa004b2e24')
    return IWbemLocator
def _define_IWbemLocator():
    IWbemLocator = win32more.System.Wmi.IWbemLocator_head
    IWbemLocator.ConnectServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,win32more.Foundation.BSTR,win32more.System.Wmi.IWbemContext_head,POINTER(win32more.System.Wmi.IWbemServices_head), use_last_error=False)(3, 'ConnectServer', ((1, 'strNetworkResource'),(1, 'strUser'),(1, 'strPassword'),(1, 'strLocale'),(1, 'lSecurityFlags'),(1, 'strAuthority'),(1, 'pCtx'),(1, 'ppNamespace'),)))
    return IWbemLocator
def _define_IWbemObjectSink_head():
    class IWbemObjectSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('7c857801-7381-11cf-884d-00aa004b2e24')
    return IWbemObjectSink
def _define_IWbemObjectSink():
    IWbemObjectSink = win32more.System.Wmi.IWbemObjectSink_head
    IWbemObjectSink.Indicate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Wmi.IWbemClassObject_head), use_last_error=False)(3, 'Indicate', ((1, 'lObjectCount'),(1, 'apObjArray'),)))
    IWbemObjectSink.SetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Wmi.IWbemClassObject_head, use_last_error=False)(4, 'SetStatus', ((1, 'lFlags'),(1, 'hResult'),(1, 'strParam'),(1, 'pObjParam'),)))
    return IWbemObjectSink
def _define_IEnumWbemClassObject_head():
    class IEnumWbemClassObject(win32more.System.Com.IUnknown_head):
        Guid = Guid('027947e1-d731-11ce-a357-000000000001')
    return IEnumWbemClassObject
def _define_IEnumWbemClassObject():
    IEnumWbemClassObject = win32more.System.Wmi.IEnumWbemClassObject_head
    IEnumWbemClassObject.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Reset', ()))
    IEnumWbemClassObject.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,UInt32,POINTER(win32more.System.Wmi.IWbemClassObject_head),POINTER(UInt32), use_last_error=False)(4, 'Next', ((1, 'lTimeout'),(1, 'uCount'),(1, 'apObjects'),(1, 'puReturned'),)))
    IEnumWbemClassObject.NextAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.Wmi.IWbemObjectSink_head, use_last_error=False)(5, 'NextAsync', ((1, 'uCount'),(1, 'pSink'),)))
    IEnumWbemClassObject.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.IEnumWbemClassObject_head), use_last_error=False)(6, 'Clone', ((1, 'ppEnum'),)))
    IEnumWbemClassObject.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,UInt32, use_last_error=False)(7, 'Skip', ((1, 'lTimeout'),(1, 'nCount'),)))
    return IEnumWbemClassObject
def _define_IWbemCallResult_head():
    class IWbemCallResult(win32more.System.Com.IUnknown_head):
        Guid = Guid('44aca675-e8fc-11d0-a07c-00c04fb68820')
    return IWbemCallResult
def _define_IWbemCallResult():
    IWbemCallResult = win32more.System.Wmi.IWbemCallResult_head
    IWbemCallResult.GetResultObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Wmi.IWbemClassObject_head), use_last_error=False)(3, 'GetResultObject', ((1, 'lTimeout'),(1, 'ppResultObject'),)))
    IWbemCallResult.GetResultString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'GetResultString', ((1, 'lTimeout'),(1, 'pstrResultString'),)))
    IWbemCallResult.GetResultServices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Wmi.IWbemServices_head), use_last_error=False)(5, 'GetResultServices', ((1, 'lTimeout'),(1, 'ppServices'),)))
    IWbemCallResult.GetCallStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int32), use_last_error=False)(6, 'GetCallStatus', ((1, 'lTimeout'),(1, 'plStatus'),)))
    return IWbemCallResult
def _define_IWbemContext_head():
    class IWbemContext(win32more.System.Com.IUnknown_head):
        Guid = Guid('44aca674-e8fc-11d0-a07c-00c04fb68820')
    return IWbemContext
def _define_IWbemContext():
    IWbemContext = win32more.System.Wmi.IWbemContext_head
    IWbemContext.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.IWbemContext_head), use_last_error=False)(3, 'Clone', ((1, 'ppNewCopy'),)))
    IWbemContext.GetNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(4, 'GetNames', ((1, 'lFlags'),(1, 'pNames'),)))
    IWbemContext.BeginEnumeration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(5, 'BeginEnumeration', ((1, 'lFlags'),)))
    IWbemContext.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(6, 'Next', ((1, 'lFlags'),(1, 'pstrName'),(1, 'pValue'),)))
    IWbemContext.EndEnumeration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'EndEnumeration', ()))
    IWbemContext.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(8, 'SetValue', ((1, 'wszName'),(1, 'lFlags'),(1, 'pValue'),)))
    IWbemContext.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(9, 'GetValue', ((1, 'wszName'),(1, 'lFlags'),(1, 'pValue'),)))
    IWbemContext.DeleteValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Int32, use_last_error=False)(10, 'DeleteValue', ((1, 'wszName'),(1, 'lFlags'),)))
    IWbemContext.DeleteAll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'DeleteAll', ()))
    return IWbemContext
def _define_IUnsecuredApartment_head():
    class IUnsecuredApartment(win32more.System.Com.IUnknown_head):
        Guid = Guid('1cfaba8c-1523-11d1-ad79-00c04fd8fdff')
    return IUnsecuredApartment
def _define_IUnsecuredApartment():
    IUnsecuredApartment = win32more.System.Wmi.IUnsecuredApartment_head
    IUnsecuredApartment.CreateObjectStub = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(3, 'CreateObjectStub', ((1, 'pObject'),(1, 'ppStub'),)))
    return IUnsecuredApartment
def _define_IWbemUnsecuredApartment_head():
    class IWbemUnsecuredApartment(win32more.System.Wmi.IUnsecuredApartment_head):
        Guid = Guid('31739d04-3471-4cf4-9a7c-57a44ae71956')
    return IWbemUnsecuredApartment
def _define_IWbemUnsecuredApartment():
    IWbemUnsecuredApartment = win32more.System.Wmi.IWbemUnsecuredApartment_head
    IWbemUnsecuredApartment.CreateSinkStub = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Wmi.IWbemObjectSink_head,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.System.Wmi.IWbemObjectSink_head), use_last_error=False)(4, 'CreateSinkStub', ((1, 'pSink'),(1, 'dwFlags'),(1, 'wszReserved'),(1, 'ppStub'),)))
    return IWbemUnsecuredApartment
def _define_IWbemStatusCodeText_head():
    class IWbemStatusCodeText(win32more.System.Com.IUnknown_head):
        Guid = Guid('eb87e1bc-3233-11d2-aec9-00c04fb68820')
    return IWbemStatusCodeText
def _define_IWbemStatusCodeText():
    IWbemStatusCodeText = win32more.System.Wmi.IWbemStatusCodeText_head
    IWbemStatusCodeText.GetErrorCodeText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,UInt32,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'GetErrorCodeText', ((1, 'hRes'),(1, 'LocaleId'),(1, 'lFlags'),(1, 'MessageText'),)))
    IWbemStatusCodeText.GetFacilityCodeText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,UInt32,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'GetFacilityCodeText', ((1, 'hRes'),(1, 'LocaleId'),(1, 'lFlags'),(1, 'MessageText'),)))
    return IWbemStatusCodeText
def _define_IWbemBackupRestore_head():
    class IWbemBackupRestore(win32more.System.Com.IUnknown_head):
        Guid = Guid('c49e32c7-bc8b-11d2-85d4-00105a1f8304')
    return IWbemBackupRestore
def _define_IWbemBackupRestore():
    IWbemBackupRestore = win32more.System.Wmi.IWbemBackupRestore_head
    IWbemBackupRestore.Backup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Int32, use_last_error=False)(3, 'Backup', ((1, 'strBackupToFile'),(1, 'lFlags'),)))
    IWbemBackupRestore.Restore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Int32, use_last_error=False)(4, 'Restore', ((1, 'strRestoreFromFile'),(1, 'lFlags'),)))
    return IWbemBackupRestore
def _define_IWbemBackupRestoreEx_head():
    class IWbemBackupRestoreEx(win32more.System.Wmi.IWbemBackupRestore_head):
        Guid = Guid('a359dec5-e813-4834-8a2a-ba7f1d777d76')
    return IWbemBackupRestoreEx
def _define_IWbemBackupRestoreEx():
    IWbemBackupRestoreEx = win32more.System.Wmi.IWbemBackupRestoreEx_head
    IWbemBackupRestoreEx.Pause = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Pause', ()))
    IWbemBackupRestoreEx.Resume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'Resume', ()))
    return IWbemBackupRestoreEx
def _define_IWbemRefresher_head():
    class IWbemRefresher(win32more.System.Com.IUnknown_head):
        Guid = Guid('49353c99-516b-11d1-aea6-00c04fb68820')
    return IWbemRefresher
def _define_IWbemRefresher():
    IWbemRefresher = win32more.System.Wmi.IWbemRefresher_head
    IWbemRefresher.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(3, 'Refresh', ((1, 'lFlags'),)))
    return IWbemRefresher
def _define_IWbemHiPerfEnum_head():
    class IWbemHiPerfEnum(win32more.System.Com.IUnknown_head):
        Guid = Guid('2705c288-79ae-11d2-b348-00105a1f8177')
    return IWbemHiPerfEnum
def _define_IWbemHiPerfEnum():
    IWbemHiPerfEnum = win32more.System.Wmi.IWbemHiPerfEnum_head
    IWbemHiPerfEnum.AddObjects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,UInt32,POINTER(Int32),POINTER(win32more.System.Wmi.IWbemObjectAccess_head), use_last_error=False)(3, 'AddObjects', ((1, 'lFlags'),(1, 'uNumObjects'),(1, 'apIds'),(1, 'apObj'),)))
    IWbemHiPerfEnum.RemoveObjects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,UInt32,POINTER(Int32), use_last_error=False)(4, 'RemoveObjects', ((1, 'lFlags'),(1, 'uNumObjects'),(1, 'apIds'),)))
    IWbemHiPerfEnum.GetObjects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,UInt32,POINTER(win32more.System.Wmi.IWbemObjectAccess_head),POINTER(UInt32), use_last_error=False)(5, 'GetObjects', ((1, 'lFlags'),(1, 'uNumObjects'),(1, 'apObj'),(1, 'puReturned'),)))
    IWbemHiPerfEnum.RemoveAll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(6, 'RemoveAll', ((1, 'lFlags'),)))
    return IWbemHiPerfEnum
def _define_IWbemConfigureRefresher_head():
    class IWbemConfigureRefresher(win32more.System.Com.IUnknown_head):
        Guid = Guid('49353c92-516b-11d1-aea6-00c04fb68820')
    return IWbemConfigureRefresher
def _define_IWbemConfigureRefresher():
    IWbemConfigureRefresher = win32more.System.Wmi.IWbemConfigureRefresher_head
    IWbemConfigureRefresher.AddObjectByPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Wmi.IWbemServices_head,win32more.Foundation.PWSTR,Int32,win32more.System.Wmi.IWbemContext_head,POINTER(win32more.System.Wmi.IWbemClassObject_head),POINTER(Int32), use_last_error=False)(3, 'AddObjectByPath', ((1, 'pNamespace'),(1, 'wszPath'),(1, 'lFlags'),(1, 'pContext'),(1, 'ppRefreshable'),(1, 'plId'),)))
    IWbemConfigureRefresher.AddObjectByTemplate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Wmi.IWbemServices_head,win32more.System.Wmi.IWbemClassObject_head,Int32,win32more.System.Wmi.IWbemContext_head,POINTER(win32more.System.Wmi.IWbemClassObject_head),POINTER(Int32), use_last_error=False)(4, 'AddObjectByTemplate', ((1, 'pNamespace'),(1, 'pTemplate'),(1, 'lFlags'),(1, 'pContext'),(1, 'ppRefreshable'),(1, 'plId'),)))
    IWbemConfigureRefresher.AddRefresher = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Wmi.IWbemRefresher_head,Int32,POINTER(Int32), use_last_error=False)(5, 'AddRefresher', ((1, 'pRefresher'),(1, 'lFlags'),(1, 'plId'),)))
    IWbemConfigureRefresher.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(6, 'Remove', ((1, 'lId'),(1, 'lFlags'),)))
    IWbemConfigureRefresher.AddEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Wmi.IWbemServices_head,win32more.Foundation.PWSTR,Int32,win32more.System.Wmi.IWbemContext_head,POINTER(win32more.System.Wmi.IWbemHiPerfEnum_head),POINTER(Int32), use_last_error=False)(7, 'AddEnum', ((1, 'pNamespace'),(1, 'wszClassName'),(1, 'lFlags'),(1, 'pContext'),(1, 'ppEnum'),(1, 'plId'),)))
    return IWbemConfigureRefresher
def _define_IWbemObjectSinkEx_head():
    class IWbemObjectSinkEx(win32more.System.Wmi.IWbemObjectSink_head):
        Guid = Guid('e7d35cfa-348b-485e-b524-252725d697ca')
    return IWbemObjectSinkEx
def _define_IWbemObjectSinkEx():
    IWbemObjectSinkEx = win32more.System.Wmi.IWbemObjectSinkEx_head
    IWbemObjectSinkEx.WriteMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.BSTR, use_last_error=False)(5, 'WriteMessage', ((1, 'uChannel'),(1, 'strMessage'),)))
    IWbemObjectSinkEx.WriteError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Wmi.IWbemClassObject_head,c_char_p_no, use_last_error=False)(6, 'WriteError', ((1, 'pObjError'),(1, 'puReturned'),)))
    IWbemObjectSinkEx.PromptUser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Byte,c_char_p_no, use_last_error=False)(7, 'PromptUser', ((1, 'strMessage'),(1, 'uPromptType'),(1, 'puReturned'),)))
    IWbemObjectSinkEx.WriteProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,UInt32,UInt32, use_last_error=False)(8, 'WriteProgress', ((1, 'strActivity'),(1, 'strCurrentOperation'),(1, 'strStatusDescription'),(1, 'uPercentComplete'),(1, 'uSecondsRemaining'),)))
    IWbemObjectSinkEx.WriteStreamParameter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),UInt32,UInt32, use_last_error=False)(9, 'WriteStreamParameter', ((1, 'strName'),(1, 'vtValue'),(1, 'ulType'),(1, 'ulFlags'),)))
    return IWbemObjectSinkEx
def _define_IWbemShutdown_head():
    class IWbemShutdown(win32more.System.Com.IUnknown_head):
        Guid = Guid('b7b31df9-d515-11d3-a11c-00105a1f515a')
    return IWbemShutdown
def _define_IWbemShutdown():
    IWbemShutdown = win32more.System.Wmi.IWbemShutdown_head
    IWbemShutdown.Shutdown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,UInt32,win32more.System.Wmi.IWbemContext_head, use_last_error=False)(3, 'Shutdown', ((1, 'uReason'),(1, 'uMaxMilliseconds'),(1, 'pCtx'),)))
    return IWbemShutdown
WMI_OBJ_TEXT = Int32
WMI_OBJ_TEXT_CIM_DTD_2_0 = 1
WMI_OBJ_TEXT_WMI_DTD_2_0 = 2
WMI_OBJ_TEXT_WMI_EXT1 = 3
WMI_OBJ_TEXT_WMI_EXT2 = 4
WMI_OBJ_TEXT_WMI_EXT3 = 5
WMI_OBJ_TEXT_WMI_EXT4 = 6
WMI_OBJ_TEXT_WMI_EXT5 = 7
WMI_OBJ_TEXT_WMI_EXT6 = 8
WMI_OBJ_TEXT_WMI_EXT7 = 9
WMI_OBJ_TEXT_WMI_EXT8 = 10
WMI_OBJ_TEXT_WMI_EXT9 = 11
WMI_OBJ_TEXT_WMI_EXT10 = 12
WMI_OBJ_TEXT_LAST = 13
def _define_IWbemObjectTextSrc_head():
    class IWbemObjectTextSrc(win32more.System.Com.IUnknown_head):
        Guid = Guid('bfbf883a-cad7-11d3-a11b-00105a1f515a')
    return IWbemObjectTextSrc
def _define_IWbemObjectTextSrc():
    IWbemObjectTextSrc = win32more.System.Wmi.IWbemObjectTextSrc_head
    IWbemObjectTextSrc.GetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Wmi.IWbemClassObject_head,UInt32,win32more.System.Wmi.IWbemContext_head,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'GetText', ((1, 'lFlags'),(1, 'pObj'),(1, 'uObjTextFormat'),(1, 'pCtx'),(1, 'strText'),)))
    IWbemObjectTextSrc.CreateFromText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR,UInt32,win32more.System.Wmi.IWbemContext_head,POINTER(win32more.System.Wmi.IWbemClassObject_head), use_last_error=False)(4, 'CreateFromText', ((1, 'lFlags'),(1, 'strText'),(1, 'uObjTextFormat'),(1, 'pCtx'),(1, 'pNewObj'),)))
    return IWbemObjectTextSrc
def _define_WBEM_COMPILE_STATUS_INFO_head():
    class WBEM_COMPILE_STATUS_INFO(Structure):
        pass
    return WBEM_COMPILE_STATUS_INFO
def _define_WBEM_COMPILE_STATUS_INFO():
    WBEM_COMPILE_STATUS_INFO = win32more.System.Wmi.WBEM_COMPILE_STATUS_INFO_head
    WBEM_COMPILE_STATUS_INFO._fields_ = [
        ("lPhaseError", Int32),
        ("hRes", win32more.Foundation.HRESULT),
        ("ObjectNum", Int32),
        ("FirstLine", Int32),
        ("LastLine", Int32),
        ("dwOutFlags", UInt32),
    ]
    return WBEM_COMPILE_STATUS_INFO
WBEM_COMPILER_OPTIONS = Int32
WBEM_FLAG_CHECK_ONLY = 1
WBEM_FLAG_AUTORECOVER = 2
WBEM_FLAG_WMI_CHECK = 4
WBEM_FLAG_CONSOLE_PRINT = 8
WBEM_FLAG_DONT_ADD_TO_LIST = 16
WBEM_FLAG_SPLIT_FILES = 32
WBEM_FLAG_STORE_FILE = 256
WBEM_CONNECT_OPTIONS = Int32
WBEM_FLAG_CONNECT_REPOSITORY_ONLY = 64
WBEM_FLAG_CONNECT_USE_MAX_WAIT = 128
WBEM_FLAG_CONNECT_PROVIDERS = 256
def _define_IMofCompiler_head():
    class IMofCompiler(win32more.System.Com.IUnknown_head):
        Guid = Guid('6daf974e-2e37-11d2-aec9-00c04fb68820')
    return IMofCompiler
def _define_IMofCompiler():
    IMofCompiler = win32more.System.Wmi.IMofCompiler_head
    IMofCompiler.CompileFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Int32,Int32,Int32,POINTER(win32more.System.Wmi.WBEM_COMPILE_STATUS_INFO_head), use_last_error=False)(3, 'CompileFile', ((1, 'FileName'),(1, 'ServerAndNamespace'),(1, 'User'),(1, 'Authority'),(1, 'Password'),(1, 'lOptionFlags'),(1, 'lClassFlags'),(1, 'lInstanceFlags'),(1, 'pInfo'),)))
    IMofCompiler.CompileBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,c_char_p_no,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Int32,Int32,Int32,POINTER(win32more.System.Wmi.WBEM_COMPILE_STATUS_INFO_head), use_last_error=False)(4, 'CompileBuffer', ((1, 'BuffSize'),(1, 'pBuffer'),(1, 'ServerAndNamespace'),(1, 'User'),(1, 'Authority'),(1, 'Password'),(1, 'lOptionFlags'),(1, 'lClassFlags'),(1, 'lInstanceFlags'),(1, 'pInfo'),)))
    IMofCompiler.CreateBMOF = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Int32,Int32,Int32,POINTER(win32more.System.Wmi.WBEM_COMPILE_STATUS_INFO_head), use_last_error=False)(5, 'CreateBMOF', ((1, 'TextFileName'),(1, 'BMOFFileName'),(1, 'ServerAndNamespace'),(1, 'lOptionFlags'),(1, 'lClassFlags'),(1, 'lInstanceFlags'),(1, 'pInfo'),)))
    return IMofCompiler
WBEM_UNSECAPP_FLAG_TYPE = Int32
WBEM_FLAG_UNSECAPP_DEFAULT_CHECK_ACCESS = 0
WBEM_FLAG_UNSECAPP_CHECK_ACCESS = 1
WBEM_FLAG_UNSECAPP_DONT_CHECK_ACCESS = 2
WBEM_INFORMATION_FLAG_TYPE = Int32
WBEM_FLAG_SHORT_NAME = 1
WBEM_FLAG_LONG_NAME = 2
WbemAdministrativeLocator = Guid('cb8555cc-9128-11d1-ad9b-00c04fd8fdff')
WbemAuthenticatedLocator = Guid('cd184336-9128-11d1-ad9b-00c04fd8fdff')
WbemUnauthenticatedLocator = Guid('443e7b79-de31-11d2-b340-00104bcc4b4a')
WbemDecoupledRegistrar = Guid('4cfc7932-0f9d-4bef-9c32-8ea2a6b56fcb')
WbemDecoupledBasicEventProvider = Guid('f5f75737-2843-4f22-933d-c76a97cda62f')
WBEM_PROVIDER_REQUIREMENTS_TYPE = Int32
WBEM_REQUIREMENTS_START_POSTFILTER = 0
WBEM_REQUIREMENTS_STOP_POSTFILTER = 1
WBEM_REQUIREMENTS_RECHECK_SUBSCRIPTIONS = 2
def _define_IWbemPropertyProvider_head():
    class IWbemPropertyProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('ce61e841-65bc-11d0-b6bd-00aa003240c7')
    return IWbemPropertyProvider
def _define_IWbemPropertyProvider():
    IWbemPropertyProvider = win32more.System.Wmi.IWbemPropertyProvider_head
    IWbemPropertyProvider.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(3, 'GetProperty', ((1, 'lFlags'),(1, 'strLocale'),(1, 'strClassMapping'),(1, 'strInstMapping'),(1, 'strPropMapping'),(1, 'pvValue'),)))
    IWbemPropertyProvider.PutProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(4, 'PutProperty', ((1, 'lFlags'),(1, 'strLocale'),(1, 'strClassMapping'),(1, 'strInstMapping'),(1, 'strPropMapping'),(1, 'pvValue'),)))
    return IWbemPropertyProvider
def _define_IWbemUnboundObjectSink_head():
    class IWbemUnboundObjectSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('e246107b-b06e-11d0-ad61-00c04fd8fdff')
    return IWbemUnboundObjectSink
def _define_IWbemUnboundObjectSink():
    IWbemUnboundObjectSink = win32more.System.Wmi.IWbemUnboundObjectSink_head
    IWbemUnboundObjectSink.IndicateToConsumer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Wmi.IWbemClassObject_head,Int32,POINTER(win32more.System.Wmi.IWbemClassObject_head), use_last_error=False)(3, 'IndicateToConsumer', ((1, 'pLogicalConsumer'),(1, 'lNumObjects'),(1, 'apObjects'),)))
    return IWbemUnboundObjectSink
def _define_IWbemEventProvider_head():
    class IWbemEventProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('e245105b-b06e-11d0-ad61-00c04fd8fdff')
    return IWbemEventProvider
def _define_IWbemEventProvider():
    IWbemEventProvider = win32more.System.Wmi.IWbemEventProvider_head
    IWbemEventProvider.ProvideEvents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Wmi.IWbemObjectSink_head,Int32, use_last_error=False)(3, 'ProvideEvents', ((1, 'pSink'),(1, 'lFlags'),)))
    return IWbemEventProvider
def _define_IWbemEventProviderQuerySink_head():
    class IWbemEventProviderQuerySink(win32more.System.Com.IUnknown_head):
        Guid = Guid('580acaf8-fa1c-11d0-ad72-00c04fd8fdff')
    return IWbemEventProviderQuerySink
def _define_IWbemEventProviderQuerySink():
    IWbemEventProviderQuerySink = win32more.System.Wmi.IWbemEventProviderQuerySink_head
    IWbemEventProviderQuerySink.NewQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt16),POINTER(UInt16), use_last_error=False)(3, 'NewQuery', ((1, 'dwId'),(1, 'wszQueryLanguage'),(1, 'wszQuery'),)))
    IWbemEventProviderQuerySink.CancelQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'CancelQuery', ((1, 'dwId'),)))
    return IWbemEventProviderQuerySink
def _define_IWbemEventProviderSecurity_head():
    class IWbemEventProviderSecurity(win32more.System.Com.IUnknown_head):
        Guid = Guid('631f7d96-d993-11d2-b339-00105a1f4aaf')
    return IWbemEventProviderSecurity
def _define_IWbemEventProviderSecurity():
    IWbemEventProviderSecurity = win32more.System.Wmi.IWbemEventProviderSecurity_head
    IWbemEventProviderSecurity.AccessCheck = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),POINTER(UInt16),Int32,POINTER(Byte), use_last_error=False)(3, 'AccessCheck', ((1, 'wszQueryLanguage'),(1, 'wszQuery'),(1, 'lSidLength'),(1, 'pSid'),)))
    return IWbemEventProviderSecurity
def _define_IWbemEventConsumerProvider_head():
    class IWbemEventConsumerProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('e246107a-b06e-11d0-ad61-00c04fd8fdff')
    return IWbemEventConsumerProvider
def _define_IWbemEventConsumerProvider():
    IWbemEventConsumerProvider = win32more.System.Wmi.IWbemEventConsumerProvider_head
    IWbemEventConsumerProvider.FindConsumer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Wmi.IWbemClassObject_head,POINTER(win32more.System.Wmi.IWbemUnboundObjectSink_head), use_last_error=False)(3, 'FindConsumer', ((1, 'pLogicalConsumer'),(1, 'ppConsumer'),)))
    return IWbemEventConsumerProvider
def _define_IWbemProviderInitSink_head():
    class IWbemProviderInitSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('1be41571-91dd-11d1-aeb2-00c04fb68820')
    return IWbemProviderInitSink
def _define_IWbemProviderInitSink():
    IWbemProviderInitSink = win32more.System.Wmi.IWbemProviderInitSink_head
    IWbemProviderInitSink.SetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(3, 'SetStatus', ((1, 'lStatus'),(1, 'lFlags'),)))
    return IWbemProviderInitSink
def _define_IWbemProviderInit_head():
    class IWbemProviderInit(win32more.System.Com.IUnknown_head):
        Guid = Guid('1be41572-91dd-11d1-aeb2-00c04fb68820')
    return IWbemProviderInit
def _define_IWbemProviderInit():
    IWbemProviderInit = win32more.System.Wmi.IWbemProviderInit_head
    IWbemProviderInit.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Int32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.System.Wmi.IWbemServices_head,win32more.System.Wmi.IWbemContext_head,win32more.System.Wmi.IWbemProviderInitSink_head, use_last_error=False)(3, 'Initialize', ((1, 'wszUser'),(1, 'lFlags'),(1, 'wszNamespace'),(1, 'wszLocale'),(1, 'pNamespace'),(1, 'pCtx'),(1, 'pInitSink'),)))
    return IWbemProviderInit
def _define_IWbemHiPerfProvider_head():
    class IWbemHiPerfProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('49353c93-516b-11d1-aea6-00c04fb68820')
    return IWbemHiPerfProvider
def _define_IWbemHiPerfProvider():
    IWbemHiPerfProvider = win32more.System.Wmi.IWbemHiPerfProvider_head
    IWbemHiPerfProvider.QueryInstances = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Wmi.IWbemServices_head,win32more.Foundation.PWSTR,Int32,win32more.System.Wmi.IWbemContext_head,win32more.System.Wmi.IWbemObjectSink_head, use_last_error=False)(3, 'QueryInstances', ((1, 'pNamespace'),(1, 'wszClass'),(1, 'lFlags'),(1, 'pCtx'),(1, 'pSink'),)))
    IWbemHiPerfProvider.CreateRefresher = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Wmi.IWbemServices_head,Int32,POINTER(win32more.System.Wmi.IWbemRefresher_head), use_last_error=False)(4, 'CreateRefresher', ((1, 'pNamespace'),(1, 'lFlags'),(1, 'ppRefresher'),)))
    IWbemHiPerfProvider.CreateRefreshableObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Wmi.IWbemServices_head,win32more.System.Wmi.IWbemObjectAccess_head,win32more.System.Wmi.IWbemRefresher_head,Int32,win32more.System.Wmi.IWbemContext_head,POINTER(win32more.System.Wmi.IWbemObjectAccess_head),POINTER(Int32), use_last_error=False)(5, 'CreateRefreshableObject', ((1, 'pNamespace'),(1, 'pTemplate'),(1, 'pRefresher'),(1, 'lFlags'),(1, 'pContext'),(1, 'ppRefreshable'),(1, 'plId'),)))
    IWbemHiPerfProvider.StopRefreshing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Wmi.IWbemRefresher_head,Int32,Int32, use_last_error=False)(6, 'StopRefreshing', ((1, 'pRefresher'),(1, 'lId'),(1, 'lFlags'),)))
    IWbemHiPerfProvider.CreateRefreshableEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Wmi.IWbemServices_head,win32more.Foundation.PWSTR,win32more.System.Wmi.IWbemRefresher_head,Int32,win32more.System.Wmi.IWbemContext_head,win32more.System.Wmi.IWbemHiPerfEnum_head,POINTER(Int32), use_last_error=False)(7, 'CreateRefreshableEnum', ((1, 'pNamespace'),(1, 'wszClass'),(1, 'pRefresher'),(1, 'lFlags'),(1, 'pContext'),(1, 'pHiPerfEnum'),(1, 'plId'),)))
    IWbemHiPerfProvider.GetObjects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Wmi.IWbemServices_head,Int32,POINTER(win32more.System.Wmi.IWbemObjectAccess_head),Int32,win32more.System.Wmi.IWbemContext_head, use_last_error=False)(8, 'GetObjects', ((1, 'pNamespace'),(1, 'lNumObjects'),(1, 'apObj'),(1, 'lFlags'),(1, 'pContext'),)))
    return IWbemHiPerfProvider
def _define_IWbemDecoupledRegistrar_head():
    class IWbemDecoupledRegistrar(win32more.System.Com.IUnknown_head):
        Guid = Guid('1005cbcf-e64f-4646-bcd3-3a089d8a84b4')
    return IWbemDecoupledRegistrar
def _define_IWbemDecoupledRegistrar():
    IWbemDecoupledRegistrar = win32more.System.Wmi.IWbemDecoupledRegistrar_head
    IWbemDecoupledRegistrar.Register = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Wmi.IWbemContext_head,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.System.Com.IUnknown_head, use_last_error=False)(3, 'Register', ((1, 'a_Flags'),(1, 'a_Context'),(1, 'a_User'),(1, 'a_Locale'),(1, 'a_Scope'),(1, 'a_Registration'),(1, 'pIUnknown'),)))
    IWbemDecoupledRegistrar.UnRegister = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'UnRegister', ()))
    return IWbemDecoupledRegistrar
def _define_IWbemProviderIdentity_head():
    class IWbemProviderIdentity(win32more.System.Com.IUnknown_head):
        Guid = Guid('631f7d97-d993-11d2-b339-00105a1f4aaf')
    return IWbemProviderIdentity
def _define_IWbemProviderIdentity():
    IWbemProviderIdentity = win32more.System.Wmi.IWbemProviderIdentity_head
    IWbemProviderIdentity.SetRegistrationObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Wmi.IWbemClassObject_head, use_last_error=False)(3, 'SetRegistrationObject', ((1, 'lFlags'),(1, 'pProvReg'),)))
    return IWbemProviderIdentity
WBEM_EXTRA_RETURN_CODES = Int32
WBEM_S_INITIALIZED = 0
WBEM_S_LIMITED_SERVICE = 274433
WBEM_S_INDIRECTLY_UPDATED = 274434
WBEM_S_SUBJECT_TO_SDS = 274435
WBEM_E_RETRY_LATER = -2147209215
WBEM_E_RESOURCE_CONTENTION = -2147209214
WBEM_PROVIDER_FLAGS = Int32
WBEM_FLAG_OWNER_UPDATE = 65536
def _define_IWbemDecoupledBasicEventProvider_head():
    class IWbemDecoupledBasicEventProvider(win32more.System.Wmi.IWbemDecoupledRegistrar_head):
        Guid = Guid('86336d20-ca11-4786-9ef1-bc8a946b42fc')
    return IWbemDecoupledBasicEventProvider
def _define_IWbemDecoupledBasicEventProvider():
    IWbemDecoupledBasicEventProvider = win32more.System.Wmi.IWbemDecoupledBasicEventProvider_head
    IWbemDecoupledBasicEventProvider.GetSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Wmi.IWbemContext_head,POINTER(win32more.System.Wmi.IWbemObjectSink_head), use_last_error=False)(5, 'GetSink', ((1, 'a_Flags'),(1, 'a_Context'),(1, 'a_Sink'),)))
    IWbemDecoupledBasicEventProvider.GetService = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Wmi.IWbemContext_head,POINTER(win32more.System.Wmi.IWbemServices_head), use_last_error=False)(6, 'GetService', ((1, 'a_Flags'),(1, 'a_Context'),(1, 'a_Service'),)))
    return IWbemDecoupledBasicEventProvider
WBEM_BATCH_TYPE = Int32
WBEM_FLAG_BATCH_IF_NEEDED = 0
WBEM_FLAG_MUST_BATCH = 1
WBEM_FLAG_MUST_NOT_BATCH = 2
def _define_IWbemEventSink_head():
    class IWbemEventSink(win32more.System.Wmi.IWbemObjectSink_head):
        Guid = Guid('3ae0080a-7e3a-4366-bf89-0feedc931659')
    return IWbemEventSink
def _define_IWbemEventSink():
    IWbemEventSink = win32more.System.Wmi.IWbemEventSink_head
    IWbemEventSink.SetSinkSecurity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Byte), use_last_error=False)(5, 'SetSinkSecurity', ((1, 'lSDLength'),(1, 'pSD'),)))
    IWbemEventSink.IsActive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'IsActive', ()))
    IWbemEventSink.GetRestrictedSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.PWSTR),win32more.System.Com.IUnknown_head,POINTER(win32more.System.Wmi.IWbemEventSink_head), use_last_error=False)(7, 'GetRestrictedSink', ((1, 'lNumQueries'),(1, 'awszQueries'),(1, 'pCallback'),(1, 'ppSink'),)))
    IWbemEventSink.SetBatchingParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,UInt32,UInt32, use_last_error=False)(8, 'SetBatchingParameters', ((1, 'lFlags'),(1, 'dwMaxBufferSize'),(1, 'dwMaxSendLatency'),)))
    return IWbemEventSink
SWbemLocator = Guid('76a64158-cb41-11d1-8b02-00600806d9b6')
SWbemNamedValueSet = Guid('9aed384e-ce8b-11d1-8b05-00600806d9b6')
SWbemObjectPath = Guid('5791bc26-ce9c-11d1-97bf-0000f81e849c')
SWbemLastError = Guid('c2feeeac-cfcd-11d1-8b05-00600806d9b6')
SWbemSink = Guid('75718c9a-f029-11d1-a1ac-00c04fb6c223')
SWbemDateTime = Guid('47dfbe54-cf76-11d3-b38f-00105a1f473a')
SWbemRefresher = Guid('d269bf5c-d9c1-11d3-b38f-00105a1f473a')
SWbemServices = Guid('04b83d63-21ae-11d2-8b33-00600806d9b6')
SWbemServicesEx = Guid('62e522dc-8cf3-40a8-8b2e-37d595651e40')
SWbemObject = Guid('04b83d62-21ae-11d2-8b33-00600806d9b6')
SWbemObjectEx = Guid('d6bdafb2-9435-491f-bb87-6aa0f0bc31a2')
SWbemObjectSet = Guid('04b83d61-21ae-11d2-8b33-00600806d9b6')
SWbemNamedValue = Guid('04b83d60-21ae-11d2-8b33-00600806d9b6')
SWbemQualifier = Guid('04b83d5f-21ae-11d2-8b33-00600806d9b6')
SWbemQualifierSet = Guid('04b83d5e-21ae-11d2-8b33-00600806d9b6')
SWbemProperty = Guid('04b83d5d-21ae-11d2-8b33-00600806d9b6')
SWbemPropertySet = Guid('04b83d5c-21ae-11d2-8b33-00600806d9b6')
SWbemMethod = Guid('04b83d5b-21ae-11d2-8b33-00600806d9b6')
SWbemMethodSet = Guid('04b83d5a-21ae-11d2-8b33-00600806d9b6')
SWbemEventSource = Guid('04b83d58-21ae-11d2-8b33-00600806d9b6')
SWbemSecurity = Guid('b54d66e9-2287-11d2-8b33-00600806d9b6')
SWbemPrivilege = Guid('26ee67bc-5804-11d2-8b4a-00600806d9b6')
SWbemPrivilegeSet = Guid('26ee67be-5804-11d2-8b4a-00600806d9b6')
SWbemRefreshableItem = Guid('8c6854bc-de4b-11d3-b390-00105a1f473a')
WbemChangeFlagEnum = Int32
WbemChangeFlagEnum_wbemChangeFlagCreateOrUpdate = 0
WbemChangeFlagEnum_wbemChangeFlagUpdateOnly = 1
WbemChangeFlagEnum_wbemChangeFlagCreateOnly = 2
WbemChangeFlagEnum_wbemChangeFlagUpdateCompatible = 0
WbemChangeFlagEnum_wbemChangeFlagUpdateSafeMode = 32
WbemChangeFlagEnum_wbemChangeFlagUpdateForceMode = 64
WbemChangeFlagEnum_wbemChangeFlagStrongValidation = 128
WbemChangeFlagEnum_wbemChangeFlagAdvisory = 65536
WbemFlagEnum = Int32
WbemFlagEnum_wbemFlagReturnImmediately = 16
WbemFlagEnum_wbemFlagReturnWhenComplete = 0
WbemFlagEnum_wbemFlagBidirectional = 0
WbemFlagEnum_wbemFlagForwardOnly = 32
WbemFlagEnum_wbemFlagNoErrorObject = 64
WbemFlagEnum_wbemFlagReturnErrorObject = 0
WbemFlagEnum_wbemFlagSendStatus = 128
WbemFlagEnum_wbemFlagDontSendStatus = 0
WbemFlagEnum_wbemFlagEnsureLocatable = 256
WbemFlagEnum_wbemFlagDirectRead = 512
WbemFlagEnum_wbemFlagSendOnlySelected = 0
WbemFlagEnum_wbemFlagUseAmendedQualifiers = 131072
WbemFlagEnum_wbemFlagGetDefault = 0
WbemFlagEnum_wbemFlagSpawnInstance = 1
WbemFlagEnum_wbemFlagUseCurrentTime = 1
WbemQueryFlagEnum = Int32
WbemQueryFlagEnum_wbemQueryFlagDeep = 0
WbemQueryFlagEnum_wbemQueryFlagShallow = 1
WbemQueryFlagEnum_wbemQueryFlagPrototype = 2
WbemTextFlagEnum = Int32
WbemTextFlagEnum_wbemTextFlagNoFlavors = 1
WbemTimeout = Int32
WbemTimeout_wbemTimeoutInfinite = -1
WbemComparisonFlagEnum = Int32
WbemComparisonFlagEnum_wbemComparisonFlagIncludeAll = 0
WbemComparisonFlagEnum_wbemComparisonFlagIgnoreQualifiers = 1
WbemComparisonFlagEnum_wbemComparisonFlagIgnoreObjectSource = 2
WbemComparisonFlagEnum_wbemComparisonFlagIgnoreDefaultValues = 4
WbemComparisonFlagEnum_wbemComparisonFlagIgnoreClass = 8
WbemComparisonFlagEnum_wbemComparisonFlagIgnoreCase = 16
WbemComparisonFlagEnum_wbemComparisonFlagIgnoreFlavor = 32
WbemCimtypeEnum = Int32
WbemCimtypeEnum_wbemCimtypeSint8 = 16
WbemCimtypeEnum_wbemCimtypeUint8 = 17
WbemCimtypeEnum_wbemCimtypeSint16 = 2
WbemCimtypeEnum_wbemCimtypeUint16 = 18
WbemCimtypeEnum_wbemCimtypeSint32 = 3
WbemCimtypeEnum_wbemCimtypeUint32 = 19
WbemCimtypeEnum_wbemCimtypeSint64 = 20
WbemCimtypeEnum_wbemCimtypeUint64 = 21
WbemCimtypeEnum_wbemCimtypeReal32 = 4
WbemCimtypeEnum_wbemCimtypeReal64 = 5
WbemCimtypeEnum_wbemCimtypeBoolean = 11
WbemCimtypeEnum_wbemCimtypeString = 8
WbemCimtypeEnum_wbemCimtypeDatetime = 101
WbemCimtypeEnum_wbemCimtypeReference = 102
WbemCimtypeEnum_wbemCimtypeChar16 = 103
WbemCimtypeEnum_wbemCimtypeObject = 13
WbemErrorEnum = Int32
WbemErrorEnum_wbemNoErr = 0
WbemErrorEnum_wbemErrFailed = -2147217407
WbemErrorEnum_wbemErrNotFound = -2147217406
WbemErrorEnum_wbemErrAccessDenied = -2147217405
WbemErrorEnum_wbemErrProviderFailure = -2147217404
WbemErrorEnum_wbemErrTypeMismatch = -2147217403
WbemErrorEnum_wbemErrOutOfMemory = -2147217402
WbemErrorEnum_wbemErrInvalidContext = -2147217401
WbemErrorEnum_wbemErrInvalidParameter = -2147217400
WbemErrorEnum_wbemErrNotAvailable = -2147217399
WbemErrorEnum_wbemErrCriticalError = -2147217398
WbemErrorEnum_wbemErrInvalidStream = -2147217397
WbemErrorEnum_wbemErrNotSupported = -2147217396
WbemErrorEnum_wbemErrInvalidSuperclass = -2147217395
WbemErrorEnum_wbemErrInvalidNamespace = -2147217394
WbemErrorEnum_wbemErrInvalidObject = -2147217393
WbemErrorEnum_wbemErrInvalidClass = -2147217392
WbemErrorEnum_wbemErrProviderNotFound = -2147217391
WbemErrorEnum_wbemErrInvalidProviderRegistration = -2147217390
WbemErrorEnum_wbemErrProviderLoadFailure = -2147217389
WbemErrorEnum_wbemErrInitializationFailure = -2147217388
WbemErrorEnum_wbemErrTransportFailure = -2147217387
WbemErrorEnum_wbemErrInvalidOperation = -2147217386
WbemErrorEnum_wbemErrInvalidQuery = -2147217385
WbemErrorEnum_wbemErrInvalidQueryType = -2147217384
WbemErrorEnum_wbemErrAlreadyExists = -2147217383
WbemErrorEnum_wbemErrOverrideNotAllowed = -2147217382
WbemErrorEnum_wbemErrPropagatedQualifier = -2147217381
WbemErrorEnum_wbemErrPropagatedProperty = -2147217380
WbemErrorEnum_wbemErrUnexpected = -2147217379
WbemErrorEnum_wbemErrIllegalOperation = -2147217378
WbemErrorEnum_wbemErrCannotBeKey = -2147217377
WbemErrorEnum_wbemErrIncompleteClass = -2147217376
WbemErrorEnum_wbemErrInvalidSyntax = -2147217375
WbemErrorEnum_wbemErrNondecoratedObject = -2147217374
WbemErrorEnum_wbemErrReadOnly = -2147217373
WbemErrorEnum_wbemErrProviderNotCapable = -2147217372
WbemErrorEnum_wbemErrClassHasChildren = -2147217371
WbemErrorEnum_wbemErrClassHasInstances = -2147217370
WbemErrorEnum_wbemErrQueryNotImplemented = -2147217369
WbemErrorEnum_wbemErrIllegalNull = -2147217368
WbemErrorEnum_wbemErrInvalidQualifierType = -2147217367
WbemErrorEnum_wbemErrInvalidPropertyType = -2147217366
WbemErrorEnum_wbemErrValueOutOfRange = -2147217365
WbemErrorEnum_wbemErrCannotBeSingleton = -2147217364
WbemErrorEnum_wbemErrInvalidCimType = -2147217363
WbemErrorEnum_wbemErrInvalidMethod = -2147217362
WbemErrorEnum_wbemErrInvalidMethodParameters = -2147217361
WbemErrorEnum_wbemErrSystemProperty = -2147217360
WbemErrorEnum_wbemErrInvalidProperty = -2147217359
WbemErrorEnum_wbemErrCallCancelled = -2147217358
WbemErrorEnum_wbemErrShuttingDown = -2147217357
WbemErrorEnum_wbemErrPropagatedMethod = -2147217356
WbemErrorEnum_wbemErrUnsupportedParameter = -2147217355
WbemErrorEnum_wbemErrMissingParameter = -2147217354
WbemErrorEnum_wbemErrInvalidParameterId = -2147217353
WbemErrorEnum_wbemErrNonConsecutiveParameterIds = -2147217352
WbemErrorEnum_wbemErrParameterIdOnRetval = -2147217351
WbemErrorEnum_wbemErrInvalidObjectPath = -2147217350
WbemErrorEnum_wbemErrOutOfDiskSpace = -2147217349
WbemErrorEnum_wbemErrBufferTooSmall = -2147217348
WbemErrorEnum_wbemErrUnsupportedPutExtension = -2147217347
WbemErrorEnum_wbemErrUnknownObjectType = -2147217346
WbemErrorEnum_wbemErrUnknownPacketType = -2147217345
WbemErrorEnum_wbemErrMarshalVersionMismatch = -2147217344
WbemErrorEnum_wbemErrMarshalInvalidSignature = -2147217343
WbemErrorEnum_wbemErrInvalidQualifier = -2147217342
WbemErrorEnum_wbemErrInvalidDuplicateParameter = -2147217341
WbemErrorEnum_wbemErrTooMuchData = -2147217340
WbemErrorEnum_wbemErrServerTooBusy = -2147217339
WbemErrorEnum_wbemErrInvalidFlavor = -2147217338
WbemErrorEnum_wbemErrCircularReference = -2147217337
WbemErrorEnum_wbemErrUnsupportedClassUpdate = -2147217336
WbemErrorEnum_wbemErrCannotChangeKeyInheritance = -2147217335
WbemErrorEnum_wbemErrCannotChangeIndexInheritance = -2147217328
WbemErrorEnum_wbemErrTooManyProperties = -2147217327
WbemErrorEnum_wbemErrUpdateTypeMismatch = -2147217326
WbemErrorEnum_wbemErrUpdateOverrideNotAllowed = -2147217325
WbemErrorEnum_wbemErrUpdatePropagatedMethod = -2147217324
WbemErrorEnum_wbemErrMethodNotImplemented = -2147217323
WbemErrorEnum_wbemErrMethodDisabled = -2147217322
WbemErrorEnum_wbemErrRefresherBusy = -2147217321
WbemErrorEnum_wbemErrUnparsableQuery = -2147217320
WbemErrorEnum_wbemErrNotEventClass = -2147217319
WbemErrorEnum_wbemErrMissingGroupWithin = -2147217318
WbemErrorEnum_wbemErrMissingAggregationList = -2147217317
WbemErrorEnum_wbemErrPropertyNotAnObject = -2147217316
WbemErrorEnum_wbemErrAggregatingByObject = -2147217315
WbemErrorEnum_wbemErrUninterpretableProviderQuery = -2147217313
WbemErrorEnum_wbemErrBackupRestoreWinmgmtRunning = -2147217312
WbemErrorEnum_wbemErrQueueOverflow = -2147217311
WbemErrorEnum_wbemErrPrivilegeNotHeld = -2147217310
WbemErrorEnum_wbemErrInvalidOperator = -2147217309
WbemErrorEnum_wbemErrLocalCredentials = -2147217308
WbemErrorEnum_wbemErrCannotBeAbstract = -2147217307
WbemErrorEnum_wbemErrAmendedObject = -2147217306
WbemErrorEnum_wbemErrClientTooSlow = -2147217305
WbemErrorEnum_wbemErrNullSecurityDescriptor = -2147217304
WbemErrorEnum_wbemErrTimeout = -2147217303
WbemErrorEnum_wbemErrInvalidAssociation = -2147217302
WbemErrorEnum_wbemErrAmbiguousOperation = -2147217301
WbemErrorEnum_wbemErrQuotaViolation = -2147217300
WbemErrorEnum_wbemErrTransactionConflict = -2147217299
WbemErrorEnum_wbemErrForcedRollback = -2147217298
WbemErrorEnum_wbemErrUnsupportedLocale = -2147217297
WbemErrorEnum_wbemErrHandleOutOfDate = -2147217296
WbemErrorEnum_wbemErrConnectionFailed = -2147217295
WbemErrorEnum_wbemErrInvalidHandleRequest = -2147217294
WbemErrorEnum_wbemErrPropertyNameTooWide = -2147217293
WbemErrorEnum_wbemErrClassNameTooWide = -2147217292
WbemErrorEnum_wbemErrMethodNameTooWide = -2147217291
WbemErrorEnum_wbemErrQualifierNameTooWide = -2147217290
WbemErrorEnum_wbemErrRerunCommand = -2147217289
WbemErrorEnum_wbemErrDatabaseVerMismatch = -2147217288
WbemErrorEnum_wbemErrVetoPut = -2147217287
WbemErrorEnum_wbemErrVetoDelete = -2147217286
WbemErrorEnum_wbemErrInvalidLocale = -2147217280
WbemErrorEnum_wbemErrProviderSuspended = -2147217279
WbemErrorEnum_wbemErrSynchronizationRequired = -2147217278
WbemErrorEnum_wbemErrNoSchema = -2147217277
WbemErrorEnum_wbemErrProviderAlreadyRegistered = -2147217276
WbemErrorEnum_wbemErrProviderNotRegistered = -2147217275
WbemErrorEnum_wbemErrFatalTransportError = -2147217274
WbemErrorEnum_wbemErrEncryptedConnectionRequired = -2147217273
WbemErrorEnum_wbemErrRegistrationTooBroad = -2147213311
WbemErrorEnum_wbemErrRegistrationTooPrecise = -2147213310
WbemErrorEnum_wbemErrTimedout = -2147209215
WbemErrorEnum_wbemErrResetToDefault = -2147209214
WbemAuthenticationLevelEnum = Int32
WbemAuthenticationLevelEnum_wbemAuthenticationLevelDefault = 0
WbemAuthenticationLevelEnum_wbemAuthenticationLevelNone = 1
WbemAuthenticationLevelEnum_wbemAuthenticationLevelConnect = 2
WbemAuthenticationLevelEnum_wbemAuthenticationLevelCall = 3
WbemAuthenticationLevelEnum_wbemAuthenticationLevelPkt = 4
WbemAuthenticationLevelEnum_wbemAuthenticationLevelPktIntegrity = 5
WbemAuthenticationLevelEnum_wbemAuthenticationLevelPktPrivacy = 6
WbemImpersonationLevelEnum = Int32
WbemImpersonationLevelEnum_wbemImpersonationLevelAnonymous = 1
WbemImpersonationLevelEnum_wbemImpersonationLevelIdentify = 2
WbemImpersonationLevelEnum_wbemImpersonationLevelImpersonate = 3
WbemImpersonationLevelEnum_wbemImpersonationLevelDelegate = 4
WbemPrivilegeEnum = Int32
WbemPrivilegeEnum_wbemPrivilegeCreateToken = 1
WbemPrivilegeEnum_wbemPrivilegePrimaryToken = 2
WbemPrivilegeEnum_wbemPrivilegeLockMemory = 3
WbemPrivilegeEnum_wbemPrivilegeIncreaseQuota = 4
WbemPrivilegeEnum_wbemPrivilegeMachineAccount = 5
WbemPrivilegeEnum_wbemPrivilegeTcb = 6
WbemPrivilegeEnum_wbemPrivilegeSecurity = 7
WbemPrivilegeEnum_wbemPrivilegeTakeOwnership = 8
WbemPrivilegeEnum_wbemPrivilegeLoadDriver = 9
WbemPrivilegeEnum_wbemPrivilegeSystemProfile = 10
WbemPrivilegeEnum_wbemPrivilegeSystemtime = 11
WbemPrivilegeEnum_wbemPrivilegeProfileSingleProcess = 12
WbemPrivilegeEnum_wbemPrivilegeIncreaseBasePriority = 13
WbemPrivilegeEnum_wbemPrivilegeCreatePagefile = 14
WbemPrivilegeEnum_wbemPrivilegeCreatePermanent = 15
WbemPrivilegeEnum_wbemPrivilegeBackup = 16
WbemPrivilegeEnum_wbemPrivilegeRestore = 17
WbemPrivilegeEnum_wbemPrivilegeShutdown = 18
WbemPrivilegeEnum_wbemPrivilegeDebug = 19
WbemPrivilegeEnum_wbemPrivilegeAudit = 20
WbemPrivilegeEnum_wbemPrivilegeSystemEnvironment = 21
WbemPrivilegeEnum_wbemPrivilegeChangeNotify = 22
WbemPrivilegeEnum_wbemPrivilegeRemoteShutdown = 23
WbemPrivilegeEnum_wbemPrivilegeUndock = 24
WbemPrivilegeEnum_wbemPrivilegeSyncAgent = 25
WbemPrivilegeEnum_wbemPrivilegeEnableDelegation = 26
WbemPrivilegeEnum_wbemPrivilegeManageVolume = 27
WbemObjectTextFormatEnum = Int32
WbemObjectTextFormatEnum_wbemObjectTextFormatCIMDTD20 = 1
WbemObjectTextFormatEnum_wbemObjectTextFormatWMIDTD20 = 2
WbemConnectOptionsEnum = Int32
WbemConnectOptionsEnum_wbemConnectFlagUseMaxWait = 128
def _define_ISWbemServices_head():
    class ISWbemServices(win32more.System.Com.IDispatch_head):
        Guid = Guid('76a6415c-cb41-11d1-8b02-00600806d9b6')
    return ISWbemServices
def _define_ISWbemServices():
    ISWbemServices = win32more.System.Wmi.ISWbemServices_head
    ISWbemServices.Get = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.System.Com.IDispatch_head,POINTER(win32more.System.Wmi.ISWbemObject_head), use_last_error=False)(7, 'Get', ((1, 'strObjectPath'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemObject'),)))
    ISWbemServices.GetAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,win32more.Foundation.BSTR,Int32,win32more.System.Com.IDispatch_head,win32more.System.Com.IDispatch_head, use_last_error=False)(8, 'GetAsync', ((1, 'objWbemSink'),(1, 'strObjectPath'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemAsyncContext'),)))
    ISWbemServices.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.System.Com.IDispatch_head, use_last_error=False)(9, 'Delete', ((1, 'strObjectPath'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),)))
    ISWbemServices.DeleteAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,win32more.Foundation.BSTR,Int32,win32more.System.Com.IDispatch_head,win32more.System.Com.IDispatch_head, use_last_error=False)(10, 'DeleteAsync', ((1, 'objWbemSink'),(1, 'strObjectPath'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemAsyncContext'),)))
    ISWbemServices.InstancesOf = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.System.Com.IDispatch_head,POINTER(win32more.System.Wmi.ISWbemObjectSet_head), use_last_error=False)(11, 'InstancesOf', ((1, 'strClass'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemObjectSet'),)))
    ISWbemServices.InstancesOfAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,win32more.Foundation.BSTR,Int32,win32more.System.Com.IDispatch_head,win32more.System.Com.IDispatch_head, use_last_error=False)(12, 'InstancesOfAsync', ((1, 'objWbemSink'),(1, 'strClass'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemAsyncContext'),)))
    ISWbemServices.SubclassesOf = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,win32more.System.Com.IDispatch_head,POINTER(win32more.System.Wmi.ISWbemObjectSet_head), use_last_error=False)(13, 'SubclassesOf', ((1, 'strSuperclass'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemObjectSet'),)))
    ISWbemServices.SubclassesOfAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,win32more.Foundation.BSTR,Int32,win32more.System.Com.IDispatch_head,win32more.System.Com.IDispatch_head, use_last_error=False)(14, 'SubclassesOfAsync', ((1, 'objWbemSink'),(1, 'strSuperclass'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemAsyncContext'),)))
    ISWbemServices.ExecQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,win32more.System.Com.IDispatch_head,POINTER(win32more.System.Wmi.ISWbemObjectSet_head), use_last_error=False)(15, 'ExecQuery', ((1, 'strQuery'),(1, 'strQueryLanguage'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemObjectSet'),)))
    ISWbemServices.ExecQueryAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,win32more.System.Com.IDispatch_head,win32more.System.Com.IDispatch_head, use_last_error=False)(16, 'ExecQueryAsync', ((1, 'objWbemSink'),(1, 'strQuery'),(1, 'strQueryLanguage'),(1, 'lFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemAsyncContext'),)))
    ISWbemServices.AssociatorsOf = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int16,Int16,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,win32more.System.Com.IDispatch_head,POINTER(win32more.System.Wmi.ISWbemObjectSet_head), use_last_error=False)(17, 'AssociatorsOf', ((1, 'strObjectPath'),(1, 'strAssocClass'),(1, 'strResultClass'),(1, 'strResultRole'),(1, 'strRole'),(1, 'bClassesOnly'),(1, 'bSchemaOnly'),(1, 'strRequiredAssocQualifier'),(1, 'strRequiredQualifier'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemObjectSet'),)))
    ISWbemServices.AssociatorsOfAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int16,Int16,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,win32more.System.Com.IDispatch_head,win32more.System.Com.IDispatch_head, use_last_error=False)(18, 'AssociatorsOfAsync', ((1, 'objWbemSink'),(1, 'strObjectPath'),(1, 'strAssocClass'),(1, 'strResultClass'),(1, 'strResultRole'),(1, 'strRole'),(1, 'bClassesOnly'),(1, 'bSchemaOnly'),(1, 'strRequiredAssocQualifier'),(1, 'strRequiredQualifier'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemAsyncContext'),)))
    ISWbemServices.ReferencesTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int16,Int16,win32more.Foundation.BSTR,Int32,win32more.System.Com.IDispatch_head,POINTER(win32more.System.Wmi.ISWbemObjectSet_head), use_last_error=False)(19, 'ReferencesTo', ((1, 'strObjectPath'),(1, 'strResultClass'),(1, 'strRole'),(1, 'bClassesOnly'),(1, 'bSchemaOnly'),(1, 'strRequiredQualifier'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemObjectSet'),)))
    ISWbemServices.ReferencesToAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int16,Int16,win32more.Foundation.BSTR,Int32,win32more.System.Com.IDispatch_head,win32more.System.Com.IDispatch_head, use_last_error=False)(20, 'ReferencesToAsync', ((1, 'objWbemSink'),(1, 'strObjectPath'),(1, 'strResultClass'),(1, 'strRole'),(1, 'bClassesOnly'),(1, 'bSchemaOnly'),(1, 'strRequiredQualifier'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemAsyncContext'),)))
    ISWbemServices.ExecNotificationQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,win32more.System.Com.IDispatch_head,POINTER(win32more.System.Wmi.ISWbemEventSource_head), use_last_error=False)(21, 'ExecNotificationQuery', ((1, 'strQuery'),(1, 'strQueryLanguage'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemEventSource'),)))
    ISWbemServices.ExecNotificationQueryAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,win32more.System.Com.IDispatch_head,win32more.System.Com.IDispatch_head, use_last_error=False)(22, 'ExecNotificationQueryAsync', ((1, 'objWbemSink'),(1, 'strQuery'),(1, 'strQueryLanguage'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemAsyncContext'),)))
    ISWbemServices.ExecMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.System.Com.IDispatch_head,Int32,win32more.System.Com.IDispatch_head,POINTER(win32more.System.Wmi.ISWbemObject_head), use_last_error=False)(23, 'ExecMethod', ((1, 'strObjectPath'),(1, 'strMethodName'),(1, 'objWbemInParameters'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemOutParameters'),)))
    ISWbemServices.ExecMethodAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.System.Com.IDispatch_head,Int32,win32more.System.Com.IDispatch_head,win32more.System.Com.IDispatch_head, use_last_error=False)(24, 'ExecMethodAsync', ((1, 'objWbemSink'),(1, 'strObjectPath'),(1, 'strMethodName'),(1, 'objWbemInParameters'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemAsyncContext'),)))
    ISWbemServices.get_Security_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.ISWbemSecurity_head), use_last_error=False)(25, 'get_Security_', ((1, 'objWbemSecurity'),)))
    return ISWbemServices
def _define_ISWbemLocator_head():
    class ISWbemLocator(win32more.System.Com.IDispatch_head):
        Guid = Guid('76a6415b-cb41-11d1-8b02-00600806d9b6')
    return ISWbemLocator
def _define_ISWbemLocator():
    ISWbemLocator = win32more.System.Wmi.ISWbemLocator_head
    ISWbemLocator.ConnectServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,win32more.System.Com.IDispatch_head,POINTER(win32more.System.Wmi.ISWbemServices_head), use_last_error=False)(7, 'ConnectServer', ((1, 'strServer'),(1, 'strNamespace'),(1, 'strUser'),(1, 'strPassword'),(1, 'strLocale'),(1, 'strAuthority'),(1, 'iSecurityFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemServices'),)))
    ISWbemLocator.get_Security_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.ISWbemSecurity_head), use_last_error=False)(8, 'get_Security_', ((1, 'objWbemSecurity'),)))
    return ISWbemLocator
def _define_ISWbemObject_head():
    class ISWbemObject(win32more.System.Com.IDispatch_head):
        Guid = Guid('76a6415a-cb41-11d1-8b02-00600806d9b6')
    return ISWbemObject
def _define_ISWbemObject():
    ISWbemObject = win32more.System.Wmi.ISWbemObject_head
    ISWbemObject.Put_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.IDispatch_head,POINTER(win32more.System.Wmi.ISWbemObjectPath_head), use_last_error=False)(7, 'Put_', ((1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemObjectPath'),)))
    ISWbemObject.PutAsync_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,Int32,win32more.System.Com.IDispatch_head,win32more.System.Com.IDispatch_head, use_last_error=False)(8, 'PutAsync_', ((1, 'objWbemSink'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemAsyncContext'),)))
    ISWbemObject.Delete_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.IDispatch_head, use_last_error=False)(9, 'Delete_', ((1, 'iFlags'),(1, 'objWbemNamedValueSet'),)))
    ISWbemObject.DeleteAsync_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,Int32,win32more.System.Com.IDispatch_head,win32more.System.Com.IDispatch_head, use_last_error=False)(10, 'DeleteAsync_', ((1, 'objWbemSink'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemAsyncContext'),)))
    ISWbemObject.Instances_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.IDispatch_head,POINTER(win32more.System.Wmi.ISWbemObjectSet_head), use_last_error=False)(11, 'Instances_', ((1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemObjectSet'),)))
    ISWbemObject.InstancesAsync_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,Int32,win32more.System.Com.IDispatch_head,win32more.System.Com.IDispatch_head, use_last_error=False)(12, 'InstancesAsync_', ((1, 'objWbemSink'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemAsyncContext'),)))
    ISWbemObject.Subclasses_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.IDispatch_head,POINTER(win32more.System.Wmi.ISWbemObjectSet_head), use_last_error=False)(13, 'Subclasses_', ((1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemObjectSet'),)))
    ISWbemObject.SubclassesAsync_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,Int32,win32more.System.Com.IDispatch_head,win32more.System.Com.IDispatch_head, use_last_error=False)(14, 'SubclassesAsync_', ((1, 'objWbemSink'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemAsyncContext'),)))
    ISWbemObject.Associators_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int16,Int16,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,win32more.System.Com.IDispatch_head,POINTER(win32more.System.Wmi.ISWbemObjectSet_head), use_last_error=False)(15, 'Associators_', ((1, 'strAssocClass'),(1, 'strResultClass'),(1, 'strResultRole'),(1, 'strRole'),(1, 'bClassesOnly'),(1, 'bSchemaOnly'),(1, 'strRequiredAssocQualifier'),(1, 'strRequiredQualifier'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemObjectSet'),)))
    ISWbemObject.AssociatorsAsync_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int16,Int16,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,win32more.System.Com.IDispatch_head,win32more.System.Com.IDispatch_head, use_last_error=False)(16, 'AssociatorsAsync_', ((1, 'objWbemSink'),(1, 'strAssocClass'),(1, 'strResultClass'),(1, 'strResultRole'),(1, 'strRole'),(1, 'bClassesOnly'),(1, 'bSchemaOnly'),(1, 'strRequiredAssocQualifier'),(1, 'strRequiredQualifier'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemAsyncContext'),)))
    ISWbemObject.References_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int16,Int16,win32more.Foundation.BSTR,Int32,win32more.System.Com.IDispatch_head,POINTER(win32more.System.Wmi.ISWbemObjectSet_head), use_last_error=False)(17, 'References_', ((1, 'strResultClass'),(1, 'strRole'),(1, 'bClassesOnly'),(1, 'bSchemaOnly'),(1, 'strRequiredQualifier'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemObjectSet'),)))
    ISWbemObject.ReferencesAsync_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int16,Int16,win32more.Foundation.BSTR,Int32,win32more.System.Com.IDispatch_head,win32more.System.Com.IDispatch_head, use_last_error=False)(18, 'ReferencesAsync_', ((1, 'objWbemSink'),(1, 'strResultClass'),(1, 'strRole'),(1, 'bClassesOnly'),(1, 'bSchemaOnly'),(1, 'strRequiredQualifier'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemAsyncContext'),)))
    ISWbemObject.ExecMethod_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Com.IDispatch_head,Int32,win32more.System.Com.IDispatch_head,POINTER(win32more.System.Wmi.ISWbemObject_head), use_last_error=False)(19, 'ExecMethod_', ((1, 'strMethodName'),(1, 'objWbemInParameters'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemOutParameters'),)))
    ISWbemObject.ExecMethodAsync_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,win32more.Foundation.BSTR,win32more.System.Com.IDispatch_head,Int32,win32more.System.Com.IDispatch_head,win32more.System.Com.IDispatch_head, use_last_error=False)(20, 'ExecMethodAsync_', ((1, 'objWbemSink'),(1, 'strMethodName'),(1, 'objWbemInParameters'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemAsyncContext'),)))
    ISWbemObject.Clone_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.ISWbemObject_head), use_last_error=False)(21, 'Clone_', ((1, 'objWbemObject'),)))
    ISWbemObject.GetObjectText_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(22, 'GetObjectText_', ((1, 'iFlags'),(1, 'strObjectText'),)))
    ISWbemObject.SpawnDerivedClass_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Wmi.ISWbemObject_head), use_last_error=False)(23, 'SpawnDerivedClass_', ((1, 'iFlags'),(1, 'objWbemObject'),)))
    ISWbemObject.SpawnInstance_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Wmi.ISWbemObject_head), use_last_error=False)(24, 'SpawnInstance_', ((1, 'iFlags'),(1, 'objWbemObject'),)))
    ISWbemObject.CompareTo_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,Int32,POINTER(Int16), use_last_error=False)(25, 'CompareTo_', ((1, 'objWbemObject'),(1, 'iFlags'),(1, 'bResult'),)))
    ISWbemObject.get_Qualifiers_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.ISWbemQualifierSet_head), use_last_error=False)(26, 'get_Qualifiers_', ((1, 'objWbemQualifierSet'),)))
    ISWbemObject.get_Properties_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.ISWbemPropertySet_head), use_last_error=False)(27, 'get_Properties_', ((1, 'objWbemPropertySet'),)))
    ISWbemObject.get_Methods_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.ISWbemMethodSet_head), use_last_error=False)(28, 'get_Methods_', ((1, 'objWbemMethodSet'),)))
    ISWbemObject.get_Derivation_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(29, 'get_Derivation_', ((1, 'strClassNameArray'),)))
    ISWbemObject.get_Path_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.ISWbemObjectPath_head), use_last_error=False)(30, 'get_Path_', ((1, 'objWbemObjectPath'),)))
    ISWbemObject.get_Security_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.ISWbemSecurity_head), use_last_error=False)(31, 'get_Security_', ((1, 'objWbemSecurity'),)))
    return ISWbemObject
def _define_ISWbemObjectSet_head():
    class ISWbemObjectSet(win32more.System.Com.IDispatch_head):
        Guid = Guid('76a6415f-cb41-11d1-8b02-00600806d9b6')
    return ISWbemObjectSet
def _define_ISWbemObjectSet():
    ISWbemObjectSet = win32more.System.Wmi.ISWbemObjectSet_head
    ISWbemObjectSet.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'pUnk'),)))
    ISWbemObjectSet.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,POINTER(win32more.System.Wmi.ISWbemObject_head), use_last_error=False)(8, 'Item', ((1, 'strObjectPath'),(1, 'iFlags'),(1, 'objWbemObject'),)))
    ISWbemObjectSet.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'iCount'),)))
    ISWbemObjectSet.get_Security_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.ISWbemSecurity_head), use_last_error=False)(10, 'get_Security_', ((1, 'objWbemSecurity'),)))
    ISWbemObjectSet.ItemIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Wmi.ISWbemObject_head), use_last_error=False)(11, 'ItemIndex', ((1, 'lIndex'),(1, 'objWbemObject'),)))
    return ISWbemObjectSet
def _define_ISWbemNamedValue_head():
    class ISWbemNamedValue(win32more.System.Com.IDispatch_head):
        Guid = Guid('76a64164-cb41-11d1-8b02-00600806d9b6')
    return ISWbemNamedValue
def _define_ISWbemNamedValue():
    ISWbemNamedValue = win32more.System.Wmi.ISWbemNamedValue_head
    ISWbemNamedValue.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'get_Value', ((1, 'varValue'),)))
    ISWbemNamedValue.put_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(8, 'put_Value', ((1, 'varValue'),)))
    ISWbemNamedValue.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_Name', ((1, 'strName'),)))
    return ISWbemNamedValue
def _define_ISWbemNamedValueSet_head():
    class ISWbemNamedValueSet(win32more.System.Com.IDispatch_head):
        Guid = Guid('cf2376ea-ce8c-11d1-8b05-00600806d9b6')
    return ISWbemNamedValueSet
def _define_ISWbemNamedValueSet():
    ISWbemNamedValueSet = win32more.System.Wmi.ISWbemNamedValueSet_head
    ISWbemNamedValueSet.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'pUnk'),)))
    ISWbemNamedValueSet.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,POINTER(win32more.System.Wmi.ISWbemNamedValue_head), use_last_error=False)(8, 'Item', ((1, 'strName'),(1, 'iFlags'),(1, 'objWbemNamedValue'),)))
    ISWbemNamedValueSet.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'iCount'),)))
    ISWbemNamedValueSet.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),Int32,POINTER(win32more.System.Wmi.ISWbemNamedValue_head), use_last_error=False)(10, 'Add', ((1, 'strName'),(1, 'varValue'),(1, 'iFlags'),(1, 'objWbemNamedValue'),)))
    ISWbemNamedValueSet.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32, use_last_error=False)(11, 'Remove', ((1, 'strName'),(1, 'iFlags'),)))
    ISWbemNamedValueSet.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.ISWbemNamedValueSet_head), use_last_error=False)(12, 'Clone', ((1, 'objWbemNamedValueSet'),)))
    ISWbemNamedValueSet.DeleteAll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(13, 'DeleteAll', ()))
    return ISWbemNamedValueSet
def _define_ISWbemQualifier_head():
    class ISWbemQualifier(win32more.System.Com.IDispatch_head):
        Guid = Guid('79b05932-d3b7-11d1-8b06-00600806d9b6')
    return ISWbemQualifier
def _define_ISWbemQualifier():
    ISWbemQualifier = win32more.System.Wmi.ISWbemQualifier_head
    ISWbemQualifier.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'get_Value', ((1, 'varValue'),)))
    ISWbemQualifier.put_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(8, 'put_Value', ((1, 'varValue'),)))
    ISWbemQualifier.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_Name', ((1, 'strName'),)))
    ISWbemQualifier.get_IsLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(10, 'get_IsLocal', ((1, 'bIsLocal'),)))
    ISWbemQualifier.get_PropagatesToSubclass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(11, 'get_PropagatesToSubclass', ((1, 'bPropagatesToSubclass'),)))
    ISWbemQualifier.put_PropagatesToSubclass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(12, 'put_PropagatesToSubclass', ((1, 'bPropagatesToSubclass'),)))
    ISWbemQualifier.get_PropagatesToInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(13, 'get_PropagatesToInstance', ((1, 'bPropagatesToInstance'),)))
    ISWbemQualifier.put_PropagatesToInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(14, 'put_PropagatesToInstance', ((1, 'bPropagatesToInstance'),)))
    ISWbemQualifier.get_IsOverridable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(15, 'get_IsOverridable', ((1, 'bIsOverridable'),)))
    ISWbemQualifier.put_IsOverridable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(16, 'put_IsOverridable', ((1, 'bIsOverridable'),)))
    ISWbemQualifier.get_IsAmended = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(17, 'get_IsAmended', ((1, 'bIsAmended'),)))
    return ISWbemQualifier
def _define_ISWbemQualifierSet_head():
    class ISWbemQualifierSet(win32more.System.Com.IDispatch_head):
        Guid = Guid('9b16ed16-d3df-11d1-8b08-00600806d9b6')
    return ISWbemQualifierSet
def _define_ISWbemQualifierSet():
    ISWbemQualifierSet = win32more.System.Wmi.ISWbemQualifierSet_head
    ISWbemQualifierSet.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'pUnk'),)))
    ISWbemQualifierSet.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,POINTER(win32more.System.Wmi.ISWbemQualifier_head), use_last_error=False)(8, 'Item', ((1, 'name'),(1, 'iFlags'),(1, 'objWbemQualifier'),)))
    ISWbemQualifierSet.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'iCount'),)))
    ISWbemQualifierSet.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(win32more.System.Com.VARIANT_head),Int16,Int16,Int16,Int32,POINTER(win32more.System.Wmi.ISWbemQualifier_head), use_last_error=False)(10, 'Add', ((1, 'strName'),(1, 'varVal'),(1, 'bPropagatesToSubclass'),(1, 'bPropagatesToInstance'),(1, 'bIsOverridable'),(1, 'iFlags'),(1, 'objWbemQualifier'),)))
    ISWbemQualifierSet.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32, use_last_error=False)(11, 'Remove', ((1, 'strName'),(1, 'iFlags'),)))
    return ISWbemQualifierSet
def _define_ISWbemProperty_head():
    class ISWbemProperty(win32more.System.Com.IDispatch_head):
        Guid = Guid('1a388f98-d4ba-11d1-8b09-00600806d9b6')
    return ISWbemProperty
def _define_ISWbemProperty():
    ISWbemProperty = win32more.System.Wmi.ISWbemProperty_head
    ISWbemProperty.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(7, 'get_Value', ((1, 'varValue'),)))
    ISWbemProperty.put_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(8, 'put_Value', ((1, 'varValue'),)))
    ISWbemProperty.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_Name', ((1, 'strName'),)))
    ISWbemProperty.get_IsLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(10, 'get_IsLocal', ((1, 'bIsLocal'),)))
    ISWbemProperty.get_Origin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_Origin', ((1, 'strOrigin'),)))
    ISWbemProperty.get_CIMType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.WbemCimtypeEnum), use_last_error=False)(12, 'get_CIMType', ((1, 'iCimType'),)))
    ISWbemProperty.get_Qualifiers_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.ISWbemQualifierSet_head), use_last_error=False)(13, 'get_Qualifiers_', ((1, 'objWbemQualifierSet'),)))
    ISWbemProperty.get_IsArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(14, 'get_IsArray', ((1, 'bIsArray'),)))
    return ISWbemProperty
def _define_ISWbemPropertySet_head():
    class ISWbemPropertySet(win32more.System.Com.IDispatch_head):
        Guid = Guid('dea0a7b2-d4ba-11d1-8b09-00600806d9b6')
    return ISWbemPropertySet
def _define_ISWbemPropertySet():
    ISWbemPropertySet = win32more.System.Wmi.ISWbemPropertySet_head
    ISWbemPropertySet.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'pUnk'),)))
    ISWbemPropertySet.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,POINTER(win32more.System.Wmi.ISWbemProperty_head), use_last_error=False)(8, 'Item', ((1, 'strName'),(1, 'iFlags'),(1, 'objWbemProperty'),)))
    ISWbemPropertySet.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'iCount'),)))
    ISWbemPropertySet.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Wmi.WbemCimtypeEnum,Int16,Int32,POINTER(win32more.System.Wmi.ISWbemProperty_head), use_last_error=False)(10, 'Add', ((1, 'strName'),(1, 'iCIMType'),(1, 'bIsArray'),(1, 'iFlags'),(1, 'objWbemProperty'),)))
    ISWbemPropertySet.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32, use_last_error=False)(11, 'Remove', ((1, 'strName'),(1, 'iFlags'),)))
    return ISWbemPropertySet
def _define_ISWbemMethod_head():
    class ISWbemMethod(win32more.System.Com.IDispatch_head):
        Guid = Guid('422e8e90-d955-11d1-8b09-00600806d9b6')
    return ISWbemMethod
def _define_ISWbemMethod():
    ISWbemMethod = win32more.System.Wmi.ISWbemMethod_head
    ISWbemMethod.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Name', ((1, 'strName'),)))
    ISWbemMethod.get_Origin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'get_Origin', ((1, 'strOrigin'),)))
    ISWbemMethod.get_InParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.ISWbemObject_head), use_last_error=False)(9, 'get_InParameters', ((1, 'objWbemInParameters'),)))
    ISWbemMethod.get_OutParameters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.ISWbemObject_head), use_last_error=False)(10, 'get_OutParameters', ((1, 'objWbemOutParameters'),)))
    ISWbemMethod.get_Qualifiers_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.ISWbemQualifierSet_head), use_last_error=False)(11, 'get_Qualifiers_', ((1, 'objWbemQualifierSet'),)))
    return ISWbemMethod
def _define_ISWbemMethodSet_head():
    class ISWbemMethodSet(win32more.System.Com.IDispatch_head):
        Guid = Guid('c93ba292-d955-11d1-8b09-00600806d9b6')
    return ISWbemMethodSet
def _define_ISWbemMethodSet():
    ISWbemMethodSet = win32more.System.Wmi.ISWbemMethodSet_head
    ISWbemMethodSet.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'pUnk'),)))
    ISWbemMethodSet.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,POINTER(win32more.System.Wmi.ISWbemMethod_head), use_last_error=False)(8, 'Item', ((1, 'strName'),(1, 'iFlags'),(1, 'objWbemMethod'),)))
    ISWbemMethodSet.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'iCount'),)))
    return ISWbemMethodSet
def _define_ISWbemEventSource_head():
    class ISWbemEventSource(win32more.System.Com.IDispatch_head):
        Guid = Guid('27d54d92-0ebe-11d2-8b22-00600806d9b6')
    return ISWbemEventSource
def _define_ISWbemEventSource():
    ISWbemEventSource = win32more.System.Wmi.ISWbemEventSource_head
    ISWbemEventSource.NextEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Wmi.ISWbemObject_head), use_last_error=False)(7, 'NextEvent', ((1, 'iTimeoutMs'),(1, 'objWbemObject'),)))
    ISWbemEventSource.get_Security_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.ISWbemSecurity_head), use_last_error=False)(8, 'get_Security_', ((1, 'objWbemSecurity'),)))
    return ISWbemEventSource
def _define_ISWbemObjectPath_head():
    class ISWbemObjectPath(win32more.System.Com.IDispatch_head):
        Guid = Guid('5791bc27-ce9c-11d1-97bf-0000f81e849c')
    return ISWbemObjectPath
def _define_ISWbemObjectPath():
    ISWbemObjectPath = win32more.System.Wmi.ISWbemObjectPath_head
    ISWbemObjectPath.get_Path = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Path', ((1, 'strPath'),)))
    ISWbemObjectPath.put_Path = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_Path', ((1, 'strPath'),)))
    ISWbemObjectPath.get_RelPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_RelPath', ((1, 'strRelPath'),)))
    ISWbemObjectPath.put_RelPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(10, 'put_RelPath', ((1, 'strRelPath'),)))
    ISWbemObjectPath.get_Server = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'get_Server', ((1, 'strServer'),)))
    ISWbemObjectPath.put_Server = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(12, 'put_Server', ((1, 'strServer'),)))
    ISWbemObjectPath.get_Namespace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'get_Namespace', ((1, 'strNamespace'),)))
    ISWbemObjectPath.put_Namespace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(14, 'put_Namespace', ((1, 'strNamespace'),)))
    ISWbemObjectPath.get_ParentNamespace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(15, 'get_ParentNamespace', ((1, 'strParentNamespace'),)))
    ISWbemObjectPath.get_DisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(16, 'get_DisplayName', ((1, 'strDisplayName'),)))
    ISWbemObjectPath.put_DisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(17, 'put_DisplayName', ((1, 'strDisplayName'),)))
    ISWbemObjectPath.get_Class = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(18, 'get_Class', ((1, 'strClass'),)))
    ISWbemObjectPath.put_Class = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(19, 'put_Class', ((1, 'strClass'),)))
    ISWbemObjectPath.get_IsClass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(20, 'get_IsClass', ((1, 'bIsClass'),)))
    ISWbemObjectPath.SetAsClass = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(21, 'SetAsClass', ()))
    ISWbemObjectPath.get_IsSingleton = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(22, 'get_IsSingleton', ((1, 'bIsSingleton'),)))
    ISWbemObjectPath.SetAsSingleton = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(23, 'SetAsSingleton', ()))
    ISWbemObjectPath.get_Keys = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.ISWbemNamedValueSet_head), use_last_error=False)(24, 'get_Keys', ((1, 'objWbemNamedValueSet'),)))
    ISWbemObjectPath.get_Security_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.ISWbemSecurity_head), use_last_error=False)(25, 'get_Security_', ((1, 'objWbemSecurity'),)))
    ISWbemObjectPath.get_Locale = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(26, 'get_Locale', ((1, 'strLocale'),)))
    ISWbemObjectPath.put_Locale = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(27, 'put_Locale', ((1, 'strLocale'),)))
    ISWbemObjectPath.get_Authority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(28, 'get_Authority', ((1, 'strAuthority'),)))
    ISWbemObjectPath.put_Authority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(29, 'put_Authority', ((1, 'strAuthority'),)))
    return ISWbemObjectPath
def _define_ISWbemLastError_head():
    class ISWbemLastError(win32more.System.Wmi.ISWbemObject_head):
        Guid = Guid('d962db84-d4bb-11d1-8b09-00600806d9b6')
    return ISWbemLastError
def _define_ISWbemLastError():
    ISWbemLastError = win32more.System.Wmi.ISWbemLastError_head
    return ISWbemLastError
def _define_ISWbemSinkEvents_head():
    class ISWbemSinkEvents(win32more.System.Com.IDispatch_head):
        Guid = Guid('75718ca0-f029-11d1-a1ac-00c04fb6c223')
    return ISWbemSinkEvents
def _define_ISWbemSinkEvents():
    ISWbemSinkEvents = win32more.System.Wmi.ISWbemSinkEvents_head
    return ISWbemSinkEvents
def _define_ISWbemSink_head():
    class ISWbemSink(win32more.System.Com.IDispatch_head):
        Guid = Guid('75718c9f-f029-11d1-a1ac-00c04fb6c223')
    return ISWbemSink
def _define_ISWbemSink():
    ISWbemSink = win32more.System.Wmi.ISWbemSink_head
    ISWbemSink.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Cancel', ()))
    return ISWbemSink
def _define_ISWbemSecurity_head():
    class ISWbemSecurity(win32more.System.Com.IDispatch_head):
        Guid = Guid('b54d66e6-2287-11d2-8b33-00600806d9b6')
    return ISWbemSecurity
def _define_ISWbemSecurity():
    ISWbemSecurity = win32more.System.Wmi.ISWbemSecurity_head
    ISWbemSecurity.get_ImpersonationLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.WbemImpersonationLevelEnum), use_last_error=False)(7, 'get_ImpersonationLevel', ((1, 'iImpersonationLevel'),)))
    ISWbemSecurity.put_ImpersonationLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Wmi.WbemImpersonationLevelEnum, use_last_error=False)(8, 'put_ImpersonationLevel', ((1, 'iImpersonationLevel'),)))
    ISWbemSecurity.get_AuthenticationLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.WbemAuthenticationLevelEnum), use_last_error=False)(9, 'get_AuthenticationLevel', ((1, 'iAuthenticationLevel'),)))
    ISWbemSecurity.put_AuthenticationLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Wmi.WbemAuthenticationLevelEnum, use_last_error=False)(10, 'put_AuthenticationLevel', ((1, 'iAuthenticationLevel'),)))
    ISWbemSecurity.get_Privileges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.ISWbemPrivilegeSet_head), use_last_error=False)(11, 'get_Privileges', ((1, 'objWbemPrivilegeSet'),)))
    return ISWbemSecurity
def _define_ISWbemPrivilege_head():
    class ISWbemPrivilege(win32more.System.Com.IDispatch_head):
        Guid = Guid('26ee67bd-5804-11d2-8b4a-00600806d9b6')
    return ISWbemPrivilege
def _define_ISWbemPrivilege():
    ISWbemPrivilege = win32more.System.Wmi.ISWbemPrivilege_head
    ISWbemPrivilege.get_IsEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(7, 'get_IsEnabled', ((1, 'bIsEnabled'),)))
    ISWbemPrivilege.put_IsEnabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(8, 'put_IsEnabled', ((1, 'bIsEnabled'),)))
    ISWbemPrivilege.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(9, 'get_Name', ((1, 'strDisplayName'),)))
    ISWbemPrivilege.get_DisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(10, 'get_DisplayName', ((1, 'strDisplayName'),)))
    ISWbemPrivilege.get_Identifier = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.WbemPrivilegeEnum), use_last_error=False)(11, 'get_Identifier', ((1, 'iPrivilege'),)))
    return ISWbemPrivilege
def _define_ISWbemPrivilegeSet_head():
    class ISWbemPrivilegeSet(win32more.System.Com.IDispatch_head):
        Guid = Guid('26ee67bf-5804-11d2-8b4a-00600806d9b6')
    return ISWbemPrivilegeSet
def _define_ISWbemPrivilegeSet():
    ISWbemPrivilegeSet = win32more.System.Wmi.ISWbemPrivilegeSet_head
    ISWbemPrivilegeSet.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'pUnk'),)))
    ISWbemPrivilegeSet.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Wmi.WbemPrivilegeEnum,POINTER(win32more.System.Wmi.ISWbemPrivilege_head), use_last_error=False)(8, 'Item', ((1, 'iPrivilege'),(1, 'objWbemPrivilege'),)))
    ISWbemPrivilegeSet.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'iCount'),)))
    ISWbemPrivilegeSet.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Wmi.WbemPrivilegeEnum,Int16,POINTER(win32more.System.Wmi.ISWbemPrivilege_head), use_last_error=False)(10, 'Add', ((1, 'iPrivilege'),(1, 'bIsEnabled'),(1, 'objWbemPrivilege'),)))
    ISWbemPrivilegeSet.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Wmi.WbemPrivilegeEnum, use_last_error=False)(11, 'Remove', ((1, 'iPrivilege'),)))
    ISWbemPrivilegeSet.DeleteAll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'DeleteAll', ()))
    ISWbemPrivilegeSet.AddAsString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int16,POINTER(win32more.System.Wmi.ISWbemPrivilege_head), use_last_error=False)(13, 'AddAsString', ((1, 'strPrivilege'),(1, 'bIsEnabled'),(1, 'objWbemPrivilege'),)))
    return ISWbemPrivilegeSet
def _define_ISWbemServicesEx_head():
    class ISWbemServicesEx(win32more.System.Wmi.ISWbemServices_head):
        Guid = Guid('d2f68443-85dc-427e-91d8-366554cc754c')
    return ISWbemServicesEx
def _define_ISWbemServicesEx():
    ISWbemServicesEx = win32more.System.Wmi.ISWbemServicesEx_head
    ISWbemServicesEx.Put = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Wmi.ISWbemObjectEx_head,Int32,win32more.System.Com.IDispatch_head,POINTER(win32more.System.Wmi.ISWbemObjectPath_head), use_last_error=False)(26, 'Put', ((1, 'objWbemObject'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemObjectPath'),)))
    ISWbemServicesEx.PutAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Wmi.ISWbemSink_head,win32more.System.Wmi.ISWbemObjectEx_head,Int32,win32more.System.Com.IDispatch_head,win32more.System.Com.IDispatch_head, use_last_error=False)(27, 'PutAsync', ((1, 'objWbemSink'),(1, 'objWbemObject'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemAsyncContext'),)))
    return ISWbemServicesEx
def _define_ISWbemObjectEx_head():
    class ISWbemObjectEx(win32more.System.Wmi.ISWbemObject_head):
        Guid = Guid('269ad56a-8a67-4129-bc8c-0506dcfe9880')
    return ISWbemObjectEx
def _define_ISWbemObjectEx():
    ISWbemObjectEx = win32more.System.Wmi.ISWbemObjectEx_head
    ISWbemObjectEx.Refresh_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.IDispatch_head, use_last_error=False)(32, 'Refresh_', ((1, 'iFlags'),(1, 'objWbemNamedValueSet'),)))
    ISWbemObjectEx.get_SystemProperties_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.ISWbemPropertySet_head), use_last_error=False)(33, 'get_SystemProperties_', ((1, 'objWbemPropertySet'),)))
    ISWbemObjectEx.GetText_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Wmi.WbemObjectTextFormatEnum,Int32,win32more.System.Com.IDispatch_head,POINTER(win32more.Foundation.BSTR), use_last_error=False)(34, 'GetText_', ((1, 'iObjectTextFormat'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'bsText'),)))
    ISWbemObjectEx.SetFromText_ = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.System.Wmi.WbemObjectTextFormatEnum,Int32,win32more.System.Com.IDispatch_head, use_last_error=False)(35, 'SetFromText_', ((1, 'bsText'),(1, 'iObjectTextFormat'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),)))
    return ISWbemObjectEx
def _define_ISWbemDateTime_head():
    class ISWbemDateTime(win32more.System.Com.IDispatch_head):
        Guid = Guid('5e97458a-cf77-11d3-b38f-00105a1f473a')
    return ISWbemDateTime
def _define_ISWbemDateTime():
    ISWbemDateTime = win32more.System.Wmi.ISWbemDateTime_head
    ISWbemDateTime.get_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_Value', ((1, 'strValue'),)))
    ISWbemDateTime.put_Value = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'put_Value', ((1, 'strValue'),)))
    ISWbemDateTime.get_Year = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Year', ((1, 'iYear'),)))
    ISWbemDateTime.put_Year = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(10, 'put_Year', ((1, 'iYear'),)))
    ISWbemDateTime.get_YearSpecified = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(11, 'get_YearSpecified', ((1, 'bYearSpecified'),)))
    ISWbemDateTime.put_YearSpecified = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(12, 'put_YearSpecified', ((1, 'bYearSpecified'),)))
    ISWbemDateTime.get_Month = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(13, 'get_Month', ((1, 'iMonth'),)))
    ISWbemDateTime.put_Month = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(14, 'put_Month', ((1, 'iMonth'),)))
    ISWbemDateTime.get_MonthSpecified = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(15, 'get_MonthSpecified', ((1, 'bMonthSpecified'),)))
    ISWbemDateTime.put_MonthSpecified = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(16, 'put_MonthSpecified', ((1, 'bMonthSpecified'),)))
    ISWbemDateTime.get_Day = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(17, 'get_Day', ((1, 'iDay'),)))
    ISWbemDateTime.put_Day = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(18, 'put_Day', ((1, 'iDay'),)))
    ISWbemDateTime.get_DaySpecified = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(19, 'get_DaySpecified', ((1, 'bDaySpecified'),)))
    ISWbemDateTime.put_DaySpecified = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(20, 'put_DaySpecified', ((1, 'bDaySpecified'),)))
    ISWbemDateTime.get_Hours = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(21, 'get_Hours', ((1, 'iHours'),)))
    ISWbemDateTime.put_Hours = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(22, 'put_Hours', ((1, 'iHours'),)))
    ISWbemDateTime.get_HoursSpecified = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(23, 'get_HoursSpecified', ((1, 'bHoursSpecified'),)))
    ISWbemDateTime.put_HoursSpecified = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(24, 'put_HoursSpecified', ((1, 'bHoursSpecified'),)))
    ISWbemDateTime.get_Minutes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(25, 'get_Minutes', ((1, 'iMinutes'),)))
    ISWbemDateTime.put_Minutes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(26, 'put_Minutes', ((1, 'iMinutes'),)))
    ISWbemDateTime.get_MinutesSpecified = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(27, 'get_MinutesSpecified', ((1, 'bMinutesSpecified'),)))
    ISWbemDateTime.put_MinutesSpecified = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(28, 'put_MinutesSpecified', ((1, 'bMinutesSpecified'),)))
    ISWbemDateTime.get_Seconds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(29, 'get_Seconds', ((1, 'iSeconds'),)))
    ISWbemDateTime.put_Seconds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(30, 'put_Seconds', ((1, 'iSeconds'),)))
    ISWbemDateTime.get_SecondsSpecified = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(31, 'get_SecondsSpecified', ((1, 'bSecondsSpecified'),)))
    ISWbemDateTime.put_SecondsSpecified = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(32, 'put_SecondsSpecified', ((1, 'bSecondsSpecified'),)))
    ISWbemDateTime.get_Microseconds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(33, 'get_Microseconds', ((1, 'iMicroseconds'),)))
    ISWbemDateTime.put_Microseconds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(34, 'put_Microseconds', ((1, 'iMicroseconds'),)))
    ISWbemDateTime.get_MicrosecondsSpecified = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(35, 'get_MicrosecondsSpecified', ((1, 'bMicrosecondsSpecified'),)))
    ISWbemDateTime.put_MicrosecondsSpecified = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(36, 'put_MicrosecondsSpecified', ((1, 'bMicrosecondsSpecified'),)))
    ISWbemDateTime.get_UTC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(37, 'get_UTC', ((1, 'iUTC'),)))
    ISWbemDateTime.put_UTC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(38, 'put_UTC', ((1, 'iUTC'),)))
    ISWbemDateTime.get_UTCSpecified = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(39, 'get_UTCSpecified', ((1, 'bUTCSpecified'),)))
    ISWbemDateTime.put_UTCSpecified = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(40, 'put_UTCSpecified', ((1, 'bUTCSpecified'),)))
    ISWbemDateTime.get_IsInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(41, 'get_IsInterval', ((1, 'bIsInterval'),)))
    ISWbemDateTime.put_IsInterval = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(42, 'put_IsInterval', ((1, 'bIsInterval'),)))
    ISWbemDateTime.GetVarDate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,POINTER(Double), use_last_error=False)(43, 'GetVarDate', ((1, 'bIsLocal'),(1, 'dVarDate'),)))
    ISWbemDateTime.SetVarDate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Int16, use_last_error=False)(44, 'SetVarDate', ((1, 'dVarDate'),(1, 'bIsLocal'),)))
    ISWbemDateTime.GetFileTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,POINTER(win32more.Foundation.BSTR), use_last_error=False)(45, 'GetFileTime', ((1, 'bIsLocal'),(1, 'strFileTime'),)))
    ISWbemDateTime.SetFileTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int16, use_last_error=False)(46, 'SetFileTime', ((1, 'strFileTime'),(1, 'bIsLocal'),)))
    return ISWbemDateTime
def _define_ISWbemRefresher_head():
    class ISWbemRefresher(win32more.System.Com.IDispatch_head):
        Guid = Guid('14d8250e-d9c2-11d3-b38f-00105a1f473a')
    return ISWbemRefresher
def _define_ISWbemRefresher():
    ISWbemRefresher = win32more.System.Wmi.ISWbemRefresher_head
    ISWbemRefresher.get__NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'get__NewEnum', ((1, 'pUnk'),)))
    ISWbemRefresher.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Wmi.ISWbemRefreshableItem_head), use_last_error=False)(8, 'Item', ((1, 'iIndex'),(1, 'objWbemRefreshableItem'),)))
    ISWbemRefresher.get_Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'get_Count', ((1, 'iCount'),)))
    ISWbemRefresher.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Wmi.ISWbemServicesEx_head,win32more.Foundation.BSTR,Int32,win32more.System.Com.IDispatch_head,POINTER(win32more.System.Wmi.ISWbemRefreshableItem_head), use_last_error=False)(10, 'Add', ((1, 'objWbemServices'),(1, 'bsInstancePath'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemRefreshableItem'),)))
    ISWbemRefresher.AddEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Wmi.ISWbemServicesEx_head,win32more.Foundation.BSTR,Int32,win32more.System.Com.IDispatch_head,POINTER(win32more.System.Wmi.ISWbemRefreshableItem_head), use_last_error=False)(11, 'AddEnum', ((1, 'objWbemServices'),(1, 'bsClassName'),(1, 'iFlags'),(1, 'objWbemNamedValueSet'),(1, 'objWbemRefreshableItem'),)))
    ISWbemRefresher.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(12, 'Remove', ((1, 'iIndex'),(1, 'iFlags'),)))
    ISWbemRefresher.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(13, 'Refresh', ((1, 'iFlags'),)))
    ISWbemRefresher.get_AutoReconnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(14, 'get_AutoReconnect', ((1, 'bCount'),)))
    ISWbemRefresher.put_AutoReconnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(15, 'put_AutoReconnect', ((1, 'bCount'),)))
    ISWbemRefresher.DeleteAll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(16, 'DeleteAll', ()))
    return ISWbemRefresher
def _define_ISWbemRefreshableItem_head():
    class ISWbemRefreshableItem(win32more.System.Com.IDispatch_head):
        Guid = Guid('5ad4bf92-daab-11d3-b38f-00105a1f473a')
    return ISWbemRefreshableItem
def _define_ISWbemRefreshableItem():
    ISWbemRefreshableItem = win32more.System.Wmi.ISWbemRefreshableItem_head
    ISWbemRefreshableItem.get_Index = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Index', ((1, 'iIndex'),)))
    ISWbemRefreshableItem.get_Refresher = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.ISWbemRefresher_head), use_last_error=False)(8, 'get_Refresher', ((1, 'objWbemRefresher'),)))
    ISWbemRefreshableItem.get_IsSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(9, 'get_IsSet', ((1, 'bIsSet'),)))
    ISWbemRefreshableItem.get_Object = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.ISWbemObjectEx_head), use_last_error=False)(10, 'get_Object', ((1, 'objWbemObject'),)))
    ISWbemRefreshableItem.get_ObjectSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.ISWbemObjectSet_head), use_last_error=False)(11, 'get_ObjectSet', ((1, 'objWbemObjectSet'),)))
    ISWbemRefreshableItem.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(12, 'Remove', ((1, 'iFlags'),)))
    return ISWbemRefreshableItem
WMIExtension = Guid('f0975afe-5c7f-11d2-8b74-00104b2afb41')
def _define_IWMIExtension_head():
    class IWMIExtension(win32more.System.Com.IDispatch_head):
        Guid = Guid('adc1f06e-5c7e-11d2-8b74-00104b2afb41')
    return IWMIExtension
def _define_IWMIExtension():
    IWMIExtension = win32more.System.Wmi.IWMIExtension_head
    IWMIExtension.get_WMIObjectPath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'get_WMIObjectPath', ((1, 'strWMIObjectPath'),)))
    IWMIExtension.GetWMIObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.ISWbemObject_head), use_last_error=False)(8, 'GetWMIObject', ((1, 'objWMIObject'),)))
    IWMIExtension.GetWMIServices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Wmi.ISWbemServices_head), use_last_error=False)(9, 'GetWMIServices', ((1, 'objWMIServices'),)))
    return IWMIExtension
WbemLevel1Login = Guid('8bc3f05e-d86b-11d0-a075-00c04fb68820')
WbemLocalAddrRes = Guid('a1044801-8f7e-11d1-9e7c-00c04fc324a8')
WbemUninitializedClassObject = Guid('7a0227f6-7108-11d1-ad90-00c04fd8fdff')
WbemDCOMTransport = Guid('f7ce2e13-8c90-11d1-9e7b-00c04fc324a8')
tag_WBEM_LOGIN_TYPE = Int32
WBEM_FLAG_INPROC_LOGIN = 0
WBEM_FLAG_LOCAL_LOGIN = 1
WBEM_FLAG_REMOTE_LOGIN = 2
WBEM_AUTHENTICATION_METHOD_MASK = 15
WBEM_FLAG_USE_MULTIPLE_CHALLENGES = 16
def _define_IWbemTransport_head():
    class IWbemTransport(win32more.System.Com.IUnknown_head):
        Guid = Guid('553fe584-2156-11d0-b6ae-00aa003240c7')
    return IWbemTransport
def _define_IWbemTransport():
    IWbemTransport = win32more.System.Wmi.IWbemTransport_head
    IWbemTransport.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Initialize', ()))
    return IWbemTransport
def _define_IWbemLevel1Login_head():
    class IWbemLevel1Login(win32more.System.Com.IUnknown_head):
        Guid = Guid('f309ad18-d86a-11d0-a075-00c04fb68820')
    return IWbemLevel1Login
def _define_IWbemLevel1Login():
    IWbemLevel1Login = win32more.System.Wmi.IWbemLevel1Login_head
    IWbemLevel1Login.EstablishPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32), use_last_error=False)(3, 'EstablishPosition', ((1, 'wszLocaleList'),(1, 'dwNumLocales'),(1, 'reserved'),)))
    IWbemLevel1Login.RequestChallenge = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_char_p_no, use_last_error=False)(4, 'RequestChallenge', ((1, 'wszNetworkResource'),(1, 'wszUser'),(1, 'Nonce'),)))
    IWbemLevel1Login.WBEMLogin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,c_char_p_no,Int32,win32more.System.Wmi.IWbemContext_head,POINTER(win32more.System.Wmi.IWbemServices_head), use_last_error=False)(5, 'WBEMLogin', ((1, 'wszPreferredLocale'),(1, 'AccessToken'),(1, 'lFlags'),(1, 'pCtx'),(1, 'ppNamespace'),)))
    IWbemLevel1Login.NTLMLogin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Int32,win32more.System.Wmi.IWbemContext_head,POINTER(win32more.System.Wmi.IWbemServices_head), use_last_error=False)(6, 'NTLMLogin', ((1, 'wszNetworkResource'),(1, 'wszPreferredLocale'),(1, 'lFlags'),(1, 'pCtx'),(1, 'ppNamespace'),)))
    return IWbemLevel1Login
def _define_IWbemConnectorLogin_head():
    class IWbemConnectorLogin(win32more.System.Com.IUnknown_head):
        Guid = Guid('d8ec9cb1-b135-4f10-8b1b-c7188bb0d186')
    return IWbemConnectorLogin
def _define_IWbemConnectorLogin():
    IWbemConnectorLogin = win32more.System.Wmi.IWbemConnectorLogin_head
    IWbemConnectorLogin.ConnectorLogin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Int32,win32more.System.Wmi.IWbemContext_head,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(3, 'ConnectorLogin', ((1, 'wszNetworkResource'),(1, 'wszPreferredLocale'),(1, 'lFlags'),(1, 'pCtx'),(1, 'riid'),(1, 'pInterface'),)))
    return IWbemConnectorLogin
def _define_IWbemAddressResolution_head():
    class IWbemAddressResolution(win32more.System.Com.IUnknown_head):
        Guid = Guid('f7ce2e12-8c90-11d1-9e7b-00c04fc324a8')
    return IWbemAddressResolution
def _define_IWbemAddressResolution():
    IWbemAddressResolution = win32more.System.Wmi.IWbemAddressResolution_head
    IWbemAddressResolution.Resolve = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(c_char_p_no), use_last_error=False)(3, 'Resolve', ((1, 'wszNamespacePath'),(1, 'wszAddressType'),(1, 'pdwAddressLength'),(1, 'pabBinaryAddress'),)))
    return IWbemAddressResolution
def _define_IWbemClientTransport_head():
    class IWbemClientTransport(win32more.System.Com.IUnknown_head):
        Guid = Guid('f7ce2e11-8c90-11d1-9e7b-00c04fc324a8')
    return IWbemClientTransport
def _define_IWbemClientTransport():
    IWbemClientTransport = win32more.System.Wmi.IWbemClientTransport_head
    IWbemClientTransport.ConnectServer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,UInt32,POINTER(Byte),win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,win32more.Foundation.BSTR,win32more.System.Wmi.IWbemContext_head,POINTER(win32more.System.Wmi.IWbemServices_head), use_last_error=False)(3, 'ConnectServer', ((1, 'strAddressType'),(1, 'dwBinaryAddressLength'),(1, 'abBinaryAddress'),(1, 'strNetworkResource'),(1, 'strUser'),(1, 'strPassword'),(1, 'strLocale'),(1, 'lSecurityFlags'),(1, 'strAuthority'),(1, 'pCtx'),(1, 'ppNamespace'),)))
    return IWbemClientTransport
def _define_IWbemClientConnectionTransport_head():
    class IWbemClientConnectionTransport(win32more.System.Com.IUnknown_head):
        Guid = Guid('a889c72a-fcc1-4a9e-af61-ed071333fb5b')
    return IWbemClientConnectionTransport
def _define_IWbemClientConnectionTransport():
    IWbemClientConnectionTransport = win32more.System.Wmi.IWbemClientConnectionTransport_head
    IWbemClientConnectionTransport.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,UInt32,POINTER(Byte),win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,win32more.System.Wmi.IWbemContext_head,POINTER(Guid),POINTER(c_void_p),POINTER(win32more.System.Wmi.IWbemCallResult_head), use_last_error=False)(3, 'Open', ((1, 'strAddressType'),(1, 'dwBinaryAddressLength'),(1, 'abBinaryAddress'),(1, 'strObject'),(1, 'strUser'),(1, 'strPassword'),(1, 'strLocale'),(1, 'lFlags'),(1, 'pCtx'),(1, 'riid'),(1, 'pInterface'),(1, 'pCallRes'),)))
    IWbemClientConnectionTransport.OpenAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,UInt32,POINTER(Byte),win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,win32more.Foundation.BSTR,Int32,win32more.System.Wmi.IWbemContext_head,POINTER(Guid),win32more.System.Wmi.IWbemObjectSink_head, use_last_error=False)(4, 'OpenAsync', ((1, 'strAddressType'),(1, 'dwBinaryAddressLength'),(1, 'abBinaryAddress'),(1, 'strObject'),(1, 'strUser'),(1, 'strPassword'),(1, 'strLocale'),(1, 'lFlags'),(1, 'pCtx'),(1, 'riid'),(1, 'pResponseHandler'),)))
    IWbemClientConnectionTransport.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Wmi.IWbemObjectSink_head, use_last_error=False)(5, 'Cancel', ((1, 'lFlags'),(1, 'pHandler'),)))
    return IWbemClientConnectionTransport
def _define_IWbemConstructClassObject_head():
    class IWbemConstructClassObject(win32more.System.Com.IUnknown_head):
        Guid = Guid('9ef76194-70d5-11d1-ad90-00c04fd8fdff')
    return IWbemConstructClassObject
def _define_IWbemConstructClassObject():
    IWbemConstructClassObject = win32more.System.Wmi.IWbemConstructClassObject_head
    IWbemConstructClassObject.SetInheritanceChain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'SetInheritanceChain', ((1, 'lNumAntecedents'),(1, 'awszAntecedents'),)))
    IWbemConstructClassObject.SetPropertyOrigin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Int32, use_last_error=False)(4, 'SetPropertyOrigin', ((1, 'wszPropertyName'),(1, 'lOriginIndex'),)))
    IWbemConstructClassObject.SetMethodOrigin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,Int32, use_last_error=False)(5, 'SetMethodOrigin', ((1, 'wszMethodName'),(1, 'lOriginIndex'),)))
    IWbemConstructClassObject.SetServerNamespace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(6, 'SetServerNamespace', ((1, 'wszServer'),(1, 'wszNamespace'),)))
    return IWbemConstructClassObject
def _define_MI_Application_InitializeV1():
    try:
        return WINFUNCTYPE(win32more.System.Wmi.MI_Result,UInt32,POINTER(UInt16),POINTER(POINTER(win32more.System.Wmi.MI_Instance_head)),POINTER(win32more.System.Wmi.MI_Application_head), use_last_error=False)(("MI_Application_InitializeV1", windll["mi"]), ((1, 'flags'),(1, 'applicationID'),(1, 'extendedError'),(1, 'application'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "MI_FLAG_ANY",
    "MI_FLAG_VERSION",
    "MI_FLAG_ADOPT",
    "MI_FLAG_CLASS",
    "MI_FLAG_METHOD",
    "MI_FLAG_PROPERTY",
    "MI_FLAG_PARAMETER",
    "MI_FLAG_ASSOCIATION",
    "MI_FLAG_INDICATION",
    "MI_FLAG_REFERENCE",
    "MI_FLAG_ENABLEOVERRIDE",
    "MI_FLAG_DISABLEOVERRIDE",
    "MI_FLAG_RESTRICTED",
    "MI_FLAG_TOSUBCLASS",
    "MI_FLAG_TRANSLATABLE",
    "MI_FLAG_KEY",
    "MI_FLAG_IN",
    "MI_FLAG_OUT",
    "MI_FLAG_REQUIRED",
    "MI_FLAG_STATIC",
    "MI_FLAG_ABSTRACT",
    "MI_FLAG_TERMINAL",
    "MI_FLAG_EXPENSIVE",
    "MI_FLAG_STREAM",
    "MI_FLAG_READONLY",
    "MI_FLAG_EXTENDED",
    "MI_FLAG_NOT_MODIFIED",
    "MI_FLAG_NULL",
    "MI_FLAG_BORROW",
    "MI_MODULE_FLAG_STANDARD_QUALIFIERS",
    "MI_MODULE_FLAG_DESCRIPTIONS",
    "MI_MODULE_FLAG_VALUES",
    "MI_MODULE_FLAG_MAPPING_STRINGS",
    "MI_MODULE_FLAG_BOOLEANS",
    "MI_MODULE_FLAG_CPLUSPLUS",
    "MI_MODULE_FLAG_LOCALIZED",
    "MI_MODULE_FLAG_FILTER_SUPPORT",
    "MI_MAX_LOCALE_SIZE",
    "MI_WRITEMESSAGE_CHANNEL_WARNING",
    "MI_WRITEMESSAGE_CHANNEL_VERBOSE",
    "MI_WRITEMESSAGE_CHANNEL_DEBUG",
    "MI_CALL_VERSION",
    "MI_OPERATIONFLAGS_MANUAL_ACK_RESULTS",
    "MI_OPERATIONFLAGS_NO_RTTI",
    "MI_OPERATIONFLAGS_BASIC_RTTI",
    "MI_OPERATIONFLAGS_STANDARD_RTTI",
    "MI_OPERATIONFLAGS_FULL_RTTI",
    "MI_OPERATIONFLAGS_DEFAULT_RTTI",
    "MI_OPERATIONFLAGS_LOCALIZED_QUALIFIERS",
    "MI_OPERATIONFLAGS_EXPENSIVE_PROPERTIES",
    "MI_OPERATIONFLAGS_POLYMORPHISM_SHALLOW",
    "MI_OPERATIONFLAGS_POLYMORPHISM_DEEP_BASE_PROPS_ONLY",
    "MI_OPERATIONFLAGS_REPORT_OPERATION_STARTED",
    "MI_SERIALIZER_FLAGS_CLASS_DEEP",
    "MI_SERIALIZER_FLAGS_INSTANCE_WITH_CLASS",
    "WBEMS_DISPID_DERIVATION",
    "WBEMS_DISPID_OBJECT_READY",
    "WBEMS_DISPID_COMPLETED",
    "WBEMS_DISPID_PROGRESS",
    "WBEMS_DISPID_OBJECT_PUT",
    "WBEMS_DISPID_CONNECTION_READY",
    "MI_Result",
    "MI_RESULT_OK",
    "MI_RESULT_FAILED",
    "MI_RESULT_ACCESS_DENIED",
    "MI_RESULT_INVALID_NAMESPACE",
    "MI_RESULT_INVALID_PARAMETER",
    "MI_RESULT_INVALID_CLASS",
    "MI_RESULT_NOT_FOUND",
    "MI_RESULT_NOT_SUPPORTED",
    "MI_RESULT_CLASS_HAS_CHILDREN",
    "MI_RESULT_CLASS_HAS_INSTANCES",
    "MI_RESULT_INVALID_SUPERCLASS",
    "MI_RESULT_ALREADY_EXISTS",
    "MI_RESULT_NO_SUCH_PROPERTY",
    "MI_RESULT_TYPE_MISMATCH",
    "MI_RESULT_QUERY_LANGUAGE_NOT_SUPPORTED",
    "MI_RESULT_INVALID_QUERY",
    "MI_RESULT_METHOD_NOT_AVAILABLE",
    "MI_RESULT_METHOD_NOT_FOUND",
    "MI_RESULT_NAMESPACE_NOT_EMPTY",
    "MI_RESULT_INVALID_ENUMERATION_CONTEXT",
    "MI_RESULT_INVALID_OPERATION_TIMEOUT",
    "MI_RESULT_PULL_HAS_BEEN_ABANDONED",
    "MI_RESULT_PULL_CANNOT_BE_ABANDONED",
    "MI_RESULT_FILTERED_ENUMERATION_NOT_SUPPORTED",
    "MI_RESULT_CONTINUATION_ON_ERROR_NOT_SUPPORTED",
    "MI_RESULT_SERVER_LIMITS_EXCEEDED",
    "MI_RESULT_SERVER_IS_SHUTTING_DOWN",
    "MI_ErrorCategory",
    "MI_ERRORCATEGORY_NOT_SPECIFIED",
    "MI_ERRORCATEGORY_OPEN_ERROR",
    "MI_ERRORCATEGORY_CLOS_EERROR",
    "MI_ERRORCATEGORY_DEVICE_ERROR",
    "MI_ERRORCATEGORY_DEADLOCK_DETECTED",
    "MI_ERRORCATEGORY_INVALID_ARGUMENT",
    "MI_ERRORCATEGORY_INVALID_DATA",
    "MI_ERRORCATEGORY_INVALID_OPERATION",
    "MI_ERRORCATEGORY_INVALID_RESULT",
    "MI_ERRORCATEGORY_INVALID_TYPE",
    "MI_ERRORCATEGORY_METADATA_ERROR",
    "MI_ERRORCATEGORY_NOT_IMPLEMENTED",
    "MI_ERRORCATEGORY_NOT_INSTALLED",
    "MI_ERRORCATEGORY_OBJECT_NOT_FOUND",
    "MI_ERRORCATEGORY_OPERATION_STOPPED",
    "MI_ERRORCATEGORY_OPERATION_TIMEOUT",
    "MI_ERRORCATEGORY_SYNTAX_ERROR",
    "MI_ERRORCATEGORY_PARSER_ERROR",
    "MI_ERRORCATEGORY_ACCESS_DENIED",
    "MI_ERRORCATEGORY_RESOURCE_BUSY",
    "MI_ERRORCATEGORY_RESOURCE_EXISTS",
    "MI_ERRORCATEGORY_RESOURCE_UNAVAILABLE",
    "MI_ERRORCATEGORY_READ_ERROR",
    "MI_ERRORCATEGORY_WRITE_ERROR",
    "MI_ERRORCATEGORY_FROM_STDERR",
    "MI_ERRORCATEGORY_SECURITY_ERROR",
    "MI_ERRORCATEGORY_PROTOCOL_ERROR",
    "MI_ERRORCATEGORY_CONNECTION_ERROR",
    "MI_ERRORCATEGORY_AUTHENTICATION_ERROR",
    "MI_ERRORCATEGORY_LIMITS_EXCEEDED",
    "MI_ERRORCATEGORY_QUOTA_EXCEEDED",
    "MI_ERRORCATEGORY_NOT_ENABLED",
    "MI_PromptType",
    "MI_PROMPTTYPE_NORMAL",
    "MI_PROMPTTYPE_CRITICAL",
    "MI_CallbackMode",
    "MI_CALLBACKMODE_REPORT",
    "MI_CALLBACKMODE_INQUIRE",
    "MI_CALLBACKMODE_IGNORE",
    "MI_ProviderArchitecture",
    "MI_PROVIDER_ARCHITECTURE_32BIT",
    "MI_PROVIDER_ARCHITECTURE_64BIT",
    "MI_Type",
    "MI_BOOLEAN",
    "MI_UINT8",
    "MI_SINT8",
    "MI_UINT16",
    "MI_SINT16",
    "MI_UINT32",
    "MI_SINT32",
    "MI_UINT64",
    "MI_SINT64",
    "MI_REAL32",
    "MI_REAL64",
    "MI_CHAR16",
    "MI_DATETIME",
    "MI_STRING",
    "MI_REFERENCE",
    "MI_INSTANCE",
    "MI_BOOLEANA",
    "MI_UINT8A",
    "MI_SINT8A",
    "MI_UINT16A",
    "MI_SINT16A",
    "MI_UINT32A",
    "MI_SINT32A",
    "MI_UINT64A",
    "MI_SINT64A",
    "MI_REAL32A",
    "MI_REAL64A",
    "MI_CHAR16A",
    "MI_DATETIMEA",
    "MI_STRINGA",
    "MI_REFERENCEA",
    "MI_INSTANCEA",
    "MI_ARRAY",
    "MI_Timestamp",
    "MI_Interval",
    "MI_Datetime",
    "MI_BooleanA",
    "MI_Uint8A",
    "MI_Sint8A",
    "MI_Uint16A",
    "MI_Sint16A",
    "MI_Uint32A",
    "MI_Sint32A",
    "MI_Uint64A",
    "MI_Sint64A",
    "MI_Real32A",
    "MI_Real64A",
    "MI_Char16A",
    "MI_DatetimeA",
    "MI_StringA",
    "MI_ReferenceA",
    "MI_InstanceA",
    "MI_Array",
    "MI_ConstBooleanA",
    "MI_ConstUint8A",
    "MI_ConstSint8A",
    "MI_ConstUint16A",
    "MI_ConstSint16A",
    "MI_ConstUint32A",
    "MI_ConstSint32A",
    "MI_ConstUint64A",
    "MI_ConstSint64A",
    "MI_ConstReal32A",
    "MI_ConstReal64A",
    "MI_ConstChar16A",
    "MI_ConstDatetimeA",
    "MI_ConstStringA",
    "MI_ConstReferenceA",
    "MI_ConstInstanceA",
    "MI_Value",
    "MI_BooleanField",
    "MI_Sint8Field",
    "MI_Uint8Field",
    "MI_Sint16Field",
    "MI_Uint16Field",
    "MI_Sint32Field",
    "MI_Uint32Field",
    "MI_Sint64Field",
    "MI_Uint64Field",
    "MI_Real32Field",
    "MI_Real64Field",
    "MI_Char16Field",
    "MI_DatetimeField",
    "MI_StringField",
    "MI_ReferenceField",
    "MI_InstanceField",
    "MI_BooleanAField",
    "MI_Uint8AField",
    "MI_Sint8AField",
    "MI_Uint16AField",
    "MI_Sint16AField",
    "MI_Uint32AField",
    "MI_Sint32AField",
    "MI_Uint64AField",
    "MI_Sint64AField",
    "MI_Real32AField",
    "MI_Real64AField",
    "MI_Char16AField",
    "MI_DatetimeAField",
    "MI_StringAField",
    "MI_ReferenceAField",
    "MI_InstanceAField",
    "MI_ArrayField",
    "MI_ConstBooleanField",
    "MI_ConstSint8Field",
    "MI_ConstUint8Field",
    "MI_ConstSint16Field",
    "MI_ConstUint16Field",
    "MI_ConstSint32Field",
    "MI_ConstUint32Field",
    "MI_ConstSint64Field",
    "MI_ConstUint64Field",
    "MI_ConstReal32Field",
    "MI_ConstReal64Field",
    "MI_ConstChar16Field",
    "MI_ConstDatetimeField",
    "MI_ConstStringField",
    "MI_ConstReferenceField",
    "MI_ConstInstanceField",
    "MI_ConstBooleanAField",
    "MI_ConstUint8AField",
    "MI_ConstSint8AField",
    "MI_ConstUint16AField",
    "MI_ConstSint16AField",
    "MI_ConstUint32AField",
    "MI_ConstSint32AField",
    "MI_ConstUint64AField",
    "MI_ConstSint64AField",
    "MI_ConstReal32AField",
    "MI_ConstReal64AField",
    "MI_ConstChar16AField",
    "MI_ConstDatetimeAField",
    "MI_ConstStringAField",
    "MI_ConstReferenceAField",
    "MI_ConstInstanceAField",
    "MI_ServerFT",
    "MI_Server",
    "MI_FilterFT",
    "MI_Filter",
    "MI_PropertySetFT",
    "MI_PropertySet",
    "MI_ObjectDecl",
    "MI_ClassDecl",
    "MI_FeatureDecl",
    "MI_ParameterDecl",
    "MI_PropertyDecl",
    "MI_MethodDecl_Invoke",
    "MI_MethodDecl",
    "MI_QualifierDecl",
    "MI_Qualifier",
    "MI_SchemaDecl",
    "MI_Module_Self",
    "MI_ProviderFT_Load",
    "MI_ProviderFT_Unload",
    "MI_ProviderFT_GetInstance",
    "MI_ProviderFT_EnumerateInstances",
    "MI_ProviderFT_CreateInstance",
    "MI_ProviderFT_ModifyInstance",
    "MI_ProviderFT_DeleteInstance",
    "MI_ProviderFT_AssociatorInstances",
    "MI_ProviderFT_ReferenceInstances",
    "MI_ProviderFT_EnableIndications",
    "MI_ProviderFT_DisableIndications",
    "MI_ProviderFT_Subscribe",
    "MI_ProviderFT_Unsubscribe",
    "MI_ProviderFT_Invoke",
    "MI_ProviderFT",
    "MI_Module_Load",
    "MI_Module_Unload",
    "MI_Module",
    "MI_InstanceFT",
    "MI_InstanceExFT",
    "MI_Instance",
    "MI_LocaleType",
    "MI_LOCALE_TYPE_REQUESTED_UI",
    "MI_LOCALE_TYPE_REQUESTED_DATA",
    "MI_LOCALE_TYPE_CLOSEST_UI",
    "MI_LOCALE_TYPE_CLOSEST_DATA",
    "MI_CancellationReason",
    "MI_REASON_NONE",
    "MI_REASON_TIMEOUT",
    "MI_REASON_SHUTDOWN",
    "MI_REASON_SERVICESTOP",
    "MI_CancelCallback",
    "MI_ContextFT",
    "MI_Context",
    "MI_MainFunction",
    "MI_QualifierSetFT",
    "MI_QualifierSet",
    "MI_ParameterSetFT",
    "MI_ParameterSet",
    "MI_ClassFT",
    "MI_Class",
    "MI_OperationCallback_ResponseType",
    "MI_OperationCallback_ResponseType_No",
    "MI_OperationCallback_ResponseType_Yes",
    "MI_OperationCallback_ResponseType_NoToAll",
    "MI_OperationCallback_ResponseType_YesToAll",
    "MI_OperationCallback_PromptUser",
    "MI_OperationCallback_WriteError",
    "MI_OperationCallback_WriteMessage",
    "MI_OperationCallback_WriteProgress",
    "MI_OperationCallback_Instance",
    "MI_OperationCallback_StreamedParameter",
    "MI_OperationCallback_Indication",
    "MI_OperationCallback_Class",
    "MI_OperationCallbacks",
    "MI_SessionCallbacks",
    "MI_UsernamePasswordCreds",
    "MI_UserCredentials",
    "MI_SubscriptionDeliveryType",
    "MI_SubscriptionDeliveryType_Pull",
    "MI_SubscriptionDeliveryType_Push",
    "MI_SubscriptionDeliveryOptionsFT",
    "MI_SubscriptionDeliveryOptions",
    "MI_Serializer",
    "MI_Deserializer",
    "MI_SerializerFT",
    "MI_Deserializer_ClassObjectNeeded",
    "MI_DeserializerFT",
    "MI_ApplicationFT",
    "MI_HostedProviderFT",
    "MI_SessionFT",
    "MI_OperationFT",
    "MI_DestinationOptionsFT",
    "MI_OperationOptionsFT",
    "MI_Application",
    "MI_Session",
    "MI_Operation",
    "MI_HostedProvider",
    "MI_DestinationOptions",
    "MI_OperationOptions",
    "MI_UtilitiesFT",
    "MI_ClientFT_V1",
    "MI_DestinationOptions_ImpersonationType",
    "MI_DestinationOptions_ImpersonationType_Default",
    "MI_DestinationOptions_ImpersonationType_None",
    "MI_DestinationOptions_ImpersonationType_Identify",
    "MI_DestinationOptions_ImpersonationType_Impersonate",
    "MI_DestinationOptions_ImpersonationType_Delegate",
    "WbemDefPath",
    "WbemQuery",
    "WBEM_PATH_STATUS_FLAG",
    "WBEMPATH_INFO_ANON_LOCAL_MACHINE",
    "WBEMPATH_INFO_HAS_MACHINE_NAME",
    "WBEMPATH_INFO_IS_CLASS_REF",
    "WBEMPATH_INFO_IS_INST_REF",
    "WBEMPATH_INFO_HAS_SUBSCOPES",
    "WBEMPATH_INFO_IS_COMPOUND",
    "WBEMPATH_INFO_HAS_V2_REF_PATHS",
    "WBEMPATH_INFO_HAS_IMPLIED_KEY",
    "WBEMPATH_INFO_CONTAINS_SINGLETON",
    "WBEMPATH_INFO_V1_COMPLIANT",
    "WBEMPATH_INFO_V2_COMPLIANT",
    "WBEMPATH_INFO_CIM_COMPLIANT",
    "WBEMPATH_INFO_IS_SINGLETON",
    "WBEMPATH_INFO_IS_PARENT",
    "WBEMPATH_INFO_SERVER_NAMESPACE_ONLY",
    "WBEMPATH_INFO_NATIVE_PATH",
    "WBEMPATH_INFO_WMI_PATH",
    "WBEMPATH_INFO_PATH_HAD_SERVER",
    "WBEM_PATH_CREATE_FLAG",
    "WBEMPATH_CREATE_ACCEPT_RELATIVE",
    "WBEMPATH_CREATE_ACCEPT_ABSOLUTE",
    "WBEMPATH_CREATE_ACCEPT_ALL",
    "WBEMPATH_TREAT_SINGLE_IDENT_AS_NS",
    "WBEM_GET_TEXT_FLAGS",
    "WBEMPATH_COMPRESSED",
    "WBEMPATH_GET_RELATIVE_ONLY",
    "WBEMPATH_GET_SERVER_TOO",
    "WBEMPATH_GET_SERVER_AND_NAMESPACE_ONLY",
    "WBEMPATH_GET_NAMESPACE_ONLY",
    "WBEMPATH_GET_ORIGINAL",
    "WBEM_GET_KEY_FLAGS",
    "WBEMPATH_TEXT",
    "WBEMPATH_QUOTEDTEXT",
    "IWbemPathKeyList",
    "IWbemPath",
    "IWbemQuery",
    "WMIQ_ANALYSIS_TYPE",
    "WMIQ_ANALYSIS_RPN_SEQUENCE",
    "WMIQ_ANALYSIS_ASSOC_QUERY",
    "WMIQ_ANALYSIS_PROP_ANALYSIS_MATRIX",
    "WMIQ_ANALYSIS_QUERY_TEXT",
    "WMIQ_ANALYSIS_RESERVED",
    "WMIQ_RPN_TOKEN_FLAGS",
    "WMIQ_RPN_TOKEN_EXPRESSION",
    "WMIQ_RPN_TOKEN_AND",
    "WMIQ_RPN_TOKEN_OR",
    "WMIQ_RPN_TOKEN_NOT",
    "WMIQ_RPN_OP_UNDEFINED",
    "WMIQ_RPN_OP_EQ",
    "WMIQ_RPN_OP_NE",
    "WMIQ_RPN_OP_GE",
    "WMIQ_RPN_OP_LE",
    "WMIQ_RPN_OP_LT",
    "WMIQ_RPN_OP_GT",
    "WMIQ_RPN_OP_LIKE",
    "WMIQ_RPN_OP_ISA",
    "WMIQ_RPN_OP_ISNOTA",
    "WMIQ_RPN_OP_ISNULL",
    "WMIQ_RPN_OP_ISNOTNULL",
    "WMIQ_RPN_LEFT_PROPERTY_NAME",
    "WMIQ_RPN_RIGHT_PROPERTY_NAME",
    "WMIQ_RPN_CONST2",
    "WMIQ_RPN_CONST",
    "WMIQ_RPN_RELOP",
    "WMIQ_RPN_LEFT_FUNCTION",
    "WMIQ_RPN_RIGHT_FUNCTION",
    "WMIQ_RPN_GET_TOKEN_TYPE",
    "WMIQ_RPN_GET_EXPR_SHAPE",
    "WMIQ_RPN_GET_LEFT_FUNCTION",
    "WMIQ_RPN_GET_RIGHT_FUNCTION",
    "WMIQ_RPN_GET_RELOP",
    "WMIQ_RPN_NEXT_TOKEN",
    "WMIQ_RPN_FROM_UNARY",
    "WMIQ_RPN_FROM_PATH",
    "WMIQ_RPN_FROM_CLASS_LIST",
    "WMIQ_RPN_FROM_MULTIPLE",
    "WMIQ_ASSOCQ_FLAGS",
    "WMIQ_ASSOCQ_ASSOCIATORS",
    "WMIQ_ASSOCQ_REFERENCES",
    "WMIQ_ASSOCQ_RESULTCLASS",
    "WMIQ_ASSOCQ_ASSOCCLASS",
    "WMIQ_ASSOCQ_ROLE",
    "WMIQ_ASSOCQ_RESULTROLE",
    "WMIQ_ASSOCQ_REQUIREDQUALIFIER",
    "WMIQ_ASSOCQ_REQUIREDASSOCQUALIFIER",
    "WMIQ_ASSOCQ_CLASSDEFSONLY",
    "WMIQ_ASSOCQ_KEYSONLY",
    "WMIQ_ASSOCQ_SCHEMAONLY",
    "WMIQ_ASSOCQ_CLASSREFSONLY",
    "SWbemQueryQualifiedName",
    "SWbemRpnConst",
    "SWbemRpnQueryToken",
    "SWbemRpnTokenList",
    "WMIQ_LANGUAGE_FEATURES",
    "WMIQ_LF1_BASIC_SELECT",
    "WMIQ_LF2_CLASS_NAME_IN_QUERY",
    "WMIQ_LF3_STRING_CASE_FUNCTIONS",
    "WMIQ_LF4_PROP_TO_PROP_TESTS",
    "WMIQ_LF5_COUNT_STAR",
    "WMIQ_LF6_ORDER_BY",
    "WMIQ_LF7_DISTINCT",
    "WMIQ_LF8_ISA",
    "WMIQ_LF9_THIS",
    "WMIQ_LF10_COMPEX_SUBEXPRESSIONS",
    "WMIQ_LF11_ALIASING",
    "WMIQ_LF12_GROUP_BY_HAVING",
    "WMIQ_LF13_WMI_WITHIN",
    "WMIQ_LF14_SQL_WRITE_OPERATIONS",
    "WMIQ_LF15_GO",
    "WMIQ_LF16_SINGLE_LEVEL_TRANSACTIONS",
    "WMIQ_LF17_QUALIFIED_NAMES",
    "WMIQ_LF18_ASSOCIATONS",
    "WMIQ_LF19_SYSTEM_PROPERTIES",
    "WMIQ_LF20_EXTENDED_SYSTEM_PROPERTIES",
    "WMIQ_LF21_SQL89_JOINS",
    "WMIQ_LF22_SQL92_JOINS",
    "WMIQ_LF23_SUBSELECTS",
    "WMIQ_LF24_UMI_EXTENSIONS",
    "WMIQ_LF25_DATEPART",
    "WMIQ_LF26_LIKE",
    "WMIQ_LF27_CIM_TEMPORAL_CONSTRUCTS",
    "WMIQ_LF28_STANDARD_AGGREGATES",
    "WMIQ_LF29_MULTI_LEVEL_ORDER_BY",
    "WMIQ_LF30_WMI_PRAGMAS",
    "WMIQ_LF31_QUALIFIER_TESTS",
    "WMIQ_LF32_SP_EXECUTE",
    "WMIQ_LF33_ARRAY_ACCESS",
    "WMIQ_LF34_UNION",
    "WMIQ_LF35_COMPLEX_SELECT_TARGET",
    "WMIQ_LF36_REFERENCE_TESTS",
    "WMIQ_LF37_SELECT_INTO",
    "WMIQ_LF38_BASIC_DATETIME_TESTS",
    "WMIQ_LF39_COUNT_COLUMN",
    "WMIQ_LF40_BETWEEN",
    "WMIQ_LF_LAST",
    "WMIQ_RPNQ_FEATURE",
    "WMIQ_RPNF_WHERE_CLAUSE_PRESENT",
    "WMIQ_RPNF_QUERY_IS_CONJUNCTIVE",
    "WMIQ_RPNF_QUERY_IS_DISJUNCTIVE",
    "WMIQ_RPNF_PROJECTION",
    "WMIQ_RPNF_FEATURE_SELECT_STAR",
    "WMIQ_RPNF_EQUALITY_TESTS_ONLY",
    "WMIQ_RPNF_COUNT_STAR",
    "WMIQ_RPNF_QUALIFIED_NAMES_USED",
    "WMIQ_RPNF_SYSPROP_CLASS_USED",
    "WMIQ_RPNF_PROP_TO_PROP_TESTS",
    "WMIQ_RPNF_ORDER_BY",
    "WMIQ_RPNF_ISA_USED",
    "WMIQ_RPNF_GROUP_BY_HAVING",
    "WMIQ_RPNF_ARRAY_ACCESS_USED",
    "SWbemRpnEncodedQuery",
    "SWbemAnalysisMatrix",
    "SWbemAnalysisMatrixList",
    "SWbemAssocQueryInf",
    "WbemLocator",
    "WbemContext",
    "UnsecuredApartment",
    "WbemClassObject",
    "MofCompiler",
    "WbemStatusCodeText",
    "WbemBackupRestore",
    "WbemRefresher",
    "WbemObjectTextSrc",
    "WBEM_GENUS_TYPE",
    "WBEM_GENUS_CLASS",
    "WBEM_GENUS_INSTANCE",
    "WBEM_CHANGE_FLAG_TYPE",
    "WBEM_FLAG_CREATE_OR_UPDATE",
    "WBEM_FLAG_UPDATE_ONLY",
    "WBEM_FLAG_CREATE_ONLY",
    "WBEM_FLAG_UPDATE_COMPATIBLE",
    "WBEM_FLAG_UPDATE_SAFE_MODE",
    "WBEM_FLAG_UPDATE_FORCE_MODE",
    "WBEM_MASK_UPDATE_MODE",
    "WBEM_FLAG_ADVISORY",
    "WBEM_GENERIC_FLAG_TYPE",
    "WBEM_FLAG_RETURN_IMMEDIATELY",
    "WBEM_FLAG_RETURN_WBEM_COMPLETE",
    "WBEM_FLAG_BIDIRECTIONAL",
    "WBEM_FLAG_FORWARD_ONLY",
    "WBEM_FLAG_NO_ERROR_OBJECT",
    "WBEM_FLAG_RETURN_ERROR_OBJECT",
    "WBEM_FLAG_SEND_STATUS",
    "WBEM_FLAG_DONT_SEND_STATUS",
    "WBEM_FLAG_ENSURE_LOCATABLE",
    "WBEM_FLAG_DIRECT_READ",
    "WBEM_FLAG_SEND_ONLY_SELECTED",
    "WBEM_RETURN_WHEN_COMPLETE",
    "WBEM_RETURN_IMMEDIATELY",
    "WBEM_MASK_RESERVED_FLAGS",
    "WBEM_FLAG_USE_AMENDED_QUALIFIERS",
    "WBEM_FLAG_STRONG_VALIDATION",
    "WBEM_STATUS_TYPE",
    "WBEM_STATUS_COMPLETE",
    "WBEM_STATUS_REQUIREMENTS",
    "WBEM_STATUS_PROGRESS",
    "WBEM_STATUS_LOGGING_INFORMATION",
    "WBEM_STATUS_LOGGING_INFORMATION_PROVIDER",
    "WBEM_STATUS_LOGGING_INFORMATION_HOST",
    "WBEM_STATUS_LOGGING_INFORMATION_REPOSITORY",
    "WBEM_STATUS_LOGGING_INFORMATION_ESS",
    "WBEM_TIMEOUT_TYPE",
    "WBEM_NO_WAIT",
    "WBEM_INFINITE",
    "WBEM_CONDITION_FLAG_TYPE",
    "WBEM_FLAG_ALWAYS",
    "WBEM_FLAG_ONLY_IF_TRUE",
    "WBEM_FLAG_ONLY_IF_FALSE",
    "WBEM_FLAG_ONLY_IF_IDENTICAL",
    "WBEM_MASK_PRIMARY_CONDITION",
    "WBEM_FLAG_KEYS_ONLY",
    "WBEM_FLAG_REFS_ONLY",
    "WBEM_FLAG_LOCAL_ONLY",
    "WBEM_FLAG_PROPAGATED_ONLY",
    "WBEM_FLAG_SYSTEM_ONLY",
    "WBEM_FLAG_NONSYSTEM_ONLY",
    "WBEM_MASK_CONDITION_ORIGIN",
    "WBEM_FLAG_CLASS_OVERRIDES_ONLY",
    "WBEM_FLAG_CLASS_LOCAL_AND_OVERRIDES",
    "WBEM_MASK_CLASS_CONDITION",
    "WBEM_FLAVOR_TYPE",
    "WBEM_FLAVOR_DONT_PROPAGATE",
    "WBEM_FLAVOR_FLAG_PROPAGATE_TO_INSTANCE",
    "WBEM_FLAVOR_FLAG_PROPAGATE_TO_DERIVED_CLASS",
    "WBEM_FLAVOR_MASK_PROPAGATION",
    "WBEM_FLAVOR_OVERRIDABLE",
    "WBEM_FLAVOR_NOT_OVERRIDABLE",
    "WBEM_FLAVOR_MASK_PERMISSIONS",
    "WBEM_FLAVOR_ORIGIN_LOCAL",
    "WBEM_FLAVOR_ORIGIN_PROPAGATED",
    "WBEM_FLAVOR_ORIGIN_SYSTEM",
    "WBEM_FLAVOR_MASK_ORIGIN",
    "WBEM_FLAVOR_NOT_AMENDED",
    "WBEM_FLAVOR_AMENDED",
    "WBEM_FLAVOR_MASK_AMENDED",
    "WBEM_QUERY_FLAG_TYPE",
    "WBEM_FLAG_DEEP",
    "WBEM_FLAG_SHALLOW",
    "WBEM_FLAG_PROTOTYPE",
    "WBEM_SECURITY_FLAGS",
    "WBEM_ENABLE",
    "WBEM_METHOD_EXECUTE",
    "WBEM_FULL_WRITE_REP",
    "WBEM_PARTIAL_WRITE_REP",
    "WBEM_WRITE_PROVIDER",
    "WBEM_REMOTE_ACCESS",
    "WBEM_RIGHT_SUBSCRIBE",
    "WBEM_RIGHT_PUBLISH",
    "WBEM_LIMITATION_FLAG_TYPE",
    "WBEM_FLAG_EXCLUDE_OBJECT_QUALIFIERS",
    "WBEM_FLAG_EXCLUDE_PROPERTY_QUALIFIERS",
    "WBEM_TEXT_FLAG_TYPE",
    "WBEM_FLAG_NO_FLAVORS",
    "WBEM_COMPARISON_FLAG",
    "WBEM_COMPARISON_INCLUDE_ALL",
    "WBEM_FLAG_IGNORE_QUALIFIERS",
    "WBEM_FLAG_IGNORE_OBJECT_SOURCE",
    "WBEM_FLAG_IGNORE_DEFAULT_VALUES",
    "WBEM_FLAG_IGNORE_CLASS",
    "WBEM_FLAG_IGNORE_CASE",
    "WBEM_FLAG_IGNORE_FLAVOR",
    "WBEM_LOCKING",
    "WBEM_FLAG_ALLOW_READ",
    "CIMTYPE_ENUMERATION",
    "CIM_ILLEGAL",
    "CIM_EMPTY",
    "CIM_SINT8",
    "CIM_UINT8",
    "CIM_SINT16",
    "CIM_UINT16",
    "CIM_SINT32",
    "CIM_UINT32",
    "CIM_SINT64",
    "CIM_UINT64",
    "CIM_REAL32",
    "CIM_REAL64",
    "CIM_BOOLEAN",
    "CIM_STRING",
    "CIM_DATETIME",
    "CIM_REFERENCE",
    "CIM_CHAR16",
    "CIM_OBJECT",
    "CIM_FLAG_ARRAY",
    "WBEM_BACKUP_RESTORE_FLAGS",
    "WBEM_FLAG_BACKUP_RESTORE_DEFAULT",
    "WBEM_FLAG_BACKUP_RESTORE_FORCE_SHUTDOWN",
    "WBEM_REFRESHER_FLAGS",
    "WBEM_FLAG_REFRESH_AUTO_RECONNECT",
    "WBEM_FLAG_REFRESH_NO_AUTO_RECONNECT",
    "WBEM_SHUTDOWN_FLAGS",
    "WBEM_SHUTDOWN_UNLOAD_COMPONENT",
    "WBEM_SHUTDOWN_WMI",
    "WBEM_SHUTDOWN_OS",
    "WBEMSTATUS_FORMAT",
    "WBEMSTATUS_FORMAT_NEWLINE",
    "WBEMSTATUS_FORMAT_NO_NEWLINE",
    "WBEM_LIMITS",
    "WBEM_MAX_IDENTIFIER",
    "WBEM_MAX_QUERY",
    "WBEM_MAX_PATH",
    "WBEM_MAX_OBJECT_NESTING",
    "WBEM_MAX_USER_PROPERTIES",
    "WBEMSTATUS",
    "WBEM_NO_ERROR",
    "WBEM_S_NO_ERROR",
    "WBEM_S_SAME",
    "WBEM_S_FALSE",
    "WBEM_S_ALREADY_EXISTS",
    "WBEM_S_RESET_TO_DEFAULT",
    "WBEM_S_DIFFERENT",
    "WBEM_S_TIMEDOUT",
    "WBEM_S_NO_MORE_DATA",
    "WBEM_S_OPERATION_CANCELLED",
    "WBEM_S_PENDING",
    "WBEM_S_DUPLICATE_OBJECTS",
    "WBEM_S_ACCESS_DENIED",
    "WBEM_S_PARTIAL_RESULTS",
    "WBEM_S_SOURCE_NOT_AVAILABLE",
    "WBEM_E_FAILED",
    "WBEM_E_NOT_FOUND",
    "WBEM_E_ACCESS_DENIED",
    "WBEM_E_PROVIDER_FAILURE",
    "WBEM_E_TYPE_MISMATCH",
    "WBEM_E_OUT_OF_MEMORY",
    "WBEM_E_INVALID_CONTEXT",
    "WBEM_E_INVALID_PARAMETER",
    "WBEM_E_NOT_AVAILABLE",
    "WBEM_E_CRITICAL_ERROR",
    "WBEM_E_INVALID_STREAM",
    "WBEM_E_NOT_SUPPORTED",
    "WBEM_E_INVALID_SUPERCLASS",
    "WBEM_E_INVALID_NAMESPACE",
    "WBEM_E_INVALID_OBJECT",
    "WBEM_E_INVALID_CLASS",
    "WBEM_E_PROVIDER_NOT_FOUND",
    "WBEM_E_INVALID_PROVIDER_REGISTRATION",
    "WBEM_E_PROVIDER_LOAD_FAILURE",
    "WBEM_E_INITIALIZATION_FAILURE",
    "WBEM_E_TRANSPORT_FAILURE",
    "WBEM_E_INVALID_OPERATION",
    "WBEM_E_INVALID_QUERY",
    "WBEM_E_INVALID_QUERY_TYPE",
    "WBEM_E_ALREADY_EXISTS",
    "WBEM_E_OVERRIDE_NOT_ALLOWED",
    "WBEM_E_PROPAGATED_QUALIFIER",
    "WBEM_E_PROPAGATED_PROPERTY",
    "WBEM_E_UNEXPECTED",
    "WBEM_E_ILLEGAL_OPERATION",
    "WBEM_E_CANNOT_BE_KEY",
    "WBEM_E_INCOMPLETE_CLASS",
    "WBEM_E_INVALID_SYNTAX",
    "WBEM_E_NONDECORATED_OBJECT",
    "WBEM_E_READ_ONLY",
    "WBEM_E_PROVIDER_NOT_CAPABLE",
    "WBEM_E_CLASS_HAS_CHILDREN",
    "WBEM_E_CLASS_HAS_INSTANCES",
    "WBEM_E_QUERY_NOT_IMPLEMENTED",
    "WBEM_E_ILLEGAL_NULL",
    "WBEM_E_INVALID_QUALIFIER_TYPE",
    "WBEM_E_INVALID_PROPERTY_TYPE",
    "WBEM_E_VALUE_OUT_OF_RANGE",
    "WBEM_E_CANNOT_BE_SINGLETON",
    "WBEM_E_INVALID_CIM_TYPE",
    "WBEM_E_INVALID_METHOD",
    "WBEM_E_INVALID_METHOD_PARAMETERS",
    "WBEM_E_SYSTEM_PROPERTY",
    "WBEM_E_INVALID_PROPERTY",
    "WBEM_E_CALL_CANCELLED",
    "WBEM_E_SHUTTING_DOWN",
    "WBEM_E_PROPAGATED_METHOD",
    "WBEM_E_UNSUPPORTED_PARAMETER",
    "WBEM_E_MISSING_PARAMETER_ID",
    "WBEM_E_INVALID_PARAMETER_ID",
    "WBEM_E_NONCONSECUTIVE_PARAMETER_IDS",
    "WBEM_E_PARAMETER_ID_ON_RETVAL",
    "WBEM_E_INVALID_OBJECT_PATH",
    "WBEM_E_OUT_OF_DISK_SPACE",
    "WBEM_E_BUFFER_TOO_SMALL",
    "WBEM_E_UNSUPPORTED_PUT_EXTENSION",
    "WBEM_E_UNKNOWN_OBJECT_TYPE",
    "WBEM_E_UNKNOWN_PACKET_TYPE",
    "WBEM_E_MARSHAL_VERSION_MISMATCH",
    "WBEM_E_MARSHAL_INVALID_SIGNATURE",
    "WBEM_E_INVALID_QUALIFIER",
    "WBEM_E_INVALID_DUPLICATE_PARAMETER",
    "WBEM_E_TOO_MUCH_DATA",
    "WBEM_E_SERVER_TOO_BUSY",
    "WBEM_E_INVALID_FLAVOR",
    "WBEM_E_CIRCULAR_REFERENCE",
    "WBEM_E_UNSUPPORTED_CLASS_UPDATE",
    "WBEM_E_CANNOT_CHANGE_KEY_INHERITANCE",
    "WBEM_E_CANNOT_CHANGE_INDEX_INHERITANCE",
    "WBEM_E_TOO_MANY_PROPERTIES",
    "WBEM_E_UPDATE_TYPE_MISMATCH",
    "WBEM_E_UPDATE_OVERRIDE_NOT_ALLOWED",
    "WBEM_E_UPDATE_PROPAGATED_METHOD",
    "WBEM_E_METHOD_NOT_IMPLEMENTED",
    "WBEM_E_METHOD_DISABLED",
    "WBEM_E_REFRESHER_BUSY",
    "WBEM_E_UNPARSABLE_QUERY",
    "WBEM_E_NOT_EVENT_CLASS",
    "WBEM_E_MISSING_GROUP_WITHIN",
    "WBEM_E_MISSING_AGGREGATION_LIST",
    "WBEM_E_PROPERTY_NOT_AN_OBJECT",
    "WBEM_E_AGGREGATING_BY_OBJECT",
    "WBEM_E_UNINTERPRETABLE_PROVIDER_QUERY",
    "WBEM_E_BACKUP_RESTORE_WINMGMT_RUNNING",
    "WBEM_E_QUEUE_OVERFLOW",
    "WBEM_E_PRIVILEGE_NOT_HELD",
    "WBEM_E_INVALID_OPERATOR",
    "WBEM_E_LOCAL_CREDENTIALS",
    "WBEM_E_CANNOT_BE_ABSTRACT",
    "WBEM_E_AMENDED_OBJECT",
    "WBEM_E_CLIENT_TOO_SLOW",
    "WBEM_E_NULL_SECURITY_DESCRIPTOR",
    "WBEM_E_TIMED_OUT",
    "WBEM_E_INVALID_ASSOCIATION",
    "WBEM_E_AMBIGUOUS_OPERATION",
    "WBEM_E_QUOTA_VIOLATION",
    "WBEM_E_RESERVED_001",
    "WBEM_E_RESERVED_002",
    "WBEM_E_UNSUPPORTED_LOCALE",
    "WBEM_E_HANDLE_OUT_OF_DATE",
    "WBEM_E_CONNECTION_FAILED",
    "WBEM_E_INVALID_HANDLE_REQUEST",
    "WBEM_E_PROPERTY_NAME_TOO_WIDE",
    "WBEM_E_CLASS_NAME_TOO_WIDE",
    "WBEM_E_METHOD_NAME_TOO_WIDE",
    "WBEM_E_QUALIFIER_NAME_TOO_WIDE",
    "WBEM_E_RERUN_COMMAND",
    "WBEM_E_DATABASE_VER_MISMATCH",
    "WBEM_E_VETO_DELETE",
    "WBEM_E_VETO_PUT",
    "WBEM_E_INVALID_LOCALE",
    "WBEM_E_PROVIDER_SUSPENDED",
    "WBEM_E_SYNCHRONIZATION_REQUIRED",
    "WBEM_E_NO_SCHEMA",
    "WBEM_E_PROVIDER_ALREADY_REGISTERED",
    "WBEM_E_PROVIDER_NOT_REGISTERED",
    "WBEM_E_FATAL_TRANSPORT_ERROR",
    "WBEM_E_ENCRYPTED_CONNECTION_REQUIRED",
    "WBEM_E_PROVIDER_TIMED_OUT",
    "WBEM_E_NO_KEY",
    "WBEM_E_PROVIDER_DISABLED",
    "WBEMESS_E_REGISTRATION_TOO_BROAD",
    "WBEMESS_E_REGISTRATION_TOO_PRECISE",
    "WBEMESS_E_AUTHZ_NOT_PRIVILEGED",
    "WBEMMOF_E_EXPECTED_QUALIFIER_NAME",
    "WBEMMOF_E_EXPECTED_SEMI",
    "WBEMMOF_E_EXPECTED_OPEN_BRACE",
    "WBEMMOF_E_EXPECTED_CLOSE_BRACE",
    "WBEMMOF_E_EXPECTED_CLOSE_BRACKET",
    "WBEMMOF_E_EXPECTED_CLOSE_PAREN",
    "WBEMMOF_E_ILLEGAL_CONSTANT_VALUE",
    "WBEMMOF_E_EXPECTED_TYPE_IDENTIFIER",
    "WBEMMOF_E_EXPECTED_OPEN_PAREN",
    "WBEMMOF_E_UNRECOGNIZED_TOKEN",
    "WBEMMOF_E_UNRECOGNIZED_TYPE",
    "WBEMMOF_E_EXPECTED_PROPERTY_NAME",
    "WBEMMOF_E_TYPEDEF_NOT_SUPPORTED",
    "WBEMMOF_E_UNEXPECTED_ALIAS",
    "WBEMMOF_E_UNEXPECTED_ARRAY_INIT",
    "WBEMMOF_E_INVALID_AMENDMENT_SYNTAX",
    "WBEMMOF_E_INVALID_DUPLICATE_AMENDMENT",
    "WBEMMOF_E_INVALID_PRAGMA",
    "WBEMMOF_E_INVALID_NAMESPACE_SYNTAX",
    "WBEMMOF_E_EXPECTED_CLASS_NAME",
    "WBEMMOF_E_TYPE_MISMATCH",
    "WBEMMOF_E_EXPECTED_ALIAS_NAME",
    "WBEMMOF_E_INVALID_CLASS_DECLARATION",
    "WBEMMOF_E_INVALID_INSTANCE_DECLARATION",
    "WBEMMOF_E_EXPECTED_DOLLAR",
    "WBEMMOF_E_CIMTYPE_QUALIFIER",
    "WBEMMOF_E_DUPLICATE_PROPERTY",
    "WBEMMOF_E_INVALID_NAMESPACE_SPECIFICATION",
    "WBEMMOF_E_OUT_OF_RANGE",
    "WBEMMOF_E_INVALID_FILE",
    "WBEMMOF_E_ALIASES_IN_EMBEDDED",
    "WBEMMOF_E_NULL_ARRAY_ELEM",
    "WBEMMOF_E_DUPLICATE_QUALIFIER",
    "WBEMMOF_E_EXPECTED_FLAVOR_TYPE",
    "WBEMMOF_E_INCOMPATIBLE_FLAVOR_TYPES",
    "WBEMMOF_E_MULTIPLE_ALIASES",
    "WBEMMOF_E_INCOMPATIBLE_FLAVOR_TYPES2",
    "WBEMMOF_E_NO_ARRAYS_RETURNED",
    "WBEMMOF_E_MUST_BE_IN_OR_OUT",
    "WBEMMOF_E_INVALID_FLAGS_SYNTAX",
    "WBEMMOF_E_EXPECTED_BRACE_OR_BAD_TYPE",
    "WBEMMOF_E_UNSUPPORTED_CIMV22_QUAL_VALUE",
    "WBEMMOF_E_UNSUPPORTED_CIMV22_DATA_TYPE",
    "WBEMMOF_E_INVALID_DELETEINSTANCE_SYNTAX",
    "WBEMMOF_E_INVALID_QUALIFIER_SYNTAX",
    "WBEMMOF_E_QUALIFIER_USED_OUTSIDE_SCOPE",
    "WBEMMOF_E_ERROR_CREATING_TEMP_FILE",
    "WBEMMOF_E_ERROR_INVALID_INCLUDE_FILE",
    "WBEMMOF_E_INVALID_DELETECLASS_SYNTAX",
    "IWbemClassObject",
    "IWbemObjectAccess",
    "IWbemQualifierSet",
    "IWbemServices",
    "IWbemLocator",
    "IWbemObjectSink",
    "IEnumWbemClassObject",
    "IWbemCallResult",
    "IWbemContext",
    "IUnsecuredApartment",
    "IWbemUnsecuredApartment",
    "IWbemStatusCodeText",
    "IWbemBackupRestore",
    "IWbemBackupRestoreEx",
    "IWbemRefresher",
    "IWbemHiPerfEnum",
    "IWbemConfigureRefresher",
    "IWbemObjectSinkEx",
    "IWbemShutdown",
    "WMI_OBJ_TEXT",
    "WMI_OBJ_TEXT_CIM_DTD_2_0",
    "WMI_OBJ_TEXT_WMI_DTD_2_0",
    "WMI_OBJ_TEXT_WMI_EXT1",
    "WMI_OBJ_TEXT_WMI_EXT2",
    "WMI_OBJ_TEXT_WMI_EXT3",
    "WMI_OBJ_TEXT_WMI_EXT4",
    "WMI_OBJ_TEXT_WMI_EXT5",
    "WMI_OBJ_TEXT_WMI_EXT6",
    "WMI_OBJ_TEXT_WMI_EXT7",
    "WMI_OBJ_TEXT_WMI_EXT8",
    "WMI_OBJ_TEXT_WMI_EXT9",
    "WMI_OBJ_TEXT_WMI_EXT10",
    "WMI_OBJ_TEXT_LAST",
    "IWbemObjectTextSrc",
    "WBEM_COMPILE_STATUS_INFO",
    "WBEM_COMPILER_OPTIONS",
    "WBEM_FLAG_CHECK_ONLY",
    "WBEM_FLAG_AUTORECOVER",
    "WBEM_FLAG_WMI_CHECK",
    "WBEM_FLAG_CONSOLE_PRINT",
    "WBEM_FLAG_DONT_ADD_TO_LIST",
    "WBEM_FLAG_SPLIT_FILES",
    "WBEM_FLAG_STORE_FILE",
    "WBEM_CONNECT_OPTIONS",
    "WBEM_FLAG_CONNECT_REPOSITORY_ONLY",
    "WBEM_FLAG_CONNECT_USE_MAX_WAIT",
    "WBEM_FLAG_CONNECT_PROVIDERS",
    "IMofCompiler",
    "WBEM_UNSECAPP_FLAG_TYPE",
    "WBEM_FLAG_UNSECAPP_DEFAULT_CHECK_ACCESS",
    "WBEM_FLAG_UNSECAPP_CHECK_ACCESS",
    "WBEM_FLAG_UNSECAPP_DONT_CHECK_ACCESS",
    "WBEM_INFORMATION_FLAG_TYPE",
    "WBEM_FLAG_SHORT_NAME",
    "WBEM_FLAG_LONG_NAME",
    "WbemAdministrativeLocator",
    "WbemAuthenticatedLocator",
    "WbemUnauthenticatedLocator",
    "WbemDecoupledRegistrar",
    "WbemDecoupledBasicEventProvider",
    "WBEM_PROVIDER_REQUIREMENTS_TYPE",
    "WBEM_REQUIREMENTS_START_POSTFILTER",
    "WBEM_REQUIREMENTS_STOP_POSTFILTER",
    "WBEM_REQUIREMENTS_RECHECK_SUBSCRIPTIONS",
    "IWbemPropertyProvider",
    "IWbemUnboundObjectSink",
    "IWbemEventProvider",
    "IWbemEventProviderQuerySink",
    "IWbemEventProviderSecurity",
    "IWbemEventConsumerProvider",
    "IWbemProviderInitSink",
    "IWbemProviderInit",
    "IWbemHiPerfProvider",
    "IWbemDecoupledRegistrar",
    "IWbemProviderIdentity",
    "WBEM_EXTRA_RETURN_CODES",
    "WBEM_S_INITIALIZED",
    "WBEM_S_LIMITED_SERVICE",
    "WBEM_S_INDIRECTLY_UPDATED",
    "WBEM_S_SUBJECT_TO_SDS",
    "WBEM_E_RETRY_LATER",
    "WBEM_E_RESOURCE_CONTENTION",
    "WBEM_PROVIDER_FLAGS",
    "WBEM_FLAG_OWNER_UPDATE",
    "IWbemDecoupledBasicEventProvider",
    "WBEM_BATCH_TYPE",
    "WBEM_FLAG_BATCH_IF_NEEDED",
    "WBEM_FLAG_MUST_BATCH",
    "WBEM_FLAG_MUST_NOT_BATCH",
    "IWbemEventSink",
    "SWbemLocator",
    "SWbemNamedValueSet",
    "SWbemObjectPath",
    "SWbemLastError",
    "SWbemSink",
    "SWbemDateTime",
    "SWbemRefresher",
    "SWbemServices",
    "SWbemServicesEx",
    "SWbemObject",
    "SWbemObjectEx",
    "SWbemObjectSet",
    "SWbemNamedValue",
    "SWbemQualifier",
    "SWbemQualifierSet",
    "SWbemProperty",
    "SWbemPropertySet",
    "SWbemMethod",
    "SWbemMethodSet",
    "SWbemEventSource",
    "SWbemSecurity",
    "SWbemPrivilege",
    "SWbemPrivilegeSet",
    "SWbemRefreshableItem",
    "WbemChangeFlagEnum",
    "WbemChangeFlagEnum_wbemChangeFlagCreateOrUpdate",
    "WbemChangeFlagEnum_wbemChangeFlagUpdateOnly",
    "WbemChangeFlagEnum_wbemChangeFlagCreateOnly",
    "WbemChangeFlagEnum_wbemChangeFlagUpdateCompatible",
    "WbemChangeFlagEnum_wbemChangeFlagUpdateSafeMode",
    "WbemChangeFlagEnum_wbemChangeFlagUpdateForceMode",
    "WbemChangeFlagEnum_wbemChangeFlagStrongValidation",
    "WbemChangeFlagEnum_wbemChangeFlagAdvisory",
    "WbemFlagEnum",
    "WbemFlagEnum_wbemFlagReturnImmediately",
    "WbemFlagEnum_wbemFlagReturnWhenComplete",
    "WbemFlagEnum_wbemFlagBidirectional",
    "WbemFlagEnum_wbemFlagForwardOnly",
    "WbemFlagEnum_wbemFlagNoErrorObject",
    "WbemFlagEnum_wbemFlagReturnErrorObject",
    "WbemFlagEnum_wbemFlagSendStatus",
    "WbemFlagEnum_wbemFlagDontSendStatus",
    "WbemFlagEnum_wbemFlagEnsureLocatable",
    "WbemFlagEnum_wbemFlagDirectRead",
    "WbemFlagEnum_wbemFlagSendOnlySelected",
    "WbemFlagEnum_wbemFlagUseAmendedQualifiers",
    "WbemFlagEnum_wbemFlagGetDefault",
    "WbemFlagEnum_wbemFlagSpawnInstance",
    "WbemFlagEnum_wbemFlagUseCurrentTime",
    "WbemQueryFlagEnum",
    "WbemQueryFlagEnum_wbemQueryFlagDeep",
    "WbemQueryFlagEnum_wbemQueryFlagShallow",
    "WbemQueryFlagEnum_wbemQueryFlagPrototype",
    "WbemTextFlagEnum",
    "WbemTextFlagEnum_wbemTextFlagNoFlavors",
    "WbemTimeout",
    "WbemTimeout_wbemTimeoutInfinite",
    "WbemComparisonFlagEnum",
    "WbemComparisonFlagEnum_wbemComparisonFlagIncludeAll",
    "WbemComparisonFlagEnum_wbemComparisonFlagIgnoreQualifiers",
    "WbemComparisonFlagEnum_wbemComparisonFlagIgnoreObjectSource",
    "WbemComparisonFlagEnum_wbemComparisonFlagIgnoreDefaultValues",
    "WbemComparisonFlagEnum_wbemComparisonFlagIgnoreClass",
    "WbemComparisonFlagEnum_wbemComparisonFlagIgnoreCase",
    "WbemComparisonFlagEnum_wbemComparisonFlagIgnoreFlavor",
    "WbemCimtypeEnum",
    "WbemCimtypeEnum_wbemCimtypeSint8",
    "WbemCimtypeEnum_wbemCimtypeUint8",
    "WbemCimtypeEnum_wbemCimtypeSint16",
    "WbemCimtypeEnum_wbemCimtypeUint16",
    "WbemCimtypeEnum_wbemCimtypeSint32",
    "WbemCimtypeEnum_wbemCimtypeUint32",
    "WbemCimtypeEnum_wbemCimtypeSint64",
    "WbemCimtypeEnum_wbemCimtypeUint64",
    "WbemCimtypeEnum_wbemCimtypeReal32",
    "WbemCimtypeEnum_wbemCimtypeReal64",
    "WbemCimtypeEnum_wbemCimtypeBoolean",
    "WbemCimtypeEnum_wbemCimtypeString",
    "WbemCimtypeEnum_wbemCimtypeDatetime",
    "WbemCimtypeEnum_wbemCimtypeReference",
    "WbemCimtypeEnum_wbemCimtypeChar16",
    "WbemCimtypeEnum_wbemCimtypeObject",
    "WbemErrorEnum",
    "WbemErrorEnum_wbemNoErr",
    "WbemErrorEnum_wbemErrFailed",
    "WbemErrorEnum_wbemErrNotFound",
    "WbemErrorEnum_wbemErrAccessDenied",
    "WbemErrorEnum_wbemErrProviderFailure",
    "WbemErrorEnum_wbemErrTypeMismatch",
    "WbemErrorEnum_wbemErrOutOfMemory",
    "WbemErrorEnum_wbemErrInvalidContext",
    "WbemErrorEnum_wbemErrInvalidParameter",
    "WbemErrorEnum_wbemErrNotAvailable",
    "WbemErrorEnum_wbemErrCriticalError",
    "WbemErrorEnum_wbemErrInvalidStream",
    "WbemErrorEnum_wbemErrNotSupported",
    "WbemErrorEnum_wbemErrInvalidSuperclass",
    "WbemErrorEnum_wbemErrInvalidNamespace",
    "WbemErrorEnum_wbemErrInvalidObject",
    "WbemErrorEnum_wbemErrInvalidClass",
    "WbemErrorEnum_wbemErrProviderNotFound",
    "WbemErrorEnum_wbemErrInvalidProviderRegistration",
    "WbemErrorEnum_wbemErrProviderLoadFailure",
    "WbemErrorEnum_wbemErrInitializationFailure",
    "WbemErrorEnum_wbemErrTransportFailure",
    "WbemErrorEnum_wbemErrInvalidOperation",
    "WbemErrorEnum_wbemErrInvalidQuery",
    "WbemErrorEnum_wbemErrInvalidQueryType",
    "WbemErrorEnum_wbemErrAlreadyExists",
    "WbemErrorEnum_wbemErrOverrideNotAllowed",
    "WbemErrorEnum_wbemErrPropagatedQualifier",
    "WbemErrorEnum_wbemErrPropagatedProperty",
    "WbemErrorEnum_wbemErrUnexpected",
    "WbemErrorEnum_wbemErrIllegalOperation",
    "WbemErrorEnum_wbemErrCannotBeKey",
    "WbemErrorEnum_wbemErrIncompleteClass",
    "WbemErrorEnum_wbemErrInvalidSyntax",
    "WbemErrorEnum_wbemErrNondecoratedObject",
    "WbemErrorEnum_wbemErrReadOnly",
    "WbemErrorEnum_wbemErrProviderNotCapable",
    "WbemErrorEnum_wbemErrClassHasChildren",
    "WbemErrorEnum_wbemErrClassHasInstances",
    "WbemErrorEnum_wbemErrQueryNotImplemented",
    "WbemErrorEnum_wbemErrIllegalNull",
    "WbemErrorEnum_wbemErrInvalidQualifierType",
    "WbemErrorEnum_wbemErrInvalidPropertyType",
    "WbemErrorEnum_wbemErrValueOutOfRange",
    "WbemErrorEnum_wbemErrCannotBeSingleton",
    "WbemErrorEnum_wbemErrInvalidCimType",
    "WbemErrorEnum_wbemErrInvalidMethod",
    "WbemErrorEnum_wbemErrInvalidMethodParameters",
    "WbemErrorEnum_wbemErrSystemProperty",
    "WbemErrorEnum_wbemErrInvalidProperty",
    "WbemErrorEnum_wbemErrCallCancelled",
    "WbemErrorEnum_wbemErrShuttingDown",
    "WbemErrorEnum_wbemErrPropagatedMethod",
    "WbemErrorEnum_wbemErrUnsupportedParameter",
    "WbemErrorEnum_wbemErrMissingParameter",
    "WbemErrorEnum_wbemErrInvalidParameterId",
    "WbemErrorEnum_wbemErrNonConsecutiveParameterIds",
    "WbemErrorEnum_wbemErrParameterIdOnRetval",
    "WbemErrorEnum_wbemErrInvalidObjectPath",
    "WbemErrorEnum_wbemErrOutOfDiskSpace",
    "WbemErrorEnum_wbemErrBufferTooSmall",
    "WbemErrorEnum_wbemErrUnsupportedPutExtension",
    "WbemErrorEnum_wbemErrUnknownObjectType",
    "WbemErrorEnum_wbemErrUnknownPacketType",
    "WbemErrorEnum_wbemErrMarshalVersionMismatch",
    "WbemErrorEnum_wbemErrMarshalInvalidSignature",
    "WbemErrorEnum_wbemErrInvalidQualifier",
    "WbemErrorEnum_wbemErrInvalidDuplicateParameter",
    "WbemErrorEnum_wbemErrTooMuchData",
    "WbemErrorEnum_wbemErrServerTooBusy",
    "WbemErrorEnum_wbemErrInvalidFlavor",
    "WbemErrorEnum_wbemErrCircularReference",
    "WbemErrorEnum_wbemErrUnsupportedClassUpdate",
    "WbemErrorEnum_wbemErrCannotChangeKeyInheritance",
    "WbemErrorEnum_wbemErrCannotChangeIndexInheritance",
    "WbemErrorEnum_wbemErrTooManyProperties",
    "WbemErrorEnum_wbemErrUpdateTypeMismatch",
    "WbemErrorEnum_wbemErrUpdateOverrideNotAllowed",
    "WbemErrorEnum_wbemErrUpdatePropagatedMethod",
    "WbemErrorEnum_wbemErrMethodNotImplemented",
    "WbemErrorEnum_wbemErrMethodDisabled",
    "WbemErrorEnum_wbemErrRefresherBusy",
    "WbemErrorEnum_wbemErrUnparsableQuery",
    "WbemErrorEnum_wbemErrNotEventClass",
    "WbemErrorEnum_wbemErrMissingGroupWithin",
    "WbemErrorEnum_wbemErrMissingAggregationList",
    "WbemErrorEnum_wbemErrPropertyNotAnObject",
    "WbemErrorEnum_wbemErrAggregatingByObject",
    "WbemErrorEnum_wbemErrUninterpretableProviderQuery",
    "WbemErrorEnum_wbemErrBackupRestoreWinmgmtRunning",
    "WbemErrorEnum_wbemErrQueueOverflow",
    "WbemErrorEnum_wbemErrPrivilegeNotHeld",
    "WbemErrorEnum_wbemErrInvalidOperator",
    "WbemErrorEnum_wbemErrLocalCredentials",
    "WbemErrorEnum_wbemErrCannotBeAbstract",
    "WbemErrorEnum_wbemErrAmendedObject",
    "WbemErrorEnum_wbemErrClientTooSlow",
    "WbemErrorEnum_wbemErrNullSecurityDescriptor",
    "WbemErrorEnum_wbemErrTimeout",
    "WbemErrorEnum_wbemErrInvalidAssociation",
    "WbemErrorEnum_wbemErrAmbiguousOperation",
    "WbemErrorEnum_wbemErrQuotaViolation",
    "WbemErrorEnum_wbemErrTransactionConflict",
    "WbemErrorEnum_wbemErrForcedRollback",
    "WbemErrorEnum_wbemErrUnsupportedLocale",
    "WbemErrorEnum_wbemErrHandleOutOfDate",
    "WbemErrorEnum_wbemErrConnectionFailed",
    "WbemErrorEnum_wbemErrInvalidHandleRequest",
    "WbemErrorEnum_wbemErrPropertyNameTooWide",
    "WbemErrorEnum_wbemErrClassNameTooWide",
    "WbemErrorEnum_wbemErrMethodNameTooWide",
    "WbemErrorEnum_wbemErrQualifierNameTooWide",
    "WbemErrorEnum_wbemErrRerunCommand",
    "WbemErrorEnum_wbemErrDatabaseVerMismatch",
    "WbemErrorEnum_wbemErrVetoPut",
    "WbemErrorEnum_wbemErrVetoDelete",
    "WbemErrorEnum_wbemErrInvalidLocale",
    "WbemErrorEnum_wbemErrProviderSuspended",
    "WbemErrorEnum_wbemErrSynchronizationRequired",
    "WbemErrorEnum_wbemErrNoSchema",
    "WbemErrorEnum_wbemErrProviderAlreadyRegistered",
    "WbemErrorEnum_wbemErrProviderNotRegistered",
    "WbemErrorEnum_wbemErrFatalTransportError",
    "WbemErrorEnum_wbemErrEncryptedConnectionRequired",
    "WbemErrorEnum_wbemErrRegistrationTooBroad",
    "WbemErrorEnum_wbemErrRegistrationTooPrecise",
    "WbemErrorEnum_wbemErrTimedout",
    "WbemErrorEnum_wbemErrResetToDefault",
    "WbemAuthenticationLevelEnum",
    "WbemAuthenticationLevelEnum_wbemAuthenticationLevelDefault",
    "WbemAuthenticationLevelEnum_wbemAuthenticationLevelNone",
    "WbemAuthenticationLevelEnum_wbemAuthenticationLevelConnect",
    "WbemAuthenticationLevelEnum_wbemAuthenticationLevelCall",
    "WbemAuthenticationLevelEnum_wbemAuthenticationLevelPkt",
    "WbemAuthenticationLevelEnum_wbemAuthenticationLevelPktIntegrity",
    "WbemAuthenticationLevelEnum_wbemAuthenticationLevelPktPrivacy",
    "WbemImpersonationLevelEnum",
    "WbemImpersonationLevelEnum_wbemImpersonationLevelAnonymous",
    "WbemImpersonationLevelEnum_wbemImpersonationLevelIdentify",
    "WbemImpersonationLevelEnum_wbemImpersonationLevelImpersonate",
    "WbemImpersonationLevelEnum_wbemImpersonationLevelDelegate",
    "WbemPrivilegeEnum",
    "WbemPrivilegeEnum_wbemPrivilegeCreateToken",
    "WbemPrivilegeEnum_wbemPrivilegePrimaryToken",
    "WbemPrivilegeEnum_wbemPrivilegeLockMemory",
    "WbemPrivilegeEnum_wbemPrivilegeIncreaseQuota",
    "WbemPrivilegeEnum_wbemPrivilegeMachineAccount",
    "WbemPrivilegeEnum_wbemPrivilegeTcb",
    "WbemPrivilegeEnum_wbemPrivilegeSecurity",
    "WbemPrivilegeEnum_wbemPrivilegeTakeOwnership",
    "WbemPrivilegeEnum_wbemPrivilegeLoadDriver",
    "WbemPrivilegeEnum_wbemPrivilegeSystemProfile",
    "WbemPrivilegeEnum_wbemPrivilegeSystemtime",
    "WbemPrivilegeEnum_wbemPrivilegeProfileSingleProcess",
    "WbemPrivilegeEnum_wbemPrivilegeIncreaseBasePriority",
    "WbemPrivilegeEnum_wbemPrivilegeCreatePagefile",
    "WbemPrivilegeEnum_wbemPrivilegeCreatePermanent",
    "WbemPrivilegeEnum_wbemPrivilegeBackup",
    "WbemPrivilegeEnum_wbemPrivilegeRestore",
    "WbemPrivilegeEnum_wbemPrivilegeShutdown",
    "WbemPrivilegeEnum_wbemPrivilegeDebug",
    "WbemPrivilegeEnum_wbemPrivilegeAudit",
    "WbemPrivilegeEnum_wbemPrivilegeSystemEnvironment",
    "WbemPrivilegeEnum_wbemPrivilegeChangeNotify",
    "WbemPrivilegeEnum_wbemPrivilegeRemoteShutdown",
    "WbemPrivilegeEnum_wbemPrivilegeUndock",
    "WbemPrivilegeEnum_wbemPrivilegeSyncAgent",
    "WbemPrivilegeEnum_wbemPrivilegeEnableDelegation",
    "WbemPrivilegeEnum_wbemPrivilegeManageVolume",
    "WbemObjectTextFormatEnum",
    "WbemObjectTextFormatEnum_wbemObjectTextFormatCIMDTD20",
    "WbemObjectTextFormatEnum_wbemObjectTextFormatWMIDTD20",
    "WbemConnectOptionsEnum",
    "WbemConnectOptionsEnum_wbemConnectFlagUseMaxWait",
    "ISWbemServices",
    "ISWbemLocator",
    "ISWbemObject",
    "ISWbemObjectSet",
    "ISWbemNamedValue",
    "ISWbemNamedValueSet",
    "ISWbemQualifier",
    "ISWbemQualifierSet",
    "ISWbemProperty",
    "ISWbemPropertySet",
    "ISWbemMethod",
    "ISWbemMethodSet",
    "ISWbemEventSource",
    "ISWbemObjectPath",
    "ISWbemLastError",
    "ISWbemSinkEvents",
    "ISWbemSink",
    "ISWbemSecurity",
    "ISWbemPrivilege",
    "ISWbemPrivilegeSet",
    "ISWbemServicesEx",
    "ISWbemObjectEx",
    "ISWbemDateTime",
    "ISWbemRefresher",
    "ISWbemRefreshableItem",
    "WMIExtension",
    "IWMIExtension",
    "WbemLevel1Login",
    "WbemLocalAddrRes",
    "WbemUninitializedClassObject",
    "WbemDCOMTransport",
    "tag_WBEM_LOGIN_TYPE",
    "WBEM_FLAG_INPROC_LOGIN",
    "WBEM_FLAG_LOCAL_LOGIN",
    "WBEM_FLAG_REMOTE_LOGIN",
    "WBEM_AUTHENTICATION_METHOD_MASK",
    "WBEM_FLAG_USE_MULTIPLE_CHALLENGES",
    "IWbemTransport",
    "IWbemLevel1Login",
    "IWbemConnectorLogin",
    "IWbemAddressResolution",
    "IWbemClientTransport",
    "IWbemClientConnectionTransport",
    "IWbemConstructClassObject",
    "MI_Application_InitializeV1",
]
