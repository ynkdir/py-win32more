from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Devices.Haptics
import win32more.Windows.Devices.Power
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Foundation.Numerics
import win32more.Windows.Perception
import win32more.Windows.Perception.People
import win32more.Windows.Perception.Spatial
import win32more.Windows.Storage.Streams
import win32more.Windows.UI.Input.Spatial
import win32more.Windows.Win32.System.WinRT
class ISpatialGestureRecognizer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialGestureRecognizer'
    _iid_ = Guid('{71605bcc-0c35-4673-adbd-cc04caa6ef45}')
    @winrt_commethod(6)
    def add_RecognitionStarted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialGestureRecognizer, win32more.Windows.UI.Input.Spatial.SpatialRecognitionStartedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_RecognitionStarted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_RecognitionEnded(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialGestureRecognizer, win32more.Windows.UI.Input.Spatial.SpatialRecognitionEndedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_RecognitionEnded(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_Tapped(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialGestureRecognizer, win32more.Windows.UI.Input.Spatial.SpatialTappedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_Tapped(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_HoldStarted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialGestureRecognizer, win32more.Windows.UI.Input.Spatial.SpatialHoldStartedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_HoldStarted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_HoldCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialGestureRecognizer, win32more.Windows.UI.Input.Spatial.SpatialHoldCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_HoldCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_HoldCanceled(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialGestureRecognizer, win32more.Windows.UI.Input.Spatial.SpatialHoldCanceledEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_HoldCanceled(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_ManipulationStarted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialGestureRecognizer, win32more.Windows.UI.Input.Spatial.SpatialManipulationStartedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_ManipulationStarted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(20)
    def add_ManipulationUpdated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialGestureRecognizer, win32more.Windows.UI.Input.Spatial.SpatialManipulationUpdatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(21)
    def remove_ManipulationUpdated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(22)
    def add_ManipulationCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialGestureRecognizer, win32more.Windows.UI.Input.Spatial.SpatialManipulationCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(23)
    def remove_ManipulationCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(24)
    def add_ManipulationCanceled(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialGestureRecognizer, win32more.Windows.UI.Input.Spatial.SpatialManipulationCanceledEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(25)
    def remove_ManipulationCanceled(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(26)
    def add_NavigationStarted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialGestureRecognizer, win32more.Windows.UI.Input.Spatial.SpatialNavigationStartedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(27)
    def remove_NavigationStarted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(28)
    def add_NavigationUpdated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialGestureRecognizer, win32more.Windows.UI.Input.Spatial.SpatialNavigationUpdatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(29)
    def remove_NavigationUpdated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(30)
    def add_NavigationCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialGestureRecognizer, win32more.Windows.UI.Input.Spatial.SpatialNavigationCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(31)
    def remove_NavigationCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(32)
    def add_NavigationCanceled(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialGestureRecognizer, win32more.Windows.UI.Input.Spatial.SpatialNavigationCanceledEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(33)
    def remove_NavigationCanceled(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(34)
    def CaptureInteraction(self, interaction: win32more.Windows.UI.Input.Spatial.SpatialInteraction) -> Void: ...
    @winrt_commethod(35)
    def CancelPendingGestures(self) -> Void: ...
    @winrt_commethod(36)
    def TrySetGestureSettings(self, settings: win32more.Windows.UI.Input.Spatial.SpatialGestureSettings) -> Boolean: ...
    @winrt_commethod(37)
    def get_GestureSettings(self) -> win32more.Windows.UI.Input.Spatial.SpatialGestureSettings: ...
    GestureSettings = property(get_GestureSettings, None)
    RecognitionStarted = event()
    RecognitionEnded = event()
    Tapped = event()
    HoldStarted = event()
    HoldCompleted = event()
    HoldCanceled = event()
    ManipulationStarted = event()
    ManipulationUpdated = event()
    ManipulationCompleted = event()
    ManipulationCanceled = event()
    NavigationStarted = event()
    NavigationUpdated = event()
    NavigationCompleted = event()
    NavigationCanceled = event()
class ISpatialGestureRecognizerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialGestureRecognizerFactory'
    _iid_ = Guid('{77214186-57b9-3150-8382-698b24e264d0}')
    @winrt_commethod(6)
    def Create(self, settings: win32more.Windows.UI.Input.Spatial.SpatialGestureSettings) -> win32more.Windows.UI.Input.Spatial.SpatialGestureRecognizer: ...
class ISpatialHoldCanceledEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialHoldCanceledEventArgs'
    _iid_ = Guid('{5dfcb667-4caa-4093-8c35-b601a839f31b}')
    @winrt_commethod(6)
    def get_InteractionSourceKind(self) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class ISpatialHoldCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialHoldCompletedEventArgs'
    _iid_ = Guid('{3f64470b-4cfd-43da-8dc4-e64552173971}')
    @winrt_commethod(6)
    def get_InteractionSourceKind(self) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class ISpatialHoldStartedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialHoldStartedEventArgs'
    _iid_ = Guid('{8e343d79-acb6-4144-8615-2cfba8a3cb3f}')
    @winrt_commethod(6)
    def get_InteractionSourceKind(self) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_commethod(7)
    def TryGetPointerPose(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.UI.Input.Spatial.SpatialPointerPose: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class ISpatialInteraction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialInteraction'
    _iid_ = Guid('{fc967639-88e6-4646-9112-4344aaec9dfa}')
    @winrt_commethod(6)
    def get_SourceState(self) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceState: ...
    SourceState = property(get_SourceState, None)
class ISpatialInteractionController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialInteractionController'
    _iid_ = Guid('{5f0e5ba3-0954-4e97-86c5-e7f30b114dfd}')
    @winrt_commethod(6)
    def get_HasTouchpad(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_HasThumbstick(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_SimpleHapticsController(self) -> win32more.Windows.Devices.Haptics.SimpleHapticsController: ...
    @winrt_commethod(9)
    def get_VendorId(self) -> UInt16: ...
    @winrt_commethod(10)
    def get_ProductId(self) -> UInt16: ...
    @winrt_commethod(11)
    def get_Version(self) -> UInt16: ...
    HasThumbstick = property(get_HasThumbstick, None)
    HasTouchpad = property(get_HasTouchpad, None)
    ProductId = property(get_ProductId, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
    VendorId = property(get_VendorId, None)
    Version = property(get_Version, None)
class ISpatialInteractionController2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialInteractionController2'
    _iid_ = Guid('{35b6d924-c7a2-49b7-b72e-5436b2fb8f9c}')
    @winrt_commethod(6)
    def TryGetRenderableModelAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStreamWithContentType]: ...
class ISpatialInteractionController3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialInteractionController3'
    _iid_ = Guid('{628466a0-9d91-4a0b-888d-165e670a8cd5}')
    @winrt_commethod(6)
    def TryGetBatteryReport(self) -> win32more.Windows.Devices.Power.BatteryReport: ...
class ISpatialInteractionControllerProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialInteractionControllerProperties'
    _iid_ = Guid('{61056fb1-7ba9-4e35-b93f-9272cba9b28b}')
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
    IsThumbstickPressed = property(get_IsThumbstickPressed, None)
    IsTouchpadPressed = property(get_IsTouchpadPressed, None)
    IsTouchpadTouched = property(get_IsTouchpadTouched, None)
    ThumbstickX = property(get_ThumbstickX, None)
    ThumbstickY = property(get_ThumbstickY, None)
    TouchpadX = property(get_TouchpadX, None)
    TouchpadY = property(get_TouchpadY, None)
class ISpatialInteractionDetectedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialInteractionDetectedEventArgs'
    _iid_ = Guid('{075878e4-5961-3b41-9dfb-cea5d89cc38a}')
    @winrt_commethod(6)
    def get_InteractionSourceKind(self) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_commethod(7)
    def TryGetPointerPose(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.UI.Input.Spatial.SpatialPointerPose: ...
    @winrt_commethod(8)
    def get_Interaction(self) -> win32more.Windows.UI.Input.Spatial.SpatialInteraction: ...
    Interaction = property(get_Interaction, None)
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class ISpatialInteractionDetectedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialInteractionDetectedEventArgs2'
    _iid_ = Guid('{7b263e93-5f13-419c-97d5-834678266aa6}')
    @winrt_commethod(6)
    def get_InteractionSource(self) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSource: ...
    InteractionSource = property(get_InteractionSource, None)
class ISpatialInteractionManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialInteractionManager'
    _iid_ = Guid('{32a64ea8-a15a-3995-b8bd-80513cb5adef}')
    @winrt_commethod(6)
    def add_SourceDetected(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialInteractionManager, win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_SourceDetected(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_SourceLost(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialInteractionManager, win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_SourceLost(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_SourceUpdated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialInteractionManager, win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_SourceUpdated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_SourcePressed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialInteractionManager, win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_SourcePressed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_SourceReleased(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialInteractionManager, win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_SourceReleased(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_InteractionDetected(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialInteractionManager, win32more.Windows.UI.Input.Spatial.SpatialInteractionDetectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_InteractionDetected(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def GetDetectedSourcesAtTimestamp(self, timeStamp: win32more.Windows.Perception.PerceptionTimestamp) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceState]: ...
    SourceDetected = event()
    SourceLost = event()
    SourceUpdated = event()
    SourcePressed = event()
    SourceReleased = event()
    InteractionDetected = event()
class ISpatialInteractionManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialInteractionManagerStatics'
    _iid_ = Guid('{00e31fa6-8ca2-30bf-91fe-d9cb4a008990}')
    @winrt_commethod(6)
    def GetForCurrentView(self) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionManager: ...
class ISpatialInteractionManagerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialInteractionManagerStatics2'
    _iid_ = Guid('{93f16c52-b88a-5929-8d7c-48cb948b081c}')
    @winrt_commethod(6)
    def IsSourceKindSupported(self, kind: win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind) -> Boolean: ...
class ISpatialInteractionSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialInteractionSource'
    _iid_ = Guid('{fb5433ba-b0b3-3148-9f3b-e9f5de568f5d}')
    @winrt_commethod(6)
    def get_Id(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_Kind(self) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    Id = property(get_Id, None)
    Kind = property(get_Kind, None)
class ISpatialInteractionSource2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialInteractionSource2'
    _iid_ = Guid('{e4c5b70c-0470-4028-88c0-a0eb44d34efe}')
    @winrt_commethod(6)
    def get_IsPointingSupported(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsMenuSupported(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsGraspSupported(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Controller(self) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionController: ...
    @winrt_commethod(10)
    def TryGetStateAtTimestamp(self, timestamp: win32more.Windows.Perception.PerceptionTimestamp) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceState: ...
    Controller = property(get_Controller, None)
    IsGraspSupported = property(get_IsGraspSupported, None)
    IsMenuSupported = property(get_IsMenuSupported, None)
    IsPointingSupported = property(get_IsPointingSupported, None)
class ISpatialInteractionSource3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialInteractionSource3'
    _iid_ = Guid('{0406d9f9-9afd-44f9-85dc-700023a962e3}')
    @winrt_commethod(6)
    def get_Handedness(self) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceHandedness: ...
    Handedness = property(get_Handedness, None)
class ISpatialInteractionSource4(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialInteractionSource4'
    _iid_ = Guid('{0073bc4d-df66-5a91-a2ba-cea3e5c58a19}')
    @winrt_commethod(6)
    def TryCreateHandMeshObserver(self) -> win32more.Windows.Perception.People.HandMeshObserver: ...
    @winrt_commethod(7)
    def TryCreateHandMeshObserverAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Perception.People.HandMeshObserver]: ...
class ISpatialInteractionSourceEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialInteractionSourceEventArgs'
    _iid_ = Guid('{23b786cf-ec23-3979-b27c-eb0e12feb7c7}')
    @winrt_commethod(6)
    def get_State(self) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceState: ...
    State = property(get_State, None)
class ISpatialInteractionSourceEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialInteractionSourceEventArgs2'
    _iid_ = Guid('{d8b4b467-e648-4d52-ab49-e0d227199f63}')
    @winrt_commethod(6)
    def get_PressKind(self) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionPressKind: ...
    PressKind = property(get_PressKind, None)
class ISpatialInteractionSourceLocation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialInteractionSourceLocation'
    _iid_ = Guid('{ea4696c4-7e8b-30ca-bcc5-c77189cea30a}')
    @winrt_commethod(6)
    def get_Position(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector3]: ...
    @winrt_commethod(7)
    def get_Velocity(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector3]: ...
    Position = property(get_Position, None)
    Velocity = property(get_Velocity, None)
class ISpatialInteractionSourceLocation2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialInteractionSourceLocation2'
    _iid_ = Guid('{4c671045-3917-40fc-a9ac-31c9cf5ff91b}')
    @winrt_commethod(6)
    def get_Orientation(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Quaternion]: ...
    Orientation = property(get_Orientation, None)
class ISpatialInteractionSourceLocation3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialInteractionSourceLocation3'
    _iid_ = Guid('{6702e65e-e915-4cfb-9c1b-0538efc86687}')
    @winrt_commethod(6)
    def get_PositionAccuracy(self) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourcePositionAccuracy: ...
    @winrt_commethod(7)
    def get_AngularVelocity(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector3]: ...
    @winrt_commethod(8)
    def get_SourcePointerPose(self) -> win32more.Windows.UI.Input.Spatial.SpatialPointerInteractionSourcePose: ...
    AngularVelocity = property(get_AngularVelocity, None)
    PositionAccuracy = property(get_PositionAccuracy, None)
    SourcePointerPose = property(get_SourcePointerPose, None)
class ISpatialInteractionSourceProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialInteractionSourceProperties'
    _iid_ = Guid('{05604542-3ef7-3222-9f53-63c9cb7e3bc7}')
    @winrt_commethod(6)
    def TryGetSourceLossMitigationDirection(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector3]: ...
    @winrt_commethod(7)
    def get_SourceLossRisk(self) -> Double: ...
    @winrt_commethod(8)
    def TryGetLocation(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceLocation: ...
    SourceLossRisk = property(get_SourceLossRisk, None)
class ISpatialInteractionSourceState(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialInteractionSourceState'
    _iid_ = Guid('{d5c475ef-4b63-37ec-98b9-9fc652b9d2f2}')
    @winrt_commethod(6)
    def get_Source(self) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSource: ...
    @winrt_commethod(7)
    def get_Properties(self) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceProperties: ...
    @winrt_commethod(8)
    def get_IsPressed(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Timestamp(self) -> win32more.Windows.Perception.PerceptionTimestamp: ...
    @winrt_commethod(10)
    def TryGetPointerPose(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.UI.Input.Spatial.SpatialPointerPose: ...
    IsPressed = property(get_IsPressed, None)
    Properties = property(get_Properties, None)
    Source = property(get_Source, None)
    Timestamp = property(get_Timestamp, None)
class ISpatialInteractionSourceState2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialInteractionSourceState2'
    _iid_ = Guid('{45f6d0bd-1773-492e-9ba3-8ac1cbe77c08}')
    @winrt_commethod(6)
    def get_IsSelectPressed(self) -> Boolean: ...
    @winrt_commethod(7)
    def get_IsMenuPressed(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsGrasped(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_SelectPressedValue(self) -> Double: ...
    @winrt_commethod(10)
    def get_ControllerProperties(self) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionControllerProperties: ...
    ControllerProperties = property(get_ControllerProperties, None)
    IsGrasped = property(get_IsGrasped, None)
    IsMenuPressed = property(get_IsMenuPressed, None)
    IsSelectPressed = property(get_IsSelectPressed, None)
    SelectPressedValue = property(get_SelectPressedValue, None)
class ISpatialInteractionSourceState3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialInteractionSourceState3'
    _iid_ = Guid('{f2f00bc2-bd2b-4a01-a8fb-323e0158527c}')
    @winrt_commethod(6)
    def TryGetHandPose(self) -> win32more.Windows.Perception.People.HandPose: ...
class ISpatialManipulationCanceledEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialManipulationCanceledEventArgs'
    _iid_ = Guid('{2d40d1cb-e7da-4220-b0bf-819301674780}')
    @winrt_commethod(6)
    def get_InteractionSourceKind(self) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class ISpatialManipulationCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialManipulationCompletedEventArgs'
    _iid_ = Guid('{05086802-f301-4343-9250-2fbaa5f87a37}')
    @winrt_commethod(6)
    def get_InteractionSourceKind(self) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_commethod(7)
    def TryGetCumulativeDelta(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.UI.Input.Spatial.SpatialManipulationDelta: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class ISpatialManipulationDelta(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialManipulationDelta'
    _iid_ = Guid('{a7ec967a-d123-3a81-a15b-992923dcbe91}')
    @winrt_commethod(6)
    def get_Translation(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    Translation = property(get_Translation, None)
class ISpatialManipulationStartedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialManipulationStartedEventArgs'
    _iid_ = Guid('{a1d6bbce-42a5-377b-ada6-d28e3d384737}')
    @winrt_commethod(6)
    def get_InteractionSourceKind(self) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_commethod(7)
    def TryGetPointerPose(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.UI.Input.Spatial.SpatialPointerPose: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class ISpatialManipulationUpdatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialManipulationUpdatedEventArgs'
    _iid_ = Guid('{5f230b9b-60c6-4dc6-bdc9-9f4a6f15fe49}')
    @winrt_commethod(6)
    def get_InteractionSourceKind(self) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_commethod(7)
    def TryGetCumulativeDelta(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.UI.Input.Spatial.SpatialManipulationDelta: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class ISpatialNavigationCanceledEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialNavigationCanceledEventArgs'
    _iid_ = Guid('{ce503edc-e8a5-46f0-92d4-3c122b35112a}')
    @winrt_commethod(6)
    def get_InteractionSourceKind(self) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class ISpatialNavigationCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialNavigationCompletedEventArgs'
    _iid_ = Guid('{012e80b7-af3b-42c2-9e41-baaa0e721f3a}')
    @winrt_commethod(6)
    def get_InteractionSourceKind(self) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_commethod(7)
    def get_NormalizedOffset(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
    NormalizedOffset = property(get_NormalizedOffset, None)
class ISpatialNavigationStartedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialNavigationStartedEventArgs'
    _iid_ = Guid('{754a348a-fb64-4656-8ebd-9deecaafe475}')
    @winrt_commethod(6)
    def get_InteractionSourceKind(self) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_commethod(7)
    def TryGetPointerPose(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.UI.Input.Spatial.SpatialPointerPose: ...
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
class ISpatialNavigationUpdatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialNavigationUpdatedEventArgs'
    _iid_ = Guid('{9b713fd7-839d-4a74-8732-45466fc044b5}')
    @winrt_commethod(6)
    def get_InteractionSourceKind(self) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_commethod(7)
    def get_NormalizedOffset(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
    NormalizedOffset = property(get_NormalizedOffset, None)
class ISpatialPointerInteractionSourcePose(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialPointerInteractionSourcePose'
    _iid_ = Guid('{a7104307-2c2b-4d3a-92a7-80ced7c4a0d0}')
    @winrt_commethod(6)
    def get_Position(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(7)
    def get_ForwardDirection(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_commethod(8)
    def get_UpDirection(self) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    ForwardDirection = property(get_ForwardDirection, None)
    Position = property(get_Position, None)
    UpDirection = property(get_UpDirection, None)
class ISpatialPointerInteractionSourcePose2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialPointerInteractionSourcePose2'
    _iid_ = Guid('{eccd86b8-52db-469f-9e3f-80c47f74bce9}')
    @winrt_commethod(6)
    def get_Orientation(self) -> win32more.Windows.Foundation.Numerics.Quaternion: ...
    @winrt_commethod(7)
    def get_PositionAccuracy(self) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourcePositionAccuracy: ...
    Orientation = property(get_Orientation, None)
    PositionAccuracy = property(get_PositionAccuracy, None)
class ISpatialPointerPose(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialPointerPose'
    _iid_ = Guid('{6953a42e-c17e-357d-97a1-7269d0ed2d10}')
    @winrt_commethod(6)
    def get_Timestamp(self) -> win32more.Windows.Perception.PerceptionTimestamp: ...
    @winrt_commethod(7)
    def get_Head(self) -> win32more.Windows.Perception.People.HeadPose: ...
    Head = property(get_Head, None)
    Timestamp = property(get_Timestamp, None)
class ISpatialPointerPose2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialPointerPose2'
    _iid_ = Guid('{9d202b17-954e-4e0c-96d1-b6790b6fc2fd}')
    @winrt_commethod(6)
    def TryGetInteractionSourcePose(self, source: win32more.Windows.UI.Input.Spatial.SpatialInteractionSource) -> win32more.Windows.UI.Input.Spatial.SpatialPointerInteractionSourcePose: ...
class ISpatialPointerPose3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialPointerPose3'
    _iid_ = Guid('{6342f3f0-ec49-5b4b-b8d1-d16cbb16be84}')
    @winrt_commethod(6)
    def get_Eyes(self) -> win32more.Windows.Perception.People.EyesPose: ...
    @winrt_commethod(7)
    def get_IsHeadCapturedBySystem(self) -> Boolean: ...
    Eyes = property(get_Eyes, None)
    IsHeadCapturedBySystem = property(get_IsHeadCapturedBySystem, None)
class ISpatialPointerPoseStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialPointerPoseStatics'
    _iid_ = Guid('{a25591a9-aca1-3ee0-9816-785cfb2e3fb8}')
    @winrt_commethod(6)
    def TryGetAtTimestamp(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, timestamp: win32more.Windows.Perception.PerceptionTimestamp) -> win32more.Windows.UI.Input.Spatial.SpatialPointerPose: ...
class ISpatialRecognitionEndedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialRecognitionEndedEventArgs'
    _iid_ = Guid('{0e35f5cb-3f75-43f3-ac81-d1dc2df9b1fb}')
    @winrt_commethod(6)
    def get_InteractionSourceKind(self) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class ISpatialRecognitionStartedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialRecognitionStartedEventArgs'
    _iid_ = Guid('{24da128f-0008-4a6d-aa50-2a76f9cfb264}')
    @winrt_commethod(6)
    def get_InteractionSourceKind(self) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_commethod(7)
    def TryGetPointerPose(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.UI.Input.Spatial.SpatialPointerPose: ...
    @winrt_commethod(8)
    def IsGesturePossible(self, gesture: win32more.Windows.UI.Input.Spatial.SpatialGestureSettings) -> Boolean: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class ISpatialTappedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Spatial.ISpatialTappedEventArgs'
    _iid_ = Guid('{296d83de-f444-4aa1-b2bf-9dc88d567da6}')
    @winrt_commethod(6)
    def get_InteractionSourceKind(self) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_commethod(7)
    def TryGetPointerPose(self, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.UI.Input.Spatial.SpatialPointerPose: ...
    @winrt_commethod(8)
    def get_TapCount(self) -> UInt32: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
    TapCount = property(get_TapCount, None)
class SpatialGestureRecognizer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer
    _classid_ = 'Windows.UI.Input.Spatial.SpatialGestureRecognizer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Input.Spatial.SpatialGestureRecognizer.Create(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def Create(cls: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizerFactory, settings: win32more.Windows.UI.Input.Spatial.SpatialGestureSettings) -> win32more.Windows.UI.Input.Spatial.SpatialGestureRecognizer: ...
    @winrt_mixinmethod
    def add_RecognitionStarted(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialGestureRecognizer, win32more.Windows.UI.Input.Spatial.SpatialRecognitionStartedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RecognitionStarted(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_RecognitionEnded(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialGestureRecognizer, win32more.Windows.UI.Input.Spatial.SpatialRecognitionEndedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RecognitionEnded(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Tapped(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialGestureRecognizer, win32more.Windows.UI.Input.Spatial.SpatialTappedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Tapped(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_HoldStarted(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialGestureRecognizer, win32more.Windows.UI.Input.Spatial.SpatialHoldStartedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HoldStarted(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_HoldCompleted(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialGestureRecognizer, win32more.Windows.UI.Input.Spatial.SpatialHoldCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HoldCompleted(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_HoldCanceled(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialGestureRecognizer, win32more.Windows.UI.Input.Spatial.SpatialHoldCanceledEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_HoldCanceled(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationStarted(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialGestureRecognizer, win32more.Windows.UI.Input.Spatial.SpatialManipulationStartedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationStarted(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationUpdated(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialGestureRecognizer, win32more.Windows.UI.Input.Spatial.SpatialManipulationUpdatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationUpdated(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationCompleted(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialGestureRecognizer, win32more.Windows.UI.Input.Spatial.SpatialManipulationCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationCompleted(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationCanceled(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialGestureRecognizer, win32more.Windows.UI.Input.Spatial.SpatialManipulationCanceledEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationCanceled(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_NavigationStarted(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialGestureRecognizer, win32more.Windows.UI.Input.Spatial.SpatialNavigationStartedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NavigationStarted(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_NavigationUpdated(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialGestureRecognizer, win32more.Windows.UI.Input.Spatial.SpatialNavigationUpdatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NavigationUpdated(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_NavigationCompleted(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialGestureRecognizer, win32more.Windows.UI.Input.Spatial.SpatialNavigationCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NavigationCompleted(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_NavigationCanceled(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialGestureRecognizer, win32more.Windows.UI.Input.Spatial.SpatialNavigationCanceledEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NavigationCanceled(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def CaptureInteraction(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer, interaction: win32more.Windows.UI.Input.Spatial.SpatialInteraction) -> Void: ...
    @winrt_mixinmethod
    def CancelPendingGestures(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer) -> Void: ...
    @winrt_mixinmethod
    def TrySetGestureSettings(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer, settings: win32more.Windows.UI.Input.Spatial.SpatialGestureSettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_GestureSettings(self: win32more.Windows.UI.Input.Spatial.ISpatialGestureRecognizer) -> win32more.Windows.UI.Input.Spatial.SpatialGestureSettings: ...
    GestureSettings = property(get_GestureSettings, None)
    RecognitionStarted = event()
    RecognitionEnded = event()
    Tapped = event()
    HoldStarted = event()
    HoldCompleted = event()
    HoldCanceled = event()
    ManipulationStarted = event()
    ManipulationUpdated = event()
    ManipulationCompleted = event()
    ManipulationCanceled = event()
    NavigationStarted = event()
    NavigationUpdated = event()
    NavigationCompleted = event()
    NavigationCanceled = event()
class SpatialGestureSettings(Enum, UInt32):
    None_ = 0
    Tap = 1
    DoubleTap = 2
    Hold = 4
    ManipulationTranslate = 8
    NavigationX = 16
    NavigationY = 32
    NavigationZ = 64
    NavigationRailsX = 128
    NavigationRailsY = 256
    NavigationRailsZ = 512
class SpatialHoldCanceledEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Spatial.ISpatialHoldCanceledEventArgs
    _classid_ = 'Windows.UI.Input.Spatial.SpatialHoldCanceledEventArgs'
    @winrt_mixinmethod
    def get_InteractionSourceKind(self: win32more.Windows.UI.Input.Spatial.ISpatialHoldCanceledEventArgs) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class SpatialHoldCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Spatial.ISpatialHoldCompletedEventArgs
    _classid_ = 'Windows.UI.Input.Spatial.SpatialHoldCompletedEventArgs'
    @winrt_mixinmethod
    def get_InteractionSourceKind(self: win32more.Windows.UI.Input.Spatial.ISpatialHoldCompletedEventArgs) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class SpatialHoldStartedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Spatial.ISpatialHoldStartedEventArgs
    _classid_ = 'Windows.UI.Input.Spatial.SpatialHoldStartedEventArgs'
    @winrt_mixinmethod
    def get_InteractionSourceKind(self: win32more.Windows.UI.Input.Spatial.ISpatialHoldStartedEventArgs) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_mixinmethod
    def TryGetPointerPose(self: win32more.Windows.UI.Input.Spatial.ISpatialHoldStartedEventArgs, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.UI.Input.Spatial.SpatialPointerPose: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class SpatialInteraction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Spatial.ISpatialInteraction
    _classid_ = 'Windows.UI.Input.Spatial.SpatialInteraction'
    @winrt_mixinmethod
    def get_SourceState(self: win32more.Windows.UI.Input.Spatial.ISpatialInteraction) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceState: ...
    SourceState = property(get_SourceState, None)
class SpatialInteractionController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Spatial.ISpatialInteractionController
    _classid_ = 'Windows.UI.Input.Spatial.SpatialInteractionController'
    @winrt_mixinmethod
    def get_HasTouchpad(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionController) -> Boolean: ...
    @winrt_mixinmethod
    def get_HasThumbstick(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionController) -> Boolean: ...
    @winrt_mixinmethod
    def get_SimpleHapticsController(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionController) -> win32more.Windows.Devices.Haptics.SimpleHapticsController: ...
    @winrt_mixinmethod
    def get_VendorId(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionController) -> UInt16: ...
    @winrt_mixinmethod
    def get_ProductId(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionController) -> UInt16: ...
    @winrt_mixinmethod
    def get_Version(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionController) -> UInt16: ...
    @winrt_mixinmethod
    def TryGetRenderableModelAsync(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionController2) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.Streams.IRandomAccessStreamWithContentType]: ...
    @winrt_mixinmethod
    def TryGetBatteryReport(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionController3) -> win32more.Windows.Devices.Power.BatteryReport: ...
    HasThumbstick = property(get_HasThumbstick, None)
    HasTouchpad = property(get_HasTouchpad, None)
    ProductId = property(get_ProductId, None)
    SimpleHapticsController = property(get_SimpleHapticsController, None)
    VendorId = property(get_VendorId, None)
    Version = property(get_Version, None)
class SpatialInteractionControllerProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Spatial.ISpatialInteractionControllerProperties
    _classid_ = 'Windows.UI.Input.Spatial.SpatialInteractionControllerProperties'
    @winrt_mixinmethod
    def get_IsTouchpadTouched(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionControllerProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsTouchpadPressed(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionControllerProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsThumbstickPressed(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionControllerProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_ThumbstickX(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionControllerProperties) -> Double: ...
    @winrt_mixinmethod
    def get_ThumbstickY(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionControllerProperties) -> Double: ...
    @winrt_mixinmethod
    def get_TouchpadX(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionControllerProperties) -> Double: ...
    @winrt_mixinmethod
    def get_TouchpadY(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionControllerProperties) -> Double: ...
    IsThumbstickPressed = property(get_IsThumbstickPressed, None)
    IsTouchpadPressed = property(get_IsTouchpadPressed, None)
    IsTouchpadTouched = property(get_IsTouchpadTouched, None)
    ThumbstickX = property(get_ThumbstickX, None)
    ThumbstickY = property(get_ThumbstickY, None)
    TouchpadX = property(get_TouchpadX, None)
    TouchpadY = property(get_TouchpadY, None)
class SpatialInteractionDetectedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Spatial.ISpatialInteractionDetectedEventArgs
    _classid_ = 'Windows.UI.Input.Spatial.SpatialInteractionDetectedEventArgs'
    @winrt_mixinmethod
    def get_InteractionSourceKind(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionDetectedEventArgs) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_mixinmethod
    def TryGetPointerPose(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionDetectedEventArgs, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.UI.Input.Spatial.SpatialPointerPose: ...
    @winrt_mixinmethod
    def get_Interaction(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionDetectedEventArgs) -> win32more.Windows.UI.Input.Spatial.SpatialInteraction: ...
    @winrt_mixinmethod
    def get_InteractionSource(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionDetectedEventArgs2) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSource: ...
    Interaction = property(get_Interaction, None)
    InteractionSource = property(get_InteractionSource, None)
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class SpatialInteractionManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Spatial.ISpatialInteractionManager
    _classid_ = 'Windows.UI.Input.Spatial.SpatialInteractionManager'
    @winrt_mixinmethod
    def add_SourceDetected(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialInteractionManager, win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceDetected(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SourceLost(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialInteractionManager, win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceLost(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SourceUpdated(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialInteractionManager, win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceUpdated(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SourcePressed(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialInteractionManager, win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourcePressed(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SourceReleased(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialInteractionManager, win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SourceReleased(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_InteractionDetected(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionManager, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Input.Spatial.SpatialInteractionManager, win32more.Windows.UI.Input.Spatial.SpatialInteractionDetectedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_InteractionDetected(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionManager, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetDetectedSourcesAtTimestamp(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionManager, timeStamp: win32more.Windows.Perception.PerceptionTimestamp) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceState]: ...
    @winrt_classmethod
    def IsSourceKindSupported(cls: win32more.Windows.UI.Input.Spatial.ISpatialInteractionManagerStatics2, kind: win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind) -> Boolean: ...
    @winrt_classmethod
    def GetForCurrentView(cls: win32more.Windows.UI.Input.Spatial.ISpatialInteractionManagerStatics) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionManager: ...
    SourceDetected = event()
    SourceLost = event()
    SourceUpdated = event()
    SourcePressed = event()
    SourceReleased = event()
    InteractionDetected = event()
class SpatialInteractionPressKind(Enum, Int32):
    None_ = 0
    Select = 1
    Menu = 2
    Grasp = 3
    Touchpad = 4
    Thumbstick = 5
class SpatialInteractionSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSource
    _classid_ = 'Windows.UI.Input.Spatial.SpatialInteractionSource'
    @winrt_mixinmethod
    def get_Id(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSource) -> UInt32: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSource) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_mixinmethod
    def get_IsPointingSupported(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSource2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsMenuSupported(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSource2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsGraspSupported(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSource2) -> Boolean: ...
    @winrt_mixinmethod
    def get_Controller(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSource2) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionController: ...
    @winrt_mixinmethod
    def TryGetStateAtTimestamp(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSource2, timestamp: win32more.Windows.Perception.PerceptionTimestamp) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceState: ...
    @winrt_mixinmethod
    def get_Handedness(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSource3) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceHandedness: ...
    @winrt_mixinmethod
    def TryCreateHandMeshObserver(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSource4) -> win32more.Windows.Perception.People.HandMeshObserver: ...
    @winrt_mixinmethod
    def TryCreateHandMeshObserverAsync(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSource4) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Perception.People.HandMeshObserver]: ...
    Controller = property(get_Controller, None)
    Handedness = property(get_Handedness, None)
    Id = property(get_Id, None)
    IsGraspSupported = property(get_IsGraspSupported, None)
    IsMenuSupported = property(get_IsMenuSupported, None)
    IsPointingSupported = property(get_IsPointingSupported, None)
    Kind = property(get_Kind, None)
class SpatialInteractionSourceEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSourceEventArgs
    _classid_ = 'Windows.UI.Input.Spatial.SpatialInteractionSourceEventArgs'
    @winrt_mixinmethod
    def get_State(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSourceEventArgs) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceState: ...
    @winrt_mixinmethod
    def get_PressKind(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSourceEventArgs2) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionPressKind: ...
    PressKind = property(get_PressKind, None)
    State = property(get_State, None)
class SpatialInteractionSourceHandedness(Enum, Int32):
    Unspecified = 0
    Left = 1
    Right = 2
class SpatialInteractionSourceKind(Enum, Int32):
    Other = 0
    Hand = 1
    Voice = 2
    Controller = 3
class SpatialInteractionSourceLocation(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSourceLocation
    _classid_ = 'Windows.UI.Input.Spatial.SpatialInteractionSourceLocation'
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSourceLocation) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector3]: ...
    @winrt_mixinmethod
    def get_Velocity(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSourceLocation) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector3]: ...
    @winrt_mixinmethod
    def get_Orientation(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSourceLocation2) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Quaternion]: ...
    @winrt_mixinmethod
    def get_PositionAccuracy(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSourceLocation3) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourcePositionAccuracy: ...
    @winrt_mixinmethod
    def get_AngularVelocity(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSourceLocation3) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector3]: ...
    @winrt_mixinmethod
    def get_SourcePointerPose(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSourceLocation3) -> win32more.Windows.UI.Input.Spatial.SpatialPointerInteractionSourcePose: ...
    AngularVelocity = property(get_AngularVelocity, None)
    Orientation = property(get_Orientation, None)
    Position = property(get_Position, None)
    PositionAccuracy = property(get_PositionAccuracy, None)
    SourcePointerPose = property(get_SourcePointerPose, None)
    Velocity = property(get_Velocity, None)
class SpatialInteractionSourcePositionAccuracy(Enum, Int32):
    High = 0
    Approximate = 1
class SpatialInteractionSourceProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSourceProperties
    _classid_ = 'Windows.UI.Input.Spatial.SpatialInteractionSourceProperties'
    @winrt_mixinmethod
    def TryGetSourceLossMitigationDirection(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSourceProperties, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Numerics.Vector3]: ...
    @winrt_mixinmethod
    def get_SourceLossRisk(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSourceProperties) -> Double: ...
    @winrt_mixinmethod
    def TryGetLocation(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSourceProperties, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceLocation: ...
    SourceLossRisk = property(get_SourceLossRisk, None)
class SpatialInteractionSourceState(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSourceState
    _classid_ = 'Windows.UI.Input.Spatial.SpatialInteractionSourceState'
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSourceState) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSource: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSourceState) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceProperties: ...
    @winrt_mixinmethod
    def get_IsPressed(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSourceState) -> Boolean: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSourceState) -> win32more.Windows.Perception.PerceptionTimestamp: ...
    @winrt_mixinmethod
    def TryGetPointerPose(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSourceState, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.UI.Input.Spatial.SpatialPointerPose: ...
    @winrt_mixinmethod
    def get_IsSelectPressed(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSourceState2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsMenuPressed(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSourceState2) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsGrasped(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSourceState2) -> Boolean: ...
    @winrt_mixinmethod
    def get_SelectPressedValue(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSourceState2) -> Double: ...
    @winrt_mixinmethod
    def get_ControllerProperties(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSourceState2) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionControllerProperties: ...
    @winrt_mixinmethod
    def TryGetHandPose(self: win32more.Windows.UI.Input.Spatial.ISpatialInteractionSourceState3) -> win32more.Windows.Perception.People.HandPose: ...
    ControllerProperties = property(get_ControllerProperties, None)
    IsGrasped = property(get_IsGrasped, None)
    IsMenuPressed = property(get_IsMenuPressed, None)
    IsPressed = property(get_IsPressed, None)
    IsSelectPressed = property(get_IsSelectPressed, None)
    Properties = property(get_Properties, None)
    SelectPressedValue = property(get_SelectPressedValue, None)
    Source = property(get_Source, None)
    Timestamp = property(get_Timestamp, None)
class SpatialManipulationCanceledEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Spatial.ISpatialManipulationCanceledEventArgs
    _classid_ = 'Windows.UI.Input.Spatial.SpatialManipulationCanceledEventArgs'
    @winrt_mixinmethod
    def get_InteractionSourceKind(self: win32more.Windows.UI.Input.Spatial.ISpatialManipulationCanceledEventArgs) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class SpatialManipulationCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Spatial.ISpatialManipulationCompletedEventArgs
    _classid_ = 'Windows.UI.Input.Spatial.SpatialManipulationCompletedEventArgs'
    @winrt_mixinmethod
    def get_InteractionSourceKind(self: win32more.Windows.UI.Input.Spatial.ISpatialManipulationCompletedEventArgs) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_mixinmethod
    def TryGetCumulativeDelta(self: win32more.Windows.UI.Input.Spatial.ISpatialManipulationCompletedEventArgs, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.UI.Input.Spatial.SpatialManipulationDelta: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class SpatialManipulationDelta(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Spatial.ISpatialManipulationDelta
    _classid_ = 'Windows.UI.Input.Spatial.SpatialManipulationDelta'
    @winrt_mixinmethod
    def get_Translation(self: win32more.Windows.UI.Input.Spatial.ISpatialManipulationDelta) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    Translation = property(get_Translation, None)
class SpatialManipulationStartedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Spatial.ISpatialManipulationStartedEventArgs
    _classid_ = 'Windows.UI.Input.Spatial.SpatialManipulationStartedEventArgs'
    @winrt_mixinmethod
    def get_InteractionSourceKind(self: win32more.Windows.UI.Input.Spatial.ISpatialManipulationStartedEventArgs) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_mixinmethod
    def TryGetPointerPose(self: win32more.Windows.UI.Input.Spatial.ISpatialManipulationStartedEventArgs, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.UI.Input.Spatial.SpatialPointerPose: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class SpatialManipulationUpdatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Spatial.ISpatialManipulationUpdatedEventArgs
    _classid_ = 'Windows.UI.Input.Spatial.SpatialManipulationUpdatedEventArgs'
    @winrt_mixinmethod
    def get_InteractionSourceKind(self: win32more.Windows.UI.Input.Spatial.ISpatialManipulationUpdatedEventArgs) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_mixinmethod
    def TryGetCumulativeDelta(self: win32more.Windows.UI.Input.Spatial.ISpatialManipulationUpdatedEventArgs, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.UI.Input.Spatial.SpatialManipulationDelta: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class SpatialNavigationCanceledEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Spatial.ISpatialNavigationCanceledEventArgs
    _classid_ = 'Windows.UI.Input.Spatial.SpatialNavigationCanceledEventArgs'
    @winrt_mixinmethod
    def get_InteractionSourceKind(self: win32more.Windows.UI.Input.Spatial.ISpatialNavigationCanceledEventArgs) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class SpatialNavigationCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Spatial.ISpatialNavigationCompletedEventArgs
    _classid_ = 'Windows.UI.Input.Spatial.SpatialNavigationCompletedEventArgs'
    @winrt_mixinmethod
    def get_InteractionSourceKind(self: win32more.Windows.UI.Input.Spatial.ISpatialNavigationCompletedEventArgs) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_mixinmethod
    def get_NormalizedOffset(self: win32more.Windows.UI.Input.Spatial.ISpatialNavigationCompletedEventArgs) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
    NormalizedOffset = property(get_NormalizedOffset, None)
class SpatialNavigationStartedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Spatial.ISpatialNavigationStartedEventArgs
    _classid_ = 'Windows.UI.Input.Spatial.SpatialNavigationStartedEventArgs'
    @winrt_mixinmethod
    def get_InteractionSourceKind(self: win32more.Windows.UI.Input.Spatial.ISpatialNavigationStartedEventArgs) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_mixinmethod
    def TryGetPointerPose(self: win32more.Windows.UI.Input.Spatial.ISpatialNavigationStartedEventArgs, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.UI.Input.Spatial.SpatialPointerPose: ...
    @winrt_mixinmethod
    def get_IsNavigatingX(self: win32more.Windows.UI.Input.Spatial.ISpatialNavigationStartedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsNavigatingY(self: win32more.Windows.UI.Input.Spatial.ISpatialNavigationStartedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsNavigatingZ(self: win32more.Windows.UI.Input.Spatial.ISpatialNavigationStartedEventArgs) -> Boolean: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
    IsNavigatingX = property(get_IsNavigatingX, None)
    IsNavigatingY = property(get_IsNavigatingY, None)
    IsNavigatingZ = property(get_IsNavigatingZ, None)
class SpatialNavigationUpdatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Spatial.ISpatialNavigationUpdatedEventArgs
    _classid_ = 'Windows.UI.Input.Spatial.SpatialNavigationUpdatedEventArgs'
    @winrt_mixinmethod
    def get_InteractionSourceKind(self: win32more.Windows.UI.Input.Spatial.ISpatialNavigationUpdatedEventArgs) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_mixinmethod
    def get_NormalizedOffset(self: win32more.Windows.UI.Input.Spatial.ISpatialNavigationUpdatedEventArgs) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
    NormalizedOffset = property(get_NormalizedOffset, None)
class SpatialPointerInteractionSourcePose(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Spatial.ISpatialPointerInteractionSourcePose
    _classid_ = 'Windows.UI.Input.Spatial.SpatialPointerInteractionSourcePose'
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.UI.Input.Spatial.ISpatialPointerInteractionSourcePose) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_ForwardDirection(self: win32more.Windows.UI.Input.Spatial.ISpatialPointerInteractionSourcePose) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_UpDirection(self: win32more.Windows.UI.Input.Spatial.ISpatialPointerInteractionSourcePose) -> win32more.Windows.Foundation.Numerics.Vector3: ...
    @winrt_mixinmethod
    def get_Orientation(self: win32more.Windows.UI.Input.Spatial.ISpatialPointerInteractionSourcePose2) -> win32more.Windows.Foundation.Numerics.Quaternion: ...
    @winrt_mixinmethod
    def get_PositionAccuracy(self: win32more.Windows.UI.Input.Spatial.ISpatialPointerInteractionSourcePose2) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourcePositionAccuracy: ...
    ForwardDirection = property(get_ForwardDirection, None)
    Orientation = property(get_Orientation, None)
    Position = property(get_Position, None)
    PositionAccuracy = property(get_PositionAccuracy, None)
    UpDirection = property(get_UpDirection, None)
class SpatialPointerPose(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Spatial.ISpatialPointerPose
    _classid_ = 'Windows.UI.Input.Spatial.SpatialPointerPose'
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.UI.Input.Spatial.ISpatialPointerPose) -> win32more.Windows.Perception.PerceptionTimestamp: ...
    @winrt_mixinmethod
    def get_Head(self: win32more.Windows.UI.Input.Spatial.ISpatialPointerPose) -> win32more.Windows.Perception.People.HeadPose: ...
    @winrt_mixinmethod
    def TryGetInteractionSourcePose(self: win32more.Windows.UI.Input.Spatial.ISpatialPointerPose2, source: win32more.Windows.UI.Input.Spatial.SpatialInteractionSource) -> win32more.Windows.UI.Input.Spatial.SpatialPointerInteractionSourcePose: ...
    @winrt_mixinmethod
    def get_Eyes(self: win32more.Windows.UI.Input.Spatial.ISpatialPointerPose3) -> win32more.Windows.Perception.People.EyesPose: ...
    @winrt_mixinmethod
    def get_IsHeadCapturedBySystem(self: win32more.Windows.UI.Input.Spatial.ISpatialPointerPose3) -> Boolean: ...
    @winrt_classmethod
    def TryGetAtTimestamp(cls: win32more.Windows.UI.Input.Spatial.ISpatialPointerPoseStatics, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem, timestamp: win32more.Windows.Perception.PerceptionTimestamp) -> win32more.Windows.UI.Input.Spatial.SpatialPointerPose: ...
    Eyes = property(get_Eyes, None)
    Head = property(get_Head, None)
    IsHeadCapturedBySystem = property(get_IsHeadCapturedBySystem, None)
    Timestamp = property(get_Timestamp, None)
class SpatialRecognitionEndedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Spatial.ISpatialRecognitionEndedEventArgs
    _classid_ = 'Windows.UI.Input.Spatial.SpatialRecognitionEndedEventArgs'
    @winrt_mixinmethod
    def get_InteractionSourceKind(self: win32more.Windows.UI.Input.Spatial.ISpatialRecognitionEndedEventArgs) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class SpatialRecognitionStartedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Spatial.ISpatialRecognitionStartedEventArgs
    _classid_ = 'Windows.UI.Input.Spatial.SpatialRecognitionStartedEventArgs'
    @winrt_mixinmethod
    def get_InteractionSourceKind(self: win32more.Windows.UI.Input.Spatial.ISpatialRecognitionStartedEventArgs) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_mixinmethod
    def TryGetPointerPose(self: win32more.Windows.UI.Input.Spatial.ISpatialRecognitionStartedEventArgs, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.UI.Input.Spatial.SpatialPointerPose: ...
    @winrt_mixinmethod
    def IsGesturePossible(self: win32more.Windows.UI.Input.Spatial.ISpatialRecognitionStartedEventArgs, gesture: win32more.Windows.UI.Input.Spatial.SpatialGestureSettings) -> Boolean: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
class SpatialTappedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Input.Spatial.ISpatialTappedEventArgs
    _classid_ = 'Windows.UI.Input.Spatial.SpatialTappedEventArgs'
    @winrt_mixinmethod
    def get_InteractionSourceKind(self: win32more.Windows.UI.Input.Spatial.ISpatialTappedEventArgs) -> win32more.Windows.UI.Input.Spatial.SpatialInteractionSourceKind: ...
    @winrt_mixinmethod
    def TryGetPointerPose(self: win32more.Windows.UI.Input.Spatial.ISpatialTappedEventArgs, coordinateSystem: win32more.Windows.Perception.Spatial.SpatialCoordinateSystem) -> win32more.Windows.UI.Input.Spatial.SpatialPointerPose: ...
    @winrt_mixinmethod
    def get_TapCount(self: win32more.Windows.UI.Input.Spatial.ISpatialTappedEventArgs) -> UInt32: ...
    InteractionSourceKind = property(get_InteractionSourceKind, None)
    TapCount = property(get_TapCount, None)


make_ready(__name__)
