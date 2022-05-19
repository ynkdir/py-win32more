from win32more import *
import win32more.Foundation
import win32more.Graphics.Direct2D.Common
import win32more.Graphics.Dxgi.Common
import win32more.System.Com

import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f"_define_{name}"]
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
def _define_D2D_COLOR_F_head():
    class D2D_COLOR_F(Structure):
        pass
    return D2D_COLOR_F
def _define_D2D_COLOR_F():
    D2D_COLOR_F = win32more.Graphics.Direct2D.Common.D2D_COLOR_F_head
    D2D_COLOR_F._fields_ = [
        ("r", Single),
        ("g", Single),
        ("b", Single),
        ("a", Single),
    ]
    return D2D_COLOR_F
def _define_D2D1_COLOR_F_head():
    class D2D1_COLOR_F(Structure):
        pass
    return D2D1_COLOR_F
def _define_D2D1_COLOR_F():
    D2D1_COLOR_F = win32more.Graphics.Direct2D.Common.D2D1_COLOR_F_head
    D2D1_COLOR_F._fields_ = [
        ("r", Single),
        ("g", Single),
        ("b", Single),
        ("a", Single),
    ]
    return D2D1_COLOR_F
D2D1_ALPHA_MODE = UInt32
D2D1_ALPHA_MODE_UNKNOWN = 0
D2D1_ALPHA_MODE_PREMULTIPLIED = 1
D2D1_ALPHA_MODE_STRAIGHT = 2
D2D1_ALPHA_MODE_IGNORE = 3
D2D1_ALPHA_MODE_FORCE_DWORD = 4294967295
def _define_D2D1_PIXEL_FORMAT_head():
    class D2D1_PIXEL_FORMAT(Structure):
        pass
    return D2D1_PIXEL_FORMAT
def _define_D2D1_PIXEL_FORMAT():
    D2D1_PIXEL_FORMAT = win32more.Graphics.Direct2D.Common.D2D1_PIXEL_FORMAT_head
    D2D1_PIXEL_FORMAT._fields_ = [
        ("format", win32more.Graphics.Dxgi.Common.DXGI_FORMAT),
        ("alphaMode", win32more.Graphics.Direct2D.Common.D2D1_ALPHA_MODE),
    ]
    return D2D1_PIXEL_FORMAT
def _define_D2D_POINT_2U_head():
    class D2D_POINT_2U(Structure):
        pass
    return D2D_POINT_2U
def _define_D2D_POINT_2U():
    D2D_POINT_2U = win32more.Graphics.Direct2D.Common.D2D_POINT_2U_head
    D2D_POINT_2U._fields_ = [
        ("x", UInt32),
        ("y", UInt32),
    ]
    return D2D_POINT_2U
def _define_D2D_POINT_2F_head():
    class D2D_POINT_2F(Structure):
        pass
    return D2D_POINT_2F
def _define_D2D_POINT_2F():
    D2D_POINT_2F = win32more.Graphics.Direct2D.Common.D2D_POINT_2F_head
    D2D_POINT_2F._fields_ = [
        ("x", Single),
        ("y", Single),
    ]
    return D2D_POINT_2F
def _define_D2D_VECTOR_2F_head():
    class D2D_VECTOR_2F(Structure):
        pass
    return D2D_VECTOR_2F
def _define_D2D_VECTOR_2F():
    D2D_VECTOR_2F = win32more.Graphics.Direct2D.Common.D2D_VECTOR_2F_head
    D2D_VECTOR_2F._fields_ = [
        ("x", Single),
        ("y", Single),
    ]
    return D2D_VECTOR_2F
def _define_D2D_VECTOR_3F_head():
    class D2D_VECTOR_3F(Structure):
        pass
    return D2D_VECTOR_3F
def _define_D2D_VECTOR_3F():
    D2D_VECTOR_3F = win32more.Graphics.Direct2D.Common.D2D_VECTOR_3F_head
    D2D_VECTOR_3F._fields_ = [
        ("x", Single),
        ("y", Single),
        ("z", Single),
    ]
    return D2D_VECTOR_3F
def _define_D2D_VECTOR_4F_head():
    class D2D_VECTOR_4F(Structure):
        pass
    return D2D_VECTOR_4F
def _define_D2D_VECTOR_4F():
    D2D_VECTOR_4F = win32more.Graphics.Direct2D.Common.D2D_VECTOR_4F_head
    D2D_VECTOR_4F._fields_ = [
        ("x", Single),
        ("y", Single),
        ("z", Single),
        ("w", Single),
    ]
    return D2D_VECTOR_4F
def _define_D2D_RECT_F_head():
    class D2D_RECT_F(Structure):
        pass
    return D2D_RECT_F
def _define_D2D_RECT_F():
    D2D_RECT_F = win32more.Graphics.Direct2D.Common.D2D_RECT_F_head
    D2D_RECT_F._fields_ = [
        ("left", Single),
        ("top", Single),
        ("right", Single),
        ("bottom", Single),
    ]
    return D2D_RECT_F
def _define_D2D_RECT_U_head():
    class D2D_RECT_U(Structure):
        pass
    return D2D_RECT_U
def _define_D2D_RECT_U():
    D2D_RECT_U = win32more.Graphics.Direct2D.Common.D2D_RECT_U_head
    D2D_RECT_U._fields_ = [
        ("left", UInt32),
        ("top", UInt32),
        ("right", UInt32),
        ("bottom", UInt32),
    ]
    return D2D_RECT_U
def _define_D2D_SIZE_F_head():
    class D2D_SIZE_F(Structure):
        pass
    return D2D_SIZE_F
def _define_D2D_SIZE_F():
    D2D_SIZE_F = win32more.Graphics.Direct2D.Common.D2D_SIZE_F_head
    D2D_SIZE_F._fields_ = [
        ("width", Single),
        ("height", Single),
    ]
    return D2D_SIZE_F
def _define_D2D_SIZE_U_head():
    class D2D_SIZE_U(Structure):
        pass
    return D2D_SIZE_U
def _define_D2D_SIZE_U():
    D2D_SIZE_U = win32more.Graphics.Direct2D.Common.D2D_SIZE_U_head
    D2D_SIZE_U._fields_ = [
        ("width", UInt32),
        ("height", UInt32),
    ]
    return D2D_SIZE_U
def _define_D2D_MATRIX_3X2_F_head():
    class D2D_MATRIX_3X2_F(Structure):
        pass
    return D2D_MATRIX_3X2_F
def _define_D2D_MATRIX_3X2_F():
    D2D_MATRIX_3X2_F = win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head
    class D2D_MATRIX_3X2_F__Anonymous_e__Union(Union):
        pass
    class D2D_MATRIX_3X2_F__Anonymous_e__Union__Anonymous1_e__Struct(Structure):
        pass
    D2D_MATRIX_3X2_F__Anonymous_e__Union__Anonymous1_e__Struct._fields_ = [
        ("m11", Single),
        ("m12", Single),
        ("m21", Single),
        ("m22", Single),
        ("dx", Single),
        ("dy", Single),
    ]
    class D2D_MATRIX_3X2_F__Anonymous_e__Union__Anonymous2_e__Struct(Structure):
        pass
    D2D_MATRIX_3X2_F__Anonymous_e__Union__Anonymous2_e__Struct._fields_ = [
        ("_11", Single),
        ("_12", Single),
        ("_21", Single),
        ("_22", Single),
        ("_31", Single),
        ("_32", Single),
    ]
    D2D_MATRIX_3X2_F__Anonymous_e__Union._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    D2D_MATRIX_3X2_F__Anonymous_e__Union._fields_ = [
        ("Anonymous1", D2D_MATRIX_3X2_F__Anonymous_e__Union__Anonymous1_e__Struct),
        ("Anonymous2", D2D_MATRIX_3X2_F__Anonymous_e__Union__Anonymous2_e__Struct),
        ("m", Single * 6),
    ]
    D2D_MATRIX_3X2_F._anonymous_ = [
        'Anonymous',
    ]
    D2D_MATRIX_3X2_F._fields_ = [
        ("Anonymous", D2D_MATRIX_3X2_F__Anonymous_e__Union),
    ]
    return D2D_MATRIX_3X2_F
def _define_D2D_MATRIX_4X3_F_head():
    class D2D_MATRIX_4X3_F(Structure):
        pass
    return D2D_MATRIX_4X3_F
def _define_D2D_MATRIX_4X3_F():
    D2D_MATRIX_4X3_F = win32more.Graphics.Direct2D.Common.D2D_MATRIX_4X3_F_head
    class D2D_MATRIX_4X3_F__Anonymous_e__Union(Union):
        pass
    class D2D_MATRIX_4X3_F__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    D2D_MATRIX_4X3_F__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("_11", Single),
        ("_12", Single),
        ("_13", Single),
        ("_21", Single),
        ("_22", Single),
        ("_23", Single),
        ("_31", Single),
        ("_32", Single),
        ("_33", Single),
        ("_41", Single),
        ("_42", Single),
        ("_43", Single),
    ]
    D2D_MATRIX_4X3_F__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    D2D_MATRIX_4X3_F__Anonymous_e__Union._fields_ = [
        ("Anonymous", D2D_MATRIX_4X3_F__Anonymous_e__Union__Anonymous_e__Struct),
        ("m", Single * 12),
    ]
    D2D_MATRIX_4X3_F._anonymous_ = [
        'Anonymous',
    ]
    D2D_MATRIX_4X3_F._fields_ = [
        ("Anonymous", D2D_MATRIX_4X3_F__Anonymous_e__Union),
    ]
    return D2D_MATRIX_4X3_F
def _define_D2D_MATRIX_4X4_F_head():
    class D2D_MATRIX_4X4_F(Structure):
        pass
    return D2D_MATRIX_4X4_F
def _define_D2D_MATRIX_4X4_F():
    D2D_MATRIX_4X4_F = win32more.Graphics.Direct2D.Common.D2D_MATRIX_4X4_F_head
    class D2D_MATRIX_4X4_F__Anonymous_e__Union(Union):
        pass
    class D2D_MATRIX_4X4_F__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    D2D_MATRIX_4X4_F__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("_11", Single),
        ("_12", Single),
        ("_13", Single),
        ("_14", Single),
        ("_21", Single),
        ("_22", Single),
        ("_23", Single),
        ("_24", Single),
        ("_31", Single),
        ("_32", Single),
        ("_33", Single),
        ("_34", Single),
        ("_41", Single),
        ("_42", Single),
        ("_43", Single),
        ("_44", Single),
    ]
    D2D_MATRIX_4X4_F__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    D2D_MATRIX_4X4_F__Anonymous_e__Union._fields_ = [
        ("Anonymous", D2D_MATRIX_4X4_F__Anonymous_e__Union__Anonymous_e__Struct),
        ("m", Single * 16),
    ]
    D2D_MATRIX_4X4_F._anonymous_ = [
        'Anonymous',
    ]
    D2D_MATRIX_4X4_F._fields_ = [
        ("Anonymous", D2D_MATRIX_4X4_F__Anonymous_e__Union),
    ]
    return D2D_MATRIX_4X4_F
def _define_D2D_MATRIX_5X4_F_head():
    class D2D_MATRIX_5X4_F(Structure):
        pass
    return D2D_MATRIX_5X4_F
def _define_D2D_MATRIX_5X4_F():
    D2D_MATRIX_5X4_F = win32more.Graphics.Direct2D.Common.D2D_MATRIX_5X4_F_head
    class D2D_MATRIX_5X4_F__Anonymous_e__Union(Union):
        pass
    class D2D_MATRIX_5X4_F__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    D2D_MATRIX_5X4_F__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("_11", Single),
        ("_12", Single),
        ("_13", Single),
        ("_14", Single),
        ("_21", Single),
        ("_22", Single),
        ("_23", Single),
        ("_24", Single),
        ("_31", Single),
        ("_32", Single),
        ("_33", Single),
        ("_34", Single),
        ("_41", Single),
        ("_42", Single),
        ("_43", Single),
        ("_44", Single),
        ("_51", Single),
        ("_52", Single),
        ("_53", Single),
        ("_54", Single),
    ]
    D2D_MATRIX_5X4_F__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    D2D_MATRIX_5X4_F__Anonymous_e__Union._fields_ = [
        ("Anonymous", D2D_MATRIX_5X4_F__Anonymous_e__Union__Anonymous_e__Struct),
        ("m", Single * 20),
    ]
    D2D_MATRIX_5X4_F._anonymous_ = [
        'Anonymous',
    ]
    D2D_MATRIX_5X4_F._fields_ = [
        ("Anonymous", D2D_MATRIX_5X4_F__Anonymous_e__Union),
    ]
    return D2D_MATRIX_5X4_F
D2D1_FIGURE_BEGIN = UInt32
D2D1_FIGURE_BEGIN_FILLED = 0
D2D1_FIGURE_BEGIN_HOLLOW = 1
D2D1_FIGURE_BEGIN_FORCE_DWORD = 4294967295
D2D1_FIGURE_END = UInt32
D2D1_FIGURE_END_OPEN = 0
D2D1_FIGURE_END_CLOSED = 1
D2D1_FIGURE_END_FORCE_DWORD = 4294967295
def _define_D2D1_BEZIER_SEGMENT_head():
    class D2D1_BEZIER_SEGMENT(Structure):
        pass
    return D2D1_BEZIER_SEGMENT
def _define_D2D1_BEZIER_SEGMENT():
    D2D1_BEZIER_SEGMENT = win32more.Graphics.Direct2D.Common.D2D1_BEZIER_SEGMENT_head
    D2D1_BEZIER_SEGMENT._fields_ = [
        ("point1", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("point2", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("point3", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
    ]
    return D2D1_BEZIER_SEGMENT
D2D1_PATH_SEGMENT = UInt32
D2D1_PATH_SEGMENT_NONE = 0
D2D1_PATH_SEGMENT_FORCE_UNSTROKED = 1
D2D1_PATH_SEGMENT_FORCE_ROUND_LINE_JOIN = 2
D2D1_PATH_SEGMENT_FORCE_DWORD = 4294967295
D2D1_FILL_MODE = UInt32
D2D1_FILL_MODE_ALTERNATE = 0
D2D1_FILL_MODE_WINDING = 1
D2D1_FILL_MODE_FORCE_DWORD = 4294967295
def _define_ID2D1SimplifiedGeometrySink_head():
    class ID2D1SimplifiedGeometrySink(win32more.System.Com.IUnknown_head):
        Guid = Guid('2cd9069e-12e2-11dc-9fed-001143a055f9')
    return ID2D1SimplifiedGeometrySink
def _define_ID2D1SimplifiedGeometrySink():
    ID2D1SimplifiedGeometrySink = win32more.Graphics.Direct2D.Common.ID2D1SimplifiedGeometrySink_head
    ID2D1SimplifiedGeometrySink.SetFillMode = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.Common.D2D1_FILL_MODE, use_last_error=False)(3, 'SetFillMode', ((1, 'fillMode'),)))
    ID2D1SimplifiedGeometrySink.SetSegmentFlags = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.Common.D2D1_PATH_SEGMENT, use_last_error=False)(4, 'SetSegmentFlags', ((1, 'vertexFlags'),)))
    ID2D1SimplifiedGeometrySink.BeginFigure = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.Common.D2D_POINT_2F,win32more.Graphics.Direct2D.Common.D2D1_FIGURE_BEGIN, use_last_error=False)(5, 'BeginFigure', ((1, 'startPoint'),(1, 'figureBegin'),)))
    ID2D1SimplifiedGeometrySink.AddLines = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2F),UInt32, use_last_error=False)(6, 'AddLines', ((1, 'points'),(1, 'pointsCount'),)))
    ID2D1SimplifiedGeometrySink.AddBeziers = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.Common.D2D1_BEZIER_SEGMENT),UInt32, use_last_error=False)(7, 'AddBeziers', ((1, 'beziers'),(1, 'beziersCount'),)))
    ID2D1SimplifiedGeometrySink.EndFigure = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.Common.D2D1_FIGURE_END, use_last_error=False)(8, 'EndFigure', ((1, 'figureEnd'),)))
    ID2D1SimplifiedGeometrySink.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'Close', ()))
    return ID2D1SimplifiedGeometrySink
D2D1_BORDER_MODE = UInt32
D2D1_BORDER_MODE_SOFT = 0
D2D1_BORDER_MODE_HARD = 1
D2D1_BORDER_MODE_FORCE_DWORD = 4294967295
D2D1_BLEND_MODE = UInt32
D2D1_BLEND_MODE_MULTIPLY = 0
D2D1_BLEND_MODE_SCREEN = 1
D2D1_BLEND_MODE_DARKEN = 2
D2D1_BLEND_MODE_LIGHTEN = 3
D2D1_BLEND_MODE_DISSOLVE = 4
D2D1_BLEND_MODE_COLOR_BURN = 5
D2D1_BLEND_MODE_LINEAR_BURN = 6
D2D1_BLEND_MODE_DARKER_COLOR = 7
D2D1_BLEND_MODE_LIGHTER_COLOR = 8
D2D1_BLEND_MODE_COLOR_DODGE = 9
D2D1_BLEND_MODE_LINEAR_DODGE = 10
D2D1_BLEND_MODE_OVERLAY = 11
D2D1_BLEND_MODE_SOFT_LIGHT = 12
D2D1_BLEND_MODE_HARD_LIGHT = 13
D2D1_BLEND_MODE_VIVID_LIGHT = 14
D2D1_BLEND_MODE_LINEAR_LIGHT = 15
D2D1_BLEND_MODE_PIN_LIGHT = 16
D2D1_BLEND_MODE_HARD_MIX = 17
D2D1_BLEND_MODE_DIFFERENCE = 18
D2D1_BLEND_MODE_EXCLUSION = 19
D2D1_BLEND_MODE_HUE = 20
D2D1_BLEND_MODE_SATURATION = 21
D2D1_BLEND_MODE_COLOR = 22
D2D1_BLEND_MODE_LUMINOSITY = 23
D2D1_BLEND_MODE_SUBTRACT = 24
D2D1_BLEND_MODE_DIVISION = 25
D2D1_BLEND_MODE_FORCE_DWORD = 4294967295
D2D1_COLORMATRIX_ALPHA_MODE = UInt32
D2D1_COLORMATRIX_ALPHA_MODE_PREMULTIPLIED = 1
D2D1_COLORMATRIX_ALPHA_MODE_STRAIGHT = 2
D2D1_COLORMATRIX_ALPHA_MODE_FORCE_DWORD = 4294967295
D2D1_TURBULENCE_NOISE = UInt32
D2D1_TURBULENCE_NOISE_FRACTAL_SUM = 0
D2D1_TURBULENCE_NOISE_TURBULENCE = 1
D2D1_TURBULENCE_NOISE_FORCE_DWORD = 4294967295
D2D1_COMPOSITE_MODE = UInt32
D2D1_COMPOSITE_MODE_SOURCE_OVER = 0
D2D1_COMPOSITE_MODE_DESTINATION_OVER = 1
D2D1_COMPOSITE_MODE_SOURCE_IN = 2
D2D1_COMPOSITE_MODE_DESTINATION_IN = 3
D2D1_COMPOSITE_MODE_SOURCE_OUT = 4
D2D1_COMPOSITE_MODE_DESTINATION_OUT = 5
D2D1_COMPOSITE_MODE_SOURCE_ATOP = 6
D2D1_COMPOSITE_MODE_DESTINATION_ATOP = 7
D2D1_COMPOSITE_MODE_XOR = 8
D2D1_COMPOSITE_MODE_PLUS = 9
D2D1_COMPOSITE_MODE_SOURCE_COPY = 10
D2D1_COMPOSITE_MODE_BOUNDED_SOURCE_COPY = 11
D2D1_COMPOSITE_MODE_MASK_INVERT = 12
D2D1_COMPOSITE_MODE_FORCE_DWORD = 4294967295
__all__ = [
    "D2D_COLOR_F",
    "D2D1_COLOR_F",
    "D2D1_ALPHA_MODE",
    "D2D1_ALPHA_MODE_UNKNOWN",
    "D2D1_ALPHA_MODE_PREMULTIPLIED",
    "D2D1_ALPHA_MODE_STRAIGHT",
    "D2D1_ALPHA_MODE_IGNORE",
    "D2D1_ALPHA_MODE_FORCE_DWORD",
    "D2D1_PIXEL_FORMAT",
    "D2D_POINT_2U",
    "D2D_POINT_2F",
    "D2D_VECTOR_2F",
    "D2D_VECTOR_3F",
    "D2D_VECTOR_4F",
    "D2D_RECT_F",
    "D2D_RECT_U",
    "D2D_SIZE_F",
    "D2D_SIZE_U",
    "D2D_MATRIX_3X2_F",
    "D2D_MATRIX_4X3_F",
    "D2D_MATRIX_4X4_F",
    "D2D_MATRIX_5X4_F",
    "D2D1_FIGURE_BEGIN",
    "D2D1_FIGURE_BEGIN_FILLED",
    "D2D1_FIGURE_BEGIN_HOLLOW",
    "D2D1_FIGURE_BEGIN_FORCE_DWORD",
    "D2D1_FIGURE_END",
    "D2D1_FIGURE_END_OPEN",
    "D2D1_FIGURE_END_CLOSED",
    "D2D1_FIGURE_END_FORCE_DWORD",
    "D2D1_BEZIER_SEGMENT",
    "D2D1_PATH_SEGMENT",
    "D2D1_PATH_SEGMENT_NONE",
    "D2D1_PATH_SEGMENT_FORCE_UNSTROKED",
    "D2D1_PATH_SEGMENT_FORCE_ROUND_LINE_JOIN",
    "D2D1_PATH_SEGMENT_FORCE_DWORD",
    "D2D1_FILL_MODE",
    "D2D1_FILL_MODE_ALTERNATE",
    "D2D1_FILL_MODE_WINDING",
    "D2D1_FILL_MODE_FORCE_DWORD",
    "ID2D1SimplifiedGeometrySink",
    "D2D1_BORDER_MODE",
    "D2D1_BORDER_MODE_SOFT",
    "D2D1_BORDER_MODE_HARD",
    "D2D1_BORDER_MODE_FORCE_DWORD",
    "D2D1_BLEND_MODE",
    "D2D1_BLEND_MODE_MULTIPLY",
    "D2D1_BLEND_MODE_SCREEN",
    "D2D1_BLEND_MODE_DARKEN",
    "D2D1_BLEND_MODE_LIGHTEN",
    "D2D1_BLEND_MODE_DISSOLVE",
    "D2D1_BLEND_MODE_COLOR_BURN",
    "D2D1_BLEND_MODE_LINEAR_BURN",
    "D2D1_BLEND_MODE_DARKER_COLOR",
    "D2D1_BLEND_MODE_LIGHTER_COLOR",
    "D2D1_BLEND_MODE_COLOR_DODGE",
    "D2D1_BLEND_MODE_LINEAR_DODGE",
    "D2D1_BLEND_MODE_OVERLAY",
    "D2D1_BLEND_MODE_SOFT_LIGHT",
    "D2D1_BLEND_MODE_HARD_LIGHT",
    "D2D1_BLEND_MODE_VIVID_LIGHT",
    "D2D1_BLEND_MODE_LINEAR_LIGHT",
    "D2D1_BLEND_MODE_PIN_LIGHT",
    "D2D1_BLEND_MODE_HARD_MIX",
    "D2D1_BLEND_MODE_DIFFERENCE",
    "D2D1_BLEND_MODE_EXCLUSION",
    "D2D1_BLEND_MODE_HUE",
    "D2D1_BLEND_MODE_SATURATION",
    "D2D1_BLEND_MODE_COLOR",
    "D2D1_BLEND_MODE_LUMINOSITY",
    "D2D1_BLEND_MODE_SUBTRACT",
    "D2D1_BLEND_MODE_DIVISION",
    "D2D1_BLEND_MODE_FORCE_DWORD",
    "D2D1_COLORMATRIX_ALPHA_MODE",
    "D2D1_COLORMATRIX_ALPHA_MODE_PREMULTIPLIED",
    "D2D1_COLORMATRIX_ALPHA_MODE_STRAIGHT",
    "D2D1_COLORMATRIX_ALPHA_MODE_FORCE_DWORD",
    "D2D1_TURBULENCE_NOISE",
    "D2D1_TURBULENCE_NOISE_FRACTAL_SUM",
    "D2D1_TURBULENCE_NOISE_TURBULENCE",
    "D2D1_TURBULENCE_NOISE_FORCE_DWORD",
    "D2D1_COMPOSITE_MODE",
    "D2D1_COMPOSITE_MODE_SOURCE_OVER",
    "D2D1_COMPOSITE_MODE_DESTINATION_OVER",
    "D2D1_COMPOSITE_MODE_SOURCE_IN",
    "D2D1_COMPOSITE_MODE_DESTINATION_IN",
    "D2D1_COMPOSITE_MODE_SOURCE_OUT",
    "D2D1_COMPOSITE_MODE_DESTINATION_OUT",
    "D2D1_COMPOSITE_MODE_SOURCE_ATOP",
    "D2D1_COMPOSITE_MODE_DESTINATION_ATOP",
    "D2D1_COMPOSITE_MODE_XOR",
    "D2D1_COMPOSITE_MODE_PLUS",
    "D2D1_COMPOSITE_MODE_SOURCE_COPY",
    "D2D1_COMPOSITE_MODE_BOUNDED_SOURCE_COPY",
    "D2D1_COMPOSITE_MODE_MASK_INVERT",
    "D2D1_COMPOSITE_MODE_FORCE_DWORD",
]
