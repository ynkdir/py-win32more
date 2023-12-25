from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Foundation
import win32more.Windows.Media.AppBroadcasting
import win32more.Windows.System
AppBroadcastingContract: UInt32 = 65536
class AppBroadcastingMonitor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Media.AppBroadcasting.IAppBroadcastingMonitor
    _classid_ = 'Windows.Media.AppBroadcasting.AppBroadcastingMonitor'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 0:
            return win32more.Windows.Media.AppBroadcasting.AppBroadcastingMonitor.CreateInstance(*args)
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
    IsCaptureResourceUnavailable = property(get_IsCaptureResourceUnavailable, None)
    IsGameStreamInProgress = property(get_IsGameStreamInProgress, None)
    IsGpuConstrained = property(get_IsGpuConstrained, None)
    IsAppInactive = property(get_IsAppInactive, None)
    IsBlockedForApp = property(get_IsBlockedForApp, None)
    IsDisabledByUser = property(get_IsDisabledByUser, None)
    IsDisabledBySystem = property(get_IsDisabledBySystem, None)
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
    IsCaptureResourceUnavailable = property(get_IsCaptureResourceUnavailable, None)
    IsGameStreamInProgress = property(get_IsGameStreamInProgress, None)
    IsGpuConstrained = property(get_IsGpuConstrained, None)
    IsAppInactive = property(get_IsAppInactive, None)
    IsBlockedForApp = property(get_IsBlockedForApp, None)
    IsDisabledByUser = property(get_IsDisabledByUser, None)
    IsDisabledBySystem = property(get_IsDisabledBySystem, None)
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
