from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.Graphics.OpenGL
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
GL_VERSION_1_1 = 1
GL_ACCUM = 256
GL_LOAD = 257
GL_RETURN = 258
GL_MULT = 259
GL_ADD = 260
GL_NEVER = 512
GL_LESS = 513
GL_EQUAL = 514
GL_LEQUAL = 515
GL_GREATER = 516
GL_NOTEQUAL = 517
GL_GEQUAL = 518
GL_ALWAYS = 519
GL_CURRENT_BIT = 1
GL_POINT_BIT = 2
GL_LINE_BIT = 4
GL_POLYGON_BIT = 8
GL_POLYGON_STIPPLE_BIT = 16
GL_PIXEL_MODE_BIT = 32
GL_LIGHTING_BIT = 64
GL_FOG_BIT = 128
GL_DEPTH_BUFFER_BIT = 256
GL_ACCUM_BUFFER_BIT = 512
GL_STENCIL_BUFFER_BIT = 1024
GL_VIEWPORT_BIT = 2048
GL_TRANSFORM_BIT = 4096
GL_ENABLE_BIT = 8192
GL_COLOR_BUFFER_BIT = 16384
GL_HINT_BIT = 32768
GL_EVAL_BIT = 65536
GL_LIST_BIT = 131072
GL_TEXTURE_BIT = 262144
GL_SCISSOR_BIT = 524288
GL_ALL_ATTRIB_BITS = 1048575
GL_POINTS = 0
GL_LINES = 1
GL_LINE_LOOP = 2
GL_LINE_STRIP = 3
GL_TRIANGLES = 4
GL_TRIANGLE_STRIP = 5
GL_TRIANGLE_FAN = 6
GL_QUADS = 7
GL_QUAD_STRIP = 8
GL_POLYGON = 9
GL_ZERO = 0
GL_ONE = 1
GL_SRC_COLOR = 768
GL_ONE_MINUS_SRC_COLOR = 769
GL_SRC_ALPHA = 770
GL_ONE_MINUS_SRC_ALPHA = 771
GL_DST_ALPHA = 772
GL_ONE_MINUS_DST_ALPHA = 773
GL_DST_COLOR = 774
GL_ONE_MINUS_DST_COLOR = 775
GL_SRC_ALPHA_SATURATE = 776
GL_TRUE = 1
GL_FALSE = 0
GL_CLIP_PLANE0 = 12288
GL_CLIP_PLANE1 = 12289
GL_CLIP_PLANE2 = 12290
GL_CLIP_PLANE3 = 12291
GL_CLIP_PLANE4 = 12292
GL_CLIP_PLANE5 = 12293
GL_BYTE = 5120
GL_UNSIGNED_BYTE = 5121
GL_SHORT = 5122
GL_UNSIGNED_SHORT = 5123
GL_INT = 5124
GL_UNSIGNED_INT = 5125
GL_FLOAT = 5126
GL_2_BYTES = 5127
GL_3_BYTES = 5128
GL_4_BYTES = 5129
GL_DOUBLE = 5130
GL_NONE = 0
GL_FRONT_LEFT = 1024
GL_FRONT_RIGHT = 1025
GL_BACK_LEFT = 1026
GL_BACK_RIGHT = 1027
GL_FRONT = 1028
GL_BACK = 1029
GL_LEFT = 1030
GL_RIGHT = 1031
GL_FRONT_AND_BACK = 1032
GL_AUX0 = 1033
GL_AUX1 = 1034
GL_AUX2 = 1035
GL_AUX3 = 1036
GL_NO_ERROR = 0
GL_INVALID_ENUM = 1280
GL_INVALID_VALUE = 1281
GL_INVALID_OPERATION = 1282
GL_STACK_OVERFLOW = 1283
GL_STACK_UNDERFLOW = 1284
GL_OUT_OF_MEMORY = 1285
GL_2D = 1536
GL_3D = 1537
GL_3D_COLOR = 1538
GL_3D_COLOR_TEXTURE = 1539
GL_4D_COLOR_TEXTURE = 1540
GL_PASS_THROUGH_TOKEN = 1792
GL_POINT_TOKEN = 1793
GL_LINE_TOKEN = 1794
GL_POLYGON_TOKEN = 1795
GL_BITMAP_TOKEN = 1796
GL_DRAW_PIXEL_TOKEN = 1797
GL_COPY_PIXEL_TOKEN = 1798
GL_LINE_RESET_TOKEN = 1799
GL_EXP = 2048
GL_EXP2 = 2049
GL_CW = 2304
GL_CCW = 2305
GL_COEFF = 2560
GL_ORDER = 2561
GL_DOMAIN = 2562
GL_CURRENT_COLOR = 2816
GL_CURRENT_INDEX = 2817
GL_CURRENT_NORMAL = 2818
GL_CURRENT_TEXTURE_COORDS = 2819
GL_CURRENT_RASTER_COLOR = 2820
GL_CURRENT_RASTER_INDEX = 2821
GL_CURRENT_RASTER_TEXTURE_COORDS = 2822
GL_CURRENT_RASTER_POSITION = 2823
GL_CURRENT_RASTER_POSITION_VALID = 2824
GL_CURRENT_RASTER_DISTANCE = 2825
GL_POINT_SMOOTH = 2832
GL_POINT_SIZE = 2833
GL_POINT_SIZE_RANGE = 2834
GL_POINT_SIZE_GRANULARITY = 2835
GL_LINE_SMOOTH = 2848
GL_LINE_WIDTH = 2849
GL_LINE_WIDTH_RANGE = 2850
GL_LINE_WIDTH_GRANULARITY = 2851
GL_LINE_STIPPLE = 2852
GL_LINE_STIPPLE_PATTERN = 2853
GL_LINE_STIPPLE_REPEAT = 2854
GL_LIST_MODE = 2864
GL_MAX_LIST_NESTING = 2865
GL_LIST_BASE = 2866
GL_LIST_INDEX = 2867
GL_POLYGON_MODE = 2880
GL_POLYGON_SMOOTH = 2881
GL_POLYGON_STIPPLE = 2882
GL_EDGE_FLAG = 2883
GL_CULL_FACE = 2884
GL_CULL_FACE_MODE = 2885
GL_FRONT_FACE = 2886
GL_LIGHTING = 2896
GL_LIGHT_MODEL_LOCAL_VIEWER = 2897
GL_LIGHT_MODEL_TWO_SIDE = 2898
GL_LIGHT_MODEL_AMBIENT = 2899
GL_SHADE_MODEL = 2900
GL_COLOR_MATERIAL_FACE = 2901
GL_COLOR_MATERIAL_PARAMETER = 2902
GL_COLOR_MATERIAL = 2903
GL_FOG = 2912
GL_FOG_INDEX = 2913
GL_FOG_DENSITY = 2914
GL_FOG_START = 2915
GL_FOG_END = 2916
GL_FOG_MODE = 2917
GL_FOG_COLOR = 2918
GL_DEPTH_RANGE = 2928
GL_DEPTH_TEST = 2929
GL_DEPTH_WRITEMASK = 2930
GL_DEPTH_CLEAR_VALUE = 2931
GL_DEPTH_FUNC = 2932
GL_ACCUM_CLEAR_VALUE = 2944
GL_STENCIL_TEST = 2960
GL_STENCIL_CLEAR_VALUE = 2961
GL_STENCIL_FUNC = 2962
GL_STENCIL_VALUE_MASK = 2963
GL_STENCIL_FAIL = 2964
GL_STENCIL_PASS_DEPTH_FAIL = 2965
GL_STENCIL_PASS_DEPTH_PASS = 2966
GL_STENCIL_REF = 2967
GL_STENCIL_WRITEMASK = 2968
GL_MATRIX_MODE = 2976
GL_NORMALIZE = 2977
GL_VIEWPORT = 2978
GL_MODELVIEW_STACK_DEPTH = 2979
GL_PROJECTION_STACK_DEPTH = 2980
GL_TEXTURE_STACK_DEPTH = 2981
GL_MODELVIEW_MATRIX = 2982
GL_PROJECTION_MATRIX = 2983
GL_TEXTURE_MATRIX = 2984
GL_ATTRIB_STACK_DEPTH = 2992
GL_CLIENT_ATTRIB_STACK_DEPTH = 2993
GL_ALPHA_TEST = 3008
GL_ALPHA_TEST_FUNC = 3009
GL_ALPHA_TEST_REF = 3010
GL_DITHER = 3024
GL_BLEND_DST = 3040
GL_BLEND_SRC = 3041
GL_BLEND = 3042
GL_LOGIC_OP_MODE = 3056
GL_INDEX_LOGIC_OP = 3057
GL_COLOR_LOGIC_OP = 3058
GL_AUX_BUFFERS = 3072
GL_DRAW_BUFFER = 3073
GL_READ_BUFFER = 3074
GL_SCISSOR_BOX = 3088
GL_SCISSOR_TEST = 3089
GL_INDEX_CLEAR_VALUE = 3104
GL_INDEX_WRITEMASK = 3105
GL_COLOR_CLEAR_VALUE = 3106
GL_COLOR_WRITEMASK = 3107
GL_INDEX_MODE = 3120
GL_RGBA_MODE = 3121
GL_DOUBLEBUFFER = 3122
GL_STEREO = 3123
GL_RENDER_MODE = 3136
GL_PERSPECTIVE_CORRECTION_HINT = 3152
GL_POINT_SMOOTH_HINT = 3153
GL_LINE_SMOOTH_HINT = 3154
GL_POLYGON_SMOOTH_HINT = 3155
GL_FOG_HINT = 3156
GL_TEXTURE_GEN_S = 3168
GL_TEXTURE_GEN_T = 3169
GL_TEXTURE_GEN_R = 3170
GL_TEXTURE_GEN_Q = 3171
GL_PIXEL_MAP_I_TO_I = 3184
GL_PIXEL_MAP_S_TO_S = 3185
GL_PIXEL_MAP_I_TO_R = 3186
GL_PIXEL_MAP_I_TO_G = 3187
GL_PIXEL_MAP_I_TO_B = 3188
GL_PIXEL_MAP_I_TO_A = 3189
GL_PIXEL_MAP_R_TO_R = 3190
GL_PIXEL_MAP_G_TO_G = 3191
GL_PIXEL_MAP_B_TO_B = 3192
GL_PIXEL_MAP_A_TO_A = 3193
GL_PIXEL_MAP_I_TO_I_SIZE = 3248
GL_PIXEL_MAP_S_TO_S_SIZE = 3249
GL_PIXEL_MAP_I_TO_R_SIZE = 3250
GL_PIXEL_MAP_I_TO_G_SIZE = 3251
GL_PIXEL_MAP_I_TO_B_SIZE = 3252
GL_PIXEL_MAP_I_TO_A_SIZE = 3253
GL_PIXEL_MAP_R_TO_R_SIZE = 3254
GL_PIXEL_MAP_G_TO_G_SIZE = 3255
GL_PIXEL_MAP_B_TO_B_SIZE = 3256
GL_PIXEL_MAP_A_TO_A_SIZE = 3257
GL_UNPACK_SWAP_BYTES = 3312
GL_UNPACK_LSB_FIRST = 3313
GL_UNPACK_ROW_LENGTH = 3314
GL_UNPACK_SKIP_ROWS = 3315
GL_UNPACK_SKIP_PIXELS = 3316
GL_UNPACK_ALIGNMENT = 3317
GL_PACK_SWAP_BYTES = 3328
GL_PACK_LSB_FIRST = 3329
GL_PACK_ROW_LENGTH = 3330
GL_PACK_SKIP_ROWS = 3331
GL_PACK_SKIP_PIXELS = 3332
GL_PACK_ALIGNMENT = 3333
GL_MAP_COLOR = 3344
GL_MAP_STENCIL = 3345
GL_INDEX_SHIFT = 3346
GL_INDEX_OFFSET = 3347
GL_RED_SCALE = 3348
GL_RED_BIAS = 3349
GL_ZOOM_X = 3350
GL_ZOOM_Y = 3351
GL_GREEN_SCALE = 3352
GL_GREEN_BIAS = 3353
GL_BLUE_SCALE = 3354
GL_BLUE_BIAS = 3355
GL_ALPHA_SCALE = 3356
GL_ALPHA_BIAS = 3357
GL_DEPTH_SCALE = 3358
GL_DEPTH_BIAS = 3359
GL_MAX_EVAL_ORDER = 3376
GL_MAX_LIGHTS = 3377
GL_MAX_CLIP_PLANES = 3378
GL_MAX_TEXTURE_SIZE = 3379
GL_MAX_PIXEL_MAP_TABLE = 3380
GL_MAX_ATTRIB_STACK_DEPTH = 3381
GL_MAX_MODELVIEW_STACK_DEPTH = 3382
GL_MAX_NAME_STACK_DEPTH = 3383
GL_MAX_PROJECTION_STACK_DEPTH = 3384
GL_MAX_TEXTURE_STACK_DEPTH = 3385
GL_MAX_VIEWPORT_DIMS = 3386
GL_MAX_CLIENT_ATTRIB_STACK_DEPTH = 3387
GL_SUBPIXEL_BITS = 3408
GL_INDEX_BITS = 3409
GL_RED_BITS = 3410
GL_GREEN_BITS = 3411
GL_BLUE_BITS = 3412
GL_ALPHA_BITS = 3413
GL_DEPTH_BITS = 3414
GL_STENCIL_BITS = 3415
GL_ACCUM_RED_BITS = 3416
GL_ACCUM_GREEN_BITS = 3417
GL_ACCUM_BLUE_BITS = 3418
GL_ACCUM_ALPHA_BITS = 3419
GL_NAME_STACK_DEPTH = 3440
GL_AUTO_NORMAL = 3456
GL_MAP1_COLOR_4 = 3472
GL_MAP1_INDEX = 3473
GL_MAP1_NORMAL = 3474
GL_MAP1_TEXTURE_COORD_1 = 3475
GL_MAP1_TEXTURE_COORD_2 = 3476
GL_MAP1_TEXTURE_COORD_3 = 3477
GL_MAP1_TEXTURE_COORD_4 = 3478
GL_MAP1_VERTEX_3 = 3479
GL_MAP1_VERTEX_4 = 3480
GL_MAP2_COLOR_4 = 3504
GL_MAP2_INDEX = 3505
GL_MAP2_NORMAL = 3506
GL_MAP2_TEXTURE_COORD_1 = 3507
GL_MAP2_TEXTURE_COORD_2 = 3508
GL_MAP2_TEXTURE_COORD_3 = 3509
GL_MAP2_TEXTURE_COORD_4 = 3510
GL_MAP2_VERTEX_3 = 3511
GL_MAP2_VERTEX_4 = 3512
GL_MAP1_GRID_DOMAIN = 3536
GL_MAP1_GRID_SEGMENTS = 3537
GL_MAP2_GRID_DOMAIN = 3538
GL_MAP2_GRID_SEGMENTS = 3539
GL_TEXTURE_1D = 3552
GL_TEXTURE_2D = 3553
GL_FEEDBACK_BUFFER_POINTER = 3568
GL_FEEDBACK_BUFFER_SIZE = 3569
GL_FEEDBACK_BUFFER_TYPE = 3570
GL_SELECTION_BUFFER_POINTER = 3571
GL_SELECTION_BUFFER_SIZE = 3572
GL_TEXTURE_WIDTH = 4096
GL_TEXTURE_HEIGHT = 4097
GL_TEXTURE_INTERNAL_FORMAT = 4099
GL_TEXTURE_BORDER_COLOR = 4100
GL_TEXTURE_BORDER = 4101
GL_DONT_CARE = 4352
GL_FASTEST = 4353
GL_NICEST = 4354
GL_LIGHT0 = 16384
GL_LIGHT1 = 16385
GL_LIGHT2 = 16386
GL_LIGHT3 = 16387
GL_LIGHT4 = 16388
GL_LIGHT5 = 16389
GL_LIGHT6 = 16390
GL_LIGHT7 = 16391
GL_AMBIENT = 4608
GL_DIFFUSE = 4609
GL_SPECULAR = 4610
GL_POSITION = 4611
GL_SPOT_DIRECTION = 4612
GL_SPOT_EXPONENT = 4613
GL_SPOT_CUTOFF = 4614
GL_CONSTANT_ATTENUATION = 4615
GL_LINEAR_ATTENUATION = 4616
GL_QUADRATIC_ATTENUATION = 4617
GL_COMPILE = 4864
GL_COMPILE_AND_EXECUTE = 4865
GL_CLEAR = 5376
GL_AND = 5377
GL_AND_REVERSE = 5378
GL_COPY = 5379
GL_AND_INVERTED = 5380
GL_NOOP = 5381
GL_XOR = 5382
GL_OR = 5383
GL_NOR = 5384
GL_EQUIV = 5385
GL_INVERT = 5386
GL_OR_REVERSE = 5387
GL_COPY_INVERTED = 5388
GL_OR_INVERTED = 5389
GL_NAND = 5390
GL_SET = 5391
GL_EMISSION = 5632
GL_SHININESS = 5633
GL_AMBIENT_AND_DIFFUSE = 5634
GL_COLOR_INDEXES = 5635
GL_MODELVIEW = 5888
GL_PROJECTION = 5889
GL_TEXTURE = 5890
GL_COLOR = 6144
GL_DEPTH = 6145
GL_STENCIL = 6146
GL_COLOR_INDEX = 6400
GL_STENCIL_INDEX = 6401
GL_DEPTH_COMPONENT = 6402
GL_RED = 6403
GL_GREEN = 6404
GL_BLUE = 6405
GL_ALPHA = 6406
GL_RGB = 6407
GL_RGBA = 6408
GL_LUMINANCE = 6409
GL_LUMINANCE_ALPHA = 6410
GL_BITMAP = 6656
GL_POINT = 6912
GL_LINE = 6913
GL_FILL = 6914
GL_RENDER = 7168
GL_FEEDBACK = 7169
GL_SELECT = 7170
GL_FLAT = 7424
GL_SMOOTH = 7425
GL_KEEP = 7680
GL_REPLACE = 7681
GL_INCR = 7682
GL_DECR = 7683
GL_VENDOR = 7936
GL_RENDERER = 7937
GL_VERSION = 7938
GL_EXTENSIONS = 7939
GL_S = 8192
GL_T = 8193
GL_R = 8194
GL_Q = 8195
GL_MODULATE = 8448
GL_DECAL = 8449
GL_TEXTURE_ENV_MODE = 8704
GL_TEXTURE_ENV_COLOR = 8705
GL_TEXTURE_ENV = 8960
GL_EYE_LINEAR = 9216
GL_OBJECT_LINEAR = 9217
GL_SPHERE_MAP = 9218
GL_TEXTURE_GEN_MODE = 9472
GL_OBJECT_PLANE = 9473
GL_EYE_PLANE = 9474
GL_NEAREST = 9728
GL_LINEAR = 9729
GL_NEAREST_MIPMAP_NEAREST = 9984
GL_LINEAR_MIPMAP_NEAREST = 9985
GL_NEAREST_MIPMAP_LINEAR = 9986
GL_LINEAR_MIPMAP_LINEAR = 9987
GL_TEXTURE_MAG_FILTER = 10240
GL_TEXTURE_MIN_FILTER = 10241
GL_TEXTURE_WRAP_S = 10242
GL_TEXTURE_WRAP_T = 10243
GL_CLAMP = 10496
GL_REPEAT = 10497
GL_CLIENT_PIXEL_STORE_BIT = 1
GL_CLIENT_VERTEX_ARRAY_BIT = 2
GL_CLIENT_ALL_ATTRIB_BITS = 4294967295
GL_POLYGON_OFFSET_FACTOR = 32824
GL_POLYGON_OFFSET_UNITS = 10752
GL_POLYGON_OFFSET_POINT = 10753
GL_POLYGON_OFFSET_LINE = 10754
GL_POLYGON_OFFSET_FILL = 32823
GL_ALPHA4 = 32827
GL_ALPHA8 = 32828
GL_ALPHA12 = 32829
GL_ALPHA16 = 32830
GL_LUMINANCE4 = 32831
GL_LUMINANCE8 = 32832
GL_LUMINANCE12 = 32833
GL_LUMINANCE16 = 32834
GL_LUMINANCE4_ALPHA4 = 32835
GL_LUMINANCE6_ALPHA2 = 32836
GL_LUMINANCE8_ALPHA8 = 32837
GL_LUMINANCE12_ALPHA4 = 32838
GL_LUMINANCE12_ALPHA12 = 32839
GL_LUMINANCE16_ALPHA16 = 32840
GL_INTENSITY = 32841
GL_INTENSITY4 = 32842
GL_INTENSITY8 = 32843
GL_INTENSITY12 = 32844
GL_INTENSITY16 = 32845
GL_R3_G3_B2 = 10768
GL_RGB4 = 32847
GL_RGB5 = 32848
GL_RGB8 = 32849
GL_RGB10 = 32850
GL_RGB12 = 32851
GL_RGB16 = 32852
GL_RGBA2 = 32853
GL_RGBA4 = 32854
GL_RGB5_A1 = 32855
GL_RGBA8 = 32856
GL_RGB10_A2 = 32857
GL_RGBA12 = 32858
GL_RGBA16 = 32859
GL_TEXTURE_RED_SIZE = 32860
GL_TEXTURE_GREEN_SIZE = 32861
GL_TEXTURE_BLUE_SIZE = 32862
GL_TEXTURE_ALPHA_SIZE = 32863
GL_TEXTURE_LUMINANCE_SIZE = 32864
GL_TEXTURE_INTENSITY_SIZE = 32865
GL_PROXY_TEXTURE_1D = 32867
GL_PROXY_TEXTURE_2D = 32868
GL_TEXTURE_PRIORITY = 32870
GL_TEXTURE_RESIDENT = 32871
GL_TEXTURE_BINDING_1D = 32872
GL_TEXTURE_BINDING_2D = 32873
GL_VERTEX_ARRAY = 32884
GL_NORMAL_ARRAY = 32885
GL_COLOR_ARRAY = 32886
GL_INDEX_ARRAY = 32887
GL_TEXTURE_COORD_ARRAY = 32888
GL_EDGE_FLAG_ARRAY = 32889
GL_VERTEX_ARRAY_SIZE = 32890
GL_VERTEX_ARRAY_TYPE = 32891
GL_VERTEX_ARRAY_STRIDE = 32892
GL_NORMAL_ARRAY_TYPE = 32894
GL_NORMAL_ARRAY_STRIDE = 32895
GL_COLOR_ARRAY_SIZE = 32897
GL_COLOR_ARRAY_TYPE = 32898
GL_COLOR_ARRAY_STRIDE = 32899
GL_INDEX_ARRAY_TYPE = 32901
GL_INDEX_ARRAY_STRIDE = 32902
GL_TEXTURE_COORD_ARRAY_SIZE = 32904
GL_TEXTURE_COORD_ARRAY_TYPE = 32905
GL_TEXTURE_COORD_ARRAY_STRIDE = 32906
GL_EDGE_FLAG_ARRAY_STRIDE = 32908
GL_VERTEX_ARRAY_POINTER = 32910
GL_NORMAL_ARRAY_POINTER = 32911
GL_COLOR_ARRAY_POINTER = 32912
GL_INDEX_ARRAY_POINTER = 32913
GL_TEXTURE_COORD_ARRAY_POINTER = 32914
GL_EDGE_FLAG_ARRAY_POINTER = 32915
GL_V2F = 10784
GL_V3F = 10785
GL_C4UB_V2F = 10786
GL_C4UB_V3F = 10787
GL_C3F_V3F = 10788
GL_N3F_V3F = 10789
GL_C4F_N3F_V3F = 10790
GL_T2F_V3F = 10791
GL_T4F_V4F = 10792
GL_T2F_C4UB_V3F = 10793
GL_T2F_C3F_V3F = 10794
GL_T2F_N3F_V3F = 10795
GL_T2F_C4F_N3F_V3F = 10796
GL_T4F_C4F_N3F_V4F = 10797
GL_EXT_vertex_array = 1
GL_EXT_bgra = 1
GL_EXT_paletted_texture = 1
GL_WIN_swap_hint = 1
GL_WIN_draw_range_elements = 1
GL_VERTEX_ARRAY_EXT = 32884
GL_NORMAL_ARRAY_EXT = 32885
GL_COLOR_ARRAY_EXT = 32886
GL_INDEX_ARRAY_EXT = 32887
GL_TEXTURE_COORD_ARRAY_EXT = 32888
GL_EDGE_FLAG_ARRAY_EXT = 32889
GL_VERTEX_ARRAY_SIZE_EXT = 32890
GL_VERTEX_ARRAY_TYPE_EXT = 32891
GL_VERTEX_ARRAY_STRIDE_EXT = 32892
GL_VERTEX_ARRAY_COUNT_EXT = 32893
GL_NORMAL_ARRAY_TYPE_EXT = 32894
GL_NORMAL_ARRAY_STRIDE_EXT = 32895
GL_NORMAL_ARRAY_COUNT_EXT = 32896
GL_COLOR_ARRAY_SIZE_EXT = 32897
GL_COLOR_ARRAY_TYPE_EXT = 32898
GL_COLOR_ARRAY_STRIDE_EXT = 32899
GL_COLOR_ARRAY_COUNT_EXT = 32900
GL_INDEX_ARRAY_TYPE_EXT = 32901
GL_INDEX_ARRAY_STRIDE_EXT = 32902
GL_INDEX_ARRAY_COUNT_EXT = 32903
GL_TEXTURE_COORD_ARRAY_SIZE_EXT = 32904
GL_TEXTURE_COORD_ARRAY_TYPE_EXT = 32905
GL_TEXTURE_COORD_ARRAY_STRIDE_EXT = 32906
GL_TEXTURE_COORD_ARRAY_COUNT_EXT = 32907
GL_EDGE_FLAG_ARRAY_STRIDE_EXT = 32908
GL_EDGE_FLAG_ARRAY_COUNT_EXT = 32909
GL_VERTEX_ARRAY_POINTER_EXT = 32910
GL_NORMAL_ARRAY_POINTER_EXT = 32911
GL_COLOR_ARRAY_POINTER_EXT = 32912
GL_INDEX_ARRAY_POINTER_EXT = 32913
GL_TEXTURE_COORD_ARRAY_POINTER_EXT = 32914
GL_EDGE_FLAG_ARRAY_POINTER_EXT = 32915
GL_DOUBLE_EXT = 5130
GL_BGR_EXT = 32992
GL_BGRA_EXT = 32993
GL_COLOR_TABLE_FORMAT_EXT = 32984
GL_COLOR_TABLE_WIDTH_EXT = 32985
GL_COLOR_TABLE_RED_SIZE_EXT = 32986
GL_COLOR_TABLE_GREEN_SIZE_EXT = 32987
GL_COLOR_TABLE_BLUE_SIZE_EXT = 32988
GL_COLOR_TABLE_ALPHA_SIZE_EXT = 32989
GL_COLOR_TABLE_LUMINANCE_SIZE_EXT = 32990
GL_COLOR_TABLE_INTENSITY_SIZE_EXT = 32991
GL_COLOR_INDEX1_EXT = 32994
GL_COLOR_INDEX2_EXT = 32995
GL_COLOR_INDEX4_EXT = 32996
GL_COLOR_INDEX8_EXT = 32997
GL_COLOR_INDEX12_EXT = 32998
GL_COLOR_INDEX16_EXT = 32999
GL_MAX_ELEMENTS_VERTICES_WIN = 33000
GL_MAX_ELEMENTS_INDICES_WIN = 33001
GL_PHONG_WIN = 33002
GL_PHONG_HINT_WIN = 33003
GL_FOG_SPECULAR_TEXTURE_WIN = 33004
GL_LOGIC_OP = 3057
GL_TEXTURE_COMPONENTS = 4099
GLU_VERSION_1_1 = 1
GLU_VERSION_1_2 = 1
GLU_INVALID_ENUM = 100900
GLU_INVALID_VALUE = 100901
GLU_OUT_OF_MEMORY = 100902
GLU_INCOMPATIBLE_GL_VERSION = 100903
GLU_VERSION = 100800
GLU_EXTENSIONS = 100801
GLU_TRUE = 1
GLU_FALSE = 0
GLU_SMOOTH = 100000
GLU_FLAT = 100001
GLU_NONE = 100002
GLU_POINT = 100010
GLU_LINE = 100011
GLU_FILL = 100012
GLU_SILHOUETTE = 100013
GLU_OUTSIDE = 100020
GLU_INSIDE = 100021
GLU_TESS_WINDING_RULE = 100140
GLU_TESS_BOUNDARY_ONLY = 100141
GLU_TESS_TOLERANCE = 100142
GLU_TESS_WINDING_ODD = 100130
GLU_TESS_WINDING_NONZERO = 100131
GLU_TESS_WINDING_POSITIVE = 100132
GLU_TESS_WINDING_NEGATIVE = 100133
GLU_TESS_WINDING_ABS_GEQ_TWO = 100134
GLU_TESS_BEGIN = 100100
GLU_TESS_VERTEX = 100101
GLU_TESS_END = 100102
GLU_TESS_ERROR = 100103
GLU_TESS_EDGE_FLAG = 100104
GLU_TESS_COMBINE = 100105
GLU_TESS_BEGIN_DATA = 100106
GLU_TESS_VERTEX_DATA = 100107
GLU_TESS_END_DATA = 100108
GLU_TESS_ERROR_DATA = 100109
GLU_TESS_EDGE_FLAG_DATA = 100110
GLU_TESS_COMBINE_DATA = 100111
GLU_TESS_ERROR1 = 100151
GLU_TESS_ERROR2 = 100152
GLU_TESS_ERROR3 = 100153
GLU_TESS_ERROR4 = 100154
GLU_TESS_ERROR5 = 100155
GLU_TESS_ERROR6 = 100156
GLU_TESS_ERROR7 = 100157
GLU_TESS_ERROR8 = 100158
GLU_TESS_MISSING_BEGIN_POLYGON = 100151
GLU_TESS_MISSING_BEGIN_CONTOUR = 100152
GLU_TESS_MISSING_END_POLYGON = 100153
GLU_TESS_MISSING_END_CONTOUR = 100154
GLU_TESS_COORD_TOO_LARGE = 100155
GLU_TESS_NEED_COMBINE_CALLBACK = 100156
GLU_AUTO_LOAD_MATRIX = 100200
GLU_CULLING = 100201
GLU_SAMPLING_TOLERANCE = 100203
GLU_DISPLAY_MODE = 100204
GLU_PARAMETRIC_TOLERANCE = 100202
GLU_SAMPLING_METHOD = 100205
GLU_U_STEP = 100206
GLU_V_STEP = 100207
GLU_PATH_LENGTH = 100215
GLU_PARAMETRIC_ERROR = 100216
GLU_DOMAIN_DISTANCE = 100217
GLU_MAP1_TRIM_2 = 100210
GLU_MAP1_TRIM_3 = 100211
GLU_OUTLINE_POLYGON = 100240
GLU_OUTLINE_PATCH = 100241
GLU_NURBS_ERROR1 = 100251
GLU_NURBS_ERROR2 = 100252
GLU_NURBS_ERROR3 = 100253
GLU_NURBS_ERROR4 = 100254
GLU_NURBS_ERROR5 = 100255
GLU_NURBS_ERROR6 = 100256
GLU_NURBS_ERROR7 = 100257
GLU_NURBS_ERROR8 = 100258
GLU_NURBS_ERROR9 = 100259
GLU_NURBS_ERROR10 = 100260
GLU_NURBS_ERROR11 = 100261
GLU_NURBS_ERROR12 = 100262
GLU_NURBS_ERROR13 = 100263
GLU_NURBS_ERROR14 = 100264
GLU_NURBS_ERROR15 = 100265
GLU_NURBS_ERROR16 = 100266
GLU_NURBS_ERROR17 = 100267
GLU_NURBS_ERROR18 = 100268
GLU_NURBS_ERROR19 = 100269
GLU_NURBS_ERROR20 = 100270
GLU_NURBS_ERROR21 = 100271
GLU_NURBS_ERROR22 = 100272
GLU_NURBS_ERROR23 = 100273
GLU_NURBS_ERROR24 = 100274
GLU_NURBS_ERROR25 = 100275
GLU_NURBS_ERROR26 = 100276
GLU_NURBS_ERROR27 = 100277
GLU_NURBS_ERROR28 = 100278
GLU_NURBS_ERROR29 = 100279
GLU_NURBS_ERROR30 = 100280
GLU_NURBS_ERROR31 = 100281
GLU_NURBS_ERROR32 = 100282
GLU_NURBS_ERROR33 = 100283
GLU_NURBS_ERROR34 = 100284
GLU_NURBS_ERROR35 = 100285
GLU_NURBS_ERROR36 = 100286
GLU_NURBS_ERROR37 = 100287
GLU_CW = 100120
GLU_CCW = 100121
GLU_INTERIOR = 100122
GLU_EXTERIOR = 100123
GLU_UNKNOWN = 100124
GLU_BEGIN = 100100
GLU_VERTEX = 100101
GLU_END = 100102
GLU_ERROR = 100103
GLU_EDGE_FLAG = 100104
def _define_ChoosePixelFormat():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,POINTER(win32more.Graphics.OpenGL.PIXELFORMATDESCRIPTOR_head))(('ChoosePixelFormat', windll['GDI32.dll']), ((1, 'hdc'),(1, 'ppfd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DescribePixelFormat():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,Int32,UInt32,POINTER(win32more.Graphics.OpenGL.PIXELFORMATDESCRIPTOR_head))(('DescribePixelFormat', windll['GDI32.dll']), ((1, 'hdc'),(1, 'iPixelFormat'),(1, 'nBytes'),(1, 'ppfd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPixelFormat():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC)(('GetPixelFormat', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetPixelFormat():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,POINTER(win32more.Graphics.OpenGL.PIXELFORMATDESCRIPTOR_head))(('SetPixelFormat', windll['GDI32.dll']), ((1, 'hdc'),(1, 'format'),(1, 'ppfd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetEnhMetaFilePixelFormat():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HENHMETAFILE,UInt32,POINTER(win32more.Graphics.OpenGL.PIXELFORMATDESCRIPTOR_head))(('GetEnhMetaFilePixelFormat', windll['GDI32.dll']), ((1, 'hemf'),(1, 'cbBuffer'),(1, 'ppfd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_wglCopyContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.OpenGL.HGLRC,win32more.Graphics.OpenGL.HGLRC,UInt32)(('wglCopyContext', windll['OPENGL32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_wglCreateContext():
    try:
        return WINFUNCTYPE(win32more.Graphics.OpenGL.HGLRC,win32more.Graphics.Gdi.HDC)(('wglCreateContext', windll['OPENGL32.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_wglCreateLayerContext():
    try:
        return WINFUNCTYPE(win32more.Graphics.OpenGL.HGLRC,win32more.Graphics.Gdi.HDC,Int32)(('wglCreateLayerContext', windll['OPENGL32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_wglDeleteContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.OpenGL.HGLRC)(('wglDeleteContext', windll['OPENGL32.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_wglGetCurrentContext():
    try:
        return WINFUNCTYPE(win32more.Graphics.OpenGL.HGLRC,)(('wglGetCurrentContext', windll['OPENGL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_wglGetCurrentDC():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HDC,)(('wglGetCurrentDC', windll['OPENGL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_wglGetProcAddress():
    try:
        return WINFUNCTYPE(win32more.Foundation.PROC,win32more.Foundation.PSTR)(('wglGetProcAddress', windll['OPENGL32.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_wglMakeCurrent():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,win32more.Graphics.OpenGL.HGLRC)(('wglMakeCurrent', windll['OPENGL32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_wglShareLists():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.OpenGL.HGLRC,win32more.Graphics.OpenGL.HGLRC)(('wglShareLists', windll['OPENGL32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_wglUseFontBitmapsA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,UInt32,UInt32,UInt32)(('wglUseFontBitmapsA', windll['OPENGL32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_wglUseFontBitmapsW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,UInt32,UInt32,UInt32)(('wglUseFontBitmapsW', windll['OPENGL32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SwapBuffers():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC)(('SwapBuffers', windll['GDI32.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_wglUseFontOutlinesA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,UInt32,UInt32,UInt32,Single,Single,Int32,POINTER(win32more.Graphics.OpenGL.GLYPHMETRICSFLOAT_head))(('wglUseFontOutlinesA', windll['OPENGL32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),(1, 'param4'),(1, 'param5'),(1, 'param6'),(1, 'param7'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_wglUseFontOutlinesW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,UInt32,UInt32,UInt32,Single,Single,Int32,POINTER(win32more.Graphics.OpenGL.GLYPHMETRICSFLOAT_head))(('wglUseFontOutlinesW', windll['OPENGL32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),(1, 'param4'),(1, 'param5'),(1, 'param6'),(1, 'param7'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_wglDescribeLayerPlane():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,UInt32,POINTER(win32more.Graphics.OpenGL.LAYERPLANEDESCRIPTOR_head))(('wglDescribeLayerPlane', windll['OPENGL32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),(1, 'param4'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_wglSetLayerPaletteEntries():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,Int32,Int32,Int32,POINTER(win32more.Foundation.COLORREF))(('wglSetLayerPaletteEntries', windll['OPENGL32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),(1, 'param4'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_wglGetLayerPaletteEntries():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,Int32,Int32,Int32,POINTER(win32more.Foundation.COLORREF))(('wglGetLayerPaletteEntries', windll['OPENGL32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),(1, 'param4'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_wglRealizeLayerPalette():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,win32more.Foundation.BOOL)(('wglRealizeLayerPalette', windll['OPENGL32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_wglSwapLayerBuffers():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,UInt32)(('wglSwapLayerBuffers', windll['OPENGL32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glAccum():
    try:
        return WINFUNCTYPE(Void,UInt32,Single)(('glAccum', windll['OPENGL32.dll']), ((1, 'op'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glAlphaFunc():
    try:
        return WINFUNCTYPE(Void,UInt32,Single)(('glAlphaFunc', windll['OPENGL32.dll']), ((1, 'func'),(1, 'ref'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glAreTexturesResident():
    try:
        return WINFUNCTYPE(Byte,Int32,POINTER(UInt32),c_char_p_no)(('glAreTexturesResident', windll['OPENGL32.dll']), ((1, 'n'),(1, 'textures'),(1, 'residences'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glArrayElement():
    try:
        return WINFUNCTYPE(Void,Int32)(('glArrayElement', windll['OPENGL32.dll']), ((1, 'i'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glBegin():
    try:
        return WINFUNCTYPE(Void,UInt32)(('glBegin', windll['OPENGL32.dll']), ((1, 'mode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glBindTexture():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32)(('glBindTexture', windll['OPENGL32.dll']), ((1, 'target'),(1, 'texture'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glBitmap():
    try:
        return WINFUNCTYPE(Void,Int32,Int32,Single,Single,Single,Single,c_char_p_no)(('glBitmap', windll['OPENGL32.dll']), ((1, 'width'),(1, 'height'),(1, 'xorig'),(1, 'yorig'),(1, 'xmove'),(1, 'ymove'),(1, 'bitmap'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glBlendFunc():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32)(('glBlendFunc', windll['OPENGL32.dll']), ((1, 'sfactor'),(1, 'dfactor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glCallList():
    try:
        return WINFUNCTYPE(Void,UInt32)(('glCallList', windll['OPENGL32.dll']), ((1, 'list'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glCallLists():
    try:
        return WINFUNCTYPE(Void,Int32,UInt32,c_void_p)(('glCallLists', windll['OPENGL32.dll']), ((1, 'n'),(1, 'type'),(1, 'lists'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glClear():
    try:
        return WINFUNCTYPE(Void,UInt32)(('glClear', windll['OPENGL32.dll']), ((1, 'mask'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glClearAccum():
    try:
        return WINFUNCTYPE(Void,Single,Single,Single,Single)(('glClearAccum', windll['OPENGL32.dll']), ((1, 'red'),(1, 'green'),(1, 'blue'),(1, 'alpha'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glClearColor():
    try:
        return WINFUNCTYPE(Void,Single,Single,Single,Single)(('glClearColor', windll['OPENGL32.dll']), ((1, 'red'),(1, 'green'),(1, 'blue'),(1, 'alpha'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glClearDepth():
    try:
        return WINFUNCTYPE(Void,Double)(('glClearDepth', windll['OPENGL32.dll']), ((1, 'depth'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glClearIndex():
    try:
        return WINFUNCTYPE(Void,Single)(('glClearIndex', windll['OPENGL32.dll']), ((1, 'c'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glClearStencil():
    try:
        return WINFUNCTYPE(Void,Int32)(('glClearStencil', windll['OPENGL32.dll']), ((1, 's'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glClipPlane():
    try:
        return WINFUNCTYPE(Void,UInt32,POINTER(Double))(('glClipPlane', windll['OPENGL32.dll']), ((1, 'plane'),(1, 'equation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor3b():
    try:
        return WINFUNCTYPE(Void,SByte,SByte,SByte)(('glColor3b', windll['OPENGL32.dll']), ((1, 'red'),(1, 'green'),(1, 'blue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor3bv():
    try:
        return WINFUNCTYPE(Void,POINTER(SByte))(('glColor3bv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor3d():
    try:
        return WINFUNCTYPE(Void,Double,Double,Double)(('glColor3d', windll['OPENGL32.dll']), ((1, 'red'),(1, 'green'),(1, 'blue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor3dv():
    try:
        return WINFUNCTYPE(Void,POINTER(Double))(('glColor3dv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor3f():
    try:
        return WINFUNCTYPE(Void,Single,Single,Single)(('glColor3f', windll['OPENGL32.dll']), ((1, 'red'),(1, 'green'),(1, 'blue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor3fv():
    try:
        return WINFUNCTYPE(Void,POINTER(Single))(('glColor3fv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor3i():
    try:
        return WINFUNCTYPE(Void,Int32,Int32,Int32)(('glColor3i', windll['OPENGL32.dll']), ((1, 'red'),(1, 'green'),(1, 'blue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor3iv():
    try:
        return WINFUNCTYPE(Void,POINTER(Int32))(('glColor3iv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor3s():
    try:
        return WINFUNCTYPE(Void,Int16,Int16,Int16)(('glColor3s', windll['OPENGL32.dll']), ((1, 'red'),(1, 'green'),(1, 'blue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor3sv():
    try:
        return WINFUNCTYPE(Void,POINTER(Int16))(('glColor3sv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor3ub():
    try:
        return WINFUNCTYPE(Void,Byte,Byte,Byte)(('glColor3ub', windll['OPENGL32.dll']), ((1, 'red'),(1, 'green'),(1, 'blue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor3ubv():
    try:
        return WINFUNCTYPE(Void,c_char_p_no)(('glColor3ubv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor3ui():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,UInt32)(('glColor3ui', windll['OPENGL32.dll']), ((1, 'red'),(1, 'green'),(1, 'blue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor3uiv():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32))(('glColor3uiv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor3us():
    try:
        return WINFUNCTYPE(Void,UInt16,UInt16,UInt16)(('glColor3us', windll['OPENGL32.dll']), ((1, 'red'),(1, 'green'),(1, 'blue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor3usv():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt16))(('glColor3usv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor4b():
    try:
        return WINFUNCTYPE(Void,SByte,SByte,SByte,SByte)(('glColor4b', windll['OPENGL32.dll']), ((1, 'red'),(1, 'green'),(1, 'blue'),(1, 'alpha'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor4bv():
    try:
        return WINFUNCTYPE(Void,POINTER(SByte))(('glColor4bv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor4d():
    try:
        return WINFUNCTYPE(Void,Double,Double,Double,Double)(('glColor4d', windll['OPENGL32.dll']), ((1, 'red'),(1, 'green'),(1, 'blue'),(1, 'alpha'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor4dv():
    try:
        return WINFUNCTYPE(Void,POINTER(Double))(('glColor4dv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor4f():
    try:
        return WINFUNCTYPE(Void,Single,Single,Single,Single)(('glColor4f', windll['OPENGL32.dll']), ((1, 'red'),(1, 'green'),(1, 'blue'),(1, 'alpha'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor4fv():
    try:
        return WINFUNCTYPE(Void,POINTER(Single))(('glColor4fv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor4i():
    try:
        return WINFUNCTYPE(Void,Int32,Int32,Int32,Int32)(('glColor4i', windll['OPENGL32.dll']), ((1, 'red'),(1, 'green'),(1, 'blue'),(1, 'alpha'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor4iv():
    try:
        return WINFUNCTYPE(Void,POINTER(Int32))(('glColor4iv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor4s():
    try:
        return WINFUNCTYPE(Void,Int16,Int16,Int16,Int16)(('glColor4s', windll['OPENGL32.dll']), ((1, 'red'),(1, 'green'),(1, 'blue'),(1, 'alpha'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor4sv():
    try:
        return WINFUNCTYPE(Void,POINTER(Int16))(('glColor4sv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor4ub():
    try:
        return WINFUNCTYPE(Void,Byte,Byte,Byte,Byte)(('glColor4ub', windll['OPENGL32.dll']), ((1, 'red'),(1, 'green'),(1, 'blue'),(1, 'alpha'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor4ubv():
    try:
        return WINFUNCTYPE(Void,c_char_p_no)(('glColor4ubv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor4ui():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,UInt32,UInt32)(('glColor4ui', windll['OPENGL32.dll']), ((1, 'red'),(1, 'green'),(1, 'blue'),(1, 'alpha'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor4uiv():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32))(('glColor4uiv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor4us():
    try:
        return WINFUNCTYPE(Void,UInt16,UInt16,UInt16,UInt16)(('glColor4us', windll['OPENGL32.dll']), ((1, 'red'),(1, 'green'),(1, 'blue'),(1, 'alpha'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColor4usv():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt16))(('glColor4usv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColorMask():
    try:
        return WINFUNCTYPE(Void,Byte,Byte,Byte,Byte)(('glColorMask', windll['OPENGL32.dll']), ((1, 'red'),(1, 'green'),(1, 'blue'),(1, 'alpha'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColorMaterial():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32)(('glColorMaterial', windll['OPENGL32.dll']), ((1, 'face'),(1, 'mode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glColorPointer():
    try:
        return WINFUNCTYPE(Void,Int32,UInt32,Int32,c_void_p)(('glColorPointer', windll['OPENGL32.dll']), ((1, 'size'),(1, 'type'),(1, 'stride'),(1, 'pointer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glCopyPixels():
    try:
        return WINFUNCTYPE(Void,Int32,Int32,Int32,Int32,UInt32)(('glCopyPixels', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),(1, 'width'),(1, 'height'),(1, 'type'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glCopyTexImage1D():
    try:
        return WINFUNCTYPE(Void,UInt32,Int32,UInt32,Int32,Int32,Int32,Int32)(('glCopyTexImage1D', windll['OPENGL32.dll']), ((1, 'target'),(1, 'level'),(1, 'internalFormat'),(1, 'x'),(1, 'y'),(1, 'width'),(1, 'border'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glCopyTexImage2D():
    try:
        return WINFUNCTYPE(Void,UInt32,Int32,UInt32,Int32,Int32,Int32,Int32,Int32)(('glCopyTexImage2D', windll['OPENGL32.dll']), ((1, 'target'),(1, 'level'),(1, 'internalFormat'),(1, 'x'),(1, 'y'),(1, 'width'),(1, 'height'),(1, 'border'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glCopyTexSubImage1D():
    try:
        return WINFUNCTYPE(Void,UInt32,Int32,Int32,Int32,Int32,Int32)(('glCopyTexSubImage1D', windll['OPENGL32.dll']), ((1, 'target'),(1, 'level'),(1, 'xoffset'),(1, 'x'),(1, 'y'),(1, 'width'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glCopyTexSubImage2D():
    try:
        return WINFUNCTYPE(Void,UInt32,Int32,Int32,Int32,Int32,Int32,Int32,Int32)(('glCopyTexSubImage2D', windll['OPENGL32.dll']), ((1, 'target'),(1, 'level'),(1, 'xoffset'),(1, 'yoffset'),(1, 'x'),(1, 'y'),(1, 'width'),(1, 'height'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glCullFace():
    try:
        return WINFUNCTYPE(Void,UInt32)(('glCullFace', windll['OPENGL32.dll']), ((1, 'mode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glDeleteLists():
    try:
        return WINFUNCTYPE(Void,UInt32,Int32)(('glDeleteLists', windll['OPENGL32.dll']), ((1, 'list'),(1, 'range'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glDeleteTextures():
    try:
        return WINFUNCTYPE(Void,Int32,POINTER(UInt32))(('glDeleteTextures', windll['OPENGL32.dll']), ((1, 'n'),(1, 'textures'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glDepthFunc():
    try:
        return WINFUNCTYPE(Void,UInt32)(('glDepthFunc', windll['OPENGL32.dll']), ((1, 'func'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glDepthMask():
    try:
        return WINFUNCTYPE(Void,Byte)(('glDepthMask', windll['OPENGL32.dll']), ((1, 'flag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glDepthRange():
    try:
        return WINFUNCTYPE(Void,Double,Double)(('glDepthRange', windll['OPENGL32.dll']), ((1, 'zNear'),(1, 'zFar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glDisable():
    try:
        return WINFUNCTYPE(Void,UInt32)(('glDisable', windll['OPENGL32.dll']), ((1, 'cap'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glDisableClientState():
    try:
        return WINFUNCTYPE(Void,UInt32)(('glDisableClientState', windll['OPENGL32.dll']), ((1, 'array'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glDrawArrays():
    try:
        return WINFUNCTYPE(Void,UInt32,Int32,Int32)(('glDrawArrays', windll['OPENGL32.dll']), ((1, 'mode'),(1, 'first'),(1, 'count'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glDrawBuffer():
    try:
        return WINFUNCTYPE(Void,UInt32)(('glDrawBuffer', windll['OPENGL32.dll']), ((1, 'mode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glDrawElements():
    try:
        return WINFUNCTYPE(Void,UInt32,Int32,UInt32,c_void_p)(('glDrawElements', windll['OPENGL32.dll']), ((1, 'mode'),(1, 'count'),(1, 'type'),(1, 'indices'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glDrawPixels():
    try:
        return WINFUNCTYPE(Void,Int32,Int32,UInt32,UInt32,c_void_p)(('glDrawPixels', windll['OPENGL32.dll']), ((1, 'width'),(1, 'height'),(1, 'format'),(1, 'type'),(1, 'pixels'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glEdgeFlag():
    try:
        return WINFUNCTYPE(Void,Byte)(('glEdgeFlag', windll['OPENGL32.dll']), ((1, 'flag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glEdgeFlagPointer():
    try:
        return WINFUNCTYPE(Void,Int32,c_void_p)(('glEdgeFlagPointer', windll['OPENGL32.dll']), ((1, 'stride'),(1, 'pointer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glEdgeFlagv():
    try:
        return WINFUNCTYPE(Void,c_char_p_no)(('glEdgeFlagv', windll['OPENGL32.dll']), ((1, 'flag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glEnable():
    try:
        return WINFUNCTYPE(Void,UInt32)(('glEnable', windll['OPENGL32.dll']), ((1, 'cap'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glEnableClientState():
    try:
        return WINFUNCTYPE(Void,UInt32)(('glEnableClientState', windll['OPENGL32.dll']), ((1, 'array'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glEnd():
    try:
        return WINFUNCTYPE(Void,)(('glEnd', windll['OPENGL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_glEndList():
    try:
        return WINFUNCTYPE(Void,)(('glEndList', windll['OPENGL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_glEvalCoord1d():
    try:
        return WINFUNCTYPE(Void,Double)(('glEvalCoord1d', windll['OPENGL32.dll']), ((1, 'u'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glEvalCoord1dv():
    try:
        return WINFUNCTYPE(Void,POINTER(Double))(('glEvalCoord1dv', windll['OPENGL32.dll']), ((1, 'u'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glEvalCoord1f():
    try:
        return WINFUNCTYPE(Void,Single)(('glEvalCoord1f', windll['OPENGL32.dll']), ((1, 'u'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glEvalCoord1fv():
    try:
        return WINFUNCTYPE(Void,POINTER(Single))(('glEvalCoord1fv', windll['OPENGL32.dll']), ((1, 'u'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glEvalCoord2d():
    try:
        return WINFUNCTYPE(Void,Double,Double)(('glEvalCoord2d', windll['OPENGL32.dll']), ((1, 'u'),(1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glEvalCoord2dv():
    try:
        return WINFUNCTYPE(Void,POINTER(Double))(('glEvalCoord2dv', windll['OPENGL32.dll']), ((1, 'u'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glEvalCoord2f():
    try:
        return WINFUNCTYPE(Void,Single,Single)(('glEvalCoord2f', windll['OPENGL32.dll']), ((1, 'u'),(1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glEvalCoord2fv():
    try:
        return WINFUNCTYPE(Void,POINTER(Single))(('glEvalCoord2fv', windll['OPENGL32.dll']), ((1, 'u'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glEvalMesh1():
    try:
        return WINFUNCTYPE(Void,UInt32,Int32,Int32)(('glEvalMesh1', windll['OPENGL32.dll']), ((1, 'mode'),(1, 'i1'),(1, 'i2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glEvalMesh2():
    try:
        return WINFUNCTYPE(Void,UInt32,Int32,Int32,Int32,Int32)(('glEvalMesh2', windll['OPENGL32.dll']), ((1, 'mode'),(1, 'i1'),(1, 'i2'),(1, 'j1'),(1, 'j2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glEvalPoint1():
    try:
        return WINFUNCTYPE(Void,Int32)(('glEvalPoint1', windll['OPENGL32.dll']), ((1, 'i'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glEvalPoint2():
    try:
        return WINFUNCTYPE(Void,Int32,Int32)(('glEvalPoint2', windll['OPENGL32.dll']), ((1, 'i'),(1, 'j'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glFeedbackBuffer():
    try:
        return WINFUNCTYPE(Void,Int32,UInt32,POINTER(Single))(('glFeedbackBuffer', windll['OPENGL32.dll']), ((1, 'size'),(1, 'type'),(1, 'buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glFinish():
    try:
        return WINFUNCTYPE(Void,)(('glFinish', windll['OPENGL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_glFlush():
    try:
        return WINFUNCTYPE(Void,)(('glFlush', windll['OPENGL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_glFogf():
    try:
        return WINFUNCTYPE(Void,UInt32,Single)(('glFogf', windll['OPENGL32.dll']), ((1, 'pname'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glFogfv():
    try:
        return WINFUNCTYPE(Void,UInt32,POINTER(Single))(('glFogfv', windll['OPENGL32.dll']), ((1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glFogi():
    try:
        return WINFUNCTYPE(Void,UInt32,Int32)(('glFogi', windll['OPENGL32.dll']), ((1, 'pname'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glFogiv():
    try:
        return WINFUNCTYPE(Void,UInt32,POINTER(Int32))(('glFogiv', windll['OPENGL32.dll']), ((1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glFrontFace():
    try:
        return WINFUNCTYPE(Void,UInt32)(('glFrontFace', windll['OPENGL32.dll']), ((1, 'mode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glFrustum():
    try:
        return WINFUNCTYPE(Void,Double,Double,Double,Double,Double,Double)(('glFrustum', windll['OPENGL32.dll']), ((1, 'left'),(1, 'right'),(1, 'bottom'),(1, 'top'),(1, 'zNear'),(1, 'zFar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glGenLists():
    try:
        return WINFUNCTYPE(UInt32,Int32)(('glGenLists', windll['OPENGL32.dll']), ((1, 'range'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glGenTextures():
    try:
        return WINFUNCTYPE(Void,Int32,POINTER(UInt32))(('glGenTextures', windll['OPENGL32.dll']), ((1, 'n'),(1, 'textures'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glGetBooleanv():
    try:
        return WINFUNCTYPE(Void,UInt32,c_char_p_no)(('glGetBooleanv', windll['OPENGL32.dll']), ((1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glGetClipPlane():
    try:
        return WINFUNCTYPE(Void,UInt32,POINTER(Double))(('glGetClipPlane', windll['OPENGL32.dll']), ((1, 'plane'),(1, 'equation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glGetDoublev():
    try:
        return WINFUNCTYPE(Void,UInt32,POINTER(Double))(('glGetDoublev', windll['OPENGL32.dll']), ((1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glGetError():
    try:
        return WINFUNCTYPE(UInt32,)(('glGetError', windll['OPENGL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_glGetFloatv():
    try:
        return WINFUNCTYPE(Void,UInt32,POINTER(Single))(('glGetFloatv', windll['OPENGL32.dll']), ((1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glGetIntegerv():
    try:
        return WINFUNCTYPE(Void,UInt32,POINTER(Int32))(('glGetIntegerv', windll['OPENGL32.dll']), ((1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glGetLightfv():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(Single))(('glGetLightfv', windll['OPENGL32.dll']), ((1, 'light'),(1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glGetLightiv():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(Int32))(('glGetLightiv', windll['OPENGL32.dll']), ((1, 'light'),(1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glGetMapdv():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(Double))(('glGetMapdv', windll['OPENGL32.dll']), ((1, 'target'),(1, 'query'),(1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glGetMapfv():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(Single))(('glGetMapfv', windll['OPENGL32.dll']), ((1, 'target'),(1, 'query'),(1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glGetMapiv():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(Int32))(('glGetMapiv', windll['OPENGL32.dll']), ((1, 'target'),(1, 'query'),(1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glGetMaterialfv():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(Single))(('glGetMaterialfv', windll['OPENGL32.dll']), ((1, 'face'),(1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glGetMaterialiv():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(Int32))(('glGetMaterialiv', windll['OPENGL32.dll']), ((1, 'face'),(1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glGetPixelMapfv():
    try:
        return WINFUNCTYPE(Void,UInt32,POINTER(Single))(('glGetPixelMapfv', windll['OPENGL32.dll']), ((1, 'map'),(1, 'values'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glGetPixelMapuiv():
    try:
        return WINFUNCTYPE(Void,UInt32,POINTER(UInt32))(('glGetPixelMapuiv', windll['OPENGL32.dll']), ((1, 'map'),(1, 'values'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glGetPixelMapusv():
    try:
        return WINFUNCTYPE(Void,UInt32,POINTER(UInt16))(('glGetPixelMapusv', windll['OPENGL32.dll']), ((1, 'map'),(1, 'values'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glGetPointerv():
    try:
        return WINFUNCTYPE(Void,UInt32,POINTER(c_void_p))(('glGetPointerv', windll['OPENGL32.dll']), ((1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glGetPolygonStipple():
    try:
        return WINFUNCTYPE(Void,c_char_p_no)(('glGetPolygonStipple', windll['OPENGL32.dll']), ((1, 'mask'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glGetString():
    try:
        return WINFUNCTYPE(c_char_p_no,UInt32)(('glGetString', windll['OPENGL32.dll']), ((1, 'name'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glGetTexEnvfv():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(Single))(('glGetTexEnvfv', windll['OPENGL32.dll']), ((1, 'target'),(1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glGetTexEnviv():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(Int32))(('glGetTexEnviv', windll['OPENGL32.dll']), ((1, 'target'),(1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glGetTexGendv():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(Double))(('glGetTexGendv', windll['OPENGL32.dll']), ((1, 'coord'),(1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glGetTexGenfv():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(Single))(('glGetTexGenfv', windll['OPENGL32.dll']), ((1, 'coord'),(1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glGetTexGeniv():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(Int32))(('glGetTexGeniv', windll['OPENGL32.dll']), ((1, 'coord'),(1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glGetTexImage():
    try:
        return WINFUNCTYPE(Void,UInt32,Int32,UInt32,UInt32,c_void_p)(('glGetTexImage', windll['OPENGL32.dll']), ((1, 'target'),(1, 'level'),(1, 'format'),(1, 'type'),(1, 'pixels'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glGetTexLevelParameterfv():
    try:
        return WINFUNCTYPE(Void,UInt32,Int32,UInt32,POINTER(Single))(('glGetTexLevelParameterfv', windll['OPENGL32.dll']), ((1, 'target'),(1, 'level'),(1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glGetTexLevelParameteriv():
    try:
        return WINFUNCTYPE(Void,UInt32,Int32,UInt32,POINTER(Int32))(('glGetTexLevelParameteriv', windll['OPENGL32.dll']), ((1, 'target'),(1, 'level'),(1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glGetTexParameterfv():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(Single))(('glGetTexParameterfv', windll['OPENGL32.dll']), ((1, 'target'),(1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glGetTexParameteriv():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(Int32))(('glGetTexParameteriv', windll['OPENGL32.dll']), ((1, 'target'),(1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glHint():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32)(('glHint', windll['OPENGL32.dll']), ((1, 'target'),(1, 'mode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glIndexMask():
    try:
        return WINFUNCTYPE(Void,UInt32)(('glIndexMask', windll['OPENGL32.dll']), ((1, 'mask'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glIndexPointer():
    try:
        return WINFUNCTYPE(Void,UInt32,Int32,c_void_p)(('glIndexPointer', windll['OPENGL32.dll']), ((1, 'type'),(1, 'stride'),(1, 'pointer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glIndexd():
    try:
        return WINFUNCTYPE(Void,Double)(('glIndexd', windll['OPENGL32.dll']), ((1, 'c'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glIndexdv():
    try:
        return WINFUNCTYPE(Void,POINTER(Double))(('glIndexdv', windll['OPENGL32.dll']), ((1, 'c'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glIndexf():
    try:
        return WINFUNCTYPE(Void,Single)(('glIndexf', windll['OPENGL32.dll']), ((1, 'c'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glIndexfv():
    try:
        return WINFUNCTYPE(Void,POINTER(Single))(('glIndexfv', windll['OPENGL32.dll']), ((1, 'c'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glIndexi():
    try:
        return WINFUNCTYPE(Void,Int32)(('glIndexi', windll['OPENGL32.dll']), ((1, 'c'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glIndexiv():
    try:
        return WINFUNCTYPE(Void,POINTER(Int32))(('glIndexiv', windll['OPENGL32.dll']), ((1, 'c'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glIndexs():
    try:
        return WINFUNCTYPE(Void,Int16)(('glIndexs', windll['OPENGL32.dll']), ((1, 'c'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glIndexsv():
    try:
        return WINFUNCTYPE(Void,POINTER(Int16))(('glIndexsv', windll['OPENGL32.dll']), ((1, 'c'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glIndexub():
    try:
        return WINFUNCTYPE(Void,Byte)(('glIndexub', windll['OPENGL32.dll']), ((1, 'c'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glIndexubv():
    try:
        return WINFUNCTYPE(Void,c_char_p_no)(('glIndexubv', windll['OPENGL32.dll']), ((1, 'c'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glInitNames():
    try:
        return WINFUNCTYPE(Void,)(('glInitNames', windll['OPENGL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_glInterleavedArrays():
    try:
        return WINFUNCTYPE(Void,UInt32,Int32,c_void_p)(('glInterleavedArrays', windll['OPENGL32.dll']), ((1, 'format'),(1, 'stride'),(1, 'pointer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glIsEnabled():
    try:
        return WINFUNCTYPE(Byte,UInt32)(('glIsEnabled', windll['OPENGL32.dll']), ((1, 'cap'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glIsList():
    try:
        return WINFUNCTYPE(Byte,UInt32)(('glIsList', windll['OPENGL32.dll']), ((1, 'list'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glIsTexture():
    try:
        return WINFUNCTYPE(Byte,UInt32)(('glIsTexture', windll['OPENGL32.dll']), ((1, 'texture'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glLightModelf():
    try:
        return WINFUNCTYPE(Void,UInt32,Single)(('glLightModelf', windll['OPENGL32.dll']), ((1, 'pname'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glLightModelfv():
    try:
        return WINFUNCTYPE(Void,UInt32,POINTER(Single))(('glLightModelfv', windll['OPENGL32.dll']), ((1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glLightModeli():
    try:
        return WINFUNCTYPE(Void,UInt32,Int32)(('glLightModeli', windll['OPENGL32.dll']), ((1, 'pname'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glLightModeliv():
    try:
        return WINFUNCTYPE(Void,UInt32,POINTER(Int32))(('glLightModeliv', windll['OPENGL32.dll']), ((1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glLightf():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,Single)(('glLightf', windll['OPENGL32.dll']), ((1, 'light'),(1, 'pname'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glLightfv():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(Single))(('glLightfv', windll['OPENGL32.dll']), ((1, 'light'),(1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glLighti():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,Int32)(('glLighti', windll['OPENGL32.dll']), ((1, 'light'),(1, 'pname'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glLightiv():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(Int32))(('glLightiv', windll['OPENGL32.dll']), ((1, 'light'),(1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glLineStipple():
    try:
        return WINFUNCTYPE(Void,Int32,UInt16)(('glLineStipple', windll['OPENGL32.dll']), ((1, 'factor'),(1, 'pattern'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glLineWidth():
    try:
        return WINFUNCTYPE(Void,Single)(('glLineWidth', windll['OPENGL32.dll']), ((1, 'width'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glListBase():
    try:
        return WINFUNCTYPE(Void,UInt32)(('glListBase', windll['OPENGL32.dll']), ((1, 'base'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glLoadIdentity():
    try:
        return WINFUNCTYPE(Void,)(('glLoadIdentity', windll['OPENGL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_glLoadMatrixd():
    try:
        return WINFUNCTYPE(Void,POINTER(Double))(('glLoadMatrixd', windll['OPENGL32.dll']), ((1, 'm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glLoadMatrixf():
    try:
        return WINFUNCTYPE(Void,POINTER(Single))(('glLoadMatrixf', windll['OPENGL32.dll']), ((1, 'm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glLoadName():
    try:
        return WINFUNCTYPE(Void,UInt32)(('glLoadName', windll['OPENGL32.dll']), ((1, 'name'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glLogicOp():
    try:
        return WINFUNCTYPE(Void,UInt32)(('glLogicOp', windll['OPENGL32.dll']), ((1, 'opcode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glMap1d():
    try:
        return WINFUNCTYPE(Void,UInt32,Double,Double,Int32,Int32,POINTER(Double))(('glMap1d', windll['OPENGL32.dll']), ((1, 'target'),(1, 'u1'),(1, 'u2'),(1, 'stride'),(1, 'order'),(1, 'points'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glMap1f():
    try:
        return WINFUNCTYPE(Void,UInt32,Single,Single,Int32,Int32,POINTER(Single))(('glMap1f', windll['OPENGL32.dll']), ((1, 'target'),(1, 'u1'),(1, 'u2'),(1, 'stride'),(1, 'order'),(1, 'points'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glMap2d():
    try:
        return WINFUNCTYPE(Void,UInt32,Double,Double,Int32,Int32,Double,Double,Int32,Int32,POINTER(Double))(('glMap2d', windll['OPENGL32.dll']), ((1, 'target'),(1, 'u1'),(1, 'u2'),(1, 'ustride'),(1, 'uorder'),(1, 'v1'),(1, 'v2'),(1, 'vstride'),(1, 'vorder'),(1, 'points'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glMap2f():
    try:
        return WINFUNCTYPE(Void,UInt32,Single,Single,Int32,Int32,Single,Single,Int32,Int32,POINTER(Single))(('glMap2f', windll['OPENGL32.dll']), ((1, 'target'),(1, 'u1'),(1, 'u2'),(1, 'ustride'),(1, 'uorder'),(1, 'v1'),(1, 'v2'),(1, 'vstride'),(1, 'vorder'),(1, 'points'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glMapGrid1d():
    try:
        return WINFUNCTYPE(Void,Int32,Double,Double)(('glMapGrid1d', windll['OPENGL32.dll']), ((1, 'un'),(1, 'u1'),(1, 'u2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glMapGrid1f():
    try:
        return WINFUNCTYPE(Void,Int32,Single,Single)(('glMapGrid1f', windll['OPENGL32.dll']), ((1, 'un'),(1, 'u1'),(1, 'u2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glMapGrid2d():
    try:
        return WINFUNCTYPE(Void,Int32,Double,Double,Int32,Double,Double)(('glMapGrid2d', windll['OPENGL32.dll']), ((1, 'un'),(1, 'u1'),(1, 'u2'),(1, 'vn'),(1, 'v1'),(1, 'v2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glMapGrid2f():
    try:
        return WINFUNCTYPE(Void,Int32,Single,Single,Int32,Single,Single)(('glMapGrid2f', windll['OPENGL32.dll']), ((1, 'un'),(1, 'u1'),(1, 'u2'),(1, 'vn'),(1, 'v1'),(1, 'v2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glMaterialf():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,Single)(('glMaterialf', windll['OPENGL32.dll']), ((1, 'face'),(1, 'pname'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glMaterialfv():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(Single))(('glMaterialfv', windll['OPENGL32.dll']), ((1, 'face'),(1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glMateriali():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,Int32)(('glMateriali', windll['OPENGL32.dll']), ((1, 'face'),(1, 'pname'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glMaterialiv():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(Int32))(('glMaterialiv', windll['OPENGL32.dll']), ((1, 'face'),(1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glMatrixMode():
    try:
        return WINFUNCTYPE(Void,UInt32)(('glMatrixMode', windll['OPENGL32.dll']), ((1, 'mode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glMultMatrixd():
    try:
        return WINFUNCTYPE(Void,POINTER(Double))(('glMultMatrixd', windll['OPENGL32.dll']), ((1, 'm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glMultMatrixf():
    try:
        return WINFUNCTYPE(Void,POINTER(Single))(('glMultMatrixf', windll['OPENGL32.dll']), ((1, 'm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glNewList():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32)(('glNewList', windll['OPENGL32.dll']), ((1, 'list'),(1, 'mode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glNormal3b():
    try:
        return WINFUNCTYPE(Void,SByte,SByte,SByte)(('glNormal3b', windll['OPENGL32.dll']), ((1, 'nx'),(1, 'ny'),(1, 'nz'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glNormal3bv():
    try:
        return WINFUNCTYPE(Void,POINTER(SByte))(('glNormal3bv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glNormal3d():
    try:
        return WINFUNCTYPE(Void,Double,Double,Double)(('glNormal3d', windll['OPENGL32.dll']), ((1, 'nx'),(1, 'ny'),(1, 'nz'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glNormal3dv():
    try:
        return WINFUNCTYPE(Void,POINTER(Double))(('glNormal3dv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glNormal3f():
    try:
        return WINFUNCTYPE(Void,Single,Single,Single)(('glNormal3f', windll['OPENGL32.dll']), ((1, 'nx'),(1, 'ny'),(1, 'nz'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glNormal3fv():
    try:
        return WINFUNCTYPE(Void,POINTER(Single))(('glNormal3fv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glNormal3i():
    try:
        return WINFUNCTYPE(Void,Int32,Int32,Int32)(('glNormal3i', windll['OPENGL32.dll']), ((1, 'nx'),(1, 'ny'),(1, 'nz'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glNormal3iv():
    try:
        return WINFUNCTYPE(Void,POINTER(Int32))(('glNormal3iv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glNormal3s():
    try:
        return WINFUNCTYPE(Void,Int16,Int16,Int16)(('glNormal3s', windll['OPENGL32.dll']), ((1, 'nx'),(1, 'ny'),(1, 'nz'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glNormal3sv():
    try:
        return WINFUNCTYPE(Void,POINTER(Int16))(('glNormal3sv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glNormalPointer():
    try:
        return WINFUNCTYPE(Void,UInt32,Int32,c_void_p)(('glNormalPointer', windll['OPENGL32.dll']), ((1, 'type'),(1, 'stride'),(1, 'pointer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glOrtho():
    try:
        return WINFUNCTYPE(Void,Double,Double,Double,Double,Double,Double)(('glOrtho', windll['OPENGL32.dll']), ((1, 'left'),(1, 'right'),(1, 'bottom'),(1, 'top'),(1, 'zNear'),(1, 'zFar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glPassThrough():
    try:
        return WINFUNCTYPE(Void,Single)(('glPassThrough', windll['OPENGL32.dll']), ((1, 'token'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glPixelMapfv():
    try:
        return WINFUNCTYPE(Void,UInt32,Int32,POINTER(Single))(('glPixelMapfv', windll['OPENGL32.dll']), ((1, 'map'),(1, 'mapsize'),(1, 'values'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glPixelMapuiv():
    try:
        return WINFUNCTYPE(Void,UInt32,Int32,POINTER(UInt32))(('glPixelMapuiv', windll['OPENGL32.dll']), ((1, 'map'),(1, 'mapsize'),(1, 'values'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glPixelMapusv():
    try:
        return WINFUNCTYPE(Void,UInt32,Int32,POINTER(UInt16))(('glPixelMapusv', windll['OPENGL32.dll']), ((1, 'map'),(1, 'mapsize'),(1, 'values'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glPixelStoref():
    try:
        return WINFUNCTYPE(Void,UInt32,Single)(('glPixelStoref', windll['OPENGL32.dll']), ((1, 'pname'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glPixelStorei():
    try:
        return WINFUNCTYPE(Void,UInt32,Int32)(('glPixelStorei', windll['OPENGL32.dll']), ((1, 'pname'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glPixelTransferf():
    try:
        return WINFUNCTYPE(Void,UInt32,Single)(('glPixelTransferf', windll['OPENGL32.dll']), ((1, 'pname'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glPixelTransferi():
    try:
        return WINFUNCTYPE(Void,UInt32,Int32)(('glPixelTransferi', windll['OPENGL32.dll']), ((1, 'pname'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glPixelZoom():
    try:
        return WINFUNCTYPE(Void,Single,Single)(('glPixelZoom', windll['OPENGL32.dll']), ((1, 'xfactor'),(1, 'yfactor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glPointSize():
    try:
        return WINFUNCTYPE(Void,Single)(('glPointSize', windll['OPENGL32.dll']), ((1, 'size'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glPolygonMode():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32)(('glPolygonMode', windll['OPENGL32.dll']), ((1, 'face'),(1, 'mode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glPolygonOffset():
    try:
        return WINFUNCTYPE(Void,Single,Single)(('glPolygonOffset', windll['OPENGL32.dll']), ((1, 'factor'),(1, 'units'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glPolygonStipple():
    try:
        return WINFUNCTYPE(Void,c_char_p_no)(('glPolygonStipple', windll['OPENGL32.dll']), ((1, 'mask'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glPopAttrib():
    try:
        return WINFUNCTYPE(Void,)(('glPopAttrib', windll['OPENGL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_glPopClientAttrib():
    try:
        return WINFUNCTYPE(Void,)(('glPopClientAttrib', windll['OPENGL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_glPopMatrix():
    try:
        return WINFUNCTYPE(Void,)(('glPopMatrix', windll['OPENGL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_glPopName():
    try:
        return WINFUNCTYPE(Void,)(('glPopName', windll['OPENGL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_glPrioritizeTextures():
    try:
        return WINFUNCTYPE(Void,Int32,POINTER(UInt32),POINTER(Single))(('glPrioritizeTextures', windll['OPENGL32.dll']), ((1, 'n'),(1, 'textures'),(1, 'priorities'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glPushAttrib():
    try:
        return WINFUNCTYPE(Void,UInt32)(('glPushAttrib', windll['OPENGL32.dll']), ((1, 'mask'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glPushClientAttrib():
    try:
        return WINFUNCTYPE(Void,UInt32)(('glPushClientAttrib', windll['OPENGL32.dll']), ((1, 'mask'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glPushMatrix():
    try:
        return WINFUNCTYPE(Void,)(('glPushMatrix', windll['OPENGL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_glPushName():
    try:
        return WINFUNCTYPE(Void,UInt32)(('glPushName', windll['OPENGL32.dll']), ((1, 'name'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRasterPos2d():
    try:
        return WINFUNCTYPE(Void,Double,Double)(('glRasterPos2d', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRasterPos2dv():
    try:
        return WINFUNCTYPE(Void,POINTER(Double))(('glRasterPos2dv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRasterPos2f():
    try:
        return WINFUNCTYPE(Void,Single,Single)(('glRasterPos2f', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRasterPos2fv():
    try:
        return WINFUNCTYPE(Void,POINTER(Single))(('glRasterPos2fv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRasterPos2i():
    try:
        return WINFUNCTYPE(Void,Int32,Int32)(('glRasterPos2i', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRasterPos2iv():
    try:
        return WINFUNCTYPE(Void,POINTER(Int32))(('glRasterPos2iv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRasterPos2s():
    try:
        return WINFUNCTYPE(Void,Int16,Int16)(('glRasterPos2s', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRasterPos2sv():
    try:
        return WINFUNCTYPE(Void,POINTER(Int16))(('glRasterPos2sv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRasterPos3d():
    try:
        return WINFUNCTYPE(Void,Double,Double,Double)(('glRasterPos3d', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),(1, 'z'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRasterPos3dv():
    try:
        return WINFUNCTYPE(Void,POINTER(Double))(('glRasterPos3dv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRasterPos3f():
    try:
        return WINFUNCTYPE(Void,Single,Single,Single)(('glRasterPos3f', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),(1, 'z'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRasterPos3fv():
    try:
        return WINFUNCTYPE(Void,POINTER(Single))(('glRasterPos3fv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRasterPos3i():
    try:
        return WINFUNCTYPE(Void,Int32,Int32,Int32)(('glRasterPos3i', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),(1, 'z'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRasterPos3iv():
    try:
        return WINFUNCTYPE(Void,POINTER(Int32))(('glRasterPos3iv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRasterPos3s():
    try:
        return WINFUNCTYPE(Void,Int16,Int16,Int16)(('glRasterPos3s', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),(1, 'z'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRasterPos3sv():
    try:
        return WINFUNCTYPE(Void,POINTER(Int16))(('glRasterPos3sv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRasterPos4d():
    try:
        return WINFUNCTYPE(Void,Double,Double,Double,Double)(('glRasterPos4d', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),(1, 'z'),(1, 'w'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRasterPos4dv():
    try:
        return WINFUNCTYPE(Void,POINTER(Double))(('glRasterPos4dv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRasterPos4f():
    try:
        return WINFUNCTYPE(Void,Single,Single,Single,Single)(('glRasterPos4f', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),(1, 'z'),(1, 'w'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRasterPos4fv():
    try:
        return WINFUNCTYPE(Void,POINTER(Single))(('glRasterPos4fv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRasterPos4i():
    try:
        return WINFUNCTYPE(Void,Int32,Int32,Int32,Int32)(('glRasterPos4i', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),(1, 'z'),(1, 'w'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRasterPos4iv():
    try:
        return WINFUNCTYPE(Void,POINTER(Int32))(('glRasterPos4iv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRasterPos4s():
    try:
        return WINFUNCTYPE(Void,Int16,Int16,Int16,Int16)(('glRasterPos4s', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),(1, 'z'),(1, 'w'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRasterPos4sv():
    try:
        return WINFUNCTYPE(Void,POINTER(Int16))(('glRasterPos4sv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glReadBuffer():
    try:
        return WINFUNCTYPE(Void,UInt32)(('glReadBuffer', windll['OPENGL32.dll']), ((1, 'mode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glReadPixels():
    try:
        return WINFUNCTYPE(Void,Int32,Int32,Int32,Int32,UInt32,UInt32,c_void_p)(('glReadPixels', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),(1, 'width'),(1, 'height'),(1, 'format'),(1, 'type'),(1, 'pixels'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRectd():
    try:
        return WINFUNCTYPE(Void,Double,Double,Double,Double)(('glRectd', windll['OPENGL32.dll']), ((1, 'x1'),(1, 'y1'),(1, 'x2'),(1, 'y2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRectdv():
    try:
        return WINFUNCTYPE(Void,POINTER(Double),POINTER(Double))(('glRectdv', windll['OPENGL32.dll']), ((1, 'v1'),(1, 'v2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRectf():
    try:
        return WINFUNCTYPE(Void,Single,Single,Single,Single)(('glRectf', windll['OPENGL32.dll']), ((1, 'x1'),(1, 'y1'),(1, 'x2'),(1, 'y2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRectfv():
    try:
        return WINFUNCTYPE(Void,POINTER(Single),POINTER(Single))(('glRectfv', windll['OPENGL32.dll']), ((1, 'v1'),(1, 'v2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRecti():
    try:
        return WINFUNCTYPE(Void,Int32,Int32,Int32,Int32)(('glRecti', windll['OPENGL32.dll']), ((1, 'x1'),(1, 'y1'),(1, 'x2'),(1, 'y2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRectiv():
    try:
        return WINFUNCTYPE(Void,POINTER(Int32),POINTER(Int32))(('glRectiv', windll['OPENGL32.dll']), ((1, 'v1'),(1, 'v2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRects():
    try:
        return WINFUNCTYPE(Void,Int16,Int16,Int16,Int16)(('glRects', windll['OPENGL32.dll']), ((1, 'x1'),(1, 'y1'),(1, 'x2'),(1, 'y2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRectsv():
    try:
        return WINFUNCTYPE(Void,POINTER(Int16),POINTER(Int16))(('glRectsv', windll['OPENGL32.dll']), ((1, 'v1'),(1, 'v2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRenderMode():
    try:
        return WINFUNCTYPE(Int32,UInt32)(('glRenderMode', windll['OPENGL32.dll']), ((1, 'mode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRotated():
    try:
        return WINFUNCTYPE(Void,Double,Double,Double,Double)(('glRotated', windll['OPENGL32.dll']), ((1, 'angle'),(1, 'x'),(1, 'y'),(1, 'z'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glRotatef():
    try:
        return WINFUNCTYPE(Void,Single,Single,Single,Single)(('glRotatef', windll['OPENGL32.dll']), ((1, 'angle'),(1, 'x'),(1, 'y'),(1, 'z'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glScaled():
    try:
        return WINFUNCTYPE(Void,Double,Double,Double)(('glScaled', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),(1, 'z'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glScalef():
    try:
        return WINFUNCTYPE(Void,Single,Single,Single)(('glScalef', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),(1, 'z'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glScissor():
    try:
        return WINFUNCTYPE(Void,Int32,Int32,Int32,Int32)(('glScissor', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),(1, 'width'),(1, 'height'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glSelectBuffer():
    try:
        return WINFUNCTYPE(Void,Int32,POINTER(UInt32))(('glSelectBuffer', windll['OPENGL32.dll']), ((1, 'size'),(1, 'buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glShadeModel():
    try:
        return WINFUNCTYPE(Void,UInt32)(('glShadeModel', windll['OPENGL32.dll']), ((1, 'mode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glStencilFunc():
    try:
        return WINFUNCTYPE(Void,UInt32,Int32,UInt32)(('glStencilFunc', windll['OPENGL32.dll']), ((1, 'func'),(1, 'ref'),(1, 'mask'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glStencilMask():
    try:
        return WINFUNCTYPE(Void,UInt32)(('glStencilMask', windll['OPENGL32.dll']), ((1, 'mask'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glStencilOp():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,UInt32)(('glStencilOp', windll['OPENGL32.dll']), ((1, 'fail'),(1, 'zfail'),(1, 'zpass'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord1d():
    try:
        return WINFUNCTYPE(Void,Double)(('glTexCoord1d', windll['OPENGL32.dll']), ((1, 's'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord1dv():
    try:
        return WINFUNCTYPE(Void,POINTER(Double))(('glTexCoord1dv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord1f():
    try:
        return WINFUNCTYPE(Void,Single)(('glTexCoord1f', windll['OPENGL32.dll']), ((1, 's'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord1fv():
    try:
        return WINFUNCTYPE(Void,POINTER(Single))(('glTexCoord1fv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord1i():
    try:
        return WINFUNCTYPE(Void,Int32)(('glTexCoord1i', windll['OPENGL32.dll']), ((1, 's'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord1iv():
    try:
        return WINFUNCTYPE(Void,POINTER(Int32))(('glTexCoord1iv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord1s():
    try:
        return WINFUNCTYPE(Void,Int16)(('glTexCoord1s', windll['OPENGL32.dll']), ((1, 's'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord1sv():
    try:
        return WINFUNCTYPE(Void,POINTER(Int16))(('glTexCoord1sv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord2d():
    try:
        return WINFUNCTYPE(Void,Double,Double)(('glTexCoord2d', windll['OPENGL32.dll']), ((1, 's'),(1, 't'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord2dv():
    try:
        return WINFUNCTYPE(Void,POINTER(Double))(('glTexCoord2dv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord2f():
    try:
        return WINFUNCTYPE(Void,Single,Single)(('glTexCoord2f', windll['OPENGL32.dll']), ((1, 's'),(1, 't'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord2fv():
    try:
        return WINFUNCTYPE(Void,POINTER(Single))(('glTexCoord2fv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord2i():
    try:
        return WINFUNCTYPE(Void,Int32,Int32)(('glTexCoord2i', windll['OPENGL32.dll']), ((1, 's'),(1, 't'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord2iv():
    try:
        return WINFUNCTYPE(Void,POINTER(Int32))(('glTexCoord2iv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord2s():
    try:
        return WINFUNCTYPE(Void,Int16,Int16)(('glTexCoord2s', windll['OPENGL32.dll']), ((1, 's'),(1, 't'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord2sv():
    try:
        return WINFUNCTYPE(Void,POINTER(Int16))(('glTexCoord2sv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord3d():
    try:
        return WINFUNCTYPE(Void,Double,Double,Double)(('glTexCoord3d', windll['OPENGL32.dll']), ((1, 's'),(1, 't'),(1, 'r'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord3dv():
    try:
        return WINFUNCTYPE(Void,POINTER(Double))(('glTexCoord3dv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord3f():
    try:
        return WINFUNCTYPE(Void,Single,Single,Single)(('glTexCoord3f', windll['OPENGL32.dll']), ((1, 's'),(1, 't'),(1, 'r'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord3fv():
    try:
        return WINFUNCTYPE(Void,POINTER(Single))(('glTexCoord3fv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord3i():
    try:
        return WINFUNCTYPE(Void,Int32,Int32,Int32)(('glTexCoord3i', windll['OPENGL32.dll']), ((1, 's'),(1, 't'),(1, 'r'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord3iv():
    try:
        return WINFUNCTYPE(Void,POINTER(Int32))(('glTexCoord3iv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord3s():
    try:
        return WINFUNCTYPE(Void,Int16,Int16,Int16)(('glTexCoord3s', windll['OPENGL32.dll']), ((1, 's'),(1, 't'),(1, 'r'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord3sv():
    try:
        return WINFUNCTYPE(Void,POINTER(Int16))(('glTexCoord3sv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord4d():
    try:
        return WINFUNCTYPE(Void,Double,Double,Double,Double)(('glTexCoord4d', windll['OPENGL32.dll']), ((1, 's'),(1, 't'),(1, 'r'),(1, 'q'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord4dv():
    try:
        return WINFUNCTYPE(Void,POINTER(Double))(('glTexCoord4dv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord4f():
    try:
        return WINFUNCTYPE(Void,Single,Single,Single,Single)(('glTexCoord4f', windll['OPENGL32.dll']), ((1, 's'),(1, 't'),(1, 'r'),(1, 'q'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord4fv():
    try:
        return WINFUNCTYPE(Void,POINTER(Single))(('glTexCoord4fv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord4i():
    try:
        return WINFUNCTYPE(Void,Int32,Int32,Int32,Int32)(('glTexCoord4i', windll['OPENGL32.dll']), ((1, 's'),(1, 't'),(1, 'r'),(1, 'q'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord4iv():
    try:
        return WINFUNCTYPE(Void,POINTER(Int32))(('glTexCoord4iv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord4s():
    try:
        return WINFUNCTYPE(Void,Int16,Int16,Int16,Int16)(('glTexCoord4s', windll['OPENGL32.dll']), ((1, 's'),(1, 't'),(1, 'r'),(1, 'q'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoord4sv():
    try:
        return WINFUNCTYPE(Void,POINTER(Int16))(('glTexCoord4sv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexCoordPointer():
    try:
        return WINFUNCTYPE(Void,Int32,UInt32,Int32,c_void_p)(('glTexCoordPointer', windll['OPENGL32.dll']), ((1, 'size'),(1, 'type'),(1, 'stride'),(1, 'pointer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexEnvf():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,Single)(('glTexEnvf', windll['OPENGL32.dll']), ((1, 'target'),(1, 'pname'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexEnvfv():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(Single))(('glTexEnvfv', windll['OPENGL32.dll']), ((1, 'target'),(1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexEnvi():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,Int32)(('glTexEnvi', windll['OPENGL32.dll']), ((1, 'target'),(1, 'pname'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexEnviv():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(Int32))(('glTexEnviv', windll['OPENGL32.dll']), ((1, 'target'),(1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexGend():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,Double)(('glTexGend', windll['OPENGL32.dll']), ((1, 'coord'),(1, 'pname'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexGendv():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(Double))(('glTexGendv', windll['OPENGL32.dll']), ((1, 'coord'),(1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexGenf():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,Single)(('glTexGenf', windll['OPENGL32.dll']), ((1, 'coord'),(1, 'pname'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexGenfv():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(Single))(('glTexGenfv', windll['OPENGL32.dll']), ((1, 'coord'),(1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexGeni():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,Int32)(('glTexGeni', windll['OPENGL32.dll']), ((1, 'coord'),(1, 'pname'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexGeniv():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(Int32))(('glTexGeniv', windll['OPENGL32.dll']), ((1, 'coord'),(1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexImage1D():
    try:
        return WINFUNCTYPE(Void,UInt32,Int32,Int32,Int32,Int32,UInt32,UInt32,c_void_p)(('glTexImage1D', windll['OPENGL32.dll']), ((1, 'target'),(1, 'level'),(1, 'internalformat'),(1, 'width'),(1, 'border'),(1, 'format'),(1, 'type'),(1, 'pixels'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexImage2D():
    try:
        return WINFUNCTYPE(Void,UInt32,Int32,Int32,Int32,Int32,Int32,UInt32,UInt32,c_void_p)(('glTexImage2D', windll['OPENGL32.dll']), ((1, 'target'),(1, 'level'),(1, 'internalformat'),(1, 'width'),(1, 'height'),(1, 'border'),(1, 'format'),(1, 'type'),(1, 'pixels'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexParameterf():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,Single)(('glTexParameterf', windll['OPENGL32.dll']), ((1, 'target'),(1, 'pname'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexParameterfv():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(Single))(('glTexParameterfv', windll['OPENGL32.dll']), ((1, 'target'),(1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexParameteri():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,Int32)(('glTexParameteri', windll['OPENGL32.dll']), ((1, 'target'),(1, 'pname'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexParameteriv():
    try:
        return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(Int32))(('glTexParameteriv', windll['OPENGL32.dll']), ((1, 'target'),(1, 'pname'),(1, 'params'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexSubImage1D():
    try:
        return WINFUNCTYPE(Void,UInt32,Int32,Int32,Int32,UInt32,UInt32,c_void_p)(('glTexSubImage1D', windll['OPENGL32.dll']), ((1, 'target'),(1, 'level'),(1, 'xoffset'),(1, 'width'),(1, 'format'),(1, 'type'),(1, 'pixels'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTexSubImage2D():
    try:
        return WINFUNCTYPE(Void,UInt32,Int32,Int32,Int32,Int32,Int32,UInt32,UInt32,c_void_p)(('glTexSubImage2D', windll['OPENGL32.dll']), ((1, 'target'),(1, 'level'),(1, 'xoffset'),(1, 'yoffset'),(1, 'width'),(1, 'height'),(1, 'format'),(1, 'type'),(1, 'pixels'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTranslated():
    try:
        return WINFUNCTYPE(Void,Double,Double,Double)(('glTranslated', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),(1, 'z'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glTranslatef():
    try:
        return WINFUNCTYPE(Void,Single,Single,Single)(('glTranslatef', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),(1, 'z'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glVertex2d():
    try:
        return WINFUNCTYPE(Void,Double,Double)(('glVertex2d', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glVertex2dv():
    try:
        return WINFUNCTYPE(Void,POINTER(Double))(('glVertex2dv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glVertex2f():
    try:
        return WINFUNCTYPE(Void,Single,Single)(('glVertex2f', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glVertex2fv():
    try:
        return WINFUNCTYPE(Void,POINTER(Single))(('glVertex2fv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glVertex2i():
    try:
        return WINFUNCTYPE(Void,Int32,Int32)(('glVertex2i', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glVertex2iv():
    try:
        return WINFUNCTYPE(Void,POINTER(Int32))(('glVertex2iv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glVertex2s():
    try:
        return WINFUNCTYPE(Void,Int16,Int16)(('glVertex2s', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glVertex2sv():
    try:
        return WINFUNCTYPE(Void,POINTER(Int16))(('glVertex2sv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glVertex3d():
    try:
        return WINFUNCTYPE(Void,Double,Double,Double)(('glVertex3d', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),(1, 'z'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glVertex3dv():
    try:
        return WINFUNCTYPE(Void,POINTER(Double))(('glVertex3dv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glVertex3f():
    try:
        return WINFUNCTYPE(Void,Single,Single,Single)(('glVertex3f', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),(1, 'z'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glVertex3fv():
    try:
        return WINFUNCTYPE(Void,POINTER(Single))(('glVertex3fv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glVertex3i():
    try:
        return WINFUNCTYPE(Void,Int32,Int32,Int32)(('glVertex3i', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),(1, 'z'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glVertex3iv():
    try:
        return WINFUNCTYPE(Void,POINTER(Int32))(('glVertex3iv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glVertex3s():
    try:
        return WINFUNCTYPE(Void,Int16,Int16,Int16)(('glVertex3s', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),(1, 'z'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glVertex3sv():
    try:
        return WINFUNCTYPE(Void,POINTER(Int16))(('glVertex3sv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glVertex4d():
    try:
        return WINFUNCTYPE(Void,Double,Double,Double,Double)(('glVertex4d', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),(1, 'z'),(1, 'w'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glVertex4dv():
    try:
        return WINFUNCTYPE(Void,POINTER(Double))(('glVertex4dv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glVertex4f():
    try:
        return WINFUNCTYPE(Void,Single,Single,Single,Single)(('glVertex4f', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),(1, 'z'),(1, 'w'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glVertex4fv():
    try:
        return WINFUNCTYPE(Void,POINTER(Single))(('glVertex4fv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glVertex4i():
    try:
        return WINFUNCTYPE(Void,Int32,Int32,Int32,Int32)(('glVertex4i', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),(1, 'z'),(1, 'w'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glVertex4iv():
    try:
        return WINFUNCTYPE(Void,POINTER(Int32))(('glVertex4iv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glVertex4s():
    try:
        return WINFUNCTYPE(Void,Int16,Int16,Int16,Int16)(('glVertex4s', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),(1, 'z'),(1, 'w'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glVertex4sv():
    try:
        return WINFUNCTYPE(Void,POINTER(Int16))(('glVertex4sv', windll['OPENGL32.dll']), ((1, 'v'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glVertexPointer():
    try:
        return WINFUNCTYPE(Void,Int32,UInt32,Int32,c_void_p)(('glVertexPointer', windll['OPENGL32.dll']), ((1, 'size'),(1, 'type'),(1, 'stride'),(1, 'pointer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_glViewport():
    try:
        return WINFUNCTYPE(Void,Int32,Int32,Int32,Int32)(('glViewport', windll['OPENGL32.dll']), ((1, 'x'),(1, 'y'),(1, 'width'),(1, 'height'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluErrorString():
    try:
        return WINFUNCTYPE(c_char_p_no,UInt32)(('gluErrorString', windll['GLU32.dll']), ((1, 'errCode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluErrorUnicodeStringEXT():
    try:
        return WINFUNCTYPE(win32more.Foundation.PWSTR,UInt32)(('gluErrorUnicodeStringEXT', windll['GLU32.dll']), ((1, 'errCode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluGetString():
    try:
        return WINFUNCTYPE(c_char_p_no,UInt32)(('gluGetString', windll['GLU32.dll']), ((1, 'name'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluOrtho2D():
    try:
        return WINFUNCTYPE(Void,Double,Double,Double,Double)(('gluOrtho2D', windll['GLU32.dll']), ((1, 'left'),(1, 'right'),(1, 'bottom'),(1, 'top'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluPerspective():
    try:
        return WINFUNCTYPE(Void,Double,Double,Double,Double)(('gluPerspective', windll['GLU32.dll']), ((1, 'fovy'),(1, 'aspect'),(1, 'zNear'),(1, 'zFar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluPickMatrix():
    try:
        return WINFUNCTYPE(Void,Double,Double,Double,Double,POINTER(Int32))(('gluPickMatrix', windll['GLU32.dll']), ((1, 'x'),(1, 'y'),(1, 'width'),(1, 'height'),(1, 'viewport'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluLookAt():
    try:
        return WINFUNCTYPE(Void,Double,Double,Double,Double,Double,Double,Double,Double,Double)(('gluLookAt', windll['GLU32.dll']), ((1, 'eyex'),(1, 'eyey'),(1, 'eyez'),(1, 'centerx'),(1, 'centery'),(1, 'centerz'),(1, 'upx'),(1, 'upy'),(1, 'upz'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluProject():
    try:
        return WINFUNCTYPE(Int32,Double,Double,Double,POINTER(Double),POINTER(Double),POINTER(Int32),POINTER(Double),POINTER(Double),POINTER(Double))(('gluProject', windll['GLU32.dll']), ((1, 'objx'),(1, 'objy'),(1, 'objz'),(1, 'modelMatrix'),(1, 'projMatrix'),(1, 'viewport'),(1, 'winx'),(1, 'winy'),(1, 'winz'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluUnProject():
    try:
        return WINFUNCTYPE(Int32,Double,Double,Double,POINTER(Double),POINTER(Double),POINTER(Int32),POINTER(Double),POINTER(Double),POINTER(Double))(('gluUnProject', windll['GLU32.dll']), ((1, 'winx'),(1, 'winy'),(1, 'winz'),(1, 'modelMatrix'),(1, 'projMatrix'),(1, 'viewport'),(1, 'objx'),(1, 'objy'),(1, 'objz'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluScaleImage():
    try:
        return WINFUNCTYPE(Int32,UInt32,Int32,Int32,UInt32,c_void_p,Int32,Int32,UInt32,c_void_p)(('gluScaleImage', windll['GLU32.dll']), ((1, 'format'),(1, 'widthin'),(1, 'heightin'),(1, 'typein'),(1, 'datain'),(1, 'widthout'),(1, 'heightout'),(1, 'typeout'),(1, 'dataout'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluBuild1DMipmaps():
    try:
        return WINFUNCTYPE(Int32,UInt32,Int32,Int32,UInt32,UInt32,c_void_p)(('gluBuild1DMipmaps', windll['GLU32.dll']), ((1, 'target'),(1, 'components'),(1, 'width'),(1, 'format'),(1, 'type'),(1, 'data'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluBuild2DMipmaps():
    try:
        return WINFUNCTYPE(Int32,UInt32,Int32,Int32,Int32,UInt32,UInt32,c_void_p)(('gluBuild2DMipmaps', windll['GLU32.dll']), ((1, 'target'),(1, 'components'),(1, 'width'),(1, 'height'),(1, 'format'),(1, 'type'),(1, 'data'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluNewQuadric():
    try:
        return WINFUNCTYPE(POINTER(win32more.Graphics.OpenGL.GLUquadric_head),)(('gluNewQuadric', windll['GLU32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluDeleteQuadric():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUquadric_head))(('gluDeleteQuadric', windll['GLU32.dll']), ((1, 'state'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluQuadricNormals():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUquadric_head),UInt32)(('gluQuadricNormals', windll['GLU32.dll']), ((1, 'quadObject'),(1, 'normals'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluQuadricTexture():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUquadric_head),Byte)(('gluQuadricTexture', windll['GLU32.dll']), ((1, 'quadObject'),(1, 'textureCoords'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluQuadricOrientation():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUquadric_head),UInt32)(('gluQuadricOrientation', windll['GLU32.dll']), ((1, 'quadObject'),(1, 'orientation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluQuadricDrawStyle():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUquadric_head),UInt32)(('gluQuadricDrawStyle', windll['GLU32.dll']), ((1, 'quadObject'),(1, 'drawStyle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluCylinder():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUquadric_head),Double,Double,Double,Int32,Int32)(('gluCylinder', windll['GLU32.dll']), ((1, 'qobj'),(1, 'baseRadius'),(1, 'topRadius'),(1, 'height'),(1, 'slices'),(1, 'stacks'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluDisk():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUquadric_head),Double,Double,Int32,Int32)(('gluDisk', windll['GLU32.dll']), ((1, 'qobj'),(1, 'innerRadius'),(1, 'outerRadius'),(1, 'slices'),(1, 'loops'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluPartialDisk():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUquadric_head),Double,Double,Int32,Int32,Double,Double)(('gluPartialDisk', windll['GLU32.dll']), ((1, 'qobj'),(1, 'innerRadius'),(1, 'outerRadius'),(1, 'slices'),(1, 'loops'),(1, 'startAngle'),(1, 'sweepAngle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluSphere():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUquadric_head),Double,Int32,Int32)(('gluSphere', windll['GLU32.dll']), ((1, 'qobj'),(1, 'radius'),(1, 'slices'),(1, 'stacks'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluQuadricCallback():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUquadric_head),UInt32,IntPtr)(('gluQuadricCallback', windll['GLU32.dll']), ((1, 'qobj'),(1, 'which'),(1, 'fn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluNewTess():
    try:
        return WINFUNCTYPE(POINTER(win32more.Graphics.OpenGL.GLUtesselator_head),)(('gluNewTess', windll['GLU32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluDeleteTess():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUtesselator_head))(('gluDeleteTess', windll['GLU32.dll']), ((1, 'tess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluTessBeginPolygon():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUtesselator_head),c_void_p)(('gluTessBeginPolygon', windll['GLU32.dll']), ((1, 'tess'),(1, 'polygon_data'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluTessBeginContour():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUtesselator_head))(('gluTessBeginContour', windll['GLU32.dll']), ((1, 'tess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluTessVertex():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUtesselator_head),POINTER(Double),c_void_p)(('gluTessVertex', windll['GLU32.dll']), ((1, 'tess'),(1, 'coords'),(1, 'data'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluTessEndContour():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUtesselator_head))(('gluTessEndContour', windll['GLU32.dll']), ((1, 'tess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluTessEndPolygon():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUtesselator_head))(('gluTessEndPolygon', windll['GLU32.dll']), ((1, 'tess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluTessProperty():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUtesselator_head),UInt32,Double)(('gluTessProperty', windll['GLU32.dll']), ((1, 'tess'),(1, 'which'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluTessNormal():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUtesselator_head),Double,Double,Double)(('gluTessNormal', windll['GLU32.dll']), ((1, 'tess'),(1, 'x'),(1, 'y'),(1, 'z'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluTessCallback():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUtesselator_head),UInt32,IntPtr)(('gluTessCallback', windll['GLU32.dll']), ((1, 'tess'),(1, 'which'),(1, 'fn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluGetTessProperty():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUtesselator_head),UInt32,POINTER(Double))(('gluGetTessProperty', windll['GLU32.dll']), ((1, 'tess'),(1, 'which'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluNewNurbsRenderer():
    try:
        return WINFUNCTYPE(POINTER(win32more.Graphics.OpenGL.GLUnurbs_head),)(('gluNewNurbsRenderer', windll['GLU32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluDeleteNurbsRenderer():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUnurbs_head))(('gluDeleteNurbsRenderer', windll['GLU32.dll']), ((1, 'nobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluBeginSurface():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUnurbs_head))(('gluBeginSurface', windll['GLU32.dll']), ((1, 'nobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluBeginCurve():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUnurbs_head))(('gluBeginCurve', windll['GLU32.dll']), ((1, 'nobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluEndCurve():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUnurbs_head))(('gluEndCurve', windll['GLU32.dll']), ((1, 'nobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluEndSurface():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUnurbs_head))(('gluEndSurface', windll['GLU32.dll']), ((1, 'nobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluBeginTrim():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUnurbs_head))(('gluBeginTrim', windll['GLU32.dll']), ((1, 'nobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluEndTrim():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUnurbs_head))(('gluEndTrim', windll['GLU32.dll']), ((1, 'nobj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluPwlCurve():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUnurbs_head),Int32,POINTER(Single),Int32,UInt32)(('gluPwlCurve', windll['GLU32.dll']), ((1, 'nobj'),(1, 'count'),(1, 'array'),(1, 'stride'),(1, 'type'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluNurbsCurve():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUnurbs_head),Int32,POINTER(Single),Int32,POINTER(Single),Int32,UInt32)(('gluNurbsCurve', windll['GLU32.dll']), ((1, 'nobj'),(1, 'nknots'),(1, 'knot'),(1, 'stride'),(1, 'ctlarray'),(1, 'order'),(1, 'type'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluNurbsSurface():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUnurbs_head),Int32,POINTER(Single),Int32,POINTER(Single),Int32,Int32,POINTER(Single),Int32,Int32,UInt32)(('gluNurbsSurface', windll['GLU32.dll']), ((1, 'nobj'),(1, 'sknot_count'),(1, 'sknot'),(1, 'tknot_count'),(1, 'tknot'),(1, 's_stride'),(1, 't_stride'),(1, 'ctlarray'),(1, 'sorder'),(1, 'torder'),(1, 'type'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluLoadSamplingMatrices():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUnurbs_head),POINTER(Single),POINTER(Single),POINTER(Int32))(('gluLoadSamplingMatrices', windll['GLU32.dll']), ((1, 'nobj'),(1, 'modelMatrix'),(1, 'projMatrix'),(1, 'viewport'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluNurbsProperty():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUnurbs_head),UInt32,Single)(('gluNurbsProperty', windll['GLU32.dll']), ((1, 'nobj'),(1, 'property'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluGetNurbsProperty():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUnurbs_head),UInt32,POINTER(Single))(('gluGetNurbsProperty', windll['GLU32.dll']), ((1, 'nobj'),(1, 'property'),(1, 'value'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluNurbsCallback():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUnurbs_head),UInt32,IntPtr)(('gluNurbsCallback', windll['GLU32.dll']), ((1, 'nobj'),(1, 'which'),(1, 'fn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluBeginPolygon():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUtesselator_head))(('gluBeginPolygon', windll['GLU32.dll']), ((1, 'tess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluNextContour():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUtesselator_head),UInt32)(('gluNextContour', windll['GLU32.dll']), ((1, 'tess'),(1, 'type'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_gluEndPolygon():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Graphics.OpenGL.GLUtesselator_head))(('gluEndPolygon', windll['GLU32.dll']), ((1, 'tess'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EMRPIXELFORMAT_head():
    class EMRPIXELFORMAT(Structure):
        pass
    return EMRPIXELFORMAT
def _define_EMRPIXELFORMAT():
    EMRPIXELFORMAT = win32more.Graphics.OpenGL.EMRPIXELFORMAT_head
    EMRPIXELFORMAT._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('pfd', win32more.Graphics.OpenGL.PIXELFORMATDESCRIPTOR),
    ]
    return EMRPIXELFORMAT
def _define_GLUnurbs_head():
    class GLUnurbs(Structure):
        pass
    return GLUnurbs
def _define_GLUnurbs():
    GLUnurbs = win32more.Graphics.OpenGL.GLUnurbs_head
    return GLUnurbs
def _define_GLUnurbsErrorProc():
    return WINFUNCTYPE(Void,UInt32)
def _define_GLUquadric_head():
    class GLUquadric(Structure):
        pass
    return GLUquadric
def _define_GLUquadric():
    GLUquadric = win32more.Graphics.OpenGL.GLUquadric_head
    return GLUquadric
def _define_GLUquadricErrorProc():
    return WINFUNCTYPE(Void,UInt32)
def _define_GLUtessBeginDataProc():
    return WINFUNCTYPE(Void,UInt32,c_void_p)
def _define_GLUtessBeginProc():
    return WINFUNCTYPE(Void,UInt32)
def _define_GLUtessCombineDataProc():
    return WINFUNCTYPE(Void,POINTER(Double),POINTER(c_void_p),POINTER(Single),POINTER(c_void_p),c_void_p)
def _define_GLUtessCombineProc():
    return WINFUNCTYPE(Void,POINTER(Double),POINTER(c_void_p),POINTER(Single),POINTER(c_void_p))
def _define_GLUtessEdgeFlagDataProc():
    return WINFUNCTYPE(Void,Byte,c_void_p)
def _define_GLUtessEdgeFlagProc():
    return WINFUNCTYPE(Void,Byte)
def _define_GLUtesselator_head():
    class GLUtesselator(Structure):
        pass
    return GLUtesselator
def _define_GLUtesselator():
    GLUtesselator = win32more.Graphics.OpenGL.GLUtesselator_head
    return GLUtesselator
def _define_GLUtessEndDataProc():
    return WINFUNCTYPE(Void,c_void_p)
def _define_GLUtessEndProc():
    return WINFUNCTYPE(Void,)
def _define_GLUtessErrorDataProc():
    return WINFUNCTYPE(Void,UInt32,c_void_p)
def _define_GLUtessErrorProc():
    return WINFUNCTYPE(Void,UInt32)
def _define_GLUtessVertexDataProc():
    return WINFUNCTYPE(Void,c_void_p,c_void_p)
def _define_GLUtessVertexProc():
    return WINFUNCTYPE(Void,c_void_p)
def _define_GLYPHMETRICSFLOAT_head():
    class GLYPHMETRICSFLOAT(Structure):
        pass
    return GLYPHMETRICSFLOAT
def _define_GLYPHMETRICSFLOAT():
    GLYPHMETRICSFLOAT = win32more.Graphics.OpenGL.GLYPHMETRICSFLOAT_head
    GLYPHMETRICSFLOAT._fields_ = [
        ('gmfBlackBoxX', Single),
        ('gmfBlackBoxY', Single),
        ('gmfptGlyphOrigin', win32more.Graphics.OpenGL.POINTFLOAT),
        ('gmfCellIncX', Single),
        ('gmfCellIncY', Single),
    ]
    return GLYPHMETRICSFLOAT
HGLRC = IntPtr
def _define_LAYERPLANEDESCRIPTOR_head():
    class LAYERPLANEDESCRIPTOR(Structure):
        pass
    return LAYERPLANEDESCRIPTOR
def _define_LAYERPLANEDESCRIPTOR():
    LAYERPLANEDESCRIPTOR = win32more.Graphics.OpenGL.LAYERPLANEDESCRIPTOR_head
    LAYERPLANEDESCRIPTOR._fields_ = [
        ('nSize', UInt16),
        ('nVersion', UInt16),
        ('dwFlags', UInt32),
        ('iPixelType', Byte),
        ('cColorBits', Byte),
        ('cRedBits', Byte),
        ('cRedShift', Byte),
        ('cGreenBits', Byte),
        ('cGreenShift', Byte),
        ('cBlueBits', Byte),
        ('cBlueShift', Byte),
        ('cAlphaBits', Byte),
        ('cAlphaShift', Byte),
        ('cAccumBits', Byte),
        ('cAccumRedBits', Byte),
        ('cAccumGreenBits', Byte),
        ('cAccumBlueBits', Byte),
        ('cAccumAlphaBits', Byte),
        ('cDepthBits', Byte),
        ('cStencilBits', Byte),
        ('cAuxBuffers', Byte),
        ('iLayerPlane', Byte),
        ('bReserved', Byte),
        ('crTransparent', win32more.Foundation.COLORREF),
    ]
    return LAYERPLANEDESCRIPTOR
PFD_FLAGS = UInt32
PFD_DOUBLEBUFFER = 1
PFD_STEREO = 2
PFD_DRAW_TO_WINDOW = 4
PFD_DRAW_TO_BITMAP = 8
PFD_SUPPORT_GDI = 16
PFD_SUPPORT_OPENGL = 32
PFD_GENERIC_FORMAT = 64
PFD_NEED_PALETTE = 128
PFD_NEED_SYSTEM_PALETTE = 256
PFD_SWAP_EXCHANGE = 512
PFD_SWAP_COPY = 1024
PFD_SWAP_LAYER_BUFFERS = 2048
PFD_GENERIC_ACCELERATED = 4096
PFD_SUPPORT_DIRECTDRAW = 8192
PFD_DIRECT3D_ACCELERATED = 16384
PFD_SUPPORT_COMPOSITION = 32768
PFD_DEPTH_DONTCARE = 536870912
PFD_DOUBLEBUFFER_DONTCARE = 1073741824
PFD_STEREO_DONTCARE = 2147483648
PFD_LAYER_TYPE = SByte
PFD_UNDERLAY_PLANE = -1
PFD_MAIN_PLANE = 0
PFD_OVERLAY_PLANE = 1
PFD_PIXEL_TYPE = SByte
PFD_TYPE_RGBA = 0
PFD_TYPE_COLORINDEX = 1
def _define_PFNGLADDSWAPHINTRECTWINPROC():
    return WINFUNCTYPE(Void,Int32,Int32,Int32,Int32)
def _define_PFNGLARRAYELEMENTARRAYEXTPROC():
    return WINFUNCTYPE(Void,UInt32,Int32,c_void_p)
def _define_PFNGLARRAYELEMENTEXTPROC():
    return WINFUNCTYPE(Void,Int32)
def _define_PFNGLCOLORPOINTEREXTPROC():
    return WINFUNCTYPE(Void,Int32,UInt32,Int32,Int32,c_void_p)
def _define_PFNGLCOLORSUBTABLEEXTPROC():
    return WINFUNCTYPE(Void,UInt32,Int32,Int32,UInt32,UInt32,c_void_p)
def _define_PFNGLCOLORTABLEEXTPROC():
    return WINFUNCTYPE(Void,UInt32,UInt32,Int32,UInt32,UInt32,c_void_p)
def _define_PFNGLDRAWARRAYSEXTPROC():
    return WINFUNCTYPE(Void,UInt32,Int32,Int32)
def _define_PFNGLDRAWRANGEELEMENTSWINPROC():
    return WINFUNCTYPE(Void,UInt32,UInt32,UInt32,Int32,UInt32,c_void_p)
def _define_PFNGLEDGEFLAGPOINTEREXTPROC():
    return WINFUNCTYPE(Void,Int32,Int32,c_char_p_no)
def _define_PFNGLGETCOLORTABLEEXTPROC():
    return WINFUNCTYPE(Void,UInt32,UInt32,UInt32,c_void_p)
def _define_PFNGLGETCOLORTABLEPARAMETERFVEXTPROC():
    return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(Single))
def _define_PFNGLGETCOLORTABLEPARAMETERIVEXTPROC():
    return WINFUNCTYPE(Void,UInt32,UInt32,POINTER(Int32))
def _define_PFNGLGETPOINTERVEXTPROC():
    return WINFUNCTYPE(Void,UInt32,POINTER(c_void_p))
def _define_PFNGLINDEXPOINTEREXTPROC():
    return WINFUNCTYPE(Void,UInt32,Int32,Int32,c_void_p)
def _define_PFNGLNORMALPOINTEREXTPROC():
    return WINFUNCTYPE(Void,UInt32,Int32,Int32,c_void_p)
def _define_PFNGLTEXCOORDPOINTEREXTPROC():
    return WINFUNCTYPE(Void,Int32,UInt32,Int32,Int32,c_void_p)
def _define_PFNGLVERTEXPOINTEREXTPROC():
    return WINFUNCTYPE(Void,Int32,UInt32,Int32,Int32,c_void_p)
def _define_PIXELFORMATDESCRIPTOR_head():
    class PIXELFORMATDESCRIPTOR(Structure):
        pass
    return PIXELFORMATDESCRIPTOR
def _define_PIXELFORMATDESCRIPTOR():
    PIXELFORMATDESCRIPTOR = win32more.Graphics.OpenGL.PIXELFORMATDESCRIPTOR_head
    PIXELFORMATDESCRIPTOR._fields_ = [
        ('nSize', UInt16),
        ('nVersion', UInt16),
        ('dwFlags', win32more.Graphics.OpenGL.PFD_FLAGS),
        ('iPixelType', win32more.Graphics.OpenGL.PFD_PIXEL_TYPE),
        ('cColorBits', Byte),
        ('cRedBits', Byte),
        ('cRedShift', Byte),
        ('cGreenBits', Byte),
        ('cGreenShift', Byte),
        ('cBlueBits', Byte),
        ('cBlueShift', Byte),
        ('cAlphaBits', Byte),
        ('cAlphaShift', Byte),
        ('cAccumBits', Byte),
        ('cAccumRedBits', Byte),
        ('cAccumGreenBits', Byte),
        ('cAccumBlueBits', Byte),
        ('cAccumAlphaBits', Byte),
        ('cDepthBits', Byte),
        ('cStencilBits', Byte),
        ('cAuxBuffers', Byte),
        ('iLayerType', win32more.Graphics.OpenGL.PFD_LAYER_TYPE),
        ('bReserved', Byte),
        ('dwLayerMask', UInt32),
        ('dwVisibleMask', UInt32),
        ('dwDamageMask', UInt32),
    ]
    return PIXELFORMATDESCRIPTOR
def _define_POINTFLOAT_head():
    class POINTFLOAT(Structure):
        pass
    return POINTFLOAT
def _define_POINTFLOAT():
    POINTFLOAT = win32more.Graphics.OpenGL.POINTFLOAT_head
    POINTFLOAT._fields_ = [
        ('x', Single),
        ('y', Single),
    ]
    return POINTFLOAT
__all__ = [
    "ChoosePixelFormat",
    "DescribePixelFormat",
    "EMRPIXELFORMAT",
    "GLU_AUTO_LOAD_MATRIX",
    "GLU_BEGIN",
    "GLU_CCW",
    "GLU_CULLING",
    "GLU_CW",
    "GLU_DISPLAY_MODE",
    "GLU_DOMAIN_DISTANCE",
    "GLU_EDGE_FLAG",
    "GLU_END",
    "GLU_ERROR",
    "GLU_EXTENSIONS",
    "GLU_EXTERIOR",
    "GLU_FALSE",
    "GLU_FILL",
    "GLU_FLAT",
    "GLU_INCOMPATIBLE_GL_VERSION",
    "GLU_INSIDE",
    "GLU_INTERIOR",
    "GLU_INVALID_ENUM",
    "GLU_INVALID_VALUE",
    "GLU_LINE",
    "GLU_MAP1_TRIM_2",
    "GLU_MAP1_TRIM_3",
    "GLU_NONE",
    "GLU_NURBS_ERROR1",
    "GLU_NURBS_ERROR10",
    "GLU_NURBS_ERROR11",
    "GLU_NURBS_ERROR12",
    "GLU_NURBS_ERROR13",
    "GLU_NURBS_ERROR14",
    "GLU_NURBS_ERROR15",
    "GLU_NURBS_ERROR16",
    "GLU_NURBS_ERROR17",
    "GLU_NURBS_ERROR18",
    "GLU_NURBS_ERROR19",
    "GLU_NURBS_ERROR2",
    "GLU_NURBS_ERROR20",
    "GLU_NURBS_ERROR21",
    "GLU_NURBS_ERROR22",
    "GLU_NURBS_ERROR23",
    "GLU_NURBS_ERROR24",
    "GLU_NURBS_ERROR25",
    "GLU_NURBS_ERROR26",
    "GLU_NURBS_ERROR27",
    "GLU_NURBS_ERROR28",
    "GLU_NURBS_ERROR29",
    "GLU_NURBS_ERROR3",
    "GLU_NURBS_ERROR30",
    "GLU_NURBS_ERROR31",
    "GLU_NURBS_ERROR32",
    "GLU_NURBS_ERROR33",
    "GLU_NURBS_ERROR34",
    "GLU_NURBS_ERROR35",
    "GLU_NURBS_ERROR36",
    "GLU_NURBS_ERROR37",
    "GLU_NURBS_ERROR4",
    "GLU_NURBS_ERROR5",
    "GLU_NURBS_ERROR6",
    "GLU_NURBS_ERROR7",
    "GLU_NURBS_ERROR8",
    "GLU_NURBS_ERROR9",
    "GLU_OUTLINE_PATCH",
    "GLU_OUTLINE_POLYGON",
    "GLU_OUTSIDE",
    "GLU_OUT_OF_MEMORY",
    "GLU_PARAMETRIC_ERROR",
    "GLU_PARAMETRIC_TOLERANCE",
    "GLU_PATH_LENGTH",
    "GLU_POINT",
    "GLU_SAMPLING_METHOD",
    "GLU_SAMPLING_TOLERANCE",
    "GLU_SILHOUETTE",
    "GLU_SMOOTH",
    "GLU_TESS_BEGIN",
    "GLU_TESS_BEGIN_DATA",
    "GLU_TESS_BOUNDARY_ONLY",
    "GLU_TESS_COMBINE",
    "GLU_TESS_COMBINE_DATA",
    "GLU_TESS_COORD_TOO_LARGE",
    "GLU_TESS_EDGE_FLAG",
    "GLU_TESS_EDGE_FLAG_DATA",
    "GLU_TESS_END",
    "GLU_TESS_END_DATA",
    "GLU_TESS_ERROR",
    "GLU_TESS_ERROR1",
    "GLU_TESS_ERROR2",
    "GLU_TESS_ERROR3",
    "GLU_TESS_ERROR4",
    "GLU_TESS_ERROR5",
    "GLU_TESS_ERROR6",
    "GLU_TESS_ERROR7",
    "GLU_TESS_ERROR8",
    "GLU_TESS_ERROR_DATA",
    "GLU_TESS_MISSING_BEGIN_CONTOUR",
    "GLU_TESS_MISSING_BEGIN_POLYGON",
    "GLU_TESS_MISSING_END_CONTOUR",
    "GLU_TESS_MISSING_END_POLYGON",
    "GLU_TESS_NEED_COMBINE_CALLBACK",
    "GLU_TESS_TOLERANCE",
    "GLU_TESS_VERTEX",
    "GLU_TESS_VERTEX_DATA",
    "GLU_TESS_WINDING_ABS_GEQ_TWO",
    "GLU_TESS_WINDING_NEGATIVE",
    "GLU_TESS_WINDING_NONZERO",
    "GLU_TESS_WINDING_ODD",
    "GLU_TESS_WINDING_POSITIVE",
    "GLU_TESS_WINDING_RULE",
    "GLU_TRUE",
    "GLU_UNKNOWN",
    "GLU_U_STEP",
    "GLU_VERSION",
    "GLU_VERSION_1_1",
    "GLU_VERSION_1_2",
    "GLU_VERTEX",
    "GLU_V_STEP",
    "GLUnurbs",
    "GLUnurbsErrorProc",
    "GLUquadric",
    "GLUquadricErrorProc",
    "GLUtessBeginDataProc",
    "GLUtessBeginProc",
    "GLUtessCombineDataProc",
    "GLUtessCombineProc",
    "GLUtessEdgeFlagDataProc",
    "GLUtessEdgeFlagProc",
    "GLUtessEndDataProc",
    "GLUtessEndProc",
    "GLUtessErrorDataProc",
    "GLUtessErrorProc",
    "GLUtessVertexDataProc",
    "GLUtessVertexProc",
    "GLUtesselator",
    "GLYPHMETRICSFLOAT",
    "GL_2D",
    "GL_2_BYTES",
    "GL_3D",
    "GL_3D_COLOR",
    "GL_3D_COLOR_TEXTURE",
    "GL_3_BYTES",
    "GL_4D_COLOR_TEXTURE",
    "GL_4_BYTES",
    "GL_ACCUM",
    "GL_ACCUM_ALPHA_BITS",
    "GL_ACCUM_BLUE_BITS",
    "GL_ACCUM_BUFFER_BIT",
    "GL_ACCUM_CLEAR_VALUE",
    "GL_ACCUM_GREEN_BITS",
    "GL_ACCUM_RED_BITS",
    "GL_ADD",
    "GL_ALL_ATTRIB_BITS",
    "GL_ALPHA",
    "GL_ALPHA12",
    "GL_ALPHA16",
    "GL_ALPHA4",
    "GL_ALPHA8",
    "GL_ALPHA_BIAS",
    "GL_ALPHA_BITS",
    "GL_ALPHA_SCALE",
    "GL_ALPHA_TEST",
    "GL_ALPHA_TEST_FUNC",
    "GL_ALPHA_TEST_REF",
    "GL_ALWAYS",
    "GL_AMBIENT",
    "GL_AMBIENT_AND_DIFFUSE",
    "GL_AND",
    "GL_AND_INVERTED",
    "GL_AND_REVERSE",
    "GL_ATTRIB_STACK_DEPTH",
    "GL_AUTO_NORMAL",
    "GL_AUX0",
    "GL_AUX1",
    "GL_AUX2",
    "GL_AUX3",
    "GL_AUX_BUFFERS",
    "GL_BACK",
    "GL_BACK_LEFT",
    "GL_BACK_RIGHT",
    "GL_BGRA_EXT",
    "GL_BGR_EXT",
    "GL_BITMAP",
    "GL_BITMAP_TOKEN",
    "GL_BLEND",
    "GL_BLEND_DST",
    "GL_BLEND_SRC",
    "GL_BLUE",
    "GL_BLUE_BIAS",
    "GL_BLUE_BITS",
    "GL_BLUE_SCALE",
    "GL_BYTE",
    "GL_C3F_V3F",
    "GL_C4F_N3F_V3F",
    "GL_C4UB_V2F",
    "GL_C4UB_V3F",
    "GL_CCW",
    "GL_CLAMP",
    "GL_CLEAR",
    "GL_CLIENT_ALL_ATTRIB_BITS",
    "GL_CLIENT_ATTRIB_STACK_DEPTH",
    "GL_CLIENT_PIXEL_STORE_BIT",
    "GL_CLIENT_VERTEX_ARRAY_BIT",
    "GL_CLIP_PLANE0",
    "GL_CLIP_PLANE1",
    "GL_CLIP_PLANE2",
    "GL_CLIP_PLANE3",
    "GL_CLIP_PLANE4",
    "GL_CLIP_PLANE5",
    "GL_COEFF",
    "GL_COLOR",
    "GL_COLOR_ARRAY",
    "GL_COLOR_ARRAY_COUNT_EXT",
    "GL_COLOR_ARRAY_EXT",
    "GL_COLOR_ARRAY_POINTER",
    "GL_COLOR_ARRAY_POINTER_EXT",
    "GL_COLOR_ARRAY_SIZE",
    "GL_COLOR_ARRAY_SIZE_EXT",
    "GL_COLOR_ARRAY_STRIDE",
    "GL_COLOR_ARRAY_STRIDE_EXT",
    "GL_COLOR_ARRAY_TYPE",
    "GL_COLOR_ARRAY_TYPE_EXT",
    "GL_COLOR_BUFFER_BIT",
    "GL_COLOR_CLEAR_VALUE",
    "GL_COLOR_INDEX",
    "GL_COLOR_INDEX12_EXT",
    "GL_COLOR_INDEX16_EXT",
    "GL_COLOR_INDEX1_EXT",
    "GL_COLOR_INDEX2_EXT",
    "GL_COLOR_INDEX4_EXT",
    "GL_COLOR_INDEX8_EXT",
    "GL_COLOR_INDEXES",
    "GL_COLOR_LOGIC_OP",
    "GL_COLOR_MATERIAL",
    "GL_COLOR_MATERIAL_FACE",
    "GL_COLOR_MATERIAL_PARAMETER",
    "GL_COLOR_TABLE_ALPHA_SIZE_EXT",
    "GL_COLOR_TABLE_BLUE_SIZE_EXT",
    "GL_COLOR_TABLE_FORMAT_EXT",
    "GL_COLOR_TABLE_GREEN_SIZE_EXT",
    "GL_COLOR_TABLE_INTENSITY_SIZE_EXT",
    "GL_COLOR_TABLE_LUMINANCE_SIZE_EXT",
    "GL_COLOR_TABLE_RED_SIZE_EXT",
    "GL_COLOR_TABLE_WIDTH_EXT",
    "GL_COLOR_WRITEMASK",
    "GL_COMPILE",
    "GL_COMPILE_AND_EXECUTE",
    "GL_CONSTANT_ATTENUATION",
    "GL_COPY",
    "GL_COPY_INVERTED",
    "GL_COPY_PIXEL_TOKEN",
    "GL_CULL_FACE",
    "GL_CULL_FACE_MODE",
    "GL_CURRENT_BIT",
    "GL_CURRENT_COLOR",
    "GL_CURRENT_INDEX",
    "GL_CURRENT_NORMAL",
    "GL_CURRENT_RASTER_COLOR",
    "GL_CURRENT_RASTER_DISTANCE",
    "GL_CURRENT_RASTER_INDEX",
    "GL_CURRENT_RASTER_POSITION",
    "GL_CURRENT_RASTER_POSITION_VALID",
    "GL_CURRENT_RASTER_TEXTURE_COORDS",
    "GL_CURRENT_TEXTURE_COORDS",
    "GL_CW",
    "GL_DECAL",
    "GL_DECR",
    "GL_DEPTH",
    "GL_DEPTH_BIAS",
    "GL_DEPTH_BITS",
    "GL_DEPTH_BUFFER_BIT",
    "GL_DEPTH_CLEAR_VALUE",
    "GL_DEPTH_COMPONENT",
    "GL_DEPTH_FUNC",
    "GL_DEPTH_RANGE",
    "GL_DEPTH_SCALE",
    "GL_DEPTH_TEST",
    "GL_DEPTH_WRITEMASK",
    "GL_DIFFUSE",
    "GL_DITHER",
    "GL_DOMAIN",
    "GL_DONT_CARE",
    "GL_DOUBLE",
    "GL_DOUBLEBUFFER",
    "GL_DOUBLE_EXT",
    "GL_DRAW_BUFFER",
    "GL_DRAW_PIXEL_TOKEN",
    "GL_DST_ALPHA",
    "GL_DST_COLOR",
    "GL_EDGE_FLAG",
    "GL_EDGE_FLAG_ARRAY",
    "GL_EDGE_FLAG_ARRAY_COUNT_EXT",
    "GL_EDGE_FLAG_ARRAY_EXT",
    "GL_EDGE_FLAG_ARRAY_POINTER",
    "GL_EDGE_FLAG_ARRAY_POINTER_EXT",
    "GL_EDGE_FLAG_ARRAY_STRIDE",
    "GL_EDGE_FLAG_ARRAY_STRIDE_EXT",
    "GL_EMISSION",
    "GL_ENABLE_BIT",
    "GL_EQUAL",
    "GL_EQUIV",
    "GL_EVAL_BIT",
    "GL_EXP",
    "GL_EXP2",
    "GL_EXTENSIONS",
    "GL_EXT_bgra",
    "GL_EXT_paletted_texture",
    "GL_EXT_vertex_array",
    "GL_EYE_LINEAR",
    "GL_EYE_PLANE",
    "GL_FALSE",
    "GL_FASTEST",
    "GL_FEEDBACK",
    "GL_FEEDBACK_BUFFER_POINTER",
    "GL_FEEDBACK_BUFFER_SIZE",
    "GL_FEEDBACK_BUFFER_TYPE",
    "GL_FILL",
    "GL_FLAT",
    "GL_FLOAT",
    "GL_FOG",
    "GL_FOG_BIT",
    "GL_FOG_COLOR",
    "GL_FOG_DENSITY",
    "GL_FOG_END",
    "GL_FOG_HINT",
    "GL_FOG_INDEX",
    "GL_FOG_MODE",
    "GL_FOG_SPECULAR_TEXTURE_WIN",
    "GL_FOG_START",
    "GL_FRONT",
    "GL_FRONT_AND_BACK",
    "GL_FRONT_FACE",
    "GL_FRONT_LEFT",
    "GL_FRONT_RIGHT",
    "GL_GEQUAL",
    "GL_GREATER",
    "GL_GREEN",
    "GL_GREEN_BIAS",
    "GL_GREEN_BITS",
    "GL_GREEN_SCALE",
    "GL_HINT_BIT",
    "GL_INCR",
    "GL_INDEX_ARRAY",
    "GL_INDEX_ARRAY_COUNT_EXT",
    "GL_INDEX_ARRAY_EXT",
    "GL_INDEX_ARRAY_POINTER",
    "GL_INDEX_ARRAY_POINTER_EXT",
    "GL_INDEX_ARRAY_STRIDE",
    "GL_INDEX_ARRAY_STRIDE_EXT",
    "GL_INDEX_ARRAY_TYPE",
    "GL_INDEX_ARRAY_TYPE_EXT",
    "GL_INDEX_BITS",
    "GL_INDEX_CLEAR_VALUE",
    "GL_INDEX_LOGIC_OP",
    "GL_INDEX_MODE",
    "GL_INDEX_OFFSET",
    "GL_INDEX_SHIFT",
    "GL_INDEX_WRITEMASK",
    "GL_INT",
    "GL_INTENSITY",
    "GL_INTENSITY12",
    "GL_INTENSITY16",
    "GL_INTENSITY4",
    "GL_INTENSITY8",
    "GL_INVALID_ENUM",
    "GL_INVALID_OPERATION",
    "GL_INVALID_VALUE",
    "GL_INVERT",
    "GL_KEEP",
    "GL_LEFT",
    "GL_LEQUAL",
    "GL_LESS",
    "GL_LIGHT0",
    "GL_LIGHT1",
    "GL_LIGHT2",
    "GL_LIGHT3",
    "GL_LIGHT4",
    "GL_LIGHT5",
    "GL_LIGHT6",
    "GL_LIGHT7",
    "GL_LIGHTING",
    "GL_LIGHTING_BIT",
    "GL_LIGHT_MODEL_AMBIENT",
    "GL_LIGHT_MODEL_LOCAL_VIEWER",
    "GL_LIGHT_MODEL_TWO_SIDE",
    "GL_LINE",
    "GL_LINEAR",
    "GL_LINEAR_ATTENUATION",
    "GL_LINEAR_MIPMAP_LINEAR",
    "GL_LINEAR_MIPMAP_NEAREST",
    "GL_LINES",
    "GL_LINE_BIT",
    "GL_LINE_LOOP",
    "GL_LINE_RESET_TOKEN",
    "GL_LINE_SMOOTH",
    "GL_LINE_SMOOTH_HINT",
    "GL_LINE_STIPPLE",
    "GL_LINE_STIPPLE_PATTERN",
    "GL_LINE_STIPPLE_REPEAT",
    "GL_LINE_STRIP",
    "GL_LINE_TOKEN",
    "GL_LINE_WIDTH",
    "GL_LINE_WIDTH_GRANULARITY",
    "GL_LINE_WIDTH_RANGE",
    "GL_LIST_BASE",
    "GL_LIST_BIT",
    "GL_LIST_INDEX",
    "GL_LIST_MODE",
    "GL_LOAD",
    "GL_LOGIC_OP",
    "GL_LOGIC_OP_MODE",
    "GL_LUMINANCE",
    "GL_LUMINANCE12",
    "GL_LUMINANCE12_ALPHA12",
    "GL_LUMINANCE12_ALPHA4",
    "GL_LUMINANCE16",
    "GL_LUMINANCE16_ALPHA16",
    "GL_LUMINANCE4",
    "GL_LUMINANCE4_ALPHA4",
    "GL_LUMINANCE6_ALPHA2",
    "GL_LUMINANCE8",
    "GL_LUMINANCE8_ALPHA8",
    "GL_LUMINANCE_ALPHA",
    "GL_MAP1_COLOR_4",
    "GL_MAP1_GRID_DOMAIN",
    "GL_MAP1_GRID_SEGMENTS",
    "GL_MAP1_INDEX",
    "GL_MAP1_NORMAL",
    "GL_MAP1_TEXTURE_COORD_1",
    "GL_MAP1_TEXTURE_COORD_2",
    "GL_MAP1_TEXTURE_COORD_3",
    "GL_MAP1_TEXTURE_COORD_4",
    "GL_MAP1_VERTEX_3",
    "GL_MAP1_VERTEX_4",
    "GL_MAP2_COLOR_4",
    "GL_MAP2_GRID_DOMAIN",
    "GL_MAP2_GRID_SEGMENTS",
    "GL_MAP2_INDEX",
    "GL_MAP2_NORMAL",
    "GL_MAP2_TEXTURE_COORD_1",
    "GL_MAP2_TEXTURE_COORD_2",
    "GL_MAP2_TEXTURE_COORD_3",
    "GL_MAP2_TEXTURE_COORD_4",
    "GL_MAP2_VERTEX_3",
    "GL_MAP2_VERTEX_4",
    "GL_MAP_COLOR",
    "GL_MAP_STENCIL",
    "GL_MATRIX_MODE",
    "GL_MAX_ATTRIB_STACK_DEPTH",
    "GL_MAX_CLIENT_ATTRIB_STACK_DEPTH",
    "GL_MAX_CLIP_PLANES",
    "GL_MAX_ELEMENTS_INDICES_WIN",
    "GL_MAX_ELEMENTS_VERTICES_WIN",
    "GL_MAX_EVAL_ORDER",
    "GL_MAX_LIGHTS",
    "GL_MAX_LIST_NESTING",
    "GL_MAX_MODELVIEW_STACK_DEPTH",
    "GL_MAX_NAME_STACK_DEPTH",
    "GL_MAX_PIXEL_MAP_TABLE",
    "GL_MAX_PROJECTION_STACK_DEPTH",
    "GL_MAX_TEXTURE_SIZE",
    "GL_MAX_TEXTURE_STACK_DEPTH",
    "GL_MAX_VIEWPORT_DIMS",
    "GL_MODELVIEW",
    "GL_MODELVIEW_MATRIX",
    "GL_MODELVIEW_STACK_DEPTH",
    "GL_MODULATE",
    "GL_MULT",
    "GL_N3F_V3F",
    "GL_NAME_STACK_DEPTH",
    "GL_NAND",
    "GL_NEAREST",
    "GL_NEAREST_MIPMAP_LINEAR",
    "GL_NEAREST_MIPMAP_NEAREST",
    "GL_NEVER",
    "GL_NICEST",
    "GL_NONE",
    "GL_NOOP",
    "GL_NOR",
    "GL_NORMALIZE",
    "GL_NORMAL_ARRAY",
    "GL_NORMAL_ARRAY_COUNT_EXT",
    "GL_NORMAL_ARRAY_EXT",
    "GL_NORMAL_ARRAY_POINTER",
    "GL_NORMAL_ARRAY_POINTER_EXT",
    "GL_NORMAL_ARRAY_STRIDE",
    "GL_NORMAL_ARRAY_STRIDE_EXT",
    "GL_NORMAL_ARRAY_TYPE",
    "GL_NORMAL_ARRAY_TYPE_EXT",
    "GL_NOTEQUAL",
    "GL_NO_ERROR",
    "GL_OBJECT_LINEAR",
    "GL_OBJECT_PLANE",
    "GL_ONE",
    "GL_ONE_MINUS_DST_ALPHA",
    "GL_ONE_MINUS_DST_COLOR",
    "GL_ONE_MINUS_SRC_ALPHA",
    "GL_ONE_MINUS_SRC_COLOR",
    "GL_OR",
    "GL_ORDER",
    "GL_OR_INVERTED",
    "GL_OR_REVERSE",
    "GL_OUT_OF_MEMORY",
    "GL_PACK_ALIGNMENT",
    "GL_PACK_LSB_FIRST",
    "GL_PACK_ROW_LENGTH",
    "GL_PACK_SKIP_PIXELS",
    "GL_PACK_SKIP_ROWS",
    "GL_PACK_SWAP_BYTES",
    "GL_PASS_THROUGH_TOKEN",
    "GL_PERSPECTIVE_CORRECTION_HINT",
    "GL_PHONG_HINT_WIN",
    "GL_PHONG_WIN",
    "GL_PIXEL_MAP_A_TO_A",
    "GL_PIXEL_MAP_A_TO_A_SIZE",
    "GL_PIXEL_MAP_B_TO_B",
    "GL_PIXEL_MAP_B_TO_B_SIZE",
    "GL_PIXEL_MAP_G_TO_G",
    "GL_PIXEL_MAP_G_TO_G_SIZE",
    "GL_PIXEL_MAP_I_TO_A",
    "GL_PIXEL_MAP_I_TO_A_SIZE",
    "GL_PIXEL_MAP_I_TO_B",
    "GL_PIXEL_MAP_I_TO_B_SIZE",
    "GL_PIXEL_MAP_I_TO_G",
    "GL_PIXEL_MAP_I_TO_G_SIZE",
    "GL_PIXEL_MAP_I_TO_I",
    "GL_PIXEL_MAP_I_TO_I_SIZE",
    "GL_PIXEL_MAP_I_TO_R",
    "GL_PIXEL_MAP_I_TO_R_SIZE",
    "GL_PIXEL_MAP_R_TO_R",
    "GL_PIXEL_MAP_R_TO_R_SIZE",
    "GL_PIXEL_MAP_S_TO_S",
    "GL_PIXEL_MAP_S_TO_S_SIZE",
    "GL_PIXEL_MODE_BIT",
    "GL_POINT",
    "GL_POINTS",
    "GL_POINT_BIT",
    "GL_POINT_SIZE",
    "GL_POINT_SIZE_GRANULARITY",
    "GL_POINT_SIZE_RANGE",
    "GL_POINT_SMOOTH",
    "GL_POINT_SMOOTH_HINT",
    "GL_POINT_TOKEN",
    "GL_POLYGON",
    "GL_POLYGON_BIT",
    "GL_POLYGON_MODE",
    "GL_POLYGON_OFFSET_FACTOR",
    "GL_POLYGON_OFFSET_FILL",
    "GL_POLYGON_OFFSET_LINE",
    "GL_POLYGON_OFFSET_POINT",
    "GL_POLYGON_OFFSET_UNITS",
    "GL_POLYGON_SMOOTH",
    "GL_POLYGON_SMOOTH_HINT",
    "GL_POLYGON_STIPPLE",
    "GL_POLYGON_STIPPLE_BIT",
    "GL_POLYGON_TOKEN",
    "GL_POSITION",
    "GL_PROJECTION",
    "GL_PROJECTION_MATRIX",
    "GL_PROJECTION_STACK_DEPTH",
    "GL_PROXY_TEXTURE_1D",
    "GL_PROXY_TEXTURE_2D",
    "GL_Q",
    "GL_QUADRATIC_ATTENUATION",
    "GL_QUADS",
    "GL_QUAD_STRIP",
    "GL_R",
    "GL_R3_G3_B2",
    "GL_READ_BUFFER",
    "GL_RED",
    "GL_RED_BIAS",
    "GL_RED_BITS",
    "GL_RED_SCALE",
    "GL_RENDER",
    "GL_RENDERER",
    "GL_RENDER_MODE",
    "GL_REPEAT",
    "GL_REPLACE",
    "GL_RETURN",
    "GL_RGB",
    "GL_RGB10",
    "GL_RGB10_A2",
    "GL_RGB12",
    "GL_RGB16",
    "GL_RGB4",
    "GL_RGB5",
    "GL_RGB5_A1",
    "GL_RGB8",
    "GL_RGBA",
    "GL_RGBA12",
    "GL_RGBA16",
    "GL_RGBA2",
    "GL_RGBA4",
    "GL_RGBA8",
    "GL_RGBA_MODE",
    "GL_RIGHT",
    "GL_S",
    "GL_SCISSOR_BIT",
    "GL_SCISSOR_BOX",
    "GL_SCISSOR_TEST",
    "GL_SELECT",
    "GL_SELECTION_BUFFER_POINTER",
    "GL_SELECTION_BUFFER_SIZE",
    "GL_SET",
    "GL_SHADE_MODEL",
    "GL_SHININESS",
    "GL_SHORT",
    "GL_SMOOTH",
    "GL_SPECULAR",
    "GL_SPHERE_MAP",
    "GL_SPOT_CUTOFF",
    "GL_SPOT_DIRECTION",
    "GL_SPOT_EXPONENT",
    "GL_SRC_ALPHA",
    "GL_SRC_ALPHA_SATURATE",
    "GL_SRC_COLOR",
    "GL_STACK_OVERFLOW",
    "GL_STACK_UNDERFLOW",
    "GL_STENCIL",
    "GL_STENCIL_BITS",
    "GL_STENCIL_BUFFER_BIT",
    "GL_STENCIL_CLEAR_VALUE",
    "GL_STENCIL_FAIL",
    "GL_STENCIL_FUNC",
    "GL_STENCIL_INDEX",
    "GL_STENCIL_PASS_DEPTH_FAIL",
    "GL_STENCIL_PASS_DEPTH_PASS",
    "GL_STENCIL_REF",
    "GL_STENCIL_TEST",
    "GL_STENCIL_VALUE_MASK",
    "GL_STENCIL_WRITEMASK",
    "GL_STEREO",
    "GL_SUBPIXEL_BITS",
    "GL_T",
    "GL_T2F_C3F_V3F",
    "GL_T2F_C4F_N3F_V3F",
    "GL_T2F_C4UB_V3F",
    "GL_T2F_N3F_V3F",
    "GL_T2F_V3F",
    "GL_T4F_C4F_N3F_V4F",
    "GL_T4F_V4F",
    "GL_TEXTURE",
    "GL_TEXTURE_1D",
    "GL_TEXTURE_2D",
    "GL_TEXTURE_ALPHA_SIZE",
    "GL_TEXTURE_BINDING_1D",
    "GL_TEXTURE_BINDING_2D",
    "GL_TEXTURE_BIT",
    "GL_TEXTURE_BLUE_SIZE",
    "GL_TEXTURE_BORDER",
    "GL_TEXTURE_BORDER_COLOR",
    "GL_TEXTURE_COMPONENTS",
    "GL_TEXTURE_COORD_ARRAY",
    "GL_TEXTURE_COORD_ARRAY_COUNT_EXT",
    "GL_TEXTURE_COORD_ARRAY_EXT",
    "GL_TEXTURE_COORD_ARRAY_POINTER",
    "GL_TEXTURE_COORD_ARRAY_POINTER_EXT",
    "GL_TEXTURE_COORD_ARRAY_SIZE",
    "GL_TEXTURE_COORD_ARRAY_SIZE_EXT",
    "GL_TEXTURE_COORD_ARRAY_STRIDE",
    "GL_TEXTURE_COORD_ARRAY_STRIDE_EXT",
    "GL_TEXTURE_COORD_ARRAY_TYPE",
    "GL_TEXTURE_COORD_ARRAY_TYPE_EXT",
    "GL_TEXTURE_ENV",
    "GL_TEXTURE_ENV_COLOR",
    "GL_TEXTURE_ENV_MODE",
    "GL_TEXTURE_GEN_MODE",
    "GL_TEXTURE_GEN_Q",
    "GL_TEXTURE_GEN_R",
    "GL_TEXTURE_GEN_S",
    "GL_TEXTURE_GEN_T",
    "GL_TEXTURE_GREEN_SIZE",
    "GL_TEXTURE_HEIGHT",
    "GL_TEXTURE_INTENSITY_SIZE",
    "GL_TEXTURE_INTERNAL_FORMAT",
    "GL_TEXTURE_LUMINANCE_SIZE",
    "GL_TEXTURE_MAG_FILTER",
    "GL_TEXTURE_MATRIX",
    "GL_TEXTURE_MIN_FILTER",
    "GL_TEXTURE_PRIORITY",
    "GL_TEXTURE_RED_SIZE",
    "GL_TEXTURE_RESIDENT",
    "GL_TEXTURE_STACK_DEPTH",
    "GL_TEXTURE_WIDTH",
    "GL_TEXTURE_WRAP_S",
    "GL_TEXTURE_WRAP_T",
    "GL_TRANSFORM_BIT",
    "GL_TRIANGLES",
    "GL_TRIANGLE_FAN",
    "GL_TRIANGLE_STRIP",
    "GL_TRUE",
    "GL_UNPACK_ALIGNMENT",
    "GL_UNPACK_LSB_FIRST",
    "GL_UNPACK_ROW_LENGTH",
    "GL_UNPACK_SKIP_PIXELS",
    "GL_UNPACK_SKIP_ROWS",
    "GL_UNPACK_SWAP_BYTES",
    "GL_UNSIGNED_BYTE",
    "GL_UNSIGNED_INT",
    "GL_UNSIGNED_SHORT",
    "GL_V2F",
    "GL_V3F",
    "GL_VENDOR",
    "GL_VERSION",
    "GL_VERSION_1_1",
    "GL_VERTEX_ARRAY",
    "GL_VERTEX_ARRAY_COUNT_EXT",
    "GL_VERTEX_ARRAY_EXT",
    "GL_VERTEX_ARRAY_POINTER",
    "GL_VERTEX_ARRAY_POINTER_EXT",
    "GL_VERTEX_ARRAY_SIZE",
    "GL_VERTEX_ARRAY_SIZE_EXT",
    "GL_VERTEX_ARRAY_STRIDE",
    "GL_VERTEX_ARRAY_STRIDE_EXT",
    "GL_VERTEX_ARRAY_TYPE",
    "GL_VERTEX_ARRAY_TYPE_EXT",
    "GL_VIEWPORT",
    "GL_VIEWPORT_BIT",
    "GL_WIN_draw_range_elements",
    "GL_WIN_swap_hint",
    "GL_XOR",
    "GL_ZERO",
    "GL_ZOOM_X",
    "GL_ZOOM_Y",
    "GetEnhMetaFilePixelFormat",
    "GetPixelFormat",
    "HGLRC",
    "LAYERPLANEDESCRIPTOR",
    "PFD_DEPTH_DONTCARE",
    "PFD_DIRECT3D_ACCELERATED",
    "PFD_DOUBLEBUFFER",
    "PFD_DOUBLEBUFFER_DONTCARE",
    "PFD_DRAW_TO_BITMAP",
    "PFD_DRAW_TO_WINDOW",
    "PFD_FLAGS",
    "PFD_GENERIC_ACCELERATED",
    "PFD_GENERIC_FORMAT",
    "PFD_LAYER_TYPE",
    "PFD_MAIN_PLANE",
    "PFD_NEED_PALETTE",
    "PFD_NEED_SYSTEM_PALETTE",
    "PFD_OVERLAY_PLANE",
    "PFD_PIXEL_TYPE",
    "PFD_STEREO",
    "PFD_STEREO_DONTCARE",
    "PFD_SUPPORT_COMPOSITION",
    "PFD_SUPPORT_DIRECTDRAW",
    "PFD_SUPPORT_GDI",
    "PFD_SUPPORT_OPENGL",
    "PFD_SWAP_COPY",
    "PFD_SWAP_EXCHANGE",
    "PFD_SWAP_LAYER_BUFFERS",
    "PFD_TYPE_COLORINDEX",
    "PFD_TYPE_RGBA",
    "PFD_UNDERLAY_PLANE",
    "PFNGLADDSWAPHINTRECTWINPROC",
    "PFNGLARRAYELEMENTARRAYEXTPROC",
    "PFNGLARRAYELEMENTEXTPROC",
    "PFNGLCOLORPOINTEREXTPROC",
    "PFNGLCOLORSUBTABLEEXTPROC",
    "PFNGLCOLORTABLEEXTPROC",
    "PFNGLDRAWARRAYSEXTPROC",
    "PFNGLDRAWRANGEELEMENTSWINPROC",
    "PFNGLEDGEFLAGPOINTEREXTPROC",
    "PFNGLGETCOLORTABLEEXTPROC",
    "PFNGLGETCOLORTABLEPARAMETERFVEXTPROC",
    "PFNGLGETCOLORTABLEPARAMETERIVEXTPROC",
    "PFNGLGETPOINTERVEXTPROC",
    "PFNGLINDEXPOINTEREXTPROC",
    "PFNGLNORMALPOINTEREXTPROC",
    "PFNGLTEXCOORDPOINTEREXTPROC",
    "PFNGLVERTEXPOINTEREXTPROC",
    "PIXELFORMATDESCRIPTOR",
    "POINTFLOAT",
    "SetPixelFormat",
    "SwapBuffers",
    "glAccum",
    "glAlphaFunc",
    "glAreTexturesResident",
    "glArrayElement",
    "glBegin",
    "glBindTexture",
    "glBitmap",
    "glBlendFunc",
    "glCallList",
    "glCallLists",
    "glClear",
    "glClearAccum",
    "glClearColor",
    "glClearDepth",
    "glClearIndex",
    "glClearStencil",
    "glClipPlane",
    "glColor3b",
    "glColor3bv",
    "glColor3d",
    "glColor3dv",
    "glColor3f",
    "glColor3fv",
    "glColor3i",
    "glColor3iv",
    "glColor3s",
    "glColor3sv",
    "glColor3ub",
    "glColor3ubv",
    "glColor3ui",
    "glColor3uiv",
    "glColor3us",
    "glColor3usv",
    "glColor4b",
    "glColor4bv",
    "glColor4d",
    "glColor4dv",
    "glColor4f",
    "glColor4fv",
    "glColor4i",
    "glColor4iv",
    "glColor4s",
    "glColor4sv",
    "glColor4ub",
    "glColor4ubv",
    "glColor4ui",
    "glColor4uiv",
    "glColor4us",
    "glColor4usv",
    "glColorMask",
    "glColorMaterial",
    "glColorPointer",
    "glCopyPixels",
    "glCopyTexImage1D",
    "glCopyTexImage2D",
    "glCopyTexSubImage1D",
    "glCopyTexSubImage2D",
    "glCullFace",
    "glDeleteLists",
    "glDeleteTextures",
    "glDepthFunc",
    "glDepthMask",
    "glDepthRange",
    "glDisable",
    "glDisableClientState",
    "glDrawArrays",
    "glDrawBuffer",
    "glDrawElements",
    "glDrawPixels",
    "glEdgeFlag",
    "glEdgeFlagPointer",
    "glEdgeFlagv",
    "glEnable",
    "glEnableClientState",
    "glEnd",
    "glEndList",
    "glEvalCoord1d",
    "glEvalCoord1dv",
    "glEvalCoord1f",
    "glEvalCoord1fv",
    "glEvalCoord2d",
    "glEvalCoord2dv",
    "glEvalCoord2f",
    "glEvalCoord2fv",
    "glEvalMesh1",
    "glEvalMesh2",
    "glEvalPoint1",
    "glEvalPoint2",
    "glFeedbackBuffer",
    "glFinish",
    "glFlush",
    "glFogf",
    "glFogfv",
    "glFogi",
    "glFogiv",
    "glFrontFace",
    "glFrustum",
    "glGenLists",
    "glGenTextures",
    "glGetBooleanv",
    "glGetClipPlane",
    "glGetDoublev",
    "glGetError",
    "glGetFloatv",
    "glGetIntegerv",
    "glGetLightfv",
    "glGetLightiv",
    "glGetMapdv",
    "glGetMapfv",
    "glGetMapiv",
    "glGetMaterialfv",
    "glGetMaterialiv",
    "glGetPixelMapfv",
    "glGetPixelMapuiv",
    "glGetPixelMapusv",
    "glGetPointerv",
    "glGetPolygonStipple",
    "glGetString",
    "glGetTexEnvfv",
    "glGetTexEnviv",
    "glGetTexGendv",
    "glGetTexGenfv",
    "glGetTexGeniv",
    "glGetTexImage",
    "glGetTexLevelParameterfv",
    "glGetTexLevelParameteriv",
    "glGetTexParameterfv",
    "glGetTexParameteriv",
    "glHint",
    "glIndexMask",
    "glIndexPointer",
    "glIndexd",
    "glIndexdv",
    "glIndexf",
    "glIndexfv",
    "glIndexi",
    "glIndexiv",
    "glIndexs",
    "glIndexsv",
    "glIndexub",
    "glIndexubv",
    "glInitNames",
    "glInterleavedArrays",
    "glIsEnabled",
    "glIsList",
    "glIsTexture",
    "glLightModelf",
    "glLightModelfv",
    "glLightModeli",
    "glLightModeliv",
    "glLightf",
    "glLightfv",
    "glLighti",
    "glLightiv",
    "glLineStipple",
    "glLineWidth",
    "glListBase",
    "glLoadIdentity",
    "glLoadMatrixd",
    "glLoadMatrixf",
    "glLoadName",
    "glLogicOp",
    "glMap1d",
    "glMap1f",
    "glMap2d",
    "glMap2f",
    "glMapGrid1d",
    "glMapGrid1f",
    "glMapGrid2d",
    "glMapGrid2f",
    "glMaterialf",
    "glMaterialfv",
    "glMateriali",
    "glMaterialiv",
    "glMatrixMode",
    "glMultMatrixd",
    "glMultMatrixf",
    "glNewList",
    "glNormal3b",
    "glNormal3bv",
    "glNormal3d",
    "glNormal3dv",
    "glNormal3f",
    "glNormal3fv",
    "glNormal3i",
    "glNormal3iv",
    "glNormal3s",
    "glNormal3sv",
    "glNormalPointer",
    "glOrtho",
    "glPassThrough",
    "glPixelMapfv",
    "glPixelMapuiv",
    "glPixelMapusv",
    "glPixelStoref",
    "glPixelStorei",
    "glPixelTransferf",
    "glPixelTransferi",
    "glPixelZoom",
    "glPointSize",
    "glPolygonMode",
    "glPolygonOffset",
    "glPolygonStipple",
    "glPopAttrib",
    "glPopClientAttrib",
    "glPopMatrix",
    "glPopName",
    "glPrioritizeTextures",
    "glPushAttrib",
    "glPushClientAttrib",
    "glPushMatrix",
    "glPushName",
    "glRasterPos2d",
    "glRasterPos2dv",
    "glRasterPos2f",
    "glRasterPos2fv",
    "glRasterPos2i",
    "glRasterPos2iv",
    "glRasterPos2s",
    "glRasterPos2sv",
    "glRasterPos3d",
    "glRasterPos3dv",
    "glRasterPos3f",
    "glRasterPos3fv",
    "glRasterPos3i",
    "glRasterPos3iv",
    "glRasterPos3s",
    "glRasterPos3sv",
    "glRasterPos4d",
    "glRasterPos4dv",
    "glRasterPos4f",
    "glRasterPos4fv",
    "glRasterPos4i",
    "glRasterPos4iv",
    "glRasterPos4s",
    "glRasterPos4sv",
    "glReadBuffer",
    "glReadPixels",
    "glRectd",
    "glRectdv",
    "glRectf",
    "glRectfv",
    "glRecti",
    "glRectiv",
    "glRects",
    "glRectsv",
    "glRenderMode",
    "glRotated",
    "glRotatef",
    "glScaled",
    "glScalef",
    "glScissor",
    "glSelectBuffer",
    "glShadeModel",
    "glStencilFunc",
    "glStencilMask",
    "glStencilOp",
    "glTexCoord1d",
    "glTexCoord1dv",
    "glTexCoord1f",
    "glTexCoord1fv",
    "glTexCoord1i",
    "glTexCoord1iv",
    "glTexCoord1s",
    "glTexCoord1sv",
    "glTexCoord2d",
    "glTexCoord2dv",
    "glTexCoord2f",
    "glTexCoord2fv",
    "glTexCoord2i",
    "glTexCoord2iv",
    "glTexCoord2s",
    "glTexCoord2sv",
    "glTexCoord3d",
    "glTexCoord3dv",
    "glTexCoord3f",
    "glTexCoord3fv",
    "glTexCoord3i",
    "glTexCoord3iv",
    "glTexCoord3s",
    "glTexCoord3sv",
    "glTexCoord4d",
    "glTexCoord4dv",
    "glTexCoord4f",
    "glTexCoord4fv",
    "glTexCoord4i",
    "glTexCoord4iv",
    "glTexCoord4s",
    "glTexCoord4sv",
    "glTexCoordPointer",
    "glTexEnvf",
    "glTexEnvfv",
    "glTexEnvi",
    "glTexEnviv",
    "glTexGend",
    "glTexGendv",
    "glTexGenf",
    "glTexGenfv",
    "glTexGeni",
    "glTexGeniv",
    "glTexImage1D",
    "glTexImage2D",
    "glTexParameterf",
    "glTexParameterfv",
    "glTexParameteri",
    "glTexParameteriv",
    "glTexSubImage1D",
    "glTexSubImage2D",
    "glTranslated",
    "glTranslatef",
    "glVertex2d",
    "glVertex2dv",
    "glVertex2f",
    "glVertex2fv",
    "glVertex2i",
    "glVertex2iv",
    "glVertex2s",
    "glVertex2sv",
    "glVertex3d",
    "glVertex3dv",
    "glVertex3f",
    "glVertex3fv",
    "glVertex3i",
    "glVertex3iv",
    "glVertex3s",
    "glVertex3sv",
    "glVertex4d",
    "glVertex4dv",
    "glVertex4f",
    "glVertex4fv",
    "glVertex4i",
    "glVertex4iv",
    "glVertex4s",
    "glVertex4sv",
    "glVertexPointer",
    "glViewport",
    "gluBeginCurve",
    "gluBeginPolygon",
    "gluBeginSurface",
    "gluBeginTrim",
    "gluBuild1DMipmaps",
    "gluBuild2DMipmaps",
    "gluCylinder",
    "gluDeleteNurbsRenderer",
    "gluDeleteQuadric",
    "gluDeleteTess",
    "gluDisk",
    "gluEndCurve",
    "gluEndPolygon",
    "gluEndSurface",
    "gluEndTrim",
    "gluErrorString",
    "gluErrorUnicodeStringEXT",
    "gluGetNurbsProperty",
    "gluGetString",
    "gluGetTessProperty",
    "gluLoadSamplingMatrices",
    "gluLookAt",
    "gluNewNurbsRenderer",
    "gluNewQuadric",
    "gluNewTess",
    "gluNextContour",
    "gluNurbsCallback",
    "gluNurbsCurve",
    "gluNurbsProperty",
    "gluNurbsSurface",
    "gluOrtho2D",
    "gluPartialDisk",
    "gluPerspective",
    "gluPickMatrix",
    "gluProject",
    "gluPwlCurve",
    "gluQuadricCallback",
    "gluQuadricDrawStyle",
    "gluQuadricNormals",
    "gluQuadricOrientation",
    "gluQuadricTexture",
    "gluScaleImage",
    "gluSphere",
    "gluTessBeginContour",
    "gluTessBeginPolygon",
    "gluTessCallback",
    "gluTessEndContour",
    "gluTessEndPolygon",
    "gluTessNormal",
    "gluTessProperty",
    "gluTessVertex",
    "gluUnProject",
    "wglCopyContext",
    "wglCreateContext",
    "wglCreateLayerContext",
    "wglDeleteContext",
    "wglDescribeLayerPlane",
    "wglGetCurrentContext",
    "wglGetCurrentDC",
    "wglGetLayerPaletteEntries",
    "wglGetProcAddress",
    "wglMakeCurrent",
    "wglRealizeLayerPalette",
    "wglSetLayerPaletteEntries",
    "wglShareLists",
    "wglSwapLayerBuffers",
    "wglUseFontBitmapsA",
    "wglUseFontBitmapsW",
    "wglUseFontOutlinesA",
    "wglUseFontOutlinesW",
]
