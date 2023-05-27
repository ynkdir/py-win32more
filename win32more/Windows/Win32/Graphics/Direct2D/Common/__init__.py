from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Direct2D.Common
import win32more.Windows.Win32.Graphics.Dxgi.Common
import win32more.Windows.Win32.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
D2D1_2DAFFINETRANSFORM_INTERPOLATION_MODE = UInt32
D2D1_2DAFFINETRANSFORM_INTERPOLATION_MODE_NEAREST_NEIGHBOR: D2D1_2DAFFINETRANSFORM_INTERPOLATION_MODE = 0
D2D1_2DAFFINETRANSFORM_INTERPOLATION_MODE_LINEAR: D2D1_2DAFFINETRANSFORM_INTERPOLATION_MODE = 1
D2D1_2DAFFINETRANSFORM_INTERPOLATION_MODE_CUBIC: D2D1_2DAFFINETRANSFORM_INTERPOLATION_MODE = 2
D2D1_2DAFFINETRANSFORM_INTERPOLATION_MODE_MULTI_SAMPLE_LINEAR: D2D1_2DAFFINETRANSFORM_INTERPOLATION_MODE = 3
D2D1_2DAFFINETRANSFORM_INTERPOLATION_MODE_ANISOTROPIC: D2D1_2DAFFINETRANSFORM_INTERPOLATION_MODE = 4
D2D1_2DAFFINETRANSFORM_INTERPOLATION_MODE_HIGH_QUALITY_CUBIC: D2D1_2DAFFINETRANSFORM_INTERPOLATION_MODE = 5
D2D1_ALPHA_MODE = UInt32
D2D1_ALPHA_MODE_UNKNOWN: D2D1_ALPHA_MODE = 0
D2D1_ALPHA_MODE_PREMULTIPLIED: D2D1_ALPHA_MODE = 1
D2D1_ALPHA_MODE_STRAIGHT: D2D1_ALPHA_MODE = 2
D2D1_ALPHA_MODE_IGNORE: D2D1_ALPHA_MODE = 3
class D2D1_BEZIER_SEGMENT(EasyCastStructure):
    point1: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D_POINT_2F
    point2: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D_POINT_2F
    point3: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D_POINT_2F
D2D1_BLEND_MODE = UInt32
D2D1_BLEND_MODE_MULTIPLY: D2D1_BLEND_MODE = 0
D2D1_BLEND_MODE_SCREEN: D2D1_BLEND_MODE = 1
D2D1_BLEND_MODE_DARKEN: D2D1_BLEND_MODE = 2
D2D1_BLEND_MODE_LIGHTEN: D2D1_BLEND_MODE = 3
D2D1_BLEND_MODE_DISSOLVE: D2D1_BLEND_MODE = 4
D2D1_BLEND_MODE_COLOR_BURN: D2D1_BLEND_MODE = 5
D2D1_BLEND_MODE_LINEAR_BURN: D2D1_BLEND_MODE = 6
D2D1_BLEND_MODE_DARKER_COLOR: D2D1_BLEND_MODE = 7
D2D1_BLEND_MODE_LIGHTER_COLOR: D2D1_BLEND_MODE = 8
D2D1_BLEND_MODE_COLOR_DODGE: D2D1_BLEND_MODE = 9
D2D1_BLEND_MODE_LINEAR_DODGE: D2D1_BLEND_MODE = 10
D2D1_BLEND_MODE_OVERLAY: D2D1_BLEND_MODE = 11
D2D1_BLEND_MODE_SOFT_LIGHT: D2D1_BLEND_MODE = 12
D2D1_BLEND_MODE_HARD_LIGHT: D2D1_BLEND_MODE = 13
D2D1_BLEND_MODE_VIVID_LIGHT: D2D1_BLEND_MODE = 14
D2D1_BLEND_MODE_LINEAR_LIGHT: D2D1_BLEND_MODE = 15
D2D1_BLEND_MODE_PIN_LIGHT: D2D1_BLEND_MODE = 16
D2D1_BLEND_MODE_HARD_MIX: D2D1_BLEND_MODE = 17
D2D1_BLEND_MODE_DIFFERENCE: D2D1_BLEND_MODE = 18
D2D1_BLEND_MODE_EXCLUSION: D2D1_BLEND_MODE = 19
D2D1_BLEND_MODE_HUE: D2D1_BLEND_MODE = 20
D2D1_BLEND_MODE_SATURATION: D2D1_BLEND_MODE = 21
D2D1_BLEND_MODE_COLOR: D2D1_BLEND_MODE = 22
D2D1_BLEND_MODE_LUMINOSITY: D2D1_BLEND_MODE = 23
D2D1_BLEND_MODE_SUBTRACT: D2D1_BLEND_MODE = 24
D2D1_BLEND_MODE_DIVISION: D2D1_BLEND_MODE = 25
D2D1_BORDER_MODE = UInt32
D2D1_BORDER_MODE_SOFT: D2D1_BORDER_MODE = 0
D2D1_BORDER_MODE_HARD: D2D1_BORDER_MODE = 1
D2D1_COLORMATRIX_ALPHA_MODE = UInt32
D2D1_COLORMATRIX_ALPHA_MODE_PREMULTIPLIED: D2D1_COLORMATRIX_ALPHA_MODE = 1
D2D1_COLORMATRIX_ALPHA_MODE_STRAIGHT: D2D1_COLORMATRIX_ALPHA_MODE = 2
class D2D1_COLOR_F(EasyCastStructure):
    r: Single
    g: Single
    b: Single
    a: Single
D2D1_COMPOSITE_MODE = UInt32
D2D1_COMPOSITE_MODE_SOURCE_OVER: D2D1_COMPOSITE_MODE = 0
D2D1_COMPOSITE_MODE_DESTINATION_OVER: D2D1_COMPOSITE_MODE = 1
D2D1_COMPOSITE_MODE_SOURCE_IN: D2D1_COMPOSITE_MODE = 2
D2D1_COMPOSITE_MODE_DESTINATION_IN: D2D1_COMPOSITE_MODE = 3
D2D1_COMPOSITE_MODE_SOURCE_OUT: D2D1_COMPOSITE_MODE = 4
D2D1_COMPOSITE_MODE_DESTINATION_OUT: D2D1_COMPOSITE_MODE = 5
D2D1_COMPOSITE_MODE_SOURCE_ATOP: D2D1_COMPOSITE_MODE = 6
D2D1_COMPOSITE_MODE_DESTINATION_ATOP: D2D1_COMPOSITE_MODE = 7
D2D1_COMPOSITE_MODE_XOR: D2D1_COMPOSITE_MODE = 8
D2D1_COMPOSITE_MODE_PLUS: D2D1_COMPOSITE_MODE = 9
D2D1_COMPOSITE_MODE_SOURCE_COPY: D2D1_COMPOSITE_MODE = 10
D2D1_COMPOSITE_MODE_BOUNDED_SOURCE_COPY: D2D1_COMPOSITE_MODE = 11
D2D1_COMPOSITE_MODE_MASK_INVERT: D2D1_COMPOSITE_MODE = 12
D2D1_FIGURE_BEGIN = UInt32
D2D1_FIGURE_BEGIN_FILLED: D2D1_FIGURE_BEGIN = 0
D2D1_FIGURE_BEGIN_HOLLOW: D2D1_FIGURE_BEGIN = 1
D2D1_FIGURE_END = UInt32
D2D1_FIGURE_END_OPEN: D2D1_FIGURE_END = 0
D2D1_FIGURE_END_CLOSED: D2D1_FIGURE_END = 1
D2D1_FILL_MODE = UInt32
D2D1_FILL_MODE_ALTERNATE: D2D1_FILL_MODE = 0
D2D1_FILL_MODE_WINDING: D2D1_FILL_MODE = 1
D2D1_PATH_SEGMENT = UInt32
D2D1_PATH_SEGMENT_NONE: D2D1_PATH_SEGMENT = 0
D2D1_PATH_SEGMENT_FORCE_UNSTROKED: D2D1_PATH_SEGMENT = 1
D2D1_PATH_SEGMENT_FORCE_ROUND_LINE_JOIN: D2D1_PATH_SEGMENT = 2
class D2D1_PIXEL_FORMAT(EasyCastStructure):
    format: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT
    alphaMode: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_ALPHA_MODE
D2D1_TURBULENCE_NOISE = UInt32
D2D1_TURBULENCE_NOISE_FRACTAL_SUM: D2D1_TURBULENCE_NOISE = 0
D2D1_TURBULENCE_NOISE_TURBULENCE: D2D1_TURBULENCE_NOISE = 1
class D2D_COLOR_F(EasyCastStructure):
    r: Single
    g: Single
    b: Single
    a: Single
class D2D_MATRIX_3X2_F(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Anonymous1: _Anonymous1_e__Struct
        Anonymous2: _Anonymous2_e__Struct
        m: Single * 6
        class _Anonymous1_e__Struct(EasyCastStructure):
            m11: Single
            m12: Single
            m21: Single
            m22: Single
            dx: Single
            dy: Single
        class _Anonymous2_e__Struct(EasyCastStructure):
            _11: Single
            _12: Single
            _21: Single
            _22: Single
            _31: Single
            _32: Single
class D2D_MATRIX_4X3_F(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        m: Single * 12
        class _Anonymous_e__Struct(EasyCastStructure):
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
class D2D_MATRIX_4X4_F(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        m: Single * 16
        class _Anonymous_e__Struct(EasyCastStructure):
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
class D2D_MATRIX_5X4_F(EasyCastStructure):
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        Anonymous: _Anonymous_e__Struct
        m: Single * 20
        class _Anonymous_e__Struct(EasyCastStructure):
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
class D2D_POINT_2F(EasyCastStructure):
    x: Single
    y: Single
class D2D_POINT_2U(EasyCastStructure):
    x: UInt32
    y: UInt32
class D2D_RECT_F(EasyCastStructure):
    left: Single
    top: Single
    right: Single
    bottom: Single
class D2D_RECT_U(EasyCastStructure):
    left: UInt32
    top: UInt32
    right: UInt32
    bottom: UInt32
class D2D_SIZE_F(EasyCastStructure):
    width: Single
    height: Single
class D2D_SIZE_U(EasyCastStructure):
    width: UInt32
    height: UInt32
class D2D_VECTOR_2F(EasyCastStructure):
    x: Single
    y: Single
class D2D_VECTOR_3F(EasyCastStructure):
    x: Single
    y: Single
    z: Single
class D2D_VECTOR_4F(EasyCastStructure):
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
    def AddLines(self, points: POINTER(win32more.Windows.Win32.Graphics.Direct2D.Common.D2D_POINT_2F_head), pointsCount: UInt32) -> Void: ...
    @commethod(7)
    def AddBeziers(self, beziers: POINTER(win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_BEZIER_SEGMENT_head), beziersCount: UInt32) -> Void: ...
    @commethod(8)
    def EndFigure(self, figureEnd: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D1_FIGURE_END) -> Void: ...
    @commethod(9)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'D2D1_BEZIER_SEGMENT')
make_head(_module, 'D2D1_COLOR_F')
make_head(_module, 'D2D1_PIXEL_FORMAT')
make_head(_module, 'D2D_COLOR_F')
make_head(_module, 'D2D_MATRIX_3X2_F')
make_head(_module, 'D2D_MATRIX_4X3_F')
make_head(_module, 'D2D_MATRIX_4X4_F')
make_head(_module, 'D2D_MATRIX_5X4_F')
make_head(_module, 'D2D_POINT_2F')
make_head(_module, 'D2D_POINT_2U')
make_head(_module, 'D2D_RECT_F')
make_head(_module, 'D2D_RECT_U')
make_head(_module, 'D2D_SIZE_F')
make_head(_module, 'D2D_SIZE_U')
make_head(_module, 'D2D_VECTOR_2F')
make_head(_module, 'D2D_VECTOR_3F')
make_head(_module, 'D2D_VECTOR_4F')
make_head(_module, 'ID2D1SimplifiedGeometrySink')
