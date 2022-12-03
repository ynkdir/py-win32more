from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Com
import win32more.System.Com.Marshal
import win32more.System.WinRT
import win32more.UI.Shell.PropertiesSystem
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
def _define__RO_REGISTRATION_COOKIE_head():
    class _RO_REGISTRATION_COOKIE(Structure):
        pass
    return _RO_REGISTRATION_COOKIE
def _define__RO_REGISTRATION_COOKIE():
    _RO_REGISTRATION_COOKIE = win32more.System.WinRT._RO_REGISTRATION_COOKIE_head
    return _RO_REGISTRATION_COOKIE
ACTIVATIONTYPE = Int32
ACTIVATIONTYPE_UNCATEGORIZED = 0
ACTIVATIONTYPE_FROM_MONIKER = 1
ACTIVATIONTYPE_FROM_DATA = 2
ACTIVATIONTYPE_FROM_STORAGE = 4
ACTIVATIONTYPE_FROM_STREAM = 8
ACTIVATIONTYPE_FROM_FILE = 16
AgileReferenceOptions = Int32
AGILEREFERENCE_DEFAULT = 0
AGILEREFERENCE_DELAYEDMARSHAL = 1
APARTMENT_SHUTDOWN_REGISTRATION_COOKIE = IntPtr
MAX_ERROR_MESSAGE_CHARS = 512
CastingSourceInfo_Property_PreferredSourceUriScheme = 'PreferredSourceUriScheme'
CastingSourceInfo_Property_CastingTypes = 'CastingTypes'
CastingSourceInfo_Property_ProtectedMedia = 'ProtectedMedia'
def _define_CoDecodeProxy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt64,POINTER(win32more.System.WinRT.ServerInformation_head))(('CoDecodeProxy', windll['OLE32.dll']), ((1, 'dwClientPid'),(1, 'ui64ProxyAddress'),(1, 'pServerInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoGetAgileReference():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.AgileReferenceOptions,POINTER(Guid),win32more.System.Com.IUnknown_head,POINTER(win32more.System.WinRT.IAgileReference_head))(('RoGetAgileReference', windll['OLE32.dll']), ((1, 'options'),(1, 'riid'),(1, 'pUnk'),(1, 'ppAgileReference'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HSTRING_UserSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.System.WinRT.HSTRING))(('HSTRING_UserSize', windll['api-ms-win-core-winrt-string-l1-1-0.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HSTRING_UserMarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.System.WinRT.HSTRING))(('HSTRING_UserMarshal', windll['api-ms-win-core-winrt-string-l1-1-0.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HSTRING_UserUnmarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.System.WinRT.HSTRING))(('HSTRING_UserUnmarshal', windll['api-ms-win-core-winrt-string-l1-1-0.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HSTRING_UserFree():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.System.WinRT.HSTRING))(('HSTRING_UserFree', windll['api-ms-win-core-winrt-string-l1-1-0.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HSTRING_UserSize64():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.System.WinRT.HSTRING))(('HSTRING_UserSize64', windll['api-ms-win-core-winrt-string-l1-1-0.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HSTRING_UserMarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.System.WinRT.HSTRING))(('HSTRING_UserMarshal64', windll['api-ms-win-core-winrt-string-l1-1-0.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HSTRING_UserUnmarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.System.WinRT.HSTRING))(('HSTRING_UserUnmarshal64', windll['api-ms-win-core-winrt-string-l1-1-0.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HSTRING_UserFree64():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.System.WinRT.HSTRING))(('HSTRING_UserFree64', windll['api-ms-win-core-winrt-string-l1-1-0.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WindowsCreateString():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.System.WinRT.HSTRING))(('WindowsCreateString', windll['api-ms-win-core-winrt-string-l1-1-0.dll']), ((1, 'sourceString'),(1, 'length'),(1, 'string'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WindowsCreateStringReference():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.System.WinRT.HSTRING_HEADER_head),POINTER(win32more.System.WinRT.HSTRING))(('WindowsCreateStringReference', windll['api-ms-win-core-winrt-string-l1-1-0.dll']), ((1, 'sourceString'),(1, 'length'),(1, 'hstringHeader'),(1, 'string'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WindowsDeleteString():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.HSTRING)(('WindowsDeleteString', windll['api-ms-win-core-winrt-string-l1-1-0.dll']), ((1, 'string'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WindowsDuplicateString():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.HSTRING,POINTER(win32more.System.WinRT.HSTRING))(('WindowsDuplicateString', windll['api-ms-win-core-winrt-string-l1-1-0.dll']), ((1, 'string'),(1, 'newString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WindowsGetStringLen():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.WinRT.HSTRING)(('WindowsGetStringLen', windll['api-ms-win-core-winrt-string-l1-1-0.dll']), ((1, 'string'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WindowsGetStringRawBuffer():
    try:
        return WINFUNCTYPE(win32more.Foundation.PWSTR,win32more.System.WinRT.HSTRING,POINTER(UInt32))(('WindowsGetStringRawBuffer', windll['api-ms-win-core-winrt-string-l1-1-0.dll']), ((1, 'string'),(1, 'length'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WindowsIsStringEmpty():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.WinRT.HSTRING)(('WindowsIsStringEmpty', windll['api-ms-win-core-winrt-string-l1-1-0.dll']), ((1, 'string'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WindowsStringHasEmbeddedNull():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.HSTRING,POINTER(win32more.Foundation.BOOL))(('WindowsStringHasEmbeddedNull', windll['api-ms-win-core-winrt-string-l1-1-0.dll']), ((1, 'string'),(1, 'hasEmbedNull'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WindowsCompareStringOrdinal():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,POINTER(Int32))(('WindowsCompareStringOrdinal', windll['api-ms-win-core-winrt-string-l1-1-0.dll']), ((1, 'string1'),(1, 'string2'),(1, 'result'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WindowsSubstring():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.HSTRING,UInt32,POINTER(win32more.System.WinRT.HSTRING))(('WindowsSubstring', windll['api-ms-win-core-winrt-string-l1-1-0.dll']), ((1, 'string'),(1, 'startIndex'),(1, 'newString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WindowsSubstringWithSpecifiedLength():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.HSTRING,UInt32,UInt32,POINTER(win32more.System.WinRT.HSTRING))(('WindowsSubstringWithSpecifiedLength', windll['api-ms-win-core-winrt-string-l1-1-0.dll']), ((1, 'string'),(1, 'startIndex'),(1, 'length'),(1, 'newString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WindowsConcatString():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,POINTER(win32more.System.WinRT.HSTRING))(('WindowsConcatString', windll['api-ms-win-core-winrt-string-l1-1-0.dll']), ((1, 'string1'),(1, 'string2'),(1, 'newString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WindowsReplaceString():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,POINTER(win32more.System.WinRT.HSTRING))(('WindowsReplaceString', windll['api-ms-win-core-winrt-string-l1-1-0.dll']), ((1, 'string'),(1, 'stringReplaced'),(1, 'stringReplaceWith'),(1, 'newString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WindowsTrimStringStart():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,POINTER(win32more.System.WinRT.HSTRING))(('WindowsTrimStringStart', windll['api-ms-win-core-winrt-string-l1-1-0.dll']), ((1, 'string'),(1, 'trimString'),(1, 'newString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WindowsTrimStringEnd():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.HSTRING,win32more.System.WinRT.HSTRING,POINTER(win32more.System.WinRT.HSTRING))(('WindowsTrimStringEnd', windll['api-ms-win-core-winrt-string-l1-1-0.dll']), ((1, 'string'),(1, 'trimString'),(1, 'newString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WindowsPreallocateStringBuffer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(UInt16)),POINTER(win32more.System.WinRT.HSTRING_BUFFER))(('WindowsPreallocateStringBuffer', windll['api-ms-win-core-winrt-string-l1-1-0.dll']), ((1, 'length'),(1, 'charBuffer'),(1, 'bufferHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WindowsPromoteStringBuffer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.HSTRING_BUFFER,POINTER(win32more.System.WinRT.HSTRING))(('WindowsPromoteStringBuffer', windll['api-ms-win-core-winrt-string-l1-1-0.dll']), ((1, 'bufferHandle'),(1, 'string'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WindowsDeleteStringBuffer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.HSTRING_BUFFER)(('WindowsDeleteStringBuffer', windll['api-ms-win-core-winrt-string-l1-1-0.dll']), ((1, 'bufferHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WindowsInspectString():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr,UInt16,win32more.System.WinRT.PINSPECT_HSTRING_CALLBACK,c_void_p,POINTER(UInt32),POINTER(UIntPtr))(('WindowsInspectString', windll['api-ms-win-core-winrt-string-l1-1-0.dll']), ((1, 'targetHString'),(1, 'machine'),(1, 'callback'),(1, 'context'),(1, 'length'),(1, 'targetStringAddress'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WindowsInspectString2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,UInt16,win32more.System.WinRT.PINSPECT_HSTRING_CALLBACK2,c_void_p,POINTER(UInt32),POINTER(UInt64))(('WindowsInspectString2', windll['api-ms-win-core-winrt-string-l1-1-1.dll']), ((1, 'targetHString'),(1, 'machine'),(1, 'callback'),(1, 'context'),(1, 'length'),(1, 'targetStringAddress'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateDispatcherQueueController():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.DispatcherQueueOptions,POINTER(MissingType))(('CreateDispatcherQueueController', windll['CoreMessaging.dll']), ((1, 'options'),(1, 'dispatcherQueueController'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoInitialize():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.RO_INIT_TYPE)(('RoInitialize', windll['api-ms-win-core-winrt-l1-1-0.dll']), ((1, 'initType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoUninitialize():
    try:
        return WINFUNCTYPE(Void,)(('RoUninitialize', windll['api-ms-win-core-winrt-l1-1-0.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoActivateInstance():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.HSTRING,POINTER(win32more.System.WinRT.IInspectable_head))(('RoActivateInstance', windll['api-ms-win-core-winrt-l1-1-0.dll']), ((1, 'activatableClassId'),(1, 'instance'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoRegisterActivationFactories():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WinRT.HSTRING),POINTER(IntPtr),UInt32,POINTER(IntPtr))(('RoRegisterActivationFactories', windll['api-ms-win-core-winrt-l1-1-0.dll']), ((1, 'activatableClassIds'),(1, 'activationFactoryCallbacks'),(1, 'count'),(1, 'cookie'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoRevokeActivationFactories():
    try:
        return WINFUNCTYPE(Void,IntPtr)(('RoRevokeActivationFactories', windll['api-ms-win-core-winrt-l1-1-0.dll']), ((1, 'cookie'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoGetActivationFactory():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.HSTRING,POINTER(Guid),POINTER(c_void_p))(('RoGetActivationFactory', windll['api-ms-win-core-winrt-l1-1-0.dll']), ((1, 'activatableClassId'),(1, 'iid'),(1, 'factory'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoRegisterForApartmentShutdown():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.IApartmentShutdown_head,POINTER(UInt64),POINTER(win32more.System.WinRT.APARTMENT_SHUTDOWN_REGISTRATION_COOKIE))(('RoRegisterForApartmentShutdown', windll['api-ms-win-core-winrt-l1-1-0.dll']), ((1, 'callbackObject'),(1, 'apartmentIdentifier'),(1, 'regCookie'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoUnregisterForApartmentShutdown():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.APARTMENT_SHUTDOWN_REGISTRATION_COOKIE)(('RoUnregisterForApartmentShutdown', windll['api-ms-win-core-winrt-l1-1-0.dll']), ((1, 'regCookie'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoGetApartmentIdentifier():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64))(('RoGetApartmentIdentifier', windll['api-ms-win-core-winrt-l1-1-0.dll']), ((1, 'apartmentIdentifier'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoGetBufferMarshaler():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.Marshal.IMarshal_head))(('RoGetBufferMarshaler', windll['api-ms-win-core-winrt-robuffer-l1-1-0.dll']), ((1, 'bufferMarshaler'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoGetErrorReportingFlags():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(('RoGetErrorReportingFlags', windll['api-ms-win-core-winrt-error-l1-1-0.dll']), ((1, 'pflags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoSetErrorReportingFlags():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(('RoSetErrorReportingFlags', windll['api-ms-win-core-winrt-error-l1-1-0.dll']), ((1, 'flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoResolveRestrictedErrorInfoReference():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.WinRT.IRestrictedErrorInfo_head))(('RoResolveRestrictedErrorInfoReference', windll['api-ms-win-core-winrt-error-l1-1-0.dll']), ((1, 'reference'),(1, 'ppRestrictedErrorInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetRestrictedErrorInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.IRestrictedErrorInfo_head)(('SetRestrictedErrorInfo', windll['api-ms-win-core-winrt-error-l1-1-0.dll']), ((1, 'pRestrictedErrorInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetRestrictedErrorInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WinRT.IRestrictedErrorInfo_head))(('GetRestrictedErrorInfo', windll['api-ms-win-core-winrt-error-l1-1-0.dll']), ((1, 'ppRestrictedErrorInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoOriginateErrorW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR)(('RoOriginateErrorW', windll['api-ms-win-core-winrt-error-l1-1-0.dll']), ((1, 'error'),(1, 'cchMax'),(1, 'message'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoOriginateError():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HRESULT,win32more.System.WinRT.HSTRING)(('RoOriginateError', windll['api-ms-win-core-winrt-error-l1-1-0.dll']), ((1, 'error'),(1, 'message'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoTransformErrorW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR)(('RoTransformErrorW', windll['api-ms-win-core-winrt-error-l1-1-0.dll']), ((1, 'oldError'),(1, 'newError'),(1, 'cchMax'),(1, 'message'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoTransformError():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,win32more.System.WinRT.HSTRING)(('RoTransformError', windll['api-ms-win-core-winrt-error-l1-1-0.dll']), ((1, 'oldError'),(1, 'newError'),(1, 'message'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoCaptureErrorContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT)(('RoCaptureErrorContext', windll['api-ms-win-core-winrt-error-l1-1-0.dll']), ((1, 'hr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoFailFastWithErrorContext():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.HRESULT)(('RoFailFastWithErrorContext', windll['api-ms-win-core-winrt-error-l1-1-0.dll']), ((1, 'hrError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoOriginateLanguageException():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HRESULT,win32more.System.WinRT.HSTRING,win32more.System.Com.IUnknown_head)(('RoOriginateLanguageException', windll['api-ms-win-core-winrt-error-l1-1-1.dll']), ((1, 'error'),(1, 'message'),(1, 'languageException'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoClearError():
    try:
        return WINFUNCTYPE(Void,)(('RoClearError', windll['api-ms-win-core-winrt-error-l1-1-1.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoReportUnhandledError():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.IRestrictedErrorInfo_head)(('RoReportUnhandledError', windll['api-ms-win-core-winrt-error-l1-1-1.dll']), ((1, 'pRestrictedErrorInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoInspectThreadErrorInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr,UInt16,win32more.System.WinRT.PINSPECT_MEMORY_CALLBACK,c_void_p,POINTER(UIntPtr))(('RoInspectThreadErrorInfo', windll['api-ms-win-core-winrt-error-l1-1-1.dll']), ((1, 'targetTebAddress'),(1, 'machine'),(1, 'readMemoryCallback'),(1, 'context'),(1, 'targetErrorInfoAddress'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoInspectCapturedStackBackTrace():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr,UInt16,win32more.System.WinRT.PINSPECT_MEMORY_CALLBACK,c_void_p,POINTER(UInt32),POINTER(UIntPtr))(('RoInspectCapturedStackBackTrace', windll['api-ms-win-core-winrt-error-l1-1-1.dll']), ((1, 'targetErrorInfoAddress'),(1, 'machine'),(1, 'readMemoryCallback'),(1, 'context'),(1, 'frameCount'),(1, 'targetBackTraceAddress'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoGetMatchingRestrictedErrorInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,POINTER(win32more.System.WinRT.IRestrictedErrorInfo_head))(('RoGetMatchingRestrictedErrorInfo', windll['api-ms-win-core-winrt-error-l1-1-1.dll']), ((1, 'hrIn'),(1, 'ppRestrictedErrorInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoReportFailedDelegate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.System.WinRT.IRestrictedErrorInfo_head)(('RoReportFailedDelegate', windll['api-ms-win-core-winrt-error-l1-1-1.dll']), ((1, 'punkDelegate'),(1, 'pRestrictedErrorInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsErrorPropagationEnabled():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,)(('IsErrorPropagationEnabled', windll['api-ms-win-core-winrt-error-l1-1-1.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_MetaDataGetDispenser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),POINTER(c_void_p))(('MetaDataGetDispenser', windll['RoMetadata.dll']), ((1, 'rclsid'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoGetParameterizedTypeInstanceIID():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.PWSTR),win32more.System.WinRT.IRoMetaDataLocator_head,POINTER(Guid),POINTER(win32more.System.WinRT.ROPARAMIIDHANDLE))(('RoGetParameterizedTypeInstanceIID', windll['api-ms-win-core-winrt-roparameterizediid-l1-1-0.dll']), ((1, 'nameElementCount'),(1, 'nameElements'),(1, 'metaDataLocator'),(1, 'iid'),(1, 'pExtra'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoFreeParameterizedTypeExtra():
    try:
        return WINFUNCTYPE(Void,win32more.System.WinRT.ROPARAMIIDHANDLE)(('RoFreeParameterizedTypeExtra', windll['api-ms-win-core-winrt-roparameterizediid-l1-1-0.dll']), ((1, 'extra'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoParameterizedTypeExtraGetTypeSignature():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.System.WinRT.ROPARAMIIDHANDLE)(('RoParameterizedTypeExtraGetTypeSignature', windll['api-ms-win-core-winrt-roparameterizediid-l1-1-0.dll']), ((1, 'extra'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoGetServerActivatableClasses():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.HSTRING,POINTER(POINTER(win32more.System.WinRT.HSTRING)),POINTER(UInt32))(('RoGetServerActivatableClasses', windll['api-ms-win-core-winrt-registration-l1-1-0.dll']), ((1, 'serverName'),(1, 'activatableClassIds'),(1, 'count'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateRandomAccessStreamOnFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(Guid),POINTER(c_void_p))(('CreateRandomAccessStreamOnFile', windll['api-ms-win-shcore-stream-winrt-l1-1-0.dll']), ((1, 'filePath'),(1, 'accessMode'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateRandomAccessStreamOverStream():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.System.WinRT.BSOS_OPTIONS,POINTER(Guid),POINTER(c_void_p))(('CreateRandomAccessStreamOverStream', windll['api-ms-win-shcore-stream-winrt-l1-1-0.dll']), ((1, 'stream'),(1, 'options'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateStreamOverRandomAccessStream():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(Guid),POINTER(c_void_p))(('CreateStreamOverRandomAccessStream', windll['api-ms-win-shcore-stream-winrt-l1-1-0.dll']), ((1, 'randomAccessStream'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateControlInput():
    try:
        return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p))(('CreateControlInput', cdll['Windows.UI.dll']), ((1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateControlInputEx():
    try:
        return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(Guid),POINTER(c_void_p))(('CreateControlInputEx', cdll['Windows.UI.dll']), ((1, 'pCoreWindow'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
BSOS_OPTIONS = Int32
BSOS_DEFAULT = 0
BSOS_PREFERDESTINATIONSTREAM = 1
CASTING_CONNECTION_ERROR_STATUS = Int32
CASTING_CONNECTION_ERROR_STATUS_SUCCEEDED = 0
CASTING_CONNECTION_ERROR_STATUS_DEVICE_DID_NOT_RESPOND = 1
CASTING_CONNECTION_ERROR_STATUS_DEVICE_ERROR = 2
CASTING_CONNECTION_ERROR_STATUS_DEVICE_LOCKED = 3
CASTING_CONNECTION_ERROR_STATUS_PROTECTED_PLAYBACK_FAILED = 4
CASTING_CONNECTION_ERROR_STATUS_INVALID_CASTING_SOURCE = 5
CASTING_CONNECTION_ERROR_STATUS_UNKNOWN = 6
CASTING_CONNECTION_STATE = Int32
CASTING_CONNECTION_STATE_DISCONNECTED = 0
CASTING_CONNECTION_STATE_CONNECTED = 1
CASTING_CONNECTION_STATE_RENDERING = 2
CASTING_CONNECTION_STATE_DISCONNECTING = 3
CASTING_CONNECTION_STATE_CONNECTING = 4
DISPATCHERQUEUE_THREAD_APARTMENTTYPE = Int32
DQTAT_COM_NONE = 0
DQTAT_COM_ASTA = 1
DQTAT_COM_STA = 2
DISPATCHERQUEUE_THREAD_TYPE = Int32
DQTYPE_THREAD_DEDICATED = 1
DQTYPE_THREAD_CURRENT = 2
def _define_DispatcherQueueOptions_head():
    class DispatcherQueueOptions(Structure):
        pass
    return DispatcherQueueOptions
def _define_DispatcherQueueOptions():
    DispatcherQueueOptions = win32more.System.WinRT.DispatcherQueueOptions_head
    DispatcherQueueOptions._fields_ = [
        ('dwSize', UInt32),
        ('threadType', win32more.System.WinRT.DISPATCHERQUEUE_THREAD_TYPE),
        ('apartmentType', win32more.System.WinRT.DISPATCHERQUEUE_THREAD_APARTMENTTYPE),
    ]
    return DispatcherQueueOptions
def _define_EventRegistrationToken_head():
    class EventRegistrationToken(Structure):
        pass
    return EventRegistrationToken
def _define_EventRegistrationToken():
    EventRegistrationToken = win32more.System.WinRT.EventRegistrationToken_head
    EventRegistrationToken._fields_ = [
        ('value', Int64),
    ]
    return EventRegistrationToken
HSTRING = IntPtr
HSTRING_BUFFER = IntPtr
def _define_HSTRING_HEADER_head():
    class HSTRING_HEADER(Structure):
        pass
    return HSTRING_HEADER
def _define_HSTRING_HEADER():
    HSTRING_HEADER = win32more.System.WinRT.HSTRING_HEADER_head
    HSTRING_HEADER._fields_ = [
        ('flags', UInt32),
        ('length', UInt32),
        ('padding1', UInt32),
        ('padding2', UInt32),
        ('data', IntPtr),
    ]
    return HSTRING_HEADER
def _define_IAccountsSettingsPaneInterop_head():
    class IAccountsSettingsPaneInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('d3ee12ad-3865-4362-97-46-b7-5a-68-2d-f0-e6')
    return IAccountsSettingsPaneInterop
def _define_IAccountsSettingsPaneInterop():
    IAccountsSettingsPaneInterop = win32more.System.WinRT.IAccountsSettingsPaneInterop_head
    IAccountsSettingsPaneInterop.GetForWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p))(6, 'GetForWindow', ((1, 'appWindow'),(1, 'riid'),(1, 'accountsSettingsPane'),)))
    IAccountsSettingsPaneInterop.ShowManageAccountsForWindowAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p))(7, 'ShowManageAccountsForWindowAsync', ((1, 'appWindow'),(1, 'riid'),(1, 'asyncAction'),)))
    IAccountsSettingsPaneInterop.ShowAddAccountForWindowAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p))(8, 'ShowAddAccountForWindowAsync', ((1, 'appWindow'),(1, 'riid'),(1, 'asyncAction'),)))
    win32more.System.WinRT.IInspectable
    return IAccountsSettingsPaneInterop
def _define_IActivationFactory_head():
    class IActivationFactory(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('00000035-0000-0000-c0-00-00-00-00-00-00-46')
    return IActivationFactory
def _define_IActivationFactory():
    IActivationFactory = win32more.System.WinRT.IActivationFactory_head
    IActivationFactory.ActivateInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WinRT.IInspectable_head))(6, 'ActivateInstance', ((1, 'instance'),)))
    win32more.System.WinRT.IInspectable
    return IActivationFactory
def _define_IAgileReference_head():
    class IAgileReference(win32more.System.Com.IUnknown_head):
        Guid = Guid('c03f6a43-65a4-9818-98-7e-e0-b8-10-d2-a6-f2')
    return IAgileReference
def _define_IAgileReference():
    IAgileReference = win32more.System.WinRT.IAgileReference_head
    IAgileReference.Resolve = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p))(3, 'Resolve', ((1, 'riid'),(1, 'ppvObjectReference'),)))
    win32more.System.Com.IUnknown
    return IAgileReference
def _define_IApartmentShutdown_head():
    class IApartmentShutdown(win32more.System.Com.IUnknown_head):
        Guid = Guid('a2f05a09-27a2-42b5-bc-0e-ac-16-3e-f4-9d-9b')
    return IApartmentShutdown
def _define_IApartmentShutdown():
    IApartmentShutdown = win32more.System.WinRT.IApartmentShutdown_head
    IApartmentShutdown.OnUninitialize = COMMETHOD(WINFUNCTYPE(Void,UInt64)(3, 'OnUninitialize', ((1, 'ui64ApartmentIdentifier'),)))
    win32more.System.Com.IUnknown
    return IApartmentShutdown
def _define_IAppServiceConnectionExtendedExecution_head():
    class IAppServiceConnectionExtendedExecution(win32more.System.Com.IUnknown_head):
        Guid = Guid('65219584-f9cb-4ae3-81-f9-a2-8a-6c-a4-50-d9')
    return IAppServiceConnectionExtendedExecution
def _define_IAppServiceConnectionExtendedExecution():
    IAppServiceConnectionExtendedExecution = win32more.System.WinRT.IAppServiceConnectionExtendedExecution_head
    IAppServiceConnectionExtendedExecution.OpenForExtendedExecutionAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p))(3, 'OpenForExtendedExecutionAsync', ((1, 'riid'),(1, 'operation'),)))
    win32more.System.Com.IUnknown
    return IAppServiceConnectionExtendedExecution
def _define_IBufferByteAccess_head():
    class IBufferByteAccess(win32more.System.Com.IUnknown_head):
        Guid = Guid('905a0fef-bc53-11df-8c-49-00-1e-4f-c6-86-da')
    return IBufferByteAccess
def _define_IBufferByteAccess():
    IBufferByteAccess = win32more.System.WinRT.IBufferByteAccess_head
    IBufferByteAccess.Buffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_char_p_no))(3, 'Buffer', ((1, 'value'),)))
    win32more.System.Com.IUnknown
    return IBufferByteAccess
def _define_ICastingController_head():
    class ICastingController(win32more.System.Com.IUnknown_head):
        Guid = Guid('f0a56423-a664-4fbd-8b-43-40-9a-45-e8-d9-a1')
    return ICastingController
def _define_ICastingController():
    ICastingController = win32more.System.WinRT.ICastingController_head
    ICastingController.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.System.Com.IUnknown_head)(3, 'Initialize', ((1, 'castingEngine'),(1, 'castingSource'),)))
    ICastingController.Connect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Connect', ()))
    ICastingController.Disconnect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Disconnect', ()))
    ICastingController.Advise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.ICastingEventHandler_head,POINTER(UInt32))(6, 'Advise', ((1, 'eventHandler'),(1, 'cookie'),)))
    ICastingController.UnAdvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(7, 'UnAdvise', ((1, 'cookie'),)))
    win32more.System.Com.IUnknown
    return ICastingController
def _define_ICastingEventHandler_head():
    class ICastingEventHandler(win32more.System.Com.IUnknown_head):
        Guid = Guid('c79a6cb7-bebd-47a6-a2-ad-4d-45-ad-79-c7-bc')
    return ICastingEventHandler
def _define_ICastingEventHandler():
    ICastingEventHandler = win32more.System.WinRT.ICastingEventHandler_head
    ICastingEventHandler.OnStateChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.CASTING_CONNECTION_STATE)(3, 'OnStateChanged', ((1, 'newState'),)))
    ICastingEventHandler.OnError = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.CASTING_CONNECTION_ERROR_STATUS,win32more.Foundation.PWSTR)(4, 'OnError', ((1, 'errorStatus'),(1, 'errorMessage'),)))
    win32more.System.Com.IUnknown
    return ICastingEventHandler
def _define_ICastingSourceInfo_head():
    class ICastingSourceInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('45101ab7-7c3a-4bce-95-00-12-c0-90-24-b2-98')
    return ICastingSourceInfo
def _define_ICastingSourceInfo():
    ICastingSourceInfo = win32more.System.WinRT.ICastingSourceInfo_head
    ICastingSourceInfo.GetController = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WinRT.ICastingController_head))(3, 'GetController', ((1, 'controller'),)))
    ICastingSourceInfo.GetProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Shell.PropertiesSystem.INamedPropertyStore_head))(4, 'GetProperties', ((1, 'props'),)))
    win32more.System.Com.IUnknown
    return ICastingSourceInfo
def _define_ICoreInputInterop_head():
    class ICoreInputInterop(win32more.System.Com.IUnknown_head):
        Guid = Guid('40bfe3e3-b75a-4479-ac-96-47-53-65-74-9b-b8')
    return ICoreInputInterop
def _define_ICoreInputInterop():
    ICoreInputInterop = win32more.System.WinRT.ICoreInputInterop_head
    ICoreInputInterop.SetInputSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(3, 'SetInputSource', ((1, 'value'),)))
    ICoreInputInterop.put_MessageHandled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Byte)(4, 'put_MessageHandled', ((1, 'value'),)))
    win32more.System.Com.IUnknown
    return ICoreInputInterop
def _define_ICoreWindowAdapterInterop_head():
    class ICoreWindowAdapterInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('7a5b6fd1-cd73-4b6c-9c-f4-2e-86-9e-af-47-0a')
    return ICoreWindowAdapterInterop
def _define_ICoreWindowAdapterInterop():
    ICoreWindowAdapterInterop = win32more.System.WinRT.ICoreWindowAdapterInterop_head
    ICoreWindowAdapterInterop.get_AppActivationClientAdapter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(6, 'get_AppActivationClientAdapter', ((1, 'value'),)))
    ICoreWindowAdapterInterop.get_ApplicationViewClientAdapter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(7, 'get_ApplicationViewClientAdapter', ((1, 'value'),)))
    ICoreWindowAdapterInterop.get_CoreApplicationViewClientAdapter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(8, 'get_CoreApplicationViewClientAdapter', ((1, 'value'),)))
    ICoreWindowAdapterInterop.get_HoloViewClientAdapter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(9, 'get_HoloViewClientAdapter', ((1, 'value'),)))
    ICoreWindowAdapterInterop.get_PositionerClientAdapter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(10, 'get_PositionerClientAdapter', ((1, 'value'),)))
    ICoreWindowAdapterInterop.get_SystemNavigationClientAdapter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(11, 'get_SystemNavigationClientAdapter', ((1, 'value'),)))
    ICoreWindowAdapterInterop.get_TitleBarClientAdapter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(12, 'get_TitleBarClientAdapter', ((1, 'value'),)))
    ICoreWindowAdapterInterop.SetWindowClientAdapter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(13, 'SetWindowClientAdapter', ((1, 'value'),)))
    win32more.System.WinRT.IInspectable
    return ICoreWindowAdapterInterop
def _define_ICoreWindowComponentInterop_head():
    class ICoreWindowComponentInterop(win32more.System.Com.IUnknown_head):
        Guid = Guid('0576ab31-a310-4c40-ba-31-fd-37-e0-29-8d-fa')
    return ICoreWindowComponentInterop
def _define_ICoreWindowComponentInterop():
    ICoreWindowComponentInterop = win32more.System.WinRT.ICoreWindowComponentInterop_head
    ICoreWindowComponentInterop.ConfigureComponentInput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.HWND,win32more.System.Com.IUnknown_head)(3, 'ConfigureComponentInput', ((1, 'hostViewInstanceId'),(1, 'hwndHost'),(1, 'inputSourceVisual'),)))
    ICoreWindowComponentInterop.GetViewInstanceId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(4, 'GetViewInstanceId', ((1, 'componentViewInstanceId'),)))
    win32more.System.Com.IUnknown
    return ICoreWindowComponentInterop
def _define_ICoreWindowInterop_head():
    class ICoreWindowInterop(win32more.System.Com.IUnknown_head):
        Guid = Guid('45d64a29-a63e-4cb6-b4-98-57-81-d2-98-cb-4f')
    return ICoreWindowInterop
def _define_ICoreWindowInterop():
    ICoreWindowInterop = win32more.System.WinRT.ICoreWindowInterop_head
    ICoreWindowInterop.get_WindowHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HWND))(3, 'get_WindowHandle', ((1, 'hwnd'),)))
    ICoreWindowInterop.put_MessageHandled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Byte)(4, 'put_MessageHandled', ((1, 'value'),)))
    win32more.System.Com.IUnknown
    return ICoreWindowInterop
def _define_ICorrelationVectorInformation_head():
    class ICorrelationVectorInformation(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('83c78b3c-d88b-4950-aa-6e-22-b8-d2-2a-ab-d3')
    return ICorrelationVectorInformation
def _define_ICorrelationVectorInformation():
    ICorrelationVectorInformation = win32more.System.WinRT.ICorrelationVectorInformation_head
    ICorrelationVectorInformation.get_LastCorrelationVectorForThread = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WinRT.HSTRING))(6, 'get_LastCorrelationVectorForThread', ((1, 'cv'),)))
    ICorrelationVectorInformation.get_NextCorrelationVectorForThread = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WinRT.HSTRING))(7, 'get_NextCorrelationVectorForThread', ((1, 'cv'),)))
    ICorrelationVectorInformation.put_NextCorrelationVectorForThread = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.HSTRING)(8, 'put_NextCorrelationVectorForThread', ((1, 'cv'),)))
    win32more.System.WinRT.IInspectable
    return ICorrelationVectorInformation
def _define_ICorrelationVectorSource_head():
    class ICorrelationVectorSource(win32more.System.Com.IUnknown_head):
        Guid = Guid('152b8a3b-b9b9-4685-b5-6e-97-48-47-bc-75-45')
    return ICorrelationVectorSource
def _define_ICorrelationVectorSource():
    ICorrelationVectorSource = win32more.System.WinRT.ICorrelationVectorSource_head
    ICorrelationVectorSource.get_CorrelationVector = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WinRT.HSTRING))(3, 'get_CorrelationVector', ((1, 'cv'),)))
    win32more.System.Com.IUnknown
    return ICorrelationVectorSource
def _define_IDragDropManagerInterop_head():
    class IDragDropManagerInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('5ad8cba7-4c01-4dac-90-74-82-78-94-29-2d-63')
    return IDragDropManagerInterop
def _define_IDragDropManagerInterop():
    IDragDropManagerInterop = win32more.System.WinRT.IDragDropManagerInterop_head
    IDragDropManagerInterop.GetForWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p))(6, 'GetForWindow', ((1, 'hwnd'),(1, 'riid'),(1, 'ppv'),)))
    win32more.System.WinRT.IInspectable
    return IDragDropManagerInterop
def _define_IHolographicSpaceInterop_head():
    class IHolographicSpaceInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('5c4ee536-6a98-4b86-a1-70-58-70-13-d6-fd-4b')
    return IHolographicSpaceInterop
def _define_IHolographicSpaceInterop():
    IHolographicSpaceInterop = win32more.System.WinRT.IHolographicSpaceInterop_head
    IHolographicSpaceInterop.CreateForWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p))(6, 'CreateForWindow', ((1, 'window'),(1, 'riid'),(1, 'holographicSpace'),)))
    win32more.System.WinRT.IInspectable
    return IHolographicSpaceInterop
def _define_IInputPaneInterop_head():
    class IInputPaneInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('75cf2c57-9195-4931-83-32-f0-b4-09-e9-16-af')
    return IInputPaneInterop
def _define_IInputPaneInterop():
    IInputPaneInterop = win32more.System.WinRT.IInputPaneInterop_head
    IInputPaneInterop.GetForWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p))(6, 'GetForWindow', ((1, 'appWindow'),(1, 'riid'),(1, 'inputPane'),)))
    win32more.System.WinRT.IInspectable
    return IInputPaneInterop
def _define_IInspectable_head():
    class IInspectable(win32more.System.Com.IUnknown_head):
        Guid = Guid('af86e2e0-b12d-4c6a-9c-5a-d7-aa-65-10-1e-90')
    return IInspectable
def _define_IInspectable():
    IInspectable = win32more.System.WinRT.IInspectable_head
    IInspectable.GetIids = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(POINTER(Guid)))(3, 'GetIids', ((1, 'iidCount'),(1, 'iids'),)))
    IInspectable.GetRuntimeClassName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WinRT.HSTRING))(4, 'GetRuntimeClassName', ((1, 'className'),)))
    IInspectable.GetTrustLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WinRT.TrustLevel))(5, 'GetTrustLevel', ((1, 'trustLevel'),)))
    win32more.System.Com.IUnknown
    return IInspectable
def _define_ILanguageExceptionErrorInfo_head():
    class ILanguageExceptionErrorInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('04a2dbf3-df83-116c-09-46-08-12-ab-f6-e0-7d')
    return ILanguageExceptionErrorInfo
def _define_ILanguageExceptionErrorInfo():
    ILanguageExceptionErrorInfo = win32more.System.WinRT.ILanguageExceptionErrorInfo_head
    ILanguageExceptionErrorInfo.GetLanguageException = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(3, 'GetLanguageException', ((1, 'languageException'),)))
    win32more.System.Com.IUnknown
    return ILanguageExceptionErrorInfo
def _define_ILanguageExceptionErrorInfo2_head():
    class ILanguageExceptionErrorInfo2(win32more.System.WinRT.ILanguageExceptionErrorInfo_head):
        Guid = Guid('5746e5c4-5b97-424c-b6-20-28-22-91-57-34-dd')
    return ILanguageExceptionErrorInfo2
def _define_ILanguageExceptionErrorInfo2():
    ILanguageExceptionErrorInfo2 = win32more.System.WinRT.ILanguageExceptionErrorInfo2_head
    ILanguageExceptionErrorInfo2.GetPreviousLanguageExceptionErrorInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WinRT.ILanguageExceptionErrorInfo2_head))(4, 'GetPreviousLanguageExceptionErrorInfo', ((1, 'previousLanguageExceptionErrorInfo'),)))
    ILanguageExceptionErrorInfo2.CapturePropagationContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head)(5, 'CapturePropagationContext', ((1, 'languageException'),)))
    ILanguageExceptionErrorInfo2.GetPropagationContextHead = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WinRT.ILanguageExceptionErrorInfo2_head))(6, 'GetPropagationContextHead', ((1, 'propagatedLanguageExceptionErrorInfoHead'),)))
    win32more.System.WinRT.ILanguageExceptionErrorInfo
    return ILanguageExceptionErrorInfo2
def _define_ILanguageExceptionStackBackTrace_head():
    class ILanguageExceptionStackBackTrace(win32more.System.Com.IUnknown_head):
        Guid = Guid('cbe53fb5-f967-4258-8d-34-42-f5-e2-58-33-de')
    return ILanguageExceptionStackBackTrace
def _define_ILanguageExceptionStackBackTrace():
    ILanguageExceptionStackBackTrace = win32more.System.WinRT.ILanguageExceptionStackBackTrace_head
    ILanguageExceptionStackBackTrace.GetStackBackTrace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UIntPtr),POINTER(UInt32))(3, 'GetStackBackTrace', ((1, 'maxFramesToCapture'),(1, 'stackBackTrace'),(1, 'framesCaptured'),)))
    win32more.System.Com.IUnknown
    return ILanguageExceptionStackBackTrace
def _define_ILanguageExceptionTransform_head():
    class ILanguageExceptionTransform(win32more.System.Com.IUnknown_head):
        Guid = Guid('feb5a271-a6cd-45ce-88-0a-69-67-06-ba-dc-65')
    return ILanguageExceptionTransform
def _define_ILanguageExceptionTransform():
    ILanguageExceptionTransform = win32more.System.WinRT.ILanguageExceptionTransform_head
    ILanguageExceptionTransform.GetTransformedRestrictedErrorInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WinRT.IRestrictedErrorInfo_head))(3, 'GetTransformedRestrictedErrorInfo', ((1, 'restrictedErrorInfo'),)))
    win32more.System.Com.IUnknown
    return ILanguageExceptionTransform
def _define_IMemoryBufferByteAccess_head():
    class IMemoryBufferByteAccess(win32more.System.Com.IUnknown_head):
        Guid = Guid('5b0d3235-4dba-4d44-86-5e-8f-1d-0e-4f-d0-4d')
    return IMemoryBufferByteAccess
def _define_IMemoryBufferByteAccess():
    IMemoryBufferByteAccess = win32more.System.WinRT.IMemoryBufferByteAccess_head
    IMemoryBufferByteAccess.GetBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_char_p_no),POINTER(UInt32))(3, 'GetBuffer', ((1, 'value'),(1, 'capacity'),)))
    win32more.System.Com.IUnknown
    return IMemoryBufferByteAccess
def _define_IMessageDispatcher_head():
    class IMessageDispatcher(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('f5f84c8f-cfd0-4cd6-b6-6b-c5-d2-6f-f1-68-9d')
    return IMessageDispatcher
def _define_IMessageDispatcher():
    IMessageDispatcher = win32more.System.WinRT.IMessageDispatcher_head
    IMessageDispatcher.PumpMessages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(6, 'PumpMessages', ()))
    win32more.System.WinRT.IInspectable
    return IMessageDispatcher
def _define_IPlayToManagerInterop_head():
    class IPlayToManagerInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('24394699-1f2c-4eb3-8c-d7-0e-c1-da-42-a5-40')
    return IPlayToManagerInterop
def _define_IPlayToManagerInterop():
    IPlayToManagerInterop = win32more.System.WinRT.IPlayToManagerInterop_head
    IPlayToManagerInterop.GetForWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p))(6, 'GetForWindow', ((1, 'appWindow'),(1, 'riid'),(1, 'playToManager'),)))
    IPlayToManagerInterop.ShowPlayToUIForWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND)(7, 'ShowPlayToUIForWindow', ((1, 'appWindow'),)))
    win32more.System.WinRT.IInspectable
    return IPlayToManagerInterop
def _define_IRestrictedErrorInfo_head():
    class IRestrictedErrorInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('82ba7092-4c88-427d-a7-bc-16-dd-93-fe-b6-7e')
    return IRestrictedErrorInfo
def _define_IRestrictedErrorInfo():
    IRestrictedErrorInfo = win32more.System.WinRT.IRestrictedErrorInfo_head
    IRestrictedErrorInfo.GetErrorDetails = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.HRESULT),POINTER(win32more.Foundation.BSTR),POINTER(win32more.Foundation.BSTR))(3, 'GetErrorDetails', ((1, 'description'),(1, 'error'),(1, 'restrictedDescription'),(1, 'capabilitySid'),)))
    IRestrictedErrorInfo.GetReference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR))(4, 'GetReference', ((1, 'reference'),)))
    win32more.System.Com.IUnknown
    return IRestrictedErrorInfo
def _define_IRoMetaDataLocator_head():
    class IRoMetaDataLocator(c_void_p):
        pass
    return IRoMetaDataLocator
def _define_IRoMetaDataLocator():
    IRoMetaDataLocator = win32more.System.WinRT.IRoMetaDataLocator_head
    IRoMetaDataLocator.Locate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.WinRT.IRoSimpleMetaDataBuilder_head)(0, 'Locate', ((1, 'nameElement'),(1, 'metaDataDestination'),)))
    return IRoMetaDataLocator
def _define_IRoSimpleMetaDataBuilder_head():
    class IRoSimpleMetaDataBuilder(c_void_p):
        pass
    return IRoSimpleMetaDataBuilder
def _define_IRoSimpleMetaDataBuilder():
    IRoSimpleMetaDataBuilder = win32more.System.WinRT.IRoSimpleMetaDataBuilder_head
    IRoSimpleMetaDataBuilder.SetWinRtInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid)(0, 'SetWinRtInterface', ((1, 'iid'),)))
    IRoSimpleMetaDataBuilder.SetDelegate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid)(1, 'SetDelegate', ((1, 'iid'),)))
    IRoSimpleMetaDataBuilder.SetInterfaceGroupSimpleDefault = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(Guid))(2, 'SetInterfaceGroupSimpleDefault', ((1, 'name'),(1, 'defaultInterfaceName'),(1, 'defaultInterfaceIID'),)))
    IRoSimpleMetaDataBuilder.SetInterfaceGroupParameterizedDefault = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Foundation.PWSTR))(3, 'SetInterfaceGroupParameterizedDefault', ((1, 'name'),(1, 'elementCount'),(1, 'defaultInterfaceNameElements'),)))
    IRoSimpleMetaDataBuilder.SetRuntimeClassSimpleDefault = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(Guid))(4, 'SetRuntimeClassSimpleDefault', ((1, 'name'),(1, 'defaultInterfaceName'),(1, 'defaultInterfaceIID'),)))
    IRoSimpleMetaDataBuilder.SetRuntimeClassParameterizedDefault = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Foundation.PWSTR))(5, 'SetRuntimeClassParameterizedDefault', ((1, 'name'),(1, 'elementCount'),(1, 'defaultInterfaceNameElements'),)))
    IRoSimpleMetaDataBuilder.SetStruct = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Foundation.PWSTR))(6, 'SetStruct', ((1, 'name'),(1, 'numFields'),(1, 'fieldTypeNames'),)))
    IRoSimpleMetaDataBuilder.SetEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(7, 'SetEnum', ((1, 'name'),(1, 'baseType'),)))
    IRoSimpleMetaDataBuilder.SetParameterizedInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,UInt32)(8, 'SetParameterizedInterface', ((1, 'piid'),(1, 'numArgs'),)))
    IRoSimpleMetaDataBuilder.SetParameterizedDelegate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,UInt32)(9, 'SetParameterizedDelegate', ((1, 'piid'),(1, 'numArgs'),)))
    return IRoSimpleMetaDataBuilder
def _define_IShareWindowCommandEventArgsInterop_head():
    class IShareWindowCommandEventArgsInterop(win32more.System.Com.IUnknown_head):
        Guid = Guid('6571a721-643d-43d4-ac-a4-6b-6f-5f-30-f1-ad')
    return IShareWindowCommandEventArgsInterop
def _define_IShareWindowCommandEventArgsInterop():
    IShareWindowCommandEventArgsInterop = win32more.System.WinRT.IShareWindowCommandEventArgsInterop_head
    IShareWindowCommandEventArgsInterop.GetWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HWND))(3, 'GetWindow', ((1, 'value'),)))
    win32more.System.Com.IUnknown
    return IShareWindowCommandEventArgsInterop
def _define_IShareWindowCommandSourceInterop_head():
    class IShareWindowCommandSourceInterop(win32more.System.Com.IUnknown_head):
        Guid = Guid('461a191f-8424-43a6-a0-fa-34-51-a2-2f-56-ab')
    return IShareWindowCommandSourceInterop
def _define_IShareWindowCommandSourceInterop():
    IShareWindowCommandSourceInterop = win32more.System.WinRT.IShareWindowCommandSourceInterop_head
    IShareWindowCommandSourceInterop.GetForWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p))(3, 'GetForWindow', ((1, 'appWindow'),(1, 'riid'),(1, 'shareWindowCommandSource'),)))
    win32more.System.Com.IUnknown
    return IShareWindowCommandSourceInterop
def _define_ISpatialInteractionManagerInterop_head():
    class ISpatialInteractionManagerInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('5c4ee536-6a98-4b86-a1-70-58-70-13-d6-fd-4b')
    return ISpatialInteractionManagerInterop
def _define_ISpatialInteractionManagerInterop():
    ISpatialInteractionManagerInterop = win32more.System.WinRT.ISpatialInteractionManagerInterop_head
    ISpatialInteractionManagerInterop.GetForWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p))(6, 'GetForWindow', ((1, 'window'),(1, 'riid'),(1, 'spatialInteractionManager'),)))
    win32more.System.WinRT.IInspectable
    return ISpatialInteractionManagerInterop
def _define_ISystemMediaTransportControlsInterop_head():
    class ISystemMediaTransportControlsInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('ddb0472d-c911-4a1f-86-d9-dc-3d-71-a9-5f-5a')
    return ISystemMediaTransportControlsInterop
def _define_ISystemMediaTransportControlsInterop():
    ISystemMediaTransportControlsInterop = win32more.System.WinRT.ISystemMediaTransportControlsInterop_head
    ISystemMediaTransportControlsInterop.GetForWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p))(6, 'GetForWindow', ((1, 'appWindow'),(1, 'riid'),(1, 'mediaTransportControl'),)))
    win32more.System.WinRT.IInspectable
    return ISystemMediaTransportControlsInterop
def _define_IUIViewSettingsInterop_head():
    class IUIViewSettingsInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('3694dbf9-8f68-44be-8f-f5-19-5c-98-ed-e8-a6')
    return IUIViewSettingsInterop
def _define_IUIViewSettingsInterop():
    IUIViewSettingsInterop = win32more.System.WinRT.IUIViewSettingsInterop_head
    IUIViewSettingsInterop.GetForWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p))(6, 'GetForWindow', ((1, 'hwnd'),(1, 'riid'),(1, 'ppv'),)))
    win32more.System.WinRT.IInspectable
    return IUIViewSettingsInterop
def _define_IUserActivityInterop_head():
    class IUserActivityInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('1ade314d-0e0a-40d9-82-4c-9a-08-8a-50-05-9f')
    return IUserActivityInterop
def _define_IUserActivityInterop():
    IUserActivityInterop = win32more.System.WinRT.IUserActivityInterop_head
    IUserActivityInterop.CreateSessionForWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p))(6, 'CreateSessionForWindow', ((1, 'window'),(1, 'iid'),(1, 'value'),)))
    win32more.System.WinRT.IInspectable
    return IUserActivityInterop
def _define_IUserActivityRequestManagerInterop_head():
    class IUserActivityRequestManagerInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('dd69f876-9699-4715-90-95-e3-7e-a3-0d-fa-1b')
    return IUserActivityRequestManagerInterop
def _define_IUserActivityRequestManagerInterop():
    IUserActivityRequestManagerInterop = win32more.System.WinRT.IUserActivityRequestManagerInterop_head
    IUserActivityRequestManagerInterop.GetForWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(Guid),POINTER(c_void_p))(6, 'GetForWindow', ((1, 'window'),(1, 'iid'),(1, 'value'),)))
    win32more.System.WinRT.IInspectable
    return IUserActivityRequestManagerInterop
def _define_IUserActivitySourceHostInterop_head():
    class IUserActivitySourceHostInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('c15df8bc-8844-487a-b8-5b-75-78-e0-f6-14-19')
    return IUserActivitySourceHostInterop
def _define_IUserActivitySourceHostInterop():
    IUserActivitySourceHostInterop = win32more.System.WinRT.IUserActivitySourceHostInterop_head
    IUserActivitySourceHostInterop.SetActivitySourceHost = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.WinRT.HSTRING)(6, 'SetActivitySourceHost', ((1, 'activitySourceHost'),)))
    win32more.System.WinRT.IInspectable
    return IUserActivitySourceHostInterop
def _define_IUserConsentVerifierInterop_head():
    class IUserConsentVerifierInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('39e050c3-4e74-441a-8d-c0-b8-11-04-df-94-9c')
    return IUserConsentVerifierInterop
def _define_IUserConsentVerifierInterop():
    IUserConsentVerifierInterop = win32more.System.WinRT.IUserConsentVerifierInterop_head
    IUserConsentVerifierInterop.RequestVerificationForWindowAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.System.WinRT.HSTRING,POINTER(Guid),POINTER(c_void_p))(6, 'RequestVerificationForWindowAsync', ((1, 'appWindow'),(1, 'message'),(1, 'riid'),(1, 'asyncOperation'),)))
    win32more.System.WinRT.IInspectable
    return IUserConsentVerifierInterop
def _define_IWeakReference_head():
    class IWeakReference(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000037-0000-0000-c0-00-00-00-00-00-00-46')
    return IWeakReference
def _define_IWeakReference():
    IWeakReference = win32more.System.WinRT.IWeakReference_head
    IWeakReference.Resolve = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p))(3, 'Resolve', ((1, 'riid'),(1, 'objectReference'),)))
    win32more.System.Com.IUnknown
    return IWeakReference
def _define_IWeakReferenceSource_head():
    class IWeakReferenceSource(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000038-0000-0000-c0-00-00-00-00-00-00-46')
    return IWeakReferenceSource
def _define_IWeakReferenceSource():
    IWeakReferenceSource = win32more.System.WinRT.IWeakReferenceSource_head
    IWeakReferenceSource.GetWeakReference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.WinRT.IWeakReference_head))(3, 'GetWeakReference', ((1, 'weakReference'),)))
    win32more.System.Com.IUnknown
    return IWeakReferenceSource
def _define_IWebAuthenticationCoreManagerInterop_head():
    class IWebAuthenticationCoreManagerInterop(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('f4b8e804-811e-4436-b6-9c-44-cb-67-b7-20-84')
    return IWebAuthenticationCoreManagerInterop
def _define_IWebAuthenticationCoreManagerInterop():
    IWebAuthenticationCoreManagerInterop = win32more.System.WinRT.IWebAuthenticationCoreManagerInterop_head
    IWebAuthenticationCoreManagerInterop.RequestTokenForWindowAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.System.WinRT.IInspectable_head,POINTER(Guid),POINTER(c_void_p))(6, 'RequestTokenForWindowAsync', ((1, 'appWindow'),(1, 'request'),(1, 'riid'),(1, 'asyncInfo'),)))
    IWebAuthenticationCoreManagerInterop.RequestTokenWithWebAccountForWindowAsync = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.System.WinRT.IInspectable_head,win32more.System.WinRT.IInspectable_head,POINTER(Guid),POINTER(c_void_p))(7, 'RequestTokenWithWebAccountForWindowAsync', ((1, 'appWindow'),(1, 'request'),(1, 'webAccount'),(1, 'riid'),(1, 'asyncInfo'),)))
    win32more.System.WinRT.IInspectable
    return IWebAuthenticationCoreManagerInterop
def _define_PINSPECT_HSTRING_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,UInt32,c_char_p_no)
def _define_PINSPECT_HSTRING_CALLBACK2():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt64,UInt32,c_char_p_no)
def _define_PINSPECT_MEMORY_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,UInt32,c_char_p_no)
RO_ERROR_REPORTING_FLAGS = UInt32
RO_ERROR_REPORTING_NONE = 0
RO_ERROR_REPORTING_SUPPRESSEXCEPTIONS = 1
RO_ERROR_REPORTING_FORCEEXCEPTIONS = 2
RO_ERROR_REPORTING_USESETERRORINFO = 4
RO_ERROR_REPORTING_SUPPRESSSETERRORINFO = 8
RO_INIT_TYPE = Int32
RO_INIT_SINGLETHREADED = 0
RO_INIT_MULTITHREADED = 1
ROPARAMIIDHANDLE = IntPtr
def _define_ServerInformation_head():
    class ServerInformation(Structure):
        pass
    return ServerInformation
def _define_ServerInformation():
    ServerInformation = win32more.System.WinRT.ServerInformation_head
    ServerInformation._fields_ = [
        ('dwServerPid', UInt32),
        ('dwServerTid', UInt32),
        ('ui64ServerAddress', UInt64),
    ]
    return ServerInformation
TrustLevel = Int32
TrustLevel_BaseTrust = 0
TrustLevel_PartialTrust = 1
TrustLevel_FullTrust = 2
__all__ = [
    "ACTIVATIONTYPE",
    "ACTIVATIONTYPE_FROM_DATA",
    "ACTIVATIONTYPE_FROM_FILE",
    "ACTIVATIONTYPE_FROM_MONIKER",
    "ACTIVATIONTYPE_FROM_STORAGE",
    "ACTIVATIONTYPE_FROM_STREAM",
    "ACTIVATIONTYPE_UNCATEGORIZED",
    "AGILEREFERENCE_DEFAULT",
    "AGILEREFERENCE_DELAYEDMARSHAL",
    "APARTMENT_SHUTDOWN_REGISTRATION_COOKIE",
    "AgileReferenceOptions",
    "BSOS_DEFAULT",
    "BSOS_OPTIONS",
    "BSOS_PREFERDESTINATIONSTREAM",
    "CASTING_CONNECTION_ERROR_STATUS",
    "CASTING_CONNECTION_ERROR_STATUS_DEVICE_DID_NOT_RESPOND",
    "CASTING_CONNECTION_ERROR_STATUS_DEVICE_ERROR",
    "CASTING_CONNECTION_ERROR_STATUS_DEVICE_LOCKED",
    "CASTING_CONNECTION_ERROR_STATUS_INVALID_CASTING_SOURCE",
    "CASTING_CONNECTION_ERROR_STATUS_PROTECTED_PLAYBACK_FAILED",
    "CASTING_CONNECTION_ERROR_STATUS_SUCCEEDED",
    "CASTING_CONNECTION_ERROR_STATUS_UNKNOWN",
    "CASTING_CONNECTION_STATE",
    "CASTING_CONNECTION_STATE_CONNECTED",
    "CASTING_CONNECTION_STATE_CONNECTING",
    "CASTING_CONNECTION_STATE_DISCONNECTED",
    "CASTING_CONNECTION_STATE_DISCONNECTING",
    "CASTING_CONNECTION_STATE_RENDERING",
    "CastingSourceInfo_Property_CastingTypes",
    "CastingSourceInfo_Property_PreferredSourceUriScheme",
    "CastingSourceInfo_Property_ProtectedMedia",
    "CoDecodeProxy",
    "CreateControlInput",
    "CreateControlInputEx",
    "CreateDispatcherQueueController",
    "CreateRandomAccessStreamOnFile",
    "CreateRandomAccessStreamOverStream",
    "CreateStreamOverRandomAccessStream",
    "DISPATCHERQUEUE_THREAD_APARTMENTTYPE",
    "DISPATCHERQUEUE_THREAD_TYPE",
    "DQTAT_COM_ASTA",
    "DQTAT_COM_NONE",
    "DQTAT_COM_STA",
    "DQTYPE_THREAD_CURRENT",
    "DQTYPE_THREAD_DEDICATED",
    "DispatcherQueueOptions",
    "EventRegistrationToken",
    "GetRestrictedErrorInfo",
    "HSTRING",
    "HSTRING_BUFFER",
    "HSTRING_HEADER",
    "HSTRING_UserFree",
    "HSTRING_UserFree64",
    "HSTRING_UserMarshal",
    "HSTRING_UserMarshal64",
    "HSTRING_UserSize",
    "HSTRING_UserSize64",
    "HSTRING_UserUnmarshal",
    "HSTRING_UserUnmarshal64",
    "IAccountsSettingsPaneInterop",
    "IActivationFactory",
    "IAgileReference",
    "IApartmentShutdown",
    "IAppServiceConnectionExtendedExecution",
    "IBufferByteAccess",
    "ICastingController",
    "ICastingEventHandler",
    "ICastingSourceInfo",
    "ICoreInputInterop",
    "ICoreWindowAdapterInterop",
    "ICoreWindowComponentInterop",
    "ICoreWindowInterop",
    "ICorrelationVectorInformation",
    "ICorrelationVectorSource",
    "IDragDropManagerInterop",
    "IHolographicSpaceInterop",
    "IInputPaneInterop",
    "IInspectable",
    "ILanguageExceptionErrorInfo",
    "ILanguageExceptionErrorInfo2",
    "ILanguageExceptionStackBackTrace",
    "ILanguageExceptionTransform",
    "IMemoryBufferByteAccess",
    "IMessageDispatcher",
    "IPlayToManagerInterop",
    "IRestrictedErrorInfo",
    "IRoMetaDataLocator",
    "IRoSimpleMetaDataBuilder",
    "IShareWindowCommandEventArgsInterop",
    "IShareWindowCommandSourceInterop",
    "ISpatialInteractionManagerInterop",
    "ISystemMediaTransportControlsInterop",
    "IUIViewSettingsInterop",
    "IUserActivityInterop",
    "IUserActivityRequestManagerInterop",
    "IUserActivitySourceHostInterop",
    "IUserConsentVerifierInterop",
    "IWeakReference",
    "IWeakReferenceSource",
    "IWebAuthenticationCoreManagerInterop",
    "IsErrorPropagationEnabled",
    "MAX_ERROR_MESSAGE_CHARS",
    "MetaDataGetDispenser",
    "PINSPECT_HSTRING_CALLBACK",
    "PINSPECT_HSTRING_CALLBACK2",
    "PINSPECT_MEMORY_CALLBACK",
    "ROPARAMIIDHANDLE",
    "RO_ERROR_REPORTING_FLAGS",
    "RO_ERROR_REPORTING_FORCEEXCEPTIONS",
    "RO_ERROR_REPORTING_NONE",
    "RO_ERROR_REPORTING_SUPPRESSEXCEPTIONS",
    "RO_ERROR_REPORTING_SUPPRESSSETERRORINFO",
    "RO_ERROR_REPORTING_USESETERRORINFO",
    "RO_INIT_MULTITHREADED",
    "RO_INIT_SINGLETHREADED",
    "RO_INIT_TYPE",
    "RoActivateInstance",
    "RoCaptureErrorContext",
    "RoClearError",
    "RoFailFastWithErrorContext",
    "RoFreeParameterizedTypeExtra",
    "RoGetActivationFactory",
    "RoGetAgileReference",
    "RoGetApartmentIdentifier",
    "RoGetBufferMarshaler",
    "RoGetErrorReportingFlags",
    "RoGetMatchingRestrictedErrorInfo",
    "RoGetParameterizedTypeInstanceIID",
    "RoGetServerActivatableClasses",
    "RoInitialize",
    "RoInspectCapturedStackBackTrace",
    "RoInspectThreadErrorInfo",
    "RoOriginateError",
    "RoOriginateErrorW",
    "RoOriginateLanguageException",
    "RoParameterizedTypeExtraGetTypeSignature",
    "RoRegisterActivationFactories",
    "RoRegisterForApartmentShutdown",
    "RoReportFailedDelegate",
    "RoReportUnhandledError",
    "RoResolveRestrictedErrorInfoReference",
    "RoRevokeActivationFactories",
    "RoSetErrorReportingFlags",
    "RoTransformError",
    "RoTransformErrorW",
    "RoUninitialize",
    "RoUnregisterForApartmentShutdown",
    "ServerInformation",
    "SetRestrictedErrorInfo",
    "TrustLevel",
    "TrustLevel_BaseTrust",
    "TrustLevel_FullTrust",
    "TrustLevel_PartialTrust",
    "WindowsCompareStringOrdinal",
    "WindowsConcatString",
    "WindowsCreateString",
    "WindowsCreateStringReference",
    "WindowsDeleteString",
    "WindowsDeleteStringBuffer",
    "WindowsDuplicateString",
    "WindowsGetStringLen",
    "WindowsGetStringRawBuffer",
    "WindowsInspectString",
    "WindowsInspectString2",
    "WindowsIsStringEmpty",
    "WindowsPreallocateStringBuffer",
    "WindowsPromoteStringBuffer",
    "WindowsReplaceString",
    "WindowsStringHasEmbeddedNull",
    "WindowsSubstring",
    "WindowsSubstringWithSpecifiedLength",
    "WindowsTrimStringEnd",
    "WindowsTrimStringStart",
    "_RO_REGISTRATION_COOKIE",
]
