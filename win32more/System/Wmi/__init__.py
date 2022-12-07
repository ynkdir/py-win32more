from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.System.Com
import win32more.System.Wmi
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
MI_FLAG_ANY: UInt32 = 127
MI_FLAG_VERSION: UInt32 = 469762048
MI_FLAG_ADOPT: UInt32 = 2147483648
MI_CHAR_TYPE: UInt32 = 2
MI_FLAG_CLASS: UInt32 = 1
MI_FLAG_METHOD: UInt32 = 2
MI_FLAG_PROPERTY: UInt32 = 4
MI_FLAG_PARAMETER: UInt32 = 8
MI_FLAG_ASSOCIATION: UInt32 = 16
MI_FLAG_INDICATION: UInt32 = 32
MI_FLAG_REFERENCE: UInt32 = 64
MI_FLAG_ENABLEOVERRIDE: UInt32 = 128
MI_FLAG_DISABLEOVERRIDE: UInt32 = 256
MI_FLAG_RESTRICTED: UInt32 = 512
MI_FLAG_TOSUBCLASS: UInt32 = 1024
MI_FLAG_TRANSLATABLE: UInt32 = 2048
MI_FLAG_KEY: UInt32 = 4096
MI_FLAG_IN: UInt32 = 8192
MI_FLAG_OUT: UInt32 = 16384
MI_FLAG_REQUIRED: UInt32 = 32768
MI_FLAG_STATIC: UInt32 = 65536
MI_FLAG_ABSTRACT: UInt32 = 131072
MI_FLAG_TERMINAL: UInt32 = 262144
MI_FLAG_EXPENSIVE: UInt32 = 524288
MI_FLAG_STREAM: UInt32 = 1048576
MI_FLAG_READONLY: UInt32 = 2097152
MI_FLAG_EXTENDED: UInt32 = 4096
MI_FLAG_NOT_MODIFIED: UInt32 = 33554432
MI_FLAG_NULL: UInt32 = 536870912
MI_FLAG_BORROW: UInt32 = 1073741824
MI_MODULE_FLAG_STANDARD_QUALIFIERS: UInt32 = 1
MI_MODULE_FLAG_DESCRIPTIONS: UInt32 = 2
MI_MODULE_FLAG_VALUES: UInt32 = 4
MI_MODULE_FLAG_MAPPING_STRINGS: UInt32 = 8
MI_MODULE_FLAG_BOOLEANS: UInt32 = 16
MI_MODULE_FLAG_CPLUSPLUS: UInt32 = 32
MI_MODULE_FLAG_LOCALIZED: UInt32 = 64
MI_MODULE_FLAG_FILTER_SUPPORT: UInt32 = 128
MI_MAX_LOCALE_SIZE: UInt32 = 128
MI_WRITEMESSAGE_CHANNEL_WARNING: UInt32 = 0
MI_WRITEMESSAGE_CHANNEL_VERBOSE: UInt32 = 1
MI_WRITEMESSAGE_CHANNEL_DEBUG: UInt32 = 2
MI_CALL_VERSION: UInt32 = 1
MI_OPERATIONFLAGS_MANUAL_ACK_RESULTS: UInt32 = 1
MI_OPERATIONFLAGS_NO_RTTI: UInt32 = 1024
MI_OPERATIONFLAGS_BASIC_RTTI: UInt32 = 2
MI_OPERATIONFLAGS_STANDARD_RTTI: UInt32 = 2048
MI_OPERATIONFLAGS_FULL_RTTI: UInt32 = 4
MI_OPERATIONFLAGS_DEFAULT_RTTI: UInt32 = 0
MI_OPERATIONFLAGS_LOCALIZED_QUALIFIERS: UInt32 = 8
MI_OPERATIONFLAGS_EXPENSIVE_PROPERTIES: UInt32 = 64
MI_OPERATIONFLAGS_POLYMORPHISM_SHALLOW: UInt32 = 128
MI_OPERATIONFLAGS_POLYMORPHISM_DEEP_BASE_PROPS_ONLY: UInt32 = 384
MI_OPERATIONFLAGS_REPORT_OPERATION_STARTED: UInt32 = 512
MI_SUBSCRIBE_BOOKMARK_OLDEST: String = 'MI_SUBSCRIBE_BOOKMARK_OLDEST'
MI_SUBSCRIBE_BOOKMARK_NEWEST: String = 'MI_SUBSCRIBE_BOOKMARK_NEWEST'
MI_SERIALIZER_FLAGS_CLASS_DEEP: UInt32 = 1
MI_SERIALIZER_FLAGS_INSTANCE_WITH_CLASS: UInt32 = 1
WBEMS_DISPID_DERIVATION: UInt32 = 23
WBEMS_DISPID_OBJECT_READY: UInt32 = 1
WBEMS_DISPID_COMPLETED: UInt32 = 2
WBEMS_DISPID_PROGRESS: UInt32 = 3
WBEMS_DISPID_OBJECT_PUT: UInt32 = 4
WBEMS_DISPID_CONNECTION_READY: UInt32 = 5
WBEM_NO_WAIT: Int32 = 0
WBEM_INFINITE: Int32 = -1
@cfunctype('mi.dll')
def MI_Application_InitializeV1(flags: UInt32, applicationID: POINTER(UInt16), extendedError: POINTER(POINTER(win32more.System.Wmi.MI_Instance_head)), application: POINTER(win32more.System.Wmi.MI_Application_head)) -> win32more.System.Wmi.MI_Result: ...
CIMTYPE_ENUMERATION = Int32
CIM_ILLEGAL: CIMTYPE_ENUMERATION = 4095
CIM_EMPTY: CIMTYPE_ENUMERATION = 0
CIM_SINT8: CIMTYPE_ENUMERATION = 16
CIM_UINT8: CIMTYPE_ENUMERATION = 17
CIM_SINT16: CIMTYPE_ENUMERATION = 2
CIM_UINT16: CIMTYPE_ENUMERATION = 18
CIM_SINT32: CIMTYPE_ENUMERATION = 3
CIM_UINT32: CIMTYPE_ENUMERATION = 19
CIM_SINT64: CIMTYPE_ENUMERATION = 20
CIM_UINT64: CIMTYPE_ENUMERATION = 21
CIM_REAL32: CIMTYPE_ENUMERATION = 4
CIM_REAL64: CIMTYPE_ENUMERATION = 5
CIM_BOOLEAN: CIMTYPE_ENUMERATION = 11
CIM_STRING: CIMTYPE_ENUMERATION = 8
CIM_DATETIME: CIMTYPE_ENUMERATION = 101
CIM_REFERENCE: CIMTYPE_ENUMERATION = 102
CIM_CHAR16: CIMTYPE_ENUMERATION = 103
CIM_OBJECT: CIMTYPE_ENUMERATION = 13
CIM_FLAG_ARRAY: CIMTYPE_ENUMERATION = 8192
class IEnumWbemClassObject(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('027947e1-d731-11ce-a3-57-00-00-00-00-00-01')
    @commethod(3)
    def Reset() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Next(lTimeout: Int32, uCount: UInt32, apObjects: POINTER(win32more.System.Wmi.IWbemClassObject_head), puReturned: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def NextAsync(uCount: UInt32, pSink: win32more.System.Wmi.IWbemObjectSink_head) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(win32more.System.Wmi.IEnumWbemClassObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Skip(lTimeout: Int32, nCount: UInt32) -> win32more.Foundation.HRESULT: ...
class IMofCompiler(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('6daf974e-2e37-11d2-ae-c9-00-c0-4f-b6-88-20')
    @commethod(3)
    def CompileFile(FileName: win32more.Foundation.PWSTR, ServerAndNamespace: win32more.Foundation.PWSTR, User: win32more.Foundation.PWSTR, Authority: win32more.Foundation.PWSTR, Password: win32more.Foundation.PWSTR, lOptionFlags: Int32, lClassFlags: Int32, lInstanceFlags: Int32, pInfo: POINTER(win32more.System.Wmi.WBEM_COMPILE_STATUS_INFO_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CompileBuffer(BuffSize: Int32, pBuffer: c_char_p_no, ServerAndNamespace: win32more.Foundation.PWSTR, User: win32more.Foundation.PWSTR, Authority: win32more.Foundation.PWSTR, Password: win32more.Foundation.PWSTR, lOptionFlags: Int32, lClassFlags: Int32, lInstanceFlags: Int32, pInfo: POINTER(win32more.System.Wmi.WBEM_COMPILE_STATUS_INFO_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CreateBMOF(TextFileName: win32more.Foundation.PWSTR, BMOFFileName: win32more.Foundation.PWSTR, ServerAndNamespace: win32more.Foundation.PWSTR, lOptionFlags: Int32, lClassFlags: Int32, lInstanceFlags: Int32, pInfo: POINTER(win32more.System.Wmi.WBEM_COMPILE_STATUS_INFO_head)) -> win32more.Foundation.HRESULT: ...
class ISWbemDateTime(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('5e97458a-cf77-11d3-b3-8f-00-10-5a-1f-47-3a')
    @commethod(7)
    def get_Value(strValue: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_Value(strValue: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Year(iYear: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_Year(iYear: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_YearSpecified(bYearSpecified: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_YearSpecified(bYearSpecified: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_Month(iMonth: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_Month(iMonth: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_MonthSpecified(bMonthSpecified: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_MonthSpecified(bMonthSpecified: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_Day(iDay: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def put_Day(iDay: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def get_DaySpecified(bDaySpecified: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def put_DaySpecified(bDaySpecified: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def get_Hours(iHours: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def put_Hours(iHours: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def get_HoursSpecified(bHoursSpecified: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def put_HoursSpecified(bHoursSpecified: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_Minutes(iMinutes: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def put_Minutes(iMinutes: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def get_MinutesSpecified(bMinutesSpecified: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def put_MinutesSpecified(bMinutesSpecified: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def get_Seconds(iSeconds: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def put_Seconds(iSeconds: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def get_SecondsSpecified(bSecondsSpecified: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def put_SecondsSpecified(bSecondsSpecified: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def get_Microseconds(iMicroseconds: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def put_Microseconds(iMicroseconds: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def get_MicrosecondsSpecified(bMicrosecondsSpecified: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def put_MicrosecondsSpecified(bMicrosecondsSpecified: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def get_UTC(iUTC: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def put_UTC(iUTC: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def get_UTCSpecified(bUTCSpecified: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def put_UTCSpecified(bUTCSpecified: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def get_IsInterval(bIsInterval: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def put_IsInterval(bIsInterval: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def GetVarDate(bIsLocal: win32more.Foundation.VARIANT_BOOL, dVarDate: POINTER(Double)) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def SetVarDate(dVarDate: Double, bIsLocal: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def GetFileTime(bIsLocal: win32more.Foundation.VARIANT_BOOL, strFileTime: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def SetFileTime(strFileTime: win32more.Foundation.BSTR, bIsLocal: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
class ISWbemEventSource(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('27d54d92-0ebe-11d2-8b-22-00-60-08-06-d9-b6')
    @commethod(7)
    def NextEvent(iTimeoutMs: Int32, objWbemObject: POINTER(win32more.System.Wmi.ISWbemObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Security_(objWbemSecurity: POINTER(win32more.System.Wmi.ISWbemSecurity_head)) -> win32more.Foundation.HRESULT: ...
class ISWbemLastError(c_void_p):
    extends: win32more.System.Wmi.ISWbemObject
    Guid = Guid('d962db84-d4bb-11d1-8b-09-00-60-08-06-d9-b6')
class ISWbemLocator(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('76a6415b-cb41-11d1-8b-02-00-60-08-06-d9-b6')
    @commethod(7)
    def ConnectServer(strServer: win32more.Foundation.BSTR, strNamespace: win32more.Foundation.BSTR, strUser: win32more.Foundation.BSTR, strPassword: win32more.Foundation.BSTR, strLocale: win32more.Foundation.BSTR, strAuthority: win32more.Foundation.BSTR, iSecurityFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemServices: POINTER(win32more.System.Wmi.ISWbemServices_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Security_(objWbemSecurity: POINTER(win32more.System.Wmi.ISWbemSecurity_head)) -> win32more.Foundation.HRESULT: ...
class ISWbemMethod(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('422e8e90-d955-11d1-8b-09-00-60-08-06-d9-b6')
    @commethod(7)
    def get_Name(strName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Origin(strOrigin: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_InParameters(objWbemInParameters: POINTER(win32more.System.Wmi.ISWbemObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_OutParameters(objWbemOutParameters: POINTER(win32more.System.Wmi.ISWbemObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_Qualifiers_(objWbemQualifierSet: POINTER(win32more.System.Wmi.ISWbemQualifierSet_head)) -> win32more.Foundation.HRESULT: ...
class ISWbemMethodSet(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('c93ba292-d955-11d1-8b-09-00-60-08-06-d9-b6')
    @commethod(7)
    def get__NewEnum(pUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Item(strName: win32more.Foundation.BSTR, iFlags: Int32, objWbemMethod: POINTER(win32more.System.Wmi.ISWbemMethod_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(iCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class ISWbemNamedValue(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('76a64164-cb41-11d1-8b-02-00-60-08-06-d9-b6')
    @commethod(7)
    def get_Value(varValue: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_Value(varValue: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(strName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class ISWbemNamedValueSet(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('cf2376ea-ce8c-11d1-8b-05-00-60-08-06-d9-b6')
    @commethod(7)
    def get__NewEnum(pUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Item(strName: win32more.Foundation.BSTR, iFlags: Int32, objWbemNamedValue: POINTER(win32more.System.Wmi.ISWbemNamedValue_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(iCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Add(strName: win32more.Foundation.BSTR, varValue: POINTER(win32more.System.Com.VARIANT_head), iFlags: Int32, objWbemNamedValue: POINTER(win32more.System.Wmi.ISWbemNamedValue_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(strName: win32more.Foundation.BSTR, iFlags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Clone(objWbemNamedValueSet: POINTER(win32more.System.Wmi.ISWbemNamedValueSet_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def DeleteAll() -> win32more.Foundation.HRESULT: ...
class ISWbemObject(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('76a6415a-cb41-11d1-8b-02-00-60-08-06-d9-b6')
    @commethod(7)
    def Put_(iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemObjectPath: POINTER(win32more.System.Wmi.ISWbemObjectPath_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def PutAsync_(objWbemSink: win32more.System.Com.IDispatch_head, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemAsyncContext: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Delete_(iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def DeleteAsync_(objWbemSink: win32more.System.Com.IDispatch_head, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemAsyncContext: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Instances_(iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemObjectSet: POINTER(win32more.System.Wmi.ISWbemObjectSet_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def InstancesAsync_(objWbemSink: win32more.System.Com.IDispatch_head, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemAsyncContext: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def Subclasses_(iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemObjectSet: POINTER(win32more.System.Wmi.ISWbemObjectSet_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SubclassesAsync_(objWbemSink: win32more.System.Com.IDispatch_head, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemAsyncContext: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def Associators_(strAssocClass: win32more.Foundation.BSTR, strResultClass: win32more.Foundation.BSTR, strResultRole: win32more.Foundation.BSTR, strRole: win32more.Foundation.BSTR, bClassesOnly: win32more.Foundation.VARIANT_BOOL, bSchemaOnly: win32more.Foundation.VARIANT_BOOL, strRequiredAssocQualifier: win32more.Foundation.BSTR, strRequiredQualifier: win32more.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemObjectSet: POINTER(win32more.System.Wmi.ISWbemObjectSet_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def AssociatorsAsync_(objWbemSink: win32more.System.Com.IDispatch_head, strAssocClass: win32more.Foundation.BSTR, strResultClass: win32more.Foundation.BSTR, strResultRole: win32more.Foundation.BSTR, strRole: win32more.Foundation.BSTR, bClassesOnly: win32more.Foundation.VARIANT_BOOL, bSchemaOnly: win32more.Foundation.VARIANT_BOOL, strRequiredAssocQualifier: win32more.Foundation.BSTR, strRequiredQualifier: win32more.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemAsyncContext: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def References_(strResultClass: win32more.Foundation.BSTR, strRole: win32more.Foundation.BSTR, bClassesOnly: win32more.Foundation.VARIANT_BOOL, bSchemaOnly: win32more.Foundation.VARIANT_BOOL, strRequiredQualifier: win32more.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemObjectSet: POINTER(win32more.System.Wmi.ISWbemObjectSet_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def ReferencesAsync_(objWbemSink: win32more.System.Com.IDispatch_head, strResultClass: win32more.Foundation.BSTR, strRole: win32more.Foundation.BSTR, bClassesOnly: win32more.Foundation.VARIANT_BOOL, bSchemaOnly: win32more.Foundation.VARIANT_BOOL, strRequiredQualifier: win32more.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemAsyncContext: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def ExecMethod_(strMethodName: win32more.Foundation.BSTR, objWbemInParameters: win32more.System.Com.IDispatch_head, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemOutParameters: POINTER(win32more.System.Wmi.ISWbemObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def ExecMethodAsync_(objWbemSink: win32more.System.Com.IDispatch_head, strMethodName: win32more.Foundation.BSTR, objWbemInParameters: win32more.System.Com.IDispatch_head, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemAsyncContext: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def Clone_(objWbemObject: POINTER(win32more.System.Wmi.ISWbemObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def GetObjectText_(iFlags: Int32, strObjectText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def SpawnDerivedClass_(iFlags: Int32, objWbemObject: POINTER(win32more.System.Wmi.ISWbemObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def SpawnInstance_(iFlags: Int32, objWbemObject: POINTER(win32more.System.Wmi.ISWbemObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def CompareTo_(objWbemObject: win32more.System.Com.IDispatch_head, iFlags: Int32, bResult: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_Qualifiers_(objWbemQualifierSet: POINTER(win32more.System.Wmi.ISWbemQualifierSet_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def get_Properties_(objWbemPropertySet: POINTER(win32more.System.Wmi.ISWbemPropertySet_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def get_Methods_(objWbemMethodSet: POINTER(win32more.System.Wmi.ISWbemMethodSet_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def get_Derivation_(strClassNameArray: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def get_Path_(objWbemObjectPath: POINTER(win32more.System.Wmi.ISWbemObjectPath_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def get_Security_(objWbemSecurity: POINTER(win32more.System.Wmi.ISWbemSecurity_head)) -> win32more.Foundation.HRESULT: ...
class ISWbemObjectEx(c_void_p):
    extends: win32more.System.Wmi.ISWbemObject
    Guid = Guid('269ad56a-8a67-4129-bc-8c-05-06-dc-fe-98-80')
    @commethod(32)
    def Refresh_(iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def get_SystemProperties_(objWbemPropertySet: POINTER(win32more.System.Wmi.ISWbemPropertySet_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def GetText_(iObjectTextFormat: win32more.System.Wmi.WbemObjectTextFormatEnum, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, bsText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def SetFromText_(bsText: win32more.Foundation.BSTR, iObjectTextFormat: win32more.System.Wmi.WbemObjectTextFormatEnum, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
class ISWbemObjectPath(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('5791bc27-ce9c-11d1-97-bf-00-00-f8-1e-84-9c')
    @commethod(7)
    def get_Path(strPath: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_Path(strPath: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_RelPath(strRelPath: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_RelPath(strRelPath: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_Server(strServer: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_Server(strServer: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_Namespace(strNamespace: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_Namespace(strNamespace: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_ParentNamespace(strParentNamespace: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def get_DisplayName(strDisplayName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def put_DisplayName(strDisplayName: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def get_Class(strClass: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def put_Class(strClass: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def get_IsClass(bIsClass: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def SetAsClass() -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def get_IsSingleton(bIsSingleton: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def SetAsSingleton() -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def get_Keys(objWbemNamedValueSet: POINTER(win32more.System.Wmi.ISWbemNamedValueSet_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_Security_(objWbemSecurity: POINTER(win32more.System.Wmi.ISWbemSecurity_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def get_Locale(strLocale: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def put_Locale(strLocale: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def get_Authority(strAuthority: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def put_Authority(strAuthority: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class ISWbemObjectSet(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('76a6415f-cb41-11d1-8b-02-00-60-08-06-d9-b6')
    @commethod(7)
    def get__NewEnum(pUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Item(strObjectPath: win32more.Foundation.BSTR, iFlags: Int32, objWbemObject: POINTER(win32more.System.Wmi.ISWbemObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(iCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Security_(objWbemSecurity: POINTER(win32more.System.Wmi.ISWbemSecurity_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def ItemIndex(lIndex: Int32, objWbemObject: POINTER(win32more.System.Wmi.ISWbemObject_head)) -> win32more.Foundation.HRESULT: ...
class ISWbemPrivilege(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('26ee67bd-5804-11d2-8b-4a-00-60-08-06-d9-b6')
    @commethod(7)
    def get_IsEnabled(bIsEnabled: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_IsEnabled(bIsEnabled: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(strDisplayName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_DisplayName(strDisplayName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_Identifier(iPrivilege: POINTER(win32more.System.Wmi.WbemPrivilegeEnum)) -> win32more.Foundation.HRESULT: ...
class ISWbemPrivilegeSet(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('26ee67bf-5804-11d2-8b-4a-00-60-08-06-d9-b6')
    @commethod(7)
    def get__NewEnum(pUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Item(iPrivilege: win32more.System.Wmi.WbemPrivilegeEnum, objWbemPrivilege: POINTER(win32more.System.Wmi.ISWbemPrivilege_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(iCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Add(iPrivilege: win32more.System.Wmi.WbemPrivilegeEnum, bIsEnabled: win32more.Foundation.VARIANT_BOOL, objWbemPrivilege: POINTER(win32more.System.Wmi.ISWbemPrivilege_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(iPrivilege: win32more.System.Wmi.WbemPrivilegeEnum) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def DeleteAll() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def AddAsString(strPrivilege: win32more.Foundation.BSTR, bIsEnabled: win32more.Foundation.VARIANT_BOOL, objWbemPrivilege: POINTER(win32more.System.Wmi.ISWbemPrivilege_head)) -> win32more.Foundation.HRESULT: ...
class ISWbemProperty(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('1a388f98-d4ba-11d1-8b-09-00-60-08-06-d9-b6')
    @commethod(7)
    def get_Value(varValue: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_Value(varValue: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(strName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_IsLocal(bIsLocal: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_Origin(strOrigin: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def get_CIMType(iCimType: POINTER(win32more.System.Wmi.WbemCimtypeEnum)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_Qualifiers_(objWbemQualifierSet: POINTER(win32more.System.Wmi.ISWbemQualifierSet_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_IsArray(bIsArray: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
class ISWbemPropertySet(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('dea0a7b2-d4ba-11d1-8b-09-00-60-08-06-d9-b6')
    @commethod(7)
    def get__NewEnum(pUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Item(strName: win32more.Foundation.BSTR, iFlags: Int32, objWbemProperty: POINTER(win32more.System.Wmi.ISWbemProperty_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(iCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Add(strName: win32more.Foundation.BSTR, iCIMType: win32more.System.Wmi.WbemCimtypeEnum, bIsArray: win32more.Foundation.VARIANT_BOOL, iFlags: Int32, objWbemProperty: POINTER(win32more.System.Wmi.ISWbemProperty_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(strName: win32more.Foundation.BSTR, iFlags: Int32) -> win32more.Foundation.HRESULT: ...
class ISWbemQualifier(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('79b05932-d3b7-11d1-8b-06-00-60-08-06-d9-b6')
    @commethod(7)
    def get_Value(varValue: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_Value(varValue: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(strName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_IsLocal(bIsLocal: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_PropagatesToSubclass(bPropagatesToSubclass: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def put_PropagatesToSubclass(bPropagatesToSubclass: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def get_PropagatesToInstance(bPropagatesToInstance: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def put_PropagatesToInstance(bPropagatesToInstance: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def get_IsOverridable(bIsOverridable: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def put_IsOverridable(bIsOverridable: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def get_IsAmended(bIsAmended: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
class ISWbemQualifierSet(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('9b16ed16-d3df-11d1-8b-08-00-60-08-06-d9-b6')
    @commethod(7)
    def get__NewEnum(pUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Item(name: win32more.Foundation.BSTR, iFlags: Int32, objWbemQualifier: POINTER(win32more.System.Wmi.ISWbemQualifier_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(iCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Add(strName: win32more.Foundation.BSTR, varVal: POINTER(win32more.System.Com.VARIANT_head), bPropagatesToSubclass: win32more.Foundation.VARIANT_BOOL, bPropagatesToInstance: win32more.Foundation.VARIANT_BOOL, bIsOverridable: win32more.Foundation.VARIANT_BOOL, iFlags: Int32, objWbemQualifier: POINTER(win32more.System.Wmi.ISWbemQualifier_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(strName: win32more.Foundation.BSTR, iFlags: Int32) -> win32more.Foundation.HRESULT: ...
class ISWbemRefreshableItem(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('5ad4bf92-daab-11d3-b3-8f-00-10-5a-1f-47-3a')
    @commethod(7)
    def get_Index(iIndex: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def get_Refresher(objWbemRefresher: POINTER(win32more.System.Wmi.ISWbemRefresher_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_IsSet(bIsSet: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def get_Object(objWbemObject: POINTER(win32more.System.Wmi.ISWbemObjectEx_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_ObjectSet(objWbemObjectSet: POINTER(win32more.System.Wmi.ISWbemObjectSet_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Remove(iFlags: Int32) -> win32more.Foundation.HRESULT: ...
class ISWbemRefresher(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('14d8250e-d9c2-11d3-b3-8f-00-10-5a-1f-47-3a')
    @commethod(7)
    def get__NewEnum(pUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Item(iIndex: Int32, objWbemRefreshableItem: POINTER(win32more.System.Wmi.ISWbemRefreshableItem_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(iCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Add(objWbemServices: win32more.System.Wmi.ISWbemServicesEx_head, bsInstancePath: win32more.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemRefreshableItem: POINTER(win32more.System.Wmi.ISWbemRefreshableItem_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def AddEnum(objWbemServices: win32more.System.Wmi.ISWbemServicesEx_head, bsClassName: win32more.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemRefreshableItem: POINTER(win32more.System.Wmi.ISWbemRefreshableItem_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Remove(iIndex: Int32, iFlags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def Refresh(iFlags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def get_AutoReconnect(bCount: POINTER(win32more.Foundation.VARIANT_BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def put_AutoReconnect(bCount: win32more.Foundation.VARIANT_BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def DeleteAll() -> win32more.Foundation.HRESULT: ...
class ISWbemSecurity(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('b54d66e6-2287-11d2-8b-33-00-60-08-06-d9-b6')
    @commethod(7)
    def get_ImpersonationLevel(iImpersonationLevel: POINTER(win32more.System.Wmi.WbemImpersonationLevelEnum)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def put_ImpersonationLevel(iImpersonationLevel: win32more.System.Wmi.WbemImpersonationLevelEnum) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def get_AuthenticationLevel(iAuthenticationLevel: POINTER(win32more.System.Wmi.WbemAuthenticationLevelEnum)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def put_AuthenticationLevel(iAuthenticationLevel: win32more.System.Wmi.WbemAuthenticationLevelEnum) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def get_Privileges(objWbemPrivilegeSet: POINTER(win32more.System.Wmi.ISWbemPrivilegeSet_head)) -> win32more.Foundation.HRESULT: ...
class ISWbemServices(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('76a6415c-cb41-11d1-8b-02-00-60-08-06-d9-b6')
    @commethod(7)
    def Get(strObjectPath: win32more.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemObject: POINTER(win32more.System.Wmi.ISWbemObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetAsync(objWbemSink: win32more.System.Com.IDispatch_head, strObjectPath: win32more.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemAsyncContext: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Delete(strObjectPath: win32more.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def DeleteAsync(objWbemSink: win32more.System.Com.IDispatch_head, strObjectPath: win32more.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemAsyncContext: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def InstancesOf(strClass: win32more.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemObjectSet: POINTER(win32more.System.Wmi.ISWbemObjectSet_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def InstancesOfAsync(objWbemSink: win32more.System.Com.IDispatch_head, strClass: win32more.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemAsyncContext: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def SubclassesOf(strSuperclass: win32more.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemObjectSet: POINTER(win32more.System.Wmi.ISWbemObjectSet_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SubclassesOfAsync(objWbemSink: win32more.System.Com.IDispatch_head, strSuperclass: win32more.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemAsyncContext: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def ExecQuery(strQuery: win32more.Foundation.BSTR, strQueryLanguage: win32more.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemObjectSet: POINTER(win32more.System.Wmi.ISWbemObjectSet_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def ExecQueryAsync(objWbemSink: win32more.System.Com.IDispatch_head, strQuery: win32more.Foundation.BSTR, strQueryLanguage: win32more.Foundation.BSTR, lFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemAsyncContext: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def AssociatorsOf(strObjectPath: win32more.Foundation.BSTR, strAssocClass: win32more.Foundation.BSTR, strResultClass: win32more.Foundation.BSTR, strResultRole: win32more.Foundation.BSTR, strRole: win32more.Foundation.BSTR, bClassesOnly: win32more.Foundation.VARIANT_BOOL, bSchemaOnly: win32more.Foundation.VARIANT_BOOL, strRequiredAssocQualifier: win32more.Foundation.BSTR, strRequiredQualifier: win32more.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemObjectSet: POINTER(win32more.System.Wmi.ISWbemObjectSet_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def AssociatorsOfAsync(objWbemSink: win32more.System.Com.IDispatch_head, strObjectPath: win32more.Foundation.BSTR, strAssocClass: win32more.Foundation.BSTR, strResultClass: win32more.Foundation.BSTR, strResultRole: win32more.Foundation.BSTR, strRole: win32more.Foundation.BSTR, bClassesOnly: win32more.Foundation.VARIANT_BOOL, bSchemaOnly: win32more.Foundation.VARIANT_BOOL, strRequiredAssocQualifier: win32more.Foundation.BSTR, strRequiredQualifier: win32more.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemAsyncContext: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def ReferencesTo(strObjectPath: win32more.Foundation.BSTR, strResultClass: win32more.Foundation.BSTR, strRole: win32more.Foundation.BSTR, bClassesOnly: win32more.Foundation.VARIANT_BOOL, bSchemaOnly: win32more.Foundation.VARIANT_BOOL, strRequiredQualifier: win32more.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemObjectSet: POINTER(win32more.System.Wmi.ISWbemObjectSet_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def ReferencesToAsync(objWbemSink: win32more.System.Com.IDispatch_head, strObjectPath: win32more.Foundation.BSTR, strResultClass: win32more.Foundation.BSTR, strRole: win32more.Foundation.BSTR, bClassesOnly: win32more.Foundation.VARIANT_BOOL, bSchemaOnly: win32more.Foundation.VARIANT_BOOL, strRequiredQualifier: win32more.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemAsyncContext: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def ExecNotificationQuery(strQuery: win32more.Foundation.BSTR, strQueryLanguage: win32more.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemEventSource: POINTER(win32more.System.Wmi.ISWbemEventSource_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def ExecNotificationQueryAsync(objWbemSink: win32more.System.Com.IDispatch_head, strQuery: win32more.Foundation.BSTR, strQueryLanguage: win32more.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemAsyncContext: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def ExecMethod(strObjectPath: win32more.Foundation.BSTR, strMethodName: win32more.Foundation.BSTR, objWbemInParameters: win32more.System.Com.IDispatch_head, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemOutParameters: POINTER(win32more.System.Wmi.ISWbemObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def ExecMethodAsync(objWbemSink: win32more.System.Com.IDispatch_head, strObjectPath: win32more.Foundation.BSTR, strMethodName: win32more.Foundation.BSTR, objWbemInParameters: win32more.System.Com.IDispatch_head, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemAsyncContext: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def get_Security_(objWbemSecurity: POINTER(win32more.System.Wmi.ISWbemSecurity_head)) -> win32more.Foundation.HRESULT: ...
class ISWbemServicesEx(c_void_p):
    extends: win32more.System.Wmi.ISWbemServices
    Guid = Guid('d2f68443-85dc-427e-91-d8-36-65-54-cc-75-4c')
    @commethod(26)
    def Put(objWbemObject: win32more.System.Wmi.ISWbemObjectEx_head, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemObjectPath: POINTER(win32more.System.Wmi.ISWbemObjectPath_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def PutAsync(objWbemSink: win32more.System.Wmi.ISWbemSink_head, objWbemObject: win32more.System.Wmi.ISWbemObjectEx_head, iFlags: Int32, objWbemNamedValueSet: win32more.System.Com.IDispatch_head, objWbemAsyncContext: win32more.System.Com.IDispatch_head) -> win32more.Foundation.HRESULT: ...
class ISWbemSink(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('75718c9f-f029-11d1-a1-ac-00-c0-4f-b6-c2-23')
    @commethod(7)
    def Cancel() -> win32more.Foundation.HRESULT: ...
class ISWbemSinkEvents(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('75718ca0-f029-11d1-a1-ac-00-c0-4f-b6-c2-23')
class IUnsecuredApartment(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1cfaba8c-1523-11d1-ad-79-00-c0-4f-d8-fd-ff')
    @commethod(3)
    def CreateObjectStub(pObject: win32more.System.Com.IUnknown_head, ppStub: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class IWbemAddressResolution(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f7ce2e12-8c90-11d1-9e-7b-00-c0-4f-c3-24-a8')
    @commethod(3)
    def Resolve(wszNamespacePath: win32more.Foundation.PWSTR, wszAddressType: win32more.Foundation.PWSTR, pdwAddressLength: POINTER(UInt32), pabBinaryAddress: POINTER(c_char_p_no)) -> win32more.Foundation.HRESULT: ...
class IWbemBackupRestore(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c49e32c7-bc8b-11d2-85-d4-00-10-5a-1f-83-04')
    @commethod(3)
    def Backup(strBackupToFile: win32more.Foundation.PWSTR, lFlags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Restore(strRestoreFromFile: win32more.Foundation.PWSTR, lFlags: Int32) -> win32more.Foundation.HRESULT: ...
class IWbemBackupRestoreEx(c_void_p):
    extends: win32more.System.Wmi.IWbemBackupRestore
    Guid = Guid('a359dec5-e813-4834-8a-2a-ba-7f-1d-77-7d-76')
    @commethod(5)
    def Pause() -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Resume() -> win32more.Foundation.HRESULT: ...
class IWbemCallResult(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('44aca675-e8fc-11d0-a0-7c-00-c0-4f-b6-88-20')
    @commethod(3)
    def GetResultObject(lTimeout: Int32, ppResultObject: POINTER(win32more.System.Wmi.IWbemClassObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetResultString(lTimeout: Int32, pstrResultString: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetResultServices(lTimeout: Int32, ppServices: POINTER(win32more.System.Wmi.IWbemServices_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetCallStatus(lTimeout: Int32, plStatus: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IWbemClassObject(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('dc12a681-737f-11cf-88-4d-00-aa-00-4b-2e-24')
    @commethod(3)
    def GetQualifierSet(ppQualSet: POINTER(win32more.System.Wmi.IWbemQualifierSet_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Get(wszName: win32more.Foundation.PWSTR, lFlags: Int32, pVal: POINTER(win32more.System.Com.VARIANT_head), pType: POINTER(Int32), plFlavor: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Put(wszName: win32more.Foundation.PWSTR, lFlags: Int32, pVal: POINTER(win32more.System.Com.VARIANT_head), Type: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Delete(wszName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetNames(wszQualifierName: win32more.Foundation.PWSTR, lFlags: Int32, pQualifierVal: POINTER(win32more.System.Com.VARIANT_head), pNames: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def BeginEnumeration(lEnumFlags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Next(lFlags: Int32, strName: POINTER(win32more.Foundation.BSTR), pVal: POINTER(win32more.System.Com.VARIANT_head), pType: POINTER(Int32), plFlavor: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def EndEnumeration() -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetPropertyQualifierSet(wszProperty: win32more.Foundation.PWSTR, ppQualSet: POINTER(win32more.System.Wmi.IWbemQualifierSet_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Clone(ppCopy: POINTER(win32more.System.Wmi.IWbemClassObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetObjectText(lFlags: Int32, pstrObjectText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SpawnDerivedClass(lFlags: Int32, ppNewClass: POINTER(win32more.System.Wmi.IWbemClassObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def SpawnInstance(lFlags: Int32, ppNewInstance: POINTER(win32more.System.Wmi.IWbemClassObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def CompareTo(lFlags: Int32, pCompareTo: win32more.System.Wmi.IWbemClassObject_head) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetPropertyOrigin(wszName: win32more.Foundation.PWSTR, pstrClassName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def InheritsFrom(strAncestor: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetMethod(wszName: win32more.Foundation.PWSTR, lFlags: Int32, ppInSignature: POINTER(win32more.System.Wmi.IWbemClassObject_head), ppOutSignature: POINTER(win32more.System.Wmi.IWbemClassObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def PutMethod(wszName: win32more.Foundation.PWSTR, lFlags: Int32, pInSignature: win32more.System.Wmi.IWbemClassObject_head, pOutSignature: win32more.System.Wmi.IWbemClassObject_head) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def DeleteMethod(wszName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def BeginMethodEnumeration(lEnumFlags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def NextMethod(lFlags: Int32, pstrName: POINTER(win32more.Foundation.BSTR), ppInSignature: POINTER(win32more.System.Wmi.IWbemClassObject_head), ppOutSignature: POINTER(win32more.System.Wmi.IWbemClassObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def EndMethodEnumeration() -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def GetMethodQualifierSet(wszMethod: win32more.Foundation.PWSTR, ppQualSet: POINTER(win32more.System.Wmi.IWbemQualifierSet_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def GetMethodOrigin(wszMethodName: win32more.Foundation.PWSTR, pstrClassName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IWbemClientConnectionTransport(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('a889c72a-fcc1-4a9e-af-61-ed-07-13-33-fb-5b')
    @commethod(3)
    def Open(strAddressType: win32more.Foundation.BSTR, dwBinaryAddressLength: UInt32, abBinaryAddress: c_char_p_no, strObject: win32more.Foundation.BSTR, strUser: win32more.Foundation.BSTR, strPassword: win32more.Foundation.BSTR, strLocale: win32more.Foundation.BSTR, lFlags: Int32, pCtx: win32more.System.Wmi.IWbemContext_head, riid: POINTER(Guid), pInterface: POINTER(c_void_p), pCallRes: POINTER(win32more.System.Wmi.IWbemCallResult_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def OpenAsync(strAddressType: win32more.Foundation.BSTR, dwBinaryAddressLength: UInt32, abBinaryAddress: c_char_p_no, strObject: win32more.Foundation.BSTR, strUser: win32more.Foundation.BSTR, strPassword: win32more.Foundation.BSTR, strLocale: win32more.Foundation.BSTR, lFlags: Int32, pCtx: win32more.System.Wmi.IWbemContext_head, riid: POINTER(Guid), pResponseHandler: win32more.System.Wmi.IWbemObjectSink_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Cancel(lFlags: Int32, pHandler: win32more.System.Wmi.IWbemObjectSink_head) -> win32more.Foundation.HRESULT: ...
class IWbemClientTransport(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f7ce2e11-8c90-11d1-9e-7b-00-c0-4f-c3-24-a8')
    @commethod(3)
    def ConnectServer(strAddressType: win32more.Foundation.BSTR, dwBinaryAddressLength: UInt32, abBinaryAddress: c_char_p_no, strNetworkResource: win32more.Foundation.BSTR, strUser: win32more.Foundation.BSTR, strPassword: win32more.Foundation.BSTR, strLocale: win32more.Foundation.BSTR, lSecurityFlags: Int32, strAuthority: win32more.Foundation.BSTR, pCtx: win32more.System.Wmi.IWbemContext_head, ppNamespace: POINTER(win32more.System.Wmi.IWbemServices_head)) -> win32more.Foundation.HRESULT: ...
class IWbemConfigureRefresher(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('49353c92-516b-11d1-ae-a6-00-c0-4f-b6-88-20')
    @commethod(3)
    def AddObjectByPath(pNamespace: win32more.System.Wmi.IWbemServices_head, wszPath: win32more.Foundation.PWSTR, lFlags: Int32, pContext: win32more.System.Wmi.IWbemContext_head, ppRefreshable: POINTER(win32more.System.Wmi.IWbemClassObject_head), plId: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def AddObjectByTemplate(pNamespace: win32more.System.Wmi.IWbemServices_head, pTemplate: win32more.System.Wmi.IWbemClassObject_head, lFlags: Int32, pContext: win32more.System.Wmi.IWbemContext_head, ppRefreshable: POINTER(win32more.System.Wmi.IWbemClassObject_head), plId: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def AddRefresher(pRefresher: win32more.System.Wmi.IWbemRefresher_head, lFlags: Int32, plId: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Remove(lId: Int32, lFlags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def AddEnum(pNamespace: win32more.System.Wmi.IWbemServices_head, wszClassName: win32more.Foundation.PWSTR, lFlags: Int32, pContext: win32more.System.Wmi.IWbemContext_head, ppEnum: POINTER(win32more.System.Wmi.IWbemHiPerfEnum_head), plId: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class IWbemConnectorLogin(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('d8ec9cb1-b135-4f10-8b-1b-c7-18-8b-b0-d1-86')
    @commethod(3)
    def ConnectorLogin(wszNetworkResource: win32more.Foundation.PWSTR, wszPreferredLocale: win32more.Foundation.PWSTR, lFlags: Int32, pCtx: win32more.System.Wmi.IWbemContext_head, riid: POINTER(Guid), pInterface: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
class IWbemConstructClassObject(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9ef76194-70d5-11d1-ad-90-00-c0-4f-d8-fd-ff')
    @commethod(3)
    def SetInheritanceChain(lNumAntecedents: Int32, awszAntecedents: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetPropertyOrigin(wszPropertyName: win32more.Foundation.PWSTR, lOriginIndex: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetMethodOrigin(wszMethodName: win32more.Foundation.PWSTR, lOriginIndex: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetServerNamespace(wszServer: win32more.Foundation.PWSTR, wszNamespace: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
class IWbemContext(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('44aca674-e8fc-11d0-a0-7c-00-c0-4f-b6-88-20')
    @commethod(3)
    def Clone(ppNewCopy: POINTER(win32more.System.Wmi.IWbemContext_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetNames(lFlags: Int32, pNames: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def BeginEnumeration(lFlags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Next(lFlags: Int32, pstrName: POINTER(win32more.Foundation.BSTR), pValue: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def EndEnumeration() -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetValue(wszName: win32more.Foundation.PWSTR, lFlags: Int32, pValue: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetValue(wszName: win32more.Foundation.PWSTR, lFlags: Int32, pValue: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def DeleteValue(wszName: win32more.Foundation.PWSTR, lFlags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def DeleteAll() -> win32more.Foundation.HRESULT: ...
class IWbemDecoupledBasicEventProvider(c_void_p):
    extends: win32more.System.Wmi.IWbemDecoupledRegistrar
    Guid = Guid('86336d20-ca11-4786-9e-f1-bc-8a-94-6b-42-fc')
    @commethod(5)
    def GetSink(a_Flags: Int32, a_Context: win32more.System.Wmi.IWbemContext_head, a_Sink: POINTER(win32more.System.Wmi.IWbemObjectSink_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetService(a_Flags: Int32, a_Context: win32more.System.Wmi.IWbemContext_head, a_Service: POINTER(win32more.System.Wmi.IWbemServices_head)) -> win32more.Foundation.HRESULT: ...
class IWbemDecoupledRegistrar(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1005cbcf-e64f-4646-bc-d3-3a-08-9d-8a-84-b4')
    @commethod(3)
    def Register(a_Flags: Int32, a_Context: win32more.System.Wmi.IWbemContext_head, a_User: win32more.Foundation.PWSTR, a_Locale: win32more.Foundation.PWSTR, a_Scope: win32more.Foundation.PWSTR, a_Registration: win32more.Foundation.PWSTR, pIUnknown: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def UnRegister() -> win32more.Foundation.HRESULT: ...
class IWbemEventConsumerProvider(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('e246107a-b06e-11d0-ad-61-00-c0-4f-d8-fd-ff')
    @commethod(3)
    def FindConsumer(pLogicalConsumer: win32more.System.Wmi.IWbemClassObject_head, ppConsumer: POINTER(win32more.System.Wmi.IWbemUnboundObjectSink_head)) -> win32more.Foundation.HRESULT: ...
class IWbemEventProvider(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('e245105b-b06e-11d0-ad-61-00-c0-4f-d8-fd-ff')
    @commethod(3)
    def ProvideEvents(pSink: win32more.System.Wmi.IWbemObjectSink_head, lFlags: Int32) -> win32more.Foundation.HRESULT: ...
class IWbemEventProviderQuerySink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('580acaf8-fa1c-11d0-ad-72-00-c0-4f-d8-fd-ff')
    @commethod(3)
    def NewQuery(dwId: UInt32, wszQueryLanguage: POINTER(UInt16), wszQuery: POINTER(UInt16)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CancelQuery(dwId: UInt32) -> win32more.Foundation.HRESULT: ...
class IWbemEventProviderSecurity(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('631f7d96-d993-11d2-b3-39-00-10-5a-1f-4a-af')
    @commethod(3)
    def AccessCheck(wszQueryLanguage: POINTER(UInt16), wszQuery: POINTER(UInt16), lSidLength: Int32, pSid: c_char_p_no) -> win32more.Foundation.HRESULT: ...
class IWbemEventSink(c_void_p):
    extends: win32more.System.Wmi.IWbemObjectSink
    Guid = Guid('3ae0080a-7e3a-4366-bf-89-0f-ee-dc-93-16-59')
    @commethod(5)
    def SetSinkSecurity(lSDLength: Int32, pSD: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def IsActive() -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetRestrictedSink(lNumQueries: Int32, awszQueries: POINTER(win32more.Foundation.PWSTR), pCallback: win32more.System.Com.IUnknown_head, ppSink: POINTER(win32more.System.Wmi.IWbemEventSink_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetBatchingParameters(lFlags: Int32, dwMaxBufferSize: UInt32, dwMaxSendLatency: UInt32) -> win32more.Foundation.HRESULT: ...
class IWbemHiPerfEnum(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('2705c288-79ae-11d2-b3-48-00-10-5a-1f-81-77')
    @commethod(3)
    def AddObjects(lFlags: Int32, uNumObjects: UInt32, apIds: POINTER(Int32), apObj: POINTER(win32more.System.Wmi.IWbemObjectAccess_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveObjects(lFlags: Int32, uNumObjects: UInt32, apIds: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetObjects(lFlags: Int32, uNumObjects: UInt32, apObj: POINTER(win32more.System.Wmi.IWbemObjectAccess_head), puReturned: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveAll(lFlags: Int32) -> win32more.Foundation.HRESULT: ...
class IWbemHiPerfProvider(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('49353c93-516b-11d1-ae-a6-00-c0-4f-b6-88-20')
    @commethod(3)
    def QueryInstances(pNamespace: win32more.System.Wmi.IWbemServices_head, wszClass: win32more.Foundation.PWSTR, lFlags: Int32, pCtx: win32more.System.Wmi.IWbemContext_head, pSink: win32more.System.Wmi.IWbemObjectSink_head) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CreateRefresher(pNamespace: win32more.System.Wmi.IWbemServices_head, lFlags: Int32, ppRefresher: POINTER(win32more.System.Wmi.IWbemRefresher_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CreateRefreshableObject(pNamespace: win32more.System.Wmi.IWbemServices_head, pTemplate: win32more.System.Wmi.IWbemObjectAccess_head, pRefresher: win32more.System.Wmi.IWbemRefresher_head, lFlags: Int32, pContext: win32more.System.Wmi.IWbemContext_head, ppRefreshable: POINTER(win32more.System.Wmi.IWbemObjectAccess_head), plId: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def StopRefreshing(pRefresher: win32more.System.Wmi.IWbemRefresher_head, lId: Int32, lFlags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def CreateRefreshableEnum(pNamespace: win32more.System.Wmi.IWbemServices_head, wszClass: win32more.Foundation.PWSTR, pRefresher: win32more.System.Wmi.IWbemRefresher_head, lFlags: Int32, pContext: win32more.System.Wmi.IWbemContext_head, pHiPerfEnum: win32more.System.Wmi.IWbemHiPerfEnum_head, plId: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetObjects(pNamespace: win32more.System.Wmi.IWbemServices_head, lNumObjects: Int32, apObj: POINTER(win32more.System.Wmi.IWbemObjectAccess_head), lFlags: Int32, pContext: win32more.System.Wmi.IWbemContext_head) -> win32more.Foundation.HRESULT: ...
class IWbemLevel1Login(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('f309ad18-d86a-11d0-a0-75-00-c0-4f-b6-88-20')
    @commethod(3)
    def EstablishPosition(wszLocaleList: win32more.Foundation.PWSTR, dwNumLocales: UInt32, reserved: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def RequestChallenge(wszNetworkResource: win32more.Foundation.PWSTR, wszUser: win32more.Foundation.PWSTR, Nonce: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def WBEMLogin(wszPreferredLocale: win32more.Foundation.PWSTR, AccessToken: c_char_p_no, lFlags: Int32, pCtx: win32more.System.Wmi.IWbemContext_head, ppNamespace: POINTER(win32more.System.Wmi.IWbemServices_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def NTLMLogin(wszNetworkResource: win32more.Foundation.PWSTR, wszPreferredLocale: win32more.Foundation.PWSTR, lFlags: Int32, pCtx: win32more.System.Wmi.IWbemContext_head, ppNamespace: POINTER(win32more.System.Wmi.IWbemServices_head)) -> win32more.Foundation.HRESULT: ...
class IWbemLocator(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('dc12a687-737f-11cf-88-4d-00-aa-00-4b-2e-24')
    @commethod(3)
    def ConnectServer(strNetworkResource: win32more.Foundation.BSTR, strUser: win32more.Foundation.BSTR, strPassword: win32more.Foundation.BSTR, strLocale: win32more.Foundation.BSTR, lSecurityFlags: Int32, strAuthority: win32more.Foundation.BSTR, pCtx: win32more.System.Wmi.IWbemContext_head, ppNamespace: POINTER(win32more.System.Wmi.IWbemServices_head)) -> win32more.Foundation.HRESULT: ...
class IWbemObjectAccess(c_void_p):
    extends: win32more.System.Wmi.IWbemClassObject
    Guid = Guid('49353c9a-516b-11d1-ae-a6-00-c0-4f-b6-88-20')
    @commethod(27)
    def GetPropertyHandle(wszPropertyName: win32more.Foundation.PWSTR, pType: POINTER(Int32), plHandle: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def WritePropertyValue(lHandle: Int32, lNumBytes: Int32, aData: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def ReadPropertyValue(lHandle: Int32, lBufferSize: Int32, plNumBytes: POINTER(Int32), aData: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def ReadDWORD(lHandle: Int32, pdw: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def WriteDWORD(lHandle: Int32, dw: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def ReadQWORD(lHandle: Int32, pqw: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def WriteQWORD(lHandle: Int32, pw: UInt64) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def GetPropertyInfoByHandle(lHandle: Int32, pstrName: POINTER(win32more.Foundation.BSTR), pType: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def Lock(lFlags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def Unlock(lFlags: Int32) -> win32more.Foundation.HRESULT: ...
class IWbemObjectSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('7c857801-7381-11cf-88-4d-00-aa-00-4b-2e-24')
    @commethod(3)
    def Indicate(lObjectCount: Int32, apObjArray: POINTER(win32more.System.Wmi.IWbemClassObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetStatus(lFlags: Int32, hResult: win32more.Foundation.HRESULT, strParam: win32more.Foundation.BSTR, pObjParam: win32more.System.Wmi.IWbemClassObject_head) -> win32more.Foundation.HRESULT: ...
class IWbemObjectSinkEx(c_void_p):
    extends: win32more.System.Wmi.IWbemObjectSink
    Guid = Guid('e7d35cfa-348b-485e-b5-24-25-27-25-d6-97-ca')
    @commethod(5)
    def WriteMessage(uChannel: UInt32, strMessage: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def WriteError(pObjError: win32more.System.Wmi.IWbemClassObject_head, puReturned: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def PromptUser(strMessage: win32more.Foundation.BSTR, uPromptType: Byte, puReturned: c_char_p_no) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def WriteProgress(strActivity: win32more.Foundation.BSTR, strCurrentOperation: win32more.Foundation.BSTR, strStatusDescription: win32more.Foundation.BSTR, uPercentComplete: UInt32, uSecondsRemaining: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def WriteStreamParameter(strName: win32more.Foundation.BSTR, vtValue: POINTER(win32more.System.Com.VARIANT_head), ulType: UInt32, ulFlags: UInt32) -> win32more.Foundation.HRESULT: ...
class IWbemObjectTextSrc(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('bfbf883a-cad7-11d3-a1-1b-00-10-5a-1f-51-5a')
    @commethod(3)
    def GetText(lFlags: Int32, pObj: win32more.System.Wmi.IWbemClassObject_head, uObjTextFormat: UInt32, pCtx: win32more.System.Wmi.IWbemContext_head, strText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CreateFromText(lFlags: Int32, strText: win32more.Foundation.BSTR, uObjTextFormat: UInt32, pCtx: win32more.System.Wmi.IWbemContext_head, pNewObj: POINTER(win32more.System.Wmi.IWbemClassObject_head)) -> win32more.Foundation.HRESULT: ...
class IWbemPath(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3bc15af2-736c-477e-9e-51-23-8a-f8-66-7d-cc')
    @commethod(3)
    def SetText(uMode: UInt32, pszPath: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetText(lFlags: Int32, puBuffLength: POINTER(UInt32), pszText: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetInfo(uRequestedInfo: UInt32, puResponse: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def SetServer(Name: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetServer(puNameBufLength: POINTER(UInt32), pName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetNamespaceCount(puCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def SetNamespaceAt(uIndex: UInt32, pszName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetNamespaceAt(uIndex: UInt32, puNameBufLength: POINTER(UInt32), pName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def RemoveNamespaceAt(uIndex: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def RemoveAllNamespaces() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetScopeCount(puCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetScope(uIndex: UInt32, pszClass: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def SetScopeFromText(uIndex: UInt32, pszText: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetScope(uIndex: UInt32, puClassNameBufSize: POINTER(UInt32), pszClass: win32more.Foundation.PWSTR, pKeyList: POINTER(win32more.System.Wmi.IWbemPathKeyList_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetScopeAsText(uIndex: UInt32, puTextBufSize: POINTER(UInt32), pszText: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def RemoveScope(uIndex: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def RemoveAllScopes() -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def SetClassName(Name: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def GetClassName(puBuffLength: POINTER(UInt32), pszName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def GetKeyList(pOut: POINTER(win32more.System.Wmi.IWbemPathKeyList_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def CreateClassPart(lFlags: Int32, Name: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def DeleteClassPart(lFlags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def IsRelative(wszMachine: win32more.Foundation.PWSTR, wszNamespace: win32more.Foundation.PWSTR) -> win32more.Foundation.BOOL: ...
    @commethod(26)
    def IsRelativeOrChild(wszMachine: win32more.Foundation.PWSTR, wszNamespace: win32more.Foundation.PWSTR, lFlags: Int32) -> win32more.Foundation.BOOL: ...
    @commethod(27)
    def IsLocal(wszMachine: win32more.Foundation.PWSTR) -> win32more.Foundation.BOOL: ...
    @commethod(28)
    def IsSameClassName(wszClass: win32more.Foundation.PWSTR) -> win32more.Foundation.BOOL: ...
class IWbemPathKeyList(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9ae62877-7544-4bb0-aa-26-a1-38-24-65-9e-d6')
    @commethod(3)
    def GetCount(puKeyCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetKey(wszName: win32more.Foundation.PWSTR, uFlags: UInt32, uCimType: UInt32, pKeyVal: c_void_p) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetKey2(wszName: win32more.Foundation.PWSTR, uFlags: UInt32, uCimType: UInt32, pKeyVal: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetKey(uKeyIx: UInt32, uFlags: UInt32, puNameBufSize: POINTER(UInt32), pszKeyName: win32more.Foundation.PWSTR, puKeyValBufSize: POINTER(UInt32), pKeyVal: c_void_p, puApparentCimType: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetKey2(uKeyIx: UInt32, uFlags: UInt32, puNameBufSize: POINTER(UInt32), pszKeyName: win32more.Foundation.PWSTR, pKeyValue: POINTER(win32more.System.Com.VARIANT_head), puApparentCimType: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveKey(wszName: win32more.Foundation.PWSTR, uFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def RemoveAllKeys(uFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def MakeSingleton(bSet: Byte) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetInfo(uRequestedInfo: UInt32, puResponse: POINTER(UInt64)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetText(lFlags: Int32, puBuffLength: POINTER(UInt32), pszText: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
class IWbemPropertyProvider(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('ce61e841-65bc-11d0-b6-bd-00-aa-00-32-40-c7')
    @commethod(3)
    def GetProperty(lFlags: Int32, strLocale: win32more.Foundation.BSTR, strClassMapping: win32more.Foundation.BSTR, strInstMapping: win32more.Foundation.BSTR, strPropMapping: win32more.Foundation.BSTR, pvValue: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def PutProperty(lFlags: Int32, strLocale: win32more.Foundation.BSTR, strClassMapping: win32more.Foundation.BSTR, strInstMapping: win32more.Foundation.BSTR, strPropMapping: win32more.Foundation.BSTR, pvValue: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
class IWbemProviderIdentity(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('631f7d97-d993-11d2-b3-39-00-10-5a-1f-4a-af')
    @commethod(3)
    def SetRegistrationObject(lFlags: Int32, pProvReg: win32more.System.Wmi.IWbemClassObject_head) -> win32more.Foundation.HRESULT: ...
class IWbemProviderInit(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1be41572-91dd-11d1-ae-b2-00-c0-4f-b6-88-20')
    @commethod(3)
    def Initialize(wszUser: win32more.Foundation.PWSTR, lFlags: Int32, wszNamespace: win32more.Foundation.PWSTR, wszLocale: win32more.Foundation.PWSTR, pNamespace: win32more.System.Wmi.IWbemServices_head, pCtx: win32more.System.Wmi.IWbemContext_head, pInitSink: win32more.System.Wmi.IWbemProviderInitSink_head) -> win32more.Foundation.HRESULT: ...
class IWbemProviderInitSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1be41571-91dd-11d1-ae-b2-00-c0-4f-b6-88-20')
    @commethod(3)
    def SetStatus(lStatus: Int32, lFlags: Int32) -> win32more.Foundation.HRESULT: ...
class IWbemQualifierSet(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('dc12a680-737f-11cf-88-4d-00-aa-00-4b-2e-24')
    @commethod(3)
    def Get(wszName: win32more.Foundation.PWSTR, lFlags: Int32, pVal: POINTER(win32more.System.Com.VARIANT_head), plFlavor: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Put(wszName: win32more.Foundation.PWSTR, pVal: POINTER(win32more.System.Com.VARIANT_head), lFlavor: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def Delete(wszName: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetNames(lFlags: Int32, pNames: POINTER(POINTER(win32more.System.Com.SAFEARRAY_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def BeginEnumeration(lFlags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Next(lFlags: Int32, pstrName: POINTER(win32more.Foundation.BSTR), pVal: POINTER(win32more.System.Com.VARIANT_head), plFlavor: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def EndEnumeration() -> win32more.Foundation.HRESULT: ...
class IWbemQuery(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('81166f58-dd98-11d3-a1-20-00-10-5a-1f-51-5a')
    @commethod(3)
    def Empty() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetLanguageFeatures(uFlags: UInt32, uArraySize: UInt32, puFeatures: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def TestLanguageFeatures(uFlags: UInt32, uArraySize: POINTER(UInt32), puFeatures: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Parse(pszLang: win32more.Foundation.PWSTR, pszQuery: win32more.Foundation.PWSTR, uFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetAnalysis(uAnalysisType: UInt32, uFlags: UInt32, pAnalysis: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def FreeMemory(pMem: c_void_p) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetQueryInfo(uAnalysisType: UInt32, uInfoId: UInt32, uBufSize: UInt32, pDestBuf: c_void_p) -> win32more.Foundation.HRESULT: ...
class IWbemRefresher(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('49353c99-516b-11d1-ae-a6-00-c0-4f-b6-88-20')
    @commethod(3)
    def Refresh(lFlags: Int32) -> win32more.Foundation.HRESULT: ...
class IWbemServices(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('9556dc99-828c-11cf-a3-7e-00-aa-00-32-40-c7')
    @commethod(3)
    def OpenNamespace(strNamespace: win32more.Foundation.BSTR, lFlags: Int32, pCtx: win32more.System.Wmi.IWbemContext_head, ppWorkingNamespace: POINTER(win32more.System.Wmi.IWbemServices_head), ppResult: POINTER(win32more.System.Wmi.IWbemCallResult_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def CancelAsyncCall(pSink: win32more.System.Wmi.IWbemObjectSink_head) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def QueryObjectSink(lFlags: Int32, ppResponseHandler: POINTER(win32more.System.Wmi.IWbemObjectSink_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetObject(strObjectPath: win32more.Foundation.BSTR, lFlags: Int32, pCtx: win32more.System.Wmi.IWbemContext_head, ppObject: POINTER(win32more.System.Wmi.IWbemClassObject_head), ppCallResult: POINTER(win32more.System.Wmi.IWbemCallResult_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetObjectAsync(strObjectPath: win32more.Foundation.BSTR, lFlags: Int32, pCtx: win32more.System.Wmi.IWbemContext_head, pResponseHandler: win32more.System.Wmi.IWbemObjectSink_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def PutClass(pObject: win32more.System.Wmi.IWbemClassObject_head, lFlags: Int32, pCtx: win32more.System.Wmi.IWbemContext_head, ppCallResult: POINTER(win32more.System.Wmi.IWbemCallResult_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def PutClassAsync(pObject: win32more.System.Wmi.IWbemClassObject_head, lFlags: Int32, pCtx: win32more.System.Wmi.IWbemContext_head, pResponseHandler: win32more.System.Wmi.IWbemObjectSink_head) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def DeleteClass(strClass: win32more.Foundation.BSTR, lFlags: Int32, pCtx: win32more.System.Wmi.IWbemContext_head, ppCallResult: POINTER(win32more.System.Wmi.IWbemCallResult_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def DeleteClassAsync(strClass: win32more.Foundation.BSTR, lFlags: Int32, pCtx: win32more.System.Wmi.IWbemContext_head, pResponseHandler: win32more.System.Wmi.IWbemObjectSink_head) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def CreateClassEnum(strSuperclass: win32more.Foundation.BSTR, lFlags: Int32, pCtx: win32more.System.Wmi.IWbemContext_head, ppEnum: POINTER(win32more.System.Wmi.IEnumWbemClassObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def CreateClassEnumAsync(strSuperclass: win32more.Foundation.BSTR, lFlags: Int32, pCtx: win32more.System.Wmi.IWbemContext_head, pResponseHandler: win32more.System.Wmi.IWbemObjectSink_head) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def PutInstance(pInst: win32more.System.Wmi.IWbemClassObject_head, lFlags: Int32, pCtx: win32more.System.Wmi.IWbemContext_head, ppCallResult: POINTER(win32more.System.Wmi.IWbemCallResult_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def PutInstanceAsync(pInst: win32more.System.Wmi.IWbemClassObject_head, lFlags: Int32, pCtx: win32more.System.Wmi.IWbemContext_head, pResponseHandler: win32more.System.Wmi.IWbemObjectSink_head) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def DeleteInstance(strObjectPath: win32more.Foundation.BSTR, lFlags: Int32, pCtx: win32more.System.Wmi.IWbemContext_head, ppCallResult: POINTER(win32more.System.Wmi.IWbemCallResult_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def DeleteInstanceAsync(strObjectPath: win32more.Foundation.BSTR, lFlags: Int32, pCtx: win32more.System.Wmi.IWbemContext_head, pResponseHandler: win32more.System.Wmi.IWbemObjectSink_head) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def CreateInstanceEnum(strFilter: win32more.Foundation.BSTR, lFlags: Int32, pCtx: win32more.System.Wmi.IWbemContext_head, ppEnum: POINTER(win32more.System.Wmi.IEnumWbemClassObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def CreateInstanceEnumAsync(strFilter: win32more.Foundation.BSTR, lFlags: Int32, pCtx: win32more.System.Wmi.IWbemContext_head, pResponseHandler: win32more.System.Wmi.IWbemObjectSink_head) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def ExecQuery(strQueryLanguage: win32more.Foundation.BSTR, strQuery: win32more.Foundation.BSTR, lFlags: win32more.System.Wmi.WBEM_GENERIC_FLAG_TYPE, pCtx: win32more.System.Wmi.IWbemContext_head, ppEnum: POINTER(win32more.System.Wmi.IEnumWbemClassObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def ExecQueryAsync(strQueryLanguage: win32more.Foundation.BSTR, strQuery: win32more.Foundation.BSTR, lFlags: Int32, pCtx: win32more.System.Wmi.IWbemContext_head, pResponseHandler: win32more.System.Wmi.IWbemObjectSink_head) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def ExecNotificationQuery(strQueryLanguage: win32more.Foundation.BSTR, strQuery: win32more.Foundation.BSTR, lFlags: Int32, pCtx: win32more.System.Wmi.IWbemContext_head, ppEnum: POINTER(win32more.System.Wmi.IEnumWbemClassObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def ExecNotificationQueryAsync(strQueryLanguage: win32more.Foundation.BSTR, strQuery: win32more.Foundation.BSTR, lFlags: Int32, pCtx: win32more.System.Wmi.IWbemContext_head, pResponseHandler: win32more.System.Wmi.IWbemObjectSink_head) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def ExecMethod(strObjectPath: win32more.Foundation.BSTR, strMethodName: win32more.Foundation.BSTR, lFlags: Int32, pCtx: win32more.System.Wmi.IWbemContext_head, pInParams: win32more.System.Wmi.IWbemClassObject_head, ppOutParams: POINTER(win32more.System.Wmi.IWbemClassObject_head), ppCallResult: POINTER(win32more.System.Wmi.IWbemCallResult_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def ExecMethodAsync(strObjectPath: win32more.Foundation.BSTR, strMethodName: win32more.Foundation.BSTR, lFlags: Int32, pCtx: win32more.System.Wmi.IWbemContext_head, pInParams: win32more.System.Wmi.IWbemClassObject_head, pResponseHandler: win32more.System.Wmi.IWbemObjectSink_head) -> win32more.Foundation.HRESULT: ...
class IWbemShutdown(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('b7b31df9-d515-11d3-a1-1c-00-10-5a-1f-51-5a')
    @commethod(3)
    def Shutdown(uReason: Int32, uMaxMilliseconds: UInt32, pCtx: win32more.System.Wmi.IWbemContext_head) -> win32more.Foundation.HRESULT: ...
class IWbemStatusCodeText(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('eb87e1bc-3233-11d2-ae-c9-00-c0-4f-b6-88-20')
    @commethod(3)
    def GetErrorCodeText(hRes: win32more.Foundation.HRESULT, LocaleId: UInt32, lFlags: Int32, MessageText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetFacilityCodeText(hRes: win32more.Foundation.HRESULT, LocaleId: UInt32, lFlags: Int32, MessageText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
class IWbemTransport(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('553fe584-2156-11d0-b6-ae-00-aa-00-32-40-c7')
    @commethod(3)
    def Initialize() -> win32more.Foundation.HRESULT: ...
class IWbemUnboundObjectSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('e246107b-b06e-11d0-ad-61-00-c0-4f-d8-fd-ff')
    @commethod(3)
    def IndicateToConsumer(pLogicalConsumer: win32more.System.Wmi.IWbemClassObject_head, lNumObjects: Int32, apObjects: POINTER(win32more.System.Wmi.IWbemClassObject_head)) -> win32more.Foundation.HRESULT: ...
class IWbemUnsecuredApartment(c_void_p):
    extends: win32more.System.Wmi.IUnsecuredApartment
    Guid = Guid('31739d04-3471-4cf4-9a-7c-57-a4-4a-e7-19-56')
    @commethod(4)
    def CreateSinkStub(pSink: win32more.System.Wmi.IWbemObjectSink_head, dwFlags: UInt32, wszReserved: win32more.Foundation.PWSTR, ppStub: POINTER(win32more.System.Wmi.IWbemObjectSink_head)) -> win32more.Foundation.HRESULT: ...
class IWMIExtension(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('adc1f06e-5c7e-11d2-8b-74-00-10-4b-2a-fb-41')
    @commethod(7)
    def get_WMIObjectPath(strWMIObjectPath: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetWMIObject(objWMIObject: POINTER(win32more.System.Wmi.ISWbemObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetWMIServices(objWMIServices: POINTER(win32more.System.Wmi.ISWbemServices_head)) -> win32more.Foundation.HRESULT: ...
class MI_Application(Structure):
    reserved1: UInt64
    reserved2: IntPtr
    ft: POINTER(win32more.System.Wmi.MI_ApplicationFT_head)
class MI_ApplicationFT(Structure):
    Close: IntPtr
    NewSession: IntPtr
    NewHostedProvider: IntPtr
    NewInstance: IntPtr
    NewDestinationOptions: IntPtr
    NewOperationOptions: IntPtr
    NewSubscriptionDeliveryOptions: IntPtr
    NewSerializer: IntPtr
    NewDeserializer: IntPtr
    NewInstanceFromClass: IntPtr
    NewClass: IntPtr
class MI_Array(Structure):
    data: c_void_p
    size: UInt32
class MI_ArrayField(Structure):
    value: win32more.System.Wmi.MI_Array
    exists: Byte
    flags: Byte
class MI_BooleanA(Structure):
    data: c_char_p_no
    size: UInt32
class MI_BooleanAField(Structure):
    value: win32more.System.Wmi.MI_BooleanA
    exists: Byte
    flags: Byte
class MI_BooleanField(Structure):
    value: Byte
    exists: Byte
    flags: Byte
MI_CallbackMode = Int32
MI_CALLBACKMODE_REPORT: MI_CallbackMode = 0
MI_CALLBACKMODE_INQUIRE: MI_CallbackMode = 1
MI_CALLBACKMODE_IGNORE: MI_CallbackMode = 2
@winfunctype_pointer
def MI_CancelCallback(reason: win32more.System.Wmi.MI_CancellationReason, callbackData: c_void_p) -> Void: ...
MI_CancellationReason = Int32
MI_REASON_NONE: MI_CancellationReason = 0
MI_REASON_TIMEOUT: MI_CancellationReason = 1
MI_REASON_SHUTDOWN: MI_CancellationReason = 2
MI_REASON_SERVICESTOP: MI_CancellationReason = 3
class MI_Char16A(Structure):
    data: POINTER(UInt16)
    size: UInt32
class MI_Char16AField(Structure):
    value: win32more.System.Wmi.MI_Char16A
    exists: Byte
    flags: Byte
class MI_Char16Field(Structure):
    value: UInt16
    exists: Byte
    flags: Byte
class MI_Class(Structure):
    ft: POINTER(win32more.System.Wmi.MI_ClassFT_head)
    classDecl: POINTER(win32more.System.Wmi.MI_ClassDecl_head)
    namespaceName: POINTER(UInt16)
    serverName: POINTER(UInt16)
    reserved: IntPtr * 4
class MI_ClassDecl(Structure):
    flags: UInt32
    code: UInt32
    name: POINTER(UInt16)
    qualifiers: POINTER(POINTER(win32more.System.Wmi.MI_Qualifier_head))
    numQualifiers: UInt32
    properties: POINTER(POINTER(win32more.System.Wmi.MI_PropertyDecl_head))
    numProperties: UInt32
    size: UInt32
    superClass: POINTER(UInt16)
    superClassDecl: POINTER(win32more.System.Wmi.MI_ClassDecl_head)
    methods: POINTER(POINTER(win32more.System.Wmi.MI_MethodDecl_head))
    numMethods: UInt32
    schema: POINTER(win32more.System.Wmi.MI_SchemaDecl_head)
    providerFT: POINTER(win32more.System.Wmi.MI_ProviderFT_head)
    owningClass: POINTER(win32more.System.Wmi.MI_Class_head)
class MI_ClassFT(Structure):
    GetClassNameA: IntPtr
    GetNameSpace: IntPtr
    GetServerName: IntPtr
    GetElementCount: IntPtr
    GetElement: IntPtr
    GetElementAt: IntPtr
    GetClassQualifierSet: IntPtr
    GetMethodCount: IntPtr
    GetMethodAt: IntPtr
    GetMethod: IntPtr
    GetParentClassName: IntPtr
    GetParentClass: IntPtr
    Delete: IntPtr
    Clone: IntPtr
class MI_ClientFT_V1(Structure):
    applicationFT: POINTER(win32more.System.Wmi.MI_ApplicationFT_head)
    sessionFT: POINTER(win32more.System.Wmi.MI_SessionFT_head)
    operationFT: POINTER(win32more.System.Wmi.MI_OperationFT_head)
    hostedProviderFT: POINTER(win32more.System.Wmi.MI_HostedProviderFT_head)
    serializerFT: POINTER(win32more.System.Wmi.MI_SerializerFT_head)
    deserializerFT: POINTER(win32more.System.Wmi.MI_DeserializerFT_head)
    subscribeDeliveryOptionsFT: POINTER(win32more.System.Wmi.MI_SubscriptionDeliveryOptionsFT_head)
    destinationOptionsFT: POINTER(win32more.System.Wmi.MI_DestinationOptionsFT_head)
    operationOptionsFT: POINTER(win32more.System.Wmi.MI_OperationOptionsFT_head)
    utilitiesFT: POINTER(win32more.System.Wmi.MI_UtilitiesFT_head)
class MI_ConstBooleanA(Structure):
    data: c_char_p_no
    size: UInt32
class MI_ConstBooleanAField(Structure):
    value: win32more.System.Wmi.MI_ConstBooleanA
    exists: Byte
    flags: Byte
class MI_ConstBooleanField(Structure):
    value: Byte
    exists: Byte
    flags: Byte
class MI_ConstChar16A(Structure):
    data: POINTER(UInt16)
    size: UInt32
class MI_ConstChar16AField(Structure):
    value: win32more.System.Wmi.MI_ConstChar16A
    exists: Byte
    flags: Byte
class MI_ConstChar16Field(Structure):
    value: UInt16
    exists: Byte
    flags: Byte
class MI_ConstDatetimeA(Structure):
    data: POINTER(win32more.System.Wmi.MI_Datetime_head)
    size: UInt32
class MI_ConstDatetimeAField(Structure):
    value: win32more.System.Wmi.MI_ConstDatetimeA
    exists: Byte
    flags: Byte
class MI_ConstDatetimeField(Structure):
    value: win32more.System.Wmi.MI_Datetime
    exists: Byte
    flags: Byte
class MI_ConstInstanceA(Structure):
    data: POINTER(POINTER(win32more.System.Wmi.MI_Instance_head))
    size: UInt32
class MI_ConstInstanceAField(Structure):
    value: win32more.System.Wmi.MI_ConstInstanceA
    exists: Byte
    flags: Byte
class MI_ConstInstanceField(Structure):
    value: POINTER(win32more.System.Wmi.MI_Instance_head)
    exists: Byte
    flags: Byte
class MI_ConstReal32A(Structure):
    data: POINTER(Single)
    size: UInt32
class MI_ConstReal32AField(Structure):
    value: win32more.System.Wmi.MI_ConstReal32A
    exists: Byte
    flags: Byte
class MI_ConstReal32Field(Structure):
    value: Single
    exists: Byte
    flags: Byte
class MI_ConstReal64A(Structure):
    data: POINTER(Double)
    size: UInt32
class MI_ConstReal64AField(Structure):
    value: win32more.System.Wmi.MI_ConstReal64A
    exists: Byte
    flags: Byte
class MI_ConstReal64Field(Structure):
    value: Double
    exists: Byte
    flags: Byte
class MI_ConstReferenceA(Structure):
    data: POINTER(POINTER(win32more.System.Wmi.MI_Instance_head))
    size: UInt32
class MI_ConstReferenceAField(Structure):
    value: win32more.System.Wmi.MI_ConstReferenceA
    exists: Byte
    flags: Byte
class MI_ConstReferenceField(Structure):
    value: POINTER(win32more.System.Wmi.MI_Instance_head)
    exists: Byte
    flags: Byte
class MI_ConstSint16A(Structure):
    data: POINTER(Int16)
    size: UInt32
class MI_ConstSint16AField(Structure):
    value: win32more.System.Wmi.MI_ConstSint16A
    exists: Byte
    flags: Byte
class MI_ConstSint16Field(Structure):
    value: Int16
    exists: Byte
    flags: Byte
class MI_ConstSint32A(Structure):
    data: POINTER(Int32)
    size: UInt32
class MI_ConstSint32AField(Structure):
    value: win32more.System.Wmi.MI_ConstSint32A
    exists: Byte
    flags: Byte
class MI_ConstSint32Field(Structure):
    value: Int32
    exists: Byte
    flags: Byte
class MI_ConstSint64A(Structure):
    data: POINTER(Int64)
    size: UInt32
class MI_ConstSint64AField(Structure):
    value: win32more.System.Wmi.MI_ConstSint64A
    exists: Byte
    flags: Byte
class MI_ConstSint64Field(Structure):
    value: Int64
    exists: Byte
    flags: Byte
class MI_ConstSint8A(Structure):
    data: POINTER(SByte)
    size: UInt32
class MI_ConstSint8AField(Structure):
    value: win32more.System.Wmi.MI_ConstSint8A
    exists: Byte
    flags: Byte
class MI_ConstSint8Field(Structure):
    value: SByte
    exists: Byte
    flags: Byte
class MI_ConstStringA(Structure):
    data: POINTER(POINTER(UInt16))
    size: UInt32
class MI_ConstStringAField(Structure):
    value: win32more.System.Wmi.MI_ConstStringA
    exists: Byte
    flags: Byte
class MI_ConstStringField(Structure):
    value: POINTER(UInt16)
    exists: Byte
    flags: Byte
class MI_ConstUint16A(Structure):
    data: POINTER(UInt16)
    size: UInt32
class MI_ConstUint16AField(Structure):
    value: win32more.System.Wmi.MI_ConstUint16A
    exists: Byte
    flags: Byte
class MI_ConstUint16Field(Structure):
    value: UInt16
    exists: Byte
    flags: Byte
class MI_ConstUint32A(Structure):
    data: POINTER(UInt32)
    size: UInt32
class MI_ConstUint32AField(Structure):
    value: win32more.System.Wmi.MI_ConstUint32A
    exists: Byte
    flags: Byte
class MI_ConstUint32Field(Structure):
    value: UInt32
    exists: Byte
    flags: Byte
class MI_ConstUint64A(Structure):
    data: POINTER(UInt64)
    size: UInt32
class MI_ConstUint64AField(Structure):
    value: win32more.System.Wmi.MI_ConstUint64A
    exists: Byte
    flags: Byte
class MI_ConstUint64Field(Structure):
    value: UInt64
    exists: Byte
    flags: Byte
class MI_ConstUint8A(Structure):
    data: c_char_p_no
    size: UInt32
class MI_ConstUint8AField(Structure):
    value: win32more.System.Wmi.MI_ConstUint8A
    exists: Byte
    flags: Byte
class MI_ConstUint8Field(Structure):
    value: Byte
    exists: Byte
    flags: Byte
class MI_Context(Structure):
    ft: POINTER(win32more.System.Wmi.MI_ContextFT_head)
    reserved: IntPtr * 3
class MI_ContextFT(Structure):
    PostResult: IntPtr
    PostInstance: IntPtr
    PostIndication: IntPtr
    ConstructInstance: IntPtr
    ConstructParameters: IntPtr
    NewInstance: IntPtr
    NewDynamicInstance: IntPtr
    NewParameters: IntPtr
    Canceled: IntPtr
    GetLocale: IntPtr
    RegisterCancel: IntPtr
    RequestUnload: IntPtr
    RefuseUnload: IntPtr
    GetLocalSession: IntPtr
    SetStringOption: IntPtr
    GetStringOption: IntPtr
    GetNumberOption: IntPtr
    GetCustomOption: IntPtr
    GetCustomOptionCount: IntPtr
    GetCustomOptionAt: IntPtr
    WriteMessage: IntPtr
    WriteProgress: IntPtr
    WriteStreamParameter: IntPtr
    WriteCimError: IntPtr
    PromptUser: IntPtr
    ShouldProcess: IntPtr
    ShouldContinue: IntPtr
    PostError: IntPtr
    PostCimError: IntPtr
    WriteError: IntPtr
class MI_Datetime(Structure):
    isTimestamp: UInt32
    u: _u_e__Union
    class _u_e__Union(Union):
        timestamp: win32more.System.Wmi.MI_Timestamp
        interval: win32more.System.Wmi.MI_Interval
class MI_DatetimeA(Structure):
    data: POINTER(win32more.System.Wmi.MI_Datetime_head)
    size: UInt32
class MI_DatetimeAField(Structure):
    value: win32more.System.Wmi.MI_DatetimeA
    exists: Byte
    flags: Byte
class MI_DatetimeField(Structure):
    value: win32more.System.Wmi.MI_Datetime
    exists: Byte
    flags: Byte
class MI_Deserializer(Structure):
    reserved1: UInt64
    reserved2: IntPtr
@winfunctype_pointer
def MI_Deserializer_ClassObjectNeeded(context: c_void_p, serverName: POINTER(UInt16), namespaceName: POINTER(UInt16), className: POINTER(UInt16), requestedClassObject: POINTER(POINTER(win32more.System.Wmi.MI_Class_head))) -> win32more.System.Wmi.MI_Result: ...
class MI_DeserializerFT(Structure):
    Close: IntPtr
    DeserializeClass: IntPtr
    Class_GetClassName: IntPtr
    Class_GetParentClassName: IntPtr
    DeserializeInstance: IntPtr
    Instance_GetClassName: IntPtr
class MI_DestinationOptions(Structure):
    reserved1: UInt64
    reserved2: IntPtr
    ft: POINTER(win32more.System.Wmi.MI_DestinationOptionsFT_head)
MI_DestinationOptions_ImpersonationType = Int32
MI_DestinationOptions_ImpersonationType_Default: MI_DestinationOptions_ImpersonationType = 0
MI_DestinationOptions_ImpersonationType_None: MI_DestinationOptions_ImpersonationType = 1
MI_DestinationOptions_ImpersonationType_Identify: MI_DestinationOptions_ImpersonationType = 2
MI_DestinationOptions_ImpersonationType_Impersonate: MI_DestinationOptions_ImpersonationType = 3
MI_DestinationOptions_ImpersonationType_Delegate: MI_DestinationOptions_ImpersonationType = 4
class MI_DestinationOptionsFT(Structure):
    Delete: IntPtr
    SetString: IntPtr
    SetNumber: IntPtr
    AddCredentials: IntPtr
    GetString: IntPtr
    GetNumber: IntPtr
    GetOptionCount: IntPtr
    GetOptionAt: IntPtr
    GetOption: IntPtr
    GetCredentialsCount: IntPtr
    GetCredentialsAt: IntPtr
    GetCredentialsPasswordAt: IntPtr
    Clone: IntPtr
    SetInterval: IntPtr
    GetInterval: IntPtr
MI_ErrorCategory = Int32
MI_ERRORCATEGORY_NOT_SPECIFIED: MI_ErrorCategory = 0
MI_ERRORCATEGORY_OPEN_ERROR: MI_ErrorCategory = 1
MI_ERRORCATEGORY_CLOS_EERROR: MI_ErrorCategory = 2
MI_ERRORCATEGORY_DEVICE_ERROR: MI_ErrorCategory = 3
MI_ERRORCATEGORY_DEADLOCK_DETECTED: MI_ErrorCategory = 4
MI_ERRORCATEGORY_INVALID_ARGUMENT: MI_ErrorCategory = 5
MI_ERRORCATEGORY_INVALID_DATA: MI_ErrorCategory = 6
MI_ERRORCATEGORY_INVALID_OPERATION: MI_ErrorCategory = 7
MI_ERRORCATEGORY_INVALID_RESULT: MI_ErrorCategory = 8
MI_ERRORCATEGORY_INVALID_TYPE: MI_ErrorCategory = 9
MI_ERRORCATEGORY_METADATA_ERROR: MI_ErrorCategory = 10
MI_ERRORCATEGORY_NOT_IMPLEMENTED: MI_ErrorCategory = 11
MI_ERRORCATEGORY_NOT_INSTALLED: MI_ErrorCategory = 12
MI_ERRORCATEGORY_OBJECT_NOT_FOUND: MI_ErrorCategory = 13
MI_ERRORCATEGORY_OPERATION_STOPPED: MI_ErrorCategory = 14
MI_ERRORCATEGORY_OPERATION_TIMEOUT: MI_ErrorCategory = 15
MI_ERRORCATEGORY_SYNTAX_ERROR: MI_ErrorCategory = 16
MI_ERRORCATEGORY_PARSER_ERROR: MI_ErrorCategory = 17
MI_ERRORCATEGORY_ACCESS_DENIED: MI_ErrorCategory = 18
MI_ERRORCATEGORY_RESOURCE_BUSY: MI_ErrorCategory = 19
MI_ERRORCATEGORY_RESOURCE_EXISTS: MI_ErrorCategory = 20
MI_ERRORCATEGORY_RESOURCE_UNAVAILABLE: MI_ErrorCategory = 21
MI_ERRORCATEGORY_READ_ERROR: MI_ErrorCategory = 22
MI_ERRORCATEGORY_WRITE_ERROR: MI_ErrorCategory = 23
MI_ERRORCATEGORY_FROM_STDERR: MI_ErrorCategory = 24
MI_ERRORCATEGORY_SECURITY_ERROR: MI_ErrorCategory = 25
MI_ERRORCATEGORY_PROTOCOL_ERROR: MI_ErrorCategory = 26
MI_ERRORCATEGORY_CONNECTION_ERROR: MI_ErrorCategory = 27
MI_ERRORCATEGORY_AUTHENTICATION_ERROR: MI_ErrorCategory = 28
MI_ERRORCATEGORY_LIMITS_EXCEEDED: MI_ErrorCategory = 29
MI_ERRORCATEGORY_QUOTA_EXCEEDED: MI_ErrorCategory = 30
MI_ERRORCATEGORY_NOT_ENABLED: MI_ErrorCategory = 31
class MI_FeatureDecl(Structure):
    flags: UInt32
    code: UInt32
    name: POINTER(UInt16)
    qualifiers: POINTER(POINTER(win32more.System.Wmi.MI_Qualifier_head))
    numQualifiers: UInt32
class MI_Filter(Structure):
    ft: POINTER(win32more.System.Wmi.MI_FilterFT_head)
    reserved: IntPtr * 3
class MI_FilterFT(Structure):
    Evaluate: IntPtr
    GetExpression: IntPtr
class MI_HostedProvider(Structure):
    reserved1: UInt64
    reserved2: IntPtr
    ft: POINTER(win32more.System.Wmi.MI_HostedProviderFT_head)
class MI_HostedProviderFT(Structure):
    Close: IntPtr
    GetApplication: IntPtr
class MI_Instance(Structure):
    ft: POINTER(win32more.System.Wmi.MI_InstanceFT_head)
    classDecl: POINTER(win32more.System.Wmi.MI_ClassDecl_head)
    serverName: POINTER(UInt16)
    nameSpace: POINTER(UInt16)
    reserved: IntPtr * 4
class MI_InstanceA(Structure):
    data: POINTER(POINTER(win32more.System.Wmi.MI_Instance_head))
    size: UInt32
class MI_InstanceAField(Structure):
    value: win32more.System.Wmi.MI_InstanceA
    exists: Byte
    flags: Byte
class MI_InstanceExFT(Structure):
    parent: win32more.System.Wmi.MI_InstanceFT
    Normalize: IntPtr
class MI_InstanceField(Structure):
    value: POINTER(win32more.System.Wmi.MI_Instance_head)
    exists: Byte
    flags: Byte
class MI_InstanceFT(Structure):
    Clone: IntPtr
    Destruct: IntPtr
    Delete: IntPtr
    IsA: IntPtr
    GetClassNameA: IntPtr
    SetNameSpace: IntPtr
    GetNameSpace: IntPtr
    GetElementCount: IntPtr
    AddElement: IntPtr
    SetElement: IntPtr
    SetElementAt: IntPtr
    GetElement: IntPtr
    GetElementAt: IntPtr
    ClearElement: IntPtr
    ClearElementAt: IntPtr
    GetServerName: IntPtr
    SetServerName: IntPtr
    GetClass: IntPtr
class MI_Interval(Structure):
    days: UInt32
    hours: UInt32
    minutes: UInt32
    seconds: UInt32
    microseconds: UInt32
    __padding1: UInt32
    __padding2: UInt32
    __padding3: UInt32
MI_LocaleType = Int32
MI_LOCALE_TYPE_REQUESTED_UI: MI_LocaleType = 0
MI_LOCALE_TYPE_REQUESTED_DATA: MI_LocaleType = 1
MI_LOCALE_TYPE_CLOSEST_UI: MI_LocaleType = 2
MI_LOCALE_TYPE_CLOSEST_DATA: MI_LocaleType = 3
@cfunctype_pointer
def MI_MainFunction(server: POINTER(win32more.System.Wmi.MI_Server_head)) -> POINTER(win32more.System.Wmi.MI_Module_head): ...
class MI_MethodDecl(Structure):
    flags: UInt32
    code: UInt32
    name: POINTER(UInt16)
    qualifiers: POINTER(POINTER(win32more.System.Wmi.MI_Qualifier_head))
    numQualifiers: UInt32
    parameters: POINTER(POINTER(win32more.System.Wmi.MI_ParameterDecl_head))
    numParameters: UInt32
    size: UInt32
    returnType: UInt32
    origin: POINTER(UInt16)
    propagator: POINTER(UInt16)
    schema: POINTER(win32more.System.Wmi.MI_SchemaDecl_head)
    function: win32more.System.Wmi.MI_MethodDecl_Invoke
@winfunctype_pointer
def MI_MethodDecl_Invoke(self: c_void_p, context: POINTER(win32more.System.Wmi.MI_Context_head), nameSpace: POINTER(UInt16), className: POINTER(UInt16), methodName: POINTER(UInt16), instanceName: POINTER(win32more.System.Wmi.MI_Instance_head), parameters: POINTER(win32more.System.Wmi.MI_Instance_head)) -> Void: ...
class MI_Module(Structure):
    version: UInt32
    generatorVersion: UInt32
    flags: UInt32
    charSize: UInt32
    schemaDecl: POINTER(win32more.System.Wmi.MI_SchemaDecl_head)
    Load: win32more.System.Wmi.MI_Module_Load
    Unload: win32more.System.Wmi.MI_Module_Unload
    dynamicProviderFT: POINTER(win32more.System.Wmi.MI_ProviderFT_head)
@winfunctype_pointer
def MI_Module_Load(self: POINTER(POINTER(win32more.System.Wmi.MI_Module_Self_head)), context: POINTER(win32more.System.Wmi.MI_Context_head)) -> Void: ...
class MI_Module_Self(Structure):
    pass
@winfunctype_pointer
def MI_Module_Unload(self: POINTER(win32more.System.Wmi.MI_Module_Self_head), context: POINTER(win32more.System.Wmi.MI_Context_head)) -> Void: ...
class MI_ObjectDecl(Structure):
    flags: UInt32
    code: UInt32
    name: POINTER(UInt16)
    qualifiers: POINTER(POINTER(win32more.System.Wmi.MI_Qualifier_head))
    numQualifiers: UInt32
    properties: POINTER(POINTER(win32more.System.Wmi.MI_PropertyDecl_head))
    numProperties: UInt32
    size: UInt32
class MI_Operation(Structure):
    reserved1: UInt64
    reserved2: IntPtr
    ft: POINTER(win32more.System.Wmi.MI_OperationFT_head)
@winfunctype_pointer
def MI_OperationCallback_Class(operation: POINTER(win32more.System.Wmi.MI_Operation_head), callbackContext: c_void_p, classResult: POINTER(win32more.System.Wmi.MI_Class_head), moreResults: Byte, resultCode: win32more.System.Wmi.MI_Result, errorString: POINTER(UInt16), errorDetails: POINTER(win32more.System.Wmi.MI_Instance_head), resultAcknowledgement: IntPtr) -> Void: ...
@winfunctype_pointer
def MI_OperationCallback_Indication(operation: POINTER(win32more.System.Wmi.MI_Operation_head), callbackContext: c_void_p, instance: POINTER(win32more.System.Wmi.MI_Instance_head), bookmark: POINTER(UInt16), machineID: POINTER(UInt16), moreResults: Byte, resultCode: win32more.System.Wmi.MI_Result, errorString: POINTER(UInt16), errorDetails: POINTER(win32more.System.Wmi.MI_Instance_head), resultAcknowledgement: IntPtr) -> Void: ...
@winfunctype_pointer
def MI_OperationCallback_Instance(operation: POINTER(win32more.System.Wmi.MI_Operation_head), callbackContext: c_void_p, instance: POINTER(win32more.System.Wmi.MI_Instance_head), moreResults: Byte, resultCode: win32more.System.Wmi.MI_Result, errorString: POINTER(UInt16), errorDetails: POINTER(win32more.System.Wmi.MI_Instance_head), resultAcknowledgement: IntPtr) -> Void: ...
@winfunctype_pointer
def MI_OperationCallback_PromptUser(operation: POINTER(win32more.System.Wmi.MI_Operation_head), callbackContext: c_void_p, message: POINTER(UInt16), promptType: win32more.System.Wmi.MI_PromptType, promptUserResult: IntPtr) -> Void: ...
MI_OperationCallback_ResponseType = Int32
MI_OperationCallback_ResponseType_No: MI_OperationCallback_ResponseType = 0
MI_OperationCallback_ResponseType_Yes: MI_OperationCallback_ResponseType = 1
MI_OperationCallback_ResponseType_NoToAll: MI_OperationCallback_ResponseType = 2
MI_OperationCallback_ResponseType_YesToAll: MI_OperationCallback_ResponseType = 3
@winfunctype_pointer
def MI_OperationCallback_StreamedParameter(operation: POINTER(win32more.System.Wmi.MI_Operation_head), callbackContext: c_void_p, parameterName: POINTER(UInt16), resultType: win32more.System.Wmi.MI_Type, result: POINTER(win32more.System.Wmi.MI_Value_head), resultAcknowledgement: IntPtr) -> Void: ...
@winfunctype_pointer
def MI_OperationCallback_WriteError(operation: POINTER(win32more.System.Wmi.MI_Operation_head), callbackContext: c_void_p, instance: POINTER(win32more.System.Wmi.MI_Instance_head), writeErrorResult: IntPtr) -> Void: ...
@winfunctype_pointer
def MI_OperationCallback_WriteMessage(operation: POINTER(win32more.System.Wmi.MI_Operation_head), callbackContext: c_void_p, channel: UInt32, message: POINTER(UInt16)) -> Void: ...
@winfunctype_pointer
def MI_OperationCallback_WriteProgress(operation: POINTER(win32more.System.Wmi.MI_Operation_head), callbackContext: c_void_p, activity: POINTER(UInt16), currentOperation: POINTER(UInt16), statusDescription: POINTER(UInt16), percentageComplete: UInt32, secondsRemaining: UInt32) -> Void: ...
class MI_OperationCallbacks(Structure):
    callbackContext: c_void_p
    promptUser: win32more.System.Wmi.MI_OperationCallback_PromptUser
    writeError: win32more.System.Wmi.MI_OperationCallback_WriteError
    writeMessage: win32more.System.Wmi.MI_OperationCallback_WriteMessage
    writeProgress: win32more.System.Wmi.MI_OperationCallback_WriteProgress
    instanceResult: win32more.System.Wmi.MI_OperationCallback_Instance
    indicationResult: win32more.System.Wmi.MI_OperationCallback_Indication
    classResult: win32more.System.Wmi.MI_OperationCallback_Class
    streamedParameterResult: win32more.System.Wmi.MI_OperationCallback_StreamedParameter
class MI_OperationFT(Structure):
    Close: IntPtr
    Cancel: IntPtr
    GetSession: IntPtr
    GetInstance: IntPtr
    GetIndication: IntPtr
    GetClass: IntPtr
class MI_OperationOptions(Structure):
    reserved1: UInt64
    reserved2: IntPtr
    ft: POINTER(win32more.System.Wmi.MI_OperationOptionsFT_head)
class MI_OperationOptionsFT(Structure):
    Delete: IntPtr
    SetString: IntPtr
    SetNumber: IntPtr
    SetCustomOption: IntPtr
    GetString: IntPtr
    GetNumber: IntPtr
    GetOptionCount: IntPtr
    GetOptionAt: IntPtr
    GetOption: IntPtr
    GetEnabledChannels: IntPtr
    Clone: IntPtr
    SetInterval: IntPtr
    GetInterval: IntPtr
class MI_ParameterDecl(Structure):
    flags: UInt32
    code: UInt32
    name: POINTER(UInt16)
    qualifiers: POINTER(POINTER(win32more.System.Wmi.MI_Qualifier_head))
    numQualifiers: UInt32
    type: UInt32
    className: POINTER(UInt16)
    subscript: UInt32
    offset: UInt32
class MI_ParameterSet(Structure):
    reserved1: UInt64
    reserved2: IntPtr
    ft: POINTER(win32more.System.Wmi.MI_ParameterSetFT_head)
class MI_ParameterSetFT(Structure):
    GetMethodReturnType: IntPtr
    GetParameterCount: IntPtr
    GetParameterAt: IntPtr
    GetParameter: IntPtr
MI_PromptType = Int32
MI_PROMPTTYPE_NORMAL: MI_PromptType = 0
MI_PROMPTTYPE_CRITICAL: MI_PromptType = 1
class MI_PropertyDecl(Structure):
    flags: UInt32
    code: UInt32
    name: POINTER(UInt16)
    qualifiers: POINTER(POINTER(win32more.System.Wmi.MI_Qualifier_head))
    numQualifiers: UInt32
    type: UInt32
    className: POINTER(UInt16)
    subscript: UInt32
    offset: UInt32
    origin: POINTER(UInt16)
    propagator: POINTER(UInt16)
    value: c_void_p
class MI_PropertySet(Structure):
    ft: POINTER(win32more.System.Wmi.MI_PropertySetFT_head)
    reserved: IntPtr * 3
class MI_PropertySetFT(Structure):
    GetElementCount: IntPtr
    ContainsElement: IntPtr
    AddElement: IntPtr
    GetElementAt: IntPtr
    Clear: IntPtr
    Destruct: IntPtr
    Delete: IntPtr
    Clone: IntPtr
MI_ProviderArchitecture = Int32
MI_PROVIDER_ARCHITECTURE_32BIT: MI_ProviderArchitecture = 0
MI_PROVIDER_ARCHITECTURE_64BIT: MI_ProviderArchitecture = 1
class MI_ProviderFT(Structure):
    Load: win32more.System.Wmi.MI_ProviderFT_Load
    Unload: win32more.System.Wmi.MI_ProviderFT_Unload
    GetInstance: win32more.System.Wmi.MI_ProviderFT_GetInstance
    EnumerateInstances: win32more.System.Wmi.MI_ProviderFT_EnumerateInstances
    CreateInstance: win32more.System.Wmi.MI_ProviderFT_CreateInstance
    ModifyInstance: win32more.System.Wmi.MI_ProviderFT_ModifyInstance
    DeleteInstance: win32more.System.Wmi.MI_ProviderFT_DeleteInstance
    AssociatorInstances: win32more.System.Wmi.MI_ProviderFT_AssociatorInstances
    ReferenceInstances: win32more.System.Wmi.MI_ProviderFT_ReferenceInstances
    EnableIndications: win32more.System.Wmi.MI_ProviderFT_EnableIndications
    DisableIndications: win32more.System.Wmi.MI_ProviderFT_DisableIndications
    Subscribe: win32more.System.Wmi.MI_ProviderFT_Subscribe
    Unsubscribe: win32more.System.Wmi.MI_ProviderFT_Unsubscribe
    Invoke: win32more.System.Wmi.MI_ProviderFT_Invoke
@winfunctype_pointer
def MI_ProviderFT_AssociatorInstances(self: c_void_p, context: POINTER(win32more.System.Wmi.MI_Context_head), nameSpace: POINTER(UInt16), className: POINTER(UInt16), instanceName: POINTER(win32more.System.Wmi.MI_Instance_head), resultClass: POINTER(UInt16), role: POINTER(UInt16), resultRole: POINTER(UInt16), propertySet: POINTER(win32more.System.Wmi.MI_PropertySet_head), keysOnly: Byte, filter: POINTER(win32more.System.Wmi.MI_Filter_head)) -> Void: ...
@winfunctype_pointer
def MI_ProviderFT_CreateInstance(self: c_void_p, context: POINTER(win32more.System.Wmi.MI_Context_head), nameSpace: POINTER(UInt16), className: POINTER(UInt16), newInstance: POINTER(win32more.System.Wmi.MI_Instance_head)) -> Void: ...
@winfunctype_pointer
def MI_ProviderFT_DeleteInstance(self: c_void_p, context: POINTER(win32more.System.Wmi.MI_Context_head), nameSpace: POINTER(UInt16), className: POINTER(UInt16), instanceName: POINTER(win32more.System.Wmi.MI_Instance_head)) -> Void: ...
@winfunctype_pointer
def MI_ProviderFT_DisableIndications(self: c_void_p, indicationsContext: POINTER(win32more.System.Wmi.MI_Context_head), nameSpace: POINTER(UInt16), className: POINTER(UInt16)) -> Void: ...
@winfunctype_pointer
def MI_ProviderFT_EnableIndications(self: c_void_p, indicationsContext: POINTER(win32more.System.Wmi.MI_Context_head), nameSpace: POINTER(UInt16), className: POINTER(UInt16)) -> Void: ...
@winfunctype_pointer
def MI_ProviderFT_EnumerateInstances(self: c_void_p, context: POINTER(win32more.System.Wmi.MI_Context_head), nameSpace: POINTER(UInt16), className: POINTER(UInt16), propertySet: POINTER(win32more.System.Wmi.MI_PropertySet_head), keysOnly: Byte, filter: POINTER(win32more.System.Wmi.MI_Filter_head)) -> Void: ...
@winfunctype_pointer
def MI_ProviderFT_GetInstance(self: c_void_p, context: POINTER(win32more.System.Wmi.MI_Context_head), nameSpace: POINTER(UInt16), className: POINTER(UInt16), instanceName: POINTER(win32more.System.Wmi.MI_Instance_head), propertySet: POINTER(win32more.System.Wmi.MI_PropertySet_head)) -> Void: ...
@winfunctype_pointer
def MI_ProviderFT_Invoke(self: c_void_p, context: POINTER(win32more.System.Wmi.MI_Context_head), nameSpace: POINTER(UInt16), className: POINTER(UInt16), methodName: POINTER(UInt16), instanceName: POINTER(win32more.System.Wmi.MI_Instance_head), inputParameters: POINTER(win32more.System.Wmi.MI_Instance_head)) -> Void: ...
@winfunctype_pointer
def MI_ProviderFT_Load(self: POINTER(c_void_p), selfModule: POINTER(win32more.System.Wmi.MI_Module_Self_head), context: POINTER(win32more.System.Wmi.MI_Context_head)) -> Void: ...
@winfunctype_pointer
def MI_ProviderFT_ModifyInstance(self: c_void_p, context: POINTER(win32more.System.Wmi.MI_Context_head), nameSpace: POINTER(UInt16), className: POINTER(UInt16), modifiedInstance: POINTER(win32more.System.Wmi.MI_Instance_head), propertySet: POINTER(win32more.System.Wmi.MI_PropertySet_head)) -> Void: ...
@winfunctype_pointer
def MI_ProviderFT_ReferenceInstances(self: c_void_p, context: POINTER(win32more.System.Wmi.MI_Context_head), nameSpace: POINTER(UInt16), className: POINTER(UInt16), instanceName: POINTER(win32more.System.Wmi.MI_Instance_head), role: POINTER(UInt16), propertySet: POINTER(win32more.System.Wmi.MI_PropertySet_head), keysOnly: Byte, filter: POINTER(win32more.System.Wmi.MI_Filter_head)) -> Void: ...
@winfunctype_pointer
def MI_ProviderFT_Subscribe(self: c_void_p, context: POINTER(win32more.System.Wmi.MI_Context_head), nameSpace: POINTER(UInt16), className: POINTER(UInt16), filter: POINTER(win32more.System.Wmi.MI_Filter_head), bookmark: POINTER(UInt16), subscriptionID: UInt64, subscriptionSelf: POINTER(c_void_p)) -> Void: ...
@winfunctype_pointer
def MI_ProviderFT_Unload(self: c_void_p, context: POINTER(win32more.System.Wmi.MI_Context_head)) -> Void: ...
@winfunctype_pointer
def MI_ProviderFT_Unsubscribe(self: c_void_p, context: POINTER(win32more.System.Wmi.MI_Context_head), nameSpace: POINTER(UInt16), className: POINTER(UInt16), subscriptionID: UInt64, subscriptionSelf: c_void_p) -> Void: ...
class MI_Qualifier(Structure):
    name: POINTER(UInt16)
    type: UInt32
    flavor: UInt32
    value: c_void_p
class MI_QualifierDecl(Structure):
    name: POINTER(UInt16)
    type: UInt32
    scope: UInt32
    flavor: UInt32
    subscript: UInt32
    value: c_void_p
class MI_QualifierSet(Structure):
    reserved1: UInt64
    reserved2: IntPtr
    ft: POINTER(win32more.System.Wmi.MI_QualifierSetFT_head)
class MI_QualifierSetFT(Structure):
    GetQualifierCount: IntPtr
    GetQualifierAt: IntPtr
    GetQualifier: IntPtr
class MI_Real32A(Structure):
    data: POINTER(Single)
    size: UInt32
class MI_Real32AField(Structure):
    value: win32more.System.Wmi.MI_Real32A
    exists: Byte
    flags: Byte
class MI_Real32Field(Structure):
    value: Single
    exists: Byte
    flags: Byte
class MI_Real64A(Structure):
    data: POINTER(Double)
    size: UInt32
class MI_Real64AField(Structure):
    value: win32more.System.Wmi.MI_Real64A
    exists: Byte
    flags: Byte
class MI_Real64Field(Structure):
    value: Double
    exists: Byte
    flags: Byte
class MI_ReferenceA(Structure):
    data: POINTER(POINTER(win32more.System.Wmi.MI_Instance_head))
    size: UInt32
class MI_ReferenceAField(Structure):
    value: win32more.System.Wmi.MI_ReferenceA
    exists: Byte
    flags: Byte
class MI_ReferenceField(Structure):
    value: POINTER(win32more.System.Wmi.MI_Instance_head)
    exists: Byte
    flags: Byte
MI_Result = Int32
MI_RESULT_OK: MI_Result = 0
MI_RESULT_FAILED: MI_Result = 1
MI_RESULT_ACCESS_DENIED: MI_Result = 2
MI_RESULT_INVALID_NAMESPACE: MI_Result = 3
MI_RESULT_INVALID_PARAMETER: MI_Result = 4
MI_RESULT_INVALID_CLASS: MI_Result = 5
MI_RESULT_NOT_FOUND: MI_Result = 6
MI_RESULT_NOT_SUPPORTED: MI_Result = 7
MI_RESULT_CLASS_HAS_CHILDREN: MI_Result = 8
MI_RESULT_CLASS_HAS_INSTANCES: MI_Result = 9
MI_RESULT_INVALID_SUPERCLASS: MI_Result = 10
MI_RESULT_ALREADY_EXISTS: MI_Result = 11
MI_RESULT_NO_SUCH_PROPERTY: MI_Result = 12
MI_RESULT_TYPE_MISMATCH: MI_Result = 13
MI_RESULT_QUERY_LANGUAGE_NOT_SUPPORTED: MI_Result = 14
MI_RESULT_INVALID_QUERY: MI_Result = 15
MI_RESULT_METHOD_NOT_AVAILABLE: MI_Result = 16
MI_RESULT_METHOD_NOT_FOUND: MI_Result = 17
MI_RESULT_NAMESPACE_NOT_EMPTY: MI_Result = 20
MI_RESULT_INVALID_ENUMERATION_CONTEXT: MI_Result = 21
MI_RESULT_INVALID_OPERATION_TIMEOUT: MI_Result = 22
MI_RESULT_PULL_HAS_BEEN_ABANDONED: MI_Result = 23
MI_RESULT_PULL_CANNOT_BE_ABANDONED: MI_Result = 24
MI_RESULT_FILTERED_ENUMERATION_NOT_SUPPORTED: MI_Result = 25
MI_RESULT_CONTINUATION_ON_ERROR_NOT_SUPPORTED: MI_Result = 26
MI_RESULT_SERVER_LIMITS_EXCEEDED: MI_Result = 27
MI_RESULT_SERVER_IS_SHUTTING_DOWN: MI_Result = 28
class MI_SchemaDecl(Structure):
    qualifierDecls: POINTER(POINTER(win32more.System.Wmi.MI_QualifierDecl_head))
    numQualifierDecls: UInt32
    classDecls: POINTER(POINTER(win32more.System.Wmi.MI_ClassDecl_head))
    numClassDecls: UInt32
class MI_Serializer(Structure):
    reserved1: UInt64
    reserved2: IntPtr
class MI_SerializerFT(Structure):
    Close: IntPtr
    SerializeClass: IntPtr
    SerializeInstance: IntPtr
class MI_Server(Structure):
    serverFT: POINTER(win32more.System.Wmi.MI_ServerFT_head)
    contextFT: POINTER(win32more.System.Wmi.MI_ContextFT_head)
    instanceFT: POINTER(win32more.System.Wmi.MI_InstanceFT_head)
    propertySetFT: POINTER(win32more.System.Wmi.MI_PropertySetFT_head)
    filterFT: POINTER(win32more.System.Wmi.MI_FilterFT_head)
class MI_ServerFT(Structure):
    GetVersion: IntPtr
    GetSystemName: IntPtr
class MI_Session(Structure):
    reserved1: UInt64
    reserved2: IntPtr
    ft: POINTER(win32more.System.Wmi.MI_SessionFT_head)
class MI_SessionCallbacks(Structure):
    callbackContext: c_void_p
    writeMessage: IntPtr
    writeError: IntPtr
class MI_SessionFT(Structure):
    Close: IntPtr
    GetApplication: IntPtr
    GetInstance: IntPtr
    ModifyInstance: IntPtr
    CreateInstance: IntPtr
    DeleteInstance: IntPtr
    Invoke: IntPtr
    EnumerateInstances: IntPtr
    QueryInstances: IntPtr
    AssociatorInstances: IntPtr
    ReferenceInstances: IntPtr
    Subscribe: IntPtr
    GetClass: IntPtr
    EnumerateClasses: IntPtr
    TestConnection: IntPtr
class MI_Sint16A(Structure):
    data: POINTER(Int16)
    size: UInt32
class MI_Sint16AField(Structure):
    value: win32more.System.Wmi.MI_Sint16A
    exists: Byte
    flags: Byte
class MI_Sint16Field(Structure):
    value: Int16
    exists: Byte
    flags: Byte
class MI_Sint32A(Structure):
    data: POINTER(Int32)
    size: UInt32
class MI_Sint32AField(Structure):
    value: win32more.System.Wmi.MI_Sint32A
    exists: Byte
    flags: Byte
class MI_Sint32Field(Structure):
    value: Int32
    exists: Byte
    flags: Byte
class MI_Sint64A(Structure):
    data: POINTER(Int64)
    size: UInt32
class MI_Sint64AField(Structure):
    value: win32more.System.Wmi.MI_Sint64A
    exists: Byte
    flags: Byte
class MI_Sint64Field(Structure):
    value: Int64
    exists: Byte
    flags: Byte
class MI_Sint8A(Structure):
    data: POINTER(SByte)
    size: UInt32
class MI_Sint8AField(Structure):
    value: win32more.System.Wmi.MI_Sint8A
    exists: Byte
    flags: Byte
class MI_Sint8Field(Structure):
    value: SByte
    exists: Byte
    flags: Byte
class MI_StringA(Structure):
    data: POINTER(POINTER(UInt16))
    size: UInt32
class MI_StringAField(Structure):
    value: win32more.System.Wmi.MI_StringA
    exists: Byte
    flags: Byte
class MI_StringField(Structure):
    value: POINTER(UInt16)
    exists: Byte
    flags: Byte
class MI_SubscriptionDeliveryOptions(Structure):
    reserved1: UInt64
    reserved2: IntPtr
    ft: POINTER(win32more.System.Wmi.MI_SubscriptionDeliveryOptionsFT_head)
class MI_SubscriptionDeliveryOptionsFT(Structure):
    SetString: IntPtr
    SetNumber: IntPtr
    SetDateTime: IntPtr
    SetInterval: IntPtr
    AddCredentials: IntPtr
    Delete: IntPtr
    GetString: IntPtr
    GetNumber: IntPtr
    GetDateTime: IntPtr
    GetInterval: IntPtr
    GetOptionCount: IntPtr
    GetOptionAt: IntPtr
    GetOption: IntPtr
    GetCredentialsCount: IntPtr
    GetCredentialsAt: IntPtr
    GetCredentialsPasswordAt: IntPtr
    Clone: IntPtr
MI_SubscriptionDeliveryType = Int32
MI_SubscriptionDeliveryType_Pull: MI_SubscriptionDeliveryType = 1
MI_SubscriptionDeliveryType_Push: MI_SubscriptionDeliveryType = 2
class MI_Timestamp(Structure):
    year: UInt32
    month: UInt32
    day: UInt32
    hour: UInt32
    minute: UInt32
    second: UInt32
    microseconds: UInt32
    utc: Int32
MI_Type = Int32
MI_BOOLEAN: MI_Type = 0
MI_UINT8: MI_Type = 1
MI_SINT8: MI_Type = 2
MI_UINT16: MI_Type = 3
MI_SINT16: MI_Type = 4
MI_UINT32: MI_Type = 5
MI_SINT32: MI_Type = 6
MI_UINT64: MI_Type = 7
MI_SINT64: MI_Type = 8
MI_REAL32: MI_Type = 9
MI_REAL64: MI_Type = 10
MI_CHAR16: MI_Type = 11
MI_DATETIME: MI_Type = 12
MI_STRING: MI_Type = 13
MI_REFERENCE: MI_Type = 14
MI_INSTANCE: MI_Type = 15
MI_BOOLEANA: MI_Type = 16
MI_UINT8A: MI_Type = 17
MI_SINT8A: MI_Type = 18
MI_UINT16A: MI_Type = 19
MI_SINT16A: MI_Type = 20
MI_UINT32A: MI_Type = 21
MI_SINT32A: MI_Type = 22
MI_UINT64A: MI_Type = 23
MI_SINT64A: MI_Type = 24
MI_REAL32A: MI_Type = 25
MI_REAL64A: MI_Type = 26
MI_CHAR16A: MI_Type = 27
MI_DATETIMEA: MI_Type = 28
MI_STRINGA: MI_Type = 29
MI_REFERENCEA: MI_Type = 30
MI_INSTANCEA: MI_Type = 31
MI_ARRAY: MI_Type = 16
class MI_Uint16A(Structure):
    data: POINTER(UInt16)
    size: UInt32
class MI_Uint16AField(Structure):
    value: win32more.System.Wmi.MI_Uint16A
    exists: Byte
    flags: Byte
class MI_Uint16Field(Structure):
    value: UInt16
    exists: Byte
    flags: Byte
class MI_Uint32A(Structure):
    data: POINTER(UInt32)
    size: UInt32
class MI_Uint32AField(Structure):
    value: win32more.System.Wmi.MI_Uint32A
    exists: Byte
    flags: Byte
class MI_Uint32Field(Structure):
    value: UInt32
    exists: Byte
    flags: Byte
class MI_Uint64A(Structure):
    data: POINTER(UInt64)
    size: UInt32
class MI_Uint64AField(Structure):
    value: win32more.System.Wmi.MI_Uint64A
    exists: Byte
    flags: Byte
class MI_Uint64Field(Structure):
    value: UInt64
    exists: Byte
    flags: Byte
class MI_Uint8A(Structure):
    data: c_char_p_no
    size: UInt32
class MI_Uint8AField(Structure):
    value: win32more.System.Wmi.MI_Uint8A
    exists: Byte
    flags: Byte
class MI_Uint8Field(Structure):
    value: Byte
    exists: Byte
    flags: Byte
class MI_UserCredentials(Structure):
    authenticationType: POINTER(UInt16)
    credentials: _credentials_e__Union
    class _credentials_e__Union(Union):
        usernamePassword: win32more.System.Wmi.MI_UsernamePasswordCreds
        certificateThumbprint: POINTER(UInt16)
class MI_UsernamePasswordCreds(Structure):
    domain: POINTER(UInt16)
    username: POINTER(UInt16)
    password: POINTER(UInt16)
class MI_UtilitiesFT(Structure):
    MapErrorToMiErrorCategory: IntPtr
    CimErrorFromErrorCode: IntPtr
class MI_Value(Union):
    boolean: Byte
    uint8: Byte
    sint8: SByte
    uint16: UInt16
    sint16: Int16
    uint32: UInt32
    sint32: Int32
    uint64: UInt64
    sint64: Int64
    real32: Single
    real64: Double
    char16: UInt16
    datetime: win32more.System.Wmi.MI_Datetime
    string: POINTER(UInt16)
    instance: POINTER(win32more.System.Wmi.MI_Instance_head)
    reference: POINTER(win32more.System.Wmi.MI_Instance_head)
    booleana: win32more.System.Wmi.MI_BooleanA
    uint8a: win32more.System.Wmi.MI_Uint8A
    sint8a: win32more.System.Wmi.MI_Sint8A
    uint16a: win32more.System.Wmi.MI_Uint16A
    sint16a: win32more.System.Wmi.MI_Sint16A
    uint32a: win32more.System.Wmi.MI_Uint32A
    sint32a: win32more.System.Wmi.MI_Sint32A
    uint64a: win32more.System.Wmi.MI_Uint64A
    sint64a: win32more.System.Wmi.MI_Sint64A
    real32a: win32more.System.Wmi.MI_Real32A
    real64a: win32more.System.Wmi.MI_Real64A
    char16a: win32more.System.Wmi.MI_Char16A
    datetimea: win32more.System.Wmi.MI_DatetimeA
    stringa: win32more.System.Wmi.MI_StringA
    referencea: win32more.System.Wmi.MI_ReferenceA
    instancea: win32more.System.Wmi.MI_InstanceA
    array: win32more.System.Wmi.MI_Array
MofCompiler = Guid('6daf9757-2e37-11d2-ae-c9-00-c0-4f-b6-88-20')
class SWbemAnalysisMatrix(Structure):
    m_uVersion: UInt32
    m_uMatrixType: UInt32
    m_pszProperty: win32more.Foundation.PWSTR
    m_uPropertyType: UInt32
    m_uEntries: UInt32
    m_pValues: POINTER(c_void_p)
    m_pbTruthTable: POINTER(win32more.Foundation.BOOL)
class SWbemAnalysisMatrixList(Structure):
    m_uVersion: UInt32
    m_uMatrixType: UInt32
    m_uNumMatrices: UInt32
    m_pMatrices: POINTER(win32more.System.Wmi.SWbemAnalysisMatrix_head)
class SWbemAssocQueryInf(Structure):
    m_uVersion: UInt32
    m_uAnalysisType: UInt32
    m_uFeatureMask: UInt32
    m_pPath: win32more.System.Wmi.IWbemPath_head
    m_pszPath: win32more.Foundation.PWSTR
    m_pszQueryText: win32more.Foundation.PWSTR
    m_pszResultClass: win32more.Foundation.PWSTR
    m_pszAssocClass: win32more.Foundation.PWSTR
    m_pszRole: win32more.Foundation.PWSTR
    m_pszResultRole: win32more.Foundation.PWSTR
    m_pszRequiredQualifier: win32more.Foundation.PWSTR
    m_pszRequiredAssocQualifier: win32more.Foundation.PWSTR
SWbemDateTime = Guid('47dfbe54-cf76-11d3-b3-8f-00-10-5a-1f-47-3a')
SWbemEventSource = Guid('04b83d58-21ae-11d2-8b-33-00-60-08-06-d9-b6')
SWbemLastError = Guid('c2feeeac-cfcd-11d1-8b-05-00-60-08-06-d9-b6')
SWbemLocator = Guid('76a64158-cb41-11d1-8b-02-00-60-08-06-d9-b6')
SWbemMethod = Guid('04b83d5b-21ae-11d2-8b-33-00-60-08-06-d9-b6')
SWbemMethodSet = Guid('04b83d5a-21ae-11d2-8b-33-00-60-08-06-d9-b6')
SWbemNamedValue = Guid('04b83d60-21ae-11d2-8b-33-00-60-08-06-d9-b6')
SWbemNamedValueSet = Guid('9aed384e-ce8b-11d1-8b-05-00-60-08-06-d9-b6')
SWbemObject = Guid('04b83d62-21ae-11d2-8b-33-00-60-08-06-d9-b6')
SWbemObjectEx = Guid('d6bdafb2-9435-491f-bb-87-6a-a0-f0-bc-31-a2')
SWbemObjectPath = Guid('5791bc26-ce9c-11d1-97-bf-00-00-f8-1e-84-9c')
SWbemObjectSet = Guid('04b83d61-21ae-11d2-8b-33-00-60-08-06-d9-b6')
SWbemPrivilege = Guid('26ee67bc-5804-11d2-8b-4a-00-60-08-06-d9-b6')
SWbemPrivilegeSet = Guid('26ee67be-5804-11d2-8b-4a-00-60-08-06-d9-b6')
SWbemProperty = Guid('04b83d5d-21ae-11d2-8b-33-00-60-08-06-d9-b6')
SWbemPropertySet = Guid('04b83d5c-21ae-11d2-8b-33-00-60-08-06-d9-b6')
SWbemQualifier = Guid('04b83d5f-21ae-11d2-8b-33-00-60-08-06-d9-b6')
SWbemQualifierSet = Guid('04b83d5e-21ae-11d2-8b-33-00-60-08-06-d9-b6')
class SWbemQueryQualifiedName(Structure):
    m_uVersion: UInt32
    m_uTokenType: UInt32
    m_uNameListSize: UInt32
    m_ppszNameList: POINTER(win32more.Foundation.PWSTR)
    m_bArraysUsed: win32more.Foundation.BOOL
    m_pbArrayElUsed: POINTER(win32more.Foundation.BOOL)
    m_puArrayIndex: POINTER(UInt32)
SWbemRefreshableItem = Guid('8c6854bc-de4b-11d3-b3-90-00-10-5a-1f-47-3a')
SWbemRefresher = Guid('d269bf5c-d9c1-11d3-b3-8f-00-10-5a-1f-47-3a')
class SWbemRpnConst(Union):
    m_pszStrVal: win32more.Foundation.PWSTR
    m_bBoolVal: win32more.Foundation.BOOL
    m_lLongVal: Int32
    m_uLongVal: UInt32
    m_dblVal: Double
    m_lVal64: Int64
    m_uVal64: Int64
class SWbemRpnEncodedQuery(Structure):
    m_uVersion: UInt32
    m_uTokenType: UInt32
    m_uParsedFeatureMask: UInt64
    m_uDetectedArraySize: UInt32
    m_puDetectedFeatures: POINTER(UInt32)
    m_uSelectListSize: UInt32
    m_ppSelectList: POINTER(POINTER(win32more.System.Wmi.SWbemQueryQualifiedName_head))
    m_uFromTargetType: UInt32
    m_pszOptionalFromPath: win32more.Foundation.PWSTR
    m_uFromListSize: UInt32
    m_ppszFromList: POINTER(win32more.Foundation.PWSTR)
    m_uWhereClauseSize: UInt32
    m_ppRpnWhereClause: POINTER(POINTER(win32more.System.Wmi.SWbemRpnQueryToken_head))
    m_dblWithinPolling: Double
    m_dblWithinWindow: Double
    m_uOrderByListSize: UInt32
    m_ppszOrderByList: POINTER(win32more.Foundation.PWSTR)
    m_uOrderDirectionEl: POINTER(UInt32)
class SWbemRpnQueryToken(Structure):
    m_uVersion: UInt32
    m_uTokenType: UInt32
    m_uSubexpressionShape: UInt32
    m_uOperator: UInt32
    m_pRightIdent: POINTER(win32more.System.Wmi.SWbemQueryQualifiedName_head)
    m_pLeftIdent: POINTER(win32more.System.Wmi.SWbemQueryQualifiedName_head)
    m_uConstApparentType: UInt32
    m_Const: win32more.System.Wmi.SWbemRpnConst
    m_uConst2ApparentType: UInt32
    m_Const2: win32more.System.Wmi.SWbemRpnConst
    m_pszRightFunc: win32more.Foundation.PWSTR
    m_pszLeftFunc: win32more.Foundation.PWSTR
class SWbemRpnTokenList(Structure):
    m_uVersion: UInt32
    m_uTokenType: UInt32
    m_uNumTokens: UInt32
SWbemSecurity = Guid('b54d66e9-2287-11d2-8b-33-00-60-08-06-d9-b6')
SWbemServices = Guid('04b83d63-21ae-11d2-8b-33-00-60-08-06-d9-b6')
SWbemServicesEx = Guid('62e522dc-8cf3-40a8-8b-2e-37-d5-95-65-1e-40')
SWbemSink = Guid('75718c9a-f029-11d1-a1-ac-00-c0-4f-b6-c2-23')
UnsecuredApartment = Guid('49bd2028-1523-11d1-ad-79-00-c0-4f-d8-fd-ff')
WBEM_BACKUP_RESTORE_FLAGS = Int32
WBEM_FLAG_BACKUP_RESTORE_DEFAULT: WBEM_BACKUP_RESTORE_FLAGS = 0
WBEM_FLAG_BACKUP_RESTORE_FORCE_SHUTDOWN: WBEM_BACKUP_RESTORE_FLAGS = 1
WBEM_BATCH_TYPE = Int32
WBEM_FLAG_BATCH_IF_NEEDED: WBEM_BATCH_TYPE = 0
WBEM_FLAG_MUST_BATCH: WBEM_BATCH_TYPE = 1
WBEM_FLAG_MUST_NOT_BATCH: WBEM_BATCH_TYPE = 2
WBEM_CHANGE_FLAG_TYPE = Int32
WBEM_FLAG_CREATE_OR_UPDATE: WBEM_CHANGE_FLAG_TYPE = 0
WBEM_FLAG_UPDATE_ONLY: WBEM_CHANGE_FLAG_TYPE = 1
WBEM_FLAG_CREATE_ONLY: WBEM_CHANGE_FLAG_TYPE = 2
WBEM_FLAG_UPDATE_COMPATIBLE: WBEM_CHANGE_FLAG_TYPE = 0
WBEM_FLAG_UPDATE_SAFE_MODE: WBEM_CHANGE_FLAG_TYPE = 32
WBEM_FLAG_UPDATE_FORCE_MODE: WBEM_CHANGE_FLAG_TYPE = 64
WBEM_MASK_UPDATE_MODE: WBEM_CHANGE_FLAG_TYPE = 96
WBEM_FLAG_ADVISORY: WBEM_CHANGE_FLAG_TYPE = 65536
WBEM_COMPARISON_FLAG = Int32
WBEM_COMPARISON_INCLUDE_ALL: WBEM_COMPARISON_FLAG = 0
WBEM_FLAG_IGNORE_QUALIFIERS: WBEM_COMPARISON_FLAG = 1
WBEM_FLAG_IGNORE_OBJECT_SOURCE: WBEM_COMPARISON_FLAG = 2
WBEM_FLAG_IGNORE_DEFAULT_VALUES: WBEM_COMPARISON_FLAG = 4
WBEM_FLAG_IGNORE_CLASS: WBEM_COMPARISON_FLAG = 8
WBEM_FLAG_IGNORE_CASE: WBEM_COMPARISON_FLAG = 16
WBEM_FLAG_IGNORE_FLAVOR: WBEM_COMPARISON_FLAG = 32
class WBEM_COMPILE_STATUS_INFO(Structure):
    lPhaseError: Int32
    hRes: win32more.Foundation.HRESULT
    ObjectNum: Int32
    FirstLine: Int32
    LastLine: Int32
    dwOutFlags: UInt32
WBEM_COMPILER_OPTIONS = Int32
WBEM_FLAG_CHECK_ONLY: WBEM_COMPILER_OPTIONS = 1
WBEM_FLAG_AUTORECOVER: WBEM_COMPILER_OPTIONS = 2
WBEM_FLAG_WMI_CHECK: WBEM_COMPILER_OPTIONS = 4
WBEM_FLAG_CONSOLE_PRINT: WBEM_COMPILER_OPTIONS = 8
WBEM_FLAG_DONT_ADD_TO_LIST: WBEM_COMPILER_OPTIONS = 16
WBEM_FLAG_SPLIT_FILES: WBEM_COMPILER_OPTIONS = 32
WBEM_FLAG_STORE_FILE: WBEM_COMPILER_OPTIONS = 256
WBEM_CONDITION_FLAG_TYPE = Int32
WBEM_FLAG_ALWAYS: WBEM_CONDITION_FLAG_TYPE = 0
WBEM_FLAG_ONLY_IF_TRUE: WBEM_CONDITION_FLAG_TYPE = 1
WBEM_FLAG_ONLY_IF_FALSE: WBEM_CONDITION_FLAG_TYPE = 2
WBEM_FLAG_ONLY_IF_IDENTICAL: WBEM_CONDITION_FLAG_TYPE = 3
WBEM_MASK_PRIMARY_CONDITION: WBEM_CONDITION_FLAG_TYPE = 3
WBEM_FLAG_KEYS_ONLY: WBEM_CONDITION_FLAG_TYPE = 4
WBEM_FLAG_REFS_ONLY: WBEM_CONDITION_FLAG_TYPE = 8
WBEM_FLAG_LOCAL_ONLY: WBEM_CONDITION_FLAG_TYPE = 16
WBEM_FLAG_PROPAGATED_ONLY: WBEM_CONDITION_FLAG_TYPE = 32
WBEM_FLAG_SYSTEM_ONLY: WBEM_CONDITION_FLAG_TYPE = 48
WBEM_FLAG_NONSYSTEM_ONLY: WBEM_CONDITION_FLAG_TYPE = 64
WBEM_MASK_CONDITION_ORIGIN: WBEM_CONDITION_FLAG_TYPE = 112
WBEM_FLAG_CLASS_OVERRIDES_ONLY: WBEM_CONDITION_FLAG_TYPE = 256
WBEM_FLAG_CLASS_LOCAL_AND_OVERRIDES: WBEM_CONDITION_FLAG_TYPE = 512
WBEM_MASK_CLASS_CONDITION: WBEM_CONDITION_FLAG_TYPE = 768
WBEM_CONNECT_OPTIONS = Int32
WBEM_FLAG_CONNECT_REPOSITORY_ONLY: WBEM_CONNECT_OPTIONS = 64
WBEM_FLAG_CONNECT_USE_MAX_WAIT: WBEM_CONNECT_OPTIONS = 128
WBEM_FLAG_CONNECT_PROVIDERS: WBEM_CONNECT_OPTIONS = 256
WBEM_EXTRA_RETURN_CODES = Int32
WBEM_S_INITIALIZED: WBEM_EXTRA_RETURN_CODES = 0
WBEM_S_LIMITED_SERVICE: WBEM_EXTRA_RETURN_CODES = 274433
WBEM_S_INDIRECTLY_UPDATED: WBEM_EXTRA_RETURN_CODES = 274434
WBEM_S_SUBJECT_TO_SDS: WBEM_EXTRA_RETURN_CODES = 274435
WBEM_E_RETRY_LATER: WBEM_EXTRA_RETURN_CODES = -2147209215
WBEM_E_RESOURCE_CONTENTION: WBEM_EXTRA_RETURN_CODES = -2147209214
WBEM_FLAVOR_TYPE = Int32
WBEM_FLAVOR_DONT_PROPAGATE: WBEM_FLAVOR_TYPE = 0
WBEM_FLAVOR_FLAG_PROPAGATE_TO_INSTANCE: WBEM_FLAVOR_TYPE = 1
WBEM_FLAVOR_FLAG_PROPAGATE_TO_DERIVED_CLASS: WBEM_FLAVOR_TYPE = 2
WBEM_FLAVOR_MASK_PROPAGATION: WBEM_FLAVOR_TYPE = 15
WBEM_FLAVOR_OVERRIDABLE: WBEM_FLAVOR_TYPE = 0
WBEM_FLAVOR_NOT_OVERRIDABLE: WBEM_FLAVOR_TYPE = 16
WBEM_FLAVOR_MASK_PERMISSIONS: WBEM_FLAVOR_TYPE = 16
WBEM_FLAVOR_ORIGIN_LOCAL: WBEM_FLAVOR_TYPE = 0
WBEM_FLAVOR_ORIGIN_PROPAGATED: WBEM_FLAVOR_TYPE = 32
WBEM_FLAVOR_ORIGIN_SYSTEM: WBEM_FLAVOR_TYPE = 64
WBEM_FLAVOR_MASK_ORIGIN: WBEM_FLAVOR_TYPE = 96
WBEM_FLAVOR_NOT_AMENDED: WBEM_FLAVOR_TYPE = 0
WBEM_FLAVOR_AMENDED: WBEM_FLAVOR_TYPE = 128
WBEM_FLAVOR_MASK_AMENDED: WBEM_FLAVOR_TYPE = 128
WBEM_GENERIC_FLAG_TYPE = UInt32
WBEM_FLAG_RETURN_IMMEDIATELY: WBEM_GENERIC_FLAG_TYPE = 16
WBEM_FLAG_RETURN_WBEM_COMPLETE: WBEM_GENERIC_FLAG_TYPE = 0
WBEM_FLAG_BIDIRECTIONAL: WBEM_GENERIC_FLAG_TYPE = 0
WBEM_FLAG_FORWARD_ONLY: WBEM_GENERIC_FLAG_TYPE = 32
WBEM_FLAG_NO_ERROR_OBJECT: WBEM_GENERIC_FLAG_TYPE = 64
WBEM_FLAG_RETURN_ERROR_OBJECT: WBEM_GENERIC_FLAG_TYPE = 0
WBEM_FLAG_SEND_STATUS: WBEM_GENERIC_FLAG_TYPE = 128
WBEM_FLAG_DONT_SEND_STATUS: WBEM_GENERIC_FLAG_TYPE = 0
WBEM_FLAG_ENSURE_LOCATABLE: WBEM_GENERIC_FLAG_TYPE = 256
WBEM_FLAG_DIRECT_READ: WBEM_GENERIC_FLAG_TYPE = 512
WBEM_FLAG_SEND_ONLY_SELECTED: WBEM_GENERIC_FLAG_TYPE = 0
WBEM_RETURN_WHEN_COMPLETE: WBEM_GENERIC_FLAG_TYPE = 0
WBEM_RETURN_IMMEDIATELY: WBEM_GENERIC_FLAG_TYPE = 16
WBEM_MASK_RESERVED_FLAGS: WBEM_GENERIC_FLAG_TYPE = 126976
WBEM_FLAG_USE_AMENDED_QUALIFIERS: WBEM_GENERIC_FLAG_TYPE = 131072
WBEM_FLAG_STRONG_VALIDATION: WBEM_GENERIC_FLAG_TYPE = 1048576
WBEM_GENUS_TYPE = Int32
WBEM_GENUS_CLASS: WBEM_GENUS_TYPE = 1
WBEM_GENUS_INSTANCE: WBEM_GENUS_TYPE = 2
WBEM_GET_KEY_FLAGS = Int32
WBEMPATH_TEXT: WBEM_GET_KEY_FLAGS = 1
WBEMPATH_QUOTEDTEXT: WBEM_GET_KEY_FLAGS = 2
WBEM_GET_TEXT_FLAGS = Int32
WBEMPATH_COMPRESSED: WBEM_GET_TEXT_FLAGS = 1
WBEMPATH_GET_RELATIVE_ONLY: WBEM_GET_TEXT_FLAGS = 2
WBEMPATH_GET_SERVER_TOO: WBEM_GET_TEXT_FLAGS = 4
WBEMPATH_GET_SERVER_AND_NAMESPACE_ONLY: WBEM_GET_TEXT_FLAGS = 8
WBEMPATH_GET_NAMESPACE_ONLY: WBEM_GET_TEXT_FLAGS = 16
WBEMPATH_GET_ORIGINAL: WBEM_GET_TEXT_FLAGS = 32
WBEM_INFORMATION_FLAG_TYPE = Int32
WBEM_FLAG_SHORT_NAME: WBEM_INFORMATION_FLAG_TYPE = 1
WBEM_FLAG_LONG_NAME: WBEM_INFORMATION_FLAG_TYPE = 2
WBEM_LIMITATION_FLAG_TYPE = Int32
WBEM_FLAG_EXCLUDE_OBJECT_QUALIFIERS: WBEM_LIMITATION_FLAG_TYPE = 16
WBEM_FLAG_EXCLUDE_PROPERTY_QUALIFIERS: WBEM_LIMITATION_FLAG_TYPE = 32
WBEM_LIMITS = Int32
WBEM_MAX_IDENTIFIER: WBEM_LIMITS = 4096
WBEM_MAX_QUERY: WBEM_LIMITS = 16384
WBEM_MAX_PATH: WBEM_LIMITS = 8192
WBEM_MAX_OBJECT_NESTING: WBEM_LIMITS = 64
WBEM_MAX_USER_PROPERTIES: WBEM_LIMITS = 1024
WBEM_LOCKING_FLAG_TYPE = Int32
WBEM_FLAG_ALLOW_READ: WBEM_LOCKING_FLAG_TYPE = 1
WBEM_LOGIN_TYPE = Int32
WBEM_FLAG_INPROC_LOGIN: WBEM_LOGIN_TYPE = 0
WBEM_FLAG_LOCAL_LOGIN: WBEM_LOGIN_TYPE = 1
WBEM_FLAG_REMOTE_LOGIN: WBEM_LOGIN_TYPE = 2
WBEM_AUTHENTICATION_METHOD_MASK: WBEM_LOGIN_TYPE = 15
WBEM_FLAG_USE_MULTIPLE_CHALLENGES: WBEM_LOGIN_TYPE = 16
WBEM_PATH_CREATE_FLAG = Int32
WBEMPATH_CREATE_ACCEPT_RELATIVE: WBEM_PATH_CREATE_FLAG = 1
WBEMPATH_CREATE_ACCEPT_ABSOLUTE: WBEM_PATH_CREATE_FLAG = 2
WBEMPATH_CREATE_ACCEPT_ALL: WBEM_PATH_CREATE_FLAG = 4
WBEMPATH_TREAT_SINGLE_IDENT_AS_NS: WBEM_PATH_CREATE_FLAG = 8
WBEM_PATH_STATUS_FLAG = Int32
WBEMPATH_INFO_ANON_LOCAL_MACHINE: WBEM_PATH_STATUS_FLAG = 1
WBEMPATH_INFO_HAS_MACHINE_NAME: WBEM_PATH_STATUS_FLAG = 2
WBEMPATH_INFO_IS_CLASS_REF: WBEM_PATH_STATUS_FLAG = 4
WBEMPATH_INFO_IS_INST_REF: WBEM_PATH_STATUS_FLAG = 8
WBEMPATH_INFO_HAS_SUBSCOPES: WBEM_PATH_STATUS_FLAG = 16
WBEMPATH_INFO_IS_COMPOUND: WBEM_PATH_STATUS_FLAG = 32
WBEMPATH_INFO_HAS_V2_REF_PATHS: WBEM_PATH_STATUS_FLAG = 64
WBEMPATH_INFO_HAS_IMPLIED_KEY: WBEM_PATH_STATUS_FLAG = 128
WBEMPATH_INFO_CONTAINS_SINGLETON: WBEM_PATH_STATUS_FLAG = 256
WBEMPATH_INFO_V1_COMPLIANT: WBEM_PATH_STATUS_FLAG = 512
WBEMPATH_INFO_V2_COMPLIANT: WBEM_PATH_STATUS_FLAG = 1024
WBEMPATH_INFO_CIM_COMPLIANT: WBEM_PATH_STATUS_FLAG = 2048
WBEMPATH_INFO_IS_SINGLETON: WBEM_PATH_STATUS_FLAG = 4096
WBEMPATH_INFO_IS_PARENT: WBEM_PATH_STATUS_FLAG = 8192
WBEMPATH_INFO_SERVER_NAMESPACE_ONLY: WBEM_PATH_STATUS_FLAG = 16384
WBEMPATH_INFO_NATIVE_PATH: WBEM_PATH_STATUS_FLAG = 32768
WBEMPATH_INFO_WMI_PATH: WBEM_PATH_STATUS_FLAG = 65536
WBEMPATH_INFO_PATH_HAD_SERVER: WBEM_PATH_STATUS_FLAG = 131072
WBEM_PROVIDER_FLAGS = Int32
WBEM_FLAG_OWNER_UPDATE: WBEM_PROVIDER_FLAGS = 65536
WBEM_PROVIDER_REQUIREMENTS_TYPE = Int32
WBEM_REQUIREMENTS_START_POSTFILTER: WBEM_PROVIDER_REQUIREMENTS_TYPE = 0
WBEM_REQUIREMENTS_STOP_POSTFILTER: WBEM_PROVIDER_REQUIREMENTS_TYPE = 1
WBEM_REQUIREMENTS_RECHECK_SUBSCRIPTIONS: WBEM_PROVIDER_REQUIREMENTS_TYPE = 2
WBEM_QUERY_FLAG_TYPE = Int32
WBEM_FLAG_DEEP: WBEM_QUERY_FLAG_TYPE = 0
WBEM_FLAG_SHALLOW: WBEM_QUERY_FLAG_TYPE = 1
WBEM_FLAG_PROTOTYPE: WBEM_QUERY_FLAG_TYPE = 2
WBEM_REFRESHER_FLAGS = Int32
WBEM_FLAG_REFRESH_AUTO_RECONNECT: WBEM_REFRESHER_FLAGS = 0
WBEM_FLAG_REFRESH_NO_AUTO_RECONNECT: WBEM_REFRESHER_FLAGS = 1
WBEM_SECURITY_FLAGS = Int32
WBEM_ENABLE: WBEM_SECURITY_FLAGS = 1
WBEM_METHOD_EXECUTE: WBEM_SECURITY_FLAGS = 2
WBEM_FULL_WRITE_REP: WBEM_SECURITY_FLAGS = 4
WBEM_PARTIAL_WRITE_REP: WBEM_SECURITY_FLAGS = 8
WBEM_WRITE_PROVIDER: WBEM_SECURITY_FLAGS = 16
WBEM_REMOTE_ACCESS: WBEM_SECURITY_FLAGS = 32
WBEM_RIGHT_SUBSCRIBE: WBEM_SECURITY_FLAGS = 64
WBEM_RIGHT_PUBLISH: WBEM_SECURITY_FLAGS = 128
WBEM_SHUTDOWN_FLAGS = Int32
WBEM_SHUTDOWN_UNLOAD_COMPONENT: WBEM_SHUTDOWN_FLAGS = 1
WBEM_SHUTDOWN_WMI: WBEM_SHUTDOWN_FLAGS = 2
WBEM_SHUTDOWN_OS: WBEM_SHUTDOWN_FLAGS = 3
WBEM_STATUS_TYPE = Int32
WBEM_STATUS_COMPLETE: WBEM_STATUS_TYPE = 0
WBEM_STATUS_REQUIREMENTS: WBEM_STATUS_TYPE = 1
WBEM_STATUS_PROGRESS: WBEM_STATUS_TYPE = 2
WBEM_STATUS_LOGGING_INFORMATION: WBEM_STATUS_TYPE = 256
WBEM_STATUS_LOGGING_INFORMATION_PROVIDER: WBEM_STATUS_TYPE = 512
WBEM_STATUS_LOGGING_INFORMATION_HOST: WBEM_STATUS_TYPE = 1024
WBEM_STATUS_LOGGING_INFORMATION_REPOSITORY: WBEM_STATUS_TYPE = 2048
WBEM_STATUS_LOGGING_INFORMATION_ESS: WBEM_STATUS_TYPE = 4096
WBEM_TEXT_FLAG_TYPE = Int32
WBEM_FLAG_NO_FLAVORS: WBEM_TEXT_FLAG_TYPE = 1
WBEM_UNSECAPP_FLAG_TYPE = Int32
WBEM_FLAG_UNSECAPP_DEFAULT_CHECK_ACCESS: WBEM_UNSECAPP_FLAG_TYPE = 0
WBEM_FLAG_UNSECAPP_CHECK_ACCESS: WBEM_UNSECAPP_FLAG_TYPE = 1
WBEM_FLAG_UNSECAPP_DONT_CHECK_ACCESS: WBEM_UNSECAPP_FLAG_TYPE = 2
WbemAdministrativeLocator = Guid('cb8555cc-9128-11d1-ad-9b-00-c0-4f-d8-fd-ff')
WbemAuthenticatedLocator = Guid('cd184336-9128-11d1-ad-9b-00-c0-4f-d8-fd-ff')
WbemAuthenticationLevelEnum = Int32
WbemAuthenticationLevelEnum_wbemAuthenticationLevelDefault: WbemAuthenticationLevelEnum = 0
WbemAuthenticationLevelEnum_wbemAuthenticationLevelNone: WbemAuthenticationLevelEnum = 1
WbemAuthenticationLevelEnum_wbemAuthenticationLevelConnect: WbemAuthenticationLevelEnum = 2
WbemAuthenticationLevelEnum_wbemAuthenticationLevelCall: WbemAuthenticationLevelEnum = 3
WbemAuthenticationLevelEnum_wbemAuthenticationLevelPkt: WbemAuthenticationLevelEnum = 4
WbemAuthenticationLevelEnum_wbemAuthenticationLevelPktIntegrity: WbemAuthenticationLevelEnum = 5
WbemAuthenticationLevelEnum_wbemAuthenticationLevelPktPrivacy: WbemAuthenticationLevelEnum = 6
WbemBackupRestore = Guid('c49e32c6-bc8b-11d2-85-d4-00-10-5a-1f-83-04')
WbemChangeFlagEnum = Int32
WbemChangeFlagEnum_wbemChangeFlagCreateOrUpdate: WbemChangeFlagEnum = 0
WbemChangeFlagEnum_wbemChangeFlagUpdateOnly: WbemChangeFlagEnum = 1
WbemChangeFlagEnum_wbemChangeFlagCreateOnly: WbemChangeFlagEnum = 2
WbemChangeFlagEnum_wbemChangeFlagUpdateCompatible: WbemChangeFlagEnum = 0
WbemChangeFlagEnum_wbemChangeFlagUpdateSafeMode: WbemChangeFlagEnum = 32
WbemChangeFlagEnum_wbemChangeFlagUpdateForceMode: WbemChangeFlagEnum = 64
WbemChangeFlagEnum_wbemChangeFlagStrongValidation: WbemChangeFlagEnum = 128
WbemChangeFlagEnum_wbemChangeFlagAdvisory: WbemChangeFlagEnum = 65536
WbemCimtypeEnum = Int32
WbemCimtypeEnum_wbemCimtypeSint8: WbemCimtypeEnum = 16
WbemCimtypeEnum_wbemCimtypeUint8: WbemCimtypeEnum = 17
WbemCimtypeEnum_wbemCimtypeSint16: WbemCimtypeEnum = 2
WbemCimtypeEnum_wbemCimtypeUint16: WbemCimtypeEnum = 18
WbemCimtypeEnum_wbemCimtypeSint32: WbemCimtypeEnum = 3
WbemCimtypeEnum_wbemCimtypeUint32: WbemCimtypeEnum = 19
WbemCimtypeEnum_wbemCimtypeSint64: WbemCimtypeEnum = 20
WbemCimtypeEnum_wbemCimtypeUint64: WbemCimtypeEnum = 21
WbemCimtypeEnum_wbemCimtypeReal32: WbemCimtypeEnum = 4
WbemCimtypeEnum_wbemCimtypeReal64: WbemCimtypeEnum = 5
WbemCimtypeEnum_wbemCimtypeBoolean: WbemCimtypeEnum = 11
WbemCimtypeEnum_wbemCimtypeString: WbemCimtypeEnum = 8
WbemCimtypeEnum_wbemCimtypeDatetime: WbemCimtypeEnum = 101
WbemCimtypeEnum_wbemCimtypeReference: WbemCimtypeEnum = 102
WbemCimtypeEnum_wbemCimtypeChar16: WbemCimtypeEnum = 103
WbemCimtypeEnum_wbemCimtypeObject: WbemCimtypeEnum = 13
WbemClassObject = Guid('9a653086-174f-11d2-b5-f9-00-10-4b-70-3e-fd')
WbemComparisonFlagEnum = Int32
WbemComparisonFlagEnum_wbemComparisonFlagIncludeAll: WbemComparisonFlagEnum = 0
WbemComparisonFlagEnum_wbemComparisonFlagIgnoreQualifiers: WbemComparisonFlagEnum = 1
WbemComparisonFlagEnum_wbemComparisonFlagIgnoreObjectSource: WbemComparisonFlagEnum = 2
WbemComparisonFlagEnum_wbemComparisonFlagIgnoreDefaultValues: WbemComparisonFlagEnum = 4
WbemComparisonFlagEnum_wbemComparisonFlagIgnoreClass: WbemComparisonFlagEnum = 8
WbemComparisonFlagEnum_wbemComparisonFlagIgnoreCase: WbemComparisonFlagEnum = 16
WbemComparisonFlagEnum_wbemComparisonFlagIgnoreFlavor: WbemComparisonFlagEnum = 32
WbemConnectOptionsEnum = Int32
WbemConnectOptionsEnum_wbemConnectFlagUseMaxWait: WbemConnectOptionsEnum = 128
WbemContext = Guid('674b6698-ee92-11d0-ad-71-00-c0-4f-d8-fd-ff')
WbemDCOMTransport = Guid('f7ce2e13-8c90-11d1-9e-7b-00-c0-4f-c3-24-a8')
WbemDecoupledBasicEventProvider = Guid('f5f75737-2843-4f22-93-3d-c7-6a-97-cd-a6-2f')
WbemDecoupledRegistrar = Guid('4cfc7932-0f9d-4bef-9c-32-8e-a2-a6-b5-6f-cb')
WbemDefPath = Guid('cf4cc405-e2c5-4ddd-b3-ce-5e-75-82-d8-c9-fa')
WbemErrorEnum = Int32
WbemErrorEnum_wbemNoErr: WbemErrorEnum = 0
WbemErrorEnum_wbemErrFailed: WbemErrorEnum = -2147217407
WbemErrorEnum_wbemErrNotFound: WbemErrorEnum = -2147217406
WbemErrorEnum_wbemErrAccessDenied: WbemErrorEnum = -2147217405
WbemErrorEnum_wbemErrProviderFailure: WbemErrorEnum = -2147217404
WbemErrorEnum_wbemErrTypeMismatch: WbemErrorEnum = -2147217403
WbemErrorEnum_wbemErrOutOfMemory: WbemErrorEnum = -2147217402
WbemErrorEnum_wbemErrInvalidContext: WbemErrorEnum = -2147217401
WbemErrorEnum_wbemErrInvalidParameter: WbemErrorEnum = -2147217400
WbemErrorEnum_wbemErrNotAvailable: WbemErrorEnum = -2147217399
WbemErrorEnum_wbemErrCriticalError: WbemErrorEnum = -2147217398
WbemErrorEnum_wbemErrInvalidStream: WbemErrorEnum = -2147217397
WbemErrorEnum_wbemErrNotSupported: WbemErrorEnum = -2147217396
WbemErrorEnum_wbemErrInvalidSuperclass: WbemErrorEnum = -2147217395
WbemErrorEnum_wbemErrInvalidNamespace: WbemErrorEnum = -2147217394
WbemErrorEnum_wbemErrInvalidObject: WbemErrorEnum = -2147217393
WbemErrorEnum_wbemErrInvalidClass: WbemErrorEnum = -2147217392
WbemErrorEnum_wbemErrProviderNotFound: WbemErrorEnum = -2147217391
WbemErrorEnum_wbemErrInvalidProviderRegistration: WbemErrorEnum = -2147217390
WbemErrorEnum_wbemErrProviderLoadFailure: WbemErrorEnum = -2147217389
WbemErrorEnum_wbemErrInitializationFailure: WbemErrorEnum = -2147217388
WbemErrorEnum_wbemErrTransportFailure: WbemErrorEnum = -2147217387
WbemErrorEnum_wbemErrInvalidOperation: WbemErrorEnum = -2147217386
WbemErrorEnum_wbemErrInvalidQuery: WbemErrorEnum = -2147217385
WbemErrorEnum_wbemErrInvalidQueryType: WbemErrorEnum = -2147217384
WbemErrorEnum_wbemErrAlreadyExists: WbemErrorEnum = -2147217383
WbemErrorEnum_wbemErrOverrideNotAllowed: WbemErrorEnum = -2147217382
WbemErrorEnum_wbemErrPropagatedQualifier: WbemErrorEnum = -2147217381
WbemErrorEnum_wbemErrPropagatedProperty: WbemErrorEnum = -2147217380
WbemErrorEnum_wbemErrUnexpected: WbemErrorEnum = -2147217379
WbemErrorEnum_wbemErrIllegalOperation: WbemErrorEnum = -2147217378
WbemErrorEnum_wbemErrCannotBeKey: WbemErrorEnum = -2147217377
WbemErrorEnum_wbemErrIncompleteClass: WbemErrorEnum = -2147217376
WbemErrorEnum_wbemErrInvalidSyntax: WbemErrorEnum = -2147217375
WbemErrorEnum_wbemErrNondecoratedObject: WbemErrorEnum = -2147217374
WbemErrorEnum_wbemErrReadOnly: WbemErrorEnum = -2147217373
WbemErrorEnum_wbemErrProviderNotCapable: WbemErrorEnum = -2147217372
WbemErrorEnum_wbemErrClassHasChildren: WbemErrorEnum = -2147217371
WbemErrorEnum_wbemErrClassHasInstances: WbemErrorEnum = -2147217370
WbemErrorEnum_wbemErrQueryNotImplemented: WbemErrorEnum = -2147217369
WbemErrorEnum_wbemErrIllegalNull: WbemErrorEnum = -2147217368
WbemErrorEnum_wbemErrInvalidQualifierType: WbemErrorEnum = -2147217367
WbemErrorEnum_wbemErrInvalidPropertyType: WbemErrorEnum = -2147217366
WbemErrorEnum_wbemErrValueOutOfRange: WbemErrorEnum = -2147217365
WbemErrorEnum_wbemErrCannotBeSingleton: WbemErrorEnum = -2147217364
WbemErrorEnum_wbemErrInvalidCimType: WbemErrorEnum = -2147217363
WbemErrorEnum_wbemErrInvalidMethod: WbemErrorEnum = -2147217362
WbemErrorEnum_wbemErrInvalidMethodParameters: WbemErrorEnum = -2147217361
WbemErrorEnum_wbemErrSystemProperty: WbemErrorEnum = -2147217360
WbemErrorEnum_wbemErrInvalidProperty: WbemErrorEnum = -2147217359
WbemErrorEnum_wbemErrCallCancelled: WbemErrorEnum = -2147217358
WbemErrorEnum_wbemErrShuttingDown: WbemErrorEnum = -2147217357
WbemErrorEnum_wbemErrPropagatedMethod: WbemErrorEnum = -2147217356
WbemErrorEnum_wbemErrUnsupportedParameter: WbemErrorEnum = -2147217355
WbemErrorEnum_wbemErrMissingParameter: WbemErrorEnum = -2147217354
WbemErrorEnum_wbemErrInvalidParameterId: WbemErrorEnum = -2147217353
WbemErrorEnum_wbemErrNonConsecutiveParameterIds: WbemErrorEnum = -2147217352
WbemErrorEnum_wbemErrParameterIdOnRetval: WbemErrorEnum = -2147217351
WbemErrorEnum_wbemErrInvalidObjectPath: WbemErrorEnum = -2147217350
WbemErrorEnum_wbemErrOutOfDiskSpace: WbemErrorEnum = -2147217349
WbemErrorEnum_wbemErrBufferTooSmall: WbemErrorEnum = -2147217348
WbemErrorEnum_wbemErrUnsupportedPutExtension: WbemErrorEnum = -2147217347
WbemErrorEnum_wbemErrUnknownObjectType: WbemErrorEnum = -2147217346
WbemErrorEnum_wbemErrUnknownPacketType: WbemErrorEnum = -2147217345
WbemErrorEnum_wbemErrMarshalVersionMismatch: WbemErrorEnum = -2147217344
WbemErrorEnum_wbemErrMarshalInvalidSignature: WbemErrorEnum = -2147217343
WbemErrorEnum_wbemErrInvalidQualifier: WbemErrorEnum = -2147217342
WbemErrorEnum_wbemErrInvalidDuplicateParameter: WbemErrorEnum = -2147217341
WbemErrorEnum_wbemErrTooMuchData: WbemErrorEnum = -2147217340
WbemErrorEnum_wbemErrServerTooBusy: WbemErrorEnum = -2147217339
WbemErrorEnum_wbemErrInvalidFlavor: WbemErrorEnum = -2147217338
WbemErrorEnum_wbemErrCircularReference: WbemErrorEnum = -2147217337
WbemErrorEnum_wbemErrUnsupportedClassUpdate: WbemErrorEnum = -2147217336
WbemErrorEnum_wbemErrCannotChangeKeyInheritance: WbemErrorEnum = -2147217335
WbemErrorEnum_wbemErrCannotChangeIndexInheritance: WbemErrorEnum = -2147217328
WbemErrorEnum_wbemErrTooManyProperties: WbemErrorEnum = -2147217327
WbemErrorEnum_wbemErrUpdateTypeMismatch: WbemErrorEnum = -2147217326
WbemErrorEnum_wbemErrUpdateOverrideNotAllowed: WbemErrorEnum = -2147217325
WbemErrorEnum_wbemErrUpdatePropagatedMethod: WbemErrorEnum = -2147217324
WbemErrorEnum_wbemErrMethodNotImplemented: WbemErrorEnum = -2147217323
WbemErrorEnum_wbemErrMethodDisabled: WbemErrorEnum = -2147217322
WbemErrorEnum_wbemErrRefresherBusy: WbemErrorEnum = -2147217321
WbemErrorEnum_wbemErrUnparsableQuery: WbemErrorEnum = -2147217320
WbemErrorEnum_wbemErrNotEventClass: WbemErrorEnum = -2147217319
WbemErrorEnum_wbemErrMissingGroupWithin: WbemErrorEnum = -2147217318
WbemErrorEnum_wbemErrMissingAggregationList: WbemErrorEnum = -2147217317
WbemErrorEnum_wbemErrPropertyNotAnObject: WbemErrorEnum = -2147217316
WbemErrorEnum_wbemErrAggregatingByObject: WbemErrorEnum = -2147217315
WbemErrorEnum_wbemErrUninterpretableProviderQuery: WbemErrorEnum = -2147217313
WbemErrorEnum_wbemErrBackupRestoreWinmgmtRunning: WbemErrorEnum = -2147217312
WbemErrorEnum_wbemErrQueueOverflow: WbemErrorEnum = -2147217311
WbemErrorEnum_wbemErrPrivilegeNotHeld: WbemErrorEnum = -2147217310
WbemErrorEnum_wbemErrInvalidOperator: WbemErrorEnum = -2147217309
WbemErrorEnum_wbemErrLocalCredentials: WbemErrorEnum = -2147217308
WbemErrorEnum_wbemErrCannotBeAbstract: WbemErrorEnum = -2147217307
WbemErrorEnum_wbemErrAmendedObject: WbemErrorEnum = -2147217306
WbemErrorEnum_wbemErrClientTooSlow: WbemErrorEnum = -2147217305
WbemErrorEnum_wbemErrNullSecurityDescriptor: WbemErrorEnum = -2147217304
WbemErrorEnum_wbemErrTimeout: WbemErrorEnum = -2147217303
WbemErrorEnum_wbemErrInvalidAssociation: WbemErrorEnum = -2147217302
WbemErrorEnum_wbemErrAmbiguousOperation: WbemErrorEnum = -2147217301
WbemErrorEnum_wbemErrQuotaViolation: WbemErrorEnum = -2147217300
WbemErrorEnum_wbemErrTransactionConflict: WbemErrorEnum = -2147217299
WbemErrorEnum_wbemErrForcedRollback: WbemErrorEnum = -2147217298
WbemErrorEnum_wbemErrUnsupportedLocale: WbemErrorEnum = -2147217297
WbemErrorEnum_wbemErrHandleOutOfDate: WbemErrorEnum = -2147217296
WbemErrorEnum_wbemErrConnectionFailed: WbemErrorEnum = -2147217295
WbemErrorEnum_wbemErrInvalidHandleRequest: WbemErrorEnum = -2147217294
WbemErrorEnum_wbemErrPropertyNameTooWide: WbemErrorEnum = -2147217293
WbemErrorEnum_wbemErrClassNameTooWide: WbemErrorEnum = -2147217292
WbemErrorEnum_wbemErrMethodNameTooWide: WbemErrorEnum = -2147217291
WbemErrorEnum_wbemErrQualifierNameTooWide: WbemErrorEnum = -2147217290
WbemErrorEnum_wbemErrRerunCommand: WbemErrorEnum = -2147217289
WbemErrorEnum_wbemErrDatabaseVerMismatch: WbemErrorEnum = -2147217288
WbemErrorEnum_wbemErrVetoPut: WbemErrorEnum = -2147217287
WbemErrorEnum_wbemErrVetoDelete: WbemErrorEnum = -2147217286
WbemErrorEnum_wbemErrInvalidLocale: WbemErrorEnum = -2147217280
WbemErrorEnum_wbemErrProviderSuspended: WbemErrorEnum = -2147217279
WbemErrorEnum_wbemErrSynchronizationRequired: WbemErrorEnum = -2147217278
WbemErrorEnum_wbemErrNoSchema: WbemErrorEnum = -2147217277
WbemErrorEnum_wbemErrProviderAlreadyRegistered: WbemErrorEnum = -2147217276
WbemErrorEnum_wbemErrProviderNotRegistered: WbemErrorEnum = -2147217275
WbemErrorEnum_wbemErrFatalTransportError: WbemErrorEnum = -2147217274
WbemErrorEnum_wbemErrEncryptedConnectionRequired: WbemErrorEnum = -2147217273
WbemErrorEnum_wbemErrRegistrationTooBroad: WbemErrorEnum = -2147213311
WbemErrorEnum_wbemErrRegistrationTooPrecise: WbemErrorEnum = -2147213310
WbemErrorEnum_wbemErrTimedout: WbemErrorEnum = -2147209215
WbemErrorEnum_wbemErrResetToDefault: WbemErrorEnum = -2147209214
WbemFlagEnum = Int32
WbemFlagEnum_wbemFlagReturnImmediately: WbemFlagEnum = 16
WbemFlagEnum_wbemFlagReturnWhenComplete: WbemFlagEnum = 0
WbemFlagEnum_wbemFlagBidirectional: WbemFlagEnum = 0
WbemFlagEnum_wbemFlagForwardOnly: WbemFlagEnum = 32
WbemFlagEnum_wbemFlagNoErrorObject: WbemFlagEnum = 64
WbemFlagEnum_wbemFlagReturnErrorObject: WbemFlagEnum = 0
WbemFlagEnum_wbemFlagSendStatus: WbemFlagEnum = 128
WbemFlagEnum_wbemFlagDontSendStatus: WbemFlagEnum = 0
WbemFlagEnum_wbemFlagEnsureLocatable: WbemFlagEnum = 256
WbemFlagEnum_wbemFlagDirectRead: WbemFlagEnum = 512
WbemFlagEnum_wbemFlagSendOnlySelected: WbemFlagEnum = 0
WbemFlagEnum_wbemFlagUseAmendedQualifiers: WbemFlagEnum = 131072
WbemFlagEnum_wbemFlagGetDefault: WbemFlagEnum = 0
WbemFlagEnum_wbemFlagSpawnInstance: WbemFlagEnum = 1
WbemFlagEnum_wbemFlagUseCurrentTime: WbemFlagEnum = 1
WbemImpersonationLevelEnum = Int32
WbemImpersonationLevelEnum_wbemImpersonationLevelAnonymous: WbemImpersonationLevelEnum = 1
WbemImpersonationLevelEnum_wbemImpersonationLevelIdentify: WbemImpersonationLevelEnum = 2
WbemImpersonationLevelEnum_wbemImpersonationLevelImpersonate: WbemImpersonationLevelEnum = 3
WbemImpersonationLevelEnum_wbemImpersonationLevelDelegate: WbemImpersonationLevelEnum = 4
WbemLevel1Login = Guid('8bc3f05e-d86b-11d0-a0-75-00-c0-4f-b6-88-20')
WbemLocalAddrRes = Guid('a1044801-8f7e-11d1-9e-7c-00-c0-4f-c3-24-a8')
WbemLocator = Guid('4590f811-1d3a-11d0-89-1f-00-aa-00-4b-2e-24')
WbemObjectTextFormatEnum = Int32
WbemObjectTextFormatEnum_wbemObjectTextFormatCIMDTD20: WbemObjectTextFormatEnum = 1
WbemObjectTextFormatEnum_wbemObjectTextFormatWMIDTD20: WbemObjectTextFormatEnum = 2
WbemObjectTextSrc = Guid('8d1c559d-84f0-4bb3-a7-d5-56-a7-43-5a-9b-a6')
WbemPrivilegeEnum = Int32
WbemPrivilegeEnum_wbemPrivilegeCreateToken: WbemPrivilegeEnum = 1
WbemPrivilegeEnum_wbemPrivilegePrimaryToken: WbemPrivilegeEnum = 2
WbemPrivilegeEnum_wbemPrivilegeLockMemory: WbemPrivilegeEnum = 3
WbemPrivilegeEnum_wbemPrivilegeIncreaseQuota: WbemPrivilegeEnum = 4
WbemPrivilegeEnum_wbemPrivilegeMachineAccount: WbemPrivilegeEnum = 5
WbemPrivilegeEnum_wbemPrivilegeTcb: WbemPrivilegeEnum = 6
WbemPrivilegeEnum_wbemPrivilegeSecurity: WbemPrivilegeEnum = 7
WbemPrivilegeEnum_wbemPrivilegeTakeOwnership: WbemPrivilegeEnum = 8
WbemPrivilegeEnum_wbemPrivilegeLoadDriver: WbemPrivilegeEnum = 9
WbemPrivilegeEnum_wbemPrivilegeSystemProfile: WbemPrivilegeEnum = 10
WbemPrivilegeEnum_wbemPrivilegeSystemtime: WbemPrivilegeEnum = 11
WbemPrivilegeEnum_wbemPrivilegeProfileSingleProcess: WbemPrivilegeEnum = 12
WbemPrivilegeEnum_wbemPrivilegeIncreaseBasePriority: WbemPrivilegeEnum = 13
WbemPrivilegeEnum_wbemPrivilegeCreatePagefile: WbemPrivilegeEnum = 14
WbemPrivilegeEnum_wbemPrivilegeCreatePermanent: WbemPrivilegeEnum = 15
WbemPrivilegeEnum_wbemPrivilegeBackup: WbemPrivilegeEnum = 16
WbemPrivilegeEnum_wbemPrivilegeRestore: WbemPrivilegeEnum = 17
WbemPrivilegeEnum_wbemPrivilegeShutdown: WbemPrivilegeEnum = 18
WbemPrivilegeEnum_wbemPrivilegeDebug: WbemPrivilegeEnum = 19
WbemPrivilegeEnum_wbemPrivilegeAudit: WbemPrivilegeEnum = 20
WbemPrivilegeEnum_wbemPrivilegeSystemEnvironment: WbemPrivilegeEnum = 21
WbemPrivilegeEnum_wbemPrivilegeChangeNotify: WbemPrivilegeEnum = 22
WbemPrivilegeEnum_wbemPrivilegeRemoteShutdown: WbemPrivilegeEnum = 23
WbemPrivilegeEnum_wbemPrivilegeUndock: WbemPrivilegeEnum = 24
WbemPrivilegeEnum_wbemPrivilegeSyncAgent: WbemPrivilegeEnum = 25
WbemPrivilegeEnum_wbemPrivilegeEnableDelegation: WbemPrivilegeEnum = 26
WbemPrivilegeEnum_wbemPrivilegeManageVolume: WbemPrivilegeEnum = 27
WbemQuery = Guid('eac8a024-21e2-4523-ad-73-a7-1a-0a-a2-f5-6a')
WbemQueryFlagEnum = Int32
WbemQueryFlagEnum_wbemQueryFlagDeep: WbemQueryFlagEnum = 0
WbemQueryFlagEnum_wbemQueryFlagShallow: WbemQueryFlagEnum = 1
WbemQueryFlagEnum_wbemQueryFlagPrototype: WbemQueryFlagEnum = 2
WbemRefresher = Guid('c71566f2-561e-11d1-ad-87-00-c0-4f-d8-fd-ff')
WBEMSTATUS = Int32
WBEM_NO_ERROR: WBEMSTATUS = 0
WBEM_S_NO_ERROR: WBEMSTATUS = 0
WBEM_S_SAME: WBEMSTATUS = 0
WBEM_S_FALSE: WBEMSTATUS = 1
WBEM_S_ALREADY_EXISTS: WBEMSTATUS = 262145
WBEM_S_RESET_TO_DEFAULT: WBEMSTATUS = 262146
WBEM_S_DIFFERENT: WBEMSTATUS = 262147
WBEM_S_TIMEDOUT: WBEMSTATUS = 262148
WBEM_S_NO_MORE_DATA: WBEMSTATUS = 262149
WBEM_S_OPERATION_CANCELLED: WBEMSTATUS = 262150
WBEM_S_PENDING: WBEMSTATUS = 262151
WBEM_S_DUPLICATE_OBJECTS: WBEMSTATUS = 262152
WBEM_S_ACCESS_DENIED: WBEMSTATUS = 262153
WBEM_S_PARTIAL_RESULTS: WBEMSTATUS = 262160
WBEM_S_SOURCE_NOT_AVAILABLE: WBEMSTATUS = 262167
WBEM_E_FAILED: WBEMSTATUS = -2147217407
WBEM_E_NOT_FOUND: WBEMSTATUS = -2147217406
WBEM_E_ACCESS_DENIED: WBEMSTATUS = -2147217405
WBEM_E_PROVIDER_FAILURE: WBEMSTATUS = -2147217404
WBEM_E_TYPE_MISMATCH: WBEMSTATUS = -2147217403
WBEM_E_OUT_OF_MEMORY: WBEMSTATUS = -2147217402
WBEM_E_INVALID_CONTEXT: WBEMSTATUS = -2147217401
WBEM_E_INVALID_PARAMETER: WBEMSTATUS = -2147217400
WBEM_E_NOT_AVAILABLE: WBEMSTATUS = -2147217399
WBEM_E_CRITICAL_ERROR: WBEMSTATUS = -2147217398
WBEM_E_INVALID_STREAM: WBEMSTATUS = -2147217397
WBEM_E_NOT_SUPPORTED: WBEMSTATUS = -2147217396
WBEM_E_INVALID_SUPERCLASS: WBEMSTATUS = -2147217395
WBEM_E_INVALID_NAMESPACE: WBEMSTATUS = -2147217394
WBEM_E_INVALID_OBJECT: WBEMSTATUS = -2147217393
WBEM_E_INVALID_CLASS: WBEMSTATUS = -2147217392
WBEM_E_PROVIDER_NOT_FOUND: WBEMSTATUS = -2147217391
WBEM_E_INVALID_PROVIDER_REGISTRATION: WBEMSTATUS = -2147217390
WBEM_E_PROVIDER_LOAD_FAILURE: WBEMSTATUS = -2147217389
WBEM_E_INITIALIZATION_FAILURE: WBEMSTATUS = -2147217388
WBEM_E_TRANSPORT_FAILURE: WBEMSTATUS = -2147217387
WBEM_E_INVALID_OPERATION: WBEMSTATUS = -2147217386
WBEM_E_INVALID_QUERY: WBEMSTATUS = -2147217385
WBEM_E_INVALID_QUERY_TYPE: WBEMSTATUS = -2147217384
WBEM_E_ALREADY_EXISTS: WBEMSTATUS = -2147217383
WBEM_E_OVERRIDE_NOT_ALLOWED: WBEMSTATUS = -2147217382
WBEM_E_PROPAGATED_QUALIFIER: WBEMSTATUS = -2147217381
WBEM_E_PROPAGATED_PROPERTY: WBEMSTATUS = -2147217380
WBEM_E_UNEXPECTED: WBEMSTATUS = -2147217379
WBEM_E_ILLEGAL_OPERATION: WBEMSTATUS = -2147217378
WBEM_E_CANNOT_BE_KEY: WBEMSTATUS = -2147217377
WBEM_E_INCOMPLETE_CLASS: WBEMSTATUS = -2147217376
WBEM_E_INVALID_SYNTAX: WBEMSTATUS = -2147217375
WBEM_E_NONDECORATED_OBJECT: WBEMSTATUS = -2147217374
WBEM_E_READ_ONLY: WBEMSTATUS = -2147217373
WBEM_E_PROVIDER_NOT_CAPABLE: WBEMSTATUS = -2147217372
WBEM_E_CLASS_HAS_CHILDREN: WBEMSTATUS = -2147217371
WBEM_E_CLASS_HAS_INSTANCES: WBEMSTATUS = -2147217370
WBEM_E_QUERY_NOT_IMPLEMENTED: WBEMSTATUS = -2147217369
WBEM_E_ILLEGAL_NULL: WBEMSTATUS = -2147217368
WBEM_E_INVALID_QUALIFIER_TYPE: WBEMSTATUS = -2147217367
WBEM_E_INVALID_PROPERTY_TYPE: WBEMSTATUS = -2147217366
WBEM_E_VALUE_OUT_OF_RANGE: WBEMSTATUS = -2147217365
WBEM_E_CANNOT_BE_SINGLETON: WBEMSTATUS = -2147217364
WBEM_E_INVALID_CIM_TYPE: WBEMSTATUS = -2147217363
WBEM_E_INVALID_METHOD: WBEMSTATUS = -2147217362
WBEM_E_INVALID_METHOD_PARAMETERS: WBEMSTATUS = -2147217361
WBEM_E_SYSTEM_PROPERTY: WBEMSTATUS = -2147217360
WBEM_E_INVALID_PROPERTY: WBEMSTATUS = -2147217359
WBEM_E_CALL_CANCELLED: WBEMSTATUS = -2147217358
WBEM_E_SHUTTING_DOWN: WBEMSTATUS = -2147217357
WBEM_E_PROPAGATED_METHOD: WBEMSTATUS = -2147217356
WBEM_E_UNSUPPORTED_PARAMETER: WBEMSTATUS = -2147217355
WBEM_E_MISSING_PARAMETER_ID: WBEMSTATUS = -2147217354
WBEM_E_INVALID_PARAMETER_ID: WBEMSTATUS = -2147217353
WBEM_E_NONCONSECUTIVE_PARAMETER_IDS: WBEMSTATUS = -2147217352
WBEM_E_PARAMETER_ID_ON_RETVAL: WBEMSTATUS = -2147217351
WBEM_E_INVALID_OBJECT_PATH: WBEMSTATUS = -2147217350
WBEM_E_OUT_OF_DISK_SPACE: WBEMSTATUS = -2147217349
WBEM_E_BUFFER_TOO_SMALL: WBEMSTATUS = -2147217348
WBEM_E_UNSUPPORTED_PUT_EXTENSION: WBEMSTATUS = -2147217347
WBEM_E_UNKNOWN_OBJECT_TYPE: WBEMSTATUS = -2147217346
WBEM_E_UNKNOWN_PACKET_TYPE: WBEMSTATUS = -2147217345
WBEM_E_MARSHAL_VERSION_MISMATCH: WBEMSTATUS = -2147217344
WBEM_E_MARSHAL_INVALID_SIGNATURE: WBEMSTATUS = -2147217343
WBEM_E_INVALID_QUALIFIER: WBEMSTATUS = -2147217342
WBEM_E_INVALID_DUPLICATE_PARAMETER: WBEMSTATUS = -2147217341
WBEM_E_TOO_MUCH_DATA: WBEMSTATUS = -2147217340
WBEM_E_SERVER_TOO_BUSY: WBEMSTATUS = -2147217339
WBEM_E_INVALID_FLAVOR: WBEMSTATUS = -2147217338
WBEM_E_CIRCULAR_REFERENCE: WBEMSTATUS = -2147217337
WBEM_E_UNSUPPORTED_CLASS_UPDATE: WBEMSTATUS = -2147217336
WBEM_E_CANNOT_CHANGE_KEY_INHERITANCE: WBEMSTATUS = -2147217335
WBEM_E_CANNOT_CHANGE_INDEX_INHERITANCE: WBEMSTATUS = -2147217328
WBEM_E_TOO_MANY_PROPERTIES: WBEMSTATUS = -2147217327
WBEM_E_UPDATE_TYPE_MISMATCH: WBEMSTATUS = -2147217326
WBEM_E_UPDATE_OVERRIDE_NOT_ALLOWED: WBEMSTATUS = -2147217325
WBEM_E_UPDATE_PROPAGATED_METHOD: WBEMSTATUS = -2147217324
WBEM_E_METHOD_NOT_IMPLEMENTED: WBEMSTATUS = -2147217323
WBEM_E_METHOD_DISABLED: WBEMSTATUS = -2147217322
WBEM_E_REFRESHER_BUSY: WBEMSTATUS = -2147217321
WBEM_E_UNPARSABLE_QUERY: WBEMSTATUS = -2147217320
WBEM_E_NOT_EVENT_CLASS: WBEMSTATUS = -2147217319
WBEM_E_MISSING_GROUP_WITHIN: WBEMSTATUS = -2147217318
WBEM_E_MISSING_AGGREGATION_LIST: WBEMSTATUS = -2147217317
WBEM_E_PROPERTY_NOT_AN_OBJECT: WBEMSTATUS = -2147217316
WBEM_E_AGGREGATING_BY_OBJECT: WBEMSTATUS = -2147217315
WBEM_E_UNINTERPRETABLE_PROVIDER_QUERY: WBEMSTATUS = -2147217313
WBEM_E_BACKUP_RESTORE_WINMGMT_RUNNING: WBEMSTATUS = -2147217312
WBEM_E_QUEUE_OVERFLOW: WBEMSTATUS = -2147217311
WBEM_E_PRIVILEGE_NOT_HELD: WBEMSTATUS = -2147217310
WBEM_E_INVALID_OPERATOR: WBEMSTATUS = -2147217309
WBEM_E_LOCAL_CREDENTIALS: WBEMSTATUS = -2147217308
WBEM_E_CANNOT_BE_ABSTRACT: WBEMSTATUS = -2147217307
WBEM_E_AMENDED_OBJECT: WBEMSTATUS = -2147217306
WBEM_E_CLIENT_TOO_SLOW: WBEMSTATUS = -2147217305
WBEM_E_NULL_SECURITY_DESCRIPTOR: WBEMSTATUS = -2147217304
WBEM_E_TIMED_OUT: WBEMSTATUS = -2147217303
WBEM_E_INVALID_ASSOCIATION: WBEMSTATUS = -2147217302
WBEM_E_AMBIGUOUS_OPERATION: WBEMSTATUS = -2147217301
WBEM_E_QUOTA_VIOLATION: WBEMSTATUS = -2147217300
WBEM_E_RESERVED_001: WBEMSTATUS = -2147217299
WBEM_E_RESERVED_002: WBEMSTATUS = -2147217298
WBEM_E_UNSUPPORTED_LOCALE: WBEMSTATUS = -2147217297
WBEM_E_HANDLE_OUT_OF_DATE: WBEMSTATUS = -2147217296
WBEM_E_CONNECTION_FAILED: WBEMSTATUS = -2147217295
WBEM_E_INVALID_HANDLE_REQUEST: WBEMSTATUS = -2147217294
WBEM_E_PROPERTY_NAME_TOO_WIDE: WBEMSTATUS = -2147217293
WBEM_E_CLASS_NAME_TOO_WIDE: WBEMSTATUS = -2147217292
WBEM_E_METHOD_NAME_TOO_WIDE: WBEMSTATUS = -2147217291
WBEM_E_QUALIFIER_NAME_TOO_WIDE: WBEMSTATUS = -2147217290
WBEM_E_RERUN_COMMAND: WBEMSTATUS = -2147217289
WBEM_E_DATABASE_VER_MISMATCH: WBEMSTATUS = -2147217288
WBEM_E_VETO_DELETE: WBEMSTATUS = -2147217287
WBEM_E_VETO_PUT: WBEMSTATUS = -2147217286
WBEM_E_INVALID_LOCALE: WBEMSTATUS = -2147217280
WBEM_E_PROVIDER_SUSPENDED: WBEMSTATUS = -2147217279
WBEM_E_SYNCHRONIZATION_REQUIRED: WBEMSTATUS = -2147217278
WBEM_E_NO_SCHEMA: WBEMSTATUS = -2147217277
WBEM_E_PROVIDER_ALREADY_REGISTERED: WBEMSTATUS = -2147217276
WBEM_E_PROVIDER_NOT_REGISTERED: WBEMSTATUS = -2147217275
WBEM_E_FATAL_TRANSPORT_ERROR: WBEMSTATUS = -2147217274
WBEM_E_ENCRYPTED_CONNECTION_REQUIRED: WBEMSTATUS = -2147217273
WBEM_E_PROVIDER_TIMED_OUT: WBEMSTATUS = -2147217272
WBEM_E_NO_KEY: WBEMSTATUS = -2147217271
WBEM_E_PROVIDER_DISABLED: WBEMSTATUS = -2147217270
WBEMESS_E_REGISTRATION_TOO_BROAD: WBEMSTATUS = -2147213311
WBEMESS_E_REGISTRATION_TOO_PRECISE: WBEMSTATUS = -2147213310
WBEMESS_E_AUTHZ_NOT_PRIVILEGED: WBEMSTATUS = -2147213309
WBEMMOF_E_EXPECTED_QUALIFIER_NAME: WBEMSTATUS = -2147205119
WBEMMOF_E_EXPECTED_SEMI: WBEMSTATUS = -2147205118
WBEMMOF_E_EXPECTED_OPEN_BRACE: WBEMSTATUS = -2147205117
WBEMMOF_E_EXPECTED_CLOSE_BRACE: WBEMSTATUS = -2147205116
WBEMMOF_E_EXPECTED_CLOSE_BRACKET: WBEMSTATUS = -2147205115
WBEMMOF_E_EXPECTED_CLOSE_PAREN: WBEMSTATUS = -2147205114
WBEMMOF_E_ILLEGAL_CONSTANT_VALUE: WBEMSTATUS = -2147205113
WBEMMOF_E_EXPECTED_TYPE_IDENTIFIER: WBEMSTATUS = -2147205112
WBEMMOF_E_EXPECTED_OPEN_PAREN: WBEMSTATUS = -2147205111
WBEMMOF_E_UNRECOGNIZED_TOKEN: WBEMSTATUS = -2147205110
WBEMMOF_E_UNRECOGNIZED_TYPE: WBEMSTATUS = -2147205109
WBEMMOF_E_EXPECTED_PROPERTY_NAME: WBEMSTATUS = -2147205108
WBEMMOF_E_TYPEDEF_NOT_SUPPORTED: WBEMSTATUS = -2147205107
WBEMMOF_E_UNEXPECTED_ALIAS: WBEMSTATUS = -2147205106
WBEMMOF_E_UNEXPECTED_ARRAY_INIT: WBEMSTATUS = -2147205105
WBEMMOF_E_INVALID_AMENDMENT_SYNTAX: WBEMSTATUS = -2147205104
WBEMMOF_E_INVALID_DUPLICATE_AMENDMENT: WBEMSTATUS = -2147205103
WBEMMOF_E_INVALID_PRAGMA: WBEMSTATUS = -2147205102
WBEMMOF_E_INVALID_NAMESPACE_SYNTAX: WBEMSTATUS = -2147205101
WBEMMOF_E_EXPECTED_CLASS_NAME: WBEMSTATUS = -2147205100
WBEMMOF_E_TYPE_MISMATCH: WBEMSTATUS = -2147205099
WBEMMOF_E_EXPECTED_ALIAS_NAME: WBEMSTATUS = -2147205098
WBEMMOF_E_INVALID_CLASS_DECLARATION: WBEMSTATUS = -2147205097
WBEMMOF_E_INVALID_INSTANCE_DECLARATION: WBEMSTATUS = -2147205096
WBEMMOF_E_EXPECTED_DOLLAR: WBEMSTATUS = -2147205095
WBEMMOF_E_CIMTYPE_QUALIFIER: WBEMSTATUS = -2147205094
WBEMMOF_E_DUPLICATE_PROPERTY: WBEMSTATUS = -2147205093
WBEMMOF_E_INVALID_NAMESPACE_SPECIFICATION: WBEMSTATUS = -2147205092
WBEMMOF_E_OUT_OF_RANGE: WBEMSTATUS = -2147205091
WBEMMOF_E_INVALID_FILE: WBEMSTATUS = -2147205090
WBEMMOF_E_ALIASES_IN_EMBEDDED: WBEMSTATUS = -2147205089
WBEMMOF_E_NULL_ARRAY_ELEM: WBEMSTATUS = -2147205088
WBEMMOF_E_DUPLICATE_QUALIFIER: WBEMSTATUS = -2147205087
WBEMMOF_E_EXPECTED_FLAVOR_TYPE: WBEMSTATUS = -2147205086
WBEMMOF_E_INCOMPATIBLE_FLAVOR_TYPES: WBEMSTATUS = -2147205085
WBEMMOF_E_MULTIPLE_ALIASES: WBEMSTATUS = -2147205084
WBEMMOF_E_INCOMPATIBLE_FLAVOR_TYPES2: WBEMSTATUS = -2147205083
WBEMMOF_E_NO_ARRAYS_RETURNED: WBEMSTATUS = -2147205082
WBEMMOF_E_MUST_BE_IN_OR_OUT: WBEMSTATUS = -2147205081
WBEMMOF_E_INVALID_FLAGS_SYNTAX: WBEMSTATUS = -2147205080
WBEMMOF_E_EXPECTED_BRACE_OR_BAD_TYPE: WBEMSTATUS = -2147205079
WBEMMOF_E_UNSUPPORTED_CIMV22_QUAL_VALUE: WBEMSTATUS = -2147205078
WBEMMOF_E_UNSUPPORTED_CIMV22_DATA_TYPE: WBEMSTATUS = -2147205077
WBEMMOF_E_INVALID_DELETEINSTANCE_SYNTAX: WBEMSTATUS = -2147205076
WBEMMOF_E_INVALID_QUALIFIER_SYNTAX: WBEMSTATUS = -2147205075
WBEMMOF_E_QUALIFIER_USED_OUTSIDE_SCOPE: WBEMSTATUS = -2147205074
WBEMMOF_E_ERROR_CREATING_TEMP_FILE: WBEMSTATUS = -2147205073
WBEMMOF_E_ERROR_INVALID_INCLUDE_FILE: WBEMSTATUS = -2147205072
WBEMMOF_E_INVALID_DELETECLASS_SYNTAX: WBEMSTATUS = -2147205071
WBEMSTATUS_FORMAT = Int32
WBEMSTATUS_FORMAT_NEWLINE: WBEMSTATUS_FORMAT = 0
WBEMSTATUS_FORMAT_NO_NEWLINE: WBEMSTATUS_FORMAT = 1
WbemStatusCodeText = Guid('eb87e1bd-3233-11d2-ae-c9-00-c0-4f-b6-88-20')
WbemTextFlagEnum = Int32
WbemTextFlagEnum_wbemTextFlagNoFlavors: WbemTextFlagEnum = 1
WbemTimeout = Int32
WbemTimeout_wbemTimeoutInfinite: WbemTimeout = -1
WbemUnauthenticatedLocator = Guid('443e7b79-de31-11d2-b3-40-00-10-4b-cc-4b-4a')
WbemUninitializedClassObject = Guid('7a0227f6-7108-11d1-ad-90-00-c0-4f-d8-fd-ff')
WMI_OBJ_TEXT = Int32
WMI_OBJ_TEXT_CIM_DTD_2_0: WMI_OBJ_TEXT = 1
WMI_OBJ_TEXT_WMI_DTD_2_0: WMI_OBJ_TEXT = 2
WMI_OBJ_TEXT_WMI_EXT1: WMI_OBJ_TEXT = 3
WMI_OBJ_TEXT_WMI_EXT2: WMI_OBJ_TEXT = 4
WMI_OBJ_TEXT_WMI_EXT3: WMI_OBJ_TEXT = 5
WMI_OBJ_TEXT_WMI_EXT4: WMI_OBJ_TEXT = 6
WMI_OBJ_TEXT_WMI_EXT5: WMI_OBJ_TEXT = 7
WMI_OBJ_TEXT_WMI_EXT6: WMI_OBJ_TEXT = 8
WMI_OBJ_TEXT_WMI_EXT7: WMI_OBJ_TEXT = 9
WMI_OBJ_TEXT_WMI_EXT8: WMI_OBJ_TEXT = 10
WMI_OBJ_TEXT_WMI_EXT9: WMI_OBJ_TEXT = 11
WMI_OBJ_TEXT_WMI_EXT10: WMI_OBJ_TEXT = 12
WMI_OBJ_TEXT_LAST: WMI_OBJ_TEXT = 13
WMIExtension = Guid('f0975afe-5c7f-11d2-8b-74-00-10-4b-2a-fb-41')
WMIQ_ANALYSIS_TYPE = Int32
WMIQ_ANALYSIS_RPN_SEQUENCE: WMIQ_ANALYSIS_TYPE = 1
WMIQ_ANALYSIS_ASSOC_QUERY: WMIQ_ANALYSIS_TYPE = 2
WMIQ_ANALYSIS_PROP_ANALYSIS_MATRIX: WMIQ_ANALYSIS_TYPE = 3
WMIQ_ANALYSIS_QUERY_TEXT: WMIQ_ANALYSIS_TYPE = 4
WMIQ_ANALYSIS_RESERVED: WMIQ_ANALYSIS_TYPE = 134217728
WMIQ_ASSOCQ_FLAGS = Int32
WMIQ_ASSOCQ_ASSOCIATORS: WMIQ_ASSOCQ_FLAGS = 1
WMIQ_ASSOCQ_REFERENCES: WMIQ_ASSOCQ_FLAGS = 2
WMIQ_ASSOCQ_RESULTCLASS: WMIQ_ASSOCQ_FLAGS = 4
WMIQ_ASSOCQ_ASSOCCLASS: WMIQ_ASSOCQ_FLAGS = 8
WMIQ_ASSOCQ_ROLE: WMIQ_ASSOCQ_FLAGS = 16
WMIQ_ASSOCQ_RESULTROLE: WMIQ_ASSOCQ_FLAGS = 32
WMIQ_ASSOCQ_REQUIREDQUALIFIER: WMIQ_ASSOCQ_FLAGS = 64
WMIQ_ASSOCQ_REQUIREDASSOCQUALIFIER: WMIQ_ASSOCQ_FLAGS = 128
WMIQ_ASSOCQ_CLASSDEFSONLY: WMIQ_ASSOCQ_FLAGS = 256
WMIQ_ASSOCQ_KEYSONLY: WMIQ_ASSOCQ_FLAGS = 512
WMIQ_ASSOCQ_SCHEMAONLY: WMIQ_ASSOCQ_FLAGS = 1024
WMIQ_ASSOCQ_CLASSREFSONLY: WMIQ_ASSOCQ_FLAGS = 2048
WMIQ_LANGUAGE_FEATURES = Int32
WMIQ_LF1_BASIC_SELECT: WMIQ_LANGUAGE_FEATURES = 1
WMIQ_LF2_CLASS_NAME_IN_QUERY: WMIQ_LANGUAGE_FEATURES = 2
WMIQ_LF3_STRING_CASE_FUNCTIONS: WMIQ_LANGUAGE_FEATURES = 3
WMIQ_LF4_PROP_TO_PROP_TESTS: WMIQ_LANGUAGE_FEATURES = 4
WMIQ_LF5_COUNT_STAR: WMIQ_LANGUAGE_FEATURES = 5
WMIQ_LF6_ORDER_BY: WMIQ_LANGUAGE_FEATURES = 6
WMIQ_LF7_DISTINCT: WMIQ_LANGUAGE_FEATURES = 7
WMIQ_LF8_ISA: WMIQ_LANGUAGE_FEATURES = 8
WMIQ_LF9_THIS: WMIQ_LANGUAGE_FEATURES = 9
WMIQ_LF10_COMPEX_SUBEXPRESSIONS: WMIQ_LANGUAGE_FEATURES = 10
WMIQ_LF11_ALIASING: WMIQ_LANGUAGE_FEATURES = 11
WMIQ_LF12_GROUP_BY_HAVING: WMIQ_LANGUAGE_FEATURES = 12
WMIQ_LF13_WMI_WITHIN: WMIQ_LANGUAGE_FEATURES = 13
WMIQ_LF14_SQL_WRITE_OPERATIONS: WMIQ_LANGUAGE_FEATURES = 14
WMIQ_LF15_GO: WMIQ_LANGUAGE_FEATURES = 15
WMIQ_LF16_SINGLE_LEVEL_TRANSACTIONS: WMIQ_LANGUAGE_FEATURES = 16
WMIQ_LF17_QUALIFIED_NAMES: WMIQ_LANGUAGE_FEATURES = 17
WMIQ_LF18_ASSOCIATONS: WMIQ_LANGUAGE_FEATURES = 18
WMIQ_LF19_SYSTEM_PROPERTIES: WMIQ_LANGUAGE_FEATURES = 19
WMIQ_LF20_EXTENDED_SYSTEM_PROPERTIES: WMIQ_LANGUAGE_FEATURES = 20
WMIQ_LF21_SQL89_JOINS: WMIQ_LANGUAGE_FEATURES = 21
WMIQ_LF22_SQL92_JOINS: WMIQ_LANGUAGE_FEATURES = 22
WMIQ_LF23_SUBSELECTS: WMIQ_LANGUAGE_FEATURES = 23
WMIQ_LF24_UMI_EXTENSIONS: WMIQ_LANGUAGE_FEATURES = 24
WMIQ_LF25_DATEPART: WMIQ_LANGUAGE_FEATURES = 25
WMIQ_LF26_LIKE: WMIQ_LANGUAGE_FEATURES = 26
WMIQ_LF27_CIM_TEMPORAL_CONSTRUCTS: WMIQ_LANGUAGE_FEATURES = 27
WMIQ_LF28_STANDARD_AGGREGATES: WMIQ_LANGUAGE_FEATURES = 28
WMIQ_LF29_MULTI_LEVEL_ORDER_BY: WMIQ_LANGUAGE_FEATURES = 29
WMIQ_LF30_WMI_PRAGMAS: WMIQ_LANGUAGE_FEATURES = 30
WMIQ_LF31_QUALIFIER_TESTS: WMIQ_LANGUAGE_FEATURES = 31
WMIQ_LF32_SP_EXECUTE: WMIQ_LANGUAGE_FEATURES = 32
WMIQ_LF33_ARRAY_ACCESS: WMIQ_LANGUAGE_FEATURES = 33
WMIQ_LF34_UNION: WMIQ_LANGUAGE_FEATURES = 34
WMIQ_LF35_COMPLEX_SELECT_TARGET: WMIQ_LANGUAGE_FEATURES = 35
WMIQ_LF36_REFERENCE_TESTS: WMIQ_LANGUAGE_FEATURES = 36
WMIQ_LF37_SELECT_INTO: WMIQ_LANGUAGE_FEATURES = 37
WMIQ_LF38_BASIC_DATETIME_TESTS: WMIQ_LANGUAGE_FEATURES = 38
WMIQ_LF39_COUNT_COLUMN: WMIQ_LANGUAGE_FEATURES = 39
WMIQ_LF40_BETWEEN: WMIQ_LANGUAGE_FEATURES = 40
WMIQ_LF_LAST: WMIQ_LANGUAGE_FEATURES = 40
WMIQ_RPN_TOKEN_FLAGS = Int32
WMIQ_RPN_TOKEN_EXPRESSION: WMIQ_RPN_TOKEN_FLAGS = 1
WMIQ_RPN_TOKEN_AND: WMIQ_RPN_TOKEN_FLAGS = 2
WMIQ_RPN_TOKEN_OR: WMIQ_RPN_TOKEN_FLAGS = 3
WMIQ_RPN_TOKEN_NOT: WMIQ_RPN_TOKEN_FLAGS = 4
WMIQ_RPN_OP_UNDEFINED: WMIQ_RPN_TOKEN_FLAGS = 0
WMIQ_RPN_OP_EQ: WMIQ_RPN_TOKEN_FLAGS = 1
WMIQ_RPN_OP_NE: WMIQ_RPN_TOKEN_FLAGS = 2
WMIQ_RPN_OP_GE: WMIQ_RPN_TOKEN_FLAGS = 3
WMIQ_RPN_OP_LE: WMIQ_RPN_TOKEN_FLAGS = 4
WMIQ_RPN_OP_LT: WMIQ_RPN_TOKEN_FLAGS = 5
WMIQ_RPN_OP_GT: WMIQ_RPN_TOKEN_FLAGS = 6
WMIQ_RPN_OP_LIKE: WMIQ_RPN_TOKEN_FLAGS = 7
WMIQ_RPN_OP_ISA: WMIQ_RPN_TOKEN_FLAGS = 8
WMIQ_RPN_OP_ISNOTA: WMIQ_RPN_TOKEN_FLAGS = 9
WMIQ_RPN_OP_ISNULL: WMIQ_RPN_TOKEN_FLAGS = 10
WMIQ_RPN_OP_ISNOTNULL: WMIQ_RPN_TOKEN_FLAGS = 11
WMIQ_RPN_LEFT_PROPERTY_NAME: WMIQ_RPN_TOKEN_FLAGS = 1
WMIQ_RPN_RIGHT_PROPERTY_NAME: WMIQ_RPN_TOKEN_FLAGS = 2
WMIQ_RPN_CONST2: WMIQ_RPN_TOKEN_FLAGS = 4
WMIQ_RPN_CONST: WMIQ_RPN_TOKEN_FLAGS = 8
WMIQ_RPN_RELOP: WMIQ_RPN_TOKEN_FLAGS = 16
WMIQ_RPN_LEFT_FUNCTION: WMIQ_RPN_TOKEN_FLAGS = 32
WMIQ_RPN_RIGHT_FUNCTION: WMIQ_RPN_TOKEN_FLAGS = 64
WMIQ_RPN_GET_TOKEN_TYPE: WMIQ_RPN_TOKEN_FLAGS = 1
WMIQ_RPN_GET_EXPR_SHAPE: WMIQ_RPN_TOKEN_FLAGS = 2
WMIQ_RPN_GET_LEFT_FUNCTION: WMIQ_RPN_TOKEN_FLAGS = 3
WMIQ_RPN_GET_RIGHT_FUNCTION: WMIQ_RPN_TOKEN_FLAGS = 4
WMIQ_RPN_GET_RELOP: WMIQ_RPN_TOKEN_FLAGS = 5
WMIQ_RPN_NEXT_TOKEN: WMIQ_RPN_TOKEN_FLAGS = 1
WMIQ_RPN_FROM_UNARY: WMIQ_RPN_TOKEN_FLAGS = 1
WMIQ_RPN_FROM_PATH: WMIQ_RPN_TOKEN_FLAGS = 2
WMIQ_RPN_FROM_CLASS_LIST: WMIQ_RPN_TOKEN_FLAGS = 4
WMIQ_RPN_FROM_MULTIPLE: WMIQ_RPN_TOKEN_FLAGS = 8
WMIQ_RPNF_FEATURE = Int32
WMIQ_RPNF_WHERE_CLAUSE_PRESENT: WMIQ_RPNF_FEATURE = 1
WMIQ_RPNF_QUERY_IS_CONJUNCTIVE: WMIQ_RPNF_FEATURE = 2
WMIQ_RPNF_QUERY_IS_DISJUNCTIVE: WMIQ_RPNF_FEATURE = 4
WMIQ_RPNF_PROJECTION: WMIQ_RPNF_FEATURE = 8
WMIQ_RPNF_FEATURE_SELECT_STAR: WMIQ_RPNF_FEATURE = 16
WMIQ_RPNF_EQUALITY_TESTS_ONLY: WMIQ_RPNF_FEATURE = 32
WMIQ_RPNF_COUNT_STAR: WMIQ_RPNF_FEATURE = 64
WMIQ_RPNF_QUALIFIED_NAMES_USED: WMIQ_RPNF_FEATURE = 128
WMIQ_RPNF_SYSPROP_CLASS_USED: WMIQ_RPNF_FEATURE = 256
WMIQ_RPNF_PROP_TO_PROP_TESTS: WMIQ_RPNF_FEATURE = 512
WMIQ_RPNF_ORDER_BY: WMIQ_RPNF_FEATURE = 1024
WMIQ_RPNF_ISA_USED: WMIQ_RPNF_FEATURE = 2048
WMIQ_RPNF_GROUP_BY_HAVING: WMIQ_RPNF_FEATURE = 4096
WMIQ_RPNF_ARRAY_ACCESS_USED: WMIQ_RPNF_FEATURE = 8192
make_head(_module, 'IEnumWbemClassObject')
make_head(_module, 'IMofCompiler')
make_head(_module, 'ISWbemDateTime')
make_head(_module, 'ISWbemEventSource')
make_head(_module, 'ISWbemLastError')
make_head(_module, 'ISWbemLocator')
make_head(_module, 'ISWbemMethod')
make_head(_module, 'ISWbemMethodSet')
make_head(_module, 'ISWbemNamedValue')
make_head(_module, 'ISWbemNamedValueSet')
make_head(_module, 'ISWbemObject')
make_head(_module, 'ISWbemObjectEx')
make_head(_module, 'ISWbemObjectPath')
make_head(_module, 'ISWbemObjectSet')
make_head(_module, 'ISWbemPrivilege')
make_head(_module, 'ISWbemPrivilegeSet')
make_head(_module, 'ISWbemProperty')
make_head(_module, 'ISWbemPropertySet')
make_head(_module, 'ISWbemQualifier')
make_head(_module, 'ISWbemQualifierSet')
make_head(_module, 'ISWbemRefreshableItem')
make_head(_module, 'ISWbemRefresher')
make_head(_module, 'ISWbemSecurity')
make_head(_module, 'ISWbemServices')
make_head(_module, 'ISWbemServicesEx')
make_head(_module, 'ISWbemSink')
make_head(_module, 'ISWbemSinkEvents')
make_head(_module, 'IUnsecuredApartment')
make_head(_module, 'IWbemAddressResolution')
make_head(_module, 'IWbemBackupRestore')
make_head(_module, 'IWbemBackupRestoreEx')
make_head(_module, 'IWbemCallResult')
make_head(_module, 'IWbemClassObject')
make_head(_module, 'IWbemClientConnectionTransport')
make_head(_module, 'IWbemClientTransport')
make_head(_module, 'IWbemConfigureRefresher')
make_head(_module, 'IWbemConnectorLogin')
make_head(_module, 'IWbemConstructClassObject')
make_head(_module, 'IWbemContext')
make_head(_module, 'IWbemDecoupledBasicEventProvider')
make_head(_module, 'IWbemDecoupledRegistrar')
make_head(_module, 'IWbemEventConsumerProvider')
make_head(_module, 'IWbemEventProvider')
make_head(_module, 'IWbemEventProviderQuerySink')
make_head(_module, 'IWbemEventProviderSecurity')
make_head(_module, 'IWbemEventSink')
make_head(_module, 'IWbemHiPerfEnum')
make_head(_module, 'IWbemHiPerfProvider')
make_head(_module, 'IWbemLevel1Login')
make_head(_module, 'IWbemLocator')
make_head(_module, 'IWbemObjectAccess')
make_head(_module, 'IWbemObjectSink')
make_head(_module, 'IWbemObjectSinkEx')
make_head(_module, 'IWbemObjectTextSrc')
make_head(_module, 'IWbemPath')
make_head(_module, 'IWbemPathKeyList')
make_head(_module, 'IWbemPropertyProvider')
make_head(_module, 'IWbemProviderIdentity')
make_head(_module, 'IWbemProviderInit')
make_head(_module, 'IWbemProviderInitSink')
make_head(_module, 'IWbemQualifierSet')
make_head(_module, 'IWbemQuery')
make_head(_module, 'IWbemRefresher')
make_head(_module, 'IWbemServices')
make_head(_module, 'IWbemShutdown')
make_head(_module, 'IWbemStatusCodeText')
make_head(_module, 'IWbemTransport')
make_head(_module, 'IWbemUnboundObjectSink')
make_head(_module, 'IWbemUnsecuredApartment')
make_head(_module, 'IWMIExtension')
make_head(_module, 'MI_Application')
make_head(_module, 'MI_ApplicationFT')
make_head(_module, 'MI_Array')
make_head(_module, 'MI_ArrayField')
make_head(_module, 'MI_BooleanA')
make_head(_module, 'MI_BooleanAField')
make_head(_module, 'MI_BooleanField')
make_head(_module, 'MI_CancelCallback')
make_head(_module, 'MI_Char16A')
make_head(_module, 'MI_Char16AField')
make_head(_module, 'MI_Char16Field')
make_head(_module, 'MI_Class')
make_head(_module, 'MI_ClassDecl')
make_head(_module, 'MI_ClassFT')
make_head(_module, 'MI_ClientFT_V1')
make_head(_module, 'MI_ConstBooleanA')
make_head(_module, 'MI_ConstBooleanAField')
make_head(_module, 'MI_ConstBooleanField')
make_head(_module, 'MI_ConstChar16A')
make_head(_module, 'MI_ConstChar16AField')
make_head(_module, 'MI_ConstChar16Field')
make_head(_module, 'MI_ConstDatetimeA')
make_head(_module, 'MI_ConstDatetimeAField')
make_head(_module, 'MI_ConstDatetimeField')
make_head(_module, 'MI_ConstInstanceA')
make_head(_module, 'MI_ConstInstanceAField')
make_head(_module, 'MI_ConstInstanceField')
make_head(_module, 'MI_ConstReal32A')
make_head(_module, 'MI_ConstReal32AField')
make_head(_module, 'MI_ConstReal32Field')
make_head(_module, 'MI_ConstReal64A')
make_head(_module, 'MI_ConstReal64AField')
make_head(_module, 'MI_ConstReal64Field')
make_head(_module, 'MI_ConstReferenceA')
make_head(_module, 'MI_ConstReferenceAField')
make_head(_module, 'MI_ConstReferenceField')
make_head(_module, 'MI_ConstSint16A')
make_head(_module, 'MI_ConstSint16AField')
make_head(_module, 'MI_ConstSint16Field')
make_head(_module, 'MI_ConstSint32A')
make_head(_module, 'MI_ConstSint32AField')
make_head(_module, 'MI_ConstSint32Field')
make_head(_module, 'MI_ConstSint64A')
make_head(_module, 'MI_ConstSint64AField')
make_head(_module, 'MI_ConstSint64Field')
make_head(_module, 'MI_ConstSint8A')
make_head(_module, 'MI_ConstSint8AField')
make_head(_module, 'MI_ConstSint8Field')
make_head(_module, 'MI_ConstStringA')
make_head(_module, 'MI_ConstStringAField')
make_head(_module, 'MI_ConstStringField')
make_head(_module, 'MI_ConstUint16A')
make_head(_module, 'MI_ConstUint16AField')
make_head(_module, 'MI_ConstUint16Field')
make_head(_module, 'MI_ConstUint32A')
make_head(_module, 'MI_ConstUint32AField')
make_head(_module, 'MI_ConstUint32Field')
make_head(_module, 'MI_ConstUint64A')
make_head(_module, 'MI_ConstUint64AField')
make_head(_module, 'MI_ConstUint64Field')
make_head(_module, 'MI_ConstUint8A')
make_head(_module, 'MI_ConstUint8AField')
make_head(_module, 'MI_ConstUint8Field')
make_head(_module, 'MI_Context')
make_head(_module, 'MI_ContextFT')
make_head(_module, 'MI_Datetime')
make_head(_module, 'MI_DatetimeA')
make_head(_module, 'MI_DatetimeAField')
make_head(_module, 'MI_DatetimeField')
make_head(_module, 'MI_Deserializer')
make_head(_module, 'MI_Deserializer_ClassObjectNeeded')
make_head(_module, 'MI_DeserializerFT')
make_head(_module, 'MI_DestinationOptions')
make_head(_module, 'MI_DestinationOptionsFT')
make_head(_module, 'MI_FeatureDecl')
make_head(_module, 'MI_Filter')
make_head(_module, 'MI_FilterFT')
make_head(_module, 'MI_HostedProvider')
make_head(_module, 'MI_HostedProviderFT')
make_head(_module, 'MI_Instance')
make_head(_module, 'MI_InstanceA')
make_head(_module, 'MI_InstanceAField')
make_head(_module, 'MI_InstanceExFT')
make_head(_module, 'MI_InstanceField')
make_head(_module, 'MI_InstanceFT')
make_head(_module, 'MI_Interval')
make_head(_module, 'MI_MainFunction')
make_head(_module, 'MI_MethodDecl')
make_head(_module, 'MI_MethodDecl_Invoke')
make_head(_module, 'MI_Module')
make_head(_module, 'MI_Module_Load')
make_head(_module, 'MI_Module_Self')
make_head(_module, 'MI_Module_Unload')
make_head(_module, 'MI_ObjectDecl')
make_head(_module, 'MI_Operation')
make_head(_module, 'MI_OperationCallback_Class')
make_head(_module, 'MI_OperationCallback_Indication')
make_head(_module, 'MI_OperationCallback_Instance')
make_head(_module, 'MI_OperationCallback_PromptUser')
make_head(_module, 'MI_OperationCallback_StreamedParameter')
make_head(_module, 'MI_OperationCallback_WriteError')
make_head(_module, 'MI_OperationCallback_WriteMessage')
make_head(_module, 'MI_OperationCallback_WriteProgress')
make_head(_module, 'MI_OperationCallbacks')
make_head(_module, 'MI_OperationFT')
make_head(_module, 'MI_OperationOptions')
make_head(_module, 'MI_OperationOptionsFT')
make_head(_module, 'MI_ParameterDecl')
make_head(_module, 'MI_ParameterSet')
make_head(_module, 'MI_ParameterSetFT')
make_head(_module, 'MI_PropertyDecl')
make_head(_module, 'MI_PropertySet')
make_head(_module, 'MI_PropertySetFT')
make_head(_module, 'MI_ProviderFT')
make_head(_module, 'MI_ProviderFT_AssociatorInstances')
make_head(_module, 'MI_ProviderFT_CreateInstance')
make_head(_module, 'MI_ProviderFT_DeleteInstance')
make_head(_module, 'MI_ProviderFT_DisableIndications')
make_head(_module, 'MI_ProviderFT_EnableIndications')
make_head(_module, 'MI_ProviderFT_EnumerateInstances')
make_head(_module, 'MI_ProviderFT_GetInstance')
make_head(_module, 'MI_ProviderFT_Invoke')
make_head(_module, 'MI_ProviderFT_Load')
make_head(_module, 'MI_ProviderFT_ModifyInstance')
make_head(_module, 'MI_ProviderFT_ReferenceInstances')
make_head(_module, 'MI_ProviderFT_Subscribe')
make_head(_module, 'MI_ProviderFT_Unload')
make_head(_module, 'MI_ProviderFT_Unsubscribe')
make_head(_module, 'MI_Qualifier')
make_head(_module, 'MI_QualifierDecl')
make_head(_module, 'MI_QualifierSet')
make_head(_module, 'MI_QualifierSetFT')
make_head(_module, 'MI_Real32A')
make_head(_module, 'MI_Real32AField')
make_head(_module, 'MI_Real32Field')
make_head(_module, 'MI_Real64A')
make_head(_module, 'MI_Real64AField')
make_head(_module, 'MI_Real64Field')
make_head(_module, 'MI_ReferenceA')
make_head(_module, 'MI_ReferenceAField')
make_head(_module, 'MI_ReferenceField')
make_head(_module, 'MI_SchemaDecl')
make_head(_module, 'MI_Serializer')
make_head(_module, 'MI_SerializerFT')
make_head(_module, 'MI_Server')
make_head(_module, 'MI_ServerFT')
make_head(_module, 'MI_Session')
make_head(_module, 'MI_SessionCallbacks')
make_head(_module, 'MI_SessionFT')
make_head(_module, 'MI_Sint16A')
make_head(_module, 'MI_Sint16AField')
make_head(_module, 'MI_Sint16Field')
make_head(_module, 'MI_Sint32A')
make_head(_module, 'MI_Sint32AField')
make_head(_module, 'MI_Sint32Field')
make_head(_module, 'MI_Sint64A')
make_head(_module, 'MI_Sint64AField')
make_head(_module, 'MI_Sint64Field')
make_head(_module, 'MI_Sint8A')
make_head(_module, 'MI_Sint8AField')
make_head(_module, 'MI_Sint8Field')
make_head(_module, 'MI_StringA')
make_head(_module, 'MI_StringAField')
make_head(_module, 'MI_StringField')
make_head(_module, 'MI_SubscriptionDeliveryOptions')
make_head(_module, 'MI_SubscriptionDeliveryOptionsFT')
make_head(_module, 'MI_Timestamp')
make_head(_module, 'MI_Uint16A')
make_head(_module, 'MI_Uint16AField')
make_head(_module, 'MI_Uint16Field')
make_head(_module, 'MI_Uint32A')
make_head(_module, 'MI_Uint32AField')
make_head(_module, 'MI_Uint32Field')
make_head(_module, 'MI_Uint64A')
make_head(_module, 'MI_Uint64AField')
make_head(_module, 'MI_Uint64Field')
make_head(_module, 'MI_Uint8A')
make_head(_module, 'MI_Uint8AField')
make_head(_module, 'MI_Uint8Field')
make_head(_module, 'MI_UserCredentials')
make_head(_module, 'MI_UsernamePasswordCreds')
make_head(_module, 'MI_UtilitiesFT')
make_head(_module, 'MI_Value')
make_head(_module, 'SWbemAnalysisMatrix')
make_head(_module, 'SWbemAnalysisMatrixList')
make_head(_module, 'SWbemAssocQueryInf')
make_head(_module, 'SWbemQueryQualifiedName')
make_head(_module, 'SWbemRpnConst')
make_head(_module, 'SWbemRpnEncodedQuery')
make_head(_module, 'SWbemRpnQueryToken')
make_head(_module, 'SWbemRpnTokenList')
make_head(_module, 'WBEM_COMPILE_STATUS_INFO')
__all__ = [
    "CIMTYPE_ENUMERATION",
    "CIM_BOOLEAN",
    "CIM_CHAR16",
    "CIM_DATETIME",
    "CIM_EMPTY",
    "CIM_FLAG_ARRAY",
    "CIM_ILLEGAL",
    "CIM_OBJECT",
    "CIM_REAL32",
    "CIM_REAL64",
    "CIM_REFERENCE",
    "CIM_SINT16",
    "CIM_SINT32",
    "CIM_SINT64",
    "CIM_SINT8",
    "CIM_STRING",
    "CIM_UINT16",
    "CIM_UINT32",
    "CIM_UINT64",
    "CIM_UINT8",
    "IEnumWbemClassObject",
    "IMofCompiler",
    "ISWbemDateTime",
    "ISWbemEventSource",
    "ISWbemLastError",
    "ISWbemLocator",
    "ISWbemMethod",
    "ISWbemMethodSet",
    "ISWbemNamedValue",
    "ISWbemNamedValueSet",
    "ISWbemObject",
    "ISWbemObjectEx",
    "ISWbemObjectPath",
    "ISWbemObjectSet",
    "ISWbemPrivilege",
    "ISWbemPrivilegeSet",
    "ISWbemProperty",
    "ISWbemPropertySet",
    "ISWbemQualifier",
    "ISWbemQualifierSet",
    "ISWbemRefreshableItem",
    "ISWbemRefresher",
    "ISWbemSecurity",
    "ISWbemServices",
    "ISWbemServicesEx",
    "ISWbemSink",
    "ISWbemSinkEvents",
    "IUnsecuredApartment",
    "IWMIExtension",
    "IWbemAddressResolution",
    "IWbemBackupRestore",
    "IWbemBackupRestoreEx",
    "IWbemCallResult",
    "IWbemClassObject",
    "IWbemClientConnectionTransport",
    "IWbemClientTransport",
    "IWbemConfigureRefresher",
    "IWbemConnectorLogin",
    "IWbemConstructClassObject",
    "IWbemContext",
    "IWbemDecoupledBasicEventProvider",
    "IWbemDecoupledRegistrar",
    "IWbemEventConsumerProvider",
    "IWbemEventProvider",
    "IWbemEventProviderQuerySink",
    "IWbemEventProviderSecurity",
    "IWbemEventSink",
    "IWbemHiPerfEnum",
    "IWbemHiPerfProvider",
    "IWbemLevel1Login",
    "IWbemLocator",
    "IWbemObjectAccess",
    "IWbemObjectSink",
    "IWbemObjectSinkEx",
    "IWbemObjectTextSrc",
    "IWbemPath",
    "IWbemPathKeyList",
    "IWbemPropertyProvider",
    "IWbemProviderIdentity",
    "IWbemProviderInit",
    "IWbemProviderInitSink",
    "IWbemQualifierSet",
    "IWbemQuery",
    "IWbemRefresher",
    "IWbemServices",
    "IWbemShutdown",
    "IWbemStatusCodeText",
    "IWbemTransport",
    "IWbemUnboundObjectSink",
    "IWbemUnsecuredApartment",
    "MI_ARRAY",
    "MI_Application",
    "MI_ApplicationFT",
    "MI_Application_InitializeV1",
    "MI_Array",
    "MI_ArrayField",
    "MI_BOOLEAN",
    "MI_BOOLEANA",
    "MI_BooleanA",
    "MI_BooleanAField",
    "MI_BooleanField",
    "MI_CALLBACKMODE_IGNORE",
    "MI_CALLBACKMODE_INQUIRE",
    "MI_CALLBACKMODE_REPORT",
    "MI_CALL_VERSION",
    "MI_CHAR16",
    "MI_CHAR16A",
    "MI_CHAR_TYPE",
    "MI_CallbackMode",
    "MI_CancelCallback",
    "MI_CancellationReason",
    "MI_Char16A",
    "MI_Char16AField",
    "MI_Char16Field",
    "MI_Class",
    "MI_ClassDecl",
    "MI_ClassFT",
    "MI_ClientFT_V1",
    "MI_ConstBooleanA",
    "MI_ConstBooleanAField",
    "MI_ConstBooleanField",
    "MI_ConstChar16A",
    "MI_ConstChar16AField",
    "MI_ConstChar16Field",
    "MI_ConstDatetimeA",
    "MI_ConstDatetimeAField",
    "MI_ConstDatetimeField",
    "MI_ConstInstanceA",
    "MI_ConstInstanceAField",
    "MI_ConstInstanceField",
    "MI_ConstReal32A",
    "MI_ConstReal32AField",
    "MI_ConstReal32Field",
    "MI_ConstReal64A",
    "MI_ConstReal64AField",
    "MI_ConstReal64Field",
    "MI_ConstReferenceA",
    "MI_ConstReferenceAField",
    "MI_ConstReferenceField",
    "MI_ConstSint16A",
    "MI_ConstSint16AField",
    "MI_ConstSint16Field",
    "MI_ConstSint32A",
    "MI_ConstSint32AField",
    "MI_ConstSint32Field",
    "MI_ConstSint64A",
    "MI_ConstSint64AField",
    "MI_ConstSint64Field",
    "MI_ConstSint8A",
    "MI_ConstSint8AField",
    "MI_ConstSint8Field",
    "MI_ConstStringA",
    "MI_ConstStringAField",
    "MI_ConstStringField",
    "MI_ConstUint16A",
    "MI_ConstUint16AField",
    "MI_ConstUint16Field",
    "MI_ConstUint32A",
    "MI_ConstUint32AField",
    "MI_ConstUint32Field",
    "MI_ConstUint64A",
    "MI_ConstUint64AField",
    "MI_ConstUint64Field",
    "MI_ConstUint8A",
    "MI_ConstUint8AField",
    "MI_ConstUint8Field",
    "MI_Context",
    "MI_ContextFT",
    "MI_DATETIME",
    "MI_DATETIMEA",
    "MI_Datetime",
    "MI_DatetimeA",
    "MI_DatetimeAField",
    "MI_DatetimeField",
    "MI_Deserializer",
    "MI_DeserializerFT",
    "MI_Deserializer_ClassObjectNeeded",
    "MI_DestinationOptions",
    "MI_DestinationOptionsFT",
    "MI_DestinationOptions_ImpersonationType",
    "MI_DestinationOptions_ImpersonationType_Default",
    "MI_DestinationOptions_ImpersonationType_Delegate",
    "MI_DestinationOptions_ImpersonationType_Identify",
    "MI_DestinationOptions_ImpersonationType_Impersonate",
    "MI_DestinationOptions_ImpersonationType_None",
    "MI_ERRORCATEGORY_ACCESS_DENIED",
    "MI_ERRORCATEGORY_AUTHENTICATION_ERROR",
    "MI_ERRORCATEGORY_CLOS_EERROR",
    "MI_ERRORCATEGORY_CONNECTION_ERROR",
    "MI_ERRORCATEGORY_DEADLOCK_DETECTED",
    "MI_ERRORCATEGORY_DEVICE_ERROR",
    "MI_ERRORCATEGORY_FROM_STDERR",
    "MI_ERRORCATEGORY_INVALID_ARGUMENT",
    "MI_ERRORCATEGORY_INVALID_DATA",
    "MI_ERRORCATEGORY_INVALID_OPERATION",
    "MI_ERRORCATEGORY_INVALID_RESULT",
    "MI_ERRORCATEGORY_INVALID_TYPE",
    "MI_ERRORCATEGORY_LIMITS_EXCEEDED",
    "MI_ERRORCATEGORY_METADATA_ERROR",
    "MI_ERRORCATEGORY_NOT_ENABLED",
    "MI_ERRORCATEGORY_NOT_IMPLEMENTED",
    "MI_ERRORCATEGORY_NOT_INSTALLED",
    "MI_ERRORCATEGORY_NOT_SPECIFIED",
    "MI_ERRORCATEGORY_OBJECT_NOT_FOUND",
    "MI_ERRORCATEGORY_OPEN_ERROR",
    "MI_ERRORCATEGORY_OPERATION_STOPPED",
    "MI_ERRORCATEGORY_OPERATION_TIMEOUT",
    "MI_ERRORCATEGORY_PARSER_ERROR",
    "MI_ERRORCATEGORY_PROTOCOL_ERROR",
    "MI_ERRORCATEGORY_QUOTA_EXCEEDED",
    "MI_ERRORCATEGORY_READ_ERROR",
    "MI_ERRORCATEGORY_RESOURCE_BUSY",
    "MI_ERRORCATEGORY_RESOURCE_EXISTS",
    "MI_ERRORCATEGORY_RESOURCE_UNAVAILABLE",
    "MI_ERRORCATEGORY_SECURITY_ERROR",
    "MI_ERRORCATEGORY_SYNTAX_ERROR",
    "MI_ERRORCATEGORY_WRITE_ERROR",
    "MI_ErrorCategory",
    "MI_FLAG_ABSTRACT",
    "MI_FLAG_ADOPT",
    "MI_FLAG_ANY",
    "MI_FLAG_ASSOCIATION",
    "MI_FLAG_BORROW",
    "MI_FLAG_CLASS",
    "MI_FLAG_DISABLEOVERRIDE",
    "MI_FLAG_ENABLEOVERRIDE",
    "MI_FLAG_EXPENSIVE",
    "MI_FLAG_EXTENDED",
    "MI_FLAG_IN",
    "MI_FLAG_INDICATION",
    "MI_FLAG_KEY",
    "MI_FLAG_METHOD",
    "MI_FLAG_NOT_MODIFIED",
    "MI_FLAG_NULL",
    "MI_FLAG_OUT",
    "MI_FLAG_PARAMETER",
    "MI_FLAG_PROPERTY",
    "MI_FLAG_READONLY",
    "MI_FLAG_REFERENCE",
    "MI_FLAG_REQUIRED",
    "MI_FLAG_RESTRICTED",
    "MI_FLAG_STATIC",
    "MI_FLAG_STREAM",
    "MI_FLAG_TERMINAL",
    "MI_FLAG_TOSUBCLASS",
    "MI_FLAG_TRANSLATABLE",
    "MI_FLAG_VERSION",
    "MI_FeatureDecl",
    "MI_Filter",
    "MI_FilterFT",
    "MI_HostedProvider",
    "MI_HostedProviderFT",
    "MI_INSTANCE",
    "MI_INSTANCEA",
    "MI_Instance",
    "MI_InstanceA",
    "MI_InstanceAField",
    "MI_InstanceExFT",
    "MI_InstanceFT",
    "MI_InstanceField",
    "MI_Interval",
    "MI_LOCALE_TYPE_CLOSEST_DATA",
    "MI_LOCALE_TYPE_CLOSEST_UI",
    "MI_LOCALE_TYPE_REQUESTED_DATA",
    "MI_LOCALE_TYPE_REQUESTED_UI",
    "MI_LocaleType",
    "MI_MAX_LOCALE_SIZE",
    "MI_MODULE_FLAG_BOOLEANS",
    "MI_MODULE_FLAG_CPLUSPLUS",
    "MI_MODULE_FLAG_DESCRIPTIONS",
    "MI_MODULE_FLAG_FILTER_SUPPORT",
    "MI_MODULE_FLAG_LOCALIZED",
    "MI_MODULE_FLAG_MAPPING_STRINGS",
    "MI_MODULE_FLAG_STANDARD_QUALIFIERS",
    "MI_MODULE_FLAG_VALUES",
    "MI_MainFunction",
    "MI_MethodDecl",
    "MI_MethodDecl_Invoke",
    "MI_Module",
    "MI_Module_Load",
    "MI_Module_Self",
    "MI_Module_Unload",
    "MI_OPERATIONFLAGS_BASIC_RTTI",
    "MI_OPERATIONFLAGS_DEFAULT_RTTI",
    "MI_OPERATIONFLAGS_EXPENSIVE_PROPERTIES",
    "MI_OPERATIONFLAGS_FULL_RTTI",
    "MI_OPERATIONFLAGS_LOCALIZED_QUALIFIERS",
    "MI_OPERATIONFLAGS_MANUAL_ACK_RESULTS",
    "MI_OPERATIONFLAGS_NO_RTTI",
    "MI_OPERATIONFLAGS_POLYMORPHISM_DEEP_BASE_PROPS_ONLY",
    "MI_OPERATIONFLAGS_POLYMORPHISM_SHALLOW",
    "MI_OPERATIONFLAGS_REPORT_OPERATION_STARTED",
    "MI_OPERATIONFLAGS_STANDARD_RTTI",
    "MI_ObjectDecl",
    "MI_Operation",
    "MI_OperationCallback_Class",
    "MI_OperationCallback_Indication",
    "MI_OperationCallback_Instance",
    "MI_OperationCallback_PromptUser",
    "MI_OperationCallback_ResponseType",
    "MI_OperationCallback_ResponseType_No",
    "MI_OperationCallback_ResponseType_NoToAll",
    "MI_OperationCallback_ResponseType_Yes",
    "MI_OperationCallback_ResponseType_YesToAll",
    "MI_OperationCallback_StreamedParameter",
    "MI_OperationCallback_WriteError",
    "MI_OperationCallback_WriteMessage",
    "MI_OperationCallback_WriteProgress",
    "MI_OperationCallbacks",
    "MI_OperationFT",
    "MI_OperationOptions",
    "MI_OperationOptionsFT",
    "MI_PROMPTTYPE_CRITICAL",
    "MI_PROMPTTYPE_NORMAL",
    "MI_PROVIDER_ARCHITECTURE_32BIT",
    "MI_PROVIDER_ARCHITECTURE_64BIT",
    "MI_ParameterDecl",
    "MI_ParameterSet",
    "MI_ParameterSetFT",
    "MI_PromptType",
    "MI_PropertyDecl",
    "MI_PropertySet",
    "MI_PropertySetFT",
    "MI_ProviderArchitecture",
    "MI_ProviderFT",
    "MI_ProviderFT_AssociatorInstances",
    "MI_ProviderFT_CreateInstance",
    "MI_ProviderFT_DeleteInstance",
    "MI_ProviderFT_DisableIndications",
    "MI_ProviderFT_EnableIndications",
    "MI_ProviderFT_EnumerateInstances",
    "MI_ProviderFT_GetInstance",
    "MI_ProviderFT_Invoke",
    "MI_ProviderFT_Load",
    "MI_ProviderFT_ModifyInstance",
    "MI_ProviderFT_ReferenceInstances",
    "MI_ProviderFT_Subscribe",
    "MI_ProviderFT_Unload",
    "MI_ProviderFT_Unsubscribe",
    "MI_Qualifier",
    "MI_QualifierDecl",
    "MI_QualifierSet",
    "MI_QualifierSetFT",
    "MI_REAL32",
    "MI_REAL32A",
    "MI_REAL64",
    "MI_REAL64A",
    "MI_REASON_NONE",
    "MI_REASON_SERVICESTOP",
    "MI_REASON_SHUTDOWN",
    "MI_REASON_TIMEOUT",
    "MI_REFERENCE",
    "MI_REFERENCEA",
    "MI_RESULT_ACCESS_DENIED",
    "MI_RESULT_ALREADY_EXISTS",
    "MI_RESULT_CLASS_HAS_CHILDREN",
    "MI_RESULT_CLASS_HAS_INSTANCES",
    "MI_RESULT_CONTINUATION_ON_ERROR_NOT_SUPPORTED",
    "MI_RESULT_FAILED",
    "MI_RESULT_FILTERED_ENUMERATION_NOT_SUPPORTED",
    "MI_RESULT_INVALID_CLASS",
    "MI_RESULT_INVALID_ENUMERATION_CONTEXT",
    "MI_RESULT_INVALID_NAMESPACE",
    "MI_RESULT_INVALID_OPERATION_TIMEOUT",
    "MI_RESULT_INVALID_PARAMETER",
    "MI_RESULT_INVALID_QUERY",
    "MI_RESULT_INVALID_SUPERCLASS",
    "MI_RESULT_METHOD_NOT_AVAILABLE",
    "MI_RESULT_METHOD_NOT_FOUND",
    "MI_RESULT_NAMESPACE_NOT_EMPTY",
    "MI_RESULT_NOT_FOUND",
    "MI_RESULT_NOT_SUPPORTED",
    "MI_RESULT_NO_SUCH_PROPERTY",
    "MI_RESULT_OK",
    "MI_RESULT_PULL_CANNOT_BE_ABANDONED",
    "MI_RESULT_PULL_HAS_BEEN_ABANDONED",
    "MI_RESULT_QUERY_LANGUAGE_NOT_SUPPORTED",
    "MI_RESULT_SERVER_IS_SHUTTING_DOWN",
    "MI_RESULT_SERVER_LIMITS_EXCEEDED",
    "MI_RESULT_TYPE_MISMATCH",
    "MI_Real32A",
    "MI_Real32AField",
    "MI_Real32Field",
    "MI_Real64A",
    "MI_Real64AField",
    "MI_Real64Field",
    "MI_ReferenceA",
    "MI_ReferenceAField",
    "MI_ReferenceField",
    "MI_Result",
    "MI_SERIALIZER_FLAGS_CLASS_DEEP",
    "MI_SERIALIZER_FLAGS_INSTANCE_WITH_CLASS",
    "MI_SINT16",
    "MI_SINT16A",
    "MI_SINT32",
    "MI_SINT32A",
    "MI_SINT64",
    "MI_SINT64A",
    "MI_SINT8",
    "MI_SINT8A",
    "MI_STRING",
    "MI_STRINGA",
    "MI_SUBSCRIBE_BOOKMARK_NEWEST",
    "MI_SUBSCRIBE_BOOKMARK_OLDEST",
    "MI_SchemaDecl",
    "MI_Serializer",
    "MI_SerializerFT",
    "MI_Server",
    "MI_ServerFT",
    "MI_Session",
    "MI_SessionCallbacks",
    "MI_SessionFT",
    "MI_Sint16A",
    "MI_Sint16AField",
    "MI_Sint16Field",
    "MI_Sint32A",
    "MI_Sint32AField",
    "MI_Sint32Field",
    "MI_Sint64A",
    "MI_Sint64AField",
    "MI_Sint64Field",
    "MI_Sint8A",
    "MI_Sint8AField",
    "MI_Sint8Field",
    "MI_StringA",
    "MI_StringAField",
    "MI_StringField",
    "MI_SubscriptionDeliveryOptions",
    "MI_SubscriptionDeliveryOptionsFT",
    "MI_SubscriptionDeliveryType",
    "MI_SubscriptionDeliveryType_Pull",
    "MI_SubscriptionDeliveryType_Push",
    "MI_Timestamp",
    "MI_Type",
    "MI_UINT16",
    "MI_UINT16A",
    "MI_UINT32",
    "MI_UINT32A",
    "MI_UINT64",
    "MI_UINT64A",
    "MI_UINT8",
    "MI_UINT8A",
    "MI_Uint16A",
    "MI_Uint16AField",
    "MI_Uint16Field",
    "MI_Uint32A",
    "MI_Uint32AField",
    "MI_Uint32Field",
    "MI_Uint64A",
    "MI_Uint64AField",
    "MI_Uint64Field",
    "MI_Uint8A",
    "MI_Uint8AField",
    "MI_Uint8Field",
    "MI_UserCredentials",
    "MI_UsernamePasswordCreds",
    "MI_UtilitiesFT",
    "MI_Value",
    "MI_WRITEMESSAGE_CHANNEL_DEBUG",
    "MI_WRITEMESSAGE_CHANNEL_VERBOSE",
    "MI_WRITEMESSAGE_CHANNEL_WARNING",
    "MofCompiler",
    "SWbemAnalysisMatrix",
    "SWbemAnalysisMatrixList",
    "SWbemAssocQueryInf",
    "SWbemDateTime",
    "SWbemEventSource",
    "SWbemLastError",
    "SWbemLocator",
    "SWbemMethod",
    "SWbemMethodSet",
    "SWbemNamedValue",
    "SWbemNamedValueSet",
    "SWbemObject",
    "SWbemObjectEx",
    "SWbemObjectPath",
    "SWbemObjectSet",
    "SWbemPrivilege",
    "SWbemPrivilegeSet",
    "SWbemProperty",
    "SWbemPropertySet",
    "SWbemQualifier",
    "SWbemQualifierSet",
    "SWbemQueryQualifiedName",
    "SWbemRefreshableItem",
    "SWbemRefresher",
    "SWbemRpnConst",
    "SWbemRpnEncodedQuery",
    "SWbemRpnQueryToken",
    "SWbemRpnTokenList",
    "SWbemSecurity",
    "SWbemServices",
    "SWbemServicesEx",
    "SWbemSink",
    "UnsecuredApartment",
    "WBEMESS_E_AUTHZ_NOT_PRIVILEGED",
    "WBEMESS_E_REGISTRATION_TOO_BROAD",
    "WBEMESS_E_REGISTRATION_TOO_PRECISE",
    "WBEMMOF_E_ALIASES_IN_EMBEDDED",
    "WBEMMOF_E_CIMTYPE_QUALIFIER",
    "WBEMMOF_E_DUPLICATE_PROPERTY",
    "WBEMMOF_E_DUPLICATE_QUALIFIER",
    "WBEMMOF_E_ERROR_CREATING_TEMP_FILE",
    "WBEMMOF_E_ERROR_INVALID_INCLUDE_FILE",
    "WBEMMOF_E_EXPECTED_ALIAS_NAME",
    "WBEMMOF_E_EXPECTED_BRACE_OR_BAD_TYPE",
    "WBEMMOF_E_EXPECTED_CLASS_NAME",
    "WBEMMOF_E_EXPECTED_CLOSE_BRACE",
    "WBEMMOF_E_EXPECTED_CLOSE_BRACKET",
    "WBEMMOF_E_EXPECTED_CLOSE_PAREN",
    "WBEMMOF_E_EXPECTED_DOLLAR",
    "WBEMMOF_E_EXPECTED_FLAVOR_TYPE",
    "WBEMMOF_E_EXPECTED_OPEN_BRACE",
    "WBEMMOF_E_EXPECTED_OPEN_PAREN",
    "WBEMMOF_E_EXPECTED_PROPERTY_NAME",
    "WBEMMOF_E_EXPECTED_QUALIFIER_NAME",
    "WBEMMOF_E_EXPECTED_SEMI",
    "WBEMMOF_E_EXPECTED_TYPE_IDENTIFIER",
    "WBEMMOF_E_ILLEGAL_CONSTANT_VALUE",
    "WBEMMOF_E_INCOMPATIBLE_FLAVOR_TYPES",
    "WBEMMOF_E_INCOMPATIBLE_FLAVOR_TYPES2",
    "WBEMMOF_E_INVALID_AMENDMENT_SYNTAX",
    "WBEMMOF_E_INVALID_CLASS_DECLARATION",
    "WBEMMOF_E_INVALID_DELETECLASS_SYNTAX",
    "WBEMMOF_E_INVALID_DELETEINSTANCE_SYNTAX",
    "WBEMMOF_E_INVALID_DUPLICATE_AMENDMENT",
    "WBEMMOF_E_INVALID_FILE",
    "WBEMMOF_E_INVALID_FLAGS_SYNTAX",
    "WBEMMOF_E_INVALID_INSTANCE_DECLARATION",
    "WBEMMOF_E_INVALID_NAMESPACE_SPECIFICATION",
    "WBEMMOF_E_INVALID_NAMESPACE_SYNTAX",
    "WBEMMOF_E_INVALID_PRAGMA",
    "WBEMMOF_E_INVALID_QUALIFIER_SYNTAX",
    "WBEMMOF_E_MULTIPLE_ALIASES",
    "WBEMMOF_E_MUST_BE_IN_OR_OUT",
    "WBEMMOF_E_NO_ARRAYS_RETURNED",
    "WBEMMOF_E_NULL_ARRAY_ELEM",
    "WBEMMOF_E_OUT_OF_RANGE",
    "WBEMMOF_E_QUALIFIER_USED_OUTSIDE_SCOPE",
    "WBEMMOF_E_TYPEDEF_NOT_SUPPORTED",
    "WBEMMOF_E_TYPE_MISMATCH",
    "WBEMMOF_E_UNEXPECTED_ALIAS",
    "WBEMMOF_E_UNEXPECTED_ARRAY_INIT",
    "WBEMMOF_E_UNRECOGNIZED_TOKEN",
    "WBEMMOF_E_UNRECOGNIZED_TYPE",
    "WBEMMOF_E_UNSUPPORTED_CIMV22_DATA_TYPE",
    "WBEMMOF_E_UNSUPPORTED_CIMV22_QUAL_VALUE",
    "WBEMPATH_COMPRESSED",
    "WBEMPATH_CREATE_ACCEPT_ABSOLUTE",
    "WBEMPATH_CREATE_ACCEPT_ALL",
    "WBEMPATH_CREATE_ACCEPT_RELATIVE",
    "WBEMPATH_GET_NAMESPACE_ONLY",
    "WBEMPATH_GET_ORIGINAL",
    "WBEMPATH_GET_RELATIVE_ONLY",
    "WBEMPATH_GET_SERVER_AND_NAMESPACE_ONLY",
    "WBEMPATH_GET_SERVER_TOO",
    "WBEMPATH_INFO_ANON_LOCAL_MACHINE",
    "WBEMPATH_INFO_CIM_COMPLIANT",
    "WBEMPATH_INFO_CONTAINS_SINGLETON",
    "WBEMPATH_INFO_HAS_IMPLIED_KEY",
    "WBEMPATH_INFO_HAS_MACHINE_NAME",
    "WBEMPATH_INFO_HAS_SUBSCOPES",
    "WBEMPATH_INFO_HAS_V2_REF_PATHS",
    "WBEMPATH_INFO_IS_CLASS_REF",
    "WBEMPATH_INFO_IS_COMPOUND",
    "WBEMPATH_INFO_IS_INST_REF",
    "WBEMPATH_INFO_IS_PARENT",
    "WBEMPATH_INFO_IS_SINGLETON",
    "WBEMPATH_INFO_NATIVE_PATH",
    "WBEMPATH_INFO_PATH_HAD_SERVER",
    "WBEMPATH_INFO_SERVER_NAMESPACE_ONLY",
    "WBEMPATH_INFO_V1_COMPLIANT",
    "WBEMPATH_INFO_V2_COMPLIANT",
    "WBEMPATH_INFO_WMI_PATH",
    "WBEMPATH_QUOTEDTEXT",
    "WBEMPATH_TEXT",
    "WBEMPATH_TREAT_SINGLE_IDENT_AS_NS",
    "WBEMSTATUS",
    "WBEMSTATUS_FORMAT",
    "WBEMSTATUS_FORMAT_NEWLINE",
    "WBEMSTATUS_FORMAT_NO_NEWLINE",
    "WBEMS_DISPID_COMPLETED",
    "WBEMS_DISPID_CONNECTION_READY",
    "WBEMS_DISPID_DERIVATION",
    "WBEMS_DISPID_OBJECT_PUT",
    "WBEMS_DISPID_OBJECT_READY",
    "WBEMS_DISPID_PROGRESS",
    "WBEM_AUTHENTICATION_METHOD_MASK",
    "WBEM_BACKUP_RESTORE_FLAGS",
    "WBEM_BATCH_TYPE",
    "WBEM_CHANGE_FLAG_TYPE",
    "WBEM_COMPARISON_FLAG",
    "WBEM_COMPARISON_INCLUDE_ALL",
    "WBEM_COMPILER_OPTIONS",
    "WBEM_COMPILE_STATUS_INFO",
    "WBEM_CONDITION_FLAG_TYPE",
    "WBEM_CONNECT_OPTIONS",
    "WBEM_ENABLE",
    "WBEM_EXTRA_RETURN_CODES",
    "WBEM_E_ACCESS_DENIED",
    "WBEM_E_AGGREGATING_BY_OBJECT",
    "WBEM_E_ALREADY_EXISTS",
    "WBEM_E_AMBIGUOUS_OPERATION",
    "WBEM_E_AMENDED_OBJECT",
    "WBEM_E_BACKUP_RESTORE_WINMGMT_RUNNING",
    "WBEM_E_BUFFER_TOO_SMALL",
    "WBEM_E_CALL_CANCELLED",
    "WBEM_E_CANNOT_BE_ABSTRACT",
    "WBEM_E_CANNOT_BE_KEY",
    "WBEM_E_CANNOT_BE_SINGLETON",
    "WBEM_E_CANNOT_CHANGE_INDEX_INHERITANCE",
    "WBEM_E_CANNOT_CHANGE_KEY_INHERITANCE",
    "WBEM_E_CIRCULAR_REFERENCE",
    "WBEM_E_CLASS_HAS_CHILDREN",
    "WBEM_E_CLASS_HAS_INSTANCES",
    "WBEM_E_CLASS_NAME_TOO_WIDE",
    "WBEM_E_CLIENT_TOO_SLOW",
    "WBEM_E_CONNECTION_FAILED",
    "WBEM_E_CRITICAL_ERROR",
    "WBEM_E_DATABASE_VER_MISMATCH",
    "WBEM_E_ENCRYPTED_CONNECTION_REQUIRED",
    "WBEM_E_FAILED",
    "WBEM_E_FATAL_TRANSPORT_ERROR",
    "WBEM_E_HANDLE_OUT_OF_DATE",
    "WBEM_E_ILLEGAL_NULL",
    "WBEM_E_ILLEGAL_OPERATION",
    "WBEM_E_INCOMPLETE_CLASS",
    "WBEM_E_INITIALIZATION_FAILURE",
    "WBEM_E_INVALID_ASSOCIATION",
    "WBEM_E_INVALID_CIM_TYPE",
    "WBEM_E_INVALID_CLASS",
    "WBEM_E_INVALID_CONTEXT",
    "WBEM_E_INVALID_DUPLICATE_PARAMETER",
    "WBEM_E_INVALID_FLAVOR",
    "WBEM_E_INVALID_HANDLE_REQUEST",
    "WBEM_E_INVALID_LOCALE",
    "WBEM_E_INVALID_METHOD",
    "WBEM_E_INVALID_METHOD_PARAMETERS",
    "WBEM_E_INVALID_NAMESPACE",
    "WBEM_E_INVALID_OBJECT",
    "WBEM_E_INVALID_OBJECT_PATH",
    "WBEM_E_INVALID_OPERATION",
    "WBEM_E_INVALID_OPERATOR",
    "WBEM_E_INVALID_PARAMETER",
    "WBEM_E_INVALID_PARAMETER_ID",
    "WBEM_E_INVALID_PROPERTY",
    "WBEM_E_INVALID_PROPERTY_TYPE",
    "WBEM_E_INVALID_PROVIDER_REGISTRATION",
    "WBEM_E_INVALID_QUALIFIER",
    "WBEM_E_INVALID_QUALIFIER_TYPE",
    "WBEM_E_INVALID_QUERY",
    "WBEM_E_INVALID_QUERY_TYPE",
    "WBEM_E_INVALID_STREAM",
    "WBEM_E_INVALID_SUPERCLASS",
    "WBEM_E_INVALID_SYNTAX",
    "WBEM_E_LOCAL_CREDENTIALS",
    "WBEM_E_MARSHAL_INVALID_SIGNATURE",
    "WBEM_E_MARSHAL_VERSION_MISMATCH",
    "WBEM_E_METHOD_DISABLED",
    "WBEM_E_METHOD_NAME_TOO_WIDE",
    "WBEM_E_METHOD_NOT_IMPLEMENTED",
    "WBEM_E_MISSING_AGGREGATION_LIST",
    "WBEM_E_MISSING_GROUP_WITHIN",
    "WBEM_E_MISSING_PARAMETER_ID",
    "WBEM_E_NONCONSECUTIVE_PARAMETER_IDS",
    "WBEM_E_NONDECORATED_OBJECT",
    "WBEM_E_NOT_AVAILABLE",
    "WBEM_E_NOT_EVENT_CLASS",
    "WBEM_E_NOT_FOUND",
    "WBEM_E_NOT_SUPPORTED",
    "WBEM_E_NO_KEY",
    "WBEM_E_NO_SCHEMA",
    "WBEM_E_NULL_SECURITY_DESCRIPTOR",
    "WBEM_E_OUT_OF_DISK_SPACE",
    "WBEM_E_OUT_OF_MEMORY",
    "WBEM_E_OVERRIDE_NOT_ALLOWED",
    "WBEM_E_PARAMETER_ID_ON_RETVAL",
    "WBEM_E_PRIVILEGE_NOT_HELD",
    "WBEM_E_PROPAGATED_METHOD",
    "WBEM_E_PROPAGATED_PROPERTY",
    "WBEM_E_PROPAGATED_QUALIFIER",
    "WBEM_E_PROPERTY_NAME_TOO_WIDE",
    "WBEM_E_PROPERTY_NOT_AN_OBJECT",
    "WBEM_E_PROVIDER_ALREADY_REGISTERED",
    "WBEM_E_PROVIDER_DISABLED",
    "WBEM_E_PROVIDER_FAILURE",
    "WBEM_E_PROVIDER_LOAD_FAILURE",
    "WBEM_E_PROVIDER_NOT_CAPABLE",
    "WBEM_E_PROVIDER_NOT_FOUND",
    "WBEM_E_PROVIDER_NOT_REGISTERED",
    "WBEM_E_PROVIDER_SUSPENDED",
    "WBEM_E_PROVIDER_TIMED_OUT",
    "WBEM_E_QUALIFIER_NAME_TOO_WIDE",
    "WBEM_E_QUERY_NOT_IMPLEMENTED",
    "WBEM_E_QUEUE_OVERFLOW",
    "WBEM_E_QUOTA_VIOLATION",
    "WBEM_E_READ_ONLY",
    "WBEM_E_REFRESHER_BUSY",
    "WBEM_E_RERUN_COMMAND",
    "WBEM_E_RESERVED_001",
    "WBEM_E_RESERVED_002",
    "WBEM_E_RESOURCE_CONTENTION",
    "WBEM_E_RETRY_LATER",
    "WBEM_E_SERVER_TOO_BUSY",
    "WBEM_E_SHUTTING_DOWN",
    "WBEM_E_SYNCHRONIZATION_REQUIRED",
    "WBEM_E_SYSTEM_PROPERTY",
    "WBEM_E_TIMED_OUT",
    "WBEM_E_TOO_MANY_PROPERTIES",
    "WBEM_E_TOO_MUCH_DATA",
    "WBEM_E_TRANSPORT_FAILURE",
    "WBEM_E_TYPE_MISMATCH",
    "WBEM_E_UNEXPECTED",
    "WBEM_E_UNINTERPRETABLE_PROVIDER_QUERY",
    "WBEM_E_UNKNOWN_OBJECT_TYPE",
    "WBEM_E_UNKNOWN_PACKET_TYPE",
    "WBEM_E_UNPARSABLE_QUERY",
    "WBEM_E_UNSUPPORTED_CLASS_UPDATE",
    "WBEM_E_UNSUPPORTED_LOCALE",
    "WBEM_E_UNSUPPORTED_PARAMETER",
    "WBEM_E_UNSUPPORTED_PUT_EXTENSION",
    "WBEM_E_UPDATE_OVERRIDE_NOT_ALLOWED",
    "WBEM_E_UPDATE_PROPAGATED_METHOD",
    "WBEM_E_UPDATE_TYPE_MISMATCH",
    "WBEM_E_VALUE_OUT_OF_RANGE",
    "WBEM_E_VETO_DELETE",
    "WBEM_E_VETO_PUT",
    "WBEM_FLAG_ADVISORY",
    "WBEM_FLAG_ALLOW_READ",
    "WBEM_FLAG_ALWAYS",
    "WBEM_FLAG_AUTORECOVER",
    "WBEM_FLAG_BACKUP_RESTORE_DEFAULT",
    "WBEM_FLAG_BACKUP_RESTORE_FORCE_SHUTDOWN",
    "WBEM_FLAG_BATCH_IF_NEEDED",
    "WBEM_FLAG_BIDIRECTIONAL",
    "WBEM_FLAG_CHECK_ONLY",
    "WBEM_FLAG_CLASS_LOCAL_AND_OVERRIDES",
    "WBEM_FLAG_CLASS_OVERRIDES_ONLY",
    "WBEM_FLAG_CONNECT_PROVIDERS",
    "WBEM_FLAG_CONNECT_REPOSITORY_ONLY",
    "WBEM_FLAG_CONNECT_USE_MAX_WAIT",
    "WBEM_FLAG_CONSOLE_PRINT",
    "WBEM_FLAG_CREATE_ONLY",
    "WBEM_FLAG_CREATE_OR_UPDATE",
    "WBEM_FLAG_DEEP",
    "WBEM_FLAG_DIRECT_READ",
    "WBEM_FLAG_DONT_ADD_TO_LIST",
    "WBEM_FLAG_DONT_SEND_STATUS",
    "WBEM_FLAG_ENSURE_LOCATABLE",
    "WBEM_FLAG_EXCLUDE_OBJECT_QUALIFIERS",
    "WBEM_FLAG_EXCLUDE_PROPERTY_QUALIFIERS",
    "WBEM_FLAG_FORWARD_ONLY",
    "WBEM_FLAG_IGNORE_CASE",
    "WBEM_FLAG_IGNORE_CLASS",
    "WBEM_FLAG_IGNORE_DEFAULT_VALUES",
    "WBEM_FLAG_IGNORE_FLAVOR",
    "WBEM_FLAG_IGNORE_OBJECT_SOURCE",
    "WBEM_FLAG_IGNORE_QUALIFIERS",
    "WBEM_FLAG_INPROC_LOGIN",
    "WBEM_FLAG_KEYS_ONLY",
    "WBEM_FLAG_LOCAL_LOGIN",
    "WBEM_FLAG_LOCAL_ONLY",
    "WBEM_FLAG_LONG_NAME",
    "WBEM_FLAG_MUST_BATCH",
    "WBEM_FLAG_MUST_NOT_BATCH",
    "WBEM_FLAG_NONSYSTEM_ONLY",
    "WBEM_FLAG_NO_ERROR_OBJECT",
    "WBEM_FLAG_NO_FLAVORS",
    "WBEM_FLAG_ONLY_IF_FALSE",
    "WBEM_FLAG_ONLY_IF_IDENTICAL",
    "WBEM_FLAG_ONLY_IF_TRUE",
    "WBEM_FLAG_OWNER_UPDATE",
    "WBEM_FLAG_PROPAGATED_ONLY",
    "WBEM_FLAG_PROTOTYPE",
    "WBEM_FLAG_REFRESH_AUTO_RECONNECT",
    "WBEM_FLAG_REFRESH_NO_AUTO_RECONNECT",
    "WBEM_FLAG_REFS_ONLY",
    "WBEM_FLAG_REMOTE_LOGIN",
    "WBEM_FLAG_RETURN_ERROR_OBJECT",
    "WBEM_FLAG_RETURN_IMMEDIATELY",
    "WBEM_FLAG_RETURN_WBEM_COMPLETE",
    "WBEM_FLAG_SEND_ONLY_SELECTED",
    "WBEM_FLAG_SEND_STATUS",
    "WBEM_FLAG_SHALLOW",
    "WBEM_FLAG_SHORT_NAME",
    "WBEM_FLAG_SPLIT_FILES",
    "WBEM_FLAG_STORE_FILE",
    "WBEM_FLAG_STRONG_VALIDATION",
    "WBEM_FLAG_SYSTEM_ONLY",
    "WBEM_FLAG_UNSECAPP_CHECK_ACCESS",
    "WBEM_FLAG_UNSECAPP_DEFAULT_CHECK_ACCESS",
    "WBEM_FLAG_UNSECAPP_DONT_CHECK_ACCESS",
    "WBEM_FLAG_UPDATE_COMPATIBLE",
    "WBEM_FLAG_UPDATE_FORCE_MODE",
    "WBEM_FLAG_UPDATE_ONLY",
    "WBEM_FLAG_UPDATE_SAFE_MODE",
    "WBEM_FLAG_USE_AMENDED_QUALIFIERS",
    "WBEM_FLAG_USE_MULTIPLE_CHALLENGES",
    "WBEM_FLAG_WMI_CHECK",
    "WBEM_FLAVOR_AMENDED",
    "WBEM_FLAVOR_DONT_PROPAGATE",
    "WBEM_FLAVOR_FLAG_PROPAGATE_TO_DERIVED_CLASS",
    "WBEM_FLAVOR_FLAG_PROPAGATE_TO_INSTANCE",
    "WBEM_FLAVOR_MASK_AMENDED",
    "WBEM_FLAVOR_MASK_ORIGIN",
    "WBEM_FLAVOR_MASK_PERMISSIONS",
    "WBEM_FLAVOR_MASK_PROPAGATION",
    "WBEM_FLAVOR_NOT_AMENDED",
    "WBEM_FLAVOR_NOT_OVERRIDABLE",
    "WBEM_FLAVOR_ORIGIN_LOCAL",
    "WBEM_FLAVOR_ORIGIN_PROPAGATED",
    "WBEM_FLAVOR_ORIGIN_SYSTEM",
    "WBEM_FLAVOR_OVERRIDABLE",
    "WBEM_FLAVOR_TYPE",
    "WBEM_FULL_WRITE_REP",
    "WBEM_GENERIC_FLAG_TYPE",
    "WBEM_GENUS_CLASS",
    "WBEM_GENUS_INSTANCE",
    "WBEM_GENUS_TYPE",
    "WBEM_GET_KEY_FLAGS",
    "WBEM_GET_TEXT_FLAGS",
    "WBEM_INFINITE",
    "WBEM_INFORMATION_FLAG_TYPE",
    "WBEM_LIMITATION_FLAG_TYPE",
    "WBEM_LIMITS",
    "WBEM_LOCKING_FLAG_TYPE",
    "WBEM_LOGIN_TYPE",
    "WBEM_MASK_CLASS_CONDITION",
    "WBEM_MASK_CONDITION_ORIGIN",
    "WBEM_MASK_PRIMARY_CONDITION",
    "WBEM_MASK_RESERVED_FLAGS",
    "WBEM_MASK_UPDATE_MODE",
    "WBEM_MAX_IDENTIFIER",
    "WBEM_MAX_OBJECT_NESTING",
    "WBEM_MAX_PATH",
    "WBEM_MAX_QUERY",
    "WBEM_MAX_USER_PROPERTIES",
    "WBEM_METHOD_EXECUTE",
    "WBEM_NO_ERROR",
    "WBEM_NO_WAIT",
    "WBEM_PARTIAL_WRITE_REP",
    "WBEM_PATH_CREATE_FLAG",
    "WBEM_PATH_STATUS_FLAG",
    "WBEM_PROVIDER_FLAGS",
    "WBEM_PROVIDER_REQUIREMENTS_TYPE",
    "WBEM_QUERY_FLAG_TYPE",
    "WBEM_REFRESHER_FLAGS",
    "WBEM_REMOTE_ACCESS",
    "WBEM_REQUIREMENTS_RECHECK_SUBSCRIPTIONS",
    "WBEM_REQUIREMENTS_START_POSTFILTER",
    "WBEM_REQUIREMENTS_STOP_POSTFILTER",
    "WBEM_RETURN_IMMEDIATELY",
    "WBEM_RETURN_WHEN_COMPLETE",
    "WBEM_RIGHT_PUBLISH",
    "WBEM_RIGHT_SUBSCRIBE",
    "WBEM_SECURITY_FLAGS",
    "WBEM_SHUTDOWN_FLAGS",
    "WBEM_SHUTDOWN_OS",
    "WBEM_SHUTDOWN_UNLOAD_COMPONENT",
    "WBEM_SHUTDOWN_WMI",
    "WBEM_STATUS_COMPLETE",
    "WBEM_STATUS_LOGGING_INFORMATION",
    "WBEM_STATUS_LOGGING_INFORMATION_ESS",
    "WBEM_STATUS_LOGGING_INFORMATION_HOST",
    "WBEM_STATUS_LOGGING_INFORMATION_PROVIDER",
    "WBEM_STATUS_LOGGING_INFORMATION_REPOSITORY",
    "WBEM_STATUS_PROGRESS",
    "WBEM_STATUS_REQUIREMENTS",
    "WBEM_STATUS_TYPE",
    "WBEM_S_ACCESS_DENIED",
    "WBEM_S_ALREADY_EXISTS",
    "WBEM_S_DIFFERENT",
    "WBEM_S_DUPLICATE_OBJECTS",
    "WBEM_S_FALSE",
    "WBEM_S_INDIRECTLY_UPDATED",
    "WBEM_S_INITIALIZED",
    "WBEM_S_LIMITED_SERVICE",
    "WBEM_S_NO_ERROR",
    "WBEM_S_NO_MORE_DATA",
    "WBEM_S_OPERATION_CANCELLED",
    "WBEM_S_PARTIAL_RESULTS",
    "WBEM_S_PENDING",
    "WBEM_S_RESET_TO_DEFAULT",
    "WBEM_S_SAME",
    "WBEM_S_SOURCE_NOT_AVAILABLE",
    "WBEM_S_SUBJECT_TO_SDS",
    "WBEM_S_TIMEDOUT",
    "WBEM_TEXT_FLAG_TYPE",
    "WBEM_UNSECAPP_FLAG_TYPE",
    "WBEM_WRITE_PROVIDER",
    "WMIExtension",
    "WMIQ_ANALYSIS_ASSOC_QUERY",
    "WMIQ_ANALYSIS_PROP_ANALYSIS_MATRIX",
    "WMIQ_ANALYSIS_QUERY_TEXT",
    "WMIQ_ANALYSIS_RESERVED",
    "WMIQ_ANALYSIS_RPN_SEQUENCE",
    "WMIQ_ANALYSIS_TYPE",
    "WMIQ_ASSOCQ_ASSOCCLASS",
    "WMIQ_ASSOCQ_ASSOCIATORS",
    "WMIQ_ASSOCQ_CLASSDEFSONLY",
    "WMIQ_ASSOCQ_CLASSREFSONLY",
    "WMIQ_ASSOCQ_FLAGS",
    "WMIQ_ASSOCQ_KEYSONLY",
    "WMIQ_ASSOCQ_REFERENCES",
    "WMIQ_ASSOCQ_REQUIREDASSOCQUALIFIER",
    "WMIQ_ASSOCQ_REQUIREDQUALIFIER",
    "WMIQ_ASSOCQ_RESULTCLASS",
    "WMIQ_ASSOCQ_RESULTROLE",
    "WMIQ_ASSOCQ_ROLE",
    "WMIQ_ASSOCQ_SCHEMAONLY",
    "WMIQ_LANGUAGE_FEATURES",
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
    "WMIQ_LF1_BASIC_SELECT",
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
    "WMIQ_LF2_CLASS_NAME_IN_QUERY",
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
    "WMIQ_LF3_STRING_CASE_FUNCTIONS",
    "WMIQ_LF40_BETWEEN",
    "WMIQ_LF4_PROP_TO_PROP_TESTS",
    "WMIQ_LF5_COUNT_STAR",
    "WMIQ_LF6_ORDER_BY",
    "WMIQ_LF7_DISTINCT",
    "WMIQ_LF8_ISA",
    "WMIQ_LF9_THIS",
    "WMIQ_LF_LAST",
    "WMIQ_RPNF_ARRAY_ACCESS_USED",
    "WMIQ_RPNF_COUNT_STAR",
    "WMIQ_RPNF_EQUALITY_TESTS_ONLY",
    "WMIQ_RPNF_FEATURE",
    "WMIQ_RPNF_FEATURE_SELECT_STAR",
    "WMIQ_RPNF_GROUP_BY_HAVING",
    "WMIQ_RPNF_ISA_USED",
    "WMIQ_RPNF_ORDER_BY",
    "WMIQ_RPNF_PROJECTION",
    "WMIQ_RPNF_PROP_TO_PROP_TESTS",
    "WMIQ_RPNF_QUALIFIED_NAMES_USED",
    "WMIQ_RPNF_QUERY_IS_CONJUNCTIVE",
    "WMIQ_RPNF_QUERY_IS_DISJUNCTIVE",
    "WMIQ_RPNF_SYSPROP_CLASS_USED",
    "WMIQ_RPNF_WHERE_CLAUSE_PRESENT",
    "WMIQ_RPN_CONST",
    "WMIQ_RPN_CONST2",
    "WMIQ_RPN_FROM_CLASS_LIST",
    "WMIQ_RPN_FROM_MULTIPLE",
    "WMIQ_RPN_FROM_PATH",
    "WMIQ_RPN_FROM_UNARY",
    "WMIQ_RPN_GET_EXPR_SHAPE",
    "WMIQ_RPN_GET_LEFT_FUNCTION",
    "WMIQ_RPN_GET_RELOP",
    "WMIQ_RPN_GET_RIGHT_FUNCTION",
    "WMIQ_RPN_GET_TOKEN_TYPE",
    "WMIQ_RPN_LEFT_FUNCTION",
    "WMIQ_RPN_LEFT_PROPERTY_NAME",
    "WMIQ_RPN_NEXT_TOKEN",
    "WMIQ_RPN_OP_EQ",
    "WMIQ_RPN_OP_GE",
    "WMIQ_RPN_OP_GT",
    "WMIQ_RPN_OP_ISA",
    "WMIQ_RPN_OP_ISNOTA",
    "WMIQ_RPN_OP_ISNOTNULL",
    "WMIQ_RPN_OP_ISNULL",
    "WMIQ_RPN_OP_LE",
    "WMIQ_RPN_OP_LIKE",
    "WMIQ_RPN_OP_LT",
    "WMIQ_RPN_OP_NE",
    "WMIQ_RPN_OP_UNDEFINED",
    "WMIQ_RPN_RELOP",
    "WMIQ_RPN_RIGHT_FUNCTION",
    "WMIQ_RPN_RIGHT_PROPERTY_NAME",
    "WMIQ_RPN_TOKEN_AND",
    "WMIQ_RPN_TOKEN_EXPRESSION",
    "WMIQ_RPN_TOKEN_FLAGS",
    "WMIQ_RPN_TOKEN_NOT",
    "WMIQ_RPN_TOKEN_OR",
    "WMI_OBJ_TEXT",
    "WMI_OBJ_TEXT_CIM_DTD_2_0",
    "WMI_OBJ_TEXT_LAST",
    "WMI_OBJ_TEXT_WMI_DTD_2_0",
    "WMI_OBJ_TEXT_WMI_EXT1",
    "WMI_OBJ_TEXT_WMI_EXT10",
    "WMI_OBJ_TEXT_WMI_EXT2",
    "WMI_OBJ_TEXT_WMI_EXT3",
    "WMI_OBJ_TEXT_WMI_EXT4",
    "WMI_OBJ_TEXT_WMI_EXT5",
    "WMI_OBJ_TEXT_WMI_EXT6",
    "WMI_OBJ_TEXT_WMI_EXT7",
    "WMI_OBJ_TEXT_WMI_EXT8",
    "WMI_OBJ_TEXT_WMI_EXT9",
    "WbemAdministrativeLocator",
    "WbemAuthenticatedLocator",
    "WbemAuthenticationLevelEnum",
    "WbemAuthenticationLevelEnum_wbemAuthenticationLevelCall",
    "WbemAuthenticationLevelEnum_wbemAuthenticationLevelConnect",
    "WbemAuthenticationLevelEnum_wbemAuthenticationLevelDefault",
    "WbemAuthenticationLevelEnum_wbemAuthenticationLevelNone",
    "WbemAuthenticationLevelEnum_wbemAuthenticationLevelPkt",
    "WbemAuthenticationLevelEnum_wbemAuthenticationLevelPktIntegrity",
    "WbemAuthenticationLevelEnum_wbemAuthenticationLevelPktPrivacy",
    "WbemBackupRestore",
    "WbemChangeFlagEnum",
    "WbemChangeFlagEnum_wbemChangeFlagAdvisory",
    "WbemChangeFlagEnum_wbemChangeFlagCreateOnly",
    "WbemChangeFlagEnum_wbemChangeFlagCreateOrUpdate",
    "WbemChangeFlagEnum_wbemChangeFlagStrongValidation",
    "WbemChangeFlagEnum_wbemChangeFlagUpdateCompatible",
    "WbemChangeFlagEnum_wbemChangeFlagUpdateForceMode",
    "WbemChangeFlagEnum_wbemChangeFlagUpdateOnly",
    "WbemChangeFlagEnum_wbemChangeFlagUpdateSafeMode",
    "WbemCimtypeEnum",
    "WbemCimtypeEnum_wbemCimtypeBoolean",
    "WbemCimtypeEnum_wbemCimtypeChar16",
    "WbemCimtypeEnum_wbemCimtypeDatetime",
    "WbemCimtypeEnum_wbemCimtypeObject",
    "WbemCimtypeEnum_wbemCimtypeReal32",
    "WbemCimtypeEnum_wbemCimtypeReal64",
    "WbemCimtypeEnum_wbemCimtypeReference",
    "WbemCimtypeEnum_wbemCimtypeSint16",
    "WbemCimtypeEnum_wbemCimtypeSint32",
    "WbemCimtypeEnum_wbemCimtypeSint64",
    "WbemCimtypeEnum_wbemCimtypeSint8",
    "WbemCimtypeEnum_wbemCimtypeString",
    "WbemCimtypeEnum_wbemCimtypeUint16",
    "WbemCimtypeEnum_wbemCimtypeUint32",
    "WbemCimtypeEnum_wbemCimtypeUint64",
    "WbemCimtypeEnum_wbemCimtypeUint8",
    "WbemClassObject",
    "WbemComparisonFlagEnum",
    "WbemComparisonFlagEnum_wbemComparisonFlagIgnoreCase",
    "WbemComparisonFlagEnum_wbemComparisonFlagIgnoreClass",
    "WbemComparisonFlagEnum_wbemComparisonFlagIgnoreDefaultValues",
    "WbemComparisonFlagEnum_wbemComparisonFlagIgnoreFlavor",
    "WbemComparisonFlagEnum_wbemComparisonFlagIgnoreObjectSource",
    "WbemComparisonFlagEnum_wbemComparisonFlagIgnoreQualifiers",
    "WbemComparisonFlagEnum_wbemComparisonFlagIncludeAll",
    "WbemConnectOptionsEnum",
    "WbemConnectOptionsEnum_wbemConnectFlagUseMaxWait",
    "WbemContext",
    "WbemDCOMTransport",
    "WbemDecoupledBasicEventProvider",
    "WbemDecoupledRegistrar",
    "WbemDefPath",
    "WbemErrorEnum",
    "WbemErrorEnum_wbemErrAccessDenied",
    "WbemErrorEnum_wbemErrAggregatingByObject",
    "WbemErrorEnum_wbemErrAlreadyExists",
    "WbemErrorEnum_wbemErrAmbiguousOperation",
    "WbemErrorEnum_wbemErrAmendedObject",
    "WbemErrorEnum_wbemErrBackupRestoreWinmgmtRunning",
    "WbemErrorEnum_wbemErrBufferTooSmall",
    "WbemErrorEnum_wbemErrCallCancelled",
    "WbemErrorEnum_wbemErrCannotBeAbstract",
    "WbemErrorEnum_wbemErrCannotBeKey",
    "WbemErrorEnum_wbemErrCannotBeSingleton",
    "WbemErrorEnum_wbemErrCannotChangeIndexInheritance",
    "WbemErrorEnum_wbemErrCannotChangeKeyInheritance",
    "WbemErrorEnum_wbemErrCircularReference",
    "WbemErrorEnum_wbemErrClassHasChildren",
    "WbemErrorEnum_wbemErrClassHasInstances",
    "WbemErrorEnum_wbemErrClassNameTooWide",
    "WbemErrorEnum_wbemErrClientTooSlow",
    "WbemErrorEnum_wbemErrConnectionFailed",
    "WbemErrorEnum_wbemErrCriticalError",
    "WbemErrorEnum_wbemErrDatabaseVerMismatch",
    "WbemErrorEnum_wbemErrEncryptedConnectionRequired",
    "WbemErrorEnum_wbemErrFailed",
    "WbemErrorEnum_wbemErrFatalTransportError",
    "WbemErrorEnum_wbemErrForcedRollback",
    "WbemErrorEnum_wbemErrHandleOutOfDate",
    "WbemErrorEnum_wbemErrIllegalNull",
    "WbemErrorEnum_wbemErrIllegalOperation",
    "WbemErrorEnum_wbemErrIncompleteClass",
    "WbemErrorEnum_wbemErrInitializationFailure",
    "WbemErrorEnum_wbemErrInvalidAssociation",
    "WbemErrorEnum_wbemErrInvalidCimType",
    "WbemErrorEnum_wbemErrInvalidClass",
    "WbemErrorEnum_wbemErrInvalidContext",
    "WbemErrorEnum_wbemErrInvalidDuplicateParameter",
    "WbemErrorEnum_wbemErrInvalidFlavor",
    "WbemErrorEnum_wbemErrInvalidHandleRequest",
    "WbemErrorEnum_wbemErrInvalidLocale",
    "WbemErrorEnum_wbemErrInvalidMethod",
    "WbemErrorEnum_wbemErrInvalidMethodParameters",
    "WbemErrorEnum_wbemErrInvalidNamespace",
    "WbemErrorEnum_wbemErrInvalidObject",
    "WbemErrorEnum_wbemErrInvalidObjectPath",
    "WbemErrorEnum_wbemErrInvalidOperation",
    "WbemErrorEnum_wbemErrInvalidOperator",
    "WbemErrorEnum_wbemErrInvalidParameter",
    "WbemErrorEnum_wbemErrInvalidParameterId",
    "WbemErrorEnum_wbemErrInvalidProperty",
    "WbemErrorEnum_wbemErrInvalidPropertyType",
    "WbemErrorEnum_wbemErrInvalidProviderRegistration",
    "WbemErrorEnum_wbemErrInvalidQualifier",
    "WbemErrorEnum_wbemErrInvalidQualifierType",
    "WbemErrorEnum_wbemErrInvalidQuery",
    "WbemErrorEnum_wbemErrInvalidQueryType",
    "WbemErrorEnum_wbemErrInvalidStream",
    "WbemErrorEnum_wbemErrInvalidSuperclass",
    "WbemErrorEnum_wbemErrInvalidSyntax",
    "WbemErrorEnum_wbemErrLocalCredentials",
    "WbemErrorEnum_wbemErrMarshalInvalidSignature",
    "WbemErrorEnum_wbemErrMarshalVersionMismatch",
    "WbemErrorEnum_wbemErrMethodDisabled",
    "WbemErrorEnum_wbemErrMethodNameTooWide",
    "WbemErrorEnum_wbemErrMethodNotImplemented",
    "WbemErrorEnum_wbemErrMissingAggregationList",
    "WbemErrorEnum_wbemErrMissingGroupWithin",
    "WbemErrorEnum_wbemErrMissingParameter",
    "WbemErrorEnum_wbemErrNoSchema",
    "WbemErrorEnum_wbemErrNonConsecutiveParameterIds",
    "WbemErrorEnum_wbemErrNondecoratedObject",
    "WbemErrorEnum_wbemErrNotAvailable",
    "WbemErrorEnum_wbemErrNotEventClass",
    "WbemErrorEnum_wbemErrNotFound",
    "WbemErrorEnum_wbemErrNotSupported",
    "WbemErrorEnum_wbemErrNullSecurityDescriptor",
    "WbemErrorEnum_wbemErrOutOfDiskSpace",
    "WbemErrorEnum_wbemErrOutOfMemory",
    "WbemErrorEnum_wbemErrOverrideNotAllowed",
    "WbemErrorEnum_wbemErrParameterIdOnRetval",
    "WbemErrorEnum_wbemErrPrivilegeNotHeld",
    "WbemErrorEnum_wbemErrPropagatedMethod",
    "WbemErrorEnum_wbemErrPropagatedProperty",
    "WbemErrorEnum_wbemErrPropagatedQualifier",
    "WbemErrorEnum_wbemErrPropertyNameTooWide",
    "WbemErrorEnum_wbemErrPropertyNotAnObject",
    "WbemErrorEnum_wbemErrProviderAlreadyRegistered",
    "WbemErrorEnum_wbemErrProviderFailure",
    "WbemErrorEnum_wbemErrProviderLoadFailure",
    "WbemErrorEnum_wbemErrProviderNotCapable",
    "WbemErrorEnum_wbemErrProviderNotFound",
    "WbemErrorEnum_wbemErrProviderNotRegistered",
    "WbemErrorEnum_wbemErrProviderSuspended",
    "WbemErrorEnum_wbemErrQualifierNameTooWide",
    "WbemErrorEnum_wbemErrQueryNotImplemented",
    "WbemErrorEnum_wbemErrQueueOverflow",
    "WbemErrorEnum_wbemErrQuotaViolation",
    "WbemErrorEnum_wbemErrReadOnly",
    "WbemErrorEnum_wbemErrRefresherBusy",
    "WbemErrorEnum_wbemErrRegistrationTooBroad",
    "WbemErrorEnum_wbemErrRegistrationTooPrecise",
    "WbemErrorEnum_wbemErrRerunCommand",
    "WbemErrorEnum_wbemErrResetToDefault",
    "WbemErrorEnum_wbemErrServerTooBusy",
    "WbemErrorEnum_wbemErrShuttingDown",
    "WbemErrorEnum_wbemErrSynchronizationRequired",
    "WbemErrorEnum_wbemErrSystemProperty",
    "WbemErrorEnum_wbemErrTimedout",
    "WbemErrorEnum_wbemErrTimeout",
    "WbemErrorEnum_wbemErrTooManyProperties",
    "WbemErrorEnum_wbemErrTooMuchData",
    "WbemErrorEnum_wbemErrTransactionConflict",
    "WbemErrorEnum_wbemErrTransportFailure",
    "WbemErrorEnum_wbemErrTypeMismatch",
    "WbemErrorEnum_wbemErrUnexpected",
    "WbemErrorEnum_wbemErrUninterpretableProviderQuery",
    "WbemErrorEnum_wbemErrUnknownObjectType",
    "WbemErrorEnum_wbemErrUnknownPacketType",
    "WbemErrorEnum_wbemErrUnparsableQuery",
    "WbemErrorEnum_wbemErrUnsupportedClassUpdate",
    "WbemErrorEnum_wbemErrUnsupportedLocale",
    "WbemErrorEnum_wbemErrUnsupportedParameter",
    "WbemErrorEnum_wbemErrUnsupportedPutExtension",
    "WbemErrorEnum_wbemErrUpdateOverrideNotAllowed",
    "WbemErrorEnum_wbemErrUpdatePropagatedMethod",
    "WbemErrorEnum_wbemErrUpdateTypeMismatch",
    "WbemErrorEnum_wbemErrValueOutOfRange",
    "WbemErrorEnum_wbemErrVetoDelete",
    "WbemErrorEnum_wbemErrVetoPut",
    "WbemErrorEnum_wbemNoErr",
    "WbemFlagEnum",
    "WbemFlagEnum_wbemFlagBidirectional",
    "WbemFlagEnum_wbemFlagDirectRead",
    "WbemFlagEnum_wbemFlagDontSendStatus",
    "WbemFlagEnum_wbemFlagEnsureLocatable",
    "WbemFlagEnum_wbemFlagForwardOnly",
    "WbemFlagEnum_wbemFlagGetDefault",
    "WbemFlagEnum_wbemFlagNoErrorObject",
    "WbemFlagEnum_wbemFlagReturnErrorObject",
    "WbemFlagEnum_wbemFlagReturnImmediately",
    "WbemFlagEnum_wbemFlagReturnWhenComplete",
    "WbemFlagEnum_wbemFlagSendOnlySelected",
    "WbemFlagEnum_wbemFlagSendStatus",
    "WbemFlagEnum_wbemFlagSpawnInstance",
    "WbemFlagEnum_wbemFlagUseAmendedQualifiers",
    "WbemFlagEnum_wbemFlagUseCurrentTime",
    "WbemImpersonationLevelEnum",
    "WbemImpersonationLevelEnum_wbemImpersonationLevelAnonymous",
    "WbemImpersonationLevelEnum_wbemImpersonationLevelDelegate",
    "WbemImpersonationLevelEnum_wbemImpersonationLevelIdentify",
    "WbemImpersonationLevelEnum_wbemImpersonationLevelImpersonate",
    "WbemLevel1Login",
    "WbemLocalAddrRes",
    "WbemLocator",
    "WbemObjectTextFormatEnum",
    "WbemObjectTextFormatEnum_wbemObjectTextFormatCIMDTD20",
    "WbemObjectTextFormatEnum_wbemObjectTextFormatWMIDTD20",
    "WbemObjectTextSrc",
    "WbemPrivilegeEnum",
    "WbemPrivilegeEnum_wbemPrivilegeAudit",
    "WbemPrivilegeEnum_wbemPrivilegeBackup",
    "WbemPrivilegeEnum_wbemPrivilegeChangeNotify",
    "WbemPrivilegeEnum_wbemPrivilegeCreatePagefile",
    "WbemPrivilegeEnum_wbemPrivilegeCreatePermanent",
    "WbemPrivilegeEnum_wbemPrivilegeCreateToken",
    "WbemPrivilegeEnum_wbemPrivilegeDebug",
    "WbemPrivilegeEnum_wbemPrivilegeEnableDelegation",
    "WbemPrivilegeEnum_wbemPrivilegeIncreaseBasePriority",
    "WbemPrivilegeEnum_wbemPrivilegeIncreaseQuota",
    "WbemPrivilegeEnum_wbemPrivilegeLoadDriver",
    "WbemPrivilegeEnum_wbemPrivilegeLockMemory",
    "WbemPrivilegeEnum_wbemPrivilegeMachineAccount",
    "WbemPrivilegeEnum_wbemPrivilegeManageVolume",
    "WbemPrivilegeEnum_wbemPrivilegePrimaryToken",
    "WbemPrivilegeEnum_wbemPrivilegeProfileSingleProcess",
    "WbemPrivilegeEnum_wbemPrivilegeRemoteShutdown",
    "WbemPrivilegeEnum_wbemPrivilegeRestore",
    "WbemPrivilegeEnum_wbemPrivilegeSecurity",
    "WbemPrivilegeEnum_wbemPrivilegeShutdown",
    "WbemPrivilegeEnum_wbemPrivilegeSyncAgent",
    "WbemPrivilegeEnum_wbemPrivilegeSystemEnvironment",
    "WbemPrivilegeEnum_wbemPrivilegeSystemProfile",
    "WbemPrivilegeEnum_wbemPrivilegeSystemtime",
    "WbemPrivilegeEnum_wbemPrivilegeTakeOwnership",
    "WbemPrivilegeEnum_wbemPrivilegeTcb",
    "WbemPrivilegeEnum_wbemPrivilegeUndock",
    "WbemQuery",
    "WbemQueryFlagEnum",
    "WbemQueryFlagEnum_wbemQueryFlagDeep",
    "WbemQueryFlagEnum_wbemQueryFlagPrototype",
    "WbemQueryFlagEnum_wbemQueryFlagShallow",
    "WbemRefresher",
    "WbemStatusCodeText",
    "WbemTextFlagEnum",
    "WbemTextFlagEnum_wbemTextFlagNoFlavors",
    "WbemTimeout",
    "WbemTimeout_wbemTimeoutInfinite",
    "WbemUnauthenticatedLocator",
    "WbemUninitializedClassObject",
]
