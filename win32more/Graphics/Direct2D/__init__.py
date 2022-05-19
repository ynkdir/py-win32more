from win32more import *
import win32more.Foundation
import win32more.Graphics.Direct2D
import win32more.Graphics.Direct2D.Common
import win32more.Graphics.Direct3D
import win32more.Graphics.DirectWrite
import win32more.Graphics.Dxgi
import win32more.Graphics.Dxgi.Common
import win32more.Graphics.Gdi
import win32more.Graphics.Imaging
import win32more.Storage.Xps.Printing
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
D2D1_DEFAULT_FLATTENING_TOLERANCE = 0.25
CLSID_D2D12DAffineTransform = '6aa97485-6354-4cfc-908c-e4a74f62c96c'
CLSID_D2D13DPerspectiveTransform = 'c2844d0b-3d86-46e7-85ba-526c9240f3fb'
CLSID_D2D13DTransform = 'e8467b04-ec61-4b8a-b5de-d4d73debea5a'
CLSID_D2D1ArithmeticComposite = 'fc151437-049a-4784-a24a-f1c4daf20987'
CLSID_D2D1Atlas = '913e2be4-fdcf-4fe2-a5f0-2454f14ff408'
CLSID_D2D1BitmapSource = '5fb6c24d-c6dd-4231-9404-50f4d5c3252d'
CLSID_D2D1Blend = '81c5b77b-13f8-4cdd-ad20-c890547ac65d'
CLSID_D2D1Border = '2a2d49c0-4acf-43c7-8c6a-7c4a27874d27'
CLSID_D2D1Brightness = '8cea8d1e-77b0-4986-b3b9-2f0c0eae7887'
CLSID_D2D1ColorManagement = '1a28524c-fdd6-4aa4-ae8f-837eb8267b37'
CLSID_D2D1ColorMatrix = '921f03d6-641c-47df-852d-b4bb6153ae11'
CLSID_D2D1Composite = '48fc9f51-f6ac-48f1-8b58-3b28ac46f76d'
CLSID_D2D1ConvolveMatrix = '407f8c08-5533-4331-a341-23cc3877843e'
CLSID_D2D1Crop = 'e23f7110-0e9a-4324-af47-6a2c0c46f35b'
CLSID_D2D1DirectionalBlur = '174319a6-58e9-49b2-bb63-caf2c811a3db'
CLSID_D2D1DiscreteTransfer = '90866fcd-488e-454b-af06-e5041b66c36c'
CLSID_D2D1DisplacementMap = 'edc48364-0417-4111-9450-43845fa9f890'
CLSID_D2D1DistantDiffuse = '3e7efd62-a32d-46d4-a83c-5278889ac954'
CLSID_D2D1DistantSpecular = '428c1ee5-77b8-4450-8ab5-72219c21abda'
CLSID_D2D1DpiCompensation = '6c26c5c7-34e0-46fc-9cfd-e5823706e228'
CLSID_D2D1Flood = '61c23c20-ae69-4d8e-94cf-50078df638f2'
CLSID_D2D1GammaTransfer = '409444c4-c419-41a0-b0c1-8cd0c0a18e42'
CLSID_D2D1GaussianBlur = '1feb6d69-2fe6-4ac9-8c58-1d7f93e7a6a5'
CLSID_D2D1Scale = '9daf9369-3846-4d0e-a44e-0c607934a5d7'
CLSID_D2D1Histogram = '881db7d0-f7ee-4d4d-a6d2-4697acc66ee8'
CLSID_D2D1HueRotation = '0f4458ec-4b32-491b-9e85-bd73f44d3eb6'
CLSID_D2D1LinearTransfer = 'ad47c8fd-63ef-4acc-9b51-67979c036c06'
CLSID_D2D1LuminanceToAlpha = '41251ab7-0beb-46f8-9da7-59e93fcce5de'
CLSID_D2D1Morphology = 'eae6c40d-626a-4c2d-bfcb-391001abe202'
CLSID_D2D1OpacityMetadata = '6c53006a-4450-4199-aa5b-ad1656fece5e'
CLSID_D2D1PointDiffuse = 'b9e303c3-c08c-4f91-8b7b-38656bc48c20'
CLSID_D2D1PointSpecular = '09c3ca26-3ae2-4f09-9ebc-ed3865d53f22'
CLSID_D2D1Premultiply = '06eab419-deed-4018-80d2-3e1d471adeb2'
CLSID_D2D1Saturation = '5cb2d9cf-327d-459f-a0ce-40c0b2086bf7'
CLSID_D2D1Shadow = 'c67ea361-1863-4e69-89db-695d3e9a5b6b'
CLSID_D2D1SpotDiffuse = '818a1105-7932-44f4-aa86-08ae7b2f2c93'
CLSID_D2D1SpotSpecular = 'edae421e-7654-4a37-9db8-71acc1beb3c1'
CLSID_D2D1TableTransfer = '5bf818c3-5e43-48cb-b631-868396d6a1d4'
CLSID_D2D1Tile = 'b0784138-3b76-4bc5-b13b-0fa2ad02659f'
CLSID_D2D1Turbulence = 'cf2bb6ae-889a-4ad7-ba29-a2fd732c9fc9'
CLSID_D2D1UnPremultiply = 'fb9ac489-ad8d-41ed-9999-bb6347d110f7'
CLSID_D2D1YCbCr = '99503cc1-66c7-45c9-a875-8ad8a7914401'
CLSID_D2D1Contrast = 'b648a78a-0ed5-4f80-a94a-8e825aca6b77'
CLSID_D2D1RgbToHue = '23f3e5ec-91e8-4d3d-ad0a-afadc1004aa1'
CLSID_D2D1HueToRgb = '7b78a6bd-0141-4def-8a52-6356ee0cbdd5'
CLSID_D2D1ChromaKey = '74c01f5b-2a0d-408c-88e2-c7a3c7197742'
CLSID_D2D1Emboss = 'b1c5eb2b-0348-43f0-8107-4957cacba2ae'
CLSID_D2D1Exposure = 'b56c8cfa-f634-41ee-bee0-ffa617106004'
CLSID_D2D1Grayscale = '36dde0eb-3725-42e0-836d-52fb20aee644'
CLSID_D2D1Invert = 'e0c3784d-cb39-4e84-b6fd-6b72f0810263'
CLSID_D2D1Posterize = '2188945e-33a3-4366-b7bc-086bd02d0884'
CLSID_D2D1Sepia = '3a1af410-5f1d-4dbe-84df-915da79b7153'
CLSID_D2D1Sharpen = 'c9b887cb-c5ff-4dc5-9779-273dcf417c7d'
CLSID_D2D1Straighten = '4da47b12-79a3-4fb0-8237-bbc3b2a4de08'
CLSID_D2D1TemperatureTint = '89176087-8af9-4a08-aeb1-895f38db1766'
CLSID_D2D1Vignette = 'c00c40be-5e67-4ca3-95b4-f4b02c115135'
CLSID_D2D1EdgeDetection = 'eff583ca-cb07-4aa9-ac5d-2cc44c76460f'
CLSID_D2D1HighlightsShadows = 'cadc8384-323f-4c7e-a361-2e2b24df6ee4'
CLSID_D2D1LookupTable3D = '349e0eda-0088-4a79-9ca3-c7e300202020'
CLSID_D2D1Opacity = '811d79a4-de28-4454-8094-c64685f8bd4c'
CLSID_D2D1AlphaMask = 'c80ecff0-3fd5-4f05-8328-c5d1724b4f0a'
CLSID_D2D1CrossFade = '12f575e8-4db1-485f-9a84-03a07dd3829f'
CLSID_D2D1Tint = '36312b17-f7dd-4014-915d-ffca768cf211'
D2D1_SCENE_REFERRED_SDR_WHITE_LEVEL = 80
CLSID_D2D1WhiteLevelAdjustment = '44a1cadb-6cdd-4818-8ff4-26c1cfe95bdb'
CLSID_D2D1HdrToneMap = '7b0b748d-4610-4486-a90c-999d9a2e2b11'
D2D1_APPEND_ALIGNED_ELEMENT = 4294967295
FACILITY_D2D = 2201
D2D1_INTERPOLATION_MODE_DEFINITION = Int32
D2D1_INTERPOLATION_MODE_DEFINITION_NEAREST_NEIGHBOR = 0
D2D1_INTERPOLATION_MODE_DEFINITION_LINEAR = 1
D2D1_INTERPOLATION_MODE_DEFINITION_CUBIC = 2
D2D1_INTERPOLATION_MODE_DEFINITION_MULTI_SAMPLE_LINEAR = 3
D2D1_INTERPOLATION_MODE_DEFINITION_ANISOTROPIC = 4
D2D1_INTERPOLATION_MODE_DEFINITION_HIGH_QUALITY_CUBIC = 5
D2D1_INTERPOLATION_MODE_DEFINITION_FANT = 6
D2D1_INTERPOLATION_MODE_DEFINITION_MIPMAP_LINEAR = 7
D2D1_GAMMA = UInt32
D2D1_GAMMA_2_2 = 0
D2D1_GAMMA_1_0 = 1
D2D1_GAMMA_FORCE_DWORD = 4294967295
D2D1_OPACITY_MASK_CONTENT = UInt32
D2D1_OPACITY_MASK_CONTENT_GRAPHICS = 0
D2D1_OPACITY_MASK_CONTENT_TEXT_NATURAL = 1
D2D1_OPACITY_MASK_CONTENT_TEXT_GDI_COMPATIBLE = 2
D2D1_OPACITY_MASK_CONTENT_FORCE_DWORD = 4294967295
D2D1_EXTEND_MODE = UInt32
D2D1_EXTEND_MODE_CLAMP = 0
D2D1_EXTEND_MODE_WRAP = 1
D2D1_EXTEND_MODE_MIRROR = 2
D2D1_EXTEND_MODE_FORCE_DWORD = 4294967295
D2D1_ANTIALIAS_MODE = UInt32
D2D1_ANTIALIAS_MODE_PER_PRIMITIVE = 0
D2D1_ANTIALIAS_MODE_ALIASED = 1
D2D1_ANTIALIAS_MODE_FORCE_DWORD = 4294967295
D2D1_TEXT_ANTIALIAS_MODE = UInt32
D2D1_TEXT_ANTIALIAS_MODE_DEFAULT = 0
D2D1_TEXT_ANTIALIAS_MODE_CLEARTYPE = 1
D2D1_TEXT_ANTIALIAS_MODE_GRAYSCALE = 2
D2D1_TEXT_ANTIALIAS_MODE_ALIASED = 3
D2D1_TEXT_ANTIALIAS_MODE_FORCE_DWORD = 4294967295
D2D1_BITMAP_INTERPOLATION_MODE = UInt32
D2D1_BITMAP_INTERPOLATION_MODE_NEAREST_NEIGHBOR = 0
D2D1_BITMAP_INTERPOLATION_MODE_LINEAR = 1
D2D1_BITMAP_INTERPOLATION_MODE_FORCE_DWORD = 4294967295
D2D1_DRAW_TEXT_OPTIONS = UInt32
D2D1_DRAW_TEXT_OPTIONS_NO_SNAP = 1
D2D1_DRAW_TEXT_OPTIONS_CLIP = 2
D2D1_DRAW_TEXT_OPTIONS_ENABLE_COLOR_FONT = 4
D2D1_DRAW_TEXT_OPTIONS_DISABLE_COLOR_BITMAP_SNAPPING = 8
D2D1_DRAW_TEXT_OPTIONS_NONE = 0
D2D1_DRAW_TEXT_OPTIONS_FORCE_DWORD = 4294967295
def _define_D2D1_BITMAP_PROPERTIES_head():
    class D2D1_BITMAP_PROPERTIES(Structure):
        pass
    return D2D1_BITMAP_PROPERTIES
def _define_D2D1_BITMAP_PROPERTIES():
    D2D1_BITMAP_PROPERTIES = win32more.Graphics.Direct2D.D2D1_BITMAP_PROPERTIES_head
    D2D1_BITMAP_PROPERTIES._fields_ = [
        ("pixelFormat", win32more.Graphics.Direct2D.Common.D2D1_PIXEL_FORMAT),
        ("dpiX", Single),
        ("dpiY", Single),
    ]
    return D2D1_BITMAP_PROPERTIES
def _define_D2D1_GRADIENT_STOP_head():
    class D2D1_GRADIENT_STOP(Structure):
        pass
    return D2D1_GRADIENT_STOP
def _define_D2D1_GRADIENT_STOP():
    D2D1_GRADIENT_STOP = win32more.Graphics.Direct2D.D2D1_GRADIENT_STOP_head
    D2D1_GRADIENT_STOP._fields_ = [
        ("position", Single),
        ("color", win32more.Graphics.Direct2D.Common.D2D1_COLOR_F),
    ]
    return D2D1_GRADIENT_STOP
def _define_D2D1_BRUSH_PROPERTIES_head():
    class D2D1_BRUSH_PROPERTIES(Structure):
        pass
    return D2D1_BRUSH_PROPERTIES
def _define_D2D1_BRUSH_PROPERTIES():
    D2D1_BRUSH_PROPERTIES = win32more.Graphics.Direct2D.D2D1_BRUSH_PROPERTIES_head
    D2D1_BRUSH_PROPERTIES._fields_ = [
        ("opacity", Single),
        ("transform", win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F),
    ]
    return D2D1_BRUSH_PROPERTIES
def _define_D2D1_BITMAP_BRUSH_PROPERTIES_head():
    class D2D1_BITMAP_BRUSH_PROPERTIES(Structure):
        pass
    return D2D1_BITMAP_BRUSH_PROPERTIES
def _define_D2D1_BITMAP_BRUSH_PROPERTIES():
    D2D1_BITMAP_BRUSH_PROPERTIES = win32more.Graphics.Direct2D.D2D1_BITMAP_BRUSH_PROPERTIES_head
    D2D1_BITMAP_BRUSH_PROPERTIES._fields_ = [
        ("extendModeX", win32more.Graphics.Direct2D.D2D1_EXTEND_MODE),
        ("extendModeY", win32more.Graphics.Direct2D.D2D1_EXTEND_MODE),
        ("interpolationMode", win32more.Graphics.Direct2D.D2D1_BITMAP_INTERPOLATION_MODE),
    ]
    return D2D1_BITMAP_BRUSH_PROPERTIES
def _define_D2D1_LINEAR_GRADIENT_BRUSH_PROPERTIES_head():
    class D2D1_LINEAR_GRADIENT_BRUSH_PROPERTIES(Structure):
        pass
    return D2D1_LINEAR_GRADIENT_BRUSH_PROPERTIES
def _define_D2D1_LINEAR_GRADIENT_BRUSH_PROPERTIES():
    D2D1_LINEAR_GRADIENT_BRUSH_PROPERTIES = win32more.Graphics.Direct2D.D2D1_LINEAR_GRADIENT_BRUSH_PROPERTIES_head
    D2D1_LINEAR_GRADIENT_BRUSH_PROPERTIES._fields_ = [
        ("startPoint", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("endPoint", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
    ]
    return D2D1_LINEAR_GRADIENT_BRUSH_PROPERTIES
def _define_D2D1_RADIAL_GRADIENT_BRUSH_PROPERTIES_head():
    class D2D1_RADIAL_GRADIENT_BRUSH_PROPERTIES(Structure):
        pass
    return D2D1_RADIAL_GRADIENT_BRUSH_PROPERTIES
def _define_D2D1_RADIAL_GRADIENT_BRUSH_PROPERTIES():
    D2D1_RADIAL_GRADIENT_BRUSH_PROPERTIES = win32more.Graphics.Direct2D.D2D1_RADIAL_GRADIENT_BRUSH_PROPERTIES_head
    D2D1_RADIAL_GRADIENT_BRUSH_PROPERTIES._fields_ = [
        ("center", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("gradientOriginOffset", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("radiusX", Single),
        ("radiusY", Single),
    ]
    return D2D1_RADIAL_GRADIENT_BRUSH_PROPERTIES
D2D1_ARC_SIZE = UInt32
D2D1_ARC_SIZE_SMALL = 0
D2D1_ARC_SIZE_LARGE = 1
D2D1_ARC_SIZE_FORCE_DWORD = 4294967295
D2D1_CAP_STYLE = UInt32
D2D1_CAP_STYLE_FLAT = 0
D2D1_CAP_STYLE_SQUARE = 1
D2D1_CAP_STYLE_ROUND = 2
D2D1_CAP_STYLE_TRIANGLE = 3
D2D1_CAP_STYLE_FORCE_DWORD = 4294967295
D2D1_DASH_STYLE = UInt32
D2D1_DASH_STYLE_SOLID = 0
D2D1_DASH_STYLE_DASH = 1
D2D1_DASH_STYLE_DOT = 2
D2D1_DASH_STYLE_DASH_DOT = 3
D2D1_DASH_STYLE_DASH_DOT_DOT = 4
D2D1_DASH_STYLE_CUSTOM = 5
D2D1_DASH_STYLE_FORCE_DWORD = 4294967295
D2D1_LINE_JOIN = UInt32
D2D1_LINE_JOIN_MITER = 0
D2D1_LINE_JOIN_BEVEL = 1
D2D1_LINE_JOIN_ROUND = 2
D2D1_LINE_JOIN_MITER_OR_BEVEL = 3
D2D1_LINE_JOIN_FORCE_DWORD = 4294967295
D2D1_COMBINE_MODE = UInt32
D2D1_COMBINE_MODE_UNION = 0
D2D1_COMBINE_MODE_INTERSECT = 1
D2D1_COMBINE_MODE_XOR = 2
D2D1_COMBINE_MODE_EXCLUDE = 3
D2D1_COMBINE_MODE_FORCE_DWORD = 4294967295
D2D1_GEOMETRY_RELATION = UInt32
D2D1_GEOMETRY_RELATION_UNKNOWN = 0
D2D1_GEOMETRY_RELATION_DISJOINT = 1
D2D1_GEOMETRY_RELATION_IS_CONTAINED = 2
D2D1_GEOMETRY_RELATION_CONTAINS = 3
D2D1_GEOMETRY_RELATION_OVERLAP = 4
D2D1_GEOMETRY_RELATION_FORCE_DWORD = 4294967295
D2D1_GEOMETRY_SIMPLIFICATION_OPTION = UInt32
D2D1_GEOMETRY_SIMPLIFICATION_OPTION_CUBICS_AND_LINES = 0
D2D1_GEOMETRY_SIMPLIFICATION_OPTION_LINES = 1
D2D1_GEOMETRY_SIMPLIFICATION_OPTION_FORCE_DWORD = 4294967295
def _define_D2D1_TRIANGLE_head():
    class D2D1_TRIANGLE(Structure):
        pass
    return D2D1_TRIANGLE
def _define_D2D1_TRIANGLE():
    D2D1_TRIANGLE = win32more.Graphics.Direct2D.D2D1_TRIANGLE_head
    D2D1_TRIANGLE._fields_ = [
        ("point1", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("point2", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("point3", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
    ]
    return D2D1_TRIANGLE
D2D1_SWEEP_DIRECTION = UInt32
D2D1_SWEEP_DIRECTION_COUNTER_CLOCKWISE = 0
D2D1_SWEEP_DIRECTION_CLOCKWISE = 1
D2D1_SWEEP_DIRECTION_FORCE_DWORD = 4294967295
def _define_D2D1_ARC_SEGMENT_head():
    class D2D1_ARC_SEGMENT(Structure):
        pass
    return D2D1_ARC_SEGMENT
def _define_D2D1_ARC_SEGMENT():
    D2D1_ARC_SEGMENT = win32more.Graphics.Direct2D.D2D1_ARC_SEGMENT_head
    D2D1_ARC_SEGMENT._fields_ = [
        ("point", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("size", win32more.Graphics.Direct2D.Common.D2D_SIZE_F),
        ("rotationAngle", Single),
        ("sweepDirection", win32more.Graphics.Direct2D.D2D1_SWEEP_DIRECTION),
        ("arcSize", win32more.Graphics.Direct2D.D2D1_ARC_SIZE),
    ]
    return D2D1_ARC_SEGMENT
def _define_D2D1_QUADRATIC_BEZIER_SEGMENT_head():
    class D2D1_QUADRATIC_BEZIER_SEGMENT(Structure):
        pass
    return D2D1_QUADRATIC_BEZIER_SEGMENT
def _define_D2D1_QUADRATIC_BEZIER_SEGMENT():
    D2D1_QUADRATIC_BEZIER_SEGMENT = win32more.Graphics.Direct2D.D2D1_QUADRATIC_BEZIER_SEGMENT_head
    D2D1_QUADRATIC_BEZIER_SEGMENT._fields_ = [
        ("point1", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("point2", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
    ]
    return D2D1_QUADRATIC_BEZIER_SEGMENT
def _define_D2D1_ELLIPSE_head():
    class D2D1_ELLIPSE(Structure):
        pass
    return D2D1_ELLIPSE
def _define_D2D1_ELLIPSE():
    D2D1_ELLIPSE = win32more.Graphics.Direct2D.D2D1_ELLIPSE_head
    D2D1_ELLIPSE._fields_ = [
        ("point", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("radiusX", Single),
        ("radiusY", Single),
    ]
    return D2D1_ELLIPSE
def _define_D2D1_ROUNDED_RECT_head():
    class D2D1_ROUNDED_RECT(Structure):
        pass
    return D2D1_ROUNDED_RECT
def _define_D2D1_ROUNDED_RECT():
    D2D1_ROUNDED_RECT = win32more.Graphics.Direct2D.D2D1_ROUNDED_RECT_head
    D2D1_ROUNDED_RECT._fields_ = [
        ("rect", win32more.Graphics.Direct2D.Common.D2D_RECT_F),
        ("radiusX", Single),
        ("radiusY", Single),
    ]
    return D2D1_ROUNDED_RECT
def _define_D2D1_STROKE_STYLE_PROPERTIES_head():
    class D2D1_STROKE_STYLE_PROPERTIES(Structure):
        pass
    return D2D1_STROKE_STYLE_PROPERTIES
def _define_D2D1_STROKE_STYLE_PROPERTIES():
    D2D1_STROKE_STYLE_PROPERTIES = win32more.Graphics.Direct2D.D2D1_STROKE_STYLE_PROPERTIES_head
    D2D1_STROKE_STYLE_PROPERTIES._fields_ = [
        ("startCap", win32more.Graphics.Direct2D.D2D1_CAP_STYLE),
        ("endCap", win32more.Graphics.Direct2D.D2D1_CAP_STYLE),
        ("dashCap", win32more.Graphics.Direct2D.D2D1_CAP_STYLE),
        ("lineJoin", win32more.Graphics.Direct2D.D2D1_LINE_JOIN),
        ("miterLimit", Single),
        ("dashStyle", win32more.Graphics.Direct2D.D2D1_DASH_STYLE),
        ("dashOffset", Single),
    ]
    return D2D1_STROKE_STYLE_PROPERTIES
D2D1_LAYER_OPTIONS = UInt32
D2D1_LAYER_OPTIONS_NONE = 0
D2D1_LAYER_OPTIONS_INITIALIZE_FOR_CLEARTYPE = 1
D2D1_LAYER_OPTIONS_FORCE_DWORD = 4294967295
def _define_D2D1_LAYER_PARAMETERS_head():
    class D2D1_LAYER_PARAMETERS(Structure):
        pass
    return D2D1_LAYER_PARAMETERS
def _define_D2D1_LAYER_PARAMETERS():
    D2D1_LAYER_PARAMETERS = win32more.Graphics.Direct2D.D2D1_LAYER_PARAMETERS_head
    D2D1_LAYER_PARAMETERS._fields_ = [
        ("contentBounds", win32more.Graphics.Direct2D.Common.D2D_RECT_F),
        ("geometricMask", win32more.Graphics.Direct2D.ID2D1Geometry_head),
        ("maskAntialiasMode", win32more.Graphics.Direct2D.D2D1_ANTIALIAS_MODE),
        ("maskTransform", win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F),
        ("opacity", Single),
        ("opacityBrush", win32more.Graphics.Direct2D.ID2D1Brush_head),
        ("layerOptions", win32more.Graphics.Direct2D.D2D1_LAYER_OPTIONS),
    ]
    return D2D1_LAYER_PARAMETERS
D2D1_WINDOW_STATE = UInt32
D2D1_WINDOW_STATE_NONE = 0
D2D1_WINDOW_STATE_OCCLUDED = 1
D2D1_WINDOW_STATE_FORCE_DWORD = 4294967295
D2D1_RENDER_TARGET_TYPE = UInt32
D2D1_RENDER_TARGET_TYPE_DEFAULT = 0
D2D1_RENDER_TARGET_TYPE_SOFTWARE = 1
D2D1_RENDER_TARGET_TYPE_HARDWARE = 2
D2D1_RENDER_TARGET_TYPE_FORCE_DWORD = 4294967295
D2D1_FEATURE_LEVEL = UInt32
D2D1_FEATURE_LEVEL_DEFAULT = 0
D2D1_FEATURE_LEVEL_9 = 37120
D2D1_FEATURE_LEVEL_10 = 40960
D2D1_FEATURE_LEVEL_FORCE_DWORD = 4294967295
D2D1_RENDER_TARGET_USAGE = UInt32
D2D1_RENDER_TARGET_USAGE_NONE = 0
D2D1_RENDER_TARGET_USAGE_FORCE_BITMAP_REMOTING = 1
D2D1_RENDER_TARGET_USAGE_GDI_COMPATIBLE = 2
D2D1_RENDER_TARGET_USAGE_FORCE_DWORD = 4294967295
D2D1_PRESENT_OPTIONS = UInt32
D2D1_PRESENT_OPTIONS_NONE = 0
D2D1_PRESENT_OPTIONS_RETAIN_CONTENTS = 1
D2D1_PRESENT_OPTIONS_IMMEDIATELY = 2
D2D1_PRESENT_OPTIONS_FORCE_DWORD = 4294967295
def _define_D2D1_RENDER_TARGET_PROPERTIES_head():
    class D2D1_RENDER_TARGET_PROPERTIES(Structure):
        pass
    return D2D1_RENDER_TARGET_PROPERTIES
def _define_D2D1_RENDER_TARGET_PROPERTIES():
    D2D1_RENDER_TARGET_PROPERTIES = win32more.Graphics.Direct2D.D2D1_RENDER_TARGET_PROPERTIES_head
    D2D1_RENDER_TARGET_PROPERTIES._fields_ = [
        ("type", win32more.Graphics.Direct2D.D2D1_RENDER_TARGET_TYPE),
        ("pixelFormat", win32more.Graphics.Direct2D.Common.D2D1_PIXEL_FORMAT),
        ("dpiX", Single),
        ("dpiY", Single),
        ("usage", win32more.Graphics.Direct2D.D2D1_RENDER_TARGET_USAGE),
        ("minLevel", win32more.Graphics.Direct2D.D2D1_FEATURE_LEVEL),
    ]
    return D2D1_RENDER_TARGET_PROPERTIES
def _define_D2D1_HWND_RENDER_TARGET_PROPERTIES_head():
    class D2D1_HWND_RENDER_TARGET_PROPERTIES(Structure):
        pass
    return D2D1_HWND_RENDER_TARGET_PROPERTIES
def _define_D2D1_HWND_RENDER_TARGET_PROPERTIES():
    D2D1_HWND_RENDER_TARGET_PROPERTIES = win32more.Graphics.Direct2D.D2D1_HWND_RENDER_TARGET_PROPERTIES_head
    D2D1_HWND_RENDER_TARGET_PROPERTIES._fields_ = [
        ("hwnd", win32more.Foundation.HWND),
        ("pixelSize", win32more.Graphics.Direct2D.Common.D2D_SIZE_U),
        ("presentOptions", win32more.Graphics.Direct2D.D2D1_PRESENT_OPTIONS),
    ]
    return D2D1_HWND_RENDER_TARGET_PROPERTIES
D2D1_COMPATIBLE_RENDER_TARGET_OPTIONS = UInt32
D2D1_COMPATIBLE_RENDER_TARGET_OPTIONS_NONE = 0
D2D1_COMPATIBLE_RENDER_TARGET_OPTIONS_GDI_COMPATIBLE = 1
D2D1_COMPATIBLE_RENDER_TARGET_OPTIONS_FORCE_DWORD = 4294967295
def _define_D2D1_DRAWING_STATE_DESCRIPTION_head():
    class D2D1_DRAWING_STATE_DESCRIPTION(Structure):
        pass
    return D2D1_DRAWING_STATE_DESCRIPTION
def _define_D2D1_DRAWING_STATE_DESCRIPTION():
    D2D1_DRAWING_STATE_DESCRIPTION = win32more.Graphics.Direct2D.D2D1_DRAWING_STATE_DESCRIPTION_head
    D2D1_DRAWING_STATE_DESCRIPTION._fields_ = [
        ("antialiasMode", win32more.Graphics.Direct2D.D2D1_ANTIALIAS_MODE),
        ("textAntialiasMode", win32more.Graphics.Direct2D.D2D1_TEXT_ANTIALIAS_MODE),
        ("tag1", UInt64),
        ("tag2", UInt64),
        ("transform", win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F),
    ]
    return D2D1_DRAWING_STATE_DESCRIPTION
D2D1_DC_INITIALIZE_MODE = UInt32
D2D1_DC_INITIALIZE_MODE_COPY = 0
D2D1_DC_INITIALIZE_MODE_CLEAR = 1
D2D1_DC_INITIALIZE_MODE_FORCE_DWORD = 4294967295
D2D1_DEBUG_LEVEL = UInt32
D2D1_DEBUG_LEVEL_NONE = 0
D2D1_DEBUG_LEVEL_ERROR = 1
D2D1_DEBUG_LEVEL_WARNING = 2
D2D1_DEBUG_LEVEL_INFORMATION = 3
D2D1_DEBUG_LEVEL_FORCE_DWORD = 4294967295
D2D1_FACTORY_TYPE = UInt32
D2D1_FACTORY_TYPE_SINGLE_THREADED = 0
D2D1_FACTORY_TYPE_MULTI_THREADED = 1
D2D1_FACTORY_TYPE_FORCE_DWORD = 4294967295
def _define_D2D1_FACTORY_OPTIONS_head():
    class D2D1_FACTORY_OPTIONS(Structure):
        pass
    return D2D1_FACTORY_OPTIONS
def _define_D2D1_FACTORY_OPTIONS():
    D2D1_FACTORY_OPTIONS = win32more.Graphics.Direct2D.D2D1_FACTORY_OPTIONS_head
    D2D1_FACTORY_OPTIONS._fields_ = [
        ("debugLevel", win32more.Graphics.Direct2D.D2D1_DEBUG_LEVEL),
    ]
    return D2D1_FACTORY_OPTIONS
def _define_ID2D1Resource_head():
    class ID2D1Resource(win32more.System.Com.IUnknown_head):
        Guid = Guid('2cd90691-12e2-11dc-9fed-001143a055f9')
    return ID2D1Resource
def _define_ID2D1Resource():
    ID2D1Resource = win32more.Graphics.Direct2D.ID2D1Resource_head
    ID2D1Resource.GetFactory = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.ID2D1Factory_head), use_last_error=False)(3, 'GetFactory', ((1, 'factory'),)))
    return ID2D1Resource
def _define_ID2D1Image_head():
    class ID2D1Image(win32more.Graphics.Direct2D.ID2D1Resource_head):
        Guid = Guid('65019f75-8da2-497c-b32c-dfa34e48ede6')
    return ID2D1Image
def _define_ID2D1Image():
    ID2D1Image = win32more.Graphics.Direct2D.ID2D1Image_head
    return ID2D1Image
def _define_ID2D1Bitmap_head():
    class ID2D1Bitmap(win32more.Graphics.Direct2D.ID2D1Image_head):
        Guid = Guid('a2296057-ea42-4099-983b-539fb6505426')
    return ID2D1Bitmap
def _define_ID2D1Bitmap():
    ID2D1Bitmap = win32more.Graphics.Direct2D.ID2D1Bitmap_head
    ID2D1Bitmap.GetSize = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.Common.D2D_SIZE_F, use_last_error=False)(4, 'GetSize', ()))
    ID2D1Bitmap.GetPixelSize = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.Common.D2D_SIZE_U, use_last_error=False)(5, 'GetPixelSize', ()))
    ID2D1Bitmap.GetPixelFormat = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.Common.D2D1_PIXEL_FORMAT, use_last_error=False)(6, 'GetPixelFormat', ()))
    ID2D1Bitmap.GetDpi = COMMETHOD(WINFUNCTYPE(Void,POINTER(Single),POINTER(Single), use_last_error=False)(7, 'GetDpi', ((1, 'dpiX'),(1, 'dpiY'),)))
    ID2D1Bitmap.CopyFromBitmap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2U_head),win32more.Graphics.Direct2D.ID2D1Bitmap_head,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_U_head), use_last_error=False)(8, 'CopyFromBitmap', ((1, 'destPoint'),(1, 'bitmap'),(1, 'srcRect'),)))
    ID2D1Bitmap.CopyFromRenderTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2U_head),win32more.Graphics.Direct2D.ID2D1RenderTarget_head,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_U_head), use_last_error=False)(9, 'CopyFromRenderTarget', ((1, 'destPoint'),(1, 'renderTarget'),(1, 'srcRect'),)))
    ID2D1Bitmap.CopyFromMemory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_U_head),c_void_p,UInt32, use_last_error=False)(10, 'CopyFromMemory', ((1, 'dstRect'),(1, 'srcData'),(1, 'pitch'),)))
    return ID2D1Bitmap
def _define_ID2D1GradientStopCollection_head():
    class ID2D1GradientStopCollection(win32more.Graphics.Direct2D.ID2D1Resource_head):
        Guid = Guid('2cd906a7-12e2-11dc-9fed-001143a055f9')
    return ID2D1GradientStopCollection
def _define_ID2D1GradientStopCollection():
    ID2D1GradientStopCollection = win32more.Graphics.Direct2D.ID2D1GradientStopCollection_head
    ID2D1GradientStopCollection.GetGradientStopCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(4, 'GetGradientStopCount', ()))
    ID2D1GradientStopCollection.GetGradientStops = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.D2D1_GRADIENT_STOP),UInt32, use_last_error=False)(5, 'GetGradientStops', ((1, 'gradientStops'),(1, 'gradientStopsCount'),)))
    ID2D1GradientStopCollection.GetColorInterpolationGamma = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_GAMMA, use_last_error=False)(6, 'GetColorInterpolationGamma', ()))
    ID2D1GradientStopCollection.GetExtendMode = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_EXTEND_MODE, use_last_error=False)(7, 'GetExtendMode', ()))
    return ID2D1GradientStopCollection
def _define_ID2D1Brush_head():
    class ID2D1Brush(win32more.Graphics.Direct2D.ID2D1Resource_head):
        Guid = Guid('2cd906a8-12e2-11dc-9fed-001143a055f9')
    return ID2D1Brush
def _define_ID2D1Brush():
    ID2D1Brush = win32more.Graphics.Direct2D.ID2D1Brush_head
    ID2D1Brush.SetOpacity = COMMETHOD(WINFUNCTYPE(Void,Single, use_last_error=False)(4, 'SetOpacity', ((1, 'opacity'),)))
    ID2D1Brush.SetTransform = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head), use_last_error=False)(5, 'SetTransform', ((1, 'transform'),)))
    ID2D1Brush.GetOpacity = COMMETHOD(WINFUNCTYPE(Single, use_last_error=False)(6, 'GetOpacity', ()))
    ID2D1Brush.GetTransform = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head), use_last_error=False)(7, 'GetTransform', ((1, 'transform'),)))
    return ID2D1Brush
def _define_ID2D1BitmapBrush_head():
    class ID2D1BitmapBrush(win32more.Graphics.Direct2D.ID2D1Brush_head):
        Guid = Guid('2cd906aa-12e2-11dc-9fed-001143a055f9')
    return ID2D1BitmapBrush
def _define_ID2D1BitmapBrush():
    ID2D1BitmapBrush = win32more.Graphics.Direct2D.ID2D1BitmapBrush_head
    ID2D1BitmapBrush.SetExtendModeX = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.D2D1_EXTEND_MODE, use_last_error=False)(8, 'SetExtendModeX', ((1, 'extendModeX'),)))
    ID2D1BitmapBrush.SetExtendModeY = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.D2D1_EXTEND_MODE, use_last_error=False)(9, 'SetExtendModeY', ((1, 'extendModeY'),)))
    ID2D1BitmapBrush.SetInterpolationMode = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.D2D1_BITMAP_INTERPOLATION_MODE, use_last_error=False)(10, 'SetInterpolationMode', ((1, 'interpolationMode'),)))
    ID2D1BitmapBrush.SetBitmap = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.ID2D1Bitmap_head, use_last_error=False)(11, 'SetBitmap', ((1, 'bitmap'),)))
    ID2D1BitmapBrush.GetExtendModeX = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_EXTEND_MODE, use_last_error=False)(12, 'GetExtendModeX', ()))
    ID2D1BitmapBrush.GetExtendModeY = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_EXTEND_MODE, use_last_error=False)(13, 'GetExtendModeY', ()))
    ID2D1BitmapBrush.GetInterpolationMode = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_BITMAP_INTERPOLATION_MODE, use_last_error=False)(14, 'GetInterpolationMode', ()))
    ID2D1BitmapBrush.GetBitmap = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.ID2D1Bitmap_head), use_last_error=False)(15, 'GetBitmap', ((1, 'bitmap'),)))
    return ID2D1BitmapBrush
def _define_ID2D1SolidColorBrush_head():
    class ID2D1SolidColorBrush(win32more.Graphics.Direct2D.ID2D1Brush_head):
        Guid = Guid('2cd906a9-12e2-11dc-9fed-001143a055f9')
    return ID2D1SolidColorBrush
def _define_ID2D1SolidColorBrush():
    ID2D1SolidColorBrush = win32more.Graphics.Direct2D.ID2D1SolidColorBrush_head
    ID2D1SolidColorBrush.SetColor = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.Common.D2D1_COLOR_F_head), use_last_error=False)(8, 'SetColor', ((1, 'color'),)))
    ID2D1SolidColorBrush.GetColor = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.Common.D2D1_COLOR_F, use_last_error=False)(9, 'GetColor', ()))
    return ID2D1SolidColorBrush
def _define_ID2D1LinearGradientBrush_head():
    class ID2D1LinearGradientBrush(win32more.Graphics.Direct2D.ID2D1Brush_head):
        Guid = Guid('2cd906ab-12e2-11dc-9fed-001143a055f9')
    return ID2D1LinearGradientBrush
def _define_ID2D1LinearGradientBrush():
    ID2D1LinearGradientBrush = win32more.Graphics.Direct2D.ID2D1LinearGradientBrush_head
    ID2D1LinearGradientBrush.SetStartPoint = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.Common.D2D_POINT_2F, use_last_error=False)(8, 'SetStartPoint', ((1, 'startPoint'),)))
    ID2D1LinearGradientBrush.SetEndPoint = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.Common.D2D_POINT_2F, use_last_error=False)(9, 'SetEndPoint', ((1, 'endPoint'),)))
    ID2D1LinearGradientBrush.GetStartPoint = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.Common.D2D_POINT_2F, use_last_error=False)(10, 'GetStartPoint', ()))
    ID2D1LinearGradientBrush.GetEndPoint = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.Common.D2D_POINT_2F, use_last_error=False)(11, 'GetEndPoint', ()))
    ID2D1LinearGradientBrush.GetGradientStopCollection = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.ID2D1GradientStopCollection_head), use_last_error=False)(12, 'GetGradientStopCollection', ((1, 'gradientStopCollection'),)))
    return ID2D1LinearGradientBrush
def _define_ID2D1RadialGradientBrush_head():
    class ID2D1RadialGradientBrush(win32more.Graphics.Direct2D.ID2D1Brush_head):
        Guid = Guid('2cd906ac-12e2-11dc-9fed-001143a055f9')
    return ID2D1RadialGradientBrush
def _define_ID2D1RadialGradientBrush():
    ID2D1RadialGradientBrush = win32more.Graphics.Direct2D.ID2D1RadialGradientBrush_head
    ID2D1RadialGradientBrush.SetCenter = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.Common.D2D_POINT_2F, use_last_error=False)(8, 'SetCenter', ((1, 'center'),)))
    ID2D1RadialGradientBrush.SetGradientOriginOffset = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.Common.D2D_POINT_2F, use_last_error=False)(9, 'SetGradientOriginOffset', ((1, 'gradientOriginOffset'),)))
    ID2D1RadialGradientBrush.SetRadiusX = COMMETHOD(WINFUNCTYPE(Void,Single, use_last_error=False)(10, 'SetRadiusX', ((1, 'radiusX'),)))
    ID2D1RadialGradientBrush.SetRadiusY = COMMETHOD(WINFUNCTYPE(Void,Single, use_last_error=False)(11, 'SetRadiusY', ((1, 'radiusY'),)))
    ID2D1RadialGradientBrush.GetCenter = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.Common.D2D_POINT_2F, use_last_error=False)(12, 'GetCenter', ()))
    ID2D1RadialGradientBrush.GetGradientOriginOffset = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.Common.D2D_POINT_2F, use_last_error=False)(13, 'GetGradientOriginOffset', ()))
    ID2D1RadialGradientBrush.GetRadiusX = COMMETHOD(WINFUNCTYPE(Single, use_last_error=False)(14, 'GetRadiusX', ()))
    ID2D1RadialGradientBrush.GetRadiusY = COMMETHOD(WINFUNCTYPE(Single, use_last_error=False)(15, 'GetRadiusY', ()))
    ID2D1RadialGradientBrush.GetGradientStopCollection = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.ID2D1GradientStopCollection_head), use_last_error=False)(16, 'GetGradientStopCollection', ((1, 'gradientStopCollection'),)))
    return ID2D1RadialGradientBrush
def _define_ID2D1StrokeStyle_head():
    class ID2D1StrokeStyle(win32more.Graphics.Direct2D.ID2D1Resource_head):
        Guid = Guid('2cd9069d-12e2-11dc-9fed-001143a055f9')
    return ID2D1StrokeStyle
def _define_ID2D1StrokeStyle():
    ID2D1StrokeStyle = win32more.Graphics.Direct2D.ID2D1StrokeStyle_head
    ID2D1StrokeStyle.GetStartCap = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_CAP_STYLE, use_last_error=False)(4, 'GetStartCap', ()))
    ID2D1StrokeStyle.GetEndCap = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_CAP_STYLE, use_last_error=False)(5, 'GetEndCap', ()))
    ID2D1StrokeStyle.GetDashCap = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_CAP_STYLE, use_last_error=False)(6, 'GetDashCap', ()))
    ID2D1StrokeStyle.GetMiterLimit = COMMETHOD(WINFUNCTYPE(Single, use_last_error=False)(7, 'GetMiterLimit', ()))
    ID2D1StrokeStyle.GetLineJoin = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_LINE_JOIN, use_last_error=False)(8, 'GetLineJoin', ()))
    ID2D1StrokeStyle.GetDashOffset = COMMETHOD(WINFUNCTYPE(Single, use_last_error=False)(9, 'GetDashOffset', ()))
    ID2D1StrokeStyle.GetDashStyle = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_DASH_STYLE, use_last_error=False)(10, 'GetDashStyle', ()))
    ID2D1StrokeStyle.GetDashesCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(11, 'GetDashesCount', ()))
    ID2D1StrokeStyle.GetDashes = COMMETHOD(WINFUNCTYPE(Void,POINTER(Single),UInt32, use_last_error=False)(12, 'GetDashes', ((1, 'dashes'),(1, 'dashesCount'),)))
    return ID2D1StrokeStyle
def _define_ID2D1Geometry_head():
    class ID2D1Geometry(win32more.Graphics.Direct2D.ID2D1Resource_head):
        Guid = Guid('2cd906a1-12e2-11dc-9fed-001143a055f9')
    return ID2D1Geometry
def _define_ID2D1Geometry():
    ID2D1Geometry = win32more.Graphics.Direct2D.ID2D1Geometry_head
    ID2D1Geometry.GetBounds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head), use_last_error=False)(4, 'GetBounds', ((1, 'worldTransform'),(1, 'bounds'),)))
    ID2D1Geometry.GetWidenedBounds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,win32more.Graphics.Direct2D.ID2D1StrokeStyle_head,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head),Single,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head), use_last_error=False)(5, 'GetWidenedBounds', ((1, 'strokeWidth'),(1, 'strokeStyle'),(1, 'worldTransform'),(1, 'flatteningTolerance'),(1, 'bounds'),)))
    ID2D1Geometry.StrokeContainsPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.Common.D2D_POINT_2F,Single,win32more.Graphics.Direct2D.ID2D1StrokeStyle_head,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head),Single,POINTER(win32more.Foundation.BOOL), use_last_error=False)(6, 'StrokeContainsPoint', ((1, 'point'),(1, 'strokeWidth'),(1, 'strokeStyle'),(1, 'worldTransform'),(1, 'flatteningTolerance'),(1, 'contains'),)))
    ID2D1Geometry.FillContainsPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.Common.D2D_POINT_2F,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head),Single,POINTER(win32more.Foundation.BOOL), use_last_error=False)(7, 'FillContainsPoint', ((1, 'point'),(1, 'worldTransform'),(1, 'flatteningTolerance'),(1, 'contains'),)))
    ID2D1Geometry.CompareWithGeometry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Geometry_head,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head),Single,POINTER(win32more.Graphics.Direct2D.D2D1_GEOMETRY_RELATION), use_last_error=False)(8, 'CompareWithGeometry', ((1, 'inputGeometry'),(1, 'inputGeometryTransform'),(1, 'flatteningTolerance'),(1, 'relation'),)))
    ID2D1Geometry.Simplify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.D2D1_GEOMETRY_SIMPLIFICATION_OPTION,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head),Single,win32more.Graphics.Direct2D.Common.ID2D1SimplifiedGeometrySink_head, use_last_error=False)(9, 'Simplify', ((1, 'simplificationOption'),(1, 'worldTransform'),(1, 'flatteningTolerance'),(1, 'geometrySink'),)))
    ID2D1Geometry.Tessellate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head),Single,win32more.Graphics.Direct2D.ID2D1TessellationSink_head, use_last_error=False)(10, 'Tessellate', ((1, 'worldTransform'),(1, 'flatteningTolerance'),(1, 'tessellationSink'),)))
    ID2D1Geometry.CombineWithGeometry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Geometry_head,win32more.Graphics.Direct2D.D2D1_COMBINE_MODE,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head),Single,win32more.Graphics.Direct2D.Common.ID2D1SimplifiedGeometrySink_head, use_last_error=False)(11, 'CombineWithGeometry', ((1, 'inputGeometry'),(1, 'combineMode'),(1, 'inputGeometryTransform'),(1, 'flatteningTolerance'),(1, 'geometrySink'),)))
    ID2D1Geometry.Outline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head),Single,win32more.Graphics.Direct2D.Common.ID2D1SimplifiedGeometrySink_head, use_last_error=False)(12, 'Outline', ((1, 'worldTransform'),(1, 'flatteningTolerance'),(1, 'geometrySink'),)))
    ID2D1Geometry.ComputeArea = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head),Single,POINTER(Single), use_last_error=False)(13, 'ComputeArea', ((1, 'worldTransform'),(1, 'flatteningTolerance'),(1, 'area'),)))
    ID2D1Geometry.ComputeLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head),Single,POINTER(Single), use_last_error=False)(14, 'ComputeLength', ((1, 'worldTransform'),(1, 'flatteningTolerance'),(1, 'length'),)))
    ID2D1Geometry.ComputePointAtLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head),Single,POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2F_head), use_last_error=False)(15, 'ComputePointAtLength', ((1, 'length'),(1, 'worldTransform'),(1, 'flatteningTolerance'),(1, 'point'),(1, 'unitTangentVector'),)))
    ID2D1Geometry.Widen = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,win32more.Graphics.Direct2D.ID2D1StrokeStyle_head,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head),Single,win32more.Graphics.Direct2D.Common.ID2D1SimplifiedGeometrySink_head, use_last_error=False)(16, 'Widen', ((1, 'strokeWidth'),(1, 'strokeStyle'),(1, 'worldTransform'),(1, 'flatteningTolerance'),(1, 'geometrySink'),)))
    return ID2D1Geometry
def _define_ID2D1RectangleGeometry_head():
    class ID2D1RectangleGeometry(win32more.Graphics.Direct2D.ID2D1Geometry_head):
        Guid = Guid('2cd906a2-12e2-11dc-9fed-001143a055f9')
    return ID2D1RectangleGeometry
def _define_ID2D1RectangleGeometry():
    ID2D1RectangleGeometry = win32more.Graphics.Direct2D.ID2D1RectangleGeometry_head
    ID2D1RectangleGeometry.GetRect = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head), use_last_error=False)(17, 'GetRect', ((1, 'rect'),)))
    return ID2D1RectangleGeometry
def _define_ID2D1RoundedRectangleGeometry_head():
    class ID2D1RoundedRectangleGeometry(win32more.Graphics.Direct2D.ID2D1Geometry_head):
        Guid = Guid('2cd906a3-12e2-11dc-9fed-001143a055f9')
    return ID2D1RoundedRectangleGeometry
def _define_ID2D1RoundedRectangleGeometry():
    ID2D1RoundedRectangleGeometry = win32more.Graphics.Direct2D.ID2D1RoundedRectangleGeometry_head
    ID2D1RoundedRectangleGeometry.GetRoundedRect = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.D2D1_ROUNDED_RECT_head), use_last_error=False)(17, 'GetRoundedRect', ((1, 'roundedRect'),)))
    return ID2D1RoundedRectangleGeometry
def _define_ID2D1EllipseGeometry_head():
    class ID2D1EllipseGeometry(win32more.Graphics.Direct2D.ID2D1Geometry_head):
        Guid = Guid('2cd906a4-12e2-11dc-9fed-001143a055f9')
    return ID2D1EllipseGeometry
def _define_ID2D1EllipseGeometry():
    ID2D1EllipseGeometry = win32more.Graphics.Direct2D.ID2D1EllipseGeometry_head
    ID2D1EllipseGeometry.GetEllipse = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.D2D1_ELLIPSE_head), use_last_error=False)(17, 'GetEllipse', ((1, 'ellipse'),)))
    return ID2D1EllipseGeometry
def _define_ID2D1GeometryGroup_head():
    class ID2D1GeometryGroup(win32more.Graphics.Direct2D.ID2D1Geometry_head):
        Guid = Guid('2cd906a6-12e2-11dc-9fed-001143a055f9')
    return ID2D1GeometryGroup
def _define_ID2D1GeometryGroup():
    ID2D1GeometryGroup = win32more.Graphics.Direct2D.ID2D1GeometryGroup_head
    ID2D1GeometryGroup.GetFillMode = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.Common.D2D1_FILL_MODE, use_last_error=False)(17, 'GetFillMode', ()))
    ID2D1GeometryGroup.GetSourceGeometryCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(18, 'GetSourceGeometryCount', ()))
    ID2D1GeometryGroup.GetSourceGeometries = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.ID2D1Geometry_head),UInt32, use_last_error=False)(19, 'GetSourceGeometries', ((1, 'geometries'),(1, 'geometriesCount'),)))
    return ID2D1GeometryGroup
def _define_ID2D1TransformedGeometry_head():
    class ID2D1TransformedGeometry(win32more.Graphics.Direct2D.ID2D1Geometry_head):
        Guid = Guid('2cd906bb-12e2-11dc-9fed-001143a055f9')
    return ID2D1TransformedGeometry
def _define_ID2D1TransformedGeometry():
    ID2D1TransformedGeometry = win32more.Graphics.Direct2D.ID2D1TransformedGeometry_head
    ID2D1TransformedGeometry.GetSourceGeometry = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.ID2D1Geometry_head), use_last_error=False)(17, 'GetSourceGeometry', ((1, 'sourceGeometry'),)))
    ID2D1TransformedGeometry.GetTransform = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head), use_last_error=False)(18, 'GetTransform', ((1, 'transform'),)))
    return ID2D1TransformedGeometry
def _define_ID2D1GeometrySink_head():
    class ID2D1GeometrySink(win32more.Graphics.Direct2D.Common.ID2D1SimplifiedGeometrySink_head):
        Guid = Guid('2cd9069f-12e2-11dc-9fed-001143a055f9')
    return ID2D1GeometrySink
def _define_ID2D1GeometrySink():
    ID2D1GeometrySink = win32more.Graphics.Direct2D.ID2D1GeometrySink_head
    ID2D1GeometrySink.AddLine = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.Common.D2D_POINT_2F, use_last_error=False)(10, 'AddLine', ((1, 'point'),)))
    ID2D1GeometrySink.AddBezier = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.Common.D2D1_BEZIER_SEGMENT_head), use_last_error=False)(11, 'AddBezier', ((1, 'bezier'),)))
    ID2D1GeometrySink.AddQuadraticBezier = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.D2D1_QUADRATIC_BEZIER_SEGMENT_head), use_last_error=False)(12, 'AddQuadraticBezier', ((1, 'bezier'),)))
    ID2D1GeometrySink.AddQuadraticBeziers = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.D2D1_QUADRATIC_BEZIER_SEGMENT),UInt32, use_last_error=False)(13, 'AddQuadraticBeziers', ((1, 'beziers'),(1, 'beziersCount'),)))
    ID2D1GeometrySink.AddArc = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.D2D1_ARC_SEGMENT_head), use_last_error=False)(14, 'AddArc', ((1, 'arc'),)))
    return ID2D1GeometrySink
def _define_ID2D1TessellationSink_head():
    class ID2D1TessellationSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('2cd906c1-12e2-11dc-9fed-001143a055f9')
    return ID2D1TessellationSink
def _define_ID2D1TessellationSink():
    ID2D1TessellationSink = win32more.Graphics.Direct2D.ID2D1TessellationSink_head
    ID2D1TessellationSink.AddTriangles = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.D2D1_TRIANGLE),UInt32, use_last_error=False)(3, 'AddTriangles', ((1, 'triangles'),(1, 'trianglesCount'),)))
    ID2D1TessellationSink.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Close', ()))
    return ID2D1TessellationSink
def _define_ID2D1PathGeometry_head():
    class ID2D1PathGeometry(win32more.Graphics.Direct2D.ID2D1Geometry_head):
        Guid = Guid('2cd906a5-12e2-11dc-9fed-001143a055f9')
    return ID2D1PathGeometry
def _define_ID2D1PathGeometry():
    ID2D1PathGeometry = win32more.Graphics.Direct2D.ID2D1PathGeometry_head
    ID2D1PathGeometry.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.ID2D1GeometrySink_head), use_last_error=False)(17, 'Open', ((1, 'geometrySink'),)))
    ID2D1PathGeometry.Stream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1GeometrySink_head, use_last_error=False)(18, 'Stream', ((1, 'geometrySink'),)))
    ID2D1PathGeometry.GetSegmentCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(19, 'GetSegmentCount', ((1, 'count'),)))
    ID2D1PathGeometry.GetFigureCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(20, 'GetFigureCount', ((1, 'count'),)))
    return ID2D1PathGeometry
def _define_ID2D1Mesh_head():
    class ID2D1Mesh(win32more.Graphics.Direct2D.ID2D1Resource_head):
        Guid = Guid('2cd906c2-12e2-11dc-9fed-001143a055f9')
    return ID2D1Mesh
def _define_ID2D1Mesh():
    ID2D1Mesh = win32more.Graphics.Direct2D.ID2D1Mesh_head
    ID2D1Mesh.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.ID2D1TessellationSink_head), use_last_error=False)(4, 'Open', ((1, 'tessellationSink'),)))
    return ID2D1Mesh
def _define_ID2D1Layer_head():
    class ID2D1Layer(win32more.Graphics.Direct2D.ID2D1Resource_head):
        Guid = Guid('2cd9069b-12e2-11dc-9fed-001143a055f9')
    return ID2D1Layer
def _define_ID2D1Layer():
    ID2D1Layer = win32more.Graphics.Direct2D.ID2D1Layer_head
    ID2D1Layer.GetSize = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.Common.D2D_SIZE_F, use_last_error=False)(4, 'GetSize', ()))
    return ID2D1Layer
def _define_ID2D1DrawingStateBlock_head():
    class ID2D1DrawingStateBlock(win32more.Graphics.Direct2D.ID2D1Resource_head):
        Guid = Guid('28506e39-ebf6-46a1-bb47-fd85565ab957')
    return ID2D1DrawingStateBlock
def _define_ID2D1DrawingStateBlock():
    ID2D1DrawingStateBlock = win32more.Graphics.Direct2D.ID2D1DrawingStateBlock_head
    ID2D1DrawingStateBlock.GetDescription = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.D2D1_DRAWING_STATE_DESCRIPTION_head), use_last_error=False)(4, 'GetDescription', ((1, 'stateDescription'),)))
    ID2D1DrawingStateBlock.SetDescription = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.D2D1_DRAWING_STATE_DESCRIPTION_head), use_last_error=False)(5, 'SetDescription', ((1, 'stateDescription'),)))
    ID2D1DrawingStateBlock.SetTextRenderingParams = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.DirectWrite.IDWriteRenderingParams_head, use_last_error=False)(6, 'SetTextRenderingParams', ((1, 'textRenderingParams'),)))
    ID2D1DrawingStateBlock.GetTextRenderingParams = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.DirectWrite.IDWriteRenderingParams_head), use_last_error=False)(7, 'GetTextRenderingParams', ((1, 'textRenderingParams'),)))
    return ID2D1DrawingStateBlock
def _define_ID2D1RenderTarget_head():
    class ID2D1RenderTarget(win32more.Graphics.Direct2D.ID2D1Resource_head):
        Guid = Guid('2cd90694-12e2-11dc-9fed-001143a055f9')
    return ID2D1RenderTarget
def _define_ID2D1RenderTarget():
    ID2D1RenderTarget = win32more.Graphics.Direct2D.ID2D1RenderTarget_head
    ID2D1RenderTarget.CreateBitmap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.Common.D2D_SIZE_U,c_void_p,UInt32,POINTER(win32more.Graphics.Direct2D.D2D1_BITMAP_PROPERTIES_head),POINTER(win32more.Graphics.Direct2D.ID2D1Bitmap_head), use_last_error=False)(4, 'CreateBitmap', ((1, 'size'),(1, 'srcData'),(1, 'pitch'),(1, 'bitmapProperties'),(1, 'bitmap'),)))
    ID2D1RenderTarget.CreateBitmapFromWicBitmap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmapSource_head,POINTER(win32more.Graphics.Direct2D.D2D1_BITMAP_PROPERTIES_head),POINTER(win32more.Graphics.Direct2D.ID2D1Bitmap_head), use_last_error=False)(5, 'CreateBitmapFromWicBitmap', ((1, 'wicBitmapSource'),(1, 'bitmapProperties'),(1, 'bitmap'),)))
    ID2D1RenderTarget.CreateSharedBitmap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),c_void_p,POINTER(win32more.Graphics.Direct2D.D2D1_BITMAP_PROPERTIES_head),POINTER(win32more.Graphics.Direct2D.ID2D1Bitmap_head), use_last_error=False)(6, 'CreateSharedBitmap', ((1, 'riid'),(1, 'data'),(1, 'bitmapProperties'),(1, 'bitmap'),)))
    ID2D1RenderTarget.CreateBitmapBrush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Bitmap_head,POINTER(win32more.Graphics.Direct2D.D2D1_BITMAP_BRUSH_PROPERTIES_head),POINTER(win32more.Graphics.Direct2D.D2D1_BRUSH_PROPERTIES_head),POINTER(win32more.Graphics.Direct2D.ID2D1BitmapBrush_head), use_last_error=False)(7, 'CreateBitmapBrush', ((1, 'bitmap'),(1, 'bitmapBrushProperties'),(1, 'brushProperties'),(1, 'bitmapBrush'),)))
    ID2D1RenderTarget.CreateSolidColorBrush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D1_COLOR_F_head),POINTER(win32more.Graphics.Direct2D.D2D1_BRUSH_PROPERTIES_head),POINTER(win32more.Graphics.Direct2D.ID2D1SolidColorBrush_head), use_last_error=False)(8, 'CreateSolidColorBrush', ((1, 'color'),(1, 'brushProperties'),(1, 'solidColorBrush'),)))
    ID2D1RenderTarget.CreateGradientStopCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.D2D1_GRADIENT_STOP),UInt32,win32more.Graphics.Direct2D.D2D1_GAMMA,win32more.Graphics.Direct2D.D2D1_EXTEND_MODE,POINTER(win32more.Graphics.Direct2D.ID2D1GradientStopCollection_head), use_last_error=False)(9, 'CreateGradientStopCollection', ((1, 'gradientStops'),(1, 'gradientStopsCount'),(1, 'colorInterpolationGamma'),(1, 'extendMode'),(1, 'gradientStopCollection'),)))
    ID2D1RenderTarget.CreateLinearGradientBrush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.D2D1_LINEAR_GRADIENT_BRUSH_PROPERTIES_head),POINTER(win32more.Graphics.Direct2D.D2D1_BRUSH_PROPERTIES_head),win32more.Graphics.Direct2D.ID2D1GradientStopCollection_head,POINTER(win32more.Graphics.Direct2D.ID2D1LinearGradientBrush_head), use_last_error=False)(10, 'CreateLinearGradientBrush', ((1, 'linearGradientBrushProperties'),(1, 'brushProperties'),(1, 'gradientStopCollection'),(1, 'linearGradientBrush'),)))
    ID2D1RenderTarget.CreateRadialGradientBrush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.D2D1_RADIAL_GRADIENT_BRUSH_PROPERTIES_head),POINTER(win32more.Graphics.Direct2D.D2D1_BRUSH_PROPERTIES_head),win32more.Graphics.Direct2D.ID2D1GradientStopCollection_head,POINTER(win32more.Graphics.Direct2D.ID2D1RadialGradientBrush_head), use_last_error=False)(11, 'CreateRadialGradientBrush', ((1, 'radialGradientBrushProperties'),(1, 'brushProperties'),(1, 'gradientStopCollection'),(1, 'radialGradientBrush'),)))
    ID2D1RenderTarget.CreateCompatibleRenderTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_SIZE_F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_SIZE_U_head),POINTER(win32more.Graphics.Direct2D.Common.D2D1_PIXEL_FORMAT_head),win32more.Graphics.Direct2D.D2D1_COMPATIBLE_RENDER_TARGET_OPTIONS,POINTER(win32more.Graphics.Direct2D.ID2D1BitmapRenderTarget_head), use_last_error=False)(12, 'CreateCompatibleRenderTarget', ((1, 'desiredSize'),(1, 'desiredPixelSize'),(1, 'desiredFormat'),(1, 'options'),(1, 'bitmapRenderTarget'),)))
    ID2D1RenderTarget.CreateLayer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_SIZE_F_head),POINTER(win32more.Graphics.Direct2D.ID2D1Layer_head), use_last_error=False)(13, 'CreateLayer', ((1, 'size'),(1, 'layer'),)))
    ID2D1RenderTarget.CreateMesh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.ID2D1Mesh_head), use_last_error=False)(14, 'CreateMesh', ((1, 'mesh'),)))
    ID2D1RenderTarget.DrawLine = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.Common.D2D_POINT_2F,win32more.Graphics.Direct2D.Common.D2D_POINT_2F,win32more.Graphics.Direct2D.ID2D1Brush_head,Single,win32more.Graphics.Direct2D.ID2D1StrokeStyle_head, use_last_error=False)(15, 'DrawLine', ((1, 'point0'),(1, 'point1'),(1, 'brush'),(1, 'strokeWidth'),(1, 'strokeStyle'),)))
    ID2D1RenderTarget.DrawRectangle = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head),win32more.Graphics.Direct2D.ID2D1Brush_head,Single,win32more.Graphics.Direct2D.ID2D1StrokeStyle_head, use_last_error=False)(16, 'DrawRectangle', ((1, 'rect'),(1, 'brush'),(1, 'strokeWidth'),(1, 'strokeStyle'),)))
    ID2D1RenderTarget.FillRectangle = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head),win32more.Graphics.Direct2D.ID2D1Brush_head, use_last_error=False)(17, 'FillRectangle', ((1, 'rect'),(1, 'brush'),)))
    ID2D1RenderTarget.DrawRoundedRectangle = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.D2D1_ROUNDED_RECT_head),win32more.Graphics.Direct2D.ID2D1Brush_head,Single,win32more.Graphics.Direct2D.ID2D1StrokeStyle_head, use_last_error=False)(18, 'DrawRoundedRectangle', ((1, 'roundedRect'),(1, 'brush'),(1, 'strokeWidth'),(1, 'strokeStyle'),)))
    ID2D1RenderTarget.FillRoundedRectangle = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.D2D1_ROUNDED_RECT_head),win32more.Graphics.Direct2D.ID2D1Brush_head, use_last_error=False)(19, 'FillRoundedRectangle', ((1, 'roundedRect'),(1, 'brush'),)))
    ID2D1RenderTarget.DrawEllipse = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.D2D1_ELLIPSE_head),win32more.Graphics.Direct2D.ID2D1Brush_head,Single,win32more.Graphics.Direct2D.ID2D1StrokeStyle_head, use_last_error=False)(20, 'DrawEllipse', ((1, 'ellipse'),(1, 'brush'),(1, 'strokeWidth'),(1, 'strokeStyle'),)))
    ID2D1RenderTarget.FillEllipse = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.D2D1_ELLIPSE_head),win32more.Graphics.Direct2D.ID2D1Brush_head, use_last_error=False)(21, 'FillEllipse', ((1, 'ellipse'),(1, 'brush'),)))
    ID2D1RenderTarget.DrawGeometry = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.ID2D1Geometry_head,win32more.Graphics.Direct2D.ID2D1Brush_head,Single,win32more.Graphics.Direct2D.ID2D1StrokeStyle_head, use_last_error=False)(22, 'DrawGeometry', ((1, 'geometry'),(1, 'brush'),(1, 'strokeWidth'),(1, 'strokeStyle'),)))
    ID2D1RenderTarget.FillGeometry = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.ID2D1Geometry_head,win32more.Graphics.Direct2D.ID2D1Brush_head,win32more.Graphics.Direct2D.ID2D1Brush_head, use_last_error=False)(23, 'FillGeometry', ((1, 'geometry'),(1, 'brush'),(1, 'opacityBrush'),)))
    ID2D1RenderTarget.FillMesh = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.ID2D1Mesh_head,win32more.Graphics.Direct2D.ID2D1Brush_head, use_last_error=False)(24, 'FillMesh', ((1, 'mesh'),(1, 'brush'),)))
    ID2D1RenderTarget.FillOpacityMask = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.ID2D1Bitmap_head,win32more.Graphics.Direct2D.ID2D1Brush_head,win32more.Graphics.Direct2D.D2D1_OPACITY_MASK_CONTENT,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head), use_last_error=False)(25, 'FillOpacityMask', ((1, 'opacityMask'),(1, 'brush'),(1, 'content'),(1, 'destinationRectangle'),(1, 'sourceRectangle'),)))
    ID2D1RenderTarget.DrawBitmap = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.ID2D1Bitmap_head,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head),Single,win32more.Graphics.Direct2D.D2D1_BITMAP_INTERPOLATION_MODE,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head), use_last_error=False)(26, 'DrawBitmap', ((1, 'bitmap'),(1, 'destinationRectangle'),(1, 'opacity'),(1, 'interpolationMode'),(1, 'sourceRectangle'),)))
    ID2D1RenderTarget.DrawText = COMMETHOD(WINFUNCTYPE(Void,POINTER(Char),UInt32,win32more.Graphics.DirectWrite.IDWriteTextFormat_head,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head),win32more.Graphics.Direct2D.ID2D1Brush_head,win32more.Graphics.Direct2D.D2D1_DRAW_TEXT_OPTIONS,win32more.Graphics.DirectWrite.DWRITE_MEASURING_MODE, use_last_error=False)(27, 'DrawText', ((1, 'string'),(1, 'stringLength'),(1, 'textFormat'),(1, 'layoutRect'),(1, 'defaultFillBrush'),(1, 'options'),(1, 'measuringMode'),)))
    ID2D1RenderTarget.DrawTextLayout = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.Common.D2D_POINT_2F,win32more.Graphics.DirectWrite.IDWriteTextLayout_head,win32more.Graphics.Direct2D.ID2D1Brush_head,win32more.Graphics.Direct2D.D2D1_DRAW_TEXT_OPTIONS, use_last_error=False)(28, 'DrawTextLayout', ((1, 'origin'),(1, 'textLayout'),(1, 'defaultFillBrush'),(1, 'options'),)))
    ID2D1RenderTarget.DrawGlyphRun = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.Common.D2D_POINT_2F,POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_RUN_head),win32more.Graphics.Direct2D.ID2D1Brush_head,win32more.Graphics.DirectWrite.DWRITE_MEASURING_MODE, use_last_error=False)(29, 'DrawGlyphRun', ((1, 'baselineOrigin'),(1, 'glyphRun'),(1, 'foregroundBrush'),(1, 'measuringMode'),)))
    ID2D1RenderTarget.SetTransform = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head), use_last_error=False)(30, 'SetTransform', ((1, 'transform'),)))
    ID2D1RenderTarget.GetTransform = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head), use_last_error=False)(31, 'GetTransform', ((1, 'transform'),)))
    ID2D1RenderTarget.SetAntialiasMode = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.D2D1_ANTIALIAS_MODE, use_last_error=False)(32, 'SetAntialiasMode', ((1, 'antialiasMode'),)))
    ID2D1RenderTarget.GetAntialiasMode = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_ANTIALIAS_MODE, use_last_error=False)(33, 'GetAntialiasMode', ()))
    ID2D1RenderTarget.SetTextAntialiasMode = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.D2D1_TEXT_ANTIALIAS_MODE, use_last_error=False)(34, 'SetTextAntialiasMode', ((1, 'textAntialiasMode'),)))
    ID2D1RenderTarget.GetTextAntialiasMode = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_TEXT_ANTIALIAS_MODE, use_last_error=False)(35, 'GetTextAntialiasMode', ()))
    ID2D1RenderTarget.SetTextRenderingParams = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.DirectWrite.IDWriteRenderingParams_head, use_last_error=False)(36, 'SetTextRenderingParams', ((1, 'textRenderingParams'),)))
    ID2D1RenderTarget.GetTextRenderingParams = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.DirectWrite.IDWriteRenderingParams_head), use_last_error=False)(37, 'GetTextRenderingParams', ((1, 'textRenderingParams'),)))
    ID2D1RenderTarget.SetTags = COMMETHOD(WINFUNCTYPE(Void,UInt64,UInt64, use_last_error=False)(38, 'SetTags', ((1, 'tag1'),(1, 'tag2'),)))
    ID2D1RenderTarget.GetTags = COMMETHOD(WINFUNCTYPE(Void,POINTER(UInt64),POINTER(UInt64), use_last_error=False)(39, 'GetTags', ((1, 'tag1'),(1, 'tag2'),)))
    ID2D1RenderTarget.PushLayer = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.D2D1_LAYER_PARAMETERS_head),win32more.Graphics.Direct2D.ID2D1Layer_head, use_last_error=False)(40, 'PushLayer', ((1, 'layerParameters'),(1, 'layer'),)))
    ID2D1RenderTarget.PopLayer = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(41, 'PopLayer', ()))
    ID2D1RenderTarget.Flush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64),POINTER(UInt64), use_last_error=False)(42, 'Flush', ((1, 'tag1'),(1, 'tag2'),)))
    ID2D1RenderTarget.SaveDrawingState = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.ID2D1DrawingStateBlock_head, use_last_error=False)(43, 'SaveDrawingState', ((1, 'drawingStateBlock'),)))
    ID2D1RenderTarget.RestoreDrawingState = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.ID2D1DrawingStateBlock_head, use_last_error=False)(44, 'RestoreDrawingState', ((1, 'drawingStateBlock'),)))
    ID2D1RenderTarget.PushAxisAlignedClip = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head),win32more.Graphics.Direct2D.D2D1_ANTIALIAS_MODE, use_last_error=False)(45, 'PushAxisAlignedClip', ((1, 'clipRect'),(1, 'antialiasMode'),)))
    ID2D1RenderTarget.PopAxisAlignedClip = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(46, 'PopAxisAlignedClip', ()))
    ID2D1RenderTarget.Clear = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.Common.D2D1_COLOR_F_head), use_last_error=False)(47, 'Clear', ((1, 'clearColor'),)))
    ID2D1RenderTarget.BeginDraw = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(48, 'BeginDraw', ()))
    ID2D1RenderTarget.EndDraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64),POINTER(UInt64), use_last_error=False)(49, 'EndDraw', ((1, 'tag1'),(1, 'tag2'),)))
    ID2D1RenderTarget.GetPixelFormat = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.Common.D2D1_PIXEL_FORMAT, use_last_error=False)(50, 'GetPixelFormat', ()))
    ID2D1RenderTarget.SetDpi = COMMETHOD(WINFUNCTYPE(Void,Single,Single, use_last_error=False)(51, 'SetDpi', ((1, 'dpiX'),(1, 'dpiY'),)))
    ID2D1RenderTarget.GetDpi = COMMETHOD(WINFUNCTYPE(Void,POINTER(Single),POINTER(Single), use_last_error=False)(52, 'GetDpi', ((1, 'dpiX'),(1, 'dpiY'),)))
    ID2D1RenderTarget.GetSize = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.Common.D2D_SIZE_F, use_last_error=False)(53, 'GetSize', ()))
    ID2D1RenderTarget.GetPixelSize = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.Common.D2D_SIZE_U, use_last_error=False)(54, 'GetPixelSize', ()))
    ID2D1RenderTarget.GetMaximumBitmapSize = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(55, 'GetMaximumBitmapSize', ()))
    ID2D1RenderTarget.IsSupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Graphics.Direct2D.D2D1_RENDER_TARGET_PROPERTIES_head), use_last_error=False)(56, 'IsSupported', ((1, 'renderTargetProperties'),)))
    return ID2D1RenderTarget
def _define_ID2D1BitmapRenderTarget_head():
    class ID2D1BitmapRenderTarget(win32more.Graphics.Direct2D.ID2D1RenderTarget_head):
        Guid = Guid('2cd90695-12e2-11dc-9fed-001143a055f9')
    return ID2D1BitmapRenderTarget
def _define_ID2D1BitmapRenderTarget():
    ID2D1BitmapRenderTarget = win32more.Graphics.Direct2D.ID2D1BitmapRenderTarget_head
    ID2D1BitmapRenderTarget.GetBitmap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.ID2D1Bitmap_head), use_last_error=False)(57, 'GetBitmap', ((1, 'bitmap'),)))
    return ID2D1BitmapRenderTarget
def _define_ID2D1HwndRenderTarget_head():
    class ID2D1HwndRenderTarget(win32more.Graphics.Direct2D.ID2D1RenderTarget_head):
        Guid = Guid('2cd90698-12e2-11dc-9fed-001143a055f9')
    return ID2D1HwndRenderTarget
def _define_ID2D1HwndRenderTarget():
    ID2D1HwndRenderTarget = win32more.Graphics.Direct2D.ID2D1HwndRenderTarget_head
    ID2D1HwndRenderTarget.CheckWindowState = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_WINDOW_STATE, use_last_error=False)(57, 'CheckWindowState', ()))
    ID2D1HwndRenderTarget.Resize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_SIZE_U_head), use_last_error=False)(58, 'Resize', ((1, 'pixelSize'),)))
    ID2D1HwndRenderTarget.GetHwnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HWND, use_last_error=False)(59, 'GetHwnd', ()))
    return ID2D1HwndRenderTarget
def _define_ID2D1GdiInteropRenderTarget_head():
    class ID2D1GdiInteropRenderTarget(win32more.System.Com.IUnknown_head):
        Guid = Guid('e0db51c3-6f77-4bae-b3d5-e47509b35838')
    return ID2D1GdiInteropRenderTarget
def _define_ID2D1GdiInteropRenderTarget():
    ID2D1GdiInteropRenderTarget = win32more.Graphics.Direct2D.ID2D1GdiInteropRenderTarget_head
    ID2D1GdiInteropRenderTarget.GetDC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.D2D1_DC_INITIALIZE_MODE,POINTER(win32more.Graphics.Gdi.HDC), use_last_error=False)(3, 'GetDC', ((1, 'mode'),(1, 'hdc'),)))
    ID2D1GdiInteropRenderTarget.ReleaseDC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(4, 'ReleaseDC', ((1, 'update'),)))
    return ID2D1GdiInteropRenderTarget
def _define_ID2D1DCRenderTarget_head():
    class ID2D1DCRenderTarget(win32more.Graphics.Direct2D.ID2D1RenderTarget_head):
        Guid = Guid('1c51bc64-de61-46fd-9899-63a5d8f03950')
    return ID2D1DCRenderTarget
def _define_ID2D1DCRenderTarget():
    ID2D1DCRenderTarget = win32more.Graphics.Direct2D.ID2D1DCRenderTarget_head
    ID2D1DCRenderTarget.BindDC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(57, 'BindDC', ((1, 'hDC'),(1, 'pSubRect'),)))
    return ID2D1DCRenderTarget
def _define_ID2D1Factory_head():
    class ID2D1Factory(win32more.System.Com.IUnknown_head):
        Guid = Guid('06152247-6f50-465a-9245-118bfd3b6007')
    return ID2D1Factory
def _define_ID2D1Factory():
    ID2D1Factory = win32more.Graphics.Direct2D.ID2D1Factory_head
    ID2D1Factory.ReloadSystemMetrics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'ReloadSystemMetrics', ()))
    ID2D1Factory.GetDesktopDpi = COMMETHOD(WINFUNCTYPE(Void,POINTER(Single),POINTER(Single), use_last_error=False)(4, 'GetDesktopDpi', ((1, 'dpiX'),(1, 'dpiY'),)))
    ID2D1Factory.CreateRectangleGeometry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head),POINTER(win32more.Graphics.Direct2D.ID2D1RectangleGeometry_head), use_last_error=False)(5, 'CreateRectangleGeometry', ((1, 'rectangle'),(1, 'rectangleGeometry'),)))
    ID2D1Factory.CreateRoundedRectangleGeometry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.D2D1_ROUNDED_RECT_head),POINTER(win32more.Graphics.Direct2D.ID2D1RoundedRectangleGeometry_head), use_last_error=False)(6, 'CreateRoundedRectangleGeometry', ((1, 'roundedRectangle'),(1, 'roundedRectangleGeometry'),)))
    ID2D1Factory.CreateEllipseGeometry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.D2D1_ELLIPSE_head),POINTER(win32more.Graphics.Direct2D.ID2D1EllipseGeometry_head), use_last_error=False)(7, 'CreateEllipseGeometry', ((1, 'ellipse'),(1, 'ellipseGeometry'),)))
    ID2D1Factory.CreateGeometryGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.Common.D2D1_FILL_MODE,POINTER(win32more.Graphics.Direct2D.ID2D1Geometry_head),UInt32,POINTER(win32more.Graphics.Direct2D.ID2D1GeometryGroup_head), use_last_error=False)(8, 'CreateGeometryGroup', ((1, 'fillMode'),(1, 'geometries'),(1, 'geometriesCount'),(1, 'geometryGroup'),)))
    ID2D1Factory.CreateTransformedGeometry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Geometry_head,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head),POINTER(win32more.Graphics.Direct2D.ID2D1TransformedGeometry_head), use_last_error=False)(9, 'CreateTransformedGeometry', ((1, 'sourceGeometry'),(1, 'transform'),(1, 'transformedGeometry'),)))
    ID2D1Factory.CreatePathGeometry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.ID2D1PathGeometry_head), use_last_error=False)(10, 'CreatePathGeometry', ((1, 'pathGeometry'),)))
    ID2D1Factory.CreateStrokeStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.D2D1_STROKE_STYLE_PROPERTIES_head),POINTER(Single),UInt32,POINTER(win32more.Graphics.Direct2D.ID2D1StrokeStyle_head), use_last_error=False)(11, 'CreateStrokeStyle', ((1, 'strokeStyleProperties'),(1, 'dashes'),(1, 'dashesCount'),(1, 'strokeStyle'),)))
    ID2D1Factory.CreateDrawingStateBlock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.D2D1_DRAWING_STATE_DESCRIPTION_head),win32more.Graphics.DirectWrite.IDWriteRenderingParams_head,POINTER(win32more.Graphics.Direct2D.ID2D1DrawingStateBlock_head), use_last_error=False)(12, 'CreateDrawingStateBlock', ((1, 'drawingStateDescription'),(1, 'textRenderingParams'),(1, 'drawingStateBlock'),)))
    ID2D1Factory.CreateWicBitmapRenderTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmap_head,POINTER(win32more.Graphics.Direct2D.D2D1_RENDER_TARGET_PROPERTIES_head),POINTER(win32more.Graphics.Direct2D.ID2D1RenderTarget_head), use_last_error=False)(13, 'CreateWicBitmapRenderTarget', ((1, 'target'),(1, 'renderTargetProperties'),(1, 'renderTarget'),)))
    ID2D1Factory.CreateHwndRenderTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.D2D1_RENDER_TARGET_PROPERTIES_head),POINTER(win32more.Graphics.Direct2D.D2D1_HWND_RENDER_TARGET_PROPERTIES_head),POINTER(win32more.Graphics.Direct2D.ID2D1HwndRenderTarget_head), use_last_error=False)(14, 'CreateHwndRenderTarget', ((1, 'renderTargetProperties'),(1, 'hwndRenderTargetProperties'),(1, 'hwndRenderTarget'),)))
    ID2D1Factory.CreateDxgiSurfaceRenderTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGISurface_head,POINTER(win32more.Graphics.Direct2D.D2D1_RENDER_TARGET_PROPERTIES_head),POINTER(win32more.Graphics.Direct2D.ID2D1RenderTarget_head), use_last_error=False)(15, 'CreateDxgiSurfaceRenderTarget', ((1, 'dxgiSurface'),(1, 'renderTargetProperties'),(1, 'renderTarget'),)))
    ID2D1Factory.CreateDCRenderTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.D2D1_RENDER_TARGET_PROPERTIES_head),POINTER(win32more.Graphics.Direct2D.ID2D1DCRenderTarget_head), use_last_error=False)(16, 'CreateDCRenderTarget', ((1, 'renderTargetProperties'),(1, 'dcRenderTarget'),)))
    return ID2D1Factory
D2D1_CHANNEL_SELECTOR = UInt32
D2D1_CHANNEL_SELECTOR_R = 0
D2D1_CHANNEL_SELECTOR_G = 1
D2D1_CHANNEL_SELECTOR_B = 2
D2D1_CHANNEL_SELECTOR_A = 3
D2D1_CHANNEL_SELECTOR_FORCE_DWORD = 4294967295
D2D1_BITMAPSOURCE_ORIENTATION = UInt32
D2D1_BITMAPSOURCE_ORIENTATION_DEFAULT = 1
D2D1_BITMAPSOURCE_ORIENTATION_FLIP_HORIZONTAL = 2
D2D1_BITMAPSOURCE_ORIENTATION_ROTATE_CLOCKWISE180 = 3
D2D1_BITMAPSOURCE_ORIENTATION_ROTATE_CLOCKWISE180_FLIP_HORIZONTAL = 4
D2D1_BITMAPSOURCE_ORIENTATION_ROTATE_CLOCKWISE270_FLIP_HORIZONTAL = 5
D2D1_BITMAPSOURCE_ORIENTATION_ROTATE_CLOCKWISE90 = 6
D2D1_BITMAPSOURCE_ORIENTATION_ROTATE_CLOCKWISE90_FLIP_HORIZONTAL = 7
D2D1_BITMAPSOURCE_ORIENTATION_ROTATE_CLOCKWISE270 = 8
D2D1_BITMAPSOURCE_ORIENTATION_FORCE_DWORD = 4294967295
D2D1_GAUSSIANBLUR_PROP = UInt32
D2D1_GAUSSIANBLUR_PROP_STANDARD_DEVIATION = 0
D2D1_GAUSSIANBLUR_PROP_OPTIMIZATION = 1
D2D1_GAUSSIANBLUR_PROP_BORDER_MODE = 2
D2D1_GAUSSIANBLUR_PROP_FORCE_DWORD = 4294967295
D2D1_GAUSSIANBLUR_OPTIMIZATION = UInt32
D2D1_GAUSSIANBLUR_OPTIMIZATION_SPEED = 0
D2D1_GAUSSIANBLUR_OPTIMIZATION_BALANCED = 1
D2D1_GAUSSIANBLUR_OPTIMIZATION_QUALITY = 2
D2D1_GAUSSIANBLUR_OPTIMIZATION_FORCE_DWORD = 4294967295
D2D1_DIRECTIONALBLUR_PROP = UInt32
D2D1_DIRECTIONALBLUR_PROP_STANDARD_DEVIATION = 0
D2D1_DIRECTIONALBLUR_PROP_ANGLE = 1
D2D1_DIRECTIONALBLUR_PROP_OPTIMIZATION = 2
D2D1_DIRECTIONALBLUR_PROP_BORDER_MODE = 3
D2D1_DIRECTIONALBLUR_PROP_FORCE_DWORD = 4294967295
D2D1_DIRECTIONALBLUR_OPTIMIZATION = UInt32
D2D1_DIRECTIONALBLUR_OPTIMIZATION_SPEED = 0
D2D1_DIRECTIONALBLUR_OPTIMIZATION_BALANCED = 1
D2D1_DIRECTIONALBLUR_OPTIMIZATION_QUALITY = 2
D2D1_DIRECTIONALBLUR_OPTIMIZATION_FORCE_DWORD = 4294967295
D2D1_SHADOW_PROP = UInt32
D2D1_SHADOW_PROP_BLUR_STANDARD_DEVIATION = 0
D2D1_SHADOW_PROP_COLOR = 1
D2D1_SHADOW_PROP_OPTIMIZATION = 2
D2D1_SHADOW_PROP_FORCE_DWORD = 4294967295
D2D1_SHADOW_OPTIMIZATION = UInt32
D2D1_SHADOW_OPTIMIZATION_SPEED = 0
D2D1_SHADOW_OPTIMIZATION_BALANCED = 1
D2D1_SHADOW_OPTIMIZATION_QUALITY = 2
D2D1_SHADOW_OPTIMIZATION_FORCE_DWORD = 4294967295
D2D1_BLEND_PROP = UInt32
D2D1_BLEND_PROP_MODE = 0
D2D1_BLEND_PROP_FORCE_DWORD = 4294967295
D2D1_SATURATION_PROP = UInt32
D2D1_SATURATION_PROP_SATURATION = 0
D2D1_SATURATION_PROP_FORCE_DWORD = 4294967295
D2D1_HUEROTATION_PROP = UInt32
D2D1_HUEROTATION_PROP_ANGLE = 0
D2D1_HUEROTATION_PROP_FORCE_DWORD = 4294967295
D2D1_COLORMATRIX_PROP = UInt32
D2D1_COLORMATRIX_PROP_COLOR_MATRIX = 0
D2D1_COLORMATRIX_PROP_ALPHA_MODE = 1
D2D1_COLORMATRIX_PROP_CLAMP_OUTPUT = 2
D2D1_COLORMATRIX_PROP_FORCE_DWORD = 4294967295
D2D1_BITMAPSOURCE_PROP = UInt32
D2D1_BITMAPSOURCE_PROP_WIC_BITMAP_SOURCE = 0
D2D1_BITMAPSOURCE_PROP_SCALE = 1
D2D1_BITMAPSOURCE_PROP_INTERPOLATION_MODE = 2
D2D1_BITMAPSOURCE_PROP_ENABLE_DPI_CORRECTION = 3
D2D1_BITMAPSOURCE_PROP_ALPHA_MODE = 4
D2D1_BITMAPSOURCE_PROP_ORIENTATION = 5
D2D1_BITMAPSOURCE_PROP_FORCE_DWORD = 4294967295
D2D1_BITMAPSOURCE_INTERPOLATION_MODE = UInt32
D2D1_BITMAPSOURCE_INTERPOLATION_MODE_NEAREST_NEIGHBOR = 0
D2D1_BITMAPSOURCE_INTERPOLATION_MODE_LINEAR = 1
D2D1_BITMAPSOURCE_INTERPOLATION_MODE_CUBIC = 2
D2D1_BITMAPSOURCE_INTERPOLATION_MODE_FANT = 6
D2D1_BITMAPSOURCE_INTERPOLATION_MODE_MIPMAP_LINEAR = 7
D2D1_BITMAPSOURCE_INTERPOLATION_MODE_FORCE_DWORD = 4294967295
D2D1_BITMAPSOURCE_ALPHA_MODE = UInt32
D2D1_BITMAPSOURCE_ALPHA_MODE_PREMULTIPLIED = 1
D2D1_BITMAPSOURCE_ALPHA_MODE_STRAIGHT = 2
D2D1_BITMAPSOURCE_ALPHA_MODE_FORCE_DWORD = 4294967295
D2D1_COMPOSITE_PROP = UInt32
D2D1_COMPOSITE_PROP_MODE = 0
D2D1_COMPOSITE_PROP_FORCE_DWORD = 4294967295
D2D1_3DTRANSFORM_PROP = UInt32
D2D1_3DTRANSFORM_PROP_INTERPOLATION_MODE = 0
D2D1_3DTRANSFORM_PROP_BORDER_MODE = 1
D2D1_3DTRANSFORM_PROP_TRANSFORM_MATRIX = 2
D2D1_3DTRANSFORM_PROP_FORCE_DWORD = 4294967295
D2D1_3DTRANSFORM_INTERPOLATION_MODE = UInt32
D2D1_3DTRANSFORM_INTERPOLATION_MODE_NEAREST_NEIGHBOR = 0
D2D1_3DTRANSFORM_INTERPOLATION_MODE_LINEAR = 1
D2D1_3DTRANSFORM_INTERPOLATION_MODE_CUBIC = 2
D2D1_3DTRANSFORM_INTERPOLATION_MODE_MULTI_SAMPLE_LINEAR = 3
D2D1_3DTRANSFORM_INTERPOLATION_MODE_ANISOTROPIC = 4
D2D1_3DTRANSFORM_INTERPOLATION_MODE_FORCE_DWORD = 4294967295
D2D1_3DPERSPECTIVETRANSFORM_PROP = UInt32
D2D1_3DPERSPECTIVETRANSFORM_PROP_INTERPOLATION_MODE = 0
D2D1_3DPERSPECTIVETRANSFORM_PROP_BORDER_MODE = 1
D2D1_3DPERSPECTIVETRANSFORM_PROP_DEPTH = 2
D2D1_3DPERSPECTIVETRANSFORM_PROP_PERSPECTIVE_ORIGIN = 3
D2D1_3DPERSPECTIVETRANSFORM_PROP_LOCAL_OFFSET = 4
D2D1_3DPERSPECTIVETRANSFORM_PROP_GLOBAL_OFFSET = 5
D2D1_3DPERSPECTIVETRANSFORM_PROP_ROTATION_ORIGIN = 6
D2D1_3DPERSPECTIVETRANSFORM_PROP_ROTATION = 7
D2D1_3DPERSPECTIVETRANSFORM_PROP_FORCE_DWORD = 4294967295
D2D1_3DPERSPECTIVETRANSFORM_INTERPOLATION_MODE = UInt32
D2D1_3DPERSPECTIVETRANSFORM_INTERPOLATION_MODE_NEAREST_NEIGHBOR = 0
D2D1_3DPERSPECTIVETRANSFORM_INTERPOLATION_MODE_LINEAR = 1
D2D1_3DPERSPECTIVETRANSFORM_INTERPOLATION_MODE_CUBIC = 2
D2D1_3DPERSPECTIVETRANSFORM_INTERPOLATION_MODE_MULTI_SAMPLE_LINEAR = 3
D2D1_3DPERSPECTIVETRANSFORM_INTERPOLATION_MODE_ANISOTROPIC = 4
D2D1_3DPERSPECTIVETRANSFORM_INTERPOLATION_MODE_FORCE_DWORD = 4294967295
D2D1_2DAFFINETRANSFORM_PROP = UInt32
D2D1_2DAFFINETRANSFORM_PROP_INTERPOLATION_MODE = 0
D2D1_2DAFFINETRANSFORM_PROP_BORDER_MODE = 1
D2D1_2DAFFINETRANSFORM_PROP_TRANSFORM_MATRIX = 2
D2D1_2DAFFINETRANSFORM_PROP_SHARPNESS = 3
D2D1_2DAFFINETRANSFORM_PROP_FORCE_DWORD = 4294967295
D2D1_DPICOMPENSATION_PROP = UInt32
D2D1_DPICOMPENSATION_PROP_INTERPOLATION_MODE = 0
D2D1_DPICOMPENSATION_PROP_BORDER_MODE = 1
D2D1_DPICOMPENSATION_PROP_INPUT_DPI = 2
D2D1_DPICOMPENSATION_PROP_FORCE_DWORD = 4294967295
D2D1_DPICOMPENSATION_INTERPOLATION_MODE = UInt32
D2D1_DPICOMPENSATION_INTERPOLATION_MODE_NEAREST_NEIGHBOR = 0
D2D1_DPICOMPENSATION_INTERPOLATION_MODE_LINEAR = 1
D2D1_DPICOMPENSATION_INTERPOLATION_MODE_CUBIC = 2
D2D1_DPICOMPENSATION_INTERPOLATION_MODE_MULTI_SAMPLE_LINEAR = 3
D2D1_DPICOMPENSATION_INTERPOLATION_MODE_ANISOTROPIC = 4
D2D1_DPICOMPENSATION_INTERPOLATION_MODE_HIGH_QUALITY_CUBIC = 5
D2D1_DPICOMPENSATION_INTERPOLATION_MODE_FORCE_DWORD = 4294967295
D2D1_SCALE_PROP = UInt32
D2D1_SCALE_PROP_SCALE = 0
D2D1_SCALE_PROP_CENTER_POINT = 1
D2D1_SCALE_PROP_INTERPOLATION_MODE = 2
D2D1_SCALE_PROP_BORDER_MODE = 3
D2D1_SCALE_PROP_SHARPNESS = 4
D2D1_SCALE_PROP_FORCE_DWORD = 4294967295
D2D1_SCALE_INTERPOLATION_MODE = UInt32
D2D1_SCALE_INTERPOLATION_MODE_NEAREST_NEIGHBOR = 0
D2D1_SCALE_INTERPOLATION_MODE_LINEAR = 1
D2D1_SCALE_INTERPOLATION_MODE_CUBIC = 2
D2D1_SCALE_INTERPOLATION_MODE_MULTI_SAMPLE_LINEAR = 3
D2D1_SCALE_INTERPOLATION_MODE_ANISOTROPIC = 4
D2D1_SCALE_INTERPOLATION_MODE_HIGH_QUALITY_CUBIC = 5
D2D1_SCALE_INTERPOLATION_MODE_FORCE_DWORD = 4294967295
D2D1_TURBULENCE_PROP = UInt32
D2D1_TURBULENCE_PROP_OFFSET = 0
D2D1_TURBULENCE_PROP_SIZE = 1
D2D1_TURBULENCE_PROP_BASE_FREQUENCY = 2
D2D1_TURBULENCE_PROP_NUM_OCTAVES = 3
D2D1_TURBULENCE_PROP_SEED = 4
D2D1_TURBULENCE_PROP_NOISE = 5
D2D1_TURBULENCE_PROP_STITCHABLE = 6
D2D1_TURBULENCE_PROP_FORCE_DWORD = 4294967295
D2D1_DISPLACEMENTMAP_PROP = UInt32
D2D1_DISPLACEMENTMAP_PROP_SCALE = 0
D2D1_DISPLACEMENTMAP_PROP_X_CHANNEL_SELECT = 1
D2D1_DISPLACEMENTMAP_PROP_Y_CHANNEL_SELECT = 2
D2D1_DISPLACEMENTMAP_PROP_FORCE_DWORD = 4294967295
D2D1_COLORMANAGEMENT_PROP = UInt32
D2D1_COLORMANAGEMENT_PROP_SOURCE_COLOR_CONTEXT = 0
D2D1_COLORMANAGEMENT_PROP_SOURCE_RENDERING_INTENT = 1
D2D1_COLORMANAGEMENT_PROP_DESTINATION_COLOR_CONTEXT = 2
D2D1_COLORMANAGEMENT_PROP_DESTINATION_RENDERING_INTENT = 3
D2D1_COLORMANAGEMENT_PROP_ALPHA_MODE = 4
D2D1_COLORMANAGEMENT_PROP_QUALITY = 5
D2D1_COLORMANAGEMENT_PROP_FORCE_DWORD = 4294967295
D2D1_COLORMANAGEMENT_ALPHA_MODE = UInt32
D2D1_COLORMANAGEMENT_ALPHA_MODE_PREMULTIPLIED = 1
D2D1_COLORMANAGEMENT_ALPHA_MODE_STRAIGHT = 2
D2D1_COLORMANAGEMENT_ALPHA_MODE_FORCE_DWORD = 4294967295
D2D1_COLORMANAGEMENT_QUALITY = UInt32
D2D1_COLORMANAGEMENT_QUALITY_PROOF = 0
D2D1_COLORMANAGEMENT_QUALITY_NORMAL = 1
D2D1_COLORMANAGEMENT_QUALITY_BEST = 2
D2D1_COLORMANAGEMENT_QUALITY_FORCE_DWORD = 4294967295
D2D1_COLORMANAGEMENT_RENDERING_INTENT = UInt32
D2D1_COLORMANAGEMENT_RENDERING_INTENT_PERCEPTUAL = 0
D2D1_COLORMANAGEMENT_RENDERING_INTENT_RELATIVE_COLORIMETRIC = 1
D2D1_COLORMANAGEMENT_RENDERING_INTENT_SATURATION = 2
D2D1_COLORMANAGEMENT_RENDERING_INTENT_ABSOLUTE_COLORIMETRIC = 3
D2D1_COLORMANAGEMENT_RENDERING_INTENT_FORCE_DWORD = 4294967295
D2D1_HISTOGRAM_PROP = UInt32
D2D1_HISTOGRAM_PROP_NUM_BINS = 0
D2D1_HISTOGRAM_PROP_CHANNEL_SELECT = 1
D2D1_HISTOGRAM_PROP_HISTOGRAM_OUTPUT = 2
D2D1_HISTOGRAM_PROP_FORCE_DWORD = 4294967295
D2D1_POINTSPECULAR_PROP = UInt32
D2D1_POINTSPECULAR_PROP_LIGHT_POSITION = 0
D2D1_POINTSPECULAR_PROP_SPECULAR_EXPONENT = 1
D2D1_POINTSPECULAR_PROP_SPECULAR_CONSTANT = 2
D2D1_POINTSPECULAR_PROP_SURFACE_SCALE = 3
D2D1_POINTSPECULAR_PROP_COLOR = 4
D2D1_POINTSPECULAR_PROP_KERNEL_UNIT_LENGTH = 5
D2D1_POINTSPECULAR_PROP_SCALE_MODE = 6
D2D1_POINTSPECULAR_PROP_FORCE_DWORD = 4294967295
D2D1_POINTSPECULAR_SCALE_MODE = UInt32
D2D1_POINTSPECULAR_SCALE_MODE_NEAREST_NEIGHBOR = 0
D2D1_POINTSPECULAR_SCALE_MODE_LINEAR = 1
D2D1_POINTSPECULAR_SCALE_MODE_CUBIC = 2
D2D1_POINTSPECULAR_SCALE_MODE_MULTI_SAMPLE_LINEAR = 3
D2D1_POINTSPECULAR_SCALE_MODE_ANISOTROPIC = 4
D2D1_POINTSPECULAR_SCALE_MODE_HIGH_QUALITY_CUBIC = 5
D2D1_POINTSPECULAR_SCALE_MODE_FORCE_DWORD = 4294967295
D2D1_SPOTSPECULAR_PROP = UInt32
D2D1_SPOTSPECULAR_PROP_LIGHT_POSITION = 0
D2D1_SPOTSPECULAR_PROP_POINTS_AT = 1
D2D1_SPOTSPECULAR_PROP_FOCUS = 2
D2D1_SPOTSPECULAR_PROP_LIMITING_CONE_ANGLE = 3
D2D1_SPOTSPECULAR_PROP_SPECULAR_EXPONENT = 4
D2D1_SPOTSPECULAR_PROP_SPECULAR_CONSTANT = 5
D2D1_SPOTSPECULAR_PROP_SURFACE_SCALE = 6
D2D1_SPOTSPECULAR_PROP_COLOR = 7
D2D1_SPOTSPECULAR_PROP_KERNEL_UNIT_LENGTH = 8
D2D1_SPOTSPECULAR_PROP_SCALE_MODE = 9
D2D1_SPOTSPECULAR_PROP_FORCE_DWORD = 4294967295
D2D1_SPOTSPECULAR_SCALE_MODE = UInt32
D2D1_SPOTSPECULAR_SCALE_MODE_NEAREST_NEIGHBOR = 0
D2D1_SPOTSPECULAR_SCALE_MODE_LINEAR = 1
D2D1_SPOTSPECULAR_SCALE_MODE_CUBIC = 2
D2D1_SPOTSPECULAR_SCALE_MODE_MULTI_SAMPLE_LINEAR = 3
D2D1_SPOTSPECULAR_SCALE_MODE_ANISOTROPIC = 4
D2D1_SPOTSPECULAR_SCALE_MODE_HIGH_QUALITY_CUBIC = 5
D2D1_SPOTSPECULAR_SCALE_MODE_FORCE_DWORD = 4294967295
D2D1_DISTANTSPECULAR_PROP = UInt32
D2D1_DISTANTSPECULAR_PROP_AZIMUTH = 0
D2D1_DISTANTSPECULAR_PROP_ELEVATION = 1
D2D1_DISTANTSPECULAR_PROP_SPECULAR_EXPONENT = 2
D2D1_DISTANTSPECULAR_PROP_SPECULAR_CONSTANT = 3
D2D1_DISTANTSPECULAR_PROP_SURFACE_SCALE = 4
D2D1_DISTANTSPECULAR_PROP_COLOR = 5
D2D1_DISTANTSPECULAR_PROP_KERNEL_UNIT_LENGTH = 6
D2D1_DISTANTSPECULAR_PROP_SCALE_MODE = 7
D2D1_DISTANTSPECULAR_PROP_FORCE_DWORD = 4294967295
D2D1_DISTANTSPECULAR_SCALE_MODE = UInt32
D2D1_DISTANTSPECULAR_SCALE_MODE_NEAREST_NEIGHBOR = 0
D2D1_DISTANTSPECULAR_SCALE_MODE_LINEAR = 1
D2D1_DISTANTSPECULAR_SCALE_MODE_CUBIC = 2
D2D1_DISTANTSPECULAR_SCALE_MODE_MULTI_SAMPLE_LINEAR = 3
D2D1_DISTANTSPECULAR_SCALE_MODE_ANISOTROPIC = 4
D2D1_DISTANTSPECULAR_SCALE_MODE_HIGH_QUALITY_CUBIC = 5
D2D1_DISTANTSPECULAR_SCALE_MODE_FORCE_DWORD = 4294967295
D2D1_POINTDIFFUSE_PROP = UInt32
D2D1_POINTDIFFUSE_PROP_LIGHT_POSITION = 0
D2D1_POINTDIFFUSE_PROP_DIFFUSE_CONSTANT = 1
D2D1_POINTDIFFUSE_PROP_SURFACE_SCALE = 2
D2D1_POINTDIFFUSE_PROP_COLOR = 3
D2D1_POINTDIFFUSE_PROP_KERNEL_UNIT_LENGTH = 4
D2D1_POINTDIFFUSE_PROP_SCALE_MODE = 5
D2D1_POINTDIFFUSE_PROP_FORCE_DWORD = 4294967295
D2D1_POINTDIFFUSE_SCALE_MODE = UInt32
D2D1_POINTDIFFUSE_SCALE_MODE_NEAREST_NEIGHBOR = 0
D2D1_POINTDIFFUSE_SCALE_MODE_LINEAR = 1
D2D1_POINTDIFFUSE_SCALE_MODE_CUBIC = 2
D2D1_POINTDIFFUSE_SCALE_MODE_MULTI_SAMPLE_LINEAR = 3
D2D1_POINTDIFFUSE_SCALE_MODE_ANISOTROPIC = 4
D2D1_POINTDIFFUSE_SCALE_MODE_HIGH_QUALITY_CUBIC = 5
D2D1_POINTDIFFUSE_SCALE_MODE_FORCE_DWORD = 4294967295
D2D1_SPOTDIFFUSE_PROP = UInt32
D2D1_SPOTDIFFUSE_PROP_LIGHT_POSITION = 0
D2D1_SPOTDIFFUSE_PROP_POINTS_AT = 1
D2D1_SPOTDIFFUSE_PROP_FOCUS = 2
D2D1_SPOTDIFFUSE_PROP_LIMITING_CONE_ANGLE = 3
D2D1_SPOTDIFFUSE_PROP_DIFFUSE_CONSTANT = 4
D2D1_SPOTDIFFUSE_PROP_SURFACE_SCALE = 5
D2D1_SPOTDIFFUSE_PROP_COLOR = 6
D2D1_SPOTDIFFUSE_PROP_KERNEL_UNIT_LENGTH = 7
D2D1_SPOTDIFFUSE_PROP_SCALE_MODE = 8
D2D1_SPOTDIFFUSE_PROP_FORCE_DWORD = 4294967295
D2D1_SPOTDIFFUSE_SCALE_MODE = UInt32
D2D1_SPOTDIFFUSE_SCALE_MODE_NEAREST_NEIGHBOR = 0
D2D1_SPOTDIFFUSE_SCALE_MODE_LINEAR = 1
D2D1_SPOTDIFFUSE_SCALE_MODE_CUBIC = 2
D2D1_SPOTDIFFUSE_SCALE_MODE_MULTI_SAMPLE_LINEAR = 3
D2D1_SPOTDIFFUSE_SCALE_MODE_ANISOTROPIC = 4
D2D1_SPOTDIFFUSE_SCALE_MODE_HIGH_QUALITY_CUBIC = 5
D2D1_SPOTDIFFUSE_SCALE_MODE_FORCE_DWORD = 4294967295
D2D1_DISTANTDIFFUSE_PROP = UInt32
D2D1_DISTANTDIFFUSE_PROP_AZIMUTH = 0
D2D1_DISTANTDIFFUSE_PROP_ELEVATION = 1
D2D1_DISTANTDIFFUSE_PROP_DIFFUSE_CONSTANT = 2
D2D1_DISTANTDIFFUSE_PROP_SURFACE_SCALE = 3
D2D1_DISTANTDIFFUSE_PROP_COLOR = 4
D2D1_DISTANTDIFFUSE_PROP_KERNEL_UNIT_LENGTH = 5
D2D1_DISTANTDIFFUSE_PROP_SCALE_MODE = 6
D2D1_DISTANTDIFFUSE_PROP_FORCE_DWORD = 4294967295
D2D1_DISTANTDIFFUSE_SCALE_MODE = UInt32
D2D1_DISTANTDIFFUSE_SCALE_MODE_NEAREST_NEIGHBOR = 0
D2D1_DISTANTDIFFUSE_SCALE_MODE_LINEAR = 1
D2D1_DISTANTDIFFUSE_SCALE_MODE_CUBIC = 2
D2D1_DISTANTDIFFUSE_SCALE_MODE_MULTI_SAMPLE_LINEAR = 3
D2D1_DISTANTDIFFUSE_SCALE_MODE_ANISOTROPIC = 4
D2D1_DISTANTDIFFUSE_SCALE_MODE_HIGH_QUALITY_CUBIC = 5
D2D1_DISTANTDIFFUSE_SCALE_MODE_FORCE_DWORD = 4294967295
D2D1_FLOOD_PROP = UInt32
D2D1_FLOOD_PROP_COLOR = 0
D2D1_FLOOD_PROP_FORCE_DWORD = 4294967295
D2D1_LINEARTRANSFER_PROP = UInt32
D2D1_LINEARTRANSFER_PROP_RED_Y_INTERCEPT = 0
D2D1_LINEARTRANSFER_PROP_RED_SLOPE = 1
D2D1_LINEARTRANSFER_PROP_RED_DISABLE = 2
D2D1_LINEARTRANSFER_PROP_GREEN_Y_INTERCEPT = 3
D2D1_LINEARTRANSFER_PROP_GREEN_SLOPE = 4
D2D1_LINEARTRANSFER_PROP_GREEN_DISABLE = 5
D2D1_LINEARTRANSFER_PROP_BLUE_Y_INTERCEPT = 6
D2D1_LINEARTRANSFER_PROP_BLUE_SLOPE = 7
D2D1_LINEARTRANSFER_PROP_BLUE_DISABLE = 8
D2D1_LINEARTRANSFER_PROP_ALPHA_Y_INTERCEPT = 9
D2D1_LINEARTRANSFER_PROP_ALPHA_SLOPE = 10
D2D1_LINEARTRANSFER_PROP_ALPHA_DISABLE = 11
D2D1_LINEARTRANSFER_PROP_CLAMP_OUTPUT = 12
D2D1_LINEARTRANSFER_PROP_FORCE_DWORD = 4294967295
D2D1_GAMMATRANSFER_PROP = UInt32
D2D1_GAMMATRANSFER_PROP_RED_AMPLITUDE = 0
D2D1_GAMMATRANSFER_PROP_RED_EXPONENT = 1
D2D1_GAMMATRANSFER_PROP_RED_OFFSET = 2
D2D1_GAMMATRANSFER_PROP_RED_DISABLE = 3
D2D1_GAMMATRANSFER_PROP_GREEN_AMPLITUDE = 4
D2D1_GAMMATRANSFER_PROP_GREEN_EXPONENT = 5
D2D1_GAMMATRANSFER_PROP_GREEN_OFFSET = 6
D2D1_GAMMATRANSFER_PROP_GREEN_DISABLE = 7
D2D1_GAMMATRANSFER_PROP_BLUE_AMPLITUDE = 8
D2D1_GAMMATRANSFER_PROP_BLUE_EXPONENT = 9
D2D1_GAMMATRANSFER_PROP_BLUE_OFFSET = 10
D2D1_GAMMATRANSFER_PROP_BLUE_DISABLE = 11
D2D1_GAMMATRANSFER_PROP_ALPHA_AMPLITUDE = 12
D2D1_GAMMATRANSFER_PROP_ALPHA_EXPONENT = 13
D2D1_GAMMATRANSFER_PROP_ALPHA_OFFSET = 14
D2D1_GAMMATRANSFER_PROP_ALPHA_DISABLE = 15
D2D1_GAMMATRANSFER_PROP_CLAMP_OUTPUT = 16
D2D1_GAMMATRANSFER_PROP_FORCE_DWORD = 4294967295
D2D1_TABLETRANSFER_PROP = UInt32
D2D1_TABLETRANSFER_PROP_RED_TABLE = 0
D2D1_TABLETRANSFER_PROP_RED_DISABLE = 1
D2D1_TABLETRANSFER_PROP_GREEN_TABLE = 2
D2D1_TABLETRANSFER_PROP_GREEN_DISABLE = 3
D2D1_TABLETRANSFER_PROP_BLUE_TABLE = 4
D2D1_TABLETRANSFER_PROP_BLUE_DISABLE = 5
D2D1_TABLETRANSFER_PROP_ALPHA_TABLE = 6
D2D1_TABLETRANSFER_PROP_ALPHA_DISABLE = 7
D2D1_TABLETRANSFER_PROP_CLAMP_OUTPUT = 8
D2D1_TABLETRANSFER_PROP_FORCE_DWORD = 4294967295
D2D1_DISCRETETRANSFER_PROP = UInt32
D2D1_DISCRETETRANSFER_PROP_RED_TABLE = 0
D2D1_DISCRETETRANSFER_PROP_RED_DISABLE = 1
D2D1_DISCRETETRANSFER_PROP_GREEN_TABLE = 2
D2D1_DISCRETETRANSFER_PROP_GREEN_DISABLE = 3
D2D1_DISCRETETRANSFER_PROP_BLUE_TABLE = 4
D2D1_DISCRETETRANSFER_PROP_BLUE_DISABLE = 5
D2D1_DISCRETETRANSFER_PROP_ALPHA_TABLE = 6
D2D1_DISCRETETRANSFER_PROP_ALPHA_DISABLE = 7
D2D1_DISCRETETRANSFER_PROP_CLAMP_OUTPUT = 8
D2D1_DISCRETETRANSFER_PROP_FORCE_DWORD = 4294967295
D2D1_CONVOLVEMATRIX_PROP = UInt32
D2D1_CONVOLVEMATRIX_PROP_KERNEL_UNIT_LENGTH = 0
D2D1_CONVOLVEMATRIX_PROP_SCALE_MODE = 1
D2D1_CONVOLVEMATRIX_PROP_KERNEL_SIZE_X = 2
D2D1_CONVOLVEMATRIX_PROP_KERNEL_SIZE_Y = 3
D2D1_CONVOLVEMATRIX_PROP_KERNEL_MATRIX = 4
D2D1_CONVOLVEMATRIX_PROP_DIVISOR = 5
D2D1_CONVOLVEMATRIX_PROP_BIAS = 6
D2D1_CONVOLVEMATRIX_PROP_KERNEL_OFFSET = 7
D2D1_CONVOLVEMATRIX_PROP_PRESERVE_ALPHA = 8
D2D1_CONVOLVEMATRIX_PROP_BORDER_MODE = 9
D2D1_CONVOLVEMATRIX_PROP_CLAMP_OUTPUT = 10
D2D1_CONVOLVEMATRIX_PROP_FORCE_DWORD = 4294967295
D2D1_CONVOLVEMATRIX_SCALE_MODE = UInt32
D2D1_CONVOLVEMATRIX_SCALE_MODE_NEAREST_NEIGHBOR = 0
D2D1_CONVOLVEMATRIX_SCALE_MODE_LINEAR = 1
D2D1_CONVOLVEMATRIX_SCALE_MODE_CUBIC = 2
D2D1_CONVOLVEMATRIX_SCALE_MODE_MULTI_SAMPLE_LINEAR = 3
D2D1_CONVOLVEMATRIX_SCALE_MODE_ANISOTROPIC = 4
D2D1_CONVOLVEMATRIX_SCALE_MODE_HIGH_QUALITY_CUBIC = 5
D2D1_CONVOLVEMATRIX_SCALE_MODE_FORCE_DWORD = 4294967295
D2D1_BRIGHTNESS_PROP = UInt32
D2D1_BRIGHTNESS_PROP_WHITE_POINT = 0
D2D1_BRIGHTNESS_PROP_BLACK_POINT = 1
D2D1_BRIGHTNESS_PROP_FORCE_DWORD = 4294967295
D2D1_ARITHMETICCOMPOSITE_PROP = UInt32
D2D1_ARITHMETICCOMPOSITE_PROP_COEFFICIENTS = 0
D2D1_ARITHMETICCOMPOSITE_PROP_CLAMP_OUTPUT = 1
D2D1_ARITHMETICCOMPOSITE_PROP_FORCE_DWORD = 4294967295
D2D1_CROP_PROP = UInt32
D2D1_CROP_PROP_RECT = 0
D2D1_CROP_PROP_BORDER_MODE = 1
D2D1_CROP_PROP_FORCE_DWORD = 4294967295
D2D1_BORDER_PROP = UInt32
D2D1_BORDER_PROP_EDGE_MODE_X = 0
D2D1_BORDER_PROP_EDGE_MODE_Y = 1
D2D1_BORDER_PROP_FORCE_DWORD = 4294967295
D2D1_BORDER_EDGE_MODE = UInt32
D2D1_BORDER_EDGE_MODE_CLAMP = 0
D2D1_BORDER_EDGE_MODE_WRAP = 1
D2D1_BORDER_EDGE_MODE_MIRROR = 2
D2D1_BORDER_EDGE_MODE_FORCE_DWORD = 4294967295
D2D1_MORPHOLOGY_PROP = UInt32
D2D1_MORPHOLOGY_PROP_MODE = 0
D2D1_MORPHOLOGY_PROP_WIDTH = 1
D2D1_MORPHOLOGY_PROP_HEIGHT = 2
D2D1_MORPHOLOGY_PROP_FORCE_DWORD = 4294967295
D2D1_MORPHOLOGY_MODE = UInt32
D2D1_MORPHOLOGY_MODE_ERODE = 0
D2D1_MORPHOLOGY_MODE_DILATE = 1
D2D1_MORPHOLOGY_MODE_FORCE_DWORD = 4294967295
D2D1_TILE_PROP = UInt32
D2D1_TILE_PROP_RECT = 0
D2D1_TILE_PROP_FORCE_DWORD = 4294967295
D2D1_ATLAS_PROP = UInt32
D2D1_ATLAS_PROP_INPUT_RECT = 0
D2D1_ATLAS_PROP_INPUT_PADDING_RECT = 1
D2D1_ATLAS_PROP_FORCE_DWORD = 4294967295
D2D1_OPACITYMETADATA_PROP = UInt32
D2D1_OPACITYMETADATA_PROP_INPUT_OPAQUE_RECT = 0
D2D1_OPACITYMETADATA_PROP_FORCE_DWORD = 4294967295
def _define_PD2D1_EFFECT_FACTORY():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)
D2D1_PROPERTY_TYPE = UInt32
D2D1_PROPERTY_TYPE_UNKNOWN = 0
D2D1_PROPERTY_TYPE_STRING = 1
D2D1_PROPERTY_TYPE_BOOL = 2
D2D1_PROPERTY_TYPE_UINT32 = 3
D2D1_PROPERTY_TYPE_INT32 = 4
D2D1_PROPERTY_TYPE_FLOAT = 5
D2D1_PROPERTY_TYPE_VECTOR2 = 6
D2D1_PROPERTY_TYPE_VECTOR3 = 7
D2D1_PROPERTY_TYPE_VECTOR4 = 8
D2D1_PROPERTY_TYPE_BLOB = 9
D2D1_PROPERTY_TYPE_IUNKNOWN = 10
D2D1_PROPERTY_TYPE_ENUM = 11
D2D1_PROPERTY_TYPE_ARRAY = 12
D2D1_PROPERTY_TYPE_CLSID = 13
D2D1_PROPERTY_TYPE_MATRIX_3X2 = 14
D2D1_PROPERTY_TYPE_MATRIX_4X3 = 15
D2D1_PROPERTY_TYPE_MATRIX_4X4 = 16
D2D1_PROPERTY_TYPE_MATRIX_5X4 = 17
D2D1_PROPERTY_TYPE_COLOR_CONTEXT = 18
D2D1_PROPERTY_TYPE_FORCE_DWORD = 4294967295
D2D1_PROPERTY = UInt32
D2D1_PROPERTY_CLSID = 2147483648
D2D1_PROPERTY_DISPLAYNAME = 2147483649
D2D1_PROPERTY_AUTHOR = 2147483650
D2D1_PROPERTY_CATEGORY = 2147483651
D2D1_PROPERTY_DESCRIPTION = 2147483652
D2D1_PROPERTY_INPUTS = 2147483653
D2D1_PROPERTY_CACHED = 2147483654
D2D1_PROPERTY_PRECISION = 2147483655
D2D1_PROPERTY_MIN_INPUTS = 2147483656
D2D1_PROPERTY_MAX_INPUTS = 2147483657
D2D1_PROPERTY_FORCE_DWORD = 4294967295
D2D1_SUBPROPERTY = UInt32
D2D1_SUBPROPERTY_DISPLAYNAME = 2147483648
D2D1_SUBPROPERTY_ISREADONLY = 2147483649
D2D1_SUBPROPERTY_MIN = 2147483650
D2D1_SUBPROPERTY_MAX = 2147483651
D2D1_SUBPROPERTY_DEFAULT = 2147483652
D2D1_SUBPROPERTY_FIELDS = 2147483653
D2D1_SUBPROPERTY_INDEX = 2147483654
D2D1_SUBPROPERTY_FORCE_DWORD = 4294967295
D2D1_BITMAP_OPTIONS = UInt32
D2D1_BITMAP_OPTIONS_NONE = 0
D2D1_BITMAP_OPTIONS_TARGET = 1
D2D1_BITMAP_OPTIONS_CANNOT_DRAW = 2
D2D1_BITMAP_OPTIONS_CPU_READ = 4
D2D1_BITMAP_OPTIONS_GDI_COMPATIBLE = 8
D2D1_BITMAP_OPTIONS_FORCE_DWORD = 4294967295
D2D1_BUFFER_PRECISION = UInt32
D2D1_BUFFER_PRECISION_UNKNOWN = 0
D2D1_BUFFER_PRECISION_8BPC_UNORM = 1
D2D1_BUFFER_PRECISION_8BPC_UNORM_SRGB = 2
D2D1_BUFFER_PRECISION_16BPC_UNORM = 3
D2D1_BUFFER_PRECISION_16BPC_FLOAT = 4
D2D1_BUFFER_PRECISION_32BPC_FLOAT = 5
D2D1_BUFFER_PRECISION_FORCE_DWORD = 4294967295
D2D1_MAP_OPTIONS = UInt32
D2D1_MAP_OPTIONS_NONE = 0
D2D1_MAP_OPTIONS_READ = 1
D2D1_MAP_OPTIONS_WRITE = 2
D2D1_MAP_OPTIONS_DISCARD = 4
D2D1_MAP_OPTIONS_FORCE_DWORD = 4294967295
D2D1_INTERPOLATION_MODE = UInt32
D2D1_INTERPOLATION_MODE_NEAREST_NEIGHBOR = 0
D2D1_INTERPOLATION_MODE_LINEAR = 1
D2D1_INTERPOLATION_MODE_CUBIC = 2
D2D1_INTERPOLATION_MODE_MULTI_SAMPLE_LINEAR = 3
D2D1_INTERPOLATION_MODE_ANISOTROPIC = 4
D2D1_INTERPOLATION_MODE_HIGH_QUALITY_CUBIC = 5
D2D1_INTERPOLATION_MODE_FORCE_DWORD = 4294967295
D2D1_UNIT_MODE = UInt32
D2D1_UNIT_MODE_DIPS = 0
D2D1_UNIT_MODE_PIXELS = 1
D2D1_UNIT_MODE_FORCE_DWORD = 4294967295
D2D1_COLOR_SPACE = UInt32
D2D1_COLOR_SPACE_CUSTOM = 0
D2D1_COLOR_SPACE_SRGB = 1
D2D1_COLOR_SPACE_SCRGB = 2
D2D1_COLOR_SPACE_FORCE_DWORD = 4294967295
D2D1_DEVICE_CONTEXT_OPTIONS = UInt32
D2D1_DEVICE_CONTEXT_OPTIONS_NONE = 0
D2D1_DEVICE_CONTEXT_OPTIONS_ENABLE_MULTITHREADED_OPTIMIZATIONS = 1
D2D1_DEVICE_CONTEXT_OPTIONS_FORCE_DWORD = 4294967295
D2D1_STROKE_TRANSFORM_TYPE = UInt32
D2D1_STROKE_TRANSFORM_TYPE_NORMAL = 0
D2D1_STROKE_TRANSFORM_TYPE_FIXED = 1
D2D1_STROKE_TRANSFORM_TYPE_HAIRLINE = 2
D2D1_STROKE_TRANSFORM_TYPE_FORCE_DWORD = 4294967295
D2D1_PRIMITIVE_BLEND = UInt32
D2D1_PRIMITIVE_BLEND_SOURCE_OVER = 0
D2D1_PRIMITIVE_BLEND_COPY = 1
D2D1_PRIMITIVE_BLEND_MIN = 2
D2D1_PRIMITIVE_BLEND_ADD = 3
D2D1_PRIMITIVE_BLEND_MAX = 4
D2D1_PRIMITIVE_BLEND_FORCE_DWORD = 4294967295
D2D1_THREADING_MODE = UInt32
D2D1_THREADING_MODE_SINGLE_THREADED = 0
D2D1_THREADING_MODE_MULTI_THREADED = 1
D2D1_THREADING_MODE_FORCE_DWORD = 4294967295
D2D1_COLOR_INTERPOLATION_MODE = UInt32
D2D1_COLOR_INTERPOLATION_MODE_STRAIGHT = 0
D2D1_COLOR_INTERPOLATION_MODE_PREMULTIPLIED = 1
D2D1_COLOR_INTERPOLATION_MODE_FORCE_DWORD = 4294967295
def _define_D2D1_BITMAP_PROPERTIES1_head():
    class D2D1_BITMAP_PROPERTIES1(Structure):
        pass
    return D2D1_BITMAP_PROPERTIES1
def _define_D2D1_BITMAP_PROPERTIES1():
    D2D1_BITMAP_PROPERTIES1 = win32more.Graphics.Direct2D.D2D1_BITMAP_PROPERTIES1_head
    D2D1_BITMAP_PROPERTIES1._fields_ = [
        ("pixelFormat", win32more.Graphics.Direct2D.Common.D2D1_PIXEL_FORMAT),
        ("dpiX", Single),
        ("dpiY", Single),
        ("bitmapOptions", win32more.Graphics.Direct2D.D2D1_BITMAP_OPTIONS),
        ("colorContext", win32more.Graphics.Direct2D.ID2D1ColorContext_head),
    ]
    return D2D1_BITMAP_PROPERTIES1
def _define_D2D1_MAPPED_RECT_head():
    class D2D1_MAPPED_RECT(Structure):
        pass
    return D2D1_MAPPED_RECT
def _define_D2D1_MAPPED_RECT():
    D2D1_MAPPED_RECT = win32more.Graphics.Direct2D.D2D1_MAPPED_RECT_head
    D2D1_MAPPED_RECT._fields_ = [
        ("pitch", UInt32),
        ("bits", c_char_p_no),
    ]
    return D2D1_MAPPED_RECT
def _define_D2D1_RENDERING_CONTROLS_head():
    class D2D1_RENDERING_CONTROLS(Structure):
        pass
    return D2D1_RENDERING_CONTROLS
def _define_D2D1_RENDERING_CONTROLS():
    D2D1_RENDERING_CONTROLS = win32more.Graphics.Direct2D.D2D1_RENDERING_CONTROLS_head
    D2D1_RENDERING_CONTROLS._fields_ = [
        ("bufferPrecision", win32more.Graphics.Direct2D.D2D1_BUFFER_PRECISION),
        ("tileSize", win32more.Graphics.Direct2D.Common.D2D_SIZE_U),
    ]
    return D2D1_RENDERING_CONTROLS
def _define_D2D1_EFFECT_INPUT_DESCRIPTION_head():
    class D2D1_EFFECT_INPUT_DESCRIPTION(Structure):
        pass
    return D2D1_EFFECT_INPUT_DESCRIPTION
def _define_D2D1_EFFECT_INPUT_DESCRIPTION():
    D2D1_EFFECT_INPUT_DESCRIPTION = win32more.Graphics.Direct2D.D2D1_EFFECT_INPUT_DESCRIPTION_head
    D2D1_EFFECT_INPUT_DESCRIPTION._fields_ = [
        ("effect", win32more.Graphics.Direct2D.ID2D1Effect_head),
        ("inputIndex", UInt32),
        ("inputRectangle", win32more.Graphics.Direct2D.Common.D2D_RECT_F),
    ]
    return D2D1_EFFECT_INPUT_DESCRIPTION
def _define_D2D1_POINT_DESCRIPTION_head():
    class D2D1_POINT_DESCRIPTION(Structure):
        pass
    return D2D1_POINT_DESCRIPTION
def _define_D2D1_POINT_DESCRIPTION():
    D2D1_POINT_DESCRIPTION = win32more.Graphics.Direct2D.D2D1_POINT_DESCRIPTION_head
    D2D1_POINT_DESCRIPTION._fields_ = [
        ("point", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("unitTangentVector", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("endSegment", UInt32),
        ("endFigure", UInt32),
        ("lengthToEndSegment", Single),
    ]
    return D2D1_POINT_DESCRIPTION
def _define_D2D1_IMAGE_BRUSH_PROPERTIES_head():
    class D2D1_IMAGE_BRUSH_PROPERTIES(Structure):
        pass
    return D2D1_IMAGE_BRUSH_PROPERTIES
def _define_D2D1_IMAGE_BRUSH_PROPERTIES():
    D2D1_IMAGE_BRUSH_PROPERTIES = win32more.Graphics.Direct2D.D2D1_IMAGE_BRUSH_PROPERTIES_head
    D2D1_IMAGE_BRUSH_PROPERTIES._fields_ = [
        ("sourceRectangle", win32more.Graphics.Direct2D.Common.D2D_RECT_F),
        ("extendModeX", win32more.Graphics.Direct2D.D2D1_EXTEND_MODE),
        ("extendModeY", win32more.Graphics.Direct2D.D2D1_EXTEND_MODE),
        ("interpolationMode", win32more.Graphics.Direct2D.D2D1_INTERPOLATION_MODE),
    ]
    return D2D1_IMAGE_BRUSH_PROPERTIES
def _define_D2D1_BITMAP_BRUSH_PROPERTIES1_head():
    class D2D1_BITMAP_BRUSH_PROPERTIES1(Structure):
        pass
    return D2D1_BITMAP_BRUSH_PROPERTIES1
def _define_D2D1_BITMAP_BRUSH_PROPERTIES1():
    D2D1_BITMAP_BRUSH_PROPERTIES1 = win32more.Graphics.Direct2D.D2D1_BITMAP_BRUSH_PROPERTIES1_head
    D2D1_BITMAP_BRUSH_PROPERTIES1._fields_ = [
        ("extendModeX", win32more.Graphics.Direct2D.D2D1_EXTEND_MODE),
        ("extendModeY", win32more.Graphics.Direct2D.D2D1_EXTEND_MODE),
        ("interpolationMode", win32more.Graphics.Direct2D.D2D1_INTERPOLATION_MODE),
    ]
    return D2D1_BITMAP_BRUSH_PROPERTIES1
def _define_D2D1_STROKE_STYLE_PROPERTIES1_head():
    class D2D1_STROKE_STYLE_PROPERTIES1(Structure):
        pass
    return D2D1_STROKE_STYLE_PROPERTIES1
def _define_D2D1_STROKE_STYLE_PROPERTIES1():
    D2D1_STROKE_STYLE_PROPERTIES1 = win32more.Graphics.Direct2D.D2D1_STROKE_STYLE_PROPERTIES1_head
    D2D1_STROKE_STYLE_PROPERTIES1._fields_ = [
        ("startCap", win32more.Graphics.Direct2D.D2D1_CAP_STYLE),
        ("endCap", win32more.Graphics.Direct2D.D2D1_CAP_STYLE),
        ("dashCap", win32more.Graphics.Direct2D.D2D1_CAP_STYLE),
        ("lineJoin", win32more.Graphics.Direct2D.D2D1_LINE_JOIN),
        ("miterLimit", Single),
        ("dashStyle", win32more.Graphics.Direct2D.D2D1_DASH_STYLE),
        ("dashOffset", Single),
        ("transformType", win32more.Graphics.Direct2D.D2D1_STROKE_TRANSFORM_TYPE),
    ]
    return D2D1_STROKE_STYLE_PROPERTIES1
D2D1_LAYER_OPTIONS1 = UInt32
D2D1_LAYER_OPTIONS1_NONE = 0
D2D1_LAYER_OPTIONS1_INITIALIZE_FROM_BACKGROUND = 1
D2D1_LAYER_OPTIONS1_IGNORE_ALPHA = 2
D2D1_LAYER_OPTIONS1_FORCE_DWORD = 4294967295
def _define_D2D1_LAYER_PARAMETERS1_head():
    class D2D1_LAYER_PARAMETERS1(Structure):
        pass
    return D2D1_LAYER_PARAMETERS1
def _define_D2D1_LAYER_PARAMETERS1():
    D2D1_LAYER_PARAMETERS1 = win32more.Graphics.Direct2D.D2D1_LAYER_PARAMETERS1_head
    D2D1_LAYER_PARAMETERS1._fields_ = [
        ("contentBounds", win32more.Graphics.Direct2D.Common.D2D_RECT_F),
        ("geometricMask", win32more.Graphics.Direct2D.ID2D1Geometry_head),
        ("maskAntialiasMode", win32more.Graphics.Direct2D.D2D1_ANTIALIAS_MODE),
        ("maskTransform", win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F),
        ("opacity", Single),
        ("opacityBrush", win32more.Graphics.Direct2D.ID2D1Brush_head),
        ("layerOptions", win32more.Graphics.Direct2D.D2D1_LAYER_OPTIONS1),
    ]
    return D2D1_LAYER_PARAMETERS1
D2D1_PRINT_FONT_SUBSET_MODE = UInt32
D2D1_PRINT_FONT_SUBSET_MODE_DEFAULT = 0
D2D1_PRINT_FONT_SUBSET_MODE_EACHPAGE = 1
D2D1_PRINT_FONT_SUBSET_MODE_NONE = 2
D2D1_PRINT_FONT_SUBSET_MODE_FORCE_DWORD = 4294967295
def _define_D2D1_DRAWING_STATE_DESCRIPTION1_head():
    class D2D1_DRAWING_STATE_DESCRIPTION1(Structure):
        pass
    return D2D1_DRAWING_STATE_DESCRIPTION1
def _define_D2D1_DRAWING_STATE_DESCRIPTION1():
    D2D1_DRAWING_STATE_DESCRIPTION1 = win32more.Graphics.Direct2D.D2D1_DRAWING_STATE_DESCRIPTION1_head
    D2D1_DRAWING_STATE_DESCRIPTION1._fields_ = [
        ("antialiasMode", win32more.Graphics.Direct2D.D2D1_ANTIALIAS_MODE),
        ("textAntialiasMode", win32more.Graphics.Direct2D.D2D1_TEXT_ANTIALIAS_MODE),
        ("tag1", UInt64),
        ("tag2", UInt64),
        ("transform", win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F),
        ("primitiveBlend", win32more.Graphics.Direct2D.D2D1_PRIMITIVE_BLEND),
        ("unitMode", win32more.Graphics.Direct2D.D2D1_UNIT_MODE),
    ]
    return D2D1_DRAWING_STATE_DESCRIPTION1
def _define_D2D1_PRINT_CONTROL_PROPERTIES_head():
    class D2D1_PRINT_CONTROL_PROPERTIES(Structure):
        pass
    return D2D1_PRINT_CONTROL_PROPERTIES
def _define_D2D1_PRINT_CONTROL_PROPERTIES():
    D2D1_PRINT_CONTROL_PROPERTIES = win32more.Graphics.Direct2D.D2D1_PRINT_CONTROL_PROPERTIES_head
    D2D1_PRINT_CONTROL_PROPERTIES._fields_ = [
        ("fontSubset", win32more.Graphics.Direct2D.D2D1_PRINT_FONT_SUBSET_MODE),
        ("rasterDPI", Single),
        ("colorSpace", win32more.Graphics.Direct2D.D2D1_COLOR_SPACE),
    ]
    return D2D1_PRINT_CONTROL_PROPERTIES
def _define_D2D1_CREATION_PROPERTIES_head():
    class D2D1_CREATION_PROPERTIES(Structure):
        pass
    return D2D1_CREATION_PROPERTIES
def _define_D2D1_CREATION_PROPERTIES():
    D2D1_CREATION_PROPERTIES = win32more.Graphics.Direct2D.D2D1_CREATION_PROPERTIES_head
    D2D1_CREATION_PROPERTIES._fields_ = [
        ("threadingMode", win32more.Graphics.Direct2D.D2D1_THREADING_MODE),
        ("debugLevel", win32more.Graphics.Direct2D.D2D1_DEBUG_LEVEL),
        ("options", win32more.Graphics.Direct2D.D2D1_DEVICE_CONTEXT_OPTIONS),
    ]
    return D2D1_CREATION_PROPERTIES
def _define_ID2D1GdiMetafileSink_head():
    class ID2D1GdiMetafileSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('82237326-8111-4f7c-bcf4-b5c1175564fe')
    return ID2D1GdiMetafileSink
def _define_ID2D1GdiMetafileSink():
    ID2D1GdiMetafileSink = win32more.Graphics.Direct2D.ID2D1GdiMetafileSink_head
    ID2D1GdiMetafileSink.ProcessRecord = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p,UInt32, use_last_error=False)(3, 'ProcessRecord', ((1, 'recordType'),(1, 'recordData'),(1, 'recordDataSize'),)))
    return ID2D1GdiMetafileSink
def _define_ID2D1GdiMetafile_head():
    class ID2D1GdiMetafile(win32more.Graphics.Direct2D.ID2D1Resource_head):
        Guid = Guid('2f543dc3-cfc1-4211-864f-cfd91c6f3395')
    return ID2D1GdiMetafile
def _define_ID2D1GdiMetafile():
    ID2D1GdiMetafile = win32more.Graphics.Direct2D.ID2D1GdiMetafile_head
    ID2D1GdiMetafile.Stream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1GdiMetafileSink_head, use_last_error=False)(4, 'Stream', ((1, 'sink'),)))
    ID2D1GdiMetafile.GetBounds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head), use_last_error=False)(5, 'GetBounds', ((1, 'bounds'),)))
    return ID2D1GdiMetafile
def _define_ID2D1CommandSink_head():
    class ID2D1CommandSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('54d7898a-a061-40a7-bec7-e465bcba2c4f')
    return ID2D1CommandSink
def _define_ID2D1CommandSink():
    ID2D1CommandSink = win32more.Graphics.Direct2D.ID2D1CommandSink_head
    ID2D1CommandSink.BeginDraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'BeginDraw', ()))
    ID2D1CommandSink.EndDraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'EndDraw', ()))
    ID2D1CommandSink.SetAntialiasMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.D2D1_ANTIALIAS_MODE, use_last_error=False)(5, 'SetAntialiasMode', ((1, 'antialiasMode'),)))
    ID2D1CommandSink.SetTags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,UInt64, use_last_error=False)(6, 'SetTags', ((1, 'tag1'),(1, 'tag2'),)))
    ID2D1CommandSink.SetTextAntialiasMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.D2D1_TEXT_ANTIALIAS_MODE, use_last_error=False)(7, 'SetTextAntialiasMode', ((1, 'textAntialiasMode'),)))
    ID2D1CommandSink.SetTextRenderingParams = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteRenderingParams_head, use_last_error=False)(8, 'SetTextRenderingParams', ((1, 'textRenderingParams'),)))
    ID2D1CommandSink.SetTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head), use_last_error=False)(9, 'SetTransform', ((1, 'transform'),)))
    ID2D1CommandSink.SetPrimitiveBlend = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.D2D1_PRIMITIVE_BLEND, use_last_error=False)(10, 'SetPrimitiveBlend', ((1, 'primitiveBlend'),)))
    ID2D1CommandSink.SetUnitMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.D2D1_UNIT_MODE, use_last_error=False)(11, 'SetUnitMode', ((1, 'unitMode'),)))
    ID2D1CommandSink.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D1_COLOR_F_head), use_last_error=False)(12, 'Clear', ((1, 'color'),)))
    ID2D1CommandSink.DrawGlyphRun = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.Common.D2D_POINT_2F,POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_RUN_head),POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_RUN_DESCRIPTION_head),win32more.Graphics.Direct2D.ID2D1Brush_head,win32more.Graphics.DirectWrite.DWRITE_MEASURING_MODE, use_last_error=False)(13, 'DrawGlyphRun', ((1, 'baselineOrigin'),(1, 'glyphRun'),(1, 'glyphRunDescription'),(1, 'foregroundBrush'),(1, 'measuringMode'),)))
    ID2D1CommandSink.DrawLine = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.Common.D2D_POINT_2F,win32more.Graphics.Direct2D.Common.D2D_POINT_2F,win32more.Graphics.Direct2D.ID2D1Brush_head,Single,win32more.Graphics.Direct2D.ID2D1StrokeStyle_head, use_last_error=False)(14, 'DrawLine', ((1, 'point0'),(1, 'point1'),(1, 'brush'),(1, 'strokeWidth'),(1, 'strokeStyle'),)))
    ID2D1CommandSink.DrawGeometry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Geometry_head,win32more.Graphics.Direct2D.ID2D1Brush_head,Single,win32more.Graphics.Direct2D.ID2D1StrokeStyle_head, use_last_error=False)(15, 'DrawGeometry', ((1, 'geometry'),(1, 'brush'),(1, 'strokeWidth'),(1, 'strokeStyle'),)))
    ID2D1CommandSink.DrawRectangle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head),win32more.Graphics.Direct2D.ID2D1Brush_head,Single,win32more.Graphics.Direct2D.ID2D1StrokeStyle_head, use_last_error=False)(16, 'DrawRectangle', ((1, 'rect'),(1, 'brush'),(1, 'strokeWidth'),(1, 'strokeStyle'),)))
    ID2D1CommandSink.DrawBitmap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Bitmap_head,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head),Single,win32more.Graphics.Direct2D.D2D1_INTERPOLATION_MODE,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_4X4_F_head), use_last_error=False)(17, 'DrawBitmap', ((1, 'bitmap'),(1, 'destinationRectangle'),(1, 'opacity'),(1, 'interpolationMode'),(1, 'sourceRectangle'),(1, 'perspectiveTransform'),)))
    ID2D1CommandSink.DrawImage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Image_head,POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head),win32more.Graphics.Direct2D.D2D1_INTERPOLATION_MODE,win32more.Graphics.Direct2D.Common.D2D1_COMPOSITE_MODE, use_last_error=False)(18, 'DrawImage', ((1, 'image'),(1, 'targetOffset'),(1, 'imageRectangle'),(1, 'interpolationMode'),(1, 'compositeMode'),)))
    ID2D1CommandSink.DrawGdiMetafile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1GdiMetafile_head,POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2F_head), use_last_error=False)(19, 'DrawGdiMetafile', ((1, 'gdiMetafile'),(1, 'targetOffset'),)))
    ID2D1CommandSink.FillMesh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Mesh_head,win32more.Graphics.Direct2D.ID2D1Brush_head, use_last_error=False)(20, 'FillMesh', ((1, 'mesh'),(1, 'brush'),)))
    ID2D1CommandSink.FillOpacityMask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Bitmap_head,win32more.Graphics.Direct2D.ID2D1Brush_head,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head), use_last_error=False)(21, 'FillOpacityMask', ((1, 'opacityMask'),(1, 'brush'),(1, 'destinationRectangle'),(1, 'sourceRectangle'),)))
    ID2D1CommandSink.FillGeometry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Geometry_head,win32more.Graphics.Direct2D.ID2D1Brush_head,win32more.Graphics.Direct2D.ID2D1Brush_head, use_last_error=False)(22, 'FillGeometry', ((1, 'geometry'),(1, 'brush'),(1, 'opacityBrush'),)))
    ID2D1CommandSink.FillRectangle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head),win32more.Graphics.Direct2D.ID2D1Brush_head, use_last_error=False)(23, 'FillRectangle', ((1, 'rect'),(1, 'brush'),)))
    ID2D1CommandSink.PushAxisAlignedClip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head),win32more.Graphics.Direct2D.D2D1_ANTIALIAS_MODE, use_last_error=False)(24, 'PushAxisAlignedClip', ((1, 'clipRect'),(1, 'antialiasMode'),)))
    ID2D1CommandSink.PushLayer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.D2D1_LAYER_PARAMETERS1_head),win32more.Graphics.Direct2D.ID2D1Layer_head, use_last_error=False)(25, 'PushLayer', ((1, 'layerParameters1'),(1, 'layer'),)))
    ID2D1CommandSink.PopAxisAlignedClip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(26, 'PopAxisAlignedClip', ()))
    ID2D1CommandSink.PopLayer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(27, 'PopLayer', ()))
    return ID2D1CommandSink
def _define_ID2D1CommandList_head():
    class ID2D1CommandList(win32more.Graphics.Direct2D.ID2D1Image_head):
        Guid = Guid('b4f34a19-2383-4d76-94f6-ec343657c3dc')
    return ID2D1CommandList
def _define_ID2D1CommandList():
    ID2D1CommandList = win32more.Graphics.Direct2D.ID2D1CommandList_head
    ID2D1CommandList.Stream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1CommandSink_head, use_last_error=False)(4, 'Stream', ((1, 'sink'),)))
    ID2D1CommandList.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Close', ()))
    return ID2D1CommandList
def _define_ID2D1PrintControl_head():
    class ID2D1PrintControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('2c1d867d-c290-41c8-ae7e-34a98702e9a5')
    return ID2D1PrintControl
def _define_ID2D1PrintControl():
    ID2D1PrintControl = win32more.Graphics.Direct2D.ID2D1PrintControl_head
    ID2D1PrintControl.AddPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1CommandList_head,win32more.Graphics.Direct2D.Common.D2D_SIZE_F,win32more.System.Com.IStream_head,POINTER(UInt64),POINTER(UInt64), use_last_error=False)(3, 'AddPage', ((1, 'commandList'),(1, 'pageSize'),(1, 'pagePrintTicketStream'),(1, 'tag1'),(1, 'tag2'),)))
    ID2D1PrintControl.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Close', ()))
    return ID2D1PrintControl
def _define_ID2D1ImageBrush_head():
    class ID2D1ImageBrush(win32more.Graphics.Direct2D.ID2D1Brush_head):
        Guid = Guid('fe9e984d-3f95-407c-b5db-cb94d4e8f87c')
    return ID2D1ImageBrush
def _define_ID2D1ImageBrush():
    ID2D1ImageBrush = win32more.Graphics.Direct2D.ID2D1ImageBrush_head
    ID2D1ImageBrush.SetImage = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.ID2D1Image_head, use_last_error=False)(8, 'SetImage', ((1, 'image'),)))
    ID2D1ImageBrush.SetExtendModeX = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.D2D1_EXTEND_MODE, use_last_error=False)(9, 'SetExtendModeX', ((1, 'extendModeX'),)))
    ID2D1ImageBrush.SetExtendModeY = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.D2D1_EXTEND_MODE, use_last_error=False)(10, 'SetExtendModeY', ((1, 'extendModeY'),)))
    ID2D1ImageBrush.SetInterpolationMode = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.D2D1_INTERPOLATION_MODE, use_last_error=False)(11, 'SetInterpolationMode', ((1, 'interpolationMode'),)))
    ID2D1ImageBrush.SetSourceRectangle = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head), use_last_error=False)(12, 'SetSourceRectangle', ((1, 'sourceRectangle'),)))
    ID2D1ImageBrush.GetImage = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.ID2D1Image_head), use_last_error=False)(13, 'GetImage', ((1, 'image'),)))
    ID2D1ImageBrush.GetExtendModeX = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_EXTEND_MODE, use_last_error=False)(14, 'GetExtendModeX', ()))
    ID2D1ImageBrush.GetExtendModeY = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_EXTEND_MODE, use_last_error=False)(15, 'GetExtendModeY', ()))
    ID2D1ImageBrush.GetInterpolationMode = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_INTERPOLATION_MODE, use_last_error=False)(16, 'GetInterpolationMode', ()))
    ID2D1ImageBrush.GetSourceRectangle = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head), use_last_error=False)(17, 'GetSourceRectangle', ((1, 'sourceRectangle'),)))
    return ID2D1ImageBrush
def _define_ID2D1BitmapBrush1_head():
    class ID2D1BitmapBrush1(win32more.Graphics.Direct2D.ID2D1BitmapBrush_head):
        Guid = Guid('41343a53-e41a-49a2-91cd-21793bbb62e5')
    return ID2D1BitmapBrush1
def _define_ID2D1BitmapBrush1():
    ID2D1BitmapBrush1 = win32more.Graphics.Direct2D.ID2D1BitmapBrush1_head
    ID2D1BitmapBrush1.SetInterpolationMode1 = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.D2D1_INTERPOLATION_MODE, use_last_error=False)(16, 'SetInterpolationMode1', ((1, 'interpolationMode'),)))
    ID2D1BitmapBrush1.GetInterpolationMode1 = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_INTERPOLATION_MODE, use_last_error=False)(17, 'GetInterpolationMode1', ()))
    return ID2D1BitmapBrush1
def _define_ID2D1StrokeStyle1_head():
    class ID2D1StrokeStyle1(win32more.Graphics.Direct2D.ID2D1StrokeStyle_head):
        Guid = Guid('10a72a66-e91c-43f4-993f-ddf4b82b0b4a')
    return ID2D1StrokeStyle1
def _define_ID2D1StrokeStyle1():
    ID2D1StrokeStyle1 = win32more.Graphics.Direct2D.ID2D1StrokeStyle1_head
    ID2D1StrokeStyle1.GetStrokeTransformType = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_STROKE_TRANSFORM_TYPE, use_last_error=False)(13, 'GetStrokeTransformType', ()))
    return ID2D1StrokeStyle1
def _define_ID2D1PathGeometry1_head():
    class ID2D1PathGeometry1(win32more.Graphics.Direct2D.ID2D1PathGeometry_head):
        Guid = Guid('62baa2d2-ab54-41b7-b872-787e0106a421')
    return ID2D1PathGeometry1
def _define_ID2D1PathGeometry1():
    ID2D1PathGeometry1 = win32more.Graphics.Direct2D.ID2D1PathGeometry1_head
    ID2D1PathGeometry1.ComputePointAndSegmentAtLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,UInt32,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head),Single,POINTER(win32more.Graphics.Direct2D.D2D1_POINT_DESCRIPTION_head), use_last_error=False)(21, 'ComputePointAndSegmentAtLength', ((1, 'length'),(1, 'startSegment'),(1, 'worldTransform'),(1, 'flatteningTolerance'),(1, 'pointDescription'),)))
    return ID2D1PathGeometry1
def _define_ID2D1Properties_head():
    class ID2D1Properties(win32more.System.Com.IUnknown_head):
        Guid = Guid('483473d7-cd46-4f9d-9d3a-3112aa80159d')
    return ID2D1Properties
def _define_ID2D1Properties():
    ID2D1Properties = win32more.Graphics.Direct2D.ID2D1Properties_head
    ID2D1Properties.GetPropertyCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(3, 'GetPropertyCount', ()))
    ID2D1Properties.GetPropertyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Char),UInt32, use_last_error=False)(4, 'GetPropertyName', ((1, 'index'),(1, 'name'),(1, 'nameCount'),)))
    ID2D1Properties.GetPropertyNameLength = COMMETHOD(WINFUNCTYPE(UInt32,UInt32, use_last_error=False)(5, 'GetPropertyNameLength', ((1, 'index'),)))
    ID2D1Properties.GetType = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_PROPERTY_TYPE,UInt32, use_last_error=False)(6, 'GetType', ((1, 'index'),)))
    ID2D1Properties.GetPropertyIndex = COMMETHOD(WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR, use_last_error=False)(7, 'GetPropertyIndex', ((1, 'name'),)))
    ID2D1Properties.SetValueByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Graphics.Direct2D.D2D1_PROPERTY_TYPE,POINTER(Byte),UInt32, use_last_error=False)(8, 'SetValueByName', ((1, 'name'),(1, 'type'),(1, 'data'),(1, 'dataSize'),)))
    ID2D1Properties.SetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Graphics.Direct2D.D2D1_PROPERTY_TYPE,POINTER(Byte),UInt32, use_last_error=False)(9, 'SetValue', ((1, 'index'),(1, 'type'),(1, 'data'),(1, 'dataSize'),)))
    ID2D1Properties.GetValueByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Graphics.Direct2D.D2D1_PROPERTY_TYPE,POINTER(Byte),UInt32, use_last_error=False)(10, 'GetValueByName', ((1, 'name'),(1, 'type'),(1, 'data'),(1, 'dataSize'),)))
    ID2D1Properties.GetValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Graphics.Direct2D.D2D1_PROPERTY_TYPE,POINTER(Byte),UInt32, use_last_error=False)(11, 'GetValue', ((1, 'index'),(1, 'type'),(1, 'data'),(1, 'dataSize'),)))
    ID2D1Properties.GetValueSize = COMMETHOD(WINFUNCTYPE(UInt32,UInt32, use_last_error=False)(12, 'GetValueSize', ((1, 'index'),)))
    ID2D1Properties.GetSubProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Direct2D.ID2D1Properties_head), use_last_error=False)(13, 'GetSubProperties', ((1, 'index'),(1, 'subProperties'),)))
    return ID2D1Properties
def _define_ID2D1Effect_head():
    class ID2D1Effect(win32more.Graphics.Direct2D.ID2D1Properties_head):
        Guid = Guid('28211a43-7d89-476f-8181-2d6159b220ad')
    return ID2D1Effect
def _define_ID2D1Effect():
    ID2D1Effect = win32more.Graphics.Direct2D.ID2D1Effect_head
    ID2D1Effect.SetInput = COMMETHOD(WINFUNCTYPE(Void,UInt32,win32more.Graphics.Direct2D.ID2D1Image_head,win32more.Foundation.BOOL, use_last_error=False)(14, 'SetInput', ((1, 'index'),(1, 'input'),(1, 'invalidate'),)))
    ID2D1Effect.SetInputCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(15, 'SetInputCount', ((1, 'inputCount'),)))
    ID2D1Effect.GetInput = COMMETHOD(WINFUNCTYPE(Void,UInt32,POINTER(win32more.Graphics.Direct2D.ID2D1Image_head), use_last_error=False)(16, 'GetInput', ((1, 'index'),(1, 'input'),)))
    ID2D1Effect.GetInputCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(17, 'GetInputCount', ()))
    ID2D1Effect.GetOutput = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.ID2D1Image_head), use_last_error=False)(18, 'GetOutput', ((1, 'outputImage'),)))
    return ID2D1Effect
def _define_ID2D1Bitmap1_head():
    class ID2D1Bitmap1(win32more.Graphics.Direct2D.ID2D1Bitmap_head):
        Guid = Guid('a898a84c-3873-4588-b08b-ebbf978df041')
    return ID2D1Bitmap1
def _define_ID2D1Bitmap1():
    ID2D1Bitmap1 = win32more.Graphics.Direct2D.ID2D1Bitmap1_head
    ID2D1Bitmap1.GetColorContext = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.ID2D1ColorContext_head), use_last_error=False)(11, 'GetColorContext', ((1, 'colorContext'),)))
    ID2D1Bitmap1.GetOptions = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_BITMAP_OPTIONS, use_last_error=False)(12, 'GetOptions', ()))
    ID2D1Bitmap1.GetSurface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.IDXGISurface_head), use_last_error=False)(13, 'GetSurface', ((1, 'dxgiSurface'),)))
    ID2D1Bitmap1.Map = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.D2D1_MAP_OPTIONS,POINTER(win32more.Graphics.Direct2D.D2D1_MAPPED_RECT_head), use_last_error=False)(14, 'Map', ((1, 'options'),(1, 'mappedRect'),)))
    ID2D1Bitmap1.Unmap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(15, 'Unmap', ()))
    return ID2D1Bitmap1
def _define_ID2D1ColorContext_head():
    class ID2D1ColorContext(win32more.Graphics.Direct2D.ID2D1Resource_head):
        Guid = Guid('1c4820bb-5771-4518-a581-2fe4dd0ec657')
    return ID2D1ColorContext
def _define_ID2D1ColorContext():
    ID2D1ColorContext = win32more.Graphics.Direct2D.ID2D1ColorContext_head
    ID2D1ColorContext.GetColorSpace = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_COLOR_SPACE, use_last_error=False)(4, 'GetColorSpace', ()))
    ID2D1ColorContext.GetProfileSize = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(5, 'GetProfileSize', ()))
    ID2D1ColorContext.GetProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32, use_last_error=False)(6, 'GetProfile', ((1, 'profile'),(1, 'profileSize'),)))
    return ID2D1ColorContext
def _define_ID2D1GradientStopCollection1_head():
    class ID2D1GradientStopCollection1(win32more.Graphics.Direct2D.ID2D1GradientStopCollection_head):
        Guid = Guid('ae1572f4-5dd0-4777-998b-9279472ae63b')
    return ID2D1GradientStopCollection1
def _define_ID2D1GradientStopCollection1():
    ID2D1GradientStopCollection1 = win32more.Graphics.Direct2D.ID2D1GradientStopCollection1_head
    ID2D1GradientStopCollection1.GetGradientStops1 = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.D2D1_GRADIENT_STOP),UInt32, use_last_error=False)(8, 'GetGradientStops1', ((1, 'gradientStops'),(1, 'gradientStopsCount'),)))
    ID2D1GradientStopCollection1.GetPreInterpolationSpace = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_COLOR_SPACE, use_last_error=False)(9, 'GetPreInterpolationSpace', ()))
    ID2D1GradientStopCollection1.GetPostInterpolationSpace = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_COLOR_SPACE, use_last_error=False)(10, 'GetPostInterpolationSpace', ()))
    ID2D1GradientStopCollection1.GetBufferPrecision = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_BUFFER_PRECISION, use_last_error=False)(11, 'GetBufferPrecision', ()))
    ID2D1GradientStopCollection1.GetColorInterpolationMode = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_COLOR_INTERPOLATION_MODE, use_last_error=False)(12, 'GetColorInterpolationMode', ()))
    return ID2D1GradientStopCollection1
def _define_ID2D1DrawingStateBlock1_head():
    class ID2D1DrawingStateBlock1(win32more.Graphics.Direct2D.ID2D1DrawingStateBlock_head):
        Guid = Guid('689f1f85-c72e-4e33-8f19-85754efd5ace')
    return ID2D1DrawingStateBlock1
def _define_ID2D1DrawingStateBlock1():
    ID2D1DrawingStateBlock1 = win32more.Graphics.Direct2D.ID2D1DrawingStateBlock1_head
    ID2D1DrawingStateBlock1.GetDescription = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.D2D1_DRAWING_STATE_DESCRIPTION1_head), use_last_error=False)(8, 'GetDescription', ((1, 'stateDescription'),)))
    ID2D1DrawingStateBlock1.SetDescription = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.D2D1_DRAWING_STATE_DESCRIPTION1_head), use_last_error=False)(9, 'SetDescription', ((1, 'stateDescription'),)))
    return ID2D1DrawingStateBlock1
def _define_ID2D1DeviceContext_head():
    class ID2D1DeviceContext(win32more.Graphics.Direct2D.ID2D1RenderTarget_head):
        Guid = Guid('e8f7fe7a-191c-466d-ad95-975678bda998')
    return ID2D1DeviceContext
def _define_ID2D1DeviceContext():
    ID2D1DeviceContext = win32more.Graphics.Direct2D.ID2D1DeviceContext_head
    ID2D1DeviceContext.CreateBitmap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.Common.D2D_SIZE_U,c_void_p,UInt32,POINTER(win32more.Graphics.Direct2D.D2D1_BITMAP_PROPERTIES1_head),POINTER(win32more.Graphics.Direct2D.ID2D1Bitmap1_head), use_last_error=False)(57, 'CreateBitmap', ((1, 'size'),(1, 'sourceData'),(1, 'pitch'),(1, 'bitmapProperties'),(1, 'bitmap'),)))
    ID2D1DeviceContext.CreateBitmapFromWicBitmap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmapSource_head,POINTER(win32more.Graphics.Direct2D.D2D1_BITMAP_PROPERTIES1_head),POINTER(win32more.Graphics.Direct2D.ID2D1Bitmap1_head), use_last_error=False)(58, 'CreateBitmapFromWicBitmap', ((1, 'wicBitmapSource'),(1, 'bitmapProperties'),(1, 'bitmap'),)))
    ID2D1DeviceContext.CreateColorContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.D2D1_COLOR_SPACE,POINTER(Byte),UInt32,POINTER(win32more.Graphics.Direct2D.ID2D1ColorContext_head), use_last_error=False)(59, 'CreateColorContext', ((1, 'space'),(1, 'profile'),(1, 'profileSize'),(1, 'colorContext'),)))
    ID2D1DeviceContext.CreateColorContextFromFilename = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Graphics.Direct2D.ID2D1ColorContext_head), use_last_error=False)(60, 'CreateColorContextFromFilename', ((1, 'filename'),(1, 'colorContext'),)))
    ID2D1DeviceContext.CreateColorContextFromWicColorContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICColorContext_head,POINTER(win32more.Graphics.Direct2D.ID2D1ColorContext_head), use_last_error=False)(61, 'CreateColorContextFromWicColorContext', ((1, 'wicColorContext'),(1, 'colorContext'),)))
    ID2D1DeviceContext.CreateBitmapFromDxgiSurface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGISurface_head,POINTER(win32more.Graphics.Direct2D.D2D1_BITMAP_PROPERTIES1_head),POINTER(win32more.Graphics.Direct2D.ID2D1Bitmap1_head), use_last_error=False)(62, 'CreateBitmapFromDxgiSurface', ((1, 'surface'),(1, 'bitmapProperties'),(1, 'bitmap'),)))
    ID2D1DeviceContext.CreateEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Graphics.Direct2D.ID2D1Effect_head), use_last_error=False)(63, 'CreateEffect', ((1, 'effectId'),(1, 'effect'),)))
    ID2D1DeviceContext.CreateGradientStopCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.D2D1_GRADIENT_STOP),UInt32,win32more.Graphics.Direct2D.D2D1_COLOR_SPACE,win32more.Graphics.Direct2D.D2D1_COLOR_SPACE,win32more.Graphics.Direct2D.D2D1_BUFFER_PRECISION,win32more.Graphics.Direct2D.D2D1_EXTEND_MODE,win32more.Graphics.Direct2D.D2D1_COLOR_INTERPOLATION_MODE,POINTER(win32more.Graphics.Direct2D.ID2D1GradientStopCollection1_head), use_last_error=False)(64, 'CreateGradientStopCollection', ((1, 'straightAlphaGradientStops'),(1, 'straightAlphaGradientStopsCount'),(1, 'preInterpolationSpace'),(1, 'postInterpolationSpace'),(1, 'bufferPrecision'),(1, 'extendMode'),(1, 'colorInterpolationMode'),(1, 'gradientStopCollection1'),)))
    ID2D1DeviceContext.CreateImageBrush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Image_head,POINTER(win32more.Graphics.Direct2D.D2D1_IMAGE_BRUSH_PROPERTIES_head),POINTER(win32more.Graphics.Direct2D.D2D1_BRUSH_PROPERTIES_head),POINTER(win32more.Graphics.Direct2D.ID2D1ImageBrush_head), use_last_error=False)(65, 'CreateImageBrush', ((1, 'image'),(1, 'imageBrushProperties'),(1, 'brushProperties'),(1, 'imageBrush'),)))
    ID2D1DeviceContext.CreateBitmapBrush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Bitmap_head,POINTER(win32more.Graphics.Direct2D.D2D1_BITMAP_BRUSH_PROPERTIES1_head),POINTER(win32more.Graphics.Direct2D.D2D1_BRUSH_PROPERTIES_head),POINTER(win32more.Graphics.Direct2D.ID2D1BitmapBrush1_head), use_last_error=False)(66, 'CreateBitmapBrush', ((1, 'bitmap'),(1, 'bitmapBrushProperties'),(1, 'brushProperties'),(1, 'bitmapBrush'),)))
    ID2D1DeviceContext.CreateCommandList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.ID2D1CommandList_head), use_last_error=False)(67, 'CreateCommandList', ((1, 'commandList'),)))
    ID2D1DeviceContext.IsDxgiFormatSupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Dxgi.Common.DXGI_FORMAT, use_last_error=False)(68, 'IsDxgiFormatSupported', ((1, 'format'),)))
    ID2D1DeviceContext.IsBufferPrecisionSupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Direct2D.D2D1_BUFFER_PRECISION, use_last_error=False)(69, 'IsBufferPrecisionSupported', ((1, 'bufferPrecision'),)))
    ID2D1DeviceContext.GetImageLocalBounds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Image_head,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head), use_last_error=False)(70, 'GetImageLocalBounds', ((1, 'image'),(1, 'localBounds'),)))
    ID2D1DeviceContext.GetImageWorldBounds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Image_head,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head), use_last_error=False)(71, 'GetImageWorldBounds', ((1, 'image'),(1, 'worldBounds'),)))
    ID2D1DeviceContext.GetGlyphRunWorldBounds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.Common.D2D_POINT_2F,POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_RUN_head),win32more.Graphics.DirectWrite.DWRITE_MEASURING_MODE,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head), use_last_error=False)(72, 'GetGlyphRunWorldBounds', ((1, 'baselineOrigin'),(1, 'glyphRun'),(1, 'measuringMode'),(1, 'bounds'),)))
    ID2D1DeviceContext.GetDevice = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.ID2D1Device_head), use_last_error=False)(73, 'GetDevice', ((1, 'device'),)))
    ID2D1DeviceContext.SetTarget = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.ID2D1Image_head, use_last_error=False)(74, 'SetTarget', ((1, 'image'),)))
    ID2D1DeviceContext.GetTarget = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.ID2D1Image_head), use_last_error=False)(75, 'GetTarget', ((1, 'image'),)))
    ID2D1DeviceContext.SetRenderingControls = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.D2D1_RENDERING_CONTROLS_head), use_last_error=False)(76, 'SetRenderingControls', ((1, 'renderingControls'),)))
    ID2D1DeviceContext.GetRenderingControls = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.D2D1_RENDERING_CONTROLS_head), use_last_error=False)(77, 'GetRenderingControls', ((1, 'renderingControls'),)))
    ID2D1DeviceContext.SetPrimitiveBlend = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.D2D1_PRIMITIVE_BLEND, use_last_error=False)(78, 'SetPrimitiveBlend', ((1, 'primitiveBlend'),)))
    ID2D1DeviceContext.GetPrimitiveBlend = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_PRIMITIVE_BLEND, use_last_error=False)(79, 'GetPrimitiveBlend', ()))
    ID2D1DeviceContext.SetUnitMode = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.D2D1_UNIT_MODE, use_last_error=False)(80, 'SetUnitMode', ((1, 'unitMode'),)))
    ID2D1DeviceContext.GetUnitMode = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_UNIT_MODE, use_last_error=False)(81, 'GetUnitMode', ()))
    ID2D1DeviceContext.DrawGlyphRun = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.Common.D2D_POINT_2F,POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_RUN_head),POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_RUN_DESCRIPTION_head),win32more.Graphics.Direct2D.ID2D1Brush_head,win32more.Graphics.DirectWrite.DWRITE_MEASURING_MODE, use_last_error=False)(82, 'DrawGlyphRun', ((1, 'baselineOrigin'),(1, 'glyphRun'),(1, 'glyphRunDescription'),(1, 'foregroundBrush'),(1, 'measuringMode'),)))
    ID2D1DeviceContext.DrawImage = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.ID2D1Image_head,POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head),win32more.Graphics.Direct2D.D2D1_INTERPOLATION_MODE,win32more.Graphics.Direct2D.Common.D2D1_COMPOSITE_MODE, use_last_error=False)(83, 'DrawImage', ((1, 'image'),(1, 'targetOffset'),(1, 'imageRectangle'),(1, 'interpolationMode'),(1, 'compositeMode'),)))
    ID2D1DeviceContext.DrawGdiMetafile = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.ID2D1GdiMetafile_head,POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2F_head), use_last_error=False)(84, 'DrawGdiMetafile', ((1, 'gdiMetafile'),(1, 'targetOffset'),)))
    ID2D1DeviceContext.DrawBitmap = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.ID2D1Bitmap_head,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head),Single,win32more.Graphics.Direct2D.D2D1_INTERPOLATION_MODE,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_4X4_F_head), use_last_error=False)(85, 'DrawBitmap', ((1, 'bitmap'),(1, 'destinationRectangle'),(1, 'opacity'),(1, 'interpolationMode'),(1, 'sourceRectangle'),(1, 'perspectiveTransform'),)))
    ID2D1DeviceContext.PushLayer = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.D2D1_LAYER_PARAMETERS1_head),win32more.Graphics.Direct2D.ID2D1Layer_head, use_last_error=False)(86, 'PushLayer', ((1, 'layerParameters'),(1, 'layer'),)))
    ID2D1DeviceContext.InvalidateEffectInputRectangle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Effect_head,UInt32,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head), use_last_error=False)(87, 'InvalidateEffectInputRectangle', ((1, 'effect'),(1, 'input'),(1, 'inputRectangle'),)))
    ID2D1DeviceContext.GetEffectInvalidRectangleCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Effect_head,POINTER(UInt32), use_last_error=False)(88, 'GetEffectInvalidRectangleCount', ((1, 'effect'),(1, 'rectangleCount'),)))
    ID2D1DeviceContext.GetEffectInvalidRectangles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Effect_head,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F),UInt32, use_last_error=False)(89, 'GetEffectInvalidRectangles', ((1, 'effect'),(1, 'rectangles'),(1, 'rectanglesCount'),)))
    ID2D1DeviceContext.GetEffectRequiredInputRectangles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Effect_head,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head),POINTER(win32more.Graphics.Direct2D.D2D1_EFFECT_INPUT_DESCRIPTION),POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F),UInt32, use_last_error=False)(90, 'GetEffectRequiredInputRectangles', ((1, 'renderEffect'),(1, 'renderImageRectangle'),(1, 'inputDescriptions'),(1, 'requiredInputRects'),(1, 'inputCount'),)))
    ID2D1DeviceContext.FillOpacityMask = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.ID2D1Bitmap_head,win32more.Graphics.Direct2D.ID2D1Brush_head,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head), use_last_error=False)(91, 'FillOpacityMask', ((1, 'opacityMask'),(1, 'brush'),(1, 'destinationRectangle'),(1, 'sourceRectangle'),)))
    return ID2D1DeviceContext
def _define_ID2D1Device_head():
    class ID2D1Device(win32more.Graphics.Direct2D.ID2D1Resource_head):
        Guid = Guid('47dd575d-ac05-4cdd-8049-9b02cd16f44c')
    return ID2D1Device
def _define_ID2D1Device():
    ID2D1Device = win32more.Graphics.Direct2D.ID2D1Device_head
    ID2D1Device.CreateDeviceContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.D2D1_DEVICE_CONTEXT_OPTIONS,POINTER(win32more.Graphics.Direct2D.ID2D1DeviceContext_head), use_last_error=False)(4, 'CreateDeviceContext', ((1, 'options'),(1, 'deviceContext'),)))
    ID2D1Device.CreatePrintControl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICImagingFactory_head,win32more.Storage.Xps.Printing.IPrintDocumentPackageTarget_head,POINTER(win32more.Graphics.Direct2D.D2D1_PRINT_CONTROL_PROPERTIES_head),POINTER(win32more.Graphics.Direct2D.ID2D1PrintControl_head), use_last_error=False)(5, 'CreatePrintControl', ((1, 'wicFactory'),(1, 'documentTarget'),(1, 'printControlProperties'),(1, 'printControl'),)))
    ID2D1Device.SetMaximumTextureMemory = COMMETHOD(WINFUNCTYPE(Void,UInt64, use_last_error=False)(6, 'SetMaximumTextureMemory', ((1, 'maximumInBytes'),)))
    ID2D1Device.GetMaximumTextureMemory = COMMETHOD(WINFUNCTYPE(UInt64, use_last_error=False)(7, 'GetMaximumTextureMemory', ()))
    ID2D1Device.ClearResources = COMMETHOD(WINFUNCTYPE(Void,UInt32, use_last_error=False)(8, 'ClearResources', ((1, 'millisecondsSinceUse'),)))
    return ID2D1Device
def _define_ID2D1Factory1_head():
    class ID2D1Factory1(win32more.Graphics.Direct2D.ID2D1Factory_head):
        Guid = Guid('bb12d362-daee-4b9a-aa1d-14ba401cfa1f')
    return ID2D1Factory1
def _define_ID2D1Factory1():
    ID2D1Factory1 = win32more.Graphics.Direct2D.ID2D1Factory1_head
    ID2D1Factory1.CreateDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGIDevice_head,POINTER(win32more.Graphics.Direct2D.ID2D1Device_head), use_last_error=False)(17, 'CreateDevice', ((1, 'dxgiDevice'),(1, 'd2dDevice'),)))
    ID2D1Factory1.CreateStrokeStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.D2D1_STROKE_STYLE_PROPERTIES1_head),POINTER(Single),UInt32,POINTER(win32more.Graphics.Direct2D.ID2D1StrokeStyle1_head), use_last_error=False)(18, 'CreateStrokeStyle', ((1, 'strokeStyleProperties'),(1, 'dashes'),(1, 'dashesCount'),(1, 'strokeStyle'),)))
    ID2D1Factory1.CreatePathGeometry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.ID2D1PathGeometry1_head), use_last_error=False)(19, 'CreatePathGeometry', ((1, 'pathGeometry'),)))
    ID2D1Factory1.CreateDrawingStateBlock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.D2D1_DRAWING_STATE_DESCRIPTION1_head),win32more.Graphics.DirectWrite.IDWriteRenderingParams_head,POINTER(win32more.Graphics.Direct2D.ID2D1DrawingStateBlock1_head), use_last_error=False)(20, 'CreateDrawingStateBlock', ((1, 'drawingStateDescription'),(1, 'textRenderingParams'),(1, 'drawingStateBlock'),)))
    ID2D1Factory1.CreateGdiMetafile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(win32more.Graphics.Direct2D.ID2D1GdiMetafile_head), use_last_error=False)(21, 'CreateGdiMetafile', ((1, 'metafileStream'),(1, 'metafile'),)))
    ID2D1Factory1.RegisterEffectFromStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IStream_head,POINTER(win32more.Graphics.Direct2D.D2D1_PROPERTY_BINDING),UInt32,win32more.Graphics.Direct2D.PD2D1_EFFECT_FACTORY, use_last_error=False)(22, 'RegisterEffectFromStream', ((1, 'classId'),(1, 'propertyXml'),(1, 'bindings'),(1, 'bindingsCount'),(1, 'effectFactory'),)))
    ID2D1Factory1.RegisterEffectFromString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.PWSTR,POINTER(win32more.Graphics.Direct2D.D2D1_PROPERTY_BINDING),UInt32,win32more.Graphics.Direct2D.PD2D1_EFFECT_FACTORY, use_last_error=False)(23, 'RegisterEffectFromString', ((1, 'classId'),(1, 'propertyXml'),(1, 'bindings'),(1, 'bindingsCount'),(1, 'effectFactory'),)))
    ID2D1Factory1.UnregisterEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(24, 'UnregisterEffect', ((1, 'classId'),)))
    ID2D1Factory1.GetRegisteredEffects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(25, 'GetRegisteredEffects', ((1, 'effects'),(1, 'effectsCount'),(1, 'effectsReturned'),(1, 'effectsRegistered'),)))
    ID2D1Factory1.GetEffectProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Graphics.Direct2D.ID2D1Properties_head), use_last_error=False)(26, 'GetEffectProperties', ((1, 'effectId'),(1, 'properties'),)))
    return ID2D1Factory1
def _define_ID2D1Multithread_head():
    class ID2D1Multithread(win32more.System.Com.IUnknown_head):
        Guid = Guid('31e6e7bc-e0ff-4d46-8c64-a0a8c41c15d3')
    return ID2D1Multithread
def _define_ID2D1Multithread():
    ID2D1Multithread = win32more.Graphics.Direct2D.ID2D1Multithread_head
    ID2D1Multithread.GetMultithreadProtected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(3, 'GetMultithreadProtected', ()))
    ID2D1Multithread.Enter = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(4, 'Enter', ()))
    ID2D1Multithread.Leave = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(5, 'Leave', ()))
    return ID2D1Multithread
def _define_Matrix4x3F_head():
    class Matrix4x3F(Structure):
        pass
    return Matrix4x3F
def _define_Matrix4x3F():
    Matrix4x3F = win32more.Graphics.Direct2D.Matrix4x3F_head
    Matrix4x3F._fields_ = [
        ("__AnonymousBase_d2d1_1helper_L45_C31", win32more.Graphics.Direct2D.Common.D2D_MATRIX_4X3_F),
    ]
    return Matrix4x3F
def _define_Matrix4x4F_head():
    class Matrix4x4F(Structure):
        pass
    return Matrix4x4F
def _define_Matrix4x4F():
    Matrix4x4F = win32more.Graphics.Direct2D.Matrix4x4F_head
    Matrix4x4F._fields_ = [
        ("__AnonymousBase_d2d1_1helper_L97_C31", win32more.Graphics.Direct2D.Common.D2D_MATRIX_4X4_F),
    ]
    return Matrix4x4F
def _define_Matrix5x4F_head():
    class Matrix5x4F(Structure):
        pass
    return Matrix5x4F
def _define_Matrix5x4F():
    Matrix5x4F = win32more.Graphics.Direct2D.Matrix5x4F_head
    Matrix5x4F._fields_ = [
        ("__AnonymousBase_d2d1_1helper_L472_C31", win32more.Graphics.Direct2D.Common.D2D_MATRIX_5X4_F),
    ]
    return Matrix5x4F
def _define_PD2D1_PROPERTY_SET_FUNCTION():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(Byte),UInt32, use_last_error=False)
def _define_PD2D1_PROPERTY_GET_FUNCTION():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(Byte),UInt32,POINTER(UInt32), use_last_error=False)
D2D1_CHANGE_TYPE = UInt32
D2D1_CHANGE_TYPE_NONE = 0
D2D1_CHANGE_TYPE_PROPERTIES = 1
D2D1_CHANGE_TYPE_CONTEXT = 2
D2D1_CHANGE_TYPE_GRAPH = 3
D2D1_CHANGE_TYPE_FORCE_DWORD = 4294967295
D2D1_PIXEL_OPTIONS = UInt32
D2D1_PIXEL_OPTIONS_NONE = 0
D2D1_PIXEL_OPTIONS_TRIVIAL_SAMPLING = 1
D2D1_PIXEL_OPTIONS_FORCE_DWORD = 4294967295
D2D1_VERTEX_OPTIONS = UInt32
D2D1_VERTEX_OPTIONS_NONE = 0
D2D1_VERTEX_OPTIONS_DO_NOT_CLEAR = 1
D2D1_VERTEX_OPTIONS_USE_DEPTH_BUFFER = 2
D2D1_VERTEX_OPTIONS_ASSUME_NO_OVERLAP = 4
D2D1_VERTEX_OPTIONS_FORCE_DWORD = 4294967295
D2D1_VERTEX_USAGE = UInt32
D2D1_VERTEX_USAGE_STATIC = 0
D2D1_VERTEX_USAGE_DYNAMIC = 1
D2D1_VERTEX_USAGE_FORCE_DWORD = 4294967295
D2D1_BLEND_OPERATION = UInt32
D2D1_BLEND_OPERATION_ADD = 1
D2D1_BLEND_OPERATION_SUBTRACT = 2
D2D1_BLEND_OPERATION_REV_SUBTRACT = 3
D2D1_BLEND_OPERATION_MIN = 4
D2D1_BLEND_OPERATION_MAX = 5
D2D1_BLEND_OPERATION_FORCE_DWORD = 4294967295
D2D1_BLEND = UInt32
D2D1_BLEND_ZERO = 1
D2D1_BLEND_ONE = 2
D2D1_BLEND_SRC_COLOR = 3
D2D1_BLEND_INV_SRC_COLOR = 4
D2D1_BLEND_SRC_ALPHA = 5
D2D1_BLEND_INV_SRC_ALPHA = 6
D2D1_BLEND_DEST_ALPHA = 7
D2D1_BLEND_INV_DEST_ALPHA = 8
D2D1_BLEND_DEST_COLOR = 9
D2D1_BLEND_INV_DEST_COLOR = 10
D2D1_BLEND_SRC_ALPHA_SAT = 11
D2D1_BLEND_BLEND_FACTOR = 14
D2D1_BLEND_INV_BLEND_FACTOR = 15
D2D1_BLEND_FORCE_DWORD = 4294967295
D2D1_CHANNEL_DEPTH = UInt32
D2D1_CHANNEL_DEPTH_DEFAULT = 0
D2D1_CHANNEL_DEPTH_1 = 1
D2D1_CHANNEL_DEPTH_4 = 4
D2D1_CHANNEL_DEPTH_FORCE_DWORD = 4294967295
D2D1_FILTER = UInt32
D2D1_FILTER_MIN_MAG_MIP_POINT = 0
D2D1_FILTER_MIN_MAG_POINT_MIP_LINEAR = 1
D2D1_FILTER_MIN_POINT_MAG_LINEAR_MIP_POINT = 4
D2D1_FILTER_MIN_POINT_MAG_MIP_LINEAR = 5
D2D1_FILTER_MIN_LINEAR_MAG_MIP_POINT = 16
D2D1_FILTER_MIN_LINEAR_MAG_POINT_MIP_LINEAR = 17
D2D1_FILTER_MIN_MAG_LINEAR_MIP_POINT = 20
D2D1_FILTER_MIN_MAG_MIP_LINEAR = 21
D2D1_FILTER_ANISOTROPIC = 85
D2D1_FILTER_FORCE_DWORD = 4294967295
D2D1_FEATURE = UInt32
D2D1_FEATURE_DOUBLES = 0
D2D1_FEATURE_D3D10_X_HARDWARE_OPTIONS = 1
D2D1_FEATURE_FORCE_DWORD = 4294967295
def _define_D2D1_PROPERTY_BINDING_head():
    class D2D1_PROPERTY_BINDING(Structure):
        pass
    return D2D1_PROPERTY_BINDING
def _define_D2D1_PROPERTY_BINDING():
    D2D1_PROPERTY_BINDING = win32more.Graphics.Direct2D.D2D1_PROPERTY_BINDING_head
    D2D1_PROPERTY_BINDING._fields_ = [
        ("propertyName", win32more.Foundation.PWSTR),
        ("setFunction", win32more.Graphics.Direct2D.PD2D1_PROPERTY_SET_FUNCTION),
        ("getFunction", win32more.Graphics.Direct2D.PD2D1_PROPERTY_GET_FUNCTION),
    ]
    return D2D1_PROPERTY_BINDING
def _define_D2D1_RESOURCE_TEXTURE_PROPERTIES_head():
    class D2D1_RESOURCE_TEXTURE_PROPERTIES(Structure):
        pass
    return D2D1_RESOURCE_TEXTURE_PROPERTIES
def _define_D2D1_RESOURCE_TEXTURE_PROPERTIES():
    D2D1_RESOURCE_TEXTURE_PROPERTIES = win32more.Graphics.Direct2D.D2D1_RESOURCE_TEXTURE_PROPERTIES_head
    D2D1_RESOURCE_TEXTURE_PROPERTIES._fields_ = [
        ("extents", POINTER(UInt32)),
        ("dimensions", UInt32),
        ("bufferPrecision", win32more.Graphics.Direct2D.D2D1_BUFFER_PRECISION),
        ("channelDepth", win32more.Graphics.Direct2D.D2D1_CHANNEL_DEPTH),
        ("filter", win32more.Graphics.Direct2D.D2D1_FILTER),
        ("extendModes", POINTER(win32more.Graphics.Direct2D.D2D1_EXTEND_MODE)),
    ]
    return D2D1_RESOURCE_TEXTURE_PROPERTIES
def _define_D2D1_INPUT_ELEMENT_DESC_head():
    class D2D1_INPUT_ELEMENT_DESC(Structure):
        pass
    return D2D1_INPUT_ELEMENT_DESC
def _define_D2D1_INPUT_ELEMENT_DESC():
    D2D1_INPUT_ELEMENT_DESC = win32more.Graphics.Direct2D.D2D1_INPUT_ELEMENT_DESC_head
    D2D1_INPUT_ELEMENT_DESC._fields_ = [
        ("semanticName", win32more.Foundation.PSTR),
        ("semanticIndex", UInt32),
        ("format", win32more.Graphics.Dxgi.Common.DXGI_FORMAT),
        ("inputSlot", UInt32),
        ("alignedByteOffset", UInt32),
    ]
    return D2D1_INPUT_ELEMENT_DESC
def _define_D2D1_VERTEX_BUFFER_PROPERTIES_head():
    class D2D1_VERTEX_BUFFER_PROPERTIES(Structure):
        pass
    return D2D1_VERTEX_BUFFER_PROPERTIES
def _define_D2D1_VERTEX_BUFFER_PROPERTIES():
    D2D1_VERTEX_BUFFER_PROPERTIES = win32more.Graphics.Direct2D.D2D1_VERTEX_BUFFER_PROPERTIES_head
    D2D1_VERTEX_BUFFER_PROPERTIES._fields_ = [
        ("inputCount", UInt32),
        ("usage", win32more.Graphics.Direct2D.D2D1_VERTEX_USAGE),
        ("data", c_char_p_no),
        ("byteWidth", UInt32),
    ]
    return D2D1_VERTEX_BUFFER_PROPERTIES
def _define_D2D1_CUSTOM_VERTEX_BUFFER_PROPERTIES_head():
    class D2D1_CUSTOM_VERTEX_BUFFER_PROPERTIES(Structure):
        pass
    return D2D1_CUSTOM_VERTEX_BUFFER_PROPERTIES
def _define_D2D1_CUSTOM_VERTEX_BUFFER_PROPERTIES():
    D2D1_CUSTOM_VERTEX_BUFFER_PROPERTIES = win32more.Graphics.Direct2D.D2D1_CUSTOM_VERTEX_BUFFER_PROPERTIES_head
    D2D1_CUSTOM_VERTEX_BUFFER_PROPERTIES._fields_ = [
        ("shaderBufferWithInputSignature", c_char_p_no),
        ("shaderBufferSize", UInt32),
        ("inputElements", POINTER(win32more.Graphics.Direct2D.D2D1_INPUT_ELEMENT_DESC_head)),
        ("elementCount", UInt32),
        ("stride", UInt32),
    ]
    return D2D1_CUSTOM_VERTEX_BUFFER_PROPERTIES
def _define_D2D1_VERTEX_RANGE_head():
    class D2D1_VERTEX_RANGE(Structure):
        pass
    return D2D1_VERTEX_RANGE
def _define_D2D1_VERTEX_RANGE():
    D2D1_VERTEX_RANGE = win32more.Graphics.Direct2D.D2D1_VERTEX_RANGE_head
    D2D1_VERTEX_RANGE._fields_ = [
        ("startVertex", UInt32),
        ("vertexCount", UInt32),
    ]
    return D2D1_VERTEX_RANGE
def _define_D2D1_BLEND_DESCRIPTION_head():
    class D2D1_BLEND_DESCRIPTION(Structure):
        pass
    return D2D1_BLEND_DESCRIPTION
def _define_D2D1_BLEND_DESCRIPTION():
    D2D1_BLEND_DESCRIPTION = win32more.Graphics.Direct2D.D2D1_BLEND_DESCRIPTION_head
    D2D1_BLEND_DESCRIPTION._fields_ = [
        ("sourceBlend", win32more.Graphics.Direct2D.D2D1_BLEND),
        ("destinationBlend", win32more.Graphics.Direct2D.D2D1_BLEND),
        ("blendOperation", win32more.Graphics.Direct2D.D2D1_BLEND_OPERATION),
        ("sourceBlendAlpha", win32more.Graphics.Direct2D.D2D1_BLEND),
        ("destinationBlendAlpha", win32more.Graphics.Direct2D.D2D1_BLEND),
        ("blendOperationAlpha", win32more.Graphics.Direct2D.D2D1_BLEND_OPERATION),
        ("blendFactor", Single * 4),
    ]
    return D2D1_BLEND_DESCRIPTION
def _define_D2D1_INPUT_DESCRIPTION_head():
    class D2D1_INPUT_DESCRIPTION(Structure):
        pass
    return D2D1_INPUT_DESCRIPTION
def _define_D2D1_INPUT_DESCRIPTION():
    D2D1_INPUT_DESCRIPTION = win32more.Graphics.Direct2D.D2D1_INPUT_DESCRIPTION_head
    D2D1_INPUT_DESCRIPTION._fields_ = [
        ("filter", win32more.Graphics.Direct2D.D2D1_FILTER),
        ("levelOfDetailCount", UInt32),
    ]
    return D2D1_INPUT_DESCRIPTION
def _define_D2D1_FEATURE_DATA_DOUBLES_head():
    class D2D1_FEATURE_DATA_DOUBLES(Structure):
        pass
    return D2D1_FEATURE_DATA_DOUBLES
def _define_D2D1_FEATURE_DATA_DOUBLES():
    D2D1_FEATURE_DATA_DOUBLES = win32more.Graphics.Direct2D.D2D1_FEATURE_DATA_DOUBLES_head
    D2D1_FEATURE_DATA_DOUBLES._fields_ = [
        ("doublePrecisionFloatShaderOps", win32more.Foundation.BOOL),
    ]
    return D2D1_FEATURE_DATA_DOUBLES
def _define_D2D1_FEATURE_DATA_D3D10_X_HARDWARE_OPTIONS_head():
    class D2D1_FEATURE_DATA_D3D10_X_HARDWARE_OPTIONS(Structure):
        pass
    return D2D1_FEATURE_DATA_D3D10_X_HARDWARE_OPTIONS
def _define_D2D1_FEATURE_DATA_D3D10_X_HARDWARE_OPTIONS():
    D2D1_FEATURE_DATA_D3D10_X_HARDWARE_OPTIONS = win32more.Graphics.Direct2D.D2D1_FEATURE_DATA_D3D10_X_HARDWARE_OPTIONS_head
    D2D1_FEATURE_DATA_D3D10_X_HARDWARE_OPTIONS._fields_ = [
        ("computeShaders_Plus_RawAndStructuredBuffers_Via_Shader_4_x", win32more.Foundation.BOOL),
    ]
    return D2D1_FEATURE_DATA_D3D10_X_HARDWARE_OPTIONS
def _define_ID2D1VertexBuffer_head():
    class ID2D1VertexBuffer(win32more.System.Com.IUnknown_head):
        Guid = Guid('9b8b1336-00a5-4668-92b7-ced5d8bf9b7b')
    return ID2D1VertexBuffer
def _define_ID2D1VertexBuffer():
    ID2D1VertexBuffer = win32more.Graphics.Direct2D.ID2D1VertexBuffer_head
    ID2D1VertexBuffer.Map = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_char_p_no),UInt32, use_last_error=False)(3, 'Map', ((1, 'data'),(1, 'bufferSize'),)))
    ID2D1VertexBuffer.Unmap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Unmap', ()))
    return ID2D1VertexBuffer
def _define_ID2D1ResourceTexture_head():
    class ID2D1ResourceTexture(win32more.System.Com.IUnknown_head):
        Guid = Guid('688d15c3-02b0-438d-b13a-d1b44c32c39a')
    return ID2D1ResourceTexture
def _define_ID2D1ResourceTexture():
    ID2D1ResourceTexture = win32more.Graphics.Direct2D.ID2D1ResourceTexture_head
    ID2D1ResourceTexture.Update = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),UInt32,POINTER(Byte),UInt32, use_last_error=False)(3, 'Update', ((1, 'minimumExtents'),(1, 'maximimumExtents'),(1, 'strides'),(1, 'dimensions'),(1, 'data'),(1, 'dataCount'),)))
    return ID2D1ResourceTexture
def _define_ID2D1RenderInfo_head():
    class ID2D1RenderInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('519ae1bd-d19a-420d-b849-364f594776b7')
    return ID2D1RenderInfo
def _define_ID2D1RenderInfo():
    ID2D1RenderInfo = win32more.Graphics.Direct2D.ID2D1RenderInfo_head
    ID2D1RenderInfo.SetInputDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Graphics.Direct2D.D2D1_INPUT_DESCRIPTION, use_last_error=False)(3, 'SetInputDescription', ((1, 'inputIndex'),(1, 'inputDescription'),)))
    ID2D1RenderInfo.SetOutputBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.D2D1_BUFFER_PRECISION,win32more.Graphics.Direct2D.D2D1_CHANNEL_DEPTH, use_last_error=False)(4, 'SetOutputBuffer', ((1, 'bufferPrecision'),(1, 'channelDepth'),)))
    ID2D1RenderInfo.SetCached = COMMETHOD(WINFUNCTYPE(Void,win32more.Foundation.BOOL, use_last_error=False)(5, 'SetCached', ((1, 'isCached'),)))
    ID2D1RenderInfo.SetInstructionCountHint = COMMETHOD(WINFUNCTYPE(Void,UInt32, use_last_error=False)(6, 'SetInstructionCountHint', ((1, 'instructionCount'),)))
    return ID2D1RenderInfo
def _define_ID2D1DrawInfo_head():
    class ID2D1DrawInfo(win32more.Graphics.Direct2D.ID2D1RenderInfo_head):
        Guid = Guid('693ce632-7f2f-45de-93fe-18d88b37aa21')
    return ID2D1DrawInfo
def _define_ID2D1DrawInfo():
    ID2D1DrawInfo = win32more.Graphics.Direct2D.ID2D1DrawInfo_head
    ID2D1DrawInfo.SetPixelShaderConstantBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32, use_last_error=False)(7, 'SetPixelShaderConstantBuffer', ((1, 'buffer'),(1, 'bufferCount'),)))
    ID2D1DrawInfo.SetResourceTexture = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Graphics.Direct2D.ID2D1ResourceTexture_head, use_last_error=False)(8, 'SetResourceTexture', ((1, 'textureIndex'),(1, 'resourceTexture'),)))
    ID2D1DrawInfo.SetVertexShaderConstantBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32, use_last_error=False)(9, 'SetVertexShaderConstantBuffer', ((1, 'buffer'),(1, 'bufferCount'),)))
    ID2D1DrawInfo.SetPixelShader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Graphics.Direct2D.D2D1_PIXEL_OPTIONS, use_last_error=False)(10, 'SetPixelShader', ((1, 'shaderId'),(1, 'pixelOptions'),)))
    ID2D1DrawInfo.SetVertexProcessing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1VertexBuffer_head,win32more.Graphics.Direct2D.D2D1_VERTEX_OPTIONS,POINTER(win32more.Graphics.Direct2D.D2D1_BLEND_DESCRIPTION_head),POINTER(win32more.Graphics.Direct2D.D2D1_VERTEX_RANGE_head),POINTER(Guid), use_last_error=False)(11, 'SetVertexProcessing', ((1, 'vertexBuffer'),(1, 'vertexOptions'),(1, 'blendDescription'),(1, 'vertexRange'),(1, 'vertexShader'),)))
    return ID2D1DrawInfo
def _define_ID2D1ComputeInfo_head():
    class ID2D1ComputeInfo(win32more.Graphics.Direct2D.ID2D1RenderInfo_head):
        Guid = Guid('5598b14b-9fd7-48b7-9bdb-8f0964eb38bc')
    return ID2D1ComputeInfo
def _define_ID2D1ComputeInfo():
    ID2D1ComputeInfo = win32more.Graphics.Direct2D.ID2D1ComputeInfo_head
    ID2D1ComputeInfo.SetComputeShaderConstantBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32, use_last_error=False)(7, 'SetComputeShaderConstantBuffer', ((1, 'buffer'),(1, 'bufferCount'),)))
    ID2D1ComputeInfo.SetComputeShader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(8, 'SetComputeShader', ((1, 'shaderId'),)))
    ID2D1ComputeInfo.SetResourceTexture = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Graphics.Direct2D.ID2D1ResourceTexture_head, use_last_error=False)(9, 'SetResourceTexture', ((1, 'textureIndex'),(1, 'resourceTexture'),)))
    return ID2D1ComputeInfo
def _define_ID2D1TransformNode_head():
    class ID2D1TransformNode(win32more.System.Com.IUnknown_head):
        Guid = Guid('b2efe1e7-729f-4102-949f-505fa21bf666')
    return ID2D1TransformNode
def _define_ID2D1TransformNode():
    ID2D1TransformNode = win32more.Graphics.Direct2D.ID2D1TransformNode_head
    ID2D1TransformNode.GetInputCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(3, 'GetInputCount', ()))
    return ID2D1TransformNode
def _define_ID2D1TransformGraph_head():
    class ID2D1TransformGraph(win32more.System.Com.IUnknown_head):
        Guid = Guid('13d29038-c3e6-4034-9081-13b53a417992')
    return ID2D1TransformGraph
def _define_ID2D1TransformGraph():
    ID2D1TransformGraph = win32more.Graphics.Direct2D.ID2D1TransformGraph_head
    ID2D1TransformGraph.GetInputCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(3, 'GetInputCount', ()))
    ID2D1TransformGraph.SetSingleTransformNode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1TransformNode_head, use_last_error=False)(4, 'SetSingleTransformNode', ((1, 'node'),)))
    ID2D1TransformGraph.AddNode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1TransformNode_head, use_last_error=False)(5, 'AddNode', ((1, 'node'),)))
    ID2D1TransformGraph.RemoveNode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1TransformNode_head, use_last_error=False)(6, 'RemoveNode', ((1, 'node'),)))
    ID2D1TransformGraph.SetOutputNode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1TransformNode_head, use_last_error=False)(7, 'SetOutputNode', ((1, 'node'),)))
    ID2D1TransformGraph.ConnectNode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1TransformNode_head,win32more.Graphics.Direct2D.ID2D1TransformNode_head,UInt32, use_last_error=False)(8, 'ConnectNode', ((1, 'fromNode'),(1, 'toNode'),(1, 'toNodeInputIndex'),)))
    ID2D1TransformGraph.ConnectToEffectInput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Graphics.Direct2D.ID2D1TransformNode_head,UInt32, use_last_error=False)(9, 'ConnectToEffectInput', ((1, 'toEffectInputIndex'),(1, 'node'),(1, 'toNodeInputIndex'),)))
    ID2D1TransformGraph.Clear = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(10, 'Clear', ()))
    ID2D1TransformGraph.SetPassthroughGraph = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(11, 'SetPassthroughGraph', ((1, 'effectInputIndex'),)))
    return ID2D1TransformGraph
def _define_ID2D1Transform_head():
    class ID2D1Transform(win32more.Graphics.Direct2D.ID2D1TransformNode_head):
        Guid = Guid('ef1a287d-342a-4f76-8fdb-da0d6ea9f92b')
    return ID2D1Transform
def _define_ID2D1Transform():
    ID2D1Transform = win32more.Graphics.Direct2D.ID2D1Transform_head
    ID2D1Transform.MapOutputRectToInputRects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.RECT),UInt32, use_last_error=False)(4, 'MapOutputRectToInputRects', ((1, 'outputRect'),(1, 'inputRects'),(1, 'inputRectsCount'),)))
    ID2D1Transform.MapInputRectsToOutputRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT),POINTER(win32more.Foundation.RECT),UInt32,POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.RECT_head), use_last_error=False)(5, 'MapInputRectsToOutputRect', ((1, 'inputRects'),(1, 'inputOpaqueSubRects'),(1, 'inputRectCount'),(1, 'outputRect'),(1, 'outputOpaqueSubRect'),)))
    ID2D1Transform.MapInvalidRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.RECT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(6, 'MapInvalidRect', ((1, 'inputIndex'),(1, 'invalidInputRect'),(1, 'invalidOutputRect'),)))
    return ID2D1Transform
def _define_ID2D1DrawTransform_head():
    class ID2D1DrawTransform(win32more.Graphics.Direct2D.ID2D1Transform_head):
        Guid = Guid('36bfdcb6-9739-435d-a30d-a653beff6a6f')
    return ID2D1DrawTransform
def _define_ID2D1DrawTransform():
    ID2D1DrawTransform = win32more.Graphics.Direct2D.ID2D1DrawTransform_head
    ID2D1DrawTransform.SetDrawInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1DrawInfo_head, use_last_error=False)(7, 'SetDrawInfo', ((1, 'drawInfo'),)))
    return ID2D1DrawTransform
def _define_ID2D1ComputeTransform_head():
    class ID2D1ComputeTransform(win32more.Graphics.Direct2D.ID2D1Transform_head):
        Guid = Guid('0d85573c-01e3-4f7d-bfd9-0d60608bf3c3')
    return ID2D1ComputeTransform
def _define_ID2D1ComputeTransform():
    ID2D1ComputeTransform = win32more.Graphics.Direct2D.ID2D1ComputeTransform_head
    ID2D1ComputeTransform.SetComputeInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1ComputeInfo_head, use_last_error=False)(7, 'SetComputeInfo', ((1, 'computeInfo'),)))
    ID2D1ComputeTransform.CalculateThreadgroups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(8, 'CalculateThreadgroups', ((1, 'outputRect'),(1, 'dimensionX'),(1, 'dimensionY'),(1, 'dimensionZ'),)))
    return ID2D1ComputeTransform
def _define_ID2D1AnalysisTransform_head():
    class ID2D1AnalysisTransform(win32more.System.Com.IUnknown_head):
        Guid = Guid('0359dc30-95e6-4568-9055-27720d130e93')
    return ID2D1AnalysisTransform
def _define_ID2D1AnalysisTransform():
    ID2D1AnalysisTransform = win32more.Graphics.Direct2D.ID2D1AnalysisTransform_head
    ID2D1AnalysisTransform.ProcessAnalysisResults = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32, use_last_error=False)(3, 'ProcessAnalysisResults', ((1, 'analysisData'),(1, 'analysisDataCount'),)))
    return ID2D1AnalysisTransform
def _define_ID2D1SourceTransform_head():
    class ID2D1SourceTransform(win32more.Graphics.Direct2D.ID2D1Transform_head):
        Guid = Guid('db1800dd-0c34-4cf9-be90-31cc0a5653e1')
    return ID2D1SourceTransform
def _define_ID2D1SourceTransform():
    ID2D1SourceTransform = win32more.Graphics.Direct2D.ID2D1SourceTransform_head
    ID2D1SourceTransform.SetRenderInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1RenderInfo_head, use_last_error=False)(7, 'SetRenderInfo', ((1, 'renderInfo'),)))
    ID2D1SourceTransform.Draw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Bitmap1_head,POINTER(win32more.Foundation.RECT_head),win32more.Graphics.Direct2D.Common.D2D_POINT_2U, use_last_error=False)(8, 'Draw', ((1, 'target'),(1, 'drawRect'),(1, 'targetOrigin'),)))
    return ID2D1SourceTransform
def _define_ID2D1ConcreteTransform_head():
    class ID2D1ConcreteTransform(win32more.Graphics.Direct2D.ID2D1TransformNode_head):
        Guid = Guid('1a799d8a-69f7-4e4c-9fed-437ccc6684cc')
    return ID2D1ConcreteTransform
def _define_ID2D1ConcreteTransform():
    ID2D1ConcreteTransform = win32more.Graphics.Direct2D.ID2D1ConcreteTransform_head
    ID2D1ConcreteTransform.SetOutputBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.D2D1_BUFFER_PRECISION,win32more.Graphics.Direct2D.D2D1_CHANNEL_DEPTH, use_last_error=False)(4, 'SetOutputBuffer', ((1, 'bufferPrecision'),(1, 'channelDepth'),)))
    ID2D1ConcreteTransform.SetCached = COMMETHOD(WINFUNCTYPE(Void,win32more.Foundation.BOOL, use_last_error=False)(5, 'SetCached', ((1, 'isCached'),)))
    return ID2D1ConcreteTransform
def _define_ID2D1BlendTransform_head():
    class ID2D1BlendTransform(win32more.Graphics.Direct2D.ID2D1ConcreteTransform_head):
        Guid = Guid('63ac0b32-ba44-450f-8806-7f4ca1ff2f1b')
    return ID2D1BlendTransform
def _define_ID2D1BlendTransform():
    ID2D1BlendTransform = win32more.Graphics.Direct2D.ID2D1BlendTransform_head
    ID2D1BlendTransform.SetDescription = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.D2D1_BLEND_DESCRIPTION_head), use_last_error=False)(6, 'SetDescription', ((1, 'description'),)))
    ID2D1BlendTransform.GetDescription = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.D2D1_BLEND_DESCRIPTION_head), use_last_error=False)(7, 'GetDescription', ((1, 'description'),)))
    return ID2D1BlendTransform
def _define_ID2D1BorderTransform_head():
    class ID2D1BorderTransform(win32more.Graphics.Direct2D.ID2D1ConcreteTransform_head):
        Guid = Guid('4998735c-3a19-473c-9781-656847e3a347')
    return ID2D1BorderTransform
def _define_ID2D1BorderTransform():
    ID2D1BorderTransform = win32more.Graphics.Direct2D.ID2D1BorderTransform_head
    ID2D1BorderTransform.SetExtendModeX = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.D2D1_EXTEND_MODE, use_last_error=False)(6, 'SetExtendModeX', ((1, 'extendMode'),)))
    ID2D1BorderTransform.SetExtendModeY = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.D2D1_EXTEND_MODE, use_last_error=False)(7, 'SetExtendModeY', ((1, 'extendMode'),)))
    ID2D1BorderTransform.GetExtendModeX = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_EXTEND_MODE, use_last_error=False)(8, 'GetExtendModeX', ()))
    ID2D1BorderTransform.GetExtendModeY = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_EXTEND_MODE, use_last_error=False)(9, 'GetExtendModeY', ()))
    return ID2D1BorderTransform
def _define_ID2D1OffsetTransform_head():
    class ID2D1OffsetTransform(win32more.Graphics.Direct2D.ID2D1TransformNode_head):
        Guid = Guid('3fe6adea-7643-4f53-bd14-a0ce63f24042')
    return ID2D1OffsetTransform
def _define_ID2D1OffsetTransform():
    ID2D1OffsetTransform = win32more.Graphics.Direct2D.ID2D1OffsetTransform_head
    ID2D1OffsetTransform.SetOffset = COMMETHOD(WINFUNCTYPE(Void,win32more.Foundation.POINT, use_last_error=False)(4, 'SetOffset', ((1, 'offset'),)))
    ID2D1OffsetTransform.GetOffset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.POINT, use_last_error=False)(5, 'GetOffset', ()))
    return ID2D1OffsetTransform
def _define_ID2D1BoundsAdjustmentTransform_head():
    class ID2D1BoundsAdjustmentTransform(win32more.Graphics.Direct2D.ID2D1TransformNode_head):
        Guid = Guid('90f732e2-5092-4606-a819-8651970baccd')
    return ID2D1BoundsAdjustmentTransform
def _define_ID2D1BoundsAdjustmentTransform():
    ID2D1BoundsAdjustmentTransform = win32more.Graphics.Direct2D.ID2D1BoundsAdjustmentTransform_head
    ID2D1BoundsAdjustmentTransform.SetOutputBounds = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(4, 'SetOutputBounds', ((1, 'outputBounds'),)))
    ID2D1BoundsAdjustmentTransform.GetOutputBounds = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(5, 'GetOutputBounds', ((1, 'outputBounds'),)))
    return ID2D1BoundsAdjustmentTransform
def _define_ID2D1EffectImpl_head():
    class ID2D1EffectImpl(win32more.System.Com.IUnknown_head):
        Guid = Guid('a248fd3f-3e6c-4e63-9f03-7f68ecc91db9')
    return ID2D1EffectImpl
def _define_ID2D1EffectImpl():
    ID2D1EffectImpl = win32more.Graphics.Direct2D.ID2D1EffectImpl_head
    ID2D1EffectImpl.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1EffectContext_head,win32more.Graphics.Direct2D.ID2D1TransformGraph_head, use_last_error=False)(3, 'Initialize', ((1, 'effectContext'),(1, 'transformGraph'),)))
    ID2D1EffectImpl.PrepareForRender = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.D2D1_CHANGE_TYPE, use_last_error=False)(4, 'PrepareForRender', ((1, 'changeType'),)))
    ID2D1EffectImpl.SetGraph = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1TransformGraph_head, use_last_error=False)(5, 'SetGraph', ((1, 'transformGraph'),)))
    return ID2D1EffectImpl
def _define_ID2D1EffectContext_head():
    class ID2D1EffectContext(win32more.System.Com.IUnknown_head):
        Guid = Guid('3d9f916b-27dc-4ad7-b4f1-64945340f563')
    return ID2D1EffectContext
def _define_ID2D1EffectContext():
    ID2D1EffectContext = win32more.Graphics.Direct2D.ID2D1EffectContext_head
    ID2D1EffectContext.GetDpi = COMMETHOD(WINFUNCTYPE(Void,POINTER(Single),POINTER(Single), use_last_error=False)(3, 'GetDpi', ((1, 'dpiX'),(1, 'dpiY'),)))
    ID2D1EffectContext.CreateEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Graphics.Direct2D.ID2D1Effect_head), use_last_error=False)(4, 'CreateEffect', ((1, 'effectId'),(1, 'effect'),)))
    ID2D1EffectContext.GetMaximumSupportedFeatureLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D.D3D_FEATURE_LEVEL),UInt32,POINTER(win32more.Graphics.Direct3D.D3D_FEATURE_LEVEL), use_last_error=False)(5, 'GetMaximumSupportedFeatureLevel', ((1, 'featureLevels'),(1, 'featureLevelsCount'),(1, 'maximumSupportedFeatureLevel'),)))
    ID2D1EffectContext.CreateTransformNodeFromEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Effect_head,POINTER(win32more.Graphics.Direct2D.ID2D1TransformNode_head), use_last_error=False)(6, 'CreateTransformNodeFromEffect', ((1, 'effect'),(1, 'transformNode'),)))
    ID2D1EffectContext.CreateBlendTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Direct2D.D2D1_BLEND_DESCRIPTION_head),POINTER(win32more.Graphics.Direct2D.ID2D1BlendTransform_head), use_last_error=False)(7, 'CreateBlendTransform', ((1, 'numInputs'),(1, 'blendDescription'),(1, 'transform'),)))
    ID2D1EffectContext.CreateBorderTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.D2D1_EXTEND_MODE,win32more.Graphics.Direct2D.D2D1_EXTEND_MODE,POINTER(win32more.Graphics.Direct2D.ID2D1BorderTransform_head), use_last_error=False)(8, 'CreateBorderTransform', ((1, 'extendModeX'),(1, 'extendModeY'),(1, 'transform'),)))
    ID2D1EffectContext.CreateOffsetTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.POINT,POINTER(win32more.Graphics.Direct2D.ID2D1OffsetTransform_head), use_last_error=False)(9, 'CreateOffsetTransform', ((1, 'offset'),(1, 'transform'),)))
    ID2D1EffectContext.CreateBoundsAdjustmentTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Graphics.Direct2D.ID2D1BoundsAdjustmentTransform_head), use_last_error=False)(10, 'CreateBoundsAdjustmentTransform', ((1, 'outputRectangle'),(1, 'transform'),)))
    ID2D1EffectContext.LoadPixelShader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Byte),UInt32, use_last_error=False)(11, 'LoadPixelShader', ((1, 'shaderId'),(1, 'shaderBuffer'),(1, 'shaderBufferCount'),)))
    ID2D1EffectContext.LoadVertexShader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Byte),UInt32, use_last_error=False)(12, 'LoadVertexShader', ((1, 'resourceId'),(1, 'shaderBuffer'),(1, 'shaderBufferCount'),)))
    ID2D1EffectContext.LoadComputeShader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Byte),UInt32, use_last_error=False)(13, 'LoadComputeShader', ((1, 'resourceId'),(1, 'shaderBuffer'),(1, 'shaderBufferCount'),)))
    ID2D1EffectContext.IsShaderLoaded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(Guid), use_last_error=False)(14, 'IsShaderLoaded', ((1, 'shaderId'),)))
    ID2D1EffectContext.CreateResourceTexture = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Graphics.Direct2D.D2D1_RESOURCE_TEXTURE_PROPERTIES_head),POINTER(Byte),POINTER(UInt32),UInt32,POINTER(win32more.Graphics.Direct2D.ID2D1ResourceTexture_head), use_last_error=False)(15, 'CreateResourceTexture', ((1, 'resourceId'),(1, 'resourceTextureProperties'),(1, 'data'),(1, 'strides'),(1, 'dataSize'),(1, 'resourceTexture'),)))
    ID2D1EffectContext.FindResourceTexture = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Graphics.Direct2D.ID2D1ResourceTexture_head), use_last_error=False)(16, 'FindResourceTexture', ((1, 'resourceId'),(1, 'resourceTexture'),)))
    ID2D1EffectContext.CreateVertexBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.D2D1_VERTEX_BUFFER_PROPERTIES_head),POINTER(Guid),POINTER(win32more.Graphics.Direct2D.D2D1_CUSTOM_VERTEX_BUFFER_PROPERTIES_head),POINTER(win32more.Graphics.Direct2D.ID2D1VertexBuffer_head), use_last_error=False)(17, 'CreateVertexBuffer', ((1, 'vertexBufferProperties'),(1, 'resourceId'),(1, 'customVertexBufferProperties'),(1, 'buffer'),)))
    ID2D1EffectContext.FindVertexBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Graphics.Direct2D.ID2D1VertexBuffer_head), use_last_error=False)(18, 'FindVertexBuffer', ((1, 'resourceId'),(1, 'buffer'),)))
    ID2D1EffectContext.CreateColorContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.D2D1_COLOR_SPACE,POINTER(Byte),UInt32,POINTER(win32more.Graphics.Direct2D.ID2D1ColorContext_head), use_last_error=False)(19, 'CreateColorContext', ((1, 'space'),(1, 'profile'),(1, 'profileSize'),(1, 'colorContext'),)))
    ID2D1EffectContext.CreateColorContextFromFilename = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Graphics.Direct2D.ID2D1ColorContext_head), use_last_error=False)(20, 'CreateColorContextFromFilename', ((1, 'filename'),(1, 'colorContext'),)))
    ID2D1EffectContext.CreateColorContextFromWicColorContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICColorContext_head,POINTER(win32more.Graphics.Direct2D.ID2D1ColorContext_head), use_last_error=False)(21, 'CreateColorContextFromWicColorContext', ((1, 'wicColorContext'),(1, 'colorContext'),)))
    ID2D1EffectContext.CheckFeatureSupport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.D2D1_FEATURE,c_void_p,UInt32, use_last_error=False)(22, 'CheckFeatureSupport', ((1, 'feature'),(1, 'featureSupportData'),(1, 'featureSupportDataSize'),)))
    ID2D1EffectContext.IsBufferPrecisionSupported = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Direct2D.D2D1_BUFFER_PRECISION, use_last_error=False)(23, 'IsBufferPrecisionSupported', ((1, 'bufferPrecision'),)))
    return ID2D1EffectContext
D2D1_YCBCR_PROP = UInt32
D2D1_YCBCR_PROP_CHROMA_SUBSAMPLING = 0
D2D1_YCBCR_PROP_TRANSFORM_MATRIX = 1
D2D1_YCBCR_PROP_INTERPOLATION_MODE = 2
D2D1_YCBCR_PROP_FORCE_DWORD = 4294967295
D2D1_YCBCR_CHROMA_SUBSAMPLING = UInt32
D2D1_YCBCR_CHROMA_SUBSAMPLING_AUTO = 0
D2D1_YCBCR_CHROMA_SUBSAMPLING_420 = 1
D2D1_YCBCR_CHROMA_SUBSAMPLING_422 = 2
D2D1_YCBCR_CHROMA_SUBSAMPLING_444 = 3
D2D1_YCBCR_CHROMA_SUBSAMPLING_440 = 4
D2D1_YCBCR_CHROMA_SUBSAMPLING_FORCE_DWORD = 4294967295
D2D1_YCBCR_INTERPOLATION_MODE = UInt32
D2D1_YCBCR_INTERPOLATION_MODE_NEAREST_NEIGHBOR = 0
D2D1_YCBCR_INTERPOLATION_MODE_LINEAR = 1
D2D1_YCBCR_INTERPOLATION_MODE_CUBIC = 2
D2D1_YCBCR_INTERPOLATION_MODE_MULTI_SAMPLE_LINEAR = 3
D2D1_YCBCR_INTERPOLATION_MODE_ANISOTROPIC = 4
D2D1_YCBCR_INTERPOLATION_MODE_HIGH_QUALITY_CUBIC = 5
D2D1_YCBCR_INTERPOLATION_MODE_FORCE_DWORD = 4294967295
D2D1_CONTRAST_PROP = UInt32
D2D1_CONTRAST_PROP_CONTRAST = 0
D2D1_CONTRAST_PROP_CLAMP_INPUT = 1
D2D1_CONTRAST_PROP_FORCE_DWORD = 4294967295
D2D1_RGBTOHUE_PROP = UInt32
D2D1_RGBTOHUE_PROP_OUTPUT_COLOR_SPACE = 0
D2D1_RGBTOHUE_PROP_FORCE_DWORD = 4294967295
D2D1_RGBTOHUE_OUTPUT_COLOR_SPACE = UInt32
D2D1_RGBTOHUE_OUTPUT_COLOR_SPACE_HUE_SATURATION_VALUE = 0
D2D1_RGBTOHUE_OUTPUT_COLOR_SPACE_HUE_SATURATION_LIGHTNESS = 1
D2D1_RGBTOHUE_OUTPUT_COLOR_SPACE_FORCE_DWORD = 4294967295
D2D1_HUETORGB_PROP = UInt32
D2D1_HUETORGB_PROP_INPUT_COLOR_SPACE = 0
D2D1_HUETORGB_PROP_FORCE_DWORD = 4294967295
D2D1_HUETORGB_INPUT_COLOR_SPACE = UInt32
D2D1_HUETORGB_INPUT_COLOR_SPACE_HUE_SATURATION_VALUE = 0
D2D1_HUETORGB_INPUT_COLOR_SPACE_HUE_SATURATION_LIGHTNESS = 1
D2D1_HUETORGB_INPUT_COLOR_SPACE_FORCE_DWORD = 4294967295
D2D1_CHROMAKEY_PROP = UInt32
D2D1_CHROMAKEY_PROP_COLOR = 0
D2D1_CHROMAKEY_PROP_TOLERANCE = 1
D2D1_CHROMAKEY_PROP_INVERT_ALPHA = 2
D2D1_CHROMAKEY_PROP_FEATHER = 3
D2D1_CHROMAKEY_PROP_FORCE_DWORD = 4294967295
D2D1_EMBOSS_PROP = UInt32
D2D1_EMBOSS_PROP_HEIGHT = 0
D2D1_EMBOSS_PROP_DIRECTION = 1
D2D1_EMBOSS_PROP_FORCE_DWORD = 4294967295
D2D1_EXPOSURE_PROP = UInt32
D2D1_EXPOSURE_PROP_EXPOSURE_VALUE = 0
D2D1_EXPOSURE_PROP_FORCE_DWORD = 4294967295
D2D1_POSTERIZE_PROP = UInt32
D2D1_POSTERIZE_PROP_RED_VALUE_COUNT = 0
D2D1_POSTERIZE_PROP_GREEN_VALUE_COUNT = 1
D2D1_POSTERIZE_PROP_BLUE_VALUE_COUNT = 2
D2D1_POSTERIZE_PROP_FORCE_DWORD = 4294967295
D2D1_SEPIA_PROP = UInt32
D2D1_SEPIA_PROP_INTENSITY = 0
D2D1_SEPIA_PROP_ALPHA_MODE = 1
D2D1_SEPIA_PROP_FORCE_DWORD = 4294967295
D2D1_SHARPEN_PROP = UInt32
D2D1_SHARPEN_PROP_SHARPNESS = 0
D2D1_SHARPEN_PROP_THRESHOLD = 1
D2D1_SHARPEN_PROP_FORCE_DWORD = 4294967295
D2D1_STRAIGHTEN_PROP = UInt32
D2D1_STRAIGHTEN_PROP_ANGLE = 0
D2D1_STRAIGHTEN_PROP_MAINTAIN_SIZE = 1
D2D1_STRAIGHTEN_PROP_SCALE_MODE = 2
D2D1_STRAIGHTEN_PROP_FORCE_DWORD = 4294967295
D2D1_STRAIGHTEN_SCALE_MODE = UInt32
D2D1_STRAIGHTEN_SCALE_MODE_NEAREST_NEIGHBOR = 0
D2D1_STRAIGHTEN_SCALE_MODE_LINEAR = 1
D2D1_STRAIGHTEN_SCALE_MODE_CUBIC = 2
D2D1_STRAIGHTEN_SCALE_MODE_MULTI_SAMPLE_LINEAR = 3
D2D1_STRAIGHTEN_SCALE_MODE_ANISOTROPIC = 4
D2D1_STRAIGHTEN_SCALE_MODE_FORCE_DWORD = 4294967295
D2D1_TEMPERATUREANDTINT_PROP = UInt32
D2D1_TEMPERATUREANDTINT_PROP_TEMPERATURE = 0
D2D1_TEMPERATUREANDTINT_PROP_TINT = 1
D2D1_TEMPERATUREANDTINT_PROP_FORCE_DWORD = 4294967295
D2D1_VIGNETTE_PROP = UInt32
D2D1_VIGNETTE_PROP_COLOR = 0
D2D1_VIGNETTE_PROP_TRANSITION_SIZE = 1
D2D1_VIGNETTE_PROP_STRENGTH = 2
D2D1_VIGNETTE_PROP_FORCE_DWORD = 4294967295
D2D1_EDGEDETECTION_PROP = UInt32
D2D1_EDGEDETECTION_PROP_STRENGTH = 0
D2D1_EDGEDETECTION_PROP_BLUR_RADIUS = 1
D2D1_EDGEDETECTION_PROP_MODE = 2
D2D1_EDGEDETECTION_PROP_OVERLAY_EDGES = 3
D2D1_EDGEDETECTION_PROP_ALPHA_MODE = 4
D2D1_EDGEDETECTION_PROP_FORCE_DWORD = 4294967295
D2D1_EDGEDETECTION_MODE = UInt32
D2D1_EDGEDETECTION_MODE_SOBEL = 0
D2D1_EDGEDETECTION_MODE_PREWITT = 1
D2D1_EDGEDETECTION_MODE_FORCE_DWORD = 4294967295
D2D1_HIGHLIGHTSANDSHADOWS_PROP = UInt32
D2D1_HIGHLIGHTSANDSHADOWS_PROP_HIGHLIGHTS = 0
D2D1_HIGHLIGHTSANDSHADOWS_PROP_SHADOWS = 1
D2D1_HIGHLIGHTSANDSHADOWS_PROP_CLARITY = 2
D2D1_HIGHLIGHTSANDSHADOWS_PROP_INPUT_GAMMA = 3
D2D1_HIGHLIGHTSANDSHADOWS_PROP_MASK_BLUR_RADIUS = 4
D2D1_HIGHLIGHTSANDSHADOWS_PROP_FORCE_DWORD = 4294967295
D2D1_HIGHLIGHTSANDSHADOWS_INPUT_GAMMA = UInt32
D2D1_HIGHLIGHTSANDSHADOWS_INPUT_GAMMA_LINEAR = 0
D2D1_HIGHLIGHTSANDSHADOWS_INPUT_GAMMA_SRGB = 1
D2D1_HIGHLIGHTSANDSHADOWS_INPUT_GAMMA_FORCE_DWORD = 4294967295
D2D1_LOOKUPTABLE3D_PROP = UInt32
D2D1_LOOKUPTABLE3D_PROP_LUT = 0
D2D1_LOOKUPTABLE3D_PROP_ALPHA_MODE = 1
D2D1_LOOKUPTABLE3D_PROP_FORCE_DWORD = 4294967295
D2D1_OPACITY_PROP = UInt32
D2D1_OPACITY_PROP_OPACITY = 0
D2D1_OPACITY_PROP_FORCE_DWORD = 4294967295
D2D1_CROSSFADE_PROP = UInt32
D2D1_CROSSFADE_PROP_WEIGHT = 0
D2D1_CROSSFADE_PROP_FORCE_DWORD = 4294967295
D2D1_TINT_PROP = UInt32
D2D1_TINT_PROP_COLOR = 0
D2D1_TINT_PROP_CLAMP_OUTPUT = 1
D2D1_TINT_PROP_FORCE_DWORD = 4294967295
D2D1_WHITELEVELADJUSTMENT_PROP = UInt32
D2D1_WHITELEVELADJUSTMENT_PROP_INPUT_WHITE_LEVEL = 0
D2D1_WHITELEVELADJUSTMENT_PROP_OUTPUT_WHITE_LEVEL = 1
D2D1_WHITELEVELADJUSTMENT_PROP_FORCE_DWORD = 4294967295
D2D1_HDRTONEMAP_PROP = UInt32
D2D1_HDRTONEMAP_PROP_INPUT_MAX_LUMINANCE = 0
D2D1_HDRTONEMAP_PROP_OUTPUT_MAX_LUMINANCE = 1
D2D1_HDRTONEMAP_PROP_DISPLAY_MODE = 2
D2D1_HDRTONEMAP_PROP_FORCE_DWORD = 4294967295
D2D1_HDRTONEMAP_DISPLAY_MODE = UInt32
D2D1_HDRTONEMAP_DISPLAY_MODE_SDR = 0
D2D1_HDRTONEMAP_DISPLAY_MODE_HDR = 1
D2D1_HDRTONEMAP_DISPLAY_MODE_FORCE_DWORD = 4294967295
D2D1_RENDERING_PRIORITY = UInt32
D2D1_RENDERING_PRIORITY_NORMAL = 0
D2D1_RENDERING_PRIORITY_LOW = 1
D2D1_RENDERING_PRIORITY_FORCE_DWORD = 4294967295
def _define_ID2D1GeometryRealization_head():
    class ID2D1GeometryRealization(win32more.Graphics.Direct2D.ID2D1Resource_head):
        Guid = Guid('a16907d7-bc02-4801-99e8-8cf7f485f774')
    return ID2D1GeometryRealization
def _define_ID2D1GeometryRealization():
    ID2D1GeometryRealization = win32more.Graphics.Direct2D.ID2D1GeometryRealization_head
    return ID2D1GeometryRealization
def _define_ID2D1DeviceContext1_head():
    class ID2D1DeviceContext1(win32more.Graphics.Direct2D.ID2D1DeviceContext_head):
        Guid = Guid('d37f57e4-6908-459f-a199-e72f24f79987')
    return ID2D1DeviceContext1
def _define_ID2D1DeviceContext1():
    ID2D1DeviceContext1 = win32more.Graphics.Direct2D.ID2D1DeviceContext1_head
    ID2D1DeviceContext1.CreateFilledGeometryRealization = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Geometry_head,Single,POINTER(win32more.Graphics.Direct2D.ID2D1GeometryRealization_head), use_last_error=False)(92, 'CreateFilledGeometryRealization', ((1, 'geometry'),(1, 'flatteningTolerance'),(1, 'geometryRealization'),)))
    ID2D1DeviceContext1.CreateStrokedGeometryRealization = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Geometry_head,Single,Single,win32more.Graphics.Direct2D.ID2D1StrokeStyle_head,POINTER(win32more.Graphics.Direct2D.ID2D1GeometryRealization_head), use_last_error=False)(93, 'CreateStrokedGeometryRealization', ((1, 'geometry'),(1, 'flatteningTolerance'),(1, 'strokeWidth'),(1, 'strokeStyle'),(1, 'geometryRealization'),)))
    ID2D1DeviceContext1.DrawGeometryRealization = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.ID2D1GeometryRealization_head,win32more.Graphics.Direct2D.ID2D1Brush_head, use_last_error=False)(94, 'DrawGeometryRealization', ((1, 'geometryRealization'),(1, 'brush'),)))
    return ID2D1DeviceContext1
def _define_ID2D1Device1_head():
    class ID2D1Device1(win32more.Graphics.Direct2D.ID2D1Device_head):
        Guid = Guid('d21768e1-23a4-4823-a14b-7c3eba85d658')
    return ID2D1Device1
def _define_ID2D1Device1():
    ID2D1Device1 = win32more.Graphics.Direct2D.ID2D1Device1_head
    ID2D1Device1.GetRenderingPriority = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_RENDERING_PRIORITY, use_last_error=False)(9, 'GetRenderingPriority', ()))
    ID2D1Device1.SetRenderingPriority = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.D2D1_RENDERING_PRIORITY, use_last_error=False)(10, 'SetRenderingPriority', ((1, 'renderingPriority'),)))
    ID2D1Device1.CreateDeviceContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.D2D1_DEVICE_CONTEXT_OPTIONS,POINTER(win32more.Graphics.Direct2D.ID2D1DeviceContext1_head), use_last_error=False)(11, 'CreateDeviceContext', ((1, 'options'),(1, 'deviceContext1'),)))
    return ID2D1Device1
def _define_ID2D1Factory2_head():
    class ID2D1Factory2(win32more.Graphics.Direct2D.ID2D1Factory1_head):
        Guid = Guid('94f81a73-9212-4376-9c58-b16a3a0d3992')
    return ID2D1Factory2
def _define_ID2D1Factory2():
    ID2D1Factory2 = win32more.Graphics.Direct2D.ID2D1Factory2_head
    ID2D1Factory2.CreateDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGIDevice_head,POINTER(win32more.Graphics.Direct2D.ID2D1Device1_head), use_last_error=False)(27, 'CreateDevice', ((1, 'dxgiDevice'),(1, 'd2dDevice1'),)))
    return ID2D1Factory2
def _define_ID2D1CommandSink1_head():
    class ID2D1CommandSink1(win32more.Graphics.Direct2D.ID2D1CommandSink_head):
        Guid = Guid('9eb767fd-4269-4467-b8c2-eb30cb305743')
    return ID2D1CommandSink1
def _define_ID2D1CommandSink1():
    ID2D1CommandSink1 = win32more.Graphics.Direct2D.ID2D1CommandSink1_head
    ID2D1CommandSink1.SetPrimitiveBlend1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.D2D1_PRIMITIVE_BLEND, use_last_error=False)(28, 'SetPrimitiveBlend1', ((1, 'primitiveBlend'),)))
    return ID2D1CommandSink1
D2D1_SVG_PAINT_TYPE = UInt32
D2D1_SVG_PAINT_TYPE_NONE = 0
D2D1_SVG_PAINT_TYPE_COLOR = 1
D2D1_SVG_PAINT_TYPE_CURRENT_COLOR = 2
D2D1_SVG_PAINT_TYPE_URI = 3
D2D1_SVG_PAINT_TYPE_URI_NONE = 4
D2D1_SVG_PAINT_TYPE_URI_COLOR = 5
D2D1_SVG_PAINT_TYPE_URI_CURRENT_COLOR = 6
D2D1_SVG_PAINT_TYPE_FORCE_DWORD = 4294967295
D2D1_SVG_LENGTH_UNITS = UInt32
D2D1_SVG_LENGTH_UNITS_NUMBER = 0
D2D1_SVG_LENGTH_UNITS_PERCENTAGE = 1
D2D1_SVG_LENGTH_UNITS_FORCE_DWORD = 4294967295
D2D1_SVG_DISPLAY = UInt32
D2D1_SVG_DISPLAY_INLINE = 0
D2D1_SVG_DISPLAY_NONE = 1
D2D1_SVG_DISPLAY_FORCE_DWORD = 4294967295
D2D1_SVG_VISIBILITY = UInt32
D2D1_SVG_VISIBILITY_VISIBLE = 0
D2D1_SVG_VISIBILITY_HIDDEN = 1
D2D1_SVG_VISIBILITY_FORCE_DWORD = 4294967295
D2D1_SVG_OVERFLOW = UInt32
D2D1_SVG_OVERFLOW_VISIBLE = 0
D2D1_SVG_OVERFLOW_HIDDEN = 1
D2D1_SVG_OVERFLOW_FORCE_DWORD = 4294967295
D2D1_SVG_LINE_CAP = UInt32
D2D1_SVG_LINE_CAP_BUTT = 0
D2D1_SVG_LINE_CAP_SQUARE = 1
D2D1_SVG_LINE_CAP_ROUND = 2
D2D1_SVG_LINE_CAP_FORCE_DWORD = 4294967295
D2D1_SVG_LINE_JOIN = UInt32
D2D1_SVG_LINE_JOIN_BEVEL = 1
D2D1_SVG_LINE_JOIN_MITER = 3
D2D1_SVG_LINE_JOIN_ROUND = 2
D2D1_SVG_LINE_JOIN_FORCE_DWORD = 4294967295
D2D1_SVG_ASPECT_ALIGN = UInt32
D2D1_SVG_ASPECT_ALIGN_NONE = 0
D2D1_SVG_ASPECT_ALIGN_X_MIN_Y_MIN = 1
D2D1_SVG_ASPECT_ALIGN_X_MID_Y_MIN = 2
D2D1_SVG_ASPECT_ALIGN_X_MAX_Y_MIN = 3
D2D1_SVG_ASPECT_ALIGN_X_MIN_Y_MID = 4
D2D1_SVG_ASPECT_ALIGN_X_MID_Y_MID = 5
D2D1_SVG_ASPECT_ALIGN_X_MAX_Y_MID = 6
D2D1_SVG_ASPECT_ALIGN_X_MIN_Y_MAX = 7
D2D1_SVG_ASPECT_ALIGN_X_MID_Y_MAX = 8
D2D1_SVG_ASPECT_ALIGN_X_MAX_Y_MAX = 9
D2D1_SVG_ASPECT_ALIGN_FORCE_DWORD = 4294967295
D2D1_SVG_ASPECT_SCALING = UInt32
D2D1_SVG_ASPECT_SCALING_MEET = 0
D2D1_SVG_ASPECT_SCALING_SLICE = 1
D2D1_SVG_ASPECT_SCALING_FORCE_DWORD = 4294967295
D2D1_SVG_PATH_COMMAND = UInt32
D2D1_SVG_PATH_COMMAND_CLOSE_PATH = 0
D2D1_SVG_PATH_COMMAND_MOVE_ABSOLUTE = 1
D2D1_SVG_PATH_COMMAND_MOVE_RELATIVE = 2
D2D1_SVG_PATH_COMMAND_LINE_ABSOLUTE = 3
D2D1_SVG_PATH_COMMAND_LINE_RELATIVE = 4
D2D1_SVG_PATH_COMMAND_CUBIC_ABSOLUTE = 5
D2D1_SVG_PATH_COMMAND_CUBIC_RELATIVE = 6
D2D1_SVG_PATH_COMMAND_QUADRADIC_ABSOLUTE = 7
D2D1_SVG_PATH_COMMAND_QUADRADIC_RELATIVE = 8
D2D1_SVG_PATH_COMMAND_ARC_ABSOLUTE = 9
D2D1_SVG_PATH_COMMAND_ARC_RELATIVE = 10
D2D1_SVG_PATH_COMMAND_HORIZONTAL_ABSOLUTE = 11
D2D1_SVG_PATH_COMMAND_HORIZONTAL_RELATIVE = 12
D2D1_SVG_PATH_COMMAND_VERTICAL_ABSOLUTE = 13
D2D1_SVG_PATH_COMMAND_VERTICAL_RELATIVE = 14
D2D1_SVG_PATH_COMMAND_CUBIC_SMOOTH_ABSOLUTE = 15
D2D1_SVG_PATH_COMMAND_CUBIC_SMOOTH_RELATIVE = 16
D2D1_SVG_PATH_COMMAND_QUADRADIC_SMOOTH_ABSOLUTE = 17
D2D1_SVG_PATH_COMMAND_QUADRADIC_SMOOTH_RELATIVE = 18
D2D1_SVG_PATH_COMMAND_FORCE_DWORD = 4294967295
D2D1_SVG_UNIT_TYPE = UInt32
D2D1_SVG_UNIT_TYPE_USER_SPACE_ON_USE = 0
D2D1_SVG_UNIT_TYPE_OBJECT_BOUNDING_BOX = 1
D2D1_SVG_UNIT_TYPE_FORCE_DWORD = 4294967295
D2D1_SVG_ATTRIBUTE_STRING_TYPE = UInt32
D2D1_SVG_ATTRIBUTE_STRING_TYPE_SVG = 0
D2D1_SVG_ATTRIBUTE_STRING_TYPE_ID = 1
D2D1_SVG_ATTRIBUTE_STRING_TYPE_FORCE_DWORD = 4294967295
D2D1_SVG_ATTRIBUTE_POD_TYPE = UInt32
D2D1_SVG_ATTRIBUTE_POD_TYPE_FLOAT = 0
D2D1_SVG_ATTRIBUTE_POD_TYPE_COLOR = 1
D2D1_SVG_ATTRIBUTE_POD_TYPE_FILL_MODE = 2
D2D1_SVG_ATTRIBUTE_POD_TYPE_DISPLAY = 3
D2D1_SVG_ATTRIBUTE_POD_TYPE_OVERFLOW = 4
D2D1_SVG_ATTRIBUTE_POD_TYPE_LINE_CAP = 5
D2D1_SVG_ATTRIBUTE_POD_TYPE_LINE_JOIN = 6
D2D1_SVG_ATTRIBUTE_POD_TYPE_VISIBILITY = 7
D2D1_SVG_ATTRIBUTE_POD_TYPE_MATRIX = 8
D2D1_SVG_ATTRIBUTE_POD_TYPE_UNIT_TYPE = 9
D2D1_SVG_ATTRIBUTE_POD_TYPE_EXTEND_MODE = 10
D2D1_SVG_ATTRIBUTE_POD_TYPE_PRESERVE_ASPECT_RATIO = 11
D2D1_SVG_ATTRIBUTE_POD_TYPE_VIEWBOX = 12
D2D1_SVG_ATTRIBUTE_POD_TYPE_LENGTH = 13
D2D1_SVG_ATTRIBUTE_POD_TYPE_FORCE_DWORD = 4294967295
def _define_D2D1_SVG_LENGTH_head():
    class D2D1_SVG_LENGTH(Structure):
        pass
    return D2D1_SVG_LENGTH
def _define_D2D1_SVG_LENGTH():
    D2D1_SVG_LENGTH = win32more.Graphics.Direct2D.D2D1_SVG_LENGTH_head
    D2D1_SVG_LENGTH._fields_ = [
        ("value", Single),
        ("units", win32more.Graphics.Direct2D.D2D1_SVG_LENGTH_UNITS),
    ]
    return D2D1_SVG_LENGTH
def _define_D2D1_SVG_PRESERVE_ASPECT_RATIO_head():
    class D2D1_SVG_PRESERVE_ASPECT_RATIO(Structure):
        pass
    return D2D1_SVG_PRESERVE_ASPECT_RATIO
def _define_D2D1_SVG_PRESERVE_ASPECT_RATIO():
    D2D1_SVG_PRESERVE_ASPECT_RATIO = win32more.Graphics.Direct2D.D2D1_SVG_PRESERVE_ASPECT_RATIO_head
    D2D1_SVG_PRESERVE_ASPECT_RATIO._fields_ = [
        ("defer", win32more.Foundation.BOOL),
        ("align", win32more.Graphics.Direct2D.D2D1_SVG_ASPECT_ALIGN),
        ("meetOrSlice", win32more.Graphics.Direct2D.D2D1_SVG_ASPECT_SCALING),
    ]
    return D2D1_SVG_PRESERVE_ASPECT_RATIO
def _define_D2D1_SVG_VIEWBOX_head():
    class D2D1_SVG_VIEWBOX(Structure):
        pass
    return D2D1_SVG_VIEWBOX
def _define_D2D1_SVG_VIEWBOX():
    D2D1_SVG_VIEWBOX = win32more.Graphics.Direct2D.D2D1_SVG_VIEWBOX_head
    D2D1_SVG_VIEWBOX._fields_ = [
        ("x", Single),
        ("y", Single),
        ("width", Single),
        ("height", Single),
    ]
    return D2D1_SVG_VIEWBOX
def _define_ID2D1SvgAttribute_head():
    class ID2D1SvgAttribute(win32more.Graphics.Direct2D.ID2D1Resource_head):
        Guid = Guid('c9cdb0dd-f8c9-4e70-b7c2-301c80292c5e')
    return ID2D1SvgAttribute
def _define_ID2D1SvgAttribute():
    ID2D1SvgAttribute = win32more.Graphics.Direct2D.ID2D1SvgAttribute_head
    ID2D1SvgAttribute.GetElement = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.ID2D1SvgElement_head), use_last_error=False)(4, 'GetElement', ((1, 'element'),)))
    ID2D1SvgAttribute.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.ID2D1SvgAttribute_head), use_last_error=False)(5, 'Clone', ((1, 'attribute'),)))
    return ID2D1SvgAttribute
def _define_ID2D1SvgPaint_head():
    class ID2D1SvgPaint(win32more.Graphics.Direct2D.ID2D1SvgAttribute_head):
        Guid = Guid('d59bab0a-68a2-455b-a5dc-9eb2854e2490')
    return ID2D1SvgPaint
def _define_ID2D1SvgPaint():
    ID2D1SvgPaint = win32more.Graphics.Direct2D.ID2D1SvgPaint_head
    ID2D1SvgPaint.SetPaintType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.D2D1_SVG_PAINT_TYPE, use_last_error=False)(6, 'SetPaintType', ((1, 'paintType'),)))
    ID2D1SvgPaint.GetPaintType = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_SVG_PAINT_TYPE, use_last_error=False)(7, 'GetPaintType', ()))
    ID2D1SvgPaint.SetColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D1_COLOR_F_head), use_last_error=False)(8, 'SetColor', ((1, 'color'),)))
    ID2D1SvgPaint.GetColor = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.Common.D2D1_COLOR_F_head), use_last_error=False)(9, 'GetColor', ((1, 'color'),)))
    ID2D1SvgPaint.SetId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(10, 'SetId', ((1, 'id'),)))
    ID2D1SvgPaint.GetId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32, use_last_error=False)(11, 'GetId', ((1, 'id'),(1, 'idCount'),)))
    ID2D1SvgPaint.GetIdLength = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(12, 'GetIdLength', ()))
    return ID2D1SvgPaint
def _define_ID2D1SvgStrokeDashArray_head():
    class ID2D1SvgStrokeDashArray(win32more.Graphics.Direct2D.ID2D1SvgAttribute_head):
        Guid = Guid('f1c0ca52-92a3-4f00-b4ce-f35691efd9d9')
    return ID2D1SvgStrokeDashArray
def _define_ID2D1SvgStrokeDashArray():
    ID2D1SvgStrokeDashArray = win32more.Graphics.Direct2D.ID2D1SvgStrokeDashArray_head
    ID2D1SvgStrokeDashArray.RemoveDashesAtEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'RemoveDashesAtEnd', ((1, 'dashesCount'),)))
    ID2D1SvgStrokeDashArray.UpdateDashes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.D2D1_SVG_LENGTH),UInt32,UInt32, use_last_error=False)(7, 'UpdateDashes', ((1, 'dashes'),(1, 'dashesCount'),(1, 'startIndex'),)))
    ID2D1SvgStrokeDashArray.UpdateDashes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single),UInt32,UInt32, use_last_error=False)(8, 'UpdateDashes', ((1, 'dashes'),(1, 'dashesCount'),(1, 'startIndex'),)))
    ID2D1SvgStrokeDashArray.GetDashes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.D2D1_SVG_LENGTH),UInt32,UInt32, use_last_error=False)(9, 'GetDashes', ((1, 'dashes'),(1, 'dashesCount'),(1, 'startIndex'),)))
    ID2D1SvgStrokeDashArray.GetDashes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single),UInt32,UInt32, use_last_error=False)(10, 'GetDashes', ((1, 'dashes'),(1, 'dashesCount'),(1, 'startIndex'),)))
    ID2D1SvgStrokeDashArray.GetDashesCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(11, 'GetDashesCount', ()))
    return ID2D1SvgStrokeDashArray
def _define_ID2D1SvgPointCollection_head():
    class ID2D1SvgPointCollection(win32more.Graphics.Direct2D.ID2D1SvgAttribute_head):
        Guid = Guid('9dbe4c0d-3572-4dd9-9825-5530813bb712')
    return ID2D1SvgPointCollection
def _define_ID2D1SvgPointCollection():
    ID2D1SvgPointCollection = win32more.Graphics.Direct2D.ID2D1SvgPointCollection_head
    ID2D1SvgPointCollection.RemovePointsAtEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'RemovePointsAtEnd', ((1, 'pointsCount'),)))
    ID2D1SvgPointCollection.UpdatePoints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2F),UInt32,UInt32, use_last_error=False)(7, 'UpdatePoints', ((1, 'points'),(1, 'pointsCount'),(1, 'startIndex'),)))
    ID2D1SvgPointCollection.GetPoints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2F),UInt32,UInt32, use_last_error=False)(8, 'GetPoints', ((1, 'points'),(1, 'pointsCount'),(1, 'startIndex'),)))
    ID2D1SvgPointCollection.GetPointsCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(9, 'GetPointsCount', ()))
    return ID2D1SvgPointCollection
def _define_ID2D1SvgPathData_head():
    class ID2D1SvgPathData(win32more.Graphics.Direct2D.ID2D1SvgAttribute_head):
        Guid = Guid('c095e4f4-bb98-43d6-9745-4d1b84ec9888')
    return ID2D1SvgPathData
def _define_ID2D1SvgPathData():
    ID2D1SvgPathData = win32more.Graphics.Direct2D.ID2D1SvgPathData_head
    ID2D1SvgPathData.RemoveSegmentDataAtEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'RemoveSegmentDataAtEnd', ((1, 'dataCount'),)))
    ID2D1SvgPathData.UpdateSegmentData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single),UInt32,UInt32, use_last_error=False)(7, 'UpdateSegmentData', ((1, 'data'),(1, 'dataCount'),(1, 'startIndex'),)))
    ID2D1SvgPathData.GetSegmentData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single),UInt32,UInt32, use_last_error=False)(8, 'GetSegmentData', ((1, 'data'),(1, 'dataCount'),(1, 'startIndex'),)))
    ID2D1SvgPathData.GetSegmentDataCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(9, 'GetSegmentDataCount', ()))
    ID2D1SvgPathData.RemoveCommandsAtEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(10, 'RemoveCommandsAtEnd', ((1, 'commandsCount'),)))
    ID2D1SvgPathData.UpdateCommands = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.D2D1_SVG_PATH_COMMAND),UInt32,UInt32, use_last_error=False)(11, 'UpdateCommands', ((1, 'commands'),(1, 'commandsCount'),(1, 'startIndex'),)))
    ID2D1SvgPathData.GetCommands = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.D2D1_SVG_PATH_COMMAND),UInt32,UInt32, use_last_error=False)(12, 'GetCommands', ((1, 'commands'),(1, 'commandsCount'),(1, 'startIndex'),)))
    ID2D1SvgPathData.GetCommandsCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(13, 'GetCommandsCount', ()))
    ID2D1SvgPathData.CreatePathGeometry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.Common.D2D1_FILL_MODE,POINTER(win32more.Graphics.Direct2D.ID2D1PathGeometry1_head), use_last_error=False)(14, 'CreatePathGeometry', ((1, 'fillMode'),(1, 'pathGeometry'),)))
    return ID2D1SvgPathData
def _define_ID2D1SvgElement_head():
    class ID2D1SvgElement(win32more.Graphics.Direct2D.ID2D1Resource_head):
        Guid = Guid('ac7b67a6-183e-49c1-a823-0ebe40b0db29')
    return ID2D1SvgElement
def _define_ID2D1SvgElement():
    ID2D1SvgElement = win32more.Graphics.Direct2D.ID2D1SvgElement_head
    ID2D1SvgElement.GetDocument = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.ID2D1SvgDocument_head), use_last_error=False)(4, 'GetDocument', ((1, 'document'),)))
    ID2D1SvgElement.GetTagName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32, use_last_error=False)(5, 'GetTagName', ((1, 'name'),(1, 'nameCount'),)))
    ID2D1SvgElement.GetTagNameLength = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(6, 'GetTagNameLength', ()))
    ID2D1SvgElement.IsTextContent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(7, 'IsTextContent', ()))
    ID2D1SvgElement.GetParent = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.ID2D1SvgElement_head), use_last_error=False)(8, 'GetParent', ((1, 'parent'),)))
    ID2D1SvgElement.HasChildren = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(9, 'HasChildren', ()))
    ID2D1SvgElement.GetFirstChild = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.ID2D1SvgElement_head), use_last_error=False)(10, 'GetFirstChild', ((1, 'child'),)))
    ID2D1SvgElement.GetLastChild = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.ID2D1SvgElement_head), use_last_error=False)(11, 'GetLastChild', ((1, 'child'),)))
    ID2D1SvgElement.GetPreviousChild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1SvgElement_head,POINTER(win32more.Graphics.Direct2D.ID2D1SvgElement_head), use_last_error=False)(12, 'GetPreviousChild', ((1, 'referenceChild'),(1, 'previousChild'),)))
    ID2D1SvgElement.GetNextChild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1SvgElement_head,POINTER(win32more.Graphics.Direct2D.ID2D1SvgElement_head), use_last_error=False)(13, 'GetNextChild', ((1, 'referenceChild'),(1, 'nextChild'),)))
    ID2D1SvgElement.InsertChildBefore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1SvgElement_head,win32more.Graphics.Direct2D.ID2D1SvgElement_head, use_last_error=False)(14, 'InsertChildBefore', ((1, 'newChild'),(1, 'referenceChild'),)))
    ID2D1SvgElement.AppendChild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1SvgElement_head, use_last_error=False)(15, 'AppendChild', ((1, 'newChild'),)))
    ID2D1SvgElement.ReplaceChild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1SvgElement_head,win32more.Graphics.Direct2D.ID2D1SvgElement_head, use_last_error=False)(16, 'ReplaceChild', ((1, 'newChild'),(1, 'oldChild'),)))
    ID2D1SvgElement.RemoveChild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1SvgElement_head, use_last_error=False)(17, 'RemoveChild', ((1, 'oldChild'),)))
    ID2D1SvgElement.CreateChild = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Graphics.Direct2D.ID2D1SvgElement_head), use_last_error=False)(18, 'CreateChild', ((1, 'tagName'),(1, 'newChild'),)))
    ID2D1SvgElement.IsAttributeSpecified = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BOOL), use_last_error=False)(19, 'IsAttributeSpecified', ((1, 'name'),(1, 'inherited'),)))
    ID2D1SvgElement.GetSpecifiedAttributeCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(20, 'GetSpecifiedAttributeCount', ()))
    ID2D1SvgElement.GetSpecifiedAttributeName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Char),UInt32,POINTER(win32more.Foundation.BOOL), use_last_error=False)(21, 'GetSpecifiedAttributeName', ((1, 'index'),(1, 'name'),(1, 'nameCount'),(1, 'inherited'),)))
    ID2D1SvgElement.GetSpecifiedAttributeNameLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(win32more.Foundation.BOOL), use_last_error=False)(22, 'GetSpecifiedAttributeNameLength', ((1, 'index'),(1, 'nameLength'),(1, 'inherited'),)))
    ID2D1SvgElement.RemoveAttribute = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(23, 'RemoveAttribute', ((1, 'name'),)))
    ID2D1SvgElement.SetTextValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32, use_last_error=False)(24, 'SetTextValue', ((1, 'name'),(1, 'nameCount'),)))
    ID2D1SvgElement.GetTextValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32, use_last_error=False)(25, 'GetTextValue', ((1, 'name'),(1, 'nameCount'),)))
    ID2D1SvgElement.GetTextValueLength = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(26, 'GetTextValueLength', ()))
    ID2D1SvgElement.SetAttributeValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Graphics.Direct2D.ID2D1SvgAttribute_head, use_last_error=False)(27, 'SetAttributeValue', ((1, 'name'),(1, 'value'),)))
    ID2D1SvgElement.SetAttributeValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Graphics.Direct2D.D2D1_SVG_ATTRIBUTE_POD_TYPE,c_void_p,UInt32, use_last_error=False)(28, 'SetAttributeValue', ((1, 'name'),(1, 'type'),(1, 'value'),(1, 'valueSizeInBytes'),)))
    ID2D1SvgElement.SetAttributeValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Graphics.Direct2D.D2D1_SVG_ATTRIBUTE_STRING_TYPE,win32more.Foundation.PWSTR, use_last_error=False)(29, 'SetAttributeValue', ((1, 'name'),(1, 'type'),(1, 'value'),)))
    ID2D1SvgElement.GetAttributeValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(30, 'GetAttributeValue', ((1, 'name'),(1, 'riid'),(1, 'value'),)))
    ID2D1SvgElement.GetAttributeValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Graphics.Direct2D.D2D1_SVG_ATTRIBUTE_POD_TYPE,c_void_p,UInt32, use_last_error=False)(31, 'GetAttributeValue', ((1, 'name'),(1, 'type'),(1, 'value'),(1, 'valueSizeInBytes'),)))
    ID2D1SvgElement.GetAttributeValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Graphics.Direct2D.D2D1_SVG_ATTRIBUTE_STRING_TYPE,POINTER(Char),UInt32, use_last_error=False)(32, 'GetAttributeValue', ((1, 'name'),(1, 'type'),(1, 'value'),(1, 'valueCount'),)))
    ID2D1SvgElement.GetAttributeValueLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Graphics.Direct2D.D2D1_SVG_ATTRIBUTE_STRING_TYPE,POINTER(UInt32), use_last_error=False)(33, 'GetAttributeValueLength', ((1, 'name'),(1, 'type'),(1, 'valueLength'),)))
    return ID2D1SvgElement
def _define_ID2D1SvgDocument_head():
    class ID2D1SvgDocument(win32more.Graphics.Direct2D.ID2D1Resource_head):
        Guid = Guid('86b88e4d-afa4-4d7b-88e4-68a51c4a0aec')
    return ID2D1SvgDocument
def _define_ID2D1SvgDocument():
    ID2D1SvgDocument = win32more.Graphics.Direct2D.ID2D1SvgDocument_head
    ID2D1SvgDocument.SetViewportSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.Common.D2D_SIZE_F, use_last_error=False)(4, 'SetViewportSize', ((1, 'viewportSize'),)))
    ID2D1SvgDocument.GetViewportSize = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.Common.D2D_SIZE_F, use_last_error=False)(5, 'GetViewportSize', ()))
    ID2D1SvgDocument.SetRoot = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1SvgElement_head, use_last_error=False)(6, 'SetRoot', ((1, 'root'),)))
    ID2D1SvgDocument.GetRoot = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.ID2D1SvgElement_head), use_last_error=False)(7, 'GetRoot', ((1, 'root'),)))
    ID2D1SvgDocument.FindElementById = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Graphics.Direct2D.ID2D1SvgElement_head), use_last_error=False)(8, 'FindElementById', ((1, 'id'),(1, 'svgElement'),)))
    ID2D1SvgDocument.Serialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Graphics.Direct2D.ID2D1SvgElement_head, use_last_error=False)(9, 'Serialize', ((1, 'outputXmlStream'),(1, 'subtree'),)))
    ID2D1SvgDocument.Deserialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(win32more.Graphics.Direct2D.ID2D1SvgElement_head), use_last_error=False)(10, 'Deserialize', ((1, 'inputXmlStream'),(1, 'subtree'),)))
    ID2D1SvgDocument.CreatePaint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.D2D1_SVG_PAINT_TYPE,POINTER(win32more.Graphics.Direct2D.Common.D2D1_COLOR_F_head),win32more.Foundation.PWSTR,POINTER(win32more.Graphics.Direct2D.ID2D1SvgPaint_head), use_last_error=False)(11, 'CreatePaint', ((1, 'paintType'),(1, 'color'),(1, 'id'),(1, 'paint'),)))
    ID2D1SvgDocument.CreateStrokeDashArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.D2D1_SVG_LENGTH),UInt32,POINTER(win32more.Graphics.Direct2D.ID2D1SvgStrokeDashArray_head), use_last_error=False)(12, 'CreateStrokeDashArray', ((1, 'dashes'),(1, 'dashesCount'),(1, 'strokeDashArray'),)))
    ID2D1SvgDocument.CreatePointCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2F),UInt32,POINTER(win32more.Graphics.Direct2D.ID2D1SvgPointCollection_head), use_last_error=False)(13, 'CreatePointCollection', ((1, 'points'),(1, 'pointsCount'),(1, 'pointCollection'),)))
    ID2D1SvgDocument.CreatePathData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single),UInt32,POINTER(win32more.Graphics.Direct2D.D2D1_SVG_PATH_COMMAND),UInt32,POINTER(win32more.Graphics.Direct2D.ID2D1SvgPathData_head), use_last_error=False)(14, 'CreatePathData', ((1, 'segmentData'),(1, 'segmentDataCount'),(1, 'commands'),(1, 'commandsCount'),(1, 'pathData'),)))
    return ID2D1SvgDocument
D2D1_INK_NIB_SHAPE = UInt32
D2D1_INK_NIB_SHAPE_ROUND = 0
D2D1_INK_NIB_SHAPE_SQUARE = 1
D2D1_INK_NIB_SHAPE_FORCE_DWORD = 4294967295
D2D1_ORIENTATION = UInt32
D2D1_ORIENTATION_DEFAULT = 1
D2D1_ORIENTATION_FLIP_HORIZONTAL = 2
D2D1_ORIENTATION_ROTATE_CLOCKWISE180 = 3
D2D1_ORIENTATION_ROTATE_CLOCKWISE180_FLIP_HORIZONTAL = 4
D2D1_ORIENTATION_ROTATE_CLOCKWISE90_FLIP_HORIZONTAL = 5
D2D1_ORIENTATION_ROTATE_CLOCKWISE270 = 6
D2D1_ORIENTATION_ROTATE_CLOCKWISE270_FLIP_HORIZONTAL = 7
D2D1_ORIENTATION_ROTATE_CLOCKWISE90 = 8
D2D1_ORIENTATION_FORCE_DWORD = 4294967295
D2D1_IMAGE_SOURCE_LOADING_OPTIONS = UInt32
D2D1_IMAGE_SOURCE_LOADING_OPTIONS_NONE = 0
D2D1_IMAGE_SOURCE_LOADING_OPTIONS_RELEASE_SOURCE = 1
D2D1_IMAGE_SOURCE_LOADING_OPTIONS_CACHE_ON_DEMAND = 2
D2D1_IMAGE_SOURCE_LOADING_OPTIONS_FORCE_DWORD = 4294967295
D2D1_IMAGE_SOURCE_FROM_DXGI_OPTIONS = UInt32
D2D1_IMAGE_SOURCE_FROM_DXGI_OPTIONS_NONE = 0
D2D1_IMAGE_SOURCE_FROM_DXGI_OPTIONS_LOW_QUALITY_PRIMARY_CONVERSION = 1
D2D1_IMAGE_SOURCE_FROM_DXGI_OPTIONS_FORCE_DWORD = 4294967295
D2D1_TRANSFORMED_IMAGE_SOURCE_OPTIONS = UInt32
D2D1_TRANSFORMED_IMAGE_SOURCE_OPTIONS_NONE = 0
D2D1_TRANSFORMED_IMAGE_SOURCE_OPTIONS_DISABLE_DPI_SCALE = 1
D2D1_TRANSFORMED_IMAGE_SOURCE_OPTIONS_FORCE_DWORD = 4294967295
def _define_D2D1_TRANSFORMED_IMAGE_SOURCE_PROPERTIES_head():
    class D2D1_TRANSFORMED_IMAGE_SOURCE_PROPERTIES(Structure):
        pass
    return D2D1_TRANSFORMED_IMAGE_SOURCE_PROPERTIES
def _define_D2D1_TRANSFORMED_IMAGE_SOURCE_PROPERTIES():
    D2D1_TRANSFORMED_IMAGE_SOURCE_PROPERTIES = win32more.Graphics.Direct2D.D2D1_TRANSFORMED_IMAGE_SOURCE_PROPERTIES_head
    D2D1_TRANSFORMED_IMAGE_SOURCE_PROPERTIES._fields_ = [
        ("orientation", win32more.Graphics.Direct2D.D2D1_ORIENTATION),
        ("scaleX", Single),
        ("scaleY", Single),
        ("interpolationMode", win32more.Graphics.Direct2D.D2D1_INTERPOLATION_MODE),
        ("options", win32more.Graphics.Direct2D.D2D1_TRANSFORMED_IMAGE_SOURCE_OPTIONS),
    ]
    return D2D1_TRANSFORMED_IMAGE_SOURCE_PROPERTIES
def _define_D2D1_INK_POINT_head():
    class D2D1_INK_POINT(Structure):
        pass
    return D2D1_INK_POINT
def _define_D2D1_INK_POINT():
    D2D1_INK_POINT = win32more.Graphics.Direct2D.D2D1_INK_POINT_head
    D2D1_INK_POINT._fields_ = [
        ("x", Single),
        ("y", Single),
        ("radius", Single),
    ]
    return D2D1_INK_POINT
def _define_D2D1_INK_BEZIER_SEGMENT_head():
    class D2D1_INK_BEZIER_SEGMENT(Structure):
        pass
    return D2D1_INK_BEZIER_SEGMENT
def _define_D2D1_INK_BEZIER_SEGMENT():
    D2D1_INK_BEZIER_SEGMENT = win32more.Graphics.Direct2D.D2D1_INK_BEZIER_SEGMENT_head
    D2D1_INK_BEZIER_SEGMENT._fields_ = [
        ("point1", win32more.Graphics.Direct2D.D2D1_INK_POINT),
        ("point2", win32more.Graphics.Direct2D.D2D1_INK_POINT),
        ("point3", win32more.Graphics.Direct2D.D2D1_INK_POINT),
    ]
    return D2D1_INK_BEZIER_SEGMENT
def _define_D2D1_INK_STYLE_PROPERTIES_head():
    class D2D1_INK_STYLE_PROPERTIES(Structure):
        pass
    return D2D1_INK_STYLE_PROPERTIES
def _define_D2D1_INK_STYLE_PROPERTIES():
    D2D1_INK_STYLE_PROPERTIES = win32more.Graphics.Direct2D.D2D1_INK_STYLE_PROPERTIES_head
    D2D1_INK_STYLE_PROPERTIES._fields_ = [
        ("nibShape", win32more.Graphics.Direct2D.D2D1_INK_NIB_SHAPE),
        ("nibTransform", win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F),
    ]
    return D2D1_INK_STYLE_PROPERTIES
D2D1_PATCH_EDGE_MODE = UInt32
D2D1_PATCH_EDGE_MODE_ALIASED = 0
D2D1_PATCH_EDGE_MODE_ANTIALIASED = 1
D2D1_PATCH_EDGE_MODE_ALIASED_INFLATED = 2
D2D1_PATCH_EDGE_MODE_FORCE_DWORD = 4294967295
def _define_D2D1_GRADIENT_MESH_PATCH_head():
    class D2D1_GRADIENT_MESH_PATCH(Structure):
        pass
    return D2D1_GRADIENT_MESH_PATCH
def _define_D2D1_GRADIENT_MESH_PATCH():
    D2D1_GRADIENT_MESH_PATCH = win32more.Graphics.Direct2D.D2D1_GRADIENT_MESH_PATCH_head
    D2D1_GRADIENT_MESH_PATCH._fields_ = [
        ("point00", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("point01", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("point02", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("point03", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("point10", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("point11", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("point12", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("point13", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("point20", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("point21", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("point22", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("point23", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("point30", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("point31", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("point32", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("point33", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("color00", win32more.Graphics.Direct2D.Common.D2D1_COLOR_F),
        ("color03", win32more.Graphics.Direct2D.Common.D2D1_COLOR_F),
        ("color30", win32more.Graphics.Direct2D.Common.D2D1_COLOR_F),
        ("color33", win32more.Graphics.Direct2D.Common.D2D1_COLOR_F),
        ("topEdgeMode", win32more.Graphics.Direct2D.D2D1_PATCH_EDGE_MODE),
        ("leftEdgeMode", win32more.Graphics.Direct2D.D2D1_PATCH_EDGE_MODE),
        ("bottomEdgeMode", win32more.Graphics.Direct2D.D2D1_PATCH_EDGE_MODE),
        ("rightEdgeMode", win32more.Graphics.Direct2D.D2D1_PATCH_EDGE_MODE),
    ]
    return D2D1_GRADIENT_MESH_PATCH
D2D1_SPRITE_OPTIONS = UInt32
D2D1_SPRITE_OPTIONS_NONE = 0
D2D1_SPRITE_OPTIONS_CLAMP_TO_SOURCE_RECTANGLE = 1
D2D1_SPRITE_OPTIONS_FORCE_DWORD = 4294967295
D2D1_COLOR_BITMAP_GLYPH_SNAP_OPTION = UInt32
D2D1_COLOR_BITMAP_GLYPH_SNAP_OPTION_DEFAULT = 0
D2D1_COLOR_BITMAP_GLYPH_SNAP_OPTION_DISABLE = 1
D2D1_COLOR_BITMAP_GLYPH_SNAP_OPTION_FORCE_DWORD = 4294967295
D2D1_GAMMA1 = UInt32
D2D1_GAMMA1_G22 = 0
D2D1_GAMMA1_G10 = 1
D2D1_GAMMA1_G2084 = 2
D2D1_GAMMA1_FORCE_DWORD = 4294967295
def _define_D2D1_SIMPLE_COLOR_PROFILE_head():
    class D2D1_SIMPLE_COLOR_PROFILE(Structure):
        pass
    return D2D1_SIMPLE_COLOR_PROFILE
def _define_D2D1_SIMPLE_COLOR_PROFILE():
    D2D1_SIMPLE_COLOR_PROFILE = win32more.Graphics.Direct2D.D2D1_SIMPLE_COLOR_PROFILE_head
    D2D1_SIMPLE_COLOR_PROFILE._fields_ = [
        ("redPrimary", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("greenPrimary", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("bluePrimary", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("whitePointXZ", win32more.Graphics.Direct2D.Common.D2D_POINT_2F),
        ("gamma", win32more.Graphics.Direct2D.D2D1_GAMMA1),
    ]
    return D2D1_SIMPLE_COLOR_PROFILE
D2D1_COLOR_CONTEXT_TYPE = UInt32
D2D1_COLOR_CONTEXT_TYPE_ICC = 0
D2D1_COLOR_CONTEXT_TYPE_SIMPLE = 1
D2D1_COLOR_CONTEXT_TYPE_DXGI = 2
D2D1_COLOR_CONTEXT_TYPE_FORCE_DWORD = 4294967295
def _define_ID2D1InkStyle_head():
    class ID2D1InkStyle(win32more.Graphics.Direct2D.ID2D1Resource_head):
        Guid = Guid('bae8b344-23fc-4071-8cb5-d05d6f073848')
    return ID2D1InkStyle
def _define_ID2D1InkStyle():
    ID2D1InkStyle = win32more.Graphics.Direct2D.ID2D1InkStyle_head
    ID2D1InkStyle.SetNibTransform = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head), use_last_error=False)(4, 'SetNibTransform', ((1, 'transform'),)))
    ID2D1InkStyle.GetNibTransform = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head), use_last_error=False)(5, 'GetNibTransform', ((1, 'transform'),)))
    ID2D1InkStyle.SetNibShape = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.D2D1_INK_NIB_SHAPE, use_last_error=False)(6, 'SetNibShape', ((1, 'nibShape'),)))
    ID2D1InkStyle.GetNibShape = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_INK_NIB_SHAPE, use_last_error=False)(7, 'GetNibShape', ()))
    return ID2D1InkStyle
def _define_ID2D1Ink_head():
    class ID2D1Ink(win32more.Graphics.Direct2D.ID2D1Resource_head):
        Guid = Guid('b499923b-7029-478f-a8b3-432c7c5f5312')
    return ID2D1Ink
def _define_ID2D1Ink():
    ID2D1Ink = win32more.Graphics.Direct2D.ID2D1Ink_head
    ID2D1Ink.SetStartPoint = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.D2D1_INK_POINT_head), use_last_error=False)(4, 'SetStartPoint', ((1, 'startPoint'),)))
    ID2D1Ink.GetStartPoint = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_INK_POINT, use_last_error=False)(5, 'GetStartPoint', ()))
    ID2D1Ink.AddSegments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.D2D1_INK_BEZIER_SEGMENT),UInt32, use_last_error=False)(6, 'AddSegments', ((1, 'segments'),(1, 'segmentsCount'),)))
    ID2D1Ink.RemoveSegmentsAtEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(7, 'RemoveSegmentsAtEnd', ((1, 'segmentsCount'),)))
    ID2D1Ink.SetSegments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Direct2D.D2D1_INK_BEZIER_SEGMENT),UInt32, use_last_error=False)(8, 'SetSegments', ((1, 'startSegment'),(1, 'segments'),(1, 'segmentsCount'),)))
    ID2D1Ink.SetSegmentAtEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.D2D1_INK_BEZIER_SEGMENT_head), use_last_error=False)(9, 'SetSegmentAtEnd', ((1, 'segment'),)))
    ID2D1Ink.GetSegmentCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(10, 'GetSegmentCount', ()))
    ID2D1Ink.GetSegments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Direct2D.D2D1_INK_BEZIER_SEGMENT),UInt32, use_last_error=False)(11, 'GetSegments', ((1, 'startSegment'),(1, 'segments'),(1, 'segmentsCount'),)))
    ID2D1Ink.StreamAsGeometry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1InkStyle_head,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head),Single,win32more.Graphics.Direct2D.Common.ID2D1SimplifiedGeometrySink_head, use_last_error=False)(12, 'StreamAsGeometry', ((1, 'inkStyle'),(1, 'worldTransform'),(1, 'flatteningTolerance'),(1, 'geometrySink'),)))
    ID2D1Ink.GetBounds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1InkStyle_head,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head), use_last_error=False)(13, 'GetBounds', ((1, 'inkStyle'),(1, 'worldTransform'),(1, 'bounds'),)))
    return ID2D1Ink
def _define_ID2D1GradientMesh_head():
    class ID2D1GradientMesh(win32more.Graphics.Direct2D.ID2D1Resource_head):
        Guid = Guid('f292e401-c050-4cde-83d7-04962d3b23c2')
    return ID2D1GradientMesh
def _define_ID2D1GradientMesh():
    ID2D1GradientMesh = win32more.Graphics.Direct2D.ID2D1GradientMesh_head
    ID2D1GradientMesh.GetPatchCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(4, 'GetPatchCount', ()))
    ID2D1GradientMesh.GetPatches = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Direct2D.D2D1_GRADIENT_MESH_PATCH),UInt32, use_last_error=False)(5, 'GetPatches', ((1, 'startIndex'),(1, 'patches'),(1, 'patchesCount'),)))
    return ID2D1GradientMesh
def _define_ID2D1ImageSource_head():
    class ID2D1ImageSource(win32more.Graphics.Direct2D.ID2D1Image_head):
        Guid = Guid('c9b664e5-74a1-4378-9ac2-eefc37a3f4d8')
    return ID2D1ImageSource
def _define_ID2D1ImageSource():
    ID2D1ImageSource = win32more.Graphics.Direct2D.ID2D1ImageSource_head
    ID2D1ImageSource.OfferResources = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'OfferResources', ()))
    ID2D1ImageSource.TryReclaimResources = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'TryReclaimResources', ((1, 'resourcesDiscarded'),)))
    return ID2D1ImageSource
def _define_ID2D1ImageSourceFromWic_head():
    class ID2D1ImageSourceFromWic(win32more.Graphics.Direct2D.ID2D1ImageSource_head):
        Guid = Guid('77395441-1c8f-4555-8683-f50dab0fe792')
    return ID2D1ImageSourceFromWic
def _define_ID2D1ImageSourceFromWic():
    ID2D1ImageSourceFromWic = win32more.Graphics.Direct2D.ID2D1ImageSourceFromWic_head
    ID2D1ImageSourceFromWic.EnsureCached = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_U_head), use_last_error=False)(6, 'EnsureCached', ((1, 'rectangleToFill'),)))
    ID2D1ImageSourceFromWic.TrimCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_U_head), use_last_error=False)(7, 'TrimCache', ((1, 'rectangleToPreserve'),)))
    ID2D1ImageSourceFromWic.GetSource = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Imaging.IWICBitmapSource_head), use_last_error=False)(8, 'GetSource', ((1, 'wicBitmapSource'),)))
    return ID2D1ImageSourceFromWic
def _define_ID2D1TransformedImageSource_head():
    class ID2D1TransformedImageSource(win32more.Graphics.Direct2D.ID2D1Image_head):
        Guid = Guid('7f1f79e5-2796-416c-8f55-700f911445e5')
    return ID2D1TransformedImageSource
def _define_ID2D1TransformedImageSource():
    ID2D1TransformedImageSource = win32more.Graphics.Direct2D.ID2D1TransformedImageSource_head
    ID2D1TransformedImageSource.GetSource = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.ID2D1ImageSource_head), use_last_error=False)(4, 'GetSource', ((1, 'imageSource'),)))
    ID2D1TransformedImageSource.GetProperties = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.D2D1_TRANSFORMED_IMAGE_SOURCE_PROPERTIES_head), use_last_error=False)(5, 'GetProperties', ((1, 'properties'),)))
    return ID2D1TransformedImageSource
def _define_ID2D1LookupTable3D_head():
    class ID2D1LookupTable3D(win32more.Graphics.Direct2D.ID2D1Resource_head):
        Guid = Guid('53dd9855-a3b0-4d5b-82e1-26e25c5e5797')
    return ID2D1LookupTable3D
def _define_ID2D1LookupTable3D():
    ID2D1LookupTable3D = win32more.Graphics.Direct2D.ID2D1LookupTable3D_head
    return ID2D1LookupTable3D
def _define_ID2D1DeviceContext2_head():
    class ID2D1DeviceContext2(win32more.Graphics.Direct2D.ID2D1DeviceContext1_head):
        Guid = Guid('394ea6a3-0c34-4321-950b-6ca20f0be6c7')
    return ID2D1DeviceContext2
def _define_ID2D1DeviceContext2():
    ID2D1DeviceContext2 = win32more.Graphics.Direct2D.ID2D1DeviceContext2_head
    ID2D1DeviceContext2.CreateInk = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.D2D1_INK_POINT_head),POINTER(win32more.Graphics.Direct2D.ID2D1Ink_head), use_last_error=False)(95, 'CreateInk', ((1, 'startPoint'),(1, 'ink'),)))
    ID2D1DeviceContext2.CreateInkStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.D2D1_INK_STYLE_PROPERTIES_head),POINTER(win32more.Graphics.Direct2D.ID2D1InkStyle_head), use_last_error=False)(96, 'CreateInkStyle', ((1, 'inkStyleProperties'),(1, 'inkStyle'),)))
    ID2D1DeviceContext2.CreateGradientMesh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.D2D1_GRADIENT_MESH_PATCH),UInt32,POINTER(win32more.Graphics.Direct2D.ID2D1GradientMesh_head), use_last_error=False)(97, 'CreateGradientMesh', ((1, 'patches'),(1, 'patchesCount'),(1, 'gradientMesh'),)))
    ID2D1DeviceContext2.CreateImageSourceFromWic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Imaging.IWICBitmapSource_head,win32more.Graphics.Direct2D.D2D1_IMAGE_SOURCE_LOADING_OPTIONS,win32more.Graphics.Direct2D.Common.D2D1_ALPHA_MODE,POINTER(win32more.Graphics.Direct2D.ID2D1ImageSourceFromWic_head), use_last_error=False)(98, 'CreateImageSourceFromWic', ((1, 'wicBitmapSource'),(1, 'loadingOptions'),(1, 'alphaMode'),(1, 'imageSource'),)))
    ID2D1DeviceContext2.CreateLookupTable3D = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.D2D1_BUFFER_PRECISION,POINTER(UInt32),POINTER(Byte),UInt32,POINTER(UInt32),POINTER(win32more.Graphics.Direct2D.ID2D1LookupTable3D_head), use_last_error=False)(99, 'CreateLookupTable3D', ((1, 'precision'),(1, 'extents'),(1, 'data'),(1, 'dataCount'),(1, 'strides'),(1, 'lookupTable'),)))
    ID2D1DeviceContext2.CreateImageSourceFromDxgi = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.IDXGISurface_head),UInt32,win32more.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE,win32more.Graphics.Direct2D.D2D1_IMAGE_SOURCE_FROM_DXGI_OPTIONS,POINTER(win32more.Graphics.Direct2D.ID2D1ImageSource_head), use_last_error=False)(100, 'CreateImageSourceFromDxgi', ((1, 'surfaces'),(1, 'surfaceCount'),(1, 'colorSpace'),(1, 'options'),(1, 'imageSource'),)))
    ID2D1DeviceContext2.GetGradientMeshWorldBounds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1GradientMesh_head,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head), use_last_error=False)(101, 'GetGradientMeshWorldBounds', ((1, 'gradientMesh'),(1, 'pBounds'),)))
    ID2D1DeviceContext2.DrawInk = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.ID2D1Ink_head,win32more.Graphics.Direct2D.ID2D1Brush_head,win32more.Graphics.Direct2D.ID2D1InkStyle_head, use_last_error=False)(102, 'DrawInk', ((1, 'ink'),(1, 'brush'),(1, 'inkStyle'),)))
    ID2D1DeviceContext2.DrawGradientMesh = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.ID2D1GradientMesh_head, use_last_error=False)(103, 'DrawGradientMesh', ((1, 'gradientMesh'),)))
    ID2D1DeviceContext2.DrawGdiMetafile = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.ID2D1GdiMetafile_head,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head), use_last_error=False)(104, 'DrawGdiMetafile', ((1, 'gdiMetafile'),(1, 'destinationRectangle'),(1, 'sourceRectangle'),)))
    ID2D1DeviceContext2.CreateTransformedImageSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1ImageSource_head,POINTER(win32more.Graphics.Direct2D.D2D1_TRANSFORMED_IMAGE_SOURCE_PROPERTIES_head),POINTER(win32more.Graphics.Direct2D.ID2D1TransformedImageSource_head), use_last_error=False)(105, 'CreateTransformedImageSource', ((1, 'imageSource'),(1, 'properties'),(1, 'transformedImageSource'),)))
    return ID2D1DeviceContext2
def _define_ID2D1Device2_head():
    class ID2D1Device2(win32more.Graphics.Direct2D.ID2D1Device1_head):
        Guid = Guid('a44472e1-8dfb-4e60-8492-6e2861c9ca8b')
    return ID2D1Device2
def _define_ID2D1Device2():
    ID2D1Device2 = win32more.Graphics.Direct2D.ID2D1Device2_head
    ID2D1Device2.CreateDeviceContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.D2D1_DEVICE_CONTEXT_OPTIONS,POINTER(win32more.Graphics.Direct2D.ID2D1DeviceContext2_head), use_last_error=False)(12, 'CreateDeviceContext', ((1, 'options'),(1, 'deviceContext2'),)))
    ID2D1Device2.FlushDeviceContexts = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.ID2D1Bitmap_head, use_last_error=False)(13, 'FlushDeviceContexts', ((1, 'bitmap'),)))
    ID2D1Device2.GetDxgiDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.IDXGIDevice_head), use_last_error=False)(14, 'GetDxgiDevice', ((1, 'dxgiDevice'),)))
    return ID2D1Device2
def _define_ID2D1Factory3_head():
    class ID2D1Factory3(win32more.Graphics.Direct2D.ID2D1Factory2_head):
        Guid = Guid('0869759f-4f00-413f-b03e-2bda45404d0f')
    return ID2D1Factory3
def _define_ID2D1Factory3():
    ID2D1Factory3 = win32more.Graphics.Direct2D.ID2D1Factory3_head
    ID2D1Factory3.CreateDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGIDevice_head,POINTER(win32more.Graphics.Direct2D.ID2D1Device2_head), use_last_error=False)(28, 'CreateDevice', ((1, 'dxgiDevice'),(1, 'd2dDevice2'),)))
    return ID2D1Factory3
def _define_ID2D1CommandSink2_head():
    class ID2D1CommandSink2(win32more.Graphics.Direct2D.ID2D1CommandSink1_head):
        Guid = Guid('3bab440e-417e-47df-a2e2-bc0be6a00916')
    return ID2D1CommandSink2
def _define_ID2D1CommandSink2():
    ID2D1CommandSink2 = win32more.Graphics.Direct2D.ID2D1CommandSink2_head
    ID2D1CommandSink2.DrawInk = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Ink_head,win32more.Graphics.Direct2D.ID2D1Brush_head,win32more.Graphics.Direct2D.ID2D1InkStyle_head, use_last_error=False)(29, 'DrawInk', ((1, 'ink'),(1, 'brush'),(1, 'inkStyle'),)))
    ID2D1CommandSink2.DrawGradientMesh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1GradientMesh_head, use_last_error=False)(30, 'DrawGradientMesh', ((1, 'gradientMesh'),)))
    ID2D1CommandSink2.DrawGdiMetafile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1GdiMetafile_head,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head), use_last_error=False)(31, 'DrawGdiMetafile', ((1, 'gdiMetafile'),(1, 'destinationRectangle'),(1, 'sourceRectangle'),)))
    return ID2D1CommandSink2
def _define_ID2D1GdiMetafile1_head():
    class ID2D1GdiMetafile1(win32more.Graphics.Direct2D.ID2D1GdiMetafile_head):
        Guid = Guid('2e69f9e8-dd3f-4bf9-95ba-c04f49d788df')
    return ID2D1GdiMetafile1
def _define_ID2D1GdiMetafile1():
    ID2D1GdiMetafile1 = win32more.Graphics.Direct2D.ID2D1GdiMetafile1_head
    ID2D1GdiMetafile1.GetDpi = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single),POINTER(Single), use_last_error=False)(6, 'GetDpi', ((1, 'dpiX'),(1, 'dpiY'),)))
    ID2D1GdiMetafile1.GetSourceBounds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head), use_last_error=False)(7, 'GetSourceBounds', ((1, 'bounds'),)))
    return ID2D1GdiMetafile1
def _define_ID2D1GdiMetafileSink1_head():
    class ID2D1GdiMetafileSink1(win32more.Graphics.Direct2D.ID2D1GdiMetafileSink_head):
        Guid = Guid('fd0ecb6b-91e6-411e-8655-395e760f91b4')
    return ID2D1GdiMetafileSink1
def _define_ID2D1GdiMetafileSink1():
    ID2D1GdiMetafileSink1 = win32more.Graphics.Direct2D.ID2D1GdiMetafileSink1_head
    ID2D1GdiMetafileSink1.ProcessRecord = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p,UInt32,UInt32, use_last_error=False)(4, 'ProcessRecord', ((1, 'recordType'),(1, 'recordData'),(1, 'recordDataSize'),(1, 'flags'),)))
    return ID2D1GdiMetafileSink1
def _define_ID2D1SpriteBatch_head():
    class ID2D1SpriteBatch(win32more.Graphics.Direct2D.ID2D1Resource_head):
        Guid = Guid('4dc583bf-3a10-438a-8722-e9765224f1f1')
    return ID2D1SpriteBatch
def _define_ID2D1SpriteBatch():
    ID2D1SpriteBatch = win32more.Graphics.Direct2D.ID2D1SpriteBatch_head
    ID2D1SpriteBatch.AddSprites = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_U_head),POINTER(win32more.Graphics.Direct2D.Common.D2D1_COLOR_F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head),UInt32,UInt32,UInt32,UInt32, use_last_error=False)(4, 'AddSprites', ((1, 'spriteCount'),(1, 'destinationRectangles'),(1, 'sourceRectangles'),(1, 'colors'),(1, 'transforms'),(1, 'destinationRectanglesStride'),(1, 'sourceRectanglesStride'),(1, 'colorsStride'),(1, 'transformsStride'),)))
    ID2D1SpriteBatch.SetSprites = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_U_head),POINTER(win32more.Graphics.Direct2D.Common.D2D1_COLOR_F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head),UInt32,UInt32,UInt32,UInt32, use_last_error=False)(5, 'SetSprites', ((1, 'startIndex'),(1, 'spriteCount'),(1, 'destinationRectangles'),(1, 'sourceRectangles'),(1, 'colors'),(1, 'transforms'),(1, 'destinationRectanglesStride'),(1, 'sourceRectanglesStride'),(1, 'colorsStride'),(1, 'transformsStride'),)))
    ID2D1SpriteBatch.GetSprites = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F),POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_U),POINTER(win32more.Graphics.Direct2D.Common.D2D1_COLOR_F),POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F), use_last_error=False)(6, 'GetSprites', ((1, 'startIndex'),(1, 'spriteCount'),(1, 'destinationRectangles'),(1, 'sourceRectangles'),(1, 'colors'),(1, 'transforms'),)))
    ID2D1SpriteBatch.GetSpriteCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(7, 'GetSpriteCount', ()))
    ID2D1SpriteBatch.Clear = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(8, 'Clear', ()))
    return ID2D1SpriteBatch
def _define_ID2D1DeviceContext3_head():
    class ID2D1DeviceContext3(win32more.Graphics.Direct2D.ID2D1DeviceContext2_head):
        Guid = Guid('235a7496-8351-414c-bcd4-6672ab2d8e00')
    return ID2D1DeviceContext3
def _define_ID2D1DeviceContext3():
    ID2D1DeviceContext3 = win32more.Graphics.Direct2D.ID2D1DeviceContext3_head
    ID2D1DeviceContext3.CreateSpriteBatch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.ID2D1SpriteBatch_head), use_last_error=False)(106, 'CreateSpriteBatch', ((1, 'spriteBatch'),)))
    ID2D1DeviceContext3.DrawSpriteBatch = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.ID2D1SpriteBatch_head,UInt32,UInt32,win32more.Graphics.Direct2D.ID2D1Bitmap_head,win32more.Graphics.Direct2D.D2D1_BITMAP_INTERPOLATION_MODE,win32more.Graphics.Direct2D.D2D1_SPRITE_OPTIONS, use_last_error=False)(107, 'DrawSpriteBatch', ((1, 'spriteBatch'),(1, 'startIndex'),(1, 'spriteCount'),(1, 'bitmap'),(1, 'interpolationMode'),(1, 'spriteOptions'),)))
    return ID2D1DeviceContext3
def _define_ID2D1Device3_head():
    class ID2D1Device3(win32more.Graphics.Direct2D.ID2D1Device2_head):
        Guid = Guid('852f2087-802c-4037-ab60-ff2e7ee6fc01')
    return ID2D1Device3
def _define_ID2D1Device3():
    ID2D1Device3 = win32more.Graphics.Direct2D.ID2D1Device3_head
    ID2D1Device3.CreateDeviceContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.D2D1_DEVICE_CONTEXT_OPTIONS,POINTER(win32more.Graphics.Direct2D.ID2D1DeviceContext3_head), use_last_error=False)(15, 'CreateDeviceContext', ((1, 'options'),(1, 'deviceContext3'),)))
    return ID2D1Device3
def _define_ID2D1Factory4_head():
    class ID2D1Factory4(win32more.Graphics.Direct2D.ID2D1Factory3_head):
        Guid = Guid('bd4ec2d2-0662-4bee-ba8e-6f29f032e096')
    return ID2D1Factory4
def _define_ID2D1Factory4():
    ID2D1Factory4 = win32more.Graphics.Direct2D.ID2D1Factory4_head
    ID2D1Factory4.CreateDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGIDevice_head,POINTER(win32more.Graphics.Direct2D.ID2D1Device3_head), use_last_error=False)(29, 'CreateDevice', ((1, 'dxgiDevice'),(1, 'd2dDevice3'),)))
    return ID2D1Factory4
def _define_ID2D1CommandSink3_head():
    class ID2D1CommandSink3(win32more.Graphics.Direct2D.ID2D1CommandSink2_head):
        Guid = Guid('18079135-4cf3-4868-bc8e-06067e6d242d')
    return ID2D1CommandSink3
def _define_ID2D1CommandSink3():
    ID2D1CommandSink3 = win32more.Graphics.Direct2D.ID2D1CommandSink3_head
    ID2D1CommandSink3.DrawSpriteBatch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1SpriteBatch_head,UInt32,UInt32,win32more.Graphics.Direct2D.ID2D1Bitmap_head,win32more.Graphics.Direct2D.D2D1_BITMAP_INTERPOLATION_MODE,win32more.Graphics.Direct2D.D2D1_SPRITE_OPTIONS, use_last_error=False)(32, 'DrawSpriteBatch', ((1, 'spriteBatch'),(1, 'startIndex'),(1, 'spriteCount'),(1, 'bitmap'),(1, 'interpolationMode'),(1, 'spriteOptions'),)))
    return ID2D1CommandSink3
def _define_ID2D1SvgGlyphStyle_head():
    class ID2D1SvgGlyphStyle(win32more.Graphics.Direct2D.ID2D1Resource_head):
        Guid = Guid('af671749-d241-4db8-8e41-dcc2e5c1a438')
    return ID2D1SvgGlyphStyle
def _define_ID2D1SvgGlyphStyle():
    ID2D1SvgGlyphStyle = win32more.Graphics.Direct2D.ID2D1SvgGlyphStyle_head
    ID2D1SvgGlyphStyle.SetFill = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Brush_head, use_last_error=False)(4, 'SetFill', ((1, 'brush'),)))
    ID2D1SvgGlyphStyle.GetFill = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.ID2D1Brush_head), use_last_error=False)(5, 'GetFill', ((1, 'brush'),)))
    ID2D1SvgGlyphStyle.SetStroke = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Brush_head,Single,POINTER(Single),UInt32,Single, use_last_error=False)(6, 'SetStroke', ((1, 'brush'),(1, 'strokeWidth'),(1, 'dashes'),(1, 'dashesCount'),(1, 'dashOffset'),)))
    ID2D1SvgGlyphStyle.GetStrokeDashesCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(7, 'GetStrokeDashesCount', ()))
    ID2D1SvgGlyphStyle.GetStroke = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.ID2D1Brush_head),POINTER(Single),POINTER(Single),UInt32,POINTER(Single), use_last_error=False)(8, 'GetStroke', ((1, 'brush'),(1, 'strokeWidth'),(1, 'dashes'),(1, 'dashesCount'),(1, 'dashOffset'),)))
    return ID2D1SvgGlyphStyle
def _define_ID2D1DeviceContext4_head():
    class ID2D1DeviceContext4(win32more.Graphics.Direct2D.ID2D1DeviceContext3_head):
        Guid = Guid('8c427831-3d90-4476-b647-c4fae349e4db')
    return ID2D1DeviceContext4
def _define_ID2D1DeviceContext4():
    ID2D1DeviceContext4 = win32more.Graphics.Direct2D.ID2D1DeviceContext4_head
    ID2D1DeviceContext4.CreateSvgGlyphStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.ID2D1SvgGlyphStyle_head), use_last_error=False)(108, 'CreateSvgGlyphStyle', ((1, 'svgGlyphStyle'),)))
    ID2D1DeviceContext4.DrawText = COMMETHOD(WINFUNCTYPE(Void,POINTER(Char),UInt32,win32more.Graphics.DirectWrite.IDWriteTextFormat_head,POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head),win32more.Graphics.Direct2D.ID2D1Brush_head,win32more.Graphics.Direct2D.ID2D1SvgGlyphStyle_head,UInt32,win32more.Graphics.Direct2D.D2D1_DRAW_TEXT_OPTIONS,win32more.Graphics.DirectWrite.DWRITE_MEASURING_MODE, use_last_error=False)(109, 'DrawText', ((1, 'string'),(1, 'stringLength'),(1, 'textFormat'),(1, 'layoutRect'),(1, 'defaultFillBrush'),(1, 'svgGlyphStyle'),(1, 'colorPaletteIndex'),(1, 'options'),(1, 'measuringMode'),)))
    ID2D1DeviceContext4.DrawTextLayout = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.Common.D2D_POINT_2F,win32more.Graphics.DirectWrite.IDWriteTextLayout_head,win32more.Graphics.Direct2D.ID2D1Brush_head,win32more.Graphics.Direct2D.ID2D1SvgGlyphStyle_head,UInt32,win32more.Graphics.Direct2D.D2D1_DRAW_TEXT_OPTIONS, use_last_error=False)(110, 'DrawTextLayout', ((1, 'origin'),(1, 'textLayout'),(1, 'defaultFillBrush'),(1, 'svgGlyphStyle'),(1, 'colorPaletteIndex'),(1, 'options'),)))
    ID2D1DeviceContext4.DrawColorBitmapGlyphRun = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.DirectWrite.DWRITE_GLYPH_IMAGE_FORMATS,win32more.Graphics.Direct2D.Common.D2D_POINT_2F,POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_RUN_head),win32more.Graphics.DirectWrite.DWRITE_MEASURING_MODE,win32more.Graphics.Direct2D.D2D1_COLOR_BITMAP_GLYPH_SNAP_OPTION, use_last_error=False)(111, 'DrawColorBitmapGlyphRun', ((1, 'glyphImageFormat'),(1, 'baselineOrigin'),(1, 'glyphRun'),(1, 'measuringMode'),(1, 'bitmapSnapOption'),)))
    ID2D1DeviceContext4.DrawSvgGlyphRun = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.Common.D2D_POINT_2F,POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_RUN_head),win32more.Graphics.Direct2D.ID2D1Brush_head,win32more.Graphics.Direct2D.ID2D1SvgGlyphStyle_head,UInt32,win32more.Graphics.DirectWrite.DWRITE_MEASURING_MODE, use_last_error=False)(112, 'DrawSvgGlyphRun', ((1, 'baselineOrigin'),(1, 'glyphRun'),(1, 'defaultFillBrush'),(1, 'svgGlyphStyle'),(1, 'colorPaletteIndex'),(1, 'measuringMode'),)))
    ID2D1DeviceContext4.GetColorBitmapGlyphImage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_GLYPH_IMAGE_FORMATS,win32more.Graphics.Direct2D.Common.D2D_POINT_2F,win32more.Graphics.DirectWrite.IDWriteFontFace_head,Single,UInt16,win32more.Foundation.BOOL,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head),Single,Single,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head),POINTER(win32more.Graphics.Direct2D.ID2D1Image_head), use_last_error=False)(113, 'GetColorBitmapGlyphImage', ((1, 'glyphImageFormat'),(1, 'glyphOrigin'),(1, 'fontFace'),(1, 'fontEmSize'),(1, 'glyphIndex'),(1, 'isSideways'),(1, 'worldTransform'),(1, 'dpiX'),(1, 'dpiY'),(1, 'glyphTransform'),(1, 'glyphImage'),)))
    ID2D1DeviceContext4.GetSvgGlyphImage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.Common.D2D_POINT_2F,win32more.Graphics.DirectWrite.IDWriteFontFace_head,Single,UInt16,win32more.Foundation.BOOL,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head),win32more.Graphics.Direct2D.ID2D1Brush_head,win32more.Graphics.Direct2D.ID2D1SvgGlyphStyle_head,UInt32,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head),POINTER(win32more.Graphics.Direct2D.ID2D1CommandList_head), use_last_error=False)(114, 'GetSvgGlyphImage', ((1, 'glyphOrigin'),(1, 'fontFace'),(1, 'fontEmSize'),(1, 'glyphIndex'),(1, 'isSideways'),(1, 'worldTransform'),(1, 'defaultFillBrush'),(1, 'svgGlyphStyle'),(1, 'colorPaletteIndex'),(1, 'glyphTransform'),(1, 'glyphImage'),)))
    return ID2D1DeviceContext4
def _define_ID2D1Device4_head():
    class ID2D1Device4(win32more.Graphics.Direct2D.ID2D1Device3_head):
        Guid = Guid('d7bdb159-5683-4a46-bc9c-72dc720b858b')
    return ID2D1Device4
def _define_ID2D1Device4():
    ID2D1Device4 = win32more.Graphics.Direct2D.ID2D1Device4_head
    ID2D1Device4.CreateDeviceContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.D2D1_DEVICE_CONTEXT_OPTIONS,POINTER(win32more.Graphics.Direct2D.ID2D1DeviceContext4_head), use_last_error=False)(16, 'CreateDeviceContext', ((1, 'options'),(1, 'deviceContext4'),)))
    ID2D1Device4.SetMaximumColorGlyphCacheMemory = COMMETHOD(WINFUNCTYPE(Void,UInt64, use_last_error=False)(17, 'SetMaximumColorGlyphCacheMemory', ((1, 'maximumInBytes'),)))
    ID2D1Device4.GetMaximumColorGlyphCacheMemory = COMMETHOD(WINFUNCTYPE(UInt64, use_last_error=False)(18, 'GetMaximumColorGlyphCacheMemory', ()))
    return ID2D1Device4
def _define_ID2D1Factory5_head():
    class ID2D1Factory5(win32more.Graphics.Direct2D.ID2D1Factory4_head):
        Guid = Guid('c4349994-838e-4b0f-8cab-44997d9eeacc')
    return ID2D1Factory5
def _define_ID2D1Factory5():
    ID2D1Factory5 = win32more.Graphics.Direct2D.ID2D1Factory5_head
    ID2D1Factory5.CreateDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGIDevice_head,POINTER(win32more.Graphics.Direct2D.ID2D1Device4_head), use_last_error=False)(30, 'CreateDevice', ((1, 'dxgiDevice'),(1, 'd2dDevice4'),)))
    return ID2D1Factory5
def _define_ID2D1CommandSink4_head():
    class ID2D1CommandSink4(win32more.Graphics.Direct2D.ID2D1CommandSink3_head):
        Guid = Guid('c78a6519-40d6-4218-b2de-beeeb744bb3e')
    return ID2D1CommandSink4
def _define_ID2D1CommandSink4():
    ID2D1CommandSink4 = win32more.Graphics.Direct2D.ID2D1CommandSink4_head
    ID2D1CommandSink4.SetPrimitiveBlend2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.D2D1_PRIMITIVE_BLEND, use_last_error=False)(33, 'SetPrimitiveBlend2', ((1, 'primitiveBlend'),)))
    return ID2D1CommandSink4
def _define_ID2D1ColorContext1_head():
    class ID2D1ColorContext1(win32more.Graphics.Direct2D.ID2D1ColorContext_head):
        Guid = Guid('1ab42875-c57f-4be9-bd85-9cd78d6f55ee')
    return ID2D1ColorContext1
def _define_ID2D1ColorContext1():
    ID2D1ColorContext1 = win32more.Graphics.Direct2D.ID2D1ColorContext1_head
    ID2D1ColorContext1.GetColorContextType = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct2D.D2D1_COLOR_CONTEXT_TYPE, use_last_error=False)(7, 'GetColorContextType', ()))
    ID2D1ColorContext1.GetDXGIColorSpace = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE, use_last_error=False)(8, 'GetDXGIColorSpace', ()))
    ID2D1ColorContext1.GetSimpleColorProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.D2D1_SIMPLE_COLOR_PROFILE_head), use_last_error=False)(9, 'GetSimpleColorProfile', ((1, 'simpleProfile'),)))
    return ID2D1ColorContext1
def _define_ID2D1DeviceContext5_head():
    class ID2D1DeviceContext5(win32more.Graphics.Direct2D.ID2D1DeviceContext4_head):
        Guid = Guid('7836d248-68cc-4df6-b9e8-de991bf62eb7')
    return ID2D1DeviceContext5
def _define_ID2D1DeviceContext5():
    ID2D1DeviceContext5 = win32more.Graphics.Direct2D.ID2D1DeviceContext5_head
    ID2D1DeviceContext5.CreateSvgDocument = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Graphics.Direct2D.Common.D2D_SIZE_F,POINTER(win32more.Graphics.Direct2D.ID2D1SvgDocument_head), use_last_error=False)(115, 'CreateSvgDocument', ((1, 'inputXmlStream'),(1, 'viewportSize'),(1, 'svgDocument'),)))
    ID2D1DeviceContext5.DrawSvgDocument = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.ID2D1SvgDocument_head, use_last_error=False)(116, 'DrawSvgDocument', ((1, 'svgDocument'),)))
    ID2D1DeviceContext5.CreateColorContextFromDxgiColorSpace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE,POINTER(win32more.Graphics.Direct2D.ID2D1ColorContext1_head), use_last_error=False)(117, 'CreateColorContextFromDxgiColorSpace', ((1, 'colorSpace'),(1, 'colorContext'),)))
    ID2D1DeviceContext5.CreateColorContextFromSimpleColorProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.D2D1_SIMPLE_COLOR_PROFILE_head),POINTER(win32more.Graphics.Direct2D.ID2D1ColorContext1_head), use_last_error=False)(118, 'CreateColorContextFromSimpleColorProfile', ((1, 'simpleProfile'),(1, 'colorContext'),)))
    return ID2D1DeviceContext5
def _define_ID2D1Device5_head():
    class ID2D1Device5(win32more.Graphics.Direct2D.ID2D1Device4_head):
        Guid = Guid('d55ba0a4-6405-4694-aef5-08ee1a4358b4')
    return ID2D1Device5
def _define_ID2D1Device5():
    ID2D1Device5 = win32more.Graphics.Direct2D.ID2D1Device5_head
    ID2D1Device5.CreateDeviceContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.D2D1_DEVICE_CONTEXT_OPTIONS,POINTER(win32more.Graphics.Direct2D.ID2D1DeviceContext5_head), use_last_error=False)(19, 'CreateDeviceContext', ((1, 'options'),(1, 'deviceContext5'),)))
    return ID2D1Device5
def _define_ID2D1Factory6_head():
    class ID2D1Factory6(win32more.Graphics.Direct2D.ID2D1Factory5_head):
        Guid = Guid('f9976f46-f642-44c1-97ca-da32ea2a2635')
    return ID2D1Factory6
def _define_ID2D1Factory6():
    ID2D1Factory6 = win32more.Graphics.Direct2D.ID2D1Factory6_head
    ID2D1Factory6.CreateDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGIDevice_head,POINTER(win32more.Graphics.Direct2D.ID2D1Device5_head), use_last_error=False)(31, 'CreateDevice', ((1, 'dxgiDevice'),(1, 'd2dDevice5'),)))
    return ID2D1Factory6
def _define_ID2D1CommandSink5_head():
    class ID2D1CommandSink5(win32more.Graphics.Direct2D.ID2D1CommandSink4_head):
        Guid = Guid('7047dd26-b1e7-44a7-959a-8349e2144fa8')
    return ID2D1CommandSink5
def _define_ID2D1CommandSink5():
    ID2D1CommandSink5 = win32more.Graphics.Direct2D.ID2D1CommandSink5_head
    ID2D1CommandSink5.BlendImage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1Image_head,win32more.Graphics.Direct2D.Common.D2D1_BLEND_MODE,POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head),win32more.Graphics.Direct2D.D2D1_INTERPOLATION_MODE, use_last_error=False)(34, 'BlendImage', ((1, 'image'),(1, 'blendMode'),(1, 'targetOffset'),(1, 'imageRectangle'),(1, 'interpolationMode'),)))
    return ID2D1CommandSink5
def _define_ID2D1DeviceContext6_head():
    class ID2D1DeviceContext6(win32more.Graphics.Direct2D.ID2D1DeviceContext5_head):
        Guid = Guid('985f7e37-4ed0-4a19-98a3-15b0edfde306')
    return ID2D1DeviceContext6
def _define_ID2D1DeviceContext6():
    ID2D1DeviceContext6 = win32more.Graphics.Direct2D.ID2D1DeviceContext6_head
    ID2D1DeviceContext6.BlendImage = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct2D.ID2D1Image_head,win32more.Graphics.Direct2D.Common.D2D1_BLEND_MODE,POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_RECT_F_head),win32more.Graphics.Direct2D.D2D1_INTERPOLATION_MODE, use_last_error=False)(119, 'BlendImage', ((1, 'image'),(1, 'blendMode'),(1, 'targetOffset'),(1, 'imageRectangle'),(1, 'interpolationMode'),)))
    return ID2D1DeviceContext6
def _define_ID2D1Device6_head():
    class ID2D1Device6(win32more.Graphics.Direct2D.ID2D1Device5_head):
        Guid = Guid('7bfef914-2d75-4bad-be87-e18ddb077b6d')
    return ID2D1Device6
def _define_ID2D1Device6():
    ID2D1Device6 = win32more.Graphics.Direct2D.ID2D1Device6_head
    ID2D1Device6.CreateDeviceContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.D2D1_DEVICE_CONTEXT_OPTIONS,POINTER(win32more.Graphics.Direct2D.ID2D1DeviceContext6_head), use_last_error=False)(20, 'CreateDeviceContext', ((1, 'options'),(1, 'deviceContext6'),)))
    return ID2D1Device6
def _define_ID2D1Factory7_head():
    class ID2D1Factory7(win32more.Graphics.Direct2D.ID2D1Factory6_head):
        Guid = Guid('bdc2bdd3-b96c-4de6-bdf7-99d4745454de')
    return ID2D1Factory7
def _define_ID2D1Factory7():
    ID2D1Factory7 = win32more.Graphics.Direct2D.ID2D1Factory7_head
    ID2D1Factory7.CreateDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGIDevice_head,POINTER(win32more.Graphics.Direct2D.ID2D1Device6_head), use_last_error=False)(32, 'CreateDevice', ((1, 'dxgiDevice'),(1, 'd2dDevice6'),)))
    return ID2D1Factory7
def _define_ID2D1EffectContext1_head():
    class ID2D1EffectContext1(win32more.Graphics.Direct2D.ID2D1EffectContext_head):
        Guid = Guid('84ab595a-fc81-4546-bacd-e8ef4d8abe7a')
    return ID2D1EffectContext1
def _define_ID2D1EffectContext1():
    ID2D1EffectContext1 = win32more.Graphics.Direct2D.ID2D1EffectContext1_head
    ID2D1EffectContext1.CreateLookupTable3D = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.D2D1_BUFFER_PRECISION,POINTER(UInt32),POINTER(Byte),UInt32,POINTER(UInt32),POINTER(win32more.Graphics.Direct2D.ID2D1LookupTable3D_head), use_last_error=False)(24, 'CreateLookupTable3D', ((1, 'precision'),(1, 'extents'),(1, 'data'),(1, 'dataCount'),(1, 'strides'),(1, 'lookupTable'),)))
    return ID2D1EffectContext1
def _define_ID2D1EffectContext2_head():
    class ID2D1EffectContext2(win32more.Graphics.Direct2D.ID2D1EffectContext1_head):
        Guid = Guid('577ad2a0-9fc7-4dda-8b18-dab810140052')
    return ID2D1EffectContext2
def _define_ID2D1EffectContext2():
    ID2D1EffectContext2 = win32more.Graphics.Direct2D.ID2D1EffectContext2_head
    ID2D1EffectContext2.CreateColorContextFromDxgiColorSpace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.Common.DXGI_COLOR_SPACE_TYPE,POINTER(win32more.Graphics.Direct2D.ID2D1ColorContext1_head), use_last_error=False)(25, 'CreateColorContextFromDxgiColorSpace', ((1, 'colorSpace'),(1, 'colorContext'),)))
    ID2D1EffectContext2.CreateColorContextFromSimpleColorProfile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct2D.D2D1_SIMPLE_COLOR_PROFILE_head),POINTER(win32more.Graphics.Direct2D.ID2D1ColorContext1_head), use_last_error=False)(26, 'CreateColorContextFromSimpleColorProfile', ((1, 'simpleProfile'),(1, 'colorContext'),)))
    return ID2D1EffectContext2
def _define_D2D1CreateFactory():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.D2D1_FACTORY_TYPE,POINTER(Guid),POINTER(win32more.Graphics.Direct2D.D2D1_FACTORY_OPTIONS_head),POINTER(c_void_p), use_last_error=False)(("D2D1CreateFactory", windll["d2d1"]), ((1, 'factoryType'),(1, 'riid'),(1, 'pFactoryOptions'),(1, 'ppIFactory'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D2D1MakeRotateMatrix():
    try:
        return WINFUNCTYPE(Void,Single,win32more.Graphics.Direct2D.Common.D2D_POINT_2F,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head), use_last_error=False)(("D2D1MakeRotateMatrix", windll["d2d1"]), ((1, 'angle'),(1, 'center'),(1, 'matrix'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D2D1MakeSkewMatrix():
    try:
        return WINFUNCTYPE(Void,Single,Single,win32more.Graphics.Direct2D.Common.D2D_POINT_2F,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head), use_last_error=False)(("D2D1MakeSkewMatrix", windll["d2d1"]), ((1, 'angleX'),(1, 'angleY'),(1, 'center'),(1, 'matrix'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D2D1IsMatrixInvertible():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head), use_last_error=False)(("D2D1IsMatrixInvertible", windll["d2d1"]), ((1, 'matrix'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D2D1InvertMatrix():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head), use_last_error=False)(("D2D1InvertMatrix", windll["d2d1"]), ((1, 'matrix'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D2D1CreateDevice():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGIDevice_head,POINTER(win32more.Graphics.Direct2D.D2D1_CREATION_PROPERTIES_head),POINTER(win32more.Graphics.Direct2D.ID2D1Device_head), use_last_error=False)(("D2D1CreateDevice", windll["d2d1"]), ((1, 'dxgiDevice'),(1, 'creationProperties'),(1, 'd2dDevice'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D2D1CreateDeviceContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGISurface_head,POINTER(win32more.Graphics.Direct2D.D2D1_CREATION_PROPERTIES_head),POINTER(win32more.Graphics.Direct2D.ID2D1DeviceContext_head), use_last_error=False)(("D2D1CreateDeviceContext", windll["d2d1"]), ((1, 'dxgiSurface'),(1, 'creationProperties'),(1, 'd2dDeviceContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D2D1ConvertColorSpace():
    try:
        return WINFUNCTYPE(win32more.Graphics.Direct2D.Common.D2D1_COLOR_F,win32more.Graphics.Direct2D.D2D1_COLOR_SPACE,win32more.Graphics.Direct2D.D2D1_COLOR_SPACE,POINTER(win32more.Graphics.Direct2D.Common.D2D1_COLOR_F_head), use_last_error=False)(("D2D1ConvertColorSpace", windll["d2d1"]), ((1, 'sourceColorSpace'),(1, 'destinationColorSpace'),(1, 'color'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D2D1SinCos():
    try:
        return WINFUNCTYPE(Void,Single,POINTER(Single),POINTER(Single), use_last_error=False)(("D2D1SinCos", windll["d2d1"]), ((1, 'angle'),(1, 's'),(1, 'c'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D2D1Tan():
    try:
        return WINFUNCTYPE(Single,Single, use_last_error=False)(("D2D1Tan", windll["d2d1"]), ((1, 'angle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D2D1Vec3Length():
    try:
        return WINFUNCTYPE(Single,Single,Single,Single, use_last_error=False)(("D2D1Vec3Length", windll["d2d1"]), ((1, 'x'),(1, 'y'),(1, 'z'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D2D1ComputeMaximumScaleFactor():
    try:
        return WINFUNCTYPE(Single,POINTER(win32more.Graphics.Direct2D.Common.D2D_MATRIX_3X2_F_head), use_last_error=False)(("D2D1ComputeMaximumScaleFactor", windll["d2d1"]), ((1, 'matrix'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D2D1GetGradientMeshInteriorPointsFromCoonsPatch():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2F_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2F_head), use_last_error=False)(("D2D1GetGradientMeshInteriorPointsFromCoonsPatch", windll["d2d1"]), ((1, 'pPoint0'),(1, 'pPoint1'),(1, 'pPoint2'),(1, 'pPoint3'),(1, 'pPoint4'),(1, 'pPoint5'),(1, 'pPoint6'),(1, 'pPoint7'),(1, 'pPoint8'),(1, 'pPoint9'),(1, 'pPoint10'),(1, 'pPoint11'),(1, 'pTensorPoint11'),(1, 'pTensorPoint12'),(1, 'pTensorPoint21'),(1, 'pTensorPoint22'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "D2D1_DEFAULT_FLATTENING_TOLERANCE",
    "CLSID_D2D12DAffineTransform",
    "CLSID_D2D13DPerspectiveTransform",
    "CLSID_D2D13DTransform",
    "CLSID_D2D1ArithmeticComposite",
    "CLSID_D2D1Atlas",
    "CLSID_D2D1BitmapSource",
    "CLSID_D2D1Blend",
    "CLSID_D2D1Border",
    "CLSID_D2D1Brightness",
    "CLSID_D2D1ColorManagement",
    "CLSID_D2D1ColorMatrix",
    "CLSID_D2D1Composite",
    "CLSID_D2D1ConvolveMatrix",
    "CLSID_D2D1Crop",
    "CLSID_D2D1DirectionalBlur",
    "CLSID_D2D1DiscreteTransfer",
    "CLSID_D2D1DisplacementMap",
    "CLSID_D2D1DistantDiffuse",
    "CLSID_D2D1DistantSpecular",
    "CLSID_D2D1DpiCompensation",
    "CLSID_D2D1Flood",
    "CLSID_D2D1GammaTransfer",
    "CLSID_D2D1GaussianBlur",
    "CLSID_D2D1Scale",
    "CLSID_D2D1Histogram",
    "CLSID_D2D1HueRotation",
    "CLSID_D2D1LinearTransfer",
    "CLSID_D2D1LuminanceToAlpha",
    "CLSID_D2D1Morphology",
    "CLSID_D2D1OpacityMetadata",
    "CLSID_D2D1PointDiffuse",
    "CLSID_D2D1PointSpecular",
    "CLSID_D2D1Premultiply",
    "CLSID_D2D1Saturation",
    "CLSID_D2D1Shadow",
    "CLSID_D2D1SpotDiffuse",
    "CLSID_D2D1SpotSpecular",
    "CLSID_D2D1TableTransfer",
    "CLSID_D2D1Tile",
    "CLSID_D2D1Turbulence",
    "CLSID_D2D1UnPremultiply",
    "CLSID_D2D1YCbCr",
    "CLSID_D2D1Contrast",
    "CLSID_D2D1RgbToHue",
    "CLSID_D2D1HueToRgb",
    "CLSID_D2D1ChromaKey",
    "CLSID_D2D1Emboss",
    "CLSID_D2D1Exposure",
    "CLSID_D2D1Grayscale",
    "CLSID_D2D1Invert",
    "CLSID_D2D1Posterize",
    "CLSID_D2D1Sepia",
    "CLSID_D2D1Sharpen",
    "CLSID_D2D1Straighten",
    "CLSID_D2D1TemperatureTint",
    "CLSID_D2D1Vignette",
    "CLSID_D2D1EdgeDetection",
    "CLSID_D2D1HighlightsShadows",
    "CLSID_D2D1LookupTable3D",
    "CLSID_D2D1Opacity",
    "CLSID_D2D1AlphaMask",
    "CLSID_D2D1CrossFade",
    "CLSID_D2D1Tint",
    "D2D1_SCENE_REFERRED_SDR_WHITE_LEVEL",
    "CLSID_D2D1WhiteLevelAdjustment",
    "CLSID_D2D1HdrToneMap",
    "D2D1_APPEND_ALIGNED_ELEMENT",
    "FACILITY_D2D",
    "D2D1_INTERPOLATION_MODE_DEFINITION",
    "D2D1_INTERPOLATION_MODE_DEFINITION_NEAREST_NEIGHBOR",
    "D2D1_INTERPOLATION_MODE_DEFINITION_LINEAR",
    "D2D1_INTERPOLATION_MODE_DEFINITION_CUBIC",
    "D2D1_INTERPOLATION_MODE_DEFINITION_MULTI_SAMPLE_LINEAR",
    "D2D1_INTERPOLATION_MODE_DEFINITION_ANISOTROPIC",
    "D2D1_INTERPOLATION_MODE_DEFINITION_HIGH_QUALITY_CUBIC",
    "D2D1_INTERPOLATION_MODE_DEFINITION_FANT",
    "D2D1_INTERPOLATION_MODE_DEFINITION_MIPMAP_LINEAR",
    "D2D1_GAMMA",
    "D2D1_GAMMA_2_2",
    "D2D1_GAMMA_1_0",
    "D2D1_GAMMA_FORCE_DWORD",
    "D2D1_OPACITY_MASK_CONTENT",
    "D2D1_OPACITY_MASK_CONTENT_GRAPHICS",
    "D2D1_OPACITY_MASK_CONTENT_TEXT_NATURAL",
    "D2D1_OPACITY_MASK_CONTENT_TEXT_GDI_COMPATIBLE",
    "D2D1_OPACITY_MASK_CONTENT_FORCE_DWORD",
    "D2D1_EXTEND_MODE",
    "D2D1_EXTEND_MODE_CLAMP",
    "D2D1_EXTEND_MODE_WRAP",
    "D2D1_EXTEND_MODE_MIRROR",
    "D2D1_EXTEND_MODE_FORCE_DWORD",
    "D2D1_ANTIALIAS_MODE",
    "D2D1_ANTIALIAS_MODE_PER_PRIMITIVE",
    "D2D1_ANTIALIAS_MODE_ALIASED",
    "D2D1_ANTIALIAS_MODE_FORCE_DWORD",
    "D2D1_TEXT_ANTIALIAS_MODE",
    "D2D1_TEXT_ANTIALIAS_MODE_DEFAULT",
    "D2D1_TEXT_ANTIALIAS_MODE_CLEARTYPE",
    "D2D1_TEXT_ANTIALIAS_MODE_GRAYSCALE",
    "D2D1_TEXT_ANTIALIAS_MODE_ALIASED",
    "D2D1_TEXT_ANTIALIAS_MODE_FORCE_DWORD",
    "D2D1_BITMAP_INTERPOLATION_MODE",
    "D2D1_BITMAP_INTERPOLATION_MODE_NEAREST_NEIGHBOR",
    "D2D1_BITMAP_INTERPOLATION_MODE_LINEAR",
    "D2D1_BITMAP_INTERPOLATION_MODE_FORCE_DWORD",
    "D2D1_DRAW_TEXT_OPTIONS",
    "D2D1_DRAW_TEXT_OPTIONS_NO_SNAP",
    "D2D1_DRAW_TEXT_OPTIONS_CLIP",
    "D2D1_DRAW_TEXT_OPTIONS_ENABLE_COLOR_FONT",
    "D2D1_DRAW_TEXT_OPTIONS_DISABLE_COLOR_BITMAP_SNAPPING",
    "D2D1_DRAW_TEXT_OPTIONS_NONE",
    "D2D1_DRAW_TEXT_OPTIONS_FORCE_DWORD",
    "D2D1_BITMAP_PROPERTIES",
    "D2D1_GRADIENT_STOP",
    "D2D1_BRUSH_PROPERTIES",
    "D2D1_BITMAP_BRUSH_PROPERTIES",
    "D2D1_LINEAR_GRADIENT_BRUSH_PROPERTIES",
    "D2D1_RADIAL_GRADIENT_BRUSH_PROPERTIES",
    "D2D1_ARC_SIZE",
    "D2D1_ARC_SIZE_SMALL",
    "D2D1_ARC_SIZE_LARGE",
    "D2D1_ARC_SIZE_FORCE_DWORD",
    "D2D1_CAP_STYLE",
    "D2D1_CAP_STYLE_FLAT",
    "D2D1_CAP_STYLE_SQUARE",
    "D2D1_CAP_STYLE_ROUND",
    "D2D1_CAP_STYLE_TRIANGLE",
    "D2D1_CAP_STYLE_FORCE_DWORD",
    "D2D1_DASH_STYLE",
    "D2D1_DASH_STYLE_SOLID",
    "D2D1_DASH_STYLE_DASH",
    "D2D1_DASH_STYLE_DOT",
    "D2D1_DASH_STYLE_DASH_DOT",
    "D2D1_DASH_STYLE_DASH_DOT_DOT",
    "D2D1_DASH_STYLE_CUSTOM",
    "D2D1_DASH_STYLE_FORCE_DWORD",
    "D2D1_LINE_JOIN",
    "D2D1_LINE_JOIN_MITER",
    "D2D1_LINE_JOIN_BEVEL",
    "D2D1_LINE_JOIN_ROUND",
    "D2D1_LINE_JOIN_MITER_OR_BEVEL",
    "D2D1_LINE_JOIN_FORCE_DWORD",
    "D2D1_COMBINE_MODE",
    "D2D1_COMBINE_MODE_UNION",
    "D2D1_COMBINE_MODE_INTERSECT",
    "D2D1_COMBINE_MODE_XOR",
    "D2D1_COMBINE_MODE_EXCLUDE",
    "D2D1_COMBINE_MODE_FORCE_DWORD",
    "D2D1_GEOMETRY_RELATION",
    "D2D1_GEOMETRY_RELATION_UNKNOWN",
    "D2D1_GEOMETRY_RELATION_DISJOINT",
    "D2D1_GEOMETRY_RELATION_IS_CONTAINED",
    "D2D1_GEOMETRY_RELATION_CONTAINS",
    "D2D1_GEOMETRY_RELATION_OVERLAP",
    "D2D1_GEOMETRY_RELATION_FORCE_DWORD",
    "D2D1_GEOMETRY_SIMPLIFICATION_OPTION",
    "D2D1_GEOMETRY_SIMPLIFICATION_OPTION_CUBICS_AND_LINES",
    "D2D1_GEOMETRY_SIMPLIFICATION_OPTION_LINES",
    "D2D1_GEOMETRY_SIMPLIFICATION_OPTION_FORCE_DWORD",
    "D2D1_TRIANGLE",
    "D2D1_SWEEP_DIRECTION",
    "D2D1_SWEEP_DIRECTION_COUNTER_CLOCKWISE",
    "D2D1_SWEEP_DIRECTION_CLOCKWISE",
    "D2D1_SWEEP_DIRECTION_FORCE_DWORD",
    "D2D1_ARC_SEGMENT",
    "D2D1_QUADRATIC_BEZIER_SEGMENT",
    "D2D1_ELLIPSE",
    "D2D1_ROUNDED_RECT",
    "D2D1_STROKE_STYLE_PROPERTIES",
    "D2D1_LAYER_OPTIONS",
    "D2D1_LAYER_OPTIONS_NONE",
    "D2D1_LAYER_OPTIONS_INITIALIZE_FOR_CLEARTYPE",
    "D2D1_LAYER_OPTIONS_FORCE_DWORD",
    "D2D1_LAYER_PARAMETERS",
    "D2D1_WINDOW_STATE",
    "D2D1_WINDOW_STATE_NONE",
    "D2D1_WINDOW_STATE_OCCLUDED",
    "D2D1_WINDOW_STATE_FORCE_DWORD",
    "D2D1_RENDER_TARGET_TYPE",
    "D2D1_RENDER_TARGET_TYPE_DEFAULT",
    "D2D1_RENDER_TARGET_TYPE_SOFTWARE",
    "D2D1_RENDER_TARGET_TYPE_HARDWARE",
    "D2D1_RENDER_TARGET_TYPE_FORCE_DWORD",
    "D2D1_FEATURE_LEVEL",
    "D2D1_FEATURE_LEVEL_DEFAULT",
    "D2D1_FEATURE_LEVEL_9",
    "D2D1_FEATURE_LEVEL_10",
    "D2D1_FEATURE_LEVEL_FORCE_DWORD",
    "D2D1_RENDER_TARGET_USAGE",
    "D2D1_RENDER_TARGET_USAGE_NONE",
    "D2D1_RENDER_TARGET_USAGE_FORCE_BITMAP_REMOTING",
    "D2D1_RENDER_TARGET_USAGE_GDI_COMPATIBLE",
    "D2D1_RENDER_TARGET_USAGE_FORCE_DWORD",
    "D2D1_PRESENT_OPTIONS",
    "D2D1_PRESENT_OPTIONS_NONE",
    "D2D1_PRESENT_OPTIONS_RETAIN_CONTENTS",
    "D2D1_PRESENT_OPTIONS_IMMEDIATELY",
    "D2D1_PRESENT_OPTIONS_FORCE_DWORD",
    "D2D1_RENDER_TARGET_PROPERTIES",
    "D2D1_HWND_RENDER_TARGET_PROPERTIES",
    "D2D1_COMPATIBLE_RENDER_TARGET_OPTIONS",
    "D2D1_COMPATIBLE_RENDER_TARGET_OPTIONS_NONE",
    "D2D1_COMPATIBLE_RENDER_TARGET_OPTIONS_GDI_COMPATIBLE",
    "D2D1_COMPATIBLE_RENDER_TARGET_OPTIONS_FORCE_DWORD",
    "D2D1_DRAWING_STATE_DESCRIPTION",
    "D2D1_DC_INITIALIZE_MODE",
    "D2D1_DC_INITIALIZE_MODE_COPY",
    "D2D1_DC_INITIALIZE_MODE_CLEAR",
    "D2D1_DC_INITIALIZE_MODE_FORCE_DWORD",
    "D2D1_DEBUG_LEVEL",
    "D2D1_DEBUG_LEVEL_NONE",
    "D2D1_DEBUG_LEVEL_ERROR",
    "D2D1_DEBUG_LEVEL_WARNING",
    "D2D1_DEBUG_LEVEL_INFORMATION",
    "D2D1_DEBUG_LEVEL_FORCE_DWORD",
    "D2D1_FACTORY_TYPE",
    "D2D1_FACTORY_TYPE_SINGLE_THREADED",
    "D2D1_FACTORY_TYPE_MULTI_THREADED",
    "D2D1_FACTORY_TYPE_FORCE_DWORD",
    "D2D1_FACTORY_OPTIONS",
    "ID2D1Resource",
    "ID2D1Image",
    "ID2D1Bitmap",
    "ID2D1GradientStopCollection",
    "ID2D1Brush",
    "ID2D1BitmapBrush",
    "ID2D1SolidColorBrush",
    "ID2D1LinearGradientBrush",
    "ID2D1RadialGradientBrush",
    "ID2D1StrokeStyle",
    "ID2D1Geometry",
    "ID2D1RectangleGeometry",
    "ID2D1RoundedRectangleGeometry",
    "ID2D1EllipseGeometry",
    "ID2D1GeometryGroup",
    "ID2D1TransformedGeometry",
    "ID2D1GeometrySink",
    "ID2D1TessellationSink",
    "ID2D1PathGeometry",
    "ID2D1Mesh",
    "ID2D1Layer",
    "ID2D1DrawingStateBlock",
    "ID2D1RenderTarget",
    "ID2D1BitmapRenderTarget",
    "ID2D1HwndRenderTarget",
    "ID2D1GdiInteropRenderTarget",
    "ID2D1DCRenderTarget",
    "ID2D1Factory",
    "D2D1_CHANNEL_SELECTOR",
    "D2D1_CHANNEL_SELECTOR_R",
    "D2D1_CHANNEL_SELECTOR_G",
    "D2D1_CHANNEL_SELECTOR_B",
    "D2D1_CHANNEL_SELECTOR_A",
    "D2D1_CHANNEL_SELECTOR_FORCE_DWORD",
    "D2D1_BITMAPSOURCE_ORIENTATION",
    "D2D1_BITMAPSOURCE_ORIENTATION_DEFAULT",
    "D2D1_BITMAPSOURCE_ORIENTATION_FLIP_HORIZONTAL",
    "D2D1_BITMAPSOURCE_ORIENTATION_ROTATE_CLOCKWISE180",
    "D2D1_BITMAPSOURCE_ORIENTATION_ROTATE_CLOCKWISE180_FLIP_HORIZONTAL",
    "D2D1_BITMAPSOURCE_ORIENTATION_ROTATE_CLOCKWISE270_FLIP_HORIZONTAL",
    "D2D1_BITMAPSOURCE_ORIENTATION_ROTATE_CLOCKWISE90",
    "D2D1_BITMAPSOURCE_ORIENTATION_ROTATE_CLOCKWISE90_FLIP_HORIZONTAL",
    "D2D1_BITMAPSOURCE_ORIENTATION_ROTATE_CLOCKWISE270",
    "D2D1_BITMAPSOURCE_ORIENTATION_FORCE_DWORD",
    "D2D1_GAUSSIANBLUR_PROP",
    "D2D1_GAUSSIANBLUR_PROP_STANDARD_DEVIATION",
    "D2D1_GAUSSIANBLUR_PROP_OPTIMIZATION",
    "D2D1_GAUSSIANBLUR_PROP_BORDER_MODE",
    "D2D1_GAUSSIANBLUR_PROP_FORCE_DWORD",
    "D2D1_GAUSSIANBLUR_OPTIMIZATION",
    "D2D1_GAUSSIANBLUR_OPTIMIZATION_SPEED",
    "D2D1_GAUSSIANBLUR_OPTIMIZATION_BALANCED",
    "D2D1_GAUSSIANBLUR_OPTIMIZATION_QUALITY",
    "D2D1_GAUSSIANBLUR_OPTIMIZATION_FORCE_DWORD",
    "D2D1_DIRECTIONALBLUR_PROP",
    "D2D1_DIRECTIONALBLUR_PROP_STANDARD_DEVIATION",
    "D2D1_DIRECTIONALBLUR_PROP_ANGLE",
    "D2D1_DIRECTIONALBLUR_PROP_OPTIMIZATION",
    "D2D1_DIRECTIONALBLUR_PROP_BORDER_MODE",
    "D2D1_DIRECTIONALBLUR_PROP_FORCE_DWORD",
    "D2D1_DIRECTIONALBLUR_OPTIMIZATION",
    "D2D1_DIRECTIONALBLUR_OPTIMIZATION_SPEED",
    "D2D1_DIRECTIONALBLUR_OPTIMIZATION_BALANCED",
    "D2D1_DIRECTIONALBLUR_OPTIMIZATION_QUALITY",
    "D2D1_DIRECTIONALBLUR_OPTIMIZATION_FORCE_DWORD",
    "D2D1_SHADOW_PROP",
    "D2D1_SHADOW_PROP_BLUR_STANDARD_DEVIATION",
    "D2D1_SHADOW_PROP_COLOR",
    "D2D1_SHADOW_PROP_OPTIMIZATION",
    "D2D1_SHADOW_PROP_FORCE_DWORD",
    "D2D1_SHADOW_OPTIMIZATION",
    "D2D1_SHADOW_OPTIMIZATION_SPEED",
    "D2D1_SHADOW_OPTIMIZATION_BALANCED",
    "D2D1_SHADOW_OPTIMIZATION_QUALITY",
    "D2D1_SHADOW_OPTIMIZATION_FORCE_DWORD",
    "D2D1_BLEND_PROP",
    "D2D1_BLEND_PROP_MODE",
    "D2D1_BLEND_PROP_FORCE_DWORD",
    "D2D1_SATURATION_PROP",
    "D2D1_SATURATION_PROP_SATURATION",
    "D2D1_SATURATION_PROP_FORCE_DWORD",
    "D2D1_HUEROTATION_PROP",
    "D2D1_HUEROTATION_PROP_ANGLE",
    "D2D1_HUEROTATION_PROP_FORCE_DWORD",
    "D2D1_COLORMATRIX_PROP",
    "D2D1_COLORMATRIX_PROP_COLOR_MATRIX",
    "D2D1_COLORMATRIX_PROP_ALPHA_MODE",
    "D2D1_COLORMATRIX_PROP_CLAMP_OUTPUT",
    "D2D1_COLORMATRIX_PROP_FORCE_DWORD",
    "D2D1_BITMAPSOURCE_PROP",
    "D2D1_BITMAPSOURCE_PROP_WIC_BITMAP_SOURCE",
    "D2D1_BITMAPSOURCE_PROP_SCALE",
    "D2D1_BITMAPSOURCE_PROP_INTERPOLATION_MODE",
    "D2D1_BITMAPSOURCE_PROP_ENABLE_DPI_CORRECTION",
    "D2D1_BITMAPSOURCE_PROP_ALPHA_MODE",
    "D2D1_BITMAPSOURCE_PROP_ORIENTATION",
    "D2D1_BITMAPSOURCE_PROP_FORCE_DWORD",
    "D2D1_BITMAPSOURCE_INTERPOLATION_MODE",
    "D2D1_BITMAPSOURCE_INTERPOLATION_MODE_NEAREST_NEIGHBOR",
    "D2D1_BITMAPSOURCE_INTERPOLATION_MODE_LINEAR",
    "D2D1_BITMAPSOURCE_INTERPOLATION_MODE_CUBIC",
    "D2D1_BITMAPSOURCE_INTERPOLATION_MODE_FANT",
    "D2D1_BITMAPSOURCE_INTERPOLATION_MODE_MIPMAP_LINEAR",
    "D2D1_BITMAPSOURCE_INTERPOLATION_MODE_FORCE_DWORD",
    "D2D1_BITMAPSOURCE_ALPHA_MODE",
    "D2D1_BITMAPSOURCE_ALPHA_MODE_PREMULTIPLIED",
    "D2D1_BITMAPSOURCE_ALPHA_MODE_STRAIGHT",
    "D2D1_BITMAPSOURCE_ALPHA_MODE_FORCE_DWORD",
    "D2D1_COMPOSITE_PROP",
    "D2D1_COMPOSITE_PROP_MODE",
    "D2D1_COMPOSITE_PROP_FORCE_DWORD",
    "D2D1_3DTRANSFORM_PROP",
    "D2D1_3DTRANSFORM_PROP_INTERPOLATION_MODE",
    "D2D1_3DTRANSFORM_PROP_BORDER_MODE",
    "D2D1_3DTRANSFORM_PROP_TRANSFORM_MATRIX",
    "D2D1_3DTRANSFORM_PROP_FORCE_DWORD",
    "D2D1_3DTRANSFORM_INTERPOLATION_MODE",
    "D2D1_3DTRANSFORM_INTERPOLATION_MODE_NEAREST_NEIGHBOR",
    "D2D1_3DTRANSFORM_INTERPOLATION_MODE_LINEAR",
    "D2D1_3DTRANSFORM_INTERPOLATION_MODE_CUBIC",
    "D2D1_3DTRANSFORM_INTERPOLATION_MODE_MULTI_SAMPLE_LINEAR",
    "D2D1_3DTRANSFORM_INTERPOLATION_MODE_ANISOTROPIC",
    "D2D1_3DTRANSFORM_INTERPOLATION_MODE_FORCE_DWORD",
    "D2D1_3DPERSPECTIVETRANSFORM_PROP",
    "D2D1_3DPERSPECTIVETRANSFORM_PROP_INTERPOLATION_MODE",
    "D2D1_3DPERSPECTIVETRANSFORM_PROP_BORDER_MODE",
    "D2D1_3DPERSPECTIVETRANSFORM_PROP_DEPTH",
    "D2D1_3DPERSPECTIVETRANSFORM_PROP_PERSPECTIVE_ORIGIN",
    "D2D1_3DPERSPECTIVETRANSFORM_PROP_LOCAL_OFFSET",
    "D2D1_3DPERSPECTIVETRANSFORM_PROP_GLOBAL_OFFSET",
    "D2D1_3DPERSPECTIVETRANSFORM_PROP_ROTATION_ORIGIN",
    "D2D1_3DPERSPECTIVETRANSFORM_PROP_ROTATION",
    "D2D1_3DPERSPECTIVETRANSFORM_PROP_FORCE_DWORD",
    "D2D1_3DPERSPECTIVETRANSFORM_INTERPOLATION_MODE",
    "D2D1_3DPERSPECTIVETRANSFORM_INTERPOLATION_MODE_NEAREST_NEIGHBOR",
    "D2D1_3DPERSPECTIVETRANSFORM_INTERPOLATION_MODE_LINEAR",
    "D2D1_3DPERSPECTIVETRANSFORM_INTERPOLATION_MODE_CUBIC",
    "D2D1_3DPERSPECTIVETRANSFORM_INTERPOLATION_MODE_MULTI_SAMPLE_LINEAR",
    "D2D1_3DPERSPECTIVETRANSFORM_INTERPOLATION_MODE_ANISOTROPIC",
    "D2D1_3DPERSPECTIVETRANSFORM_INTERPOLATION_MODE_FORCE_DWORD",
    "D2D1_2DAFFINETRANSFORM_PROP",
    "D2D1_2DAFFINETRANSFORM_PROP_INTERPOLATION_MODE",
    "D2D1_2DAFFINETRANSFORM_PROP_BORDER_MODE",
    "D2D1_2DAFFINETRANSFORM_PROP_TRANSFORM_MATRIX",
    "D2D1_2DAFFINETRANSFORM_PROP_SHARPNESS",
    "D2D1_2DAFFINETRANSFORM_PROP_FORCE_DWORD",
    "D2D1_DPICOMPENSATION_PROP",
    "D2D1_DPICOMPENSATION_PROP_INTERPOLATION_MODE",
    "D2D1_DPICOMPENSATION_PROP_BORDER_MODE",
    "D2D1_DPICOMPENSATION_PROP_INPUT_DPI",
    "D2D1_DPICOMPENSATION_PROP_FORCE_DWORD",
    "D2D1_DPICOMPENSATION_INTERPOLATION_MODE",
    "D2D1_DPICOMPENSATION_INTERPOLATION_MODE_NEAREST_NEIGHBOR",
    "D2D1_DPICOMPENSATION_INTERPOLATION_MODE_LINEAR",
    "D2D1_DPICOMPENSATION_INTERPOLATION_MODE_CUBIC",
    "D2D1_DPICOMPENSATION_INTERPOLATION_MODE_MULTI_SAMPLE_LINEAR",
    "D2D1_DPICOMPENSATION_INTERPOLATION_MODE_ANISOTROPIC",
    "D2D1_DPICOMPENSATION_INTERPOLATION_MODE_HIGH_QUALITY_CUBIC",
    "D2D1_DPICOMPENSATION_INTERPOLATION_MODE_FORCE_DWORD",
    "D2D1_SCALE_PROP",
    "D2D1_SCALE_PROP_SCALE",
    "D2D1_SCALE_PROP_CENTER_POINT",
    "D2D1_SCALE_PROP_INTERPOLATION_MODE",
    "D2D1_SCALE_PROP_BORDER_MODE",
    "D2D1_SCALE_PROP_SHARPNESS",
    "D2D1_SCALE_PROP_FORCE_DWORD",
    "D2D1_SCALE_INTERPOLATION_MODE",
    "D2D1_SCALE_INTERPOLATION_MODE_NEAREST_NEIGHBOR",
    "D2D1_SCALE_INTERPOLATION_MODE_LINEAR",
    "D2D1_SCALE_INTERPOLATION_MODE_CUBIC",
    "D2D1_SCALE_INTERPOLATION_MODE_MULTI_SAMPLE_LINEAR",
    "D2D1_SCALE_INTERPOLATION_MODE_ANISOTROPIC",
    "D2D1_SCALE_INTERPOLATION_MODE_HIGH_QUALITY_CUBIC",
    "D2D1_SCALE_INTERPOLATION_MODE_FORCE_DWORD",
    "D2D1_TURBULENCE_PROP",
    "D2D1_TURBULENCE_PROP_OFFSET",
    "D2D1_TURBULENCE_PROP_SIZE",
    "D2D1_TURBULENCE_PROP_BASE_FREQUENCY",
    "D2D1_TURBULENCE_PROP_NUM_OCTAVES",
    "D2D1_TURBULENCE_PROP_SEED",
    "D2D1_TURBULENCE_PROP_NOISE",
    "D2D1_TURBULENCE_PROP_STITCHABLE",
    "D2D1_TURBULENCE_PROP_FORCE_DWORD",
    "D2D1_DISPLACEMENTMAP_PROP",
    "D2D1_DISPLACEMENTMAP_PROP_SCALE",
    "D2D1_DISPLACEMENTMAP_PROP_X_CHANNEL_SELECT",
    "D2D1_DISPLACEMENTMAP_PROP_Y_CHANNEL_SELECT",
    "D2D1_DISPLACEMENTMAP_PROP_FORCE_DWORD",
    "D2D1_COLORMANAGEMENT_PROP",
    "D2D1_COLORMANAGEMENT_PROP_SOURCE_COLOR_CONTEXT",
    "D2D1_COLORMANAGEMENT_PROP_SOURCE_RENDERING_INTENT",
    "D2D1_COLORMANAGEMENT_PROP_DESTINATION_COLOR_CONTEXT",
    "D2D1_COLORMANAGEMENT_PROP_DESTINATION_RENDERING_INTENT",
    "D2D1_COLORMANAGEMENT_PROP_ALPHA_MODE",
    "D2D1_COLORMANAGEMENT_PROP_QUALITY",
    "D2D1_COLORMANAGEMENT_PROP_FORCE_DWORD",
    "D2D1_COLORMANAGEMENT_ALPHA_MODE",
    "D2D1_COLORMANAGEMENT_ALPHA_MODE_PREMULTIPLIED",
    "D2D1_COLORMANAGEMENT_ALPHA_MODE_STRAIGHT",
    "D2D1_COLORMANAGEMENT_ALPHA_MODE_FORCE_DWORD",
    "D2D1_COLORMANAGEMENT_QUALITY",
    "D2D1_COLORMANAGEMENT_QUALITY_PROOF",
    "D2D1_COLORMANAGEMENT_QUALITY_NORMAL",
    "D2D1_COLORMANAGEMENT_QUALITY_BEST",
    "D2D1_COLORMANAGEMENT_QUALITY_FORCE_DWORD",
    "D2D1_COLORMANAGEMENT_RENDERING_INTENT",
    "D2D1_COLORMANAGEMENT_RENDERING_INTENT_PERCEPTUAL",
    "D2D1_COLORMANAGEMENT_RENDERING_INTENT_RELATIVE_COLORIMETRIC",
    "D2D1_COLORMANAGEMENT_RENDERING_INTENT_SATURATION",
    "D2D1_COLORMANAGEMENT_RENDERING_INTENT_ABSOLUTE_COLORIMETRIC",
    "D2D1_COLORMANAGEMENT_RENDERING_INTENT_FORCE_DWORD",
    "D2D1_HISTOGRAM_PROP",
    "D2D1_HISTOGRAM_PROP_NUM_BINS",
    "D2D1_HISTOGRAM_PROP_CHANNEL_SELECT",
    "D2D1_HISTOGRAM_PROP_HISTOGRAM_OUTPUT",
    "D2D1_HISTOGRAM_PROP_FORCE_DWORD",
    "D2D1_POINTSPECULAR_PROP",
    "D2D1_POINTSPECULAR_PROP_LIGHT_POSITION",
    "D2D1_POINTSPECULAR_PROP_SPECULAR_EXPONENT",
    "D2D1_POINTSPECULAR_PROP_SPECULAR_CONSTANT",
    "D2D1_POINTSPECULAR_PROP_SURFACE_SCALE",
    "D2D1_POINTSPECULAR_PROP_COLOR",
    "D2D1_POINTSPECULAR_PROP_KERNEL_UNIT_LENGTH",
    "D2D1_POINTSPECULAR_PROP_SCALE_MODE",
    "D2D1_POINTSPECULAR_PROP_FORCE_DWORD",
    "D2D1_POINTSPECULAR_SCALE_MODE",
    "D2D1_POINTSPECULAR_SCALE_MODE_NEAREST_NEIGHBOR",
    "D2D1_POINTSPECULAR_SCALE_MODE_LINEAR",
    "D2D1_POINTSPECULAR_SCALE_MODE_CUBIC",
    "D2D1_POINTSPECULAR_SCALE_MODE_MULTI_SAMPLE_LINEAR",
    "D2D1_POINTSPECULAR_SCALE_MODE_ANISOTROPIC",
    "D2D1_POINTSPECULAR_SCALE_MODE_HIGH_QUALITY_CUBIC",
    "D2D1_POINTSPECULAR_SCALE_MODE_FORCE_DWORD",
    "D2D1_SPOTSPECULAR_PROP",
    "D2D1_SPOTSPECULAR_PROP_LIGHT_POSITION",
    "D2D1_SPOTSPECULAR_PROP_POINTS_AT",
    "D2D1_SPOTSPECULAR_PROP_FOCUS",
    "D2D1_SPOTSPECULAR_PROP_LIMITING_CONE_ANGLE",
    "D2D1_SPOTSPECULAR_PROP_SPECULAR_EXPONENT",
    "D2D1_SPOTSPECULAR_PROP_SPECULAR_CONSTANT",
    "D2D1_SPOTSPECULAR_PROP_SURFACE_SCALE",
    "D2D1_SPOTSPECULAR_PROP_COLOR",
    "D2D1_SPOTSPECULAR_PROP_KERNEL_UNIT_LENGTH",
    "D2D1_SPOTSPECULAR_PROP_SCALE_MODE",
    "D2D1_SPOTSPECULAR_PROP_FORCE_DWORD",
    "D2D1_SPOTSPECULAR_SCALE_MODE",
    "D2D1_SPOTSPECULAR_SCALE_MODE_NEAREST_NEIGHBOR",
    "D2D1_SPOTSPECULAR_SCALE_MODE_LINEAR",
    "D2D1_SPOTSPECULAR_SCALE_MODE_CUBIC",
    "D2D1_SPOTSPECULAR_SCALE_MODE_MULTI_SAMPLE_LINEAR",
    "D2D1_SPOTSPECULAR_SCALE_MODE_ANISOTROPIC",
    "D2D1_SPOTSPECULAR_SCALE_MODE_HIGH_QUALITY_CUBIC",
    "D2D1_SPOTSPECULAR_SCALE_MODE_FORCE_DWORD",
    "D2D1_DISTANTSPECULAR_PROP",
    "D2D1_DISTANTSPECULAR_PROP_AZIMUTH",
    "D2D1_DISTANTSPECULAR_PROP_ELEVATION",
    "D2D1_DISTANTSPECULAR_PROP_SPECULAR_EXPONENT",
    "D2D1_DISTANTSPECULAR_PROP_SPECULAR_CONSTANT",
    "D2D1_DISTANTSPECULAR_PROP_SURFACE_SCALE",
    "D2D1_DISTANTSPECULAR_PROP_COLOR",
    "D2D1_DISTANTSPECULAR_PROP_KERNEL_UNIT_LENGTH",
    "D2D1_DISTANTSPECULAR_PROP_SCALE_MODE",
    "D2D1_DISTANTSPECULAR_PROP_FORCE_DWORD",
    "D2D1_DISTANTSPECULAR_SCALE_MODE",
    "D2D1_DISTANTSPECULAR_SCALE_MODE_NEAREST_NEIGHBOR",
    "D2D1_DISTANTSPECULAR_SCALE_MODE_LINEAR",
    "D2D1_DISTANTSPECULAR_SCALE_MODE_CUBIC",
    "D2D1_DISTANTSPECULAR_SCALE_MODE_MULTI_SAMPLE_LINEAR",
    "D2D1_DISTANTSPECULAR_SCALE_MODE_ANISOTROPIC",
    "D2D1_DISTANTSPECULAR_SCALE_MODE_HIGH_QUALITY_CUBIC",
    "D2D1_DISTANTSPECULAR_SCALE_MODE_FORCE_DWORD",
    "D2D1_POINTDIFFUSE_PROP",
    "D2D1_POINTDIFFUSE_PROP_LIGHT_POSITION",
    "D2D1_POINTDIFFUSE_PROP_DIFFUSE_CONSTANT",
    "D2D1_POINTDIFFUSE_PROP_SURFACE_SCALE",
    "D2D1_POINTDIFFUSE_PROP_COLOR",
    "D2D1_POINTDIFFUSE_PROP_KERNEL_UNIT_LENGTH",
    "D2D1_POINTDIFFUSE_PROP_SCALE_MODE",
    "D2D1_POINTDIFFUSE_PROP_FORCE_DWORD",
    "D2D1_POINTDIFFUSE_SCALE_MODE",
    "D2D1_POINTDIFFUSE_SCALE_MODE_NEAREST_NEIGHBOR",
    "D2D1_POINTDIFFUSE_SCALE_MODE_LINEAR",
    "D2D1_POINTDIFFUSE_SCALE_MODE_CUBIC",
    "D2D1_POINTDIFFUSE_SCALE_MODE_MULTI_SAMPLE_LINEAR",
    "D2D1_POINTDIFFUSE_SCALE_MODE_ANISOTROPIC",
    "D2D1_POINTDIFFUSE_SCALE_MODE_HIGH_QUALITY_CUBIC",
    "D2D1_POINTDIFFUSE_SCALE_MODE_FORCE_DWORD",
    "D2D1_SPOTDIFFUSE_PROP",
    "D2D1_SPOTDIFFUSE_PROP_LIGHT_POSITION",
    "D2D1_SPOTDIFFUSE_PROP_POINTS_AT",
    "D2D1_SPOTDIFFUSE_PROP_FOCUS",
    "D2D1_SPOTDIFFUSE_PROP_LIMITING_CONE_ANGLE",
    "D2D1_SPOTDIFFUSE_PROP_DIFFUSE_CONSTANT",
    "D2D1_SPOTDIFFUSE_PROP_SURFACE_SCALE",
    "D2D1_SPOTDIFFUSE_PROP_COLOR",
    "D2D1_SPOTDIFFUSE_PROP_KERNEL_UNIT_LENGTH",
    "D2D1_SPOTDIFFUSE_PROP_SCALE_MODE",
    "D2D1_SPOTDIFFUSE_PROP_FORCE_DWORD",
    "D2D1_SPOTDIFFUSE_SCALE_MODE",
    "D2D1_SPOTDIFFUSE_SCALE_MODE_NEAREST_NEIGHBOR",
    "D2D1_SPOTDIFFUSE_SCALE_MODE_LINEAR",
    "D2D1_SPOTDIFFUSE_SCALE_MODE_CUBIC",
    "D2D1_SPOTDIFFUSE_SCALE_MODE_MULTI_SAMPLE_LINEAR",
    "D2D1_SPOTDIFFUSE_SCALE_MODE_ANISOTROPIC",
    "D2D1_SPOTDIFFUSE_SCALE_MODE_HIGH_QUALITY_CUBIC",
    "D2D1_SPOTDIFFUSE_SCALE_MODE_FORCE_DWORD",
    "D2D1_DISTANTDIFFUSE_PROP",
    "D2D1_DISTANTDIFFUSE_PROP_AZIMUTH",
    "D2D1_DISTANTDIFFUSE_PROP_ELEVATION",
    "D2D1_DISTANTDIFFUSE_PROP_DIFFUSE_CONSTANT",
    "D2D1_DISTANTDIFFUSE_PROP_SURFACE_SCALE",
    "D2D1_DISTANTDIFFUSE_PROP_COLOR",
    "D2D1_DISTANTDIFFUSE_PROP_KERNEL_UNIT_LENGTH",
    "D2D1_DISTANTDIFFUSE_PROP_SCALE_MODE",
    "D2D1_DISTANTDIFFUSE_PROP_FORCE_DWORD",
    "D2D1_DISTANTDIFFUSE_SCALE_MODE",
    "D2D1_DISTANTDIFFUSE_SCALE_MODE_NEAREST_NEIGHBOR",
    "D2D1_DISTANTDIFFUSE_SCALE_MODE_LINEAR",
    "D2D1_DISTANTDIFFUSE_SCALE_MODE_CUBIC",
    "D2D1_DISTANTDIFFUSE_SCALE_MODE_MULTI_SAMPLE_LINEAR",
    "D2D1_DISTANTDIFFUSE_SCALE_MODE_ANISOTROPIC",
    "D2D1_DISTANTDIFFUSE_SCALE_MODE_HIGH_QUALITY_CUBIC",
    "D2D1_DISTANTDIFFUSE_SCALE_MODE_FORCE_DWORD",
    "D2D1_FLOOD_PROP",
    "D2D1_FLOOD_PROP_COLOR",
    "D2D1_FLOOD_PROP_FORCE_DWORD",
    "D2D1_LINEARTRANSFER_PROP",
    "D2D1_LINEARTRANSFER_PROP_RED_Y_INTERCEPT",
    "D2D1_LINEARTRANSFER_PROP_RED_SLOPE",
    "D2D1_LINEARTRANSFER_PROP_RED_DISABLE",
    "D2D1_LINEARTRANSFER_PROP_GREEN_Y_INTERCEPT",
    "D2D1_LINEARTRANSFER_PROP_GREEN_SLOPE",
    "D2D1_LINEARTRANSFER_PROP_GREEN_DISABLE",
    "D2D1_LINEARTRANSFER_PROP_BLUE_Y_INTERCEPT",
    "D2D1_LINEARTRANSFER_PROP_BLUE_SLOPE",
    "D2D1_LINEARTRANSFER_PROP_BLUE_DISABLE",
    "D2D1_LINEARTRANSFER_PROP_ALPHA_Y_INTERCEPT",
    "D2D1_LINEARTRANSFER_PROP_ALPHA_SLOPE",
    "D2D1_LINEARTRANSFER_PROP_ALPHA_DISABLE",
    "D2D1_LINEARTRANSFER_PROP_CLAMP_OUTPUT",
    "D2D1_LINEARTRANSFER_PROP_FORCE_DWORD",
    "D2D1_GAMMATRANSFER_PROP",
    "D2D1_GAMMATRANSFER_PROP_RED_AMPLITUDE",
    "D2D1_GAMMATRANSFER_PROP_RED_EXPONENT",
    "D2D1_GAMMATRANSFER_PROP_RED_OFFSET",
    "D2D1_GAMMATRANSFER_PROP_RED_DISABLE",
    "D2D1_GAMMATRANSFER_PROP_GREEN_AMPLITUDE",
    "D2D1_GAMMATRANSFER_PROP_GREEN_EXPONENT",
    "D2D1_GAMMATRANSFER_PROP_GREEN_OFFSET",
    "D2D1_GAMMATRANSFER_PROP_GREEN_DISABLE",
    "D2D1_GAMMATRANSFER_PROP_BLUE_AMPLITUDE",
    "D2D1_GAMMATRANSFER_PROP_BLUE_EXPONENT",
    "D2D1_GAMMATRANSFER_PROP_BLUE_OFFSET",
    "D2D1_GAMMATRANSFER_PROP_BLUE_DISABLE",
    "D2D1_GAMMATRANSFER_PROP_ALPHA_AMPLITUDE",
    "D2D1_GAMMATRANSFER_PROP_ALPHA_EXPONENT",
    "D2D1_GAMMATRANSFER_PROP_ALPHA_OFFSET",
    "D2D1_GAMMATRANSFER_PROP_ALPHA_DISABLE",
    "D2D1_GAMMATRANSFER_PROP_CLAMP_OUTPUT",
    "D2D1_GAMMATRANSFER_PROP_FORCE_DWORD",
    "D2D1_TABLETRANSFER_PROP",
    "D2D1_TABLETRANSFER_PROP_RED_TABLE",
    "D2D1_TABLETRANSFER_PROP_RED_DISABLE",
    "D2D1_TABLETRANSFER_PROP_GREEN_TABLE",
    "D2D1_TABLETRANSFER_PROP_GREEN_DISABLE",
    "D2D1_TABLETRANSFER_PROP_BLUE_TABLE",
    "D2D1_TABLETRANSFER_PROP_BLUE_DISABLE",
    "D2D1_TABLETRANSFER_PROP_ALPHA_TABLE",
    "D2D1_TABLETRANSFER_PROP_ALPHA_DISABLE",
    "D2D1_TABLETRANSFER_PROP_CLAMP_OUTPUT",
    "D2D1_TABLETRANSFER_PROP_FORCE_DWORD",
    "D2D1_DISCRETETRANSFER_PROP",
    "D2D1_DISCRETETRANSFER_PROP_RED_TABLE",
    "D2D1_DISCRETETRANSFER_PROP_RED_DISABLE",
    "D2D1_DISCRETETRANSFER_PROP_GREEN_TABLE",
    "D2D1_DISCRETETRANSFER_PROP_GREEN_DISABLE",
    "D2D1_DISCRETETRANSFER_PROP_BLUE_TABLE",
    "D2D1_DISCRETETRANSFER_PROP_BLUE_DISABLE",
    "D2D1_DISCRETETRANSFER_PROP_ALPHA_TABLE",
    "D2D1_DISCRETETRANSFER_PROP_ALPHA_DISABLE",
    "D2D1_DISCRETETRANSFER_PROP_CLAMP_OUTPUT",
    "D2D1_DISCRETETRANSFER_PROP_FORCE_DWORD",
    "D2D1_CONVOLVEMATRIX_PROP",
    "D2D1_CONVOLVEMATRIX_PROP_KERNEL_UNIT_LENGTH",
    "D2D1_CONVOLVEMATRIX_PROP_SCALE_MODE",
    "D2D1_CONVOLVEMATRIX_PROP_KERNEL_SIZE_X",
    "D2D1_CONVOLVEMATRIX_PROP_KERNEL_SIZE_Y",
    "D2D1_CONVOLVEMATRIX_PROP_KERNEL_MATRIX",
    "D2D1_CONVOLVEMATRIX_PROP_DIVISOR",
    "D2D1_CONVOLVEMATRIX_PROP_BIAS",
    "D2D1_CONVOLVEMATRIX_PROP_KERNEL_OFFSET",
    "D2D1_CONVOLVEMATRIX_PROP_PRESERVE_ALPHA",
    "D2D1_CONVOLVEMATRIX_PROP_BORDER_MODE",
    "D2D1_CONVOLVEMATRIX_PROP_CLAMP_OUTPUT",
    "D2D1_CONVOLVEMATRIX_PROP_FORCE_DWORD",
    "D2D1_CONVOLVEMATRIX_SCALE_MODE",
    "D2D1_CONVOLVEMATRIX_SCALE_MODE_NEAREST_NEIGHBOR",
    "D2D1_CONVOLVEMATRIX_SCALE_MODE_LINEAR",
    "D2D1_CONVOLVEMATRIX_SCALE_MODE_CUBIC",
    "D2D1_CONVOLVEMATRIX_SCALE_MODE_MULTI_SAMPLE_LINEAR",
    "D2D1_CONVOLVEMATRIX_SCALE_MODE_ANISOTROPIC",
    "D2D1_CONVOLVEMATRIX_SCALE_MODE_HIGH_QUALITY_CUBIC",
    "D2D1_CONVOLVEMATRIX_SCALE_MODE_FORCE_DWORD",
    "D2D1_BRIGHTNESS_PROP",
    "D2D1_BRIGHTNESS_PROP_WHITE_POINT",
    "D2D1_BRIGHTNESS_PROP_BLACK_POINT",
    "D2D1_BRIGHTNESS_PROP_FORCE_DWORD",
    "D2D1_ARITHMETICCOMPOSITE_PROP",
    "D2D1_ARITHMETICCOMPOSITE_PROP_COEFFICIENTS",
    "D2D1_ARITHMETICCOMPOSITE_PROP_CLAMP_OUTPUT",
    "D2D1_ARITHMETICCOMPOSITE_PROP_FORCE_DWORD",
    "D2D1_CROP_PROP",
    "D2D1_CROP_PROP_RECT",
    "D2D1_CROP_PROP_BORDER_MODE",
    "D2D1_CROP_PROP_FORCE_DWORD",
    "D2D1_BORDER_PROP",
    "D2D1_BORDER_PROP_EDGE_MODE_X",
    "D2D1_BORDER_PROP_EDGE_MODE_Y",
    "D2D1_BORDER_PROP_FORCE_DWORD",
    "D2D1_BORDER_EDGE_MODE",
    "D2D1_BORDER_EDGE_MODE_CLAMP",
    "D2D1_BORDER_EDGE_MODE_WRAP",
    "D2D1_BORDER_EDGE_MODE_MIRROR",
    "D2D1_BORDER_EDGE_MODE_FORCE_DWORD",
    "D2D1_MORPHOLOGY_PROP",
    "D2D1_MORPHOLOGY_PROP_MODE",
    "D2D1_MORPHOLOGY_PROP_WIDTH",
    "D2D1_MORPHOLOGY_PROP_HEIGHT",
    "D2D1_MORPHOLOGY_PROP_FORCE_DWORD",
    "D2D1_MORPHOLOGY_MODE",
    "D2D1_MORPHOLOGY_MODE_ERODE",
    "D2D1_MORPHOLOGY_MODE_DILATE",
    "D2D1_MORPHOLOGY_MODE_FORCE_DWORD",
    "D2D1_TILE_PROP",
    "D2D1_TILE_PROP_RECT",
    "D2D1_TILE_PROP_FORCE_DWORD",
    "D2D1_ATLAS_PROP",
    "D2D1_ATLAS_PROP_INPUT_RECT",
    "D2D1_ATLAS_PROP_INPUT_PADDING_RECT",
    "D2D1_ATLAS_PROP_FORCE_DWORD",
    "D2D1_OPACITYMETADATA_PROP",
    "D2D1_OPACITYMETADATA_PROP_INPUT_OPAQUE_RECT",
    "D2D1_OPACITYMETADATA_PROP_FORCE_DWORD",
    "PD2D1_EFFECT_FACTORY",
    "D2D1_PROPERTY_TYPE",
    "D2D1_PROPERTY_TYPE_UNKNOWN",
    "D2D1_PROPERTY_TYPE_STRING",
    "D2D1_PROPERTY_TYPE_BOOL",
    "D2D1_PROPERTY_TYPE_UINT32",
    "D2D1_PROPERTY_TYPE_INT32",
    "D2D1_PROPERTY_TYPE_FLOAT",
    "D2D1_PROPERTY_TYPE_VECTOR2",
    "D2D1_PROPERTY_TYPE_VECTOR3",
    "D2D1_PROPERTY_TYPE_VECTOR4",
    "D2D1_PROPERTY_TYPE_BLOB",
    "D2D1_PROPERTY_TYPE_IUNKNOWN",
    "D2D1_PROPERTY_TYPE_ENUM",
    "D2D1_PROPERTY_TYPE_ARRAY",
    "D2D1_PROPERTY_TYPE_CLSID",
    "D2D1_PROPERTY_TYPE_MATRIX_3X2",
    "D2D1_PROPERTY_TYPE_MATRIX_4X3",
    "D2D1_PROPERTY_TYPE_MATRIX_4X4",
    "D2D1_PROPERTY_TYPE_MATRIX_5X4",
    "D2D1_PROPERTY_TYPE_COLOR_CONTEXT",
    "D2D1_PROPERTY_TYPE_FORCE_DWORD",
    "D2D1_PROPERTY",
    "D2D1_PROPERTY_CLSID",
    "D2D1_PROPERTY_DISPLAYNAME",
    "D2D1_PROPERTY_AUTHOR",
    "D2D1_PROPERTY_CATEGORY",
    "D2D1_PROPERTY_DESCRIPTION",
    "D2D1_PROPERTY_INPUTS",
    "D2D1_PROPERTY_CACHED",
    "D2D1_PROPERTY_PRECISION",
    "D2D1_PROPERTY_MIN_INPUTS",
    "D2D1_PROPERTY_MAX_INPUTS",
    "D2D1_PROPERTY_FORCE_DWORD",
    "D2D1_SUBPROPERTY",
    "D2D1_SUBPROPERTY_DISPLAYNAME",
    "D2D1_SUBPROPERTY_ISREADONLY",
    "D2D1_SUBPROPERTY_MIN",
    "D2D1_SUBPROPERTY_MAX",
    "D2D1_SUBPROPERTY_DEFAULT",
    "D2D1_SUBPROPERTY_FIELDS",
    "D2D1_SUBPROPERTY_INDEX",
    "D2D1_SUBPROPERTY_FORCE_DWORD",
    "D2D1_BITMAP_OPTIONS",
    "D2D1_BITMAP_OPTIONS_NONE",
    "D2D1_BITMAP_OPTIONS_TARGET",
    "D2D1_BITMAP_OPTIONS_CANNOT_DRAW",
    "D2D1_BITMAP_OPTIONS_CPU_READ",
    "D2D1_BITMAP_OPTIONS_GDI_COMPATIBLE",
    "D2D1_BITMAP_OPTIONS_FORCE_DWORD",
    "D2D1_BUFFER_PRECISION",
    "D2D1_BUFFER_PRECISION_UNKNOWN",
    "D2D1_BUFFER_PRECISION_8BPC_UNORM",
    "D2D1_BUFFER_PRECISION_8BPC_UNORM_SRGB",
    "D2D1_BUFFER_PRECISION_16BPC_UNORM",
    "D2D1_BUFFER_PRECISION_16BPC_FLOAT",
    "D2D1_BUFFER_PRECISION_32BPC_FLOAT",
    "D2D1_BUFFER_PRECISION_FORCE_DWORD",
    "D2D1_MAP_OPTIONS",
    "D2D1_MAP_OPTIONS_NONE",
    "D2D1_MAP_OPTIONS_READ",
    "D2D1_MAP_OPTIONS_WRITE",
    "D2D1_MAP_OPTIONS_DISCARD",
    "D2D1_MAP_OPTIONS_FORCE_DWORD",
    "D2D1_INTERPOLATION_MODE",
    "D2D1_INTERPOLATION_MODE_NEAREST_NEIGHBOR",
    "D2D1_INTERPOLATION_MODE_LINEAR",
    "D2D1_INTERPOLATION_MODE_CUBIC",
    "D2D1_INTERPOLATION_MODE_MULTI_SAMPLE_LINEAR",
    "D2D1_INTERPOLATION_MODE_ANISOTROPIC",
    "D2D1_INTERPOLATION_MODE_HIGH_QUALITY_CUBIC",
    "D2D1_INTERPOLATION_MODE_FORCE_DWORD",
    "D2D1_UNIT_MODE",
    "D2D1_UNIT_MODE_DIPS",
    "D2D1_UNIT_MODE_PIXELS",
    "D2D1_UNIT_MODE_FORCE_DWORD",
    "D2D1_COLOR_SPACE",
    "D2D1_COLOR_SPACE_CUSTOM",
    "D2D1_COLOR_SPACE_SRGB",
    "D2D1_COLOR_SPACE_SCRGB",
    "D2D1_COLOR_SPACE_FORCE_DWORD",
    "D2D1_DEVICE_CONTEXT_OPTIONS",
    "D2D1_DEVICE_CONTEXT_OPTIONS_NONE",
    "D2D1_DEVICE_CONTEXT_OPTIONS_ENABLE_MULTITHREADED_OPTIMIZATIONS",
    "D2D1_DEVICE_CONTEXT_OPTIONS_FORCE_DWORD",
    "D2D1_STROKE_TRANSFORM_TYPE",
    "D2D1_STROKE_TRANSFORM_TYPE_NORMAL",
    "D2D1_STROKE_TRANSFORM_TYPE_FIXED",
    "D2D1_STROKE_TRANSFORM_TYPE_HAIRLINE",
    "D2D1_STROKE_TRANSFORM_TYPE_FORCE_DWORD",
    "D2D1_PRIMITIVE_BLEND",
    "D2D1_PRIMITIVE_BLEND_SOURCE_OVER",
    "D2D1_PRIMITIVE_BLEND_COPY",
    "D2D1_PRIMITIVE_BLEND_MIN",
    "D2D1_PRIMITIVE_BLEND_ADD",
    "D2D1_PRIMITIVE_BLEND_MAX",
    "D2D1_PRIMITIVE_BLEND_FORCE_DWORD",
    "D2D1_THREADING_MODE",
    "D2D1_THREADING_MODE_SINGLE_THREADED",
    "D2D1_THREADING_MODE_MULTI_THREADED",
    "D2D1_THREADING_MODE_FORCE_DWORD",
    "D2D1_COLOR_INTERPOLATION_MODE",
    "D2D1_COLOR_INTERPOLATION_MODE_STRAIGHT",
    "D2D1_COLOR_INTERPOLATION_MODE_PREMULTIPLIED",
    "D2D1_COLOR_INTERPOLATION_MODE_FORCE_DWORD",
    "D2D1_BITMAP_PROPERTIES1",
    "D2D1_MAPPED_RECT",
    "D2D1_RENDERING_CONTROLS",
    "D2D1_EFFECT_INPUT_DESCRIPTION",
    "D2D1_POINT_DESCRIPTION",
    "D2D1_IMAGE_BRUSH_PROPERTIES",
    "D2D1_BITMAP_BRUSH_PROPERTIES1",
    "D2D1_STROKE_STYLE_PROPERTIES1",
    "D2D1_LAYER_OPTIONS1",
    "D2D1_LAYER_OPTIONS1_NONE",
    "D2D1_LAYER_OPTIONS1_INITIALIZE_FROM_BACKGROUND",
    "D2D1_LAYER_OPTIONS1_IGNORE_ALPHA",
    "D2D1_LAYER_OPTIONS1_FORCE_DWORD",
    "D2D1_LAYER_PARAMETERS1",
    "D2D1_PRINT_FONT_SUBSET_MODE",
    "D2D1_PRINT_FONT_SUBSET_MODE_DEFAULT",
    "D2D1_PRINT_FONT_SUBSET_MODE_EACHPAGE",
    "D2D1_PRINT_FONT_SUBSET_MODE_NONE",
    "D2D1_PRINT_FONT_SUBSET_MODE_FORCE_DWORD",
    "D2D1_DRAWING_STATE_DESCRIPTION1",
    "D2D1_PRINT_CONTROL_PROPERTIES",
    "D2D1_CREATION_PROPERTIES",
    "ID2D1GdiMetafileSink",
    "ID2D1GdiMetafile",
    "ID2D1CommandSink",
    "ID2D1CommandList",
    "ID2D1PrintControl",
    "ID2D1ImageBrush",
    "ID2D1BitmapBrush1",
    "ID2D1StrokeStyle1",
    "ID2D1PathGeometry1",
    "ID2D1Properties",
    "ID2D1Effect",
    "ID2D1Bitmap1",
    "ID2D1ColorContext",
    "ID2D1GradientStopCollection1",
    "ID2D1DrawingStateBlock1",
    "ID2D1DeviceContext",
    "ID2D1Device",
    "ID2D1Factory1",
    "ID2D1Multithread",
    "Matrix4x3F",
    "Matrix4x4F",
    "Matrix5x4F",
    "PD2D1_PROPERTY_SET_FUNCTION",
    "PD2D1_PROPERTY_GET_FUNCTION",
    "D2D1_CHANGE_TYPE",
    "D2D1_CHANGE_TYPE_NONE",
    "D2D1_CHANGE_TYPE_PROPERTIES",
    "D2D1_CHANGE_TYPE_CONTEXT",
    "D2D1_CHANGE_TYPE_GRAPH",
    "D2D1_CHANGE_TYPE_FORCE_DWORD",
    "D2D1_PIXEL_OPTIONS",
    "D2D1_PIXEL_OPTIONS_NONE",
    "D2D1_PIXEL_OPTIONS_TRIVIAL_SAMPLING",
    "D2D1_PIXEL_OPTIONS_FORCE_DWORD",
    "D2D1_VERTEX_OPTIONS",
    "D2D1_VERTEX_OPTIONS_NONE",
    "D2D1_VERTEX_OPTIONS_DO_NOT_CLEAR",
    "D2D1_VERTEX_OPTIONS_USE_DEPTH_BUFFER",
    "D2D1_VERTEX_OPTIONS_ASSUME_NO_OVERLAP",
    "D2D1_VERTEX_OPTIONS_FORCE_DWORD",
    "D2D1_VERTEX_USAGE",
    "D2D1_VERTEX_USAGE_STATIC",
    "D2D1_VERTEX_USAGE_DYNAMIC",
    "D2D1_VERTEX_USAGE_FORCE_DWORD",
    "D2D1_BLEND_OPERATION",
    "D2D1_BLEND_OPERATION_ADD",
    "D2D1_BLEND_OPERATION_SUBTRACT",
    "D2D1_BLEND_OPERATION_REV_SUBTRACT",
    "D2D1_BLEND_OPERATION_MIN",
    "D2D1_BLEND_OPERATION_MAX",
    "D2D1_BLEND_OPERATION_FORCE_DWORD",
    "D2D1_BLEND",
    "D2D1_BLEND_ZERO",
    "D2D1_BLEND_ONE",
    "D2D1_BLEND_SRC_COLOR",
    "D2D1_BLEND_INV_SRC_COLOR",
    "D2D1_BLEND_SRC_ALPHA",
    "D2D1_BLEND_INV_SRC_ALPHA",
    "D2D1_BLEND_DEST_ALPHA",
    "D2D1_BLEND_INV_DEST_ALPHA",
    "D2D1_BLEND_DEST_COLOR",
    "D2D1_BLEND_INV_DEST_COLOR",
    "D2D1_BLEND_SRC_ALPHA_SAT",
    "D2D1_BLEND_BLEND_FACTOR",
    "D2D1_BLEND_INV_BLEND_FACTOR",
    "D2D1_BLEND_FORCE_DWORD",
    "D2D1_CHANNEL_DEPTH",
    "D2D1_CHANNEL_DEPTH_DEFAULT",
    "D2D1_CHANNEL_DEPTH_1",
    "D2D1_CHANNEL_DEPTH_4",
    "D2D1_CHANNEL_DEPTH_FORCE_DWORD",
    "D2D1_FILTER",
    "D2D1_FILTER_MIN_MAG_MIP_POINT",
    "D2D1_FILTER_MIN_MAG_POINT_MIP_LINEAR",
    "D2D1_FILTER_MIN_POINT_MAG_LINEAR_MIP_POINT",
    "D2D1_FILTER_MIN_POINT_MAG_MIP_LINEAR",
    "D2D1_FILTER_MIN_LINEAR_MAG_MIP_POINT",
    "D2D1_FILTER_MIN_LINEAR_MAG_POINT_MIP_LINEAR",
    "D2D1_FILTER_MIN_MAG_LINEAR_MIP_POINT",
    "D2D1_FILTER_MIN_MAG_MIP_LINEAR",
    "D2D1_FILTER_ANISOTROPIC",
    "D2D1_FILTER_FORCE_DWORD",
    "D2D1_FEATURE",
    "D2D1_FEATURE_DOUBLES",
    "D2D1_FEATURE_D3D10_X_HARDWARE_OPTIONS",
    "D2D1_FEATURE_FORCE_DWORD",
    "D2D1_PROPERTY_BINDING",
    "D2D1_RESOURCE_TEXTURE_PROPERTIES",
    "D2D1_INPUT_ELEMENT_DESC",
    "D2D1_VERTEX_BUFFER_PROPERTIES",
    "D2D1_CUSTOM_VERTEX_BUFFER_PROPERTIES",
    "D2D1_VERTEX_RANGE",
    "D2D1_BLEND_DESCRIPTION",
    "D2D1_INPUT_DESCRIPTION",
    "D2D1_FEATURE_DATA_DOUBLES",
    "D2D1_FEATURE_DATA_D3D10_X_HARDWARE_OPTIONS",
    "ID2D1VertexBuffer",
    "ID2D1ResourceTexture",
    "ID2D1RenderInfo",
    "ID2D1DrawInfo",
    "ID2D1ComputeInfo",
    "ID2D1TransformNode",
    "ID2D1TransformGraph",
    "ID2D1Transform",
    "ID2D1DrawTransform",
    "ID2D1ComputeTransform",
    "ID2D1AnalysisTransform",
    "ID2D1SourceTransform",
    "ID2D1ConcreteTransform",
    "ID2D1BlendTransform",
    "ID2D1BorderTransform",
    "ID2D1OffsetTransform",
    "ID2D1BoundsAdjustmentTransform",
    "ID2D1EffectImpl",
    "ID2D1EffectContext",
    "D2D1_YCBCR_PROP",
    "D2D1_YCBCR_PROP_CHROMA_SUBSAMPLING",
    "D2D1_YCBCR_PROP_TRANSFORM_MATRIX",
    "D2D1_YCBCR_PROP_INTERPOLATION_MODE",
    "D2D1_YCBCR_PROP_FORCE_DWORD",
    "D2D1_YCBCR_CHROMA_SUBSAMPLING",
    "D2D1_YCBCR_CHROMA_SUBSAMPLING_AUTO",
    "D2D1_YCBCR_CHROMA_SUBSAMPLING_420",
    "D2D1_YCBCR_CHROMA_SUBSAMPLING_422",
    "D2D1_YCBCR_CHROMA_SUBSAMPLING_444",
    "D2D1_YCBCR_CHROMA_SUBSAMPLING_440",
    "D2D1_YCBCR_CHROMA_SUBSAMPLING_FORCE_DWORD",
    "D2D1_YCBCR_INTERPOLATION_MODE",
    "D2D1_YCBCR_INTERPOLATION_MODE_NEAREST_NEIGHBOR",
    "D2D1_YCBCR_INTERPOLATION_MODE_LINEAR",
    "D2D1_YCBCR_INTERPOLATION_MODE_CUBIC",
    "D2D1_YCBCR_INTERPOLATION_MODE_MULTI_SAMPLE_LINEAR",
    "D2D1_YCBCR_INTERPOLATION_MODE_ANISOTROPIC",
    "D2D1_YCBCR_INTERPOLATION_MODE_HIGH_QUALITY_CUBIC",
    "D2D1_YCBCR_INTERPOLATION_MODE_FORCE_DWORD",
    "D2D1_CONTRAST_PROP",
    "D2D1_CONTRAST_PROP_CONTRAST",
    "D2D1_CONTRAST_PROP_CLAMP_INPUT",
    "D2D1_CONTRAST_PROP_FORCE_DWORD",
    "D2D1_RGBTOHUE_PROP",
    "D2D1_RGBTOHUE_PROP_OUTPUT_COLOR_SPACE",
    "D2D1_RGBTOHUE_PROP_FORCE_DWORD",
    "D2D1_RGBTOHUE_OUTPUT_COLOR_SPACE",
    "D2D1_RGBTOHUE_OUTPUT_COLOR_SPACE_HUE_SATURATION_VALUE",
    "D2D1_RGBTOHUE_OUTPUT_COLOR_SPACE_HUE_SATURATION_LIGHTNESS",
    "D2D1_RGBTOHUE_OUTPUT_COLOR_SPACE_FORCE_DWORD",
    "D2D1_HUETORGB_PROP",
    "D2D1_HUETORGB_PROP_INPUT_COLOR_SPACE",
    "D2D1_HUETORGB_PROP_FORCE_DWORD",
    "D2D1_HUETORGB_INPUT_COLOR_SPACE",
    "D2D1_HUETORGB_INPUT_COLOR_SPACE_HUE_SATURATION_VALUE",
    "D2D1_HUETORGB_INPUT_COLOR_SPACE_HUE_SATURATION_LIGHTNESS",
    "D2D1_HUETORGB_INPUT_COLOR_SPACE_FORCE_DWORD",
    "D2D1_CHROMAKEY_PROP",
    "D2D1_CHROMAKEY_PROP_COLOR",
    "D2D1_CHROMAKEY_PROP_TOLERANCE",
    "D2D1_CHROMAKEY_PROP_INVERT_ALPHA",
    "D2D1_CHROMAKEY_PROP_FEATHER",
    "D2D1_CHROMAKEY_PROP_FORCE_DWORD",
    "D2D1_EMBOSS_PROP",
    "D2D1_EMBOSS_PROP_HEIGHT",
    "D2D1_EMBOSS_PROP_DIRECTION",
    "D2D1_EMBOSS_PROP_FORCE_DWORD",
    "D2D1_EXPOSURE_PROP",
    "D2D1_EXPOSURE_PROP_EXPOSURE_VALUE",
    "D2D1_EXPOSURE_PROP_FORCE_DWORD",
    "D2D1_POSTERIZE_PROP",
    "D2D1_POSTERIZE_PROP_RED_VALUE_COUNT",
    "D2D1_POSTERIZE_PROP_GREEN_VALUE_COUNT",
    "D2D1_POSTERIZE_PROP_BLUE_VALUE_COUNT",
    "D2D1_POSTERIZE_PROP_FORCE_DWORD",
    "D2D1_SEPIA_PROP",
    "D2D1_SEPIA_PROP_INTENSITY",
    "D2D1_SEPIA_PROP_ALPHA_MODE",
    "D2D1_SEPIA_PROP_FORCE_DWORD",
    "D2D1_SHARPEN_PROP",
    "D2D1_SHARPEN_PROP_SHARPNESS",
    "D2D1_SHARPEN_PROP_THRESHOLD",
    "D2D1_SHARPEN_PROP_FORCE_DWORD",
    "D2D1_STRAIGHTEN_PROP",
    "D2D1_STRAIGHTEN_PROP_ANGLE",
    "D2D1_STRAIGHTEN_PROP_MAINTAIN_SIZE",
    "D2D1_STRAIGHTEN_PROP_SCALE_MODE",
    "D2D1_STRAIGHTEN_PROP_FORCE_DWORD",
    "D2D1_STRAIGHTEN_SCALE_MODE",
    "D2D1_STRAIGHTEN_SCALE_MODE_NEAREST_NEIGHBOR",
    "D2D1_STRAIGHTEN_SCALE_MODE_LINEAR",
    "D2D1_STRAIGHTEN_SCALE_MODE_CUBIC",
    "D2D1_STRAIGHTEN_SCALE_MODE_MULTI_SAMPLE_LINEAR",
    "D2D1_STRAIGHTEN_SCALE_MODE_ANISOTROPIC",
    "D2D1_STRAIGHTEN_SCALE_MODE_FORCE_DWORD",
    "D2D1_TEMPERATUREANDTINT_PROP",
    "D2D1_TEMPERATUREANDTINT_PROP_TEMPERATURE",
    "D2D1_TEMPERATUREANDTINT_PROP_TINT",
    "D2D1_TEMPERATUREANDTINT_PROP_FORCE_DWORD",
    "D2D1_VIGNETTE_PROP",
    "D2D1_VIGNETTE_PROP_COLOR",
    "D2D1_VIGNETTE_PROP_TRANSITION_SIZE",
    "D2D1_VIGNETTE_PROP_STRENGTH",
    "D2D1_VIGNETTE_PROP_FORCE_DWORD",
    "D2D1_EDGEDETECTION_PROP",
    "D2D1_EDGEDETECTION_PROP_STRENGTH",
    "D2D1_EDGEDETECTION_PROP_BLUR_RADIUS",
    "D2D1_EDGEDETECTION_PROP_MODE",
    "D2D1_EDGEDETECTION_PROP_OVERLAY_EDGES",
    "D2D1_EDGEDETECTION_PROP_ALPHA_MODE",
    "D2D1_EDGEDETECTION_PROP_FORCE_DWORD",
    "D2D1_EDGEDETECTION_MODE",
    "D2D1_EDGEDETECTION_MODE_SOBEL",
    "D2D1_EDGEDETECTION_MODE_PREWITT",
    "D2D1_EDGEDETECTION_MODE_FORCE_DWORD",
    "D2D1_HIGHLIGHTSANDSHADOWS_PROP",
    "D2D1_HIGHLIGHTSANDSHADOWS_PROP_HIGHLIGHTS",
    "D2D1_HIGHLIGHTSANDSHADOWS_PROP_SHADOWS",
    "D2D1_HIGHLIGHTSANDSHADOWS_PROP_CLARITY",
    "D2D1_HIGHLIGHTSANDSHADOWS_PROP_INPUT_GAMMA",
    "D2D1_HIGHLIGHTSANDSHADOWS_PROP_MASK_BLUR_RADIUS",
    "D2D1_HIGHLIGHTSANDSHADOWS_PROP_FORCE_DWORD",
    "D2D1_HIGHLIGHTSANDSHADOWS_INPUT_GAMMA",
    "D2D1_HIGHLIGHTSANDSHADOWS_INPUT_GAMMA_LINEAR",
    "D2D1_HIGHLIGHTSANDSHADOWS_INPUT_GAMMA_SRGB",
    "D2D1_HIGHLIGHTSANDSHADOWS_INPUT_GAMMA_FORCE_DWORD",
    "D2D1_LOOKUPTABLE3D_PROP",
    "D2D1_LOOKUPTABLE3D_PROP_LUT",
    "D2D1_LOOKUPTABLE3D_PROP_ALPHA_MODE",
    "D2D1_LOOKUPTABLE3D_PROP_FORCE_DWORD",
    "D2D1_OPACITY_PROP",
    "D2D1_OPACITY_PROP_OPACITY",
    "D2D1_OPACITY_PROP_FORCE_DWORD",
    "D2D1_CROSSFADE_PROP",
    "D2D1_CROSSFADE_PROP_WEIGHT",
    "D2D1_CROSSFADE_PROP_FORCE_DWORD",
    "D2D1_TINT_PROP",
    "D2D1_TINT_PROP_COLOR",
    "D2D1_TINT_PROP_CLAMP_OUTPUT",
    "D2D1_TINT_PROP_FORCE_DWORD",
    "D2D1_WHITELEVELADJUSTMENT_PROP",
    "D2D1_WHITELEVELADJUSTMENT_PROP_INPUT_WHITE_LEVEL",
    "D2D1_WHITELEVELADJUSTMENT_PROP_OUTPUT_WHITE_LEVEL",
    "D2D1_WHITELEVELADJUSTMENT_PROP_FORCE_DWORD",
    "D2D1_HDRTONEMAP_PROP",
    "D2D1_HDRTONEMAP_PROP_INPUT_MAX_LUMINANCE",
    "D2D1_HDRTONEMAP_PROP_OUTPUT_MAX_LUMINANCE",
    "D2D1_HDRTONEMAP_PROP_DISPLAY_MODE",
    "D2D1_HDRTONEMAP_PROP_FORCE_DWORD",
    "D2D1_HDRTONEMAP_DISPLAY_MODE",
    "D2D1_HDRTONEMAP_DISPLAY_MODE_SDR",
    "D2D1_HDRTONEMAP_DISPLAY_MODE_HDR",
    "D2D1_HDRTONEMAP_DISPLAY_MODE_FORCE_DWORD",
    "D2D1_RENDERING_PRIORITY",
    "D2D1_RENDERING_PRIORITY_NORMAL",
    "D2D1_RENDERING_PRIORITY_LOW",
    "D2D1_RENDERING_PRIORITY_FORCE_DWORD",
    "ID2D1GeometryRealization",
    "ID2D1DeviceContext1",
    "ID2D1Device1",
    "ID2D1Factory2",
    "ID2D1CommandSink1",
    "D2D1_SVG_PAINT_TYPE",
    "D2D1_SVG_PAINT_TYPE_NONE",
    "D2D1_SVG_PAINT_TYPE_COLOR",
    "D2D1_SVG_PAINT_TYPE_CURRENT_COLOR",
    "D2D1_SVG_PAINT_TYPE_URI",
    "D2D1_SVG_PAINT_TYPE_URI_NONE",
    "D2D1_SVG_PAINT_TYPE_URI_COLOR",
    "D2D1_SVG_PAINT_TYPE_URI_CURRENT_COLOR",
    "D2D1_SVG_PAINT_TYPE_FORCE_DWORD",
    "D2D1_SVG_LENGTH_UNITS",
    "D2D1_SVG_LENGTH_UNITS_NUMBER",
    "D2D1_SVG_LENGTH_UNITS_PERCENTAGE",
    "D2D1_SVG_LENGTH_UNITS_FORCE_DWORD",
    "D2D1_SVG_DISPLAY",
    "D2D1_SVG_DISPLAY_INLINE",
    "D2D1_SVG_DISPLAY_NONE",
    "D2D1_SVG_DISPLAY_FORCE_DWORD",
    "D2D1_SVG_VISIBILITY",
    "D2D1_SVG_VISIBILITY_VISIBLE",
    "D2D1_SVG_VISIBILITY_HIDDEN",
    "D2D1_SVG_VISIBILITY_FORCE_DWORD",
    "D2D1_SVG_OVERFLOW",
    "D2D1_SVG_OVERFLOW_VISIBLE",
    "D2D1_SVG_OVERFLOW_HIDDEN",
    "D2D1_SVG_OVERFLOW_FORCE_DWORD",
    "D2D1_SVG_LINE_CAP",
    "D2D1_SVG_LINE_CAP_BUTT",
    "D2D1_SVG_LINE_CAP_SQUARE",
    "D2D1_SVG_LINE_CAP_ROUND",
    "D2D1_SVG_LINE_CAP_FORCE_DWORD",
    "D2D1_SVG_LINE_JOIN",
    "D2D1_SVG_LINE_JOIN_BEVEL",
    "D2D1_SVG_LINE_JOIN_MITER",
    "D2D1_SVG_LINE_JOIN_ROUND",
    "D2D1_SVG_LINE_JOIN_FORCE_DWORD",
    "D2D1_SVG_ASPECT_ALIGN",
    "D2D1_SVG_ASPECT_ALIGN_NONE",
    "D2D1_SVG_ASPECT_ALIGN_X_MIN_Y_MIN",
    "D2D1_SVG_ASPECT_ALIGN_X_MID_Y_MIN",
    "D2D1_SVG_ASPECT_ALIGN_X_MAX_Y_MIN",
    "D2D1_SVG_ASPECT_ALIGN_X_MIN_Y_MID",
    "D2D1_SVG_ASPECT_ALIGN_X_MID_Y_MID",
    "D2D1_SVG_ASPECT_ALIGN_X_MAX_Y_MID",
    "D2D1_SVG_ASPECT_ALIGN_X_MIN_Y_MAX",
    "D2D1_SVG_ASPECT_ALIGN_X_MID_Y_MAX",
    "D2D1_SVG_ASPECT_ALIGN_X_MAX_Y_MAX",
    "D2D1_SVG_ASPECT_ALIGN_FORCE_DWORD",
    "D2D1_SVG_ASPECT_SCALING",
    "D2D1_SVG_ASPECT_SCALING_MEET",
    "D2D1_SVG_ASPECT_SCALING_SLICE",
    "D2D1_SVG_ASPECT_SCALING_FORCE_DWORD",
    "D2D1_SVG_PATH_COMMAND",
    "D2D1_SVG_PATH_COMMAND_CLOSE_PATH",
    "D2D1_SVG_PATH_COMMAND_MOVE_ABSOLUTE",
    "D2D1_SVG_PATH_COMMAND_MOVE_RELATIVE",
    "D2D1_SVG_PATH_COMMAND_LINE_ABSOLUTE",
    "D2D1_SVG_PATH_COMMAND_LINE_RELATIVE",
    "D2D1_SVG_PATH_COMMAND_CUBIC_ABSOLUTE",
    "D2D1_SVG_PATH_COMMAND_CUBIC_RELATIVE",
    "D2D1_SVG_PATH_COMMAND_QUADRADIC_ABSOLUTE",
    "D2D1_SVG_PATH_COMMAND_QUADRADIC_RELATIVE",
    "D2D1_SVG_PATH_COMMAND_ARC_ABSOLUTE",
    "D2D1_SVG_PATH_COMMAND_ARC_RELATIVE",
    "D2D1_SVG_PATH_COMMAND_HORIZONTAL_ABSOLUTE",
    "D2D1_SVG_PATH_COMMAND_HORIZONTAL_RELATIVE",
    "D2D1_SVG_PATH_COMMAND_VERTICAL_ABSOLUTE",
    "D2D1_SVG_PATH_COMMAND_VERTICAL_RELATIVE",
    "D2D1_SVG_PATH_COMMAND_CUBIC_SMOOTH_ABSOLUTE",
    "D2D1_SVG_PATH_COMMAND_CUBIC_SMOOTH_RELATIVE",
    "D2D1_SVG_PATH_COMMAND_QUADRADIC_SMOOTH_ABSOLUTE",
    "D2D1_SVG_PATH_COMMAND_QUADRADIC_SMOOTH_RELATIVE",
    "D2D1_SVG_PATH_COMMAND_FORCE_DWORD",
    "D2D1_SVG_UNIT_TYPE",
    "D2D1_SVG_UNIT_TYPE_USER_SPACE_ON_USE",
    "D2D1_SVG_UNIT_TYPE_OBJECT_BOUNDING_BOX",
    "D2D1_SVG_UNIT_TYPE_FORCE_DWORD",
    "D2D1_SVG_ATTRIBUTE_STRING_TYPE",
    "D2D1_SVG_ATTRIBUTE_STRING_TYPE_SVG",
    "D2D1_SVG_ATTRIBUTE_STRING_TYPE_ID",
    "D2D1_SVG_ATTRIBUTE_STRING_TYPE_FORCE_DWORD",
    "D2D1_SVG_ATTRIBUTE_POD_TYPE",
    "D2D1_SVG_ATTRIBUTE_POD_TYPE_FLOAT",
    "D2D1_SVG_ATTRIBUTE_POD_TYPE_COLOR",
    "D2D1_SVG_ATTRIBUTE_POD_TYPE_FILL_MODE",
    "D2D1_SVG_ATTRIBUTE_POD_TYPE_DISPLAY",
    "D2D1_SVG_ATTRIBUTE_POD_TYPE_OVERFLOW",
    "D2D1_SVG_ATTRIBUTE_POD_TYPE_LINE_CAP",
    "D2D1_SVG_ATTRIBUTE_POD_TYPE_LINE_JOIN",
    "D2D1_SVG_ATTRIBUTE_POD_TYPE_VISIBILITY",
    "D2D1_SVG_ATTRIBUTE_POD_TYPE_MATRIX",
    "D2D1_SVG_ATTRIBUTE_POD_TYPE_UNIT_TYPE",
    "D2D1_SVG_ATTRIBUTE_POD_TYPE_EXTEND_MODE",
    "D2D1_SVG_ATTRIBUTE_POD_TYPE_PRESERVE_ASPECT_RATIO",
    "D2D1_SVG_ATTRIBUTE_POD_TYPE_VIEWBOX",
    "D2D1_SVG_ATTRIBUTE_POD_TYPE_LENGTH",
    "D2D1_SVG_ATTRIBUTE_POD_TYPE_FORCE_DWORD",
    "D2D1_SVG_LENGTH",
    "D2D1_SVG_PRESERVE_ASPECT_RATIO",
    "D2D1_SVG_VIEWBOX",
    "ID2D1SvgAttribute",
    "ID2D1SvgPaint",
    "ID2D1SvgStrokeDashArray",
    "ID2D1SvgPointCollection",
    "ID2D1SvgPathData",
    "ID2D1SvgElement",
    "ID2D1SvgDocument",
    "D2D1_INK_NIB_SHAPE",
    "D2D1_INK_NIB_SHAPE_ROUND",
    "D2D1_INK_NIB_SHAPE_SQUARE",
    "D2D1_INK_NIB_SHAPE_FORCE_DWORD",
    "D2D1_ORIENTATION",
    "D2D1_ORIENTATION_DEFAULT",
    "D2D1_ORIENTATION_FLIP_HORIZONTAL",
    "D2D1_ORIENTATION_ROTATE_CLOCKWISE180",
    "D2D1_ORIENTATION_ROTATE_CLOCKWISE180_FLIP_HORIZONTAL",
    "D2D1_ORIENTATION_ROTATE_CLOCKWISE90_FLIP_HORIZONTAL",
    "D2D1_ORIENTATION_ROTATE_CLOCKWISE270",
    "D2D1_ORIENTATION_ROTATE_CLOCKWISE270_FLIP_HORIZONTAL",
    "D2D1_ORIENTATION_ROTATE_CLOCKWISE90",
    "D2D1_ORIENTATION_FORCE_DWORD",
    "D2D1_IMAGE_SOURCE_LOADING_OPTIONS",
    "D2D1_IMAGE_SOURCE_LOADING_OPTIONS_NONE",
    "D2D1_IMAGE_SOURCE_LOADING_OPTIONS_RELEASE_SOURCE",
    "D2D1_IMAGE_SOURCE_LOADING_OPTIONS_CACHE_ON_DEMAND",
    "D2D1_IMAGE_SOURCE_LOADING_OPTIONS_FORCE_DWORD",
    "D2D1_IMAGE_SOURCE_FROM_DXGI_OPTIONS",
    "D2D1_IMAGE_SOURCE_FROM_DXGI_OPTIONS_NONE",
    "D2D1_IMAGE_SOURCE_FROM_DXGI_OPTIONS_LOW_QUALITY_PRIMARY_CONVERSION",
    "D2D1_IMAGE_SOURCE_FROM_DXGI_OPTIONS_FORCE_DWORD",
    "D2D1_TRANSFORMED_IMAGE_SOURCE_OPTIONS",
    "D2D1_TRANSFORMED_IMAGE_SOURCE_OPTIONS_NONE",
    "D2D1_TRANSFORMED_IMAGE_SOURCE_OPTIONS_DISABLE_DPI_SCALE",
    "D2D1_TRANSFORMED_IMAGE_SOURCE_OPTIONS_FORCE_DWORD",
    "D2D1_TRANSFORMED_IMAGE_SOURCE_PROPERTIES",
    "D2D1_INK_POINT",
    "D2D1_INK_BEZIER_SEGMENT",
    "D2D1_INK_STYLE_PROPERTIES",
    "D2D1_PATCH_EDGE_MODE",
    "D2D1_PATCH_EDGE_MODE_ALIASED",
    "D2D1_PATCH_EDGE_MODE_ANTIALIASED",
    "D2D1_PATCH_EDGE_MODE_ALIASED_INFLATED",
    "D2D1_PATCH_EDGE_MODE_FORCE_DWORD",
    "D2D1_GRADIENT_MESH_PATCH",
    "D2D1_SPRITE_OPTIONS",
    "D2D1_SPRITE_OPTIONS_NONE",
    "D2D1_SPRITE_OPTIONS_CLAMP_TO_SOURCE_RECTANGLE",
    "D2D1_SPRITE_OPTIONS_FORCE_DWORD",
    "D2D1_COLOR_BITMAP_GLYPH_SNAP_OPTION",
    "D2D1_COLOR_BITMAP_GLYPH_SNAP_OPTION_DEFAULT",
    "D2D1_COLOR_BITMAP_GLYPH_SNAP_OPTION_DISABLE",
    "D2D1_COLOR_BITMAP_GLYPH_SNAP_OPTION_FORCE_DWORD",
    "D2D1_GAMMA1",
    "D2D1_GAMMA1_G22",
    "D2D1_GAMMA1_G10",
    "D2D1_GAMMA1_G2084",
    "D2D1_GAMMA1_FORCE_DWORD",
    "D2D1_SIMPLE_COLOR_PROFILE",
    "D2D1_COLOR_CONTEXT_TYPE",
    "D2D1_COLOR_CONTEXT_TYPE_ICC",
    "D2D1_COLOR_CONTEXT_TYPE_SIMPLE",
    "D2D1_COLOR_CONTEXT_TYPE_DXGI",
    "D2D1_COLOR_CONTEXT_TYPE_FORCE_DWORD",
    "ID2D1InkStyle",
    "ID2D1Ink",
    "ID2D1GradientMesh",
    "ID2D1ImageSource",
    "ID2D1ImageSourceFromWic",
    "ID2D1TransformedImageSource",
    "ID2D1LookupTable3D",
    "ID2D1DeviceContext2",
    "ID2D1Device2",
    "ID2D1Factory3",
    "ID2D1CommandSink2",
    "ID2D1GdiMetafile1",
    "ID2D1GdiMetafileSink1",
    "ID2D1SpriteBatch",
    "ID2D1DeviceContext3",
    "ID2D1Device3",
    "ID2D1Factory4",
    "ID2D1CommandSink3",
    "ID2D1SvgGlyphStyle",
    "ID2D1DeviceContext4",
    "ID2D1Device4",
    "ID2D1Factory5",
    "ID2D1CommandSink4",
    "ID2D1ColorContext1",
    "ID2D1DeviceContext5",
    "ID2D1Device5",
    "ID2D1Factory6",
    "ID2D1CommandSink5",
    "ID2D1DeviceContext6",
    "ID2D1Device6",
    "ID2D1Factory7",
    "ID2D1EffectContext1",
    "ID2D1EffectContext2",
    "D2D1CreateFactory",
    "D2D1MakeRotateMatrix",
    "D2D1MakeSkewMatrix",
    "D2D1IsMatrixInvertible",
    "D2D1InvertMatrix",
    "D2D1CreateDevice",
    "D2D1CreateDeviceContext",
    "D2D1ConvertColorSpace",
    "D2D1SinCos",
    "D2D1Tan",
    "D2D1Vec3Length",
    "D2D1ComputeMaximumScaleFactor",
    "D2D1GetGradientMeshInteriorPointsFromCoonsPatch",
]
