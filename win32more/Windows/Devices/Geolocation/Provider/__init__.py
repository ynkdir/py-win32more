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
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Devices.Geolocation
import win32more.Windows.Devices.Geolocation.Provider
import win32more.Windows.Foundation
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class GeolocationProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Geolocation.Provider.IGeolocationProvider
    _classid_ = 'Windows.Devices.Geolocation.Provider.GeolocationProvider'
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Geolocation.Provider.GeolocationProvider: ...
    @winrt_mixinmethod
    def get_IsOverridden(self: win32more.Windows.Devices.Geolocation.Provider.IGeolocationProvider) -> Boolean: ...
    @winrt_mixinmethod
    def SetOverridePosition(self: win32more.Windows.Devices.Geolocation.Provider.IGeolocationProvider, newPosition: win32more.Windows.Devices.Geolocation.BasicGeoposition, positionSource: win32more.Windows.Devices.Geolocation.PositionSource, accuracyInMeters: Double) -> win32more.Windows.Devices.Geolocation.Provider.LocationOverrideStatus: ...
    @winrt_mixinmethod
    def ClearOverridePosition(self: win32more.Windows.Devices.Geolocation.Provider.IGeolocationProvider) -> Void: ...
    @winrt_mixinmethod
    def add_IsOverriddenChanged(self: win32more.Windows.Devices.Geolocation.Provider.IGeolocationProvider, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_IsOverriddenChanged(self: win32more.Windows.Devices.Geolocation.Provider.IGeolocationProvider, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsOverridden = property(get_IsOverridden, None)
class IGeolocationProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.Provider.IGeolocationProvider'
    _iid_ = Guid('{e4cf071d-3f64-509f-8dc2-0b74a059829d}')
    @winrt_commethod(6)
    def get_IsOverridden(self) -> Boolean: ...
    @winrt_commethod(7)
    def SetOverridePosition(self, newPosition: win32more.Windows.Devices.Geolocation.BasicGeoposition, positionSource: win32more.Windows.Devices.Geolocation.PositionSource, accuracyInMeters: Double) -> win32more.Windows.Devices.Geolocation.Provider.LocationOverrideStatus: ...
    @winrt_commethod(8)
    def ClearOverridePosition(self) -> Void: ...
    @winrt_commethod(9)
    def add_IsOverriddenChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_IsOverriddenChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsOverridden = property(get_IsOverridden, None)
LocationOverrideStatus = Int32
LocationOverrideStatus_Success: LocationOverrideStatus = 0
LocationOverrideStatus_AccessDenied: LocationOverrideStatus = 1
LocationOverrideStatus_AlreadyStarted: LocationOverrideStatus = 2
LocationOverrideStatus_Other: LocationOverrideStatus = 3
make_head(_module, 'GeolocationProvider')
make_head(_module, 'IGeolocationProvider')
