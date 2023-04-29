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
import Windows.Devices.Geolocation
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Services.Maps
import Windows.UI.Popups
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class EnhancedWaypoint(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Maps.EnhancedWaypoint'
    @winrt_factorymethod
    def Create(cls: Windows.Services.Maps.IEnhancedWaypointFactory, point: Windows.Devices.Geolocation.Geopoint, kind: Windows.Services.Maps.WaypointKind) -> Windows.Services.Maps.EnhancedWaypoint: ...
    @winrt_mixinmethod
    def get_Point(self: Windows.Services.Maps.IEnhancedWaypoint) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.Services.Maps.IEnhancedWaypoint) -> Windows.Services.Maps.WaypointKind: ...
    Point = property(get_Point, None)
    Kind = property(get_Kind, None)
GuidanceContract: UInt32 = 196608
class IEnhancedWaypoint(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ed268c74-5913-11e6-8b-77-86-f3-0c-a8-93-d3')
    @winrt_commethod(6)
    def get_Point(self) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(7)
    def get_Kind(self) -> Windows.Services.Maps.WaypointKind: ...
    Point = property(get_Point, None)
    Kind = property(get_Kind, None)
class IEnhancedWaypointFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('af868477-a2aa-46dd-b6-45-23-b3-1b-8a-a6-c7')
    @winrt_commethod(6)
    def Create(self, point: Windows.Devices.Geolocation.Geopoint, kind: Windows.Services.Maps.WaypointKind) -> Windows.Services.Maps.EnhancedWaypoint: ...
class IManeuverWarning(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('c1a36d8a-2630-4378-9e-4a-6e-44-25-3d-ce-ba')
    @winrt_commethod(6)
    def get_Kind(self) -> Windows.Services.Maps.ManeuverWarningKind: ...
    @winrt_commethod(7)
    def get_Severity(self) -> Windows.Services.Maps.ManeuverWarningSeverity: ...
    Kind = property(get_Kind, None)
    Severity = property(get_Severity, None)
class IMapAddress(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('cfa7a973-a3b4-4494-b3-ff-cb-a9-4d-b6-96-99')
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
    BuildingName = property(get_BuildingName, None)
    BuildingFloor = property(get_BuildingFloor, None)
    BuildingRoom = property(get_BuildingRoom, None)
    BuildingWing = property(get_BuildingWing, None)
    StreetNumber = property(get_StreetNumber, None)
    Street = property(get_Street, None)
    Neighborhood = property(get_Neighborhood, None)
    District = property(get_District, None)
    Town = property(get_Town, None)
    Region = property(get_Region, None)
    RegionCode = property(get_RegionCode, None)
    Country = property(get_Country, None)
    CountryCode = property(get_CountryCode, None)
    PostCode = property(get_PostCode, None)
    Continent = property(get_Continent, None)
class IMapAddress2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('75cd6df1-e5ad-45a9-bf-40-6c-f2-56-c1-dd-13')
    @winrt_commethod(6)
    def get_FormattedAddress(self) -> WinRT_String: ...
    FormattedAddress = property(get_FormattedAddress, None)
class IMapLocation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3c073f57-0da4-42e8-9e-e2-a9-6f-cf-23-71-dc')
    @winrt_commethod(6)
    def get_Point(self) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_Description(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Address(self) -> Windows.Services.Maps.MapAddress: ...
    Point = property(get_Point, None)
    DisplayName = property(get_DisplayName, None)
    Description = property(get_Description, None)
    Address = property(get_Address, None)
class IMapLocationFinderResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('43f1f179-e8cc-45f6-be-d2-54-cc-bf-96-5d-9a')
    @winrt_commethod(6)
    def get_Locations(self) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Maps.MapLocation]: ...
    @winrt_commethod(7)
    def get_Status(self) -> Windows.Services.Maps.MapLocationFinderStatus: ...
    Locations = property(get_Locations, None)
    Status = property(get_Status, None)
class IMapLocationFinderStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('318adb5d-1c5d-4f35-a2-df-aa-ca-94-95-95-17')
    @winrt_commethod(6)
    def FindLocationsAtAsync(self, queryPoint: Windows.Devices.Geolocation.Geopoint) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapLocationFinderResult]: ...
    @winrt_commethod(7)
    def FindLocationsAsync(self, searchText: WinRT_String, referencePoint: Windows.Devices.Geolocation.Geopoint) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapLocationFinderResult]: ...
    @winrt_commethod(8)
    def FindLocationsWithMaxCountAsync(self, searchText: WinRT_String, referencePoint: Windows.Devices.Geolocation.Geopoint, maxCount: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapLocationFinderResult]: ...
class IMapLocationFinderStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('959a8b96-6485-4dfd-85-1a-33-ac-31-7e-3a-f6')
    @winrt_commethod(6)
    def FindLocationsAtWithAccuracyAsync(self, queryPoint: Windows.Devices.Geolocation.Geopoint, accuracy: Windows.Services.Maps.MapLocationDesiredAccuracy) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapLocationFinderResult]: ...
class IMapManagerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('37e3e515-82b4-4d54-8f-d9-af-26-24-b3-01-1c')
    @winrt_commethod(6)
    def ShowDownloadedMapsUI(self) -> Void: ...
    @winrt_commethod(7)
    def ShowMapsUpdateUI(self) -> Void: ...
class IMapRoute(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fb07b732-584d-4583-9c-60-64-1f-ea-27-43-49')
    @winrt_commethod(6)
    def get_BoundingBox(self) -> Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_commethod(7)
    def get_LengthInMeters(self) -> Double: ...
    @winrt_commethod(8)
    def get_EstimatedDuration(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(9)
    def get_Path(self) -> Windows.Devices.Geolocation.Geopath: ...
    @winrt_commethod(10)
    def get_Legs(self) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Maps.MapRouteLeg]: ...
    @winrt_commethod(11)
    def get_IsTrafficBased(self) -> Boolean: ...
    BoundingBox = property(get_BoundingBox, None)
    LengthInMeters = property(get_LengthInMeters, None)
    EstimatedDuration = property(get_EstimatedDuration, None)
    Path = property(get_Path, None)
    Legs = property(get_Legs, None)
    IsTrafficBased = property(get_IsTrafficBased, None)
class IMapRoute2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d1c5d40c-2213-4ab0-a2-60-46-b3-81-69-be-ac')
    @winrt_commethod(6)
    def get_ViolatedRestrictions(self) -> Windows.Services.Maps.MapRouteRestrictions: ...
    @winrt_commethod(7)
    def get_HasBlockedRoads(self) -> Boolean: ...
    ViolatedRestrictions = property(get_ViolatedRestrictions, None)
    HasBlockedRoads = property(get_HasBlockedRoads, None)
class IMapRoute3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('858d1eae-f2ad-429f-bb-37-cd-21-09-4f-fc-92')
    @winrt_commethod(6)
    def get_DurationWithoutTraffic(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def get_TrafficCongestion(self) -> Windows.Services.Maps.TrafficCongestion: ...
    DurationWithoutTraffic = property(get_DurationWithoutTraffic, None)
    TrafficCongestion = property(get_TrafficCongestion, None)
class IMapRoute4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('366c8ca5-3053-4fa1-80-ff-d4-75-f3-ed-1e-6e')
    @winrt_commethod(6)
    def get_IsScenic(self) -> Boolean: ...
    IsScenic = property(get_IsScenic, None)
class IMapRouteDrivingOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6815364d-c6dc-4697-a4-52-b1-8f-8f-0b-67-a1')
    @winrt_commethod(6)
    def get_MaxAlternateRouteCount(self) -> UInt32: ...
    @winrt_commethod(7)
    def put_MaxAlternateRouteCount(self, value: UInt32) -> Void: ...
    @winrt_commethod(8)
    def get_InitialHeading(self) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(9)
    def put_InitialHeading(self, value: Windows.Foundation.IReference[Double]) -> Void: ...
    @winrt_commethod(10)
    def get_RouteOptimization(self) -> Windows.Services.Maps.MapRouteOptimization: ...
    @winrt_commethod(11)
    def put_RouteOptimization(self, value: Windows.Services.Maps.MapRouteOptimization) -> Void: ...
    @winrt_commethod(12)
    def get_RouteRestrictions(self) -> Windows.Services.Maps.MapRouteRestrictions: ...
    @winrt_commethod(13)
    def put_RouteRestrictions(self, value: Windows.Services.Maps.MapRouteRestrictions) -> Void: ...
    MaxAlternateRouteCount = property(get_MaxAlternateRouteCount, put_MaxAlternateRouteCount)
    InitialHeading = property(get_InitialHeading, put_InitialHeading)
    RouteOptimization = property(get_RouteOptimization, put_RouteOptimization)
    RouteRestrictions = property(get_RouteRestrictions, put_RouteRestrictions)
class IMapRouteDrivingOptions2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('35dc8670-c298-48d0-b5-ad-82-54-60-64-56-03')
    @winrt_commethod(6)
    def get_DepartureTime(self) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_commethod(7)
    def put_DepartureTime(self, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    DepartureTime = property(get_DepartureTime, put_DepartureTime)
class IMapRouteFinderResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a868a31a-9422-46ac-8c-a1-b1-61-4d-4b-fb-e2')
    @winrt_commethod(6)
    def get_Route(self) -> Windows.Services.Maps.MapRoute: ...
    @winrt_commethod(7)
    def get_Status(self) -> Windows.Services.Maps.MapRouteFinderStatus: ...
    Route = property(get_Route, None)
    Status = property(get_Status, None)
class IMapRouteFinderResult2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('20709c6d-d90c-46c8-91-c6-7d-4b-e4-ef-b2-15')
    @winrt_commethod(6)
    def get_AlternateRoutes(self) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Maps.MapRoute]: ...
    AlternateRoutes = property(get_AlternateRoutes, None)
class IMapRouteFinderStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('b8a5c50f-1c64-4c3a-81-eb-1f-7c-15-2a-fb-bb')
    @winrt_commethod(6)
    def GetDrivingRouteAsync(self, startPoint: Windows.Devices.Geolocation.Geopoint, endPoint: Windows.Devices.Geolocation.Geopoint) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_commethod(7)
    def GetDrivingRouteWithOptimizationAsync(self, startPoint: Windows.Devices.Geolocation.Geopoint, endPoint: Windows.Devices.Geolocation.Geopoint, optimization: Windows.Services.Maps.MapRouteOptimization) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_commethod(8)
    def GetDrivingRouteWithOptimizationAndRestrictionsAsync(self, startPoint: Windows.Devices.Geolocation.Geopoint, endPoint: Windows.Devices.Geolocation.Geopoint, optimization: Windows.Services.Maps.MapRouteOptimization, restrictions: Windows.Services.Maps.MapRouteRestrictions) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_commethod(9)
    def GetDrivingRouteWithOptimizationRestrictionsAndHeadingAsync(self, startPoint: Windows.Devices.Geolocation.Geopoint, endPoint: Windows.Devices.Geolocation.Geopoint, optimization: Windows.Services.Maps.MapRouteOptimization, restrictions: Windows.Services.Maps.MapRouteRestrictions, headingInDegrees: Double) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_commethod(10)
    def GetDrivingRouteFromWaypointsAsync(self, wayPoints: Windows.Foundation.Collections.IIterable[Windows.Devices.Geolocation.Geopoint]) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_commethod(11)
    def GetDrivingRouteFromWaypointsAndOptimizationAsync(self, wayPoints: Windows.Foundation.Collections.IIterable[Windows.Devices.Geolocation.Geopoint], optimization: Windows.Services.Maps.MapRouteOptimization) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_commethod(12)
    def GetDrivingRouteFromWaypointsOptimizationAndRestrictionsAsync(self, wayPoints: Windows.Foundation.Collections.IIterable[Windows.Devices.Geolocation.Geopoint], optimization: Windows.Services.Maps.MapRouteOptimization, restrictions: Windows.Services.Maps.MapRouteRestrictions) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_commethod(13)
    def GetDrivingRouteFromWaypointsOptimizationRestrictionsAndHeadingAsync(self, wayPoints: Windows.Foundation.Collections.IIterable[Windows.Devices.Geolocation.Geopoint], optimization: Windows.Services.Maps.MapRouteOptimization, restrictions: Windows.Services.Maps.MapRouteRestrictions, headingInDegrees: Double) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_commethod(14)
    def GetWalkingRouteAsync(self, startPoint: Windows.Devices.Geolocation.Geopoint, endPoint: Windows.Devices.Geolocation.Geopoint) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_commethod(15)
    def GetWalkingRouteFromWaypointsAsync(self, wayPoints: Windows.Foundation.Collections.IIterable[Windows.Devices.Geolocation.Geopoint]) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapRouteFinderResult]: ...
class IMapRouteFinderStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('afcc2c73-7760-49af-b3-bd-ba-f1-35-b7-03-e1')
    @winrt_commethod(6)
    def GetDrivingRouteWithOptionsAsync(self, startPoint: Windows.Devices.Geolocation.Geopoint, endPoint: Windows.Devices.Geolocation.Geopoint, options: Windows.Services.Maps.MapRouteDrivingOptions) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapRouteFinderResult]: ...
class IMapRouteFinderStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f6098134-5913-11e6-8b-77-86-f3-0c-a8-93-d3')
    @winrt_commethod(6)
    def GetDrivingRouteFromEnhancedWaypointsAsync(self, waypoints: Windows.Foundation.Collections.IIterable[Windows.Services.Maps.EnhancedWaypoint]) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_commethod(7)
    def GetDrivingRouteFromEnhancedWaypointsWithOptionsAsync(self, waypoints: Windows.Foundation.Collections.IIterable[Windows.Services.Maps.EnhancedWaypoint], options: Windows.Services.Maps.MapRouteDrivingOptions) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapRouteFinderResult]: ...
class IMapRouteLeg(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('96f8b2f6-5bba-4d17-9d-b6-1a-26-3f-ec-74-71')
    @winrt_commethod(6)
    def get_BoundingBox(self) -> Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_commethod(7)
    def get_Path(self) -> Windows.Devices.Geolocation.Geopath: ...
    @winrt_commethod(8)
    def get_LengthInMeters(self) -> Double: ...
    @winrt_commethod(9)
    def get_EstimatedDuration(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(10)
    def get_Maneuvers(self) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Maps.MapRouteManeuver]: ...
    BoundingBox = property(get_BoundingBox, None)
    Path = property(get_Path, None)
    LengthInMeters = property(get_LengthInMeters, None)
    EstimatedDuration = property(get_EstimatedDuration, None)
    Maneuvers = property(get_Maneuvers, None)
class IMapRouteLeg2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('02e2062d-c9c6-45b8-8e-54-1a-10-b5-7a-17-e8')
    @winrt_commethod(6)
    def get_DurationWithoutTraffic(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def get_TrafficCongestion(self) -> Windows.Services.Maps.TrafficCongestion: ...
    DurationWithoutTraffic = property(get_DurationWithoutTraffic, None)
    TrafficCongestion = property(get_TrafficCongestion, None)
class IMapRouteManeuver(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ed5c17f0-a6ab-4d65-a0-86-fa-8a-7e-34-0d-f2')
    @winrt_commethod(6)
    def get_StartingPoint(self) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(7)
    def get_LengthInMeters(self) -> Double: ...
    @winrt_commethod(8)
    def get_InstructionText(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_Kind(self) -> Windows.Services.Maps.MapRouteManeuverKind: ...
    @winrt_commethod(10)
    def get_ExitNumber(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_ManeuverNotices(self) -> Windows.Services.Maps.MapManeuverNotices: ...
    StartingPoint = property(get_StartingPoint, None)
    LengthInMeters = property(get_LengthInMeters, None)
    InstructionText = property(get_InstructionText, None)
    Kind = property(get_Kind, None)
    ExitNumber = property(get_ExitNumber, None)
    ManeuverNotices = property(get_ManeuverNotices, None)
class IMapRouteManeuver2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5d7bcd9c-7c9b-41df-83-8b-ea-e2-1e-4b-05-a9')
    @winrt_commethod(6)
    def get_StartHeading(self) -> Double: ...
    @winrt_commethod(7)
    def get_EndHeading(self) -> Double: ...
    @winrt_commethod(8)
    def get_StreetName(self) -> WinRT_String: ...
    StartHeading = property(get_StartHeading, None)
    EndHeading = property(get_EndHeading, None)
    StreetName = property(get_StreetName, None)
class IMapRouteManeuver3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a6a138df-0483-4166-85-be-b9-93-36-c1-18-75')
    @winrt_commethod(6)
    def get_Warnings(self) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Maps.ManeuverWarning]: ...
    Warnings = property(get_Warnings, None)
class IMapServiceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0144ad85-c04c-4cdd-87-1a-a0-72-6d-09-7c-d4')
    @winrt_commethod(6)
    def put_ServiceToken(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_ServiceToken(self) -> WinRT_String: ...
    ServiceToken = property(get_ServiceToken, put_ServiceToken)
class IMapServiceStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f8193eed-9c85-40a9-88-96-0f-c3-fd-2b-7c-2a')
    @winrt_commethod(6)
    def get_WorldViewRegionCode(self) -> WinRT_String: ...
    WorldViewRegionCode = property(get_WorldViewRegionCode, None)
class IMapServiceStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0a11ce20-63a7-4854-b3-55-d6-dc-da-22-3d-1b')
    @winrt_commethod(6)
    def get_DataAttributions(self) -> WinRT_String: ...
    DataAttributions = property(get_DataAttributions, None)
class IMapServiceStatics4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('088a2862-6abc-420e-94-5f-4c-fd-89-c6-73-56')
    @winrt_commethod(6)
    def put_DataUsagePreference(self, value: Windows.Services.Maps.MapServiceDataUsagePreference) -> Void: ...
    @winrt_commethod(7)
    def get_DataUsagePreference(self) -> Windows.Services.Maps.MapServiceDataUsagePreference: ...
    DataUsagePreference = property(get_DataUsagePreference, put_DataUsagePreference)
class IPlaceInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9a0810b6-31c8-4f6a-9f-18-95-0b-4c-38-95-1a')
    @winrt_commethod(6)
    def Show(self, selection: Windows.Foundation.Rect) -> Void: ...
    @winrt_commethod(7)
    def ShowWithPreferredPlacement(self, selection: Windows.Foundation.Rect, preferredPlacement: Windows.UI.Popups.Placement) -> Void: ...
    @winrt_commethod(8)
    def get_Identifier(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_DisplayAddress(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_Geoshape(self) -> Windows.Devices.Geolocation.IGeoshape: ...
    Identifier = property(get_Identifier, None)
    DisplayName = property(get_DisplayName, None)
    DisplayAddress = property(get_DisplayAddress, None)
    Geoshape = property(get_Geoshape, None)
class IPlaceInfoCreateOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('cd33c125-67f1-4bb3-99-07-ec-ce-93-9b-03-99')
    @winrt_commethod(6)
    def put_DisplayName(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(7)
    def get_DisplayName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_DisplayAddress(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_DisplayAddress(self) -> WinRT_String: ...
    DisplayName = property(get_DisplayName, put_DisplayName)
    DisplayAddress = property(get_DisplayAddress, put_DisplayAddress)
class IPlaceInfoStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('82b9ff71-6cd0-48a4-af-d9-5e-d8-20-97-93-6b')
    @winrt_commethod(6)
    def Create(self, referencePoint: Windows.Devices.Geolocation.Geopoint) -> Windows.Services.Maps.PlaceInfo: ...
    @winrt_commethod(7)
    def CreateWithGeopointAndOptions(self, referencePoint: Windows.Devices.Geolocation.Geopoint, options: Windows.Services.Maps.PlaceInfoCreateOptions) -> Windows.Services.Maps.PlaceInfo: ...
    @winrt_commethod(8)
    def CreateFromIdentifier(self, identifier: WinRT_String) -> Windows.Services.Maps.PlaceInfo: ...
    @winrt_commethod(9)
    def CreateFromIdentifierWithOptions(self, identifier: WinRT_String, defaultPoint: Windows.Devices.Geolocation.Geopoint, options: Windows.Services.Maps.PlaceInfoCreateOptions) -> Windows.Services.Maps.PlaceInfo: ...
    @winrt_commethod(10)
    def CreateFromMapLocation(self, location: Windows.Services.Maps.MapLocation) -> Windows.Services.Maps.PlaceInfo: ...
    @winrt_commethod(11)
    def get_IsShowSupported(self) -> Boolean: ...
    IsShowSupported = property(get_IsShowSupported, None)
class IPlaceInfoStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('730f0249-4047-44a3-8f-81-25-50-a5-21-63-70')
    @winrt_commethod(6)
    def CreateFromAddress(self, displayAddress: WinRT_String) -> Windows.Services.Maps.PlaceInfo: ...
    @winrt_commethod(7)
    def CreateFromAddressWithName(self, displayAddress: WinRT_String, displayName: WinRT_String) -> Windows.Services.Maps.PlaceInfo: ...
LocalSearchContract: UInt32 = 262144
class ManeuverWarning(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Maps.ManeuverWarning'
    @winrt_mixinmethod
    def get_Kind(self: Windows.Services.Maps.IManeuverWarning) -> Windows.Services.Maps.ManeuverWarningKind: ...
    @winrt_mixinmethod
    def get_Severity(self: Windows.Services.Maps.IManeuverWarning) -> Windows.Services.Maps.ManeuverWarningSeverity: ...
    Kind = property(get_Kind, None)
    Severity = property(get_Severity, None)
ManeuverWarningKind = Int32
ManeuverWarningKind_None: ManeuverWarningKind = 0
ManeuverWarningKind_Accident: ManeuverWarningKind = 1
ManeuverWarningKind_AdministrativeDivisionChange: ManeuverWarningKind = 2
ManeuverWarningKind_Alert: ManeuverWarningKind = 3
ManeuverWarningKind_BlockedRoad: ManeuverWarningKind = 4
ManeuverWarningKind_CheckTimetable: ManeuverWarningKind = 5
ManeuverWarningKind_Congestion: ManeuverWarningKind = 6
ManeuverWarningKind_Construction: ManeuverWarningKind = 7
ManeuverWarningKind_CountryChange: ManeuverWarningKind = 8
ManeuverWarningKind_DisabledVehicle: ManeuverWarningKind = 9
ManeuverWarningKind_GateAccess: ManeuverWarningKind = 10
ManeuverWarningKind_GetOffTransit: ManeuverWarningKind = 11
ManeuverWarningKind_GetOnTransit: ManeuverWarningKind = 12
ManeuverWarningKind_IllegalUTurn: ManeuverWarningKind = 13
ManeuverWarningKind_MassTransit: ManeuverWarningKind = 14
ManeuverWarningKind_Miscellaneous: ManeuverWarningKind = 15
ManeuverWarningKind_NoIncident: ManeuverWarningKind = 16
ManeuverWarningKind_Other: ManeuverWarningKind = 17
ManeuverWarningKind_OtherNews: ManeuverWarningKind = 18
ManeuverWarningKind_OtherTrafficIncidents: ManeuverWarningKind = 19
ManeuverWarningKind_PlannedEvent: ManeuverWarningKind = 20
ManeuverWarningKind_PrivateRoad: ManeuverWarningKind = 21
ManeuverWarningKind_RestrictedTurn: ManeuverWarningKind = 22
ManeuverWarningKind_RoadClosures: ManeuverWarningKind = 23
ManeuverWarningKind_RoadHazard: ManeuverWarningKind = 24
ManeuverWarningKind_ScheduledConstruction: ManeuverWarningKind = 25
ManeuverWarningKind_SeasonalClosures: ManeuverWarningKind = 26
ManeuverWarningKind_Tollbooth: ManeuverWarningKind = 27
ManeuverWarningKind_TollRoad: ManeuverWarningKind = 28
ManeuverWarningKind_TollZoneEnter: ManeuverWarningKind = 29
ManeuverWarningKind_TollZoneExit: ManeuverWarningKind = 30
ManeuverWarningKind_TrafficFlow: ManeuverWarningKind = 31
ManeuverWarningKind_TransitLineChange: ManeuverWarningKind = 32
ManeuverWarningKind_UnpavedRoad: ManeuverWarningKind = 33
ManeuverWarningKind_UnscheduledConstruction: ManeuverWarningKind = 34
ManeuverWarningKind_Weather: ManeuverWarningKind = 35
ManeuverWarningSeverity = Int32
ManeuverWarningSeverity_None: ManeuverWarningSeverity = 0
ManeuverWarningSeverity_LowImpact: ManeuverWarningSeverity = 1
ManeuverWarningSeverity_Minor: ManeuverWarningSeverity = 2
ManeuverWarningSeverity_Moderate: ManeuverWarningSeverity = 3
ManeuverWarningSeverity_Serious: ManeuverWarningSeverity = 4
class MapAddress(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Maps.MapAddress'
    @winrt_mixinmethod
    def get_BuildingName(self: Windows.Services.Maps.IMapAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_BuildingFloor(self: Windows.Services.Maps.IMapAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_BuildingRoom(self: Windows.Services.Maps.IMapAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_BuildingWing(self: Windows.Services.Maps.IMapAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_StreetNumber(self: Windows.Services.Maps.IMapAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Street(self: Windows.Services.Maps.IMapAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Neighborhood(self: Windows.Services.Maps.IMapAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_District(self: Windows.Services.Maps.IMapAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Town(self: Windows.Services.Maps.IMapAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Region(self: Windows.Services.Maps.IMapAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_RegionCode(self: Windows.Services.Maps.IMapAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Country(self: Windows.Services.Maps.IMapAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_CountryCode(self: Windows.Services.Maps.IMapAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_PostCode(self: Windows.Services.Maps.IMapAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Continent(self: Windows.Services.Maps.IMapAddress) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_FormattedAddress(self: Windows.Services.Maps.IMapAddress2) -> WinRT_String: ...
    BuildingName = property(get_BuildingName, None)
    BuildingFloor = property(get_BuildingFloor, None)
    BuildingRoom = property(get_BuildingRoom, None)
    BuildingWing = property(get_BuildingWing, None)
    StreetNumber = property(get_StreetNumber, None)
    Street = property(get_Street, None)
    Neighborhood = property(get_Neighborhood, None)
    District = property(get_District, None)
    Town = property(get_Town, None)
    Region = property(get_Region, None)
    RegionCode = property(get_RegionCode, None)
    Country = property(get_Country, None)
    CountryCode = property(get_CountryCode, None)
    PostCode = property(get_PostCode, None)
    Continent = property(get_Continent, None)
    FormattedAddress = property(get_FormattedAddress, None)
class MapLocation(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Maps.MapLocation'
    @winrt_mixinmethod
    def get_Point(self: Windows.Services.Maps.IMapLocation) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Services.Maps.IMapLocation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Description(self: Windows.Services.Maps.IMapLocation) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Address(self: Windows.Services.Maps.IMapLocation) -> Windows.Services.Maps.MapAddress: ...
    Point = property(get_Point, None)
    DisplayName = property(get_DisplayName, None)
    Description = property(get_Description, None)
    Address = property(get_Address, None)
MapLocationDesiredAccuracy = Int32
MapLocationDesiredAccuracy_High: MapLocationDesiredAccuracy = 0
MapLocationDesiredAccuracy_Low: MapLocationDesiredAccuracy = 1
class MapLocationFinder(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Maps.MapLocationFinder'
    @winrt_classmethod
    def FindLocationsAtWithAccuracyAsync(cls: Windows.Services.Maps.IMapLocationFinderStatics2, queryPoint: Windows.Devices.Geolocation.Geopoint, accuracy: Windows.Services.Maps.MapLocationDesiredAccuracy) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapLocationFinderResult]: ...
    @winrt_classmethod
    def FindLocationsAtAsync(cls: Windows.Services.Maps.IMapLocationFinderStatics, queryPoint: Windows.Devices.Geolocation.Geopoint) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapLocationFinderResult]: ...
    @winrt_classmethod
    def FindLocationsAsync(cls: Windows.Services.Maps.IMapLocationFinderStatics, searchText: WinRT_String, referencePoint: Windows.Devices.Geolocation.Geopoint) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapLocationFinderResult]: ...
    @winrt_classmethod
    def FindLocationsWithMaxCountAsync(cls: Windows.Services.Maps.IMapLocationFinderStatics, searchText: WinRT_String, referencePoint: Windows.Devices.Geolocation.Geopoint, maxCount: UInt32) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapLocationFinderResult]: ...
class MapLocationFinderResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Maps.MapLocationFinderResult'
    @winrt_mixinmethod
    def get_Locations(self: Windows.Services.Maps.IMapLocationFinderResult) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Maps.MapLocation]: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Services.Maps.IMapLocationFinderResult) -> Windows.Services.Maps.MapLocationFinderStatus: ...
    Locations = property(get_Locations, None)
    Status = property(get_Status, None)
MapLocationFinderStatus = Int32
MapLocationFinderStatus_Success: MapLocationFinderStatus = 0
MapLocationFinderStatus_UnknownError: MapLocationFinderStatus = 1
MapLocationFinderStatus_InvalidCredentials: MapLocationFinderStatus = 2
MapLocationFinderStatus_BadLocation: MapLocationFinderStatus = 3
MapLocationFinderStatus_IndexFailure: MapLocationFinderStatus = 4
MapLocationFinderStatus_NetworkFailure: MapLocationFinderStatus = 5
MapLocationFinderStatus_NotSupported: MapLocationFinderStatus = 6
class MapManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Maps.MapManager'
    @winrt_classmethod
    def ShowDownloadedMapsUI(cls: Windows.Services.Maps.IMapManagerStatics) -> Void: ...
    @winrt_classmethod
    def ShowMapsUpdateUI(cls: Windows.Services.Maps.IMapManagerStatics) -> Void: ...
MapManeuverNotices = UInt32
MapManeuverNotices_None: MapManeuverNotices = 0
MapManeuverNotices_Toll: MapManeuverNotices = 1
MapManeuverNotices_Unpaved: MapManeuverNotices = 2
class MapRoute(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Maps.MapRoute'
    @winrt_mixinmethod
    def get_BoundingBox(self: Windows.Services.Maps.IMapRoute) -> Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_mixinmethod
    def get_LengthInMeters(self: Windows.Services.Maps.IMapRoute) -> Double: ...
    @winrt_mixinmethod
    def get_EstimatedDuration(self: Windows.Services.Maps.IMapRoute) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Path(self: Windows.Services.Maps.IMapRoute) -> Windows.Devices.Geolocation.Geopath: ...
    @winrt_mixinmethod
    def get_Legs(self: Windows.Services.Maps.IMapRoute) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Maps.MapRouteLeg]: ...
    @winrt_mixinmethod
    def get_IsTrafficBased(self: Windows.Services.Maps.IMapRoute) -> Boolean: ...
    @winrt_mixinmethod
    def get_ViolatedRestrictions(self: Windows.Services.Maps.IMapRoute2) -> Windows.Services.Maps.MapRouteRestrictions: ...
    @winrt_mixinmethod
    def get_HasBlockedRoads(self: Windows.Services.Maps.IMapRoute2) -> Boolean: ...
    @winrt_mixinmethod
    def get_DurationWithoutTraffic(self: Windows.Services.Maps.IMapRoute3) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_TrafficCongestion(self: Windows.Services.Maps.IMapRoute3) -> Windows.Services.Maps.TrafficCongestion: ...
    @winrt_mixinmethod
    def get_IsScenic(self: Windows.Services.Maps.IMapRoute4) -> Boolean: ...
    BoundingBox = property(get_BoundingBox, None)
    LengthInMeters = property(get_LengthInMeters, None)
    EstimatedDuration = property(get_EstimatedDuration, None)
    Path = property(get_Path, None)
    Legs = property(get_Legs, None)
    IsTrafficBased = property(get_IsTrafficBased, None)
    ViolatedRestrictions = property(get_ViolatedRestrictions, None)
    HasBlockedRoads = property(get_HasBlockedRoads, None)
    DurationWithoutTraffic = property(get_DurationWithoutTraffic, None)
    TrafficCongestion = property(get_TrafficCongestion, None)
    IsScenic = property(get_IsScenic, None)
class MapRouteDrivingOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Maps.MapRouteDrivingOptions'
    @winrt_activatemethod
    def New(cls) -> Windows.Services.Maps.MapRouteDrivingOptions: ...
    @winrt_mixinmethod
    def get_MaxAlternateRouteCount(self: Windows.Services.Maps.IMapRouteDrivingOptions) -> UInt32: ...
    @winrt_mixinmethod
    def put_MaxAlternateRouteCount(self: Windows.Services.Maps.IMapRouteDrivingOptions, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_InitialHeading(self: Windows.Services.Maps.IMapRouteDrivingOptions) -> Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def put_InitialHeading(self: Windows.Services.Maps.IMapRouteDrivingOptions, value: Windows.Foundation.IReference[Double]) -> Void: ...
    @winrt_mixinmethod
    def get_RouteOptimization(self: Windows.Services.Maps.IMapRouteDrivingOptions) -> Windows.Services.Maps.MapRouteOptimization: ...
    @winrt_mixinmethod
    def put_RouteOptimization(self: Windows.Services.Maps.IMapRouteDrivingOptions, value: Windows.Services.Maps.MapRouteOptimization) -> Void: ...
    @winrt_mixinmethod
    def get_RouteRestrictions(self: Windows.Services.Maps.IMapRouteDrivingOptions) -> Windows.Services.Maps.MapRouteRestrictions: ...
    @winrt_mixinmethod
    def put_RouteRestrictions(self: Windows.Services.Maps.IMapRouteDrivingOptions, value: Windows.Services.Maps.MapRouteRestrictions) -> Void: ...
    @winrt_mixinmethod
    def get_DepartureTime(self: Windows.Services.Maps.IMapRouteDrivingOptions2) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_DepartureTime(self: Windows.Services.Maps.IMapRouteDrivingOptions2, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    MaxAlternateRouteCount = property(get_MaxAlternateRouteCount, put_MaxAlternateRouteCount)
    InitialHeading = property(get_InitialHeading, put_InitialHeading)
    RouteOptimization = property(get_RouteOptimization, put_RouteOptimization)
    RouteRestrictions = property(get_RouteRestrictions, put_RouteRestrictions)
    DepartureTime = property(get_DepartureTime, put_DepartureTime)
class MapRouteFinder(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Maps.MapRouteFinder'
    @winrt_classmethod
    def GetDrivingRouteFromEnhancedWaypointsAsync(cls: Windows.Services.Maps.IMapRouteFinderStatics3, waypoints: Windows.Foundation.Collections.IIterable[Windows.Services.Maps.EnhancedWaypoint]) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_classmethod
    def GetDrivingRouteFromEnhancedWaypointsWithOptionsAsync(cls: Windows.Services.Maps.IMapRouteFinderStatics3, waypoints: Windows.Foundation.Collections.IIterable[Windows.Services.Maps.EnhancedWaypoint], options: Windows.Services.Maps.MapRouteDrivingOptions) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_classmethod
    def GetDrivingRouteWithOptionsAsync(cls: Windows.Services.Maps.IMapRouteFinderStatics2, startPoint: Windows.Devices.Geolocation.Geopoint, endPoint: Windows.Devices.Geolocation.Geopoint, options: Windows.Services.Maps.MapRouteDrivingOptions) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_classmethod
    def GetDrivingRouteAsync(cls: Windows.Services.Maps.IMapRouteFinderStatics, startPoint: Windows.Devices.Geolocation.Geopoint, endPoint: Windows.Devices.Geolocation.Geopoint) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_classmethod
    def GetDrivingRouteWithOptimizationAsync(cls: Windows.Services.Maps.IMapRouteFinderStatics, startPoint: Windows.Devices.Geolocation.Geopoint, endPoint: Windows.Devices.Geolocation.Geopoint, optimization: Windows.Services.Maps.MapRouteOptimization) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_classmethod
    def GetDrivingRouteWithOptimizationAndRestrictionsAsync(cls: Windows.Services.Maps.IMapRouteFinderStatics, startPoint: Windows.Devices.Geolocation.Geopoint, endPoint: Windows.Devices.Geolocation.Geopoint, optimization: Windows.Services.Maps.MapRouteOptimization, restrictions: Windows.Services.Maps.MapRouteRestrictions) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_classmethod
    def GetDrivingRouteWithOptimizationRestrictionsAndHeadingAsync(cls: Windows.Services.Maps.IMapRouteFinderStatics, startPoint: Windows.Devices.Geolocation.Geopoint, endPoint: Windows.Devices.Geolocation.Geopoint, optimization: Windows.Services.Maps.MapRouteOptimization, restrictions: Windows.Services.Maps.MapRouteRestrictions, headingInDegrees: Double) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_classmethod
    def GetDrivingRouteFromWaypointsAsync(cls: Windows.Services.Maps.IMapRouteFinderStatics, wayPoints: Windows.Foundation.Collections.IIterable[Windows.Devices.Geolocation.Geopoint]) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_classmethod
    def GetDrivingRouteFromWaypointsAndOptimizationAsync(cls: Windows.Services.Maps.IMapRouteFinderStatics, wayPoints: Windows.Foundation.Collections.IIterable[Windows.Devices.Geolocation.Geopoint], optimization: Windows.Services.Maps.MapRouteOptimization) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_classmethod
    def GetDrivingRouteFromWaypointsOptimizationAndRestrictionsAsync(cls: Windows.Services.Maps.IMapRouteFinderStatics, wayPoints: Windows.Foundation.Collections.IIterable[Windows.Devices.Geolocation.Geopoint], optimization: Windows.Services.Maps.MapRouteOptimization, restrictions: Windows.Services.Maps.MapRouteRestrictions) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_classmethod
    def GetDrivingRouteFromWaypointsOptimizationRestrictionsAndHeadingAsync(cls: Windows.Services.Maps.IMapRouteFinderStatics, wayPoints: Windows.Foundation.Collections.IIterable[Windows.Devices.Geolocation.Geopoint], optimization: Windows.Services.Maps.MapRouteOptimization, restrictions: Windows.Services.Maps.MapRouteRestrictions, headingInDegrees: Double) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_classmethod
    def GetWalkingRouteAsync(cls: Windows.Services.Maps.IMapRouteFinderStatics, startPoint: Windows.Devices.Geolocation.Geopoint, endPoint: Windows.Devices.Geolocation.Geopoint) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapRouteFinderResult]: ...
    @winrt_classmethod
    def GetWalkingRouteFromWaypointsAsync(cls: Windows.Services.Maps.IMapRouteFinderStatics, wayPoints: Windows.Foundation.Collections.IIterable[Windows.Devices.Geolocation.Geopoint]) -> Windows.Foundation.IAsyncOperation[Windows.Services.Maps.MapRouteFinderResult]: ...
class MapRouteFinderResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Maps.MapRouteFinderResult'
    @winrt_mixinmethod
    def get_Route(self: Windows.Services.Maps.IMapRouteFinderResult) -> Windows.Services.Maps.MapRoute: ...
    @winrt_mixinmethod
    def get_Status(self: Windows.Services.Maps.IMapRouteFinderResult) -> Windows.Services.Maps.MapRouteFinderStatus: ...
    @winrt_mixinmethod
    def get_AlternateRoutes(self: Windows.Services.Maps.IMapRouteFinderResult2) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Maps.MapRoute]: ...
    Route = property(get_Route, None)
    Status = property(get_Status, None)
    AlternateRoutes = property(get_AlternateRoutes, None)
MapRouteFinderStatus = Int32
MapRouteFinderStatus_Success: MapRouteFinderStatus = 0
MapRouteFinderStatus_UnknownError: MapRouteFinderStatus = 1
MapRouteFinderStatus_InvalidCredentials: MapRouteFinderStatus = 2
MapRouteFinderStatus_NoRouteFound: MapRouteFinderStatus = 3
MapRouteFinderStatus_NoRouteFoundWithGivenOptions: MapRouteFinderStatus = 4
MapRouteFinderStatus_StartPointNotFound: MapRouteFinderStatus = 5
MapRouteFinderStatus_EndPointNotFound: MapRouteFinderStatus = 6
MapRouteFinderStatus_NoPedestrianRouteFound: MapRouteFinderStatus = 7
MapRouteFinderStatus_NetworkFailure: MapRouteFinderStatus = 8
MapRouteFinderStatus_NotSupported: MapRouteFinderStatus = 9
class MapRouteLeg(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Maps.MapRouteLeg'
    @winrt_mixinmethod
    def get_BoundingBox(self: Windows.Services.Maps.IMapRouteLeg) -> Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_mixinmethod
    def get_Path(self: Windows.Services.Maps.IMapRouteLeg) -> Windows.Devices.Geolocation.Geopath: ...
    @winrt_mixinmethod
    def get_LengthInMeters(self: Windows.Services.Maps.IMapRouteLeg) -> Double: ...
    @winrt_mixinmethod
    def get_EstimatedDuration(self: Windows.Services.Maps.IMapRouteLeg) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Maneuvers(self: Windows.Services.Maps.IMapRouteLeg) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Maps.MapRouteManeuver]: ...
    @winrt_mixinmethod
    def get_DurationWithoutTraffic(self: Windows.Services.Maps.IMapRouteLeg2) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_TrafficCongestion(self: Windows.Services.Maps.IMapRouteLeg2) -> Windows.Services.Maps.TrafficCongestion: ...
    BoundingBox = property(get_BoundingBox, None)
    Path = property(get_Path, None)
    LengthInMeters = property(get_LengthInMeters, None)
    EstimatedDuration = property(get_EstimatedDuration, None)
    Maneuvers = property(get_Maneuvers, None)
    DurationWithoutTraffic = property(get_DurationWithoutTraffic, None)
    TrafficCongestion = property(get_TrafficCongestion, None)
class MapRouteManeuver(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Maps.MapRouteManeuver'
    @winrt_mixinmethod
    def get_StartingPoint(self: Windows.Services.Maps.IMapRouteManeuver) -> Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_LengthInMeters(self: Windows.Services.Maps.IMapRouteManeuver) -> Double: ...
    @winrt_mixinmethod
    def get_InstructionText(self: Windows.Services.Maps.IMapRouteManeuver) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.Services.Maps.IMapRouteManeuver) -> Windows.Services.Maps.MapRouteManeuverKind: ...
    @winrt_mixinmethod
    def get_ExitNumber(self: Windows.Services.Maps.IMapRouteManeuver) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ManeuverNotices(self: Windows.Services.Maps.IMapRouteManeuver) -> Windows.Services.Maps.MapManeuverNotices: ...
    @winrt_mixinmethod
    def get_StartHeading(self: Windows.Services.Maps.IMapRouteManeuver2) -> Double: ...
    @winrt_mixinmethod
    def get_EndHeading(self: Windows.Services.Maps.IMapRouteManeuver2) -> Double: ...
    @winrt_mixinmethod
    def get_StreetName(self: Windows.Services.Maps.IMapRouteManeuver2) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Warnings(self: Windows.Services.Maps.IMapRouteManeuver3) -> Windows.Foundation.Collections.IVectorView[Windows.Services.Maps.ManeuverWarning]: ...
    StartingPoint = property(get_StartingPoint, None)
    LengthInMeters = property(get_LengthInMeters, None)
    InstructionText = property(get_InstructionText, None)
    Kind = property(get_Kind, None)
    ExitNumber = property(get_ExitNumber, None)
    ManeuverNotices = property(get_ManeuverNotices, None)
    StartHeading = property(get_StartHeading, None)
    EndHeading = property(get_EndHeading, None)
    StreetName = property(get_StreetName, None)
    Warnings = property(get_Warnings, None)
MapRouteManeuverKind = Int32
MapRouteManeuverKind_None: MapRouteManeuverKind = 0
MapRouteManeuverKind_Start: MapRouteManeuverKind = 1
MapRouteManeuverKind_Stopover: MapRouteManeuverKind = 2
MapRouteManeuverKind_StopoverResume: MapRouteManeuverKind = 3
MapRouteManeuverKind_End: MapRouteManeuverKind = 4
MapRouteManeuverKind_GoStraight: MapRouteManeuverKind = 5
MapRouteManeuverKind_UTurnLeft: MapRouteManeuverKind = 6
MapRouteManeuverKind_UTurnRight: MapRouteManeuverKind = 7
MapRouteManeuverKind_TurnKeepLeft: MapRouteManeuverKind = 8
MapRouteManeuverKind_TurnKeepRight: MapRouteManeuverKind = 9
MapRouteManeuverKind_TurnLightLeft: MapRouteManeuverKind = 10
MapRouteManeuverKind_TurnLightRight: MapRouteManeuverKind = 11
MapRouteManeuverKind_TurnLeft: MapRouteManeuverKind = 12
MapRouteManeuverKind_TurnRight: MapRouteManeuverKind = 13
MapRouteManeuverKind_TurnHardLeft: MapRouteManeuverKind = 14
MapRouteManeuverKind_TurnHardRight: MapRouteManeuverKind = 15
MapRouteManeuverKind_FreewayEnterLeft: MapRouteManeuverKind = 16
MapRouteManeuverKind_FreewayEnterRight: MapRouteManeuverKind = 17
MapRouteManeuverKind_FreewayLeaveLeft: MapRouteManeuverKind = 18
MapRouteManeuverKind_FreewayLeaveRight: MapRouteManeuverKind = 19
MapRouteManeuverKind_FreewayContinueLeft: MapRouteManeuverKind = 20
MapRouteManeuverKind_FreewayContinueRight: MapRouteManeuverKind = 21
MapRouteManeuverKind_TrafficCircleLeft: MapRouteManeuverKind = 22
MapRouteManeuverKind_TrafficCircleRight: MapRouteManeuverKind = 23
MapRouteManeuverKind_TakeFerry: MapRouteManeuverKind = 24
MapRouteOptimization = Int32
MapRouteOptimization_Time: MapRouteOptimization = 0
MapRouteOptimization_Distance: MapRouteOptimization = 1
MapRouteOptimization_TimeWithTraffic: MapRouteOptimization = 2
MapRouteOptimization_Scenic: MapRouteOptimization = 3
MapRouteRestrictions = UInt32
MapRouteRestrictions_None: MapRouteRestrictions = 0
MapRouteRestrictions_Highways: MapRouteRestrictions = 1
MapRouteRestrictions_TollRoads: MapRouteRestrictions = 2
MapRouteRestrictions_Ferries: MapRouteRestrictions = 4
MapRouteRestrictions_Tunnels: MapRouteRestrictions = 8
MapRouteRestrictions_DirtRoads: MapRouteRestrictions = 16
MapRouteRestrictions_Motorail: MapRouteRestrictions = 32
class MapService(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Maps.MapService'
    @winrt_classmethod
    def put_DataUsagePreference(cls: Windows.Services.Maps.IMapServiceStatics4, value: Windows.Services.Maps.MapServiceDataUsagePreference) -> Void: ...
    @winrt_classmethod
    def get_DataUsagePreference(cls: Windows.Services.Maps.IMapServiceStatics4) -> Windows.Services.Maps.MapServiceDataUsagePreference: ...
    @winrt_classmethod
    def get_DataAttributions(cls: Windows.Services.Maps.IMapServiceStatics3) -> WinRT_String: ...
    @winrt_classmethod
    def get_WorldViewRegionCode(cls: Windows.Services.Maps.IMapServiceStatics2) -> WinRT_String: ...
    @winrt_classmethod
    def put_ServiceToken(cls: Windows.Services.Maps.IMapServiceStatics, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_ServiceToken(cls: Windows.Services.Maps.IMapServiceStatics) -> WinRT_String: ...
    DataUsagePreference = property(get_DataUsagePreference, put_DataUsagePreference)
    DataAttributions = property(get_DataAttributions, None)
    WorldViewRegionCode = property(get_WorldViewRegionCode, None)
    ServiceToken = property(get_ServiceToken, put_ServiceToken)
MapServiceDataUsagePreference = Int32
MapServiceDataUsagePreference_Default: MapServiceDataUsagePreference = 0
MapServiceDataUsagePreference_OfflineMapDataOnly: MapServiceDataUsagePreference = 1
class PlaceInfo(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Maps.PlaceInfo'
    @winrt_mixinmethod
    def Show(self: Windows.Services.Maps.IPlaceInfo, selection: Windows.Foundation.Rect) -> Void: ...
    @winrt_mixinmethod
    def ShowWithPreferredPlacement(self: Windows.Services.Maps.IPlaceInfo, selection: Windows.Foundation.Rect, preferredPlacement: Windows.UI.Popups.Placement) -> Void: ...
    @winrt_mixinmethod
    def get_Identifier(self: Windows.Services.Maps.IPlaceInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Services.Maps.IPlaceInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DisplayAddress(self: Windows.Services.Maps.IPlaceInfo) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Geoshape(self: Windows.Services.Maps.IPlaceInfo) -> Windows.Devices.Geolocation.IGeoshape: ...
    @winrt_classmethod
    def CreateFromAddress(cls: Windows.Services.Maps.IPlaceInfoStatics2, displayAddress: WinRT_String) -> Windows.Services.Maps.PlaceInfo: ...
    @winrt_classmethod
    def CreateFromAddressWithName(cls: Windows.Services.Maps.IPlaceInfoStatics2, displayAddress: WinRT_String, displayName: WinRT_String) -> Windows.Services.Maps.PlaceInfo: ...
    @winrt_classmethod
    def Create(cls: Windows.Services.Maps.IPlaceInfoStatics, referencePoint: Windows.Devices.Geolocation.Geopoint) -> Windows.Services.Maps.PlaceInfo: ...
    @winrt_classmethod
    def CreateWithGeopointAndOptions(cls: Windows.Services.Maps.IPlaceInfoStatics, referencePoint: Windows.Devices.Geolocation.Geopoint, options: Windows.Services.Maps.PlaceInfoCreateOptions) -> Windows.Services.Maps.PlaceInfo: ...
    @winrt_classmethod
    def CreateFromIdentifier(cls: Windows.Services.Maps.IPlaceInfoStatics, identifier: WinRT_String) -> Windows.Services.Maps.PlaceInfo: ...
    @winrt_classmethod
    def CreateFromIdentifierWithOptions(cls: Windows.Services.Maps.IPlaceInfoStatics, identifier: WinRT_String, defaultPoint: Windows.Devices.Geolocation.Geopoint, options: Windows.Services.Maps.PlaceInfoCreateOptions) -> Windows.Services.Maps.PlaceInfo: ...
    @winrt_classmethod
    def CreateFromMapLocation(cls: Windows.Services.Maps.IPlaceInfoStatics, location: Windows.Services.Maps.MapLocation) -> Windows.Services.Maps.PlaceInfo: ...
    @winrt_classmethod
    def get_IsShowSupported(cls: Windows.Services.Maps.IPlaceInfoStatics) -> Boolean: ...
    Identifier = property(get_Identifier, None)
    DisplayName = property(get_DisplayName, None)
    DisplayAddress = property(get_DisplayAddress, None)
    Geoshape = property(get_Geoshape, None)
    IsShowSupported = property(get_IsShowSupported, None)
class PlaceInfoCreateOptions(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.Services.Maps.PlaceInfoCreateOptions'
    @winrt_activatemethod
    def New(cls) -> Windows.Services.Maps.PlaceInfoCreateOptions: ...
    @winrt_mixinmethod
    def put_DisplayName(self: Windows.Services.Maps.IPlaceInfoCreateOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayName(self: Windows.Services.Maps.IPlaceInfoCreateOptions) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_DisplayAddress(self: Windows.Services.Maps.IPlaceInfoCreateOptions, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_DisplayAddress(self: Windows.Services.Maps.IPlaceInfoCreateOptions) -> WinRT_String: ...
    DisplayName = property(get_DisplayName, put_DisplayName)
    DisplayAddress = property(get_DisplayAddress, put_DisplayAddress)
TrafficCongestion = Int32
TrafficCongestion_Unknown: TrafficCongestion = 0
TrafficCongestion_Light: TrafficCongestion = 1
TrafficCongestion_Mild: TrafficCongestion = 2
TrafficCongestion_Medium: TrafficCongestion = 3
TrafficCongestion_Heavy: TrafficCongestion = 4
WaypointKind = Int32
WaypointKind_Stop: WaypointKind = 0
WaypointKind_Via: WaypointKind = 1
make_head(_module, 'EnhancedWaypoint')
make_head(_module, 'IEnhancedWaypoint')
make_head(_module, 'IEnhancedWaypointFactory')
make_head(_module, 'IManeuverWarning')
make_head(_module, 'IMapAddress')
make_head(_module, 'IMapAddress2')
make_head(_module, 'IMapLocation')
make_head(_module, 'IMapLocationFinderResult')
make_head(_module, 'IMapLocationFinderStatics')
make_head(_module, 'IMapLocationFinderStatics2')
make_head(_module, 'IMapManagerStatics')
make_head(_module, 'IMapRoute')
make_head(_module, 'IMapRoute2')
make_head(_module, 'IMapRoute3')
make_head(_module, 'IMapRoute4')
make_head(_module, 'IMapRouteDrivingOptions')
make_head(_module, 'IMapRouteDrivingOptions2')
make_head(_module, 'IMapRouteFinderResult')
make_head(_module, 'IMapRouteFinderResult2')
make_head(_module, 'IMapRouteFinderStatics')
make_head(_module, 'IMapRouteFinderStatics2')
make_head(_module, 'IMapRouteFinderStatics3')
make_head(_module, 'IMapRouteLeg')
make_head(_module, 'IMapRouteLeg2')
make_head(_module, 'IMapRouteManeuver')
make_head(_module, 'IMapRouteManeuver2')
make_head(_module, 'IMapRouteManeuver3')
make_head(_module, 'IMapServiceStatics')
make_head(_module, 'IMapServiceStatics2')
make_head(_module, 'IMapServiceStatics3')
make_head(_module, 'IMapServiceStatics4')
make_head(_module, 'IPlaceInfo')
make_head(_module, 'IPlaceInfoCreateOptions')
make_head(_module, 'IPlaceInfoStatics')
make_head(_module, 'IPlaceInfoStatics2')
make_head(_module, 'ManeuverWarning')
make_head(_module, 'MapAddress')
make_head(_module, 'MapLocation')
make_head(_module, 'MapLocationFinder')
make_head(_module, 'MapLocationFinderResult')
make_head(_module, 'MapManager')
make_head(_module, 'MapRoute')
make_head(_module, 'MapRouteDrivingOptions')
make_head(_module, 'MapRouteFinder')
make_head(_module, 'MapRouteFinderResult')
make_head(_module, 'MapRouteLeg')
make_head(_module, 'MapRouteManeuver')
make_head(_module, 'MapService')
make_head(_module, 'PlaceInfo')
make_head(_module, 'PlaceInfoCreateOptions')
