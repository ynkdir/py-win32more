from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.Graphics.OpenGL
GL_VERSION_1_1: UInt32 = 1
GL_ACCUM: UInt32 = 256
GL_LOAD: UInt32 = 257
GL_RETURN: UInt32 = 258
GL_MULT: UInt32 = 259
GL_ADD: UInt32 = 260
GL_NEVER: UInt32 = 512
GL_LESS: UInt32 = 513
GL_EQUAL: UInt32 = 514
GL_LEQUAL: UInt32 = 515
GL_GREATER: UInt32 = 516
GL_NOTEQUAL: UInt32 = 517
GL_GEQUAL: UInt32 = 518
GL_ALWAYS: UInt32 = 519
GL_CURRENT_BIT: UInt32 = 1
GL_POINT_BIT: UInt32 = 2
GL_LINE_BIT: UInt32 = 4
GL_POLYGON_BIT: UInt32 = 8
GL_POLYGON_STIPPLE_BIT: UInt32 = 16
GL_PIXEL_MODE_BIT: UInt32 = 32
GL_LIGHTING_BIT: UInt32 = 64
GL_FOG_BIT: UInt32 = 128
GL_DEPTH_BUFFER_BIT: UInt32 = 256
GL_ACCUM_BUFFER_BIT: UInt32 = 512
GL_STENCIL_BUFFER_BIT: UInt32 = 1024
GL_VIEWPORT_BIT: UInt32 = 2048
GL_TRANSFORM_BIT: UInt32 = 4096
GL_ENABLE_BIT: UInt32 = 8192
GL_COLOR_BUFFER_BIT: UInt32 = 16384
GL_HINT_BIT: UInt32 = 32768
GL_EVAL_BIT: UInt32 = 65536
GL_LIST_BIT: UInt32 = 131072
GL_TEXTURE_BIT: UInt32 = 262144
GL_SCISSOR_BIT: UInt32 = 524288
GL_ALL_ATTRIB_BITS: UInt32 = 1048575
GL_POINTS: UInt32 = 0
GL_LINES: UInt32 = 1
GL_LINE_LOOP: UInt32 = 2
GL_LINE_STRIP: UInt32 = 3
GL_TRIANGLES: UInt32 = 4
GL_TRIANGLE_STRIP: UInt32 = 5
GL_TRIANGLE_FAN: UInt32 = 6
GL_QUADS: UInt32 = 7
GL_QUAD_STRIP: UInt32 = 8
GL_POLYGON: UInt32 = 9
GL_ZERO: UInt32 = 0
GL_ONE: UInt32 = 1
GL_SRC_COLOR: UInt32 = 768
GL_ONE_MINUS_SRC_COLOR: UInt32 = 769
GL_SRC_ALPHA: UInt32 = 770
GL_ONE_MINUS_SRC_ALPHA: UInt32 = 771
GL_DST_ALPHA: UInt32 = 772
GL_ONE_MINUS_DST_ALPHA: UInt32 = 773
GL_DST_COLOR: UInt32 = 774
GL_ONE_MINUS_DST_COLOR: UInt32 = 775
GL_SRC_ALPHA_SATURATE: UInt32 = 776
GL_TRUE: UInt32 = 1
GL_FALSE: UInt32 = 0
GL_CLIP_PLANE0: UInt32 = 12288
GL_CLIP_PLANE1: UInt32 = 12289
GL_CLIP_PLANE2: UInt32 = 12290
GL_CLIP_PLANE3: UInt32 = 12291
GL_CLIP_PLANE4: UInt32 = 12292
GL_CLIP_PLANE5: UInt32 = 12293
GL_BYTE: UInt32 = 5120
GL_UNSIGNED_BYTE: UInt32 = 5121
GL_SHORT: UInt32 = 5122
GL_UNSIGNED_SHORT: UInt32 = 5123
GL_INT: UInt32 = 5124
GL_UNSIGNED_INT: UInt32 = 5125
GL_FLOAT: UInt32 = 5126
GL_2_BYTES: UInt32 = 5127
GL_3_BYTES: UInt32 = 5128
GL_4_BYTES: UInt32 = 5129
GL_DOUBLE: UInt32 = 5130
GL_NONE: UInt32 = 0
GL_FRONT_LEFT: UInt32 = 1024
GL_FRONT_RIGHT: UInt32 = 1025
GL_BACK_LEFT: UInt32 = 1026
GL_BACK_RIGHT: UInt32 = 1027
GL_FRONT: UInt32 = 1028
GL_BACK: UInt32 = 1029
GL_LEFT: UInt32 = 1030
GL_RIGHT: UInt32 = 1031
GL_FRONT_AND_BACK: UInt32 = 1032
GL_AUX0: UInt32 = 1033
GL_AUX1: UInt32 = 1034
GL_AUX2: UInt32 = 1035
GL_AUX3: UInt32 = 1036
GL_NO_ERROR: UInt32 = 0
GL_INVALID_ENUM: UInt32 = 1280
GL_INVALID_VALUE: UInt32 = 1281
GL_INVALID_OPERATION: UInt32 = 1282
GL_STACK_OVERFLOW: UInt32 = 1283
GL_STACK_UNDERFLOW: UInt32 = 1284
GL_OUT_OF_MEMORY: UInt32 = 1285
GL_2D: UInt32 = 1536
GL_3D: UInt32 = 1537
GL_3D_COLOR: UInt32 = 1538
GL_3D_COLOR_TEXTURE: UInt32 = 1539
GL_4D_COLOR_TEXTURE: UInt32 = 1540
GL_PASS_THROUGH_TOKEN: UInt32 = 1792
GL_POINT_TOKEN: UInt32 = 1793
GL_LINE_TOKEN: UInt32 = 1794
GL_POLYGON_TOKEN: UInt32 = 1795
GL_BITMAP_TOKEN: UInt32 = 1796
GL_DRAW_PIXEL_TOKEN: UInt32 = 1797
GL_COPY_PIXEL_TOKEN: UInt32 = 1798
GL_LINE_RESET_TOKEN: UInt32 = 1799
GL_EXP: UInt32 = 2048
GL_EXP2: UInt32 = 2049
GL_CW: UInt32 = 2304
GL_CCW: UInt32 = 2305
GL_COEFF: UInt32 = 2560
GL_ORDER: UInt32 = 2561
GL_DOMAIN: UInt32 = 2562
GL_CURRENT_COLOR: UInt32 = 2816
GL_CURRENT_INDEX: UInt32 = 2817
GL_CURRENT_NORMAL: UInt32 = 2818
GL_CURRENT_TEXTURE_COORDS: UInt32 = 2819
GL_CURRENT_RASTER_COLOR: UInt32 = 2820
GL_CURRENT_RASTER_INDEX: UInt32 = 2821
GL_CURRENT_RASTER_TEXTURE_COORDS: UInt32 = 2822
GL_CURRENT_RASTER_POSITION: UInt32 = 2823
GL_CURRENT_RASTER_POSITION_VALID: UInt32 = 2824
GL_CURRENT_RASTER_DISTANCE: UInt32 = 2825
GL_POINT_SMOOTH: UInt32 = 2832
GL_POINT_SIZE: UInt32 = 2833
GL_POINT_SIZE_RANGE: UInt32 = 2834
GL_POINT_SIZE_GRANULARITY: UInt32 = 2835
GL_LINE_SMOOTH: UInt32 = 2848
GL_LINE_WIDTH: UInt32 = 2849
GL_LINE_WIDTH_RANGE: UInt32 = 2850
GL_LINE_WIDTH_GRANULARITY: UInt32 = 2851
GL_LINE_STIPPLE: UInt32 = 2852
GL_LINE_STIPPLE_PATTERN: UInt32 = 2853
GL_LINE_STIPPLE_REPEAT: UInt32 = 2854
GL_LIST_MODE: UInt32 = 2864
GL_MAX_LIST_NESTING: UInt32 = 2865
GL_LIST_BASE: UInt32 = 2866
GL_LIST_INDEX: UInt32 = 2867
GL_POLYGON_MODE: UInt32 = 2880
GL_POLYGON_SMOOTH: UInt32 = 2881
GL_POLYGON_STIPPLE: UInt32 = 2882
GL_EDGE_FLAG: UInt32 = 2883
GL_CULL_FACE: UInt32 = 2884
GL_CULL_FACE_MODE: UInt32 = 2885
GL_FRONT_FACE: UInt32 = 2886
GL_LIGHTING: UInt32 = 2896
GL_LIGHT_MODEL_LOCAL_VIEWER: UInt32 = 2897
GL_LIGHT_MODEL_TWO_SIDE: UInt32 = 2898
GL_LIGHT_MODEL_AMBIENT: UInt32 = 2899
GL_SHADE_MODEL: UInt32 = 2900
GL_COLOR_MATERIAL_FACE: UInt32 = 2901
GL_COLOR_MATERIAL_PARAMETER: UInt32 = 2902
GL_COLOR_MATERIAL: UInt32 = 2903
GL_FOG: UInt32 = 2912
GL_FOG_INDEX: UInt32 = 2913
GL_FOG_DENSITY: UInt32 = 2914
GL_FOG_START: UInt32 = 2915
GL_FOG_END: UInt32 = 2916
GL_FOG_MODE: UInt32 = 2917
GL_FOG_COLOR: UInt32 = 2918
GL_DEPTH_RANGE: UInt32 = 2928
GL_DEPTH_TEST: UInt32 = 2929
GL_DEPTH_WRITEMASK: UInt32 = 2930
GL_DEPTH_CLEAR_VALUE: UInt32 = 2931
GL_DEPTH_FUNC: UInt32 = 2932
GL_ACCUM_CLEAR_VALUE: UInt32 = 2944
GL_STENCIL_TEST: UInt32 = 2960
GL_STENCIL_CLEAR_VALUE: UInt32 = 2961
GL_STENCIL_FUNC: UInt32 = 2962
GL_STENCIL_VALUE_MASK: UInt32 = 2963
GL_STENCIL_FAIL: UInt32 = 2964
GL_STENCIL_PASS_DEPTH_FAIL: UInt32 = 2965
GL_STENCIL_PASS_DEPTH_PASS: UInt32 = 2966
GL_STENCIL_REF: UInt32 = 2967
GL_STENCIL_WRITEMASK: UInt32 = 2968
GL_MATRIX_MODE: UInt32 = 2976
GL_NORMALIZE: UInt32 = 2977
GL_VIEWPORT: UInt32 = 2978
GL_MODELVIEW_STACK_DEPTH: UInt32 = 2979
GL_PROJECTION_STACK_DEPTH: UInt32 = 2980
GL_TEXTURE_STACK_DEPTH: UInt32 = 2981
GL_MODELVIEW_MATRIX: UInt32 = 2982
GL_PROJECTION_MATRIX: UInt32 = 2983
GL_TEXTURE_MATRIX: UInt32 = 2984
GL_ATTRIB_STACK_DEPTH: UInt32 = 2992
GL_CLIENT_ATTRIB_STACK_DEPTH: UInt32 = 2993
GL_ALPHA_TEST: UInt32 = 3008
GL_ALPHA_TEST_FUNC: UInt32 = 3009
GL_ALPHA_TEST_REF: UInt32 = 3010
GL_DITHER: UInt32 = 3024
GL_BLEND_DST: UInt32 = 3040
GL_BLEND_SRC: UInt32 = 3041
GL_BLEND: UInt32 = 3042
GL_LOGIC_OP_MODE: UInt32 = 3056
GL_INDEX_LOGIC_OP: UInt32 = 3057
GL_COLOR_LOGIC_OP: UInt32 = 3058
GL_AUX_BUFFERS: UInt32 = 3072
GL_DRAW_BUFFER: UInt32 = 3073
GL_READ_BUFFER: UInt32 = 3074
GL_SCISSOR_BOX: UInt32 = 3088
GL_SCISSOR_TEST: UInt32 = 3089
GL_INDEX_CLEAR_VALUE: UInt32 = 3104
GL_INDEX_WRITEMASK: UInt32 = 3105
GL_COLOR_CLEAR_VALUE: UInt32 = 3106
GL_COLOR_WRITEMASK: UInt32 = 3107
GL_INDEX_MODE: UInt32 = 3120
GL_RGBA_MODE: UInt32 = 3121
GL_DOUBLEBUFFER: UInt32 = 3122
GL_STEREO: UInt32 = 3123
GL_RENDER_MODE: UInt32 = 3136
GL_PERSPECTIVE_CORRECTION_HINT: UInt32 = 3152
GL_POINT_SMOOTH_HINT: UInt32 = 3153
GL_LINE_SMOOTH_HINT: UInt32 = 3154
GL_POLYGON_SMOOTH_HINT: UInt32 = 3155
GL_FOG_HINT: UInt32 = 3156
GL_TEXTURE_GEN_S: UInt32 = 3168
GL_TEXTURE_GEN_T: UInt32 = 3169
GL_TEXTURE_GEN_R: UInt32 = 3170
GL_TEXTURE_GEN_Q: UInt32 = 3171
GL_PIXEL_MAP_I_TO_I: UInt32 = 3184
GL_PIXEL_MAP_S_TO_S: UInt32 = 3185
GL_PIXEL_MAP_I_TO_R: UInt32 = 3186
GL_PIXEL_MAP_I_TO_G: UInt32 = 3187
GL_PIXEL_MAP_I_TO_B: UInt32 = 3188
GL_PIXEL_MAP_I_TO_A: UInt32 = 3189
GL_PIXEL_MAP_R_TO_R: UInt32 = 3190
GL_PIXEL_MAP_G_TO_G: UInt32 = 3191
GL_PIXEL_MAP_B_TO_B: UInt32 = 3192
GL_PIXEL_MAP_A_TO_A: UInt32 = 3193
GL_PIXEL_MAP_I_TO_I_SIZE: UInt32 = 3248
GL_PIXEL_MAP_S_TO_S_SIZE: UInt32 = 3249
GL_PIXEL_MAP_I_TO_R_SIZE: UInt32 = 3250
GL_PIXEL_MAP_I_TO_G_SIZE: UInt32 = 3251
GL_PIXEL_MAP_I_TO_B_SIZE: UInt32 = 3252
GL_PIXEL_MAP_I_TO_A_SIZE: UInt32 = 3253
GL_PIXEL_MAP_R_TO_R_SIZE: UInt32 = 3254
GL_PIXEL_MAP_G_TO_G_SIZE: UInt32 = 3255
GL_PIXEL_MAP_B_TO_B_SIZE: UInt32 = 3256
GL_PIXEL_MAP_A_TO_A_SIZE: UInt32 = 3257
GL_UNPACK_SWAP_BYTES: UInt32 = 3312
GL_UNPACK_LSB_FIRST: UInt32 = 3313
GL_UNPACK_ROW_LENGTH: UInt32 = 3314
GL_UNPACK_SKIP_ROWS: UInt32 = 3315
GL_UNPACK_SKIP_PIXELS: UInt32 = 3316
GL_UNPACK_ALIGNMENT: UInt32 = 3317
GL_PACK_SWAP_BYTES: UInt32 = 3328
GL_PACK_LSB_FIRST: UInt32 = 3329
GL_PACK_ROW_LENGTH: UInt32 = 3330
GL_PACK_SKIP_ROWS: UInt32 = 3331
GL_PACK_SKIP_PIXELS: UInt32 = 3332
GL_PACK_ALIGNMENT: UInt32 = 3333
GL_MAP_COLOR: UInt32 = 3344
GL_MAP_STENCIL: UInt32 = 3345
GL_INDEX_SHIFT: UInt32 = 3346
GL_INDEX_OFFSET: UInt32 = 3347
GL_RED_SCALE: UInt32 = 3348
GL_RED_BIAS: UInt32 = 3349
GL_ZOOM_X: UInt32 = 3350
GL_ZOOM_Y: UInt32 = 3351
GL_GREEN_SCALE: UInt32 = 3352
GL_GREEN_BIAS: UInt32 = 3353
GL_BLUE_SCALE: UInt32 = 3354
GL_BLUE_BIAS: UInt32 = 3355
GL_ALPHA_SCALE: UInt32 = 3356
GL_ALPHA_BIAS: UInt32 = 3357
GL_DEPTH_SCALE: UInt32 = 3358
GL_DEPTH_BIAS: UInt32 = 3359
GL_MAX_EVAL_ORDER: UInt32 = 3376
GL_MAX_LIGHTS: UInt32 = 3377
GL_MAX_CLIP_PLANES: UInt32 = 3378
GL_MAX_TEXTURE_SIZE: UInt32 = 3379
GL_MAX_PIXEL_MAP_TABLE: UInt32 = 3380
GL_MAX_ATTRIB_STACK_DEPTH: UInt32 = 3381
GL_MAX_MODELVIEW_STACK_DEPTH: UInt32 = 3382
GL_MAX_NAME_STACK_DEPTH: UInt32 = 3383
GL_MAX_PROJECTION_STACK_DEPTH: UInt32 = 3384
GL_MAX_TEXTURE_STACK_DEPTH: UInt32 = 3385
GL_MAX_VIEWPORT_DIMS: UInt32 = 3386
GL_MAX_CLIENT_ATTRIB_STACK_DEPTH: UInt32 = 3387
GL_SUBPIXEL_BITS: UInt32 = 3408
GL_INDEX_BITS: UInt32 = 3409
GL_RED_BITS: UInt32 = 3410
GL_GREEN_BITS: UInt32 = 3411
GL_BLUE_BITS: UInt32 = 3412
GL_ALPHA_BITS: UInt32 = 3413
GL_DEPTH_BITS: UInt32 = 3414
GL_STENCIL_BITS: UInt32 = 3415
GL_ACCUM_RED_BITS: UInt32 = 3416
GL_ACCUM_GREEN_BITS: UInt32 = 3417
GL_ACCUM_BLUE_BITS: UInt32 = 3418
GL_ACCUM_ALPHA_BITS: UInt32 = 3419
GL_NAME_STACK_DEPTH: UInt32 = 3440
GL_AUTO_NORMAL: UInt32 = 3456
GL_MAP1_COLOR_4: UInt32 = 3472
GL_MAP1_INDEX: UInt32 = 3473
GL_MAP1_NORMAL: UInt32 = 3474
GL_MAP1_TEXTURE_COORD_1: UInt32 = 3475
GL_MAP1_TEXTURE_COORD_2: UInt32 = 3476
GL_MAP1_TEXTURE_COORD_3: UInt32 = 3477
GL_MAP1_TEXTURE_COORD_4: UInt32 = 3478
GL_MAP1_VERTEX_3: UInt32 = 3479
GL_MAP1_VERTEX_4: UInt32 = 3480
GL_MAP2_COLOR_4: UInt32 = 3504
GL_MAP2_INDEX: UInt32 = 3505
GL_MAP2_NORMAL: UInt32 = 3506
GL_MAP2_TEXTURE_COORD_1: UInt32 = 3507
GL_MAP2_TEXTURE_COORD_2: UInt32 = 3508
GL_MAP2_TEXTURE_COORD_3: UInt32 = 3509
GL_MAP2_TEXTURE_COORD_4: UInt32 = 3510
GL_MAP2_VERTEX_3: UInt32 = 3511
GL_MAP2_VERTEX_4: UInt32 = 3512
GL_MAP1_GRID_DOMAIN: UInt32 = 3536
GL_MAP1_GRID_SEGMENTS: UInt32 = 3537
GL_MAP2_GRID_DOMAIN: UInt32 = 3538
GL_MAP2_GRID_SEGMENTS: UInt32 = 3539
GL_TEXTURE_1D: UInt32 = 3552
GL_TEXTURE_2D: UInt32 = 3553
GL_FEEDBACK_BUFFER_POINTER: UInt32 = 3568
GL_FEEDBACK_BUFFER_SIZE: UInt32 = 3569
GL_FEEDBACK_BUFFER_TYPE: UInt32 = 3570
GL_SELECTION_BUFFER_POINTER: UInt32 = 3571
GL_SELECTION_BUFFER_SIZE: UInt32 = 3572
GL_TEXTURE_WIDTH: UInt32 = 4096
GL_TEXTURE_HEIGHT: UInt32 = 4097
GL_TEXTURE_INTERNAL_FORMAT: UInt32 = 4099
GL_TEXTURE_BORDER_COLOR: UInt32 = 4100
GL_TEXTURE_BORDER: UInt32 = 4101
GL_DONT_CARE: UInt32 = 4352
GL_FASTEST: UInt32 = 4353
GL_NICEST: UInt32 = 4354
GL_LIGHT0: UInt32 = 16384
GL_LIGHT1: UInt32 = 16385
GL_LIGHT2: UInt32 = 16386
GL_LIGHT3: UInt32 = 16387
GL_LIGHT4: UInt32 = 16388
GL_LIGHT5: UInt32 = 16389
GL_LIGHT6: UInt32 = 16390
GL_LIGHT7: UInt32 = 16391
GL_AMBIENT: UInt32 = 4608
GL_DIFFUSE: UInt32 = 4609
GL_SPECULAR: UInt32 = 4610
GL_POSITION: UInt32 = 4611
GL_SPOT_DIRECTION: UInt32 = 4612
GL_SPOT_EXPONENT: UInt32 = 4613
GL_SPOT_CUTOFF: UInt32 = 4614
GL_CONSTANT_ATTENUATION: UInt32 = 4615
GL_LINEAR_ATTENUATION: UInt32 = 4616
GL_QUADRATIC_ATTENUATION: UInt32 = 4617
GL_COMPILE: UInt32 = 4864
GL_COMPILE_AND_EXECUTE: UInt32 = 4865
GL_CLEAR: UInt32 = 5376
GL_AND: UInt32 = 5377
GL_AND_REVERSE: UInt32 = 5378
GL_COPY: UInt32 = 5379
GL_AND_INVERTED: UInt32 = 5380
GL_NOOP: UInt32 = 5381
GL_XOR: UInt32 = 5382
GL_OR: UInt32 = 5383
GL_NOR: UInt32 = 5384
GL_EQUIV: UInt32 = 5385
GL_INVERT: UInt32 = 5386
GL_OR_REVERSE: UInt32 = 5387
GL_COPY_INVERTED: UInt32 = 5388
GL_OR_INVERTED: UInt32 = 5389
GL_NAND: UInt32 = 5390
GL_SET: UInt32 = 5391
GL_EMISSION: UInt32 = 5632
GL_SHININESS: UInt32 = 5633
GL_AMBIENT_AND_DIFFUSE: UInt32 = 5634
GL_COLOR_INDEXES: UInt32 = 5635
GL_MODELVIEW: UInt32 = 5888
GL_PROJECTION: UInt32 = 5889
GL_TEXTURE: UInt32 = 5890
GL_COLOR: UInt32 = 6144
GL_DEPTH: UInt32 = 6145
GL_STENCIL: UInt32 = 6146
GL_COLOR_INDEX: UInt32 = 6400
GL_STENCIL_INDEX: UInt32 = 6401
GL_DEPTH_COMPONENT: UInt32 = 6402
GL_RED: UInt32 = 6403
GL_GREEN: UInt32 = 6404
GL_BLUE: UInt32 = 6405
GL_ALPHA: UInt32 = 6406
GL_RGB: UInt32 = 6407
GL_RGBA: UInt32 = 6408
GL_LUMINANCE: UInt32 = 6409
GL_LUMINANCE_ALPHA: UInt32 = 6410
GL_BITMAP: UInt32 = 6656
GL_POINT: UInt32 = 6912
GL_LINE: UInt32 = 6913
GL_FILL: UInt32 = 6914
GL_RENDER: UInt32 = 7168
GL_FEEDBACK: UInt32 = 7169
GL_SELECT: UInt32 = 7170
GL_FLAT: UInt32 = 7424
GL_SMOOTH: UInt32 = 7425
GL_KEEP: UInt32 = 7680
GL_REPLACE: UInt32 = 7681
GL_INCR: UInt32 = 7682
GL_DECR: UInt32 = 7683
GL_VENDOR: UInt32 = 7936
GL_RENDERER: UInt32 = 7937
GL_VERSION: UInt32 = 7938
GL_EXTENSIONS: UInt32 = 7939
GL_S: UInt32 = 8192
GL_T: UInt32 = 8193
GL_R: UInt32 = 8194
GL_Q: UInt32 = 8195
GL_MODULATE: UInt32 = 8448
GL_DECAL: UInt32 = 8449
GL_TEXTURE_ENV_MODE: UInt32 = 8704
GL_TEXTURE_ENV_COLOR: UInt32 = 8705
GL_TEXTURE_ENV: UInt32 = 8960
GL_EYE_LINEAR: UInt32 = 9216
GL_OBJECT_LINEAR: UInt32 = 9217
GL_SPHERE_MAP: UInt32 = 9218
GL_TEXTURE_GEN_MODE: UInt32 = 9472
GL_OBJECT_PLANE: UInt32 = 9473
GL_EYE_PLANE: UInt32 = 9474
GL_NEAREST: UInt32 = 9728
GL_LINEAR: UInt32 = 9729
GL_NEAREST_MIPMAP_NEAREST: UInt32 = 9984
GL_LINEAR_MIPMAP_NEAREST: UInt32 = 9985
GL_NEAREST_MIPMAP_LINEAR: UInt32 = 9986
GL_LINEAR_MIPMAP_LINEAR: UInt32 = 9987
GL_TEXTURE_MAG_FILTER: UInt32 = 10240
GL_TEXTURE_MIN_FILTER: UInt32 = 10241
GL_TEXTURE_WRAP_S: UInt32 = 10242
GL_TEXTURE_WRAP_T: UInt32 = 10243
GL_CLAMP: UInt32 = 10496
GL_REPEAT: UInt32 = 10497
GL_CLIENT_PIXEL_STORE_BIT: UInt32 = 1
GL_CLIENT_VERTEX_ARRAY_BIT: UInt32 = 2
GL_CLIENT_ALL_ATTRIB_BITS: UInt32 = 4294967295
GL_POLYGON_OFFSET_FACTOR: UInt32 = 32824
GL_POLYGON_OFFSET_UNITS: UInt32 = 10752
GL_POLYGON_OFFSET_POINT: UInt32 = 10753
GL_POLYGON_OFFSET_LINE: UInt32 = 10754
GL_POLYGON_OFFSET_FILL: UInt32 = 32823
GL_ALPHA4: UInt32 = 32827
GL_ALPHA8: UInt32 = 32828
GL_ALPHA12: UInt32 = 32829
GL_ALPHA16: UInt32 = 32830
GL_LUMINANCE4: UInt32 = 32831
GL_LUMINANCE8: UInt32 = 32832
GL_LUMINANCE12: UInt32 = 32833
GL_LUMINANCE16: UInt32 = 32834
GL_LUMINANCE4_ALPHA4: UInt32 = 32835
GL_LUMINANCE6_ALPHA2: UInt32 = 32836
GL_LUMINANCE8_ALPHA8: UInt32 = 32837
GL_LUMINANCE12_ALPHA4: UInt32 = 32838
GL_LUMINANCE12_ALPHA12: UInt32 = 32839
GL_LUMINANCE16_ALPHA16: UInt32 = 32840
GL_INTENSITY: UInt32 = 32841
GL_INTENSITY4: UInt32 = 32842
GL_INTENSITY8: UInt32 = 32843
GL_INTENSITY12: UInt32 = 32844
GL_INTENSITY16: UInt32 = 32845
GL_R3_G3_B2: UInt32 = 10768
GL_RGB4: UInt32 = 32847
GL_RGB5: UInt32 = 32848
GL_RGB8: UInt32 = 32849
GL_RGB10: UInt32 = 32850
GL_RGB12: UInt32 = 32851
GL_RGB16: UInt32 = 32852
GL_RGBA2: UInt32 = 32853
GL_RGBA4: UInt32 = 32854
GL_RGB5_A1: UInt32 = 32855
GL_RGBA8: UInt32 = 32856
GL_RGB10_A2: UInt32 = 32857
GL_RGBA12: UInt32 = 32858
GL_RGBA16: UInt32 = 32859
GL_TEXTURE_RED_SIZE: UInt32 = 32860
GL_TEXTURE_GREEN_SIZE: UInt32 = 32861
GL_TEXTURE_BLUE_SIZE: UInt32 = 32862
GL_TEXTURE_ALPHA_SIZE: UInt32 = 32863
GL_TEXTURE_LUMINANCE_SIZE: UInt32 = 32864
GL_TEXTURE_INTENSITY_SIZE: UInt32 = 32865
GL_PROXY_TEXTURE_1D: UInt32 = 32867
GL_PROXY_TEXTURE_2D: UInt32 = 32868
GL_TEXTURE_PRIORITY: UInt32 = 32870
GL_TEXTURE_RESIDENT: UInt32 = 32871
GL_TEXTURE_BINDING_1D: UInt32 = 32872
GL_TEXTURE_BINDING_2D: UInt32 = 32873
GL_VERTEX_ARRAY: UInt32 = 32884
GL_NORMAL_ARRAY: UInt32 = 32885
GL_COLOR_ARRAY: UInt32 = 32886
GL_INDEX_ARRAY: UInt32 = 32887
GL_TEXTURE_COORD_ARRAY: UInt32 = 32888
GL_EDGE_FLAG_ARRAY: UInt32 = 32889
GL_VERTEX_ARRAY_SIZE: UInt32 = 32890
GL_VERTEX_ARRAY_TYPE: UInt32 = 32891
GL_VERTEX_ARRAY_STRIDE: UInt32 = 32892
GL_NORMAL_ARRAY_TYPE: UInt32 = 32894
GL_NORMAL_ARRAY_STRIDE: UInt32 = 32895
GL_COLOR_ARRAY_SIZE: UInt32 = 32897
GL_COLOR_ARRAY_TYPE: UInt32 = 32898
GL_COLOR_ARRAY_STRIDE: UInt32 = 32899
GL_INDEX_ARRAY_TYPE: UInt32 = 32901
GL_INDEX_ARRAY_STRIDE: UInt32 = 32902
GL_TEXTURE_COORD_ARRAY_SIZE: UInt32 = 32904
GL_TEXTURE_COORD_ARRAY_TYPE: UInt32 = 32905
GL_TEXTURE_COORD_ARRAY_STRIDE: UInt32 = 32906
GL_EDGE_FLAG_ARRAY_STRIDE: UInt32 = 32908
GL_VERTEX_ARRAY_POINTER: UInt32 = 32910
GL_NORMAL_ARRAY_POINTER: UInt32 = 32911
GL_COLOR_ARRAY_POINTER: UInt32 = 32912
GL_INDEX_ARRAY_POINTER: UInt32 = 32913
GL_TEXTURE_COORD_ARRAY_POINTER: UInt32 = 32914
GL_EDGE_FLAG_ARRAY_POINTER: UInt32 = 32915
GL_V2F: UInt32 = 10784
GL_V3F: UInt32 = 10785
GL_C4UB_V2F: UInt32 = 10786
GL_C4UB_V3F: UInt32 = 10787
GL_C3F_V3F: UInt32 = 10788
GL_N3F_V3F: UInt32 = 10789
GL_C4F_N3F_V3F: UInt32 = 10790
GL_T2F_V3F: UInt32 = 10791
GL_T4F_V4F: UInt32 = 10792
GL_T2F_C4UB_V3F: UInt32 = 10793
GL_T2F_C3F_V3F: UInt32 = 10794
GL_T2F_N3F_V3F: UInt32 = 10795
GL_T2F_C4F_N3F_V3F: UInt32 = 10796
GL_T4F_C4F_N3F_V4F: UInt32 = 10797
GL_EXT_vertex_array: UInt32 = 1
GL_EXT_bgra: UInt32 = 1
GL_EXT_paletted_texture: UInt32 = 1
GL_WIN_swap_hint: UInt32 = 1
GL_WIN_draw_range_elements: UInt32 = 1
GL_VERTEX_ARRAY_EXT: UInt32 = 32884
GL_NORMAL_ARRAY_EXT: UInt32 = 32885
GL_COLOR_ARRAY_EXT: UInt32 = 32886
GL_INDEX_ARRAY_EXT: UInt32 = 32887
GL_TEXTURE_COORD_ARRAY_EXT: UInt32 = 32888
GL_EDGE_FLAG_ARRAY_EXT: UInt32 = 32889
GL_VERTEX_ARRAY_SIZE_EXT: UInt32 = 32890
GL_VERTEX_ARRAY_TYPE_EXT: UInt32 = 32891
GL_VERTEX_ARRAY_STRIDE_EXT: UInt32 = 32892
GL_VERTEX_ARRAY_COUNT_EXT: UInt32 = 32893
GL_NORMAL_ARRAY_TYPE_EXT: UInt32 = 32894
GL_NORMAL_ARRAY_STRIDE_EXT: UInt32 = 32895
GL_NORMAL_ARRAY_COUNT_EXT: UInt32 = 32896
GL_COLOR_ARRAY_SIZE_EXT: UInt32 = 32897
GL_COLOR_ARRAY_TYPE_EXT: UInt32 = 32898
GL_COLOR_ARRAY_STRIDE_EXT: UInt32 = 32899
GL_COLOR_ARRAY_COUNT_EXT: UInt32 = 32900
GL_INDEX_ARRAY_TYPE_EXT: UInt32 = 32901
GL_INDEX_ARRAY_STRIDE_EXT: UInt32 = 32902
GL_INDEX_ARRAY_COUNT_EXT: UInt32 = 32903
GL_TEXTURE_COORD_ARRAY_SIZE_EXT: UInt32 = 32904
GL_TEXTURE_COORD_ARRAY_TYPE_EXT: UInt32 = 32905
GL_TEXTURE_COORD_ARRAY_STRIDE_EXT: UInt32 = 32906
GL_TEXTURE_COORD_ARRAY_COUNT_EXT: UInt32 = 32907
GL_EDGE_FLAG_ARRAY_STRIDE_EXT: UInt32 = 32908
GL_EDGE_FLAG_ARRAY_COUNT_EXT: UInt32 = 32909
GL_VERTEX_ARRAY_POINTER_EXT: UInt32 = 32910
GL_NORMAL_ARRAY_POINTER_EXT: UInt32 = 32911
GL_COLOR_ARRAY_POINTER_EXT: UInt32 = 32912
GL_INDEX_ARRAY_POINTER_EXT: UInt32 = 32913
GL_TEXTURE_COORD_ARRAY_POINTER_EXT: UInt32 = 32914
GL_EDGE_FLAG_ARRAY_POINTER_EXT: UInt32 = 32915
GL_DOUBLE_EXT: UInt32 = 5130
GL_BGR_EXT: UInt32 = 32992
GL_BGRA_EXT: UInt32 = 32993
GL_COLOR_TABLE_FORMAT_EXT: UInt32 = 32984
GL_COLOR_TABLE_WIDTH_EXT: UInt32 = 32985
GL_COLOR_TABLE_RED_SIZE_EXT: UInt32 = 32986
GL_COLOR_TABLE_GREEN_SIZE_EXT: UInt32 = 32987
GL_COLOR_TABLE_BLUE_SIZE_EXT: UInt32 = 32988
GL_COLOR_TABLE_ALPHA_SIZE_EXT: UInt32 = 32989
GL_COLOR_TABLE_LUMINANCE_SIZE_EXT: UInt32 = 32990
GL_COLOR_TABLE_INTENSITY_SIZE_EXT: UInt32 = 32991
GL_COLOR_INDEX1_EXT: UInt32 = 32994
GL_COLOR_INDEX2_EXT: UInt32 = 32995
GL_COLOR_INDEX4_EXT: UInt32 = 32996
GL_COLOR_INDEX8_EXT: UInt32 = 32997
GL_COLOR_INDEX12_EXT: UInt32 = 32998
GL_COLOR_INDEX16_EXT: UInt32 = 32999
GL_MAX_ELEMENTS_VERTICES_WIN: UInt32 = 33000
GL_MAX_ELEMENTS_INDICES_WIN: UInt32 = 33001
GL_PHONG_WIN: UInt32 = 33002
GL_PHONG_HINT_WIN: UInt32 = 33003
GL_FOG_SPECULAR_TEXTURE_WIN: UInt32 = 33004
GL_LOGIC_OP: UInt32 = 3057
GL_TEXTURE_COMPONENTS: UInt32 = 4099
GLU_VERSION_1_1: UInt32 = 1
GLU_VERSION_1_2: UInt32 = 1
GLU_INVALID_ENUM: UInt32 = 100900
GLU_INVALID_VALUE: UInt32 = 100901
GLU_OUT_OF_MEMORY: UInt32 = 100902
GLU_INCOMPATIBLE_GL_VERSION: UInt32 = 100903
GLU_VERSION: UInt32 = 100800
GLU_EXTENSIONS: UInt32 = 100801
GLU_TRUE: UInt32 = 1
GLU_FALSE: UInt32 = 0
GLU_SMOOTH: UInt32 = 100000
GLU_FLAT: UInt32 = 100001
GLU_NONE: UInt32 = 100002
GLU_POINT: UInt32 = 100010
GLU_LINE: UInt32 = 100011
GLU_FILL: UInt32 = 100012
GLU_SILHOUETTE: UInt32 = 100013
GLU_OUTSIDE: UInt32 = 100020
GLU_INSIDE: UInt32 = 100021
GLU_TESS_WINDING_RULE: UInt32 = 100140
GLU_TESS_BOUNDARY_ONLY: UInt32 = 100141
GLU_TESS_TOLERANCE: UInt32 = 100142
GLU_TESS_WINDING_ODD: UInt32 = 100130
GLU_TESS_WINDING_NONZERO: UInt32 = 100131
GLU_TESS_WINDING_POSITIVE: UInt32 = 100132
GLU_TESS_WINDING_NEGATIVE: UInt32 = 100133
GLU_TESS_WINDING_ABS_GEQ_TWO: UInt32 = 100134
GLU_TESS_BEGIN: UInt32 = 100100
GLU_TESS_VERTEX: UInt32 = 100101
GLU_TESS_END: UInt32 = 100102
GLU_TESS_ERROR: UInt32 = 100103
GLU_TESS_EDGE_FLAG: UInt32 = 100104
GLU_TESS_COMBINE: UInt32 = 100105
GLU_TESS_BEGIN_DATA: UInt32 = 100106
GLU_TESS_VERTEX_DATA: UInt32 = 100107
GLU_TESS_END_DATA: UInt32 = 100108
GLU_TESS_ERROR_DATA: UInt32 = 100109
GLU_TESS_EDGE_FLAG_DATA: UInt32 = 100110
GLU_TESS_COMBINE_DATA: UInt32 = 100111
GLU_TESS_ERROR1: UInt32 = 100151
GLU_TESS_ERROR2: UInt32 = 100152
GLU_TESS_ERROR3: UInt32 = 100153
GLU_TESS_ERROR4: UInt32 = 100154
GLU_TESS_ERROR5: UInt32 = 100155
GLU_TESS_ERROR6: UInt32 = 100156
GLU_TESS_ERROR7: UInt32 = 100157
GLU_TESS_ERROR8: UInt32 = 100158
GLU_TESS_MISSING_BEGIN_POLYGON: UInt32 = 100151
GLU_TESS_MISSING_BEGIN_CONTOUR: UInt32 = 100152
GLU_TESS_MISSING_END_POLYGON: UInt32 = 100153
GLU_TESS_MISSING_END_CONTOUR: UInt32 = 100154
GLU_TESS_COORD_TOO_LARGE: UInt32 = 100155
GLU_TESS_NEED_COMBINE_CALLBACK: UInt32 = 100156
GLU_AUTO_LOAD_MATRIX: UInt32 = 100200
GLU_CULLING: UInt32 = 100201
GLU_SAMPLING_TOLERANCE: UInt32 = 100203
GLU_DISPLAY_MODE: UInt32 = 100204
GLU_PARAMETRIC_TOLERANCE: UInt32 = 100202
GLU_SAMPLING_METHOD: UInt32 = 100205
GLU_U_STEP: UInt32 = 100206
GLU_V_STEP: UInt32 = 100207
GLU_PATH_LENGTH: UInt32 = 100215
GLU_PARAMETRIC_ERROR: UInt32 = 100216
GLU_DOMAIN_DISTANCE: UInt32 = 100217
GLU_MAP1_TRIM_2: UInt32 = 100210
GLU_MAP1_TRIM_3: UInt32 = 100211
GLU_OUTLINE_POLYGON: UInt32 = 100240
GLU_OUTLINE_PATCH: UInt32 = 100241
GLU_NURBS_ERROR1: UInt32 = 100251
GLU_NURBS_ERROR2: UInt32 = 100252
GLU_NURBS_ERROR3: UInt32 = 100253
GLU_NURBS_ERROR4: UInt32 = 100254
GLU_NURBS_ERROR5: UInt32 = 100255
GLU_NURBS_ERROR6: UInt32 = 100256
GLU_NURBS_ERROR7: UInt32 = 100257
GLU_NURBS_ERROR8: UInt32 = 100258
GLU_NURBS_ERROR9: UInt32 = 100259
GLU_NURBS_ERROR10: UInt32 = 100260
GLU_NURBS_ERROR11: UInt32 = 100261
GLU_NURBS_ERROR12: UInt32 = 100262
GLU_NURBS_ERROR13: UInt32 = 100263
GLU_NURBS_ERROR14: UInt32 = 100264
GLU_NURBS_ERROR15: UInt32 = 100265
GLU_NURBS_ERROR16: UInt32 = 100266
GLU_NURBS_ERROR17: UInt32 = 100267
GLU_NURBS_ERROR18: UInt32 = 100268
GLU_NURBS_ERROR19: UInt32 = 100269
GLU_NURBS_ERROR20: UInt32 = 100270
GLU_NURBS_ERROR21: UInt32 = 100271
GLU_NURBS_ERROR22: UInt32 = 100272
GLU_NURBS_ERROR23: UInt32 = 100273
GLU_NURBS_ERROR24: UInt32 = 100274
GLU_NURBS_ERROR25: UInt32 = 100275
GLU_NURBS_ERROR26: UInt32 = 100276
GLU_NURBS_ERROR27: UInt32 = 100277
GLU_NURBS_ERROR28: UInt32 = 100278
GLU_NURBS_ERROR29: UInt32 = 100279
GLU_NURBS_ERROR30: UInt32 = 100280
GLU_NURBS_ERROR31: UInt32 = 100281
GLU_NURBS_ERROR32: UInt32 = 100282
GLU_NURBS_ERROR33: UInt32 = 100283
GLU_NURBS_ERROR34: UInt32 = 100284
GLU_NURBS_ERROR35: UInt32 = 100285
GLU_NURBS_ERROR36: UInt32 = 100286
GLU_NURBS_ERROR37: UInt32 = 100287
GLU_CW: UInt32 = 100120
GLU_CCW: UInt32 = 100121
GLU_INTERIOR: UInt32 = 100122
GLU_EXTERIOR: UInt32 = 100123
GLU_UNKNOWN: UInt32 = 100124
GLU_BEGIN: UInt32 = 100100
GLU_VERTEX: UInt32 = 100101
GLU_END: UInt32 = 100102
GLU_ERROR: UInt32 = 100103
GLU_EDGE_FLAG: UInt32 = 100104
@winfunctype('GDI32.dll')
def ChoosePixelFormat(hdc: win32more.Windows.Win32.Graphics.Gdi.HDC, ppfd: POINTER(win32more.Windows.Win32.Graphics.OpenGL.PIXELFORMATDESCRIPTOR)) -> Int32: ...
@winfunctype('GDI32.dll')
def DescribePixelFormat(hdc: win32more.Windows.Win32.Graphics.Gdi.HDC, iPixelFormat: Int32, nBytes: UInt32, ppfd: POINTER(win32more.Windows.Win32.Graphics.OpenGL.PIXELFORMATDESCRIPTOR)) -> Int32: ...
@winfunctype('GDI32.dll')
def GetPixelFormat(hdc: win32more.Windows.Win32.Graphics.Gdi.HDC) -> Int32: ...
@winfunctype('GDI32.dll')
def SetPixelFormat(hdc: win32more.Windows.Win32.Graphics.Gdi.HDC, format: Int32, ppfd: POINTER(win32more.Windows.Win32.Graphics.OpenGL.PIXELFORMATDESCRIPTOR)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def GetEnhMetaFilePixelFormat(hemf: win32more.Windows.Win32.Graphics.Gdi.HENHMETAFILE, cbBuffer: UInt32, ppfd: POINTER(win32more.Windows.Win32.Graphics.OpenGL.PIXELFORMATDESCRIPTOR)) -> UInt32: ...
@winfunctype('OPENGL32.dll')
def wglCopyContext(param0: win32more.Windows.Win32.Graphics.OpenGL.HGLRC, param1: win32more.Windows.Win32.Graphics.OpenGL.HGLRC, param2: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('OPENGL32.dll')
def wglCreateContext(param0: win32more.Windows.Win32.Graphics.Gdi.HDC) -> win32more.Windows.Win32.Graphics.OpenGL.HGLRC: ...
@winfunctype('OPENGL32.dll')
def wglCreateLayerContext(param0: win32more.Windows.Win32.Graphics.Gdi.HDC, param1: Int32) -> win32more.Windows.Win32.Graphics.OpenGL.HGLRC: ...
@winfunctype('OPENGL32.dll')
def wglDeleteContext(param0: win32more.Windows.Win32.Graphics.OpenGL.HGLRC) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('OPENGL32.dll')
def wglGetCurrentContext() -> win32more.Windows.Win32.Graphics.OpenGL.HGLRC: ...
@winfunctype('OPENGL32.dll')
def wglGetCurrentDC() -> win32more.Windows.Win32.Graphics.Gdi.HDC: ...
@winfunctype('OPENGL32.dll')
def wglGetProcAddress(param0: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.PROC: ...
@winfunctype('OPENGL32.dll')
def wglMakeCurrent(param0: win32more.Windows.Win32.Graphics.Gdi.HDC, param1: win32more.Windows.Win32.Graphics.OpenGL.HGLRC) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('OPENGL32.dll')
def wglShareLists(param0: win32more.Windows.Win32.Graphics.OpenGL.HGLRC, param1: win32more.Windows.Win32.Graphics.OpenGL.HGLRC) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('OPENGL32.dll')
def wglUseFontBitmapsA(param0: win32more.Windows.Win32.Graphics.Gdi.HDC, param1: UInt32, param2: UInt32, param3: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('OPENGL32.dll')
def wglUseFontBitmapsW(param0: win32more.Windows.Win32.Graphics.Gdi.HDC, param1: UInt32, param2: UInt32, param3: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
wglUseFontBitmaps = UnicodeAlias('wglUseFontBitmapsW')
@winfunctype('GDI32.dll')
def SwapBuffers(param0: win32more.Windows.Win32.Graphics.Gdi.HDC) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('OPENGL32.dll')
def wglUseFontOutlinesA(param0: win32more.Windows.Win32.Graphics.Gdi.HDC, param1: UInt32, param2: UInt32, param3: UInt32, param4: Single, param5: Single, param6: Int32, param7: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLYPHMETRICSFLOAT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('OPENGL32.dll')
def wglUseFontOutlinesW(param0: win32more.Windows.Win32.Graphics.Gdi.HDC, param1: UInt32, param2: UInt32, param3: UInt32, param4: Single, param5: Single, param6: Int32, param7: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLYPHMETRICSFLOAT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
wglUseFontOutlines = UnicodeAlias('wglUseFontOutlinesW')
@winfunctype('OPENGL32.dll')
def wglDescribeLayerPlane(param0: win32more.Windows.Win32.Graphics.Gdi.HDC, param1: Int32, param2: Int32, param3: UInt32, param4: POINTER(win32more.Windows.Win32.Graphics.OpenGL.LAYERPLANEDESCRIPTOR)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('OPENGL32.dll')
def wglSetLayerPaletteEntries(param0: win32more.Windows.Win32.Graphics.Gdi.HDC, param1: Int32, param2: Int32, param3: Int32, param4: POINTER(win32more.Windows.Win32.Foundation.COLORREF)) -> Int32: ...
@winfunctype('OPENGL32.dll')
def wglGetLayerPaletteEntries(param0: win32more.Windows.Win32.Graphics.Gdi.HDC, param1: Int32, param2: Int32, param3: Int32, param4: POINTER(win32more.Windows.Win32.Foundation.COLORREF)) -> Int32: ...
@winfunctype('OPENGL32.dll')
def wglRealizeLayerPalette(param0: win32more.Windows.Win32.Graphics.Gdi.HDC, param1: Int32, param2: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('OPENGL32.dll')
def wglSwapLayerBuffers(param0: win32more.Windows.Win32.Graphics.Gdi.HDC, param1: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('OPENGL32.dll')
def glAccum(op: UInt32, value: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glAlphaFunc(func: UInt32, ref: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glAreTexturesResident(n: Int32, textures: POINTER(UInt32), residences: POINTER(Byte)) -> Byte: ...
@winfunctype('OPENGL32.dll')
def glArrayElement(i: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glBegin(mode: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glBindTexture(target: UInt32, texture: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glBitmap(width: Int32, height: Int32, xorig: Single, yorig: Single, xmove: Single, ymove: Single, bitmap: POINTER(Byte)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glBlendFunc(sfactor: UInt32, dfactor: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glCallList(list: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glCallLists(n: Int32, type: UInt32, lists: VoidPtr) -> Void: ...
@winfunctype('OPENGL32.dll')
def glClear(mask: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glClearAccum(red: Single, green: Single, blue: Single, alpha: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glClearColor(red: Single, green: Single, blue: Single, alpha: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glClearDepth(depth: Double) -> Void: ...
@winfunctype('OPENGL32.dll')
def glClearIndex(c: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glClearStencil(s: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glClipPlane(plane: UInt32, equation: POINTER(Double)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor3b(red: SByte, green: SByte, blue: SByte) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor3bv(v: POINTER(SByte)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor3d(red: Double, green: Double, blue: Double) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor3dv(v: POINTER(Double)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor3f(red: Single, green: Single, blue: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor3fv(v: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor3i(red: Int32, green: Int32, blue: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor3iv(v: POINTER(Int32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor3s(red: Int16, green: Int16, blue: Int16) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor3sv(v: POINTER(Int16)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor3ub(red: Byte, green: Byte, blue: Byte) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor3ubv(v: POINTER(Byte)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor3ui(red: UInt32, green: UInt32, blue: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor3uiv(v: POINTER(UInt32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor3us(red: UInt16, green: UInt16, blue: UInt16) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor3usv(v: POINTER(UInt16)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor4b(red: SByte, green: SByte, blue: SByte, alpha: SByte) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor4bv(v: POINTER(SByte)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor4d(red: Double, green: Double, blue: Double, alpha: Double) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor4dv(v: POINTER(Double)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor4f(red: Single, green: Single, blue: Single, alpha: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor4fv(v: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor4i(red: Int32, green: Int32, blue: Int32, alpha: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor4iv(v: POINTER(Int32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor4s(red: Int16, green: Int16, blue: Int16, alpha: Int16) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor4sv(v: POINTER(Int16)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor4ub(red: Byte, green: Byte, blue: Byte, alpha: Byte) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor4ubv(v: POINTER(Byte)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor4ui(red: UInt32, green: UInt32, blue: UInt32, alpha: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor4uiv(v: POINTER(UInt32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor4us(red: UInt16, green: UInt16, blue: UInt16, alpha: UInt16) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColor4usv(v: POINTER(UInt16)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColorMask(red: Byte, green: Byte, blue: Byte, alpha: Byte) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColorMaterial(face: UInt32, mode: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glColorPointer(size: Int32, type: UInt32, stride: Int32, pointer: VoidPtr) -> Void: ...
@winfunctype('OPENGL32.dll')
def glCopyPixels(x: Int32, y: Int32, width: Int32, height: Int32, type: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glCopyTexImage1D(target: UInt32, level: Int32, internalFormat: UInt32, x: Int32, y: Int32, width: Int32, border: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glCopyTexImage2D(target: UInt32, level: Int32, internalFormat: UInt32, x: Int32, y: Int32, width: Int32, height: Int32, border: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glCopyTexSubImage1D(target: UInt32, level: Int32, xoffset: Int32, x: Int32, y: Int32, width: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glCopyTexSubImage2D(target: UInt32, level: Int32, xoffset: Int32, yoffset: Int32, x: Int32, y: Int32, width: Int32, height: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glCullFace(mode: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glDeleteLists(list: UInt32, range: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glDeleteTextures(n: Int32, textures: POINTER(UInt32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glDepthFunc(func: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glDepthMask(flag: Byte) -> Void: ...
@winfunctype('OPENGL32.dll')
def glDepthRange(zNear: Double, zFar: Double) -> Void: ...
@winfunctype('OPENGL32.dll')
def glDisable(cap: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glDisableClientState(array: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glDrawArrays(mode: UInt32, first: Int32, count: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glDrawBuffer(mode: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glDrawElements(mode: UInt32, count: Int32, type: UInt32, indices: VoidPtr) -> Void: ...
@winfunctype('OPENGL32.dll')
def glDrawPixels(width: Int32, height: Int32, format: UInt32, type: UInt32, pixels: VoidPtr) -> Void: ...
@winfunctype('OPENGL32.dll')
def glEdgeFlag(flag: Byte) -> Void: ...
@winfunctype('OPENGL32.dll')
def glEdgeFlagPointer(stride: Int32, pointer: VoidPtr) -> Void: ...
@winfunctype('OPENGL32.dll')
def glEdgeFlagv(flag: POINTER(Byte)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glEnable(cap: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glEnableClientState(array: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glEnd() -> Void: ...
@winfunctype('OPENGL32.dll')
def glEndList() -> Void: ...
@winfunctype('OPENGL32.dll')
def glEvalCoord1d(u: Double) -> Void: ...
@winfunctype('OPENGL32.dll')
def glEvalCoord1dv(u: POINTER(Double)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glEvalCoord1f(u: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glEvalCoord1fv(u: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glEvalCoord2d(u: Double, v: Double) -> Void: ...
@winfunctype('OPENGL32.dll')
def glEvalCoord2dv(u: POINTER(Double)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glEvalCoord2f(u: Single, v: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glEvalCoord2fv(u: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glEvalMesh1(mode: UInt32, i1: Int32, i2: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glEvalMesh2(mode: UInt32, i1: Int32, i2: Int32, j1: Int32, j2: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glEvalPoint1(i: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glEvalPoint2(i: Int32, j: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glFeedbackBuffer(size: Int32, type: UInt32, buffer: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glFinish() -> Void: ...
@winfunctype('OPENGL32.dll')
def glFlush() -> Void: ...
@winfunctype('OPENGL32.dll')
def glFogf(pname: UInt32, param1: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glFogfv(pname: UInt32, params: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glFogi(pname: UInt32, param1: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glFogiv(pname: UInt32, params: POINTER(Int32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glFrontFace(mode: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glFrustum(left: Double, right: Double, bottom: Double, top: Double, zNear: Double, zFar: Double) -> Void: ...
@winfunctype('OPENGL32.dll')
def glGenLists(range: Int32) -> UInt32: ...
@winfunctype('OPENGL32.dll')
def glGenTextures(n: Int32, textures: POINTER(UInt32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glGetBooleanv(pname: UInt32, params: POINTER(Byte)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glGetClipPlane(plane: UInt32, equation: POINTER(Double)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glGetDoublev(pname: UInt32, params: POINTER(Double)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glGetError() -> UInt32: ...
@winfunctype('OPENGL32.dll')
def glGetFloatv(pname: UInt32, params: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glGetIntegerv(pname: UInt32, params: POINTER(Int32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glGetLightfv(light: UInt32, pname: UInt32, params: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glGetLightiv(light: UInt32, pname: UInt32, params: POINTER(Int32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glGetMapdv(target: UInt32, query: UInt32, v: POINTER(Double)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glGetMapfv(target: UInt32, query: UInt32, v: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glGetMapiv(target: UInt32, query: UInt32, v: POINTER(Int32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glGetMaterialfv(face: UInt32, pname: UInt32, params: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glGetMaterialiv(face: UInt32, pname: UInt32, params: POINTER(Int32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glGetPixelMapfv(map: UInt32, values: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glGetPixelMapuiv(map: UInt32, values: POINTER(UInt32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glGetPixelMapusv(map: UInt32, values: POINTER(UInt16)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glGetPointerv(pname: UInt32, params: POINTER(VoidPtr)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glGetPolygonStipple(mask: POINTER(Byte)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glGetString(name: UInt32) -> POINTER(Byte): ...
@winfunctype('OPENGL32.dll')
def glGetTexEnvfv(target: UInt32, pname: UInt32, params: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glGetTexEnviv(target: UInt32, pname: UInt32, params: POINTER(Int32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glGetTexGendv(coord: UInt32, pname: UInt32, params: POINTER(Double)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glGetTexGenfv(coord: UInt32, pname: UInt32, params: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glGetTexGeniv(coord: UInt32, pname: UInt32, params: POINTER(Int32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glGetTexImage(target: UInt32, level: Int32, format: UInt32, type: UInt32, pixels: VoidPtr) -> Void: ...
@winfunctype('OPENGL32.dll')
def glGetTexLevelParameterfv(target: UInt32, level: Int32, pname: UInt32, params: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glGetTexLevelParameteriv(target: UInt32, level: Int32, pname: UInt32, params: POINTER(Int32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glGetTexParameterfv(target: UInt32, pname: UInt32, params: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glGetTexParameteriv(target: UInt32, pname: UInt32, params: POINTER(Int32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glHint(target: UInt32, mode: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glIndexMask(mask: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glIndexPointer(type: UInt32, stride: Int32, pointer: VoidPtr) -> Void: ...
@winfunctype('OPENGL32.dll')
def glIndexd(c: Double) -> Void: ...
@winfunctype('OPENGL32.dll')
def glIndexdv(c: POINTER(Double)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glIndexf(c: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glIndexfv(c: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glIndexi(c: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glIndexiv(c: POINTER(Int32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glIndexs(c: Int16) -> Void: ...
@winfunctype('OPENGL32.dll')
def glIndexsv(c: POINTER(Int16)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glIndexub(c: Byte) -> Void: ...
@winfunctype('OPENGL32.dll')
def glIndexubv(c: POINTER(Byte)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glInitNames() -> Void: ...
@winfunctype('OPENGL32.dll')
def glInterleavedArrays(format: UInt32, stride: Int32, pointer: VoidPtr) -> Void: ...
@winfunctype('OPENGL32.dll')
def glIsEnabled(cap: UInt32) -> Byte: ...
@winfunctype('OPENGL32.dll')
def glIsList(list: UInt32) -> Byte: ...
@winfunctype('OPENGL32.dll')
def glIsTexture(texture: UInt32) -> Byte: ...
@winfunctype('OPENGL32.dll')
def glLightModelf(pname: UInt32, param1: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glLightModelfv(pname: UInt32, params: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glLightModeli(pname: UInt32, param1: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glLightModeliv(pname: UInt32, params: POINTER(Int32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glLightf(light: UInt32, pname: UInt32, param2: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glLightfv(light: UInt32, pname: UInt32, params: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glLighti(light: UInt32, pname: UInt32, param2: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glLightiv(light: UInt32, pname: UInt32, params: POINTER(Int32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glLineStipple(factor: Int32, pattern: UInt16) -> Void: ...
@winfunctype('OPENGL32.dll')
def glLineWidth(width: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glListBase(base: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glLoadIdentity() -> Void: ...
@winfunctype('OPENGL32.dll')
def glLoadMatrixd(m: POINTER(Double)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glLoadMatrixf(m: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glLoadName(name: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glLogicOp(opcode: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glMap1d(target: UInt32, u1: Double, u2: Double, stride: Int32, order: Int32, points: POINTER(Double)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glMap1f(target: UInt32, u1: Single, u2: Single, stride: Int32, order: Int32, points: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glMap2d(target: UInt32, u1: Double, u2: Double, ustride: Int32, uorder: Int32, v1: Double, v2: Double, vstride: Int32, vorder: Int32, points: POINTER(Double)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glMap2f(target: UInt32, u1: Single, u2: Single, ustride: Int32, uorder: Int32, v1: Single, v2: Single, vstride: Int32, vorder: Int32, points: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glMapGrid1d(un: Int32, u1: Double, u2: Double) -> Void: ...
@winfunctype('OPENGL32.dll')
def glMapGrid1f(un: Int32, u1: Single, u2: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glMapGrid2d(un: Int32, u1: Double, u2: Double, vn: Int32, v1: Double, v2: Double) -> Void: ...
@winfunctype('OPENGL32.dll')
def glMapGrid2f(un: Int32, u1: Single, u2: Single, vn: Int32, v1: Single, v2: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glMaterialf(face: UInt32, pname: UInt32, param2: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glMaterialfv(face: UInt32, pname: UInt32, params: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glMateriali(face: UInt32, pname: UInt32, param2: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glMaterialiv(face: UInt32, pname: UInt32, params: POINTER(Int32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glMatrixMode(mode: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glMultMatrixd(m: POINTER(Double)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glMultMatrixf(m: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glNewList(list: UInt32, mode: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glNormal3b(nx: SByte, ny: SByte, nz: SByte) -> Void: ...
@winfunctype('OPENGL32.dll')
def glNormal3bv(v: POINTER(SByte)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glNormal3d(nx: Double, ny: Double, nz: Double) -> Void: ...
@winfunctype('OPENGL32.dll')
def glNormal3dv(v: POINTER(Double)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glNormal3f(nx: Single, ny: Single, nz: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glNormal3fv(v: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glNormal3i(nx: Int32, ny: Int32, nz: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glNormal3iv(v: POINTER(Int32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glNormal3s(nx: Int16, ny: Int16, nz: Int16) -> Void: ...
@winfunctype('OPENGL32.dll')
def glNormal3sv(v: POINTER(Int16)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glNormalPointer(type: UInt32, stride: Int32, pointer: VoidPtr) -> Void: ...
@winfunctype('OPENGL32.dll')
def glOrtho(left: Double, right: Double, bottom: Double, top: Double, zNear: Double, zFar: Double) -> Void: ...
@winfunctype('OPENGL32.dll')
def glPassThrough(token: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glPixelMapfv(map: UInt32, mapsize: Int32, values: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glPixelMapuiv(map: UInt32, mapsize: Int32, values: POINTER(UInt32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glPixelMapusv(map: UInt32, mapsize: Int32, values: POINTER(UInt16)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glPixelStoref(pname: UInt32, param1: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glPixelStorei(pname: UInt32, param1: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glPixelTransferf(pname: UInt32, param1: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glPixelTransferi(pname: UInt32, param1: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glPixelZoom(xfactor: Single, yfactor: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glPointSize(size: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glPolygonMode(face: UInt32, mode: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glPolygonOffset(factor: Single, units: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glPolygonStipple(mask: POINTER(Byte)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glPopAttrib() -> Void: ...
@winfunctype('OPENGL32.dll')
def glPopClientAttrib() -> Void: ...
@winfunctype('OPENGL32.dll')
def glPopMatrix() -> Void: ...
@winfunctype('OPENGL32.dll')
def glPopName() -> Void: ...
@winfunctype('OPENGL32.dll')
def glPrioritizeTextures(n: Int32, textures: POINTER(UInt32), priorities: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glPushAttrib(mask: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glPushClientAttrib(mask: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glPushMatrix() -> Void: ...
@winfunctype('OPENGL32.dll')
def glPushName(name: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRasterPos2d(x: Double, y: Double) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRasterPos2dv(v: POINTER(Double)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRasterPos2f(x: Single, y: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRasterPos2fv(v: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRasterPos2i(x: Int32, y: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRasterPos2iv(v: POINTER(Int32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRasterPos2s(x: Int16, y: Int16) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRasterPos2sv(v: POINTER(Int16)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRasterPos3d(x: Double, y: Double, z: Double) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRasterPos3dv(v: POINTER(Double)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRasterPos3f(x: Single, y: Single, z: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRasterPos3fv(v: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRasterPos3i(x: Int32, y: Int32, z: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRasterPos3iv(v: POINTER(Int32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRasterPos3s(x: Int16, y: Int16, z: Int16) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRasterPos3sv(v: POINTER(Int16)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRasterPos4d(x: Double, y: Double, z: Double, w: Double) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRasterPos4dv(v: POINTER(Double)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRasterPos4f(x: Single, y: Single, z: Single, w: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRasterPos4fv(v: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRasterPos4i(x: Int32, y: Int32, z: Int32, w: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRasterPos4iv(v: POINTER(Int32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRasterPos4s(x: Int16, y: Int16, z: Int16, w: Int16) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRasterPos4sv(v: POINTER(Int16)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glReadBuffer(mode: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glReadPixels(x: Int32, y: Int32, width: Int32, height: Int32, format: UInt32, type: UInt32, pixels: VoidPtr) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRectd(x1: Double, y1: Double, x2: Double, y2: Double) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRectdv(v1: POINTER(Double), v2: POINTER(Double)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRectf(x1: Single, y1: Single, x2: Single, y2: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRectfv(v1: POINTER(Single), v2: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRecti(x1: Int32, y1: Int32, x2: Int32, y2: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRectiv(v1: POINTER(Int32), v2: POINTER(Int32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRects(x1: Int16, y1: Int16, x2: Int16, y2: Int16) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRectsv(v1: POINTER(Int16), v2: POINTER(Int16)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRenderMode(mode: UInt32) -> Int32: ...
@winfunctype('OPENGL32.dll')
def glRotated(angle: Double, x: Double, y: Double, z: Double) -> Void: ...
@winfunctype('OPENGL32.dll')
def glRotatef(angle: Single, x: Single, y: Single, z: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glScaled(x: Double, y: Double, z: Double) -> Void: ...
@winfunctype('OPENGL32.dll')
def glScalef(x: Single, y: Single, z: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glScissor(x: Int32, y: Int32, width: Int32, height: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glSelectBuffer(size: Int32, buffer: POINTER(UInt32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glShadeModel(mode: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glStencilFunc(func: UInt32, ref: Int32, mask: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glStencilMask(mask: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glStencilOp(fail: UInt32, zfail: UInt32, zpass: UInt32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord1d(s: Double) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord1dv(v: POINTER(Double)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord1f(s: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord1fv(v: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord1i(s: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord1iv(v: POINTER(Int32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord1s(s: Int16) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord1sv(v: POINTER(Int16)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord2d(s: Double, t: Double) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord2dv(v: POINTER(Double)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord2f(s: Single, t: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord2fv(v: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord2i(s: Int32, t: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord2iv(v: POINTER(Int32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord2s(s: Int16, t: Int16) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord2sv(v: POINTER(Int16)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord3d(s: Double, t: Double, r: Double) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord3dv(v: POINTER(Double)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord3f(s: Single, t: Single, r: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord3fv(v: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord3i(s: Int32, t: Int32, r: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord3iv(v: POINTER(Int32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord3s(s: Int16, t: Int16, r: Int16) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord3sv(v: POINTER(Int16)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord4d(s: Double, t: Double, r: Double, q: Double) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord4dv(v: POINTER(Double)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord4f(s: Single, t: Single, r: Single, q: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord4fv(v: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord4i(s: Int32, t: Int32, r: Int32, q: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord4iv(v: POINTER(Int32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord4s(s: Int16, t: Int16, r: Int16, q: Int16) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoord4sv(v: POINTER(Int16)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexCoordPointer(size: Int32, type: UInt32, stride: Int32, pointer: VoidPtr) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexEnvf(target: UInt32, pname: UInt32, param2: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexEnvfv(target: UInt32, pname: UInt32, params: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexEnvi(target: UInt32, pname: UInt32, param2: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexEnviv(target: UInt32, pname: UInt32, params: POINTER(Int32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexGend(coord: UInt32, pname: UInt32, param2: Double) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexGendv(coord: UInt32, pname: UInt32, params: POINTER(Double)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexGenf(coord: UInt32, pname: UInt32, param2: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexGenfv(coord: UInt32, pname: UInt32, params: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexGeni(coord: UInt32, pname: UInt32, param2: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexGeniv(coord: UInt32, pname: UInt32, params: POINTER(Int32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexImage1D(target: UInt32, level: Int32, internalformat: Int32, width: Int32, border: Int32, format: UInt32, type: UInt32, pixels: VoidPtr) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexImage2D(target: UInt32, level: Int32, internalformat: Int32, width: Int32, height: Int32, border: Int32, format: UInt32, type: UInt32, pixels: VoidPtr) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexParameterf(target: UInt32, pname: UInt32, param2: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexParameterfv(target: UInt32, pname: UInt32, params: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexParameteri(target: UInt32, pname: UInt32, param2: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexParameteriv(target: UInt32, pname: UInt32, params: POINTER(Int32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexSubImage1D(target: UInt32, level: Int32, xoffset: Int32, width: Int32, format: UInt32, type: UInt32, pixels: VoidPtr) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTexSubImage2D(target: UInt32, level: Int32, xoffset: Int32, yoffset: Int32, width: Int32, height: Int32, format: UInt32, type: UInt32, pixels: VoidPtr) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTranslated(x: Double, y: Double, z: Double) -> Void: ...
@winfunctype('OPENGL32.dll')
def glTranslatef(x: Single, y: Single, z: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glVertex2d(x: Double, y: Double) -> Void: ...
@winfunctype('OPENGL32.dll')
def glVertex2dv(v: POINTER(Double)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glVertex2f(x: Single, y: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glVertex2fv(v: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glVertex2i(x: Int32, y: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glVertex2iv(v: POINTER(Int32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glVertex2s(x: Int16, y: Int16) -> Void: ...
@winfunctype('OPENGL32.dll')
def glVertex2sv(v: POINTER(Int16)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glVertex3d(x: Double, y: Double, z: Double) -> Void: ...
@winfunctype('OPENGL32.dll')
def glVertex3dv(v: POINTER(Double)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glVertex3f(x: Single, y: Single, z: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glVertex3fv(v: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glVertex3i(x: Int32, y: Int32, z: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glVertex3iv(v: POINTER(Int32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glVertex3s(x: Int16, y: Int16, z: Int16) -> Void: ...
@winfunctype('OPENGL32.dll')
def glVertex3sv(v: POINTER(Int16)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glVertex4d(x: Double, y: Double, z: Double, w: Double) -> Void: ...
@winfunctype('OPENGL32.dll')
def glVertex4dv(v: POINTER(Double)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glVertex4f(x: Single, y: Single, z: Single, w: Single) -> Void: ...
@winfunctype('OPENGL32.dll')
def glVertex4fv(v: POINTER(Single)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glVertex4i(x: Int32, y: Int32, z: Int32, w: Int32) -> Void: ...
@winfunctype('OPENGL32.dll')
def glVertex4iv(v: POINTER(Int32)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glVertex4s(x: Int16, y: Int16, z: Int16, w: Int16) -> Void: ...
@winfunctype('OPENGL32.dll')
def glVertex4sv(v: POINTER(Int16)) -> Void: ...
@winfunctype('OPENGL32.dll')
def glVertexPointer(size: Int32, type: UInt32, stride: Int32, pointer: VoidPtr) -> Void: ...
@winfunctype('OPENGL32.dll')
def glViewport(x: Int32, y: Int32, width: Int32, height: Int32) -> Void: ...
@winfunctype('GLU32.dll')
def gluErrorString(errCode: UInt32) -> POINTER(Byte): ...
@winfunctype('GLU32.dll')
def gluErrorUnicodeStringEXT(errCode: UInt32) -> win32more.Windows.Win32.Foundation.PWSTR: ...
@winfunctype('GLU32.dll')
def gluGetString(name: UInt32) -> POINTER(Byte): ...
@winfunctype('GLU32.dll')
def gluOrtho2D(left: Double, right: Double, bottom: Double, top: Double) -> Void: ...
@winfunctype('GLU32.dll')
def gluPerspective(fovy: Double, aspect: Double, zNear: Double, zFar: Double) -> Void: ...
@winfunctype('GLU32.dll')
def gluPickMatrix(x: Double, y: Double, width: Double, height: Double, viewport: POINTER(Int32)) -> Void: ...
@winfunctype('GLU32.dll')
def gluLookAt(eyex: Double, eyey: Double, eyez: Double, centerx: Double, centery: Double, centerz: Double, upx: Double, upy: Double, upz: Double) -> Void: ...
@winfunctype('GLU32.dll')
def gluProject(objx: Double, objy: Double, objz: Double, modelMatrix: POINTER(Double), projMatrix: POINTER(Double), viewport: POINTER(Int32), winx: POINTER(Double), winy: POINTER(Double), winz: POINTER(Double)) -> Int32: ...
@winfunctype('GLU32.dll')
def gluUnProject(winx: Double, winy: Double, winz: Double, modelMatrix: POINTER(Double), projMatrix: POINTER(Double), viewport: POINTER(Int32), objx: POINTER(Double), objy: POINTER(Double), objz: POINTER(Double)) -> Int32: ...
@winfunctype('GLU32.dll')
def gluScaleImage(format: UInt32, widthin: Int32, heightin: Int32, typein: UInt32, datain: VoidPtr, widthout: Int32, heightout: Int32, typeout: UInt32, dataout: VoidPtr) -> Int32: ...
@winfunctype('GLU32.dll')
def gluBuild1DMipmaps(target: UInt32, components: Int32, width: Int32, format: UInt32, type: UInt32, data: VoidPtr) -> Int32: ...
@winfunctype('GLU32.dll')
def gluBuild2DMipmaps(target: UInt32, components: Int32, width: Int32, height: Int32, format: UInt32, type: UInt32, data: VoidPtr) -> Int32: ...
@winfunctype('GLU32.dll')
def gluNewQuadric() -> POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUquadric): ...
@winfunctype('GLU32.dll')
def gluDeleteQuadric(state: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUquadric)) -> Void: ...
@winfunctype('GLU32.dll')
def gluQuadricNormals(quadObject: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUquadric), normals: UInt32) -> Void: ...
@winfunctype('GLU32.dll')
def gluQuadricTexture(quadObject: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUquadric), textureCoords: Byte) -> Void: ...
@winfunctype('GLU32.dll')
def gluQuadricOrientation(quadObject: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUquadric), orientation: UInt32) -> Void: ...
@winfunctype('GLU32.dll')
def gluQuadricDrawStyle(quadObject: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUquadric), drawStyle: UInt32) -> Void: ...
@winfunctype('GLU32.dll')
def gluCylinder(qobj: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUquadric), baseRadius: Double, topRadius: Double, height: Double, slices: Int32, stacks: Int32) -> Void: ...
@winfunctype('GLU32.dll')
def gluDisk(qobj: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUquadric), innerRadius: Double, outerRadius: Double, slices: Int32, loops: Int32) -> Void: ...
@winfunctype('GLU32.dll')
def gluPartialDisk(qobj: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUquadric), innerRadius: Double, outerRadius: Double, slices: Int32, loops: Int32, startAngle: Double, sweepAngle: Double) -> Void: ...
@winfunctype('GLU32.dll')
def gluSphere(qobj: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUquadric), radius: Double, slices: Int32, stacks: Int32) -> Void: ...
@winfunctype('GLU32.dll')
def gluQuadricCallback(qobj: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUquadric), which: UInt32, fn: IntPtr) -> Void: ...
@winfunctype('GLU32.dll')
def gluNewTess() -> POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUtesselator): ...
@winfunctype('GLU32.dll')
def gluDeleteTess(tess: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUtesselator)) -> Void: ...
@winfunctype('GLU32.dll')
def gluTessBeginPolygon(tess: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUtesselator), polygon_data: VoidPtr) -> Void: ...
@winfunctype('GLU32.dll')
def gluTessBeginContour(tess: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUtesselator)) -> Void: ...
@winfunctype('GLU32.dll')
def gluTessVertex(tess: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUtesselator), coords: POINTER(Double), data: VoidPtr) -> Void: ...
@winfunctype('GLU32.dll')
def gluTessEndContour(tess: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUtesselator)) -> Void: ...
@winfunctype('GLU32.dll')
def gluTessEndPolygon(tess: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUtesselator)) -> Void: ...
@winfunctype('GLU32.dll')
def gluTessProperty(tess: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUtesselator), which: UInt32, value: Double) -> Void: ...
@winfunctype('GLU32.dll')
def gluTessNormal(tess: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUtesselator), x: Double, y: Double, z: Double) -> Void: ...
@winfunctype('GLU32.dll')
def gluTessCallback(tess: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUtesselator), which: UInt32, fn: IntPtr) -> Void: ...
@winfunctype('GLU32.dll')
def gluGetTessProperty(tess: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUtesselator), which: UInt32, value: POINTER(Double)) -> Void: ...
@winfunctype('GLU32.dll')
def gluNewNurbsRenderer() -> POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUnurbs): ...
@winfunctype('GLU32.dll')
def gluDeleteNurbsRenderer(nobj: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUnurbs)) -> Void: ...
@winfunctype('GLU32.dll')
def gluBeginSurface(nobj: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUnurbs)) -> Void: ...
@winfunctype('GLU32.dll')
def gluBeginCurve(nobj: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUnurbs)) -> Void: ...
@winfunctype('GLU32.dll')
def gluEndCurve(nobj: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUnurbs)) -> Void: ...
@winfunctype('GLU32.dll')
def gluEndSurface(nobj: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUnurbs)) -> Void: ...
@winfunctype('GLU32.dll')
def gluBeginTrim(nobj: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUnurbs)) -> Void: ...
@winfunctype('GLU32.dll')
def gluEndTrim(nobj: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUnurbs)) -> Void: ...
@winfunctype('GLU32.dll')
def gluPwlCurve(nobj: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUnurbs), count: Int32, array: POINTER(Single), stride: Int32, type: UInt32) -> Void: ...
@winfunctype('GLU32.dll')
def gluNurbsCurve(nobj: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUnurbs), nknots: Int32, knot: POINTER(Single), stride: Int32, ctlarray: POINTER(Single), order: Int32, type: UInt32) -> Void: ...
@winfunctype('GLU32.dll')
def gluNurbsSurface(nobj: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUnurbs), sknot_count: Int32, sknot: POINTER(Single), tknot_count: Int32, tknot: POINTER(Single), s_stride: Int32, t_stride: Int32, ctlarray: POINTER(Single), sorder: Int32, torder: Int32, type: UInt32) -> Void: ...
@winfunctype('GLU32.dll')
def gluLoadSamplingMatrices(nobj: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUnurbs), modelMatrix: POINTER(Single), projMatrix: POINTER(Single), viewport: POINTER(Int32)) -> Void: ...
@winfunctype('GLU32.dll')
def gluNurbsProperty(nobj: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUnurbs), property: UInt32, value: Single) -> Void: ...
@winfunctype('GLU32.dll')
def gluGetNurbsProperty(nobj: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUnurbs), property: UInt32, value: POINTER(Single)) -> Void: ...
@winfunctype('GLU32.dll')
def gluNurbsCallback(nobj: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUnurbs), which: UInt32, fn: IntPtr) -> Void: ...
@winfunctype('GLU32.dll')
def gluBeginPolygon(tess: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUtesselator)) -> Void: ...
@winfunctype('GLU32.dll')
def gluNextContour(tess: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUtesselator), type: UInt32) -> Void: ...
@winfunctype('GLU32.dll')
def gluEndPolygon(tess: POINTER(win32more.Windows.Win32.Graphics.OpenGL.GLUtesselator)) -> Void: ...
class EMRPIXELFORMAT(Structure):
    emr: win32more.Windows.Win32.Graphics.Gdi.EMR
    pfd: win32more.Windows.Win32.Graphics.OpenGL.PIXELFORMATDESCRIPTOR
GLUnurbs = IntPtr
@winfunctype_pointer
def GLUnurbsErrorProc(param0: UInt32) -> Void: ...
GLUquadric = IntPtr
@winfunctype_pointer
def GLUquadricErrorProc(param0: UInt32) -> Void: ...
@winfunctype_pointer
def GLUtessBeginDataProc(param0: UInt32, param1: VoidPtr) -> Void: ...
@winfunctype_pointer
def GLUtessBeginProc(param0: UInt32) -> Void: ...
@winfunctype_pointer
def GLUtessCombineDataProc(param0: POINTER(Double), param1: POINTER(VoidPtr), param2: POINTER(Single), param3: POINTER(VoidPtr), param4: VoidPtr) -> Void: ...
@winfunctype_pointer
def GLUtessCombineProc(param0: POINTER(Double), param1: POINTER(VoidPtr), param2: POINTER(Single), param3: POINTER(VoidPtr)) -> Void: ...
@winfunctype_pointer
def GLUtessEdgeFlagDataProc(param0: Byte, param1: VoidPtr) -> Void: ...
@winfunctype_pointer
def GLUtessEdgeFlagProc(param0: Byte) -> Void: ...
@winfunctype_pointer
def GLUtessEndDataProc(param0: VoidPtr) -> Void: ...
@winfunctype_pointer
def GLUtessEndProc() -> Void: ...
@winfunctype_pointer
def GLUtessErrorDataProc(param0: UInt32, param1: VoidPtr) -> Void: ...
@winfunctype_pointer
def GLUtessErrorProc(param0: UInt32) -> Void: ...
@winfunctype_pointer
def GLUtessVertexDataProc(param0: VoidPtr, param1: VoidPtr) -> Void: ...
@winfunctype_pointer
def GLUtessVertexProc(param0: VoidPtr) -> Void: ...
GLUtesselator = IntPtr
class GLYPHMETRICSFLOAT(Structure):
    gmfBlackBoxX: Single
    gmfBlackBoxY: Single
    gmfptGlyphOrigin: win32more.Windows.Win32.Graphics.OpenGL.POINTFLOAT
    gmfCellIncX: Single
    gmfCellIncY: Single
HGLRC = VoidPtr
class LAYERPLANEDESCRIPTOR(Structure):
    nSize: UInt16
    nVersion: UInt16
    dwFlags: UInt32
    iPixelType: Byte
    cColorBits: Byte
    cRedBits: Byte
    cRedShift: Byte
    cGreenBits: Byte
    cGreenShift: Byte
    cBlueBits: Byte
    cBlueShift: Byte
    cAlphaBits: Byte
    cAlphaShift: Byte
    cAccumBits: Byte
    cAccumRedBits: Byte
    cAccumGreenBits: Byte
    cAccumBlueBits: Byte
    cAccumAlphaBits: Byte
    cDepthBits: Byte
    cStencilBits: Byte
    cAuxBuffers: Byte
    iLayerPlane: Byte
    bReserved: Byte
    crTransparent: win32more.Windows.Win32.Foundation.COLORREF
PFD_FLAGS = UInt32
PFD_DOUBLEBUFFER: win32more.Windows.Win32.Graphics.OpenGL.PFD_FLAGS = 1
PFD_STEREO: win32more.Windows.Win32.Graphics.OpenGL.PFD_FLAGS = 2
PFD_DRAW_TO_WINDOW: win32more.Windows.Win32.Graphics.OpenGL.PFD_FLAGS = 4
PFD_DRAW_TO_BITMAP: win32more.Windows.Win32.Graphics.OpenGL.PFD_FLAGS = 8
PFD_SUPPORT_GDI: win32more.Windows.Win32.Graphics.OpenGL.PFD_FLAGS = 16
PFD_SUPPORT_OPENGL: win32more.Windows.Win32.Graphics.OpenGL.PFD_FLAGS = 32
PFD_GENERIC_FORMAT: win32more.Windows.Win32.Graphics.OpenGL.PFD_FLAGS = 64
PFD_NEED_PALETTE: win32more.Windows.Win32.Graphics.OpenGL.PFD_FLAGS = 128
PFD_NEED_SYSTEM_PALETTE: win32more.Windows.Win32.Graphics.OpenGL.PFD_FLAGS = 256
PFD_SWAP_EXCHANGE: win32more.Windows.Win32.Graphics.OpenGL.PFD_FLAGS = 512
PFD_SWAP_COPY: win32more.Windows.Win32.Graphics.OpenGL.PFD_FLAGS = 1024
PFD_SWAP_LAYER_BUFFERS: win32more.Windows.Win32.Graphics.OpenGL.PFD_FLAGS = 2048
PFD_GENERIC_ACCELERATED: win32more.Windows.Win32.Graphics.OpenGL.PFD_FLAGS = 4096
PFD_SUPPORT_DIRECTDRAW: win32more.Windows.Win32.Graphics.OpenGL.PFD_FLAGS = 8192
PFD_DIRECT3D_ACCELERATED: win32more.Windows.Win32.Graphics.OpenGL.PFD_FLAGS = 16384
PFD_SUPPORT_COMPOSITION: win32more.Windows.Win32.Graphics.OpenGL.PFD_FLAGS = 32768
PFD_DEPTH_DONTCARE: win32more.Windows.Win32.Graphics.OpenGL.PFD_FLAGS = 536870912
PFD_DOUBLEBUFFER_DONTCARE: win32more.Windows.Win32.Graphics.OpenGL.PFD_FLAGS = 1073741824
PFD_STEREO_DONTCARE: win32more.Windows.Win32.Graphics.OpenGL.PFD_FLAGS = 2147483648
PFD_LAYER_TYPE = SByte
PFD_UNDERLAY_PLANE: win32more.Windows.Win32.Graphics.OpenGL.PFD_LAYER_TYPE = -1
PFD_MAIN_PLANE: win32more.Windows.Win32.Graphics.OpenGL.PFD_LAYER_TYPE = 0
PFD_OVERLAY_PLANE: win32more.Windows.Win32.Graphics.OpenGL.PFD_LAYER_TYPE = 1
PFD_PIXEL_TYPE = Byte
PFD_TYPE_RGBA: win32more.Windows.Win32.Graphics.OpenGL.PFD_PIXEL_TYPE = 0
PFD_TYPE_COLORINDEX: win32more.Windows.Win32.Graphics.OpenGL.PFD_PIXEL_TYPE = 1
@winfunctype_pointer
def PFNGLADDSWAPHINTRECTWINPROC(x: Int32, y: Int32, width: Int32, height: Int32) -> Void: ...
@winfunctype_pointer
def PFNGLARRAYELEMENTARRAYEXTPROC(mode: UInt32, count: Int32, pi: VoidPtr) -> Void: ...
@winfunctype_pointer
def PFNGLARRAYELEMENTEXTPROC(i: Int32) -> Void: ...
@winfunctype_pointer
def PFNGLCOLORPOINTEREXTPROC(size: Int32, type: UInt32, stride: Int32, count: Int32, pointer: VoidPtr) -> Void: ...
@winfunctype_pointer
def PFNGLCOLORSUBTABLEEXTPROC(target: UInt32, start: Int32, count: Int32, format: UInt32, type: UInt32, data: VoidPtr) -> Void: ...
@winfunctype_pointer
def PFNGLCOLORTABLEEXTPROC(target: UInt32, internalFormat: UInt32, width: Int32, format: UInt32, type: UInt32, data: VoidPtr) -> Void: ...
@winfunctype_pointer
def PFNGLDRAWARRAYSEXTPROC(mode: UInt32, first: Int32, count: Int32) -> Void: ...
@winfunctype_pointer
def PFNGLDRAWRANGEELEMENTSWINPROC(mode: UInt32, start: UInt32, end: UInt32, count: Int32, type: UInt32, indices: VoidPtr) -> Void: ...
@winfunctype_pointer
def PFNGLEDGEFLAGPOINTEREXTPROC(stride: Int32, count: Int32, pointer: POINTER(Byte)) -> Void: ...
@winfunctype_pointer
def PFNGLGETCOLORTABLEEXTPROC(target: UInt32, format: UInt32, type: UInt32, data: VoidPtr) -> Void: ...
@winfunctype_pointer
def PFNGLGETCOLORTABLEPARAMETERFVEXTPROC(target: UInt32, pname: UInt32, params: POINTER(Single)) -> Void: ...
@winfunctype_pointer
def PFNGLGETCOLORTABLEPARAMETERIVEXTPROC(target: UInt32, pname: UInt32, params: POINTER(Int32)) -> Void: ...
@winfunctype_pointer
def PFNGLGETPOINTERVEXTPROC(pname: UInt32, params: POINTER(VoidPtr)) -> Void: ...
@winfunctype_pointer
def PFNGLINDEXPOINTEREXTPROC(type: UInt32, stride: Int32, count: Int32, pointer: VoidPtr) -> Void: ...
@winfunctype_pointer
def PFNGLNORMALPOINTEREXTPROC(type: UInt32, stride: Int32, count: Int32, pointer: VoidPtr) -> Void: ...
@winfunctype_pointer
def PFNGLTEXCOORDPOINTEREXTPROC(size: Int32, type: UInt32, stride: Int32, count: Int32, pointer: VoidPtr) -> Void: ...
@winfunctype_pointer
def PFNGLVERTEXPOINTEREXTPROC(size: Int32, type: UInt32, stride: Int32, count: Int32, pointer: VoidPtr) -> Void: ...
class PIXELFORMATDESCRIPTOR(Structure):
    nSize: UInt16
    nVersion: UInt16
    dwFlags: win32more.Windows.Win32.Graphics.OpenGL.PFD_FLAGS
    iPixelType: win32more.Windows.Win32.Graphics.OpenGL.PFD_PIXEL_TYPE
    cColorBits: Byte
    cRedBits: Byte
    cRedShift: Byte
    cGreenBits: Byte
    cGreenShift: Byte
    cBlueBits: Byte
    cBlueShift: Byte
    cAlphaBits: Byte
    cAlphaShift: Byte
    cAccumBits: Byte
    cAccumRedBits: Byte
    cAccumGreenBits: Byte
    cAccumBlueBits: Byte
    cAccumAlphaBits: Byte
    cDepthBits: Byte
    cStencilBits: Byte
    cAuxBuffers: Byte
    iLayerType: Byte
    bReserved: Byte
    dwLayerMask: UInt32
    dwVisibleMask: UInt32
    dwDamageMask: UInt32
class POINTFLOAT(Structure):
    x: Single
    y: Single


make_ready(__name__)
