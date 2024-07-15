from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Geolocation
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Services.Maps
import win32more.Windows.UI.Popups
import win32more.Windows.Win32.System.WinRT
class EnhancedWaypoint(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Maps.IEnhancedWaypoint
    _classid_ = 'Windows.Services.Maps.EnhancedWaypoint'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.Services.Maps.EnhancedWaypoint.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.Services.Maps.IEnhancedWaypointFactory, point: win32more.Windows.Devices.Geolocation.Geopoint, kind: win32more.Windows.Services.Maps.WaypointKind) -> win32more.Windows.Services.Maps.EnhancedWaypoint: ...
    @winrt_mixinmethod
    def get_Point(self: win32more.Windows.Services.Maps.IEnhancedWaypoint) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.Services.Maps.IEnhancedWaypoint) -> win32more.Windows.Services.Maps.WaypointKind: ...
    Kind = property(get_Kind, None)
    Point = property(get_Point, None)
GuidanceContract: UInt32 = 196608
class IEnhancedWaypoint(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IEnhancedWaypoint'
    _iid_ = Guid('{ed268c74-5913-11e6-8b77-86f30ca893d3}')
    @winrt_commethod(6)
    def get_Point(self) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(7)
    def get_Kind(self) -> win32more.Windows.Services.Maps.WaypointKind: ...
    Kind = property(get_Kind, None)
    Point = property(get_Point, None)
class IEnhancedWaypointFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IEnhancedWaypointFactory'
    _iid_ = Guid('{af868477-a2aa-46dd-b645-23b31b8aa6c7}')
    @winrt_commethod(6)
    def Create(self, point: win32more.Windows.Devices.Geolocation.Geopoint, kind: win32more.Windows.Services.Maps.WaypointKind) -> win32more.Windows.Services.Maps.EnhancedWaypoint: ...
class IManeuverWarning(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IManeuverWarning'
    _iid_ = Guid('{c1a36d8a-2630-4378-9e4a-6e44253dceba}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Windows.Services.Maps.ManeuverWarningKind: ...
    @winrt_commethod(7)
    def get_Severity(self) -> win32more.Windows.Services.Maps.ManeuverWarningSeverity: ...
    Kind = property(get_Kind, None)
    Severity = property(get_Severity, None)
class IMapAddress(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IMapAddress'
    _iid_ = Guid('{cfa7a973-a3b4-4494-b3ff-cba94db69699}')
    @winrt_commethod(6)
    def get_BuildingName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_BuildingFloor(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_BuildingRoom(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_BuildingWing(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_StreetNumber(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_Street(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_Neighborhood(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_District(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def get_Town(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def get_Region(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def get_RegionCode(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def get_Country(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def get_CountryCode(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def get_PostCode(self) -> WinRT_String: ...
    @winrt_commethod(20)
    def get_Continent(self) -> WinRT_String: ...
    BuildingFloor = property(get_BuildingFloor, None)
    BuildingName = property(get_BuildingName, None)
    BuildingRoom = property(get_BuildingRoom, None)
    BuildingWing = property(get_BuildingWing, None)
    Continent = property(get_Continent, None)
    Country = property(get_Country, None)
    CountryCode = property(get_CountryCode, None)
    District = property(get_District, None)
    Neighborhood = property(get_Neighborhood, None)
    PostCode = property(get_PostCode, None)
    Region = property(get_Region, None)
    RegionCode = property(get_RegionCode, None)
    Street = property(get_Street, None)
    StreetNumber = property(get_StreetNumber, None)
    Town = property(get_Town, None)
class IMapAddress2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IMapAddress2'
    _iid_ = Guid('{75cd6df1-e5ad-45a9-bf40-6cf256c1dd13}')
    @winrt_commethod(6)
    def get_FormattedAddress(self) -> WinRT_String: ...
    FormattedAddress = property(get_FormattedAddress, None)
class IMapLocation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IMapLocation'
    _iid_ = Guid('{3c073f57-0da4-42e8-9ee2-a96fcf2371dc}')
    @winrt_commethod(6)
    def get_Point(self) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Address(self) -> win32more.Windows.Services.Maps.MapAddress: ...
    Address = property(get_Address, None)
    Description = property(get_Description, None)
    DisplayName = property(get_DisplayName, None)
    Point = property(get_Point, None)
class IMapLocationFinderResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IMapLocationFinderResult'
    _iid_ = Guid('{43f1f179-e8cc-45f6-bed2-54ccbf965d9a}')
    @winrt_commethod(6)
    def get_Locations(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.MapLocation]: ...
    @winrt_commethod(7)
    def get_Status(self) -> win32more.Windows.Services.Maps.MapLocationFinderStatus: ...
    Locations = property(get_Locations, None)
    Status = property(get_Status, None)
class IMapLocationFinderStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IMapLocationFinderStatics'
    _iid_ = Guid('{318adb5d-1c5d-4f35-a2df-aaca94959517}')
    @winrt_commethod(6)
    def FindLocationsAtAsync(self, queryPoint: win32more.Windows.Devices.Geolocation.Geopoint) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapLocationFinderResult]: ...
    @winrt_commethod(7)
    def FindLocationsAsync(self, searchText: WinRT_String, referencePoint: win32more.Windows.Devices.Geolocation.Geopoint) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapLocationFinderResult]: ...
    @winrt_commethod(8)
    def FindLocationsWithMaxCountAsync(self, searchText: WinRT_String, referencePoint: win32more.Windows.Devices.Geolocation.Geopoint, maxCount: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapLocationFinderResult]: ...
class IMapLocationFinderStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IMapLocationFinderStatics2'
    _iid_ = Guid('{959a8b96-6485-4dfd-851a-33ac317e3af6}')
    @winrt_commethod(6)
    def FindLocationsAtWithAccuracyAsync(self, queryPoint: win32more.Windows.Devices.Geolocation.Geopoint, accuracy: win32more.Windows.Services.Maps.MapLocationDesiredAccuracy) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapLocationFinderResult]: ...
class IMapManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IMapManagerStatics'
    _iid_ = Guid('{37e3e515-82b4-4d54-8fd9-af2624b3011c}')
    @winrt_commethod(6)
    def ShowDownloadedMapsUI(self) -> Void: ...
    @winrt_commethod(7)
    def ShowMapsUpdateUI(self) -> Void: ...
class IMapRoute(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IMapRoute'
    _iid_ = Guid('{fb07b732-584d-4583-9c60-641fea274349}')
    @winrt_commethod(6)
    def get_BoundingBox(self) -> win32more.Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_commethod(7)
    def get_LengthInMeters(self) -> Double: ...
    @winrt_commethod(8)
    def get_EstimatedDuration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_Path(self) -> win32more.Windows.Devices.Geolocation.Geopath: ...
    @winrt_commethod(10)
    def get_Legs(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.MapRouteLeg]: ...
    @winrt_commethod(11)
    def get_IsTrafficBased(self) -> Boolean: ...
    BoundingBox = property(get_BoundingBox, None)
    EstimatedDuration = property(get_EstimatedDuration, None)
    IsTrafficBased = property(get_IsTrafficBased, None)
    Legs = property(get_Legs, None)
    LengthInMeters = property(get_LengthInMeters, None)
    Path = property(get_Path, None)
class IMapRoute2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IMapRoute2'
    _iid_ = Guid('{d1c5d40c-2213-4ab0-a260-46b38169beac}')
    @winrt_commethod(6)
    def get_ViolatedRestrictions(self) -> win32more.Windows.Services.Maps.MapRouteRestrictions: ...
    @winrt_commethod(7)
    def get_HasBlockedRoads(self) -> Boolean: ...
    HasBlockedRoads = property(get_HasBlockedRoads, None)
    ViolatedRestrictions = property(get_ViolatedRestrictions, None)
class IMapRoute3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IMapRoute3'
    _iid_ = Guid('{858d1eae-f2ad-429f-bb37-cd21094ffc92}')
    @winrt_commethod(6)
    def get_DurationWithoutTraffic(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def get_TrafficCongestion(self) -> win32more.Windows.Services.Maps.TrafficCongestion: ...
    DurationWithoutTraffic = property(get_DurationWithoutTraffic, None)
    TrafficCongestion = property(get_TrafficCongestion, None)
class IMapRoute4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IMapRoute4'
    _iid_ = Guid('{366c8ca5-3053-4fa1-80ff-d475f3ed1e6e}')
    @winrt_commethod(6)
    def get_IsScenic(self) -> Boolean: ...
    IsScenic = property(get_IsScenic, None)
class IMapRouteDrivingOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IMapRouteDrivingOptions'
    _iid_ = Guid('{6815364d-c6dc-4697-a452-b18f8f0b67a1}')
    @winrt_commethod(6)
    def get_MaxAlternateRouteCount(self) -> UInt32: ...
    @winrt_commethod(7)
    def put_MaxAlternateRouteCount(self, value: UInt32) -> Void: ...
    @winrt_commethod(8)
    def get_InitialHeading(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(9)
    def put_InitialHeading(self, value: win32more.Windows.Foundation.IReference[Double]) -> Void: ...
    @winrt_commethod(10)
    def get_RouteOptimization(self) -> win32more.Windows.Services.Maps.MapRouteOptimization: ...
    @winrt_commethod(11)
    def put_RouteOptimization(self, value: win32more.Windows.Services.Maps.MapRouteOptimization) -> Void: ...
    @winrt_commethod(12)
    def get_RouteRestrictions(self) -> win32more.Windows.Services.Maps.MapRouteRestrictions: ...
    @winrt_commethod(13)
    def put_RouteRestrictions(self, value: win32more.Windows.Services.Maps.MapRouteRestrictions) -> Void: ...
    InitialHeading = property(get_InitialHeading, put_InitialHeading)
    MaxAlternateRouteCount = property(get_MaxAlternateRouteCount, put_MaxAlternateRouteCount)
    RouteOptimization = property(get_RouteOptimization, put_RouteOptimization)
    RouteRestrictions = property(get_RouteRestrictions, put_RouteRestrictions)
class IMapRouteDrivingOptions2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IMapRouteDrivingOptions2'
    _iid_ = Guid('{35dc8670-c298-48d0-b5ad-825460645603}')
    @winrt_commethod(6)
    def get_DepartureTime(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_commethod(7)
    def put_DepartureTime(self, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    DepartureTime = property(get_DepartureTime, put_DepartureTime)
class IMapRouteFinderResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IMapRouteFinderResult'
    _iid_ = Guid('{a868a31a-9422-46ac-8ca1-b1614d4bfbe2}')
    @winrt_commethod(6)
    def get_Route(self) -> win32more.Windows.Services.Maps.MapRoute: ...
    @winrt_commethod(7)
    def get_Status(self) -> win32more.Windows.Services.Maps.MapRouteFinderStatus: ...
    Route = property(get_Route, None)
    Status = property(get_Status, None)
class IMapRouteFinderResult2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IMapRouteFinderResult2'
    _iid_ = Guid('{20709c6d-d90c-46c8-91c6-7d4be4efb215}')
    @winrt_commethod(6)
    def get_AlternateRoutes(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.MapRoute]: ...
    AlternateRoutes = property(get_AlternateRoutes, None)
class IMapRouteFinderStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IMapRouteFinderStatics'
    _iid_ = Guid('{b8a5c50f-1c64-4c3a-81eb-1f7c152afbbb}')
    @winrt_commethod(6)
    def GetDrivingRouteAsync(self, startPoint: win32more.Windows.Devices.Geolocation.Geopoint, endPoint: win32more.Windows.Devices.Geolocation.Geopoint) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_commethod(7)
    def GetDrivingRouteWithOptimizationAsync(self, startPoint: win32more.Windows.Devices.Geolocation.Geopoint, endPoint: win32more.Windows.Devices.Geolocation.Geopoint, optimization: win32more.Windows.Services.Maps.MapRouteOptimization) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_commethod(8)
    def GetDrivingRouteWithOptimizationAndRestrictionsAsync(self, startPoint: win32more.Windows.Devices.Geolocation.Geopoint, endPoint: win32more.Windows.Devices.Geolocation.Geopoint, optimization: win32more.Windows.Services.Maps.MapRouteOptimization, restrictions: win32more.Windows.Services.Maps.MapRouteRestrictions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_commethod(9)
    def GetDrivingRouteWithOptimizationRestrictionsAndHeadingAsync(self, startPoint: win32more.Windows.Devices.Geolocation.Geopoint, endPoint: win32more.Windows.Devices.Geolocation.Geopoint, optimization: win32more.Windows.Services.Maps.MapRouteOptimization, restrictions: win32more.Windows.Services.Maps.MapRouteRestrictions, headingInDegrees: Double) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_commethod(10)
    def GetDrivingRouteFromWaypointsAsync(self, wayPoints: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Geolocation.Geopoint]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_commethod(11)
    def GetDrivingRouteFromWaypointsAndOptimizationAsync(self, wayPoints: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Geolocation.Geopoint], optimization: win32more.Windows.Services.Maps.MapRouteOptimization) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_commethod(12)
    def GetDrivingRouteFromWaypointsOptimizationAndRestrictionsAsync(self, wayPoints: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Geolocation.Geopoint], optimization: win32more.Windows.Services.Maps.MapRouteOptimization, restrictions: win32more.Windows.Services.Maps.MapRouteRestrictions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_commethod(13)
    def GetDrivingRouteFromWaypointsOptimizationRestrictionsAndHeadingAsync(self, wayPoints: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Geolocation.Geopoint], optimization: win32more.Windows.Services.Maps.MapRouteOptimization, restrictions: win32more.Windows.Services.Maps.MapRouteRestrictions, headingInDegrees: Double) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_commethod(14)
    def GetWalkingRouteAsync(self, startPoint: win32more.Windows.Devices.Geolocation.Geopoint, endPoint: win32more.Windows.Devices.Geolocation.Geopoint) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_commethod(15)
    def GetWalkingRouteFromWaypointsAsync(self, wayPoints: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Geolocation.Geopoint]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapRouteFinderResult]: ...
class IMapRouteFinderStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IMapRouteFinderStatics2'
    _iid_ = Guid('{afcc2c73-7760-49af-b3bd-baf135b703e1}')
    @winrt_commethod(6)
    def GetDrivingRouteWithOptionsAsync(self, startPoint: win32more.Windows.Devices.Geolocation.Geopoint, endPoint: win32more.Windows.Devices.Geolocation.Geopoint, options: win32more.Windows.Services.Maps.MapRouteDrivingOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapRouteFinderResult]: ...
class IMapRouteFinderStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IMapRouteFinderStatics3'
    _iid_ = Guid('{f6098134-5913-11e6-8b77-86f30ca893d3}')
    @winrt_commethod(6)
    def GetDrivingRouteFromEnhancedWaypointsAsync(self, waypoints: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Services.Maps.EnhancedWaypoint]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_commethod(7)
    def GetDrivingRouteFromEnhancedWaypointsWithOptionsAsync(self, waypoints: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Services.Maps.EnhancedWaypoint], options: win32more.Windows.Services.Maps.MapRouteDrivingOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapRouteFinderResult]: ...
class IMapRouteLeg(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IMapRouteLeg'
    _iid_ = Guid('{96f8b2f6-5bba-4d17-9db6-1a263fec7471}')
    @winrt_commethod(6)
    def get_BoundingBox(self) -> win32more.Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_commethod(7)
    def get_Path(self) -> win32more.Windows.Devices.Geolocation.Geopath: ...
    @winrt_commethod(8)
    def get_LengthInMeters(self) -> Double: ...
    @winrt_commethod(9)
    def get_EstimatedDuration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(10)
    def get_Maneuvers(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.MapRouteManeuver]: ...
    BoundingBox = property(get_BoundingBox, None)
    EstimatedDuration = property(get_EstimatedDuration, None)
    LengthInMeters = property(get_LengthInMeters, None)
    Maneuvers = property(get_Maneuvers, None)
    Path = property(get_Path, None)
class IMapRouteLeg2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IMapRouteLeg2'
    _iid_ = Guid('{02e2062d-c9c6-45b8-8e54-1a10b57a17e8}')
    @winrt_commethod(6)
    def get_DurationWithoutTraffic(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def get_TrafficCongestion(self) -> win32more.Windows.Services.Maps.TrafficCongestion: ...
    DurationWithoutTraffic = property(get_DurationWithoutTraffic, None)
    TrafficCongestion = property(get_TrafficCongestion, None)
class IMapRouteManeuver(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IMapRouteManeuver'
    _iid_ = Guid('{ed5c17f0-a6ab-4d65-a086-fa8a7e340df2}')
    @winrt_commethod(6)
    def get_StartingPoint(self) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(7)
    def get_LengthInMeters(self) -> Double: ...
    @winrt_commethod(8)
    def get_InstructionText(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Kind(self) -> win32more.Windows.Services.Maps.MapRouteManeuverKind: ...
    @winrt_commethod(10)
    def get_ExitNumber(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_ManeuverNotices(self) -> win32more.Windows.Services.Maps.MapManeuverNotices: ...
    ExitNumber = property(get_ExitNumber, None)
    InstructionText = property(get_InstructionText, None)
    Kind = property(get_Kind, None)
    LengthInMeters = property(get_LengthInMeters, None)
    ManeuverNotices = property(get_ManeuverNotices, None)
    StartingPoint = property(get_StartingPoint, None)
class IMapRouteManeuver2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IMapRouteManeuver2'
    _iid_ = Guid('{5d7bcd9c-7c9b-41df-838b-eae21e4b05a9}')
    @winrt_commethod(6)
    def get_StartHeading(self) -> Double: ...
    @winrt_commethod(7)
    def get_EndHeading(self) -> Double: ...
    @winrt_commethod(8)
    def get_StreetName(self) -> WinRT_String: ...
    EndHeading = property(get_EndHeading, None)
    StartHeading = property(get_StartHeading, None)
    StreetName = property(get_StreetName, None)
class IMapRouteManeuver3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IMapRouteManeuver3'
    _iid_ = Guid('{a6a138df-0483-4166-85be-b99336c11875}')
    @winrt_commethod(6)
    def get_Warnings(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.ManeuverWarning]: ...
    Warnings = property(get_Warnings, None)
class IMapServiceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IMapServiceStatics'
    _iid_ = Guid('{0144ad85-c04c-4cdd-871a-a0726d097cd4}')
    @winrt_commethod(6)
    def put_ServiceToken(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_ServiceToken(self) -> WinRT_String: ...
    ServiceToken = property(get_ServiceToken, put_ServiceToken)
class IMapServiceStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IMapServiceStatics2'
    _iid_ = Guid('{f8193eed-9c85-40a9-8896-0fc3fd2b7c2a}')
    @winrt_commethod(6)
    def get_WorldViewRegionCode(self) -> WinRT_String: ...
    WorldViewRegionCode = property(get_WorldViewRegionCode, None)
class IMapServiceStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IMapServiceStatics3'
    _iid_ = Guid('{0a11ce20-63a7-4854-b355-d6dcda223d1b}')
    @winrt_commethod(6)
    def get_DataAttributions(self) -> WinRT_String: ...
    DataAttributions = property(get_DataAttributions, None)
class IMapServiceStatics4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IMapServiceStatics4'
    _iid_ = Guid('{088a2862-6abc-420e-945f-4cfd89c67356}')
    @winrt_commethod(6)
    def put_DataUsagePreference(self, value: win32more.Windows.Services.Maps.MapServiceDataUsagePreference) -> Void: ...
    @winrt_commethod(7)
    def get_DataUsagePreference(self) -> win32more.Windows.Services.Maps.MapServiceDataUsagePreference: ...
    DataUsagePreference = property(get_DataUsagePreference, put_DataUsagePreference)
class IPlaceInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IPlaceInfo'
    _iid_ = Guid('{9a0810b6-31c8-4f6a-9f18-950b4c38951a}')
    @winrt_commethod(6)
    def Show(self, selection: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(7)
    def ShowWithPreferredPlacement(self, selection: win32more.Windows.Foundation.Rect, preferredPlacement: win32more.Windows.UI.Popups.Placement) -> Void: ...
    @winrt_commethod(8)
    def get_Identifier(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_DisplayAddress(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_Geoshape(self) -> win32more.Windows.Devices.Geolocation.IGeoshape: ...
    DisplayAddress = property(get_DisplayAddress, None)
    DisplayName = property(get_DisplayName, None)
    Geoshape = property(get_Geoshape, None)
    Identifier = property(get_Identifier, None)
class IPlaceInfoCreateOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IPlaceInfoCreateOptions'
    _iid_ = Guid('{cd33c125-67f1-4bb3-9907-ecce939b0399}')
    @winrt_commethod(6)
    def put_DisplayName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_DisplayAddress(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_DisplayAddress(self) -> WinRT_String: ...
    DisplayAddress = property(get_DisplayAddress, put_DisplayAddress)
    DisplayName = property(get_DisplayName, put_DisplayName)
class IPlaceInfoStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IPlaceInfoStatics'
    _iid_ = Guid('{82b9ff71-6cd0-48a4-afd9-5ed82097936b}')
    @winrt_commethod(6)
    def Create(self, referencePoint: win32more.Windows.Devices.Geolocation.Geopoint) -> win32more.Windows.Services.Maps.PlaceInfo: ...
    @winrt_commethod(7)
    def CreateWithGeopointAndOptions(self, referencePoint: win32more.Windows.Devices.Geolocation.Geopoint, options: win32more.Windows.Services.Maps.PlaceInfoCreateOptions) -> win32more.Windows.Services.Maps.PlaceInfo: ...
    @winrt_commethod(8)
    def CreateFromIdentifier(self, identifier: WinRT_String) -> win32more.Windows.Services.Maps.PlaceInfo: ...
    @winrt_commethod(9)
    def CreateFromIdentifierWithOptions(self, identifier: WinRT_String, defaultPoint: win32more.Windows.Devices.Geolocation.Geopoint, options: win32more.Windows.Services.Maps.PlaceInfoCreateOptions) -> win32more.Windows.Services.Maps.PlaceInfo: ...
    @winrt_commethod(10)
    def CreateFromMapLocation(self, location: win32more.Windows.Services.Maps.MapLocation) -> win32more.Windows.Services.Maps.PlaceInfo: ...
    @winrt_commethod(11)
    def get_IsShowSupported(self) -> Boolean: ...
    IsShowSupported = property(get_IsShowSupported, None)
class IPlaceInfoStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.IPlaceInfoStatics2'
    _iid_ = Guid('{730f0249-4047-44a3-8f81-2550a5216370}')
    @winrt_commethod(6)
    def CreateFromAddress(self, displayAddress: WinRT_String) -> win32more.Windows.Services.Maps.PlaceInfo: ...
    @winrt_commethod(7)
    def CreateFromAddressWithName(self, displayAddress: WinRT_String, displayName: WinRT_String) -> win32more.Windows.Services.Maps.PlaceInfo: ...
LocalSearchContract: UInt32 = 262144
class ManeuverWarning(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Maps.IManeuverWarning
    _classid_ = 'Windows.Services.Maps.ManeuverWarning'
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.Services.Maps.IManeuverWarning) -> win32more.Windows.Services.Maps.ManeuverWarningKind: ...
    @winrt_mixinmethod
    def get_Severity(self: win32more.Windows.Services.Maps.IManeuverWarning) -> win32more.Windows.Services.Maps.ManeuverWarningSeverity: ...
    Kind = property(get_Kind, None)
    Severity = property(get_Severity, None)
class ManeuverWarningKind(Enum, Int32):
    None_ = 0
    Accident = 1
    AdministrativeDivisionChange = 2
    Alert = 3
    BlockedRoad = 4
    CheckTimetable = 5
    Congestion = 6
    Construction = 7
    CountryChange = 8
    DisabledVehicle = 9
    GateAccess = 10
    GetOffTransit = 11
    GetOnTransit = 12
    IllegalUTurn = 13
    MassTransit = 14
    Miscellaneous = 15
    NoIncident = 16
    Other = 17
    OtherNews = 18
    OtherTrafficIncidents = 19
    PlannedEvent = 20
    PrivateRoad = 21
    RestrictedTurn = 22
    RoadClosures = 23
    RoadHazard = 24
    ScheduledConstruction = 25
    SeasonalClosures = 26
    Tollbooth = 27
    TollRoad = 28
    TollZoneEnter = 29
    TollZoneExit = 30
    TrafficFlow = 31
    TransitLineChange = 32
    UnpavedRoad = 33
    UnscheduledConstruction = 34
    Weather = 35
class ManeuverWarningSeverity(Enum, Int32):
    None_ = 0
    LowImpact = 1
    Minor = 2
    Moderate = 3
    Serious = 4
class MapAddress(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Maps.IMapAddress
    _classid_ = 'Windows.Services.Maps.MapAddress'
    @winrt_mixinmethod
    def get_BuildingName(self: win32more.Windows.Services.Maps.IMapAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_BuildingFloor(self: win32more.Windows.Services.Maps.IMapAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_BuildingRoom(self: win32more.Windows.Services.Maps.IMapAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_BuildingWing(self: win32more.Windows.Services.Maps.IMapAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_StreetNumber(self: win32more.Windows.Services.Maps.IMapAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Street(self: win32more.Windows.Services.Maps.IMapAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Neighborhood(self: win32more.Windows.Services.Maps.IMapAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_District(self: win32more.Windows.Services.Maps.IMapAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Town(self: win32more.Windows.Services.Maps.IMapAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Region(self: win32more.Windows.Services.Maps.IMapAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RegionCode(self: win32more.Windows.Services.Maps.IMapAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Country(self: win32more.Windows.Services.Maps.IMapAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CountryCode(self: win32more.Windows.Services.Maps.IMapAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PostCode(self: win32more.Windows.Services.Maps.IMapAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Continent(self: win32more.Windows.Services.Maps.IMapAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FormattedAddress(self: win32more.Windows.Services.Maps.IMapAddress2) -> WinRT_String: ...
    BuildingFloor = property(get_BuildingFloor, None)
    BuildingName = property(get_BuildingName, None)
    BuildingRoom = property(get_BuildingRoom, None)
    BuildingWing = property(get_BuildingWing, None)
    Continent = property(get_Continent, None)
    Country = property(get_Country, None)
    CountryCode = property(get_CountryCode, None)
    District = property(get_District, None)
    FormattedAddress = property(get_FormattedAddress, None)
    Neighborhood = property(get_Neighborhood, None)
    PostCode = property(get_PostCode, None)
    Region = property(get_Region, None)
    RegionCode = property(get_RegionCode, None)
    Street = property(get_Street, None)
    StreetNumber = property(get_StreetNumber, None)
    Town = property(get_Town, None)
class MapLocation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Maps.IMapLocation
    _classid_ = 'Windows.Services.Maps.MapLocation'
    @winrt_mixinmethod
    def get_Point(self: win32more.Windows.Services.Maps.IMapLocation) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Services.Maps.IMapLocation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: win32more.Windows.Services.Maps.IMapLocation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Address(self: win32more.Windows.Services.Maps.IMapLocation) -> win32more.Windows.Services.Maps.MapAddress: ...
    Address = property(get_Address, None)
    Description = property(get_Description, None)
    DisplayName = property(get_DisplayName, None)
    Point = property(get_Point, None)
class MapLocationDesiredAccuracy(Enum, Int32):
    High = 0
    Low = 1
class MapLocationFinder(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.MapLocationFinder'
    @winrt_classmethod
    def FindLocationsAtWithAccuracyAsync(cls: win32more.Windows.Services.Maps.IMapLocationFinderStatics2, queryPoint: win32more.Windows.Devices.Geolocation.Geopoint, accuracy: win32more.Windows.Services.Maps.MapLocationDesiredAccuracy) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapLocationFinderResult]: ...
    @winrt_classmethod
    def FindLocationsAtAsync(cls: win32more.Windows.Services.Maps.IMapLocationFinderStatics, queryPoint: win32more.Windows.Devices.Geolocation.Geopoint) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapLocationFinderResult]: ...
    @winrt_classmethod
    def FindLocationsAsync(cls: win32more.Windows.Services.Maps.IMapLocationFinderStatics, searchText: WinRT_String, referencePoint: win32more.Windows.Devices.Geolocation.Geopoint) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapLocationFinderResult]: ...
    @winrt_classmethod
    def FindLocationsWithMaxCountAsync(cls: win32more.Windows.Services.Maps.IMapLocationFinderStatics, searchText: WinRT_String, referencePoint: win32more.Windows.Devices.Geolocation.Geopoint, maxCount: UInt32) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapLocationFinderResult]: ...
class MapLocationFinderResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Maps.IMapLocationFinderResult
    _classid_ = 'Windows.Services.Maps.MapLocationFinderResult'
    @winrt_mixinmethod
    def get_Locations(self: win32more.Windows.Services.Maps.IMapLocationFinderResult) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.MapLocation]: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Services.Maps.IMapLocationFinderResult) -> win32more.Windows.Services.Maps.MapLocationFinderStatus: ...
    Locations = property(get_Locations, None)
    Status = property(get_Status, None)
class MapLocationFinderStatus(Enum, Int32):
    Success = 0
    UnknownError = 1
    InvalidCredentials = 2
    BadLocation = 3
    IndexFailure = 4
    NetworkFailure = 5
    NotSupported = 6
class MapManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.MapManager'
    @winrt_classmethod
    def ShowDownloadedMapsUI(cls: win32more.Windows.Services.Maps.IMapManagerStatics) -> Void: ...
    @winrt_classmethod
    def ShowMapsUpdateUI(cls: win32more.Windows.Services.Maps.IMapManagerStatics) -> Void: ...
class MapManeuverNotices(Enum, UInt32):
    None_ = 0
    Toll = 1
    Unpaved = 2
class MapRoute(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Maps.IMapRoute
    _classid_ = 'Windows.Services.Maps.MapRoute'
    @winrt_mixinmethod
    def get_BoundingBox(self: win32more.Windows.Services.Maps.IMapRoute) -> win32more.Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_mixinmethod
    def get_LengthInMeters(self: win32more.Windows.Services.Maps.IMapRoute) -> Double: ...
    @winrt_mixinmethod
    def get_EstimatedDuration(self: win32more.Windows.Services.Maps.IMapRoute) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Path(self: win32more.Windows.Services.Maps.IMapRoute) -> win32more.Windows.Devices.Geolocation.Geopath: ...
    @winrt_mixinmethod
    def get_Legs(self: win32more.Windows.Services.Maps.IMapRoute) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.MapRouteLeg]: ...
    @winrt_mixinmethod
    def get_IsTrafficBased(self: win32more.Windows.Services.Maps.IMapRoute) -> Boolean: ...
    @winrt_mixinmethod
    def get_ViolatedRestrictions(self: win32more.Windows.Services.Maps.IMapRoute2) -> win32more.Windows.Services.Maps.MapRouteRestrictions: ...
    @winrt_mixinmethod
    def get_HasBlockedRoads(self: win32more.Windows.Services.Maps.IMapRoute2) -> Boolean: ...
    @winrt_mixinmethod
    def get_DurationWithoutTraffic(self: win32more.Windows.Services.Maps.IMapRoute3) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_TrafficCongestion(self: win32more.Windows.Services.Maps.IMapRoute3) -> win32more.Windows.Services.Maps.TrafficCongestion: ...
    @winrt_mixinmethod
    def get_IsScenic(self: win32more.Windows.Services.Maps.IMapRoute4) -> Boolean: ...
    BoundingBox = property(get_BoundingBox, None)
    DurationWithoutTraffic = property(get_DurationWithoutTraffic, None)
    EstimatedDuration = property(get_EstimatedDuration, None)
    HasBlockedRoads = property(get_HasBlockedRoads, None)
    IsScenic = property(get_IsScenic, None)
    IsTrafficBased = property(get_IsTrafficBased, None)
    Legs = property(get_Legs, None)
    LengthInMeters = property(get_LengthInMeters, None)
    Path = property(get_Path, None)
    TrafficCongestion = property(get_TrafficCongestion, None)
    ViolatedRestrictions = property(get_ViolatedRestrictions, None)
class MapRouteDrivingOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Maps.IMapRouteDrivingOptions
    _classid_ = 'Windows.Services.Maps.MapRouteDrivingOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Services.Maps.MapRouteDrivingOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Services.Maps.MapRouteDrivingOptions: ...
    @winrt_mixinmethod
    def get_MaxAlternateRouteCount(self: win32more.Windows.Services.Maps.IMapRouteDrivingOptions) -> UInt32: ...
    @winrt_mixinmethod
    def put_MaxAlternateRouteCount(self: win32more.Windows.Services.Maps.IMapRouteDrivingOptions, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_InitialHeading(self: win32more.Windows.Services.Maps.IMapRouteDrivingOptions) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def put_InitialHeading(self: win32more.Windows.Services.Maps.IMapRouteDrivingOptions, value: win32more.Windows.Foundation.IReference[Double]) -> Void: ...
    @winrt_mixinmethod
    def get_RouteOptimization(self: win32more.Windows.Services.Maps.IMapRouteDrivingOptions) -> win32more.Windows.Services.Maps.MapRouteOptimization: ...
    @winrt_mixinmethod
    def put_RouteOptimization(self: win32more.Windows.Services.Maps.IMapRouteDrivingOptions, value: win32more.Windows.Services.Maps.MapRouteOptimization) -> Void: ...
    @winrt_mixinmethod
    def get_RouteRestrictions(self: win32more.Windows.Services.Maps.IMapRouteDrivingOptions) -> win32more.Windows.Services.Maps.MapRouteRestrictions: ...
    @winrt_mixinmethod
    def put_RouteRestrictions(self: win32more.Windows.Services.Maps.IMapRouteDrivingOptions, value: win32more.Windows.Services.Maps.MapRouteRestrictions) -> Void: ...
    @winrt_mixinmethod
    def get_DepartureTime(self: win32more.Windows.Services.Maps.IMapRouteDrivingOptions2) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_DepartureTime(self: win32more.Windows.Services.Maps.IMapRouteDrivingOptions2, value: win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.DateTime]) -> Void: ...
    DepartureTime = property(get_DepartureTime, put_DepartureTime)
    InitialHeading = property(get_InitialHeading, put_InitialHeading)
    MaxAlternateRouteCount = property(get_MaxAlternateRouteCount, put_MaxAlternateRouteCount)
    RouteOptimization = property(get_RouteOptimization, put_RouteOptimization)
    RouteRestrictions = property(get_RouteRestrictions, put_RouteRestrictions)
class MapRouteFinder(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.MapRouteFinder'
    @winrt_classmethod
    def GetDrivingRouteFromEnhancedWaypointsAsync(cls: win32more.Windows.Services.Maps.IMapRouteFinderStatics3, waypoints: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Services.Maps.EnhancedWaypoint]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_classmethod
    def GetDrivingRouteFromEnhancedWaypointsWithOptionsAsync(cls: win32more.Windows.Services.Maps.IMapRouteFinderStatics3, waypoints: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Services.Maps.EnhancedWaypoint], options: win32more.Windows.Services.Maps.MapRouteDrivingOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_classmethod
    def GetDrivingRouteWithOptionsAsync(cls: win32more.Windows.Services.Maps.IMapRouteFinderStatics2, startPoint: win32more.Windows.Devices.Geolocation.Geopoint, endPoint: win32more.Windows.Devices.Geolocation.Geopoint, options: win32more.Windows.Services.Maps.MapRouteDrivingOptions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_classmethod
    def GetDrivingRouteAsync(cls: win32more.Windows.Services.Maps.IMapRouteFinderStatics, startPoint: win32more.Windows.Devices.Geolocation.Geopoint, endPoint: win32more.Windows.Devices.Geolocation.Geopoint) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_classmethod
    def GetDrivingRouteWithOptimizationAsync(cls: win32more.Windows.Services.Maps.IMapRouteFinderStatics, startPoint: win32more.Windows.Devices.Geolocation.Geopoint, endPoint: win32more.Windows.Devices.Geolocation.Geopoint, optimization: win32more.Windows.Services.Maps.MapRouteOptimization) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_classmethod
    def GetDrivingRouteWithOptimizationAndRestrictionsAsync(cls: win32more.Windows.Services.Maps.IMapRouteFinderStatics, startPoint: win32more.Windows.Devices.Geolocation.Geopoint, endPoint: win32more.Windows.Devices.Geolocation.Geopoint, optimization: win32more.Windows.Services.Maps.MapRouteOptimization, restrictions: win32more.Windows.Services.Maps.MapRouteRestrictions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_classmethod
    def GetDrivingRouteWithOptimizationRestrictionsAndHeadingAsync(cls: win32more.Windows.Services.Maps.IMapRouteFinderStatics, startPoint: win32more.Windows.Devices.Geolocation.Geopoint, endPoint: win32more.Windows.Devices.Geolocation.Geopoint, optimization: win32more.Windows.Services.Maps.MapRouteOptimization, restrictions: win32more.Windows.Services.Maps.MapRouteRestrictions, headingInDegrees: Double) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_classmethod
    def GetDrivingRouteFromWaypointsAsync(cls: win32more.Windows.Services.Maps.IMapRouteFinderStatics, wayPoints: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Geolocation.Geopoint]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_classmethod
    def GetDrivingRouteFromWaypointsAndOptimizationAsync(cls: win32more.Windows.Services.Maps.IMapRouteFinderStatics, wayPoints: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Geolocation.Geopoint], optimization: win32more.Windows.Services.Maps.MapRouteOptimization) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_classmethod
    def GetDrivingRouteFromWaypointsOptimizationAndRestrictionsAsync(cls: win32more.Windows.Services.Maps.IMapRouteFinderStatics, wayPoints: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Geolocation.Geopoint], optimization: win32more.Windows.Services.Maps.MapRouteOptimization, restrictions: win32more.Windows.Services.Maps.MapRouteRestrictions) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_classmethod
    def GetDrivingRouteFromWaypointsOptimizationRestrictionsAndHeadingAsync(cls: win32more.Windows.Services.Maps.IMapRouteFinderStatics, wayPoints: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Geolocation.Geopoint], optimization: win32more.Windows.Services.Maps.MapRouteOptimization, restrictions: win32more.Windows.Services.Maps.MapRouteRestrictions, headingInDegrees: Double) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_classmethod
    def GetWalkingRouteAsync(cls: win32more.Windows.Services.Maps.IMapRouteFinderStatics, startPoint: win32more.Windows.Devices.Geolocation.Geopoint, endPoint: win32more.Windows.Devices.Geolocation.Geopoint) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_classmethod
    def GetWalkingRouteFromWaypointsAsync(cls: win32more.Windows.Services.Maps.IMapRouteFinderStatics, wayPoints: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Devices.Geolocation.Geopoint]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Services.Maps.MapRouteFinderResult]: ...
class MapRouteFinderResult(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Maps.IMapRouteFinderResult
    _classid_ = 'Windows.Services.Maps.MapRouteFinderResult'
    @winrt_mixinmethod
    def get_Route(self: win32more.Windows.Services.Maps.IMapRouteFinderResult) -> win32more.Windows.Services.Maps.MapRoute: ...
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.Services.Maps.IMapRouteFinderResult) -> win32more.Windows.Services.Maps.MapRouteFinderStatus: ...
    @winrt_mixinmethod
    def get_AlternateRoutes(self: win32more.Windows.Services.Maps.IMapRouteFinderResult2) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.MapRoute]: ...
    AlternateRoutes = property(get_AlternateRoutes, None)
    Route = property(get_Route, None)
    Status = property(get_Status, None)
class MapRouteFinderStatus(Enum, Int32):
    Success = 0
    UnknownError = 1
    InvalidCredentials = 2
    NoRouteFound = 3
    NoRouteFoundWithGivenOptions = 4
    StartPointNotFound = 5
    EndPointNotFound = 6
    NoPedestrianRouteFound = 7
    NetworkFailure = 8
    NotSupported = 9
class MapRouteLeg(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Maps.IMapRouteLeg
    _classid_ = 'Windows.Services.Maps.MapRouteLeg'
    @winrt_mixinmethod
    def get_BoundingBox(self: win32more.Windows.Services.Maps.IMapRouteLeg) -> win32more.Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_mixinmethod
    def get_Path(self: win32more.Windows.Services.Maps.IMapRouteLeg) -> win32more.Windows.Devices.Geolocation.Geopath: ...
    @winrt_mixinmethod
    def get_LengthInMeters(self: win32more.Windows.Services.Maps.IMapRouteLeg) -> Double: ...
    @winrt_mixinmethod
    def get_EstimatedDuration(self: win32more.Windows.Services.Maps.IMapRouteLeg) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Maneuvers(self: win32more.Windows.Services.Maps.IMapRouteLeg) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.MapRouteManeuver]: ...
    @winrt_mixinmethod
    def get_DurationWithoutTraffic(self: win32more.Windows.Services.Maps.IMapRouteLeg2) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_TrafficCongestion(self: win32more.Windows.Services.Maps.IMapRouteLeg2) -> win32more.Windows.Services.Maps.TrafficCongestion: ...
    BoundingBox = property(get_BoundingBox, None)
    DurationWithoutTraffic = property(get_DurationWithoutTraffic, None)
    EstimatedDuration = property(get_EstimatedDuration, None)
    LengthInMeters = property(get_LengthInMeters, None)
    Maneuvers = property(get_Maneuvers, None)
    Path = property(get_Path, None)
    TrafficCongestion = property(get_TrafficCongestion, None)
class MapRouteManeuver(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Maps.IMapRouteManeuver
    _classid_ = 'Windows.Services.Maps.MapRouteManeuver'
    @winrt_mixinmethod
    def get_StartingPoint(self: win32more.Windows.Services.Maps.IMapRouteManeuver) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_LengthInMeters(self: win32more.Windows.Services.Maps.IMapRouteManeuver) -> Double: ...
    @winrt_mixinmethod
    def get_InstructionText(self: win32more.Windows.Services.Maps.IMapRouteManeuver) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.Services.Maps.IMapRouteManeuver) -> win32more.Windows.Services.Maps.MapRouteManeuverKind: ...
    @winrt_mixinmethod
    def get_ExitNumber(self: win32more.Windows.Services.Maps.IMapRouteManeuver) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ManeuverNotices(self: win32more.Windows.Services.Maps.IMapRouteManeuver) -> win32more.Windows.Services.Maps.MapManeuverNotices: ...
    @winrt_mixinmethod
    def get_StartHeading(self: win32more.Windows.Services.Maps.IMapRouteManeuver2) -> Double: ...
    @winrt_mixinmethod
    def get_EndHeading(self: win32more.Windows.Services.Maps.IMapRouteManeuver2) -> Double: ...
    @winrt_mixinmethod
    def get_StreetName(self: win32more.Windows.Services.Maps.IMapRouteManeuver2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Warnings(self: win32more.Windows.Services.Maps.IMapRouteManeuver3) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.ManeuverWarning]: ...
    EndHeading = property(get_EndHeading, None)
    ExitNumber = property(get_ExitNumber, None)
    InstructionText = property(get_InstructionText, None)
    Kind = property(get_Kind, None)
    LengthInMeters = property(get_LengthInMeters, None)
    ManeuverNotices = property(get_ManeuverNotices, None)
    StartHeading = property(get_StartHeading, None)
    StartingPoint = property(get_StartingPoint, None)
    StreetName = property(get_StreetName, None)
    Warnings = property(get_Warnings, None)
class MapRouteManeuverKind(Enum, Int32):
    None_ = 0
    Start = 1
    Stopover = 2
    StopoverResume = 3
    End = 4
    GoStraight = 5
    UTurnLeft = 6
    UTurnRight = 7
    TurnKeepLeft = 8
    TurnKeepRight = 9
    TurnLightLeft = 10
    TurnLightRight = 11
    TurnLeft = 12
    TurnRight = 13
    TurnHardLeft = 14
    TurnHardRight = 15
    FreewayEnterLeft = 16
    FreewayEnterRight = 17
    FreewayLeaveLeft = 18
    FreewayLeaveRight = 19
    FreewayContinueLeft = 20
    FreewayContinueRight = 21
    TrafficCircleLeft = 22
    TrafficCircleRight = 23
    TakeFerry = 24
class MapRouteOptimization(Enum, Int32):
    Time = 0
    Distance = 1
    TimeWithTraffic = 2
    Scenic = 3
class MapRouteRestrictions(Enum, UInt32):
    None_ = 0
    Highways = 1
    TollRoads = 2
    Ferries = 4
    Tunnels = 8
    DirtRoads = 16
    Motorail = 32
class _MapService_Meta_(ComPtr.__class__):
    pass
class MapService(ComPtr, metaclass=_MapService_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.MapService'
    @winrt_classmethod
    def put_DataUsagePreference(cls: win32more.Windows.Services.Maps.IMapServiceStatics4, value: win32more.Windows.Services.Maps.MapServiceDataUsagePreference) -> Void: ...
    @winrt_classmethod
    def get_DataUsagePreference(cls: win32more.Windows.Services.Maps.IMapServiceStatics4) -> win32more.Windows.Services.Maps.MapServiceDataUsagePreference: ...
    @winrt_classmethod
    def get_DataAttributions(cls: win32more.Windows.Services.Maps.IMapServiceStatics3) -> WinRT_String: ...
    @winrt_classmethod
    def get_WorldViewRegionCode(cls: win32more.Windows.Services.Maps.IMapServiceStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def put_ServiceToken(cls: win32more.Windows.Services.Maps.IMapServiceStatics, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_ServiceToken(cls: win32more.Windows.Services.Maps.IMapServiceStatics) -> WinRT_String: ...
    _MapService_Meta_.DataAttributions = property(get_DataAttributions, None)
    _MapService_Meta_.DataUsagePreference = property(get_DataUsagePreference, put_DataUsagePreference)
    _MapService_Meta_.ServiceToken = property(get_ServiceToken, put_ServiceToken)
    _MapService_Meta_.WorldViewRegionCode = property(get_WorldViewRegionCode, None)
class MapServiceDataUsagePreference(Enum, Int32):
    Default = 0
    OfflineMapDataOnly = 1
class _PlaceInfo_Meta_(ComPtr.__class__):
    pass
class PlaceInfo(ComPtr, metaclass=_PlaceInfo_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Maps.IPlaceInfo
    _classid_ = 'Windows.Services.Maps.PlaceInfo'
    @winrt_mixinmethod
    def Show(self: win32more.Windows.Services.Maps.IPlaceInfo, selection: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def ShowWithPreferredPlacement(self: win32more.Windows.Services.Maps.IPlaceInfo, selection: win32more.Windows.Foundation.Rect, preferredPlacement: win32more.Windows.UI.Popups.Placement) -> Void: ...
    @winrt_mixinmethod
    def get_Identifier(self: win32more.Windows.Services.Maps.IPlaceInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Services.Maps.IPlaceInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayAddress(self: win32more.Windows.Services.Maps.IPlaceInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Geoshape(self: win32more.Windows.Services.Maps.IPlaceInfo) -> win32more.Windows.Devices.Geolocation.IGeoshape: ...
    @winrt_classmethod
    def CreateFromAddress(cls: win32more.Windows.Services.Maps.IPlaceInfoStatics2, displayAddress: WinRT_String) -> win32more.Windows.Services.Maps.PlaceInfo: ...
    @winrt_classmethod
    def CreateFromAddressWithName(cls: win32more.Windows.Services.Maps.IPlaceInfoStatics2, displayAddress: WinRT_String, displayName: WinRT_String) -> win32more.Windows.Services.Maps.PlaceInfo: ...
    @winrt_classmethod
    def Create(cls: win32more.Windows.Services.Maps.IPlaceInfoStatics, referencePoint: win32more.Windows.Devices.Geolocation.Geopoint) -> win32more.Windows.Services.Maps.PlaceInfo: ...
    @winrt_classmethod
    def CreateWithGeopointAndOptions(cls: win32more.Windows.Services.Maps.IPlaceInfoStatics, referencePoint: win32more.Windows.Devices.Geolocation.Geopoint, options: win32more.Windows.Services.Maps.PlaceInfoCreateOptions) -> win32more.Windows.Services.Maps.PlaceInfo: ...
    @winrt_classmethod
    def CreateFromIdentifier(cls: win32more.Windows.Services.Maps.IPlaceInfoStatics, identifier: WinRT_String) -> win32more.Windows.Services.Maps.PlaceInfo: ...
    @winrt_classmethod
    def CreateFromIdentifierWithOptions(cls: win32more.Windows.Services.Maps.IPlaceInfoStatics, identifier: WinRT_String, defaultPoint: win32more.Windows.Devices.Geolocation.Geopoint, options: win32more.Windows.Services.Maps.PlaceInfoCreateOptions) -> win32more.Windows.Services.Maps.PlaceInfo: ...
    @winrt_classmethod
    def CreateFromMapLocation(cls: win32more.Windows.Services.Maps.IPlaceInfoStatics, location: win32more.Windows.Services.Maps.MapLocation) -> win32more.Windows.Services.Maps.PlaceInfo: ...
    @winrt_classmethod
    def get_IsShowSupported(cls: win32more.Windows.Services.Maps.IPlaceInfoStatics) -> Boolean: ...
    DisplayAddress = property(get_DisplayAddress, None)
    DisplayName = property(get_DisplayName, None)
    Geoshape = property(get_Geoshape, None)
    Identifier = property(get_Identifier, None)
    _PlaceInfo_Meta_.IsShowSupported = property(get_IsShowSupported, None)
class PlaceInfoCreateOptions(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Maps.IPlaceInfoCreateOptions
    _classid_ = 'Windows.Services.Maps.PlaceInfoCreateOptions'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.Services.Maps.PlaceInfoCreateOptions.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.Services.Maps.PlaceInfoCreateOptions: ...
    @winrt_mixinmethod
    def put_DisplayName(self: win32more.Windows.Services.Maps.IPlaceInfoCreateOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayName(self: win32more.Windows.Services.Maps.IPlaceInfoCreateOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayAddress(self: win32more.Windows.Services.Maps.IPlaceInfoCreateOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayAddress(self: win32more.Windows.Services.Maps.IPlaceInfoCreateOptions) -> WinRT_String: ...
    DisplayAddress = property(get_DisplayAddress, put_DisplayAddress)
    DisplayName = property(get_DisplayName, put_DisplayName)
class TrafficCongestion(Enum, Int32):
    Unknown = 0
    Light = 1
    Mild = 2
    Medium = 3
    Heavy = 4
class WaypointKind(Enum, Int32):
    Stop = 0
    Via = 1


make_ready(__name__)
