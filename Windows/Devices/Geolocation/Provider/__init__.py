from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, WinRT_String, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.System.WinRT
import Windows.Devices.Geolocation
import Windows.Devices.Geolocation.Provider
import Windows.Foundation
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class GeolocationProvider(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Devices.Geolocation.Provider.GeolocationProvider'
    @winrt_activatemethod
    def New(cls) -> Windows.Devices.Geolocation.Provider.GeolocationProvider: ...
    @winrt_mixinmethod
    def get_IsOverridden(self: Windows.Devices.Geolocation.Provider.IGeolocationProvider) -> Boolean: ...
    @winrt_mixinmethod
    def SetOverridePosition(self: Windows.Devices.Geolocation.Provider.IGeolocationProvider, newPosition: Windows.Devices.Geolocation.BasicGeoposition, positionSource: Windows.Devices.Geolocation.PositionSource, accuracyInMeters: Double) -> Windows.Devices.Geolocation.Provider.LocationOverrideStatus: ...
    @winrt_mixinmethod
    def ClearOverridePosition(self: Windows.Devices.Geolocation.Provider.IGeolocationProvider) -> Void: ...
    @winrt_mixinmethod
    def add_IsOverriddenChanged(self: Windows.Devices.Geolocation.Provider.IGeolocationProvider, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_IsOverriddenChanged(self: Windows.Devices.Geolocation.Provider.IGeolocationProvider, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsOverridden = property(get_IsOverridden, None)
class IGeolocationProvider(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e4cf071d-3f64-509f-8d-c2-0b-74-a0-59-82-9d')
    @winrt_commethod(6)
    def get_IsOverridden(self) -> Boolean: ...
    @winrt_commethod(7)
    def SetOverridePosition(self, newPosition: Windows.Devices.Geolocation.BasicGeoposition, positionSource: Windows.Devices.Geolocation.PositionSource, accuracyInMeters: Double) -> Windows.Devices.Geolocation.Provider.LocationOverrideStatus: ...
    @winrt_commethod(8)
    def ClearOverridePosition(self) -> Void: ...
    @winrt_commethod(9)
    def add_IsOverriddenChanged(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_IsOverriddenChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsOverridden = property(get_IsOverridden, None)
LocationOverrideStatus = Int32
LocationOverrideStatus_Success: LocationOverrideStatus = 0
LocationOverrideStatus_AccessDenied: LocationOverrideStatus = 1
LocationOverrideStatus_AlreadyStarted: LocationOverrideStatus = 2
LocationOverrideStatus_Other: LocationOverrideStatus = 3
make_head(_module, 'GeolocationProvider')
make_head(_module, 'IGeolocationProvider')
