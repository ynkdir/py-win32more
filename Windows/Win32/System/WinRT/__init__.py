from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.Com.Marshal
import Windows.Win32.System.WinRT
import Windows.Win32.UI.Shell.PropertiesSystem
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
ACTIVATIONTYPE = Int32
ACTIVATIONTYPE_UNCATEGORIZED: ACTIVATIONTYPE = 0
ACTIVATIONTYPE_FROM_MONIKER: ACTIVATIONTYPE = 1
ACTIVATIONTYPE_FROM_DATA: ACTIVATIONTYPE = 2
ACTIVATIONTYPE_FROM_STORAGE: ACTIVATIONTYPE = 4
ACTIVATIONTYPE_FROM_STREAM: ACTIVATIONTYPE = 8
ACTIVATIONTYPE_FROM_FILE: ACTIVATIONTYPE = 16
APARTMENT_SHUTDOWN_REGISTRATION_COOKIE = IntPtr
AgileReferenceOptions = Int32
AGILEREFERENCE_DEFAULT: AgileReferenceOptions = 0
AGILEREFERENCE_DELAYEDMARSHAL: AgileReferenceOptions = 1
MAX_ERROR_MESSAGE_CHARS: UInt32 = 512
CastingSourceInfo_Property_PreferredSourceUriScheme: String = 'PreferredSourceUriScheme'
CastingSourceInfo_Property_CastingTypes: String = 'CastingTypes'
CastingSourceInfo_Property_ProtectedMedia: String = 'ProtectedMedia'
@winfunctype('OLE32.dll')
def CoDecodeProxy(dwClientPid: UInt32, ui64ProxyAddress: UInt64, pServerInformation: POINTER(Windows.Win32.System.WinRT.ServerInformation_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def RoGetAgileReference(options: Windows.Win32.System.WinRT.AgileReferenceOptions, riid: POINTER(Guid), pUnk: Windows.Win32.System.Com.IUnknown_head, ppAgileReference: POINTER(Windows.Win32.System.WinRT.IAgileReference_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def HSTRING_UserSize(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(Windows.Win32.System.WinRT.HSTRING)) -> UInt32: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def HSTRING_UserMarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.System.WinRT.HSTRING)) -> POINTER(Byte): ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def HSTRING_UserUnmarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.System.WinRT.HSTRING)) -> POINTER(Byte): ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def HSTRING_UserFree(param0: POINTER(UInt32), param1: POINTER(Windows.Win32.System.WinRT.HSTRING)) -> Void: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def HSTRING_UserSize64(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(Windows.Win32.System.WinRT.HSTRING)) -> UInt32: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def HSTRING_UserMarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.System.WinRT.HSTRING)) -> POINTER(Byte): ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def HSTRING_UserUnmarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.System.WinRT.HSTRING)) -> POINTER(Byte): ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def HSTRING_UserFree64(param0: POINTER(UInt32), param1: POINTER(Windows.Win32.System.WinRT.HSTRING)) -> Void: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsCreateString(sourceString: Windows.Win32.Foundation.PWSTR, length: UInt32, string: POINTER(Windows.Win32.System.WinRT.HSTRING)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsCreateStringReference(sourceString: Windows.Win32.Foundation.PWSTR, length: UInt32, hstringHeader: POINTER(Windows.Win32.System.WinRT.HSTRING_HEADER_head), string: POINTER(Windows.Win32.System.WinRT.HSTRING)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsDeleteString(string: Windows.Win32.System.WinRT.HSTRING) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsDuplicateString(string: Windows.Win32.System.WinRT.HSTRING, newString: POINTER(Windows.Win32.System.WinRT.HSTRING)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsGetStringLen(string: Windows.Win32.System.WinRT.HSTRING) -> UInt32: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsGetStringRawBuffer(string: Windows.Win32.System.WinRT.HSTRING, length: POINTER(UInt32)) -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsIsStringEmpty(string: Windows.Win32.System.WinRT.HSTRING) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsStringHasEmbeddedNull(string: Windows.Win32.System.WinRT.HSTRING, hasEmbedNull: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsCompareStringOrdinal(string1: Windows.Win32.System.WinRT.HSTRING, string2: Windows.Win32.System.WinRT.HSTRING, result: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsSubstring(string: Windows.Win32.System.WinRT.HSTRING, startIndex: UInt32, newString: POINTER(Windows.Win32.System.WinRT.HSTRING)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsSubstringWithSpecifiedLength(string: Windows.Win32.System.WinRT.HSTRING, startIndex: UInt32, length: UInt32, newString: POINTER(Windows.Win32.System.WinRT.HSTRING)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsConcatString(string1: Windows.Win32.System.WinRT.HSTRING, string2: Windows.Win32.System.WinRT.HSTRING, newString: POINTER(Windows.Win32.System.WinRT.HSTRING)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsReplaceString(string: Windows.Win32.System.WinRT.HSTRING, stringReplaced: Windows.Win32.System.WinRT.HSTRING, stringReplaceWith: Windows.Win32.System.WinRT.HSTRING, newString: POINTER(Windows.Win32.System.WinRT.HSTRING)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsTrimStringStart(string: Windows.Win32.System.WinRT.HSTRING, trimString: Windows.Win32.System.WinRT.HSTRING, newString: POINTER(Windows.Win32.System.WinRT.HSTRING)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsTrimStringEnd(string: Windows.Win32.System.WinRT.HSTRING, trimString: Windows.Win32.System.WinRT.HSTRING, newString: POINTER(Windows.Win32.System.WinRT.HSTRING)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsPreallocateStringBuffer(length: UInt32, charBuffer: POINTER(POINTER(UInt16)), bufferHandle: POINTER(Windows.Win32.System.WinRT.HSTRING_BUFFER)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsPromoteStringBuffer(bufferHandle: Windows.Win32.System.WinRT.HSTRING_BUFFER, string: POINTER(Windows.Win32.System.WinRT.HSTRING)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsDeleteStringBuffer(bufferHandle: Windows.Win32.System.WinRT.HSTRING_BUFFER) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-0.dll')
def WindowsInspectString(targetHString: UIntPtr, machine: UInt16, callback: Windows.Win32.System.WinRT.PINSPECT_HSTRING_CALLBACK, context: c_void_p, length: POINTER(UInt32), targetStringAddress: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-string-l1-1-1.dll')
def WindowsInspectString2(targetHString: UInt64, machine: UInt16, callback: Windows.Win32.System.WinRT.PINSPECT_HSTRING_CALLBACK2, context: c_void_p, length: POINTER(UInt32), targetStringAddress: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('CoreMessaging.dll')
def CreateDispatcherQueueController(options: Windows.Win32.System.WinRT.DispatcherQueueOptions, dispatcherQueueController: POINTER(MissingType)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-l1-1-0.dll')
def RoInitialize(initType: Windows.Win32.System.WinRT.RO_INIT_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-l1-1-0.dll')
def RoUninitialize() -> Void: ...
@winfunctype('api-ms-win-core-winrt-l1-1-0.dll')
def RoActivateInstance(activatableClassId: Windows.Win32.System.WinRT.HSTRING, instance: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-l1-1-0.dll')
def RoRegisterActivationFactories(activatableClassIds: POINTER(Windows.Win32.System.WinRT.HSTRING), activationFactoryCallbacks: POINTER(Windows.Win32.System.WinRT.PFNGETACTIVATIONFACTORY), count: UInt32, cookie: POINTER(Windows.Win32.System.WinRT.RO_REGISTRATION_COOKIE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-l1-1-0.dll')
def RoRevokeActivationFactories(cookie: Windows.Win32.System.WinRT.RO_REGISTRATION_COOKIE) -> Void: ...
@winfunctype('api-ms-win-core-winrt-l1-1-0.dll')
def RoGetActivationFactory(activatableClassId: Windows.Win32.System.WinRT.HSTRING, iid: POINTER(Guid), factory: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-l1-1-0.dll')
def RoRegisterForApartmentShutdown(callbackObject: Windows.Win32.System.WinRT.IApartmentShutdown_head, apartmentIdentifier: POINTER(UInt64), regCookie: POINTER(Windows.Win32.System.WinRT.APARTMENT_SHUTDOWN_REGISTRATION_COOKIE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-l1-1-0.dll')
def RoUnregisterForApartmentShutdown(regCookie: Windows.Win32.System.WinRT.APARTMENT_SHUTDOWN_REGISTRATION_COOKIE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-l1-1-0.dll')
def RoGetApartmentIdentifier(apartmentIdentifier: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-robuffer-l1-1-0.dll')
def RoGetBufferMarshaler(bufferMarshaler: POINTER(Windows.Win32.System.Com.Marshal.IMarshal_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def RoGetErrorReportingFlags(pflags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def RoSetErrorReportingFlags(flags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def RoResolveRestrictedErrorInfoReference(reference: Windows.Win32.Foundation.PWSTR, ppRestrictedErrorInfo: POINTER(Windows.Win32.System.WinRT.IRestrictedErrorInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def SetRestrictedErrorInfo(pRestrictedErrorInfo: Windows.Win32.System.WinRT.IRestrictedErrorInfo_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def GetRestrictedErrorInfo(ppRestrictedErrorInfo: POINTER(Windows.Win32.System.WinRT.IRestrictedErrorInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def RoOriginateErrorW(error: Windows.Win32.Foundation.HRESULT, cchMax: UInt32, message: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def RoOriginateError(error: Windows.Win32.Foundation.HRESULT, message: Windows.Win32.System.WinRT.HSTRING) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def RoTransformErrorW(oldError: Windows.Win32.Foundation.HRESULT, newError: Windows.Win32.Foundation.HRESULT, cchMax: UInt32, message: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def RoTransformError(oldError: Windows.Win32.Foundation.HRESULT, newError: Windows.Win32.Foundation.HRESULT, message: Windows.Win32.System.WinRT.HSTRING) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def RoCaptureErrorContext(hr: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-0.dll')
def RoFailFastWithErrorContext(hrError: Windows.Win32.Foundation.HRESULT) -> Void: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-1.dll')
def RoOriginateLanguageException(error: Windows.Win32.Foundation.HRESULT, message: Windows.Win32.System.WinRT.HSTRING, languageException: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-1.dll')
def RoClearError() -> Void: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-1.dll')
def RoReportUnhandledError(pRestrictedErrorInfo: Windows.Win32.System.WinRT.IRestrictedErrorInfo_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-1.dll')
def RoInspectThreadErrorInfo(targetTebAddress: UIntPtr, machine: UInt16, readMemoryCallback: Windows.Win32.System.WinRT.PINSPECT_MEMORY_CALLBACK, context: c_void_p, targetErrorInfoAddress: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-1.dll')
def RoInspectCapturedStackBackTrace(targetErrorInfoAddress: UIntPtr, machine: UInt16, readMemoryCallback: Windows.Win32.System.WinRT.PINSPECT_MEMORY_CALLBACK, context: c_void_p, frameCount: POINTER(UInt32), targetBackTraceAddress: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-1.dll')
def RoGetMatchingRestrictedErrorInfo(hrIn: Windows.Win32.Foundation.HRESULT, ppRestrictedErrorInfo: POINTER(Windows.Win32.System.WinRT.IRestrictedErrorInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-1.dll')
def RoReportFailedDelegate(punkDelegate: Windows.Win32.System.Com.IUnknown_head, pRestrictedErrorInfo: Windows.Win32.System.WinRT.IRestrictedErrorInfo_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-winrt-error-l1-1-1.dll')
def IsErrorPropagationEnabled() -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-winrt-registration-l1-1-0.dll')
def RoGetServerActivatableClasses(serverName: Windows.Win32.System.WinRT.HSTRING, activatableClassIds: POINTER(POINTER(Windows.Win32.System.WinRT.HSTRING)), count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-shcore-stream-winrt-l1-1-0.dll')
def CreateRandomAccessStreamOnFile(filePath: Windows.Win32.Foundation.PWSTR, accessMode: UInt32, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-shcore-stream-winrt-l1-1-0.dll')
def CreateRandomAccessStreamOverStream(stream: Windows.Win32.System.Com.IStream_head, options: Windows.Win32.System.WinRT.BSOS_OPTIONS, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-shcore-stream-winrt-l1-1-0.dll')
def CreateStreamOverRandomAccessStream(randomAccessStream: Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@cfunctype('Windows.UI.dll')
def CreateControlInput(riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@cfunctype('Windows.UI.dll')
def CreateControlInputEx(pCoreWindow: Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
BSOS_OPTIONS = Int32
BSOS_DEFAULT: BSOS_OPTIONS = 0
BSOS_PREFERDESTINATIONSTREAM: BSOS_OPTIONS = 1
CASTING_CONNECTION_ERROR_STATUS = Int32
CASTING_CONNECTION_ERROR_STATUS_SUCCEEDED: CASTING_CONNECTION_ERROR_STATUS = 0
CASTING_CONNECTION_ERROR_STATUS_DEVICE_DID_NOT_RESPOND: CASTING_CONNECTION_ERROR_STATUS = 1
CASTING_CONNECTION_ERROR_STATUS_DEVICE_ERROR: CASTING_CONNECTION_ERROR_STATUS = 2
CASTING_CONNECTION_ERROR_STATUS_DEVICE_LOCKED: CASTING_CONNECTION_ERROR_STATUS = 3
CASTING_CONNECTION_ERROR_STATUS_PROTECTED_PLAYBACK_FAILED: CASTING_CONNECTION_ERROR_STATUS = 4
CASTING_CONNECTION_ERROR_STATUS_INVALID_CASTING_SOURCE: CASTING_CONNECTION_ERROR_STATUS = 5
CASTING_CONNECTION_ERROR_STATUS_UNKNOWN: CASTING_CONNECTION_ERROR_STATUS = 6
CASTING_CONNECTION_STATE = Int32
CASTING_CONNECTION_STATE_DISCONNECTED: CASTING_CONNECTION_STATE = 0
CASTING_CONNECTION_STATE_CONNECTED: CASTING_CONNECTION_STATE = 1
CASTING_CONNECTION_STATE_RENDERING: CASTING_CONNECTION_STATE = 2
CASTING_CONNECTION_STATE_DISCONNECTING: CASTING_CONNECTION_STATE = 3
CASTING_CONNECTION_STATE_CONNECTING: CASTING_CONNECTION_STATE = 4
DISPATCHERQUEUE_THREAD_APARTMENTTYPE = Int32
DQTAT_COM_NONE: DISPATCHERQUEUE_THREAD_APARTMENTTYPE = 0
DQTAT_COM_ASTA: DISPATCHERQUEUE_THREAD_APARTMENTTYPE = 1
DQTAT_COM_STA: DISPATCHERQUEUE_THREAD_APARTMENTTYPE = 2
DISPATCHERQUEUE_THREAD_TYPE = Int32
DQTYPE_THREAD_DEDICATED: DISPATCHERQUEUE_THREAD_TYPE = 1
DQTYPE_THREAD_CURRENT: DISPATCHERQUEUE_THREAD_TYPE = 2
class DispatcherQueueOptions(EasyCastStructure):
    dwSize: UInt32
    threadType: Windows.Win32.System.WinRT.DISPATCHERQUEUE_THREAD_TYPE
    apartmentType: Windows.Win32.System.WinRT.DISPATCHERQUEUE_THREAD_APARTMENTTYPE
class EventRegistrationToken(EasyCastStructure):
    value: Int64
HSTRING = IntPtr
HSTRING_BUFFER = IntPtr
class HSTRING_HEADER(EasyCastStructure):
    flags: UInt32
    length: UInt32
    padding1: UInt32
    padding2: UInt32
    data: IntPtr
class IAccountsSettingsPaneInterop(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{d3ee12ad-3865-4362-9746-b75a682df0e6}')
    @commethod(6)
    def GetForWindow(self, appWindow: Windows.Win32.Foundation.HWND, riid: POINTER(Guid), accountsSettingsPane: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ShowManageAccountsForWindowAsync(self, appWindow: Windows.Win32.Foundation.HWND, riid: POINTER(Guid), asyncAction: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ShowAddAccountForWindowAsync(self, appWindow: Windows.Win32.Foundation.HWND, riid: POINTER(Guid), asyncAction: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IActivationFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{00000035-0000-0000-c000-000000000046}')
    @commethod(6)
    def ActivateInstance(self, instance: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAgileReference(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c03f6a43-65a4-9818-987e-e0b810d2a6f2}')
    @commethod(3)
    def Resolve(self, riid: POINTER(Guid), ppvObjectReference: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IApartmentShutdown(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a2f05a09-27a2-42b5-bc0e-ac163ef49d9b}')
    @commethod(3)
    def OnUninitialize(self, ui64ApartmentIdentifier: UInt64) -> Void: ...
class IAppServiceConnectionExtendedExecution(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{65219584-f9cb-4ae3-81f9-a28a6ca450d9}')
    @commethod(3)
    def OpenForExtendedExecutionAsync(self, riid: POINTER(Guid), operation: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IBufferByteAccess(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{905a0fef-bc53-11df-8c49-001e4fc686da}')
    @commethod(3)
    def Buffer(self, value: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
class ICastingController(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f0a56423-a664-4fbd-8b43-409a45e8d9a1}')
    @commethod(3)
    def Initialize(self, castingEngine: Windows.Win32.System.Com.IUnknown_head, castingSource: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Connect(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Disconnect(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Advise(self, eventHandler: Windows.Win32.System.WinRT.ICastingEventHandler_head, cookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UnAdvise(self, cookie: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ICastingEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c79a6cb7-bebd-47a6-a2ad-4d45ad79c7bc}')
    @commethod(3)
    def OnStateChanged(self, newState: Windows.Win32.System.WinRT.CASTING_CONNECTION_STATE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnError(self, errorStatus: Windows.Win32.System.WinRT.CASTING_CONNECTION_ERROR_STATUS, errorMessage: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ICastingSourceInfo(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{45101ab7-7c3a-4bce-9500-12c09024b298}')
    @commethod(3)
    def GetController(self, controller: POINTER(Windows.Win32.System.WinRT.ICastingController_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetProperties(self, props: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.INamedPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ICoreInputInterop(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{40bfe3e3-b75a-4479-ac96-475365749bb8}')
    @commethod(3)
    def SetInputSource(self, value: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_MessageHandled(self, value: Byte) -> Windows.Win32.Foundation.HRESULT: ...
class ICoreWindowAdapterInterop(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{7a5b6fd1-cd73-4b6c-9cf4-2e869eaf470a}')
    @commethod(6)
    def get_AppActivationClientAdapter(self, value: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_ApplicationViewClientAdapter(self, value: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_CoreApplicationViewClientAdapter(self, value: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_HoloViewClientAdapter(self, value: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_PositionerClientAdapter(self, value: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_SystemNavigationClientAdapter(self, value: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_TitleBarClientAdapter(self, value: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetWindowClientAdapter(self, value: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class ICoreWindowComponentInterop(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0576ab31-a310-4c40-ba31-fd37e0298dfa}')
    @commethod(3)
    def ConfigureComponentInput(self, hostViewInstanceId: UInt32, hwndHost: Windows.Win32.Foundation.HWND, inputSourceVisual: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetViewInstanceId(self, componentViewInstanceId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ICoreWindowInterop(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{45d64a29-a63e-4cb6-b498-5781d298cb4f}')
    @commethod(3)
    def get_WindowHandle(self, hwnd: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_MessageHandled(self, value: Byte) -> Windows.Win32.Foundation.HRESULT: ...
class ICorrelationVectorInformation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{83c78b3c-d88b-4950-aa6e-22b8d22aabd3}')
    @commethod(6)
    def get_LastCorrelationVectorForThread(self, cv: POINTER(Windows.Win32.System.WinRT.HSTRING)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_NextCorrelationVectorForThread(self, cv: POINTER(Windows.Win32.System.WinRT.HSTRING)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_NextCorrelationVectorForThread(self, cv: Windows.Win32.System.WinRT.HSTRING) -> Windows.Win32.Foundation.HRESULT: ...
class ICorrelationVectorSource(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{152b8a3b-b9b9-4685-b56e-974847bc7545}')
    @commethod(3)
    def get_CorrelationVector(self, cv: POINTER(Windows.Win32.System.WinRT.HSTRING)) -> Windows.Win32.Foundation.HRESULT: ...
class IDragDropManagerInterop(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{5ad8cba7-4c01-4dac-9074-827894292d63}')
    @commethod(6)
    def GetForWindow(self, hwnd: Windows.Win32.Foundation.HWND, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IHolographicSpaceInterop(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{5c4ee536-6a98-4b86-a170-587013d6fd4b}')
    @commethod(6)
    def CreateForWindow(self, window: Windows.Win32.Foundation.HWND, riid: POINTER(Guid), holographicSpace: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IInputPaneInterop(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{75cf2c57-9195-4931-8332-f0b409e916af}')
    @commethod(6)
    def GetForWindow(self, appWindow: Windows.Win32.Foundation.HWND, riid: POINTER(Guid), inputPane: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IInspectable(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{af86e2e0-b12d-4c6a-9c5a-d7aa65101e90}')
    @commethod(3)
    def GetIids(self, iidCount: POINTER(UInt32), iids: POINTER(POINTER(Guid))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetRuntimeClassName(self, className: POINTER(Windows.Win32.System.WinRT.HSTRING)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTrustLevel(self, trustLevel: POINTER(Windows.Win32.System.WinRT.TrustLevel)) -> Windows.Win32.Foundation.HRESULT: ...
class ILanguageExceptionErrorInfo(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{04a2dbf3-df83-116c-0946-0812abf6e07d}')
    @commethod(3)
    def GetLanguageException(self, languageException: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ILanguageExceptionErrorInfo2(ComPtr):
    extends: Windows.Win32.System.WinRT.ILanguageExceptionErrorInfo
    _iid_ = Guid('{5746e5c4-5b97-424c-b620-2822915734dd}')
    @commethod(4)
    def GetPreviousLanguageExceptionErrorInfo(self, previousLanguageExceptionErrorInfo: POINTER(Windows.Win32.System.WinRT.ILanguageExceptionErrorInfo2_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CapturePropagationContext(self, languageException: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPropagationContextHead(self, propagatedLanguageExceptionErrorInfoHead: POINTER(Windows.Win32.System.WinRT.ILanguageExceptionErrorInfo2_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ILanguageExceptionStackBackTrace(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cbe53fb5-f967-4258-8d34-42f5e25833de}')
    @commethod(3)
    def GetStackBackTrace(self, maxFramesToCapture: UInt32, stackBackTrace: POINTER(UIntPtr), framesCaptured: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ILanguageExceptionTransform(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{feb5a271-a6cd-45ce-880a-696706badc65}')
    @commethod(3)
    def GetTransformedRestrictedErrorInfo(self, restrictedErrorInfo: POINTER(Windows.Win32.System.WinRT.IRestrictedErrorInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMemoryBufferByteAccess(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5b0d3235-4dba-4d44-865e-8f1d0e4fd04d}')
    @commethod(3)
    def GetBuffer(self, value: POINTER(POINTER(Byte)), capacity: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMessageDispatcher(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f5f84c8f-cfd0-4cd6-b66b-c5d26ff1689d}')
    @commethod(6)
    def PumpMessages(self) -> Windows.Win32.Foundation.HRESULT: ...
class IPlayToManagerInterop(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{24394699-1f2c-4eb3-8cd7-0ec1da42a540}')
    @commethod(6)
    def GetForWindow(self, appWindow: Windows.Win32.Foundation.HWND, riid: POINTER(Guid), playToManager: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ShowPlayToUIForWindow(self, appWindow: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
class IRestrictedErrorInfo(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{82ba7092-4c88-427d-a7bc-16dd93feb67e}')
    @commethod(3)
    def GetErrorDetails(self, description: POINTER(Windows.Win32.Foundation.BSTR), error: POINTER(Windows.Win32.Foundation.HRESULT), restrictedDescription: POINTER(Windows.Win32.Foundation.BSTR), capabilitySid: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetReference(self, reference: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IShareWindowCommandEventArgsInterop(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6571a721-643d-43d4-aca4-6b6f5f30f1ad}')
    @commethod(3)
    def GetWindow(self, value: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
class IShareWindowCommandSourceInterop(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{461a191f-8424-43a6-a0fa-3451a22f56ab}')
    @commethod(3)
    def GetForWindow(self, appWindow: Windows.Win32.Foundation.HWND, riid: POINTER(Guid), shareWindowCommandSource: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpatialInteractionManagerInterop(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{5c4ee536-6a98-4b86-a170-587013d6fd4b}')
    @commethod(6)
    def GetForWindow(self, window: Windows.Win32.Foundation.HWND, riid: POINTER(Guid), spatialInteractionManager: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class ISystemMediaTransportControlsInterop(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{ddb0472d-c911-4a1f-86d9-dc3d71a95f5a}')
    @commethod(6)
    def GetForWindow(self, appWindow: Windows.Win32.Foundation.HWND, riid: POINTER(Guid), mediaTransportControl: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IUIViewSettingsInterop(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{3694dbf9-8f68-44be-8ff5-195c98ede8a6}')
    @commethod(6)
    def GetForWindow(self, hwnd: Windows.Win32.Foundation.HWND, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IUserActivityInterop(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{1ade314d-0e0a-40d9-824c-9a088a50059f}')
    @commethod(6)
    def CreateSessionForWindow(self, window: Windows.Win32.Foundation.HWND, iid: POINTER(Guid), value: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IUserActivityRequestManagerInterop(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{dd69f876-9699-4715-9095-e37ea30dfa1b}')
    @commethod(6)
    def GetForWindow(self, window: Windows.Win32.Foundation.HWND, iid: POINTER(Guid), value: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IUserActivitySourceHostInterop(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c15df8bc-8844-487a-b85b-7578e0f61419}')
    @commethod(6)
    def SetActivitySourceHost(self, activitySourceHost: Windows.Win32.System.WinRT.HSTRING) -> Windows.Win32.Foundation.HRESULT: ...
class IUserConsentVerifierInterop(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{39e050c3-4e74-441a-8dc0-b81104df949c}')
    @commethod(6)
    def RequestVerificationForWindowAsync(self, appWindow: Windows.Win32.Foundation.HWND, message: Windows.Win32.System.WinRT.HSTRING, riid: POINTER(Guid), asyncOperation: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IWeakReference(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000037-0000-0000-c000-000000000046}')
    @commethod(3)
    def Resolve(self, riid: POINTER(Guid), objectReference: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IWeakReferenceSource(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000038-0000-0000-c000-000000000046}')
    @commethod(3)
    def GetWeakReference(self, weakReference: POINTER(Windows.Win32.System.WinRT.IWeakReference_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWebAuthenticationCoreManagerInterop(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{f4b8e804-811e-4436-b69c-44cb67b72084}')
    @commethod(6)
    def RequestTokenForWindowAsync(self, appWindow: Windows.Win32.Foundation.HWND, request: Windows.Win32.System.WinRT.IInspectable_head, riid: POINTER(Guid), asyncInfo: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RequestTokenWithWebAccountForWindowAsync(self, appWindow: Windows.Win32.Foundation.HWND, request: Windows.Win32.System.WinRT.IInspectable_head, webAccount: Windows.Win32.System.WinRT.IInspectable_head, riid: POINTER(Guid), asyncInfo: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNGETACTIVATIONFACTORY(param0: Windows.Win32.System.WinRT.HSTRING, param1: POINTER(Windows.Win32.System.WinRT.IActivationFactory_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PINSPECT_HSTRING_CALLBACK(context: c_void_p, readAddress: UIntPtr, length: UInt32, buffer: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PINSPECT_HSTRING_CALLBACK2(context: c_void_p, readAddress: UInt64, length: UInt32, buffer: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PINSPECT_MEMORY_CALLBACK(context: c_void_p, readAddress: UIntPtr, length: UInt32, buffer: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
ROPARAMIIDHANDLE = IntPtr
RO_ERROR_REPORTING_FLAGS = Int32
RO_ERROR_REPORTING_NONE: RO_ERROR_REPORTING_FLAGS = 0
RO_ERROR_REPORTING_SUPPRESSEXCEPTIONS: RO_ERROR_REPORTING_FLAGS = 1
RO_ERROR_REPORTING_FORCEEXCEPTIONS: RO_ERROR_REPORTING_FLAGS = 2
RO_ERROR_REPORTING_USESETERRORINFO: RO_ERROR_REPORTING_FLAGS = 4
RO_ERROR_REPORTING_SUPPRESSSETERRORINFO: RO_ERROR_REPORTING_FLAGS = 8
RO_INIT_TYPE = Int32
RO_INIT_SINGLETHREADED: RO_INIT_TYPE = 0
RO_INIT_MULTITHREADED: RO_INIT_TYPE = 1
RO_REGISTRATION_COOKIE = IntPtr
class ServerInformation(EasyCastStructure):
    dwServerPid: UInt32
    dwServerTid: UInt32
    ui64ServerAddress: UInt64
TrustLevel = Int32
TrustLevel_BaseTrust: TrustLevel = 0
TrustLevel_PartialTrust: TrustLevel = 1
TrustLevel_FullTrust: TrustLevel = 2
make_head(_module, 'DispatcherQueueOptions')
make_head(_module, 'EventRegistrationToken')
make_head(_module, 'HSTRING_HEADER')
make_head(_module, 'IAccountsSettingsPaneInterop')
make_head(_module, 'IActivationFactory')
make_head(_module, 'IAgileReference')
make_head(_module, 'IApartmentShutdown')
make_head(_module, 'IAppServiceConnectionExtendedExecution')
make_head(_module, 'IBufferByteAccess')
make_head(_module, 'ICastingController')
make_head(_module, 'ICastingEventHandler')
make_head(_module, 'ICastingSourceInfo')
make_head(_module, 'ICoreInputInterop')
make_head(_module, 'ICoreWindowAdapterInterop')
make_head(_module, 'ICoreWindowComponentInterop')
make_head(_module, 'ICoreWindowInterop')
make_head(_module, 'ICorrelationVectorInformation')
make_head(_module, 'ICorrelationVectorSource')
make_head(_module, 'IDragDropManagerInterop')
make_head(_module, 'IHolographicSpaceInterop')
make_head(_module, 'IInputPaneInterop')
make_head(_module, 'IInspectable')
make_head(_module, 'ILanguageExceptionErrorInfo')
make_head(_module, 'ILanguageExceptionErrorInfo2')
make_head(_module, 'ILanguageExceptionStackBackTrace')
make_head(_module, 'ILanguageExceptionTransform')
make_head(_module, 'IMemoryBufferByteAccess')
make_head(_module, 'IMessageDispatcher')
make_head(_module, 'IPlayToManagerInterop')
make_head(_module, 'IRestrictedErrorInfo')
make_head(_module, 'IShareWindowCommandEventArgsInterop')
make_head(_module, 'IShareWindowCommandSourceInterop')
make_head(_module, 'ISpatialInteractionManagerInterop')
make_head(_module, 'ISystemMediaTransportControlsInterop')
make_head(_module, 'IUIViewSettingsInterop')
make_head(_module, 'IUserActivityInterop')
make_head(_module, 'IUserActivityRequestManagerInterop')
make_head(_module, 'IUserActivitySourceHostInterop')
make_head(_module, 'IUserConsentVerifierInterop')
make_head(_module, 'IWeakReference')
make_head(_module, 'IWeakReferenceSource')
make_head(_module, 'IWebAuthenticationCoreManagerInterop')
make_head(_module, 'PFNGETACTIVATIONFACTORY')
make_head(_module, 'PINSPECT_HSTRING_CALLBACK')
make_head(_module, 'PINSPECT_HSTRING_CALLBACK2')
make_head(_module, 'PINSPECT_MEMORY_CALLBACK')
make_head(_module, 'ServerInformation')
