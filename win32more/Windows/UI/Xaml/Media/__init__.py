from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Media.Playback
import win32more.Windows.Storage.Streams
import win32more.Windows.UI
import win32more.Windows.UI.Composition
import win32more.Windows.UI.Xaml
import win32more.Windows.UI.Xaml.Controls.Primitives
import win32more.Windows.UI.Xaml.Media
import win32more.Windows.UI.Xaml.Media.Media3D
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.WinRT
class AcrylicBackgroundSource(Enum, Int32):
    HostBackdrop = 0
    Backdrop = 1
class _AcrylicBrush_Meta_(ComPtr.__class__):
    pass
class AcrylicBrush(ComPtr, metaclass=_AcrylicBrush_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.XamlCompositionBrushBase
    default_interface: win32more.Windows.UI.Xaml.Media.IAcrylicBrush
    _classid_ = 'Windows.UI.Xaml.Media.AcrylicBrush'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.AcrylicBrush.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Media.IAcrylicBrushFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.AcrylicBrush: ...
    @winrt_mixinmethod
    def get_BackgroundSource(self: win32more.Windows.UI.Xaml.Media.IAcrylicBrush) -> win32more.Windows.UI.Xaml.Media.AcrylicBackgroundSource: ...
    @winrt_mixinmethod
    def put_BackgroundSource(self: win32more.Windows.UI.Xaml.Media.IAcrylicBrush, value: win32more.Windows.UI.Xaml.Media.AcrylicBackgroundSource) -> Void: ...
    @winrt_mixinmethod
    def get_TintColor(self: win32more.Windows.UI.Xaml.Media.IAcrylicBrush) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_TintColor(self: win32more.Windows.UI.Xaml.Media.IAcrylicBrush, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_TintOpacity(self: win32more.Windows.UI.Xaml.Media.IAcrylicBrush) -> Double: ...
    @winrt_mixinmethod
    def put_TintOpacity(self: win32more.Windows.UI.Xaml.Media.IAcrylicBrush, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_TintTransitionDuration(self: win32more.Windows.UI.Xaml.Media.IAcrylicBrush) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_TintTransitionDuration(self: win32more.Windows.UI.Xaml.Media.IAcrylicBrush, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_AlwaysUseFallback(self: win32more.Windows.UI.Xaml.Media.IAcrylicBrush) -> Boolean: ...
    @winrt_mixinmethod
    def put_AlwaysUseFallback(self: win32more.Windows.UI.Xaml.Media.IAcrylicBrush, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_TintLuminosityOpacity(self: win32more.Windows.UI.Xaml.Media.IAcrylicBrush2) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def put_TintLuminosityOpacity(self: win32more.Windows.UI.Xaml.Media.IAcrylicBrush2, value: win32more.Windows.Foundation.IReference[Double]) -> Void: ...
    @winrt_classmethod
    def get_TintLuminosityOpacityProperty(cls: win32more.Windows.UI.Xaml.Media.IAcrylicBrushStatics2) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_BackgroundSourceProperty(cls: win32more.Windows.UI.Xaml.Media.IAcrylicBrushStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TintColorProperty(cls: win32more.Windows.UI.Xaml.Media.IAcrylicBrushStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TintOpacityProperty(cls: win32more.Windows.UI.Xaml.Media.IAcrylicBrushStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TintTransitionDurationProperty(cls: win32more.Windows.UI.Xaml.Media.IAcrylicBrushStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AlwaysUseFallbackProperty(cls: win32more.Windows.UI.Xaml.Media.IAcrylicBrushStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    AlwaysUseFallback = property(get_AlwaysUseFallback, put_AlwaysUseFallback)
    BackgroundSource = property(get_BackgroundSource, put_BackgroundSource)
    TintColor = property(get_TintColor, put_TintColor)
    TintLuminosityOpacity = property(get_TintLuminosityOpacity, put_TintLuminosityOpacity)
    TintOpacity = property(get_TintOpacity, put_TintOpacity)
    TintTransitionDuration = property(get_TintTransitionDuration, put_TintTransitionDuration)
    _AcrylicBrush_Meta_.AlwaysUseFallbackProperty = property(get_AlwaysUseFallbackProperty, None)
    _AcrylicBrush_Meta_.BackgroundSourceProperty = property(get_BackgroundSourceProperty, None)
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
    extends: win32more.Windows.UI.Xaml.Media.PathSegment
    default_interface: win32more.Windows.UI.Xaml.Media.IArcSegment
    _classid_ = 'Windows.UI.Xaml.Media.ArcSegment'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.ArcSegment.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.ArcSegment: ...
    @winrt_mixinmethod
    def get_Point(self: win32more.Windows.UI.Xaml.Media.IArcSegment) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Point(self: win32more.Windows.UI.Xaml.Media.IArcSegment, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.UI.Xaml.Media.IArcSegment) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def put_Size(self: win32more.Windows.UI.Xaml.Media.IArcSegment, value: win32more.Windows.Foundation.Size) -> Void: ...
    @winrt_mixinmethod
    def get_RotationAngle(self: win32more.Windows.UI.Xaml.Media.IArcSegment) -> Double: ...
    @winrt_mixinmethod
    def put_RotationAngle(self: win32more.Windows.UI.Xaml.Media.IArcSegment, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_IsLargeArc(self: win32more.Windows.UI.Xaml.Media.IArcSegment) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsLargeArc(self: win32more.Windows.UI.Xaml.Media.IArcSegment, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_SweepDirection(self: win32more.Windows.UI.Xaml.Media.IArcSegment) -> win32more.Windows.UI.Xaml.Media.SweepDirection: ...
    @winrt_mixinmethod
    def put_SweepDirection(self: win32more.Windows.UI.Xaml.Media.IArcSegment, value: win32more.Windows.UI.Xaml.Media.SweepDirection) -> Void: ...
    @winrt_classmethod
    def get_PointProperty(cls: win32more.Windows.UI.Xaml.Media.IArcSegmentStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SizeProperty(cls: win32more.Windows.UI.Xaml.Media.IArcSegmentStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RotationAngleProperty(cls: win32more.Windows.UI.Xaml.Media.IArcSegmentStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsLargeArcProperty(cls: win32more.Windows.UI.Xaml.Media.IArcSegmentStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SweepDirectionProperty(cls: win32more.Windows.UI.Xaml.Media.IArcSegmentStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
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
class AudioCategory(Enum, Int32):
    Other = 0
    ForegroundOnlyMedia = 1
    BackgroundCapableMedia = 2
    Communications = 3
    Alerts = 4
    SoundEffects = 5
    GameEffects = 6
    GameMedia = 7
    GameChat = 8
    Speech = 9
    Movie = 10
    Media = 11
class AudioDeviceType(Enum, Int32):
    Console = 0
    Multimedia = 1
    Communications = 2
class _BezierSegment_Meta_(ComPtr.__class__):
    pass
class BezierSegment(ComPtr, metaclass=_BezierSegment_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.PathSegment
    default_interface: win32more.Windows.UI.Xaml.Media.IBezierSegment
    _classid_ = 'Windows.UI.Xaml.Media.BezierSegment'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.BezierSegment.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.BezierSegment: ...
    @winrt_mixinmethod
    def get_Point1(self: win32more.Windows.UI.Xaml.Media.IBezierSegment) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Point1(self: win32more.Windows.UI.Xaml.Media.IBezierSegment, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_Point2(self: win32more.Windows.UI.Xaml.Media.IBezierSegment) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Point2(self: win32more.Windows.UI.Xaml.Media.IBezierSegment, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_Point3(self: win32more.Windows.UI.Xaml.Media.IBezierSegment) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Point3(self: win32more.Windows.UI.Xaml.Media.IBezierSegment, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_classmethod
    def get_Point1Property(cls: win32more.Windows.UI.Xaml.Media.IBezierSegmentStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_Point2Property(cls: win32more.Windows.UI.Xaml.Media.IBezierSegmentStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_Point3Property(cls: win32more.Windows.UI.Xaml.Media.IBezierSegmentStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Point1 = property(get_Point1, put_Point1)
    Point2 = property(get_Point2, put_Point2)
    Point3 = property(get_Point3, put_Point3)
    _BezierSegment_Meta_.Point1Property = property(get_Point1Property, None)
    _BezierSegment_Meta_.Point2Property = property(get_Point2Property, None)
    _BezierSegment_Meta_.Point3Property = property(get_Point3Property, None)
class BitmapCache(ComPtr):
    extends: win32more.Windows.UI.Xaml.Media.CacheMode
    default_interface: win32more.Windows.UI.Xaml.Media.IBitmapCache
    _classid_ = 'Windows.UI.Xaml.Media.BitmapCache'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.BitmapCache.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.BitmapCache: ...
class _Brush_Meta_(ComPtr.__class__):
    pass
class Brush(ComPtr, metaclass=_Brush_Meta_):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Media.IBrush
    _classid_ = 'Windows.UI.Xaml.Media.Brush'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Brush.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Media.IBrushFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def get_Opacity(self: win32more.Windows.UI.Xaml.Media.IBrush) -> Double: ...
    @winrt_mixinmethod
    def put_Opacity(self: win32more.Windows.UI.Xaml.Media.IBrush, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Transform(self: win32more.Windows.UI.Xaml.Media.IBrush) -> win32more.Windows.UI.Xaml.Media.Transform: ...
    @winrt_mixinmethod
    def put_Transform(self: win32more.Windows.UI.Xaml.Media.IBrush, value: win32more.Windows.UI.Xaml.Media.Transform) -> Void: ...
    @winrt_mixinmethod
    def get_RelativeTransform(self: win32more.Windows.UI.Xaml.Media.IBrush) -> win32more.Windows.UI.Xaml.Media.Transform: ...
    @winrt_mixinmethod
    def put_RelativeTransform(self: win32more.Windows.UI.Xaml.Media.IBrush, value: win32more.Windows.UI.Xaml.Media.Transform) -> Void: ...
    @winrt_mixinmethod
    def PopulatePropertyInfoOverride(self: win32more.Windows.UI.Xaml.Media.IBrushOverrides2, propertyName: WinRT_String, animationPropertyInfo: win32more.Windows.UI.Composition.AnimationPropertyInfo) -> Void: ...
    @winrt_mixinmethod
    def PopulatePropertyInfo(self: win32more.Windows.UI.Composition.IAnimationObject, propertyName: WinRT_String, propertyInfo: win32more.Windows.UI.Composition.AnimationPropertyInfo) -> Void: ...
    @winrt_classmethod
    def get_OpacityProperty(cls: win32more.Windows.UI.Xaml.Media.IBrushStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TransformProperty(cls: win32more.Windows.UI.Xaml.Media.IBrushStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RelativeTransformProperty(cls: win32more.Windows.UI.Xaml.Media.IBrushStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Opacity = property(get_Opacity, put_Opacity)
    RelativeTransform = property(get_RelativeTransform, put_RelativeTransform)
    Transform = property(get_Transform, put_Transform)
    _Brush_Meta_.OpacityProperty = property(get_OpacityProperty, None)
    _Brush_Meta_.RelativeTransformProperty = property(get_RelativeTransformProperty, None)
    _Brush_Meta_.TransformProperty = property(get_TransformProperty, None)
class BrushCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Windows.UI.Xaml.Media.Brush]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Brush]
    _classid_ = 'Windows.UI.Xaml.Media.BrushCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.BrushCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.BrushCollection: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Brush], index: UInt32) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Brush]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Brush]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.Media.Brush]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Brush], value: win32more.Windows.UI.Xaml.Media.Brush, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Brush], index: UInt32, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Brush], index: UInt32, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Brush], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Brush], value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Brush]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Brush]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Brush], startIndex: UInt32, items: FillArray[win32more.Windows.UI.Xaml.Media.Brush]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Brush], items: PassArray[win32more.Windows.UI.Xaml.Media.Brush]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.Media.Brush]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.UI.Xaml.Media.Brush]: ...
    Size = property(get_Size, None)
class BrushMappingMode(Enum, Int32):
    Absolute = 0
    RelativeToBoundingBox = 1
class CacheMode(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Media.ICacheMode
    _classid_ = 'Windows.UI.Xaml.Media.CacheMode'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.CacheMode.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Media.ICacheModeFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.CacheMode: ...
class ColorInterpolationMode(Enum, Int32):
    ScRgbLinearInterpolation = 0
    SRgbLinearInterpolation = 1
class _CompositeTransform_Meta_(ComPtr.__class__):
    pass
class CompositeTransform(ComPtr, metaclass=_CompositeTransform_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Transform
    default_interface: win32more.Windows.UI.Xaml.Media.ICompositeTransform
    _classid_ = 'Windows.UI.Xaml.Media.CompositeTransform'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.CompositeTransform.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.CompositeTransform: ...
    @winrt_mixinmethod
    def get_CenterX(self: win32more.Windows.UI.Xaml.Media.ICompositeTransform) -> Double: ...
    @winrt_mixinmethod
    def put_CenterX(self: win32more.Windows.UI.Xaml.Media.ICompositeTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_CenterY(self: win32more.Windows.UI.Xaml.Media.ICompositeTransform) -> Double: ...
    @winrt_mixinmethod
    def put_CenterY(self: win32more.Windows.UI.Xaml.Media.ICompositeTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleX(self: win32more.Windows.UI.Xaml.Media.ICompositeTransform) -> Double: ...
    @winrt_mixinmethod
    def put_ScaleX(self: win32more.Windows.UI.Xaml.Media.ICompositeTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleY(self: win32more.Windows.UI.Xaml.Media.ICompositeTransform) -> Double: ...
    @winrt_mixinmethod
    def put_ScaleY(self: win32more.Windows.UI.Xaml.Media.ICompositeTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_SkewX(self: win32more.Windows.UI.Xaml.Media.ICompositeTransform) -> Double: ...
    @winrt_mixinmethod
    def put_SkewX(self: win32more.Windows.UI.Xaml.Media.ICompositeTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_SkewY(self: win32more.Windows.UI.Xaml.Media.ICompositeTransform) -> Double: ...
    @winrt_mixinmethod
    def put_SkewY(self: win32more.Windows.UI.Xaml.Media.ICompositeTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Rotation(self: win32more.Windows.UI.Xaml.Media.ICompositeTransform) -> Double: ...
    @winrt_mixinmethod
    def put_Rotation(self: win32more.Windows.UI.Xaml.Media.ICompositeTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_TranslateX(self: win32more.Windows.UI.Xaml.Media.ICompositeTransform) -> Double: ...
    @winrt_mixinmethod
    def put_TranslateX(self: win32more.Windows.UI.Xaml.Media.ICompositeTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_TranslateY(self: win32more.Windows.UI.Xaml.Media.ICompositeTransform) -> Double: ...
    @winrt_mixinmethod
    def put_TranslateY(self: win32more.Windows.UI.Xaml.Media.ICompositeTransform, value: Double) -> Void: ...
    @winrt_classmethod
    def get_CenterXProperty(cls: win32more.Windows.UI.Xaml.Media.ICompositeTransformStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CenterYProperty(cls: win32more.Windows.UI.Xaml.Media.ICompositeTransformStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ScaleXProperty(cls: win32more.Windows.UI.Xaml.Media.ICompositeTransformStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ScaleYProperty(cls: win32more.Windows.UI.Xaml.Media.ICompositeTransformStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SkewXProperty(cls: win32more.Windows.UI.Xaml.Media.ICompositeTransformStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_SkewYProperty(cls: win32more.Windows.UI.Xaml.Media.ICompositeTransformStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RotationProperty(cls: win32more.Windows.UI.Xaml.Media.ICompositeTransformStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TranslateXProperty(cls: win32more.Windows.UI.Xaml.Media.ICompositeTransformStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TranslateYProperty(cls: win32more.Windows.UI.Xaml.Media.ICompositeTransformStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
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
    default_interface: win32more.Windows.UI.Xaml.Media.ICompositionTarget
    _classid_ = 'Windows.UI.Xaml.Media.CompositionTarget'
    @winrt_classmethod
    def add_Rendered(cls: win32more.Windows.UI.Xaml.Media.ICompositionTargetStatics3, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.UI.Xaml.Media.RenderedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_Rendered(cls: win32more.Windows.UI.Xaml.Media.ICompositionTargetStatics3, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_Rendering(cls: win32more.Windows.UI.Xaml.Media.ICompositionTargetStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_Rendering(cls: win32more.Windows.UI.Xaml.Media.ICompositionTargetStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def add_SurfaceContentsLost(cls: win32more.Windows.UI.Xaml.Media.ICompositionTargetStatics, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_classmethod
    def remove_SurfaceContentsLost(cls: win32more.Windows.UI.Xaml.Media.ICompositionTargetStatics, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
class DoubleCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[Double]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[Double]
    _classid_ = 'Windows.UI.Xaml.Media.DoubleCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.DoubleCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.DoubleCollection: ...
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
    extends: win32more.Windows.UI.Xaml.Media.Geometry
    default_interface: win32more.Windows.UI.Xaml.Media.IEllipseGeometry
    _classid_ = 'Windows.UI.Xaml.Media.EllipseGeometry'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.EllipseGeometry.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.EllipseGeometry: ...
    @winrt_mixinmethod
    def get_Center(self: win32more.Windows.UI.Xaml.Media.IEllipseGeometry) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Center(self: win32more.Windows.UI.Xaml.Media.IEllipseGeometry, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_RadiusX(self: win32more.Windows.UI.Xaml.Media.IEllipseGeometry) -> Double: ...
    @winrt_mixinmethod
    def put_RadiusX(self: win32more.Windows.UI.Xaml.Media.IEllipseGeometry, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RadiusY(self: win32more.Windows.UI.Xaml.Media.IEllipseGeometry) -> Double: ...
    @winrt_mixinmethod
    def put_RadiusY(self: win32more.Windows.UI.Xaml.Media.IEllipseGeometry, value: Double) -> Void: ...
    @winrt_classmethod
    def get_CenterProperty(cls: win32more.Windows.UI.Xaml.Media.IEllipseGeometryStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RadiusXProperty(cls: win32more.Windows.UI.Xaml.Media.IEllipseGeometryStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RadiusYProperty(cls: win32more.Windows.UI.Xaml.Media.IEllipseGeometryStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
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
    default_interface: win32more.Windows.UI.Xaml.Media.IFontFamily
    _classid_ = 'Windows.UI.Xaml.Media.FontFamily'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.FontFamily.CreateInstanceWithName(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstanceWithName(cls: win32more.Windows.UI.Xaml.Media.IFontFamilyFactory, familyName: WinRT_String, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.FontFamily: ...
    @winrt_mixinmethod
    def get_Source(self: win32more.Windows.UI.Xaml.Media.IFontFamily) -> WinRT_String: ...
    @winrt_classmethod
    def get_XamlAutoFontFamily(cls: win32more.Windows.UI.Xaml.Media.IFontFamilyStatics2) -> win32more.Windows.UI.Xaml.Media.FontFamily: ...
    Source = property(get_Source, None)
    _FontFamily_Meta_.XamlAutoFontFamily = property(get_XamlAutoFontFamily, None)
class GeneralTransform(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Media.IGeneralTransform
    _classid_ = 'Windows.UI.Xaml.Media.GeneralTransform'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.GeneralTransform.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Media.IGeneralTransformFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.GeneralTransform: ...
    @winrt_mixinmethod
    def get_Inverse(self: win32more.Windows.UI.Xaml.Media.IGeneralTransform) -> win32more.Windows.UI.Xaml.Media.GeneralTransform: ...
    @winrt_mixinmethod
    def TransformPoint(self: win32more.Windows.UI.Xaml.Media.IGeneralTransform, point: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def TryTransform(self: win32more.Windows.UI.Xaml.Media.IGeneralTransform, inPoint: win32more.Windows.Foundation.Point, outPoint: POINTER(win32more.Windows.Foundation.Point)) -> Boolean: ...
    @winrt_mixinmethod
    def TransformBounds(self: win32more.Windows.UI.Xaml.Media.IGeneralTransform, rect: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def get_InverseCore(self: win32more.Windows.UI.Xaml.Media.IGeneralTransformOverrides) -> win32more.Windows.UI.Xaml.Media.GeneralTransform: ...
    @winrt_mixinmethod
    def TryTransformCore(self: win32more.Windows.UI.Xaml.Media.IGeneralTransformOverrides, inPoint: win32more.Windows.Foundation.Point, outPoint: POINTER(win32more.Windows.Foundation.Point)) -> Boolean: ...
    @winrt_mixinmethod
    def TransformBoundsCore(self: win32more.Windows.UI.Xaml.Media.IGeneralTransformOverrides, rect: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.Rect: ...
    Inverse = property(get_Inverse, None)
    InverseCore = property(get_InverseCore, None)
class _Geometry_Meta_(ComPtr.__class__):
    pass
class Geometry(ComPtr, metaclass=_Geometry_Meta_):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Media.IGeometry
    _classid_ = 'Windows.UI.Xaml.Media.Geometry'
    @winrt_mixinmethod
    def get_Transform(self: win32more.Windows.UI.Xaml.Media.IGeometry) -> win32more.Windows.UI.Xaml.Media.Transform: ...
    @winrt_mixinmethod
    def put_Transform(self: win32more.Windows.UI.Xaml.Media.IGeometry, value: win32more.Windows.UI.Xaml.Media.Transform) -> Void: ...
    @winrt_mixinmethod
    def get_Bounds(self: win32more.Windows.UI.Xaml.Media.IGeometry) -> win32more.Windows.Foundation.Rect: ...
    @winrt_classmethod
    def get_Empty(cls: win32more.Windows.UI.Xaml.Media.IGeometryStatics) -> win32more.Windows.UI.Xaml.Media.Geometry: ...
    @winrt_classmethod
    def get_StandardFlatteningTolerance(cls: win32more.Windows.UI.Xaml.Media.IGeometryStatics) -> Double: ...
    @winrt_classmethod
    def get_TransformProperty(cls: win32more.Windows.UI.Xaml.Media.IGeometryStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Bounds = property(get_Bounds, None)
    Transform = property(get_Transform, put_Transform)
    _Geometry_Meta_.Empty = property(get_Empty, None)
    _Geometry_Meta_.StandardFlatteningTolerance = property(get_StandardFlatteningTolerance, None)
    _Geometry_Meta_.TransformProperty = property(get_TransformProperty, None)
class GeometryCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Windows.UI.Xaml.Media.Geometry]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Geometry]
    _classid_ = 'Windows.UI.Xaml.Media.GeometryCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.GeometryCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.GeometryCollection: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Geometry], index: UInt32) -> win32more.Windows.UI.Xaml.Media.Geometry: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Geometry]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Geometry]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.Media.Geometry]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Geometry], value: win32more.Windows.UI.Xaml.Media.Geometry, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Geometry], index: UInt32, value: win32more.Windows.UI.Xaml.Media.Geometry) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Geometry], index: UInt32, value: win32more.Windows.UI.Xaml.Media.Geometry) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Geometry], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Geometry], value: win32more.Windows.UI.Xaml.Media.Geometry) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Geometry]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Geometry]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Geometry], startIndex: UInt32, items: FillArray[win32more.Windows.UI.Xaml.Media.Geometry]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Geometry], items: PassArray[win32more.Windows.UI.Xaml.Media.Geometry]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.Media.Geometry]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.UI.Xaml.Media.Geometry]: ...
    Size = property(get_Size, None)
class _GeometryGroup_Meta_(ComPtr.__class__):
    pass
class GeometryGroup(ComPtr, metaclass=_GeometryGroup_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Geometry
    default_interface: win32more.Windows.UI.Xaml.Media.IGeometryGroup
    _classid_ = 'Windows.UI.Xaml.Media.GeometryGroup'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.GeometryGroup.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.GeometryGroup: ...
    @winrt_mixinmethod
    def get_FillRule(self: win32more.Windows.UI.Xaml.Media.IGeometryGroup) -> win32more.Windows.UI.Xaml.Media.FillRule: ...
    @winrt_mixinmethod
    def put_FillRule(self: win32more.Windows.UI.Xaml.Media.IGeometryGroup, value: win32more.Windows.UI.Xaml.Media.FillRule) -> Void: ...
    @winrt_mixinmethod
    def get_Children(self: win32more.Windows.UI.Xaml.Media.IGeometryGroup) -> win32more.Windows.UI.Xaml.Media.GeometryCollection: ...
    @winrt_mixinmethod
    def put_Children(self: win32more.Windows.UI.Xaml.Media.IGeometryGroup, value: win32more.Windows.UI.Xaml.Media.GeometryCollection) -> Void: ...
    @winrt_classmethod
    def get_FillRuleProperty(cls: win32more.Windows.UI.Xaml.Media.IGeometryGroupStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ChildrenProperty(cls: win32more.Windows.UI.Xaml.Media.IGeometryGroupStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Children = property(get_Children, put_Children)
    FillRule = property(get_FillRule, put_FillRule)
    _GeometryGroup_Meta_.ChildrenProperty = property(get_ChildrenProperty, None)
    _GeometryGroup_Meta_.FillRuleProperty = property(get_FillRuleProperty, None)
class _GradientBrush_Meta_(ComPtr.__class__):
    pass
class GradientBrush(ComPtr, metaclass=_GradientBrush_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Brush
    default_interface: win32more.Windows.UI.Xaml.Media.IGradientBrush
    _classid_ = 'Windows.UI.Xaml.Media.GradientBrush'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.GradientBrush.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Media.IGradientBrushFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.GradientBrush: ...
    @winrt_mixinmethod
    def get_SpreadMethod(self: win32more.Windows.UI.Xaml.Media.IGradientBrush) -> win32more.Windows.UI.Xaml.Media.GradientSpreadMethod: ...
    @winrt_mixinmethod
    def put_SpreadMethod(self: win32more.Windows.UI.Xaml.Media.IGradientBrush, value: win32more.Windows.UI.Xaml.Media.GradientSpreadMethod) -> Void: ...
    @winrt_mixinmethod
    def get_MappingMode(self: win32more.Windows.UI.Xaml.Media.IGradientBrush) -> win32more.Windows.UI.Xaml.Media.BrushMappingMode: ...
    @winrt_mixinmethod
    def put_MappingMode(self: win32more.Windows.UI.Xaml.Media.IGradientBrush, value: win32more.Windows.UI.Xaml.Media.BrushMappingMode) -> Void: ...
    @winrt_mixinmethod
    def get_ColorInterpolationMode(self: win32more.Windows.UI.Xaml.Media.IGradientBrush) -> win32more.Windows.UI.Xaml.Media.ColorInterpolationMode: ...
    @winrt_mixinmethod
    def put_ColorInterpolationMode(self: win32more.Windows.UI.Xaml.Media.IGradientBrush, value: win32more.Windows.UI.Xaml.Media.ColorInterpolationMode) -> Void: ...
    @winrt_mixinmethod
    def get_GradientStops(self: win32more.Windows.UI.Xaml.Media.IGradientBrush) -> win32more.Windows.UI.Xaml.Media.GradientStopCollection: ...
    @winrt_mixinmethod
    def put_GradientStops(self: win32more.Windows.UI.Xaml.Media.IGradientBrush, value: win32more.Windows.UI.Xaml.Media.GradientStopCollection) -> Void: ...
    @winrt_classmethod
    def get_SpreadMethodProperty(cls: win32more.Windows.UI.Xaml.Media.IGradientBrushStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_MappingModeProperty(cls: win32more.Windows.UI.Xaml.Media.IGradientBrushStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ColorInterpolationModeProperty(cls: win32more.Windows.UI.Xaml.Media.IGradientBrushStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_GradientStopsProperty(cls: win32more.Windows.UI.Xaml.Media.IGradientBrushStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
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
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Media.IGradientStop
    _classid_ = 'Windows.UI.Xaml.Media.GradientStop'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.GradientStop.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.GradientStop: ...
    @winrt_mixinmethod
    def get_Color(self: win32more.Windows.UI.Xaml.Media.IGradientStop) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: win32more.Windows.UI.Xaml.Media.IGradientStop, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_Offset(self: win32more.Windows.UI.Xaml.Media.IGradientStop) -> Double: ...
    @winrt_mixinmethod
    def put_Offset(self: win32more.Windows.UI.Xaml.Media.IGradientStop, value: Double) -> Void: ...
    @winrt_classmethod
    def get_ColorProperty(cls: win32more.Windows.UI.Xaml.Media.IGradientStopStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_OffsetProperty(cls: win32more.Windows.UI.Xaml.Media.IGradientStopStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Color = property(get_Color, put_Color)
    Offset = property(get_Offset, put_Offset)
    _GradientStop_Meta_.ColorProperty = property(get_ColorProperty, None)
    _GradientStop_Meta_.OffsetProperty = property(get_OffsetProperty, None)
class GradientStopCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Windows.UI.Xaml.Media.GradientStop]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.GradientStop]
    _classid_ = 'Windows.UI.Xaml.Media.GradientStopCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.GradientStopCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.GradientStopCollection: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.GradientStop], index: UInt32) -> win32more.Windows.UI.Xaml.Media.GradientStop: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.GradientStop]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.GradientStop]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.Media.GradientStop]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.GradientStop], value: win32more.Windows.UI.Xaml.Media.GradientStop, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.GradientStop], index: UInt32, value: win32more.Windows.UI.Xaml.Media.GradientStop) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.GradientStop], index: UInt32, value: win32more.Windows.UI.Xaml.Media.GradientStop) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.GradientStop], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.GradientStop], value: win32more.Windows.UI.Xaml.Media.GradientStop) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.GradientStop]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.GradientStop]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.GradientStop], startIndex: UInt32, items: FillArray[win32more.Windows.UI.Xaml.Media.GradientStop]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.GradientStop], items: PassArray[win32more.Windows.UI.Xaml.Media.GradientStop]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.Media.GradientStop]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.UI.Xaml.Media.GradientStop]: ...
    Size = property(get_Size, None)
class IAcrylicBrush(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IAcrylicBrush'
    _iid_ = Guid('{79bbcf4e-cd66-4f1b-a8b6-cd6d2977c18d}')
    @winrt_commethod(6)
    def get_BackgroundSource(self) -> win32more.Windows.UI.Xaml.Media.AcrylicBackgroundSource: ...
    @winrt_commethod(7)
    def put_BackgroundSource(self, value: win32more.Windows.UI.Xaml.Media.AcrylicBackgroundSource) -> Void: ...
    @winrt_commethod(8)
    def get_TintColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(9)
    def put_TintColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(10)
    def get_TintOpacity(self) -> Double: ...
    @winrt_commethod(11)
    def put_TintOpacity(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def get_TintTransitionDuration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(13)
    def put_TintTransitionDuration(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(14)
    def get_AlwaysUseFallback(self) -> Boolean: ...
    @winrt_commethod(15)
    def put_AlwaysUseFallback(self, value: Boolean) -> Void: ...
    AlwaysUseFallback = property(get_AlwaysUseFallback, put_AlwaysUseFallback)
    BackgroundSource = property(get_BackgroundSource, put_BackgroundSource)
    TintColor = property(get_TintColor, put_TintColor)
    TintOpacity = property(get_TintOpacity, put_TintOpacity)
    TintTransitionDuration = property(get_TintTransitionDuration, put_TintTransitionDuration)
class IAcrylicBrush2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IAcrylicBrush2'
    _iid_ = Guid('{c9645383-b19e-5ac0-86ff-3d90506dbcda}')
    @winrt_commethod(6)
    def get_TintLuminosityOpacity(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(7)
    def put_TintLuminosityOpacity(self, value: win32more.Windows.Foundation.IReference[Double]) -> Void: ...
    TintLuminosityOpacity = property(get_TintLuminosityOpacity, put_TintLuminosityOpacity)
class IAcrylicBrushFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IAcrylicBrushFactory'
    _iid_ = Guid('{81a32568-f6cc-4013-8363-928ae23b7a61}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.AcrylicBrush: ...
class IAcrylicBrushStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IAcrylicBrushStatics'
    _iid_ = Guid('{2787fd79-a3da-423f-b81a-599147971523}')
    @winrt_commethod(6)
    def get_BackgroundSourceProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_TintColorProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_TintOpacityProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_TintTransitionDurationProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_AlwaysUseFallbackProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    AlwaysUseFallbackProperty = property(get_AlwaysUseFallbackProperty, None)
    BackgroundSourceProperty = property(get_BackgroundSourceProperty, None)
    TintColorProperty = property(get_TintColorProperty, None)
    TintOpacityProperty = property(get_TintOpacityProperty, None)
    TintTransitionDurationProperty = property(get_TintTransitionDurationProperty, None)
class IAcrylicBrushStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IAcrylicBrushStatics2'
    _iid_ = Guid('{129188a8-bf11-5bbc-8445-8c510e5926c0}')
    @winrt_commethod(6)
    def get_TintLuminosityOpacityProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    TintLuminosityOpacityProperty = property(get_TintLuminosityOpacityProperty, None)
class IArcSegment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IArcSegment'
    _iid_ = Guid('{07940c5f-63fb-4469-91be-f1097c168052}')
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
    def get_SweepDirection(self) -> win32more.Windows.UI.Xaml.Media.SweepDirection: ...
    @winrt_commethod(15)
    def put_SweepDirection(self, value: win32more.Windows.UI.Xaml.Media.SweepDirection) -> Void: ...
    IsLargeArc = property(get_IsLargeArc, put_IsLargeArc)
    Point = property(get_Point, put_Point)
    RotationAngle = property(get_RotationAngle, put_RotationAngle)
    Size = property(get_Size, put_Size)
    SweepDirection = property(get_SweepDirection, put_SweepDirection)
class IArcSegmentStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IArcSegmentStatics'
    _iid_ = Guid('{82348f6e-8a69-4204-9c12-7207df317643}')
    @winrt_commethod(6)
    def get_PointProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_SizeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_RotationAngleProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_IsLargeArcProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_SweepDirectionProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    IsLargeArcProperty = property(get_IsLargeArcProperty, None)
    PointProperty = property(get_PointProperty, None)
    RotationAngleProperty = property(get_RotationAngleProperty, None)
    SizeProperty = property(get_SizeProperty, None)
    SweepDirectionProperty = property(get_SweepDirectionProperty, None)
class IBezierSegment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IBezierSegment'
    _iid_ = Guid('{af4bb9ee-8984-49b7-81df-3f35994b95eb}')
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
    _classid_ = 'Windows.UI.Xaml.Media.IBezierSegmentStatics'
    _iid_ = Guid('{c0287bac-1410-4530-8452-1c9d0ad1f341}')
    @winrt_commethod(6)
    def get_Point1Property(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_Point2Property(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_Point3Property(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Point1Property = property(get_Point1Property, None)
    Point2Property = property(get_Point2Property, None)
    Point3Property = property(get_Point3Property, None)
class IBitmapCache(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IBitmapCache'
    _iid_ = Guid('{79c2219e-44d2-4610-9735-9bec83809ecf}')
class IBrush(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IBrush'
    _iid_ = Guid('{8806a321-1e06-422c-a1cc-01696559e021}')
    @winrt_commethod(6)
    def get_Opacity(self) -> Double: ...
    @winrt_commethod(7)
    def put_Opacity(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_Transform(self) -> win32more.Windows.UI.Xaml.Media.Transform: ...
    @winrt_commethod(9)
    def put_Transform(self, value: win32more.Windows.UI.Xaml.Media.Transform) -> Void: ...
    @winrt_commethod(10)
    def get_RelativeTransform(self) -> win32more.Windows.UI.Xaml.Media.Transform: ...
    @winrt_commethod(11)
    def put_RelativeTransform(self, value: win32more.Windows.UI.Xaml.Media.Transform) -> Void: ...
    Opacity = property(get_Opacity, put_Opacity)
    RelativeTransform = property(get_RelativeTransform, put_RelativeTransform)
    Transform = property(get_Transform, put_Transform)
class IBrushFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IBrushFactory'
    _iid_ = Guid('{399658a2-14fb-4b8f-83e6-6e3dab12069b}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Brush: ...
class IBrushOverrides2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IBrushOverrides2'
    _iid_ = Guid('{d092b151-d83b-5a81-a71e-a1c7f8ad6963}')
    @winrt_commethod(6)
    def PopulatePropertyInfoOverride(self, propertyName: WinRT_String, animationPropertyInfo: win32more.Windows.UI.Composition.AnimationPropertyInfo) -> Void: ...
class IBrushStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IBrushStatics'
    _iid_ = Guid('{e70c3102-0225-47f5-b22e-0467619f6a22}')
    @winrt_commethod(6)
    def get_OpacityProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_TransformProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_RelativeTransformProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    OpacityProperty = property(get_OpacityProperty, None)
    RelativeTransformProperty = property(get_RelativeTransformProperty, None)
    TransformProperty = property(get_TransformProperty, None)
class ICacheMode(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ICacheMode'
    _iid_ = Guid('{98dc8b11-c6f9-4dab-b838-5fd5ec8c7350}')
class ICacheModeFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ICacheModeFactory'
    _iid_ = Guid('{eb1f8c5b-0abb-4e70-b8a8-620d0d953ab2}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.CacheMode: ...
class ICompositeTransform(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    Rotation = property(get_Rotation, put_Rotation)
    ScaleX = property(get_ScaleX, put_ScaleX)
    ScaleY = property(get_ScaleY, put_ScaleY)
    SkewX = property(get_SkewX, put_SkewX)
    SkewY = property(get_SkewY, put_SkewY)
    TranslateX = property(get_TranslateX, put_TranslateX)
    TranslateY = property(get_TranslateY, put_TranslateY)
class ICompositeTransformStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ICompositeTransformStatics'
    _iid_ = Guid('{2f190c08-8266-496f-9653-a18bd4f836aa}')
    @winrt_commethod(6)
    def get_CenterXProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_CenterYProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ScaleXProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_ScaleYProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_SkewXProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_SkewYProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_RotationProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_TranslateXProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_TranslateYProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
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
    _classid_ = 'Windows.UI.Xaml.Media.ICompositionTarget'
    _iid_ = Guid('{26cfbff0-713c-4bec-8803-e101f7b14ed3}')
class ICompositionTargetStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ICompositionTargetStatics'
    _iid_ = Guid('{2b1af03d-1ed2-4b59-bd00-7594ee92832b}')
    @winrt_commethod(6)
    def add_Rendering(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Rendering(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(8)
    def add_SurfaceContentsLost(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.Win32.System.WinRT.IInspectable]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_SurfaceContentsLost(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Rendering = event()
    SurfaceContentsLost = event()
class ICompositionTargetStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ICompositionTargetStatics3'
    _iid_ = Guid('{bc0a7cd9-6750-4708-994c-2028e0312ac8}')
    @winrt_commethod(6)
    def add_Rendered(self, handler: win32more.Windows.Foundation.EventHandler[win32more.Windows.UI.Xaml.Media.RenderedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(7)
    def remove_Rendered(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    Rendered = event()
class IEllipseGeometry(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IEllipseGeometry'
    _iid_ = Guid('{d4f61bba-4ea2-40d6-aa6c-8d38aa87651f}')
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
    _classid_ = 'Windows.UI.Xaml.Media.IEllipseGeometryStatics'
    _iid_ = Guid('{1744db47-f635-4b16-aee6-e052a65defb2}')
    @winrt_commethod(6)
    def get_CenterProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_RadiusXProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_RadiusYProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    CenterProperty = property(get_CenterProperty, None)
    RadiusXProperty = property(get_RadiusXProperty, None)
    RadiusYProperty = property(get_RadiusYProperty, None)
class IFontFamily(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IFontFamily'
    _iid_ = Guid('{92467e64-d66a-4cf4-9322-3d23b3c0c361}')
    @winrt_commethod(6)
    def get_Source(self) -> WinRT_String: ...
    Source = property(get_Source, None)
class IFontFamilyFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IFontFamilyFactory'
    _iid_ = Guid('{d5603377-3dae-4dcd-af09-f9498e9ec659}')
    @winrt_commethod(6)
    def CreateInstanceWithName(self, familyName: WinRT_String, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.FontFamily: ...
class IFontFamilyStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IFontFamilyStatics2'
    _iid_ = Guid('{52ad7af9-37e6-4297-a238-97fb6a408d9e}')
    @winrt_commethod(6)
    def get_XamlAutoFontFamily(self) -> win32more.Windows.UI.Xaml.Media.FontFamily: ...
    XamlAutoFontFamily = property(get_XamlAutoFontFamily, None)
class IGeneralTransform(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IGeneralTransform'
    _iid_ = Guid('{a06798b7-a2ec-415f-ade2-eade9333f2c7}')
    @winrt_commethod(6)
    def get_Inverse(self) -> win32more.Windows.UI.Xaml.Media.GeneralTransform: ...
    @winrt_commethod(7)
    def TransformPoint(self, point: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(8)
    def TryTransform(self, inPoint: win32more.Windows.Foundation.Point, outPoint: POINTER(win32more.Windows.Foundation.Point)) -> Boolean: ...
    @winrt_commethod(9)
    def TransformBounds(self, rect: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.Rect: ...
    Inverse = property(get_Inverse, None)
class IGeneralTransformFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IGeneralTransformFactory'
    _iid_ = Guid('{7a25c930-29c4-4e31-b6f9-dedd52e4df1b}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.GeneralTransform: ...
class IGeneralTransformOverrides(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IGeneralTransformOverrides'
    _iid_ = Guid('{4f121083-24cf-4524-90ad-8a42b1c12783}')
    @winrt_commethod(6)
    def get_InverseCore(self) -> win32more.Windows.UI.Xaml.Media.GeneralTransform: ...
    @winrt_commethod(7)
    def TryTransformCore(self, inPoint: win32more.Windows.Foundation.Point, outPoint: POINTER(win32more.Windows.Foundation.Point)) -> Boolean: ...
    @winrt_commethod(8)
    def TransformBoundsCore(self, rect: win32more.Windows.Foundation.Rect) -> win32more.Windows.Foundation.Rect: ...
    InverseCore = property(get_InverseCore, None)
class IGeometry(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IGeometry'
    _iid_ = Guid('{fa123889-0acd-417b-b62d-5ca1bf4dfc0e}')
    @winrt_commethod(6)
    def get_Transform(self) -> win32more.Windows.UI.Xaml.Media.Transform: ...
    @winrt_commethod(7)
    def put_Transform(self, value: win32more.Windows.UI.Xaml.Media.Transform) -> Void: ...
    @winrt_commethod(8)
    def get_Bounds(self) -> win32more.Windows.Foundation.Rect: ...
    Bounds = property(get_Bounds, None)
    Transform = property(get_Transform, put_Transform)
class IGeometryFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IGeometryFactory'
    _iid_ = Guid('{f65daf23-d5fd-42f9-b32a-929c5a4b54e1}')
class IGeometryGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IGeometryGroup'
    _iid_ = Guid('{55225a61-8677-4c8c-8e46-ee3dc355114b}')
    @winrt_commethod(6)
    def get_FillRule(self) -> win32more.Windows.UI.Xaml.Media.FillRule: ...
    @winrt_commethod(7)
    def put_FillRule(self, value: win32more.Windows.UI.Xaml.Media.FillRule) -> Void: ...
    @winrt_commethod(8)
    def get_Children(self) -> win32more.Windows.UI.Xaml.Media.GeometryCollection: ...
    @winrt_commethod(9)
    def put_Children(self, value: win32more.Windows.UI.Xaml.Media.GeometryCollection) -> Void: ...
    Children = property(get_Children, put_Children)
    FillRule = property(get_FillRule, put_FillRule)
class IGeometryGroupStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IGeometryGroupStatics'
    _iid_ = Guid('{56c955f4-8496-4bb6-abf0-617b1fe78b45}')
    @winrt_commethod(6)
    def get_FillRuleProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_ChildrenProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    ChildrenProperty = property(get_ChildrenProperty, None)
    FillRuleProperty = property(get_FillRuleProperty, None)
class IGeometryStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IGeometryStatics'
    _iid_ = Guid('{7a70aa8c-0b06-465f-b637-9a47e5a70111}')
    @winrt_commethod(6)
    def get_Empty(self) -> win32more.Windows.UI.Xaml.Media.Geometry: ...
    @winrt_commethod(7)
    def get_StandardFlatteningTolerance(self) -> Double: ...
    @winrt_commethod(8)
    def get_TransformProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Empty = property(get_Empty, None)
    StandardFlatteningTolerance = property(get_StandardFlatteningTolerance, None)
    TransformProperty = property(get_TransformProperty, None)
class IGradientBrush(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IGradientBrush'
    _iid_ = Guid('{2166e69f-935a-4191-8e3c-1c8dfdfcdc78}')
    @winrt_commethod(6)
    def get_SpreadMethod(self) -> win32more.Windows.UI.Xaml.Media.GradientSpreadMethod: ...
    @winrt_commethod(7)
    def put_SpreadMethod(self, value: win32more.Windows.UI.Xaml.Media.GradientSpreadMethod) -> Void: ...
    @winrt_commethod(8)
    def get_MappingMode(self) -> win32more.Windows.UI.Xaml.Media.BrushMappingMode: ...
    @winrt_commethod(9)
    def put_MappingMode(self, value: win32more.Windows.UI.Xaml.Media.BrushMappingMode) -> Void: ...
    @winrt_commethod(10)
    def get_ColorInterpolationMode(self) -> win32more.Windows.UI.Xaml.Media.ColorInterpolationMode: ...
    @winrt_commethod(11)
    def put_ColorInterpolationMode(self, value: win32more.Windows.UI.Xaml.Media.ColorInterpolationMode) -> Void: ...
    @winrt_commethod(12)
    def get_GradientStops(self) -> win32more.Windows.UI.Xaml.Media.GradientStopCollection: ...
    @winrt_commethod(13)
    def put_GradientStops(self, value: win32more.Windows.UI.Xaml.Media.GradientStopCollection) -> Void: ...
    ColorInterpolationMode = property(get_ColorInterpolationMode, put_ColorInterpolationMode)
    GradientStops = property(get_GradientStops, put_GradientStops)
    MappingMode = property(get_MappingMode, put_MappingMode)
    SpreadMethod = property(get_SpreadMethod, put_SpreadMethod)
class IGradientBrushFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IGradientBrushFactory'
    _iid_ = Guid('{ed4779ca-45bd-4131-b625-be86e07c6112}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.GradientBrush: ...
class IGradientBrushStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IGradientBrushStatics'
    _iid_ = Guid('{961661f9-8bb4-4e6c-b923-b5d787e0f1a9}')
    @winrt_commethod(6)
    def get_SpreadMethodProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_MappingModeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ColorInterpolationModeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_GradientStopsProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    ColorInterpolationModeProperty = property(get_ColorInterpolationModeProperty, None)
    GradientStopsProperty = property(get_GradientStopsProperty, None)
    MappingModeProperty = property(get_MappingModeProperty, None)
    SpreadMethodProperty = property(get_SpreadMethodProperty, None)
class IGradientStop(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IGradientStop'
    _iid_ = Guid('{665f44fe-2e59-4c4a-ab53-076a100ccd81}')
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
    _classid_ = 'Windows.UI.Xaml.Media.IGradientStopStatics'
    _iid_ = Guid('{602a6d75-6193-4fe5-8e82-c7c6f6febafd}')
    @winrt_commethod(6)
    def get_ColorProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_OffsetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    ColorProperty = property(get_ColorProperty, None)
    OffsetProperty = property(get_OffsetProperty, None)
class IImageBrush(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IImageBrush'
    _iid_ = Guid('{9fd11377-c12a-4493-bf7d-f3a8ad74b554}')
    @winrt_commethod(6)
    def get_ImageSource(self) -> win32more.Windows.UI.Xaml.Media.ImageSource: ...
    @winrt_commethod(7)
    def put_ImageSource(self, value: win32more.Windows.UI.Xaml.Media.ImageSource) -> Void: ...
    @winrt_commethod(8)
    def add_ImageFailed(self, handler: win32more.Windows.UI.Xaml.ExceptionRoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(9)
    def remove_ImageFailed(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_commethod(10)
    def add_ImageOpened(self, handler: win32more.Windows.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(11)
    def remove_ImageOpened(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    ImageSource = property(get_ImageSource, put_ImageSource)
    ImageFailed = event()
    ImageOpened = event()
class IImageBrushStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IImageBrushStatics'
    _iid_ = Guid('{1255b1b2-dd18-42e5-892c-eae30c305b8c}')
    @winrt_commethod(6)
    def get_ImageSourceProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    ImageSourceProperty = property(get_ImageSourceProperty, None)
class IImageSource(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IImageSource'
    _iid_ = Guid('{737ef309-ea41-4d96-a71c-98e98efcab07}')
class IImageSourceFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IImageSourceFactory'
    _iid_ = Guid('{297ec001-2540-4e5a-ab66-88035dd3ddb5}')
class ILineGeometry(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ILineGeometry'
    _iid_ = Guid('{30edd4a2-8fc5-40af-a7a2-c27fe7aa1363}')
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
    _classid_ = 'Windows.UI.Xaml.Media.ILineGeometryStatics'
    _iid_ = Guid('{578ae763-5562-4ee4-8703-ea4036d891e3}')
    @winrt_commethod(6)
    def get_StartPointProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_EndPointProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    EndPointProperty = property(get_EndPointProperty, None)
    StartPointProperty = property(get_StartPointProperty, None)
class ILineSegment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ILineSegment'
    _iid_ = Guid('{ef6a2e25-3ff0-4420-a411-7182a4cecb15}')
    @winrt_commethod(6)
    def get_Point(self) -> win32more.Windows.Foundation.Point: ...
    @winrt_commethod(7)
    def put_Point(self, value: win32more.Windows.Foundation.Point) -> Void: ...
    Point = property(get_Point, put_Point)
class ILineSegmentStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ILineSegmentStatics'
    _iid_ = Guid('{9fcab141-04c0-4afb-87b3-e800b969b894}')
    @winrt_commethod(6)
    def get_PointProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    PointProperty = property(get_PointProperty, None)
class ILinearGradientBrush(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ILinearGradientBrush'
    _iid_ = Guid('{8e96d16b-bb84-4c6f-9dbf-9d6c5c6d9c39}')
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
    _classid_ = 'Windows.UI.Xaml.Media.ILinearGradientBrushFactory'
    _iid_ = Guid('{0ae0861c-1e7a-4fed-9857-ea8caa798490}')
    @winrt_commethod(6)
    def CreateInstanceWithGradientStopCollectionAndAngle(self, gradientStopCollection: win32more.Windows.UI.Xaml.Media.GradientStopCollection, angle: Double) -> win32more.Windows.UI.Xaml.Media.LinearGradientBrush: ...
class ILinearGradientBrushStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ILinearGradientBrushStatics'
    _iid_ = Guid('{7af6e504-2dc3-40e3-be0b-b314c13cb991}')
    @winrt_commethod(6)
    def get_StartPointProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_EndPointProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    EndPointProperty = property(get_EndPointProperty, None)
    StartPointProperty = property(get_StartPointProperty, None)
class ILoadedImageSourceLoadCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ILoadedImageSourceLoadCompletedEventArgs'
    _iid_ = Guid('{1ac60b1e-7837-4489-b3e5-d0d5ad0a56c4}')
    @winrt_commethod(6)
    def get_Status(self) -> win32more.Windows.UI.Xaml.Media.LoadedImageSourceLoadStatus: ...
    Status = property(get_Status, None)
class ILoadedImageSurface(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ILoadedImageSurface'
    _iid_ = Guid('{050c8313-6737-45ba-8531-33094febef55}')
    @winrt_commethod(6)
    def get_DecodedPhysicalSize(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(7)
    def get_DecodedSize(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(8)
    def get_NaturalSize(self) -> win32more.Windows.Foundation.Size: ...
    @winrt_commethod(9)
    def add_LoadCompleted(self, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Media.LoadedImageSurface, win32more.Windows.UI.Xaml.Media.LoadedImageSourceLoadCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_commethod(10)
    def remove_LoadCompleted(self, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    DecodedPhysicalSize = property(get_DecodedPhysicalSize, None)
    DecodedSize = property(get_DecodedSize, None)
    NaturalSize = property(get_NaturalSize, None)
    LoadCompleted = event()
class ILoadedImageSurfaceStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ILoadedImageSurfaceStatics'
    _iid_ = Guid('{22b8edf6-84ad-40ab-937d-4871613e765d}')
    @winrt_commethod(6)
    def StartLoadFromUriWithSize(self, uri: win32more.Windows.Foundation.Uri, desiredMaxSize: win32more.Windows.Foundation.Size) -> win32more.Windows.UI.Xaml.Media.LoadedImageSurface: ...
    @winrt_commethod(7)
    def StartLoadFromUri(self, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.UI.Xaml.Media.LoadedImageSurface: ...
    @winrt_commethod(8)
    def StartLoadFromStreamWithSize(self, stream: win32more.Windows.Storage.Streams.IRandomAccessStream, desiredMaxSize: win32more.Windows.Foundation.Size) -> win32more.Windows.UI.Xaml.Media.LoadedImageSurface: ...
    @winrt_commethod(9)
    def StartLoadFromStream(self, stream: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.UI.Xaml.Media.LoadedImageSurface: ...
class IMatrix3DProjection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IMatrix3DProjection'
    _iid_ = Guid('{6f03e149-bfc9-4c01-b578-50338cec97fc}')
    @winrt_commethod(6)
    def get_ProjectionMatrix(self) -> win32more.Windows.UI.Xaml.Media.Media3D.Matrix3D: ...
    @winrt_commethod(7)
    def put_ProjectionMatrix(self, value: win32more.Windows.UI.Xaml.Media.Media3D.Matrix3D) -> Void: ...
    ProjectionMatrix = property(get_ProjectionMatrix, put_ProjectionMatrix)
class IMatrix3DProjectionStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IMatrix3DProjectionStatics'
    _iid_ = Guid('{ae9d5895-41ec-4e37-abaa-69f41d2f876b}')
    @winrt_commethod(6)
    def get_ProjectionMatrixProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    ProjectionMatrixProperty = property(get_ProjectionMatrixProperty, None)
class IMatrixHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IMatrixHelper'
    _iid_ = Guid('{f3cf4882-06b5-48c8-9eb2-1763e9364038}')
class IMatrixHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IMatrixHelperStatics'
    _iid_ = Guid('{c18606a6-39f4-4b8a-8403-28e5e5f033b4}')
    @winrt_commethod(6)
    def get_Identity(self) -> win32more.Windows.UI.Xaml.Media.Matrix: ...
    @winrt_commethod(7)
    def FromElements(self, m11: Double, m12: Double, m21: Double, m22: Double, offsetX: Double, offsetY: Double) -> win32more.Windows.UI.Xaml.Media.Matrix: ...
    @winrt_commethod(8)
    def GetIsIdentity(self, target: win32more.Windows.UI.Xaml.Media.Matrix) -> Boolean: ...
    @winrt_commethod(9)
    def Transform(self, target: win32more.Windows.UI.Xaml.Media.Matrix, point: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.Point: ...
    Identity = property(get_Identity, None)
class IMatrixTransform(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IMatrixTransform'
    _iid_ = Guid('{edfdd551-5fed-45fc-ae62-92a4b6cf9707}')
    @winrt_commethod(6)
    def get_Matrix(self) -> win32more.Windows.UI.Xaml.Media.Matrix: ...
    @winrt_commethod(7)
    def put_Matrix(self, value: win32more.Windows.UI.Xaml.Media.Matrix) -> Void: ...
    Matrix = property(get_Matrix, put_Matrix)
class IMatrixTransformStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IMatrixTransformStatics'
    _iid_ = Guid('{43e02e47-15b8-4758-bb97-7d52420acc5b}')
    @winrt_commethod(6)
    def get_MatrixProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    MatrixProperty = property(get_MatrixProperty, None)
class IMediaTransportControlsThumbnailRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IMediaTransportControlsThumbnailRequestedEventArgs'
    _iid_ = Guid('{e4a8b21c-e3c2-485c-ae69-f1537b76755a}')
    @winrt_commethod(6)
    def SetThumbnailImage(self, source: win32more.Windows.Storage.Streams.IInputStream) -> Void: ...
    @winrt_commethod(7)
    def GetDeferral(self) -> win32more.Windows.Foundation.Deferral: ...
class IPartialMediaFailureDetectedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IPartialMediaFailureDetectedEventArgs'
    _iid_ = Guid('{02b65a91-e5a1-442b-88d3-2dc127bfc59b}')
    @winrt_commethod(6)
    def get_StreamKind(self) -> win32more.Windows.Media.Playback.FailedMediaStreamKind: ...
    StreamKind = property(get_StreamKind, None)
class IPartialMediaFailureDetectedEventArgs2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IPartialMediaFailureDetectedEventArgs2'
    _iid_ = Guid('{73074875-890d-416b-b9ae-e84dfd9c4b1b}')
    @winrt_commethod(6)
    def get_ExtendedError(self) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
class IPathFigure(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IPathFigure'
    _iid_ = Guid('{5d955c8c-5fa9-4dda-a3cc-10fcdcaa20d7}')
    @winrt_commethod(6)
    def get_Segments(self) -> win32more.Windows.UI.Xaml.Media.PathSegmentCollection: ...
    @winrt_commethod(7)
    def put_Segments(self, value: win32more.Windows.UI.Xaml.Media.PathSegmentCollection) -> Void: ...
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
    _classid_ = 'Windows.UI.Xaml.Media.IPathFigureStatics'
    _iid_ = Guid('{b60591d9-2395-4317-9552-3a58526f8c7b}')
    @winrt_commethod(6)
    def get_SegmentsProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_StartPointProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_IsClosedProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_IsFilledProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    IsClosedProperty = property(get_IsClosedProperty, None)
    IsFilledProperty = property(get_IsFilledProperty, None)
    SegmentsProperty = property(get_SegmentsProperty, None)
    StartPointProperty = property(get_StartPointProperty, None)
class IPathGeometry(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IPathGeometry'
    _iid_ = Guid('{081b9df8-bae6-4bcb-813c-bde0e46dc8b7}')
    @winrt_commethod(6)
    def get_FillRule(self) -> win32more.Windows.UI.Xaml.Media.FillRule: ...
    @winrt_commethod(7)
    def put_FillRule(self, value: win32more.Windows.UI.Xaml.Media.FillRule) -> Void: ...
    @winrt_commethod(8)
    def get_Figures(self) -> win32more.Windows.UI.Xaml.Media.PathFigureCollection: ...
    @winrt_commethod(9)
    def put_Figures(self, value: win32more.Windows.UI.Xaml.Media.PathFigureCollection) -> Void: ...
    Figures = property(get_Figures, put_Figures)
    FillRule = property(get_FillRule, put_FillRule)
class IPathGeometryStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IPathGeometryStatics'
    _iid_ = Guid('{d9e58bba-2cba-4741-8f8d-3198cf5186b9}')
    @winrt_commethod(6)
    def get_FillRuleProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_FiguresProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    FiguresProperty = property(get_FiguresProperty, None)
    FillRuleProperty = property(get_FillRuleProperty, None)
class IPathSegment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IPathSegment'
    _iid_ = Guid('{fcfa71cf-9ce3-474f-8157-10b6435a616b}')
class IPathSegmentFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IPathSegmentFactory'
    _iid_ = Guid('{2a1c0aae-eccd-4464-a148-6ffdb3aa281f}')
class IPlaneProjection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    def get_ProjectionMatrix(self) -> win32more.Windows.UI.Xaml.Media.Media3D.Matrix3D: ...
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
    _classid_ = 'Windows.UI.Xaml.Media.IPlaneProjectionStatics'
    _iid_ = Guid('{ad919c67-3bdc-4855-8969-d1f9a3adc27d}')
    @winrt_commethod(6)
    def get_LocalOffsetXProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_LocalOffsetYProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_LocalOffsetZProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_RotationXProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_RotationYProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_RotationZProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_CenterOfRotationXProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_CenterOfRotationYProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_CenterOfRotationZProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_GlobalOffsetXProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def get_GlobalOffsetYProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(17)
    def get_GlobalOffsetZProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(18)
    def get_ProjectionMatrixProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
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
    _classid_ = 'Windows.UI.Xaml.Media.IPolyBezierSegment'
    _iid_ = Guid('{36805271-38c4-4bcf-96cd-028a6d38af25}')
    @winrt_commethod(6)
    def get_Points(self) -> win32more.Windows.UI.Xaml.Media.PointCollection: ...
    @winrt_commethod(7)
    def put_Points(self, value: win32more.Windows.UI.Xaml.Media.PointCollection) -> Void: ...
    Points = property(get_Points, put_Points)
class IPolyBezierSegmentStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IPolyBezierSegmentStatics'
    _iid_ = Guid('{1d91a6da-1492-4acc-bd66-a496f3d829d6}')
    @winrt_commethod(6)
    def get_PointsProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    PointsProperty = property(get_PointsProperty, None)
class IPolyLineSegment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IPolyLineSegment'
    _iid_ = Guid('{4b397f87-a2e6-479d-bdc8-6f4464646887}')
    @winrt_commethod(6)
    def get_Points(self) -> win32more.Windows.UI.Xaml.Media.PointCollection: ...
    @winrt_commethod(7)
    def put_Points(self, value: win32more.Windows.UI.Xaml.Media.PointCollection) -> Void: ...
    Points = property(get_Points, put_Points)
class IPolyLineSegmentStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IPolyLineSegmentStatics'
    _iid_ = Guid('{d64a2c87-33f1-4e70-a47f-b4981ef648a2}')
    @winrt_commethod(6)
    def get_PointsProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    PointsProperty = property(get_PointsProperty, None)
class IPolyQuadraticBezierSegment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IPolyQuadraticBezierSegment'
    _iid_ = Guid('{dd5ced7d-e6db-4c96-b6a1-3fce96e987a6}')
    @winrt_commethod(6)
    def get_Points(self) -> win32more.Windows.UI.Xaml.Media.PointCollection: ...
    @winrt_commethod(7)
    def put_Points(self, value: win32more.Windows.UI.Xaml.Media.PointCollection) -> Void: ...
    Points = property(get_Points, put_Points)
class IPolyQuadraticBezierSegmentStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IPolyQuadraticBezierSegmentStatics'
    _iid_ = Guid('{fdf5eb75-7ad5-4c89-8169-8c9786abd9eb}')
    @winrt_commethod(6)
    def get_PointsProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    PointsProperty = property(get_PointsProperty, None)
class IProjection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IProjection'
    _iid_ = Guid('{b3443557-7f39-4d04-a89c-844338cac897}')
class IProjectionFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IProjectionFactory'
    _iid_ = Guid('{c4f29cab-60ad-4f24-bd27-9d69c3127c9a}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Projection: ...
class IQuadraticBezierSegment(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IQuadraticBezierSegment'
    _iid_ = Guid('{2c509a5b-bf18-455a-a078-914b5232d8af}')
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
    _classid_ = 'Windows.UI.Xaml.Media.IQuadraticBezierSegmentStatics'
    _iid_ = Guid('{69c78278-3c0b-4b4f-b7a2-f003ded41bb0}')
    @winrt_commethod(6)
    def get_Point1Property(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_Point2Property(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Point1Property = property(get_Point1Property, None)
    Point2Property = property(get_Point2Property, None)
class IRateChangedRoutedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IRateChangedRoutedEventArgs'
    _iid_ = Guid('{9016aa6f-3ca8-4c80-8e2f-8851a68f131f}')
class IRectangleGeometry(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IRectangleGeometry'
    _iid_ = Guid('{a25a1f58-c575-4196-91cf-9fdfb10445c3}')
    @winrt_commethod(6)
    def get_Rect(self) -> win32more.Windows.Foundation.Rect: ...
    @winrt_commethod(7)
    def put_Rect(self, value: win32more.Windows.Foundation.Rect) -> Void: ...
    Rect = property(get_Rect, put_Rect)
class IRectangleGeometryStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IRectangleGeometryStatics'
    _iid_ = Guid('{377f8dba-7902-48e3-83be-7c8002a6653c}')
    @winrt_commethod(6)
    def get_RectProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    RectProperty = property(get_RectProperty, None)
class IRenderedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IRenderedEventArgs'
    _iid_ = Guid('{e349817d-81c7-4938-828c-a7e2797b35a6}')
    @winrt_commethod(6)
    def get_FrameDuration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    FrameDuration = property(get_FrameDuration, None)
class IRenderingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IRenderingEventArgs'
    _iid_ = Guid('{5bf7d30d-9748-4aed-8380-d7890eb776a0}')
    @winrt_commethod(6)
    def get_RenderingTime(self) -> win32more.Windows.Foundation.TimeSpan: ...
    RenderingTime = property(get_RenderingTime, None)
class IRevealBackgroundBrush(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IRevealBackgroundBrush'
    _iid_ = Guid('{261dcc0e-1991-4cdf-aee0-6350a3f90bb9}')
class IRevealBackgroundBrushFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IRevealBackgroundBrushFactory'
    _iid_ = Guid('{8c56bcaa-02a5-4f45-8506-8d39228f5d3f}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.RevealBackgroundBrush: ...
class IRevealBorderBrush(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IRevealBorderBrush'
    _iid_ = Guid('{060ba115-c542-483c-8202-5f03331866c9}')
class IRevealBorderBrushFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IRevealBorderBrushFactory'
    _iid_ = Guid('{94c25298-f5f8-4482-a25c-6758501a8626}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.RevealBorderBrush: ...
class IRevealBrush(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IRevealBrush'
    _iid_ = Guid('{2036a0ed-8271-4398-9019-25872093f13f}')
    @winrt_commethod(6)
    def get_Color(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_Color(self, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_commethod(8)
    def get_TargetTheme(self) -> win32more.Windows.UI.Xaml.ApplicationTheme: ...
    @winrt_commethod(9)
    def put_TargetTheme(self, value: win32more.Windows.UI.Xaml.ApplicationTheme) -> Void: ...
    @winrt_commethod(10)
    def get_AlwaysUseFallback(self) -> Boolean: ...
    @winrt_commethod(11)
    def put_AlwaysUseFallback(self, value: Boolean) -> Void: ...
    AlwaysUseFallback = property(get_AlwaysUseFallback, put_AlwaysUseFallback)
    Color = property(get_Color, put_Color)
    TargetTheme = property(get_TargetTheme, put_TargetTheme)
class IRevealBrushFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IRevealBrushFactory'
    _iid_ = Guid('{9d9379ce-e3a0-4aaf-be37-ea9d9dd43105}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.RevealBrush: ...
class IRevealBrushStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IRevealBrushStatics'
    _iid_ = Guid('{190f2625-7209-4d42-a847-1ac4bbbb3499}')
    @winrt_commethod(6)
    def get_ColorProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_TargetThemeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_AlwaysUseFallbackProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_StateProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def SetState(self, element: win32more.Windows.UI.Xaml.UIElement, value: win32more.Windows.UI.Xaml.Media.RevealBrushState) -> Void: ...
    @winrt_commethod(11)
    def GetState(self, element: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.UI.Xaml.Media.RevealBrushState: ...
    AlwaysUseFallbackProperty = property(get_AlwaysUseFallbackProperty, None)
    ColorProperty = property(get_ColorProperty, None)
    StateProperty = property(get_StateProperty, None)
    TargetThemeProperty = property(get_TargetThemeProperty, None)
class IRotateTransform(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    Angle = property(get_Angle, put_Angle)
    CenterX = property(get_CenterX, put_CenterX)
    CenterY = property(get_CenterY, put_CenterY)
class IRotateTransformStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IRotateTransformStatics'
    _iid_ = Guid('{a131eb8a-51a3-41b6-b9d3-a10e429054ab}')
    @winrt_commethod(6)
    def get_CenterXProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_CenterYProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_AngleProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    AngleProperty = property(get_AngleProperty, None)
    CenterXProperty = property(get_CenterXProperty, None)
    CenterYProperty = property(get_CenterYProperty, None)
class IScaleTransform(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IScaleTransformStatics'
    _iid_ = Guid('{9d9436f4-40a7-46dd-975a-07d337cd852e}')
    @winrt_commethod(6)
    def get_CenterXProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_CenterYProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_ScaleXProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_ScaleYProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    CenterXProperty = property(get_CenterXProperty, None)
    CenterYProperty = property(get_CenterYProperty, None)
    ScaleXProperty = property(get_ScaleXProperty, None)
    ScaleYProperty = property(get_ScaleYProperty, None)
class IShadow(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IShadow'
    _iid_ = Guid('{6813a583-f3b4-5fcf-8694-2cd0aefc2fad}')
class IShadowFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IShadowFactory'
    _iid_ = Guid('{19899f25-d28b-51e6-94b0-d7e709686305}')
class ISkewTransform(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    AngleX = property(get_AngleX, put_AngleX)
    AngleY = property(get_AngleY, put_AngleY)
    CenterX = property(get_CenterX, put_CenterX)
    CenterY = property(get_CenterY, put_CenterY)
class ISkewTransformStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ISkewTransformStatics'
    _iid_ = Guid('{ecd11d73-5614-4b31-b6af-beae10105624}')
    @winrt_commethod(6)
    def get_CenterXProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_CenterYProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_AngleXProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_AngleYProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    AngleXProperty = property(get_AngleXProperty, None)
    AngleYProperty = property(get_AngleYProperty, None)
    CenterXProperty = property(get_CenterXProperty, None)
    CenterYProperty = property(get_CenterYProperty, None)
class ISolidColorBrush(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ISolidColorBrush'
    _iid_ = Guid('{9d850850-66f3-48df-9a8f-824bd5e070af}')
    @winrt_commethod(6)
    def get_Color(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_Color(self, value: win32more.Windows.UI.Color) -> Void: ...
    Color = property(get_Color, put_Color)
class ISolidColorBrushFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ISolidColorBrushFactory'
    _iid_ = Guid('{d935ce0c-86f5-4da6-8a27-b1619ef7f92b}')
    @winrt_commethod(6)
    def CreateInstanceWithColor(self, color: win32more.Windows.UI.Color) -> win32more.Windows.UI.Xaml.Media.SolidColorBrush: ...
class ISolidColorBrushStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ISolidColorBrushStatics'
    _iid_ = Guid('{e1a65efa-2b23-41ba-b9ba-7094ec8e4e9f}')
    @winrt_commethod(6)
    def get_ColorProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    ColorProperty = property(get_ColorProperty, None)
class IThemeShadow(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IThemeShadow'
    _iid_ = Guid('{3eccad09-7985-5f39-8b62-6c10696dca6f}')
    @winrt_commethod(6)
    def get_Receivers(self) -> win32more.Windows.UI.Xaml.UIElementWeakCollection: ...
    Receivers = property(get_Receivers, None)
class IThemeShadowFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IThemeShadowFactory'
    _iid_ = Guid('{2e71465d-0f67-590e-831b-7e5e2a32b778}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.ThemeShadow: ...
class ITileBrush(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ITileBrush'
    _iid_ = Guid('{c201cf06-cd84-48a5-9607-664d7361cd61}')
    @winrt_commethod(6)
    def get_AlignmentX(self) -> win32more.Windows.UI.Xaml.Media.AlignmentX: ...
    @winrt_commethod(7)
    def put_AlignmentX(self, value: win32more.Windows.UI.Xaml.Media.AlignmentX) -> Void: ...
    @winrt_commethod(8)
    def get_AlignmentY(self) -> win32more.Windows.UI.Xaml.Media.AlignmentY: ...
    @winrt_commethod(9)
    def put_AlignmentY(self, value: win32more.Windows.UI.Xaml.Media.AlignmentY) -> Void: ...
    @winrt_commethod(10)
    def get_Stretch(self) -> win32more.Windows.UI.Xaml.Media.Stretch: ...
    @winrt_commethod(11)
    def put_Stretch(self, value: win32more.Windows.UI.Xaml.Media.Stretch) -> Void: ...
    AlignmentX = property(get_AlignmentX, put_AlignmentX)
    AlignmentY = property(get_AlignmentY, put_AlignmentY)
    Stretch = property(get_Stretch, put_Stretch)
class ITileBrushFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ITileBrushFactory'
    _iid_ = Guid('{aa159f7c-ed6a-4fb3-b014-b5c7e379a4de}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.TileBrush: ...
class ITileBrushStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ITileBrushStatics'
    _iid_ = Guid('{3497c25b-b562-4e68-8435-2399f6eb94d5}')
    @winrt_commethod(6)
    def get_AlignmentXProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_AlignmentYProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_StretchProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    AlignmentXProperty = property(get_AlignmentXProperty, None)
    AlignmentYProperty = property(get_AlignmentYProperty, None)
    StretchProperty = property(get_StretchProperty, None)
class ITimelineMarker(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ITimelineMarker'
    _iid_ = Guid('{a68ef02d-45ba-4e50-8cad-aaea3a227af5}')
    @winrt_commethod(6)
    def get_Time(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(7)
    def put_Time(self, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_commethod(8)
    def get_Type(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Type(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Text(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_Text(self, value: WinRT_String) -> Void: ...
    Text = property(get_Text, put_Text)
    Time = property(get_Time, put_Time)
    Type = property(get_Type, put_Type)
class ITimelineMarkerRoutedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ITimelineMarkerRoutedEventArgs'
    _iid_ = Guid('{7c3b3ef3-2c88-4d9c-99b6-46cdbd48d4c1}')
    @winrt_commethod(6)
    def get_Marker(self) -> win32more.Windows.UI.Xaml.Media.TimelineMarker: ...
    @winrt_commethod(7)
    def put_Marker(self, value: win32more.Windows.UI.Xaml.Media.TimelineMarker) -> Void: ...
    Marker = property(get_Marker, put_Marker)
class ITimelineMarkerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ITimelineMarkerStatics'
    _iid_ = Guid('{c4aef0c6-16a3-484b-87f5-6528b8f04a47}')
    @winrt_commethod(6)
    def get_TimeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_TypeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_TextProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    TextProperty = property(get_TextProperty, None)
    TimeProperty = property(get_TimeProperty, None)
    TypeProperty = property(get_TypeProperty, None)
class ITransform(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ITransform'
    _iid_ = Guid('{4df74078-bfd6-4ed1-9682-d2fd8bf2fe6f}')
class ITransformFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ITransformFactory'
    _iid_ = Guid('{1a955a66-7cf4-4320-b416-6181192fcc6d}')
class ITransformGroup(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ITransformGroup'
    _iid_ = Guid('{63418ccc-8d2d-4737-b951-2afce1ddc4c4}')
    @winrt_commethod(6)
    def get_Children(self) -> win32more.Windows.UI.Xaml.Media.TransformCollection: ...
    @winrt_commethod(7)
    def put_Children(self, value: win32more.Windows.UI.Xaml.Media.TransformCollection) -> Void: ...
    @winrt_commethod(8)
    def get_Value(self) -> win32more.Windows.UI.Xaml.Media.Matrix: ...
    Children = property(get_Children, put_Children)
    Value = property(get_Value, None)
class ITransformGroupStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ITransformGroupStatics'
    _iid_ = Guid('{25312f2a-cfab-4b24-9713-5bdead1929c0}')
    @winrt_commethod(6)
    def get_ChildrenProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    ChildrenProperty = property(get_ChildrenProperty, None)
class ITranslateTransform(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
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
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.ITranslateTransformStatics'
    _iid_ = Guid('{f419aa91-e042-4111-9c2f-d201304123dd}')
    @winrt_commethod(6)
    def get_XProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_YProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    XProperty = property(get_XProperty, None)
    YProperty = property(get_YProperty, None)
class IVisualTreeHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IVisualTreeHelper'
    _iid_ = Guid('{24b935e3-52c7-4141-8bac-a73d06130569}')
class IVisualTreeHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IVisualTreeHelperStatics'
    _iid_ = Guid('{e75758c4-d25d-4b1d-971f-596f17f12baa}')
    @winrt_commethod(6)
    def FindElementsInHostCoordinatesPoint(self, intersectingPoint: win32more.Windows.Foundation.Point, subtree: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.UIElement]: ...
    @winrt_commethod(7)
    def FindElementsInHostCoordinatesRect(self, intersectingRect: win32more.Windows.Foundation.Rect, subtree: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.UIElement]: ...
    @winrt_commethod(8)
    def FindAllElementsInHostCoordinatesPoint(self, intersectingPoint: win32more.Windows.Foundation.Point, subtree: win32more.Windows.UI.Xaml.UIElement, includeAllElements: Boolean) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.UIElement]: ...
    @winrt_commethod(9)
    def FindAllElementsInHostCoordinatesRect(self, intersectingRect: win32more.Windows.Foundation.Rect, subtree: win32more.Windows.UI.Xaml.UIElement, includeAllElements: Boolean) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.UIElement]: ...
    @winrt_commethod(10)
    def GetChild(self, reference: win32more.Windows.UI.Xaml.DependencyObject, childIndex: Int32) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(11)
    def GetChildrenCount(self, reference: win32more.Windows.UI.Xaml.DependencyObject) -> Int32: ...
    @winrt_commethod(12)
    def GetParent(self, reference: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_commethod(13)
    def DisconnectChildrenRecursive(self, element: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
class IVisualTreeHelperStatics2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IVisualTreeHelperStatics2'
    _iid_ = Guid('{07bcd176-869f-44a7-8797-2103a4c3e47a}')
    @winrt_commethod(6)
    def GetOpenPopups(self, window: win32more.Windows.UI.Xaml.Window) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.Controls.Primitives.Popup]: ...
class IVisualTreeHelperStatics3(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IVisualTreeHelperStatics3'
    _iid_ = Guid('{40420d50-ca16-57da-8aac-944c8af577fd}')
    @winrt_commethod(6)
    def GetOpenPopupsForXamlRoot(self, xamlRoot: win32more.Windows.UI.Xaml.XamlRoot) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.Controls.Primitives.Popup]: ...
class IXamlCompositionBrushBase(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IXamlCompositionBrushBase'
    _iid_ = Guid('{03e432d9-b35c-4a79-811c-c5652004da0e}')
    @winrt_commethod(6)
    def get_FallbackColor(self) -> win32more.Windows.UI.Color: ...
    @winrt_commethod(7)
    def put_FallbackColor(self, value: win32more.Windows.UI.Color) -> Void: ...
    FallbackColor = property(get_FallbackColor, put_FallbackColor)
class IXamlCompositionBrushBaseFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IXamlCompositionBrushBaseFactory'
    _iid_ = Guid('{394f0823-2451-4ed8-bd24-488149b3428d}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.XamlCompositionBrushBase: ...
class IXamlCompositionBrushBaseOverrides(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IXamlCompositionBrushBaseOverrides'
    _iid_ = Guid('{d19127f1-38b4-4ea1-8f33-849629a4c9c1}')
    @winrt_commethod(6)
    def OnConnected(self) -> Void: ...
    @winrt_commethod(7)
    def OnDisconnected(self) -> Void: ...
class IXamlCompositionBrushBaseProtected(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IXamlCompositionBrushBaseProtected'
    _iid_ = Guid('{1513f3d8-0457-4e1c-ad77-11c1d9879743}')
    @winrt_commethod(6)
    def get_CompositionBrush(self) -> win32more.Windows.UI.Composition.CompositionBrush: ...
    @winrt_commethod(7)
    def put_CompositionBrush(self, value: win32more.Windows.UI.Composition.CompositionBrush) -> Void: ...
    CompositionBrush = property(get_CompositionBrush, put_CompositionBrush)
class IXamlCompositionBrushBaseStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IXamlCompositionBrushBaseStatics'
    _iid_ = Guid('{4fd49b06-061a-441f-b97a-adfbd41ae681}')
    @winrt_commethod(6)
    def get_FallbackColorProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    FallbackColorProperty = property(get_FallbackColorProperty, None)
class IXamlLight(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IXamlLight'
    _iid_ = Guid('{0cc3fc1f-b327-4a18-9648-7c84db26ce22}')
class IXamlLightFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IXamlLightFactory'
    _iid_ = Guid('{87ded768-3055-43b8-8ef6-798dc4c2329a}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.XamlLight: ...
class IXamlLightOverrides(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IXamlLightOverrides'
    _iid_ = Guid('{7c6296c7-0173-48e1-b73d-7fa216a9ac28}')
    @winrt_commethod(6)
    def GetId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def OnConnected(self, newElement: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(8)
    def OnDisconnected(self, oldElement: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
class IXamlLightProtected(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IXamlLightProtected'
    _iid_ = Guid('{5ecf220b-1252-43d0-9729-6ea692046838}')
    @winrt_commethod(6)
    def get_CompositionLight(self) -> win32more.Windows.UI.Composition.CompositionLight: ...
    @winrt_commethod(7)
    def put_CompositionLight(self, value: win32more.Windows.UI.Composition.CompositionLight) -> Void: ...
    CompositionLight = property(get_CompositionLight, put_CompositionLight)
class IXamlLightStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Media.IXamlLightStatics'
    _iid_ = Guid('{b5ea9d69-b508-4e9c-bd27-6b044b5f78a0}')
    @winrt_commethod(6)
    def AddTargetElement(self, lightId: WinRT_String, element: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(7)
    def RemoveTargetElement(self, lightId: WinRT_String, element: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_commethod(8)
    def AddTargetBrush(self, lightId: WinRT_String, brush: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(9)
    def RemoveTargetBrush(self, lightId: WinRT_String, brush: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
class _ImageBrush_Meta_(ComPtr.__class__):
    pass
class ImageBrush(ComPtr, metaclass=_ImageBrush_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.TileBrush
    default_interface: win32more.Windows.UI.Xaml.Media.IImageBrush
    _classid_ = 'Windows.UI.Xaml.Media.ImageBrush'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.ImageBrush.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.ImageBrush: ...
    @winrt_mixinmethod
    def get_ImageSource(self: win32more.Windows.UI.Xaml.Media.IImageBrush) -> win32more.Windows.UI.Xaml.Media.ImageSource: ...
    @winrt_mixinmethod
    def put_ImageSource(self: win32more.Windows.UI.Xaml.Media.IImageBrush, value: win32more.Windows.UI.Xaml.Media.ImageSource) -> Void: ...
    @winrt_mixinmethod
    def add_ImageFailed(self: win32more.Windows.UI.Xaml.Media.IImageBrush, handler: win32more.Windows.UI.Xaml.ExceptionRoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ImageFailed(self: win32more.Windows.UI.Xaml.Media.IImageBrush, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def add_ImageOpened(self: win32more.Windows.UI.Xaml.Media.IImageBrush, handler: win32more.Windows.UI.Xaml.RoutedEventHandler) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_ImageOpened(self: win32more.Windows.UI.Xaml.Media.IImageBrush, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_classmethod
    def get_ImageSourceProperty(cls: win32more.Windows.UI.Xaml.Media.IImageBrushStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    ImageSource = property(get_ImageSource, put_ImageSource)
    _ImageBrush_Meta_.ImageSourceProperty = property(get_ImageSourceProperty, None)
    ImageFailed = event()
    ImageOpened = event()
class ImageSource(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Media.IImageSource
    _classid_ = 'Windows.UI.Xaml.Media.ImageSource'
class _LineGeometry_Meta_(ComPtr.__class__):
    pass
class LineGeometry(ComPtr, metaclass=_LineGeometry_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Geometry
    default_interface: win32more.Windows.UI.Xaml.Media.ILineGeometry
    _classid_ = 'Windows.UI.Xaml.Media.LineGeometry'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.LineGeometry.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.LineGeometry: ...
    @winrt_mixinmethod
    def get_StartPoint(self: win32more.Windows.UI.Xaml.Media.ILineGeometry) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_StartPoint(self: win32more.Windows.UI.Xaml.Media.ILineGeometry, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_EndPoint(self: win32more.Windows.UI.Xaml.Media.ILineGeometry) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_EndPoint(self: win32more.Windows.UI.Xaml.Media.ILineGeometry, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_classmethod
    def get_StartPointProperty(cls: win32more.Windows.UI.Xaml.Media.ILineGeometryStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_EndPointProperty(cls: win32more.Windows.UI.Xaml.Media.ILineGeometryStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    EndPoint = property(get_EndPoint, put_EndPoint)
    StartPoint = property(get_StartPoint, put_StartPoint)
    _LineGeometry_Meta_.EndPointProperty = property(get_EndPointProperty, None)
    _LineGeometry_Meta_.StartPointProperty = property(get_StartPointProperty, None)
class _LineSegment_Meta_(ComPtr.__class__):
    pass
class LineSegment(ComPtr, metaclass=_LineSegment_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.PathSegment
    default_interface: win32more.Windows.UI.Xaml.Media.ILineSegment
    _classid_ = 'Windows.UI.Xaml.Media.LineSegment'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.LineSegment.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.LineSegment: ...
    @winrt_mixinmethod
    def get_Point(self: win32more.Windows.UI.Xaml.Media.ILineSegment) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Point(self: win32more.Windows.UI.Xaml.Media.ILineSegment, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_classmethod
    def get_PointProperty(cls: win32more.Windows.UI.Xaml.Media.ILineSegmentStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Point = property(get_Point, put_Point)
    _LineSegment_Meta_.PointProperty = property(get_PointProperty, None)
class _LinearGradientBrush_Meta_(ComPtr.__class__):
    pass
class LinearGradientBrush(ComPtr, metaclass=_LinearGradientBrush_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.GradientBrush
    default_interface: win32more.Windows.UI.Xaml.Media.ILinearGradientBrush
    _classid_ = 'Windows.UI.Xaml.Media.LinearGradientBrush'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.LinearGradientBrush.CreateInstance(*args))
        elif len(args) == 2:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.LinearGradientBrush.CreateInstanceWithGradientStopCollectionAndAngle(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.LinearGradientBrush: ...
    @winrt_factorymethod
    def CreateInstanceWithGradientStopCollectionAndAngle(cls: win32more.Windows.UI.Xaml.Media.ILinearGradientBrushFactory, gradientStopCollection: win32more.Windows.UI.Xaml.Media.GradientStopCollection, angle: Double) -> win32more.Windows.UI.Xaml.Media.LinearGradientBrush: ...
    @winrt_mixinmethod
    def get_StartPoint(self: win32more.Windows.UI.Xaml.Media.ILinearGradientBrush) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_StartPoint(self: win32more.Windows.UI.Xaml.Media.ILinearGradientBrush, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_EndPoint(self: win32more.Windows.UI.Xaml.Media.ILinearGradientBrush) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_EndPoint(self: win32more.Windows.UI.Xaml.Media.ILinearGradientBrush, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_classmethod
    def get_StartPointProperty(cls: win32more.Windows.UI.Xaml.Media.ILinearGradientBrushStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_EndPointProperty(cls: win32more.Windows.UI.Xaml.Media.ILinearGradientBrushStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    EndPoint = property(get_EndPoint, put_EndPoint)
    StartPoint = property(get_StartPoint, put_StartPoint)
    _LinearGradientBrush_Meta_.EndPointProperty = property(get_EndPointProperty, None)
    _LinearGradientBrush_Meta_.StartPointProperty = property(get_StartPointProperty, None)
class LoadedImageSourceLoadCompletedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Media.ILoadedImageSourceLoadCompletedEventArgs
    _classid_ = 'Windows.UI.Xaml.Media.LoadedImageSourceLoadCompletedEventArgs'
    @winrt_mixinmethod
    def get_Status(self: win32more.Windows.UI.Xaml.Media.ILoadedImageSourceLoadCompletedEventArgs) -> win32more.Windows.UI.Xaml.Media.LoadedImageSourceLoadStatus: ...
    Status = property(get_Status, None)
class LoadedImageSourceLoadStatus(Enum, Int32):
    Success = 0
    NetworkError = 1
    InvalidFormat = 2
    Other = 3
class LoadedImageSurface(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[ContextManagerProtocol]
    default_interface: win32more.Windows.UI.Xaml.Media.ILoadedImageSurface
    _classid_ = 'Windows.UI.Xaml.Media.LoadedImageSurface'
    @winrt_mixinmethod
    def get_DecodedPhysicalSize(self: win32more.Windows.UI.Xaml.Media.ILoadedImageSurface) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_DecodedSize(self: win32more.Windows.UI.Xaml.Media.ILoadedImageSurface) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def get_NaturalSize(self: win32more.Windows.UI.Xaml.Media.ILoadedImageSurface) -> win32more.Windows.Foundation.Size: ...
    @winrt_mixinmethod
    def add_LoadCompleted(self: win32more.Windows.UI.Xaml.Media.ILoadedImageSurface, handler: win32more.Windows.Foundation.TypedEventHandler[win32more.Windows.UI.Xaml.Media.LoadedImageSurface, win32more.Windows.UI.Xaml.Media.LoadedImageSourceLoadCompletedEventArgs]) -> win32more.Windows.Foundation.EventRegistrationToken: ...
    @winrt_mixinmethod
    def remove_LoadCompleted(self: win32more.Windows.UI.Xaml.Media.ILoadedImageSurface, token: win32more.Windows.Foundation.EventRegistrationToken) -> Void: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_classmethod
    def StartLoadFromUriWithSize(cls: win32more.Windows.UI.Xaml.Media.ILoadedImageSurfaceStatics, uri: win32more.Windows.Foundation.Uri, desiredMaxSize: win32more.Windows.Foundation.Size) -> win32more.Windows.UI.Xaml.Media.LoadedImageSurface: ...
    @winrt_classmethod
    def StartLoadFromUri(cls: win32more.Windows.UI.Xaml.Media.ILoadedImageSurfaceStatics, uri: win32more.Windows.Foundation.Uri) -> win32more.Windows.UI.Xaml.Media.LoadedImageSurface: ...
    @winrt_classmethod
    def StartLoadFromStreamWithSize(cls: win32more.Windows.UI.Xaml.Media.ILoadedImageSurfaceStatics, stream: win32more.Windows.Storage.Streams.IRandomAccessStream, desiredMaxSize: win32more.Windows.Foundation.Size) -> win32more.Windows.UI.Xaml.Media.LoadedImageSurface: ...
    @winrt_classmethod
    def StartLoadFromStream(cls: win32more.Windows.UI.Xaml.Media.ILoadedImageSurfaceStatics, stream: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.UI.Xaml.Media.LoadedImageSurface: ...
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
    extends: win32more.Windows.UI.Xaml.Media.Projection
    default_interface: win32more.Windows.UI.Xaml.Media.IMatrix3DProjection
    _classid_ = 'Windows.UI.Xaml.Media.Matrix3DProjection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Matrix3DProjection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.Matrix3DProjection: ...
    @winrt_mixinmethod
    def get_ProjectionMatrix(self: win32more.Windows.UI.Xaml.Media.IMatrix3DProjection) -> win32more.Windows.UI.Xaml.Media.Media3D.Matrix3D: ...
    @winrt_mixinmethod
    def put_ProjectionMatrix(self: win32more.Windows.UI.Xaml.Media.IMatrix3DProjection, value: win32more.Windows.UI.Xaml.Media.Media3D.Matrix3D) -> Void: ...
    @winrt_classmethod
    def get_ProjectionMatrixProperty(cls: win32more.Windows.UI.Xaml.Media.IMatrix3DProjectionStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    ProjectionMatrix = property(get_ProjectionMatrix, put_ProjectionMatrix)
    _Matrix3DProjection_Meta_.ProjectionMatrixProperty = property(get_ProjectionMatrixProperty, None)
class _MatrixHelper_Meta_(ComPtr.__class__):
    pass
class MatrixHelper(ComPtr, metaclass=_MatrixHelper_Meta_):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Media.IMatrixHelper
    _classid_ = 'Windows.UI.Xaml.Media.MatrixHelper'
    @winrt_classmethod
    def get_Identity(cls: win32more.Windows.UI.Xaml.Media.IMatrixHelperStatics) -> win32more.Windows.UI.Xaml.Media.Matrix: ...
    @winrt_classmethod
    def FromElements(cls: win32more.Windows.UI.Xaml.Media.IMatrixHelperStatics, m11: Double, m12: Double, m21: Double, m22: Double, offsetX: Double, offsetY: Double) -> win32more.Windows.UI.Xaml.Media.Matrix: ...
    @winrt_classmethod
    def GetIsIdentity(cls: win32more.Windows.UI.Xaml.Media.IMatrixHelperStatics, target: win32more.Windows.UI.Xaml.Media.Matrix) -> Boolean: ...
    @winrt_classmethod
    def Transform(cls: win32more.Windows.UI.Xaml.Media.IMatrixHelperStatics, target: win32more.Windows.UI.Xaml.Media.Matrix, point: win32more.Windows.Foundation.Point) -> win32more.Windows.Foundation.Point: ...
    _MatrixHelper_Meta_.Identity = property(get_Identity, None)
class _MatrixTransform_Meta_(ComPtr.__class__):
    pass
class MatrixTransform(ComPtr, metaclass=_MatrixTransform_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Transform
    default_interface: win32more.Windows.UI.Xaml.Media.IMatrixTransform
    _classid_ = 'Windows.UI.Xaml.Media.MatrixTransform'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.MatrixTransform.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.MatrixTransform: ...
    @winrt_mixinmethod
    def get_Matrix(self: win32more.Windows.UI.Xaml.Media.IMatrixTransform) -> win32more.Windows.UI.Xaml.Media.Matrix: ...
    @winrt_mixinmethod
    def put_Matrix(self: win32more.Windows.UI.Xaml.Media.IMatrixTransform, value: win32more.Windows.UI.Xaml.Media.Matrix) -> Void: ...
    @winrt_classmethod
    def get_MatrixProperty(cls: win32more.Windows.UI.Xaml.Media.IMatrixTransformStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Matrix = property(get_Matrix, put_Matrix)
    _MatrixTransform_Meta_.MatrixProperty = property(get_MatrixProperty, None)
class MediaCanPlayResponse(Enum, Int32):
    NotSupported = 0
    Maybe = 1
    Probably = 2
class MediaElementState(Enum, Int32):
    Closed = 0
    Opening = 1
    Buffering = 2
    Playing = 3
    Paused = 4
    Stopped = 5
class MediaTransportControlsThumbnailRequestedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Media.IMediaTransportControlsThumbnailRequestedEventArgs
    _classid_ = 'Windows.UI.Xaml.Media.MediaTransportControlsThumbnailRequestedEventArgs'
    @winrt_mixinmethod
    def SetThumbnailImage(self: win32more.Windows.UI.Xaml.Media.IMediaTransportControlsThumbnailRequestedEventArgs, source: win32more.Windows.Storage.Streams.IInputStream) -> Void: ...
    @winrt_mixinmethod
    def GetDeferral(self: win32more.Windows.UI.Xaml.Media.IMediaTransportControlsThumbnailRequestedEventArgs) -> win32more.Windows.Foundation.Deferral: ...
class PartialMediaFailureDetectedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Media.IPartialMediaFailureDetectedEventArgs
    _classid_ = 'Windows.UI.Xaml.Media.PartialMediaFailureDetectedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.PartialMediaFailureDetectedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.PartialMediaFailureDetectedEventArgs: ...
    @winrt_mixinmethod
    def get_StreamKind(self: win32more.Windows.UI.Xaml.Media.IPartialMediaFailureDetectedEventArgs) -> win32more.Windows.Media.Playback.FailedMediaStreamKind: ...
    @winrt_mixinmethod
    def get_ExtendedError(self: win32more.Windows.UI.Xaml.Media.IPartialMediaFailureDetectedEventArgs2) -> win32more.Windows.Foundation.HResult: ...
    ExtendedError = property(get_ExtendedError, None)
    StreamKind = property(get_StreamKind, None)
class _PathFigure_Meta_(ComPtr.__class__):
    pass
class PathFigure(ComPtr, metaclass=_PathFigure_Meta_):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Media.IPathFigure
    _classid_ = 'Windows.UI.Xaml.Media.PathFigure'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.PathFigure.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.PathFigure: ...
    @winrt_mixinmethod
    def get_Segments(self: win32more.Windows.UI.Xaml.Media.IPathFigure) -> win32more.Windows.UI.Xaml.Media.PathSegmentCollection: ...
    @winrt_mixinmethod
    def put_Segments(self: win32more.Windows.UI.Xaml.Media.IPathFigure, value: win32more.Windows.UI.Xaml.Media.PathSegmentCollection) -> Void: ...
    @winrt_mixinmethod
    def get_StartPoint(self: win32more.Windows.UI.Xaml.Media.IPathFigure) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_StartPoint(self: win32more.Windows.UI.Xaml.Media.IPathFigure, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_IsClosed(self: win32more.Windows.UI.Xaml.Media.IPathFigure) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsClosed(self: win32more.Windows.UI.Xaml.Media.IPathFigure, value: Boolean) -> Void: ...
    @winrt_mixinmethod
    def get_IsFilled(self: win32more.Windows.UI.Xaml.Media.IPathFigure) -> Boolean: ...
    @winrt_mixinmethod
    def put_IsFilled(self: win32more.Windows.UI.Xaml.Media.IPathFigure, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_SegmentsProperty(cls: win32more.Windows.UI.Xaml.Media.IPathFigureStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StartPointProperty(cls: win32more.Windows.UI.Xaml.Media.IPathFigureStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsClosedProperty(cls: win32more.Windows.UI.Xaml.Media.IPathFigureStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_IsFilledProperty(cls: win32more.Windows.UI.Xaml.Media.IPathFigureStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
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
    implements: Tuple[SequenceProtocol[win32more.Windows.UI.Xaml.Media.PathFigure]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.PathFigure]
    _classid_ = 'Windows.UI.Xaml.Media.PathFigureCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.PathFigureCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.PathFigureCollection: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.PathFigure], index: UInt32) -> win32more.Windows.UI.Xaml.Media.PathFigure: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.PathFigure]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.PathFigure]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.Media.PathFigure]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.PathFigure], value: win32more.Windows.UI.Xaml.Media.PathFigure, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.PathFigure], index: UInt32, value: win32more.Windows.UI.Xaml.Media.PathFigure) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.PathFigure], index: UInt32, value: win32more.Windows.UI.Xaml.Media.PathFigure) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.PathFigure], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.PathFigure], value: win32more.Windows.UI.Xaml.Media.PathFigure) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.PathFigure]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.PathFigure]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.PathFigure], startIndex: UInt32, items: FillArray[win32more.Windows.UI.Xaml.Media.PathFigure]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.PathFigure], items: PassArray[win32more.Windows.UI.Xaml.Media.PathFigure]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.Media.PathFigure]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.UI.Xaml.Media.PathFigure]: ...
    Size = property(get_Size, None)
class _PathGeometry_Meta_(ComPtr.__class__):
    pass
class PathGeometry(ComPtr, metaclass=_PathGeometry_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Geometry
    default_interface: win32more.Windows.UI.Xaml.Media.IPathGeometry
    _classid_ = 'Windows.UI.Xaml.Media.PathGeometry'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.PathGeometry.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.PathGeometry: ...
    @winrt_mixinmethod
    def get_FillRule(self: win32more.Windows.UI.Xaml.Media.IPathGeometry) -> win32more.Windows.UI.Xaml.Media.FillRule: ...
    @winrt_mixinmethod
    def put_FillRule(self: win32more.Windows.UI.Xaml.Media.IPathGeometry, value: win32more.Windows.UI.Xaml.Media.FillRule) -> Void: ...
    @winrt_mixinmethod
    def get_Figures(self: win32more.Windows.UI.Xaml.Media.IPathGeometry) -> win32more.Windows.UI.Xaml.Media.PathFigureCollection: ...
    @winrt_mixinmethod
    def put_Figures(self: win32more.Windows.UI.Xaml.Media.IPathGeometry, value: win32more.Windows.UI.Xaml.Media.PathFigureCollection) -> Void: ...
    @winrt_classmethod
    def get_FillRuleProperty(cls: win32more.Windows.UI.Xaml.Media.IPathGeometryStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_FiguresProperty(cls: win32more.Windows.UI.Xaml.Media.IPathGeometryStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Figures = property(get_Figures, put_Figures)
    FillRule = property(get_FillRule, put_FillRule)
    _PathGeometry_Meta_.FiguresProperty = property(get_FiguresProperty, None)
    _PathGeometry_Meta_.FillRuleProperty = property(get_FillRuleProperty, None)
class PathSegment(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Media.IPathSegment
    _classid_ = 'Windows.UI.Xaml.Media.PathSegment'
class PathSegmentCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Windows.UI.Xaml.Media.PathSegment]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.PathSegment]
    _classid_ = 'Windows.UI.Xaml.Media.PathSegmentCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.PathSegmentCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.PathSegmentCollection: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.PathSegment], index: UInt32) -> win32more.Windows.UI.Xaml.Media.PathSegment: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.PathSegment]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.PathSegment]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.Media.PathSegment]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.PathSegment], value: win32more.Windows.UI.Xaml.Media.PathSegment, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.PathSegment], index: UInt32, value: win32more.Windows.UI.Xaml.Media.PathSegment) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.PathSegment], index: UInt32, value: win32more.Windows.UI.Xaml.Media.PathSegment) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.PathSegment], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.PathSegment], value: win32more.Windows.UI.Xaml.Media.PathSegment) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.PathSegment]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.PathSegment]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.PathSegment], startIndex: UInt32, items: FillArray[win32more.Windows.UI.Xaml.Media.PathSegment]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.PathSegment], items: PassArray[win32more.Windows.UI.Xaml.Media.PathSegment]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.Media.PathSegment]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.UI.Xaml.Media.PathSegment]: ...
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
    extends: win32more.Windows.UI.Xaml.Media.Projection
    default_interface: win32more.Windows.UI.Xaml.Media.IPlaneProjection
    _classid_ = 'Windows.UI.Xaml.Media.PlaneProjection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.PlaneProjection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.PlaneProjection: ...
    @winrt_mixinmethod
    def get_LocalOffsetX(self: win32more.Windows.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_LocalOffsetX(self: win32more.Windows.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_LocalOffsetY(self: win32more.Windows.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_LocalOffsetY(self: win32more.Windows.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_LocalOffsetZ(self: win32more.Windows.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_LocalOffsetZ(self: win32more.Windows.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RotationX(self: win32more.Windows.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_RotationX(self: win32more.Windows.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RotationY(self: win32more.Windows.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_RotationY(self: win32more.Windows.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RotationZ(self: win32more.Windows.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_RotationZ(self: win32more.Windows.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_CenterOfRotationX(self: win32more.Windows.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_CenterOfRotationX(self: win32more.Windows.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_CenterOfRotationY(self: win32more.Windows.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_CenterOfRotationY(self: win32more.Windows.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_CenterOfRotationZ(self: win32more.Windows.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_CenterOfRotationZ(self: win32more.Windows.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_GlobalOffsetX(self: win32more.Windows.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_GlobalOffsetX(self: win32more.Windows.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_GlobalOffsetY(self: win32more.Windows.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_GlobalOffsetY(self: win32more.Windows.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_GlobalOffsetZ(self: win32more.Windows.UI.Xaml.Media.IPlaneProjection) -> Double: ...
    @winrt_mixinmethod
    def put_GlobalOffsetZ(self: win32more.Windows.UI.Xaml.Media.IPlaneProjection, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ProjectionMatrix(self: win32more.Windows.UI.Xaml.Media.IPlaneProjection) -> win32more.Windows.UI.Xaml.Media.Media3D.Matrix3D: ...
    @winrt_classmethod
    def get_LocalOffsetXProperty(cls: win32more.Windows.UI.Xaml.Media.IPlaneProjectionStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_LocalOffsetYProperty(cls: win32more.Windows.UI.Xaml.Media.IPlaneProjectionStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_LocalOffsetZProperty(cls: win32more.Windows.UI.Xaml.Media.IPlaneProjectionStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RotationXProperty(cls: win32more.Windows.UI.Xaml.Media.IPlaneProjectionStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RotationYProperty(cls: win32more.Windows.UI.Xaml.Media.IPlaneProjectionStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RotationZProperty(cls: win32more.Windows.UI.Xaml.Media.IPlaneProjectionStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CenterOfRotationXProperty(cls: win32more.Windows.UI.Xaml.Media.IPlaneProjectionStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CenterOfRotationYProperty(cls: win32more.Windows.UI.Xaml.Media.IPlaneProjectionStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CenterOfRotationZProperty(cls: win32more.Windows.UI.Xaml.Media.IPlaneProjectionStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_GlobalOffsetXProperty(cls: win32more.Windows.UI.Xaml.Media.IPlaneProjectionStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_GlobalOffsetYProperty(cls: win32more.Windows.UI.Xaml.Media.IPlaneProjectionStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_GlobalOffsetZProperty(cls: win32more.Windows.UI.Xaml.Media.IPlaneProjectionStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ProjectionMatrixProperty(cls: win32more.Windows.UI.Xaml.Media.IPlaneProjectionStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
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
    _classid_ = 'Windows.UI.Xaml.Media.PointCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.PointCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.PointCollection: ...
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
    extends: win32more.Windows.UI.Xaml.Media.PathSegment
    default_interface: win32more.Windows.UI.Xaml.Media.IPolyBezierSegment
    _classid_ = 'Windows.UI.Xaml.Media.PolyBezierSegment'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.PolyBezierSegment.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.PolyBezierSegment: ...
    @winrt_mixinmethod
    def get_Points(self: win32more.Windows.UI.Xaml.Media.IPolyBezierSegment) -> win32more.Windows.UI.Xaml.Media.PointCollection: ...
    @winrt_mixinmethod
    def put_Points(self: win32more.Windows.UI.Xaml.Media.IPolyBezierSegment, value: win32more.Windows.UI.Xaml.Media.PointCollection) -> Void: ...
    @winrt_classmethod
    def get_PointsProperty(cls: win32more.Windows.UI.Xaml.Media.IPolyBezierSegmentStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Points = property(get_Points, put_Points)
    _PolyBezierSegment_Meta_.PointsProperty = property(get_PointsProperty, None)
class _PolyLineSegment_Meta_(ComPtr.__class__):
    pass
class PolyLineSegment(ComPtr, metaclass=_PolyLineSegment_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.PathSegment
    default_interface: win32more.Windows.UI.Xaml.Media.IPolyLineSegment
    _classid_ = 'Windows.UI.Xaml.Media.PolyLineSegment'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.PolyLineSegment.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.PolyLineSegment: ...
    @winrt_mixinmethod
    def get_Points(self: win32more.Windows.UI.Xaml.Media.IPolyLineSegment) -> win32more.Windows.UI.Xaml.Media.PointCollection: ...
    @winrt_mixinmethod
    def put_Points(self: win32more.Windows.UI.Xaml.Media.IPolyLineSegment, value: win32more.Windows.UI.Xaml.Media.PointCollection) -> Void: ...
    @winrt_classmethod
    def get_PointsProperty(cls: win32more.Windows.UI.Xaml.Media.IPolyLineSegmentStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Points = property(get_Points, put_Points)
    _PolyLineSegment_Meta_.PointsProperty = property(get_PointsProperty, None)
class _PolyQuadraticBezierSegment_Meta_(ComPtr.__class__):
    pass
class PolyQuadraticBezierSegment(ComPtr, metaclass=_PolyQuadraticBezierSegment_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.PathSegment
    default_interface: win32more.Windows.UI.Xaml.Media.IPolyQuadraticBezierSegment
    _classid_ = 'Windows.UI.Xaml.Media.PolyQuadraticBezierSegment'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.PolyQuadraticBezierSegment.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.PolyQuadraticBezierSegment: ...
    @winrt_mixinmethod
    def get_Points(self: win32more.Windows.UI.Xaml.Media.IPolyQuadraticBezierSegment) -> win32more.Windows.UI.Xaml.Media.PointCollection: ...
    @winrt_mixinmethod
    def put_Points(self: win32more.Windows.UI.Xaml.Media.IPolyQuadraticBezierSegment, value: win32more.Windows.UI.Xaml.Media.PointCollection) -> Void: ...
    @winrt_classmethod
    def get_PointsProperty(cls: win32more.Windows.UI.Xaml.Media.IPolyQuadraticBezierSegmentStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Points = property(get_Points, put_Points)
    _PolyQuadraticBezierSegment_Meta_.PointsProperty = property(get_PointsProperty, None)
class Projection(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Media.IProjection
    _classid_ = 'Windows.UI.Xaml.Media.Projection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.Projection.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Media.IProjectionFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.Projection: ...
class _QuadraticBezierSegment_Meta_(ComPtr.__class__):
    pass
class QuadraticBezierSegment(ComPtr, metaclass=_QuadraticBezierSegment_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.PathSegment
    default_interface: win32more.Windows.UI.Xaml.Media.IQuadraticBezierSegment
    _classid_ = 'Windows.UI.Xaml.Media.QuadraticBezierSegment'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.QuadraticBezierSegment.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.QuadraticBezierSegment: ...
    @winrt_mixinmethod
    def get_Point1(self: win32more.Windows.UI.Xaml.Media.IQuadraticBezierSegment) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Point1(self: win32more.Windows.UI.Xaml.Media.IQuadraticBezierSegment, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_mixinmethod
    def get_Point2(self: win32more.Windows.UI.Xaml.Media.IQuadraticBezierSegment) -> win32more.Windows.Foundation.Point: ...
    @winrt_mixinmethod
    def put_Point2(self: win32more.Windows.UI.Xaml.Media.IQuadraticBezierSegment, value: win32more.Windows.Foundation.Point) -> Void: ...
    @winrt_classmethod
    def get_Point1Property(cls: win32more.Windows.UI.Xaml.Media.IQuadraticBezierSegmentStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_Point2Property(cls: win32more.Windows.UI.Xaml.Media.IQuadraticBezierSegmentStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Point1 = property(get_Point1, put_Point1)
    Point2 = property(get_Point2, put_Point2)
    _QuadraticBezierSegment_Meta_.Point1Property = property(get_Point1Property, None)
    _QuadraticBezierSegment_Meta_.Point2Property = property(get_Point2Property, None)
class RateChangedRoutedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Media.IRateChangedRoutedEventArgs
    _classid_ = 'Windows.UI.Xaml.Media.RateChangedRoutedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.RateChangedRoutedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.RateChangedRoutedEventArgs: ...
class RateChangedRoutedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{08e9a257-ae05-489b-8839-28c6225d2349}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Media.RateChangedRoutedEventArgs) -> Void: ...
class _RectangleGeometry_Meta_(ComPtr.__class__):
    pass
class RectangleGeometry(ComPtr, metaclass=_RectangleGeometry_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Geometry
    default_interface: win32more.Windows.UI.Xaml.Media.IRectangleGeometry
    _classid_ = 'Windows.UI.Xaml.Media.RectangleGeometry'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.RectangleGeometry.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.RectangleGeometry: ...
    @winrt_mixinmethod
    def get_Rect(self: win32more.Windows.UI.Xaml.Media.IRectangleGeometry) -> win32more.Windows.Foundation.Rect: ...
    @winrt_mixinmethod
    def put_Rect(self: win32more.Windows.UI.Xaml.Media.IRectangleGeometry, value: win32more.Windows.Foundation.Rect) -> Void: ...
    @winrt_classmethod
    def get_RectProperty(cls: win32more.Windows.UI.Xaml.Media.IRectangleGeometryStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Rect = property(get_Rect, put_Rect)
    _RectangleGeometry_Meta_.RectProperty = property(get_RectProperty, None)
class RenderedEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Media.IRenderedEventArgs
    _classid_ = 'Windows.UI.Xaml.Media.RenderedEventArgs'
    @winrt_mixinmethod
    def get_FrameDuration(self: win32more.Windows.UI.Xaml.Media.IRenderedEventArgs) -> win32more.Windows.Foundation.TimeSpan: ...
    FrameDuration = property(get_FrameDuration, None)
class RenderingEventArgs(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Media.IRenderingEventArgs
    _classid_ = 'Windows.UI.Xaml.Media.RenderingEventArgs'
    @winrt_mixinmethod
    def get_RenderingTime(self: win32more.Windows.UI.Xaml.Media.IRenderingEventArgs) -> win32more.Windows.Foundation.TimeSpan: ...
    RenderingTime = property(get_RenderingTime, None)
class RevealBackgroundBrush(ComPtr):
    extends: win32more.Windows.UI.Xaml.Media.RevealBrush
    default_interface: win32more.Windows.UI.Xaml.Media.IRevealBackgroundBrush
    _classid_ = 'Windows.UI.Xaml.Media.RevealBackgroundBrush'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.RevealBackgroundBrush.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Media.IRevealBackgroundBrushFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.RevealBackgroundBrush: ...
class RevealBorderBrush(ComPtr):
    extends: win32more.Windows.UI.Xaml.Media.RevealBrush
    default_interface: win32more.Windows.UI.Xaml.Media.IRevealBorderBrush
    _classid_ = 'Windows.UI.Xaml.Media.RevealBorderBrush'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.RevealBorderBrush.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Media.IRevealBorderBrushFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.RevealBorderBrush: ...
class _RevealBrush_Meta_(ComPtr.__class__):
    pass
class RevealBrush(ComPtr, metaclass=_RevealBrush_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.XamlCompositionBrushBase
    default_interface: win32more.Windows.UI.Xaml.Media.IRevealBrush
    _classid_ = 'Windows.UI.Xaml.Media.RevealBrush'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.RevealBrush.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Media.IRevealBrushFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.RevealBrush: ...
    @winrt_mixinmethod
    def get_Color(self: win32more.Windows.UI.Xaml.Media.IRevealBrush) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: win32more.Windows.UI.Xaml.Media.IRevealBrush, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_TargetTheme(self: win32more.Windows.UI.Xaml.Media.IRevealBrush) -> win32more.Windows.UI.Xaml.ApplicationTheme: ...
    @winrt_mixinmethod
    def put_TargetTheme(self: win32more.Windows.UI.Xaml.Media.IRevealBrush, value: win32more.Windows.UI.Xaml.ApplicationTheme) -> Void: ...
    @winrt_mixinmethod
    def get_AlwaysUseFallback(self: win32more.Windows.UI.Xaml.Media.IRevealBrush) -> Boolean: ...
    @winrt_mixinmethod
    def put_AlwaysUseFallback(self: win32more.Windows.UI.Xaml.Media.IRevealBrush, value: Boolean) -> Void: ...
    @winrt_classmethod
    def get_ColorProperty(cls: win32more.Windows.UI.Xaml.Media.IRevealBrushStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TargetThemeProperty(cls: win32more.Windows.UI.Xaml.Media.IRevealBrushStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AlwaysUseFallbackProperty(cls: win32more.Windows.UI.Xaml.Media.IRevealBrushStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StateProperty(cls: win32more.Windows.UI.Xaml.Media.IRevealBrushStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def SetState(cls: win32more.Windows.UI.Xaml.Media.IRevealBrushStatics, element: win32more.Windows.UI.Xaml.UIElement, value: win32more.Windows.UI.Xaml.Media.RevealBrushState) -> Void: ...
    @winrt_classmethod
    def GetState(cls: win32more.Windows.UI.Xaml.Media.IRevealBrushStatics, element: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.UI.Xaml.Media.RevealBrushState: ...
    AlwaysUseFallback = property(get_AlwaysUseFallback, put_AlwaysUseFallback)
    Color = property(get_Color, put_Color)
    TargetTheme = property(get_TargetTheme, put_TargetTheme)
    _RevealBrush_Meta_.AlwaysUseFallbackProperty = property(get_AlwaysUseFallbackProperty, None)
    _RevealBrush_Meta_.ColorProperty = property(get_ColorProperty, None)
    _RevealBrush_Meta_.StateProperty = property(get_StateProperty, None)
    _RevealBrush_Meta_.TargetThemeProperty = property(get_TargetThemeProperty, None)
class RevealBrushState(Enum, Int32):
    Normal = 0
    PointerOver = 1
    Pressed = 2
class _RotateTransform_Meta_(ComPtr.__class__):
    pass
class RotateTransform(ComPtr, metaclass=_RotateTransform_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Transform
    default_interface: win32more.Windows.UI.Xaml.Media.IRotateTransform
    _classid_ = 'Windows.UI.Xaml.Media.RotateTransform'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.RotateTransform.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.RotateTransform: ...
    @winrt_mixinmethod
    def get_CenterX(self: win32more.Windows.UI.Xaml.Media.IRotateTransform) -> Double: ...
    @winrt_mixinmethod
    def put_CenterX(self: win32more.Windows.UI.Xaml.Media.IRotateTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_CenterY(self: win32more.Windows.UI.Xaml.Media.IRotateTransform) -> Double: ...
    @winrt_mixinmethod
    def put_CenterY(self: win32more.Windows.UI.Xaml.Media.IRotateTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Angle(self: win32more.Windows.UI.Xaml.Media.IRotateTransform) -> Double: ...
    @winrt_mixinmethod
    def put_Angle(self: win32more.Windows.UI.Xaml.Media.IRotateTransform, value: Double) -> Void: ...
    @winrt_classmethod
    def get_CenterXProperty(cls: win32more.Windows.UI.Xaml.Media.IRotateTransformStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CenterYProperty(cls: win32more.Windows.UI.Xaml.Media.IRotateTransformStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AngleProperty(cls: win32more.Windows.UI.Xaml.Media.IRotateTransformStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Angle = property(get_Angle, put_Angle)
    CenterX = property(get_CenterX, put_CenterX)
    CenterY = property(get_CenterY, put_CenterY)
    _RotateTransform_Meta_.AngleProperty = property(get_AngleProperty, None)
    _RotateTransform_Meta_.CenterXProperty = property(get_CenterXProperty, None)
    _RotateTransform_Meta_.CenterYProperty = property(get_CenterYProperty, None)
class _ScaleTransform_Meta_(ComPtr.__class__):
    pass
class ScaleTransform(ComPtr, metaclass=_ScaleTransform_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Transform
    default_interface: win32more.Windows.UI.Xaml.Media.IScaleTransform
    _classid_ = 'Windows.UI.Xaml.Media.ScaleTransform'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.ScaleTransform.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.ScaleTransform: ...
    @winrt_mixinmethod
    def get_CenterX(self: win32more.Windows.UI.Xaml.Media.IScaleTransform) -> Double: ...
    @winrt_mixinmethod
    def put_CenterX(self: win32more.Windows.UI.Xaml.Media.IScaleTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_CenterY(self: win32more.Windows.UI.Xaml.Media.IScaleTransform) -> Double: ...
    @winrt_mixinmethod
    def put_CenterY(self: win32more.Windows.UI.Xaml.Media.IScaleTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleX(self: win32more.Windows.UI.Xaml.Media.IScaleTransform) -> Double: ...
    @winrt_mixinmethod
    def put_ScaleX(self: win32more.Windows.UI.Xaml.Media.IScaleTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_ScaleY(self: win32more.Windows.UI.Xaml.Media.IScaleTransform) -> Double: ...
    @winrt_mixinmethod
    def put_ScaleY(self: win32more.Windows.UI.Xaml.Media.IScaleTransform, value: Double) -> Void: ...
    @winrt_classmethod
    def get_CenterXProperty(cls: win32more.Windows.UI.Xaml.Media.IScaleTransformStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CenterYProperty(cls: win32more.Windows.UI.Xaml.Media.IScaleTransformStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ScaleXProperty(cls: win32more.Windows.UI.Xaml.Media.IScaleTransformStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_ScaleYProperty(cls: win32more.Windows.UI.Xaml.Media.IScaleTransformStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    CenterX = property(get_CenterX, put_CenterX)
    CenterY = property(get_CenterY, put_CenterY)
    ScaleX = property(get_ScaleX, put_ScaleX)
    ScaleY = property(get_ScaleY, put_ScaleY)
    _ScaleTransform_Meta_.CenterXProperty = property(get_CenterXProperty, None)
    _ScaleTransform_Meta_.CenterYProperty = property(get_CenterYProperty, None)
    _ScaleTransform_Meta_.ScaleXProperty = property(get_ScaleXProperty, None)
    _ScaleTransform_Meta_.ScaleYProperty = property(get_ScaleYProperty, None)
class Shadow(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Media.IShadow
    _classid_ = 'Windows.UI.Xaml.Media.Shadow'
class _SkewTransform_Meta_(ComPtr.__class__):
    pass
class SkewTransform(ComPtr, metaclass=_SkewTransform_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Transform
    default_interface: win32more.Windows.UI.Xaml.Media.ISkewTransform
    _classid_ = 'Windows.UI.Xaml.Media.SkewTransform'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.SkewTransform.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.SkewTransform: ...
    @winrt_mixinmethod
    def get_CenterX(self: win32more.Windows.UI.Xaml.Media.ISkewTransform) -> Double: ...
    @winrt_mixinmethod
    def put_CenterX(self: win32more.Windows.UI.Xaml.Media.ISkewTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_CenterY(self: win32more.Windows.UI.Xaml.Media.ISkewTransform) -> Double: ...
    @winrt_mixinmethod
    def put_CenterY(self: win32more.Windows.UI.Xaml.Media.ISkewTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_AngleX(self: win32more.Windows.UI.Xaml.Media.ISkewTransform) -> Double: ...
    @winrt_mixinmethod
    def put_AngleX(self: win32more.Windows.UI.Xaml.Media.ISkewTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_AngleY(self: win32more.Windows.UI.Xaml.Media.ISkewTransform) -> Double: ...
    @winrt_mixinmethod
    def put_AngleY(self: win32more.Windows.UI.Xaml.Media.ISkewTransform, value: Double) -> Void: ...
    @winrt_classmethod
    def get_CenterXProperty(cls: win32more.Windows.UI.Xaml.Media.ISkewTransformStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_CenterYProperty(cls: win32more.Windows.UI.Xaml.Media.ISkewTransformStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AngleXProperty(cls: win32more.Windows.UI.Xaml.Media.ISkewTransformStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AngleYProperty(cls: win32more.Windows.UI.Xaml.Media.ISkewTransformStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
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
    extends: win32more.Windows.UI.Xaml.Media.Brush
    default_interface: win32more.Windows.UI.Xaml.Media.ISolidColorBrush
    _classid_ = 'Windows.UI.Xaml.Media.SolidColorBrush'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.SolidColorBrush.CreateInstance(*args))
        elif len(args) == 1:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.SolidColorBrush.CreateInstanceWithColor(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.SolidColorBrush: ...
    @winrt_factorymethod
    def CreateInstanceWithColor(cls: win32more.Windows.UI.Xaml.Media.ISolidColorBrushFactory, color: win32more.Windows.UI.Color) -> win32more.Windows.UI.Xaml.Media.SolidColorBrush: ...
    @winrt_mixinmethod
    def get_Color(self: win32more.Windows.UI.Xaml.Media.ISolidColorBrush) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_Color(self: win32more.Windows.UI.Xaml.Media.ISolidColorBrush, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_classmethod
    def get_ColorProperty(cls: win32more.Windows.UI.Xaml.Media.ISolidColorBrushStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Color = property(get_Color, put_Color)
    _SolidColorBrush_Meta_.ColorProperty = property(get_ColorProperty, None)
class Stereo3DVideoPackingMode(Enum, Int32):
    None_ = 0
    SideBySide = 1
    TopBottom = 2
class Stereo3DVideoRenderMode(Enum, Int32):
    Mono = 0
    Stereo = 1
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
class ThemeShadow(ComPtr):
    extends: win32more.Windows.UI.Xaml.Media.Shadow
    default_interface: win32more.Windows.UI.Xaml.Media.IThemeShadow
    _classid_ = 'Windows.UI.Xaml.Media.ThemeShadow'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.ThemeShadow.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Media.IThemeShadowFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.ThemeShadow: ...
    @winrt_mixinmethod
    def get_Receivers(self: win32more.Windows.UI.Xaml.Media.IThemeShadow) -> win32more.Windows.UI.Xaml.UIElementWeakCollection: ...
    Receivers = property(get_Receivers, None)
class _TileBrush_Meta_(ComPtr.__class__):
    pass
class TileBrush(ComPtr, metaclass=_TileBrush_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Brush
    default_interface: win32more.Windows.UI.Xaml.Media.ITileBrush
    _classid_ = 'Windows.UI.Xaml.Media.TileBrush'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.TileBrush.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Media.ITileBrushFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.TileBrush: ...
    @winrt_mixinmethod
    def get_AlignmentX(self: win32more.Windows.UI.Xaml.Media.ITileBrush) -> win32more.Windows.UI.Xaml.Media.AlignmentX: ...
    @winrt_mixinmethod
    def put_AlignmentX(self: win32more.Windows.UI.Xaml.Media.ITileBrush, value: win32more.Windows.UI.Xaml.Media.AlignmentX) -> Void: ...
    @winrt_mixinmethod
    def get_AlignmentY(self: win32more.Windows.UI.Xaml.Media.ITileBrush) -> win32more.Windows.UI.Xaml.Media.AlignmentY: ...
    @winrt_mixinmethod
    def put_AlignmentY(self: win32more.Windows.UI.Xaml.Media.ITileBrush, value: win32more.Windows.UI.Xaml.Media.AlignmentY) -> Void: ...
    @winrt_mixinmethod
    def get_Stretch(self: win32more.Windows.UI.Xaml.Media.ITileBrush) -> win32more.Windows.UI.Xaml.Media.Stretch: ...
    @winrt_mixinmethod
    def put_Stretch(self: win32more.Windows.UI.Xaml.Media.ITileBrush, value: win32more.Windows.UI.Xaml.Media.Stretch) -> Void: ...
    @winrt_classmethod
    def get_AlignmentXProperty(cls: win32more.Windows.UI.Xaml.Media.ITileBrushStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_AlignmentYProperty(cls: win32more.Windows.UI.Xaml.Media.ITileBrushStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StretchProperty(cls: win32more.Windows.UI.Xaml.Media.ITileBrushStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    AlignmentX = property(get_AlignmentX, put_AlignmentX)
    AlignmentY = property(get_AlignmentY, put_AlignmentY)
    Stretch = property(get_Stretch, put_Stretch)
    _TileBrush_Meta_.AlignmentXProperty = property(get_AlignmentXProperty, None)
    _TileBrush_Meta_.AlignmentYProperty = property(get_AlignmentYProperty, None)
    _TileBrush_Meta_.StretchProperty = property(get_StretchProperty, None)
class _TimelineMarker_Meta_(ComPtr.__class__):
    pass
class TimelineMarker(ComPtr, metaclass=_TimelineMarker_Meta_):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Media.ITimelineMarker
    _classid_ = 'Windows.UI.Xaml.Media.TimelineMarker'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.TimelineMarker.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.TimelineMarker: ...
    @winrt_mixinmethod
    def get_Time(self: win32more.Windows.UI.Xaml.Media.ITimelineMarker) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def put_Time(self: win32more.Windows.UI.Xaml.Media.ITimelineMarker, value: win32more.Windows.Foundation.TimeSpan) -> Void: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.UI.Xaml.Media.ITimelineMarker) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Type(self: win32more.Windows.UI.Xaml.Media.ITimelineMarker, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Text(self: win32more.Windows.UI.Xaml.Media.ITimelineMarker) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Text(self: win32more.Windows.UI.Xaml.Media.ITimelineMarker, value: WinRT_String) -> Void: ...
    @winrt_classmethod
    def get_TimeProperty(cls: win32more.Windows.UI.Xaml.Media.ITimelineMarkerStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TypeProperty(cls: win32more.Windows.UI.Xaml.Media.ITimelineMarkerStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_TextProperty(cls: win32more.Windows.UI.Xaml.Media.ITimelineMarkerStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Text = property(get_Text, put_Text)
    Time = property(get_Time, put_Time)
    Type = property(get_Type, put_Type)
    _TimelineMarker_Meta_.TextProperty = property(get_TextProperty, None)
    _TimelineMarker_Meta_.TimeProperty = property(get_TimeProperty, None)
    _TimelineMarker_Meta_.TypeProperty = property(get_TypeProperty, None)
class TimelineMarkerCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Windows.UI.Xaml.Media.TimelineMarker]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.TimelineMarker]
    _classid_ = 'Windows.UI.Xaml.Media.TimelineMarkerCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.TimelineMarkerCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.TimelineMarkerCollection: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.TimelineMarker], index: UInt32) -> win32more.Windows.UI.Xaml.Media.TimelineMarker: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.TimelineMarker]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.TimelineMarker]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.Media.TimelineMarker]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.TimelineMarker], value: win32more.Windows.UI.Xaml.Media.TimelineMarker, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.TimelineMarker], index: UInt32, value: win32more.Windows.UI.Xaml.Media.TimelineMarker) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.TimelineMarker], index: UInt32, value: win32more.Windows.UI.Xaml.Media.TimelineMarker) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.TimelineMarker], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.TimelineMarker], value: win32more.Windows.UI.Xaml.Media.TimelineMarker) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.TimelineMarker]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.TimelineMarker]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.TimelineMarker], startIndex: UInt32, items: FillArray[win32more.Windows.UI.Xaml.Media.TimelineMarker]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.TimelineMarker], items: PassArray[win32more.Windows.UI.Xaml.Media.TimelineMarker]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.Media.TimelineMarker]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.UI.Xaml.Media.TimelineMarker]: ...
    Size = property(get_Size, None)
class TimelineMarkerRoutedEventArgs(ComPtr):
    extends: win32more.Windows.UI.Xaml.RoutedEventArgs
    default_interface: win32more.Windows.UI.Xaml.Media.ITimelineMarkerRoutedEventArgs
    _classid_ = 'Windows.UI.Xaml.Media.TimelineMarkerRoutedEventArgs'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.TimelineMarkerRoutedEventArgs.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.TimelineMarkerRoutedEventArgs: ...
    @winrt_mixinmethod
    def get_Marker(self: win32more.Windows.UI.Xaml.Media.ITimelineMarkerRoutedEventArgs) -> win32more.Windows.UI.Xaml.Media.TimelineMarker: ...
    @winrt_mixinmethod
    def put_Marker(self: win32more.Windows.UI.Xaml.Media.ITimelineMarkerRoutedEventArgs, value: win32more.Windows.UI.Xaml.Media.TimelineMarker) -> Void: ...
    Marker = property(get_Marker, put_Marker)
class TimelineMarkerRoutedEventHandler(MulticastDelegate):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{72e2fa9c-6dea-4cbe-a159-06ce95fbeced}')
    @winrt_commethod(3)
    def Invoke(self, sender: win32more.Windows.Win32.System.WinRT.IInspectable, e: win32more.Windows.UI.Xaml.Media.TimelineMarkerRoutedEventArgs) -> Void: ...
class Transform(ComPtr):
    extends: win32more.Windows.UI.Xaml.Media.GeneralTransform
    default_interface: win32more.Windows.UI.Xaml.Media.ITransform
    _classid_ = 'Windows.UI.Xaml.Media.Transform'
class TransformCollection(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    implements: Tuple[SequenceProtocol[win32more.Windows.UI.Xaml.Media.Transform]]
    default_interface: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Transform]
    _classid_ = 'Windows.UI.Xaml.Media.TransformCollection'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.TransformCollection.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.TransformCollection: ...
    @winrt_mixinmethod
    def GetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Transform], index: UInt32) -> win32more.Windows.UI.Xaml.Media.Transform: ...
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Transform]) -> UInt32: ...
    @winrt_mixinmethod
    def GetView(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Transform]) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.Media.Transform]: ...
    @winrt_mixinmethod
    def IndexOf(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Transform], value: win32more.Windows.UI.Xaml.Media.Transform, index: POINTER(UInt32)) -> Boolean: ...
    @winrt_mixinmethod
    def SetAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Transform], index: UInt32, value: win32more.Windows.UI.Xaml.Media.Transform) -> Void: ...
    @winrt_mixinmethod
    def InsertAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Transform], index: UInt32, value: win32more.Windows.UI.Xaml.Media.Transform) -> Void: ...
    @winrt_mixinmethod
    def RemoveAt(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Transform], index: UInt32) -> Void: ...
    @winrt_mixinmethod
    def Append(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Transform], value: win32more.Windows.UI.Xaml.Media.Transform) -> Void: ...
    @winrt_mixinmethod
    def RemoveAtEnd(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Transform]) -> Void: ...
    @winrt_mixinmethod
    def Clear(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Transform]) -> Void: ...
    @winrt_mixinmethod
    def GetMany(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Transform], startIndex: UInt32, items: FillArray[win32more.Windows.UI.Xaml.Media.Transform]) -> UInt32: ...
    @winrt_mixinmethod
    def ReplaceAll(self: win32more.Windows.Foundation.Collections.IVector[win32more.Windows.UI.Xaml.Media.Transform], items: PassArray[win32more.Windows.UI.Xaml.Media.Transform]) -> Void: ...
    @winrt_mixinmethod
    def First(self: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.Media.Transform]) -> win32more.Windows.Foundation.Collections.IIterator[win32more.Windows.UI.Xaml.Media.Transform]: ...
    Size = property(get_Size, None)
class _TransformGroup_Meta_(ComPtr.__class__):
    pass
class TransformGroup(ComPtr, metaclass=_TransformGroup_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Transform
    default_interface: win32more.Windows.UI.Xaml.Media.ITransformGroup
    _classid_ = 'Windows.UI.Xaml.Media.TransformGroup'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.TransformGroup.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.TransformGroup: ...
    @winrt_mixinmethod
    def get_Children(self: win32more.Windows.UI.Xaml.Media.ITransformGroup) -> win32more.Windows.UI.Xaml.Media.TransformCollection: ...
    @winrt_mixinmethod
    def put_Children(self: win32more.Windows.UI.Xaml.Media.ITransformGroup, value: win32more.Windows.UI.Xaml.Media.TransformCollection) -> Void: ...
    @winrt_mixinmethod
    def get_Value(self: win32more.Windows.UI.Xaml.Media.ITransformGroup) -> win32more.Windows.UI.Xaml.Media.Matrix: ...
    @winrt_classmethod
    def get_ChildrenProperty(cls: win32more.Windows.UI.Xaml.Media.ITransformGroupStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Children = property(get_Children, put_Children)
    Value = property(get_Value, None)
    _TransformGroup_Meta_.ChildrenProperty = property(get_ChildrenProperty, None)
class _TranslateTransform_Meta_(ComPtr.__class__):
    pass
class TranslateTransform(ComPtr, metaclass=_TranslateTransform_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Transform
    default_interface: win32more.Windows.UI.Xaml.Media.ITranslateTransform
    _classid_ = 'Windows.UI.Xaml.Media.TranslateTransform'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.TranslateTransform.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Media.TranslateTransform: ...
    @winrt_mixinmethod
    def get_X(self: win32more.Windows.UI.Xaml.Media.ITranslateTransform) -> Double: ...
    @winrt_mixinmethod
    def put_X(self: win32more.Windows.UI.Xaml.Media.ITranslateTransform, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Y(self: win32more.Windows.UI.Xaml.Media.ITranslateTransform) -> Double: ...
    @winrt_mixinmethod
    def put_Y(self: win32more.Windows.UI.Xaml.Media.ITranslateTransform, value: Double) -> Void: ...
    @winrt_classmethod
    def get_XProperty(cls: win32more.Windows.UI.Xaml.Media.ITranslateTransformStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_YProperty(cls: win32more.Windows.UI.Xaml.Media.ITranslateTransformStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    X = property(get_X, put_X)
    Y = property(get_Y, put_Y)
    _TranslateTransform_Meta_.XProperty = property(get_XProperty, None)
    _TranslateTransform_Meta_.YProperty = property(get_YProperty, None)
class VisualTreeHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.UI.Xaml.Media.IVisualTreeHelper
    _classid_ = 'Windows.UI.Xaml.Media.VisualTreeHelper'
    @winrt_classmethod
    def GetOpenPopupsForXamlRoot(cls: win32more.Windows.UI.Xaml.Media.IVisualTreeHelperStatics3, xamlRoot: win32more.Windows.UI.Xaml.XamlRoot) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.Controls.Primitives.Popup]: ...
    @winrt_classmethod
    def GetOpenPopups(cls: win32more.Windows.UI.Xaml.Media.IVisualTreeHelperStatics2, window: win32more.Windows.UI.Xaml.Window) -> win32more.Windows.Foundation.Collections.IVectorView[win32more.Windows.UI.Xaml.Controls.Primitives.Popup]: ...
    @winrt_classmethod
    def FindElementsInHostCoordinatesPoint(cls: win32more.Windows.UI.Xaml.Media.IVisualTreeHelperStatics, intersectingPoint: win32more.Windows.Foundation.Point, subtree: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.UIElement]: ...
    @winrt_classmethod
    def FindElementsInHostCoordinatesRect(cls: win32more.Windows.UI.Xaml.Media.IVisualTreeHelperStatics, intersectingRect: win32more.Windows.Foundation.Rect, subtree: win32more.Windows.UI.Xaml.UIElement) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.UIElement]: ...
    @winrt_classmethod
    def FindAllElementsInHostCoordinatesPoint(cls: win32more.Windows.UI.Xaml.Media.IVisualTreeHelperStatics, intersectingPoint: win32more.Windows.Foundation.Point, subtree: win32more.Windows.UI.Xaml.UIElement, includeAllElements: Boolean) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.UIElement]: ...
    @winrt_classmethod
    def FindAllElementsInHostCoordinatesRect(cls: win32more.Windows.UI.Xaml.Media.IVisualTreeHelperStatics, intersectingRect: win32more.Windows.Foundation.Rect, subtree: win32more.Windows.UI.Xaml.UIElement, includeAllElements: Boolean) -> win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.UI.Xaml.UIElement]: ...
    @winrt_classmethod
    def GetChild(cls: win32more.Windows.UI.Xaml.Media.IVisualTreeHelperStatics, reference: win32more.Windows.UI.Xaml.DependencyObject, childIndex: Int32) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_classmethod
    def GetChildrenCount(cls: win32more.Windows.UI.Xaml.Media.IVisualTreeHelperStatics, reference: win32more.Windows.UI.Xaml.DependencyObject) -> Int32: ...
    @winrt_classmethod
    def GetParent(cls: win32more.Windows.UI.Xaml.Media.IVisualTreeHelperStatics, reference: win32more.Windows.UI.Xaml.DependencyObject) -> win32more.Windows.UI.Xaml.DependencyObject: ...
    @winrt_classmethod
    def DisconnectChildrenRecursive(cls: win32more.Windows.UI.Xaml.Media.IVisualTreeHelperStatics, element: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
class _XamlCompositionBrushBase_Meta_(ComPtr.__class__):
    pass
class XamlCompositionBrushBase(ComPtr, metaclass=_XamlCompositionBrushBase_Meta_):
    extends: win32more.Windows.UI.Xaml.Media.Brush
    default_interface: win32more.Windows.UI.Xaml.Media.IXamlCompositionBrushBase
    _classid_ = 'Windows.UI.Xaml.Media.XamlCompositionBrushBase'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.XamlCompositionBrushBase.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Media.IXamlCompositionBrushBaseFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.XamlCompositionBrushBase: ...
    @winrt_mixinmethod
    def get_FallbackColor(self: win32more.Windows.UI.Xaml.Media.IXamlCompositionBrushBase) -> win32more.Windows.UI.Color: ...
    @winrt_mixinmethod
    def put_FallbackColor(self: win32more.Windows.UI.Xaml.Media.IXamlCompositionBrushBase, value: win32more.Windows.UI.Color) -> Void: ...
    @winrt_mixinmethod
    def get_CompositionBrush(self: win32more.Windows.UI.Xaml.Media.IXamlCompositionBrushBaseProtected) -> win32more.Windows.UI.Composition.CompositionBrush: ...
    @winrt_mixinmethod
    def put_CompositionBrush(self: win32more.Windows.UI.Xaml.Media.IXamlCompositionBrushBaseProtected, value: win32more.Windows.UI.Composition.CompositionBrush) -> Void: ...
    @winrt_mixinmethod
    def OnConnected(self: win32more.Windows.UI.Xaml.Media.IXamlCompositionBrushBaseOverrides) -> Void: ...
    @winrt_mixinmethod
    def OnDisconnected(self: win32more.Windows.UI.Xaml.Media.IXamlCompositionBrushBaseOverrides) -> Void: ...
    @winrt_classmethod
    def get_FallbackColorProperty(cls: win32more.Windows.UI.Xaml.Media.IXamlCompositionBrushBaseStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    CompositionBrush = property(get_CompositionBrush, put_CompositionBrush)
    FallbackColor = property(get_FallbackColor, put_FallbackColor)
    _XamlCompositionBrushBase_Meta_.FallbackColorProperty = property(get_FallbackColorProperty, None)
class XamlLight(ComPtr):
    extends: win32more.Windows.UI.Xaml.DependencyObject
    default_interface: win32more.Windows.UI.Xaml.Media.IXamlLight
    _classid_ = 'Windows.UI.Xaml.Media.XamlLight'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Windows.UI.Xaml.Media.XamlLight.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Media.IXamlLightFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Media.XamlLight: ...
    @winrt_mixinmethod
    def get_CompositionLight(self: win32more.Windows.UI.Xaml.Media.IXamlLightProtected) -> win32more.Windows.UI.Composition.CompositionLight: ...
    @winrt_mixinmethod
    def put_CompositionLight(self: win32more.Windows.UI.Xaml.Media.IXamlLightProtected, value: win32more.Windows.UI.Composition.CompositionLight) -> Void: ...
    @winrt_mixinmethod
    def GetId(self: win32more.Windows.UI.Xaml.Media.IXamlLightOverrides) -> WinRT_String: ...
    @winrt_mixinmethod
    def OnConnected(self: win32more.Windows.UI.Xaml.Media.IXamlLightOverrides, newElement: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_mixinmethod
    def OnDisconnected(self: win32more.Windows.UI.Xaml.Media.IXamlLightOverrides, oldElement: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_classmethod
    def AddTargetElement(cls: win32more.Windows.UI.Xaml.Media.IXamlLightStatics, lightId: WinRT_String, element: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_classmethod
    def RemoveTargetElement(cls: win32more.Windows.UI.Xaml.Media.IXamlLightStatics, lightId: WinRT_String, element: win32more.Windows.UI.Xaml.UIElement) -> Void: ...
    @winrt_classmethod
    def AddTargetBrush(cls: win32more.Windows.UI.Xaml.Media.IXamlLightStatics, lightId: WinRT_String, brush: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_classmethod
    def RemoveTargetBrush(cls: win32more.Windows.UI.Xaml.Media.IXamlLightStatics, lightId: WinRT_String, brush: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    CompositionLight = property(get_CompositionLight, put_CompositionLight)


make_ready(__name__)
