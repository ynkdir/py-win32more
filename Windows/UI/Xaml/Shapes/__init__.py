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
import Windows.UI.Composition
import Windows.UI.Xaml
import Windows.UI.Xaml.Media
import Windows.UI.Xaml.Shapes
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class Ellipse(ComPtr):
    extends: Windows.UI.Xaml.Shapes.Shape
    default_interface: Windows.UI.Xaml.Shapes.IEllipse
    _classid_ = 'Windows.UI.Xaml.Shapes.Ellipse'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Shapes.Ellipse: ...
class IEllipse(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Shapes.IEllipse'
    _iid_ = Guid('{70e05ac4-d38d-4bab-831f-4a22ef52ac86}')
class ILine(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Shapes.ILineStatics'
    _iid_ = Guid('{267c123d-6ea4-4c50-8b1d-50207aff1e8a}')
    @winrt_commethod(6)
    def get_X1Property(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_Y1Property(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_X2Property(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_Y2Property(self) -> Windows.UI.Xaml.DependencyProperty: ...
    X1Property = property(get_X1Property, None)
    Y1Property = property(get_Y1Property, None)
    X2Property = property(get_X2Property, None)
    Y2Property = property(get_Y2Property, None)
class IPath(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Shapes.IPath'
    _iid_ = Guid('{78883609-3d57-4f3c-b8a5-6cabcac9711f}')
    @winrt_commethod(6)
    def get_Data(self) -> Windows.UI.Xaml.Media.Geometry: ...
    @winrt_commethod(7)
    def put_Data(self, value: Windows.UI.Xaml.Media.Geometry) -> Void: ...
    Data = property(get_Data, put_Data)
class IPathFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Shapes.IPathFactory'
    _iid_ = Guid('{2340a4e3-5a86-4fc6-9a50-cbb93b828766}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Shapes.Path: ...
class IPathStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Shapes.IPathStatics'
    _iid_ = Guid('{f627e59d-87dc-4142-81f1-97fc7ff8641c}')
    @winrt_commethod(6)
    def get_DataProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    DataProperty = property(get_DataProperty, None)
class IPolygon(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Shapes.IPolygon'
    _iid_ = Guid('{e3755c19-2e4d-4bcc-8d34-86871957fa01}')
    @winrt_commethod(6)
    def get_FillRule(self) -> Windows.UI.Xaml.Media.FillRule: ...
    @winrt_commethod(7)
    def put_FillRule(self, value: Windows.UI.Xaml.Media.FillRule) -> Void: ...
    @winrt_commethod(8)
    def get_Points(self) -> Windows.UI.Xaml.Media.PointCollection: ...
    @winrt_commethod(9)
    def put_Points(self, value: Windows.UI.Xaml.Media.PointCollection) -> Void: ...
    FillRule = property(get_FillRule, put_FillRule)
    Points = property(get_Points, put_Points)
class IPolygonStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Shapes.IPolygonStatics'
    _iid_ = Guid('{362a8aab-d463-4366-9e1a-beba72810fb7}')
    @winrt_commethod(6)
    def get_FillRuleProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_PointsProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    FillRuleProperty = property(get_FillRuleProperty, None)
    PointsProperty = property(get_PointsProperty, None)
class IPolyline(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Shapes.IPolyline'
    _iid_ = Guid('{91dc62f8-42b3-47f3-8476-c55124a7c4c6}')
    @winrt_commethod(6)
    def get_FillRule(self) -> Windows.UI.Xaml.Media.FillRule: ...
    @winrt_commethod(7)
    def put_FillRule(self, value: Windows.UI.Xaml.Media.FillRule) -> Void: ...
    @winrt_commethod(8)
    def get_Points(self) -> Windows.UI.Xaml.Media.PointCollection: ...
    @winrt_commethod(9)
    def put_Points(self, value: Windows.UI.Xaml.Media.PointCollection) -> Void: ...
    FillRule = property(get_FillRule, put_FillRule)
    Points = property(get_Points, put_Points)
class IPolylineStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Shapes.IPolylineStatics'
    _iid_ = Guid('{c7aa2cd1-a26c-43b0-aaa5-822fa64a11b9}')
    @winrt_commethod(6)
    def get_FillRuleProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_PointsProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    FillRuleProperty = property(get_FillRuleProperty, None)
    PointsProperty = property(get_PointsProperty, None)
class IRectangle(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Shapes.IRectangleStatics'
    _iid_ = Guid('{9f25aa53-bb3a-4c3c-89db-6fbc0d1fa0cc}')
    @winrt_commethod(6)
    def get_RadiusXProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_RadiusYProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    RadiusXProperty = property(get_RadiusXProperty, None)
    RadiusYProperty = property(get_RadiusYProperty, None)
class IShape(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Shapes.IShape'
    _iid_ = Guid('{786f2b75-9aa0-454d-ae06-a2466e37c832}')
    @winrt_commethod(6)
    def get_Fill(self) -> Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(7)
    def put_Fill(self, value: Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(8)
    def get_Stroke(self) -> Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(9)
    def put_Stroke(self, value: Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(10)
    def get_StrokeMiterLimit(self) -> Double: ...
    @winrt_commethod(11)
    def put_StrokeMiterLimit(self, value: Double) -> Void: ...
    @winrt_commethod(12)
    def get_StrokeThickness(self) -> Double: ...
    @winrt_commethod(13)
    def put_StrokeThickness(self, value: Double) -> Void: ...
    @winrt_commethod(14)
    def get_StrokeStartLineCap(self) -> Windows.UI.Xaml.Media.PenLineCap: ...
    @winrt_commethod(15)
    def put_StrokeStartLineCap(self, value: Windows.UI.Xaml.Media.PenLineCap) -> Void: ...
    @winrt_commethod(16)
    def get_StrokeEndLineCap(self) -> Windows.UI.Xaml.Media.PenLineCap: ...
    @winrt_commethod(17)
    def put_StrokeEndLineCap(self, value: Windows.UI.Xaml.Media.PenLineCap) -> Void: ...
    @winrt_commethod(18)
    def get_StrokeLineJoin(self) -> Windows.UI.Xaml.Media.PenLineJoin: ...
    @winrt_commethod(19)
    def put_StrokeLineJoin(self, value: Windows.UI.Xaml.Media.PenLineJoin) -> Void: ...
    @winrt_commethod(20)
    def get_StrokeDashOffset(self) -> Double: ...
    @winrt_commethod(21)
    def put_StrokeDashOffset(self, value: Double) -> Void: ...
    @winrt_commethod(22)
    def get_StrokeDashCap(self) -> Windows.UI.Xaml.Media.PenLineCap: ...
    @winrt_commethod(23)
    def put_StrokeDashCap(self, value: Windows.UI.Xaml.Media.PenLineCap) -> Void: ...
    @winrt_commethod(24)
    def get_StrokeDashArray(self) -> Windows.UI.Xaml.Media.DoubleCollection: ...
    @winrt_commethod(25)
    def put_StrokeDashArray(self, value: Windows.UI.Xaml.Media.DoubleCollection) -> Void: ...
    @winrt_commethod(26)
    def get_Stretch(self) -> Windows.UI.Xaml.Media.Stretch: ...
    @winrt_commethod(27)
    def put_Stretch(self, value: Windows.UI.Xaml.Media.Stretch) -> Void: ...
    @winrt_commethod(28)
    def get_GeometryTransform(self) -> Windows.UI.Xaml.Media.Transform: ...
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
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Shapes.IShape2'
    _iid_ = Guid('{97248dba-49f2-49a4-a5dd-164df824db14}')
    @winrt_commethod(6)
    def GetAlphaMask(self) -> Windows.UI.Composition.CompositionBrush: ...
class IShapeFactory(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Shapes.IShapeFactory'
    _iid_ = Guid('{4b717613-f6aa-48d5-9588-e1d188eacbc9}')
    @winrt_commethod(6)
    def CreateInstance(self, baseInterface: Windows.Win32.System.WinRT.IInspectable_head, innerInterface: POINTER(Windows.Win32.System.WinRT.IInspectable_head)) -> Windows.UI.Xaml.Shapes.Shape: ...
class IShapeStatics(ComPtr):
    extends: Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.UI.Xaml.Shapes.IShapeStatics'
    _iid_ = Guid('{1d7b4c55-9df3-48dc-9194-9d306faa6089}')
    @winrt_commethod(6)
    def get_FillProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(7)
    def get_StrokeProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(8)
    def get_StrokeMiterLimitProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(9)
    def get_StrokeThicknessProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(10)
    def get_StrokeStartLineCapProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(11)
    def get_StrokeEndLineCapProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(12)
    def get_StrokeLineJoinProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(13)
    def get_StrokeDashOffsetProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(14)
    def get_StrokeDashCapProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(15)
    def get_StrokeDashArrayProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_commethod(16)
    def get_StretchProperty(self) -> Windows.UI.Xaml.DependencyProperty: ...
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
class Line(ComPtr):
    extends: Windows.UI.Xaml.Shapes.Shape
    default_interface: Windows.UI.Xaml.Shapes.ILine
    _classid_ = 'Windows.UI.Xaml.Shapes.Line'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Shapes.Line: ...
    @winrt_mixinmethod
    def get_X1(self: Windows.UI.Xaml.Shapes.ILine) -> Double: ...
    @winrt_mixinmethod
    def put_X1(self: Windows.UI.Xaml.Shapes.ILine, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Y1(self: Windows.UI.Xaml.Shapes.ILine) -> Double: ...
    @winrt_mixinmethod
    def put_Y1(self: Windows.UI.Xaml.Shapes.ILine, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_X2(self: Windows.UI.Xaml.Shapes.ILine) -> Double: ...
    @winrt_mixinmethod
    def put_X2(self: Windows.UI.Xaml.Shapes.ILine, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_Y2(self: Windows.UI.Xaml.Shapes.ILine) -> Double: ...
    @winrt_mixinmethod
    def put_Y2(self: Windows.UI.Xaml.Shapes.ILine, value: Double) -> Void: ...
    @winrt_classmethod
    def get_X1Property(cls: Windows.UI.Xaml.Shapes.ILineStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_Y1Property(cls: Windows.UI.Xaml.Shapes.ILineStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_X2Property(cls: Windows.UI.Xaml.Shapes.ILineStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_Y2Property(cls: Windows.UI.Xaml.Shapes.ILineStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    X1 = property(get_X1, put_X1)
    Y1 = property(get_Y1, put_Y1)
    X2 = property(get_X2, put_X2)
    Y2 = property(get_Y2, put_Y2)
    X1Property = property(get_X1Property, None)
    Y1Property = property(get_Y1Property, None)
    X2Property = property(get_X2Property, None)
    Y2Property = property(get_Y2Property, None)
class Path(ComPtr):
    extends: Windows.UI.Xaml.Shapes.Shape
    default_interface: Windows.UI.Xaml.Shapes.IPath
    _classid_ = 'Windows.UI.Xaml.Shapes.Path'
    @winrt_commethod(442)
    def get_Data(self) -> Windows.UI.Xaml.Media.Geometry: ...
    @winrt_commethod(443)
    def put_Data(self, value: Windows.UI.Xaml.Media.Geometry) -> Void: ...
    @winrt_classmethod
    def get_DataProperty(cls: Windows.UI.Xaml.Shapes.IPathStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    Data = property(get_Data, put_Data)
    DataProperty = property(get_DataProperty, None)
class Polygon(ComPtr):
    extends: Windows.UI.Xaml.Shapes.Shape
    default_interface: Windows.UI.Xaml.Shapes.IPolygon
    _classid_ = 'Windows.UI.Xaml.Shapes.Polygon'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Shapes.Polygon: ...
    @winrt_mixinmethod
    def get_FillRule(self: Windows.UI.Xaml.Shapes.IPolygon) -> Windows.UI.Xaml.Media.FillRule: ...
    @winrt_mixinmethod
    def put_FillRule(self: Windows.UI.Xaml.Shapes.IPolygon, value: Windows.UI.Xaml.Media.FillRule) -> Void: ...
    @winrt_mixinmethod
    def get_Points(self: Windows.UI.Xaml.Shapes.IPolygon) -> Windows.UI.Xaml.Media.PointCollection: ...
    @winrt_mixinmethod
    def put_Points(self: Windows.UI.Xaml.Shapes.IPolygon, value: Windows.UI.Xaml.Media.PointCollection) -> Void: ...
    @winrt_classmethod
    def get_FillRuleProperty(cls: Windows.UI.Xaml.Shapes.IPolygonStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PointsProperty(cls: Windows.UI.Xaml.Shapes.IPolygonStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    FillRule = property(get_FillRule, put_FillRule)
    Points = property(get_Points, put_Points)
    FillRuleProperty = property(get_FillRuleProperty, None)
    PointsProperty = property(get_PointsProperty, None)
class Polyline(ComPtr):
    extends: Windows.UI.Xaml.Shapes.Shape
    default_interface: Windows.UI.Xaml.Shapes.IPolyline
    _classid_ = 'Windows.UI.Xaml.Shapes.Polyline'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Shapes.Polyline: ...
    @winrt_mixinmethod
    def get_FillRule(self: Windows.UI.Xaml.Shapes.IPolyline) -> Windows.UI.Xaml.Media.FillRule: ...
    @winrt_mixinmethod
    def put_FillRule(self: Windows.UI.Xaml.Shapes.IPolyline, value: Windows.UI.Xaml.Media.FillRule) -> Void: ...
    @winrt_mixinmethod
    def get_Points(self: Windows.UI.Xaml.Shapes.IPolyline) -> Windows.UI.Xaml.Media.PointCollection: ...
    @winrt_mixinmethod
    def put_Points(self: Windows.UI.Xaml.Shapes.IPolyline, value: Windows.UI.Xaml.Media.PointCollection) -> Void: ...
    @winrt_classmethod
    def get_FillRuleProperty(cls: Windows.UI.Xaml.Shapes.IPolylineStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_PointsProperty(cls: Windows.UI.Xaml.Shapes.IPolylineStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    FillRule = property(get_FillRule, put_FillRule)
    Points = property(get_Points, put_Points)
    FillRuleProperty = property(get_FillRuleProperty, None)
    PointsProperty = property(get_PointsProperty, None)
class Rectangle(ComPtr):
    extends: Windows.UI.Xaml.Shapes.Shape
    default_interface: Windows.UI.Xaml.Shapes.IRectangle
    _classid_ = 'Windows.UI.Xaml.Shapes.Rectangle'
    @winrt_activatemethod
    def New(cls) -> Windows.UI.Xaml.Shapes.Rectangle: ...
    @winrt_mixinmethod
    def get_RadiusX(self: Windows.UI.Xaml.Shapes.IRectangle) -> Double: ...
    @winrt_mixinmethod
    def put_RadiusX(self: Windows.UI.Xaml.Shapes.IRectangle, value: Double) -> Void: ...
    @winrt_mixinmethod
    def get_RadiusY(self: Windows.UI.Xaml.Shapes.IRectangle) -> Double: ...
    @winrt_mixinmethod
    def put_RadiusY(self: Windows.UI.Xaml.Shapes.IRectangle, value: Double) -> Void: ...
    @winrt_classmethod
    def get_RadiusXProperty(cls: Windows.UI.Xaml.Shapes.IRectangleStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_RadiusYProperty(cls: Windows.UI.Xaml.Shapes.IRectangleStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    RadiusX = property(get_RadiusX, put_RadiusX)
    RadiusY = property(get_RadiusY, put_RadiusY)
    RadiusXProperty = property(get_RadiusXProperty, None)
    RadiusYProperty = property(get_RadiusYProperty, None)
class Shape(ComPtr):
    extends: Windows.UI.Xaml.FrameworkElement
    default_interface: Windows.UI.Xaml.Shapes.IShape
    _classid_ = 'Windows.UI.Xaml.Shapes.Shape'
    @winrt_commethod(438)
    def get_Fill(self) -> Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(439)
    def put_Fill(self, value: Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(440)
    def get_Stroke(self) -> Windows.UI.Xaml.Media.Brush: ...
    @winrt_commethod(441)
    def put_Stroke(self, value: Windows.UI.Xaml.Media.Brush) -> Void: ...
    @winrt_commethod(442)
    def get_StrokeMiterLimit(self) -> Double: ...
    @winrt_commethod(443)
    def put_StrokeMiterLimit(self, value: Double) -> Void: ...
    @winrt_commethod(444)
    def get_StrokeThickness(self) -> Double: ...
    @winrt_commethod(445)
    def put_StrokeThickness(self, value: Double) -> Void: ...
    @winrt_commethod(446)
    def get_StrokeStartLineCap(self) -> Windows.UI.Xaml.Media.PenLineCap: ...
    @winrt_commethod(447)
    def put_StrokeStartLineCap(self, value: Windows.UI.Xaml.Media.PenLineCap) -> Void: ...
    @winrt_commethod(448)
    def get_StrokeEndLineCap(self) -> Windows.UI.Xaml.Media.PenLineCap: ...
    @winrt_commethod(449)
    def put_StrokeEndLineCap(self, value: Windows.UI.Xaml.Media.PenLineCap) -> Void: ...
    @winrt_commethod(450)
    def get_StrokeLineJoin(self) -> Windows.UI.Xaml.Media.PenLineJoin: ...
    @winrt_commethod(451)
    def put_StrokeLineJoin(self, value: Windows.UI.Xaml.Media.PenLineJoin) -> Void: ...
    @winrt_commethod(452)
    def get_StrokeDashOffset(self) -> Double: ...
    @winrt_commethod(453)
    def put_StrokeDashOffset(self, value: Double) -> Void: ...
    @winrt_commethod(454)
    def get_StrokeDashCap(self) -> Windows.UI.Xaml.Media.PenLineCap: ...
    @winrt_commethod(455)
    def put_StrokeDashCap(self, value: Windows.UI.Xaml.Media.PenLineCap) -> Void: ...
    @winrt_commethod(456)
    def get_StrokeDashArray(self) -> Windows.UI.Xaml.Media.DoubleCollection: ...
    @winrt_commethod(457)
    def put_StrokeDashArray(self, value: Windows.UI.Xaml.Media.DoubleCollection) -> Void: ...
    @winrt_commethod(458)
    def get_Stretch(self) -> Windows.UI.Xaml.Media.Stretch: ...
    @winrt_commethod(459)
    def put_Stretch(self, value: Windows.UI.Xaml.Media.Stretch) -> Void: ...
    @winrt_commethod(460)
    def get_GeometryTransform(self) -> Windows.UI.Xaml.Media.Transform: ...
    @winrt_commethod(461)
    def GetAlphaMask(self) -> Windows.UI.Composition.CompositionBrush: ...
    @winrt_classmethod
    def get_FillProperty(cls: Windows.UI.Xaml.Shapes.IShapeStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeProperty(cls: Windows.UI.Xaml.Shapes.IShapeStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeMiterLimitProperty(cls: Windows.UI.Xaml.Shapes.IShapeStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeThicknessProperty(cls: Windows.UI.Xaml.Shapes.IShapeStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeStartLineCapProperty(cls: Windows.UI.Xaml.Shapes.IShapeStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeEndLineCapProperty(cls: Windows.UI.Xaml.Shapes.IShapeStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeLineJoinProperty(cls: Windows.UI.Xaml.Shapes.IShapeStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeDashOffsetProperty(cls: Windows.UI.Xaml.Shapes.IShapeStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeDashCapProperty(cls: Windows.UI.Xaml.Shapes.IShapeStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StrokeDashArrayProperty(cls: Windows.UI.Xaml.Shapes.IShapeStatics) -> Windows.UI.Xaml.DependencyProperty: ...
    @winrt_classmethod
    def get_StretchProperty(cls: Windows.UI.Xaml.Shapes.IShapeStatics) -> Windows.UI.Xaml.DependencyProperty: ...
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
make_head(_module, 'Ellipse')
make_head(_module, 'IEllipse')
make_head(_module, 'ILine')
make_head(_module, 'ILineStatics')
make_head(_module, 'IPath')
make_head(_module, 'IPathFactory')
make_head(_module, 'IPathStatics')
make_head(_module, 'IPolygon')
make_head(_module, 'IPolygonStatics')
make_head(_module, 'IPolyline')
make_head(_module, 'IPolylineStatics')
make_head(_module, 'IRectangle')
make_head(_module, 'IRectangleStatics')
make_head(_module, 'IShape')
make_head(_module, 'IShape2')
make_head(_module, 'IShapeFactory')
make_head(_module, 'IShapeStatics')
make_head(_module, 'Line')
make_head(_module, 'Path')
make_head(_module, 'Polygon')
make_head(_module, 'Polyline')
make_head(_module, 'Rectangle')
make_head(_module, 'Shape')
