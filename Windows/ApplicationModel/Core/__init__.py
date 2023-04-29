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
import Windows.ApplicationModel.Core
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.System
import Windows.UI.Core
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class AppListEntry(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Core.AppListEntry'
    @winrt_mixinmethod
    def get_DisplayInfo(self: Windows.ApplicationModel.Core.IAppListEntry) -> Windows.ApplicationModel.AppDisplayInfo: ...
    @winrt_mixinmethod
    def LaunchAsync(self: Windows.ApplicationModel.Core.IAppListEntry) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_AppUserModelId(self: Windows.ApplicationModel.Core.IAppListEntry2) -> WinRT_String: ...
    @winrt_mixinmethod
    def LaunchForUserAsync(self: Windows.ApplicationModel.Core.IAppListEntry3, user: Windows.System.User) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_AppInfo(self: Windows.ApplicationModel.Core.IAppListEntry4) -> Windows.ApplicationModel.AppInfo: ...
    DisplayInfo = property(get_DisplayInfo, None)
    AppUserModelId = property(get_AppUserModelId, None)
    AppInfo = property(get_AppInfo, None)
AppRestartFailureReason = Int32
AppRestartFailureReason_RestartPending: AppRestartFailureReason = 0
AppRestartFailureReason_NotInForeground: AppRestartFailureReason = 1
AppRestartFailureReason_InvalidUser: AppRestartFailureReason = 2
AppRestartFailureReason_Other: AppRestartFailureReason = 3
class CoreApplication(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Core.CoreApplication'
    @winrt_classmethod
    def CreateNewViewWithViewSource(cls: Windows.ApplicationModel.Core.ICoreImmersiveApplication3, viewSource: Windows.ApplicationModel.Core.IFrameworkViewSource) -> Windows.ApplicationModel.Core.CoreApplicationView: ...
    @winrt_classmethod
    def CreateNewViewFromMainView(cls: Windows.ApplicationModel.Core.ICoreImmersiveApplication2) -> Windows.ApplicationModel.Core.CoreApplicationView: ...
    @winrt_classmethod
    def add_UnhandledErrorDetected(cls: Windows.ApplicationModel.Core.ICoreApplicationUnhandledError, handler: Windows.Foundation.EventHandler[Windows.ApplicationModel.Core.UnhandledErrorDetectedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_UnhandledErrorDetected(cls: Windows.ApplicationModel.Core.ICoreApplicationUnhandledError, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def IncrementApplicationUseCount(cls: Windows.ApplicationModel.Core.ICoreApplicationUseCount) -> Void: ...
    @winrt_classmethod
    def DecrementApplicationUseCount(cls: Windows.ApplicationModel.Core.ICoreApplicationUseCount) -> Void: ...
    @winrt_classmethod
    def get_Views(cls: Windows.ApplicationModel.Core.ICoreImmersiveApplication) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Core.CoreApplicationView]: ...
    @winrt_classmethod
    def CreateNewView(cls: Windows.ApplicationModel.Core.ICoreImmersiveApplication, runtimeType: WinRT_String, entryPoint: WinRT_String) -> Windows.ApplicationModel.Core.CoreApplicationView: ...
    @winrt_classmethod
    def get_MainView(cls: Windows.ApplicationModel.Core.ICoreImmersiveApplication) -> Windows.ApplicationModel.Core.CoreApplicationView: ...
    @winrt_classmethod
    def Exit(cls: Windows.ApplicationModel.Core.ICoreApplicationExit) -> Void: ...
    @winrt_classmethod
    def add_Exiting(cls: Windows.ApplicationModel.Core.ICoreApplicationExit, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_Exiting(cls: Windows.ApplicationModel.Core.ICoreApplicationExit, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def RequestRestartAsync(cls: Windows.ApplicationModel.Core.ICoreApplication3, launchArguments: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Core.AppRestartFailureReason]: ...
    @winrt_classmethod
    def RequestRestartForUserAsync(cls: Windows.ApplicationModel.Core.ICoreApplication3, user: Windows.System.User, launchArguments: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Core.AppRestartFailureReason]: ...
    @winrt_classmethod
    def add_BackgroundActivated(cls: Windows.ApplicationModel.Core.ICoreApplication2, handler: Windows.Foundation.EventHandler[Windows.ApplicationModel.Activation.BackgroundActivatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_BackgroundActivated(cls: Windows.ApplicationModel.Core.ICoreApplication2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_LeavingBackground(cls: Windows.ApplicationModel.Core.ICoreApplication2, handler: Windows.Foundation.EventHandler[Windows.ApplicationModel.LeavingBackgroundEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_LeavingBackground(cls: Windows.ApplicationModel.Core.ICoreApplication2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_EnteredBackground(cls: Windows.ApplicationModel.Core.ICoreApplication2, handler: Windows.Foundation.EventHandler[Windows.ApplicationModel.EnteredBackgroundEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_EnteredBackground(cls: Windows.ApplicationModel.Core.ICoreApplication2, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def EnablePrelaunch(cls: Windows.ApplicationModel.Core.ICoreApplication2, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_Id(cls: Windows.ApplicationModel.Core.ICoreApplication) -> WinRT_String: ...
    @winrt_classmethod
    def add_Suspending(cls: Windows.ApplicationModel.Core.ICoreApplication, handler: Windows.Foundation.EventHandler[Windows.ApplicationModel.SuspendingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_Suspending(cls: Windows.ApplicationModel.Core.ICoreApplication, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_Resuming(cls: Windows.ApplicationModel.Core.ICoreApplication, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_Resuming(cls: Windows.ApplicationModel.Core.ICoreApplication, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_Properties(cls: Windows.ApplicationModel.Core.ICoreApplication) -> Windows.Foundation.Collections.IPropertySet: ...
    @winrt_classmethod
    def GetCurrentView(cls: Windows.ApplicationModel.Core.ICoreApplication) -> Windows.ApplicationModel.Core.CoreApplicationView: ...
    @winrt_classmethod
    def Run(cls: Windows.ApplicationModel.Core.ICoreApplication, viewSource: Windows.ApplicationModel.Core.IFrameworkViewSource) -> Void: ...
    @winrt_classmethod
    def RunWithActivationFactories(cls: Windows.ApplicationModel.Core.ICoreApplication, activationFactoryCallback: Windows.Foundation.IGetActivationFactory) -> Void: ...
    Views = property(get_Views, None)
    MainView = property(get_MainView, None)
    Id = property(get_Id, None)
    Properties = property(get_Properties, None)
class CoreApplicationView(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Core.CoreApplicationView'
    @winrt_mixinmethod
    def get_CoreWindow(self: Windows.ApplicationModel.Core.ICoreApplicationView) -> Windows.UI.Core.CoreWindow: ...
    @winrt_mixinmethod
    def add_Activated(self: Windows.ApplicationModel.Core.ICoreApplicationView, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Core.CoreApplicationView, Windows.ApplicationModel.Activation.IActivatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Activated(self: Windows.ApplicationModel.Core.ICoreApplicationView, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_IsMain(self: Windows.ApplicationModel.Core.ICoreApplicationView) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsHosted(self: Windows.ApplicationModel.Core.ICoreApplicationView) -> Boolean: ...
    @winrt_mixinmethod
    def get_Dispatcher(self: Windows.ApplicationModel.Core.ICoreApplicationView2) -> Windows.UI.Core.CoreDispatcher: ...
    @winrt_mixinmethod
    def get_IsComponent(self: Windows.ApplicationModel.Core.ICoreApplicationView3) -> Boolean: ...
    @winrt_mixinmethod
    def get_TitleBar(self: Windows.ApplicationModel.Core.ICoreApplicationView3) -> Windows.ApplicationModel.Core.CoreApplicationViewTitleBar: ...
    @winrt_mixinmethod
    def add_HostedViewClosing(self: Windows.ApplicationModel.Core.ICoreApplicationView3, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Core.CoreApplicationView, Windows.ApplicationModel.Core.HostedViewClosingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HostedViewClosing(self: Windows.ApplicationModel.Core.ICoreApplicationView3, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.ApplicationModel.Core.ICoreApplicationView5) -> Windows.Foundation.Collections.IPropertySet: ...
    @winrt_mixinmethod
    def get_DispatcherQueue(self: Windows.ApplicationModel.Core.ICoreApplicationView6) -> Windows.System.DispatcherQueue: ...
    CoreWindow = property(get_CoreWindow, None)
    IsMain = property(get_IsMain, None)
    IsHosted = property(get_IsHosted, None)
    Dispatcher = property(get_Dispatcher, None)
    IsComponent = property(get_IsComponent, None)
    TitleBar = property(get_TitleBar, None)
    Properties = property(get_Properties, None)
    DispatcherQueue = property(get_DispatcherQueue, None)
class CoreApplicationViewTitleBar(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Core.CoreApplicationViewTitleBar'
    @winrt_mixinmethod
    def put_ExtendViewIntoTitleBar(self: Windows.ApplicationModel.Core.ICoreApplicationViewTitleBar, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ExtendViewIntoTitleBar(self: Windows.ApplicationModel.Core.ICoreApplicationViewTitleBar) -> Boolean: ...
    @winrt_mixinmethod
    def get_SystemOverlayLeftInset(self: Windows.ApplicationModel.Core.ICoreApplicationViewTitleBar) -> Double: ...
    @winrt_mixinmethod
    def get_SystemOverlayRightInset(self: Windows.ApplicationModel.Core.ICoreApplicationViewTitleBar) -> Double: ...
    @winrt_mixinmethod
    def get_Height(self: Windows.ApplicationModel.Core.ICoreApplicationViewTitleBar) -> Double: ...
    @winrt_mixinmethod
    def add_LayoutMetricsChanged(self: Windows.ApplicationModel.Core.ICoreApplicationViewTitleBar, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Core.CoreApplicationViewTitleBar, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LayoutMetricsChanged(self: Windows.ApplicationModel.Core.ICoreApplicationViewTitleBar, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_IsVisible(self: Windows.ApplicationModel.Core.ICoreApplicationViewTitleBar) -> Boolean: ...
    @winrt_mixinmethod
    def add_IsVisibleChanged(self: Windows.ApplicationModel.Core.ICoreApplicationViewTitleBar, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Core.CoreApplicationViewTitleBar, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_IsVisibleChanged(self: Windows.ApplicationModel.Core.ICoreApplicationViewTitleBar, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    ExtendViewIntoTitleBar = property(get_ExtendViewIntoTitleBar, put_ExtendViewIntoTitleBar)
    SystemOverlayLeftInset = property(get_SystemOverlayLeftInset, None)
    SystemOverlayRightInset = property(get_SystemOverlayRightInset, None)
    Height = property(get_Height, None)
    IsVisible = property(get_IsVisible, None)
class HostedViewClosingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Core.HostedViewClosingEventArgs'
    @winrt_mixinmethod
    def GetDeferral(self: Windows.ApplicationModel.Core.IHostedViewClosingEventArgs) -> Windows.Foundation.Deferral: ...
class IAppListEntry(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('ef00f07f-2108-490a-87-7a-8a-9f-17-c2-5f-ad')
    @winrt_commethod(6)
    def get_DisplayInfo(self) -> Windows.ApplicationModel.AppDisplayInfo: ...
    @winrt_commethod(7)
    def LaunchAsync(self) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
    DisplayInfo = property(get_DisplayInfo, None)
class IAppListEntry2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d0a618ad-bf35-42ac-ac-06-86-ee-eb-41-d0-4b')
    @winrt_commethod(6)
    def get_AppUserModelId(self) -> WinRT_String: ...
    AppUserModelId = property(get_AppUserModelId, None)
class IAppListEntry3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('6099f28d-fc32-470a-bc-69-4b-06-1a-76-ef-2e')
    @winrt_commethod(6)
    def LaunchForUserAsync(self, user: Windows.System.User) -> Windows.Foundation.IAsyncOperation[Boolean]: ...
class IAppListEntry4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2a131ed2-56f5-487c-86-97-51-66-f3-b3-3d-a0')
    @winrt_commethod(6)
    def get_AppInfo(self) -> Windows.ApplicationModel.AppInfo: ...
    AppInfo = property(get_AppInfo, None)
class ICoreApplication(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('0aacf7a4-5e1d-49df-80-34-fb-6a-68-bc-5e-d1')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def add_Suspending(self, handler: Windows.Foundation.EventHandler[Windows.ApplicationModel.SuspendingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_Suspending(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def add_Resuming(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_Resuming(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def get_Properties(self) -> Windows.Foundation.Collections.IPropertySet: ...
    @winrt_commethod(12)
    def GetCurrentView(self) -> Windows.ApplicationModel.Core.CoreApplicationView: ...
    @winrt_commethod(13)
    def Run(self, viewSource: Windows.ApplicationModel.Core.IFrameworkViewSource) -> Void: ...
    @winrt_commethod(14)
    def RunWithActivationFactories(self, activationFactoryCallback: Windows.Foundation.IGetActivationFactory) -> Void: ...
    Id = property(get_Id, None)
    Properties = property(get_Properties, None)
class ICoreApplication2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('998681fb-1ab6-4b7f-be-4a-9a-06-45-22-4c-04')
    @winrt_commethod(6)
    def add_BackgroundActivated(self, handler: Windows.Foundation.EventHandler[Windows.ApplicationModel.Activation.BackgroundActivatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_BackgroundActivated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_LeavingBackground(self, handler: Windows.Foundation.EventHandler[Windows.ApplicationModel.LeavingBackgroundEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_LeavingBackground(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_EnteredBackground(self, handler: Windows.Foundation.EventHandler[Windows.ApplicationModel.EnteredBackgroundEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_EnteredBackground(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def EnablePrelaunch(self, value: Boolean) -> Void: ...
class ICoreApplication3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('feec0d39-598b-4507-8a-67-77-26-32-58-0a-57')
    @winrt_commethod(6)
    def RequestRestartAsync(self, launchArguments: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Core.AppRestartFailureReason]: ...
    @winrt_commethod(7)
    def RequestRestartForUserAsync(self, user: Windows.System.User, launchArguments: WinRT_String) -> Windows.Foundation.IAsyncOperation[Windows.ApplicationModel.Core.AppRestartFailureReason]: ...
class ICoreApplicationExit(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('cf86461d-261e-4b72-9a-cd-44-ed-2a-ce-6a-29')
    @winrt_commethod(6)
    def Exit(self) -> Void: ...
    @winrt_commethod(7)
    def add_Exiting(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_Exiting(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class ICoreApplicationUnhandledError(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('f0e24ab0-dd09-42e1-b0-bc-e0-e1-31-f7-8d-7e')
    @winrt_commethod(6)
    def add_UnhandledErrorDetected(self, handler: Windows.Foundation.EventHandler[Windows.ApplicationModel.Core.UnhandledErrorDetectedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_UnhandledErrorDetected(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class ICoreApplicationUseCount(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('518dc408-c077-475b-80-9e-0b-c0-c5-7e-4b-74')
    @winrt_commethod(6)
    def IncrementApplicationUseCount(self) -> Void: ...
    @winrt_commethod(7)
    def DecrementApplicationUseCount(self) -> Void: ...
class ICoreApplicationView(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('638bb2db-451d-4661-b0-99-41-4f-34-ff-b9-f1')
    @winrt_commethod(6)
    def get_CoreWindow(self) -> Windows.UI.Core.CoreWindow: ...
    @winrt_commethod(7)
    def add_Activated(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Core.CoreApplicationView, Windows.ApplicationModel.Activation.IActivatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_Activated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(9)
    def get_IsMain(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_IsHosted(self) -> Boolean: ...
    CoreWindow = property(get_CoreWindow, None)
    IsMain = property(get_IsMain, None)
    IsHosted = property(get_IsHosted, None)
class ICoreApplicationView2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('68eb7adf-917f-48eb-9a-eb-7d-e5-3e-08-6a-b1')
    @winrt_commethod(6)
    def get_Dispatcher(self) -> Windows.UI.Core.CoreDispatcher: ...
    Dispatcher = property(get_Dispatcher, None)
class ICoreApplicationView3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('07ebe1b3-a4cf-4550-ab-70-b0-7e-85-33-0b-c8')
    @winrt_commethod(6)
    def get_IsComponent(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_TitleBar(self) -> Windows.ApplicationModel.Core.CoreApplicationViewTitleBar: ...
    @winrt_commethod(8)
    def add_HostedViewClosing(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Core.CoreApplicationView, Windows.ApplicationModel.Core.HostedViewClosingEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_HostedViewClosing(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsComponent = property(get_IsComponent, None)
    TitleBar = property(get_TitleBar, None)
class ICoreApplicationView5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('2bc095a8-8ef0-446d-9e-60-3a-3e-04-28-c6-71')
    @winrt_commethod(6)
    def get_Properties(self) -> Windows.Foundation.Collections.IPropertySet: ...
    Properties = property(get_Properties, None)
class ICoreApplicationView6(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('c119d49a-0679-49ba-80-3f-b7-9c-5c-f3-4c-ca')
    @winrt_commethod(6)
    def get_DispatcherQueue(self) -> Windows.System.DispatcherQueue: ...
    DispatcherQueue = property(get_DispatcherQueue, None)
class ICoreApplicationViewTitleBar(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('006d35e3-e1f1-431b-95-08-29-b9-69-26-ac-53')
    @winrt_commethod(6)
    def put_ExtendViewIntoTitleBar(self, value: Boolean) -> Void: ...
    @winrt_commethod(7)
    def get_ExtendViewIntoTitleBar(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_SystemOverlayLeftInset(self) -> Double: ...
    @winrt_commethod(9)
    def get_SystemOverlayRightInset(self) -> Double: ...
    @winrt_commethod(10)
    def get_Height(self) -> Double: ...
    @winrt_commethod(11)
    def add_LayoutMetricsChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Core.CoreApplicationViewTitleBar, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_LayoutMetricsChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def get_IsVisible(self) -> Boolean: ...
    @winrt_commethod(14)
    def add_IsVisibleChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.ApplicationModel.Core.CoreApplicationViewTitleBar, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_IsVisibleChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    ExtendViewIntoTitleBar = property(get_ExtendViewIntoTitleBar, put_ExtendViewIntoTitleBar)
    SystemOverlayLeftInset = property(get_SystemOverlayLeftInset, None)
    SystemOverlayRightInset = property(get_SystemOverlayRightInset, None)
    Height = property(get_Height, None)
    IsVisible = property(get_IsVisible, None)
class ICoreImmersiveApplication(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('1ada0e3e-e4a2-4123-b4-51-dc-96-bf-80-04-19')
    @winrt_commethod(6)
    def get_Views(self) -> Windows.Foundation.Collections.IVectorView[Windows.ApplicationModel.Core.CoreApplicationView]: ...
    @winrt_commethod(7)
    def CreateNewView(self, runtimeType: WinRT_String, entryPoint: WinRT_String) -> Windows.ApplicationModel.Core.CoreApplicationView: ...
    @winrt_commethod(8)
    def get_MainView(self) -> Windows.ApplicationModel.Core.CoreApplicationView: ...
    Views = property(get_Views, None)
    MainView = property(get_MainView, None)
class ICoreImmersiveApplication2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('828e1e36-e9e3-4cfc-9b-66-48-b7-8e-a9-bb-2c')
    @winrt_commethod(6)
    def CreateNewViewFromMainView(self) -> Windows.ApplicationModel.Core.CoreApplicationView: ...
class ICoreImmersiveApplication3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('34a05b2f-ee0d-41e5-83-14-cf-10-c9-1b-f0-af')
    @winrt_commethod(6)
    def CreateNewViewWithViewSource(self, viewSource: Windows.ApplicationModel.Core.IFrameworkViewSource) -> Windows.ApplicationModel.Core.CoreApplicationView: ...
class IFrameworkView(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('faab5cd0-8924-45ac-ad-0f-a0-8f-ae-5d-03-24')
    @winrt_commethod(6)
    def Initialize(self, applicationView: Windows.ApplicationModel.Core.CoreApplicationView) -> Void: ...
    @winrt_commethod(7)
    def SetWindow(self, window: Windows.UI.Core.CoreWindow) -> Void: ...
    @winrt_commethod(8)
    def Load(self, entryPoint: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def Run(self) -> Void: ...
    @winrt_commethod(10)
    def Uninitialize(self) -> Void: ...
class IFrameworkViewSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('cd770614-65c4-426c-94-94-34-fc-43-55-48-62')
    @winrt_commethod(6)
    def CreateView(self) -> Windows.ApplicationModel.Core.IFrameworkView: ...
class IHostedViewClosingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('d238943c-b24e-4790-ac-b5-3e-42-43-c4-ff-87')
    @winrt_commethod(6)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
class IUnhandledError(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('9459b726-53b5-4686-9e-af-fa-81-62-dc-39-80')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def Propagate(self) -> Void: ...
    Handled = property(get_Handled, None)
class IUnhandledErrorDetectedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _iid_ = Guid('679ab78b-b336-4822-ac-40-0d-75-0f-0b-7a-2b')
    @winrt_commethod(6)
    def get_UnhandledError(self) -> Windows.ApplicationModel.Core.UnhandledError: ...
    UnhandledError = property(get_UnhandledError, None)
class UnhandledError(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Core.UnhandledError'
    @winrt_mixinmethod
    def get_Handled(self: Windows.ApplicationModel.Core.IUnhandledError) -> Boolean: ...
    @winrt_mixinmethod
    def Propagate(self: Windows.ApplicationModel.Core.IUnhandledError) -> Void: ...
    Handled = property(get_Handled, None)
class UnhandledErrorDetectedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.ApplicationModel.Core.UnhandledErrorDetectedEventArgs'
    @winrt_mixinmethod
    def get_UnhandledError(self: Windows.ApplicationModel.Core.IUnhandledErrorDetectedEventArgs) -> Windows.ApplicationModel.Core.UnhandledError: ...
    UnhandledError = property(get_UnhandledError, None)
make_head(_module, 'AppListEntry')
make_head(_module, 'CoreApplication')
make_head(_module, 'CoreApplicationView')
make_head(_module, 'CoreApplicationViewTitleBar')
make_head(_module, 'HostedViewClosingEventArgs')
make_head(_module, 'IAppListEntry')
make_head(_module, 'IAppListEntry2')
make_head(_module, 'IAppListEntry3')
make_head(_module, 'IAppListEntry4')
make_head(_module, 'ICoreApplication')
make_head(_module, 'ICoreApplication2')
make_head(_module, 'ICoreApplication3')
make_head(_module, 'ICoreApplicationExit')
make_head(_module, 'ICoreApplicationUnhandledError')
make_head(_module, 'ICoreApplicationUseCount')
make_head(_module, 'ICoreApplicationView')
make_head(_module, 'ICoreApplicationView2')
make_head(_module, 'ICoreApplicationView3')
make_head(_module, 'ICoreApplicationView5')
make_head(_module, 'ICoreApplicationView6')
make_head(_module, 'ICoreApplicationViewTitleBar')
make_head(_module, 'ICoreImmersiveApplication')
make_head(_module, 'ICoreImmersiveApplication2')
make_head(_module, 'ICoreImmersiveApplication3')
make_head(_module, 'IFrameworkView')
make_head(_module, 'IFrameworkViewSource')
make_head(_module, 'IHostedViewClosingEventArgs')
make_head(_module, 'IUnhandledError')
make_head(_module, 'IUnhandledErrorDetectedEventArgs')
make_head(_module, 'UnhandledError')
make_head(_module, 'UnhandledErrorDetectedEventArgs')
