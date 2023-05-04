from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.ApplicationModel.DataTransfer
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Storage.Streams
import Windows.UI
import Windows.Web
import Windows.Web.Http
import Windows.Web.UI
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class IWebViewControl(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{3f921316-bc70-4bda-9136-c94370899fab}')
    @winrt_commethod(6)
    def get_Source(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def put_Source(self, source: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(8)
    def get_DocumentTitle(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_CanGoBack(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_CanGoForward(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_DefaultBackgroundColor(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(12)
    def get_DefaultBackgroundColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(13)
    def get_ContainsFullScreenElement(self) -> Boolean: ...
    @winrt_commethod(14)
    def get_Settings(self) -> Windows.Web.UI.WebViewControlSettings: ...
    @winrt_commethod(15)
    def get_DeferredPermissionRequests(self) -> Windows.Foundation.Collections.IVectorView[Windows.Web.UI.WebViewControlDeferredPermissionRequest]: ...
    @winrt_commethod(16)
    def GoForward(self) -> Void: ...
    @winrt_commethod(17)
    def GoBack(self) -> Void: ...
    @winrt_commethod(18)
    def Refresh(self) -> Void: ...
    @winrt_commethod(19)
    def Stop(self) -> Void: ...
    @winrt_commethod(20)
    def Navigate(self, source: Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(21)
    def NavigateToString(self, text: WinRT_String) -> Void: ...
    @winrt_commethod(22)
    def NavigateToLocalStreamUri(self, source: Windows.Foundation.Uri, streamResolver: Windows.Web.IUriToStreamResolver) -> Void: ...
    @winrt_commethod(23)
    def NavigateWithHttpRequestMessage(self, requestMessage: Windows.Web.Http.HttpRequestMessage) -> Void: ...
    @winrt_commethod(24)
    def InvokeScriptAsync(self, scriptName: WinRT_String, arguments: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(25)
    def CapturePreviewToStreamAsync(self, stream: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(26)
    def CaptureSelectedContentToDataPackageAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.DataTransfer.DataPackage]: ...
    @winrt_commethod(27)
    def BuildLocalStreamUri(self, contentIdentifier: WinRT_String, relativePath: WinRT_String) -> Windows.Foundation.Uri: ...
    @winrt_commethod(28)
    def GetDeferredPermissionRequestById(self, id: UInt32, result: POINTER(Windows.Web.UI.WebViewControlDeferredPermissionRequest)) -> Void: ...
    @winrt_commethod(29)
    def add_NavigationStarting(self, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlNavigationStartingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(30)
    def remove_NavigationStarting(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(31)
    def add_ContentLoading(self, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlContentLoadingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(32)
    def remove_ContentLoading(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(33)
    def add_DOMContentLoaded(self, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlDOMContentLoadedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(34)
    def remove_DOMContentLoaded(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(35)
    def add_NavigationCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlNavigationCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(36)
    def remove_NavigationCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(37)
    def add_FrameNavigationStarting(self, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlNavigationStartingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(38)
    def remove_FrameNavigationStarting(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(39)
    def add_FrameContentLoading(self, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlContentLoadingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(40)
    def remove_FrameContentLoading(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(41)
    def add_FrameDOMContentLoaded(self, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlDOMContentLoadedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(42)
    def remove_FrameDOMContentLoaded(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(43)
    def add_FrameNavigationCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlNavigationCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(44)
    def remove_FrameNavigationCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(45)
    def add_ScriptNotify(self, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlScriptNotifyEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(46)
    def remove_ScriptNotify(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(47)
    def add_LongRunningScriptDetected(self, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlLongRunningScriptDetectedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(48)
    def remove_LongRunningScriptDetected(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(49)
    def add_UnsafeContentWarningDisplaying(self, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(50)
    def remove_UnsafeContentWarningDisplaying(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(51)
    def add_UnviewableContentIdentified(self, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlUnviewableContentIdentifiedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(52)
    def remove_UnviewableContentIdentified(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(53)
    def add_PermissionRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlPermissionRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(54)
    def remove_PermissionRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(55)
    def add_UnsupportedUriSchemeIdentified(self, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlUnsupportedUriSchemeIdentifiedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(56)
    def remove_UnsupportedUriSchemeIdentified(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(57)
    def add_NewWindowRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlNewWindowRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(58)
    def remove_NewWindowRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(59)
    def add_ContainsFullScreenElementChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(60)
    def remove_ContainsFullScreenElementChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(61)
    def add_WebResourceRequested(self, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlWebResourceRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(62)
    def remove_WebResourceRequested(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    Source = property(get_Source, put_Source)
    DocumentTitle = property(get_DocumentTitle, None)
    CanGoBack = property(get_CanGoBack, None)
    CanGoForward = property(get_CanGoForward, None)
    DefaultBackgroundColor = property(get_DefaultBackgroundColor, put_DefaultBackgroundColor)
    ContainsFullScreenElement = property(get_ContainsFullScreenElement, None)
    Settings = property(get_Settings, None)
    DeferredPermissionRequests = property(get_DeferredPermissionRequests, None)
class IWebViewControl2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{4d3c06f9-c8df-41cc-8bd5-2a947b204503}')
    @winrt_commethod(6)
    def AddInitializeScript(self, script: WinRT_String) -> Void: ...
class IWebViewControlContentLoadingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{9a3fccb2-b9bb-404b-a22b-66dccd1250c6}')
    @winrt_commethod(6)
    def get_Uri(self) -> Windows.Foundation.Uri: ...
    Uri = property(get_Uri, None)
class IWebViewControlDOMContentLoadedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{be8bc008-9541-4545-9ff2-2df585b29f7d}')
    @winrt_commethod(6)
    def get_Uri(self) -> Windows.Foundation.Uri: ...
    Uri = property(get_Uri, None)
class IWebViewControlDeferredPermissionRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{2ce349e0-d759-445c-9926-8995298f152b}')
    @winrt_commethod(6)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Uri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(8)
    def get_PermissionType(self) -> Windows.Web.UI.WebViewControlPermissionType: ...
    @winrt_commethod(9)
    def Allow(self) -> Void: ...
    @winrt_commethod(10)
    def Deny(self) -> Void: ...
    Id = property(get_Id, None)
    Uri = property(get_Uri, None)
    PermissionType = property(get_PermissionType, None)
class IWebViewControlLongRunningScriptDetectedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{2a6e5bba-98b4-45bc-bbeb-0f69ce49c599}')
    @winrt_commethod(6)
    def get_ExecutionTime(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def get_StopPageScriptExecution(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_StopPageScriptExecution(self, value: Boolean) -> Void: ...
    ExecutionTime = property(get_ExecutionTime, None)
    StopPageScriptExecution = property(get_StopPageScriptExecution, put_StopPageScriptExecution)
class IWebViewControlNavigationCompletedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{20409918-4a15-4c46-a55d-f79edb0bde8b}')
    @winrt_commethod(6)
    def get_Uri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def get_IsSuccess(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_WebErrorStatus(self) -> Windows.Web.WebErrorStatus: ...
    Uri = property(get_Uri, None)
    IsSuccess = property(get_IsSuccess, None)
    WebErrorStatus = property(get_WebErrorStatus, None)
class IWebViewControlNavigationStartingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{0c9057c5-0a08-41c7-863b-71e3a9549137}')
    @winrt_commethod(6)
    def get_Uri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def get_Cancel(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Cancel(self, value: Boolean) -> Void: ...
    Uri = property(get_Uri, None)
    Cancel = property(get_Cancel, put_Cancel)
class IWebViewControlNewWindowRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{3df44bbb-a124-46d5-a083-d02cacdff5ad}')
    @winrt_commethod(6)
    def get_Uri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def get_Referrer(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(8)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Handled(self, value: Boolean) -> Void: ...
    Uri = property(get_Uri, None)
    Referrer = property(get_Referrer, None)
    Handled = property(get_Handled, put_Handled)
class IWebViewControlNewWindowRequestedEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{b53c5ca6-2aae-4bfc-92b9-c30e92b48098}')
    @winrt_commethod(6)
    def get_NewWindow(self) -> Windows.Web.UI.IWebViewControl: ...
    @winrt_commethod(7)
    def put_NewWindow(self, value: Windows.Web.UI.IWebViewControl) -> Void: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    NewWindow = property(get_NewWindow, put_NewWindow)
class IWebViewControlPermissionRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{e5bc836c-f22f-40e2-95b2-7729f840eb7f}')
    @winrt_commethod(6)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Uri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(8)
    def get_PermissionType(self) -> Windows.Web.UI.WebViewControlPermissionType: ...
    @winrt_commethod(9)
    def get_State(self) -> Windows.Web.UI.WebViewControlPermissionState: ...
    @winrt_commethod(10)
    def Defer(self) -> Void: ...
    @winrt_commethod(11)
    def Allow(self) -> Void: ...
    @winrt_commethod(12)
    def Deny(self) -> Void: ...
    Id = property(get_Id, None)
    Uri = property(get_Uri, None)
    PermissionType = property(get_PermissionType, None)
    State = property(get_State, None)
class IWebViewControlPermissionRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{27204d51-2488-4cc5-968e-0a771e59c147}')
    @winrt_commethod(6)
    def get_PermissionRequest(self) -> Windows.Web.UI.WebViewControlPermissionRequest: ...
    PermissionRequest = property(get_PermissionRequest, None)
class IWebViewControlScriptNotifyEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{491de57b-6f49-41bb-b591-51b85b817037}')
    @winrt_commethod(6)
    def get_Uri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def get_Value(self) -> WinRT_String: ...
    Uri = property(get_Uri, None)
    Value = property(get_Value, None)
class IWebViewControlSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{c9967fbf-5e98-4cfd-8cce-27b0911e3de8}')
    @winrt_commethod(6)
    def put_IsJavaScriptEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_IsJavaScriptEnabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_IsIndexedDBEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_IsIndexedDBEnabled(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_IsScriptNotifyAllowed(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_IsScriptNotifyAllowed(self) -> Boolean: ...
    IsJavaScriptEnabled = property(get_IsJavaScriptEnabled, put_IsJavaScriptEnabled)
    IsIndexedDBEnabled = property(get_IsIndexedDBEnabled, put_IsIndexedDBEnabled)
    IsScriptNotifyAllowed = property(get_IsScriptNotifyAllowed, put_IsScriptNotifyAllowed)
class IWebViewControlUnsupportedUriSchemeIdentifiedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{e3b81944-e4fc-43dc-94ca-f980f30bc51d}')
    @winrt_commethod(6)
    def get_Uri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Handled(self, value: Boolean) -> Void: ...
    Uri = property(get_Uri, None)
    Handled = property(get_Handled, put_Handled)
class IWebViewControlUnviewableContentIdentifiedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{4a9680db-88f2-4e20-b693-b4e2df4aa581}')
    @winrt_commethod(6)
    def get_Uri(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def get_Referrer(self) -> Windows.Foundation.Uri: ...
    @winrt_commethod(8)
    def get_MediaType(self) -> WinRT_String: ...
    Uri = property(get_Uri, None)
    Referrer = property(get_Referrer, None)
    MediaType = property(get_MediaType, None)
class IWebViewControlWebResourceRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('{44d6524d-55a4-4d8b-891c-931d8e25d42e}')
    @winrt_commethod(6)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    @winrt_commethod(7)
    def get_Request(self) -> Windows.Web.Http.HttpRequestMessage: ...
    @winrt_commethod(8)
    def put_Response(self, value: Windows.Web.Http.HttpResponseMessage) -> Void: ...
    @winrt_commethod(9)
    def get_Response(self) -> Windows.Web.Http.HttpResponseMessage: ...
    Request = property(get_Request, None)
    Response = property(get_Response, put_Response)
class WebViewControlContentLoadingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Web.UI.IWebViewControlContentLoadingEventArgs
    _classid_ = 'Windows.Web.UI.WebViewControlContentLoadingEventArgs'
    @winrt_mixinmethod
    def get_Uri(self: Windows.Web.UI.IWebViewControlContentLoadingEventArgs) -> Windows.Foundation.Uri: ...
    Uri = property(get_Uri, None)
class WebViewControlDOMContentLoadedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Web.UI.IWebViewControlDOMContentLoadedEventArgs
    _classid_ = 'Windows.Web.UI.WebViewControlDOMContentLoadedEventArgs'
    @winrt_mixinmethod
    def get_Uri(self: Windows.Web.UI.IWebViewControlDOMContentLoadedEventArgs) -> Windows.Foundation.Uri: ...
    Uri = property(get_Uri, None)
class WebViewControlDeferredPermissionRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Web.UI.IWebViewControlDeferredPermissionRequest
    _classid_ = 'Windows.Web.UI.WebViewControlDeferredPermissionRequest'
    @winrt_mixinmethod
    def get_Id(self: Windows.Web.UI.IWebViewControlDeferredPermissionRequest) -> UInt32: ...
    @winrt_mixinmethod
    def get_Uri(self: Windows.Web.UI.IWebViewControlDeferredPermissionRequest) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_PermissionType(self: Windows.Web.UI.IWebViewControlDeferredPermissionRequest) -> Windows.Web.UI.WebViewControlPermissionType: ...
    @winrt_mixinmethod
    def Allow(self: Windows.Web.UI.IWebViewControlDeferredPermissionRequest) -> Void: ...
    @winrt_mixinmethod
    def Deny(self: Windows.Web.UI.IWebViewControlDeferredPermissionRequest) -> Void: ...
    Id = property(get_Id, None)
    Uri = property(get_Uri, None)
    PermissionType = property(get_PermissionType, None)
class WebViewControlLongRunningScriptDetectedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Web.UI.IWebViewControlLongRunningScriptDetectedEventArgs
    _classid_ = 'Windows.Web.UI.WebViewControlLongRunningScriptDetectedEventArgs'
    @winrt_mixinmethod
    def get_ExecutionTime(self: Windows.Web.UI.IWebViewControlLongRunningScriptDetectedEventArgs) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_StopPageScriptExecution(self: Windows.Web.UI.IWebViewControlLongRunningScriptDetectedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_StopPageScriptExecution(self: Windows.Web.UI.IWebViewControlLongRunningScriptDetectedEventArgs, value: Boolean) -> Void: ...
    ExecutionTime = property(get_ExecutionTime, None)
    StopPageScriptExecution = property(get_StopPageScriptExecution, put_StopPageScriptExecution)
class WebViewControlNavigationCompletedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Web.UI.IWebViewControlNavigationCompletedEventArgs
    _classid_ = 'Windows.Web.UI.WebViewControlNavigationCompletedEventArgs'
    @winrt_mixinmethod
    def get_Uri(self: Windows.Web.UI.IWebViewControlNavigationCompletedEventArgs) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_IsSuccess(self: Windows.Web.UI.IWebViewControlNavigationCompletedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_WebErrorStatus(self: Windows.Web.UI.IWebViewControlNavigationCompletedEventArgs) -> Windows.Web.WebErrorStatus: ...
    Uri = property(get_Uri, None)
    IsSuccess = property(get_IsSuccess, None)
    WebErrorStatus = property(get_WebErrorStatus, None)
class WebViewControlNavigationStartingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Web.UI.IWebViewControlNavigationStartingEventArgs
    _classid_ = 'Windows.Web.UI.WebViewControlNavigationStartingEventArgs'
    @winrt_mixinmethod
    def get_Uri(self: Windows.Web.UI.IWebViewControlNavigationStartingEventArgs) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Cancel(self: Windows.Web.UI.IWebViewControlNavigationStartingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Cancel(self: Windows.Web.UI.IWebViewControlNavigationStartingEventArgs, value: Boolean) -> Void: ...
    Uri = property(get_Uri, None)
    Cancel = property(get_Cancel, put_Cancel)
class WebViewControlNewWindowRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Web.UI.IWebViewControlNewWindowRequestedEventArgs
    _classid_ = 'Windows.Web.UI.WebViewControlNewWindowRequestedEventArgs'
    @winrt_mixinmethod
    def get_Uri(self: Windows.Web.UI.IWebViewControlNewWindowRequestedEventArgs) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Referrer(self: Windows.Web.UI.IWebViewControlNewWindowRequestedEventArgs) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.Web.UI.IWebViewControlNewWindowRequestedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.Web.UI.IWebViewControlNewWindowRequestedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_NewWindow(self: Windows.Web.UI.IWebViewControlNewWindowRequestedEventArgs2) -> Windows.Web.UI.IWebViewControl: ...
    @winrt_mixinmethod
    def put_NewWindow(self: Windows.Web.UI.IWebViewControlNewWindowRequestedEventArgs2, value: Windows.Web.UI.IWebViewControl) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Web.UI.IWebViewControlNewWindowRequestedEventArgs2) -> Windows.Foundation.Deferral: ...
    Uri = property(get_Uri, None)
    Referrer = property(get_Referrer, None)
    Handled = property(get_Handled, put_Handled)
    NewWindow = property(get_NewWindow, put_NewWindow)
class WebViewControlPermissionRequest(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Web.UI.IWebViewControlPermissionRequest
    _classid_ = 'Windows.Web.UI.WebViewControlPermissionRequest'
    @winrt_mixinmethod
    def get_Id(self: Windows.Web.UI.IWebViewControlPermissionRequest) -> UInt32: ...
    @winrt_mixinmethod
    def get_Uri(self: Windows.Web.UI.IWebViewControlPermissionRequest) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_PermissionType(self: Windows.Web.UI.IWebViewControlPermissionRequest) -> Windows.Web.UI.WebViewControlPermissionType: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Web.UI.IWebViewControlPermissionRequest) -> Windows.Web.UI.WebViewControlPermissionState: ...
    @winrt_mixinmethod
    def Defer(self: Windows.Web.UI.IWebViewControlPermissionRequest) -> Void: ...
    @winrt_mixinmethod
    def Allow(self: Windows.Web.UI.IWebViewControlPermissionRequest) -> Void: ...
    @winrt_mixinmethod
    def Deny(self: Windows.Web.UI.IWebViewControlPermissionRequest) -> Void: ...
    Id = property(get_Id, None)
    Uri = property(get_Uri, None)
    PermissionType = property(get_PermissionType, None)
    State = property(get_State, None)
class WebViewControlPermissionRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Web.UI.IWebViewControlPermissionRequestedEventArgs
    _classid_ = 'Windows.Web.UI.WebViewControlPermissionRequestedEventArgs'
    @winrt_mixinmethod
    def get_PermissionRequest(self: Windows.Web.UI.IWebViewControlPermissionRequestedEventArgs) -> Windows.Web.UI.WebViewControlPermissionRequest: ...
    PermissionRequest = property(get_PermissionRequest, None)
WebViewControlPermissionState = Int32
WebViewControlPermissionState_Unknown: WebViewControlPermissionState = 0
WebViewControlPermissionState_Defer: WebViewControlPermissionState = 1
WebViewControlPermissionState_Allow: WebViewControlPermissionState = 2
WebViewControlPermissionState_Deny: WebViewControlPermissionState = 3
WebViewControlPermissionType = Int32
WebViewControlPermissionType_Geolocation: WebViewControlPermissionType = 0
WebViewControlPermissionType_UnlimitedIndexedDBQuota: WebViewControlPermissionType = 1
WebViewControlPermissionType_Media: WebViewControlPermissionType = 2
WebViewControlPermissionType_PointerLock: WebViewControlPermissionType = 3
WebViewControlPermissionType_WebNotifications: WebViewControlPermissionType = 4
WebViewControlPermissionType_Screen: WebViewControlPermissionType = 5
WebViewControlPermissionType_ImmersiveView: WebViewControlPermissionType = 6
class WebViewControlScriptNotifyEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Web.UI.IWebViewControlScriptNotifyEventArgs
    _classid_ = 'Windows.Web.UI.WebViewControlScriptNotifyEventArgs'
    @winrt_mixinmethod
    def get_Uri(self: Windows.Web.UI.IWebViewControlScriptNotifyEventArgs) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.Web.UI.IWebViewControlScriptNotifyEventArgs) -> WinRT_String: ...
    Uri = property(get_Uri, None)
    Value = property(get_Value, None)
class WebViewControlSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Web.UI.IWebViewControlSettings
    _classid_ = 'Windows.Web.UI.WebViewControlSettings'
    @winrt_mixinmethod
    def put_IsJavaScriptEnabled(self: Windows.Web.UI.IWebViewControlSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsJavaScriptEnabled(self: Windows.Web.UI.IWebViewControlSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsIndexedDBEnabled(self: Windows.Web.UI.IWebViewControlSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsIndexedDBEnabled(self: Windows.Web.UI.IWebViewControlSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsScriptNotifyAllowed(self: Windows.Web.UI.IWebViewControlSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsScriptNotifyAllowed(self: Windows.Web.UI.IWebViewControlSettings) -> Boolean: ...
    IsJavaScriptEnabled = property(get_IsJavaScriptEnabled, put_IsJavaScriptEnabled)
    IsIndexedDBEnabled = property(get_IsIndexedDBEnabled, put_IsIndexedDBEnabled)
    IsScriptNotifyAllowed = property(get_IsScriptNotifyAllowed, put_IsScriptNotifyAllowed)
class WebViewControlUnsupportedUriSchemeIdentifiedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Web.UI.IWebViewControlUnsupportedUriSchemeIdentifiedEventArgs
    _classid_ = 'Windows.Web.UI.WebViewControlUnsupportedUriSchemeIdentifiedEventArgs'
    @winrt_mixinmethod
    def get_Uri(self: Windows.Web.UI.IWebViewControlUnsupportedUriSchemeIdentifiedEventArgs) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Handled(self: Windows.Web.UI.IWebViewControlUnsupportedUriSchemeIdentifiedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: Windows.Web.UI.IWebViewControlUnsupportedUriSchemeIdentifiedEventArgs, value: Boolean) -> Void: ...
    Uri = property(get_Uri, None)
    Handled = property(get_Handled, put_Handled)
class WebViewControlUnviewableContentIdentifiedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Web.UI.IWebViewControlUnviewableContentIdentifiedEventArgs
    _classid_ = 'Windows.Web.UI.WebViewControlUnviewableContentIdentifiedEventArgs'
    @winrt_mixinmethod
    def get_Uri(self: Windows.Web.UI.IWebViewControlUnviewableContentIdentifiedEventArgs) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Referrer(self: Windows.Web.UI.IWebViewControlUnviewableContentIdentifiedEventArgs) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_MediaType(self: Windows.Web.UI.IWebViewControlUnviewableContentIdentifiedEventArgs) -> WinRT_String: ...
    Uri = property(get_Uri, None)
    Referrer = property(get_Referrer, None)
    MediaType = property(get_MediaType, None)
class WebViewControlWebResourceRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Web.UI.IWebViewControlWebResourceRequestedEventArgs
    _classid_ = 'Windows.Web.UI.WebViewControlWebResourceRequestedEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: Windows.Web.UI.IWebViewControlWebResourceRequestedEventArgs) -> Windows.Foundation.Deferral: ...
    @winrt_mixinmethod
    def get_Request(self: Windows.Web.UI.IWebViewControlWebResourceRequestedEventArgs) -> Windows.Web.Http.HttpRequestMessage: ...
    @winrt_mixinmethod
    def put_Response(self: Windows.Web.UI.IWebViewControlWebResourceRequestedEventArgs, value: Windows.Web.Http.HttpResponseMessage) -> Void: ...
    @winrt_mixinmethod
    def get_Response(self: Windows.Web.UI.IWebViewControlWebResourceRequestedEventArgs) -> Windows.Web.Http.HttpResponseMessage: ...
    Request = property(get_Request, None)
    Response = property(get_Response, put_Response)
make_head(_module, 'IWebViewControl')
make_head(_module, 'IWebViewControl2')
make_head(_module, 'IWebViewControlContentLoadingEventArgs')
make_head(_module, 'IWebViewControlDOMContentLoadedEventArgs')
make_head(_module, 'IWebViewControlDeferredPermissionRequest')
make_head(_module, 'IWebViewControlLongRunningScriptDetectedEventArgs')
make_head(_module, 'IWebViewControlNavigationCompletedEventArgs')
make_head(_module, 'IWebViewControlNavigationStartingEventArgs')
make_head(_module, 'IWebViewControlNewWindowRequestedEventArgs')
make_head(_module, 'IWebViewControlNewWindowRequestedEventArgs2')
make_head(_module, 'IWebViewControlPermissionRequest')
make_head(_module, 'IWebViewControlPermissionRequestedEventArgs')
make_head(_module, 'IWebViewControlScriptNotifyEventArgs')
make_head(_module, 'IWebViewControlSettings')
make_head(_module, 'IWebViewControlUnsupportedUriSchemeIdentifiedEventArgs')
make_head(_module, 'IWebViewControlUnviewableContentIdentifiedEventArgs')
make_head(_module, 'IWebViewControlWebResourceRequestedEventArgs')
make_head(_module, 'WebViewControlContentLoadingEventArgs')
make_head(_module, 'WebViewControlDOMContentLoadedEventArgs')
make_head(_module, 'WebViewControlDeferredPermissionRequest')
make_head(_module, 'WebViewControlLongRunningScriptDetectedEventArgs')
make_head(_module, 'WebViewControlNavigationCompletedEventArgs')
make_head(_module, 'WebViewControlNavigationStartingEventArgs')
make_head(_module, 'WebViewControlNewWindowRequestedEventArgs')
make_head(_module, 'WebViewControlPermissionRequest')
make_head(_module, 'WebViewControlPermissionRequestedEventArgs')
make_head(_module, 'WebViewControlScriptNotifyEventArgs')
make_head(_module, 'WebViewControlSettings')
make_head(_module, 'WebViewControlUnsupportedUriSchemeIdentifiedEventArgs')
make_head(_module, 'WebViewControlUnviewableContentIdentifiedEventArgs')
make_head(_module, 'WebViewControlWebResourceRequestedEventArgs')
