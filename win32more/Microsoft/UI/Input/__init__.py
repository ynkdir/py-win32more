from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.UI
import win32more.Microsoft.UI.Content
import win32more.Microsoft.UI.Dispatching
import win32more.Microsoft.UI.Input
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Graphics
import win32more.Windows.System
import win32more.Windows.UI.Core
import win32more.Windows.Win32.System.WinRT
class CharacterReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.ICharacterReceivedEventArgs
    _classid_ = 'Microsoft.UI.Input.CharacterReceivedEventArgs'
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.UI.Input.ICharacterReceivedEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.UI.Input.ICharacterReceivedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_KeyCode(self: win32more.Microsoft.UI.Input.ICharacterReceivedEventArgs) -> UInt32: ...
    @winrt_mixinmethod
    def get_KeyStatus(self: win32more.Microsoft.UI.Input.ICharacterReceivedEventArgs) -> win32more.Microsoft.UI.Input.PhysicalKeyStatus: ...
    Handled = property(get_Handled, put_Handled)
    KeyCode = property(get_KeyCode, None)
    KeyStatus = property(get_KeyStatus, None)
class ContextMenuKeyEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.IContextMenuKeyEventArgs
    _classid_ = 'Microsoft.UI.Input.ContextMenuKeyEventArgs'
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.UI.Input.IContextMenuKeyEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.UI.Input.IContextMenuKeyEventArgs, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
class CrossSlideThresholds(Structure):
    SelectionStart: Single
    SpeedBumpStart: Single
    SpeedBumpEnd: Single
    RearrangeStart: Single
class CrossSlidingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.ICrossSlidingEventArgs
    _classid_ = 'Microsoft.UI.Input.CrossSlidingEventArgs'
    @winrt_mixinmethod
    def get_CrossSlidingState(self: win32more.Microsoft.UI.Input.ICrossSlidingEventArgs) -> win32more.Microsoft.UI.Input.CrossSlidingState: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Microsoft.UI.Input.ICrossSlidingEventArgs) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Microsoft.UI.Input.ICrossSlidingEventArgs) -> win32more.Windows.Foundation.Point: ...
    CrossSlidingState = property(get_CrossSlidingState, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
class CrossSlidingState(Enum, Int32):
    Started = 0
    Dragging = 1
    Selecting = 2
    SelectSpeedBumping = 3
    SpeedBumping = 4
    Rearranging = 5
    Completed = 6
class DraggingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.IDraggingEventArgs
    _classid_ = 'Microsoft.UI.Input.DraggingEventArgs'
    @winrt_mixinmethod
    def get_DraggingState(self: win32more.Microsoft.UI.Input.IDraggingEventArgs) -> win32more.Microsoft.UI.Input.DraggingState: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Microsoft.UI.Input.IDraggingEventArgs) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Microsoft.UI.Input.IDraggingEventArgs) -> win32more.Windows.Foundation.Point: ...
    DraggingState = property(get_DraggingState, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
class DraggingState(Enum, Int32):
    Started = 0
    Continuing = 1
    Completed = 2
class EnteredMoveSizeEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.IEnteredMoveSizeEventArgs
    _classid_ = 'Microsoft.UI.Input.EnteredMoveSizeEventArgs'
    @winrt_mixinmethod
    def get_PointerScreenPoint(self: win32more.Microsoft.UI.Input.IEnteredMoveSizeEventArgs) -> win32more.Windows.Graphics.PointInt32: ...
    @winrt_mixinmethod
    def get_MoveSizeOperation(self: win32more.Microsoft.UI.Input.IEnteredMoveSizeEventArgs) -> win32more.Microsoft.UI.Input.MoveSizeOperation: ...
    MoveSizeOperation = property(get_MoveSizeOperation, None)
    PointerScreenPoint = property(get_PointerScreenPoint, None)
class EnteringMoveSizeEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.IEnteringMoveSizeEventArgs
    _classid_ = 'Microsoft.UI.Input.EnteringMoveSizeEventArgs'
    @winrt_mixinmethod
    def get_MoveSizeWindowId(self: win32more.Microsoft.UI.Input.IEnteringMoveSizeEventArgs) -> win32more.Microsoft.UI.WindowId: ...
    @winrt_mixinmethod
    def get_MoveSizeOperation(self: win32more.Microsoft.UI.Input.IEnteringMoveSizeEventArgs) -> win32more.Microsoft.UI.Input.MoveSizeOperation: ...
    @winrt_mixinmethod
    def get_PointerScreenPoint(self: win32more.Microsoft.UI.Input.IEnteringMoveSizeEventArgs) -> win32more.Windows.Graphics.PointInt32: ...
    @winrt_mixinmethod
    def put_MoveSizeWindowId(self: win32more.Microsoft.UI.Input.IEnteringMoveSizeEventArgs, value: win32more.Microsoft.UI.WindowId) -> Void: ...
    MoveSizeOperation = property(get_MoveSizeOperation, None)
    MoveSizeWindowId = property(get_MoveSizeWindowId, put_MoveSizeWindowId)
    PointerScreenPoint = property(get_PointerScreenPoint, None)
class ExitedMoveSizeEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.IExitedMoveSizeEventArgs
    _classid_ = 'Microsoft.UI.Input.ExitedMoveSizeEventArgs'
    @winrt_mixinmethod
    def get_PointerScreenPoint(self: win32more.Microsoft.UI.Input.IExitedMoveSizeEventArgs) -> win32more.Windows.Graphics.PointInt32: ...
    @winrt_mixinmethod
    def get_MoveSizeOperation(self: win32more.Microsoft.UI.Input.IExitedMoveSizeEventArgs) -> win32more.Microsoft.UI.Input.MoveSizeOperation: ...
    MoveSizeOperation = property(get_MoveSizeOperation, None)
    PointerScreenPoint = property(get_PointerScreenPoint, None)
class FocusChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.IFocusChangedEventArgs
    _classid_ = 'Microsoft.UI.Input.FocusChangedEventArgs'
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.UI.Input.IFocusChangedEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.UI.Input.IFocusChangedEventArgs, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
class FocusNavigationReason(Enum, Int32):
    Programmatic = 0
    Restore = 1
    First = 2
    Last = 3
    Left = 4
    Up = 5
    Right = 6
    Down = 7
class FocusNavigationRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.IFocusNavigationRequest
    _classid_ = 'Microsoft.UI.Input.FocusNavigationRequest'
    @winrt_mixinmethod
    def get_Reason(self: win32more.Microsoft.UI.Input.IFocusNavigationRequest) -> win32more.Microsoft.UI.Input.FocusNavigationReason: ...
    @winrt_mixinmethod
    def get_HintRect(self: win32more.Microsoft.UI.Input.IFocusNavigationRequest) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]: ...
    @winrt_mixinmethod
    def get_CorrelationId(self: win32more.Microsoft.UI.Input.IFocusNavigationRequest) -> Guid: ...
    @winrt_classmethod
    def Create(cls: win32more.Microsoft.UI.Input.IFocusNavigationRequestStatics, reason: win32more.Microsoft.UI.Input.FocusNavigationReason) -> win32more.Microsoft.UI.Input.FocusNavigationRequest: ...
    @winrt_classmethod
    def CreateWithHintRect(cls: win32more.Microsoft.UI.Input.IFocusNavigationRequestStatics, reason: win32more.Microsoft.UI.Input.FocusNavigationReason, hintRect: win32more.Windows.Foundation.Rect) -> win32more.Microsoft.UI.Input.FocusNavigationRequest: ...
    @winrt_classmethod
    def CreateWithHintRectAndId(cls: win32more.Microsoft.UI.Input.IFocusNavigationRequestStatics, reason: win32more.Microsoft.UI.Input.FocusNavigationReason, hintRect: win32more.Windows.Foundation.Rect, correlationId: Guid) -> win32more.Microsoft.UI.Input.FocusNavigationRequest: ...
    CorrelationId = property(get_CorrelationId, None)
    HintRect = property(get_HintRect, None)
    Reason = property(get_Reason, None)
class FocusNavigationRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.IFocusNavigationRequestEventArgs
    _classid_ = 'Microsoft.UI.Input.FocusNavigationRequestEventArgs'
    @winrt_mixinmethod
    def get_Request(self: win32more.Microsoft.UI.Input.IFocusNavigationRequestEventArgs) -> win32more.Microsoft.UI.Input.FocusNavigationRequest: ...
    @winrt_mixinmethod
    def get_Result(self: win32more.Microsoft.UI.Input.IFocusNavigationRequestEventArgs) -> win32more.Microsoft.UI.Input.FocusNavigationResult: ...
    @winrt_mixinmethod
    def put_Result(self: win32more.Microsoft.UI.Input.IFocusNavigationRequestEventArgs, value: win32more.Microsoft.UI.Input.FocusNavigationResult) -> Void: ...
    Request = property(get_Request, None)
    Result = property(get_Result, put_Result)
class FocusNavigationResult(Enum, Int32):
    NotMoved = 0
    Moved = 1
    NoFocusableElements = 2
class GestureRecognizer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.IGestureRecognizer
    _classid_ = 'Microsoft.UI.Input.GestureRecognizer'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Input.GestureRecognizer.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Input.GestureRecognizer: ...
    @winrt_mixinmethod
    def get_CrossSlideHorizontally(self: win32more.Microsoft.UI.Input.IGestureRecognizer) -> Boolean: ...
    @winrt_mixinmethod
    def put_AutoProcessInertia(self: win32more.Microsoft.UI.Input.IGestureRecognizer, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CrossSlideExact(self: win32more.Microsoft.UI.Input.IGestureRecognizer) -> Boolean: ...
    @winrt_mixinmethod
    def put_CrossSlideExact(self: win32more.Microsoft.UI.Input.IGestureRecognizer, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_InertiaTranslationDeceleration(self: win32more.Microsoft.UI.Input.IGestureRecognizer) -> Single: ...
    @winrt_mixinmethod
    def put_CrossSlideHorizontally(self: win32more.Microsoft.UI.Input.IGestureRecognizer, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_CrossSlideThresholds(self: win32more.Microsoft.UI.Input.IGestureRecognizer) -> win32more.Microsoft.UI.Input.CrossSlideThresholds: ...
    @winrt_mixinmethod
    def put_CrossSlideThresholds(self: win32more.Microsoft.UI.Input.IGestureRecognizer, value: win32more.Microsoft.UI.Input.CrossSlideThresholds) -> Void: ...
    @winrt_mixinmethod
    def get_GestureSettings(self: win32more.Microsoft.UI.Input.IGestureRecognizer) -> win32more.Microsoft.UI.Input.GestureSettings: ...
    @winrt_mixinmethod
    def put_GestureSettings(self: win32more.Microsoft.UI.Input.IGestureRecognizer, value: win32more.Microsoft.UI.Input.GestureSettings) -> Void: ...
    @winrt_mixinmethod
    def get_IsActive(self: win32more.Microsoft.UI.Input.IGestureRecognizer) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsInertial(self: win32more.Microsoft.UI.Input.IGestureRecognizer) -> Boolean: ...
    @winrt_mixinmethod
    def get_PivotCenter(self: win32more.Microsoft.UI.Input.IGestureRecognizer) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_PivotCenter(self: win32more.Microsoft.UI.Input.IGestureRecognizer, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_PivotRadius(self: win32more.Microsoft.UI.Input.IGestureRecognizer) -> Single: ...
    @winrt_mixinmethod
    def put_PivotRadius(self: win32more.Microsoft.UI.Input.IGestureRecognizer, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_InertiaExpansionDeceleration(self: win32more.Microsoft.UI.Input.IGestureRecognizer) -> Single: ...
    @winrt_mixinmethod
    def put_InertiaExpansionDeceleration(self: win32more.Microsoft.UI.Input.IGestureRecognizer, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_InertiaExpansion(self: win32more.Microsoft.UI.Input.IGestureRecognizer) -> Single: ...
    @winrt_mixinmethod
    def put_InertiaExpansion(self: win32more.Microsoft.UI.Input.IGestureRecognizer, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_InertiaRotationAngle(self: win32more.Microsoft.UI.Input.IGestureRecognizer) -> Single: ...
    @winrt_mixinmethod
    def put_InertiaRotationAngle(self: win32more.Microsoft.UI.Input.IGestureRecognizer, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_InertiaRotationDeceleration(self: win32more.Microsoft.UI.Input.IGestureRecognizer) -> Single: ...
    @winrt_mixinmethod
    def put_InertiaRotationDeceleration(self: win32more.Microsoft.UI.Input.IGestureRecognizer, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_AutoProcessInertia(self: win32more.Microsoft.UI.Input.IGestureRecognizer) -> Boolean: ...
    @winrt_mixinmethod
    def put_InertiaTranslationDeceleration(self: win32more.Microsoft.UI.Input.IGestureRecognizer, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_InertiaTranslationDisplacement(self: win32more.Microsoft.UI.Input.IGestureRecognizer) -> Single: ...
    @winrt_mixinmethod
    def put_InertiaTranslationDisplacement(self: win32more.Microsoft.UI.Input.IGestureRecognizer, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_ManipulationExact(self: win32more.Microsoft.UI.Input.IGestureRecognizer) -> Boolean: ...
    @winrt_mixinmethod
    def put_ManipulationExact(self: win32more.Microsoft.UI.Input.IGestureRecognizer, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_MouseWheelParameters(self: win32more.Microsoft.UI.Input.IGestureRecognizer) -> win32more.Microsoft.UI.Input.MouseWheelParameters: ...
    @winrt_mixinmethod
    def get_ShowGestureFeedback(self: win32more.Microsoft.UI.Input.IGestureRecognizer) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShowGestureFeedback(self: win32more.Microsoft.UI.Input.IGestureRecognizer, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def CanBeDoubleTap(self: win32more.Microsoft.UI.Input.IGestureRecognizer, value: win32more.Microsoft.UI.Input.PointerPoint) -> Boolean: ...
    @winrt_mixinmethod
    def CompleteGesture(self: win32more.Microsoft.UI.Input.IGestureRecognizer) -> Void: ...
    @winrt_mixinmethod
    def ProcessDownEvent(self: win32more.Microsoft.UI.Input.IGestureRecognizer, value: win32more.Microsoft.UI.Input.PointerPoint) -> Void: ...
    @winrt_mixinmethod
    def ProcessMoveEvents(self: win32more.Microsoft.UI.Input.IGestureRecognizer, value: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Input.PointerPoint]) -> Void: ...
    @winrt_mixinmethod
    def ProcessMouseWheelEvent(self: win32more.Microsoft.UI.Input.IGestureRecognizer, value: win32more.Microsoft.UI.Input.PointerPoint, isShiftKeyDown: Boolean, isControlKeyDown: Boolean) -> Void: ...
    @winrt_mixinmethod
    def ProcessInertia(self: win32more.Microsoft.UI.Input.IGestureRecognizer) -> Void: ...
    @winrt_mixinmethod
    def ProcessUpEvent(self: win32more.Microsoft.UI.Input.IGestureRecognizer, value: win32more.Microsoft.UI.Input.PointerPoint) -> Void: ...
    @winrt_mixinmethod
    def add_Tapped(self: win32more.Microsoft.UI.Input.IGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.GestureRecognizer, win32more.Microsoft.UI.Input.TappedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Tapped(self: win32more.Microsoft.UI.Input.IGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_RightTapped(self: win32more.Microsoft.UI.Input.IGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.GestureRecognizer, win32more.Microsoft.UI.Input.RightTappedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RightTapped(self: win32more.Microsoft.UI.Input.IGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Holding(self: win32more.Microsoft.UI.Input.IGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.GestureRecognizer, win32more.Microsoft.UI.Input.HoldingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Holding(self: win32more.Microsoft.UI.Input.IGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_Dragging(self: win32more.Microsoft.UI.Input.IGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.GestureRecognizer, win32more.Microsoft.UI.Input.DraggingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Dragging(self: win32more.Microsoft.UI.Input.IGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationStarted(self: win32more.Microsoft.UI.Input.IGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.GestureRecognizer, win32more.Microsoft.UI.Input.ManipulationStartedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationStarted(self: win32more.Microsoft.UI.Input.IGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationUpdated(self: win32more.Microsoft.UI.Input.IGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.GestureRecognizer, win32more.Microsoft.UI.Input.ManipulationUpdatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationUpdated(self: win32more.Microsoft.UI.Input.IGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationInertiaStarting(self: win32more.Microsoft.UI.Input.IGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.GestureRecognizer, win32more.Microsoft.UI.Input.ManipulationInertiaStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationInertiaStarting(self: win32more.Microsoft.UI.Input.IGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ManipulationCompleted(self: win32more.Microsoft.UI.Input.IGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.GestureRecognizer, win32more.Microsoft.UI.Input.ManipulationCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ManipulationCompleted(self: win32more.Microsoft.UI.Input.IGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CrossSliding(self: win32more.Microsoft.UI.Input.IGestureRecognizer, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.GestureRecognizer, win32more.Microsoft.UI.Input.CrossSlidingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CrossSliding(self: win32more.Microsoft.UI.Input.IGestureRecognizer, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AutoProcessInertia = property(get_AutoProcessInertia, put_AutoProcessInertia)
    CrossSlideExact = property(get_CrossSlideExact, put_CrossSlideExact)
    CrossSlideHorizontally = property(get_CrossSlideHorizontally, put_CrossSlideHorizontally)
    CrossSlideThresholds = property(get_CrossSlideThresholds, put_CrossSlideThresholds)
    GestureSettings = property(get_GestureSettings, put_GestureSettings)
    InertiaExpansion = property(get_InertiaExpansion, put_InertiaExpansion)
    InertiaExpansionDeceleration = property(get_InertiaExpansionDeceleration, put_InertiaExpansionDeceleration)
    InertiaRotationAngle = property(get_InertiaRotationAngle, put_InertiaRotationAngle)
    InertiaRotationDeceleration = property(get_InertiaRotationDeceleration, put_InertiaRotationDeceleration)
    InertiaTranslationDeceleration = property(get_InertiaTranslationDeceleration, put_InertiaTranslationDeceleration)
    InertiaTranslationDisplacement = property(get_InertiaTranslationDisplacement, put_InertiaTranslationDisplacement)
    IsActive = property(get_IsActive, None)
    IsInertial = property(get_IsInertial, None)
    ManipulationExact = property(get_ManipulationExact, put_ManipulationExact)
    MouseWheelParameters = property(get_MouseWheelParameters, None)
    PivotCenter = property(get_PivotCenter, put_PivotCenter)
    PivotRadius = property(get_PivotRadius, put_PivotRadius)
    ShowGestureFeedback = property(get_ShowGestureFeedback, put_ShowGestureFeedback)
    Tapped = event()
    RightTapped = event()
    Holding = event()
    Dragging = event()
    ManipulationStarted = event()
    ManipulationUpdated = event()
    ManipulationInertiaStarting = event()
    ManipulationCompleted = event()
    CrossSliding = event()
class GestureSettings(Enum, UInt32):
    None_ = 0
    Tap = 1
    DoubleTap = 2
    Hold = 4
    HoldWithMouse = 8
    RightTap = 16
    Drag = 32
    ManipulationTranslateX = 64
    ManipulationTranslateY = 128
    ManipulationTranslateRailsX = 256
    ManipulationTranslateRailsY = 512
    ManipulationRotate = 1024
    ManipulationScale = 2048
    ManipulationTranslateInertia = 4096
    ManipulationRotateInertia = 8192
    ManipulationScaleInertia = 16384
    CrossSlide = 32768
    ManipulationMultipleFingerPanning = 65536
class HoldingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.IHoldingEventArgs
    _classid_ = 'Microsoft.UI.Input.HoldingEventArgs'
    @winrt_mixinmethod
    def get_HoldingState(self: win32more.Microsoft.UI.Input.IHoldingEventArgs) -> win32more.Microsoft.UI.Input.HoldingState: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Microsoft.UI.Input.IHoldingEventArgs) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Microsoft.UI.Input.IHoldingEventArgs) -> win32more.Windows.Foundation.Point: ...
    HoldingState = property(get_HoldingState, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
class HoldingState(Enum, Int32):
    Started = 0
    Completed = 1
    Canceled = 2
class ICharacterReceivedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.ICharacterReceivedEventArgs'
    _iid_ = Guid('{36122718-9263-592b-8d87-8f86543ffc95}')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_KeyCode(self) -> UInt32: ...
    @winrt_commethod(9)
    def get_KeyStatus(self) -> win32more.Microsoft.UI.Input.PhysicalKeyStatus: ...
    Handled = property(get_Handled, put_Handled)
    KeyCode = property(get_KeyCode, None)
    KeyStatus = property(get_KeyStatus, None)
class IContextMenuKeyEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IContextMenuKeyEventArgs'
    _iid_ = Guid('{f6025762-9426-541a-b647-037abdbecefc}')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
class ICrossSlidingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.ICrossSlidingEventArgs'
    _iid_ = Guid('{7679641f-ba9f-543c-a7c8-6229a98f89ef}')
    @winrt_commethod(6)
    def get_CrossSlidingState(self) -> win32more.Microsoft.UI.Input.CrossSlidingState: ...
    @winrt_commethod(7)
    def get_PointerDeviceType(self) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_commethod(8)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    CrossSlidingState = property(get_CrossSlidingState, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
class IDraggingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IDraggingEventArgs'
    _iid_ = Guid('{3efb1b75-3d3b-550e-963d-0828ca76128a}')
    @winrt_commethod(6)
    def get_DraggingState(self) -> win32more.Microsoft.UI.Input.DraggingState: ...
    @winrt_commethod(7)
    def get_PointerDeviceType(self) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_commethod(8)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    DraggingState = property(get_DraggingState, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
class IEnteredMoveSizeEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IEnteredMoveSizeEventArgs'
    _iid_ = Guid('{698d28fe-d325-59e0-9834-b10fc2f7ba67}')
    @winrt_commethod(6)
    def get_PointerScreenPoint(self) -> win32more.Windows.Graphics.PointInt32: ...
    @winrt_commethod(7)
    def get_MoveSizeOperation(self) -> win32more.Microsoft.UI.Input.MoveSizeOperation: ...
    MoveSizeOperation = property(get_MoveSizeOperation, None)
    PointerScreenPoint = property(get_PointerScreenPoint, None)
class IEnteringMoveSizeEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IEnteringMoveSizeEventArgs'
    _iid_ = Guid('{47c083b2-402b-51ec-8836-d48679fea695}')
    @winrt_commethod(6)
    def get_PointerScreenPoint(self) -> win32more.Windows.Graphics.PointInt32: ...
    @winrt_commethod(7)
    def get_MoveSizeOperation(self) -> win32more.Microsoft.UI.Input.MoveSizeOperation: ...
    @winrt_commethod(8)
    def get_MoveSizeWindowId(self) -> win32more.Microsoft.UI.WindowId: ...
    @winrt_commethod(9)
    def put_MoveSizeWindowId(self, value: win32more.Microsoft.UI.WindowId) -> Void: ...
    MoveSizeOperation = property(get_MoveSizeOperation, None)
    MoveSizeWindowId = property(get_MoveSizeWindowId, put_MoveSizeWindowId)
    PointerScreenPoint = property(get_PointerScreenPoint, None)
class IExitedMoveSizeEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IExitedMoveSizeEventArgs'
    _iid_ = Guid('{df12a46e-daee-5dac-a678-d7d5e4d0893a}')
    @winrt_commethod(6)
    def get_PointerScreenPoint(self) -> win32more.Windows.Graphics.PointInt32: ...
    @winrt_commethod(7)
    def get_MoveSizeOperation(self) -> win32more.Microsoft.UI.Input.MoveSizeOperation: ...
    MoveSizeOperation = property(get_MoveSizeOperation, None)
    PointerScreenPoint = property(get_PointerScreenPoint, None)
class IFocusChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IFocusChangedEventArgs'
    _iid_ = Guid('{a039b115-dbdf-594c-9b86-da6aa05c9fa2}')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    Handled = property(get_Handled, put_Handled)
class IFocusNavigationRequest(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IFocusNavigationRequest'
    _iid_ = Guid('{6d84bb83-9c84-5112-85e9-8919acf97262}')
    @winrt_commethod(6)
    def get_CorrelationId(self) -> Guid: ...
    @winrt_commethod(7)
    def get_HintRect(self) -> win32more.Windows.Foundation.IReference[win32more.Windows.Foundation.Rect]: ...
    @winrt_commethod(8)
    def get_Reason(self) -> win32more.Microsoft.UI.Input.FocusNavigationReason: ...
    CorrelationId = property(get_CorrelationId, None)
    HintRect = property(get_HintRect, None)
    Reason = property(get_Reason, None)
class IFocusNavigationRequestEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IFocusNavigationRequestEventArgs'
    _iid_ = Guid('{35a63426-e271-59f9-a231-0d190314b415}')
    @winrt_commethod(6)
    def get_Request(self) -> win32more.Microsoft.UI.Input.FocusNavigationRequest: ...
    @winrt_commethod(7)
    def get_Result(self) -> win32more.Microsoft.UI.Input.FocusNavigationResult: ...
    @winrt_commethod(8)
    def put_Result(self, value: win32more.Microsoft.UI.Input.FocusNavigationResult) -> Void: ...
    Request = property(get_Request, None)
    Result = property(get_Result, put_Result)
class IFocusNavigationRequestStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IFocusNavigationRequestStatics'
    _iid_ = Guid('{8c4d2ed8-3a63-519e-a827-f57e263bd1ff}')
    @winrt_commethod(6)
    def Create(self, reason: win32more.Microsoft.UI.Input.FocusNavigationReason) -> win32more.Microsoft.UI.Input.FocusNavigationRequest: ...
    @winrt_commethod(7)
    def CreateWithHintRect(self, reason: win32more.Microsoft.UI.Input.FocusNavigationReason, hintRect: win32more.Windows.Foundation.Rect) -> win32more.Microsoft.UI.Input.FocusNavigationRequest: ...
    @winrt_commethod(8)
    def CreateWithHintRectAndId(self, reason: win32more.Microsoft.UI.Input.FocusNavigationReason, hintRect: win32more.Windows.Foundation.Rect, correlationId: Guid) -> win32more.Microsoft.UI.Input.FocusNavigationRequest: ...
class IGestureRecognizer(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IGestureRecognizer'
    _iid_ = Guid('{cda89afc-6bd0-595c-ba37-545fce5bf016}')
    @winrt_commethod(6)
    def get_AutoProcessInertia(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_AutoProcessInertia(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_CrossSlideExact(self) -> Boolean: ...
    @winrt_commethod(9)
    def put_CrossSlideExact(self, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_CrossSlideHorizontally(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_CrossSlideHorizontally(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_CrossSlideThresholds(self) -> win32more.Microsoft.UI.Input.CrossSlideThresholds: ...
    @winrt_commethod(13)
    def put_CrossSlideThresholds(self, value: win32more.Microsoft.UI.Input.CrossSlideThresholds) -> Void: ...
    @winrt_commethod(14)
    def get_GestureSettings(self) -> win32more.Microsoft.UI.Input.GestureSettings: ...
    @winrt_commethod(15)
    def put_GestureSettings(self, value: win32more.Microsoft.UI.Input.GestureSettings) -> Void: ...
    @winrt_commethod(16)
    def get_IsActive(self) -> Boolean: ...
    @winrt_commethod(17)
    def get_IsInertial(self) -> Boolean: ...
    @winrt_commethod(18)
    def get_PivotCenter(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(19)
    def put_PivotCenter(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(20)
    def get_PivotRadius(self) -> Single: ...
    @winrt_commethod(21)
    def put_PivotRadius(self, value: Single) -> Void: ...
    @winrt_commethod(22)
    def get_InertiaExpansionDeceleration(self) -> Single: ...
    @winrt_commethod(23)
    def put_InertiaExpansionDeceleration(self, value: Single) -> Void: ...
    @winrt_commethod(24)
    def get_InertiaExpansion(self) -> Single: ...
    @winrt_commethod(25)
    def put_InertiaExpansion(self, value: Single) -> Void: ...
    @winrt_commethod(26)
    def get_InertiaRotationAngle(self) -> Single: ...
    @winrt_commethod(27)
    def put_InertiaRotationAngle(self, value: Single) -> Void: ...
    @winrt_commethod(28)
    def get_InertiaRotationDeceleration(self) -> Single: ...
    @winrt_commethod(29)
    def put_InertiaRotationDeceleration(self, value: Single) -> Void: ...
    @winrt_commethod(30)
    def get_InertiaTranslationDeceleration(self) -> Single: ...
    @winrt_commethod(31)
    def put_InertiaTranslationDeceleration(self, value: Single) -> Void: ...
    @winrt_commethod(32)
    def get_InertiaTranslationDisplacement(self) -> Single: ...
    @winrt_commethod(33)
    def put_InertiaTranslationDisplacement(self, value: Single) -> Void: ...
    @winrt_commethod(34)
    def get_ManipulationExact(self) -> Boolean: ...
    @winrt_commethod(35)
    def put_ManipulationExact(self, value: Boolean) -> Void: ...
    @winrt_commethod(36)
    def get_MouseWheelParameters(self) -> win32more.Microsoft.UI.Input.MouseWheelParameters: ...
    @winrt_commethod(37)
    def get_ShowGestureFeedback(self) -> Boolean: ...
    @winrt_commethod(38)
    def put_ShowGestureFeedback(self, value: Boolean) -> Void: ...
    @winrt_commethod(39)
    def CanBeDoubleTap(self, value: win32more.Microsoft.UI.Input.PointerPoint) -> Boolean: ...
    @winrt_commethod(40)
    def CompleteGesture(self) -> Void: ...
    @winrt_commethod(41)
    def ProcessDownEvent(self, value: win32more.Microsoft.UI.Input.PointerPoint) -> Void: ...
    @winrt_commethod(42)
    def ProcessMoveEvents(self, value: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Input.PointerPoint]) -> Void: ...
    @winrt_commethod(43)
    def ProcessMouseWheelEvent(self, value: win32more.Microsoft.UI.Input.PointerPoint, isShiftKeyDown: Boolean, isControlKeyDown: Boolean) -> Void: ...
    @winrt_commethod(44)
    def ProcessInertia(self) -> Void: ...
    @winrt_commethod(45)
    def ProcessUpEvent(self, value: win32more.Microsoft.UI.Input.PointerPoint) -> Void: ...
    @winrt_commethod(46)
    def add_Tapped(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.GestureRecognizer, win32more.Microsoft.UI.Input.TappedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(47)
    def remove_Tapped(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(48)
    def add_RightTapped(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.GestureRecognizer, win32more.Microsoft.UI.Input.RightTappedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(49)
    def remove_RightTapped(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(50)
    def add_Holding(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.GestureRecognizer, win32more.Microsoft.UI.Input.HoldingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(51)
    def remove_Holding(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(52)
    def add_Dragging(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.GestureRecognizer, win32more.Microsoft.UI.Input.DraggingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(53)
    def remove_Dragging(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(54)
    def add_ManipulationStarted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.GestureRecognizer, win32more.Microsoft.UI.Input.ManipulationStartedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(55)
    def remove_ManipulationStarted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(56)
    def add_ManipulationUpdated(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.GestureRecognizer, win32more.Microsoft.UI.Input.ManipulationUpdatedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(57)
    def remove_ManipulationUpdated(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(58)
    def add_ManipulationInertiaStarting(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.GestureRecognizer, win32more.Microsoft.UI.Input.ManipulationInertiaStartingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(59)
    def remove_ManipulationInertiaStarting(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(60)
    def add_ManipulationCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.GestureRecognizer, win32more.Microsoft.UI.Input.ManipulationCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(61)
    def remove_ManipulationCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(62)
    def add_CrossSliding(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.GestureRecognizer, win32more.Microsoft.UI.Input.CrossSlidingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(63)
    def remove_CrossSliding(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    AutoProcessInertia = property(get_AutoProcessInertia, put_AutoProcessInertia)
    CrossSlideExact = property(get_CrossSlideExact, put_CrossSlideExact)
    CrossSlideHorizontally = property(get_CrossSlideHorizontally, put_CrossSlideHorizontally)
    CrossSlideThresholds = property(get_CrossSlideThresholds, put_CrossSlideThresholds)
    GestureSettings = property(get_GestureSettings, put_GestureSettings)
    InertiaExpansion = property(get_InertiaExpansion, put_InertiaExpansion)
    InertiaExpansionDeceleration = property(get_InertiaExpansionDeceleration, put_InertiaExpansionDeceleration)
    InertiaRotationAngle = property(get_InertiaRotationAngle, put_InertiaRotationAngle)
    InertiaRotationDeceleration = property(get_InertiaRotationDeceleration, put_InertiaRotationDeceleration)
    InertiaTranslationDeceleration = property(get_InertiaTranslationDeceleration, put_InertiaTranslationDeceleration)
    InertiaTranslationDisplacement = property(get_InertiaTranslationDisplacement, put_InertiaTranslationDisplacement)
    IsActive = property(get_IsActive, None)
    IsInertial = property(get_IsInertial, None)
    ManipulationExact = property(get_ManipulationExact, put_ManipulationExact)
    MouseWheelParameters = property(get_MouseWheelParameters, None)
    PivotCenter = property(get_PivotCenter, put_PivotCenter)
    PivotRadius = property(get_PivotRadius, put_PivotRadius)
    ShowGestureFeedback = property(get_ShowGestureFeedback, put_ShowGestureFeedback)
    Tapped = event()
    RightTapped = event()
    Holding = event()
    Dragging = event()
    ManipulationStarted = event()
    ManipulationUpdated = event()
    ManipulationInertiaStarting = event()
    ManipulationCompleted = event()
    CrossSliding = event()
class IHoldingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IHoldingEventArgs'
    _iid_ = Guid('{8e449e85-d223-533c-b0b2-bf7c6d10c2db}')
    @winrt_commethod(6)
    def get_HoldingState(self) -> win32more.Microsoft.UI.Input.HoldingState: ...
    @winrt_commethod(7)
    def get_PointerDeviceType(self) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_commethod(8)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    HoldingState = property(get_HoldingState, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
class IInputActivationListener(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputActivationListener'
    _iid_ = Guid('{3b818627-6ce7-5e0d-a0f5-6684fd1aec78}')
    @winrt_commethod(6)
    def get_State(self) -> win32more.Microsoft.UI.Input.InputActivationState: ...
    @winrt_commethod(7)
    def add_InputActivationChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputActivationListener, win32more.Microsoft.UI.Input.InputActivationListenerActivationChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_InputActivationChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    State = property(get_State, None)
    InputActivationChanged = event()
class IInputActivationListenerActivationChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputActivationListenerActivationChangedEventArgs'
    _iid_ = Guid('{7978526b-00b6-5303-8f7d-55bef36da786}')
class IInputActivationListenerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputActivationListenerStatics'
    _iid_ = Guid('{c4249843-f053-5c99-9d51-720ade94224d}')
    @winrt_commethod(6)
    def GetForWindowId(self, windowId: win32more.Microsoft.UI.WindowId) -> win32more.Microsoft.UI.Input.InputActivationListener: ...
class IInputActivationListenerStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputActivationListenerStatics2'
    _iid_ = Guid('{7ea26120-9636-5292-a7b1-56544ac51a22}')
    @winrt_commethod(6)
    def GetForIsland(self, island: win32more.Microsoft.UI.Content.ContentIsland) -> win32more.Microsoft.UI.Input.InputActivationListener: ...
class IInputCursor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputCursor'
    _iid_ = Guid('{359b15f9-19c2-5714-8432-75176826406b}')
class IInputCursorFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputCursorFactory'
    _iid_ = Guid('{2f47647b-4be0-53e9-be7e-c38d5459db6b}')
class IInputCursorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputCursorStatics'
    _iid_ = Guid('{92f6a552-099f-55fb-8c31-e450284c9643}')
    @winrt_commethod(6)
    def CreateFromCoreCursor(self, cursor: win32more.Windows.UI.Core.CoreCursor) -> win32more.Microsoft.UI.Input.InputCursor: ...
class IInputCustomCursor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputCustomCursor'
    _iid_ = Guid('{5486f042-7e1a-5dc8-8041-e47b609a5ba1}')
class IInputCustomCursorFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputCustomCursorFactory'
    _iid_ = Guid('{6f402882-66e0-57d3-89d0-aa5e2ff917bc}')
class IInputDesktopNamedResourceCursor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputDesktopNamedResourceCursor'
    _iid_ = Guid('{f40ea93b-0ed7-5b3a-bfe2-14e2b5ad88a3}')
    @winrt_commethod(6)
    def get_ModuleName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ResourceName(self) -> WinRT_String: ...
    ModuleName = property(get_ModuleName, None)
    ResourceName = property(get_ResourceName, None)
class IInputDesktopNamedResourceCursorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputDesktopNamedResourceCursorStatics'
    _iid_ = Guid('{e8b6d5aa-898b-5e69-b01f-383a0943e3e4}')
    @winrt_commethod(6)
    def Create(self, resourceName: WinRT_String) -> win32more.Microsoft.UI.Input.InputDesktopNamedResourceCursor: ...
    @winrt_commethod(7)
    def CreateFromModule(self, moduleName: WinRT_String, resourceName: WinRT_String) -> win32more.Microsoft.UI.Input.InputDesktopNamedResourceCursor: ...
class IInputDesktopResourceCursor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputDesktopResourceCursor'
    _iid_ = Guid('{1df2777f-7c90-58fc-a7a3-d5736c6510fd}')
    @winrt_commethod(6)
    def get_ModuleName(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_ResourceId(self) -> UInt32: ...
    ModuleName = property(get_ModuleName, None)
    ResourceId = property(get_ResourceId, None)
class IInputDesktopResourceCursorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputDesktopResourceCursorStatics'
    _iid_ = Guid('{f440dc37-a0b6-56eb-bcec-b024f2233d47}')
    @winrt_commethod(6)
    def Create(self, resourceId: UInt32) -> win32more.Microsoft.UI.Input.InputDesktopResourceCursor: ...
    @winrt_commethod(7)
    def CreateFromModule(self, moduleName: WinRT_String, resourceId: UInt32) -> win32more.Microsoft.UI.Input.InputDesktopResourceCursor: ...
class IInputFocusController(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputFocusController'
    _iid_ = Guid('{8dfdc26c-8b8d-515d-8ddd-4685b3a540e9}')
    @winrt_commethod(6)
    def get_HasFocus(self) -> Boolean: ...
    @winrt_commethod(7)
    def TrySetFocus(self) -> Boolean: ...
    @winrt_commethod(8)
    def add_GotFocus(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputFocusController, win32more.Microsoft.UI.Input.FocusChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_GotFocus(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_LostFocus(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputFocusController, win32more.Microsoft.UI.Input.FocusChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_LostFocus(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    HasFocus = property(get_HasFocus, None)
    GotFocus = event()
    LostFocus = event()
class IInputFocusController2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputFocusController2'
    _iid_ = Guid('{5165077c-cd4b-501d-b386-b50682360185}')
    @winrt_commethod(6)
    def DepartFocus(self, request: win32more.Microsoft.UI.Input.FocusNavigationRequest) -> win32more.Microsoft.UI.Input.FocusNavigationResult: ...
    @winrt_commethod(7)
    def add_NavigateFocusRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputFocusController, win32more.Microsoft.UI.Input.FocusNavigationRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(8)
    def remove_NavigateFocusRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    NavigateFocusRequested = event()
class IInputFocusControllerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputFocusControllerStatics'
    _iid_ = Guid('{aeb311da-da9b-5a1b-92f4-83ddde933e00}')
    @winrt_commethod(6)
    def GetForIsland(self, island: win32more.Microsoft.UI.Content.ContentIsland) -> win32more.Microsoft.UI.Input.InputFocusController: ...
class IInputFocusNavigationHost(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputFocusNavigationHost'
    _iid_ = Guid('{53c2a147-932c-5486-a9c6-f6c5a9c65956}')
    @winrt_commethod(6)
    def get_ContainsFocus(self) -> Boolean: ...
    @winrt_commethod(7)
    def NavigateFocus(self, request: win32more.Microsoft.UI.Input.FocusNavigationRequest) -> win32more.Microsoft.UI.Input.FocusNavigationResult: ...
    @winrt_commethod(8)
    def add_DepartFocusRequested(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputFocusNavigationHost, win32more.Microsoft.UI.Input.FocusNavigationRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_DepartFocusRequested(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ContainsFocus = property(get_ContainsFocus, None)
    DepartFocusRequested = event()
class IInputFocusNavigationHostStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputFocusNavigationHostStatics'
    _iid_ = Guid('{c9c62cd1-73db-5aa9-b89d-143509db8f37}')
    @winrt_commethod(6)
    def GetForSiteBridge(self, site: win32more.Microsoft.UI.Content.IContentSiteBridge) -> win32more.Microsoft.UI.Input.InputFocusNavigationHost: ...
class IInputFocusNavigationHostStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputFocusNavigationHostStatics2'
    _iid_ = Guid('{82505f60-ef7b-55d8-8362-8cc2840266a1}')
    @winrt_commethod(6)
    def GetForSiteLink(self, contentSiteLink: win32more.Microsoft.UI.Content.IContentSiteLink) -> win32more.Microsoft.UI.Input.InputFocusNavigationHost: ...
class IInputKeyboardSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputKeyboardSource'
    _iid_ = Guid('{ed61b906-16ad-5df7-a550-5e6f7d2229f7}')
class IInputKeyboardSource2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputKeyboardSource2'
    _iid_ = Guid('{79d1c9b6-b3c9-5ec2-8a5b-707088787f78}')
    @winrt_commethod(6)
    def GetCurrentKeyState(self, virtualKey: win32more.Windows.System.VirtualKey) -> win32more.Microsoft.UI.Input.VirtualKeyStates: ...
    @winrt_commethod(7)
    def GetKeyState(self, virtualKey: win32more.Windows.System.VirtualKey) -> win32more.Microsoft.UI.Input.VirtualKeyStates: ...
    @winrt_commethod(8)
    def add_CharacterReceived(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputKeyboardSource, win32more.Microsoft.UI.Input.CharacterReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_CharacterReceived(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_ContextMenuKey(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputKeyboardSource, win32more.Microsoft.UI.Input.ContextMenuKeyEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ContextMenuKey(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_KeyDown(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputKeyboardSource, win32more.Microsoft.UI.Input.KeyEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_KeyDown(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_KeyUp(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputKeyboardSource, win32more.Microsoft.UI.Input.KeyEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_KeyUp(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_SystemKeyDown(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputKeyboardSource, win32more.Microsoft.UI.Input.KeyEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_SystemKeyDown(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_SystemKeyUp(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputKeyboardSource, win32more.Microsoft.UI.Input.KeyEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_SystemKeyUp(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    CharacterReceived = event()
    ContextMenuKey = event()
    KeyDown = event()
    KeyUp = event()
    SystemKeyDown = event()
    SystemKeyUp = event()
class IInputKeyboardSourceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputKeyboardSourceStatics'
    _iid_ = Guid('{f4e1563d-8c2e-5bcd-b784-47adeaa3cd7e}')
    @winrt_commethod(6)
    def GetKeyStateForCurrentThread(self, virtualKey: win32more.Windows.System.VirtualKey) -> win32more.Windows.UI.Core.CoreVirtualKeyStates: ...
class IInputKeyboardSourceStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputKeyboardSourceStatics2'
    _iid_ = Guid('{8857518c-2899-5f11-9b64-0ad83234824b}')
    @winrt_commethod(6)
    def GetForIsland(self, island: win32more.Microsoft.UI.Content.ContentIsland) -> win32more.Microsoft.UI.Input.InputKeyboardSource: ...
class IInputLightDismissAction(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputLightDismissAction'
    _iid_ = Guid('{e8a39502-a860-502f-8c10-3646d43aecf1}')
    @winrt_commethod(6)
    def add_Dismissed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputLightDismissAction, win32more.Microsoft.UI.Input.InputLightDismissEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Dismissed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Dismissed = event()
class IInputLightDismissActionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputLightDismissActionStatics'
    _iid_ = Guid('{ed9b8def-6496-5169-984d-d44b4e690623}')
    @winrt_commethod(6)
    def GetForWindowId(self, windowId: win32more.Microsoft.UI.WindowId) -> win32more.Microsoft.UI.Input.InputLightDismissAction: ...
class IInputLightDismissEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputLightDismissEventArgs'
    _iid_ = Guid('{078660ee-07ca-5808-b982-e6e899cf098c}')
class IInputNonClientPointerSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputNonClientPointerSource'
    _iid_ = Guid('{471732b4-3d07-5104-b192-ebacf71e86df}')
    @winrt_commethod(6)
    def get_DispatcherQueue(self) -> win32more.Microsoft.UI.Dispatching.DispatcherQueue: ...
    @winrt_commethod(7)
    def ClearAllRegionRects(self) -> Void: ...
    @winrt_commethod(8)
    def ClearRegionRects(self, region: win32more.Microsoft.UI.Input.NonClientRegionKind) -> Void: ...
    @winrt_commethod(9)
    def GetRegionRects(self, region: win32more.Microsoft.UI.Input.NonClientRegionKind) -> ReceiveArray[win32more.Windows.Graphics.RectInt32]: ...
    @winrt_commethod(10)
    def SetRegionRects(self, region: win32more.Microsoft.UI.Input.NonClientRegionKind, rects: PassArray[win32more.Windows.Graphics.RectInt32]) -> Void: ...
    @winrt_commethod(11)
    def add_CaptionTapped(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputNonClientPointerSource, win32more.Microsoft.UI.Input.NonClientCaptionTappedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_CaptionTapped(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_PointerEntered(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputNonClientPointerSource, win32more.Microsoft.UI.Input.NonClientPointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_PointerEntered(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def add_PointerExited(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputNonClientPointerSource, win32more.Microsoft.UI.Input.NonClientPointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_PointerExited(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_PointerMoved(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputNonClientPointerSource, win32more.Microsoft.UI.Input.NonClientPointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_PointerMoved(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(19)
    def add_PointerPressed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputNonClientPointerSource, win32more.Microsoft.UI.Input.NonClientPointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_PointerPressed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(21)
    def add_PointerReleased(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputNonClientPointerSource, win32more.Microsoft.UI.Input.NonClientPointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(22)
    def remove_PointerReleased(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(23)
    def add_RegionsChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputNonClientPointerSource, win32more.Microsoft.UI.Input.NonClientRegionsChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(24)
    def remove_RegionsChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    DispatcherQueue = property(get_DispatcherQueue, None)
    CaptionTapped = event()
    PointerEntered = event()
    PointerExited = event()
    PointerMoved = event()
    PointerPressed = event()
    PointerReleased = event()
    RegionsChanged = event()
class IInputNonClientPointerSource2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputNonClientPointerSource2'
    _iid_ = Guid('{dd2b10c4-7de6-5c1d-b438-06ddc994058f}')
    @winrt_commethod(6)
    def add_EnteringMoveSize(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputNonClientPointerSource, win32more.Microsoft.UI.Input.EnteringMoveSizeEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_EnteringMoveSize(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_EnteredMoveSize(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputNonClientPointerSource, win32more.Microsoft.UI.Input.EnteredMoveSizeEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_EnteredMoveSize(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_WindowRectChanging(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputNonClientPointerSource, win32more.Microsoft.UI.Input.WindowRectChangingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_WindowRectChanging(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_WindowRectChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputNonClientPointerSource, win32more.Microsoft.UI.Input.WindowRectChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_WindowRectChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_ExitedMoveSize(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputNonClientPointerSource, win32more.Microsoft.UI.Input.ExitedMoveSizeEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_ExitedMoveSize(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    EnteringMoveSize = event()
    EnteredMoveSize = event()
    WindowRectChanging = event()
    WindowRectChanged = event()
    ExitedMoveSize = event()
class IInputNonClientPointerSourceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputNonClientPointerSourceStatics'
    _iid_ = Guid('{7d0b775c-1903-5dc7-bd2f-7a4b31f0cff2}')
    @winrt_commethod(6)
    def GetForWindowId(self, windowId: win32more.Microsoft.UI.WindowId) -> win32more.Microsoft.UI.Input.InputNonClientPointerSource: ...
class IInputObject(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputObject'
    _iid_ = Guid('{42edbc88-d386-544d-b1b8-68617fe68282}')
    @winrt_commethod(6)
    def get_DispatcherQueue(self) -> win32more.Microsoft.UI.Dispatching.DispatcherQueue: ...
    DispatcherQueue = property(get_DispatcherQueue, None)
class IInputObjectFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputObjectFactory'
    _iid_ = Guid('{f7786bc2-b0b8-5961-9a57-ae199d452106}')
class IInputPointerSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputPointerSource'
    _iid_ = Guid('{6a6c2764-c3f4-5be5-8447-c9a98766c240}')
    @winrt_commethod(6)
    def get_Cursor(self) -> win32more.Microsoft.UI.Input.InputCursor: ...
    @winrt_commethod(7)
    def put_Cursor(self, value: win32more.Microsoft.UI.Input.InputCursor) -> Void: ...
    @winrt_commethod(8)
    def get_DeviceKinds(self) -> win32more.Microsoft.UI.Input.InputPointerSourceDeviceKinds: ...
    @winrt_commethod(9)
    def add_PointerCaptureLost(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputPointerSource, win32more.Microsoft.UI.Input.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_PointerCaptureLost(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(11)
    def add_PointerEntered(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputPointerSource, win32more.Microsoft.UI.Input.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(12)
    def remove_PointerEntered(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(13)
    def add_PointerExited(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputPointerSource, win32more.Microsoft.UI.Input.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(14)
    def remove_PointerExited(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(15)
    def add_PointerMoved(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputPointerSource, win32more.Microsoft.UI.Input.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(16)
    def remove_PointerMoved(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(17)
    def add_PointerPressed(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputPointerSource, win32more.Microsoft.UI.Input.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(18)
    def remove_PointerPressed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(19)
    def add_PointerReleased(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputPointerSource, win32more.Microsoft.UI.Input.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_PointerReleased(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(21)
    def add_PointerRoutedAway(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputPointerSource, win32more.Microsoft.UI.Input.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(22)
    def remove_PointerRoutedAway(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(23)
    def add_PointerRoutedReleased(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputPointerSource, win32more.Microsoft.UI.Input.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(24)
    def remove_PointerRoutedReleased(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(25)
    def add_PointerRoutedTo(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputPointerSource, win32more.Microsoft.UI.Input.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(26)
    def remove_PointerRoutedTo(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(27)
    def add_PointerWheelChanged(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputPointerSource, win32more.Microsoft.UI.Input.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(28)
    def remove_PointerWheelChanged(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Cursor = property(get_Cursor, put_Cursor)
    DeviceKinds = property(get_DeviceKinds, None)
    PointerCaptureLost = event()
    PointerEntered = event()
    PointerExited = event()
    PointerMoved = event()
    PointerPressed = event()
    PointerReleased = event()
    PointerRoutedAway = event()
    PointerRoutedReleased = event()
    PointerRoutedTo = event()
    PointerWheelChanged = event()
class IInputPointerSourceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputPointerSourceStatics'
    _iid_ = Guid('{e8a19fd1-a914-533f-9b0f-6bf0065e6781}')
    @winrt_commethod(6)
    def GetForIsland(self, island: win32more.Microsoft.UI.Content.ContentIsland) -> win32more.Microsoft.UI.Input.InputPointerSource: ...
class IInputPreTranslateKeyboardSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputPreTranslateKeyboardSource'
    _iid_ = Guid('{2f327feb-b7e7-5e37-a0cc-37dcabe76588}')
class IInputPreTranslateKeyboardSourceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputPreTranslateKeyboardSourceStatics'
    _iid_ = Guid('{23d584d2-af8c-5a8a-806f-2ba9c5b1a5ec}')
    @winrt_commethod(6)
    def GetForIsland(self, island: win32more.Microsoft.UI.Content.ContentIsland) -> win32more.Microsoft.UI.Input.InputPreTranslateKeyboardSource: ...
class IInputSystemCursor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputSystemCursor'
    _iid_ = Guid('{59f538e7-c500-59ab-8b54-0bc6100fd49e}')
    @winrt_commethod(6)
    def get_CursorShape(self) -> win32more.Microsoft.UI.Input.InputSystemCursorShape: ...
    CursorShape = property(get_CursorShape, None)
class IInputSystemCursorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IInputSystemCursorStatics'
    _iid_ = Guid('{d3860bb6-698a-5814-aedd-c2fa8bba5a02}')
    @winrt_commethod(6)
    def Create(self, type: win32more.Microsoft.UI.Input.InputSystemCursorShape) -> win32more.Microsoft.UI.Input.InputSystemCursor: ...
class IKeyEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IKeyEventArgs'
    _iid_ = Guid('{40d5bb74-977e-5194-8039-9f6c44427bbb}')
    @winrt_commethod(6)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(7)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_KeyStatus(self) -> win32more.Microsoft.UI.Input.PhysicalKeyStatus: ...
    @winrt_commethod(9)
    def get_Timestamp(self) -> UInt64: ...
    @winrt_commethod(10)
    def get_VirtualKey(self) -> win32more.Windows.System.VirtualKey: ...
    Handled = property(get_Handled, put_Handled)
    KeyStatus = property(get_KeyStatus, None)
    Timestamp = property(get_Timestamp, None)
    VirtualKey = property(get_VirtualKey, None)
class IManipulationCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IManipulationCompletedEventArgs'
    _iid_ = Guid('{0e0249d4-46e4-5559-aee3-fa45ce2a7f56}')
    @winrt_commethod(6)
    def get_Cumulative(self) -> win32more.Microsoft.UI.Input.ManipulationDelta: ...
    @winrt_commethod(7)
    def get_PointerDeviceType(self) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_commethod(8)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(9)
    def get_Velocities(self) -> win32more.Microsoft.UI.Input.ManipulationVelocities: ...
    Cumulative = property(get_Cumulative, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    Velocities = property(get_Velocities, None)
class IManipulationInertiaStartingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IManipulationInertiaStartingEventArgs'
    _iid_ = Guid('{acf9ef71-6e15-56ab-9260-f0d3ce5f66e8}')
    @winrt_commethod(6)
    def get_Cumulative(self) -> win32more.Microsoft.UI.Input.ManipulationDelta: ...
    @winrt_commethod(7)
    def get_Delta(self) -> win32more.Microsoft.UI.Input.ManipulationDelta: ...
    @winrt_commethod(8)
    def get_PointerDeviceType(self) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_commethod(9)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(10)
    def get_Velocities(self) -> win32more.Microsoft.UI.Input.ManipulationVelocities: ...
    Cumulative = property(get_Cumulative, None)
    Delta = property(get_Delta, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    Velocities = property(get_Velocities, None)
class IManipulationStartedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IManipulationStartedEventArgs'
    _iid_ = Guid('{4a616613-eef1-5f1b-a768-0775478d49d4}')
    @winrt_commethod(6)
    def get_Cumulative(self) -> win32more.Microsoft.UI.Input.ManipulationDelta: ...
    @winrt_commethod(7)
    def get_PointerDeviceType(self) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_commethod(8)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    Cumulative = property(get_Cumulative, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
class IManipulationUpdatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IManipulationUpdatedEventArgs'
    _iid_ = Guid('{406e1961-0c98-5fc0-b3d8-116492ef0053}')
    @winrt_commethod(6)
    def get_Cumulative(self) -> win32more.Microsoft.UI.Input.ManipulationDelta: ...
    @winrt_commethod(7)
    def get_Delta(self) -> win32more.Microsoft.UI.Input.ManipulationDelta: ...
    @winrt_commethod(8)
    def get_PointerDeviceType(self) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_commethod(9)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(10)
    def get_Velocities(self) -> win32more.Microsoft.UI.Input.ManipulationVelocities: ...
    Cumulative = property(get_Cumulative, None)
    Delta = property(get_Delta, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    Velocities = property(get_Velocities, None)
class IMouseWheelParameters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IMouseWheelParameters'
    _iid_ = Guid('{6d98be40-1d56-51d1-aa0d-f325439cd009}')
    @winrt_commethod(6)
    def get_CharTranslation(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def put_CharTranslation(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(8)
    def get_DeltaScale(self) -> Single: ...
    @winrt_commethod(9)
    def put_DeltaScale(self, value: Single) -> Void: ...
    @winrt_commethod(10)
    def get_DeltaRotationAngle(self) -> Single: ...
    @winrt_commethod(11)
    def put_DeltaRotationAngle(self, value: Single) -> Void: ...
    @winrt_commethod(12)
    def get_PageTranslation(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(13)
    def put_PageTranslation(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    CharTranslation = property(get_CharTranslation, put_CharTranslation)
    DeltaRotationAngle = property(get_DeltaRotationAngle, put_DeltaRotationAngle)
    DeltaScale = property(get_DeltaScale, put_DeltaScale)
    PageTranslation = property(get_PageTranslation, put_PageTranslation)
class INonClientCaptionTappedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.INonClientCaptionTappedEventArgs'
    _iid_ = Guid('{3d173531-991f-5753-b7e0-14a121c3cd2d}')
    @winrt_commethod(6)
    def get_Point(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def get_PointerDeviceType(self) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    Point = property(get_Point, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
class INonClientPointerEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.INonClientPointerEventArgs'
    _iid_ = Guid('{a5b44aec-b797-505a-a129-ae4e5271c73c}')
    @winrt_commethod(6)
    def get_Point(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def get_PointerDeviceType(self) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_commethod(8)
    def get_RegionKind(self) -> win32more.Microsoft.UI.Input.NonClientRegionKind: ...
    @winrt_commethod(9)
    def get_IsPointInRegion(self) -> Boolean: ...
    IsPointInRegion = property(get_IsPointInRegion, None)
    Point = property(get_Point, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    RegionKind = property(get_RegionKind, None)
class INonClientRegionsChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.INonClientRegionsChangedEventArgs'
    _iid_ = Guid('{fe97ee95-1824-51b2-b8eb-10ff0665ce23}')
    @winrt_commethod(6)
    def get_ChangedRegions(self) -> ReceiveArray[win32more.Microsoft.UI.Input.NonClientRegionKind]: ...
    ChangedRegions = property(get_ChangedRegions, None)
class IPointerEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IPointerEventArgs'
    _iid_ = Guid('{865b188c-2ed5-5df8-829f-ac0701d5c51a}')
    @winrt_commethod(6)
    def get_CurrentPoint(self) -> win32more.Microsoft.UI.Input.PointerPoint: ...
    @winrt_commethod(7)
    def get_Handled(self) -> Boolean: ...
    @winrt_commethod(8)
    def put_Handled(self, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_KeyModifiers(self) -> win32more.Windows.System.VirtualKeyModifiers: ...
    @winrt_commethod(10)
    def GetIntermediatePoints(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Input.PointerPoint]: ...
    @winrt_commethod(11)
    def GetIntermediateTransformedPoints(self, transform: win32more.Microsoft.UI.Input.IPointerPointTransform) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Input.PointerPoint]: ...
    CurrentPoint = property(get_CurrentPoint, None)
    Handled = property(get_Handled, put_Handled)
    KeyModifiers = property(get_KeyModifiers, None)
class IPointerPoint(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IPointerPoint'
    _iid_ = Guid('{0d430ee6-252c-59a4-b2a2-d44264dc6a40}')
    @winrt_commethod(6)
    def get_FrameId(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_IsInContact(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_PointerDeviceType(self) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_commethod(9)
    def get_PointerId(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(11)
    def get_Properties(self) -> win32more.Microsoft.UI.Input.PointerPointProperties: ...
    @winrt_commethod(12)
    def get_Timestamp(self) -> UInt64: ...
    @winrt_commethod(13)
    def GetTransformedPoint(self, transform: win32more.Microsoft.UI.Input.IPointerPointTransform) -> win32more.Microsoft.UI.Input.PointerPoint: ...
    FrameId = property(get_FrameId, None)
    IsInContact = property(get_IsInContact, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    PointerId = property(get_PointerId, None)
    Position = property(get_Position, None)
    Properties = property(get_Properties, None)
    Timestamp = property(get_Timestamp, None)
class IPointerPointProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IPointerPointProperties'
    _iid_ = Guid('{d760ed77-4b10-57a5-b3cc-d9bf3413e996}')
    @winrt_commethod(6)
    def get_ContactRect(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def get_IsBarrelButtonPressed(self) -> Boolean: ...
    @winrt_commethod(8)
    def get_IsCanceled(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_IsEraser(self) -> Boolean: ...
    @winrt_commethod(10)
    def get_IsHorizontalMouseWheel(self) -> Boolean: ...
    @winrt_commethod(11)
    def get_IsInRange(self) -> Boolean: ...
    @winrt_commethod(12)
    def get_IsInverted(self) -> Boolean: ...
    @winrt_commethod(13)
    def get_IsLeftButtonPressed(self) -> Boolean: ...
    @winrt_commethod(14)
    def get_IsMiddleButtonPressed(self) -> Boolean: ...
    @winrt_commethod(15)
    def get_IsPrimary(self) -> Boolean: ...
    @winrt_commethod(16)
    def get_IsRightButtonPressed(self) -> Boolean: ...
    @winrt_commethod(17)
    def get_IsXButton1Pressed(self) -> Boolean: ...
    @winrt_commethod(18)
    def get_IsXButton2Pressed(self) -> Boolean: ...
    @winrt_commethod(19)
    def get_MouseWheelDelta(self) -> Int32: ...
    @winrt_commethod(20)
    def get_Orientation(self) -> Single: ...
    @winrt_commethod(21)
    def get_PointerUpdateKind(self) -> win32more.Microsoft.UI.Input.PointerUpdateKind: ...
    @winrt_commethod(22)
    def get_Pressure(self) -> Single: ...
    @winrt_commethod(23)
    def get_TouchConfidence(self) -> Boolean: ...
    @winrt_commethod(24)
    def get_Twist(self) -> Single: ...
    @winrt_commethod(25)
    def get_XTilt(self) -> Single: ...
    @winrt_commethod(26)
    def get_YTilt(self) -> Single: ...
    ContactRect = property(get_ContactRect, None)
    IsBarrelButtonPressed = property(get_IsBarrelButtonPressed, None)
    IsCanceled = property(get_IsCanceled, None)
    IsEraser = property(get_IsEraser, None)
    IsHorizontalMouseWheel = property(get_IsHorizontalMouseWheel, None)
    IsInRange = property(get_IsInRange, None)
    IsInverted = property(get_IsInverted, None)
    IsLeftButtonPressed = property(get_IsLeftButtonPressed, None)
    IsMiddleButtonPressed = property(get_IsMiddleButtonPressed, None)
    IsPrimary = property(get_IsPrimary, None)
    IsRightButtonPressed = property(get_IsRightButtonPressed, None)
    IsXButton1Pressed = property(get_IsXButton1Pressed, None)
    IsXButton2Pressed = property(get_IsXButton2Pressed, None)
    MouseWheelDelta = property(get_MouseWheelDelta, None)
    Orientation = property(get_Orientation, None)
    PointerUpdateKind = property(get_PointerUpdateKind, None)
    Pressure = property(get_Pressure, None)
    TouchConfidence = property(get_TouchConfidence, None)
    Twist = property(get_Twist, None)
    XTilt = property(get_XTilt, None)
    YTilt = property(get_YTilt, None)
class IPointerPointTransform(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IPointerPointTransform'
    _iid_ = Guid('{db4791bc-994d-54c7-92ef-66ea1de9b43c}')
    @winrt_commethod(6)
    def get_Inverse(self) -> win32more.Microsoft.UI.Input.IPointerPointTransform: ...
    @winrt_commethod(7)
    def TryTransform(self, inPoint: win32more.Windows.Foundation.Point, outPoint: POINTER(win32more.Windows.Foundation.Point)) -> Boolean: ...
    @winrt_commethod(8)
    def TryTransformBounds(self, inRect: win32more.Windows.Foundation.Rect, outRect: POINTER(win32more.Windows.Foundation.Rect)) -> Boolean: ...
    Inverse = property(get_Inverse, None)
class IPointerPredictor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IPointerPredictor'
    _iid_ = Guid('{12c100ec-2100-565f-a60c-f1187f438828}')
    @winrt_commethod(6)
    def get_PredictionTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_PredictionTime(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def GetPredictedPoints(self, point: win32more.Microsoft.UI.Input.PointerPoint) -> ReceiveArray[win32more.Microsoft.UI.Input.PointerPoint]: ...
    PredictionTime = property(get_PredictionTime, put_PredictionTime)
class IPointerPredictorStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IPointerPredictorStatics'
    _iid_ = Guid('{78a8ef30-3e5c-55cd-8f85-65ac09b1a987}')
    @winrt_commethod(6)
    def CreateForInputPointerSource(self, inputPointerSource: win32more.Microsoft.UI.Input.InputPointerSource) -> win32more.Microsoft.UI.Input.PointerPredictor: ...
class IRightTappedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IRightTappedEventArgs'
    _iid_ = Guid('{8ff73b39-887e-50a4-8500-77953039dcb4}')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
class ITappedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.ITappedEventArgs'
    _iid_ = Guid('{c3a01bb5-6076-5e0f-871a-9d94a6a8f82b}')
    @winrt_commethod(6)
    def get_PointerDeviceType(self) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_commethod(7)
    def get_Position(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_TapCount(self) -> UInt32: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    TapCount = property(get_TapCount, None)
class IWindowRectChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IWindowRectChangedEventArgs'
    _iid_ = Guid('{8a885d28-d2d9-5dda-9848-cdf247771037}')
    @winrt_commethod(6)
    def get_PointerScreenPoint(self) -> win32more.Windows.Graphics.PointInt32: ...
    @winrt_commethod(7)
    def get_MoveSizeOperation(self) -> win32more.Microsoft.UI.Input.MoveSizeOperation: ...
    @winrt_commethod(8)
    def get_OldWindowRect(self) -> win32more.Windows.Graphics.RectInt32: ...
    @winrt_commethod(9)
    def get_NewWindowRect(self) -> win32more.Windows.Graphics.RectInt32: ...
    MoveSizeOperation = property(get_MoveSizeOperation, None)
    NewWindowRect = property(get_NewWindowRect, None)
    OldWindowRect = property(get_OldWindowRect, None)
    PointerScreenPoint = property(get_PointerScreenPoint, None)
class IWindowRectChangingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Input.IWindowRectChangingEventArgs'
    _iid_ = Guid('{db13ed3c-debc-5855-8d70-5936fd813457}')
    @winrt_commethod(6)
    def get_PointerScreenPoint(self) -> win32more.Windows.Graphics.PointInt32: ...
    @winrt_commethod(7)
    def get_MoveSizeOperation(self) -> win32more.Microsoft.UI.Input.MoveSizeOperation: ...
    @winrt_commethod(8)
    def get_OldWindowRect(self) -> win32more.Windows.Graphics.RectInt32: ...
    @winrt_commethod(9)
    def get_NewWindowRect(self) -> win32more.Windows.Graphics.RectInt32: ...
    @winrt_commethod(10)
    def put_NewWindowRect(self, value: win32more.Windows.Graphics.RectInt32) -> Void: ...
    @winrt_commethod(11)
    def get_AllowRectChange(self) -> Boolean: ...
    @winrt_commethod(12)
    def put_AllowRectChange(self, value: Boolean) -> Void: ...
    @winrt_commethod(13)
    def get_ShowWindow(self) -> Boolean: ...
    @winrt_commethod(14)
    def put_ShowWindow(self, value: Boolean) -> Void: ...
    AllowRectChange = property(get_AllowRectChange, put_AllowRectChange)
    MoveSizeOperation = property(get_MoveSizeOperation, None)
    NewWindowRect = property(get_NewWindowRect, put_NewWindowRect)
    OldWindowRect = property(get_OldWindowRect, None)
    PointerScreenPoint = property(get_PointerScreenPoint, None)
    ShowWindow = property(get_ShowWindow, put_ShowWindow)
class InputActivationListener(ComPtr):
    extends: win32more.Microsoft.UI.Input.InputObject
    default_interface: win32more.Microsoft.UI.Input.IInputActivationListener
    _classid_ = 'Microsoft.UI.Input.InputActivationListener'
    @winrt_mixinmethod
    def remove_InputActivationChanged(self: win32more.Microsoft.UI.Input.IInputActivationListener, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_InputActivationChanged(self: win32more.Microsoft.UI.Input.IInputActivationListener, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputActivationListener, win32more.Microsoft.UI.Input.InputActivationListenerActivationChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def get_State(self: win32more.Microsoft.UI.Input.IInputActivationListener) -> win32more.Microsoft.UI.Input.InputActivationState: ...
    @winrt_classmethod
    def GetForIsland(cls: win32more.Microsoft.UI.Input.IInputActivationListenerStatics2, island: win32more.Microsoft.UI.Content.ContentIsland) -> win32more.Microsoft.UI.Input.InputActivationListener: ...
    @winrt_classmethod
    def GetForWindowId(cls: win32more.Microsoft.UI.Input.IInputActivationListenerStatics, windowId: win32more.Microsoft.UI.WindowId) -> win32more.Microsoft.UI.Input.InputActivationListener: ...
    State = property(get_State, None)
    InputActivationChanged = event()
class InputActivationListenerActivationChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.IInputActivationListenerActivationChangedEventArgs
    _classid_ = 'Microsoft.UI.Input.InputActivationListenerActivationChangedEventArgs'
class InputActivationState(Enum, Int32):
    None_ = 0
    Deactivated = 1
    Activated = 2
class InputCursor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.UI.Input.IInputCursor
    _classid_ = 'Microsoft.UI.Input.InputCursor'
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateFromCoreCursor(cls: win32more.Microsoft.UI.Input.IInputCursorStatics, cursor: win32more.Windows.UI.Core.CoreCursor) -> win32more.Microsoft.UI.Input.InputCursor: ...
class InputCustomCursor(ComPtr):
    extends: win32more.Microsoft.UI.Input.InputCursor
    default_interface: win32more.Microsoft.UI.Input.IInputCustomCursor
    _classid_ = 'Microsoft.UI.Input.InputCustomCursor'
class InputDesktopNamedResourceCursor(ComPtr):
    extends: win32more.Microsoft.UI.Input.InputCursor
    default_interface: win32more.Microsoft.UI.Input.IInputDesktopNamedResourceCursor
    _classid_ = 'Microsoft.UI.Input.InputDesktopNamedResourceCursor'
    @winrt_mixinmethod
    def get_ModuleName(self: win32more.Microsoft.UI.Input.IInputDesktopNamedResourceCursor) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_ResourceName(self: win32more.Microsoft.UI.Input.IInputDesktopNamedResourceCursor) -> WinRT_String: ...
    @winrt_classmethod
    def Create(cls: win32more.Microsoft.UI.Input.IInputDesktopNamedResourceCursorStatics, resourceName: WinRT_String) -> win32more.Microsoft.UI.Input.InputDesktopNamedResourceCursor: ...
    @winrt_classmethod
    def CreateFromModule(cls: win32more.Microsoft.UI.Input.IInputDesktopNamedResourceCursorStatics, moduleName: WinRT_String, resourceName: WinRT_String) -> win32more.Microsoft.UI.Input.InputDesktopNamedResourceCursor: ...
    ModuleName = property(get_ModuleName, None)
    ResourceName = property(get_ResourceName, None)
class InputDesktopResourceCursor(ComPtr):
    extends: win32more.Microsoft.UI.Input.InputCursor
    default_interface: win32more.Microsoft.UI.Input.IInputDesktopResourceCursor
    _classid_ = 'Microsoft.UI.Input.InputDesktopResourceCursor'
    @winrt_mixinmethod
    def get_ResourceId(self: win32more.Microsoft.UI.Input.IInputDesktopResourceCursor) -> UInt32: ...
    @winrt_mixinmethod
    def get_ModuleName(self: win32more.Microsoft.UI.Input.IInputDesktopResourceCursor) -> WinRT_String: ...
    @winrt_classmethod
    def Create(cls: win32more.Microsoft.UI.Input.IInputDesktopResourceCursorStatics, resourceId: UInt32) -> win32more.Microsoft.UI.Input.InputDesktopResourceCursor: ...
    @winrt_classmethod
    def CreateFromModule(cls: win32more.Microsoft.UI.Input.IInputDesktopResourceCursorStatics, moduleName: WinRT_String, resourceId: UInt32) -> win32more.Microsoft.UI.Input.InputDesktopResourceCursor: ...
    ModuleName = property(get_ModuleName, None)
    ResourceId = property(get_ResourceId, None)
class InputFocusController(ComPtr):
    extends: win32more.Microsoft.UI.Input.InputObject
    default_interface: win32more.Microsoft.UI.Input.IInputFocusController
    _classid_ = 'Microsoft.UI.Input.InputFocusController'
    @winrt_mixinmethod
    def TrySetFocus(self: win32more.Microsoft.UI.Input.IInputFocusController) -> Boolean: ...
    @winrt_mixinmethod
    def add_GotFocus(self: win32more.Microsoft.UI.Input.IInputFocusController, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputFocusController, win32more.Microsoft.UI.Input.FocusChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_GotFocus(self: win32more.Microsoft.UI.Input.IInputFocusController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_LostFocus(self: win32more.Microsoft.UI.Input.IInputFocusController, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputFocusController, win32more.Microsoft.UI.Input.FocusChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LostFocus(self: win32more.Microsoft.UI.Input.IInputFocusController, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def DepartFocus(self: win32more.Microsoft.UI.Input.IInputFocusController2, request: win32more.Microsoft.UI.Input.FocusNavigationRequest) -> win32more.Microsoft.UI.Input.FocusNavigationResult: ...
    @winrt_mixinmethod
    def add_NavigateFocusRequested(self: win32more.Microsoft.UI.Input.IInputFocusController2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputFocusController, win32more.Microsoft.UI.Input.FocusNavigationRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_NavigateFocusRequested(self: win32more.Microsoft.UI.Input.IInputFocusController2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_HasFocus(self: win32more.Microsoft.UI.Input.IInputFocusController) -> Boolean: ...
    @winrt_classmethod
    def GetForIsland(cls: win32more.Microsoft.UI.Input.IInputFocusControllerStatics, island: win32more.Microsoft.UI.Content.ContentIsland) -> win32more.Microsoft.UI.Input.InputFocusController: ...
    HasFocus = property(get_HasFocus, None)
    GotFocus = event()
    LostFocus = event()
    NavigateFocusRequested = event()
class InputFocusNavigationHost(ComPtr):
    extends: win32more.Microsoft.UI.Input.InputObject
    default_interface: win32more.Microsoft.UI.Input.IInputFocusNavigationHost
    _classid_ = 'Microsoft.UI.Input.InputFocusNavigationHost'
    @winrt_mixinmethod
    def get_ContainsFocus(self: win32more.Microsoft.UI.Input.IInputFocusNavigationHost) -> Boolean: ...
    @winrt_mixinmethod
    def NavigateFocus(self: win32more.Microsoft.UI.Input.IInputFocusNavigationHost, request: win32more.Microsoft.UI.Input.FocusNavigationRequest) -> win32more.Microsoft.UI.Input.FocusNavigationResult: ...
    @winrt_mixinmethod
    def remove_DepartFocusRequested(self: win32more.Microsoft.UI.Input.IInputFocusNavigationHost, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_DepartFocusRequested(self: win32more.Microsoft.UI.Input.IInputFocusNavigationHost, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputFocusNavigationHost, win32more.Microsoft.UI.Input.FocusNavigationRequestEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def GetForSiteLink(cls: win32more.Microsoft.UI.Input.IInputFocusNavigationHostStatics2, contentSiteLink: win32more.Microsoft.UI.Content.IContentSiteLink) -> win32more.Microsoft.UI.Input.InputFocusNavigationHost: ...
    @winrt_classmethod
    def GetForSiteBridge(cls: win32more.Microsoft.UI.Input.IInputFocusNavigationHostStatics, site: win32more.Microsoft.UI.Content.IContentSiteBridge) -> win32more.Microsoft.UI.Input.InputFocusNavigationHost: ...
    ContainsFocus = property(get_ContainsFocus, None)
    DepartFocusRequested = event()
class InputKeyboardSource(ComPtr):
    extends: win32more.Microsoft.UI.Input.InputObject
    default_interface: win32more.Microsoft.UI.Input.IInputKeyboardSource
    _classid_ = 'Microsoft.UI.Input.InputKeyboardSource'
    @winrt_mixinmethod
    def remove_KeyDown(self: win32more.Microsoft.UI.Input.IInputKeyboardSource2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_CharacterReceived(self: win32more.Microsoft.UI.Input.IInputKeyboardSource2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputKeyboardSource, win32more.Microsoft.UI.Input.CharacterReceivedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CharacterReceived(self: win32more.Microsoft.UI.Input.IInputKeyboardSource2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ContextMenuKey(self: win32more.Microsoft.UI.Input.IInputKeyboardSource2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputKeyboardSource, win32more.Microsoft.UI.Input.ContextMenuKeyEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def GetCurrentKeyState(self: win32more.Microsoft.UI.Input.IInputKeyboardSource2, virtualKey: win32more.Windows.System.VirtualKey) -> win32more.Microsoft.UI.Input.VirtualKeyStates: ...
    @winrt_mixinmethod
    def add_KeyDown(self: win32more.Microsoft.UI.Input.IInputKeyboardSource2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputKeyboardSource, win32more.Microsoft.UI.Input.KeyEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ContextMenuKey(self: win32more.Microsoft.UI.Input.IInputKeyboardSource2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_KeyUp(self: win32more.Microsoft.UI.Input.IInputKeyboardSource2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputKeyboardSource, win32more.Microsoft.UI.Input.KeyEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_KeyUp(self: win32more.Microsoft.UI.Input.IInputKeyboardSource2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SystemKeyDown(self: win32more.Microsoft.UI.Input.IInputKeyboardSource2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputKeyboardSource, win32more.Microsoft.UI.Input.KeyEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_SystemKeyDown(self: win32more.Microsoft.UI.Input.IInputKeyboardSource2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def GetKeyState(self: win32more.Microsoft.UI.Input.IInputKeyboardSource2, virtualKey: win32more.Windows.System.VirtualKey) -> win32more.Microsoft.UI.Input.VirtualKeyStates: ...
    @winrt_mixinmethod
    def remove_SystemKeyUp(self: win32more.Microsoft.UI.Input.IInputKeyboardSource2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_SystemKeyUp(self: win32more.Microsoft.UI.Input.IInputKeyboardSource2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputKeyboardSource, win32more.Microsoft.UI.Input.KeyEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def GetForIsland(cls: win32more.Microsoft.UI.Input.IInputKeyboardSourceStatics2, island: win32more.Microsoft.UI.Content.ContentIsland) -> win32more.Microsoft.UI.Input.InputKeyboardSource: ...
    @winrt_classmethod
    def GetKeyStateForCurrentThread(cls: win32more.Microsoft.UI.Input.IInputKeyboardSourceStatics, virtualKey: win32more.Windows.System.VirtualKey) -> win32more.Windows.UI.Core.CoreVirtualKeyStates: ...
    CharacterReceived = event()
    ContextMenuKey = event()
    KeyDown = event()
    KeyUp = event()
    SystemKeyDown = event()
    SystemKeyUp = event()
class InputLightDismissAction(ComPtr):
    extends: win32more.Microsoft.UI.Input.InputObject
    default_interface: win32more.Microsoft.UI.Input.IInputLightDismissAction
    _classid_ = 'Microsoft.UI.Input.InputLightDismissAction'
    @winrt_mixinmethod
    def add_Dismissed(self: win32more.Microsoft.UI.Input.IInputLightDismissAction, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputLightDismissAction, win32more.Microsoft.UI.Input.InputLightDismissEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_Dismissed(self: win32more.Microsoft.UI.Input.IInputLightDismissAction, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetForWindowId(cls: win32more.Microsoft.UI.Input.IInputLightDismissActionStatics, windowId: win32more.Microsoft.UI.WindowId) -> win32more.Microsoft.UI.Input.InputLightDismissAction: ...
    Dismissed = event()
class InputLightDismissEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.IInputLightDismissEventArgs
    _classid_ = 'Microsoft.UI.Input.InputLightDismissEventArgs'
class InputNonClientPointerSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.IInputNonClientPointerSource
    _classid_ = 'Microsoft.UI.Input.InputNonClientPointerSource'
    @winrt_mixinmethod
    def remove_PointerPressed(self: win32more.Microsoft.UI.Input.IInputNonClientPointerSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def ClearRegionRects(self: win32more.Microsoft.UI.Input.IInputNonClientPointerSource, region: win32more.Microsoft.UI.Input.NonClientRegionKind) -> Void: ...
    @winrt_mixinmethod
    def GetRegionRects(self: win32more.Microsoft.UI.Input.IInputNonClientPointerSource, region: win32more.Microsoft.UI.Input.NonClientRegionKind) -> ReceiveArray[win32more.Windows.Graphics.RectInt32]: ...
    @winrt_mixinmethod
    def SetRegionRects(self: win32more.Microsoft.UI.Input.IInputNonClientPointerSource, region: win32more.Microsoft.UI.Input.NonClientRegionKind, rects: PassArray[win32more.Windows.Graphics.RectInt32]) -> Void: ...
    @winrt_mixinmethod
    def add_CaptionTapped(self: win32more.Microsoft.UI.Input.IInputNonClientPointerSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputNonClientPointerSource, win32more.Microsoft.UI.Input.NonClientCaptionTappedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_CaptionTapped(self: win32more.Microsoft.UI.Input.IInputNonClientPointerSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerEntered(self: win32more.Microsoft.UI.Input.IInputNonClientPointerSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputNonClientPointerSource, win32more.Microsoft.UI.Input.NonClientPointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerEntered(self: win32more.Microsoft.UI.Input.IInputNonClientPointerSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_DispatcherQueue(self: win32more.Microsoft.UI.Input.IInputNonClientPointerSource) -> win32more.Microsoft.UI.Dispatching.DispatcherQueue: ...
    @winrt_mixinmethod
    def remove_PointerExited(self: win32more.Microsoft.UI.Input.IInputNonClientPointerSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerMoved(self: win32more.Microsoft.UI.Input.IInputNonClientPointerSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputNonClientPointerSource, win32more.Microsoft.UI.Input.NonClientPointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerMoved(self: win32more.Microsoft.UI.Input.IInputNonClientPointerSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerPressed(self: win32more.Microsoft.UI.Input.IInputNonClientPointerSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputNonClientPointerSource, win32more.Microsoft.UI.Input.NonClientPointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def add_PointerExited(self: win32more.Microsoft.UI.Input.IInputNonClientPointerSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputNonClientPointerSource, win32more.Microsoft.UI.Input.NonClientPointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def add_PointerReleased(self: win32more.Microsoft.UI.Input.IInputNonClientPointerSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputNonClientPointerSource, win32more.Microsoft.UI.Input.NonClientPointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerReleased(self: win32more.Microsoft.UI.Input.IInputNonClientPointerSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_RegionsChanged(self: win32more.Microsoft.UI.Input.IInputNonClientPointerSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputNonClientPointerSource, win32more.Microsoft.UI.Input.NonClientRegionsChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_RegionsChanged(self: win32more.Microsoft.UI.Input.IInputNonClientPointerSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnteringMoveSize(self: win32more.Microsoft.UI.Input.IInputNonClientPointerSource2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputNonClientPointerSource, win32more.Microsoft.UI.Input.EnteringMoveSizeEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnteringMoveSize(self: win32more.Microsoft.UI.Input.IInputNonClientPointerSource2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_EnteredMoveSize(self: win32more.Microsoft.UI.Input.IInputNonClientPointerSource2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputNonClientPointerSource, win32more.Microsoft.UI.Input.EnteredMoveSizeEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_EnteredMoveSize(self: win32more.Microsoft.UI.Input.IInputNonClientPointerSource2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_WindowRectChanging(self: win32more.Microsoft.UI.Input.IInputNonClientPointerSource2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputNonClientPointerSource, win32more.Microsoft.UI.Input.WindowRectChangingEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_WindowRectChanging(self: win32more.Microsoft.UI.Input.IInputNonClientPointerSource2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_WindowRectChanged(self: win32more.Microsoft.UI.Input.IInputNonClientPointerSource2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputNonClientPointerSource, win32more.Microsoft.UI.Input.WindowRectChangedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_WindowRectChanged(self: win32more.Microsoft.UI.Input.IInputNonClientPointerSource2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ExitedMoveSize(self: win32more.Microsoft.UI.Input.IInputNonClientPointerSource2, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputNonClientPointerSource, win32more.Microsoft.UI.Input.ExitedMoveSizeEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ExitedMoveSize(self: win32more.Microsoft.UI.Input.IInputNonClientPointerSource2, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def ClearAllRegionRects(self: win32more.Microsoft.UI.Input.IInputNonClientPointerSource) -> Void: ...
    @winrt_classmethod
    def GetForWindowId(cls: win32more.Microsoft.UI.Input.IInputNonClientPointerSourceStatics, windowId: win32more.Microsoft.UI.WindowId) -> win32more.Microsoft.UI.Input.InputNonClientPointerSource: ...
    DispatcherQueue = property(get_DispatcherQueue, None)
    CaptionTapped = event()
    PointerEntered = event()
    PointerMoved = event()
    PointerPressed = event()
    PointerExited = event()
    PointerReleased = event()
    RegionsChanged = event()
    EnteringMoveSize = event()
    EnteredMoveSize = event()
    WindowRectChanging = event()
    WindowRectChanged = event()
    ExitedMoveSize = event()
class InputObject(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.IInputObject
    _classid_ = 'Microsoft.UI.Input.InputObject'
    @winrt_mixinmethod
    def get_DispatcherQueue(self: win32more.Microsoft.UI.Input.IInputObject) -> win32more.Microsoft.UI.Dispatching.DispatcherQueue: ...
    DispatcherQueue = property(get_DispatcherQueue, None)
class InputPointerSource(ComPtr):
    extends: win32more.Microsoft.UI.Input.InputObject
    default_interface: win32more.Microsoft.UI.Input.IInputPointerSource
    _classid_ = 'Microsoft.UI.Input.InputPointerSource'
    @winrt_mixinmethod
    def add_PointerEntered(self: win32more.Microsoft.UI.Input.IInputPointerSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputPointerSource, win32more.Microsoft.UI.Input.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def get_DeviceKinds(self: win32more.Microsoft.UI.Input.IInputPointerSource) -> win32more.Microsoft.UI.Input.InputPointerSourceDeviceKinds: ...
    @winrt_mixinmethod
    def add_PointerCaptureLost(self: win32more.Microsoft.UI.Input.IInputPointerSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputPointerSource, win32more.Microsoft.UI.Input.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerCaptureLost(self: win32more.Microsoft.UI.Input.IInputPointerSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def put_Cursor(self: win32more.Microsoft.UI.Input.IInputPointerSource, value: win32more.Microsoft.UI.Input.InputCursor) -> Void: ...
    @winrt_mixinmethod
    def remove_PointerEntered(self: win32more.Microsoft.UI.Input.IInputPointerSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerExited(self: win32more.Microsoft.UI.Input.IInputPointerSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputPointerSource, win32more.Microsoft.UI.Input.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerExited(self: win32more.Microsoft.UI.Input.IInputPointerSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerMoved(self: win32more.Microsoft.UI.Input.IInputPointerSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputPointerSource, win32more.Microsoft.UI.Input.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerMoved(self: win32more.Microsoft.UI.Input.IInputPointerSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerPressed(self: win32more.Microsoft.UI.Input.IInputPointerSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputPointerSource, win32more.Microsoft.UI.Input.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerPressed(self: win32more.Microsoft.UI.Input.IInputPointerSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerReleased(self: win32more.Microsoft.UI.Input.IInputPointerSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputPointerSource, win32more.Microsoft.UI.Input.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerReleased(self: win32more.Microsoft.UI.Input.IInputPointerSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerRoutedAway(self: win32more.Microsoft.UI.Input.IInputPointerSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputPointerSource, win32more.Microsoft.UI.Input.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerRoutedAway(self: win32more.Microsoft.UI.Input.IInputPointerSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerRoutedReleased(self: win32more.Microsoft.UI.Input.IInputPointerSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputPointerSource, win32more.Microsoft.UI.Input.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerRoutedReleased(self: win32more.Microsoft.UI.Input.IInputPointerSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerRoutedTo(self: win32more.Microsoft.UI.Input.IInputPointerSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputPointerSource, win32more.Microsoft.UI.Input.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerRoutedTo(self: win32more.Microsoft.UI.Input.IInputPointerSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerWheelChanged(self: win32more.Microsoft.UI.Input.IInputPointerSource, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Input.InputPointerSource, win32more.Microsoft.UI.Input.PointerEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerWheelChanged(self: win32more.Microsoft.UI.Input.IInputPointerSource, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_Cursor(self: win32more.Microsoft.UI.Input.IInputPointerSource) -> win32more.Microsoft.UI.Input.InputCursor: ...
    @winrt_classmethod
    def GetForIsland(cls: win32more.Microsoft.UI.Input.IInputPointerSourceStatics, island: win32more.Microsoft.UI.Content.ContentIsland) -> win32more.Microsoft.UI.Input.InputPointerSource: ...
    Cursor = property(get_Cursor, put_Cursor)
    DeviceKinds = property(get_DeviceKinds, None)
    PointerEntered = event()
    PointerCaptureLost = event()
    PointerExited = event()
    PointerMoved = event()
    PointerPressed = event()
    PointerReleased = event()
    PointerRoutedAway = event()
    PointerRoutedReleased = event()
    PointerRoutedTo = event()
    PointerWheelChanged = event()
class InputPointerSourceDeviceKinds(Enum, UInt32):
    None_ = 0
    Touch = 1
    Pen = 2
    Mouse = 4
class InputPreTranslateKeyboardSource(ComPtr):
    extends: win32more.Microsoft.UI.Input.InputObject
    default_interface: win32more.Microsoft.UI.Input.IInputPreTranslateKeyboardSource
    _classid_ = 'Microsoft.UI.Input.InputPreTranslateKeyboardSource'
    @winrt_classmethod
    def GetForIsland(cls: win32more.Microsoft.UI.Input.IInputPreTranslateKeyboardSourceStatics, island: win32more.Microsoft.UI.Content.ContentIsland) -> win32more.Microsoft.UI.Input.InputPreTranslateKeyboardSource: ...
class InputSystemCursor(ComPtr):
    extends: win32more.Microsoft.UI.Input.InputCursor
    default_interface: win32more.Microsoft.UI.Input.IInputSystemCursor
    _classid_ = 'Microsoft.UI.Input.InputSystemCursor'
    @winrt_mixinmethod
    def get_CursorShape(self: win32more.Microsoft.UI.Input.IInputSystemCursor) -> win32more.Microsoft.UI.Input.InputSystemCursorShape: ...
    @winrt_classmethod
    def Create(cls: win32more.Microsoft.UI.Input.IInputSystemCursorStatics, type: win32more.Microsoft.UI.Input.InputSystemCursorShape) -> win32more.Microsoft.UI.Input.InputSystemCursor: ...
    CursorShape = property(get_CursorShape, None)
class InputSystemCursorShape(Enum, Int32):
    Arrow = 0
    Cross = 1
    Hand = 3
    Help = 4
    IBeam = 5
    SizeAll = 6
    SizeNortheastSouthwest = 7
    SizeNorthSouth = 8
    SizeNorthwestSoutheast = 9
    SizeWestEast = 10
    UniversalNo = 11
    UpArrow = 12
    Wait = 13
    Pin = 14
    Person = 15
    AppStarting = 16
class KeyEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.IKeyEventArgs
    _classid_ = 'Microsoft.UI.Input.KeyEventArgs'
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Microsoft.UI.Input.IKeyEventArgs) -> UInt64: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.UI.Input.IKeyEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_KeyStatus(self: win32more.Microsoft.UI.Input.IKeyEventArgs) -> win32more.Microsoft.UI.Input.PhysicalKeyStatus: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.UI.Input.IKeyEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def get_VirtualKey(self: win32more.Microsoft.UI.Input.IKeyEventArgs) -> win32more.Windows.System.VirtualKey: ...
    Handled = property(get_Handled, put_Handled)
    KeyStatus = property(get_KeyStatus, None)
    Timestamp = property(get_Timestamp, None)
    VirtualKey = property(get_VirtualKey, None)
class ManipulationCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.IManipulationCompletedEventArgs
    _classid_ = 'Microsoft.UI.Input.ManipulationCompletedEventArgs'
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Microsoft.UI.Input.IManipulationCompletedEventArgs) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Cumulative(self: win32more.Microsoft.UI.Input.IManipulationCompletedEventArgs) -> win32more.Microsoft.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Microsoft.UI.Input.IManipulationCompletedEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Velocities(self: win32more.Microsoft.UI.Input.IManipulationCompletedEventArgs) -> win32more.Microsoft.UI.Input.ManipulationVelocities: ...
    Cumulative = property(get_Cumulative, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    Velocities = property(get_Velocities, None)
class ManipulationDelta(Structure):
    Translation: win32more.Windows.Foundation.Point
    Scale: Single
    Rotation: Single
    Expansion: Single
class ManipulationInertiaStartingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.IManipulationInertiaStartingEventArgs
    _classid_ = 'Microsoft.UI.Input.ManipulationInertiaStartingEventArgs'
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Microsoft.UI.Input.IManipulationInertiaStartingEventArgs) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Delta(self: win32more.Microsoft.UI.Input.IManipulationInertiaStartingEventArgs) -> win32more.Microsoft.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def get_Cumulative(self: win32more.Microsoft.UI.Input.IManipulationInertiaStartingEventArgs) -> win32more.Microsoft.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Microsoft.UI.Input.IManipulationInertiaStartingEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Velocities(self: win32more.Microsoft.UI.Input.IManipulationInertiaStartingEventArgs) -> win32more.Microsoft.UI.Input.ManipulationVelocities: ...
    Cumulative = property(get_Cumulative, None)
    Delta = property(get_Delta, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    Velocities = property(get_Velocities, None)
class ManipulationStartedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.IManipulationStartedEventArgs
    _classid_ = 'Microsoft.UI.Input.ManipulationStartedEventArgs'
    @winrt_mixinmethod
    def get_Position(self: win32more.Microsoft.UI.Input.IManipulationStartedEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Microsoft.UI.Input.IManipulationStartedEventArgs) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Cumulative(self: win32more.Microsoft.UI.Input.IManipulationStartedEventArgs) -> win32more.Microsoft.UI.Input.ManipulationDelta: ...
    Cumulative = property(get_Cumulative, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
class ManipulationUpdatedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.IManipulationUpdatedEventArgs
    _classid_ = 'Microsoft.UI.Input.ManipulationUpdatedEventArgs'
    @winrt_mixinmethod
    def get_Delta(self: win32more.Microsoft.UI.Input.IManipulationUpdatedEventArgs) -> win32more.Microsoft.UI.Input.ManipulationDelta: ...
    @winrt_mixinmethod
    def get_Velocities(self: win32more.Microsoft.UI.Input.IManipulationUpdatedEventArgs) -> win32more.Microsoft.UI.Input.ManipulationVelocities: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Microsoft.UI.Input.IManipulationUpdatedEventArgs) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Microsoft.UI.Input.IManipulationUpdatedEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Cumulative(self: win32more.Microsoft.UI.Input.IManipulationUpdatedEventArgs) -> win32more.Microsoft.UI.Input.ManipulationDelta: ...
    Cumulative = property(get_Cumulative, None)
    Delta = property(get_Delta, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    Velocities = property(get_Velocities, None)
class ManipulationVelocities(Structure):
    Linear: win32more.Windows.Foundation.Point
    Angular: Single
    Expansion: Single
class MouseWheelParameters(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.IMouseWheelParameters
    _classid_ = 'Microsoft.UI.Input.MouseWheelParameters'
    @winrt_mixinmethod
    def put_CharTranslation(self: win32more.Microsoft.UI.Input.IMouseWheelParameters, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_DeltaScale(self: win32more.Microsoft.UI.Input.IMouseWheelParameters) -> Single: ...
    @winrt_mixinmethod
    def get_CharTranslation(self: win32more.Microsoft.UI.Input.IMouseWheelParameters) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_DeltaScale(self: win32more.Microsoft.UI.Input.IMouseWheelParameters, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_DeltaRotationAngle(self: win32more.Microsoft.UI.Input.IMouseWheelParameters) -> Single: ...
    @winrt_mixinmethod
    def put_DeltaRotationAngle(self: win32more.Microsoft.UI.Input.IMouseWheelParameters, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_PageTranslation(self: win32more.Microsoft.UI.Input.IMouseWheelParameters) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_PageTranslation(self: win32more.Microsoft.UI.Input.IMouseWheelParameters, value: win32more.Windows.Foundation.Point) -> Void: ...
    CharTranslation = property(get_CharTranslation, put_CharTranslation)
    DeltaRotationAngle = property(get_DeltaRotationAngle, put_DeltaRotationAngle)
    DeltaScale = property(get_DeltaScale, put_DeltaScale)
    PageTranslation = property(get_PageTranslation, put_PageTranslation)
class MoveSizeOperation(Enum, Int32):
    Move = 0
    SizeBottom = 1
    SizeBottomLeft = 2
    SizeBottomRight = 3
    SizeLeft = 4
    SizeRight = 5
    SizeTop = 6
    SizeTopLeft = 7
    SizeTopRight = 8
class NonClientCaptionTappedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.INonClientCaptionTappedEventArgs
    _classid_ = 'Microsoft.UI.Input.NonClientCaptionTappedEventArgs'
    @winrt_mixinmethod
    def get_Point(self: win32more.Microsoft.UI.Input.INonClientCaptionTappedEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Microsoft.UI.Input.INonClientCaptionTappedEventArgs) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    Point = property(get_Point, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
class NonClientPointerEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.INonClientPointerEventArgs
    _classid_ = 'Microsoft.UI.Input.NonClientPointerEventArgs'
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Microsoft.UI.Input.INonClientPointerEventArgs) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Point(self: win32more.Microsoft.UI.Input.INonClientPointerEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_RegionKind(self: win32more.Microsoft.UI.Input.INonClientPointerEventArgs) -> win32more.Microsoft.UI.Input.NonClientRegionKind: ...
    @winrt_mixinmethod
    def get_IsPointInRegion(self: win32more.Microsoft.UI.Input.INonClientPointerEventArgs) -> Boolean: ...
    IsPointInRegion = property(get_IsPointInRegion, None)
    Point = property(get_Point, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    RegionKind = property(get_RegionKind, None)
class NonClientRegionKind(Enum, Int32):
    Close = 0
    Maximize = 1
    Minimize = 2
    Icon = 3
    Caption = 4
    TopBorder = 5
    LeftBorder = 6
    BottomBorder = 7
    RightBorder = 8
    Passthrough = 9
class NonClientRegionsChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.INonClientRegionsChangedEventArgs
    _classid_ = 'Microsoft.UI.Input.NonClientRegionsChangedEventArgs'
    @winrt_mixinmethod
    def get_ChangedRegions(self: win32more.Microsoft.UI.Input.INonClientRegionsChangedEventArgs) -> ReceiveArray[win32more.Microsoft.UI.Input.NonClientRegionKind]: ...
    ChangedRegions = property(get_ChangedRegions, None)
class PhysicalKeyStatus(Structure):
    RepeatCount: UInt32
    ScanCode: UInt32
    IsExtendedKey: Boolean
    IsMenuKeyDown: Boolean
    WasKeyDown: Boolean
    IsKeyReleased: Boolean
class PointerDeviceType(Enum, Int32):
    Touch = 0
    Pen = 1
    Mouse = 2
    Touchpad = 3
class PointerEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.IPointerEventArgs
    _classid_ = 'Microsoft.UI.Input.PointerEventArgs'
    @winrt_mixinmethod
    def GetIntermediatePoints(self: win32more.Microsoft.UI.Input.IPointerEventArgs) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Input.PointerPoint]: ...
    @winrt_mixinmethod
    def get_Handled(self: win32more.Microsoft.UI.Input.IPointerEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_Handled(self: win32more.Microsoft.UI.Input.IPointerEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_KeyModifiers(self: win32more.Microsoft.UI.Input.IPointerEventArgs) -> win32more.Windows.System.VirtualKeyModifiers: ...
    @winrt_mixinmethod
    def GetIntermediateTransformedPoints(self: win32more.Microsoft.UI.Input.IPointerEventArgs, transform: win32more.Microsoft.UI.Input.IPointerPointTransform) -> win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Input.PointerPoint]: ...
    @winrt_mixinmethod
    def get_CurrentPoint(self: win32more.Microsoft.UI.Input.IPointerEventArgs) -> win32more.Microsoft.UI.Input.PointerPoint: ...
    CurrentPoint = property(get_CurrentPoint, None)
    Handled = property(get_Handled, put_Handled)
    KeyModifiers = property(get_KeyModifiers, None)
class PointerPoint(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.IPointerPoint
    _classid_ = 'Microsoft.UI.Input.PointerPoint'
    @winrt_mixinmethod
    def get_IsInContact(self: win32more.Microsoft.UI.Input.IPointerPoint) -> Boolean: ...
    @winrt_mixinmethod
    def get_FrameId(self: win32more.Microsoft.UI.Input.IPointerPoint) -> UInt32: ...
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Microsoft.UI.Input.IPointerPoint) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_PointerId(self: win32more.Microsoft.UI.Input.IPointerPoint) -> UInt32: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Microsoft.UI.Input.IPointerPoint) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Properties(self: win32more.Microsoft.UI.Input.IPointerPoint) -> win32more.Microsoft.UI.Input.PointerPointProperties: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Microsoft.UI.Input.IPointerPoint) -> UInt64: ...
    @winrt_mixinmethod
    def GetTransformedPoint(self: win32more.Microsoft.UI.Input.IPointerPoint, transform: win32more.Microsoft.UI.Input.IPointerPointTransform) -> win32more.Microsoft.UI.Input.PointerPoint: ...
    FrameId = property(get_FrameId, None)
    IsInContact = property(get_IsInContact, None)
    PointerDeviceType = property(get_PointerDeviceType, None)
    PointerId = property(get_PointerId, None)
    Position = property(get_Position, None)
    Properties = property(get_Properties, None)
    Timestamp = property(get_Timestamp, None)
class PointerPointProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.IPointerPointProperties
    _classid_ = 'Microsoft.UI.Input.PointerPointProperties'
    @winrt_mixinmethod
    def get_IsInRange(self: win32more.Microsoft.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsBarrelButtonPressed(self: win32more.Microsoft.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsCanceled(self: win32more.Microsoft.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsEraser(self: win32more.Microsoft.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsHorizontalMouseWheel(self: win32more.Microsoft.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_ContactRect(self: win32more.Microsoft.UI.Input.IPointerPointProperties) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_IsInverted(self: win32more.Microsoft.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsLeftButtonPressed(self: win32more.Microsoft.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsMiddleButtonPressed(self: win32more.Microsoft.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsPrimary(self: win32more.Microsoft.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsRightButtonPressed(self: win32more.Microsoft.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsXButton1Pressed(self: win32more.Microsoft.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsXButton2Pressed(self: win32more.Microsoft.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_MouseWheelDelta(self: win32more.Microsoft.UI.Input.IPointerPointProperties) -> Int32: ...
    @winrt_mixinmethod
    def get_Orientation(self: win32more.Microsoft.UI.Input.IPointerPointProperties) -> Single: ...
    @winrt_mixinmethod
    def get_PointerUpdateKind(self: win32more.Microsoft.UI.Input.IPointerPointProperties) -> win32more.Microsoft.UI.Input.PointerUpdateKind: ...
    @winrt_mixinmethod
    def get_Pressure(self: win32more.Microsoft.UI.Input.IPointerPointProperties) -> Single: ...
    @winrt_mixinmethod
    def get_TouchConfidence(self: win32more.Microsoft.UI.Input.IPointerPointProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_Twist(self: win32more.Microsoft.UI.Input.IPointerPointProperties) -> Single: ...
    @winrt_mixinmethod
    def get_XTilt(self: win32more.Microsoft.UI.Input.IPointerPointProperties) -> Single: ...
    @winrt_mixinmethod
    def get_YTilt(self: win32more.Microsoft.UI.Input.IPointerPointProperties) -> Single: ...
    ContactRect = property(get_ContactRect, None)
    IsBarrelButtonPressed = property(get_IsBarrelButtonPressed, None)
    IsCanceled = property(get_IsCanceled, None)
    IsEraser = property(get_IsEraser, None)
    IsHorizontalMouseWheel = property(get_IsHorizontalMouseWheel, None)
    IsInRange = property(get_IsInRange, None)
    IsInverted = property(get_IsInverted, None)
    IsLeftButtonPressed = property(get_IsLeftButtonPressed, None)
    IsMiddleButtonPressed = property(get_IsMiddleButtonPressed, None)
    IsPrimary = property(get_IsPrimary, None)
    IsRightButtonPressed = property(get_IsRightButtonPressed, None)
    IsXButton1Pressed = property(get_IsXButton1Pressed, None)
    IsXButton2Pressed = property(get_IsXButton2Pressed, None)
    MouseWheelDelta = property(get_MouseWheelDelta, None)
    Orientation = property(get_Orientation, None)
    PointerUpdateKind = property(get_PointerUpdateKind, None)
    Pressure = property(get_Pressure, None)
    TouchConfidence = property(get_TouchConfidence, None)
    Twist = property(get_Twist, None)
    XTilt = property(get_XTilt, None)
    YTilt = property(get_YTilt, None)
class PointerPredictor(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.UI.Input.IPointerPredictor
    _classid_ = 'Microsoft.UI.Input.PointerPredictor'
    @winrt_mixinmethod
    def GetPredictedPoints(self: win32more.Microsoft.UI.Input.IPointerPredictor, point: win32more.Microsoft.UI.Input.PointerPoint) -> ReceiveArray[win32more.Microsoft.UI.Input.PointerPoint]: ...
    @winrt_mixinmethod
    def put_PredictionTime(self: win32more.Microsoft.UI.Input.IPointerPredictor, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_PredictionTime(self: win32more.Microsoft.UI.Input.IPointerPredictor) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def CreateForInputPointerSource(cls: win32more.Microsoft.UI.Input.IPointerPredictorStatics, inputPointerSource: win32more.Microsoft.UI.Input.InputPointerSource) -> win32more.Microsoft.UI.Input.PointerPredictor: ...
    PredictionTime = property(get_PredictionTime, put_PredictionTime)
class PointerUpdateKind(Enum, Int32):
    Other = 0
    LeftButtonPressed = 1
    LeftButtonReleased = 2
    RightButtonPressed = 3
    RightButtonReleased = 4
    MiddleButtonPressed = 5
    MiddleButtonReleased = 6
    XButton1Pressed = 7
    XButton1Released = 8
    XButton2Pressed = 9
    XButton2Released = 10
class RightTappedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.IRightTappedEventArgs
    _classid_ = 'Microsoft.UI.Input.RightTappedEventArgs'
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Microsoft.UI.Input.IRightTappedEventArgs) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Microsoft.UI.Input.IRightTappedEventArgs) -> win32more.Windows.Foundation.Point: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
class TappedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.ITappedEventArgs
    _classid_ = 'Microsoft.UI.Input.TappedEventArgs'
    @winrt_mixinmethod
    def get_PointerDeviceType(self: win32more.Microsoft.UI.Input.ITappedEventArgs) -> win32more.Microsoft.UI.Input.PointerDeviceType: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Microsoft.UI.Input.ITappedEventArgs) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_TapCount(self: win32more.Microsoft.UI.Input.ITappedEventArgs) -> UInt32: ...
    PointerDeviceType = property(get_PointerDeviceType, None)
    Position = property(get_Position, None)
    TapCount = property(get_TapCount, None)
class VirtualKeyStates(Enum, UInt32):
    None_ = 0
    Down = 1
    Locked = 2
class WindowRectChangedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.IWindowRectChangedEventArgs
    _classid_ = 'Microsoft.UI.Input.WindowRectChangedEventArgs'
    @winrt_mixinmethod
    def get_PointerScreenPoint(self: win32more.Microsoft.UI.Input.IWindowRectChangedEventArgs) -> win32more.Windows.Graphics.PointInt32: ...
    @winrt_mixinmethod
    def get_MoveSizeOperation(self: win32more.Microsoft.UI.Input.IWindowRectChangedEventArgs) -> win32more.Microsoft.UI.Input.MoveSizeOperation: ...
    @winrt_mixinmethod
    def get_OldWindowRect(self: win32more.Microsoft.UI.Input.IWindowRectChangedEventArgs) -> win32more.Windows.Graphics.RectInt32: ...
    @winrt_mixinmethod
    def get_NewWindowRect(self: win32more.Microsoft.UI.Input.IWindowRectChangedEventArgs) -> win32more.Windows.Graphics.RectInt32: ...
    MoveSizeOperation = property(get_MoveSizeOperation, None)
    NewWindowRect = property(get_NewWindowRect, None)
    OldWindowRect = property(get_OldWindowRect, None)
    PointerScreenPoint = property(get_PointerScreenPoint, None)
class WindowRectChangingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Input.IWindowRectChangingEventArgs
    _classid_ = 'Microsoft.UI.Input.WindowRectChangingEventArgs'
    @winrt_mixinmethod
    def get_MoveSizeOperation(self: win32more.Microsoft.UI.Input.IWindowRectChangingEventArgs) -> win32more.Microsoft.UI.Input.MoveSizeOperation: ...
    @winrt_mixinmethod
    def get_PointerScreenPoint(self: win32more.Microsoft.UI.Input.IWindowRectChangingEventArgs) -> win32more.Windows.Graphics.PointInt32: ...
    @winrt_mixinmethod
    def get_OldWindowRect(self: win32more.Microsoft.UI.Input.IWindowRectChangingEventArgs) -> win32more.Windows.Graphics.RectInt32: ...
    @winrt_mixinmethod
    def get_NewWindowRect(self: win32more.Microsoft.UI.Input.IWindowRectChangingEventArgs) -> win32more.Windows.Graphics.RectInt32: ...
    @winrt_mixinmethod
    def put_NewWindowRect(self: win32more.Microsoft.UI.Input.IWindowRectChangingEventArgs, value: win32more.Windows.Graphics.RectInt32) -> Void: ...
    @winrt_mixinmethod
    def get_AllowRectChange(self: win32more.Microsoft.UI.Input.IWindowRectChangingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_AllowRectChange(self: win32more.Microsoft.UI.Input.IWindowRectChangingEventArgs, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ShowWindow(self: win32more.Microsoft.UI.Input.IWindowRectChangingEventArgs) -> Boolean: ...
    @winrt_mixinmethod
    def put_ShowWindow(self: win32more.Microsoft.UI.Input.IWindowRectChangingEventArgs, value: Boolean) -> Void: ...
    AllowRectChange = property(get_AllowRectChange, put_AllowRectChange)
    MoveSizeOperation = property(get_MoveSizeOperation, None)
    NewWindowRect = property(get_NewWindowRect, put_NewWindowRect)
    OldWindowRect = property(get_OldWindowRect, None)
    PointerScreenPoint = property(get_PointerScreenPoint, None)
    ShowWindow = property(get_ShowWindow, put_ShowWindow)


make_ready(__name__)
