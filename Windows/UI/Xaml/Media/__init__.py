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
import Windows.Media.Playback
import Windows.Storage.Streams
import Windows.UI
import Windows.UI.Composition
import Windows.UI.Xaml
import Windows.UI.Xaml.Controls.Primitives
import Windows.UI.Xaml.Media
import Windows.UI.Xaml.Media.Media3D
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
AcrylicBackgroundSource = Int32
AcrylicBackgroundSource_HostBackdrop: AcrylicBackgroundSource = 0
AcrylicBackgroundSource_Backdrop: AcrylicBackgroundSource = 1
class AcrylicBrush(ComPtr):
    extends: Windows.UI.Xaml.Media.XamlCompositionBrushBase
    default_interface: Windows.UI.Xaml.Media.IAcrylicBrush
    _classid_ = 'Windows.UI.Xaml.Media.AcrylicBrush'
    @winrt_commethod(45)
    def get_BackgroundSource(self) -> Windows.UI.Xaml.Media.AcrylicBackgroundSource: ...
    @winrt_commethod(46)
    def put_BackgroundSource(self, value: Windows.UI.Xaml.Media.AcrylicBackgroundSource) -> Void: ...
    @winrt_commethod(47)
    def get_TintColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(48)
    def put_TintColor(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(49)
    def get_TintOpacity(self) -> Double: ...
    @winrt_commethod(50)
    def put_TintOpacity(self, value: Double) -> Void: ...
    @winrt_commethod(51)
    def get_TintTransitionDuration(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(52)
    def put_TintTransitionDuration(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(53)
    def get_AlwaysUseFallback(self) -> Boolean: ...
    @winrt_commethod(54)
    def put_AlwaysUseFallback(self, value: Boolean) -> Void: ...
    @winrt_commethod(55)
    def get_TintLuminosityOpacity(self) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(56)
    def put_TintLuminosityOpacity(self, value: Windows.Foundation.IReference[Double]) -> Void: ...
    @winrt_classmethod
    def get_TintLuminosityOpacityProperty(cls: Windows.UI.Xaml.Media.IAcrylicBrushStatics2) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_BackgroundSourceProperty(cls: Windows.UI.Xaml.Media.IAcrylicBrushStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TintColorProperty(cls: Windows.UI.Xaml.Media.IAcrylicBrushStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TintOpacityProperty(cls: Windows.UI.Xaml.Media.IAcrylicBrushStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TintTransitionDurationProperty(cls: Windows.UI.Xaml.Media.IAcrylicBrushStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AlwaysUseFallbackProperty(cls: Windows.UI.Xaml.Media.IAcrylicBrushStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    BackgroundSource = property(get_BackgroundSource, put_BackgroundSource)
    TintColor = property(get_TintColor, put_TintColor)
    TintOpacity = property(get_TintOpacity, put_TintOpacity)
    TintTransitionDuration = property(get_TintTransitionDuration, put_TintTransitionDuration)
    AlwaysUseFallback = property(get_AlwaysUseFallback, put_AlwaysUseFallback)
    TintLuminosityOpacity = property(get_TintLuminosityOpacity, put_TintLuminosityOpacity)
    TintLuminosityOpacityProperty = property(get_TintLuminosityOpacityProperty, None)
    BackgroundSourceProperty = property(get_BackgroundSourceProperty, None)
    TintColorProperty = property(get_TintColorProperty, None)
    TintOpacityProperty = property(get_TintOpacityProperty, None)
    TintTransitionDurationProperty = property(get_TintTransitionDurationProperty, None)
    AlwaysUseFallbackProperty = property(get_AlwaysUseFallbackProperty, None)
AlignmentX = Int32
AlignmentX_Left: AlignmentX = 0
AlignmentX_Center: AlignmentX = 1
AlignmentX_Right: AlignmentX = 2
AlignmentY = Int32
AlignmentY_Top: AlignmentY = 0
AlignmentY_Center: AlignmentY = 1
AlignmentY_Bottom: AlignmentY = 2
class ArcSegment(ComPtr):
    extends: Windows.UI.Xaml.Media.PathSegment
    default_interface: Windows.UI.Xaml.Media.IArcSegment
    _classid_ = 'Windows.UI.Xaml.Media.ArcSegment'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.ArcSegment: ...
    @winrt_mixinmethod
    def get_Point(self: Windows.UI.Xaml.Media.IArcSegment) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Point(self: Windows.UI.Xaml.Media.IArcSegment, value: Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.UI.Xaml.Media.IArcSegment) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def put_Size(self: Windows.UI.Xaml.Media.IArcSegment, value: Windows.Foundation.Size) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAngle(self: Windows.UI.Xaml.Media.IArcSegment) -> Double: ...
    @winrt_mixinmethod
    def put_RotationAngle(self: Windows.UI.Xaml.Media.IArcSegment, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_IsLargeArc(self: Windows.UI.Xaml.Media.IArcSegment) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsLargeArc(self: Windows.UI.Xaml.Media.IArcSegment, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SweepDirection(self: Windows.UI.Xaml.Media.IArcSegment) -> Windows.UI.Xaml.Media.SweepDirection: ...
    @winrt_mixinmethod
    def put_SweepDirection(self: Windows.UI.Xaml.Media.IArcSegment, value: Windows.UI.Xaml.Media.SweepDirection) -> Void: ...
    @winrt_classmethod
    def get_PointProperty(cls: Windows.UI.Xaml.Media.IArcSegmentStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SizeProperty(cls: Windows.UI.Xaml.Media.IArcSegmentStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RotationAngleProperty(cls: Windows.UI.Xaml.Media.IArcSegmentStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsLargeArcProperty(cls: Windows.UI.Xaml.Media.IArcSegmentStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SweepDirectionProperty(cls: Windows.UI.Xaml.Media.IArcSegmentStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Point = property(get_Point, put_Point)
    Size = property(get_Size, put_Size)
    RotationAngle = property(get_RotationAngle, put_RotationAngle)
    IsLargeArc = property(get_IsLargeArc, put_IsLargeArc)
    SweepDirection = property(get_SweepDirection, put_SweepDirection)
    PointProperty = property(get_PointProperty, None)
    SizeProperty = property(get_SizeProperty, None)
    RotationAngleProperty = property(get_RotationAngleProperty, None)
    IsLargeArcProperty = property(get_IsLargeArcProperty, None)
    SweepDirectionProperty = property(get_SweepDirectionProperty, None)
AudioCategory = Int32
AudioCategory_Other: AudioCategory = 0
AudioCategory_ForegroundOnlyMedia: AudioCategory = 1
AudioCategory_BackgroundCapableMedia: AudioCategory = 2
AudioCategory_Communications: AudioCategory = 3
AudioCategory_Alerts: AudioCategory = 4
AudioCategory_SoundEffects: AudioCategory = 5
AudioCategory_GameEffects: AudioCategory = 6
AudioCategory_GameMedia: AudioCategory = 7
AudioCategory_GameChat: AudioCategory = 8
AudioCategory_Speech: AudioCategory = 9
AudioCategory_Movie: AudioCategory = 10
AudioCategory_Media: AudioCategory = 11
AudioDeviceType = Int32
AudioDeviceType_Console: AudioDeviceType = 0
AudioDeviceType_Multimedia: AudioDeviceType = 1
AudioDeviceType_Communications: AudioDeviceType = 2
class BezierSegment(ComPtr):
    extends: Windows.UI.Xaml.Media.PathSegment
    default_interface: Windows.UI.Xaml.Media.IBezierSegment
    _classid_ = 'Windows.UI.Xaml.Media.BezierSegment'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.BezierSegment: ...
    @winrt_mixinmethod
    def get_Point1(self: Windows.UI.Xaml.Media.IBezierSegment) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Point1(self: Windows.UI.Xaml.Media.IBezierSegment, value: Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_Point2(self: Windows.UI.Xaml.Media.IBezierSegment) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Point2(self: Windows.UI.Xaml.Media.IBezierSegment, value: Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_Point3(self: Windows.UI.Xaml.Media.IBezierSegment) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Point3(self: Windows.UI.Xaml.Media.IBezierSegment, value: Windows.Foundation.Point) -> Void: ...
    @winrt_classmethod
    def get_Point1Property(cls: Windows.UI.Xaml.Media.IBezierSegmentStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_Point2Property(cls: Windows.UI.Xaml.Media.IBezierSegmentStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_Point3Property(cls: Windows.UI.Xaml.Media.IBezierSegmentStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Point1 = property(get_Point1, put_Point1)
    Point2 = property(get_Point2, put_Point2)
    Point3 = property(get_Point3, put_Point3)
    Point1Property = property(get_Point1Property, None)
    Point2Property = property(get_Point2Property, None)
    Point3Property = property(get_Point3Property, None)
class BitmapCache(ComPtr):
    extends: Windows.UI.Xaml.Media.CacheMode
    default_interface: Windows.UI.Xaml.Media.IBitmapCache
    _classid_ = 'Windows.UI.Xaml.Media.BitmapCache'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.BitmapCache: ...
class Brush(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Media.IBrush
    _classid_ = 'Windows.UI.Xaml.Media.Brush'
    @winrt_commethod(18)
    def get_Opacity(self) -> Double: ...
    @winrt_commethod(19)
    def put_Opacity(self, value: Double) -> Void: ...
    @winrt_commethod(20)
    def get_Transform(self) -> Windows.UI.Xaml.Media.Transform: ...
    @winrt_commethod(21)
    def put_Transform(self, value: Windows.UI.Xaml.Media.Transform) -> Void: ...
    @winrt_commethod(22)
    def get_RelativeTransform(self) -> Windows.UI.Xaml.Media.Transform: ...
    @winrt_commethod(23)
    def put_RelativeTransform(self, value: Windows.UI.Xaml.Media.Transform) -> Void: ...
    @winrt_commethod(24)
    def PopulatePropertyInfoOverride(self, propertyName: WinRT_String, animationPropertyInfo: Windows.UI.Composition.AnimationPropertyInfo) -> Void: ...
    @winrt_commethod(25)
    def PopulatePropertyInfo(self, propertyName: WinRT_String, propertyInfo: Windows.UI.Composition.AnimationPropertyInfo) -> Void: ...
    @winrt_classmethod
    def get_OpacityProperty(cls: Windows.UI.Xaml.Media.IBrushStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TransformProperty(cls: Windows.UI.Xaml.Media.IBrushStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RelativeTransformProperty(cls: Windows.UI.Xaml.Media.IBrushStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Opacity = property(get_Opacity, put_Opacity)
    Transform = property(get_Transform, put_Transform)
    RelativeTransform = property(get_RelativeTransform, put_RelativeTransform)
    OpacityProperty = property(get_OpacityProperty, None)
    TransformProperty = property(get_TransformProperty, None)
    RelativeTransformProperty = property(get_RelativeTransformProperty, None)
class BrushCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Brush]
    _classid_ = 'Windows.UI.Xaml.Media.BrushCollection'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.BrushCollection: ...
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Brush], index: UInt32) -> Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Brush]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Brush]) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Media.Brush]: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Brush], value: Windows.UI.Xaml.Media.Brush, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Brush], index: UInt32, value: Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Brush], index: UInt32, value: Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Brush], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Brush], value: Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Brush]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Brush]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Brush], startIndex: UInt32, items: POINTER(Windows.UI.Xaml.Media.Brush)) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Brush], items: POINTER(Windows.UI.Xaml.Media.Brush)) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.Media.Brush]) -> Windows.Foundation.Collections.IIterator[Windows.UI.Xaml.Media.Brush]: ...
    Size = property(get_Size, None)
BrushMappingMode = Int32
BrushMappingMode_Absolute: BrushMappingMode = 0
BrushMappingMode_RelativeToBoundingBox: BrushMappingMode = 1
class CacheMode(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Media.ICacheMode
    _classid_ = 'Windows.UI.Xaml.Media.CacheMode'
ColorInterpolationMode = Int32
ColorInterpolationMode_ScRgbLinearInterpolation: ColorInterpolationMode = 0
ColorInterpolationMode_SRgbLinearInterpolation: ColorInterpolationMode = 1
class CompositeTransform(ComPtr):
    extends: Windows.UI.Xaml.Media.Transform
    default_interface: Windows.UI.Xaml.Media.ICompositeTransform
    _classid_ = 'Windows.UI.Xaml.Media.CompositeTransform'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.CompositeTransform: ...
    @winrt_mixinmethod
    def get_CenterX(self: Windows.UI.Xaml.Media.ICompositeTransform) -> Double: ...
    @winrt_mixinmethod
    def put_CenterX(self: Windows.UI.Xaml.Media.ICompositeTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_CenterY(self: Windows.UI.Xaml.Media.ICompositeTransform) -> Double: ...
    @winrt_mixinmethod
    def put_CenterY(self: Windows.UI.Xaml.Media.ICompositeTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleX(self: Windows.UI.Xaml.Media.ICompositeTransform) -> Double: ...
    @winrt_mixinmethod
    def put_ScaleX(self: Windows.UI.Xaml.Media.ICompositeTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleY(self: Windows.UI.Xaml.Media.ICompositeTransform) -> Double: ...
    @winrt_mixinmethod
    def put_ScaleY(self: Windows.UI.Xaml.Media.ICompositeTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_SkewX(self: Windows.UI.Xaml.Media.ICompositeTransform) -> Double: ...
    @winrt_mixinmethod
    def put_SkewX(self: Windows.UI.Xaml.Media.ICompositeTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_SkewY(self: Windows.UI.Xaml.Media.ICompositeTransform) -> Double: ...
    @winrt_mixinmethod
    def put_SkewY(self: Windows.UI.Xaml.Media.ICompositeTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Rotation(self: Windows.UI.Xaml.Media.ICompositeTransform) -> Double: ...
    @winrt_mixinmethod
    def put_Rotation(self: Windows.UI.Xaml.Media.ICompositeTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_TranslateX(self: Windows.UI.Xaml.Media.ICompositeTransform) -> Double: ...
    @winrt_mixinmethod
    def put_TranslateX(self: Windows.UI.Xaml.Media.ICompositeTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_TranslateY(self: Windows.UI.Xaml.Media.ICompositeTransform) -> Double: ...
    @winrt_mixinmethod
    def put_TranslateY(self: Windows.UI.Xaml.Media.ICompositeTransform, value: Double) -> Void: ...
    @winrt_classmethod
    def get_CenterXProperty(cls: Windows.UI.Xaml.Media.ICompositeTransformStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CenterYProperty(cls: Windows.UI.Xaml.Media.ICompositeTransformStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ScaleXProperty(cls: Windows.UI.Xaml.Media.ICompositeTransformStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ScaleYProperty(cls: Windows.UI.Xaml.Media.ICompositeTransformStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SkewXProperty(cls: Windows.UI.Xaml.Media.ICompositeTransformStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SkewYProperty(cls: Windows.UI.Xaml.Media.ICompositeTransformStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RotationProperty(cls: Windows.UI.Xaml.Media.ICompositeTransformStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TranslateXProperty(cls: Windows.UI.Xaml.Media.ICompositeTransformStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TranslateYProperty(cls: Windows.UI.Xaml.Media.ICompositeTransformStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    CenterX = property(get_CenterX, put_CenterX)
    CenterY = property(get_CenterY, put_CenterY)
    ScaleX = property(get_ScaleX, put_ScaleX)
    ScaleY = property(get_ScaleY, put_ScaleY)
    SkewX = property(get_SkewX, put_SkewX)
    SkewY = property(get_SkewY, put_SkewY)
    Rotation = property(get_Rotation, put_Rotation)
    TranslateX = property(get_TranslateX, put_TranslateX)
    TranslateY = property(get_TranslateY, put_TranslateY)
    CenterXProperty = property(get_CenterXProperty, None)
    CenterYProperty = property(get_CenterYProperty, None)
    ScaleXProperty = property(get_ScaleXProperty, None)
    ScaleYProperty = property(get_ScaleYProperty, None)
    SkewXProperty = property(get_SkewXProperty, None)
    SkewYProperty = property(get_SkewYProperty, None)
    RotationProperty = property(get_RotationProperty, None)
    TranslateXProperty = property(get_TranslateXProperty, None)
    TranslateYProperty = property(get_TranslateYProperty, None)
class CompositionTarget(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Media.ICompositionTarget
    _classid_ = 'Windows.UI.Xaml.Media.CompositionTarget'
    @winrt_classmethod
    def add_Rendered(cls: Windows.UI.Xaml.Media.ICompositionTargetStatics3, handler: Windows.Foundation.EventHandler[Windows.UI.Xaml.Media.RenderedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_Rendered(cls: Windows.UI.Xaml.Media.ICompositionTargetStatics3, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_Rendering(cls: Windows.UI.Xaml.Media.ICompositionTargetStatics, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_Rendering(cls: Windows.UI.Xaml.Media.ICompositionTargetStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_SurfaceContentsLost(cls: Windows.UI.Xaml.Media.ICompositionTargetStatics, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_SurfaceContentsLost(cls: Windows.UI.Xaml.Media.ICompositionTargetStatics, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class DoubleCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IVector[Double]
    _classid_ = 'Windows.UI.Xaml.Media.DoubleCollection'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.DoubleCollection: ...
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVector[Double], index: UInt32) -> Double: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVector[Double]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IVector[Double]) -> Windows.Foundation.Collections.IVectorView[Double]: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVector[Double], value: Double, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: Windows.Foundation.Collections.IVector[Double], index: UInt32, value: Double) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: Windows.Foundation.Collections.IVector[Double], index: UInt32, value: Double) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: Windows.Foundation.Collections.IVector[Double], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: Windows.Foundation.Collections.IVector[Double], value: Double) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: Windows.Foundation.Collections.IVector[Double]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IVector[Double]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVector[Double], startIndex: UInt32, items: POINTER(Double)) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: Windows.Foundation.Collections.IVector[Double], items: POINTER(Double)) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Double]) -> Windows.Foundation.Collections.IIterator[Double]: ...
    Size = property(get_Size, None)
ElementCompositeMode = Int32
ElementCompositeMode_Inherit: ElementCompositeMode = 0
ElementCompositeMode_SourceOver: ElementCompositeMode = 1
ElementCompositeMode_MinBlend: ElementCompositeMode = 2
class EllipseGeometry(ComPtr):
    extends: Windows.UI.Xaml.Media.Geometry
    default_interface: Windows.UI.Xaml.Media.IEllipseGeometry
    _classid_ = 'Windows.UI.Xaml.Media.EllipseGeometry'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.EllipseGeometry: ...
    @winrt_mixinmethod
    def get_Center(self: Windows.UI.Xaml.Media.IEllipseGeometry) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Center(self: Windows.UI.Xaml.Media.IEllipseGeometry, value: Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_RadiusX(self: Windows.UI.Xaml.Media.IEllipseGeometry) -> Double: ...
    @winrt_mixinmethod
    def put_RadiusX(self: Windows.UI.Xaml.Media.IEllipseGeometry, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RadiusY(self: Windows.UI.Xaml.Media.IEllipseGeometry) -> Double: ...
    @winrt_mixinmethod
    def put_RadiusY(self: Windows.UI.Xaml.Media.IEllipseGeometry, value: Double) -> Void: ...
    @winrt_classmethod
    def get_CenterProperty(cls: Windows.UI.Xaml.Media.IEllipseGeometryStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RadiusXProperty(cls: Windows.UI.Xaml.Media.IEllipseGeometryStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RadiusYProperty(cls: Windows.UI.Xaml.Media.IEllipseGeometryStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Center = property(get_Center, put_Center)
    RadiusX = property(get_RadiusX, put_RadiusX)
    RadiusY = property(get_RadiusY, put_RadiusY)
    CenterProperty = property(get_CenterProperty, None)
    RadiusXProperty = property(get_RadiusXProperty, None)
    RadiusYProperty = property(get_RadiusYProperty, None)
FastPlayFallbackBehaviour = Int32
FastPlayFallbackBehaviour_Skip: FastPlayFallbackBehaviour = 0
FastPlayFallbackBehaviour_Hide: FastPlayFallbackBehaviour = 1
FastPlayFallbackBehaviour_Disable: FastPlayFallbackBehaviour = 2
FillRule = Int32
FillRule_EvenOdd: FillRule = 0
FillRule_Nonzero: FillRule = 1
class FontFamily(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Media.IFontFamily
    _classid_ = 'Windows.UI.Xaml.Media.FontFamily'
    @winrt_commethod(6)
    def get_Source(self) -> WinRT_String: ...
    @winrt_classmethod
    def get_XamlAutoFontFamily(cls: Windows.UI.Xaml.Media.IFontFamilyStatics2) -> Windows.UI.Xaml.Media.FontFamily: ...
    Source = property(get_Source, None)
    XamlAutoFontFamily = property(get_XamlAutoFontFamily, None)
class GeneralTransform(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Media.IGeneralTransform
    _classid_ = 'Windows.UI.Xaml.Media.GeneralTransform'
    @winrt_commethod(14)
    def get_Inverse(self) -> Windows.UI.Xaml.Media.GeneralTransform: ...
    @winrt_commethod(15)
    def TransformPoint(self, point: Windows.Foundation.Point) -> Windows.Foundation.Point: ...
    @winrt_commethod(16)
    def TryTransform(self, inPoint: Windows.Foundation.Point, outPoint: POINTER(Windows.Foundation.Point_head)) -> Boolean: ...
    @winrt_commethod(17)
    def TransformBounds(self, rect: Windows.Foundation.Rect) -> Windows.Foundation.Rect: ...
    @winrt_commethod(18)
    def get_InverseCore(self) -> Windows.UI.Xaml.Media.GeneralTransform: ...
    @winrt_commethod(19)
    def TryTransformCore(self, inPoint: Windows.Foundation.Point, outPoint: POINTER(Windows.Foundation.Point_head)) -> Boolean: ...
    @winrt_commethod(20)
    def TransformBoundsCore(self, rect: Windows.Foundation.Rect) -> Windows.Foundation.Rect: ...
    Inverse = property(get_Inverse, None)
    InverseCore = property(get_InverseCore, None)
class Geometry(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Media.IGeometry
    _classid_ = 'Windows.UI.Xaml.Media.Geometry'
    @winrt_commethod(12)
    def get_Transform(self) -> Windows.UI.Xaml.Media.Transform: ...
    @winrt_commethod(13)
    def put_Transform(self, value: Windows.UI.Xaml.Media.Transform) -> Void: ...
    @winrt_commethod(14)
    def get_Bounds(self) -> Windows.Foundation.Rect: ...
    @winrt_classmethod
    def get_Empty(cls: Windows.UI.Xaml.Media.IGeometryStatics) -> Windows.UI.Xaml.Media.Geometry: ...
    @winrt_classmethod
    def get_StandardFlatteningTolerance(cls: Windows.UI.Xaml.Media.IGeometryStatics) -> Double: ...
    @winrt_classmethod
    def get_TransformProperty(cls: Windows.UI.Xaml.Media.IGeometryStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Transform = property(get_Transform, put_Transform)
    Bounds = property(get_Bounds, None)
    Empty = property(get_Empty, None)
    StandardFlatteningTolerance = property(get_StandardFlatteningTolerance, None)
    TransformProperty = property(get_TransformProperty, None)
class GeometryCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Geometry]
    _classid_ = 'Windows.UI.Xaml.Media.GeometryCollection'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.GeometryCollection: ...
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Geometry], index: UInt32) -> Windows.UI.Xaml.Media.Geometry: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Geometry]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Geometry]) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Media.Geometry]: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Geometry], value: Windows.UI.Xaml.Media.Geometry, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Geometry], index: UInt32, value: Windows.UI.Xaml.Media.Geometry) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Geometry], index: UInt32, value: Windows.UI.Xaml.Media.Geometry) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Geometry], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Geometry], value: Windows.UI.Xaml.Media.Geometry) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Geometry]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Geometry]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Geometry], startIndex: UInt32, items: POINTER(Windows.UI.Xaml.Media.Geometry)) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Geometry], items: POINTER(Windows.UI.Xaml.Media.Geometry)) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.Media.Geometry]) -> Windows.Foundation.Collections.IIterator[Windows.UI.Xaml.Media.Geometry]: ...
    Size = property(get_Size, None)
class GeometryGroup(ComPtr):
    extends: Windows.UI.Xaml.Media.Geometry
    default_interface: Windows.UI.Xaml.Media.IGeometryGroup
    _classid_ = 'Windows.UI.Xaml.Media.GeometryGroup'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.GeometryGroup: ...
    @winrt_mixinmethod
    def get_FillRule(self: Windows.UI.Xaml.Media.IGeometryGroup) -> Windows.UI.Xaml.Media.FillRule: ...
    @winrt_mixinmethod
    def put_FillRule(self: Windows.UI.Xaml.Media.IGeometryGroup, value: Windows.UI.Xaml.Media.FillRule) -> Void: ...
    @winrt_mixinmethod
    def get_Children(self: Windows.UI.Xaml.Media.IGeometryGroup) -> Windows.UI.Xaml.Media.GeometryCollection: ...
    @winrt_mixinmethod
    def put_Children(self: Windows.UI.Xaml.Media.IGeometryGroup, value: Windows.UI.Xaml.Media.GeometryCollection) -> Void: ...
    @winrt_classmethod
    def get_FillRuleProperty(cls: Windows.UI.Xaml.Media.IGeometryGroupStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ChildrenProperty(cls: Windows.UI.Xaml.Media.IGeometryGroupStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    FillRule = property(get_FillRule, put_FillRule)
    Children = property(get_Children, put_Children)
    FillRuleProperty = property(get_FillRuleProperty, None)
    ChildrenProperty = property(get_ChildrenProperty, None)
class GradientBrush(ComPtr):
    extends: Windows.UI.Xaml.Media.Brush
    default_interface: Windows.UI.Xaml.Media.IGradientBrush
    _classid_ = 'Windows.UI.Xaml.Media.GradientBrush'
    @winrt_commethod(31)
    def get_SpreadMethod(self) -> Windows.UI.Xaml.Media.GradientSpreadMethod: ...
    @winrt_commethod(32)
    def put_SpreadMethod(self, value: Windows.UI.Xaml.Media.GradientSpreadMethod) -> Void: ...
    @winrt_commethod(33)
    def get_MappingMode(self) -> Windows.UI.Xaml.Media.BrushMappingMode: ...
    @winrt_commethod(34)
    def put_MappingMode(self, value: Windows.UI.Xaml.Media.BrushMappingMode) -> Void: ...
    @winrt_commethod(35)
    def get_ColorInterpolationMode(self) -> Windows.UI.Xaml.Media.ColorInterpolationMode: ...
    @winrt_commethod(36)
    def put_ColorInterpolationMode(self, value: Windows.UI.Xaml.Media.ColorInterpolationMode) -> Void: ...
    @winrt_commethod(37)
    def get_GradientStops(self) -> Windows.UI.Xaml.Media.GradientStopCollection: ...
    @winrt_commethod(38)
    def put_GradientStops(self, value: Windows.UI.Xaml.Media.GradientStopCollection) -> Void: ...
    @winrt_classmethod
    def get_SpreadMethodProperty(cls: Windows.UI.Xaml.Media.IGradientBrushStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MappingModeProperty(cls: Windows.UI.Xaml.Media.IGradientBrushStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ColorInterpolationModeProperty(cls: Windows.UI.Xaml.Media.IGradientBrushStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_GradientStopsProperty(cls: Windows.UI.Xaml.Media.IGradientBrushStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    SpreadMethod = property(get_SpreadMethod, put_SpreadMethod)
    MappingMode = property(get_MappingMode, put_MappingMode)
    ColorInterpolationMode = property(get_ColorInterpolationMode, put_ColorInterpolationMode)
    GradientStops = property(get_GradientStops, put_GradientStops)
    SpreadMethodProperty = property(get_SpreadMethodProperty, None)
    MappingModeProperty = property(get_MappingModeProperty, None)
    ColorInterpolationModeProperty = property(get_ColorInterpolationModeProperty, None)
    GradientStopsProperty = property(get_GradientStopsProperty, None)
GradientSpreadMethod = Int32
GradientSpreadMethod_Pad: GradientSpreadMethod = 0
GradientSpreadMethod_Reflect: GradientSpreadMethod = 1
GradientSpreadMethod_Repeat: GradientSpreadMethod = 2
class GradientStop(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Media.IGradientStop
    _classid_ = 'Windows.UI.Xaml.Media.GradientStop'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.GradientStop: ...
    @winrt_mixinmethod
    def get_Color(self: Windows.UI.Xaml.Media.IGradientStop) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: Windows.UI.Xaml.Media.IGradientStop, value: Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_Offset(self: Windows.UI.Xaml.Media.IGradientStop) -> Double: ...
    @winrt_mixinmethod
    def put_Offset(self: Windows.UI.Xaml.Media.IGradientStop, value: Double) -> Void: ...
    @winrt_classmethod
    def get_ColorProperty(cls: Windows.UI.Xaml.Media.IGradientStopStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_OffsetProperty(cls: Windows.UI.Xaml.Media.IGradientStopStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Color = property(get_Color, put_Color)
    Offset = property(get_Offset, put_Offset)
    ColorProperty = property(get_ColorProperty, None)
    OffsetProperty = property(get_OffsetProperty, None)
class GradientStopCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.GradientStop]
    _classid_ = 'Windows.UI.Xaml.Media.GradientStopCollection'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.GradientStopCollection: ...
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.GradientStop], index: UInt32) -> Windows.UI.Xaml.Media.GradientStop: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.GradientStop]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.GradientStop]) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Media.GradientStop]: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.GradientStop], value: Windows.UI.Xaml.Media.GradientStop, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.GradientStop], index: UInt32, value: Windows.UI.Xaml.Media.GradientStop) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.GradientStop], index: UInt32, value: Windows.UI.Xaml.Media.GradientStop) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.GradientStop], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.GradientStop], value: Windows.UI.Xaml.Media.GradientStop) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.GradientStop]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.GradientStop]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.GradientStop], startIndex: UInt32, items: POINTER(Windows.UI.Xaml.Media.GradientStop)) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.GradientStop], items: POINTER(Windows.UI.Xaml.Media.GradientStop)) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.Media.GradientStop]) -> Windows.Foundation.Collections.IIterator[Windows.UI.Xaml.Media.GradientStop]: ...
    Size = property(get_Size, None)
class IAcrylicBrush(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IAcrylicBrush'
    _iid_ = Guid('{79bbcf4e-cd66-4f1b-a8b6-cd6d2977c18d}')
    @winrt_commethod(6)
    def get_BackgroundSource(self) -> Windows.UI.Xaml.Media.AcrylicBackgroundSource: ...
    @winrt_commethod(7)
    def put_BackgroundSource(self, value: Windows.UI.Xaml.Media.AcrylicBackgroundSource) -> Void: ...
    @winrt_commethod(8)
    def get_TintColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(9)
    def put_TintColor(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(10)
    def get_TintOpacity(self) -> Double: ...
    @winrt_commethod(11)
    def put_TintOpacity(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def get_TintTransitionDuration(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(13)
    def put_TintTransitionDuration(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(14)
    def get_AlwaysUseFallback(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_AlwaysUseFallback(self, value: Boolean) -> Void: ...
    BackgroundSource = property(get_BackgroundSource, put_BackgroundSource)
    TintColor = property(get_TintColor, put_TintColor)
    TintOpacity = property(get_TintOpacity, put_TintOpacity)
    TintTransitionDuration = property(get_TintTransitionDuration, put_TintTransitionDuration)
    AlwaysUseFallback = property(get_AlwaysUseFallback, put_AlwaysUseFallback)
class IAcrylicBrush2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IAcrylicBrush2'
    _iid_ = Guid('{c9645383-b19e-5ac0-86ff-3d90506dbcda}')
    @winrt_commethod(6)
    def get_TintLuminosityOpacity(self) -> Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(7)
    def put_TintLuminosityOpacity(self, value: Windows.Foundation.IReference[Double]) -> Void: ...
    TintLuminosityOpacity = property(get_TintLuminosityOpacity, put_TintLuminosityOpacity)
class IAcrylicBrushFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IAcrylicBrushFactory'
    _iid_ = Guid('{81a32568-f6cc-4013-8363-928ae23b7a61}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.AcrylicBrush: ...
class IAcrylicBrushStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IAcrylicBrushStatics'
    _iid_ = Guid('{2787fd79-a3da-423f-b81a-599147971523}')
    @winrt_commethod(6)
    def get_BackgroundSourceProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_TintColorProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_TintOpacityProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_TintTransitionDurationProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_AlwaysUseFallbackProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    BackgroundSourceProperty = property(get_BackgroundSourceProperty, None)
    TintColorProperty = property(get_TintColorProperty, None)
    TintOpacityProperty = property(get_TintOpacityProperty, None)
    TintTransitionDurationProperty = property(get_TintTransitionDurationProperty, None)
    AlwaysUseFallbackProperty = property(get_AlwaysUseFallbackProperty, None)
class IAcrylicBrushStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IAcrylicBrushStatics2'
    _iid_ = Guid('{129188a8-bf11-5bbc-8445-8c510e5926c0}')
    @winrt_commethod(6)
    def get_TintLuminosityOpacityProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    TintLuminosityOpacityProperty = property(get_TintLuminosityOpacityProperty, None)
class IArcSegment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IArcSegment'
    _iid_ = Guid('{07940c5f-63fb-4469-91be-f1097c168052}')
    @winrt_commethod(6)
    def get_Point(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def put_Point(self, value: Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(8)
    def get_Size(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(9)
    def put_Size(self, value: Windows.Foundation.Size) -> Void: ...
    @winrt_commethod(10)
    def get_RotationAngle(self) -> Double: ...
    @winrt_commethod(11)
    def put_RotationAngle(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def get_IsLargeArc(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_IsLargeArc(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_SweepDirection(self) -> Windows.UI.Xaml.Media.SweepDirection: ...
    @winrt_commethod(15)
    def put_SweepDirection(self, value: Windows.UI.Xaml.Media.SweepDirection) -> Void: ...
    Point = property(get_Point, put_Point)
    Size = property(get_Size, put_Size)
    RotationAngle = property(get_RotationAngle, put_RotationAngle)
    IsLargeArc = property(get_IsLargeArc, put_IsLargeArc)
    SweepDirection = property(get_SweepDirection, put_SweepDirection)
class IArcSegmentStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IArcSegmentStatics'
    _iid_ = Guid('{82348f6e-8a69-4204-9c12-7207df317643}')
    @winrt_commethod(6)
    def get_PointProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_SizeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_RotationAngleProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_IsLargeArcProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_SweepDirectionProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    PointProperty = property(get_PointProperty, None)
    SizeProperty = property(get_SizeProperty, None)
    RotationAngleProperty = property(get_RotationAngleProperty, None)
    IsLargeArcProperty = property(get_IsLargeArcProperty, None)
    SweepDirectionProperty = property(get_SweepDirectionProperty, None)
class IBezierSegment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IBezierSegment'
    _iid_ = Guid('{af4bb9ee-8984-49b7-81df-3f35994b95eb}')
    @winrt_commethod(6)
    def get_Point1(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def put_Point1(self, value: Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(8)
    def get_Point2(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(9)
    def put_Point2(self, value: Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(10)
    def get_Point3(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(11)
    def put_Point3(self, value: Windows.Foundation.Point) -> Void: ...
    Point1 = property(get_Point1, put_Point1)
    Point2 = property(get_Point2, put_Point2)
    Point3 = property(get_Point3, put_Point3)
class IBezierSegmentStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IBezierSegmentStatics'
    _iid_ = Guid('{c0287bac-1410-4530-8452-1c9d0ad1f341}')
    @winrt_commethod(6)
    def get_Point1Property(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_Point2Property(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_Point3Property(self) -> Windows.UI.Xaml.DependencyProperty: ...
    Point1Property = property(get_Point1Property, None)
    Point2Property = property(get_Point2Property, None)
    Point3Property = property(get_Point3Property, None)
class IBitmapCache(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IBitmapCache'
    _iid_ = Guid('{79c2219e-44d2-4610-9735-9bec83809ecf}')
class IBrush(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IBrush'
    _iid_ = Guid('{8806a321-1e06-422c-a1cc-01696559e021}')
    @winrt_commethod(6)
    def get_Opacity(self) -> Double: ...
    @winrt_commethod(7)
    def put_Opacity(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_Transform(self) -> Windows.UI.Xaml.Media.Transform: ...
    @winrt_commethod(9)
    def put_Transform(self, value: Windows.UI.Xaml.Media.Transform) -> Void: ...
    @winrt_commethod(10)
    def get_RelativeTransform(self) -> Windows.UI.Xaml.Media.Transform: ...
    @winrt_commethod(11)
    def put_RelativeTransform(self, value: Windows.UI.Xaml.Media.Transform) -> Void: ...
    Opacity = property(get_Opacity, put_Opacity)
    Transform = property(get_Transform, put_Transform)
    RelativeTransform = property(get_RelativeTransform, put_RelativeTransform)
class IBrushFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IBrushFactory'
    _iid_ = Guid('{399658a2-14fb-4b8f-83e6-6e3dab12069b}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.Brush: ...
class IBrushOverrides2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IBrushOverrides2'
    _iid_ = Guid('{d092b151-d83b-5a81-a71e-a1c7f8ad6963}')
    @winrt_commethod(6)
    def PopulatePropertyInfoOverride(self, propertyName: WinRT_String, animationPropertyInfo: Windows.UI.Composition.AnimationPropertyInfo) -> Void: ...
class IBrushStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IBrushStatics'
    _iid_ = Guid('{e70c3102-0225-47f5-b22e-0467619f6a22}')
    @winrt_commethod(6)
    def get_OpacityProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_TransformProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_RelativeTransformProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    OpacityProperty = property(get_OpacityProperty, None)
    TransformProperty = property(get_TransformProperty, None)
    RelativeTransformProperty = property(get_RelativeTransformProperty, None)
class ICacheMode(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ICacheMode'
    _iid_ = Guid('{98dc8b11-c6f9-4dab-b838-5fd5ec8c7350}')
class ICacheModeFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ICacheModeFactory'
    _iid_ = Guid('{eb1f8c5b-0abb-4e70-b8a8-620d0d953ab2}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.CacheMode: ...
class ICompositeTransform(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ICompositeTransform'
    _iid_ = Guid('{c8a4385b-f24a-4701-a265-a78846f142b9}')
    @winrt_commethod(6)
    def get_CenterX(self) -> Double: ...
    @winrt_commethod(7)
    def put_CenterX(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_CenterY(self) -> Double: ...
    @winrt_commethod(9)
    def put_CenterY(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_ScaleX(self) -> Double: ...
    @winrt_commethod(11)
    def put_ScaleX(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def get_ScaleY(self) -> Double: ...
    @winrt_commethod(13)
    def put_ScaleY(self, value: Double) -> Void: ...
    @winrt_commethod(14)
    def get_SkewX(self) -> Double: ...
    @winrt_commethod(15)
    def put_SkewX(self, value: Double) -> Void: ...
    @winrt_commethod(16)
    def get_SkewY(self) -> Double: ...
    @winrt_commethod(17)
    def put_SkewY(self, value: Double) -> Void: ...
    @winrt_commethod(18)
    def get_Rotation(self) -> Double: ...
    @winrt_commethod(19)
    def put_Rotation(self, value: Double) -> Void: ...
    @winrt_commethod(20)
    def get_TranslateX(self) -> Double: ...
    @winrt_commethod(21)
    def put_TranslateX(self, value: Double) -> Void: ...
    @winrt_commethod(22)
    def get_TranslateY(self) -> Double: ...
    @winrt_commethod(23)
    def put_TranslateY(self, value: Double) -> Void: ...
    CenterX = property(get_CenterX, put_CenterX)
    CenterY = property(get_CenterY, put_CenterY)
    ScaleX = property(get_ScaleX, put_ScaleX)
    ScaleY = property(get_ScaleY, put_ScaleY)
    SkewX = property(get_SkewX, put_SkewX)
    SkewY = property(get_SkewY, put_SkewY)
    Rotation = property(get_Rotation, put_Rotation)
    TranslateX = property(get_TranslateX, put_TranslateX)
    TranslateY = property(get_TranslateY, put_TranslateY)
class ICompositeTransformStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ICompositeTransformStatics'
    _iid_ = Guid('{2f190c08-8266-496f-9653-a18bd4f836aa}')
    @winrt_commethod(6)
    def get_CenterXProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_CenterYProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ScaleXProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_ScaleYProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_SkewXProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_SkewYProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_RotationProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_TranslateXProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_TranslateYProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    CenterXProperty = property(get_CenterXProperty, None)
    CenterYProperty = property(get_CenterYProperty, None)
    ScaleXProperty = property(get_ScaleXProperty, None)
    ScaleYProperty = property(get_ScaleYProperty, None)
    SkewXProperty = property(get_SkewXProperty, None)
    SkewYProperty = property(get_SkewYProperty, None)
    RotationProperty = property(get_RotationProperty, None)
    TranslateXProperty = property(get_TranslateXProperty, None)
    TranslateYProperty = property(get_TranslateYProperty, None)
class ICompositionTarget(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ICompositionTarget'
    _iid_ = Guid('{26cfbff0-713c-4bec-8803-e101f7b14ed3}')
class ICompositionTargetStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ICompositionTargetStatics'
    _iid_ = Guid('{2b1af03d-1ed2-4b59-bd00-7594ee92832b}')
    @winrt_commethod(6)
    def add_Rendering(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Rendering(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_SurfaceContentsLost(self, handler: Windows.Foundation.EventHandler[Windows.Win32.System.WinRT.IInspectable_head]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_SurfaceContentsLost(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class ICompositionTargetStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ICompositionTargetStatics3'
    _iid_ = Guid('{bc0a7cd9-6750-4708-994c-2028e0312ac8}')
    @winrt_commethod(6)
    def add_Rendered(self, handler: Windows.Foundation.EventHandler[Windows.UI.Xaml.Media.RenderedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Rendered(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
class IEllipseGeometry(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IEllipseGeometry'
    _iid_ = Guid('{d4f61bba-4ea2-40d6-aa6c-8d38aa87651f}')
    @winrt_commethod(6)
    def get_Center(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def put_Center(self, value: Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(8)
    def get_RadiusX(self) -> Double: ...
    @winrt_commethod(9)
    def put_RadiusX(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_RadiusY(self) -> Double: ...
    @winrt_commethod(11)
    def put_RadiusY(self, value: Double) -> Void: ...
    Center = property(get_Center, put_Center)
    RadiusX = property(get_RadiusX, put_RadiusX)
    RadiusY = property(get_RadiusY, put_RadiusY)
class IEllipseGeometryStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IEllipseGeometryStatics'
    _iid_ = Guid('{1744db47-f635-4b16-aee6-e052a65defb2}')
    @winrt_commethod(6)
    def get_CenterProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_RadiusXProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_RadiusYProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    CenterProperty = property(get_CenterProperty, None)
    RadiusXProperty = property(get_RadiusXProperty, None)
    RadiusYProperty = property(get_RadiusYProperty, None)
class IFontFamily(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IFontFamily'
    _iid_ = Guid('{92467e64-d66a-4cf4-9322-3d23b3c0c361}')
    @winrt_commethod(6)
    def get_Source(self) -> WinRT_String: ...
    Source = property(get_Source, None)
class IFontFamilyFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IFontFamilyFactory'
    _iid_ = Guid('{d5603377-3dae-4dcd-af09-f9498e9ec659}')
    @winrt_commethod(6)
    def CreateInstanceWithName(self, familyName: WinRT_String, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.FontFamily: ...
class IFontFamilyStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IFontFamilyStatics2'
    _iid_ = Guid('{52ad7af9-37e6-4297-a238-97fb6a408d9e}')
    @winrt_commethod(6)
    def get_XamlAutoFontFamily(self) -> Windows.UI.Xaml.Media.FontFamily: ...
    XamlAutoFontFamily = property(get_XamlAutoFontFamily, None)
class IGeneralTransform(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IGeneralTransform'
    _iid_ = Guid('{a06798b7-a2ec-415f-ade2-eade9333f2c7}')
    @winrt_commethod(6)
    def get_Inverse(self) -> Windows.UI.Xaml.Media.GeneralTransform: ...
    @winrt_commethod(7)
    def TransformPoint(self, point: Windows.Foundation.Point) -> Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def TryTransform(self, inPoint: Windows.Foundation.Point, outPoint: POINTER(Windows.Foundation.Point_head)) -> Boolean: ...
    @winrt_commethod(9)
    def TransformBounds(self, rect: Windows.Foundation.Rect) -> Windows.Foundation.Rect: ...
    Inverse = property(get_Inverse, None)
class IGeneralTransformFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IGeneralTransformFactory'
    _iid_ = Guid('{7a25c930-29c4-4e31-b6f9-dedd52e4df1b}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.GeneralTransform: ...
class IGeneralTransformOverrides(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IGeneralTransformOverrides'
    _iid_ = Guid('{4f121083-24cf-4524-90ad-8a42b1c12783}')
    @winrt_commethod(6)
    def get_InverseCore(self) -> Windows.UI.Xaml.Media.GeneralTransform: ...
    @winrt_commethod(7)
    def TryTransformCore(self, inPoint: Windows.Foundation.Point, outPoint: POINTER(Windows.Foundation.Point_head)) -> Boolean: ...
    @winrt_commethod(8)
    def TransformBoundsCore(self, rect: Windows.Foundation.Rect) -> Windows.Foundation.Rect: ...
    InverseCore = property(get_InverseCore, None)
class IGeometry(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IGeometry'
    _iid_ = Guid('{fa123889-0acd-417b-b62d-5ca1bf4dfc0e}')
    @winrt_commethod(6)
    def get_Transform(self) -> Windows.UI.Xaml.Media.Transform: ...
    @winrt_commethod(7)
    def put_Transform(self, value: Windows.UI.Xaml.Media.Transform) -> Void: ...
    @winrt_commethod(8)
    def get_Bounds(self) -> Windows.Foundation.Rect: ...
    Transform = property(get_Transform, put_Transform)
    Bounds = property(get_Bounds, None)
class IGeometryFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IGeometryFactory'
    _iid_ = Guid('{f65daf23-d5fd-42f9-b32a-929c5a4b54e1}')
class IGeometryGroup(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IGeometryGroup'
    _iid_ = Guid('{55225a61-8677-4c8c-8e46-ee3dc355114b}')
    @winrt_commethod(6)
    def get_FillRule(self) -> Windows.UI.Xaml.Media.FillRule: ...
    @winrt_commethod(7)
    def put_FillRule(self, value: Windows.UI.Xaml.Media.FillRule) -> Void: ...
    @winrt_commethod(8)
    def get_Children(self) -> Windows.UI.Xaml.Media.GeometryCollection: ...
    @winrt_commethod(9)
    def put_Children(self, value: Windows.UI.Xaml.Media.GeometryCollection) -> Void: ...
    FillRule = property(get_FillRule, put_FillRule)
    Children = property(get_Children, put_Children)
class IGeometryGroupStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IGeometryGroupStatics'
    _iid_ = Guid('{56c955f4-8496-4bb6-abf0-617b1fe78b45}')
    @winrt_commethod(6)
    def get_FillRuleProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ChildrenProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    FillRuleProperty = property(get_FillRuleProperty, None)
    ChildrenProperty = property(get_ChildrenProperty, None)
class IGeometryStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IGeometryStatics'
    _iid_ = Guid('{7a70aa8c-0b06-465f-b637-9a47e5a70111}')
    @winrt_commethod(6)
    def get_Empty(self) -> Windows.UI.Xaml.Media.Geometry: ...
    @winrt_commethod(7)
    def get_StandardFlatteningTolerance(self) -> Double: ...
    @winrt_commethod(8)
    def get_TransformProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    Empty = property(get_Empty, None)
    StandardFlatteningTolerance = property(get_StandardFlatteningTolerance, None)
    TransformProperty = property(get_TransformProperty, None)
class IGradientBrush(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IGradientBrush'
    _iid_ = Guid('{2166e69f-935a-4191-8e3c-1c8dfdfcdc78}')
    @winrt_commethod(6)
    def get_SpreadMethod(self) -> Windows.UI.Xaml.Media.GradientSpreadMethod: ...
    @winrt_commethod(7)
    def put_SpreadMethod(self, value: Windows.UI.Xaml.Media.GradientSpreadMethod) -> Void: ...
    @winrt_commethod(8)
    def get_MappingMode(self) -> Windows.UI.Xaml.Media.BrushMappingMode: ...
    @winrt_commethod(9)
    def put_MappingMode(self, value: Windows.UI.Xaml.Media.BrushMappingMode) -> Void: ...
    @winrt_commethod(10)
    def get_ColorInterpolationMode(self) -> Windows.UI.Xaml.Media.ColorInterpolationMode: ...
    @winrt_commethod(11)
    def put_ColorInterpolationMode(self, value: Windows.UI.Xaml.Media.ColorInterpolationMode) -> Void: ...
    @winrt_commethod(12)
    def get_GradientStops(self) -> Windows.UI.Xaml.Media.GradientStopCollection: ...
    @winrt_commethod(13)
    def put_GradientStops(self, value: Windows.UI.Xaml.Media.GradientStopCollection) -> Void: ...
    SpreadMethod = property(get_SpreadMethod, put_SpreadMethod)
    MappingMode = property(get_MappingMode, put_MappingMode)
    ColorInterpolationMode = property(get_ColorInterpolationMode, put_ColorInterpolationMode)
    GradientStops = property(get_GradientStops, put_GradientStops)
class IGradientBrushFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IGradientBrushFactory'
    _iid_ = Guid('{ed4779ca-45bd-4131-b625-be86e07c6112}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.GradientBrush: ...
class IGradientBrushStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IGradientBrushStatics'
    _iid_ = Guid('{961661f9-8bb4-4e6c-b923-b5d787e0f1a9}')
    @winrt_commethod(6)
    def get_SpreadMethodProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_MappingModeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ColorInterpolationModeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_GradientStopsProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    SpreadMethodProperty = property(get_SpreadMethodProperty, None)
    MappingModeProperty = property(get_MappingModeProperty, None)
    ColorInterpolationModeProperty = property(get_ColorInterpolationModeProperty, None)
    GradientStopsProperty = property(get_GradientStopsProperty, None)
class IGradientStop(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IGradientStop'
    _iid_ = Guid('{665f44fe-2e59-4c4a-ab53-076a100ccd81}')
    @winrt_commethod(6)
    def get_Color(self) -> Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_Color(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(8)
    def get_Offset(self) -> Double: ...
    @winrt_commethod(9)
    def put_Offset(self, value: Double) -> Void: ...
    Color = property(get_Color, put_Color)
    Offset = property(get_Offset, put_Offset)
class IGradientStopStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IGradientStopStatics'
    _iid_ = Guid('{602a6d75-6193-4fe5-8e82-c7c6f6febafd}')
    @winrt_commethod(6)
    def get_ColorProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_OffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    ColorProperty = property(get_ColorProperty, None)
    OffsetProperty = property(get_OffsetProperty, None)
class IImageBrush(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IImageBrush'
    _iid_ = Guid('{9fd11377-c12a-4493-bf7d-f3a8ad74b554}')
    @winrt_commethod(6)
    def get_ImageSource(self) -> Windows.UI.Xaml.Media.ImageSource: ...
    @winrt_commethod(7)
    def put_ImageSource(self, value: Windows.UI.Xaml.Media.ImageSource) -> Void: ...
    @winrt_commethod(8)
    def add_ImageFailed(self, handler: Windows.UI.Xaml.ExceptionRoutedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ImageFailed(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_ImageOpened(self, handler: Windows.UI.Xaml.RoutedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ImageOpened(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    ImageSource = property(get_ImageSource, put_ImageSource)
class IImageBrushStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IImageBrushStatics'
    _iid_ = Guid('{1255b1b2-dd18-42e5-892c-eae30c305b8c}')
    @winrt_commethod(6)
    def get_ImageSourceProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    ImageSourceProperty = property(get_ImageSourceProperty, None)
class IImageSource(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IImageSource'
    _iid_ = Guid('{737ef309-ea41-4d96-a71c-98e98efcab07}')
class IImageSourceFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IImageSourceFactory'
    _iid_ = Guid('{297ec001-2540-4e5a-ab66-88035dd3ddb5}')
class ILineGeometry(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ILineGeometry'
    _iid_ = Guid('{30edd4a2-8fc5-40af-a7a2-c27fe7aa1363}')
    @winrt_commethod(6)
    def get_StartPoint(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def put_StartPoint(self, value: Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(8)
    def get_EndPoint(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(9)
    def put_EndPoint(self, value: Windows.Foundation.Point) -> Void: ...
    StartPoint = property(get_StartPoint, put_StartPoint)
    EndPoint = property(get_EndPoint, put_EndPoint)
class ILineGeometryStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ILineGeometryStatics'
    _iid_ = Guid('{578ae763-5562-4ee4-8703-ea4036d891e3}')
    @winrt_commethod(6)
    def get_StartPointProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_EndPointProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    StartPointProperty = property(get_StartPointProperty, None)
    EndPointProperty = property(get_EndPointProperty, None)
class ILineSegment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ILineSegment'
    _iid_ = Guid('{ef6a2e25-3ff0-4420-a411-7182a4cecb15}')
    @winrt_commethod(6)
    def get_Point(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def put_Point(self, value: Windows.Foundation.Point) -> Void: ...
    Point = property(get_Point, put_Point)
class ILineSegmentStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ILineSegmentStatics'
    _iid_ = Guid('{9fcab141-04c0-4afb-87b3-e800b969b894}')
    @winrt_commethod(6)
    def get_PointProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    PointProperty = property(get_PointProperty, None)
class ILinearGradientBrush(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ILinearGradientBrush'
    _iid_ = Guid('{8e96d16b-bb84-4c6f-9dbf-9d6c5c6d9c39}')
    @winrt_commethod(6)
    def get_StartPoint(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def put_StartPoint(self, value: Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(8)
    def get_EndPoint(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(9)
    def put_EndPoint(self, value: Windows.Foundation.Point) -> Void: ...
    StartPoint = property(get_StartPoint, put_StartPoint)
    EndPoint = property(get_EndPoint, put_EndPoint)
class ILinearGradientBrushFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ILinearGradientBrushFactory'
    _iid_ = Guid('{0ae0861c-1e7a-4fed-9857-ea8caa798490}')
    @winrt_commethod(6)
    def CreateInstanceWithGradientStopCollectionAndAngle(self, gradientStopCollection: Windows.UI.Xaml.Media.GradientStopCollection, angle: Double) -> Windows.UI.Xaml.Media.LinearGradientBrush: ...
class ILinearGradientBrushStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ILinearGradientBrushStatics'
    _iid_ = Guid('{7af6e504-2dc3-40e3-be0b-b314c13cb991}')
    @winrt_commethod(6)
    def get_StartPointProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_EndPointProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    StartPointProperty = property(get_StartPointProperty, None)
    EndPointProperty = property(get_EndPointProperty, None)
class ILoadedImageSourceLoadCompletedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ILoadedImageSourceLoadCompletedEventArgs'
    _iid_ = Guid('{1ac60b1e-7837-4489-b3e5-d0d5ad0a56c4}')
    @winrt_commethod(6)
    def get_Status(self) -> Windows.UI.Xaml.Media.LoadedImageSourceLoadStatus: ...
    Status = property(get_Status, None)
class ILoadedImageSurface(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ILoadedImageSurface'
    _iid_ = Guid('{050c8313-6737-45ba-8531-33094febef55}')
    @winrt_commethod(6)
    def get_DecodedPhysicalSize(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(7)
    def get_DecodedSize(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(8)
    def get_NaturalSize(self) -> Windows.Foundation.Size: ...
    @winrt_commethod(9)
    def add_LoadCompleted(self, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Media.LoadedImageSurface, Windows.UI.Xaml.Media.LoadedImageSourceLoadCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_LoadCompleted(self, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    DecodedPhysicalSize = property(get_DecodedPhysicalSize, None)
    DecodedSize = property(get_DecodedSize, None)
    NaturalSize = property(get_NaturalSize, None)
class ILoadedImageSurfaceStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ILoadedImageSurfaceStatics'
    _iid_ = Guid('{22b8edf6-84ad-40ab-937d-4871613e765d}')
    @winrt_commethod(6)
    def StartLoadFromUriWithSize(self, uri: Windows.Foundation.Uri, desiredMaxSize: Windows.Foundation.Size) -> Windows.UI.Xaml.Media.LoadedImageSurface: ...
    @winrt_commethod(7)
    def StartLoadFromUri(self, uri: Windows.Foundation.Uri) -> Windows.UI.Xaml.Media.LoadedImageSurface: ...
    @winrt_commethod(8)
    def StartLoadFromStreamWithSize(self, stream: Windows.Storage.Streams.IRandomAccessStream, desiredMaxSize: Windows.Foundation.Size) -> Windows.UI.Xaml.Media.LoadedImageSurface: ...
    @winrt_commethod(9)
    def StartLoadFromStream(self, stream: Windows.Storage.Streams.IRandomAccessStream) -> Windows.UI.Xaml.Media.LoadedImageSurface: ...
class IMatrix3DProjection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IMatrix3DProjection'
    _iid_ = Guid('{6f03e149-bfc9-4c01-b578-50338cec97fc}')
    @winrt_commethod(6)
    def get_ProjectionMatrix(self) -> Windows.UI.Xaml.Media.Media3D.Matrix3D: ...
    @winrt_commethod(7)
    def put_ProjectionMatrix(self, value: Windows.UI.Xaml.Media.Media3D.Matrix3D) -> Void: ...
    ProjectionMatrix = property(get_ProjectionMatrix, put_ProjectionMatrix)
class IMatrix3DProjectionStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IMatrix3DProjectionStatics'
    _iid_ = Guid('{ae9d5895-41ec-4e37-abaa-69f41d2f876b}')
    @winrt_commethod(6)
    def get_ProjectionMatrixProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    ProjectionMatrixProperty = property(get_ProjectionMatrixProperty, None)
class IMatrixHelper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IMatrixHelper'
    _iid_ = Guid('{f3cf4882-06b5-48c8-9eb2-1763e9364038}')
class IMatrixHelperStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IMatrixHelperStatics'
    _iid_ = Guid('{c18606a6-39f4-4b8a-8403-28e5e5f033b4}')
    @winrt_commethod(6)
    def get_Identity(self) -> Windows.UI.Xaml.Media.Matrix: ...
    @winrt_commethod(7)
    def FromElements(self, m11: Double, m12: Double, m21: Double, m22: Double, offsetX: Double, offsetY: Double) -> Windows.UI.Xaml.Media.Matrix: ...
    @winrt_commethod(8)
    def GetIsIdentity(self, target: Windows.UI.Xaml.Media.Matrix) -> Boolean: ...
    @winrt_commethod(9)
    def Transform(self, target: Windows.UI.Xaml.Media.Matrix, point: Windows.Foundation.Point) -> Windows.Foundation.Point: ...
    Identity = property(get_Identity, None)
class IMatrixTransform(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IMatrixTransform'
    _iid_ = Guid('{edfdd551-5fed-45fc-ae62-92a4b6cf9707}')
    @winrt_commethod(6)
    def get_Matrix(self) -> Windows.UI.Xaml.Media.Matrix: ...
    @winrt_commethod(7)
    def put_Matrix(self, value: Windows.UI.Xaml.Media.Matrix) -> Void: ...
    Matrix = property(get_Matrix, put_Matrix)
class IMatrixTransformStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IMatrixTransformStatics'
    _iid_ = Guid('{43e02e47-15b8-4758-bb97-7d52420acc5b}')
    @winrt_commethod(6)
    def get_MatrixProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    MatrixProperty = property(get_MatrixProperty, None)
class IMediaTransportControlsThumbnailRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IMediaTransportControlsThumbnailRequestedEventArgs'
    _iid_ = Guid('{e4a8b21c-e3c2-485c-ae69-f1537b76755a}')
    @winrt_commethod(6)
    def SetThumbnailImage(self, source: Windows.Storage.Streams.IInputStream) -> Void: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> Windows.Foundation.Deferral: ...
class IPartialMediaFailureDetectedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IPartialMediaFailureDetectedEventArgs'
    _iid_ = Guid('{02b65a91-e5a1-442b-88d3-2dc127bfc59b}')
    @winrt_commethod(6)
    def get_StreamKind(self) -> Windows.Media.Playback.FailedMediaStreamKind: ...
    StreamKind = property(get_StreamKind, None)
class IPartialMediaFailureDetectedEventArgs2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IPartialMediaFailureDetectedEventArgs2'
    _iid_ = Guid('{73074875-890d-416b-b9ae-e84dfd9c4b1b}')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
class IPathFigure(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IPathFigure'
    _iid_ = Guid('{5d955c8c-5fa9-4dda-a3cc-10fcdcaa20d7}')
    @winrt_commethod(6)
    def get_Segments(self) -> Windows.UI.Xaml.Media.PathSegmentCollection: ...
    @winrt_commethod(7)
    def put_Segments(self, value: Windows.UI.Xaml.Media.PathSegmentCollection) -> Void: ...
    @winrt_commethod(8)
    def get_StartPoint(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(9)
    def put_StartPoint(self, value: Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(10)
    def get_IsClosed(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsClosed(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_IsFilled(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_IsFilled(self, value: Boolean) -> Void: ...
    Segments = property(get_Segments, put_Segments)
    StartPoint = property(get_StartPoint, put_StartPoint)
    IsClosed = property(get_IsClosed, put_IsClosed)
    IsFilled = property(get_IsFilled, put_IsFilled)
class IPathFigureStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IPathFigureStatics'
    _iid_ = Guid('{b60591d9-2395-4317-9552-3a58526f8c7b}')
    @winrt_commethod(6)
    def get_SegmentsProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_StartPointProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_IsClosedProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_IsFilledProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    SegmentsProperty = property(get_SegmentsProperty, None)
    StartPointProperty = property(get_StartPointProperty, None)
    IsClosedProperty = property(get_IsClosedProperty, None)
    IsFilledProperty = property(get_IsFilledProperty, None)
class IPathGeometry(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IPathGeometry'
    _iid_ = Guid('{081b9df8-bae6-4bcb-813c-bde0e46dc8b7}')
    @winrt_commethod(6)
    def get_FillRule(self) -> Windows.UI.Xaml.Media.FillRule: ...
    @winrt_commethod(7)
    def put_FillRule(self, value: Windows.UI.Xaml.Media.FillRule) -> Void: ...
    @winrt_commethod(8)
    def get_Figures(self) -> Windows.UI.Xaml.Media.PathFigureCollection: ...
    @winrt_commethod(9)
    def put_Figures(self, value: Windows.UI.Xaml.Media.PathFigureCollection) -> Void: ...
    FillRule = property(get_FillRule, put_FillRule)
    Figures = property(get_Figures, put_Figures)
class IPathGeometryStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IPathGeometryStatics'
    _iid_ = Guid('{d9e58bba-2cba-4741-8f8d-3198cf5186b9}')
    @winrt_commethod(6)
    def get_FillRuleProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_FiguresProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    FillRuleProperty = property(get_FillRuleProperty, None)
    FiguresProperty = property(get_FiguresProperty, None)
class IPathSegment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IPathSegment'
    _iid_ = Guid('{fcfa71cf-9ce3-474f-8157-10b6435a616b}')
class IPathSegmentFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IPathSegmentFactory'
    _iid_ = Guid('{2a1c0aae-eccd-4464-a148-6ffdb3aa281f}')
class IPlaneProjection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IPlaneProjection'
    _iid_ = Guid('{e6f82bfa-6726-469a-b259-a5188347ca8f}')
    @winrt_commethod(6)
    def get_LocalOffsetX(self) -> Double: ...
    @winrt_commethod(7)
    def put_LocalOffsetX(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_LocalOffsetY(self) -> Double: ...
    @winrt_commethod(9)
    def put_LocalOffsetY(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_LocalOffsetZ(self) -> Double: ...
    @winrt_commethod(11)
    def put_LocalOffsetZ(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def get_RotationX(self) -> Double: ...
    @winrt_commethod(13)
    def put_RotationX(self, value: Double) -> Void: ...
    @winrt_commethod(14)
    def get_RotationY(self) -> Double: ...
    @winrt_commethod(15)
    def put_RotationY(self, value: Double) -> Void: ...
    @winrt_commethod(16)
    def get_RotationZ(self) -> Double: ...
    @winrt_commethod(17)
    def put_RotationZ(self, value: Double) -> Void: ...
    @winrt_commethod(18)
    def get_CenterOfRotationX(self) -> Double: ...
    @winrt_commethod(19)
    def put_CenterOfRotationX(self, value: Double) -> Void: ...
    @winrt_commethod(20)
    def get_CenterOfRotationY(self) -> Double: ...
    @winrt_commethod(21)
    def put_CenterOfRotationY(self, value: Double) -> Void: ...
    @winrt_commethod(22)
    def get_CenterOfRotationZ(self) -> Double: ...
    @winrt_commethod(23)
    def put_CenterOfRotationZ(self, value: Double) -> Void: ...
    @winrt_commethod(24)
    def get_GlobalOffsetX(self) -> Double: ...
    @winrt_commethod(25)
    def put_GlobalOffsetX(self, value: Double) -> Void: ...
    @winrt_commethod(26)
    def get_GlobalOffsetY(self) -> Double: ...
    @winrt_commethod(27)
    def put_GlobalOffsetY(self, value: Double) -> Void: ...
    @winrt_commethod(28)
    def get_GlobalOffsetZ(self) -> Double: ...
    @winrt_commethod(29)
    def put_GlobalOffsetZ(self, value: Double) -> Void: ...
    @winrt_commethod(30)
    def get_ProjectionMatrix(self) -> Windows.UI.Xaml.Media.Media3D.Matrix3D: ...
    LocalOffsetX = property(get_LocalOffsetX, put_LocalOffsetX)
    LocalOffsetY = property(get_LocalOffsetY, put_LocalOffsetY)
    LocalOffsetZ = property(get_LocalOffsetZ, put_LocalOffsetZ)
    RotationX = property(get_RotationX, put_RotationX)
    RotationY = property(get_RotationY, put_RotationY)
    RotationZ = property(get_RotationZ, put_RotationZ)
    CenterOfRotationX = property(get_CenterOfRotationX, put_CenterOfRotationX)
    CenterOfRotationY = property(get_CenterOfRotationY, put_CenterOfRotationY)
    CenterOfRotationZ = property(get_CenterOfRotationZ, put_CenterOfRotationZ)
    GlobalOffsetX = property(get_GlobalOffsetX, put_GlobalOffsetX)
    GlobalOffsetY = property(get_GlobalOffsetY, put_GlobalOffsetY)
    GlobalOffsetZ = property(get_GlobalOffsetZ, put_GlobalOffsetZ)
    ProjectionMatrix = property(get_ProjectionMatrix, None)
class IPlaneProjectionStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IPlaneProjectionStatics'
    _iid_ = Guid('{ad919c67-3bdc-4855-8969-d1f9a3adc27d}')
    @winrt_commethod(6)
    def get_LocalOffsetXProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_LocalOffsetYProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_LocalOffsetZProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_RotationXProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_RotationYProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_RotationZProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_CenterOfRotationXProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_CenterOfRotationYProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_CenterOfRotationZProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_GlobalOffsetXProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def get_GlobalOffsetYProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(17)
    def get_GlobalOffsetZProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(18)
    def get_ProjectionMatrixProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    LocalOffsetXProperty = property(get_LocalOffsetXProperty, None)
    LocalOffsetYProperty = property(get_LocalOffsetYProperty, None)
    LocalOffsetZProperty = property(get_LocalOffsetZProperty, None)
    RotationXProperty = property(get_RotationXProperty, None)
    RotationYProperty = property(get_RotationYProperty, None)
    RotationZProperty = property(get_RotationZProperty, None)
    CenterOfRotationXProperty = property(get_CenterOfRotationXProperty, None)
    CenterOfRotationYProperty = property(get_CenterOfRotationYProperty, None)
    CenterOfRotationZProperty = property(get_CenterOfRotationZProperty, None)
    GlobalOffsetXProperty = property(get_GlobalOffsetXProperty, None)
    GlobalOffsetYProperty = property(get_GlobalOffsetYProperty, None)
    GlobalOffsetZProperty = property(get_GlobalOffsetZProperty, None)
    ProjectionMatrixProperty = property(get_ProjectionMatrixProperty, None)
class IPolyBezierSegment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IPolyBezierSegment'
    _iid_ = Guid('{36805271-38c4-4bcf-96cd-028a6d38af25}')
    @winrt_commethod(6)
    def get_Points(self) -> Windows.UI.Xaml.Media.PointCollection: ...
    @winrt_commethod(7)
    def put_Points(self, value: Windows.UI.Xaml.Media.PointCollection) -> Void: ...
    Points = property(get_Points, put_Points)
class IPolyBezierSegmentStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IPolyBezierSegmentStatics'
    _iid_ = Guid('{1d91a6da-1492-4acc-bd66-a496f3d829d6}')
    @winrt_commethod(6)
    def get_PointsProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    PointsProperty = property(get_PointsProperty, None)
class IPolyLineSegment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IPolyLineSegment'
    _iid_ = Guid('{4b397f87-a2e6-479d-bdc8-6f4464646887}')
    @winrt_commethod(6)
    def get_Points(self) -> Windows.UI.Xaml.Media.PointCollection: ...
    @winrt_commethod(7)
    def put_Points(self, value: Windows.UI.Xaml.Media.PointCollection) -> Void: ...
    Points = property(get_Points, put_Points)
class IPolyLineSegmentStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IPolyLineSegmentStatics'
    _iid_ = Guid('{d64a2c87-33f1-4e70-a47f-b4981ef648a2}')
    @winrt_commethod(6)
    def get_PointsProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    PointsProperty = property(get_PointsProperty, None)
class IPolyQuadraticBezierSegment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IPolyQuadraticBezierSegment'
    _iid_ = Guid('{dd5ced7d-e6db-4c96-b6a1-3fce96e987a6}')
    @winrt_commethod(6)
    def get_Points(self) -> Windows.UI.Xaml.Media.PointCollection: ...
    @winrt_commethod(7)
    def put_Points(self, value: Windows.UI.Xaml.Media.PointCollection) -> Void: ...
    Points = property(get_Points, put_Points)
class IPolyQuadraticBezierSegmentStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IPolyQuadraticBezierSegmentStatics'
    _iid_ = Guid('{fdf5eb75-7ad5-4c89-8169-8c9786abd9eb}')
    @winrt_commethod(6)
    def get_PointsProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    PointsProperty = property(get_PointsProperty, None)
class IProjection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IProjection'
    _iid_ = Guid('{b3443557-7f39-4d04-a89c-844338cac897}')
class IProjectionFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IProjectionFactory'
    _iid_ = Guid('{c4f29cab-60ad-4f24-bd27-9d69c3127c9a}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.Projection: ...
class IQuadraticBezierSegment(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IQuadraticBezierSegment'
    _iid_ = Guid('{2c509a5b-bf18-455a-a078-914b5232d8af}')
    @winrt_commethod(6)
    def get_Point1(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def put_Point1(self, value: Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(8)
    def get_Point2(self) -> Windows.Foundation.Point: ...
    @winrt_commethod(9)
    def put_Point2(self, value: Windows.Foundation.Point) -> Void: ...
    Point1 = property(get_Point1, put_Point1)
    Point2 = property(get_Point2, put_Point2)
class IQuadraticBezierSegmentStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IQuadraticBezierSegmentStatics'
    _iid_ = Guid('{69c78278-3c0b-4b4f-b7a2-f003ded41bb0}')
    @winrt_commethod(6)
    def get_Point1Property(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_Point2Property(self) -> Windows.UI.Xaml.DependencyProperty: ...
    Point1Property = property(get_Point1Property, None)
    Point2Property = property(get_Point2Property, None)
class IRateChangedRoutedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IRateChangedRoutedEventArgs'
    _iid_ = Guid('{9016aa6f-3ca8-4c80-8e2f-8851a68f131f}')
class IRectangleGeometry(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IRectangleGeometry'
    _iid_ = Guid('{a25a1f58-c575-4196-91cf-9fdfb10445c3}')
    @winrt_commethod(6)
    def get_Rect(self) -> Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def put_Rect(self, value: Windows.Foundation.Rect) -> Void: ...
    Rect = property(get_Rect, put_Rect)
class IRectangleGeometryStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IRectangleGeometryStatics'
    _iid_ = Guid('{377f8dba-7902-48e3-83be-7c8002a6653c}')
    @winrt_commethod(6)
    def get_RectProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    RectProperty = property(get_RectProperty, None)
class IRenderedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IRenderedEventArgs'
    _iid_ = Guid('{e349817d-81c7-4938-828c-a7e2797b35a6}')
    @winrt_commethod(6)
    def get_FrameDuration(self) -> Windows.Foundation.TimeSpan: ...
    FrameDuration = property(get_FrameDuration, None)
class IRenderingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IRenderingEventArgs'
    _iid_ = Guid('{5bf7d30d-9748-4aed-8380-d7890eb776a0}')
    @winrt_commethod(6)
    def get_RenderingTime(self) -> Windows.Foundation.TimeSpan: ...
    RenderingTime = property(get_RenderingTime, None)
class IRevealBackgroundBrush(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IRevealBackgroundBrush'
    _iid_ = Guid('{261dcc0e-1991-4cdf-aee0-6350a3f90bb9}')
class IRevealBackgroundBrushFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IRevealBackgroundBrushFactory'
    _iid_ = Guid('{8c56bcaa-02a5-4f45-8506-8d39228f5d3f}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.RevealBackgroundBrush: ...
class IRevealBorderBrush(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IRevealBorderBrush'
    _iid_ = Guid('{060ba115-c542-483c-8202-5f03331866c9}')
class IRevealBorderBrushFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IRevealBorderBrushFactory'
    _iid_ = Guid('{94c25298-f5f8-4482-a25c-6758501a8626}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.RevealBorderBrush: ...
class IRevealBrush(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IRevealBrush'
    _iid_ = Guid('{2036a0ed-8271-4398-9019-25872093f13f}')
    @winrt_commethod(6)
    def get_Color(self) -> Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_Color(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(8)
    def get_TargetTheme(self) -> Windows.UI.Xaml.ApplicationTheme: ...
    @winrt_commethod(9)
    def put_TargetTheme(self, value: Windows.UI.Xaml.ApplicationTheme) -> Void: ...
    @winrt_commethod(10)
    def get_AlwaysUseFallback(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_AlwaysUseFallback(self, value: Boolean) -> Void: ...
    Color = property(get_Color, put_Color)
    TargetTheme = property(get_TargetTheme, put_TargetTheme)
    AlwaysUseFallback = property(get_AlwaysUseFallback, put_AlwaysUseFallback)
class IRevealBrushFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IRevealBrushFactory'
    _iid_ = Guid('{9d9379ce-e3a0-4aaf-be37-ea9d9dd43105}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.RevealBrush: ...
class IRevealBrushStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IRevealBrushStatics'
    _iid_ = Guid('{190f2625-7209-4d42-a847-1ac4bbbb3499}')
    @winrt_commethod(6)
    def get_ColorProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_TargetThemeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_AlwaysUseFallbackProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_StateProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def SetState(self, element: Windows.UI.Xaml.UIElement, value: Windows.UI.Xaml.Media.RevealBrushState) -> Void: ...
    @winrt_commethod(11)
    def GetState(self, element: Windows.UI.Xaml.UIElement) -> Windows.UI.Xaml.Media.RevealBrushState: ...
    ColorProperty = property(get_ColorProperty, None)
    TargetThemeProperty = property(get_TargetThemeProperty, None)
    AlwaysUseFallbackProperty = property(get_AlwaysUseFallbackProperty, None)
    StateProperty = property(get_StateProperty, None)
class IRotateTransform(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IRotateTransform'
    _iid_ = Guid('{688ea9b9-1e4e-4596-86e3-428b27334faf}')
    @winrt_commethod(6)
    def get_CenterX(self) -> Double: ...
    @winrt_commethod(7)
    def put_CenterX(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_CenterY(self) -> Double: ...
    @winrt_commethod(9)
    def put_CenterY(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_Angle(self) -> Double: ...
    @winrt_commethod(11)
    def put_Angle(self, value: Double) -> Void: ...
    CenterX = property(get_CenterX, put_CenterX)
    CenterY = property(get_CenterY, put_CenterY)
    Angle = property(get_Angle, put_Angle)
class IRotateTransformStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IRotateTransformStatics'
    _iid_ = Guid('{a131eb8a-51a3-41b6-b9d3-a10e429054ab}')
    @winrt_commethod(6)
    def get_CenterXProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_CenterYProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_AngleProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    CenterXProperty = property(get_CenterXProperty, None)
    CenterYProperty = property(get_CenterYProperty, None)
    AngleProperty = property(get_AngleProperty, None)
class IScaleTransform(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IScaleTransform'
    _iid_ = Guid('{ed67f18d-936e-43ab-929a-e9cd0a511e52}')
    @winrt_commethod(6)
    def get_CenterX(self) -> Double: ...
    @winrt_commethod(7)
    def put_CenterX(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_CenterY(self) -> Double: ...
    @winrt_commethod(9)
    def put_CenterY(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_ScaleX(self) -> Double: ...
    @winrt_commethod(11)
    def put_ScaleX(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def get_ScaleY(self) -> Double: ...
    @winrt_commethod(13)
    def put_ScaleY(self, value: Double) -> Void: ...
    CenterX = property(get_CenterX, put_CenterX)
    CenterY = property(get_CenterY, put_CenterY)
    ScaleX = property(get_ScaleX, put_ScaleX)
    ScaleY = property(get_ScaleY, put_ScaleY)
class IScaleTransformStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IScaleTransformStatics'
    _iid_ = Guid('{9d9436f4-40a7-46dd-975a-07d337cd852e}')
    @winrt_commethod(6)
    def get_CenterXProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_CenterYProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ScaleXProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_ScaleYProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    CenterXProperty = property(get_CenterXProperty, None)
    CenterYProperty = property(get_CenterYProperty, None)
    ScaleXProperty = property(get_ScaleXProperty, None)
    ScaleYProperty = property(get_ScaleYProperty, None)
class IShadow(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IShadow'
    _iid_ = Guid('{6813a583-f3b4-5fcf-8694-2cd0aefc2fad}')
class IShadowFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IShadowFactory'
    _iid_ = Guid('{19899f25-d28b-51e6-94b0-d7e709686305}')
class ISkewTransform(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ISkewTransform'
    _iid_ = Guid('{4e8a3b15-7a0f-4617-9e98-1e65bdc92115}')
    @winrt_commethod(6)
    def get_CenterX(self) -> Double: ...
    @winrt_commethod(7)
    def put_CenterX(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_CenterY(self) -> Double: ...
    @winrt_commethod(9)
    def put_CenterY(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_AngleX(self) -> Double: ...
    @winrt_commethod(11)
    def put_AngleX(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def get_AngleY(self) -> Double: ...
    @winrt_commethod(13)
    def put_AngleY(self, value: Double) -> Void: ...
    CenterX = property(get_CenterX, put_CenterX)
    CenterY = property(get_CenterY, put_CenterY)
    AngleX = property(get_AngleX, put_AngleX)
    AngleY = property(get_AngleY, put_AngleY)
class ISkewTransformStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ISkewTransformStatics'
    _iid_ = Guid('{ecd11d73-5614-4b31-b6af-beae10105624}')
    @winrt_commethod(6)
    def get_CenterXProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_CenterYProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_AngleXProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_AngleYProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    CenterXProperty = property(get_CenterXProperty, None)
    CenterYProperty = property(get_CenterYProperty, None)
    AngleXProperty = property(get_AngleXProperty, None)
    AngleYProperty = property(get_AngleYProperty, None)
class ISolidColorBrush(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ISolidColorBrush'
    _iid_ = Guid('{9d850850-66f3-48df-9a8f-824bd5e070af}')
    @winrt_commethod(6)
    def get_Color(self) -> Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_Color(self, value: Windows.UI.Color) -> Void: ...
    Color = property(get_Color, put_Color)
class ISolidColorBrushFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ISolidColorBrushFactory'
    _iid_ = Guid('{d935ce0c-86f5-4da6-8a27-b1619ef7f92b}')
    @winrt_commethod(6)
    def CreateInstanceWithColor(self, color: Windows.UI.Color) -> Windows.UI.Xaml.Media.SolidColorBrush: ...
class ISolidColorBrushStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ISolidColorBrushStatics'
    _iid_ = Guid('{e1a65efa-2b23-41ba-b9ba-7094ec8e4e9f}')
    @winrt_commethod(6)
    def get_ColorProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    ColorProperty = property(get_ColorProperty, None)
class IThemeShadow(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IThemeShadow'
    _iid_ = Guid('{3eccad09-7985-5f39-8b62-6c10696dca6f}')
    @winrt_commethod(6)
    def get_Receivers(self) -> Windows.UI.Xaml.UIElementWeakCollection: ...
    Receivers = property(get_Receivers, None)
class IThemeShadowFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IThemeShadowFactory'
    _iid_ = Guid('{2e71465d-0f67-590e-831b-7e5e2a32b778}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.ThemeShadow: ...
class ITileBrush(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ITileBrush'
    _iid_ = Guid('{c201cf06-cd84-48a5-9607-664d7361cd61}')
    @winrt_commethod(6)
    def get_AlignmentX(self) -> Windows.UI.Xaml.Media.AlignmentX: ...
    @winrt_commethod(7)
    def put_AlignmentX(self, value: Windows.UI.Xaml.Media.AlignmentX) -> Void: ...
    @winrt_commethod(8)
    def get_AlignmentY(self) -> Windows.UI.Xaml.Media.AlignmentY: ...
    @winrt_commethod(9)
    def put_AlignmentY(self, value: Windows.UI.Xaml.Media.AlignmentY) -> Void: ...
    @winrt_commethod(10)
    def get_Stretch(self) -> Windows.UI.Xaml.Media.Stretch: ...
    @winrt_commethod(11)
    def put_Stretch(self, value: Windows.UI.Xaml.Media.Stretch) -> Void: ...
    AlignmentX = property(get_AlignmentX, put_AlignmentX)
    AlignmentY = property(get_AlignmentY, put_AlignmentY)
    Stretch = property(get_Stretch, put_Stretch)
class ITileBrushFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ITileBrushFactory'
    _iid_ = Guid('{aa159f7c-ed6a-4fb3-b014-b5c7e379a4de}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.TileBrush: ...
class ITileBrushStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ITileBrushStatics'
    _iid_ = Guid('{3497c25b-b562-4e68-8435-2399f6eb94d5}')
    @winrt_commethod(6)
    def get_AlignmentXProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_AlignmentYProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_StretchProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    AlignmentXProperty = property(get_AlignmentXProperty, None)
    AlignmentYProperty = property(get_AlignmentYProperty, None)
    StretchProperty = property(get_StretchProperty, None)
class ITimelineMarker(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ITimelineMarker'
    _iid_ = Guid('{a68ef02d-45ba-4e50-8cad-aaea3a227af5}')
    @winrt_commethod(6)
    def get_Time(self) -> Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_Time(self, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_Type(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Type(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_Text(self, value: WinRT_String) -> Void: ...
    Time = property(get_Time, put_Time)
    Type = property(get_Type, put_Type)
    Text = property(get_Text, put_Text)
class ITimelineMarkerRoutedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ITimelineMarkerRoutedEventArgs'
    _iid_ = Guid('{7c3b3ef3-2c88-4d9c-99b6-46cdbd48d4c1}')
    @winrt_commethod(6)
    def get_Marker(self) -> Windows.UI.Xaml.Media.TimelineMarker: ...
    @winrt_commethod(7)
    def put_Marker(self, value: Windows.UI.Xaml.Media.TimelineMarker) -> Void: ...
    Marker = property(get_Marker, put_Marker)
class ITimelineMarkerStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ITimelineMarkerStatics'
    _iid_ = Guid('{c4aef0c6-16a3-484b-87f5-6528b8f04a47}')
    @winrt_commethod(6)
    def get_TimeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_TypeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_TextProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    TimeProperty = property(get_TimeProperty, None)
    TypeProperty = property(get_TypeProperty, None)
    TextProperty = property(get_TextProperty, None)
class ITransform(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ITransform'
    _iid_ = Guid('{4df74078-bfd6-4ed1-9682-d2fd8bf2fe6f}')
class ITransformFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ITransformFactory'
    _iid_ = Guid('{1a955a66-7cf4-4320-b416-6181192fcc6d}')
class ITransformGroup(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ITransformGroup'
    _iid_ = Guid('{63418ccc-8d2d-4737-b951-2afce1ddc4c4}')
    @winrt_commethod(6)
    def get_Children(self) -> Windows.UI.Xaml.Media.TransformCollection: ...
    @winrt_commethod(7)
    def put_Children(self, value: Windows.UI.Xaml.Media.TransformCollection) -> Void: ...
    @winrt_commethod(8)
    def get_Value(self) -> Windows.UI.Xaml.Media.Matrix: ...
    Children = property(get_Children, put_Children)
    Value = property(get_Value, None)
class ITransformGroupStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ITransformGroupStatics'
    _iid_ = Guid('{25312f2a-cfab-4b24-9713-5bdead1929c0}')
    @winrt_commethod(6)
    def get_ChildrenProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    ChildrenProperty = property(get_ChildrenProperty, None)
class ITranslateTransform(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ITranslateTransform'
    _iid_ = Guid('{c975905c-3c36-4229-817b-178f64c0e113}')
    @winrt_commethod(6)
    def get_X(self) -> Double: ...
    @winrt_commethod(7)
    def put_X(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_Y(self) -> Double: ...
    @winrt_commethod(9)
    def put_Y(self, value: Double) -> Void: ...
    X = property(get_X, put_X)
    Y = property(get_Y, put_Y)
class ITranslateTransformStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ITranslateTransformStatics'
    _iid_ = Guid('{f419aa91-e042-4111-9c2f-d201304123dd}')
    @winrt_commethod(6)
    def get_XProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_YProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    XProperty = property(get_XProperty, None)
    YProperty = property(get_YProperty, None)
class IVisualTreeHelper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IVisualTreeHelper'
    _iid_ = Guid('{24b935e3-52c7-4141-8bac-a73d06130569}')
class IVisualTreeHelperStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IVisualTreeHelperStatics'
    _iid_ = Guid('{e75758c4-d25d-4b1d-971f-596f17f12baa}')
    @winrt_commethod(6)
    def FindElementsInHostCoordinatesPoint(self, intersectingPoint: Windows.Foundation.Point, subtree: Windows.UI.Xaml.UIElement) -> Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.UIElement]: ...
    @winrt_commethod(7)
    def FindElementsInHostCoordinatesRect(self, intersectingRect: Windows.Foundation.Rect, subtree: Windows.UI.Xaml.UIElement) -> Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.UIElement]: ...
    @winrt_commethod(8)
    def FindAllElementsInHostCoordinatesPoint(self, intersectingPoint: Windows.Foundation.Point, subtree: Windows.UI.Xaml.UIElement, includeAllElements: Boolean) -> Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.UIElement]: ...
    @winrt_commethod(9)
    def FindAllElementsInHostCoordinatesRect(self, intersectingRect: Windows.Foundation.Rect, subtree: Windows.UI.Xaml.UIElement, includeAllElements: Boolean) -> Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.UIElement]: ...
    @winrt_commethod(10)
    def GetChild(self, reference: Windows.UI.Xaml.DependencyObject, childIndex: Int32) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(11)
    def GetChildrenCount(self, reference: Windows.UI.Xaml.DependencyObject) -> Int32: ...
    @winrt_commethod(12)
    def GetParent(self, reference: Windows.UI.Xaml.DependencyObject) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(13)
    def DisconnectChildrenRecursive(self, element: Windows.UI.Xaml.UIElement) -> Void: ...
class IVisualTreeHelperStatics2(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IVisualTreeHelperStatics2'
    _iid_ = Guid('{07bcd176-869f-44a7-8797-2103a4c3e47a}')
    @winrt_commethod(6)
    def GetOpenPopups(self, window: Windows.UI.Xaml.Window) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Controls.Primitives.Popup]: ...
class IVisualTreeHelperStatics3(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IVisualTreeHelperStatics3'
    _iid_ = Guid('{40420d50-ca16-57da-8aac-944c8af577fd}')
    @winrt_commethod(6)
    def GetOpenPopupsForXamlRoot(self, xamlRoot: Windows.UI.Xaml.XamlRoot) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Controls.Primitives.Popup]: ...
class IXamlCompositionBrushBase(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IXamlCompositionBrushBase'
    _iid_ = Guid('{03e432d9-b35c-4a79-811c-c5652004da0e}')
    @winrt_commethod(6)
    def get_FallbackColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_FallbackColor(self, value: Windows.UI.Color) -> Void: ...
    FallbackColor = property(get_FallbackColor, put_FallbackColor)
class IXamlCompositionBrushBaseFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IXamlCompositionBrushBaseFactory'
    _iid_ = Guid('{394f0823-2451-4ed8-bd24-488149b3428d}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.XamlCompositionBrushBase: ...
class IXamlCompositionBrushBaseOverrides(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IXamlCompositionBrushBaseOverrides'
    _iid_ = Guid('{d19127f1-38b4-4ea1-8f33-849629a4c9c1}')
    @winrt_commethod(6)
    def OnConnected(self) -> Void: ...
    @winrt_commethod(7)
    def OnDisconnected(self) -> Void: ...
class IXamlCompositionBrushBaseProtected(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IXamlCompositionBrushBaseProtected'
    _iid_ = Guid('{1513f3d8-0457-4e1c-ad77-11c1d9879743}')
    @winrt_commethod(6)
    def get_CompositionBrush(self) -> Windows.UI.Composition.CompositionBrush: ...
    @winrt_commethod(7)
    def put_CompositionBrush(self, value: Windows.UI.Composition.CompositionBrush) -> Void: ...
    CompositionBrush = property(get_CompositionBrush, put_CompositionBrush)
class IXamlCompositionBrushBaseStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IXamlCompositionBrushBaseStatics'
    _iid_ = Guid('{4fd49b06-061a-441f-b97a-adfbd41ae681}')
    @winrt_commethod(6)
    def get_FallbackColorProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    FallbackColorProperty = property(get_FallbackColorProperty, None)
class IXamlLight(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IXamlLight'
    _iid_ = Guid('{0cc3fc1f-b327-4a18-9648-7c84db26ce22}')
class IXamlLightFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IXamlLightFactory'
    _iid_ = Guid('{87ded768-3055-43b8-8ef6-798dc4c2329a}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Media.XamlLight: ...
class IXamlLightOverrides(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IXamlLightOverrides'
    _iid_ = Guid('{7c6296c7-0173-48e1-b73d-7fa216a9ac28}')
    @winrt_commethod(6)
    def GetId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def OnConnected(self, newElement: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(8)
    def OnDisconnected(self, oldElement: Windows.UI.Xaml.UIElement) -> Void: ...
class IXamlLightProtected(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IXamlLightProtected'
    _iid_ = Guid('{5ecf220b-1252-43d0-9729-6ea692046838}')
    @winrt_commethod(6)
    def get_CompositionLight(self) -> Windows.UI.Composition.CompositionLight: ...
    @winrt_commethod(7)
    def put_CompositionLight(self, value: Windows.UI.Composition.CompositionLight) -> Void: ...
    CompositionLight = property(get_CompositionLight, put_CompositionLight)
class IXamlLightStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IXamlLightStatics'
    _iid_ = Guid('{b5ea9d69-b508-4e9c-bd27-6b044b5f78a0}')
    @winrt_commethod(6)
    def AddTargetElement(self, lightId: WinRT_String, element: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(7)
    def RemoveTargetElement(self, lightId: WinRT_String, element: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(8)
    def AddTargetBrush(self, lightId: WinRT_String, brush: Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(9)
    def RemoveTargetBrush(self, lightId: WinRT_String, brush: Windows.UI.Xaml.Media.Brush) -> Void: ...
class ImageBrush(ComPtr):
    extends: Windows.UI.Xaml.Media.TileBrush
    default_interface: Windows.UI.Xaml.Media.IImageBrush
    _classid_ = 'Windows.UI.Xaml.Media.ImageBrush'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.ImageBrush: ...
    @winrt_mixinmethod
    def get_ImageSource(self: Windows.UI.Xaml.Media.IImageBrush) -> Windows.UI.Xaml.Media.ImageSource: ...
    @winrt_mixinmethod
    def put_ImageSource(self: Windows.UI.Xaml.Media.IImageBrush, value: Windows.UI.Xaml.Media.ImageSource) -> Void: ...
    @winrt_mixinmethod
    def add_ImageFailed(self: Windows.UI.Xaml.Media.IImageBrush, handler: Windows.UI.Xaml.ExceptionRoutedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ImageFailed(self: Windows.UI.Xaml.Media.IImageBrush, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ImageOpened(self: Windows.UI.Xaml.Media.IImageBrush, handler: Windows.UI.Xaml.RoutedEventHandler) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ImageOpened(self: Windows.UI.Xaml.Media.IImageBrush, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_ImageSourceProperty(cls: Windows.UI.Xaml.Media.IImageBrushStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    ImageSource = property(get_ImageSource, put_ImageSource)
    ImageSourceProperty = property(get_ImageSourceProperty, None)
class ImageSource(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Media.IImageSource
    _classid_ = 'Windows.UI.Xaml.Media.ImageSource'
class LineGeometry(ComPtr):
    extends: Windows.UI.Xaml.Media.Geometry
    default_interface: Windows.UI.Xaml.Media.ILineGeometry
    _classid_ = 'Windows.UI.Xaml.Media.LineGeometry'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.LineGeometry: ...
    @winrt_mixinmethod
    def get_StartPoint(self: Windows.UI.Xaml.Media.ILineGeometry) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_StartPoint(self: Windows.UI.Xaml.Media.ILineGeometry, value: Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_EndPoint(self: Windows.UI.Xaml.Media.ILineGeometry) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_EndPoint(self: Windows.UI.Xaml.Media.ILineGeometry, value: Windows.Foundation.Point) -> Void: ...
    @winrt_classmethod
    def get_StartPointProperty(cls: Windows.UI.Xaml.Media.ILineGeometryStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_EndPointProperty(cls: Windows.UI.Xaml.Media.ILineGeometryStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    StartPoint = property(get_StartPoint, put_StartPoint)
    EndPoint = property(get_EndPoint, put_EndPoint)
    StartPointProperty = property(get_StartPointProperty, None)
    EndPointProperty = property(get_EndPointProperty, None)
class LineSegment(ComPtr):
    extends: Windows.UI.Xaml.Media.PathSegment
    default_interface: Windows.UI.Xaml.Media.ILineSegment
    _classid_ = 'Windows.UI.Xaml.Media.LineSegment'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.LineSegment: ...
    @winrt_mixinmethod
    def get_Point(self: Windows.UI.Xaml.Media.ILineSegment) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Point(self: Windows.UI.Xaml.Media.ILineSegment, value: Windows.Foundation.Point) -> Void: ...
    @winrt_classmethod
    def get_PointProperty(cls: Windows.UI.Xaml.Media.ILineSegmentStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Point = property(get_Point, put_Point)
    PointProperty = property(get_PointProperty, None)
class LinearGradientBrush(ComPtr):
    extends: Windows.UI.Xaml.Media.GradientBrush
    default_interface: Windows.UI.Xaml.Media.ILinearGradientBrush
    _classid_ = 'Windows.UI.Xaml.Media.LinearGradientBrush'
    @winrt_factorymethod
    def CreateInstanceWithGradientStopCollectionAndAngle(cls: Windows.UI.Xaml.Media.ILinearGradientBrushFactory, gradientStopCollection: Windows.UI.Xaml.Media.GradientStopCollection, angle: Double) -> Windows.UI.Xaml.Media.LinearGradientBrush: ...
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.LinearGradientBrush: ...
    @winrt_mixinmethod
    def get_StartPoint(self: Windows.UI.Xaml.Media.ILinearGradientBrush) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_StartPoint(self: Windows.UI.Xaml.Media.ILinearGradientBrush, value: Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_EndPoint(self: Windows.UI.Xaml.Media.ILinearGradientBrush) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_EndPoint(self: Windows.UI.Xaml.Media.ILinearGradientBrush, value: Windows.Foundation.Point) -> Void: ...
    @winrt_classmethod
    def get_StartPointProperty(cls: Windows.UI.Xaml.Media.ILinearGradientBrushStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_EndPointProperty(cls: Windows.UI.Xaml.Media.ILinearGradientBrushStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    StartPoint = property(get_StartPoint, put_StartPoint)
    EndPoint = property(get_EndPoint, put_EndPoint)
    StartPointProperty = property(get_StartPointProperty, None)
    EndPointProperty = property(get_EndPointProperty, None)
class LoadedImageSourceLoadCompletedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Media.ILoadedImageSourceLoadCompletedEventArgs
    _classid_ = 'Windows.UI.Xaml.Media.LoadedImageSourceLoadCompletedEventArgs'
    @winrt_mixinmethod
    def get_Status(self: Windows.UI.Xaml.Media.ILoadedImageSourceLoadCompletedEventArgs) -> Windows.UI.Xaml.Media.LoadedImageSourceLoadStatus: ...
    Status = property(get_Status, None)
LoadedImageSourceLoadStatus = Int32
LoadedImageSourceLoadStatus_Success: LoadedImageSourceLoadStatus = 0
LoadedImageSourceLoadStatus_NetworkError: LoadedImageSourceLoadStatus = 1
LoadedImageSourceLoadStatus_InvalidFormat: LoadedImageSourceLoadStatus = 2
LoadedImageSourceLoadStatus_Other: LoadedImageSourceLoadStatus = 3
class LoadedImageSurface(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Media.ILoadedImageSurface
    _classid_ = 'Windows.UI.Xaml.Media.LoadedImageSurface'
    @winrt_mixinmethod
    def get_DecodedPhysicalSize(self: Windows.UI.Xaml.Media.ILoadedImageSurface) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_DecodedSize(self: Windows.UI.Xaml.Media.ILoadedImageSurface) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_NaturalSize(self: Windows.UI.Xaml.Media.ILoadedImageSurface) -> Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def add_LoadCompleted(self: Windows.UI.Xaml.Media.ILoadedImageSurface, handler: Windows.Foundation.TypedEventHandler[Windows.UI.Xaml.Media.LoadedImageSurface, Windows.UI.Xaml.Media.LoadedImageSourceLoadCompletedEventArgs]) -> Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LoadCompleted(self: Windows.UI.Xaml.Media.ILoadedImageSurface, token: Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def StartLoadFromUriWithSize(cls: Windows.UI.Xaml.Media.ILoadedImageSurfaceStatics, uri: Windows.Foundation.Uri, desiredMaxSize: Windows.Foundation.Size) -> Windows.UI.Xaml.Media.LoadedImageSurface: ...
    @winrt_classmethod
    def StartLoadFromUri(cls: Windows.UI.Xaml.Media.ILoadedImageSurfaceStatics, uri: Windows.Foundation.Uri) -> Windows.UI.Xaml.Media.LoadedImageSurface: ...
    @winrt_classmethod
    def StartLoadFromStreamWithSize(cls: Windows.UI.Xaml.Media.ILoadedImageSurfaceStatics, stream: Windows.Storage.Streams.IRandomAccessStream, desiredMaxSize: Windows.Foundation.Size) -> Windows.UI.Xaml.Media.LoadedImageSurface: ...
    @winrt_classmethod
    def StartLoadFromStream(cls: Windows.UI.Xaml.Media.ILoadedImageSurfaceStatics, stream: Windows.Storage.Streams.IRandomAccessStream) -> Windows.UI.Xaml.Media.LoadedImageSurface: ...
    DecodedPhysicalSize = property(get_DecodedPhysicalSize, None)
    DecodedSize = property(get_DecodedSize, None)
    NaturalSize = property(get_NaturalSize, None)
class Matrix(EasyCastStructure):
    M11: Double
    M12: Double
    M21: Double
    M22: Double
    OffsetX: Double
    OffsetY: Double
class Matrix3DProjection(ComPtr):
    extends: Windows.UI.Xaml.Media.Projection
    default_interface: Windows.UI.Xaml.Media.IMatrix3DProjection
    _classid_ = 'Windows.UI.Xaml.Media.Matrix3DProjection'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.Matrix3DProjection: ...
    @winrt_mixinmethod
    def get_ProjectionMatrix(self: Windows.UI.Xaml.Media.IMatrix3DProjection) -> Windows.UI.Xaml.Media.Media3D.Matrix3D: ...
    @winrt_mixinmethod
    def put_ProjectionMatrix(self: Windows.UI.Xaml.Media.IMatrix3DProjection, value: Windows.UI.Xaml.Media.Media3D.Matrix3D) -> Void: ...
    @winrt_classmethod
    def get_ProjectionMatrixProperty(cls: Windows.UI.Xaml.Media.IMatrix3DProjectionStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    ProjectionMatrix = property(get_ProjectionMatrix, put_ProjectionMatrix)
    ProjectionMatrixProperty = property(get_ProjectionMatrixProperty, None)
class MatrixHelper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Media.IMatrixHelper
    _classid_ = 'Windows.UI.Xaml.Media.MatrixHelper'
    @winrt_classmethod
    def get_Identity(cls: Windows.UI.Xaml.Media.IMatrixHelperStatics) -> Windows.UI.Xaml.Media.Matrix: ...
    @winrt_classmethod
    def FromElements(cls: Windows.UI.Xaml.Media.IMatrixHelperStatics, m11: Double, m12: Double, m21: Double, m22: Double, offsetX: Double, offsetY: Double) -> Windows.UI.Xaml.Media.Matrix: ...
    @winrt_classmethod
    def GetIsIdentity(cls: Windows.UI.Xaml.Media.IMatrixHelperStatics, target: Windows.UI.Xaml.Media.Matrix) -> Boolean: ...
    @winrt_classmethod
    def Transform(cls: Windows.UI.Xaml.Media.IMatrixHelperStatics, target: Windows.UI.Xaml.Media.Matrix, point: Windows.Foundation.Point) -> Windows.Foundation.Point: ...
    Identity = property(get_Identity, None)
class MatrixTransform(ComPtr):
    extends: Windows.UI.Xaml.Media.Transform
    default_interface: Windows.UI.Xaml.Media.IMatrixTransform
    _classid_ = 'Windows.UI.Xaml.Media.MatrixTransform'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.MatrixTransform: ...
    @winrt_mixinmethod
    def get_Matrix(self: Windows.UI.Xaml.Media.IMatrixTransform) -> Windows.UI.Xaml.Media.Matrix: ...
    @winrt_mixinmethod
    def put_Matrix(self: Windows.UI.Xaml.Media.IMatrixTransform, value: Windows.UI.Xaml.Media.Matrix) -> Void: ...
    @winrt_classmethod
    def get_MatrixProperty(cls: Windows.UI.Xaml.Media.IMatrixTransformStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Matrix = property(get_Matrix, put_Matrix)
    MatrixProperty = property(get_MatrixProperty, None)
MediaCanPlayResponse = Int32
MediaCanPlayResponse_NotSupported: MediaCanPlayResponse = 0
MediaCanPlayResponse_Maybe: MediaCanPlayResponse = 1
MediaCanPlayResponse_Probably: MediaCanPlayResponse = 2
MediaElementState = Int32
MediaElementState_Closed: MediaElementState = 0
MediaElementState_Opening: MediaElementState = 1
MediaElementState_Buffering: MediaElementState = 2
MediaElementState_Playing: MediaElementState = 3
MediaElementState_Paused: MediaElementState = 4
MediaElementState_Stopped: MediaElementState = 5
class MediaTransportControlsThumbnailRequestedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Media.IMediaTransportControlsThumbnailRequestedEventArgs
    _classid_ = 'Windows.UI.Xaml.Media.MediaTransportControlsThumbnailRequestedEventArgs'
    @winrt_mixinmethod
    def SetThumbnailImage(self: Windows.UI.Xaml.Media.IMediaTransportControlsThumbnailRequestedEventArgs, source: Windows.Storage.Streams.IInputStream) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: Windows.UI.Xaml.Media.IMediaTransportControlsThumbnailRequestedEventArgs) -> Windows.Foundation.Deferral: ...
class PartialMediaFailureDetectedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Media.IPartialMediaFailureDetectedEventArgs
    _classid_ = 'Windows.UI.Xaml.Media.PartialMediaFailureDetectedEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.PartialMediaFailureDetectedEventArgs: ...
    @winrt_mixinmethod
    def get_StreamKind(self: Windows.UI.Xaml.Media.IPartialMediaFailureDetectedEventArgs) -> Windows.Media.Playback.FailedMediaStreamKind: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: Windows.UI.Xaml.Media.IPartialMediaFailureDetectedEventArgs2) -> Windows.Foundation.HResult: ...
    StreamKind = property(get_StreamKind, None)
    ExtendedError = property(get_ExtendedError, None)
class PathFigure(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Media.IPathFigure
    _classid_ = 'Windows.UI.Xaml.Media.PathFigure'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.PathFigure: ...
    @winrt_mixinmethod
    def get_Segments(self: Windows.UI.Xaml.Media.IPathFigure) -> Windows.UI.Xaml.Media.PathSegmentCollection: ...
    @winrt_mixinmethod
    def put_Segments(self: Windows.UI.Xaml.Media.IPathFigure, value: Windows.UI.Xaml.Media.PathSegmentCollection) -> Void: ...
    @winrt_mixinmethod
    def get_StartPoint(self: Windows.UI.Xaml.Media.IPathFigure) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_StartPoint(self: Windows.UI.Xaml.Media.IPathFigure, value: Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_IsClosed(self: Windows.UI.Xaml.Media.IPathFigure) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsClosed(self: Windows.UI.Xaml.Media.IPathFigure, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsFilled(self: Windows.UI.Xaml.Media.IPathFigure) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsFilled(self: Windows.UI.Xaml.Media.IPathFigure, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_SegmentsProperty(cls: Windows.UI.Xaml.Media.IPathFigureStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StartPointProperty(cls: Windows.UI.Xaml.Media.IPathFigureStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsClosedProperty(cls: Windows.UI.Xaml.Media.IPathFigureStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsFilledProperty(cls: Windows.UI.Xaml.Media.IPathFigureStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Segments = property(get_Segments, put_Segments)
    StartPoint = property(get_StartPoint, put_StartPoint)
    IsClosed = property(get_IsClosed, put_IsClosed)
    IsFilled = property(get_IsFilled, put_IsFilled)
    SegmentsProperty = property(get_SegmentsProperty, None)
    StartPointProperty = property(get_StartPointProperty, None)
    IsClosedProperty = property(get_IsClosedProperty, None)
    IsFilledProperty = property(get_IsFilledProperty, None)
class PathFigureCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.PathFigure]
    _classid_ = 'Windows.UI.Xaml.Media.PathFigureCollection'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.PathFigureCollection: ...
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.PathFigure], index: UInt32) -> Windows.UI.Xaml.Media.PathFigure: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.PathFigure]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.PathFigure]) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Media.PathFigure]: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.PathFigure], value: Windows.UI.Xaml.Media.PathFigure, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.PathFigure], index: UInt32, value: Windows.UI.Xaml.Media.PathFigure) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.PathFigure], index: UInt32, value: Windows.UI.Xaml.Media.PathFigure) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.PathFigure], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.PathFigure], value: Windows.UI.Xaml.Media.PathFigure) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.PathFigure]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.PathFigure]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.PathFigure], startIndex: UInt32, items: POINTER(Windows.UI.Xaml.Media.PathFigure)) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.PathFigure], items: POINTER(Windows.UI.Xaml.Media.PathFigure)) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.Media.PathFigure]) -> Windows.Foundation.Collections.IIterator[Windows.UI.Xaml.Media.PathFigure]: ...
    Size = property(get_Size, None)
class PathGeometry(ComPtr):
    extends: Windows.UI.Xaml.Media.Geometry
    default_interface: Windows.UI.Xaml.Media.IPathGeometry
    _classid_ = 'Windows.UI.Xaml.Media.PathGeometry'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.PathGeometry: ...
    @winrt_mixinmethod
    def get_FillRule(self: Windows.UI.Xaml.Media.IPathGeometry) -> Windows.UI.Xaml.Media.FillRule: ...
    @winrt_mixinmethod
    def put_FillRule(self: Windows.UI.Xaml.Media.IPathGeometry, value: Windows.UI.Xaml.Media.FillRule) -> Void: ...
    @winrt_mixinmethod
    def get_Figures(self: Windows.UI.Xaml.Media.IPathGeometry) -> Windows.UI.Xaml.Media.PathFigureCollection: ...
    @winrt_mixinmethod
    def put_Figures(self: Windows.UI.Xaml.Media.IPathGeometry, value: Windows.UI.Xaml.Media.PathFigureCollection) -> Void: ...
    @winrt_classmethod
    def get_FillRuleProperty(cls: Windows.UI.Xaml.Media.IPathGeometryStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FiguresProperty(cls: Windows.UI.Xaml.Media.IPathGeometryStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    FillRule = property(get_FillRule, put_FillRule)
    Figures = property(get_Figures, put_Figures)
    FillRuleProperty = property(get_FillRuleProperty, None)
    FiguresProperty = property(get_FiguresProperty, None)
class PathSegment(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Media.IPathSegment
    _classid_ = 'Windows.UI.Xaml.Media.PathSegment'
class PathSegmentCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.PathSegment]
    _classid_ = 'Windows.UI.Xaml.Media.PathSegmentCollection'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.PathSegmentCollection: ...
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.PathSegment], index: UInt32) -> Windows.UI.Xaml.Media.PathSegment: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.PathSegment]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.PathSegment]) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Media.PathSegment]: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.PathSegment], value: Windows.UI.Xaml.Media.PathSegment, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.PathSegment], index: UInt32, value: Windows.UI.Xaml.Media.PathSegment) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.PathSegment], index: UInt32, value: Windows.UI.Xaml.Media.PathSegment) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.PathSegment], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.PathSegment], value: Windows.UI.Xaml.Media.PathSegment) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.PathSegment]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.PathSegment]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.PathSegment], startIndex: UInt32, items: POINTER(Windows.UI.Xaml.Media.PathSegment)) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.PathSegment], items: POINTER(Windows.UI.Xaml.Media.PathSegment)) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.Media.PathSegment]) -> Windows.Foundation.Collections.IIterator[Windows.UI.Xaml.Media.PathSegment]: ...
    Size = property(get_Size, None)
PenLineCap = Int32
PenLineCap_Flat: PenLineCap = 0
PenLineCap_Square: PenLineCap = 1
PenLineCap_Round: PenLineCap = 2
PenLineCap_Triangle: PenLineCap = 3
PenLineJoin = Int32
PenLineJoin_Miter: PenLineJoin = 0
PenLineJoin_Bevel: PenLineJoin = 1
PenLineJoin_Round: PenLineJoin = 2
class PlaneProjection(ComPtr):
    extends: Windows.UI.Xaml.Media.Projection
    default_interface: Windows.UI.Xaml.Media.IPlaneProjection
    _classid_ = 'Windows.UI.Xaml.Media.PlaneProjection'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.PlaneProjection: ...
    @winrt_mixinmethod
    def get_LocalOffsetX(self: Windows.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_LocalOffsetX(self: Windows.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_LocalOffsetY(self: Windows.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_LocalOffsetY(self: Windows.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_LocalOffsetZ(self: Windows.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_LocalOffsetZ(self: Windows.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RotationX(self: Windows.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_RotationX(self: Windows.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RotationY(self: Windows.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_RotationY(self: Windows.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RotationZ(self: Windows.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_RotationZ(self: Windows.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_CenterOfRotationX(self: Windows.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_CenterOfRotationX(self: Windows.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_CenterOfRotationY(self: Windows.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_CenterOfRotationY(self: Windows.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_CenterOfRotationZ(self: Windows.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_CenterOfRotationZ(self: Windows.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_GlobalOffsetX(self: Windows.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_GlobalOffsetX(self: Windows.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_GlobalOffsetY(self: Windows.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_GlobalOffsetY(self: Windows.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_GlobalOffsetZ(self: Windows.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_GlobalOffsetZ(self: Windows.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ProjectionMatrix(self: Windows.UI.Xaml.Media.IPlaneProjection) -> Windows.UI.Xaml.Media.Media3D.Matrix3D: ...
    @winrt_classmethod
    def get_LocalOffsetXProperty(cls: Windows.UI.Xaml.Media.IPlaneProjectionStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_LocalOffsetYProperty(cls: Windows.UI.Xaml.Media.IPlaneProjectionStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_LocalOffsetZProperty(cls: Windows.UI.Xaml.Media.IPlaneProjectionStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RotationXProperty(cls: Windows.UI.Xaml.Media.IPlaneProjectionStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RotationYProperty(cls: Windows.UI.Xaml.Media.IPlaneProjectionStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RotationZProperty(cls: Windows.UI.Xaml.Media.IPlaneProjectionStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CenterOfRotationXProperty(cls: Windows.UI.Xaml.Media.IPlaneProjectionStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CenterOfRotationYProperty(cls: Windows.UI.Xaml.Media.IPlaneProjectionStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CenterOfRotationZProperty(cls: Windows.UI.Xaml.Media.IPlaneProjectionStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_GlobalOffsetXProperty(cls: Windows.UI.Xaml.Media.IPlaneProjectionStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_GlobalOffsetYProperty(cls: Windows.UI.Xaml.Media.IPlaneProjectionStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_GlobalOffsetZProperty(cls: Windows.UI.Xaml.Media.IPlaneProjectionStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ProjectionMatrixProperty(cls: Windows.UI.Xaml.Media.IPlaneProjectionStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    LocalOffsetX = property(get_LocalOffsetX, put_LocalOffsetX)
    LocalOffsetY = property(get_LocalOffsetY, put_LocalOffsetY)
    LocalOffsetZ = property(get_LocalOffsetZ, put_LocalOffsetZ)
    RotationX = property(get_RotationX, put_RotationX)
    RotationY = property(get_RotationY, put_RotationY)
    RotationZ = property(get_RotationZ, put_RotationZ)
    CenterOfRotationX = property(get_CenterOfRotationX, put_CenterOfRotationX)
    CenterOfRotationY = property(get_CenterOfRotationY, put_CenterOfRotationY)
    CenterOfRotationZ = property(get_CenterOfRotationZ, put_CenterOfRotationZ)
    GlobalOffsetX = property(get_GlobalOffsetX, put_GlobalOffsetX)
    GlobalOffsetY = property(get_GlobalOffsetY, put_GlobalOffsetY)
    GlobalOffsetZ = property(get_GlobalOffsetZ, put_GlobalOffsetZ)
    ProjectionMatrix = property(get_ProjectionMatrix, None)
    LocalOffsetXProperty = property(get_LocalOffsetXProperty, None)
    LocalOffsetYProperty = property(get_LocalOffsetYProperty, None)
    LocalOffsetZProperty = property(get_LocalOffsetZProperty, None)
    RotationXProperty = property(get_RotationXProperty, None)
    RotationYProperty = property(get_RotationYProperty, None)
    RotationZProperty = property(get_RotationZProperty, None)
    CenterOfRotationXProperty = property(get_CenterOfRotationXProperty, None)
    CenterOfRotationYProperty = property(get_CenterOfRotationYProperty, None)
    CenterOfRotationZProperty = property(get_CenterOfRotationZProperty, None)
    GlobalOffsetXProperty = property(get_GlobalOffsetXProperty, None)
    GlobalOffsetYProperty = property(get_GlobalOffsetYProperty, None)
    GlobalOffsetZProperty = property(get_GlobalOffsetZProperty, None)
    ProjectionMatrixProperty = property(get_ProjectionMatrixProperty, None)
class PointCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IVector[Windows.Foundation.Point]
    _classid_ = 'Windows.UI.Xaml.Media.PointCollection'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.PointCollection: ...
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVector[Windows.Foundation.Point], index: UInt32) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVector[Windows.Foundation.Point]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IVector[Windows.Foundation.Point]) -> Windows.Foundation.Collections.IVectorView[Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVector[Windows.Foundation.Point], value: Windows.Foundation.Point, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: Windows.Foundation.Collections.IVector[Windows.Foundation.Point], index: UInt32, value: Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: Windows.Foundation.Collections.IVector[Windows.Foundation.Point], index: UInt32, value: Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: Windows.Foundation.Collections.IVector[Windows.Foundation.Point], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: Windows.Foundation.Collections.IVector[Windows.Foundation.Point], value: Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: Windows.Foundation.Collections.IVector[Windows.Foundation.Point]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IVector[Windows.Foundation.Point]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVector[Windows.Foundation.Point], startIndex: UInt32, items: POINTER(Windows.Foundation.Point_head)) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: Windows.Foundation.Collections.IVector[Windows.Foundation.Point], items: POINTER(Windows.Foundation.Point_head)) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.Foundation.Point]) -> Windows.Foundation.Collections.IIterator[Windows.Foundation.Point]: ...
    Size = property(get_Size, None)
class PolyBezierSegment(ComPtr):
    extends: Windows.UI.Xaml.Media.PathSegment
    default_interface: Windows.UI.Xaml.Media.IPolyBezierSegment
    _classid_ = 'Windows.UI.Xaml.Media.PolyBezierSegment'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.PolyBezierSegment: ...
    @winrt_mixinmethod
    def get_Points(self: Windows.UI.Xaml.Media.IPolyBezierSegment) -> Windows.UI.Xaml.Media.PointCollection: ...
    @winrt_mixinmethod
    def put_Points(self: Windows.UI.Xaml.Media.IPolyBezierSegment, value: Windows.UI.Xaml.Media.PointCollection) -> Void: ...
    @winrt_classmethod
    def get_PointsProperty(cls: Windows.UI.Xaml.Media.IPolyBezierSegmentStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Points = property(get_Points, put_Points)
    PointsProperty = property(get_PointsProperty, None)
class PolyLineSegment(ComPtr):
    extends: Windows.UI.Xaml.Media.PathSegment
    default_interface: Windows.UI.Xaml.Media.IPolyLineSegment
    _classid_ = 'Windows.UI.Xaml.Media.PolyLineSegment'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.PolyLineSegment: ...
    @winrt_mixinmethod
    def get_Points(self: Windows.UI.Xaml.Media.IPolyLineSegment) -> Windows.UI.Xaml.Media.PointCollection: ...
    @winrt_mixinmethod
    def put_Points(self: Windows.UI.Xaml.Media.IPolyLineSegment, value: Windows.UI.Xaml.Media.PointCollection) -> Void: ...
    @winrt_classmethod
    def get_PointsProperty(cls: Windows.UI.Xaml.Media.IPolyLineSegmentStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Points = property(get_Points, put_Points)
    PointsProperty = property(get_PointsProperty, None)
class PolyQuadraticBezierSegment(ComPtr):
    extends: Windows.UI.Xaml.Media.PathSegment
    default_interface: Windows.UI.Xaml.Media.IPolyQuadraticBezierSegment
    _classid_ = 'Windows.UI.Xaml.Media.PolyQuadraticBezierSegment'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.PolyQuadraticBezierSegment: ...
    @winrt_mixinmethod
    def get_Points(self: Windows.UI.Xaml.Media.IPolyQuadraticBezierSegment) -> Windows.UI.Xaml.Media.PointCollection: ...
    @winrt_mixinmethod
    def put_Points(self: Windows.UI.Xaml.Media.IPolyQuadraticBezierSegment, value: Windows.UI.Xaml.Media.PointCollection) -> Void: ...
    @winrt_classmethod
    def get_PointsProperty(cls: Windows.UI.Xaml.Media.IPolyQuadraticBezierSegmentStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Points = property(get_Points, put_Points)
    PointsProperty = property(get_PointsProperty, None)
class Projection(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Media.IProjection
    _classid_ = 'Windows.UI.Xaml.Media.Projection'
class QuadraticBezierSegment(ComPtr):
    extends: Windows.UI.Xaml.Media.PathSegment
    default_interface: Windows.UI.Xaml.Media.IQuadraticBezierSegment
    _classid_ = 'Windows.UI.Xaml.Media.QuadraticBezierSegment'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.QuadraticBezierSegment: ...
    @winrt_mixinmethod
    def get_Point1(self: Windows.UI.Xaml.Media.IQuadraticBezierSegment) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Point1(self: Windows.UI.Xaml.Media.IQuadraticBezierSegment, value: Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_Point2(self: Windows.UI.Xaml.Media.IQuadraticBezierSegment) -> Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Point2(self: Windows.UI.Xaml.Media.IQuadraticBezierSegment, value: Windows.Foundation.Point) -> Void: ...
    @winrt_classmethod
    def get_Point1Property(cls: Windows.UI.Xaml.Media.IQuadraticBezierSegmentStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_Point2Property(cls: Windows.UI.Xaml.Media.IQuadraticBezierSegmentStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Point1 = property(get_Point1, put_Point1)
    Point2 = property(get_Point2, put_Point2)
    Point1Property = property(get_Point1Property, None)
    Point2Property = property(get_Point2Property, None)
class RateChangedRoutedEventArgs(ComPtr):
    extends: Windows.UI.Xaml.RoutedEventArgs
    default_interface: Windows.UI.Xaml.Media.IRateChangedRoutedEventArgs
    _classid_ = 'Windows.UI.Xaml.Media.RateChangedRoutedEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.RateChangedRoutedEventArgs: ...
class RateChangedRoutedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.Xaml.Media.RateChangedRoutedEventHandler'
    _iid_ = Guid('{08e9a257-ae05-489b-8839-28c6225d2349}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.Media.RateChangedRoutedEventArgs) -> Void: ...
class RectangleGeometry(ComPtr):
    extends: Windows.UI.Xaml.Media.Geometry
    default_interface: Windows.UI.Xaml.Media.IRectangleGeometry
    _classid_ = 'Windows.UI.Xaml.Media.RectangleGeometry'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.RectangleGeometry: ...
    @winrt_mixinmethod
    def get_Rect(self: Windows.UI.Xaml.Media.IRectangleGeometry) -> Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def put_Rect(self: Windows.UI.Xaml.Media.IRectangleGeometry, value: Windows.Foundation.Rect) -> Void: ...
    @winrt_classmethod
    def get_RectProperty(cls: Windows.UI.Xaml.Media.IRectangleGeometryStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Rect = property(get_Rect, put_Rect)
    RectProperty = property(get_RectProperty, None)
class RenderedEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Media.IRenderedEventArgs
    _classid_ = 'Windows.UI.Xaml.Media.RenderedEventArgs'
    @winrt_mixinmethod
    def get_FrameDuration(self: Windows.UI.Xaml.Media.IRenderedEventArgs) -> Windows.Foundation.TimeSpan: ...
    FrameDuration = property(get_FrameDuration, None)
class RenderingEventArgs(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Media.IRenderingEventArgs
    _classid_ = 'Windows.UI.Xaml.Media.RenderingEventArgs'
    @winrt_mixinmethod
    def get_RenderingTime(self: Windows.UI.Xaml.Media.IRenderingEventArgs) -> Windows.Foundation.TimeSpan: ...
    RenderingTime = property(get_RenderingTime, None)
class RevealBackgroundBrush(ComPtr):
    extends: Windows.UI.Xaml.Media.RevealBrush
    default_interface: Windows.UI.Xaml.Media.IRevealBackgroundBrush
    _classid_ = 'Windows.UI.Xaml.Media.RevealBackgroundBrush'
class RevealBorderBrush(ComPtr):
    extends: Windows.UI.Xaml.Media.RevealBrush
    default_interface: Windows.UI.Xaml.Media.IRevealBorderBrush
    _classid_ = 'Windows.UI.Xaml.Media.RevealBorderBrush'
class RevealBrush(ComPtr):
    extends: Windows.UI.Xaml.Media.XamlCompositionBrushBase
    default_interface: Windows.UI.Xaml.Media.IRevealBrush
    _classid_ = 'Windows.UI.Xaml.Media.RevealBrush'
    @winrt_commethod(39)
    def get_Color(self) -> Windows.UI.Color: ...
    @winrt_commethod(40)
    def put_Color(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(41)
    def get_TargetTheme(self) -> Windows.UI.Xaml.ApplicationTheme: ...
    @winrt_commethod(42)
    def put_TargetTheme(self, value: Windows.UI.Xaml.ApplicationTheme) -> Void: ...
    @winrt_commethod(43)
    def get_AlwaysUseFallback(self) -> Boolean: ...
    @winrt_commethod(44)
    def put_AlwaysUseFallback(self, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_ColorProperty(cls: Windows.UI.Xaml.Media.IRevealBrushStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TargetThemeProperty(cls: Windows.UI.Xaml.Media.IRevealBrushStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AlwaysUseFallbackProperty(cls: Windows.UI.Xaml.Media.IRevealBrushStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StateProperty(cls: Windows.UI.Xaml.Media.IRevealBrushStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def SetState(cls: Windows.UI.Xaml.Media.IRevealBrushStatics, element: Windows.UI.Xaml.UIElement, value: Windows.UI.Xaml.Media.RevealBrushState) -> Void: ...
    @winrt_classmethod
    def GetState(cls: Windows.UI.Xaml.Media.IRevealBrushStatics, element: Windows.UI.Xaml.UIElement) -> Windows.UI.Xaml.Media.RevealBrushState: ...
    Color = property(get_Color, put_Color)
    TargetTheme = property(get_TargetTheme, put_TargetTheme)
    AlwaysUseFallback = property(get_AlwaysUseFallback, put_AlwaysUseFallback)
    ColorProperty = property(get_ColorProperty, None)
    TargetThemeProperty = property(get_TargetThemeProperty, None)
    AlwaysUseFallbackProperty = property(get_AlwaysUseFallbackProperty, None)
    StateProperty = property(get_StateProperty, None)
RevealBrushState = Int32
RevealBrushState_Normal: RevealBrushState = 0
RevealBrushState_PointerOver: RevealBrushState = 1
RevealBrushState_Pressed: RevealBrushState = 2
class RotateTransform(ComPtr):
    extends: Windows.UI.Xaml.Media.Transform
    default_interface: Windows.UI.Xaml.Media.IRotateTransform
    _classid_ = 'Windows.UI.Xaml.Media.RotateTransform'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.RotateTransform: ...
    @winrt_mixinmethod
    def get_CenterX(self: Windows.UI.Xaml.Media.IRotateTransform) -> Double: ...
    @winrt_mixinmethod
    def put_CenterX(self: Windows.UI.Xaml.Media.IRotateTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_CenterY(self: Windows.UI.Xaml.Media.IRotateTransform) -> Double: ...
    @winrt_mixinmethod
    def put_CenterY(self: Windows.UI.Xaml.Media.IRotateTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Angle(self: Windows.UI.Xaml.Media.IRotateTransform) -> Double: ...
    @winrt_mixinmethod
    def put_Angle(self: Windows.UI.Xaml.Media.IRotateTransform, value: Double) -> Void: ...
    @winrt_classmethod
    def get_CenterXProperty(cls: Windows.UI.Xaml.Media.IRotateTransformStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CenterYProperty(cls: Windows.UI.Xaml.Media.IRotateTransformStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AngleProperty(cls: Windows.UI.Xaml.Media.IRotateTransformStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    CenterX = property(get_CenterX, put_CenterX)
    CenterY = property(get_CenterY, put_CenterY)
    Angle = property(get_Angle, put_Angle)
    CenterXProperty = property(get_CenterXProperty, None)
    CenterYProperty = property(get_CenterYProperty, None)
    AngleProperty = property(get_AngleProperty, None)
class ScaleTransform(ComPtr):
    extends: Windows.UI.Xaml.Media.Transform
    default_interface: Windows.UI.Xaml.Media.IScaleTransform
    _classid_ = 'Windows.UI.Xaml.Media.ScaleTransform'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.ScaleTransform: ...
    @winrt_mixinmethod
    def get_CenterX(self: Windows.UI.Xaml.Media.IScaleTransform) -> Double: ...
    @winrt_mixinmethod
    def put_CenterX(self: Windows.UI.Xaml.Media.IScaleTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_CenterY(self: Windows.UI.Xaml.Media.IScaleTransform) -> Double: ...
    @winrt_mixinmethod
    def put_CenterY(self: Windows.UI.Xaml.Media.IScaleTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleX(self: Windows.UI.Xaml.Media.IScaleTransform) -> Double: ...
    @winrt_mixinmethod
    def put_ScaleX(self: Windows.UI.Xaml.Media.IScaleTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleY(self: Windows.UI.Xaml.Media.IScaleTransform) -> Double: ...
    @winrt_mixinmethod
    def put_ScaleY(self: Windows.UI.Xaml.Media.IScaleTransform, value: Double) -> Void: ...
    @winrt_classmethod
    def get_CenterXProperty(cls: Windows.UI.Xaml.Media.IScaleTransformStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CenterYProperty(cls: Windows.UI.Xaml.Media.IScaleTransformStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ScaleXProperty(cls: Windows.UI.Xaml.Media.IScaleTransformStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ScaleYProperty(cls: Windows.UI.Xaml.Media.IScaleTransformStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    CenterX = property(get_CenterX, put_CenterX)
    CenterY = property(get_CenterY, put_CenterY)
    ScaleX = property(get_ScaleX, put_ScaleX)
    ScaleY = property(get_ScaleY, put_ScaleY)
    CenterXProperty = property(get_CenterXProperty, None)
    CenterYProperty = property(get_CenterYProperty, None)
    ScaleXProperty = property(get_ScaleXProperty, None)
    ScaleYProperty = property(get_ScaleYProperty, None)
class Shadow(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Media.IShadow
    _classid_ = 'Windows.UI.Xaml.Media.Shadow'
class SkewTransform(ComPtr):
    extends: Windows.UI.Xaml.Media.Transform
    default_interface: Windows.UI.Xaml.Media.ISkewTransform
    _classid_ = 'Windows.UI.Xaml.Media.SkewTransform'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.SkewTransform: ...
    @winrt_mixinmethod
    def get_CenterX(self: Windows.UI.Xaml.Media.ISkewTransform) -> Double: ...
    @winrt_mixinmethod
    def put_CenterX(self: Windows.UI.Xaml.Media.ISkewTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_CenterY(self: Windows.UI.Xaml.Media.ISkewTransform) -> Double: ...
    @winrt_mixinmethod
    def put_CenterY(self: Windows.UI.Xaml.Media.ISkewTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_AngleX(self: Windows.UI.Xaml.Media.ISkewTransform) -> Double: ...
    @winrt_mixinmethod
    def put_AngleX(self: Windows.UI.Xaml.Media.ISkewTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_AngleY(self: Windows.UI.Xaml.Media.ISkewTransform) -> Double: ...
    @winrt_mixinmethod
    def put_AngleY(self: Windows.UI.Xaml.Media.ISkewTransform, value: Double) -> Void: ...
    @winrt_classmethod
    def get_CenterXProperty(cls: Windows.UI.Xaml.Media.ISkewTransformStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CenterYProperty(cls: Windows.UI.Xaml.Media.ISkewTransformStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AngleXProperty(cls: Windows.UI.Xaml.Media.ISkewTransformStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AngleYProperty(cls: Windows.UI.Xaml.Media.ISkewTransformStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    CenterX = property(get_CenterX, put_CenterX)
    CenterY = property(get_CenterY, put_CenterY)
    AngleX = property(get_AngleX, put_AngleX)
    AngleY = property(get_AngleY, put_AngleY)
    CenterXProperty = property(get_CenterXProperty, None)
    CenterYProperty = property(get_CenterYProperty, None)
    AngleXProperty = property(get_AngleXProperty, None)
    AngleYProperty = property(get_AngleYProperty, None)
class SolidColorBrush(ComPtr):
    extends: Windows.UI.Xaml.Media.Brush
    default_interface: Windows.UI.Xaml.Media.ISolidColorBrush
    _classid_ = 'Windows.UI.Xaml.Media.SolidColorBrush'
    @winrt_factorymethod
    def CreateInstanceWithColor(cls: Windows.UI.Xaml.Media.ISolidColorBrushFactory, color: Windows.UI.Color) -> Windows.UI.Xaml.Media.SolidColorBrush: ...
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.SolidColorBrush: ...
    @winrt_mixinmethod
    def get_Color(self: Windows.UI.Xaml.Media.ISolidColorBrush) -> Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: Windows.UI.Xaml.Media.ISolidColorBrush, value: Windows.UI.Color) -> Void: ...
    @winrt_classmethod
    def get_ColorProperty(cls: Windows.UI.Xaml.Media.ISolidColorBrushStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Color = property(get_Color, put_Color)
    ColorProperty = property(get_ColorProperty, None)
Stereo3DVideoPackingMode = Int32
Stereo3DVideoPackingMode_None: Stereo3DVideoPackingMode = 0
Stereo3DVideoPackingMode_SideBySide: Stereo3DVideoPackingMode = 1
Stereo3DVideoPackingMode_TopBottom: Stereo3DVideoPackingMode = 2
Stereo3DVideoRenderMode = Int32
Stereo3DVideoRenderMode_Mono: Stereo3DVideoRenderMode = 0
Stereo3DVideoRenderMode_Stereo: Stereo3DVideoRenderMode = 1
Stretch = Int32
Stretch_None: Stretch = 0
Stretch_Fill: Stretch = 1
Stretch_Uniform: Stretch = 2
Stretch_UniformToFill: Stretch = 3
StyleSimulations = Int32
StyleSimulations_None: StyleSimulations = 0
StyleSimulations_BoldSimulation: StyleSimulations = 1
StyleSimulations_ItalicSimulation: StyleSimulations = 2
StyleSimulations_BoldItalicSimulation: StyleSimulations = 3
SweepDirection = Int32
SweepDirection_Counterclockwise: SweepDirection = 0
SweepDirection_Clockwise: SweepDirection = 1
class ThemeShadow(ComPtr):
    extends: Windows.UI.Xaml.Media.Shadow
    default_interface: Windows.UI.Xaml.Media.IThemeShadow
    _classid_ = 'Windows.UI.Xaml.Media.ThemeShadow'
    @winrt_commethod(8)
    def get_Receivers(self) -> Windows.UI.Xaml.UIElementWeakCollection: ...
    Receivers = property(get_Receivers, None)
class TileBrush(ComPtr):
    extends: Windows.UI.Xaml.Media.Brush
    default_interface: Windows.UI.Xaml.Media.ITileBrush
    _classid_ = 'Windows.UI.Xaml.Media.TileBrush'
    @winrt_commethod(28)
    def get_AlignmentX(self) -> Windows.UI.Xaml.Media.AlignmentX: ...
    @winrt_commethod(29)
    def put_AlignmentX(self, value: Windows.UI.Xaml.Media.AlignmentX) -> Void: ...
    @winrt_commethod(30)
    def get_AlignmentY(self) -> Windows.UI.Xaml.Media.AlignmentY: ...
    @winrt_commethod(31)
    def put_AlignmentY(self, value: Windows.UI.Xaml.Media.AlignmentY) -> Void: ...
    @winrt_commethod(32)
    def get_Stretch(self) -> Windows.UI.Xaml.Media.Stretch: ...
    @winrt_commethod(33)
    def put_Stretch(self, value: Windows.UI.Xaml.Media.Stretch) -> Void: ...
    @winrt_classmethod
    def get_AlignmentXProperty(cls: Windows.UI.Xaml.Media.ITileBrushStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AlignmentYProperty(cls: Windows.UI.Xaml.Media.ITileBrushStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StretchProperty(cls: Windows.UI.Xaml.Media.ITileBrushStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    AlignmentX = property(get_AlignmentX, put_AlignmentX)
    AlignmentY = property(get_AlignmentY, put_AlignmentY)
    Stretch = property(get_Stretch, put_Stretch)
    AlignmentXProperty = property(get_AlignmentXProperty, None)
    AlignmentYProperty = property(get_AlignmentYProperty, None)
    StretchProperty = property(get_StretchProperty, None)
class TimelineMarker(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Media.ITimelineMarker
    _classid_ = 'Windows.UI.Xaml.Media.TimelineMarker'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.TimelineMarker: ...
    @winrt_mixinmethod
    def get_Time(self: Windows.UI.Xaml.Media.ITimelineMarker) -> Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Time(self: Windows.UI.Xaml.Media.ITimelineMarker, value: Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_Type(self: Windows.UI.Xaml.Media.ITimelineMarker) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Type(self: Windows.UI.Xaml.Media.ITimelineMarker, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Text(self: Windows.UI.Xaml.Media.ITimelineMarker) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Text(self: Windows.UI.Xaml.Media.ITimelineMarker, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TimeProperty(cls: Windows.UI.Xaml.Media.ITimelineMarkerStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TypeProperty(cls: Windows.UI.Xaml.Media.ITimelineMarkerStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TextProperty(cls: Windows.UI.Xaml.Media.ITimelineMarkerStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Time = property(get_Time, put_Time)
    Type = property(get_Type, put_Type)
    Text = property(get_Text, put_Text)
    TimeProperty = property(get_TimeProperty, None)
    TypeProperty = property(get_TypeProperty, None)
    TextProperty = property(get_TextProperty, None)
class TimelineMarkerCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.TimelineMarker]
    _classid_ = 'Windows.UI.Xaml.Media.TimelineMarkerCollection'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.TimelineMarkerCollection: ...
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.TimelineMarker], index: UInt32) -> Windows.UI.Xaml.Media.TimelineMarker: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.TimelineMarker]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.TimelineMarker]) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Media.TimelineMarker]: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.TimelineMarker], value: Windows.UI.Xaml.Media.TimelineMarker, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.TimelineMarker], index: UInt32, value: Windows.UI.Xaml.Media.TimelineMarker) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.TimelineMarker], index: UInt32, value: Windows.UI.Xaml.Media.TimelineMarker) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.TimelineMarker], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.TimelineMarker], value: Windows.UI.Xaml.Media.TimelineMarker) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.TimelineMarker]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.TimelineMarker]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.TimelineMarker], startIndex: UInt32, items: POINTER(Windows.UI.Xaml.Media.TimelineMarker)) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.TimelineMarker], items: POINTER(Windows.UI.Xaml.Media.TimelineMarker)) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.Media.TimelineMarker]) -> Windows.Foundation.Collections.IIterator[Windows.UI.Xaml.Media.TimelineMarker]: ...
    Size = property(get_Size, None)
class TimelineMarkerRoutedEventArgs(ComPtr):
    extends: Windows.UI.Xaml.RoutedEventArgs
    default_interface: Windows.UI.Xaml.Media.ITimelineMarkerRoutedEventArgs
    _classid_ = 'Windows.UI.Xaml.Media.TimelineMarkerRoutedEventArgs'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.TimelineMarkerRoutedEventArgs: ...
    @winrt_mixinmethod
    def get_Marker(self: Windows.UI.Xaml.Media.ITimelineMarkerRoutedEventArgs) -> Windows.UI.Xaml.Media.TimelineMarker: ...
    @winrt_mixinmethod
    def put_Marker(self: Windows.UI.Xaml.Media.ITimelineMarkerRoutedEventArgs, value: Windows.UI.Xaml.Media.TimelineMarker) -> Void: ...
    Marker = property(get_Marker, put_Marker)
class TimelineMarkerRoutedEventHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _classid_ = 'Windows.UI.Xaml.Media.TimelineMarkerRoutedEventHandler'
    _iid_ = Guid('{72e2fa9c-6dea-4cbe-a159-06ce95fbeced}')
    @winrt_commethod(3)
    def Invoke(self, sender: Windows.Win32.System.WinRT.IInspectable_head, e: Windows.UI.Xaml.Media.TimelineMarkerRoutedEventArgs) -> Void: ...
class Transform(ComPtr):
    extends: Windows.UI.Xaml.Media.GeneralTransform
    default_interface: Windows.UI.Xaml.Media.ITransform
    _classid_ = 'Windows.UI.Xaml.Media.Transform'
class TransformCollection(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Transform]
    _classid_ = 'Windows.UI.Xaml.Media.TransformCollection'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.TransformCollection: ...
    @winrt_mixinmethod
    def GetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Transform], index: UInt32) -> Windows.UI.Xaml.Media.Transform: ...
    @winrt_mixinmethod
    def get_Size(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Transform]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Transform]) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Media.Transform]: ...
    @winrt_mixinmethod
    def IndexOf(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Transform], value: Windows.UI.Xaml.Media.Transform, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Transform], index: UInt32, value: Windows.UI.Xaml.Media.Transform) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Transform], index: UInt32, value: Windows.UI.Xaml.Media.Transform) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Transform], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Transform], value: Windows.UI.Xaml.Media.Transform) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Transform]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Transform]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Transform], startIndex: UInt32, items: POINTER(Windows.UI.Xaml.Media.Transform)) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: Windows.Foundation.Collections.IVector[Windows.UI.Xaml.Media.Transform], items: POINTER(Windows.UI.Xaml.Media.Transform)) -> Void: ...
    @winrt_mixinmethod
    def First(self: Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.Media.Transform]) -> Windows.Foundation.Collections.IIterator[Windows.UI.Xaml.Media.Transform]: ...
    Size = property(get_Size, None)
class TransformGroup(ComPtr):
    extends: Windows.UI.Xaml.Media.Transform
    default_interface: Windows.UI.Xaml.Media.ITransformGroup
    _classid_ = 'Windows.UI.Xaml.Media.TransformGroup'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.TransformGroup: ...
    @winrt_mixinmethod
    def get_Children(self: Windows.UI.Xaml.Media.ITransformGroup) -> Windows.UI.Xaml.Media.TransformCollection: ...
    @winrt_mixinmethod
    def put_Children(self: Windows.UI.Xaml.Media.ITransformGroup, value: Windows.UI.Xaml.Media.TransformCollection) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: Windows.UI.Xaml.Media.ITransformGroup) -> Windows.UI.Xaml.Media.Matrix: ...
    @winrt_classmethod
    def get_ChildrenProperty(cls: Windows.UI.Xaml.Media.ITransformGroupStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Children = property(get_Children, put_Children)
    Value = property(get_Value, None)
    ChildrenProperty = property(get_ChildrenProperty, None)
class TranslateTransform(ComPtr):
    extends: Windows.UI.Xaml.Media.Transform
    default_interface: Windows.UI.Xaml.Media.ITranslateTransform
    _classid_ = 'Windows.UI.Xaml.Media.TranslateTransform'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Media.TranslateTransform: ...
    @winrt_mixinmethod
    def get_X(self: Windows.UI.Xaml.Media.ITranslateTransform) -> Double: ...
    @winrt_mixinmethod
    def put_X(self: Windows.UI.Xaml.Media.ITranslateTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Y(self: Windows.UI.Xaml.Media.ITranslateTransform) -> Double: ...
    @winrt_mixinmethod
    def put_Y(self: Windows.UI.Xaml.Media.ITranslateTransform, value: Double) -> Void: ...
    @winrt_classmethod
    def get_XProperty(cls: Windows.UI.Xaml.Media.ITranslateTransformStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_YProperty(cls: Windows.UI.Xaml.Media.ITranslateTransformStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    X = property(get_X, put_X)
    Y = property(get_Y, put_Y)
    XProperty = property(get_XProperty, None)
    YProperty = property(get_YProperty, None)
class VisualTreeHelper(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    default_interface: Windows.UI.Xaml.Media.IVisualTreeHelper
    _classid_ = 'Windows.UI.Xaml.Media.VisualTreeHelper'
    @winrt_classmethod
    def GetOpenPopupsForXamlRoot(cls: Windows.UI.Xaml.Media.IVisualTreeHelperStatics3, xamlRoot: Windows.UI.Xaml.XamlRoot) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Controls.Primitives.Popup]: ...
    @winrt_classmethod
    def GetOpenPopups(cls: Windows.UI.Xaml.Media.IVisualTreeHelperStatics2, window: Windows.UI.Xaml.Window) -> Windows.Foundation.Collections.IVectorView[Windows.UI.Xaml.Controls.Primitives.Popup]: ...
    @winrt_classmethod
    def FindElementsInHostCoordinatesPoint(cls: Windows.UI.Xaml.Media.IVisualTreeHelperStatics, intersectingPoint: Windows.Foundation.Point, subtree: Windows.UI.Xaml.UIElement) -> Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.UIElement]: ...
    @winrt_classmethod
    def FindElementsInHostCoordinatesRect(cls: Windows.UI.Xaml.Media.IVisualTreeHelperStatics, intersectingRect: Windows.Foundation.Rect, subtree: Windows.UI.Xaml.UIElement) -> Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.UIElement]: ...
    @winrt_classmethod
    def FindAllElementsInHostCoordinatesPoint(cls: Windows.UI.Xaml.Media.IVisualTreeHelperStatics, intersectingPoint: Windows.Foundation.Point, subtree: Windows.UI.Xaml.UIElement, includeAllElements: Boolean) -> Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.UIElement]: ...
    @winrt_classmethod
    def FindAllElementsInHostCoordinatesRect(cls: Windows.UI.Xaml.Media.IVisualTreeHelperStatics, intersectingRect: Windows.Foundation.Rect, subtree: Windows.UI.Xaml.UIElement, includeAllElements: Boolean) -> Windows.Foundation.Collections.IIterable[Windows.UI.Xaml.UIElement]: ...
    @winrt_classmethod
    def GetChild(cls: Windows.UI.Xaml.Media.IVisualTreeHelperStatics, reference: Windows.UI.Xaml.DependencyObject, childIndex: Int32) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_classmethod
    def GetChildrenCount(cls: Windows.UI.Xaml.Media.IVisualTreeHelperStatics, reference: Windows.UI.Xaml.DependencyObject) -> Int32: ...
    @winrt_classmethod
    def GetParent(cls: Windows.UI.Xaml.Media.IVisualTreeHelperStatics, reference: Windows.UI.Xaml.DependencyObject) -> Windows.UI.Xaml.DependencyObject: ...
    @winrt_classmethod
    def DisconnectChildrenRecursive(cls: Windows.UI.Xaml.Media.IVisualTreeHelperStatics, element: Windows.UI.Xaml.UIElement) -> Void: ...
class XamlCompositionBrushBase(ComPtr):
    extends: Windows.UI.Xaml.Media.Brush
    default_interface: Windows.UI.Xaml.Media.IXamlCompositionBrushBase
    _classid_ = 'Windows.UI.Xaml.Media.XamlCompositionBrushBase'
    @winrt_commethod(26)
    def get_FallbackColor(self) -> Windows.UI.Color: ...
    @winrt_commethod(27)
    def put_FallbackColor(self, value: Windows.UI.Color) -> Void: ...
    @winrt_commethod(28)
    def get_CompositionBrush(self) -> Windows.UI.Composition.CompositionBrush: ...
    @winrt_commethod(29)
    def put_CompositionBrush(self, value: Windows.UI.Composition.CompositionBrush) -> Void: ...
    @winrt_commethod(30)
    def OnConnected(self) -> Void: ...
    @winrt_commethod(31)
    def OnDisconnected(self) -> Void: ...
    @winrt_classmethod
    def get_FallbackColorProperty(cls: Windows.UI.Xaml.Media.IXamlCompositionBrushBaseStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    FallbackColor = property(get_FallbackColor, put_FallbackColor)
    CompositionBrush = property(get_CompositionBrush, put_CompositionBrush)
    FallbackColorProperty = property(get_FallbackColorProperty, None)
class XamlLight(ComPtr):
    extends: Windows.UI.Xaml.DependencyObject
    default_interface: Windows.UI.Xaml.Media.IXamlLight
    _classid_ = 'Windows.UI.Xaml.Media.XamlLight'
    @winrt_commethod(16)
    def get_CompositionLight(self) -> Windows.UI.Composition.CompositionLight: ...
    @winrt_commethod(17)
    def put_CompositionLight(self, value: Windows.UI.Composition.CompositionLight) -> Void: ...
    @winrt_commethod(18)
    def GetId(self) -> WinRT_String: ...
    @winrt_commethod(19)
    def OnConnected(self, newElement: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(20)
    def OnDisconnected(self, oldElement: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_classmethod
    def AddTargetElement(cls: Windows.UI.Xaml.Media.IXamlLightStatics, lightId: WinRT_String, element: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_classmethod
    def RemoveTargetElement(cls: Windows.UI.Xaml.Media.IXamlLightStatics, lightId: WinRT_String, element: Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_classmethod
    def AddTargetBrush(cls: Windows.UI.Xaml.Media.IXamlLightStatics, lightId: WinRT_String, brush: Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_classmethod
    def RemoveTargetBrush(cls: Windows.UI.Xaml.Media.IXamlLightStatics, lightId: WinRT_String, brush: Windows.UI.Xaml.Media.Brush) -> Void: ...
    CompositionLight = property(get_CompositionLight, put_CompositionLight)
make_head(_module, 'AcrylicBrush')
make_head(_module, 'ArcSegment')
make_head(_module, 'BezierSegment')
make_head(_module, 'BitmapCache')
make_head(_module, 'Brush')
make_head(_module, 'BrushCollection')
make_head(_module, 'CacheMode')
make_head(_module, 'CompositeTransform')
make_head(_module, 'CompositionTarget')
make_head(_module, 'DoubleCollection')
make_head(_module, 'EllipseGeometry')
make_head(_module, 'FontFamily')
make_head(_module, 'GeneralTransform')
make_head(_module, 'Geometry')
make_head(_module, 'GeometryCollection')
make_head(_module, 'GeometryGroup')
make_head(_module, 'GradientBrush')
make_head(_module, 'GradientStop')
make_head(_module, 'GradientStopCollection')
make_head(_module, 'IAcrylicBrush')
make_head(_module, 'IAcrylicBrush2')
make_head(_module, 'IAcrylicBrushFactory')
make_head(_module, 'IAcrylicBrushStatics')
make_head(_module, 'IAcrylicBrushStatics2')
make_head(_module, 'IArcSegment')
make_head(_module, 'IArcSegmentStatics')
make_head(_module, 'IBezierSegment')
make_head(_module, 'IBezierSegmentStatics')
make_head(_module, 'IBitmapCache')
make_head(_module, 'IBrush')
make_head(_module, 'IBrushFactory')
make_head(_module, 'IBrushOverrides2')
make_head(_module, 'IBrushStatics')
make_head(_module, 'ICacheMode')
make_head(_module, 'ICacheModeFactory')
make_head(_module, 'ICompositeTransform')
make_head(_module, 'ICompositeTransformStatics')
make_head(_module, 'ICompositionTarget')
make_head(_module, 'ICompositionTargetStatics')
make_head(_module, 'ICompositionTargetStatics3')
make_head(_module, 'IEllipseGeometry')
make_head(_module, 'IEllipseGeometryStatics')
make_head(_module, 'IFontFamily')
make_head(_module, 'IFontFamilyFactory')
make_head(_module, 'IFontFamilyStatics2')
make_head(_module, 'IGeneralTransform')
make_head(_module, 'IGeneralTransformFactory')
make_head(_module, 'IGeneralTransformOverrides')
make_head(_module, 'IGeometry')
make_head(_module, 'IGeometryFactory')
make_head(_module, 'IGeometryGroup')
make_head(_module, 'IGeometryGroupStatics')
make_head(_module, 'IGeometryStatics')
make_head(_module, 'IGradientBrush')
make_head(_module, 'IGradientBrushFactory')
make_head(_module, 'IGradientBrushStatics')
make_head(_module, 'IGradientStop')
make_head(_module, 'IGradientStopStatics')
make_head(_module, 'IImageBrush')
make_head(_module, 'IImageBrushStatics')
make_head(_module, 'IImageSource')
make_head(_module, 'IImageSourceFactory')
make_head(_module, 'ILineGeometry')
make_head(_module, 'ILineGeometryStatics')
make_head(_module, 'ILineSegment')
make_head(_module, 'ILineSegmentStatics')
make_head(_module, 'ILinearGradientBrush')
make_head(_module, 'ILinearGradientBrushFactory')
make_head(_module, 'ILinearGradientBrushStatics')
make_head(_module, 'ILoadedImageSourceLoadCompletedEventArgs')
make_head(_module, 'ILoadedImageSurface')
make_head(_module, 'ILoadedImageSurfaceStatics')
make_head(_module, 'IMatrix3DProjection')
make_head(_module, 'IMatrix3DProjectionStatics')
make_head(_module, 'IMatrixHelper')
make_head(_module, 'IMatrixHelperStatics')
make_head(_module, 'IMatrixTransform')
make_head(_module, 'IMatrixTransformStatics')
make_head(_module, 'IMediaTransportControlsThumbnailRequestedEventArgs')
make_head(_module, 'IPartialMediaFailureDetectedEventArgs')
make_head(_module, 'IPartialMediaFailureDetectedEventArgs2')
make_head(_module, 'IPathFigure')
make_head(_module, 'IPathFigureStatics')
make_head(_module, 'IPathGeometry')
make_head(_module, 'IPathGeometryStatics')
make_head(_module, 'IPathSegment')
make_head(_module, 'IPathSegmentFactory')
make_head(_module, 'IPlaneProjection')
make_head(_module, 'IPlaneProjectionStatics')
make_head(_module, 'IPolyBezierSegment')
make_head(_module, 'IPolyBezierSegmentStatics')
make_head(_module, 'IPolyLineSegment')
make_head(_module, 'IPolyLineSegmentStatics')
make_head(_module, 'IPolyQuadraticBezierSegment')
make_head(_module, 'IPolyQuadraticBezierSegmentStatics')
make_head(_module, 'IProjection')
make_head(_module, 'IProjectionFactory')
make_head(_module, 'IQuadraticBezierSegment')
make_head(_module, 'IQuadraticBezierSegmentStatics')
make_head(_module, 'IRateChangedRoutedEventArgs')
make_head(_module, 'IRectangleGeometry')
make_head(_module, 'IRectangleGeometryStatics')
make_head(_module, 'IRenderedEventArgs')
make_head(_module, 'IRenderingEventArgs')
make_head(_module, 'IRevealBackgroundBrush')
make_head(_module, 'IRevealBackgroundBrushFactory')
make_head(_module, 'IRevealBorderBrush')
make_head(_module, 'IRevealBorderBrushFactory')
make_head(_module, 'IRevealBrush')
make_head(_module, 'IRevealBrushFactory')
make_head(_module, 'IRevealBrushStatics')
make_head(_module, 'IRotateTransform')
make_head(_module, 'IRotateTransformStatics')
make_head(_module, 'IScaleTransform')
make_head(_module, 'IScaleTransformStatics')
make_head(_module, 'IShadow')
make_head(_module, 'IShadowFactory')
make_head(_module, 'ISkewTransform')
make_head(_module, 'ISkewTransformStatics')
make_head(_module, 'ISolidColorBrush')
make_head(_module, 'ISolidColorBrushFactory')
make_head(_module, 'ISolidColorBrushStatics')
make_head(_module, 'IThemeShadow')
make_head(_module, 'IThemeShadowFactory')
make_head(_module, 'ITileBrush')
make_head(_module, 'ITileBrushFactory')
make_head(_module, 'ITileBrushStatics')
make_head(_module, 'ITimelineMarker')
make_head(_module, 'ITimelineMarkerRoutedEventArgs')
make_head(_module, 'ITimelineMarkerStatics')
make_head(_module, 'ITransform')
make_head(_module, 'ITransformFactory')
make_head(_module, 'ITransformGroup')
make_head(_module, 'ITransformGroupStatics')
make_head(_module, 'ITranslateTransform')
make_head(_module, 'ITranslateTransformStatics')
make_head(_module, 'IVisualTreeHelper')
make_head(_module, 'IVisualTreeHelperStatics')
make_head(_module, 'IVisualTreeHelperStatics2')
make_head(_module, 'IVisualTreeHelperStatics3')
make_head(_module, 'IXamlCompositionBrushBase')
make_head(_module, 'IXamlCompositionBrushBaseFactory')
make_head(_module, 'IXamlCompositionBrushBaseOverrides')
make_head(_module, 'IXamlCompositionBrushBaseProtected')
make_head(_module, 'IXamlCompositionBrushBaseStatics')
make_head(_module, 'IXamlLight')
make_head(_module, 'IXamlLightFactory')
make_head(_module, 'IXamlLightOverrides')
make_head(_module, 'IXamlLightProtected')
make_head(_module, 'IXamlLightStatics')
make_head(_module, 'ImageBrush')
make_head(_module, 'ImageSource')
make_head(_module, 'LineGeometry')
make_head(_module, 'LineSegment')
make_head(_module, 'LinearGradientBrush')
make_head(_module, 'LoadedImageSourceLoadCompletedEventArgs')
make_head(_module, 'LoadedImageSurface')
make_head(_module, 'Matrix')
make_head(_module, 'Matrix3DProjection')
make_head(_module, 'MatrixHelper')
make_head(_module, 'MatrixTransform')
make_head(_module, 'MediaTransportControlsThumbnailRequestedEventArgs')
make_head(_module, 'PartialMediaFailureDetectedEventArgs')
make_head(_module, 'PathFigure')
make_head(_module, 'PathFigureCollection')
make_head(_module, 'PathGeometry')
make_head(_module, 'PathSegment')
make_head(_module, 'PathSegmentCollection')
make_head(_module, 'PlaneProjection')
make_head(_module, 'PointCollection')
make_head(_module, 'PolyBezierSegment')
make_head(_module, 'PolyLineSegment')
make_head(_module, 'PolyQuadraticBezierSegment')
make_head(_module, 'Projection')
make_head(_module, 'QuadraticBezierSegment')
make_head(_module, 'RateChangedRoutedEventArgs')
make_head(_module, 'RateChangedRoutedEventHandler')
make_head(_module, 'RectangleGeometry')
make_head(_module, 'RenderedEventArgs')
make_head(_module, 'RenderingEventArgs')
make_head(_module, 'RevealBackgroundBrush')
make_head(_module, 'RevealBorderBrush')
make_head(_module, 'RevealBrush')
make_head(_module, 'RotateTransform')
make_head(_module, 'ScaleTransform')
make_head(_module, 'Shadow')
make_head(_module, 'SkewTransform')
make_head(_module, 'SolidColorBrush')
make_head(_module, 'ThemeShadow')
make_head(_module, 'TileBrush')
make_head(_module, 'TimelineMarker')
make_head(_module, 'TimelineMarkerCollection')
make_head(_module, 'TimelineMarkerRoutedEventArgs')
make_head(_module, 'TimelineMarkerRoutedEventHandler')
make_head(_module, 'Transform')
make_head(_module, 'TransformCollection')
make_head(_module, 'TransformGroup')
make_head(_module, 'TranslateTransform')
make_head(_module, 'VisualTreeHelper')
make_head(_module, 'XamlCompositionBrushBase')
make_head(_module, 'XamlLight')
