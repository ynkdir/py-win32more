from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.UI.Composition
import win32more.Windows.UI.Xaml
import win32more.Windows.UI.Xaml.Media
import win32more.Windows.UI.Xaml.Shapes
class Ellipse(ComPtr):
    extends: win32more.Windows.UI.Xaml.Shapes.Shape
    default_interface: win32more.Windows.UI.Xaml.Shapes.IEllipse
    _classid_ = 'Windows.UI.Xaml.Shapes.Ellipse'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs.get('allocate', False):
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.UI.Xaml.Shapes.Ellipse.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Shapes.Ellipse: ...
class IEllipse(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Shapes.IEllipse'
    _iid_ = Guid('{70e05ac4-d38d-4bab-831f-4a22ef52ac86}')
class ILine(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Shapes.ILine'
    _iid_ = Guid('{46a5433d-4ffb-48df-8732-4e15c834816b}')
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
    Y1 = property(get_Y1, put_Y1)
    X2 = property(get_X2, put_X2)
    Y2 = property(get_Y2, put_Y2)
class ILineStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Shapes.ILineStatics'
    _iid_ = Guid('{267c123d-6ea4-4c50-8b1d-50207aff1e8a}')
    @winrt_commethod(6)
    def get_X1Property(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_Y1Property(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_X2Property(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_Y2Property(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    X1Property = property(get_X1Property, None)
    Y1Property = property(get_Y1Property, None)
    X2Property = property(get_X2Property, None)
    Y2Property = property(get_Y2Property, None)
class IPath(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Shapes.IPath'
    _iid_ = Guid('{78883609-3d57-4f3c-b8a5-6cabcac9711f}')
    @winrt_commethod(6)
    def get_Data(self) -> win32more.Windows.UI.Xaml.Media.Geometry: ...
    @winrt_commethod(7)
    def put_Data(self, value: win32more.Windows.UI.Xaml.Media.Geometry) -> Void: ...
    Data = property(get_Data, put_Data)
class IPathFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Shapes.IPathFactory'
    _iid_ = Guid('{2340a4e3-5a86-4fc6-9a50-cbb93b828766}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Shapes.Path: ...
class IPathStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Shapes.IPathStatics'
    _iid_ = Guid('{f627e59d-87dc-4142-81f1-97fc7ff8641c}')
    @winrt_commethod(6)
    def get_DataProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    DataProperty = property(get_DataProperty, None)
class IPolygon(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Shapes.IPolygon'
    _iid_ = Guid('{e3755c19-2e4d-4bcc-8d34-86871957fa01}')
    @winrt_commethod(6)
    def get_FillRule(self) -> win32more.Windows.UI.Xaml.Media.FillRule: ...
    @winrt_commethod(7)
    def put_FillRule(self, value: win32more.Windows.UI.Xaml.Media.FillRule) -> Void: ...
    @winrt_commethod(8)
    def get_Points(self) -> win32more.Windows.UI.Xaml.Media.PointCollection: ...
    @winrt_commethod(9)
    def put_Points(self, value: win32more.Windows.UI.Xaml.Media.PointCollection) -> Void: ...
    FillRule = property(get_FillRule, put_FillRule)
    Points = property(get_Points, put_Points)
class IPolygonStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Shapes.IPolygonStatics'
    _iid_ = Guid('{362a8aab-d463-4366-9e1a-beba72810fb7}')
    @winrt_commethod(6)
    def get_FillRuleProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_PointsProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    FillRuleProperty = property(get_FillRuleProperty, None)
    PointsProperty = property(get_PointsProperty, None)
class IPolyline(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Shapes.IPolyline'
    _iid_ = Guid('{91dc62f8-42b3-47f3-8476-c55124a7c4c6}')
    @winrt_commethod(6)
    def get_FillRule(self) -> win32more.Windows.UI.Xaml.Media.FillRule: ...
    @winrt_commethod(7)
    def put_FillRule(self, value: win32more.Windows.UI.Xaml.Media.FillRule) -> Void: ...
    @winrt_commethod(8)
    def get_Points(self) -> win32more.Windows.UI.Xaml.Media.PointCollection: ...
    @winrt_commethod(9)
    def put_Points(self, value: win32more.Windows.UI.Xaml.Media.PointCollection) -> Void: ...
    FillRule = property(get_FillRule, put_FillRule)
    Points = property(get_Points, put_Points)
class IPolylineStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Shapes.IPolylineStatics'
    _iid_ = Guid('{c7aa2cd1-a26c-43b0-aaa5-822fa64a11b9}')
    @winrt_commethod(6)
    def get_FillRuleProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_PointsProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    FillRuleProperty = property(get_FillRuleProperty, None)
    PointsProperty = property(get_PointsProperty, None)
class IRectangle(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Shapes.IRectangle'
    _iid_ = Guid('{855bc230-8a11-4e18-a136-4bc21c7827b0}')
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
    _classid_ = 'Windows.UI.Xaml.Shapes.IRectangleStatics'
    _iid_ = Guid('{9f25aa53-bb3a-4c3c-89db-6fbc0d1fa0cc}')
    @winrt_commethod(6)
    def get_RadiusXProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_RadiusYProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    RadiusXProperty = property(get_RadiusXProperty, None)
    RadiusYProperty = property(get_RadiusYProperty, None)
class IShape(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Shapes.IShape'
    _iid_ = Guid('{786f2b75-9aa0-454d-ae06-a2466e37c832}')
    @winrt_commethod(6)
    def get_Fill(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(7)
    def put_Fill(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(8)
    def get_Stroke(self) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(9)
    def put_Stroke(self, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(10)
    def get_StrokeMiterLimit(self) -> Double: ...
    @winrt_commethod(11)
    def put_StrokeMiterLimit(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def get_StrokeThickness(self) -> Double: ...
    @winrt_commethod(13)
    def put_StrokeThickness(self, value: Double) -> Void: ...
    @winrt_commethod(14)
    def get_StrokeStartLineCap(self) -> win32more.Windows.UI.Xaml.Media.PenLineCap: ...
    @winrt_commethod(15)
    def put_StrokeStartLineCap(self, value: win32more.Windows.UI.Xaml.Media.PenLineCap) -> Void: ...
    @winrt_commethod(16)
    def get_StrokeEndLineCap(self) -> win32more.Windows.UI.Xaml.Media.PenLineCap: ...
    @winrt_commethod(17)
    def put_StrokeEndLineCap(self, value: win32more.Windows.UI.Xaml.Media.PenLineCap) -> Void: ...
    @winrt_commethod(18)
    def get_StrokeLineJoin(self) -> win32more.Windows.UI.Xaml.Media.PenLineJoin: ...
    @winrt_commethod(19)
    def put_StrokeLineJoin(self, value: win32more.Windows.UI.Xaml.Media.PenLineJoin) -> Void: ...
    @winrt_commethod(20)
    def get_StrokeDashOffset(self) -> Double: ...
    @winrt_commethod(21)
    def put_StrokeDashOffset(self, value: Double) -> Void: ...
    @winrt_commethod(22)
    def get_StrokeDashCap(self) -> win32more.Windows.UI.Xaml.Media.PenLineCap: ...
    @winrt_commethod(23)
    def put_StrokeDashCap(self, value: win32more.Windows.UI.Xaml.Media.PenLineCap) -> Void: ...
    @winrt_commethod(24)
    def get_StrokeDashArray(self) -> win32more.Windows.UI.Xaml.Media.DoubleCollection: ...
    @winrt_commethod(25)
    def put_StrokeDashArray(self, value: win32more.Windows.UI.Xaml.Media.DoubleCollection) -> Void: ...
    @winrt_commethod(26)
    def get_Stretch(self) -> win32more.Windows.UI.Xaml.Media.Stretch: ...
    @winrt_commethod(27)
    def put_Stretch(self, value: win32more.Windows.UI.Xaml.Media.Stretch) -> Void: ...
    @winrt_commethod(28)
    def get_GeometryTransform(self) -> win32more.Windows.UI.Xaml.Media.Transform: ...
    Fill = property(get_Fill, put_Fill)
    Stroke = property(get_Stroke, put_Stroke)
    StrokeMiterLimit = property(get_StrokeMiterLimit, put_StrokeMiterLimit)
    StrokeThickness = property(get_StrokeThickness, put_StrokeThickness)
    StrokeStartLineCap = property(get_StrokeStartLineCap, put_StrokeStartLineCap)
    StrokeEndLineCap = property(get_StrokeEndLineCap, put_StrokeEndLineCap)
    StrokeLineJoin = property(get_StrokeLineJoin, put_StrokeLineJoin)
    StrokeDashOffset = property(get_StrokeDashOffset, put_StrokeDashOffset)
    StrokeDashCap = property(get_StrokeDashCap, put_StrokeDashCap)
    StrokeDashArray = property(get_StrokeDashArray, put_StrokeDashArray)
    Stretch = property(get_Stretch, put_Stretch)
    GeometryTransform = property(get_GeometryTransform, None)
class IShape2(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Shapes.IShape2'
    _iid_ = Guid('{97248dba-49f2-49a4-a5dd-164df824db14}')
    @winrt_commethod(6)
    def GetAlphaMask(self) -> win32more.Windows.UI.Composition.CompositionBrush: ...
class IShapeFactory(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Shapes.IShapeFactory'
    _iid_ = Guid('{4b717613-f6aa-48d5-9588-e1d188eacbc9}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Shapes.Shape: ...
class IShapeStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Shapes.IShapeStatics'
    _iid_ = Guid('{1d7b4c55-9df3-48dc-9194-9d306faa6089}')
    @winrt_commethod(6)
    def get_FillProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_StrokeProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_StrokeMiterLimitProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_StrokeThicknessProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_StrokeStartLineCapProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_StrokeEndLineCapProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_StrokeLineJoinProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_StrokeDashOffsetProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_StrokeDashCapProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_StrokeDashArrayProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def get_StretchProperty(self) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    FillProperty = property(get_FillProperty, None)
    StrokeProperty = property(get_StrokeProperty, None)
    StrokeMiterLimitProperty = property(get_StrokeMiterLimitProperty, None)
    StrokeThicknessProperty = property(get_StrokeThicknessProperty, None)
    StrokeStartLineCapProperty = property(get_StrokeStartLineCapProperty, None)
    StrokeEndLineCapProperty = property(get_StrokeEndLineCapProperty, None)
    StrokeLineJoinProperty = property(get_StrokeLineJoinProperty, None)
    StrokeDashOffsetProperty = property(get_StrokeDashOffsetProperty, None)
    StrokeDashCapProperty = property(get_StrokeDashCapProperty, None)
    StrokeDashArrayProperty = property(get_StrokeDashArrayProperty, None)
    StretchProperty = property(get_StretchProperty, None)
class _Line_Meta_(ComPtr.__class__):
    pass
class Line(ComPtr, metaclass=_Line_Meta_):
    extends: win32more.Windows.UI.Xaml.Shapes.Shape
    default_interface: win32more.Windows.UI.Xaml.Shapes.ILine
    _classid_ = 'Windows.UI.Xaml.Shapes.Line'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs.get('allocate', False):
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.UI.Xaml.Shapes.Line.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Shapes.Line: ...
    @winrt_mixinmethod
    def get_X1(self: win32more.Windows.UI.Xaml.Shapes.ILine) -> Double: ...
    @winrt_mixinmethod
    def put_X1(self: win32more.Windows.UI.Xaml.Shapes.ILine, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Y1(self: win32more.Windows.UI.Xaml.Shapes.ILine) -> Double: ...
    @winrt_mixinmethod
    def put_Y1(self: win32more.Windows.UI.Xaml.Shapes.ILine, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_X2(self: win32more.Windows.UI.Xaml.Shapes.ILine) -> Double: ...
    @winrt_mixinmethod
    def put_X2(self: win32more.Windows.UI.Xaml.Shapes.ILine, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Y2(self: win32more.Windows.UI.Xaml.Shapes.ILine) -> Double: ...
    @winrt_mixinmethod
    def put_Y2(self: win32more.Windows.UI.Xaml.Shapes.ILine, value: Double) -> Void: ...
    @winrt_classmethod
    def get_X1Property(cls: win32more.Windows.UI.Xaml.Shapes.ILineStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_Y1Property(cls: win32more.Windows.UI.Xaml.Shapes.ILineStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_X2Property(cls: win32more.Windows.UI.Xaml.Shapes.ILineStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_Y2Property(cls: win32more.Windows.UI.Xaml.Shapes.ILineStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    X1 = property(get_X1, put_X1)
    Y1 = property(get_Y1, put_Y1)
    X2 = property(get_X2, put_X2)
    Y2 = property(get_Y2, put_Y2)
    _Line_Meta_.X1Property = property(get_X1Property.__wrapped__, None)
    _Line_Meta_.Y1Property = property(get_Y1Property.__wrapped__, None)
    _Line_Meta_.X2Property = property(get_X2Property.__wrapped__, None)
    _Line_Meta_.Y2Property = property(get_Y2Property.__wrapped__, None)
class _Path_Meta_(ComPtr.__class__):
    pass
class Path(ComPtr, metaclass=_Path_Meta_):
    extends: win32more.Windows.UI.Xaml.Shapes.Shape
    default_interface: win32more.Windows.UI.Xaml.Shapes.IPath
    _classid_ = 'Windows.UI.Xaml.Shapes.Path'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs.get('allocate', False):
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.UI.Xaml.Shapes.Path.CreateInstance(*args, None, None)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Shapes.IPathFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Shapes.Path: ...
    @winrt_mixinmethod
    def get_Data(self: win32more.Windows.UI.Xaml.Shapes.IPath) -> win32more.Windows.UI.Xaml.Media.Geometry: ...
    @winrt_mixinmethod
    def put_Data(self: win32more.Windows.UI.Xaml.Shapes.IPath, value: win32more.Windows.UI.Xaml.Media.Geometry) -> Void: ...
    @winrt_classmethod
    def get_DataProperty(cls: win32more.Windows.UI.Xaml.Shapes.IPathStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Data = property(get_Data, put_Data)
    _Path_Meta_.DataProperty = property(get_DataProperty.__wrapped__, None)
class _Polygon_Meta_(ComPtr.__class__):
    pass
class Polygon(ComPtr, metaclass=_Polygon_Meta_):
    extends: win32more.Windows.UI.Xaml.Shapes.Shape
    default_interface: win32more.Windows.UI.Xaml.Shapes.IPolygon
    _classid_ = 'Windows.UI.Xaml.Shapes.Polygon'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs.get('allocate', False):
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.UI.Xaml.Shapes.Polygon.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Shapes.Polygon: ...
    @winrt_mixinmethod
    def get_FillRule(self: win32more.Windows.UI.Xaml.Shapes.IPolygon) -> win32more.Windows.UI.Xaml.Media.FillRule: ...
    @winrt_mixinmethod
    def put_FillRule(self: win32more.Windows.UI.Xaml.Shapes.IPolygon, value: win32more.Windows.UI.Xaml.Media.FillRule) -> Void: ...
    @winrt_mixinmethod
    def get_Points(self: win32more.Windows.UI.Xaml.Shapes.IPolygon) -> win32more.Windows.UI.Xaml.Media.PointCollection: ...
    @winrt_mixinmethod
    def put_Points(self: win32more.Windows.UI.Xaml.Shapes.IPolygon, value: win32more.Windows.UI.Xaml.Media.PointCollection) -> Void: ...
    @winrt_classmethod
    def get_FillRuleProperty(cls: win32more.Windows.UI.Xaml.Shapes.IPolygonStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PointsProperty(cls: win32more.Windows.UI.Xaml.Shapes.IPolygonStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    FillRule = property(get_FillRule, put_FillRule)
    Points = property(get_Points, put_Points)
    _Polygon_Meta_.FillRuleProperty = property(get_FillRuleProperty.__wrapped__, None)
    _Polygon_Meta_.PointsProperty = property(get_PointsProperty.__wrapped__, None)
class _Polyline_Meta_(ComPtr.__class__):
    pass
class Polyline(ComPtr, metaclass=_Polyline_Meta_):
    extends: win32more.Windows.UI.Xaml.Shapes.Shape
    default_interface: win32more.Windows.UI.Xaml.Shapes.IPolyline
    _classid_ = 'Windows.UI.Xaml.Shapes.Polyline'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs.get('allocate', False):
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.UI.Xaml.Shapes.Polyline.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Shapes.Polyline: ...
    @winrt_mixinmethod
    def get_FillRule(self: win32more.Windows.UI.Xaml.Shapes.IPolyline) -> win32more.Windows.UI.Xaml.Media.FillRule: ...
    @winrt_mixinmethod
    def put_FillRule(self: win32more.Windows.UI.Xaml.Shapes.IPolyline, value: win32more.Windows.UI.Xaml.Media.FillRule) -> Void: ...
    @winrt_mixinmethod
    def get_Points(self: win32more.Windows.UI.Xaml.Shapes.IPolyline) -> win32more.Windows.UI.Xaml.Media.PointCollection: ...
    @winrt_mixinmethod
    def put_Points(self: win32more.Windows.UI.Xaml.Shapes.IPolyline, value: win32more.Windows.UI.Xaml.Media.PointCollection) -> Void: ...
    @winrt_classmethod
    def get_FillRuleProperty(cls: win32more.Windows.UI.Xaml.Shapes.IPolylineStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PointsProperty(cls: win32more.Windows.UI.Xaml.Shapes.IPolylineStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    FillRule = property(get_FillRule, put_FillRule)
    Points = property(get_Points, put_Points)
    _Polyline_Meta_.FillRuleProperty = property(get_FillRuleProperty.__wrapped__, None)
    _Polyline_Meta_.PointsProperty = property(get_PointsProperty.__wrapped__, None)
class _Rectangle_Meta_(ComPtr.__class__):
    pass
class Rectangle(ComPtr, metaclass=_Rectangle_Meta_):
    extends: win32more.Windows.UI.Xaml.Shapes.Shape
    default_interface: win32more.Windows.UI.Xaml.Shapes.IRectangle
    _classid_ = 'Windows.UI.Xaml.Shapes.Rectangle'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs.get('allocate', False):
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.UI.Xaml.Shapes.Rectangle.CreateInstance(*args)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_activatemethod
    def CreateInstance(cls) -> win32more.Windows.UI.Xaml.Shapes.Rectangle: ...
    @winrt_mixinmethod
    def get_RadiusX(self: win32more.Windows.UI.Xaml.Shapes.IRectangle) -> Double: ...
    @winrt_mixinmethod
    def put_RadiusX(self: win32more.Windows.UI.Xaml.Shapes.IRectangle, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RadiusY(self: win32more.Windows.UI.Xaml.Shapes.IRectangle) -> Double: ...
    @winrt_mixinmethod
    def put_RadiusY(self: win32more.Windows.UI.Xaml.Shapes.IRectangle, value: Double) -> Void: ...
    @winrt_classmethod
    def get_RadiusXProperty(cls: win32more.Windows.UI.Xaml.Shapes.IRectangleStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RadiusYProperty(cls: win32more.Windows.UI.Xaml.Shapes.IRectangleStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    RadiusX = property(get_RadiusX, put_RadiusX)
    RadiusY = property(get_RadiusY, put_RadiusY)
    _Rectangle_Meta_.RadiusXProperty = property(get_RadiusXProperty.__wrapped__, None)
    _Rectangle_Meta_.RadiusYProperty = property(get_RadiusYProperty.__wrapped__, None)
class _Shape_Meta_(ComPtr.__class__):
    pass
class Shape(ComPtr, metaclass=_Shape_Meta_):
    extends: win32more.Windows.UI.Xaml.FrameworkElement
    default_interface: win32more.Windows.UI.Xaml.Shapes.IShape
    _classid_ = 'Windows.UI.Xaml.Shapes.Shape'
    def __init__(self, *args, **kwargs) -> None:
        if kwargs.get('allocate', False):
            return super().__init__(**kwargs)
        elif len(args) == 0:
            instance = win32more.Windows.UI.Xaml.Shapes.Shape.CreateInstance(*args, None, None)
        else:
            raise ValueError('no matched constructor')
        self.value = instance.value
        self._own = instance._own
        instance._own = False
    @winrt_factorymethod
    def CreateInstance(cls: win32more.Windows.UI.Xaml.Shapes.IShapeFactory, baseInterface: win32more.Windows.Win32.System.WinRT.IInspectable, innerInterface: POINTER(win32more.Windows.Win32.System.WinRT.IInspectable)) -> win32more.Windows.UI.Xaml.Shapes.Shape: ...
    @winrt_mixinmethod
    def get_Fill(self: win32more.Windows.UI.Xaml.Shapes.IShape) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_Fill(self: win32more.Windows.UI.Xaml.Shapes.IShape, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_Stroke(self: win32more.Windows.UI.Xaml.Shapes.IShape) -> win32more.Windows.UI.Xaml.Media.Brush: ...
    @winrt_mixinmethod
    def put_Stroke(self: win32more.Windows.UI.Xaml.Shapes.IShape, value: win32more.Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeMiterLimit(self: win32more.Windows.UI.Xaml.Shapes.IShape) -> Double: ...
    @winrt_mixinmethod
    def put_StrokeMiterLimit(self: win32more.Windows.UI.Xaml.Shapes.IShape, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeThickness(self: win32more.Windows.UI.Xaml.Shapes.IShape) -> Double: ...
    @winrt_mixinmethod
    def put_StrokeThickness(self: win32more.Windows.UI.Xaml.Shapes.IShape, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeStartLineCap(self: win32more.Windows.UI.Xaml.Shapes.IShape) -> win32more.Windows.UI.Xaml.Media.PenLineCap: ...
    @winrt_mixinmethod
    def put_StrokeStartLineCap(self: win32more.Windows.UI.Xaml.Shapes.IShape, value: win32more.Windows.UI.Xaml.Media.PenLineCap) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeEndLineCap(self: win32more.Windows.UI.Xaml.Shapes.IShape) -> win32more.Windows.UI.Xaml.Media.PenLineCap: ...
    @winrt_mixinmethod
    def put_StrokeEndLineCap(self: win32more.Windows.UI.Xaml.Shapes.IShape, value: win32more.Windows.UI.Xaml.Media.PenLineCap) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeLineJoin(self: win32more.Windows.UI.Xaml.Shapes.IShape) -> win32more.Windows.UI.Xaml.Media.PenLineJoin: ...
    @winrt_mixinmethod
    def put_StrokeLineJoin(self: win32more.Windows.UI.Xaml.Shapes.IShape, value: win32more.Windows.UI.Xaml.Media.PenLineJoin) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeDashOffset(self: win32more.Windows.UI.Xaml.Shapes.IShape) -> Double: ...
    @winrt_mixinmethod
    def put_StrokeDashOffset(self: win32more.Windows.UI.Xaml.Shapes.IShape, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeDashCap(self: win32more.Windows.UI.Xaml.Shapes.IShape) -> win32more.Windows.UI.Xaml.Media.PenLineCap: ...
    @winrt_mixinmethod
    def put_StrokeDashCap(self: win32more.Windows.UI.Xaml.Shapes.IShape, value: win32more.Windows.UI.Xaml.Media.PenLineCap) -> Void: ...
    @winrt_mixinmethod
    def get_StrokeDashArray(self: win32more.Windows.UI.Xaml.Shapes.IShape) -> win32more.Windows.UI.Xaml.Media.DoubleCollection: ...
    @winrt_mixinmethod
    def put_StrokeDashArray(self: win32more.Windows.UI.Xaml.Shapes.IShape, value: win32more.Windows.UI.Xaml.Media.DoubleCollection) -> Void: ...
    @winrt_mixinmethod
    def get_Stretch(self: win32more.Windows.UI.Xaml.Shapes.IShape) -> win32more.Windows.UI.Xaml.Media.Stretch: ...
    @winrt_mixinmethod
    def put_Stretch(self: win32more.Windows.UI.Xaml.Shapes.IShape, value: win32more.Windows.UI.Xaml.Media.Stretch) -> Void: ...
    @winrt_mixinmethod
    def get_GeometryTransform(self: win32more.Windows.UI.Xaml.Shapes.IShape) -> win32more.Windows.UI.Xaml.Media.Transform: ...
    @winrt_mixinmethod
    def GetAlphaMask(self: win32more.Windows.UI.Xaml.Shapes.IShape2) -> win32more.Windows.UI.Composition.CompositionBrush: ...
    @winrt_classmethod
    def get_FillProperty(cls: win32more.Windows.UI.Xaml.Shapes.IShapeStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeProperty(cls: win32more.Windows.UI.Xaml.Shapes.IShapeStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeMiterLimitProperty(cls: win32more.Windows.UI.Xaml.Shapes.IShapeStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeThicknessProperty(cls: win32more.Windows.UI.Xaml.Shapes.IShapeStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeStartLineCapProperty(cls: win32more.Windows.UI.Xaml.Shapes.IShapeStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeEndLineCapProperty(cls: win32more.Windows.UI.Xaml.Shapes.IShapeStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeLineJoinProperty(cls: win32more.Windows.UI.Xaml.Shapes.IShapeStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeDashOffsetProperty(cls: win32more.Windows.UI.Xaml.Shapes.IShapeStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeDashCapProperty(cls: win32more.Windows.UI.Xaml.Shapes.IShapeStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeDashArrayProperty(cls: win32more.Windows.UI.Xaml.Shapes.IShapeStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StretchProperty(cls: win32more.Windows.UI.Xaml.Shapes.IShapeStatics) -> win32more.Windows.UI.Xaml.DependencyProperty: ...
    Fill = property(get_Fill, put_Fill)
    Stroke = property(get_Stroke, put_Stroke)
    StrokeMiterLimit = property(get_StrokeMiterLimit, put_StrokeMiterLimit)
    StrokeThickness = property(get_StrokeThickness, put_StrokeThickness)
    StrokeStartLineCap = property(get_StrokeStartLineCap, put_StrokeStartLineCap)
    StrokeEndLineCap = property(get_StrokeEndLineCap, put_StrokeEndLineCap)
    StrokeLineJoin = property(get_StrokeLineJoin, put_StrokeLineJoin)
    StrokeDashOffset = property(get_StrokeDashOffset, put_StrokeDashOffset)
    StrokeDashCap = property(get_StrokeDashCap, put_StrokeDashCap)
    StrokeDashArray = property(get_StrokeDashArray, put_StrokeDashArray)
    Stretch = property(get_Stretch, put_Stretch)
    GeometryTransform = property(get_GeometryTransform, None)
    _Shape_Meta_.FillProperty = property(get_FillProperty.__wrapped__, None)
    _Shape_Meta_.StrokeProperty = property(get_StrokeProperty.__wrapped__, None)
    _Shape_Meta_.StrokeMiterLimitProperty = property(get_StrokeMiterLimitProperty.__wrapped__, None)
    _Shape_Meta_.StrokeThicknessProperty = property(get_StrokeThicknessProperty.__wrapped__, None)
    _Shape_Meta_.StrokeStartLineCapProperty = property(get_StrokeStartLineCapProperty.__wrapped__, None)
    _Shape_Meta_.StrokeEndLineCapProperty = property(get_StrokeEndLineCapProperty.__wrapped__, None)
    _Shape_Meta_.StrokeLineJoinProperty = property(get_StrokeLineJoinProperty.__wrapped__, None)
    _Shape_Meta_.StrokeDashOffsetProperty = property(get_StrokeDashOffsetProperty.__wrapped__, None)
    _Shape_Meta_.StrokeDashCapProperty = property(get_StrokeDashCapProperty.__wrapped__, None)
    _Shape_Meta_.StrokeDashArrayProperty = property(get_StrokeDashArrayProperty.__wrapped__, None)
    _Shape_Meta_.StretchProperty = property(get_StretchProperty.__wrapped__, None)
make_ready(__name__)
