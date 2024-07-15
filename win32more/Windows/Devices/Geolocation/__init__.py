from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Geolocation
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Win32.System.WinRT
class AltitudeReferenceSystem(Enum, Int32):
    Unspecified = 0
    Terrain = 1
    Ellipsoid = 2
    Geoid = 3
    Surface = 4
class BasicGeoposition(Structure):
    Latitude: Double
    Longitude: Double
    Altitude: Double
class CivicAddress(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Geolocation.ICivicAddress
    _classid_ = 'Windows.Devices.Geolocation.CivicAddress'
    @winrt_mixinmethod
    def get_Country(self: win32more.Windows.Devices.Geolocation.ICivicAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.Devices.Geolocation.ICivicAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_City(self: win32more.Windows.Devices.Geolocation.ICivicAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PostalCode(self: win32more.Windows.Devices.Geolocation.ICivicAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.Geolocation.ICivicAddress) -> win32more.Windows.Foundation.DateTime: ...
    City = property(get_City, None)
    Country = property(get_Country, None)
    PostalCode = property(get_PostalCode, None)
    State = property(get_State, None)
    Timestamp = property(get_Timestamp, None)
class GeoboundingBox(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Geolocation.IGeoboundingBox
    _classid_ = 'Windows.Devices.Geolocation.GeoboundingBox'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Devices.Geolocation.GeoboundingBox.Create(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Devices.Geolocation.GeoboundingBox.CreateWithAltitudeReference(*args))
        elif len(args) == 4:
            super().__init__(move=win32more.Windows.Devices.Geolocation.GeoboundingBox.CreateWithAltitudeReferenceAndSpatialReference(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.Geolocation.IGeoboundingBoxFactory, northwestCorner: win32more.Windows.Devices.Geolocation.BasicGeoposition, southeastCorner: win32more.Windows.Devices.Geolocation.BasicGeoposition) -> win32more.Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_factorymethod
    def CreateWithAltitudeReference(cls: win32more.Windows.Devices.Geolocation.IGeoboundingBoxFactory, northwestCorner: win32more.Windows.Devices.Geolocation.BasicGeoposition, southeastCorner: win32more.Windows.Devices.Geolocation.BasicGeoposition, altitudeReferenceSystem: win32more.Windows.Devices.Geolocation.AltitudeReferenceSystem) -> win32more.Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_factorymethod
    def CreateWithAltitudeReferenceAndSpatialReference(cls: win32more.Windows.Devices.Geolocation.IGeoboundingBoxFactory, northwestCorner: win32more.Windows.Devices.Geolocation.BasicGeoposition, southeastCorner: win32more.Windows.Devices.Geolocation.BasicGeoposition, altitudeReferenceSystem: win32more.Windows.Devices.Geolocation.AltitudeReferenceSystem, spatialReferenceId: UInt32) -> win32more.Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_mixinmethod
    def get_NorthwestCorner(self: win32more.Windows.Devices.Geolocation.IGeoboundingBox) -> win32more.Windows.Devices.Geolocation.BasicGeoposition: ...
    @winrt_mixinmethod
    def get_SoutheastCorner(self: win32more.Windows.Devices.Geolocation.IGeoboundingBox) -> win32more.Windows.Devices.Geolocation.BasicGeoposition: ...
    @winrt_mixinmethod
    def get_Center(self: win32more.Windows.Devices.Geolocation.IGeoboundingBox) -> win32more.Windows.Devices.Geolocation.BasicGeoposition: ...
    @winrt_mixinmethod
    def get_MinAltitude(self: win32more.Windows.Devices.Geolocation.IGeoboundingBox) -> Double: ...
    @winrt_mixinmethod
    def get_MaxAltitude(self: win32more.Windows.Devices.Geolocation.IGeoboundingBox) -> Double: ...
    @winrt_mixinmethod
    def get_GeoshapeType(self: win32more.Windows.Devices.Geolocation.IGeoshape) -> win32more.Windows.Devices.Geolocation.GeoshapeType: ...
    @winrt_mixinmethod
    def get_SpatialReferenceId(self: win32more.Windows.Devices.Geolocation.IGeoshape) -> UInt32: ...
    @winrt_mixinmethod
    def get_AltitudeReferenceSystem(self: win32more.Windows.Devices.Geolocation.IGeoshape) -> win32more.Windows.Devices.Geolocation.AltitudeReferenceSystem: ...
    @winrt_classmethod
    def TryCompute(cls: win32more.Windows.Devices.Geolocation.IGeoboundingBoxStatics, positions: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Geolocation.BasicGeoposition]) -> win32more.Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_classmethod
    def TryComputeWithAltitudeReference(cls: win32more.Windows.Devices.Geolocation.IGeoboundingBoxStatics, positions: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Geolocation.BasicGeoposition], altitudeRefSystem: win32more.Windows.Devices.Geolocation.AltitudeReferenceSystem) -> win32more.Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_classmethod
    def TryComputeWithAltitudeReferenceAndSpatialReference(cls: win32more.Windows.Devices.Geolocation.IGeoboundingBoxStatics, positions: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Geolocation.BasicGeoposition], altitudeRefSystem: win32more.Windows.Devices.Geolocation.AltitudeReferenceSystem, spatialReferenceId: UInt32) -> win32more.Windows.Devices.Geolocation.GeoboundingBox: ...
    AltitudeReferenceSystem = property(get_AltitudeReferenceSystem, None)
    Center = property(get_Center, None)
    GeoshapeType = property(get_GeoshapeType, None)
    MaxAltitude = property(get_MaxAltitude, None)
    MinAltitude = property(get_MinAltitude, None)
    NorthwestCorner = property(get_NorthwestCorner, None)
    SoutheastCorner = property(get_SoutheastCorner, None)
    SpatialReferenceId = property(get_SpatialReferenceId, None)
class Geocircle(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Geolocation.IGeocircle
    _classid_ = 'Windows.Devices.Geolocation.Geocircle'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Devices.Geolocation.Geocircle.Create(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Devices.Geolocation.Geocircle.CreateWithAltitudeReferenceSystem(*args))
        elif len(args) == 4:
            super().__init__(move=win32more.Windows.Devices.Geolocation.Geocircle.CreateWithAltitudeReferenceSystemAndSpatialReferenceId(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.Geolocation.IGeocircleFactory, position: win32more.Windows.Devices.Geolocation.BasicGeoposition, radius: Double) -> win32more.Windows.Devices.Geolocation.Geocircle: ...
    @winrt_factorymethod
    def CreateWithAltitudeReferenceSystem(cls: win32more.Windows.Devices.Geolocation.IGeocircleFactory, position: win32more.Windows.Devices.Geolocation.BasicGeoposition, radius: Double, altitudeReferenceSystem: win32more.Windows.Devices.Geolocation.AltitudeReferenceSystem) -> win32more.Windows.Devices.Geolocation.Geocircle: ...
    @winrt_factorymethod
    def CreateWithAltitudeReferenceSystemAndSpatialReferenceId(cls: win32more.Windows.Devices.Geolocation.IGeocircleFactory, position: win32more.Windows.Devices.Geolocation.BasicGeoposition, radius: Double, altitudeReferenceSystem: win32more.Windows.Devices.Geolocation.AltitudeReferenceSystem, spatialReferenceId: UInt32) -> win32more.Windows.Devices.Geolocation.Geocircle: ...
    @winrt_mixinmethod
    def get_Center(self: win32more.Windows.Devices.Geolocation.IGeocircle) -> win32more.Windows.Devices.Geolocation.BasicGeoposition: ...
    @winrt_mixinmethod
    def get_Radius(self: win32more.Windows.Devices.Geolocation.IGeocircle) -> Double: ...
    @winrt_mixinmethod
    def get_GeoshapeType(self: win32more.Windows.Devices.Geolocation.IGeoshape) -> win32more.Windows.Devices.Geolocation.GeoshapeType: ...
    @winrt_mixinmethod
    def get_SpatialReferenceId(self: win32more.Windows.Devices.Geolocation.IGeoshape) -> UInt32: ...
    @winrt_mixinmethod
    def get_AltitudeReferenceSystem(self: win32more.Windows.Devices.Geolocation.IGeoshape) -> win32more.Windows.Devices.Geolocation.AltitudeReferenceSystem: ...
    AltitudeReferenceSystem = property(get_AltitudeReferenceSystem, None)
    Center = property(get_Center, None)
    GeoshapeType = property(get_GeoshapeType, None)
    Radius = property(get_Radius, None)
    SpatialReferenceId = property(get_SpatialReferenceId, None)
class Geocoordinate(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Geolocation.IGeocoordinate
    _classid_ = 'Windows.Devices.Geolocation.Geocoordinate'
    @winrt_mixinmethod
    def get_Latitude(self: win32more.Windows.Devices.Geolocation.IGeocoordinate) -> Double: ...
    @winrt_mixinmethod
    def get_Longitude(self: win32more.Windows.Devices.Geolocation.IGeocoordinate) -> Double: ...
    @winrt_mixinmethod
    def get_Altitude(self: win32more.Windows.Devices.Geolocation.IGeocoordinate) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_Accuracy(self: win32more.Windows.Devices.Geolocation.IGeocoordinate) -> Double: ...
    @winrt_mixinmethod
    def get_AltitudeAccuracy(self: win32more.Windows.Devices.Geolocation.IGeocoordinate) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_Heading(self: win32more.Windows.Devices.Geolocation.IGeocoordinate) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_Speed(self: win32more.Windows.Devices.Geolocation.IGeocoordinate) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.Geolocation.IGeocoordinate) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_PositionSource(self: win32more.Windows.Devices.Geolocation.IGeocoordinateWithPositionData) -> win32more.Windows.Devices.Geolocation.PositionSource: ...
    @winrt_mixinmethod
    def get_SatelliteData(self: win32more.Windows.Devices.Geolocation.IGeocoordinateWithPositionData) -> win32more.Windows.Devices.Geolocation.GeocoordinateSatelliteData: ...
    @winrt_mixinmethod
    def get_Point(self: win32more.Windows.Devices.Geolocation.IGeocoordinateWithPoint) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_PositionSourceTimestamp(self: win32more.Windows.Devices.Geolocation.IGeocoordinateWithPositionSourceTimestamp) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def get_IsRemoteSource(self: win32more.Windows.Devices.Geolocation.IGeocoordinateWithRemoteSource) -> Boolean: ...
    Accuracy = property(get_Accuracy, None)
    Altitude = property(get_Altitude, None)
    AltitudeAccuracy = property(get_AltitudeAccuracy, None)
    Heading = property(get_Heading, None)
    IsRemoteSource = property(get_IsRemoteSource, None)
    Latitude = property(get_Latitude, None)
    Longitude = property(get_Longitude, None)
    Point = property(get_Point, None)
    PositionSource = property(get_PositionSource, None)
    PositionSourceTimestamp = property(get_PositionSourceTimestamp, None)
    SatelliteData = property(get_SatelliteData, None)
    Speed = property(get_Speed, None)
    Timestamp = property(get_Timestamp, None)
class GeocoordinateSatelliteData(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Geolocation.IGeocoordinateSatelliteData
    _classid_ = 'Windows.Devices.Geolocation.GeocoordinateSatelliteData'
    @winrt_mixinmethod
    def get_PositionDilutionOfPrecision(self: win32more.Windows.Devices.Geolocation.IGeocoordinateSatelliteData) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_HorizontalDilutionOfPrecision(self: win32more.Windows.Devices.Geolocation.IGeocoordinateSatelliteData) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_VerticalDilutionOfPrecision(self: win32more.Windows.Devices.Geolocation.IGeocoordinateSatelliteData) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_GeometricDilutionOfPrecision(self: win32more.Windows.Devices.Geolocation.IGeocoordinateSatelliteData2) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_TimeDilutionOfPrecision(self: win32more.Windows.Devices.Geolocation.IGeocoordinateSatelliteData2) -> win32more.Windows.Foundation.IReference[Double]: ...
    GeometricDilutionOfPrecision = property(get_GeometricDilutionOfPrecision, None)
    HorizontalDilutionOfPrecision = property(get_HorizontalDilutionOfPrecision, None)
    PositionDilutionOfPrecision = property(get_PositionDilutionOfPrecision, None)
    TimeDilutionOfPrecision = property(get_TimeDilutionOfPrecision, None)
    VerticalDilutionOfPrecision = property(get_VerticalDilutionOfPrecision, None)
class GeolocationAccessStatus(Enum, Int32):
    Unspecified = 0
    Allowed = 1
    Denied = 2
class _Geolocator_Meta_(ComPtr.__class__):
    pass
class Geolocator(ComPtr, metaclass=_Geolocator_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Geolocation.IGeolocator
    _classid_ = 'Windows.Devices.Geolocation.Geolocator'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.Geolocation.Geolocator.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Geolocation.Geolocator: ...
    @winrt_mixinmethod
    def get_DesiredAccuracy(self: win32more.Windows.Devices.Geolocation.IGeolocator) -> win32more.Windows.Devices.Geolocation.PositionAccuracy: ...
    @winrt_mixinmethod
    def put_DesiredAccuracy(self: win32more.Windows.Devices.Geolocation.IGeolocator, value: win32more.Windows.Devices.Geolocation.PositionAccuracy) -> Void: ...
    @winrt_mixinmethod
    def get_MovementThreshold(self: win32more.Windows.Devices.Geolocation.IGeolocator) -> Double: ...
    @winrt_mixinmethod
    def put_MovementThreshold(self: win32more.Windows.Devices.Geolocation.IGeolocator, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ReportInterval(self: win32more.Windows.Devices.Geolocation.IGeolocator) -> UInt32: ...
    @winrt_mixinmethod
    def put_ReportInterval(self: win32more.Windows.Devices.Geolocation.IGeolocator, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_LocationStatus(self: win32more.Windows.Devices.Geolocation.IGeolocator) -> win32more.Windows.Devices.Geolocation.PositionStatus: ...
    @winrt_mixinmethod
    def GetGeopositionAsync(self: win32more.Windows.Devices.Geolocation.IGeolocator) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Geolocation.Geoposition]: ...
    @winrt_mixinmethod
    def GetGeopositionAsyncWithAgeAndTimeout(self: win32more.Windows.Devices.Geolocation.IGeolocator, maximumAge: win32more.Windows.Foundation.TimeSpan, timeout: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Geolocation.Geoposition]: ...
    @winrt_mixinmethod
    def add_PositionChanged(self: win32more.Windows.Devices.Geolocation.IGeolocator, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Geolocation.Geolocator, win32more.Windows.Devices.Geolocation.PositionChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PositionChanged(self: win32more.Windows.Devices.Geolocation.IGeolocator, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_StatusChanged(self: win32more.Windows.Devices.Geolocation.IGeolocator, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Geolocation.Geolocator, win32more.Windows.Devices.Geolocation.StatusChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StatusChanged(self: win32more.Windows.Devices.Geolocation.IGeolocator, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_DesiredAccuracyInMeters(self: win32more.Windows.Devices.Geolocation.IGeolocatorWithScalarAccuracy) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_mixinmethod
    def put_DesiredAccuracyInMeters(self: win32more.Windows.Devices.Geolocation.IGeolocatorWithScalarAccuracy, value: win32more.Windows.Foundation.IReference[UInt32]) -> Void: ...
    @winrt_mixinmethod
    def AllowFallbackToConsentlessPositions(self: win32more.Windows.Devices.Geolocation.IGeolocator2) -> Void: ...
    @winrt_classmethod
    def get_IsDefaultGeopositionRecommended(cls: win32more.Windows.Devices.Geolocation.IGeolocatorStatics2) -> Boolean: ...
    @winrt_classmethod
    def put_DefaultGeoposition(cls: win32more.Windows.Devices.Geolocation.IGeolocatorStatics2, value: win32more.Windows.Foundation.IReference[win32more.Windows.Devices.Geolocation.BasicGeoposition]) -> Void: ...
    @winrt_classmethod
    def get_DefaultGeoposition(cls: win32more.Windows.Devices.Geolocation.IGeolocatorStatics2) -> win32more.Windows.Foundation.IReference[win32more.Windows.Devices.Geolocation.BasicGeoposition]: ...
    @winrt_classmethod
    def RequestAccessAsync(cls: win32more.Windows.Devices.Geolocation.IGeolocatorStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Geolocation.GeolocationAccessStatus]: ...
    @winrt_classmethod
    def GetGeopositionHistoryAsync(cls: win32more.Windows.Devices.Geolocation.IGeolocatorStatics, startTime: win32more.Windows.Foundation.DateTime) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Geolocation.Geoposition]]: ...
    @winrt_classmethod
    def GetGeopositionHistoryWithDurationAsync(cls: win32more.Windows.Devices.Geolocation.IGeolocatorStatics, startTime: win32more.Windows.Foundation.DateTime, duration: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Geolocation.Geoposition]]: ...
    DesiredAccuracy = property(get_DesiredAccuracy, put_DesiredAccuracy)
    DesiredAccuracyInMeters = property(get_DesiredAccuracyInMeters, put_DesiredAccuracyInMeters)
    LocationStatus = property(get_LocationStatus, None)
    MovementThreshold = property(get_MovementThreshold, put_MovementThreshold)
    ReportInterval = property(get_ReportInterval, put_ReportInterval)
    _Geolocator_Meta_.DefaultGeoposition = property(get_DefaultGeoposition, put_DefaultGeoposition)
    _Geolocator_Meta_.IsDefaultGeopositionRecommended = property(get_IsDefaultGeopositionRecommended, None)
    PositionChanged = event()
    StatusChanged = event()
class Geopath(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Geolocation.IGeopath
    _classid_ = 'Windows.Devices.Geolocation.Geopath'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Devices.Geolocation.Geopath.Create(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Devices.Geolocation.Geopath.CreateWithAltitudeReference(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Devices.Geolocation.Geopath.CreateWithAltitudeReferenceAndSpatialReference(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.Geolocation.IGeopathFactory, positions: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Geolocation.BasicGeoposition]) -> win32more.Windows.Devices.Geolocation.Geopath: ...
    @winrt_factorymethod
    def CreateWithAltitudeReference(cls: win32more.Windows.Devices.Geolocation.IGeopathFactory, positions: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Geolocation.BasicGeoposition], altitudeReferenceSystem: win32more.Windows.Devices.Geolocation.AltitudeReferenceSystem) -> win32more.Windows.Devices.Geolocation.Geopath: ...
    @winrt_factorymethod
    def CreateWithAltitudeReferenceAndSpatialReference(cls: win32more.Windows.Devices.Geolocation.IGeopathFactory, positions: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Geolocation.BasicGeoposition], altitudeReferenceSystem: win32more.Windows.Devices.Geolocation.AltitudeReferenceSystem, spatialReferenceId: UInt32) -> win32more.Windows.Devices.Geolocation.Geopath: ...
    @winrt_mixinmethod
    def get_Positions(self: win32more.Windows.Devices.Geolocation.IGeopath) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Geolocation.BasicGeoposition]: ...
    @winrt_mixinmethod
    def get_GeoshapeType(self: win32more.Windows.Devices.Geolocation.IGeoshape) -> win32more.Windows.Devices.Geolocation.GeoshapeType: ...
    @winrt_mixinmethod
    def get_SpatialReferenceId(self: win32more.Windows.Devices.Geolocation.IGeoshape) -> UInt32: ...
    @winrt_mixinmethod
    def get_AltitudeReferenceSystem(self: win32more.Windows.Devices.Geolocation.IGeoshape) -> win32more.Windows.Devices.Geolocation.AltitudeReferenceSystem: ...
    AltitudeReferenceSystem = property(get_AltitudeReferenceSystem, None)
    GeoshapeType = property(get_GeoshapeType, None)
    Positions = property(get_Positions, None)
    SpatialReferenceId = property(get_SpatialReferenceId, None)
class Geopoint(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Geolocation.IGeopoint
    _classid_ = 'Windows.Devices.Geolocation.Geopoint'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.Devices.Geolocation.Geopoint.Create(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Devices.Geolocation.Geopoint.CreateWithAltitudeReferenceSystem(*args))
        elif len(args) == 3:
            super().__init__(move=win32more.Windows.Devices.Geolocation.Geopoint.CreateWithAltitudeReferenceSystemAndSpatialReferenceId(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Devices.Geolocation.IGeopointFactory, position: win32more.Windows.Devices.Geolocation.BasicGeoposition) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_factorymethod
    def CreateWithAltitudeReferenceSystem(cls: win32more.Windows.Devices.Geolocation.IGeopointFactory, position: win32more.Windows.Devices.Geolocation.BasicGeoposition, altitudeReferenceSystem: win32more.Windows.Devices.Geolocation.AltitudeReferenceSystem) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_factorymethod
    def CreateWithAltitudeReferenceSystemAndSpatialReferenceId(cls: win32more.Windows.Devices.Geolocation.IGeopointFactory, position: win32more.Windows.Devices.Geolocation.BasicGeoposition, altitudeReferenceSystem: win32more.Windows.Devices.Geolocation.AltitudeReferenceSystem, spatialReferenceId: UInt32) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.Devices.Geolocation.IGeopoint) -> win32more.Windows.Devices.Geolocation.BasicGeoposition: ...
    @winrt_mixinmethod
    def get_GeoshapeType(self: win32more.Windows.Devices.Geolocation.IGeoshape) -> win32more.Windows.Devices.Geolocation.GeoshapeType: ...
    @winrt_mixinmethod
    def get_SpatialReferenceId(self: win32more.Windows.Devices.Geolocation.IGeoshape) -> UInt32: ...
    @winrt_mixinmethod
    def get_AltitudeReferenceSystem(self: win32more.Windows.Devices.Geolocation.IGeoshape) -> win32more.Windows.Devices.Geolocation.AltitudeReferenceSystem: ...
    AltitudeReferenceSystem = property(get_AltitudeReferenceSystem, None)
    GeoshapeType = property(get_GeoshapeType, None)
    Position = property(get_Position, None)
    SpatialReferenceId = property(get_SpatialReferenceId, None)
class Geoposition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Geolocation.IGeoposition
    _classid_ = 'Windows.Devices.Geolocation.Geoposition'
    @winrt_mixinmethod
    def get_Coordinate(self: win32more.Windows.Devices.Geolocation.IGeoposition) -> win32more.Windows.Devices.Geolocation.Geocoordinate: ...
    @winrt_mixinmethod
    def get_CivicAddress(self: win32more.Windows.Devices.Geolocation.IGeoposition) -> win32more.Windows.Devices.Geolocation.CivicAddress: ...
    @winrt_mixinmethod
    def get_VenueData(self: win32more.Windows.Devices.Geolocation.IGeoposition2) -> win32more.Windows.Devices.Geolocation.VenueData: ...
    CivicAddress = property(get_CivicAddress, None)
    Coordinate = property(get_Coordinate, None)
    VenueData = property(get_VenueData, None)
class GeoshapeType(Enum, Int32):
    Geopoint = 0
    Geocircle = 1
    Geopath = 2
    GeoboundingBox = 3
class Geovisit(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Geolocation.IGeovisit
    _classid_ = 'Windows.Devices.Geolocation.Geovisit'
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.Devices.Geolocation.IGeovisit) -> win32more.Windows.Devices.Geolocation.Geoposition: ...
    @winrt_mixinmethod
    def get_StateChange(self: win32more.Windows.Devices.Geolocation.IGeovisit) -> win32more.Windows.Devices.Geolocation.VisitStateChange: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.Devices.Geolocation.IGeovisit) -> win32more.Windows.Foundation.DateTime: ...
    Position = property(get_Position, None)
    StateChange = property(get_StateChange, None)
    Timestamp = property(get_Timestamp, None)
class GeovisitMonitor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Geolocation.IGeovisitMonitor
    _classid_ = 'Windows.Devices.Geolocation.GeovisitMonitor'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Devices.Geolocation.GeovisitMonitor.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Devices.Geolocation.GeovisitMonitor: ...
    @winrt_mixinmethod
    def get_MonitoringScope(self: win32more.Windows.Devices.Geolocation.IGeovisitMonitor) -> win32more.Windows.Devices.Geolocation.VisitMonitoringScope: ...
    @winrt_mixinmethod
    def Start(self: win32more.Windows.Devices.Geolocation.IGeovisitMonitor, value: win32more.Windows.Devices.Geolocation.VisitMonitoringScope) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Devices.Geolocation.IGeovisitMonitor) -> Void: ...
    @winrt_mixinmethod
    def add_VisitStateChanged(self: win32more.Windows.Devices.Geolocation.IGeovisitMonitor, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Geolocation.GeovisitMonitor, win32more.Windows.Devices.Geolocation.GeovisitStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_VisitStateChanged(self: win32more.Windows.Devices.Geolocation.IGeovisitMonitor, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetLastReportAsync(cls: win32more.Windows.Devices.Geolocation.IGeovisitMonitorStatics) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Geolocation.Geovisit]: ...
    MonitoringScope = property(get_MonitoringScope, None)
    VisitStateChanged = event()
class GeovisitStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Geolocation.IGeovisitStateChangedEventArgs
    _classid_ = 'Windows.Devices.Geolocation.GeovisitStateChangedEventArgs'
    @winrt_mixinmethod
    def get_Visit(self: win32more.Windows.Devices.Geolocation.IGeovisitStateChangedEventArgs) -> win32more.Windows.Devices.Geolocation.Geovisit: ...
    Visit = property(get_Visit, None)
class GeovisitTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Geolocation.IGeovisitTriggerDetails
    _classid_ = 'Windows.Devices.Geolocation.GeovisitTriggerDetails'
    @winrt_mixinmethod
    def ReadReports(self: win32more.Windows.Devices.Geolocation.IGeovisitTriggerDetails) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Geolocation.Geovisit]: ...
class ICivicAddress(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    def get_Timestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    City = property(get_City, None)
    Country = property(get_Country, None)
    PostalCode = property(get_PostalCode, None)
    State = property(get_State, None)
    Timestamp = property(get_Timestamp, None)
class IGeoboundingBox(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeoboundingBox'
    _iid_ = Guid('{0896c80b-274f-43da-9a06-cbfcdaeb4ec2}')
    @winrt_commethod(6)
    def get_NorthwestCorner(self) -> win32more.Windows.Devices.Geolocation.BasicGeoposition: ...
    @winrt_commethod(7)
    def get_SoutheastCorner(self) -> win32more.Windows.Devices.Geolocation.BasicGeoposition: ...
    @winrt_commethod(8)
    def get_Center(self) -> win32more.Windows.Devices.Geolocation.BasicGeoposition: ...
    @winrt_commethod(9)
    def get_MinAltitude(self) -> Double: ...
    @winrt_commethod(10)
    def get_MaxAltitude(self) -> Double: ...
    Center = property(get_Center, None)
    MaxAltitude = property(get_MaxAltitude, None)
    MinAltitude = property(get_MinAltitude, None)
    NorthwestCorner = property(get_NorthwestCorner, None)
    SoutheastCorner = property(get_SoutheastCorner, None)
class IGeoboundingBoxFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeoboundingBoxFactory'
    _iid_ = Guid('{4dfba589-0411-4abc-b3b5-5bbccb57d98c}')
    @winrt_commethod(6)
    def Create(self, northwestCorner: win32more.Windows.Devices.Geolocation.BasicGeoposition, southeastCorner: win32more.Windows.Devices.Geolocation.BasicGeoposition) -> win32more.Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_commethod(7)
    def CreateWithAltitudeReference(self, northwestCorner: win32more.Windows.Devices.Geolocation.BasicGeoposition, southeastCorner: win32more.Windows.Devices.Geolocation.BasicGeoposition, altitudeReferenceSystem: win32more.Windows.Devices.Geolocation.AltitudeReferenceSystem) -> win32more.Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_commethod(8)
    def CreateWithAltitudeReferenceAndSpatialReference(self, northwestCorner: win32more.Windows.Devices.Geolocation.BasicGeoposition, southeastCorner: win32more.Windows.Devices.Geolocation.BasicGeoposition, altitudeReferenceSystem: win32more.Windows.Devices.Geolocation.AltitudeReferenceSystem, spatialReferenceId: UInt32) -> win32more.Windows.Devices.Geolocation.GeoboundingBox: ...
class IGeoboundingBoxStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeoboundingBoxStatics'
    _iid_ = Guid('{67b80708-e61a-4cd0-841b-93233792b5ca}')
    @winrt_commethod(6)
    def TryCompute(self, positions: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Geolocation.BasicGeoposition]) -> win32more.Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_commethod(7)
    def TryComputeWithAltitudeReference(self, positions: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Geolocation.BasicGeoposition], altitudeRefSystem: win32more.Windows.Devices.Geolocation.AltitudeReferenceSystem) -> win32more.Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_commethod(8)
    def TryComputeWithAltitudeReferenceAndSpatialReference(self, positions: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Geolocation.BasicGeoposition], altitudeRefSystem: win32more.Windows.Devices.Geolocation.AltitudeReferenceSystem, spatialReferenceId: UInt32) -> win32more.Windows.Devices.Geolocation.GeoboundingBox: ...
class IGeocircle(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeocircle'
    _iid_ = Guid('{39e45843-a7f9-4e63-92a7-ba0c28d124b1}')
    @winrt_commethod(6)
    def get_Center(self) -> win32more.Windows.Devices.Geolocation.BasicGeoposition: ...
    @winrt_commethod(7)
    def get_Radius(self) -> Double: ...
    Center = property(get_Center, None)
    Radius = property(get_Radius, None)
class IGeocircleFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeocircleFactory'
    _iid_ = Guid('{afd6531f-72b1-4f7d-87cc-4ed4c9849c05}')
    @winrt_commethod(6)
    def Create(self, position: win32more.Windows.Devices.Geolocation.BasicGeoposition, radius: Double) -> win32more.Windows.Devices.Geolocation.Geocircle: ...
    @winrt_commethod(7)
    def CreateWithAltitudeReferenceSystem(self, position: win32more.Windows.Devices.Geolocation.BasicGeoposition, radius: Double, altitudeReferenceSystem: win32more.Windows.Devices.Geolocation.AltitudeReferenceSystem) -> win32more.Windows.Devices.Geolocation.Geocircle: ...
    @winrt_commethod(8)
    def CreateWithAltitudeReferenceSystemAndSpatialReferenceId(self, position: win32more.Windows.Devices.Geolocation.BasicGeoposition, radius: Double, altitudeReferenceSystem: win32more.Windows.Devices.Geolocation.AltitudeReferenceSystem, spatialReferenceId: UInt32) -> win32more.Windows.Devices.Geolocation.Geocircle: ...
class IGeocoordinate(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeocoordinate'
    _iid_ = Guid('{ee21a3aa-976a-4c70-803d-083ea55bcbc4}')
    @winrt_commethod(6)
    def get_Latitude(self) -> Double: ...
    @winrt_commethod(7)
    def get_Longitude(self) -> Double: ...
    @winrt_commethod(8)
    def get_Altitude(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(9)
    def get_Accuracy(self) -> Double: ...
    @winrt_commethod(10)
    def get_AltitudeAccuracy(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(11)
    def get_Heading(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(12)
    def get_Speed(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(13)
    def get_Timestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    Accuracy = property(get_Accuracy, None)
    Altitude = property(get_Altitude, None)
    AltitudeAccuracy = property(get_AltitudeAccuracy, None)
    Heading = property(get_Heading, None)
    Latitude = property(get_Latitude, None)
    Longitude = property(get_Longitude, None)
    Speed = property(get_Speed, None)
    Timestamp = property(get_Timestamp, None)
class IGeocoordinateSatelliteData(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeocoordinateSatelliteData'
    _iid_ = Guid('{c32a74d9-2608-474c-912c-06dd490f4af7}')
    @winrt_commethod(6)
    def get_PositionDilutionOfPrecision(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(7)
    def get_HorizontalDilutionOfPrecision(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(8)
    def get_VerticalDilutionOfPrecision(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    HorizontalDilutionOfPrecision = property(get_HorizontalDilutionOfPrecision, None)
    PositionDilutionOfPrecision = property(get_PositionDilutionOfPrecision, None)
    VerticalDilutionOfPrecision = property(get_VerticalDilutionOfPrecision, None)
class IGeocoordinateSatelliteData2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeocoordinateSatelliteData2'
    _iid_ = Guid('{761c8cfd-a19d-5a51-80f5-71676115483e}')
    @winrt_commethod(6)
    def get_GeometricDilutionOfPrecision(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(7)
    def get_TimeDilutionOfPrecision(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    GeometricDilutionOfPrecision = property(get_GeometricDilutionOfPrecision, None)
    TimeDilutionOfPrecision = property(get_TimeDilutionOfPrecision, None)
class IGeocoordinateWithPoint(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeocoordinateWithPoint'
    _iid_ = Guid('{feea0525-d22c-4d46-b527-0b96066fc7db}')
    @winrt_commethod(6)
    def get_Point(self) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    Point = property(get_Point, None)
class IGeocoordinateWithPositionData(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeocoordinateWithPositionData'
    _iid_ = Guid('{95e634be-dbd6-40ac-b8f2-a65c0340d9a6}')
    @winrt_commethod(6)
    def get_PositionSource(self) -> win32more.Windows.Devices.Geolocation.PositionSource: ...
    @winrt_commethod(7)
    def get_SatelliteData(self) -> win32more.Windows.Devices.Geolocation.GeocoordinateSatelliteData: ...
    PositionSource = property(get_PositionSource, None)
    SatelliteData = property(get_SatelliteData, None)
class IGeocoordinateWithPositionSourceTimestamp(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeocoordinateWithPositionSourceTimestamp'
    _iid_ = Guid('{8543fc02-c9f1-4610-afe0-8bc3a6a87036}')
    @winrt_commethod(6)
    def get_PositionSourceTimestamp(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    PositionSourceTimestamp = property(get_PositionSourceTimestamp, None)
class IGeocoordinateWithRemoteSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeocoordinateWithRemoteSource'
    _iid_ = Guid('{397cebd7-ee38-5f3b-8900-c4a7bc9cf953}')
    @winrt_commethod(6)
    def get_IsRemoteSource(self) -> Boolean: ...
    IsRemoteSource = property(get_IsRemoteSource, None)
class IGeolocator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeolocator'
    _iid_ = Guid('{a9c3bf62-4524-4989-8aa9-de019d2e551f}')
    @winrt_commethod(6)
    def get_DesiredAccuracy(self) -> win32more.Windows.Devices.Geolocation.PositionAccuracy: ...
    @winrt_commethod(7)
    def put_DesiredAccuracy(self, value: win32more.Windows.Devices.Geolocation.PositionAccuracy) -> Void: ...
    @winrt_commethod(8)
    def get_MovementThreshold(self) -> Double: ...
    @winrt_commethod(9)
    def put_MovementThreshold(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_ReportInterval(self) -> UInt32: ...
    @winrt_commethod(11)
    def put_ReportInterval(self, value: UInt32) -> Void: ...
    @winrt_commethod(12)
    def get_LocationStatus(self) -> win32more.Windows.Devices.Geolocation.PositionStatus: ...
    @winrt_commethod(13)
    def GetGeopositionAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Geolocation.Geoposition]: ...
    @winrt_commethod(14)
    def GetGeopositionAsyncWithAgeAndTimeout(self, maximumAge: win32more.Windows.Foundation.TimeSpan, timeout: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Geolocation.Geoposition]: ...
    @winrt_commethod(15)
    def add_PositionChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Geolocation.Geolocator, win32more.Windows.Devices.Geolocation.PositionChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_PositionChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_StatusChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Geolocation.Geolocator, win32more.Windows.Devices.Geolocation.StatusChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_StatusChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    DesiredAccuracy = property(get_DesiredAccuracy, put_DesiredAccuracy)
    LocationStatus = property(get_LocationStatus, None)
    MovementThreshold = property(get_MovementThreshold, put_MovementThreshold)
    ReportInterval = property(get_ReportInterval, put_ReportInterval)
    PositionChanged = event()
    StatusChanged = event()
class IGeolocator2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeolocator2'
    _iid_ = Guid('{d1b42e6d-8891-43b4-ad36-27c6fe9a97b1}')
    @winrt_commethod(6)
    def AllowFallbackToConsentlessPositions(self) -> Void: ...
class IGeolocatorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeolocatorStatics'
    _iid_ = Guid('{9a8e7571-2df5-4591-9f87-eb5fd894e9b7}')
    @winrt_commethod(6)
    def RequestAccessAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Geolocation.GeolocationAccessStatus]: ...
    @winrt_commethod(7)
    def GetGeopositionHistoryAsync(self, startTime: win32more.Windows.Foundation.DateTime) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Geolocation.Geoposition]]: ...
    @winrt_commethod(8)
    def GetGeopositionHistoryWithDurationAsync(self, startTime: win32more.Windows.Foundation.DateTime, duration: win32more.Windows.Foundation.TimeSpan) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Geolocation.Geoposition]]: ...
class IGeolocatorStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeolocatorStatics2'
    _iid_ = Guid('{993011a2-fa1c-4631-a71d-0dbeb1250d9c}')
    @winrt_commethod(6)
    def get_IsDefaultGeopositionRecommended(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_DefaultGeoposition(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Devices.Geolocation.BasicGeoposition]) -> Void: ...
    @winrt_commethod(8)
    def get_DefaultGeoposition(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Devices.Geolocation.BasicGeoposition]: ...
    DefaultGeoposition = property(get_DefaultGeoposition, put_DefaultGeoposition)
    IsDefaultGeopositionRecommended = property(get_IsDefaultGeopositionRecommended, None)
class IGeolocatorWithScalarAccuracy(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeolocatorWithScalarAccuracy'
    _iid_ = Guid('{96f5d3c1-b80f-460a-994d-a96c47a51aa4}')
    @winrt_commethod(6)
    def get_DesiredAccuracyInMeters(self) -> win32more.Windows.Foundation.IReference[UInt32]: ...
    @winrt_commethod(7)
    def put_DesiredAccuracyInMeters(self, value: win32more.Windows.Foundation.IReference[UInt32]) -> Void: ...
    DesiredAccuracyInMeters = property(get_DesiredAccuracyInMeters, put_DesiredAccuracyInMeters)
class IGeopath(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeopath'
    _iid_ = Guid('{e53fd7b9-2da4-4714-a652-de8593289898}')
    @winrt_commethod(6)
    def get_Positions(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Geolocation.BasicGeoposition]: ...
    Positions = property(get_Positions, None)
class IGeopathFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeopathFactory'
    _iid_ = Guid('{27bea9c8-c7e7-4359-9b9b-fca3e05ef593}')
    @winrt_commethod(6)
    def Create(self, positions: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Geolocation.BasicGeoposition]) -> win32more.Windows.Devices.Geolocation.Geopath: ...
    @winrt_commethod(7)
    def CreateWithAltitudeReference(self, positions: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Geolocation.BasicGeoposition], altitudeReferenceSystem: win32more.Windows.Devices.Geolocation.AltitudeReferenceSystem) -> win32more.Windows.Devices.Geolocation.Geopath: ...
    @winrt_commethod(8)
    def CreateWithAltitudeReferenceAndSpatialReference(self, positions: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Geolocation.BasicGeoposition], altitudeReferenceSystem: win32more.Windows.Devices.Geolocation.AltitudeReferenceSystem, spatialReferenceId: UInt32) -> win32more.Windows.Devices.Geolocation.Geopath: ...
class IGeopoint(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeopoint'
    _iid_ = Guid('{6bfa00eb-e56e-49bb-9caf-cbaa78a8bcef}')
    @winrt_commethod(6)
    def get_Position(self) -> win32more.Windows.Devices.Geolocation.BasicGeoposition: ...
    Position = property(get_Position, None)
class IGeopointFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeopointFactory'
    _iid_ = Guid('{db6b8d33-76bd-4e30-8af7-a844dc37b7a0}')
    @winrt_commethod(6)
    def Create(self, position: win32more.Windows.Devices.Geolocation.BasicGeoposition) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(7)
    def CreateWithAltitudeReferenceSystem(self, position: win32more.Windows.Devices.Geolocation.BasicGeoposition, altitudeReferenceSystem: win32more.Windows.Devices.Geolocation.AltitudeReferenceSystem) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(8)
    def CreateWithAltitudeReferenceSystemAndSpatialReferenceId(self, position: win32more.Windows.Devices.Geolocation.BasicGeoposition, altitudeReferenceSystem: win32more.Windows.Devices.Geolocation.AltitudeReferenceSystem, spatialReferenceId: UInt32) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
class IGeoposition(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeoposition'
    _iid_ = Guid('{c18d0454-7d41-4ff7-a957-9dffb4ef7f5b}')
    @winrt_commethod(6)
    def get_Coordinate(self) -> win32more.Windows.Devices.Geolocation.Geocoordinate: ...
    @winrt_commethod(7)
    def get_CivicAddress(self) -> win32more.Windows.Devices.Geolocation.CivicAddress: ...
    CivicAddress = property(get_CivicAddress, None)
    Coordinate = property(get_Coordinate, None)
class IGeoposition2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeoposition2'
    _iid_ = Guid('{7f62f697-8671-4b0d-86f8-474a8496187c}')
    @winrt_commethod(6)
    def get_VenueData(self) -> win32more.Windows.Devices.Geolocation.VenueData: ...
    VenueData = property(get_VenueData, None)
class IGeoshape(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeoshape'
    _iid_ = Guid('{c99ca2af-c729-43c1-8fab-d6dec914df7e}')
    @winrt_commethod(6)
    def get_GeoshapeType(self) -> win32more.Windows.Devices.Geolocation.GeoshapeType: ...
    @winrt_commethod(7)
    def get_SpatialReferenceId(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_AltitudeReferenceSystem(self) -> win32more.Windows.Devices.Geolocation.AltitudeReferenceSystem: ...
    AltitudeReferenceSystem = property(get_AltitudeReferenceSystem, None)
    GeoshapeType = property(get_GeoshapeType, None)
    SpatialReferenceId = property(get_SpatialReferenceId, None)
class IGeovisit(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeovisit'
    _iid_ = Guid('{b1877a76-9ef6-41ab-a0dd-793ece76e2de}')
    @winrt_commethod(6)
    def get_Position(self) -> win32more.Windows.Devices.Geolocation.Geoposition: ...
    @winrt_commethod(7)
    def get_StateChange(self) -> win32more.Windows.Devices.Geolocation.VisitStateChange: ...
    @winrt_commethod(8)
    def get_Timestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    Position = property(get_Position, None)
    StateChange = property(get_StateChange, None)
    Timestamp = property(get_Timestamp, None)
class IGeovisitMonitor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeovisitMonitor'
    _iid_ = Guid('{80118aaf-5944-4591-83c1-396647f54f2c}')
    @winrt_commethod(6)
    def get_MonitoringScope(self) -> win32more.Windows.Devices.Geolocation.VisitMonitoringScope: ...
    @winrt_commethod(7)
    def Start(self, value: win32more.Windows.Devices.Geolocation.VisitMonitoringScope) -> Void: ...
    @winrt_commethod(8)
    def Stop(self) -> Void: ...
    @winrt_commethod(9)
    def add_VisitStateChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Devices.Geolocation.GeovisitMonitor, win32more.Windows.Devices.Geolocation.GeovisitStateChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_VisitStateChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    MonitoringScope = property(get_MonitoringScope, None)
    VisitStateChanged = event()
class IGeovisitMonitorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeovisitMonitorStatics'
    _iid_ = Guid('{bcf976a7-bbf2-4cdd-95cf-554c82edfb87}')
    @winrt_commethod(6)
    def GetLastReportAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Geolocation.Geovisit]: ...
class IGeovisitStateChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeovisitStateChangedEventArgs'
    _iid_ = Guid('{ceb4d1ff-8b53-4968-beed-4cecd029ce15}')
    @winrt_commethod(6)
    def get_Visit(self) -> win32more.Windows.Devices.Geolocation.Geovisit: ...
    Visit = property(get_Visit, None)
class IGeovisitTriggerDetails(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IGeovisitTriggerDetails'
    _iid_ = Guid('{ea770d9e-d1c9-454b-99b7-b2f8cdd2482f}')
    @winrt_commethod(6)
    def ReadReports(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Devices.Geolocation.Geovisit]: ...
class IPositionChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IPositionChangedEventArgs'
    _iid_ = Guid('{37859ce5-9d1e-46c5-bf3b-6ad8cac1a093}')
    @winrt_commethod(6)
    def get_Position(self) -> win32more.Windows.Devices.Geolocation.Geoposition: ...
    Position = property(get_Position, None)
class IStatusChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IStatusChangedEventArgs'
    _iid_ = Guid('{3453d2da-8c93-4111-a205-9aecfc9be5c0}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.Devices.Geolocation.PositionStatus: ...
    Status = property(get_Status, None)
class IVenueData(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Devices.Geolocation.IVenueData'
    _iid_ = Guid('{66f39187-60e3-4b2f-b527-4f53f1c3c677}')
    @winrt_commethod(6)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Level(self) -> WinRT_String: ...
    Id = property(get_Id, None)
    Level = property(get_Level, None)
class PositionAccuracy(Enum, Int32):
    Default = 0
    High = 1
class PositionChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Geolocation.IPositionChangedEventArgs
    _classid_ = 'Windows.Devices.Geolocation.PositionChangedEventArgs'
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.Devices.Geolocation.IPositionChangedEventArgs) -> win32more.Windows.Devices.Geolocation.Geoposition: ...
    Position = property(get_Position, None)
class PositionSource(Enum, Int32):
    Cellular = 0
    Satellite = 1
    WiFi = 2
    IPAddress = 3
    Unknown = 4
    Default = 5
    Obfuscated = 6
class PositionStatus(Enum, Int32):
    Ready = 0
    Initializing = 1
    NoData = 2
    Disabled = 3
    NotInitialized = 4
    NotAvailable = 5
class StatusChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Geolocation.IStatusChangedEventArgs
    _classid_ = 'Windows.Devices.Geolocation.StatusChangedEventArgs'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Devices.Geolocation.IStatusChangedEventArgs) -> win32more.Windows.Devices.Geolocation.PositionStatus: ...
    Status = property(get_Status, None)
class VenueData(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Devices.Geolocation.IVenueData
    _classid_ = 'Windows.Devices.Geolocation.VenueData'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Devices.Geolocation.IVenueData) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Level(self: win32more.Windows.Devices.Geolocation.IVenueData) -> WinRT_String: ...
    Id = property(get_Id, None)
    Level = property(get_Level, None)
class VisitMonitoringScope(Enum, Int32):
    Venue = 0
    City = 1
class VisitStateChange(Enum, Int32):
    TrackingLost = 0
    Arrived = 1
    Departed = 2
    OtherMovement = 3


make_ready(__name__)
