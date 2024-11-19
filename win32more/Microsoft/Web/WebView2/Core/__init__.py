from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.Web.WebView2.Core
import win32more.Windows.ApplicationModel.DataTransfer
import win32more.Windows.ApplicationModel.DataTransfer.DragDrop.Core
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Security.Cryptography.Certificates
import win32more.Windows.Storage.Streams
import win32more.Windows.UI
import win32more.Windows.UI.Core
import win32more.Windows.Win32.System.WinRT
class CoreWebView2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2'
    @winrt_mixinmethod
    def add_BasicAuthenticationRequested(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_10, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2BasicAuthenticationRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BasicAuthenticationRequested(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_10, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ContextMenuRequested(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_11, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2ContextMenuRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ContextMenuRequested(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_11, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CallDevToolsProtocolMethodForSessionAsync(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_11, sessionId: WinRT_String, methodName: WinRT_String, parametersAsJson: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def get_StatusBarText(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_12) -> WinRT_String: ...
    @winrt_mixinmethod
    def add_StatusBarTextChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_12, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StatusBarTextChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_12, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Profile(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_13) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2Profile: ...
    @winrt_mixinmethod
    def add_ServerCertificateErrorDetected(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_14, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2ServerCertificateErrorDetectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ServerCertificateErrorDetected(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_14, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def ClearServerCertificateErrorActionsAsync(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_14) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_FaviconUri(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_15) -> WinRT_String: ...
    @winrt_mixinmethod
    def add_FaviconChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_15, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FaviconChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_15, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetFaviconAsync(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_15, format: win32more.Microsoft.Web.WebView2.Core.CoreWebView2FaviconImageFormat) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_mixinmethod
    def PrintAsync(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_16, printSettings: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintSettings) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintStatus]: ...
    @winrt_mixinmethod
    def ShowPrintUI(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_16, printDialogKind: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintDialogKind) -> Void: ...
    @winrt_mixinmethod
    def PrintToPdfStreamAsync(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_16, printSettings: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintSettings) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    @winrt_mixinmethod
    def PostSharedBufferToScript(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_17, sharedBuffer: win32more.Microsoft.Web.WebView2.Core.CoreWebView2SharedBuffer, access: win32more.Microsoft.Web.WebView2.Core.CoreWebView2SharedBufferAccess, additionalDataAsJson: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def add_LaunchingExternalUriScheme(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_18, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2LaunchingExternalUriSchemeEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LaunchingExternalUriScheme(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_18, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_MemoryUsageTargetLevel(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_19) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2MemoryUsageTargetLevel: ...
    @winrt_mixinmethod
    def put_MemoryUsageTargetLevel(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_19, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2MemoryUsageTargetLevel) -> Void: ...
    @winrt_mixinmethod
    def get_CookieManager(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_2) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2CookieManager: ...
    @winrt_mixinmethod
    def get_Environment(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_2) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2Environment: ...
    @winrt_mixinmethod
    def add_WebResourceResponseReceived(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceResponseReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_WebResourceResponseReceived(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DOMContentLoaded(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2DOMContentLoadedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DOMContentLoaded(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def NavigateWithWebResourceRequest(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_2, Request: win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceRequest) -> Void: ...
    @winrt_mixinmethod
    def get_FrameId(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_20) -> UInt32: ...
    @winrt_mixinmethod
    def ExecuteScriptWithResultAsync(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_21, javaScript: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Web.WebView2.Core.CoreWebView2ExecuteScriptResult]: ...
    @winrt_mixinmethod
    def add_NotificationReceived(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_24, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2NotificationReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NotificationReceived(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_24, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SaveAsUIShowing(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_25, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2SaveAsUIShowingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SaveAsUIShowing(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_25, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def ShowSaveAsUIAsync(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_25) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Web.WebView2.Core.CoreWebView2SaveAsUIResult]: ...
    @winrt_mixinmethod
    def add_SaveFileSecurityCheckStarting(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_26, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2SaveFileSecurityCheckStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SaveFileSecurityCheckStarting(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_26, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ScreenCaptureStarting(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_27, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2ScreenCaptureStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ScreenCaptureStarting(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_27, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_IsSuspended(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_3) -> Boolean: ...
    @winrt_mixinmethod
    def TrySuspendAsync(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_3) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def Resume(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_3) -> Void: ...
    @winrt_mixinmethod
    def SetVirtualHostNameToFolderMapping(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_3, hostName: WinRT_String, folderPath: WinRT_String, accessKind: win32more.Microsoft.Web.WebView2.Core.CoreWebView2HostResourceAccessKind) -> Void: ...
    @winrt_mixinmethod
    def ClearVirtualHostNameToFolderMapping(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_3, hostName: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def add_FrameCreated(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_4, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2FrameCreatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameCreated(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_4, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DownloadStarting(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_4, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2DownloadStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DownloadStarting(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_4, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ClientCertificateRequested(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_5, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2ClientCertificateRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ClientCertificateRequested(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_5, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def OpenTaskManagerWindow(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_6) -> Void: ...
    @winrt_mixinmethod
    def PrintToPdfAsync(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_7, ResultFilePath: WinRT_String, printSettings: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintSettings) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_IsMuted(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_8) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsMuted(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_8, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsDocumentPlayingAudio(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_8) -> Boolean: ...
    @winrt_mixinmethod
    def add_IsMutedChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_8, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_IsMutedChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_8, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_IsDocumentPlayingAudioChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_8, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_IsDocumentPlayingAudioChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_8, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_IsDefaultDownloadDialogOpen(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_9) -> Boolean: ...
    @winrt_mixinmethod
    def get_DefaultDownloadDialogCornerAlignment(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_9) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2DefaultDownloadDialogCornerAlignment: ...
    @winrt_mixinmethod
    def put_DefaultDownloadDialogCornerAlignment(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_9, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2DefaultDownloadDialogCornerAlignment) -> Void: ...
    @winrt_mixinmethod
    def get_DefaultDownloadDialogMargin(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_9) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_DefaultDownloadDialogMargin(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_9, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def add_IsDefaultDownloadDialogOpenChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_9, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_IsDefaultDownloadDialogOpenChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_9, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def OpenDefaultDownloadDialog(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_9) -> Void: ...
    @winrt_mixinmethod
    def CloseDefaultDownloadDialog(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_9) -> Void: ...
    @winrt_overload
    @winrt_mixinmethod
    def AddWebResourceRequestedFilter(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_Manual, uri: WinRT_String, resourceContext: win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceContext, requestSourceKinds: win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceRequestSourceKinds) -> Void: ...
    @winrt_overload
    @winrt_mixinmethod
    def RemoveWebResourceRequestedFilter(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_Manual, uri: WinRT_String, resourceContext: win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceContext, requestSourceKinds: win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceRequestSourceKinds) -> Void: ...
    @winrt_overload
    @winrt_mixinmethod
    def PostWebMessageAsJson(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2_Manual2, webMessageAsJson: WinRT_String, additionalObjects: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Win32.System.WinRT.IInspectable]) -> Void: ...
    @winrt_mixinmethod
    def get_Settings(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2Settings: ...
    @winrt_mixinmethod
    def get_Source(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_BrowserProcessId(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2) -> UInt32: ...
    @winrt_mixinmethod
    def get_CanGoBack(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanGoForward(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2) -> Boolean: ...
    @winrt_mixinmethod
    def get_DocumentTitle(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ContainsFullScreenElement(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2) -> Boolean: ...
    @winrt_mixinmethod
    def add_NavigationStarting(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2NavigationStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NavigationStarting(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ContentLoading(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2ContentLoadingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ContentLoading(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SourceChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2SourceChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_HistoryChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HistoryChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_NavigationCompleted(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2NavigationCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NavigationCompleted(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_FrameNavigationStarting(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2NavigationStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameNavigationStarting(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_FrameNavigationCompleted(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2NavigationCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameNavigationCompleted(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ScriptDialogOpening(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2ScriptDialogOpeningEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ScriptDialogOpening(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PermissionRequested(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2PermissionRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PermissionRequested(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ProcessFailed(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2ProcessFailedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ProcessFailed(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_WebMessageReceived(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebMessageReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_WebMessageReceived(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_NewWindowRequested(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2NewWindowRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NewWindowRequested(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DocumentTitleChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DocumentTitleChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ContainsFullScreenElementChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ContainsFullScreenElementChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_WebResourceRequested(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_WebResourceRequested(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_WindowCloseRequested(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_WindowCloseRequested(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Navigate(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, uri: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def NavigateToString(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, htmlContent: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def AddScriptToExecuteOnDocumentCreatedAsync(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, javaScript: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def RemoveScriptToExecuteOnDocumentCreated(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, id: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def ExecuteScriptAsync(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, javaScript: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def CapturePreviewAsync(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, imageFormat: win32more.Microsoft.Web.WebView2.Core.CoreWebView2CapturePreviewImageFormat, imageStream: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def Reload(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2) -> Void: ...
    @PostWebMessageAsJson.register
    @winrt_mixinmethod
    def PostWebMessageAsJson(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, webMessageAsJson: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def PostWebMessageAsString(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, webMessageAsString: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def CallDevToolsProtocolMethodAsync(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, methodName: WinRT_String, parametersAsJson: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def GoBack(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2) -> Void: ...
    @winrt_mixinmethod
    def GoForward(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2) -> Void: ...
    @winrt_mixinmethod
    def GetDevToolsProtocolEventReceiver(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, eventName: WinRT_String) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2DevToolsProtocolEventReceiver: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2) -> Void: ...
    @winrt_mixinmethod
    def AddHostObjectToScript(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, name: WinRT_String, rawObject: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def RemoveHostObjectFromScript(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, name: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def OpenDevToolsWindow(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2) -> Void: ...
    @AddWebResourceRequestedFilter.register
    @winrt_mixinmethod
    def AddWebResourceRequestedFilter(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, uri: WinRT_String, ResourceContext: win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceContext) -> Void: ...
    @RemoveWebResourceRequestedFilter.register
    @winrt_mixinmethod
    def RemoveWebResourceRequestedFilter(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2, uri: WinRT_String, ResourceContext: win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceContext) -> Void: ...
    BrowserProcessId = property(get_BrowserProcessId, None)
    CanGoBack = property(get_CanGoBack, None)
    CanGoForward = property(get_CanGoForward, None)
    ContainsFullScreenElement = property(get_ContainsFullScreenElement, None)
    CookieManager = property(get_CookieManager, None)
    DefaultDownloadDialogCornerAlignment = property(get_DefaultDownloadDialogCornerAlignment, put_DefaultDownloadDialogCornerAlignment)
    DefaultDownloadDialogMargin = property(get_DefaultDownloadDialogMargin, put_DefaultDownloadDialogMargin)
    DocumentTitle = property(get_DocumentTitle, None)
    Environment = property(get_Environment, None)
    FaviconUri = property(get_FaviconUri, None)
    FrameId = property(get_FrameId, None)
    IsDefaultDownloadDialogOpen = property(get_IsDefaultDownloadDialogOpen, None)
    IsDocumentPlayingAudio = property(get_IsDocumentPlayingAudio, None)
    IsMuted = property(get_IsMuted, put_IsMuted)
    IsSuspended = property(get_IsSuspended, None)
    MemoryUsageTargetLevel = property(get_MemoryUsageTargetLevel, put_MemoryUsageTargetLevel)
    Profile = property(get_Profile, None)
    Settings = property(get_Settings, None)
    Source = property(get_Source, None)
    StatusBarText = property(get_StatusBarText, None)
    BasicAuthenticationRequested = event()
    ContextMenuRequested = event()
    StatusBarTextChanged = event()
    ServerCertificateErrorDetected = event()
    FaviconChanged = event()
    LaunchingExternalUriScheme = event()
    WebResourceResponseReceived = event()
    DOMContentLoaded = event()
    NotificationReceived = event()
    SaveAsUIShowing = event()
    SaveFileSecurityCheckStarting = event()
    ScreenCaptureStarting = event()
    FrameCreated = event()
    DownloadStarting = event()
    ClientCertificateRequested = event()
    IsMutedChanged = event()
    IsDocumentPlayingAudioChanged = event()
    IsDefaultDownloadDialogOpenChanged = event()
    NavigationStarting = event()
    ContentLoading = event()
    SourceChanged = event()
    HistoryChanged = event()
    NavigationCompleted = event()
    FrameNavigationStarting = event()
    FrameNavigationCompleted = event()
    ScriptDialogOpening = event()
    PermissionRequested = event()
    ProcessFailed = event()
    WebMessageReceived = event()
    NewWindowRequested = event()
    DocumentTitleChanged = event()
    ContainsFullScreenElementChanged = event()
    WebResourceRequested = event()
    WindowCloseRequested = event()
class CoreWebView2AcceleratorKeyPressedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2AcceleratorKeyPressedEventArgs
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2AcceleratorKeyPressedEventArgs'
    @winrt_mixinmethod
    def get_IsBrowserAcceleratorKeyEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2AcceleratorKeyPressedEventArgs2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsBrowserAcceleratorKeyEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2AcceleratorKeyPressedEventArgs2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_KeyEventKind(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2AcceleratorKeyPressedEventArgs) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2KeyEventKind: ...
    @winrt_mixinmethod
    def get_VirtualKey(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2AcceleratorKeyPressedEventArgs) -> UInt32: ...
    @winrt_mixinmethod
    def get_KeyEventLParam(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2AcceleratorKeyPressedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_PhysicalKeyStatus(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2AcceleratorKeyPressedEventArgs) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2PhysicalKeyStatus: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2AcceleratorKeyPressedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2AcceleratorKeyPressedEventArgs, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
    IsBrowserAcceleratorKeyEnabled = property(get_IsBrowserAcceleratorKeyEnabled, put_IsBrowserAcceleratorKeyEnabled)
    KeyEventKind = property(get_KeyEventKind, None)
    KeyEventLParam = property(get_KeyEventLParam, None)
    PhysicalKeyStatus = property(get_PhysicalKeyStatus, None)
    VirtualKey = property(get_VirtualKey, None)
class CoreWebView2BasicAuthenticationRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2BasicAuthenticationRequestedEventArgs
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2BasicAuthenticationRequestedEventArgs'
    @winrt_mixinmethod
    def get_Uri(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2BasicAuthenticationRequestedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Challenge(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2BasicAuthenticationRequestedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Response(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2BasicAuthenticationRequestedEventArgs) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2BasicAuthenticationResponse: ...
    @winrt_mixinmethod
    def get_Cancel(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2BasicAuthenticationRequestedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Cancel(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2BasicAuthenticationRequestedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2BasicAuthenticationRequestedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Cancel = property(get_Cancel, put_Cancel)
    Challenge = property(get_Challenge, None)
    Response = property(get_Response, None)
    Uri = property(get_Uri, None)
class CoreWebView2BasicAuthenticationResponse(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2BasicAuthenticationResponse
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2BasicAuthenticationResponse'
    @winrt_mixinmethod
    def get_UserName(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2BasicAuthenticationResponse) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_UserName(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2BasicAuthenticationResponse, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Password(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2BasicAuthenticationResponse) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Password(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2BasicAuthenticationResponse, value: WinRT_String) -> Void: ...
    Password = property(get_Password, put_Password)
    UserName = property(get_UserName, put_UserName)
class CoreWebView2BoundsMode(Enum, Int32):
    UseRawPixels = 0
    UseRasterizationScale = 1
class CoreWebView2BrowserExtension(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2BrowserExtension
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2BrowserExtension'
    @winrt_mixinmethod
    def get_Id(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2BrowserExtension) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2BrowserExtension) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2BrowserExtension) -> Boolean: ...
    @winrt_mixinmethod
    def RemoveAsync(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2BrowserExtension) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def EnableAsync(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2BrowserExtension, IsEnabled: Boolean) -> win32more.Windows.Foundation.IAsyncAction: ...
    Id = property(get_Id, None)
    IsEnabled = property(get_IsEnabled, None)
    Name = property(get_Name, None)
class CoreWebView2BrowserProcessExitKind(Enum, Int32):
    Normal = 0
    Failed = 1
class CoreWebView2BrowserProcessExitedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2BrowserProcessExitedEventArgs
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2BrowserProcessExitedEventArgs'
    @winrt_mixinmethod
    def get_BrowserProcessExitKind(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2BrowserProcessExitedEventArgs) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2BrowserProcessExitKind: ...
    @winrt_mixinmethod
    def get_BrowserProcessId(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2BrowserProcessExitedEventArgs) -> UInt32: ...
    BrowserProcessExitKind = property(get_BrowserProcessExitKind, None)
    BrowserProcessId = property(get_BrowserProcessId, None)
class CoreWebView2BrowsingDataKinds(Enum, UInt32):
    FileSystems = 1
    IndexedDb = 2
    LocalStorage = 4
    WebSql = 8
    CacheStorage = 16
    AllDomStorage = 32
    Cookies = 64
    AllSite = 128
    DiskCache = 256
    DownloadHistory = 512
    GeneralAutofill = 1024
    PasswordAutosave = 2048
    BrowsingHistory = 4096
    Settings = 8192
    AllProfile = 16384
    ServiceWorkers = 32768
class CoreWebView2CapturePreviewImageFormat(Enum, Int32):
    Png = 0
    Jpeg = 1
class CoreWebView2Certificate(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Certificate
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2Certificate'
    @winrt_mixinmethod
    def ToCertificate(self: win32more.Microsoft.Web.WebView2.Core.CoreWebView2Certificate_Manual) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def get_Subject(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Certificate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Issuer(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Certificate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ValidFrom(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Certificate) -> Double: ...
    @winrt_mixinmethod
    def get_ValidTo(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Certificate) -> Double: ...
    @winrt_mixinmethod
    def get_DerEncodedSerialNumber(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Certificate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Certificate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PemEncodedIssuerCertificateChain(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Certificate) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def ToPemEncoding(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Certificate) -> WinRT_String: ...
    DerEncodedSerialNumber = property(get_DerEncodedSerialNumber, None)
    DisplayName = property(get_DisplayName, None)
    Issuer = property(get_Issuer, None)
    PemEncodedIssuerCertificateChain = property(get_PemEncodedIssuerCertificateChain, None)
    Subject = property(get_Subject, None)
    ValidFrom = property(get_ValidFrom, None)
    ValidTo = property(get_ValidTo, None)
class CoreWebView2Certificate_Manual(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2Certificate_Manual'
    _iid_ = Guid('{4b9b0fe5-0ad9-5594-81e7-b18ecc0636de}')
    @winrt_commethod(6)
    def ToCertificate(self) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
class CoreWebView2ChannelSearchKind(Enum, Int32):
    MostStable = 0
    LeastStable = 1
class CoreWebView2ClientCertificate(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ClientCertificate
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2ClientCertificate'
    @winrt_mixinmethod
    def ToCertificate(self: win32more.Microsoft.Web.WebView2.Core.CoreWebView2ClientCertificate_Manual) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
    @winrt_mixinmethod
    def get_Subject(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ClientCertificate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Issuer(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ClientCertificate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ValidFrom(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ClientCertificate) -> Double: ...
    @winrt_mixinmethod
    def get_ValidTo(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ClientCertificate) -> Double: ...
    @winrt_mixinmethod
    def get_DerEncodedSerialNumber(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ClientCertificate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ClientCertificate) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PemEncodedIssuerCertificateChain(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ClientCertificate) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ClientCertificate) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ClientCertificateKind: ...
    @winrt_mixinmethod
    def ToPemEncoding(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ClientCertificate) -> WinRT_String: ...
    DerEncodedSerialNumber = property(get_DerEncodedSerialNumber, None)
    DisplayName = property(get_DisplayName, None)
    Issuer = property(get_Issuer, None)
    Kind = property(get_Kind, None)
    PemEncodedIssuerCertificateChain = property(get_PemEncodedIssuerCertificateChain, None)
    Subject = property(get_Subject, None)
    ValidFrom = property(get_ValidFrom, None)
    ValidTo = property(get_ValidTo, None)
class CoreWebView2ClientCertificateKind(Enum, Int32):
    SmartCard = 0
    Pin = 1
    Other = 2
class CoreWebView2ClientCertificateRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ClientCertificateRequestedEventArgs
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2ClientCertificateRequestedEventArgs'
    @winrt_mixinmethod
    def get_Host(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ClientCertificateRequestedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Port(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ClientCertificateRequestedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_IsProxy(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ClientCertificateRequestedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_AllowedCertificateAuthorities(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ClientCertificateRequestedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_MutuallyTrustedCertificates(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ClientCertificateRequestedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Web.WebView2.Core.CoreWebView2ClientCertificate]: ...
    @winrt_mixinmethod
    def get_SelectedCertificate(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ClientCertificateRequestedEventArgs) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ClientCertificate: ...
    @winrt_mixinmethod
    def put_SelectedCertificate(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ClientCertificateRequestedEventArgs, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2ClientCertificate) -> Void: ...
    @winrt_mixinmethod
    def get_Cancel(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ClientCertificateRequestedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Cancel(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ClientCertificateRequestedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ClientCertificateRequestedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ClientCertificateRequestedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ClientCertificateRequestedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    AllowedCertificateAuthorities = property(get_AllowedCertificateAuthorities, None)
    Cancel = property(get_Cancel, put_Cancel)
    Handled = property(get_Handled, put_Handled)
    Host = property(get_Host, None)
    IsProxy = property(get_IsProxy, None)
    MutuallyTrustedCertificates = property(get_MutuallyTrustedCertificates, None)
    Port = property(get_Port, None)
    SelectedCertificate = property(get_SelectedCertificate, put_SelectedCertificate)
class CoreWebView2ClientCertificate_Manual(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2ClientCertificate_Manual'
    _iid_ = Guid('{faefefc2-20c3-5d86-8a74-f6d87d6ff8fa}')
    @winrt_commethod(6)
    def ToCertificate(self) -> win32more.Windows.Security.Cryptography.Certificates.Certificate: ...
class CoreWebView2CompositionController(ComPtr):
    extends: win32more.Microsoft.Web.WebView2.Core.CoreWebView2Controller
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CompositionController
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2CompositionController'
    @winrt_mixinmethod
    def DragLeave(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CompositionController3) -> Void: ...
    @winrt_mixinmethod
    def add_NonClientRegionChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CompositionController4, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2CompositionController, win32more.Microsoft.Web.WebView2.Core.CoreWebView2NonClientRegionChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NonClientRegionChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CompositionController4, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetNonClientRegionAtPoint(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CompositionController4, point: win32more.Windows.Foundation.Point) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2NonClientRegionKind: ...
    @winrt_mixinmethod
    def QueryNonClientRegion(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CompositionController4, Kind: win32more.Microsoft.Web.WebView2.Core.CoreWebView2NonClientRegionKind) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Rect]: ...
    @winrt_mixinmethod
    def get_RootVisualTarget(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CompositionController) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def put_RootVisualTarget(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CompositionController, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_mixinmethod
    def add_CursorChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CompositionController, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2CompositionController, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CursorChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CompositionController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def SendMouseInput(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CompositionController, eventKind: win32more.Microsoft.Web.WebView2.Core.CoreWebView2MouseEventKind, virtualKeys: win32more.Microsoft.Web.WebView2.Core.CoreWebView2MouseEventVirtualKeys, mouseData: UInt32, point: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def SendPointerInput(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CompositionController, eventKind: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PointerEventKind, pointerInfo: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PointerInfo) -> Void: ...
    @winrt_mixinmethod
    def get_Cursor(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CompositionController) -> win32more.Windows.UI.Core.CoreCursor: ...
    @winrt_mixinmethod
    def DragEnter(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CompositionController, dragInfo: win32more.Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDragInfo, dragUIOverride: win32more.Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDragUIOverride) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    @winrt_mixinmethod
    def DragOver(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CompositionController, dragInfo: win32more.Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDragInfo, dragUIOverride: win32more.Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDragUIOverride) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    @winrt_mixinmethod
    def Drop(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CompositionController, dragInfo: win32more.Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDragInfo) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    Cursor = property(get_Cursor, None)
    RootVisualTarget = property(get_RootVisualTarget, put_RootVisualTarget)
    NonClientRegionChanged = event()
    CursorChanged = event()
class CoreWebView2ContentLoadingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContentLoadingEventArgs
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2ContentLoadingEventArgs'
    @winrt_mixinmethod
    def get_IsErrorPage(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContentLoadingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_NavigationId(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContentLoadingEventArgs) -> UInt64: ...
    IsErrorPage = property(get_IsErrorPage, None)
    NavigationId = property(get_NavigationId, None)
class CoreWebView2ContextMenuItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuItem
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2ContextMenuItem'
    @winrt_mixinmethod
    def get_Name(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Label(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CommandId(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuItem) -> Int32: ...
    @winrt_mixinmethod
    def get_ShortcutKeyDescription(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuItem) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Icon(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuItem) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuItem) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ContextMenuItemKind: ...
    @winrt_mixinmethod
    def get_IsEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuItem) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuItem, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsChecked(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuItem) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsChecked(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuItem, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Children(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuItem) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.Web.WebView2.Core.CoreWebView2ContextMenuItem]: ...
    @winrt_mixinmethod
    def add_CustomItemSelected(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuItem, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2ContextMenuItem, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CustomItemSelected(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuItem, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Children = property(get_Children, None)
    CommandId = property(get_CommandId, None)
    Icon = property(get_Icon, None)
    IsChecked = property(get_IsChecked, put_IsChecked)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    Kind = property(get_Kind, None)
    Label = property(get_Label, None)
    Name = property(get_Name, None)
    ShortcutKeyDescription = property(get_ShortcutKeyDescription, None)
    CustomItemSelected = event()
class CoreWebView2ContextMenuItemKind(Enum, Int32):
    Command = 0
    CheckBox = 1
    Radio = 2
    Separator = 3
    Submenu = 4
class CoreWebView2ContextMenuRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuRequestedEventArgs
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2ContextMenuRequestedEventArgs'
    @winrt_mixinmethod
    def get_MenuItems(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuRequestedEventArgs) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.Web.WebView2.Core.CoreWebView2ContextMenuItem]: ...
    @winrt_mixinmethod
    def get_ContextMenuTarget(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuRequestedEventArgs) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ContextMenuTarget: ...
    @winrt_mixinmethod
    def get_Location(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuRequestedEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_SelectedCommandId(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuRequestedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def put_SelectedCommandId(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuRequestedEventArgs, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuRequestedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuRequestedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuRequestedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    ContextMenuTarget = property(get_ContextMenuTarget, None)
    Handled = property(get_Handled, put_Handled)
    Location = property(get_Location, None)
    MenuItems = property(get_MenuItems, None)
    SelectedCommandId = property(get_SelectedCommandId, put_SelectedCommandId)
class CoreWebView2ContextMenuTarget(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuTarget
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2ContextMenuTarget'
    @winrt_mixinmethod
    def get_Kind(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuTarget) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ContextMenuTargetKind: ...
    @winrt_mixinmethod
    def get_IsEditable(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuTarget) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsRequestedForMainFrame(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuTarget) -> Boolean: ...
    @winrt_mixinmethod
    def get_PageUri(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuTarget) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FrameUri(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuTarget) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_HasLinkUri(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuTarget) -> Boolean: ...
    @winrt_mixinmethod
    def get_LinkUri(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuTarget) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_HasLinkText(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuTarget) -> Boolean: ...
    @winrt_mixinmethod
    def get_LinkText(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuTarget) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_HasSourceUri(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuTarget) -> Boolean: ...
    @winrt_mixinmethod
    def get_SourceUri(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuTarget) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_HasSelection(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuTarget) -> Boolean: ...
    @winrt_mixinmethod
    def get_SelectionText(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuTarget) -> WinRT_String: ...
    FrameUri = property(get_FrameUri, None)
    HasLinkText = property(get_HasLinkText, None)
    HasLinkUri = property(get_HasLinkUri, None)
    HasSelection = property(get_HasSelection, None)
    HasSourceUri = property(get_HasSourceUri, None)
    IsEditable = property(get_IsEditable, None)
    IsRequestedForMainFrame = property(get_IsRequestedForMainFrame, None)
    Kind = property(get_Kind, None)
    LinkText = property(get_LinkText, None)
    LinkUri = property(get_LinkUri, None)
    PageUri = property(get_PageUri, None)
    SelectionText = property(get_SelectionText, None)
    SourceUri = property(get_SourceUri, None)
class CoreWebView2ContextMenuTargetKind(Enum, Int32):
    Page = 0
    Image = 1
    SelectedText = 2
    Audio = 3
    Video = 4
class CoreWebView2Controller(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2Controller'
    @winrt_mixinmethod
    def get_DefaultBackgroundColor(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller2) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_DefaultBackgroundColor(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller2, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_RasterizationScale(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller3) -> Double: ...
    @winrt_mixinmethod
    def put_RasterizationScale(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller3, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ShouldDetectMonitorScaleChanges(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller3) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShouldDetectMonitorScaleChanges(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_BoundsMode(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller3) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2BoundsMode: ...
    @winrt_mixinmethod
    def put_BoundsMode(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller3, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2BoundsMode) -> Void: ...
    @winrt_mixinmethod
    def add_RasterizationScaleChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller3, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Controller, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RasterizationScaleChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller3, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_AllowExternalDrop(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller4) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowExternalDrop(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller4, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsBrowserHitTransparent(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrivatePartialController) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsVisible(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsVisible(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Bounds(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def put_Bounds(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def get_ZoomFactor(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller) -> Double: ...
    @winrt_mixinmethod
    def put_ZoomFactor(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ParentWindow(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ControllerWindowReference: ...
    @winrt_mixinmethod
    def put_ParentWindow(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2ControllerWindowReference) -> Void: ...
    @winrt_mixinmethod
    def get_CoreWebView2(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2: ...
    @winrt_mixinmethod
    def add_ZoomFactorChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Controller, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ZoomFactorChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_MoveFocusRequested(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Controller, win32more.Microsoft.Web.WebView2.Core.CoreWebView2MoveFocusRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_MoveFocusRequested(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_GotFocus(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Controller, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_GotFocus(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_LostFocus(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Controller, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LostFocus(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_AcceleratorKeyPressed(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Controller, win32more.Microsoft.Web.WebView2.Core.CoreWebView2AcceleratorKeyPressedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AcceleratorKeyPressed(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def SetBoundsAndZoomFactor(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller, Bounds: win32more.Windows.Foundation.Rect, ZoomFactor: Double) -> Void: ...
    @winrt_mixinmethod
    def MoveFocus(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller, reason: win32more.Microsoft.Web.WebView2.Core.CoreWebView2MoveFocusReason) -> Void: ...
    @winrt_mixinmethod
    def NotifyParentWindowPositionChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Controller) -> Void: ...
    AllowExternalDrop = property(get_AllowExternalDrop, put_AllowExternalDrop)
    Bounds = property(get_Bounds, put_Bounds)
    BoundsMode = property(get_BoundsMode, put_BoundsMode)
    CoreWebView2 = property(get_CoreWebView2, None)
    DefaultBackgroundColor = property(get_DefaultBackgroundColor, put_DefaultBackgroundColor)
    IsBrowserHitTransparent = property(get_IsBrowserHitTransparent, None)
    IsVisible = property(get_IsVisible, put_IsVisible)
    ParentWindow = property(get_ParentWindow, put_ParentWindow)
    RasterizationScale = property(get_RasterizationScale, put_RasterizationScale)
    ShouldDetectMonitorScaleChanges = property(get_ShouldDetectMonitorScaleChanges, put_ShouldDetectMonitorScaleChanges)
    ZoomFactor = property(get_ZoomFactor, put_ZoomFactor)
    RasterizationScaleChanged = event()
    ZoomFactorChanged = event()
    MoveFocusRequested = event()
    GotFocus = event()
    LostFocus = event()
    AcceleratorKeyPressed = event()
class CoreWebView2ControllerOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ControllerOptions
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2ControllerOptions'
    @winrt_mixinmethod
    def get_ScriptLocale(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ControllerOptions2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ScriptLocale(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ControllerOptions2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_ProfileName(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ControllerOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ProfileName(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ControllerOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_IsInPrivateModeEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ControllerOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsInPrivateModeEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ControllerOptions, value: Boolean) -> Void: ...
    IsInPrivateModeEnabled = property(get_IsInPrivateModeEnabled, put_IsInPrivateModeEnabled)
    ProfileName = property(get_ProfileName, put_ProfileName)
    ScriptLocale = property(get_ScriptLocale, put_ScriptLocale)
class CoreWebView2ControllerWindowReference(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ControllerWindowReference
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2ControllerWindowReference'
    @winrt_mixinmethod
    def get_WindowHandle(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ControllerWindowReference) -> UInt64: ...
    @winrt_mixinmethod
    def get_CoreWindow(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ControllerWindowReference) -> win32more.Windows.UI.Core.CoreWindow: ...
    @winrt_classmethod
    def CreateFromWindowHandle(cls: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ControllerWindowReferenceStatics, windowHandle: UInt64) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ControllerWindowReference: ...
    @winrt_classmethod
    def CreateFromCoreWindow(cls: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ControllerWindowReferenceStatics, coreWindow: win32more.Windows.UI.Core.CoreWindow) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ControllerWindowReference: ...
    CoreWindow = property(get_CoreWindow, None)
    WindowHandle = property(get_WindowHandle, None)
class CoreWebView2Cookie(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Cookie
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2Cookie'
    @winrt_mixinmethod
    def get_Name(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Cookie) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Cookie) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Value(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Cookie, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Domain(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Cookie) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Path(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Cookie) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Expires(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Cookie) -> Double: ...
    @winrt_mixinmethod
    def put_Expires(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Cookie, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_IsHttpOnly(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Cookie) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsHttpOnly(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Cookie, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SameSite(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Cookie) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2CookieSameSiteKind: ...
    @winrt_mixinmethod
    def put_SameSite(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Cookie, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2CookieSameSiteKind) -> Void: ...
    @winrt_mixinmethod
    def get_IsSecure(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Cookie) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsSecure(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Cookie, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsSession(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Cookie) -> Boolean: ...
    Domain = property(get_Domain, None)
    Expires = property(get_Expires, put_Expires)
    IsHttpOnly = property(get_IsHttpOnly, put_IsHttpOnly)
    IsSecure = property(get_IsSecure, put_IsSecure)
    IsSession = property(get_IsSession, None)
    Name = property(get_Name, None)
    Path = property(get_Path, None)
    SameSite = property(get_SameSite, put_SameSite)
    Value = property(get_Value, put_Value)
class CoreWebView2CookieManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CookieManager
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2CookieManager'
    @winrt_mixinmethod
    def GetCookiesAsync(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CookieManager_Manual, uri: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Cookie]]: ...
    @winrt_mixinmethod
    def CreateCookie(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CookieManager, name: WinRT_String, value: WinRT_String, Domain: WinRT_String, Path: WinRT_String) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2Cookie: ...
    @winrt_mixinmethod
    def CopyCookie(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CookieManager, cookieParam: win32more.Microsoft.Web.WebView2.Core.CoreWebView2Cookie) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2Cookie: ...
    @winrt_mixinmethod
    def AddOrUpdateCookie(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CookieManager, cookie: win32more.Microsoft.Web.WebView2.Core.CoreWebView2Cookie) -> Void: ...
    @winrt_mixinmethod
    def DeleteCookie(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CookieManager, cookie: win32more.Microsoft.Web.WebView2.Core.CoreWebView2Cookie) -> Void: ...
    @winrt_mixinmethod
    def DeleteCookies(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CookieManager, name: WinRT_String, uri: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def DeleteCookiesWithDomainAndPath(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CookieManager, name: WinRT_String, Domain: WinRT_String, Path: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def DeleteAllCookies(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CookieManager) -> Void: ...
class CoreWebView2CookieSameSiteKind(Enum, Int32):
    None_ = 0
    Lax = 1
    Strict = 2
class CoreWebView2CustomSchemeRegistration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CustomSchemeRegistration
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2CustomSchemeRegistration'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.Web.WebView2.Core.CoreWebView2CustomSchemeRegistration.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CustomSchemeRegistrationFactory, schemeName: WinRT_String) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2CustomSchemeRegistration: ...
    @winrt_mixinmethod
    def get_SchemeName(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CustomSchemeRegistration_Manual) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_AllowedOrigins(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CustomSchemeRegistration_Manual) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_TreatAsSecure(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CustomSchemeRegistration) -> Int32: ...
    @winrt_mixinmethod
    def put_TreatAsSecure(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CustomSchemeRegistration, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_HasAuthorityComponent(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CustomSchemeRegistration) -> Boolean: ...
    @winrt_mixinmethod
    def put_HasAuthorityComponent(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2CustomSchemeRegistration, value: Boolean) -> Void: ...
    AllowedOrigins = property(get_AllowedOrigins, None)
    HasAuthorityComponent = property(get_HasAuthorityComponent, put_HasAuthorityComponent)
    SchemeName = property(get_SchemeName, None)
    TreatAsSecure = property(get_TreatAsSecure, put_TreatAsSecure)
class CoreWebView2DOMContentLoadedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DOMContentLoadedEventArgs
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2DOMContentLoadedEventArgs'
    @winrt_mixinmethod
    def get_NavigationId(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DOMContentLoadedEventArgs) -> UInt64: ...
    NavigationId = property(get_NavigationId, None)
class CoreWebView2DefaultDownloadDialogCornerAlignment(Enum, Int32):
    TopLeft = 0
    TopRight = 1
    BottomLeft = 2
    BottomRight = 3
class CoreWebView2DevToolsProtocolEventReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DevToolsProtocolEventReceivedEventArgs
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2DevToolsProtocolEventReceivedEventArgs'
    @winrt_mixinmethod
    def get_SessionId(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DevToolsProtocolEventReceivedEventArgs2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ParameterObjectAsJson(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DevToolsProtocolEventReceivedEventArgs) -> WinRT_String: ...
    ParameterObjectAsJson = property(get_ParameterObjectAsJson, None)
    SessionId = property(get_SessionId, None)
class CoreWebView2DevToolsProtocolEventReceiver(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DevToolsProtocolEventReceiver
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2DevToolsProtocolEventReceiver'
    @winrt_mixinmethod
    def add_DevToolsProtocolEventReceived(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DevToolsProtocolEventReceiver, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2DevToolsProtocolEventReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DevToolsProtocolEventReceived(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DevToolsProtocolEventReceiver, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    DevToolsProtocolEventReceived = event()
class CoreWebView2DownloadInterruptReason(Enum, Int32):
    None_ = 0
    FileFailed = 1
    FileAccessDenied = 2
    FileNoSpace = 3
    FileNameTooLong = 4
    FileTooLarge = 5
    FileMalicious = 6
    FileTransientError = 7
    FileBlockedByPolicy = 8
    FileSecurityCheckFailed = 9
    FileTooShort = 10
    FileHashMismatch = 11
    NetworkFailed = 12
    NetworkTimeout = 13
    NetworkDisconnected = 14
    NetworkServerDown = 15
    NetworkInvalidRequest = 16
    ServerFailed = 17
    ServerNoRange = 18
    ServerBadContent = 19
    ServerUnauthorized = 20
    ServerCertificateProblem = 21
    ServerForbidden = 22
    ServerUnexpectedResponse = 23
    ServerContentLengthMismatch = 24
    ServerCrossOriginRedirect = 25
    UserCanceled = 26
    UserShutdown = 27
    UserPaused = 28
    DownloadProcessCrashed = 29
class CoreWebView2DownloadOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DownloadOperation
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2DownloadOperation'
    @winrt_mixinmethod
    def get_Uri(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DownloadOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ContentDisposition(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DownloadOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_MimeType(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DownloadOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TotalBytesToReceive(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DownloadOperation) -> Int64: ...
    @winrt_mixinmethod
    def get_BytesReceived(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DownloadOperation) -> Int64: ...
    @winrt_mixinmethod
    def get_EstimatedEndTime(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DownloadOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ResultFilePath(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DownloadOperation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DownloadOperation) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2DownloadState: ...
    @winrt_mixinmethod
    def get_InterruptReason(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DownloadOperation) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2DownloadInterruptReason: ...
    @winrt_mixinmethod
    def get_CanResume(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DownloadOperation) -> Boolean: ...
    @winrt_mixinmethod
    def add_BytesReceivedChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DownloadOperation, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2DownloadOperation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BytesReceivedChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DownloadOperation, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EstimatedEndTimeChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DownloadOperation, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2DownloadOperation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EstimatedEndTimeChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DownloadOperation, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_StateChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DownloadOperation, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2DownloadOperation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StateChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DownloadOperation, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Cancel(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DownloadOperation) -> Void: ...
    @winrt_mixinmethod
    def Pause(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DownloadOperation) -> Void: ...
    @winrt_mixinmethod
    def Resume(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DownloadOperation) -> Void: ...
    BytesReceived = property(get_BytesReceived, None)
    CanResume = property(get_CanResume, None)
    ContentDisposition = property(get_ContentDisposition, None)
    EstimatedEndTime = property(get_EstimatedEndTime, None)
    InterruptReason = property(get_InterruptReason, None)
    MimeType = property(get_MimeType, None)
    ResultFilePath = property(get_ResultFilePath, None)
    State = property(get_State, None)
    TotalBytesToReceive = property(get_TotalBytesToReceive, None)
    Uri = property(get_Uri, None)
    BytesReceivedChanged = event()
    EstimatedEndTimeChanged = event()
    StateChanged = event()
class CoreWebView2DownloadStartingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DownloadStartingEventArgs
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2DownloadStartingEventArgs'
    @winrt_mixinmethod
    def get_DownloadOperation(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DownloadStartingEventArgs) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2DownloadOperation: ...
    @winrt_mixinmethod
    def get_Cancel(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DownloadStartingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Cancel(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DownloadStartingEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ResultFilePath(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DownloadStartingEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ResultFilePath(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DownloadStartingEventArgs, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DownloadStartingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DownloadStartingEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DownloadStartingEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Cancel = property(get_Cancel, put_Cancel)
    DownloadOperation = property(get_DownloadOperation, None)
    Handled = property(get_Handled, put_Handled)
    ResultFilePath = property(get_ResultFilePath, put_ResultFilePath)
class CoreWebView2DownloadState(Enum, Int32):
    InProgress = 0
    Interrupted = 1
    Completed = 2
class CoreWebView2Environment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Environment
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2Environment'
    @winrt_mixinmethod
    def CreateCoreWebView2ControllerOptions(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Environment10) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ControllerOptions: ...
    @winrt_mixinmethod
    def get_FailureReportFolderPath(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Environment11) -> WinRT_String: ...
    @winrt_mixinmethod
    def CreateSharedBuffer(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Environment12, Size: UInt64) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2SharedBuffer: ...
    @winrt_mixinmethod
    def GetProcessExtendedInfosAsync(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Environment13) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Web.WebView2.Core.CoreWebView2ProcessExtendedInfo]]: ...
    @winrt_mixinmethod
    def CreateWebFileSystemFileHandle(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Environment14, Path: WinRT_String, Permission: win32more.Microsoft.Web.WebView2.Core.CoreWebView2FileSystemHandlePermission) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2FileSystemHandle: ...
    @winrt_mixinmethod
    def CreateWebFileSystemDirectoryHandle(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Environment14, Path: WinRT_String, Permission: win32more.Microsoft.Web.WebView2.Core.CoreWebView2FileSystemHandlePermission) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2FileSystemHandle: ...
    @winrt_mixinmethod
    def CreateWebResourceRequest(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Environment2, uri: WinRT_String, Method: WinRT_String, postData: win32more.Windows.Storage.Streams.IRandomAccessStream, Headers: WinRT_String) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceRequest: ...
    @winrt_overload
    @winrt_mixinmethod
    def CreateCoreWebView2CompositionControllerAsync(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Environment3, ParentWindow: win32more.Microsoft.Web.WebView2.Core.CoreWebView2ControllerWindowReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Web.WebView2.Core.CoreWebView2CompositionController]: ...
    @winrt_mixinmethod
    def CreateCoreWebView2PointerInfo(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Environment3) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2PointerInfo: ...
    @winrt_mixinmethod
    def add_BrowserProcessExited(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Environment5, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Environment, win32more.Microsoft.Web.WebView2.Core.CoreWebView2BrowserProcessExitedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_BrowserProcessExited(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Environment5, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CreatePrintSettings(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Environment6) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintSettings: ...
    @winrt_mixinmethod
    def get_UserDataFolder(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Environment7) -> WinRT_String: ...
    @winrt_mixinmethod
    def add_ProcessInfosChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Environment8, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Environment, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ProcessInfosChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Environment8, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetProcessInfos(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Environment8) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Web.WebView2.Core.CoreWebView2ProcessInfo]: ...
    @winrt_mixinmethod
    def CreateContextMenuItem(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Environment9, Label: WinRT_String, iconStream: win32more.Windows.Storage.Streams.IRandomAccessStream, Kind: win32more.Microsoft.Web.WebView2.Core.CoreWebView2ContextMenuItemKind) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ContextMenuItem: ...
    @winrt_overload
    @winrt_mixinmethod
    def CreateCoreWebView2ControllerAsync(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Environment_Manual, ParentWindow: win32more.Microsoft.Web.WebView2.Core.CoreWebView2ControllerWindowReference, options: win32more.Microsoft.Web.WebView2.Core.CoreWebView2ControllerOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Controller]: ...
    @CreateCoreWebView2CompositionControllerAsync.register
    @winrt_mixinmethod
    def CreateCoreWebView2CompositionControllerAsync(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Environment_Manual, ParentWindow: win32more.Microsoft.Web.WebView2.Core.CoreWebView2ControllerWindowReference, options: win32more.Microsoft.Web.WebView2.Core.CoreWebView2ControllerOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Web.WebView2.Core.CoreWebView2CompositionController]: ...
    @winrt_mixinmethod
    def get_BrowserVersionString(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Environment) -> WinRT_String: ...
    @winrt_mixinmethod
    def add_NewBrowserVersionAvailable(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Environment, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Environment, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NewBrowserVersionAvailable(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Environment, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @CreateCoreWebView2ControllerAsync.register
    @winrt_mixinmethod
    def CreateCoreWebView2ControllerAsync(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Environment, ParentWindow: win32more.Microsoft.Web.WebView2.Core.CoreWebView2ControllerWindowReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Controller]: ...
    @winrt_mixinmethod
    def CreateWebResourceResponse(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Environment, Content: win32more.Windows.Storage.Streams.IRandomAccessStream, StatusCode: Int32, ReasonPhrase: WinRT_String, Headers: WinRT_String) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceResponse: ...
    @winrt_classmethod
    def GetAvailableBrowserVersionStringWithOptions(cls: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentStatics2, browserExecutableFolder: WinRT_String, options: win32more.Microsoft.Web.WebView2.Core.CoreWebView2EnvironmentOptions) -> WinRT_String: ...
    @winrt_classmethod
    def CreateAsync(cls: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Environment]: ...
    @winrt_classmethod
    def CreateWithOptionsAsync(cls: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentStatics, browserExecutableFolder: WinRT_String, userDataFolder: WinRT_String, options: win32more.Microsoft.Web.WebView2.Core.CoreWebView2EnvironmentOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Environment]: ...
    @winrt_classmethod
    def GetAvailableBrowserVersionString(cls: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentStatics) -> WinRT_String: ...
    @winrt_classmethod
    def GetAvailableBrowserVersionString2(cls: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentStatics, browserExecutableFolder: WinRT_String) -> WinRT_String: ...
    @winrt_classmethod
    def CompareBrowserVersionString(cls: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentStatics, browserVersionString1: WinRT_String, browserVersionString2: WinRT_String) -> Int32: ...
    BrowserVersionString = property(get_BrowserVersionString, None)
    FailureReportFolderPath = property(get_FailureReportFolderPath, None)
    UserDataFolder = property(get_UserDataFolder, None)
    BrowserProcessExited = event()
    ProcessInfosChanged = event()
    NewBrowserVersionAvailable = event()
class CoreWebView2EnvironmentOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2EnvironmentOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.Web.WebView2.Core.CoreWebView2EnvironmentOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2EnvironmentOptions: ...
    @winrt_mixinmethod
    def get_ExclusiveUserDataFolderAccess(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions2) -> Boolean: ...
    @winrt_mixinmethod
    def put_ExclusiveUserDataFolderAccess(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsCustomCrashReportingEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions3) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsCustomCrashReportingEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_EnableTrackingPrevention(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions5) -> Boolean: ...
    @winrt_mixinmethod
    def put_EnableTrackingPrevention(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions5, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AreBrowserExtensionsEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions6) -> Boolean: ...
    @winrt_mixinmethod
    def put_AreBrowserExtensionsEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions6, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ChannelSearchKind(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions7) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ChannelSearchKind: ...
    @winrt_mixinmethod
    def put_ChannelSearchKind(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions7, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2ChannelSearchKind) -> Void: ...
    @winrt_mixinmethod
    def get_ReleaseChannels(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions7) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ReleaseChannels: ...
    @winrt_mixinmethod
    def put_ReleaseChannels(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions7, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2ReleaseChannels) -> Void: ...
    @winrt_mixinmethod
    def get_ScrollBarStyle(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions8) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ScrollbarStyle: ...
    @winrt_mixinmethod
    def put_ScrollBarStyle(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions8, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2ScrollbarStyle) -> Void: ...
    @winrt_mixinmethod
    def get_CustomSchemeRegistrations(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions_Manual3) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.Web.WebView2.Core.CoreWebView2CustomSchemeRegistration]: ...
    @winrt_mixinmethod
    def put_CustomSchemeRegistrations(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions_Manual3, value: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.Web.WebView2.Core.CoreWebView2CustomSchemeRegistration]) -> Void: ...
    @winrt_mixinmethod
    def get_AdditionalBrowserArguments(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_AdditionalBrowserArguments(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Language(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_TargetCompatibleBrowserVersion(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_TargetCompatibleBrowserVersion(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AllowSingleSignOnUsingOSPrimaryAccount(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowSingleSignOnUsingOSPrimaryAccount(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions, value: Boolean) -> Void: ...
    AdditionalBrowserArguments = property(get_AdditionalBrowserArguments, put_AdditionalBrowserArguments)
    AllowSingleSignOnUsingOSPrimaryAccount = property(get_AllowSingleSignOnUsingOSPrimaryAccount, put_AllowSingleSignOnUsingOSPrimaryAccount)
    AreBrowserExtensionsEnabled = property(get_AreBrowserExtensionsEnabled, put_AreBrowserExtensionsEnabled)
    ChannelSearchKind = property(get_ChannelSearchKind, put_ChannelSearchKind)
    CustomSchemeRegistrations = property(get_CustomSchemeRegistrations, put_CustomSchemeRegistrations)
    EnableTrackingPrevention = property(get_EnableTrackingPrevention, put_EnableTrackingPrevention)
    ExclusiveUserDataFolderAccess = property(get_ExclusiveUserDataFolderAccess, put_ExclusiveUserDataFolderAccess)
    IsCustomCrashReportingEnabled = property(get_IsCustomCrashReportingEnabled, put_IsCustomCrashReportingEnabled)
    Language = property(get_Language, put_Language)
    ReleaseChannels = property(get_ReleaseChannels, put_ReleaseChannels)
    ScrollBarStyle = property(get_ScrollBarStyle, put_ScrollBarStyle)
    TargetCompatibleBrowserVersion = property(get_TargetCompatibleBrowserVersion, put_TargetCompatibleBrowserVersion)
class CoreWebView2ExecuteScriptResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ExecuteScriptResult
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2ExecuteScriptResult'
    @winrt_mixinmethod
    def TryGetResultAsString(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ExecuteScriptResult_Manual, stringResult: POINTER(WinRT_String)) -> Int32: ...
    @winrt_mixinmethod
    def get_Succeeded(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ExecuteScriptResult) -> Boolean: ...
    @winrt_mixinmethod
    def get_ResultAsJson(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ExecuteScriptResult) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Exception(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ExecuteScriptResult) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ScriptException: ...
    Exception = property(get_Exception, None)
    ResultAsJson = property(get_ResultAsJson, None)
    Succeeded = property(get_Succeeded, None)
class CoreWebView2FaviconImageFormat(Enum, Int32):
    Png = 0
    Jpeg = 1
class CoreWebView2File(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2File
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2File'
    @winrt_mixinmethod
    def get_Path(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2File) -> WinRT_String: ...
    Path = property(get_Path, None)
class CoreWebView2FileSystemHandle(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2FileSystemHandle
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2FileSystemHandle'
    @winrt_mixinmethod
    def get_Kind(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2FileSystemHandle) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2FileSystemHandleKind: ...
    @winrt_mixinmethod
    def get_Path(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2FileSystemHandle) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Permission(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2FileSystemHandle) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2FileSystemHandlePermission: ...
    Kind = property(get_Kind, None)
    Path = property(get_Path, None)
    Permission = property(get_Permission, None)
class CoreWebView2FileSystemHandleKind(Enum, Int32):
    File = 0
    Directory = 1
class CoreWebView2FileSystemHandlePermission(Enum, Int32):
    ReadOnly = 0
    ReadWrite = 1
class CoreWebView2Frame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Frame
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2Frame'
    @winrt_mixinmethod
    def add_NavigationStarting(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Frame2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Frame, win32more.Microsoft.Web.WebView2.Core.CoreWebView2NavigationStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NavigationStarting(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Frame2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ContentLoading(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Frame2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Frame, win32more.Microsoft.Web.WebView2.Core.CoreWebView2ContentLoadingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ContentLoading(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Frame2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_NavigationCompleted(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Frame2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Frame, win32more.Microsoft.Web.WebView2.Core.CoreWebView2NavigationCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NavigationCompleted(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Frame2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DOMContentLoaded(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Frame2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Frame, win32more.Microsoft.Web.WebView2.Core.CoreWebView2DOMContentLoadedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DOMContentLoaded(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Frame2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_WebMessageReceived(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Frame2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Frame, win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebMessageReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_WebMessageReceived(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Frame2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def ExecuteScriptAsync(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Frame2, javaScript: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def PostWebMessageAsJson(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Frame2, webMessageAsJson: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def PostWebMessageAsString(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Frame2, webMessageAsString: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def add_PermissionRequested(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Frame3, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Frame, win32more.Microsoft.Web.WebView2.Core.CoreWebView2PermissionRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PermissionRequested(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Frame3, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def PostSharedBufferToScript(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Frame4, sharedBuffer: win32more.Microsoft.Web.WebView2.Core.CoreWebView2SharedBuffer, access: win32more.Microsoft.Web.WebView2.Core.CoreWebView2SharedBufferAccess, additionalDataAsJson: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FrameId(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Frame5) -> UInt32: ...
    @winrt_mixinmethod
    def add_ScreenCaptureStarting(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Frame6, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Frame, win32more.Microsoft.Web.WebView2.Core.CoreWebView2ScreenCaptureStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ScreenCaptureStarting(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Frame6, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Frame) -> WinRT_String: ...
    @winrt_mixinmethod
    def add_NameChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Frame, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Frame, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NameChanged(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Frame, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Destroyed(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Frame, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Frame, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Destroyed(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Frame, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def RemoveHostObjectFromScript(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Frame, name: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def IsDestroyed(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Frame) -> Int32: ...
    FrameId = property(get_FrameId, None)
    Name = property(get_Name, None)
    NavigationStarting = event()
    ContentLoading = event()
    NavigationCompleted = event()
    DOMContentLoaded = event()
    WebMessageReceived = event()
    PermissionRequested = event()
    ScreenCaptureStarting = event()
    NameChanged = event()
    Destroyed = event()
class CoreWebView2FrameCreatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2FrameCreatedEventArgs
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2FrameCreatedEventArgs'
    @winrt_mixinmethod
    def get_Frame(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2FrameCreatedEventArgs) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2Frame: ...
    Frame = property(get_Frame, None)
class CoreWebView2FrameInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2FrameInfo
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2FrameInfo'
    @winrt_mixinmethod
    def get_ParentFrameInfo(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2FrameInfo2) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2FrameInfo: ...
    @winrt_mixinmethod
    def get_FrameId(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2FrameInfo2) -> UInt32: ...
    @winrt_mixinmethod
    def get_FrameKind(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2FrameInfo2) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2FrameKind: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2FrameInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Source(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2FrameInfo) -> WinRT_String: ...
    FrameId = property(get_FrameId, None)
    FrameKind = property(get_FrameKind, None)
    Name = property(get_Name, None)
    ParentFrameInfo = property(get_ParentFrameInfo, None)
    Source = property(get_Source, None)
class CoreWebView2FrameKind(Enum, Int32):
    Unknown = 0
    MainFrame = 1
    Iframe = 2
    Embed = 3
    Object = 4
class CoreWebView2HostResourceAccessKind(Enum, Int32):
    Deny = 0
    Allow = 1
    DenyCors = 2
class CoreWebView2HttpHeadersCollectionIterator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2HttpHeadersCollectionIterator
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2HttpHeadersCollectionIterator'
    @winrt_mixinmethod
    def get_Current(self: win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]: ...
    @winrt_mixinmethod
    def get_HasCurrent(self: win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> Boolean: ...
    @winrt_mixinmethod
    def MoveNext(self: win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> Boolean: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]], items: FillArray[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> UInt32: ...
    Current = property(get_Current, None)
    HasCurrent = property(get_HasCurrent, None)
class CoreWebView2HttpRequestHeaders(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[IterableProtocol[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]]
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2HttpRequestHeaders
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2HttpRequestHeaders'
    @winrt_mixinmethod
    def GetHeader(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2HttpRequestHeaders, name: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetHeaders(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2HttpRequestHeaders, name: WinRT_String) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2HttpHeadersCollectionIterator: ...
    @winrt_mixinmethod
    def Contains(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2HttpRequestHeaders, name: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def SetHeader(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2HttpRequestHeaders, name: WinRT_String, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def RemoveHeader(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2HttpRequestHeaders, name: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]: ...
class CoreWebView2HttpResponseHeaders(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[IterableProtocol[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]]
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2HttpResponseHeaders
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2HttpResponseHeaders'
    @winrt_mixinmethod
    def AppendHeader(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2HttpResponseHeaders, name: WinRT_String, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Contains(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2HttpResponseHeaders, name: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def GetHeader(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2HttpResponseHeaders, name: WinRT_String) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetHeaders(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2HttpResponseHeaders, name: WinRT_String) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2HttpHeadersCollectionIterator: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, WinRT_String]]: ...
class CoreWebView2KeyEventKind(Enum, Int32):
    KeyDown = 0
    KeyUp = 1
    SystemKeyDown = 2
    SystemKeyUp = 3
class CoreWebView2LaunchingExternalUriSchemeEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2LaunchingExternalUriSchemeEventArgs
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2LaunchingExternalUriSchemeEventArgs'
    @winrt_mixinmethod
    def get_Uri(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2LaunchingExternalUriSchemeEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_InitiatingOrigin(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2LaunchingExternalUriSchemeEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsUserInitiated(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2LaunchingExternalUriSchemeEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_Cancel(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2LaunchingExternalUriSchemeEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Cancel(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2LaunchingExternalUriSchemeEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2LaunchingExternalUriSchemeEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Cancel = property(get_Cancel, put_Cancel)
    InitiatingOrigin = property(get_InitiatingOrigin, None)
    IsUserInitiated = property(get_IsUserInitiated, None)
    Uri = property(get_Uri, None)
class CoreWebView2MemoryUsageTargetLevel(Enum, Int32):
    Normal = 0
    Low = 1
class CoreWebView2MouseEventKind(Enum, Int32):
    HorizontalWheel = 526
    LeftButtonDoubleClick = 515
    LeftButtonDown = 513
    LeftButtonUp = 514
    Leave = 675
    MiddleButtonDoubleClick = 521
    MiddleButtonDown = 519
    MiddleButtonUp = 520
    Move = 512
    RightButtonDoubleClick = 518
    RightButtonDown = 516
    RightButtonUp = 517
    Wheel = 522
    XButtonDoubleClick = 525
    XButtonDown = 523
    XButtonUp = 524
    NonClientRightButtonDown = 164
    NonClientRightButtonUp = 165
class CoreWebView2MouseEventVirtualKeys(Enum, UInt32):
    None_ = 0
    LeftButton = 1
    RightButton = 2
    Shift = 4
    Control = 8
    MiddleButton = 16
    XButton1 = 32
    XButton2 = 64
class CoreWebView2MoveFocusReason(Enum, Int32):
    Programmatic = 0
    Next = 1
    Previous = 2
class CoreWebView2MoveFocusRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2MoveFocusRequestedEventArgs
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2MoveFocusRequestedEventArgs'
    @winrt_mixinmethod
    def get_Reason(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2MoveFocusRequestedEventArgs) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2MoveFocusReason: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2MoveFocusRequestedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2MoveFocusRequestedEventArgs, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
    Reason = property(get_Reason, None)
class CoreWebView2NavigationCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NavigationCompletedEventArgs
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2NavigationCompletedEventArgs'
    @winrt_mixinmethod
    def get_HttpStatusCode(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NavigationCompletedEventArgs2) -> Int32: ...
    @winrt_mixinmethod
    def get_IsSuccess(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NavigationCompletedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_WebErrorStatus(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NavigationCompletedEventArgs) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebErrorStatus: ...
    @winrt_mixinmethod
    def get_NavigationId(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NavigationCompletedEventArgs) -> UInt64: ...
    HttpStatusCode = property(get_HttpStatusCode, None)
    IsSuccess = property(get_IsSuccess, None)
    NavigationId = property(get_NavigationId, None)
    WebErrorStatus = property(get_WebErrorStatus, None)
class CoreWebView2NavigationKind(Enum, Int32):
    Reload = 0
    BackOrForward = 1
    NewDocument = 2
class CoreWebView2NavigationStartingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NavigationStartingEventArgs
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2NavigationStartingEventArgs'
    @winrt_mixinmethod
    def get_AdditionalAllowedFrameAncestors(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NavigationStartingEventArgs2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_AdditionalAllowedFrameAncestors(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NavigationStartingEventArgs2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_NavigationKind(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NavigationStartingEventArgs3) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2NavigationKind: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NavigationStartingEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsUserInitiated(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NavigationStartingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsRedirected(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NavigationStartingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_RequestHeaders(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NavigationStartingEventArgs) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2HttpRequestHeaders: ...
    @winrt_mixinmethod
    def get_Cancel(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NavigationStartingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Cancel(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NavigationStartingEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_NavigationId(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NavigationStartingEventArgs) -> UInt64: ...
    AdditionalAllowedFrameAncestors = property(get_AdditionalAllowedFrameAncestors, put_AdditionalAllowedFrameAncestors)
    Cancel = property(get_Cancel, put_Cancel)
    IsRedirected = property(get_IsRedirected, None)
    IsUserInitiated = property(get_IsUserInitiated, None)
    NavigationId = property(get_NavigationId, None)
    NavigationKind = property(get_NavigationKind, None)
    RequestHeaders = property(get_RequestHeaders, None)
    Uri = property(get_Uri, None)
class CoreWebView2NewWindowRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NewWindowRequestedEventArgs
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2NewWindowRequestedEventArgs'
    @winrt_mixinmethod
    def get_Name(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NewWindowRequestedEventArgs2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_OriginalSourceFrameInfo(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NewWindowRequestedEventArgs3) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2FrameInfo: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NewWindowRequestedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_NewWindow(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NewWindowRequestedEventArgs) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2: ...
    @winrt_mixinmethod
    def put_NewWindow(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NewWindowRequestedEventArgs, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2) -> Void: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NewWindowRequestedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NewWindowRequestedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsUserInitiated(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NewWindowRequestedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_WindowFeatures(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NewWindowRequestedEventArgs) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2WindowFeatures: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NewWindowRequestedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Handled = property(get_Handled, put_Handled)
    IsUserInitiated = property(get_IsUserInitiated, None)
    Name = property(get_Name, None)
    NewWindow = property(get_NewWindow, put_NewWindow)
    OriginalSourceFrameInfo = property(get_OriginalSourceFrameInfo, None)
    Uri = property(get_Uri, None)
    WindowFeatures = property(get_WindowFeatures, None)
class CoreWebView2NonClientRegionChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NonClientRegionChangedEventArgs
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2NonClientRegionChangedEventArgs'
    @winrt_mixinmethod
    def get_RegionKind(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NonClientRegionChangedEventArgs) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2NonClientRegionKind: ...
    RegionKind = property(get_RegionKind, None)
class CoreWebView2NonClientRegionKind(Enum, Int32):
    Nowhere = 0
    Client = 1
    Caption = 2
    Minimize = 8
    Maximize = 9
    Close = 20
class CoreWebView2Notification(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Notification
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2Notification'
    @winrt_mixinmethod
    def get_VibrationPattern(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Notification_Manual2) -> win32more.Windows.Foundation.Collections.IVectorView[UInt64]: ...
    @winrt_mixinmethod
    def get_Body(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Notification) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Direction(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Notification) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2TextDirectionKind: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Notification) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Tag(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Notification) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IconUri(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Notification) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Notification) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_BadgeUri(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Notification) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_BodyImageUri(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Notification) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ShouldRenotify(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Notification) -> Boolean: ...
    @winrt_mixinmethod
    def get_RequiresInteraction(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Notification) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsSilent(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Notification) -> Boolean: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Notification) -> Double: ...
    @winrt_mixinmethod
    def add_CloseRequested(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Notification, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Notification, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CloseRequested(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Notification, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def ReportShown(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Notification) -> Void: ...
    @winrt_mixinmethod
    def ReportClicked(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Notification) -> Void: ...
    @winrt_mixinmethod
    def ReportClosed(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Notification) -> Void: ...
    BadgeUri = property(get_BadgeUri, None)
    Body = property(get_Body, None)
    BodyImageUri = property(get_BodyImageUri, None)
    Direction = property(get_Direction, None)
    IconUri = property(get_IconUri, None)
    IsSilent = property(get_IsSilent, None)
    Language = property(get_Language, None)
    RequiresInteraction = property(get_RequiresInteraction, None)
    ShouldRenotify = property(get_ShouldRenotify, None)
    Tag = property(get_Tag, None)
    Timestamp = property(get_Timestamp, None)
    Title = property(get_Title, None)
    VibrationPattern = property(get_VibrationPattern, None)
    CloseRequested = event()
class CoreWebView2NotificationReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NotificationReceivedEventArgs
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2NotificationReceivedEventArgs'
    @winrt_mixinmethod
    def get_SenderOrigin(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NotificationReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Notification(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NotificationReceivedEventArgs) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2Notification: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NotificationReceivedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NotificationReceivedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2NotificationReceivedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Handled = property(get_Handled, put_Handled)
    Notification = property(get_Notification, None)
    SenderOrigin = property(get_SenderOrigin, None)
class CoreWebView2PdfToolbarItems(Enum, UInt32):
    None_ = 0
    Save = 1
    Print = 2
    SaveAs = 4
    ZoomIn = 8
    ZoomOut = 16
    Rotate = 32
    FitPage = 64
    PageLayout = 128
    Bookmarks = 256
    PageSelector = 512
    Search = 1024
    FullScreen = 2048
    MoreSettings = 4096
class CoreWebView2PermissionKind(Enum, Int32):
    UnknownPermission = 0
    Microphone = 1
    Camera = 2
    Geolocation = 3
    Notifications = 4
    OtherSensors = 5
    ClipboardRead = 6
    MultipleAutomaticDownloads = 7
    FileReadWrite = 8
    Autoplay = 9
    LocalFonts = 10
    MidiSystemExclusiveMessages = 11
    WindowManagement = 12
class CoreWebView2PermissionRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PermissionRequestedEventArgs
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2PermissionRequestedEventArgs'
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PermissionRequestedEventArgs2) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PermissionRequestedEventArgs2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SavesInProfile(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PermissionRequestedEventArgs3) -> Boolean: ...
    @winrt_mixinmethod
    def put_SavesInProfile(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PermissionRequestedEventArgs3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PermissionRequestedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PermissionKind(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PermissionRequestedEventArgs) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2PermissionKind: ...
    @winrt_mixinmethod
    def get_IsUserInitiated(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PermissionRequestedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PermissionRequestedEventArgs) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2PermissionState: ...
    @winrt_mixinmethod
    def put_State(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PermissionRequestedEventArgs, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PermissionState) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PermissionRequestedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Handled = property(get_Handled, put_Handled)
    IsUserInitiated = property(get_IsUserInitiated, None)
    PermissionKind = property(get_PermissionKind, None)
    SavesInProfile = property(get_SavesInProfile, put_SavesInProfile)
    State = property(get_State, put_State)
    Uri = property(get_Uri, None)
class CoreWebView2PermissionSetting(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PermissionSetting
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2PermissionSetting'
    @winrt_mixinmethod
    def get_PermissionKind(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PermissionSetting) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2PermissionKind: ...
    @winrt_mixinmethod
    def get_PermissionOrigin(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PermissionSetting) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PermissionState(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PermissionSetting) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2PermissionState: ...
    PermissionKind = property(get_PermissionKind, None)
    PermissionOrigin = property(get_PermissionOrigin, None)
    PermissionState = property(get_PermissionState, None)
class CoreWebView2PermissionState(Enum, Int32):
    Default = 0
    Allow = 1
    Deny = 2
class CoreWebView2PhysicalKeyStatus(Structure):
    RepeatCount: UInt32
    ScanCode: UInt32
    IsExtendedKey: Int32
    IsMenuKeyDown: Int32
    WasKeyDown: Int32
    IsKeyReleased: Int32
class CoreWebView2PointerEventKind(Enum, Int32):
    Activate = 587
    Down = 582
    Enter = 585
    Leave = 586
    Up = 583
    Update = 581
class CoreWebView2PointerInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2PointerInfo'
    @winrt_mixinmethod
    def get_PointerKind(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo) -> UInt32: ...
    @winrt_mixinmethod
    def put_PointerKind(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_PointerId(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo) -> UInt32: ...
    @winrt_mixinmethod
    def put_PointerId(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_FrameId(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo) -> UInt32: ...
    @winrt_mixinmethod
    def put_FrameId(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_PointerFlags(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo) -> UInt32: ...
    @winrt_mixinmethod
    def put_PointerFlags(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_PointerDeviceRect(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def put_PointerDeviceRect(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayRect(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def put_DisplayRect(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def get_PixelLocation(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_PixelLocation(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_HimetricLocation(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_HimetricLocation(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_PixelLocationRaw(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_PixelLocationRaw(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_HimetricLocationRaw(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_HimetricLocationRaw(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_Time(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo) -> UInt32: ...
    @winrt_mixinmethod
    def put_Time(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_HistoryCount(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo) -> UInt32: ...
    @winrt_mixinmethod
    def put_HistoryCount(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_InputData(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo) -> Int32: ...
    @winrt_mixinmethod
    def put_InputData(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_KeyStates(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo) -> UInt32: ...
    @winrt_mixinmethod
    def put_KeyStates(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_PerformanceCount(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo) -> UInt64: ...
    @winrt_mixinmethod
    def put_PerformanceCount(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo, value: UInt64) -> Void: ...
    @winrt_mixinmethod
    def get_ButtonChangeKind(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo) -> Int32: ...
    @winrt_mixinmethod
    def put_ButtonChangeKind(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_PenFlags(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo) -> UInt32: ...
    @winrt_mixinmethod
    def put_PenFlags(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_PenMask(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo) -> UInt32: ...
    @winrt_mixinmethod
    def put_PenMask(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_PenPressure(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo) -> UInt32: ...
    @winrt_mixinmethod
    def put_PenPressure(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_PenRotation(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo) -> UInt32: ...
    @winrt_mixinmethod
    def put_PenRotation(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_PenTiltX(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo) -> Int32: ...
    @winrt_mixinmethod
    def put_PenTiltX(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_PenTiltY(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo) -> Int32: ...
    @winrt_mixinmethod
    def put_PenTiltY(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_TouchFlags(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo) -> UInt32: ...
    @winrt_mixinmethod
    def put_TouchFlags(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_TouchMask(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo) -> UInt32: ...
    @winrt_mixinmethod
    def put_TouchMask(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_TouchContact(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def put_TouchContact(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def get_TouchContactRaw(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def put_TouchContactRaw(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def get_TouchOrientation(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo) -> UInt32: ...
    @winrt_mixinmethod
    def put_TouchOrientation(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_TouchPressure(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo) -> UInt32: ...
    @winrt_mixinmethod
    def put_TouchPressure(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo, value: UInt32) -> Void: ...
    ButtonChangeKind = property(get_ButtonChangeKind, put_ButtonChangeKind)
    DisplayRect = property(get_DisplayRect, put_DisplayRect)
    FrameId = property(get_FrameId, put_FrameId)
    HimetricLocation = property(get_HimetricLocation, put_HimetricLocation)
    HimetricLocationRaw = property(get_HimetricLocationRaw, put_HimetricLocationRaw)
    HistoryCount = property(get_HistoryCount, put_HistoryCount)
    InputData = property(get_InputData, put_InputData)
    KeyStates = property(get_KeyStates, put_KeyStates)
    PenFlags = property(get_PenFlags, put_PenFlags)
    PenMask = property(get_PenMask, put_PenMask)
    PenPressure = property(get_PenPressure, put_PenPressure)
    PenRotation = property(get_PenRotation, put_PenRotation)
    PenTiltX = property(get_PenTiltX, put_PenTiltX)
    PenTiltY = property(get_PenTiltY, put_PenTiltY)
    PerformanceCount = property(get_PerformanceCount, put_PerformanceCount)
    PixelLocation = property(get_PixelLocation, put_PixelLocation)
    PixelLocationRaw = property(get_PixelLocationRaw, put_PixelLocationRaw)
    PointerDeviceRect = property(get_PointerDeviceRect, put_PointerDeviceRect)
    PointerFlags = property(get_PointerFlags, put_PointerFlags)
    PointerId = property(get_PointerId, put_PointerId)
    PointerKind = property(get_PointerKind, put_PointerKind)
    Time = property(get_Time, put_Time)
    TouchContact = property(get_TouchContact, put_TouchContact)
    TouchContactRaw = property(get_TouchContactRaw, put_TouchContactRaw)
    TouchFlags = property(get_TouchFlags, put_TouchFlags)
    TouchMask = property(get_TouchMask, put_TouchMask)
    TouchOrientation = property(get_TouchOrientation, put_TouchOrientation)
    TouchPressure = property(get_TouchPressure, put_TouchPressure)
class CoreWebView2PreferredColorScheme(Enum, Int32):
    Auto = 0
    Light = 1
    Dark = 2
class CoreWebView2PrintCollation(Enum, Int32):
    Default = 0
    Collated = 1
    Uncollated = 2
class CoreWebView2PrintColorMode(Enum, Int32):
    Default = 0
    Color = 1
    Grayscale = 2
class CoreWebView2PrintDialogKind(Enum, Int32):
    Browser = 0
    System = 1
class CoreWebView2PrintDuplex(Enum, Int32):
    Default = 0
    OneSided = 1
    TwoSidedLongEdge = 2
    TwoSidedShortEdge = 3
class CoreWebView2PrintMediaSize(Enum, Int32):
    Default = 0
    Custom = 1
class CoreWebView2PrintOrientation(Enum, Int32):
    Portrait = 0
    Landscape = 1
class CoreWebView2PrintSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2PrintSettings'
    @winrt_mixinmethod
    def get_PageRanges(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PageRanges(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_PagesPerSide(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings2) -> Int32: ...
    @winrt_mixinmethod
    def put_PagesPerSide(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings2, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_Copies(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings2) -> Int32: ...
    @winrt_mixinmethod
    def put_Copies(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings2, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_Collation(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings2) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintCollation: ...
    @winrt_mixinmethod
    def put_Collation(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings2, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintCollation) -> Void: ...
    @winrt_mixinmethod
    def get_ColorMode(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings2) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintColorMode: ...
    @winrt_mixinmethod
    def put_ColorMode(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings2, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintColorMode) -> Void: ...
    @winrt_mixinmethod
    def get_Duplex(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings2) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintDuplex: ...
    @winrt_mixinmethod
    def put_Duplex(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings2, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintDuplex) -> Void: ...
    @winrt_mixinmethod
    def get_MediaSize(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings2) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintMediaSize: ...
    @winrt_mixinmethod
    def put_MediaSize(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings2, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintMediaSize) -> Void: ...
    @winrt_mixinmethod
    def get_PrinterName(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_PrinterName(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Orientation(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintOrientation: ...
    @winrt_mixinmethod
    def put_Orientation(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintOrientation) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleFactor(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings) -> Double: ...
    @winrt_mixinmethod
    def put_ScaleFactor(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_PageWidth(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings) -> Double: ...
    @winrt_mixinmethod
    def put_PageWidth(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_PageHeight(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings) -> Double: ...
    @winrt_mixinmethod
    def put_PageHeight(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_MarginTop(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings) -> Double: ...
    @winrt_mixinmethod
    def put_MarginTop(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_MarginBottom(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings) -> Double: ...
    @winrt_mixinmethod
    def put_MarginBottom(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_MarginLeft(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings) -> Double: ...
    @winrt_mixinmethod
    def put_MarginLeft(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_MarginRight(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings) -> Double: ...
    @winrt_mixinmethod
    def put_MarginRight(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ShouldPrintBackgrounds(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShouldPrintBackgrounds(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ShouldPrintSelectionOnly(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShouldPrintSelectionOnly(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ShouldPrintHeaderAndFooter(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShouldPrintHeaderAndFooter(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_HeaderTitle(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_HeaderTitle(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_FooterUri(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_FooterUri(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings, value: WinRT_String) -> Void: ...
    Collation = property(get_Collation, put_Collation)
    ColorMode = property(get_ColorMode, put_ColorMode)
    Copies = property(get_Copies, put_Copies)
    Duplex = property(get_Duplex, put_Duplex)
    FooterUri = property(get_FooterUri, put_FooterUri)
    HeaderTitle = property(get_HeaderTitle, put_HeaderTitle)
    MarginBottom = property(get_MarginBottom, put_MarginBottom)
    MarginLeft = property(get_MarginLeft, put_MarginLeft)
    MarginRight = property(get_MarginRight, put_MarginRight)
    MarginTop = property(get_MarginTop, put_MarginTop)
    MediaSize = property(get_MediaSize, put_MediaSize)
    Orientation = property(get_Orientation, put_Orientation)
    PageHeight = property(get_PageHeight, put_PageHeight)
    PageRanges = property(get_PageRanges, put_PageRanges)
    PageWidth = property(get_PageWidth, put_PageWidth)
    PagesPerSide = property(get_PagesPerSide, put_PagesPerSide)
    PrinterName = property(get_PrinterName, put_PrinterName)
    ScaleFactor = property(get_ScaleFactor, put_ScaleFactor)
    ShouldPrintBackgrounds = property(get_ShouldPrintBackgrounds, put_ShouldPrintBackgrounds)
    ShouldPrintHeaderAndFooter = property(get_ShouldPrintHeaderAndFooter, put_ShouldPrintHeaderAndFooter)
    ShouldPrintSelectionOnly = property(get_ShouldPrintSelectionOnly, put_ShouldPrintSelectionOnly)
class CoreWebView2PrintStatus(Enum, Int32):
    Succeeded = 0
    PrinterUnavailable = 1
    OtherError = 2
class CoreWebView2ProcessExtendedInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ProcessExtendedInfo
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2ProcessExtendedInfo'
    @winrt_mixinmethod
    def get_ProcessInfo(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ProcessExtendedInfo) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ProcessInfo: ...
    @winrt_mixinmethod
    def get_AssociatedFrameInfos(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ProcessExtendedInfo) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Web.WebView2.Core.CoreWebView2FrameInfo]: ...
    AssociatedFrameInfos = property(get_AssociatedFrameInfos, None)
    ProcessInfo = property(get_ProcessInfo, None)
class CoreWebView2ProcessFailedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ProcessFailedEventArgs
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2ProcessFailedEventArgs'
    @winrt_mixinmethod
    def get_Reason(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ProcessFailedEventArgs2) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ProcessFailedReason: ...
    @winrt_mixinmethod
    def get_ExitCode(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ProcessFailedEventArgs2) -> Int32: ...
    @winrt_mixinmethod
    def get_ProcessDescription(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ProcessFailedEventArgs2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FrameInfosForFailedProcess(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ProcessFailedEventArgs2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Web.WebView2.Core.CoreWebView2FrameInfo]: ...
    @winrt_mixinmethod
    def get_FailureSourceModulePath(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ProcessFailedEventArgs3) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ProcessFailedKind(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ProcessFailedEventArgs) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ProcessFailedKind: ...
    ExitCode = property(get_ExitCode, None)
    FailureSourceModulePath = property(get_FailureSourceModulePath, None)
    FrameInfosForFailedProcess = property(get_FrameInfosForFailedProcess, None)
    ProcessDescription = property(get_ProcessDescription, None)
    ProcessFailedKind = property(get_ProcessFailedKind, None)
    Reason = property(get_Reason, None)
class CoreWebView2ProcessFailedKind(Enum, Int32):
    BrowserProcessExited = 0
    RenderProcessExited = 1
    RenderProcessUnresponsive = 2
    FrameRenderProcessExited = 3
    UtilityProcessExited = 4
    SandboxHelperProcessExited = 5
    GpuProcessExited = 6
    PpapiPluginProcessExited = 7
    PpapiBrokerProcessExited = 8
    UnknownProcessExited = 9
class CoreWebView2ProcessFailedReason(Enum, Int32):
    Unexpected = 0
    Unresponsive = 1
    Terminated = 2
    Crashed = 3
    LaunchFailed = 4
    OutOfMemory = 5
    ProfileDeleted = 6
class CoreWebView2ProcessInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ProcessInfo
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2ProcessInfo'
    @winrt_mixinmethod
    def get_ProcessId(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ProcessInfo) -> Int32: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ProcessInfo) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ProcessKind: ...
    Kind = property(get_Kind, None)
    ProcessId = property(get_ProcessId, None)
class CoreWebView2ProcessKind(Enum, Int32):
    Browser = 0
    Renderer = 1
    Utility = 2
    SandboxHelper = 3
    Gpu = 4
    PpapiPlugin = 5
    PpapiBroker = 6
class CoreWebView2Profile(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Profile
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2Profile'
    @winrt_overload
    @winrt_mixinmethod
    def ClearBrowsingDataAsync(self: win32more.Microsoft.Web.WebView2.Core.CoreWebView2Profile_Manual, dataKinds: win32more.Microsoft.Web.WebView2.Core.CoreWebView2BrowsingDataKinds, startTime: win32more.Windows.Foundation.DateTime, endTime: win32more.Windows.Foundation.DateTime) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def ClearBrowsingDataAsync2(self: win32more.Microsoft.Web.WebView2.Core.CoreWebView2Profile_Manual) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def GetNonDefaultPermissionSettingsAsync(self: win32more.Microsoft.Web.WebView2.Core.CoreWebView2Profile_Manual2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Web.WebView2.Core.CoreWebView2PermissionSetting]]: ...
    @winrt_mixinmethod
    def GetBrowserExtensionsAsync(self: win32more.Microsoft.Web.WebView2.Core.CoreWebView2Profile_Manual3) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Web.WebView2.Core.CoreWebView2BrowserExtension]]: ...
    @ClearBrowsingDataAsync.register
    @winrt_mixinmethod
    def ClearBrowsingDataAsync(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Profile2, dataKinds: win32more.Microsoft.Web.WebView2.Core.CoreWebView2BrowsingDataKinds) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_PreferredTrackingPreventionLevel(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Profile3) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2TrackingPreventionLevel: ...
    @winrt_mixinmethod
    def put_PreferredTrackingPreventionLevel(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Profile3, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2TrackingPreventionLevel) -> Void: ...
    @winrt_mixinmethod
    def SetPermissionStateAsync(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Profile4, PermissionKind: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PermissionKind, origin: WinRT_String, State: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PermissionState) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_CookieManager(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Profile5) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2CookieManager: ...
    @winrt_mixinmethod
    def get_IsPasswordAutosaveEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Profile6) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsPasswordAutosaveEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Profile6, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsGeneralAutofillEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Profile6) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsGeneralAutofillEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Profile6, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def AddBrowserExtensionAsync(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Profile7, extensionFolderPath: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Web.WebView2.Core.CoreWebView2BrowserExtension]: ...
    @winrt_mixinmethod
    def add_Deleted(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Profile8, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Profile, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Deleted(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Profile8, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Delete(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Profile8) -> Void: ...
    @winrt_mixinmethod
    def get_ProfileName(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Profile) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsInPrivateModeEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Profile) -> Boolean: ...
    @winrt_mixinmethod
    def get_ProfilePath(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Profile) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DefaultDownloadFolderPath(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Profile) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DefaultDownloadFolderPath(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Profile, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_PreferredColorScheme(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Profile) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2PreferredColorScheme: ...
    @winrt_mixinmethod
    def put_PreferredColorScheme(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Profile, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PreferredColorScheme) -> Void: ...
    CookieManager = property(get_CookieManager, None)
    DefaultDownloadFolderPath = property(get_DefaultDownloadFolderPath, put_DefaultDownloadFolderPath)
    IsGeneralAutofillEnabled = property(get_IsGeneralAutofillEnabled, put_IsGeneralAutofillEnabled)
    IsInPrivateModeEnabled = property(get_IsInPrivateModeEnabled, None)
    IsPasswordAutosaveEnabled = property(get_IsPasswordAutosaveEnabled, put_IsPasswordAutosaveEnabled)
    PreferredColorScheme = property(get_PreferredColorScheme, put_PreferredColorScheme)
    PreferredTrackingPreventionLevel = property(get_PreferredTrackingPreventionLevel, put_PreferredTrackingPreventionLevel)
    ProfileName = property(get_ProfileName, None)
    ProfilePath = property(get_ProfilePath, None)
    Deleted = event()
class CoreWebView2Profile_Manual(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2Profile_Manual'
    _iid_ = Guid('{b42bfab4-c4bf-5469-89ac-cadc69e3b0f5}')
    @winrt_commethod(6)
    def ClearBrowsingDataAsync(self, dataKinds: win32more.Microsoft.Web.WebView2.Core.CoreWebView2BrowsingDataKinds, startTime: win32more.Windows.Foundation.DateTime, endTime: win32more.Windows.Foundation.DateTime) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(7)
    def ClearBrowsingDataAsync2(self) -> win32more.Windows.Foundation.IAsyncAction: ...
class CoreWebView2Profile_Manual2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2Profile_Manual2'
    _iid_ = Guid('{6e62815a-6269-5756-92c3-f08afe17649c}')
    @winrt_commethod(6)
    def GetNonDefaultPermissionSettingsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Web.WebView2.Core.CoreWebView2PermissionSetting]]: ...
class CoreWebView2Profile_Manual3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2Profile_Manual3'
    _iid_ = Guid('{c6129971-9ecc-5634-8896-723c1dbacd6f}')
    @winrt_commethod(6)
    def GetBrowserExtensionsAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Web.WebView2.Core.CoreWebView2BrowserExtension]]: ...
class CoreWebView2ReleaseChannels(Enum, UInt32):
    None_ = 0
    Stable = 1
    Beta = 2
    Dev = 4
    Canary = 8
class CoreWebView2SaveAsKind(Enum, Int32):
    Default = 0
    HtmlOnly = 1
    SingleFile = 2
    Complete = 3
class CoreWebView2SaveAsUIResult(Enum, Int32):
    Success = 0
    InvalidPath = 1
    FileAlreadyExists = 2
    KindNotSupported = 3
    Cancelled = 4
class CoreWebView2SaveAsUIShowingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2SaveAsUIShowingEventArgs
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2SaveAsUIShowingEventArgs'
    @winrt_mixinmethod
    def get_ContentMimeType(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2SaveAsUIShowingEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Cancel(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2SaveAsUIShowingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Cancel(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2SaveAsUIShowingEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SuppressDefaultDialog(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2SaveAsUIShowingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_SuppressDefaultDialog(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2SaveAsUIShowingEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SaveAsFilePath(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2SaveAsUIShowingEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_SaveAsFilePath(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2SaveAsUIShowingEventArgs, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AllowReplace(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2SaveAsUIShowingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowReplace(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2SaveAsUIShowingEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2SaveAsUIShowingEventArgs) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2SaveAsKind: ...
    @winrt_mixinmethod
    def put_Kind(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2SaveAsUIShowingEventArgs, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2SaveAsKind) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2SaveAsUIShowingEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    AllowReplace = property(get_AllowReplace, put_AllowReplace)
    Cancel = property(get_Cancel, put_Cancel)
    ContentMimeType = property(get_ContentMimeType, None)
    Kind = property(get_Kind, put_Kind)
    SaveAsFilePath = property(get_SaveAsFilePath, put_SaveAsFilePath)
    SuppressDefaultDialog = property(get_SuppressDefaultDialog, put_SuppressDefaultDialog)
class CoreWebView2SaveFileSecurityCheckStartingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2SaveFileSecurityCheckStartingEventArgs
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2SaveFileSecurityCheckStartingEventArgs'
    @winrt_mixinmethod
    def get_CancelSave(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2SaveFileSecurityCheckStartingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_CancelSave(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2SaveFileSecurityCheckStartingEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_DocumentOriginUri(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2SaveFileSecurityCheckStartingEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FileExtension(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2SaveFileSecurityCheckStartingEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FilePath(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2SaveFileSecurityCheckStartingEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SuppressDefaultPolicy(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2SaveFileSecurityCheckStartingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_SuppressDefaultPolicy(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2SaveFileSecurityCheckStartingEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2SaveFileSecurityCheckStartingEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    CancelSave = property(get_CancelSave, put_CancelSave)
    DocumentOriginUri = property(get_DocumentOriginUri, None)
    FileExtension = property(get_FileExtension, None)
    FilePath = property(get_FilePath, None)
    SuppressDefaultPolicy = property(get_SuppressDefaultPolicy, put_SuppressDefaultPolicy)
class CoreWebView2ScreenCaptureStartingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ScreenCaptureStartingEventArgs
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2ScreenCaptureStartingEventArgs'
    @winrt_mixinmethod
    def get_Cancel(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ScreenCaptureStartingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Cancel(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ScreenCaptureStartingEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ScreenCaptureStartingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ScreenCaptureStartingEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_OriginalSourceFrameInfo(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ScreenCaptureStartingEventArgs) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2FrameInfo: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ScreenCaptureStartingEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Cancel = property(get_Cancel, put_Cancel)
    Handled = property(get_Handled, put_Handled)
    OriginalSourceFrameInfo = property(get_OriginalSourceFrameInfo, None)
class CoreWebView2ScriptDialogKind(Enum, Int32):
    Alert = 0
    Confirm = 1
    Prompt = 2
    Beforeunload = 3
class CoreWebView2ScriptDialogOpeningEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ScriptDialogOpeningEventArgs
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2ScriptDialogOpeningEventArgs'
    @winrt_mixinmethod
    def get_Uri(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ScriptDialogOpeningEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ScriptDialogOpeningEventArgs) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ScriptDialogKind: ...
    @winrt_mixinmethod
    def get_Message(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ScriptDialogOpeningEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DefaultText(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ScriptDialogOpeningEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ResultText(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ScriptDialogOpeningEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ResultText(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ScriptDialogOpeningEventArgs, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def Accept(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ScriptDialogOpeningEventArgs) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ScriptDialogOpeningEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    DefaultText = property(get_DefaultText, None)
    Kind = property(get_Kind, None)
    Message = property(get_Message, None)
    ResultText = property(get_ResultText, put_ResultText)
    Uri = property(get_Uri, None)
class CoreWebView2ScriptException(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ScriptException
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2ScriptException'
    @winrt_mixinmethod
    def get_LineNumber(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ScriptException) -> UInt32: ...
    @winrt_mixinmethod
    def get_ColumnNumber(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ScriptException) -> UInt32: ...
    @winrt_mixinmethod
    def get_Name(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ScriptException) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Message(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ScriptException) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ToJson(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ScriptException) -> WinRT_String: ...
    ColumnNumber = property(get_ColumnNumber, None)
    LineNumber = property(get_LineNumber, None)
    Message = property(get_Message, None)
    Name = property(get_Name, None)
    ToJson = property(get_ToJson, None)
class CoreWebView2ScrollbarStyle(Enum, Int32):
    Default = 0
    FluentOverlay = 1
class CoreWebView2ServerCertificateErrorAction(Enum, Int32):
    AlwaysAllow = 0
    Cancel = 1
    Default = 2
class CoreWebView2ServerCertificateErrorDetectedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ServerCertificateErrorDetectedEventArgs
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2ServerCertificateErrorDetectedEventArgs'
    @winrt_mixinmethod
    def get_ErrorStatus(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ServerCertificateErrorDetectedEventArgs) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebErrorStatus: ...
    @winrt_mixinmethod
    def get_RequestUri(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ServerCertificateErrorDetectedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServerCertificate(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ServerCertificateErrorDetectedEventArgs) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2Certificate: ...
    @winrt_mixinmethod
    def get_Action(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ServerCertificateErrorDetectedEventArgs) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ServerCertificateErrorAction: ...
    @winrt_mixinmethod
    def put_Action(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ServerCertificateErrorDetectedEventArgs, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2ServerCertificateErrorAction) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2ServerCertificateErrorDetectedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Action = property(get_Action, put_Action)
    ErrorStatus = property(get_ErrorStatus, None)
    RequestUri = property(get_RequestUri, None)
    ServerCertificate = property(get_ServerCertificate, None)
class CoreWebView2Settings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2Settings'
    @winrt_mixinmethod
    def get_UserAgent(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings2) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_UserAgent(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings2, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_AreBrowserAcceleratorKeysEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings3) -> Boolean: ...
    @winrt_mixinmethod
    def put_AreBrowserAcceleratorKeysEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings3, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsPasswordAutosaveEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings4) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsPasswordAutosaveEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings4, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsGeneralAutofillEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings4) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsGeneralAutofillEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings4, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsPinchZoomEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings5) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsPinchZoomEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings5, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsSwipeNavigationEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings6) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsSwipeNavigationEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings6, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_HiddenPdfToolbarItems(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings7) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2PdfToolbarItems: ...
    @winrt_mixinmethod
    def put_HiddenPdfToolbarItems(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings7, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PdfToolbarItems) -> Void: ...
    @winrt_mixinmethod
    def get_IsReputationCheckingRequired(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings8) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsReputationCheckingRequired(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings8, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsNonClientRegionSupportEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings9) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsNonClientRegionSupportEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings9, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_HostObjectDispatchAdapter(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings_Manual) -> win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DispatchAdapter: ...
    @winrt_mixinmethod
    def put_HostObjectDispatchAdapter(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings_Manual, value: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DispatchAdapter) -> Void: ...
    @winrt_mixinmethod
    def get_IsScriptEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsScriptEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsWebMessageEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsWebMessageEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AreDefaultScriptDialogsEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings) -> Boolean: ...
    @winrt_mixinmethod
    def put_AreDefaultScriptDialogsEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsStatusBarEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsStatusBarEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AreDevToolsEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings) -> Boolean: ...
    @winrt_mixinmethod
    def put_AreDevToolsEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AreDefaultContextMenusEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings) -> Boolean: ...
    @winrt_mixinmethod
    def put_AreDefaultContextMenusEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AreHostObjectsAllowed(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings) -> Boolean: ...
    @winrt_mixinmethod
    def put_AreHostObjectsAllowed(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsZoomControlEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsZoomControlEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsBuiltInErrorPageEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsBuiltInErrorPageEnabled(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2Settings, value: Boolean) -> Void: ...
    AreBrowserAcceleratorKeysEnabled = property(get_AreBrowserAcceleratorKeysEnabled, put_AreBrowserAcceleratorKeysEnabled)
    AreDefaultContextMenusEnabled = property(get_AreDefaultContextMenusEnabled, put_AreDefaultContextMenusEnabled)
    AreDefaultScriptDialogsEnabled = property(get_AreDefaultScriptDialogsEnabled, put_AreDefaultScriptDialogsEnabled)
    AreDevToolsEnabled = property(get_AreDevToolsEnabled, put_AreDevToolsEnabled)
    AreHostObjectsAllowed = property(get_AreHostObjectsAllowed, put_AreHostObjectsAllowed)
    HiddenPdfToolbarItems = property(get_HiddenPdfToolbarItems, put_HiddenPdfToolbarItems)
    HostObjectDispatchAdapter = property(get_HostObjectDispatchAdapter, put_HostObjectDispatchAdapter)
    IsBuiltInErrorPageEnabled = property(get_IsBuiltInErrorPageEnabled, put_IsBuiltInErrorPageEnabled)
    IsGeneralAutofillEnabled = property(get_IsGeneralAutofillEnabled, put_IsGeneralAutofillEnabled)
    IsNonClientRegionSupportEnabled = property(get_IsNonClientRegionSupportEnabled, put_IsNonClientRegionSupportEnabled)
    IsPasswordAutosaveEnabled = property(get_IsPasswordAutosaveEnabled, put_IsPasswordAutosaveEnabled)
    IsPinchZoomEnabled = property(get_IsPinchZoomEnabled, put_IsPinchZoomEnabled)
    IsReputationCheckingRequired = property(get_IsReputationCheckingRequired, put_IsReputationCheckingRequired)
    IsScriptEnabled = property(get_IsScriptEnabled, put_IsScriptEnabled)
    IsStatusBarEnabled = property(get_IsStatusBarEnabled, put_IsStatusBarEnabled)
    IsSwipeNavigationEnabled = property(get_IsSwipeNavigationEnabled, put_IsSwipeNavigationEnabled)
    IsWebMessageEnabled = property(get_IsWebMessageEnabled, put_IsWebMessageEnabled)
    IsZoomControlEnabled = property(get_IsZoomControlEnabled, put_IsZoomControlEnabled)
    UserAgent = property(get_UserAgent, put_UserAgent)
class CoreWebView2SharedBuffer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2SharedBuffer
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2SharedBuffer'
    @winrt_mixinmethod
    def get_Buffer(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2SharedBuffer_Manual) -> win32more.Windows.Foundation.IMemoryBufferReference: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2SharedBuffer) -> UInt64: ...
    @winrt_mixinmethod
    def OpenStream(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2SharedBuffer) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    Buffer = property(get_Buffer, None)
    Size = property(get_Size, None)
class CoreWebView2SharedBufferAccess(Enum, Int32):
    ReadOnly = 0
    ReadWrite = 1
class CoreWebView2SourceChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2SourceChangedEventArgs
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2SourceChangedEventArgs'
    @winrt_mixinmethod
    def get_IsNewDocument(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2SourceChangedEventArgs) -> Boolean: ...
    IsNewDocument = property(get_IsNewDocument, None)
class CoreWebView2TextDirectionKind(Enum, Int32):
    Default = 0
    LeftToRight = 1
    RightToLeft = 2
class CoreWebView2TrackingPreventionLevel(Enum, Int32):
    None_ = 0
    Basic = 1
    Balanced = 2
    Strict = 3
class CoreWebView2WebErrorStatus(Enum, Int32):
    Unknown = 0
    CertificateCommonNameIsIncorrect = 1
    CertificateExpired = 2
    ClientCertificateContainsErrors = 3
    CertificateRevoked = 4
    CertificateIsInvalid = 5
    ServerUnreachable = 6
    Timeout = 7
    ErrorHttpInvalidServerResponse = 8
    ConnectionAborted = 9
    ConnectionReset = 10
    Disconnected = 11
    CannotConnect = 12
    HostNameNotResolved = 13
    OperationCanceled = 14
    RedirectFailed = 15
    UnexpectedError = 16
    ValidAuthenticationCredentialsRequired = 17
    ValidProxyAuthenticationRequired = 18
class CoreWebView2WebMessageReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebMessageReceivedEventArgs
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2WebMessageReceivedEventArgs'
    @winrt_mixinmethod
    def get_AdditionalObjects(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebMessageReceivedEventArgs2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    @winrt_mixinmethod
    def get_Source(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebMessageReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_WebMessageAsJson(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebMessageReceivedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def TryGetWebMessageAsString(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebMessageReceivedEventArgs) -> WinRT_String: ...
    AdditionalObjects = property(get_AdditionalObjects, None)
    Source = property(get_Source, None)
    WebMessageAsJson = property(get_WebMessageAsJson, None)
class CoreWebView2WebResourceContext(Enum, Int32):
    All = 0
    Document = 1
    Stylesheet = 2
    Image = 3
    Media = 4
    Font = 5
    Script = 6
    XmlHttpRequest = 7
    Fetch = 8
    TextTrack = 9
    EventSource = 10
    Websocket = 11
    Manifest = 12
    SignedExchange = 13
    Ping = 14
    CspViolationReport = 15
    Other = 16
class CoreWebView2WebResourceRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceRequest
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2WebResourceRequest'
    @winrt_mixinmethod
    def get_Uri(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Uri(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceRequest, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Method(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceRequest) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Method(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceRequest, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Content(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceRequest) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_mixinmethod
    def put_Content(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceRequest, value: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Void: ...
    @winrt_mixinmethod
    def get_Headers(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceRequest) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2HttpRequestHeaders: ...
    Content = property(get_Content, put_Content)
    Headers = property(get_Headers, None)
    Method = property(get_Method, put_Method)
    Uri = property(get_Uri, put_Uri)
class CoreWebView2WebResourceRequestSourceKinds(Enum, UInt32):
    None_ = 0
    Document = 1
    SharedWorker = 2
    ServiceWorker = 4
    All = 4294967295
class CoreWebView2WebResourceRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceRequestedEventArgs
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2WebResourceRequestedEventArgs'
    @winrt_mixinmethod
    def get_RequestedSourceKind(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceRequestedEventArgs2) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceRequestSourceKinds: ...
    @winrt_mixinmethod
    def get_Request(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceRequestedEventArgs) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceRequest: ...
    @winrt_mixinmethod
    def get_Response(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceRequestedEventArgs) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceResponse: ...
    @winrt_mixinmethod
    def put_Response(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceRequestedEventArgs, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceResponse) -> Void: ...
    @winrt_mixinmethod
    def get_ResourceContext(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceRequestedEventArgs) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceContext: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceRequestedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
    RequestedSourceKind = property(get_RequestedSourceKind, None)
    ResourceContext = property(get_ResourceContext, None)
    Response = property(get_Response, put_Response)
class CoreWebView2WebResourceResponse(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceResponse
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2WebResourceResponse'
    @winrt_mixinmethod
    def get_Content(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceResponse) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_mixinmethod
    def put_Content(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceResponse, value: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Void: ...
    @winrt_mixinmethod
    def get_Headers(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceResponse) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2HttpResponseHeaders: ...
    @winrt_mixinmethod
    def get_StatusCode(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceResponse) -> Int32: ...
    @winrt_mixinmethod
    def put_StatusCode(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceResponse, value: Int32) -> Void: ...
    @winrt_mixinmethod
    def get_ReasonPhrase(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceResponse) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_ReasonPhrase(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceResponse, value: WinRT_String) -> Void: ...
    Content = property(get_Content, put_Content)
    Headers = property(get_Headers, None)
    ReasonPhrase = property(get_ReasonPhrase, put_ReasonPhrase)
    StatusCode = property(get_StatusCode, put_StatusCode)
class CoreWebView2WebResourceResponseReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceResponseReceivedEventArgs
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2WebResourceResponseReceivedEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceResponseReceivedEventArgs) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceRequest: ...
    @winrt_mixinmethod
    def get_Response(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceResponseReceivedEventArgs) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceResponseView: ...
    Request = property(get_Request, None)
    Response = property(get_Response, None)
class CoreWebView2WebResourceResponseView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceResponseView
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2WebResourceResponseView'
    @winrt_mixinmethod
    def get_Headers(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceResponseView) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2HttpResponseHeaders: ...
    @winrt_mixinmethod
    def get_StatusCode(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceResponseView) -> Int32: ...
    @winrt_mixinmethod
    def get_ReasonPhrase(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceResponseView) -> WinRT_String: ...
    @winrt_mixinmethod
    def GetContentAsync(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceResponseView) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    Headers = property(get_Headers, None)
    ReasonPhrase = property(get_ReasonPhrase, None)
    StatusCode = property(get_StatusCode, None)
class CoreWebView2WindowFeatures(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WindowFeatures
    _classid_ = 'Microsoft.Web.WebView2.Core.CoreWebView2WindowFeatures'
    @winrt_mixinmethod
    def get_HasPosition(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WindowFeatures) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasSize(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WindowFeatures) -> Boolean: ...
    @winrt_mixinmethod
    def get_Left(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WindowFeatures) -> UInt32: ...
    @winrt_mixinmethod
    def get_Top(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WindowFeatures) -> UInt32: ...
    @winrt_mixinmethod
    def get_Height(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WindowFeatures) -> UInt32: ...
    @winrt_mixinmethod
    def get_Width(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WindowFeatures) -> UInt32: ...
    @winrt_mixinmethod
    def get_ShouldDisplayMenuBar(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WindowFeatures) -> Boolean: ...
    @winrt_mixinmethod
    def get_ShouldDisplayStatus(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WindowFeatures) -> Boolean: ...
    @winrt_mixinmethod
    def get_ShouldDisplayToolbar(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WindowFeatures) -> Boolean: ...
    @winrt_mixinmethod
    def get_ShouldDisplayScrollBars(self: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2WindowFeatures) -> Boolean: ...
    HasPosition = property(get_HasPosition, None)
    HasSize = property(get_HasSize, None)
    Height = property(get_Height, None)
    Left = property(get_Left, None)
    ShouldDisplayMenuBar = property(get_ShouldDisplayMenuBar, None)
    ShouldDisplayScrollBars = property(get_ShouldDisplayScrollBars, None)
    ShouldDisplayStatus = property(get_ShouldDisplayStatus, None)
    ShouldDisplayToolbar = property(get_ShouldDisplayToolbar, None)
    Top = property(get_Top, None)
    Width = property(get_Width, None)
class ICoreWebView2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2'
    _iid_ = Guid('{3a3f559a-e5e9-5338-bb67-4eb0504a4f14}')
    @winrt_commethod(6)
    def get_Settings(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2Settings: ...
    @winrt_commethod(7)
    def get_Source(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_BrowserProcessId(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_CanGoBack(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_CanGoForward(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_DocumentTitle(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_ContainsFullScreenElement(self) -> Boolean: ...
    @winrt_commethod(13)
    def add_NavigationStarting(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2NavigationStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_NavigationStarting(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def add_ContentLoading(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2ContentLoadingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_ContentLoading(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_SourceChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2SourceChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_SourceChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(19)
    def add_HistoryChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_HistoryChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(21)
    def add_NavigationCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2NavigationCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(22)
    def remove_NavigationCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(23)
    def add_FrameNavigationStarting(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2NavigationStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(24)
    def remove_FrameNavigationStarting(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(25)
    def add_FrameNavigationCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2NavigationCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(26)
    def remove_FrameNavigationCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(27)
    def add_ScriptDialogOpening(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2ScriptDialogOpeningEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(28)
    def remove_ScriptDialogOpening(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(29)
    def add_PermissionRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2PermissionRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(30)
    def remove_PermissionRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(31)
    def add_ProcessFailed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2ProcessFailedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(32)
    def remove_ProcessFailed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(33)
    def add_WebMessageReceived(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebMessageReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(34)
    def remove_WebMessageReceived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(35)
    def add_NewWindowRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2NewWindowRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(36)
    def remove_NewWindowRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(37)
    def add_DocumentTitleChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(38)
    def remove_DocumentTitleChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(39)
    def add_ContainsFullScreenElementChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(40)
    def remove_ContainsFullScreenElementChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(41)
    def add_WebResourceRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(42)
    def remove_WebResourceRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(43)
    def add_WindowCloseRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(44)
    def remove_WindowCloseRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(45)
    def Navigate(self, uri: WinRT_String) -> Void: ...
    @winrt_commethod(46)
    def NavigateToString(self, htmlContent: WinRT_String) -> Void: ...
    @winrt_commethod(47)
    def AddScriptToExecuteOnDocumentCreatedAsync(self, javaScript: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(48)
    def RemoveScriptToExecuteOnDocumentCreated(self, id: WinRT_String) -> Void: ...
    @winrt_commethod(49)
    def ExecuteScriptAsync(self, javaScript: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(50)
    def CapturePreviewAsync(self, imageFormat: win32more.Microsoft.Web.WebView2.Core.CoreWebView2CapturePreviewImageFormat, imageStream: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(51)
    def Reload(self) -> Void: ...
    @winrt_commethod(52)
    def PostWebMessageAsJson(self, webMessageAsJson: WinRT_String) -> Void: ...
    @winrt_commethod(53)
    def PostWebMessageAsString(self, webMessageAsString: WinRT_String) -> Void: ...
    @winrt_commethod(54)
    def CallDevToolsProtocolMethodAsync(self, methodName: WinRT_String, parametersAsJson: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(55)
    def GoBack(self) -> Void: ...
    @winrt_commethod(56)
    def GoForward(self) -> Void: ...
    @winrt_commethod(57)
    def GetDevToolsProtocolEventReceiver(self, eventName: WinRT_String) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2DevToolsProtocolEventReceiver: ...
    @winrt_commethod(58)
    def Stop(self) -> Void: ...
    @winrt_commethod(59)
    def AddHostObjectToScript(self, name: WinRT_String, rawObject: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(60)
    def RemoveHostObjectFromScript(self, name: WinRT_String) -> Void: ...
    @winrt_commethod(61)
    def OpenDevToolsWindow(self) -> Void: ...
    @winrt_commethod(62)
    def AddWebResourceRequestedFilter(self, uri: WinRT_String, ResourceContext: win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceContext) -> Void: ...
    @winrt_commethod(63)
    def RemoveWebResourceRequestedFilter(self, uri: WinRT_String, ResourceContext: win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceContext) -> Void: ...
    BrowserProcessId = property(get_BrowserProcessId, None)
    CanGoBack = property(get_CanGoBack, None)
    CanGoForward = property(get_CanGoForward, None)
    ContainsFullScreenElement = property(get_ContainsFullScreenElement, None)
    DocumentTitle = property(get_DocumentTitle, None)
    Settings = property(get_Settings, None)
    Source = property(get_Source, None)
    NavigationStarting = event()
    ContentLoading = event()
    SourceChanged = event()
    HistoryChanged = event()
    NavigationCompleted = event()
    FrameNavigationStarting = event()
    FrameNavigationCompleted = event()
    ScriptDialogOpening = event()
    PermissionRequested = event()
    ProcessFailed = event()
    WebMessageReceived = event()
    NewWindowRequested = event()
    DocumentTitleChanged = event()
    ContainsFullScreenElementChanged = event()
    WebResourceRequested = event()
    WindowCloseRequested = event()
class ICoreWebView2AcceleratorKeyPressedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2AcceleratorKeyPressedEventArgs'
    _iid_ = Guid('{41a56100-92a5-59d1-9e71-9222e33ae38b}')
    @winrt_commethod(6)
    def get_KeyEventKind(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2KeyEventKind: ...
    @winrt_commethod(7)
    def get_VirtualKey(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_KeyEventLParam(self) -> Int32: ...
    @winrt_commethod(9)
    def get_PhysicalKeyStatus(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2PhysicalKeyStatus: ...
    @winrt_commethod(10)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_Handled(self, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
    KeyEventKind = property(get_KeyEventKind, None)
    KeyEventLParam = property(get_KeyEventLParam, None)
    PhysicalKeyStatus = property(get_PhysicalKeyStatus, None)
    VirtualKey = property(get_VirtualKey, None)
class ICoreWebView2AcceleratorKeyPressedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2AcceleratorKeyPressedEventArgs2'
    _iid_ = Guid('{4d03aa18-806d-5f10-9ad8-cf5d327a58fb}')
    @winrt_commethod(6)
    def get_IsBrowserAcceleratorKeyEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsBrowserAcceleratorKeyEnabled(self, value: Boolean) -> Void: ...
    IsBrowserAcceleratorKeyEnabled = property(get_IsBrowserAcceleratorKeyEnabled, put_IsBrowserAcceleratorKeyEnabled)
class ICoreWebView2BasicAuthenticationRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2BasicAuthenticationRequestedEventArgs'
    _iid_ = Guid('{4b16330c-4ca5-555e-af21-164334405f63}')
    @winrt_commethod(6)
    def get_Uri(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Challenge(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Response(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2BasicAuthenticationResponse: ...
    @winrt_commethod(9)
    def get_Cancel(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_Cancel(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Cancel = property(get_Cancel, put_Cancel)
    Challenge = property(get_Challenge, None)
    Response = property(get_Response, None)
    Uri = property(get_Uri, None)
class ICoreWebView2BasicAuthenticationResponse(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2BasicAuthenticationResponse'
    _iid_ = Guid('{08df33b9-6e38-5962-9ffd-caab3c30fbc1}')
    @winrt_commethod(6)
    def get_UserName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_UserName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Password(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Password(self, value: WinRT_String) -> Void: ...
    Password = property(get_Password, put_Password)
    UserName = property(get_UserName, put_UserName)
class ICoreWebView2BrowserExtension(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2BrowserExtension'
    _iid_ = Guid('{bf991443-ee4f-57b8-bf2c-81cd6dbe1153}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(9)
    def RemoveAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(10)
    def EnableAsync(self, IsEnabled: Boolean) -> win32more.Windows.Foundation.IAsyncAction: ...
    Id = property(get_Id, None)
    IsEnabled = property(get_IsEnabled, None)
    Name = property(get_Name, None)
class ICoreWebView2BrowserProcessExitedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2BrowserProcessExitedEventArgs'
    _iid_ = Guid('{79963f77-1484-5a46-b91f-dfc5c1a0ce14}')
    @winrt_commethod(6)
    def get_BrowserProcessExitKind(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2BrowserProcessExitKind: ...
    @winrt_commethod(7)
    def get_BrowserProcessId(self) -> UInt32: ...
    BrowserProcessExitKind = property(get_BrowserProcessExitKind, None)
    BrowserProcessId = property(get_BrowserProcessId, None)
class ICoreWebView2Certificate(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Certificate'
    _iid_ = Guid('{414a3b75-1bc1-55e1-9926-268c0a3462c7}')
    @winrt_commethod(6)
    def get_Subject(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Issuer(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ValidFrom(self) -> Double: ...
    @winrt_commethod(9)
    def get_ValidTo(self) -> Double: ...
    @winrt_commethod(10)
    def get_DerEncodedSerialNumber(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_PemEncodedIssuerCertificateChain(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(13)
    def ToPemEncoding(self) -> WinRT_String: ...
    DerEncodedSerialNumber = property(get_DerEncodedSerialNumber, None)
    DisplayName = property(get_DisplayName, None)
    Issuer = property(get_Issuer, None)
    PemEncodedIssuerCertificateChain = property(get_PemEncodedIssuerCertificateChain, None)
    Subject = property(get_Subject, None)
    ValidFrom = property(get_ValidFrom, None)
    ValidTo = property(get_ValidTo, None)
class ICoreWebView2ClientCertificate(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2ClientCertificate'
    _iid_ = Guid('{091b39f2-68df-52b4-8fb0-fd3561af41f2}')
    @winrt_commethod(6)
    def get_Subject(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Issuer(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ValidFrom(self) -> Double: ...
    @winrt_commethod(9)
    def get_ValidTo(self) -> Double: ...
    @winrt_commethod(10)
    def get_DerEncodedSerialNumber(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_PemEncodedIssuerCertificateChain(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(13)
    def get_Kind(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ClientCertificateKind: ...
    @winrt_commethod(14)
    def ToPemEncoding(self) -> WinRT_String: ...
    DerEncodedSerialNumber = property(get_DerEncodedSerialNumber, None)
    DisplayName = property(get_DisplayName, None)
    Issuer = property(get_Issuer, None)
    Kind = property(get_Kind, None)
    PemEncodedIssuerCertificateChain = property(get_PemEncodedIssuerCertificateChain, None)
    Subject = property(get_Subject, None)
    ValidFrom = property(get_ValidFrom, None)
    ValidTo = property(get_ValidTo, None)
class ICoreWebView2ClientCertificateRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2ClientCertificateRequestedEventArgs'
    _iid_ = Guid('{93287b55-31f9-55a0-b68b-d9841d7e1bf4}')
    @winrt_commethod(6)
    def get_Host(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Port(self) -> Int32: ...
    @winrt_commethod(8)
    def get_IsProxy(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_AllowedCertificateAuthorities(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(10)
    def get_MutuallyTrustedCertificates(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Web.WebView2.Core.CoreWebView2ClientCertificate]: ...
    @winrt_commethod(11)
    def get_SelectedCertificate(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ClientCertificate: ...
    @winrt_commethod(12)
    def put_SelectedCertificate(self, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2ClientCertificate) -> Void: ...
    @winrt_commethod(13)
    def get_Cancel(self) -> Boolean: ...
    @winrt_commethod(14)
    def put_Cancel(self, value: Boolean) -> Void: ...
    @winrt_commethod(15)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(16)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(17)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    AllowedCertificateAuthorities = property(get_AllowedCertificateAuthorities, None)
    Cancel = property(get_Cancel, put_Cancel)
    Handled = property(get_Handled, put_Handled)
    Host = property(get_Host, None)
    IsProxy = property(get_IsProxy, None)
    MutuallyTrustedCertificates = property(get_MutuallyTrustedCertificates, None)
    Port = property(get_Port, None)
    SelectedCertificate = property(get_SelectedCertificate, put_SelectedCertificate)
class ICoreWebView2CompositionController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2CompositionController'
    _iid_ = Guid('{31bbb153-11b2-58e8-9beb-69f5c8e14420}')
    @winrt_commethod(6)
    def get_RootVisualTarget(self) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def put_RootVisualTarget(self, value: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
    @winrt_commethod(8)
    def add_CursorChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2CompositionController, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_CursorChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def SendMouseInput(self, eventKind: win32more.Microsoft.Web.WebView2.Core.CoreWebView2MouseEventKind, virtualKeys: win32more.Microsoft.Web.WebView2.Core.CoreWebView2MouseEventVirtualKeys, mouseData: UInt32, point: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(11)
    def SendPointerInput(self, eventKind: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PointerEventKind, pointerInfo: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PointerInfo) -> Void: ...
    @winrt_commethod(12)
    def get_Cursor(self) -> win32more.Windows.UI.Core.CoreCursor: ...
    @winrt_commethod(13)
    def DragEnter(self, dragInfo: win32more.Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDragInfo, dragUIOverride: win32more.Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDragUIOverride) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    @winrt_commethod(14)
    def DragOver(self, dragInfo: win32more.Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDragInfo, dragUIOverride: win32more.Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDragUIOverride) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    @winrt_commethod(15)
    def Drop(self, dragInfo: win32more.Windows.ApplicationModel.DataTransfer.DragDrop.Core.CoreDragInfo) -> win32more.Windows.ApplicationModel.DataTransfer.DataPackageOperation: ...
    Cursor = property(get_Cursor, None)
    RootVisualTarget = property(get_RootVisualTarget, put_RootVisualTarget)
    CursorChanged = event()
class ICoreWebView2CompositionController2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2CompositionController2'
    _iid_ = Guid('{8cef61b9-fa55-547d-aae6-7bcaed4249a2}')
class ICoreWebView2CompositionController3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2CompositionController3'
    _iid_ = Guid('{bbbecdcf-0f03-50f0-8f85-9cbf6c9bbe10}')
    @winrt_commethod(6)
    def DragLeave(self) -> Void: ...
class ICoreWebView2CompositionController4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2CompositionController4'
    _iid_ = Guid('{c950cb84-2648-5ad5-badd-bfe659682fb6}')
    @winrt_commethod(6)
    def add_NonClientRegionChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2CompositionController, win32more.Microsoft.Web.WebView2.Core.CoreWebView2NonClientRegionChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_NonClientRegionChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def GetNonClientRegionAtPoint(self, point: win32more.Windows.Foundation.Point) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2NonClientRegionKind: ...
    @winrt_commethod(9)
    def QueryNonClientRegion(self, Kind: win32more.Microsoft.Web.WebView2.Core.CoreWebView2NonClientRegionKind) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Rect]: ...
    NonClientRegionChanged = event()
class ICoreWebView2CompositionControllerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2CompositionControllerStatics'
    _iid_ = Guid('{4df0ab1f-7f2a-573b-b81a-b9b531224736}')
class ICoreWebView2CompositionControllerStatics2_Manual(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2CompositionControllerStatics2_Manual'
    _iid_ = Guid('{48a321e7-4f40-526e-837e-1eb0c477b69d}')
class ICoreWebView2ContentLoadingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2ContentLoadingEventArgs'
    _iid_ = Guid('{6cf95373-946c-5dae-9b3e-0fe23d5aa29f}')
    @winrt_commethod(6)
    def get_IsErrorPage(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_NavigationId(self) -> UInt64: ...
    IsErrorPage = property(get_IsErrorPage, None)
    NavigationId = property(get_NavigationId, None)
class ICoreWebView2ContextMenuItem(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuItem'
    _iid_ = Guid('{2a65706f-941a-52cd-8651-a165586b0abf}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Label(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_CommandId(self) -> Int32: ...
    @winrt_commethod(9)
    def get_ShortcutKeyDescription(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Icon(self) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_commethod(11)
    def get_Kind(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ContextMenuItemKind: ...
    @winrt_commethod(12)
    def get_IsEnabled(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_IsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_IsChecked(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_IsChecked(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def get_Children(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.Web.WebView2.Core.CoreWebView2ContextMenuItem]: ...
    @winrt_commethod(17)
    def add_CustomItemSelected(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2ContextMenuItem, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_CustomItemSelected(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Children = property(get_Children, None)
    CommandId = property(get_CommandId, None)
    Icon = property(get_Icon, None)
    IsChecked = property(get_IsChecked, put_IsChecked)
    IsEnabled = property(get_IsEnabled, put_IsEnabled)
    Kind = property(get_Kind, None)
    Label = property(get_Label, None)
    Name = property(get_Name, None)
    ShortcutKeyDescription = property(get_ShortcutKeyDescription, None)
    CustomItemSelected = event()
class ICoreWebView2ContextMenuRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuRequestedEventArgs'
    _iid_ = Guid('{d77bdd8c-9b3e-596e-ae80-320c0df4ecbc}')
    @winrt_commethod(6)
    def get_MenuItems(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.Web.WebView2.Core.CoreWebView2ContextMenuItem]: ...
    @winrt_commethod(7)
    def get_ContextMenuTarget(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ContextMenuTarget: ...
    @winrt_commethod(8)
    def get_Location(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(9)
    def get_SelectedCommandId(self) -> Int32: ...
    @winrt_commethod(10)
    def put_SelectedCommandId(self, value: Int32) -> Void: ...
    @winrt_commethod(11)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(13)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    ContextMenuTarget = property(get_ContextMenuTarget, None)
    Handled = property(get_Handled, put_Handled)
    Location = property(get_Location, None)
    MenuItems = property(get_MenuItems, None)
    SelectedCommandId = property(get_SelectedCommandId, put_SelectedCommandId)
class ICoreWebView2ContextMenuTarget(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2ContextMenuTarget'
    _iid_ = Guid('{41e24e6a-4612-5bd9-8e61-e9280615205e}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ContextMenuTargetKind: ...
    @winrt_commethod(7)
    def get_IsEditable(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsRequestedForMainFrame(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_PageUri(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_FrameUri(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_HasLinkUri(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_LinkUri(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_HasLinkText(self) -> Boolean: ...
    @winrt_commethod(14)
    def get_LinkText(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def get_HasSourceUri(self) -> Boolean: ...
    @winrt_commethod(16)
    def get_SourceUri(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def get_HasSelection(self) -> Boolean: ...
    @winrt_commethod(18)
    def get_SelectionText(self) -> WinRT_String: ...
    FrameUri = property(get_FrameUri, None)
    HasLinkText = property(get_HasLinkText, None)
    HasLinkUri = property(get_HasLinkUri, None)
    HasSelection = property(get_HasSelection, None)
    HasSourceUri = property(get_HasSourceUri, None)
    IsEditable = property(get_IsEditable, None)
    IsRequestedForMainFrame = property(get_IsRequestedForMainFrame, None)
    Kind = property(get_Kind, None)
    LinkText = property(get_LinkText, None)
    LinkUri = property(get_LinkUri, None)
    PageUri = property(get_PageUri, None)
    SelectionText = property(get_SelectionText, None)
    SourceUri = property(get_SourceUri, None)
class ICoreWebView2Controller(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Controller'
    _iid_ = Guid('{a588121c-53bf-590e-80e5-29d729cbd743}')
    @winrt_commethod(6)
    def get_IsVisible(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsVisible(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_Bounds(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(9)
    def put_Bounds(self, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(10)
    def get_ZoomFactor(self) -> Double: ...
    @winrt_commethod(11)
    def put_ZoomFactor(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def get_ParentWindow(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ControllerWindowReference: ...
    @winrt_commethod(13)
    def put_ParentWindow(self, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2ControllerWindowReference) -> Void: ...
    @winrt_commethod(14)
    def get_CoreWebView2(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2: ...
    @winrt_commethod(15)
    def add_ZoomFactorChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Controller, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_ZoomFactorChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_MoveFocusRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Controller, win32more.Microsoft.Web.WebView2.Core.CoreWebView2MoveFocusRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_MoveFocusRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(19)
    def add_GotFocus(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Controller, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_GotFocus(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(21)
    def add_LostFocus(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Controller, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(22)
    def remove_LostFocus(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(23)
    def add_AcceleratorKeyPressed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Controller, win32more.Microsoft.Web.WebView2.Core.CoreWebView2AcceleratorKeyPressedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(24)
    def remove_AcceleratorKeyPressed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(25)
    def SetBoundsAndZoomFactor(self, Bounds: win32more.Windows.Foundation.Rect, ZoomFactor: Double) -> Void: ...
    @winrt_commethod(26)
    def MoveFocus(self, reason: win32more.Microsoft.Web.WebView2.Core.CoreWebView2MoveFocusReason) -> Void: ...
    @winrt_commethod(27)
    def NotifyParentWindowPositionChanged(self) -> Void: ...
    @winrt_commethod(28)
    def Close(self) -> Void: ...
    Bounds = property(get_Bounds, put_Bounds)
    CoreWebView2 = property(get_CoreWebView2, None)
    IsVisible = property(get_IsVisible, put_IsVisible)
    ParentWindow = property(get_ParentWindow, put_ParentWindow)
    ZoomFactor = property(get_ZoomFactor, put_ZoomFactor)
    ZoomFactorChanged = event()
    MoveFocusRequested = event()
    GotFocus = event()
    LostFocus = event()
    AcceleratorKeyPressed = event()
class ICoreWebView2Controller2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Controller2'
    _iid_ = Guid('{0069c40b-2e8a-513f-9d9d-e0c2b64f7200}')
    @winrt_commethod(6)
    def get_DefaultBackgroundColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_DefaultBackgroundColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    DefaultBackgroundColor = property(get_DefaultBackgroundColor, put_DefaultBackgroundColor)
class ICoreWebView2Controller3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Controller3'
    _iid_ = Guid('{e5bae214-791a-5d13-9b76-a257d9fda2ac}')
    @winrt_commethod(6)
    def get_RasterizationScale(self) -> Double: ...
    @winrt_commethod(7)
    def put_RasterizationScale(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_ShouldDetectMonitorScaleChanges(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_ShouldDetectMonitorScaleChanges(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_BoundsMode(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2BoundsMode: ...
    @winrt_commethod(11)
    def put_BoundsMode(self, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2BoundsMode) -> Void: ...
    @winrt_commethod(12)
    def add_RasterizationScaleChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Controller, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_RasterizationScaleChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    BoundsMode = property(get_BoundsMode, put_BoundsMode)
    RasterizationScale = property(get_RasterizationScale, put_RasterizationScale)
    ShouldDetectMonitorScaleChanges = property(get_ShouldDetectMonitorScaleChanges, put_ShouldDetectMonitorScaleChanges)
    RasterizationScaleChanged = event()
class ICoreWebView2Controller4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Controller4'
    _iid_ = Guid('{94e2862d-4638-54ba-92cf-e31a31499b78}')
    @winrt_commethod(6)
    def get_AllowExternalDrop(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AllowExternalDrop(self, value: Boolean) -> Void: ...
    AllowExternalDrop = property(get_AllowExternalDrop, put_AllowExternalDrop)
class ICoreWebView2ControllerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2ControllerFactory'
    _iid_ = Guid('{270b2c5b-c3a9-53d8-a5ca-262ea9ea62e8}')
class ICoreWebView2ControllerOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2ControllerOptions'
    _iid_ = Guid('{3337e821-3606-5a0e-8e2f-0c1e57d743f7}')
    @winrt_commethod(6)
    def get_ProfileName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_ProfileName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_IsInPrivateModeEnabled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IsInPrivateModeEnabled(self, value: Boolean) -> Void: ...
    IsInPrivateModeEnabled = property(get_IsInPrivateModeEnabled, put_IsInPrivateModeEnabled)
    ProfileName = property(get_ProfileName, put_ProfileName)
class ICoreWebView2ControllerOptions2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2ControllerOptions2'
    _iid_ = Guid('{41b69e93-cc17-5c7d-a0c8-fa21c27aadb6}')
    @winrt_commethod(6)
    def get_ScriptLocale(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_ScriptLocale(self, value: WinRT_String) -> Void: ...
    ScriptLocale = property(get_ScriptLocale, put_ScriptLocale)
class ICoreWebView2ControllerWindowReference(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2ControllerWindowReference'
    _iid_ = Guid('{0feddad4-48a3-5cc4-9f61-e7adfd1e9c76}')
    @winrt_commethod(6)
    def get_WindowHandle(self) -> UInt64: ...
    @winrt_commethod(7)
    def get_CoreWindow(self) -> win32more.Windows.UI.Core.CoreWindow: ...
    CoreWindow = property(get_CoreWindow, None)
    WindowHandle = property(get_WindowHandle, None)
class ICoreWebView2ControllerWindowReferenceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2ControllerWindowReferenceStatics'
    _iid_ = Guid('{ddf6ebf1-ebc6-5a34-9008-661c3a2eb767}')
    @winrt_commethod(6)
    def CreateFromWindowHandle(self, windowHandle: UInt64) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ControllerWindowReference: ...
    @winrt_commethod(7)
    def CreateFromCoreWindow(self, coreWindow: win32more.Windows.UI.Core.CoreWindow) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ControllerWindowReference: ...
class ICoreWebView2Cookie(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Cookie'
    _iid_ = Guid('{52f670fe-8ca2-5aad-aedb-25f7903b7038}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Value(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_Value(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_Domain(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Path(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_Expires(self) -> Double: ...
    @winrt_commethod(12)
    def put_Expires(self, value: Double) -> Void: ...
    @winrt_commethod(13)
    def get_IsHttpOnly(self) -> Boolean: ...
    @winrt_commethod(14)
    def put_IsHttpOnly(self, value: Boolean) -> Void: ...
    @winrt_commethod(15)
    def get_SameSite(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2CookieSameSiteKind: ...
    @winrt_commethod(16)
    def put_SameSite(self, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2CookieSameSiteKind) -> Void: ...
    @winrt_commethod(17)
    def get_IsSecure(self) -> Boolean: ...
    @winrt_commethod(18)
    def put_IsSecure(self, value: Boolean) -> Void: ...
    @winrt_commethod(19)
    def get_IsSession(self) -> Boolean: ...
    Domain = property(get_Domain, None)
    Expires = property(get_Expires, put_Expires)
    IsHttpOnly = property(get_IsHttpOnly, put_IsHttpOnly)
    IsSecure = property(get_IsSecure, put_IsSecure)
    IsSession = property(get_IsSession, None)
    Name = property(get_Name, None)
    Path = property(get_Path, None)
    SameSite = property(get_SameSite, put_SameSite)
    Value = property(get_Value, put_Value)
class ICoreWebView2CookieManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2CookieManager'
    _iid_ = Guid('{4098f516-adca-5563-aaa5-d7affd847aa3}')
    @winrt_commethod(6)
    def CreateCookie(self, name: WinRT_String, value: WinRT_String, Domain: WinRT_String, Path: WinRT_String) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2Cookie: ...
    @winrt_commethod(7)
    def CopyCookie(self, cookieParam: win32more.Microsoft.Web.WebView2.Core.CoreWebView2Cookie) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2Cookie: ...
    @winrt_commethod(8)
    def AddOrUpdateCookie(self, cookie: win32more.Microsoft.Web.WebView2.Core.CoreWebView2Cookie) -> Void: ...
    @winrt_commethod(9)
    def DeleteCookie(self, cookie: win32more.Microsoft.Web.WebView2.Core.CoreWebView2Cookie) -> Void: ...
    @winrt_commethod(10)
    def DeleteCookies(self, name: WinRT_String, uri: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def DeleteCookiesWithDomainAndPath(self, name: WinRT_String, Domain: WinRT_String, Path: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def DeleteAllCookies(self) -> Void: ...
class ICoreWebView2CookieManager_Manual(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2CookieManager_Manual'
    _iid_ = Guid('{9bcca0ea-7225-577a-bb23-c7c98023154e}')
    @winrt_commethod(6)
    def GetCookiesAsync(self, uri: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Cookie]]: ...
class ICoreWebView2CustomSchemeRegistration(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2CustomSchemeRegistration'
    _iid_ = Guid('{16dc60d9-ddec-5c3d-bc1f-4408d1875af1}')
    @winrt_commethod(6)
    def get_TreatAsSecure(self) -> Int32: ...
    @winrt_commethod(7)
    def put_TreatAsSecure(self, value: Int32) -> Void: ...
    @winrt_commethod(8)
    def get_HasAuthorityComponent(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_HasAuthorityComponent(self, value: Boolean) -> Void: ...
    HasAuthorityComponent = property(get_HasAuthorityComponent, put_HasAuthorityComponent)
    TreatAsSecure = property(get_TreatAsSecure, put_TreatAsSecure)
class ICoreWebView2CustomSchemeRegistrationFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2CustomSchemeRegistrationFactory'
    _iid_ = Guid('{309dddfa-ff3e-5d8d-a18a-c1341f325ea7}')
    @winrt_commethod(6)
    def CreateInstance(self, schemeName: WinRT_String) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2CustomSchemeRegistration: ...
class ICoreWebView2CustomSchemeRegistration_Manual(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2CustomSchemeRegistration_Manual'
    _iid_ = Guid('{074ff15c-7d7f-5101-a02e-c077c5e21c41}')
    @winrt_commethod(6)
    def get_SchemeName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_AllowedOrigins(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    AllowedOrigins = property(get_AllowedOrigins, None)
    SchemeName = property(get_SchemeName, None)
class ICoreWebView2DOMContentLoadedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2DOMContentLoadedEventArgs'
    _iid_ = Guid('{c474d0a3-24ac-59fc-b78b-da7562a6a052}')
    @winrt_commethod(6)
    def get_NavigationId(self) -> UInt64: ...
    NavigationId = property(get_NavigationId, None)
class ICoreWebView2DevToolsProtocolEventReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2DevToolsProtocolEventReceivedEventArgs'
    _iid_ = Guid('{b6a4b41d-fd18-59fa-923a-c57555d960ce}')
    @winrt_commethod(6)
    def get_ParameterObjectAsJson(self) -> WinRT_String: ...
    ParameterObjectAsJson = property(get_ParameterObjectAsJson, None)
class ICoreWebView2DevToolsProtocolEventReceivedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2DevToolsProtocolEventReceivedEventArgs2'
    _iid_ = Guid('{221728ba-635e-50d2-bd3c-fd22f4113978}')
    @winrt_commethod(6)
    def get_SessionId(self) -> WinRT_String: ...
    SessionId = property(get_SessionId, None)
class ICoreWebView2DevToolsProtocolEventReceiver(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2DevToolsProtocolEventReceiver'
    _iid_ = Guid('{b2a2be79-65fc-5537-8715-3d92bf31090b}')
    @winrt_commethod(6)
    def add_DevToolsProtocolEventReceived(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2DevToolsProtocolEventReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_DevToolsProtocolEventReceived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    DevToolsProtocolEventReceived = event()
class ICoreWebView2DispatchAdapter(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2DispatchAdapter'
    _iid_ = Guid('{7888a42d-18f3-5966-80cb-8cc25351bd0a}')
    @winrt_commethod(6)
    def WrapNamedObject(self, name: WinRT_String, adapter: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DispatchAdapter) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(7)
    def WrapObject(self, unwrapped: win32more.Windows.Win32.System.WinRT.IInspectable, adapter: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DispatchAdapter) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(8)
    def UnwrapObject(self, wrapped: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_commethod(9)
    def Clean(self) -> Void: ...
class ICoreWebView2DownloadOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2DownloadOperation'
    _iid_ = Guid('{afe73e6b-e760-5a06-9bf6-1e743c13cd2d}')
    @winrt_commethod(6)
    def get_Uri(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ContentDisposition(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_MimeType(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_TotalBytesToReceive(self) -> Int64: ...
    @winrt_commethod(10)
    def get_BytesReceived(self) -> Int64: ...
    @winrt_commethod(11)
    def get_EstimatedEndTime(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_ResultFilePath(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_State(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2DownloadState: ...
    @winrt_commethod(14)
    def get_InterruptReason(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2DownloadInterruptReason: ...
    @winrt_commethod(15)
    def get_CanResume(self) -> Boolean: ...
    @winrt_commethod(16)
    def add_BytesReceivedChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2DownloadOperation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_BytesReceivedChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_EstimatedEndTimeChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2DownloadOperation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_EstimatedEndTimeChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(20)
    def add_StateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2DownloadOperation, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_StateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(22)
    def Cancel(self) -> Void: ...
    @winrt_commethod(23)
    def Pause(self) -> Void: ...
    @winrt_commethod(24)
    def Resume(self) -> Void: ...
    BytesReceived = property(get_BytesReceived, None)
    CanResume = property(get_CanResume, None)
    ContentDisposition = property(get_ContentDisposition, None)
    EstimatedEndTime = property(get_EstimatedEndTime, None)
    InterruptReason = property(get_InterruptReason, None)
    MimeType = property(get_MimeType, None)
    ResultFilePath = property(get_ResultFilePath, None)
    State = property(get_State, None)
    TotalBytesToReceive = property(get_TotalBytesToReceive, None)
    Uri = property(get_Uri, None)
    BytesReceivedChanged = event()
    EstimatedEndTimeChanged = event()
    StateChanged = event()
class ICoreWebView2DownloadStartingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2DownloadStartingEventArgs'
    _iid_ = Guid('{45d982ba-9256-5b35-b023-26a438599110}')
    @winrt_commethod(6)
    def get_DownloadOperation(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2DownloadOperation: ...
    @winrt_commethod(7)
    def get_Cancel(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Cancel(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_ResultFilePath(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def put_ResultFilePath(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(13)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Cancel = property(get_Cancel, put_Cancel)
    DownloadOperation = property(get_DownloadOperation, None)
    Handled = property(get_Handled, put_Handled)
    ResultFilePath = property(get_ResultFilePath, put_ResultFilePath)
class ICoreWebView2Environment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Environment'
    _iid_ = Guid('{d8cc7831-b783-556b-b9ce-899c1e95d585}')
    @winrt_commethod(6)
    def get_BrowserVersionString(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def add_NewBrowserVersionAvailable(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Environment, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_NewBrowserVersionAvailable(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def CreateCoreWebView2ControllerAsync(self, ParentWindow: win32more.Microsoft.Web.WebView2.Core.CoreWebView2ControllerWindowReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Controller]: ...
    @winrt_commethod(10)
    def CreateWebResourceResponse(self, Content: win32more.Windows.Storage.Streams.IRandomAccessStream, StatusCode: Int32, ReasonPhrase: WinRT_String, Headers: WinRT_String) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceResponse: ...
    BrowserVersionString = property(get_BrowserVersionString, None)
    NewBrowserVersionAvailable = event()
class ICoreWebView2Environment10(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Environment10'
    _iid_ = Guid('{c224e69c-1efd-5ecc-adc8-2b52e7b97ce5}')
    @winrt_commethod(6)
    def CreateCoreWebView2ControllerOptions(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ControllerOptions: ...
class ICoreWebView2Environment11(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Environment11'
    _iid_ = Guid('{da23d64c-8b61-5b6c-8581-f6a688abd7cd}')
    @winrt_commethod(6)
    def get_FailureReportFolderPath(self) -> WinRT_String: ...
    FailureReportFolderPath = property(get_FailureReportFolderPath, None)
class ICoreWebView2Environment12(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Environment12'
    _iid_ = Guid('{82531ddb-be63-5254-812f-880d9f0ec54e}')
    @winrt_commethod(6)
    def CreateSharedBuffer(self, Size: UInt64) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2SharedBuffer: ...
class ICoreWebView2Environment13(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Environment13'
    _iid_ = Guid('{22c97f2f-8a28-5794-941c-a25bcc3cf47e}')
    @winrt_commethod(6)
    def GetProcessExtendedInfosAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Web.WebView2.Core.CoreWebView2ProcessExtendedInfo]]: ...
class ICoreWebView2Environment14(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Environment14'
    _iid_ = Guid('{39f9505f-0d1f-5284-9fa9-9dbd818973fa}')
    @winrt_commethod(6)
    def CreateWebFileSystemFileHandle(self, Path: WinRT_String, Permission: win32more.Microsoft.Web.WebView2.Core.CoreWebView2FileSystemHandlePermission) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2FileSystemHandle: ...
    @winrt_commethod(7)
    def CreateWebFileSystemDirectoryHandle(self, Path: WinRT_String, Permission: win32more.Microsoft.Web.WebView2.Core.CoreWebView2FileSystemHandlePermission) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2FileSystemHandle: ...
class ICoreWebView2Environment2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Environment2'
    _iid_ = Guid('{0b634668-1017-5fc7-9921-f1f51866a8c0}')
    @winrt_commethod(6)
    def CreateWebResourceRequest(self, uri: WinRT_String, Method: WinRT_String, postData: win32more.Windows.Storage.Streams.IRandomAccessStream, Headers: WinRT_String) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceRequest: ...
class ICoreWebView2Environment3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Environment3'
    _iid_ = Guid('{5e33f46c-c0b9-5126-8840-17f9c11b3a8a}')
    @winrt_commethod(6)
    def CreateCoreWebView2CompositionControllerAsync(self, ParentWindow: win32more.Microsoft.Web.WebView2.Core.CoreWebView2ControllerWindowReference) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Web.WebView2.Core.CoreWebView2CompositionController]: ...
    @winrt_commethod(7)
    def CreateCoreWebView2PointerInfo(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2PointerInfo: ...
class ICoreWebView2Environment4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Environment4'
    _iid_ = Guid('{6db697da-eebd-5818-8790-1fe57ef319e2}')
class ICoreWebView2Environment5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Environment5'
    _iid_ = Guid('{f33399af-e4d3-59dc-ac38-8397aadcedb1}')
    @winrt_commethod(6)
    def add_BrowserProcessExited(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Environment, win32more.Microsoft.Web.WebView2.Core.CoreWebView2BrowserProcessExitedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_BrowserProcessExited(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    BrowserProcessExited = event()
class ICoreWebView2Environment6(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Environment6'
    _iid_ = Guid('{965d538f-5958-5d98-8972-f622021df402}')
    @winrt_commethod(6)
    def CreatePrintSettings(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintSettings: ...
class ICoreWebView2Environment7(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Environment7'
    _iid_ = Guid('{e1f44fe2-fc54-5383-a383-c87e1da96b83}')
    @winrt_commethod(6)
    def get_UserDataFolder(self) -> WinRT_String: ...
    UserDataFolder = property(get_UserDataFolder, None)
class ICoreWebView2Environment8(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Environment8'
    _iid_ = Guid('{db67c807-d0db-5980-a3a9-75ef8f63d6f6}')
    @winrt_commethod(6)
    def add_ProcessInfosChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Environment, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ProcessInfosChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def GetProcessInfos(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Web.WebView2.Core.CoreWebView2ProcessInfo]: ...
    ProcessInfosChanged = event()
class ICoreWebView2Environment9(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Environment9'
    _iid_ = Guid('{c8213ec7-7dc9-5468-a88b-15c6b7144478}')
    @winrt_commethod(6)
    def CreateContextMenuItem(self, Label: WinRT_String, iconStream: win32more.Windows.Storage.Streams.IRandomAccessStream, Kind: win32more.Microsoft.Web.WebView2.Core.CoreWebView2ContextMenuItemKind) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ContextMenuItem: ...
class ICoreWebView2EnvironmentOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions'
    _iid_ = Guid('{25d6dc39-0062-5735-8b09-a6f535f19e97}')
    @winrt_commethod(6)
    def get_AdditionalBrowserArguments(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_AdditionalBrowserArguments(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Language(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Language(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_TargetCompatibleBrowserVersion(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_TargetCompatibleBrowserVersion(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def get_AllowSingleSignOnUsingOSPrimaryAccount(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_AllowSingleSignOnUsingOSPrimaryAccount(self, value: Boolean) -> Void: ...
    AdditionalBrowserArguments = property(get_AdditionalBrowserArguments, put_AdditionalBrowserArguments)
    AllowSingleSignOnUsingOSPrimaryAccount = property(get_AllowSingleSignOnUsingOSPrimaryAccount, put_AllowSingleSignOnUsingOSPrimaryAccount)
    Language = property(get_Language, put_Language)
    TargetCompatibleBrowserVersion = property(get_TargetCompatibleBrowserVersion, put_TargetCompatibleBrowserVersion)
class ICoreWebView2EnvironmentOptions2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions2'
    _iid_ = Guid('{e77350fb-77a1-56f7-be95-eb7f8a7a3072}')
    @winrt_commethod(6)
    def get_ExclusiveUserDataFolderAccess(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_ExclusiveUserDataFolderAccess(self, value: Boolean) -> Void: ...
    ExclusiveUserDataFolderAccess = property(get_ExclusiveUserDataFolderAccess, put_ExclusiveUserDataFolderAccess)
class ICoreWebView2EnvironmentOptions3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions3'
    _iid_ = Guid('{48ab919d-2444-5e8c-a6f6-aba840d6c5ff}')
    @winrt_commethod(6)
    def get_IsCustomCrashReportingEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsCustomCrashReportingEnabled(self, value: Boolean) -> Void: ...
    IsCustomCrashReportingEnabled = property(get_IsCustomCrashReportingEnabled, put_IsCustomCrashReportingEnabled)
class ICoreWebView2EnvironmentOptions4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions4'
    _iid_ = Guid('{a2cb850f-cd14-5a7d-9c98-53fd51ec9858}')
class ICoreWebView2EnvironmentOptions5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions5'
    _iid_ = Guid('{36b1ca6c-e06c-5050-8ef9-247c5a7aa9c9}')
    @winrt_commethod(6)
    def get_EnableTrackingPrevention(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_EnableTrackingPrevention(self, value: Boolean) -> Void: ...
    EnableTrackingPrevention = property(get_EnableTrackingPrevention, put_EnableTrackingPrevention)
class ICoreWebView2EnvironmentOptions6(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions6'
    _iid_ = Guid('{eb5b14c2-6f05-514e-b19a-76744d1ce684}')
    @winrt_commethod(6)
    def get_AreBrowserExtensionsEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AreBrowserExtensionsEnabled(self, value: Boolean) -> Void: ...
    AreBrowserExtensionsEnabled = property(get_AreBrowserExtensionsEnabled, put_AreBrowserExtensionsEnabled)
class ICoreWebView2EnvironmentOptions7(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions7'
    _iid_ = Guid('{7447b9ed-a60d-5af8-ab2a-56c544bc356a}')
    @winrt_commethod(6)
    def get_ChannelSearchKind(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ChannelSearchKind: ...
    @winrt_commethod(7)
    def put_ChannelSearchKind(self, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2ChannelSearchKind) -> Void: ...
    @winrt_commethod(8)
    def get_ReleaseChannels(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ReleaseChannels: ...
    @winrt_commethod(9)
    def put_ReleaseChannels(self, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2ReleaseChannels) -> Void: ...
    ChannelSearchKind = property(get_ChannelSearchKind, put_ChannelSearchKind)
    ReleaseChannels = property(get_ReleaseChannels, put_ReleaseChannels)
class ICoreWebView2EnvironmentOptions8(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions8'
    _iid_ = Guid('{f143e9d2-2669-5b6a-8f88-7b05c9e1ef4d}')
    @winrt_commethod(6)
    def get_ScrollBarStyle(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ScrollbarStyle: ...
    @winrt_commethod(7)
    def put_ScrollBarStyle(self, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2ScrollbarStyle) -> Void: ...
    ScrollBarStyle = property(get_ScrollBarStyle, put_ScrollBarStyle)
class ICoreWebView2EnvironmentOptions_Manual(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions_Manual'
    _iid_ = Guid('{1f104443-ea93-5a37-b791-34e6a31172ed}')
class ICoreWebView2EnvironmentOptions_Manual3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentOptions_Manual3'
    _iid_ = Guid('{665e9c11-ca1b-5255-a6f5-d741ac39e18f}')
    @winrt_commethod(6)
    def get_CustomSchemeRegistrations(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.Web.WebView2.Core.CoreWebView2CustomSchemeRegistration]: ...
    @winrt_commethod(7)
    def put_CustomSchemeRegistrations(self, value: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.Web.WebView2.Core.CoreWebView2CustomSchemeRegistration]) -> Void: ...
    CustomSchemeRegistrations = property(get_CustomSchemeRegistrations, put_CustomSchemeRegistrations)
class ICoreWebView2EnvironmentStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentStatics'
    _iid_ = Guid('{0e33f804-f20b-5635-8491-162aaa27517b}')
    @winrt_commethod(6)
    def CreateAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Environment]: ...
    @winrt_commethod(7)
    def CreateWithOptionsAsync(self, browserExecutableFolder: WinRT_String, userDataFolder: WinRT_String, options: win32more.Microsoft.Web.WebView2.Core.CoreWebView2EnvironmentOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Environment]: ...
    @winrt_commethod(8)
    def GetAvailableBrowserVersionString(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def GetAvailableBrowserVersionString2(self, browserExecutableFolder: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(10)
    def CompareBrowserVersionString(self, browserVersionString1: WinRT_String, browserVersionString2: WinRT_String) -> Int32: ...
class ICoreWebView2EnvironmentStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2EnvironmentStatics2'
    _iid_ = Guid('{dcba13e4-ee49-5860-8499-c49161a7d8ce}')
    @winrt_commethod(6)
    def GetAvailableBrowserVersionStringWithOptions(self, browserExecutableFolder: WinRT_String, options: win32more.Microsoft.Web.WebView2.Core.CoreWebView2EnvironmentOptions) -> WinRT_String: ...
class ICoreWebView2Environment_Manual(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Environment_Manual'
    _iid_ = Guid('{f51cfabe-73ad-5635-a935-6386aef9238e}')
    @winrt_commethod(6)
    def CreateCoreWebView2ControllerAsync(self, ParentWindow: win32more.Microsoft.Web.WebView2.Core.CoreWebView2ControllerWindowReference, options: win32more.Microsoft.Web.WebView2.Core.CoreWebView2ControllerOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Controller]: ...
    @winrt_commethod(7)
    def CreateCoreWebView2CompositionControllerAsync(self, ParentWindow: win32more.Microsoft.Web.WebView2.Core.CoreWebView2ControllerWindowReference, options: win32more.Microsoft.Web.WebView2.Core.CoreWebView2ControllerOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Web.WebView2.Core.CoreWebView2CompositionController]: ...
class ICoreWebView2ExecuteScriptResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2ExecuteScriptResult'
    _iid_ = Guid('{9bef80f9-580c-56a0-8db9-75ec792c8421}')
    @winrt_commethod(6)
    def get_Succeeded(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_ResultAsJson(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Exception(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ScriptException: ...
    Exception = property(get_Exception, None)
    ResultAsJson = property(get_ResultAsJson, None)
    Succeeded = property(get_Succeeded, None)
class ICoreWebView2ExecuteScriptResult_Manual(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2ExecuteScriptResult_Manual'
    _iid_ = Guid('{5931bc73-376c-5ba7-bcbb-3caec6d1ff5b}')
    @winrt_commethod(6)
    def TryGetResultAsString(self, stringResult: POINTER(WinRT_String)) -> Int32: ...
class ICoreWebView2File(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2File'
    _iid_ = Guid('{cab45512-9594-50f1-ac3c-9cc103b574a3}')
    @winrt_commethod(6)
    def get_Path(self) -> WinRT_String: ...
    Path = property(get_Path, None)
class ICoreWebView2FileSystemHandle(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2FileSystemHandle'
    _iid_ = Guid('{241cb4c8-0021-5f72-8bf2-e141dce4c151}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2FileSystemHandleKind: ...
    @winrt_commethod(7)
    def get_Path(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Permission(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2FileSystemHandlePermission: ...
    Kind = property(get_Kind, None)
    Path = property(get_Path, None)
    Permission = property(get_Permission, None)
class ICoreWebView2Frame(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Frame'
    _iid_ = Guid('{02ffcbf9-19e7-5bb8-8273-346420fb1503}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def add_NameChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Frame, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_NameChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_Destroyed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Frame, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Destroyed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def RemoveHostObjectFromScript(self, name: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def IsDestroyed(self) -> Int32: ...
    Name = property(get_Name, None)
    NameChanged = event()
    Destroyed = event()
class ICoreWebView2Frame2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Frame2'
    _iid_ = Guid('{33dbc9c9-a103-56e3-b722-363814200320}')
    @winrt_commethod(6)
    def add_NavigationStarting(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Frame, win32more.Microsoft.Web.WebView2.Core.CoreWebView2NavigationStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_NavigationStarting(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_ContentLoading(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Frame, win32more.Microsoft.Web.WebView2.Core.CoreWebView2ContentLoadingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ContentLoading(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_NavigationCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Frame, win32more.Microsoft.Web.WebView2.Core.CoreWebView2NavigationCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_NavigationCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_DOMContentLoaded(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Frame, win32more.Microsoft.Web.WebView2.Core.CoreWebView2DOMContentLoadedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_DOMContentLoaded(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_WebMessageReceived(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Frame, win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebMessageReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_WebMessageReceived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def ExecuteScriptAsync(self, javaScript: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_commethod(17)
    def PostWebMessageAsJson(self, webMessageAsJson: WinRT_String) -> Void: ...
    @winrt_commethod(18)
    def PostWebMessageAsString(self, webMessageAsString: WinRT_String) -> Void: ...
    NavigationStarting = event()
    ContentLoading = event()
    NavigationCompleted = event()
    DOMContentLoaded = event()
    WebMessageReceived = event()
class ICoreWebView2Frame3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Frame3'
    _iid_ = Guid('{6545dac4-1666-50a5-bbe8-ec04842a466f}')
    @winrt_commethod(6)
    def add_PermissionRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Frame, win32more.Microsoft.Web.WebView2.Core.CoreWebView2PermissionRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_PermissionRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    PermissionRequested = event()
class ICoreWebView2Frame4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Frame4'
    _iid_ = Guid('{d46cd758-64b9-543e-a7b8-cac9b4c059a7}')
    @winrt_commethod(6)
    def PostSharedBufferToScript(self, sharedBuffer: win32more.Microsoft.Web.WebView2.Core.CoreWebView2SharedBuffer, access: win32more.Microsoft.Web.WebView2.Core.CoreWebView2SharedBufferAccess, additionalDataAsJson: WinRT_String) -> Void: ...
class ICoreWebView2Frame5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Frame5'
    _iid_ = Guid('{27c4803d-9a7f-599a-bf72-07e8dc964a5b}')
    @winrt_commethod(6)
    def get_FrameId(self) -> UInt32: ...
    FrameId = property(get_FrameId, None)
class ICoreWebView2Frame6(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Frame6'
    _iid_ = Guid('{ba197dad-d2f4-5127-80b8-faab02ec211e}')
    @winrt_commethod(6)
    def add_ScreenCaptureStarting(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Frame, win32more.Microsoft.Web.WebView2.Core.CoreWebView2ScreenCaptureStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ScreenCaptureStarting(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ScreenCaptureStarting = event()
class ICoreWebView2FrameCreatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2FrameCreatedEventArgs'
    _iid_ = Guid('{527b01b8-fc6d-5543-8dce-96cdfdb32c81}')
    @winrt_commethod(6)
    def get_Frame(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2Frame: ...
    Frame = property(get_Frame, None)
class ICoreWebView2FrameInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2FrameInfo'
    _iid_ = Guid('{f9b82e06-73f3-513b-bc2c-445ddedba976}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Source(self) -> WinRT_String: ...
    Name = property(get_Name, None)
    Source = property(get_Source, None)
class ICoreWebView2FrameInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2FrameInfo2'
    _iid_ = Guid('{7f0770c6-0d5e-529b-b00c-f15656f605c4}')
    @winrt_commethod(6)
    def get_ParentFrameInfo(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2FrameInfo: ...
    @winrt_commethod(7)
    def get_FrameId(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_FrameKind(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2FrameKind: ...
    FrameId = property(get_FrameId, None)
    FrameKind = property(get_FrameKind, None)
    ParentFrameInfo = property(get_ParentFrameInfo, None)
class ICoreWebView2HttpHeadersCollectionIterator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2HttpHeadersCollectionIterator'
    _iid_ = Guid('{adf264ee-d980-5f48-a60e-8705de046608}')
class ICoreWebView2HttpRequestHeaders(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2HttpRequestHeaders'
    _iid_ = Guid('{dc2226c7-3515-55bb-bcb2-57b78f86b91d}')
    @winrt_commethod(6)
    def GetHeader(self, name: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(7)
    def GetHeaders(self, name: WinRT_String) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2HttpHeadersCollectionIterator: ...
    @winrt_commethod(8)
    def Contains(self, name: WinRT_String) -> Boolean: ...
    @winrt_commethod(9)
    def SetHeader(self, name: WinRT_String, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def RemoveHeader(self, name: WinRT_String) -> Void: ...
class ICoreWebView2HttpResponseHeaders(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2HttpResponseHeaders'
    _iid_ = Guid('{f3d383e9-747f-5574-8662-9a6b920cecd4}')
    @winrt_commethod(6)
    def AppendHeader(self, name: WinRT_String, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def Contains(self, name: WinRT_String) -> Boolean: ...
    @winrt_commethod(8)
    def GetHeader(self, name: WinRT_String) -> WinRT_String: ...
    @winrt_commethod(9)
    def GetHeaders(self, name: WinRT_String) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2HttpHeadersCollectionIterator: ...
class ICoreWebView2LaunchingExternalUriSchemeEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2LaunchingExternalUriSchemeEventArgs'
    _iid_ = Guid('{6ab44f8d-ec6a-56a1-ae3c-9c55dff6cbc6}')
    @winrt_commethod(6)
    def get_Uri(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_InitiatingOrigin(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_IsUserInitiated(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Cancel(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_Cancel(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Cancel = property(get_Cancel, put_Cancel)
    InitiatingOrigin = property(get_InitiatingOrigin, None)
    IsUserInitiated = property(get_IsUserInitiated, None)
    Uri = property(get_Uri, None)
class ICoreWebView2MoveFocusRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2MoveFocusRequestedEventArgs'
    _iid_ = Guid('{2e29103b-ecdd-5c1d-b288-3f066d608919}')
    @winrt_commethod(6)
    def get_Reason(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2MoveFocusReason: ...
    @winrt_commethod(7)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Handled(self, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
    Reason = property(get_Reason, None)
class ICoreWebView2NavigationCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2NavigationCompletedEventArgs'
    _iid_ = Guid('{4865e238-036a-5664-95a3-447ec44cf498}')
    @winrt_commethod(6)
    def get_IsSuccess(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_WebErrorStatus(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebErrorStatus: ...
    @winrt_commethod(8)
    def get_NavigationId(self) -> UInt64: ...
    IsSuccess = property(get_IsSuccess, None)
    NavigationId = property(get_NavigationId, None)
    WebErrorStatus = property(get_WebErrorStatus, None)
class ICoreWebView2NavigationCompletedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2NavigationCompletedEventArgs2'
    _iid_ = Guid('{6e4d3c33-a6e2-5896-90c5-68b4b5e55b40}')
    @winrt_commethod(6)
    def get_HttpStatusCode(self) -> Int32: ...
    HttpStatusCode = property(get_HttpStatusCode, None)
class ICoreWebView2NavigationStartingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2NavigationStartingEventArgs'
    _iid_ = Guid('{548d23d3-fea3-5616-bd05-ae08066c86d3}')
    @winrt_commethod(6)
    def get_Uri(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_IsUserInitiated(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsRedirected(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_RequestHeaders(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2HttpRequestHeaders: ...
    @winrt_commethod(10)
    def get_Cancel(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_Cancel(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_NavigationId(self) -> UInt64: ...
    Cancel = property(get_Cancel, put_Cancel)
    IsRedirected = property(get_IsRedirected, None)
    IsUserInitiated = property(get_IsUserInitiated, None)
    NavigationId = property(get_NavigationId, None)
    RequestHeaders = property(get_RequestHeaders, None)
    Uri = property(get_Uri, None)
class ICoreWebView2NavigationStartingEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2NavigationStartingEventArgs2'
    _iid_ = Guid('{d7a3824e-7654-5c4b-b069-e6501634d84c}')
    @winrt_commethod(6)
    def get_AdditionalAllowedFrameAncestors(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_AdditionalAllowedFrameAncestors(self, value: WinRT_String) -> Void: ...
    AdditionalAllowedFrameAncestors = property(get_AdditionalAllowedFrameAncestors, put_AdditionalAllowedFrameAncestors)
class ICoreWebView2NavigationStartingEventArgs3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2NavigationStartingEventArgs3'
    _iid_ = Guid('{17db72f6-e995-59f6-91ba-4411e755f3ab}')
    @winrt_commethod(6)
    def get_NavigationKind(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2NavigationKind: ...
    NavigationKind = property(get_NavigationKind, None)
class ICoreWebView2NewWindowRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2NewWindowRequestedEventArgs'
    _iid_ = Guid('{e6e013ba-aec8-532e-9ac9-1590af7b25ec}')
    @winrt_commethod(6)
    def get_Uri(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_NewWindow(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2: ...
    @winrt_commethod(8)
    def put_NewWindow(self, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2) -> Void: ...
    @winrt_commethod(9)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_IsUserInitiated(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_WindowFeatures(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2WindowFeatures: ...
    @winrt_commethod(13)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Handled = property(get_Handled, put_Handled)
    IsUserInitiated = property(get_IsUserInitiated, None)
    NewWindow = property(get_NewWindow, put_NewWindow)
    Uri = property(get_Uri, None)
    WindowFeatures = property(get_WindowFeatures, None)
class ICoreWebView2NewWindowRequestedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2NewWindowRequestedEventArgs2'
    _iid_ = Guid('{f4806259-e63a-5c0b-a02c-5f10e11094f4}')
    @winrt_commethod(6)
    def get_Name(self) -> WinRT_String: ...
    Name = property(get_Name, None)
class ICoreWebView2NewWindowRequestedEventArgs3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2NewWindowRequestedEventArgs3'
    _iid_ = Guid('{1f0f7826-8d70-5720-bb8b-d87f63cbfb9c}')
    @winrt_commethod(6)
    def get_OriginalSourceFrameInfo(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2FrameInfo: ...
    OriginalSourceFrameInfo = property(get_OriginalSourceFrameInfo, None)
class ICoreWebView2NonClientRegionChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2NonClientRegionChangedEventArgs'
    _iid_ = Guid('{4f583622-cd0f-55d6-be7e-8a8f99a20e62}')
    @winrt_commethod(6)
    def get_RegionKind(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2NonClientRegionKind: ...
    RegionKind = property(get_RegionKind, None)
class ICoreWebView2Notification(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Notification'
    _iid_ = Guid('{2516351d-6ccd-5484-bff3-75f4dd4749e5}')
    @winrt_commethod(6)
    def get_Body(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Direction(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2TextDirectionKind: ...
    @winrt_commethod(8)
    def get_Language(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Tag(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_IconUri(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_BadgeUri(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_BodyImageUri(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_ShouldRenotify(self) -> Boolean: ...
    @winrt_commethod(15)
    def get_RequiresInteraction(self) -> Boolean: ...
    @winrt_commethod(16)
    def get_IsSilent(self) -> Boolean: ...
    @winrt_commethod(17)
    def get_Timestamp(self) -> Double: ...
    @winrt_commethod(18)
    def add_CloseRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Notification, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_CloseRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(20)
    def ReportShown(self) -> Void: ...
    @winrt_commethod(21)
    def ReportClicked(self) -> Void: ...
    @winrt_commethod(22)
    def ReportClosed(self) -> Void: ...
    BadgeUri = property(get_BadgeUri, None)
    Body = property(get_Body, None)
    BodyImageUri = property(get_BodyImageUri, None)
    Direction = property(get_Direction, None)
    IconUri = property(get_IconUri, None)
    IsSilent = property(get_IsSilent, None)
    Language = property(get_Language, None)
    RequiresInteraction = property(get_RequiresInteraction, None)
    ShouldRenotify = property(get_ShouldRenotify, None)
    Tag = property(get_Tag, None)
    Timestamp = property(get_Timestamp, None)
    Title = property(get_Title, None)
    CloseRequested = event()
class ICoreWebView2NotificationReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2NotificationReceivedEventArgs'
    _iid_ = Guid('{9416a036-5e06-57cb-8bbb-7f6ea1dc9a3d}')
    @winrt_commethod(6)
    def get_SenderOrigin(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Notification(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2Notification: ...
    @winrt_commethod(8)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Handled = property(get_Handled, put_Handled)
    Notification = property(get_Notification, None)
    SenderOrigin = property(get_SenderOrigin, None)
class ICoreWebView2Notification_Manual2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Notification_Manual2'
    _iid_ = Guid('{a2c84873-f40e-5ade-a7db-e478233c5897}')
    @winrt_commethod(6)
    def get_VibrationPattern(self) -> win32more.Windows.Foundation.Collections.IVectorView[UInt64]: ...
    VibrationPattern = property(get_VibrationPattern, None)
class ICoreWebView2PermissionRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2PermissionRequestedEventArgs'
    _iid_ = Guid('{118bdd9b-cef1-5910-929e-c1a321328239}')
    @winrt_commethod(6)
    def get_Uri(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_PermissionKind(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2PermissionKind: ...
    @winrt_commethod(8)
    def get_IsUserInitiated(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_State(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2PermissionState: ...
    @winrt_commethod(10)
    def put_State(self, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PermissionState) -> Void: ...
    @winrt_commethod(11)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    IsUserInitiated = property(get_IsUserInitiated, None)
    PermissionKind = property(get_PermissionKind, None)
    State = property(get_State, put_State)
    Uri = property(get_Uri, None)
class ICoreWebView2PermissionRequestedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2PermissionRequestedEventArgs2'
    _iid_ = Guid('{a6652fba-ebe5-5891-addc-cb37da8f7e66}')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
class ICoreWebView2PermissionRequestedEventArgs3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2PermissionRequestedEventArgs3'
    _iid_ = Guid('{200e8bcc-bc11-5beb-aa7a-79d4c95d73aa}')
    @winrt_commethod(6)
    def get_SavesInProfile(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_SavesInProfile(self, value: Boolean) -> Void: ...
    SavesInProfile = property(get_SavesInProfile, put_SavesInProfile)
class ICoreWebView2PermissionSetting(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2PermissionSetting'
    _iid_ = Guid('{b4158d0b-8ef8-575f-8e99-5fe02e8b579e}')
    @winrt_commethod(6)
    def get_PermissionKind(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2PermissionKind: ...
    @winrt_commethod(7)
    def get_PermissionOrigin(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_PermissionState(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2PermissionState: ...
    PermissionKind = property(get_PermissionKind, None)
    PermissionOrigin = property(get_PermissionOrigin, None)
    PermissionState = property(get_PermissionState, None)
class ICoreWebView2PointerInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2PointerInfo'
    _iid_ = Guid('{c3860e0d-c018-5a84-bc06-9f8f7b275dff}')
    @winrt_commethod(6)
    def get_PointerKind(self) -> UInt32: ...
    @winrt_commethod(7)
    def put_PointerKind(self, value: UInt32) -> Void: ...
    @winrt_commethod(8)
    def get_PointerId(self) -> UInt32: ...
    @winrt_commethod(9)
    def put_PointerId(self, value: UInt32) -> Void: ...
    @winrt_commethod(10)
    def get_FrameId(self) -> UInt32: ...
    @winrt_commethod(11)
    def put_FrameId(self, value: UInt32) -> Void: ...
    @winrt_commethod(12)
    def get_PointerFlags(self) -> UInt32: ...
    @winrt_commethod(13)
    def put_PointerFlags(self, value: UInt32) -> Void: ...
    @winrt_commethod(14)
    def get_PointerDeviceRect(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(15)
    def put_PointerDeviceRect(self, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(16)
    def get_DisplayRect(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(17)
    def put_DisplayRect(self, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(18)
    def get_PixelLocation(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(19)
    def put_PixelLocation(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(20)
    def get_HimetricLocation(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(21)
    def put_HimetricLocation(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(22)
    def get_PixelLocationRaw(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(23)
    def put_PixelLocationRaw(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(24)
    def get_HimetricLocationRaw(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(25)
    def put_HimetricLocationRaw(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(26)
    def get_Time(self) -> UInt32: ...
    @winrt_commethod(27)
    def put_Time(self, value: UInt32) -> Void: ...
    @winrt_commethod(28)
    def get_HistoryCount(self) -> UInt32: ...
    @winrt_commethod(29)
    def put_HistoryCount(self, value: UInt32) -> Void: ...
    @winrt_commethod(30)
    def get_InputData(self) -> Int32: ...
    @winrt_commethod(31)
    def put_InputData(self, value: Int32) -> Void: ...
    @winrt_commethod(32)
    def get_KeyStates(self) -> UInt32: ...
    @winrt_commethod(33)
    def put_KeyStates(self, value: UInt32) -> Void: ...
    @winrt_commethod(34)
    def get_PerformanceCount(self) -> UInt64: ...
    @winrt_commethod(35)
    def put_PerformanceCount(self, value: UInt64) -> Void: ...
    @winrt_commethod(36)
    def get_ButtonChangeKind(self) -> Int32: ...
    @winrt_commethod(37)
    def put_ButtonChangeKind(self, value: Int32) -> Void: ...
    @winrt_commethod(38)
    def get_PenFlags(self) -> UInt32: ...
    @winrt_commethod(39)
    def put_PenFlags(self, value: UInt32) -> Void: ...
    @winrt_commethod(40)
    def get_PenMask(self) -> UInt32: ...
    @winrt_commethod(41)
    def put_PenMask(self, value: UInt32) -> Void: ...
    @winrt_commethod(42)
    def get_PenPressure(self) -> UInt32: ...
    @winrt_commethod(43)
    def put_PenPressure(self, value: UInt32) -> Void: ...
    @winrt_commethod(44)
    def get_PenRotation(self) -> UInt32: ...
    @winrt_commethod(45)
    def put_PenRotation(self, value: UInt32) -> Void: ...
    @winrt_commethod(46)
    def get_PenTiltX(self) -> Int32: ...
    @winrt_commethod(47)
    def put_PenTiltX(self, value: Int32) -> Void: ...
    @winrt_commethod(48)
    def get_PenTiltY(self) -> Int32: ...
    @winrt_commethod(49)
    def put_PenTiltY(self, value: Int32) -> Void: ...
    @winrt_commethod(50)
    def get_TouchFlags(self) -> UInt32: ...
    @winrt_commethod(51)
    def put_TouchFlags(self, value: UInt32) -> Void: ...
    @winrt_commethod(52)
    def get_TouchMask(self) -> UInt32: ...
    @winrt_commethod(53)
    def put_TouchMask(self, value: UInt32) -> Void: ...
    @winrt_commethod(54)
    def get_TouchContact(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(55)
    def put_TouchContact(self, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(56)
    def get_TouchContactRaw(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(57)
    def put_TouchContactRaw(self, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(58)
    def get_TouchOrientation(self) -> UInt32: ...
    @winrt_commethod(59)
    def put_TouchOrientation(self, value: UInt32) -> Void: ...
    @winrt_commethod(60)
    def get_TouchPressure(self) -> UInt32: ...
    @winrt_commethod(61)
    def put_TouchPressure(self, value: UInt32) -> Void: ...
    ButtonChangeKind = property(get_ButtonChangeKind, put_ButtonChangeKind)
    DisplayRect = property(get_DisplayRect, put_DisplayRect)
    FrameId = property(get_FrameId, put_FrameId)
    HimetricLocation = property(get_HimetricLocation, put_HimetricLocation)
    HimetricLocationRaw = property(get_HimetricLocationRaw, put_HimetricLocationRaw)
    HistoryCount = property(get_HistoryCount, put_HistoryCount)
    InputData = property(get_InputData, put_InputData)
    KeyStates = property(get_KeyStates, put_KeyStates)
    PenFlags = property(get_PenFlags, put_PenFlags)
    PenMask = property(get_PenMask, put_PenMask)
    PenPressure = property(get_PenPressure, put_PenPressure)
    PenRotation = property(get_PenRotation, put_PenRotation)
    PenTiltX = property(get_PenTiltX, put_PenTiltX)
    PenTiltY = property(get_PenTiltY, put_PenTiltY)
    PerformanceCount = property(get_PerformanceCount, put_PerformanceCount)
    PixelLocation = property(get_PixelLocation, put_PixelLocation)
    PixelLocationRaw = property(get_PixelLocationRaw, put_PixelLocationRaw)
    PointerDeviceRect = property(get_PointerDeviceRect, put_PointerDeviceRect)
    PointerFlags = property(get_PointerFlags, put_PointerFlags)
    PointerId = property(get_PointerId, put_PointerId)
    PointerKind = property(get_PointerKind, put_PointerKind)
    Time = property(get_Time, put_Time)
    TouchContact = property(get_TouchContact, put_TouchContact)
    TouchContactRaw = property(get_TouchContactRaw, put_TouchContactRaw)
    TouchFlags = property(get_TouchFlags, put_TouchFlags)
    TouchMask = property(get_TouchMask, put_TouchMask)
    TouchOrientation = property(get_TouchOrientation, put_TouchOrientation)
    TouchPressure = property(get_TouchPressure, put_TouchPressure)
class ICoreWebView2PrintSettings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings'
    _iid_ = Guid('{9c75c8c0-ef3d-58a8-9a8c-18eed9fd0f16}')
    @winrt_commethod(6)
    def get_Orientation(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintOrientation: ...
    @winrt_commethod(7)
    def put_Orientation(self, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintOrientation) -> Void: ...
    @winrt_commethod(8)
    def get_ScaleFactor(self) -> Double: ...
    @winrt_commethod(9)
    def put_ScaleFactor(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_PageWidth(self) -> Double: ...
    @winrt_commethod(11)
    def put_PageWidth(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def get_PageHeight(self) -> Double: ...
    @winrt_commethod(13)
    def put_PageHeight(self, value: Double) -> Void: ...
    @winrt_commethod(14)
    def get_MarginTop(self) -> Double: ...
    @winrt_commethod(15)
    def put_MarginTop(self, value: Double) -> Void: ...
    @winrt_commethod(16)
    def get_MarginBottom(self) -> Double: ...
    @winrt_commethod(17)
    def put_MarginBottom(self, value: Double) -> Void: ...
    @winrt_commethod(18)
    def get_MarginLeft(self) -> Double: ...
    @winrt_commethod(19)
    def put_MarginLeft(self, value: Double) -> Void: ...
    @winrt_commethod(20)
    def get_MarginRight(self) -> Double: ...
    @winrt_commethod(21)
    def put_MarginRight(self, value: Double) -> Void: ...
    @winrt_commethod(22)
    def get_ShouldPrintBackgrounds(self) -> Boolean: ...
    @winrt_commethod(23)
    def put_ShouldPrintBackgrounds(self, value: Boolean) -> Void: ...
    @winrt_commethod(24)
    def get_ShouldPrintSelectionOnly(self) -> Boolean: ...
    @winrt_commethod(25)
    def put_ShouldPrintSelectionOnly(self, value: Boolean) -> Void: ...
    @winrt_commethod(26)
    def get_ShouldPrintHeaderAndFooter(self) -> Boolean: ...
    @winrt_commethod(27)
    def put_ShouldPrintHeaderAndFooter(self, value: Boolean) -> Void: ...
    @winrt_commethod(28)
    def get_HeaderTitle(self) -> WinRT_String: ...
    @winrt_commethod(29)
    def put_HeaderTitle(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(30)
    def get_FooterUri(self) -> WinRT_String: ...
    @winrt_commethod(31)
    def put_FooterUri(self, value: WinRT_String) -> Void: ...
    FooterUri = property(get_FooterUri, put_FooterUri)
    HeaderTitle = property(get_HeaderTitle, put_HeaderTitle)
    MarginBottom = property(get_MarginBottom, put_MarginBottom)
    MarginLeft = property(get_MarginLeft, put_MarginLeft)
    MarginRight = property(get_MarginRight, put_MarginRight)
    MarginTop = property(get_MarginTop, put_MarginTop)
    Orientation = property(get_Orientation, put_Orientation)
    PageHeight = property(get_PageHeight, put_PageHeight)
    PageWidth = property(get_PageWidth, put_PageWidth)
    ScaleFactor = property(get_ScaleFactor, put_ScaleFactor)
    ShouldPrintBackgrounds = property(get_ShouldPrintBackgrounds, put_ShouldPrintBackgrounds)
    ShouldPrintHeaderAndFooter = property(get_ShouldPrintHeaderAndFooter, put_ShouldPrintHeaderAndFooter)
    ShouldPrintSelectionOnly = property(get_ShouldPrintSelectionOnly, put_ShouldPrintSelectionOnly)
class ICoreWebView2PrintSettings2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2PrintSettings2'
    _iid_ = Guid('{d2a97895-ca6e-57fc-905d-c6f77a081768}')
    @winrt_commethod(6)
    def get_PageRanges(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_PageRanges(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_PagesPerSide(self) -> Int32: ...
    @winrt_commethod(9)
    def put_PagesPerSide(self, value: Int32) -> Void: ...
    @winrt_commethod(10)
    def get_Copies(self) -> Int32: ...
    @winrt_commethod(11)
    def put_Copies(self, value: Int32) -> Void: ...
    @winrt_commethod(12)
    def get_Collation(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintCollation: ...
    @winrt_commethod(13)
    def put_Collation(self, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintCollation) -> Void: ...
    @winrt_commethod(14)
    def get_ColorMode(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintColorMode: ...
    @winrt_commethod(15)
    def put_ColorMode(self, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintColorMode) -> Void: ...
    @winrt_commethod(16)
    def get_Duplex(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintDuplex: ...
    @winrt_commethod(17)
    def put_Duplex(self, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintDuplex) -> Void: ...
    @winrt_commethod(18)
    def get_MediaSize(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintMediaSize: ...
    @winrt_commethod(19)
    def put_MediaSize(self, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintMediaSize) -> Void: ...
    @winrt_commethod(20)
    def get_PrinterName(self) -> WinRT_String: ...
    @winrt_commethod(21)
    def put_PrinterName(self, value: WinRT_String) -> Void: ...
    Collation = property(get_Collation, put_Collation)
    ColorMode = property(get_ColorMode, put_ColorMode)
    Copies = property(get_Copies, put_Copies)
    Duplex = property(get_Duplex, put_Duplex)
    MediaSize = property(get_MediaSize, put_MediaSize)
    PageRanges = property(get_PageRanges, put_PageRanges)
    PagesPerSide = property(get_PagesPerSide, put_PagesPerSide)
    PrinterName = property(get_PrinterName, put_PrinterName)
class ICoreWebView2PrivatePartial(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2PrivatePartial'
    _iid_ = Guid('{2850f27c-0c9d-5cdc-b356-18f5b97d9fcf}')
class ICoreWebView2PrivatePartialController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2PrivatePartialController'
    _iid_ = Guid('{527f6678-8629-5c2a-bc3b-8d5c95e2b9bc}')
    @winrt_commethod(6)
    def get_IsBrowserHitTransparent(self) -> Boolean: ...
    IsBrowserHitTransparent = property(get_IsBrowserHitTransparent, None)
class ICoreWebView2ProcessExtendedInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2ProcessExtendedInfo'
    _iid_ = Guid('{60e9238b-621d-57e8-b670-74382b2380a7}')
    @winrt_commethod(6)
    def get_ProcessInfo(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ProcessInfo: ...
    @winrt_commethod(7)
    def get_AssociatedFrameInfos(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Web.WebView2.Core.CoreWebView2FrameInfo]: ...
    AssociatedFrameInfos = property(get_AssociatedFrameInfos, None)
    ProcessInfo = property(get_ProcessInfo, None)
class ICoreWebView2ProcessFailedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2ProcessFailedEventArgs'
    _iid_ = Guid('{25a8f8c9-d944-539d-afa3-24172b48ef47}')
    @winrt_commethod(6)
    def get_ProcessFailedKind(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ProcessFailedKind: ...
    ProcessFailedKind = property(get_ProcessFailedKind, None)
class ICoreWebView2ProcessFailedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2ProcessFailedEventArgs2'
    _iid_ = Guid('{c5d9c952-b456-5dc7-9f76-fde967484af5}')
    @winrt_commethod(6)
    def get_Reason(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ProcessFailedReason: ...
    @winrt_commethod(7)
    def get_ExitCode(self) -> Int32: ...
    @winrt_commethod(8)
    def get_ProcessDescription(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_FrameInfosForFailedProcess(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.Web.WebView2.Core.CoreWebView2FrameInfo]: ...
    ExitCode = property(get_ExitCode, None)
    FrameInfosForFailedProcess = property(get_FrameInfosForFailedProcess, None)
    ProcessDescription = property(get_ProcessDescription, None)
    Reason = property(get_Reason, None)
class ICoreWebView2ProcessFailedEventArgs3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2ProcessFailedEventArgs3'
    _iid_ = Guid('{d129a419-adae-5c3c-8fce-5592994e9cd3}')
    @winrt_commethod(6)
    def get_FailureSourceModulePath(self) -> WinRT_String: ...
    FailureSourceModulePath = property(get_FailureSourceModulePath, None)
class ICoreWebView2ProcessInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2ProcessInfo'
    _iid_ = Guid('{b6ec37e1-23eb-5924-b346-e837890aa9d5}')
    @winrt_commethod(6)
    def get_ProcessId(self) -> Int32: ...
    @winrt_commethod(7)
    def get_Kind(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ProcessKind: ...
    Kind = property(get_Kind, None)
    ProcessId = property(get_ProcessId, None)
class ICoreWebView2Profile(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Profile'
    _iid_ = Guid('{d4bdd25c-a2db-5c03-9659-abdeb9793621}')
    @winrt_commethod(6)
    def get_ProfileName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_IsInPrivateModeEnabled(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_ProfilePath(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_DefaultDownloadFolderPath(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def put_DefaultDownloadFolderPath(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(11)
    def get_PreferredColorScheme(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2PreferredColorScheme: ...
    @winrt_commethod(12)
    def put_PreferredColorScheme(self, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PreferredColorScheme) -> Void: ...
    DefaultDownloadFolderPath = property(get_DefaultDownloadFolderPath, put_DefaultDownloadFolderPath)
    IsInPrivateModeEnabled = property(get_IsInPrivateModeEnabled, None)
    PreferredColorScheme = property(get_PreferredColorScheme, put_PreferredColorScheme)
    ProfileName = property(get_ProfileName, None)
    ProfilePath = property(get_ProfilePath, None)
class ICoreWebView2Profile2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Profile2'
    _iid_ = Guid('{93d21e18-1b06-59d0-9687-10f4844b016d}')
    @winrt_commethod(6)
    def ClearBrowsingDataAsync(self, dataKinds: win32more.Microsoft.Web.WebView2.Core.CoreWebView2BrowsingDataKinds) -> win32more.Windows.Foundation.IAsyncAction: ...
class ICoreWebView2Profile3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Profile3'
    _iid_ = Guid('{507ed587-c511-5e47-be5b-fc9ccdf179b6}')
    @winrt_commethod(6)
    def get_PreferredTrackingPreventionLevel(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2TrackingPreventionLevel: ...
    @winrt_commethod(7)
    def put_PreferredTrackingPreventionLevel(self, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2TrackingPreventionLevel) -> Void: ...
    PreferredTrackingPreventionLevel = property(get_PreferredTrackingPreventionLevel, put_PreferredTrackingPreventionLevel)
class ICoreWebView2Profile4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Profile4'
    _iid_ = Guid('{eeae109a-f641-5a5b-942f-9922594ffb4d}')
    @winrt_commethod(6)
    def SetPermissionStateAsync(self, PermissionKind: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PermissionKind, origin: WinRT_String, State: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PermissionState) -> win32more.Windows.Foundation.IAsyncAction: ...
class ICoreWebView2Profile5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Profile5'
    _iid_ = Guid('{c9aac8f7-e502-5485-b033-99e4940ee0f1}')
    @winrt_commethod(6)
    def get_CookieManager(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2CookieManager: ...
    CookieManager = property(get_CookieManager, None)
class ICoreWebView2Profile6(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Profile6'
    _iid_ = Guid('{c16a4665-9d44-5768-94a3-69b3976fc3d6}')
    @winrt_commethod(6)
    def get_IsPasswordAutosaveEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsPasswordAutosaveEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_IsGeneralAutofillEnabled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IsGeneralAutofillEnabled(self, value: Boolean) -> Void: ...
    IsGeneralAutofillEnabled = property(get_IsGeneralAutofillEnabled, put_IsGeneralAutofillEnabled)
    IsPasswordAutosaveEnabled = property(get_IsPasswordAutosaveEnabled, put_IsPasswordAutosaveEnabled)
class ICoreWebView2Profile7(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Profile7'
    _iid_ = Guid('{5f665761-5c12-5f39-b9fe-607e6e94add1}')
    @winrt_commethod(6)
    def AddBrowserExtensionAsync(self, extensionFolderPath: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Web.WebView2.Core.CoreWebView2BrowserExtension]: ...
class ICoreWebView2Profile8(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Profile8'
    _iid_ = Guid('{9362d39c-d521-59e9-88fd-7c5aa1167da6}')
    @winrt_commethod(6)
    def add_Deleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2Profile, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Deleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def Delete(self) -> Void: ...
    Deleted = event()
class ICoreWebView2SaveAsUIShowingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2SaveAsUIShowingEventArgs'
    _iid_ = Guid('{cc39a250-2b4c-5608-9097-c59b8a8231b9}')
    @winrt_commethod(6)
    def get_ContentMimeType(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Cancel(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Cancel(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_SuppressDefaultDialog(self) -> Boolean: ...
    @winrt_commethod(10)
    def put_SuppressDefaultDialog(self, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_SaveAsFilePath(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def put_SaveAsFilePath(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(13)
    def get_AllowReplace(self) -> Boolean: ...
    @winrt_commethod(14)
    def put_AllowReplace(self, value: Boolean) -> Void: ...
    @winrt_commethod(15)
    def get_Kind(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2SaveAsKind: ...
    @winrt_commethod(16)
    def put_Kind(self, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2SaveAsKind) -> Void: ...
    @winrt_commethod(17)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    AllowReplace = property(get_AllowReplace, put_AllowReplace)
    Cancel = property(get_Cancel, put_Cancel)
    ContentMimeType = property(get_ContentMimeType, None)
    Kind = property(get_Kind, put_Kind)
    SaveAsFilePath = property(get_SaveAsFilePath, put_SaveAsFilePath)
    SuppressDefaultDialog = property(get_SuppressDefaultDialog, put_SuppressDefaultDialog)
class ICoreWebView2SaveFileSecurityCheckStartingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2SaveFileSecurityCheckStartingEventArgs'
    _iid_ = Guid('{6f6b50ff-3eae-5c4c-a29f-6fce822a04e0}')
    @winrt_commethod(6)
    def get_CancelSave(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_CancelSave(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_DocumentOriginUri(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_FileExtension(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_FilePath(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_SuppressDefaultPolicy(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_SuppressDefaultPolicy(self, value: Boolean) -> Void: ...
    @winrt_commethod(13)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    CancelSave = property(get_CancelSave, put_CancelSave)
    DocumentOriginUri = property(get_DocumentOriginUri, None)
    FileExtension = property(get_FileExtension, None)
    FilePath = property(get_FilePath, None)
    SuppressDefaultPolicy = property(get_SuppressDefaultPolicy, put_SuppressDefaultPolicy)
class ICoreWebView2ScreenCaptureStartingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2ScreenCaptureStartingEventArgs'
    _iid_ = Guid('{35f0e2bb-94b0-5be7-b633-f87244e38bfe}')
    @winrt_commethod(6)
    def get_Cancel(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Cancel(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_OriginalSourceFrameInfo(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2FrameInfo: ...
    @winrt_commethod(11)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Cancel = property(get_Cancel, put_Cancel)
    Handled = property(get_Handled, put_Handled)
    OriginalSourceFrameInfo = property(get_OriginalSourceFrameInfo, None)
class ICoreWebView2ScriptDialogOpeningEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2ScriptDialogOpeningEventArgs'
    _iid_ = Guid('{a4315212-c7eb-568a-86e4-c61e31ba6cda}')
    @winrt_commethod(6)
    def get_Uri(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Kind(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ScriptDialogKind: ...
    @winrt_commethod(8)
    def get_Message(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_DefaultText(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_ResultText(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_ResultText(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(12)
    def Accept(self) -> Void: ...
    @winrt_commethod(13)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    DefaultText = property(get_DefaultText, None)
    Kind = property(get_Kind, None)
    Message = property(get_Message, None)
    ResultText = property(get_ResultText, put_ResultText)
    Uri = property(get_Uri, None)
class ICoreWebView2ScriptException(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2ScriptException'
    _iid_ = Guid('{09bc3ce3-3978-50a5-86ae-5c596d371c4e}')
    @winrt_commethod(6)
    def get_LineNumber(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_ColumnNumber(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_Name(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Message(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_ToJson(self) -> WinRT_String: ...
    ColumnNumber = property(get_ColumnNumber, None)
    LineNumber = property(get_LineNumber, None)
    Message = property(get_Message, None)
    Name = property(get_Name, None)
    ToJson = property(get_ToJson, None)
class ICoreWebView2ServerCertificateErrorDetectedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2ServerCertificateErrorDetectedEventArgs'
    _iid_ = Guid('{90fdc703-5a9e-56f6-a422-7c114c736420}')
    @winrt_commethod(6)
    def get_ErrorStatus(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebErrorStatus: ...
    @winrt_commethod(7)
    def get_RequestUri(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_ServerCertificate(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2Certificate: ...
    @winrt_commethod(9)
    def get_Action(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2ServerCertificateErrorAction: ...
    @winrt_commethod(10)
    def put_Action(self, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2ServerCertificateErrorAction) -> Void: ...
    @winrt_commethod(11)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Action = property(get_Action, put_Action)
    ErrorStatus = property(get_ErrorStatus, None)
    RequestUri = property(get_RequestUri, None)
    ServerCertificate = property(get_ServerCertificate, None)
class ICoreWebView2Settings(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Settings'
    _iid_ = Guid('{003b325e-74cd-52dd-8024-ebb8be38e48e}')
    @winrt_commethod(6)
    def get_IsScriptEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsScriptEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_IsWebMessageEnabled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IsWebMessageEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_AreDefaultScriptDialogsEnabled(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_AreDefaultScriptDialogsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_IsStatusBarEnabled(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_IsStatusBarEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_AreDevToolsEnabled(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_AreDevToolsEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def get_AreDefaultContextMenusEnabled(self) -> Boolean: ...
    @winrt_commethod(17)
    def put_AreDefaultContextMenusEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(18)
    def get_AreHostObjectsAllowed(self) -> Boolean: ...
    @winrt_commethod(19)
    def put_AreHostObjectsAllowed(self, value: Boolean) -> Void: ...
    @winrt_commethod(20)
    def get_IsZoomControlEnabled(self) -> Boolean: ...
    @winrt_commethod(21)
    def put_IsZoomControlEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(22)
    def get_IsBuiltInErrorPageEnabled(self) -> Boolean: ...
    @winrt_commethod(23)
    def put_IsBuiltInErrorPageEnabled(self, value: Boolean) -> Void: ...
    AreDefaultContextMenusEnabled = property(get_AreDefaultContextMenusEnabled, put_AreDefaultContextMenusEnabled)
    AreDefaultScriptDialogsEnabled = property(get_AreDefaultScriptDialogsEnabled, put_AreDefaultScriptDialogsEnabled)
    AreDevToolsEnabled = property(get_AreDevToolsEnabled, put_AreDevToolsEnabled)
    AreHostObjectsAllowed = property(get_AreHostObjectsAllowed, put_AreHostObjectsAllowed)
    IsBuiltInErrorPageEnabled = property(get_IsBuiltInErrorPageEnabled, put_IsBuiltInErrorPageEnabled)
    IsScriptEnabled = property(get_IsScriptEnabled, put_IsScriptEnabled)
    IsStatusBarEnabled = property(get_IsStatusBarEnabled, put_IsStatusBarEnabled)
    IsWebMessageEnabled = property(get_IsWebMessageEnabled, put_IsWebMessageEnabled)
    IsZoomControlEnabled = property(get_IsZoomControlEnabled, put_IsZoomControlEnabled)
class ICoreWebView2Settings2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Settings2'
    _iid_ = Guid('{377d3480-fdb2-56e7-bade-507d352887e9}')
    @winrt_commethod(6)
    def get_UserAgent(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_UserAgent(self, value: WinRT_String) -> Void: ...
    UserAgent = property(get_UserAgent, put_UserAgent)
class ICoreWebView2Settings3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Settings3'
    _iid_ = Guid('{52200f01-5309-5b2e-a03c-3d2677591940}')
    @winrt_commethod(6)
    def get_AreBrowserAcceleratorKeysEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AreBrowserAcceleratorKeysEnabled(self, value: Boolean) -> Void: ...
    AreBrowserAcceleratorKeysEnabled = property(get_AreBrowserAcceleratorKeysEnabled, put_AreBrowserAcceleratorKeysEnabled)
class ICoreWebView2Settings4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Settings4'
    _iid_ = Guid('{d6a955f0-daef-5a6a-a6f6-c72f0ede7620}')
    @winrt_commethod(6)
    def get_IsPasswordAutosaveEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsPasswordAutosaveEnabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_IsGeneralAutofillEnabled(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IsGeneralAutofillEnabled(self, value: Boolean) -> Void: ...
    IsGeneralAutofillEnabled = property(get_IsGeneralAutofillEnabled, put_IsGeneralAutofillEnabled)
    IsPasswordAutosaveEnabled = property(get_IsPasswordAutosaveEnabled, put_IsPasswordAutosaveEnabled)
class ICoreWebView2Settings5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Settings5'
    _iid_ = Guid('{afc42b23-4839-5d73-acf7-e0335631abf5}')
    @winrt_commethod(6)
    def get_IsPinchZoomEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsPinchZoomEnabled(self, value: Boolean) -> Void: ...
    IsPinchZoomEnabled = property(get_IsPinchZoomEnabled, put_IsPinchZoomEnabled)
class ICoreWebView2Settings6(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Settings6'
    _iid_ = Guid('{3fe4ae85-0540-5bf1-b4d9-99ec57aa64f5}')
    @winrt_commethod(6)
    def get_IsSwipeNavigationEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsSwipeNavigationEnabled(self, value: Boolean) -> Void: ...
    IsSwipeNavigationEnabled = property(get_IsSwipeNavigationEnabled, put_IsSwipeNavigationEnabled)
class ICoreWebView2Settings7(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Settings7'
    _iid_ = Guid('{688027cd-9f84-59e8-8d5c-91123df24b92}')
    @winrt_commethod(6)
    def get_HiddenPdfToolbarItems(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2PdfToolbarItems: ...
    @winrt_commethod(7)
    def put_HiddenPdfToolbarItems(self, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PdfToolbarItems) -> Void: ...
    HiddenPdfToolbarItems = property(get_HiddenPdfToolbarItems, put_HiddenPdfToolbarItems)
class ICoreWebView2Settings8(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Settings8'
    _iid_ = Guid('{956f1a8f-3198-5577-b250-7d91d17f7eed}')
    @winrt_commethod(6)
    def get_IsReputationCheckingRequired(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsReputationCheckingRequired(self, value: Boolean) -> Void: ...
    IsReputationCheckingRequired = property(get_IsReputationCheckingRequired, put_IsReputationCheckingRequired)
class ICoreWebView2Settings9(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Settings9'
    _iid_ = Guid('{4c346681-714d-5a3d-8105-2a7b80beeab5}')
    @winrt_commethod(6)
    def get_IsNonClientRegionSupportEnabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsNonClientRegionSupportEnabled(self, value: Boolean) -> Void: ...
    IsNonClientRegionSupportEnabled = property(get_IsNonClientRegionSupportEnabled, put_IsNonClientRegionSupportEnabled)
class ICoreWebView2Settings_Manual(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2Settings_Manual'
    _iid_ = Guid('{0a538c87-e000-511c-87ca-ded3413d03da}')
    @winrt_commethod(6)
    def get_HostObjectDispatchAdapter(self) -> win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DispatchAdapter: ...
    @winrt_commethod(7)
    def put_HostObjectDispatchAdapter(self, value: win32more.Microsoft.Web.WebView2.Core.ICoreWebView2DispatchAdapter) -> Void: ...
    HostObjectDispatchAdapter = property(get_HostObjectDispatchAdapter, put_HostObjectDispatchAdapter)
class ICoreWebView2SharedBuffer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2SharedBuffer'
    _iid_ = Guid('{2907cc84-f843-5959-8734-f871766f8f13}')
    @winrt_commethod(6)
    def get_Size(self) -> UInt64: ...
    @winrt_commethod(7)
    def OpenStream(self) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    Size = property(get_Size, None)
class ICoreWebView2SharedBuffer_Manual(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2SharedBuffer_Manual'
    _iid_ = Guid('{1aa4e213-ace3-5f74-a2ae-c6489ceb3239}')
    @winrt_commethod(6)
    def get_Buffer(self) -> win32more.Windows.Foundation.IMemoryBufferReference: ...
    Buffer = property(get_Buffer, None)
class ICoreWebView2SourceChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2SourceChangedEventArgs'
    _iid_ = Guid('{ca437b2c-6a18-5552-b749-b198f8cc34d9}')
    @winrt_commethod(6)
    def get_IsNewDocument(self) -> Boolean: ...
    IsNewDocument = property(get_IsNewDocument, None)
class ICoreWebView2WebMessageReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2WebMessageReceivedEventArgs'
    _iid_ = Guid('{eb066159-b725-5d5b-adc8-f5d7b9290304}')
    @winrt_commethod(6)
    def get_Source(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_WebMessageAsJson(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def TryGetWebMessageAsString(self) -> WinRT_String: ...
    Source = property(get_Source, None)
    WebMessageAsJson = property(get_WebMessageAsJson, None)
class ICoreWebView2WebMessageReceivedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2WebMessageReceivedEventArgs2'
    _iid_ = Guid('{71dc5fa0-08a0-5dea-9363-799df5021452}')
    @winrt_commethod(6)
    def get_AdditionalObjects(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Win32.System.WinRT.IInspectable]: ...
    AdditionalObjects = property(get_AdditionalObjects, None)
class ICoreWebView2WebResourceRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceRequest'
    _iid_ = Guid('{5c742259-67d2-5df2-8382-0f201b4d7197}')
    @winrt_commethod(6)
    def get_Uri(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Uri(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Method(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Method(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Content(self) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_commethod(11)
    def put_Content(self, value: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Void: ...
    @winrt_commethod(12)
    def get_Headers(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2HttpRequestHeaders: ...
    Content = property(get_Content, put_Content)
    Headers = property(get_Headers, None)
    Method = property(get_Method, put_Method)
    Uri = property(get_Uri, put_Uri)
class ICoreWebView2WebResourceRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceRequestedEventArgs'
    _iid_ = Guid('{577f1fc4-c943-54a9-9700-bd469b48bd41}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceRequest: ...
    @winrt_commethod(7)
    def get_Response(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceResponse: ...
    @winrt_commethod(8)
    def put_Response(self, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceResponse) -> Void: ...
    @winrt_commethod(9)
    def get_ResourceContext(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceContext: ...
    @winrt_commethod(10)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    Request = property(get_Request, None)
    ResourceContext = property(get_ResourceContext, None)
    Response = property(get_Response, put_Response)
class ICoreWebView2WebResourceRequestedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceRequestedEventArgs2'
    _iid_ = Guid('{0bbe4b89-88a9-575a-b09e-7946ee415e94}')
    @winrt_commethod(6)
    def get_RequestedSourceKind(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceRequestSourceKinds: ...
    RequestedSourceKind = property(get_RequestedSourceKind, None)
class ICoreWebView2WebResourceResponse(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceResponse'
    _iid_ = Guid('{14621923-e485-5f44-8f5d-bd4243bc398f}')
    @winrt_commethod(6)
    def get_Content(self) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_commethod(7)
    def put_Content(self, value: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Void: ...
    @winrt_commethod(8)
    def get_Headers(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2HttpResponseHeaders: ...
    @winrt_commethod(9)
    def get_StatusCode(self) -> Int32: ...
    @winrt_commethod(10)
    def put_StatusCode(self, value: Int32) -> Void: ...
    @winrt_commethod(11)
    def get_ReasonPhrase(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def put_ReasonPhrase(self, value: WinRT_String) -> Void: ...
    Content = property(get_Content, put_Content)
    Headers = property(get_Headers, None)
    ReasonPhrase = property(get_ReasonPhrase, put_ReasonPhrase)
    StatusCode = property(get_StatusCode, put_StatusCode)
class ICoreWebView2WebResourceResponseReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceResponseReceivedEventArgs'
    _iid_ = Guid('{12424671-9711-54f4-bcdf-5f307add6ec2}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceRequest: ...
    @winrt_commethod(7)
    def get_Response(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceResponseView: ...
    Request = property(get_Request, None)
    Response = property(get_Response, None)
class ICoreWebView2WebResourceResponseView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2WebResourceResponseView'
    _iid_ = Guid('{33ee060b-b578-5698-b541-fef87fe7fe72}')
    @winrt_commethod(6)
    def get_Headers(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2HttpResponseHeaders: ...
    @winrt_commethod(7)
    def get_StatusCode(self) -> Int32: ...
    @winrt_commethod(8)
    def get_ReasonPhrase(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def GetContentAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    Headers = property(get_Headers, None)
    ReasonPhrase = property(get_ReasonPhrase, None)
    StatusCode = property(get_StatusCode, None)
class ICoreWebView2WindowFeatures(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2WindowFeatures'
    _iid_ = Guid('{ee8686d6-056f-5e06-824f-4e2a24c1c1d6}')
    @winrt_commethod(6)
    def get_HasPosition(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_HasSize(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_Left(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_Top(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_Height(self) -> UInt32: ...
    @winrt_commethod(11)
    def get_Width(self) -> UInt32: ...
    @winrt_commethod(12)
    def get_ShouldDisplayMenuBar(self) -> Boolean: ...
    @winrt_commethod(13)
    def get_ShouldDisplayStatus(self) -> Boolean: ...
    @winrt_commethod(14)
    def get_ShouldDisplayToolbar(self) -> Boolean: ...
    @winrt_commethod(15)
    def get_ShouldDisplayScrollBars(self) -> Boolean: ...
    HasPosition = property(get_HasPosition, None)
    HasSize = property(get_HasSize, None)
    Height = property(get_Height, None)
    Left = property(get_Left, None)
    ShouldDisplayMenuBar = property(get_ShouldDisplayMenuBar, None)
    ShouldDisplayScrollBars = property(get_ShouldDisplayScrollBars, None)
    ShouldDisplayStatus = property(get_ShouldDisplayStatus, None)
    ShouldDisplayToolbar = property(get_ShouldDisplayToolbar, None)
    Top = property(get_Top, None)
    Width = property(get_Width, None)
class ICoreWebView2_10(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2_10'
    _iid_ = Guid('{a7b20434-970f-54b1-aa63-3c42671fa9ab}')
    @winrt_commethod(6)
    def add_BasicAuthenticationRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2BasicAuthenticationRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_BasicAuthenticationRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    BasicAuthenticationRequested = event()
class ICoreWebView2_11(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2_11'
    _iid_ = Guid('{c00acbb1-ae32-501f-ad19-9d0ac32d6142}')
    @winrt_commethod(6)
    def add_ContextMenuRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2ContextMenuRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ContextMenuRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def CallDevToolsProtocolMethodForSessionAsync(self, sessionId: WinRT_String, methodName: WinRT_String, parametersAsJson: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    ContextMenuRequested = event()
class ICoreWebView2_12(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2_12'
    _iid_ = Guid('{dbbbe9a1-18d3-5f67-b362-0f4ae937d754}')
    @winrt_commethod(6)
    def get_StatusBarText(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def add_StatusBarTextChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_StatusBarTextChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    StatusBarText = property(get_StatusBarText, None)
    StatusBarTextChanged = event()
class ICoreWebView2_13(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2_13'
    _iid_ = Guid('{314b5846-dbc7-5de4-a792-647ea0f3296a}')
    @winrt_commethod(6)
    def get_Profile(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2Profile: ...
    Profile = property(get_Profile, None)
class ICoreWebView2_14(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2_14'
    _iid_ = Guid('{a7647b24-3b1e-50a9-be24-6e8ac63fe491}')
    @winrt_commethod(6)
    def add_ServerCertificateErrorDetected(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2ServerCertificateErrorDetectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ServerCertificateErrorDetected(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def ClearServerCertificateErrorActionsAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    ServerCertificateErrorDetected = event()
class ICoreWebView2_15(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2_15'
    _iid_ = Guid('{4443f532-d2ba-5ae2-a9b3-8de62bd5d4a9}')
    @winrt_commethod(6)
    def get_FaviconUri(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def add_FaviconChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_FaviconChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def GetFaviconAsync(self, format: win32more.Microsoft.Web.WebView2.Core.CoreWebView2FaviconImageFormat) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
    FaviconUri = property(get_FaviconUri, None)
    FaviconChanged = event()
class ICoreWebView2_16(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2_16'
    _iid_ = Guid('{61d0a57c-6c4f-50ff-a137-314b0099a2b8}')
    @winrt_commethod(6)
    def PrintAsync(self, printSettings: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintSettings) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintStatus]: ...
    @winrt_commethod(7)
    def ShowPrintUI(self, printDialogKind: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintDialogKind) -> Void: ...
    @winrt_commethod(8)
    def PrintToPdfStreamAsync(self, printSettings: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintSettings) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStream]: ...
class ICoreWebView2_17(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2_17'
    _iid_ = Guid('{2345f9db-5488-559a-82af-9086cc4f7988}')
    @winrt_commethod(6)
    def PostSharedBufferToScript(self, sharedBuffer: win32more.Microsoft.Web.WebView2.Core.CoreWebView2SharedBuffer, access: win32more.Microsoft.Web.WebView2.Core.CoreWebView2SharedBufferAccess, additionalDataAsJson: WinRT_String) -> Void: ...
class ICoreWebView2_18(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2_18'
    _iid_ = Guid('{94f52e61-9d75-5a81-acd3-830ff29ce6f7}')
    @winrt_commethod(6)
    def add_LaunchingExternalUriScheme(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2LaunchingExternalUriSchemeEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_LaunchingExternalUriScheme(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    LaunchingExternalUriScheme = event()
class ICoreWebView2_19(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2_19'
    _iid_ = Guid('{35a94a5c-e027-5dc5-8c2b-c2fc7d589159}')
    @winrt_commethod(6)
    def get_MemoryUsageTargetLevel(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2MemoryUsageTargetLevel: ...
    @winrt_commethod(7)
    def put_MemoryUsageTargetLevel(self, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2MemoryUsageTargetLevel) -> Void: ...
    MemoryUsageTargetLevel = property(get_MemoryUsageTargetLevel, put_MemoryUsageTargetLevel)
class ICoreWebView2_2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2_2'
    _iid_ = Guid('{578cb133-2873-5408-bd9e-389bbe9fa7fa}')
    @winrt_commethod(6)
    def get_CookieManager(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2CookieManager: ...
    @winrt_commethod(7)
    def get_Environment(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2Environment: ...
    @winrt_commethod(8)
    def add_WebResourceResponseReceived(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceResponseReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_WebResourceResponseReceived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_DOMContentLoaded(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2DOMContentLoadedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_DOMContentLoaded(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def NavigateWithWebResourceRequest(self, Request: win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceRequest) -> Void: ...
    CookieManager = property(get_CookieManager, None)
    Environment = property(get_Environment, None)
    WebResourceResponseReceived = event()
    DOMContentLoaded = event()
class ICoreWebView2_20(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2_20'
    _iid_ = Guid('{859c4805-e988-50d5-85d7-a50643fc815e}')
    @winrt_commethod(6)
    def get_FrameId(self) -> UInt32: ...
    FrameId = property(get_FrameId, None)
class ICoreWebView2_21(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2_21'
    _iid_ = Guid('{f7fc7705-7922-5abc-9e24-c64f1c14b185}')
    @winrt_commethod(6)
    def ExecuteScriptWithResultAsync(self, javaScript: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Web.WebView2.Core.CoreWebView2ExecuteScriptResult]: ...
class ICoreWebView2_22(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2_22'
    _iid_ = Guid('{d58aa4cf-9b67-5419-8565-f401a98feeb2}')
class ICoreWebView2_23(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2_23'
    _iid_ = Guid('{d6767391-fdfe-5b95-96ae-11de6b8726dd}')
class ICoreWebView2_24(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2_24'
    _iid_ = Guid('{469056b8-e78d-55ed-9af1-207a7f60911f}')
    @winrt_commethod(6)
    def add_NotificationReceived(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2NotificationReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_NotificationReceived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    NotificationReceived = event()
class ICoreWebView2_25(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2_25'
    _iid_ = Guid('{b8e2edce-d943-5871-8397-483dbd6c0f9e}')
    @winrt_commethod(6)
    def add_SaveAsUIShowing(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2SaveAsUIShowingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_SaveAsUIShowing(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def ShowSaveAsUIAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Microsoft.Web.WebView2.Core.CoreWebView2SaveAsUIResult]: ...
    SaveAsUIShowing = event()
class ICoreWebView2_26(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2_26'
    _iid_ = Guid('{e7d803dd-b2f4-5fa3-8e63-114489d4063d}')
    @winrt_commethod(6)
    def add_SaveFileSecurityCheckStarting(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2SaveFileSecurityCheckStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_SaveFileSecurityCheckStarting(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    SaveFileSecurityCheckStarting = event()
class ICoreWebView2_27(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2_27'
    _iid_ = Guid('{d964f497-ffdf-5bcd-bf52-ff4585f2ebc2}')
    @winrt_commethod(6)
    def add_ScreenCaptureStarting(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2ScreenCaptureStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ScreenCaptureStarting(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ScreenCaptureStarting = event()
class ICoreWebView2_3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2_3'
    _iid_ = Guid('{a8c76ae7-6170-5dfe-8f00-79cd76a9b4d9}')
    @winrt_commethod(6)
    def get_IsSuspended(self) -> Boolean: ...
    @winrt_commethod(7)
    def TrySuspendAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(8)
    def Resume(self) -> Void: ...
    @winrt_commethod(9)
    def SetVirtualHostNameToFolderMapping(self, hostName: WinRT_String, folderPath: WinRT_String, accessKind: win32more.Microsoft.Web.WebView2.Core.CoreWebView2HostResourceAccessKind) -> Void: ...
    @winrt_commethod(10)
    def ClearVirtualHostNameToFolderMapping(self, hostName: WinRT_String) -> Void: ...
    IsSuspended = property(get_IsSuspended, None)
class ICoreWebView2_4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2_4'
    _iid_ = Guid('{4ac595ce-1502-5775-b2c8-22c11a369c25}')
    @winrt_commethod(6)
    def add_FrameCreated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2FrameCreatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_FrameCreated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_DownloadStarting(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2DownloadStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_DownloadStarting(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    FrameCreated = event()
    DownloadStarting = event()
class ICoreWebView2_5(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2_5'
    _iid_ = Guid('{dd6af643-220c-5dc6-b0a8-22c41e472595}')
    @winrt_commethod(6)
    def add_ClientCertificateRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Microsoft.Web.WebView2.Core.CoreWebView2ClientCertificateRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_ClientCertificateRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ClientCertificateRequested = event()
class ICoreWebView2_6(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2_6'
    _iid_ = Guid('{92b34b96-853d-5bb6-ac52-30297ce805f1}')
    @winrt_commethod(6)
    def OpenTaskManagerWindow(self) -> Void: ...
class ICoreWebView2_7(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2_7'
    _iid_ = Guid('{f9b7107a-2e09-5596-a033-911ba12315f7}')
    @winrt_commethod(6)
    def PrintToPdfAsync(self, ResultFilePath: WinRT_String, printSettings: win32more.Microsoft.Web.WebView2.Core.CoreWebView2PrintSettings) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
class ICoreWebView2_8(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2_8'
    _iid_ = Guid('{aa2503c0-8d1c-5a3d-b898-f55f7595268a}')
    @winrt_commethod(6)
    def get_IsMuted(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsMuted(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_IsDocumentPlayingAudio(self) -> Boolean: ...
    @winrt_commethod(9)
    def add_IsMutedChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_IsMutedChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_IsDocumentPlayingAudioChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_IsDocumentPlayingAudioChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsDocumentPlayingAudio = property(get_IsDocumentPlayingAudio, None)
    IsMuted = property(get_IsMuted, put_IsMuted)
    IsMutedChanged = event()
    IsDocumentPlayingAudioChanged = event()
class ICoreWebView2_9(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2_9'
    _iid_ = Guid('{64b2ec16-0b29-5216-bf86-e575c88f7031}')
    @winrt_commethod(6)
    def get_IsDefaultDownloadDialogOpen(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_DefaultDownloadDialogCornerAlignment(self) -> win32more.Microsoft.Web.WebView2.Core.CoreWebView2DefaultDownloadDialogCornerAlignment: ...
    @winrt_commethod(8)
    def put_DefaultDownloadDialogCornerAlignment(self, value: win32more.Microsoft.Web.WebView2.Core.CoreWebView2DefaultDownloadDialogCornerAlignment) -> Void: ...
    @winrt_commethod(9)
    def get_DefaultDownloadDialogMargin(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(10)
    def put_DefaultDownloadDialogMargin(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(11)
    def add_IsDefaultDownloadDialogOpenChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.Web.WebView2.Core.CoreWebView2, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_IsDefaultDownloadDialogOpenChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def OpenDefaultDownloadDialog(self) -> Void: ...
    @winrt_commethod(14)
    def CloseDefaultDownloadDialog(self) -> Void: ...
    DefaultDownloadDialogCornerAlignment = property(get_DefaultDownloadDialogCornerAlignment, put_DefaultDownloadDialogCornerAlignment)
    DefaultDownloadDialogMargin = property(get_DefaultDownloadDialogMargin, put_DefaultDownloadDialogMargin)
    IsDefaultDownloadDialogOpen = property(get_IsDefaultDownloadDialogOpen, None)
    IsDefaultDownloadDialogOpenChanged = event()
class ICoreWebView2_Manual(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2_Manual'
    _iid_ = Guid('{2d988546-9962-516b-be53-859fb0f50179}')
    @winrt_commethod(6)
    def AddWebResourceRequestedFilter(self, uri: WinRT_String, resourceContext: win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceContext, requestSourceKinds: win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceRequestSourceKinds) -> Void: ...
    @winrt_commethod(7)
    def RemoveWebResourceRequestedFilter(self, uri: WinRT_String, resourceContext: win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceContext, requestSourceKinds: win32more.Microsoft.Web.WebView2.Core.CoreWebView2WebResourceRequestSourceKinds) -> Void: ...
class ICoreWebView2_Manual2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.Web.WebView2.Core.ICoreWebView2_Manual2'
    _iid_ = Guid('{57d0c484-f304-52d4-85a6-68cfafd63b61}')
    @winrt_commethod(6)
    def PostWebMessageAsJson(self, webMessageAsJson: WinRT_String, additionalObjects: win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Win32.System.WinRT.IInspectable]) -> Void: ...


make_ready(__name__)
