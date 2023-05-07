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
import Windows.Foundation
import Windows.Foundation.Collections
import Windows.Foundation.Numerics
import Windows.Storage.Streams
import Windows.UI
import Windows.UI.Core
import Windows.UI.Input
import Windows.UI.Input.Inking
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
HandwritingLineHeight = Int32
HandwritingLineHeight_Small: HandwritingLineHeight = 0
HandwritingLineHeight_Medium: HandwritingLineHeight = 1
HandwritingLineHeight_Large: HandwritingLineHeight = 2
class IInkDrawingAttributes(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkDrawingAttributes'
    _iid_ = Guid('{97a2176c-6774-48ad-84f0-48f5a9be74f9}')
    @winrt_commethod(6)
    def get_Color(self: Windows.UI.Input.Inking.IInkDrawingAttributes) -> Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_Color(self: Windows.UI.Input.Inking.IInkDrawingAttributes, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(8)
    def get_PenTip(self: Windows.UI.Input.Inking.IInkDrawingAttributes) -> Windows.UI.Input.Inking.PenTipShape: ...
    @winrt_commethod(9)
    def put_PenTip(self: Windows.UI.Input.Inking.IInkDrawingAttributes, value: Windows.UI.Input.Inking.PenTipShape) -> Void: ...
    @winrt_commethod(10)
    def get_Size(self: Windows.UI.Input.Inking.IInkDrawingAttributes) -> Windows.Foundation.Size: ...
    @winrt_commethod(11)
    def put_Size(self: Windows.UI.Input.Inking.IInkDrawingAttributes, value: Windows.Foundation.Size) -> Void: ...
    @winrt_commethod(12)
    def get_IgnorePressure(self: Windows.UI.Input.Inking.IInkDrawingAttributes) -> Boolean: ...
    @winrt_commethod(13)
    def put_IgnorePressure(self: Windows.UI.Input.Inking.IInkDrawingAttributes, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_FitToCurve(self: Windows.UI.Input.Inking.IInkDrawingAttributes) -> Boolean: ...
    @winrt_commethod(15)
    def put_FitToCurve(self: Windows.UI.Input.Inking.IInkDrawingAttributes, value: Boolean) -> Void: ...
    Color = property(get_Color, put_Color)
    PenTip = property(get_PenTip, put_PenTip)
    Size = property(get_Size, put_Size)
    IgnorePressure = property(get_IgnorePressure, put_IgnorePressure)
    FitToCurve = property(get_FitToCurve, put_FitToCurve)
class IInkDrawingAttributes2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkDrawingAttributes2'
    _iid_ = Guid('{7cab6508-8ec4-42fd-a5a5-e4b7d1d5316d}')
    @winrt_commethod(6)
    def get_PenTipTransform(self: Windows.UI.Input.Inking.IInkDrawingAttributes2) -> Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_commethod(7)
    def put_PenTipTransform(self: Windows.UI.Input.Inking.IInkDrawingAttributes2, value: Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    @winrt_commethod(8)
    def get_DrawAsHighlighter(self: Windows.UI.Input.Inking.IInkDrawingAttributes2) -> Boolean: ...
    @winrt_commethod(9)
    def put_DrawAsHighlighter(self: Windows.UI.Input.Inking.IInkDrawingAttributes2, value: Boolean) -> Void: ...
    PenTipTransform = property(get_PenTipTransform, put_PenTipTransform)
    DrawAsHighlighter = property(get_DrawAsHighlighter, put_DrawAsHighlighter)
class IInkDrawingAttributes3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkDrawingAttributes3'
    _iid_ = Guid('{72020002-7d5b-4690-8af4-e664cbe2b74f}')
    @winrt_commethod(6)
    def get_Kind(self: Windows.UI.Input.Inking.IInkDrawingAttributes3) -> Windows.UI.Input.Inking.InkDrawingAttributesKind: ...
    @winrt_commethod(7)
    def get_PencilProperties(self: Windows.UI.Input.Inking.IInkDrawingAttributes3) -> Windows.UI.Input.Inking.InkDrawingAttributesPencilProperties: ...
    Kind = property(get_Kind, None)
    PencilProperties = property(get_PencilProperties, None)
class IInkDrawingAttributes4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkDrawingAttributes4'
    _iid_ = Guid('{ef65dc25-9f19-456d-91a3-bc3a3d91c5fb}')
    @winrt_commethod(6)
    def get_IgnoreTilt(self: Windows.UI.Input.Inking.IInkDrawingAttributes4) -> Boolean: ...
    @winrt_commethod(7)
    def put_IgnoreTilt(self: Windows.UI.Input.Inking.IInkDrawingAttributes4, value: Boolean) -> Void: ...
    IgnoreTilt = property(get_IgnoreTilt, put_IgnoreTilt)
class IInkDrawingAttributes5(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkDrawingAttributes5'
    _iid_ = Guid('{d11aa0bb-0775-4852-ae64-41143a7ae6c9}')
    @winrt_commethod(6)
    def get_ModelerAttributes(self: Windows.UI.Input.Inking.IInkDrawingAttributes5) -> Windows.UI.Input.Inking.InkModelerAttributes: ...
    ModelerAttributes = property(get_ModelerAttributes, None)
class IInkDrawingAttributesPencilProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkDrawingAttributesPencilProperties'
    _iid_ = Guid('{4f2534cb-2d86-41bb-b0e8-e4c2a0253c52}')
    @winrt_commethod(6)
    def get_Opacity(self: Windows.UI.Input.Inking.IInkDrawingAttributesPencilProperties) -> Double: ...
    @winrt_commethod(7)
    def put_Opacity(self: Windows.UI.Input.Inking.IInkDrawingAttributesPencilProperties, value: Double) -> Void: ...
    Opacity = property(get_Opacity, put_Opacity)
class IInkDrawingAttributesStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkDrawingAttributesStatics'
    _iid_ = Guid('{f731e03f-1a65-4862-96cb-6e1665e17f6d}')
    @winrt_commethod(6)
    def CreateForPencil(self: Windows.UI.Input.Inking.IInkDrawingAttributesStatics) -> Windows.UI.Input.Inking.InkDrawingAttributes: ...
class IInkInputConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkInputConfiguration'
    _iid_ = Guid('{93a68dc4-0b7b-49d7-b34f-9901e524dcf2}')
    @winrt_commethod(6)
    def get_IsPrimaryBarrelButtonInputEnabled(self: Windows.UI.Input.Inking.IInkInputConfiguration) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsPrimaryBarrelButtonInputEnabled(self: Windows.UI.Input.Inking.IInkInputConfiguration, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_IsEraserInputEnabled(self: Windows.UI.Input.Inking.IInkInputConfiguration) -> Boolean: ...
    @winrt_commethod(9)
    def put_IsEraserInputEnabled(self: Windows.UI.Input.Inking.IInkInputConfiguration, value: Boolean) -> Void: ...
    IsPrimaryBarrelButtonInputEnabled = property(get_IsPrimaryBarrelButtonInputEnabled, put_IsPrimaryBarrelButtonInputEnabled)
    IsEraserInputEnabled = property(get_IsEraserInputEnabled, put_IsEraserInputEnabled)
class IInkInputConfiguration2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkInputConfiguration2'
    _iid_ = Guid('{6ac2272e-81b4-5cc4-a36d-d057c387dfda}')
    @winrt_commethod(6)
    def get_IsPenHapticFeedbackEnabled(self: Windows.UI.Input.Inking.IInkInputConfiguration2) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsPenHapticFeedbackEnabled(self: Windows.UI.Input.Inking.IInkInputConfiguration2, value: Boolean) -> Void: ...
    IsPenHapticFeedbackEnabled = property(get_IsPenHapticFeedbackEnabled, put_IsPenHapticFeedbackEnabled)
class IInkInputProcessingConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkInputProcessingConfiguration'
    _iid_ = Guid('{2778d85e-33ca-4b06-a6d3-ac3945116d37}')
    @winrt_commethod(6)
    def get_Mode(self: Windows.UI.Input.Inking.IInkInputProcessingConfiguration) -> Windows.UI.Input.Inking.InkInputProcessingMode: ...
    @winrt_commethod(7)
    def put_Mode(self: Windows.UI.Input.Inking.IInkInputProcessingConfiguration, value: Windows.UI.Input.Inking.InkInputProcessingMode) -> Void: ...
    @winrt_commethod(8)
    def get_RightDragAction(self: Windows.UI.Input.Inking.IInkInputProcessingConfiguration) -> Windows.UI.Input.Inking.InkInputRightDragAction: ...
    @winrt_commethod(9)
    def put_RightDragAction(self: Windows.UI.Input.Inking.IInkInputProcessingConfiguration, value: Windows.UI.Input.Inking.InkInputRightDragAction) -> Void: ...
    Mode = property(get_Mode, put_Mode)
    RightDragAction = property(get_RightDragAction, put_RightDragAction)
class IInkManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkManager'
    _iid_ = Guid('{4744737d-671b-4163-9c95-4e8d7a035fe1}')
    @winrt_commethod(6)
    def get_Mode(self: Windows.UI.Input.Inking.IInkManager) -> Windows.UI.Input.Inking.InkManipulationMode: ...
    @winrt_commethod(7)
    def put_Mode(self: Windows.UI.Input.Inking.IInkManager, value: Windows.UI.Input.Inking.InkManipulationMode) -> Void: ...
    @winrt_commethod(8)
    def ProcessPointerDown(self: Windows.UI.Input.Inking.IInkManager, pointerPoint: Windows.UI.Input.PointerPoint) -> Void: ...
    @winrt_commethod(9)
    def ProcessPointerUpdate(self: Windows.UI.Input.Inking.IInkManager, pointerPoint: Windows.UI.Input.PointerPoint) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_commethod(10)
    def ProcessPointerUp(self: Windows.UI.Input.Inking.IInkManager, pointerPoint: Windows.UI.Input.PointerPoint) -> Windows.Foundation.Rect: ...
    @winrt_commethod(11)
    def SetDefaultDrawingAttributes(self: Windows.UI.Input.Inking.IInkManager, drawingAttributes: Windows.UI.Input.Inking.InkDrawingAttributes) -> Void: ...
    @winrt_commethod(12)
    def RecognizeAsync2(self: Windows.UI.Input.Inking.IInkManager, recognitionTarget: Windows.UI.Input.Inking.InkRecognitionTarget) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.InkRecognitionResult]]: ...
    Mode = property(get_Mode, put_Mode)
class IInkModelerAttributes(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkModelerAttributes'
    _iid_ = Guid('{bad31f27-0cd9-4bfd-b6f3-9e03ba8d7454}')
    @winrt_commethod(6)
    def get_PredictionTime(self: Windows.UI.Input.Inking.IInkModelerAttributes) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_PredictionTime(self: Windows.UI.Input.Inking.IInkModelerAttributes, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_ScalingFactor(self: Windows.UI.Input.Inking.IInkModelerAttributes) -> Single: ...
    @winrt_commethod(9)
    def put_ScalingFactor(self: Windows.UI.Input.Inking.IInkModelerAttributes, value: Single) -> Void: ...
    PredictionTime = property(get_PredictionTime, put_PredictionTime)
    ScalingFactor = property(get_ScalingFactor, put_ScalingFactor)
class IInkModelerAttributes2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkModelerAttributes2'
    _iid_ = Guid('{86d1d09a-4ef8-5e25-b7bc-b65424f16bb3}')
    @winrt_commethod(6)
    def get_UseVelocityBasedPressure(self: Windows.UI.Input.Inking.IInkModelerAttributes2) -> Boolean: ...
    @winrt_commethod(7)
    def put_UseVelocityBasedPressure(self: Windows.UI.Input.Inking.IInkModelerAttributes2, value: Boolean) -> Void: ...
    UseVelocityBasedPressure = property(get_UseVelocityBasedPressure, put_UseVelocityBasedPressure)
class IInkPoint(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkPoint'
    _iid_ = Guid('{9f87272b-858c-46a5-9b41-d195970459fd}')
    @winrt_commethod(6)
    def get_Position(self: Windows.UI.Input.Inking.IInkPoint) -> Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def get_Pressure(self: Windows.UI.Input.Inking.IInkPoint) -> Single: ...
    Position = property(get_Position, None)
    Pressure = property(get_Pressure, None)
class IInkPoint2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkPoint2'
    _iid_ = Guid('{fba9c3f7-ae56-4d5c-bd2f-0ac45f5e4af9}')
    @winrt_commethod(6)
    def get_TiltX(self: Windows.UI.Input.Inking.IInkPoint2) -> Single: ...
    @winrt_commethod(7)
    def get_TiltY(self: Windows.UI.Input.Inking.IInkPoint2) -> Single: ...
    @winrt_commethod(8)
    def get_Timestamp(self: Windows.UI.Input.Inking.IInkPoint2) -> UInt64: ...
    TiltX = property(get_TiltX, None)
    TiltY = property(get_TiltY, None)
    Timestamp = property(get_Timestamp, None)
class IInkPointFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkPointFactory'
    _iid_ = Guid('{29e5d51c-c98f-405d-9f3b-e53e31068d4d}')
    @winrt_commethod(6)
    def CreateInkPoint(self: Windows.UI.Input.Inking.IInkPointFactory, position: Windows.Foundation.Point, pressure: Single) -> Windows.UI.Input.Inking.InkPoint: ...
class IInkPointFactory2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkPointFactory2'
    _iid_ = Guid('{e0145e85-daff-45f2-ad69-050d8256a209}')
    @winrt_commethod(6)
    def CreateInkPointWithTiltAndTimestamp(self: Windows.UI.Input.Inking.IInkPointFactory2, position: Windows.Foundation.Point, pressure: Single, tiltX: Single, tiltY: Single, timestamp: UInt64) -> Windows.UI.Input.Inking.InkPoint: ...
class IInkPresenter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkPresenter'
    _iid_ = Guid('{a69b70e2-887b-458f-b173-4fe4438930a3}')
    @winrt_commethod(6)
    def get_IsInputEnabled(self: Windows.UI.Input.Inking.IInkPresenter) -> Boolean: ...
    @winrt_commethod(7)
    def put_IsInputEnabled(self: Windows.UI.Input.Inking.IInkPresenter, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_InputDeviceTypes(self: Windows.UI.Input.Inking.IInkPresenter) -> Windows.UI.Core.CoreInputDeviceTypes: ...
    @winrt_commethod(9)
    def put_InputDeviceTypes(self: Windows.UI.Input.Inking.IInkPresenter, value: Windows.UI.Core.CoreInputDeviceTypes) -> Void: ...
    @winrt_commethod(10)
    def get_UnprocessedInput(self: Windows.UI.Input.Inking.IInkPresenter) -> Windows.UI.Input.Inking.InkUnprocessedInput: ...
    @winrt_commethod(11)
    def get_StrokeInput(self: Windows.UI.Input.Inking.IInkPresenter) -> Windows.UI.Input.Inking.InkStrokeInput: ...
    @winrt_commethod(12)
    def get_InputProcessingConfiguration(self: Windows.UI.Input.Inking.IInkPresenter) -> Windows.UI.Input.Inking.InkInputProcessingConfiguration: ...
    @winrt_commethod(13)
    def get_StrokeContainer(self: Windows.UI.Input.Inking.IInkPresenter) -> Windows.UI.Input.Inking.InkStrokeContainer: ...
    @winrt_commethod(14)
    def put_StrokeContainer(self: Windows.UI.Input.Inking.IInkPresenter, value: Windows.UI.Input.Inking.InkStrokeContainer) -> Void: ...
    @winrt_commethod(15)
    def CopyDefaultDrawingAttributes(self: Windows.UI.Input.Inking.IInkPresenter) -> Windows.UI.Input.Inking.InkDrawingAttributes: ...
    @winrt_commethod(16)
    def UpdateDefaultDrawingAttributes(self: Windows.UI.Input.Inking.IInkPresenter, value: Windows.UI.Input.Inking.InkDrawingAttributes) -> Void: ...
    @winrt_commethod(17)
    def ActivateCustomDrying(self: Windows.UI.Input.Inking.IInkPresenter) -> Windows.UI.Input.Inking.InkSynchronizer: ...
    @winrt_commethod(18)
    def SetPredefinedConfiguration(self: Windows.UI.Input.Inking.IInkPresenter, value: Windows.UI.Input.Inking.InkPresenterPredefinedConfiguration) -> Void: ...
    @winrt_commethod(19)
    def add_StrokesCollected(self: Windows.UI.Input.Inking.IInkPresenter, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.InkPresenter, Windows.UI.Input.Inking.InkStrokesCollectedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(20)
    def remove_StrokesCollected(self: Windows.UI.Input.Inking.IInkPresenter, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(21)
    def add_StrokesErased(self: Windows.UI.Input.Inking.IInkPresenter, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.InkPresenter, Windows.UI.Input.Inking.InkStrokesErasedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(22)
    def remove_StrokesErased(self: Windows.UI.Input.Inking.IInkPresenter, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    IsInputEnabled = property(get_IsInputEnabled, put_IsInputEnabled)
    InputDeviceTypes = property(get_InputDeviceTypes, put_InputDeviceTypes)
    UnprocessedInput = property(get_UnprocessedInput, None)
    StrokeInput = property(get_StrokeInput, None)
    InputProcessingConfiguration = property(get_InputProcessingConfiguration, None)
    StrokeContainer = property(get_StrokeContainer, put_StrokeContainer)
class IInkPresenter2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkPresenter2'
    _iid_ = Guid('{cf53e612-9a34-11e6-9f33-a24fc0d9649c}')
    @winrt_commethod(6)
    def get_HighContrastAdjustment(self: Windows.UI.Input.Inking.IInkPresenter2) -> Windows.UI.Input.Inking.InkHighContrastAdjustment: ...
    @winrt_commethod(7)
    def put_HighContrastAdjustment(self: Windows.UI.Input.Inking.IInkPresenter2, value: Windows.UI.Input.Inking.InkHighContrastAdjustment) -> Void: ...
    HighContrastAdjustment = property(get_HighContrastAdjustment, put_HighContrastAdjustment)
class IInkPresenter3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkPresenter3'
    _iid_ = Guid('{51e1ce89-d37d-4a90-83fc-7f5e9dfbf217}')
    @winrt_commethod(6)
    def get_InputConfiguration(self: Windows.UI.Input.Inking.IInkPresenter3) -> Windows.UI.Input.Inking.InkInputConfiguration: ...
    InputConfiguration = property(get_InputConfiguration, None)
class IInkPresenterProtractor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkPresenterProtractor'
    _iid_ = Guid('{7de3f2aa-ef6c-4e91-a73b-5b70d56fbd17}')
    @winrt_commethod(6)
    def get_AreTickMarksVisible(self: Windows.UI.Input.Inking.IInkPresenterProtractor) -> Boolean: ...
    @winrt_commethod(7)
    def put_AreTickMarksVisible(self: Windows.UI.Input.Inking.IInkPresenterProtractor, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_AreRaysVisible(self: Windows.UI.Input.Inking.IInkPresenterProtractor) -> Boolean: ...
    @winrt_commethod(9)
    def put_AreRaysVisible(self: Windows.UI.Input.Inking.IInkPresenterProtractor, value: Boolean) -> Void: ...
    @winrt_commethod(10)
    def get_IsCenterMarkerVisible(self: Windows.UI.Input.Inking.IInkPresenterProtractor) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsCenterMarkerVisible(self: Windows.UI.Input.Inking.IInkPresenterProtractor, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_IsAngleReadoutVisible(self: Windows.UI.Input.Inking.IInkPresenterProtractor) -> Boolean: ...
    @winrt_commethod(13)
    def put_IsAngleReadoutVisible(self: Windows.UI.Input.Inking.IInkPresenterProtractor, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_IsResizable(self: Windows.UI.Input.Inking.IInkPresenterProtractor) -> Boolean: ...
    @winrt_commethod(15)
    def put_IsResizable(self: Windows.UI.Input.Inking.IInkPresenterProtractor, value: Boolean) -> Void: ...
    @winrt_commethod(16)
    def get_Radius(self: Windows.UI.Input.Inking.IInkPresenterProtractor) -> Double: ...
    @winrt_commethod(17)
    def put_Radius(self: Windows.UI.Input.Inking.IInkPresenterProtractor, value: Double) -> Void: ...
    @winrt_commethod(18)
    def get_AccentColor(self: Windows.UI.Input.Inking.IInkPresenterProtractor) -> Windows.UI.Color: ...
    @winrt_commethod(19)
    def put_AccentColor(self: Windows.UI.Input.Inking.IInkPresenterProtractor, value: Windows.UI.Color) -> Void: ...
    AreTickMarksVisible = property(get_AreTickMarksVisible, put_AreTickMarksVisible)
    AreRaysVisible = property(get_AreRaysVisible, put_AreRaysVisible)
    IsCenterMarkerVisible = property(get_IsCenterMarkerVisible, put_IsCenterMarkerVisible)
    IsAngleReadoutVisible = property(get_IsAngleReadoutVisible, put_IsAngleReadoutVisible)
    IsResizable = property(get_IsResizable, put_IsResizable)
    Radius = property(get_Radius, put_Radius)
    AccentColor = property(get_AccentColor, put_AccentColor)
class IInkPresenterProtractorFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkPresenterProtractorFactory'
    _iid_ = Guid('{320103c9-68fa-47e9-8127-8370711fc46c}')
    @winrt_commethod(6)
    def Create(self: Windows.UI.Input.Inking.IInkPresenterProtractorFactory, inkPresenter: Windows.UI.Input.Inking.InkPresenter) -> Windows.UI.Input.Inking.InkPresenterProtractor: ...
class IInkPresenterRuler(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkPresenterRuler'
    _iid_ = Guid('{6cda7d5a-dec7-4dd7-877a-2133f183d48a}')
    @winrt_commethod(6)
    def get_Length(self: Windows.UI.Input.Inking.IInkPresenterRuler) -> Double: ...
    @winrt_commethod(7)
    def put_Length(self: Windows.UI.Input.Inking.IInkPresenterRuler, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_Width(self: Windows.UI.Input.Inking.IInkPresenterRuler) -> Double: ...
    @winrt_commethod(9)
    def put_Width(self: Windows.UI.Input.Inking.IInkPresenterRuler, value: Double) -> Void: ...
    Length = property(get_Length, put_Length)
    Width = property(get_Width, put_Width)
class IInkPresenterRuler2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkPresenterRuler2'
    _iid_ = Guid('{45130dc1-bc61-44d4-a423-54712ae671c4}')
    @winrt_commethod(6)
    def get_AreTickMarksVisible(self: Windows.UI.Input.Inking.IInkPresenterRuler2) -> Boolean: ...
    @winrt_commethod(7)
    def put_AreTickMarksVisible(self: Windows.UI.Input.Inking.IInkPresenterRuler2, value: Boolean) -> Void: ...
    @winrt_commethod(8)
    def get_IsCompassVisible(self: Windows.UI.Input.Inking.IInkPresenterRuler2) -> Boolean: ...
    @winrt_commethod(9)
    def put_IsCompassVisible(self: Windows.UI.Input.Inking.IInkPresenterRuler2, value: Boolean) -> Void: ...
    AreTickMarksVisible = property(get_AreTickMarksVisible, put_AreTickMarksVisible)
    IsCompassVisible = property(get_IsCompassVisible, put_IsCompassVisible)
class IInkPresenterRulerFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkPresenterRulerFactory'
    _iid_ = Guid('{34361beb-9001-4a4b-a690-69dbaf63e501}')
    @winrt_commethod(6)
    def Create(self: Windows.UI.Input.Inking.IInkPresenterRulerFactory, inkPresenter: Windows.UI.Input.Inking.InkPresenter) -> Windows.UI.Input.Inking.InkPresenterRuler: ...
class IInkPresenterStencil(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkPresenterStencil'
    _iid_ = Guid('{30d12d6d-3e06-4d02-b116-277fb5d8addc}')
    @winrt_commethod(6)
    def get_Kind(self: Windows.UI.Input.Inking.IInkPresenterStencil) -> Windows.UI.Input.Inking.InkPresenterStencilKind: ...
    @winrt_commethod(7)
    def get_IsVisible(self: Windows.UI.Input.Inking.IInkPresenterStencil) -> Boolean: ...
    @winrt_commethod(8)
    def put_IsVisible(self: Windows.UI.Input.Inking.IInkPresenterStencil, value: Boolean) -> Void: ...
    @winrt_commethod(9)
    def get_BackgroundColor(self: Windows.UI.Input.Inking.IInkPresenterStencil) -> Windows.UI.Color: ...
    @winrt_commethod(10)
    def put_BackgroundColor(self: Windows.UI.Input.Inking.IInkPresenterStencil, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(11)
    def get_ForegroundColor(self: Windows.UI.Input.Inking.IInkPresenterStencil) -> Windows.UI.Color: ...
    @winrt_commethod(12)
    def put_ForegroundColor(self: Windows.UI.Input.Inking.IInkPresenterStencil, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(13)
    def get_Transform(self: Windows.UI.Input.Inking.IInkPresenterStencil) -> Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_commethod(14)
    def put_Transform(self: Windows.UI.Input.Inking.IInkPresenterStencil, value: Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    Kind = property(get_Kind, None)
    IsVisible = property(get_IsVisible, put_IsVisible)
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    ForegroundColor = property(get_ForegroundColor, put_ForegroundColor)
    Transform = property(get_Transform, put_Transform)
class IInkRecognitionResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkRecognitionResult'
    _iid_ = Guid('{36461a94-5068-40ef-8a05-2c2fb60908a2}')
    @winrt_commethod(6)
    def get_BoundingRect(self: Windows.UI.Input.Inking.IInkRecognitionResult) -> Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def GetTextCandidates(self: Windows.UI.Input.Inking.IInkRecognitionResult) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_commethod(8)
    def GetStrokes(self: Windows.UI.Input.Inking.IInkRecognitionResult) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.InkStroke]: ...
    BoundingRect = property(get_BoundingRect, None)
class IInkRecognizer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkRecognizer'
    _iid_ = Guid('{077ccea3-904d-442a-b151-aaca3631c43b}')
    @winrt_commethod(6)
    def get_Name(self: Windows.UI.Input.Inking.IInkRecognizer) -> WinRT_String: ...
    Name = property(get_Name, None)
class IInkRecognizerContainer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkRecognizerContainer'
    _iid_ = Guid('{a74d9a31-8047-4698-a912-f82a5085012f}')
    @winrt_commethod(6)
    def SetDefaultRecognizer(self: Windows.UI.Input.Inking.IInkRecognizerContainer, recognizer: Windows.UI.Input.Inking.InkRecognizer) -> Void: ...
    @winrt_commethod(7)
    def RecognizeAsync(self: Windows.UI.Input.Inking.IInkRecognizerContainer, strokeCollection: Windows.UI.Input.Inking.InkStrokeContainer, recognitionTarget: Windows.UI.Input.Inking.InkRecognitionTarget) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.InkRecognitionResult]]: ...
    @winrt_commethod(8)
    def GetRecognizers(self: Windows.UI.Input.Inking.IInkRecognizerContainer) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.InkRecognizer]: ...
class IInkStroke(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkStroke'
    _iid_ = Guid('{15144d60-cce3-4fcf-9d52-11518ab6afd4}')
    @winrt_commethod(6)
    def get_DrawingAttributes(self: Windows.UI.Input.Inking.IInkStroke) -> Windows.UI.Input.Inking.InkDrawingAttributes: ...
    @winrt_commethod(7)
    def put_DrawingAttributes(self: Windows.UI.Input.Inking.IInkStroke, value: Windows.UI.Input.Inking.InkDrawingAttributes) -> Void: ...
    @winrt_commethod(8)
    def get_BoundingRect(self: Windows.UI.Input.Inking.IInkStroke) -> Windows.Foundation.Rect: ...
    @winrt_commethod(9)
    def get_Selected(self: Windows.UI.Input.Inking.IInkStroke) -> Boolean: ...
    @winrt_commethod(10)
    def put_Selected(self: Windows.UI.Input.Inking.IInkStroke, value: Boolean) -> Void: ...
    @winrt_commethod(11)
    def get_Recognized(self: Windows.UI.Input.Inking.IInkStroke) -> Boolean: ...
    @winrt_commethod(12)
    def GetRenderingSegments(self: Windows.UI.Input.Inking.IInkStroke) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.InkStrokeRenderingSegment]: ...
    @winrt_commethod(13)
    def Clone(self: Windows.UI.Input.Inking.IInkStroke) -> Windows.UI.Input.Inking.InkStroke: ...
    DrawingAttributes = property(get_DrawingAttributes, put_DrawingAttributes)
    BoundingRect = property(get_BoundingRect, None)
    Selected = property(get_Selected, put_Selected)
    Recognized = property(get_Recognized, None)
class IInkStroke2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkStroke2'
    _iid_ = Guid('{5db9e4f4-bafa-4de1-89d3-201b1ed7d89b}')
    @winrt_commethod(6)
    def get_PointTransform(self: Windows.UI.Input.Inking.IInkStroke2) -> Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_commethod(7)
    def put_PointTransform(self: Windows.UI.Input.Inking.IInkStroke2, value: Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    @winrt_commethod(8)
    def GetInkPoints(self: Windows.UI.Input.Inking.IInkStroke2) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.InkPoint]: ...
    PointTransform = property(get_PointTransform, put_PointTransform)
class IInkStroke3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkStroke3'
    _iid_ = Guid('{4a807374-9499-411d-a1c4-68855d03d65f}')
    @winrt_commethod(6)
    def get_Id(self: Windows.UI.Input.Inking.IInkStroke3) -> UInt32: ...
    @winrt_commethod(7)
    def get_StrokeStartedTime(self: Windows.UI.Input.Inking.IInkStroke3) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_commethod(8)
    def put_StrokeStartedTime(self: Windows.UI.Input.Inking.IInkStroke3, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    @winrt_commethod(9)
    def get_StrokeDuration(self: Windows.UI.Input.Inking.IInkStroke3) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_commethod(10)
    def put_StrokeDuration(self: Windows.UI.Input.Inking.IInkStroke3, value: Windows.Foundation.IReference[Windows.Foundation.TimeSpan]) -> Void: ...
    Id = property(get_Id, None)
    StrokeStartedTime = property(get_StrokeStartedTime, put_StrokeStartedTime)
    StrokeDuration = property(get_StrokeDuration, put_StrokeDuration)
class IInkStroke4(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkStroke4'
    _iid_ = Guid('{cd5b62e5-b6e9-5b91-a577-1921d2348690}')
    @winrt_commethod(6)
    def get_PointerId(self: Windows.UI.Input.Inking.IInkStroke4) -> UInt32: ...
    PointerId = property(get_PointerId, None)
class IInkStrokeBuilder(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkStrokeBuilder'
    _iid_ = Guid('{82bbd1dc-1c63-41dc-9e07-4b4a70ced801}')
    @winrt_commethod(6)
    def BeginStroke(self: Windows.UI.Input.Inking.IInkStrokeBuilder, pointerPoint: Windows.UI.Input.PointerPoint) -> Void: ...
    @winrt_commethod(7)
    def AppendToStroke(self: Windows.UI.Input.Inking.IInkStrokeBuilder, pointerPoint: Windows.UI.Input.PointerPoint) -> Windows.UI.Input.PointerPoint: ...
    @winrt_commethod(8)
    def EndStroke(self: Windows.UI.Input.Inking.IInkStrokeBuilder, pointerPoint: Windows.UI.Input.PointerPoint) -> Windows.UI.Input.Inking.InkStroke: ...
    @winrt_commethod(9)
    def CreateStroke(self: Windows.UI.Input.Inking.IInkStrokeBuilder, points: Windows.Foundation.Collections.IIterable[Windows.Foundation.Point]) -> Windows.UI.Input.Inking.InkStroke: ...
    @winrt_commethod(10)
    def SetDefaultDrawingAttributes(self: Windows.UI.Input.Inking.IInkStrokeBuilder, drawingAttributes: Windows.UI.Input.Inking.InkDrawingAttributes) -> Void: ...
class IInkStrokeBuilder2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkStrokeBuilder2'
    _iid_ = Guid('{bd82bc27-731f-4cbc-bbbf-6d468044f1e5}')
    @winrt_commethod(6)
    def CreateStrokeFromInkPoints(self: Windows.UI.Input.Inking.IInkStrokeBuilder2, inkPoints: Windows.Foundation.Collections.IIterable[Windows.UI.Input.Inking.InkPoint], transform: Windows.Foundation.Numerics.Matrix3x2) -> Windows.UI.Input.Inking.InkStroke: ...
class IInkStrokeBuilder3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkStrokeBuilder3'
    _iid_ = Guid('{b2c71fcd-5472-46b1-a81d-c37a3d169441}')
    @winrt_commethod(6)
    def CreateStrokeFromInkPoints(self: Windows.UI.Input.Inking.IInkStrokeBuilder3, inkPoints: Windows.Foundation.Collections.IIterable[Windows.UI.Input.Inking.InkPoint], transform: Windows.Foundation.Numerics.Matrix3x2, strokeStartedTime: Windows.Foundation.IReference[Windows.Foundation.DateTime], strokeDuration: Windows.Foundation.IReference[Windows.Foundation.TimeSpan]) -> Windows.UI.Input.Inking.InkStroke: ...
class IInkStrokeContainer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkStrokeContainer'
    _iid_ = Guid('{22accbc6-faa9-4f14-b68c-f6cee670ae16}')
    @winrt_commethod(6)
    def get_BoundingRect(self: Windows.UI.Input.Inking.IInkStrokeContainer) -> Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def AddStroke(self: Windows.UI.Input.Inking.IInkStrokeContainer, stroke: Windows.UI.Input.Inking.InkStroke) -> Void: ...
    @winrt_commethod(8)
    def DeleteSelected(self: Windows.UI.Input.Inking.IInkStrokeContainer) -> Windows.Foundation.Rect: ...
    @winrt_commethod(9)
    def MoveSelected(self: Windows.UI.Input.Inking.IInkStrokeContainer, translation: Windows.Foundation.Point) -> Windows.Foundation.Rect: ...
    @winrt_commethod(10)
    def SelectWithPolyLine(self: Windows.UI.Input.Inking.IInkStrokeContainer, polyline: Windows.Foundation.Collections.IIterable[Windows.Foundation.Point]) -> Windows.Foundation.Rect: ...
    @winrt_commethod(11)
    def SelectWithLine(self: Windows.UI.Input.Inking.IInkStrokeContainer, from_: Windows.Foundation.Point, to: Windows.Foundation.Point) -> Windows.Foundation.Rect: ...
    @winrt_commethod(12)
    def CopySelectedToClipboard(self: Windows.UI.Input.Inking.IInkStrokeContainer) -> Void: ...
    @winrt_commethod(13)
    def PasteFromClipboard(self: Windows.UI.Input.Inking.IInkStrokeContainer, position: Windows.Foundation.Point) -> Windows.Foundation.Rect: ...
    @winrt_commethod(14)
    def CanPasteFromClipboard(self: Windows.UI.Input.Inking.IInkStrokeContainer) -> Boolean: ...
    @winrt_commethod(15)
    def LoadAsync(self: Windows.UI.Input.Inking.IInkStrokeContainer, inputStream: Windows.Storage.Streams.IInputStream) -> Windows.Foundation.IAsyncActionWithProgress[UInt64]: ...
    @winrt_commethod(16)
    def SaveAsync(self: Windows.UI.Input.Inking.IInkStrokeContainer, outputStream: Windows.Storage.Streams.IOutputStream) -> Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
    @winrt_commethod(17)
    def UpdateRecognitionResults(self: Windows.UI.Input.Inking.IInkStrokeContainer, recognitionResults: Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.InkRecognitionResult]) -> Void: ...
    @winrt_commethod(18)
    def GetStrokes(self: Windows.UI.Input.Inking.IInkStrokeContainer) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.InkStroke]: ...
    @winrt_commethod(19)
    def GetRecognitionResults(self: Windows.UI.Input.Inking.IInkStrokeContainer) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.InkRecognitionResult]: ...
    BoundingRect = property(get_BoundingRect, None)
class IInkStrokeContainer2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkStrokeContainer2'
    _iid_ = Guid('{8901d364-da36-4bcf-9e5c-d195825995b4}')
    @winrt_commethod(6)
    def AddStrokes(self: Windows.UI.Input.Inking.IInkStrokeContainer2, strokes: Windows.Foundation.Collections.IIterable[Windows.UI.Input.Inking.InkStroke]) -> Void: ...
    @winrt_commethod(7)
    def Clear(self: Windows.UI.Input.Inking.IInkStrokeContainer2) -> Void: ...
class IInkStrokeContainer3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkStrokeContainer3'
    _iid_ = Guid('{3d07bea5-baea-4c82-a719-7b83da1067d2}')
    @winrt_commethod(6)
    def SaveWithFormatAsync(self: Windows.UI.Input.Inking.IInkStrokeContainer3, outputStream: Windows.Storage.Streams.IOutputStream, inkPersistenceFormat: Windows.UI.Input.Inking.InkPersistenceFormat) -> Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
    @winrt_commethod(7)
    def GetStrokeById(self: Windows.UI.Input.Inking.IInkStrokeContainer3, id: UInt32) -> Windows.UI.Input.Inking.InkStroke: ...
class IInkStrokeInput(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkStrokeInput'
    _iid_ = Guid('{cf2ffe7b-5e10-43c6-a080-88f26e1dc67d}')
    @winrt_commethod(6)
    def add_StrokeStarted(self: Windows.UI.Input.Inking.IInkStrokeInput, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.InkStrokeInput, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_StrokeStarted(self: Windows.UI.Input.Inking.IInkStrokeInput, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_StrokeContinued(self: Windows.UI.Input.Inking.IInkStrokeInput, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.InkStrokeInput, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_StrokeContinued(self: Windows.UI.Input.Inking.IInkStrokeInput, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_StrokeEnded(self: Windows.UI.Input.Inking.IInkStrokeInput, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.InkStrokeInput, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_StrokeEnded(self: Windows.UI.Input.Inking.IInkStrokeInput, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_StrokeCanceled(self: Windows.UI.Input.Inking.IInkStrokeInput, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.InkStrokeInput, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_StrokeCanceled(self: Windows.UI.Input.Inking.IInkStrokeInput, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def get_InkPresenter(self: Windows.UI.Input.Inking.IInkStrokeInput) -> Windows.UI.Input.Inking.InkPresenter: ...
    InkPresenter = property(get_InkPresenter, None)
class IInkStrokeRenderingSegment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkStrokeRenderingSegment'
    _iid_ = Guid('{68510f1f-88e3-477a-a2fa-569f5f1f9bd5}')
    @winrt_commethod(6)
    def get_Position(self: Windows.UI.Input.Inking.IInkStrokeRenderingSegment) -> Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def get_BezierControlPoint1(self: Windows.UI.Input.Inking.IInkStrokeRenderingSegment) -> Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def get_BezierControlPoint2(self: Windows.UI.Input.Inking.IInkStrokeRenderingSegment) -> Windows.Foundation.Point: ...
    @winrt_commethod(9)
    def get_Pressure(self: Windows.UI.Input.Inking.IInkStrokeRenderingSegment) -> Single: ...
    @winrt_commethod(10)
    def get_TiltX(self: Windows.UI.Input.Inking.IInkStrokeRenderingSegment) -> Single: ...
    @winrt_commethod(11)
    def get_TiltY(self: Windows.UI.Input.Inking.IInkStrokeRenderingSegment) -> Single: ...
    @winrt_commethod(12)
    def get_Twist(self: Windows.UI.Input.Inking.IInkStrokeRenderingSegment) -> Single: ...
    Position = property(get_Position, None)
    BezierControlPoint1 = property(get_BezierControlPoint1, None)
    BezierControlPoint2 = property(get_BezierControlPoint2, None)
    Pressure = property(get_Pressure, None)
    TiltX = property(get_TiltX, None)
    TiltY = property(get_TiltY, None)
    Twist = property(get_Twist, None)
class IInkStrokesCollectedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkStrokesCollectedEventArgs'
    _iid_ = Guid('{c4f3f229-1938-495c-b4d9-6de4b08d4811}')
    @winrt_commethod(6)
    def get_Strokes(self: Windows.UI.Input.Inking.IInkStrokesCollectedEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.InkStroke]: ...
    Strokes = property(get_Strokes, None)
class IInkStrokesErasedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkStrokesErasedEventArgs'
    _iid_ = Guid('{a4216a22-1503-4ebf-8ff5-2de84584a8aa}')
    @winrt_commethod(6)
    def get_Strokes(self: Windows.UI.Input.Inking.IInkStrokesErasedEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.InkStroke]: ...
    Strokes = property(get_Strokes, None)
class IInkSynchronizer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkSynchronizer'
    _iid_ = Guid('{9b9ea160-ae9b-45f9-8407-4b493b163661}')
    @winrt_commethod(6)
    def BeginDry(self: Windows.UI.Input.Inking.IInkSynchronizer) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.InkStroke]: ...
    @winrt_commethod(7)
    def EndDry(self: Windows.UI.Input.Inking.IInkSynchronizer) -> Void: ...
class IInkUnprocessedInput(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IInkUnprocessedInput'
    _iid_ = Guid('{db4445e0-8398-4921-ac3b-ab978c5ba256}')
    @winrt_commethod(6)
    def add_PointerEntered(self: Windows.UI.Input.Inking.IInkUnprocessedInput, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.InkUnprocessedInput, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_PointerEntered(self: Windows.UI.Input.Inking.IInkUnprocessedInput, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_PointerHovered(self: Windows.UI.Input.Inking.IInkUnprocessedInput, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.InkUnprocessedInput, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_PointerHovered(self: Windows.UI.Input.Inking.IInkUnprocessedInput, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_PointerExited(self: Windows.UI.Input.Inking.IInkUnprocessedInput, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.InkUnprocessedInput, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_PointerExited(self: Windows.UI.Input.Inking.IInkUnprocessedInput, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def add_PointerPressed(self: Windows.UI.Input.Inking.IInkUnprocessedInput, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.InkUnprocessedInput, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(13)
    def remove_PointerPressed(self: Windows.UI.Input.Inking.IInkUnprocessedInput, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(14)
    def add_PointerMoved(self: Windows.UI.Input.Inking.IInkUnprocessedInput, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.InkUnprocessedInput, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(15)
    def remove_PointerMoved(self: Windows.UI.Input.Inking.IInkUnprocessedInput, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(16)
    def add_PointerReleased(self: Windows.UI.Input.Inking.IInkUnprocessedInput, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.InkUnprocessedInput, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(17)
    def remove_PointerReleased(self: Windows.UI.Input.Inking.IInkUnprocessedInput, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(18)
    def add_PointerLost(self: Windows.UI.Input.Inking.IInkUnprocessedInput, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.InkUnprocessedInput, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(19)
    def remove_PointerLost(self: Windows.UI.Input.Inking.IInkUnprocessedInput, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(20)
    def get_InkPresenter(self: Windows.UI.Input.Inking.IInkUnprocessedInput) -> Windows.UI.Input.Inking.InkPresenter: ...
    InkPresenter = property(get_InkPresenter, None)
class IPenAndInkSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IPenAndInkSettings'
    _iid_ = Guid('{bc2ceb8f-0066-44a8-bb7a-b839b3deb8f5}')
    @winrt_commethod(6)
    def get_IsHandwritingDirectlyIntoTextFieldEnabled(self: Windows.UI.Input.Inking.IPenAndInkSettings) -> Boolean: ...
    @winrt_commethod(7)
    def get_PenHandedness(self: Windows.UI.Input.Inking.IPenAndInkSettings) -> Windows.UI.Input.Inking.PenHandedness: ...
    @winrt_commethod(8)
    def get_HandwritingLineHeight(self: Windows.UI.Input.Inking.IPenAndInkSettings) -> Windows.UI.Input.Inking.HandwritingLineHeight: ...
    @winrt_commethod(9)
    def get_FontFamilyName(self: Windows.UI.Input.Inking.IPenAndInkSettings) -> WinRT_String: ...
    @winrt_commethod(10)
    def get_UserConsentsToHandwritingTelemetryCollection(self: Windows.UI.Input.Inking.IPenAndInkSettings) -> Boolean: ...
    @winrt_commethod(11)
    def get_IsTouchHandwritingEnabled(self: Windows.UI.Input.Inking.IPenAndInkSettings) -> Boolean: ...
    IsHandwritingDirectlyIntoTextFieldEnabled = property(get_IsHandwritingDirectlyIntoTextFieldEnabled, None)
    PenHandedness = property(get_PenHandedness, None)
    HandwritingLineHeight = property(get_HandwritingLineHeight, None)
    FontFamilyName = property(get_FontFamilyName, None)
    UserConsentsToHandwritingTelemetryCollection = property(get_UserConsentsToHandwritingTelemetryCollection, None)
    IsTouchHandwritingEnabled = property(get_IsTouchHandwritingEnabled, None)
class IPenAndInkSettings2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IPenAndInkSettings2'
    _iid_ = Guid('{3262da53-1f44-55e2-9929-ebf77e5481b8}')
    @winrt_commethod(6)
    def SetPenHandedness(self: Windows.UI.Input.Inking.IPenAndInkSettings2, value: Windows.UI.Input.Inking.PenHandedness) -> Void: ...
class IPenAndInkSettingsStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Input.Inking.IPenAndInkSettingsStatics'
    _iid_ = Guid('{ed6dd036-5708-5c3c-96db-f2f552eab641}')
    @winrt_commethod(6)
    def GetDefault(self: Windows.UI.Input.Inking.IPenAndInkSettingsStatics) -> Windows.UI.Input.Inking.PenAndInkSettings: ...
class InkDrawingAttributes(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Input.Inking.IInkDrawingAttributes
    _classid_ = 'Windows.UI.Input.Inking.InkDrawingAttributes'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Input.Inking.InkDrawingAttributes: ...
    @winrt_mixinmethod
    def get_Color(self: Windows.UI.Input.Inking.IInkDrawingAttributes) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: Windows.UI.Input.Inking.IInkDrawingAttributes, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_PenTip(self: Windows.UI.Input.Inking.IInkDrawingAttributes) -> Windows.UI.Input.Inking.PenTipShape: ...
    @winrt_mixinmethod
    def put_PenTip(self: Windows.UI.Input.Inking.IInkDrawingAttributes, value: Windows.UI.Input.Inking.PenTipShape) -> Void: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.UI.Input.Inking.IInkDrawingAttributes) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def put_Size(self: Windows.UI.Input.Inking.IInkDrawingAttributes, value: Windows.Foundation.Size) -> Void: ...
    @winrt_mixinmethod
    def get_IgnorePressure(self: Windows.UI.Input.Inking.IInkDrawingAttributes) -> Boolean: ...
    @winrt_mixinmethod
    def put_IgnorePressure(self: Windows.UI.Input.Inking.IInkDrawingAttributes, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_FitToCurve(self: Windows.UI.Input.Inking.IInkDrawingAttributes) -> Boolean: ...
    @winrt_mixinmethod
    def put_FitToCurve(self: Windows.UI.Input.Inking.IInkDrawingAttributes, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_PenTipTransform(self: Windows.UI.Input.Inking.IInkDrawingAttributes2) -> Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_mixinmethod
    def put_PenTipTransform(self: Windows.UI.Input.Inking.IInkDrawingAttributes2, value: Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    @winrt_mixinmethod
    def get_DrawAsHighlighter(self: Windows.UI.Input.Inking.IInkDrawingAttributes2) -> Boolean: ...
    @winrt_mixinmethod
    def put_DrawAsHighlighter(self: Windows.UI.Input.Inking.IInkDrawingAttributes2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.UI.Input.Inking.IInkDrawingAttributes3) -> Windows.UI.Input.Inking.InkDrawingAttributesKind: ...
    @winrt_mixinmethod
    def get_PencilProperties(self: Windows.UI.Input.Inking.IInkDrawingAttributes3) -> Windows.UI.Input.Inking.InkDrawingAttributesPencilProperties: ...
    @winrt_mixinmethod
    def get_IgnoreTilt(self: Windows.UI.Input.Inking.IInkDrawingAttributes4) -> Boolean: ...
    @winrt_mixinmethod
    def put_IgnoreTilt(self: Windows.UI.Input.Inking.IInkDrawingAttributes4, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_ModelerAttributes(self: Windows.UI.Input.Inking.IInkDrawingAttributes5) -> Windows.UI.Input.Inking.InkModelerAttributes: ...
    @winrt_classmethod
    def CreateForPencil(cls: Windows.UI.Input.Inking.IInkDrawingAttributesStatics) -> Windows.UI.Input.Inking.InkDrawingAttributes: ...
    Color = property(get_Color, put_Color)
    PenTip = property(get_PenTip, put_PenTip)
    Size = property(get_Size, put_Size)
    IgnorePressure = property(get_IgnorePressure, put_IgnorePressure)
    FitToCurve = property(get_FitToCurve, put_FitToCurve)
    PenTipTransform = property(get_PenTipTransform, put_PenTipTransform)
    DrawAsHighlighter = property(get_DrawAsHighlighter, put_DrawAsHighlighter)
    Kind = property(get_Kind, None)
    PencilProperties = property(get_PencilProperties, None)
    IgnoreTilt = property(get_IgnoreTilt, put_IgnoreTilt)
    ModelerAttributes = property(get_ModelerAttributes, None)
InkDrawingAttributesKind = Int32
InkDrawingAttributesKind_Default: InkDrawingAttributesKind = 0
InkDrawingAttributesKind_Pencil: InkDrawingAttributesKind = 1
class InkDrawingAttributesPencilProperties(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Input.Inking.IInkDrawingAttributesPencilProperties
    _classid_ = 'Windows.UI.Input.Inking.InkDrawingAttributesPencilProperties'
    @winrt_mixinmethod
    def get_Opacity(self: Windows.UI.Input.Inking.IInkDrawingAttributesPencilProperties) -> Double: ...
    @winrt_mixinmethod
    def put_Opacity(self: Windows.UI.Input.Inking.IInkDrawingAttributesPencilProperties, value: Double) -> Void: ...
    Opacity = property(get_Opacity, put_Opacity)
InkHighContrastAdjustment = Int32
InkHighContrastAdjustment_UseSystemColorsWhenNecessary: InkHighContrastAdjustment = 0
InkHighContrastAdjustment_UseSystemColors: InkHighContrastAdjustment = 1
InkHighContrastAdjustment_UseOriginalColors: InkHighContrastAdjustment = 2
class InkInputConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Input.Inking.IInkInputConfiguration
    _classid_ = 'Windows.UI.Input.Inking.InkInputConfiguration'
    @winrt_mixinmethod
    def get_IsPrimaryBarrelButtonInputEnabled(self: Windows.UI.Input.Inking.IInkInputConfiguration) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsPrimaryBarrelButtonInputEnabled(self: Windows.UI.Input.Inking.IInkInputConfiguration, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsEraserInputEnabled(self: Windows.UI.Input.Inking.IInkInputConfiguration) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsEraserInputEnabled(self: Windows.UI.Input.Inking.IInkInputConfiguration, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsPenHapticFeedbackEnabled(self: Windows.UI.Input.Inking.IInkInputConfiguration2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsPenHapticFeedbackEnabled(self: Windows.UI.Input.Inking.IInkInputConfiguration2, value: Boolean) -> Void: ...
    IsPrimaryBarrelButtonInputEnabled = property(get_IsPrimaryBarrelButtonInputEnabled, put_IsPrimaryBarrelButtonInputEnabled)
    IsEraserInputEnabled = property(get_IsEraserInputEnabled, put_IsEraserInputEnabled)
    IsPenHapticFeedbackEnabled = property(get_IsPenHapticFeedbackEnabled, put_IsPenHapticFeedbackEnabled)
class InkInputProcessingConfiguration(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Input.Inking.IInkInputProcessingConfiguration
    _classid_ = 'Windows.UI.Input.Inking.InkInputProcessingConfiguration'
    @winrt_mixinmethod
    def get_Mode(self: Windows.UI.Input.Inking.IInkInputProcessingConfiguration) -> Windows.UI.Input.Inking.InkInputProcessingMode: ...
    @winrt_mixinmethod
    def put_Mode(self: Windows.UI.Input.Inking.IInkInputProcessingConfiguration, value: Windows.UI.Input.Inking.InkInputProcessingMode) -> Void: ...
    @winrt_mixinmethod
    def get_RightDragAction(self: Windows.UI.Input.Inking.IInkInputProcessingConfiguration) -> Windows.UI.Input.Inking.InkInputRightDragAction: ...
    @winrt_mixinmethod
    def put_RightDragAction(self: Windows.UI.Input.Inking.IInkInputProcessingConfiguration, value: Windows.UI.Input.Inking.InkInputRightDragAction) -> Void: ...
    Mode = property(get_Mode, put_Mode)
    RightDragAction = property(get_RightDragAction, put_RightDragAction)
InkInputProcessingMode = Int32
InkInputProcessingMode_None: InkInputProcessingMode = 0
InkInputProcessingMode_Inking: InkInputProcessingMode = 1
InkInputProcessingMode_Erasing: InkInputProcessingMode = 2
InkInputRightDragAction = Int32
InkInputRightDragAction_LeaveUnprocessed: InkInputRightDragAction = 0
InkInputRightDragAction_AllowProcessing: InkInputRightDragAction = 1
class InkManager(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Input.Inking.IInkManager
    _classid_ = 'Windows.UI.Input.Inking.InkManager'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Input.Inking.InkManager: ...
    @winrt_mixinmethod
    def get_Mode(self: Windows.UI.Input.Inking.IInkManager) -> Windows.UI.Input.Inking.InkManipulationMode: ...
    @winrt_mixinmethod
    def put_Mode(self: Windows.UI.Input.Inking.IInkManager, value: Windows.UI.Input.Inking.InkManipulationMode) -> Void: ...
    @winrt_mixinmethod
    def ProcessPointerDown(self: Windows.UI.Input.Inking.IInkManager, pointerPoint: Windows.UI.Input.PointerPoint) -> Void: ...
    @winrt_mixinmethod
    def ProcessPointerUpdate(self: Windows.UI.Input.Inking.IInkManager, pointerPoint: Windows.UI.Input.PointerPoint) -> Windows.Win32.System.WinRT.IInspectable_head: ...
    @winrt_mixinmethod
    def ProcessPointerUp(self: Windows.UI.Input.Inking.IInkManager, pointerPoint: Windows.UI.Input.PointerPoint) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def SetDefaultDrawingAttributes(self: Windows.UI.Input.Inking.IInkManager, drawingAttributes: Windows.UI.Input.Inking.InkDrawingAttributes) -> Void: ...
    @winrt_mixinmethod
    def RecognizeAsync2(self: Windows.UI.Input.Inking.IInkManager, recognitionTarget: Windows.UI.Input.Inking.InkRecognitionTarget) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.InkRecognitionResult]]: ...
    @winrt_mixinmethod
    def get_BoundingRect(self: Windows.UI.Input.Inking.IInkStrokeContainer) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def AddStroke(self: Windows.UI.Input.Inking.IInkStrokeContainer, stroke: Windows.UI.Input.Inking.InkStroke) -> Void: ...
    @winrt_mixinmethod
    def DeleteSelected(self: Windows.UI.Input.Inking.IInkStrokeContainer) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def MoveSelected(self: Windows.UI.Input.Inking.IInkStrokeContainer, translation: Windows.Foundation.Point) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def SelectWithPolyLine(self: Windows.UI.Input.Inking.IInkStrokeContainer, polyline: Windows.Foundation.Collections.IIterable[Windows.Foundation.Point]) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def SelectWithLine(self: Windows.UI.Input.Inking.IInkStrokeContainer, from_: Windows.Foundation.Point, to: Windows.Foundation.Point) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def CopySelectedToClipboard(self: Windows.UI.Input.Inking.IInkStrokeContainer) -> Void: ...
    @winrt_mixinmethod
    def PasteFromClipboard(self: Windows.UI.Input.Inking.IInkStrokeContainer, position: Windows.Foundation.Point) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def CanPasteFromClipboard(self: Windows.UI.Input.Inking.IInkStrokeContainer) -> Boolean: ...
    @winrt_mixinmethod
    def LoadAsync(self: Windows.UI.Input.Inking.IInkStrokeContainer, inputStream: Windows.Storage.Streams.IInputStream) -> Windows.Foundation.IAsyncActionWithProgress[UInt64]: ...
    @winrt_mixinmethod
    def SaveAsync(self: Windows.UI.Input.Inking.IInkStrokeContainer, outputStream: Windows.Storage.Streams.IOutputStream) -> Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
    @winrt_mixinmethod
    def UpdateRecognitionResults(self: Windows.UI.Input.Inking.IInkStrokeContainer, recognitionResults: Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.InkRecognitionResult]) -> Void: ...
    @winrt_mixinmethod
    def GetStrokes(self: Windows.UI.Input.Inking.IInkStrokeContainer) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.InkStroke]: ...
    @winrt_mixinmethod
    def GetRecognitionResults(self: Windows.UI.Input.Inking.IInkStrokeContainer) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.InkRecognitionResult]: ...
    @winrt_mixinmethod
    def SetDefaultRecognizer(self: Windows.UI.Input.Inking.IInkRecognizerContainer, recognizer: Windows.UI.Input.Inking.InkRecognizer) -> Void: ...
    @winrt_mixinmethod
    def RecognizeAsync(self: Windows.UI.Input.Inking.IInkRecognizerContainer, strokeCollection: Windows.UI.Input.Inking.InkStrokeContainer, recognitionTarget: Windows.UI.Input.Inking.InkRecognitionTarget) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.InkRecognitionResult]]: ...
    @winrt_mixinmethod
    def GetRecognizers(self: Windows.UI.Input.Inking.IInkRecognizerContainer) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.InkRecognizer]: ...
    Mode = property(get_Mode, put_Mode)
    BoundingRect = property(get_BoundingRect, None)
InkManipulationMode = Int32
InkManipulationMode_Inking: InkManipulationMode = 0
InkManipulationMode_Erasing: InkManipulationMode = 1
InkManipulationMode_Selecting: InkManipulationMode = 2
class InkModelerAttributes(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Input.Inking.IInkModelerAttributes
    _classid_ = 'Windows.UI.Input.Inking.InkModelerAttributes'
    @winrt_mixinmethod
    def get_PredictionTime(self: Windows.UI.Input.Inking.IInkModelerAttributes) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_PredictionTime(self: Windows.UI.Input.Inking.IInkModelerAttributes, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_ScalingFactor(self: Windows.UI.Input.Inking.IInkModelerAttributes) -> Single: ...
    @winrt_mixinmethod
    def put_ScalingFactor(self: Windows.UI.Input.Inking.IInkModelerAttributes, value: Single) -> Void: ...
    @winrt_mixinmethod
    def get_UseVelocityBasedPressure(self: Windows.UI.Input.Inking.IInkModelerAttributes2) -> Boolean: ...
    @winrt_mixinmethod
    def put_UseVelocityBasedPressure(self: Windows.UI.Input.Inking.IInkModelerAttributes2, value: Boolean) -> Void: ...
    PredictionTime = property(get_PredictionTime, put_PredictionTime)
    ScalingFactor = property(get_ScalingFactor, put_ScalingFactor)
    UseVelocityBasedPressure = property(get_UseVelocityBasedPressure, put_UseVelocityBasedPressure)
InkPersistenceFormat = Int32
InkPersistenceFormat_GifWithEmbeddedIsf: InkPersistenceFormat = 0
InkPersistenceFormat_Isf: InkPersistenceFormat = 1
class InkPoint(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Input.Inking.IInkPoint
    _classid_ = 'Windows.UI.Input.Inking.InkPoint'
    @winrt_factorymethod
    def CreateInkPointWithTiltAndTimestamp(cls: Windows.UI.Input.Inking.IInkPointFactory2, position: Windows.Foundation.Point, pressure: Single, tiltX: Single, tiltY: Single, timestamp: UInt64) -> Windows.UI.Input.Inking.InkPoint: ...
    @winrt_factorymethod
    def CreateInkPoint(cls: Windows.UI.Input.Inking.IInkPointFactory, position: Windows.Foundation.Point, pressure: Single) -> Windows.UI.Input.Inking.InkPoint: ...
    @winrt_mixinmethod
    def get_Position(self: Windows.UI.Input.Inking.IInkPoint) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Pressure(self: Windows.UI.Input.Inking.IInkPoint) -> Single: ...
    @winrt_mixinmethod
    def get_TiltX(self: Windows.UI.Input.Inking.IInkPoint2) -> Single: ...
    @winrt_mixinmethod
    def get_TiltY(self: Windows.UI.Input.Inking.IInkPoint2) -> Single: ...
    @winrt_mixinmethod
    def get_Timestamp(self: Windows.UI.Input.Inking.IInkPoint2) -> UInt64: ...
    Position = property(get_Position, None)
    Pressure = property(get_Pressure, None)
    TiltX = property(get_TiltX, None)
    TiltY = property(get_TiltY, None)
    Timestamp = property(get_Timestamp, None)
class InkPresenter(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Input.Inking.IInkPresenter
    _classid_ = 'Windows.UI.Input.Inking.InkPresenter'
    @winrt_mixinmethod
    def get_IsInputEnabled(self: Windows.UI.Input.Inking.IInkPresenter) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsInputEnabled(self: Windows.UI.Input.Inking.IInkPresenter, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_InputDeviceTypes(self: Windows.UI.Input.Inking.IInkPresenter) -> Windows.UI.Core.CoreInputDeviceTypes: ...
    @winrt_mixinmethod
    def put_InputDeviceTypes(self: Windows.UI.Input.Inking.IInkPresenter, value: Windows.UI.Core.CoreInputDeviceTypes) -> Void: ...
    @winrt_mixinmethod
    def get_UnprocessedInput(self: Windows.UI.Input.Inking.IInkPresenter) -> Windows.UI.Input.Inking.InkUnprocessedInput: ...
    @winrt_mixinmethod
    def get_StrokeInput(self: Windows.UI.Input.Inking.IInkPresenter) -> Windows.UI.Input.Inking.InkStrokeInput: ...
    @winrt_mixinmethod
    def get_InputProcessingConfiguration(self: Windows.UI.Input.Inking.IInkPresenter) -> Windows.UI.Input.Inking.InkInputProcessingConfiguration: ...
    @winrt_mixinmethod
    def get_StrokeContainer(self: Windows.UI.Input.Inking.IInkPresenter) -> Windows.UI.Input.Inking.InkStrokeContainer: ...
    @winrt_mixinmethod
    def put_StrokeContainer(self: Windows.UI.Input.Inking.IInkPresenter, value: Windows.UI.Input.Inking.InkStrokeContainer) -> Void: ...
    @winrt_mixinmethod
    def CopyDefaultDrawingAttributes(self: Windows.UI.Input.Inking.IInkPresenter) -> Windows.UI.Input.Inking.InkDrawingAttributes: ...
    @winrt_mixinmethod
    def UpdateDefaultDrawingAttributes(self: Windows.UI.Input.Inking.IInkPresenter, value: Windows.UI.Input.Inking.InkDrawingAttributes) -> Void: ...
    @winrt_mixinmethod
    def ActivateCustomDrying(self: Windows.UI.Input.Inking.IInkPresenter) -> Windows.UI.Input.Inking.InkSynchronizer: ...
    @winrt_mixinmethod
    def SetPredefinedConfiguration(self: Windows.UI.Input.Inking.IInkPresenter, value: Windows.UI.Input.Inking.InkPresenterPredefinedConfiguration) -> Void: ...
    @winrt_mixinmethod
    def add_StrokesCollected(self: Windows.UI.Input.Inking.IInkPresenter, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.InkPresenter, Windows.UI.Input.Inking.InkStrokesCollectedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StrokesCollected(self: Windows.UI.Input.Inking.IInkPresenter, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_StrokesErased(self: Windows.UI.Input.Inking.IInkPresenter, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.InkPresenter, Windows.UI.Input.Inking.InkStrokesErasedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StrokesErased(self: Windows.UI.Input.Inking.IInkPresenter, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_HighContrastAdjustment(self: Windows.UI.Input.Inking.IInkPresenter2) -> Windows.UI.Input.Inking.InkHighContrastAdjustment: ...
    @winrt_mixinmethod
    def put_HighContrastAdjustment(self: Windows.UI.Input.Inking.IInkPresenter2, value: Windows.UI.Input.Inking.InkHighContrastAdjustment) -> Void: ...
    @winrt_mixinmethod
    def get_InputConfiguration(self: Windows.UI.Input.Inking.IInkPresenter3) -> Windows.UI.Input.Inking.InkInputConfiguration: ...
    IsInputEnabled = property(get_IsInputEnabled, put_IsInputEnabled)
    InputDeviceTypes = property(get_InputDeviceTypes, put_InputDeviceTypes)
    UnprocessedInput = property(get_UnprocessedInput, None)
    StrokeInput = property(get_StrokeInput, None)
    InputProcessingConfiguration = property(get_InputProcessingConfiguration, None)
    StrokeContainer = property(get_StrokeContainer, put_StrokeContainer)
    HighContrastAdjustment = property(get_HighContrastAdjustment, put_HighContrastAdjustment)
    InputConfiguration = property(get_InputConfiguration, None)
InkPresenterPredefinedConfiguration = Int32
InkPresenterPredefinedConfiguration_SimpleSinglePointer: InkPresenterPredefinedConfiguration = 0
InkPresenterPredefinedConfiguration_SimpleMultiplePointer: InkPresenterPredefinedConfiguration = 1
class InkPresenterProtractor(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Input.Inking.IInkPresenterProtractor
    _classid_ = 'Windows.UI.Input.Inking.InkPresenterProtractor'
    @winrt_factorymethod
    def Create(cls: Windows.UI.Input.Inking.IInkPresenterProtractorFactory, inkPresenter: Windows.UI.Input.Inking.InkPresenter) -> Windows.UI.Input.Inking.InkPresenterProtractor: ...
    @winrt_mixinmethod
    def get_AreTickMarksVisible(self: Windows.UI.Input.Inking.IInkPresenterProtractor) -> Boolean: ...
    @winrt_mixinmethod
    def put_AreTickMarksVisible(self: Windows.UI.Input.Inking.IInkPresenterProtractor, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_AreRaysVisible(self: Windows.UI.Input.Inking.IInkPresenterProtractor) -> Boolean: ...
    @winrt_mixinmethod
    def put_AreRaysVisible(self: Windows.UI.Input.Inking.IInkPresenterProtractor, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsCenterMarkerVisible(self: Windows.UI.Input.Inking.IInkPresenterProtractor) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsCenterMarkerVisible(self: Windows.UI.Input.Inking.IInkPresenterProtractor, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsAngleReadoutVisible(self: Windows.UI.Input.Inking.IInkPresenterProtractor) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsAngleReadoutVisible(self: Windows.UI.Input.Inking.IInkPresenterProtractor, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsResizable(self: Windows.UI.Input.Inking.IInkPresenterProtractor) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsResizable(self: Windows.UI.Input.Inking.IInkPresenterProtractor, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Radius(self: Windows.UI.Input.Inking.IInkPresenterProtractor) -> Double: ...
    @winrt_mixinmethod
    def put_Radius(self: Windows.UI.Input.Inking.IInkPresenterProtractor, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_AccentColor(self: Windows.UI.Input.Inking.IInkPresenterProtractor) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_AccentColor(self: Windows.UI.Input.Inking.IInkPresenterProtractor, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.UI.Input.Inking.IInkPresenterStencil) -> Windows.UI.Input.Inking.InkPresenterStencilKind: ...
    @winrt_mixinmethod
    def get_IsVisible(self: Windows.UI.Input.Inking.IInkPresenterStencil) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsVisible(self: Windows.UI.Input.Inking.IInkPresenterStencil, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_BackgroundColor(self: Windows.UI.Input.Inking.IInkPresenterStencil) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_BackgroundColor(self: Windows.UI.Input.Inking.IInkPresenterStencil, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_ForegroundColor(self: Windows.UI.Input.Inking.IInkPresenterStencil) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_ForegroundColor(self: Windows.UI.Input.Inking.IInkPresenterStencil, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_Transform(self: Windows.UI.Input.Inking.IInkPresenterStencil) -> Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_mixinmethod
    def put_Transform(self: Windows.UI.Input.Inking.IInkPresenterStencil, value: Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    AreTickMarksVisible = property(get_AreTickMarksVisible, put_AreTickMarksVisible)
    AreRaysVisible = property(get_AreRaysVisible, put_AreRaysVisible)
    IsCenterMarkerVisible = property(get_IsCenterMarkerVisible, put_IsCenterMarkerVisible)
    IsAngleReadoutVisible = property(get_IsAngleReadoutVisible, put_IsAngleReadoutVisible)
    IsResizable = property(get_IsResizable, put_IsResizable)
    Radius = property(get_Radius, put_Radius)
    AccentColor = property(get_AccentColor, put_AccentColor)
    Kind = property(get_Kind, None)
    IsVisible = property(get_IsVisible, put_IsVisible)
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    ForegroundColor = property(get_ForegroundColor, put_ForegroundColor)
    Transform = property(get_Transform, put_Transform)
class InkPresenterRuler(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Input.Inking.IInkPresenterRuler
    _classid_ = 'Windows.UI.Input.Inking.InkPresenterRuler'
    @winrt_factorymethod
    def Create(cls: Windows.UI.Input.Inking.IInkPresenterRulerFactory, inkPresenter: Windows.UI.Input.Inking.InkPresenter) -> Windows.UI.Input.Inking.InkPresenterRuler: ...
    @winrt_mixinmethod
    def get_Length(self: Windows.UI.Input.Inking.IInkPresenterRuler) -> Double: ...
    @winrt_mixinmethod
    def put_Length(self: Windows.UI.Input.Inking.IInkPresenterRuler, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Width(self: Windows.UI.Input.Inking.IInkPresenterRuler) -> Double: ...
    @winrt_mixinmethod
    def put_Width(self: Windows.UI.Input.Inking.IInkPresenterRuler, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Kind(self: Windows.UI.Input.Inking.IInkPresenterStencil) -> Windows.UI.Input.Inking.InkPresenterStencilKind: ...
    @winrt_mixinmethod
    def get_IsVisible(self: Windows.UI.Input.Inking.IInkPresenterStencil) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsVisible(self: Windows.UI.Input.Inking.IInkPresenterStencil, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_BackgroundColor(self: Windows.UI.Input.Inking.IInkPresenterStencil) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_BackgroundColor(self: Windows.UI.Input.Inking.IInkPresenterStencil, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_ForegroundColor(self: Windows.UI.Input.Inking.IInkPresenterStencil) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_ForegroundColor(self: Windows.UI.Input.Inking.IInkPresenterStencil, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_Transform(self: Windows.UI.Input.Inking.IInkPresenterStencil) -> Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_mixinmethod
    def put_Transform(self: Windows.UI.Input.Inking.IInkPresenterStencil, value: Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    @winrt_mixinmethod
    def get_AreTickMarksVisible(self: Windows.UI.Input.Inking.IInkPresenterRuler2) -> Boolean: ...
    @winrt_mixinmethod
    def put_AreTickMarksVisible(self: Windows.UI.Input.Inking.IInkPresenterRuler2, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsCompassVisible(self: Windows.UI.Input.Inking.IInkPresenterRuler2) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsCompassVisible(self: Windows.UI.Input.Inking.IInkPresenterRuler2, value: Boolean) -> Void: ...
    Length = property(get_Length, put_Length)
    Width = property(get_Width, put_Width)
    Kind = property(get_Kind, None)
    IsVisible = property(get_IsVisible, put_IsVisible)
    BackgroundColor = property(get_BackgroundColor, put_BackgroundColor)
    ForegroundColor = property(get_ForegroundColor, put_ForegroundColor)
    Transform = property(get_Transform, put_Transform)
    AreTickMarksVisible = property(get_AreTickMarksVisible, put_AreTickMarksVisible)
    IsCompassVisible = property(get_IsCompassVisible, put_IsCompassVisible)
InkPresenterStencilKind = Int32
InkPresenterStencilKind_Other: InkPresenterStencilKind = 0
InkPresenterStencilKind_Ruler: InkPresenterStencilKind = 1
InkPresenterStencilKind_Protractor: InkPresenterStencilKind = 2
class InkRecognitionResult(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Input.Inking.IInkRecognitionResult
    _classid_ = 'Windows.UI.Input.Inking.InkRecognitionResult'
    @winrt_mixinmethod
    def get_BoundingRect(self: Windows.UI.Input.Inking.IInkRecognitionResult) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def GetTextCandidates(self: Windows.UI.Input.Inking.IInkRecognitionResult) -> Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def GetStrokes(self: Windows.UI.Input.Inking.IInkRecognitionResult) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.InkStroke]: ...
    BoundingRect = property(get_BoundingRect, None)
InkRecognitionTarget = Int32
InkRecognitionTarget_All: InkRecognitionTarget = 0
InkRecognitionTarget_Selected: InkRecognitionTarget = 1
InkRecognitionTarget_Recent: InkRecognitionTarget = 2
class InkRecognizer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Input.Inking.IInkRecognizer
    _classid_ = 'Windows.UI.Input.Inking.InkRecognizer'
    @winrt_mixinmethod
    def get_Name(self: Windows.UI.Input.Inking.IInkRecognizer) -> WinRT_String: ...
    Name = property(get_Name, None)
class InkRecognizerContainer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Input.Inking.IInkRecognizerContainer
    _classid_ = 'Windows.UI.Input.Inking.InkRecognizerContainer'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Input.Inking.InkRecognizerContainer: ...
    @winrt_mixinmethod
    def SetDefaultRecognizer(self: Windows.UI.Input.Inking.IInkRecognizerContainer, recognizer: Windows.UI.Input.Inking.InkRecognizer) -> Void: ...
    @winrt_mixinmethod
    def RecognizeAsync(self: Windows.UI.Input.Inking.IInkRecognizerContainer, strokeCollection: Windows.UI.Input.Inking.InkStrokeContainer, recognitionTarget: Windows.UI.Input.Inking.InkRecognitionTarget) -> Windows.Foundation.IAsyncOperation[Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.InkRecognitionResult]]: ...
    @winrt_mixinmethod
    def GetRecognizers(self: Windows.UI.Input.Inking.IInkRecognizerContainer) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.InkRecognizer]: ...
class InkStroke(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Input.Inking.IInkStroke
    _classid_ = 'Windows.UI.Input.Inking.InkStroke'
    @winrt_mixinmethod
    def get_DrawingAttributes(self: Windows.UI.Input.Inking.IInkStroke) -> Windows.UI.Input.Inking.InkDrawingAttributes: ...
    @winrt_mixinmethod
    def put_DrawingAttributes(self: Windows.UI.Input.Inking.IInkStroke, value: Windows.UI.Input.Inking.InkDrawingAttributes) -> Void: ...
    @winrt_mixinmethod
    def get_BoundingRect(self: Windows.UI.Input.Inking.IInkStroke) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_Selected(self: Windows.UI.Input.Inking.IInkStroke) -> Boolean: ...
    @winrt_mixinmethod
    def put_Selected(self: Windows.UI.Input.Inking.IInkStroke, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_Recognized(self: Windows.UI.Input.Inking.IInkStroke) -> Boolean: ...
    @winrt_mixinmethod
    def GetRenderingSegments(self: Windows.UI.Input.Inking.IInkStroke) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.InkStrokeRenderingSegment]: ...
    @winrt_mixinmethod
    def Clone(self: Windows.UI.Input.Inking.IInkStroke) -> Windows.UI.Input.Inking.InkStroke: ...
    @winrt_mixinmethod
    def get_PointTransform(self: Windows.UI.Input.Inking.IInkStroke2) -> Windows.Foundation.Numerics.Matrix3x2: ...
    @winrt_mixinmethod
    def put_PointTransform(self: Windows.UI.Input.Inking.IInkStroke2, value: Windows.Foundation.Numerics.Matrix3x2) -> Void: ...
    @winrt_mixinmethod
    def GetInkPoints(self: Windows.UI.Input.Inking.IInkStroke2) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.InkPoint]: ...
    @winrt_mixinmethod
    def get_Id(self: Windows.UI.Input.Inking.IInkStroke3) -> UInt32: ...
    @winrt_mixinmethod
    def get_StrokeStartedTime(self: Windows.UI.Input.Inking.IInkStroke3) -> Windows.Foundation.IReference[Windows.Foundation.DateTime]: ...
    @winrt_mixinmethod
    def put_StrokeStartedTime(self: Windows.UI.Input.Inking.IInkStroke3, value: Windows.Foundation.IReference[Windows.Foundation.DateTime]) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeDuration(self: Windows.UI.Input.Inking.IInkStroke3) -> Windows.Foundation.IReference[Windows.Foundation.TimeSpan]: ...
    @winrt_mixinmethod
    def put_StrokeDuration(self: Windows.UI.Input.Inking.IInkStroke3, value: Windows.Foundation.IReference[Windows.Foundation.TimeSpan]) -> Void: ...
    @winrt_mixinmethod
    def get_PointerId(self: Windows.UI.Input.Inking.IInkStroke4) -> UInt32: ...
    DrawingAttributes = property(get_DrawingAttributes, put_DrawingAttributes)
    BoundingRect = property(get_BoundingRect, None)
    Selected = property(get_Selected, put_Selected)
    Recognized = property(get_Recognized, None)
    PointTransform = property(get_PointTransform, put_PointTransform)
    Id = property(get_Id, None)
    StrokeStartedTime = property(get_StrokeStartedTime, put_StrokeStartedTime)
    StrokeDuration = property(get_StrokeDuration, put_StrokeDuration)
    PointerId = property(get_PointerId, None)
class InkStrokeBuilder(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Input.Inking.IInkStrokeBuilder
    _classid_ = 'Windows.UI.Input.Inking.InkStrokeBuilder'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Input.Inking.InkStrokeBuilder: ...
    @winrt_mixinmethod
    def BeginStroke(self: Windows.UI.Input.Inking.IInkStrokeBuilder, pointerPoint: Windows.UI.Input.PointerPoint) -> Void: ...
    @winrt_mixinmethod
    def AppendToStroke(self: Windows.UI.Input.Inking.IInkStrokeBuilder, pointerPoint: Windows.UI.Input.PointerPoint) -> Windows.UI.Input.PointerPoint: ...
    @winrt_mixinmethod
    def EndStroke(self: Windows.UI.Input.Inking.IInkStrokeBuilder, pointerPoint: Windows.UI.Input.PointerPoint) -> Windows.UI.Input.Inking.InkStroke: ...
    @winrt_mixinmethod
    def CreateStroke(self: Windows.UI.Input.Inking.IInkStrokeBuilder, points: Windows.Foundation.Collections.IIterable[Windows.Foundation.Point]) -> Windows.UI.Input.Inking.InkStroke: ...
    @winrt_mixinmethod
    def SetDefaultDrawingAttributes(self: Windows.UI.Input.Inking.IInkStrokeBuilder, drawingAttributes: Windows.UI.Input.Inking.InkDrawingAttributes) -> Void: ...
    @winrt_mixinmethod
    def CreateStrokeFromInkPoints(self: Windows.UI.Input.Inking.IInkStrokeBuilder2, inkPoints: Windows.Foundation.Collections.IIterable[Windows.UI.Input.Inking.InkPoint], transform: Windows.Foundation.Numerics.Matrix3x2) -> Windows.UI.Input.Inking.InkStroke: ...
    @winrt_mixinmethod
    def CreateStrokeFromInkPoints(self: Windows.UI.Input.Inking.IInkStrokeBuilder2, inkPoints: Windows.Foundation.Collections.IIterable[Windows.UI.Input.Inking.InkPoint], transform: Windows.Foundation.Numerics.Matrix3x2, strokeStartedTime: Windows.Foundation.IReference[Windows.Foundation.DateTime], strokeDuration: Windows.Foundation.IReference[Windows.Foundation.TimeSpan]) -> Windows.UI.Input.Inking.InkStroke: ...
class InkStrokeContainer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Input.Inking.IInkStrokeContainer
    _classid_ = 'Windows.UI.Input.Inking.InkStrokeContainer'
    @winrt_activatemethod
    def CreateInstance(cls) -> Windows.UI.Input.Inking.InkStrokeContainer: ...
    @winrt_mixinmethod
    def get_BoundingRect(self: Windows.UI.Input.Inking.IInkStrokeContainer) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def AddStroke(self: Windows.UI.Input.Inking.IInkStrokeContainer, stroke: Windows.UI.Input.Inking.InkStroke) -> Void: ...
    @winrt_mixinmethod
    def DeleteSelected(self: Windows.UI.Input.Inking.IInkStrokeContainer) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def MoveSelected(self: Windows.UI.Input.Inking.IInkStrokeContainer, translation: Windows.Foundation.Point) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def SelectWithPolyLine(self: Windows.UI.Input.Inking.IInkStrokeContainer, polyline: Windows.Foundation.Collections.IIterable[Windows.Foundation.Point]) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def SelectWithLine(self: Windows.UI.Input.Inking.IInkStrokeContainer, from_: Windows.Foundation.Point, to: Windows.Foundation.Point) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def CopySelectedToClipboard(self: Windows.UI.Input.Inking.IInkStrokeContainer) -> Void: ...
    @winrt_mixinmethod
    def PasteFromClipboard(self: Windows.UI.Input.Inking.IInkStrokeContainer, position: Windows.Foundation.Point) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def CanPasteFromClipboard(self: Windows.UI.Input.Inking.IInkStrokeContainer) -> Boolean: ...
    @winrt_mixinmethod
    def LoadAsync(self: Windows.UI.Input.Inking.IInkStrokeContainer, inputStream: Windows.Storage.Streams.IInputStream) -> Windows.Foundation.IAsyncActionWithProgress[UInt64]: ...
    @winrt_mixinmethod
    def SaveAsync(self: Windows.UI.Input.Inking.IInkStrokeContainer, outputStream: Windows.Storage.Streams.IOutputStream) -> Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
    @winrt_mixinmethod
    def UpdateRecognitionResults(self: Windows.UI.Input.Inking.IInkStrokeContainer, recognitionResults: Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.InkRecognitionResult]) -> Void: ...
    @winrt_mixinmethod
    def GetStrokes(self: Windows.UI.Input.Inking.IInkStrokeContainer) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.InkStroke]: ...
    @winrt_mixinmethod
    def GetRecognitionResults(self: Windows.UI.Input.Inking.IInkStrokeContainer) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.InkRecognitionResult]: ...
    @winrt_mixinmethod
    def AddStrokes(self: Windows.UI.Input.Inking.IInkStrokeContainer2, strokes: Windows.Foundation.Collections.IIterable[Windows.UI.Input.Inking.InkStroke]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.UI.Input.Inking.IInkStrokeContainer2) -> Void: ...
    @winrt_mixinmethod
    def SaveWithFormatAsync(self: Windows.UI.Input.Inking.IInkStrokeContainer3, outputStream: Windows.Storage.Streams.IOutputStream, inkPersistenceFormat: Windows.UI.Input.Inking.InkPersistenceFormat) -> Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
    @winrt_mixinmethod
    def GetStrokeById(self: Windows.UI.Input.Inking.IInkStrokeContainer3, id: UInt32) -> Windows.UI.Input.Inking.InkStroke: ...
    BoundingRect = property(get_BoundingRect, None)
class InkStrokeInput(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Input.Inking.IInkStrokeInput
    _classid_ = 'Windows.UI.Input.Inking.InkStrokeInput'
    @winrt_mixinmethod
    def add_StrokeStarted(self: Windows.UI.Input.Inking.IInkStrokeInput, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.InkStrokeInput, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StrokeStarted(self: Windows.UI.Input.Inking.IInkStrokeInput, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_StrokeContinued(self: Windows.UI.Input.Inking.IInkStrokeInput, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.InkStrokeInput, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StrokeContinued(self: Windows.UI.Input.Inking.IInkStrokeInput, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_StrokeEnded(self: Windows.UI.Input.Inking.IInkStrokeInput, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.InkStrokeInput, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StrokeEnded(self: Windows.UI.Input.Inking.IInkStrokeInput, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_StrokeCanceled(self: Windows.UI.Input.Inking.IInkStrokeInput, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.InkStrokeInput, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_StrokeCanceled(self: Windows.UI.Input.Inking.IInkStrokeInput, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_InkPresenter(self: Windows.UI.Input.Inking.IInkStrokeInput) -> Windows.UI.Input.Inking.InkPresenter: ...
    InkPresenter = property(get_InkPresenter, None)
class InkStrokeRenderingSegment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Input.Inking.IInkStrokeRenderingSegment
    _classid_ = 'Windows.UI.Input.Inking.InkStrokeRenderingSegment'
    @winrt_mixinmethod
    def get_Position(self: Windows.UI.Input.Inking.IInkStrokeRenderingSegment) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_BezierControlPoint1(self: Windows.UI.Input.Inking.IInkStrokeRenderingSegment) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_BezierControlPoint2(self: Windows.UI.Input.Inking.IInkStrokeRenderingSegment) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Pressure(self: Windows.UI.Input.Inking.IInkStrokeRenderingSegment) -> Single: ...
    @winrt_mixinmethod
    def get_TiltX(self: Windows.UI.Input.Inking.IInkStrokeRenderingSegment) -> Single: ...
    @winrt_mixinmethod
    def get_TiltY(self: Windows.UI.Input.Inking.IInkStrokeRenderingSegment) -> Single: ...
    @winrt_mixinmethod
    def get_Twist(self: Windows.UI.Input.Inking.IInkStrokeRenderingSegment) -> Single: ...
    Position = property(get_Position, None)
    BezierControlPoint1 = property(get_BezierControlPoint1, None)
    BezierControlPoint2 = property(get_BezierControlPoint2, None)
    Pressure = property(get_Pressure, None)
    TiltX = property(get_TiltX, None)
    TiltY = property(get_TiltY, None)
    Twist = property(get_Twist, None)
class InkStrokesCollectedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Input.Inking.IInkStrokesCollectedEventArgs
    _classid_ = 'Windows.UI.Input.Inking.InkStrokesCollectedEventArgs'
    @winrt_mixinmethod
    def get_Strokes(self: Windows.UI.Input.Inking.IInkStrokesCollectedEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.InkStroke]: ...
    Strokes = property(get_Strokes, None)
class InkStrokesErasedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Input.Inking.IInkStrokesErasedEventArgs
    _classid_ = 'Windows.UI.Input.Inking.InkStrokesErasedEventArgs'
    @winrt_mixinmethod
    def get_Strokes(self: Windows.UI.Input.Inking.IInkStrokesErasedEventArgs) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.InkStroke]: ...
    Strokes = property(get_Strokes, None)
class InkSynchronizer(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Input.Inking.IInkSynchronizer
    _classid_ = 'Windows.UI.Input.Inking.InkSynchronizer'
    @winrt_mixinmethod
    def BeginDry(self: Windows.UI.Input.Inking.IInkSynchronizer) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Input.Inking.InkStroke]: ...
    @winrt_mixinmethod
    def EndDry(self: Windows.UI.Input.Inking.IInkSynchronizer) -> Void: ...
class InkUnprocessedInput(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Input.Inking.IInkUnprocessedInput
    _classid_ = 'Windows.UI.Input.Inking.InkUnprocessedInput'
    @winrt_mixinmethod
    def add_PointerEntered(self: Windows.UI.Input.Inking.IInkUnprocessedInput, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.InkUnprocessedInput, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerEntered(self: Windows.UI.Input.Inking.IInkUnprocessedInput, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerHovered(self: Windows.UI.Input.Inking.IInkUnprocessedInput, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.InkUnprocessedInput, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerHovered(self: Windows.UI.Input.Inking.IInkUnprocessedInput, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerExited(self: Windows.UI.Input.Inking.IInkUnprocessedInput, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.InkUnprocessedInput, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerExited(self: Windows.UI.Input.Inking.IInkUnprocessedInput, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerPressed(self: Windows.UI.Input.Inking.IInkUnprocessedInput, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.InkUnprocessedInput, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerPressed(self: Windows.UI.Input.Inking.IInkUnprocessedInput, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerMoved(self: Windows.UI.Input.Inking.IInkUnprocessedInput, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.InkUnprocessedInput, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerMoved(self: Windows.UI.Input.Inking.IInkUnprocessedInput, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerReleased(self: Windows.UI.Input.Inking.IInkUnprocessedInput, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.InkUnprocessedInput, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerReleased(self: Windows.UI.Input.Inking.IInkUnprocessedInput, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_PointerLost(self: Windows.UI.Input.Inking.IInkUnprocessedInput, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Input.Inking.InkUnprocessedInput, Windows.UI.Core.PointerEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_PointerLost(self: Windows.UI.Input.Inking.IInkUnprocessedInput, cookie: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def get_InkPresenter(self: Windows.UI.Input.Inking.IInkUnprocessedInput) -> Windows.UI.Input.Inking.InkPresenter: ...
    InkPresenter = property(get_InkPresenter, None)
class PenAndInkSettings(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Input.Inking.IPenAndInkSettings
    _classid_ = 'Windows.UI.Input.Inking.PenAndInkSettings'
    @winrt_mixinmethod
    def get_IsHandwritingDirectlyIntoTextFieldEnabled(self: Windows.UI.Input.Inking.IPenAndInkSettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_PenHandedness(self: Windows.UI.Input.Inking.IPenAndInkSettings) -> Windows.UI.Input.Inking.PenHandedness: ...
    @winrt_mixinmethod
    def get_HandwritingLineHeight(self: Windows.UI.Input.Inking.IPenAndInkSettings) -> Windows.UI.Input.Inking.HandwritingLineHeight: ...
    @winrt_mixinmethod
    def get_FontFamilyName(self: Windows.UI.Input.Inking.IPenAndInkSettings) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_UserConsentsToHandwritingTelemetryCollection(self: Windows.UI.Input.Inking.IPenAndInkSettings) -> Boolean: ...
    @winrt_mixinmethod
    def get_IsTouchHandwritingEnabled(self: Windows.UI.Input.Inking.IPenAndInkSettings) -> Boolean: ...
    @winrt_mixinmethod
    def SetPenHandedness(self: Windows.UI.Input.Inking.IPenAndInkSettings2, value: Windows.UI.Input.Inking.PenHandedness) -> Void: ...
    @winrt_classmethod
    def GetDefault(cls: Windows.UI.Input.Inking.IPenAndInkSettingsStatics) -> Windows.UI.Input.Inking.PenAndInkSettings: ...
    IsHandwritingDirectlyIntoTextFieldEnabled = property(get_IsHandwritingDirectlyIntoTextFieldEnabled, None)
    PenHandedness = property(get_PenHandedness, None)
    HandwritingLineHeight = property(get_HandwritingLineHeight, None)
    FontFamilyName = property(get_FontFamilyName, None)
    UserConsentsToHandwritingTelemetryCollection = property(get_UserConsentsToHandwritingTelemetryCollection, None)
    IsTouchHandwritingEnabled = property(get_IsTouchHandwritingEnabled, None)
PenHandedness = Int32
PenHandedness_Right: PenHandedness = 0
PenHandedness_Left: PenHandedness = 1
PenTipShape = Int32
PenTipShape_Circle: PenTipShape = 0
PenTipShape_Rectangle: PenTipShape = 1
make_head(_module, 'IInkDrawingAttributes')
make_head(_module, 'IInkDrawingAttributes2')
make_head(_module, 'IInkDrawingAttributes3')
make_head(_module, 'IInkDrawingAttributes4')
make_head(_module, 'IInkDrawingAttributes5')
make_head(_module, 'IInkDrawingAttributesPencilProperties')
make_head(_module, 'IInkDrawingAttributesStatics')
make_head(_module, 'IInkInputConfiguration')
make_head(_module, 'IInkInputConfiguration2')
make_head(_module, 'IInkInputProcessingConfiguration')
make_head(_module, 'IInkManager')
make_head(_module, 'IInkModelerAttributes')
make_head(_module, 'IInkModelerAttributes2')
make_head(_module, 'IInkPoint')
make_head(_module, 'IInkPoint2')
make_head(_module, 'IInkPointFactory')
make_head(_module, 'IInkPointFactory2')
make_head(_module, 'IInkPresenter')
make_head(_module, 'IInkPresenter2')
make_head(_module, 'IInkPresenter3')
make_head(_module, 'IInkPresenterProtractor')
make_head(_module, 'IInkPresenterProtractorFactory')
make_head(_module, 'IInkPresenterRuler')
make_head(_module, 'IInkPresenterRuler2')
make_head(_module, 'IInkPresenterRulerFactory')
make_head(_module, 'IInkPresenterStencil')
make_head(_module, 'IInkRecognitionResult')
make_head(_module, 'IInkRecognizer')
make_head(_module, 'IInkRecognizerContainer')
make_head(_module, 'IInkStroke')
make_head(_module, 'IInkStroke2')
make_head(_module, 'IInkStroke3')
make_head(_module, 'IInkStroke4')
make_head(_module, 'IInkStrokeBuilder')
make_head(_module, 'IInkStrokeBuilder2')
make_head(_module, 'IInkStrokeBuilder3')
make_head(_module, 'IInkStrokeContainer')
make_head(_module, 'IInkStrokeContainer2')
make_head(_module, 'IInkStrokeContainer3')
make_head(_module, 'IInkStrokeInput')
make_head(_module, 'IInkStrokeRenderingSegment')
make_head(_module, 'IInkStrokesCollectedEventArgs')
make_head(_module, 'IInkStrokesErasedEventArgs')
make_head(_module, 'IInkSynchronizer')
make_head(_module, 'IInkUnprocessedInput')
make_head(_module, 'IPenAndInkSettings')
make_head(_module, 'IPenAndInkSettings2')
make_head(_module, 'IPenAndInkSettingsStatics')
make_head(_module, 'InkDrawingAttributes')
make_head(_module, 'InkDrawingAttributesPencilProperties')
make_head(_module, 'InkInputConfiguration')
make_head(_module, 'InkInputProcessingConfiguration')
make_head(_module, 'InkManager')
make_head(_module, 'InkModelerAttributes')
make_head(_module, 'InkPoint')
make_head(_module, 'InkPresenter')
make_head(_module, 'InkPresenterProtractor')
make_head(_module, 'InkPresenterRuler')
make_head(_module, 'InkRecognitionResult')
make_head(_module, 'InkRecognizer')
make_head(_module, 'InkRecognizerContainer')
make_head(_module, 'InkStroke')
make_head(_module, 'InkStrokeBuilder')
make_head(_module, 'InkStrokeContainer')
make_head(_module, 'InkStrokeInput')
make_head(_module, 'InkStrokeRenderingSegment')
make_head(_module, 'InkStrokesCollectedEventArgs')
make_head(_module, 'InkStrokesErasedEventArgs')
make_head(_module, 'InkSynchronizer')
make_head(_module, 'InkUnprocessedInput')
make_head(_module, 'PenAndInkSettings')
