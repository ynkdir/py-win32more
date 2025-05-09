from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, FlexibleArray, Guid, Int16, Int32, Int64, IntPtr, NativeBitfieldAttribute, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel.DataTransfer
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage.Streams
import win32more.Windows.System
import win32more.Windows.UI
import win32more.Windows.UI.Core
import win32more.Windows.Web
import win32more.Windows.Web.Http
import win32more.Windows.Web.UI
import win32more.Windows.Web.UI.Interop
import win32more.Windows.Win32.System.WinRT
class IWebViewControlAcceleratorKeyPressedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.UI.Interop.IWebViewControlAcceleratorKeyPressedEventArgs'
    _iid_ = Guid('{77a2a53e-7c74-437d-a290-3ac0d8cd5655}')
    @winrt_commethod(6)
    def get_EventType(self) -> win32more.Windows.UI.Core.CoreAcceleratorKeyEventType: ...
    @winrt_commethod(7)
    def get_VirtualKey(self) -> win32more.Windows.System.VirtualKey: ...
    @winrt_commethod(8)
    def get_KeyStatus(self) -> win32more.Windows.UI.Core.CorePhysicalKeyStatus: ...
    @winrt_commethod(9)
    def get_RoutingStage(self) -> win32more.Windows.Web.UI.Interop.WebViewControlAcceleratorKeyRoutingStage: ...
    @winrt_commethod(10)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_Handled(self, value: Boolean) -> Void: ...
    EventType = property(get_EventType, None)
    Handled = property(get_Handled, put_Handled)
    KeyStatus = property(get_KeyStatus, None)
    RoutingStage = property(get_RoutingStage, None)
    VirtualKey = property(get_VirtualKey, None)
class IWebViewControlMoveFocusRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.UI.Interop.IWebViewControlMoveFocusRequestedEventArgs'
    _iid_ = Guid('{6b2a340d-4bd0-405e-b7c1-1e72a492f446}')
    @winrt_commethod(6)
    def get_Reason(self) -> win32more.Windows.Web.UI.Interop.WebViewControlMoveFocusReason: ...
    Reason = property(get_Reason, None)
class IWebViewControlProcess(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.UI.Interop.IWebViewControlProcess'
    _iid_ = Guid('{02c723ec-98d6-424a-b63e-c6136c36a0f2}')
    @winrt_commethod(6)
    def get_ProcessId(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_EnterpriseId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_IsPrivateNetworkClientServerCapabilityEnabled(self) -> Boolean: ...
    @winrt_commethod(9)
    def CreateWebViewControlAsync(self, hostWindowHandle: Int64, bounds: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Web.UI.Interop.WebViewControl]: ...
    @winrt_commethod(10)
    def GetWebViewControls(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Web.UI.Interop.WebViewControl]: ...
    @winrt_commethod(11)
    def Terminate(self) -> Void: ...
    @winrt_commethod(12)
    def add_ProcessExited(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.Interop.WebViewControlProcess, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_ProcessExited(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    EnterpriseId = property(get_EnterpriseId, None)
    IsPrivateNetworkClientServerCapabilityEnabled = property(get_IsPrivateNetworkClientServerCapabilityEnabled, None)
    ProcessId = property(get_ProcessId, None)
    ProcessExited = event()
class IWebViewControlProcessFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.UI.Interop.IWebViewControlProcessFactory'
    _iid_ = Guid('{47b65cf9-a2d2-453c-b097-f6779d4b8e02}')
    @winrt_commethod(6)
    def CreateWithOptions(self, processOptions: win32more.Windows.Web.UI.Interop.WebViewControlProcessOptions) -> win32more.Windows.Web.UI.Interop.WebViewControlProcess: ...
class IWebViewControlProcessOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.UI.Interop.IWebViewControlProcessOptions'
    _iid_ = Guid('{1cca72a7-3bd6-4826-8261-6c8189505d89}')
    @winrt_commethod(6)
    def put_EnterpriseId(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_EnterpriseId(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_PrivateNetworkClientServerCapability(self, value: win32more.Windows.Web.UI.Interop.WebViewControlProcessCapabilityState) -> Void: ...
    @winrt_commethod(9)
    def get_PrivateNetworkClientServerCapability(self) -> win32more.Windows.Web.UI.Interop.WebViewControlProcessCapabilityState: ...
    EnterpriseId = property(get_EnterpriseId, put_EnterpriseId)
    PrivateNetworkClientServerCapability = property(get_PrivateNetworkClientServerCapability, put_PrivateNetworkClientServerCapability)
class IWebViewControlSite(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.UI.Interop.IWebViewControlSite'
    _iid_ = Guid('{133f47c6-12dc-4898-bd47-04967de648ba}')
    @winrt_commethod(6)
    def get_Process(self) -> win32more.Windows.Web.UI.Interop.WebViewControlProcess: ...
    @winrt_commethod(7)
    def put_Scale(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_Scale(self) -> Double: ...
    @winrt_commethod(9)
    def put_Bounds(self, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(10)
    def get_Bounds(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(11)
    def put_IsVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_IsVisible(self) -> Boolean: ...
    @winrt_commethod(13)
    def Close(self) -> Void: ...
    @winrt_commethod(14)
    def MoveFocus(self, reason: win32more.Windows.Web.UI.Interop.WebViewControlMoveFocusReason) -> Void: ...
    @winrt_commethod(15)
    def add_MoveFocusRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.Interop.WebViewControl, win32more.Windows.Web.UI.Interop.WebViewControlMoveFocusRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_MoveFocusRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_AcceleratorKeyPressed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.Interop.WebViewControl, win32more.Windows.Web.UI.Interop.WebViewControlAcceleratorKeyPressedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_AcceleratorKeyPressed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Bounds = property(get_Bounds, put_Bounds)
    IsVisible = property(get_IsVisible, put_IsVisible)
    Process = property(get_Process, None)
    Scale = property(get_Scale, put_Scale)
    MoveFocusRequested = event()
    AcceleratorKeyPressed = event()
class IWebViewControlSite2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Web.UI.Interop.IWebViewControlSite2'
    _iid_ = Guid('{d13b2e3f-48ee-4730-8243-d2ed0c05606a}')
    @winrt_commethod(6)
    def add_GotFocus(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.Interop.WebViewControl, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_GotFocus(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_LostFocus(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.Interop.WebViewControl, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_LostFocus(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    GotFocus = event()
    LostFocus = event()
class WebViewControl(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.UI.IWebViewControl
    _classid_ = 'Windows.Web.UI.Interop.WebViewControl'
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.Web.UI.IWebViewControl) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Source(self: win32more.Windows.Web.UI.IWebViewControl, source: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_DocumentTitle(self: win32more.Windows.Web.UI.IWebViewControl) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CanGoBack(self: win32more.Windows.Web.UI.IWebViewControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanGoForward(self: win32more.Windows.Web.UI.IWebViewControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_DefaultBackgroundColor(self: win32more.Windows.Web.UI.IWebViewControl, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_DefaultBackgroundColor(self: win32more.Windows.Web.UI.IWebViewControl) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def get_ContainsFullScreenElement(self: win32more.Windows.Web.UI.IWebViewControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_Settings(self: win32more.Windows.Web.UI.IWebViewControl) -> win32more.Windows.Web.UI.WebViewControlSettings: ...
    @winrt_mixinmethod
    def get_DeferredPermissionRequests(self: win32more.Windows.Web.UI.IWebViewControl) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Web.UI.WebViewControlDeferredPermissionRequest]: ...
    @winrt_mixinmethod
    def GoForward(self: win32more.Windows.Web.UI.IWebViewControl) -> Void: ...
    @winrt_mixinmethod
    def GoBack(self: win32more.Windows.Web.UI.IWebViewControl) -> Void: ...
    @winrt_mixinmethod
    def Refresh(self: win32more.Windows.Web.UI.IWebViewControl) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Web.UI.IWebViewControl) -> Void: ...
    @winrt_mixinmethod
    def Navigate(self: win32more.Windows.Web.UI.IWebViewControl, source: win32more.Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def NavigateToString(self: win32more.Windows.Web.UI.IWebViewControl, text: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def NavigateToLocalStreamUri(self: win32more.Windows.Web.UI.IWebViewControl, source: win32more.Windows.Foundation.Uri, streamResolver: win32more.Windows.Web.IUriToStreamResolver) -> Void: ...
    @winrt_mixinmethod
    def NavigateWithHttpRequestMessage(self: win32more.Windows.Web.UI.IWebViewControl, requestMessage: win32more.Windows.Web.Http.HttpRequestMessage) -> Void: ...
    @winrt_mixinmethod
    def InvokeScriptAsync(self: win32more.Windows.Web.UI.IWebViewControl, scriptName: WinRT_String, arguments: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def CapturePreviewToStreamAsync(self: win32more.Windows.Web.UI.IWebViewControl, stream: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def CaptureSelectedContentToDataPackageAsync(self: win32more.Windows.Web.UI.IWebViewControl) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.DataTransfer.DataPackage]: ...
    @winrt_mixinmethod
    def BuildLocalStreamUri(self: win32more.Windows.Web.UI.IWebViewControl, contentIdentifier: WinRT_String, relativePath: WinRT_String) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def GetDeferredPermissionRequestById(self: win32more.Windows.Web.UI.IWebViewControl, id: UInt32, result: POINTER(win32more.Windows.Web.UI.WebViewControlDeferredPermissionRequest)) -> Void: ...
    @winrt_mixinmethod
    def add_NavigationStarting(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlNavigationStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NavigationStarting(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ContentLoading(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlContentLoadingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ContentLoading(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DOMContentLoaded(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlDOMContentLoadedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DOMContentLoaded(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_NavigationCompleted(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlNavigationCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NavigationCompleted(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_FrameNavigationStarting(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlNavigationStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameNavigationStarting(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_FrameContentLoading(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlContentLoadingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameContentLoading(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_FrameDOMContentLoaded(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlDOMContentLoadedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameDOMContentLoaded(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_FrameNavigationCompleted(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlNavigationCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameNavigationCompleted(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ScriptNotify(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlScriptNotifyEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ScriptNotify(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_LongRunningScriptDetected(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlLongRunningScriptDetectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LongRunningScriptDetected(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UnsafeContentWarningDisplaying(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UnsafeContentWarningDisplaying(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UnviewableContentIdentified(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlUnviewableContentIdentifiedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UnviewableContentIdentified(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PermissionRequested(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlPermissionRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PermissionRequested(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UnsupportedUriSchemeIdentified(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlUnsupportedUriSchemeIdentifiedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UnsupportedUriSchemeIdentified(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_NewWindowRequested(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlNewWindowRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NewWindowRequested(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ContainsFullScreenElementChanged(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ContainsFullScreenElementChanged(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_WebResourceRequested(self: win32more.Windows.Web.UI.IWebViewControl, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.IWebViewControl, win32more.Windows.Web.UI.WebViewControlWebResourceRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_WebResourceRequested(self: win32more.Windows.Web.UI.IWebViewControl, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Process(self: win32more.Windows.Web.UI.Interop.IWebViewControlSite) -> win32more.Windows.Web.UI.Interop.WebViewControlProcess: ...
    @winrt_mixinmethod
    def put_Scale(self: win32more.Windows.Web.UI.Interop.IWebViewControlSite, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Scale(self: win32more.Windows.Web.UI.Interop.IWebViewControlSite) -> Double: ...
    @winrt_mixinmethod
    def put_Bounds(self: win32more.Windows.Web.UI.Interop.IWebViewControlSite, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def get_Bounds(self: win32more.Windows.Web.UI.Interop.IWebViewControlSite) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def put_IsVisible(self: win32more.Windows.Web.UI.Interop.IWebViewControlSite, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsVisible(self: win32more.Windows.Web.UI.Interop.IWebViewControlSite) -> Boolean: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Web.UI.Interop.IWebViewControlSite) -> Void: ...
    @winrt_mixinmethod
    def MoveFocus(self: win32more.Windows.Web.UI.Interop.IWebViewControlSite, reason: win32more.Windows.Web.UI.Interop.WebViewControlMoveFocusReason) -> Void: ...
    @winrt_mixinmethod
    def add_MoveFocusRequested(self: win32more.Windows.Web.UI.Interop.IWebViewControlSite, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.Interop.WebViewControl, win32more.Windows.Web.UI.Interop.WebViewControlMoveFocusRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MoveFocusRequested(self: win32more.Windows.Web.UI.Interop.IWebViewControlSite, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AcceleratorKeyPressed(self: win32more.Windows.Web.UI.Interop.IWebViewControlSite, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.Interop.WebViewControl, win32more.Windows.Web.UI.Interop.WebViewControlAcceleratorKeyPressedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AcceleratorKeyPressed(self: win32more.Windows.Web.UI.Interop.IWebViewControlSite, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def AddInitializeScript(self: win32more.Windows.Web.UI.IWebViewControl2, script: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def add_GotFocus(self: win32more.Windows.Web.UI.Interop.IWebViewControlSite2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.Interop.WebViewControl, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_GotFocus(self: win32more.Windows.Web.UI.Interop.IWebViewControlSite2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_LostFocus(self: win32more.Windows.Web.UI.Interop.IWebViewControlSite2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.Interop.WebViewControl, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LostFocus(self: win32more.Windows.Web.UI.Interop.IWebViewControlSite2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Bounds = property(get_Bounds, put_Bounds)
    CanGoBack = property(get_CanGoBack, None)
    CanGoForward = property(get_CanGoForward, None)
    ContainsFullScreenElement = property(get_ContainsFullScreenElement, None)
    DefaultBackgroundColor = property(get_DefaultBackgroundColor, put_DefaultBackgroundColor)
    DeferredPermissionRequests = property(get_DeferredPermissionRequests, None)
    DocumentTitle = property(get_DocumentTitle, None)
    IsVisible = property(get_IsVisible, put_IsVisible)
    Process = property(get_Process, None)
    Scale = property(get_Scale, put_Scale)
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
    MoveFocusRequested = event()
    AcceleratorKeyPressed = event()
    GotFocus = event()
    LostFocus = event()
class WebViewControlAcceleratorKeyPressedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.UI.Interop.IWebViewControlAcceleratorKeyPressedEventArgs
    _classid_ = 'Windows.Web.UI.Interop.WebViewControlAcceleratorKeyPressedEventArgs'
    @winrt_mixinmethod
    def get_EventType(self: win32more.Windows.Web.UI.Interop.IWebViewControlAcceleratorKeyPressedEventArgs) -> win32more.Windows.UI.Core.CoreAcceleratorKeyEventType: ...
    @winrt_mixinmethod
    def get_VirtualKey(self: win32more.Windows.Web.UI.Interop.IWebViewControlAcceleratorKeyPressedEventArgs) -> win32more.Windows.System.VirtualKey: ...
    @winrt_mixinmethod
    def get_KeyStatus(self: win32more.Windows.Web.UI.Interop.IWebViewControlAcceleratorKeyPressedEventArgs) -> win32more.Windows.UI.Core.CorePhysicalKeyStatus: ...
    @winrt_mixinmethod
    def get_RoutingStage(self: win32more.Windows.Web.UI.Interop.IWebViewControlAcceleratorKeyPressedEventArgs) -> win32more.Windows.Web.UI.Interop.WebViewControlAcceleratorKeyRoutingStage: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Windows.Web.UI.Interop.IWebViewControlAcceleratorKeyPressedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Windows.Web.UI.Interop.IWebViewControlAcceleratorKeyPressedEventArgs, value: Boolean) -> Void: ...
    EventType = property(get_EventType, None)
    Handled = property(get_Handled, put_Handled)
    KeyStatus = property(get_KeyStatus, None)
    RoutingStage = property(get_RoutingStage, None)
    VirtualKey = property(get_VirtualKey, None)
class WebViewControlAcceleratorKeyRoutingStage(Enum, Int32):
    Tunneling = 0
    Bubbling = 1
class WebViewControlMoveFocusReason(Enum, Int32):
    Programmatic = 0
    Next = 1
    Previous = 2
class WebViewControlMoveFocusRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.UI.Interop.IWebViewControlMoveFocusRequestedEventArgs
    _classid_ = 'Windows.Web.UI.Interop.WebViewControlMoveFocusRequestedEventArgs'
    @winrt_mixinmethod
    def get_Reason(self: win32more.Windows.Web.UI.Interop.IWebViewControlMoveFocusRequestedEventArgs) -> win32more.Windows.Web.UI.Interop.WebViewControlMoveFocusReason: ...
    Reason = property(get_Reason, None)
class WebViewControlProcess(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.UI.Interop.IWebViewControlProcess
    _classid_ = 'Windows.Web.UI.Interop.WebViewControlProcess'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Web.UI.Interop.WebViewControlProcess.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Web.UI.Interop.WebViewControlProcess.CreateWithOptions(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Web.UI.Interop.WebViewControlProcess: ...
    @winrt_factorymethod
    def CreateWithOptions(cls: win32more.Windows.Web.UI.Interop.IWebViewControlProcessFactory, processOptions: win32more.Windows.Web.UI.Interop.WebViewControlProcessOptions) -> win32more.Windows.Web.UI.Interop.WebViewControlProcess: ...
    @winrt_mixinmethod
    def get_ProcessId(self: win32more.Windows.Web.UI.Interop.IWebViewControlProcess) -> UInt32: ...
    @winrt_mixinmethod
    def get_EnterpriseId(self: win32more.Windows.Web.UI.Interop.IWebViewControlProcess) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsPrivateNetworkClientServerCapabilityEnabled(self: win32more.Windows.Web.UI.Interop.IWebViewControlProcess) -> Boolean: ...
    @winrt_mixinmethod
    def CreateWebViewControlAsync(self: win32more.Windows.Web.UI.Interop.IWebViewControlProcess, hostWindowHandle: Int64, bounds: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Web.UI.Interop.WebViewControl]: ...
    @winrt_mixinmethod
    def GetWebViewControls(self: win32more.Windows.Web.UI.Interop.IWebViewControlProcess) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Web.UI.Interop.WebViewControl]: ...
    @winrt_mixinmethod
    def Terminate(self: win32more.Windows.Web.UI.Interop.IWebViewControlProcess) -> Void: ...
    @winrt_mixinmethod
    def add_ProcessExited(self: win32more.Windows.Web.UI.Interop.IWebViewControlProcess, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Web.UI.Interop.WebViewControlProcess, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ProcessExited(self: win32more.Windows.Web.UI.Interop.IWebViewControlProcess, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    EnterpriseId = property(get_EnterpriseId, None)
    IsPrivateNetworkClientServerCapabilityEnabled = property(get_IsPrivateNetworkClientServerCapabilityEnabled, None)
    ProcessId = property(get_ProcessId, None)
    ProcessExited = event()
class WebViewControlProcessCapabilityState(Enum, Int32):
    Default = 0
    Disabled = 1
    Enabled = 2
class WebViewControlProcessOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Web.UI.Interop.IWebViewControlProcessOptions
    _classid_ = 'Windows.Web.UI.Interop.WebViewControlProcessOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Web.UI.Interop.WebViewControlProcessOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Web.UI.Interop.WebViewControlProcessOptions: ...
    @winrt_mixinmethod
    def put_EnterpriseId(self: win32more.Windows.Web.UI.Interop.IWebViewControlProcessOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_EnterpriseId(self: win32more.Windows.Web.UI.Interop.IWebViewControlProcessOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PrivateNetworkClientServerCapability(self: win32more.Windows.Web.UI.Interop.IWebViewControlProcessOptions, value: win32more.Windows.Web.UI.Interop.WebViewControlProcessCapabilityState) -> Void: ...
    @winrt_mixinmethod
    def get_PrivateNetworkClientServerCapability(self: win32more.Windows.Web.UI.Interop.IWebViewControlProcessOptions) -> win32more.Windows.Web.UI.Interop.WebViewControlProcessCapabilityState: ...
    EnterpriseId = property(get_EnterpriseId, put_EnterpriseId)
    PrivateNetworkClientServerCapability = property(get_PrivateNetworkClientServerCapability, put_PrivateNetworkClientServerCapability)


make_ready(__name__)
