from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar, Annotated
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Devices.Geolocation
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Services.Maps
import win32more.Windows.Services.Maps.Guidance
import win32more.Windows.UI
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
GuidanceAudioMeasurementSystem = Int32
GuidanceAudioMeasurementSystem_Meters: GuidanceAudioMeasurementSystem = 0
GuidanceAudioMeasurementSystem_MilesAndYards: GuidanceAudioMeasurementSystem = 1
GuidanceAudioMeasurementSystem_MilesAndFeet: GuidanceAudioMeasurementSystem = 2
GuidanceAudioNotificationKind = Int32
GuidanceAudioNotificationKind_Maneuver: GuidanceAudioNotificationKind = 0
GuidanceAudioNotificationKind_Route: GuidanceAudioNotificationKind = 1
GuidanceAudioNotificationKind_Gps: GuidanceAudioNotificationKind = 2
GuidanceAudioNotificationKind_SpeedLimit: GuidanceAudioNotificationKind = 3
GuidanceAudioNotificationKind_Traffic: GuidanceAudioNotificationKind = 4
GuidanceAudioNotificationKind_TrafficCamera: GuidanceAudioNotificationKind = 5
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
    AudioNotification = property(get_AudioNotification, None)
    AudioFilePaths = property(get_AudioFilePaths, None)
    AudioText = property(get_AudioText, None)
GuidanceAudioNotifications = UInt32
GuidanceAudioNotifications_None: GuidanceAudioNotifications = 0
GuidanceAudioNotifications_Maneuver: GuidanceAudioNotifications = 1
GuidanceAudioNotifications_Route: GuidanceAudioNotifications = 2
GuidanceAudioNotifications_Gps: GuidanceAudioNotifications = 4
GuidanceAudioNotifications_SpeedLimit: GuidanceAudioNotifications = 8
GuidanceAudioNotifications_Traffic: GuidanceAudioNotifications = 16
GuidanceAudioNotifications_TrafficCamera: GuidanceAudioNotifications = 32
class GuidanceLaneInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Services.Maps.Guidance.IGuidanceLaneInfo
    _classid_ = 'Windows.Services.Maps.Guidance.GuidanceLaneInfo'
    @winrt_mixinmethod
    def get_LaneMarkers(self: win32more.Windows.Services.Maps.Guidance.IGuidanceLaneInfo) -> win32more.Windows.Services.Maps.Guidance.GuidanceLaneMarkers: ...
    @winrt_mixinmethod
    def get_IsOnRoute(self: win32more.Windows.Services.Maps.Guidance.IGuidanceLaneInfo) -> Boolean: ...
    LaneMarkers = property(get_LaneMarkers, None)
    IsOnRoute = property(get_IsOnRoute, None)
GuidanceLaneMarkers = UInt32
GuidanceLaneMarkers_None: GuidanceLaneMarkers = 0
GuidanceLaneMarkers_LightRight: GuidanceLaneMarkers = 1
GuidanceLaneMarkers_Right: GuidanceLaneMarkers = 2
GuidanceLaneMarkers_HardRight: GuidanceLaneMarkers = 4
GuidanceLaneMarkers_Straight: GuidanceLaneMarkers = 8
GuidanceLaneMarkers_UTurnLeft: GuidanceLaneMarkers = 16
GuidanceLaneMarkers_HardLeft: GuidanceLaneMarkers = 32
GuidanceLaneMarkers_Left: GuidanceLaneMarkers = 64
GuidanceLaneMarkers_LightLeft: GuidanceLaneMarkers = 128
GuidanceLaneMarkers_UTurnRight: GuidanceLaneMarkers = 256
GuidanceLaneMarkers_Unknown: GuidanceLaneMarkers = 4294967295
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
    StartLocation = property(get_StartLocation, None)
    DistanceFromRouteStart = property(get_DistanceFromRouteStart, None)
    DistanceFromPreviousManeuver = property(get_DistanceFromPreviousManeuver, None)
    DepartureRoadName = property(get_DepartureRoadName, None)
    NextRoadName = property(get_NextRoadName, None)
    DepartureShortRoadName = property(get_DepartureShortRoadName, None)
    NextShortRoadName = property(get_NextShortRoadName, None)
    Kind = property(get_Kind, None)
    StartAngle = property(get_StartAngle, None)
    EndAngle = property(get_EndAngle, None)
    RoadSignpost = property(get_RoadSignpost, None)
    InstructionText = property(get_InstructionText, None)
GuidanceManeuverKind = Int32
GuidanceManeuverKind_None: GuidanceManeuverKind = 0
GuidanceManeuverKind_GoStraight: GuidanceManeuverKind = 1
GuidanceManeuverKind_UTurnRight: GuidanceManeuverKind = 2
GuidanceManeuverKind_UTurnLeft: GuidanceManeuverKind = 3
GuidanceManeuverKind_TurnKeepRight: GuidanceManeuverKind = 4
GuidanceManeuverKind_TurnLightRight: GuidanceManeuverKind = 5
GuidanceManeuverKind_TurnRight: GuidanceManeuverKind = 6
GuidanceManeuverKind_TurnHardRight: GuidanceManeuverKind = 7
GuidanceManeuverKind_KeepMiddle: GuidanceManeuverKind = 8
GuidanceManeuverKind_TurnKeepLeft: GuidanceManeuverKind = 9
GuidanceManeuverKind_TurnLightLeft: GuidanceManeuverKind = 10
GuidanceManeuverKind_TurnLeft: GuidanceManeuverKind = 11
GuidanceManeuverKind_TurnHardLeft: GuidanceManeuverKind = 12
GuidanceManeuverKind_FreewayEnterRight: GuidanceManeuverKind = 13
GuidanceManeuverKind_FreewayEnterLeft: GuidanceManeuverKind = 14
GuidanceManeuverKind_FreewayLeaveRight: GuidanceManeuverKind = 15
GuidanceManeuverKind_FreewayLeaveLeft: GuidanceManeuverKind = 16
GuidanceManeuverKind_FreewayKeepRight: GuidanceManeuverKind = 17
GuidanceManeuverKind_FreewayKeepLeft: GuidanceManeuverKind = 18
GuidanceManeuverKind_TrafficCircleRight1: GuidanceManeuverKind = 19
GuidanceManeuverKind_TrafficCircleRight2: GuidanceManeuverKind = 20
GuidanceManeuverKind_TrafficCircleRight3: GuidanceManeuverKind = 21
GuidanceManeuverKind_TrafficCircleRight4: GuidanceManeuverKind = 22
GuidanceManeuverKind_TrafficCircleRight5: GuidanceManeuverKind = 23
GuidanceManeuverKind_TrafficCircleRight6: GuidanceManeuverKind = 24
GuidanceManeuverKind_TrafficCircleRight7: GuidanceManeuverKind = 25
GuidanceManeuverKind_TrafficCircleRight8: GuidanceManeuverKind = 26
GuidanceManeuverKind_TrafficCircleRight9: GuidanceManeuverKind = 27
GuidanceManeuverKind_TrafficCircleRight10: GuidanceManeuverKind = 28
GuidanceManeuverKind_TrafficCircleRight11: GuidanceManeuverKind = 29
GuidanceManeuverKind_TrafficCircleRight12: GuidanceManeuverKind = 30
GuidanceManeuverKind_TrafficCircleLeft1: GuidanceManeuverKind = 31
GuidanceManeuverKind_TrafficCircleLeft2: GuidanceManeuverKind = 32
GuidanceManeuverKind_TrafficCircleLeft3: GuidanceManeuverKind = 33
GuidanceManeuverKind_TrafficCircleLeft4: GuidanceManeuverKind = 34
GuidanceManeuverKind_TrafficCircleLeft5: GuidanceManeuverKind = 35
GuidanceManeuverKind_TrafficCircleLeft6: GuidanceManeuverKind = 36
GuidanceManeuverKind_TrafficCircleLeft7: GuidanceManeuverKind = 37
GuidanceManeuverKind_TrafficCircleLeft8: GuidanceManeuverKind = 38
GuidanceManeuverKind_TrafficCircleLeft9: GuidanceManeuverKind = 39
GuidanceManeuverKind_TrafficCircleLeft10: GuidanceManeuverKind = 40
GuidanceManeuverKind_TrafficCircleLeft11: GuidanceManeuverKind = 41
GuidanceManeuverKind_TrafficCircleLeft12: GuidanceManeuverKind = 42
GuidanceManeuverKind_Start: GuidanceManeuverKind = 43
GuidanceManeuverKind_End: GuidanceManeuverKind = 44
GuidanceManeuverKind_TakeFerry: GuidanceManeuverKind = 45
GuidanceManeuverKind_PassTransitStation: GuidanceManeuverKind = 46
GuidanceManeuverKind_LeaveTransitStation: GuidanceManeuverKind = 47
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
    Location = property(get_Location, None)
    CurrentHeading = property(get_CurrentHeading, None)
    CurrentSpeed = property(get_CurrentSpeed, None)
    IsOnStreet = property(get_IsOnStreet, None)
    Road = property(get_Road, None)
GuidanceMode = Int32
GuidanceMode_None: GuidanceMode = 0
GuidanceMode_Simulation: GuidanceMode = 1
GuidanceMode_Navigation: GuidanceMode = 2
GuidanceMode_Tracking: GuidanceMode = 3
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
    def add_DestinationReached(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.Guidance.GuidanceNavigator, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_DestinationReached(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Rerouting(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.Guidance.GuidanceNavigator, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Rerouting(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Rerouted(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.Guidance.GuidanceNavigator, win32more.Windows.Services.Maps.Guidance.GuidanceReroutedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Rerouted(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_RerouteFailed(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.Guidance.GuidanceNavigator, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RerouteFailed(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UserLocationLost(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.Guidance.GuidanceNavigator, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_UserLocationLost(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_UserLocationRestored(self: win32more.Windows.Services.Maps.Guidance.IGuidanceNavigator, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.Guidance.GuidanceNavigator, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
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
    def get_UseAppProvidedVoice(cls: Windows.Services.Maps.Guidance.IGuidanceNavigatorStatics2) -> Boolean: ...
    @winrt_classmethod
    def GetCurrent(cls: Windows.Services.Maps.Guidance.IGuidanceNavigatorStatics) -> win32more.Windows.Services.Maps.Guidance.GuidanceNavigator: ...
    AudioMeasurementSystem = property(get_AudioMeasurementSystem, put_AudioMeasurementSystem)
    AudioNotifications = property(get_AudioNotifications, put_AudioNotifications)
    IsGuidanceAudioMuted = property(get_IsGuidanceAudioMuted, put_IsGuidanceAudioMuted)
    _GuidanceNavigator_Meta_.UseAppProvidedVoice = property(get_UseAppProvidedVoice.__wrapped__, None)
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
    RoadName = property(get_RoadName, None)
    ShortRoadName = property(get_ShortRoadName, None)
    SpeedLimit = property(get_SpeedLimit, None)
    TravelTime = property(get_TravelTime, None)
    Path = property(get_Path, None)
    Id = property(get_Id, None)
    IsHighway = property(get_IsHighway, None)
    IsTunnel = property(get_IsTunnel, None)
    IsTollRoad = property(get_IsTollRoad, None)
    IsScenic = property(get_IsScenic, None)
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
    ExitNumber = property(get_ExitNumber, None)
    Exit = property(get_Exit, None)
    BackgroundColor = property(get_BackgroundColor, None)
    ForegroundColor = property(get_ForegroundColor, None)
    ExitDirections = property(get_ExitDirections, None)
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
    def CanCreateFromMapRoute(cls: Windows.Services.Maps.Guidance.IGuidanceRouteStatics, mapRoute: win32more.Windows.Services.Maps.MapRoute) -> Boolean: ...
    @winrt_classmethod
    def TryCreateFromMapRoute(cls: Windows.Services.Maps.Guidance.IGuidanceRouteStatics, mapRoute: win32more.Windows.Services.Maps.MapRoute) -> win32more.Windows.Services.Maps.Guidance.GuidanceRoute: ...
    Duration = property(get_Duration, None)
    Distance = property(get_Distance, None)
    Maneuvers = property(get_Maneuvers, None)
    BoundingBox = property(get_BoundingBox, None)
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
    def GetCurrent(cls: Windows.Services.Maps.Guidance.IGuidanceTelemetryCollectorStatics) -> win32more.Windows.Services.Maps.Guidance.GuidanceTelemetryCollector: ...
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
    Mode = property(get_Mode, None)
    NextManeuver = property(get_NextManeuver, None)
    NextManeuverDistance = property(get_NextManeuverDistance, None)
    AfterNextManeuver = property(get_AfterNextManeuver, None)
    AfterNextManeuverDistance = property(get_AfterNextManeuverDistance, None)
    DistanceToDestination = property(get_DistanceToDestination, None)
    ElapsedDistance = property(get_ElapsedDistance, None)
    ElapsedTime = property(get_ElapsedTime, None)
    TimeToDestination = property(get_TimeToDestination, None)
    RoadName = property(get_RoadName, None)
    Route = property(get_Route, None)
    CurrentLocation = property(get_CurrentLocation, None)
    IsNewManeuver = property(get_IsNewManeuver, None)
    LaneInfo = property(get_LaneInfo, None)
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
    AudioNotification = property(get_AudioNotification, None)
    AudioFilePaths = property(get_AudioFilePaths, None)
    AudioText = property(get_AudioText, None)
class IGuidanceLaneInfo(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Services.Maps.Guidance.IGuidanceLaneInfo'
    _iid_ = Guid('{8404d114-6581-43b7-ac15-c9079bf90df1}')
    @winrt_commethod(6)
    def get_LaneMarkers(self) -> win32more.Windows.Services.Maps.Guidance.GuidanceLaneMarkers: ...
    @winrt_commethod(7)
    def get_IsOnRoute(self) -> Boolean: ...
    LaneMarkers = property(get_LaneMarkers, None)
    IsOnRoute = property(get_IsOnRoute, None)
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
    StartLocation = property(get_StartLocation, None)
    DistanceFromRouteStart = property(get_DistanceFromRouteStart, None)
    DistanceFromPreviousManeuver = property(get_DistanceFromPreviousManeuver, None)
    DepartureRoadName = property(get_DepartureRoadName, None)
    NextRoadName = property(get_NextRoadName, None)
    DepartureShortRoadName = property(get_DepartureShortRoadName, None)
    NextShortRoadName = property(get_NextShortRoadName, None)
    Kind = property(get_Kind, None)
    StartAngle = property(get_StartAngle, None)
    EndAngle = property(get_EndAngle, None)
    RoadSignpost = property(get_RoadSignpost, None)
    InstructionText = property(get_InstructionText, None)
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
    Location = property(get_Location, None)
    CurrentHeading = property(get_CurrentHeading, None)
    CurrentSpeed = property(get_CurrentSpeed, None)
    IsOnStreet = property(get_IsOnStreet, None)
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
    def add_DestinationReached(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.Guidance.GuidanceNavigator, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_DestinationReached(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(21)
    def add_Rerouting(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.Guidance.GuidanceNavigator, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(22)
    def remove_Rerouting(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(23)
    def add_Rerouted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.Guidance.GuidanceNavigator, win32more.Windows.Services.Maps.Guidance.GuidanceReroutedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(24)
    def remove_Rerouted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(25)
    def add_RerouteFailed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.Guidance.GuidanceNavigator, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(26)
    def remove_RerouteFailed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(27)
    def add_UserLocationLost(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.Guidance.GuidanceNavigator, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(28)
    def remove_UserLocationLost(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(29)
    def add_UserLocationRestored(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.Services.Maps.Guidance.GuidanceNavigator, win32more.Windows.Win32.System.WinRT.IInspectable_head]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
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
    RoadName = property(get_RoadName, None)
    ShortRoadName = property(get_ShortRoadName, None)
    SpeedLimit = property(get_SpeedLimit, None)
    TravelTime = property(get_TravelTime, None)
    Path = property(get_Path, None)
    Id = property(get_Id, None)
    IsHighway = property(get_IsHighway, None)
    IsTunnel = property(get_IsTunnel, None)
    IsTollRoad = property(get_IsTollRoad, None)
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
    ExitNumber = property(get_ExitNumber, None)
    Exit = property(get_Exit, None)
    BackgroundColor = property(get_BackgroundColor, None)
    ForegroundColor = property(get_ForegroundColor, None)
    ExitDirections = property(get_ExitDirections, None)
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
    Duration = property(get_Duration, None)
    Distance = property(get_Distance, None)
    Maneuvers = property(get_Maneuvers, None)
    BoundingBox = property(get_BoundingBox, None)
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
    Mode = property(get_Mode, None)
    NextManeuver = property(get_NextManeuver, None)
    NextManeuverDistance = property(get_NextManeuverDistance, None)
    AfterNextManeuver = property(get_AfterNextManeuver, None)
    AfterNextManeuverDistance = property(get_AfterNextManeuverDistance, None)
    DistanceToDestination = property(get_DistanceToDestination, None)
    ElapsedDistance = property(get_ElapsedDistance, None)
    ElapsedTime = property(get_ElapsedTime, None)
    TimeToDestination = property(get_TimeToDestination, None)
    RoadName = property(get_RoadName, None)
    Route = property(get_Route, None)
    CurrentLocation = property(get_CurrentLocation, None)
    IsNewManeuver = property(get_IsNewManeuver, None)
    LaneInfo = property(get_LaneInfo, None)
make_head(_module, 'GuidanceAudioNotificationRequestedEventArgs')
make_head(_module, 'GuidanceLaneInfo')
make_head(_module, 'GuidanceManeuver')
make_head(_module, 'GuidanceMapMatchedCoordinate')
make_head(_module, 'GuidanceNavigator')
make_head(_module, 'GuidanceReroutedEventArgs')
make_head(_module, 'GuidanceRoadSegment')
make_head(_module, 'GuidanceRoadSignpost')
make_head(_module, 'GuidanceRoute')
make_head(_module, 'GuidanceTelemetryCollector')
make_head(_module, 'GuidanceUpdatedEventArgs')
make_head(_module, 'IGuidanceAudioNotificationRequestedEventArgs')
make_head(_module, 'IGuidanceLaneInfo')
make_head(_module, 'IGuidanceManeuver')
make_head(_module, 'IGuidanceMapMatchedCoordinate')
make_head(_module, 'IGuidanceNavigator')
make_head(_module, 'IGuidanceNavigator2')
make_head(_module, 'IGuidanceNavigatorStatics')
make_head(_module, 'IGuidanceNavigatorStatics2')
make_head(_module, 'IGuidanceReroutedEventArgs')
make_head(_module, 'IGuidanceRoadSegment')
make_head(_module, 'IGuidanceRoadSegment2')
make_head(_module, 'IGuidanceRoadSignpost')
make_head(_module, 'IGuidanceRoute')
make_head(_module, 'IGuidanceRouteStatics')
make_head(_module, 'IGuidanceTelemetryCollector')
make_head(_module, 'IGuidanceTelemetryCollectorStatics')
make_head(_module, 'IGuidanceUpdatedEventArgs')
