from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from typing import Generic, TypeVar
K = TypeVar('T')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from Windows import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
from Windows._winrt import WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod
import Windows.Win32.System.WinRT
import Windows.Devices.Haptics
import Windows.Devices.Power
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Foundation.Numerics
import Windows.Perception
import Windows.Perception.People
import Windows.Perception.Spatial
import Windows.Storage.Streams
import Windows.UI.Input.Spatial
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ISpatialGestureRecognizer(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('71605bcc-0c35-4673-ad-bd-cc-04-ca-a6-ef-45')
    @winrt_commethod(6)
    def add_RecognitionStarted(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialGestureRecognizer, Windows.UI.Input.Spatial.SpatialRecognitionStartedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_RecognitionStarted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_RecognitionEnded(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialGestureRecognizer, Windows.UI.Input.Spatial.SpatialRecognitionEndedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_RecognitionEnded(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Tapped(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialGestureRecognizer, Windows.UI.Input.Spatial.SpatialTappedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Tapped(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_HoldStarted(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialGestureRecognizer, Windows.UI.Input.Spatial.SpatialHoldStartedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_HoldStarted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_HoldCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialGestureRecognizer, Windows.UI.Input.Spatial.SpatialHoldCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_HoldCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_HoldCanceled(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialGestureRecognizer, Windows.UI.Input.Spatial.SpatialHoldCanceledEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_HoldCanceled(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_ManipulationStarted(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialGestureRecognizer, Windows.UI.Input.Spatial.SpatialManipulationStartedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_ManipulationStarted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(20)
    def add_ManipulationUpdated(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialGestureRecognizer, Windows.UI.Input.Spatial.SpatialManipulationUpdatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_ManipulationUpdated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(22)
    def add_ManipulationCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialGestureRecognizer, Windows.UI.Input.Spatial.SpatialManipulationCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(23)
    def remove_ManipulationCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(24)
    def add_ManipulationCanceled(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialGestureRecognizer, Windows.UI.Input.Spatial.SpatialManipulationCanceledEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(25)
    def remove_ManipulationCanceled(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(26)
    def add_NavigationStarted(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialGestureRecognizer, Windows.UI.Input.Spatial.SpatialNavigationStartedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(27)
    def remove_NavigationStarted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(28)
    def add_NavigationUpdated(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialGestureRecognizer, Windows.UI.Input.Spatial.SpatialNavigationUpdatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(29)
    def remove_NavigationUpdated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(30)
    def add_NavigationCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialGestureRecognizer, Windows.UI.Input.Spatial.SpatialNavigationCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(31)
    def remove_NavigationCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(32)
    def add_NavigationCanceled(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialGestureRecognizer, Windows.UI.Input.Spatial.SpatialNavigationCanceledEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(33)
    def remove_NavigationCanceled(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(34)
    def CaptureInteraction(self, interaction: Windows.UI.Input.Spatial.SpatialInteraction) -> Void: ...
    @winrt_commethod(35)
    def CancelPendingGestures(self) -> Void: ...
    @winrt_commethod(36)
    def TrySetGestureSettings(self, settings: Windows.UI.Input.Spatial.SpatialGestureSettings) -> Boolean: ...
    @winrt_commethod(37)
    def get_GestureSettings(self) -> Windows.UI.Input.Spatial.SpatialGestureSettings: ...
    GestureSettings = property(get_GestureSettings, None)
class ISpatialGestureRecognizerFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('77214186-57b9-3150-83-82-69-8b-24-e2-64-d0')
    @winrt_commethod(6)
    def Create(self, settings: Windows.UI.Input.Spatial.SpatialGestureSettings) -> Windows.UI.Input.Spatial.SpatialGestureRecognizer: ...
class ISpatialHoldCanceledEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5dfcb667-4caa-4093-8c-35-b6-01-a8-39-f3-1b')
    @winrt_commethod(6)
    def get_InteractionSourceKind(self) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class ISpatialHoldCompletedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('3f64470b-4cfd-43da-8d-c4-e6-45-52-17-39-71')
    @winrt_commethod(6)
    def get_InteractionSourceKind(self) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class ISpatialHoldStartedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('8e343d79-acb6-4144-86-15-2c-fb-a8-a3-cb-3f')
    @winrt_commethod(6)
    def get_InteractionSourceKind(self) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_commethod(7)
    def TryGetPointerPose(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.UI.Input.Spatial.SpatialPointerPose: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class ISpatialInteraction(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fc967639-88e6-4646-91-12-43-44-aa-ec-9d-fa')
    @winrt_commethod(6)
    def get_SourceState(self) -> Windows.UI.Input.Spatial.SpatialInteractionSourceState: ...
    SourceState = property(get_SourceState, None)
class ISpatialInteractionController(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5f0e5ba3-0954-4e97-86-c5-e7-f3-0b-11-4d-fd')
    @winrt_commethod(6)
    def get_HasTouchpad(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_HasThumbstick(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_SimpleHapticsController(self) -> Windows.Devices.Haptics.SimpleHapticsController: ...
    @winrt_commethod(9)
    def get_VendorId(self) -> UInt16: ...
    @winrt_commethod(10)
    def get_ProductId(self) -> UInt16: ...
    @winrt_commethod(11)
    def get_Version(self) -> UInt16: ...
    HasTouchpad = property(get_HasTouchpad, None)
    HasThumbstick = property(get_HasThumbstick, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
    VendorId = property(get_VendorId, None)
    ProductId = property(get_ProductId, None)
    Version = property(get_Version, None)
class ISpatialInteractionController2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('35b6d924-c7a2-49b7-b7-2e-54-36-b2-fb-8f-9c')
    @winrt_commethod(6)
    def TryGetRenderableModelAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IRandomAccessStreamWithContentType]: ...
class ISpatialInteractionController3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('628466a0-9d91-4a0b-88-8d-16-5e-67-0a-8c-d5')
    @winrt_commethod(6)
    def TryGetBatteryReport(self) -> Windows.Devices.Power.BatteryReport: ...
class ISpatialInteractionControllerProperties(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('61056fb1-7ba9-4e35-b9-3f-92-72-cb-a9-b2-8b')
    @winrt_commethod(6)
    def get_IsTouchpadTouched(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsTouchpadPressed(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsThumbstickPressed(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_ThumbstickX(self) -> Double: ...
    @winrt_commethod(10)
    def get_ThumbstickY(self) -> Double: ...
    @winrt_commethod(11)
    def get_TouchpadX(self) -> Double: ...
    @winrt_commethod(12)
    def get_TouchpadY(self) -> Double: ...
    IsTouchpadTouched = property(get_IsTouchpadTouched, None)
    IsTouchpadPressed = property(get_IsTouchpadPressed, None)
    IsThumbstickPressed = property(get_IsThumbstickPressed, None)
    ThumbstickX = property(get_ThumbstickX, None)
    ThumbstickY = property(get_ThumbstickY, None)
    TouchpadX = property(get_TouchpadX, None)
    TouchpadY = property(get_TouchpadY, None)
class ISpatialInteractionDetectedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('075878e4-5961-3b41-9d-fb-ce-a5-d8-9c-c3-8a')
    @winrt_commethod(6)
    def get_InteractionSourceKind(self) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_commethod(7)
    def TryGetPointerPose(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.UI.Input.Spatial.SpatialPointerPose: ...
    @winrt_commethod(8)
    def get_Interaction(self) -> Windows.UI.Input.Spatial.SpatialInteraction: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
    Interaction = property(get_Interaction, None)
class ISpatialInteractionDetectedEventArgs2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('7b263e93-5f13-419c-97-d5-83-46-78-26-6a-a6')
    @winrt_commethod(6)
    def get_InteractionSource(self) -> Windows.UI.Input.Spatial.SpatialInteractionSource: ...
    InteractionSource = property(get_InteractionSource, None)
class ISpatialInteractionManager(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('32a64ea8-a15a-3995-b8-bd-80-51-3c-b5-ad-ef')
    @winrt_commethod(6)
    def add_SourceDetected(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialInteractionManager, Windows.UI.Input.Spatial.SpatialInteractionSourceEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_SourceDetected(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_SourceLost(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialInteractionManager, Windows.UI.Input.Spatial.SpatialInteractionSourceEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_SourceLost(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_SourceUpdated(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialInteractionManager, Windows.UI.Input.Spatial.SpatialInteractionSourceEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_SourceUpdated(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_SourcePressed(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialInteractionManager, Windows.UI.Input.Spatial.SpatialInteractionSourceEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_SourcePressed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_SourceReleased(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialInteractionManager, Windows.UI.Input.Spatial.SpatialInteractionSourceEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_SourceReleased(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_InteractionDetected(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialInteractionManager, Windows.UI.Input.Spatial.SpatialInteractionDetectedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_InteractionDetected(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def GetDetectedSourcesAtTimestamp(self, timeStamp: Windows.Perception.PerceptionTimestamp) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Spatial.SpatialInteractionSourceState]: ...
class ISpatialInteractionManagerStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('00e31fa6-8ca2-30bf-91-fe-d9-cb-4a-00-89-90')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> Windows.UI.Input.Spatial.SpatialInteractionManager: ...
class ISpatialInteractionManagerStatics2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('93f16c52-b88a-5929-8d-7c-48-cb-94-8b-08-1c')
    @winrt_commethod(6)
    def IsSourceKindSupported(self, kind: Windows.UI.Input.Spatial.SpatialInteractionSourceKind) -> Boolean: ...
class ISpatialInteractionSource(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('fb5433ba-b0b3-3148-9f-3b-e9-f5-de-56-8f-5d')
    @winrt_commethod(6)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Kind(self) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
class ISpatialInteractionSource2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('e4c5b70c-0470-4028-88-c0-a0-eb-44-d3-4e-fe')
    @winrt_commethod(6)
    def get_IsPointingSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsMenuSupported(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsGraspSupported(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Controller(self) -> Windows.UI.Input.Spatial.SpatialInteractionController: ...
    @winrt_commethod(10)
    def TryGetStateAtTimestamp(self, timestamp: Windows.Perception.PerceptionTimestamp) -> Windows.UI.Input.Spatial.SpatialInteractionSourceState: ...
    IsPointingSupported = property(get_IsPointingSupported, None)
    IsMenuSupported = property(get_IsMenuSupported, None)
    IsGraspSupported = property(get_IsGraspSupported, None)
    Controller = property(get_Controller, None)
class ISpatialInteractionSource3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0406d9f9-9afd-44f9-85-dc-70-00-23-a9-62-e3')
    @winrt_commethod(6)
    def get_Handedness(self) -> Windows.UI.Input.Spatial.SpatialInteractionSourceHandedness: ...
    Handedness = property(get_Handedness, None)
class ISpatialInteractionSource4(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0073bc4d-df66-5a91-a2-ba-ce-a3-e5-c5-8a-19')
    @winrt_commethod(6)
    def TryCreateHandMeshObserver(self) -> Windows.Perception.People.HandMeshObserver: ...
    @winrt_commethod(7)
    def TryCreateHandMeshObserverAsync(self) -> Windows.Foundation.IAsyncOperation[Windows.Perception.People.HandMeshObserver]: ...
class ISpatialInteractionSourceEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('23b786cf-ec23-3979-b2-7c-eb-0e-12-fe-b7-c7')
    @winrt_commethod(6)
    def get_State(self) -> Windows.UI.Input.Spatial.SpatialInteractionSourceState: ...
    State = property(get_State, None)
class ISpatialInteractionSourceEventArgs2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d8b4b467-e648-4d52-ab-49-e0-d2-27-19-9f-63')
    @winrt_commethod(6)
    def get_PressKind(self) -> Windows.UI.Input.Spatial.SpatialInteractionPressKind: ...
    PressKind = property(get_PressKind, None)
class ISpatialInteractionSourceLocation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ea4696c4-7e8b-30ca-bc-c5-c7-71-89-ce-a3-0a')
    @winrt_commethod(6)
    def get_Position(self) -> Windows.Foundation.IReference[Windows.Foundation.Numerics.Vector3]: ...
    @winrt_commethod(7)
    def get_Velocity(self) -> Windows.Foundation.IReference[Windows.Foundation.Numerics.Vector3]: ...
    Position = property(get_Position, None)
    Velocity = property(get_Velocity, None)
class ISpatialInteractionSourceLocation2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('4c671045-3917-40fc-a9-ac-31-c9-cf-5f-f9-1b')
    @winrt_commethod(6)
    def get_Orientation(self) -> Windows.Foundation.IReference[Windows.Foundation.Numerics.Quaternion]: ...
    Orientation = property(get_Orientation, None)
class ISpatialInteractionSourceLocation3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6702e65e-e915-4cfb-9c-1b-05-38-ef-c8-66-87')
    @winrt_commethod(6)
    def get_PositionAccuracy(self) -> Windows.UI.Input.Spatial.SpatialInteractionSourcePositionAccuracy: ...
    @winrt_commethod(7)
    def get_AngularVelocity(self) -> Windows.Foundation.IReference[Windows.Foundation.Numerics.Vector3]: ...
    @winrt_commethod(8)
    def get_SourcePointerPose(self) -> Windows.UI.Input.Spatial.SpatialPointerInteractionSourcePose: ...
    PositionAccuracy = property(get_PositionAccuracy, None)
    AngularVelocity = property(get_AngularVelocity, None)
    SourcePointerPose = property(get_SourcePointerPose, None)
class ISpatialInteractionSourceProperties(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('05604542-3ef7-3222-9f-53-63-c9-cb-7e-3b-c7')
    @winrt_commethod(6)
    def TryGetSourceLossMitigationDirection(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.Foundation.IReference[Windows.Foundation.Numerics.Vector3]: ...
    @winrt_commethod(7)
    def get_SourceLossRisk(self) -> Double: ...
    @winrt_commethod(8)
    def TryGetLocation(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.UI.Input.Spatial.SpatialInteractionSourceLocation: ...
    SourceLossRisk = property(get_SourceLossRisk, None)
class ISpatialInteractionSourceState(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('d5c475ef-4b63-37ec-98-b9-9f-c6-52-b9-d2-f2')
    @winrt_commethod(6)
    def get_Source(self) -> Windows.UI.Input.Spatial.SpatialInteractionSource: ...
    @winrt_commethod(7)
    def get_Properties(self) -> Windows.UI.Input.Spatial.SpatialInteractionSourceProperties: ...
    @winrt_commethod(8)
    def get_IsPressed(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Timestamp(self) -> Windows.Perception.PerceptionTimestamp: ...
    @winrt_commethod(10)
    def TryGetPointerPose(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.UI.Input.Spatial.SpatialPointerPose: ...
    Source = property(get_Source, None)
    Properties = property(get_Properties, None)
    IsPressed = property(get_IsPressed, None)
    Timestamp = property(get_Timestamp, None)
class ISpatialInteractionSourceState2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('45f6d0bd-1773-492e-9b-a3-8a-c1-cb-e7-7c-08')
    @winrt_commethod(6)
    def get_IsSelectPressed(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsMenuPressed(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsGrasped(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_SelectPressedValue(self) -> Double: ...
    @winrt_commethod(10)
    def get_ControllerProperties(self) -> Windows.UI.Input.Spatial.SpatialInteractionControllerProperties: ...
    IsSelectPressed = property(get_IsSelectPressed, None)
    IsMenuPressed = property(get_IsMenuPressed, None)
    IsGrasped = property(get_IsGrasped, None)
    SelectPressedValue = property(get_SelectPressedValue, None)
    ControllerProperties = property(get_ControllerProperties, None)
class ISpatialInteractionSourceState3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('f2f00bc2-bd2b-4a01-a8-fb-32-3e-01-58-52-7c')
    @winrt_commethod(6)
    def TryGetHandPose(self) -> Windows.Perception.People.HandPose: ...
class ISpatialManipulationCanceledEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2d40d1cb-e7da-4220-b0-bf-81-93-01-67-47-80')
    @winrt_commethod(6)
    def get_InteractionSourceKind(self) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class ISpatialManipulationCompletedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('05086802-f301-4343-92-50-2f-ba-a5-f8-7a-37')
    @winrt_commethod(6)
    def get_InteractionSourceKind(self) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_commethod(7)
    def TryGetCumulativeDelta(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.UI.Input.Spatial.SpatialManipulationDelta: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class ISpatialManipulationDelta(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a7ec967a-d123-3a81-a1-5b-99-29-23-dc-be-91')
    @winrt_commethod(6)
    def get_Translation(self) -> Windows.Foundation.Numerics.Vector3: ...
    Translation = property(get_Translation, None)
class ISpatialManipulationStartedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a1d6bbce-42a5-377b-ad-a6-d2-8e-3d-38-47-37')
    @winrt_commethod(6)
    def get_InteractionSourceKind(self) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_commethod(7)
    def TryGetPointerPose(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.UI.Input.Spatial.SpatialPointerPose: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class ISpatialManipulationUpdatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('5f230b9b-60c6-4dc6-bd-c9-9f-4a-6f-15-fe-49')
    @winrt_commethod(6)
    def get_InteractionSourceKind(self) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_commethod(7)
    def TryGetCumulativeDelta(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.UI.Input.Spatial.SpatialManipulationDelta: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class ISpatialNavigationCanceledEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('ce503edc-e8a5-46f0-92-d4-3c-12-2b-35-11-2a')
    @winrt_commethod(6)
    def get_InteractionSourceKind(self) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class ISpatialNavigationCompletedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('012e80b7-af3b-42c2-9e-41-ba-aa-0e-72-1f-3a')
    @winrt_commethod(6)
    def get_InteractionSourceKind(self) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_commethod(7)
    def get_NormalizedOffset(self) -> Windows.Foundation.Numerics.Vector3: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
    NormalizedOffset = property(get_NormalizedOffset, None)
class ISpatialNavigationStartedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('754a348a-fb64-4656-8e-bd-9d-ee-ca-af-e4-75')
    @winrt_commethod(6)
    def get_InteractionSourceKind(self) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_commethod(7)
    def TryGetPointerPose(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.UI.Input.Spatial.SpatialPointerPose: ...
    @winrt_commethod(8)
    def get_IsNavigatingX(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsNavigatingY(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_IsNavigatingZ(self) -> Boolean: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
    IsNavigatingX = property(get_IsNavigatingX, None)
    IsNavigatingY = property(get_IsNavigatingY, None)
    IsNavigatingZ = property(get_IsNavigatingZ, None)
class ISpatialNavigationUpdatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9b713fd7-839d-4a74-87-32-45-46-6f-c0-44-b5')
    @winrt_commethod(6)
    def get_InteractionSourceKind(self) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_commethod(7)
    def get_NormalizedOffset(self) -> Windows.Foundation.Numerics.Vector3: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
    NormalizedOffset = property(get_NormalizedOffset, None)
class ISpatialPointerInteractionSourcePose(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a7104307-2c2b-4d3a-92-a7-80-ce-d7-c4-a0-d0')
    @winrt_commethod(6)
    def get_Position(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(7)
    def get_ForwardDirection(self) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(8)
    def get_UpDirection(self) -> Windows.Foundation.Numerics.Vector3: ...
    Position = property(get_Position, None)
    ForwardDirection = property(get_ForwardDirection, None)
    UpDirection = property(get_UpDirection, None)
class ISpatialPointerInteractionSourcePose2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('eccd86b8-52db-469f-9e-3f-80-c4-7f-74-bc-e9')
    @winrt_commethod(6)
    def get_Orientation(self) -> Windows.Foundation.Numerics.Quaternion: ...
    @winrt_commethod(7)
    def get_PositionAccuracy(self) -> Windows.UI.Input.Spatial.SpatialInteractionSourcePositionAccuracy: ...
    Orientation = property(get_Orientation, None)
    PositionAccuracy = property(get_PositionAccuracy, None)
class ISpatialPointerPose(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6953a42e-c17e-357d-97-a1-72-69-d0-ed-2d-10')
    @winrt_commethod(6)
    def get_Timestamp(self) -> Windows.Perception.PerceptionTimestamp: ...
    @winrt_commethod(7)
    def get_Head(self) -> Windows.Perception.People.HeadPose: ...
    Timestamp = property(get_Timestamp, None)
    Head = property(get_Head, None)
class ISpatialPointerPose2(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('9d202b17-954e-4e0c-96-d1-b6-79-0b-6f-c2-fd')
    @winrt_commethod(6)
    def TryGetInteractionSourcePose(self, source: Windows.UI.Input.Spatial.SpatialInteractionSource) -> Windows.UI.Input.Spatial.SpatialPointerInteractionSourcePose: ...
class ISpatialPointerPose3(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('6342f3f0-ec49-5b4b-b8-d1-d1-6c-bb-16-be-84')
    @winrt_commethod(6)
    def get_Eyes(self) -> Windows.Perception.People.EyesPose: ...
    @winrt_commethod(7)
    def get_IsHeadCapturedBySystem(self) -> Boolean: ...
    Eyes = property(get_Eyes, None)
    IsHeadCapturedBySystem = property(get_IsHeadCapturedBySystem, None)
class ISpatialPointerPoseStatics(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('a25591a9-aca1-3ee0-98-16-78-5c-fb-2e-3f-b8')
    @winrt_commethod(6)
    def TryGetAtTimestamp(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, timestamp: Windows.Perception.PerceptionTimestamp) -> Windows.UI.Input.Spatial.SpatialPointerPose: ...
class ISpatialRecognitionEndedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('0e35f5cb-3f75-43f3-ac-81-d1-dc-2d-f9-b1-fb')
    @winrt_commethod(6)
    def get_InteractionSourceKind(self) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class ISpatialRecognitionStartedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('24da128f-0008-4a6d-aa-50-2a-76-f9-cf-b2-64')
    @winrt_commethod(6)
    def get_InteractionSourceKind(self) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_commethod(7)
    def TryGetPointerPose(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.UI.Input.Spatial.SpatialPointerPose: ...
    @winrt_commethod(8)
    def IsGesturePossible(self, gesture: Windows.UI.Input.Spatial.SpatialGestureSettings) -> Boolean: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class ISpatialTappedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('296d83de-f444-4aa1-b2-bf-9d-c8-8d-56-7d-a6')
    @winrt_commethod(6)
    def get_InteractionSourceKind(self) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_commethod(7)
    def TryGetPointerPose(self, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.UI.Input.Spatial.SpatialPointerPose: ...
    @winrt_commethod(8)
    def get_TapCount(self) -> UInt32: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
    TapCount = property(get_TapCount, None)
class SpatialGestureRecognizer(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Spatial.SpatialGestureRecognizer'
    @winrt_factorymethod
    def Create(cls: Windows.UI.Input.Spatial.ISpatialGestureRecognizerFactory, settings: Windows.UI.Input.Spatial.SpatialGestureSettings) -> Windows.UI.Input.Spatial.SpatialGestureRecognizer: ...
    @winrt_mixinmethod
    def add_RecognitionStarted(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialGestureRecognizer, Windows.UI.Input.Spatial.SpatialRecognitionStartedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RecognitionStarted(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_RecognitionEnded(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialGestureRecognizer, Windows.UI.Input.Spatial.SpatialRecognitionEndedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RecognitionEnded(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Tapped(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialGestureRecognizer, Windows.UI.Input.Spatial.SpatialTappedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Tapped(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_HoldStarted(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialGestureRecognizer, Windows.UI.Input.Spatial.SpatialHoldStartedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HoldStarted(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_HoldCompleted(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialGestureRecognizer, Windows.UI.Input.Spatial.SpatialHoldCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HoldCompleted(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_HoldCanceled(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialGestureRecognizer, Windows.UI.Input.Spatial.SpatialHoldCanceledEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HoldCanceled(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationStarted(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialGestureRecognizer, Windows.UI.Input.Spatial.SpatialManipulationStartedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationStarted(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationUpdated(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialGestureRecognizer, Windows.UI.Input.Spatial.SpatialManipulationUpdatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationUpdated(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationCompleted(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialGestureRecognizer, Windows.UI.Input.Spatial.SpatialManipulationCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationCompleted(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationCanceled(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialGestureRecognizer, Windows.UI.Input.Spatial.SpatialManipulationCanceledEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationCanceled(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_NavigationStarted(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialGestureRecognizer, Windows.UI.Input.Spatial.SpatialNavigationStartedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NavigationStarted(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_NavigationUpdated(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialGestureRecognizer, Windows.UI.Input.Spatial.SpatialNavigationUpdatedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NavigationUpdated(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_NavigationCompleted(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialGestureRecognizer, Windows.UI.Input.Spatial.SpatialNavigationCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NavigationCompleted(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_NavigationCanceled(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialGestureRecognizer, Windows.UI.Input.Spatial.SpatialNavigationCanceledEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NavigationCanceled(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CaptureInteraction(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer, interaction: Windows.UI.Input.Spatial.SpatialInteraction) -> Void: ...
    @winrt_mixinmethod
    def CancelPendingGestures(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer) -> Void: ...
    @winrt_mixinmethod
    def TrySetGestureSettings(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer, settings: Windows.UI.Input.Spatial.SpatialGestureSettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_GestureSettings(self: Windows.UI.Input.Spatial.ISpatialGestureRecognizer) -> Windows.UI.Input.Spatial.SpatialGestureSettings: ...
    GestureSettings = property(get_GestureSettings, None)
SpatialGestureSettings = UInt32
SpatialGestureSettings_None: SpatialGestureSettings = 0
SpatialGestureSettings_Tap: SpatialGestureSettings = 1
SpatialGestureSettings_DoubleTap: SpatialGestureSettings = 2
SpatialGestureSettings_Hold: SpatialGestureSettings = 4
SpatialGestureSettings_ManipulationTranslate: SpatialGestureSettings = 8
SpatialGestureSettings_NavigationX: SpatialGestureSettings = 16
SpatialGestureSettings_NavigationY: SpatialGestureSettings = 32
SpatialGestureSettings_NavigationZ: SpatialGestureSettings = 64
SpatialGestureSettings_NavigationRailsX: SpatialGestureSettings = 128
SpatialGestureSettings_NavigationRailsY: SpatialGestureSettings = 256
SpatialGestureSettings_NavigationRailsZ: SpatialGestureSettings = 512
class SpatialHoldCanceledEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Spatial.SpatialHoldCanceledEventArgs'
    @winrt_mixinmethod
    def get_InteractionSourceKind(self: Windows.UI.Input.Spatial.ISpatialHoldCanceledEventArgs) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class SpatialHoldCompletedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Spatial.SpatialHoldCompletedEventArgs'
    @winrt_mixinmethod
    def get_InteractionSourceKind(self: Windows.UI.Input.Spatial.ISpatialHoldCompletedEventArgs) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class SpatialHoldStartedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Spatial.SpatialHoldStartedEventArgs'
    @winrt_mixinmethod
    def get_InteractionSourceKind(self: Windows.UI.Input.Spatial.ISpatialHoldStartedEventArgs) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_mixinmethod
    def TryGetPointerPose(self: Windows.UI.Input.Spatial.ISpatialHoldStartedEventArgs, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.UI.Input.Spatial.SpatialPointerPose: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class SpatialInteraction(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Spatial.SpatialInteraction'
    @winrt_mixinmethod
    def get_SourceState(self: Windows.UI.Input.Spatial.ISpatialInteraction) -> Windows.UI.Input.Spatial.SpatialInteractionSourceState: ...
    SourceState = property(get_SourceState, None)
class SpatialInteractionController(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Spatial.SpatialInteractionController'
    @winrt_mixinmethod
    def get_HasTouchpad(self: Windows.UI.Input.Spatial.ISpatialInteractionController) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasThumbstick(self: Windows.UI.Input.Spatial.ISpatialInteractionController) -> Boolean: ...
    @winrt_mixinmethod
    def get_SimpleHapticsController(self: Windows.UI.Input.Spatial.ISpatialInteractionController) -> Windows.Devices.Haptics.SimpleHapticsController: ...
    @winrt_mixinmethod
    def get_VendorId(self: Windows.UI.Input.Spatial.ISpatialInteractionController) -> UInt16: ...
    @winrt_mixinmethod
    def get_ProductId(self: Windows.UI.Input.Spatial.ISpatialInteractionController) -> UInt16: ...
    @winrt_mixinmethod
    def get_Version(self: Windows.UI.Input.Spatial.ISpatialInteractionController) -> UInt16: ...
    @winrt_mixinmethod
    def TryGetRenderableModelAsync(self: Windows.UI.Input.Spatial.ISpatialInteractionController2) -> Windows.Foundation.IAsyncOperation[Windows.Storage.Streams.IRandomAccessStreamWithContentType]: ...
    @winrt_mixinmethod
    def TryGetBatteryReport(self: Windows.UI.Input.Spatial.ISpatialInteractionController3) -> Windows.Devices.Power.BatteryReport: ...
    HasTouchpad = property(get_HasTouchpad, None)
    HasThumbstick = property(get_HasThumbstick, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
    VendorId = property(get_VendorId, None)
    ProductId = property(get_ProductId, None)
    Version = property(get_Version, None)
class SpatialInteractionControllerProperties(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Spatial.SpatialInteractionControllerProperties'
    @winrt_mixinmethod
    def get_IsTouchpadTouched(self: Windows.UI.Input.Spatial.ISpatialInteractionControllerProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsTouchpadPressed(self: Windows.UI.Input.Spatial.ISpatialInteractionControllerProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsThumbstickPressed(self: Windows.UI.Input.Spatial.ISpatialInteractionControllerProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_ThumbstickX(self: Windows.UI.Input.Spatial.ISpatialInteractionControllerProperties) -> Double: ...
    @winrt_mixinmethod
    def get_ThumbstickY(self: Windows.UI.Input.Spatial.ISpatialInteractionControllerProperties) -> Double: ...
    @winrt_mixinmethod
    def get_TouchpadX(self: Windows.UI.Input.Spatial.ISpatialInteractionControllerProperties) -> Double: ...
    @winrt_mixinmethod
    def get_TouchpadY(self: Windows.UI.Input.Spatial.ISpatialInteractionControllerProperties) -> Double: ...
    IsTouchpadTouched = property(get_IsTouchpadTouched, None)
    IsTouchpadPressed = property(get_IsTouchpadPressed, None)
    IsThumbstickPressed = property(get_IsThumbstickPressed, None)
    ThumbstickX = property(get_ThumbstickX, None)
    ThumbstickY = property(get_ThumbstickY, None)
    TouchpadX = property(get_TouchpadX, None)
    TouchpadY = property(get_TouchpadY, None)
class SpatialInteractionDetectedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Spatial.SpatialInteractionDetectedEventArgs'
    @winrt_mixinmethod
    def get_InteractionSourceKind(self: Windows.UI.Input.Spatial.ISpatialInteractionDetectedEventArgs) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_mixinmethod
    def TryGetPointerPose(self: Windows.UI.Input.Spatial.ISpatialInteractionDetectedEventArgs, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.UI.Input.Spatial.SpatialPointerPose: ...
    @winrt_mixinmethod
    def get_Interaction(self: Windows.UI.Input.Spatial.ISpatialInteractionDetectedEventArgs) -> Windows.UI.Input.Spatial.SpatialInteraction: ...
    @winrt_mixinmethod
    def get_InteractionSource(self: Windows.UI.Input.Spatial.ISpatialInteractionDetectedEventArgs2) -> Windows.UI.Input.Spatial.SpatialInteractionSource: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
    Interaction = property(get_Interaction, None)
    InteractionSource = property(get_InteractionSource, None)
class SpatialInteractionManager(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Spatial.SpatialInteractionManager'
    @winrt_mixinmethod
    def add_SourceDetected(self: Windows.UI.Input.Spatial.ISpatialInteractionManager, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialInteractionManager, Windows.UI.Input.Spatial.SpatialInteractionSourceEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceDetected(self: Windows.UI.Input.Spatial.ISpatialInteractionManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SourceLost(self: Windows.UI.Input.Spatial.ISpatialInteractionManager, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialInteractionManager, Windows.UI.Input.Spatial.SpatialInteractionSourceEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceLost(self: Windows.UI.Input.Spatial.ISpatialInteractionManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SourceUpdated(self: Windows.UI.Input.Spatial.ISpatialInteractionManager, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialInteractionManager, Windows.UI.Input.Spatial.SpatialInteractionSourceEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceUpdated(self: Windows.UI.Input.Spatial.ISpatialInteractionManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SourcePressed(self: Windows.UI.Input.Spatial.ISpatialInteractionManager, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialInteractionManager, Windows.UI.Input.Spatial.SpatialInteractionSourceEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourcePressed(self: Windows.UI.Input.Spatial.ISpatialInteractionManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SourceReleased(self: Windows.UI.Input.Spatial.ISpatialInteractionManager, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialInteractionManager, Windows.UI.Input.Spatial.SpatialInteractionSourceEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceReleased(self: Windows.UI.Input.Spatial.ISpatialInteractionManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_InteractionDetected(self: Windows.UI.Input.Spatial.ISpatialInteractionManager, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Spatial.SpatialInteractionManager, Windows.UI.Input.Spatial.SpatialInteractionDetectedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_InteractionDetected(self: Windows.UI.Input.Spatial.ISpatialInteractionManager, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetDetectedSourcesAtTimestamp(self: Windows.UI.Input.Spatial.ISpatialInteractionManager, timeStamp: Windows.Perception.PerceptionTimestamp) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Spatial.SpatialInteractionSourceState]: ...
    @winrt_classmethod
    def IsSourceKindSupported(cls: Windows.UI.Input.Spatial.ISpatialInteractionManagerStatics2, kind: Windows.UI.Input.Spatial.SpatialInteractionSourceKind) -> Boolean: ...
    @winrt_classmethod
    def GetForCurrentView(cls: Windows.UI.Input.Spatial.ISpatialInteractionManagerStatics) -> Windows.UI.Input.Spatial.SpatialInteractionManager: ...
SpatialInteractionPressKind = Int32
SpatialInteractionPressKind_None: SpatialInteractionPressKind = 0
SpatialInteractionPressKind_Select: SpatialInteractionPressKind = 1
SpatialInteractionPressKind_Menu: SpatialInteractionPressKind = 2
SpatialInteractionPressKind_Grasp: SpatialInteractionPressKind = 3
SpatialInteractionPressKind_Touchpad: SpatialInteractionPressKind = 4
SpatialInteractionPressKind_Thumbstick: SpatialInteractionPressKind = 5
class SpatialInteractionSource(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Spatial.SpatialInteractionSource'
    @winrt_mixinmethod
    def get_Id(self: Windows.UI.Input.Spatial.ISpatialInteractionSource) -> UInt32: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.UI.Input.Spatial.ISpatialInteractionSource) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_mixinmethod
    def get_IsPointingSupported(self: Windows.UI.Input.Spatial.ISpatialInteractionSource2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsMenuSupported(self: Windows.UI.Input.Spatial.ISpatialInteractionSource2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsGraspSupported(self: Windows.UI.Input.Spatial.ISpatialInteractionSource2) -> Boolean: ...
    @winrt_mixinmethod
    def get_Controller(self: Windows.UI.Input.Spatial.ISpatialInteractionSource2) -> Windows.UI.Input.Spatial.SpatialInteractionController: ...
    @winrt_mixinmethod
    def TryGetStateAtTimestamp(self: Windows.UI.Input.Spatial.ISpatialInteractionSource2, timestamp: Windows.Perception.PerceptionTimestamp) -> Windows.UI.Input.Spatial.SpatialInteractionSourceState: ...
    @winrt_mixinmethod
    def get_Handedness(self: Windows.UI.Input.Spatial.ISpatialInteractionSource3) -> Windows.UI.Input.Spatial.SpatialInteractionSourceHandedness: ...
    @winrt_mixinmethod
    def TryCreateHandMeshObserver(self: Windows.UI.Input.Spatial.ISpatialInteractionSource4) -> Windows.Perception.People.HandMeshObserver: ...
    @winrt_mixinmethod
    def TryCreateHandMeshObserverAsync(self: Windows.UI.Input.Spatial.ISpatialInteractionSource4) -> Windows.Foundation.IAsyncOperation[Windows.Perception.People.HandMeshObserver]: ...
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
    IsPointingSupported = property(get_IsPointingSupported, None)
    IsMenuSupported = property(get_IsMenuSupported, None)
    IsGraspSupported = property(get_IsGraspSupported, None)
    Controller = property(get_Controller, None)
    Handedness = property(get_Handedness, None)
class SpatialInteractionSourceEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Spatial.SpatialInteractionSourceEventArgs'
    @winrt_mixinmethod
    def get_State(self: Windows.UI.Input.Spatial.ISpatialInteractionSourceEventArgs) -> Windows.UI.Input.Spatial.SpatialInteractionSourceState: ...
    @winrt_mixinmethod
    def get_PressKind(self: Windows.UI.Input.Spatial.ISpatialInteractionSourceEventArgs2) -> Windows.UI.Input.Spatial.SpatialInteractionPressKind: ...
    State = property(get_State, None)
    PressKind = property(get_PressKind, None)
SpatialInteractionSourceHandedness = Int32
SpatialInteractionSourceHandedness_Unspecified: SpatialInteractionSourceHandedness = 0
SpatialInteractionSourceHandedness_Left: SpatialInteractionSourceHandedness = 1
SpatialInteractionSourceHandedness_Right: SpatialInteractionSourceHandedness = 2
SpatialInteractionSourceKind = Int32
SpatialInteractionSourceKind_Other: SpatialInteractionSourceKind = 0
SpatialInteractionSourceKind_Hand: SpatialInteractionSourceKind = 1
SpatialInteractionSourceKind_Voice: SpatialInteractionSourceKind = 2
SpatialInteractionSourceKind_Controller: SpatialInteractionSourceKind = 3
class SpatialInteractionSourceLocation(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Spatial.SpatialInteractionSourceLocation'
    @winrt_mixinmethod
    def get_Position(self: Windows.UI.Input.Spatial.ISpatialInteractionSourceLocation) -> Windows.Foundation.IReference[Windows.Foundation.Numerics.Vector3]: ...
    @winrt_mixinmethod
    def get_Velocity(self: Windows.UI.Input.Spatial.ISpatialInteractionSourceLocation) -> Windows.Foundation.IReference[Windows.Foundation.Numerics.Vector3]: ...
    @winrt_mixinmethod
    def get_Orientation(self: Windows.UI.Input.Spatial.ISpatialInteractionSourceLocation2) -> Windows.Foundation.IReference[Windows.Foundation.Numerics.Quaternion]: ...
    @winrt_mixinmethod
    def get_PositionAccuracy(self: Windows.UI.Input.Spatial.ISpatialInteractionSourceLocation3) -> Windows.UI.Input.Spatial.SpatialInteractionSourcePositionAccuracy: ...
    @winrt_mixinmethod
    def get_AngularVelocity(self: Windows.UI.Input.Spatial.ISpatialInteractionSourceLocation3) -> Windows.Foundation.IReference[Windows.Foundation.Numerics.Vector3]: ...
    @winrt_mixinmethod
    def get_SourcePointerPose(self: Windows.UI.Input.Spatial.ISpatialInteractionSourceLocation3) -> Windows.UI.Input.Spatial.SpatialPointerInteractionSourcePose: ...
    Position = property(get_Position, None)
    Velocity = property(get_Velocity, None)
    Orientation = property(get_Orientation, None)
    PositionAccuracy = property(get_PositionAccuracy, None)
    AngularVelocity = property(get_AngularVelocity, None)
    SourcePointerPose = property(get_SourcePointerPose, None)
SpatialInteractionSourcePositionAccuracy = Int32
SpatialInteractionSourcePositionAccuracy_High: SpatialInteractionSourcePositionAccuracy = 0
SpatialInteractionSourcePositionAccuracy_Approximate: SpatialInteractionSourcePositionAccuracy = 1
class SpatialInteractionSourceProperties(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Spatial.SpatialInteractionSourceProperties'
    @winrt_mixinmethod
    def TryGetSourceLossMitigationDirection(self: Windows.UI.Input.Spatial.ISpatialInteractionSourceProperties, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.Foundation.IReference[Windows.Foundation.Numerics.Vector3]: ...
    @winrt_mixinmethod
    def get_SourceLossRisk(self: Windows.UI.Input.Spatial.ISpatialInteractionSourceProperties) -> Double: ...
    @winrt_mixinmethod
    def TryGetLocation(self: Windows.UI.Input.Spatial.ISpatialInteractionSourceProperties, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.UI.Input.Spatial.SpatialInteractionSourceLocation: ...
    SourceLossRisk = property(get_SourceLossRisk, None)
class SpatialInteractionSourceState(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Spatial.SpatialInteractionSourceState'
    @winrt_mixinmethod
    def get_Source(self: Windows.UI.Input.Spatial.ISpatialInteractionSourceState) -> Windows.UI.Input.Spatial.SpatialInteractionSource: ...
    @winrt_mixinmethod
    def get_Properties(self: Windows.UI.Input.Spatial.ISpatialInteractionSourceState) -> Windows.UI.Input.Spatial.SpatialInteractionSourceProperties: ...
    @winrt_mixinmethod
    def get_IsPressed(self: Windows.UI.Input.Spatial.ISpatialInteractionSourceState) -> Boolean: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.UI.Input.Spatial.ISpatialInteractionSourceState) -> Windows.Perception.PerceptionTimestamp: ...
    @winrt_mixinmethod
    def TryGetPointerPose(self: Windows.UI.Input.Spatial.ISpatialInteractionSourceState, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.UI.Input.Spatial.SpatialPointerPose: ...
    @winrt_mixinmethod
    def get_IsSelectPressed(self: Windows.UI.Input.Spatial.ISpatialInteractionSourceState2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsMenuPressed(self: Windows.UI.Input.Spatial.ISpatialInteractionSourceState2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsGrasped(self: Windows.UI.Input.Spatial.ISpatialInteractionSourceState2) -> Boolean: ...
    @winrt_mixinmethod
    def get_SelectPressedValue(self: Windows.UI.Input.Spatial.ISpatialInteractionSourceState2) -> Double: ...
    @winrt_mixinmethod
    def get_ControllerProperties(self: Windows.UI.Input.Spatial.ISpatialInteractionSourceState2) -> Windows.UI.Input.Spatial.SpatialInteractionControllerProperties: ...
    @winrt_mixinmethod
    def TryGetHandPose(self: Windows.UI.Input.Spatial.ISpatialInteractionSourceState3) -> Windows.Perception.People.HandPose: ...
    Source = property(get_Source, None)
    Properties = property(get_Properties, None)
    IsPressed = property(get_IsPressed, None)
    Timestamp = property(get_Timestamp, None)
    IsSelectPressed = property(get_IsSelectPressed, None)
    IsMenuPressed = property(get_IsMenuPressed, None)
    IsGrasped = property(get_IsGrasped, None)
    SelectPressedValue = property(get_SelectPressedValue, None)
    ControllerProperties = property(get_ControllerProperties, None)
class SpatialManipulationCanceledEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Spatial.SpatialManipulationCanceledEventArgs'
    @winrt_mixinmethod
    def get_InteractionSourceKind(self: Windows.UI.Input.Spatial.ISpatialManipulationCanceledEventArgs) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class SpatialManipulationCompletedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Spatial.SpatialManipulationCompletedEventArgs'
    @winrt_mixinmethod
    def get_InteractionSourceKind(self: Windows.UI.Input.Spatial.ISpatialManipulationCompletedEventArgs) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_mixinmethod
    def TryGetCumulativeDelta(self: Windows.UI.Input.Spatial.ISpatialManipulationCompletedEventArgs, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.UI.Input.Spatial.SpatialManipulationDelta: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class SpatialManipulationDelta(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Spatial.SpatialManipulationDelta'
    @winrt_mixinmethod
    def get_Translation(self: Windows.UI.Input.Spatial.ISpatialManipulationDelta) -> Windows.Foundation.Numerics.Vector3: ...
    Translation = property(get_Translation, None)
class SpatialManipulationStartedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Spatial.SpatialManipulationStartedEventArgs'
    @winrt_mixinmethod
    def get_InteractionSourceKind(self: Windows.UI.Input.Spatial.ISpatialManipulationStartedEventArgs) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_mixinmethod
    def TryGetPointerPose(self: Windows.UI.Input.Spatial.ISpatialManipulationStartedEventArgs, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.UI.Input.Spatial.SpatialPointerPose: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class SpatialManipulationUpdatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Spatial.SpatialManipulationUpdatedEventArgs'
    @winrt_mixinmethod
    def get_InteractionSourceKind(self: Windows.UI.Input.Spatial.ISpatialManipulationUpdatedEventArgs) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_mixinmethod
    def TryGetCumulativeDelta(self: Windows.UI.Input.Spatial.ISpatialManipulationUpdatedEventArgs, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.UI.Input.Spatial.SpatialManipulationDelta: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class SpatialNavigationCanceledEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Spatial.SpatialNavigationCanceledEventArgs'
    @winrt_mixinmethod
    def get_InteractionSourceKind(self: Windows.UI.Input.Spatial.ISpatialNavigationCanceledEventArgs) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class SpatialNavigationCompletedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Spatial.SpatialNavigationCompletedEventArgs'
    @winrt_mixinmethod
    def get_InteractionSourceKind(self: Windows.UI.Input.Spatial.ISpatialNavigationCompletedEventArgs) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_mixinmethod
    def get_NormalizedOffset(self: Windows.UI.Input.Spatial.ISpatialNavigationCompletedEventArgs) -> Windows.Foundation.Numerics.Vector3: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
    NormalizedOffset = property(get_NormalizedOffset, None)
class SpatialNavigationStartedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Spatial.SpatialNavigationStartedEventArgs'
    @winrt_mixinmethod
    def get_InteractionSourceKind(self: Windows.UI.Input.Spatial.ISpatialNavigationStartedEventArgs) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_mixinmethod
    def TryGetPointerPose(self: Windows.UI.Input.Spatial.ISpatialNavigationStartedEventArgs, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.UI.Input.Spatial.SpatialPointerPose: ...
    @winrt_mixinmethod
    def get_IsNavigatingX(self: Windows.UI.Input.Spatial.ISpatialNavigationStartedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsNavigatingY(self: Windows.UI.Input.Spatial.ISpatialNavigationStartedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsNavigatingZ(self: Windows.UI.Input.Spatial.ISpatialNavigationStartedEventArgs) -> Boolean: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
    IsNavigatingX = property(get_IsNavigatingX, None)
    IsNavigatingY = property(get_IsNavigatingY, None)
    IsNavigatingZ = property(get_IsNavigatingZ, None)
class SpatialNavigationUpdatedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Spatial.SpatialNavigationUpdatedEventArgs'
    @winrt_mixinmethod
    def get_InteractionSourceKind(self: Windows.UI.Input.Spatial.ISpatialNavigationUpdatedEventArgs) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_mixinmethod
    def get_NormalizedOffset(self: Windows.UI.Input.Spatial.ISpatialNavigationUpdatedEventArgs) -> Windows.Foundation.Numerics.Vector3: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
    NormalizedOffset = property(get_NormalizedOffset, None)
class SpatialPointerInteractionSourcePose(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Spatial.SpatialPointerInteractionSourcePose'
    @winrt_mixinmethod
    def get_Position(self: Windows.UI.Input.Spatial.ISpatialPointerInteractionSourcePose) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_ForwardDirection(self: Windows.UI.Input.Spatial.ISpatialPointerInteractionSourcePose) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_UpDirection(self: Windows.UI.Input.Spatial.ISpatialPointerInteractionSourcePose) -> Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_Orientation(self: Windows.UI.Input.Spatial.ISpatialPointerInteractionSourcePose2) -> Windows.Foundation.Numerics.Quaternion: ...
    @winrt_mixinmethod
    def get_PositionAccuracy(self: Windows.UI.Input.Spatial.ISpatialPointerInteractionSourcePose2) -> Windows.UI.Input.Spatial.SpatialInteractionSourcePositionAccuracy: ...
    Position = property(get_Position, None)
    ForwardDirection = property(get_ForwardDirection, None)
    UpDirection = property(get_UpDirection, None)
    Orientation = property(get_Orientation, None)
    PositionAccuracy = property(get_PositionAccuracy, None)
class SpatialPointerPose(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Spatial.SpatialPointerPose'
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.UI.Input.Spatial.ISpatialPointerPose) -> Windows.Perception.PerceptionTimestamp: ...
    @winrt_mixinmethod
    def get_Head(self: Windows.UI.Input.Spatial.ISpatialPointerPose) -> Windows.Perception.People.HeadPose: ...
    @winrt_mixinmethod
    def TryGetInteractionSourcePose(self: Windows.UI.Input.Spatial.ISpatialPointerPose2, source: Windows.UI.Input.Spatial.SpatialInteractionSource) -> Windows.UI.Input.Spatial.SpatialPointerInteractionSourcePose: ...
    @winrt_mixinmethod
    def get_Eyes(self: Windows.UI.Input.Spatial.ISpatialPointerPose3) -> Windows.Perception.People.EyesPose: ...
    @winrt_mixinmethod
    def get_IsHeadCapturedBySystem(self: Windows.UI.Input.Spatial.ISpatialPointerPose3) -> Boolean: ...
    @winrt_classmethod
    def TryGetAtTimestamp(cls: Windows.UI.Input.Spatial.ISpatialPointerPoseStatics, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem, timestamp: Windows.Perception.PerceptionTimestamp) -> Windows.UI.Input.Spatial.SpatialPointerPose: ...
    Timestamp = property(get_Timestamp, None)
    Head = property(get_Head, None)
    Eyes = property(get_Eyes, None)
    IsHeadCapturedBySystem = property(get_IsHeadCapturedBySystem, None)
class SpatialRecognitionEndedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Spatial.SpatialRecognitionEndedEventArgs'
    @winrt_mixinmethod
    def get_InteractionSourceKind(self: Windows.UI.Input.Spatial.ISpatialRecognitionEndedEventArgs) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class SpatialRecognitionStartedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Spatial.SpatialRecognitionStartedEventArgs'
    @winrt_mixinmethod
    def get_InteractionSourceKind(self: Windows.UI.Input.Spatial.ISpatialRecognitionStartedEventArgs) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_mixinmethod
    def TryGetPointerPose(self: Windows.UI.Input.Spatial.ISpatialRecognitionStartedEventArgs, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.UI.Input.Spatial.SpatialPointerPose: ...
    @winrt_mixinmethod
    def IsGesturePossible(self: Windows.UI.Input.Spatial.ISpatialRecognitionStartedEventArgs, gesture: Windows.UI.Input.Spatial.SpatialGestureSettings) -> Boolean: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class SpatialTappedEventArgs(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    ClassId = 'Windows.UI.Input.Spatial.SpatialTappedEventArgs'
    @winrt_mixinmethod
    def get_InteractionSourceKind(self: Windows.UI.Input.Spatial.ISpatialTappedEventArgs) -> Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_mixinmethod
    def TryGetPointerPose(self: Windows.UI.Input.Spatial.ISpatialTappedEventArgs, coordinateSystem: Windows.Perception.Spatial.SpatialCoordinateSystem) -> Windows.UI.Input.Spatial.SpatialPointerPose: ...
    @winrt_mixinmethod
    def get_TapCount(self: Windows.UI.Input.Spatial.ISpatialTappedEventArgs) -> UInt32: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
    TapCount = property(get_TapCount, None)
make_head(_module, 'ISpatialGestureRecognizer')
make_head(_module, 'ISpatialGestureRecognizerFactory')
make_head(_module, 'ISpatialHoldCanceledEventArgs')
make_head(_module, 'ISpatialHoldCompletedEventArgs')
make_head(_module, 'ISpatialHoldStartedEventArgs')
make_head(_module, 'ISpatialInteraction')
make_head(_module, 'ISpatialInteractionController')
make_head(_module, 'ISpatialInteractionController2')
make_head(_module, 'ISpatialInteractionController3')
make_head(_module, 'ISpatialInteractionControllerProperties')
make_head(_module, 'ISpatialInteractionDetectedEventArgs')
make_head(_module, 'ISpatialInteractionDetectedEventArgs2')
make_head(_module, 'ISpatialInteractionManager')
make_head(_module, 'ISpatialInteractionManagerStatics')
make_head(_module, 'ISpatialInteractionManagerStatics2')
make_head(_module, 'ISpatialInteractionSource')
make_head(_module, 'ISpatialInteractionSource2')
make_head(_module, 'ISpatialInteractionSource3')
make_head(_module, 'ISpatialInteractionSource4')
make_head(_module, 'ISpatialInteractionSourceEventArgs')
make_head(_module, 'ISpatialInteractionSourceEventArgs2')
make_head(_module, 'ISpatialInteractionSourceLocation')
make_head(_module, 'ISpatialInteractionSourceLocation2')
make_head(_module, 'ISpatialInteractionSourceLocation3')
make_head(_module, 'ISpatialInteractionSourceProperties')
make_head(_module, 'ISpatialInteractionSourceState')
make_head(_module, 'ISpatialInteractionSourceState2')
make_head(_module, 'ISpatialInteractionSourceState3')
make_head(_module, 'ISpatialManipulationCanceledEventArgs')
make_head(_module, 'ISpatialManipulationCompletedEventArgs')
make_head(_module, 'ISpatialManipulationDelta')
make_head(_module, 'ISpatialManipulationStartedEventArgs')
make_head(_module, 'ISpatialManipulationUpdatedEventArgs')
make_head(_module, 'ISpatialNavigationCanceledEventArgs')
make_head(_module, 'ISpatialNavigationCompletedEventArgs')
make_head(_module, 'ISpatialNavigationStartedEventArgs')
make_head(_module, 'ISpatialNavigationUpdatedEventArgs')
make_head(_module, 'ISpatialPointerInteractionSourcePose')
make_head(_module, 'ISpatialPointerInteractionSourcePose2')
make_head(_module, 'ISpatialPointerPose')
make_head(_module, 'ISpatialPointerPose2')
make_head(_module, 'ISpatialPointerPose3')
make_head(_module, 'ISpatialPointerPoseStatics')
make_head(_module, 'ISpatialRecognitionEndedEventArgs')
make_head(_module, 'ISpatialRecognitionStartedEventArgs')
make_head(_module, 'ISpatialTappedEventArgs')
make_head(_module, 'SpatialGestureRecognizer')
make_head(_module, 'SpatialHoldCanceledEventArgs')
make_head(_module, 'SpatialHoldCompletedEventArgs')
make_head(_module, 'SpatialHoldStartedEventArgs')
make_head(_module, 'SpatialInteraction')
make_head(_module, 'SpatialInteractionController')
make_head(_module, 'SpatialInteractionControllerProperties')
make_head(_module, 'SpatialInteractionDetectedEventArgs')
make_head(_module, 'SpatialInteractionManager')
make_head(_module, 'SpatialInteractionSource')
make_head(_module, 'SpatialInteractionSourceEventArgs')
make_head(_module, 'SpatialInteractionSourceLocation')
make_head(_module, 'SpatialInteractionSourceProperties')
make_head(_module, 'SpatialInteractionSourceState')
make_head(_module, 'SpatialManipulationCanceledEventArgs')
make_head(_module, 'SpatialManipulationCompletedEventArgs')
make_head(_module, 'SpatialManipulationDelta')
make_head(_module, 'SpatialManipulationStartedEventArgs')
make_head(_module, 'SpatialManipulationUpdatedEventArgs')
make_head(_module, 'SpatialNavigationCanceledEventArgs')
make_head(_module, 'SpatialNavigationCompletedEventArgs')
make_head(_module, 'SpatialNavigationStartedEventArgs')
make_head(_module, 'SpatialNavigationUpdatedEventArgs')
make_head(_module, 'SpatialPointerInteractionSourcePose')
make_head(_module, 'SpatialPointerPose')
make_head(_module, 'SpatialRecognitionEndedEventArgs')
make_head(_module, 'SpatialRecognitionStartedEventArgs')
make_head(_module, 'SpatialTappedEventArgs')
