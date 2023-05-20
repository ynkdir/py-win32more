from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from Windows._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import Windows.Win32.System.WinRT
import Windows.Devices.Geolocation
import Windows.Foundation
import Windows.Foundation.Collections
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
AltitudeReferenceSystem = Int32
AltitudeReferenceSystem_Unspecified: AltitudeReferenceSystem = 0
AltitudeReferenceSystem_Terrain: AltitudeReferenceSystem = 1
AltitudeReferenceSystem_Ellipsoid: AltitudeReferenceSystem = 2
AltitudeReferenceSystem_Geoid: AltitudeReferenceSystem = 3
AltitudeReferenceSystem_Surface: AltitudeReferenceSystem = 4
class BasicGeoposition(EasyCastStructure):
    Latitude: Double
    Longitude: Double
    Altitude: Double
class CivicAddress(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Geolocation.ICivicAddress
    _classid_ = 'Windows.Devices.Geolocation.CivicAddress'
    @winrt_mixinmethod
    def get_Country(self: Windows.Devices.Geolocation.ICivicAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_State(self: Windows.Devices.Geolocation.ICivicAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_City(self: Windows.Devices.Geolocation.ICivicAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PostalCode(self: Windows.Devices.Geolocation.ICivicAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Geolocation.ICivicAddress) -> Windows.Foundation.DateTime: ...
    Country = property(get_Country, None)
    State = property(get_State, None)
    City = property(get_City, None)
    PostalCode = property(get_PostalCode, None)
    Timestamp = property(get_Timestamp, None)
class GeoboundingBox(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Geolocation.IGeoboundingBox
    _classid_ = 'Windows.Devices.Geolocation.GeoboundingBox'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.Geolocation.IGeoboundingBoxFactory, northwestCorner: Windows.Devices.Geolocation.BasicGeoposition, southeastCorner: Windows.Devices.Geolocation.BasicGeoposition) -> Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_factorymethod
    def CreateWithAltitudeReference(cls: Windows.Devices.Geolocation.IGeoboundingBoxFactory, northwestCorner: Windows.Devices.Geolocation.BasicGeoposition, southeastCorner: Windows.Devices.Geolocation.BasicGeoposition, altitudeReferenceSystem: Windows.Devices.Geolocation.AltitudeReferenceSystem) -> Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_factorymethod
    def CreateWithAltitudeReferenceAndSpatialReference(cls: Windows.Devices.Geolocation.IGeoboundingBoxFactory, northwestCorner: Windows.Devices.Geolocation.BasicGeoposition, southeastCorner: Windows.Devices.Geolocation.BasicGeoposition, altitudeReferenceSystem: Windows.Devices.Geolocation.AltitudeReferenceSystem, spatialReferenceId: UInt32) -> Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_mixinmethod
    def get_NorthwestCorner(self: Windows.Devices.Geolocation.IGeoboundingBox) -> Windows.Devices.Geolocation.BasicGeoposition: ...
    @winrt_mixinmethod
    def get_SoutheastCorner(self: Windows.Devices.Geolocation.IGeoboundingBox) -> Windows.Devices.Geolocation.BasicGeoposition: ...
    @winrt_mixinmethod
    def get_Center(self: Windows.Devices.Geolocation.IGeoboundingBox) -> Windows.Devices.Geolocation.BasicGeoposition: ...
    @winrt_mixinmethod
    def get_MinAltitude(self: Windows.Devices.Geolocation.IGeoboundingBox) -> Double: ...
    @winrt_mixinmethod
    def get_MaxAltitude(self: Windows.Devices.Geolocation.IGeoboundingBox) -> Double: ...
    @winrt_mixinmethod
    def get_GeoshapeType(self: Windows.Devices.Geolocation.IGeoshape) -> Windows.Devices.Geolocation.GeoshapeType: ...
    @winrt_mixinmethod
    def get_SpatialReferenceId(self: Windows.Devices.Geolocation.IGeoshape) -> UInt32: ...
    @winrt_mixinmethod
    def get_AltitudeReferenceSystem(self: Windows.Devices.Geolocation.IGeoshape) -> Windows.Devices.Geolocation.AltitudeReferenceSystem: ...
    @winrt_classmethod
    def TryCompute(cls: Windows.Devices.Geolocation.IGeoboundingBoxStatics, positions: Windows.Foundation.Collections.IIterable[Windows.Devices.Geolocation.BasicGeoposition]) -> Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_classmethod
    def TryComputeWithAltitudeReference(cls: Windows.Devices.Geolocation.IGeoboundingBoxStatics, positions: Windows.Foundation.Collections.IIterable[Windows.Devices.Geolocation.BasicGeoposition], altitudeRefSystem: Windows.Devices.Geolocation.AltitudeReferenceSystem) -> Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_classmethod
    def TryComputeWithAltitudeReferenceAndSpatialReference(cls: Windows.Devices.Geolocation.IGeoboundingBoxStatics, positions: Windows.Foundation.Collections.IIterable[Windows.Devices.Geolocation.BasicGeoposition], altitudeRefSystem: Windows.Devices.Geolocation.AltitudeReferenceSystem, spatialReferenceId: UInt32) -> Windows.Devices.Geolocation.GeoboundingBox: ...
    NorthwestCorner = property(get_NorthwestCorner, None)
    SoutheastCorner = property(get_SoutheastCorner, None)
    Center = property(get_Center, None)
    MinAltitude = property(get_MinAltitude, None)
    MaxAltitude = property(get_MaxAltitude, None)
    GeoshapeType = property(get_GeoshapeType, None)
    SpatialReferenceId = property(get_SpatialReferenceId, None)
    AltitudeReferenceSystem = property(get_AltitudeReferenceSystem, None)
class Geocircle(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Geolocation.IGeocircle
    _classid_ = 'Windows.Devices.Geolocation.Geocircle'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.Geolocation.IGeocircleFactory, position: Windows.Devices.Geolocation.BasicGeoposition, radius: Double) -> Windows.Devices.Geolocation.Geocircle: ...
    @winrt_factorymethod
    def CreateWithAltitudeReferenceSystem(cls: Windows.Devices.Geolocation.IGeocircleFactory, position: Windows.Devices.Geolocation.BasicGeoposition, radius: Double, altitudeReferenceSystem: Windows.Devices.Geolocation.AltitudeReferenceSystem) -> Windows.Devices.Geolocation.Geocircle: ...
    @winrt_factorymethod
    def CreateWithAltitudeReferenceSystemAndSpatialReferenceId(cls: Windows.Devices.Geolocation.IGeocircleFactory, position: Windows.Devices.Geolocation.BasicGeoposition, radius: Double, altitudeReferenceSystem: Windows.Devices.Geolocation.AltitudeReferenceSystem, spatialReferenceId: UInt32) -> Windows.Devices.Geolocation.Geocircle: ...
    @winrt_mixinmethod
    def get_Center(self: Windows.Devices.Geolocation.IGeocircle) -> Windows.Devices.Geolocation.BasicGeoposition: ...
    @winrt_mixinmethod
    def get_Radius(self: Windows.Devices.Geolocation.IGeocircle) -> Double: ...
    @winrt_mixinmethod
    def get_GeoshapeType(self: Windows.Devices.Geolocation.IGeoshape) -> Windows.Devices.Geolocation.GeoshapeType: ...
    @winrt_mixinmethod
    def get_SpatialReferenceId(self: Windows.Devices.Geolocation.IGeoshape) -> UInt32: ...
    @winrt_mixinmethod
    def get_AltitudeReferenceSystem(self: Windows.Devices.Geolocation.IGeoshape) -> Windows.Devices.Geolocation.AltitudeReferenceSystem: ...
    Center = property(get_Center, None)
    Radius = property(get_Radius, None)
    GeoshapeType = property(get_GeoshapeType, None)
    SpatialReferenceId = property(get_SpatialReferenceId, None)
    AltitudeReferenceSystem = property(get_AltitudeReferenceSystem, None)
class Geocoordinate(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Geolocation.IGeocoordinate
    _classid_ = 'Windows.Devices.Geolocation.Geocoordinate'
    @winrt_mixinmethod
    def get_Latitude(self: Windows.Devices.Geolocation.IGeocoordinate) -> Double: ...
    @winrt_mixinmethod
    def get_Longitude(self: Windows.Devices.Geolocation.IGeocoordinate) -> Double: ...
    @winrt_mixinmethod
    def get_Altitude(self: Windows.Devices.Geolocation.IGeocoordinate) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_Accuracy(self: Windows.Devices.Geolocation.IGeocoordinate) -> Double: ...
    @winrt_mixinmethod
    def get_AltitudeAccuracy(self: Windows.Devices.Geolocation.IGeocoordinate) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_Heading(self: Windows.Devices.Geolocation.IGeocoordinate) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_Speed(self: Windows.Devices.Geolocation.IGeocoordinate) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Geolocation.IGeocoordinate) -> Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_PositionSource(self: Windows.Devices.Geolocation.IGeocoordinateWithPositionData) -> Windows.Devices.Geolocation.PositionSource: ...
    @winrt_mixinmethod
    def get_SatelliteData(self: Windows.Devices.Geolocation.IGeocoordinateWithPositionData) -> Windows.Devices.Geolocation.GeocoordinateSatelliteData: ...
    @winrt_mixinmethod
    def get_Point(self: Windows.Devices.Geolocation.IGeocoordinateWithPoint) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_PositionSourceTimestamp(self: Windows.Devices.Geolocation.IGeocoordinateWithPositionSourceTimestamp) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_IsRemoteSource(self: Windows.Devices.Geolocation.IGeocoordinateWithRemoteSource) -> Boolean: ...
    Latitude = property(get_Latitude, None)
    Longitude = property(get_Longitude, None)
    Altitude = property(get_Altitude, None)
    Accuracy = property(get_Accuracy, None)
    AltitudeAccuracy = property(get_AltitudeAccuracy, None)
    Heading = property(get_Heading, None)
    Speed = property(get_Speed, None)
    Timestamp = property(get_Timestamp, None)
    PositionSource = property(get_PositionSource, None)
    SatelliteData = property(get_SatelliteData, None)
    Point = property(get_Point, None)
    PositionSourceTimestamp = property(get_PositionSourceTimestamp, None)
    IsRemoteSource = property(get_IsRemoteSource, None)
class GeocoordinateSatelliteData(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Geolocation.IGeocoordinateSatelliteData
    _classid_ = 'Windows.Devices.Geolocation.GeocoordinateSatelliteData'
    @winrt_mixinmethod
    def get_PositionDilutionOfPrecision(self: Windows.Devices.Geolocation.IGeocoordinateSatelliteData) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_HorizontalDilutionOfPrecision(self: Windows.Devices.Geolocation.IGeocoordinateSatelliteData) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_VerticalDilutionOfPrecision(self: Windows.Devices.Geolocation.IGeocoordinateSatelliteData) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_GeometricDilutionOfPrecision(self: Windows.Devices.Geolocation.IGeocoordinateSatelliteData2) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_TimeDilutionOfPrecision(self: Windows.Devices.Geolocation.IGeocoordinateSatelliteData2) -> Windows.Foundation.IReference[Double]: ...
    PositionDilutionOfPrecision = property(get_PositionDilutionOfPrecision, None)
    HorizontalDilutionOfPrecision = property(get_HorizontalDilutionOfPrecision, None)
    VerticalDilutionOfPrecision = property(get_VerticalDilutionOfPrecision, None)
    GeometricDilutionOfPrecision = property(get_GeometricDilutionOfPrecision, None)
    TimeDilutionOfPrecision = property(get_TimeDilutionOfPrecision, None)
GeolocationAccessStatus = Int32
GeolocationAccessStatus_Unspecified: GeolocationAccessStatus = 0
GeolocationAccessStatus_Allowed: GeolocationAccessStatus = 1
GeolocationAccessStatus_Denied: GeolocationAccessStatus = 2
class _Geolocator_Meta_(ComPtr.__class__):
    pass
class Geolocator(ComPtr, metaclass=_Geolocator_Meta_):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Geolocation.IGeolocator
    _classid_ = 'Windows.Devices.Geolocation.Geolocator'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Devices.Geolocation.Geolocator: ...
    @winrt_mixinmethod
    def get_DesiredAccuracy(self: Windows.Devices.Geolocation.IGeolocator) -> Windows.Devices.Geolocation.PositionAccuracy: ...
    @winrt_mixinmethod
    def put_DesiredAccuracy(self: Windows.Devices.Geolocation.IGeolocator, value: Windows.Devices.Geolocation.PositionAccuracy) -> Void: ...
    @winrt_mixinmethod
    def get_MovementThreshold(self: Windows.Devices.Geolocation.IGeolocator) -> Double: ...
    @winrt_mixinmethod
    def put_MovementThreshold(self: Windows.Devices.Geolocation.IGeolocator, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ReportInterval(self: Windows.Devices.Geolocation.IGeolocator) -> UInt32: ...
    @winrt_mixinmethod
    def put_ReportInterval(self: Windows.Devices.Geolocation.IGeolocator, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_LocationStatus(self: Windows.Devices.Geolocation.IGeolocator) -> Windows.Devices.Geolocation.PositionStatus: ...
    @winrt_mixinmethod
    def GetGeopositionAsync(self: Windows.Devices.Geolocation.IGeolocator) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Geolocation.Geoposition]: ...
    @winrt_mixinmethod
    def GetGeopositionAsyncWithAgeAndTimeout(self: Windows.Devices.Geolocation.IGeolocator, maximumAge: Windows.Foundation.TimeSpan, timeout: Windows.Foundation.TimeSpan) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Geolocation.Geoposition]: ...
    @winrt_mixinmethod
    def add_PositionChanged(self: Windows.Devices.Geolocation.IGeolocator, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Geolocation.Geolocator, Windows.Devices.Geolocation.PositionChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PositionChanged(self: Windows.Devices.Geolocation.IGeolocator, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_StatusChanged(self: Windows.Devices.Geolocation.IGeolocator, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Geolocation.Geolocator, Windows.Devices.Geolocation.StatusChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StatusChanged(self: Windows.Devices.Geolocation.IGeolocator, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredAccuracyInMeters(self: Windows.Devices.Geolocation.IGeolocatorWithScalarAccuracy) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def put_DesiredAccuracyInMeters(self: Windows.Devices.Geolocation.IGeolocatorWithScalarAccuracy, value: Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_mixinmethod
    def AllowFallbackToConsentlessPositions(self: Windows.Devices.Geolocation.IGeolocator2) -> Void: ...
    @winrt_classmethod
    def get_IsDefaultGeopositionRecommended(cls: Windows.Devices.Geolocation.IGeolocatorStatics2) -> Boolean: ...
    @winrt_classmethod
    def put_DefaultGeoposition(cls: Windows.Devices.Geolocation.IGeolocatorStatics2, value: Windows.Foundation.IReference[Windows.Devices.Geolocation.BasicGeoposition]) -> Void: ...
    @winrt_classmethod
    def get_DefaultGeoposition(cls: Windows.Devices.Geolocation.IGeolocatorStatics2) -> Windows.Foundation.IReference[Windows.Devices.Geolocation.BasicGeoposition]: ...
    @winrt_classmethod
    def RequestAccessAsync(cls: Windows.Devices.Geolocation.IGeolocatorStatics) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Geolocation.GeolocationAccessStatus]: ...
    @winrt_classmethod
    def GetGeopositionHistoryAsync(cls: Windows.Devices.Geolocation.IGeolocatorStatics, startTime: Windows.Foundation.DateTime) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Geolocation.Geoposition]]: ...
    @winrt_classmethod
    def GetGeopositionHistoryWithDurationAsync(cls: Windows.Devices.Geolocation.IGeolocatorStatics, startTime: Windows.Foundation.DateTime, duration: Windows.Foundation.TimeSpan) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Geolocation.Geoposition]]: ...
    DesiredAccuracy = property(get_DesiredAccuracy, put_DesiredAccuracy)
    MovementThreshold = property(get_MovementThreshold, put_MovementThreshold)
    ReportInterval = property(get_ReportInterval, put_ReportInterval)
    LocationStatus = property(get_LocationStatus, None)
    DesiredAccuracyInMeters = property(get_DesiredAccuracyInMeters, put_DesiredAccuracyInMeters)
    _Geolocator_Meta_.IsDefaultGeopositionRecommended = property(get_IsDefaultGeopositionRecommended.__wrapped__, None)
    _Geolocator_Meta_.DefaultGeoposition = property(get_DefaultGeoposition.__wrapped__, put_DefaultGeoposition.__wrapped__)
class Geopath(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Geolocation.IGeopath
    _classid_ = 'Windows.Devices.Geolocation.Geopath'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.Geolocation.IGeopathFactory, positions: Windows.Foundation.Collections.IIterable[Windows.Devices.Geolocation.BasicGeoposition]) -> Windows.Devices.Geolocation.Geopath: ...
    @winrt_factorymethod
    def CreateWithAltitudeReference(cls: Windows.Devices.Geolocation.IGeopathFactory, positions: Windows.Foundation.Collections.IIterable[Windows.Devices.Geolocation.BasicGeoposition], altitudeReferenceSystem: Windows.Devices.Geolocation.AltitudeReferenceSystem) -> Windows.Devices.Geolocation.Geopath: ...
    @winrt_factorymethod
    def CreateWithAltitudeReferenceAndSpatialReference(cls: Windows.Devices.Geolocation.IGeopathFactory, positions: Windows.Foundation.Collections.IIterable[Windows.Devices.Geolocation.BasicGeoposition], altitudeReferenceSystem: Windows.Devices.Geolocation.AltitudeReferenceSystem, spatialReferenceId: UInt32) -> Windows.Devices.Geolocation.Geopath: ...
    @winrt_mixinmethod
    def get_Positions(self: Windows.Devices.Geolocation.IGeopath) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Geolocation.BasicGeoposition]: ...
    @winrt_mixinmethod
    def get_GeoshapeType(self: Windows.Devices.Geolocation.IGeoshape) -> Windows.Devices.Geolocation.GeoshapeType: ...
    @winrt_mixinmethod
    def get_SpatialReferenceId(self: Windows.Devices.Geolocation.IGeoshape) -> UInt32: ...
    @winrt_mixinmethod
    def get_AltitudeReferenceSystem(self: Windows.Devices.Geolocation.IGeoshape) -> Windows.Devices.Geolocation.AltitudeReferenceSystem: ...
    Positions = property(get_Positions, None)
    GeoshapeType = property(get_GeoshapeType, None)
    SpatialReferenceId = property(get_SpatialReferenceId, None)
    AltitudeReferenceSystem = property(get_AltitudeReferenceSystem, None)
class Geopoint(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Geolocation.IGeopoint
    _classid_ = 'Windows.Devices.Geolocation.Geopoint'
    @winrt_factorymethod
    def Create(cls: Windows.Devices.Geolocation.IGeopointFactory, position: Windows.Devices.Geolocation.BasicGeoposition) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_factorymethod
    def CreateWithAltitudeReferenceSystem(cls: Windows.Devices.Geolocation.IGeopointFactory, position: Windows.Devices.Geolocation.BasicGeoposition, altitudeReferenceSystem: Windows.Devices.Geolocation.AltitudeReferenceSystem) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_factorymethod
    def CreateWithAltitudeReferenceSystemAndSpatialReferenceId(cls: Windows.Devices.Geolocation.IGeopointFactory, position: Windows.Devices.Geolocation.BasicGeoposition, altitudeReferenceSystem: Windows.Devices.Geolocation.AltitudeReferenceSystem, spatialReferenceId: UInt32) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.Devices.Geolocation.IGeopoint) -> Windows.Devices.Geolocation.BasicGeoposition: ...
    @winrt_mixinmethod
    def get_GeoshapeType(self: Windows.Devices.Geolocation.IGeoshape) -> Windows.Devices.Geolocation.GeoshapeType: ...
    @winrt_mixinmethod
    def get_SpatialReferenceId(self: Windows.Devices.Geolocation.IGeoshape) -> UInt32: ...
    @winrt_mixinmethod
    def get_AltitudeReferenceSystem(self: Windows.Devices.Geolocation.IGeoshape) -> Windows.Devices.Geolocation.AltitudeReferenceSystem: ...
    Position = property(get_Position, None)
    GeoshapeType = property(get_GeoshapeType, None)
    SpatialReferenceId = property(get_SpatialReferenceId, None)
    AltitudeReferenceSystem = property(get_AltitudeReferenceSystem, None)
class Geoposition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Geolocation.IGeoposition
    _classid_ = 'Windows.Devices.Geolocation.Geoposition'
    @winrt_mixinmethod
    def get_Coordinate(self: Windows.Devices.Geolocation.IGeoposition) -> Windows.Devices.Geolocation.Geocoordinate: ...
    @winrt_mixinmethod
    def get_CivicAddress(self: Windows.Devices.Geolocation.IGeoposition) -> Windows.Devices.Geolocation.CivicAddress: ...
    @winrt_mixinmethod
    def get_VenueData(self: Windows.Devices.Geolocation.IGeoposition2) -> Windows.Devices.Geolocation.VenueData: ...
    Coordinate = property(get_Coordinate, None)
    CivicAddress = property(get_CivicAddress, None)
    VenueData = property(get_VenueData, None)
GeoshapeType = Int32
GeoshapeType_Geopoint: GeoshapeType = 0
GeoshapeType_Geocircle: GeoshapeType = 1
GeoshapeType_Geopath: GeoshapeType = 2
GeoshapeType_GeoboundingBox: GeoshapeType = 3
class Geovisit(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Geolocation.IGeovisit
    _classid_ = 'Windows.Devices.Geolocation.Geovisit'
    @winrt_mixinmethod
    def get_Position(self: Windows.Devices.Geolocation.IGeovisit) -> Windows.Devices.Geolocation.Geoposition: ...
    @winrt_mixinmethod
    def get_StateChange(self: Windows.Devices.Geolocation.IGeovisit) -> Windows.Devices.Geolocation.VisitStateChange: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.Devices.Geolocation.IGeovisit) -> Windows.Foundation.DateTime: ...
    Position = property(get_Position, None)
    StateChange = property(get_StateChange, None)
    Timestamp = property(get_Timestamp, None)
class GeovisitMonitor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Geolocation.IGeovisitMonitor
    _classid_ = 'Windows.Devices.Geolocation.GeovisitMonitor'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.Devices.Geolocation.GeovisitMonitor: ...
    @winrt_mixinmethod
    def get_MonitoringScope(self: Windows.Devices.Geolocation.IGeovisitMonitor) -> Windows.Devices.Geolocation.VisitMonitoringScope: ...
    @winrt_mixinmethod
    def Start(self: Windows.Devices.Geolocation.IGeovisitMonitor, value: Windows.Devices.Geolocation.VisitMonitoringScope) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: Windows.Devices.Geolocation.IGeovisitMonitor) -> Void: ...
    @winrt_mixinmethod
    def add_VisitStateChanged(self: Windows.Devices.Geolocation.IGeovisitMonitor, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Geolocation.GeovisitMonitor, Windows.Devices.Geolocation.GeovisitStateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VisitStateChanged(self: Windows.Devices.Geolocation.IGeovisitMonitor, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetLastReportAsync(cls: Windows.Devices.Geolocation.IGeovisitMonitorStatics) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Geolocation.Geovisit]: ...
    MonitoringScope = property(get_MonitoringScope, None)
class GeovisitStateChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Geolocation.IGeovisitStateChangedEventArgs
    _classid_ = 'Windows.Devices.Geolocation.GeovisitStateChangedEventArgs'
    @winrt_mixinmethod
    def get_Visit(self: Windows.Devices.Geolocation.IGeovisitStateChangedEventArgs) -> Windows.Devices.Geolocation.Geovisit: ...
    Visit = property(get_Visit, None)
class GeovisitTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Geolocation.IGeovisitTriggerDetails
    _classid_ = 'Windows.Devices.Geolocation.GeovisitTriggerDetails'
    @winrt_mixinmethod
    def ReadReports(self: Windows.Devices.Geolocation.IGeovisitTriggerDetails) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Geolocation.Geovisit]: ...
class ICivicAddress(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.ICivicAddress'
    _iid_ = Guid('{a8567a1a-64f4-4d48-bcea-f6b008eca34c}')
    @winrt_commethod(6)
    def get_Country(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_State(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_City(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_PostalCode(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    Country = property(get_Country, None)
    State = property(get_State, None)
    City = property(get_City, None)
    PostalCode = property(get_PostalCode, None)
    Timestamp = property(get_Timestamp, None)
class IGeoboundingBox(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeoboundingBox'
    _iid_ = Guid('{0896c80b-274f-43da-9a06-cbfcdaeb4ec2}')
    @winrt_commethod(6)
    def get_NorthwestCorner(self) -> Windows.Devices.Geolocation.BasicGeoposition: ...
    @winrt_commethod(7)
    def get_SoutheastCorner(self) -> Windows.Devices.Geolocation.BasicGeoposition: ...
    @winrt_commethod(8)
    def get_Center(self) -> Windows.Devices.Geolocation.BasicGeoposition: ...
    @winrt_commethod(9)
    def get_MinAltitude(self) -> Double: ...
    @winrt_commethod(10)
    def get_MaxAltitude(self) -> Double: ...
    NorthwestCorner = property(get_NorthwestCorner, None)
    SoutheastCorner = property(get_SoutheastCorner, None)
    Center = property(get_Center, None)
    MinAltitude = property(get_MinAltitude, None)
    MaxAltitude = property(get_MaxAltitude, None)
class IGeoboundingBoxFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeoboundingBoxFactory'
    _iid_ = Guid('{4dfba589-0411-4abc-b3b5-5bbccb57d98c}')
    @winrt_commethod(6)
    def Create(self, northwestCorner: Windows.Devices.Geolocation.BasicGeoposition, southeastCorner: Windows.Devices.Geolocation.BasicGeoposition) -> Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_commethod(7)
    def CreateWithAltitudeReference(self, northwestCorner: Windows.Devices.Geolocation.BasicGeoposition, southeastCorner: Windows.Devices.Geolocation.BasicGeoposition, altitudeReferenceSystem: Windows.Devices.Geolocation.AltitudeReferenceSystem) -> Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_commethod(8)
    def CreateWithAltitudeReferenceAndSpatialReference(self, northwestCorner: Windows.Devices.Geolocation.BasicGeoposition, southeastCorner: Windows.Devices.Geolocation.BasicGeoposition, altitudeReferenceSystem: Windows.Devices.Geolocation.AltitudeReferenceSystem, spatialReferenceId: UInt32) -> Windows.Devices.Geolocation.GeoboundingBox: ...
class IGeoboundingBoxStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeoboundingBoxStatics'
    _iid_ = Guid('{67b80708-e61a-4cd0-841b-93233792b5ca}')
    @winrt_commethod(6)
    def TryCompute(self, positions: Windows.Foundation.Collections.IIterable[Windows.Devices.Geolocation.BasicGeoposition]) -> Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_commethod(7)
    def TryComputeWithAltitudeReference(self, positions: Windows.Foundation.Collections.IIterable[Windows.Devices.Geolocation.BasicGeoposition], altitudeRefSystem: Windows.Devices.Geolocation.AltitudeReferenceSystem) -> Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_commethod(8)
    def TryComputeWithAltitudeReferenceAndSpatialReference(self, positions: Windows.Foundation.Collections.IIterable[Windows.Devices.Geolocation.BasicGeoposition], altitudeRefSystem: Windows.Devices.Geolocation.AltitudeReferenceSystem, spatialReferenceId: UInt32) -> Windows.Devices.Geolocation.GeoboundingBox: ...
class IGeocircle(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeocircle'
    _iid_ = Guid('{39e45843-a7f9-4e63-92a7-ba0c28d124b1}')
    @winrt_commethod(6)
    def get_Center(self) -> Windows.Devices.Geolocation.BasicGeoposition: ...
    @winrt_commethod(7)
    def get_Radius(self) -> Double: ...
    Center = property(get_Center, None)
    Radius = property(get_Radius, None)
class IGeocircleFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeocircleFactory'
    _iid_ = Guid('{afd6531f-72b1-4f7d-87cc-4ed4c9849c05}')
    @winrt_commethod(6)
    def Create(self, position: Windows.Devices.Geolocation.BasicGeoposition, radius: Double) -> Windows.Devices.Geolocation.Geocircle: ...
    @winrt_commethod(7)
    def CreateWithAltitudeReferenceSystem(self, position: Windows.Devices.Geolocation.BasicGeoposition, radius: Double, altitudeReferenceSystem: Windows.Devices.Geolocation.AltitudeReferenceSystem) -> Windows.Devices.Geolocation.Geocircle: ...
    @winrt_commethod(8)
    def CreateWithAltitudeReferenceSystemAndSpatialReferenceId(self, position: Windows.Devices.Geolocation.BasicGeoposition, radius: Double, altitudeReferenceSystem: Windows.Devices.Geolocation.AltitudeReferenceSystem, spatialReferenceId: UInt32) -> Windows.Devices.Geolocation.Geocircle: ...
class IGeocoordinate(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeocoordinate'
    _iid_ = Guid('{ee21a3aa-976a-4c70-803d-083ea55bcbc4}')
    @winrt_commethod(6)
    def get_Latitude(self) -> Double: ...
    @winrt_commethod(7)
    def get_Longitude(self) -> Double: ...
    @winrt_commethod(8)
    def get_Altitude(self) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(9)
    def get_Accuracy(self) -> Double: ...
    @winrt_commethod(10)
    def get_AltitudeAccuracy(self) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(11)
    def get_Heading(self) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(12)
    def get_Speed(self) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(13)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    Latitude = property(get_Latitude, None)
    Longitude = property(get_Longitude, None)
    Altitude = property(get_Altitude, None)
    Accuracy = property(get_Accuracy, None)
    AltitudeAccuracy = property(get_AltitudeAccuracy, None)
    Heading = property(get_Heading, None)
    Speed = property(get_Speed, None)
    Timestamp = property(get_Timestamp, None)
class IGeocoordinateSatelliteData(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeocoordinateSatelliteData'
    _iid_ = Guid('{c32a74d9-2608-474c-912c-06dd490f4af7}')
    @winrt_commethod(6)
    def get_PositionDilutionOfPrecision(self) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(7)
    def get_HorizontalDilutionOfPrecision(self) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(8)
    def get_VerticalDilutionOfPrecision(self) -> Windows.Foundation.IReference[Double]: ...
    PositionDilutionOfPrecision = property(get_PositionDilutionOfPrecision, None)
    HorizontalDilutionOfPrecision = property(get_HorizontalDilutionOfPrecision, None)
    VerticalDilutionOfPrecision = property(get_VerticalDilutionOfPrecision, None)
class IGeocoordinateSatelliteData2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeocoordinateSatelliteData2'
    _iid_ = Guid('{761c8cfd-a19d-5a51-80f5-71676115483e}')
    @winrt_commethod(6)
    def get_GeometricDilutionOfPrecision(self) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(7)
    def get_TimeDilutionOfPrecision(self) -> Windows.Foundation.IReference[Double]: ...
    GeometricDilutionOfPrecision = property(get_GeometricDilutionOfPrecision, None)
    TimeDilutionOfPrecision = property(get_TimeDilutionOfPrecision, None)
class IGeocoordinateWithPoint(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeocoordinateWithPoint'
    _iid_ = Guid('{feea0525-d22c-4d46-b527-0b96066fc7db}')
    @winrt_commethod(6)
    def get_Point(self) -> Windows.Devices.Geolocation.Geopoint: ...
    Point = property(get_Point, None)
class IGeocoordinateWithPositionData(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeocoordinateWithPositionData'
    _iid_ = Guid('{95e634be-dbd6-40ac-b8f2-a65c0340d9a6}')
    @winrt_commethod(6)
    def get_PositionSource(self) -> Windows.Devices.Geolocation.PositionSource: ...
    @winrt_commethod(7)
    def get_SatelliteData(self) -> Windows.Devices.Geolocation.GeocoordinateSatelliteData: ...
    PositionSource = property(get_PositionSource, None)
    SatelliteData = property(get_SatelliteData, None)
class IGeocoordinateWithPositionSourceTimestamp(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeocoordinateWithPositionSourceTimestamp'
    _iid_ = Guid('{8543fc02-c9f1-4610-afe0-8bc3a6a87036}')
    @winrt_commethod(6)
    def get_PositionSourceTimestamp(self) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    PositionSourceTimestamp = property(get_PositionSourceTimestamp, None)
class IGeocoordinateWithRemoteSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeocoordinateWithRemoteSource'
    _iid_ = Guid('{397cebd7-ee38-5f3b-8900-c4a7bc9cf953}')
    @winrt_commethod(6)
    def get_IsRemoteSource(self) -> Boolean: ...
    IsRemoteSource = property(get_IsRemoteSource, None)
class IGeolocator(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeolocator'
    _iid_ = Guid('{a9c3bf62-4524-4989-8aa9-de019d2e551f}')
    @winrt_commethod(6)
    def get_DesiredAccuracy(self) -> Windows.Devices.Geolocation.PositionAccuracy: ...
    @winrt_commethod(7)
    def put_DesiredAccuracy(self, value: Windows.Devices.Geolocation.PositionAccuracy) -> Void: ...
    @winrt_commethod(8)
    def get_MovementThreshold(self) -> Double: ...
    @winrt_commethod(9)
    def put_MovementThreshold(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_ReportInterval(self) -> UInt32: ...
    @winrt_commethod(11)
    def put_ReportInterval(self, value: UInt32) -> Void: ...
    @winrt_commethod(12)
    def get_LocationStatus(self) -> Windows.Devices.Geolocation.PositionStatus: ...
    @winrt_commethod(13)
    def GetGeopositionAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Geolocation.Geoposition]: ...
    @winrt_commethod(14)
    def GetGeopositionAsyncWithAgeAndTimeout(self, maximumAge: Windows.Foundation.TimeSpan, timeout: Windows.Foundation.TimeSpan) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Geolocation.Geoposition]: ...
    @winrt_commethod(15)
    def add_PositionChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Geolocation.Geolocator, Windows.Devices.Geolocation.PositionChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_PositionChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_StatusChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Geolocation.Geolocator, Windows.Devices.Geolocation.StatusChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_StatusChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    DesiredAccuracy = property(get_DesiredAccuracy, put_DesiredAccuracy)
    MovementThreshold = property(get_MovementThreshold, put_MovementThreshold)
    ReportInterval = property(get_ReportInterval, put_ReportInterval)
    LocationStatus = property(get_LocationStatus, None)
class IGeolocator2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeolocator2'
    _iid_ = Guid('{d1b42e6d-8891-43b4-ad36-27c6fe9a97b1}')
    @winrt_commethod(6)
    def AllowFallbackToConsentlessPositions(self) -> Void: ...
class IGeolocatorStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeolocatorStatics'
    _iid_ = Guid('{9a8e7571-2df5-4591-9f87-eb5fd894e9b7}')
    @winrt_commethod(6)
    def RequestAccessAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Geolocation.GeolocationAccessStatus]: ...
    @winrt_commethod(7)
    def GetGeopositionHistoryAsync(self, startTime: Windows.Foundation.DateTime) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Geolocation.Geoposition]]: ...
    @winrt_commethod(8)
    def GetGeopositionHistoryWithDurationAsync(self, startTime: Windows.Foundation.DateTime, duration: Windows.Foundation.TimeSpan) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.Devices.Geolocation.Geoposition]]: ...
class IGeolocatorStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeolocatorStatics2'
    _iid_ = Guid('{993011a2-fa1c-4631-a71d-0dbeb1250d9c}')
    @winrt_commethod(6)
    def get_IsDefaultGeopositionRecommended(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_DefaultGeoposition(self, value: Windows.Foundation.IReference[Windows.Devices.Geolocation.BasicGeoposition]) -> Void: ...
    @winrt_commethod(8)
    def get_DefaultGeoposition(self) -> Windows.Foundation.IReference[Windows.Devices.Geolocation.BasicGeoposition]: ...
    IsDefaultGeopositionRecommended = property(get_IsDefaultGeopositionRecommended, None)
    DefaultGeoposition = property(get_DefaultGeoposition, put_DefaultGeoposition)
class IGeolocatorWithScalarAccuracy(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeolocatorWithScalarAccuracy'
    _iid_ = Guid('{96f5d3c1-b80f-460a-994d-a96c47a51aa4}')
    @winrt_commethod(6)
    def get_DesiredAccuracyInMeters(self) -> Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(7)
    def put_DesiredAccuracyInMeters(self, value: Windows.Foundation.IReference[UInt32]) -> Void: ...
    DesiredAccuracyInMeters = property(get_DesiredAccuracyInMeters, put_DesiredAccuracyInMeters)
class IGeopath(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeopath'
    _iid_ = Guid('{e53fd7b9-2da4-4714-a652-de8593289898}')
    @winrt_commethod(6)
    def get_Positions(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Geolocation.BasicGeoposition]: ...
    Positions = property(get_Positions, None)
class IGeopathFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeopathFactory'
    _iid_ = Guid('{27bea9c8-c7e7-4359-9b9b-fca3e05ef593}')
    @winrt_commethod(6)
    def Create(self, positions: Windows.Foundation.Collections.IIterable[Windows.Devices.Geolocation.BasicGeoposition]) -> Windows.Devices.Geolocation.Geopath: ...
    @winrt_commethod(7)
    def CreateWithAltitudeReference(self, positions: Windows.Foundation.Collections.IIterable[Windows.Devices.Geolocation.BasicGeoposition], altitudeReferenceSystem: Windows.Devices.Geolocation.AltitudeReferenceSystem) -> Windows.Devices.Geolocation.Geopath: ...
    @winrt_commethod(8)
    def CreateWithAltitudeReferenceAndSpatialReference(self, positions: Windows.Foundation.Collections.IIterable[Windows.Devices.Geolocation.BasicGeoposition], altitudeReferenceSystem: Windows.Devices.Geolocation.AltitudeReferenceSystem, spatialReferenceId: UInt32) -> Windows.Devices.Geolocation.Geopath: ...
class IGeopoint(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeopoint'
    _iid_ = Guid('{6bfa00eb-e56e-49bb-9caf-cbaa78a8bcef}')
    @winrt_commethod(6)
    def get_Position(self) -> Windows.Devices.Geolocation.BasicGeoposition: ...
    Position = property(get_Position, None)
class IGeopointFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeopointFactory'
    _iid_ = Guid('{db6b8d33-76bd-4e30-8af7-a844dc37b7a0}')
    @winrt_commethod(6)
    def Create(self, position: Windows.Devices.Geolocation.BasicGeoposition) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(7)
    def CreateWithAltitudeReferenceSystem(self, position: Windows.Devices.Geolocation.BasicGeoposition, altitudeReferenceSystem: Windows.Devices.Geolocation.AltitudeReferenceSystem) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(8)
    def CreateWithAltitudeReferenceSystemAndSpatialReferenceId(self, position: Windows.Devices.Geolocation.BasicGeoposition, altitudeReferenceSystem: Windows.Devices.Geolocation.AltitudeReferenceSystem, spatialReferenceId: UInt32) -> Windows.Devices.Geolocation.Geopoint: ...
class IGeoposition(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeoposition'
    _iid_ = Guid('{c18d0454-7d41-4ff7-a957-9dffb4ef7f5b}')
    @winrt_commethod(6)
    def get_Coordinate(self) -> Windows.Devices.Geolocation.Geocoordinate: ...
    @winrt_commethod(7)
    def get_CivicAddress(self) -> Windows.Devices.Geolocation.CivicAddress: ...
    Coordinate = property(get_Coordinate, None)
    CivicAddress = property(get_CivicAddress, None)
class IGeoposition2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeoposition2'
    _iid_ = Guid('{7f62f697-8671-4b0d-86f8-474a8496187c}')
    @winrt_commethod(6)
    def get_VenueData(self) -> Windows.Devices.Geolocation.VenueData: ...
    VenueData = property(get_VenueData, None)
class IGeoshape(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeoshape'
    _iid_ = Guid('{c99ca2af-c729-43c1-8fab-d6dec914df7e}')
    @winrt_commethod(6)
    def get_GeoshapeType(self) -> Windows.Devices.Geolocation.GeoshapeType: ...
    @winrt_commethod(7)
    def get_SpatialReferenceId(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_AltitudeReferenceSystem(self) -> Windows.Devices.Geolocation.AltitudeReferenceSystem: ...
    GeoshapeType = property(get_GeoshapeType, None)
    SpatialReferenceId = property(get_SpatialReferenceId, None)
    AltitudeReferenceSystem = property(get_AltitudeReferenceSystem, None)
class IGeovisit(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeovisit'
    _iid_ = Guid('{b1877a76-9ef6-41ab-a0dd-793ece76e2de}')
    @winrt_commethod(6)
    def get_Position(self) -> Windows.Devices.Geolocation.Geoposition: ...
    @winrt_commethod(7)
    def get_StateChange(self) -> Windows.Devices.Geolocation.VisitStateChange: ...
    @winrt_commethod(8)
    def get_Timestamp(self) -> Windows.Foundation.DateTime: ...
    Position = property(get_Position, None)
    StateChange = property(get_StateChange, None)
    Timestamp = property(get_Timestamp, None)
class IGeovisitMonitor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeovisitMonitor'
    _iid_ = Guid('{80118aaf-5944-4591-83c1-396647f54f2c}')
    @winrt_commethod(6)
    def get_MonitoringScope(self) -> Windows.Devices.Geolocation.VisitMonitoringScope: ...
    @winrt_commethod(7)
    def Start(self, value: Windows.Devices.Geolocation.VisitMonitoringScope) -> Void: ...
    @winrt_commethod(8)
    def Stop(self) -> Void: ...
    @winrt_commethod(9)
    def add_VisitStateChanged(self, handler: Windows.Foundation.TypedEventHandler[Windows.Devices.Geolocation.GeovisitMonitor, Windows.Devices.Geolocation.GeovisitStateChangedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_VisitStateChanged(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    MonitoringScope = property(get_MonitoringScope, None)
class IGeovisitMonitorStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeovisitMonitorStatics'
    _iid_ = Guid('{bcf976a7-bbf2-4cdd-95cf-554c82edfb87}')
    @winrt_commethod(6)
    def GetLastReportAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Devices.Geolocation.Geovisit]: ...
class IGeovisitStateChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeovisitStateChangedEventArgs'
    _iid_ = Guid('{ceb4d1ff-8b53-4968-beed-4cecd029ce15}')
    @winrt_commethod(6)
    def get_Visit(self) -> Windows.Devices.Geolocation.Geovisit: ...
    Visit = property(get_Visit, None)
class IGeovisitTriggerDetails(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeovisitTriggerDetails'
    _iid_ = Guid('{ea770d9e-d1c9-454b-99b7-b2f8cdd2482f}')
    @winrt_commethod(6)
    def ReadReports(self) -> Windows.Foundation.Collections.IVectorView[Windows.Devices.Geolocation.Geovisit]: ...
class IPositionChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IPositionChangedEventArgs'
    _iid_ = Guid('{37859ce5-9d1e-46c5-bf3b-6ad8cac1a093}')
    @winrt_commethod(6)
    def get_Position(self) -> Windows.Devices.Geolocation.Geoposition: ...
    Position = property(get_Position, None)
class IStatusChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IStatusChangedEventArgs'
    _iid_ = Guid('{3453d2da-8c93-4111-a205-9aecfc9be5c0}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.Devices.Geolocation.PositionStatus: ...
    Status = property(get_Status, None)
class IVenueData(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IVenueData'
    _iid_ = Guid('{66f39187-60e3-4b2f-b527-4f53f1c3c677}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Level(self) -> WinRT_String: ...
    Id = property(get_Id, None)
    Level = property(get_Level, None)
PositionAccuracy = Int32
PositionAccuracy_Default: PositionAccuracy = 0
PositionAccuracy_High: PositionAccuracy = 1
class PositionChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Geolocation.IPositionChangedEventArgs
    _classid_ = 'Windows.Devices.Geolocation.PositionChangedEventArgs'
    @winrt_mixinmethod
    def get_Position(self: Windows.Devices.Geolocation.IPositionChangedEventArgs) -> Windows.Devices.Geolocation.Geoposition: ...
    Position = property(get_Position, None)
PositionSource = Int32
PositionSource_Cellular: PositionSource = 0
PositionSource_Satellite: PositionSource = 1
PositionSource_WiFi: PositionSource = 2
PositionSource_IPAddress: PositionSource = 3
PositionSource_Unknown: PositionSource = 4
PositionSource_Default: PositionSource = 5
PositionSource_Obfuscated: PositionSource = 6
PositionStatus = Int32
PositionStatus_Ready: PositionStatus = 0
PositionStatus_Initializing: PositionStatus = 1
PositionStatus_NoData: PositionStatus = 2
PositionStatus_Disabled: PositionStatus = 3
PositionStatus_NotInitialized: PositionStatus = 4
PositionStatus_NotAvailable: PositionStatus = 5
class StatusChangedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Geolocation.IStatusChangedEventArgs
    _classid_ = 'Windows.Devices.Geolocation.StatusChangedEventArgs'
    @winrt_mixinmethod
    def get_Status(self: Windows.Devices.Geolocation.IStatusChangedEventArgs) -> Windows.Devices.Geolocation.PositionStatus: ...
    Status = property(get_Status, None)
class VenueData(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Devices.Geolocation.IVenueData
    _classid_ = 'Windows.Devices.Geolocation.VenueData'
    @winrt_mixinmethod
    def get_Id(self: Windows.Devices.Geolocation.IVenueData) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Level(self: Windows.Devices.Geolocation.IVenueData) -> WinRT_String: ...
    Id = property(get_Id, None)
    Level = property(get_Level, None)
VisitMonitoringScope = Int32
VisitMonitoringScope_Venue: VisitMonitoringScope = 0
VisitMonitoringScope_City: VisitMonitoringScope = 1
VisitStateChange = Int32
VisitStateChange_TrackingLost: VisitStateChange = 0
VisitStateChange_Arrived: VisitStateChange = 1
VisitStateChange_Departed: VisitStateChange = 2
VisitStateChange_OtherMovement: VisitStateChange = 3
make_head(_module, 'BasicGeoposition')
make_head(_module, 'CivicAddress')
make_head(_module, 'GeoboundingBox')
make_head(_module, 'Geocircle')
make_head(_module, 'Geocoordinate')
make_head(_module, 'GeocoordinateSatelliteData')
make_head(_module, 'Geolocator')
make_head(_module, 'Geopath')
make_head(_module, 'Geopoint')
make_head(_module, 'Geoposition')
make_head(_module, 'Geovisit')
make_head(_module, 'GeovisitMonitor')
make_head(_module, 'GeovisitStateChangedEventArgs')
make_head(_module, 'GeovisitTriggerDetails')
make_head(_module, 'ICivicAddress')
make_head(_module, 'IGeoboundingBox')
make_head(_module, 'IGeoboundingBoxFactory')
make_head(_module, 'IGeoboundingBoxStatics')
make_head(_module, 'IGeocircle')
make_head(_module, 'IGeocircleFactory')
make_head(_module, 'IGeocoordinate')
make_head(_module, 'IGeocoordinateSatelliteData')
make_head(_module, 'IGeocoordinateSatelliteData2')
make_head(_module, 'IGeocoordinateWithPoint')
make_head(_module, 'IGeocoordinateWithPositionData')
make_head(_module, 'IGeocoordinateWithPositionSourceTimestamp')
make_head(_module, 'IGeocoordinateWithRemoteSource')
make_head(_module, 'IGeolocator')
make_head(_module, 'IGeolocator2')
make_head(_module, 'IGeolocatorStatics')
make_head(_module, 'IGeolocatorStatics2')
make_head(_module, 'IGeolocatorWithScalarAccuracy')
make_head(_module, 'IGeopath')
make_head(_module, 'IGeopathFactory')
make_head(_module, 'IGeopoint')
make_head(_module, 'IGeopointFactory')
make_head(_module, 'IGeoposition')
make_head(_module, 'IGeoposition2')
make_head(_module, 'IGeoshape')
make_head(_module, 'IGeovisit')
make_head(_module, 'IGeovisitMonitor')
make_head(_module, 'IGeovisitMonitorStatics')
make_head(_module, 'IGeovisitStateChangedEventArgs')
make_head(_module, 'IGeovisitTriggerDetails')
make_head(_module, 'IPositionChangedEventArgs')
make_head(_module, 'IStatusChangedEventArgs')
make_head(_module, 'IVenueData')
make_head(_module, 'PositionChangedEventArgs')
make_head(_module, 'StatusChangedEventArgs')
make_head(_module, 'VenueData')
