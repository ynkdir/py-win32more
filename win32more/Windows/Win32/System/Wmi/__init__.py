from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Variant
import win32more.Windows.Win32.System.Wmi
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
def MI_Application_InitializeV1(flags: UInt32, applicationID: POINTER(UInt16), extendedError: POINTER(POINTER(win32more.Windows.Win32.System.Wmi.MI_Instance)), application: POINTER(win32more.Windows.Win32.System.Wmi.MI_Application)) -> win32more.Windows.Win32.System.Wmi.MI_Result: ...
CIMTYPE_ENUMERATION = Int32
CIM_ILLEGAL: win32more.Windows.Win32.System.Wmi.CIMTYPE_ENUMERATION = 4095
CIM_EMPTY: win32more.Windows.Win32.System.Wmi.CIMTYPE_ENUMERATION = 0
CIM_SINT8: win32more.Windows.Win32.System.Wmi.CIMTYPE_ENUMERATION = 16
CIM_UINT8: win32more.Windows.Win32.System.Wmi.CIMTYPE_ENUMERATION = 17
CIM_SINT16: win32more.Windows.Win32.System.Wmi.CIMTYPE_ENUMERATION = 2
CIM_UINT16: win32more.Windows.Win32.System.Wmi.CIMTYPE_ENUMERATION = 18
CIM_SINT32: win32more.Windows.Win32.System.Wmi.CIMTYPE_ENUMERATION = 3
CIM_UINT32: win32more.Windows.Win32.System.Wmi.CIMTYPE_ENUMERATION = 19
CIM_SINT64: win32more.Windows.Win32.System.Wmi.CIMTYPE_ENUMERATION = 20
CIM_UINT64: win32more.Windows.Win32.System.Wmi.CIMTYPE_ENUMERATION = 21
CIM_REAL32: win32more.Windows.Win32.System.Wmi.CIMTYPE_ENUMERATION = 4
CIM_REAL64: win32more.Windows.Win32.System.Wmi.CIMTYPE_ENUMERATION = 5
CIM_BOOLEAN: win32more.Windows.Win32.System.Wmi.CIMTYPE_ENUMERATION = 11
CIM_STRING: win32more.Windows.Win32.System.Wmi.CIMTYPE_ENUMERATION = 8
CIM_DATETIME: win32more.Windows.Win32.System.Wmi.CIMTYPE_ENUMERATION = 101
CIM_REFERENCE: win32more.Windows.Win32.System.Wmi.CIMTYPE_ENUMERATION = 102
CIM_CHAR16: win32more.Windows.Win32.System.Wmi.CIMTYPE_ENUMERATION = 103
CIM_OBJECT: win32more.Windows.Win32.System.Wmi.CIMTYPE_ENUMERATION = 13
CIM_FLAG_ARRAY: win32more.Windows.Win32.System.Wmi.CIMTYPE_ENUMERATION = 8192
class IEnumWbemClassObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{027947e1-d731-11ce-a357-000000000001}')
    @commethod(3)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(self, lTimeout: Int32, uCount: UInt32, apObjects: POINTER(win32more.Windows.Win32.System.Wmi.IWbemClassObject), puReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def NextAsync(self, uCount: UInt32, pSink: win32more.Windows.Win32.System.Wmi.IWbemObjectSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.System.Wmi.IEnumWbemClassObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Skip(self, lTimeout: Int32, nCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMofCompiler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6daf974e-2e37-11d2-aec9-00c04fb68820}')
    @commethod(3)
    def CompileFile(self, FileName: win32more.Windows.Win32.Foundation.PWSTR, ServerAndNamespace: win32more.Windows.Win32.Foundation.PWSTR, User: win32more.Windows.Win32.Foundation.PWSTR, Authority: win32more.Windows.Win32.Foundation.PWSTR, Password: win32more.Windows.Win32.Foundation.PWSTR, lOptionFlags: Int32, lClassFlags: Int32, lInstanceFlags: Int32, pInfo: POINTER(win32more.Windows.Win32.System.Wmi.WBEM_COMPILE_STATUS_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CompileBuffer(self, BuffSize: Int32, pBuffer: POINTER(Byte), ServerAndNamespace: win32more.Windows.Win32.Foundation.PWSTR, User: win32more.Windows.Win32.Foundation.PWSTR, Authority: win32more.Windows.Win32.Foundation.PWSTR, Password: win32more.Windows.Win32.Foundation.PWSTR, lOptionFlags: Int32, lClassFlags: Int32, lInstanceFlags: Int32, pInfo: POINTER(win32more.Windows.Win32.System.Wmi.WBEM_COMPILE_STATUS_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateBMOF(self, TextFileName: win32more.Windows.Win32.Foundation.PWSTR, BMOFFileName: win32more.Windows.Win32.Foundation.PWSTR, ServerAndNamespace: win32more.Windows.Win32.Foundation.PWSTR, lOptionFlags: Int32, lClassFlags: Int32, lInstanceFlags: Int32, pInfo: POINTER(win32more.Windows.Win32.System.Wmi.WBEM_COMPILE_STATUS_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISWbemDateTime(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{5e97458a-cf77-11d3-b38f-00105a1f473a}')
    @commethod(7)
    def get_Value(self, strValue: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Value(self, strValue: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Year(self, iYear: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Year(self, iYear: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_YearSpecified(self, bYearSpecified: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_YearSpecified(self, bYearSpecified: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Month(self, iMonth: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Month(self, iMonth: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_MonthSpecified(self, bMonthSpecified: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_MonthSpecified(self, bMonthSpecified: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Day(self, iDay: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_Day(self, iDay: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_DaySpecified(self, bDaySpecified: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_DaySpecified(self, bDaySpecified: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_Hours(self, iHours: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_Hours(self, iHours: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_HoursSpecified(self, bHoursSpecified: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_HoursSpecified(self, bHoursSpecified: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_Minutes(self, iMinutes: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_Minutes(self, iMinutes: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_MinutesSpecified(self, bMinutesSpecified: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_MinutesSpecified(self, bMinutesSpecified: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_Seconds(self, iSeconds: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_Seconds(self, iSeconds: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_SecondsSpecified(self, bSecondsSpecified: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_SecondsSpecified(self, bSecondsSpecified: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_Microseconds(self, iMicroseconds: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def put_Microseconds(self, iMicroseconds: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def get_MicrosecondsSpecified(self, bMicrosecondsSpecified: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def put_MicrosecondsSpecified(self, bMicrosecondsSpecified: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_UTC(self, iUTC: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def put_UTC(self, iUTC: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def get_UTCSpecified(self, bUTCSpecified: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def put_UTCSpecified(self, bUTCSpecified: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def get_IsInterval(self, bIsInterval: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def put_IsInterval(self, bIsInterval: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def GetVarDate(self, bIsLocal: win32more.Windows.Win32.Foundation.VARIANT_BOOL, dVarDate: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def SetVarDate(self, dVarDate: Double, bIsLocal: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def GetFileTime(self, bIsLocal: win32more.Windows.Win32.Foundation.VARIANT_BOOL, strFileTime: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def SetFileTime(self, strFileTime: win32more.Windows.Win32.Foundation.BSTR, bIsLocal: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISWbemEventSource(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{27d54d92-0ebe-11d2-8b22-00600806d9b6}')
    @commethod(7)
    def NextEvent(self, iTimeoutMs: Int32, objWbemObject: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Security_(self, objWbemSecurity: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemSecurity)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISWbemLastError(ComPtr):
    extends: win32more.Windows.Win32.System.Wmi.ISWbemObject
    _iid_ = Guid('{d962db84-d4bb-11d1-8b09-00600806d9b6}')
class ISWbemLocator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{76a6415b-cb41-11d1-8b02-00600806d9b6}')
    @commethod(7)
    def ConnectServer(self, strServer: win32more.Windows.Win32.Foundation.BSTR, strNamespace: win32more.Windows.Win32.Foundation.BSTR, strUser: win32more.Windows.Win32.Foundation.BSTR, strPassword: win32more.Windows.Win32.Foundation.BSTR, strLocale: win32more.Windows.Win32.Foundation.BSTR, strAuthority: win32more.Windows.Win32.Foundation.BSTR, iSecurityFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemServices: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemServices)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Security_(self, objWbemSecurity: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemSecurity)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISWbemMethod(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{422e8e90-d955-11d1-8b09-00600806d9b6}')
    @commethod(7)
    def get_Name(self, strName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Origin(self, strOrigin: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_InParameters(self, objWbemInParameters: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_OutParameters(self, objWbemOutParameters: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Qualifiers_(self, objWbemQualifierSet: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemQualifierSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISWbemMethodSet(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c93ba292-d955-11d1-8b09-00600806d9b6}')
    @commethod(7)
    def get__NewEnum(self, pUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, strName: win32more.Windows.Win32.Foundation.BSTR, iFlags: Int32, objWbemMethod: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemMethod)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, iCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISWbemNamedValue(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{76a64164-cb41-11d1-8b02-00600806d9b6}')
    @commethod(7)
    def get_Value(self, varValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Value(self, varValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(self, strName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISWbemNamedValueSet(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{cf2376ea-ce8c-11d1-8b05-00600806d9b6}')
    @commethod(7)
    def get__NewEnum(self, pUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, strName: win32more.Windows.Win32.Foundation.BSTR, iFlags: Int32, objWbemNamedValue: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemNamedValue)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, iCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, strName: win32more.Windows.Win32.Foundation.BSTR, varValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), iFlags: Int32, objWbemNamedValue: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemNamedValue)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, strName: win32more.Windows.Win32.Foundation.BSTR, iFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Clone(self, objWbemNamedValueSet: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemNamedValueSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def DeleteAll(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISWbemObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{76a6415a-cb41-11d1-8b02-00600806d9b6}')
    @commethod(7)
    def Put_(self, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemObjectPath: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemObjectPath)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def PutAsync_(self, objWbemSink: win32more.Windows.Win32.System.Com.IDispatch, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemAsyncContext: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Delete_(self, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def DeleteAsync_(self, objWbemSink: win32more.Windows.Win32.System.Com.IDispatch, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemAsyncContext: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Instances_(self, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemObjectSet: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemObjectSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def InstancesAsync_(self, objWbemSink: win32more.Windows.Win32.System.Com.IDispatch, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemAsyncContext: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Subclasses_(self, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemObjectSet: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemObjectSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SubclassesAsync_(self, objWbemSink: win32more.Windows.Win32.System.Com.IDispatch, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemAsyncContext: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Associators_(self, strAssocClass: win32more.Windows.Win32.Foundation.BSTR, strResultClass: win32more.Windows.Win32.Foundation.BSTR, strResultRole: win32more.Windows.Win32.Foundation.BSTR, strRole: win32more.Windows.Win32.Foundation.BSTR, bClassesOnly: win32more.Windows.Win32.Foundation.VARIANT_BOOL, bSchemaOnly: win32more.Windows.Win32.Foundation.VARIANT_BOOL, strRequiredAssocQualifier: win32more.Windows.Win32.Foundation.BSTR, strRequiredQualifier: win32more.Windows.Win32.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemObjectSet: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemObjectSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def AssociatorsAsync_(self, objWbemSink: win32more.Windows.Win32.System.Com.IDispatch, strAssocClass: win32more.Windows.Win32.Foundation.BSTR, strResultClass: win32more.Windows.Win32.Foundation.BSTR, strResultRole: win32more.Windows.Win32.Foundation.BSTR, strRole: win32more.Windows.Win32.Foundation.BSTR, bClassesOnly: win32more.Windows.Win32.Foundation.VARIANT_BOOL, bSchemaOnly: win32more.Windows.Win32.Foundation.VARIANT_BOOL, strRequiredAssocQualifier: win32more.Windows.Win32.Foundation.BSTR, strRequiredQualifier: win32more.Windows.Win32.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemAsyncContext: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def References_(self, strResultClass: win32more.Windows.Win32.Foundation.BSTR, strRole: win32more.Windows.Win32.Foundation.BSTR, bClassesOnly: win32more.Windows.Win32.Foundation.VARIANT_BOOL, bSchemaOnly: win32more.Windows.Win32.Foundation.VARIANT_BOOL, strRequiredQualifier: win32more.Windows.Win32.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemObjectSet: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemObjectSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def ReferencesAsync_(self, objWbemSink: win32more.Windows.Win32.System.Com.IDispatch, strResultClass: win32more.Windows.Win32.Foundation.BSTR, strRole: win32more.Windows.Win32.Foundation.BSTR, bClassesOnly: win32more.Windows.Win32.Foundation.VARIANT_BOOL, bSchemaOnly: win32more.Windows.Win32.Foundation.VARIANT_BOOL, strRequiredQualifier: win32more.Windows.Win32.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemAsyncContext: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def ExecMethod_(self, strMethodName: win32more.Windows.Win32.Foundation.BSTR, objWbemInParameters: win32more.Windows.Win32.System.Com.IDispatch, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemOutParameters: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def ExecMethodAsync_(self, objWbemSink: win32more.Windows.Win32.System.Com.IDispatch, strMethodName: win32more.Windows.Win32.Foundation.BSTR, objWbemInParameters: win32more.Windows.Win32.System.Com.IDispatch, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemAsyncContext: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Clone_(self, objWbemObject: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetObjectText_(self, iFlags: Int32, strObjectText: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SpawnDerivedClass_(self, iFlags: Int32, objWbemObject: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SpawnInstance_(self, iFlags: Int32, objWbemObject: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def CompareTo_(self, objWbemObject: win32more.Windows.Win32.System.Com.IDispatch, iFlags: Int32, bResult: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_Qualifiers_(self, objWbemQualifierSet: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemQualifierSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_Properties_(self, objWbemPropertySet: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemPropertySet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_Methods_(self, objWbemMethodSet: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemMethodSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_Derivation_(self, strClassNameArray: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_Path_(self, objWbemObjectPath: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemObjectPath)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_Security_(self, objWbemSecurity: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemSecurity)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISWbemObjectEx(ComPtr):
    extends: win32more.Windows.Win32.System.Wmi.ISWbemObject
    _iid_ = Guid('{269ad56a-8a67-4129-bc8c-0506dcfe9880}')
    @commethod(32)
    def Refresh_(self, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_SystemProperties_(self, objWbemPropertySet: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemPropertySet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetText_(self, iObjectTextFormat: win32more.Windows.Win32.System.Wmi.WbemObjectTextFormatEnum, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, bsText: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def SetFromText_(self, bsText: win32more.Windows.Win32.Foundation.BSTR, iObjectTextFormat: win32more.Windows.Win32.System.Wmi.WbemObjectTextFormatEnum, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISWbemObjectPath(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{5791bc27-ce9c-11d1-97bf-0000f81e849c}')
    @commethod(7)
    def get_Path(self, strPath: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Path(self, strPath: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_RelPath(self, strRelPath: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_RelPath(self, strRelPath: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Server(self, strServer: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Server(self, strServer: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Namespace(self, strNamespace: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Namespace(self, strNamespace: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_ParentNamespace(self, strParentNamespace: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_DisplayName(self, strDisplayName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_DisplayName(self, strDisplayName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_Class(self, strClass: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_Class(self, strClass: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_IsClass(self, bIsClass: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetAsClass(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_IsSingleton(self, bIsSingleton: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetAsSingleton(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_Keys(self, objWbemNamedValueSet: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemNamedValueSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_Security_(self, objWbemSecurity: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemSecurity)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_Locale(self, strLocale: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_Locale(self, strLocale: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_Authority(self, strAuthority: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_Authority(self, strAuthority: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISWbemObjectSet(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{76a6415f-cb41-11d1-8b02-00600806d9b6}')
    @commethod(7)
    def get__NewEnum(self, pUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, strObjectPath: win32more.Windows.Win32.Foundation.BSTR, iFlags: Int32, objWbemObject: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, iCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Security_(self, objWbemSecurity: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemSecurity)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ItemIndex(self, lIndex: Int32, objWbemObject: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISWbemPrivilege(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{26ee67bd-5804-11d2-8b4a-00600806d9b6}')
    @commethod(7)
    def get_IsEnabled(self, bIsEnabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_IsEnabled(self, bIsEnabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(self, strDisplayName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_DisplayName(self, strDisplayName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Identifier(self, iPrivilege: POINTER(win32more.Windows.Win32.System.Wmi.WbemPrivilegeEnum)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISWbemPrivilegeSet(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{26ee67bf-5804-11d2-8b4a-00600806d9b6}')
    @commethod(7)
    def get__NewEnum(self, pUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, iPrivilege: win32more.Windows.Win32.System.Wmi.WbemPrivilegeEnum, objWbemPrivilege: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemPrivilege)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, iCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, iPrivilege: win32more.Windows.Win32.System.Wmi.WbemPrivilegeEnum, bIsEnabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL, objWbemPrivilege: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemPrivilege)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, iPrivilege: win32more.Windows.Win32.System.Wmi.WbemPrivilegeEnum) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def DeleteAll(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def AddAsString(self, strPrivilege: win32more.Windows.Win32.Foundation.BSTR, bIsEnabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL, objWbemPrivilege: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemPrivilege)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISWbemProperty(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{1a388f98-d4ba-11d1-8b09-00600806d9b6}')
    @commethod(7)
    def get_Value(self, varValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Value(self, varValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(self, strName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_IsLocal(self, bIsLocal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Origin(self, strOrigin: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_CIMType(self, iCimType: POINTER(win32more.Windows.Win32.System.Wmi.WbemCimtypeEnum)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Qualifiers_(self, objWbemQualifierSet: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemQualifierSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_IsArray(self, bIsArray: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISWbemPropertySet(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{dea0a7b2-d4ba-11d1-8b09-00600806d9b6}')
    @commethod(7)
    def get__NewEnum(self, pUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, strName: win32more.Windows.Win32.Foundation.BSTR, iFlags: Int32, objWbemProperty: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemProperty)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, iCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, strName: win32more.Windows.Win32.Foundation.BSTR, iCIMType: win32more.Windows.Win32.System.Wmi.WbemCimtypeEnum, bIsArray: win32more.Windows.Win32.Foundation.VARIANT_BOOL, iFlags: Int32, objWbemProperty: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemProperty)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, strName: win32more.Windows.Win32.Foundation.BSTR, iFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISWbemQualifier(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{79b05932-d3b7-11d1-8b06-00600806d9b6}')
    @commethod(7)
    def get_Value(self, varValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Value(self, varValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(self, strName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_IsLocal(self, bIsLocal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_PropagatesToSubclass(self, bPropagatesToSubclass: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_PropagatesToSubclass(self, bPropagatesToSubclass: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_PropagatesToInstance(self, bPropagatesToInstance: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_PropagatesToInstance(self, bPropagatesToInstance: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_IsOverridable(self, bIsOverridable: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_IsOverridable(self, bIsOverridable: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_IsAmended(self, bIsAmended: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISWbemQualifierSet(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{9b16ed16-d3df-11d1-8b08-00600806d9b6}')
    @commethod(7)
    def get__NewEnum(self, pUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, name: win32more.Windows.Win32.Foundation.BSTR, iFlags: Int32, objWbemQualifier: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemQualifier)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, iCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, strName: win32more.Windows.Win32.Foundation.BSTR, varVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), bPropagatesToSubclass: win32more.Windows.Win32.Foundation.VARIANT_BOOL, bPropagatesToInstance: win32more.Windows.Win32.Foundation.VARIANT_BOOL, bIsOverridable: win32more.Windows.Win32.Foundation.VARIANT_BOOL, iFlags: Int32, objWbemQualifier: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemQualifier)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Remove(self, strName: win32more.Windows.Win32.Foundation.BSTR, iFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISWbemRefreshableItem(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{5ad4bf92-daab-11d3-b38f-00105a1f473a}')
    @commethod(7)
    def get_Index(self, iIndex: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Refresher(self, objWbemRefresher: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemRefresher)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_IsSet(self, bIsSet: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Object(self, objWbemObject: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemObjectEx)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ObjectSet(self, objWbemObjectSet: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemObjectSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Remove(self, iFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISWbemRefresher(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{14d8250e-d9c2-11d3-b38f-00105a1f473a}')
    @commethod(7)
    def get__NewEnum(self, pUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, iIndex: Int32, objWbemRefreshableItem: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemRefreshableItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, iCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Add(self, objWbemServices: win32more.Windows.Win32.System.Wmi.ISWbemServicesEx, bsInstancePath: win32more.Windows.Win32.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemRefreshableItem: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemRefreshableItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AddEnum(self, objWbemServices: win32more.Windows.Win32.System.Wmi.ISWbemServicesEx, bsClassName: win32more.Windows.Win32.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemRefreshableItem: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemRefreshableItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Remove(self, iIndex: Int32, iFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Refresh(self, iFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_AutoReconnect(self, bCount: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_AutoReconnect(self, bCount: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def DeleteAll(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISWbemSecurity(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{b54d66e6-2287-11d2-8b33-00600806d9b6}')
    @commethod(7)
    def get_ImpersonationLevel(self, iImpersonationLevel: POINTER(win32more.Windows.Win32.System.Wmi.WbemImpersonationLevelEnum)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_ImpersonationLevel(self, iImpersonationLevel: win32more.Windows.Win32.System.Wmi.WbemImpersonationLevelEnum) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_AuthenticationLevel(self, iAuthenticationLevel: POINTER(win32more.Windows.Win32.System.Wmi.WbemAuthenticationLevelEnum)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_AuthenticationLevel(self, iAuthenticationLevel: win32more.Windows.Win32.System.Wmi.WbemAuthenticationLevelEnum) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Privileges(self, objWbemPrivilegeSet: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemPrivilegeSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISWbemServices(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{76a6415c-cb41-11d1-8b02-00600806d9b6}')
    @commethod(7)
    def Get(self, strObjectPath: win32more.Windows.Win32.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemObject: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetAsync(self, objWbemSink: win32more.Windows.Win32.System.Com.IDispatch, strObjectPath: win32more.Windows.Win32.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemAsyncContext: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Delete(self, strObjectPath: win32more.Windows.Win32.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def DeleteAsync(self, objWbemSink: win32more.Windows.Win32.System.Com.IDispatch, strObjectPath: win32more.Windows.Win32.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemAsyncContext: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def InstancesOf(self, strClass: win32more.Windows.Win32.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemObjectSet: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemObjectSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def InstancesOfAsync(self, objWbemSink: win32more.Windows.Win32.System.Com.IDispatch, strClass: win32more.Windows.Win32.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemAsyncContext: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SubclassesOf(self, strSuperclass: win32more.Windows.Win32.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemObjectSet: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemObjectSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SubclassesOfAsync(self, objWbemSink: win32more.Windows.Win32.System.Com.IDispatch, strSuperclass: win32more.Windows.Win32.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemAsyncContext: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ExecQuery(self, strQuery: win32more.Windows.Win32.Foundation.BSTR, strQueryLanguage: win32more.Windows.Win32.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemObjectSet: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemObjectSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def ExecQueryAsync(self, objWbemSink: win32more.Windows.Win32.System.Com.IDispatch, strQuery: win32more.Windows.Win32.Foundation.BSTR, strQueryLanguage: win32more.Windows.Win32.Foundation.BSTR, lFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemAsyncContext: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def AssociatorsOf(self, strObjectPath: win32more.Windows.Win32.Foundation.BSTR, strAssocClass: win32more.Windows.Win32.Foundation.BSTR, strResultClass: win32more.Windows.Win32.Foundation.BSTR, strResultRole: win32more.Windows.Win32.Foundation.BSTR, strRole: win32more.Windows.Win32.Foundation.BSTR, bClassesOnly: win32more.Windows.Win32.Foundation.VARIANT_BOOL, bSchemaOnly: win32more.Windows.Win32.Foundation.VARIANT_BOOL, strRequiredAssocQualifier: win32more.Windows.Win32.Foundation.BSTR, strRequiredQualifier: win32more.Windows.Win32.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemObjectSet: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemObjectSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def AssociatorsOfAsync(self, objWbemSink: win32more.Windows.Win32.System.Com.IDispatch, strObjectPath: win32more.Windows.Win32.Foundation.BSTR, strAssocClass: win32more.Windows.Win32.Foundation.BSTR, strResultClass: win32more.Windows.Win32.Foundation.BSTR, strResultRole: win32more.Windows.Win32.Foundation.BSTR, strRole: win32more.Windows.Win32.Foundation.BSTR, bClassesOnly: win32more.Windows.Win32.Foundation.VARIANT_BOOL, bSchemaOnly: win32more.Windows.Win32.Foundation.VARIANT_BOOL, strRequiredAssocQualifier: win32more.Windows.Win32.Foundation.BSTR, strRequiredQualifier: win32more.Windows.Win32.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemAsyncContext: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def ReferencesTo(self, strObjectPath: win32more.Windows.Win32.Foundation.BSTR, strResultClass: win32more.Windows.Win32.Foundation.BSTR, strRole: win32more.Windows.Win32.Foundation.BSTR, bClassesOnly: win32more.Windows.Win32.Foundation.VARIANT_BOOL, bSchemaOnly: win32more.Windows.Win32.Foundation.VARIANT_BOOL, strRequiredQualifier: win32more.Windows.Win32.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemObjectSet: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemObjectSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def ReferencesToAsync(self, objWbemSink: win32more.Windows.Win32.System.Com.IDispatch, strObjectPath: win32more.Windows.Win32.Foundation.BSTR, strResultClass: win32more.Windows.Win32.Foundation.BSTR, strRole: win32more.Windows.Win32.Foundation.BSTR, bClassesOnly: win32more.Windows.Win32.Foundation.VARIANT_BOOL, bSchemaOnly: win32more.Windows.Win32.Foundation.VARIANT_BOOL, strRequiredQualifier: win32more.Windows.Win32.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemAsyncContext: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def ExecNotificationQuery(self, strQuery: win32more.Windows.Win32.Foundation.BSTR, strQueryLanguage: win32more.Windows.Win32.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemEventSource: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemEventSource)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def ExecNotificationQueryAsync(self, objWbemSink: win32more.Windows.Win32.System.Com.IDispatch, strQuery: win32more.Windows.Win32.Foundation.BSTR, strQueryLanguage: win32more.Windows.Win32.Foundation.BSTR, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemAsyncContext: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def ExecMethod(self, strObjectPath: win32more.Windows.Win32.Foundation.BSTR, strMethodName: win32more.Windows.Win32.Foundation.BSTR, objWbemInParameters: win32more.Windows.Win32.System.Com.IDispatch, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemOutParameters: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def ExecMethodAsync(self, objWbemSink: win32more.Windows.Win32.System.Com.IDispatch, strObjectPath: win32more.Windows.Win32.Foundation.BSTR, strMethodName: win32more.Windows.Win32.Foundation.BSTR, objWbemInParameters: win32more.Windows.Win32.System.Com.IDispatch, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemAsyncContext: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_Security_(self, objWbemSecurity: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemSecurity)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISWbemServicesEx(ComPtr):
    extends: win32more.Windows.Win32.System.Wmi.ISWbemServices
    _iid_ = Guid('{d2f68443-85dc-427e-91d8-366554cc754c}')
    @commethod(26)
    def Put(self, objWbemObject: win32more.Windows.Win32.System.Wmi.ISWbemObjectEx, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemObjectPath: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemObjectPath)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def PutAsync(self, objWbemSink: win32more.Windows.Win32.System.Wmi.ISWbemSink, objWbemObject: win32more.Windows.Win32.System.Wmi.ISWbemObjectEx, iFlags: Int32, objWbemNamedValueSet: win32more.Windows.Win32.System.Com.IDispatch, objWbemAsyncContext: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISWbemSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{75718c9f-f029-11d1-a1ac-00c04fb6c223}')
    @commethod(7)
    def Cancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISWbemSinkEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{75718ca0-f029-11d1-a1ac-00c04fb6c223}')
class IUnsecuredApartment(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1cfaba8c-1523-11d1-ad79-00c04fd8fdff}')
    @commethod(3)
    def CreateObjectStub(self, pObject: win32more.Windows.Win32.System.Com.IUnknown, ppStub: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWMIExtension(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{adc1f06e-5c7e-11d2-8b74-00104b2afb41}')
    @commethod(7)
    def get_WMIObjectPath(self, strWMIObjectPath: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetWMIObject(self, objWMIObject: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetWMIServices(self, objWMIServices: POINTER(win32more.Windows.Win32.System.Wmi.ISWbemServices)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemAddressResolution(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f7ce2e12-8c90-11d1-9e7b-00c04fc324a8}')
    @commethod(3)
    def Resolve(self, wszNamespacePath: win32more.Windows.Win32.Foundation.PWSTR, wszAddressType: win32more.Windows.Win32.Foundation.PWSTR, pdwAddressLength: POINTER(UInt32), pabBinaryAddress: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemBackupRestore(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c49e32c7-bc8b-11d2-85d4-00105a1f8304}')
    @commethod(3)
    def Backup(self, strBackupToFile: win32more.Windows.Win32.Foundation.PWSTR, lFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Restore(self, strRestoreFromFile: win32more.Windows.Win32.Foundation.PWSTR, lFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemBackupRestoreEx(ComPtr):
    extends: win32more.Windows.Win32.System.Wmi.IWbemBackupRestore
    _iid_ = Guid('{a359dec5-e813-4834-8a2a-ba7f1d777d76}')
    @commethod(5)
    def Pause(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Resume(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemCallResult(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{44aca675-e8fc-11d0-a07c-00c04fb68820}')
    @commethod(3)
    def GetResultObject(self, lTimeout: Int32, ppResultObject: POINTER(win32more.Windows.Win32.System.Wmi.IWbemClassObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetResultString(self, lTimeout: Int32, pstrResultString: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetResultServices(self, lTimeout: Int32, ppServices: POINTER(win32more.Windows.Win32.System.Wmi.IWbemServices)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCallStatus(self, lTimeout: Int32, plStatus: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemClassObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dc12a681-737f-11cf-884d-00aa004b2e24}')
    @commethod(3)
    def GetQualifierSet(self, ppQualSet: POINTER(win32more.Windows.Win32.System.Wmi.IWbemQualifierSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Get(self, wszName: win32more.Windows.Win32.Foundation.PWSTR, lFlags: Int32, pVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pType: POINTER(Int32), plFlavor: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Put(self, wszName: win32more.Windows.Win32.Foundation.PWSTR, lFlags: Int32, pVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), Type: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Delete(self, wszName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetNames(self, wszQualifierName: win32more.Windows.Win32.Foundation.PWSTR, lFlags: win32more.Windows.Win32.System.Wmi.WBEM_CONDITION_FLAG_TYPE, pQualifierVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pNames: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def BeginEnumeration(self, lEnumFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Next(self, lFlags: Int32, strName: POINTER(win32more.Windows.Win32.Foundation.BSTR), pVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pType: POINTER(Int32), plFlavor: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EndEnumeration(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetPropertyQualifierSet(self, wszProperty: win32more.Windows.Win32.Foundation.PWSTR, ppQualSet: POINTER(win32more.Windows.Win32.System.Wmi.IWbemQualifierSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Clone(self, ppCopy: POINTER(win32more.Windows.Win32.System.Wmi.IWbemClassObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetObjectText(self, lFlags: Int32, pstrObjectText: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SpawnDerivedClass(self, lFlags: Int32, ppNewClass: POINTER(win32more.Windows.Win32.System.Wmi.IWbemClassObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SpawnInstance(self, lFlags: Int32, ppNewInstance: POINTER(win32more.Windows.Win32.System.Wmi.IWbemClassObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def CompareTo(self, lFlags: win32more.Windows.Win32.System.Wmi.WBEM_COMPARISON_FLAG, pCompareTo: win32more.Windows.Win32.System.Wmi.IWbemClassObject) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetPropertyOrigin(self, wszName: win32more.Windows.Win32.Foundation.PWSTR, pstrClassName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def InheritsFrom(self, strAncestor: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetMethod(self, wszName: win32more.Windows.Win32.Foundation.PWSTR, lFlags: Int32, ppInSignature: POINTER(win32more.Windows.Win32.System.Wmi.IWbemClassObject), ppOutSignature: POINTER(win32more.Windows.Win32.System.Wmi.IWbemClassObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def PutMethod(self, wszName: win32more.Windows.Win32.Foundation.PWSTR, lFlags: Int32, pInSignature: win32more.Windows.Win32.System.Wmi.IWbemClassObject, pOutSignature: win32more.Windows.Win32.System.Wmi.IWbemClassObject) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def DeleteMethod(self, wszName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def BeginMethodEnumeration(self, lEnumFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def NextMethod(self, lFlags: Int32, pstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR), ppInSignature: POINTER(win32more.Windows.Win32.System.Wmi.IWbemClassObject), ppOutSignature: POINTER(win32more.Windows.Win32.System.Wmi.IWbemClassObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def EndMethodEnumeration(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetMethodQualifierSet(self, wszMethod: win32more.Windows.Win32.Foundation.PWSTR, ppQualSet: POINTER(win32more.Windows.Win32.System.Wmi.IWbemQualifierSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetMethodOrigin(self, wszMethodName: win32more.Windows.Win32.Foundation.PWSTR, pstrClassName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemClientConnectionTransport(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a889c72a-fcc1-4a9e-af61-ed071333fb5b}')
    @commethod(3)
    def Open(self, strAddressType: win32more.Windows.Win32.Foundation.BSTR, dwBinaryAddressLength: UInt32, abBinaryAddress: POINTER(Byte), strObject: win32more.Windows.Win32.Foundation.BSTR, strUser: win32more.Windows.Win32.Foundation.BSTR, strPassword: win32more.Windows.Win32.Foundation.BSTR, strLocale: win32more.Windows.Win32.Foundation.BSTR, lFlags: Int32, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, riid: POINTER(Guid), pInterface: POINTER(VoidPtr), pCallRes: POINTER(win32more.Windows.Win32.System.Wmi.IWbemCallResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OpenAsync(self, strAddressType: win32more.Windows.Win32.Foundation.BSTR, dwBinaryAddressLength: UInt32, abBinaryAddress: POINTER(Byte), strObject: win32more.Windows.Win32.Foundation.BSTR, strUser: win32more.Windows.Win32.Foundation.BSTR, strPassword: win32more.Windows.Win32.Foundation.BSTR, strLocale: win32more.Windows.Win32.Foundation.BSTR, lFlags: Int32, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, riid: POINTER(Guid), pResponseHandler: win32more.Windows.Win32.System.Wmi.IWbemObjectSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Cancel(self, lFlags: Int32, pHandler: win32more.Windows.Win32.System.Wmi.IWbemObjectSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemClientTransport(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f7ce2e11-8c90-11d1-9e7b-00c04fc324a8}')
    @commethod(3)
    def ConnectServer(self, strAddressType: win32more.Windows.Win32.Foundation.BSTR, dwBinaryAddressLength: UInt32, abBinaryAddress: POINTER(Byte), strNetworkResource: win32more.Windows.Win32.Foundation.BSTR, strUser: win32more.Windows.Win32.Foundation.BSTR, strPassword: win32more.Windows.Win32.Foundation.BSTR, strLocale: win32more.Windows.Win32.Foundation.BSTR, lSecurityFlags: Int32, strAuthority: win32more.Windows.Win32.Foundation.BSTR, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, ppNamespace: POINTER(win32more.Windows.Win32.System.Wmi.IWbemServices)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemConfigureRefresher(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{49353c92-516b-11d1-aea6-00c04fb68820}')
    @commethod(3)
    def AddObjectByPath(self, pNamespace: win32more.Windows.Win32.System.Wmi.IWbemServices, wszPath: win32more.Windows.Win32.Foundation.PWSTR, lFlags: Int32, pContext: win32more.Windows.Win32.System.Wmi.IWbemContext, ppRefreshable: POINTER(win32more.Windows.Win32.System.Wmi.IWbemClassObject), plId: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddObjectByTemplate(self, pNamespace: win32more.Windows.Win32.System.Wmi.IWbemServices, pTemplate: win32more.Windows.Win32.System.Wmi.IWbemClassObject, lFlags: Int32, pContext: win32more.Windows.Win32.System.Wmi.IWbemContext, ppRefreshable: POINTER(win32more.Windows.Win32.System.Wmi.IWbemClassObject), plId: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddRefresher(self, pRefresher: win32more.Windows.Win32.System.Wmi.IWbemRefresher, lFlags: Int32, plId: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Remove(self, lId: Int32, lFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddEnum(self, pNamespace: win32more.Windows.Win32.System.Wmi.IWbemServices, wszClassName: win32more.Windows.Win32.Foundation.PWSTR, lFlags: Int32, pContext: win32more.Windows.Win32.System.Wmi.IWbemContext, ppEnum: POINTER(win32more.Windows.Win32.System.Wmi.IWbemHiPerfEnum), plId: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemConnectorLogin(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d8ec9cb1-b135-4f10-8b1b-c7188bb0d186}')
    @commethod(3)
    def ConnectorLogin(self, wszNetworkResource: win32more.Windows.Win32.Foundation.PWSTR, wszPreferredLocale: win32more.Windows.Win32.Foundation.PWSTR, lFlags: Int32, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, riid: POINTER(Guid), pInterface: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemConstructClassObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9ef76194-70d5-11d1-ad90-00c04fd8fdff}')
    @commethod(3)
    def SetInheritanceChain(self, lNumAntecedents: Int32, awszAntecedents: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetPropertyOrigin(self, wszPropertyName: win32more.Windows.Win32.Foundation.PWSTR, lOriginIndex: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetMethodOrigin(self, wszMethodName: win32more.Windows.Win32.Foundation.PWSTR, lOriginIndex: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetServerNamespace(self, wszServer: win32more.Windows.Win32.Foundation.PWSTR, wszNamespace: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{44aca674-e8fc-11d0-a07c-00c04fb68820}')
    @commethod(3)
    def Clone(self, ppNewCopy: POINTER(win32more.Windows.Win32.System.Wmi.IWbemContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNames(self, lFlags: Int32, pNames: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def BeginEnumeration(self, lFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Next(self, lFlags: Int32, pstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR), pValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EndEnumeration(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetValue(self, wszName: win32more.Windows.Win32.Foundation.PWSTR, lFlags: Int32, pValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetValue(self, wszName: win32more.Windows.Win32.Foundation.PWSTR, lFlags: Int32, pValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def DeleteValue(self, wszName: win32more.Windows.Win32.Foundation.PWSTR, lFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def DeleteAll(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemDecoupledBasicEventProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Wmi.IWbemDecoupledRegistrar
    _iid_ = Guid('{86336d20-ca11-4786-9ef1-bc8a946b42fc}')
    @commethod(5)
    def GetSink(self, a_Flags: Int32, a_Context: win32more.Windows.Win32.System.Wmi.IWbemContext, a_Sink: POINTER(win32more.Windows.Win32.System.Wmi.IWbemObjectSink)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetService(self, a_Flags: Int32, a_Context: win32more.Windows.Win32.System.Wmi.IWbemContext, a_Service: POINTER(win32more.Windows.Win32.System.Wmi.IWbemServices)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemDecoupledRegistrar(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1005cbcf-e64f-4646-bcd3-3a089d8a84b4}')
    @commethod(3)
    def Register(self, a_Flags: Int32, a_Context: win32more.Windows.Win32.System.Wmi.IWbemContext, a_User: win32more.Windows.Win32.Foundation.PWSTR, a_Locale: win32more.Windows.Win32.Foundation.PWSTR, a_Scope: win32more.Windows.Win32.Foundation.PWSTR, a_Registration: win32more.Windows.Win32.Foundation.PWSTR, pIUnknown: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnRegister(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemEventConsumerProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e246107a-b06e-11d0-ad61-00c04fd8fdff}')
    @commethod(3)
    def FindConsumer(self, pLogicalConsumer: win32more.Windows.Win32.System.Wmi.IWbemClassObject, ppConsumer: POINTER(win32more.Windows.Win32.System.Wmi.IWbemUnboundObjectSink)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemEventProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e245105b-b06e-11d0-ad61-00c04fd8fdff}')
    @commethod(3)
    def ProvideEvents(self, pSink: win32more.Windows.Win32.System.Wmi.IWbemObjectSink, lFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemEventProviderQuerySink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{580acaf8-fa1c-11d0-ad72-00c04fd8fdff}')
    @commethod(3)
    def NewQuery(self, dwId: UInt32, wszQueryLanguage: POINTER(UInt16), wszQuery: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CancelQuery(self, dwId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemEventProviderSecurity(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{631f7d96-d993-11d2-b339-00105a1f4aaf}')
    @commethod(3)
    def AccessCheck(self, wszQueryLanguage: POINTER(UInt16), wszQuery: POINTER(UInt16), lSidLength: Int32, pSid: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemEventSink(ComPtr):
    extends: win32more.Windows.Win32.System.Wmi.IWbemObjectSink
    _iid_ = Guid('{3ae0080a-7e3a-4366-bf89-0feedc931659}')
    @commethod(5)
    def SetSinkSecurity(self, lSDLength: Int32, pSD: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def IsActive(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRestrictedSink(self, lNumQueries: Int32, awszQueries: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pCallback: win32more.Windows.Win32.System.Com.IUnknown, ppSink: POINTER(win32more.Windows.Win32.System.Wmi.IWbemEventSink)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetBatchingParameters(self, lFlags: Int32, dwMaxBufferSize: UInt32, dwMaxSendLatency: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemHiPerfEnum(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2705c288-79ae-11d2-b348-00105a1f8177}')
    @commethod(3)
    def AddObjects(self, lFlags: Int32, uNumObjects: UInt32, apIds: POINTER(Int32), apObj: POINTER(win32more.Windows.Win32.System.Wmi.IWbemObjectAccess)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveObjects(self, lFlags: Int32, uNumObjects: UInt32, apIds: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetObjects(self, lFlags: Int32, uNumObjects: UInt32, apObj: POINTER(win32more.Windows.Win32.System.Wmi.IWbemObjectAccess), puReturned: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveAll(self, lFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemHiPerfProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{49353c93-516b-11d1-aea6-00c04fb68820}')
    @commethod(3)
    def QueryInstances(self, pNamespace: win32more.Windows.Win32.System.Wmi.IWbemServices, wszClass: win32more.Windows.Win32.Foundation.PWSTR, lFlags: Int32, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, pSink: win32more.Windows.Win32.System.Wmi.IWbemObjectSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateRefresher(self, pNamespace: win32more.Windows.Win32.System.Wmi.IWbemServices, lFlags: Int32, ppRefresher: POINTER(win32more.Windows.Win32.System.Wmi.IWbemRefresher)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateRefreshableObject(self, pNamespace: win32more.Windows.Win32.System.Wmi.IWbemServices, pTemplate: win32more.Windows.Win32.System.Wmi.IWbemObjectAccess, pRefresher: win32more.Windows.Win32.System.Wmi.IWbemRefresher, lFlags: Int32, pContext: win32more.Windows.Win32.System.Wmi.IWbemContext, ppRefreshable: POINTER(win32more.Windows.Win32.System.Wmi.IWbemObjectAccess), plId: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def StopRefreshing(self, pRefresher: win32more.Windows.Win32.System.Wmi.IWbemRefresher, lId: Int32, lFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateRefreshableEnum(self, pNamespace: win32more.Windows.Win32.System.Wmi.IWbemServices, wszClass: win32more.Windows.Win32.Foundation.PWSTR, pRefresher: win32more.Windows.Win32.System.Wmi.IWbemRefresher, lFlags: Int32, pContext: win32more.Windows.Win32.System.Wmi.IWbemContext, pHiPerfEnum: win32more.Windows.Win32.System.Wmi.IWbemHiPerfEnum, plId: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetObjects(self, pNamespace: win32more.Windows.Win32.System.Wmi.IWbemServices, lNumObjects: Int32, apObj: POINTER(win32more.Windows.Win32.System.Wmi.IWbemObjectAccess), lFlags: Int32, pContext: win32more.Windows.Win32.System.Wmi.IWbemContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemLevel1Login(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f309ad18-d86a-11d0-a075-00c04fb68820}')
    @commethod(3)
    def EstablishPosition(self, wszLocaleList: win32more.Windows.Win32.Foundation.PWSTR, dwNumLocales: UInt32, reserved: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RequestChallenge(self, wszNetworkResource: win32more.Windows.Win32.Foundation.PWSTR, wszUser: win32more.Windows.Win32.Foundation.PWSTR, Nonce: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def WBEMLogin(self, wszPreferredLocale: win32more.Windows.Win32.Foundation.PWSTR, AccessToken: POINTER(Byte), lFlags: Int32, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, ppNamespace: POINTER(win32more.Windows.Win32.System.Wmi.IWbemServices)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def NTLMLogin(self, wszNetworkResource: win32more.Windows.Win32.Foundation.PWSTR, wszPreferredLocale: win32more.Windows.Win32.Foundation.PWSTR, lFlags: Int32, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, ppNamespace: POINTER(win32more.Windows.Win32.System.Wmi.IWbemServices)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemLocator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dc12a687-737f-11cf-884d-00aa004b2e24}')
    @commethod(3)
    def ConnectServer(self, strNetworkResource: win32more.Windows.Win32.Foundation.BSTR, strUser: win32more.Windows.Win32.Foundation.BSTR, strPassword: win32more.Windows.Win32.Foundation.BSTR, strLocale: win32more.Windows.Win32.Foundation.BSTR, lSecurityFlags: Int32, strAuthority: win32more.Windows.Win32.Foundation.BSTR, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, ppNamespace: POINTER(win32more.Windows.Win32.System.Wmi.IWbemServices)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemObjectAccess(ComPtr):
    extends: win32more.Windows.Win32.System.Wmi.IWbemClassObject
    _iid_ = Guid('{49353c9a-516b-11d1-aea6-00c04fb68820}')
    @commethod(27)
    def GetPropertyHandle(self, wszPropertyName: win32more.Windows.Win32.Foundation.PWSTR, pType: POINTER(Int32), plHandle: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def WritePropertyValue(self, lHandle: Int32, lNumBytes: Int32, aData: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def ReadPropertyValue(self, lHandle: Int32, lBufferSize: Int32, plNumBytes: POINTER(Int32), aData: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def ReadDWORD(self, lHandle: Int32, pdw: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def WriteDWORD(self, lHandle: Int32, dw: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def ReadQWORD(self, lHandle: Int32, pqw: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def WriteQWORD(self, lHandle: Int32, pw: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetPropertyInfoByHandle(self, lHandle: Int32, pstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR), pType: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def Lock(self, lFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def Unlock(self, lFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemObjectSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7c857801-7381-11cf-884d-00aa004b2e24}')
    @commethod(3)
    def Indicate(self, lObjectCount: Int32, apObjArray: POINTER(win32more.Windows.Win32.System.Wmi.IWbemClassObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetStatus(self, lFlags: Int32, hResult: win32more.Windows.Win32.Foundation.HRESULT, strParam: win32more.Windows.Win32.Foundation.BSTR, pObjParam: win32more.Windows.Win32.System.Wmi.IWbemClassObject) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemObjectSinkEx(ComPtr):
    extends: win32more.Windows.Win32.System.Wmi.IWbemObjectSink
    _iid_ = Guid('{e7d35cfa-348b-485e-b524-252725d697ca}')
    @commethod(5)
    def WriteMessage(self, uChannel: UInt32, strMessage: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def WriteError(self, pObjError: win32more.Windows.Win32.System.Wmi.IWbemClassObject, puReturned: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def PromptUser(self, strMessage: win32more.Windows.Win32.Foundation.BSTR, uPromptType: Byte, puReturned: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def WriteProgress(self, strActivity: win32more.Windows.Win32.Foundation.BSTR, strCurrentOperation: win32more.Windows.Win32.Foundation.BSTR, strStatusDescription: win32more.Windows.Win32.Foundation.BSTR, uPercentComplete: UInt32, uSecondsRemaining: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def WriteStreamParameter(self, strName: win32more.Windows.Win32.Foundation.BSTR, vtValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), ulType: UInt32, ulFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemObjectTextSrc(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bfbf883a-cad7-11d3-a11b-00105a1f515a}')
    @commethod(3)
    def GetText(self, lFlags: Int32, pObj: win32more.Windows.Win32.System.Wmi.IWbemClassObject, uObjTextFormat: UInt32, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, strText: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateFromText(self, lFlags: Int32, strText: win32more.Windows.Win32.Foundation.BSTR, uObjTextFormat: UInt32, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, pNewObj: POINTER(win32more.Windows.Win32.System.Wmi.IWbemClassObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemPath(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3bc15af2-736c-477e-9e51-238af8667dcc}')
    @commethod(3)
    def SetText(self, uMode: UInt32, pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetText(self, lFlags: Int32, puBuffLength: POINTER(UInt32), pszText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetInfo(self, uRequestedInfo: UInt32, puResponse: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetServer(self, Name: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetServer(self, puNameBufLength: POINTER(UInt32), pName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetNamespaceCount(self, puCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetNamespaceAt(self, uIndex: UInt32, pszName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetNamespaceAt(self, uIndex: UInt32, puNameBufLength: POINTER(UInt32), pName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RemoveNamespaceAt(self, uIndex: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RemoveAllNamespaces(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetScopeCount(self, puCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetScope(self, uIndex: UInt32, pszClass: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetScopeFromText(self, uIndex: UInt32, pszText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetScope(self, uIndex: UInt32, puClassNameBufSize: POINTER(UInt32), pszClass: win32more.Windows.Win32.Foundation.PWSTR, pKeyList: POINTER(win32more.Windows.Win32.System.Wmi.IWbemPathKeyList)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetScopeAsText(self, uIndex: UInt32, puTextBufSize: POINTER(UInt32), pszText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def RemoveScope(self, uIndex: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def RemoveAllScopes(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetClassName(self, Name: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetClassName(self, puBuffLength: POINTER(UInt32), pszName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetKeyList(self, pOut: POINTER(win32more.Windows.Win32.System.Wmi.IWbemPathKeyList)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def CreateClassPart(self, lFlags: Int32, Name: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def DeleteClassPart(self, lFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def IsRelative(self, wszMachine: win32more.Windows.Win32.Foundation.PWSTR, wszNamespace: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(26)
    def IsRelativeOrChild(self, wszMachine: win32more.Windows.Win32.Foundation.PWSTR, wszNamespace: win32more.Windows.Win32.Foundation.PWSTR, lFlags: Int32) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(27)
    def IsLocal(self, wszMachine: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(28)
    def IsSameClassName(self, wszClass: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
class IWbemPathKeyList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9ae62877-7544-4bb0-aa26-a13824659ed6}')
    @commethod(3)
    def GetCount(self, puKeyCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetKey(self, wszName: win32more.Windows.Win32.Foundation.PWSTR, uFlags: UInt32, uCimType: UInt32, pKeyVal: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetKey2(self, wszName: win32more.Windows.Win32.Foundation.PWSTR, uFlags: UInt32, uCimType: UInt32, pKeyVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetKey(self, uKeyIx: UInt32, uFlags: UInt32, puNameBufSize: POINTER(UInt32), pszKeyName: win32more.Windows.Win32.Foundation.PWSTR, puKeyValBufSize: POINTER(UInt32), pKeyVal: VoidPtr, puApparentCimType: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetKey2(self, uKeyIx: UInt32, uFlags: UInt32, puNameBufSize: POINTER(UInt32), pszKeyName: win32more.Windows.Win32.Foundation.PWSTR, pKeyValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), puApparentCimType: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveKey(self, wszName: win32more.Windows.Win32.Foundation.PWSTR, uFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RemoveAllKeys(self, uFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def MakeSingleton(self, bSet: Byte) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetInfo(self, uRequestedInfo: UInt32, puResponse: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetText(self, lFlags: Int32, puBuffLength: POINTER(UInt32), pszText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemPropertyProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ce61e841-65bc-11d0-b6bd-00aa003240c7}')
    @commethod(3)
    def GetProperty(self, lFlags: Int32, strLocale: win32more.Windows.Win32.Foundation.BSTR, strClassMapping: win32more.Windows.Win32.Foundation.BSTR, strInstMapping: win32more.Windows.Win32.Foundation.BSTR, strPropMapping: win32more.Windows.Win32.Foundation.BSTR, pvValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PutProperty(self, lFlags: Int32, strLocale: win32more.Windows.Win32.Foundation.BSTR, strClassMapping: win32more.Windows.Win32.Foundation.BSTR, strInstMapping: win32more.Windows.Win32.Foundation.BSTR, strPropMapping: win32more.Windows.Win32.Foundation.BSTR, pvValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemProviderIdentity(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{631f7d97-d993-11d2-b339-00105a1f4aaf}')
    @commethod(3)
    def SetRegistrationObject(self, lFlags: Int32, pProvReg: win32more.Windows.Win32.System.Wmi.IWbemClassObject) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemProviderInit(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1be41572-91dd-11d1-aeb2-00c04fb68820}')
    @commethod(3)
    def Initialize(self, wszUser: win32more.Windows.Win32.Foundation.PWSTR, lFlags: Int32, wszNamespace: win32more.Windows.Win32.Foundation.PWSTR, wszLocale: win32more.Windows.Win32.Foundation.PWSTR, pNamespace: win32more.Windows.Win32.System.Wmi.IWbemServices, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, pInitSink: win32more.Windows.Win32.System.Wmi.IWbemProviderInitSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemProviderInitSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1be41571-91dd-11d1-aeb2-00c04fb68820}')
    @commethod(3)
    def SetStatus(self, lStatus: Int32, lFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemQualifierSet(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dc12a680-737f-11cf-884d-00aa004b2e24}')
    @commethod(3)
    def Get(self, wszName: win32more.Windows.Win32.Foundation.PWSTR, lFlags: Int32, pVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), plFlavor: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Put(self, wszName: win32more.Windows.Win32.Foundation.PWSTR, pVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), lFlavor: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Delete(self, wszName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetNames(self, lFlags: Int32, pNames: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def BeginEnumeration(self, lFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Next(self, lFlags: Int32, pstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR), pVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), plFlavor: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EndEnumeration(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemQuery(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{81166f58-dd98-11d3-a120-00105a1f515a}')
    @commethod(3)
    def Empty(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetLanguageFeatures(self, uFlags: UInt32, uArraySize: UInt32, puFeatures: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def TestLanguageFeatures(self, uFlags: UInt32, uArraySize: POINTER(UInt32), puFeatures: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Parse(self, pszLang: win32more.Windows.Win32.Foundation.PWSTR, pszQuery: win32more.Windows.Win32.Foundation.PWSTR, uFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetAnalysis(self, uAnalysisType: UInt32, uFlags: UInt32, pAnalysis: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def FreeMemory(self, pMem: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetQueryInfo(self, uAnalysisType: UInt32, uInfoId: UInt32, uBufSize: UInt32, pDestBuf: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemRefresher(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{49353c99-516b-11d1-aea6-00c04fb68820}')
    @commethod(3)
    def Refresh(self, lFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemServices(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9556dc99-828c-11cf-a37e-00aa003240c7}')
    @commethod(3)
    def OpenNamespace(self, strNamespace: win32more.Windows.Win32.Foundation.BSTR, lFlags: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, ppWorkingNamespace: POINTER(win32more.Windows.Win32.System.Wmi.IWbemServices), ppResult: POINTER(win32more.Windows.Win32.System.Wmi.IWbemCallResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CancelAsyncCall(self, pSink: win32more.Windows.Win32.System.Wmi.IWbemObjectSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def QueryObjectSink(self, lFlags: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE, ppResponseHandler: POINTER(win32more.Windows.Win32.System.Wmi.IWbemObjectSink)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetObject(self, strObjectPath: win32more.Windows.Win32.Foundation.BSTR, lFlags: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, ppObject: POINTER(win32more.Windows.Win32.System.Wmi.IWbemClassObject), ppCallResult: POINTER(win32more.Windows.Win32.System.Wmi.IWbemCallResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetObjectAsync(self, strObjectPath: win32more.Windows.Win32.Foundation.BSTR, lFlags: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, pResponseHandler: win32more.Windows.Win32.System.Wmi.IWbemObjectSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def PutClass(self, pObject: win32more.Windows.Win32.System.Wmi.IWbemClassObject, lFlags: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, ppCallResult: POINTER(win32more.Windows.Win32.System.Wmi.IWbemCallResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def PutClassAsync(self, pObject: win32more.Windows.Win32.System.Wmi.IWbemClassObject, lFlags: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, pResponseHandler: win32more.Windows.Win32.System.Wmi.IWbemObjectSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def DeleteClass(self, strClass: win32more.Windows.Win32.Foundation.BSTR, lFlags: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, ppCallResult: POINTER(win32more.Windows.Win32.System.Wmi.IWbemCallResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def DeleteClassAsync(self, strClass: win32more.Windows.Win32.Foundation.BSTR, lFlags: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, pResponseHandler: win32more.Windows.Win32.System.Wmi.IWbemObjectSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def CreateClassEnum(self, strSuperclass: win32more.Windows.Win32.Foundation.BSTR, lFlags: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, ppEnum: POINTER(win32more.Windows.Win32.System.Wmi.IEnumWbemClassObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def CreateClassEnumAsync(self, strSuperclass: win32more.Windows.Win32.Foundation.BSTR, lFlags: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, pResponseHandler: win32more.Windows.Win32.System.Wmi.IWbemObjectSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def PutInstance(self, pInst: win32more.Windows.Win32.System.Wmi.IWbemClassObject, lFlags: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, ppCallResult: POINTER(win32more.Windows.Win32.System.Wmi.IWbemCallResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def PutInstanceAsync(self, pInst: win32more.Windows.Win32.System.Wmi.IWbemClassObject, lFlags: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, pResponseHandler: win32more.Windows.Win32.System.Wmi.IWbemObjectSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def DeleteInstance(self, strObjectPath: win32more.Windows.Win32.Foundation.BSTR, lFlags: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, ppCallResult: POINTER(win32more.Windows.Win32.System.Wmi.IWbemCallResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def DeleteInstanceAsync(self, strObjectPath: win32more.Windows.Win32.Foundation.BSTR, lFlags: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, pResponseHandler: win32more.Windows.Win32.System.Wmi.IWbemObjectSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def CreateInstanceEnum(self, strFilter: win32more.Windows.Win32.Foundation.BSTR, lFlags: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, ppEnum: POINTER(win32more.Windows.Win32.System.Wmi.IEnumWbemClassObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def CreateInstanceEnumAsync(self, strFilter: win32more.Windows.Win32.Foundation.BSTR, lFlags: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, pResponseHandler: win32more.Windows.Win32.System.Wmi.IWbemObjectSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def ExecQuery(self, strQueryLanguage: win32more.Windows.Win32.Foundation.BSTR, strQuery: win32more.Windows.Win32.Foundation.BSTR, lFlags: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, ppEnum: POINTER(win32more.Windows.Win32.System.Wmi.IEnumWbemClassObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def ExecQueryAsync(self, strQueryLanguage: win32more.Windows.Win32.Foundation.BSTR, strQuery: win32more.Windows.Win32.Foundation.BSTR, lFlags: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, pResponseHandler: win32more.Windows.Win32.System.Wmi.IWbemObjectSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def ExecNotificationQuery(self, strQueryLanguage: win32more.Windows.Win32.Foundation.BSTR, strQuery: win32more.Windows.Win32.Foundation.BSTR, lFlags: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, ppEnum: POINTER(win32more.Windows.Win32.System.Wmi.IEnumWbemClassObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def ExecNotificationQueryAsync(self, strQueryLanguage: win32more.Windows.Win32.Foundation.BSTR, strQuery: win32more.Windows.Win32.Foundation.BSTR, lFlags: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, pResponseHandler: win32more.Windows.Win32.System.Wmi.IWbemObjectSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def ExecMethod(self, strObjectPath: win32more.Windows.Win32.Foundation.BSTR, strMethodName: win32more.Windows.Win32.Foundation.BSTR, lFlags: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, pInParams: win32more.Windows.Win32.System.Wmi.IWbemClassObject, ppOutParams: POINTER(win32more.Windows.Win32.System.Wmi.IWbemClassObject), ppCallResult: POINTER(win32more.Windows.Win32.System.Wmi.IWbemCallResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def ExecMethodAsync(self, strObjectPath: win32more.Windows.Win32.Foundation.BSTR, strMethodName: win32more.Windows.Win32.Foundation.BSTR, lFlags: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext, pInParams: win32more.Windows.Win32.System.Wmi.IWbemClassObject, pResponseHandler: win32more.Windows.Win32.System.Wmi.IWbemObjectSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemShutdown(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b7b31df9-d515-11d3-a11c-00105a1f515a}')
    @commethod(3)
    def Shutdown(self, uReason: Int32, uMaxMilliseconds: UInt32, pCtx: win32more.Windows.Win32.System.Wmi.IWbemContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemStatusCodeText(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{eb87e1bc-3233-11d2-aec9-00c04fb68820}')
    @commethod(3)
    def GetErrorCodeText(self, hRes: win32more.Windows.Win32.Foundation.HRESULT, LocaleId: UInt32, lFlags: Int32, MessageText: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFacilityCodeText(self, hRes: win32more.Windows.Win32.Foundation.HRESULT, LocaleId: UInt32, lFlags: Int32, MessageText: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemTransport(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{553fe584-2156-11d0-b6ae-00aa003240c7}')
    @commethod(3)
    def Initialize(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemUnboundObjectSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e246107b-b06e-11d0-ad61-00c04fd8fdff}')
    @commethod(3)
    def IndicateToConsumer(self, pLogicalConsumer: win32more.Windows.Win32.System.Wmi.IWbemClassObject, lNumObjects: Int32, apObjects: POINTER(win32more.Windows.Win32.System.Wmi.IWbemClassObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWbemUnsecuredApartment(ComPtr):
    extends: win32more.Windows.Win32.System.Wmi.IUnsecuredApartment
    _iid_ = Guid('{31739d04-3471-4cf4-9a7c-57a44ae71956}')
    @commethod(4)
    def CreateSinkStub(self, pSink: win32more.Windows.Win32.System.Wmi.IWbemObjectSink, dwFlags: UInt32, wszReserved: win32more.Windows.Win32.Foundation.PWSTR, ppStub: POINTER(win32more.Windows.Win32.System.Wmi.IWbemObjectSink)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class MI_Application(Structure):
    reserved1: UInt64
    reserved2: IntPtr
    ft: POINTER(win32more.Windows.Win32.System.Wmi.MI_ApplicationFT)
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
    data: VoidPtr
    size: UInt32
class MI_ArrayField(Structure):
    value: win32more.Windows.Win32.System.Wmi.MI_Array
    exists: Byte
    flags: Byte
class MI_BooleanA(Structure):
    data: POINTER(Byte)
    size: UInt32
class MI_BooleanAField(Structure):
    value: win32more.Windows.Win32.System.Wmi.MI_BooleanA
    exists: Byte
    flags: Byte
class MI_BooleanField(Structure):
    value: Byte
    exists: Byte
    flags: Byte
MI_CallbackMode = Int32
MI_CALLBACKMODE_REPORT: win32more.Windows.Win32.System.Wmi.MI_CallbackMode = 0
MI_CALLBACKMODE_INQUIRE: win32more.Windows.Win32.System.Wmi.MI_CallbackMode = 1
MI_CALLBACKMODE_IGNORE: win32more.Windows.Win32.System.Wmi.MI_CallbackMode = 2
@winfunctype_pointer
def MI_CancelCallback(reason: win32more.Windows.Win32.System.Wmi.MI_CancellationReason, callbackData: VoidPtr) -> Void: ...
MI_CancellationReason = Int32
MI_REASON_NONE: win32more.Windows.Win32.System.Wmi.MI_CancellationReason = 0
MI_REASON_TIMEOUT: win32more.Windows.Win32.System.Wmi.MI_CancellationReason = 1
MI_REASON_SHUTDOWN: win32more.Windows.Win32.System.Wmi.MI_CancellationReason = 2
MI_REASON_SERVICESTOP: win32more.Windows.Win32.System.Wmi.MI_CancellationReason = 3
class MI_Char16A(Structure):
    data: POINTER(UInt16)
    size: UInt32
class MI_Char16AField(Structure):
    value: win32more.Windows.Win32.System.Wmi.MI_Char16A
    exists: Byte
    flags: Byte
class MI_Char16Field(Structure):
    value: UInt16
    exists: Byte
    flags: Byte
class MI_Class(Structure):
    ft: POINTER(win32more.Windows.Win32.System.Wmi.MI_ClassFT)
    classDecl: POINTER(win32more.Windows.Win32.System.Wmi.MI_ClassDecl)
    namespaceName: POINTER(UInt16)
    serverName: POINTER(UInt16)
    reserved: IntPtr * 4
class MI_ClassDecl(Structure):
    flags: UInt32
    code: UInt32
    name: POINTER(UInt16)
    qualifiers: POINTER(POINTER(win32more.Windows.Win32.System.Wmi.MI_Qualifier))
    numQualifiers: UInt32
    properties: POINTER(POINTER(win32more.Windows.Win32.System.Wmi.MI_PropertyDecl))
    numProperties: UInt32
    size: UInt32
    superClass: POINTER(UInt16)
    superClassDecl: POINTER(win32more.Windows.Win32.System.Wmi.MI_ClassDecl)
    methods: POINTER(POINTER(win32more.Windows.Win32.System.Wmi.MI_MethodDecl))
    numMethods: UInt32
    schema: POINTER(win32more.Windows.Win32.System.Wmi.MI_SchemaDecl)
    providerFT: POINTER(win32more.Windows.Win32.System.Wmi.MI_ProviderFT)
    owningClass: POINTER(win32more.Windows.Win32.System.Wmi.MI_Class)
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
    applicationFT: POINTER(win32more.Windows.Win32.System.Wmi.MI_ApplicationFT)
    sessionFT: POINTER(win32more.Windows.Win32.System.Wmi.MI_SessionFT)
    operationFT: POINTER(win32more.Windows.Win32.System.Wmi.MI_OperationFT)
    hostedProviderFT: POINTER(win32more.Windows.Win32.System.Wmi.MI_HostedProviderFT)
    serializerFT: POINTER(win32more.Windows.Win32.System.Wmi.MI_SerializerFT)
    deserializerFT: POINTER(win32more.Windows.Win32.System.Wmi.MI_DeserializerFT)
    subscribeDeliveryOptionsFT: POINTER(win32more.Windows.Win32.System.Wmi.MI_SubscriptionDeliveryOptionsFT)
    destinationOptionsFT: POINTER(win32more.Windows.Win32.System.Wmi.MI_DestinationOptionsFT)
    operationOptionsFT: POINTER(win32more.Windows.Win32.System.Wmi.MI_OperationOptionsFT)
    utilitiesFT: POINTER(win32more.Windows.Win32.System.Wmi.MI_UtilitiesFT)
class MI_ConstBooleanA(Structure):
    data: POINTER(Byte)
    size: UInt32
class MI_ConstBooleanAField(Structure):
    value: win32more.Windows.Win32.System.Wmi.MI_ConstBooleanA
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
    value: win32more.Windows.Win32.System.Wmi.MI_ConstChar16A
    exists: Byte
    flags: Byte
class MI_ConstChar16Field(Structure):
    value: UInt16
    exists: Byte
    flags: Byte
class MI_ConstDatetimeA(Structure):
    data: POINTER(win32more.Windows.Win32.System.Wmi.MI_Datetime)
    size: UInt32
class MI_ConstDatetimeAField(Structure):
    value: win32more.Windows.Win32.System.Wmi.MI_ConstDatetimeA
    exists: Byte
    flags: Byte
class MI_ConstDatetimeField(Structure):
    value: win32more.Windows.Win32.System.Wmi.MI_Datetime
    exists: Byte
    flags: Byte
class MI_ConstInstanceA(Structure):
    data: POINTER(POINTER(win32more.Windows.Win32.System.Wmi.MI_Instance))
    size: UInt32
class MI_ConstInstanceAField(Structure):
    value: win32more.Windows.Win32.System.Wmi.MI_ConstInstanceA
    exists: Byte
    flags: Byte
class MI_ConstInstanceField(Structure):
    value: POINTER(win32more.Windows.Win32.System.Wmi.MI_Instance)
    exists: Byte
    flags: Byte
class MI_ConstReal32A(Structure):
    data: POINTER(Single)
    size: UInt32
class MI_ConstReal32AField(Structure):
    value: win32more.Windows.Win32.System.Wmi.MI_ConstReal32A
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
    value: win32more.Windows.Win32.System.Wmi.MI_ConstReal64A
    exists: Byte
    flags: Byte
class MI_ConstReal64Field(Structure):
    value: Double
    exists: Byte
    flags: Byte
class MI_ConstReferenceA(Structure):
    data: POINTER(POINTER(win32more.Windows.Win32.System.Wmi.MI_Instance))
    size: UInt32
class MI_ConstReferenceAField(Structure):
    value: win32more.Windows.Win32.System.Wmi.MI_ConstReferenceA
    exists: Byte
    flags: Byte
class MI_ConstReferenceField(Structure):
    value: POINTER(win32more.Windows.Win32.System.Wmi.MI_Instance)
    exists: Byte
    flags: Byte
class MI_ConstSint16A(Structure):
    data: POINTER(Int16)
    size: UInt32
class MI_ConstSint16AField(Structure):
    value: win32more.Windows.Win32.System.Wmi.MI_ConstSint16A
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
    value: win32more.Windows.Win32.System.Wmi.MI_ConstSint32A
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
    value: win32more.Windows.Win32.System.Wmi.MI_ConstSint64A
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
    value: win32more.Windows.Win32.System.Wmi.MI_ConstSint8A
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
    value: win32more.Windows.Win32.System.Wmi.MI_ConstStringA
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
    value: win32more.Windows.Win32.System.Wmi.MI_ConstUint16A
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
    value: win32more.Windows.Win32.System.Wmi.MI_ConstUint32A
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
    value: win32more.Windows.Win32.System.Wmi.MI_ConstUint64A
    exists: Byte
    flags: Byte
class MI_ConstUint64Field(Structure):
    value: UInt64
    exists: Byte
    flags: Byte
class MI_ConstUint8A(Structure):
    data: POINTER(Byte)
    size: UInt32
class MI_ConstUint8AField(Structure):
    value: win32more.Windows.Win32.System.Wmi.MI_ConstUint8A
    exists: Byte
    flags: Byte
class MI_ConstUint8Field(Structure):
    value: Byte
    exists: Byte
    flags: Byte
class MI_Context(Structure):
    ft: POINTER(win32more.Windows.Win32.System.Wmi.MI_ContextFT)
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
        timestamp: win32more.Windows.Win32.System.Wmi.MI_Timestamp
        interval: win32more.Windows.Win32.System.Wmi.MI_Interval
class MI_DatetimeA(Structure):
    data: POINTER(win32more.Windows.Win32.System.Wmi.MI_Datetime)
    size: UInt32
class MI_DatetimeAField(Structure):
    value: win32more.Windows.Win32.System.Wmi.MI_DatetimeA
    exists: Byte
    flags: Byte
class MI_DatetimeField(Structure):
    value: win32more.Windows.Win32.System.Wmi.MI_Datetime
    exists: Byte
    flags: Byte
class MI_Deserializer(Structure):
    reserved1: UInt64
    reserved2: IntPtr
class MI_DeserializerFT(Structure):
    Close: IntPtr
    DeserializeClass: IntPtr
    Class_GetClassName: IntPtr
    Class_GetParentClassName: IntPtr
    DeserializeInstance: IntPtr
    Instance_GetClassName: IntPtr
@winfunctype_pointer
def MI_Deserializer_ClassObjectNeeded(context: VoidPtr, serverName: POINTER(UInt16), namespaceName: POINTER(UInt16), className: POINTER(UInt16), requestedClassObject: POINTER(POINTER(win32more.Windows.Win32.System.Wmi.MI_Class))) -> win32more.Windows.Win32.System.Wmi.MI_Result: ...
class MI_DestinationOptions(Structure):
    reserved1: UInt64
    reserved2: IntPtr
    ft: POINTER(win32more.Windows.Win32.System.Wmi.MI_DestinationOptionsFT)
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
MI_DestinationOptions_ImpersonationType = Int32
MI_DestinationOptions_ImpersonationType_Default: win32more.Windows.Win32.System.Wmi.MI_DestinationOptions_ImpersonationType = 0
MI_DestinationOptions_ImpersonationType_None: win32more.Windows.Win32.System.Wmi.MI_DestinationOptions_ImpersonationType = 1
MI_DestinationOptions_ImpersonationType_Identify: win32more.Windows.Win32.System.Wmi.MI_DestinationOptions_ImpersonationType = 2
MI_DestinationOptions_ImpersonationType_Impersonate: win32more.Windows.Win32.System.Wmi.MI_DestinationOptions_ImpersonationType = 3
MI_DestinationOptions_ImpersonationType_Delegate: win32more.Windows.Win32.System.Wmi.MI_DestinationOptions_ImpersonationType = 4
MI_ErrorCategory = Int32
MI_ERRORCATEGORY_NOT_SPECIFIED: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 0
MI_ERRORCATEGORY_OPEN_ERROR: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 1
MI_ERRORCATEGORY_CLOS_EERROR: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 2
MI_ERRORCATEGORY_DEVICE_ERROR: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 3
MI_ERRORCATEGORY_DEADLOCK_DETECTED: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 4
MI_ERRORCATEGORY_INVALID_ARGUMENT: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 5
MI_ERRORCATEGORY_INVALID_DATA: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 6
MI_ERRORCATEGORY_INVALID_OPERATION: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 7
MI_ERRORCATEGORY_INVALID_RESULT: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 8
MI_ERRORCATEGORY_INVALID_TYPE: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 9
MI_ERRORCATEGORY_METADATA_ERROR: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 10
MI_ERRORCATEGORY_NOT_IMPLEMENTED: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 11
MI_ERRORCATEGORY_NOT_INSTALLED: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 12
MI_ERRORCATEGORY_OBJECT_NOT_FOUND: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 13
MI_ERRORCATEGORY_OPERATION_STOPPED: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 14
MI_ERRORCATEGORY_OPERATION_TIMEOUT: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 15
MI_ERRORCATEGORY_SYNTAX_ERROR: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 16
MI_ERRORCATEGORY_PARSER_ERROR: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 17
MI_ERRORCATEGORY_ACCESS_DENIED: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 18
MI_ERRORCATEGORY_RESOURCE_BUSY: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 19
MI_ERRORCATEGORY_RESOURCE_EXISTS: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 20
MI_ERRORCATEGORY_RESOURCE_UNAVAILABLE: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 21
MI_ERRORCATEGORY_READ_ERROR: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 22
MI_ERRORCATEGORY_WRITE_ERROR: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 23
MI_ERRORCATEGORY_FROM_STDERR: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 24
MI_ERRORCATEGORY_SECURITY_ERROR: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 25
MI_ERRORCATEGORY_PROTOCOL_ERROR: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 26
MI_ERRORCATEGORY_CONNECTION_ERROR: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 27
MI_ERRORCATEGORY_AUTHENTICATION_ERROR: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 28
MI_ERRORCATEGORY_LIMITS_EXCEEDED: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 29
MI_ERRORCATEGORY_QUOTA_EXCEEDED: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 30
MI_ERRORCATEGORY_NOT_ENABLED: win32more.Windows.Win32.System.Wmi.MI_ErrorCategory = 31
class MI_FeatureDecl(Structure):
    flags: UInt32
    code: UInt32
    name: POINTER(UInt16)
    qualifiers: POINTER(POINTER(win32more.Windows.Win32.System.Wmi.MI_Qualifier))
    numQualifiers: UInt32
class MI_Filter(Structure):
    ft: POINTER(win32more.Windows.Win32.System.Wmi.MI_FilterFT)
    reserved: IntPtr * 3
class MI_FilterFT(Structure):
    Evaluate: IntPtr
    GetExpression: IntPtr
class MI_HostedProvider(Structure):
    reserved1: UInt64
    reserved2: IntPtr
    ft: POINTER(win32more.Windows.Win32.System.Wmi.MI_HostedProviderFT)
class MI_HostedProviderFT(Structure):
    Close: IntPtr
    GetApplication: IntPtr
class MI_Instance(Structure):
    ft: POINTER(win32more.Windows.Win32.System.Wmi.MI_InstanceFT)
    classDecl: POINTER(win32more.Windows.Win32.System.Wmi.MI_ClassDecl)
    serverName: POINTER(UInt16)
    nameSpace: POINTER(UInt16)
    reserved: IntPtr * 4
class MI_InstanceA(Structure):
    data: POINTER(POINTER(win32more.Windows.Win32.System.Wmi.MI_Instance))
    size: UInt32
class MI_InstanceAField(Structure):
    value: win32more.Windows.Win32.System.Wmi.MI_InstanceA
    exists: Byte
    flags: Byte
class MI_InstanceExFT(Structure):
    parent: win32more.Windows.Win32.System.Wmi.MI_InstanceFT
    Normalize: IntPtr
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
class MI_InstanceField(Structure):
    value: POINTER(win32more.Windows.Win32.System.Wmi.MI_Instance)
    exists: Byte
    flags: Byte
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
MI_LOCALE_TYPE_REQUESTED_UI: win32more.Windows.Win32.System.Wmi.MI_LocaleType = 0
MI_LOCALE_TYPE_REQUESTED_DATA: win32more.Windows.Win32.System.Wmi.MI_LocaleType = 1
MI_LOCALE_TYPE_CLOSEST_UI: win32more.Windows.Win32.System.Wmi.MI_LocaleType = 2
MI_LOCALE_TYPE_CLOSEST_DATA: win32more.Windows.Win32.System.Wmi.MI_LocaleType = 3
@cfunctype_pointer
def MI_MainFunction(server: POINTER(win32more.Windows.Win32.System.Wmi.MI_Server)) -> POINTER(win32more.Windows.Win32.System.Wmi.MI_Module): ...
class MI_MethodDecl(Structure):
    flags: UInt32
    code: UInt32
    name: POINTER(UInt16)
    qualifiers: POINTER(POINTER(win32more.Windows.Win32.System.Wmi.MI_Qualifier))
    numQualifiers: UInt32
    parameters: POINTER(POINTER(win32more.Windows.Win32.System.Wmi.MI_ParameterDecl))
    numParameters: UInt32
    size: UInt32
    returnType: UInt32
    origin: POINTER(UInt16)
    propagator: POINTER(UInt16)
    schema: POINTER(win32more.Windows.Win32.System.Wmi.MI_SchemaDecl)
    function: win32more.Windows.Win32.System.Wmi.MI_MethodDecl_Invoke
@winfunctype_pointer
def MI_MethodDecl_Invoke(self: VoidPtr, context: POINTER(win32more.Windows.Win32.System.Wmi.MI_Context), nameSpace: POINTER(UInt16), className: POINTER(UInt16), methodName: POINTER(UInt16), instanceName: POINTER(win32more.Windows.Win32.System.Wmi.MI_Instance), parameters: POINTER(win32more.Windows.Win32.System.Wmi.MI_Instance)) -> Void: ...
class MI_Module(Structure):
    version: UInt32
    generatorVersion: UInt32
    flags: UInt32
    charSize: UInt32
    schemaDecl: POINTER(win32more.Windows.Win32.System.Wmi.MI_SchemaDecl)
    Load: win32more.Windows.Win32.System.Wmi.MI_Module_Load
    Unload: win32more.Windows.Win32.System.Wmi.MI_Module_Unload
    dynamicProviderFT: POINTER(win32more.Windows.Win32.System.Wmi.MI_ProviderFT)
@winfunctype_pointer
def MI_Module_Load(self: POINTER(POINTER(win32more.Windows.Win32.System.Wmi.MI_Module_Self)), context: POINTER(win32more.Windows.Win32.System.Wmi.MI_Context)) -> Void: ...
MI_Module_Self = IntPtr
@winfunctype_pointer
def MI_Module_Unload(self: POINTER(win32more.Windows.Win32.System.Wmi.MI_Module_Self), context: POINTER(win32more.Windows.Win32.System.Wmi.MI_Context)) -> Void: ...
class MI_ObjectDecl(Structure):
    flags: UInt32
    code: UInt32
    name: POINTER(UInt16)
    qualifiers: POINTER(POINTER(win32more.Windows.Win32.System.Wmi.MI_Qualifier))
    numQualifiers: UInt32
    properties: POINTER(POINTER(win32more.Windows.Win32.System.Wmi.MI_PropertyDecl))
    numProperties: UInt32
    size: UInt32
class MI_Operation(Structure):
    reserved1: UInt64
    reserved2: IntPtr
    ft: POINTER(win32more.Windows.Win32.System.Wmi.MI_OperationFT)
@winfunctype_pointer
def MI_OperationCallback_Class(operation: POINTER(win32more.Windows.Win32.System.Wmi.MI_Operation), callbackContext: VoidPtr, classResult: POINTER(win32more.Windows.Win32.System.Wmi.MI_Class), moreResults: Byte, resultCode: win32more.Windows.Win32.System.Wmi.MI_Result, errorString: POINTER(UInt16), errorDetails: POINTER(win32more.Windows.Win32.System.Wmi.MI_Instance), resultAcknowledgement: IntPtr) -> Void: ...
@winfunctype_pointer
def MI_OperationCallback_Indication(operation: POINTER(win32more.Windows.Win32.System.Wmi.MI_Operation), callbackContext: VoidPtr, instance: POINTER(win32more.Windows.Win32.System.Wmi.MI_Instance), bookmark: POINTER(UInt16), machineID: POINTER(UInt16), moreResults: Byte, resultCode: win32more.Windows.Win32.System.Wmi.MI_Result, errorString: POINTER(UInt16), errorDetails: POINTER(win32more.Windows.Win32.System.Wmi.MI_Instance), resultAcknowledgement: IntPtr) -> Void: ...
@winfunctype_pointer
def MI_OperationCallback_Instance(operation: POINTER(win32more.Windows.Win32.System.Wmi.MI_Operation), callbackContext: VoidPtr, instance: POINTER(win32more.Windows.Win32.System.Wmi.MI_Instance), moreResults: Byte, resultCode: win32more.Windows.Win32.System.Wmi.MI_Result, errorString: POINTER(UInt16), errorDetails: POINTER(win32more.Windows.Win32.System.Wmi.MI_Instance), resultAcknowledgement: IntPtr) -> Void: ...
@winfunctype_pointer
def MI_OperationCallback_PromptUser(operation: POINTER(win32more.Windows.Win32.System.Wmi.MI_Operation), callbackContext: VoidPtr, message: POINTER(UInt16), promptType: win32more.Windows.Win32.System.Wmi.MI_PromptType, promptUserResult: IntPtr) -> Void: ...
MI_OperationCallback_ResponseType = Int32
MI_OperationCallback_ResponseType_No: win32more.Windows.Win32.System.Wmi.MI_OperationCallback_ResponseType = 0
MI_OperationCallback_ResponseType_Yes: win32more.Windows.Win32.System.Wmi.MI_OperationCallback_ResponseType = 1
MI_OperationCallback_ResponseType_NoToAll: win32more.Windows.Win32.System.Wmi.MI_OperationCallback_ResponseType = 2
MI_OperationCallback_ResponseType_YesToAll: win32more.Windows.Win32.System.Wmi.MI_OperationCallback_ResponseType = 3
@winfunctype_pointer
def MI_OperationCallback_StreamedParameter(operation: POINTER(win32more.Windows.Win32.System.Wmi.MI_Operation), callbackContext: VoidPtr, parameterName: POINTER(UInt16), resultType: win32more.Windows.Win32.System.Wmi.MI_Type, result: POINTER(win32more.Windows.Win32.System.Wmi.MI_Value), resultAcknowledgement: IntPtr) -> Void: ...
@winfunctype_pointer
def MI_OperationCallback_WriteError(operation: POINTER(win32more.Windows.Win32.System.Wmi.MI_Operation), callbackContext: VoidPtr, instance: POINTER(win32more.Windows.Win32.System.Wmi.MI_Instance), writeErrorResult: IntPtr) -> Void: ...
@winfunctype_pointer
def MI_OperationCallback_WriteMessage(operation: POINTER(win32more.Windows.Win32.System.Wmi.MI_Operation), callbackContext: VoidPtr, channel: UInt32, message: POINTER(UInt16)) -> Void: ...
@winfunctype_pointer
def MI_OperationCallback_WriteProgress(operation: POINTER(win32more.Windows.Win32.System.Wmi.MI_Operation), callbackContext: VoidPtr, activity: POINTER(UInt16), currentOperation: POINTER(UInt16), statusDescription: POINTER(UInt16), percentageComplete: UInt32, secondsRemaining: UInt32) -> Void: ...
class MI_OperationCallbacks(Structure):
    callbackContext: VoidPtr
    promptUser: win32more.Windows.Win32.System.Wmi.MI_OperationCallback_PromptUser
    writeError: win32more.Windows.Win32.System.Wmi.MI_OperationCallback_WriteError
    writeMessage: win32more.Windows.Win32.System.Wmi.MI_OperationCallback_WriteMessage
    writeProgress: win32more.Windows.Win32.System.Wmi.MI_OperationCallback_WriteProgress
    instanceResult: win32more.Windows.Win32.System.Wmi.MI_OperationCallback_Instance
    indicationResult: win32more.Windows.Win32.System.Wmi.MI_OperationCallback_Indication
    classResult: win32more.Windows.Win32.System.Wmi.MI_OperationCallback_Class
    streamedParameterResult: win32more.Windows.Win32.System.Wmi.MI_OperationCallback_StreamedParameter
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
    ft: POINTER(win32more.Windows.Win32.System.Wmi.MI_OperationOptionsFT)
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
    qualifiers: POINTER(POINTER(win32more.Windows.Win32.System.Wmi.MI_Qualifier))
    numQualifiers: UInt32
    type: UInt32
    className: POINTER(UInt16)
    subscript: UInt32
    offset: UInt32
class MI_ParameterSet(Structure):
    reserved1: UInt64
    reserved2: IntPtr
    ft: POINTER(win32more.Windows.Win32.System.Wmi.MI_ParameterSetFT)
class MI_ParameterSetFT(Structure):
    GetMethodReturnType: IntPtr
    GetParameterCount: IntPtr
    GetParameterAt: IntPtr
    GetParameter: IntPtr
MI_PromptType = Int32
MI_PROMPTTYPE_NORMAL: win32more.Windows.Win32.System.Wmi.MI_PromptType = 0
MI_PROMPTTYPE_CRITICAL: win32more.Windows.Win32.System.Wmi.MI_PromptType = 1
class MI_PropertyDecl(Structure):
    flags: UInt32
    code: UInt32
    name: POINTER(UInt16)
    qualifiers: POINTER(POINTER(win32more.Windows.Win32.System.Wmi.MI_Qualifier))
    numQualifiers: UInt32
    type: UInt32
    className: POINTER(UInt16)
    subscript: UInt32
    offset: UInt32
    origin: POINTER(UInt16)
    propagator: POINTER(UInt16)
    value: VoidPtr
class MI_PropertySet(Structure):
    ft: POINTER(win32more.Windows.Win32.System.Wmi.MI_PropertySetFT)
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
MI_PROVIDER_ARCHITECTURE_32BIT: win32more.Windows.Win32.System.Wmi.MI_ProviderArchitecture = 0
MI_PROVIDER_ARCHITECTURE_64BIT: win32more.Windows.Win32.System.Wmi.MI_ProviderArchitecture = 1
class MI_ProviderFT(Structure):
    Load: win32more.Windows.Win32.System.Wmi.MI_ProviderFT_Load
    Unload: win32more.Windows.Win32.System.Wmi.MI_ProviderFT_Unload
    GetInstance: win32more.Windows.Win32.System.Wmi.MI_ProviderFT_GetInstance
    EnumerateInstances: win32more.Windows.Win32.System.Wmi.MI_ProviderFT_EnumerateInstances
    CreateInstance: win32more.Windows.Win32.System.Wmi.MI_ProviderFT_CreateInstance
    ModifyInstance: win32more.Windows.Win32.System.Wmi.MI_ProviderFT_ModifyInstance
    DeleteInstance: win32more.Windows.Win32.System.Wmi.MI_ProviderFT_DeleteInstance
    AssociatorInstances: win32more.Windows.Win32.System.Wmi.MI_ProviderFT_AssociatorInstances
    ReferenceInstances: win32more.Windows.Win32.System.Wmi.MI_ProviderFT_ReferenceInstances
    EnableIndications: win32more.Windows.Win32.System.Wmi.MI_ProviderFT_EnableIndications
    DisableIndications: win32more.Windows.Win32.System.Wmi.MI_ProviderFT_DisableIndications
    Subscribe: win32more.Windows.Win32.System.Wmi.MI_ProviderFT_Subscribe
    Unsubscribe: win32more.Windows.Win32.System.Wmi.MI_ProviderFT_Unsubscribe
    Invoke: win32more.Windows.Win32.System.Wmi.MI_ProviderFT_Invoke
@winfunctype_pointer
def MI_ProviderFT_AssociatorInstances(self: VoidPtr, context: POINTER(win32more.Windows.Win32.System.Wmi.MI_Context), nameSpace: POINTER(UInt16), className: POINTER(UInt16), instanceName: POINTER(win32more.Windows.Win32.System.Wmi.MI_Instance), resultClass: POINTER(UInt16), role: POINTER(UInt16), resultRole: POINTER(UInt16), propertySet: POINTER(win32more.Windows.Win32.System.Wmi.MI_PropertySet), keysOnly: Byte, filter: POINTER(win32more.Windows.Win32.System.Wmi.MI_Filter)) -> Void: ...
@winfunctype_pointer
def MI_ProviderFT_CreateInstance(self: VoidPtr, context: POINTER(win32more.Windows.Win32.System.Wmi.MI_Context), nameSpace: POINTER(UInt16), className: POINTER(UInt16), newInstance: POINTER(win32more.Windows.Win32.System.Wmi.MI_Instance)) -> Void: ...
@winfunctype_pointer
def MI_ProviderFT_DeleteInstance(self: VoidPtr, context: POINTER(win32more.Windows.Win32.System.Wmi.MI_Context), nameSpace: POINTER(UInt16), className: POINTER(UInt16), instanceName: POINTER(win32more.Windows.Win32.System.Wmi.MI_Instance)) -> Void: ...
@winfunctype_pointer
def MI_ProviderFT_DisableIndications(self: VoidPtr, indicationsContext: POINTER(win32more.Windows.Win32.System.Wmi.MI_Context), nameSpace: POINTER(UInt16), className: POINTER(UInt16)) -> Void: ...
@winfunctype_pointer
def MI_ProviderFT_EnableIndications(self: VoidPtr, indicationsContext: POINTER(win32more.Windows.Win32.System.Wmi.MI_Context), nameSpace: POINTER(UInt16), className: POINTER(UInt16)) -> Void: ...
@winfunctype_pointer
def MI_ProviderFT_EnumerateInstances(self: VoidPtr, context: POINTER(win32more.Windows.Win32.System.Wmi.MI_Context), nameSpace: POINTER(UInt16), className: POINTER(UInt16), propertySet: POINTER(win32more.Windows.Win32.System.Wmi.MI_PropertySet), keysOnly: Byte, filter: POINTER(win32more.Windows.Win32.System.Wmi.MI_Filter)) -> Void: ...
@winfunctype_pointer
def MI_ProviderFT_GetInstance(self: VoidPtr, context: POINTER(win32more.Windows.Win32.System.Wmi.MI_Context), nameSpace: POINTER(UInt16), className: POINTER(UInt16), instanceName: POINTER(win32more.Windows.Win32.System.Wmi.MI_Instance), propertySet: POINTER(win32more.Windows.Win32.System.Wmi.MI_PropertySet)) -> Void: ...
@winfunctype_pointer
def MI_ProviderFT_Invoke(self: VoidPtr, context: POINTER(win32more.Windows.Win32.System.Wmi.MI_Context), nameSpace: POINTER(UInt16), className: POINTER(UInt16), methodName: POINTER(UInt16), instanceName: POINTER(win32more.Windows.Win32.System.Wmi.MI_Instance), inputParameters: POINTER(win32more.Windows.Win32.System.Wmi.MI_Instance)) -> Void: ...
@winfunctype_pointer
def MI_ProviderFT_Load(self: POINTER(VoidPtr), selfModule: POINTER(win32more.Windows.Win32.System.Wmi.MI_Module_Self), context: POINTER(win32more.Windows.Win32.System.Wmi.MI_Context)) -> Void: ...
@winfunctype_pointer
def MI_ProviderFT_ModifyInstance(self: VoidPtr, context: POINTER(win32more.Windows.Win32.System.Wmi.MI_Context), nameSpace: POINTER(UInt16), className: POINTER(UInt16), modifiedInstance: POINTER(win32more.Windows.Win32.System.Wmi.MI_Instance), propertySet: POINTER(win32more.Windows.Win32.System.Wmi.MI_PropertySet)) -> Void: ...
@winfunctype_pointer
def MI_ProviderFT_ReferenceInstances(self: VoidPtr, context: POINTER(win32more.Windows.Win32.System.Wmi.MI_Context), nameSpace: POINTER(UInt16), className: POINTER(UInt16), instanceName: POINTER(win32more.Windows.Win32.System.Wmi.MI_Instance), role: POINTER(UInt16), propertySet: POINTER(win32more.Windows.Win32.System.Wmi.MI_PropertySet), keysOnly: Byte, filter: POINTER(win32more.Windows.Win32.System.Wmi.MI_Filter)) -> Void: ...
@winfunctype_pointer
def MI_ProviderFT_Subscribe(self: VoidPtr, context: POINTER(win32more.Windows.Win32.System.Wmi.MI_Context), nameSpace: POINTER(UInt16), className: POINTER(UInt16), filter: POINTER(win32more.Windows.Win32.System.Wmi.MI_Filter), bookmark: POINTER(UInt16), subscriptionID: UInt64, subscriptionSelf: POINTER(VoidPtr)) -> Void: ...
@winfunctype_pointer
def MI_ProviderFT_Unload(self: VoidPtr, context: POINTER(win32more.Windows.Win32.System.Wmi.MI_Context)) -> Void: ...
@winfunctype_pointer
def MI_ProviderFT_Unsubscribe(self: VoidPtr, context: POINTER(win32more.Windows.Win32.System.Wmi.MI_Context), nameSpace: POINTER(UInt16), className: POINTER(UInt16), subscriptionID: UInt64, subscriptionSelf: VoidPtr) -> Void: ...
class MI_Qualifier(Structure):
    name: POINTER(UInt16)
    type: UInt32
    flavor: UInt32
    value: VoidPtr
class MI_QualifierDecl(Structure):
    name: POINTER(UInt16)
    type: UInt32
    scope: UInt32
    flavor: UInt32
    subscript: UInt32
    value: VoidPtr
class MI_QualifierSet(Structure):
    reserved1: UInt64
    reserved2: IntPtr
    ft: POINTER(win32more.Windows.Win32.System.Wmi.MI_QualifierSetFT)
class MI_QualifierSetFT(Structure):
    GetQualifierCount: IntPtr
    GetQualifierAt: IntPtr
    GetQualifier: IntPtr
class MI_Real32A(Structure):
    data: POINTER(Single)
    size: UInt32
class MI_Real32AField(Structure):
    value: win32more.Windows.Win32.System.Wmi.MI_Real32A
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
    value: win32more.Windows.Win32.System.Wmi.MI_Real64A
    exists: Byte
    flags: Byte
class MI_Real64Field(Structure):
    value: Double
    exists: Byte
    flags: Byte
class MI_ReferenceA(Structure):
    data: POINTER(POINTER(win32more.Windows.Win32.System.Wmi.MI_Instance))
    size: UInt32
class MI_ReferenceAField(Structure):
    value: win32more.Windows.Win32.System.Wmi.MI_ReferenceA
    exists: Byte
    flags: Byte
class MI_ReferenceField(Structure):
    value: POINTER(win32more.Windows.Win32.System.Wmi.MI_Instance)
    exists: Byte
    flags: Byte
MI_Result = Int32
MI_RESULT_OK: win32more.Windows.Win32.System.Wmi.MI_Result = 0
MI_RESULT_FAILED: win32more.Windows.Win32.System.Wmi.MI_Result = 1
MI_RESULT_ACCESS_DENIED: win32more.Windows.Win32.System.Wmi.MI_Result = 2
MI_RESULT_INVALID_NAMESPACE: win32more.Windows.Win32.System.Wmi.MI_Result = 3
MI_RESULT_INVALID_PARAMETER: win32more.Windows.Win32.System.Wmi.MI_Result = 4
MI_RESULT_INVALID_CLASS: win32more.Windows.Win32.System.Wmi.MI_Result = 5
MI_RESULT_NOT_FOUND: win32more.Windows.Win32.System.Wmi.MI_Result = 6
MI_RESULT_NOT_SUPPORTED: win32more.Windows.Win32.System.Wmi.MI_Result = 7
MI_RESULT_CLASS_HAS_CHILDREN: win32more.Windows.Win32.System.Wmi.MI_Result = 8
MI_RESULT_CLASS_HAS_INSTANCES: win32more.Windows.Win32.System.Wmi.MI_Result = 9
MI_RESULT_INVALID_SUPERCLASS: win32more.Windows.Win32.System.Wmi.MI_Result = 10
MI_RESULT_ALREADY_EXISTS: win32more.Windows.Win32.System.Wmi.MI_Result = 11
MI_RESULT_NO_SUCH_PROPERTY: win32more.Windows.Win32.System.Wmi.MI_Result = 12
MI_RESULT_TYPE_MISMATCH: win32more.Windows.Win32.System.Wmi.MI_Result = 13
MI_RESULT_QUERY_LANGUAGE_NOT_SUPPORTED: win32more.Windows.Win32.System.Wmi.MI_Result = 14
MI_RESULT_INVALID_QUERY: win32more.Windows.Win32.System.Wmi.MI_Result = 15
MI_RESULT_METHOD_NOT_AVAILABLE: win32more.Windows.Win32.System.Wmi.MI_Result = 16
MI_RESULT_METHOD_NOT_FOUND: win32more.Windows.Win32.System.Wmi.MI_Result = 17
MI_RESULT_NAMESPACE_NOT_EMPTY: win32more.Windows.Win32.System.Wmi.MI_Result = 20
MI_RESULT_INVALID_ENUMERATION_CONTEXT: win32more.Windows.Win32.System.Wmi.MI_Result = 21
MI_RESULT_INVALID_OPERATION_TIMEOUT: win32more.Windows.Win32.System.Wmi.MI_Result = 22
MI_RESULT_PULL_HAS_BEEN_ABANDONED: win32more.Windows.Win32.System.Wmi.MI_Result = 23
MI_RESULT_PULL_CANNOT_BE_ABANDONED: win32more.Windows.Win32.System.Wmi.MI_Result = 24
MI_RESULT_FILTERED_ENUMERATION_NOT_SUPPORTED: win32more.Windows.Win32.System.Wmi.MI_Result = 25
MI_RESULT_CONTINUATION_ON_ERROR_NOT_SUPPORTED: win32more.Windows.Win32.System.Wmi.MI_Result = 26
MI_RESULT_SERVER_LIMITS_EXCEEDED: win32more.Windows.Win32.System.Wmi.MI_Result = 27
MI_RESULT_SERVER_IS_SHUTTING_DOWN: win32more.Windows.Win32.System.Wmi.MI_Result = 28
class MI_SchemaDecl(Structure):
    qualifierDecls: POINTER(POINTER(win32more.Windows.Win32.System.Wmi.MI_QualifierDecl))
    numQualifierDecls: UInt32
    classDecls: POINTER(POINTER(win32more.Windows.Win32.System.Wmi.MI_ClassDecl))
    numClassDecls: UInt32
class MI_Serializer(Structure):
    reserved1: UInt64
    reserved2: IntPtr
class MI_SerializerFT(Structure):
    Close: IntPtr
    SerializeClass: IntPtr
    SerializeInstance: IntPtr
class MI_Server(Structure):
    serverFT: POINTER(win32more.Windows.Win32.System.Wmi.MI_ServerFT)
    contextFT: POINTER(win32more.Windows.Win32.System.Wmi.MI_ContextFT)
    instanceFT: POINTER(win32more.Windows.Win32.System.Wmi.MI_InstanceFT)
    propertySetFT: POINTER(win32more.Windows.Win32.System.Wmi.MI_PropertySetFT)
    filterFT: POINTER(win32more.Windows.Win32.System.Wmi.MI_FilterFT)
class MI_ServerFT(Structure):
    GetVersion: IntPtr
    GetSystemName: IntPtr
class MI_Session(Structure):
    reserved1: UInt64
    reserved2: IntPtr
    ft: POINTER(win32more.Windows.Win32.System.Wmi.MI_SessionFT)
class MI_SessionCallbacks(Structure):
    callbackContext: VoidPtr
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
    value: win32more.Windows.Win32.System.Wmi.MI_Sint16A
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
    value: win32more.Windows.Win32.System.Wmi.MI_Sint32A
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
    value: win32more.Windows.Win32.System.Wmi.MI_Sint64A
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
    value: win32more.Windows.Win32.System.Wmi.MI_Sint8A
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
    value: win32more.Windows.Win32.System.Wmi.MI_StringA
    exists: Byte
    flags: Byte
class MI_StringField(Structure):
    value: POINTER(UInt16)
    exists: Byte
    flags: Byte
class MI_SubscriptionDeliveryOptions(Structure):
    reserved1: UInt64
    reserved2: IntPtr
    ft: POINTER(win32more.Windows.Win32.System.Wmi.MI_SubscriptionDeliveryOptionsFT)
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
MI_SubscriptionDeliveryType_Pull: win32more.Windows.Win32.System.Wmi.MI_SubscriptionDeliveryType = 1
MI_SubscriptionDeliveryType_Push: win32more.Windows.Win32.System.Wmi.MI_SubscriptionDeliveryType = 2
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
MI_BOOLEAN: win32more.Windows.Win32.System.Wmi.MI_Type = 0
MI_UINT8: win32more.Windows.Win32.System.Wmi.MI_Type = 1
MI_SINT8: win32more.Windows.Win32.System.Wmi.MI_Type = 2
MI_UINT16: win32more.Windows.Win32.System.Wmi.MI_Type = 3
MI_SINT16: win32more.Windows.Win32.System.Wmi.MI_Type = 4
MI_UINT32: win32more.Windows.Win32.System.Wmi.MI_Type = 5
MI_SINT32: win32more.Windows.Win32.System.Wmi.MI_Type = 6
MI_UINT64: win32more.Windows.Win32.System.Wmi.MI_Type = 7
MI_SINT64: win32more.Windows.Win32.System.Wmi.MI_Type = 8
MI_REAL32: win32more.Windows.Win32.System.Wmi.MI_Type = 9
MI_REAL64: win32more.Windows.Win32.System.Wmi.MI_Type = 10
MI_CHAR16: win32more.Windows.Win32.System.Wmi.MI_Type = 11
MI_DATETIME: win32more.Windows.Win32.System.Wmi.MI_Type = 12
MI_STRING: win32more.Windows.Win32.System.Wmi.MI_Type = 13
MI_REFERENCE: win32more.Windows.Win32.System.Wmi.MI_Type = 14
MI_INSTANCE: win32more.Windows.Win32.System.Wmi.MI_Type = 15
MI_BOOLEANA: win32more.Windows.Win32.System.Wmi.MI_Type = 16
MI_UINT8A: win32more.Windows.Win32.System.Wmi.MI_Type = 17
MI_SINT8A: win32more.Windows.Win32.System.Wmi.MI_Type = 18
MI_UINT16A: win32more.Windows.Win32.System.Wmi.MI_Type = 19
MI_SINT16A: win32more.Windows.Win32.System.Wmi.MI_Type = 20
MI_UINT32A: win32more.Windows.Win32.System.Wmi.MI_Type = 21
MI_SINT32A: win32more.Windows.Win32.System.Wmi.MI_Type = 22
MI_UINT64A: win32more.Windows.Win32.System.Wmi.MI_Type = 23
MI_SINT64A: win32more.Windows.Win32.System.Wmi.MI_Type = 24
MI_REAL32A: win32more.Windows.Win32.System.Wmi.MI_Type = 25
MI_REAL64A: win32more.Windows.Win32.System.Wmi.MI_Type = 26
MI_CHAR16A: win32more.Windows.Win32.System.Wmi.MI_Type = 27
MI_DATETIMEA: win32more.Windows.Win32.System.Wmi.MI_Type = 28
MI_STRINGA: win32more.Windows.Win32.System.Wmi.MI_Type = 29
MI_REFERENCEA: win32more.Windows.Win32.System.Wmi.MI_Type = 30
MI_INSTANCEA: win32more.Windows.Win32.System.Wmi.MI_Type = 31
MI_ARRAY: win32more.Windows.Win32.System.Wmi.MI_Type = 16
class MI_Uint16A(Structure):
    data: POINTER(UInt16)
    size: UInt32
class MI_Uint16AField(Structure):
    value: win32more.Windows.Win32.System.Wmi.MI_Uint16A
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
    value: win32more.Windows.Win32.System.Wmi.MI_Uint32A
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
    value: win32more.Windows.Win32.System.Wmi.MI_Uint64A
    exists: Byte
    flags: Byte
class MI_Uint64Field(Structure):
    value: UInt64
    exists: Byte
    flags: Byte
class MI_Uint8A(Structure):
    data: POINTER(Byte)
    size: UInt32
class MI_Uint8AField(Structure):
    value: win32more.Windows.Win32.System.Wmi.MI_Uint8A
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
        usernamePassword: win32more.Windows.Win32.System.Wmi.MI_UsernamePasswordCreds
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
    datetime: win32more.Windows.Win32.System.Wmi.MI_Datetime
    string: POINTER(UInt16)
    instance: POINTER(win32more.Windows.Win32.System.Wmi.MI_Instance)
    reference: POINTER(win32more.Windows.Win32.System.Wmi.MI_Instance)
    booleana: win32more.Windows.Win32.System.Wmi.MI_BooleanA
    uint8a: win32more.Windows.Win32.System.Wmi.MI_Uint8A
    sint8a: win32more.Windows.Win32.System.Wmi.MI_Sint8A
    uint16a: win32more.Windows.Win32.System.Wmi.MI_Uint16A
    sint16a: win32more.Windows.Win32.System.Wmi.MI_Sint16A
    uint32a: win32more.Windows.Win32.System.Wmi.MI_Uint32A
    sint32a: win32more.Windows.Win32.System.Wmi.MI_Sint32A
    uint64a: win32more.Windows.Win32.System.Wmi.MI_Uint64A
    sint64a: win32more.Windows.Win32.System.Wmi.MI_Sint64A
    real32a: win32more.Windows.Win32.System.Wmi.MI_Real32A
    real64a: win32more.Windows.Win32.System.Wmi.MI_Real64A
    char16a: win32more.Windows.Win32.System.Wmi.MI_Char16A
    datetimea: win32more.Windows.Win32.System.Wmi.MI_DatetimeA
    stringa: win32more.Windows.Win32.System.Wmi.MI_StringA
    referencea: win32more.Windows.Win32.System.Wmi.MI_ReferenceA
    instancea: win32more.Windows.Win32.System.Wmi.MI_InstanceA
    array: win32more.Windows.Win32.System.Wmi.MI_Array
MofCompiler = Guid('{6daf9757-2e37-11d2-aec9-00c04fb68820}')
class SWbemAnalysisMatrix(Structure):
    m_uVersion: UInt32
    m_uMatrixType: UInt32
    m_pszProperty: win32more.Windows.Win32.Foundation.PWSTR
    m_uPropertyType: UInt32
    m_uEntries: UInt32
    m_pValues: POINTER(VoidPtr)
    m_pbTruthTable: POINTER(win32more.Windows.Win32.Foundation.BOOL)
class SWbemAnalysisMatrixList(Structure):
    m_uVersion: UInt32
    m_uMatrixType: UInt32
    m_uNumMatrices: UInt32
    m_pMatrices: POINTER(win32more.Windows.Win32.System.Wmi.SWbemAnalysisMatrix)
class SWbemAssocQueryInf(Structure):
    m_uVersion: UInt32
    m_uAnalysisType: UInt32
    m_uFeatureMask: UInt32
    m_pPath: win32more.Windows.Win32.System.Wmi.IWbemPath
    m_pszPath: win32more.Windows.Win32.Foundation.PWSTR
    m_pszQueryText: win32more.Windows.Win32.Foundation.PWSTR
    m_pszResultClass: win32more.Windows.Win32.Foundation.PWSTR
    m_pszAssocClass: win32more.Windows.Win32.Foundation.PWSTR
    m_pszRole: win32more.Windows.Win32.Foundation.PWSTR
    m_pszResultRole: win32more.Windows.Win32.Foundation.PWSTR
    m_pszRequiredQualifier: win32more.Windows.Win32.Foundation.PWSTR
    m_pszRequiredAssocQualifier: win32more.Windows.Win32.Foundation.PWSTR
SWbemDateTime = Guid('{47dfbe54-cf76-11d3-b38f-00105a1f473a}')
SWbemEventSource = Guid('{04b83d58-21ae-11d2-8b33-00600806d9b6}')
SWbemLastError = Guid('{c2feeeac-cfcd-11d1-8b05-00600806d9b6}')
SWbemLocator = Guid('{76a64158-cb41-11d1-8b02-00600806d9b6}')
SWbemMethod = Guid('{04b83d5b-21ae-11d2-8b33-00600806d9b6}')
SWbemMethodSet = Guid('{04b83d5a-21ae-11d2-8b33-00600806d9b6}')
SWbemNamedValue = Guid('{04b83d60-21ae-11d2-8b33-00600806d9b6}')
SWbemNamedValueSet = Guid('{9aed384e-ce8b-11d1-8b05-00600806d9b6}')
SWbemObject = Guid('{04b83d62-21ae-11d2-8b33-00600806d9b6}')
SWbemObjectEx = Guid('{d6bdafb2-9435-491f-bb87-6aa0f0bc31a2}')
SWbemObjectPath = Guid('{5791bc26-ce9c-11d1-97bf-0000f81e849c}')
SWbemObjectSet = Guid('{04b83d61-21ae-11d2-8b33-00600806d9b6}')
SWbemPrivilege = Guid('{26ee67bc-5804-11d2-8b4a-00600806d9b6}')
SWbemPrivilegeSet = Guid('{26ee67be-5804-11d2-8b4a-00600806d9b6}')
SWbemProperty = Guid('{04b83d5d-21ae-11d2-8b33-00600806d9b6}')
SWbemPropertySet = Guid('{04b83d5c-21ae-11d2-8b33-00600806d9b6}')
SWbemQualifier = Guid('{04b83d5f-21ae-11d2-8b33-00600806d9b6}')
SWbemQualifierSet = Guid('{04b83d5e-21ae-11d2-8b33-00600806d9b6}')
class SWbemQueryQualifiedName(Structure):
    m_uVersion: UInt32
    m_uTokenType: UInt32
    m_uNameListSize: UInt32
    m_ppszNameList: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
    m_bArraysUsed: win32more.Windows.Win32.Foundation.BOOL
    m_pbArrayElUsed: POINTER(win32more.Windows.Win32.Foundation.BOOL)
    m_puArrayIndex: POINTER(UInt32)
SWbemRefreshableItem = Guid('{8c6854bc-de4b-11d3-b390-00105a1f473a}')
SWbemRefresher = Guid('{d269bf5c-d9c1-11d3-b38f-00105a1f473a}')
class SWbemRpnConst(Union):
    m_pszStrVal: win32more.Windows.Win32.Foundation.PWSTR
    m_bBoolVal: win32more.Windows.Win32.Foundation.BOOL
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
    m_ppSelectList: POINTER(POINTER(win32more.Windows.Win32.System.Wmi.SWbemQueryQualifiedName))
    m_uFromTargetType: UInt32
    m_pszOptionalFromPath: win32more.Windows.Win32.Foundation.PWSTR
    m_uFromListSize: UInt32
    m_ppszFromList: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
    m_uWhereClauseSize: UInt32
    m_ppRpnWhereClause: POINTER(POINTER(win32more.Windows.Win32.System.Wmi.SWbemRpnQueryToken))
    m_dblWithinPolling: Double
    m_dblWithinWindow: Double
    m_uOrderByListSize: UInt32
    m_ppszOrderByList: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
    m_uOrderDirectionEl: POINTER(UInt32)
class SWbemRpnQueryToken(Structure):
    m_uVersion: UInt32
    m_uTokenType: UInt32
    m_uSubexpressionShape: UInt32
    m_uOperator: UInt32
    m_pRightIdent: POINTER(win32more.Windows.Win32.System.Wmi.SWbemQueryQualifiedName)
    m_pLeftIdent: POINTER(win32more.Windows.Win32.System.Wmi.SWbemQueryQualifiedName)
    m_uConstApparentType: UInt32
    m_Const: win32more.Windows.Win32.System.Wmi.SWbemRpnConst
    m_uConst2ApparentType: UInt32
    m_Const2: win32more.Windows.Win32.System.Wmi.SWbemRpnConst
    m_pszRightFunc: win32more.Windows.Win32.Foundation.PWSTR
    m_pszLeftFunc: win32more.Windows.Win32.Foundation.PWSTR
class SWbemRpnTokenList(Structure):
    m_uVersion: UInt32
    m_uTokenType: UInt32
    m_uNumTokens: UInt32
SWbemSecurity = Guid('{b54d66e9-2287-11d2-8b33-00600806d9b6}')
SWbemServices = Guid('{04b83d63-21ae-11d2-8b33-00600806d9b6}')
SWbemServicesEx = Guid('{62e522dc-8cf3-40a8-8b2e-37d595651e40}')
SWbemSink = Guid('{75718c9a-f029-11d1-a1ac-00c04fb6c223}')
UnsecuredApartment = Guid('{49bd2028-1523-11d1-ad79-00c04fd8fdff}')
WBEMSTATUS = Int32
WBEM_NO_ERROR: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = 0
WBEM_S_NO_ERROR: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = 0
WBEM_S_SAME: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = 0
WBEM_S_FALSE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = 1
WBEM_S_ALREADY_EXISTS: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = 262145
WBEM_S_RESET_TO_DEFAULT: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = 262146
WBEM_S_DIFFERENT: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = 262147
WBEM_S_TIMEDOUT: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = 262148
WBEM_S_NO_MORE_DATA: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = 262149
WBEM_S_OPERATION_CANCELLED: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = 262150
WBEM_S_PENDING: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = 262151
WBEM_S_DUPLICATE_OBJECTS: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = 262152
WBEM_S_ACCESS_DENIED: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = 262153
WBEM_S_PARTIAL_RESULTS: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = 262160
WBEM_S_SOURCE_NOT_AVAILABLE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = 262167
WBEM_E_FAILED: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217407
WBEM_E_NOT_FOUND: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217406
WBEM_E_ACCESS_DENIED: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217405
WBEM_E_PROVIDER_FAILURE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217404
WBEM_E_TYPE_MISMATCH: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217403
WBEM_E_OUT_OF_MEMORY: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217402
WBEM_E_INVALID_CONTEXT: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217401
WBEM_E_INVALID_PARAMETER: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217400
WBEM_E_NOT_AVAILABLE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217399
WBEM_E_CRITICAL_ERROR: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217398
WBEM_E_INVALID_STREAM: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217397
WBEM_E_NOT_SUPPORTED: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217396
WBEM_E_INVALID_SUPERCLASS: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217395
WBEM_E_INVALID_NAMESPACE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217394
WBEM_E_INVALID_OBJECT: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217393
WBEM_E_INVALID_CLASS: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217392
WBEM_E_PROVIDER_NOT_FOUND: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217391
WBEM_E_INVALID_PROVIDER_REGISTRATION: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217390
WBEM_E_PROVIDER_LOAD_FAILURE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217389
WBEM_E_INITIALIZATION_FAILURE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217388
WBEM_E_TRANSPORT_FAILURE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217387
WBEM_E_INVALID_OPERATION: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217386
WBEM_E_INVALID_QUERY: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217385
WBEM_E_INVALID_QUERY_TYPE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217384
WBEM_E_ALREADY_EXISTS: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217383
WBEM_E_OVERRIDE_NOT_ALLOWED: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217382
WBEM_E_PROPAGATED_QUALIFIER: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217381
WBEM_E_PROPAGATED_PROPERTY: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217380
WBEM_E_UNEXPECTED: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217379
WBEM_E_ILLEGAL_OPERATION: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217378
WBEM_E_CANNOT_BE_KEY: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217377
WBEM_E_INCOMPLETE_CLASS: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217376
WBEM_E_INVALID_SYNTAX: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217375
WBEM_E_NONDECORATED_OBJECT: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217374
WBEM_E_READ_ONLY: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217373
WBEM_E_PROVIDER_NOT_CAPABLE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217372
WBEM_E_CLASS_HAS_CHILDREN: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217371
WBEM_E_CLASS_HAS_INSTANCES: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217370
WBEM_E_QUERY_NOT_IMPLEMENTED: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217369
WBEM_E_ILLEGAL_NULL: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217368
WBEM_E_INVALID_QUALIFIER_TYPE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217367
WBEM_E_INVALID_PROPERTY_TYPE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217366
WBEM_E_VALUE_OUT_OF_RANGE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217365
WBEM_E_CANNOT_BE_SINGLETON: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217364
WBEM_E_INVALID_CIM_TYPE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217363
WBEM_E_INVALID_METHOD: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217362
WBEM_E_INVALID_METHOD_PARAMETERS: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217361
WBEM_E_SYSTEM_PROPERTY: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217360
WBEM_E_INVALID_PROPERTY: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217359
WBEM_E_CALL_CANCELLED: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217358
WBEM_E_SHUTTING_DOWN: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217357
WBEM_E_PROPAGATED_METHOD: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217356
WBEM_E_UNSUPPORTED_PARAMETER: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217355
WBEM_E_MISSING_PARAMETER_ID: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217354
WBEM_E_INVALID_PARAMETER_ID: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217353
WBEM_E_NONCONSECUTIVE_PARAMETER_IDS: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217352
WBEM_E_PARAMETER_ID_ON_RETVAL: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217351
WBEM_E_INVALID_OBJECT_PATH: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217350
WBEM_E_OUT_OF_DISK_SPACE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217349
WBEM_E_BUFFER_TOO_SMALL: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217348
WBEM_E_UNSUPPORTED_PUT_EXTENSION: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217347
WBEM_E_UNKNOWN_OBJECT_TYPE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217346
WBEM_E_UNKNOWN_PACKET_TYPE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217345
WBEM_E_MARSHAL_VERSION_MISMATCH: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217344
WBEM_E_MARSHAL_INVALID_SIGNATURE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217343
WBEM_E_INVALID_QUALIFIER: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217342
WBEM_E_INVALID_DUPLICATE_PARAMETER: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217341
WBEM_E_TOO_MUCH_DATA: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217340
WBEM_E_SERVER_TOO_BUSY: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217339
WBEM_E_INVALID_FLAVOR: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217338
WBEM_E_CIRCULAR_REFERENCE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217337
WBEM_E_UNSUPPORTED_CLASS_UPDATE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217336
WBEM_E_CANNOT_CHANGE_KEY_INHERITANCE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217335
WBEM_E_CANNOT_CHANGE_INDEX_INHERITANCE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217328
WBEM_E_TOO_MANY_PROPERTIES: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217327
WBEM_E_UPDATE_TYPE_MISMATCH: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217326
WBEM_E_UPDATE_OVERRIDE_NOT_ALLOWED: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217325
WBEM_E_UPDATE_PROPAGATED_METHOD: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217324
WBEM_E_METHOD_NOT_IMPLEMENTED: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217323
WBEM_E_METHOD_DISABLED: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217322
WBEM_E_REFRESHER_BUSY: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217321
WBEM_E_UNPARSABLE_QUERY: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217320
WBEM_E_NOT_EVENT_CLASS: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217319
WBEM_E_MISSING_GROUP_WITHIN: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217318
WBEM_E_MISSING_AGGREGATION_LIST: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217317
WBEM_E_PROPERTY_NOT_AN_OBJECT: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217316
WBEM_E_AGGREGATING_BY_OBJECT: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217315
WBEM_E_UNINTERPRETABLE_PROVIDER_QUERY: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217313
WBEM_E_BACKUP_RESTORE_WINMGMT_RUNNING: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217312
WBEM_E_QUEUE_OVERFLOW: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217311
WBEM_E_PRIVILEGE_NOT_HELD: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217310
WBEM_E_INVALID_OPERATOR: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217309
WBEM_E_LOCAL_CREDENTIALS: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217308
WBEM_E_CANNOT_BE_ABSTRACT: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217307
WBEM_E_AMENDED_OBJECT: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217306
WBEM_E_CLIENT_TOO_SLOW: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217305
WBEM_E_NULL_SECURITY_DESCRIPTOR: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217304
WBEM_E_TIMED_OUT: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217303
WBEM_E_INVALID_ASSOCIATION: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217302
WBEM_E_AMBIGUOUS_OPERATION: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217301
WBEM_E_QUOTA_VIOLATION: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217300
WBEM_E_RESERVED_001: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217299
WBEM_E_RESERVED_002: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217298
WBEM_E_UNSUPPORTED_LOCALE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217297
WBEM_E_HANDLE_OUT_OF_DATE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217296
WBEM_E_CONNECTION_FAILED: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217295
WBEM_E_INVALID_HANDLE_REQUEST: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217294
WBEM_E_PROPERTY_NAME_TOO_WIDE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217293
WBEM_E_CLASS_NAME_TOO_WIDE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217292
WBEM_E_METHOD_NAME_TOO_WIDE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217291
WBEM_E_QUALIFIER_NAME_TOO_WIDE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217290
WBEM_E_RERUN_COMMAND: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217289
WBEM_E_DATABASE_VER_MISMATCH: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217288
WBEM_E_VETO_DELETE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217287
WBEM_E_VETO_PUT: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217286
WBEM_E_INVALID_LOCALE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217280
WBEM_E_PROVIDER_SUSPENDED: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217279
WBEM_E_SYNCHRONIZATION_REQUIRED: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217278
WBEM_E_NO_SCHEMA: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217277
WBEM_E_PROVIDER_ALREADY_REGISTERED: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217276
WBEM_E_PROVIDER_NOT_REGISTERED: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217275
WBEM_E_FATAL_TRANSPORT_ERROR: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217274
WBEM_E_ENCRYPTED_CONNECTION_REQUIRED: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217273
WBEM_E_PROVIDER_TIMED_OUT: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217272
WBEM_E_NO_KEY: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217271
WBEM_E_PROVIDER_DISABLED: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147217270
WBEMESS_E_REGISTRATION_TOO_BROAD: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147213311
WBEMESS_E_REGISTRATION_TOO_PRECISE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147213310
WBEMESS_E_AUTHZ_NOT_PRIVILEGED: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147213309
WBEMMOF_E_EXPECTED_QUALIFIER_NAME: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205119
WBEMMOF_E_EXPECTED_SEMI: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205118
WBEMMOF_E_EXPECTED_OPEN_BRACE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205117
WBEMMOF_E_EXPECTED_CLOSE_BRACE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205116
WBEMMOF_E_EXPECTED_CLOSE_BRACKET: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205115
WBEMMOF_E_EXPECTED_CLOSE_PAREN: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205114
WBEMMOF_E_ILLEGAL_CONSTANT_VALUE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205113
WBEMMOF_E_EXPECTED_TYPE_IDENTIFIER: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205112
WBEMMOF_E_EXPECTED_OPEN_PAREN: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205111
WBEMMOF_E_UNRECOGNIZED_TOKEN: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205110
WBEMMOF_E_UNRECOGNIZED_TYPE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205109
WBEMMOF_E_EXPECTED_PROPERTY_NAME: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205108
WBEMMOF_E_TYPEDEF_NOT_SUPPORTED: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205107
WBEMMOF_E_UNEXPECTED_ALIAS: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205106
WBEMMOF_E_UNEXPECTED_ARRAY_INIT: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205105
WBEMMOF_E_INVALID_AMENDMENT_SYNTAX: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205104
WBEMMOF_E_INVALID_DUPLICATE_AMENDMENT: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205103
WBEMMOF_E_INVALID_PRAGMA: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205102
WBEMMOF_E_INVALID_NAMESPACE_SYNTAX: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205101
WBEMMOF_E_EXPECTED_CLASS_NAME: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205100
WBEMMOF_E_TYPE_MISMATCH: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205099
WBEMMOF_E_EXPECTED_ALIAS_NAME: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205098
WBEMMOF_E_INVALID_CLASS_DECLARATION: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205097
WBEMMOF_E_INVALID_INSTANCE_DECLARATION: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205096
WBEMMOF_E_EXPECTED_DOLLAR: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205095
WBEMMOF_E_CIMTYPE_QUALIFIER: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205094
WBEMMOF_E_DUPLICATE_PROPERTY: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205093
WBEMMOF_E_INVALID_NAMESPACE_SPECIFICATION: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205092
WBEMMOF_E_OUT_OF_RANGE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205091
WBEMMOF_E_INVALID_FILE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205090
WBEMMOF_E_ALIASES_IN_EMBEDDED: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205089
WBEMMOF_E_NULL_ARRAY_ELEM: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205088
WBEMMOF_E_DUPLICATE_QUALIFIER: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205087
WBEMMOF_E_EXPECTED_FLAVOR_TYPE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205086
WBEMMOF_E_INCOMPATIBLE_FLAVOR_TYPES: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205085
WBEMMOF_E_MULTIPLE_ALIASES: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205084
WBEMMOF_E_INCOMPATIBLE_FLAVOR_TYPES2: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205083
WBEMMOF_E_NO_ARRAYS_RETURNED: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205082
WBEMMOF_E_MUST_BE_IN_OR_OUT: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205081
WBEMMOF_E_INVALID_FLAGS_SYNTAX: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205080
WBEMMOF_E_EXPECTED_BRACE_OR_BAD_TYPE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205079
WBEMMOF_E_UNSUPPORTED_CIMV22_QUAL_VALUE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205078
WBEMMOF_E_UNSUPPORTED_CIMV22_DATA_TYPE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205077
WBEMMOF_E_INVALID_DELETEINSTANCE_SYNTAX: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205076
WBEMMOF_E_INVALID_QUALIFIER_SYNTAX: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205075
WBEMMOF_E_QUALIFIER_USED_OUTSIDE_SCOPE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205074
WBEMMOF_E_ERROR_CREATING_TEMP_FILE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205073
WBEMMOF_E_ERROR_INVALID_INCLUDE_FILE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205072
WBEMMOF_E_INVALID_DELETECLASS_SYNTAX: win32more.Windows.Win32.System.Wmi.WBEMSTATUS = -2147205071
WBEMSTATUS_FORMAT = Int32
WBEMSTATUS_FORMAT_NEWLINE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS_FORMAT = 0
WBEMSTATUS_FORMAT_NO_NEWLINE: win32more.Windows.Win32.System.Wmi.WBEMSTATUS_FORMAT = 1
WBEM_BACKUP_RESTORE_FLAGS = Int32
WBEM_FLAG_BACKUP_RESTORE_DEFAULT: win32more.Windows.Win32.System.Wmi.WBEM_BACKUP_RESTORE_FLAGS = 0
WBEM_FLAG_BACKUP_RESTORE_FORCE_SHUTDOWN: win32more.Windows.Win32.System.Wmi.WBEM_BACKUP_RESTORE_FLAGS = 1
WBEM_BATCH_TYPE = Int32
WBEM_FLAG_BATCH_IF_NEEDED: win32more.Windows.Win32.System.Wmi.WBEM_BATCH_TYPE = 0
WBEM_FLAG_MUST_BATCH: win32more.Windows.Win32.System.Wmi.WBEM_BATCH_TYPE = 1
WBEM_FLAG_MUST_NOT_BATCH: win32more.Windows.Win32.System.Wmi.WBEM_BATCH_TYPE = 2
WBEM_CHANGE_FLAG_TYPE = Int32
WBEM_FLAG_CREATE_OR_UPDATE: win32more.Windows.Win32.System.Wmi.WBEM_CHANGE_FLAG_TYPE = 0
WBEM_FLAG_UPDATE_ONLY: win32more.Windows.Win32.System.Wmi.WBEM_CHANGE_FLAG_TYPE = 1
WBEM_FLAG_CREATE_ONLY: win32more.Windows.Win32.System.Wmi.WBEM_CHANGE_FLAG_TYPE = 2
WBEM_FLAG_UPDATE_COMPATIBLE: win32more.Windows.Win32.System.Wmi.WBEM_CHANGE_FLAG_TYPE = 0
WBEM_FLAG_UPDATE_SAFE_MODE: win32more.Windows.Win32.System.Wmi.WBEM_CHANGE_FLAG_TYPE = 32
WBEM_FLAG_UPDATE_FORCE_MODE: win32more.Windows.Win32.System.Wmi.WBEM_CHANGE_FLAG_TYPE = 64
WBEM_MASK_UPDATE_MODE: win32more.Windows.Win32.System.Wmi.WBEM_CHANGE_FLAG_TYPE = 96
WBEM_FLAG_ADVISORY: win32more.Windows.Win32.System.Wmi.WBEM_CHANGE_FLAG_TYPE = 65536
WBEM_COMPARISON_FLAG = Int32
WBEM_COMPARISON_INCLUDE_ALL: win32more.Windows.Win32.System.Wmi.WBEM_COMPARISON_FLAG = 0
WBEM_FLAG_IGNORE_QUALIFIERS: win32more.Windows.Win32.System.Wmi.WBEM_COMPARISON_FLAG = 1
WBEM_FLAG_IGNORE_OBJECT_SOURCE: win32more.Windows.Win32.System.Wmi.WBEM_COMPARISON_FLAG = 2
WBEM_FLAG_IGNORE_DEFAULT_VALUES: win32more.Windows.Win32.System.Wmi.WBEM_COMPARISON_FLAG = 4
WBEM_FLAG_IGNORE_CLASS: win32more.Windows.Win32.System.Wmi.WBEM_COMPARISON_FLAG = 8
WBEM_FLAG_IGNORE_CASE: win32more.Windows.Win32.System.Wmi.WBEM_COMPARISON_FLAG = 16
WBEM_FLAG_IGNORE_FLAVOR: win32more.Windows.Win32.System.Wmi.WBEM_COMPARISON_FLAG = 32
WBEM_COMPILER_OPTIONS = Int32
WBEM_FLAG_CHECK_ONLY: win32more.Windows.Win32.System.Wmi.WBEM_COMPILER_OPTIONS = 1
WBEM_FLAG_AUTORECOVER: win32more.Windows.Win32.System.Wmi.WBEM_COMPILER_OPTIONS = 2
WBEM_FLAG_WMI_CHECK: win32more.Windows.Win32.System.Wmi.WBEM_COMPILER_OPTIONS = 4
WBEM_FLAG_CONSOLE_PRINT: win32more.Windows.Win32.System.Wmi.WBEM_COMPILER_OPTIONS = 8
WBEM_FLAG_DONT_ADD_TO_LIST: win32more.Windows.Win32.System.Wmi.WBEM_COMPILER_OPTIONS = 16
WBEM_FLAG_SPLIT_FILES: win32more.Windows.Win32.System.Wmi.WBEM_COMPILER_OPTIONS = 32
WBEM_FLAG_STORE_FILE: win32more.Windows.Win32.System.Wmi.WBEM_COMPILER_OPTIONS = 256
class WBEM_COMPILE_STATUS_INFO(Structure):
    lPhaseError: Int32
    hRes: win32more.Windows.Win32.Foundation.HRESULT
    ObjectNum: Int32
    FirstLine: Int32
    LastLine: Int32
    dwOutFlags: UInt32
WBEM_CONDITION_FLAG_TYPE = Int32
WBEM_FLAG_ALWAYS: win32more.Windows.Win32.System.Wmi.WBEM_CONDITION_FLAG_TYPE = 0
WBEM_FLAG_ONLY_IF_TRUE: win32more.Windows.Win32.System.Wmi.WBEM_CONDITION_FLAG_TYPE = 1
WBEM_FLAG_ONLY_IF_FALSE: win32more.Windows.Win32.System.Wmi.WBEM_CONDITION_FLAG_TYPE = 2
WBEM_FLAG_ONLY_IF_IDENTICAL: win32more.Windows.Win32.System.Wmi.WBEM_CONDITION_FLAG_TYPE = 3
WBEM_MASK_PRIMARY_CONDITION: win32more.Windows.Win32.System.Wmi.WBEM_CONDITION_FLAG_TYPE = 3
WBEM_FLAG_KEYS_ONLY: win32more.Windows.Win32.System.Wmi.WBEM_CONDITION_FLAG_TYPE = 4
WBEM_FLAG_REFS_ONLY: win32more.Windows.Win32.System.Wmi.WBEM_CONDITION_FLAG_TYPE = 8
WBEM_FLAG_LOCAL_ONLY: win32more.Windows.Win32.System.Wmi.WBEM_CONDITION_FLAG_TYPE = 16
WBEM_FLAG_PROPAGATED_ONLY: win32more.Windows.Win32.System.Wmi.WBEM_CONDITION_FLAG_TYPE = 32
WBEM_FLAG_SYSTEM_ONLY: win32more.Windows.Win32.System.Wmi.WBEM_CONDITION_FLAG_TYPE = 48
WBEM_FLAG_NONSYSTEM_ONLY: win32more.Windows.Win32.System.Wmi.WBEM_CONDITION_FLAG_TYPE = 64
WBEM_MASK_CONDITION_ORIGIN: win32more.Windows.Win32.System.Wmi.WBEM_CONDITION_FLAG_TYPE = 112
WBEM_FLAG_CLASS_OVERRIDES_ONLY: win32more.Windows.Win32.System.Wmi.WBEM_CONDITION_FLAG_TYPE = 256
WBEM_FLAG_CLASS_LOCAL_AND_OVERRIDES: win32more.Windows.Win32.System.Wmi.WBEM_CONDITION_FLAG_TYPE = 512
WBEM_MASK_CLASS_CONDITION: win32more.Windows.Win32.System.Wmi.WBEM_CONDITION_FLAG_TYPE = 768
WBEM_CONNECT_OPTIONS = Int32
WBEM_FLAG_CONNECT_REPOSITORY_ONLY: win32more.Windows.Win32.System.Wmi.WBEM_CONNECT_OPTIONS = 64
WBEM_FLAG_CONNECT_USE_MAX_WAIT: win32more.Windows.Win32.System.Wmi.WBEM_CONNECT_OPTIONS = 128
WBEM_FLAG_CONNECT_PROVIDERS: win32more.Windows.Win32.System.Wmi.WBEM_CONNECT_OPTIONS = 256
WBEM_EXTRA_RETURN_CODES = Int32
WBEM_S_INITIALIZED: win32more.Windows.Win32.System.Wmi.WBEM_EXTRA_RETURN_CODES = 0
WBEM_S_LIMITED_SERVICE: win32more.Windows.Win32.System.Wmi.WBEM_EXTRA_RETURN_CODES = 274433
WBEM_S_INDIRECTLY_UPDATED: win32more.Windows.Win32.System.Wmi.WBEM_EXTRA_RETURN_CODES = 274434
WBEM_S_SUBJECT_TO_SDS: win32more.Windows.Win32.System.Wmi.WBEM_EXTRA_RETURN_CODES = 274435
WBEM_E_RETRY_LATER: win32more.Windows.Win32.System.Wmi.WBEM_EXTRA_RETURN_CODES = -2147209215
WBEM_E_RESOURCE_CONTENTION: win32more.Windows.Win32.System.Wmi.WBEM_EXTRA_RETURN_CODES = -2147209214
WBEM_FLAVOR_TYPE = Int32
WBEM_FLAVOR_DONT_PROPAGATE: win32more.Windows.Win32.System.Wmi.WBEM_FLAVOR_TYPE = 0
WBEM_FLAVOR_FLAG_PROPAGATE_TO_INSTANCE: win32more.Windows.Win32.System.Wmi.WBEM_FLAVOR_TYPE = 1
WBEM_FLAVOR_FLAG_PROPAGATE_TO_DERIVED_CLASS: win32more.Windows.Win32.System.Wmi.WBEM_FLAVOR_TYPE = 2
WBEM_FLAVOR_MASK_PROPAGATION: win32more.Windows.Win32.System.Wmi.WBEM_FLAVOR_TYPE = 15
WBEM_FLAVOR_OVERRIDABLE: win32more.Windows.Win32.System.Wmi.WBEM_FLAVOR_TYPE = 0
WBEM_FLAVOR_NOT_OVERRIDABLE: win32more.Windows.Win32.System.Wmi.WBEM_FLAVOR_TYPE = 16
WBEM_FLAVOR_MASK_PERMISSIONS: win32more.Windows.Win32.System.Wmi.WBEM_FLAVOR_TYPE = 16
WBEM_FLAVOR_ORIGIN_LOCAL: win32more.Windows.Win32.System.Wmi.WBEM_FLAVOR_TYPE = 0
WBEM_FLAVOR_ORIGIN_PROPAGATED: win32more.Windows.Win32.System.Wmi.WBEM_FLAVOR_TYPE = 32
WBEM_FLAVOR_ORIGIN_SYSTEM: win32more.Windows.Win32.System.Wmi.WBEM_FLAVOR_TYPE = 64
WBEM_FLAVOR_MASK_ORIGIN: win32more.Windows.Win32.System.Wmi.WBEM_FLAVOR_TYPE = 96
WBEM_FLAVOR_NOT_AMENDED: win32more.Windows.Win32.System.Wmi.WBEM_FLAVOR_TYPE = 0
WBEM_FLAVOR_AMENDED: win32more.Windows.Win32.System.Wmi.WBEM_FLAVOR_TYPE = 128
WBEM_FLAVOR_MASK_AMENDED: win32more.Windows.Win32.System.Wmi.WBEM_FLAVOR_TYPE = 128
WBEM_GENERIC_FLAG_TYPE = Int32
WBEM_FLAG_RETURN_IMMEDIATELY: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE = 16
WBEM_FLAG_RETURN_WBEM_COMPLETE: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE = 0
WBEM_FLAG_BIDIRECTIONAL: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE = 0
WBEM_FLAG_FORWARD_ONLY: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE = 32
WBEM_FLAG_NO_ERROR_OBJECT: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE = 64
WBEM_FLAG_RETURN_ERROR_OBJECT: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE = 0
WBEM_FLAG_SEND_STATUS: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE = 128
WBEM_FLAG_DONT_SEND_STATUS: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE = 0
WBEM_FLAG_ENSURE_LOCATABLE: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE = 256
WBEM_FLAG_DIRECT_READ: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE = 512
WBEM_FLAG_SEND_ONLY_SELECTED: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE = 0
WBEM_RETURN_WHEN_COMPLETE: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE = 0
WBEM_RETURN_IMMEDIATELY: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE = 16
WBEM_MASK_RESERVED_FLAGS: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE = 126976
WBEM_FLAG_USE_AMENDED_QUALIFIERS: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE = 131072
WBEM_FLAG_STRONG_VALIDATION: win32more.Windows.Win32.System.Wmi.WBEM_GENERIC_FLAG_TYPE = 1048576
WBEM_GENUS_TYPE = Int32
WBEM_GENUS_CLASS: win32more.Windows.Win32.System.Wmi.WBEM_GENUS_TYPE = 1
WBEM_GENUS_INSTANCE: win32more.Windows.Win32.System.Wmi.WBEM_GENUS_TYPE = 2
WBEM_GET_KEY_FLAGS = Int32
WBEMPATH_TEXT: win32more.Windows.Win32.System.Wmi.WBEM_GET_KEY_FLAGS = 1
WBEMPATH_QUOTEDTEXT: win32more.Windows.Win32.System.Wmi.WBEM_GET_KEY_FLAGS = 2
WBEM_GET_TEXT_FLAGS = Int32
WBEMPATH_COMPRESSED: win32more.Windows.Win32.System.Wmi.WBEM_GET_TEXT_FLAGS = 1
WBEMPATH_GET_RELATIVE_ONLY: win32more.Windows.Win32.System.Wmi.WBEM_GET_TEXT_FLAGS = 2
WBEMPATH_GET_SERVER_TOO: win32more.Windows.Win32.System.Wmi.WBEM_GET_TEXT_FLAGS = 4
WBEMPATH_GET_SERVER_AND_NAMESPACE_ONLY: win32more.Windows.Win32.System.Wmi.WBEM_GET_TEXT_FLAGS = 8
WBEMPATH_GET_NAMESPACE_ONLY: win32more.Windows.Win32.System.Wmi.WBEM_GET_TEXT_FLAGS = 16
WBEMPATH_GET_ORIGINAL: win32more.Windows.Win32.System.Wmi.WBEM_GET_TEXT_FLAGS = 32
WBEM_INFORMATION_FLAG_TYPE = Int32
WBEM_FLAG_SHORT_NAME: win32more.Windows.Win32.System.Wmi.WBEM_INFORMATION_FLAG_TYPE = 1
WBEM_FLAG_LONG_NAME: win32more.Windows.Win32.System.Wmi.WBEM_INFORMATION_FLAG_TYPE = 2
WBEM_LIMITATION_FLAG_TYPE = Int32
WBEM_FLAG_EXCLUDE_OBJECT_QUALIFIERS: win32more.Windows.Win32.System.Wmi.WBEM_LIMITATION_FLAG_TYPE = 16
WBEM_FLAG_EXCLUDE_PROPERTY_QUALIFIERS: win32more.Windows.Win32.System.Wmi.WBEM_LIMITATION_FLAG_TYPE = 32
WBEM_LIMITS = Int32
WBEM_MAX_IDENTIFIER: win32more.Windows.Win32.System.Wmi.WBEM_LIMITS = 4096
WBEM_MAX_QUERY: win32more.Windows.Win32.System.Wmi.WBEM_LIMITS = 16384
WBEM_MAX_PATH: win32more.Windows.Win32.System.Wmi.WBEM_LIMITS = 8192
WBEM_MAX_OBJECT_NESTING: win32more.Windows.Win32.System.Wmi.WBEM_LIMITS = 64
WBEM_MAX_USER_PROPERTIES: win32more.Windows.Win32.System.Wmi.WBEM_LIMITS = 1024
WBEM_LOCKING_FLAG_TYPE = Int32
WBEM_FLAG_ALLOW_READ: win32more.Windows.Win32.System.Wmi.WBEM_LOCKING_FLAG_TYPE = 1
WBEM_LOGIN_TYPE = Int32
WBEM_FLAG_INPROC_LOGIN: win32more.Windows.Win32.System.Wmi.WBEM_LOGIN_TYPE = 0
WBEM_FLAG_LOCAL_LOGIN: win32more.Windows.Win32.System.Wmi.WBEM_LOGIN_TYPE = 1
WBEM_FLAG_REMOTE_LOGIN: win32more.Windows.Win32.System.Wmi.WBEM_LOGIN_TYPE = 2
WBEM_AUTHENTICATION_METHOD_MASK: win32more.Windows.Win32.System.Wmi.WBEM_LOGIN_TYPE = 15
WBEM_FLAG_USE_MULTIPLE_CHALLENGES: win32more.Windows.Win32.System.Wmi.WBEM_LOGIN_TYPE = 16
WBEM_PATH_CREATE_FLAG = Int32
WBEMPATH_CREATE_ACCEPT_RELATIVE: win32more.Windows.Win32.System.Wmi.WBEM_PATH_CREATE_FLAG = 1
WBEMPATH_CREATE_ACCEPT_ABSOLUTE: win32more.Windows.Win32.System.Wmi.WBEM_PATH_CREATE_FLAG = 2
WBEMPATH_CREATE_ACCEPT_ALL: win32more.Windows.Win32.System.Wmi.WBEM_PATH_CREATE_FLAG = 4
WBEMPATH_TREAT_SINGLE_IDENT_AS_NS: win32more.Windows.Win32.System.Wmi.WBEM_PATH_CREATE_FLAG = 8
WBEM_PATH_STATUS_FLAG = Int32
WBEMPATH_INFO_ANON_LOCAL_MACHINE: win32more.Windows.Win32.System.Wmi.WBEM_PATH_STATUS_FLAG = 1
WBEMPATH_INFO_HAS_MACHINE_NAME: win32more.Windows.Win32.System.Wmi.WBEM_PATH_STATUS_FLAG = 2
WBEMPATH_INFO_IS_CLASS_REF: win32more.Windows.Win32.System.Wmi.WBEM_PATH_STATUS_FLAG = 4
WBEMPATH_INFO_IS_INST_REF: win32more.Windows.Win32.System.Wmi.WBEM_PATH_STATUS_FLAG = 8
WBEMPATH_INFO_HAS_SUBSCOPES: win32more.Windows.Win32.System.Wmi.WBEM_PATH_STATUS_FLAG = 16
WBEMPATH_INFO_IS_COMPOUND: win32more.Windows.Win32.System.Wmi.WBEM_PATH_STATUS_FLAG = 32
WBEMPATH_INFO_HAS_V2_REF_PATHS: win32more.Windows.Win32.System.Wmi.WBEM_PATH_STATUS_FLAG = 64
WBEMPATH_INFO_HAS_IMPLIED_KEY: win32more.Windows.Win32.System.Wmi.WBEM_PATH_STATUS_FLAG = 128
WBEMPATH_INFO_CONTAINS_SINGLETON: win32more.Windows.Win32.System.Wmi.WBEM_PATH_STATUS_FLAG = 256
WBEMPATH_INFO_V1_COMPLIANT: win32more.Windows.Win32.System.Wmi.WBEM_PATH_STATUS_FLAG = 512
WBEMPATH_INFO_V2_COMPLIANT: win32more.Windows.Win32.System.Wmi.WBEM_PATH_STATUS_FLAG = 1024
WBEMPATH_INFO_CIM_COMPLIANT: win32more.Windows.Win32.System.Wmi.WBEM_PATH_STATUS_FLAG = 2048
WBEMPATH_INFO_IS_SINGLETON: win32more.Windows.Win32.System.Wmi.WBEM_PATH_STATUS_FLAG = 4096
WBEMPATH_INFO_IS_PARENT: win32more.Windows.Win32.System.Wmi.WBEM_PATH_STATUS_FLAG = 8192
WBEMPATH_INFO_SERVER_NAMESPACE_ONLY: win32more.Windows.Win32.System.Wmi.WBEM_PATH_STATUS_FLAG = 16384
WBEMPATH_INFO_NATIVE_PATH: win32more.Windows.Win32.System.Wmi.WBEM_PATH_STATUS_FLAG = 32768
WBEMPATH_INFO_WMI_PATH: win32more.Windows.Win32.System.Wmi.WBEM_PATH_STATUS_FLAG = 65536
WBEMPATH_INFO_PATH_HAD_SERVER: win32more.Windows.Win32.System.Wmi.WBEM_PATH_STATUS_FLAG = 131072
WBEM_PROVIDER_FLAGS = Int32
WBEM_FLAG_OWNER_UPDATE: win32more.Windows.Win32.System.Wmi.WBEM_PROVIDER_FLAGS = 65536
WBEM_PROVIDER_REQUIREMENTS_TYPE = Int32
WBEM_REQUIREMENTS_START_POSTFILTER: win32more.Windows.Win32.System.Wmi.WBEM_PROVIDER_REQUIREMENTS_TYPE = 0
WBEM_REQUIREMENTS_STOP_POSTFILTER: win32more.Windows.Win32.System.Wmi.WBEM_PROVIDER_REQUIREMENTS_TYPE = 1
WBEM_REQUIREMENTS_RECHECK_SUBSCRIPTIONS: win32more.Windows.Win32.System.Wmi.WBEM_PROVIDER_REQUIREMENTS_TYPE = 2
WBEM_QUERY_FLAG_TYPE = Int32
WBEM_FLAG_DEEP: win32more.Windows.Win32.System.Wmi.WBEM_QUERY_FLAG_TYPE = 0
WBEM_FLAG_SHALLOW: win32more.Windows.Win32.System.Wmi.WBEM_QUERY_FLAG_TYPE = 1
WBEM_FLAG_PROTOTYPE: win32more.Windows.Win32.System.Wmi.WBEM_QUERY_FLAG_TYPE = 2
WBEM_REFRESHER_FLAGS = Int32
WBEM_FLAG_REFRESH_AUTO_RECONNECT: win32more.Windows.Win32.System.Wmi.WBEM_REFRESHER_FLAGS = 0
WBEM_FLAG_REFRESH_NO_AUTO_RECONNECT: win32more.Windows.Win32.System.Wmi.WBEM_REFRESHER_FLAGS = 1
WBEM_SECURITY_FLAGS = Int32
WBEM_ENABLE: win32more.Windows.Win32.System.Wmi.WBEM_SECURITY_FLAGS = 1
WBEM_METHOD_EXECUTE: win32more.Windows.Win32.System.Wmi.WBEM_SECURITY_FLAGS = 2
WBEM_FULL_WRITE_REP: win32more.Windows.Win32.System.Wmi.WBEM_SECURITY_FLAGS = 4
WBEM_PARTIAL_WRITE_REP: win32more.Windows.Win32.System.Wmi.WBEM_SECURITY_FLAGS = 8
WBEM_WRITE_PROVIDER: win32more.Windows.Win32.System.Wmi.WBEM_SECURITY_FLAGS = 16
WBEM_REMOTE_ACCESS: win32more.Windows.Win32.System.Wmi.WBEM_SECURITY_FLAGS = 32
WBEM_RIGHT_SUBSCRIBE: win32more.Windows.Win32.System.Wmi.WBEM_SECURITY_FLAGS = 64
WBEM_RIGHT_PUBLISH: win32more.Windows.Win32.System.Wmi.WBEM_SECURITY_FLAGS = 128
WBEM_SHUTDOWN_FLAGS = Int32
WBEM_SHUTDOWN_UNLOAD_COMPONENT: win32more.Windows.Win32.System.Wmi.WBEM_SHUTDOWN_FLAGS = 1
WBEM_SHUTDOWN_WMI: win32more.Windows.Win32.System.Wmi.WBEM_SHUTDOWN_FLAGS = 2
WBEM_SHUTDOWN_OS: win32more.Windows.Win32.System.Wmi.WBEM_SHUTDOWN_FLAGS = 3
WBEM_STATUS_TYPE = Int32
WBEM_STATUS_COMPLETE: win32more.Windows.Win32.System.Wmi.WBEM_STATUS_TYPE = 0
WBEM_STATUS_REQUIREMENTS: win32more.Windows.Win32.System.Wmi.WBEM_STATUS_TYPE = 1
WBEM_STATUS_PROGRESS: win32more.Windows.Win32.System.Wmi.WBEM_STATUS_TYPE = 2
WBEM_STATUS_LOGGING_INFORMATION: win32more.Windows.Win32.System.Wmi.WBEM_STATUS_TYPE = 256
WBEM_STATUS_LOGGING_INFORMATION_PROVIDER: win32more.Windows.Win32.System.Wmi.WBEM_STATUS_TYPE = 512
WBEM_STATUS_LOGGING_INFORMATION_HOST: win32more.Windows.Win32.System.Wmi.WBEM_STATUS_TYPE = 1024
WBEM_STATUS_LOGGING_INFORMATION_REPOSITORY: win32more.Windows.Win32.System.Wmi.WBEM_STATUS_TYPE = 2048
WBEM_STATUS_LOGGING_INFORMATION_ESS: win32more.Windows.Win32.System.Wmi.WBEM_STATUS_TYPE = 4096
WBEM_TEXT_FLAG_TYPE = Int32
WBEM_FLAG_NO_FLAVORS: win32more.Windows.Win32.System.Wmi.WBEM_TEXT_FLAG_TYPE = 1
WBEM_UNSECAPP_FLAG_TYPE = Int32
WBEM_FLAG_UNSECAPP_DEFAULT_CHECK_ACCESS: win32more.Windows.Win32.System.Wmi.WBEM_UNSECAPP_FLAG_TYPE = 0
WBEM_FLAG_UNSECAPP_CHECK_ACCESS: win32more.Windows.Win32.System.Wmi.WBEM_UNSECAPP_FLAG_TYPE = 1
WBEM_FLAG_UNSECAPP_DONT_CHECK_ACCESS: win32more.Windows.Win32.System.Wmi.WBEM_UNSECAPP_FLAG_TYPE = 2
WMIExtension = Guid('{f0975afe-5c7f-11d2-8b74-00104b2afb41}')
WMIQ_ANALYSIS_TYPE = Int32
WMIQ_ANALYSIS_RPN_SEQUENCE: win32more.Windows.Win32.System.Wmi.WMIQ_ANALYSIS_TYPE = 1
WMIQ_ANALYSIS_ASSOC_QUERY: win32more.Windows.Win32.System.Wmi.WMIQ_ANALYSIS_TYPE = 2
WMIQ_ANALYSIS_PROP_ANALYSIS_MATRIX: win32more.Windows.Win32.System.Wmi.WMIQ_ANALYSIS_TYPE = 3
WMIQ_ANALYSIS_QUERY_TEXT: win32more.Windows.Win32.System.Wmi.WMIQ_ANALYSIS_TYPE = 4
WMIQ_ANALYSIS_RESERVED: win32more.Windows.Win32.System.Wmi.WMIQ_ANALYSIS_TYPE = 134217728
WMIQ_ASSOCQ_FLAGS = Int32
WMIQ_ASSOCQ_ASSOCIATORS: win32more.Windows.Win32.System.Wmi.WMIQ_ASSOCQ_FLAGS = 1
WMIQ_ASSOCQ_REFERENCES: win32more.Windows.Win32.System.Wmi.WMIQ_ASSOCQ_FLAGS = 2
WMIQ_ASSOCQ_RESULTCLASS: win32more.Windows.Win32.System.Wmi.WMIQ_ASSOCQ_FLAGS = 4
WMIQ_ASSOCQ_ASSOCCLASS: win32more.Windows.Win32.System.Wmi.WMIQ_ASSOCQ_FLAGS = 8
WMIQ_ASSOCQ_ROLE: win32more.Windows.Win32.System.Wmi.WMIQ_ASSOCQ_FLAGS = 16
WMIQ_ASSOCQ_RESULTROLE: win32more.Windows.Win32.System.Wmi.WMIQ_ASSOCQ_FLAGS = 32
WMIQ_ASSOCQ_REQUIREDQUALIFIER: win32more.Windows.Win32.System.Wmi.WMIQ_ASSOCQ_FLAGS = 64
WMIQ_ASSOCQ_REQUIREDASSOCQUALIFIER: win32more.Windows.Win32.System.Wmi.WMIQ_ASSOCQ_FLAGS = 128
WMIQ_ASSOCQ_CLASSDEFSONLY: win32more.Windows.Win32.System.Wmi.WMIQ_ASSOCQ_FLAGS = 256
WMIQ_ASSOCQ_KEYSONLY: win32more.Windows.Win32.System.Wmi.WMIQ_ASSOCQ_FLAGS = 512
WMIQ_ASSOCQ_SCHEMAONLY: win32more.Windows.Win32.System.Wmi.WMIQ_ASSOCQ_FLAGS = 1024
WMIQ_ASSOCQ_CLASSREFSONLY: win32more.Windows.Win32.System.Wmi.WMIQ_ASSOCQ_FLAGS = 2048
WMIQ_LANGUAGE_FEATURES = Int32
WMIQ_LF1_BASIC_SELECT: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 1
WMIQ_LF2_CLASS_NAME_IN_QUERY: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 2
WMIQ_LF3_STRING_CASE_FUNCTIONS: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 3
WMIQ_LF4_PROP_TO_PROP_TESTS: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 4
WMIQ_LF5_COUNT_STAR: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 5
WMIQ_LF6_ORDER_BY: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 6
WMIQ_LF7_DISTINCT: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 7
WMIQ_LF8_ISA: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 8
WMIQ_LF9_THIS: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 9
WMIQ_LF10_COMPEX_SUBEXPRESSIONS: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 10
WMIQ_LF11_ALIASING: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 11
WMIQ_LF12_GROUP_BY_HAVING: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 12
WMIQ_LF13_WMI_WITHIN: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 13
WMIQ_LF14_SQL_WRITE_OPERATIONS: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 14
WMIQ_LF15_GO: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 15
WMIQ_LF16_SINGLE_LEVEL_TRANSACTIONS: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 16
WMIQ_LF17_QUALIFIED_NAMES: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 17
WMIQ_LF18_ASSOCIATONS: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 18
WMIQ_LF19_SYSTEM_PROPERTIES: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 19
WMIQ_LF20_EXTENDED_SYSTEM_PROPERTIES: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 20
WMIQ_LF21_SQL89_JOINS: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 21
WMIQ_LF22_SQL92_JOINS: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 22
WMIQ_LF23_SUBSELECTS: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 23
WMIQ_LF24_UMI_EXTENSIONS: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 24
WMIQ_LF25_DATEPART: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 25
WMIQ_LF26_LIKE: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 26
WMIQ_LF27_CIM_TEMPORAL_CONSTRUCTS: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 27
WMIQ_LF28_STANDARD_AGGREGATES: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 28
WMIQ_LF29_MULTI_LEVEL_ORDER_BY: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 29
WMIQ_LF30_WMI_PRAGMAS: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 30
WMIQ_LF31_QUALIFIER_TESTS: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 31
WMIQ_LF32_SP_EXECUTE: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 32
WMIQ_LF33_ARRAY_ACCESS: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 33
WMIQ_LF34_UNION: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 34
WMIQ_LF35_COMPLEX_SELECT_TARGET: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 35
WMIQ_LF36_REFERENCE_TESTS: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 36
WMIQ_LF37_SELECT_INTO: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 37
WMIQ_LF38_BASIC_DATETIME_TESTS: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 38
WMIQ_LF39_COUNT_COLUMN: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 39
WMIQ_LF40_BETWEEN: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 40
WMIQ_LF_LAST: win32more.Windows.Win32.System.Wmi.WMIQ_LANGUAGE_FEATURES = 40
WMIQ_RPNF_FEATURE = Int32
WMIQ_RPNF_WHERE_CLAUSE_PRESENT: win32more.Windows.Win32.System.Wmi.WMIQ_RPNF_FEATURE = 1
WMIQ_RPNF_QUERY_IS_CONJUNCTIVE: win32more.Windows.Win32.System.Wmi.WMIQ_RPNF_FEATURE = 2
WMIQ_RPNF_QUERY_IS_DISJUNCTIVE: win32more.Windows.Win32.System.Wmi.WMIQ_RPNF_FEATURE = 4
WMIQ_RPNF_PROJECTION: win32more.Windows.Win32.System.Wmi.WMIQ_RPNF_FEATURE = 8
WMIQ_RPNF_FEATURE_SELECT_STAR: win32more.Windows.Win32.System.Wmi.WMIQ_RPNF_FEATURE = 16
WMIQ_RPNF_EQUALITY_TESTS_ONLY: win32more.Windows.Win32.System.Wmi.WMIQ_RPNF_FEATURE = 32
WMIQ_RPNF_COUNT_STAR: win32more.Windows.Win32.System.Wmi.WMIQ_RPNF_FEATURE = 64
WMIQ_RPNF_QUALIFIED_NAMES_USED: win32more.Windows.Win32.System.Wmi.WMIQ_RPNF_FEATURE = 128
WMIQ_RPNF_SYSPROP_CLASS_USED: win32more.Windows.Win32.System.Wmi.WMIQ_RPNF_FEATURE = 256
WMIQ_RPNF_PROP_TO_PROP_TESTS: win32more.Windows.Win32.System.Wmi.WMIQ_RPNF_FEATURE = 512
WMIQ_RPNF_ORDER_BY: win32more.Windows.Win32.System.Wmi.WMIQ_RPNF_FEATURE = 1024
WMIQ_RPNF_ISA_USED: win32more.Windows.Win32.System.Wmi.WMIQ_RPNF_FEATURE = 2048
WMIQ_RPNF_GROUP_BY_HAVING: win32more.Windows.Win32.System.Wmi.WMIQ_RPNF_FEATURE = 4096
WMIQ_RPNF_ARRAY_ACCESS_USED: win32more.Windows.Win32.System.Wmi.WMIQ_RPNF_FEATURE = 8192
WMIQ_RPN_TOKEN_FLAGS = Int32
WMIQ_RPN_TOKEN_EXPRESSION: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 1
WMIQ_RPN_TOKEN_AND: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 2
WMIQ_RPN_TOKEN_OR: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 3
WMIQ_RPN_TOKEN_NOT: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 4
WMIQ_RPN_OP_UNDEFINED: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 0
WMIQ_RPN_OP_EQ: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 1
WMIQ_RPN_OP_NE: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 2
WMIQ_RPN_OP_GE: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 3
WMIQ_RPN_OP_LE: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 4
WMIQ_RPN_OP_LT: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 5
WMIQ_RPN_OP_GT: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 6
WMIQ_RPN_OP_LIKE: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 7
WMIQ_RPN_OP_ISA: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 8
WMIQ_RPN_OP_ISNOTA: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 9
WMIQ_RPN_OP_ISNULL: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 10
WMIQ_RPN_OP_ISNOTNULL: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 11
WMIQ_RPN_LEFT_PROPERTY_NAME: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 1
WMIQ_RPN_RIGHT_PROPERTY_NAME: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 2
WMIQ_RPN_CONST2: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 4
WMIQ_RPN_CONST: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 8
WMIQ_RPN_RELOP: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 16
WMIQ_RPN_LEFT_FUNCTION: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 32
WMIQ_RPN_RIGHT_FUNCTION: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 64
WMIQ_RPN_GET_TOKEN_TYPE: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 1
WMIQ_RPN_GET_EXPR_SHAPE: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 2
WMIQ_RPN_GET_LEFT_FUNCTION: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 3
WMIQ_RPN_GET_RIGHT_FUNCTION: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 4
WMIQ_RPN_GET_RELOP: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 5
WMIQ_RPN_NEXT_TOKEN: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 1
WMIQ_RPN_FROM_UNARY: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 1
WMIQ_RPN_FROM_PATH: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 2
WMIQ_RPN_FROM_CLASS_LIST: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 4
WMIQ_RPN_FROM_MULTIPLE: win32more.Windows.Win32.System.Wmi.WMIQ_RPN_TOKEN_FLAGS = 8
WMI_OBJ_TEXT = Int32
WMI_OBJ_TEXT_CIM_DTD_2_0: win32more.Windows.Win32.System.Wmi.WMI_OBJ_TEXT = 1
WMI_OBJ_TEXT_WMI_DTD_2_0: win32more.Windows.Win32.System.Wmi.WMI_OBJ_TEXT = 2
WMI_OBJ_TEXT_WMI_EXT1: win32more.Windows.Win32.System.Wmi.WMI_OBJ_TEXT = 3
WMI_OBJ_TEXT_WMI_EXT2: win32more.Windows.Win32.System.Wmi.WMI_OBJ_TEXT = 4
WMI_OBJ_TEXT_WMI_EXT3: win32more.Windows.Win32.System.Wmi.WMI_OBJ_TEXT = 5
WMI_OBJ_TEXT_WMI_EXT4: win32more.Windows.Win32.System.Wmi.WMI_OBJ_TEXT = 6
WMI_OBJ_TEXT_WMI_EXT5: win32more.Windows.Win32.System.Wmi.WMI_OBJ_TEXT = 7
WMI_OBJ_TEXT_WMI_EXT6: win32more.Windows.Win32.System.Wmi.WMI_OBJ_TEXT = 8
WMI_OBJ_TEXT_WMI_EXT7: win32more.Windows.Win32.System.Wmi.WMI_OBJ_TEXT = 9
WMI_OBJ_TEXT_WMI_EXT8: win32more.Windows.Win32.System.Wmi.WMI_OBJ_TEXT = 10
WMI_OBJ_TEXT_WMI_EXT9: win32more.Windows.Win32.System.Wmi.WMI_OBJ_TEXT = 11
WMI_OBJ_TEXT_WMI_EXT10: win32more.Windows.Win32.System.Wmi.WMI_OBJ_TEXT = 12
WMI_OBJ_TEXT_LAST: win32more.Windows.Win32.System.Wmi.WMI_OBJ_TEXT = 13
WbemAdministrativeLocator = Guid('{cb8555cc-9128-11d1-ad9b-00c04fd8fdff}')
WbemAuthenticatedLocator = Guid('{cd184336-9128-11d1-ad9b-00c04fd8fdff}')
WbemAuthenticationLevelEnum = Int32
wbemAuthenticationLevelDefault: win32more.Windows.Win32.System.Wmi.WbemAuthenticationLevelEnum = 0
wbemAuthenticationLevelNone: win32more.Windows.Win32.System.Wmi.WbemAuthenticationLevelEnum = 1
wbemAuthenticationLevelConnect: win32more.Windows.Win32.System.Wmi.WbemAuthenticationLevelEnum = 2
wbemAuthenticationLevelCall: win32more.Windows.Win32.System.Wmi.WbemAuthenticationLevelEnum = 3
wbemAuthenticationLevelPkt: win32more.Windows.Win32.System.Wmi.WbemAuthenticationLevelEnum = 4
wbemAuthenticationLevelPktIntegrity: win32more.Windows.Win32.System.Wmi.WbemAuthenticationLevelEnum = 5
wbemAuthenticationLevelPktPrivacy: win32more.Windows.Win32.System.Wmi.WbemAuthenticationLevelEnum = 6
WbemBackupRestore = Guid('{c49e32c6-bc8b-11d2-85d4-00105a1f8304}')
WbemChangeFlagEnum = Int32
wbemChangeFlagCreateOrUpdate: win32more.Windows.Win32.System.Wmi.WbemChangeFlagEnum = 0
wbemChangeFlagUpdateOnly: win32more.Windows.Win32.System.Wmi.WbemChangeFlagEnum = 1
wbemChangeFlagCreateOnly: win32more.Windows.Win32.System.Wmi.WbemChangeFlagEnum = 2
wbemChangeFlagUpdateCompatible: win32more.Windows.Win32.System.Wmi.WbemChangeFlagEnum = 0
wbemChangeFlagUpdateSafeMode: win32more.Windows.Win32.System.Wmi.WbemChangeFlagEnum = 32
wbemChangeFlagUpdateForceMode: win32more.Windows.Win32.System.Wmi.WbemChangeFlagEnum = 64
wbemChangeFlagStrongValidation: win32more.Windows.Win32.System.Wmi.WbemChangeFlagEnum = 128
wbemChangeFlagAdvisory: win32more.Windows.Win32.System.Wmi.WbemChangeFlagEnum = 65536
WbemCimtypeEnum = Int32
wbemCimtypeSint8: win32more.Windows.Win32.System.Wmi.WbemCimtypeEnum = 16
wbemCimtypeUint8: win32more.Windows.Win32.System.Wmi.WbemCimtypeEnum = 17
wbemCimtypeSint16: win32more.Windows.Win32.System.Wmi.WbemCimtypeEnum = 2
wbemCimtypeUint16: win32more.Windows.Win32.System.Wmi.WbemCimtypeEnum = 18
wbemCimtypeSint32: win32more.Windows.Win32.System.Wmi.WbemCimtypeEnum = 3
wbemCimtypeUint32: win32more.Windows.Win32.System.Wmi.WbemCimtypeEnum = 19
wbemCimtypeSint64: win32more.Windows.Win32.System.Wmi.WbemCimtypeEnum = 20
wbemCimtypeUint64: win32more.Windows.Win32.System.Wmi.WbemCimtypeEnum = 21
wbemCimtypeReal32: win32more.Windows.Win32.System.Wmi.WbemCimtypeEnum = 4
wbemCimtypeReal64: win32more.Windows.Win32.System.Wmi.WbemCimtypeEnum = 5
wbemCimtypeBoolean: win32more.Windows.Win32.System.Wmi.WbemCimtypeEnum = 11
wbemCimtypeString: win32more.Windows.Win32.System.Wmi.WbemCimtypeEnum = 8
wbemCimtypeDatetime: win32more.Windows.Win32.System.Wmi.WbemCimtypeEnum = 101
wbemCimtypeReference: win32more.Windows.Win32.System.Wmi.WbemCimtypeEnum = 102
wbemCimtypeChar16: win32more.Windows.Win32.System.Wmi.WbemCimtypeEnum = 103
wbemCimtypeObject: win32more.Windows.Win32.System.Wmi.WbemCimtypeEnum = 13
WbemClassObject = Guid('{9a653086-174f-11d2-b5f9-00104b703efd}')
WbemComparisonFlagEnum = Int32
wbemComparisonFlagIncludeAll: win32more.Windows.Win32.System.Wmi.WbemComparisonFlagEnum = 0
wbemComparisonFlagIgnoreQualifiers: win32more.Windows.Win32.System.Wmi.WbemComparisonFlagEnum = 1
wbemComparisonFlagIgnoreObjectSource: win32more.Windows.Win32.System.Wmi.WbemComparisonFlagEnum = 2
wbemComparisonFlagIgnoreDefaultValues: win32more.Windows.Win32.System.Wmi.WbemComparisonFlagEnum = 4
wbemComparisonFlagIgnoreClass: win32more.Windows.Win32.System.Wmi.WbemComparisonFlagEnum = 8
wbemComparisonFlagIgnoreCase: win32more.Windows.Win32.System.Wmi.WbemComparisonFlagEnum = 16
wbemComparisonFlagIgnoreFlavor: win32more.Windows.Win32.System.Wmi.WbemComparisonFlagEnum = 32
WbemConnectOptionsEnum = Int32
wbemConnectFlagUseMaxWait: win32more.Windows.Win32.System.Wmi.WbemConnectOptionsEnum = 128
WbemContext = Guid('{674b6698-ee92-11d0-ad71-00c04fd8fdff}')
WbemDCOMTransport = Guid('{f7ce2e13-8c90-11d1-9e7b-00c04fc324a8}')
WbemDecoupledBasicEventProvider = Guid('{f5f75737-2843-4f22-933d-c76a97cda62f}')
WbemDecoupledRegistrar = Guid('{4cfc7932-0f9d-4bef-9c32-8ea2a6b56fcb}')
WbemDefPath = Guid('{cf4cc405-e2c5-4ddd-b3ce-5e7582d8c9fa}')
WbemErrorEnum = Int32
wbemNoErr: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = 0
wbemErrFailed: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217407
wbemErrNotFound: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217406
wbemErrAccessDenied: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217405
wbemErrProviderFailure: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217404
wbemErrTypeMismatch: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217403
wbemErrOutOfMemory: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217402
wbemErrInvalidContext: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217401
wbemErrInvalidParameter: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217400
wbemErrNotAvailable: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217399
wbemErrCriticalError: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217398
wbemErrInvalidStream: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217397
wbemErrNotSupported: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217396
wbemErrInvalidSuperclass: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217395
wbemErrInvalidNamespace: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217394
wbemErrInvalidObject: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217393
wbemErrInvalidClass: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217392
wbemErrProviderNotFound: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217391
wbemErrInvalidProviderRegistration: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217390
wbemErrProviderLoadFailure: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217389
wbemErrInitializationFailure: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217388
wbemErrTransportFailure: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217387
wbemErrInvalidOperation: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217386
wbemErrInvalidQuery: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217385
wbemErrInvalidQueryType: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217384
wbemErrAlreadyExists: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217383
wbemErrOverrideNotAllowed: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217382
wbemErrPropagatedQualifier: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217381
wbemErrPropagatedProperty: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217380
wbemErrUnexpected: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217379
wbemErrIllegalOperation: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217378
wbemErrCannotBeKey: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217377
wbemErrIncompleteClass: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217376
wbemErrInvalidSyntax: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217375
wbemErrNondecoratedObject: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217374
wbemErrReadOnly: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217373
wbemErrProviderNotCapable: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217372
wbemErrClassHasChildren: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217371
wbemErrClassHasInstances: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217370
wbemErrQueryNotImplemented: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217369
wbemErrIllegalNull: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217368
wbemErrInvalidQualifierType: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217367
wbemErrInvalidPropertyType: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217366
wbemErrValueOutOfRange: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217365
wbemErrCannotBeSingleton: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217364
wbemErrInvalidCimType: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217363
wbemErrInvalidMethod: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217362
wbemErrInvalidMethodParameters: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217361
wbemErrSystemProperty: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217360
wbemErrInvalidProperty: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217359
wbemErrCallCancelled: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217358
wbemErrShuttingDown: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217357
wbemErrPropagatedMethod: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217356
wbemErrUnsupportedParameter: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217355
wbemErrMissingParameter: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217354
wbemErrInvalidParameterId: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217353
wbemErrNonConsecutiveParameterIds: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217352
wbemErrParameterIdOnRetval: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217351
wbemErrInvalidObjectPath: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217350
wbemErrOutOfDiskSpace: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217349
wbemErrBufferTooSmall: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217348
wbemErrUnsupportedPutExtension: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217347
wbemErrUnknownObjectType: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217346
wbemErrUnknownPacketType: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217345
wbemErrMarshalVersionMismatch: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217344
wbemErrMarshalInvalidSignature: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217343
wbemErrInvalidQualifier: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217342
wbemErrInvalidDuplicateParameter: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217341
wbemErrTooMuchData: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217340
wbemErrServerTooBusy: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217339
wbemErrInvalidFlavor: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217338
wbemErrCircularReference: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217337
wbemErrUnsupportedClassUpdate: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217336
wbemErrCannotChangeKeyInheritance: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217335
wbemErrCannotChangeIndexInheritance: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217328
wbemErrTooManyProperties: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217327
wbemErrUpdateTypeMismatch: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217326
wbemErrUpdateOverrideNotAllowed: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217325
wbemErrUpdatePropagatedMethod: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217324
wbemErrMethodNotImplemented: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217323
wbemErrMethodDisabled: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217322
wbemErrRefresherBusy: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217321
wbemErrUnparsableQuery: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217320
wbemErrNotEventClass: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217319
wbemErrMissingGroupWithin: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217318
wbemErrMissingAggregationList: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217317
wbemErrPropertyNotAnObject: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217316
wbemErrAggregatingByObject: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217315
wbemErrUninterpretableProviderQuery: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217313
wbemErrBackupRestoreWinmgmtRunning: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217312
wbemErrQueueOverflow: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217311
wbemErrPrivilegeNotHeld: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217310
wbemErrInvalidOperator: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217309
wbemErrLocalCredentials: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217308
wbemErrCannotBeAbstract: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217307
wbemErrAmendedObject: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217306
wbemErrClientTooSlow: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217305
wbemErrNullSecurityDescriptor: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217304
wbemErrTimeout: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217303
wbemErrInvalidAssociation: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217302
wbemErrAmbiguousOperation: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217301
wbemErrQuotaViolation: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217300
wbemErrTransactionConflict: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217299
wbemErrForcedRollback: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217298
wbemErrUnsupportedLocale: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217297
wbemErrHandleOutOfDate: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217296
wbemErrConnectionFailed: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217295
wbemErrInvalidHandleRequest: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217294
wbemErrPropertyNameTooWide: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217293
wbemErrClassNameTooWide: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217292
wbemErrMethodNameTooWide: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217291
wbemErrQualifierNameTooWide: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217290
wbemErrRerunCommand: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217289
wbemErrDatabaseVerMismatch: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217288
wbemErrVetoPut: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217287
wbemErrVetoDelete: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217286
wbemErrInvalidLocale: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217280
wbemErrProviderSuspended: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217279
wbemErrSynchronizationRequired: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217278
wbemErrNoSchema: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217277
wbemErrProviderAlreadyRegistered: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217276
wbemErrProviderNotRegistered: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217275
wbemErrFatalTransportError: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217274
wbemErrEncryptedConnectionRequired: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147217273
wbemErrRegistrationTooBroad: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147213311
wbemErrRegistrationTooPrecise: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147213310
wbemErrTimedout: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147209215
wbemErrResetToDefault: win32more.Windows.Win32.System.Wmi.WbemErrorEnum = -2147209214
WbemFlagEnum = Int32
wbemFlagReturnImmediately: win32more.Windows.Win32.System.Wmi.WbemFlagEnum = 16
wbemFlagReturnWhenComplete: win32more.Windows.Win32.System.Wmi.WbemFlagEnum = 0
wbemFlagBidirectional: win32more.Windows.Win32.System.Wmi.WbemFlagEnum = 0
wbemFlagForwardOnly: win32more.Windows.Win32.System.Wmi.WbemFlagEnum = 32
wbemFlagNoErrorObject: win32more.Windows.Win32.System.Wmi.WbemFlagEnum = 64
wbemFlagReturnErrorObject: win32more.Windows.Win32.System.Wmi.WbemFlagEnum = 0
wbemFlagSendStatus: win32more.Windows.Win32.System.Wmi.WbemFlagEnum = 128
wbemFlagDontSendStatus: win32more.Windows.Win32.System.Wmi.WbemFlagEnum = 0
wbemFlagEnsureLocatable: win32more.Windows.Win32.System.Wmi.WbemFlagEnum = 256
wbemFlagDirectRead: win32more.Windows.Win32.System.Wmi.WbemFlagEnum = 512
wbemFlagSendOnlySelected: win32more.Windows.Win32.System.Wmi.WbemFlagEnum = 0
wbemFlagUseAmendedQualifiers: win32more.Windows.Win32.System.Wmi.WbemFlagEnum = 131072
wbemFlagGetDefault: win32more.Windows.Win32.System.Wmi.WbemFlagEnum = 0
wbemFlagSpawnInstance: win32more.Windows.Win32.System.Wmi.WbemFlagEnum = 1
wbemFlagUseCurrentTime: win32more.Windows.Win32.System.Wmi.WbemFlagEnum = 1
WbemImpersonationLevelEnum = Int32
wbemImpersonationLevelAnonymous: win32more.Windows.Win32.System.Wmi.WbemImpersonationLevelEnum = 1
wbemImpersonationLevelIdentify: win32more.Windows.Win32.System.Wmi.WbemImpersonationLevelEnum = 2
wbemImpersonationLevelImpersonate: win32more.Windows.Win32.System.Wmi.WbemImpersonationLevelEnum = 3
wbemImpersonationLevelDelegate: win32more.Windows.Win32.System.Wmi.WbemImpersonationLevelEnum = 4
WbemLevel1Login = Guid('{8bc3f05e-d86b-11d0-a075-00c04fb68820}')
WbemLocalAddrRes = Guid('{a1044801-8f7e-11d1-9e7c-00c04fc324a8}')
WbemLocator = Guid('{4590f811-1d3a-11d0-891f-00aa004b2e24}')
WbemObjectTextFormatEnum = Int32
wbemObjectTextFormatCIMDTD20: win32more.Windows.Win32.System.Wmi.WbemObjectTextFormatEnum = 1
wbemObjectTextFormatWMIDTD20: win32more.Windows.Win32.System.Wmi.WbemObjectTextFormatEnum = 2
WbemObjectTextSrc = Guid('{8d1c559d-84f0-4bb3-a7d5-56a7435a9ba6}')
WbemPrivilegeEnum = Int32
wbemPrivilegeCreateToken: win32more.Windows.Win32.System.Wmi.WbemPrivilegeEnum = 1
wbemPrivilegePrimaryToken: win32more.Windows.Win32.System.Wmi.WbemPrivilegeEnum = 2
wbemPrivilegeLockMemory: win32more.Windows.Win32.System.Wmi.WbemPrivilegeEnum = 3
wbemPrivilegeIncreaseQuota: win32more.Windows.Win32.System.Wmi.WbemPrivilegeEnum = 4
wbemPrivilegeMachineAccount: win32more.Windows.Win32.System.Wmi.WbemPrivilegeEnum = 5
wbemPrivilegeTcb: win32more.Windows.Win32.System.Wmi.WbemPrivilegeEnum = 6
wbemPrivilegeSecurity: win32more.Windows.Win32.System.Wmi.WbemPrivilegeEnum = 7
wbemPrivilegeTakeOwnership: win32more.Windows.Win32.System.Wmi.WbemPrivilegeEnum = 8
wbemPrivilegeLoadDriver: win32more.Windows.Win32.System.Wmi.WbemPrivilegeEnum = 9
wbemPrivilegeSystemProfile: win32more.Windows.Win32.System.Wmi.WbemPrivilegeEnum = 10
wbemPrivilegeSystemtime: win32more.Windows.Win32.System.Wmi.WbemPrivilegeEnum = 11
wbemPrivilegeProfileSingleProcess: win32more.Windows.Win32.System.Wmi.WbemPrivilegeEnum = 12
wbemPrivilegeIncreaseBasePriority: win32more.Windows.Win32.System.Wmi.WbemPrivilegeEnum = 13
wbemPrivilegeCreatePagefile: win32more.Windows.Win32.System.Wmi.WbemPrivilegeEnum = 14
wbemPrivilegeCreatePermanent: win32more.Windows.Win32.System.Wmi.WbemPrivilegeEnum = 15
wbemPrivilegeBackup: win32more.Windows.Win32.System.Wmi.WbemPrivilegeEnum = 16
wbemPrivilegeRestore: win32more.Windows.Win32.System.Wmi.WbemPrivilegeEnum = 17
wbemPrivilegeShutdown: win32more.Windows.Win32.System.Wmi.WbemPrivilegeEnum = 18
wbemPrivilegeDebug: win32more.Windows.Win32.System.Wmi.WbemPrivilegeEnum = 19
wbemPrivilegeAudit: win32more.Windows.Win32.System.Wmi.WbemPrivilegeEnum = 20
wbemPrivilegeSystemEnvironment: win32more.Windows.Win32.System.Wmi.WbemPrivilegeEnum = 21
wbemPrivilegeChangeNotify: win32more.Windows.Win32.System.Wmi.WbemPrivilegeEnum = 22
wbemPrivilegeRemoteShutdown: win32more.Windows.Win32.System.Wmi.WbemPrivilegeEnum = 23
wbemPrivilegeUndock: win32more.Windows.Win32.System.Wmi.WbemPrivilegeEnum = 24
wbemPrivilegeSyncAgent: win32more.Windows.Win32.System.Wmi.WbemPrivilegeEnum = 25
wbemPrivilegeEnableDelegation: win32more.Windows.Win32.System.Wmi.WbemPrivilegeEnum = 26
wbemPrivilegeManageVolume: win32more.Windows.Win32.System.Wmi.WbemPrivilegeEnum = 27
WbemQuery = Guid('{eac8a024-21e2-4523-ad73-a71a0aa2f56a}')
WbemQueryFlagEnum = Int32
wbemQueryFlagDeep: win32more.Windows.Win32.System.Wmi.WbemQueryFlagEnum = 0
wbemQueryFlagShallow: win32more.Windows.Win32.System.Wmi.WbemQueryFlagEnum = 1
wbemQueryFlagPrototype: win32more.Windows.Win32.System.Wmi.WbemQueryFlagEnum = 2
WbemRefresher = Guid('{c71566f2-561e-11d1-ad87-00c04fd8fdff}')
WbemStatusCodeText = Guid('{eb87e1bd-3233-11d2-aec9-00c04fb68820}')
WbemTextFlagEnum = Int32
wbemTextFlagNoFlavors: win32more.Windows.Win32.System.Wmi.WbemTextFlagEnum = 1
WbemTimeout = Int32
wbemTimeoutInfinite: win32more.Windows.Win32.System.Wmi.WbemTimeout = -1
WbemUnauthenticatedLocator = Guid('{443e7b79-de31-11d2-b340-00104bcc4b4a}')
WbemUninitializedClassObject = Guid('{7a0227f6-7108-11d1-ad90-00c04fd8fdff}')


make_ready(__name__)
