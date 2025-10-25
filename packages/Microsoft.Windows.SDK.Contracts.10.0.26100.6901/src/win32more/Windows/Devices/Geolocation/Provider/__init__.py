from __future__ import annotations
from win32more.winrt.prelude import *
import win32more.Windows.Devices.Geolocation
import win32more.Windows.Devices.Geolocation.Provider
import win32more.Windows.Foundation
class GeolocationProvider(ComPtr):
    extends: IInspectable
    default_interface: win32more.Windows.Devices.Geolocation.Provider.IGeolocationProvider
    _classid_ = 'Windows.Devices.Geolocation.Provider.GeolocationProvider'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.Geolocation.Provider.GeolocationProvider.CreateInstance(*args))
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
    def add_IsOverriddenChanged(self: win32more.Windows.Devices.Geolocation.Provider.IGeolocationProvider, handler: win32more.Windows.Foundation.EventHandler[IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_IsOverriddenChanged(self: win32more.Windows.Devices.Geolocation.Provider.IGeolocationProvider, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsOverridden = property(get_IsOverridden, None)
    IsOverriddenChanged = event()
class IGeolocationProvider(ComPtr):
    extends: IInspectable
    _classid_ = 'Windows.Devices.Geolocation.Provider.IGeolocationProvider'
    _iid_ = Guid('{e4cf071d-3f64-509f-8dc2-0b74a059829d}')
    @winrt_commethod(6)
    def get_IsOverridden(self) -> Boolean: ...
    @winrt_commethod(7)
    def SetOverridePosition(self, newPosition: win32more.Windows.Devices.Geolocation.BasicGeoposition, positionSource: win32more.Windows.Devices.Geolocation.PositionSource, accuracyInMeters: Double) -> win32more.Windows.Devices.Geolocation.Provider.LocationOverrideStatus: ...
    @winrt_commethod(8)
    def ClearOverridePosition(self) -> Void: ...
    @winrt_commethod(9)
    def add_IsOverriddenChanged(self, handler: win32more.Windows.Foundation.EventHandler[IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_IsOverriddenChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsOverridden = property(get_IsOverridden, None)
    IsOverriddenChanged = event()
class LocationOverrideStatus(Enum, Int32):
    Success = 0
    AccessDenied = 1
    AlreadyStarted = 2
    Other = 3


make_ready(__name__)
