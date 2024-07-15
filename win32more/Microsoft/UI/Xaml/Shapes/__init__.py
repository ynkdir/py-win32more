from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
from win32more._winrt import AwaitableProtocol, ContextManagerProtocol, FillArray, Generic, IterableProtocol, K, MappingProtocol, MulticastDelegate, PassArray, ReceiveArray, SequenceProtocol, T, TProgress, TResult, TSender, Tuple, V, WinRT_String, event, winrt_activatemethod, winrt_classmethod, winrt_commethod, winrt_factorymethod, winrt_mixinmethod, winrt_overload
import win32more.Microsoft.UI.Composition
import win32more.Microsoft.UI.Xaml
import win32more.Microsoft.UI.Xaml.Media
import win32more.Microsoft.UI.Xaml.Shapes
import win32more.Windows.Win32.System.WinRT
class Ellipse(ComPtr):
    extends: win32more.Microsoft.UI.Xaml.Shapes.Shape
    default_interface: win32more.Microsoft.UI.Xaml.Shapes.IEllipse
    _classid_ = 'Microsoft.UI.Xaml.Shapes.Ellipse'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Shapes.Ellipse.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Shapes.Ellipse: ...
class IEllipse(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Shapes.IEllipse'
    _iid_ = Guid('{805c39aa-fa8a-5e0b-9847-4ab81b42a3df}')
class ILine(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Shapes.ILine'
    _iid_ = Guid('{507b3858-af7e-559b-a87e-4cc6a5d8ba96}')
    @winrt_commethod(6)
    def get_X1(self) -> Double: ...
    @winrt_commethod(7)
    def put_X1(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_Y1(self) -> Double: ...
    @winrt_commethod(9)
    def put_Y1(self, value: Double) -> Void: ...
    @winrt_commethod(10)
    def get_X2(self) -> Double: ...
    @winrt_commethod(11)
    def put_X2(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def get_Y2(self) -> Double: ...
    @winrt_commethod(13)
    def put_Y2(self, value: Double) -> Void: ...
    X1 = property(get_X1, put_X1)
    X2 = property(get_X2, put_X2)
    Y1 = property(get_Y1, put_Y1)
    Y2 = property(get_Y2, put_Y2)
class ILineStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Shapes.ILineStatics'
    _iid_ = Guid('{a425bf93-f1f3-5dcb-997e-b6a26f7ae8c0}')
    @winrt_commethod(6)
    def get_X1Property(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_Y1Property(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_X2Property(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_Y2Property(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    X1Property = property(get_X1Property, None)
    X2Property = property(get_X2Property, None)
    Y1Property = property(get_Y1Property, None)
    Y2Property = property(get_Y2Property, None)
class IPath(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Shapes.IPath'
    _iid_ = Guid('{757d1cd8-0ec0-55c5-b400-66657e493e78}')
    @winrt_commethod(6)
    def get_Data(self) -> win32more.Microsoft.UI.Xaml.Media.Geometry: ...
    @winrt_commethod(7)
    def put_Data(self, value: win32more.Microsoft.UI.Xaml.Media.Geometry) -> Void: ...
    Data = property(get_Data, put_Data)
class IPathFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Shapes.IPathFactory'
    _iid_ = Guid('{5e82e4c9-7502-5b1f-b940-c3346a71362a}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Shapes.Path: ...
class IPathStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Shapes.IPathStatics'
    _iid_ = Guid('{2146d36f-721c-5b54-af7d-60f3adc4fbca}')
    @winrt_commethod(6)
    def get_DataProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    DataProperty = property(get_DataProperty, None)
class IPolygon(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Shapes.IPolygon'
    _iid_ = Guid('{fa126347-d1d4-54dd-b1a4-c35019397944}')
    @winrt_commethod(6)
    def get_FillRule(self) -> win32more.Microsoft.UI.Xaml.Media.FillRule: ...
    @winrt_commethod(7)
    def put_FillRule(self, value: win32more.Microsoft.UI.Xaml.Media.FillRule) -> Void: ...
    @winrt_commethod(8)
    def get_Points(self) -> win32more.Microsoft.UI.Xaml.Media.PointCollection: ...
    @winrt_commethod(9)
    def put_Points(self, value: win32more.Microsoft.UI.Xaml.Media.PointCollection) -> Void: ...
    FillRule = property(get_FillRule, put_FillRule)
    Points = property(get_Points, put_Points)
class IPolygonStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Shapes.IPolygonStatics'
    _iid_ = Guid('{85ddbada-9e37-5971-a9aa-dce31f9cf67a}')
    @winrt_commethod(6)
    def get_FillRuleProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_PointsProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    FillRuleProperty = property(get_FillRuleProperty, None)
    PointsProperty = property(get_PointsProperty, None)
class IPolyline(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Shapes.IPolyline'
    _iid_ = Guid('{c7f0bec6-184c-5d96-8102-04dd211e100c}')
    @winrt_commethod(6)
    def get_FillRule(self) -> win32more.Microsoft.UI.Xaml.Media.FillRule: ...
    @winrt_commethod(7)
    def put_FillRule(self, value: win32more.Microsoft.UI.Xaml.Media.FillRule) -> Void: ...
    @winrt_commethod(8)
    def get_Points(self) -> win32more.Microsoft.UI.Xaml.Media.PointCollection: ...
    @winrt_commethod(9)
    def put_Points(self, value: win32more.Microsoft.UI.Xaml.Media.PointCollection) -> Void: ...
    FillRule = property(get_FillRule, put_FillRule)
    Points = property(get_Points, put_Points)
class IPolylineStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Shapes.IPolylineStatics'
    _iid_ = Guid('{48840fe7-d735-5080-9c6d-2862665cdda0}')
    @winrt_commethod(6)
    def get_FillRuleProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_PointsProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    FillRuleProperty = property(get_FillRuleProperty, None)
    PointsProperty = property(get_PointsProperty, None)
class IRectangle(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Shapes.IRectangle'
    _iid_ = Guid('{bf7d30b9-152c-556e-9f10-d0b7eba4e52f}')
    @winrt_commethod(6)
    def get_RadiusX(self) -> Double: ...
    @winrt_commethod(7)
    def put_RadiusX(self, value: Double) -> Void: ...
    @winrt_commethod(8)
    def get_RadiusY(self) -> Double: ...
    @winrt_commethod(9)
    def put_RadiusY(self, value: Double) -> Void: ...
    RadiusX = property(get_RadiusX, put_RadiusX)
    RadiusY = property(get_RadiusY, put_RadiusY)
class IRectangleStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Shapes.IRectangleStatics'
    _iid_ = Guid('{3cc3cc79-c332-5ad0-8743-1f1b1e670a86}')
    @winrt_commethod(6)
    def get_RadiusXProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_RadiusYProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    RadiusXProperty = property(get_RadiusXProperty, None)
    RadiusYProperty = property(get_RadiusYProperty, None)
class IShape(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Shapes.IShape'
    _iid_ = Guid('{9941aad3-6af2-5ba2-9085-8506d5f2485e}')
    @winrt_commethod(6)
    def get_Fill(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(7)
    def put_Fill(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(8)
    def get_Stroke(self) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_commethod(9)
    def put_Stroke(self, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(10)
    def get_StrokeMiterLimit(self) -> Double: ...
    @winrt_commethod(11)
    def put_StrokeMiterLimit(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def get_StrokeThickness(self) -> Double: ...
    @winrt_commethod(13)
    def put_StrokeThickness(self, value: Double) -> Void: ...
    @winrt_commethod(14)
    def get_StrokeStartLineCap(self) -> win32more.Microsoft.UI.Xaml.Media.PenLineCap: ...
    @winrt_commethod(15)
    def put_StrokeStartLineCap(self, value: win32more.Microsoft.UI.Xaml.Media.PenLineCap) -> Void: ...
    @winrt_commethod(16)
    def get_StrokeEndLineCap(self) -> win32more.Microsoft.UI.Xaml.Media.PenLineCap: ...
    @winrt_commethod(17)
    def put_StrokeEndLineCap(self, value: win32more.Microsoft.UI.Xaml.Media.PenLineCap) -> Void: ...
    @winrt_commethod(18)
    def get_StrokeLineJoin(self) -> win32more.Microsoft.UI.Xaml.Media.PenLineJoin: ...
    @winrt_commethod(19)
    def put_StrokeLineJoin(self, value: win32more.Microsoft.UI.Xaml.Media.PenLineJoin) -> Void: ...
    @winrt_commethod(20)
    def get_StrokeDashOffset(self) -> Double: ...
    @winrt_commethod(21)
    def put_StrokeDashOffset(self, value: Double) -> Void: ...
    @winrt_commethod(22)
    def get_StrokeDashCap(self) -> win32more.Microsoft.UI.Xaml.Media.PenLineCap: ...
    @winrt_commethod(23)
    def put_StrokeDashCap(self, value: win32more.Microsoft.UI.Xaml.Media.PenLineCap) -> Void: ...
    @winrt_commethod(24)
    def get_StrokeDashArray(self) -> win32more.Microsoft.UI.Xaml.Media.DoubleCollection: ...
    @winrt_commethod(25)
    def put_StrokeDashArray(self, value: win32more.Microsoft.UI.Xaml.Media.DoubleCollection) -> Void: ...
    @winrt_commethod(26)
    def get_Stretch(self) -> win32more.Microsoft.UI.Xaml.Media.Stretch: ...
    @winrt_commethod(27)
    def put_Stretch(self, value: win32more.Microsoft.UI.Xaml.Media.Stretch) -> Void: ...
    @winrt_commethod(28)
    def get_GeometryTransform(self) -> win32more.Microsoft.UI.Xaml.Media.Transform: ...
    @winrt_commethod(29)
    def GetAlphaMask(self) -> win32more.Microsoft.UI.Composition.CompositionBrush: ...
    Fill = property(get_Fill, put_Fill)
    GeometryTransform = property(get_GeometryTransform, None)
    Stretch = property(get_Stretch, put_Stretch)
    Stroke = property(get_Stroke, put_Stroke)
    StrokeDashArray = property(get_StrokeDashArray, put_StrokeDashArray)
    StrokeDashCap = property(get_StrokeDashCap, put_StrokeDashCap)
    StrokeDashOffset = property(get_StrokeDashOffset, put_StrokeDashOffset)
    StrokeEndLineCap = property(get_StrokeEndLineCap, put_StrokeEndLineCap)
    StrokeLineJoin = property(get_StrokeLineJoin, put_StrokeLineJoin)
    StrokeMiterLimit = property(get_StrokeMiterLimit, put_StrokeMiterLimit)
    StrokeStartLineCap = property(get_StrokeStartLineCap, put_StrokeStartLineCap)
    StrokeThickness = property(get_StrokeThickness, put_StrokeThickness)
class IShapeFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Shapes.IShapeFactory'
    _iid_ = Guid('{4fecafaf-8265-5252-ba5c-f43639f974a5}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Shapes.Shape: ...
class IShapeStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Microsoft.UI.Xaml.Shapes.IShapeStatics'
    _iid_ = Guid('{ea407c43-8a09-587a-958a-4dd17d217ce1}')
    @winrt_commethod(6)
    def get_FillProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_StrokeProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_StrokeMiterLimitProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_StrokeThicknessProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_StrokeStartLineCapProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_StrokeEndLineCapProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_StrokeLineJoinProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_StrokeDashOffsetProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_StrokeDashCapProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_StrokeDashArrayProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def get_StretchProperty(self) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    FillProperty = property(get_FillProperty, None)
    StretchProperty = property(get_StretchProperty, None)
    StrokeDashArrayProperty = property(get_StrokeDashArrayProperty, None)
    StrokeDashCapProperty = property(get_StrokeDashCapProperty, None)
    StrokeDashOffsetProperty = property(get_StrokeDashOffsetProperty, None)
    StrokeEndLineCapProperty = property(get_StrokeEndLineCapProperty, None)
    StrokeLineJoinProperty = property(get_StrokeLineJoinProperty, None)
    StrokeMiterLimitProperty = property(get_StrokeMiterLimitProperty, None)
    StrokeProperty = property(get_StrokeProperty, None)
    StrokeStartLineCapProperty = property(get_StrokeStartLineCapProperty, None)
    StrokeThicknessProperty = property(get_StrokeThicknessProperty, None)
class _Line_Meta_(ComPtr.__class__):
    pass
class Line(ComPtr, metaclass=_Line_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Shapes.Shape
    default_interface: win32more.Microsoft.UI.Xaml.Shapes.ILine
    _classid_ = 'Microsoft.UI.Xaml.Shapes.Line'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Shapes.Line.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Shapes.Line: ...
    @winrt_mixinmethod
    def get_X1(self: win32more.Microsoft.UI.Xaml.Shapes.ILine) -> Double: ...
    @winrt_mixinmethod
    def put_X1(self: win32more.Microsoft.UI.Xaml.Shapes.ILine, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Y1(self: win32more.Microsoft.UI.Xaml.Shapes.ILine) -> Double: ...
    @winrt_mixinmethod
    def put_Y1(self: win32more.Microsoft.UI.Xaml.Shapes.ILine, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_X2(self: win32more.Microsoft.UI.Xaml.Shapes.ILine) -> Double: ...
    @winrt_mixinmethod
    def put_X2(self: win32more.Microsoft.UI.Xaml.Shapes.ILine, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Y2(self: win32more.Microsoft.UI.Xaml.Shapes.ILine) -> Double: ...
    @winrt_mixinmethod
    def put_Y2(self: win32more.Microsoft.UI.Xaml.Shapes.ILine, value: Double) -> Void: ...
    @winrt_classmethod
    def get_X1Property(cls: win32more.Microsoft.UI.Xaml.Shapes.ILineStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_Y1Property(cls: win32more.Microsoft.UI.Xaml.Shapes.ILineStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_X2Property(cls: win32more.Microsoft.UI.Xaml.Shapes.ILineStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_Y2Property(cls: win32more.Microsoft.UI.Xaml.Shapes.ILineStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    X1 = property(get_X1, put_X1)
    X2 = property(get_X2, put_X2)
    Y1 = property(get_Y1, put_Y1)
    Y2 = property(get_Y2, put_Y2)
    _Line_Meta_.X1Property = property(get_X1Property, None)
    _Line_Meta_.X2Property = property(get_X2Property, None)
    _Line_Meta_.Y1Property = property(get_Y1Property, None)
    _Line_Meta_.Y2Property = property(get_Y2Property, None)
class _Path_Meta_(ComPtr.__class__):
    pass
class Path(ComPtr, metaclass=_Path_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Shapes.Shape
    default_interface: win32more.Microsoft.UI.Xaml.Shapes.IPath
    _classid_ = 'Microsoft.UI.Xaml.Shapes.Path'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Shapes.Path.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Shapes.IPathFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Shapes.Path: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Microsoft.UI.Xaml.Shapes.IPath) -> win32more.Microsoft.UI.Xaml.Media.Geometry: ...
    @winrt_mixinmethod
    def put_Data(self: win32more.Microsoft.UI.Xaml.Shapes.IPath, value: win32more.Microsoft.UI.Xaml.Media.Geometry) -> Void: ...
    @winrt_classmethod
    def get_DataProperty(cls: win32more.Microsoft.UI.Xaml.Shapes.IPathStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Data = property(get_Data, put_Data)
    _Path_Meta_.DataProperty = property(get_DataProperty, None)
class _Polygon_Meta_(ComPtr.__class__):
    pass
class Polygon(ComPtr, metaclass=_Polygon_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Shapes.Shape
    default_interface: win32more.Microsoft.UI.Xaml.Shapes.IPolygon
    _classid_ = 'Microsoft.UI.Xaml.Shapes.Polygon'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Shapes.Polygon.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Shapes.Polygon: ...
    @winrt_mixinmethod
    def get_FillRule(self: win32more.Microsoft.UI.Xaml.Shapes.IPolygon) -> win32more.Microsoft.UI.Xaml.Media.FillRule: ...
    @winrt_mixinmethod
    def put_FillRule(self: win32more.Microsoft.UI.Xaml.Shapes.IPolygon, value: win32more.Microsoft.UI.Xaml.Media.FillRule) -> Void: ...
    @winrt_mixinmethod
    def get_Points(self: win32more.Microsoft.UI.Xaml.Shapes.IPolygon) -> win32more.Microsoft.UI.Xaml.Media.PointCollection: ...
    @winrt_mixinmethod
    def put_Points(self: win32more.Microsoft.UI.Xaml.Shapes.IPolygon, value: win32more.Microsoft.UI.Xaml.Media.PointCollection) -> Void: ...
    @winrt_classmethod
    def get_FillRuleProperty(cls: win32more.Microsoft.UI.Xaml.Shapes.IPolygonStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PointsProperty(cls: win32more.Microsoft.UI.Xaml.Shapes.IPolygonStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    FillRule = property(get_FillRule, put_FillRule)
    Points = property(get_Points, put_Points)
    _Polygon_Meta_.FillRuleProperty = property(get_FillRuleProperty, None)
    _Polygon_Meta_.PointsProperty = property(get_PointsProperty, None)
class _Polyline_Meta_(ComPtr.__class__):
    pass
class Polyline(ComPtr, metaclass=_Polyline_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Shapes.Shape
    default_interface: win32more.Microsoft.UI.Xaml.Shapes.IPolyline
    _classid_ = 'Microsoft.UI.Xaml.Shapes.Polyline'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Shapes.Polyline.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Shapes.Polyline: ...
    @winrt_mixinmethod
    def get_FillRule(self: win32more.Microsoft.UI.Xaml.Shapes.IPolyline) -> win32more.Microsoft.UI.Xaml.Media.FillRule: ...
    @winrt_mixinmethod
    def put_FillRule(self: win32more.Microsoft.UI.Xaml.Shapes.IPolyline, value: win32more.Microsoft.UI.Xaml.Media.FillRule) -> Void: ...
    @winrt_mixinmethod
    def get_Points(self: win32more.Microsoft.UI.Xaml.Shapes.IPolyline) -> win32more.Microsoft.UI.Xaml.Media.PointCollection: ...
    @winrt_mixinmethod
    def put_Points(self: win32more.Microsoft.UI.Xaml.Shapes.IPolyline, value: win32more.Microsoft.UI.Xaml.Media.PointCollection) -> Void: ...
    @winrt_classmethod
    def get_FillRuleProperty(cls: win32more.Microsoft.UI.Xaml.Shapes.IPolylineStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PointsProperty(cls: win32more.Microsoft.UI.Xaml.Shapes.IPolylineStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    FillRule = property(get_FillRule, put_FillRule)
    Points = property(get_Points, put_Points)
    _Polyline_Meta_.FillRuleProperty = property(get_FillRuleProperty, None)
    _Polyline_Meta_.PointsProperty = property(get_PointsProperty, None)
class _Rectangle_Meta_(ComPtr.__class__):
    pass
class Rectangle(ComPtr, metaclass=_Rectangle_Meta_):
    extends: win32more.Microsoft.UI.Xaml.Shapes.Shape
    default_interface: win32more.Microsoft.UI.Xaml.Shapes.IRectangle
    _classid_ = 'Microsoft.UI.Xaml.Shapes.Rectangle'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Shapes.Rectangle.CreateInstance(*args))
        else:
            raise ValueError('no matched constructor')
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Microsoft.UI.Xaml.Shapes.Rectangle: ...
    @winrt_mixinmethod
    def get_RadiusX(self: win32more.Microsoft.UI.Xaml.Shapes.IRectangle) -> Double: ...
    @winrt_mixinmethod
    def put_RadiusX(self: win32more.Microsoft.UI.Xaml.Shapes.IRectangle, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RadiusY(self: win32more.Microsoft.UI.Xaml.Shapes.IRectangle) -> Double: ...
    @winrt_mixinmethod
    def put_RadiusY(self: win32more.Microsoft.UI.Xaml.Shapes.IRectangle, value: Double) -> Void: ...
    @winrt_classmethod
    def get_RadiusXProperty(cls: win32more.Microsoft.UI.Xaml.Shapes.IRectangleStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RadiusYProperty(cls: win32more.Microsoft.UI.Xaml.Shapes.IRectangleStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    RadiusX = property(get_RadiusX, put_RadiusX)
    RadiusY = property(get_RadiusY, put_RadiusY)
    _Rectangle_Meta_.RadiusXProperty = property(get_RadiusXProperty, None)
    _Rectangle_Meta_.RadiusYProperty = property(get_RadiusYProperty, None)
class _Shape_Meta_(ComPtr.__class__):
    pass
class Shape(ComPtr, metaclass=_Shape_Meta_):
    extends: win32more.Microsoft.UI.Xaml.FrameworkElement
    default_interface: win32more.Microsoft.UI.Xaml.Shapes.IShape
    _classid_ = 'Microsoft.UI.Xaml.Shapes.Shape'
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        elif len(args) == 0:
            super().__init__(move=win32more.Microsoft.UI.Xaml.Shapes.Shape.CreateInstance(*args, None, None))
        else:
            raise ValueError('no matched constructor')
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Microsoft.UI.Xaml.Shapes.IShapeFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Microsoft.UI.Xaml.Shapes.Shape: ...
    @winrt_mixinmethod
    def get_Fill(self: win32more.Microsoft.UI.Xaml.Shapes.IShape) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_Fill(self: win32more.Microsoft.UI.Xaml.Shapes.IShape, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_Stroke(self: win32more.Microsoft.UI.Xaml.Shapes.IShape) -> win32more.Microsoft.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_Stroke(self: win32more.Microsoft.UI.Xaml.Shapes.IShape, value: win32more.Microsoft.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeMiterLimit(self: win32more.Microsoft.UI.Xaml.Shapes.IShape) -> Double: ...
    @winrt_mixinmethod
    def put_StrokeMiterLimit(self: win32more.Microsoft.UI.Xaml.Shapes.IShape, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeThickness(self: win32more.Microsoft.UI.Xaml.Shapes.IShape) -> Double: ...
    @winrt_mixinmethod
    def put_StrokeThickness(self: win32more.Microsoft.UI.Xaml.Shapes.IShape, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeStartLineCap(self: win32more.Microsoft.UI.Xaml.Shapes.IShape) -> win32more.Microsoft.UI.Xaml.Media.PenLineCap: ...
    @winrt_mixinmethod
    def put_StrokeStartLineCap(self: win32more.Microsoft.UI.Xaml.Shapes.IShape, value: win32more.Microsoft.UI.Xaml.Media.PenLineCap) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeEndLineCap(self: win32more.Microsoft.UI.Xaml.Shapes.IShape) -> win32more.Microsoft.UI.Xaml.Media.PenLineCap: ...
    @winrt_mixinmethod
    def put_StrokeEndLineCap(self: win32more.Microsoft.UI.Xaml.Shapes.IShape, value: win32more.Microsoft.UI.Xaml.Media.PenLineCap) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeLineJoin(self: win32more.Microsoft.UI.Xaml.Shapes.IShape) -> win32more.Microsoft.UI.Xaml.Media.PenLineJoin: ...
    @winrt_mixinmethod
    def put_StrokeLineJoin(self: win32more.Microsoft.UI.Xaml.Shapes.IShape, value: win32more.Microsoft.UI.Xaml.Media.PenLineJoin) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeDashOffset(self: win32more.Microsoft.UI.Xaml.Shapes.IShape) -> Double: ...
    @winrt_mixinmethod
    def put_StrokeDashOffset(self: win32more.Microsoft.UI.Xaml.Shapes.IShape, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeDashCap(self: win32more.Microsoft.UI.Xaml.Shapes.IShape) -> win32more.Microsoft.UI.Xaml.Media.PenLineCap: ...
    @winrt_mixinmethod
    def put_StrokeDashCap(self: win32more.Microsoft.UI.Xaml.Shapes.IShape, value: win32more.Microsoft.UI.Xaml.Media.PenLineCap) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeDashArray(self: win32more.Microsoft.UI.Xaml.Shapes.IShape) -> win32more.Microsoft.UI.Xaml.Media.DoubleCollection: ...
    @winrt_mixinmethod
    def put_StrokeDashArray(self: win32more.Microsoft.UI.Xaml.Shapes.IShape, value: win32more.Microsoft.UI.Xaml.Media.DoubleCollection) -> Void: ...
    @winrt_mixinmethod
    def get_Stretch(self: win32more.Microsoft.UI.Xaml.Shapes.IShape) -> win32more.Microsoft.UI.Xaml.Media.Stretch: ...
    @winrt_mixinmethod
    def put_Stretch(self: win32more.Microsoft.UI.Xaml.Shapes.IShape, value: win32more.Microsoft.UI.Xaml.Media.Stretch) -> Void: ...
    @winrt_mixinmethod
    def get_GeometryTransform(self: win32more.Microsoft.UI.Xaml.Shapes.IShape) -> win32more.Microsoft.UI.Xaml.Media.Transform: ...
    @winrt_mixinmethod
    def GetAlphaMask(self: win32more.Microsoft.UI.Xaml.Shapes.IShape) -> win32more.Microsoft.UI.Composition.CompositionBrush: ...
    @winrt_classmethod
    def get_FillProperty(cls: win32more.Microsoft.UI.Xaml.Shapes.IShapeStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeProperty(cls: win32more.Microsoft.UI.Xaml.Shapes.IShapeStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeMiterLimitProperty(cls: win32more.Microsoft.UI.Xaml.Shapes.IShapeStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeThicknessProperty(cls: win32more.Microsoft.UI.Xaml.Shapes.IShapeStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeStartLineCapProperty(cls: win32more.Microsoft.UI.Xaml.Shapes.IShapeStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeEndLineCapProperty(cls: win32more.Microsoft.UI.Xaml.Shapes.IShapeStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeLineJoinProperty(cls: win32more.Microsoft.UI.Xaml.Shapes.IShapeStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeDashOffsetProperty(cls: win32more.Microsoft.UI.Xaml.Shapes.IShapeStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeDashCapProperty(cls: win32more.Microsoft.UI.Xaml.Shapes.IShapeStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeDashArrayProperty(cls: win32more.Microsoft.UI.Xaml.Shapes.IShapeStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StretchProperty(cls: win32more.Microsoft.UI.Xaml.Shapes.IShapeStatics) -> win32more.Microsoft.UI.Xaml.DependencyProperty: ...
    Fill = property(get_Fill, put_Fill)
    GeometryTransform = property(get_GeometryTransform, None)
    Stretch = property(get_Stretch, put_Stretch)
    Stroke = property(get_Stroke, put_Stroke)
    StrokeDashArray = property(get_StrokeDashArray, put_StrokeDashArray)
    StrokeDashCap = property(get_StrokeDashCap, put_StrokeDashCap)
    StrokeDashOffset = property(get_StrokeDashOffset, put_StrokeDashOffset)
    StrokeEndLineCap = property(get_StrokeEndLineCap, put_StrokeEndLineCap)
    StrokeLineJoin = property(get_StrokeLineJoin, put_StrokeLineJoin)
    StrokeMiterLimit = property(get_StrokeMiterLimit, put_StrokeMiterLimit)
    StrokeStartLineCap = property(get_StrokeStartLineCap, put_StrokeStartLineCap)
    StrokeThickness = property(get_StrokeThickness, put_StrokeThickness)
    _Shape_Meta_.FillProperty = property(get_FillProperty, None)
    _Shape_Meta_.StretchProperty = property(get_StretchProperty, None)
    _Shape_Meta_.StrokeDashArrayProperty = property(get_StrokeDashArrayProperty, None)
    _Shape_Meta_.StrokeDashCapProperty = property(get_StrokeDashCapProperty, None)
    _Shape_Meta_.StrokeDashOffsetProperty = property(get_StrokeDashOffsetProperty, None)
    _Shape_Meta_.StrokeEndLineCapProperty = property(get_StrokeEndLineCapProperty, None)
    _Shape_Meta_.StrokeLineJoinProperty = property(get_StrokeLineJoinProperty, None)
    _Shape_Meta_.StrokeMiterLimitProperty = property(get_StrokeMiterLimitProperty, None)
    _Shape_Meta_.StrokeProperty = property(get_StrokeProperty, None)
    _Shape_Meta_.StrokeStartLineCapProperty = property(get_StrokeStartLineCapProperty, None)
    _Shape_Meta_.StrokeThicknessProperty = property(get_StrokeThicknessProperty, None)


make_ready(__name__)
