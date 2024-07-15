from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.UI.Composition
import win32more.Microsoft.UI.Composition.SystemBackdrops
import win32more.Microsoft.UI.Xaml
import win32more.Microsoft.UI.Xaml.Controls.Primitives
import win32more.Microsoft.UI.Xaml.Media
import win32more.Microsoft.UI.Xaml.Media.Media3D
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage.Streams
import win32more.Windows.UI
import win32more.Windows.Win32.System.WinRT
class _AcrylicBrush_Meta_(ComPtr.__class__):
    pass
class AcrylicBrush(ComPtr, metaclass=_AcrylicBrush_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.XamlCompositionBrushBase
    default_interface: win32more.Microsoft.UI.Xaml.Media.IAcrylicBrush
    _classid_ = 'Microsoft.UI.Xaml.Media.AcrylicBrush'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.AcrylicBrush.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Media.IAcrylicBrushFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.AcrylicBrush: ...
    @winrt_mixinmethod
    def get_TintColor(self: win32more.Microsoft.UI.Xaml.Media.IAcrylicBrush) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_TintColor(self: win32more.Microsoft.UI.Xaml.Media.IAcrylicBrush, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_TintOpacity(self: win32more.Microsoft.UI.Xaml.Media.IAcrylicBrush) -> Double: ...
    @winrt_mixinmethod
    def put_TintOpacity(self: win32more.Microsoft.UI.Xaml.Media.IAcrylicBrush, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_TintTransitionDuration(self: win32more.Microsoft.UI.Xaml.Media.IAcrylicBrush) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_TintTransitionDuration(self: win32more.Microsoft.UI.Xaml.Media.IAcrylicBrush, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_AlwaysUseFallback(self: win32more.Microsoft.UI.Xaml.Media.IAcrylicBrush) -> Boolean: ...
    @winrt_mixinmethod
    def put_AlwaysUseFallback(self: win32more.Microsoft.UI.Xaml.Media.IAcrylicBrush, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_TintLuminosityOpacity(self: win32more.Microsoft.UI.Xaml.Media.IAcrylicBrush2) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def put_TintLuminosityOpacity(self: win32more.Microsoft.UI.Xaml.Media.IAcrylicBrush2, value: win32more.Windows.Foundation.IReference[Double]) -> Void: ...
    @winrt_classmethod
    def get_TintLuminosityOpacityProperty(cls: win32more.Microsoft.UI.Xaml.Media.IAcrylicBrushStatics2) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TintColorProperty(cls: win32more.Microsoft.UI.Xaml.Media.IAcrylicBrushStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TintOpacityProperty(cls: win32more.Microsoft.UI.Xaml.Media.IAcrylicBrushStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TintTransitionDurationProperty(cls: win32more.Microsoft.UI.Xaml.Media.IAcrylicBrushStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AlwaysUseFallbackProperty(cls: win32more.Microsoft.UI.Xaml.Media.IAcrylicBrushStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    AlwaysUseFallback = property(get_AlwaysUseFallback, put_AlwaysUseFallback)
    TintColor = property(get_TintColor, put_TintColor)
    TintLuminosityOpacity = property(get_TintLuminosityOpacity, put_TintLuminosityOpacity)
    TintOpacity = property(get_TintOpacity, put_TintOpacity)
    TintTransitionDuration = property(get_TintTransitionDuration, put_TintTransitionDuration)
    _AcrylicBrush_Meta_.AlwaysUseFallbackProperty = property(get_AlwaysUseFallbackProperty, None)
    _AcrylicBrush_Meta_.TintColorProperty = property(get_TintColorProperty, None)
    _AcrylicBrush_Meta_.TintLuminosityOpacityProperty = property(get_TintLuminosityOpacityProperty, None)
    _AcrylicBrush_Meta_.TintOpacityProperty = property(get_TintOpacityProperty, None)
    _AcrylicBrush_Meta_.TintTransitionDurationProperty = property(get_TintTransitionDurationProperty, None)
class AlignmentX(Enum, Int32):
    Left = 0
    Center = 1
    Right = 2
class AlignmentY(Enum, Int32):
    Top = 0
    Center = 1
    Bottom = 2
class _ArcSegment_Meta_(ComPtr.__class__):
    pass
class ArcSegment(ComPtr, metaclass=_ArcSegment_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.PathSegment
    default_interface: win32more.Microsoft.UI.Xaml.Media.IArcSegment
    _classid_ = 'Microsoft.UI.Xaml.Media.ArcSegment'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.ArcSegment.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.ArcSegment: ...
    @winrt_mixinmethod
    def get_Point(self: win32more.Microsoft.UI.Xaml.Media.IArcSegment) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Point(self: win32more.Microsoft.UI.Xaml.Media.IArcSegment, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Microsoft.UI.Xaml.Media.IArcSegment) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def put_Size(self: win32more.Microsoft.UI.Xaml.Media.IArcSegment, value: win32more.Windows.Foundation.Size) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAngle(self: win32more.Microsoft.UI.Xaml.Media.IArcSegment) -> Double: ...
    @winrt_mixinmethod
    def put_RotationAngle(self: win32more.Microsoft.UI.Xaml.Media.IArcSegment, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_IsLargeArc(self: win32more.Microsoft.UI.Xaml.Media.IArcSegment) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsLargeArc(self: win32more.Microsoft.UI.Xaml.Media.IArcSegment, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SweepDirection(self: win32more.Microsoft.UI.Xaml.Media.IArcSegment) -> win32more.Microsoft.UI.Xaml.Media.SweepDirection: ...
    @winrt_mixinmethod
    def put_SweepDirection(self: win32more.Microsoft.UI.Xaml.Media.IArcSegment, value: win32more.Microsoft.UI.Xaml.Media.SweepDirection) -> Void: ...
    @winrt_classmethod
    def get_PointProperty(cls: win32more.Microsoft.UI.Xaml.Media.IArcSegmentStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SizeProperty(cls: win32more.Microsoft.UI.Xaml.Media.IArcSegmentStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RotationAngleProperty(cls: win32more.Microsoft.UI.Xaml.Media.IArcSegmentStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsLargeArcProperty(cls: win32more.Microsoft.UI.Xaml.Media.IArcSegmentStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SweepDirectionProperty(cls: win32more.Microsoft.UI.Xaml.Media.IArcSegmentStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    IsLargeArc = property(get_IsLargeArc, put_IsLargeArc)
    Point = property(get_Point, put_Point)
    RotationAngle = property(get_RotationAngle, put_RotationAngle)
    Size = property(get_Size, put_Size)
    SweepDirection = property(get_SweepDirection, put_SweepDirection)
    _ArcSegment_Meta_.IsLargeArcProperty = property(get_IsLargeArcProperty, None)
    _ArcSegment_Meta_.PointProperty = property(get_PointProperty, None)
    _ArcSegment_Meta_.RotationAngleProperty = property(get_RotationAngleProperty, None)
    _ArcSegment_Meta_.SizeProperty = property(get_SizeProperty, None)
    _ArcSegment_Meta_.SweepDirectionProperty = property(get_SweepDirectionProperty, None)
class _BezierSegment_Meta_(ComPtr.__class__):
    pass
class BezierSegment(ComPtr, metaclass=_BezierSegment_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.PathSegment
    default_interface: win32more.Microsoft.UI.Xaml.Media.IBezierSegment
    _classid_ = 'Microsoft.UI.Xaml.Media.BezierSegment'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.BezierSegment.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.BezierSegment: ...
    @winrt_mixinmethod
    def get_Point1(self: win32more.Microsoft.UI.Xaml.Media.IBezierSegment) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Point1(self: win32more.Microsoft.UI.Xaml.Media.IBezierSegment, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_Point2(self: win32more.Microsoft.UI.Xaml.Media.IBezierSegment) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Point2(self: win32more.Microsoft.UI.Xaml.Media.IBezierSegment, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_Point3(self: win32more.Microsoft.UI.Xaml.Media.IBezierSegment) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Point3(self: win32more.Microsoft.UI.Xaml.Media.IBezierSegment, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_classmethod
    def get_Point1Property(cls: win32more.Microsoft.UI.Xaml.Media.IBezierSegmentStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_Point2Property(cls: win32more.Microsoft.UI.Xaml.Media.IBezierSegmentStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_Point3Property(cls: win32more.Microsoft.UI.Xaml.Media.IBezierSegmentStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Point1 = property(get_Point1, put_Point1)
    Point2 = property(get_Point2, put_Point2)
    Point3 = property(get_Point3, put_Point3)
    _BezierSegment_Meta_.Point1Property = property(get_Point1Property, None)
    _BezierSegment_Meta_.Point2Property = property(get_Point2Property, None)
    _BezierSegment_Meta_.Point3Property = property(get_Point3Property, None)
class BitmapCache(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Media.CacheMode
    default_interface: win32more.Microsoft.UI.Xaml.Media.IBitmapCache
    _classid_ = 'Microsoft.UI.Xaml.Media.BitmapCache'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.BitmapCache.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.BitmapCache: ...
class _Brush_Meta_(ComPtr.__class__):
    pass
class Brush(ComPtr, metaclass=_Brush_Meta_):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Media.IBrush
    _classid_ = 'Microsoft.UI.Xaml.Media.Brush'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Brush.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Media.IBrushFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def get_Opacity(self: win32more.Microsoft.UI.Xaml.Media.IBrush) -> Double: ...
    @winrt_mixinmethod
    def put_Opacity(self: win32more.Microsoft.UI.Xaml.Media.IBrush, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Transform(self: win32more.Microsoft.UI.Xaml.Media.IBrush) -> win32more.Microsoft.UI.Xaml.Media.Transform: ...
    @winrt_mixinmethod
    def put_Transform(self: win32more.Microsoft.UI.Xaml.Media.IBrush, value: win32more.Microsoft.UI.Xaml.Media.Transform) -> Void: ...
    @winrt_mixinmethod
    def get_RelativeTransform(self: win32more.Microsoft.UI.Xaml.Media.IBrush) -> win32more.Microsoft.UI.Xaml.Media.Transform: ...
    @winrt_mixinmethod
    def put_RelativeTransform(self: win32more.Microsoft.UI.Xaml.Media.IBrush, value: win32more.Microsoft.UI.Xaml.Media.Transform) -> Void: ...
    @winrt_mixinmethod
    def PopulatePropertyInfoOverride(self: win32more.Microsoft.UI.Xaml.Media.IBrushOverrides, propertyName: WinRT_String, animationPropertyInfo: win32more.Microsoft.UI.Composition.AnimationPropertyInfo) -> Void: ...
    @winrt_mixinmethod
    def PopulatePropertyInfo(self: win32more.Microsoft.UI.Composition.IAnimationObject, propertyName: WinRT_String, propertyInfo: win32more.Microsoft.UI.Composition.AnimationPropertyInfo) -> Void: ...
    @winrt_classmethod
    def get_OpacityProperty(cls: win32more.Microsoft.UI.Xaml.Media.IBrushStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TransformProperty(cls: win32more.Microsoft.UI.Xaml.Media.IBrushStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RelativeTransformProperty(cls: win32more.Microsoft.UI.Xaml.Media.IBrushStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Opacity = property(get_Opacity, put_Opacity)
    RelativeTransform = property(get_RelativeTransform, put_RelativeTransform)
    Transform = property(get_Transform, put_Transform)
    _Brush_Meta_.OpacityProperty = property(get_OpacityProperty, None)
    _Brush_Meta_.RelativeTransformProperty = property(get_RelativeTransformProperty, None)
    _Brush_Meta_.TransformProperty = property(get_TransformProperty, None)
class BrushCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Microsoft.UI.Xaml.Media.Brush]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Brush]
    _classid_ = 'Microsoft.UI.Xaml.Media.BrushCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.BrushCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.BrushCollection: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Brush], index: UInt32) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Brush]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Brush]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.UI.Xaml.Media.Brush]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Brush], value: win32more.Microsoft.UI.Xaml.Media.Brush, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Brush], index: UInt32, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Brush], index: UInt32, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Brush], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Brush], value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Brush]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Brush]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Brush], startIndex: UInt32, items: FillArray[win32more.Microsoft.UI.Xaml.Media.Brush]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Brush], items: PassArray[win32more.Microsoft.UI.Xaml.Media.Brush]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Xaml.Media.Brush]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Microsoft.UI.Xaml.Media.Brush]: ...
    Size = property(get_Size, None)
class BrushMappingMode(Enum, Int32):
    Absolute = 0
    RelativeToBoundingBox = 1
class CacheMode(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Media.ICacheMode
    _classid_ = 'Microsoft.UI.Xaml.Media.CacheMode'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.CacheMode.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Media.ICacheModeFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.CacheMode: ...
class ColorInterpolationMode(Enum, Int32):
    ScRgbLinearInterpolation = 0
    SRgbLinearInterpolation = 1
class _CompositeTransform_Meta_(ComPtr.__class__):
    pass
class CompositeTransform(ComPtr, metaclass=_CompositeTransform_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Transform
    default_interface: win32more.Microsoft.UI.Xaml.Media.ICompositeTransform
    _classid_ = 'Microsoft.UI.Xaml.Media.CompositeTransform'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.CompositeTransform.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.CompositeTransform: ...
    @winrt_mixinmethod
    def get_CenterX(self: win32more.Microsoft.UI.Xaml.Media.ICompositeTransform) -> Double: ...
    @winrt_mixinmethod
    def put_CenterX(self: win32more.Microsoft.UI.Xaml.Media.ICompositeTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_CenterY(self: win32more.Microsoft.UI.Xaml.Media.ICompositeTransform) -> Double: ...
    @winrt_mixinmethod
    def put_CenterY(self: win32more.Microsoft.UI.Xaml.Media.ICompositeTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleX(self: win32more.Microsoft.UI.Xaml.Media.ICompositeTransform) -> Double: ...
    @winrt_mixinmethod
    def put_ScaleX(self: win32more.Microsoft.UI.Xaml.Media.ICompositeTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleY(self: win32more.Microsoft.UI.Xaml.Media.ICompositeTransform) -> Double: ...
    @winrt_mixinmethod
    def put_ScaleY(self: win32more.Microsoft.UI.Xaml.Media.ICompositeTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_SkewX(self: win32more.Microsoft.UI.Xaml.Media.ICompositeTransform) -> Double: ...
    @winrt_mixinmethod
    def put_SkewX(self: win32more.Microsoft.UI.Xaml.Media.ICompositeTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_SkewY(self: win32more.Microsoft.UI.Xaml.Media.ICompositeTransform) -> Double: ...
    @winrt_mixinmethod
    def put_SkewY(self: win32more.Microsoft.UI.Xaml.Media.ICompositeTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Rotation(self: win32more.Microsoft.UI.Xaml.Media.ICompositeTransform) -> Double: ...
    @winrt_mixinmethod
    def put_Rotation(self: win32more.Microsoft.UI.Xaml.Media.ICompositeTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_TranslateX(self: win32more.Microsoft.UI.Xaml.Media.ICompositeTransform) -> Double: ...
    @winrt_mixinmethod
    def put_TranslateX(self: win32more.Microsoft.UI.Xaml.Media.ICompositeTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_TranslateY(self: win32more.Microsoft.UI.Xaml.Media.ICompositeTransform) -> Double: ...
    @winrt_mixinmethod
    def put_TranslateY(self: win32more.Microsoft.UI.Xaml.Media.ICompositeTransform, value: Double) -> Void: ...
    @winrt_classmethod
    def get_CenterXProperty(cls: win32more.Microsoft.UI.Xaml.Media.ICompositeTransformStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CenterYProperty(cls: win32more.Microsoft.UI.Xaml.Media.ICompositeTransformStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ScaleXProperty(cls: win32more.Microsoft.UI.Xaml.Media.ICompositeTransformStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ScaleYProperty(cls: win32more.Microsoft.UI.Xaml.Media.ICompositeTransformStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SkewXProperty(cls: win32more.Microsoft.UI.Xaml.Media.ICompositeTransformStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SkewYProperty(cls: win32more.Microsoft.UI.Xaml.Media.ICompositeTransformStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RotationProperty(cls: win32more.Microsoft.UI.Xaml.Media.ICompositeTransformStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TranslateXProperty(cls: win32more.Microsoft.UI.Xaml.Media.ICompositeTransformStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TranslateYProperty(cls: win32more.Microsoft.UI.Xaml.Media.ICompositeTransformStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    CenterX = property(get_CenterX, put_CenterX)
    CenterY = property(get_CenterY, put_CenterY)
    Rotation = property(get_Rotation, put_Rotation)
    ScaleX = property(get_ScaleX, put_ScaleX)
    ScaleY = property(get_ScaleY, put_ScaleY)
    SkewX = property(get_SkewX, put_SkewX)
    SkewY = property(get_SkewY, put_SkewY)
    TranslateX = property(get_TranslateX, put_TranslateX)
    TranslateY = property(get_TranslateY, put_TranslateY)
    _CompositeTransform_Meta_.CenterXProperty = property(get_CenterXProperty, None)
    _CompositeTransform_Meta_.CenterYProperty = property(get_CenterYProperty, None)
    _CompositeTransform_Meta_.RotationProperty = property(get_RotationProperty, None)
    _CompositeTransform_Meta_.ScaleXProperty = property(get_ScaleXProperty, None)
    _CompositeTransform_Meta_.ScaleYProperty = property(get_ScaleYProperty, None)
    _CompositeTransform_Meta_.SkewXProperty = property(get_SkewXProperty, None)
    _CompositeTransform_Meta_.SkewYProperty = property(get_SkewYProperty, None)
    _CompositeTransform_Meta_.TranslateXProperty = property(get_TranslateXProperty, None)
    _CompositeTransform_Meta_.TranslateYProperty = property(get_TranslateYProperty, None)
class CompositionTarget(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Media.ICompositionTarget
    _classid_ = 'Microsoft.UI.Xaml.Media.CompositionTarget'
    @winrt_classmethod
    def add_Rendering(cls: win32more.Microsoft.UI.Xaml.Media.ICompositionTargetStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_Rendering(cls: win32more.Microsoft.UI.Xaml.Media.ICompositionTargetStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_Rendered(cls: win32more.Microsoft.UI.Xaml.Media.ICompositionTargetStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Microsoft.UI.Xaml.Media.RenderedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_Rendered(cls: win32more.Microsoft.UI.Xaml.Media.ICompositionTargetStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_SurfaceContentsLost(cls: win32more.Microsoft.UI.Xaml.Media.ICompositionTargetStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_SurfaceContentsLost(cls: win32more.Microsoft.UI.Xaml.Media.ICompositionTargetStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def GetCompositorForCurrentThread(cls: win32more.Microsoft.UI.Xaml.Media.ICompositionTargetStatics) -> win32more.Microsoft.UI.Composition.Compositor: ...
class DesktopAcrylicBackdrop(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Media.SystemBackdrop
    default_interface: win32more.Microsoft.UI.Xaml.Media.IDesktopAcrylicBackdrop
    _classid_ = 'Microsoft.UI.Xaml.Media.DesktopAcrylicBackdrop'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.DesktopAcrylicBackdrop.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Media.IDesktopAcrylicBackdropFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.DesktopAcrylicBackdrop: ...
class DoubleCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[Double]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[Double]
    _classid_ = 'Microsoft.UI.Xaml.Media.DoubleCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.DoubleCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.DoubleCollection: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[Double], index: UInt32) -> Double: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[Double]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[Double]) -> win32more.Windows.Foundation.Collections.IVectorView[Double]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[Double], value: Double, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[Double], index: UInt32, value: Double) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[Double], index: UInt32, value: Double) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[Double], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[Double], value: Double) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[Double]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[Double]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[Double], startIndex: UInt32, items: FillArray[Double]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[Double], items: PassArray[Double]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[Double]) -> win32more.Windows.Foundation.Collections.IIterator[Double]: ...
    Size = property(get_Size, None)
class ElementCompositeMode(Enum, Int32):
    Inherit = 0
    SourceOver = 1
    MinBlend = 2
class _EllipseGeometry_Meta_(ComPtr.__class__):
    pass
class EllipseGeometry(ComPtr, metaclass=_EllipseGeometry_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Geometry
    default_interface: win32more.Microsoft.UI.Xaml.Media.IEllipseGeometry
    _classid_ = 'Microsoft.UI.Xaml.Media.EllipseGeometry'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.EllipseGeometry.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.EllipseGeometry: ...
    @winrt_mixinmethod
    def get_Center(self: win32more.Microsoft.UI.Xaml.Media.IEllipseGeometry) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Center(self: win32more.Microsoft.UI.Xaml.Media.IEllipseGeometry, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_RadiusX(self: win32more.Microsoft.UI.Xaml.Media.IEllipseGeometry) -> Double: ...
    @winrt_mixinmethod
    def put_RadiusX(self: win32more.Microsoft.UI.Xaml.Media.IEllipseGeometry, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RadiusY(self: win32more.Microsoft.UI.Xaml.Media.IEllipseGeometry) -> Double: ...
    @winrt_mixinmethod
    def put_RadiusY(self: win32more.Microsoft.UI.Xaml.Media.IEllipseGeometry, value: Double) -> Void: ...
    @winrt_classmethod
    def get_CenterProperty(cls: win32more.Microsoft.UI.Xaml.Media.IEllipseGeometryStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RadiusXProperty(cls: win32more.Microsoft.UI.Xaml.Media.IEllipseGeometryStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RadiusYProperty(cls: win32more.Microsoft.UI.Xaml.Media.IEllipseGeometryStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Center = property(get_Center, put_Center)
    RadiusX = property(get_RadiusX, put_RadiusX)
    RadiusY = property(get_RadiusY, put_RadiusY)
    _EllipseGeometry_Meta_.CenterProperty = property(get_CenterProperty, None)
    _EllipseGeometry_Meta_.RadiusXProperty = property(get_RadiusXProperty, None)
    _EllipseGeometry_Meta_.RadiusYProperty = property(get_RadiusYProperty, None)
class FastPlayFallbackBehaviour(Enum, Int32):
    Skip = 0
    Hide = 1
    Disable = 2
class FillRule(Enum, Int32):
    EvenOdd = 0
    Nonzero = 1
class _FontFamily_Meta_(ComPtr.__class__):
    pass
class FontFamily(ComPtr, metaclass=_FontFamily_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Media.IFontFamily
    _classid_ = 'Microsoft.UI.Xaml.Media.FontFamily'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.FontFamily.CreateInstanceWithName(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithName(cls: win32more.Microsoft.UI.Xaml.Media.IFontFamilyFactory, familyName: WinRT_String, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.FontFamily: ...
    @winrt_mixinmethod
    def get_Source(self: win32more.Microsoft.UI.Xaml.Media.IFontFamily) -> WinRT_String: ...
    @winrt_classmethod
    def get_XamlAutoFontFamily(cls: win32more.Microsoft.UI.Xaml.Media.IFontFamilyStatics) -> win32more.Microsoft.UI.Xaml.Media.FontFamily: ...
    Source = property(get_Source, None)
    _FontFamily_Meta_.XamlAutoFontFamily = property(get_XamlAutoFontFamily, None)
class GeneralTransform(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Media.IGeneralTransform
    _classid_ = 'Microsoft.UI.Xaml.Media.GeneralTransform'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.GeneralTransform.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Media.IGeneralTransformFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.GeneralTransform: ...
    @winrt_mixinmethod
    def get_Inverse(self: win32more.Microsoft.UI.Xaml.Media.IGeneralTransform) -> win32more.Microsoft.UI.Xaml.Media.GeneralTransform: ...
    @winrt_mixinmethod
    def TransformPoint(self: win32more.Microsoft.UI.Xaml.Media.IGeneralTransform, point: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def TryTransform(self: win32more.Microsoft.UI.Xaml.Media.IGeneralTransform, inPoint: win32more.Windows.Foundation.Point, outPoint: POINTER(win32more.Windows.Foundation.Point)) -> Boolean: ...
    @winrt_mixinmethod
    def TransformBounds(self: win32more.Microsoft.UI.Xaml.Media.IGeneralTransform, rect: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_InverseCore(self: win32more.Microsoft.UI.Xaml.Media.IGeneralTransformOverrides) -> win32more.Microsoft.UI.Xaml.Media.GeneralTransform: ...
    @winrt_mixinmethod
    def TryTransformCore(self: win32more.Microsoft.UI.Xaml.Media.IGeneralTransformOverrides, inPoint: win32more.Windows.Foundation.Point, outPoint: POINTER(win32more.Windows.Foundation.Point)) -> Boolean: ...
    @winrt_mixinmethod
    def TransformBoundsCore(self: win32more.Microsoft.UI.Xaml.Media.IGeneralTransformOverrides, rect: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.Rect: ...
    Inverse = property(get_Inverse, None)
    InverseCore = property(get_InverseCore, None)
class _Geometry_Meta_(ComPtr.__class__):
    pass
class Geometry(ComPtr, metaclass=_Geometry_Meta_):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Media.IGeometry
    _classid_ = 'Microsoft.UI.Xaml.Media.Geometry'
    @winrt_mixinmethod
    def get_Transform(self: win32more.Microsoft.UI.Xaml.Media.IGeometry) -> win32more.Microsoft.UI.Xaml.Media.Transform: ...
    @winrt_mixinmethod
    def put_Transform(self: win32more.Microsoft.UI.Xaml.Media.IGeometry, value: win32more.Microsoft.UI.Xaml.Media.Transform) -> Void: ...
    @winrt_mixinmethod
    def get_Bounds(self: win32more.Microsoft.UI.Xaml.Media.IGeometry) -> win32more.Windows.Foundation.Rect: ...
    @winrt_classmethod
    def get_Empty(cls: win32more.Microsoft.UI.Xaml.Media.IGeometryStatics) -> win32more.Microsoft.UI.Xaml.Media.Geometry: ...
    @winrt_classmethod
    def get_StandardFlatteningTolerance(cls: win32more.Microsoft.UI.Xaml.Media.IGeometryStatics) -> Double: ...
    @winrt_classmethod
    def get_TransformProperty(cls: win32more.Microsoft.UI.Xaml.Media.IGeometryStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Bounds = property(get_Bounds, None)
    Transform = property(get_Transform, put_Transform)
    _Geometry_Meta_.Empty = property(get_Empty, None)
    _Geometry_Meta_.StandardFlatteningTolerance = property(get_StandardFlatteningTolerance, None)
    _Geometry_Meta_.TransformProperty = property(get_TransformProperty, None)
class GeometryCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Microsoft.UI.Xaml.Media.Geometry]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Geometry]
    _classid_ = 'Microsoft.UI.Xaml.Media.GeometryCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.GeometryCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.GeometryCollection: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Geometry], index: UInt32) -> win32more.Microsoft.UI.Xaml.Media.Geometry: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Geometry]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Geometry]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.UI.Xaml.Media.Geometry]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Geometry], value: win32more.Microsoft.UI.Xaml.Media.Geometry, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Geometry], index: UInt32, value: win32more.Microsoft.UI.Xaml.Media.Geometry) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Geometry], index: UInt32, value: win32more.Microsoft.UI.Xaml.Media.Geometry) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Geometry], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Geometry], value: win32more.Microsoft.UI.Xaml.Media.Geometry) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Geometry]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Geometry]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Geometry], startIndex: UInt32, items: FillArray[win32more.Microsoft.UI.Xaml.Media.Geometry]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Geometry], items: PassArray[win32more.Microsoft.UI.Xaml.Media.Geometry]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Xaml.Media.Geometry]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Microsoft.UI.Xaml.Media.Geometry]: ...
    Size = property(get_Size, None)
class _GeometryGroup_Meta_(ComPtr.__class__):
    pass
class GeometryGroup(ComPtr, metaclass=_GeometryGroup_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Geometry
    default_interface: win32more.Microsoft.UI.Xaml.Media.IGeometryGroup
    _classid_ = 'Microsoft.UI.Xaml.Media.GeometryGroup'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.GeometryGroup.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.GeometryGroup: ...
    @winrt_mixinmethod
    def get_FillRule(self: win32more.Microsoft.UI.Xaml.Media.IGeometryGroup) -> win32more.Microsoft.UI.Xaml.Media.FillRule: ...
    @winrt_mixinmethod
    def put_FillRule(self: win32more.Microsoft.UI.Xaml.Media.IGeometryGroup, value: win32more.Microsoft.UI.Xaml.Media.FillRule) -> Void: ...
    @winrt_mixinmethod
    def get_Children(self: win32more.Microsoft.UI.Xaml.Media.IGeometryGroup) -> win32more.Microsoft.UI.Xaml.Media.GeometryCollection: ...
    @winrt_mixinmethod
    def put_Children(self: win32more.Microsoft.UI.Xaml.Media.IGeometryGroup, value: win32more.Microsoft.UI.Xaml.Media.GeometryCollection) -> Void: ...
    @winrt_classmethod
    def get_FillRuleProperty(cls: win32more.Microsoft.UI.Xaml.Media.IGeometryGroupStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ChildrenProperty(cls: win32more.Microsoft.UI.Xaml.Media.IGeometryGroupStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Children = property(get_Children, put_Children)
    FillRule = property(get_FillRule, put_FillRule)
    _GeometryGroup_Meta_.ChildrenProperty = property(get_ChildrenProperty, None)
    _GeometryGroup_Meta_.FillRuleProperty = property(get_FillRuleProperty, None)
class _GradientBrush_Meta_(ComPtr.__class__):
    pass
class GradientBrush(ComPtr, metaclass=_GradientBrush_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Brush
    default_interface: win32more.Microsoft.UI.Xaml.Media.IGradientBrush
    _classid_ = 'Microsoft.UI.Xaml.Media.GradientBrush'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.GradientBrush.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Media.IGradientBrushFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.GradientBrush: ...
    @winrt_mixinmethod
    def get_SpreadMethod(self: win32more.Microsoft.UI.Xaml.Media.IGradientBrush) -> win32more.Microsoft.UI.Xaml.Media.GradientSpreadMethod: ...
    @winrt_mixinmethod
    def put_SpreadMethod(self: win32more.Microsoft.UI.Xaml.Media.IGradientBrush, value: win32more.Microsoft.UI.Xaml.Media.GradientSpreadMethod) -> Void: ...
    @winrt_mixinmethod
    def get_MappingMode(self: win32more.Microsoft.UI.Xaml.Media.IGradientBrush) -> win32more.Microsoft.UI.Xaml.Media.BrushMappingMode: ...
    @winrt_mixinmethod
    def put_MappingMode(self: win32more.Microsoft.UI.Xaml.Media.IGradientBrush, value: win32more.Microsoft.UI.Xaml.Media.BrushMappingMode) -> Void: ...
    @winrt_mixinmethod
    def get_ColorInterpolationMode(self: win32more.Microsoft.UI.Xaml.Media.IGradientBrush) -> win32more.Microsoft.UI.Xaml.Media.ColorInterpolationMode: ...
    @winrt_mixinmethod
    def put_ColorInterpolationMode(self: win32more.Microsoft.UI.Xaml.Media.IGradientBrush, value: win32more.Microsoft.UI.Xaml.Media.ColorInterpolationMode) -> Void: ...
    @winrt_mixinmethod
    def get_GradientStops(self: win32more.Microsoft.UI.Xaml.Media.IGradientBrush) -> win32more.Microsoft.UI.Xaml.Media.GradientStopCollection: ...
    @winrt_mixinmethod
    def put_GradientStops(self: win32more.Microsoft.UI.Xaml.Media.IGradientBrush, value: win32more.Microsoft.UI.Xaml.Media.GradientStopCollection) -> Void: ...
    @winrt_classmethod
    def get_SpreadMethodProperty(cls: win32more.Microsoft.UI.Xaml.Media.IGradientBrushStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MappingModeProperty(cls: win32more.Microsoft.UI.Xaml.Media.IGradientBrushStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ColorInterpolationModeProperty(cls: win32more.Microsoft.UI.Xaml.Media.IGradientBrushStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_GradientStopsProperty(cls: win32more.Microsoft.UI.Xaml.Media.IGradientBrushStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    ColorInterpolationMode = property(get_ColorInterpolationMode, put_ColorInterpolationMode)
    GradientStops = property(get_GradientStops, put_GradientStops)
    MappingMode = property(get_MappingMode, put_MappingMode)
    SpreadMethod = property(get_SpreadMethod, put_SpreadMethod)
    _GradientBrush_Meta_.ColorInterpolationModeProperty = property(get_ColorInterpolationModeProperty, None)
    _GradientBrush_Meta_.GradientStopsProperty = property(get_GradientStopsProperty, None)
    _GradientBrush_Meta_.MappingModeProperty = property(get_MappingModeProperty, None)
    _GradientBrush_Meta_.SpreadMethodProperty = property(get_SpreadMethodProperty, None)
class GradientSpreadMethod(Enum, Int32):
    Pad = 0
    Reflect = 1
    Repeat = 2
class _GradientStop_Meta_(ComPtr.__class__):
    pass
class GradientStop(ComPtr, metaclass=_GradientStop_Meta_):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Media.IGradientStop
    _classid_ = 'Microsoft.UI.Xaml.Media.GradientStop'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.GradientStop.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.GradientStop: ...
    @winrt_mixinmethod
    def get_Color(self: win32more.Microsoft.UI.Xaml.Media.IGradientStop) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: win32more.Microsoft.UI.Xaml.Media.IGradientStop, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_Offset(self: win32more.Microsoft.UI.Xaml.Media.IGradientStop) -> Double: ...
    @winrt_mixinmethod
    def put_Offset(self: win32more.Microsoft.UI.Xaml.Media.IGradientStop, value: Double) -> Void: ...
    @winrt_classmethod
    def get_ColorProperty(cls: win32more.Microsoft.UI.Xaml.Media.IGradientStopStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_OffsetProperty(cls: win32more.Microsoft.UI.Xaml.Media.IGradientStopStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Color = property(get_Color, put_Color)
    Offset = property(get_Offset, put_Offset)
    _GradientStop_Meta_.ColorProperty = property(get_ColorProperty, None)
    _GradientStop_Meta_.OffsetProperty = property(get_OffsetProperty, None)
class GradientStopCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Microsoft.UI.Xaml.Media.GradientStop]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.GradientStop]
    _classid_ = 'Microsoft.UI.Xaml.Media.GradientStopCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.GradientStopCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.GradientStopCollection: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.GradientStop], index: UInt32) -> win32more.Microsoft.UI.Xaml.Media.GradientStop: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.GradientStop]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.GradientStop]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.UI.Xaml.Media.GradientStop]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.GradientStop], value: win32more.Microsoft.UI.Xaml.Media.GradientStop, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.GradientStop], index: UInt32, value: win32more.Microsoft.UI.Xaml.Media.GradientStop) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.GradientStop], index: UInt32, value: win32more.Microsoft.UI.Xaml.Media.GradientStop) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.GradientStop], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.GradientStop], value: win32more.Microsoft.UI.Xaml.Media.GradientStop) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.GradientStop]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.GradientStop]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.GradientStop], startIndex: UInt32, items: FillArray[win32more.Microsoft.UI.Xaml.Media.GradientStop]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.GradientStop], items: PassArray[win32more.Microsoft.UI.Xaml.Media.GradientStop]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Xaml.Media.GradientStop]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Microsoft.UI.Xaml.Media.GradientStop]: ...
    Size = property(get_Size, None)
class IAcrylicBrush(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IAcrylicBrush'
    _iid_ = Guid('{3a8c760a-941f-58bc-a6d4-aa7a0dd1d036}')
    @winrt_commethod(6)
    def get_TintColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_TintColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(8)
    def get_TintOpacity(self) -> Double: ...
    @winrt_commethod(9)
    def put_TintOpacity(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_TintTransitionDuration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(11)
    def put_TintTransitionDuration(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(12)
    def get_AlwaysUseFallback(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_AlwaysUseFallback(self, value: Boolean) -> Void: ...
    AlwaysUseFallback = property(get_AlwaysUseFallback, put_AlwaysUseFallback)
    TintColor = property(get_TintColor, put_TintColor)
    TintOpacity = property(get_TintOpacity, put_TintOpacity)
    TintTransitionDuration = property(get_TintTransitionDuration, put_TintTransitionDuration)
class IAcrylicBrush2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IAcrylicBrush2'
    _iid_ = Guid('{23fad570-43ed-5a73-9de7-a303553d5414}')
    @winrt_commethod(6)
    def get_TintLuminosityOpacity(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(7)
    def put_TintLuminosityOpacity(self, value: win32more.Windows.Foundation.IReference[Double]) -> Void: ...
    TintLuminosityOpacity = property(get_TintLuminosityOpacity, put_TintLuminosityOpacity)
class IAcrylicBrushFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IAcrylicBrushFactory'
    _iid_ = Guid('{80173353-611d-5a02-8864-1aaa279dff1c}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.AcrylicBrush: ...
class IAcrylicBrushStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IAcrylicBrushStatics'
    _iid_ = Guid('{9d9d366b-00a3-5f3e-98b8-1df7fec1828c}')
    @winrt_commethod(6)
    def get_TintColorProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_TintOpacityProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_TintTransitionDurationProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_AlwaysUseFallbackProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    AlwaysUseFallbackProperty = property(get_AlwaysUseFallbackProperty, None)
    TintColorProperty = property(get_TintColorProperty, None)
    TintOpacityProperty = property(get_TintOpacityProperty, None)
    TintTransitionDurationProperty = property(get_TintTransitionDurationProperty, None)
class IAcrylicBrushStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IAcrylicBrushStatics2'
    _iid_ = Guid('{6e3eb0bd-20a1-52ea-aede-478061012279}')
    @winrt_commethod(6)
    def get_TintLuminosityOpacityProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    TintLuminosityOpacityProperty = property(get_TintLuminosityOpacityProperty, None)
class IArcSegment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IArcSegment'
    _iid_ = Guid('{6b7ce02b-87be-5acb-9d3b-c9964c6962d0}')
    @winrt_commethod(6)
    def get_Point(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def put_Point(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(8)
    def get_Size(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(9)
    def put_Size(self, value: win32more.Windows.Foundation.Size) -> Void: ...
    @winrt_commethod(10)
    def get_RotationAngle(self) -> Double: ...
    @winrt_commethod(11)
    def put_RotationAngle(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def get_IsLargeArc(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_IsLargeArc(self, value: Boolean) -> Void: ...
    @winrt_commethod(14)
    def get_SweepDirection(self) -> win32more.Microsoft.UI.Xaml.Media.SweepDirection: ...
    @winrt_commethod(15)
    def put_SweepDirection(self, value: win32more.Microsoft.UI.Xaml.Media.SweepDirection) -> Void: ...
    IsLargeArc = property(get_IsLargeArc, put_IsLargeArc)
    Point = property(get_Point, put_Point)
    RotationAngle = property(get_RotationAngle, put_RotationAngle)
    Size = property(get_Size, put_Size)
    SweepDirection = property(get_SweepDirection, put_SweepDirection)
class IArcSegmentStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IArcSegmentStatics'
    _iid_ = Guid('{5ba7ccb3-5bc7-5038-99c5-93dc730230cf}')
    @winrt_commethod(6)
    def get_PointProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_SizeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_RotationAngleProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_IsLargeArcProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_SweepDirectionProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    IsLargeArcProperty = property(get_IsLargeArcProperty, None)
    PointProperty = property(get_PointProperty, None)
    RotationAngleProperty = property(get_RotationAngleProperty, None)
    SizeProperty = property(get_SizeProperty, None)
    SweepDirectionProperty = property(get_SweepDirectionProperty, None)
class IBezierSegment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IBezierSegment'
    _iid_ = Guid('{0f36bade-892e-51fe-b94a-3875e86feaae}')
    @winrt_commethod(6)
    def get_Point1(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def put_Point1(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(8)
    def get_Point2(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(9)
    def put_Point2(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(10)
    def get_Point3(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(11)
    def put_Point3(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    Point1 = property(get_Point1, put_Point1)
    Point2 = property(get_Point2, put_Point2)
    Point3 = property(get_Point3, put_Point3)
class IBezierSegmentStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IBezierSegmentStatics'
    _iid_ = Guid('{98e74d5c-c97a-50b0-ae0e-d436dc9df16d}')
    @winrt_commethod(6)
    def get_Point1Property(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_Point2Property(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_Point3Property(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Point1Property = property(get_Point1Property, None)
    Point2Property = property(get_Point2Property, None)
    Point3Property = property(get_Point3Property, None)
class IBitmapCache(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IBitmapCache'
    _iid_ = Guid('{4b3a8983-27a2-592a-bda4-270431eae038}')
class IBrush(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IBrush'
    _iid_ = Guid('{2de3cb83-1329-5679-88f8-c822bc5442cb}')
    @winrt_commethod(6)
    def get_Opacity(self) -> Double: ...
    @winrt_commethod(7)
    def put_Opacity(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_Transform(self) -> win32more.Microsoft.UI.Xaml.Media.Transform: ...
    @winrt_commethod(9)
    def put_Transform(self, value: win32more.Microsoft.UI.Xaml.Media.Transform) -> Void: ...
    @winrt_commethod(10)
    def get_RelativeTransform(self) -> win32more.Microsoft.UI.Xaml.Media.Transform: ...
    @winrt_commethod(11)
    def put_RelativeTransform(self, value: win32more.Microsoft.UI.Xaml.Media.Transform) -> Void: ...
    Opacity = property(get_Opacity, put_Opacity)
    RelativeTransform = property(get_RelativeTransform, put_RelativeTransform)
    Transform = property(get_Transform, put_Transform)
class IBrushFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IBrushFactory'
    _iid_ = Guid('{b5258717-6c49-5ba5-87fd-35df382647a5}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
class IBrushOverrides(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IBrushOverrides'
    _iid_ = Guid('{b6b08394-bacf-53db-9ac7-be1c693e3513}')
    @winrt_commethod(6)
    def PopulatePropertyInfoOverride(self, propertyName: WinRT_String, animationPropertyInfo: win32more.Microsoft.UI.Composition.AnimationPropertyInfo) -> Void: ...
class IBrushStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IBrushStatics'
    _iid_ = Guid('{5b854f50-f818-5f01-91b0-28132d3f5957}')
    @winrt_commethod(6)
    def get_OpacityProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_TransformProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_RelativeTransformProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    OpacityProperty = property(get_OpacityProperty, None)
    RelativeTransformProperty = property(get_RelativeTransformProperty, None)
    TransformProperty = property(get_TransformProperty, None)
class ICacheMode(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ICacheMode'
    _iid_ = Guid('{2ff1a1cb-0f48-53fd-b1de-e2223dfb2ff6}')
class ICacheModeFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ICacheModeFactory'
    _iid_ = Guid('{e257811e-dcc5-51d8-829a-3e9400198a41}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.CacheMode: ...
class ICompositeTransform(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ICompositeTransform'
    _iid_ = Guid('{55c5f8f3-20e4-5b80-a046-ce4d0f62f2fe}')
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
    Rotation = property(get_Rotation, put_Rotation)
    ScaleX = property(get_ScaleX, put_ScaleX)
    ScaleY = property(get_ScaleY, put_ScaleY)
    SkewX = property(get_SkewX, put_SkewX)
    SkewY = property(get_SkewY, put_SkewY)
    TranslateX = property(get_TranslateX, put_TranslateX)
    TranslateY = property(get_TranslateY, put_TranslateY)
class ICompositeTransformStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ICompositeTransformStatics'
    _iid_ = Guid('{7701385b-8eab-5071-bfa5-b453e1e52b43}')
    @winrt_commethod(6)
    def get_CenterXProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_CenterYProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ScaleXProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_ScaleYProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_SkewXProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_SkewYProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_RotationProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_TranslateXProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_TranslateYProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    CenterXProperty = property(get_CenterXProperty, None)
    CenterYProperty = property(get_CenterYProperty, None)
    RotationProperty = property(get_RotationProperty, None)
    ScaleXProperty = property(get_ScaleXProperty, None)
    ScaleYProperty = property(get_ScaleYProperty, None)
    SkewXProperty = property(get_SkewXProperty, None)
    SkewYProperty = property(get_SkewYProperty, None)
    TranslateXProperty = property(get_TranslateXProperty, None)
    TranslateYProperty = property(get_TranslateYProperty, None)
class ICompositionTarget(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ICompositionTarget'
    _iid_ = Guid('{7d938324-e3ad-597c-93f6-520725410e68}')
class ICompositionTargetStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ICompositionTargetStatics'
    _iid_ = Guid('{12a4be6f-6db1-5165-b622-d57ab782745b}')
    @winrt_commethod(6)
    def add_Rendering(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Rendering(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_Rendered(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Microsoft.UI.Xaml.Media.RenderedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_Rendered(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_SurfaceContentsLost(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_SurfaceContentsLost(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(12)
    def GetCompositorForCurrentThread(self) -> win32more.Microsoft.UI.Composition.Compositor: ...
    Rendering = event()
    Rendered = event()
    SurfaceContentsLost = event()
class IDesktopAcrylicBackdrop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IDesktopAcrylicBackdrop'
    _iid_ = Guid('{bfd9915b-82a6-5df6-aff0-a4824ddc1143}')
class IDesktopAcrylicBackdropFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IDesktopAcrylicBackdropFactory'
    _iid_ = Guid('{00922e6d-ae51-564a-bce2-1973d5e463dd}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.DesktopAcrylicBackdrop: ...
class IEllipseGeometry(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IEllipseGeometry'
    _iid_ = Guid('{ababd262-d8e4-5b49-bce9-0108a5209d45}')
    @winrt_commethod(6)
    def get_Center(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def put_Center(self, value: win32more.Windows.Foundation.Point) -> Void: ...
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IEllipseGeometryStatics'
    _iid_ = Guid('{e8a33c80-d72f-5248-a71f-4b70a0757f89}')
    @winrt_commethod(6)
    def get_CenterProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_RadiusXProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_RadiusYProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    CenterProperty = property(get_CenterProperty, None)
    RadiusXProperty = property(get_RadiusXProperty, None)
    RadiusYProperty = property(get_RadiusYProperty, None)
class IFontFamily(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IFontFamily'
    _iid_ = Guid('{18fa5bc1-7294-527c-bb02-b213e0b3a2a3}')
    @winrt_commethod(6)
    def get_Source(self) -> WinRT_String: ...
    Source = property(get_Source, None)
class IFontFamilyFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IFontFamilyFactory'
    _iid_ = Guid('{61b88a77-d0f9-5e9e-8c28-eda01fede22e}')
    @winrt_commethod(6)
    def CreateInstanceWithName(self, familyName: WinRT_String, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.FontFamily: ...
class IFontFamilyStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IFontFamilyStatics'
    _iid_ = Guid('{b3eadceb-c471-58fe-93d0-d71b04a7fd54}')
    @winrt_commethod(6)
    def get_XamlAutoFontFamily(self) -> win32more.Microsoft.UI.Xaml.Media.FontFamily: ...
    XamlAutoFontFamily = property(get_XamlAutoFontFamily, None)
class IGeneralTransform(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IGeneralTransform'
    _iid_ = Guid('{04eedeeb-31e5-54c0-ae3f-8bd06645d339}')
    @winrt_commethod(6)
    def get_Inverse(self) -> win32more.Microsoft.UI.Xaml.Media.GeneralTransform: ...
    @winrt_commethod(7)
    def TransformPoint(self, point: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def TryTransform(self, inPoint: win32more.Windows.Foundation.Point, outPoint: POINTER(win32more.Windows.Foundation.Point)) -> Boolean: ...
    @winrt_commethod(9)
    def TransformBounds(self, rect: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.Rect: ...
    Inverse = property(get_Inverse, None)
class IGeneralTransformFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IGeneralTransformFactory'
    _iid_ = Guid('{2f1025a3-5391-5d1b-8382-3caaa1d26a96}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.GeneralTransform: ...
class IGeneralTransformOverrides(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IGeneralTransformOverrides'
    _iid_ = Guid('{ce8970f1-83f8-543f-9cf5-439c461601f1}')
    @winrt_commethod(6)
    def get_InverseCore(self) -> win32more.Microsoft.UI.Xaml.Media.GeneralTransform: ...
    @winrt_commethod(7)
    def TryTransformCore(self, inPoint: win32more.Windows.Foundation.Point, outPoint: POINTER(win32more.Windows.Foundation.Point)) -> Boolean: ...
    @winrt_commethod(8)
    def TransformBoundsCore(self, rect: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.Rect: ...
    InverseCore = property(get_InverseCore, None)
class IGeometry(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IGeometry'
    _iid_ = Guid('{dc102dcc-3be2-5414-8599-94b6e76ef39b}')
    @winrt_commethod(6)
    def get_Transform(self) -> win32more.Microsoft.UI.Xaml.Media.Transform: ...
    @winrt_commethod(7)
    def put_Transform(self, value: win32more.Microsoft.UI.Xaml.Media.Transform) -> Void: ...
    @winrt_commethod(8)
    def get_Bounds(self) -> win32more.Windows.Foundation.Rect: ...
    Bounds = property(get_Bounds, None)
    Transform = property(get_Transform, put_Transform)
class IGeometryFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IGeometryFactory'
    _iid_ = Guid('{4edcd536-7949-548a-a9b1-6ff03b951cf3}')
class IGeometryGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IGeometryGroup'
    _iid_ = Guid('{b4dde569-ea96-5883-914c-ebb7d818dd3a}')
    @winrt_commethod(6)
    def get_FillRule(self) -> win32more.Microsoft.UI.Xaml.Media.FillRule: ...
    @winrt_commethod(7)
    def put_FillRule(self, value: win32more.Microsoft.UI.Xaml.Media.FillRule) -> Void: ...
    @winrt_commethod(8)
    def get_Children(self) -> win32more.Microsoft.UI.Xaml.Media.GeometryCollection: ...
    @winrt_commethod(9)
    def put_Children(self, value: win32more.Microsoft.UI.Xaml.Media.GeometryCollection) -> Void: ...
    Children = property(get_Children, put_Children)
    FillRule = property(get_FillRule, put_FillRule)
class IGeometryGroupStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IGeometryGroupStatics'
    _iid_ = Guid('{56a23da5-d015-568a-9f8b-11b125cfd9b4}')
    @winrt_commethod(6)
    def get_FillRuleProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ChildrenProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    ChildrenProperty = property(get_ChildrenProperty, None)
    FillRuleProperty = property(get_FillRuleProperty, None)
class IGeometryStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IGeometryStatics'
    _iid_ = Guid('{349f78d0-4978-5742-b7d2-b34ea2c95600}')
    @winrt_commethod(6)
    def get_Empty(self) -> win32more.Microsoft.UI.Xaml.Media.Geometry: ...
    @winrt_commethod(7)
    def get_StandardFlatteningTolerance(self) -> Double: ...
    @winrt_commethod(8)
    def get_TransformProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Empty = property(get_Empty, None)
    StandardFlatteningTolerance = property(get_StandardFlatteningTolerance, None)
    TransformProperty = property(get_TransformProperty, None)
class IGradientBrush(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IGradientBrush'
    _iid_ = Guid('{77c347fa-c4c4-5174-a945-65cab3aa1c75}')
    @winrt_commethod(6)
    def get_SpreadMethod(self) -> win32more.Microsoft.UI.Xaml.Media.GradientSpreadMethod: ...
    @winrt_commethod(7)
    def put_SpreadMethod(self, value: win32more.Microsoft.UI.Xaml.Media.GradientSpreadMethod) -> Void: ...
    @winrt_commethod(8)
    def get_MappingMode(self) -> win32more.Microsoft.UI.Xaml.Media.BrushMappingMode: ...
    @winrt_commethod(9)
    def put_MappingMode(self, value: win32more.Microsoft.UI.Xaml.Media.BrushMappingMode) -> Void: ...
    @winrt_commethod(10)
    def get_ColorInterpolationMode(self) -> win32more.Microsoft.UI.Xaml.Media.ColorInterpolationMode: ...
    @winrt_commethod(11)
    def put_ColorInterpolationMode(self, value: win32more.Microsoft.UI.Xaml.Media.ColorInterpolationMode) -> Void: ...
    @winrt_commethod(12)
    def get_GradientStops(self) -> win32more.Microsoft.UI.Xaml.Media.GradientStopCollection: ...
    @winrt_commethod(13)
    def put_GradientStops(self, value: win32more.Microsoft.UI.Xaml.Media.GradientStopCollection) -> Void: ...
    ColorInterpolationMode = property(get_ColorInterpolationMode, put_ColorInterpolationMode)
    GradientStops = property(get_GradientStops, put_GradientStops)
    MappingMode = property(get_MappingMode, put_MappingMode)
    SpreadMethod = property(get_SpreadMethod, put_SpreadMethod)
class IGradientBrushFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IGradientBrushFactory'
    _iid_ = Guid('{64ff6177-1eda-565b-b7aa-ac50152e3136}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.GradientBrush: ...
class IGradientBrushStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IGradientBrushStatics'
    _iid_ = Guid('{4d3697d7-c6db-501c-8fa2-da30b8c8ca3b}')
    @winrt_commethod(6)
    def get_SpreadMethodProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_MappingModeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ColorInterpolationModeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_GradientStopsProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    ColorInterpolationModeProperty = property(get_ColorInterpolationModeProperty, None)
    GradientStopsProperty = property(get_GradientStopsProperty, None)
    MappingModeProperty = property(get_MappingModeProperty, None)
    SpreadMethodProperty = property(get_SpreadMethodProperty, None)
class IGradientStop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IGradientStop'
    _iid_ = Guid('{48bcb039-e8e1-5743-94c3-f766011d3b5d}')
    @winrt_commethod(6)
    def get_Color(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_Color(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(8)
    def get_Offset(self) -> Double: ...
    @winrt_commethod(9)
    def put_Offset(self, value: Double) -> Void: ...
    Color = property(get_Color, put_Color)
    Offset = property(get_Offset, put_Offset)
class IGradientStopStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IGradientStopStatics'
    _iid_ = Guid('{0b566c1b-37de-5bfd-b419-0f7c4c0a0523}')
    @winrt_commethod(6)
    def get_ColorProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_OffsetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    ColorProperty = property(get_ColorProperty, None)
    OffsetProperty = property(get_OffsetProperty, None)
class IImageBrush(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IImageBrush'
    _iid_ = Guid('{edcd91a3-a868-5ba6-9489-5b12b4c29d85}')
    @winrt_commethod(6)
    def get_ImageSource(self) -> win32more.Microsoft.UI.Xaml.Media.ImageSource: ...
    @winrt_commethod(7)
    def put_ImageSource(self, value: win32more.Microsoft.UI.Xaml.Media.ImageSource) -> Void: ...
    @winrt_commethod(8)
    def add_ImageFailed(self, handler: win32more.Microsoft.UI.Xaml.ExceptionRoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ImageFailed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_ImageOpened(self, handler: win32more.Microsoft.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ImageOpened(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ImageSource = property(get_ImageSource, put_ImageSource)
    ImageFailed = event()
    ImageOpened = event()
class IImageBrushStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IImageBrushStatics'
    _iid_ = Guid('{ce8082dc-a505-5b4f-8861-79630f52c189}')
    @winrt_commethod(6)
    def get_ImageSourceProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    ImageSourceProperty = property(get_ImageSourceProperty, None)
class IImageSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IImageSource'
    _iid_ = Guid('{6c2038f6-d6d5-55e9-9b9e-082f12dbff60}')
class IImageSourceFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IImageSourceFactory'
    _iid_ = Guid('{0b1e64a3-e353-5901-b84b-ae9842aea5cd}')
class ILineGeometry(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ILineGeometry'
    _iid_ = Guid('{467ef3c5-bc43-50ed-bb23-16be2c63356e}')
    @winrt_commethod(6)
    def get_StartPoint(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def put_StartPoint(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(8)
    def get_EndPoint(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(9)
    def put_EndPoint(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    EndPoint = property(get_EndPoint, put_EndPoint)
    StartPoint = property(get_StartPoint, put_StartPoint)
class ILineGeometryStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ILineGeometryStatics'
    _iid_ = Guid('{ce0ecbf3-9389-5304-b7c8-5e610902f258}')
    @winrt_commethod(6)
    def get_StartPointProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_EndPointProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    EndPointProperty = property(get_EndPointProperty, None)
    StartPointProperty = property(get_StartPointProperty, None)
class ILineSegment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ILineSegment'
    _iid_ = Guid('{0c618e54-d883-588c-8875-bd8dfd6a6a3e}')
    @winrt_commethod(6)
    def get_Point(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def put_Point(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    Point = property(get_Point, put_Point)
class ILineSegmentStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ILineSegmentStatics'
    _iid_ = Guid('{c3ec48a9-b9c0-561f-9925-d1d1b2a6bae6}')
    @winrt_commethod(6)
    def get_PointProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    PointProperty = property(get_PointProperty, None)
class ILinearGradientBrush(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ILinearGradientBrush'
    _iid_ = Guid('{c0ab9638-1bd9-5fa4-9649-48cfa12f0d1e}')
    @winrt_commethod(6)
    def get_StartPoint(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def put_StartPoint(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(8)
    def get_EndPoint(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(9)
    def put_EndPoint(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    EndPoint = property(get_EndPoint, put_EndPoint)
    StartPoint = property(get_StartPoint, put_StartPoint)
class ILinearGradientBrushFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ILinearGradientBrushFactory'
    _iid_ = Guid('{c0ba7de3-ccfd-534c-882f-3ab39ae723f3}')
    @winrt_commethod(6)
    def CreateInstanceWithGradientStopCollectionAndAngle(self, gradientStopCollection: win32more.Microsoft.UI.Xaml.Media.GradientStopCollection, angle: Double) -> win32more.Microsoft.UI.Xaml.Media.LinearGradientBrush: ...
class ILinearGradientBrushStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ILinearGradientBrushStatics'
    _iid_ = Guid('{df029e84-f6be-5b7e-ba22-3b4e7a6bceee}')
    @winrt_commethod(6)
    def get_StartPointProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_EndPointProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    EndPointProperty = property(get_EndPointProperty, None)
    StartPointProperty = property(get_StartPointProperty, None)
class ILoadedImageSourceLoadCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ILoadedImageSourceLoadCompletedEventArgs'
    _iid_ = Guid('{4121bb7c-48e8-542d-b950-3ea7e709c0d6}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Microsoft.UI.Xaml.Media.LoadedImageSourceLoadStatus: ...
    Status = property(get_Status, None)
class ILoadedImageSurface(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ILoadedImageSurface'
    _iid_ = Guid('{b5275540-1706-5851-95cc-498ee81fb183}')
    @winrt_commethod(6)
    def get_DecodedPhysicalSize(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(7)
    def get_DecodedSize(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(8)
    def get_NaturalSize(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(9)
    def add_LoadCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Media.LoadedImageSurface, win32more.Microsoft.UI.Xaml.Media.LoadedImageSourceLoadCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_LoadCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    DecodedPhysicalSize = property(get_DecodedPhysicalSize, None)
    DecodedSize = property(get_DecodedSize, None)
    NaturalSize = property(get_NaturalSize, None)
    LoadCompleted = event()
class ILoadedImageSurfaceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ILoadedImageSurfaceStatics'
    _iid_ = Guid('{25d390c4-4e32-52c2-868f-f2ede74ee442}')
    @winrt_commethod(6)
    def StartLoadFromUriWithSize(self, uri: win32more.Windows.Foundation.Uri, desiredMaxSize: win32more.Windows.Foundation.Size) -> win32more.Microsoft.UI.Xaml.Media.LoadedImageSurface: ...
    @winrt_commethod(7)
    def StartLoadFromUri(self, uri: win32more.Windows.Foundation.Uri) -> win32more.Microsoft.UI.Xaml.Media.LoadedImageSurface: ...
    @winrt_commethod(8)
    def StartLoadFromStreamWithSize(self, stream: win32more.Windows.Storage.Streams.IRandomAccessStream, desiredMaxSize: win32more.Windows.Foundation.Size) -> win32more.Microsoft.UI.Xaml.Media.LoadedImageSurface: ...
    @winrt_commethod(9)
    def StartLoadFromStream(self, stream: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Microsoft.UI.Xaml.Media.LoadedImageSurface: ...
class IMatrix3DProjection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IMatrix3DProjection'
    _iid_ = Guid('{fc3338ef-f390-5bb1-932e-3b7c08788187}')
    @winrt_commethod(6)
    def get_ProjectionMatrix(self) -> win32more.Microsoft.UI.Xaml.Media.Media3D.Matrix3D: ...
    @winrt_commethod(7)
    def put_ProjectionMatrix(self, value: win32more.Microsoft.UI.Xaml.Media.Media3D.Matrix3D) -> Void: ...
    ProjectionMatrix = property(get_ProjectionMatrix, put_ProjectionMatrix)
class IMatrix3DProjectionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IMatrix3DProjectionStatics'
    _iid_ = Guid('{a5a7e267-7a5d-58ef-a8cd-b88ebdf82207}')
    @winrt_commethod(6)
    def get_ProjectionMatrixProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    ProjectionMatrixProperty = property(get_ProjectionMatrixProperty, None)
class IMatrixHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IMatrixHelper'
    _iid_ = Guid('{9571fd76-cc5c-534d-ac85-cb4ac870c912}')
class IMatrixHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IMatrixHelperStatics'
    _iid_ = Guid('{5762cf6b-4fb0-532f-8368-de960042701f}')
    @winrt_commethod(6)
    def get_Identity(self) -> win32more.Microsoft.UI.Xaml.Media.Matrix: ...
    @winrt_commethod(7)
    def FromElements(self, m11: Double, m12: Double, m21: Double, m22: Double, offsetX: Double, offsetY: Double) -> win32more.Microsoft.UI.Xaml.Media.Matrix: ...
    @winrt_commethod(8)
    def GetIsIdentity(self, target: win32more.Microsoft.UI.Xaml.Media.Matrix) -> Boolean: ...
    @winrt_commethod(9)
    def Transform(self, target: win32more.Microsoft.UI.Xaml.Media.Matrix, point: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.Point: ...
    Identity = property(get_Identity, None)
class IMatrixTransform(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IMatrixTransform'
    _iid_ = Guid('{f03138e1-addd-59fa-b993-3ea69b888ace}')
    @winrt_commethod(6)
    def get_Matrix(self) -> win32more.Microsoft.UI.Xaml.Media.Matrix: ...
    @winrt_commethod(7)
    def put_Matrix(self, value: win32more.Microsoft.UI.Xaml.Media.Matrix) -> Void: ...
    Matrix = property(get_Matrix, put_Matrix)
class IMatrixTransformStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IMatrixTransformStatics'
    _iid_ = Guid('{d7db9de3-5071-5115-98fb-ccad2fd46e44}')
    @winrt_commethod(6)
    def get_MatrixProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    MatrixProperty = property(get_MatrixProperty, None)
class IMediaTransportControlsThumbnailRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IMediaTransportControlsThumbnailRequestedEventArgs'
    _iid_ = Guid('{fe0ffb86-74b0-5031-accc-b34d0382a637}')
    @winrt_commethod(6)
    def SetThumbnailImage(self, source: win32more.Windows.Storage.Streams.IInputStream) -> Void: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
class IMicaBackdrop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IMicaBackdrop'
    _iid_ = Guid('{c156a404-3dac-593a-b1f3-7a33c289dc83}')
    @winrt_commethod(6)
    def get_Kind(self) -> win32more.Microsoft.UI.Composition.SystemBackdrops.MicaKind: ...
    @winrt_commethod(7)
    def put_Kind(self, value: win32more.Microsoft.UI.Composition.SystemBackdrops.MicaKind) -> Void: ...
    Kind = property(get_Kind, put_Kind)
class IMicaBackdropFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IMicaBackdropFactory'
    _iid_ = Guid('{774379ce-74bd-59d4-849d-d99c4184d838}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.MicaBackdrop: ...
class IMicaBackdropStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IMicaBackdropStatics'
    _iid_ = Guid('{a63abdce-c796-5509-9f4d-072bc1e599f1}')
    @winrt_commethod(6)
    def get_KindProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    KindProperty = property(get_KindProperty, None)
class IPathFigure(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IPathFigure'
    _iid_ = Guid('{0ee00712-bf65-5f27-9c06-14abdf6656d7}')
    @winrt_commethod(6)
    def get_Segments(self) -> win32more.Microsoft.UI.Xaml.Media.PathSegmentCollection: ...
    @winrt_commethod(7)
    def put_Segments(self, value: win32more.Microsoft.UI.Xaml.Media.PathSegmentCollection) -> Void: ...
    @winrt_commethod(8)
    def get_StartPoint(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(9)
    def put_StartPoint(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(10)
    def get_IsClosed(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_IsClosed(self, value: Boolean) -> Void: ...
    @winrt_commethod(12)
    def get_IsFilled(self) -> Boolean: ...
    @winrt_commethod(13)
    def put_IsFilled(self, value: Boolean) -> Void: ...
    IsClosed = property(get_IsClosed, put_IsClosed)
    IsFilled = property(get_IsFilled, put_IsFilled)
    Segments = property(get_Segments, put_Segments)
    StartPoint = property(get_StartPoint, put_StartPoint)
class IPathFigureStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IPathFigureStatics'
    _iid_ = Guid('{93bc33c4-879a-5edb-b8d7-7ecb861a7314}')
    @winrt_commethod(6)
    def get_SegmentsProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_StartPointProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_IsClosedProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_IsFilledProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    IsClosedProperty = property(get_IsClosedProperty, None)
    IsFilledProperty = property(get_IsFilledProperty, None)
    SegmentsProperty = property(get_SegmentsProperty, None)
    StartPointProperty = property(get_StartPointProperty, None)
class IPathGeometry(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IPathGeometry'
    _iid_ = Guid('{11b9d95d-d3d9-5337-a05c-73a27a2b5124}')
    @winrt_commethod(6)
    def get_FillRule(self) -> win32more.Microsoft.UI.Xaml.Media.FillRule: ...
    @winrt_commethod(7)
    def put_FillRule(self, value: win32more.Microsoft.UI.Xaml.Media.FillRule) -> Void: ...
    @winrt_commethod(8)
    def get_Figures(self) -> win32more.Microsoft.UI.Xaml.Media.PathFigureCollection: ...
    @winrt_commethod(9)
    def put_Figures(self, value: win32more.Microsoft.UI.Xaml.Media.PathFigureCollection) -> Void: ...
    Figures = property(get_Figures, put_Figures)
    FillRule = property(get_FillRule, put_FillRule)
class IPathGeometryStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IPathGeometryStatics'
    _iid_ = Guid('{d7f408fe-6c3a-5cce-91cc-c5a95d4b345a}')
    @winrt_commethod(6)
    def get_FillRuleProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_FiguresProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    FiguresProperty = property(get_FiguresProperty, None)
    FillRuleProperty = property(get_FillRuleProperty, None)
class IPathSegment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IPathSegment'
    _iid_ = Guid('{b922ebbe-08f0-57e9-8785-7e57097f3bd4}')
class IPathSegmentFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IPathSegmentFactory'
    _iid_ = Guid('{0559a4ff-ac4b-5bb7-b541-d373960e083b}')
class IPlaneProjection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IPlaneProjection'
    _iid_ = Guid('{d3e22836-0322-5d75-941c-a5ffb05192b2}')
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
    def get_ProjectionMatrix(self) -> win32more.Microsoft.UI.Xaml.Media.Media3D.Matrix3D: ...
    CenterOfRotationX = property(get_CenterOfRotationX, put_CenterOfRotationX)
    CenterOfRotationY = property(get_CenterOfRotationY, put_CenterOfRotationY)
    CenterOfRotationZ = property(get_CenterOfRotationZ, put_CenterOfRotationZ)
    GlobalOffsetX = property(get_GlobalOffsetX, put_GlobalOffsetX)
    GlobalOffsetY = property(get_GlobalOffsetY, put_GlobalOffsetY)
    GlobalOffsetZ = property(get_GlobalOffsetZ, put_GlobalOffsetZ)
    LocalOffsetX = property(get_LocalOffsetX, put_LocalOffsetX)
    LocalOffsetY = property(get_LocalOffsetY, put_LocalOffsetY)
    LocalOffsetZ = property(get_LocalOffsetZ, put_LocalOffsetZ)
    ProjectionMatrix = property(get_ProjectionMatrix, None)
    RotationX = property(get_RotationX, put_RotationX)
    RotationY = property(get_RotationY, put_RotationY)
    RotationZ = property(get_RotationZ, put_RotationZ)
class IPlaneProjectionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IPlaneProjectionStatics'
    _iid_ = Guid('{96d86c18-90dd-564a-828a-8735e4219b1d}')
    @winrt_commethod(6)
    def get_LocalOffsetXProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_LocalOffsetYProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_LocalOffsetZProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_RotationXProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_RotationYProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_RotationZProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_CenterOfRotationXProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_CenterOfRotationYProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_CenterOfRotationZProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_GlobalOffsetXProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def get_GlobalOffsetYProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(17)
    def get_GlobalOffsetZProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(18)
    def get_ProjectionMatrixProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    CenterOfRotationXProperty = property(get_CenterOfRotationXProperty, None)
    CenterOfRotationYProperty = property(get_CenterOfRotationYProperty, None)
    CenterOfRotationZProperty = property(get_CenterOfRotationZProperty, None)
    GlobalOffsetXProperty = property(get_GlobalOffsetXProperty, None)
    GlobalOffsetYProperty = property(get_GlobalOffsetYProperty, None)
    GlobalOffsetZProperty = property(get_GlobalOffsetZProperty, None)
    LocalOffsetXProperty = property(get_LocalOffsetXProperty, None)
    LocalOffsetYProperty = property(get_LocalOffsetYProperty, None)
    LocalOffsetZProperty = property(get_LocalOffsetZProperty, None)
    ProjectionMatrixProperty = property(get_ProjectionMatrixProperty, None)
    RotationXProperty = property(get_RotationXProperty, None)
    RotationYProperty = property(get_RotationYProperty, None)
    RotationZProperty = property(get_RotationZProperty, None)
class IPolyBezierSegment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IPolyBezierSegment'
    _iid_ = Guid('{d7f760a0-b93a-562a-8118-6330ed22c307}')
    @winrt_commethod(6)
    def get_Points(self) -> win32more.Microsoft.UI.Xaml.Media.PointCollection: ...
    @winrt_commethod(7)
    def put_Points(self, value: win32more.Microsoft.UI.Xaml.Media.PointCollection) -> Void: ...
    Points = property(get_Points, put_Points)
class IPolyBezierSegmentStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IPolyBezierSegmentStatics'
    _iid_ = Guid('{738ef089-a80f-53e0-816f-f787a4461907}')
    @winrt_commethod(6)
    def get_PointsProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    PointsProperty = property(get_PointsProperty, None)
class IPolyLineSegment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IPolyLineSegment'
    _iid_ = Guid('{426ef287-0287-536f-ad9e-6a05ecbb323a}')
    @winrt_commethod(6)
    def get_Points(self) -> win32more.Microsoft.UI.Xaml.Media.PointCollection: ...
    @winrt_commethod(7)
    def put_Points(self, value: win32more.Microsoft.UI.Xaml.Media.PointCollection) -> Void: ...
    Points = property(get_Points, put_Points)
class IPolyLineSegmentStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IPolyLineSegmentStatics'
    _iid_ = Guid('{cf54e568-101a-5349-9189-6f9a1e7f5280}')
    @winrt_commethod(6)
    def get_PointsProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    PointsProperty = property(get_PointsProperty, None)
class IPolyQuadraticBezierSegment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IPolyQuadraticBezierSegment'
    _iid_ = Guid('{56372f4c-c531-5c3e-b0e0-1645f5a8d872}')
    @winrt_commethod(6)
    def get_Points(self) -> win32more.Microsoft.UI.Xaml.Media.PointCollection: ...
    @winrt_commethod(7)
    def put_Points(self, value: win32more.Microsoft.UI.Xaml.Media.PointCollection) -> Void: ...
    Points = property(get_Points, put_Points)
class IPolyQuadraticBezierSegmentStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IPolyQuadraticBezierSegmentStatics'
    _iid_ = Guid('{7eb6374d-cd30-5507-b2ab-c4e3a7dc60bf}')
    @winrt_commethod(6)
    def get_PointsProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    PointsProperty = property(get_PointsProperty, None)
class IProjection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IProjection'
    _iid_ = Guid('{c95364b3-6058-5ee5-9e28-d38b7679fcd4}')
class IProjectionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IProjectionFactory'
    _iid_ = Guid('{870ea34f-db61-5b75-89ad-e0480c802937}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Projection: ...
class IQuadraticBezierSegment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IQuadraticBezierSegment'
    _iid_ = Guid('{6048abe4-7a12-5195-bd61-71dfd0361c38}')
    @winrt_commethod(6)
    def get_Point1(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def put_Point1(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(8)
    def get_Point2(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(9)
    def put_Point2(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    Point1 = property(get_Point1, put_Point1)
    Point2 = property(get_Point2, put_Point2)
class IQuadraticBezierSegmentStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IQuadraticBezierSegmentStatics'
    _iid_ = Guid('{4d56ea65-0a1a-528a-a5b6-41da03ac71f4}')
    @winrt_commethod(6)
    def get_Point1Property(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_Point2Property(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Point1Property = property(get_Point1Property, None)
    Point2Property = property(get_Point2Property, None)
class IRadialGradientBrush(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IRadialGradientBrush'
    _iid_ = Guid('{5d493ce1-b844-546a-b772-b3bcba7e98ee}')
    @winrt_commethod(6)
    def get_Center(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def put_Center(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(8)
    def get_RadiusX(self) -> Double: ...
    @winrt_commethod(9)
    def put_RadiusX(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_RadiusY(self) -> Double: ...
    @winrt_commethod(11)
    def put_RadiusY(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def get_GradientOrigin(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(13)
    def put_GradientOrigin(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_commethod(14)
    def get_MappingMode(self) -> win32more.Microsoft.UI.Xaml.Media.BrushMappingMode: ...
    @winrt_commethod(15)
    def put_MappingMode(self, value: win32more.Microsoft.UI.Xaml.Media.BrushMappingMode) -> Void: ...
    @winrt_commethod(16)
    def get_InterpolationSpace(self) -> win32more.Microsoft.UI.Composition.CompositionColorSpace: ...
    @winrt_commethod(17)
    def put_InterpolationSpace(self, value: win32more.Microsoft.UI.Composition.CompositionColorSpace) -> Void: ...
    @winrt_commethod(18)
    def get_SpreadMethod(self) -> win32more.Microsoft.UI.Xaml.Media.GradientSpreadMethod: ...
    @winrt_commethod(19)
    def put_SpreadMethod(self, value: win32more.Microsoft.UI.Xaml.Media.GradientSpreadMethod) -> Void: ...
    @winrt_commethod(20)
    def get_GradientStops(self) -> win32more.Windows.Foundation.Collections.IObservableVector[win32more.Microsoft.UI.Xaml.Media.GradientStop]: ...
    Center = property(get_Center, put_Center)
    GradientOrigin = property(get_GradientOrigin, put_GradientOrigin)
    GradientStops = property(get_GradientStops, None)
    InterpolationSpace = property(get_InterpolationSpace, put_InterpolationSpace)
    MappingMode = property(get_MappingMode, put_MappingMode)
    RadiusX = property(get_RadiusX, put_RadiusX)
    RadiusY = property(get_RadiusY, put_RadiusY)
    SpreadMethod = property(get_SpreadMethod, put_SpreadMethod)
class IRadialGradientBrushFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IRadialGradientBrushFactory'
    _iid_ = Guid('{d90ba26e-9e67-54bd-a2d9-61c8f9f1d433}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.RadialGradientBrush: ...
class IRadialGradientBrushStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IRadialGradientBrushStatics'
    _iid_ = Guid('{f275a0b8-66f9-5b7d-a415-7eda65fe6dd3}')
    @winrt_commethod(6)
    def get_CenterProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_RadiusXProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_RadiusYProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_GradientOriginProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_InterpolationSpaceProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_MappingModeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_SpreadMethodProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    CenterProperty = property(get_CenterProperty, None)
    GradientOriginProperty = property(get_GradientOriginProperty, None)
    InterpolationSpaceProperty = property(get_InterpolationSpaceProperty, None)
    MappingModeProperty = property(get_MappingModeProperty, None)
    RadiusXProperty = property(get_RadiusXProperty, None)
    RadiusYProperty = property(get_RadiusYProperty, None)
    SpreadMethodProperty = property(get_SpreadMethodProperty, None)
class IRectangleGeometry(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IRectangleGeometry'
    _iid_ = Guid('{b6143890-a5f5-54e0-ab42-d88bab451f04}')
    @winrt_commethod(6)
    def get_Rect(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def put_Rect(self, value: win32more.Windows.Foundation.Rect) -> Void: ...
    Rect = property(get_Rect, put_Rect)
class IRectangleGeometryStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IRectangleGeometryStatics'
    _iid_ = Guid('{1ae7ac26-8a8b-55a5-b035-586e2b642919}')
    @winrt_commethod(6)
    def get_RectProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    RectProperty = property(get_RectProperty, None)
class IRenderedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IRenderedEventArgs'
    _iid_ = Guid('{b268b885-118d-5b66-8099-3b6bb8644726}')
    @winrt_commethod(6)
    def get_FrameDuration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    FrameDuration = property(get_FrameDuration, None)
class IRenderingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IRenderingEventArgs'
    _iid_ = Guid('{a67c8f8d-1885-5fc9-975c-901224f79b1e}')
    @winrt_commethod(6)
    def get_RenderingTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    RenderingTime = property(get_RenderingTime, None)
class IRotateTransform(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IRotateTransform'
    _iid_ = Guid('{d4686e7c-a374-5cac-8927-0ef07c5b254d}')
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
    Angle = property(get_Angle, put_Angle)
    CenterX = property(get_CenterX, put_CenterX)
    CenterY = property(get_CenterY, put_CenterY)
class IRotateTransformStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IRotateTransformStatics'
    _iid_ = Guid('{8ec4c662-04f8-51d7-bcb2-17f10c2faa38}')
    @winrt_commethod(6)
    def get_CenterXProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_CenterYProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_AngleProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    AngleProperty = property(get_AngleProperty, None)
    CenterXProperty = property(get_CenterXProperty, None)
    CenterYProperty = property(get_CenterYProperty, None)
class IScaleTransform(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IScaleTransform'
    _iid_ = Guid('{94b064a4-34f0-5ef9-8b67-444f5699f52a}')
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IScaleTransformStatics'
    _iid_ = Guid('{76485bd5-a5bf-5790-a837-8193c84df353}')
    @winrt_commethod(6)
    def get_CenterXProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_CenterYProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ScaleXProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_ScaleYProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    CenterXProperty = property(get_CenterXProperty, None)
    CenterYProperty = property(get_CenterYProperty, None)
    ScaleXProperty = property(get_ScaleXProperty, None)
    ScaleYProperty = property(get_ScaleYProperty, None)
class IShadow(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IShadow'
    _iid_ = Guid('{cc12fd6a-50aa-5eb3-9a0e-b938b454c439}')
class IShadowFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IShadowFactory'
    _iid_ = Guid('{c9115fbb-fcc3-52bf-b8ee-c348102a46e0}')
class ISkewTransform(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ISkewTransform'
    _iid_ = Guid('{230abaa6-a9b6-5210-873f-36bea29d7c06}')
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
    AngleX = property(get_AngleX, put_AngleX)
    AngleY = property(get_AngleY, put_AngleY)
    CenterX = property(get_CenterX, put_CenterX)
    CenterY = property(get_CenterY, put_CenterY)
class ISkewTransformStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ISkewTransformStatics'
    _iid_ = Guid('{93265150-53d0-52e3-88a3-3d93e2ed861a}')
    @winrt_commethod(6)
    def get_CenterXProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_CenterYProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_AngleXProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_AngleYProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    AngleXProperty = property(get_AngleXProperty, None)
    AngleYProperty = property(get_AngleYProperty, None)
    CenterXProperty = property(get_CenterXProperty, None)
    CenterYProperty = property(get_CenterYProperty, None)
class ISolidColorBrush(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ISolidColorBrush'
    _iid_ = Guid('{b3865c31-37c8-55c1-8a72-d41c67642e2a}')
    @winrt_commethod(6)
    def get_Color(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_Color(self, value: win32more.Windows.UI.Color) -> Void: ...
    Color = property(get_Color, put_Color)
class ISolidColorBrushFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ISolidColorBrushFactory'
    _iid_ = Guid('{7b559384-4daa-54f4-91ef-33a23fd816ca}')
    @winrt_commethod(6)
    def CreateInstanceWithColor(self, color: win32more.Windows.UI.Color) -> win32more.Microsoft.UI.Xaml.Media.SolidColorBrush: ...
class ISolidColorBrushStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ISolidColorBrushStatics'
    _iid_ = Guid('{6bc16da0-c4e6-59b8-995b-b31e48424c07}')
    @winrt_commethod(6)
    def get_ColorProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    ColorProperty = property(get_ColorProperty, None)
class ISystemBackdrop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ISystemBackdrop'
    _iid_ = Guid('{5aeed5c4-37ac-5852-b73f-1b76ebc3205f}')
    @winrt_commethod(6)
    def GetDefaultSystemBackdropConfiguration(self, target: win32more.Microsoft.UI.Composition.ICompositionSupportsSystemBackdrop, xamlRoot: win32more.Microsoft.UI.Xaml.XamlRoot) -> win32more.Microsoft.UI.Composition.SystemBackdrops.SystemBackdropConfiguration: ...
class ISystemBackdropFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ISystemBackdropFactory'
    _iid_ = Guid('{1e07656b-fad2-5b29-913f-b6748bc45942}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.SystemBackdrop: ...
class ISystemBackdropOverrides(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ISystemBackdropOverrides'
    _iid_ = Guid('{eb1f5399-cad7-5611-b637-09d76a07e708}')
    @winrt_commethod(6)
    def OnTargetConnected(self, connectedTarget: win32more.Microsoft.UI.Composition.ICompositionSupportsSystemBackdrop, xamlRoot: win32more.Microsoft.UI.Xaml.XamlRoot) -> Void: ...
    @winrt_commethod(7)
    def OnTargetDisconnected(self, disconnectedTarget: win32more.Microsoft.UI.Composition.ICompositionSupportsSystemBackdrop) -> Void: ...
    @winrt_commethod(8)
    def OnDefaultSystemBackdropConfigurationChanged(self, target: win32more.Microsoft.UI.Composition.ICompositionSupportsSystemBackdrop, xamlRoot: win32more.Microsoft.UI.Xaml.XamlRoot) -> Void: ...
class IThemeShadow(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IThemeShadow'
    _iid_ = Guid('{c264208a-d1f4-58ae-8a88-fc59148bee69}')
    @winrt_commethod(6)
    def get_Receivers(self) -> win32more.Microsoft.UI.Xaml.UIElementWeakCollection: ...
    Receivers = property(get_Receivers, None)
class IThemeShadowFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IThemeShadowFactory'
    _iid_ = Guid('{704a9c96-76a0-569e-8ceb-34e92a23fe11}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.ThemeShadow: ...
class ITileBrush(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ITileBrush'
    _iid_ = Guid('{ee46060d-cabc-505d-883c-75d2e0e45875}')
    @winrt_commethod(6)
    def get_AlignmentX(self) -> win32more.Microsoft.UI.Xaml.Media.AlignmentX: ...
    @winrt_commethod(7)
    def put_AlignmentX(self, value: win32more.Microsoft.UI.Xaml.Media.AlignmentX) -> Void: ...
    @winrt_commethod(8)
    def get_AlignmentY(self) -> win32more.Microsoft.UI.Xaml.Media.AlignmentY: ...
    @winrt_commethod(9)
    def put_AlignmentY(self, value: win32more.Microsoft.UI.Xaml.Media.AlignmentY) -> Void: ...
    @winrt_commethod(10)
    def get_Stretch(self) -> win32more.Microsoft.UI.Xaml.Media.Stretch: ...
    @winrt_commethod(11)
    def put_Stretch(self, value: win32more.Microsoft.UI.Xaml.Media.Stretch) -> Void: ...
    AlignmentX = property(get_AlignmentX, put_AlignmentX)
    AlignmentY = property(get_AlignmentY, put_AlignmentY)
    Stretch = property(get_Stretch, put_Stretch)
class ITileBrushFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ITileBrushFactory'
    _iid_ = Guid('{8542e5e6-5177-506f-8a3b-aa7da651f099}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.TileBrush: ...
class ITileBrushStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ITileBrushStatics'
    _iid_ = Guid('{f402197b-9047-5f8a-90bc-6f5d8c748a5f}')
    @winrt_commethod(6)
    def get_AlignmentXProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_AlignmentYProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_StretchProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    AlignmentXProperty = property(get_AlignmentXProperty, None)
    AlignmentYProperty = property(get_AlignmentYProperty, None)
    StretchProperty = property(get_StretchProperty, None)
class ITransform(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ITransform'
    _iid_ = Guid('{92a8dee5-1413-56b9-8cca-3c46918fde1b}')
class ITransformFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ITransformFactory'
    _iid_ = Guid('{7da293f9-b82e-5d15-b623-c08210cbb640}')
class ITransformGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ITransformGroup'
    _iid_ = Guid('{17c55f3b-899c-588f-8bd4-40fa3a5fcb04}')
    @winrt_commethod(6)
    def get_Children(self) -> win32more.Microsoft.UI.Xaml.Media.TransformCollection: ...
    @winrt_commethod(7)
    def put_Children(self, value: win32more.Microsoft.UI.Xaml.Media.TransformCollection) -> Void: ...
    @winrt_commethod(8)
    def get_Value(self) -> win32more.Microsoft.UI.Xaml.Media.Matrix: ...
    Children = property(get_Children, put_Children)
    Value = property(get_Value, None)
class ITransformGroupStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ITransformGroupStatics'
    _iid_ = Guid('{8f1508f6-7dcf-53d5-bbc0-d8fcd96d7399}')
    @winrt_commethod(6)
    def get_ChildrenProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    ChildrenProperty = property(get_ChildrenProperty, None)
class ITranslateTransform(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ITranslateTransform'
    _iid_ = Guid('{cfa21ca9-b79f-5450-b459-a96c48cb2c8f}')
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.ITranslateTransformStatics'
    _iid_ = Guid('{1342eb11-5a6e-5263-ab3e-9b672a86fc0c}')
    @winrt_commethod(6)
    def get_XProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_YProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    XProperty = property(get_XProperty, None)
    YProperty = property(get_YProperty, None)
class IVisualTreeHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IVisualTreeHelper'
    _iid_ = Guid('{5f69ac1e-6504-5e3f-a11c-87684c1db814}')
class IVisualTreeHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IVisualTreeHelperStatics'
    _iid_ = Guid('{5aece43c-7651-5bb5-855c-2198496e455e}')
    @winrt_commethod(6)
    def FindElementsInHostCoordinatesPoint(self, intersectingPoint: win32more.Windows.Foundation.Point, subtree: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Xaml.UIElement]: ...
    @winrt_commethod(7)
    def FindElementsInHostCoordinatesRect(self, intersectingRect: win32more.Windows.Foundation.Rect, subtree: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Xaml.UIElement]: ...
    @winrt_commethod(8)
    def FindAllElementsInHostCoordinatesPoint(self, intersectingPoint: win32more.Windows.Foundation.Point, subtree: win32more.Microsoft.UI.Xaml.UIElement, includeAllElements: Boolean) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Xaml.UIElement]: ...
    @winrt_commethod(9)
    def FindAllElementsInHostCoordinatesRect(self, intersectingRect: win32more.Windows.Foundation.Rect, subtree: win32more.Microsoft.UI.Xaml.UIElement, includeAllElements: Boolean) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Xaml.UIElement]: ...
    @winrt_commethod(10)
    def GetChild(self, reference: win32more.Microsoft.UI.Xaml.DependencyObject, childIndex: Int32) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_commethod(11)
    def GetChildrenCount(self, reference: win32more.Microsoft.UI.Xaml.DependencyObject) -> Int32: ...
    @winrt_commethod(12)
    def GetParent(self, reference: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_commethod(13)
    def DisconnectChildrenRecursive(self, element: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(14)
    def GetOpenPopups(self, window: win32more.Microsoft.UI.Xaml.Window) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.UI.Xaml.Controls.Primitives.Popup]: ...
    @winrt_commethod(15)
    def GetOpenPopupsForXamlRoot(self, xamlRoot: win32more.Microsoft.UI.Xaml.XamlRoot) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.UI.Xaml.Controls.Primitives.Popup]: ...
class IXamlCompositionBrushBase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IXamlCompositionBrushBase'
    _iid_ = Guid('{feaead28-5cd0-5e58-bcea-8670f832aca9}')
    @winrt_commethod(6)
    def get_FallbackColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_FallbackColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    FallbackColor = property(get_FallbackColor, put_FallbackColor)
class IXamlCompositionBrushBaseFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IXamlCompositionBrushBaseFactory'
    _iid_ = Guid('{b1626d56-0f6f-5416-ada4-5c8105d3f082}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.XamlCompositionBrushBase: ...
class IXamlCompositionBrushBaseOverrides(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IXamlCompositionBrushBaseOverrides'
    _iid_ = Guid('{8881b559-54a0-56c4-a79a-135152fb1dfa}')
    @winrt_commethod(6)
    def OnConnected(self) -> Void: ...
    @winrt_commethod(7)
    def OnDisconnected(self) -> Void: ...
class IXamlCompositionBrushBaseProtected(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IXamlCompositionBrushBaseProtected'
    _iid_ = Guid('{6617e1a5-e27a-5b95-b03e-6758b58f92a0}')
    @winrt_commethod(6)
    def get_CompositionBrush(self) -> win32more.Microsoft.UI.Composition.CompositionBrush: ...
    @winrt_commethod(7)
    def put_CompositionBrush(self, value: win32more.Microsoft.UI.Composition.CompositionBrush) -> Void: ...
    CompositionBrush = property(get_CompositionBrush, put_CompositionBrush)
class IXamlCompositionBrushBaseStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IXamlCompositionBrushBaseStatics'
    _iid_ = Guid('{3eed6e16-c386-5a1c-b70d-ef1c0015e691}')
    @winrt_commethod(6)
    def get_FallbackColorProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    FallbackColorProperty = property(get_FallbackColorProperty, None)
class IXamlLight(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IXamlLight'
    _iid_ = Guid('{dcd20139-8cd5-5da5-a25c-2b7b813d8d58}')
class IXamlLightFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IXamlLightFactory'
    _iid_ = Guid('{76da6306-96fc-553e-bb39-9a4801d06f48}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.XamlLight: ...
class IXamlLightOverrides(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IXamlLightOverrides'
    _iid_ = Guid('{696d4f30-92ee-540d-ad70-33d4489514d0}')
    @winrt_commethod(6)
    def GetId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def OnConnected(self, newElement: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(8)
    def OnDisconnected(self, oldElement: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
class IXamlLightProtected(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IXamlLightProtected'
    _iid_ = Guid('{c307bf12-fdaf-54ca-a631-ad0e86263c6e}')
    @winrt_commethod(6)
    def get_CompositionLight(self) -> win32more.Microsoft.UI.Composition.CompositionLight: ...
    @winrt_commethod(7)
    def put_CompositionLight(self, value: win32more.Microsoft.UI.Composition.CompositionLight) -> Void: ...
    CompositionLight = property(get_CompositionLight, put_CompositionLight)
class IXamlLightStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Media.IXamlLightStatics'
    _iid_ = Guid('{a2d8ea26-26ff-5374-b1dd-f232d5604f6a}')
    @winrt_commethod(6)
    def AddTargetElement(self, lightId: WinRT_String, element: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(7)
    def RemoveTargetElement(self, lightId: WinRT_String, element: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(8)
    def AddTargetBrush(self, lightId: WinRT_String, brush: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(9)
    def RemoveTargetBrush(self, lightId: WinRT_String, brush: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
class _ImageBrush_Meta_(ComPtr.__class__):
    pass
class ImageBrush(ComPtr, metaclass=_ImageBrush_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.TileBrush
    default_interface: win32more.Microsoft.UI.Xaml.Media.IImageBrush
    _classid_ = 'Microsoft.UI.Xaml.Media.ImageBrush'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.ImageBrush.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.ImageBrush: ...
    @winrt_mixinmethod
    def get_ImageSource(self: win32more.Microsoft.UI.Xaml.Media.IImageBrush) -> win32more.Microsoft.UI.Xaml.Media.ImageSource: ...
    @winrt_mixinmethod
    def put_ImageSource(self: win32more.Microsoft.UI.Xaml.Media.IImageBrush, value: win32more.Microsoft.UI.Xaml.Media.ImageSource) -> Void: ...
    @winrt_mixinmethod
    def add_ImageFailed(self: win32more.Microsoft.UI.Xaml.Media.IImageBrush, handler: win32more.Microsoft.UI.Xaml.ExceptionRoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ImageFailed(self: win32more.Microsoft.UI.Xaml.Media.IImageBrush, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ImageOpened(self: win32more.Microsoft.UI.Xaml.Media.IImageBrush, handler: win32more.Microsoft.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ImageOpened(self: win32more.Microsoft.UI.Xaml.Media.IImageBrush, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_ImageSourceProperty(cls: win32more.Microsoft.UI.Xaml.Media.IImageBrushStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    ImageSource = property(get_ImageSource, put_ImageSource)
    _ImageBrush_Meta_.ImageSourceProperty = property(get_ImageSourceProperty, None)
    ImageFailed = event()
    ImageOpened = event()
class ImageSource(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Media.IImageSource
    _classid_ = 'Microsoft.UI.Xaml.Media.ImageSource'
class _LineGeometry_Meta_(ComPtr.__class__):
    pass
class LineGeometry(ComPtr, metaclass=_LineGeometry_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Geometry
    default_interface: win32more.Microsoft.UI.Xaml.Media.ILineGeometry
    _classid_ = 'Microsoft.UI.Xaml.Media.LineGeometry'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.LineGeometry.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.LineGeometry: ...
    @winrt_mixinmethod
    def get_StartPoint(self: win32more.Microsoft.UI.Xaml.Media.ILineGeometry) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_StartPoint(self: win32more.Microsoft.UI.Xaml.Media.ILineGeometry, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_EndPoint(self: win32more.Microsoft.UI.Xaml.Media.ILineGeometry) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_EndPoint(self: win32more.Microsoft.UI.Xaml.Media.ILineGeometry, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_classmethod
    def get_StartPointProperty(cls: win32more.Microsoft.UI.Xaml.Media.ILineGeometryStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_EndPointProperty(cls: win32more.Microsoft.UI.Xaml.Media.ILineGeometryStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    EndPoint = property(get_EndPoint, put_EndPoint)
    StartPoint = property(get_StartPoint, put_StartPoint)
    _LineGeometry_Meta_.EndPointProperty = property(get_EndPointProperty, None)
    _LineGeometry_Meta_.StartPointProperty = property(get_StartPointProperty, None)
class _LineSegment_Meta_(ComPtr.__class__):
    pass
class LineSegment(ComPtr, metaclass=_LineSegment_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.PathSegment
    default_interface: win32more.Microsoft.UI.Xaml.Media.ILineSegment
    _classid_ = 'Microsoft.UI.Xaml.Media.LineSegment'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.LineSegment.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.LineSegment: ...
    @winrt_mixinmethod
    def get_Point(self: win32more.Microsoft.UI.Xaml.Media.ILineSegment) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Point(self: win32more.Microsoft.UI.Xaml.Media.ILineSegment, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_classmethod
    def get_PointProperty(cls: win32more.Microsoft.UI.Xaml.Media.ILineSegmentStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Point = property(get_Point, put_Point)
    _LineSegment_Meta_.PointProperty = property(get_PointProperty, None)
class _LinearGradientBrush_Meta_(ComPtr.__class__):
    pass
class LinearGradientBrush(ComPtr, metaclass=_LinearGradientBrush_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.GradientBrush
    default_interface: win32more.Microsoft.UI.Xaml.Media.ILinearGradientBrush
    _classid_ = 'Microsoft.UI.Xaml.Media.LinearGradientBrush'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.LinearGradientBrush.CreateInstance(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.LinearGradientBrush.CreateInstanceWithGradientStopCollectionAndAngle(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.LinearGradientBrush: ...
    @winrt_factorymethod
    def CreateInstanceWithGradientStopCollectionAndAngle(cls: win32more.Microsoft.UI.Xaml.Media.ILinearGradientBrushFactory, gradientStopCollection: win32more.Microsoft.UI.Xaml.Media.GradientStopCollection, angle: Double) -> win32more.Microsoft.UI.Xaml.Media.LinearGradientBrush: ...
    @winrt_mixinmethod
    def get_StartPoint(self: win32more.Microsoft.UI.Xaml.Media.ILinearGradientBrush) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_StartPoint(self: win32more.Microsoft.UI.Xaml.Media.ILinearGradientBrush, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_EndPoint(self: win32more.Microsoft.UI.Xaml.Media.ILinearGradientBrush) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_EndPoint(self: win32more.Microsoft.UI.Xaml.Media.ILinearGradientBrush, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_classmethod
    def get_StartPointProperty(cls: win32more.Microsoft.UI.Xaml.Media.ILinearGradientBrushStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_EndPointProperty(cls: win32more.Microsoft.UI.Xaml.Media.ILinearGradientBrushStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    EndPoint = property(get_EndPoint, put_EndPoint)
    StartPoint = property(get_StartPoint, put_StartPoint)
    _LinearGradientBrush_Meta_.EndPointProperty = property(get_EndPointProperty, None)
    _LinearGradientBrush_Meta_.StartPointProperty = property(get_StartPointProperty, None)
class LoadedImageSourceLoadCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Media.ILoadedImageSourceLoadCompletedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Media.LoadedImageSourceLoadCompletedEventArgs'
    @winrt_mixinmethod
    def get_Status(self: win32more.Microsoft.UI.Xaml.Media.ILoadedImageSourceLoadCompletedEventArgs) -> win32more.Microsoft.UI.Xaml.Media.LoadedImageSourceLoadStatus: ...
    Status = property(get_Status, None)
class LoadedImageSourceLoadStatus(Enum, Int32):
    Success = 0
    NetworkError = 1
    InvalidFormat = 2
    Other = 3
class LoadedImageSurface(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Microsoft.UI.Xaml.Media.ILoadedImageSurface
    _classid_ = 'Microsoft.UI.Xaml.Media.LoadedImageSurface'
    @winrt_mixinmethod
    def get_DecodedPhysicalSize(self: win32more.Microsoft.UI.Xaml.Media.ILoadedImageSurface) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_DecodedSize(self: win32more.Microsoft.UI.Xaml.Media.ILoadedImageSurface) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_NaturalSize(self: win32more.Microsoft.UI.Xaml.Media.ILoadedImageSurface) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def add_LoadCompleted(self: win32more.Microsoft.UI.Xaml.Media.ILoadedImageSurface, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Microsoft.UI.Xaml.Media.LoadedImageSurface, win32more.Microsoft.UI.Xaml.Media.LoadedImageSourceLoadCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LoadCompleted(self: win32more.Microsoft.UI.Xaml.Media.ILoadedImageSurface, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def StartLoadFromUriWithSize(cls: win32more.Microsoft.UI.Xaml.Media.ILoadedImageSurfaceStatics, uri: win32more.Windows.Foundation.Uri, desiredMaxSize: win32more.Windows.Foundation.Size) -> win32more.Microsoft.UI.Xaml.Media.LoadedImageSurface: ...
    @winrt_classmethod
    def StartLoadFromUri(cls: win32more.Microsoft.UI.Xaml.Media.ILoadedImageSurfaceStatics, uri: win32more.Windows.Foundation.Uri) -> win32more.Microsoft.UI.Xaml.Media.LoadedImageSurface: ...
    @winrt_classmethod
    def StartLoadFromStreamWithSize(cls: win32more.Microsoft.UI.Xaml.Media.ILoadedImageSurfaceStatics, stream: win32more.Windows.Storage.Streams.IRandomAccessStream, desiredMaxSize: win32more.Windows.Foundation.Size) -> win32more.Microsoft.UI.Xaml.Media.LoadedImageSurface: ...
    @winrt_classmethod
    def StartLoadFromStream(cls: win32more.Microsoft.UI.Xaml.Media.ILoadedImageSurfaceStatics, stream: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Microsoft.UI.Xaml.Media.LoadedImageSurface: ...
    DecodedPhysicalSize = property(get_DecodedPhysicalSize, None)
    DecodedSize = property(get_DecodedSize, None)
    NaturalSize = property(get_NaturalSize, None)
    LoadCompleted = event()
class Matrix(Structure):
    M11: Double
    M12: Double
    M21: Double
    M22: Double
    OffsetX: Double
    OffsetY: Double
class _Matrix3DProjection_Meta_(ComPtr.__class__):
    pass
class Matrix3DProjection(ComPtr, metaclass=_Matrix3DProjection_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Projection
    default_interface: win32more.Microsoft.UI.Xaml.Media.IMatrix3DProjection
    _classid_ = 'Microsoft.UI.Xaml.Media.Matrix3DProjection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Matrix3DProjection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.Matrix3DProjection: ...
    @winrt_mixinmethod
    def get_ProjectionMatrix(self: win32more.Microsoft.UI.Xaml.Media.IMatrix3DProjection) -> win32more.Microsoft.UI.Xaml.Media.Media3D.Matrix3D: ...
    @winrt_mixinmethod
    def put_ProjectionMatrix(self: win32more.Microsoft.UI.Xaml.Media.IMatrix3DProjection, value: win32more.Microsoft.UI.Xaml.Media.Media3D.Matrix3D) -> Void: ...
    @winrt_classmethod
    def get_ProjectionMatrixProperty(cls: win32more.Microsoft.UI.Xaml.Media.IMatrix3DProjectionStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    ProjectionMatrix = property(get_ProjectionMatrix, put_ProjectionMatrix)
    _Matrix3DProjection_Meta_.ProjectionMatrixProperty = property(get_ProjectionMatrixProperty, None)
class _MatrixHelper_Meta_(ComPtr.__class__):
    pass
class MatrixHelper(ComPtr, metaclass=_MatrixHelper_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Media.IMatrixHelper
    _classid_ = 'Microsoft.UI.Xaml.Media.MatrixHelper'
    @winrt_classmethod
    def get_Identity(cls: win32more.Microsoft.UI.Xaml.Media.IMatrixHelperStatics) -> win32more.Microsoft.UI.Xaml.Media.Matrix: ...
    @winrt_classmethod
    def FromElements(cls: win32more.Microsoft.UI.Xaml.Media.IMatrixHelperStatics, m11: Double, m12: Double, m21: Double, m22: Double, offsetX: Double, offsetY: Double) -> win32more.Microsoft.UI.Xaml.Media.Matrix: ...
    @winrt_classmethod
    def GetIsIdentity(cls: win32more.Microsoft.UI.Xaml.Media.IMatrixHelperStatics, target: win32more.Microsoft.UI.Xaml.Media.Matrix) -> Boolean: ...
    @winrt_classmethod
    def Transform(cls: win32more.Microsoft.UI.Xaml.Media.IMatrixHelperStatics, target: win32more.Microsoft.UI.Xaml.Media.Matrix, point: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.Point: ...
    _MatrixHelper_Meta_.Identity = property(get_Identity, None)
class _MatrixTransform_Meta_(ComPtr.__class__):
    pass
class MatrixTransform(ComPtr, metaclass=_MatrixTransform_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Transform
    default_interface: win32more.Microsoft.UI.Xaml.Media.IMatrixTransform
    _classid_ = 'Microsoft.UI.Xaml.Media.MatrixTransform'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.MatrixTransform.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.MatrixTransform: ...
    @winrt_mixinmethod
    def get_Matrix(self: win32more.Microsoft.UI.Xaml.Media.IMatrixTransform) -> win32more.Microsoft.UI.Xaml.Media.Matrix: ...
    @winrt_mixinmethod
    def put_Matrix(self: win32more.Microsoft.UI.Xaml.Media.IMatrixTransform, value: win32more.Microsoft.UI.Xaml.Media.Matrix) -> Void: ...
    @winrt_classmethod
    def get_MatrixProperty(cls: win32more.Microsoft.UI.Xaml.Media.IMatrixTransformStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Matrix = property(get_Matrix, put_Matrix)
    _MatrixTransform_Meta_.MatrixProperty = property(get_MatrixProperty, None)
class MediaTransportControlsThumbnailRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Media.IMediaTransportControlsThumbnailRequestedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Media.MediaTransportControlsThumbnailRequestedEventArgs'
    @winrt_mixinmethod
    def SetThumbnailImage(self: win32more.Microsoft.UI.Xaml.Media.IMediaTransportControlsThumbnailRequestedEventArgs, source: win32more.Windows.Storage.Streams.IInputStream) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Microsoft.UI.Xaml.Media.IMediaTransportControlsThumbnailRequestedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
class _MicaBackdrop_Meta_(ComPtr.__class__):
    pass
class MicaBackdrop(ComPtr, metaclass=_MicaBackdrop_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.SystemBackdrop
    default_interface: win32more.Microsoft.UI.Xaml.Media.IMicaBackdrop
    _classid_ = 'Microsoft.UI.Xaml.Media.MicaBackdrop'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.MicaBackdrop.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Media.IMicaBackdropFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.MicaBackdrop: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Microsoft.UI.Xaml.Media.IMicaBackdrop) -> win32more.Microsoft.UI.Composition.SystemBackdrops.MicaKind: ...
    @winrt_mixinmethod
    def put_Kind(self: win32more.Microsoft.UI.Xaml.Media.IMicaBackdrop, value: win32more.Microsoft.UI.Composition.SystemBackdrops.MicaKind) -> Void: ...
    @winrt_classmethod
    def get_KindProperty(cls: win32more.Microsoft.UI.Xaml.Media.IMicaBackdropStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Kind = property(get_Kind, put_Kind)
    _MicaBackdrop_Meta_.KindProperty = property(get_KindProperty, None)
class _PathFigure_Meta_(ComPtr.__class__):
    pass
class PathFigure(ComPtr, metaclass=_PathFigure_Meta_):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Media.IPathFigure
    _classid_ = 'Microsoft.UI.Xaml.Media.PathFigure'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.PathFigure.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.PathFigure: ...
    @winrt_mixinmethod
    def get_Segments(self: win32more.Microsoft.UI.Xaml.Media.IPathFigure) -> win32more.Microsoft.UI.Xaml.Media.PathSegmentCollection: ...
    @winrt_mixinmethod
    def put_Segments(self: win32more.Microsoft.UI.Xaml.Media.IPathFigure, value: win32more.Microsoft.UI.Xaml.Media.PathSegmentCollection) -> Void: ...
    @winrt_mixinmethod
    def get_StartPoint(self: win32more.Microsoft.UI.Xaml.Media.IPathFigure) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_StartPoint(self: win32more.Microsoft.UI.Xaml.Media.IPathFigure, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_IsClosed(self: win32more.Microsoft.UI.Xaml.Media.IPathFigure) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsClosed(self: win32more.Microsoft.UI.Xaml.Media.IPathFigure, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsFilled(self: win32more.Microsoft.UI.Xaml.Media.IPathFigure) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsFilled(self: win32more.Microsoft.UI.Xaml.Media.IPathFigure, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_SegmentsProperty(cls: win32more.Microsoft.UI.Xaml.Media.IPathFigureStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StartPointProperty(cls: win32more.Microsoft.UI.Xaml.Media.IPathFigureStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsClosedProperty(cls: win32more.Microsoft.UI.Xaml.Media.IPathFigureStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsFilledProperty(cls: win32more.Microsoft.UI.Xaml.Media.IPathFigureStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    IsClosed = property(get_IsClosed, put_IsClosed)
    IsFilled = property(get_IsFilled, put_IsFilled)
    Segments = property(get_Segments, put_Segments)
    StartPoint = property(get_StartPoint, put_StartPoint)
    _PathFigure_Meta_.IsClosedProperty = property(get_IsClosedProperty, None)
    _PathFigure_Meta_.IsFilledProperty = property(get_IsFilledProperty, None)
    _PathFigure_Meta_.SegmentsProperty = property(get_SegmentsProperty, None)
    _PathFigure_Meta_.StartPointProperty = property(get_StartPointProperty, None)
class PathFigureCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Microsoft.UI.Xaml.Media.PathFigure]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.PathFigure]
    _classid_ = 'Microsoft.UI.Xaml.Media.PathFigureCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.PathFigureCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.PathFigureCollection: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.PathFigure], index: UInt32) -> win32more.Microsoft.UI.Xaml.Media.PathFigure: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.PathFigure]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.PathFigure]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.UI.Xaml.Media.PathFigure]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.PathFigure], value: win32more.Microsoft.UI.Xaml.Media.PathFigure, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.PathFigure], index: UInt32, value: win32more.Microsoft.UI.Xaml.Media.PathFigure) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.PathFigure], index: UInt32, value: win32more.Microsoft.UI.Xaml.Media.PathFigure) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.PathFigure], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.PathFigure], value: win32more.Microsoft.UI.Xaml.Media.PathFigure) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.PathFigure]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.PathFigure]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.PathFigure], startIndex: UInt32, items: FillArray[win32more.Microsoft.UI.Xaml.Media.PathFigure]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.PathFigure], items: PassArray[win32more.Microsoft.UI.Xaml.Media.PathFigure]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Xaml.Media.PathFigure]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Microsoft.UI.Xaml.Media.PathFigure]: ...
    Size = property(get_Size, None)
class _PathGeometry_Meta_(ComPtr.__class__):
    pass
class PathGeometry(ComPtr, metaclass=_PathGeometry_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Geometry
    default_interface: win32more.Microsoft.UI.Xaml.Media.IPathGeometry
    _classid_ = 'Microsoft.UI.Xaml.Media.PathGeometry'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.PathGeometry.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.PathGeometry: ...
    @winrt_mixinmethod
    def get_FillRule(self: win32more.Microsoft.UI.Xaml.Media.IPathGeometry) -> win32more.Microsoft.UI.Xaml.Media.FillRule: ...
    @winrt_mixinmethod
    def put_FillRule(self: win32more.Microsoft.UI.Xaml.Media.IPathGeometry, value: win32more.Microsoft.UI.Xaml.Media.FillRule) -> Void: ...
    @winrt_mixinmethod
    def get_Figures(self: win32more.Microsoft.UI.Xaml.Media.IPathGeometry) -> win32more.Microsoft.UI.Xaml.Media.PathFigureCollection: ...
    @winrt_mixinmethod
    def put_Figures(self: win32more.Microsoft.UI.Xaml.Media.IPathGeometry, value: win32more.Microsoft.UI.Xaml.Media.PathFigureCollection) -> Void: ...
    @winrt_classmethod
    def get_FillRuleProperty(cls: win32more.Microsoft.UI.Xaml.Media.IPathGeometryStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FiguresProperty(cls: win32more.Microsoft.UI.Xaml.Media.IPathGeometryStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Figures = property(get_Figures, put_Figures)
    FillRule = property(get_FillRule, put_FillRule)
    _PathGeometry_Meta_.FiguresProperty = property(get_FiguresProperty, None)
    _PathGeometry_Meta_.FillRuleProperty = property(get_FillRuleProperty, None)
class PathSegment(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Media.IPathSegment
    _classid_ = 'Microsoft.UI.Xaml.Media.PathSegment'
class PathSegmentCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Microsoft.UI.Xaml.Media.PathSegment]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.PathSegment]
    _classid_ = 'Microsoft.UI.Xaml.Media.PathSegmentCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.PathSegmentCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.PathSegmentCollection: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.PathSegment], index: UInt32) -> win32more.Microsoft.UI.Xaml.Media.PathSegment: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.PathSegment]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.PathSegment]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.UI.Xaml.Media.PathSegment]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.PathSegment], value: win32more.Microsoft.UI.Xaml.Media.PathSegment, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.PathSegment], index: UInt32, value: win32more.Microsoft.UI.Xaml.Media.PathSegment) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.PathSegment], index: UInt32, value: win32more.Microsoft.UI.Xaml.Media.PathSegment) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.PathSegment], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.PathSegment], value: win32more.Microsoft.UI.Xaml.Media.PathSegment) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.PathSegment]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.PathSegment]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.PathSegment], startIndex: UInt32, items: FillArray[win32more.Microsoft.UI.Xaml.Media.PathSegment]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.PathSegment], items: PassArray[win32more.Microsoft.UI.Xaml.Media.PathSegment]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Xaml.Media.PathSegment]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Microsoft.UI.Xaml.Media.PathSegment]: ...
    Size = property(get_Size, None)
class PenLineCap(Enum, Int32):
    Flat = 0
    Square = 1
    Round = 2
    Triangle = 3
class PenLineJoin(Enum, Int32):
    Miter = 0
    Bevel = 1
    Round = 2
class _PlaneProjection_Meta_(ComPtr.__class__):
    pass
class PlaneProjection(ComPtr, metaclass=_PlaneProjection_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Projection
    default_interface: win32more.Microsoft.UI.Xaml.Media.IPlaneProjection
    _classid_ = 'Microsoft.UI.Xaml.Media.PlaneProjection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.PlaneProjection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.PlaneProjection: ...
    @winrt_mixinmethod
    def get_LocalOffsetX(self: win32more.Microsoft.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_LocalOffsetX(self: win32more.Microsoft.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_LocalOffsetY(self: win32more.Microsoft.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_LocalOffsetY(self: win32more.Microsoft.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_LocalOffsetZ(self: win32more.Microsoft.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_LocalOffsetZ(self: win32more.Microsoft.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RotationX(self: win32more.Microsoft.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_RotationX(self: win32more.Microsoft.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RotationY(self: win32more.Microsoft.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_RotationY(self: win32more.Microsoft.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RotationZ(self: win32more.Microsoft.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_RotationZ(self: win32more.Microsoft.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_CenterOfRotationX(self: win32more.Microsoft.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_CenterOfRotationX(self: win32more.Microsoft.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_CenterOfRotationY(self: win32more.Microsoft.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_CenterOfRotationY(self: win32more.Microsoft.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_CenterOfRotationZ(self: win32more.Microsoft.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_CenterOfRotationZ(self: win32more.Microsoft.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_GlobalOffsetX(self: win32more.Microsoft.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_GlobalOffsetX(self: win32more.Microsoft.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_GlobalOffsetY(self: win32more.Microsoft.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_GlobalOffsetY(self: win32more.Microsoft.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_GlobalOffsetZ(self: win32more.Microsoft.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_GlobalOffsetZ(self: win32more.Microsoft.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ProjectionMatrix(self: win32more.Microsoft.UI.Xaml.Media.IPlaneProjection) -> win32more.Microsoft.UI.Xaml.Media.Media3D.Matrix3D: ...
    @winrt_classmethod
    def get_LocalOffsetXProperty(cls: win32more.Microsoft.UI.Xaml.Media.IPlaneProjectionStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_LocalOffsetYProperty(cls: win32more.Microsoft.UI.Xaml.Media.IPlaneProjectionStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_LocalOffsetZProperty(cls: win32more.Microsoft.UI.Xaml.Media.IPlaneProjectionStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RotationXProperty(cls: win32more.Microsoft.UI.Xaml.Media.IPlaneProjectionStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RotationYProperty(cls: win32more.Microsoft.UI.Xaml.Media.IPlaneProjectionStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RotationZProperty(cls: win32more.Microsoft.UI.Xaml.Media.IPlaneProjectionStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CenterOfRotationXProperty(cls: win32more.Microsoft.UI.Xaml.Media.IPlaneProjectionStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CenterOfRotationYProperty(cls: win32more.Microsoft.UI.Xaml.Media.IPlaneProjectionStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CenterOfRotationZProperty(cls: win32more.Microsoft.UI.Xaml.Media.IPlaneProjectionStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_GlobalOffsetXProperty(cls: win32more.Microsoft.UI.Xaml.Media.IPlaneProjectionStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_GlobalOffsetYProperty(cls: win32more.Microsoft.UI.Xaml.Media.IPlaneProjectionStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_GlobalOffsetZProperty(cls: win32more.Microsoft.UI.Xaml.Media.IPlaneProjectionStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ProjectionMatrixProperty(cls: win32more.Microsoft.UI.Xaml.Media.IPlaneProjectionStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    CenterOfRotationX = property(get_CenterOfRotationX, put_CenterOfRotationX)
    CenterOfRotationY = property(get_CenterOfRotationY, put_CenterOfRotationY)
    CenterOfRotationZ = property(get_CenterOfRotationZ, put_CenterOfRotationZ)
    GlobalOffsetX = property(get_GlobalOffsetX, put_GlobalOffsetX)
    GlobalOffsetY = property(get_GlobalOffsetY, put_GlobalOffsetY)
    GlobalOffsetZ = property(get_GlobalOffsetZ, put_GlobalOffsetZ)
    LocalOffsetX = property(get_LocalOffsetX, put_LocalOffsetX)
    LocalOffsetY = property(get_LocalOffsetY, put_LocalOffsetY)
    LocalOffsetZ = property(get_LocalOffsetZ, put_LocalOffsetZ)
    ProjectionMatrix = property(get_ProjectionMatrix, None)
    RotationX = property(get_RotationX, put_RotationX)
    RotationY = property(get_RotationY, put_RotationY)
    RotationZ = property(get_RotationZ, put_RotationZ)
    _PlaneProjection_Meta_.CenterOfRotationXProperty = property(get_CenterOfRotationXProperty, None)
    _PlaneProjection_Meta_.CenterOfRotationYProperty = property(get_CenterOfRotationYProperty, None)
    _PlaneProjection_Meta_.CenterOfRotationZProperty = property(get_CenterOfRotationZProperty, None)
    _PlaneProjection_Meta_.GlobalOffsetXProperty = property(get_GlobalOffsetXProperty, None)
    _PlaneProjection_Meta_.GlobalOffsetYProperty = property(get_GlobalOffsetYProperty, None)
    _PlaneProjection_Meta_.GlobalOffsetZProperty = property(get_GlobalOffsetZProperty, None)
    _PlaneProjection_Meta_.LocalOffsetXProperty = property(get_LocalOffsetXProperty, None)
    _PlaneProjection_Meta_.LocalOffsetYProperty = property(get_LocalOffsetYProperty, None)
    _PlaneProjection_Meta_.LocalOffsetZProperty = property(get_LocalOffsetZProperty, None)
    _PlaneProjection_Meta_.ProjectionMatrixProperty = property(get_ProjectionMatrixProperty, None)
    _PlaneProjection_Meta_.RotationXProperty = property(get_RotationXProperty, None)
    _PlaneProjection_Meta_.RotationYProperty = property(get_RotationYProperty, None)
    _PlaneProjection_Meta_.RotationZProperty = property(get_RotationZProperty, None)
class PointCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Windows.Foundation.Point]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Foundation.Point]
    _classid_ = 'Microsoft.UI.Xaml.Media.PointCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.PointCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.PointCollection: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Foundation.Point], index: UInt32) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Foundation.Point]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Foundation.Point]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.Foundation.Point]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Foundation.Point], value: win32more.Windows.Foundation.Point, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Foundation.Point], index: UInt32, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Foundation.Point], index: UInt32, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Foundation.Point], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Foundation.Point], value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Foundation.Point]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Foundation.Point]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Foundation.Point], startIndex: UInt32, items: FillArray[win32more.Windows.Foundation.Point]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.Foundation.Point], items: PassArray[win32more.Windows.Foundation.Point]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Point]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.Foundation.Point]: ...
    Size = property(get_Size, None)
class _PolyBezierSegment_Meta_(ComPtr.__class__):
    pass
class PolyBezierSegment(ComPtr, metaclass=_PolyBezierSegment_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.PathSegment
    default_interface: win32more.Microsoft.UI.Xaml.Media.IPolyBezierSegment
    _classid_ = 'Microsoft.UI.Xaml.Media.PolyBezierSegment'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.PolyBezierSegment.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.PolyBezierSegment: ...
    @winrt_mixinmethod
    def get_Points(self: win32more.Microsoft.UI.Xaml.Media.IPolyBezierSegment) -> win32more.Microsoft.UI.Xaml.Media.PointCollection: ...
    @winrt_mixinmethod
    def put_Points(self: win32more.Microsoft.UI.Xaml.Media.IPolyBezierSegment, value: win32more.Microsoft.UI.Xaml.Media.PointCollection) -> Void: ...
    @winrt_classmethod
    def get_PointsProperty(cls: win32more.Microsoft.UI.Xaml.Media.IPolyBezierSegmentStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Points = property(get_Points, put_Points)
    _PolyBezierSegment_Meta_.PointsProperty = property(get_PointsProperty, None)
class _PolyLineSegment_Meta_(ComPtr.__class__):
    pass
class PolyLineSegment(ComPtr, metaclass=_PolyLineSegment_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.PathSegment
    default_interface: win32more.Microsoft.UI.Xaml.Media.IPolyLineSegment
    _classid_ = 'Microsoft.UI.Xaml.Media.PolyLineSegment'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.PolyLineSegment.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.PolyLineSegment: ...
    @winrt_mixinmethod
    def get_Points(self: win32more.Microsoft.UI.Xaml.Media.IPolyLineSegment) -> win32more.Microsoft.UI.Xaml.Media.PointCollection: ...
    @winrt_mixinmethod
    def put_Points(self: win32more.Microsoft.UI.Xaml.Media.IPolyLineSegment, value: win32more.Microsoft.UI.Xaml.Media.PointCollection) -> Void: ...
    @winrt_classmethod
    def get_PointsProperty(cls: win32more.Microsoft.UI.Xaml.Media.IPolyLineSegmentStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Points = property(get_Points, put_Points)
    _PolyLineSegment_Meta_.PointsProperty = property(get_PointsProperty, None)
class _PolyQuadraticBezierSegment_Meta_(ComPtr.__class__):
    pass
class PolyQuadraticBezierSegment(ComPtr, metaclass=_PolyQuadraticBezierSegment_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.PathSegment
    default_interface: win32more.Microsoft.UI.Xaml.Media.IPolyQuadraticBezierSegment
    _classid_ = 'Microsoft.UI.Xaml.Media.PolyQuadraticBezierSegment'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.PolyQuadraticBezierSegment.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.PolyQuadraticBezierSegment: ...
    @winrt_mixinmethod
    def get_Points(self: win32more.Microsoft.UI.Xaml.Media.IPolyQuadraticBezierSegment) -> win32more.Microsoft.UI.Xaml.Media.PointCollection: ...
    @winrt_mixinmethod
    def put_Points(self: win32more.Microsoft.UI.Xaml.Media.IPolyQuadraticBezierSegment, value: win32more.Microsoft.UI.Xaml.Media.PointCollection) -> Void: ...
    @winrt_classmethod
    def get_PointsProperty(cls: win32more.Microsoft.UI.Xaml.Media.IPolyQuadraticBezierSegmentStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Points = property(get_Points, put_Points)
    _PolyQuadraticBezierSegment_Meta_.PointsProperty = property(get_PointsProperty, None)
class Projection(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Media.IProjection
    _classid_ = 'Microsoft.UI.Xaml.Media.Projection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.Projection.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Media.IProjectionFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.Projection: ...
class _QuadraticBezierSegment_Meta_(ComPtr.__class__):
    pass
class QuadraticBezierSegment(ComPtr, metaclass=_QuadraticBezierSegment_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.PathSegment
    default_interface: win32more.Microsoft.UI.Xaml.Media.IQuadraticBezierSegment
    _classid_ = 'Microsoft.UI.Xaml.Media.QuadraticBezierSegment'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.QuadraticBezierSegment.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.QuadraticBezierSegment: ...
    @winrt_mixinmethod
    def get_Point1(self: win32more.Microsoft.UI.Xaml.Media.IQuadraticBezierSegment) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Point1(self: win32more.Microsoft.UI.Xaml.Media.IQuadraticBezierSegment, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_Point2(self: win32more.Microsoft.UI.Xaml.Media.IQuadraticBezierSegment) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Point2(self: win32more.Microsoft.UI.Xaml.Media.IQuadraticBezierSegment, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_classmethod
    def get_Point1Property(cls: win32more.Microsoft.UI.Xaml.Media.IQuadraticBezierSegmentStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_Point2Property(cls: win32more.Microsoft.UI.Xaml.Media.IQuadraticBezierSegmentStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Point1 = property(get_Point1, put_Point1)
    Point2 = property(get_Point2, put_Point2)
    _QuadraticBezierSegment_Meta_.Point1Property = property(get_Point1Property, None)
    _QuadraticBezierSegment_Meta_.Point2Property = property(get_Point2Property, None)
class _RadialGradientBrush_Meta_(ComPtr.__class__):
    pass
class RadialGradientBrush(ComPtr, metaclass=_RadialGradientBrush_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.XamlCompositionBrushBase
    default_interface: win32more.Microsoft.UI.Xaml.Media.IRadialGradientBrush
    _classid_ = 'Microsoft.UI.Xaml.Media.RadialGradientBrush'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.RadialGradientBrush.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Media.IRadialGradientBrushFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.RadialGradientBrush: ...
    @winrt_mixinmethod
    def get_Center(self: win32more.Microsoft.UI.Xaml.Media.IRadialGradientBrush) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Center(self: win32more.Microsoft.UI.Xaml.Media.IRadialGradientBrush, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_RadiusX(self: win32more.Microsoft.UI.Xaml.Media.IRadialGradientBrush) -> Double: ...
    @winrt_mixinmethod
    def put_RadiusX(self: win32more.Microsoft.UI.Xaml.Media.IRadialGradientBrush, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RadiusY(self: win32more.Microsoft.UI.Xaml.Media.IRadialGradientBrush) -> Double: ...
    @winrt_mixinmethod
    def put_RadiusY(self: win32more.Microsoft.UI.Xaml.Media.IRadialGradientBrush, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_GradientOrigin(self: win32more.Microsoft.UI.Xaml.Media.IRadialGradientBrush) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_GradientOrigin(self: win32more.Microsoft.UI.Xaml.Media.IRadialGradientBrush, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_MappingMode(self: win32more.Microsoft.UI.Xaml.Media.IRadialGradientBrush) -> win32more.Microsoft.UI.Xaml.Media.BrushMappingMode: ...
    @winrt_mixinmethod
    def put_MappingMode(self: win32more.Microsoft.UI.Xaml.Media.IRadialGradientBrush, value: win32more.Microsoft.UI.Xaml.Media.BrushMappingMode) -> Void: ...
    @winrt_mixinmethod
    def get_InterpolationSpace(self: win32more.Microsoft.UI.Xaml.Media.IRadialGradientBrush) -> win32more.Microsoft.UI.Composition.CompositionColorSpace: ...
    @winrt_mixinmethod
    def put_InterpolationSpace(self: win32more.Microsoft.UI.Xaml.Media.IRadialGradientBrush, value: win32more.Microsoft.UI.Composition.CompositionColorSpace) -> Void: ...
    @winrt_mixinmethod
    def get_SpreadMethod(self: win32more.Microsoft.UI.Xaml.Media.IRadialGradientBrush) -> win32more.Microsoft.UI.Xaml.Media.GradientSpreadMethod: ...
    @winrt_mixinmethod
    def put_SpreadMethod(self: win32more.Microsoft.UI.Xaml.Media.IRadialGradientBrush, value: win32more.Microsoft.UI.Xaml.Media.GradientSpreadMethod) -> Void: ...
    @winrt_mixinmethod
    def get_GradientStops(self: win32more.Microsoft.UI.Xaml.Media.IRadialGradientBrush) -> win32more.Windows.Foundation.Collections.IObservableVector[win32more.Microsoft.UI.Xaml.Media.GradientStop]: ...
    @winrt_classmethod
    def get_CenterProperty(cls: win32more.Microsoft.UI.Xaml.Media.IRadialGradientBrushStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RadiusXProperty(cls: win32more.Microsoft.UI.Xaml.Media.IRadialGradientBrushStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RadiusYProperty(cls: win32more.Microsoft.UI.Xaml.Media.IRadialGradientBrushStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_GradientOriginProperty(cls: win32more.Microsoft.UI.Xaml.Media.IRadialGradientBrushStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_InterpolationSpaceProperty(cls: win32more.Microsoft.UI.Xaml.Media.IRadialGradientBrushStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MappingModeProperty(cls: win32more.Microsoft.UI.Xaml.Media.IRadialGradientBrushStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SpreadMethodProperty(cls: win32more.Microsoft.UI.Xaml.Media.IRadialGradientBrushStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Center = property(get_Center, put_Center)
    GradientOrigin = property(get_GradientOrigin, put_GradientOrigin)
    GradientStops = property(get_GradientStops, None)
    InterpolationSpace = property(get_InterpolationSpace, put_InterpolationSpace)
    MappingMode = property(get_MappingMode, put_MappingMode)
    RadiusX = property(get_RadiusX, put_RadiusX)
    RadiusY = property(get_RadiusY, put_RadiusY)
    SpreadMethod = property(get_SpreadMethod, put_SpreadMethod)
    _RadialGradientBrush_Meta_.CenterProperty = property(get_CenterProperty, None)
    _RadialGradientBrush_Meta_.GradientOriginProperty = property(get_GradientOriginProperty, None)
    _RadialGradientBrush_Meta_.InterpolationSpaceProperty = property(get_InterpolationSpaceProperty, None)
    _RadialGradientBrush_Meta_.MappingModeProperty = property(get_MappingModeProperty, None)
    _RadialGradientBrush_Meta_.RadiusXProperty = property(get_RadiusXProperty, None)
    _RadialGradientBrush_Meta_.RadiusYProperty = property(get_RadiusYProperty, None)
    _RadialGradientBrush_Meta_.SpreadMethodProperty = property(get_SpreadMethodProperty, None)
class _RectangleGeometry_Meta_(ComPtr.__class__):
    pass
class RectangleGeometry(ComPtr, metaclass=_RectangleGeometry_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Geometry
    default_interface: win32more.Microsoft.UI.Xaml.Media.IRectangleGeometry
    _classid_ = 'Microsoft.UI.Xaml.Media.RectangleGeometry'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.RectangleGeometry.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.RectangleGeometry: ...
    @winrt_mixinmethod
    def get_Rect(self: win32more.Microsoft.UI.Xaml.Media.IRectangleGeometry) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def put_Rect(self: win32more.Microsoft.UI.Xaml.Media.IRectangleGeometry, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_classmethod
    def get_RectProperty(cls: win32more.Microsoft.UI.Xaml.Media.IRectangleGeometryStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Rect = property(get_Rect, put_Rect)
    _RectangleGeometry_Meta_.RectProperty = property(get_RectProperty, None)
class RenderedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Media.IRenderedEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Media.RenderedEventArgs'
    @winrt_mixinmethod
    def get_FrameDuration(self: win32more.Microsoft.UI.Xaml.Media.IRenderedEventArgs) -> win32more.Windows.Foundation.TimeSpan: ...
    FrameDuration = property(get_FrameDuration, None)
class RenderingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Media.IRenderingEventArgs
    _classid_ = 'Microsoft.UI.Xaml.Media.RenderingEventArgs'
    @winrt_mixinmethod
    def get_RenderingTime(self: win32more.Microsoft.UI.Xaml.Media.IRenderingEventArgs) -> win32more.Windows.Foundation.TimeSpan: ...
    RenderingTime = property(get_RenderingTime, None)
class _RotateTransform_Meta_(ComPtr.__class__):
    pass
class RotateTransform(ComPtr, metaclass=_RotateTransform_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Transform
    default_interface: win32more.Microsoft.UI.Xaml.Media.IRotateTransform
    _classid_ = 'Microsoft.UI.Xaml.Media.RotateTransform'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.RotateTransform.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.RotateTransform: ...
    @winrt_mixinmethod
    def get_CenterX(self: win32more.Microsoft.UI.Xaml.Media.IRotateTransform) -> Double: ...
    @winrt_mixinmethod
    def put_CenterX(self: win32more.Microsoft.UI.Xaml.Media.IRotateTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_CenterY(self: win32more.Microsoft.UI.Xaml.Media.IRotateTransform) -> Double: ...
    @winrt_mixinmethod
    def put_CenterY(self: win32more.Microsoft.UI.Xaml.Media.IRotateTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Angle(self: win32more.Microsoft.UI.Xaml.Media.IRotateTransform) -> Double: ...
    @winrt_mixinmethod
    def put_Angle(self: win32more.Microsoft.UI.Xaml.Media.IRotateTransform, value: Double) -> Void: ...
    @winrt_classmethod
    def get_CenterXProperty(cls: win32more.Microsoft.UI.Xaml.Media.IRotateTransformStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CenterYProperty(cls: win32more.Microsoft.UI.Xaml.Media.IRotateTransformStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AngleProperty(cls: win32more.Microsoft.UI.Xaml.Media.IRotateTransformStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Angle = property(get_Angle, put_Angle)
    CenterX = property(get_CenterX, put_CenterX)
    CenterY = property(get_CenterY, put_CenterY)
    _RotateTransform_Meta_.AngleProperty = property(get_AngleProperty, None)
    _RotateTransform_Meta_.CenterXProperty = property(get_CenterXProperty, None)
    _RotateTransform_Meta_.CenterYProperty = property(get_CenterYProperty, None)
class _ScaleTransform_Meta_(ComPtr.__class__):
    pass
class ScaleTransform(ComPtr, metaclass=_ScaleTransform_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Transform
    default_interface: win32more.Microsoft.UI.Xaml.Media.IScaleTransform
    _classid_ = 'Microsoft.UI.Xaml.Media.ScaleTransform'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.ScaleTransform.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.ScaleTransform: ...
    @winrt_mixinmethod
    def get_CenterX(self: win32more.Microsoft.UI.Xaml.Media.IScaleTransform) -> Double: ...
    @winrt_mixinmethod
    def put_CenterX(self: win32more.Microsoft.UI.Xaml.Media.IScaleTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_CenterY(self: win32more.Microsoft.UI.Xaml.Media.IScaleTransform) -> Double: ...
    @winrt_mixinmethod
    def put_CenterY(self: win32more.Microsoft.UI.Xaml.Media.IScaleTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleX(self: win32more.Microsoft.UI.Xaml.Media.IScaleTransform) -> Double: ...
    @winrt_mixinmethod
    def put_ScaleX(self: win32more.Microsoft.UI.Xaml.Media.IScaleTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleY(self: win32more.Microsoft.UI.Xaml.Media.IScaleTransform) -> Double: ...
    @winrt_mixinmethod
    def put_ScaleY(self: win32more.Microsoft.UI.Xaml.Media.IScaleTransform, value: Double) -> Void: ...
    @winrt_classmethod
    def get_CenterXProperty(cls: win32more.Microsoft.UI.Xaml.Media.IScaleTransformStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CenterYProperty(cls: win32more.Microsoft.UI.Xaml.Media.IScaleTransformStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ScaleXProperty(cls: win32more.Microsoft.UI.Xaml.Media.IScaleTransformStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ScaleYProperty(cls: win32more.Microsoft.UI.Xaml.Media.IScaleTransformStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    CenterX = property(get_CenterX, put_CenterX)
    CenterY = property(get_CenterY, put_CenterY)
    ScaleX = property(get_ScaleX, put_ScaleX)
    ScaleY = property(get_ScaleY, put_ScaleY)
    _ScaleTransform_Meta_.CenterXProperty = property(get_CenterXProperty, None)
    _ScaleTransform_Meta_.CenterYProperty = property(get_CenterYProperty, None)
    _ScaleTransform_Meta_.ScaleXProperty = property(get_ScaleXProperty, None)
    _ScaleTransform_Meta_.ScaleYProperty = property(get_ScaleYProperty, None)
class Shadow(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Media.IShadow
    _classid_ = 'Microsoft.UI.Xaml.Media.Shadow'
class _SkewTransform_Meta_(ComPtr.__class__):
    pass
class SkewTransform(ComPtr, metaclass=_SkewTransform_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Transform
    default_interface: win32more.Microsoft.UI.Xaml.Media.ISkewTransform
    _classid_ = 'Microsoft.UI.Xaml.Media.SkewTransform'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.SkewTransform.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.SkewTransform: ...
    @winrt_mixinmethod
    def get_CenterX(self: win32more.Microsoft.UI.Xaml.Media.ISkewTransform) -> Double: ...
    @winrt_mixinmethod
    def put_CenterX(self: win32more.Microsoft.UI.Xaml.Media.ISkewTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_CenterY(self: win32more.Microsoft.UI.Xaml.Media.ISkewTransform) -> Double: ...
    @winrt_mixinmethod
    def put_CenterY(self: win32more.Microsoft.UI.Xaml.Media.ISkewTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_AngleX(self: win32more.Microsoft.UI.Xaml.Media.ISkewTransform) -> Double: ...
    @winrt_mixinmethod
    def put_AngleX(self: win32more.Microsoft.UI.Xaml.Media.ISkewTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_AngleY(self: win32more.Microsoft.UI.Xaml.Media.ISkewTransform) -> Double: ...
    @winrt_mixinmethod
    def put_AngleY(self: win32more.Microsoft.UI.Xaml.Media.ISkewTransform, value: Double) -> Void: ...
    @winrt_classmethod
    def get_CenterXProperty(cls: win32more.Microsoft.UI.Xaml.Media.ISkewTransformStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CenterYProperty(cls: win32more.Microsoft.UI.Xaml.Media.ISkewTransformStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AngleXProperty(cls: win32more.Microsoft.UI.Xaml.Media.ISkewTransformStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AngleYProperty(cls: win32more.Microsoft.UI.Xaml.Media.ISkewTransformStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    AngleX = property(get_AngleX, put_AngleX)
    AngleY = property(get_AngleY, put_AngleY)
    CenterX = property(get_CenterX, put_CenterX)
    CenterY = property(get_CenterY, put_CenterY)
    _SkewTransform_Meta_.AngleXProperty = property(get_AngleXProperty, None)
    _SkewTransform_Meta_.AngleYProperty = property(get_AngleYProperty, None)
    _SkewTransform_Meta_.CenterXProperty = property(get_CenterXProperty, None)
    _SkewTransform_Meta_.CenterYProperty = property(get_CenterYProperty, None)
class _SolidColorBrush_Meta_(ComPtr.__class__):
    pass
class SolidColorBrush(ComPtr, metaclass=_SolidColorBrush_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Brush
    default_interface: win32more.Microsoft.UI.Xaml.Media.ISolidColorBrush
    _classid_ = 'Microsoft.UI.Xaml.Media.SolidColorBrush'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.SolidColorBrush.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.SolidColorBrush.CreateInstanceWithColor(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.SolidColorBrush: ...
    @winrt_factorymethod
    def CreateInstanceWithColor(cls: win32more.Microsoft.UI.Xaml.Media.ISolidColorBrushFactory, color: win32more.Windows.UI.Color) -> win32more.Microsoft.UI.Xaml.Media.SolidColorBrush: ...
    @winrt_mixinmethod
    def get_Color(self: win32more.Microsoft.UI.Xaml.Media.ISolidColorBrush) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: win32more.Microsoft.UI.Xaml.Media.ISolidColorBrush, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_classmethod
    def get_ColorProperty(cls: win32more.Microsoft.UI.Xaml.Media.ISolidColorBrushStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Color = property(get_Color, put_Color)
    _SolidColorBrush_Meta_.ColorProperty = property(get_ColorProperty, None)
class Stretch(Enum, Int32):
    None_ = 0
    Fill = 1
    Uniform = 2
    UniformToFill = 3
class StyleSimulations(Enum, Int32):
    None_ = 0
    BoldSimulation = 1
    ItalicSimulation = 2
    BoldItalicSimulation = 3
class SweepDirection(Enum, Int32):
    Counterclockwise = 0
    Clockwise = 1
class SystemBackdrop(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Media.ISystemBackdrop
    _classid_ = 'Microsoft.UI.Xaml.Media.SystemBackdrop'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.SystemBackdrop.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Media.ISystemBackdropFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.SystemBackdrop: ...
    @winrt_mixinmethod
    def GetDefaultSystemBackdropConfiguration(self: win32more.Microsoft.UI.Xaml.Media.ISystemBackdrop, target: win32more.Microsoft.UI.Composition.ICompositionSupportsSystemBackdrop, xamlRoot: win32more.Microsoft.UI.Xaml.XamlRoot) -> win32more.Microsoft.UI.Composition.SystemBackdrops.SystemBackdropConfiguration: ...
    @winrt_mixinmethod
    def OnTargetConnected(self: win32more.Microsoft.UI.Xaml.Media.ISystemBackdropOverrides, connectedTarget: win32more.Microsoft.UI.Composition.ICompositionSupportsSystemBackdrop, xamlRoot: win32more.Microsoft.UI.Xaml.XamlRoot) -> Void: ...
    @winrt_mixinmethod
    def OnTargetDisconnected(self: win32more.Microsoft.UI.Xaml.Media.ISystemBackdropOverrides, disconnectedTarget: win32more.Microsoft.UI.Composition.ICompositionSupportsSystemBackdrop) -> Void: ...
    @winrt_mixinmethod
    def OnDefaultSystemBackdropConfigurationChanged(self: win32more.Microsoft.UI.Xaml.Media.ISystemBackdropOverrides, target: win32more.Microsoft.UI.Composition.ICompositionSupportsSystemBackdrop, xamlRoot: win32more.Microsoft.UI.Xaml.XamlRoot) -> Void: ...
class ThemeShadow(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Media.Shadow
    default_interface: win32more.Microsoft.UI.Xaml.Media.IThemeShadow
    _classid_ = 'Microsoft.UI.Xaml.Media.ThemeShadow'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.ThemeShadow.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Media.IThemeShadowFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.ThemeShadow: ...
    @winrt_mixinmethod
    def get_Receivers(self: win32more.Microsoft.UI.Xaml.Media.IThemeShadow) -> win32more.Microsoft.UI.Xaml.UIElementWeakCollection: ...
    Receivers = property(get_Receivers, None)
class _TileBrush_Meta_(ComPtr.__class__):
    pass
class TileBrush(ComPtr, metaclass=_TileBrush_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Brush
    default_interface: win32more.Microsoft.UI.Xaml.Media.ITileBrush
    _classid_ = 'Microsoft.UI.Xaml.Media.TileBrush'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.TileBrush.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Media.ITileBrushFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.TileBrush: ...
    @winrt_mixinmethod
    def get_AlignmentX(self: win32more.Microsoft.UI.Xaml.Media.ITileBrush) -> win32more.Microsoft.UI.Xaml.Media.AlignmentX: ...
    @winrt_mixinmethod
    def put_AlignmentX(self: win32more.Microsoft.UI.Xaml.Media.ITileBrush, value: win32more.Microsoft.UI.Xaml.Media.AlignmentX) -> Void: ...
    @winrt_mixinmethod
    def get_AlignmentY(self: win32more.Microsoft.UI.Xaml.Media.ITileBrush) -> win32more.Microsoft.UI.Xaml.Media.AlignmentY: ...
    @winrt_mixinmethod
    def put_AlignmentY(self: win32more.Microsoft.UI.Xaml.Media.ITileBrush, value: win32more.Microsoft.UI.Xaml.Media.AlignmentY) -> Void: ...
    @winrt_mixinmethod
    def get_Stretch(self: win32more.Microsoft.UI.Xaml.Media.ITileBrush) -> win32more.Microsoft.UI.Xaml.Media.Stretch: ...
    @winrt_mixinmethod
    def put_Stretch(self: win32more.Microsoft.UI.Xaml.Media.ITileBrush, value: win32more.Microsoft.UI.Xaml.Media.Stretch) -> Void: ...
    @winrt_classmethod
    def get_AlignmentXProperty(cls: win32more.Microsoft.UI.Xaml.Media.ITileBrushStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AlignmentYProperty(cls: win32more.Microsoft.UI.Xaml.Media.ITileBrushStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StretchProperty(cls: win32more.Microsoft.UI.Xaml.Media.ITileBrushStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    AlignmentX = property(get_AlignmentX, put_AlignmentX)
    AlignmentY = property(get_AlignmentY, put_AlignmentY)
    Stretch = property(get_Stretch, put_Stretch)
    _TileBrush_Meta_.AlignmentXProperty = property(get_AlignmentXProperty, None)
    _TileBrush_Meta_.AlignmentYProperty = property(get_AlignmentYProperty, None)
    _TileBrush_Meta_.StretchProperty = property(get_StretchProperty, None)
class Transform(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Media.GeneralTransform
    default_interface: win32more.Microsoft.UI.Xaml.Media.ITransform
    _classid_ = 'Microsoft.UI.Xaml.Media.Transform'
class TransformCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Microsoft.UI.Xaml.Media.Transform]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Transform]
    _classid_ = 'Microsoft.UI.Xaml.Media.TransformCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.TransformCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.TransformCollection: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Transform], index: UInt32) -> win32more.Microsoft.UI.Xaml.Media.Transform: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Transform]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Transform]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.UI.Xaml.Media.Transform]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Transform], value: win32more.Microsoft.UI.Xaml.Media.Transform, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Transform], index: UInt32, value: win32more.Microsoft.UI.Xaml.Media.Transform) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Transform], index: UInt32, value: win32more.Microsoft.UI.Xaml.Media.Transform) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Transform], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Transform], value: win32more.Microsoft.UI.Xaml.Media.Transform) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Transform]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Transform]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Transform], startIndex: UInt32, items: FillArray[win32more.Microsoft.UI.Xaml.Media.Transform]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Microsoft.UI.Xaml.Media.Transform], items: PassArray[win32more.Microsoft.UI.Xaml.Media.Transform]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Xaml.Media.Transform]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Microsoft.UI.Xaml.Media.Transform]: ...
    Size = property(get_Size, None)
class _TransformGroup_Meta_(ComPtr.__class__):
    pass
class TransformGroup(ComPtr, metaclass=_TransformGroup_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Transform
    default_interface: win32more.Microsoft.UI.Xaml.Media.ITransformGroup
    _classid_ = 'Microsoft.UI.Xaml.Media.TransformGroup'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.TransformGroup.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.TransformGroup: ...
    @winrt_mixinmethod
    def get_Children(self: win32more.Microsoft.UI.Xaml.Media.ITransformGroup) -> win32more.Microsoft.UI.Xaml.Media.TransformCollection: ...
    @winrt_mixinmethod
    def put_Children(self: win32more.Microsoft.UI.Xaml.Media.ITransformGroup, value: win32more.Microsoft.UI.Xaml.Media.TransformCollection) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Microsoft.UI.Xaml.Media.ITransformGroup) -> win32more.Microsoft.UI.Xaml.Media.Matrix: ...
    @winrt_classmethod
    def get_ChildrenProperty(cls: win32more.Microsoft.UI.Xaml.Media.ITransformGroupStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Children = property(get_Children, put_Children)
    Value = property(get_Value, None)
    _TransformGroup_Meta_.ChildrenProperty = property(get_ChildrenProperty, None)
class _TranslateTransform_Meta_(ComPtr.__class__):
    pass
class TranslateTransform(ComPtr, metaclass=_TranslateTransform_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Transform
    default_interface: win32more.Microsoft.UI.Xaml.Media.ITranslateTransform
    _classid_ = 'Microsoft.UI.Xaml.Media.TranslateTransform'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.TranslateTransform.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Media.TranslateTransform: ...
    @winrt_mixinmethod
    def get_X(self: win32more.Microsoft.UI.Xaml.Media.ITranslateTransform) -> Double: ...
    @winrt_mixinmethod
    def put_X(self: win32more.Microsoft.UI.Xaml.Media.ITranslateTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Y(self: win32more.Microsoft.UI.Xaml.Media.ITranslateTransform) -> Double: ...
    @winrt_mixinmethod
    def put_Y(self: win32more.Microsoft.UI.Xaml.Media.ITranslateTransform, value: Double) -> Void: ...
    @winrt_classmethod
    def get_XProperty(cls: win32more.Microsoft.UI.Xaml.Media.ITranslateTransformStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_YProperty(cls: win32more.Microsoft.UI.Xaml.Media.ITranslateTransformStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    X = property(get_X, put_X)
    Y = property(get_Y, put_Y)
    _TranslateTransform_Meta_.XProperty = property(get_XProperty, None)
    _TranslateTransform_Meta_.YProperty = property(get_YProperty, None)
class VisualTreeHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Microsoft.UI.Xaml.Media.IVisualTreeHelper
    _classid_ = 'Microsoft.UI.Xaml.Media.VisualTreeHelper'
    @winrt_classmethod
    def FindElementsInHostCoordinatesPoint(cls: win32more.Microsoft.UI.Xaml.Media.IVisualTreeHelperStatics, intersectingPoint: win32more.Windows.Foundation.Point, subtree: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Xaml.UIElement]: ...
    @winrt_classmethod
    def FindElementsInHostCoordinatesRect(cls: win32more.Microsoft.UI.Xaml.Media.IVisualTreeHelperStatics, intersectingRect: win32more.Windows.Foundation.Rect, subtree: win32more.Microsoft.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Xaml.UIElement]: ...
    @winrt_classmethod
    def FindAllElementsInHostCoordinatesPoint(cls: win32more.Microsoft.UI.Xaml.Media.IVisualTreeHelperStatics, intersectingPoint: win32more.Windows.Foundation.Point, subtree: win32more.Microsoft.UI.Xaml.UIElement, includeAllElements: Boolean) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Xaml.UIElement]: ...
    @winrt_classmethod
    def FindAllElementsInHostCoordinatesRect(cls: win32more.Microsoft.UI.Xaml.Media.IVisualTreeHelperStatics, intersectingRect: win32more.Windows.Foundation.Rect, subtree: win32more.Microsoft.UI.Xaml.UIElement, includeAllElements: Boolean) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Microsoft.UI.Xaml.UIElement]: ...
    @winrt_classmethod
    def GetChild(cls: win32more.Microsoft.UI.Xaml.Media.IVisualTreeHelperStatics, reference: win32more.Microsoft.UI.Xaml.DependencyObject, childIndex: Int32) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_classmethod
    def GetChildrenCount(cls: win32more.Microsoft.UI.Xaml.Media.IVisualTreeHelperStatics, reference: win32more.Microsoft.UI.Xaml.DependencyObject) -> Int32: ...
    @winrt_classmethod
    def GetParent(cls: win32more.Microsoft.UI.Xaml.Media.IVisualTreeHelperStatics, reference: win32more.Microsoft.UI.Xaml.DependencyObject) -> win32more.Microsoft.UI.Xaml.DependencyObject: ...
    @winrt_classmethod
    def DisconnectChildrenRecursive(cls: win32more.Microsoft.UI.Xaml.Media.IVisualTreeHelperStatics, element: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_classmethod
    def GetOpenPopups(cls: win32more.Microsoft.UI.Xaml.Media.IVisualTreeHelperStatics, window: win32more.Microsoft.UI.Xaml.Window) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.UI.Xaml.Controls.Primitives.Popup]: ...
    @winrt_classmethod
    def GetOpenPopupsForXamlRoot(cls: win32more.Microsoft.UI.Xaml.Media.IVisualTreeHelperStatics, xamlRoot: win32more.Microsoft.UI.Xaml.XamlRoot) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Microsoft.UI.Xaml.Controls.Primitives.Popup]: ...
class _XamlCompositionBrushBase_Meta_(ComPtr.__class__):
    pass
class XamlCompositionBrushBase(ComPtr, metaclass=_XamlCompositionBrushBase_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Media.Brush
    default_interface: win32more.Microsoft.UI.Xaml.Media.IXamlCompositionBrushBase
    _classid_ = 'Microsoft.UI.Xaml.Media.XamlCompositionBrushBase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.XamlCompositionBrushBase.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Media.IXamlCompositionBrushBaseFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.XamlCompositionBrushBase: ...
    @winrt_mixinmethod
    def get_FallbackColor(self: win32more.Microsoft.UI.Xaml.Media.IXamlCompositionBrushBase) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_FallbackColor(self: win32more.Microsoft.UI.Xaml.Media.IXamlCompositionBrushBase, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_CompositionBrush(self: win32more.Microsoft.UI.Xaml.Media.IXamlCompositionBrushBaseProtected) -> win32more.Microsoft.UI.Composition.CompositionBrush: ...
    @winrt_mixinmethod
    def put_CompositionBrush(self: win32more.Microsoft.UI.Xaml.Media.IXamlCompositionBrushBaseProtected, value: win32more.Microsoft.UI.Composition.CompositionBrush) -> Void: ...
    @winrt_mixinmethod
    def OnConnected(self: win32more.Microsoft.UI.Xaml.Media.IXamlCompositionBrushBaseOverrides) -> Void: ...
    @winrt_mixinmethod
    def OnDisconnected(self: win32more.Microsoft.UI.Xaml.Media.IXamlCompositionBrushBaseOverrides) -> Void: ...
    @winrt_classmethod
    def get_FallbackColorProperty(cls: win32more.Microsoft.UI.Xaml.Media.IXamlCompositionBrushBaseStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    CompositionBrush = property(get_CompositionBrush, put_CompositionBrush)
    FallbackColor = property(get_FallbackColor, put_FallbackColor)
    _XamlCompositionBrushBase_Meta_.FallbackColorProperty = property(get_FallbackColorProperty, None)
class XamlLight(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.DependencyObject
    default_interface: win32more.Microsoft.UI.Xaml.Media.IXamlLight
    _classid_ = 'Microsoft.UI.Xaml.Media.XamlLight'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Media.XamlLight.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Media.IXamlLightFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Media.XamlLight: ...
    @winrt_mixinmethod
    def get_CompositionLight(self: win32more.Microsoft.UI.Xaml.Media.IXamlLightProtected) -> win32more.Microsoft.UI.Composition.CompositionLight: ...
    @winrt_mixinmethod
    def put_CompositionLight(self: win32more.Microsoft.UI.Xaml.Media.IXamlLightProtected, value: win32more.Microsoft.UI.Composition.CompositionLight) -> Void: ...
    @winrt_mixinmethod
    def GetId(self: win32more.Microsoft.UI.Xaml.Media.IXamlLightOverrides) -> WinRT_String: ...
    @winrt_mixinmethod
    def OnConnected(self: win32more.Microsoft.UI.Xaml.Media.IXamlLightOverrides, newElement: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def OnDisconnected(self: win32more.Microsoft.UI.Xaml.Media.IXamlLightOverrides, oldElement: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_classmethod
    def AddTargetElement(cls: win32more.Microsoft.UI.Xaml.Media.IXamlLightStatics, lightId: WinRT_String, element: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_classmethod
    def RemoveTargetElement(cls: win32more.Microsoft.UI.Xaml.Media.IXamlLightStatics, lightId: WinRT_String, element: win32more.Microsoft.UI.Xaml.UIElement) -> Void: ...
    @winrt_classmethod
    def AddTargetBrush(cls: win32more.Microsoft.UI.Xaml.Media.IXamlLightStatics, lightId: WinRT_String, brush: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_classmethod
    def RemoveTargetBrush(cls: win32more.Microsoft.UI.Xaml.Media.IXamlLightStatics, lightId: WinRT_String, brush: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    CompositionLight = property(get_CompositionLight, put_CompositionLight)


make_ready(__name__)
