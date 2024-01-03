from __future__ import annotations
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
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, winrt_overload, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Devices.Geolocation
import win32more.Windows.Devices.Geolocation.Provider
import win32more.Windows.Foundation
class GeolocationProvider(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Geolocation.Provider.IGeolocationProvider
    _classid_ = 'Windows.Devices.Geolocation.Provider.GeolocationProvider'
    def __new__(cls, *args, **kwargs):
        if kwargs:
            return super().__new__(cls, **kwargs)
        elif len(args) == 0:
            return win32more.Windows.Devices.Geolocation.Provider.GeolocationProvider.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Geolocation.Provider.GeolocationProvider: ...
    @winrt_mixinmethod
    def get_IsOverridden(self: win32more.Windows.Devices.Geolocation.Provider.IGeolocationProvider) -> Boolean: ...
    @winrt_mixinmethod
    def SetOverridePosition(self: win32more.Windows.Devices.Geolocation.Provider.IGeolocationProvider, newPosition: win32more.Windows.Devices.Geolocation.BasicGeoposition, positionSource: win32more.Windows.Devices.Geolocation.PositionSource, accuracyInMeters: Double) -> win32more.Windows.Devices.Geolocation.Provider.LocationOverrideStatus: ...
    @winrt_mixinmethod
    def ClearOverridePosition(self: win32more.Windows.Devices.Geolocation.Provider.IGeolocationProvider) -> Void: ...
    @winrt_mixinmethod
    def add_IsOverriddenChanged(self: win32more.Windows.Devices.Geolocation.Provider.IGeolocationProvider, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
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
    def add_IsOverriddenChanged(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_IsOverriddenChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsOverridden = property(get_IsOverridden, None)
LocationOverrideStatus = Int32
LocationOverrideStatus_Success: LocationOverrideStatus = 0
LocationOverrideStatus_AccessDenied: LocationOverrideStatus = 1
LocationOverrideStatus_AlreadyStarted: LocationOverrideStatus = 2
LocationOverrideStatus_Other: LocationOverrideStatus = 3


make_ready(__name__)
