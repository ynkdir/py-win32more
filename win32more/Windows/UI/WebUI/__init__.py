from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.ApplicationModel
import win32more.Windows.ApplicationModel.Activation
import win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider
import win32more.Windows.ApplicationModel.Background
import win32more.Windows.ApplicationModel.Calls
import win32more.Windows.ApplicationModel.Contacts
import win32more.Windows.ApplicationModel.Contacts.Provider
import win32more.Windows.ApplicationModel.Core
import win32more.Windows.ApplicationModel.DataTransfer
import win32more.Windows.ApplicationModel.DataTransfer.ShareTarget
import win32more.Windows.ApplicationModel.Search
import win32more.Windows.ApplicationModel.UserDataAccounts.Provider
import win32more.Windows.ApplicationModel.Wallet
import win32more.Windows.Devices.Enumeration
import win32more.Windows.Devices.Printers.Extensions
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Graphics.Printing
import win32more.Windows.Media.SpeechRecognition
import win32more.Windows.Security.Authentication.Web
import win32more.Windows.Security.Authentication.Web.Provider
import win32more.Windows.Storage
import win32more.Windows.Storage.Pickers.Provider
import win32more.Windows.Storage.Provider
import win32more.Windows.Storage.Search
import win32more.Windows.Storage.Streams
import win32more.Windows.System
import win32more.Windows.UI
import win32more.Windows.UI.WebUI
import win32more.Windows.Web
import win32more.Windows.Web.Http
import win32more.Windows.Web.UI
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class ActivatedDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.WebUI.IActivatedDeferral
    _classid_ = 'Windows.UI.WebUI.ActivatedDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.UI.WebUI.IActivatedDeferral) -> Void: ...
class ActivatedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{50f1e730-c5d1-4b6b-9adb-8a11756be29c}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, eventArgs: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Void: ...
class ActivatedOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.WebUI.IActivatedOperation
    _classid_ = 'Windows.UI.WebUI.ActivatedOperation'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.UI.WebUI.IActivatedOperation) -> win32more.Windows.UI.WebUI.ActivatedDeferral: ...
class BackgroundActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IBackgroundActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.BackgroundActivatedEventArgs'
    @winrt_mixinmethod
    def get_TaskInstance(self: win32more.Windows.ApplicationModel.Activation.IBackgroundActivatedEventArgs) -> win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance: ...
    TaskInstance = property(get_TaskInstance, None)
class BackgroundActivatedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{edb19fbb-0761-47cc-9a77-24d7072965ca}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, eventArgs: win32more.Windows.ApplicationModel.Activation.IBackgroundActivatedEventArgs) -> Void: ...
class EnteredBackgroundEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.IEnteredBackgroundEventArgs
    _classid_ = 'Windows.UI.WebUI.EnteredBackgroundEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.IEnteredBackgroundEventArgs) -> win32more.Windows.Foundation.Deferral: ...
class EnteredBackgroundEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2b09a173-b68e-4def-88c1-8de84e5aab2f}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.ApplicationModel.IEnteredBackgroundEventArgs) -> Void: ...
class HtmlPrintDocumentSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource
    _classid_ = 'Windows.UI.WebUI.HtmlPrintDocumentSource'
    @winrt_mixinmethod
    def get_Content(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource) -> win32more.Windows.UI.WebUI.PrintContent: ...
    @winrt_mixinmethod
    def put_Content(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource, value: win32more.Windows.UI.WebUI.PrintContent) -> Void: ...
    @winrt_mixinmethod
    def get_LeftMargin(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource) -> Single: ...
    @winrt_mixinmethod
    def put_LeftMargin(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_TopMargin(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource) -> Single: ...
    @winrt_mixinmethod
    def put_TopMargin(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_RightMargin(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource) -> Single: ...
    @winrt_mixinmethod
    def put_RightMargin(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_BottomMargin(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource) -> Single: ...
    @winrt_mixinmethod
    def put_BottomMargin(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_EnableHeaderFooter(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource) -> Boolean: ...
    @winrt_mixinmethod
    def put_EnableHeaderFooter(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ShrinkToFit(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShrinkToFit(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PercentScale(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource) -> Single: ...
    @winrt_mixinmethod
    def put_PercentScale(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource, scalePercent: Single) -> Void: ...
    @winrt_mixinmethod
    def get_PageRange(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def TrySetPageRange(self: win32more.Windows.UI.WebUI.IHtmlPrintDocumentSource, strPageRange: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    BottomMargin = property(get_BottomMargin, put_BottomMargin)
    Content = property(get_Content, put_Content)
    EnableHeaderFooter = property(get_EnableHeaderFooter, put_EnableHeaderFooter)
    LeftMargin = property(get_LeftMargin, put_LeftMargin)
    PageRange = property(get_PageRange, None)
    PercentScale = property(get_PercentScale, put_PercentScale)
    RightMargin = property(get_RightMargin, put_RightMargin)
    ShrinkToFit = property(get_ShrinkToFit, put_ShrinkToFit)
    TopMargin = property(get_TopMargin, put_TopMargin)
class IActivatedDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IActivatedDeferral'
    _iid_ = Guid('{c3bd1978-a431-49d8-a76a-395a4e03dcf3}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IActivatedEventArgsDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IActivatedEventArgsDeferral'
    _iid_ = Guid('{ca6d5f74-63c2-44a6-b97b-d9a03c20bc9b}')
    @winrt_commethod(6)
    def get_ActivatedOperation(self) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
class IActivatedOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IActivatedOperation'
    _iid_ = Guid('{b6a0b4bc-c6ca-42fd-9818-71904e45fed7}')
    @winrt_commethod(6)
    def GetDeferral(self) -> win32more.Windows.UI.WebUI.ActivatedDeferral: ...
class IHtmlPrintDocumentSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IHtmlPrintDocumentSource'
    _iid_ = Guid('{cea6469a-0e05-467a-abc9-36ec1d4cdcb6}')
    @winrt_commethod(6)
    def get_Content(self) -> win32more.Windows.UI.WebUI.PrintContent: ...
    @winrt_commethod(7)
    def put_Content(self, value: win32more.Windows.UI.WebUI.PrintContent) -> Void: ...
    @winrt_commethod(8)
    def get_LeftMargin(self) -> Single: ...
    @winrt_commethod(9)
    def put_LeftMargin(self, value: Single) -> Void: ...
    @winrt_commethod(10)
    def get_TopMargin(self) -> Single: ...
    @winrt_commethod(11)
    def put_TopMargin(self, value: Single) -> Void: ...
    @winrt_commethod(12)
    def get_RightMargin(self) -> Single: ...
    @winrt_commethod(13)
    def put_RightMargin(self, value: Single) -> Void: ...
    @winrt_commethod(14)
    def get_BottomMargin(self) -> Single: ...
    @winrt_commethod(15)
    def put_BottomMargin(self, value: Single) -> Void: ...
    @winrt_commethod(16)
    def get_EnableHeaderFooter(self) -> Boolean: ...
    @winrt_commethod(17)
    def put_EnableHeaderFooter(self, value: Boolean) -> Void: ...
    @winrt_commethod(18)
    def get_ShrinkToFit(self) -> Boolean: ...
    @winrt_commethod(19)
    def put_ShrinkToFit(self, value: Boolean) -> Void: ...
    @winrt_commethod(20)
    def get_PercentScale(self) -> Single: ...
    @winrt_commethod(21)
    def put_PercentScale(self, scalePercent: Single) -> Void: ...
    @winrt_commethod(22)
    def get_PageRange(self) -> WinRT_String: ...
    @winrt_commethod(23)
    def TrySetPageRange(self, strPageRange: WinRT_String) -> Boolean: ...
    BottomMargin = property(get_BottomMargin, put_BottomMargin)
    Content = property(get_Content, put_Content)
    EnableHeaderFooter = property(get_EnableHeaderFooter, put_EnableHeaderFooter)
    LeftMargin = property(get_LeftMargin, put_LeftMargin)
    PageRange = property(get_PageRange, None)
    PercentScale = property(get_PercentScale, put_PercentScale)
    RightMargin = property(get_RightMargin, put_RightMargin)
    ShrinkToFit = property(get_ShrinkToFit, put_ShrinkToFit)
    TopMargin = property(get_TopMargin, put_TopMargin)
class INewWebUIViewCreatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.INewWebUIViewCreatedEventArgs'
    _iid_ = Guid('{e8e1b216-be2b-4c9e-85e7-083143ec4be7}')
    @winrt_commethod(6)
    def get_WebUIView(self) -> win32more.Windows.UI.WebUI.WebUIView: ...
    @winrt_commethod(7)
    def get_ActivatedEventArgs(self) -> win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs: ...
    @winrt_commethod(8)
    def get_HasPendingNavigate(self) -> Boolean: ...
    @winrt_commethod(9)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
    ActivatedEventArgs = property(get_ActivatedEventArgs, None)
    HasPendingNavigate = property(get_HasPendingNavigate, None)
    WebUIView = property(get_WebUIView, None)
class IWebUIActivationStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUIActivationStatics'
    _iid_ = Guid('{351b86bd-43b3-482b-85db-35d87b517ad9}')
    @winrt_commethod(6)
    def add_Activated(self, handler: win32more.Windows.UI.WebUI.ActivatedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Activated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_Suspending(self, handler: win32more.Windows.UI.WebUI.SuspendingEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Suspending(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Resuming(self, handler: win32more.Windows.UI.WebUI.ResumingEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Resuming(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_Navigated(self, handler: win32more.Windows.UI.WebUI.NavigatedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_Navigated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Activated = event()
    Suspending = event()
    Resuming = event()
    Navigated = event()
class IWebUIActivationStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUIActivationStatics2'
    _iid_ = Guid('{c8e88696-4d78-4aa4-8f06-2a9eadc6c40a}')
    @winrt_commethod(6)
    def add_LeavingBackground(self, handler: win32more.Windows.UI.WebUI.LeavingBackgroundEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_LeavingBackground(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_EnteredBackground(self, handler: win32more.Windows.UI.WebUI.EnteredBackgroundEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_EnteredBackground(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def EnablePrelaunch(self, value: Boolean) -> Void: ...
    LeavingBackground = event()
    EnteredBackground = event()
class IWebUIActivationStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUIActivationStatics3'
    _iid_ = Guid('{91abb686-1af5-4445-b49f-9459f40fc8de}')
    @winrt_commethod(6)
    def RequestRestartAsync(self, launchArguments: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Core.AppRestartFailureReason]: ...
    @winrt_commethod(7)
    def RequestRestartForUserAsync(self, user: win32more.Windows.System.User, launchArguments: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Core.AppRestartFailureReason]: ...
class IWebUIActivationStatics4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUIActivationStatics4'
    _iid_ = Guid('{5e391429-183f-478d-8a25-67f80d03935b}')
    @winrt_commethod(6)
    def add_NewWebUIViewCreated(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.UI.WebUI.NewWebUIViewCreatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_NewWebUIViewCreated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_BackgroundActivated(self, handler: win32more.Windows.UI.WebUI.BackgroundActivatedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_BackgroundActivated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    NewWebUIViewCreated = event()
    BackgroundActivated = event()
class IWebUIBackgroundTaskInstance(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUIBackgroundTaskInstance'
    _iid_ = Guid('{23f12c25-e2f7-4741-bc9c-394595de24dc}')
    @winrt_commethod(6)
    def get_Succeeded(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Succeeded(self, succeeded: Boolean) -> Void: ...
    Succeeded = property(get_Succeeded, put_Succeeded)
class IWebUIBackgroundTaskInstanceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUIBackgroundTaskInstanceStatics'
    _iid_ = Guid('{9c7a5291-19ae-4ca3-b94b-fe4ec744a740}')
    @winrt_commethod(6)
    def get_Current(self) -> win32more.Windows.UI.WebUI.IWebUIBackgroundTaskInstance: ...
    Current = property(get_Current, None)
class IWebUINavigatedDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUINavigatedDeferral'
    _iid_ = Guid('{d804204d-831f-46e2-b432-3afce211f962}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IWebUINavigatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUINavigatedEventArgs'
    _iid_ = Guid('{a75841b8-2499-4030-a69d-15d2d9cfe524}')
    @winrt_commethod(6)
    def get_NavigatedOperation(self) -> win32more.Windows.UI.WebUI.WebUINavigatedOperation: ...
    NavigatedOperation = property(get_NavigatedOperation, None)
class IWebUINavigatedOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUINavigatedOperation'
    _iid_ = Guid('{7a965f08-8182-4a89-ab67-8492e8750d4b}')
    @winrt_commethod(6)
    def GetDeferral(self) -> win32more.Windows.UI.WebUI.WebUINavigatedDeferral: ...
class IWebUIView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUIView'
    _iid_ = Guid('{6783f64f-52da-4fd7-be69-8ef6284b423c}')
    @winrt_commethod(6)
    def get_ApplicationViewId(self) -> Int32: ...
    @winrt_commethod(7)
    def add_Closed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.WebUI.WebUIView, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_Closed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_Activated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.WebUI.WebUIView, win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Activated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def get_IgnoreApplicationContentUriRulesNavigationRestrictions(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_IgnoreApplicationContentUriRulesNavigationRestrictions(self, value: Boolean) -> Void: ...
    ApplicationViewId = property(get_ApplicationViewId, None)
    IgnoreApplicationContentUriRulesNavigationRestrictions = property(get_IgnoreApplicationContentUriRulesNavigationRestrictions, put_IgnoreApplicationContentUriRulesNavigationRestrictions)
    Closed = event()
    Activated = event()
class IWebUIViewStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUIViewStatics'
    _iid_ = Guid('{b591e668-8e59-44f9-8803-1b24c9149d30}')
    @winrt_commethod(6)
    def CreateAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.WebUI.WebUIView]: ...
    @winrt_commethod(7)
    def CreateWithUriAsync(self, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.WebUI.WebUIView]: ...
class LeavingBackgroundEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.ILeavingBackgroundEventArgs
    _classid_ = 'Windows.UI.WebUI.LeavingBackgroundEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.ILeavingBackgroundEventArgs) -> win32more.Windows.Foundation.Deferral: ...
class LeavingBackgroundEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00b4ccd9-7a9c-4b6b-9ac4-13474f268bc4}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.ApplicationModel.ILeavingBackgroundEventArgs) -> Void: ...
class NavigatedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7af46fe6-40ca-4e49-a7d6-dbdb330cd1a3}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.WebUI.IWebUINavigatedEventArgs) -> Void: ...
class NewWebUIViewCreatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.WebUI.INewWebUIViewCreatedEventArgs
    _classid_ = 'Windows.UI.WebUI.NewWebUIViewCreatedEventArgs'
    @winrt_mixinmethod
    def get_WebUIView(self: win32more.Windows.UI.WebUI.INewWebUIViewCreatedEventArgs) -> win32more.Windows.UI.WebUI.WebUIView: ...
    @winrt_mixinmethod
    def get_ActivatedEventArgs(self: win32more.Windows.UI.WebUI.INewWebUIViewCreatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs: ...
    @winrt_mixinmethod
    def get_HasPendingNavigate(self: win32more.Windows.UI.WebUI.INewWebUIViewCreatedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.UI.WebUI.INewWebUIViewCreatedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
    ActivatedEventArgs = property(get_ActivatedEventArgs, None)
    HasPendingNavigate = property(get_HasPendingNavigate, None)
    WebUIView = property(get_WebUIView, None)
class PrintContent(Enum, Int32):
    AllPages = 0
    CurrentPage = 1
    CustomPageRange = 2
    CurrentSelection = 3
class ResumingEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{26599ba9-a22d-4806-a728-acadc1d075fa}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable) -> Void: ...
class SuspendingDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.ISuspendingDeferral
    _classid_ = 'Windows.UI.WebUI.SuspendingDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.ApplicationModel.ISuspendingDeferral) -> Void: ...
class SuspendingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.ISuspendingEventArgs
    _classid_ = 'Windows.UI.WebUI.SuspendingEventArgs'
    @winrt_mixinmethod
    def get_SuspendingOperation(self: win32more.Windows.ApplicationModel.ISuspendingEventArgs) -> win32more.Windows.ApplicationModel.SuspendingOperation: ...
    SuspendingOperation = property(get_SuspendingOperation, None)
class SuspendingEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{509c429c-78e2-4883-abc8-8960dcde1b5c}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.ApplicationModel.ISuspendingEventArgs) -> Void: ...
class SuspendingOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.ISuspendingOperation
    _classid_ = 'Windows.UI.WebUI.SuspendingOperation'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.ISuspendingOperation) -> win32more.Windows.ApplicationModel.SuspendingDeferral: ...
    @winrt_mixinmethod
    def get_Deadline(self: win32more.Windows.ApplicationModel.ISuspendingOperation) -> win32more.Windows.Foundation.DateTime: ...
    Deadline = property(get_Deadline, None)
class WebUIApplication(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.WebUIApplication'
    @winrt_classmethod
    def add_NewWebUIViewCreated(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics4, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.UI.WebUI.NewWebUIViewCreatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_NewWebUIViewCreated(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics4, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_BackgroundActivated(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics4, handler: win32more.Windows.UI.WebUI.BackgroundActivatedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_BackgroundActivated(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics4, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def RequestRestartAsync(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics3, launchArguments: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Core.AppRestartFailureReason]: ...
    @winrt_classmethod
    def RequestRestartForUserAsync(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics3, user: win32more.Windows.System.User, launchArguments: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.Core.AppRestartFailureReason]: ...
    @winrt_classmethod
    def add_LeavingBackground(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics2, handler: win32more.Windows.UI.WebUI.LeavingBackgroundEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_LeavingBackground(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_EnteredBackground(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics2, handler: win32more.Windows.UI.WebUI.EnteredBackgroundEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_EnteredBackground(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def EnablePrelaunch(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics2, value: Boolean) -> Void: ...
    @winrt_classmethod
    def add_Activated(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics, handler: win32more.Windows.UI.WebUI.ActivatedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_Activated(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_Suspending(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics, handler: win32more.Windows.UI.WebUI.SuspendingEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_Suspending(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_Resuming(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics, handler: win32more.Windows.UI.WebUI.ResumingEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_Resuming(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_Navigated(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics, handler: win32more.Windows.UI.WebUI.NavigatedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_Navigated(cls: win32more.Windows.UI.WebUI.IWebUIActivationStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class WebUIAppointmentsProviderAddAppointmentActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderAddAppointmentActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIAppointmentsProviderAddAppointmentActivatedEventArgs'
    @winrt_mixinmethod
    def get_AddAppointmentOperation(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderAddAppointmentActivatedEventArgs) -> win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.AddAppointmentOperation: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    AddAppointmentOperation = property(get_AddAppointmentOperation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
    Verb = property(get_Verb, None)
class WebUIAppointmentsProviderRemoveAppointmentActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderRemoveAppointmentActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIAppointmentsProviderRemoveAppointmentActivatedEventArgs'
    @winrt_mixinmethod
    def get_RemoveAppointmentOperation(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderRemoveAppointmentActivatedEventArgs) -> win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.RemoveAppointmentOperation: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    RemoveAppointmentOperation = property(get_RemoveAppointmentOperation, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
    Verb = property(get_Verb, None)
class WebUIAppointmentsProviderReplaceAppointmentActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderReplaceAppointmentActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIAppointmentsProviderReplaceAppointmentActivatedEventArgs'
    @winrt_mixinmethod
    def get_ReplaceAppointmentOperation(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderReplaceAppointmentActivatedEventArgs) -> win32more.Windows.ApplicationModel.Appointments.AppointmentsProvider.ReplaceAppointmentOperation: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    ReplaceAppointmentOperation = property(get_ReplaceAppointmentOperation, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
    Verb = property(get_Verb, None)
class WebUIAppointmentsProviderShowAppointmentDetailsActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderShowAppointmentDetailsActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIAppointmentsProviderShowAppointmentDetailsActivatedEventArgs'
    @winrt_mixinmethod
    def get_InstanceStartDate(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderShowAppointmentDetailsActivatedEventArgs) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_LocalId(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderShowAppointmentDetailsActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RoamingId(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderShowAppointmentDetailsActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    InstanceStartDate = property(get_InstanceStartDate, None)
    Kind = property(get_Kind, None)
    LocalId = property(get_LocalId, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    RoamingId = property(get_RoamingId, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
    Verb = property(get_Verb, None)
class WebUIAppointmentsProviderShowTimeFrameActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderShowTimeFrameActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIAppointmentsProviderShowTimeFrameActivatedEventArgs'
    @winrt_mixinmethod
    def get_TimeToShow(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderShowTimeFrameActivatedEventArgs) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderShowTimeFrameActivatedEventArgs) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IAppointmentsProviderActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    Duration = property(get_Duration, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    TimeToShow = property(get_TimeToShow, None)
    User = property(get_User, None)
    Verb = property(get_Verb, None)
class _WebUIBackgroundTaskInstance_Meta_(ComPtr.__class__):
    pass
class WebUIBackgroundTaskInstance(ComPtr, metaclass=_WebUIBackgroundTaskInstance_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.WebUIBackgroundTaskInstance'
    @winrt_classmethod
    def get_Current(cls: win32more.Windows.UI.WebUI.IWebUIBackgroundTaskInstanceStatics) -> win32more.Windows.UI.WebUI.IWebUIBackgroundTaskInstance: ...
    _WebUIBackgroundTaskInstance_Meta_.Current = property(get_Current, None)
class WebUIBackgroundTaskInstanceRuntimeClass(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.WebUI.IWebUIBackgroundTaskInstance
    _classid_ = 'Windows.UI.WebUI.WebUIBackgroundTaskInstanceRuntimeClass'
    @winrt_mixinmethod
    def get_Succeeded(self: win32more.Windows.UI.WebUI.IWebUIBackgroundTaskInstance) -> Boolean: ...
    @winrt_mixinmethod
    def put_Succeeded(self: win32more.Windows.UI.WebUI.IWebUIBackgroundTaskInstance, succeeded: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_InstanceId(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance) -> Guid: ...
    @winrt_mixinmethod
    def get_Task(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance) -> win32more.Windows.ApplicationModel.Background.BackgroundTaskRegistration: ...
    @winrt_mixinmethod
    def get_Progress(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance) -> UInt32: ...
    @winrt_mixinmethod
    def put_Progress(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_TriggerDetails(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def add_Canceled(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance, cancelHandler: win32more.Windows.ApplicationModel.Background.BackgroundTaskCanceledEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Canceled(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance, cookie: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_SuspendedCount(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance) -> UInt32: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.ApplicationModel.Background.IBackgroundTaskInstance) -> win32more.Windows.ApplicationModel.Background.BackgroundTaskDeferral: ...
    InstanceId = property(get_InstanceId, None)
    Progress = property(get_Progress, put_Progress)
    Succeeded = property(get_Succeeded, put_Succeeded)
    SuspendedCount = property(get_SuspendedCount, None)
    Task = property(get_Task, None)
    TriggerDetails = property(get_TriggerDetails, None)
    Canceled = event()
class WebUIBarcodeScannerPreviewActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IBarcodeScannerPreviewActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIBarcodeScannerPreviewActivatedEventArgs'
    @winrt_mixinmethod
    def get_ConnectionId(self: win32more.Windows.ApplicationModel.Activation.IBarcodeScannerPreviewActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    ConnectionId = property(get_ConnectionId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class WebUICachedFileUpdaterActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.ICachedFileUpdaterActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUICachedFileUpdaterActivatedEventArgs'
    @winrt_mixinmethod
    def get_CachedFileUpdaterUI(self: win32more.Windows.ApplicationModel.Activation.ICachedFileUpdaterActivatedEventArgs) -> win32more.Windows.Storage.Provider.CachedFileUpdaterUI: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    CachedFileUpdaterUI = property(get_CachedFileUpdaterUI, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class WebUICameraSettingsActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.ICameraSettingsActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUICameraSettingsActivatedEventArgs'
    @winrt_mixinmethod
    def get_VideoDeviceController(self: win32more.Windows.ApplicationModel.Activation.ICameraSettingsActivatedEventArgs) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_VideoDeviceExtension(self: win32more.Windows.ApplicationModel.Activation.ICameraSettingsActivatedEventArgs) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    VideoDeviceController = property(get_VideoDeviceController, None)
    VideoDeviceExtension = property(get_VideoDeviceExtension, None)
class WebUICommandLineActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.ICommandLineActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUICommandLineActivatedEventArgs'
    @winrt_mixinmethod
    def get_Operation(self: win32more.Windows.ApplicationModel.Activation.ICommandLineActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.CommandLineActivationOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    Kind = property(get_Kind, None)
    Operation = property(get_Operation, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class WebUIContactCallActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IContactCallActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIContactCallActivatedEventArgs'
    @winrt_mixinmethod
    def get_ServiceId(self: win32more.Windows.ApplicationModel.Activation.IContactCallActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServiceUserId(self: win32more.Windows.ApplicationModel.Activation.IContactCallActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.ApplicationModel.Activation.IContactCallActivatedEventArgs) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IContactActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    Contact = property(get_Contact, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    ServiceId = property(get_ServiceId, None)
    ServiceUserId = property(get_ServiceUserId, None)
    SplashScreen = property(get_SplashScreen, None)
    Verb = property(get_Verb, None)
class WebUIContactMapActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IContactMapActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIContactMapActivatedEventArgs'
    @winrt_mixinmethod
    def get_Address(self: win32more.Windows.ApplicationModel.Activation.IContactMapActivatedEventArgs) -> win32more.Windows.ApplicationModel.Contacts.ContactAddress: ...
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.ApplicationModel.Activation.IContactMapActivatedEventArgs) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IContactActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    Address = property(get_Address, None)
    Contact = property(get_Contact, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    Verb = property(get_Verb, None)
class WebUIContactMessageActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IContactMessageActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIContactMessageActivatedEventArgs'
    @winrt_mixinmethod
    def get_ServiceId(self: win32more.Windows.ApplicationModel.Activation.IContactMessageActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServiceUserId(self: win32more.Windows.ApplicationModel.Activation.IContactMessageActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.ApplicationModel.Activation.IContactMessageActivatedEventArgs) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IContactActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    Contact = property(get_Contact, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    ServiceId = property(get_ServiceId, None)
    ServiceUserId = property(get_ServiceUserId, None)
    SplashScreen = property(get_SplashScreen, None)
    Verb = property(get_Verb, None)
class WebUIContactPanelActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IContactPanelActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIContactPanelActivatedEventArgs'
    @winrt_mixinmethod
    def get_ContactPanel(self: win32more.Windows.ApplicationModel.Activation.IContactPanelActivatedEventArgs) -> win32more.Windows.ApplicationModel.Contacts.ContactPanel: ...
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.ApplicationModel.Activation.IContactPanelActivatedEventArgs) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    Contact = property(get_Contact, None)
    ContactPanel = property(get_ContactPanel, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class WebUIContactPickerActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IContactPickerActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIContactPickerActivatedEventArgs'
    @winrt_mixinmethod
    def get_ContactPickerUI(self: win32more.Windows.ApplicationModel.Activation.IContactPickerActivatedEventArgs) -> win32more.Windows.ApplicationModel.Contacts.Provider.ContactPickerUI: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    ContactPickerUI = property(get_ContactPickerUI, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
class WebUIContactPostActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IContactPostActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIContactPostActivatedEventArgs'
    @winrt_mixinmethod
    def get_ServiceId(self: win32more.Windows.ApplicationModel.Activation.IContactPostActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServiceUserId(self: win32more.Windows.ApplicationModel.Activation.IContactPostActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.ApplicationModel.Activation.IContactPostActivatedEventArgs) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IContactActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    Contact = property(get_Contact, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    ServiceId = property(get_ServiceId, None)
    ServiceUserId = property(get_ServiceUserId, None)
    SplashScreen = property(get_SplashScreen, None)
    Verb = property(get_Verb, None)
class WebUIContactVideoCallActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IContactVideoCallActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIContactVideoCallActivatedEventArgs'
    @winrt_mixinmethod
    def get_ServiceId(self: win32more.Windows.ApplicationModel.Activation.IContactVideoCallActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServiceUserId(self: win32more.Windows.ApplicationModel.Activation.IContactVideoCallActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Contact(self: win32more.Windows.ApplicationModel.Activation.IContactVideoCallActivatedEventArgs) -> win32more.Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IContactActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    Contact = property(get_Contact, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    ServiceId = property(get_ServiceId, None)
    ServiceUserId = property(get_ServiceUserId, None)
    SplashScreen = property(get_SplashScreen, None)
    Verb = property(get_Verb, None)
class WebUIDeviceActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IDeviceActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIDeviceActivatedEventArgs'
    @winrt_mixinmethod
    def get_DeviceInformationId(self: win32more.Windows.ApplicationModel.Activation.IDeviceActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IDeviceActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: win32more.Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    DeviceInformationId = property(get_DeviceInformationId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
    Verb = property(get_Verb, None)
class WebUIDevicePairingActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IDevicePairingActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIDevicePairingActivatedEventArgs'
    @winrt_mixinmethod
    def get_DeviceInformation(self: win32more.Windows.ApplicationModel.Activation.IDevicePairingActivatedEventArgs) -> win32more.Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    DeviceInformation = property(get_DeviceInformation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class WebUIDialReceiverActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IDialReceiverActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIDialReceiverActivatedEventArgs'
    @winrt_mixinmethod
    def get_AppName(self: win32more.Windows.ApplicationModel.Activation.IDialReceiverActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Arguments(self: win32more.Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TileId(self: win32more.Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: win32more.Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    AppName = property(get_AppName, None)
    Arguments = property(get_Arguments, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    TileId = property(get_TileId, None)
    User = property(get_User, None)
class WebUIFileActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IFileActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIFileActivatedEventArgs'
    @winrt_mixinmethod
    def get_Files(self: win32more.Windows.ApplicationModel.Activation.IFileActivatedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.IStorageItem]: ...
    @winrt_mixinmethod
    def get_Verb(self: win32more.Windows.ApplicationModel.Activation.IFileActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: win32more.Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_NeighboringFilesQuery(self: win32more.Windows.ApplicationModel.Activation.IFileActivatedEventArgsWithNeighboringFiles) -> win32more.Windows.Storage.Search.StorageFileQueryResult: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    Files = property(get_Files, None)
    Kind = property(get_Kind, None)
    NeighboringFilesQuery = property(get_NeighboringFilesQuery, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
    Verb = property(get_Verb, None)
class WebUIFileOpenPickerActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IFileOpenPickerActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIFileOpenPickerActivatedEventArgs'
    @winrt_mixinmethod
    def get_FileOpenPickerUI(self: win32more.Windows.ApplicationModel.Activation.IFileOpenPickerActivatedEventArgs) -> win32more.Windows.Storage.Pickers.Provider.FileOpenPickerUI: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CallerPackageFamilyName(self: win32more.Windows.ApplicationModel.Activation.IFileOpenPickerActivatedEventArgs2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    FileOpenPickerUI = property(get_FileOpenPickerUI, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class WebUIFileOpenPickerContinuationEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IFileOpenPickerContinuationEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIFileOpenPickerContinuationEventArgs'
    @winrt_mixinmethod
    def get_Files(self: win32more.Windows.ApplicationModel.Activation.IFileOpenPickerContinuationEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def get_ContinuationData(self: win32more.Windows.ApplicationModel.Activation.IContinuationActivatedEventArgs) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    ContinuationData = property(get_ContinuationData, None)
    Files = property(get_Files, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class WebUIFileSavePickerActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IFileSavePickerActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIFileSavePickerActivatedEventArgs'
    @winrt_mixinmethod
    def get_FileSavePickerUI(self: win32more.Windows.ApplicationModel.Activation.IFileSavePickerActivatedEventArgs) -> win32more.Windows.Storage.Pickers.Provider.FileSavePickerUI: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CallerPackageFamilyName(self: win32more.Windows.ApplicationModel.Activation.IFileSavePickerActivatedEventArgs2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EnterpriseId(self: win32more.Windows.ApplicationModel.Activation.IFileSavePickerActivatedEventArgs2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    EnterpriseId = property(get_EnterpriseId, None)
    FileSavePickerUI = property(get_FileSavePickerUI, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class WebUIFileSavePickerContinuationEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IFileSavePickerContinuationEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIFileSavePickerContinuationEventArgs'
    @winrt_mixinmethod
    def get_File(self: win32more.Windows.ApplicationModel.Activation.IFileSavePickerContinuationEventArgs) -> win32more.Windows.Storage.StorageFile: ...
    @winrt_mixinmethod
    def get_ContinuationData(self: win32more.Windows.ApplicationModel.Activation.IContinuationActivatedEventArgs) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    ContinuationData = property(get_ContinuationData, None)
    File = property(get_File, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class WebUIFolderPickerContinuationEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IFolderPickerContinuationEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIFolderPickerContinuationEventArgs'
    @winrt_mixinmethod
    def get_Folder(self: win32more.Windows.ApplicationModel.Activation.IFolderPickerContinuationEventArgs) -> win32more.Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def get_ContinuationData(self: win32more.Windows.ApplicationModel.Activation.IContinuationActivatedEventArgs) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    ContinuationData = property(get_ContinuationData, None)
    Folder = property(get_Folder, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class WebUILaunchActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUILaunchActivatedEventArgs'
    @winrt_mixinmethod
    def get_Arguments(self: win32more.Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TileId(self: win32more.Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_PrelaunchActivated(self: win32more.Windows.ApplicationModel.Activation.IPrelaunchActivatedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: win32more.Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def get_TileActivatedInfo(self: win32more.Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs2) -> win32more.Windows.ApplicationModel.Activation.TileActivatedInfo: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    Arguments = property(get_Arguments, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    Kind = property(get_Kind, None)
    PrelaunchActivated = property(get_PrelaunchActivated, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    TileActivatedInfo = property(get_TileActivatedInfo, None)
    TileId = property(get_TileId, None)
    User = property(get_User, None)
class WebUILockScreenActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.ILockScreenActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUILockScreenActivatedEventArgs'
    @winrt_mixinmethod
    def get_Info(self: win32more.Windows.ApplicationModel.Activation.ILockScreenActivatedEventArgs) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: win32more.Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    Info = property(get_Info, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class WebUILockScreenCallActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.ILockScreenCallActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUILockScreenCallActivatedEventArgs'
    @winrt_mixinmethod
    def get_CallUI(self: win32more.Windows.ApplicationModel.Activation.ILockScreenCallActivatedEventArgs) -> win32more.Windows.ApplicationModel.Calls.LockScreenCallUI: ...
    @winrt_mixinmethod
    def get_Arguments(self: win32more.Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TileId(self: win32more.Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: win32more.Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    Arguments = property(get_Arguments, None)
    CallUI = property(get_CallUI, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    TileId = property(get_TileId, None)
class WebUILockScreenComponentActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUILockScreenComponentActivatedEventArgs'
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
class WebUINavigatedDeferral(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.WebUI.IWebUINavigatedDeferral
    _classid_ = 'Windows.UI.WebUI.WebUINavigatedDeferral'
    @winrt_mixinmethod
    def Complete(self: win32more.Windows.UI.WebUI.IWebUINavigatedDeferral) -> Void: ...
class WebUINavigatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.WebUI.IWebUINavigatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUINavigatedEventArgs'
    @winrt_mixinmethod
    def get_NavigatedOperation(self: win32more.Windows.UI.WebUI.IWebUINavigatedEventArgs) -> win32more.Windows.UI.WebUI.WebUINavigatedOperation: ...
    NavigatedOperation = property(get_NavigatedOperation, None)
class WebUINavigatedOperation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.WebUI.IWebUINavigatedOperation
    _classid_ = 'Windows.UI.WebUI.WebUINavigatedOperation'
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.UI.WebUI.IWebUINavigatedOperation) -> win32more.Windows.UI.WebUI.WebUINavigatedDeferral: ...
class WebUIPhoneCallActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IPhoneCallActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIPhoneCallActivatedEventArgs'
    @winrt_mixinmethod
    def get_LineId(self: win32more.Windows.ApplicationModel.Activation.IPhoneCallActivatedEventArgs) -> Guid: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    Kind = property(get_Kind, None)
    LineId = property(get_LineId, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class WebUIPrint3DWorkflowActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IPrint3DWorkflowActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIPrint3DWorkflowActivatedEventArgs'
    @winrt_mixinmethod
    def get_Workflow(self: win32more.Windows.ApplicationModel.Activation.IPrint3DWorkflowActivatedEventArgs) -> win32more.Windows.Devices.Printers.Extensions.Print3DWorkflow: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    Workflow = property(get_Workflow, None)
class WebUIPrintTaskSettingsActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IPrintTaskSettingsActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIPrintTaskSettingsActivatedEventArgs'
    @winrt_mixinmethod
    def get_Configuration(self: win32more.Windows.ApplicationModel.Activation.IPrintTaskSettingsActivatedEventArgs) -> win32more.Windows.Devices.Printers.Extensions.PrintTaskConfiguration: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    Configuration = property(get_Configuration, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
class WebUIPrintWorkflowForegroundTaskActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIPrintWorkflowForegroundTaskActivatedEventArgs'
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
class WebUIProtocolActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IProtocolActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIProtocolActivatedEventArgs'
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.ApplicationModel.Activation.IProtocolActivatedEventArgs) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CallerPackageFamilyName(self: win32more.Windows.ApplicationModel.Activation.IProtocolActivatedEventArgsWithCallerPackageFamilyNameAndData) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Windows.ApplicationModel.Activation.IProtocolActivatedEventArgsWithCallerPackageFamilyNameAndData) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: win32more.Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    Data = property(get_Data, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    Uri = property(get_Uri, None)
    User = property(get_User, None)
class WebUIProtocolForResultsActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IProtocolForResultsActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIProtocolForResultsActivatedEventArgs'
    @winrt_mixinmethod
    def get_ProtocolForResultsOperation(self: win32more.Windows.ApplicationModel.Activation.IProtocolForResultsActivatedEventArgs) -> win32more.Windows.System.ProtocolForResultsOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_Uri(self: win32more.Windows.ApplicationModel.Activation.IProtocolActivatedEventArgs) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_CallerPackageFamilyName(self: win32more.Windows.ApplicationModel.Activation.IProtocolActivatedEventArgsWithCallerPackageFamilyNameAndData) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Windows.ApplicationModel.Activation.IProtocolActivatedEventArgsWithCallerPackageFamilyNameAndData) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: win32more.Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    Data = property(get_Data, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    ProtocolForResultsOperation = property(get_ProtocolForResultsOperation, None)
    SplashScreen = property(get_SplashScreen, None)
    Uri = property(get_Uri, None)
    User = property(get_User, None)
class WebUIRestrictedLaunchActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IRestrictedLaunchActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIRestrictedLaunchActivatedEventArgs'
    @winrt_mixinmethod
    def get_SharedContext(self: win32more.Windows.ApplicationModel.Activation.IRestrictedLaunchActivatedEventArgs) -> win32more.Windows.Win32.System.WinRT.IInspectable: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SharedContext = property(get_SharedContext, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class WebUISearchActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.ISearchActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUISearchActivatedEventArgs'
    @winrt_mixinmethod
    def get_QueryText(self: win32more.Windows.ApplicationModel.Activation.ISearchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Language(self: win32more.Windows.ApplicationModel.Activation.ISearchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_LinguisticDetails(self: win32more.Windows.ApplicationModel.Activation.ISearchActivatedEventArgsWithLinguisticDetails) -> win32more.Windows.ApplicationModel.Search.SearchPaneQueryLinguisticDetails: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: win32more.Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    Kind = property(get_Kind, None)
    Language = property(get_Language, None)
    LinguisticDetails = property(get_LinguisticDetails, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    QueryText = property(get_QueryText, None)
    SplashScreen = property(get_SplashScreen, None)
class WebUIShareTargetActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IShareTargetActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIShareTargetActivatedEventArgs'
    @winrt_mixinmethod
    def get_ShareOperation(self: win32more.Windows.ApplicationModel.Activation.IShareTargetActivatedEventArgs) -> win32more.Windows.ApplicationModel.DataTransfer.ShareTarget.ShareOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    ShareOperation = property(get_ShareOperation, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class WebUIStartupTaskActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IStartupTaskActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIStartupTaskActivatedEventArgs'
    @winrt_mixinmethod
    def get_TaskId(self: win32more.Windows.ApplicationModel.Activation.IStartupTaskActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    TaskId = property(get_TaskId, None)
    User = property(get_User, None)
class WebUIToastNotificationActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IToastNotificationActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIToastNotificationActivatedEventArgs'
    @winrt_mixinmethod
    def get_Argument(self: win32more.Windows.ApplicationModel.Activation.IToastNotificationActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_UserInput(self: win32more.Windows.ApplicationModel.Activation.IToastNotificationActivatedEventArgs) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    Argument = property(get_Argument, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
    UserInput = property(get_UserInput, None)
class WebUIUserDataAccountProviderActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IUserDataAccountProviderActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIUserDataAccountProviderActivatedEventArgs'
    @winrt_mixinmethod
    def get_Operation(self: win32more.Windows.ApplicationModel.Activation.IUserDataAccountProviderActivatedEventArgs) -> win32more.Windows.ApplicationModel.UserDataAccounts.Provider.IUserDataAccountProviderOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    Kind = property(get_Kind, None)
    Operation = property(get_Operation, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
class WebUIView(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.WebUI.IWebUIView
    _classid_ = 'Windows.UI.WebUI.WebUIView'
    @winrt_mixinmethod
    def get_ApplicationViewId(self: win32more.Windows.UI.WebUI.IWebUIView) -> Int32: ...
    @winrt_mixinmethod
    def add_Closed(self: win32more.Windows.UI.WebUI.IWebUIView, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.WebUI.WebUIView, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: win32more.Windows.UI.WebUI.IWebUIView, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Activated(self: win32more.Windows.UI.WebUI.IWebUIView, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.WebUI.WebUIView, win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Activated(self: win32more.Windows.UI.WebUI.IWebUIView, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_IgnoreApplicationContentUriRulesNavigationRestrictions(self: win32more.Windows.UI.WebUI.IWebUIView) -> Boolean: ...
    @winrt_mixinmethod
    def put_IgnoreApplicationContentUriRulesNavigationRestrictions(self: win32more.Windows.UI.WebUI.IWebUIView, value: Boolean) -> Void: ...
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
    def AddInitializeScript(self: win32more.Windows.Web.UI.IWebViewControl2, script: WinRT_String) -> Void: ...
    @winrt_classmethod
    def CreateAsync(cls: win32more.Windows.UI.WebUI.IWebUIViewStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.WebUI.WebUIView]: ...
    @winrt_classmethod
    def CreateWithUriAsync(cls: win32more.Windows.UI.WebUI.IWebUIViewStatics, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.UI.WebUI.WebUIView]: ...
    ApplicationViewId = property(get_ApplicationViewId, None)
    CanGoBack = property(get_CanGoBack, None)
    CanGoForward = property(get_CanGoForward, None)
    ContainsFullScreenElement = property(get_ContainsFullScreenElement, None)
    DefaultBackgroundColor = property(get_DefaultBackgroundColor, put_DefaultBackgroundColor)
    DeferredPermissionRequests = property(get_DeferredPermissionRequests, None)
    DocumentTitle = property(get_DocumentTitle, None)
    IgnoreApplicationContentUriRulesNavigationRestrictions = property(get_IgnoreApplicationContentUriRulesNavigationRestrictions, put_IgnoreApplicationContentUriRulesNavigationRestrictions)
    Settings = property(get_Settings, None)
    Source = property(get_Source, put_Source)
    Closed = event()
    Activated = event()
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
class WebUIVoiceCommandActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IVoiceCommandActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIVoiceCommandActivatedEventArgs'
    @winrt_mixinmethod
    def get_Result(self: win32more.Windows.ApplicationModel.Activation.IVoiceCommandActivatedEventArgs) -> win32more.Windows.Media.SpeechRecognition.SpeechRecognitionResult: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    Result = property(get_Result, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class WebUIWalletActionActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IWalletActionActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIWalletActionActivatedEventArgs'
    @winrt_mixinmethod
    def get_ItemId(self: win32more.Windows.ApplicationModel.Activation.IWalletActionActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ActionKind(self: win32more.Windows.ApplicationModel.Activation.IWalletActionActivatedEventArgs) -> win32more.Windows.ApplicationModel.Wallet.WalletActionKind: ...
    @winrt_mixinmethod
    def get_ActionId(self: win32more.Windows.ApplicationModel.Activation.IWalletActionActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    ActionId = property(get_ActionId, None)
    ActionKind = property(get_ActionKind, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    ItemId = property(get_ItemId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
class WebUIWebAccountProviderActivatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IWebAccountProviderActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIWebAccountProviderActivatedEventArgs'
    @winrt_mixinmethod
    def get_Operation(self: win32more.Windows.ApplicationModel.Activation.IWebAccountProviderActivatedEventArgs) -> win32more.Windows.Security.Authentication.Web.Provider.IWebAccountProviderOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> win32more.Windows.System.User: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    Kind = property(get_Kind, None)
    Operation = property(get_Operation, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
class WebUIWebAuthenticationBrokerContinuationEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.Activation.IWebAuthenticationBrokerContinuationEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIWebAuthenticationBrokerContinuationEventArgs'
    @winrt_mixinmethod
    def get_WebAuthenticationResult(self: win32more.Windows.ApplicationModel.Activation.IWebAuthenticationBrokerContinuationEventArgs) -> win32more.Windows.Security.Authentication.Web.WebAuthenticationResult: ...
    @winrt_mixinmethod
    def get_ContinuationData(self: win32more.Windows.ApplicationModel.Activation.IContinuationActivatedEventArgs) -> win32more.Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: win32more.Windows.ApplicationModel.Activation.IActivatedEventArgs) -> win32more.Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: win32more.Windows.UI.WebUI.IActivatedEventArgsDeferral) -> win32more.Windows.UI.WebUI.ActivatedOperation: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
    ContinuationData = property(get_ContinuationData, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    WebAuthenticationResult = property(get_WebAuthenticationResult, None)


make_ready(__name__)
