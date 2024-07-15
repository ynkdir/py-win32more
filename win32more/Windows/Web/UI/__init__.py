from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.DataTransfer
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage.Streams
import win32more.Windows.UI
import win32more.Windows.Web
import win32more.Windows.Web.Http
import win32more.Windows.Web.UI
import win32more.Windows.Win32.System.WinRT
class IWebViewControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.UI.IWebViewControl'
    _iid_ = Guid('{3f921316-bc70-4bda-9136-c94370899fab}')
    @winrt_commethod(6)
    def get_Source(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def put_Source(self, source: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(8)
    def get_DocumentTitle(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_CanGoBack(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_CanGoForward(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_DefaultBackgroundColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(12)
    def get_DefaultBackgroundColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(13)
    def get_ContainsFullScreenElement(self) -> Boolean: ...
    @winrt_commethod(14)
    def get_Settings(self) -> win32more.Windows.Web.UI.WebViewControlSettings: ...
    @winrt_commethod(15)
    def get_DeferredPermissionRequests(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Web.UI.WebViewControlDeferredPermissionRequest]: ...
    @winrt_commethod(16)
    def GoForward(self) -> Void: ...
    @winrt_commethod(17)
    def GoBack(self) -> Void: ...
    @winrt_commethod(18)
    def Refresh(self) -> Void: ...
    @winrt_commethod(19)
    def Stop(self) -> Void: ...
    @winrt_commethod(20)
    def Navigate(self, source: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_commethod(21)
    def NavigateToString(self, text: WinRT_String) -> Void: ...
    @winrt_commethod(22)
    def NavigateToLocalStreamUri(self, source: win32more.Windows.Foundation.Uri, streamResolver: win32more.Windows.Web.IUriToStreamResolver) -> Void: ...
    @winrt_commethod(23)
    def NavigateWithHttpRequestMessage(self, requestMessage: win32more.Windows.Web.Http.HttpRequestMessage) -> Void: ...
    @winrt_commethod(24)
    def InvokeScriptAsync(self, scriptName: WinRT_String, arguments: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(25)
    def CapturePreviewToStreamAsync(self, stream: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(26)
    def CaptureSelectedContentToDataPackageAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.DataTransfer.DataPackage]: ...
    @winrt_commethod(27)
    def BuildLocalStreamUri(self, contentIdentifier: WinRT_String, relativePath: WinRT_String) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(28)
    def GetDeferredPermissionRequestById(self, id: UInt32, result: POINTER(win32more.Windows.Web.UI.WebViewControlDeferredPermissionRequest)) -> Void: ...
    @winrt_commethod(29)
    def add_NavigationStarting(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlNavigationStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(30)
    def remove_NavigationStarting(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(31)
    def add_ContentLoading(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlContentLoadingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(32)
    def remove_ContentLoading(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(33)
    def add_DOMContentLoaded(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlDOMContentLoadedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(34)
    def remove_DOMContentLoaded(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(35)
    def add_NavigationCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlNavigationCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(36)
    def remove_NavigationCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(37)
    def add_FrameNavigationStarting(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlNavigationStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(38)
    def remove_FrameNavigationStarting(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(39)
    def add_FrameContentLoading(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlContentLoadingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(40)
    def remove_FrameContentLoading(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(41)
    def add_FrameDOMContentLoaded(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlDOMContentLoadedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(42)
    def remove_FrameDOMContentLoaded(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(43)
    def add_FrameNavigationCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlNavigationCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(44)
    def remove_FrameNavigationCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(45)
    def add_ScriptNotify(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlScriptNotifyEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(46)
    def remove_ScriptNotify(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(47)
    def add_LongRunningScriptDetected(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlLongRunningScriptDetectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(48)
    def remove_LongRunningScriptDetected(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(49)
    def add_UnsafeContentWarningDisplaying(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(50)
    def remove_UnsafeContentWarningDisplaying(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(51)
    def add_UnviewableContentIdentified(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlUnviewableContentIdentifiedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(52)
    def remove_UnviewableContentIdentified(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(53)
    def add_PermissionRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlPermissionRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(54)
    def remove_PermissionRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(55)
    def add_UnsupportedUriSchemeIdentified(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlUnsupportedUriSchemeIdentifiedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(56)
    def remove_UnsupportedUriSchemeIdentified(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(57)
    def add_NewWindowRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlNewWindowRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(58)
    def remove_NewWindowRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(59)
    def add_ContainsFullScreenElementChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(60)
    def remove_ContainsFullScreenElementChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(61)
    def add_WebResourceRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlWebResourceRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(62)
    def remove_WebResourceRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    CanGoBack = property(get_CanGoBack, None)
    CanGoForward = property(get_CanGoForward, None)
    ContainsFullScreenElement = property(get_ContainsFullScreenElement, None)
    DefaultBackgroundColor = property(get_DefaultBackgroundColor, put_DefaultBackgroundColor)
    DeferredPermissionRequests = property(get_DeferredPermissionRequests, None)
    DocumentTitle = property(get_DocumentTitle, None)
    Settings = property(get_Settings, None)
    Source = property(get_Source, put_Source)
    NavigationStarting = event()
    ContentLoading = event()
    DOMContentLoaded = event()
    NavigationCompleted = event()
    FrameNavigationStarting = event()
    FrameContentLoading = event()
    FrameDOMContentLoaded = event()
    FrameNavigationCompleted = event()
    ScriptNotify = event()
    LongRunningScriptDetected = event()
    UnsafeContentWarningDisplaying = event()
    UnviewableContentIdentified = event()
    PermissionRequested = event()
    UnsupportedUriSchemeIdentified = event()
    NewWindowRequested = event()
    ContainsFullScreenElementChanged = event()
    WebResourceRequested = event()
class IWebViewControl2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.UI.IWebViewControl2'
    _iid_ = Guid('{4d3c06f9-c8df-41cc-8bd5-2a947b204503}')
    @winrt_commethod(6)
    def AddInitializeScript(self, script: WinRT_String) -> Void: ...
class IWebViewControlContentLoadingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.UI.IWebViewControlContentLoadingEventArgs'
    _iid_ = Guid('{9a3fccb2-b9bb-404b-a22b-66dccd1250c6}')
    @winrt_commethod(6)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    Uri = property(get_Uri, None)
class IWebViewControlDOMContentLoadedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.UI.IWebViewControlDOMContentLoadedEventArgs'
    _iid_ = Guid('{be8bc008-9541-4545-9ff2-2df585b29f7d}')
    @winrt_commethod(6)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    Uri = property(get_Uri, None)
class IWebViewControlDeferredPermissionRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.UI.IWebViewControlDeferredPermissionRequest'
    _iid_ = Guid('{2ce349e0-d759-445c-9926-8995298f152b}')
    @winrt_commethod(6)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(8)
    def get_PermissionType(self) -> win32more.Windows.Web.UI.WebViewControlPermissionType: ...
    @winrt_commethod(9)
    def Allow(self) -> Void: ...
    @winrt_commethod(10)
    def Deny(self) -> Void: ...
    Id = property(get_Id, None)
    PermissionType = property(get_PermissionType, None)
    Uri = property(get_Uri, None)
class IWebViewControlLongRunningScriptDetectedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.UI.IWebViewControlLongRunningScriptDetectedEventArgs'
    _iid_ = Guid('{2a6e5bba-98b4-45bc-bbeb-0f69ce49c599}')
    @winrt_commethod(6)
    def get_ExecutionTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def get_StopPageScriptExecution(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_StopPageScriptExecution(self, value: Boolean) -> Void: ...
    ExecutionTime = property(get_ExecutionTime, None)
    StopPageScriptExecution = property(get_StopPageScriptExecution, put_StopPageScriptExecution)
class IWebViewControlNavigationCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.UI.IWebViewControlNavigationCompletedEventArgs'
    _iid_ = Guid('{20409918-4a15-4c46-a55d-f79edb0bde8b}')
    @winrt_commethod(6)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def get_IsSuccess(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_WebErrorStatus(self) -> win32more.Windows.Web.WebErrorStatus: ...
    IsSuccess = property(get_IsSuccess, None)
    Uri = property(get_Uri, None)
    WebErrorStatus = property(get_WebErrorStatus, None)
class IWebViewControlNavigationStartingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.UI.IWebViewControlNavigationStartingEventArgs'
    _iid_ = Guid('{0c9057c5-0a08-41c7-863b-71e3a9549137}')
    @winrt_commethod(6)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def get_Cancel(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Cancel(self, value: Boolean) -> Void: ...
    Cancel = property(get_Cancel, put_Cancel)
    Uri = property(get_Uri, None)
class IWebViewControlNewWindowRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.UI.IWebViewControlNewWindowRequestedEventArgs'
    _iid_ = Guid('{3df44bbb-a124-46d5-a083-d02cacdff5ad}')
    @winrt_commethod(6)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def get_Referrer(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(8)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Handled(self, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
    Referrer = property(get_Referrer, None)
    Uri = property(get_Uri, None)
class IWebViewControlNewWindowRequestedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.UI.IWebViewControlNewWindowRequestedEventArgs2'
    _iid_ = Guid('{b53c5ca6-2aae-4bfc-92b9-c30e92b48098}')
    @winrt_commethod(6)
    def get_NewWindow(self) -> win32more.Windows.Web.UI.IWebViewControl: ...
    @winrt_commethod(7)
    def put_NewWindow(self, value: win32more.Windows.Web.UI.IWebViewControl) -> Void: ...
    @winrt_commethod(8)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    NewWindow = property(get_NewWindow, put_NewWindow)
class IWebViewControlPermissionRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.UI.IWebViewControlPermissionRequest'
    _iid_ = Guid('{e5bc836c-f22f-40e2-95b2-7729f840eb7f}')
    @winrt_commethod(6)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(8)
    def get_PermissionType(self) -> win32more.Windows.Web.UI.WebViewControlPermissionType: ...
    @winrt_commethod(9)
    def get_State(self) -> win32more.Windows.Web.UI.WebViewControlPermissionState: ...
    @winrt_commethod(10)
    def Defer(self) -> Void: ...
    @winrt_commethod(11)
    def Allow(self) -> Void: ...
    @winrt_commethod(12)
    def Deny(self) -> Void: ...
    Id = property(get_Id, None)
    PermissionType = property(get_PermissionType, None)
    State = property(get_State, None)
    Uri = property(get_Uri, None)
class IWebViewControlPermissionRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.UI.IWebViewControlPermissionRequestedEventArgs'
    _iid_ = Guid('{27204d51-2488-4cc5-968e-0a771e59c147}')
    @winrt_commethod(6)
    def get_PermissionRequest(self) -> win32more.Windows.Web.UI.WebViewControlPermissionRequest: ...
    PermissionRequest = property(get_PermissionRequest, None)
class IWebViewControlScriptNotifyEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.UI.IWebViewControlScriptNotifyEventArgs'
    _iid_ = Guid('{491de57b-6f49-41bb-b591-51b85b817037}')
    @winrt_commethod(6)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def get_Value(self) -> WinRT_String: ...
    Uri = property(get_Uri, None)
    Value = property(get_Value, None)
class IWebViewControlSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.UI.IWebViewControlSettings'
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
    IsIndexedDBEnabled = property(get_IsIndexedDBEnabled, put_IsIndexedDBEnabled)
    IsJavaScriptEnabled = property(get_IsJavaScriptEnabled, put_IsJavaScriptEnabled)
    IsScriptNotifyAllowed = property(get_IsScriptNotifyAllowed, put_IsScriptNotifyAllowed)
class IWebViewControlUnsupportedUriSchemeIdentifiedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.UI.IWebViewControlUnsupportedUriSchemeIdentifiedEventArgs'
    _iid_ = Guid('{e3b81944-e4fc-43dc-94ca-f980f30bc51d}')
    @winrt_commethod(6)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Handled(self, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
    Uri = property(get_Uri, None)
class IWebViewControlUnviewableContentIdentifiedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.UI.IWebViewControlUnviewableContentIdentifiedEventArgs'
    _iid_ = Guid('{4a9680db-88f2-4e20-b693-b4e2df4aa581}')
    @winrt_commethod(6)
    def get_Uri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(7)
    def get_Referrer(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(8)
    def get_MediaType(self) -> WinRT_String: ...
    MediaType = property(get_MediaType, None)
    Referrer = property(get_Referrer, None)
    Uri = property(get_Uri, None)
class IWebViewControlWebResourceRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.UI.IWebViewControlWebResourceRequestedEventArgs'
    _iid_ = Guid('{44d6524d-55a4-4d8b-891c-931d8e25d42e}')
    @winrt_commethod(6)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    @winrt_commethod(7)
    def get_Request(self) -> win32more.Windows.Web.Http.HttpRequestMessage: ...
    @winrt_commethod(8)
    def put_Response(self, value: win32more.Windows.Web.Http.HttpResponseMessage) -> Void: ...
    @winrt_commethod(9)
    def get_Response(self) -> win32more.Windows.Web.Http.HttpResponseMessage: ...
    Request = property(get_Request, None)
    Response = property(get_Response, put_Response)
class WebViewControlContentLoadingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.UI.IWebViewControlContentLoadingEventArgs
    _classid_ = 'Windows.Web.UI.WebViewControlContentLoadingEventArgs'
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.Web.UI.IWebViewControlContentLoadingEventArgs) -> win32more.Windows.Foundation.Uri: ...
    Uri = property(get_Uri, None)
class WebViewControlDOMContentLoadedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.UI.IWebViewControlDOMContentLoadedEventArgs
    _classid_ = 'Windows.Web.UI.WebViewControlDOMContentLoadedEventArgs'
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.Web.UI.IWebViewControlDOMContentLoadedEventArgs) -> win32more.Windows.Foundation.Uri: ...
    Uri = property(get_Uri, None)
class WebViewControlDeferredPermissionRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.UI.IWebViewControlDeferredPermissionRequest
    _classid_ = 'Windows.Web.UI.WebViewControlDeferredPermissionRequest'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Web.UI.IWebViewControlDeferredPermissionRequest) -> UInt32: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.Web.UI.IWebViewControlDeferredPermissionRequest) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_PermissionType(self: win32more.Windows.Web.UI.IWebViewControlDeferredPermissionRequest) -> win32more.Windows.Web.UI.WebViewControlPermissionType: ...
    @winrt_mixinmethod
    def Allow(self: win32more.Windows.Web.UI.IWebViewControlDeferredPermissionRequest) -> Void: ...
    @winrt_mixinmethod
    def Deny(self: win32more.Windows.Web.UI.IWebViewControlDeferredPermissionRequest) -> Void: ...
    Id = property(get_Id, None)
    PermissionType = property(get_PermissionType, None)
    Uri = property(get_Uri, None)
class WebViewControlLongRunningScriptDetectedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.UI.IWebViewControlLongRunningScriptDetectedEventArgs
    _classid_ = 'Windows.Web.UI.WebViewControlLongRunningScriptDetectedEventArgs'
    @winrt_mixinmethod
    def get_ExecutionTime(self: win32more.Windows.Web.UI.IWebViewControlLongRunningScriptDetectedEventArgs) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_StopPageScriptExecution(self: win32more.Windows.Web.UI.IWebViewControlLongRunningScriptDetectedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_StopPageScriptExecution(self: win32more.Windows.Web.UI.IWebViewControlLongRunningScriptDetectedEventArgs, value: Boolean) -> Void: ...
    ExecutionTime = property(get_ExecutionTime, None)
    StopPageScriptExecution = property(get_StopPageScriptExecution, put_StopPageScriptExecution)
class WebViewControlNavigationCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.UI.IWebViewControlNavigationCompletedEventArgs
    _classid_ = 'Windows.Web.UI.WebViewControlNavigationCompletedEventArgs'
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.Web.UI.IWebViewControlNavigationCompletedEventArgs) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_IsSuccess(self: win32more.Windows.Web.UI.IWebViewControlNavigationCompletedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_WebErrorStatus(self: win32more.Windows.Web.UI.IWebViewControlNavigationCompletedEventArgs) -> win32more.Windows.Web.WebErrorStatus: ...
    IsSuccess = property(get_IsSuccess, None)
    Uri = property(get_Uri, None)
    WebErrorStatus = property(get_WebErrorStatus, None)
class WebViewControlNavigationStartingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.UI.IWebViewControlNavigationStartingEventArgs
    _classid_ = 'Windows.Web.UI.WebViewControlNavigationStartingEventArgs'
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.Web.UI.IWebViewControlNavigationStartingEventArgs) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Cancel(self: win32more.Windows.Web.UI.IWebViewControlNavigationStartingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Cancel(self: win32more.Windows.Web.UI.IWebViewControlNavigationStartingEventArgs, value: Boolean) -> Void: ...
    Cancel = property(get_Cancel, put_Cancel)
    Uri = property(get_Uri, None)
class WebViewControlNewWindowRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.UI.IWebViewControlNewWindowRequestedEventArgs
    _classid_ = 'Windows.Web.UI.WebViewControlNewWindowRequestedEventArgs'
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.Web.UI.IWebViewControlNewWindowRequestedEventArgs) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Referrer(self: win32more.Windows.Web.UI.IWebViewControlNewWindowRequestedEventArgs) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.Web.UI.IWebViewControlNewWindowRequestedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.Web.UI.IWebViewControlNewWindowRequestedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_NewWindow(self: win32more.Windows.Web.UI.IWebViewControlNewWindowRequestedEventArgs2) -> win32more.Windows.Web.UI.IWebViewControl: ...
    @winrt_mixinmethod
    def put_NewWindow(self: win32more.Windows.Web.UI.IWebViewControlNewWindowRequestedEventArgs2, value: win32more.Windows.Web.UI.IWebViewControl) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Web.UI.IWebViewControlNewWindowRequestedEventArgs2) -> win32more.Windows.Foundation.Deferral: ...
    Handled = property(get_Handled, put_Handled)
    NewWindow = property(get_NewWindow, put_NewWindow)
    Referrer = property(get_Referrer, None)
    Uri = property(get_Uri, None)
class WebViewControlPermissionRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.UI.IWebViewControlPermissionRequest
    _classid_ = 'Windows.Web.UI.WebViewControlPermissionRequest'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Web.UI.IWebViewControlPermissionRequest) -> UInt32: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.Web.UI.IWebViewControlPermissionRequest) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_PermissionType(self: win32more.Windows.Web.UI.IWebViewControlPermissionRequest) -> win32more.Windows.Web.UI.WebViewControlPermissionType: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Web.UI.IWebViewControlPermissionRequest) -> win32more.Windows.Web.UI.WebViewControlPermissionState: ...
    @winrt_mixinmethod
    def Defer(self: win32more.Windows.Web.UI.IWebViewControlPermissionRequest) -> Void: ...
    @winrt_mixinmethod
    def Allow(self: win32more.Windows.Web.UI.IWebViewControlPermissionRequest) -> Void: ...
    @winrt_mixinmethod
    def Deny(self: win32more.Windows.Web.UI.IWebViewControlPermissionRequest) -> Void: ...
    Id = property(get_Id, None)
    PermissionType = property(get_PermissionType, None)
    State = property(get_State, None)
    Uri = property(get_Uri, None)
class WebViewControlPermissionRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.UI.IWebViewControlPermissionRequestedEventArgs
    _classid_ = 'Windows.Web.UI.WebViewControlPermissionRequestedEventArgs'
    @winrt_mixinmethod
    def get_PermissionRequest(self: win32more.Windows.Web.UI.IWebViewControlPermissionRequestedEventArgs) -> win32more.Windows.Web.UI.WebViewControlPermissionRequest: ...
    PermissionRequest = property(get_PermissionRequest, None)
class WebViewControlPermissionState(Enum, Int32):
    Unknown = 0
    Defer = 1
    Allow = 2
    Deny = 3
class WebViewControlPermissionType(Enum, Int32):
    Geolocation = 0
    UnlimitedIndexedDBQuota = 1
    Media = 2
    PointerLock = 3
    WebNotifications = 4
    Screen = 5
    ImmersiveView = 6
class WebViewControlScriptNotifyEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.UI.IWebViewControlScriptNotifyEventArgs
    _classid_ = 'Windows.Web.UI.WebViewControlScriptNotifyEventArgs'
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.Web.UI.IWebViewControlScriptNotifyEventArgs) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.Web.UI.IWebViewControlScriptNotifyEventArgs) -> WinRT_String: ...
    Uri = property(get_Uri, None)
    Value = property(get_Value, None)
class WebViewControlSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.UI.IWebViewControlSettings
    _classid_ = 'Windows.Web.UI.WebViewControlSettings'
    @winrt_mixinmethod
    def put_IsJavaScriptEnabled(self: win32more.Windows.Web.UI.IWebViewControlSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsJavaScriptEnabled(self: win32more.Windows.Web.UI.IWebViewControlSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsIndexedDBEnabled(self: win32more.Windows.Web.UI.IWebViewControlSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsIndexedDBEnabled(self: win32more.Windows.Web.UI.IWebViewControlSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsScriptNotifyAllowed(self: win32more.Windows.Web.UI.IWebViewControlSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsScriptNotifyAllowed(self: win32more.Windows.Web.UI.IWebViewControlSettings) -> Boolean: ...
    IsIndexedDBEnabled = property(get_IsIndexedDBEnabled, put_IsIndexedDBEnabled)
    IsJavaScriptEnabled = property(get_IsJavaScriptEnabled, put_IsJavaScriptEnabled)
    IsScriptNotifyAllowed = property(get_IsScriptNotifyAllowed, put_IsScriptNotifyAllowed)
class WebViewControlUnsupportedUriSchemeIdentifiedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.UI.IWebViewControlUnsupportedUriSchemeIdentifiedEventArgs
    _classid_ = 'Windows.Web.UI.WebViewControlUnsupportedUriSchemeIdentifiedEventArgs'
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.Web.UI.IWebViewControlUnsupportedUriSchemeIdentifiedEventArgs) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.Web.UI.IWebViewControlUnsupportedUriSchemeIdentifiedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.Web.UI.IWebViewControlUnsupportedUriSchemeIdentifiedEventArgs, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
    Uri = property(get_Uri, None)
class WebViewControlUnviewableContentIdentifiedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.UI.IWebViewControlUnviewableContentIdentifiedEventArgs
    _classid_ = 'Windows.Web.UI.WebViewControlUnviewableContentIdentifiedEventArgs'
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.Web.UI.IWebViewControlUnviewableContentIdentifiedEventArgs) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Referrer(self: win32more.Windows.Web.UI.IWebViewControlUnviewableContentIdentifiedEventArgs) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_MediaType(self: win32more.Windows.Web.UI.IWebViewControlUnviewableContentIdentifiedEventArgs) -> WinRT_String: ...
    MediaType = property(get_MediaType, None)
    Referrer = property(get_Referrer, None)
    Uri = property(get_Uri, None)
class WebViewControlWebResourceRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.UI.IWebViewControlWebResourceRequestedEventArgs
    _classid_ = 'Windows.Web.UI.WebViewControlWebResourceRequestedEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.Web.UI.IWebViewControlWebResourceRequestedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    @winrt_mixinmethod
    def get_Request(self: win32more.Windows.Web.UI.IWebViewControlWebResourceRequestedEventArgs) -> win32more.Windows.Web.Http.HttpRequestMessage: ...
    @winrt_mixinmethod
    def put_Response(self: win32more.Windows.Web.UI.IWebViewControlWebResourceRequestedEventArgs, value: win32more.Windows.Web.Http.HttpResponseMessage) -> Void: ...
    @winrt_mixinmethod
    def get_Response(self: win32more.Windows.Web.UI.IWebViewControlWebResourceRequestedEventArgs) -> win32more.Windows.Web.Http.HttpResponseMessage: ...
    Request = property(get_Request, None)
    Response = property(get_Response, put_Response)


make_ready(__name__)
