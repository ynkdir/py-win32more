from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Direct2D.Common
import win32more.Windows.Win32.Graphics.Dxgi.Common
import win32more.Windows.Win32.System.Com
D2D1_2DAFFINETRANSFORM_INTERPOLATION_MODE = Int32
D2D1_2DAFFINETRANSFORM_INTERPOLATION_MODE_NEAREST_NEIGHBOR: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_2DAFFINETRANSFORM_INTERPOLATION_MODE = 0
D2D1_2DAFFINETRANSFORM_INTERPOLATION_MODE_LINEAR: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_2DAFFINETRANSFORM_INTERPOLATION_MODE = 1
D2D1_2DAFFINETRANSFORM_INTERPOLATION_MODE_CUBIC: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_2DAFFINETRANSFORM_INTERPOLATION_MODE = 2
D2D1_2DAFFINETRANSFORM_INTERPOLATION_MODE_MULTI_SAMPLE_LINEAR: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_2DAFFINETRANSFORM_INTERPOLATION_MODE = 3
D2D1_2DAFFINETRANSFORM_INTERPOLATION_MODE_ANISOTROPIC: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_2DAFFINETRANSFORM_INTERPOLATION_MODE = 4
D2D1_2DAFFINETRANSFORM_INTERPOLATION_MODE_HIGH_QUALITY_CUBIC: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_2DAFFINETRANSFORM_INTERPOLATION_MODE = 5
D2D1_ALPHA_MODE = Int32
D2D1_ALPHA_MODE_UNKNOWN: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_ALPHA_MODE = 0
D2D1_ALPHA_MODE_PREMULTIPLIED: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_ALPHA_MODE = 1
D2D1_ALPHA_MODE_STRAIGHT: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_ALPHA_MODE = 2
D2D1_ALPHA_MODE_IGNORE: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_ALPHA_MODE = 3
class D2D1_BEZIER_SEGMENT(Structure):
    point1: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D_POINT_2F
    point2: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D_POINT_2F
    point3: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D_POINT_2F
D2D1_BLEND_MODE = Int32
D2D1_BLEND_MODE_MULTIPLY: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_BLEND_MODE = 0
D2D1_BLEND_MODE_SCREEN: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_BLEND_MODE = 1
D2D1_BLEND_MODE_DARKEN: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_BLEND_MODE = 2
D2D1_BLEND_MODE_LIGHTEN: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_BLEND_MODE = 3
D2D1_BLEND_MODE_DISSOLVE: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_BLEND_MODE = 4
D2D1_BLEND_MODE_COLOR_BURN: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_BLEND_MODE = 5
D2D1_BLEND_MODE_LINEAR_BURN: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_BLEND_MODE = 6
D2D1_BLEND_MODE_DARKER_COLOR: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_BLEND_MODE = 7
D2D1_BLEND_MODE_LIGHTER_COLOR: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_BLEND_MODE = 8
D2D1_BLEND_MODE_COLOR_DODGE: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_BLEND_MODE = 9
D2D1_BLEND_MODE_LINEAR_DODGE: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_BLEND_MODE = 10
D2D1_BLEND_MODE_OVERLAY: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_BLEND_MODE = 11
D2D1_BLEND_MODE_SOFT_LIGHT: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_BLEND_MODE = 12
D2D1_BLEND_MODE_HARD_LIGHT: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_BLEND_MODE = 13
D2D1_BLEND_MODE_VIVID_LIGHT: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_BLEND_MODE = 14
D2D1_BLEND_MODE_LINEAR_LIGHT: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_BLEND_MODE = 15
D2D1_BLEND_MODE_PIN_LIGHT: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_BLEND_MODE = 16
D2D1_BLEND_MODE_HARD_MIX: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_BLEND_MODE = 17
D2D1_BLEND_MODE_DIFFERENCE: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_BLEND_MODE = 18
D2D1_BLEND_MODE_EXCLUSION: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_BLEND_MODE = 19
D2D1_BLEND_MODE_HUE: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_BLEND_MODE = 20
D2D1_BLEND_MODE_SATURATION: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_BLEND_MODE = 21
D2D1_BLEND_MODE_COLOR: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_BLEND_MODE = 22
D2D1_BLEND_MODE_LUMINOSITY: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_BLEND_MODE = 23
D2D1_BLEND_MODE_SUBTRACT: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_BLEND_MODE = 24
D2D1_BLEND_MODE_DIVISION: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_BLEND_MODE = 25
D2D1_BORDER_MODE = Int32
D2D1_BORDER_MODE_SOFT: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_BORDER_MODE = 0
D2D1_BORDER_MODE_HARD: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_BORDER_MODE = 1
D2D1_COLORMATRIX_ALPHA_MODE = Int32
D2D1_COLORMATRIX_ALPHA_MODE_PREMULTIPLIED: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_COLORMATRIX_ALPHA_MODE = 1
D2D1_COLORMATRIX_ALPHA_MODE_STRAIGHT: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_COLORMATRIX_ALPHA_MODE = 2
class D2D1_COLOR_F(Structure):
    r: Single
    g: Single
    b: Single
    a: Single
D2D1_COMPOSITE_MODE = Int32
D2D1_COMPOSITE_MODE_SOURCE_OVER: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_COMPOSITE_MODE = 0
D2D1_COMPOSITE_MODE_DESTINATION_OVER: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_COMPOSITE_MODE = 1
D2D1_COMPOSITE_MODE_SOURCE_IN: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_COMPOSITE_MODE = 2
D2D1_COMPOSITE_MODE_DESTINATION_IN: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_COMPOSITE_MODE = 3
D2D1_COMPOSITE_MODE_SOURCE_OUT: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_COMPOSITE_MODE = 4
D2D1_COMPOSITE_MODE_DESTINATION_OUT: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_COMPOSITE_MODE = 5
D2D1_COMPOSITE_MODE_SOURCE_ATOP: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_COMPOSITE_MODE = 6
D2D1_COMPOSITE_MODE_DESTINATION_ATOP: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_COMPOSITE_MODE = 7
D2D1_COMPOSITE_MODE_XOR: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_COMPOSITE_MODE = 8
D2D1_COMPOSITE_MODE_PLUS: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_COMPOSITE_MODE = 9
D2D1_COMPOSITE_MODE_SOURCE_COPY: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_COMPOSITE_MODE = 10
D2D1_COMPOSITE_MODE_BOUNDED_SOURCE_COPY: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_COMPOSITE_MODE = 11
D2D1_COMPOSITE_MODE_MASK_INVERT: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_COMPOSITE_MODE = 12
D2D1_FIGURE_BEGIN = Int32
D2D1_FIGURE_BEGIN_FILLED: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_FIGURE_BEGIN = 0
D2D1_FIGURE_BEGIN_HOLLOW: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_FIGURE_BEGIN = 1
D2D1_FIGURE_END = Int32
D2D1_FIGURE_END_OPEN: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_FIGURE_END = 0
D2D1_FIGURE_END_CLOSED: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_FIGURE_END = 1
D2D1_FILL_MODE = Int32
D2D1_FILL_MODE_ALTERNATE: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_FILL_MODE = 0
D2D1_FILL_MODE_WINDING: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_FILL_MODE = 1
class D2D1_GRADIENT_STOP(Structure):
    position: Single
    color: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_COLOR_F
D2D1_PATH_SEGMENT = Int32
D2D1_PATH_SEGMENT_NONE: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_PATH_SEGMENT = 0
D2D1_PATH_SEGMENT_FORCE_UNSTROKED: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_PATH_SEGMENT = 1
D2D1_PATH_SEGMENT_FORCE_ROUND_LINE_JOIN: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_PATH_SEGMENT = 2
class D2D1_PIXEL_FORMAT(Structure):
    format: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT
    alphaMode: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_ALPHA_MODE
D2D1_TURBULENCE_NOISE = Int32
D2D1_TURBULENCE_NOISE_FRACTAL_SUM: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_TURBULENCE_NOISE = 0
D2D1_TURBULENCE_NOISE_TURBULENCE: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_TURBULENCE_NOISE = 1
class D2D_COLOR_F(Structure):
    r: Single
    g: Single
    b: Single
    a: Single
class D2D_MATRIX_3X2_F(Structure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous1: _Anonymous1_e__Struct
        Anonymous2: _Anonymous2_e__Struct
        m: Single * 6
        class _Anonymous1_e__Struct(Structure):
            m11: Single
            m12: Single
            m21: Single
            m22: Single
            dx: Single
            dy: Single
        class _Anonymous2_e__Struct(Structure):
            _11: Single
            _12: Single
            _21: Single
            _22: Single
            _31: Single
            _32: Single
class D2D_MATRIX_4X3_F(Structure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        m: Single * 12
        class _Anonymous_e__Struct(Structure):
            _11: Single
            _12: Single
            _13: Single
            _21: Single
            _22: Single
            _23: Single
            _31: Single
            _32: Single
            _33: Single
            _41: Single
            _42: Single
            _43: Single
class D2D_MATRIX_4X4_F(Structure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        m: Single * 16
        class _Anonymous_e__Struct(Structure):
            _11: Single
            _12: Single
            _13: Single
            _14: Single
            _21: Single
            _22: Single
            _23: Single
            _24: Single
            _31: Single
            _32: Single
            _33: Single
            _34: Single
            _41: Single
            _42: Single
            _43: Single
            _44: Single
class D2D_MATRIX_5X4_F(Structure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Anonymous: _Anonymous_e__Struct
        m: Single * 20
        class _Anonymous_e__Struct(Structure):
            _11: Single
            _12: Single
            _13: Single
            _14: Single
            _21: Single
            _22: Single
            _23: Single
            _24: Single
            _31: Single
            _32: Single
            _33: Single
            _34: Single
            _41: Single
            _42: Single
            _43: Single
            _44: Single
            _51: Single
            _52: Single
            _53: Single
            _54: Single
class D2D_POINT_2F(Structure):
    x: Single
    y: Single
class D2D_POINT_2U(Structure):
    x: UInt32
    y: UInt32
class D2D_RECT_F(Structure):
    left: Single
    top: Single
    right: Single
    bottom: Single
class D2D_RECT_U(Structure):
    left: UInt32
    top: UInt32
    right: UInt32
    bottom: UInt32
class D2D_SIZE_F(Structure):
    width: Single
    height: Single
class D2D_SIZE_U(Structure):
    width: UInt32
    height: UInt32
class D2D_VECTOR_2F(Structure):
    x: Single
    y: Single
class D2D_VECTOR_3F(Structure):
    x: Single
    y: Single
    z: Single
class D2D_VECTOR_4F(Structure):
    x: Single
    y: Single
    z: Single
    w: Single
class ID2D1SimplifiedGeometrySink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2cd9069e-12e2-11dc-9fed-001143a055f9}')
    @commethod(3)
    def SetFillMode(self, fillMode: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_FILL_MODE) -> Void: ...
    @commethod(4)
    def SetSegmentFlags(self, vertexFlags: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_PATH_SEGMENT) -> Void: ...
    @commethod(5)
    def BeginFigure(self, startPoint: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D_POINT_2F, figureBegin: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_FIGURE_BEGIN) -> Void: ...
    @commethod(6)
    def AddLines(self, points: POINTER(win32more.Windows.Win32.Graphics.Direct2D.Common.D2D_POINT_2F), pointsCount: UInt32) -> Void: ...
    @commethod(7)
    def AddBeziers(self, beziers: POINTER(win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_BEZIER_SEGMENT), beziersCount: UInt32) -> Void: ...
    @commethod(8)
    def EndFigure(self, figureEnd: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_FIGURE_END) -> Void: ...
    @commethod(9)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
