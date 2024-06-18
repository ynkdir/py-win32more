from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.Marshal
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Win32.UI.Shell.PropertiesSystem
ACTIVATIONTYPE = Int32
ACTIVATIONTYPE_UNCATEGORIZED: win32more.Windows.Win32.System.WinRT.ACTIVATIONTYPE = 0
ACTIVATIONTYPE_FROM_MONIKER: win32more.Windows.Win32.System.WinRT.ACTIVATIONTYPE = 1
ACTIVATIONTYPE_FROM_DATA: win32more.Windows.Win32.System.WinRT.ACTIVATIONTYPE = 2
ACTIVATIONTYPE_FROM_STORAGE: win32more.Windows.Win32.System.WinRT.ACTIVATIONTYPE = 4
ACTIVATIONTYPE_FROM_STREAM: win32more.Windows.Win32.System.WinRT.ACTIVATIONTYPE = 8
ACTIVATIONTYPE_FROM_FILE: win32more.Windows.Win32.System.WinRT.ACTIVATIONTYPE = 16
APARTMENT_SHUTDOWN_REGISTRATION_COOKIE = VoidPtr
AgileReferenceOptions = Int32
AGILEREFERENCE_DEFAULT: win32more.Windows.Win32.System.WinRT.AgileReferenceOptions = 0
AGILEREFERENCE_DELAYEDMARSHAL: win32more.Windows.Win32.System.WinRT.AgileReferenceOptions = 1
MAX_ERROR_MESSAGE_CHARS: UInt32 = 512
CastingSourceInfo_Property_PreferredSourceUriScheme: String = 'PreferredSourceUriScheme'
CastingSourceInfo_Property_CastingTypes: String = 'CastingTypes'
CastingSourceInfo_Property_ProtectedMedia: String = 'ProtectedMedia'
@winfunctype('OLE32.dll')
def CoDecodeProxy(dwClientPid: UInt32, ui64ProxyAddress: UInt64, pServerInformation: POINTER(win32more.Windows.Win32.System.WinRT.ServerInformation)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def RoGetAgileReference(options: win32more.Windows.Win32.System.WinRT.AgileReferenceOptions, riid: POINTER(Guid), pUnk: win32more.Windows.Win32.System.Com.IUnknown, ppAgileReference: POINTER(win32more.Windows.Win32.System.WinRT.IAgileReference)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def HSTRING_UserSize(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING)) -> UInt32: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def HSTRING_UserMarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING)) -> POINTER(Byte): ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def HSTRING_UserUnmarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING)) -> POINTER(Byte): ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def HSTRING_UserFree(param0: POINTER(UInt32), param1: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING)) -> Void: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def HSTRING_UserSize64(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING)) -> UInt32: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def HSTRING_UserMarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING)) -> POINTER(Byte): ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def HSTRING_UserUnmarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING)) -> POINTER(Byte): ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def HSTRING_UserFree64(param0: POINTER(UInt32), param1: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING)) -> Void: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsCreateString(sourceString: win32more.Windows.Win32.Foundation.PWSTR, length: UInt32, string: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsCreateStringReference(sourceString: win32more.Windows.Win32.Foundation.PWSTR, length: UInt32, hstringHeader: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING_HEADER), string: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsDeleteString(string: win32more.Windows.Win32.System.WinRT.HSTRING) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsDuplicateString(string: win32more.Windows.Win32.System.WinRT.HSTRING, newString: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsGetStringLen(string: win32more.Windows.Win32.System.WinRT.HSTRING) -> UInt32: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsGetStringRawBuffer(string: win32more.Windows.Win32.System.WinRT.HSTRING, length: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.PWSTR: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsIsStringEmpty(string: win32more.Windows.Win32.System.WinRT.HSTRING) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsStringHasEmbeddedNull(string: win32more.Windows.Win32.System.WinRT.HSTRING, hasEmbedNull: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsCompareStringOrdinal(string1: win32more.Windows.Win32.System.WinRT.HSTRING, string2: win32more.Windows.Win32.System.WinRT.HSTRING, result: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsSubstring(string: win32more.Windows.Win32.System.WinRT.HSTRING, startIndex: UInt32, newString: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsSubstringWithSpecifiedLength(string: win32more.Windows.Win32.System.WinRT.HSTRING, startIndex: UInt32, length: UInt32, newString: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsConcatString(string1: win32more.Windows.Win32.System.WinRT.HSTRING, string2: win32more.Windows.Win32.System.WinRT.HSTRING, newString: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsReplaceString(string: win32more.Windows.Win32.System.WinRT.HSTRING, stringReplaced: win32more.Windows.Win32.System.WinRT.HSTRING, stringReplaceWith: win32more.Windows.Win32.System.WinRT.HSTRING, newString: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsTrimStringStart(string: win32more.Windows.Win32.System.WinRT.HSTRING, trimString: win32more.Windows.Win32.System.WinRT.HSTRING, newString: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsTrimStringEnd(string: win32more.Windows.Win32.System.WinRT.HSTRING, trimString: win32more.Windows.Win32.System.WinRT.HSTRING, newString: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsPreallocateStringBuffer(length: UInt32, charBuffer: POINTER(POINTER(UInt16)), bufferHandle: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING_BUFFER)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsPromoteStringBuffer(bufferHandle: win32more.Windows.Win32.System.WinRT.HSTRING_BUFFER, string: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsDeleteStringBuffer(bufferHandle: win32more.Windows.Win32.System.WinRT.HSTRING_BUFFER) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsInspectString(targetHString: UIntPtr, machine: UInt16, callback: win32more.Windows.Win32.System.WinRT.PINSPECT_HSTRING_CALLBACK, context: VoidPtr, length: POINTER(UInt32), targetStringAddress: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-1.dll')
def WindowsInspectString2(targetHString: UInt64, machine: UInt16, callback: win32more.Windows.Win32.System.WinRT.PINSPECT_HSTRING_CALLBACK2, context: VoidPtr, length: POINTER(UInt32), targetStringAddress: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('CoreMessaging.dll')
def CreateDispatcherQueueController(options: win32more.Windows.Win32.System.WinRT.DispatcherQueueOptions, dispatcherQueueController: POINTER(win32more.Windows.System.DispatcherQueueController)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-l1-1-0.dll')
def RoInitialize(initType: win32more.Windows.Win32.System.WinRT.RO_INIT_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-l1-1-0.dll')
def RoUninitialize() -> Void: ...
@winfunctype('api-ms-win-core-winrt-l1-1-0.dll')
def RoActivateInstance(activatableClassId: win32more.Windows.Win32.System.WinRT.HSTRING, instance: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-l1-1-0.dll')
def RoRegisterActivationFactories(activatableClassIds: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING), activationFactoryCallbacks: POINTER(win32more.Windows.Win32.System.WinRT.PFNGETACTIVATIONFACTORY), count: UInt32, cookie: POINTER(win32more.Windows.Win32.System.WinRT.RO_REGISTRATION_COOKIE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-l1-1-0.dll')
def RoRevokeActivationFactories(cookie: win32more.Windows.Win32.System.WinRT.RO_REGISTRATION_COOKIE) -> Void: ...
@winfunctype('api-ms-win-core-winrt-l1-1-0.dll')
def RoGetActivationFactory(activatableClassId: win32more.Windows.Win32.System.WinRT.HSTRING, iid: POINTER(Guid), factory: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-l1-1-0.dll')
def RoRegisterForApartmentShutdown(callbackObject: win32more.Windows.Win32.System.WinRT.IApartmentShutdown, apartmentIdentifier: POINTER(UInt64), regCookie: POINTER(win32more.Windows.Win32.System.WinRT.APARTMENT_SHUTDOWN_REGISTRATION_COOKIE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-l1-1-0.dll')
def RoUnregisterForApartmentShutdown(regCookie: win32more.Windows.Win32.System.WinRT.APARTMENT_SHUTDOWN_REGISTRATION_COOKIE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-l1-1-0.dll')
def RoGetApartmentIdentifier(apartmentIdentifier: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-robuffer-l1-1-0.dll')
def RoGetBufferMarshaler(bufferMarshaler: POINTER(win32more.Windows.Win32.System.Com.Marshal.IMarshal)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def RoGetErrorReportingFlags(pflags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def RoSetErrorReportingFlags(flags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def RoResolveRestrictedErrorInfoReference(reference: win32more.Windows.Win32.Foundation.PWSTR, ppRestrictedErrorInfo: POINTER(win32more.Windows.Win32.System.WinRT.IRestrictedErrorInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def SetRestrictedErrorInfo(pRestrictedErrorInfo: win32more.Windows.Win32.System.WinRT.IRestrictedErrorInfo) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def GetRestrictedErrorInfo(ppRestrictedErrorInfo: POINTER(win32more.Windows.Win32.System.WinRT.IRestrictedErrorInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def RoOriginateErrorW(error: win32more.Windows.Win32.Foundation.HRESULT, cchMax: UInt32, message: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def RoOriginateError(error: win32more.Windows.Win32.Foundation.HRESULT, message: win32more.Windows.Win32.System.WinRT.HSTRING) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def RoTransformErrorW(oldError: win32more.Windows.Win32.Foundation.HRESULT, newError: win32more.Windows.Win32.Foundation.HRESULT, cchMax: UInt32, message: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def RoTransformError(oldError: win32more.Windows.Win32.Foundation.HRESULT, newError: win32more.Windows.Win32.Foundation.HRESULT, message: win32more.Windows.Win32.System.WinRT.HSTRING) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def RoCaptureErrorContext(hr: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def RoFailFastWithErrorContext(hrError: win32more.Windows.Win32.Foundation.HRESULT) -> Void: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-1.dll')
def RoOriginateLanguageException(error: win32more.Windows.Win32.Foundation.HRESULT, message: win32more.Windows.Win32.System.WinRT.HSTRING, languageException: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-1.dll')
def RoClearError() -> Void: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-1.dll')
def RoReportUnhandledError(pRestrictedErrorInfo: win32more.Windows.Win32.System.WinRT.IRestrictedErrorInfo) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-1.dll')
def RoInspectThreadErrorInfo(targetTebAddress: UIntPtr, machine: UInt16, readMemoryCallback: win32more.Windows.Win32.System.WinRT.PINSPECT_MEMORY_CALLBACK, context: VoidPtr, targetErrorInfoAddress: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-1.dll')
def RoInspectCapturedStackBackTrace(targetErrorInfoAddress: UIntPtr, machine: UInt16, readMemoryCallback: win32more.Windows.Win32.System.WinRT.PINSPECT_MEMORY_CALLBACK, context: VoidPtr, frameCount: POINTER(UInt32), targetBackTraceAddress: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-1.dll')
def RoGetMatchingRestrictedErrorInfo(hrIn: win32more.Windows.Win32.Foundation.HRESULT, ppRestrictedErrorInfo: POINTER(win32more.Windows.Win32.System.WinRT.IRestrictedErrorInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-1.dll')
def RoReportFailedDelegate(punkDelegate: win32more.Windows.Win32.System.Com.IUnknown, pRestrictedErrorInfo: win32more.Windows.Win32.System.WinRT.IRestrictedErrorInfo) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-1.dll')
def IsErrorPropagationEnabled() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-winrt-registration-l1-1-0.dll')
def RoGetServerActivatableClasses(serverName: win32more.Windows.Win32.System.WinRT.HSTRING, activatableClassIds: POINTER(POINTER(win32more.Windows.Win32.System.WinRT.HSTRING)), count: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-shcore-stream-winrt-l1-1-0.dll')
def CreateRandomAccessStreamOnFile(filePath: win32more.Windows.Win32.Foundation.PWSTR, accessMode: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-shcore-stream-winrt-l1-1-0.dll')
def CreateRandomAccessStreamOverStream(stream: win32more.Windows.Win32.System.Com.IStream, options: win32more.Windows.Win32.System.WinRT.BSOS_OPTIONS, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-shcore-stream-winrt-l1-1-0.dll')
def CreateStreamOverRandomAccessStream(randomAccessStream: win32more.Windows.Win32.System.Com.IUnknown, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@cfunctype('Windows.UI.dll')
def CreateControlInput(riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@cfunctype('Windows.UI.dll')
def CreateControlInputEx(pCoreWindow: win32more.Windows.Win32.System.Com.IUnknown, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
BSOS_OPTIONS = Int32
BSOS_DEFAULT: win32more.Windows.Win32.System.WinRT.BSOS_OPTIONS = 0
BSOS_PREFERDESTINATIONSTREAM: win32more.Windows.Win32.System.WinRT.BSOS_OPTIONS = 1
CASTING_CONNECTION_ERROR_STATUS = Int32
CASTING_CONNECTION_ERROR_STATUS_SUCCEEDED: win32more.Windows.Win32.System.WinRT.CASTING_CONNECTION_ERROR_STATUS = 0
CASTING_CONNECTION_ERROR_STATUS_DEVICE_DID_NOT_RESPOND: win32more.Windows.Win32.System.WinRT.CASTING_CONNECTION_ERROR_STATUS = 1
CASTING_CONNECTION_ERROR_STATUS_DEVICE_ERROR: win32more.Windows.Win32.System.WinRT.CASTING_CONNECTION_ERROR_STATUS = 2
CASTING_CONNECTION_ERROR_STATUS_DEVICE_LOCKED: win32more.Windows.Win32.System.WinRT.CASTING_CONNECTION_ERROR_STATUS = 3
CASTING_CONNECTION_ERROR_STATUS_PROTECTED_PLAYBACK_FAILED: win32more.Windows.Win32.System.WinRT.CASTING_CONNECTION_ERROR_STATUS = 4
CASTING_CONNECTION_ERROR_STATUS_INVALID_CASTING_SOURCE: win32more.Windows.Win32.System.WinRT.CASTING_CONNECTION_ERROR_STATUS = 5
CASTING_CONNECTION_ERROR_STATUS_UNKNOWN: win32more.Windows.Win32.System.WinRT.CASTING_CONNECTION_ERROR_STATUS = 6
CASTING_CONNECTION_STATE = Int32
CASTING_CONNECTION_STATE_DISCONNECTED: win32more.Windows.Win32.System.WinRT.CASTING_CONNECTION_STATE = 0
CASTING_CONNECTION_STATE_CONNECTED: win32more.Windows.Win32.System.WinRT.CASTING_CONNECTION_STATE = 1
CASTING_CONNECTION_STATE_RENDERING: win32more.Windows.Win32.System.WinRT.CASTING_CONNECTION_STATE = 2
CASTING_CONNECTION_STATE_DISCONNECTING: win32more.Windows.Win32.System.WinRT.CASTING_CONNECTION_STATE = 3
CASTING_CONNECTION_STATE_CONNECTING: win32more.Windows.Win32.System.WinRT.CASTING_CONNECTION_STATE = 4
DISPATCHERQUEUE_THREAD_APARTMENTTYPE = Int32
DQTAT_COM_NONE: win32more.Windows.Win32.System.WinRT.DISPATCHERQUEUE_THREAD_APARTMENTTYPE = 0
DQTAT_COM_ASTA: win32more.Windows.Win32.System.WinRT.DISPATCHERQUEUE_THREAD_APARTMENTTYPE = 1
DQTAT_COM_STA: win32more.Windows.Win32.System.WinRT.DISPATCHERQUEUE_THREAD_APARTMENTTYPE = 2
DISPATCHERQUEUE_THREAD_TYPE = Int32
DQTYPE_THREAD_DEDICATED: win32more.Windows.Win32.System.WinRT.DISPATCHERQUEUE_THREAD_TYPE = 1
DQTYPE_THREAD_CURRENT: win32more.Windows.Win32.System.WinRT.DISPATCHERQUEUE_THREAD_TYPE = 2
class DispatcherQueueOptions(Structure):
    dwSize: UInt32
    threadType: win32more.Windows.Win32.System.WinRT.DISPATCHERQUEUE_THREAD_TYPE
    apartmentType: win32more.Windows.Win32.System.WinRT.DISPATCHERQUEUE_THREAD_APARTMENTTYPE
class EventRegistrationToken(Structure):
    value: Int64
HSTRING = VoidPtr
HSTRING_BUFFER = VoidPtr
class HSTRING_HEADER(Structure):
    flags: UInt32
    length: UInt32
    padding1: UInt32
    padding2: UInt32
    data: IntPtr
class IAccountsSettingsPaneInterop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{d3ee12ad-3865-4362-9746-b75a682df0e6}')
    @commethod(6)
    def GetForWindow(self, appWindow: win32more.Windows.Win32.Foundation.HWND, riid: POINTER(Guid), accountsSettingsPane: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ShowManageAccountsForWindowAsync(self, appWindow: win32more.Windows.Win32.Foundation.HWND, riid: POINTER(Guid), asyncAction: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ShowAddAccountForWindowAsync(self, appWindow: win32more.Windows.Win32.Foundation.HWND, riid: POINTER(Guid), asyncAction: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActivationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{00000035-0000-0000-c000-000000000046}')
    @commethod(6)
    def ActivateInstance(self, instance: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAgileReference(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c03f6a43-65a4-9818-987e-e0b810d2a6f2}')
    @commethod(3)
    def Resolve(self, riid: POINTER(Guid), ppvObjectReference: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IApartmentShutdown(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a2f05a09-27a2-42b5-bc0e-ac163ef49d9b}')
    @commethod(3)
    def OnUninitialize(self, ui64ApartmentIdentifier: UInt64) -> Void: ...
class IAppServiceConnectionExtendedExecution(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{65219584-f9cb-4ae3-81f9-a28a6ca450d9}')
    @commethod(3)
    def OpenForExtendedExecutionAsync(self, riid: POINTER(Guid), operation: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBufferByteAccess(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{905a0fef-bc53-11df-8c49-001e4fc686da}')
    @commethod(3)
    def Buffer(self, value: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICastingController(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f0a56423-a664-4fbd-8b43-409a45e8d9a1}')
    @commethod(3)
    def Initialize(self, castingEngine: win32more.Windows.Win32.System.Com.IUnknown, castingSource: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Connect(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Disconnect(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Advise(self, eventHandler: win32more.Windows.Win32.System.WinRT.ICastingEventHandler, cookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UnAdvise(self, cookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICastingEventHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c79a6cb7-bebd-47a6-a2ad-4d45ad79c7bc}')
    @commethod(3)
    def OnStateChanged(self, newState: win32more.Windows.Win32.System.WinRT.CASTING_CONNECTION_STATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnError(self, errorStatus: win32more.Windows.Win32.System.WinRT.CASTING_CONNECTION_ERROR_STATUS, errorMessage: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICastingSourceInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{45101ab7-7c3a-4bce-9500-12c09024b298}')
    @commethod(3)
    def GetController(self, controller: POINTER(win32more.Windows.Win32.System.WinRT.ICastingController)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetProperties(self, props: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.INamedPropertyStore)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICoreInputInterop(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{40bfe3e3-b75a-4479-ac96-475365749bb8}')
    @commethod(3)
    def SetInputSource(self, value: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_MessageHandled(self, value: Byte) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICoreInputInterop2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{b8a2acd7-a0f0-40ee-8ee7-c82f59cc5cd4}')
    @commethod(6)
    def get_WindowHandle(self, window: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ChangeHostingContext(self, newParentWindow: win32more.Windows.Win32.Foundation.HWND, newViewInstanceId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICoreWindowAdapterInterop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{7a5b6fd1-cd73-4b6c-9cf4-2e869eaf470a}')
    @commethod(6)
    def get_AppActivationClientAdapter(self, value: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_ApplicationViewClientAdapter(self, value: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CoreApplicationViewClientAdapter(self, value: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_HoloViewClientAdapter(self, value: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_PositionerClientAdapter(self, value: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_SystemNavigationClientAdapter(self, value: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_TitleBarClientAdapter(self, value: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetWindowClientAdapter(self, value: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICoreWindowComponentInterop(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0576ab31-a310-4c40-ba31-fd37e0298dfa}')
    @commethod(3)
    def ConfigureComponentInput(self, hostViewInstanceId: UInt32, hwndHost: win32more.Windows.Win32.Foundation.HWND, inputSourceVisual: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetViewInstanceId(self, componentViewInstanceId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICoreWindowInterop(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{45d64a29-a63e-4cb6-b498-5781d298cb4f}')
    @commethod(3)
    def get_WindowHandle(self, hwnd: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_MessageHandled(self, value: Byte) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICorrelationVectorInformation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{83c78b3c-d88b-4950-aa6e-22b8d22aabd3}')
    @commethod(6)
    def get_LastCorrelationVectorForThread(self, cv: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_NextCorrelationVectorForThread(self, cv: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_NextCorrelationVectorForThread(self, cv: win32more.Windows.Win32.System.WinRT.HSTRING) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICorrelationVectorSource(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{152b8a3b-b9b9-4685-b56e-974847bc7545}')
    @commethod(3)
    def get_CorrelationVector(self, cv: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDragDropManagerInterop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{5ad8cba7-4c01-4dac-9074-827894292d63}')
    @commethod(6)
    def GetForWindow(self, hwnd: win32more.Windows.Win32.Foundation.HWND, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHolographicSpaceInterop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{5c4ee536-6a98-4b86-a170-587013d6fd4b}')
    @commethod(6)
    def CreateForWindow(self, window: win32more.Windows.Win32.Foundation.HWND, riid: POINTER(Guid), holographicSpace: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInputPaneInterop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{75cf2c57-9195-4931-8332-f0b409e916af}')
    @commethod(6)
    def GetForWindow(self, appWindow: win32more.Windows.Win32.Foundation.HWND, riid: POINTER(Guid), inputPane: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInspectable(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{af86e2e0-b12d-4c6a-9c5a-d7aa65101e90}')
    @commethod(3)
    def GetIids(self, iidCount: POINTER(UInt32), iids: POINTER(POINTER(Guid))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRuntimeClassName(self, className: POINTER(win32more.Windows.Win32.System.WinRT.HSTRING)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTrustLevel(self, trustLevel: POINTER(win32more.Windows.Win32.System.WinRT.TrustLevel)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ILanguageExceptionErrorInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{04a2dbf3-df83-116c-0946-0812abf6e07d}')
    @commethod(3)
    def GetLanguageException(self, languageException: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ILanguageExceptionErrorInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.ILanguageExceptionErrorInfo
    _iid_ = Guid('{5746e5c4-5b97-424c-b620-2822915734dd}')
    @commethod(4)
    def GetPreviousLanguageExceptionErrorInfo(self, previousLanguageExceptionErrorInfo: POINTER(win32more.Windows.Win32.System.WinRT.ILanguageExceptionErrorInfo2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CapturePropagationContext(self, languageException: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPropagationContextHead(self, propagatedLanguageExceptionErrorInfoHead: POINTER(win32more.Windows.Win32.System.WinRT.ILanguageExceptionErrorInfo2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ILanguageExceptionStackBackTrace(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cbe53fb5-f967-4258-8d34-42f5e25833de}')
    @commethod(3)
    def GetStackBackTrace(self, maxFramesToCapture: UInt32, stackBackTrace: POINTER(UIntPtr), framesCaptured: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ILanguageExceptionTransform(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{feb5a271-a6cd-45ce-880a-696706badc65}')
    @commethod(3)
    def GetTransformedRestrictedErrorInfo(self, restrictedErrorInfo: POINTER(win32more.Windows.Win32.System.WinRT.IRestrictedErrorInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMemoryBufferByteAccess(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5b0d3235-4dba-4d44-865e-8f1d0e4fd04d}')
    @commethod(3)
    def GetBuffer(self, value: POINTER(POINTER(Byte)), capacity: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMessageDispatcher(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f5f84c8f-cfd0-4cd6-b66b-c5d26ff1689d}')
    @commethod(6)
    def PumpMessages(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPlayToManagerInterop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{24394699-1f2c-4eb3-8cd7-0ec1da42a540}')
    @commethod(6)
    def GetForWindow(self, appWindow: win32more.Windows.Win32.Foundation.HWND, riid: POINTER(Guid), playToManager: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ShowPlayToUIForWindow(self, appWindow: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRestrictedErrorInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{82ba7092-4c88-427d-a7bc-16dd93feb67e}')
    @commethod(3)
    def GetErrorDetails(self, description: POINTER(win32more.Windows.Win32.Foundation.BSTR), error: POINTER(win32more.Windows.Win32.Foundation.HRESULT), restrictedDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR), capabilitySid: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetReference(self, reference: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShareWindowCommandEventArgsInterop(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6571a721-643d-43d4-aca4-6b6f5f30f1ad}')
    @commethod(3)
    def GetWindow(self, value: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShareWindowCommandSourceInterop(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{461a191f-8424-43a6-a0fa-3451a22f56ab}')
    @commethod(3)
    def GetForWindow(self, appWindow: win32more.Windows.Win32.Foundation.HWND, riid: POINTER(Guid), shareWindowCommandSource: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpatialInteractionManagerInterop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{5c4ee536-6a98-4b86-a170-587013d6fd4b}')
    @commethod(6)
    def GetForWindow(self, window: win32more.Windows.Win32.Foundation.HWND, riid: POINTER(Guid), spatialInteractionManager: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISystemMediaTransportControlsInterop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{ddb0472d-c911-4a1f-86d9-dc3d71a95f5a}')
    @commethod(6)
    def GetForWindow(self, appWindow: win32more.Windows.Win32.Foundation.HWND, riid: POINTER(Guid), mediaTransportControl: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUIViewSettingsInterop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{3694dbf9-8f68-44be-8ff5-195c98ede8a6}')
    @commethod(6)
    def GetForWindow(self, hwnd: win32more.Windows.Win32.Foundation.HWND, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUserActivityInterop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{1ade314d-0e0a-40d9-824c-9a088a50059f}')
    @commethod(6)
    def CreateSessionForWindow(self, window: win32more.Windows.Win32.Foundation.HWND, iid: POINTER(Guid), value: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUserActivityRequestManagerInterop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{dd69f876-9699-4715-9095-e37ea30dfa1b}')
    @commethod(6)
    def GetForWindow(self, window: win32more.Windows.Win32.Foundation.HWND, iid: POINTER(Guid), value: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUserActivitySourceHostInterop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c15df8bc-8844-487a-b85b-7578e0f61419}')
    @commethod(6)
    def SetActivitySourceHost(self, activitySourceHost: win32more.Windows.Win32.System.WinRT.HSTRING) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUserConsentVerifierInterop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{39e050c3-4e74-441a-8dc0-b81104df949c}')
    @commethod(6)
    def RequestVerificationForWindowAsync(self, appWindow: win32more.Windows.Win32.Foundation.HWND, message: win32more.Windows.Win32.System.WinRT.HSTRING, riid: POINTER(Guid), asyncOperation: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWeakReference(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000037-0000-0000-c000-000000000046}')
    @commethod(3)
    def Resolve(self, riid: POINTER(Guid), objectReference: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWeakReferenceSource(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000038-0000-0000-c000-000000000046}')
    @commethod(3)
    def GetWeakReference(self, weakReference: POINTER(win32more.Windows.Win32.System.WinRT.IWeakReference)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWebAuthenticationCoreManagerInterop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f4b8e804-811e-4436-b69c-44cb67b72084}')
    @commethod(6)
    def RequestTokenForWindowAsync(self, appWindow: win32more.Windows.Win32.Foundation.HWND, request: win32more.Windows.Win32.System.WinRT.IInspectable, riid: POINTER(Guid), asyncInfo: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RequestTokenWithWebAccountForWindowAsync(self, appWindow: win32more.Windows.Win32.Foundation.HWND, request: win32more.Windows.Win32.System.WinRT.IInspectable, webAccount: win32more.Windows.Win32.System.WinRT.IInspectable, riid: POINTER(Guid), asyncInfo: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNGETACTIVATIONFACTORY(param0: win32more.Windows.Win32.System.WinRT.HSTRING, param1: POINTER(win32more.Windows.Win32.System.WinRT.IActivationFactory)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PINSPECT_HSTRING_CALLBACK(context: VoidPtr, readAddress: UIntPtr, length: UInt32, buffer: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PINSPECT_HSTRING_CALLBACK2(context: VoidPtr, readAddress: UInt64, length: UInt32, buffer: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PINSPECT_MEMORY_CALLBACK(context: VoidPtr, readAddress: UIntPtr, length: UInt32, buffer: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
RO_ERROR_REPORTING_FLAGS = Int32
RO_ERROR_REPORTING_NONE: win32more.Windows.Win32.System.WinRT.RO_ERROR_REPORTING_FLAGS = 0
RO_ERROR_REPORTING_SUPPRESSEXCEPTIONS: win32more.Windows.Win32.System.WinRT.RO_ERROR_REPORTING_FLAGS = 1
RO_ERROR_REPORTING_FORCEEXCEPTIONS: win32more.Windows.Win32.System.WinRT.RO_ERROR_REPORTING_FLAGS = 2
RO_ERROR_REPORTING_USESETERRORINFO: win32more.Windows.Win32.System.WinRT.RO_ERROR_REPORTING_FLAGS = 4
RO_ERROR_REPORTING_SUPPRESSSETERRORINFO: win32more.Windows.Win32.System.WinRT.RO_ERROR_REPORTING_FLAGS = 8
RO_INIT_TYPE = Int32
RO_INIT_SINGLETHREADED: win32more.Windows.Win32.System.WinRT.RO_INIT_TYPE = 0
RO_INIT_MULTITHREADED: win32more.Windows.Win32.System.WinRT.RO_INIT_TYPE = 1
RO_REGISTRATION_COOKIE = IntPtr
class ServerInformation(Structure):
    dwServerPid: UInt32
    dwServerTid: UInt32
    ui64ServerAddress: UInt64
TrustLevel = Int32
BaseTrust: win32more.Windows.Win32.System.WinRT.TrustLevel = 0
PartialTrust: win32more.Windows.Win32.System.WinRT.TrustLevel = 1
FullTrust: win32more.Windows.Win32.System.WinRT.TrustLevel = 2


make_ready(__name__)
