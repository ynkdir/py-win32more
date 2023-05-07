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
import Windows.Foundation
import Windows.Media.AppBroadcasting
import Windows.System
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
AppBroadcastingContract: UInt32 = 65536
class AppBroadcastingMonitor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.AppBroadcasting.IAppBroadcastingMonitor
    _classid_ = 'Windows.Media.AppBroadcasting.AppBroadcastingMonitor'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Media.AppBroadcasting.AppBroadcastingMonitor: ...
    @winrt_mixinmethod
    def get_IsCurrentAppBroadcasting(self: Windows.Media.AppBroadcasting.IAppBroadcastingMonitor) -> Boolean: ...
    @winrt_mixinmethod
    def add_IsCurrentAppBroadcastingChanged(self: Windows.Media.AppBroadcasting.IAppBroadcastingMonitor, handler: Windows.Foundation.TypedEventHandler[Windows.Media.AppBroadcasting.AppBroadcastingMonitor, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_IsCurrentAppBroadcastingChanged(self: Windows.Media.AppBroadcasting.IAppBroadcastingMonitor, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsCurrentAppBroadcasting = property(get_IsCurrentAppBroadcasting, None)
class AppBroadcastingStatus(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.AppBroadcasting.IAppBroadcastingStatus
    _classid_ = 'Windows.Media.AppBroadcasting.AppBroadcastingStatus'
    @winrt_mixinmethod
    def get_CanStartBroadcast(self: Windows.Media.AppBroadcasting.IAppBroadcastingStatus) -> Boolean: ...
    @winrt_mixinmethod
    def get_Details(self: Windows.Media.AppBroadcasting.IAppBroadcastingStatus) -> Windows.Media.AppBroadcasting.AppBroadcastingStatusDetails: ...
    CanStartBroadcast = property(get_CanStartBroadcast, None)
    Details = property(get_Details, None)
class AppBroadcastingStatusDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.AppBroadcasting.IAppBroadcastingStatusDetails
    _classid_ = 'Windows.Media.AppBroadcasting.AppBroadcastingStatusDetails'
    @winrt_mixinmethod
    def get_IsAnyAppBroadcasting(self: Windows.Media.AppBroadcasting.IAppBroadcastingStatusDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsCaptureResourceUnavailable(self: Windows.Media.AppBroadcasting.IAppBroadcastingStatusDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsGameStreamInProgress(self: Windows.Media.AppBroadcasting.IAppBroadcastingStatusDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsGpuConstrained(self: Windows.Media.AppBroadcasting.IAppBroadcastingStatusDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsAppInactive(self: Windows.Media.AppBroadcasting.IAppBroadcastingStatusDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsBlockedForApp(self: Windows.Media.AppBroadcasting.IAppBroadcastingStatusDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDisabledByUser(self: Windows.Media.AppBroadcasting.IAppBroadcastingStatusDetails) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsDisabledBySystem(self: Windows.Media.AppBroadcasting.IAppBroadcastingStatusDetails) -> Boolean: ...
    IsAnyAppBroadcasting = property(get_IsAnyAppBroadcasting, None)
    IsCaptureResourceUnavailable = property(get_IsCaptureResourceUnavailable, None)
    IsGameStreamInProgress = property(get_IsGameStreamInProgress, None)
    IsGpuConstrained = property(get_IsGpuConstrained, None)
    IsAppInactive = property(get_IsAppInactive, None)
    IsBlockedForApp = property(get_IsBlockedForApp, None)
    IsDisabledByUser = property(get_IsDisabledByUser, None)
    IsDisabledBySystem = property(get_IsDisabledBySystem, None)
class AppBroadcastingUI(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Media.AppBroadcasting.IAppBroadcastingUI
    _classid_ = 'Windows.Media.AppBroadcasting.AppBroadcastingUI'
    @winrt_mixinmethod
    def GetStatus(self: Windows.Media.AppBroadcasting.IAppBroadcastingUI) -> Windows.Media.AppBroadcasting.AppBroadcastingStatus: ...
    @winrt_mixinmethod
    def ShowBroadcastUI(self: Windows.Media.AppBroadcasting.IAppBroadcastingUI) -> Void: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.Media.AppBroadcasting.IAppBroadcastingUIStatics) -> Windows.Media.AppBroadcasting.AppBroadcastingUI: ...
    @winrt_classmethod
    def GetForUser(cls: Windows.Media.AppBroadcasting.IAppBroadcastingUIStatics, user: Windows.System.User) -> Windows.Media.AppBroadcasting.AppBroadcastingUI: ...
class IAppBroadcastingMonitor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.AppBroadcasting.IAppBroadcastingMonitor'
    _iid_ = Guid('{00f95a68-8907-48a0-b8ef-24d208137542}')
    @winrt_commethod(6)
    def get_IsCurrentAppBroadcasting(self: Windows.Media.AppBroadcasting.IAppBroadcastingMonitor) -> Boolean: ...
    @winrt_commethod(7)
    def add_IsCurrentAppBroadcastingChanged(self: Windows.Media.AppBroadcasting.IAppBroadcastingMonitor, handler: Windows.Foundation.TypedEventHandler[Windows.Media.AppBroadcasting.AppBroadcastingMonitor, Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_IsCurrentAppBroadcastingChanged(self: Windows.Media.AppBroadcasting.IAppBroadcastingMonitor, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsCurrentAppBroadcasting = property(get_IsCurrentAppBroadcasting, None)
class IAppBroadcastingStatus(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.AppBroadcasting.IAppBroadcastingStatus'
    _iid_ = Guid('{1225e4df-03a1-42f8-8b80-c9228cd9cf2e}')
    @winrt_commethod(6)
    def get_CanStartBroadcast(self: Windows.Media.AppBroadcasting.IAppBroadcastingStatus) -> Boolean: ...
    @winrt_commethod(7)
    def get_Details(self: Windows.Media.AppBroadcasting.IAppBroadcastingStatus) -> Windows.Media.AppBroadcasting.AppBroadcastingStatusDetails: ...
    CanStartBroadcast = property(get_CanStartBroadcast, None)
    Details = property(get_Details, None)
class IAppBroadcastingStatusDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.AppBroadcasting.IAppBroadcastingStatusDetails'
    _iid_ = Guid('{069dada4-b573-4e3c-8e19-1bafacd09713}')
    @winrt_commethod(6)
    def get_IsAnyAppBroadcasting(self: Windows.Media.AppBroadcasting.IAppBroadcastingStatusDetails) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsCaptureResourceUnavailable(self: Windows.Media.AppBroadcasting.IAppBroadcastingStatusDetails) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsGameStreamInProgress(self: Windows.Media.AppBroadcasting.IAppBroadcastingStatusDetails) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsGpuConstrained(self: Windows.Media.AppBroadcasting.IAppBroadcastingStatusDetails) -> Boolean: ...
    @winrt_commethod(10)
    def get_IsAppInactive(self: Windows.Media.AppBroadcasting.IAppBroadcastingStatusDetails) -> Boolean: ...
    @winrt_commethod(11)
    def get_IsBlockedForApp(self: Windows.Media.AppBroadcasting.IAppBroadcastingStatusDetails) -> Boolean: ...
    @winrt_commethod(12)
    def get_IsDisabledByUser(self: Windows.Media.AppBroadcasting.IAppBroadcastingStatusDetails) -> Boolean: ...
    @winrt_commethod(13)
    def get_IsDisabledBySystem(self: Windows.Media.AppBroadcasting.IAppBroadcastingStatusDetails) -> Boolean: ...
    IsAnyAppBroadcasting = property(get_IsAnyAppBroadcasting, None)
    IsCaptureResourceUnavailable = property(get_IsCaptureResourceUnavailable, None)
    IsGameStreamInProgress = property(get_IsGameStreamInProgress, None)
    IsGpuConstrained = property(get_IsGpuConstrained, None)
    IsAppInactive = property(get_IsAppInactive, None)
    IsBlockedForApp = property(get_IsBlockedForApp, None)
    IsDisabledByUser = property(get_IsDisabledByUser, None)
    IsDisabledBySystem = property(get_IsDisabledBySystem, None)
class IAppBroadcastingUI(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.AppBroadcasting.IAppBroadcastingUI'
    _iid_ = Guid('{e56f9f8f-ee99-4dca-a3c3-70af3db44f5f}')
    @winrt_commethod(6)
    def GetStatus(self: Windows.Media.AppBroadcasting.IAppBroadcastingUI) -> Windows.Media.AppBroadcasting.AppBroadcastingStatus: ...
    @winrt_commethod(7)
    def ShowBroadcastUI(self: Windows.Media.AppBroadcasting.IAppBroadcastingUI) -> Void: ...
class IAppBroadcastingUIStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Media.AppBroadcasting.IAppBroadcastingUIStatics'
    _iid_ = Guid('{55a8a79d-23cb-4579-9c34-886fe02c045a}')
    @winrt_commethod(6)
    def GetDefault(self: Windows.Media.AppBroadcasting.IAppBroadcastingUIStatics) -> Windows.Media.AppBroadcasting.AppBroadcastingUI: ...
    @winrt_commethod(7)
    def GetForUser(self: Windows.Media.AppBroadcasting.IAppBroadcastingUIStatics, user: Windows.System.User) -> Windows.Media.AppBroadcasting.AppBroadcastingUI: ...
make_head(_module, 'AppBroadcastingMonitor')
make_head(_module, 'AppBroadcastingStatus')
make_head(_module, 'AppBroadcastingStatusDetails')
make_head(_module, 'AppBroadcastingUI')
make_head(_module, 'IAppBroadcastingMonitor')
make_head(_module, 'IAppBroadcastingStatus')
make_head(_module, 'IAppBroadcastingStatusDetails')
make_head(_module, 'IAppBroadcastingUI')
make_head(_module, 'IAppBroadcastingUIStatics')
