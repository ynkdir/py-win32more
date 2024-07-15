from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Media.AppBroadcasting
import win32more.Windows.System
import win32more.Windows.Win32.System.WinRT
AppBroadcastingContract: UInt32 = 65536
class AppBroadcastingMonitor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.AppBroadcasting.IAppBroadcastingMonitor
    _classid_ = 'Windows.Media.AppBroadcasting.AppBroadcastingMonitor'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Media.AppBroadcasting.AppBroadcastingMonitor.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Media.AppBroadcasting.AppBroadcastingMonitor: ...
    @winrt_mixinmethod
    def get_IsCurrentAppBroadcasting(self: win32more.Windows.Media.AppBroadcasting.IAppBroadcastingMonitor) -> Boolean: ...
    @winrt_mixinmethod
    def add_IsCurrentAppBroadcastingChanged(self: win32more.Windows.Media.AppBroadcasting.IAppBroadcastingMonitor, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.AppBroadcasting.AppBroadcastingMonitor, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_IsCurrentAppBroadcastingChanged(self: win32more.Windows.Media.AppBroadcasting.IAppBroadcastingMonitor, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsCurrentAppBroadcasting = property(get_IsCurrentAppBroadcasting, None)
    IsCurrentAppBroadcastingChanged = event()
class AppBroadcastingStatus(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.AppBroadcasting.IAppBroadcastingStatus
    _classid_ = 'Windows.Media.AppBroadcasting.AppBroadcastingStatus'
    @winrt_mixinmethod
    def get_CanStartBroadcast(self: win32more.Windows.Media.AppBroadcasting.IAppBroadcastingStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_Details(self: win32more.Windows.Media.AppBroadcasting.IAppBroadcastingStatus) -> win32more.Windows.Media.AppBroadcasting.AppBroadcastingStatusDetails: ...
    CanStartBroadcast = property(get_CanStartBroadcast, None)
    Details = property(get_Details, None)
class AppBroadcastingStatusDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.AppBroadcasting.IAppBroadcastingStatusDetails
    _classid_ = 'Windows.Media.AppBroadcasting.AppBroadcastingStatusDetails'
    @winrt_mixinmethod
    def get_IsAnyAppBroadcasting(self: win32more.Windows.Media.AppBroadcasting.IAppBroadcastingStatusDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsCaptureResourceUnavailable(self: win32more.Windows.Media.AppBroadcasting.IAppBroadcastingStatusDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsGameStreamInProgress(self: win32more.Windows.Media.AppBroadcasting.IAppBroadcastingStatusDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsGpuConstrained(self: win32more.Windows.Media.AppBroadcasting.IAppBroadcastingStatusDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsAppInactive(self: win32more.Windows.Media.AppBroadcasting.IAppBroadcastingStatusDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsBlockedForApp(self: win32more.Windows.Media.AppBroadcasting.IAppBroadcastingStatusDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDisabledByUser(self: win32more.Windows.Media.AppBroadcasting.IAppBroadcastingStatusDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDisabledBySystem(self: win32more.Windows.Media.AppBroadcasting.IAppBroadcastingStatusDetails) -> Boolean: ...
    IsAnyAppBroadcasting = property(get_IsAnyAppBroadcasting, None)
    IsAppInactive = property(get_IsAppInactive, None)
    IsBlockedForApp = property(get_IsBlockedForApp, None)
    IsCaptureResourceUnavailable = property(get_IsCaptureResourceUnavailable, None)
    IsDisabledBySystem = property(get_IsDisabledBySystem, None)
    IsDisabledByUser = property(get_IsDisabledByUser, None)
    IsGameStreamInProgress = property(get_IsGameStreamInProgress, None)
    IsGpuConstrained = property(get_IsGpuConstrained, None)
class AppBroadcastingUI(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.AppBroadcasting.IAppBroadcastingUI
    _classid_ = 'Windows.Media.AppBroadcasting.AppBroadcastingUI'
    @winrt_mixinmethod
    def GetStatus(self: win32more.Windows.Media.AppBroadcasting.IAppBroadcastingUI) -> win32more.Windows.Media.AppBroadcasting.AppBroadcastingStatus: ...
    @winrt_mixinmethod
    def ShowBroadcastUI(self: win32more.Windows.Media.AppBroadcasting.IAppBroadcastingUI) -> Void: ...
    @winrt_classmethod
    def GetDefault(cls: win32more.Windows.Media.AppBroadcasting.IAppBroadcastingUIStatics) -> win32more.Windows.Media.AppBroadcasting.AppBroadcastingUI: ...
    @winrt_classmethod
    def GetForUser(cls: win32more.Windows.Media.AppBroadcasting.IAppBroadcastingUIStatics, user: win32more.Windows.System.User) -> win32more.Windows.Media.AppBroadcasting.AppBroadcastingUI: ...
class IAppBroadcastingMonitor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.AppBroadcasting.IAppBroadcastingMonitor'
    _iid_ = Guid('{00f95a68-8907-48a0-b8ef-24d208137542}')
    @winrt_commethod(6)
    def get_IsCurrentAppBroadcasting(self) -> Boolean: ...
    @winrt_commethod(7)
    def add_IsCurrentAppBroadcastingChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Media.AppBroadcasting.AppBroadcastingMonitor, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_IsCurrentAppBroadcastingChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsCurrentAppBroadcasting = property(get_IsCurrentAppBroadcasting, None)
    IsCurrentAppBroadcastingChanged = event()
class IAppBroadcastingStatus(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.AppBroadcasting.IAppBroadcastingStatus'
    _iid_ = Guid('{1225e4df-03a1-42f8-8b80-c9228cd9cf2e}')
    @winrt_commethod(6)
    def get_CanStartBroadcast(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_Details(self) -> win32more.Windows.Media.AppBroadcasting.AppBroadcastingStatusDetails: ...
    CanStartBroadcast = property(get_CanStartBroadcast, None)
    Details = property(get_Details, None)
class IAppBroadcastingStatusDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.AppBroadcasting.IAppBroadcastingStatusDetails'
    _iid_ = Guid('{069dada4-b573-4e3c-8e19-1bafacd09713}')
    @winrt_commethod(6)
    def get_IsAnyAppBroadcasting(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsCaptureResourceUnavailable(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsGameStreamInProgress(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsGpuConstrained(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_IsAppInactive(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_IsBlockedForApp(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_IsDisabledByUser(self) -> Boolean: ...
    @winrt_commethod(13)
    def get_IsDisabledBySystem(self) -> Boolean: ...
    IsAnyAppBroadcasting = property(get_IsAnyAppBroadcasting, None)
    IsAppInactive = property(get_IsAppInactive, None)
    IsBlockedForApp = property(get_IsBlockedForApp, None)
    IsCaptureResourceUnavailable = property(get_IsCaptureResourceUnavailable, None)
    IsDisabledBySystem = property(get_IsDisabledBySystem, None)
    IsDisabledByUser = property(get_IsDisabledByUser, None)
    IsGameStreamInProgress = property(get_IsGameStreamInProgress, None)
    IsGpuConstrained = property(get_IsGpuConstrained, None)
class IAppBroadcastingUI(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.AppBroadcasting.IAppBroadcastingUI'
    _iid_ = Guid('{e56f9f8f-ee99-4dca-a3c3-70af3db44f5f}')
    @winrt_commethod(6)
    def GetStatus(self) -> win32more.Windows.Media.AppBroadcasting.AppBroadcastingStatus: ...
    @winrt_commethod(7)
    def ShowBroadcastUI(self) -> Void: ...
class IAppBroadcastingUIStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.AppBroadcasting.IAppBroadcastingUIStatics'
    _iid_ = Guid('{55a8a79d-23cb-4579-9c34-886fe02c045a}')
    @winrt_commethod(6)
    def GetDefault(self) -> win32more.Windows.Media.AppBroadcasting.AppBroadcastingUI: ...
    @winrt_commethod(7)
    def GetForUser(self, user: win32more.Windows.System.User) -> win32more.Windows.Media.AppBroadcasting.AppBroadcastingUI: ...


make_ready(__name__)
