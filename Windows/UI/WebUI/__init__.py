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
import Windows.ApplicationModel
import Windows.ApplicationModel.Activation
import Windows.ApplicationModel.Appointments.AppointmentsProvider
import Windows.ApplicationModel.Background
import Windows.ApplicationModel.Calls
import Windows.ApplicationModel.Contacts
import Windows.ApplicationModel.Contacts.Provider
import Windows.ApplicationModel.Core
import Windows.ApplicationModel.DataTransfer
import Windows.ApplicationModel.DataTransfer.ShareTarget
import Windows.ApplicationModel.Search
import Windows.ApplicationModel.UserDataAccounts.Provider
import Windows.ApplicationModel.Wallet
import Windows.Devices.Enumeration
import Windows.Devices.Printers.Extensions
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Graphics.Printing
import Windows.Media.SpeechRecognition
import Windows.Security.Authentication.Web
import Windows.Security.Authentication.Web.Provider
import Windows.Storage
import Windows.Storage.Pickers.Provider
import Windows.Storage.Provider
import Windows.Storage.Search
import Windows.Storage.Streams
import Windows.System
import Windows.UI
import Windows.UI.WebUI
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
class ActivatedDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.WebUI.IActivatedDeferral
    _classid_ = 'Windows.UI.WebUI.ActivatedDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.UI.WebUI.IActivatedDeferral) -> Void: ...
class ActivatedEventHandler(ComPtr):
    # System.MulticastDelegate
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.WebUI.ActivatedEventHandler'
    _iid_ = Guid('{50f1e730-c5d1-4b6b-9adb-8a11756be29c}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, eventArgs: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Void: ...
class ActivatedOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.WebUI.IActivatedOperation
    _classid_ = 'Windows.UI.WebUI.ActivatedOperation'
    @winrt_mixinmethod
    def GetDeferral(self: Windows.UI.WebUI.IActivatedOperation) -> Windows.UI.WebUI.ActivatedDeferral: ...
class BackgroundActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IBackgroundActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.BackgroundActivatedEventArgs'
    @winrt_mixinmethod
    def get_TaskInstance(self: Windows.ApplicationModel.Activation.IBackgroundActivatedEventArgs) -> Windows.ApplicationModel.Background.IBackgroundTaskInstance: ...
    TaskInstance = property(get_TaskInstance, None)
class BackgroundActivatedEventHandler(ComPtr):
    # System.MulticastDelegate
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.WebUI.BackgroundActivatedEventHandler'
    _iid_ = Guid('{edb19fbb-0761-47cc-9a77-24d7072965ca}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, eventArgs: Windows.ApplicationModel.Activation.IBackgroundActivatedEventArgs) -> Void: ...
class EnteredBackgroundEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.IEnteredBackgroundEventArgs
    _classid_ = 'Windows.UI.WebUI.EnteredBackgroundEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.IEnteredBackgroundEventArgs) -> Windows.Foundation.Deferral: ...
class EnteredBackgroundEventHandler(ComPtr):
    # System.MulticastDelegate
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.WebUI.EnteredBackgroundEventHandler'
    _iid_ = Guid('{2b09a173-b68e-4def-88c1-8de84e5aab2f}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.ApplicationModel.IEnteredBackgroundEventArgs) -> Void: ...
class HtmlPrintDocumentSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.WebUI.IHtmlPrintDocumentSource
    _classid_ = 'Windows.UI.WebUI.HtmlPrintDocumentSource'
    @winrt_mixinmethod
    def get_Content(self: Windows.UI.WebUI.IHtmlPrintDocumentSource) -> Windows.UI.WebUI.PrintContent: ...
    @winrt_mixinmethod
    def put_Content(self: Windows.UI.WebUI.IHtmlPrintDocumentSource, value: Windows.UI.WebUI.PrintContent) -> Void: ...
    @winrt_mixinmethod
    def get_LeftMargin(self: Windows.UI.WebUI.IHtmlPrintDocumentSource) -> Single: ...
    @winrt_mixinmethod
    def put_LeftMargin(self: Windows.UI.WebUI.IHtmlPrintDocumentSource, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_TopMargin(self: Windows.UI.WebUI.IHtmlPrintDocumentSource) -> Single: ...
    @winrt_mixinmethod
    def put_TopMargin(self: Windows.UI.WebUI.IHtmlPrintDocumentSource, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_RightMargin(self: Windows.UI.WebUI.IHtmlPrintDocumentSource) -> Single: ...
    @winrt_mixinmethod
    def put_RightMargin(self: Windows.UI.WebUI.IHtmlPrintDocumentSource, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_BottomMargin(self: Windows.UI.WebUI.IHtmlPrintDocumentSource) -> Single: ...
    @winrt_mixinmethod
    def put_BottomMargin(self: Windows.UI.WebUI.IHtmlPrintDocumentSource, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_EnableHeaderFooter(self: Windows.UI.WebUI.IHtmlPrintDocumentSource) -> Boolean: ...
    @winrt_mixinmethod
    def put_EnableHeaderFooter(self: Windows.UI.WebUI.IHtmlPrintDocumentSource, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ShrinkToFit(self: Windows.UI.WebUI.IHtmlPrintDocumentSource) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShrinkToFit(self: Windows.UI.WebUI.IHtmlPrintDocumentSource, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PercentScale(self: Windows.UI.WebUI.IHtmlPrintDocumentSource) -> Single: ...
    @winrt_mixinmethod
    def put_PercentScale(self: Windows.UI.WebUI.IHtmlPrintDocumentSource, scalePercent: Single) -> Void: ...
    @winrt_mixinmethod
    def get_PageRange(self: Windows.UI.WebUI.IHtmlPrintDocumentSource) -> WinRT_String: ...
    @winrt_mixinmethod
    def TrySetPageRange(self: Windows.UI.WebUI.IHtmlPrintDocumentSource, strPageRange: WinRT_String) -> Boolean: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    Content = property(get_Content, put_Content)
    LeftMargin = property(get_LeftMargin, put_LeftMargin)
    TopMargin = property(get_TopMargin, put_TopMargin)
    RightMargin = property(get_RightMargin, put_RightMargin)
    BottomMargin = property(get_BottomMargin, put_BottomMargin)
    EnableHeaderFooter = property(get_EnableHeaderFooter, put_EnableHeaderFooter)
    ShrinkToFit = property(get_ShrinkToFit, put_ShrinkToFit)
    PercentScale = property(get_PercentScale, put_PercentScale)
    PageRange = property(get_PageRange, None)
class IActivatedDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IActivatedDeferral'
    _iid_ = Guid('{c3bd1978-a431-49d8-a76a-395a4e03dcf3}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IActivatedEventArgsDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IActivatedEventArgsDeferral'
    _iid_ = Guid('{ca6d5f74-63c2-44a6-b97b-d9a03c20bc9b}')
    @winrt_commethod(6)
    def get_ActivatedOperation(self) -> Windows.UI.WebUI.ActivatedOperation: ...
    ActivatedOperation = property(get_ActivatedOperation, None)
class IActivatedOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IActivatedOperation'
    _iid_ = Guid('{b6a0b4bc-c6ca-42fd-9818-71904e45fed7}')
    @winrt_commethod(6)
    def GetDeferral(self) -> Windows.UI.WebUI.ActivatedDeferral: ...
class IHtmlPrintDocumentSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IHtmlPrintDocumentSource'
    _iid_ = Guid('{cea6469a-0e05-467a-abc9-36ec1d4cdcb6}')
    @winrt_commethod(6)
    def get_Content(self) -> Windows.UI.WebUI.PrintContent: ...
    @winrt_commethod(7)
    def put_Content(self, value: Windows.UI.WebUI.PrintContent) -> Void: ...
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
    Content = property(get_Content, put_Content)
    LeftMargin = property(get_LeftMargin, put_LeftMargin)
    TopMargin = property(get_TopMargin, put_TopMargin)
    RightMargin = property(get_RightMargin, put_RightMargin)
    BottomMargin = property(get_BottomMargin, put_BottomMargin)
    EnableHeaderFooter = property(get_EnableHeaderFooter, put_EnableHeaderFooter)
    ShrinkToFit = property(get_ShrinkToFit, put_ShrinkToFit)
    PercentScale = property(get_PercentScale, put_PercentScale)
    PageRange = property(get_PageRange, None)
class INewWebUIViewCreatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.INewWebUIViewCreatedEventArgs'
    _iid_ = Guid('{e8e1b216-be2b-4c9e-85e7-083143ec4be7}')
    @winrt_commethod(6)
    def get_WebUIView(self) -> Windows.UI.WebUI.WebUIView: ...
    @winrt_commethod(7)
    def get_ActivatedEventArgs(self) -> Windows.ApplicationModel.Activation.IActivatedEventArgs: ...
    @winrt_commethod(8)
    def get_HasPendingNavigate(self) -> Boolean: ...
    @winrt_commethod(9)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
    WebUIView = property(get_WebUIView, None)
    ActivatedEventArgs = property(get_ActivatedEventArgs, None)
    HasPendingNavigate = property(get_HasPendingNavigate, None)
class IWebUIActivationStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUIActivationStatics'
    _iid_ = Guid('{351b86bd-43b3-482b-85db-35d87b517ad9}')
    @winrt_commethod(6)
    def add_Activated(self, handler: Windows.UI.WebUI.ActivatedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Activated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_Suspending(self, handler: Windows.UI.WebUI.SuspendingEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Suspending(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Resuming(self, handler: Windows.UI.WebUI.ResumingEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Resuming(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_Navigated(self, handler: Windows.UI.WebUI.NavigatedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_Navigated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IWebUIActivationStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUIActivationStatics2'
    _iid_ = Guid('{c8e88696-4d78-4aa4-8f06-2a9eadc6c40a}')
    @winrt_commethod(6)
    def add_LeavingBackground(self, handler: Windows.UI.WebUI.LeavingBackgroundEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_LeavingBackground(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_EnteredBackground(self, handler: Windows.UI.WebUI.EnteredBackgroundEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_EnteredBackground(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def EnablePrelaunch(self, value: Boolean) -> Void: ...
class IWebUIActivationStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUIActivationStatics3'
    _iid_ = Guid('{91abb686-1af5-4445-b49f-9459f40fc8de}')
    @winrt_commethod(6)
    def RequestRestartAsync(self, launchArguments: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Core.AppRestartFailureReason]: ...
    @winrt_commethod(7)
    def RequestRestartForUserAsync(self, user: Windows.System.User, launchArguments: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Core.AppRestartFailureReason]: ...
class IWebUIActivationStatics4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUIActivationStatics4'
    _iid_ = Guid('{5e391429-183f-478d-8a25-67f80d03935b}')
    @winrt_commethod(6)
    def add_NewWebUIViewCreated(self, handler: Windows.Foundation.EventHandler[Windows.UI.WebUI.NewWebUIViewCreatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_NewWebUIViewCreated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_BackgroundActivated(self, handler: Windows.UI.WebUI.BackgroundActivatedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_BackgroundActivated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IWebUIBackgroundTaskInstance(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUIBackgroundTaskInstance'
    _iid_ = Guid('{23f12c25-e2f7-4741-bc9c-394595de24dc}')
    @winrt_commethod(6)
    def get_Succeeded(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Succeeded(self, succeeded: Boolean) -> Void: ...
    Succeeded = property(get_Succeeded, put_Succeeded)
class IWebUIBackgroundTaskInstanceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUIBackgroundTaskInstanceStatics'
    _iid_ = Guid('{9c7a5291-19ae-4ca3-b94b-fe4ec744a740}')
    @winrt_commethod(6)
    def get_Current(self) -> Windows.UI.WebUI.IWebUIBackgroundTaskInstance: ...
    Current = property(get_Current, None)
class IWebUINavigatedDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUINavigatedDeferral'
    _iid_ = Guid('{d804204d-831f-46e2-b432-3afce211f962}')
    @winrt_commethod(6)
    def Complete(self) -> Void: ...
class IWebUINavigatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUINavigatedEventArgs'
    _iid_ = Guid('{a75841b8-2499-4030-a69d-15d2d9cfe524}')
    @winrt_commethod(6)
    def get_NavigatedOperation(self) -> Windows.UI.WebUI.WebUINavigatedOperation: ...
    NavigatedOperation = property(get_NavigatedOperation, None)
class IWebUINavigatedOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUINavigatedOperation'
    _iid_ = Guid('{7a965f08-8182-4a89-ab67-8492e8750d4b}')
    @winrt_commethod(6)
    def GetDeferral(self) -> Windows.UI.WebUI.WebUINavigatedDeferral: ...
class IWebUIView(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUIView'
    _iid_ = Guid('{6783f64f-52da-4fd7-be69-8ef6284b423c}')
    @winrt_commethod(6)
    def get_ApplicationViewId(self) -> Int32: ...
    @winrt_commethod(7)
    def add_Closed(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.WebUI.WebUIView, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_Closed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_Activated(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.WebUI.WebUIView, Windows.ApplicationModel.Activation.IActivatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Activated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def get_IgnoreApplicationContentUriRulesNavigationRestrictions(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_IgnoreApplicationContentUriRulesNavigationRestrictions(self, value: Boolean) -> Void: ...
    ApplicationViewId = property(get_ApplicationViewId, None)
    IgnoreApplicationContentUriRulesNavigationRestrictions = property(get_IgnoreApplicationContentUriRulesNavigationRestrictions, put_IgnoreApplicationContentUriRulesNavigationRestrictions)
class IWebUIViewStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.IWebUIViewStatics'
    _iid_ = Guid('{b591e668-8e59-44f9-8803-1b24c9149d30}')
    @winrt_commethod(6)
    def CreateAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.UI.WebUI.WebUIView]: ...
    @winrt_commethod(7)
    def CreateWithUriAsync(self, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperation[Windows.UI.WebUI.WebUIView]: ...
class LeavingBackgroundEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.ILeavingBackgroundEventArgs
    _classid_ = 'Windows.UI.WebUI.LeavingBackgroundEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.ILeavingBackgroundEventArgs) -> Windows.Foundation.Deferral: ...
class LeavingBackgroundEventHandler(ComPtr):
    # System.MulticastDelegate
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.WebUI.LeavingBackgroundEventHandler'
    _iid_ = Guid('{00b4ccd9-7a9c-4b6b-9ac4-13474f268bc4}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.ApplicationModel.ILeavingBackgroundEventArgs) -> Void: ...
class NavigatedEventHandler(ComPtr):
    # System.MulticastDelegate
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.WebUI.NavigatedEventHandler'
    _iid_ = Guid('{7af46fe6-40ca-4e49-a7d6-dbdb330cd1a3}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.WebUI.IWebUINavigatedEventArgs) -> Void: ...
class NewWebUIViewCreatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.WebUI.INewWebUIViewCreatedEventArgs
    _classid_ = 'Windows.UI.WebUI.NewWebUIViewCreatedEventArgs'
    @winrt_mixinmethod
    def get_WebUIView(self: Windows.UI.WebUI.INewWebUIViewCreatedEventArgs) -> Windows.UI.WebUI.WebUIView: ...
    @winrt_mixinmethod
    def get_ActivatedEventArgs(self: Windows.UI.WebUI.INewWebUIViewCreatedEventArgs) -> Windows.ApplicationModel.Activation.IActivatedEventArgs: ...
    @winrt_mixinmethod
    def get_HasPendingNavigate(self: Windows.UI.WebUI.INewWebUIViewCreatedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.UI.WebUI.INewWebUIViewCreatedEventArgs) -> Windows.Foundation.Deferral: ...
    WebUIView = property(get_WebUIView, None)
    ActivatedEventArgs = property(get_ActivatedEventArgs, None)
    HasPendingNavigate = property(get_HasPendingNavigate, None)
PrintContent = Int32
PrintContent_AllPages: PrintContent = 0
PrintContent_CurrentPage: PrintContent = 1
PrintContent_CustomPageRange: PrintContent = 2
PrintContent_CurrentSelection: PrintContent = 3
class ResumingEventHandler(ComPtr):
    # System.MulticastDelegate
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.WebUI.ResumingEventHandler'
    _iid_ = Guid('{26599ba9-a22d-4806-a728-acadc1d075fa}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head) -> Void: ...
class SuspendingDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.ISuspendingDeferral
    _classid_ = 'Windows.UI.WebUI.SuspendingDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.ApplicationModel.ISuspendingDeferral) -> Void: ...
class SuspendingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.ISuspendingEventArgs
    _classid_ = 'Windows.UI.WebUI.SuspendingEventArgs'
    @winrt_mixinmethod
    def get_SuspendingOperation(self: Windows.ApplicationModel.ISuspendingEventArgs) -> Windows.ApplicationModel.SuspendingOperation: ...
    SuspendingOperation = property(get_SuspendingOperation, None)
class SuspendingEventHandler(ComPtr):
    # System.MulticastDelegate
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.WebUI.SuspendingEventHandler'
    _iid_ = Guid('{509c429c-78e2-4883-abc8-8960dcde1b5c}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.ApplicationModel.ISuspendingEventArgs) -> Void: ...
class SuspendingOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.ISuspendingOperation
    _classid_ = 'Windows.UI.WebUI.SuspendingOperation'
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.ISuspendingOperation) -> Windows.ApplicationModel.SuspendingDeferral: ...
    @winrt_mixinmethod
    def get_Deadline(self: Windows.ApplicationModel.ISuspendingOperation) -> Windows.Foundation.DateTime: ...
    Deadline = property(get_Deadline, None)
class WebUIApplication(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.WebUIApplication'
    @winrt_classmethod
    def add_NewWebUIViewCreated(cls: Windows.UI.WebUI.IWebUIActivationStatics4, handler: Windows.Foundation.EventHandler[Windows.UI.WebUI.NewWebUIViewCreatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_NewWebUIViewCreated(cls: Windows.UI.WebUI.IWebUIActivationStatics4, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_BackgroundActivated(cls: Windows.UI.WebUI.IWebUIActivationStatics4, handler: Windows.UI.WebUI.BackgroundActivatedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_BackgroundActivated(cls: Windows.UI.WebUI.IWebUIActivationStatics4, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def RequestRestartAsync(cls: Windows.UI.WebUI.IWebUIActivationStatics3, launchArguments: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Core.AppRestartFailureReason]: ...
    @winrt_classmethod
    def RequestRestartForUserAsync(cls: Windows.UI.WebUI.IWebUIActivationStatics3, user: Windows.System.User, launchArguments: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Core.AppRestartFailureReason]: ...
    @winrt_classmethod
    def add_LeavingBackground(cls: Windows.UI.WebUI.IWebUIActivationStatics2, handler: Windows.UI.WebUI.LeavingBackgroundEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_LeavingBackground(cls: Windows.UI.WebUI.IWebUIActivationStatics2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_EnteredBackground(cls: Windows.UI.WebUI.IWebUIActivationStatics2, handler: Windows.UI.WebUI.EnteredBackgroundEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_EnteredBackground(cls: Windows.UI.WebUI.IWebUIActivationStatics2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def EnablePrelaunch(cls: Windows.UI.WebUI.IWebUIActivationStatics2, value: Boolean) -> Void: ...
    @winrt_classmethod
    def add_Activated(cls: Windows.UI.WebUI.IWebUIActivationStatics, handler: Windows.UI.WebUI.ActivatedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_Activated(cls: Windows.UI.WebUI.IWebUIActivationStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_Suspending(cls: Windows.UI.WebUI.IWebUIActivationStatics, handler: Windows.UI.WebUI.SuspendingEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_Suspending(cls: Windows.UI.WebUI.IWebUIActivationStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_Resuming(cls: Windows.UI.WebUI.IWebUIActivationStatics, handler: Windows.UI.WebUI.ResumingEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_Resuming(cls: Windows.UI.WebUI.IWebUIActivationStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_Navigated(cls: Windows.UI.WebUI.IWebUIActivationStatics, handler: Windows.UI.WebUI.NavigatedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_Navigated(cls: Windows.UI.WebUI.IWebUIActivationStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class WebUIAppointmentsProviderAddAppointmentActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IAppointmentsProviderAddAppointmentActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIAppointmentsProviderAddAppointmentActivatedEventArgs'
    @winrt_mixinmethod
    def get_AddAppointmentOperation(self: Windows.ApplicationModel.Activation.IAppointmentsProviderAddAppointmentActivatedEventArgs) -> Windows.ApplicationModel.Appointments.AppointmentsProvider.AddAppointmentOperation: ...
    @winrt_mixinmethod
    def get_Verb(self: Windows.ApplicationModel.Activation.IAppointmentsProviderActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    AddAppointmentOperation = property(get_AddAppointmentOperation, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIAppointmentsProviderRemoveAppointmentActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IAppointmentsProviderRemoveAppointmentActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIAppointmentsProviderRemoveAppointmentActivatedEventArgs'
    @winrt_mixinmethod
    def get_RemoveAppointmentOperation(self: Windows.ApplicationModel.Activation.IAppointmentsProviderRemoveAppointmentActivatedEventArgs) -> Windows.ApplicationModel.Appointments.AppointmentsProvider.RemoveAppointmentOperation: ...
    @winrt_mixinmethod
    def get_Verb(self: Windows.ApplicationModel.Activation.IAppointmentsProviderActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    RemoveAppointmentOperation = property(get_RemoveAppointmentOperation, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIAppointmentsProviderReplaceAppointmentActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IAppointmentsProviderReplaceAppointmentActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIAppointmentsProviderReplaceAppointmentActivatedEventArgs'
    @winrt_mixinmethod
    def get_ReplaceAppointmentOperation(self: Windows.ApplicationModel.Activation.IAppointmentsProviderReplaceAppointmentActivatedEventArgs) -> Windows.ApplicationModel.Appointments.AppointmentsProvider.ReplaceAppointmentOperation: ...
    @winrt_mixinmethod
    def get_Verb(self: Windows.ApplicationModel.Activation.IAppointmentsProviderActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    ReplaceAppointmentOperation = property(get_ReplaceAppointmentOperation, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIAppointmentsProviderShowAppointmentDetailsActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IAppointmentsProviderShowAppointmentDetailsActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIAppointmentsProviderShowAppointmentDetailsActivatedEventArgs'
    @winrt_mixinmethod
    def get_InstanceStartDate(self: Windows.ApplicationModel.Activation.IAppointmentsProviderShowAppointmentDetailsActivatedEventArgs) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_LocalId(self: Windows.ApplicationModel.Activation.IAppointmentsProviderShowAppointmentDetailsActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RoamingId(self: Windows.ApplicationModel.Activation.IAppointmentsProviderShowAppointmentDetailsActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Verb(self: Windows.ApplicationModel.Activation.IAppointmentsProviderActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    InstanceStartDate = property(get_InstanceStartDate, None)
    LocalId = property(get_LocalId, None)
    RoamingId = property(get_RoamingId, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIAppointmentsProviderShowTimeFrameActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IAppointmentsProviderShowTimeFrameActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIAppointmentsProviderShowTimeFrameActivatedEventArgs'
    @winrt_mixinmethod
    def get_TimeToShow(self: Windows.ApplicationModel.Activation.IAppointmentsProviderShowTimeFrameActivatedEventArgs) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_Duration(self: Windows.ApplicationModel.Activation.IAppointmentsProviderShowTimeFrameActivatedEventArgs) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Verb(self: Windows.ApplicationModel.Activation.IAppointmentsProviderActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    TimeToShow = property(get_TimeToShow, None)
    Duration = property(get_Duration, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class _WebUIBackgroundTaskInstance_Meta_(ComPtr.__class__):
    pass
class WebUIBackgroundTaskInstance(ComPtr, metaclass=_WebUIBackgroundTaskInstance_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.WebUI.WebUIBackgroundTaskInstance'
    @winrt_classmethod
    def get_Current(cls: Windows.UI.WebUI.IWebUIBackgroundTaskInstanceStatics) -> Windows.UI.WebUI.IWebUIBackgroundTaskInstance: ...
    _WebUIBackgroundTaskInstance_Meta_.Current = property(get_Current.__wrapped__, None)
class WebUIBackgroundTaskInstanceRuntimeClass(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.WebUI.IWebUIBackgroundTaskInstance
    _classid_ = 'Windows.UI.WebUI.WebUIBackgroundTaskInstanceRuntimeClass'
    @winrt_mixinmethod
    def get_Succeeded(self: Windows.UI.WebUI.IWebUIBackgroundTaskInstance) -> Boolean: ...
    @winrt_mixinmethod
    def put_Succeeded(self: Windows.UI.WebUI.IWebUIBackgroundTaskInstance, succeeded: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_InstanceId(self: Windows.ApplicationModel.Background.IBackgroundTaskInstance) -> Guid: ...
    @winrt_mixinmethod
    def get_Task(self: Windows.ApplicationModel.Background.IBackgroundTaskInstance) -> Windows.ApplicationModel.Background.BackgroundTaskRegistration: ...
    @winrt_mixinmethod
    def get_Progress(self: Windows.ApplicationModel.Background.IBackgroundTaskInstance) -> UInt32: ...
    @winrt_mixinmethod
    def put_Progress(self: Windows.ApplicationModel.Background.IBackgroundTaskInstance, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_TriggerDetails(self: Windows.ApplicationModel.Background.IBackgroundTaskInstance) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def add_Canceled(self: Windows.ApplicationModel.Background.IBackgroundTaskInstance, cancelHandler: Windows.ApplicationModel.Background.BackgroundTaskCanceledEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Canceled(self: Windows.ApplicationModel.Background.IBackgroundTaskInstance, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_SuspendedCount(self: Windows.ApplicationModel.Background.IBackgroundTaskInstance) -> UInt32: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.Background.IBackgroundTaskInstance) -> Windows.ApplicationModel.Background.BackgroundTaskDeferral: ...
    Succeeded = property(get_Succeeded, put_Succeeded)
    InstanceId = property(get_InstanceId, None)
    Task = property(get_Task, None)
    Progress = property(get_Progress, put_Progress)
    TriggerDetails = property(get_TriggerDetails, None)
    SuspendedCount = property(get_SuspendedCount, None)
class WebUIBarcodeScannerPreviewActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IBarcodeScannerPreviewActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIBarcodeScannerPreviewActivatedEventArgs'
    @winrt_mixinmethod
    def get_ConnectionId(self: Windows.ApplicationModel.Activation.IBarcodeScannerPreviewActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    ConnectionId = property(get_ConnectionId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUICachedFileUpdaterActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.ICachedFileUpdaterActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUICachedFileUpdaterActivatedEventArgs'
    @winrt_mixinmethod
    def get_CachedFileUpdaterUI(self: Windows.ApplicationModel.Activation.ICachedFileUpdaterActivatedEventArgs) -> Windows.Storage.Provider.CachedFileUpdaterUI: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    CachedFileUpdaterUI = property(get_CachedFileUpdaterUI, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUICameraSettingsActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.ICameraSettingsActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUICameraSettingsActivatedEventArgs'
    @winrt_mixinmethod
    def get_VideoDeviceController(self: Windows.ApplicationModel.Activation.ICameraSettingsActivatedEventArgs) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_VideoDeviceExtension(self: Windows.ApplicationModel.Activation.ICameraSettingsActivatedEventArgs) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    VideoDeviceController = property(get_VideoDeviceController, None)
    VideoDeviceExtension = property(get_VideoDeviceExtension, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUICommandLineActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.ICommandLineActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUICommandLineActivatedEventArgs'
    @winrt_mixinmethod
    def get_Operation(self: Windows.ApplicationModel.Activation.ICommandLineActivatedEventArgs) -> Windows.ApplicationModel.Activation.CommandLineActivationOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    Operation = property(get_Operation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUIContactCallActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IContactCallActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIContactCallActivatedEventArgs'
    @winrt_mixinmethod
    def get_ServiceId(self: Windows.ApplicationModel.Activation.IContactCallActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServiceUserId(self: Windows.ApplicationModel.Activation.IContactCallActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Contact(self: Windows.ApplicationModel.Activation.IContactCallActivatedEventArgs) -> Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Verb(self: Windows.ApplicationModel.Activation.IContactActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    ServiceId = property(get_ServiceId, None)
    ServiceUserId = property(get_ServiceUserId, None)
    Contact = property(get_Contact, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUIContactMapActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IContactMapActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIContactMapActivatedEventArgs'
    @winrt_mixinmethod
    def get_Address(self: Windows.ApplicationModel.Activation.IContactMapActivatedEventArgs) -> Windows.ApplicationModel.Contacts.ContactAddress: ...
    @winrt_mixinmethod
    def get_Contact(self: Windows.ApplicationModel.Activation.IContactMapActivatedEventArgs) -> Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Verb(self: Windows.ApplicationModel.Activation.IContactActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    Address = property(get_Address, None)
    Contact = property(get_Contact, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUIContactMessageActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IContactMessageActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIContactMessageActivatedEventArgs'
    @winrt_mixinmethod
    def get_ServiceId(self: Windows.ApplicationModel.Activation.IContactMessageActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServiceUserId(self: Windows.ApplicationModel.Activation.IContactMessageActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Contact(self: Windows.ApplicationModel.Activation.IContactMessageActivatedEventArgs) -> Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Verb(self: Windows.ApplicationModel.Activation.IContactActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    ServiceId = property(get_ServiceId, None)
    ServiceUserId = property(get_ServiceUserId, None)
    Contact = property(get_Contact, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUIContactPanelActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IContactPanelActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIContactPanelActivatedEventArgs'
    @winrt_mixinmethod
    def get_ContactPanel(self: Windows.ApplicationModel.Activation.IContactPanelActivatedEventArgs) -> Windows.ApplicationModel.Contacts.ContactPanel: ...
    @winrt_mixinmethod
    def get_Contact(self: Windows.ApplicationModel.Activation.IContactPanelActivatedEventArgs) -> Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    ContactPanel = property(get_ContactPanel, None)
    Contact = property(get_Contact, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIContactPickerActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IContactPickerActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIContactPickerActivatedEventArgs'
    @winrt_mixinmethod
    def get_ContactPickerUI(self: Windows.ApplicationModel.Activation.IContactPickerActivatedEventArgs) -> Windows.ApplicationModel.Contacts.Provider.ContactPickerUI: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    ContactPickerUI = property(get_ContactPickerUI, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUIContactPostActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IContactPostActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIContactPostActivatedEventArgs'
    @winrt_mixinmethod
    def get_ServiceId(self: Windows.ApplicationModel.Activation.IContactPostActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServiceUserId(self: Windows.ApplicationModel.Activation.IContactPostActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Contact(self: Windows.ApplicationModel.Activation.IContactPostActivatedEventArgs) -> Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Verb(self: Windows.ApplicationModel.Activation.IContactActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    ServiceId = property(get_ServiceId, None)
    ServiceUserId = property(get_ServiceUserId, None)
    Contact = property(get_Contact, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUIContactVideoCallActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IContactVideoCallActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIContactVideoCallActivatedEventArgs'
    @winrt_mixinmethod
    def get_ServiceId(self: Windows.ApplicationModel.Activation.IContactVideoCallActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ServiceUserId(self: Windows.ApplicationModel.Activation.IContactVideoCallActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Contact(self: Windows.ApplicationModel.Activation.IContactVideoCallActivatedEventArgs) -> Windows.ApplicationModel.Contacts.Contact: ...
    @winrt_mixinmethod
    def get_Verb(self: Windows.ApplicationModel.Activation.IContactActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    ServiceId = property(get_ServiceId, None)
    ServiceUserId = property(get_ServiceUserId, None)
    Contact = property(get_Contact, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUIDeviceActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IDeviceActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIDeviceActivatedEventArgs'
    @winrt_mixinmethod
    def get_DeviceInformationId(self: Windows.ApplicationModel.Activation.IDeviceActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Verb(self: Windows.ApplicationModel.Activation.IDeviceActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    DeviceInformationId = property(get_DeviceInformationId, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIDevicePairingActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IDevicePairingActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIDevicePairingActivatedEventArgs'
    @winrt_mixinmethod
    def get_DeviceInformation(self: Windows.ApplicationModel.Activation.IDevicePairingActivatedEventArgs) -> Windows.Devices.Enumeration.DeviceInformation: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    DeviceInformation = property(get_DeviceInformation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIDialReceiverActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IDialReceiverActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIDialReceiverActivatedEventArgs'
    @winrt_mixinmethod
    def get_AppName(self: Windows.ApplicationModel.Activation.IDialReceiverActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Arguments(self: Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TileId(self: Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    AppName = property(get_AppName, None)
    Arguments = property(get_Arguments, None)
    TileId = property(get_TileId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIFileActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IFileActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIFileActivatedEventArgs'
    @winrt_mixinmethod
    def get_Files(self: Windows.ApplicationModel.Activation.IFileActivatedEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.Storage.IStorageItem]: ...
    @winrt_mixinmethod
    def get_Verb(self: Windows.ApplicationModel.Activation.IFileActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_NeighboringFilesQuery(self: Windows.ApplicationModel.Activation.IFileActivatedEventArgsWithNeighboringFiles) -> Windows.Storage.Search.StorageFileQueryResult: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    Files = property(get_Files, None)
    Verb = property(get_Verb, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    NeighboringFilesQuery = property(get_NeighboringFilesQuery, None)
    User = property(get_User, None)
class WebUIFileOpenPickerActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IFileOpenPickerActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIFileOpenPickerActivatedEventArgs'
    @winrt_mixinmethod
    def get_FileOpenPickerUI(self: Windows.ApplicationModel.Activation.IFileOpenPickerActivatedEventArgs) -> Windows.Storage.Pickers.Provider.FileOpenPickerUI: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CallerPackageFamilyName(self: Windows.ApplicationModel.Activation.IFileOpenPickerActivatedEventArgs2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    FileOpenPickerUI = property(get_FileOpenPickerUI, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIFileOpenPickerContinuationEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IFileOpenPickerContinuationEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIFileOpenPickerContinuationEventArgs'
    @winrt_mixinmethod
    def get_Files(self: Windows.ApplicationModel.Activation.IFileOpenPickerContinuationEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.Storage.StorageFile]: ...
    @winrt_mixinmethod
    def get_ContinuationData(self: Windows.ApplicationModel.Activation.IContinuationActivatedEventArgs) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    Files = property(get_Files, None)
    ContinuationData = property(get_ContinuationData, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIFileSavePickerActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IFileSavePickerActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIFileSavePickerActivatedEventArgs'
    @winrt_mixinmethod
    def get_FileSavePickerUI(self: Windows.ApplicationModel.Activation.IFileSavePickerActivatedEventArgs) -> Windows.Storage.Pickers.Provider.FileSavePickerUI: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CallerPackageFamilyName(self: Windows.ApplicationModel.Activation.IFileSavePickerActivatedEventArgs2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_EnterpriseId(self: Windows.ApplicationModel.Activation.IFileSavePickerActivatedEventArgs2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    FileSavePickerUI = property(get_FileSavePickerUI, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    EnterpriseId = property(get_EnterpriseId, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIFileSavePickerContinuationEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IFileSavePickerContinuationEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIFileSavePickerContinuationEventArgs'
    @winrt_mixinmethod
    def get_File(self: Windows.ApplicationModel.Activation.IFileSavePickerContinuationEventArgs) -> Windows.Storage.StorageFile: ...
    @winrt_mixinmethod
    def get_ContinuationData(self: Windows.ApplicationModel.Activation.IContinuationActivatedEventArgs) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    File = property(get_File, None)
    ContinuationData = property(get_ContinuationData, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIFolderPickerContinuationEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IFolderPickerContinuationEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIFolderPickerContinuationEventArgs'
    @winrt_mixinmethod
    def get_Folder(self: Windows.ApplicationModel.Activation.IFolderPickerContinuationEventArgs) -> Windows.Storage.StorageFolder: ...
    @winrt_mixinmethod
    def get_ContinuationData(self: Windows.ApplicationModel.Activation.IContinuationActivatedEventArgs) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    Folder = property(get_Folder, None)
    ContinuationData = property(get_ContinuationData, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUILaunchActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUILaunchActivatedEventArgs'
    @winrt_mixinmethod
    def get_Arguments(self: Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TileId(self: Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_PrelaunchActivated(self: Windows.ApplicationModel.Activation.IPrelaunchActivatedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    @winrt_mixinmethod
    def get_TileActivatedInfo(self: Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs2) -> Windows.ApplicationModel.Activation.TileActivatedInfo: ...
    Arguments = property(get_Arguments, None)
    TileId = property(get_TileId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    PrelaunchActivated = property(get_PrelaunchActivated, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
    TileActivatedInfo = property(get_TileActivatedInfo, None)
class WebUILockScreenActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.ILockScreenActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUILockScreenActivatedEventArgs'
    @winrt_mixinmethod
    def get_Info(self: Windows.ApplicationModel.Activation.ILockScreenActivatedEventArgs) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    Info = property(get_Info, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUILockScreenCallActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.ILockScreenCallActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUILockScreenCallActivatedEventArgs'
    @winrt_mixinmethod
    def get_CallUI(self: Windows.ApplicationModel.Activation.ILockScreenCallActivatedEventArgs) -> Windows.ApplicationModel.Calls.LockScreenCallUI: ...
    @winrt_mixinmethod
    def get_Arguments(self: Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_TileId(self: Windows.ApplicationModel.Activation.ILaunchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    CallUI = property(get_CallUI, None)
    Arguments = property(get_Arguments, None)
    TileId = property(get_TileId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUILockScreenComponentActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUILockScreenComponentActivatedEventArgs'
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUINavigatedDeferral(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.WebUI.IWebUINavigatedDeferral
    _classid_ = 'Windows.UI.WebUI.WebUINavigatedDeferral'
    @winrt_mixinmethod
    def Complete(self: Windows.UI.WebUI.IWebUINavigatedDeferral) -> Void: ...
class WebUINavigatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.WebUI.IWebUINavigatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUINavigatedEventArgs'
    @winrt_mixinmethod
    def get_NavigatedOperation(self: Windows.UI.WebUI.IWebUINavigatedEventArgs) -> Windows.UI.WebUI.WebUINavigatedOperation: ...
    NavigatedOperation = property(get_NavigatedOperation, None)
class WebUINavigatedOperation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.WebUI.IWebUINavigatedOperation
    _classid_ = 'Windows.UI.WebUI.WebUINavigatedOperation'
    @winrt_mixinmethod
    def GetDeferral(self: Windows.UI.WebUI.IWebUINavigatedOperation) -> Windows.UI.WebUI.WebUINavigatedDeferral: ...
class WebUIPhoneCallActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IPhoneCallActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIPhoneCallActivatedEventArgs'
    @winrt_mixinmethod
    def get_LineId(self: Windows.ApplicationModel.Activation.IPhoneCallActivatedEventArgs) -> Guid: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    LineId = property(get_LineId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUIPrint3DWorkflowActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IPrint3DWorkflowActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIPrint3DWorkflowActivatedEventArgs'
    @winrt_mixinmethod
    def get_Workflow(self: Windows.ApplicationModel.Activation.IPrint3DWorkflowActivatedEventArgs) -> Windows.Devices.Printers.Extensions.Print3DWorkflow: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    Workflow = property(get_Workflow, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUIPrintTaskSettingsActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IPrintTaskSettingsActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIPrintTaskSettingsActivatedEventArgs'
    @winrt_mixinmethod
    def get_Configuration(self: Windows.ApplicationModel.Activation.IPrintTaskSettingsActivatedEventArgs) -> Windows.Devices.Printers.Extensions.PrintTaskConfiguration: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    Configuration = property(get_Configuration, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUIPrintWorkflowForegroundTaskActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIPrintWorkflowForegroundTaskActivatedEventArgs'
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUIProtocolActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IProtocolActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIProtocolActivatedEventArgs'
    @winrt_mixinmethod
    def get_Uri(self: Windows.ApplicationModel.Activation.IProtocolActivatedEventArgs) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_CallerPackageFamilyName(self: Windows.ApplicationModel.Activation.IProtocolActivatedEventArgsWithCallerPackageFamilyNameAndData) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Data(self: Windows.ApplicationModel.Activation.IProtocolActivatedEventArgsWithCallerPackageFamilyNameAndData) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    Uri = property(get_Uri, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    Data = property(get_Data, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIProtocolForResultsActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IProtocolForResultsActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIProtocolForResultsActivatedEventArgs'
    @winrt_mixinmethod
    def get_ProtocolForResultsOperation(self: Windows.ApplicationModel.Activation.IProtocolForResultsActivatedEventArgs) -> Windows.System.ProtocolForResultsOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_Uri(self: Windows.ApplicationModel.Activation.IProtocolActivatedEventArgs) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def get_CallerPackageFamilyName(self: Windows.ApplicationModel.Activation.IProtocolActivatedEventArgsWithCallerPackageFamilyNameAndData) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Data(self: Windows.ApplicationModel.Activation.IProtocolActivatedEventArgsWithCallerPackageFamilyNameAndData) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    ProtocolForResultsOperation = property(get_ProtocolForResultsOperation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    Uri = property(get_Uri, None)
    CallerPackageFamilyName = property(get_CallerPackageFamilyName, None)
    Data = property(get_Data, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIRestrictedLaunchActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IRestrictedLaunchActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIRestrictedLaunchActivatedEventArgs'
    @winrt_mixinmethod
    def get_SharedContext(self: Windows.ApplicationModel.Activation.IRestrictedLaunchActivatedEventArgs) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    SharedContext = property(get_SharedContext, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUISearchActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.ISearchActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUISearchActivatedEventArgs'
    @winrt_mixinmethod
    def get_QueryText(self: Windows.ApplicationModel.Activation.ISearchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Language(self: Windows.ApplicationModel.Activation.ISearchActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_LinguisticDetails(self: Windows.ApplicationModel.Activation.ISearchActivatedEventArgsWithLinguisticDetails) -> Windows.ApplicationModel.Search.SearchPaneQueryLinguisticDetails: ...
    @winrt_mixinmethod
    def get_CurrentlyShownApplicationViewId(self: Windows.ApplicationModel.Activation.IApplicationViewActivatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    QueryText = property(get_QueryText, None)
    Language = property(get_Language, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    LinguisticDetails = property(get_LinguisticDetails, None)
    CurrentlyShownApplicationViewId = property(get_CurrentlyShownApplicationViewId, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUIShareTargetActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IShareTargetActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIShareTargetActivatedEventArgs'
    @winrt_mixinmethod
    def get_ShareOperation(self: Windows.ApplicationModel.Activation.IShareTargetActivatedEventArgs) -> Windows.ApplicationModel.DataTransfer.ShareTarget.ShareOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    ShareOperation = property(get_ShareOperation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIStartupTaskActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IStartupTaskActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIStartupTaskActivatedEventArgs'
    @winrt_mixinmethod
    def get_TaskId(self: Windows.ApplicationModel.Activation.IStartupTaskActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    TaskId = property(get_TaskId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    User = property(get_User, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUIToastNotificationActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IToastNotificationActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIToastNotificationActivatedEventArgs'
    @winrt_mixinmethod
    def get_Argument(self: Windows.ApplicationModel.Activation.IToastNotificationActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_UserInput(self: Windows.ApplicationModel.Activation.IToastNotificationActivatedEventArgs) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    Argument = property(get_Argument, None)
    UserInput = property(get_UserInput, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIUserDataAccountProviderActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IUserDataAccountProviderActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIUserDataAccountProviderActivatedEventArgs'
    @winrt_mixinmethod
    def get_Operation(self: Windows.ApplicationModel.Activation.IUserDataAccountProviderActivatedEventArgs) -> Windows.ApplicationModel.UserDataAccounts.Provider.IUserDataAccountProviderOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    Operation = property(get_Operation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUIView(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.WebUI.IWebUIView
    _classid_ = 'Windows.UI.WebUI.WebUIView'
    @winrt_mixinmethod
    def get_ApplicationViewId(self: Windows.UI.WebUI.IWebUIView) -> Int32: ...
    @winrt_mixinmethod
    def add_Closed(self: Windows.UI.WebUI.IWebUIView, handler: Windows.Foundation.TypedEventHandler[Windows.UI.WebUI.WebUIView, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Closed(self: Windows.UI.WebUI.IWebUIView, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Activated(self: Windows.UI.WebUI.IWebUIView, handler: Windows.Foundation.TypedEventHandler[Windows.UI.WebUI.WebUIView, Windows.ApplicationModel.Activation.IActivatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Activated(self: Windows.UI.WebUI.IWebUIView, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_IgnoreApplicationContentUriRulesNavigationRestrictions(self: Windows.UI.WebUI.IWebUIView) -> Boolean: ...
    @winrt_mixinmethod
    def put_IgnoreApplicationContentUriRulesNavigationRestrictions(self: Windows.UI.WebUI.IWebUIView, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Source(self: Windows.Web.UI.IWebViewControl) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_Source(self: Windows.Web.UI.IWebViewControl, source: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def get_DocumentTitle(self: Windows.Web.UI.IWebViewControl) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CanGoBack(self: Windows.Web.UI.IWebViewControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanGoForward(self: Windows.Web.UI.IWebViewControl) -> Boolean: ...
    @winrt_mixinmethod
    def put_DefaultBackgroundColor(self: Windows.Web.UI.IWebViewControl, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_DefaultBackgroundColor(self: Windows.Web.UI.IWebViewControl) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def get_ContainsFullScreenElement(self: Windows.Web.UI.IWebViewControl) -> Boolean: ...
    @winrt_mixinmethod
    def get_Settings(self: Windows.Web.UI.IWebViewControl) -> Windows.Web.UI.WebViewControlSettings: ...
    @winrt_mixinmethod
    def get_DeferredPermissionRequests(self: Windows.Web.UI.IWebViewControl) -> Windows.Foundation.Collections.IVectorView[Windows.Web.UI.WebViewControlDeferredPermissionRequest]: ...
    @winrt_mixinmethod
    def GoForward(self: Windows.Web.UI.IWebViewControl) -> Void: ...
    @winrt_mixinmethod
    def GoBack(self: Windows.Web.UI.IWebViewControl) -> Void: ...
    @winrt_mixinmethod
    def Refresh(self: Windows.Web.UI.IWebViewControl) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.Web.UI.IWebViewControl) -> Void: ...
    @winrt_mixinmethod
    def Navigate(self: Windows.Web.UI.IWebViewControl, source: Windows.Foundation.Uri) -> Void: ...
    @winrt_mixinmethod
    def NavigateToString(self: Windows.Web.UI.IWebViewControl, text: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def NavigateToLocalStreamUri(self: Windows.Web.UI.IWebViewControl, source: Windows.Foundation.Uri, streamResolver: Windows.Web.IUriToStreamResolver) -> Void: ...
    @winrt_mixinmethod
    def NavigateWithHttpRequestMessage(self: Windows.Web.UI.IWebViewControl, requestMessage: Windows.Web.Http.HttpRequestMessage) -> Void: ...
    @winrt_mixinmethod
    def InvokeScriptAsync(self: Windows.Web.UI.IWebViewControl, scriptName: WinRT_String, arguments: Windows.Foundation.Collections.IIterable[WinRT_String]) -> Windows.Foundation.IAsyncOperation[WinRT_String]: ...
    @winrt_mixinmethod
    def CapturePreviewToStreamAsync(self: Windows.Web.UI.IWebViewControl, stream: Windows.Storage.Streams.IRandomAccessStream) -> Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def CaptureSelectedContentToDataPackageAsync(self: Windows.Web.UI.IWebViewControl) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.DataTransfer.DataPackage]: ...
    @winrt_mixinmethod
    def BuildLocalStreamUri(self: Windows.Web.UI.IWebViewControl, contentIdentifier: WinRT_String, relativePath: WinRT_String) -> Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def GetDeferredPermissionRequestById(self: Windows.Web.UI.IWebViewControl, id: UInt32, result: POINTER(Windows.Web.UI.WebViewControlDeferredPermissionRequest)) -> Void: ...
    @winrt_mixinmethod
    def add_NavigationStarting(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlNavigationStartingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NavigationStarting(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ContentLoading(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlContentLoadingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ContentLoading(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DOMContentLoaded(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlDOMContentLoadedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DOMContentLoaded(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_NavigationCompleted(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlNavigationCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NavigationCompleted(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_FrameNavigationStarting(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlNavigationStartingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameNavigationStarting(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_FrameContentLoading(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlContentLoadingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameContentLoading(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_FrameDOMContentLoaded(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlDOMContentLoadedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameDOMContentLoaded(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_FrameNavigationCompleted(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlNavigationCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_FrameNavigationCompleted(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ScriptNotify(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlScriptNotifyEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ScriptNotify(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_LongRunningScriptDetected(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlLongRunningScriptDetectedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LongRunningScriptDetected(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UnsafeContentWarningDisplaying(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UnsafeContentWarningDisplaying(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UnviewableContentIdentified(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlUnviewableContentIdentifiedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UnviewableContentIdentified(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PermissionRequested(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlPermissionRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PermissionRequested(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UnsupportedUriSchemeIdentified(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlUnsupportedUriSchemeIdentifiedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UnsupportedUriSchemeIdentified(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_NewWindowRequested(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlNewWindowRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NewWindowRequested(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ContainsFullScreenElementChanged(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ContainsFullScreenElementChanged(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_WebResourceRequested(self: Windows.Web.UI.IWebViewControl, handler: Windows.Foundation.TypedEventHandler[Windows.Web.UI.IWebViewControl, Windows.Web.UI.WebViewControlWebResourceRequestedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_WebResourceRequested(self: Windows.Web.UI.IWebViewControl, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def AddInitializeScript(self: Windows.Web.UI.IWebViewControl2, script: WinRT_String) -> Void: ...
    @winrt_classmethod
    def CreateAsync(cls: Windows.UI.WebUI.IWebUIViewStatics) -> Windows.Foundation.IAsyncOperation[Windows.UI.WebUI.WebUIView]: ...
    @winrt_classmethod
    def CreateWithUriAsync(cls: Windows.UI.WebUI.IWebUIViewStatics, uri: Windows.Foundation.Uri) -> Windows.Foundation.IAsyncOperation[Windows.UI.WebUI.WebUIView]: ...
    ApplicationViewId = property(get_ApplicationViewId, None)
    IgnoreApplicationContentUriRulesNavigationRestrictions = property(get_IgnoreApplicationContentUriRulesNavigationRestrictions, put_IgnoreApplicationContentUriRulesNavigationRestrictions)
    Source = property(get_Source, put_Source)
    DocumentTitle = property(get_DocumentTitle, None)
    CanGoBack = property(get_CanGoBack, None)
    CanGoForward = property(get_CanGoForward, None)
    DefaultBackgroundColor = property(get_DefaultBackgroundColor, put_DefaultBackgroundColor)
    ContainsFullScreenElement = property(get_ContainsFullScreenElement, None)
    Settings = property(get_Settings, None)
    DeferredPermissionRequests = property(get_DeferredPermissionRequests, None)
class WebUIVoiceCommandActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IVoiceCommandActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIVoiceCommandActivatedEventArgs'
    @winrt_mixinmethod
    def get_Result(self: Windows.ApplicationModel.Activation.IVoiceCommandActivatedEventArgs) -> Windows.Media.SpeechRecognition.SpeechRecognitionResult: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    Result = property(get_Result, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIWalletActionActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IWalletActionActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIWalletActionActivatedEventArgs'
    @winrt_mixinmethod
    def get_ItemId(self: Windows.ApplicationModel.Activation.IWalletActionActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ActionKind(self: Windows.ApplicationModel.Activation.IWalletActionActivatedEventArgs) -> Windows.ApplicationModel.Wallet.WalletActionKind: ...
    @winrt_mixinmethod
    def get_ActionId(self: Windows.ApplicationModel.Activation.IWalletActionActivatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    ItemId = property(get_ItemId, None)
    ActionKind = property(get_ActionKind, None)
    ActionId = property(get_ActionId, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
class WebUIWebAccountProviderActivatedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IWebAccountProviderActivatedEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIWebAccountProviderActivatedEventArgs'
    @winrt_mixinmethod
    def get_Operation(self: Windows.ApplicationModel.Activation.IWebAccountProviderActivatedEventArgs) -> Windows.Security.Authentication.Web.Provider.IWebAccountProviderOperation: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    @winrt_mixinmethod
    def get_User(self: Windows.ApplicationModel.Activation.IActivatedEventArgsWithUser) -> Windows.System.User: ...
    Operation = property(get_Operation, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
    User = property(get_User, None)
class WebUIWebAuthenticationBrokerContinuationEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.ApplicationModel.Activation.IWebAuthenticationBrokerContinuationEventArgs
    _classid_ = 'Windows.UI.WebUI.WebUIWebAuthenticationBrokerContinuationEventArgs'
    @winrt_mixinmethod
    def get_WebAuthenticationResult(self: Windows.ApplicationModel.Activation.IWebAuthenticationBrokerContinuationEventArgs) -> Windows.Security.Authentication.Web.WebAuthenticationResult: ...
    @winrt_mixinmethod
    def get_ContinuationData(self: Windows.ApplicationModel.Activation.IContinuationActivatedEventArgs) -> Windows.Foundation.Collections.ValueSet: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ActivationKind: ...
    @winrt_mixinmethod
    def get_PreviousExecutionState(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.ApplicationExecutionState: ...
    @winrt_mixinmethod
    def get_SplashScreen(self: Windows.ApplicationModel.Activation.IActivatedEventArgs) -> Windows.ApplicationModel.Activation.SplashScreen: ...
    @winrt_mixinmethod
    def get_ActivatedOperation(self: Windows.UI.WebUI.IActivatedEventArgsDeferral) -> Windows.UI.WebUI.ActivatedOperation: ...
    WebAuthenticationResult = property(get_WebAuthenticationResult, None)
    ContinuationData = property(get_ContinuationData, None)
    Kind = property(get_Kind, None)
    PreviousExecutionState = property(get_PreviousExecutionState, None)
    SplashScreen = property(get_SplashScreen, None)
    ActivatedOperation = property(get_ActivatedOperation, None)
make_head(_module, 'ActivatedDeferral')
make_head(_module, 'ActivatedEventHandler')
make_head(_module, 'ActivatedOperation')
make_head(_module, 'BackgroundActivatedEventArgs')
make_head(_module, 'BackgroundActivatedEventHandler')
make_head(_module, 'EnteredBackgroundEventArgs')
make_head(_module, 'EnteredBackgroundEventHandler')
make_head(_module, 'HtmlPrintDocumentSource')
make_head(_module, 'IActivatedDeferral')
make_head(_module, 'IActivatedEventArgsDeferral')
make_head(_module, 'IActivatedOperation')
make_head(_module, 'IHtmlPrintDocumentSource')
make_head(_module, 'INewWebUIViewCreatedEventArgs')
make_head(_module, 'IWebUIActivationStatics')
make_head(_module, 'IWebUIActivationStatics2')
make_head(_module, 'IWebUIActivationStatics3')
make_head(_module, 'IWebUIActivationStatics4')
make_head(_module, 'IWebUIBackgroundTaskInstance')
make_head(_module, 'IWebUIBackgroundTaskInstanceStatics')
make_head(_module, 'IWebUINavigatedDeferral')
make_head(_module, 'IWebUINavigatedEventArgs')
make_head(_module, 'IWebUINavigatedOperation')
make_head(_module, 'IWebUIView')
make_head(_module, 'IWebUIViewStatics')
make_head(_module, 'LeavingBackgroundEventArgs')
make_head(_module, 'LeavingBackgroundEventHandler')
make_head(_module, 'NavigatedEventHandler')
make_head(_module, 'NewWebUIViewCreatedEventArgs')
make_head(_module, 'ResumingEventHandler')
make_head(_module, 'SuspendingDeferral')
make_head(_module, 'SuspendingEventArgs')
make_head(_module, 'SuspendingEventHandler')
make_head(_module, 'SuspendingOperation')
make_head(_module, 'WebUIApplication')
make_head(_module, 'WebUIAppointmentsProviderAddAppointmentActivatedEventArgs')
make_head(_module, 'WebUIAppointmentsProviderRemoveAppointmentActivatedEventArgs')
make_head(_module, 'WebUIAppointmentsProviderReplaceAppointmentActivatedEventArgs')
make_head(_module, 'WebUIAppointmentsProviderShowAppointmentDetailsActivatedEventArgs')
make_head(_module, 'WebUIAppointmentsProviderShowTimeFrameActivatedEventArgs')
make_head(_module, 'WebUIBackgroundTaskInstance')
make_head(_module, 'WebUIBackgroundTaskInstanceRuntimeClass')
make_head(_module, 'WebUIBarcodeScannerPreviewActivatedEventArgs')
make_head(_module, 'WebUICachedFileUpdaterActivatedEventArgs')
make_head(_module, 'WebUICameraSettingsActivatedEventArgs')
make_head(_module, 'WebUICommandLineActivatedEventArgs')
make_head(_module, 'WebUIContactCallActivatedEventArgs')
make_head(_module, 'WebUIContactMapActivatedEventArgs')
make_head(_module, 'WebUIContactMessageActivatedEventArgs')
make_head(_module, 'WebUIContactPanelActivatedEventArgs')
make_head(_module, 'WebUIContactPickerActivatedEventArgs')
make_head(_module, 'WebUIContactPostActivatedEventArgs')
make_head(_module, 'WebUIContactVideoCallActivatedEventArgs')
make_head(_module, 'WebUIDeviceActivatedEventArgs')
make_head(_module, 'WebUIDevicePairingActivatedEventArgs')
make_head(_module, 'WebUIDialReceiverActivatedEventArgs')
make_head(_module, 'WebUIFileActivatedEventArgs')
make_head(_module, 'WebUIFileOpenPickerActivatedEventArgs')
make_head(_module, 'WebUIFileOpenPickerContinuationEventArgs')
make_head(_module, 'WebUIFileSavePickerActivatedEventArgs')
make_head(_module, 'WebUIFileSavePickerContinuationEventArgs')
make_head(_module, 'WebUIFolderPickerContinuationEventArgs')
make_head(_module, 'WebUILaunchActivatedEventArgs')
make_head(_module, 'WebUILockScreenActivatedEventArgs')
make_head(_module, 'WebUILockScreenCallActivatedEventArgs')
make_head(_module, 'WebUILockScreenComponentActivatedEventArgs')
make_head(_module, 'WebUINavigatedDeferral')
make_head(_module, 'WebUINavigatedEventArgs')
make_head(_module, 'WebUINavigatedOperation')
make_head(_module, 'WebUIPhoneCallActivatedEventArgs')
make_head(_module, 'WebUIPrint3DWorkflowActivatedEventArgs')
make_head(_module, 'WebUIPrintTaskSettingsActivatedEventArgs')
make_head(_module, 'WebUIPrintWorkflowForegroundTaskActivatedEventArgs')
make_head(_module, 'WebUIProtocolActivatedEventArgs')
make_head(_module, 'WebUIProtocolForResultsActivatedEventArgs')
make_head(_module, 'WebUIRestrictedLaunchActivatedEventArgs')
make_head(_module, 'WebUISearchActivatedEventArgs')
make_head(_module, 'WebUIShareTargetActivatedEventArgs')
make_head(_module, 'WebUIStartupTaskActivatedEventArgs')
make_head(_module, 'WebUIToastNotificationActivatedEventArgs')
make_head(_module, 'WebUIUserDataAccountProviderActivatedEventArgs')
make_head(_module, 'WebUIView')
make_head(_module, 'WebUIVoiceCommandActivatedEventArgs')
make_head(_module, 'WebUIWalletActionActivatedEventArgs')
make_head(_module, 'WebUIWebAccountProviderActivatedEventArgs')
make_head(_module, 'WebUIWebAuthenticationBrokerContinuationEventArgs')
