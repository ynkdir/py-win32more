from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Geolocation
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Services.Maps
import win32more.Windows.Services.Maps.Guidance
import win32more.Windows.UI
import win32more.Windows.Win32.System.WinRT
class GuidanceAudioMeasurementSystem(Enum, Int32):
    Meters = 0
    MilesAndYards = 1
    MilesAndFeet = 2
class GuidanceAudioNotificationKind(Enum, Int32):
    Maneuver = 0
    Route = 1
    Gps = 2
    SpeedLimit = 3
    Traffic = 4
    TrafficCamera = 5
class GuidanceAudioNotificationRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Maps.Guidance.IGuidanceAudioNotificationRequestedEventArgs
    _classid_ = 'Windows.Services.Maps.Guidance.GuidanceAudioNotificationRequestedEventArgs'
    @winrt_mixinmethod
    def get_AudioNotification(self: win32more.Windows.Services.Maps.Guidance.IGuidanceAudioNotificationRequestedEventArgs) -> win32more.Windows.Services.Maps.Guidance.GuidanceAudioNotificationKind: ...
    @winrt_mixinmethod
    def get_AudioFilePaths(self: win32more.Windows.Services.Maps.Guidance.IGuidanceAudioNotificationRequestedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def get_AudioText(self: win32more.Windows.Services.Maps.Guidance.IGuidanceAudioNotificationRequestedEventArgs) -> WinRT_String: ...
    AudioFilePaths = property(get_AudioFilePaths, None)
    AudioNotification = property(get_AudioNotification, None)
    AudioText = property(get_AudioText, None)
class GuidanceAudioNotifications(Enum, UInt32):
    None_ = 0
    Maneuver = 1
    Route = 2
    Gps = 4
    SpeedLimit = 8
    Traffic = 16
    TrafficCamera = 32
class GuidanceLaneInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Maps.Guidance.IGuidanceLaneInfo
    _classid_ = 'Windows.Services.Maps.Guidance.GuidanceLaneInfo'
    @winrt_mixinmethod
    def get_LaneMarkers(self: win32more.Windows.Services.Maps.Guidance.IGuidanceLaneInfo) -> win32more.Windows.Services.Maps.Guidance.GuidanceLaneMarkers: ...
    @winrt_mixinmethod
    def get_IsOnRoute(self: win32more.Windows.Services.Maps.Guidance.IGuidanceLaneInfo) -> Boolean: ...
    IsOnRoute = property(get_IsOnRoute, None)
    LaneMarkers = property(get_LaneMarkers, None)
class GuidanceLaneMarkers(Enum, UInt32):
    None_ = 0
    LightRight = 1
    Right = 2
    HardRight = 4
    Straight = 8
    UTurnLeft = 16
    HardLeft = 32
    Left = 64
    LightLeft = 128
    UTurnRight = 256
    Unknown = 4294967295
class GuidanceManeuver(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Maps.Guidance.IGuidanceManeuver
    _classid_ = 'Windows.Services.Maps.Guidance.GuidanceManeuver'
    @winrt_mixinmethod
    def get_StartLocation(self: win32more.Windows.Services.Maps.Guidance.IGuidanceManeuver) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_DistanceFromRouteStart(self: win32more.Windows.Services.Maps.Guidance.IGuidanceManeuver) -> Int32: ...
    @winrt_mixinmethod
    def get_DistanceFromPreviousManeuver(self: win32more.Windows.Services.Maps.Guidance.IGuidanceManeuver) -> Int32: ...
    @winrt_mixinmethod
    def get_DepartureRoadName(self: win32more.Windows.Services.Maps.Guidance.IGuidanceManeuver) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_NextRoadName(self: win32more.Windows.Services.Maps.Guidance.IGuidanceManeuver) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_DepartureShortRoadName(self: win32more.Windows.Services.Maps.Guidance.IGuidanceManeuver) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_NextShortRoadName(self: win32more.Windows.Services.Maps.Guidance.IGuidanceManeuver) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.Services.Maps.Guidance.IGuidanceManeuver) -> win32more.Windows.Services.Maps.Guidance.GuidanceManeuverKind: ...
    @winrt_mixinmethod
    def get_StartAngle(self: win32more.Windows.Services.Maps.Guidance.IGuidanceManeuver) -> Int32: ...
    @winrt_mixinmethod
    def get_EndAngle(self: win32more.Windows.Services.Maps.Guidance.IGuidanceManeuver) -> Int32: ...
    @winrt_mixinmethod
    def get_RoadSignpost(self: win32more.Windows.Services.Maps.Guidance.IGuidanceManeuver) -> win32more.Windows.Services.Maps.Guidance.GuidanceRoadSignpost: ...
    @winrt_mixinmethod
    def get_InstructionText(self: win32more.Windows.Services.Maps.Guidance.IGuidanceManeuver) -> WinRT_String: ...
    DepartureRoadName = property(get_DepartureRoadName, None)
    DepartureShortRoadName = property(get_DepartureShortRoadName, None)
    DistanceFromPreviousManeuver = property(get_DistanceFromPreviousManeuver, None)
    DistanceFromRouteStart = property(get_DistanceFromRouteStart, None)
    EndAngle = property(get_EndAngle, None)
    InstructionText = property(get_InstructionText, None)
    Kind = property(get_Kind, None)
    NextRoadName = property(get_NextRoadName, None)
    NextShortRoadName = property(get_NextShortRoadName, None)
    RoadSignpost = property(get_RoadSignpost, None)
    StartAngle = property(get_StartAngle, None)
    StartLocation = property(get_StartLocation, None)
class GuidanceManeuverKind(Enum, Int32):
    None_ = 0
    GoStraight = 1
    UTurnRight = 2
    UTurnLeft = 3
    TurnKeepRight = 4
    TurnLightRight = 5
    TurnRight = 6
    TurnHardRight = 7
    KeepMiddle = 8
    TurnKeepLeft = 9
    TurnLightLeft = 10
    TurnLeft = 11
    TurnHardLeft = 12
    FreewayEnterRight = 13
    FreewayEnterLeft = 14
    FreewayLeaveRight = 15
    FreewayLeaveLeft = 16
    FreewayKeepRight = 17
    FreewayKeepLeft = 18
    TrafficCircleRight1 = 19
    TrafficCircleRight2 = 20
    TrafficCircleRight3 = 21
    TrafficCircleRight4 = 22
    TrafficCircleRight5 = 23
    TrafficCircleRight6 = 24
    TrafficCircleRight7 = 25
    TrafficCircleRight8 = 26
    TrafficCircleRight9 = 27
    TrafficCircleRight10 = 28
    TrafficCircleRight11 = 29
    TrafficCircleRight12 = 30
    TrafficCircleLeft1 = 31
    TrafficCircleLeft2 = 32
    TrafficCircleLeft3 = 33
    TrafficCircleLeft4 = 34
    TrafficCircleLeft5 = 35
    TrafficCircleLeft6 = 36
    TrafficCircleLeft7 = 37
    TrafficCircleLeft8 = 38
    TrafficCircleLeft9 = 39
    TrafficCircleLeft10 = 40
    TrafficCircleLeft11 = 41
    TrafficCircleLeft12 = 42
    Start = 43
    End = 44
    TakeFerry = 45
    PassTransitStation = 46
    LeaveTransitStation = 47
class GuidanceMapMatchedCoordinate(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Maps.Guidance.IGuidanceMapMatchedCoordinate
    _classid_ = 'Windows.Services.Maps.Guidance.GuidanceMapMatchedCoordinate'
    @winrt_mixinmethod
    def get_Location(self: win32more.Windows.Services.Maps.Guidance.IGuidanceMapMatchedCoordinate) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_mixinmethod
    def get_CurrentHeading(self: win32more.Windows.Services.Maps.Guidance.IGuidanceMapMatchedCoordinate) -> Double: ...
    @winrt_mixinmethod
    def get_CurrentSpeed(self: win32more.Windows.Services.Maps.Guidance.IGuidanceMapMatchedCoordinate) -> Double: ...
    @winrt_mixinmethod
    def get_IsOnStreet(self: win32more.Windows.Services.Maps.Guidance.IGuidanceMapMatchedCoordinate) -> Boolean: ...
    @winrt_mixinmethod
    def get_Road(self: win32more.Windows.Services.Maps.Guidance.IGuidanceMapMatchedCoordinate) -> win32more.Windows.Services.Maps.Guidance.GuidanceRoadSegment: ...
    CurrentHeading = property(get_CurrentHeading, None)
    CurrentSpeed = property(get_CurrentSpeed, None)
    IsOnStreet = property(get_IsOnStreet, None)
    Location = property(get_Location, None)
    Road = property(get_Road, None)
class GuidanceMode(Enum, Int32):
    None_ = 0
    Simulation = 1
    Navigation = 2
    Tracking = 3
class _GuidanceNavigator_Meta_(ComPtr.__class__):
    pass
class GuidanceNavigator(ComPtr, metaclass=_GuidanceNavigator_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator
    _classid_ = 'Windows.Services.Maps.Guidance.GuidanceNavigator'
    @winrt_mixinmethod
    def StartNavigating(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, route: win32more.Windows.Services.Maps.Guidance.GuidanceRoute) -> Void: ...
    @winrt_mixinmethod
    def StartSimulating(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, route: win32more.Windows.Services.Maps.Guidance.GuidanceRoute, speedInMetersPerSecond: Int32) -> Void: ...
    @winrt_mixinmethod
    def StartTracking(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator) -> Void: ...
    @winrt_mixinmethod
    def Pause(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator) -> Void: ...
    @winrt_mixinmethod
    def Resume(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator) -> Void: ...
    @winrt_mixinmethod
    def Stop(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator) -> Void: ...
    @winrt_mixinmethod
    def RepeatLastAudioNotification(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator) -> Void: ...
    @winrt_mixinmethod
    def get_AudioMeasurementSystem(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator) -> win32more.Windows.Services.Maps.Guidance.GuidanceAudioMeasurementSystem: ...
    @winrt_mixinmethod
    def put_AudioMeasurementSystem(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, value: win32more.Windows.Services.Maps.Guidance.GuidanceAudioMeasurementSystem) -> Void: ...
    @winrt_mixinmethod
    def get_AudioNotifications(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator) -> win32more.Windows.Services.Maps.Guidance.GuidanceAudioNotifications: ...
    @winrt_mixinmethod
    def put_AudioNotifications(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, value: win32more.Windows.Services.Maps.Guidance.GuidanceAudioNotifications) -> Void: ...
    @winrt_mixinmethod
    def add_GuidanceUpdated(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.Guidance.GuidanceNavigator, win32more.Windows.Services.Maps.Guidance.GuidanceUpdatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_GuidanceUpdated(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DestinationReached(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.Guidance.GuidanceNavigator, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DestinationReached(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Rerouting(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.Guidance.GuidanceNavigator, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Rerouting(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Rerouted(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.Guidance.GuidanceNavigator, win32more.Windows.Services.Maps.Guidance.GuidanceReroutedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Rerouted(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_RerouteFailed(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.Guidance.GuidanceNavigator, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RerouteFailed(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UserLocationLost(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.Guidance.GuidanceNavigator, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UserLocationLost(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UserLocationRestored(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.Guidance.GuidanceNavigator, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UserLocationRestored(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def SetGuidanceVoice(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, voiceId: Int32, voiceFolder: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def UpdateUserLocation(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, userLocation: win32more.Windows.Devices.Geolocation.Geocoordinate) -> Void: ...
    @winrt_mixinmethod
    def UpdateUserLocationWithPositionOverride(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, userLocation: win32more.Windows.Devices.Geolocation.Geocoordinate, positionOverride: win32more.Windows.Devices.Geolocation.BasicGeoposition) -> Void: ...
    @winrt_mixinmethod
    def add_AudioNotificationRequested(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator2, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.Guidance.GuidanceNavigator, win32more.Windows.Services.Maps.Guidance.GuidanceAudioNotificationRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_AudioNotificationRequested(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_IsGuidanceAudioMuted(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsGuidanceAudioMuted(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator2, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_UseAppProvidedVoice(cls: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigatorStatics2) -> Boolean: ...
    @winrt_classmethod
    def GetCurrent(cls: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigatorStatics) -> win32more.Windows.Services.Maps.Guidance.GuidanceNavigator: ...
    AudioMeasurementSystem = property(get_AudioMeasurementSystem, put_AudioMeasurementSystem)
    AudioNotifications = property(get_AudioNotifications, put_AudioNotifications)
    IsGuidanceAudioMuted = property(get_IsGuidanceAudioMuted, put_IsGuidanceAudioMuted)
    _GuidanceNavigator_Meta_.UseAppProvidedVoice = property(get_UseAppProvidedVoice, None)
    GuidanceUpdated = event()
    DestinationReached = event()
    Rerouting = event()
    Rerouted = event()
    RerouteFailed = event()
    UserLocationLost = event()
    UserLocationRestored = event()
    AudioNotificationRequested = event()
class GuidanceReroutedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Maps.Guidance.IGuidanceReroutedEventArgs
    _classid_ = 'Windows.Services.Maps.Guidance.GuidanceReroutedEventArgs'
    @winrt_mixinmethod
    def get_Route(self: win32more.Windows.Services.Maps.Guidance.IGuidanceReroutedEventArgs) -> win32more.Windows.Services.Maps.Guidance.GuidanceRoute: ...
    Route = property(get_Route, None)
class GuidanceRoadSegment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Maps.Guidance.IGuidanceRoadSegment
    _classid_ = 'Windows.Services.Maps.Guidance.GuidanceRoadSegment'
    @winrt_mixinmethod
    def get_RoadName(self: win32more.Windows.Services.Maps.Guidance.IGuidanceRoadSegment) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ShortRoadName(self: win32more.Windows.Services.Maps.Guidance.IGuidanceRoadSegment) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_SpeedLimit(self: win32more.Windows.Services.Maps.Guidance.IGuidanceRoadSegment) -> Double: ...
    @winrt_mixinmethod
    def get_TravelTime(self: win32more.Windows.Services.Maps.Guidance.IGuidanceRoadSegment) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Path(self: win32more.Windows.Services.Maps.Guidance.IGuidanceRoadSegment) -> win32more.Windows.Devices.Geolocation.Geopath: ...
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.Services.Maps.Guidance.IGuidanceRoadSegment) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_IsHighway(self: win32more.Windows.Services.Maps.Guidance.IGuidanceRoadSegment) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsTunnel(self: win32more.Windows.Services.Maps.Guidance.IGuidanceRoadSegment) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsTollRoad(self: win32more.Windows.Services.Maps.Guidance.IGuidanceRoadSegment) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsScenic(self: win32more.Windows.Services.Maps.Guidance.IGuidanceRoadSegment2) -> Boolean: ...
    Id = property(get_Id, None)
    IsHighway = property(get_IsHighway, None)
    IsScenic = property(get_IsScenic, None)
    IsTollRoad = property(get_IsTollRoad, None)
    IsTunnel = property(get_IsTunnel, None)
    Path = property(get_Path, None)
    RoadName = property(get_RoadName, None)
    ShortRoadName = property(get_ShortRoadName, None)
    SpeedLimit = property(get_SpeedLimit, None)
    TravelTime = property(get_TravelTime, None)
class GuidanceRoadSignpost(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Maps.Guidance.IGuidanceRoadSignpost
    _classid_ = 'Windows.Services.Maps.Guidance.GuidanceRoadSignpost'
    @winrt_mixinmethod
    def get_ExitNumber(self: win32more.Windows.Services.Maps.Guidance.IGuidanceRoadSignpost) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Exit(self: win32more.Windows.Services.Maps.Guidance.IGuidanceRoadSignpost) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_BackgroundColor(self: win32more.Windows.Services.Maps.Guidance.IGuidanceRoadSignpost) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def get_ForegroundColor(self: win32more.Windows.Services.Maps.Guidance.IGuidanceRoadSignpost) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def get_ExitDirections(self: win32more.Windows.Services.Maps.Guidance.IGuidanceRoadSignpost) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    BackgroundColor = property(get_BackgroundColor, None)
    Exit = property(get_Exit, None)
    ExitDirections = property(get_ExitDirections, None)
    ExitNumber = property(get_ExitNumber, None)
    ForegroundColor = property(get_ForegroundColor, None)
class GuidanceRoute(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Maps.Guidance.IGuidanceRoute
    _classid_ = 'Windows.Services.Maps.Guidance.GuidanceRoute'
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Services.Maps.Guidance.IGuidanceRoute) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Distance(self: win32more.Windows.Services.Maps.Guidance.IGuidanceRoute) -> Int32: ...
    @winrt_mixinmethod
    def get_Maneuvers(self: win32more.Windows.Services.Maps.Guidance.IGuidanceRoute) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.Guidance.GuidanceManeuver]: ...
    @winrt_mixinmethod
    def get_BoundingBox(self: win32more.Windows.Services.Maps.Guidance.IGuidanceRoute) -> win32more.Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_mixinmethod
    def get_Path(self: win32more.Windows.Services.Maps.Guidance.IGuidanceRoute) -> win32more.Windows.Devices.Geolocation.Geopath: ...
    @winrt_mixinmethod
    def get_RoadSegments(self: win32more.Windows.Services.Maps.Guidance.IGuidanceRoute) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.Guidance.GuidanceRoadSegment]: ...
    @winrt_mixinmethod
    def ConvertToMapRoute(self: win32more.Windows.Services.Maps.Guidance.IGuidanceRoute) -> win32more.Windows.Services.Maps.MapRoute: ...
    @winrt_classmethod
    def CanCreateFromMapRoute(cls: win32more.Windows.Services.Maps.Guidance.IGuidanceRouteStatics, mapRoute: win32more.Windows.Services.Maps.MapRoute) -> Boolean: ...
    @winrt_classmethod
    def TryCreateFromMapRoute(cls: win32more.Windows.Services.Maps.Guidance.IGuidanceRouteStatics, mapRoute: win32more.Windows.Services.Maps.MapRoute) -> win32more.Windows.Services.Maps.Guidance.GuidanceRoute: ...
    BoundingBox = property(get_BoundingBox, None)
    Distance = property(get_Distance, None)
    Duration = property(get_Duration, None)
    Maneuvers = property(get_Maneuvers, None)
    Path = property(get_Path, None)
    RoadSegments = property(get_RoadSegments, None)
class GuidanceTelemetryCollector(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Maps.Guidance.IGuidanceTelemetryCollector
    _classid_ = 'Windows.Services.Maps.Guidance.GuidanceTelemetryCollector'
    @winrt_mixinmethod
    def get_Enabled(self: win32more.Windows.Services.Maps.Guidance.IGuidanceTelemetryCollector) -> Boolean: ...
    @winrt_mixinmethod
    def put_Enabled(self: win32more.Windows.Services.Maps.Guidance.IGuidanceTelemetryCollector, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def ClearLocalData(self: win32more.Windows.Services.Maps.Guidance.IGuidanceTelemetryCollector) -> Void: ...
    @winrt_mixinmethod
    def get_SpeedTrigger(self: win32more.Windows.Services.Maps.Guidance.IGuidanceTelemetryCollector) -> Double: ...
    @winrt_mixinmethod
    def put_SpeedTrigger(self: win32more.Windows.Services.Maps.Guidance.IGuidanceTelemetryCollector, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_UploadFrequency(self: win32more.Windows.Services.Maps.Guidance.IGuidanceTelemetryCollector) -> Int32: ...
    @winrt_mixinmethod
    def put_UploadFrequency(self: win32more.Windows.Services.Maps.Guidance.IGuidanceTelemetryCollector, value: Int32) -> Void: ...
    @winrt_classmethod
    def GetCurrent(cls: win32more.Windows.Services.Maps.Guidance.IGuidanceTelemetryCollectorStatics) -> win32more.Windows.Services.Maps.Guidance.GuidanceTelemetryCollector: ...
    Enabled = property(get_Enabled, put_Enabled)
    SpeedTrigger = property(get_SpeedTrigger, put_SpeedTrigger)
    UploadFrequency = property(get_UploadFrequency, put_UploadFrequency)
class GuidanceUpdatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Maps.Guidance.IGuidanceUpdatedEventArgs
    _classid_ = 'Windows.Services.Maps.Guidance.GuidanceUpdatedEventArgs'
    @winrt_mixinmethod
    def get_Mode(self: win32more.Windows.Services.Maps.Guidance.IGuidanceUpdatedEventArgs) -> win32more.Windows.Services.Maps.Guidance.GuidanceMode: ...
    @winrt_mixinmethod
    def get_NextManeuver(self: win32more.Windows.Services.Maps.Guidance.IGuidanceUpdatedEventArgs) -> win32more.Windows.Services.Maps.Guidance.GuidanceManeuver: ...
    @winrt_mixinmethod
    def get_NextManeuverDistance(self: win32more.Windows.Services.Maps.Guidance.IGuidanceUpdatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_AfterNextManeuver(self: win32more.Windows.Services.Maps.Guidance.IGuidanceUpdatedEventArgs) -> win32more.Windows.Services.Maps.Guidance.GuidanceManeuver: ...
    @winrt_mixinmethod
    def get_AfterNextManeuverDistance(self: win32more.Windows.Services.Maps.Guidance.IGuidanceUpdatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_DistanceToDestination(self: win32more.Windows.Services.Maps.Guidance.IGuidanceUpdatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ElapsedDistance(self: win32more.Windows.Services.Maps.Guidance.IGuidanceUpdatedEventArgs) -> Int32: ...
    @winrt_mixinmethod
    def get_ElapsedTime(self: win32more.Windows.Services.Maps.Guidance.IGuidanceUpdatedEventArgs) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_TimeToDestination(self: win32more.Windows.Services.Maps.Guidance.IGuidanceUpdatedEventArgs) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_RoadName(self: win32more.Windows.Services.Maps.Guidance.IGuidanceUpdatedEventArgs) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Route(self: win32more.Windows.Services.Maps.Guidance.IGuidanceUpdatedEventArgs) -> win32more.Windows.Services.Maps.Guidance.GuidanceRoute: ...
    @winrt_mixinmethod
    def get_CurrentLocation(self: win32more.Windows.Services.Maps.Guidance.IGuidanceUpdatedEventArgs) -> win32more.Windows.Services.Maps.Guidance.GuidanceMapMatchedCoordinate: ...
    @winrt_mixinmethod
    def get_IsNewManeuver(self: win32more.Windows.Services.Maps.Guidance.IGuidanceUpdatedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_LaneInfo(self: win32more.Windows.Services.Maps.Guidance.IGuidanceUpdatedEventArgs) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.Guidance.GuidanceLaneInfo]: ...
    AfterNextManeuver = property(get_AfterNextManeuver, None)
    AfterNextManeuverDistance = property(get_AfterNextManeuverDistance, None)
    CurrentLocation = property(get_CurrentLocation, None)
    DistanceToDestination = property(get_DistanceToDestination, None)
    ElapsedDistance = property(get_ElapsedDistance, None)
    ElapsedTime = property(get_ElapsedTime, None)
    IsNewManeuver = property(get_IsNewManeuver, None)
    LaneInfo = property(get_LaneInfo, None)
    Mode = property(get_Mode, None)
    NextManeuver = property(get_NextManeuver, None)
    NextManeuverDistance = property(get_NextManeuverDistance, None)
    RoadName = property(get_RoadName, None)
    Route = property(get_Route, None)
    TimeToDestination = property(get_TimeToDestination, None)
class IGuidanceAudioNotificationRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.Guidance.IGuidanceAudioNotificationRequestedEventArgs'
    _iid_ = Guid('{ca2aa24a-c7c2-4d4c-9d7c-499576bceddb}')
    @winrt_commethod(6)
    def get_AudioNotification(self) -> win32more.Windows.Services.Maps.Guidance.GuidanceAudioNotificationKind: ...
    @winrt_commethod(7)
    def get_AudioFilePaths(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(8)
    def get_AudioText(self) -> WinRT_String: ...
    AudioFilePaths = property(get_AudioFilePaths, None)
    AudioNotification = property(get_AudioNotification, None)
    AudioText = property(get_AudioText, None)
class IGuidanceLaneInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.Guidance.IGuidanceLaneInfo'
    _iid_ = Guid('{8404d114-6581-43b7-ac15-c9079bf90df1}')
    @winrt_commethod(6)
    def get_LaneMarkers(self) -> win32more.Windows.Services.Maps.Guidance.GuidanceLaneMarkers: ...
    @winrt_commethod(7)
    def get_IsOnRoute(self) -> Boolean: ...
    IsOnRoute = property(get_IsOnRoute, None)
    LaneMarkers = property(get_LaneMarkers, None)
class IGuidanceManeuver(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.Guidance.IGuidanceManeuver'
    _iid_ = Guid('{fc09326c-ecc9-4928-a2a1-7232b99b94a1}')
    @winrt_commethod(6)
    def get_StartLocation(self) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(7)
    def get_DistanceFromRouteStart(self) -> Int32: ...
    @winrt_commethod(8)
    def get_DistanceFromPreviousManeuver(self) -> Int32: ...
    @winrt_commethod(9)
    def get_DepartureRoadName(self) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_NextRoadName(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def get_DepartureShortRoadName(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_NextShortRoadName(self) -> WinRT_String: ...
    @winrt_commethod(13)
    def get_Kind(self) -> win32more.Windows.Services.Maps.Guidance.GuidanceManeuverKind: ...
    @winrt_commethod(14)
    def get_StartAngle(self) -> Int32: ...
    @winrt_commethod(15)
    def get_EndAngle(self) -> Int32: ...
    @winrt_commethod(16)
    def get_RoadSignpost(self) -> win32more.Windows.Services.Maps.Guidance.GuidanceRoadSignpost: ...
    @winrt_commethod(17)
    def get_InstructionText(self) -> WinRT_String: ...
    DepartureRoadName = property(get_DepartureRoadName, None)
    DepartureShortRoadName = property(get_DepartureShortRoadName, None)
    DistanceFromPreviousManeuver = property(get_DistanceFromPreviousManeuver, None)
    DistanceFromRouteStart = property(get_DistanceFromRouteStart, None)
    EndAngle = property(get_EndAngle, None)
    InstructionText = property(get_InstructionText, None)
    Kind = property(get_Kind, None)
    NextRoadName = property(get_NextRoadName, None)
    NextShortRoadName = property(get_NextShortRoadName, None)
    RoadSignpost = property(get_RoadSignpost, None)
    StartAngle = property(get_StartAngle, None)
    StartLocation = property(get_StartLocation, None)
class IGuidanceMapMatchedCoordinate(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.Guidance.IGuidanceMapMatchedCoordinate'
    _iid_ = Guid('{b7acb168-2912-4a99-aff1-798609b981fe}')
    @winrt_commethod(6)
    def get_Location(self) -> win32more.Windows.Devices.Geolocation.Geopoint: ...
    @winrt_commethod(7)
    def get_CurrentHeading(self) -> Double: ...
    @winrt_commethod(8)
    def get_CurrentSpeed(self) -> Double: ...
    @winrt_commethod(9)
    def get_IsOnStreet(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_Road(self) -> win32more.Windows.Services.Maps.Guidance.GuidanceRoadSegment: ...
    CurrentHeading = property(get_CurrentHeading, None)
    CurrentSpeed = property(get_CurrentSpeed, None)
    IsOnStreet = property(get_IsOnStreet, None)
    Location = property(get_Location, None)
    Road = property(get_Road, None)
class IGuidanceNavigator(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.Guidance.IGuidanceNavigator'
    _iid_ = Guid('{08f17ef7-8e3f-4d9a-be8a-108f9a012c67}')
    @winrt_commethod(6)
    def StartNavigating(self, route: win32more.Windows.Services.Maps.Guidance.GuidanceRoute) -> Void: ...
    @winrt_commethod(7)
    def StartSimulating(self, route: win32more.Windows.Services.Maps.Guidance.GuidanceRoute, speedInMetersPerSecond: Int32) -> Void: ...
    @winrt_commethod(8)
    def StartTracking(self) -> Void: ...
    @winrt_commethod(9)
    def Pause(self) -> Void: ...
    @winrt_commethod(10)
    def Resume(self) -> Void: ...
    @winrt_commethod(11)
    def Stop(self) -> Void: ...
    @winrt_commethod(12)
    def RepeatLastAudioNotification(self) -> Void: ...
    @winrt_commethod(13)
    def get_AudioMeasurementSystem(self) -> win32more.Windows.Services.Maps.Guidance.GuidanceAudioMeasurementSystem: ...
    @winrt_commethod(14)
    def put_AudioMeasurementSystem(self, value: win32more.Windows.Services.Maps.Guidance.GuidanceAudioMeasurementSystem) -> Void: ...
    @winrt_commethod(15)
    def get_AudioNotifications(self) -> win32more.Windows.Services.Maps.Guidance.GuidanceAudioNotifications: ...
    @winrt_commethod(16)
    def put_AudioNotifications(self, value: win32more.Windows.Services.Maps.Guidance.GuidanceAudioNotifications) -> Void: ...
    @winrt_commethod(17)
    def add_GuidanceUpdated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.Guidance.GuidanceNavigator, win32more.Windows.Services.Maps.Guidance.GuidanceUpdatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_GuidanceUpdated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(19)
    def add_DestinationReached(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.Guidance.GuidanceNavigator, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_DestinationReached(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(21)
    def add_Rerouting(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.Guidance.GuidanceNavigator, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(22)
    def remove_Rerouting(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(23)
    def add_Rerouted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.Guidance.GuidanceNavigator, win32more.Windows.Services.Maps.Guidance.GuidanceReroutedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(24)
    def remove_Rerouted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(25)
    def add_RerouteFailed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.Guidance.GuidanceNavigator, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(26)
    def remove_RerouteFailed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(27)
    def add_UserLocationLost(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.Guidance.GuidanceNavigator, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(28)
    def remove_UserLocationLost(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(29)
    def add_UserLocationRestored(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.Guidance.GuidanceNavigator, win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(30)
    def remove_UserLocationRestored(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(31)
    def SetGuidanceVoice(self, voiceId: Int32, voiceFolder: WinRT_String) -> Void: ...
    @winrt_commethod(32)
    def UpdateUserLocation(self, userLocation: win32more.Windows.Devices.Geolocation.Geocoordinate) -> Void: ...
    @winrt_commethod(33)
    def UpdateUserLocationWithPositionOverride(self, userLocation: win32more.Windows.Devices.Geolocation.Geocoordinate, positionOverride: win32more.Windows.Devices.Geolocation.BasicGeoposition) -> Void: ...
    AudioMeasurementSystem = property(get_AudioMeasurementSystem, put_AudioMeasurementSystem)
    AudioNotifications = property(get_AudioNotifications, put_AudioNotifications)
    GuidanceUpdated = event()
    DestinationReached = event()
    Rerouting = event()
    Rerouted = event()
    RerouteFailed = event()
    UserLocationLost = event()
    UserLocationRestored = event()
class IGuidanceNavigator2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.Guidance.IGuidanceNavigator2'
    _iid_ = Guid('{6cdc50d1-041c-4bf3-b633-a101fc2f6b57}')
    @winrt_commethod(6)
    def add_AudioNotificationRequested(self, value: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.Guidance.GuidanceNavigator, win32more.Windows.Services.Maps.Guidance.GuidanceAudioNotificationRequestedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_AudioNotificationRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def get_IsGuidanceAudioMuted(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_IsGuidanceAudioMuted(self, value: Boolean) -> Void: ...
    IsGuidanceAudioMuted = property(get_IsGuidanceAudioMuted, put_IsGuidanceAudioMuted)
    AudioNotificationRequested = event()
class IGuidanceNavigatorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.Guidance.IGuidanceNavigatorStatics'
    _iid_ = Guid('{00fd9513-4456-4e66-a143-3add6be08426}')
    @winrt_commethod(6)
    def GetCurrent(self) -> win32more.Windows.Services.Maps.Guidance.GuidanceNavigator: ...
class IGuidanceNavigatorStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.Guidance.IGuidanceNavigatorStatics2'
    _iid_ = Guid('{54c5c3e2-7784-4c85-8c95-d0c6efb43965}')
    @winrt_commethod(6)
    def get_UseAppProvidedVoice(self) -> Boolean: ...
    UseAppProvidedVoice = property(get_UseAppProvidedVoice, None)
class IGuidanceReroutedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.Guidance.IGuidanceReroutedEventArgs'
    _iid_ = Guid('{115d4008-d528-454e-bb94-a50341d2c9f1}')
    @winrt_commethod(6)
    def get_Route(self) -> win32more.Windows.Services.Maps.Guidance.GuidanceRoute: ...
    Route = property(get_Route, None)
class IGuidanceRoadSegment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.Guidance.IGuidanceRoadSegment'
    _iid_ = Guid('{b32758a6-be78-4c63-afe7-6c2957479b3e}')
    @winrt_commethod(6)
    def get_RoadName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ShortRoadName(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_SpeedLimit(self) -> Double: ...
    @winrt_commethod(9)
    def get_TravelTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(10)
    def get_Path(self) -> win32more.Windows.Devices.Geolocation.Geopath: ...
    @winrt_commethod(11)
    def get_Id(self) -> WinRT_String: ...
    @winrt_commethod(12)
    def get_IsHighway(self) -> Boolean: ...
    @winrt_commethod(13)
    def get_IsTunnel(self) -> Boolean: ...
    @winrt_commethod(14)
    def get_IsTollRoad(self) -> Boolean: ...
    Id = property(get_Id, None)
    IsHighway = property(get_IsHighway, None)
    IsTollRoad = property(get_IsTollRoad, None)
    IsTunnel = property(get_IsTunnel, None)
    Path = property(get_Path, None)
    RoadName = property(get_RoadName, None)
    ShortRoadName = property(get_ShortRoadName, None)
    SpeedLimit = property(get_SpeedLimit, None)
    TravelTime = property(get_TravelTime, None)
class IGuidanceRoadSegment2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.Guidance.IGuidanceRoadSegment2'
    _iid_ = Guid('{2474a61d-1723-49f1-895b-47a2c4aa9c55}')
    @winrt_commethod(6)
    def get_IsScenic(self) -> Boolean: ...
    IsScenic = property(get_IsScenic, None)
class IGuidanceRoadSignpost(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.Guidance.IGuidanceRoadSignpost'
    _iid_ = Guid('{f1a728b6-f77a-4742-8312-53300f9845f0}')
    @winrt_commethod(6)
    def get_ExitNumber(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Exit(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def get_BackgroundColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(9)
    def get_ForegroundColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(10)
    def get_ExitDirections(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    BackgroundColor = property(get_BackgroundColor, None)
    Exit = property(get_Exit, None)
    ExitDirections = property(get_ExitDirections, None)
    ExitNumber = property(get_ExitNumber, None)
    ForegroundColor = property(get_ForegroundColor, None)
class IGuidanceRoute(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.Guidance.IGuidanceRoute'
    _iid_ = Guid('{3a14545d-801a-40bd-a286-afb2010cce6c}')
    @winrt_commethod(6)
    def get_Duration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def get_Distance(self) -> Int32: ...
    @winrt_commethod(8)
    def get_Maneuvers(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.Guidance.GuidanceManeuver]: ...
    @winrt_commethod(9)
    def get_BoundingBox(self) -> win32more.Windows.Devices.Geolocation.GeoboundingBox: ...
    @winrt_commethod(10)
    def get_Path(self) -> win32more.Windows.Devices.Geolocation.Geopath: ...
    @winrt_commethod(11)
    def get_RoadSegments(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.Guidance.GuidanceRoadSegment]: ...
    @winrt_commethod(12)
    def ConvertToMapRoute(self) -> win32more.Windows.Services.Maps.MapRoute: ...
    BoundingBox = property(get_BoundingBox, None)
    Distance = property(get_Distance, None)
    Duration = property(get_Duration, None)
    Maneuvers = property(get_Maneuvers, None)
    Path = property(get_Path, None)
    RoadSegments = property(get_RoadSegments, None)
class IGuidanceRouteStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.Guidance.IGuidanceRouteStatics'
    _iid_ = Guid('{f56d926a-55ed-49c1-b09c-4b8223b50db3}')
    @winrt_commethod(6)
    def CanCreateFromMapRoute(self, mapRoute: win32more.Windows.Services.Maps.MapRoute) -> Boolean: ...
    @winrt_commethod(7)
    def TryCreateFromMapRoute(self, mapRoute: win32more.Windows.Services.Maps.MapRoute) -> win32more.Windows.Services.Maps.Guidance.GuidanceRoute: ...
class IGuidanceTelemetryCollector(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.Guidance.IGuidanceTelemetryCollector'
    _iid_ = Guid('{db1f8da5-b878-4d92-98dd-347d23d38262}')
    @winrt_commethod(6)
    def get_Enabled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Enabled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def ClearLocalData(self) -> Void: ...
    @winrt_commethod(9)
    def get_SpeedTrigger(self) -> Double: ...
    @winrt_commethod(10)
    def put_SpeedTrigger(self, value: Double) -> Void: ...
    @winrt_commethod(11)
    def get_UploadFrequency(self) -> Int32: ...
    @winrt_commethod(12)
    def put_UploadFrequency(self, value: Int32) -> Void: ...
    Enabled = property(get_Enabled, put_Enabled)
    SpeedTrigger = property(get_SpeedTrigger, put_SpeedTrigger)
    UploadFrequency = property(get_UploadFrequency, put_UploadFrequency)
class IGuidanceTelemetryCollectorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.Guidance.IGuidanceTelemetryCollectorStatics'
    _iid_ = Guid('{36532047-f160-44fb-b578-94577ca05990}')
    @winrt_commethod(6)
    def GetCurrent(self) -> win32more.Windows.Services.Maps.Guidance.GuidanceTelemetryCollector: ...
class IGuidanceUpdatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.Guidance.IGuidanceUpdatedEventArgs'
    _iid_ = Guid('{fdac160b-9e8d-4de3-a9fa-b06321d18db9}')
    @winrt_commethod(6)
    def get_Mode(self) -> win32more.Windows.Services.Maps.Guidance.GuidanceMode: ...
    @winrt_commethod(7)
    def get_NextManeuver(self) -> win32more.Windows.Services.Maps.Guidance.GuidanceManeuver: ...
    @winrt_commethod(8)
    def get_NextManeuverDistance(self) -> Int32: ...
    @winrt_commethod(9)
    def get_AfterNextManeuver(self) -> win32more.Windows.Services.Maps.Guidance.GuidanceManeuver: ...
    @winrt_commethod(10)
    def get_AfterNextManeuverDistance(self) -> Int32: ...
    @winrt_commethod(11)
    def get_DistanceToDestination(self) -> Int32: ...
    @winrt_commethod(12)
    def get_ElapsedDistance(self) -> Int32: ...
    @winrt_commethod(13)
    def get_ElapsedTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(14)
    def get_TimeToDestination(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(15)
    def get_RoadName(self) -> WinRT_String: ...
    @winrt_commethod(16)
    def get_Route(self) -> win32more.Windows.Services.Maps.Guidance.GuidanceRoute: ...
    @winrt_commethod(17)
    def get_CurrentLocation(self) -> win32more.Windows.Services.Maps.Guidance.GuidanceMapMatchedCoordinate: ...
    @winrt_commethod(18)
    def get_IsNewManeuver(self) -> Boolean: ...
    @winrt_commethod(19)
    def get_LaneInfo(self) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Services.Maps.Guidance.GuidanceLaneInfo]: ...
    AfterNextManeuver = property(get_AfterNextManeuver, None)
    AfterNextManeuverDistance = property(get_AfterNextManeuverDistance, None)
    CurrentLocation = property(get_CurrentLocation, None)
    DistanceToDestination = property(get_DistanceToDestination, None)
    ElapsedDistance = property(get_ElapsedDistance, None)
    ElapsedTime = property(get_ElapsedTime, None)
    IsNewManeuver = property(get_IsNewManeuver, None)
    LaneInfo = property(get_LaneInfo, None)
    Mode = property(get_Mode, None)
    NextManeuver = property(get_NextManeuver, None)
    NextManeuverDistance = property(get_NextManeuverDistance, None)
    RoadName = property(get_RoadName, None)
    Route = property(get_Route, None)
    TimeToDestination = property(get_TimeToDestination, None)


make_ready(__name__)
