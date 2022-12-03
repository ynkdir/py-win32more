from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.Gdi
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
def _define_ABC_head():
    class ABC(Structure):
        pass
    return ABC
def _define_ABC():
    ABC = win32more.Graphics.Gdi.ABC_head
    ABC._fields_ = [
        ('abcA', Int32),
        ('abcB', UInt32),
        ('abcC', Int32),
    ]
    return ABC
def _define_ABCFLOAT_head():
    class ABCFLOAT(Structure):
        pass
    return ABCFLOAT
def _define_ABCFLOAT():
    ABCFLOAT = win32more.Graphics.Gdi.ABCFLOAT_head
    ABCFLOAT._fields_ = [
        ('abcfA', Single),
        ('abcfB', Single),
        ('abcfC', Single),
    ]
    return ABCFLOAT
def _define_ABORTPATH_head():
    class ABORTPATH(Structure):
        pass
    return ABORTPATH
def _define_ABORTPATH():
    ABORTPATH = win32more.Graphics.Gdi.ABORTPATH_head
    ABORTPATH._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
    ]
    return ABORTPATH
GDI_ERROR = -1
ERROR = 0
MAXSTRETCHBLTMODE = 4
POLYFILL_LAST = 2
LAYOUT_BTT = 2
LAYOUT_VBH = 4
ASPECT_FILTERING = 1
META_SETBKCOLOR = 513
META_SETBKMODE = 258
META_SETMAPMODE = 259
META_SETROP2 = 260
META_SETRELABS = 261
META_SETPOLYFILLMODE = 262
META_SETSTRETCHBLTMODE = 263
META_SETTEXTCHAREXTRA = 264
META_SETTEXTCOLOR = 521
META_SETTEXTJUSTIFICATION = 522
META_SETWINDOWORG = 523
META_SETWINDOWEXT = 524
META_SETVIEWPORTORG = 525
META_SETVIEWPORTEXT = 526
META_OFFSETWINDOWORG = 527
META_SCALEWINDOWEXT = 1040
META_OFFSETVIEWPORTORG = 529
META_SCALEVIEWPORTEXT = 1042
META_LINETO = 531
META_MOVETO = 532
META_EXCLUDECLIPRECT = 1045
META_INTERSECTCLIPRECT = 1046
META_ARC = 2071
META_ELLIPSE = 1048
META_FLOODFILL = 1049
META_PIE = 2074
META_RECTANGLE = 1051
META_ROUNDRECT = 1564
META_PATBLT = 1565
META_SAVEDC = 30
META_SETPIXEL = 1055
META_OFFSETCLIPRGN = 544
META_TEXTOUT = 1313
META_BITBLT = 2338
META_STRETCHBLT = 2851
META_POLYGON = 804
META_POLYLINE = 805
META_ESCAPE = 1574
META_RESTOREDC = 295
META_FILLREGION = 552
META_FRAMEREGION = 1065
META_INVERTREGION = 298
META_PAINTREGION = 299
META_SELECTCLIPREGION = 300
META_SELECTOBJECT = 301
META_SETTEXTALIGN = 302
META_CHORD = 2096
META_SETMAPPERFLAGS = 561
META_EXTTEXTOUT = 2610
META_SETDIBTODEV = 3379
META_SELECTPALETTE = 564
META_REALIZEPALETTE = 53
META_ANIMATEPALETTE = 1078
META_SETPALENTRIES = 55
META_POLYPOLYGON = 1336
META_RESIZEPALETTE = 313
META_DIBBITBLT = 2368
META_DIBSTRETCHBLT = 2881
META_DIBCREATEPATTERNBRUSH = 322
META_STRETCHDIB = 3907
META_EXTFLOODFILL = 1352
META_SETLAYOUT = 329
META_DELETEOBJECT = 496
META_CREATEPALETTE = 247
META_CREATEPATTERNBRUSH = 505
META_CREATEPENINDIRECT = 762
META_CREATEFONTINDIRECT = 763
META_CREATEBRUSHINDIRECT = 764
META_CREATEREGION = 1791
NEWFRAME = 1
ABORTDOC = 2
NEXTBAND = 3
SETCOLORTABLE = 4
GETCOLORTABLE = 5
FLUSHOUTPUT = 6
DRAFTMODE = 7
QUERYESCSUPPORT = 8
SETABORTPROC = 9
STARTDOC = 10
ENDDOC = 11
GETPHYSPAGESIZE = 12
GETPRINTINGOFFSET = 13
GETSCALINGFACTOR = 14
MFCOMMENT = 15
GETPENWIDTH = 16
SETCOPYCOUNT = 17
SELECTPAPERSOURCE = 18
DEVICEDATA = 19
PASSTHROUGH = 19
GETTECHNOLGY = 20
GETTECHNOLOGY = 20
SETLINECAP = 21
SETLINEJOIN = 22
SETMITERLIMIT = 23
BANDINFO = 24
DRAWPATTERNRECT = 25
GETVECTORPENSIZE = 26
GETVECTORBRUSHSIZE = 27
ENABLEDUPLEX = 28
GETSETPAPERBINS = 29
GETSETPRINTORIENT = 30
ENUMPAPERBINS = 31
SETDIBSCALING = 32
EPSPRINTING = 33
ENUMPAPERMETRICS = 34
GETSETPAPERMETRICS = 35
POSTSCRIPT_DATA = 37
POSTSCRIPT_IGNORE = 38
MOUSETRAILS = 39
GETDEVICEUNITS = 42
GETEXTENDEDTEXTMETRICS = 256
GETEXTENTTABLE = 257
GETPAIRKERNTABLE = 258
GETTRACKKERNTABLE = 259
EXTTEXTOUT = 512
GETFACENAME = 513
DOWNLOADFACE = 514
ENABLERELATIVEWIDTHS = 768
ENABLEPAIRKERNING = 769
SETKERNTRACK = 770
SETALLJUSTVALUES = 771
SETCHARSET = 772
STRETCHBLT = 2048
METAFILE_DRIVER = 2049
GETSETSCREENPARAMS = 3072
QUERYDIBSUPPORT = 3073
BEGIN_PATH = 4096
CLIP_TO_PATH = 4097
END_PATH = 4098
EXT_DEVICE_CAPS = 4099
RESTORE_CTM = 4100
SAVE_CTM = 4101
SET_ARC_DIRECTION = 4102
SET_BACKGROUND_COLOR = 4103
SET_POLY_MODE = 4104
SET_SCREEN_ANGLE = 4105
SET_SPREAD = 4106
TRANSFORM_CTM = 4107
SET_CLIP_BOX = 4108
SET_BOUNDS = 4109
SET_MIRROR_MODE = 4110
OPENCHANNEL = 4110
DOWNLOADHEADER = 4111
CLOSECHANNEL = 4112
POSTSCRIPT_PASSTHROUGH = 4115
ENCAPSULATED_POSTSCRIPT = 4116
POSTSCRIPT_IDENTIFY = 4117
POSTSCRIPT_INJECTION = 4118
CHECKJPEGFORMAT = 4119
CHECKPNGFORMAT = 4120
GET_PS_FEATURESETTING = 4121
GDIPLUS_TS_QUERYVER = 4122
GDIPLUS_TS_RECORD = 4123
MILCORE_TS_QUERYVER_RESULT_FALSE = 0
MILCORE_TS_QUERYVER_RESULT_TRUE = 2147483647
SPCLPASSTHROUGH2 = 4568
PSIDENT_GDICENTRIC = 0
PSIDENT_PSCENTRIC = 1
PSINJECT_DLFONT = 3722304989
FEATURESETTING_NUP = 0
FEATURESETTING_OUTPUT = 1
FEATURESETTING_PSLEVEL = 2
FEATURESETTING_CUSTPAPER = 3
FEATURESETTING_MIRROR = 4
FEATURESETTING_NEGATIVE = 5
FEATURESETTING_PROTOCOL = 6
FEATURESETTING_PRIVATE_BEGIN = 4096
FEATURESETTING_PRIVATE_END = 8191
PSPROTOCOL_ASCII = 0
PSPROTOCOL_BCP = 1
PSPROTOCOL_TBCP = 2
PSPROTOCOL_BINARY = 3
QDI_SETDIBITS = 1
QDI_GETDIBITS = 2
QDI_DIBTOSCREEN = 4
QDI_STRETCHDIB = 8
SP_NOTREPORTED = 16384
SP_ERROR = -1
SP_APPABORT = -2
SP_USERABORT = -3
SP_OUTOFDISK = -4
SP_OUTOFMEMORY = -5
PR_JOBSTATUS = 0
LCS_CALIBRATED_RGB = 0
LCS_GM_BUSINESS = 1
LCS_GM_GRAPHICS = 2
LCS_GM_IMAGES = 4
LCS_GM_ABS_COLORIMETRIC = 8
CM_OUT_OF_GAMUT = 255
CM_IN_GAMUT = 0
NTM_REGULAR = 64
NTM_BOLD = 32
NTM_ITALIC = 1
NTM_NONNEGATIVE_AC = 65536
NTM_PS_OPENTYPE = 131072
NTM_TT_OPENTYPE = 262144
NTM_MULTIPLEMASTER = 524288
NTM_TYPE1 = 1048576
NTM_DSIG = 2097152
LF_FACESIZE = 32
LF_FULLFACESIZE = 64
CLEARTYPE_NATURAL_QUALITY = 6
MONO_FONT = 8
FS_LATIN1 = 1
FS_LATIN2 = 2
FS_CYRILLIC = 4
FS_GREEK = 8
FS_TURKISH = 16
FS_HEBREW = 32
FS_ARABIC = 64
FS_BALTIC = 128
FS_VIETNAMESE = 256
FS_THAI = 65536
FS_JISJAPAN = 131072
FS_CHINESESIMP = 262144
FS_WANSUNG = 524288
FS_CHINESETRAD = 1048576
FS_JOHAB = 2097152
FS_SYMBOL = -2147483648
PANOSE_COUNT = 10
PAN_FAMILYTYPE_INDEX = 0
PAN_SERIFSTYLE_INDEX = 1
PAN_PROPORTION_INDEX = 3
PAN_STROKEVARIATION_INDEX = 5
PAN_ARMSTYLE_INDEX = 6
PAN_LETTERFORM_INDEX = 7
PAN_CULTURE_LATIN = 0
PAN_ANY = 0
PAN_NO_FIT = 1
ELF_VENDOR_SIZE = 4
ELF_VERSION = 0
ELF_CULTURE_LATIN = 0
RASTER_FONTTYPE = 1
DEVICE_FONTTYPE = 2
TRUETYPE_FONTTYPE = 4
PC_RESERVED = 1
PC_EXPLICIT = 2
PC_NOCOLLAPSE = 4
BKMODE_LAST = 2
GM_LAST = 2
PT_CLOSEFIGURE = 1
PT_LINETO = 2
PT_BEZIERTO = 4
PT_MOVETO = 6
ABSOLUTE = 1
RELATIVE = 2
STOCK_LAST = 19
CLR_INVALID = 4294967295
HS_API_MAX = 12
DT_PLOTTER = 0
DT_RASDISPLAY = 1
DT_RASPRINTER = 2
DT_RASCAMERA = 3
DT_CHARSTREAM = 4
DT_METAFILE = 5
DT_DISPFILE = 6
CC_NONE = 0
CC_CIRCLES = 1
CC_PIE = 2
CC_CHORD = 4
CC_ELLIPSES = 8
CC_WIDE = 16
CC_STYLED = 32
CC_WIDESTYLED = 64
CC_INTERIORS = 128
CC_ROUNDRECT = 256
LC_NONE = 0
LC_POLYLINE = 2
LC_MARKER = 4
LC_POLYMARKER = 8
LC_WIDE = 16
LC_STYLED = 32
LC_WIDESTYLED = 64
LC_INTERIORS = 128
PC_NONE = 0
PC_POLYGON = 1
PC_RECTANGLE = 2
PC_WINDPOLYGON = 4
PC_TRAPEZOID = 4
PC_SCANLINE = 8
PC_WIDE = 16
PC_STYLED = 32
PC_WIDESTYLED = 64
PC_INTERIORS = 128
PC_POLYPOLYGON = 256
PC_PATHS = 512
CP_NONE = 0
CP_RECTANGLE = 1
CP_REGION = 2
TC_OP_CHARACTER = 1
TC_OP_STROKE = 2
TC_CP_STROKE = 4
TC_CR_90 = 8
TC_CR_ANY = 16
TC_SF_X_YINDEP = 32
TC_SA_DOUBLE = 64
TC_SA_INTEGER = 128
TC_SA_CONTIN = 256
TC_EA_DOUBLE = 512
TC_IA_ABLE = 1024
TC_UA_ABLE = 2048
TC_SO_ABLE = 4096
TC_RA_ABLE = 8192
TC_VA_ABLE = 16384
TC_RESERVED = 32768
TC_SCROLLBLT = 65536
RC_BITBLT = 1
RC_BANDING = 2
RC_SCALING = 4
RC_BITMAP64 = 8
RC_GDI20_OUTPUT = 16
RC_GDI20_STATE = 32
RC_SAVEBITMAP = 64
RC_DI_BITMAP = 128
RC_PALETTE = 256
RC_DIBTODEV = 512
RC_BIGFONT = 1024
RC_STRETCHBLT = 2048
RC_FLOODFILL = 4096
RC_STRETCHDIB = 8192
RC_OP_DX_OUTPUT = 16384
RC_DEVBITS = 32768
SB_NONE = 0
SB_CONST_ALPHA = 1
SB_PIXEL_ALPHA = 2
SB_PREMULT_ALPHA = 4
SB_GRAD_RECT = 16
SB_GRAD_TRI = 32
CM_NONE = 0
CM_DEVICE_ICM = 1
CM_GAMMA_RAMP = 2
CM_CMYK_COLOR = 4
SYSPAL_ERROR = 0
CBM_INIT = 4
CCHFORMNAME = 32
DMORIENT_PORTRAIT = 1
DMORIENT_LANDSCAPE = 2
DMPAPER_LETTER = 1
DMPAPER_LETTERSMALL = 2
DMPAPER_TABLOID = 3
DMPAPER_LEDGER = 4
DMPAPER_LEGAL = 5
DMPAPER_STATEMENT = 6
DMPAPER_EXECUTIVE = 7
DMPAPER_A3 = 8
DMPAPER_A4 = 9
DMPAPER_A4SMALL = 10
DMPAPER_A5 = 11
DMPAPER_B4 = 12
DMPAPER_B5 = 13
DMPAPER_FOLIO = 14
DMPAPER_QUARTO = 15
DMPAPER_10X14 = 16
DMPAPER_11X17 = 17
DMPAPER_NOTE = 18
DMPAPER_ENV_9 = 19
DMPAPER_ENV_10 = 20
DMPAPER_ENV_11 = 21
DMPAPER_ENV_12 = 22
DMPAPER_ENV_14 = 23
DMPAPER_CSHEET = 24
DMPAPER_DSHEET = 25
DMPAPER_ESHEET = 26
DMPAPER_ENV_DL = 27
DMPAPER_ENV_C5 = 28
DMPAPER_ENV_C3 = 29
DMPAPER_ENV_C4 = 30
DMPAPER_ENV_C6 = 31
DMPAPER_ENV_C65 = 32
DMPAPER_ENV_B4 = 33
DMPAPER_ENV_B5 = 34
DMPAPER_ENV_B6 = 35
DMPAPER_ENV_ITALY = 36
DMPAPER_ENV_MONARCH = 37
DMPAPER_ENV_PERSONAL = 38
DMPAPER_FANFOLD_US = 39
DMPAPER_FANFOLD_STD_GERMAN = 40
DMPAPER_FANFOLD_LGL_GERMAN = 41
DMPAPER_ISO_B4 = 42
DMPAPER_JAPANESE_POSTCARD = 43
DMPAPER_9X11 = 44
DMPAPER_10X11 = 45
DMPAPER_15X11 = 46
DMPAPER_ENV_INVITE = 47
DMPAPER_RESERVED_48 = 48
DMPAPER_RESERVED_49 = 49
DMPAPER_LETTER_EXTRA = 50
DMPAPER_LEGAL_EXTRA = 51
DMPAPER_TABLOID_EXTRA = 52
DMPAPER_A4_EXTRA = 53
DMPAPER_LETTER_TRANSVERSE = 54
DMPAPER_A4_TRANSVERSE = 55
DMPAPER_LETTER_EXTRA_TRANSVERSE = 56
DMPAPER_A_PLUS = 57
DMPAPER_B_PLUS = 58
DMPAPER_LETTER_PLUS = 59
DMPAPER_A4_PLUS = 60
DMPAPER_A5_TRANSVERSE = 61
DMPAPER_B5_TRANSVERSE = 62
DMPAPER_A3_EXTRA = 63
DMPAPER_A5_EXTRA = 64
DMPAPER_B5_EXTRA = 65
DMPAPER_A2 = 66
DMPAPER_A3_TRANSVERSE = 67
DMPAPER_A3_EXTRA_TRANSVERSE = 68
DMPAPER_DBL_JAPANESE_POSTCARD = 69
DMPAPER_A6 = 70
DMPAPER_JENV_KAKU2 = 71
DMPAPER_JENV_KAKU3 = 72
DMPAPER_JENV_CHOU3 = 73
DMPAPER_JENV_CHOU4 = 74
DMPAPER_LETTER_ROTATED = 75
DMPAPER_A3_ROTATED = 76
DMPAPER_A4_ROTATED = 77
DMPAPER_A5_ROTATED = 78
DMPAPER_B4_JIS_ROTATED = 79
DMPAPER_B5_JIS_ROTATED = 80
DMPAPER_JAPANESE_POSTCARD_ROTATED = 81
DMPAPER_DBL_JAPANESE_POSTCARD_ROTATED = 82
DMPAPER_A6_ROTATED = 83
DMPAPER_JENV_KAKU2_ROTATED = 84
DMPAPER_JENV_KAKU3_ROTATED = 85
DMPAPER_JENV_CHOU3_ROTATED = 86
DMPAPER_JENV_CHOU4_ROTATED = 87
DMPAPER_B6_JIS = 88
DMPAPER_B6_JIS_ROTATED = 89
DMPAPER_12X11 = 90
DMPAPER_JENV_YOU4 = 91
DMPAPER_JENV_YOU4_ROTATED = 92
DMPAPER_P16K = 93
DMPAPER_P32K = 94
DMPAPER_P32KBIG = 95
DMPAPER_PENV_1 = 96
DMPAPER_PENV_2 = 97
DMPAPER_PENV_3 = 98
DMPAPER_PENV_4 = 99
DMPAPER_PENV_5 = 100
DMPAPER_PENV_6 = 101
DMPAPER_PENV_7 = 102
DMPAPER_PENV_8 = 103
DMPAPER_PENV_9 = 104
DMPAPER_PENV_10 = 105
DMPAPER_P16K_ROTATED = 106
DMPAPER_P32K_ROTATED = 107
DMPAPER_P32KBIG_ROTATED = 108
DMPAPER_PENV_1_ROTATED = 109
DMPAPER_PENV_2_ROTATED = 110
DMPAPER_PENV_3_ROTATED = 111
DMPAPER_PENV_4_ROTATED = 112
DMPAPER_PENV_5_ROTATED = 113
DMPAPER_PENV_6_ROTATED = 114
DMPAPER_PENV_7_ROTATED = 115
DMPAPER_PENV_8_ROTATED = 116
DMPAPER_PENV_9_ROTATED = 117
DMPAPER_PENV_10_ROTATED = 118
DMPAPER_LAST = 118
DMPAPER_USER = 256
DMBIN_UPPER = 1
DMBIN_ONLYONE = 1
DMBIN_LOWER = 2
DMBIN_MIDDLE = 3
DMBIN_MANUAL = 4
DMBIN_ENVELOPE = 5
DMBIN_ENVMANUAL = 6
DMBIN_AUTO = 7
DMBIN_TRACTOR = 8
DMBIN_SMALLFMT = 9
DMBIN_LARGEFMT = 10
DMBIN_LARGECAPACITY = 11
DMBIN_CASSETTE = 14
DMBIN_FORMSOURCE = 15
DMBIN_LAST = 15
DMBIN_USER = 256
DMRES_DRAFT = -1
DMRES_LOW = -2
DMRES_MEDIUM = -3
DMRES_HIGH = -4
DMDISPLAYFLAGS_TEXTMODE = 4
DMNUP_SYSTEM = 1
DMNUP_ONEUP = 2
DMICMMETHOD_NONE = 1
DMICMMETHOD_SYSTEM = 2
DMICMMETHOD_DRIVER = 3
DMICMMETHOD_DEVICE = 4
DMICMMETHOD_USER = 256
DMICM_SATURATE = 1
DMICM_CONTRAST = 2
DMICM_COLORIMETRIC = 3
DMICM_ABS_COLORIMETRIC = 4
DMICM_USER = 256
DMMEDIA_STANDARD = 1
DMMEDIA_TRANSPARENCY = 2
DMMEDIA_GLOSSY = 3
DMMEDIA_USER = 256
DMDITHER_NONE = 1
DMDITHER_COARSE = 2
DMDITHER_FINE = 3
DMDITHER_LINEART = 4
DMDITHER_ERRORDIFFUSION = 5
DMDITHER_RESERVED6 = 6
DMDITHER_RESERVED7 = 7
DMDITHER_RESERVED8 = 8
DMDITHER_RESERVED9 = 9
DMDITHER_GRAYSCALE = 10
DMDITHER_USER = 256
DISPLAY_DEVICE_ATTACHED_TO_DESKTOP = 1
DISPLAY_DEVICE_MULTI_DRIVER = 2
DISPLAY_DEVICE_PRIMARY_DEVICE = 4
DISPLAY_DEVICE_MIRRORING_DRIVER = 8
DISPLAY_DEVICE_VGA_COMPATIBLE = 16
DISPLAY_DEVICE_REMOVABLE = 32
DISPLAY_DEVICE_ACC_DRIVER = 64
DISPLAY_DEVICE_MODESPRUNED = 134217728
DISPLAY_DEVICE_RDPUDD = 16777216
DISPLAY_DEVICE_REMOTE = 67108864
DISPLAY_DEVICE_DISCONNECT = 33554432
DISPLAY_DEVICE_TS_COMPATIBLE = 2097152
DISPLAY_DEVICE_UNSAFE_MODES_ON = 524288
DISPLAY_DEVICE_ACTIVE = 1
DISPLAY_DEVICE_ATTACHED = 2
DISPLAYCONFIG_MAXPATH = 1024
DISPLAYCONFIG_PATH_MODE_IDX_INVALID = 4294967295
DISPLAYCONFIG_PATH_TARGET_MODE_IDX_INVALID = 65535
DISPLAYCONFIG_PATH_DESKTOP_IMAGE_IDX_INVALID = 65535
DISPLAYCONFIG_PATH_SOURCE_MODE_IDX_INVALID = 65535
DISPLAYCONFIG_PATH_CLONE_GROUP_INVALID = 65535
DISPLAYCONFIG_SOURCE_IN_USE = 1
DISPLAYCONFIG_TARGET_IN_USE = 1
DISPLAYCONFIG_TARGET_FORCIBLE = 2
DISPLAYCONFIG_TARGET_FORCED_AVAILABILITY_BOOT = 4
DISPLAYCONFIG_TARGET_FORCED_AVAILABILITY_PATH = 8
DISPLAYCONFIG_TARGET_FORCED_AVAILABILITY_SYSTEM = 16
DISPLAYCONFIG_TARGET_IS_HMD = 32
DISPLAYCONFIG_PATH_ACTIVE = 1
DISPLAYCONFIG_PATH_PREFERRED_UNSCALED = 4
DISPLAYCONFIG_PATH_SUPPORT_VIRTUAL_MODE = 8
DISPLAYCONFIG_PATH_VALID_FLAGS = 29
QDC_ALL_PATHS = 1
QDC_ONLY_ACTIVE_PATHS = 2
QDC_DATABASE_CURRENT = 4
QDC_VIRTUAL_MODE_AWARE = 16
QDC_INCLUDE_HMD = 32
QDC_VIRTUAL_REFRESH_RATE_AWARE = 64
SDC_TOPOLOGY_INTERNAL = 1
SDC_TOPOLOGY_CLONE = 2
SDC_TOPOLOGY_EXTEND = 4
SDC_TOPOLOGY_EXTERNAL = 8
SDC_TOPOLOGY_SUPPLIED = 16
SDC_USE_SUPPLIED_DISPLAY_CONFIG = 32
SDC_VALIDATE = 64
SDC_APPLY = 128
SDC_NO_OPTIMIZATION = 256
SDC_SAVE_TO_DATABASE = 512
SDC_ALLOW_CHANGES = 1024
SDC_PATH_PERSIST_IF_REQUIRED = 2048
SDC_FORCE_MODE_ENUMERATION = 4096
SDC_ALLOW_PATH_ORDER_CHANGES = 8192
SDC_VIRTUAL_MODE_AWARE = 32768
SDC_VIRTUAL_REFRESH_RATE_AWARE = 131072
RDH_RECTANGLES = 1
SYSRGN = 4
TT_POLYGON_TYPE = 24
TT_PRIM_LINE = 1
TT_PRIM_QSPLINE = 2
TT_PRIM_CSPLINE = 3
GCP_DBCS = 1
GCP_ERROR = 32768
FLI_MASK = 4155
FLI_GLYPHS = 262144
GCP_JUSTIFYIN = 2097152
GCPCLASS_LATIN = 1
GCPCLASS_HEBREW = 2
GCPCLASS_ARABIC = 2
GCPCLASS_NEUTRAL = 3
GCPCLASS_LOCALNUMBER = 4
GCPCLASS_LATINNUMBER = 5
GCPCLASS_LATINNUMERICTERMINATOR = 6
GCPCLASS_LATINNUMERICSEPARATOR = 7
GCPCLASS_NUMERICSEPARATOR = 8
GCPCLASS_PREBOUNDLTR = 128
GCPCLASS_PREBOUNDRTL = 64
GCPCLASS_POSTBOUNDLTR = 32
GCPCLASS_POSTBOUNDRTL = 16
GCPGLYPH_LINKBEFORE = 32768
GCPGLYPH_LINKAFTER = 16384
TT_AVAILABLE = 1
TT_ENABLED = 2
DC_BINADJUST = 19
DC_EMF_COMPLIANT = 20
DC_DATATYPE_PRODUCED = 21
DC_MANUFACTURER = 23
DC_MODEL = 24
PRINTRATEUNIT_PPM = 1
PRINTRATEUNIT_CPS = 2
PRINTRATEUNIT_LPM = 3
PRINTRATEUNIT_IPM = 4
DCTT_BITMAP = 1
DCTT_DOWNLOAD = 2
DCTT_SUBDEV = 4
DCTT_DOWNLOAD_OUTLINE = 8
DCBA_FACEUPNONE = 0
DCBA_FACEUPCENTER = 1
DCBA_FACEUPLEFT = 2
DCBA_FACEUPRIGHT = 3
DCBA_FACEDOWNNONE = 256
DCBA_FACEDOWNCENTER = 257
DCBA_FACEDOWNLEFT = 258
DCBA_FACEDOWNRIGHT = 259
GS_8BIT_INDICES = 1
GGI_MARK_NONEXISTING_GLYPHS = 1
MM_MAX_NUMAXES = 16
MM_MAX_AXES_NAMELEN = 16
GDIREGISTERDDRAWPACKETVERSION = 1
AC_SRC_OVER = 0
AC_SRC_ALPHA = 1
GRADIENT_FILL_OP_FLAG = 255
CA_NEGATIVE = 1
CA_LOG_FILTER = 2
ILLUMINANT_DEVICE_DEFAULT = 0
ILLUMINANT_A = 1
ILLUMINANT_B = 2
ILLUMINANT_C = 3
ILLUMINANT_D50 = 4
ILLUMINANT_D55 = 5
ILLUMINANT_D65 = 6
ILLUMINANT_D75 = 7
ILLUMINANT_F2 = 8
ILLUMINANT_MAX_INDEX = 8
ILLUMINANT_TUNGSTEN = 1
ILLUMINANT_DAYLIGHT = 3
ILLUMINANT_FLUORESCENT = 8
ILLUMINANT_NTSC = 3
DI_APPBANDING = 1
DI_ROPS_READ_DESTINATION = 2
FONTMAPPER_MAX = 10
ENHMETA_SIGNATURE = 1179469088
ENHMETA_STOCK_OBJECT = 2147483648
SETICMPROFILE_EMBEDED = 1
CREATECOLORSPACE_EMBEDED = 1
COLORMATCHTOTARGET_EMBEDED = 1
GDICOMMENT_IDENTIFIER = 1128875079
GDICOMMENT_WINDOWS_METAFILE = 2147483649
GDICOMMENT_BEGINGROUP = 2
GDICOMMENT_ENDGROUP = 3
GDICOMMENT_MULTIFORMATS = 1073741828
EPS_SIGNATURE = 1179865157
GDICOMMENT_UNICODE_STRING = 64
GDICOMMENT_UNICODE_END = 128
WGL_FONT_LINES = 0
WGL_FONT_POLYGONS = 1
LPD_DOUBLEBUFFER = 1
LPD_STEREO = 2
LPD_SUPPORT_GDI = 16
LPD_SUPPORT_OPENGL = 32
LPD_SHARE_DEPTH = 64
LPD_SHARE_STENCIL = 128
LPD_SHARE_ACCUM = 256
LPD_SWAP_EXCHANGE = 512
LPD_SWAP_COPY = 1024
LPD_TRANSPARENT = 4096
LPD_TYPE_RGBA = 0
LPD_TYPE_COLORINDEX = 1
WGL_SWAP_MAIN_PLANE = 1
WGL_SWAP_OVERLAY1 = 2
WGL_SWAP_OVERLAY2 = 4
WGL_SWAP_OVERLAY3 = 8
WGL_SWAP_OVERLAY4 = 16
WGL_SWAP_OVERLAY5 = 32
WGL_SWAP_OVERLAY6 = 64
WGL_SWAP_OVERLAY7 = 128
WGL_SWAP_OVERLAY8 = 256
WGL_SWAP_OVERLAY9 = 512
WGL_SWAP_OVERLAY10 = 1024
WGL_SWAP_OVERLAY11 = 2048
WGL_SWAP_OVERLAY12 = 4096
WGL_SWAP_OVERLAY13 = 8192
WGL_SWAP_OVERLAY14 = 16384
WGL_SWAP_OVERLAY15 = 32768
WGL_SWAP_UNDERLAY1 = 65536
WGL_SWAP_UNDERLAY2 = 131072
WGL_SWAP_UNDERLAY3 = 262144
WGL_SWAP_UNDERLAY4 = 524288
WGL_SWAP_UNDERLAY5 = 1048576
WGL_SWAP_UNDERLAY6 = 2097152
WGL_SWAP_UNDERLAY7 = 4194304
WGL_SWAP_UNDERLAY8 = 8388608
WGL_SWAP_UNDERLAY9 = 16777216
WGL_SWAP_UNDERLAY10 = 33554432
WGL_SWAP_UNDERLAY11 = 67108864
WGL_SWAP_UNDERLAY12 = 134217728
WGL_SWAP_UNDERLAY13 = 268435456
WGL_SWAP_UNDERLAY14 = 536870912
WGL_SWAP_UNDERLAY15 = 1073741824
WGL_SWAPMULTIPLE_MAX = 16
NEWTRANSPARENT = 3
QUERYROPSUPPORT = 40
SELECTDIB = 41
SC_SCREENSAVE = 61760
TTFCFP_SUBSET = 0
TTFCFP_SUBSET1 = 1
TTFCFP_DELTA = 2
TTFCFP_APPLE_PLATFORMID = 1
TTFCFP_MS_PLATFORMID = 3
TTFCFP_DONT_CARE = 65535
TTFCFP_LANG_KEEP_ALL = 0
TTFCFP_FLAGS_SUBSET = 1
TTFCFP_FLAGS_COMPRESS = 2
TTFCFP_FLAGS_TTC = 4
TTFCFP_FLAGS_GLYPHLIST = 8
TTFMFP_SUBSET = 0
TTFMFP_SUBSET1 = 1
TTFMFP_DELTA = 2
ERR_GENERIC = 1000
ERR_READOUTOFBOUNDS = 1001
ERR_WRITEOUTOFBOUNDS = 1002
ERR_READCONTROL = 1003
ERR_WRITECONTROL = 1004
ERR_MEM = 1005
ERR_FORMAT = 1006
ERR_WOULD_GROW = 1007
ERR_VERSION = 1008
ERR_NO_GLYPHS = 1009
ERR_INVALID_MERGE_FORMATS = 1010
ERR_INVALID_MERGE_CHECKSUMS = 1011
ERR_INVALID_MERGE_NUMGLYPHS = 1012
ERR_INVALID_DELTA_FORMAT = 1013
ERR_NOT_TTC = 1014
ERR_INVALID_TTC_INDEX = 1015
ERR_MISSING_CMAP = 1030
ERR_MISSING_GLYF = 1031
ERR_MISSING_HEAD = 1032
ERR_MISSING_HHEA = 1033
ERR_MISSING_HMTX = 1034
ERR_MISSING_LOCA = 1035
ERR_MISSING_MAXP = 1036
ERR_MISSING_NAME = 1037
ERR_MISSING_POST = 1038
ERR_MISSING_OS2 = 1039
ERR_MISSING_VHEA = 1040
ERR_MISSING_VMTX = 1041
ERR_MISSING_HHEA_OR_VHEA = 1042
ERR_MISSING_HMTX_OR_VMTX = 1043
ERR_MISSING_EBDT = 1044
ERR_INVALID_CMAP = 1060
ERR_INVALID_GLYF = 1061
ERR_INVALID_HEAD = 1062
ERR_INVALID_HHEA = 1063
ERR_INVALID_HMTX = 1064
ERR_INVALID_LOCA = 1065
ERR_INVALID_MAXP = 1066
ERR_INVALID_NAME = 1067
ERR_INVALID_POST = 1068
ERR_INVALID_OS2 = 1069
ERR_INVALID_VHEA = 1070
ERR_INVALID_VMTX = 1071
ERR_INVALID_HHEA_OR_VHEA = 1072
ERR_INVALID_HMTX_OR_VMTX = 1073
ERR_INVALID_TTO = 1080
ERR_INVALID_GSUB = 1081
ERR_INVALID_GPOS = 1082
ERR_INVALID_GDEF = 1083
ERR_INVALID_JSTF = 1084
ERR_INVALID_BASE = 1085
ERR_INVALID_EBLC = 1086
ERR_INVALID_LTSH = 1087
ERR_INVALID_VDMX = 1088
ERR_INVALID_HDMX = 1089
ERR_PARAMETER0 = 1100
ERR_PARAMETER1 = 1101
ERR_PARAMETER2 = 1102
ERR_PARAMETER3 = 1103
ERR_PARAMETER4 = 1104
ERR_PARAMETER5 = 1105
ERR_PARAMETER6 = 1106
ERR_PARAMETER7 = 1107
ERR_PARAMETER8 = 1108
ERR_PARAMETER9 = 1109
ERR_PARAMETER10 = 1110
ERR_PARAMETER11 = 1111
ERR_PARAMETER12 = 1112
ERR_PARAMETER13 = 1113
ERR_PARAMETER14 = 1114
ERR_PARAMETER15 = 1115
ERR_PARAMETER16 = 1116
CHARSET_DEFAULT = 1
CHARSET_GLYPHIDX = 3
TTEMBED_FAILIFVARIATIONSIMULATED = 16
TTEMBED_WEBOBJECT = 128
TTEMBED_XORENCRYPTDATA = 268435456
TTEMBED_VARIATIONSIMULATED = 1
TTEMBED_EUDCEMBEDDED = 2
TTEMBED_SUBSETCANCEL = 4
TTLOAD_PRIVATE = 1
TTLOAD_EUDC_OVERWRITE = 2
TTLOAD_EUDC_SET = 4
TTDELETE_DONTREMOVEFONT = 1
E_NONE = 0
E_API_NOTIMPL = 1
E_CHARCODECOUNTINVALID = 2
E_CHARCODESETINVALID = 3
E_DEVICETRUETYPEFONT = 4
E_HDCINVALID = 6
E_NOFREEMEMORY = 7
E_FONTREFERENCEINVALID = 8
E_NOTATRUETYPEFONT = 10
E_ERRORACCESSINGFONTDATA = 12
E_ERRORACCESSINGFACENAME = 13
E_ERRORUNICODECONVERSION = 17
E_ERRORCONVERTINGCHARS = 18
E_EXCEPTION = 19
E_RESERVEDPARAMNOTNULL = 20
E_CHARSETINVALID = 21
E_FILE_NOT_FOUND = 23
E_TTC_INDEX_OUT_OF_RANGE = 24
E_INPUTPARAMINVALID = 25
E_ERRORCOMPRESSINGFONTDATA = 256
E_FONTDATAINVALID = 258
E_NAMECHANGEFAILED = 259
E_FONTNOTEMBEDDABLE = 260
E_PRIVSINVALID = 261
E_SUBSETTINGFAILED = 262
E_READFROMSTREAMFAILED = 263
E_SAVETOSTREAMFAILED = 264
E_NOOS2 = 265
E_T2NOFREEMEMORY = 266
E_ERRORREADINGFONTDATA = 267
E_FLAGSINVALID = 268
E_ERRORCREATINGFONTFILE = 269
E_FONTALREADYEXISTS = 270
E_FONTNAMEALREADYEXISTS = 271
E_FONTINSTALLFAILED = 272
E_ERRORDECOMPRESSINGFONTDATA = 273
E_ERRORACCESSINGEXCLUDELIST = 274
E_FACENAMEINVALID = 275
E_STREAMINVALID = 276
E_STATUSINVALID = 277
E_PRIVSTATUSINVALID = 278
E_PERMISSIONSINVALID = 279
E_PBENABLEDINVALID = 280
E_SUBSETTINGEXCEPTION = 281
E_SUBSTRING_TEST_FAIL = 282
E_FONTVARIATIONSIMULATED = 283
E_FONTFAMILYNAMENOTINFULL = 285
E_ADDFONTFAILED = 512
E_COULDNTCREATETEMPFILE = 513
E_FONTFILECREATEFAILED = 515
E_WINDOWSAPI = 516
E_FONTFILENOTFOUND = 517
E_RESOURCEFILECREATEFAILED = 518
E_ERROREXPANDINGFONTDATA = 519
E_ERRORGETTINGDC = 520
E_EXCEPTIONINDECOMPRESSION = 521
E_EXCEPTIONINCOMPRESSION = 522
def _define_GetObjectA():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HGDIOBJ,Int32,c_void_p)(('GetObjectA', windll['GDI32.dll']), ((1, 'h'),(1, 'c'),(1, 'pv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddFontResourceA():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR)(('AddFontResourceA', windll['GDI32.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddFontResourceW():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR)(('AddFontResourceW', windll['GDI32.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AnimatePalette():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HPALETTE,UInt32,UInt32,POINTER(win32more.Graphics.Gdi.PALETTEENTRY_head))(('AnimatePalette', windll['GDI32.dll']), ((1, 'hPal'),(1, 'iStartIndex'),(1, 'cEntries'),(1, 'ppe'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Arc():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,Int32,Int32,Int32,Int32,Int32,Int32)(('Arc', windll['GDI32.dll']), ((1, 'hdc'),(1, 'x1'),(1, 'y1'),(1, 'x2'),(1, 'y2'),(1, 'x3'),(1, 'y3'),(1, 'x4'),(1, 'y4'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BitBlt():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,Int32,Int32,win32more.Graphics.Gdi.HDC,Int32,Int32,win32more.Graphics.Gdi.ROP_CODE)(('BitBlt', windll['GDI32.dll']), ((1, 'hdc'),(1, 'x'),(1, 'y'),(1, 'cx'),(1, 'cy'),(1, 'hdcSrc'),(1, 'x1'),(1, 'y1'),(1, 'rop'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CancelDC():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC)(('CancelDC', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Chord():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,Int32,Int32,Int32,Int32,Int32,Int32)(('Chord', windll['GDI32.dll']), ((1, 'hdc'),(1, 'x1'),(1, 'y1'),(1, 'x2'),(1, 'y2'),(1, 'x3'),(1, 'y3'),(1, 'x4'),(1, 'y4'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CloseMetaFile():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HMETAFILE,win32more.Graphics.Gdi.HDC)(('CloseMetaFile', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CombineRgn():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.GDI_REGION_TYPE,win32more.Graphics.Gdi.HRGN,win32more.Graphics.Gdi.HRGN,win32more.Graphics.Gdi.HRGN,win32more.Graphics.Gdi.RGN_COMBINE_MODE)(('CombineRgn', windll['GDI32.dll']), ((1, 'hrgnDst'),(1, 'hrgnSrc1'),(1, 'hrgnSrc2'),(1, 'iMode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CopyMetaFileA():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HMETAFILE,win32more.Graphics.Gdi.HMETAFILE,win32more.Foundation.PSTR)(('CopyMetaFileA', windll['GDI32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CopyMetaFileW():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HMETAFILE,win32more.Graphics.Gdi.HMETAFILE,win32more.Foundation.PWSTR)(('CopyMetaFileW', windll['GDI32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateBitmap():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HBITMAP,Int32,Int32,UInt32,UInt32,c_void_p)(('CreateBitmap', windll['GDI32.dll']), ((1, 'nWidth'),(1, 'nHeight'),(1, 'nPlanes'),(1, 'nBitCount'),(1, 'lpBits'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateBitmapIndirect():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HBITMAP,POINTER(win32more.Graphics.Gdi.BITMAP_head))(('CreateBitmapIndirect', windll['GDI32.dll']), ((1, 'pbm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateBrushIndirect():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HBRUSH,POINTER(win32more.Graphics.Gdi.LOGBRUSH_head))(('CreateBrushIndirect', windll['GDI32.dll']), ((1, 'plbrush'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateCompatibleBitmap():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HBITMAP,win32more.Graphics.Gdi.HDC,Int32,Int32)(('CreateCompatibleBitmap', windll['GDI32.dll']), ((1, 'hdc'),(1, 'cx'),(1, 'cy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateDiscardableBitmap():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HBITMAP,win32more.Graphics.Gdi.HDC,Int32,Int32)(('CreateDiscardableBitmap', windll['GDI32.dll']), ((1, 'hdc'),(1, 'cx'),(1, 'cy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateCompatibleDC():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.CreatedHDC,win32more.Graphics.Gdi.HDC)(('CreateCompatibleDC', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateDCA():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.CreatedHDC,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Graphics.Gdi.DEVMODEA_head))(('CreateDCA', windll['GDI32.dll']), ((1, 'pwszDriver'),(1, 'pwszDevice'),(1, 'pszPort'),(1, 'pdm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateDCW():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.CreatedHDC,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Graphics.Gdi.DEVMODEW_head))(('CreateDCW', windll['GDI32.dll']), ((1, 'pwszDriver'),(1, 'pwszDevice'),(1, 'pszPort'),(1, 'pdm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateDIBitmap():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HBITMAP,win32more.Graphics.Gdi.HDC,POINTER(win32more.Graphics.Gdi.BITMAPINFOHEADER_head),UInt32,c_void_p,POINTER(win32more.Graphics.Gdi.BITMAPINFO_head),win32more.Graphics.Gdi.DIB_USAGE)(('CreateDIBitmap', windll['GDI32.dll']), ((1, 'hdc'),(1, 'pbmih'),(1, 'flInit'),(1, 'pjBits'),(1, 'pbmi'),(1, 'iUsage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateDIBPatternBrush():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HBRUSH,IntPtr,win32more.Graphics.Gdi.DIB_USAGE)(('CreateDIBPatternBrush', windll['GDI32.dll']), ((1, 'h'),(1, 'iUsage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateDIBPatternBrushPt():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HBRUSH,c_void_p,win32more.Graphics.Gdi.DIB_USAGE)(('CreateDIBPatternBrushPt', windll['GDI32.dll']), ((1, 'lpPackedDIB'),(1, 'iUsage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateEllipticRgn():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HRGN,Int32,Int32,Int32,Int32)(('CreateEllipticRgn', windll['GDI32.dll']), ((1, 'x1'),(1, 'y1'),(1, 'x2'),(1, 'y2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateEllipticRgnIndirect():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HRGN,POINTER(win32more.Foundation.RECT_head))(('CreateEllipticRgnIndirect', windll['GDI32.dll']), ((1, 'lprect'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateFontIndirectA():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HFONT,POINTER(win32more.Graphics.Gdi.LOGFONTA_head))(('CreateFontIndirectA', windll['GDI32.dll']), ((1, 'lplf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateFontIndirectW():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HFONT,POINTER(win32more.Graphics.Gdi.LOGFONTW_head))(('CreateFontIndirectW', windll['GDI32.dll']), ((1, 'lplf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateFontA():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HFONT,Int32,Int32,Int32,Int32,Int32,UInt32,UInt32,UInt32,UInt32,UInt32,UInt32,UInt32,UInt32,win32more.Foundation.PSTR)(('CreateFontA', windll['GDI32.dll']), ((1, 'cHeight'),(1, 'cWidth'),(1, 'cEscapement'),(1, 'cOrientation'),(1, 'cWeight'),(1, 'bItalic'),(1, 'bUnderline'),(1, 'bStrikeOut'),(1, 'iCharSet'),(1, 'iOutPrecision'),(1, 'iClipPrecision'),(1, 'iQuality'),(1, 'iPitchAndFamily'),(1, 'pszFaceName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateFontW():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HFONT,Int32,Int32,Int32,Int32,Int32,UInt32,UInt32,UInt32,UInt32,UInt32,UInt32,UInt32,UInt32,win32more.Foundation.PWSTR)(('CreateFontW', windll['GDI32.dll']), ((1, 'cHeight'),(1, 'cWidth'),(1, 'cEscapement'),(1, 'cOrientation'),(1, 'cWeight'),(1, 'bItalic'),(1, 'bUnderline'),(1, 'bStrikeOut'),(1, 'iCharSet'),(1, 'iOutPrecision'),(1, 'iClipPrecision'),(1, 'iQuality'),(1, 'iPitchAndFamily'),(1, 'pszFaceName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateHatchBrush():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HBRUSH,win32more.Graphics.Gdi.HATCH_BRUSH_STYLE,win32more.Foundation.COLORREF)(('CreateHatchBrush', windll['GDI32.dll']), ((1, 'iHatch'),(1, 'color'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateICA():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.CreatedHDC,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Graphics.Gdi.DEVMODEA_head))(('CreateICA', windll['GDI32.dll']), ((1, 'pszDriver'),(1, 'pszDevice'),(1, 'pszPort'),(1, 'pdm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateICW():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.CreatedHDC,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Graphics.Gdi.DEVMODEW_head))(('CreateICW', windll['GDI32.dll']), ((1, 'pszDriver'),(1, 'pszDevice'),(1, 'pszPort'),(1, 'pdm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateMetaFileA():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HdcMetdataFileHandle,win32more.Foundation.PSTR)(('CreateMetaFileA', windll['GDI32.dll']), ((1, 'pszFile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateMetaFileW():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HdcMetdataFileHandle,win32more.Foundation.PWSTR)(('CreateMetaFileW', windll['GDI32.dll']), ((1, 'pszFile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreatePalette():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HPALETTE,POINTER(win32more.Graphics.Gdi.LOGPALETTE_head))(('CreatePalette', windll['GDI32.dll']), ((1, 'plpal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreatePen():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HPEN,win32more.Graphics.Gdi.PEN_STYLE,Int32,win32more.Foundation.COLORREF)(('CreatePen', windll['GDI32.dll']), ((1, 'iStyle'),(1, 'cWidth'),(1, 'color'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreatePenIndirect():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HPEN,POINTER(win32more.Graphics.Gdi.LOGPEN_head))(('CreatePenIndirect', windll['GDI32.dll']), ((1, 'plpen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreatePolyPolygonRgn():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HRGN,POINTER(win32more.Foundation.POINT_head),POINTER(Int32),Int32,win32more.Graphics.Gdi.CREATE_POLYGON_RGN_MODE)(('CreatePolyPolygonRgn', windll['GDI32.dll']), ((1, 'pptl'),(1, 'pc'),(1, 'cPoly'),(1, 'iMode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreatePatternBrush():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HBRUSH,win32more.Graphics.Gdi.HBITMAP)(('CreatePatternBrush', windll['GDI32.dll']), ((1, 'hbm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateRectRgn():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HRGN,Int32,Int32,Int32,Int32)(('CreateRectRgn', windll['GDI32.dll']), ((1, 'x1'),(1, 'y1'),(1, 'x2'),(1, 'y2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateRectRgnIndirect():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HRGN,POINTER(win32more.Foundation.RECT_head))(('CreateRectRgnIndirect', windll['GDI32.dll']), ((1, 'lprect'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateRoundRectRgn():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HRGN,Int32,Int32,Int32,Int32,Int32,Int32)(('CreateRoundRectRgn', windll['GDI32.dll']), ((1, 'x1'),(1, 'y1'),(1, 'x2'),(1, 'y2'),(1, 'w'),(1, 'h'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateScalableFontResourceA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('CreateScalableFontResourceA', windll['GDI32.dll']), ((1, 'fdwHidden'),(1, 'lpszFont'),(1, 'lpszFile'),(1, 'lpszPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateScalableFontResourceW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('CreateScalableFontResourceW', windll['GDI32.dll']), ((1, 'fdwHidden'),(1, 'lpszFont'),(1, 'lpszFile'),(1, 'lpszPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateSolidBrush():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HBRUSH,win32more.Foundation.COLORREF)(('CreateSolidBrush', windll['GDI32.dll']), ((1, 'color'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteDC():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.CreatedHDC)(('DeleteDC', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteMetaFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HMETAFILE)(('DeleteMetaFile', windll['GDI32.dll']), ((1, 'hmf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HGDIOBJ)(('DeleteObject', windll['GDI32.dll']), ((1, 'ho'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrawEscape():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,Int32,Int32,win32more.Foundation.PSTR)(('DrawEscape', windll['GDI32.dll']), ((1, 'hdc'),(1, 'iEscape'),(1, 'cjIn'),(1, 'lpIn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Ellipse():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,Int32,Int32)(('Ellipse', windll['GDI32.dll']), ((1, 'hdc'),(1, 'left'),(1, 'top'),(1, 'right'),(1, 'bottom'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumFontFamiliesExA():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,POINTER(win32more.Graphics.Gdi.LOGFONTA_head),win32more.Graphics.Gdi.FONTENUMPROCA,win32more.Foundation.LPARAM,UInt32)(('EnumFontFamiliesExA', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpLogfont'),(1, 'lpProc'),(1, 'lParam'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumFontFamiliesExW():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,POINTER(win32more.Graphics.Gdi.LOGFONTW_head),win32more.Graphics.Gdi.FONTENUMPROCW,win32more.Foundation.LPARAM,UInt32)(('EnumFontFamiliesExW', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpLogfont'),(1, 'lpProc'),(1, 'lParam'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumFontFamiliesA():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,win32more.Foundation.PSTR,win32more.Graphics.Gdi.FONTENUMPROCA,win32more.Foundation.LPARAM)(('EnumFontFamiliesA', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpLogfont'),(1, 'lpProc'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumFontFamiliesW():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,win32more.Foundation.PWSTR,win32more.Graphics.Gdi.FONTENUMPROCW,win32more.Foundation.LPARAM)(('EnumFontFamiliesW', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpLogfont'),(1, 'lpProc'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumFontsA():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,win32more.Foundation.PSTR,win32more.Graphics.Gdi.FONTENUMPROCA,win32more.Foundation.LPARAM)(('EnumFontsA', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpLogfont'),(1, 'lpProc'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumFontsW():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,win32more.Foundation.PWSTR,win32more.Graphics.Gdi.FONTENUMPROCW,win32more.Foundation.LPARAM)(('EnumFontsW', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpLogfont'),(1, 'lpProc'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumObjects():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.OBJ_TYPE,win32more.Graphics.Gdi.GOBJENUMPROC,win32more.Foundation.LPARAM)(('EnumObjects', windll['GDI32.dll']), ((1, 'hdc'),(1, 'nType'),(1, 'lpFunc'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EqualRgn():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HRGN,win32more.Graphics.Gdi.HRGN)(('EqualRgn', windll['GDI32.dll']), ((1, 'hrgn1'),(1, 'hrgn2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ExcludeClipRect():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.GDI_REGION_TYPE,win32more.Graphics.Gdi.HDC,Int32,Int32,Int32,Int32)(('ExcludeClipRect', windll['GDI32.dll']), ((1, 'hdc'),(1, 'left'),(1, 'top'),(1, 'right'),(1, 'bottom'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ExtCreateRegion():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HRGN,POINTER(win32more.Graphics.Gdi.XFORM_head),UInt32,POINTER(win32more.Graphics.Gdi.RGNDATA_head))(('ExtCreateRegion', windll['GDI32.dll']), ((1, 'lpx'),(1, 'nCount'),(1, 'lpData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ExtFloodFill():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,win32more.Foundation.COLORREF,win32more.Graphics.Gdi.EXT_FLOOD_FILL_TYPE)(('ExtFloodFill', windll['GDI32.dll']), ((1, 'hdc'),(1, 'x'),(1, 'y'),(1, 'color'),(1, 'type'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FillRgn():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HRGN,win32more.Graphics.Gdi.HBRUSH)(('FillRgn', windll['GDI32.dll']), ((1, 'hdc'),(1, 'hrgn'),(1, 'hbr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FloodFill():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,win32more.Foundation.COLORREF)(('FloodFill', windll['GDI32.dll']), ((1, 'hdc'),(1, 'x'),(1, 'y'),(1, 'color'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FrameRgn():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HRGN,win32more.Graphics.Gdi.HBRUSH,Int32,Int32)(('FrameRgn', windll['GDI32.dll']), ((1, 'hdc'),(1, 'hrgn'),(1, 'hbr'),(1, 'w'),(1, 'h'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetROP2():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.R2_MODE,win32more.Graphics.Gdi.HDC)(('GetROP2', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetAspectRatioFilterEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.SIZE_head))(('GetAspectRatioFilterEx', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpsize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetBkColor():
    try:
        return WINFUNCTYPE(win32more.Foundation.COLORREF,win32more.Graphics.Gdi.HDC)(('GetBkColor', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDCBrushColor():
    try:
        return WINFUNCTYPE(win32more.Foundation.COLORREF,win32more.Graphics.Gdi.HDC)(('GetDCBrushColor', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDCPenColor():
    try:
        return WINFUNCTYPE(win32more.Foundation.COLORREF,win32more.Graphics.Gdi.HDC)(('GetDCPenColor', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetBkMode():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.BACKGROUND_MODE,win32more.Graphics.Gdi.HDC)(('GetBkMode', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetBitmapBits():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HBITMAP,Int32,c_void_p)(('GetBitmapBits', windll['GDI32.dll']), ((1, 'hbit'),(1, 'cb'),(1, 'lpvBits'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetBitmapDimensionEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HBITMAP,POINTER(win32more.Foundation.SIZE_head))(('GetBitmapDimensionEx', windll['GDI32.dll']), ((1, 'hbit'),(1, 'lpsize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetBoundsRect():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.RECT_head),UInt32)(('GetBoundsRect', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lprect'),(1, 'flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetBrushOrgEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.POINT_head))(('GetBrushOrgEx', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lppt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCharWidthA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,UInt32,UInt32,POINTER(Int32))(('GetCharWidthA', windll['GDI32.dll']), ((1, 'hdc'),(1, 'iFirst'),(1, 'iLast'),(1, 'lpBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCharWidthW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,UInt32,UInt32,POINTER(Int32))(('GetCharWidthW', windll['GDI32.dll']), ((1, 'hdc'),(1, 'iFirst'),(1, 'iLast'),(1, 'lpBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCharWidth32A():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,UInt32,UInt32,POINTER(Int32))(('GetCharWidth32A', windll['GDI32.dll']), ((1, 'hdc'),(1, 'iFirst'),(1, 'iLast'),(1, 'lpBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCharWidth32W():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,UInt32,UInt32,POINTER(Int32))(('GetCharWidth32W', windll['GDI32.dll']), ((1, 'hdc'),(1, 'iFirst'),(1, 'iLast'),(1, 'lpBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCharWidthFloatA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,UInt32,UInt32,POINTER(Single))(('GetCharWidthFloatA', windll['GDI32.dll']), ((1, 'hdc'),(1, 'iFirst'),(1, 'iLast'),(1, 'lpBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCharWidthFloatW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,UInt32,UInt32,POINTER(Single))(('GetCharWidthFloatW', windll['GDI32.dll']), ((1, 'hdc'),(1, 'iFirst'),(1, 'iLast'),(1, 'lpBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCharABCWidthsA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,UInt32,UInt32,POINTER(win32more.Graphics.Gdi.ABC_head))(('GetCharABCWidthsA', windll['GDI32.dll']), ((1, 'hdc'),(1, 'wFirst'),(1, 'wLast'),(1, 'lpABC'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCharABCWidthsW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,UInt32,UInt32,POINTER(win32more.Graphics.Gdi.ABC_head))(('GetCharABCWidthsW', windll['GDI32.dll']), ((1, 'hdc'),(1, 'wFirst'),(1, 'wLast'),(1, 'lpABC'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCharABCWidthsFloatA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,UInt32,UInt32,POINTER(win32more.Graphics.Gdi.ABCFLOAT_head))(('GetCharABCWidthsFloatA', windll['GDI32.dll']), ((1, 'hdc'),(1, 'iFirst'),(1, 'iLast'),(1, 'lpABC'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCharABCWidthsFloatW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,UInt32,UInt32,POINTER(win32more.Graphics.Gdi.ABCFLOAT_head))(('GetCharABCWidthsFloatW', windll['GDI32.dll']), ((1, 'hdc'),(1, 'iFirst'),(1, 'iLast'),(1, 'lpABC'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetClipBox():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.GDI_REGION_TYPE,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.RECT_head))(('GetClipBox', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lprect'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetClipRgn():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HRGN)(('GetClipRgn', windll['GDI32.dll']), ((1, 'hdc'),(1, 'hrgn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetMetaRgn():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HRGN)(('GetMetaRgn', windll['GDI32.dll']), ((1, 'hdc'),(1, 'hrgn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCurrentObject():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HGDIOBJ,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.OBJ_TYPE)(('GetCurrentObject', windll['GDI32.dll']), ((1, 'hdc'),(1, 'type'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCurrentPositionEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.POINT_head))(('GetCurrentPositionEx', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lppt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDeviceCaps():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.GET_DEVICE_CAPS_INDEX)(('GetDeviceCaps', windll['GDI32.dll']), ((1, 'hdc'),(1, 'index'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDIBits():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HBITMAP,UInt32,UInt32,c_void_p,POINTER(win32more.Graphics.Gdi.BITMAPINFO_head),win32more.Graphics.Gdi.DIB_USAGE)(('GetDIBits', windll['GDI32.dll']), ((1, 'hdc'),(1, 'hbm'),(1, 'start'),(1, 'cLines'),(1, 'lpvBits'),(1, 'lpbmi'),(1, 'usage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFontData():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HDC,UInt32,UInt32,c_void_p,UInt32)(('GetFontData', windll['GDI32.dll']), ((1, 'hdc'),(1, 'dwTable'),(1, 'dwOffset'),(1, 'pvBuffer'),(1, 'cjBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetGlyphOutlineA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HDC,UInt32,win32more.Graphics.Gdi.GET_GLYPH_OUTLINE_FORMAT,POINTER(win32more.Graphics.Gdi.GLYPHMETRICS_head),UInt32,c_void_p,POINTER(win32more.Graphics.Gdi.MAT2_head))(('GetGlyphOutlineA', windll['GDI32.dll']), ((1, 'hdc'),(1, 'uChar'),(1, 'fuFormat'),(1, 'lpgm'),(1, 'cjBuffer'),(1, 'pvBuffer'),(1, 'lpmat2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetGlyphOutlineW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HDC,UInt32,win32more.Graphics.Gdi.GET_GLYPH_OUTLINE_FORMAT,POINTER(win32more.Graphics.Gdi.GLYPHMETRICS_head),UInt32,c_void_p,POINTER(win32more.Graphics.Gdi.MAT2_head))(('GetGlyphOutlineW', windll['GDI32.dll']), ((1, 'hdc'),(1, 'uChar'),(1, 'fuFormat'),(1, 'lpgm'),(1, 'cjBuffer'),(1, 'pvBuffer'),(1, 'lpmat2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetGraphicsMode():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC)(('GetGraphicsMode', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetMapMode():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HDC_MAP_MODE,win32more.Graphics.Gdi.HDC)(('GetMapMode', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetMetaFileBitsEx():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HMETAFILE,UInt32,c_void_p)(('GetMetaFileBitsEx', windll['GDI32.dll']), ((1, 'hMF'),(1, 'cbBuffer'),(1, 'lpData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetMetaFileA():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HMETAFILE,win32more.Foundation.PSTR)(('GetMetaFileA', windll['GDI32.dll']), ((1, 'lpName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetMetaFileW():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HMETAFILE,win32more.Foundation.PWSTR)(('GetMetaFileW', windll['GDI32.dll']), ((1, 'lpName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNearestColor():
    try:
        return WINFUNCTYPE(win32more.Foundation.COLORREF,win32more.Graphics.Gdi.HDC,win32more.Foundation.COLORREF)(('GetNearestColor', windll['GDI32.dll']), ((1, 'hdc'),(1, 'color'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNearestPaletteIndex():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HPALETTE,win32more.Foundation.COLORREF)(('GetNearestPaletteIndex', windll['GDI32.dll']), ((1, 'h'),(1, 'color'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetObjectType():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HGDIOBJ)(('GetObjectType', windll['GDI32.dll']), ((1, 'h'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetOutlineTextMetricsA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HDC,UInt32,POINTER(win32more.Graphics.Gdi.OUTLINETEXTMETRICA_head))(('GetOutlineTextMetricsA', windll['GDI32.dll']), ((1, 'hdc'),(1, 'cjCopy'),(1, 'potm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetOutlineTextMetricsW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HDC,UInt32,POINTER(win32more.Graphics.Gdi.OUTLINETEXTMETRICW_head))(('GetOutlineTextMetricsW', windll['GDI32.dll']), ((1, 'hdc'),(1, 'cjCopy'),(1, 'potm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPaletteEntries():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HPALETTE,UInt32,UInt32,POINTER(win32more.Graphics.Gdi.PALETTEENTRY_head))(('GetPaletteEntries', windll['GDI32.dll']), ((1, 'hpal'),(1, 'iStart'),(1, 'cEntries'),(1, 'pPalEntries'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPixel():
    try:
        return WINFUNCTYPE(win32more.Foundation.COLORREF,win32more.Graphics.Gdi.HDC,Int32,Int32)(('GetPixel', windll['GDI32.dll']), ((1, 'hdc'),(1, 'x'),(1, 'y'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPolyFillMode():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC)(('GetPolyFillMode', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetRasterizerCaps():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Graphics.Gdi.RASTERIZER_STATUS_head),UInt32)(('GetRasterizerCaps', windll['GDI32.dll']), ((1, 'lpraststat'),(1, 'cjBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetRandomRgn():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HRGN,Int32)(('GetRandomRgn', windll['GDI32.dll']), ((1, 'hdc'),(1, 'hrgn'),(1, 'i'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetRegionData():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HRGN,UInt32,POINTER(win32more.Graphics.Gdi.RGNDATA_head))(('GetRegionData', windll['GDI32.dll']), ((1, 'hrgn'),(1, 'nCount'),(1, 'lpRgnData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetRgnBox():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.GDI_REGION_TYPE,win32more.Graphics.Gdi.HRGN,POINTER(win32more.Foundation.RECT_head))(('GetRgnBox', windll['GDI32.dll']), ((1, 'hrgn'),(1, 'lprc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetStockObject():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HGDIOBJ,win32more.Graphics.Gdi.GET_STOCK_OBJECT_FLAGS)(('GetStockObject', windll['GDI32.dll']), ((1, 'i'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetStretchBltMode():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC)(('GetStretchBltMode', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSystemPaletteEntries():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HDC,UInt32,UInt32,POINTER(win32more.Graphics.Gdi.PALETTEENTRY_head))(('GetSystemPaletteEntries', windll['GDI32.dll']), ((1, 'hdc'),(1, 'iStart'),(1, 'cEntries'),(1, 'pPalEntries'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSystemPaletteUse():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HDC)(('GetSystemPaletteUse', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTextCharacterExtra():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC)(('GetTextCharacterExtra', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTextAlign():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.TEXT_ALIGN_OPTIONS,win32more.Graphics.Gdi.HDC)(('GetTextAlign', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTextColor():
    try:
        return WINFUNCTYPE(win32more.Foundation.COLORREF,win32more.Graphics.Gdi.HDC)(('GetTextColor', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTextExtentPointA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,win32more.Foundation.PSTR,Int32,POINTER(win32more.Foundation.SIZE_head))(('GetTextExtentPointA', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpString'),(1, 'c'),(1, 'lpsz'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTextExtentPointW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,win32more.Foundation.PWSTR,Int32,POINTER(win32more.Foundation.SIZE_head))(('GetTextExtentPointW', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpString'),(1, 'c'),(1, 'lpsz'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTextExtentPoint32A():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,win32more.Foundation.PSTR,Int32,POINTER(win32more.Foundation.SIZE_head))(('GetTextExtentPoint32A', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpString'),(1, 'c'),(1, 'psizl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTextExtentPoint32W():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,win32more.Foundation.PWSTR,Int32,POINTER(win32more.Foundation.SIZE_head))(('GetTextExtentPoint32W', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpString'),(1, 'c'),(1, 'psizl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTextExtentExPointA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,win32more.Foundation.PSTR,Int32,Int32,POINTER(Int32),POINTER(Int32),POINTER(win32more.Foundation.SIZE_head))(('GetTextExtentExPointA', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpszString'),(1, 'cchString'),(1, 'nMaxExtent'),(1, 'lpnFit'),(1, 'lpnDx'),(1, 'lpSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTextExtentExPointW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,win32more.Foundation.PWSTR,Int32,Int32,POINTER(Int32),POINTER(Int32),POINTER(win32more.Foundation.SIZE_head))(('GetTextExtentExPointW', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpszString'),(1, 'cchString'),(1, 'nMaxExtent'),(1, 'lpnFit'),(1, 'lpnDx'),(1, 'lpSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFontLanguageInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HDC)(('GetFontLanguageInfo', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCharacterPlacementA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HDC,win32more.Foundation.PSTR,Int32,Int32,POINTER(win32more.Graphics.Gdi.GCP_RESULTSA_head),win32more.Graphics.Gdi.GET_CHARACTER_PLACEMENT_FLAGS)(('GetCharacterPlacementA', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpString'),(1, 'nCount'),(1, 'nMexExtent'),(1, 'lpResults'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCharacterPlacementW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HDC,win32more.Foundation.PWSTR,Int32,Int32,POINTER(win32more.Graphics.Gdi.GCP_RESULTSW_head),win32more.Graphics.Gdi.GET_CHARACTER_PLACEMENT_FLAGS)(('GetCharacterPlacementW', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpString'),(1, 'nCount'),(1, 'nMexExtent'),(1, 'lpResults'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFontUnicodeRanges():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HDC,POINTER(win32more.Graphics.Gdi.GLYPHSET_head))(('GetFontUnicodeRanges', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpgs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetGlyphIndicesA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HDC,win32more.Foundation.PSTR,Int32,POINTER(UInt16),UInt32)(('GetGlyphIndicesA', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpstr'),(1, 'c'),(1, 'pgi'),(1, 'fl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetGlyphIndicesW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HDC,win32more.Foundation.PWSTR,Int32,POINTER(UInt16),UInt32)(('GetGlyphIndicesW', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpstr'),(1, 'c'),(1, 'pgi'),(1, 'fl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTextExtentPointI():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(UInt16),Int32,POINTER(win32more.Foundation.SIZE_head))(('GetTextExtentPointI', windll['GDI32.dll']), ((1, 'hdc'),(1, 'pgiIn'),(1, 'cgi'),(1, 'psize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTextExtentExPointI():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(UInt16),Int32,Int32,POINTER(Int32),POINTER(Int32),POINTER(win32more.Foundation.SIZE_head))(('GetTextExtentExPointI', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpwszString'),(1, 'cwchString'),(1, 'nMaxExtent'),(1, 'lpnFit'),(1, 'lpnDx'),(1, 'lpSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCharWidthI():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,UInt32,UInt32,POINTER(UInt16),POINTER(Int32))(('GetCharWidthI', windll['GDI32.dll']), ((1, 'hdc'),(1, 'giFirst'),(1, 'cgi'),(1, 'pgi'),(1, 'piWidths'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCharABCWidthsI():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,UInt32,UInt32,POINTER(UInt16),POINTER(win32more.Graphics.Gdi.ABC_head))(('GetCharABCWidthsI', windll['GDI32.dll']), ((1, 'hdc'),(1, 'giFirst'),(1, 'cgi'),(1, 'pgi'),(1, 'pabc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddFontResourceExA():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,win32more.Graphics.Gdi.FONT_RESOURCE_CHARACTERISTICS,c_void_p)(('AddFontResourceExA', windll['GDI32.dll']), ((1, 'name'),(1, 'fl'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddFontResourceExW():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,win32more.Graphics.Gdi.FONT_RESOURCE_CHARACTERISTICS,c_void_p)(('AddFontResourceExW', windll['GDI32.dll']), ((1, 'name'),(1, 'fl'),(1, 'res'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveFontResourceExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,UInt32,c_void_p)(('RemoveFontResourceExA', windll['GDI32.dll']), ((1, 'name'),(1, 'fl'),(1, 'pdv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveFontResourceExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32,c_void_p)(('RemoveFontResourceExW', windll['GDI32.dll']), ((1, 'name'),(1, 'fl'),(1, 'pdv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddFontMemResourceEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,c_void_p,UInt32,c_void_p,POINTER(UInt32))(('AddFontMemResourceEx', windll['GDI32.dll']), ((1, 'pFileView'),(1, 'cjSize'),(1, 'pvResrved'),(1, 'pNumFonts'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveFontMemResourceEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('RemoveFontMemResourceEx', windll['GDI32.dll']), ((1, 'h'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateFontIndirectExA():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HFONT,POINTER(win32more.Graphics.Gdi.ENUMLOGFONTEXDVA_head))(('CreateFontIndirectExA', windll['GDI32.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateFontIndirectExW():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HFONT,POINTER(win32more.Graphics.Gdi.ENUMLOGFONTEXDVW_head))(('CreateFontIndirectExW', windll['GDI32.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetViewportExtEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.SIZE_head))(('GetViewportExtEx', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpsize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetViewportOrgEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.POINT_head))(('GetViewportOrgEx', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lppoint'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetWindowExtEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.SIZE_head))(('GetWindowExtEx', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpsize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetWindowOrgEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.POINT_head))(('GetWindowOrgEx', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lppoint'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IntersectClipRect():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.GDI_REGION_TYPE,win32more.Graphics.Gdi.HDC,Int32,Int32,Int32,Int32)(('IntersectClipRect', windll['GDI32.dll']), ((1, 'hdc'),(1, 'left'),(1, 'top'),(1, 'right'),(1, 'bottom'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InvertRgn():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HRGN)(('InvertRgn', windll['GDI32.dll']), ((1, 'hdc'),(1, 'hrgn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LineDDA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,Int32,Int32,Int32,Int32,win32more.Graphics.Gdi.LINEDDAPROC,win32more.Foundation.LPARAM)(('LineDDA', windll['GDI32.dll']), ((1, 'xStart'),(1, 'yStart'),(1, 'xEnd'),(1, 'yEnd'),(1, 'lpProc'),(1, 'data'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LineTo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32)(('LineTo', windll['GDI32.dll']), ((1, 'hdc'),(1, 'x'),(1, 'y'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MaskBlt():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,Int32,Int32,win32more.Graphics.Gdi.HDC,Int32,Int32,win32more.Graphics.Gdi.HBITMAP,Int32,Int32,UInt32)(('MaskBlt', windll['GDI32.dll']), ((1, 'hdcDest'),(1, 'xDest'),(1, 'yDest'),(1, 'width'),(1, 'height'),(1, 'hdcSrc'),(1, 'xSrc'),(1, 'ySrc'),(1, 'hbmMask'),(1, 'xMask'),(1, 'yMask'),(1, 'rop'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PlgBlt():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.POINT_head),win32more.Graphics.Gdi.HDC,Int32,Int32,Int32,Int32,win32more.Graphics.Gdi.HBITMAP,Int32,Int32)(('PlgBlt', windll['GDI32.dll']), ((1, 'hdcDest'),(1, 'lpPoint'),(1, 'hdcSrc'),(1, 'xSrc'),(1, 'ySrc'),(1, 'width'),(1, 'height'),(1, 'hbmMask'),(1, 'xMask'),(1, 'yMask'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OffsetClipRgn():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.GDI_REGION_TYPE,win32more.Graphics.Gdi.HDC,Int32,Int32)(('OffsetClipRgn', windll['GDI32.dll']), ((1, 'hdc'),(1, 'x'),(1, 'y'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OffsetRgn():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.GDI_REGION_TYPE,win32more.Graphics.Gdi.HRGN,Int32,Int32)(('OffsetRgn', windll['GDI32.dll']), ((1, 'hrgn'),(1, 'x'),(1, 'y'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PatBlt():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,Int32,Int32,win32more.Graphics.Gdi.ROP_CODE)(('PatBlt', windll['GDI32.dll']), ((1, 'hdc'),(1, 'x'),(1, 'y'),(1, 'w'),(1, 'h'),(1, 'rop'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Pie():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,Int32,Int32,Int32,Int32,Int32,Int32)(('Pie', windll['GDI32.dll']), ((1, 'hdc'),(1, 'left'),(1, 'top'),(1, 'right'),(1, 'bottom'),(1, 'xr1'),(1, 'yr1'),(1, 'xr2'),(1, 'yr2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PlayMetaFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HMETAFILE)(('PlayMetaFile', windll['GDI32.dll']), ((1, 'hdc'),(1, 'hmf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PaintRgn():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HRGN)(('PaintRgn', windll['GDI32.dll']), ((1, 'hdc'),(1, 'hrgn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PolyPolygon():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.POINT_head),POINTER(Int32),Int32)(('PolyPolygon', windll['GDI32.dll']), ((1, 'hdc'),(1, 'apt'),(1, 'asz'),(1, 'csz'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PtInRegion():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HRGN,Int32,Int32)(('PtInRegion', windll['GDI32.dll']), ((1, 'hrgn'),(1, 'x'),(1, 'y'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PtVisible():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32)(('PtVisible', windll['GDI32.dll']), ((1, 'hdc'),(1, 'x'),(1, 'y'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RectInRegion():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HRGN,POINTER(win32more.Foundation.RECT_head))(('RectInRegion', windll['GDI32.dll']), ((1, 'hrgn'),(1, 'lprect'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RectVisible():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.RECT_head))(('RectVisible', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lprect'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Rectangle():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,Int32,Int32)(('Rectangle', windll['GDI32.dll']), ((1, 'hdc'),(1, 'left'),(1, 'top'),(1, 'right'),(1, 'bottom'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RestoreDC():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32)(('RestoreDC', windll['GDI32.dll']), ((1, 'hdc'),(1, 'nSavedDC'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ResetDCA():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HDC,POINTER(win32more.Graphics.Gdi.DEVMODEA_head))(('ResetDCA', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpdm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ResetDCW():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HDC,POINTER(win32more.Graphics.Gdi.DEVMODEW_head))(('ResetDCW', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpdm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RealizePalette():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HDC)(('RealizePalette', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveFontResourceA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR)(('RemoveFontResourceA', windll['GDI32.dll']), ((1, 'lpFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveFontResourceW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR)(('RemoveFontResourceW', windll['GDI32.dll']), ((1, 'lpFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RoundRect():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,Int32,Int32,Int32,Int32)(('RoundRect', windll['GDI32.dll']), ((1, 'hdc'),(1, 'left'),(1, 'top'),(1, 'right'),(1, 'bottom'),(1, 'width'),(1, 'height'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ResizePalette():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HPALETTE,UInt32)(('ResizePalette', windll['GDI32.dll']), ((1, 'hpal'),(1, 'n'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SaveDC():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC)(('SaveDC', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SelectClipRgn():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.GDI_REGION_TYPE,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HRGN)(('SelectClipRgn', windll['GDI32.dll']), ((1, 'hdc'),(1, 'hrgn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ExtSelectClipRgn():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.GDI_REGION_TYPE,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HRGN,win32more.Graphics.Gdi.RGN_COMBINE_MODE)(('ExtSelectClipRgn', windll['GDI32.dll']), ((1, 'hdc'),(1, 'hrgn'),(1, 'mode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetMetaRgn():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.GDI_REGION_TYPE,win32more.Graphics.Gdi.HDC)(('SetMetaRgn', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SelectObject():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HGDIOBJ,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HGDIOBJ)(('SelectObject', windll['GDI32.dll']), ((1, 'hdc'),(1, 'h'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SelectPalette():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HPALETTE,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HPALETTE,win32more.Foundation.BOOL)(('SelectPalette', windll['GDI32.dll']), ((1, 'hdc'),(1, 'hPal'),(1, 'bForceBkgd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetBkColor():
    try:
        return WINFUNCTYPE(win32more.Foundation.COLORREF,win32more.Graphics.Gdi.HDC,win32more.Foundation.COLORREF)(('SetBkColor', windll['GDI32.dll']), ((1, 'hdc'),(1, 'color'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetDCBrushColor():
    try:
        return WINFUNCTYPE(win32more.Foundation.COLORREF,win32more.Graphics.Gdi.HDC,win32more.Foundation.COLORREF)(('SetDCBrushColor', windll['GDI32.dll']), ((1, 'hdc'),(1, 'color'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetDCPenColor():
    try:
        return WINFUNCTYPE(win32more.Foundation.COLORREF,win32more.Graphics.Gdi.HDC,win32more.Foundation.COLORREF)(('SetDCPenColor', windll['GDI32.dll']), ((1, 'hdc'),(1, 'color'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetBkMode():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.BACKGROUND_MODE)(('SetBkMode', windll['GDI32.dll']), ((1, 'hdc'),(1, 'mode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetBitmapBits():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HBITMAP,UInt32,c_void_p)(('SetBitmapBits', windll['GDI32.dll']), ((1, 'hbm'),(1, 'cb'),(1, 'pvBits'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetBoundsRect():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.RECT_head),win32more.Graphics.Gdi.SET_BOUNDS_RECT_FLAGS)(('SetBoundsRect', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lprect'),(1, 'flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetDIBits():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HBITMAP,UInt32,UInt32,c_void_p,POINTER(win32more.Graphics.Gdi.BITMAPINFO_head),win32more.Graphics.Gdi.DIB_USAGE)(('SetDIBits', windll['GDI32.dll']), ((1, 'hdc'),(1, 'hbm'),(1, 'start'),(1, 'cLines'),(1, 'lpBits'),(1, 'lpbmi'),(1, 'ColorUse'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetDIBitsToDevice():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,Int32,Int32,UInt32,UInt32,Int32,Int32,UInt32,UInt32,c_void_p,POINTER(win32more.Graphics.Gdi.BITMAPINFO_head),win32more.Graphics.Gdi.DIB_USAGE)(('SetDIBitsToDevice', windll['GDI32.dll']), ((1, 'hdc'),(1, 'xDest'),(1, 'yDest'),(1, 'w'),(1, 'h'),(1, 'xSrc'),(1, 'ySrc'),(1, 'StartScan'),(1, 'cLines'),(1, 'lpvBits'),(1, 'lpbmi'),(1, 'ColorUse'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetMapperFlags():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HDC,UInt32)(('SetMapperFlags', windll['GDI32.dll']), ((1, 'hdc'),(1, 'flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetGraphicsMode():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.GRAPHICS_MODE)(('SetGraphicsMode', windll['GDI32.dll']), ((1, 'hdc'),(1, 'iMode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetMapMode():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HDC_MAP_MODE)(('SetMapMode', windll['GDI32.dll']), ((1, 'hdc'),(1, 'iMode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetLayout():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.DC_LAYOUT)(('SetLayout', windll['GDI32.dll']), ((1, 'hdc'),(1, 'l'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetLayout():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HDC)(('GetLayout', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetMetaFileBitsEx():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HMETAFILE,UInt32,c_char_p_no)(('SetMetaFileBitsEx', windll['GDI32.dll']), ((1, 'cbBuffer'),(1, 'lpData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetPaletteEntries():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HPALETTE,UInt32,UInt32,POINTER(win32more.Graphics.Gdi.PALETTEENTRY_head))(('SetPaletteEntries', windll['GDI32.dll']), ((1, 'hpal'),(1, 'iStart'),(1, 'cEntries'),(1, 'pPalEntries'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetPixel():
    try:
        return WINFUNCTYPE(win32more.Foundation.COLORREF,win32more.Graphics.Gdi.HDC,Int32,Int32,win32more.Foundation.COLORREF)(('SetPixel', windll['GDI32.dll']), ((1, 'hdc'),(1, 'x'),(1, 'y'),(1, 'color'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetPixelV():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,win32more.Foundation.COLORREF)(('SetPixelV', windll['GDI32.dll']), ((1, 'hdc'),(1, 'x'),(1, 'y'),(1, 'color'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetPolyFillMode():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.CREATE_POLYGON_RGN_MODE)(('SetPolyFillMode', windll['GDI32.dll']), ((1, 'hdc'),(1, 'mode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StretchBlt():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,Int32,Int32,win32more.Graphics.Gdi.HDC,Int32,Int32,Int32,Int32,win32more.Graphics.Gdi.ROP_CODE)(('StretchBlt', windll['GDI32.dll']), ((1, 'hdcDest'),(1, 'xDest'),(1, 'yDest'),(1, 'wDest'),(1, 'hDest'),(1, 'hdcSrc'),(1, 'xSrc'),(1, 'ySrc'),(1, 'wSrc'),(1, 'hSrc'),(1, 'rop'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetRectRgn():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HRGN,Int32,Int32,Int32,Int32)(('SetRectRgn', windll['GDI32.dll']), ((1, 'hrgn'),(1, 'left'),(1, 'top'),(1, 'right'),(1, 'bottom'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StretchDIBits():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,Int32,Int32,Int32,Int32,Int32,Int32,Int32,Int32,c_void_p,POINTER(win32more.Graphics.Gdi.BITMAPINFO_head),win32more.Graphics.Gdi.DIB_USAGE,win32more.Graphics.Gdi.ROP_CODE)(('StretchDIBits', windll['GDI32.dll']), ((1, 'hdc'),(1, 'xDest'),(1, 'yDest'),(1, 'DestWidth'),(1, 'DestHeight'),(1, 'xSrc'),(1, 'ySrc'),(1, 'SrcWidth'),(1, 'SrcHeight'),(1, 'lpBits'),(1, 'lpbmi'),(1, 'iUsage'),(1, 'rop'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetROP2():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.R2_MODE)(('SetROP2', windll['GDI32.dll']), ((1, 'hdc'),(1, 'rop2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetStretchBltMode():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.STRETCH_BLT_MODE)(('SetStretchBltMode', windll['GDI32.dll']), ((1, 'hdc'),(1, 'mode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetSystemPaletteUse():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.SYSTEM_PALETTE_USE)(('SetSystemPaletteUse', windll['GDI32.dll']), ((1, 'hdc'),(1, 'use'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetTextCharacterExtra():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,Int32)(('SetTextCharacterExtra', windll['GDI32.dll']), ((1, 'hdc'),(1, 'extra'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetTextColor():
    try:
        return WINFUNCTYPE(win32more.Foundation.COLORREF,win32more.Graphics.Gdi.HDC,win32more.Foundation.COLORREF)(('SetTextColor', windll['GDI32.dll']), ((1, 'hdc'),(1, 'color'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetTextAlign():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.TEXT_ALIGN_OPTIONS)(('SetTextAlign', windll['GDI32.dll']), ((1, 'hdc'),(1, 'align'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetTextJustification():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32)(('SetTextJustification', windll['GDI32.dll']), ((1, 'hdc'),(1, 'extra'),(1, 'count'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UpdateColors():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC)(('UpdateColors', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AlphaBlend():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,Int32,Int32,win32more.Graphics.Gdi.HDC,Int32,Int32,Int32,Int32,win32more.Graphics.Gdi.BLENDFUNCTION)(('AlphaBlend', windll['MSIMG32.dll']), ((1, 'hdcDest'),(1, 'xoriginDest'),(1, 'yoriginDest'),(1, 'wDest'),(1, 'hDest'),(1, 'hdcSrc'),(1, 'xoriginSrc'),(1, 'yoriginSrc'),(1, 'wSrc'),(1, 'hSrc'),(1, 'ftn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TransparentBlt():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,Int32,Int32,win32more.Graphics.Gdi.HDC,Int32,Int32,Int32,Int32,UInt32)(('TransparentBlt', windll['MSIMG32.dll']), ((1, 'hdcDest'),(1, 'xoriginDest'),(1, 'yoriginDest'),(1, 'wDest'),(1, 'hDest'),(1, 'hdcSrc'),(1, 'xoriginSrc'),(1, 'yoriginSrc'),(1, 'wSrc'),(1, 'hSrc'),(1, 'crTransparent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GradientFill():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Graphics.Gdi.TRIVERTEX_head),UInt32,c_void_p,UInt32,win32more.Graphics.Gdi.GRADIENT_FILL)(('GradientFill', windll['MSIMG32.dll']), ((1, 'hdc'),(1, 'pVertex'),(1, 'nVertex'),(1, 'pMesh'),(1, 'nMesh'),(1, 'ulMode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GdiAlphaBlend():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,Int32,Int32,win32more.Graphics.Gdi.HDC,Int32,Int32,Int32,Int32,win32more.Graphics.Gdi.BLENDFUNCTION)(('GdiAlphaBlend', windll['GDI32.dll']), ((1, 'hdcDest'),(1, 'xoriginDest'),(1, 'yoriginDest'),(1, 'wDest'),(1, 'hDest'),(1, 'hdcSrc'),(1, 'xoriginSrc'),(1, 'yoriginSrc'),(1, 'wSrc'),(1, 'hSrc'),(1, 'ftn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GdiTransparentBlt():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,Int32,Int32,win32more.Graphics.Gdi.HDC,Int32,Int32,Int32,Int32,UInt32)(('GdiTransparentBlt', windll['GDI32.dll']), ((1, 'hdcDest'),(1, 'xoriginDest'),(1, 'yoriginDest'),(1, 'wDest'),(1, 'hDest'),(1, 'hdcSrc'),(1, 'xoriginSrc'),(1, 'yoriginSrc'),(1, 'wSrc'),(1, 'hSrc'),(1, 'crTransparent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GdiGradientFill():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Graphics.Gdi.TRIVERTEX_head),UInt32,c_void_p,UInt32,win32more.Graphics.Gdi.GRADIENT_FILL)(('GdiGradientFill', windll['GDI32.dll']), ((1, 'hdc'),(1, 'pVertex'),(1, 'nVertex'),(1, 'pMesh'),(1, 'nCount'),(1, 'ulMode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PlayMetaFileRecord():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Graphics.Gdi.HANDLETABLE_head),POINTER(win32more.Graphics.Gdi.METARECORD_head),UInt32)(('PlayMetaFileRecord', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpHandleTable'),(1, 'lpMR'),(1, 'noObjs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumMetaFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HMETAFILE,win32more.Graphics.Gdi.MFENUMPROC,win32more.Foundation.LPARAM)(('EnumMetaFile', windll['GDI32.dll']), ((1, 'hdc'),(1, 'hmf'),(1, 'proc'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CloseEnhMetaFile():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HENHMETAFILE,win32more.Graphics.Gdi.HDC)(('CloseEnhMetaFile', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CopyEnhMetaFileA():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HENHMETAFILE,win32more.Graphics.Gdi.HENHMETAFILE,win32more.Foundation.PSTR)(('CopyEnhMetaFileA', windll['GDI32.dll']), ((1, 'hEnh'),(1, 'lpFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CopyEnhMetaFileW():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HENHMETAFILE,win32more.Graphics.Gdi.HENHMETAFILE,win32more.Foundation.PWSTR)(('CopyEnhMetaFileW', windll['GDI32.dll']), ((1, 'hEnh'),(1, 'lpFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateEnhMetaFileA():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HdcMetdataEnhFileHandle,win32more.Graphics.Gdi.HDC,win32more.Foundation.PSTR,POINTER(win32more.Foundation.RECT_head),win32more.Foundation.PSTR)(('CreateEnhMetaFileA', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpFilename'),(1, 'lprc'),(1, 'lpDesc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateEnhMetaFileW():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HdcMetdataEnhFileHandle,win32more.Graphics.Gdi.HDC,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.RECT_head),win32more.Foundation.PWSTR)(('CreateEnhMetaFileW', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpFilename'),(1, 'lprc'),(1, 'lpDesc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteEnhMetaFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HENHMETAFILE)(('DeleteEnhMetaFile', windll['GDI32.dll']), ((1, 'hmf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumEnhMetaFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HENHMETAFILE,win32more.Graphics.Gdi.ENHMFENUMPROC,c_void_p,POINTER(win32more.Foundation.RECT_head))(('EnumEnhMetaFile', windll['GDI32.dll']), ((1, 'hdc'),(1, 'hmf'),(1, 'proc'),(1, 'param3'),(1, 'lpRect'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetEnhMetaFileA():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HENHMETAFILE,win32more.Foundation.PSTR)(('GetEnhMetaFileA', windll['GDI32.dll']), ((1, 'lpName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetEnhMetaFileW():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HENHMETAFILE,win32more.Foundation.PWSTR)(('GetEnhMetaFileW', windll['GDI32.dll']), ((1, 'lpName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetEnhMetaFileBits():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HENHMETAFILE,UInt32,c_char_p_no)(('GetEnhMetaFileBits', windll['GDI32.dll']), ((1, 'hEMF'),(1, 'nSize'),(1, 'lpData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetEnhMetaFileDescriptionA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HENHMETAFILE,UInt32,win32more.Foundation.PSTR)(('GetEnhMetaFileDescriptionA', windll['GDI32.dll']), ((1, 'hemf'),(1, 'cchBuffer'),(1, 'lpDescription'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetEnhMetaFileDescriptionW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HENHMETAFILE,UInt32,win32more.Foundation.PWSTR)(('GetEnhMetaFileDescriptionW', windll['GDI32.dll']), ((1, 'hemf'),(1, 'cchBuffer'),(1, 'lpDescription'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetEnhMetaFileHeader():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HENHMETAFILE,UInt32,POINTER(win32more.Graphics.Gdi.ENHMETAHEADER_head))(('GetEnhMetaFileHeader', windll['GDI32.dll']), ((1, 'hemf'),(1, 'nSize'),(1, 'lpEnhMetaHeader'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetEnhMetaFilePaletteEntries():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HENHMETAFILE,UInt32,POINTER(win32more.Graphics.Gdi.PALETTEENTRY_head))(('GetEnhMetaFilePaletteEntries', windll['GDI32.dll']), ((1, 'hemf'),(1, 'nNumEntries'),(1, 'lpPaletteEntries'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetWinMetaFileBits():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HENHMETAFILE,UInt32,c_char_p_no,Int32,win32more.Graphics.Gdi.HDC)(('GetWinMetaFileBits', windll['GDI32.dll']), ((1, 'hemf'),(1, 'cbData16'),(1, 'pData16'),(1, 'iMapMode'),(1, 'hdcRef'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PlayEnhMetaFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HENHMETAFILE,POINTER(win32more.Foundation.RECT_head))(('PlayEnhMetaFile', windll['GDI32.dll']), ((1, 'hdc'),(1, 'hmf'),(1, 'lprect'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PlayEnhMetaFileRecord():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Graphics.Gdi.HANDLETABLE_head),POINTER(win32more.Graphics.Gdi.ENHMETARECORD_head),UInt32)(('PlayEnhMetaFileRecord', windll['GDI32.dll']), ((1, 'hdc'),(1, 'pht'),(1, 'pmr'),(1, 'cht'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetEnhMetaFileBits():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HENHMETAFILE,UInt32,c_char_p_no)(('SetEnhMetaFileBits', windll['GDI32.dll']), ((1, 'nSize'),(1, 'pb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GdiComment():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,UInt32,c_char_p_no)(('GdiComment', windll['GDI32.dll']), ((1, 'hdc'),(1, 'nSize'),(1, 'lpData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTextMetricsA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Graphics.Gdi.TEXTMETRICA_head))(('GetTextMetricsA', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lptm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTextMetricsW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Graphics.Gdi.TEXTMETRICW_head))(('GetTextMetricsW', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lptm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AngleArc():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,UInt32,Single,Single)(('AngleArc', windll['GDI32.dll']), ((1, 'hdc'),(1, 'x'),(1, 'y'),(1, 'r'),(1, 'StartAngle'),(1, 'SweepAngle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PolyPolyline():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.POINT_head),POINTER(UInt32),UInt32)(('PolyPolyline', windll['GDI32.dll']), ((1, 'hdc'),(1, 'apt'),(1, 'asz'),(1, 'csz'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetWorldTransform():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Graphics.Gdi.XFORM_head))(('GetWorldTransform', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpxf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetWorldTransform():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Graphics.Gdi.XFORM_head))(('SetWorldTransform', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpxf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ModifyWorldTransform():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Graphics.Gdi.XFORM_head),win32more.Graphics.Gdi.MODIFY_WORLD_TRANSFORM_MODE)(('ModifyWorldTransform', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpxf'),(1, 'mode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CombineTransform():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Graphics.Gdi.XFORM_head),POINTER(win32more.Graphics.Gdi.XFORM_head),POINTER(win32more.Graphics.Gdi.XFORM_head))(('CombineTransform', windll['GDI32.dll']), ((1, 'lpxfOut'),(1, 'lpxf1'),(1, 'lpxf2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateDIBSection():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HBITMAP,win32more.Graphics.Gdi.HDC,POINTER(win32more.Graphics.Gdi.BITMAPINFO_head),win32more.Graphics.Gdi.DIB_USAGE,POINTER(c_void_p),win32more.Foundation.HANDLE,UInt32)(('CreateDIBSection', windll['GDI32.dll']), ((1, 'hdc'),(1, 'pbmi'),(1, 'usage'),(1, 'ppvBits'),(1, 'hSection'),(1, 'offset'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDIBColorTable():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HDC,UInt32,UInt32,POINTER(win32more.Graphics.Gdi.RGBQUAD_head))(('GetDIBColorTable', windll['GDI32.dll']), ((1, 'hdc'),(1, 'iStart'),(1, 'cEntries'),(1, 'prgbq'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetDIBColorTable():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HDC,UInt32,UInt32,POINTER(win32more.Graphics.Gdi.RGBQUAD_head))(('SetDIBColorTable', windll['GDI32.dll']), ((1, 'hdc'),(1, 'iStart'),(1, 'cEntries'),(1, 'prgbq'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetColorAdjustment():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Graphics.Gdi.COLORADJUSTMENT_head))(('SetColorAdjustment', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpca'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetColorAdjustment():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Graphics.Gdi.COLORADJUSTMENT_head))(('GetColorAdjustment', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpca'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateHalftonePalette():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HPALETTE,win32more.Graphics.Gdi.HDC)(('CreateHalftonePalette', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AbortPath():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC)(('AbortPath', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ArcTo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,Int32,Int32,Int32,Int32,Int32,Int32)(('ArcTo', windll['GDI32.dll']), ((1, 'hdc'),(1, 'left'),(1, 'top'),(1, 'right'),(1, 'bottom'),(1, 'xr1'),(1, 'yr1'),(1, 'xr2'),(1, 'yr2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BeginPath():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC)(('BeginPath', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CloseFigure():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC)(('CloseFigure', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EndPath():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC)(('EndPath', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FillPath():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC)(('FillPath', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FlattenPath():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC)(('FlattenPath', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPath():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.POINT_head),c_char_p_no,Int32)(('GetPath', windll['GDI32.dll']), ((1, 'hdc'),(1, 'apt'),(1, 'aj'),(1, 'cpt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PathToRegion():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HRGN,win32more.Graphics.Gdi.HDC)(('PathToRegion', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PolyDraw():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.POINT_head),c_char_p_no,Int32)(('PolyDraw', windll['GDI32.dll']), ((1, 'hdc'),(1, 'apt'),(1, 'aj'),(1, 'cpt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SelectClipPath():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.RGN_COMBINE_MODE)(('SelectClipPath', windll['GDI32.dll']), ((1, 'hdc'),(1, 'mode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetArcDirection():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.ARC_DIRECTION)(('SetArcDirection', windll['GDI32.dll']), ((1, 'hdc'),(1, 'dir'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetMiterLimit():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Single,POINTER(Single))(('SetMiterLimit', windll['GDI32.dll']), ((1, 'hdc'),(1, 'limit'),(1, 'old'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StrokeAndFillPath():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC)(('StrokeAndFillPath', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StrokePath():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC)(('StrokePath', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WidenPath():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC)(('WidenPath', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ExtCreatePen():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HPEN,win32more.Graphics.Gdi.PEN_STYLE,UInt32,POINTER(win32more.Graphics.Gdi.LOGBRUSH_head),UInt32,POINTER(UInt32))(('ExtCreatePen', windll['GDI32.dll']), ((1, 'iPenStyle'),(1, 'cWidth'),(1, 'plbrush'),(1, 'cStyle'),(1, 'pstyle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetMiterLimit():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(Single))(('GetMiterLimit', windll['GDI32.dll']), ((1, 'hdc'),(1, 'plimit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetArcDirection():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC)(('GetArcDirection', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetObjectW():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HGDIOBJ,Int32,c_void_p)(('GetObjectW', windll['GDI32.dll']), ((1, 'h'),(1, 'c'),(1, 'pv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MoveToEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,POINTER(win32more.Foundation.POINT_head))(('MoveToEx', windll['GDI32.dll']), ((1, 'hdc'),(1, 'x'),(1, 'y'),(1, 'lppt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextOutA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,win32more.Foundation.PSTR,Int32)(('TextOutA', windll['GDI32.dll']), ((1, 'hdc'),(1, 'x'),(1, 'y'),(1, 'lpString'),(1, 'c'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TextOutW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,win32more.Foundation.PWSTR,Int32)(('TextOutW', windll['GDI32.dll']), ((1, 'hdc'),(1, 'x'),(1, 'y'),(1, 'lpString'),(1, 'c'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ExtTextOutA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,win32more.Graphics.Gdi.ETO_OPTIONS,POINTER(win32more.Foundation.RECT_head),win32more.Foundation.PSTR,UInt32,POINTER(Int32))(('ExtTextOutA', windll['GDI32.dll']), ((1, 'hdc'),(1, 'x'),(1, 'y'),(1, 'options'),(1, 'lprect'),(1, 'lpString'),(1, 'c'),(1, 'lpDx'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ExtTextOutW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,win32more.Graphics.Gdi.ETO_OPTIONS,POINTER(win32more.Foundation.RECT_head),win32more.Foundation.PWSTR,UInt32,POINTER(Int32))(('ExtTextOutW', windll['GDI32.dll']), ((1, 'hdc'),(1, 'x'),(1, 'y'),(1, 'options'),(1, 'lprect'),(1, 'lpString'),(1, 'c'),(1, 'lpDx'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PolyTextOutA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Graphics.Gdi.POLYTEXTA_head),Int32)(('PolyTextOutA', windll['GDI32.dll']), ((1, 'hdc'),(1, 'ppt'),(1, 'nstrings'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PolyTextOutW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Graphics.Gdi.POLYTEXTW_head),Int32)(('PolyTextOutW', windll['GDI32.dll']), ((1, 'hdc'),(1, 'ppt'),(1, 'nstrings'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreatePolygonRgn():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HRGN,POINTER(win32more.Foundation.POINT_head),Int32,win32more.Graphics.Gdi.CREATE_POLYGON_RGN_MODE)(('CreatePolygonRgn', windll['GDI32.dll']), ((1, 'pptl'),(1, 'cPoint'),(1, 'iMode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DPtoLP():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.POINT_head),Int32)(('DPtoLP', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lppt'),(1, 'c'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LPtoDP():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.POINT_head),Int32)(('LPtoDP', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lppt'),(1, 'c'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Polygon():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.POINT_head),Int32)(('Polygon', windll['GDI32.dll']), ((1, 'hdc'),(1, 'apt'),(1, 'cpt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Polyline():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.POINT_head),Int32)(('Polyline', windll['GDI32.dll']), ((1, 'hdc'),(1, 'apt'),(1, 'cpt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PolyBezier():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.POINT_head),UInt32)(('PolyBezier', windll['GDI32.dll']), ((1, 'hdc'),(1, 'apt'),(1, 'cpt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PolyBezierTo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.POINT_head),UInt32)(('PolyBezierTo', windll['GDI32.dll']), ((1, 'hdc'),(1, 'apt'),(1, 'cpt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PolylineTo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.POINT_head),UInt32)(('PolylineTo', windll['GDI32.dll']), ((1, 'hdc'),(1, 'apt'),(1, 'cpt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetViewportExtEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,POINTER(win32more.Foundation.SIZE_head))(('SetViewportExtEx', windll['GDI32.dll']), ((1, 'hdc'),(1, 'x'),(1, 'y'),(1, 'lpsz'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetViewportOrgEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,POINTER(win32more.Foundation.POINT_head))(('SetViewportOrgEx', windll['GDI32.dll']), ((1, 'hdc'),(1, 'x'),(1, 'y'),(1, 'lppt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetWindowExtEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,POINTER(win32more.Foundation.SIZE_head))(('SetWindowExtEx', windll['GDI32.dll']), ((1, 'hdc'),(1, 'x'),(1, 'y'),(1, 'lpsz'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetWindowOrgEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,POINTER(win32more.Foundation.POINT_head))(('SetWindowOrgEx', windll['GDI32.dll']), ((1, 'hdc'),(1, 'x'),(1, 'y'),(1, 'lppt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OffsetViewportOrgEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,POINTER(win32more.Foundation.POINT_head))(('OffsetViewportOrgEx', windll['GDI32.dll']), ((1, 'hdc'),(1, 'x'),(1, 'y'),(1, 'lppt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OffsetWindowOrgEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,POINTER(win32more.Foundation.POINT_head))(('OffsetWindowOrgEx', windll['GDI32.dll']), ((1, 'hdc'),(1, 'x'),(1, 'y'),(1, 'lppt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ScaleViewportExtEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,Int32,Int32,POINTER(win32more.Foundation.SIZE_head))(('ScaleViewportExtEx', windll['GDI32.dll']), ((1, 'hdc'),(1, 'xn'),(1, 'dx'),(1, 'yn'),(1, 'yd'),(1, 'lpsz'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ScaleWindowExtEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,Int32,Int32,POINTER(win32more.Foundation.SIZE_head))(('ScaleWindowExtEx', windll['GDI32.dll']), ((1, 'hdc'),(1, 'xn'),(1, 'xd'),(1, 'yn'),(1, 'yd'),(1, 'lpsz'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetBitmapDimensionEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HBITMAP,Int32,Int32,POINTER(win32more.Foundation.SIZE_head))(('SetBitmapDimensionEx', windll['GDI32.dll']), ((1, 'hbm'),(1, 'w'),(1, 'h'),(1, 'lpsz'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetBrushOrgEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,POINTER(win32more.Foundation.POINT_head))(('SetBrushOrgEx', windll['GDI32.dll']), ((1, 'hdc'),(1, 'x'),(1, 'y'),(1, 'lppt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTextFaceA():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,Int32,win32more.Foundation.PSTR)(('GetTextFaceA', windll['GDI32.dll']), ((1, 'hdc'),(1, 'c'),(1, 'lpName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTextFaceW():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,Int32,win32more.Foundation.PWSTR)(('GetTextFaceW', windll['GDI32.dll']), ((1, 'hdc'),(1, 'c'),(1, 'lpName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetKerningPairsA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HDC,UInt32,POINTER(win32more.Graphics.Gdi.KERNINGPAIR_head))(('GetKerningPairsA', windll['GDI32.dll']), ((1, 'hdc'),(1, 'nPairs'),(1, 'lpKernPair'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetKerningPairsW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HDC,UInt32,POINTER(win32more.Graphics.Gdi.KERNINGPAIR_head))(('GetKerningPairsW', windll['GDI32.dll']), ((1, 'hdc'),(1, 'nPairs'),(1, 'lpKernPair'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDCOrgEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.POINT_head))(('GetDCOrgEx', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lppt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FixBrushOrgEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32,Int32,POINTER(win32more.Foundation.POINT_head))(('FixBrushOrgEx', windll['GDI32.dll']), ((1, 'hdc'),(1, 'x'),(1, 'y'),(1, 'ptl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnrealizeObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HGDIOBJ)(('UnrealizeObject', windll['GDI32.dll']), ((1, 'h'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GdiFlush():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,)(('GdiFlush', windll['GDI32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GdiSetBatchLimit():
    try:
        return WINFUNCTYPE(UInt32,UInt32)(('GdiSetBatchLimit', windll['GDI32.dll']), ((1, 'dw'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GdiGetBatchLimit():
    try:
        return WINFUNCTYPE(UInt32,)(('GdiGetBatchLimit', windll['GDI32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_wglSwapMultipleBuffers():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(win32more.Graphics.Gdi.WGLSWAP_head))(('wglSwapMultipleBuffers', windll['OPENGL32.dll']), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateFontPackage():
    try:
        return CFUNCTYPE(UInt32,c_char_p_no,UInt32,POINTER(c_char_p_no),POINTER(UInt32),POINTER(UInt32),UInt16,UInt16,UInt16,UInt16,win32more.Graphics.Gdi.CREATE_FONT_PACKAGE_SUBSET_PLATFORM,win32more.Graphics.Gdi.CREATE_FONT_PACKAGE_SUBSET_ENCODING,POINTER(UInt16),UInt16,win32more.Graphics.Gdi.CFP_ALLOCPROC,win32more.Graphics.Gdi.CFP_REALLOCPROC,win32more.Graphics.Gdi.CFP_FREEPROC,c_void_p)(('CreateFontPackage', cdll['FONTSUB.dll']), ((1, 'puchSrcBuffer'),(1, 'ulSrcBufferSize'),(1, 'ppuchFontPackageBuffer'),(1, 'pulFontPackageBufferSize'),(1, 'pulBytesWritten'),(1, 'usFlag'),(1, 'usTTCIndex'),(1, 'usSubsetFormat'),(1, 'usSubsetLanguage'),(1, 'usSubsetPlatform'),(1, 'usSubsetEncoding'),(1, 'pusSubsetKeepList'),(1, 'usSubsetListCount'),(1, 'lpfnAllocate'),(1, 'lpfnReAllocate'),(1, 'lpfnFree'),(1, 'lpvReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MergeFontPackage():
    try:
        return CFUNCTYPE(UInt32,c_char_p_no,UInt32,c_char_p_no,UInt32,POINTER(c_char_p_no),POINTER(UInt32),POINTER(UInt32),UInt16,win32more.Graphics.Gdi.CFP_ALLOCPROC,win32more.Graphics.Gdi.CFP_REALLOCPROC,win32more.Graphics.Gdi.CFP_FREEPROC,c_void_p)(('MergeFontPackage', cdll['FONTSUB.dll']), ((1, 'puchMergeFontBuffer'),(1, 'ulMergeFontBufferSize'),(1, 'puchFontPackageBuffer'),(1, 'ulFontPackageBufferSize'),(1, 'ppuchDestBuffer'),(1, 'pulDestBufferSize'),(1, 'pulBytesWritten'),(1, 'usMode'),(1, 'lpfnAllocate'),(1, 'lpfnReAllocate'),(1, 'lpfnFree'),(1, 'lpvReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TTEmbedFont():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.TTEMBED_FLAGS,win32more.Graphics.Gdi.EMBED_FONT_CHARSET,POINTER(win32more.Graphics.Gdi.EMBEDDED_FONT_PRIV_STATUS),POINTER(UInt32),win32more.Graphics.Gdi.WRITEEMBEDPROC,c_void_p,POINTER(UInt16),UInt16,UInt16,POINTER(win32more.Graphics.Gdi.TTEMBEDINFO_head))(('TTEmbedFont', windll['t2embed.dll']), ((1, 'hDC'),(1, 'ulFlags'),(1, 'ulCharSet'),(1, 'pulPrivStatus'),(1, 'pulStatus'),(1, 'lpfnWriteToStream'),(1, 'lpvWriteStream'),(1, 'pusCharCodeSet'),(1, 'usCharCodeCount'),(1, 'usLanguage'),(1, 'pTTEmbedInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TTEmbedFontFromFileA():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,win32more.Foundation.PSTR,UInt16,win32more.Graphics.Gdi.TTEMBED_FLAGS,win32more.Graphics.Gdi.EMBED_FONT_CHARSET,POINTER(win32more.Graphics.Gdi.EMBEDDED_FONT_PRIV_STATUS),POINTER(UInt32),win32more.Graphics.Gdi.WRITEEMBEDPROC,c_void_p,POINTER(UInt16),UInt16,UInt16,POINTER(win32more.Graphics.Gdi.TTEMBEDINFO_head))(('TTEmbedFontFromFileA', windll['t2embed.dll']), ((1, 'hDC'),(1, 'szFontFileName'),(1, 'usTTCIndex'),(1, 'ulFlags'),(1, 'ulCharSet'),(1, 'pulPrivStatus'),(1, 'pulStatus'),(1, 'lpfnWriteToStream'),(1, 'lpvWriteStream'),(1, 'pusCharCodeSet'),(1, 'usCharCodeCount'),(1, 'usLanguage'),(1, 'pTTEmbedInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TTLoadEmbeddedFont():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Foundation.HANDLE),UInt32,POINTER(win32more.Graphics.Gdi.EMBEDDED_FONT_PRIV_STATUS),win32more.Graphics.Gdi.FONT_LICENSE_PRIVS,POINTER(win32more.Graphics.Gdi.TTLOAD_EMBEDDED_FONT_STATUS),win32more.Graphics.Gdi.READEMBEDPROC,c_void_p,win32more.Foundation.PWSTR,win32more.Foundation.PSTR,POINTER(win32more.Graphics.Gdi.TTLOADINFO_head))(('TTLoadEmbeddedFont', windll['t2embed.dll']), ((1, 'phFontReference'),(1, 'ulFlags'),(1, 'pulPrivStatus'),(1, 'ulPrivs'),(1, 'pulStatus'),(1, 'lpfnReadFromStream'),(1, 'lpvReadStream'),(1, 'szWinFamilyName'),(1, 'szMacFamilyName'),(1, 'pTTLoadInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TTGetEmbeddedFontInfo():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.TTEMBED_FLAGS,POINTER(UInt32),win32more.Graphics.Gdi.FONT_LICENSE_PRIVS,POINTER(UInt32),win32more.Graphics.Gdi.READEMBEDPROC,c_void_p,POINTER(win32more.Graphics.Gdi.TTLOADINFO_head))(('TTGetEmbeddedFontInfo', windll['t2embed.dll']), ((1, 'ulFlags'),(1, 'pulPrivStatus'),(1, 'ulPrivs'),(1, 'pulStatus'),(1, 'lpfnReadFromStream'),(1, 'lpvReadStream'),(1, 'pTTLoadInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TTDeleteEmbeddedFont():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,UInt32,POINTER(UInt32))(('TTDeleteEmbeddedFont', windll['t2embed.dll']), ((1, 'hFontReference'),(1, 'ulFlags'),(1, 'pulStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TTGetEmbeddingType():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,POINTER(win32more.Graphics.Gdi.EMBEDDED_FONT_PRIV_STATUS))(('TTGetEmbeddingType', windll['t2embed.dll']), ((1, 'hDC'),(1, 'pulEmbedType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TTCharToUnicode():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,c_char_p_no,UInt32,POINTER(UInt16),UInt32,UInt32)(('TTCharToUnicode', windll['t2embed.dll']), ((1, 'hDC'),(1, 'pucCharCodes'),(1, 'ulCharCodeSize'),(1, 'pusShortCodes'),(1, 'ulShortCodeSize'),(1, 'ulFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TTRunValidationTests():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,POINTER(win32more.Graphics.Gdi.TTVALIDATIONTESTSPARAMS_head))(('TTRunValidationTests', windll['t2embed.dll']), ((1, 'hDC'),(1, 'pTestParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TTIsEmbeddingEnabled():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.BOOL))(('TTIsEmbeddingEnabled', windll['t2embed.dll']), ((1, 'hDC'),(1, 'pbEnabled'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TTIsEmbeddingEnabledForFacename():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,POINTER(win32more.Foundation.BOOL))(('TTIsEmbeddingEnabledForFacename', windll['t2embed.dll']), ((1, 'lpszFacename'),(1, 'pbEnabled'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TTEnableEmbeddingForFacename():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,win32more.Foundation.BOOL)(('TTEnableEmbeddingForFacename', windll['t2embed.dll']), ((1, 'lpszFacename'),(1, 'bEnable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TTEmbedFontEx():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.TTEMBED_FLAGS,win32more.Graphics.Gdi.EMBED_FONT_CHARSET,POINTER(win32more.Graphics.Gdi.EMBEDDED_FONT_PRIV_STATUS),POINTER(UInt32),win32more.Graphics.Gdi.WRITEEMBEDPROC,c_void_p,POINTER(UInt32),UInt16,UInt16,POINTER(win32more.Graphics.Gdi.TTEMBEDINFO_head))(('TTEmbedFontEx', windll['t2embed.dll']), ((1, 'hDC'),(1, 'ulFlags'),(1, 'ulCharSet'),(1, 'pulPrivStatus'),(1, 'pulStatus'),(1, 'lpfnWriteToStream'),(1, 'lpvWriteStream'),(1, 'pulCharCodeSet'),(1, 'usCharCodeCount'),(1, 'usLanguage'),(1, 'pTTEmbedInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TTRunValidationTestsEx():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,POINTER(win32more.Graphics.Gdi.TTVALIDATIONTESTSPARAMSEX_head))(('TTRunValidationTestsEx', windll['t2embed.dll']), ((1, 'hDC'),(1, 'pTestParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TTGetNewFontName():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Foundation.HANDLE),win32more.Foundation.PWSTR,Int32,win32more.Foundation.PSTR,Int32)(('TTGetNewFontName', windll['t2embed.dll']), ((1, 'phFontReference'),(1, 'wzWinFamilyName'),(1, 'cchMaxWinName'),(1, 'szMacFamilyName'),(1, 'cchMaxMacName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrawEdge():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.RECT_head),win32more.Graphics.Gdi.DRAWEDGE_FLAGS,win32more.Graphics.Gdi.DRAW_EDGE_FLAGS)(('DrawEdge', windll['USER32.dll']), ((1, 'hdc'),(1, 'qrc'),(1, 'edge'),(1, 'grfFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrawFrameControl():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.RECT_head),win32more.Graphics.Gdi.DFC_TYPE,win32more.Graphics.Gdi.DFCS_STATE)(('DrawFrameControl', windll['USER32.dll']), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrawCaption():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.RECT_head),win32more.Graphics.Gdi.DRAW_CAPTION_FLAGS)(('DrawCaption', windll['USER32.dll']), ((1, 'hwnd'),(1, 'hdc'),(1, 'lprect'),(1, 'flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrawAnimatedRects():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,Int32,POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.RECT_head))(('DrawAnimatedRects', windll['USER32.dll']), ((1, 'hwnd'),(1, 'idAni'),(1, 'lprcFrom'),(1, 'lprcTo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrawTextA():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,win32more.Foundation.PSTR,Int32,POINTER(win32more.Foundation.RECT_head),win32more.Graphics.Gdi.DRAW_TEXT_FORMAT)(('DrawTextA', windll['USER32.dll']), ((1, 'hdc'),(1, 'lpchText'),(1, 'cchText'),(1, 'lprc'),(1, 'format'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrawTextW():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,win32more.Foundation.PWSTR,Int32,POINTER(win32more.Foundation.RECT_head),win32more.Graphics.Gdi.DRAW_TEXT_FORMAT)(('DrawTextW', windll['USER32.dll']), ((1, 'hdc'),(1, 'lpchText'),(1, 'cchText'),(1, 'lprc'),(1, 'format'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrawTextExA():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,win32more.Foundation.PSTR,Int32,POINTER(win32more.Foundation.RECT_head),win32more.Graphics.Gdi.DRAW_TEXT_FORMAT,POINTER(win32more.Graphics.Gdi.DRAWTEXTPARAMS_head))(('DrawTextExA', windll['USER32.dll']), ((1, 'hdc'),(1, 'lpchText'),(1, 'cchText'),(1, 'lprc'),(1, 'format'),(1, 'lpdtp'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrawTextExW():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,win32more.Foundation.PWSTR,Int32,POINTER(win32more.Foundation.RECT_head),win32more.Graphics.Gdi.DRAW_TEXT_FORMAT,POINTER(win32more.Graphics.Gdi.DRAWTEXTPARAMS_head))(('DrawTextExW', windll['USER32.dll']), ((1, 'hdc'),(1, 'lpchText'),(1, 'cchText'),(1, 'lprc'),(1, 'format'),(1, 'lpdtp'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GrayStringA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HBRUSH,win32more.Graphics.Gdi.GRAYSTRINGPROC,win32more.Foundation.LPARAM,Int32,Int32,Int32,Int32,Int32)(('GrayStringA', windll['USER32.dll']), ((1, 'hDC'),(1, 'hBrush'),(1, 'lpOutputFunc'),(1, 'lpData'),(1, 'nCount'),(1, 'X'),(1, 'Y'),(1, 'nWidth'),(1, 'nHeight'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GrayStringW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HBRUSH,win32more.Graphics.Gdi.GRAYSTRINGPROC,win32more.Foundation.LPARAM,Int32,Int32,Int32,Int32,Int32)(('GrayStringW', windll['USER32.dll']), ((1, 'hDC'),(1, 'hBrush'),(1, 'lpOutputFunc'),(1, 'lpData'),(1, 'nCount'),(1, 'X'),(1, 'Y'),(1, 'nWidth'),(1, 'nHeight'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrawStateA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HBRUSH,win32more.Graphics.Gdi.DRAWSTATEPROC,win32more.Foundation.LPARAM,win32more.Foundation.WPARAM,Int32,Int32,Int32,Int32,win32more.Graphics.Gdi.DRAWSTATE_FLAGS)(('DrawStateA', windll['USER32.dll']), ((1, 'hdc'),(1, 'hbrFore'),(1, 'qfnCallBack'),(1, 'lData'),(1, 'wData'),(1, 'x'),(1, 'y'),(1, 'cx'),(1, 'cy'),(1, 'uFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrawStateW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HBRUSH,win32more.Graphics.Gdi.DRAWSTATEPROC,win32more.Foundation.LPARAM,win32more.Foundation.WPARAM,Int32,Int32,Int32,Int32,win32more.Graphics.Gdi.DRAWSTATE_FLAGS)(('DrawStateW', windll['USER32.dll']), ((1, 'hdc'),(1, 'hbrFore'),(1, 'qfnCallBack'),(1, 'lData'),(1, 'wData'),(1, 'x'),(1, 'y'),(1, 'cx'),(1, 'cy'),(1, 'uFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TabbedTextOutA():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,Int32,Int32,win32more.Foundation.PSTR,Int32,Int32,POINTER(Int32),Int32)(('TabbedTextOutA', windll['USER32.dll']), ((1, 'hdc'),(1, 'x'),(1, 'y'),(1, 'lpString'),(1, 'chCount'),(1, 'nTabPositions'),(1, 'lpnTabStopPositions'),(1, 'nTabOrigin'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TabbedTextOutW():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,Int32,Int32,win32more.Foundation.PWSTR,Int32,Int32,POINTER(Int32),Int32)(('TabbedTextOutW', windll['USER32.dll']), ((1, 'hdc'),(1, 'x'),(1, 'y'),(1, 'lpString'),(1, 'chCount'),(1, 'nTabPositions'),(1, 'lpnTabStopPositions'),(1, 'nTabOrigin'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTabbedTextExtentA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HDC,win32more.Foundation.PSTR,Int32,Int32,POINTER(Int32))(('GetTabbedTextExtentA', windll['USER32.dll']), ((1, 'hdc'),(1, 'lpString'),(1, 'chCount'),(1, 'nTabPositions'),(1, 'lpnTabStopPositions'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTabbedTextExtentW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.HDC,win32more.Foundation.PWSTR,Int32,Int32,POINTER(Int32))(('GetTabbedTextExtentW', windll['USER32.dll']), ((1, 'hdc'),(1, 'lpString'),(1, 'chCount'),(1, 'nTabPositions'),(1, 'lpnTabStopPositions'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UpdateWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND)(('UpdateWindow', windll['USER32.dll']), ((1, 'hWnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PaintDesktop():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC)(('PaintDesktop', windll['USER32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WindowFromDC():
    try:
        return WINFUNCTYPE(win32more.Foundation.HWND,win32more.Graphics.Gdi.HDC)(('WindowFromDC', windll['USER32.dll']), ((1, 'hDC'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDC():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HDC,win32more.Foundation.HWND)(('GetDC', windll['USER32.dll']), ((1, 'hWnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDCEx():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HDC,win32more.Foundation.HWND,win32more.Graphics.Gdi.HRGN,win32more.Graphics.Gdi.GET_DCX_FLAGS)(('GetDCEx', windll['USER32.dll']), ((1, 'hWnd'),(1, 'hrgnClip'),(1, 'flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetWindowDC():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HDC,win32more.Foundation.HWND)(('GetWindowDC', windll['USER32.dll']), ((1, 'hWnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReleaseDC():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HWND,win32more.Graphics.Gdi.HDC)(('ReleaseDC', windll['USER32.dll']), ((1, 'hWnd'),(1, 'hDC'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BeginPaint():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HDC,win32more.Foundation.HWND,POINTER(win32more.Graphics.Gdi.PAINTSTRUCT_head))(('BeginPaint', windll['USER32.dll']), ((1, 'hWnd'),(1, 'lpPaint'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EndPaint():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,POINTER(win32more.Graphics.Gdi.PAINTSTRUCT_head))(('EndPaint', windll['USER32.dll']), ((1, 'hWnd'),(1, 'lpPaint'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetUpdateRect():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,POINTER(win32more.Foundation.RECT_head),win32more.Foundation.BOOL)(('GetUpdateRect', windll['USER32.dll']), ((1, 'hWnd'),(1, 'lpRect'),(1, 'bErase'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetUpdateRgn():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.GDI_REGION_TYPE,win32more.Foundation.HWND,win32more.Graphics.Gdi.HRGN,win32more.Foundation.BOOL)(('GetUpdateRgn', windll['USER32.dll']), ((1, 'hWnd'),(1, 'hRgn'),(1, 'bErase'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetWindowRgn():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HWND,win32more.Graphics.Gdi.HRGN,win32more.Foundation.BOOL)(('SetWindowRgn', windll['USER32.dll']), ((1, 'hWnd'),(1, 'hRgn'),(1, 'bRedraw'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetWindowRgn():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.GDI_REGION_TYPE,win32more.Foundation.HWND,win32more.Graphics.Gdi.HRGN)(('GetWindowRgn', windll['USER32.dll']), ((1, 'hWnd'),(1, 'hRgn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetWindowRgnBox():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.GDI_REGION_TYPE,win32more.Foundation.HWND,POINTER(win32more.Foundation.RECT_head))(('GetWindowRgnBox', windll['USER32.dll']), ((1, 'hWnd'),(1, 'lprc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ExcludeUpdateRgn():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,win32more.Foundation.HWND)(('ExcludeUpdateRgn', windll['USER32.dll']), ((1, 'hDC'),(1, 'hWnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InvalidateRect():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,POINTER(win32more.Foundation.RECT_head),win32more.Foundation.BOOL)(('InvalidateRect', windll['USER32.dll']), ((1, 'hWnd'),(1, 'lpRect'),(1, 'bErase'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ValidateRect():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,POINTER(win32more.Foundation.RECT_head))(('ValidateRect', windll['USER32.dll']), ((1, 'hWnd'),(1, 'lpRect'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InvalidateRgn():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.Graphics.Gdi.HRGN,win32more.Foundation.BOOL)(('InvalidateRgn', windll['USER32.dll']), ((1, 'hWnd'),(1, 'hRgn'),(1, 'bErase'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ValidateRgn():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.Graphics.Gdi.HRGN)(('ValidateRgn', windll['USER32.dll']), ((1, 'hWnd'),(1, 'hRgn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RedrawWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,POINTER(win32more.Foundation.RECT_head),win32more.Graphics.Gdi.HRGN,win32more.Graphics.Gdi.REDRAW_WINDOW_FLAGS)(('RedrawWindow', windll['USER32.dll']), ((1, 'hWnd'),(1, 'lprcUpdate'),(1, 'hrgnUpdate'),(1, 'flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LockWindowUpdate():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND)(('LockWindowUpdate', windll['USER32.dll']), ((1, 'hWndLock'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ClientToScreen():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,POINTER(win32more.Foundation.POINT_head))(('ClientToScreen', windll['USER32.dll']), ((1, 'hWnd'),(1, 'lpPoint'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ScreenToClient():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,POINTER(win32more.Foundation.POINT_head))(('ScreenToClient', windll['USER32.dll']), ((1, 'hWnd'),(1, 'lpPoint'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MapWindowPoints():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HWND,win32more.Foundation.HWND,POINTER(win32more.Foundation.POINT_head),UInt32)(('MapWindowPoints', windll['USER32.dll']), ((1, 'hWndFrom'),(1, 'hWndTo'),(1, 'lpPoints'),(1, 'cPoints'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSysColor():
    try:
        return WINFUNCTYPE(UInt32,win32more.Graphics.Gdi.SYS_COLOR_INDEX)(('GetSysColor', windll['USER32.dll']), ((1, 'nIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSysColorBrush():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HBRUSH,win32more.Graphics.Gdi.SYS_COLOR_INDEX)(('GetSysColorBrush', windll['USER32.dll']), ((1, 'nIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetSysColors():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,Int32,POINTER(Int32),POINTER(win32more.Foundation.COLORREF))(('SetSysColors', windll['USER32.dll']), ((1, 'cElements'),(1, 'lpaElements'),(1, 'lpaRgbValues'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DrawFocusRect():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.RECT_head))(('DrawFocusRect', windll['USER32.dll']), ((1, 'hDC'),(1, 'lprc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FillRect():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.RECT_head),win32more.Graphics.Gdi.HBRUSH)(('FillRect', windll['USER32.dll']), ((1, 'hDC'),(1, 'lprc'),(1, 'hbr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FrameRect():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.RECT_head),win32more.Graphics.Gdi.HBRUSH)(('FrameRect', windll['USER32.dll']), ((1, 'hDC'),(1, 'lprc'),(1, 'hbr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InvertRect():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.RECT_head))(('InvertRect', windll['USER32.dll']), ((1, 'hDC'),(1, 'lprc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetRect():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.RECT_head),Int32,Int32,Int32,Int32)(('SetRect', windll['USER32.dll']), ((1, 'lprc'),(1, 'xLeft'),(1, 'yTop'),(1, 'xRight'),(1, 'yBottom'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetRectEmpty():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.RECT_head))(('SetRectEmpty', windll['USER32.dll']), ((1, 'lprc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CopyRect():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.RECT_head))(('CopyRect', windll['USER32.dll']), ((1, 'lprcDst'),(1, 'lprcSrc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InflateRect():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.RECT_head),Int32,Int32)(('InflateRect', windll['USER32.dll']), ((1, 'lprc'),(1, 'dx'),(1, 'dy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IntersectRect():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.RECT_head))(('IntersectRect', windll['USER32.dll']), ((1, 'lprcDst'),(1, 'lprcSrc1'),(1, 'lprcSrc2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnionRect():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.RECT_head))(('UnionRect', windll['USER32.dll']), ((1, 'lprcDst'),(1, 'lprcSrc1'),(1, 'lprcSrc2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SubtractRect():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.RECT_head))(('SubtractRect', windll['USER32.dll']), ((1, 'lprcDst'),(1, 'lprcSrc1'),(1, 'lprcSrc2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OffsetRect():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.RECT_head),Int32,Int32)(('OffsetRect', windll['USER32.dll']), ((1, 'lprc'),(1, 'dx'),(1, 'dy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsRectEmpty():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.RECT_head))(('IsRectEmpty', windll['USER32.dll']), ((1, 'lprc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EqualRect():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.RECT_head))(('EqualRect', windll['USER32.dll']), ((1, 'lprc1'),(1, 'lprc2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PtInRect():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.RECT_head),win32more.Foundation.POINT)(('PtInRect', windll['USER32.dll']), ((1, 'lprc'),(1, 'pt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadBitmapA():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HBITMAP,win32more.Foundation.HINSTANCE,win32more.Foundation.PSTR)(('LoadBitmapA', windll['USER32.dll']), ((1, 'hInstance'),(1, 'lpBitmapName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadBitmapW():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HBITMAP,win32more.Foundation.HINSTANCE,win32more.Foundation.PWSTR)(('LoadBitmapW', windll['USER32.dll']), ((1, 'hInstance'),(1, 'lpBitmapName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ChangeDisplaySettingsA():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.DISP_CHANGE,POINTER(win32more.Graphics.Gdi.DEVMODEA_head),win32more.Graphics.Gdi.CDS_TYPE)(('ChangeDisplaySettingsA', windll['USER32.dll']), ((1, 'lpDevMode'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ChangeDisplaySettingsW():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.DISP_CHANGE,POINTER(win32more.Graphics.Gdi.DEVMODEW_head),win32more.Graphics.Gdi.CDS_TYPE)(('ChangeDisplaySettingsW', windll['USER32.dll']), ((1, 'lpDevMode'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ChangeDisplaySettingsExA():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.DISP_CHANGE,win32more.Foundation.PSTR,POINTER(win32more.Graphics.Gdi.DEVMODEA_head),win32more.Foundation.HWND,win32more.Graphics.Gdi.CDS_TYPE,c_void_p)(('ChangeDisplaySettingsExA', windll['USER32.dll']), ((1, 'lpszDeviceName'),(1, 'lpDevMode'),(1, 'hwnd'),(1, 'dwflags'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ChangeDisplaySettingsExW():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.DISP_CHANGE,win32more.Foundation.PWSTR,POINTER(win32more.Graphics.Gdi.DEVMODEW_head),win32more.Foundation.HWND,win32more.Graphics.Gdi.CDS_TYPE,c_void_p)(('ChangeDisplaySettingsExW', windll['USER32.dll']), ((1, 'lpszDeviceName'),(1, 'lpDevMode'),(1, 'hwnd'),(1, 'dwflags'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumDisplaySettingsA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Graphics.Gdi.ENUM_DISPLAY_SETTINGS_MODE,POINTER(win32more.Graphics.Gdi.DEVMODEA_head))(('EnumDisplaySettingsA', windll['USER32.dll']), ((1, 'lpszDeviceName'),(1, 'iModeNum'),(1, 'lpDevMode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumDisplaySettingsW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Graphics.Gdi.ENUM_DISPLAY_SETTINGS_MODE,POINTER(win32more.Graphics.Gdi.DEVMODEW_head))(('EnumDisplaySettingsW', windll['USER32.dll']), ((1, 'lpszDeviceName'),(1, 'iModeNum'),(1, 'lpDevMode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumDisplaySettingsExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Graphics.Gdi.ENUM_DISPLAY_SETTINGS_MODE,POINTER(win32more.Graphics.Gdi.DEVMODEA_head),UInt32)(('EnumDisplaySettingsExA', windll['USER32.dll']), ((1, 'lpszDeviceName'),(1, 'iModeNum'),(1, 'lpDevMode'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumDisplaySettingsExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Graphics.Gdi.ENUM_DISPLAY_SETTINGS_MODE,POINTER(win32more.Graphics.Gdi.DEVMODEW_head),UInt32)(('EnumDisplaySettingsExW', windll['USER32.dll']), ((1, 'lpszDeviceName'),(1, 'iModeNum'),(1, 'lpDevMode'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumDisplayDevicesA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,UInt32,POINTER(win32more.Graphics.Gdi.DISPLAY_DEVICEA_head),UInt32)(('EnumDisplayDevicesA', windll['USER32.dll']), ((1, 'lpDevice'),(1, 'iDevNum'),(1, 'lpDisplayDevice'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumDisplayDevicesW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Graphics.Gdi.DISPLAY_DEVICEW_head),UInt32)(('EnumDisplayDevicesW', windll['USER32.dll']), ((1, 'lpDevice'),(1, 'iDevNum'),(1, 'lpDisplayDevice'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MonitorFromPoint():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HMONITOR,win32more.Foundation.POINT,win32more.Graphics.Gdi.MONITOR_FROM_FLAGS)(('MonitorFromPoint', windll['USER32.dll']), ((1, 'pt'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MonitorFromRect():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HMONITOR,POINTER(win32more.Foundation.RECT_head),win32more.Graphics.Gdi.MONITOR_FROM_FLAGS)(('MonitorFromRect', windll['USER32.dll']), ((1, 'lprc'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MonitorFromWindow():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HMONITOR,win32more.Foundation.HWND,win32more.Graphics.Gdi.MONITOR_FROM_FLAGS)(('MonitorFromWindow', windll['USER32.dll']), ((1, 'hwnd'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetMonitorInfoA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HMONITOR,POINTER(win32more.Graphics.Gdi.MONITORINFO_head))(('GetMonitorInfoA', windll['USER32.dll']), ((1, 'hMonitor'),(1, 'lpmi'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetMonitorInfoW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HMONITOR,POINTER(win32more.Graphics.Gdi.MONITORINFO_head))(('GetMonitorInfoW', windll['USER32.dll']), ((1, 'hMonitor'),(1, 'lpmi'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumDisplayMonitors():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.RECT_head),win32more.Graphics.Gdi.MONITORENUMPROC,win32more.Foundation.LPARAM)(('EnumDisplayMonitors', windll['USER32.dll']), ((1, 'hdc'),(1, 'lprcClip'),(1, 'lpfnEnum'),(1, 'dwData'),))
    except (FileNotFoundError, AttributeError):
        return None
ARC_DIRECTION = UInt32
AD_COUNTERCLOCKWISE = 1
AD_CLOCKWISE = 2
def _define_AXESLISTA_head():
    class AXESLISTA(Structure):
        pass
    return AXESLISTA
def _define_AXESLISTA():
    AXESLISTA = win32more.Graphics.Gdi.AXESLISTA_head
    AXESLISTA._fields_ = [
        ('axlReserved', UInt32),
        ('axlNumAxes', UInt32),
        ('axlAxisInfo', win32more.Graphics.Gdi.AXISINFOA * 16),
    ]
    return AXESLISTA
def _define_AXESLISTW_head():
    class AXESLISTW(Structure):
        pass
    return AXESLISTW
def _define_AXESLISTW():
    AXESLISTW = win32more.Graphics.Gdi.AXESLISTW_head
    AXESLISTW._fields_ = [
        ('axlReserved', UInt32),
        ('axlNumAxes', UInt32),
        ('axlAxisInfo', win32more.Graphics.Gdi.AXISINFOW * 16),
    ]
    return AXESLISTW
def _define_AXISINFOA_head():
    class AXISINFOA(Structure):
        pass
    return AXISINFOA
def _define_AXISINFOA():
    AXISINFOA = win32more.Graphics.Gdi.AXISINFOA_head
    AXISINFOA._fields_ = [
        ('axMinValue', Int32),
        ('axMaxValue', Int32),
        ('axAxisName', Byte * 16),
    ]
    return AXISINFOA
def _define_AXISINFOW_head():
    class AXISINFOW(Structure):
        pass
    return AXISINFOW
def _define_AXISINFOW():
    AXISINFOW = win32more.Graphics.Gdi.AXISINFOW_head
    AXISINFOW._fields_ = [
        ('axMinValue', Int32),
        ('axMaxValue', Int32),
        ('axAxisName', Char * 16),
    ]
    return AXISINFOW
BACKGROUND_MODE = UInt32
OPAQUE = 2
TRANSPARENT = 1
BI_COMPRESSION = Int32
BI_RGB = 0
BI_RLE8 = 1
BI_RLE4 = 2
BI_BITFIELDS = 3
BI_JPEG = 4
BI_PNG = 5
def _define_BITMAP_head():
    class BITMAP(Structure):
        pass
    return BITMAP
def _define_BITMAP():
    BITMAP = win32more.Graphics.Gdi.BITMAP_head
    BITMAP._fields_ = [
        ('bmType', Int32),
        ('bmWidth', Int32),
        ('bmHeight', Int32),
        ('bmWidthBytes', Int32),
        ('bmPlanes', UInt16),
        ('bmBitsPixel', UInt16),
        ('bmBits', c_void_p),
    ]
    return BITMAP
def _define_BITMAPCOREHEADER_head():
    class BITMAPCOREHEADER(Structure):
        pass
    return BITMAPCOREHEADER
def _define_BITMAPCOREHEADER():
    BITMAPCOREHEADER = win32more.Graphics.Gdi.BITMAPCOREHEADER_head
    BITMAPCOREHEADER._fields_ = [
        ('bcSize', UInt32),
        ('bcWidth', UInt16),
        ('bcHeight', UInt16),
        ('bcPlanes', UInt16),
        ('bcBitCount', UInt16),
    ]
    return BITMAPCOREHEADER
def _define_BITMAPCOREINFO_head():
    class BITMAPCOREINFO(Structure):
        pass
    return BITMAPCOREINFO
def _define_BITMAPCOREINFO():
    BITMAPCOREINFO = win32more.Graphics.Gdi.BITMAPCOREINFO_head
    BITMAPCOREINFO._fields_ = [
        ('bmciHeader', win32more.Graphics.Gdi.BITMAPCOREHEADER),
        ('bmciColors', win32more.Graphics.Gdi.RGBTRIPLE * 1),
    ]
    return BITMAPCOREINFO
def _define_BITMAPFILEHEADER_head():
    class BITMAPFILEHEADER(Structure):
        pass
    return BITMAPFILEHEADER
def _define_BITMAPFILEHEADER():
    BITMAPFILEHEADER = win32more.Graphics.Gdi.BITMAPFILEHEADER_head
    BITMAPFILEHEADER._pack_ = 2
    BITMAPFILEHEADER._fields_ = [
        ('bfType', UInt16),
        ('bfSize', UInt32),
        ('bfReserved1', UInt16),
        ('bfReserved2', UInt16),
        ('bfOffBits', UInt32),
    ]
    return BITMAPFILEHEADER
def _define_BITMAPINFO_head():
    class BITMAPINFO(Structure):
        pass
    return BITMAPINFO
def _define_BITMAPINFO():
    BITMAPINFO = win32more.Graphics.Gdi.BITMAPINFO_head
    BITMAPINFO._fields_ = [
        ('bmiHeader', win32more.Graphics.Gdi.BITMAPINFOHEADER),
        ('bmiColors', win32more.Graphics.Gdi.RGBQUAD * 1),
    ]
    return BITMAPINFO
def _define_BITMAPINFOHEADER_head():
    class BITMAPINFOHEADER(Structure):
        pass
    return BITMAPINFOHEADER
def _define_BITMAPINFOHEADER():
    BITMAPINFOHEADER = win32more.Graphics.Gdi.BITMAPINFOHEADER_head
    BITMAPINFOHEADER._fields_ = [
        ('biSize', UInt32),
        ('biWidth', Int32),
        ('biHeight', Int32),
        ('biPlanes', UInt16),
        ('biBitCount', UInt16),
        ('biCompression', win32more.Graphics.Gdi.BI_COMPRESSION),
        ('biSizeImage', UInt32),
        ('biXPelsPerMeter', Int32),
        ('biYPelsPerMeter', Int32),
        ('biClrUsed', UInt32),
        ('biClrImportant', UInt32),
    ]
    return BITMAPINFOHEADER
def _define_BITMAPV4HEADER_head():
    class BITMAPV4HEADER(Structure):
        pass
    return BITMAPV4HEADER
def _define_BITMAPV4HEADER():
    BITMAPV4HEADER = win32more.Graphics.Gdi.BITMAPV4HEADER_head
    BITMAPV4HEADER._fields_ = [
        ('bV4Size', UInt32),
        ('bV4Width', Int32),
        ('bV4Height', Int32),
        ('bV4Planes', UInt16),
        ('bV4BitCount', UInt16),
        ('bV4V4Compression', win32more.Graphics.Gdi.BI_COMPRESSION),
        ('bV4SizeImage', UInt32),
        ('bV4XPelsPerMeter', Int32),
        ('bV4YPelsPerMeter', Int32),
        ('bV4ClrUsed', UInt32),
        ('bV4ClrImportant', UInt32),
        ('bV4RedMask', UInt32),
        ('bV4GreenMask', UInt32),
        ('bV4BlueMask', UInt32),
        ('bV4AlphaMask', UInt32),
        ('bV4CSType', UInt32),
        ('bV4Endpoints', win32more.Graphics.Gdi.CIEXYZTRIPLE),
        ('bV4GammaRed', UInt32),
        ('bV4GammaGreen', UInt32),
        ('bV4GammaBlue', UInt32),
    ]
    return BITMAPV4HEADER
def _define_BITMAPV5HEADER_head():
    class BITMAPV5HEADER(Structure):
        pass
    return BITMAPV5HEADER
def _define_BITMAPV5HEADER():
    BITMAPV5HEADER = win32more.Graphics.Gdi.BITMAPV5HEADER_head
    BITMAPV5HEADER._fields_ = [
        ('bV5Size', UInt32),
        ('bV5Width', Int32),
        ('bV5Height', Int32),
        ('bV5Planes', UInt16),
        ('bV5BitCount', UInt16),
        ('bV5Compression', win32more.Graphics.Gdi.BI_COMPRESSION),
        ('bV5SizeImage', UInt32),
        ('bV5XPelsPerMeter', Int32),
        ('bV5YPelsPerMeter', Int32),
        ('bV5ClrUsed', UInt32),
        ('bV5ClrImportant', UInt32),
        ('bV5RedMask', UInt32),
        ('bV5GreenMask', UInt32),
        ('bV5BlueMask', UInt32),
        ('bV5AlphaMask', UInt32),
        ('bV5CSType', UInt32),
        ('bV5Endpoints', win32more.Graphics.Gdi.CIEXYZTRIPLE),
        ('bV5GammaRed', UInt32),
        ('bV5GammaGreen', UInt32),
        ('bV5GammaBlue', UInt32),
        ('bV5Intent', UInt32),
        ('bV5ProfileData', UInt32),
        ('bV5ProfileSize', UInt32),
        ('bV5Reserved', UInt32),
    ]
    return BITMAPV5HEADER
def _define_BLENDFUNCTION_head():
    class BLENDFUNCTION(Structure):
        pass
    return BLENDFUNCTION
def _define_BLENDFUNCTION():
    BLENDFUNCTION = win32more.Graphics.Gdi.BLENDFUNCTION_head
    BLENDFUNCTION._fields_ = [
        ('BlendOp', Byte),
        ('BlendFlags', Byte),
        ('SourceConstantAlpha', Byte),
        ('AlphaFormat', Byte),
    ]
    return BLENDFUNCTION
BRUSH_STYLE = UInt32
BS_SOLID = 0
BS_NULL = 1
BS_HOLLOW = 1
BS_HATCHED = 2
BS_PATTERN = 3
BS_INDEXED = 4
BS_DIBPATTERN = 5
BS_DIBPATTERNPT = 6
BS_PATTERN8X8 = 7
BS_DIBPATTERN8X8 = 8
BS_MONOPATTERN = 9
CDS_TYPE = UInt32
CDS_FULLSCREEN = 4
CDS_GLOBAL = 8
CDS_NORESET = 268435456
CDS_RESET = 1073741824
CDS_SET_PRIMARY = 16
CDS_TEST = 2
CDS_UPDATEREGISTRY = 1
CDS_VIDEOPARAMETERS = 32
CDS_ENABLE_UNSAFE_MODES = 256
CDS_DISABLE_UNSAFE_MODES = 512
CDS_RESET_EX = 536870912
def _define_CFP_ALLOCPROC():
    return CFUNCTYPE(c_void_p,UIntPtr)
def _define_CFP_FREEPROC():
    return CFUNCTYPE(Void,c_void_p)
def _define_CFP_REALLOCPROC():
    return CFUNCTYPE(c_void_p,c_void_p,UIntPtr)
def _define_CIEXYZ_head():
    class CIEXYZ(Structure):
        pass
    return CIEXYZ
def _define_CIEXYZ():
    CIEXYZ = win32more.Graphics.Gdi.CIEXYZ_head
    CIEXYZ._fields_ = [
        ('ciexyzX', Int32),
        ('ciexyzY', Int32),
        ('ciexyzZ', Int32),
    ]
    return CIEXYZ
def _define_CIEXYZTRIPLE_head():
    class CIEXYZTRIPLE(Structure):
        pass
    return CIEXYZTRIPLE
def _define_CIEXYZTRIPLE():
    CIEXYZTRIPLE = win32more.Graphics.Gdi.CIEXYZTRIPLE_head
    CIEXYZTRIPLE._fields_ = [
        ('ciexyzRed', win32more.Graphics.Gdi.CIEXYZ),
        ('ciexyzGreen', win32more.Graphics.Gdi.CIEXYZ),
        ('ciexyzBlue', win32more.Graphics.Gdi.CIEXYZ),
    ]
    return CIEXYZTRIPLE
def _define_COLORADJUSTMENT_head():
    class COLORADJUSTMENT(Structure):
        pass
    return COLORADJUSTMENT
def _define_COLORADJUSTMENT():
    COLORADJUSTMENT = win32more.Graphics.Gdi.COLORADJUSTMENT_head
    COLORADJUSTMENT._fields_ = [
        ('caSize', UInt16),
        ('caFlags', UInt16),
        ('caIlluminantIndex', UInt16),
        ('caRedGamma', UInt16),
        ('caGreenGamma', UInt16),
        ('caBlueGamma', UInt16),
        ('caReferenceBlack', UInt16),
        ('caReferenceWhite', UInt16),
        ('caContrast', Int16),
        ('caBrightness', Int16),
        ('caColorfulness', Int16),
        ('caRedGreenTint', Int16),
    ]
    return COLORADJUSTMENT
CREATE_FONT_PACKAGE_SUBSET_ENCODING = UInt16
TTFCFP_STD_MAC_CHAR_SET = 0
TTFCFP_SYMBOL_CHAR_SET = 0
TTFCFP_UNICODE_CHAR_SET = 1
CREATE_FONT_PACKAGE_SUBSET_PLATFORM = UInt16
TTFCFP_UNICODE_PLATFORMID = 0
TTFCFP_ISO_PLATFORMID = 2
CREATE_POLYGON_RGN_MODE = UInt32
ALTERNATE = 1
WINDING = 2
CreatedHDC = IntPtr
DC_LAYOUT = UInt32
LAYOUT_BITMAPORIENTATIONPRESERVED = 8
LAYOUT_RTL = 1
def _define_DESIGNVECTOR_head():
    class DESIGNVECTOR(Structure):
        pass
    return DESIGNVECTOR
def _define_DESIGNVECTOR():
    DESIGNVECTOR = win32more.Graphics.Gdi.DESIGNVECTOR_head
    DESIGNVECTOR._fields_ = [
        ('dvReserved', UInt32),
        ('dvNumAxes', UInt32),
        ('dvValues', Int32 * 16),
    ]
    return DESIGNVECTOR
DEVMODE_COLLATE = UInt16
DMCOLLATE_FALSE = 0
DMCOLLATE_TRUE = 1
DEVMODE_COLOR = UInt16
DMCOLOR_MONOCHROME = 1
DMCOLOR_COLOR = 2
DEVMODE_DISPLAY_FIXED_OUTPUT = UInt32
DMDFO_DEFAULT = 0
DMDFO_STRETCH = 1
DMDFO_CENTER = 2
DEVMODE_DISPLAY_ORIENTATION = UInt32
DMDO_DEFAULT = 0
DMDO_90 = 1
DMDO_180 = 2
DMDO_270 = 3
DEVMODE_DUPLEX = UInt16
DMDUP_SIMPLEX = 1
DMDUP_VERTICAL = 2
DMDUP_HORIZONTAL = 3
DEVMODE_FIELD_FLAGS = UInt32
DM_SPECVERSION = 1025
DM_ORIENTATION = 1
DM_PAPERSIZE = 2
DM_PAPERLENGTH = 4
DM_PAPERWIDTH = 8
DM_SCALE = 16
DM_POSITION = 32
DM_NUP = 64
DM_DISPLAYORIENTATION = 128
DM_COPIES = 256
DM_DEFAULTSOURCE = 512
DM_PRINTQUALITY = 1024
DM_COLOR = 2048
DM_DUPLEX = 4096
DM_YRESOLUTION = 8192
DM_TTOPTION = 16384
DM_COLLATE = 32768
DM_FORMNAME = 65536
DM_LOGPIXELS = 131072
DM_BITSPERPEL = 262144
DM_PELSWIDTH = 524288
DM_PELSHEIGHT = 1048576
DM_DISPLAYFLAGS = 2097152
DM_DISPLAYFREQUENCY = 4194304
DM_ICMMETHOD = 8388608
DM_ICMINTENT = 16777216
DM_MEDIATYPE = 33554432
DM_DITHERTYPE = 67108864
DM_PANNINGWIDTH = 134217728
DM_PANNINGHEIGHT = 268435456
DM_DISPLAYFIXEDOUTPUT = 536870912
DM_INTERLACED = 2
DM_UPDATE = 1
DM_COPY = 2
DM_PROMPT = 4
DM_MODIFY = 8
DM_IN_BUFFER = 8
DM_IN_PROMPT = 4
DM_OUT_BUFFER = 2
DM_OUT_DEFAULT = 1
DEVMODE_TRUETYPE_OPTION = UInt16
DMTT_BITMAP = 1
DMTT_DOWNLOAD = 2
DMTT_SUBDEV = 3
DMTT_DOWNLOAD_OUTLINE = 4
def _define_DEVMODEA_head():
    class DEVMODEA(Structure):
        pass
    return DEVMODEA
def _define_DEVMODEA():
    DEVMODEA = win32more.Graphics.Gdi.DEVMODEA_head
    class DEVMODEA__Anonymous1_e__Union(Union):
        pass
    class DEVMODEA__Anonymous1_e__Union__Anonymous1_e__Struct(Structure):
        pass
    DEVMODEA__Anonymous1_e__Union__Anonymous1_e__Struct._fields_ = [
        ('dmOrientation', Int16),
        ('dmPaperSize', Int16),
        ('dmPaperLength', Int16),
        ('dmPaperWidth', Int16),
        ('dmScale', Int16),
        ('dmCopies', Int16),
        ('dmDefaultSource', Int16),
        ('dmPrintQuality', Int16),
    ]
    class DEVMODEA__Anonymous1_e__Union__Anonymous2_e__Struct(Structure):
        pass
    DEVMODEA__Anonymous1_e__Union__Anonymous2_e__Struct._fields_ = [
        ('dmPosition', win32more.Foundation.POINTL),
        ('dmDisplayOrientation', win32more.Graphics.Gdi.DEVMODE_DISPLAY_ORIENTATION),
        ('dmDisplayFixedOutput', win32more.Graphics.Gdi.DEVMODE_DISPLAY_FIXED_OUTPUT),
    ]
    DEVMODEA__Anonymous1_e__Union._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    DEVMODEA__Anonymous1_e__Union._fields_ = [
        ('Anonymous1', DEVMODEA__Anonymous1_e__Union__Anonymous1_e__Struct),
        ('Anonymous2', DEVMODEA__Anonymous1_e__Union__Anonymous2_e__Struct),
    ]
    class DEVMODEA__Anonymous2_e__Union(Union):
        pass
    DEVMODEA__Anonymous2_e__Union._fields_ = [
        ('dmDisplayFlags', UInt32),
        ('dmNup', UInt32),
    ]
    DEVMODEA._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    DEVMODEA._fields_ = [
        ('dmDeviceName', Byte * 32),
        ('dmSpecVersion', UInt16),
        ('dmDriverVersion', UInt16),
        ('dmSize', UInt16),
        ('dmDriverExtra', UInt16),
        ('dmFields', win32more.Graphics.Gdi.DEVMODE_FIELD_FLAGS),
        ('Anonymous1', DEVMODEA__Anonymous1_e__Union),
        ('dmColor', win32more.Graphics.Gdi.DEVMODE_COLOR),
        ('dmDuplex', win32more.Graphics.Gdi.DEVMODE_DUPLEX),
        ('dmYResolution', Int16),
        ('dmTTOption', win32more.Graphics.Gdi.DEVMODE_TRUETYPE_OPTION),
        ('dmCollate', win32more.Graphics.Gdi.DEVMODE_COLLATE),
        ('dmFormName', Byte * 32),
        ('dmLogPixels', UInt16),
        ('dmBitsPerPel', UInt32),
        ('dmPelsWidth', UInt32),
        ('dmPelsHeight', UInt32),
        ('Anonymous2', DEVMODEA__Anonymous2_e__Union),
        ('dmDisplayFrequency', UInt32),
        ('dmICMMethod', UInt32),
        ('dmICMIntent', UInt32),
        ('dmMediaType', UInt32),
        ('dmDitherType', UInt32),
        ('dmReserved1', UInt32),
        ('dmReserved2', UInt32),
        ('dmPanningWidth', UInt32),
        ('dmPanningHeight', UInt32),
    ]
    return DEVMODEA
def _define_DEVMODEW_head():
    class DEVMODEW(Structure):
        pass
    return DEVMODEW
def _define_DEVMODEW():
    DEVMODEW = win32more.Graphics.Gdi.DEVMODEW_head
    class DEVMODEW__Anonymous1_e__Union(Union):
        pass
    class DEVMODEW__Anonymous1_e__Union__Anonymous1_e__Struct(Structure):
        pass
    DEVMODEW__Anonymous1_e__Union__Anonymous1_e__Struct._fields_ = [
        ('dmOrientation', Int16),
        ('dmPaperSize', Int16),
        ('dmPaperLength', Int16),
        ('dmPaperWidth', Int16),
        ('dmScale', Int16),
        ('dmCopies', Int16),
        ('dmDefaultSource', Int16),
        ('dmPrintQuality', Int16),
    ]
    class DEVMODEW__Anonymous1_e__Union__Anonymous2_e__Struct(Structure):
        pass
    DEVMODEW__Anonymous1_e__Union__Anonymous2_e__Struct._fields_ = [
        ('dmPosition', win32more.Foundation.POINTL),
        ('dmDisplayOrientation', win32more.Graphics.Gdi.DEVMODE_DISPLAY_ORIENTATION),
        ('dmDisplayFixedOutput', win32more.Graphics.Gdi.DEVMODE_DISPLAY_FIXED_OUTPUT),
    ]
    DEVMODEW__Anonymous1_e__Union._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    DEVMODEW__Anonymous1_e__Union._fields_ = [
        ('Anonymous1', DEVMODEW__Anonymous1_e__Union__Anonymous1_e__Struct),
        ('Anonymous2', DEVMODEW__Anonymous1_e__Union__Anonymous2_e__Struct),
    ]
    class DEVMODEW__Anonymous2_e__Union(Union):
        pass
    DEVMODEW__Anonymous2_e__Union._fields_ = [
        ('dmDisplayFlags', UInt32),
        ('dmNup', UInt32),
    ]
    DEVMODEW._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    DEVMODEW._fields_ = [
        ('dmDeviceName', Char * 32),
        ('dmSpecVersion', UInt16),
        ('dmDriverVersion', UInt16),
        ('dmSize', UInt16),
        ('dmDriverExtra', UInt16),
        ('dmFields', win32more.Graphics.Gdi.DEVMODE_FIELD_FLAGS),
        ('Anonymous1', DEVMODEW__Anonymous1_e__Union),
        ('dmColor', win32more.Graphics.Gdi.DEVMODE_COLOR),
        ('dmDuplex', win32more.Graphics.Gdi.DEVMODE_DUPLEX),
        ('dmYResolution', Int16),
        ('dmTTOption', win32more.Graphics.Gdi.DEVMODE_TRUETYPE_OPTION),
        ('dmCollate', win32more.Graphics.Gdi.DEVMODE_COLLATE),
        ('dmFormName', Char * 32),
        ('dmLogPixels', UInt16),
        ('dmBitsPerPel', UInt32),
        ('dmPelsWidth', UInt32),
        ('dmPelsHeight', UInt32),
        ('Anonymous2', DEVMODEW__Anonymous2_e__Union),
        ('dmDisplayFrequency', UInt32),
        ('dmICMMethod', UInt32),
        ('dmICMIntent', UInt32),
        ('dmMediaType', UInt32),
        ('dmDitherType', UInt32),
        ('dmReserved1', UInt32),
        ('dmReserved2', UInt32),
        ('dmPanningWidth', UInt32),
        ('dmPanningHeight', UInt32),
    ]
    return DEVMODEW
DFC_TYPE = UInt32
DFC_CAPTION = 1
DFC_MENU = 2
DFC_SCROLL = 3
DFC_BUTTON = 4
DFC_POPUPMENU = 5
DFCS_STATE = UInt32
DFCS_CAPTIONCLOSE = 0
DFCS_CAPTIONMIN = 1
DFCS_CAPTIONMAX = 2
DFCS_CAPTIONRESTORE = 3
DFCS_CAPTIONHELP = 4
DFCS_MENUARROW = 0
DFCS_MENUCHECK = 1
DFCS_MENUBULLET = 2
DFCS_MENUARROWRIGHT = 4
DFCS_SCROLLUP = 0
DFCS_SCROLLDOWN = 1
DFCS_SCROLLLEFT = 2
DFCS_SCROLLRIGHT = 3
DFCS_SCROLLCOMBOBOX = 5
DFCS_SCROLLSIZEGRIP = 8
DFCS_SCROLLSIZEGRIPRIGHT = 16
DFCS_BUTTONCHECK = 0
DFCS_BUTTONRADIOIMAGE = 1
DFCS_BUTTONRADIOMASK = 2
DFCS_BUTTONRADIO = 4
DFCS_BUTTON3STATE = 8
DFCS_BUTTONPUSH = 16
DFCS_INACTIVE = 256
DFCS_PUSHED = 512
DFCS_CHECKED = 1024
DFCS_TRANSPARENT = 2048
DFCS_HOT = 4096
DFCS_ADJUSTRECT = 8192
DFCS_FLAT = 16384
DFCS_MONO = 32768
DIB_USAGE = UInt32
DIB_RGB_COLORS = 0
DIB_PAL_COLORS = 1
def _define_DIBSECTION_head():
    class DIBSECTION(Structure):
        pass
    return DIBSECTION
def _define_DIBSECTION():
    DIBSECTION = win32more.Graphics.Gdi.DIBSECTION_head
    DIBSECTION._fields_ = [
        ('dsBm', win32more.Graphics.Gdi.BITMAP),
        ('dsBmih', win32more.Graphics.Gdi.BITMAPINFOHEADER),
        ('dsBitfields', UInt32 * 3),
        ('dshSection', win32more.Foundation.HANDLE),
        ('dsOffset', UInt32),
    ]
    return DIBSECTION
DISP_CHANGE = Int32
DISP_CHANGE_SUCCESSFUL = 0
DISP_CHANGE_RESTART = 1
DISP_CHANGE_FAILED = -1
DISP_CHANGE_BADMODE = -2
DISP_CHANGE_NOTUPDATED = -3
DISP_CHANGE_BADFLAGS = -4
DISP_CHANGE_BADPARAM = -5
DISP_CHANGE_BADDUALVIEW = -6
def _define_DISPLAY_DEVICEA_head():
    class DISPLAY_DEVICEA(Structure):
        pass
    return DISPLAY_DEVICEA
def _define_DISPLAY_DEVICEA():
    DISPLAY_DEVICEA = win32more.Graphics.Gdi.DISPLAY_DEVICEA_head
    DISPLAY_DEVICEA._fields_ = [
        ('cb', UInt32),
        ('DeviceName', win32more.Foundation.CHAR * 32),
        ('DeviceString', win32more.Foundation.CHAR * 128),
        ('StateFlags', UInt32),
        ('DeviceID', win32more.Foundation.CHAR * 128),
        ('DeviceKey', win32more.Foundation.CHAR * 128),
    ]
    return DISPLAY_DEVICEA
def _define_DISPLAY_DEVICEW_head():
    class DISPLAY_DEVICEW(Structure):
        pass
    return DISPLAY_DEVICEW
def _define_DISPLAY_DEVICEW():
    DISPLAY_DEVICEW = win32more.Graphics.Gdi.DISPLAY_DEVICEW_head
    DISPLAY_DEVICEW._fields_ = [
        ('cb', UInt32),
        ('DeviceName', Char * 32),
        ('DeviceString', Char * 128),
        ('StateFlags', UInt32),
        ('DeviceID', Char * 128),
        ('DeviceKey', Char * 128),
    ]
    return DISPLAY_DEVICEW
DISPLAYCONFIG_COLOR_ENCODING = Int32
DISPLAYCONFIG_COLOR_ENCODING_RGB = 0
DISPLAYCONFIG_COLOR_ENCODING_YCBCR444 = 1
DISPLAYCONFIG_COLOR_ENCODING_YCBCR422 = 2
DISPLAYCONFIG_COLOR_ENCODING_YCBCR420 = 3
DISPLAYCONFIG_COLOR_ENCODING_INTENSITY = 4
DISPLAYCONFIG_COLOR_ENCODING_FORCE_UINT32 = -1
DRAW_CAPTION_FLAGS = UInt32
DC_ACTIVE = 1
DC_BUTTONS = 4096
DC_GRADIENT = 32
DC_ICON = 4
DC_INBUTTON = 16
DC_SMALLCAP = 2
DC_TEXT = 8
DRAW_EDGE_FLAGS = UInt32
BF_ADJUST = 8192
BF_BOTTOM = 8
BF_BOTTOMLEFT = 9
BF_BOTTOMRIGHT = 12
BF_DIAGONAL = 16
BF_DIAGONAL_ENDBOTTOMLEFT = 25
BF_DIAGONAL_ENDBOTTOMRIGHT = 28
BF_DIAGONAL_ENDTOPLEFT = 19
BF_DIAGONAL_ENDTOPRIGHT = 22
BF_FLAT = 16384
BF_LEFT = 1
BF_MIDDLE = 2048
BF_MONO = 32768
BF_RECT = 15
BF_RIGHT = 4
BF_SOFT = 4096
BF_TOP = 2
BF_TOPLEFT = 3
BF_TOPRIGHT = 6
DRAW_TEXT_FORMAT = UInt32
DT_BOTTOM = 8
DT_CALCRECT = 1024
DT_CENTER = 1
DT_EDITCONTROL = 8192
DT_END_ELLIPSIS = 32768
DT_EXPANDTABS = 64
DT_EXTERNALLEADING = 512
DT_HIDEPREFIX = 1048576
DT_INTERNAL = 4096
DT_LEFT = 0
DT_MODIFYSTRING = 65536
DT_NOCLIP = 256
DT_NOFULLWIDTHCHARBREAK = 524288
DT_NOPREFIX = 2048
DT_PATH_ELLIPSIS = 16384
DT_PREFIXONLY = 2097152
DT_RIGHT = 2
DT_RTLREADING = 131072
DT_SINGLELINE = 32
DT_TABSTOP = 128
DT_TOP = 0
DT_VCENTER = 4
DT_WORDBREAK = 16
DT_WORD_ELLIPSIS = 262144
DRAWEDGE_FLAGS = UInt32
BDR_RAISEDOUTER = 1
BDR_SUNKENOUTER = 2
BDR_RAISEDINNER = 4
BDR_SUNKENINNER = 8
BDR_OUTER = 3
BDR_INNER = 12
BDR_RAISED = 5
BDR_SUNKEN = 10
EDGE_RAISED = 5
EDGE_SUNKEN = 10
EDGE_ETCHED = 6
EDGE_BUMP = 9
DRAWSTATE_FLAGS = UInt32
DST_COMPLEX = 0
DST_TEXT = 1
DST_PREFIXTEXT = 2
DST_ICON = 3
DST_BITMAP = 4
DSS_NORMAL = 0
DSS_UNION = 16
DSS_DISABLED = 32
DSS_MONO = 128
DSS_HIDEPREFIX = 512
DSS_PREFIXONLY = 1024
DSS_RIGHT = 32768
def _define_DRAWSTATEPROC():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,win32more.Foundation.LPARAM,win32more.Foundation.WPARAM,Int32,Int32)
def _define_DRAWTEXTPARAMS_head():
    class DRAWTEXTPARAMS(Structure):
        pass
    return DRAWTEXTPARAMS
def _define_DRAWTEXTPARAMS():
    DRAWTEXTPARAMS = win32more.Graphics.Gdi.DRAWTEXTPARAMS_head
    DRAWTEXTPARAMS._fields_ = [
        ('cbSize', UInt32),
        ('iTabLength', Int32),
        ('iLeftMargin', Int32),
        ('iRightMargin', Int32),
        ('uiLengthDrawn', UInt32),
    ]
    return DRAWTEXTPARAMS
EMBED_FONT_CHARSET = UInt32
CHARSET_UNICODE = 1
CHARSET_SYMBOL = 2
EMBEDDED_FONT_PRIV_STATUS = UInt32
EMBED_PREVIEWPRINT = 1
EMBED_EDITABLE = 2
EMBED_INSTALLABLE = 3
EMBED_NOEMBEDDING = 4
def _define_EMR_head():
    class EMR(Structure):
        pass
    return EMR
def _define_EMR():
    EMR = win32more.Graphics.Gdi.EMR_head
    EMR._fields_ = [
        ('iType', win32more.Graphics.Gdi.ENHANCED_METAFILE_RECORD_TYPE),
        ('nSize', UInt32),
    ]
    return EMR
def _define_EMRALPHABLEND_head():
    class EMRALPHABLEND(Structure):
        pass
    return EMRALPHABLEND
def _define_EMRALPHABLEND():
    EMRALPHABLEND = win32more.Graphics.Gdi.EMRALPHABLEND_head
    EMRALPHABLEND._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('rclBounds', win32more.Foundation.RECTL),
        ('xDest', Int32),
        ('yDest', Int32),
        ('cxDest', Int32),
        ('cyDest', Int32),
        ('dwRop', UInt32),
        ('xSrc', Int32),
        ('ySrc', Int32),
        ('xformSrc', win32more.Graphics.Gdi.XFORM),
        ('crBkColorSrc', win32more.Foundation.COLORREF),
        ('iUsageSrc', UInt32),
        ('offBmiSrc', UInt32),
        ('cbBmiSrc', UInt32),
        ('offBitsSrc', UInt32),
        ('cbBitsSrc', UInt32),
        ('cxSrc', Int32),
        ('cySrc', Int32),
    ]
    return EMRALPHABLEND
def _define_EMRANGLEARC_head():
    class EMRANGLEARC(Structure):
        pass
    return EMRANGLEARC
def _define_EMRANGLEARC():
    EMRANGLEARC = win32more.Graphics.Gdi.EMRANGLEARC_head
    EMRANGLEARC._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('ptlCenter', win32more.Foundation.POINTL),
        ('nRadius', UInt32),
        ('eStartAngle', Single),
        ('eSweepAngle', Single),
    ]
    return EMRANGLEARC
def _define_EMRARC_head():
    class EMRARC(Structure):
        pass
    return EMRARC
def _define_EMRARC():
    EMRARC = win32more.Graphics.Gdi.EMRARC_head
    EMRARC._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('rclBox', win32more.Foundation.RECTL),
        ('ptlStart', win32more.Foundation.POINTL),
        ('ptlEnd', win32more.Foundation.POINTL),
    ]
    return EMRARC
def _define_EMRBITBLT_head():
    class EMRBITBLT(Structure):
        pass
    return EMRBITBLT
def _define_EMRBITBLT():
    EMRBITBLT = win32more.Graphics.Gdi.EMRBITBLT_head
    EMRBITBLT._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('rclBounds', win32more.Foundation.RECTL),
        ('xDest', Int32),
        ('yDest', Int32),
        ('cxDest', Int32),
        ('cyDest', Int32),
        ('dwRop', UInt32),
        ('xSrc', Int32),
        ('ySrc', Int32),
        ('xformSrc', win32more.Graphics.Gdi.XFORM),
        ('crBkColorSrc', win32more.Foundation.COLORREF),
        ('iUsageSrc', UInt32),
        ('offBmiSrc', UInt32),
        ('cbBmiSrc', UInt32),
        ('offBitsSrc', UInt32),
        ('cbBitsSrc', UInt32),
    ]
    return EMRBITBLT
def _define_EMRCOLORCORRECTPALETTE_head():
    class EMRCOLORCORRECTPALETTE(Structure):
        pass
    return EMRCOLORCORRECTPALETTE
def _define_EMRCOLORCORRECTPALETTE():
    EMRCOLORCORRECTPALETTE = win32more.Graphics.Gdi.EMRCOLORCORRECTPALETTE_head
    EMRCOLORCORRECTPALETTE._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('ihPalette', UInt32),
        ('nFirstEntry', UInt32),
        ('nPalEntries', UInt32),
        ('nReserved', UInt32),
    ]
    return EMRCOLORCORRECTPALETTE
def _define_EMRCOLORMATCHTOTARGET_head():
    class EMRCOLORMATCHTOTARGET(Structure):
        pass
    return EMRCOLORMATCHTOTARGET
def _define_EMRCOLORMATCHTOTARGET():
    EMRCOLORMATCHTOTARGET = win32more.Graphics.Gdi.EMRCOLORMATCHTOTARGET_head
    EMRCOLORMATCHTOTARGET._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('dwAction', UInt32),
        ('dwFlags', UInt32),
        ('cbName', UInt32),
        ('cbData', UInt32),
        ('Data', Byte * 1),
    ]
    return EMRCOLORMATCHTOTARGET
def _define_EMRCREATEBRUSHINDIRECT_head():
    class EMRCREATEBRUSHINDIRECT(Structure):
        pass
    return EMRCREATEBRUSHINDIRECT
def _define_EMRCREATEBRUSHINDIRECT():
    EMRCREATEBRUSHINDIRECT = win32more.Graphics.Gdi.EMRCREATEBRUSHINDIRECT_head
    EMRCREATEBRUSHINDIRECT._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('ihBrush', UInt32),
        ('lb', win32more.Graphics.Gdi.LOGBRUSH32),
    ]
    return EMRCREATEBRUSHINDIRECT
def _define_EMRCREATEDIBPATTERNBRUSHPT_head():
    class EMRCREATEDIBPATTERNBRUSHPT(Structure):
        pass
    return EMRCREATEDIBPATTERNBRUSHPT
def _define_EMRCREATEDIBPATTERNBRUSHPT():
    EMRCREATEDIBPATTERNBRUSHPT = win32more.Graphics.Gdi.EMRCREATEDIBPATTERNBRUSHPT_head
    EMRCREATEDIBPATTERNBRUSHPT._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('ihBrush', UInt32),
        ('iUsage', UInt32),
        ('offBmi', UInt32),
        ('cbBmi', UInt32),
        ('offBits', UInt32),
        ('cbBits', UInt32),
    ]
    return EMRCREATEDIBPATTERNBRUSHPT
def _define_EMRCREATEMONOBRUSH_head():
    class EMRCREATEMONOBRUSH(Structure):
        pass
    return EMRCREATEMONOBRUSH
def _define_EMRCREATEMONOBRUSH():
    EMRCREATEMONOBRUSH = win32more.Graphics.Gdi.EMRCREATEMONOBRUSH_head
    EMRCREATEMONOBRUSH._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('ihBrush', UInt32),
        ('iUsage', UInt32),
        ('offBmi', UInt32),
        ('cbBmi', UInt32),
        ('offBits', UInt32),
        ('cbBits', UInt32),
    ]
    return EMRCREATEMONOBRUSH
def _define_EMRCREATEPALETTE_head():
    class EMRCREATEPALETTE(Structure):
        pass
    return EMRCREATEPALETTE
def _define_EMRCREATEPALETTE():
    EMRCREATEPALETTE = win32more.Graphics.Gdi.EMRCREATEPALETTE_head
    EMRCREATEPALETTE._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('ihPal', UInt32),
        ('lgpl', win32more.Graphics.Gdi.LOGPALETTE),
    ]
    return EMRCREATEPALETTE
def _define_EMRCREATEPEN_head():
    class EMRCREATEPEN(Structure):
        pass
    return EMRCREATEPEN
def _define_EMRCREATEPEN():
    EMRCREATEPEN = win32more.Graphics.Gdi.EMRCREATEPEN_head
    EMRCREATEPEN._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('ihPen', UInt32),
        ('lopn', win32more.Graphics.Gdi.LOGPEN),
    ]
    return EMRCREATEPEN
def _define_EMRELLIPSE_head():
    class EMRELLIPSE(Structure):
        pass
    return EMRELLIPSE
def _define_EMRELLIPSE():
    EMRELLIPSE = win32more.Graphics.Gdi.EMRELLIPSE_head
    EMRELLIPSE._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('rclBox', win32more.Foundation.RECTL),
    ]
    return EMRELLIPSE
def _define_EMREOF_head():
    class EMREOF(Structure):
        pass
    return EMREOF
def _define_EMREOF():
    EMREOF = win32more.Graphics.Gdi.EMREOF_head
    EMREOF._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('nPalEntries', UInt32),
        ('offPalEntries', UInt32),
        ('nSizeLast', UInt32),
    ]
    return EMREOF
def _define_EMREXCLUDECLIPRECT_head():
    class EMREXCLUDECLIPRECT(Structure):
        pass
    return EMREXCLUDECLIPRECT
def _define_EMREXCLUDECLIPRECT():
    EMREXCLUDECLIPRECT = win32more.Graphics.Gdi.EMREXCLUDECLIPRECT_head
    EMREXCLUDECLIPRECT._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('rclClip', win32more.Foundation.RECTL),
    ]
    return EMREXCLUDECLIPRECT
def _define_EMREXTCREATEFONTINDIRECTW_head():
    class EMREXTCREATEFONTINDIRECTW(Structure):
        pass
    return EMREXTCREATEFONTINDIRECTW
def _define_EMREXTCREATEFONTINDIRECTW():
    EMREXTCREATEFONTINDIRECTW = win32more.Graphics.Gdi.EMREXTCREATEFONTINDIRECTW_head
    EMREXTCREATEFONTINDIRECTW._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('ihFont', UInt32),
        ('elfw', win32more.Graphics.Gdi.EXTLOGFONTW),
    ]
    return EMREXTCREATEFONTINDIRECTW
def _define_EMREXTCREATEPEN_head():
    class EMREXTCREATEPEN(Structure):
        pass
    return EMREXTCREATEPEN
def _define_EMREXTCREATEPEN():
    EMREXTCREATEPEN = win32more.Graphics.Gdi.EMREXTCREATEPEN_head
    EMREXTCREATEPEN._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('ihPen', UInt32),
        ('offBmi', UInt32),
        ('cbBmi', UInt32),
        ('offBits', UInt32),
        ('cbBits', UInt32),
        ('elp', win32more.Graphics.Gdi.EXTLOGPEN32),
    ]
    return EMREXTCREATEPEN
def _define_EMREXTESCAPE_head():
    class EMREXTESCAPE(Structure):
        pass
    return EMREXTESCAPE
def _define_EMREXTESCAPE():
    EMREXTESCAPE = win32more.Graphics.Gdi.EMREXTESCAPE_head
    EMREXTESCAPE._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('iEscape', Int32),
        ('cbEscData', Int32),
        ('EscData', Byte * 1),
    ]
    return EMREXTESCAPE
def _define_EMREXTFLOODFILL_head():
    class EMREXTFLOODFILL(Structure):
        pass
    return EMREXTFLOODFILL
def _define_EMREXTFLOODFILL():
    EMREXTFLOODFILL = win32more.Graphics.Gdi.EMREXTFLOODFILL_head
    EMREXTFLOODFILL._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('ptlStart', win32more.Foundation.POINTL),
        ('crColor', win32more.Foundation.COLORREF),
        ('iMode', UInt32),
    ]
    return EMREXTFLOODFILL
def _define_EMREXTSELECTCLIPRGN_head():
    class EMREXTSELECTCLIPRGN(Structure):
        pass
    return EMREXTSELECTCLIPRGN
def _define_EMREXTSELECTCLIPRGN():
    EMREXTSELECTCLIPRGN = win32more.Graphics.Gdi.EMREXTSELECTCLIPRGN_head
    EMREXTSELECTCLIPRGN._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('cbRgnData', UInt32),
        ('iMode', win32more.Graphics.Gdi.RGN_COMBINE_MODE),
        ('RgnData', Byte * 1),
    ]
    return EMREXTSELECTCLIPRGN
def _define_EMREXTTEXTOUTA_head():
    class EMREXTTEXTOUTA(Structure):
        pass
    return EMREXTTEXTOUTA
def _define_EMREXTTEXTOUTA():
    EMREXTTEXTOUTA = win32more.Graphics.Gdi.EMREXTTEXTOUTA_head
    EMREXTTEXTOUTA._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('rclBounds', win32more.Foundation.RECTL),
        ('iGraphicsMode', UInt32),
        ('exScale', Single),
        ('eyScale', Single),
        ('emrtext', win32more.Graphics.Gdi.EMRTEXT),
    ]
    return EMREXTTEXTOUTA
def _define_EMRFILLPATH_head():
    class EMRFILLPATH(Structure):
        pass
    return EMRFILLPATH
def _define_EMRFILLPATH():
    EMRFILLPATH = win32more.Graphics.Gdi.EMRFILLPATH_head
    EMRFILLPATH._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('rclBounds', win32more.Foundation.RECTL),
    ]
    return EMRFILLPATH
def _define_EMRFILLRGN_head():
    class EMRFILLRGN(Structure):
        pass
    return EMRFILLRGN
def _define_EMRFILLRGN():
    EMRFILLRGN = win32more.Graphics.Gdi.EMRFILLRGN_head
    EMRFILLRGN._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('rclBounds', win32more.Foundation.RECTL),
        ('cbRgnData', UInt32),
        ('ihBrush', UInt32),
        ('RgnData', Byte * 1),
    ]
    return EMRFILLRGN
def _define_EMRFORMAT_head():
    class EMRFORMAT(Structure):
        pass
    return EMRFORMAT
def _define_EMRFORMAT():
    EMRFORMAT = win32more.Graphics.Gdi.EMRFORMAT_head
    EMRFORMAT._fields_ = [
        ('dSignature', UInt32),
        ('nVersion', UInt32),
        ('cbData', UInt32),
        ('offData', UInt32),
    ]
    return EMRFORMAT
def _define_EMRFRAMERGN_head():
    class EMRFRAMERGN(Structure):
        pass
    return EMRFRAMERGN
def _define_EMRFRAMERGN():
    EMRFRAMERGN = win32more.Graphics.Gdi.EMRFRAMERGN_head
    EMRFRAMERGN._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('rclBounds', win32more.Foundation.RECTL),
        ('cbRgnData', UInt32),
        ('ihBrush', UInt32),
        ('szlStroke', win32more.Foundation.SIZE),
        ('RgnData', Byte * 1),
    ]
    return EMRFRAMERGN
def _define_EMRGDICOMMENT_head():
    class EMRGDICOMMENT(Structure):
        pass
    return EMRGDICOMMENT
def _define_EMRGDICOMMENT():
    EMRGDICOMMENT = win32more.Graphics.Gdi.EMRGDICOMMENT_head
    EMRGDICOMMENT._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('cbData', UInt32),
        ('Data', Byte * 1),
    ]
    return EMRGDICOMMENT
def _define_EMRGLSBOUNDEDRECORD_head():
    class EMRGLSBOUNDEDRECORD(Structure):
        pass
    return EMRGLSBOUNDEDRECORD
def _define_EMRGLSBOUNDEDRECORD():
    EMRGLSBOUNDEDRECORD = win32more.Graphics.Gdi.EMRGLSBOUNDEDRECORD_head
    EMRGLSBOUNDEDRECORD._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('rclBounds', win32more.Foundation.RECTL),
        ('cbData', UInt32),
        ('Data', Byte * 1),
    ]
    return EMRGLSBOUNDEDRECORD
def _define_EMRGLSRECORD_head():
    class EMRGLSRECORD(Structure):
        pass
    return EMRGLSRECORD
def _define_EMRGLSRECORD():
    EMRGLSRECORD = win32more.Graphics.Gdi.EMRGLSRECORD_head
    EMRGLSRECORD._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('cbData', UInt32),
        ('Data', Byte * 1),
    ]
    return EMRGLSRECORD
def _define_EMRGRADIENTFILL_head():
    class EMRGRADIENTFILL(Structure):
        pass
    return EMRGRADIENTFILL
def _define_EMRGRADIENTFILL():
    EMRGRADIENTFILL = win32more.Graphics.Gdi.EMRGRADIENTFILL_head
    EMRGRADIENTFILL._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('rclBounds', win32more.Foundation.RECTL),
        ('nVer', UInt32),
        ('nTri', UInt32),
        ('ulMode', win32more.Graphics.Gdi.GRADIENT_FILL),
        ('Ver', win32more.Graphics.Gdi.TRIVERTEX * 1),
    ]
    return EMRGRADIENTFILL
def _define_EMRINVERTRGN_head():
    class EMRINVERTRGN(Structure):
        pass
    return EMRINVERTRGN
def _define_EMRINVERTRGN():
    EMRINVERTRGN = win32more.Graphics.Gdi.EMRINVERTRGN_head
    EMRINVERTRGN._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('rclBounds', win32more.Foundation.RECTL),
        ('cbRgnData', UInt32),
        ('RgnData', Byte * 1),
    ]
    return EMRINVERTRGN
def _define_EMRLINETO_head():
    class EMRLINETO(Structure):
        pass
    return EMRLINETO
def _define_EMRLINETO():
    EMRLINETO = win32more.Graphics.Gdi.EMRLINETO_head
    EMRLINETO._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('ptl', win32more.Foundation.POINTL),
    ]
    return EMRLINETO
def _define_EMRMASKBLT_head():
    class EMRMASKBLT(Structure):
        pass
    return EMRMASKBLT
def _define_EMRMASKBLT():
    EMRMASKBLT = win32more.Graphics.Gdi.EMRMASKBLT_head
    EMRMASKBLT._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('rclBounds', win32more.Foundation.RECTL),
        ('xDest', Int32),
        ('yDest', Int32),
        ('cxDest', Int32),
        ('cyDest', Int32),
        ('dwRop', UInt32),
        ('xSrc', Int32),
        ('ySrc', Int32),
        ('xformSrc', win32more.Graphics.Gdi.XFORM),
        ('crBkColorSrc', win32more.Foundation.COLORREF),
        ('iUsageSrc', UInt32),
        ('offBmiSrc', UInt32),
        ('cbBmiSrc', UInt32),
        ('offBitsSrc', UInt32),
        ('cbBitsSrc', UInt32),
        ('xMask', Int32),
        ('yMask', Int32),
        ('iUsageMask', UInt32),
        ('offBmiMask', UInt32),
        ('cbBmiMask', UInt32),
        ('offBitsMask', UInt32),
        ('cbBitsMask', UInt32),
    ]
    return EMRMASKBLT
def _define_EMRMODIFYWORLDTRANSFORM_head():
    class EMRMODIFYWORLDTRANSFORM(Structure):
        pass
    return EMRMODIFYWORLDTRANSFORM
def _define_EMRMODIFYWORLDTRANSFORM():
    EMRMODIFYWORLDTRANSFORM = win32more.Graphics.Gdi.EMRMODIFYWORLDTRANSFORM_head
    EMRMODIFYWORLDTRANSFORM._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('xform', win32more.Graphics.Gdi.XFORM),
        ('iMode', win32more.Graphics.Gdi.MODIFY_WORLD_TRANSFORM_MODE),
    ]
    return EMRMODIFYWORLDTRANSFORM
def _define_EMRNAMEDESCAPE_head():
    class EMRNAMEDESCAPE(Structure):
        pass
    return EMRNAMEDESCAPE
def _define_EMRNAMEDESCAPE():
    EMRNAMEDESCAPE = win32more.Graphics.Gdi.EMRNAMEDESCAPE_head
    EMRNAMEDESCAPE._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('iEscape', Int32),
        ('cbDriver', Int32),
        ('cbEscData', Int32),
        ('EscData', Byte * 1),
    ]
    return EMRNAMEDESCAPE
def _define_EMROFFSETCLIPRGN_head():
    class EMROFFSETCLIPRGN(Structure):
        pass
    return EMROFFSETCLIPRGN
def _define_EMROFFSETCLIPRGN():
    EMROFFSETCLIPRGN = win32more.Graphics.Gdi.EMROFFSETCLIPRGN_head
    EMROFFSETCLIPRGN._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('ptlOffset', win32more.Foundation.POINTL),
    ]
    return EMROFFSETCLIPRGN
def _define_EMRPLGBLT_head():
    class EMRPLGBLT(Structure):
        pass
    return EMRPLGBLT
def _define_EMRPLGBLT():
    EMRPLGBLT = win32more.Graphics.Gdi.EMRPLGBLT_head
    EMRPLGBLT._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('rclBounds', win32more.Foundation.RECTL),
        ('aptlDest', win32more.Foundation.POINTL * 3),
        ('xSrc', Int32),
        ('ySrc', Int32),
        ('cxSrc', Int32),
        ('cySrc', Int32),
        ('xformSrc', win32more.Graphics.Gdi.XFORM),
        ('crBkColorSrc', win32more.Foundation.COLORREF),
        ('iUsageSrc', UInt32),
        ('offBmiSrc', UInt32),
        ('cbBmiSrc', UInt32),
        ('offBitsSrc', UInt32),
        ('cbBitsSrc', UInt32),
        ('xMask', Int32),
        ('yMask', Int32),
        ('iUsageMask', UInt32),
        ('offBmiMask', UInt32),
        ('cbBmiMask', UInt32),
        ('offBitsMask', UInt32),
        ('cbBitsMask', UInt32),
    ]
    return EMRPLGBLT
def _define_EMRPOLYDRAW_head():
    class EMRPOLYDRAW(Structure):
        pass
    return EMRPOLYDRAW
def _define_EMRPOLYDRAW():
    EMRPOLYDRAW = win32more.Graphics.Gdi.EMRPOLYDRAW_head
    EMRPOLYDRAW._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('rclBounds', win32more.Foundation.RECTL),
        ('cptl', UInt32),
        ('aptl', win32more.Foundation.POINTL * 1),
        ('abTypes', Byte * 1),
    ]
    return EMRPOLYDRAW
def _define_EMRPOLYDRAW16_head():
    class EMRPOLYDRAW16(Structure):
        pass
    return EMRPOLYDRAW16
def _define_EMRPOLYDRAW16():
    EMRPOLYDRAW16 = win32more.Graphics.Gdi.EMRPOLYDRAW16_head
    EMRPOLYDRAW16._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('rclBounds', win32more.Foundation.RECTL),
        ('cpts', UInt32),
        ('apts', win32more.Foundation.POINTS * 1),
        ('abTypes', Byte * 1),
    ]
    return EMRPOLYDRAW16
def _define_EMRPOLYLINE_head():
    class EMRPOLYLINE(Structure):
        pass
    return EMRPOLYLINE
def _define_EMRPOLYLINE():
    EMRPOLYLINE = win32more.Graphics.Gdi.EMRPOLYLINE_head
    EMRPOLYLINE._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('rclBounds', win32more.Foundation.RECTL),
        ('cptl', UInt32),
        ('aptl', win32more.Foundation.POINTL * 1),
    ]
    return EMRPOLYLINE
def _define_EMRPOLYLINE16_head():
    class EMRPOLYLINE16(Structure):
        pass
    return EMRPOLYLINE16
def _define_EMRPOLYLINE16():
    EMRPOLYLINE16 = win32more.Graphics.Gdi.EMRPOLYLINE16_head
    EMRPOLYLINE16._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('rclBounds', win32more.Foundation.RECTL),
        ('cpts', UInt32),
        ('apts', win32more.Foundation.POINTS * 1),
    ]
    return EMRPOLYLINE16
def _define_EMRPOLYPOLYLINE_head():
    class EMRPOLYPOLYLINE(Structure):
        pass
    return EMRPOLYPOLYLINE
def _define_EMRPOLYPOLYLINE():
    EMRPOLYPOLYLINE = win32more.Graphics.Gdi.EMRPOLYPOLYLINE_head
    EMRPOLYPOLYLINE._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('rclBounds', win32more.Foundation.RECTL),
        ('nPolys', UInt32),
        ('cptl', UInt32),
        ('aPolyCounts', UInt32 * 1),
        ('aptl', win32more.Foundation.POINTL * 1),
    ]
    return EMRPOLYPOLYLINE
def _define_EMRPOLYPOLYLINE16_head():
    class EMRPOLYPOLYLINE16(Structure):
        pass
    return EMRPOLYPOLYLINE16
def _define_EMRPOLYPOLYLINE16():
    EMRPOLYPOLYLINE16 = win32more.Graphics.Gdi.EMRPOLYPOLYLINE16_head
    EMRPOLYPOLYLINE16._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('rclBounds', win32more.Foundation.RECTL),
        ('nPolys', UInt32),
        ('cpts', UInt32),
        ('aPolyCounts', UInt32 * 1),
        ('apts', win32more.Foundation.POINTS * 1),
    ]
    return EMRPOLYPOLYLINE16
def _define_EMRPOLYTEXTOUTA_head():
    class EMRPOLYTEXTOUTA(Structure):
        pass
    return EMRPOLYTEXTOUTA
def _define_EMRPOLYTEXTOUTA():
    EMRPOLYTEXTOUTA = win32more.Graphics.Gdi.EMRPOLYTEXTOUTA_head
    EMRPOLYTEXTOUTA._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('rclBounds', win32more.Foundation.RECTL),
        ('iGraphicsMode', UInt32),
        ('exScale', Single),
        ('eyScale', Single),
        ('cStrings', Int32),
        ('aemrtext', win32more.Graphics.Gdi.EMRTEXT * 1),
    ]
    return EMRPOLYTEXTOUTA
def _define_EMRRESIZEPALETTE_head():
    class EMRRESIZEPALETTE(Structure):
        pass
    return EMRRESIZEPALETTE
def _define_EMRRESIZEPALETTE():
    EMRRESIZEPALETTE = win32more.Graphics.Gdi.EMRRESIZEPALETTE_head
    EMRRESIZEPALETTE._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('ihPal', UInt32),
        ('cEntries', UInt32),
    ]
    return EMRRESIZEPALETTE
def _define_EMRRESTOREDC_head():
    class EMRRESTOREDC(Structure):
        pass
    return EMRRESTOREDC
def _define_EMRRESTOREDC():
    EMRRESTOREDC = win32more.Graphics.Gdi.EMRRESTOREDC_head
    EMRRESTOREDC._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('iRelative', Int32),
    ]
    return EMRRESTOREDC
def _define_EMRROUNDRECT_head():
    class EMRROUNDRECT(Structure):
        pass
    return EMRROUNDRECT
def _define_EMRROUNDRECT():
    EMRROUNDRECT = win32more.Graphics.Gdi.EMRROUNDRECT_head
    EMRROUNDRECT._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('rclBox', win32more.Foundation.RECTL),
        ('szlCorner', win32more.Foundation.SIZE),
    ]
    return EMRROUNDRECT
def _define_EMRSCALEVIEWPORTEXTEX_head():
    class EMRSCALEVIEWPORTEXTEX(Structure):
        pass
    return EMRSCALEVIEWPORTEXTEX
def _define_EMRSCALEVIEWPORTEXTEX():
    EMRSCALEVIEWPORTEXTEX = win32more.Graphics.Gdi.EMRSCALEVIEWPORTEXTEX_head
    EMRSCALEVIEWPORTEXTEX._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('xNum', Int32),
        ('xDenom', Int32),
        ('yNum', Int32),
        ('yDenom', Int32),
    ]
    return EMRSCALEVIEWPORTEXTEX
def _define_EMRSELECTCLIPPATH_head():
    class EMRSELECTCLIPPATH(Structure):
        pass
    return EMRSELECTCLIPPATH
def _define_EMRSELECTCLIPPATH():
    EMRSELECTCLIPPATH = win32more.Graphics.Gdi.EMRSELECTCLIPPATH_head
    EMRSELECTCLIPPATH._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('iMode', UInt32),
    ]
    return EMRSELECTCLIPPATH
def _define_EMRSELECTOBJECT_head():
    class EMRSELECTOBJECT(Structure):
        pass
    return EMRSELECTOBJECT
def _define_EMRSELECTOBJECT():
    EMRSELECTOBJECT = win32more.Graphics.Gdi.EMRSELECTOBJECT_head
    EMRSELECTOBJECT._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('ihObject', UInt32),
    ]
    return EMRSELECTOBJECT
def _define_EMRSELECTPALETTE_head():
    class EMRSELECTPALETTE(Structure):
        pass
    return EMRSELECTPALETTE
def _define_EMRSELECTPALETTE():
    EMRSELECTPALETTE = win32more.Graphics.Gdi.EMRSELECTPALETTE_head
    EMRSELECTPALETTE._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('ihPal', UInt32),
    ]
    return EMRSELECTPALETTE
def _define_EMRSETARCDIRECTION_head():
    class EMRSETARCDIRECTION(Structure):
        pass
    return EMRSETARCDIRECTION
def _define_EMRSETARCDIRECTION():
    EMRSETARCDIRECTION = win32more.Graphics.Gdi.EMRSETARCDIRECTION_head
    EMRSETARCDIRECTION._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('iArcDirection', UInt32),
    ]
    return EMRSETARCDIRECTION
def _define_EMRSETCOLORADJUSTMENT_head():
    class EMRSETCOLORADJUSTMENT(Structure):
        pass
    return EMRSETCOLORADJUSTMENT
def _define_EMRSETCOLORADJUSTMENT():
    EMRSETCOLORADJUSTMENT = win32more.Graphics.Gdi.EMRSETCOLORADJUSTMENT_head
    EMRSETCOLORADJUSTMENT._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('ColorAdjustment', win32more.Graphics.Gdi.COLORADJUSTMENT),
    ]
    return EMRSETCOLORADJUSTMENT
def _define_EMRSETCOLORSPACE_head():
    class EMRSETCOLORSPACE(Structure):
        pass
    return EMRSETCOLORSPACE
def _define_EMRSETCOLORSPACE():
    EMRSETCOLORSPACE = win32more.Graphics.Gdi.EMRSETCOLORSPACE_head
    EMRSETCOLORSPACE._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('ihCS', UInt32),
    ]
    return EMRSETCOLORSPACE
def _define_EMRSETDIBITSTODEVICE_head():
    class EMRSETDIBITSTODEVICE(Structure):
        pass
    return EMRSETDIBITSTODEVICE
def _define_EMRSETDIBITSTODEVICE():
    EMRSETDIBITSTODEVICE = win32more.Graphics.Gdi.EMRSETDIBITSTODEVICE_head
    EMRSETDIBITSTODEVICE._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('rclBounds', win32more.Foundation.RECTL),
        ('xDest', Int32),
        ('yDest', Int32),
        ('xSrc', Int32),
        ('ySrc', Int32),
        ('cxSrc', Int32),
        ('cySrc', Int32),
        ('offBmiSrc', UInt32),
        ('cbBmiSrc', UInt32),
        ('offBitsSrc', UInt32),
        ('cbBitsSrc', UInt32),
        ('iUsageSrc', UInt32),
        ('iStartScan', UInt32),
        ('cScans', UInt32),
    ]
    return EMRSETDIBITSTODEVICE
def _define_EMRSETICMPROFILE_head():
    class EMRSETICMPROFILE(Structure):
        pass
    return EMRSETICMPROFILE
def _define_EMRSETICMPROFILE():
    EMRSETICMPROFILE = win32more.Graphics.Gdi.EMRSETICMPROFILE_head
    EMRSETICMPROFILE._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('dwFlags', UInt32),
        ('cbName', UInt32),
        ('cbData', UInt32),
        ('Data', Byte * 1),
    ]
    return EMRSETICMPROFILE
def _define_EMRSETMAPPERFLAGS_head():
    class EMRSETMAPPERFLAGS(Structure):
        pass
    return EMRSETMAPPERFLAGS
def _define_EMRSETMAPPERFLAGS():
    EMRSETMAPPERFLAGS = win32more.Graphics.Gdi.EMRSETMAPPERFLAGS_head
    EMRSETMAPPERFLAGS._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('dwFlags', UInt32),
    ]
    return EMRSETMAPPERFLAGS
def _define_EMRSETMITERLIMIT_head():
    class EMRSETMITERLIMIT(Structure):
        pass
    return EMRSETMITERLIMIT
def _define_EMRSETMITERLIMIT():
    EMRSETMITERLIMIT = win32more.Graphics.Gdi.EMRSETMITERLIMIT_head
    EMRSETMITERLIMIT._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('eMiterLimit', Single),
    ]
    return EMRSETMITERLIMIT
def _define_EMRSETPALETTEENTRIES_head():
    class EMRSETPALETTEENTRIES(Structure):
        pass
    return EMRSETPALETTEENTRIES
def _define_EMRSETPALETTEENTRIES():
    EMRSETPALETTEENTRIES = win32more.Graphics.Gdi.EMRSETPALETTEENTRIES_head
    EMRSETPALETTEENTRIES._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('ihPal', UInt32),
        ('iStart', UInt32),
        ('cEntries', UInt32),
        ('aPalEntries', win32more.Graphics.Gdi.PALETTEENTRY * 1),
    ]
    return EMRSETPALETTEENTRIES
def _define_EMRSETPIXELV_head():
    class EMRSETPIXELV(Structure):
        pass
    return EMRSETPIXELV
def _define_EMRSETPIXELV():
    EMRSETPIXELV = win32more.Graphics.Gdi.EMRSETPIXELV_head
    EMRSETPIXELV._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('ptlPixel', win32more.Foundation.POINTL),
        ('crColor', win32more.Foundation.COLORREF),
    ]
    return EMRSETPIXELV
def _define_EMRSETTEXTCOLOR_head():
    class EMRSETTEXTCOLOR(Structure):
        pass
    return EMRSETTEXTCOLOR
def _define_EMRSETTEXTCOLOR():
    EMRSETTEXTCOLOR = win32more.Graphics.Gdi.EMRSETTEXTCOLOR_head
    EMRSETTEXTCOLOR._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('crColor', win32more.Foundation.COLORREF),
    ]
    return EMRSETTEXTCOLOR
def _define_EMRSETVIEWPORTEXTEX_head():
    class EMRSETVIEWPORTEXTEX(Structure):
        pass
    return EMRSETVIEWPORTEXTEX
def _define_EMRSETVIEWPORTEXTEX():
    EMRSETVIEWPORTEXTEX = win32more.Graphics.Gdi.EMRSETVIEWPORTEXTEX_head
    EMRSETVIEWPORTEXTEX._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('szlExtent', win32more.Foundation.SIZE),
    ]
    return EMRSETVIEWPORTEXTEX
def _define_EMRSETVIEWPORTORGEX_head():
    class EMRSETVIEWPORTORGEX(Structure):
        pass
    return EMRSETVIEWPORTORGEX
def _define_EMRSETVIEWPORTORGEX():
    EMRSETVIEWPORTORGEX = win32more.Graphics.Gdi.EMRSETVIEWPORTORGEX_head
    EMRSETVIEWPORTORGEX._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('ptlOrigin', win32more.Foundation.POINTL),
    ]
    return EMRSETVIEWPORTORGEX
def _define_EMRSETWORLDTRANSFORM_head():
    class EMRSETWORLDTRANSFORM(Structure):
        pass
    return EMRSETWORLDTRANSFORM
def _define_EMRSETWORLDTRANSFORM():
    EMRSETWORLDTRANSFORM = win32more.Graphics.Gdi.EMRSETWORLDTRANSFORM_head
    EMRSETWORLDTRANSFORM._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('xform', win32more.Graphics.Gdi.XFORM),
    ]
    return EMRSETWORLDTRANSFORM
def _define_EMRSTRETCHBLT_head():
    class EMRSTRETCHBLT(Structure):
        pass
    return EMRSTRETCHBLT
def _define_EMRSTRETCHBLT():
    EMRSTRETCHBLT = win32more.Graphics.Gdi.EMRSTRETCHBLT_head
    EMRSTRETCHBLT._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('rclBounds', win32more.Foundation.RECTL),
        ('xDest', Int32),
        ('yDest', Int32),
        ('cxDest', Int32),
        ('cyDest', Int32),
        ('dwRop', UInt32),
        ('xSrc', Int32),
        ('ySrc', Int32),
        ('xformSrc', win32more.Graphics.Gdi.XFORM),
        ('crBkColorSrc', win32more.Foundation.COLORREF),
        ('iUsageSrc', UInt32),
        ('offBmiSrc', UInt32),
        ('cbBmiSrc', UInt32),
        ('offBitsSrc', UInt32),
        ('cbBitsSrc', UInt32),
        ('cxSrc', Int32),
        ('cySrc', Int32),
    ]
    return EMRSTRETCHBLT
def _define_EMRSTRETCHDIBITS_head():
    class EMRSTRETCHDIBITS(Structure):
        pass
    return EMRSTRETCHDIBITS
def _define_EMRSTRETCHDIBITS():
    EMRSTRETCHDIBITS = win32more.Graphics.Gdi.EMRSTRETCHDIBITS_head
    EMRSTRETCHDIBITS._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('rclBounds', win32more.Foundation.RECTL),
        ('xDest', Int32),
        ('yDest', Int32),
        ('xSrc', Int32),
        ('ySrc', Int32),
        ('cxSrc', Int32),
        ('cySrc', Int32),
        ('offBmiSrc', UInt32),
        ('cbBmiSrc', UInt32),
        ('offBitsSrc', UInt32),
        ('cbBitsSrc', UInt32),
        ('iUsageSrc', UInt32),
        ('dwRop', UInt32),
        ('cxDest', Int32),
        ('cyDest', Int32),
    ]
    return EMRSTRETCHDIBITS
def _define_EMRTEXT_head():
    class EMRTEXT(Structure):
        pass
    return EMRTEXT
def _define_EMRTEXT():
    EMRTEXT = win32more.Graphics.Gdi.EMRTEXT_head
    EMRTEXT._fields_ = [
        ('ptlReference', win32more.Foundation.POINTL),
        ('nChars', UInt32),
        ('offString', UInt32),
        ('fOptions', UInt32),
        ('rcl', win32more.Foundation.RECTL),
        ('offDx', UInt32),
    ]
    return EMRTEXT
def _define_EMRTRANSPARENTBLT_head():
    class EMRTRANSPARENTBLT(Structure):
        pass
    return EMRTRANSPARENTBLT
def _define_EMRTRANSPARENTBLT():
    EMRTRANSPARENTBLT = win32more.Graphics.Gdi.EMRTRANSPARENTBLT_head
    EMRTRANSPARENTBLT._fields_ = [
        ('emr', win32more.Graphics.Gdi.EMR),
        ('rclBounds', win32more.Foundation.RECTL),
        ('xDest', Int32),
        ('yDest', Int32),
        ('cxDest', Int32),
        ('cyDest', Int32),
        ('dwRop', UInt32),
        ('xSrc', Int32),
        ('ySrc', Int32),
        ('xformSrc', win32more.Graphics.Gdi.XFORM),
        ('crBkColorSrc', win32more.Foundation.COLORREF),
        ('iUsageSrc', UInt32),
        ('offBmiSrc', UInt32),
        ('cbBmiSrc', UInt32),
        ('offBitsSrc', UInt32),
        ('cbBitsSrc', UInt32),
        ('cxSrc', Int32),
        ('cySrc', Int32),
    ]
    return EMRTRANSPARENTBLT
ENHANCED_METAFILE_RECORD_TYPE = UInt32
EMR_HEADER = 1
EMR_POLYBEZIER = 2
EMR_POLYGON = 3
EMR_POLYLINE = 4
EMR_POLYBEZIERTO = 5
EMR_POLYLINETO = 6
EMR_POLYPOLYLINE = 7
EMR_POLYPOLYGON = 8
EMR_SETWINDOWEXTEX = 9
EMR_SETWINDOWORGEX = 10
EMR_SETVIEWPORTEXTEX = 11
EMR_SETVIEWPORTORGEX = 12
EMR_SETBRUSHORGEX = 13
EMR_EOF = 14
EMR_SETPIXELV = 15
EMR_SETMAPPERFLAGS = 16
EMR_SETMAPMODE = 17
EMR_SETBKMODE = 18
EMR_SETPOLYFILLMODE = 19
EMR_SETROP2 = 20
EMR_SETSTRETCHBLTMODE = 21
EMR_SETTEXTALIGN = 22
EMR_SETCOLORADJUSTMENT = 23
EMR_SETTEXTCOLOR = 24
EMR_SETBKCOLOR = 25
EMR_OFFSETCLIPRGN = 26
EMR_MOVETOEX = 27
EMR_SETMETARGN = 28
EMR_EXCLUDECLIPRECT = 29
EMR_INTERSECTCLIPRECT = 30
EMR_SCALEVIEWPORTEXTEX = 31
EMR_SCALEWINDOWEXTEX = 32
EMR_SAVEDC = 33
EMR_RESTOREDC = 34
EMR_SETWORLDTRANSFORM = 35
EMR_MODIFYWORLDTRANSFORM = 36
EMR_SELECTOBJECT = 37
EMR_CREATEPEN = 38
EMR_CREATEBRUSHINDIRECT = 39
EMR_DELETEOBJECT = 40
EMR_ANGLEARC = 41
EMR_ELLIPSE = 42
EMR_RECTANGLE = 43
EMR_ROUNDRECT = 44
EMR_ARC = 45
EMR_CHORD = 46
EMR_PIE = 47
EMR_SELECTPALETTE = 48
EMR_CREATEPALETTE = 49
EMR_SETPALETTEENTRIES = 50
EMR_RESIZEPALETTE = 51
EMR_REALIZEPALETTE = 52
EMR_EXTFLOODFILL = 53
EMR_LINETO = 54
EMR_ARCTO = 55
EMR_POLYDRAW = 56
EMR_SETARCDIRECTION = 57
EMR_SETMITERLIMIT = 58
EMR_BEGINPATH = 59
EMR_ENDPATH = 60
EMR_CLOSEFIGURE = 61
EMR_FILLPATH = 62
EMR_STROKEANDFILLPATH = 63
EMR_STROKEPATH = 64
EMR_FLATTENPATH = 65
EMR_WIDENPATH = 66
EMR_SELECTCLIPPATH = 67
EMR_ABORTPATH = 68
EMR_GDICOMMENT = 70
EMR_FILLRGN = 71
EMR_FRAMERGN = 72
EMR_INVERTRGN = 73
EMR_PAINTRGN = 74
EMR_EXTSELECTCLIPRGN = 75
EMR_BITBLT = 76
EMR_STRETCHBLT = 77
EMR_MASKBLT = 78
EMR_PLGBLT = 79
EMR_SETDIBITSTODEVICE = 80
EMR_STRETCHDIBITS = 81
EMR_EXTCREATEFONTINDIRECTW = 82
EMR_EXTTEXTOUTA = 83
EMR_EXTTEXTOUTW = 84
EMR_POLYBEZIER16 = 85
EMR_POLYGON16 = 86
EMR_POLYLINE16 = 87
EMR_POLYBEZIERTO16 = 88
EMR_POLYLINETO16 = 89
EMR_POLYPOLYLINE16 = 90
EMR_POLYPOLYGON16 = 91
EMR_POLYDRAW16 = 92
EMR_CREATEMONOBRUSH = 93
EMR_CREATEDIBPATTERNBRUSHPT = 94
EMR_EXTCREATEPEN = 95
EMR_POLYTEXTOUTA = 96
EMR_POLYTEXTOUTW = 97
EMR_SETICMMODE = 98
EMR_CREATECOLORSPACE = 99
EMR_SETCOLORSPACE = 100
EMR_DELETECOLORSPACE = 101
EMR_GLSRECORD = 102
EMR_GLSBOUNDEDRECORD = 103
EMR_PIXELFORMAT = 104
EMR_RESERVED_105 = 105
EMR_RESERVED_106 = 106
EMR_RESERVED_107 = 107
EMR_RESERVED_108 = 108
EMR_RESERVED_109 = 109
EMR_RESERVED_110 = 110
EMR_COLORCORRECTPALETTE = 111
EMR_SETICMPROFILEA = 112
EMR_SETICMPROFILEW = 113
EMR_ALPHABLEND = 114
EMR_SETLAYOUT = 115
EMR_TRANSPARENTBLT = 116
EMR_RESERVED_117 = 117
EMR_GRADIENTFILL = 118
EMR_RESERVED_119 = 119
EMR_RESERVED_120 = 120
EMR_COLORMATCHTOTARGETW = 121
EMR_CREATECOLORSPACEW = 122
EMR_MIN = 1
EMR_MAX = 122
def _define_ENHMETAHEADER_head():
    class ENHMETAHEADER(Structure):
        pass
    return ENHMETAHEADER
def _define_ENHMETAHEADER():
    ENHMETAHEADER = win32more.Graphics.Gdi.ENHMETAHEADER_head
    ENHMETAHEADER._fields_ = [
        ('iType', UInt32),
        ('nSize', UInt32),
        ('rclBounds', win32more.Foundation.RECTL),
        ('rclFrame', win32more.Foundation.RECTL),
        ('dSignature', UInt32),
        ('nVersion', UInt32),
        ('nBytes', UInt32),
        ('nRecords', UInt32),
        ('nHandles', UInt16),
        ('sReserved', UInt16),
        ('nDescription', UInt32),
        ('offDescription', UInt32),
        ('nPalEntries', UInt32),
        ('szlDevice', win32more.Foundation.SIZE),
        ('szlMillimeters', win32more.Foundation.SIZE),
        ('cbPixelFormat', UInt32),
        ('offPixelFormat', UInt32),
        ('bOpenGL', UInt32),
        ('szlMicrometers', win32more.Foundation.SIZE),
    ]
    return ENHMETAHEADER
def _define_ENHMETARECORD_head():
    class ENHMETARECORD(Structure):
        pass
    return ENHMETARECORD
def _define_ENHMETARECORD():
    ENHMETARECORD = win32more.Graphics.Gdi.ENHMETARECORD_head
    ENHMETARECORD._fields_ = [
        ('iType', win32more.Graphics.Gdi.ENHANCED_METAFILE_RECORD_TYPE),
        ('nSize', UInt32),
        ('dParm', UInt32 * 1),
    ]
    return ENHMETARECORD
def _define_ENHMFENUMPROC():
    return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,POINTER(win32more.Graphics.Gdi.HANDLETABLE_head),POINTER(win32more.Graphics.Gdi.ENHMETARECORD_head),Int32,win32more.Foundation.LPARAM)
ENUM_DISPLAY_SETTINGS_MODE = UInt32
ENUM_CURRENT_SETTINGS = 4294967295
ENUM_REGISTRY_SETTINGS = 4294967294
def _define_ENUMLOGFONTA_head():
    class ENUMLOGFONTA(Structure):
        pass
    return ENUMLOGFONTA
def _define_ENUMLOGFONTA():
    ENUMLOGFONTA = win32more.Graphics.Gdi.ENUMLOGFONTA_head
    ENUMLOGFONTA._fields_ = [
        ('elfLogFont', win32more.Graphics.Gdi.LOGFONTA),
        ('elfFullName', Byte * 64),
        ('elfStyle', Byte * 32),
    ]
    return ENUMLOGFONTA
def _define_ENUMLOGFONTEXA_head():
    class ENUMLOGFONTEXA(Structure):
        pass
    return ENUMLOGFONTEXA
def _define_ENUMLOGFONTEXA():
    ENUMLOGFONTEXA = win32more.Graphics.Gdi.ENUMLOGFONTEXA_head
    ENUMLOGFONTEXA._fields_ = [
        ('elfLogFont', win32more.Graphics.Gdi.LOGFONTA),
        ('elfFullName', Byte * 64),
        ('elfStyle', Byte * 32),
        ('elfScript', Byte * 32),
    ]
    return ENUMLOGFONTEXA
def _define_ENUMLOGFONTEXDVA_head():
    class ENUMLOGFONTEXDVA(Structure):
        pass
    return ENUMLOGFONTEXDVA
def _define_ENUMLOGFONTEXDVA():
    ENUMLOGFONTEXDVA = win32more.Graphics.Gdi.ENUMLOGFONTEXDVA_head
    ENUMLOGFONTEXDVA._fields_ = [
        ('elfEnumLogfontEx', win32more.Graphics.Gdi.ENUMLOGFONTEXA),
        ('elfDesignVector', win32more.Graphics.Gdi.DESIGNVECTOR),
    ]
    return ENUMLOGFONTEXDVA
def _define_ENUMLOGFONTEXDVW_head():
    class ENUMLOGFONTEXDVW(Structure):
        pass
    return ENUMLOGFONTEXDVW
def _define_ENUMLOGFONTEXDVW():
    ENUMLOGFONTEXDVW = win32more.Graphics.Gdi.ENUMLOGFONTEXDVW_head
    ENUMLOGFONTEXDVW._fields_ = [
        ('elfEnumLogfontEx', win32more.Graphics.Gdi.ENUMLOGFONTEXW),
        ('elfDesignVector', win32more.Graphics.Gdi.DESIGNVECTOR),
    ]
    return ENUMLOGFONTEXDVW
def _define_ENUMLOGFONTEXW_head():
    class ENUMLOGFONTEXW(Structure):
        pass
    return ENUMLOGFONTEXW
def _define_ENUMLOGFONTEXW():
    ENUMLOGFONTEXW = win32more.Graphics.Gdi.ENUMLOGFONTEXW_head
    ENUMLOGFONTEXW._fields_ = [
        ('elfLogFont', win32more.Graphics.Gdi.LOGFONTW),
        ('elfFullName', Char * 64),
        ('elfStyle', Char * 32),
        ('elfScript', Char * 32),
    ]
    return ENUMLOGFONTEXW
def _define_ENUMLOGFONTW_head():
    class ENUMLOGFONTW(Structure):
        pass
    return ENUMLOGFONTW
def _define_ENUMLOGFONTW():
    ENUMLOGFONTW = win32more.Graphics.Gdi.ENUMLOGFONTW_head
    ENUMLOGFONTW._fields_ = [
        ('elfLogFont', win32more.Graphics.Gdi.LOGFONTW),
        ('elfFullName', Char * 64),
        ('elfStyle', Char * 32),
    ]
    return ENUMLOGFONTW
ETO_OPTIONS = UInt32
ETO_OPAQUE = 2
ETO_CLIPPED = 4
ETO_GLYPH_INDEX = 16
ETO_RTLREADING = 128
ETO_NUMERICSLOCAL = 1024
ETO_NUMERICSLATIN = 2048
ETO_IGNORELANGUAGE = 4096
ETO_PDY = 8192
ETO_REVERSE_INDEX_MAP = 65536
EXT_FLOOD_FILL_TYPE = UInt32
FLOODFILLBORDER = 0
FLOODFILLSURFACE = 1
def _define_EXTLOGFONTA_head():
    class EXTLOGFONTA(Structure):
        pass
    return EXTLOGFONTA
def _define_EXTLOGFONTA():
    EXTLOGFONTA = win32more.Graphics.Gdi.EXTLOGFONTA_head
    EXTLOGFONTA._fields_ = [
        ('elfLogFont', win32more.Graphics.Gdi.LOGFONTA),
        ('elfFullName', Byte * 64),
        ('elfStyle', Byte * 32),
        ('elfVersion', UInt32),
        ('elfStyleSize', UInt32),
        ('elfMatch', UInt32),
        ('elfReserved', UInt32),
        ('elfVendorId', Byte * 4),
        ('elfCulture', UInt32),
        ('elfPanose', win32more.Graphics.Gdi.PANOSE),
    ]
    return EXTLOGFONTA
def _define_EXTLOGFONTW_head():
    class EXTLOGFONTW(Structure):
        pass
    return EXTLOGFONTW
def _define_EXTLOGFONTW():
    EXTLOGFONTW = win32more.Graphics.Gdi.EXTLOGFONTW_head
    EXTLOGFONTW._fields_ = [
        ('elfLogFont', win32more.Graphics.Gdi.LOGFONTW),
        ('elfFullName', Char * 64),
        ('elfStyle', Char * 32),
        ('elfVersion', UInt32),
        ('elfStyleSize', UInt32),
        ('elfMatch', UInt32),
        ('elfReserved', UInt32),
        ('elfVendorId', Byte * 4),
        ('elfCulture', UInt32),
        ('elfPanose', win32more.Graphics.Gdi.PANOSE),
    ]
    return EXTLOGFONTW
def _define_EXTLOGPEN_head():
    class EXTLOGPEN(Structure):
        pass
    return EXTLOGPEN
def _define_EXTLOGPEN():
    EXTLOGPEN = win32more.Graphics.Gdi.EXTLOGPEN_head
    EXTLOGPEN._fields_ = [
        ('elpPenStyle', win32more.Graphics.Gdi.PEN_STYLE),
        ('elpWidth', UInt32),
        ('elpBrushStyle', UInt32),
        ('elpColor', win32more.Foundation.COLORREF),
        ('elpHatch', UIntPtr),
        ('elpNumEntries', UInt32),
        ('elpStyleEntry', UInt32 * 1),
    ]
    return EXTLOGPEN
def _define_EXTLOGPEN32_head():
    class EXTLOGPEN32(Structure):
        pass
    return EXTLOGPEN32
def _define_EXTLOGPEN32():
    EXTLOGPEN32 = win32more.Graphics.Gdi.EXTLOGPEN32_head
    EXTLOGPEN32._fields_ = [
        ('elpPenStyle', win32more.Graphics.Gdi.PEN_STYLE),
        ('elpWidth', UInt32),
        ('elpBrushStyle', UInt32),
        ('elpColor', win32more.Foundation.COLORREF),
        ('elpHatch', UInt32),
        ('elpNumEntries', UInt32),
        ('elpStyleEntry', UInt32 * 1),
    ]
    return EXTLOGPEN32
def _define_FIXED_head():
    class FIXED(Structure):
        pass
    return FIXED
def _define_FIXED():
    FIXED = win32more.Graphics.Gdi.FIXED_head
    FIXED._fields_ = [
        ('fract', UInt16),
        ('value', Int16),
    ]
    return FIXED
FONT_CHARSET = Byte
ANSI_CHARSET = 0
DEFAULT_CHARSET = 1
SYMBOL_CHARSET = 2
SHIFTJIS_CHARSET = 128
HANGEUL_CHARSET = 129
HANGUL_CHARSET = 129
GB2312_CHARSET = 134
CHINESEBIG5_CHARSET = 136
OEM_CHARSET = 255
JOHAB_CHARSET = 130
HEBREW_CHARSET = 177
ARABIC_CHARSET = 178
GREEK_CHARSET = 161
TURKISH_CHARSET = 162
VIETNAMESE_CHARSET = 163
THAI_CHARSET = 222
EASTEUROPE_CHARSET = 238
RUSSIAN_CHARSET = 204
MAC_CHARSET = 77
BALTIC_CHARSET = 186
FONT_CLIP_PRECISION = Byte
CLIP_DEFAULT_PRECIS = 0
CLIP_CHARACTER_PRECIS = 1
CLIP_STROKE_PRECIS = 2
CLIP_MASK = 15
CLIP_LH_ANGLES = 16
CLIP_TT_ALWAYS = 32
CLIP_DFA_DISABLE = 64
CLIP_EMBEDDED = 128
CLIP_DFA_OVERRIDE = 64
FONT_FAMILY = Byte
FF_DECORATIVE = 80
FF_DONTCARE = 0
FF_MODERN = 48
FF_ROMAN = 16
FF_SCRIPT = 64
FF_SWISS = 32
FONT_LICENSE_PRIVS = UInt32
LICENSE_PREVIEWPRINT = 4
LICENSE_EDITABLE = 8
LICENSE_INSTALLABLE = 0
LICENSE_NOEMBEDDING = 2
LICENSE_DEFAULT = 0
FONT_OUTPUT_PRECISION = Byte
OUT_DEFAULT_PRECIS = 0
OUT_STRING_PRECIS = 1
OUT_CHARACTER_PRECIS = 2
OUT_STROKE_PRECIS = 3
OUT_TT_PRECIS = 4
OUT_DEVICE_PRECIS = 5
OUT_RASTER_PRECIS = 6
OUT_TT_ONLY_PRECIS = 7
OUT_OUTLINE_PRECIS = 8
OUT_SCREEN_OUTLINE_PRECIS = 9
OUT_PS_ONLY_PRECIS = 10
FONT_PITCH = Byte
DEFAULT_PITCH = 0
FIXED_PITCH = 1
VARIABLE_PITCH = 2
FONT_QUALITY = Byte
DEFAULT_QUALITY = 0
DRAFT_QUALITY = 1
PROOF_QUALITY = 2
NONANTIALIASED_QUALITY = 3
ANTIALIASED_QUALITY = 4
CLEARTYPE_QUALITY = 5
FONT_RESOURCE_CHARACTERISTICS = UInt32
FR_PRIVATE = 16
FR_NOT_ENUM = 32
FONT_WEIGHT = UInt32
FW_DONTCARE = 0
FW_THIN = 100
FW_EXTRALIGHT = 200
FW_LIGHT = 300
FW_NORMAL = 400
FW_MEDIUM = 500
FW_SEMIBOLD = 600
FW_BOLD = 700
FW_EXTRABOLD = 800
FW_HEAVY = 900
FW_ULTRALIGHT = 200
FW_REGULAR = 400
FW_DEMIBOLD = 600
FW_ULTRABOLD = 800
FW_BLACK = 900
def _define_FONTENUMPROCA():
    return WINFUNCTYPE(Int32,POINTER(win32more.Graphics.Gdi.LOGFONTA_head),POINTER(win32more.Graphics.Gdi.TEXTMETRICA_head),UInt32,win32more.Foundation.LPARAM)
def _define_FONTENUMPROCW():
    return WINFUNCTYPE(Int32,POINTER(win32more.Graphics.Gdi.LOGFONTW_head),POINTER(win32more.Graphics.Gdi.TEXTMETRICW_head),UInt32,win32more.Foundation.LPARAM)
def _define_GCP_RESULTSA_head():
    class GCP_RESULTSA(Structure):
        pass
    return GCP_RESULTSA
def _define_GCP_RESULTSA():
    GCP_RESULTSA = win32more.Graphics.Gdi.GCP_RESULTSA_head
    GCP_RESULTSA._fields_ = [
        ('lStructSize', UInt32),
        ('lpOutString', win32more.Foundation.PSTR),
        ('lpOrder', POINTER(UInt32)),
        ('lpDx', POINTER(Int32)),
        ('lpCaretPos', POINTER(Int32)),
        ('lpClass', win32more.Foundation.PSTR),
        ('lpGlyphs', win32more.Foundation.PWSTR),
        ('nGlyphs', UInt32),
        ('nMaxFit', Int32),
    ]
    return GCP_RESULTSA
def _define_GCP_RESULTSW_head():
    class GCP_RESULTSW(Structure):
        pass
    return GCP_RESULTSW
def _define_GCP_RESULTSW():
    GCP_RESULTSW = win32more.Graphics.Gdi.GCP_RESULTSW_head
    GCP_RESULTSW._fields_ = [
        ('lStructSize', UInt32),
        ('lpOutString', win32more.Foundation.PWSTR),
        ('lpOrder', POINTER(UInt32)),
        ('lpDx', POINTER(Int32)),
        ('lpCaretPos', POINTER(Int32)),
        ('lpClass', win32more.Foundation.PSTR),
        ('lpGlyphs', win32more.Foundation.PWSTR),
        ('nGlyphs', UInt32),
        ('nMaxFit', Int32),
    ]
    return GCP_RESULTSW
GDI_REGION_TYPE = Int32
RGN_ERROR = 0
NULLREGION = 1
SIMPLEREGION = 2
COMPLEXREGION = 3
GET_CHARACTER_PLACEMENT_FLAGS = UInt32
GCP_CLASSIN = 524288
GCP_DIACRITIC = 256
GCP_DISPLAYZWG = 4194304
GCP_GLYPHSHAPE = 16
GCP_JUSTIFY = 65536
GCP_KASHIDA = 1024
GCP_LIGATE = 32
GCP_MAXEXTENT = 1048576
GCP_NEUTRALOVERRIDE = 33554432
GCP_NUMERICOVERRIDE = 16777216
GCP_NUMERICSLATIN = 67108864
GCP_NUMERICSLOCAL = 134217728
GCP_REORDER = 2
GCP_SYMSWAPOFF = 8388608
GCP_USEKERNING = 8
GET_DCX_FLAGS = UInt32
DCX_WINDOW = 1
DCX_CACHE = 2
DCX_PARENTCLIP = 32
DCX_CLIPSIBLINGS = 16
DCX_CLIPCHILDREN = 8
DCX_NORESETATTRS = 4
DCX_LOCKWINDOWUPDATE = 1024
DCX_EXCLUDERGN = 64
DCX_INTERSECTRGN = 128
DCX_INTERSECTUPDATE = 512
DCX_VALIDATE = 2097152
GET_DEVICE_CAPS_INDEX = UInt32
DRIVERVERSION = 0
TECHNOLOGY = 2
HORZSIZE = 4
VERTSIZE = 6
HORZRES = 8
VERTRES = 10
BITSPIXEL = 12
PLANES = 14
NUMBRUSHES = 16
NUMPENS = 18
NUMMARKERS = 20
NUMFONTS = 22
NUMCOLORS = 24
PDEVICESIZE = 26
CURVECAPS = 28
LINECAPS = 30
POLYGONALCAPS = 32
TEXTCAPS = 34
CLIPCAPS = 36
RASTERCAPS = 38
ASPECTX = 40
ASPECTY = 42
ASPECTXY = 44
LOGPIXELSX = 88
LOGPIXELSY = 90
SIZEPALETTE = 104
NUMRESERVED = 106
COLORRES = 108
PHYSICALWIDTH = 110
PHYSICALHEIGHT = 111
PHYSICALOFFSETX = 112
PHYSICALOFFSETY = 113
SCALINGFACTORX = 114
SCALINGFACTORY = 115
VREFRESH = 116
DESKTOPVERTRES = 117
DESKTOPHORZRES = 118
BLTALIGNMENT = 119
SHADEBLENDCAPS = 120
COLORMGMTCAPS = 121
GET_GLYPH_OUTLINE_FORMAT = UInt32
GGO_BEZIER = 3
GGO_BITMAP = 1
GGO_GLYPH_INDEX = 128
GGO_GRAY2_BITMAP = 4
GGO_GRAY4_BITMAP = 5
GGO_GRAY8_BITMAP = 6
GGO_METRICS = 0
GGO_NATIVE = 2
GGO_UNHINTED = 256
GET_STOCK_OBJECT_FLAGS = UInt32
BLACK_BRUSH = 4
DKGRAY_BRUSH = 3
DC_BRUSH = 18
GRAY_BRUSH = 2
HOLLOW_BRUSH = 5
LTGRAY_BRUSH = 1
NULL_BRUSH = 5
WHITE_BRUSH = 0
BLACK_PEN = 7
DC_PEN = 19
NULL_PEN = 8
WHITE_PEN = 6
ANSI_FIXED_FONT = 11
ANSI_VAR_FONT = 12
DEVICE_DEFAULT_FONT = 14
DEFAULT_GUI_FONT = 17
OEM_FIXED_FONT = 10
SYSTEM_FONT = 13
SYSTEM_FIXED_FONT = 16
DEFAULT_PALETTE = 15
def _define_GLYPHMETRICS_head():
    class GLYPHMETRICS(Structure):
        pass
    return GLYPHMETRICS
def _define_GLYPHMETRICS():
    GLYPHMETRICS = win32more.Graphics.Gdi.GLYPHMETRICS_head
    GLYPHMETRICS._fields_ = [
        ('gmBlackBoxX', UInt32),
        ('gmBlackBoxY', UInt32),
        ('gmptGlyphOrigin', win32more.Foundation.POINT),
        ('gmCellIncX', Int16),
        ('gmCellIncY', Int16),
    ]
    return GLYPHMETRICS
def _define_GLYPHSET_head():
    class GLYPHSET(Structure):
        pass
    return GLYPHSET
def _define_GLYPHSET():
    GLYPHSET = win32more.Graphics.Gdi.GLYPHSET_head
    GLYPHSET._fields_ = [
        ('cbThis', UInt32),
        ('flAccel', UInt32),
        ('cGlyphsSupported', UInt32),
        ('cRanges', UInt32),
        ('ranges', win32more.Graphics.Gdi.WCRANGE * 1),
    ]
    return GLYPHSET
def _define_GOBJENUMPROC():
    return WINFUNCTYPE(Int32,c_void_p,win32more.Foundation.LPARAM)
GRADIENT_FILL = UInt32
GRADIENT_FILL_RECT_H = 0
GRADIENT_FILL_RECT_V = 1
GRADIENT_FILL_TRIANGLE = 2
def _define_GRADIENT_RECT_head():
    class GRADIENT_RECT(Structure):
        pass
    return GRADIENT_RECT
def _define_GRADIENT_RECT():
    GRADIENT_RECT = win32more.Graphics.Gdi.GRADIENT_RECT_head
    GRADIENT_RECT._fields_ = [
        ('UpperLeft', UInt32),
        ('LowerRight', UInt32),
    ]
    return GRADIENT_RECT
def _define_GRADIENT_TRIANGLE_head():
    class GRADIENT_TRIANGLE(Structure):
        pass
    return GRADIENT_TRIANGLE
def _define_GRADIENT_TRIANGLE():
    GRADIENT_TRIANGLE = win32more.Graphics.Gdi.GRADIENT_TRIANGLE_head
    GRADIENT_TRIANGLE._fields_ = [
        ('Vertex1', UInt32),
        ('Vertex2', UInt32),
        ('Vertex3', UInt32),
    ]
    return GRADIENT_TRIANGLE
GRAPHICS_MODE = UInt32
GM_COMPATIBLE = 1
GM_ADVANCED = 2
def _define_GRAYSTRINGPROC():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,win32more.Foundation.LPARAM,Int32)
def _define_HANDLETABLE_head():
    class HANDLETABLE(Structure):
        pass
    return HANDLETABLE
def _define_HANDLETABLE():
    HANDLETABLE = win32more.Graphics.Gdi.HANDLETABLE_head
    HANDLETABLE._fields_ = [
        ('objectHandle', win32more.Graphics.Gdi.HGDIOBJ * 1),
    ]
    return HANDLETABLE
HATCH_BRUSH_STYLE = UInt32
HS_BDIAGONAL = 3
HS_CROSS = 4
HS_DIAGCROSS = 5
HS_FDIAGONAL = 2
HS_HORIZONTAL = 0
HS_VERTICAL = 1
HBITMAP = IntPtr
HBRUSH = IntPtr
HDC = IntPtr
HDC_MAP_MODE = UInt32
MM_ANISOTROPIC = 8
MM_HIENGLISH = 5
MM_HIMETRIC = 3
MM_ISOTROPIC = 7
MM_LOENGLISH = 4
MM_LOMETRIC = 2
MM_TEXT = 1
MM_TWIPS = 6
HdcMetdataEnhFileHandle = IntPtr
HdcMetdataFileHandle = IntPtr
HENHMETAFILE = IntPtr
HFONT = IntPtr
HGDIOBJ = IntPtr
HMETAFILE = IntPtr
HMONITOR = IntPtr
HPALETTE = IntPtr
HPEN = IntPtr
HRGN = IntPtr
def _define_KERNINGPAIR_head():
    class KERNINGPAIR(Structure):
        pass
    return KERNINGPAIR
def _define_KERNINGPAIR():
    KERNINGPAIR = win32more.Graphics.Gdi.KERNINGPAIR_head
    KERNINGPAIR._fields_ = [
        ('wFirst', UInt16),
        ('wSecond', UInt16),
        ('iKernAmount', Int32),
    ]
    return KERNINGPAIR
def _define_LINEDDAPROC():
    return WINFUNCTYPE(Void,Int32,Int32,win32more.Foundation.LPARAM)
def _define_LOGBRUSH_head():
    class LOGBRUSH(Structure):
        pass
    return LOGBRUSH
def _define_LOGBRUSH():
    LOGBRUSH = win32more.Graphics.Gdi.LOGBRUSH_head
    LOGBRUSH._fields_ = [
        ('lbStyle', win32more.Graphics.Gdi.BRUSH_STYLE),
        ('lbColor', win32more.Foundation.COLORREF),
        ('lbHatch', UIntPtr),
    ]
    return LOGBRUSH
def _define_LOGBRUSH32_head():
    class LOGBRUSH32(Structure):
        pass
    return LOGBRUSH32
def _define_LOGBRUSH32():
    LOGBRUSH32 = win32more.Graphics.Gdi.LOGBRUSH32_head
    LOGBRUSH32._fields_ = [
        ('lbStyle', win32more.Graphics.Gdi.BRUSH_STYLE),
        ('lbColor', win32more.Foundation.COLORREF),
        ('lbHatch', UInt32),
    ]
    return LOGBRUSH32
def _define_LOGFONTA_head():
    class LOGFONTA(Structure):
        pass
    return LOGFONTA
def _define_LOGFONTA():
    LOGFONTA = win32more.Graphics.Gdi.LOGFONTA_head
    LOGFONTA._fields_ = [
        ('lfHeight', Int32),
        ('lfWidth', Int32),
        ('lfEscapement', Int32),
        ('lfOrientation', Int32),
        ('lfWeight', Int32),
        ('lfItalic', Byte),
        ('lfUnderline', Byte),
        ('lfStrikeOut', Byte),
        ('lfCharSet', win32more.Graphics.Gdi.FONT_CHARSET),
        ('lfOutPrecision', win32more.Graphics.Gdi.FONT_OUTPUT_PRECISION),
        ('lfClipPrecision', win32more.Graphics.Gdi.FONT_CLIP_PRECISION),
        ('lfQuality', win32more.Graphics.Gdi.FONT_QUALITY),
        ('lfPitchAndFamily', Byte),
        ('lfFaceName', win32more.Foundation.CHAR * 32),
    ]
    return LOGFONTA
def _define_LOGFONTW_head():
    class LOGFONTW(Structure):
        pass
    return LOGFONTW
def _define_LOGFONTW():
    LOGFONTW = win32more.Graphics.Gdi.LOGFONTW_head
    LOGFONTW._fields_ = [
        ('lfHeight', Int32),
        ('lfWidth', Int32),
        ('lfEscapement', Int32),
        ('lfOrientation', Int32),
        ('lfWeight', Int32),
        ('lfItalic', Byte),
        ('lfUnderline', Byte),
        ('lfStrikeOut', Byte),
        ('lfCharSet', win32more.Graphics.Gdi.FONT_CHARSET),
        ('lfOutPrecision', win32more.Graphics.Gdi.FONT_OUTPUT_PRECISION),
        ('lfClipPrecision', win32more.Graphics.Gdi.FONT_CLIP_PRECISION),
        ('lfQuality', win32more.Graphics.Gdi.FONT_QUALITY),
        ('lfPitchAndFamily', Byte),
        ('lfFaceName', Char * 32),
    ]
    return LOGFONTW
def _define_LOGPALETTE_head():
    class LOGPALETTE(Structure):
        pass
    return LOGPALETTE
def _define_LOGPALETTE():
    LOGPALETTE = win32more.Graphics.Gdi.LOGPALETTE_head
    LOGPALETTE._fields_ = [
        ('palVersion', UInt16),
        ('palNumEntries', UInt16),
        ('palPalEntry', win32more.Graphics.Gdi.PALETTEENTRY * 1),
    ]
    return LOGPALETTE
def _define_LOGPEN_head():
    class LOGPEN(Structure):
        pass
    return LOGPEN
def _define_LOGPEN():
    LOGPEN = win32more.Graphics.Gdi.LOGPEN_head
    LOGPEN._fields_ = [
        ('lopnStyle', win32more.Graphics.Gdi.PEN_STYLE),
        ('lopnWidth', win32more.Foundation.POINT),
        ('lopnColor', win32more.Foundation.COLORREF),
    ]
    return LOGPEN
def _define_LPFNDEVCAPS():
    return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(win32more.Graphics.Gdi.DEVMODEA_head))
def _define_LPFNDEVMODE():
    return WINFUNCTYPE(UInt32,win32more.Foundation.HWND,win32more.Foundation.HINSTANCE,POINTER(win32more.Graphics.Gdi.DEVMODEA_head),win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Graphics.Gdi.DEVMODEA_head),win32more.Foundation.PSTR,UInt32)
def _define_MAT2_head():
    class MAT2(Structure):
        pass
    return MAT2
def _define_MAT2():
    MAT2 = win32more.Graphics.Gdi.MAT2_head
    MAT2._fields_ = [
        ('eM11', win32more.Graphics.Gdi.FIXED),
        ('eM12', win32more.Graphics.Gdi.FIXED),
        ('eM21', win32more.Graphics.Gdi.FIXED),
        ('eM22', win32more.Graphics.Gdi.FIXED),
    ]
    return MAT2
def _define_METAHEADER_head():
    class METAHEADER(Structure):
        pass
    return METAHEADER
def _define_METAHEADER():
    METAHEADER = win32more.Graphics.Gdi.METAHEADER_head
    METAHEADER._pack_ = 2
    METAHEADER._fields_ = [
        ('mtType', UInt16),
        ('mtHeaderSize', UInt16),
        ('mtVersion', UInt16),
        ('mtSize', UInt32),
        ('mtNoObjects', UInt16),
        ('mtMaxRecord', UInt32),
        ('mtNoParameters', UInt16),
    ]
    return METAHEADER
def _define_METARECORD_head():
    class METARECORD(Structure):
        pass
    return METARECORD
def _define_METARECORD():
    METARECORD = win32more.Graphics.Gdi.METARECORD_head
    METARECORD._fields_ = [
        ('rdSize', UInt32),
        ('rdFunction', UInt16),
        ('rdParm', UInt16 * 1),
    ]
    return METARECORD
def _define_MFENUMPROC():
    return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,POINTER(win32more.Graphics.Gdi.HANDLETABLE_head),POINTER(win32more.Graphics.Gdi.METARECORD_head),Int32,win32more.Foundation.LPARAM)
MODIFY_WORLD_TRANSFORM_MODE = UInt32
MWT_IDENTITY = 1
MWT_LEFTMULTIPLY = 2
MWT_RIGHTMULTIPLY = 3
MONITOR_FROM_FLAGS = UInt32
MONITOR_DEFAULTTONEAREST = 2
MONITOR_DEFAULTTONULL = 0
MONITOR_DEFAULTTOPRIMARY = 1
def _define_MONITORENUMPROC():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HMONITOR,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.RECT_head),win32more.Foundation.LPARAM)
def _define_MONITORINFO_head():
    class MONITORINFO(Structure):
        pass
    return MONITORINFO
def _define_MONITORINFO():
    MONITORINFO = win32more.Graphics.Gdi.MONITORINFO_head
    MONITORINFO._fields_ = [
        ('cbSize', UInt32),
        ('rcMonitor', win32more.Foundation.RECT),
        ('rcWork', win32more.Foundation.RECT),
        ('dwFlags', UInt32),
    ]
    return MONITORINFO
def _define_MONITORINFOEXA_head():
    class MONITORINFOEXA(Structure):
        pass
    return MONITORINFOEXA
def _define_MONITORINFOEXA():
    MONITORINFOEXA = win32more.Graphics.Gdi.MONITORINFOEXA_head
    MONITORINFOEXA._fields_ = [
        ('monitorInfo', win32more.Graphics.Gdi.MONITORINFO),
        ('szDevice', win32more.Foundation.CHAR * 32),
    ]
    return MONITORINFOEXA
def _define_MONITORINFOEXW_head():
    class MONITORINFOEXW(Structure):
        pass
    return MONITORINFOEXW
def _define_MONITORINFOEXW():
    MONITORINFOEXW = win32more.Graphics.Gdi.MONITORINFOEXW_head
    MONITORINFOEXW._fields_ = [
        ('monitorInfo', win32more.Graphics.Gdi.MONITORINFO),
        ('szDevice', Char * 32),
    ]
    return MONITORINFOEXW
def _define_NEWTEXTMETRICA_head():
    class NEWTEXTMETRICA(Structure):
        pass
    return NEWTEXTMETRICA
def _define_NEWTEXTMETRICA():
    NEWTEXTMETRICA = win32more.Graphics.Gdi.NEWTEXTMETRICA_head
    NEWTEXTMETRICA._fields_ = [
        ('tmHeight', Int32),
        ('tmAscent', Int32),
        ('tmDescent', Int32),
        ('tmInternalLeading', Int32),
        ('tmExternalLeading', Int32),
        ('tmAveCharWidth', Int32),
        ('tmMaxCharWidth', Int32),
        ('tmWeight', Int32),
        ('tmOverhang', Int32),
        ('tmDigitizedAspectX', Int32),
        ('tmDigitizedAspectY', Int32),
        ('tmFirstChar', Byte),
        ('tmLastChar', Byte),
        ('tmDefaultChar', Byte),
        ('tmBreakChar', Byte),
        ('tmItalic', Byte),
        ('tmUnderlined', Byte),
        ('tmStruckOut', Byte),
        ('tmPitchAndFamily', win32more.Graphics.Gdi.TMPF_FLAGS),
        ('tmCharSet', Byte),
        ('ntmFlags', UInt32),
        ('ntmSizeEM', UInt32),
        ('ntmCellHeight', UInt32),
        ('ntmAvgWidth', UInt32),
    ]
    return NEWTEXTMETRICA
def _define_NEWTEXTMETRICW_head():
    class NEWTEXTMETRICW(Structure):
        pass
    return NEWTEXTMETRICW
def _define_NEWTEXTMETRICW():
    NEWTEXTMETRICW = win32more.Graphics.Gdi.NEWTEXTMETRICW_head
    NEWTEXTMETRICW._fields_ = [
        ('tmHeight', Int32),
        ('tmAscent', Int32),
        ('tmDescent', Int32),
        ('tmInternalLeading', Int32),
        ('tmExternalLeading', Int32),
        ('tmAveCharWidth', Int32),
        ('tmMaxCharWidth', Int32),
        ('tmWeight', Int32),
        ('tmOverhang', Int32),
        ('tmDigitizedAspectX', Int32),
        ('tmDigitizedAspectY', Int32),
        ('tmFirstChar', Char),
        ('tmLastChar', Char),
        ('tmDefaultChar', Char),
        ('tmBreakChar', Char),
        ('tmItalic', Byte),
        ('tmUnderlined', Byte),
        ('tmStruckOut', Byte),
        ('tmPitchAndFamily', win32more.Graphics.Gdi.TMPF_FLAGS),
        ('tmCharSet', Byte),
        ('ntmFlags', UInt32),
        ('ntmSizeEM', UInt32),
        ('ntmCellHeight', UInt32),
        ('ntmAvgWidth', UInt32),
    ]
    return NEWTEXTMETRICW
OBJ_TYPE = Int32
OBJ_PEN = 1
OBJ_BRUSH = 2
OBJ_DC = 3
OBJ_METADC = 4
OBJ_PAL = 5
OBJ_FONT = 6
OBJ_BITMAP = 7
OBJ_REGION = 8
OBJ_METAFILE = 9
OBJ_MEMDC = 10
OBJ_EXTPEN = 11
OBJ_ENHMETADC = 12
OBJ_ENHMETAFILE = 13
OBJ_COLORSPACE = 14
def _define_OUTLINETEXTMETRICA_head():
    class OUTLINETEXTMETRICA(Structure):
        pass
    return OUTLINETEXTMETRICA
def _define_OUTLINETEXTMETRICA():
    OUTLINETEXTMETRICA = win32more.Graphics.Gdi.OUTLINETEXTMETRICA_head
    OUTLINETEXTMETRICA._fields_ = [
        ('otmSize', UInt32),
        ('otmTextMetrics', win32more.Graphics.Gdi.TEXTMETRICA),
        ('otmFiller', Byte),
        ('otmPanoseNumber', win32more.Graphics.Gdi.PANOSE),
        ('otmfsSelection', UInt32),
        ('otmfsType', UInt32),
        ('otmsCharSlopeRise', Int32),
        ('otmsCharSlopeRun', Int32),
        ('otmItalicAngle', Int32),
        ('otmEMSquare', UInt32),
        ('otmAscent', Int32),
        ('otmDescent', Int32),
        ('otmLineGap', UInt32),
        ('otmsCapEmHeight', UInt32),
        ('otmsXHeight', UInt32),
        ('otmrcFontBox', win32more.Foundation.RECT),
        ('otmMacAscent', Int32),
        ('otmMacDescent', Int32),
        ('otmMacLineGap', UInt32),
        ('otmusMinimumPPEM', UInt32),
        ('otmptSubscriptSize', win32more.Foundation.POINT),
        ('otmptSubscriptOffset', win32more.Foundation.POINT),
        ('otmptSuperscriptSize', win32more.Foundation.POINT),
        ('otmptSuperscriptOffset', win32more.Foundation.POINT),
        ('otmsStrikeoutSize', UInt32),
        ('otmsStrikeoutPosition', Int32),
        ('otmsUnderscoreSize', Int32),
        ('otmsUnderscorePosition', Int32),
        ('otmpFamilyName', win32more.Foundation.PSTR),
        ('otmpFaceName', win32more.Foundation.PSTR),
        ('otmpStyleName', win32more.Foundation.PSTR),
        ('otmpFullName', win32more.Foundation.PSTR),
    ]
    return OUTLINETEXTMETRICA
def _define_OUTLINETEXTMETRICW_head():
    class OUTLINETEXTMETRICW(Structure):
        pass
    return OUTLINETEXTMETRICW
def _define_OUTLINETEXTMETRICW():
    OUTLINETEXTMETRICW = win32more.Graphics.Gdi.OUTLINETEXTMETRICW_head
    OUTLINETEXTMETRICW._fields_ = [
        ('otmSize', UInt32),
        ('otmTextMetrics', win32more.Graphics.Gdi.TEXTMETRICW),
        ('otmFiller', Byte),
        ('otmPanoseNumber', win32more.Graphics.Gdi.PANOSE),
        ('otmfsSelection', UInt32),
        ('otmfsType', UInt32),
        ('otmsCharSlopeRise', Int32),
        ('otmsCharSlopeRun', Int32),
        ('otmItalicAngle', Int32),
        ('otmEMSquare', UInt32),
        ('otmAscent', Int32),
        ('otmDescent', Int32),
        ('otmLineGap', UInt32),
        ('otmsCapEmHeight', UInt32),
        ('otmsXHeight', UInt32),
        ('otmrcFontBox', win32more.Foundation.RECT),
        ('otmMacAscent', Int32),
        ('otmMacDescent', Int32),
        ('otmMacLineGap', UInt32),
        ('otmusMinimumPPEM', UInt32),
        ('otmptSubscriptSize', win32more.Foundation.POINT),
        ('otmptSubscriptOffset', win32more.Foundation.POINT),
        ('otmptSuperscriptSize', win32more.Foundation.POINT),
        ('otmptSuperscriptOffset', win32more.Foundation.POINT),
        ('otmsStrikeoutSize', UInt32),
        ('otmsStrikeoutPosition', Int32),
        ('otmsUnderscoreSize', Int32),
        ('otmsUnderscorePosition', Int32),
        ('otmpFamilyName', win32more.Foundation.PSTR),
        ('otmpFaceName', win32more.Foundation.PSTR),
        ('otmpStyleName', win32more.Foundation.PSTR),
        ('otmpFullName', win32more.Foundation.PSTR),
    ]
    return OUTLINETEXTMETRICW
def _define_PAINTSTRUCT_head():
    class PAINTSTRUCT(Structure):
        pass
    return PAINTSTRUCT
def _define_PAINTSTRUCT():
    PAINTSTRUCT = win32more.Graphics.Gdi.PAINTSTRUCT_head
    PAINTSTRUCT._fields_ = [
        ('hdc', win32more.Graphics.Gdi.HDC),
        ('fErase', win32more.Foundation.BOOL),
        ('rcPaint', win32more.Foundation.RECT),
        ('fRestore', win32more.Foundation.BOOL),
        ('fIncUpdate', win32more.Foundation.BOOL),
        ('rgbReserved', Byte * 32),
    ]
    return PAINTSTRUCT
def _define_PALETTEENTRY_head():
    class PALETTEENTRY(Structure):
        pass
    return PALETTEENTRY
def _define_PALETTEENTRY():
    PALETTEENTRY = win32more.Graphics.Gdi.PALETTEENTRY_head
    PALETTEENTRY._fields_ = [
        ('peRed', Byte),
        ('peGreen', Byte),
        ('peBlue', Byte),
        ('peFlags', Byte),
    ]
    return PALETTEENTRY
PAN_ARM_STYLE = UInt32
PAN_ARM_ANY = 0
PAN_ARM_NO_FIT = 1
PAN_STRAIGHT_ARMS_HORZ = 2
PAN_STRAIGHT_ARMS_WEDGE = 3
PAN_STRAIGHT_ARMS_VERT = 4
PAN_STRAIGHT_ARMS_SINGLE_SERIF = 5
PAN_STRAIGHT_ARMS_DOUBLE_SERIF = 6
PAN_BENT_ARMS_HORZ = 7
PAN_BENT_ARMS_WEDGE = 8
PAN_BENT_ARMS_VERT = 9
PAN_BENT_ARMS_SINGLE_SERIF = 10
PAN_BENT_ARMS_DOUBLE_SERIF = 11
PAN_CONTRAST = UInt32
PAN_CONTRAST_ANY = 0
PAN_CONTRAST_NO_FIT = 1
PAN_CONTRAST_INDEX = 4
PAN_CONTRAST_NONE = 2
PAN_CONTRAST_VERY_LOW = 3
PAN_CONTRAST_LOW = 4
PAN_CONTRAST_MEDIUM_LOW = 5
PAN_CONTRAST_MEDIUM = 6
PAN_CONTRAST_MEDIUM_HIGH = 7
PAN_CONTRAST_HIGH = 8
PAN_CONTRAST_VERY_HIGH = 9
PAN_FAMILY_TYPE = UInt32
PAN_FAMILY_ANY = 0
PAN_FAMILY_NO_FIT = 1
PAN_FAMILY_TEXT_DISPLAY = 2
PAN_FAMILY_SCRIPT = 3
PAN_FAMILY_DECORATIVE = 4
PAN_FAMILY_PICTORIAL = 5
PAN_LETT_FORM = UInt32
PAN_LETT_FORM_ANY = 0
PAN_LETT_FORM_NO_FIT = 1
PAN_LETT_NORMAL_CONTACT = 2
PAN_LETT_NORMAL_WEIGHTED = 3
PAN_LETT_NORMAL_BOXED = 4
PAN_LETT_NORMAL_FLATTENED = 5
PAN_LETT_NORMAL_ROUNDED = 6
PAN_LETT_NORMAL_OFF_CENTER = 7
PAN_LETT_NORMAL_SQUARE = 8
PAN_LETT_OBLIQUE_CONTACT = 9
PAN_LETT_OBLIQUE_WEIGHTED = 10
PAN_LETT_OBLIQUE_BOXED = 11
PAN_LETT_OBLIQUE_FLATTENED = 12
PAN_LETT_OBLIQUE_ROUNDED = 13
PAN_LETT_OBLIQUE_OFF_CENTER = 14
PAN_LETT_OBLIQUE_SQUARE = 15
PAN_MIDLINE = UInt32
PAN_MIDLINE_ANY = 0
PAN_MIDLINE_NO_FIT = 1
PAN_MIDLINE_INDEX = 8
PAN_MIDLINE_STANDARD_TRIMMED = 2
PAN_MIDLINE_STANDARD_POINTED = 3
PAN_MIDLINE_STANDARD_SERIFED = 4
PAN_MIDLINE_HIGH_TRIMMED = 5
PAN_MIDLINE_HIGH_POINTED = 6
PAN_MIDLINE_HIGH_SERIFED = 7
PAN_MIDLINE_CONSTANT_TRIMMED = 8
PAN_MIDLINE_CONSTANT_POINTED = 9
PAN_MIDLINE_CONSTANT_SERIFED = 10
PAN_MIDLINE_LOW_TRIMMED = 11
PAN_MIDLINE_LOW_POINTED = 12
PAN_MIDLINE_LOW_SERIFED = 13
PAN_PROPORTION = UInt32
PAN_PROP_ANY = 0
PAN_PROP_NO_FIT = 1
PAN_PROP_OLD_STYLE = 2
PAN_PROP_MODERN = 3
PAN_PROP_EVEN_WIDTH = 4
PAN_PROP_EXPANDED = 5
PAN_PROP_CONDENSED = 6
PAN_PROP_VERY_EXPANDED = 7
PAN_PROP_VERY_CONDENSED = 8
PAN_PROP_MONOSPACED = 9
PAN_SERIF_STYLE = UInt32
PAN_SERIF_ANY = 0
PAN_SERIF_NO_FIT = 1
PAN_SERIF_COVE = 2
PAN_SERIF_OBTUSE_COVE = 3
PAN_SERIF_SQUARE_COVE = 4
PAN_SERIF_OBTUSE_SQUARE_COVE = 5
PAN_SERIF_SQUARE = 6
PAN_SERIF_THIN = 7
PAN_SERIF_BONE = 8
PAN_SERIF_EXAGGERATED = 9
PAN_SERIF_TRIANGLE = 10
PAN_SERIF_NORMAL_SANS = 11
PAN_SERIF_OBTUSE_SANS = 12
PAN_SERIF_PERP_SANS = 13
PAN_SERIF_FLARED = 14
PAN_SERIF_ROUNDED = 15
PAN_STROKE_VARIATION = UInt32
PAN_STROKE_ANY = 0
PAN_STROKE_NO_FIT = 1
PAN_STROKE_GRADUAL_DIAG = 2
PAN_STROKE_GRADUAL_TRAN = 3
PAN_STROKE_GRADUAL_VERT = 4
PAN_STROKE_GRADUAL_HORZ = 5
PAN_STROKE_RAPID_VERT = 6
PAN_STROKE_RAPID_HORZ = 7
PAN_STROKE_INSTANT_VERT = 8
PAN_WEIGHT = UInt32
PAN_WEIGHT_ANY = 0
PAN_WEIGHT_NO_FIT = 1
PAN_WEIGHT_INDEX = 2
PAN_WEIGHT_VERY_LIGHT = 2
PAN_WEIGHT_LIGHT = 3
PAN_WEIGHT_THIN = 4
PAN_WEIGHT_BOOK = 5
PAN_WEIGHT_MEDIUM = 6
PAN_WEIGHT_DEMI = 7
PAN_WEIGHT_BOLD = 8
PAN_WEIGHT_HEAVY = 9
PAN_WEIGHT_BLACK = 10
PAN_WEIGHT_NORD = 11
PAN_XHEIGHT = UInt32
PAN_XHEIGHT_ANY = 0
PAN_XHEIGHT_NO_FIT = 1
PAN_XHEIGHT_INDEX = 9
PAN_XHEIGHT_CONSTANT_SMALL = 2
PAN_XHEIGHT_CONSTANT_STD = 3
PAN_XHEIGHT_CONSTANT_LARGE = 4
PAN_XHEIGHT_DUCKING_SMALL = 5
PAN_XHEIGHT_DUCKING_STD = 6
PAN_XHEIGHT_DUCKING_LARGE = 7
def _define_PANOSE_head():
    class PANOSE(Structure):
        pass
    return PANOSE
def _define_PANOSE():
    PANOSE = win32more.Graphics.Gdi.PANOSE_head
    PANOSE._fields_ = [
        ('bFamilyType', win32more.Graphics.Gdi.PAN_FAMILY_TYPE),
        ('bSerifStyle', win32more.Graphics.Gdi.PAN_SERIF_STYLE),
        ('bWeight', win32more.Graphics.Gdi.PAN_WEIGHT),
        ('bProportion', win32more.Graphics.Gdi.PAN_PROPORTION),
        ('bContrast', win32more.Graphics.Gdi.PAN_CONTRAST),
        ('bStrokeVariation', win32more.Graphics.Gdi.PAN_STROKE_VARIATION),
        ('bArmStyle', win32more.Graphics.Gdi.PAN_ARM_STYLE),
        ('bLetterform', win32more.Graphics.Gdi.PAN_LETT_FORM),
        ('bMidline', win32more.Graphics.Gdi.PAN_MIDLINE),
        ('bXHeight', win32more.Graphics.Gdi.PAN_XHEIGHT),
    ]
    return PANOSE
def _define_PELARRAY_head():
    class PELARRAY(Structure):
        pass
    return PELARRAY
def _define_PELARRAY():
    PELARRAY = win32more.Graphics.Gdi.PELARRAY_head
    PELARRAY._fields_ = [
        ('paXCount', Int32),
        ('paYCount', Int32),
        ('paXExt', Int32),
        ('paYExt', Int32),
        ('paRGBs', Byte),
    ]
    return PELARRAY
PEN_STYLE = UInt32
PS_GEOMETRIC = 65536
PS_COSMETIC = 0
PS_SOLID = 0
PS_DASH = 1
PS_DOT = 2
PS_DASHDOT = 3
PS_DASHDOTDOT = 4
PS_NULL = 5
PS_INSIDEFRAME = 6
PS_USERSTYLE = 7
PS_ALTERNATE = 8
PS_STYLE_MASK = 15
PS_ENDCAP_ROUND = 0
PS_ENDCAP_SQUARE = 256
PS_ENDCAP_FLAT = 512
PS_ENDCAP_MASK = 3840
PS_JOIN_ROUND = 0
PS_JOIN_BEVEL = 4096
PS_JOIN_MITER = 8192
PS_JOIN_MASK = 61440
PS_TYPE_MASK = 983040
def _define_POINTFX_head():
    class POINTFX(Structure):
        pass
    return POINTFX
def _define_POINTFX():
    POINTFX = win32more.Graphics.Gdi.POINTFX_head
    POINTFX._fields_ = [
        ('x', win32more.Graphics.Gdi.FIXED),
        ('y', win32more.Graphics.Gdi.FIXED),
    ]
    return POINTFX
def _define_POLYTEXTA_head():
    class POLYTEXTA(Structure):
        pass
    return POLYTEXTA
def _define_POLYTEXTA():
    POLYTEXTA = win32more.Graphics.Gdi.POLYTEXTA_head
    POLYTEXTA._fields_ = [
        ('x', Int32),
        ('y', Int32),
        ('n', UInt32),
        ('lpstr', win32more.Foundation.PSTR),
        ('uiFlags', UInt32),
        ('rcl', win32more.Foundation.RECT),
        ('pdx', POINTER(Int32)),
    ]
    return POLYTEXTA
def _define_POLYTEXTW_head():
    class POLYTEXTW(Structure):
        pass
    return POLYTEXTW
def _define_POLYTEXTW():
    POLYTEXTW = win32more.Graphics.Gdi.POLYTEXTW_head
    POLYTEXTW._fields_ = [
        ('x', Int32),
        ('y', Int32),
        ('n', UInt32),
        ('lpstr', win32more.Foundation.PWSTR),
        ('uiFlags', UInt32),
        ('rcl', win32more.Foundation.RECT),
        ('pdx', POINTER(Int32)),
    ]
    return POLYTEXTW
R2_MODE = Int32
R2_BLACK = 1
R2_NOTMERGEPEN = 2
R2_MASKNOTPEN = 3
R2_NOTCOPYPEN = 4
R2_MASKPENNOT = 5
R2_NOT = 6
R2_XORPEN = 7
R2_NOTMASKPEN = 8
R2_MASKPEN = 9
R2_NOTXORPEN = 10
R2_NOP = 11
R2_MERGENOTPEN = 12
R2_COPYPEN = 13
R2_MERGEPENNOT = 14
R2_MERGEPEN = 15
R2_WHITE = 16
R2_LAST = 16
def _define_RASTERIZER_STATUS_head():
    class RASTERIZER_STATUS(Structure):
        pass
    return RASTERIZER_STATUS
def _define_RASTERIZER_STATUS():
    RASTERIZER_STATUS = win32more.Graphics.Gdi.RASTERIZER_STATUS_head
    RASTERIZER_STATUS._fields_ = [
        ('nSize', Int16),
        ('wFlags', Int16),
        ('nLanguageID', Int16),
    ]
    return RASTERIZER_STATUS
def _define_READEMBEDPROC():
    return CFUNCTYPE(UInt32,c_void_p,c_void_p,UInt32)
REDRAW_WINDOW_FLAGS = UInt32
RDW_INVALIDATE = 1
RDW_INTERNALPAINT = 2
RDW_ERASE = 4
RDW_VALIDATE = 8
RDW_NOINTERNALPAINT = 16
RDW_NOERASE = 32
RDW_NOCHILDREN = 64
RDW_ALLCHILDREN = 128
RDW_UPDATENOW = 256
RDW_ERASENOW = 512
RDW_FRAME = 1024
RDW_NOFRAME = 2048
def _define_RGBQUAD_head():
    class RGBQUAD(Structure):
        pass
    return RGBQUAD
def _define_RGBQUAD():
    RGBQUAD = win32more.Graphics.Gdi.RGBQUAD_head
    RGBQUAD._fields_ = [
        ('rgbBlue', Byte),
        ('rgbGreen', Byte),
        ('rgbRed', Byte),
        ('rgbReserved', Byte),
    ]
    return RGBQUAD
def _define_RGBTRIPLE_head():
    class RGBTRIPLE(Structure):
        pass
    return RGBTRIPLE
def _define_RGBTRIPLE():
    RGBTRIPLE = win32more.Graphics.Gdi.RGBTRIPLE_head
    RGBTRIPLE._fields_ = [
        ('rgbtBlue', Byte),
        ('rgbtGreen', Byte),
        ('rgbtRed', Byte),
    ]
    return RGBTRIPLE
RGN_COMBINE_MODE = Int32
RGN_AND = 1
RGN_OR = 2
RGN_XOR = 3
RGN_DIFF = 4
RGN_COPY = 5
RGN_MIN = 1
RGN_MAX = 5
def _define_RGNDATA_head():
    class RGNDATA(Structure):
        pass
    return RGNDATA
def _define_RGNDATA():
    RGNDATA = win32more.Graphics.Gdi.RGNDATA_head
    RGNDATA._fields_ = [
        ('rdh', win32more.Graphics.Gdi.RGNDATAHEADER),
        ('Buffer', win32more.Foundation.CHAR * 1),
    ]
    return RGNDATA
def _define_RGNDATAHEADER_head():
    class RGNDATAHEADER(Structure):
        pass
    return RGNDATAHEADER
def _define_RGNDATAHEADER():
    RGNDATAHEADER = win32more.Graphics.Gdi.RGNDATAHEADER_head
    RGNDATAHEADER._fields_ = [
        ('dwSize', UInt32),
        ('iType', UInt32),
        ('nCount', UInt32),
        ('nRgnSize', UInt32),
        ('rcBound', win32more.Foundation.RECT),
    ]
    return RGNDATAHEADER
ROP_CODE = UInt32
BLACKNESS = 66
NOTSRCERASE = 1114278
NOTSRCCOPY = 3342344
SRCERASE = 4457256
DSTINVERT = 5570569
PATINVERT = 5898313
SRCINVERT = 6684742
SRCAND = 8913094
MERGEPAINT = 12255782
MERGECOPY = 12583114
SRCCOPY = 13369376
SRCPAINT = 15597702
PATCOPY = 15728673
PATPAINT = 16452105
WHITENESS = 16711778
CAPTUREBLT = 1073741824
NOMIRRORBITMAP = 2147483648
SET_BOUNDS_RECT_FLAGS = UInt32
DCB_ACCUMULATE = 2
DCB_DISABLE = 8
DCB_ENABLE = 4
DCB_RESET = 1
STRETCH_BLT_MODE = UInt32
BLACKONWHITE = 1
COLORONCOLOR = 3
HALFTONE = 4
STRETCH_ANDSCANS = 1
STRETCH_DELETESCANS = 3
STRETCH_HALFTONE = 4
STRETCH_ORSCANS = 2
WHITEONBLACK = 2
SYS_COLOR_INDEX = Int32
COLOR_SCROLLBAR = 0
COLOR_BACKGROUND = 1
COLOR_ACTIVECAPTION = 2
COLOR_INACTIVECAPTION = 3
COLOR_MENU = 4
COLOR_WINDOW = 5
COLOR_WINDOWFRAME = 6
COLOR_MENUTEXT = 7
COLOR_WINDOWTEXT = 8
COLOR_CAPTIONTEXT = 9
COLOR_ACTIVEBORDER = 10
COLOR_INACTIVEBORDER = 11
COLOR_APPWORKSPACE = 12
COLOR_HIGHLIGHT = 13
COLOR_HIGHLIGHTTEXT = 14
COLOR_BTNFACE = 15
COLOR_BTNSHADOW = 16
COLOR_GRAYTEXT = 17
COLOR_BTNTEXT = 18
COLOR_INACTIVECAPTIONTEXT = 19
COLOR_BTNHIGHLIGHT = 20
COLOR_3DDKSHADOW = 21
COLOR_3DLIGHT = 22
COLOR_INFOTEXT = 23
COLOR_INFOBK = 24
COLOR_HOTLIGHT = 26
COLOR_GRADIENTACTIVECAPTION = 27
COLOR_GRADIENTINACTIVECAPTION = 28
COLOR_MENUHILIGHT = 29
COLOR_MENUBAR = 30
COLOR_DESKTOP = 1
COLOR_3DFACE = 15
COLOR_3DSHADOW = 16
COLOR_3DHIGHLIGHT = 20
COLOR_3DHILIGHT = 20
COLOR_BTNHILIGHT = 20
SYSTEM_PALETTE_USE = UInt32
SYSPAL_NOSTATIC = 2
SYSPAL_NOSTATIC256 = 3
SYSPAL_STATIC = 1
TEXT_ALIGN_OPTIONS = UInt32
TA_NOUPDATECP = 0
TA_UPDATECP = 1
TA_LEFT = 0
TA_RIGHT = 2
TA_CENTER = 6
TA_TOP = 0
TA_BOTTOM = 8
TA_BASELINE = 24
TA_RTLREADING = 256
TA_MASK = 287
VTA_BASELINE = 24
VTA_LEFT = 8
VTA_RIGHT = 0
VTA_CENTER = 6
VTA_BOTTOM = 2
VTA_TOP = 0
def _define_TEXTMETRICA_head():
    class TEXTMETRICA(Structure):
        pass
    return TEXTMETRICA
def _define_TEXTMETRICA():
    TEXTMETRICA = win32more.Graphics.Gdi.TEXTMETRICA_head
    TEXTMETRICA._fields_ = [
        ('tmHeight', Int32),
        ('tmAscent', Int32),
        ('tmDescent', Int32),
        ('tmInternalLeading', Int32),
        ('tmExternalLeading', Int32),
        ('tmAveCharWidth', Int32),
        ('tmMaxCharWidth', Int32),
        ('tmWeight', Int32),
        ('tmOverhang', Int32),
        ('tmDigitizedAspectX', Int32),
        ('tmDigitizedAspectY', Int32),
        ('tmFirstChar', Byte),
        ('tmLastChar', Byte),
        ('tmDefaultChar', Byte),
        ('tmBreakChar', Byte),
        ('tmItalic', Byte),
        ('tmUnderlined', Byte),
        ('tmStruckOut', Byte),
        ('tmPitchAndFamily', win32more.Graphics.Gdi.TMPF_FLAGS),
        ('tmCharSet', Byte),
    ]
    return TEXTMETRICA
def _define_TEXTMETRICW_head():
    class TEXTMETRICW(Structure):
        pass
    return TEXTMETRICW
def _define_TEXTMETRICW():
    TEXTMETRICW = win32more.Graphics.Gdi.TEXTMETRICW_head
    TEXTMETRICW._fields_ = [
        ('tmHeight', Int32),
        ('tmAscent', Int32),
        ('tmDescent', Int32),
        ('tmInternalLeading', Int32),
        ('tmExternalLeading', Int32),
        ('tmAveCharWidth', Int32),
        ('tmMaxCharWidth', Int32),
        ('tmWeight', Int32),
        ('tmOverhang', Int32),
        ('tmDigitizedAspectX', Int32),
        ('tmDigitizedAspectY', Int32),
        ('tmFirstChar', Char),
        ('tmLastChar', Char),
        ('tmDefaultChar', Char),
        ('tmBreakChar', Char),
        ('tmItalic', Byte),
        ('tmUnderlined', Byte),
        ('tmStruckOut', Byte),
        ('tmPitchAndFamily', win32more.Graphics.Gdi.TMPF_FLAGS),
        ('tmCharSet', Byte),
    ]
    return TEXTMETRICW
TMPF_FLAGS = Byte
TMPF_FIXED_PITCH = 1
TMPF_VECTOR = 2
TMPF_DEVICE = 8
TMPF_TRUETYPE = 4
def _define_TRIVERTEX_head():
    class TRIVERTEX(Structure):
        pass
    return TRIVERTEX
def _define_TRIVERTEX():
    TRIVERTEX = win32more.Graphics.Gdi.TRIVERTEX_head
    TRIVERTEX._fields_ = [
        ('x', Int32),
        ('y', Int32),
        ('Red', UInt16),
        ('Green', UInt16),
        ('Blue', UInt16),
        ('Alpha', UInt16),
    ]
    return TRIVERTEX
TTEMBED_FLAGS = UInt32
TTEMBED_EMBEDEUDC = 32
TTEMBED_RAW = 0
TTEMBED_SUBSET = 1
TTEMBED_TTCOMPRESSED = 4
def _define_TTEMBEDINFO_head():
    class TTEMBEDINFO(Structure):
        pass
    return TTEMBEDINFO
def _define_TTEMBEDINFO():
    TTEMBEDINFO = win32more.Graphics.Gdi.TTEMBEDINFO_head
    TTEMBEDINFO._fields_ = [
        ('usStructSize', UInt16),
        ('usRootStrSize', UInt16),
        ('pusRootStr', POINTER(UInt16)),
    ]
    return TTEMBEDINFO
TTLOAD_EMBEDDED_FONT_STATUS = UInt32
TTLOAD_FONT_SUBSETTED = 1
TTLOAD_FONT_IN_SYSSTARTUP = 2
def _define_TTLOADINFO_head():
    class TTLOADINFO(Structure):
        pass
    return TTLOADINFO
def _define_TTLOADINFO():
    TTLOADINFO = win32more.Graphics.Gdi.TTLOADINFO_head
    TTLOADINFO._fields_ = [
        ('usStructSize', UInt16),
        ('usRefStrSize', UInt16),
        ('pusRefStr', POINTER(UInt16)),
    ]
    return TTLOADINFO
def _define_TTPOLYCURVE_head():
    class TTPOLYCURVE(Structure):
        pass
    return TTPOLYCURVE
def _define_TTPOLYCURVE():
    TTPOLYCURVE = win32more.Graphics.Gdi.TTPOLYCURVE_head
    TTPOLYCURVE._fields_ = [
        ('wType', UInt16),
        ('cpfx', UInt16),
        ('apfx', win32more.Graphics.Gdi.POINTFX * 1),
    ]
    return TTPOLYCURVE
def _define_TTPOLYGONHEADER_head():
    class TTPOLYGONHEADER(Structure):
        pass
    return TTPOLYGONHEADER
def _define_TTPOLYGONHEADER():
    TTPOLYGONHEADER = win32more.Graphics.Gdi.TTPOLYGONHEADER_head
    TTPOLYGONHEADER._fields_ = [
        ('cb', UInt32),
        ('dwType', UInt32),
        ('pfxStart', win32more.Graphics.Gdi.POINTFX),
    ]
    return TTPOLYGONHEADER
def _define_TTVALIDATIONTESTSPARAMS_head():
    class TTVALIDATIONTESTSPARAMS(Structure):
        pass
    return TTVALIDATIONTESTSPARAMS
def _define_TTVALIDATIONTESTSPARAMS():
    TTVALIDATIONTESTSPARAMS = win32more.Graphics.Gdi.TTVALIDATIONTESTSPARAMS_head
    TTVALIDATIONTESTSPARAMS._fields_ = [
        ('ulStructSize', UInt32),
        ('lTestFromSize', Int32),
        ('lTestToSize', Int32),
        ('ulCharSet', UInt32),
        ('usReserved1', UInt16),
        ('usCharCodeCount', UInt16),
        ('pusCharCodeSet', POINTER(UInt16)),
    ]
    return TTVALIDATIONTESTSPARAMS
def _define_TTVALIDATIONTESTSPARAMSEX_head():
    class TTVALIDATIONTESTSPARAMSEX(Structure):
        pass
    return TTVALIDATIONTESTSPARAMSEX
def _define_TTVALIDATIONTESTSPARAMSEX():
    TTVALIDATIONTESTSPARAMSEX = win32more.Graphics.Gdi.TTVALIDATIONTESTSPARAMSEX_head
    TTVALIDATIONTESTSPARAMSEX._fields_ = [
        ('ulStructSize', UInt32),
        ('lTestFromSize', Int32),
        ('lTestToSize', Int32),
        ('ulCharSet', UInt32),
        ('usReserved1', UInt16),
        ('usCharCodeCount', UInt16),
        ('pulCharCodeSet', POINTER(UInt32)),
    ]
    return TTVALIDATIONTESTSPARAMSEX
def _define_WCRANGE_head():
    class WCRANGE(Structure):
        pass
    return WCRANGE
def _define_WCRANGE():
    WCRANGE = win32more.Graphics.Gdi.WCRANGE_head
    WCRANGE._fields_ = [
        ('wcLow', Char),
        ('cGlyphs', UInt16),
    ]
    return WCRANGE
def _define_WGLSWAP_head():
    class WGLSWAP(Structure):
        pass
    return WGLSWAP
def _define_WGLSWAP():
    WGLSWAP = win32more.Graphics.Gdi.WGLSWAP_head
    WGLSWAP._fields_ = [
        ('hdc', win32more.Graphics.Gdi.HDC),
        ('uiFlags', UInt32),
    ]
    return WGLSWAP
def _define_WRITEEMBEDPROC():
    return CFUNCTYPE(UInt32,c_void_p,c_void_p,UInt32)
def _define_XFORM_head():
    class XFORM(Structure):
        pass
    return XFORM
def _define_XFORM():
    XFORM = win32more.Graphics.Gdi.XFORM_head
    XFORM._fields_ = [
        ('eM11', Single),
        ('eM12', Single),
        ('eM21', Single),
        ('eM22', Single),
        ('eDx', Single),
        ('eDy', Single),
    ]
    return XFORM
__all__ = [
    "ABC",
    "ABCFLOAT",
    "ABORTDOC",
    "ABORTPATH",
    "ABSOLUTE",
    "AC_SRC_ALPHA",
    "AC_SRC_OVER",
    "AD_CLOCKWISE",
    "AD_COUNTERCLOCKWISE",
    "ALTERNATE",
    "ANSI_CHARSET",
    "ANSI_FIXED_FONT",
    "ANSI_VAR_FONT",
    "ANTIALIASED_QUALITY",
    "ARABIC_CHARSET",
    "ARC_DIRECTION",
    "ASPECTX",
    "ASPECTXY",
    "ASPECTY",
    "ASPECT_FILTERING",
    "AXESLISTA",
    "AXESLISTW",
    "AXISINFOA",
    "AXISINFOW",
    "AbortPath",
    "AddFontMemResourceEx",
    "AddFontResourceA",
    "AddFontResourceExA",
    "AddFontResourceExW",
    "AddFontResourceW",
    "AlphaBlend",
    "AngleArc",
    "AnimatePalette",
    "Arc",
    "ArcTo",
    "BACKGROUND_MODE",
    "BALTIC_CHARSET",
    "BANDINFO",
    "BDR_INNER",
    "BDR_OUTER",
    "BDR_RAISED",
    "BDR_RAISEDINNER",
    "BDR_RAISEDOUTER",
    "BDR_SUNKEN",
    "BDR_SUNKENINNER",
    "BDR_SUNKENOUTER",
    "BEGIN_PATH",
    "BF_ADJUST",
    "BF_BOTTOM",
    "BF_BOTTOMLEFT",
    "BF_BOTTOMRIGHT",
    "BF_DIAGONAL",
    "BF_DIAGONAL_ENDBOTTOMLEFT",
    "BF_DIAGONAL_ENDBOTTOMRIGHT",
    "BF_DIAGONAL_ENDTOPLEFT",
    "BF_DIAGONAL_ENDTOPRIGHT",
    "BF_FLAT",
    "BF_LEFT",
    "BF_MIDDLE",
    "BF_MONO",
    "BF_RECT",
    "BF_RIGHT",
    "BF_SOFT",
    "BF_TOP",
    "BF_TOPLEFT",
    "BF_TOPRIGHT",
    "BITMAP",
    "BITMAPCOREHEADER",
    "BITMAPCOREINFO",
    "BITMAPFILEHEADER",
    "BITMAPINFO",
    "BITMAPINFOHEADER",
    "BITMAPV4HEADER",
    "BITMAPV5HEADER",
    "BITSPIXEL",
    "BI_BITFIELDS",
    "BI_COMPRESSION",
    "BI_JPEG",
    "BI_PNG",
    "BI_RGB",
    "BI_RLE4",
    "BI_RLE8",
    "BKMODE_LAST",
    "BLACKNESS",
    "BLACKONWHITE",
    "BLACK_BRUSH",
    "BLACK_PEN",
    "BLENDFUNCTION",
    "BLTALIGNMENT",
    "BRUSH_STYLE",
    "BS_DIBPATTERN",
    "BS_DIBPATTERN8X8",
    "BS_DIBPATTERNPT",
    "BS_HATCHED",
    "BS_HOLLOW",
    "BS_INDEXED",
    "BS_MONOPATTERN",
    "BS_NULL",
    "BS_PATTERN",
    "BS_PATTERN8X8",
    "BS_SOLID",
    "BeginPaint",
    "BeginPath",
    "BitBlt",
    "CAPTUREBLT",
    "CA_LOG_FILTER",
    "CA_NEGATIVE",
    "CBM_INIT",
    "CCHFORMNAME",
    "CC_CHORD",
    "CC_CIRCLES",
    "CC_ELLIPSES",
    "CC_INTERIORS",
    "CC_NONE",
    "CC_PIE",
    "CC_ROUNDRECT",
    "CC_STYLED",
    "CC_WIDE",
    "CC_WIDESTYLED",
    "CDS_DISABLE_UNSAFE_MODES",
    "CDS_ENABLE_UNSAFE_MODES",
    "CDS_FULLSCREEN",
    "CDS_GLOBAL",
    "CDS_NORESET",
    "CDS_RESET",
    "CDS_RESET_EX",
    "CDS_SET_PRIMARY",
    "CDS_TEST",
    "CDS_TYPE",
    "CDS_UPDATEREGISTRY",
    "CDS_VIDEOPARAMETERS",
    "CFP_ALLOCPROC",
    "CFP_FREEPROC",
    "CFP_REALLOCPROC",
    "CHARSET_DEFAULT",
    "CHARSET_GLYPHIDX",
    "CHARSET_SYMBOL",
    "CHARSET_UNICODE",
    "CHECKJPEGFORMAT",
    "CHECKPNGFORMAT",
    "CHINESEBIG5_CHARSET",
    "CIEXYZ",
    "CIEXYZTRIPLE",
    "CLEARTYPE_NATURAL_QUALITY",
    "CLEARTYPE_QUALITY",
    "CLIPCAPS",
    "CLIP_CHARACTER_PRECIS",
    "CLIP_DEFAULT_PRECIS",
    "CLIP_DFA_DISABLE",
    "CLIP_DFA_OVERRIDE",
    "CLIP_EMBEDDED",
    "CLIP_LH_ANGLES",
    "CLIP_MASK",
    "CLIP_STROKE_PRECIS",
    "CLIP_TO_PATH",
    "CLIP_TT_ALWAYS",
    "CLOSECHANNEL",
    "CLR_INVALID",
    "CM_CMYK_COLOR",
    "CM_DEVICE_ICM",
    "CM_GAMMA_RAMP",
    "CM_IN_GAMUT",
    "CM_NONE",
    "CM_OUT_OF_GAMUT",
    "COLORADJUSTMENT",
    "COLORMATCHTOTARGET_EMBEDED",
    "COLORMGMTCAPS",
    "COLORONCOLOR",
    "COLORRES",
    "COLOR_3DDKSHADOW",
    "COLOR_3DFACE",
    "COLOR_3DHIGHLIGHT",
    "COLOR_3DHILIGHT",
    "COLOR_3DLIGHT",
    "COLOR_3DSHADOW",
    "COLOR_ACTIVEBORDER",
    "COLOR_ACTIVECAPTION",
    "COLOR_APPWORKSPACE",
    "COLOR_BACKGROUND",
    "COLOR_BTNFACE",
    "COLOR_BTNHIGHLIGHT",
    "COLOR_BTNHILIGHT",
    "COLOR_BTNSHADOW",
    "COLOR_BTNTEXT",
    "COLOR_CAPTIONTEXT",
    "COLOR_DESKTOP",
    "COLOR_GRADIENTACTIVECAPTION",
    "COLOR_GRADIENTINACTIVECAPTION",
    "COLOR_GRAYTEXT",
    "COLOR_HIGHLIGHT",
    "COLOR_HIGHLIGHTTEXT",
    "COLOR_HOTLIGHT",
    "COLOR_INACTIVEBORDER",
    "COLOR_INACTIVECAPTION",
    "COLOR_INACTIVECAPTIONTEXT",
    "COLOR_INFOBK",
    "COLOR_INFOTEXT",
    "COLOR_MENU",
    "COLOR_MENUBAR",
    "COLOR_MENUHILIGHT",
    "COLOR_MENUTEXT",
    "COLOR_SCROLLBAR",
    "COLOR_WINDOW",
    "COLOR_WINDOWFRAME",
    "COLOR_WINDOWTEXT",
    "COMPLEXREGION",
    "CP_NONE",
    "CP_RECTANGLE",
    "CP_REGION",
    "CREATECOLORSPACE_EMBEDED",
    "CREATE_FONT_PACKAGE_SUBSET_ENCODING",
    "CREATE_FONT_PACKAGE_SUBSET_PLATFORM",
    "CREATE_POLYGON_RGN_MODE",
    "CURVECAPS",
    "CancelDC",
    "ChangeDisplaySettingsA",
    "ChangeDisplaySettingsExA",
    "ChangeDisplaySettingsExW",
    "ChangeDisplaySettingsW",
    "Chord",
    "ClientToScreen",
    "CloseEnhMetaFile",
    "CloseFigure",
    "CloseMetaFile",
    "CombineRgn",
    "CombineTransform",
    "CopyEnhMetaFileA",
    "CopyEnhMetaFileW",
    "CopyMetaFileA",
    "CopyMetaFileW",
    "CopyRect",
    "CreateBitmap",
    "CreateBitmapIndirect",
    "CreateBrushIndirect",
    "CreateCompatibleBitmap",
    "CreateCompatibleDC",
    "CreateDCA",
    "CreateDCW",
    "CreateDIBPatternBrush",
    "CreateDIBPatternBrushPt",
    "CreateDIBSection",
    "CreateDIBitmap",
    "CreateDiscardableBitmap",
    "CreateEllipticRgn",
    "CreateEllipticRgnIndirect",
    "CreateEnhMetaFileA",
    "CreateEnhMetaFileW",
    "CreateFontA",
    "CreateFontIndirectA",
    "CreateFontIndirectExA",
    "CreateFontIndirectExW",
    "CreateFontIndirectW",
    "CreateFontPackage",
    "CreateFontW",
    "CreateHalftonePalette",
    "CreateHatchBrush",
    "CreateICA",
    "CreateICW",
    "CreateMetaFileA",
    "CreateMetaFileW",
    "CreatePalette",
    "CreatePatternBrush",
    "CreatePen",
    "CreatePenIndirect",
    "CreatePolyPolygonRgn",
    "CreatePolygonRgn",
    "CreateRectRgn",
    "CreateRectRgnIndirect",
    "CreateRoundRectRgn",
    "CreateScalableFontResourceA",
    "CreateScalableFontResourceW",
    "CreateSolidBrush",
    "CreatedHDC",
    "DCBA_FACEDOWNCENTER",
    "DCBA_FACEDOWNLEFT",
    "DCBA_FACEDOWNNONE",
    "DCBA_FACEDOWNRIGHT",
    "DCBA_FACEUPCENTER",
    "DCBA_FACEUPLEFT",
    "DCBA_FACEUPNONE",
    "DCBA_FACEUPRIGHT",
    "DCB_ACCUMULATE",
    "DCB_DISABLE",
    "DCB_ENABLE",
    "DCB_RESET",
    "DCTT_BITMAP",
    "DCTT_DOWNLOAD",
    "DCTT_DOWNLOAD_OUTLINE",
    "DCTT_SUBDEV",
    "DCX_CACHE",
    "DCX_CLIPCHILDREN",
    "DCX_CLIPSIBLINGS",
    "DCX_EXCLUDERGN",
    "DCX_INTERSECTRGN",
    "DCX_INTERSECTUPDATE",
    "DCX_LOCKWINDOWUPDATE",
    "DCX_NORESETATTRS",
    "DCX_PARENTCLIP",
    "DCX_VALIDATE",
    "DCX_WINDOW",
    "DC_ACTIVE",
    "DC_BINADJUST",
    "DC_BRUSH",
    "DC_BUTTONS",
    "DC_DATATYPE_PRODUCED",
    "DC_EMF_COMPLIANT",
    "DC_GRADIENT",
    "DC_ICON",
    "DC_INBUTTON",
    "DC_LAYOUT",
    "DC_MANUFACTURER",
    "DC_MODEL",
    "DC_PEN",
    "DC_SMALLCAP",
    "DC_TEXT",
    "DEFAULT_CHARSET",
    "DEFAULT_GUI_FONT",
    "DEFAULT_PALETTE",
    "DEFAULT_PITCH",
    "DEFAULT_QUALITY",
    "DESIGNVECTOR",
    "DESKTOPHORZRES",
    "DESKTOPVERTRES",
    "DEVICEDATA",
    "DEVICE_DEFAULT_FONT",
    "DEVICE_FONTTYPE",
    "DEVMODEA",
    "DEVMODEW",
    "DEVMODE_COLLATE",
    "DEVMODE_COLOR",
    "DEVMODE_DISPLAY_FIXED_OUTPUT",
    "DEVMODE_DISPLAY_ORIENTATION",
    "DEVMODE_DUPLEX",
    "DEVMODE_FIELD_FLAGS",
    "DEVMODE_TRUETYPE_OPTION",
    "DFCS_ADJUSTRECT",
    "DFCS_BUTTON3STATE",
    "DFCS_BUTTONCHECK",
    "DFCS_BUTTONPUSH",
    "DFCS_BUTTONRADIO",
    "DFCS_BUTTONRADIOIMAGE",
    "DFCS_BUTTONRADIOMASK",
    "DFCS_CAPTIONCLOSE",
    "DFCS_CAPTIONHELP",
    "DFCS_CAPTIONMAX",
    "DFCS_CAPTIONMIN",
    "DFCS_CAPTIONRESTORE",
    "DFCS_CHECKED",
    "DFCS_FLAT",
    "DFCS_HOT",
    "DFCS_INACTIVE",
    "DFCS_MENUARROW",
    "DFCS_MENUARROWRIGHT",
    "DFCS_MENUBULLET",
    "DFCS_MENUCHECK",
    "DFCS_MONO",
    "DFCS_PUSHED",
    "DFCS_SCROLLCOMBOBOX",
    "DFCS_SCROLLDOWN",
    "DFCS_SCROLLLEFT",
    "DFCS_SCROLLRIGHT",
    "DFCS_SCROLLSIZEGRIP",
    "DFCS_SCROLLSIZEGRIPRIGHT",
    "DFCS_SCROLLUP",
    "DFCS_STATE",
    "DFCS_TRANSPARENT",
    "DFC_BUTTON",
    "DFC_CAPTION",
    "DFC_MENU",
    "DFC_POPUPMENU",
    "DFC_SCROLL",
    "DFC_TYPE",
    "DIBSECTION",
    "DIB_PAL_COLORS",
    "DIB_RGB_COLORS",
    "DIB_USAGE",
    "DISPLAYCONFIG_COLOR_ENCODING",
    "DISPLAYCONFIG_COLOR_ENCODING_FORCE_UINT32",
    "DISPLAYCONFIG_COLOR_ENCODING_INTENSITY",
    "DISPLAYCONFIG_COLOR_ENCODING_RGB",
    "DISPLAYCONFIG_COLOR_ENCODING_YCBCR420",
    "DISPLAYCONFIG_COLOR_ENCODING_YCBCR422",
    "DISPLAYCONFIG_COLOR_ENCODING_YCBCR444",
    "DISPLAYCONFIG_MAXPATH",
    "DISPLAYCONFIG_PATH_ACTIVE",
    "DISPLAYCONFIG_PATH_CLONE_GROUP_INVALID",
    "DISPLAYCONFIG_PATH_DESKTOP_IMAGE_IDX_INVALID",
    "DISPLAYCONFIG_PATH_MODE_IDX_INVALID",
    "DISPLAYCONFIG_PATH_PREFERRED_UNSCALED",
    "DISPLAYCONFIG_PATH_SOURCE_MODE_IDX_INVALID",
    "DISPLAYCONFIG_PATH_SUPPORT_VIRTUAL_MODE",
    "DISPLAYCONFIG_PATH_TARGET_MODE_IDX_INVALID",
    "DISPLAYCONFIG_PATH_VALID_FLAGS",
    "DISPLAYCONFIG_SOURCE_IN_USE",
    "DISPLAYCONFIG_TARGET_FORCED_AVAILABILITY_BOOT",
    "DISPLAYCONFIG_TARGET_FORCED_AVAILABILITY_PATH",
    "DISPLAYCONFIG_TARGET_FORCED_AVAILABILITY_SYSTEM",
    "DISPLAYCONFIG_TARGET_FORCIBLE",
    "DISPLAYCONFIG_TARGET_IN_USE",
    "DISPLAYCONFIG_TARGET_IS_HMD",
    "DISPLAY_DEVICEA",
    "DISPLAY_DEVICEW",
    "DISPLAY_DEVICE_ACC_DRIVER",
    "DISPLAY_DEVICE_ACTIVE",
    "DISPLAY_DEVICE_ATTACHED",
    "DISPLAY_DEVICE_ATTACHED_TO_DESKTOP",
    "DISPLAY_DEVICE_DISCONNECT",
    "DISPLAY_DEVICE_MIRRORING_DRIVER",
    "DISPLAY_DEVICE_MODESPRUNED",
    "DISPLAY_DEVICE_MULTI_DRIVER",
    "DISPLAY_DEVICE_PRIMARY_DEVICE",
    "DISPLAY_DEVICE_RDPUDD",
    "DISPLAY_DEVICE_REMOTE",
    "DISPLAY_DEVICE_REMOVABLE",
    "DISPLAY_DEVICE_TS_COMPATIBLE",
    "DISPLAY_DEVICE_UNSAFE_MODES_ON",
    "DISPLAY_DEVICE_VGA_COMPATIBLE",
    "DISP_CHANGE",
    "DISP_CHANGE_BADDUALVIEW",
    "DISP_CHANGE_BADFLAGS",
    "DISP_CHANGE_BADMODE",
    "DISP_CHANGE_BADPARAM",
    "DISP_CHANGE_FAILED",
    "DISP_CHANGE_NOTUPDATED",
    "DISP_CHANGE_RESTART",
    "DISP_CHANGE_SUCCESSFUL",
    "DI_APPBANDING",
    "DI_ROPS_READ_DESTINATION",
    "DKGRAY_BRUSH",
    "DMBIN_AUTO",
    "DMBIN_CASSETTE",
    "DMBIN_ENVELOPE",
    "DMBIN_ENVMANUAL",
    "DMBIN_FORMSOURCE",
    "DMBIN_LARGECAPACITY",
    "DMBIN_LARGEFMT",
    "DMBIN_LAST",
    "DMBIN_LOWER",
    "DMBIN_MANUAL",
    "DMBIN_MIDDLE",
    "DMBIN_ONLYONE",
    "DMBIN_SMALLFMT",
    "DMBIN_TRACTOR",
    "DMBIN_UPPER",
    "DMBIN_USER",
    "DMCOLLATE_FALSE",
    "DMCOLLATE_TRUE",
    "DMCOLOR_COLOR",
    "DMCOLOR_MONOCHROME",
    "DMDFO_CENTER",
    "DMDFO_DEFAULT",
    "DMDFO_STRETCH",
    "DMDISPLAYFLAGS_TEXTMODE",
    "DMDITHER_COARSE",
    "DMDITHER_ERRORDIFFUSION",
    "DMDITHER_FINE",
    "DMDITHER_GRAYSCALE",
    "DMDITHER_LINEART",
    "DMDITHER_NONE",
    "DMDITHER_RESERVED6",
    "DMDITHER_RESERVED7",
    "DMDITHER_RESERVED8",
    "DMDITHER_RESERVED9",
    "DMDITHER_USER",
    "DMDO_180",
    "DMDO_270",
    "DMDO_90",
    "DMDO_DEFAULT",
    "DMDUP_HORIZONTAL",
    "DMDUP_SIMPLEX",
    "DMDUP_VERTICAL",
    "DMICMMETHOD_DEVICE",
    "DMICMMETHOD_DRIVER",
    "DMICMMETHOD_NONE",
    "DMICMMETHOD_SYSTEM",
    "DMICMMETHOD_USER",
    "DMICM_ABS_COLORIMETRIC",
    "DMICM_COLORIMETRIC",
    "DMICM_CONTRAST",
    "DMICM_SATURATE",
    "DMICM_USER",
    "DMMEDIA_GLOSSY",
    "DMMEDIA_STANDARD",
    "DMMEDIA_TRANSPARENCY",
    "DMMEDIA_USER",
    "DMNUP_ONEUP",
    "DMNUP_SYSTEM",
    "DMORIENT_LANDSCAPE",
    "DMORIENT_PORTRAIT",
    "DMPAPER_10X11",
    "DMPAPER_10X14",
    "DMPAPER_11X17",
    "DMPAPER_12X11",
    "DMPAPER_15X11",
    "DMPAPER_9X11",
    "DMPAPER_A2",
    "DMPAPER_A3",
    "DMPAPER_A3_EXTRA",
    "DMPAPER_A3_EXTRA_TRANSVERSE",
    "DMPAPER_A3_ROTATED",
    "DMPAPER_A3_TRANSVERSE",
    "DMPAPER_A4",
    "DMPAPER_A4SMALL",
    "DMPAPER_A4_EXTRA",
    "DMPAPER_A4_PLUS",
    "DMPAPER_A4_ROTATED",
    "DMPAPER_A4_TRANSVERSE",
    "DMPAPER_A5",
    "DMPAPER_A5_EXTRA",
    "DMPAPER_A5_ROTATED",
    "DMPAPER_A5_TRANSVERSE",
    "DMPAPER_A6",
    "DMPAPER_A6_ROTATED",
    "DMPAPER_A_PLUS",
    "DMPAPER_B4",
    "DMPAPER_B4_JIS_ROTATED",
    "DMPAPER_B5",
    "DMPAPER_B5_EXTRA",
    "DMPAPER_B5_JIS_ROTATED",
    "DMPAPER_B5_TRANSVERSE",
    "DMPAPER_B6_JIS",
    "DMPAPER_B6_JIS_ROTATED",
    "DMPAPER_B_PLUS",
    "DMPAPER_CSHEET",
    "DMPAPER_DBL_JAPANESE_POSTCARD",
    "DMPAPER_DBL_JAPANESE_POSTCARD_ROTATED",
    "DMPAPER_DSHEET",
    "DMPAPER_ENV_10",
    "DMPAPER_ENV_11",
    "DMPAPER_ENV_12",
    "DMPAPER_ENV_14",
    "DMPAPER_ENV_9",
    "DMPAPER_ENV_B4",
    "DMPAPER_ENV_B5",
    "DMPAPER_ENV_B6",
    "DMPAPER_ENV_C3",
    "DMPAPER_ENV_C4",
    "DMPAPER_ENV_C5",
    "DMPAPER_ENV_C6",
    "DMPAPER_ENV_C65",
    "DMPAPER_ENV_DL",
    "DMPAPER_ENV_INVITE",
    "DMPAPER_ENV_ITALY",
    "DMPAPER_ENV_MONARCH",
    "DMPAPER_ENV_PERSONAL",
    "DMPAPER_ESHEET",
    "DMPAPER_EXECUTIVE",
    "DMPAPER_FANFOLD_LGL_GERMAN",
    "DMPAPER_FANFOLD_STD_GERMAN",
    "DMPAPER_FANFOLD_US",
    "DMPAPER_FOLIO",
    "DMPAPER_ISO_B4",
    "DMPAPER_JAPANESE_POSTCARD",
    "DMPAPER_JAPANESE_POSTCARD_ROTATED",
    "DMPAPER_JENV_CHOU3",
    "DMPAPER_JENV_CHOU3_ROTATED",
    "DMPAPER_JENV_CHOU4",
    "DMPAPER_JENV_CHOU4_ROTATED",
    "DMPAPER_JENV_KAKU2",
    "DMPAPER_JENV_KAKU2_ROTATED",
    "DMPAPER_JENV_KAKU3",
    "DMPAPER_JENV_KAKU3_ROTATED",
    "DMPAPER_JENV_YOU4",
    "DMPAPER_JENV_YOU4_ROTATED",
    "DMPAPER_LAST",
    "DMPAPER_LEDGER",
    "DMPAPER_LEGAL",
    "DMPAPER_LEGAL_EXTRA",
    "DMPAPER_LETTER",
    "DMPAPER_LETTERSMALL",
    "DMPAPER_LETTER_EXTRA",
    "DMPAPER_LETTER_EXTRA_TRANSVERSE",
    "DMPAPER_LETTER_PLUS",
    "DMPAPER_LETTER_ROTATED",
    "DMPAPER_LETTER_TRANSVERSE",
    "DMPAPER_NOTE",
    "DMPAPER_P16K",
    "DMPAPER_P16K_ROTATED",
    "DMPAPER_P32K",
    "DMPAPER_P32KBIG",
    "DMPAPER_P32KBIG_ROTATED",
    "DMPAPER_P32K_ROTATED",
    "DMPAPER_PENV_1",
    "DMPAPER_PENV_10",
    "DMPAPER_PENV_10_ROTATED",
    "DMPAPER_PENV_1_ROTATED",
    "DMPAPER_PENV_2",
    "DMPAPER_PENV_2_ROTATED",
    "DMPAPER_PENV_3",
    "DMPAPER_PENV_3_ROTATED",
    "DMPAPER_PENV_4",
    "DMPAPER_PENV_4_ROTATED",
    "DMPAPER_PENV_5",
    "DMPAPER_PENV_5_ROTATED",
    "DMPAPER_PENV_6",
    "DMPAPER_PENV_6_ROTATED",
    "DMPAPER_PENV_7",
    "DMPAPER_PENV_7_ROTATED",
    "DMPAPER_PENV_8",
    "DMPAPER_PENV_8_ROTATED",
    "DMPAPER_PENV_9",
    "DMPAPER_PENV_9_ROTATED",
    "DMPAPER_QUARTO",
    "DMPAPER_RESERVED_48",
    "DMPAPER_RESERVED_49",
    "DMPAPER_STATEMENT",
    "DMPAPER_TABLOID",
    "DMPAPER_TABLOID_EXTRA",
    "DMPAPER_USER",
    "DMRES_DRAFT",
    "DMRES_HIGH",
    "DMRES_LOW",
    "DMRES_MEDIUM",
    "DMTT_BITMAP",
    "DMTT_DOWNLOAD",
    "DMTT_DOWNLOAD_OUTLINE",
    "DMTT_SUBDEV",
    "DM_BITSPERPEL",
    "DM_COLLATE",
    "DM_COLOR",
    "DM_COPIES",
    "DM_COPY",
    "DM_DEFAULTSOURCE",
    "DM_DISPLAYFIXEDOUTPUT",
    "DM_DISPLAYFLAGS",
    "DM_DISPLAYFREQUENCY",
    "DM_DISPLAYORIENTATION",
    "DM_DITHERTYPE",
    "DM_DUPLEX",
    "DM_FORMNAME",
    "DM_ICMINTENT",
    "DM_ICMMETHOD",
    "DM_INTERLACED",
    "DM_IN_BUFFER",
    "DM_IN_PROMPT",
    "DM_LOGPIXELS",
    "DM_MEDIATYPE",
    "DM_MODIFY",
    "DM_NUP",
    "DM_ORIENTATION",
    "DM_OUT_BUFFER",
    "DM_OUT_DEFAULT",
    "DM_PANNINGHEIGHT",
    "DM_PANNINGWIDTH",
    "DM_PAPERLENGTH",
    "DM_PAPERSIZE",
    "DM_PAPERWIDTH",
    "DM_PELSHEIGHT",
    "DM_PELSWIDTH",
    "DM_POSITION",
    "DM_PRINTQUALITY",
    "DM_PROMPT",
    "DM_SCALE",
    "DM_SPECVERSION",
    "DM_TTOPTION",
    "DM_UPDATE",
    "DM_YRESOLUTION",
    "DOWNLOADFACE",
    "DOWNLOADHEADER",
    "DPtoLP",
    "DRAFTMODE",
    "DRAFT_QUALITY",
    "DRAWEDGE_FLAGS",
    "DRAWPATTERNRECT",
    "DRAWSTATEPROC",
    "DRAWSTATE_FLAGS",
    "DRAWTEXTPARAMS",
    "DRAW_CAPTION_FLAGS",
    "DRAW_EDGE_FLAGS",
    "DRAW_TEXT_FORMAT",
    "DRIVERVERSION",
    "DSS_DISABLED",
    "DSS_HIDEPREFIX",
    "DSS_MONO",
    "DSS_NORMAL",
    "DSS_PREFIXONLY",
    "DSS_RIGHT",
    "DSS_UNION",
    "DSTINVERT",
    "DST_BITMAP",
    "DST_COMPLEX",
    "DST_ICON",
    "DST_PREFIXTEXT",
    "DST_TEXT",
    "DT_BOTTOM",
    "DT_CALCRECT",
    "DT_CENTER",
    "DT_CHARSTREAM",
    "DT_DISPFILE",
    "DT_EDITCONTROL",
    "DT_END_ELLIPSIS",
    "DT_EXPANDTABS",
    "DT_EXTERNALLEADING",
    "DT_HIDEPREFIX",
    "DT_INTERNAL",
    "DT_LEFT",
    "DT_METAFILE",
    "DT_MODIFYSTRING",
    "DT_NOCLIP",
    "DT_NOFULLWIDTHCHARBREAK",
    "DT_NOPREFIX",
    "DT_PATH_ELLIPSIS",
    "DT_PLOTTER",
    "DT_PREFIXONLY",
    "DT_RASCAMERA",
    "DT_RASDISPLAY",
    "DT_RASPRINTER",
    "DT_RIGHT",
    "DT_RTLREADING",
    "DT_SINGLELINE",
    "DT_TABSTOP",
    "DT_TOP",
    "DT_VCENTER",
    "DT_WORDBREAK",
    "DT_WORD_ELLIPSIS",
    "DeleteDC",
    "DeleteEnhMetaFile",
    "DeleteMetaFile",
    "DeleteObject",
    "DrawAnimatedRects",
    "DrawCaption",
    "DrawEdge",
    "DrawEscape",
    "DrawFocusRect",
    "DrawFrameControl",
    "DrawStateA",
    "DrawStateW",
    "DrawTextA",
    "DrawTextExA",
    "DrawTextExW",
    "DrawTextW",
    "EASTEUROPE_CHARSET",
    "EDGE_BUMP",
    "EDGE_ETCHED",
    "EDGE_RAISED",
    "EDGE_SUNKEN",
    "ELF_CULTURE_LATIN",
    "ELF_VENDOR_SIZE",
    "ELF_VERSION",
    "EMBEDDED_FONT_PRIV_STATUS",
    "EMBED_EDITABLE",
    "EMBED_FONT_CHARSET",
    "EMBED_INSTALLABLE",
    "EMBED_NOEMBEDDING",
    "EMBED_PREVIEWPRINT",
    "EMR",
    "EMRALPHABLEND",
    "EMRANGLEARC",
    "EMRARC",
    "EMRBITBLT",
    "EMRCOLORCORRECTPALETTE",
    "EMRCOLORMATCHTOTARGET",
    "EMRCREATEBRUSHINDIRECT",
    "EMRCREATEDIBPATTERNBRUSHPT",
    "EMRCREATEMONOBRUSH",
    "EMRCREATEPALETTE",
    "EMRCREATEPEN",
    "EMRELLIPSE",
    "EMREOF",
    "EMREXCLUDECLIPRECT",
    "EMREXTCREATEFONTINDIRECTW",
    "EMREXTCREATEPEN",
    "EMREXTESCAPE",
    "EMREXTFLOODFILL",
    "EMREXTSELECTCLIPRGN",
    "EMREXTTEXTOUTA",
    "EMRFILLPATH",
    "EMRFILLRGN",
    "EMRFORMAT",
    "EMRFRAMERGN",
    "EMRGDICOMMENT",
    "EMRGLSBOUNDEDRECORD",
    "EMRGLSRECORD",
    "EMRGRADIENTFILL",
    "EMRINVERTRGN",
    "EMRLINETO",
    "EMRMASKBLT",
    "EMRMODIFYWORLDTRANSFORM",
    "EMRNAMEDESCAPE",
    "EMROFFSETCLIPRGN",
    "EMRPLGBLT",
    "EMRPOLYDRAW",
    "EMRPOLYDRAW16",
    "EMRPOLYLINE",
    "EMRPOLYLINE16",
    "EMRPOLYPOLYLINE",
    "EMRPOLYPOLYLINE16",
    "EMRPOLYTEXTOUTA",
    "EMRRESIZEPALETTE",
    "EMRRESTOREDC",
    "EMRROUNDRECT",
    "EMRSCALEVIEWPORTEXTEX",
    "EMRSELECTCLIPPATH",
    "EMRSELECTOBJECT",
    "EMRSELECTPALETTE",
    "EMRSETARCDIRECTION",
    "EMRSETCOLORADJUSTMENT",
    "EMRSETCOLORSPACE",
    "EMRSETDIBITSTODEVICE",
    "EMRSETICMPROFILE",
    "EMRSETMAPPERFLAGS",
    "EMRSETMITERLIMIT",
    "EMRSETPALETTEENTRIES",
    "EMRSETPIXELV",
    "EMRSETTEXTCOLOR",
    "EMRSETVIEWPORTEXTEX",
    "EMRSETVIEWPORTORGEX",
    "EMRSETWORLDTRANSFORM",
    "EMRSTRETCHBLT",
    "EMRSTRETCHDIBITS",
    "EMRTEXT",
    "EMRTRANSPARENTBLT",
    "EMR_ABORTPATH",
    "EMR_ALPHABLEND",
    "EMR_ANGLEARC",
    "EMR_ARC",
    "EMR_ARCTO",
    "EMR_BEGINPATH",
    "EMR_BITBLT",
    "EMR_CHORD",
    "EMR_CLOSEFIGURE",
    "EMR_COLORCORRECTPALETTE",
    "EMR_COLORMATCHTOTARGETW",
    "EMR_CREATEBRUSHINDIRECT",
    "EMR_CREATECOLORSPACE",
    "EMR_CREATECOLORSPACEW",
    "EMR_CREATEDIBPATTERNBRUSHPT",
    "EMR_CREATEMONOBRUSH",
    "EMR_CREATEPALETTE",
    "EMR_CREATEPEN",
    "EMR_DELETECOLORSPACE",
    "EMR_DELETEOBJECT",
    "EMR_ELLIPSE",
    "EMR_ENDPATH",
    "EMR_EOF",
    "EMR_EXCLUDECLIPRECT",
    "EMR_EXTCREATEFONTINDIRECTW",
    "EMR_EXTCREATEPEN",
    "EMR_EXTFLOODFILL",
    "EMR_EXTSELECTCLIPRGN",
    "EMR_EXTTEXTOUTA",
    "EMR_EXTTEXTOUTW",
    "EMR_FILLPATH",
    "EMR_FILLRGN",
    "EMR_FLATTENPATH",
    "EMR_FRAMERGN",
    "EMR_GDICOMMENT",
    "EMR_GLSBOUNDEDRECORD",
    "EMR_GLSRECORD",
    "EMR_GRADIENTFILL",
    "EMR_HEADER",
    "EMR_INTERSECTCLIPRECT",
    "EMR_INVERTRGN",
    "EMR_LINETO",
    "EMR_MASKBLT",
    "EMR_MAX",
    "EMR_MIN",
    "EMR_MODIFYWORLDTRANSFORM",
    "EMR_MOVETOEX",
    "EMR_OFFSETCLIPRGN",
    "EMR_PAINTRGN",
    "EMR_PIE",
    "EMR_PIXELFORMAT",
    "EMR_PLGBLT",
    "EMR_POLYBEZIER",
    "EMR_POLYBEZIER16",
    "EMR_POLYBEZIERTO",
    "EMR_POLYBEZIERTO16",
    "EMR_POLYDRAW",
    "EMR_POLYDRAW16",
    "EMR_POLYGON",
    "EMR_POLYGON16",
    "EMR_POLYLINE",
    "EMR_POLYLINE16",
    "EMR_POLYLINETO",
    "EMR_POLYLINETO16",
    "EMR_POLYPOLYGON",
    "EMR_POLYPOLYGON16",
    "EMR_POLYPOLYLINE",
    "EMR_POLYPOLYLINE16",
    "EMR_POLYTEXTOUTA",
    "EMR_POLYTEXTOUTW",
    "EMR_REALIZEPALETTE",
    "EMR_RECTANGLE",
    "EMR_RESERVED_105",
    "EMR_RESERVED_106",
    "EMR_RESERVED_107",
    "EMR_RESERVED_108",
    "EMR_RESERVED_109",
    "EMR_RESERVED_110",
    "EMR_RESERVED_117",
    "EMR_RESERVED_119",
    "EMR_RESERVED_120",
    "EMR_RESIZEPALETTE",
    "EMR_RESTOREDC",
    "EMR_ROUNDRECT",
    "EMR_SAVEDC",
    "EMR_SCALEVIEWPORTEXTEX",
    "EMR_SCALEWINDOWEXTEX",
    "EMR_SELECTCLIPPATH",
    "EMR_SELECTOBJECT",
    "EMR_SELECTPALETTE",
    "EMR_SETARCDIRECTION",
    "EMR_SETBKCOLOR",
    "EMR_SETBKMODE",
    "EMR_SETBRUSHORGEX",
    "EMR_SETCOLORADJUSTMENT",
    "EMR_SETCOLORSPACE",
    "EMR_SETDIBITSTODEVICE",
    "EMR_SETICMMODE",
    "EMR_SETICMPROFILEA",
    "EMR_SETICMPROFILEW",
    "EMR_SETLAYOUT",
    "EMR_SETMAPMODE",
    "EMR_SETMAPPERFLAGS",
    "EMR_SETMETARGN",
    "EMR_SETMITERLIMIT",
    "EMR_SETPALETTEENTRIES",
    "EMR_SETPIXELV",
    "EMR_SETPOLYFILLMODE",
    "EMR_SETROP2",
    "EMR_SETSTRETCHBLTMODE",
    "EMR_SETTEXTALIGN",
    "EMR_SETTEXTCOLOR",
    "EMR_SETVIEWPORTEXTEX",
    "EMR_SETVIEWPORTORGEX",
    "EMR_SETWINDOWEXTEX",
    "EMR_SETWINDOWORGEX",
    "EMR_SETWORLDTRANSFORM",
    "EMR_STRETCHBLT",
    "EMR_STRETCHDIBITS",
    "EMR_STROKEANDFILLPATH",
    "EMR_STROKEPATH",
    "EMR_TRANSPARENTBLT",
    "EMR_WIDENPATH",
    "ENABLEDUPLEX",
    "ENABLEPAIRKERNING",
    "ENABLERELATIVEWIDTHS",
    "ENCAPSULATED_POSTSCRIPT",
    "ENDDOC",
    "END_PATH",
    "ENHANCED_METAFILE_RECORD_TYPE",
    "ENHMETAHEADER",
    "ENHMETARECORD",
    "ENHMETA_SIGNATURE",
    "ENHMETA_STOCK_OBJECT",
    "ENHMFENUMPROC",
    "ENUMLOGFONTA",
    "ENUMLOGFONTEXA",
    "ENUMLOGFONTEXDVA",
    "ENUMLOGFONTEXDVW",
    "ENUMLOGFONTEXW",
    "ENUMLOGFONTW",
    "ENUMPAPERBINS",
    "ENUMPAPERMETRICS",
    "ENUM_CURRENT_SETTINGS",
    "ENUM_DISPLAY_SETTINGS_MODE",
    "ENUM_REGISTRY_SETTINGS",
    "EPSPRINTING",
    "EPS_SIGNATURE",
    "ERROR",
    "ERR_FORMAT",
    "ERR_GENERIC",
    "ERR_INVALID_BASE",
    "ERR_INVALID_CMAP",
    "ERR_INVALID_DELTA_FORMAT",
    "ERR_INVALID_EBLC",
    "ERR_INVALID_GDEF",
    "ERR_INVALID_GLYF",
    "ERR_INVALID_GPOS",
    "ERR_INVALID_GSUB",
    "ERR_INVALID_HDMX",
    "ERR_INVALID_HEAD",
    "ERR_INVALID_HHEA",
    "ERR_INVALID_HHEA_OR_VHEA",
    "ERR_INVALID_HMTX",
    "ERR_INVALID_HMTX_OR_VMTX",
    "ERR_INVALID_JSTF",
    "ERR_INVALID_LOCA",
    "ERR_INVALID_LTSH",
    "ERR_INVALID_MAXP",
    "ERR_INVALID_MERGE_CHECKSUMS",
    "ERR_INVALID_MERGE_FORMATS",
    "ERR_INVALID_MERGE_NUMGLYPHS",
    "ERR_INVALID_NAME",
    "ERR_INVALID_OS2",
    "ERR_INVALID_POST",
    "ERR_INVALID_TTC_INDEX",
    "ERR_INVALID_TTO",
    "ERR_INVALID_VDMX",
    "ERR_INVALID_VHEA",
    "ERR_INVALID_VMTX",
    "ERR_MEM",
    "ERR_MISSING_CMAP",
    "ERR_MISSING_EBDT",
    "ERR_MISSING_GLYF",
    "ERR_MISSING_HEAD",
    "ERR_MISSING_HHEA",
    "ERR_MISSING_HHEA_OR_VHEA",
    "ERR_MISSING_HMTX",
    "ERR_MISSING_HMTX_OR_VMTX",
    "ERR_MISSING_LOCA",
    "ERR_MISSING_MAXP",
    "ERR_MISSING_NAME",
    "ERR_MISSING_OS2",
    "ERR_MISSING_POST",
    "ERR_MISSING_VHEA",
    "ERR_MISSING_VMTX",
    "ERR_NOT_TTC",
    "ERR_NO_GLYPHS",
    "ERR_PARAMETER0",
    "ERR_PARAMETER1",
    "ERR_PARAMETER10",
    "ERR_PARAMETER11",
    "ERR_PARAMETER12",
    "ERR_PARAMETER13",
    "ERR_PARAMETER14",
    "ERR_PARAMETER15",
    "ERR_PARAMETER16",
    "ERR_PARAMETER2",
    "ERR_PARAMETER3",
    "ERR_PARAMETER4",
    "ERR_PARAMETER5",
    "ERR_PARAMETER6",
    "ERR_PARAMETER7",
    "ERR_PARAMETER8",
    "ERR_PARAMETER9",
    "ERR_READCONTROL",
    "ERR_READOUTOFBOUNDS",
    "ERR_VERSION",
    "ERR_WOULD_GROW",
    "ERR_WRITECONTROL",
    "ERR_WRITEOUTOFBOUNDS",
    "ETO_CLIPPED",
    "ETO_GLYPH_INDEX",
    "ETO_IGNORELANGUAGE",
    "ETO_NUMERICSLATIN",
    "ETO_NUMERICSLOCAL",
    "ETO_OPAQUE",
    "ETO_OPTIONS",
    "ETO_PDY",
    "ETO_REVERSE_INDEX_MAP",
    "ETO_RTLREADING",
    "EXTLOGFONTA",
    "EXTLOGFONTW",
    "EXTLOGPEN",
    "EXTLOGPEN32",
    "EXTTEXTOUT",
    "EXT_DEVICE_CAPS",
    "EXT_FLOOD_FILL_TYPE",
    "E_ADDFONTFAILED",
    "E_API_NOTIMPL",
    "E_CHARCODECOUNTINVALID",
    "E_CHARCODESETINVALID",
    "E_CHARSETINVALID",
    "E_COULDNTCREATETEMPFILE",
    "E_DEVICETRUETYPEFONT",
    "E_ERRORACCESSINGEXCLUDELIST",
    "E_ERRORACCESSINGFACENAME",
    "E_ERRORACCESSINGFONTDATA",
    "E_ERRORCOMPRESSINGFONTDATA",
    "E_ERRORCONVERTINGCHARS",
    "E_ERRORCREATINGFONTFILE",
    "E_ERRORDECOMPRESSINGFONTDATA",
    "E_ERROREXPANDINGFONTDATA",
    "E_ERRORGETTINGDC",
    "E_ERRORREADINGFONTDATA",
    "E_ERRORUNICODECONVERSION",
    "E_EXCEPTION",
    "E_EXCEPTIONINCOMPRESSION",
    "E_EXCEPTIONINDECOMPRESSION",
    "E_FACENAMEINVALID",
    "E_FILE_NOT_FOUND",
    "E_FLAGSINVALID",
    "E_FONTALREADYEXISTS",
    "E_FONTDATAINVALID",
    "E_FONTFAMILYNAMENOTINFULL",
    "E_FONTFILECREATEFAILED",
    "E_FONTFILENOTFOUND",
    "E_FONTINSTALLFAILED",
    "E_FONTNAMEALREADYEXISTS",
    "E_FONTNOTEMBEDDABLE",
    "E_FONTREFERENCEINVALID",
    "E_FONTVARIATIONSIMULATED",
    "E_HDCINVALID",
    "E_INPUTPARAMINVALID",
    "E_NAMECHANGEFAILED",
    "E_NOFREEMEMORY",
    "E_NONE",
    "E_NOOS2",
    "E_NOTATRUETYPEFONT",
    "E_PBENABLEDINVALID",
    "E_PERMISSIONSINVALID",
    "E_PRIVSINVALID",
    "E_PRIVSTATUSINVALID",
    "E_READFROMSTREAMFAILED",
    "E_RESERVEDPARAMNOTNULL",
    "E_RESOURCEFILECREATEFAILED",
    "E_SAVETOSTREAMFAILED",
    "E_STATUSINVALID",
    "E_STREAMINVALID",
    "E_SUBSETTINGEXCEPTION",
    "E_SUBSETTINGFAILED",
    "E_SUBSTRING_TEST_FAIL",
    "E_T2NOFREEMEMORY",
    "E_TTC_INDEX_OUT_OF_RANGE",
    "E_WINDOWSAPI",
    "Ellipse",
    "EndPaint",
    "EndPath",
    "EnumDisplayDevicesA",
    "EnumDisplayDevicesW",
    "EnumDisplayMonitors",
    "EnumDisplaySettingsA",
    "EnumDisplaySettingsExA",
    "EnumDisplaySettingsExW",
    "EnumDisplaySettingsW",
    "EnumEnhMetaFile",
    "EnumFontFamiliesA",
    "EnumFontFamiliesExA",
    "EnumFontFamiliesExW",
    "EnumFontFamiliesW",
    "EnumFontsA",
    "EnumFontsW",
    "EnumMetaFile",
    "EnumObjects",
    "EqualRect",
    "EqualRgn",
    "ExcludeClipRect",
    "ExcludeUpdateRgn",
    "ExtCreatePen",
    "ExtCreateRegion",
    "ExtFloodFill",
    "ExtSelectClipRgn",
    "ExtTextOutA",
    "ExtTextOutW",
    "FEATURESETTING_CUSTPAPER",
    "FEATURESETTING_MIRROR",
    "FEATURESETTING_NEGATIVE",
    "FEATURESETTING_NUP",
    "FEATURESETTING_OUTPUT",
    "FEATURESETTING_PRIVATE_BEGIN",
    "FEATURESETTING_PRIVATE_END",
    "FEATURESETTING_PROTOCOL",
    "FEATURESETTING_PSLEVEL",
    "FF_DECORATIVE",
    "FF_DONTCARE",
    "FF_MODERN",
    "FF_ROMAN",
    "FF_SCRIPT",
    "FF_SWISS",
    "FIXED",
    "FIXED_PITCH",
    "FLI_GLYPHS",
    "FLI_MASK",
    "FLOODFILLBORDER",
    "FLOODFILLSURFACE",
    "FLUSHOUTPUT",
    "FONTENUMPROCA",
    "FONTENUMPROCW",
    "FONTMAPPER_MAX",
    "FONT_CHARSET",
    "FONT_CLIP_PRECISION",
    "FONT_FAMILY",
    "FONT_LICENSE_PRIVS",
    "FONT_OUTPUT_PRECISION",
    "FONT_PITCH",
    "FONT_QUALITY",
    "FONT_RESOURCE_CHARACTERISTICS",
    "FONT_WEIGHT",
    "FR_NOT_ENUM",
    "FR_PRIVATE",
    "FS_ARABIC",
    "FS_BALTIC",
    "FS_CHINESESIMP",
    "FS_CHINESETRAD",
    "FS_CYRILLIC",
    "FS_GREEK",
    "FS_HEBREW",
    "FS_JISJAPAN",
    "FS_JOHAB",
    "FS_LATIN1",
    "FS_LATIN2",
    "FS_SYMBOL",
    "FS_THAI",
    "FS_TURKISH",
    "FS_VIETNAMESE",
    "FS_WANSUNG",
    "FW_BLACK",
    "FW_BOLD",
    "FW_DEMIBOLD",
    "FW_DONTCARE",
    "FW_EXTRABOLD",
    "FW_EXTRALIGHT",
    "FW_HEAVY",
    "FW_LIGHT",
    "FW_MEDIUM",
    "FW_NORMAL",
    "FW_REGULAR",
    "FW_SEMIBOLD",
    "FW_THIN",
    "FW_ULTRABOLD",
    "FW_ULTRALIGHT",
    "FillPath",
    "FillRect",
    "FillRgn",
    "FixBrushOrgEx",
    "FlattenPath",
    "FloodFill",
    "FrameRect",
    "FrameRgn",
    "GB2312_CHARSET",
    "GCPCLASS_ARABIC",
    "GCPCLASS_HEBREW",
    "GCPCLASS_LATIN",
    "GCPCLASS_LATINNUMBER",
    "GCPCLASS_LATINNUMERICSEPARATOR",
    "GCPCLASS_LATINNUMERICTERMINATOR",
    "GCPCLASS_LOCALNUMBER",
    "GCPCLASS_NEUTRAL",
    "GCPCLASS_NUMERICSEPARATOR",
    "GCPCLASS_POSTBOUNDLTR",
    "GCPCLASS_POSTBOUNDRTL",
    "GCPCLASS_PREBOUNDLTR",
    "GCPCLASS_PREBOUNDRTL",
    "GCPGLYPH_LINKAFTER",
    "GCPGLYPH_LINKBEFORE",
    "GCP_CLASSIN",
    "GCP_DBCS",
    "GCP_DIACRITIC",
    "GCP_DISPLAYZWG",
    "GCP_ERROR",
    "GCP_GLYPHSHAPE",
    "GCP_JUSTIFY",
    "GCP_JUSTIFYIN",
    "GCP_KASHIDA",
    "GCP_LIGATE",
    "GCP_MAXEXTENT",
    "GCP_NEUTRALOVERRIDE",
    "GCP_NUMERICOVERRIDE",
    "GCP_NUMERICSLATIN",
    "GCP_NUMERICSLOCAL",
    "GCP_REORDER",
    "GCP_RESULTSA",
    "GCP_RESULTSW",
    "GCP_SYMSWAPOFF",
    "GCP_USEKERNING",
    "GDICOMMENT_BEGINGROUP",
    "GDICOMMENT_ENDGROUP",
    "GDICOMMENT_IDENTIFIER",
    "GDICOMMENT_MULTIFORMATS",
    "GDICOMMENT_UNICODE_END",
    "GDICOMMENT_UNICODE_STRING",
    "GDICOMMENT_WINDOWS_METAFILE",
    "GDIPLUS_TS_QUERYVER",
    "GDIPLUS_TS_RECORD",
    "GDIREGISTERDDRAWPACKETVERSION",
    "GDI_ERROR",
    "GDI_REGION_TYPE",
    "GETCOLORTABLE",
    "GETDEVICEUNITS",
    "GETEXTENDEDTEXTMETRICS",
    "GETEXTENTTABLE",
    "GETFACENAME",
    "GETPAIRKERNTABLE",
    "GETPENWIDTH",
    "GETPHYSPAGESIZE",
    "GETPRINTINGOFFSET",
    "GETSCALINGFACTOR",
    "GETSETPAPERBINS",
    "GETSETPAPERMETRICS",
    "GETSETPRINTORIENT",
    "GETSETSCREENPARAMS",
    "GETTECHNOLGY",
    "GETTECHNOLOGY",
    "GETTRACKKERNTABLE",
    "GETVECTORBRUSHSIZE",
    "GETVECTORPENSIZE",
    "GET_CHARACTER_PLACEMENT_FLAGS",
    "GET_DCX_FLAGS",
    "GET_DEVICE_CAPS_INDEX",
    "GET_GLYPH_OUTLINE_FORMAT",
    "GET_PS_FEATURESETTING",
    "GET_STOCK_OBJECT_FLAGS",
    "GGI_MARK_NONEXISTING_GLYPHS",
    "GGO_BEZIER",
    "GGO_BITMAP",
    "GGO_GLYPH_INDEX",
    "GGO_GRAY2_BITMAP",
    "GGO_GRAY4_BITMAP",
    "GGO_GRAY8_BITMAP",
    "GGO_METRICS",
    "GGO_NATIVE",
    "GGO_UNHINTED",
    "GLYPHMETRICS",
    "GLYPHSET",
    "GM_ADVANCED",
    "GM_COMPATIBLE",
    "GM_LAST",
    "GOBJENUMPROC",
    "GRADIENT_FILL",
    "GRADIENT_FILL_OP_FLAG",
    "GRADIENT_FILL_RECT_H",
    "GRADIENT_FILL_RECT_V",
    "GRADIENT_FILL_TRIANGLE",
    "GRADIENT_RECT",
    "GRADIENT_TRIANGLE",
    "GRAPHICS_MODE",
    "GRAYSTRINGPROC",
    "GRAY_BRUSH",
    "GREEK_CHARSET",
    "GS_8BIT_INDICES",
    "GdiAlphaBlend",
    "GdiComment",
    "GdiFlush",
    "GdiGetBatchLimit",
    "GdiGradientFill",
    "GdiSetBatchLimit",
    "GdiTransparentBlt",
    "GetArcDirection",
    "GetAspectRatioFilterEx",
    "GetBitmapBits",
    "GetBitmapDimensionEx",
    "GetBkColor",
    "GetBkMode",
    "GetBoundsRect",
    "GetBrushOrgEx",
    "GetCharABCWidthsA",
    "GetCharABCWidthsFloatA",
    "GetCharABCWidthsFloatW",
    "GetCharABCWidthsI",
    "GetCharABCWidthsW",
    "GetCharWidth32A",
    "GetCharWidth32W",
    "GetCharWidthA",
    "GetCharWidthFloatA",
    "GetCharWidthFloatW",
    "GetCharWidthI",
    "GetCharWidthW",
    "GetCharacterPlacementA",
    "GetCharacterPlacementW",
    "GetClipBox",
    "GetClipRgn",
    "GetColorAdjustment",
    "GetCurrentObject",
    "GetCurrentPositionEx",
    "GetDC",
    "GetDCBrushColor",
    "GetDCEx",
    "GetDCOrgEx",
    "GetDCPenColor",
    "GetDIBColorTable",
    "GetDIBits",
    "GetDeviceCaps",
    "GetEnhMetaFileA",
    "GetEnhMetaFileBits",
    "GetEnhMetaFileDescriptionA",
    "GetEnhMetaFileDescriptionW",
    "GetEnhMetaFileHeader",
    "GetEnhMetaFilePaletteEntries",
    "GetEnhMetaFileW",
    "GetFontData",
    "GetFontLanguageInfo",
    "GetFontUnicodeRanges",
    "GetGlyphIndicesA",
    "GetGlyphIndicesW",
    "GetGlyphOutlineA",
    "GetGlyphOutlineW",
    "GetGraphicsMode",
    "GetKerningPairsA",
    "GetKerningPairsW",
    "GetLayout",
    "GetMapMode",
    "GetMetaFileA",
    "GetMetaFileBitsEx",
    "GetMetaFileW",
    "GetMetaRgn",
    "GetMiterLimit",
    "GetMonitorInfoA",
    "GetMonitorInfoW",
    "GetNearestColor",
    "GetNearestPaletteIndex",
    "GetObjectA",
    "GetObjectType",
    "GetObjectW",
    "GetOutlineTextMetricsA",
    "GetOutlineTextMetricsW",
    "GetPaletteEntries",
    "GetPath",
    "GetPixel",
    "GetPolyFillMode",
    "GetROP2",
    "GetRandomRgn",
    "GetRasterizerCaps",
    "GetRegionData",
    "GetRgnBox",
    "GetStockObject",
    "GetStretchBltMode",
    "GetSysColor",
    "GetSysColorBrush",
    "GetSystemPaletteEntries",
    "GetSystemPaletteUse",
    "GetTabbedTextExtentA",
    "GetTabbedTextExtentW",
    "GetTextAlign",
    "GetTextCharacterExtra",
    "GetTextColor",
    "GetTextExtentExPointA",
    "GetTextExtentExPointI",
    "GetTextExtentExPointW",
    "GetTextExtentPoint32A",
    "GetTextExtentPoint32W",
    "GetTextExtentPointA",
    "GetTextExtentPointI",
    "GetTextExtentPointW",
    "GetTextFaceA",
    "GetTextFaceW",
    "GetTextMetricsA",
    "GetTextMetricsW",
    "GetUpdateRect",
    "GetUpdateRgn",
    "GetViewportExtEx",
    "GetViewportOrgEx",
    "GetWinMetaFileBits",
    "GetWindowDC",
    "GetWindowExtEx",
    "GetWindowOrgEx",
    "GetWindowRgn",
    "GetWindowRgnBox",
    "GetWorldTransform",
    "GradientFill",
    "GrayStringA",
    "GrayStringW",
    "HALFTONE",
    "HANDLETABLE",
    "HANGEUL_CHARSET",
    "HANGUL_CHARSET",
    "HATCH_BRUSH_STYLE",
    "HBITMAP",
    "HBRUSH",
    "HDC",
    "HDC_MAP_MODE",
    "HEBREW_CHARSET",
    "HENHMETAFILE",
    "HFONT",
    "HGDIOBJ",
    "HMETAFILE",
    "HMONITOR",
    "HOLLOW_BRUSH",
    "HORZRES",
    "HORZSIZE",
    "HPALETTE",
    "HPEN",
    "HRGN",
    "HS_API_MAX",
    "HS_BDIAGONAL",
    "HS_CROSS",
    "HS_DIAGCROSS",
    "HS_FDIAGONAL",
    "HS_HORIZONTAL",
    "HS_VERTICAL",
    "HdcMetdataEnhFileHandle",
    "HdcMetdataFileHandle",
    "ILLUMINANT_A",
    "ILLUMINANT_B",
    "ILLUMINANT_C",
    "ILLUMINANT_D50",
    "ILLUMINANT_D55",
    "ILLUMINANT_D65",
    "ILLUMINANT_D75",
    "ILLUMINANT_DAYLIGHT",
    "ILLUMINANT_DEVICE_DEFAULT",
    "ILLUMINANT_F2",
    "ILLUMINANT_FLUORESCENT",
    "ILLUMINANT_MAX_INDEX",
    "ILLUMINANT_NTSC",
    "ILLUMINANT_TUNGSTEN",
    "InflateRect",
    "IntersectClipRect",
    "IntersectRect",
    "InvalidateRect",
    "InvalidateRgn",
    "InvertRect",
    "InvertRgn",
    "IsRectEmpty",
    "JOHAB_CHARSET",
    "KERNINGPAIR",
    "LAYOUT_BITMAPORIENTATIONPRESERVED",
    "LAYOUT_BTT",
    "LAYOUT_RTL",
    "LAYOUT_VBH",
    "LCS_CALIBRATED_RGB",
    "LCS_GM_ABS_COLORIMETRIC",
    "LCS_GM_BUSINESS",
    "LCS_GM_GRAPHICS",
    "LCS_GM_IMAGES",
    "LC_INTERIORS",
    "LC_MARKER",
    "LC_NONE",
    "LC_POLYLINE",
    "LC_POLYMARKER",
    "LC_STYLED",
    "LC_WIDE",
    "LC_WIDESTYLED",
    "LF_FACESIZE",
    "LF_FULLFACESIZE",
    "LICENSE_DEFAULT",
    "LICENSE_EDITABLE",
    "LICENSE_INSTALLABLE",
    "LICENSE_NOEMBEDDING",
    "LICENSE_PREVIEWPRINT",
    "LINECAPS",
    "LINEDDAPROC",
    "LOGBRUSH",
    "LOGBRUSH32",
    "LOGFONTA",
    "LOGFONTW",
    "LOGPALETTE",
    "LOGPEN",
    "LOGPIXELSX",
    "LOGPIXELSY",
    "LPD_DOUBLEBUFFER",
    "LPD_SHARE_ACCUM",
    "LPD_SHARE_DEPTH",
    "LPD_SHARE_STENCIL",
    "LPD_STEREO",
    "LPD_SUPPORT_GDI",
    "LPD_SUPPORT_OPENGL",
    "LPD_SWAP_COPY",
    "LPD_SWAP_EXCHANGE",
    "LPD_TRANSPARENT",
    "LPD_TYPE_COLORINDEX",
    "LPD_TYPE_RGBA",
    "LPFNDEVCAPS",
    "LPFNDEVMODE",
    "LPtoDP",
    "LTGRAY_BRUSH",
    "LineDDA",
    "LineTo",
    "LoadBitmapA",
    "LoadBitmapW",
    "LockWindowUpdate",
    "MAC_CHARSET",
    "MAT2",
    "MAXSTRETCHBLTMODE",
    "MERGECOPY",
    "MERGEPAINT",
    "METAFILE_DRIVER",
    "METAHEADER",
    "METARECORD",
    "META_ANIMATEPALETTE",
    "META_ARC",
    "META_BITBLT",
    "META_CHORD",
    "META_CREATEBRUSHINDIRECT",
    "META_CREATEFONTINDIRECT",
    "META_CREATEPALETTE",
    "META_CREATEPATTERNBRUSH",
    "META_CREATEPENINDIRECT",
    "META_CREATEREGION",
    "META_DELETEOBJECT",
    "META_DIBBITBLT",
    "META_DIBCREATEPATTERNBRUSH",
    "META_DIBSTRETCHBLT",
    "META_ELLIPSE",
    "META_ESCAPE",
    "META_EXCLUDECLIPRECT",
    "META_EXTFLOODFILL",
    "META_EXTTEXTOUT",
    "META_FILLREGION",
    "META_FLOODFILL",
    "META_FRAMEREGION",
    "META_INTERSECTCLIPRECT",
    "META_INVERTREGION",
    "META_LINETO",
    "META_MOVETO",
    "META_OFFSETCLIPRGN",
    "META_OFFSETVIEWPORTORG",
    "META_OFFSETWINDOWORG",
    "META_PAINTREGION",
    "META_PATBLT",
    "META_PIE",
    "META_POLYGON",
    "META_POLYLINE",
    "META_POLYPOLYGON",
    "META_REALIZEPALETTE",
    "META_RECTANGLE",
    "META_RESIZEPALETTE",
    "META_RESTOREDC",
    "META_ROUNDRECT",
    "META_SAVEDC",
    "META_SCALEVIEWPORTEXT",
    "META_SCALEWINDOWEXT",
    "META_SELECTCLIPREGION",
    "META_SELECTOBJECT",
    "META_SELECTPALETTE",
    "META_SETBKCOLOR",
    "META_SETBKMODE",
    "META_SETDIBTODEV",
    "META_SETLAYOUT",
    "META_SETMAPMODE",
    "META_SETMAPPERFLAGS",
    "META_SETPALENTRIES",
    "META_SETPIXEL",
    "META_SETPOLYFILLMODE",
    "META_SETRELABS",
    "META_SETROP2",
    "META_SETSTRETCHBLTMODE",
    "META_SETTEXTALIGN",
    "META_SETTEXTCHAREXTRA",
    "META_SETTEXTCOLOR",
    "META_SETTEXTJUSTIFICATION",
    "META_SETVIEWPORTEXT",
    "META_SETVIEWPORTORG",
    "META_SETWINDOWEXT",
    "META_SETWINDOWORG",
    "META_STRETCHBLT",
    "META_STRETCHDIB",
    "META_TEXTOUT",
    "MFCOMMENT",
    "MFENUMPROC",
    "MILCORE_TS_QUERYVER_RESULT_FALSE",
    "MILCORE_TS_QUERYVER_RESULT_TRUE",
    "MM_ANISOTROPIC",
    "MM_HIENGLISH",
    "MM_HIMETRIC",
    "MM_ISOTROPIC",
    "MM_LOENGLISH",
    "MM_LOMETRIC",
    "MM_MAX_AXES_NAMELEN",
    "MM_MAX_NUMAXES",
    "MM_TEXT",
    "MM_TWIPS",
    "MODIFY_WORLD_TRANSFORM_MODE",
    "MONITORENUMPROC",
    "MONITORINFO",
    "MONITORINFOEXA",
    "MONITORINFOEXW",
    "MONITOR_DEFAULTTONEAREST",
    "MONITOR_DEFAULTTONULL",
    "MONITOR_DEFAULTTOPRIMARY",
    "MONITOR_FROM_FLAGS",
    "MONO_FONT",
    "MOUSETRAILS",
    "MWT_IDENTITY",
    "MWT_LEFTMULTIPLY",
    "MWT_RIGHTMULTIPLY",
    "MapWindowPoints",
    "MaskBlt",
    "MergeFontPackage",
    "ModifyWorldTransform",
    "MonitorFromPoint",
    "MonitorFromRect",
    "MonitorFromWindow",
    "MoveToEx",
    "NEWFRAME",
    "NEWTEXTMETRICA",
    "NEWTEXTMETRICW",
    "NEWTRANSPARENT",
    "NEXTBAND",
    "NOMIRRORBITMAP",
    "NONANTIALIASED_QUALITY",
    "NOTSRCCOPY",
    "NOTSRCERASE",
    "NTM_BOLD",
    "NTM_DSIG",
    "NTM_ITALIC",
    "NTM_MULTIPLEMASTER",
    "NTM_NONNEGATIVE_AC",
    "NTM_PS_OPENTYPE",
    "NTM_REGULAR",
    "NTM_TT_OPENTYPE",
    "NTM_TYPE1",
    "NULLREGION",
    "NULL_BRUSH",
    "NULL_PEN",
    "NUMBRUSHES",
    "NUMCOLORS",
    "NUMFONTS",
    "NUMMARKERS",
    "NUMPENS",
    "NUMRESERVED",
    "OBJ_BITMAP",
    "OBJ_BRUSH",
    "OBJ_COLORSPACE",
    "OBJ_DC",
    "OBJ_ENHMETADC",
    "OBJ_ENHMETAFILE",
    "OBJ_EXTPEN",
    "OBJ_FONT",
    "OBJ_MEMDC",
    "OBJ_METADC",
    "OBJ_METAFILE",
    "OBJ_PAL",
    "OBJ_PEN",
    "OBJ_REGION",
    "OBJ_TYPE",
    "OEM_CHARSET",
    "OEM_FIXED_FONT",
    "OPAQUE",
    "OPENCHANNEL",
    "OUTLINETEXTMETRICA",
    "OUTLINETEXTMETRICW",
    "OUT_CHARACTER_PRECIS",
    "OUT_DEFAULT_PRECIS",
    "OUT_DEVICE_PRECIS",
    "OUT_OUTLINE_PRECIS",
    "OUT_PS_ONLY_PRECIS",
    "OUT_RASTER_PRECIS",
    "OUT_SCREEN_OUTLINE_PRECIS",
    "OUT_STRING_PRECIS",
    "OUT_STROKE_PRECIS",
    "OUT_TT_ONLY_PRECIS",
    "OUT_TT_PRECIS",
    "OffsetClipRgn",
    "OffsetRect",
    "OffsetRgn",
    "OffsetViewportOrgEx",
    "OffsetWindowOrgEx",
    "PAINTSTRUCT",
    "PALETTEENTRY",
    "PANOSE",
    "PANOSE_COUNT",
    "PAN_ANY",
    "PAN_ARMSTYLE_INDEX",
    "PAN_ARM_ANY",
    "PAN_ARM_NO_FIT",
    "PAN_ARM_STYLE",
    "PAN_BENT_ARMS_DOUBLE_SERIF",
    "PAN_BENT_ARMS_HORZ",
    "PAN_BENT_ARMS_SINGLE_SERIF",
    "PAN_BENT_ARMS_VERT",
    "PAN_BENT_ARMS_WEDGE",
    "PAN_CONTRAST",
    "PAN_CONTRAST_ANY",
    "PAN_CONTRAST_HIGH",
    "PAN_CONTRAST_INDEX",
    "PAN_CONTRAST_LOW",
    "PAN_CONTRAST_MEDIUM",
    "PAN_CONTRAST_MEDIUM_HIGH",
    "PAN_CONTRAST_MEDIUM_LOW",
    "PAN_CONTRAST_NONE",
    "PAN_CONTRAST_NO_FIT",
    "PAN_CONTRAST_VERY_HIGH",
    "PAN_CONTRAST_VERY_LOW",
    "PAN_CULTURE_LATIN",
    "PAN_FAMILYTYPE_INDEX",
    "PAN_FAMILY_ANY",
    "PAN_FAMILY_DECORATIVE",
    "PAN_FAMILY_NO_FIT",
    "PAN_FAMILY_PICTORIAL",
    "PAN_FAMILY_SCRIPT",
    "PAN_FAMILY_TEXT_DISPLAY",
    "PAN_FAMILY_TYPE",
    "PAN_LETTERFORM_INDEX",
    "PAN_LETT_FORM",
    "PAN_LETT_FORM_ANY",
    "PAN_LETT_FORM_NO_FIT",
    "PAN_LETT_NORMAL_BOXED",
    "PAN_LETT_NORMAL_CONTACT",
    "PAN_LETT_NORMAL_FLATTENED",
    "PAN_LETT_NORMAL_OFF_CENTER",
    "PAN_LETT_NORMAL_ROUNDED",
    "PAN_LETT_NORMAL_SQUARE",
    "PAN_LETT_NORMAL_WEIGHTED",
    "PAN_LETT_OBLIQUE_BOXED",
    "PAN_LETT_OBLIQUE_CONTACT",
    "PAN_LETT_OBLIQUE_FLATTENED",
    "PAN_LETT_OBLIQUE_OFF_CENTER",
    "PAN_LETT_OBLIQUE_ROUNDED",
    "PAN_LETT_OBLIQUE_SQUARE",
    "PAN_LETT_OBLIQUE_WEIGHTED",
    "PAN_MIDLINE",
    "PAN_MIDLINE_ANY",
    "PAN_MIDLINE_CONSTANT_POINTED",
    "PAN_MIDLINE_CONSTANT_SERIFED",
    "PAN_MIDLINE_CONSTANT_TRIMMED",
    "PAN_MIDLINE_HIGH_POINTED",
    "PAN_MIDLINE_HIGH_SERIFED",
    "PAN_MIDLINE_HIGH_TRIMMED",
    "PAN_MIDLINE_INDEX",
    "PAN_MIDLINE_LOW_POINTED",
    "PAN_MIDLINE_LOW_SERIFED",
    "PAN_MIDLINE_LOW_TRIMMED",
    "PAN_MIDLINE_NO_FIT",
    "PAN_MIDLINE_STANDARD_POINTED",
    "PAN_MIDLINE_STANDARD_SERIFED",
    "PAN_MIDLINE_STANDARD_TRIMMED",
    "PAN_NO_FIT",
    "PAN_PROPORTION",
    "PAN_PROPORTION_INDEX",
    "PAN_PROP_ANY",
    "PAN_PROP_CONDENSED",
    "PAN_PROP_EVEN_WIDTH",
    "PAN_PROP_EXPANDED",
    "PAN_PROP_MODERN",
    "PAN_PROP_MONOSPACED",
    "PAN_PROP_NO_FIT",
    "PAN_PROP_OLD_STYLE",
    "PAN_PROP_VERY_CONDENSED",
    "PAN_PROP_VERY_EXPANDED",
    "PAN_SERIFSTYLE_INDEX",
    "PAN_SERIF_ANY",
    "PAN_SERIF_BONE",
    "PAN_SERIF_COVE",
    "PAN_SERIF_EXAGGERATED",
    "PAN_SERIF_FLARED",
    "PAN_SERIF_NORMAL_SANS",
    "PAN_SERIF_NO_FIT",
    "PAN_SERIF_OBTUSE_COVE",
    "PAN_SERIF_OBTUSE_SANS",
    "PAN_SERIF_OBTUSE_SQUARE_COVE",
    "PAN_SERIF_PERP_SANS",
    "PAN_SERIF_ROUNDED",
    "PAN_SERIF_SQUARE",
    "PAN_SERIF_SQUARE_COVE",
    "PAN_SERIF_STYLE",
    "PAN_SERIF_THIN",
    "PAN_SERIF_TRIANGLE",
    "PAN_STRAIGHT_ARMS_DOUBLE_SERIF",
    "PAN_STRAIGHT_ARMS_HORZ",
    "PAN_STRAIGHT_ARMS_SINGLE_SERIF",
    "PAN_STRAIGHT_ARMS_VERT",
    "PAN_STRAIGHT_ARMS_WEDGE",
    "PAN_STROKEVARIATION_INDEX",
    "PAN_STROKE_ANY",
    "PAN_STROKE_GRADUAL_DIAG",
    "PAN_STROKE_GRADUAL_HORZ",
    "PAN_STROKE_GRADUAL_TRAN",
    "PAN_STROKE_GRADUAL_VERT",
    "PAN_STROKE_INSTANT_VERT",
    "PAN_STROKE_NO_FIT",
    "PAN_STROKE_RAPID_HORZ",
    "PAN_STROKE_RAPID_VERT",
    "PAN_STROKE_VARIATION",
    "PAN_WEIGHT",
    "PAN_WEIGHT_ANY",
    "PAN_WEIGHT_BLACK",
    "PAN_WEIGHT_BOLD",
    "PAN_WEIGHT_BOOK",
    "PAN_WEIGHT_DEMI",
    "PAN_WEIGHT_HEAVY",
    "PAN_WEIGHT_INDEX",
    "PAN_WEIGHT_LIGHT",
    "PAN_WEIGHT_MEDIUM",
    "PAN_WEIGHT_NORD",
    "PAN_WEIGHT_NO_FIT",
    "PAN_WEIGHT_THIN",
    "PAN_WEIGHT_VERY_LIGHT",
    "PAN_XHEIGHT",
    "PAN_XHEIGHT_ANY",
    "PAN_XHEIGHT_CONSTANT_LARGE",
    "PAN_XHEIGHT_CONSTANT_SMALL",
    "PAN_XHEIGHT_CONSTANT_STD",
    "PAN_XHEIGHT_DUCKING_LARGE",
    "PAN_XHEIGHT_DUCKING_SMALL",
    "PAN_XHEIGHT_DUCKING_STD",
    "PAN_XHEIGHT_INDEX",
    "PAN_XHEIGHT_NO_FIT",
    "PASSTHROUGH",
    "PATCOPY",
    "PATINVERT",
    "PATPAINT",
    "PC_EXPLICIT",
    "PC_INTERIORS",
    "PC_NOCOLLAPSE",
    "PC_NONE",
    "PC_PATHS",
    "PC_POLYGON",
    "PC_POLYPOLYGON",
    "PC_RECTANGLE",
    "PC_RESERVED",
    "PC_SCANLINE",
    "PC_STYLED",
    "PC_TRAPEZOID",
    "PC_WIDE",
    "PC_WIDESTYLED",
    "PC_WINDPOLYGON",
    "PDEVICESIZE",
    "PELARRAY",
    "PEN_STYLE",
    "PHYSICALHEIGHT",
    "PHYSICALOFFSETX",
    "PHYSICALOFFSETY",
    "PHYSICALWIDTH",
    "PLANES",
    "POINTFX",
    "POLYFILL_LAST",
    "POLYGONALCAPS",
    "POLYTEXTA",
    "POLYTEXTW",
    "POSTSCRIPT_DATA",
    "POSTSCRIPT_IDENTIFY",
    "POSTSCRIPT_IGNORE",
    "POSTSCRIPT_INJECTION",
    "POSTSCRIPT_PASSTHROUGH",
    "PRINTRATEUNIT_CPS",
    "PRINTRATEUNIT_IPM",
    "PRINTRATEUNIT_LPM",
    "PRINTRATEUNIT_PPM",
    "PROOF_QUALITY",
    "PR_JOBSTATUS",
    "PSIDENT_GDICENTRIC",
    "PSIDENT_PSCENTRIC",
    "PSINJECT_DLFONT",
    "PSPROTOCOL_ASCII",
    "PSPROTOCOL_BCP",
    "PSPROTOCOL_BINARY",
    "PSPROTOCOL_TBCP",
    "PS_ALTERNATE",
    "PS_COSMETIC",
    "PS_DASH",
    "PS_DASHDOT",
    "PS_DASHDOTDOT",
    "PS_DOT",
    "PS_ENDCAP_FLAT",
    "PS_ENDCAP_MASK",
    "PS_ENDCAP_ROUND",
    "PS_ENDCAP_SQUARE",
    "PS_GEOMETRIC",
    "PS_INSIDEFRAME",
    "PS_JOIN_BEVEL",
    "PS_JOIN_MASK",
    "PS_JOIN_MITER",
    "PS_JOIN_ROUND",
    "PS_NULL",
    "PS_SOLID",
    "PS_STYLE_MASK",
    "PS_TYPE_MASK",
    "PS_USERSTYLE",
    "PT_BEZIERTO",
    "PT_CLOSEFIGURE",
    "PT_LINETO",
    "PT_MOVETO",
    "PaintDesktop",
    "PaintRgn",
    "PatBlt",
    "PathToRegion",
    "Pie",
    "PlayEnhMetaFile",
    "PlayEnhMetaFileRecord",
    "PlayMetaFile",
    "PlayMetaFileRecord",
    "PlgBlt",
    "PolyBezier",
    "PolyBezierTo",
    "PolyDraw",
    "PolyPolygon",
    "PolyPolyline",
    "PolyTextOutA",
    "PolyTextOutW",
    "Polygon",
    "Polyline",
    "PolylineTo",
    "PtInRect",
    "PtInRegion",
    "PtVisible",
    "QDC_ALL_PATHS",
    "QDC_DATABASE_CURRENT",
    "QDC_INCLUDE_HMD",
    "QDC_ONLY_ACTIVE_PATHS",
    "QDC_VIRTUAL_MODE_AWARE",
    "QDC_VIRTUAL_REFRESH_RATE_AWARE",
    "QDI_DIBTOSCREEN",
    "QDI_GETDIBITS",
    "QDI_SETDIBITS",
    "QDI_STRETCHDIB",
    "QUERYDIBSUPPORT",
    "QUERYESCSUPPORT",
    "QUERYROPSUPPORT",
    "R2_BLACK",
    "R2_COPYPEN",
    "R2_LAST",
    "R2_MASKNOTPEN",
    "R2_MASKPEN",
    "R2_MASKPENNOT",
    "R2_MERGENOTPEN",
    "R2_MERGEPEN",
    "R2_MERGEPENNOT",
    "R2_MODE",
    "R2_NOP",
    "R2_NOT",
    "R2_NOTCOPYPEN",
    "R2_NOTMASKPEN",
    "R2_NOTMERGEPEN",
    "R2_NOTXORPEN",
    "R2_WHITE",
    "R2_XORPEN",
    "RASTERCAPS",
    "RASTERIZER_STATUS",
    "RASTER_FONTTYPE",
    "RC_BANDING",
    "RC_BIGFONT",
    "RC_BITBLT",
    "RC_BITMAP64",
    "RC_DEVBITS",
    "RC_DIBTODEV",
    "RC_DI_BITMAP",
    "RC_FLOODFILL",
    "RC_GDI20_OUTPUT",
    "RC_GDI20_STATE",
    "RC_OP_DX_OUTPUT",
    "RC_PALETTE",
    "RC_SAVEBITMAP",
    "RC_SCALING",
    "RC_STRETCHBLT",
    "RC_STRETCHDIB",
    "RDH_RECTANGLES",
    "RDW_ALLCHILDREN",
    "RDW_ERASE",
    "RDW_ERASENOW",
    "RDW_FRAME",
    "RDW_INTERNALPAINT",
    "RDW_INVALIDATE",
    "RDW_NOCHILDREN",
    "RDW_NOERASE",
    "RDW_NOFRAME",
    "RDW_NOINTERNALPAINT",
    "RDW_UPDATENOW",
    "RDW_VALIDATE",
    "READEMBEDPROC",
    "REDRAW_WINDOW_FLAGS",
    "RELATIVE",
    "RESTORE_CTM",
    "RGBQUAD",
    "RGBTRIPLE",
    "RGNDATA",
    "RGNDATAHEADER",
    "RGN_AND",
    "RGN_COMBINE_MODE",
    "RGN_COPY",
    "RGN_DIFF",
    "RGN_ERROR",
    "RGN_MAX",
    "RGN_MIN",
    "RGN_OR",
    "RGN_XOR",
    "ROP_CODE",
    "RUSSIAN_CHARSET",
    "RealizePalette",
    "RectInRegion",
    "RectVisible",
    "Rectangle",
    "RedrawWindow",
    "ReleaseDC",
    "RemoveFontMemResourceEx",
    "RemoveFontResourceA",
    "RemoveFontResourceExA",
    "RemoveFontResourceExW",
    "RemoveFontResourceW",
    "ResetDCA",
    "ResetDCW",
    "ResizePalette",
    "RestoreDC",
    "RoundRect",
    "SAVE_CTM",
    "SB_CONST_ALPHA",
    "SB_GRAD_RECT",
    "SB_GRAD_TRI",
    "SB_NONE",
    "SB_PIXEL_ALPHA",
    "SB_PREMULT_ALPHA",
    "SCALINGFACTORX",
    "SCALINGFACTORY",
    "SC_SCREENSAVE",
    "SDC_ALLOW_CHANGES",
    "SDC_ALLOW_PATH_ORDER_CHANGES",
    "SDC_APPLY",
    "SDC_FORCE_MODE_ENUMERATION",
    "SDC_NO_OPTIMIZATION",
    "SDC_PATH_PERSIST_IF_REQUIRED",
    "SDC_SAVE_TO_DATABASE",
    "SDC_TOPOLOGY_CLONE",
    "SDC_TOPOLOGY_EXTEND",
    "SDC_TOPOLOGY_EXTERNAL",
    "SDC_TOPOLOGY_INTERNAL",
    "SDC_TOPOLOGY_SUPPLIED",
    "SDC_USE_SUPPLIED_DISPLAY_CONFIG",
    "SDC_VALIDATE",
    "SDC_VIRTUAL_MODE_AWARE",
    "SDC_VIRTUAL_REFRESH_RATE_AWARE",
    "SELECTDIB",
    "SELECTPAPERSOURCE",
    "SETABORTPROC",
    "SETALLJUSTVALUES",
    "SETCHARSET",
    "SETCOLORTABLE",
    "SETCOPYCOUNT",
    "SETDIBSCALING",
    "SETICMPROFILE_EMBEDED",
    "SETKERNTRACK",
    "SETLINECAP",
    "SETLINEJOIN",
    "SETMITERLIMIT",
    "SET_ARC_DIRECTION",
    "SET_BACKGROUND_COLOR",
    "SET_BOUNDS",
    "SET_BOUNDS_RECT_FLAGS",
    "SET_CLIP_BOX",
    "SET_MIRROR_MODE",
    "SET_POLY_MODE",
    "SET_SCREEN_ANGLE",
    "SET_SPREAD",
    "SHADEBLENDCAPS",
    "SHIFTJIS_CHARSET",
    "SIMPLEREGION",
    "SIZEPALETTE",
    "SPCLPASSTHROUGH2",
    "SP_APPABORT",
    "SP_ERROR",
    "SP_NOTREPORTED",
    "SP_OUTOFDISK",
    "SP_OUTOFMEMORY",
    "SP_USERABORT",
    "SRCAND",
    "SRCCOPY",
    "SRCERASE",
    "SRCINVERT",
    "SRCPAINT",
    "STARTDOC",
    "STOCK_LAST",
    "STRETCHBLT",
    "STRETCH_ANDSCANS",
    "STRETCH_BLT_MODE",
    "STRETCH_DELETESCANS",
    "STRETCH_HALFTONE",
    "STRETCH_ORSCANS",
    "SYMBOL_CHARSET",
    "SYSPAL_ERROR",
    "SYSPAL_NOSTATIC",
    "SYSPAL_NOSTATIC256",
    "SYSPAL_STATIC",
    "SYSRGN",
    "SYSTEM_FIXED_FONT",
    "SYSTEM_FONT",
    "SYSTEM_PALETTE_USE",
    "SYS_COLOR_INDEX",
    "SaveDC",
    "ScaleViewportExtEx",
    "ScaleWindowExtEx",
    "ScreenToClient",
    "SelectClipPath",
    "SelectClipRgn",
    "SelectObject",
    "SelectPalette",
    "SetArcDirection",
    "SetBitmapBits",
    "SetBitmapDimensionEx",
    "SetBkColor",
    "SetBkMode",
    "SetBoundsRect",
    "SetBrushOrgEx",
    "SetColorAdjustment",
    "SetDCBrushColor",
    "SetDCPenColor",
    "SetDIBColorTable",
    "SetDIBits",
    "SetDIBitsToDevice",
    "SetEnhMetaFileBits",
    "SetGraphicsMode",
    "SetLayout",
    "SetMapMode",
    "SetMapperFlags",
    "SetMetaFileBitsEx",
    "SetMetaRgn",
    "SetMiterLimit",
    "SetPaletteEntries",
    "SetPixel",
    "SetPixelV",
    "SetPolyFillMode",
    "SetROP2",
    "SetRect",
    "SetRectEmpty",
    "SetRectRgn",
    "SetStretchBltMode",
    "SetSysColors",
    "SetSystemPaletteUse",
    "SetTextAlign",
    "SetTextCharacterExtra",
    "SetTextColor",
    "SetTextJustification",
    "SetViewportExtEx",
    "SetViewportOrgEx",
    "SetWindowExtEx",
    "SetWindowOrgEx",
    "SetWindowRgn",
    "SetWorldTransform",
    "StretchBlt",
    "StretchDIBits",
    "StrokeAndFillPath",
    "StrokePath",
    "SubtractRect",
    "TA_BASELINE",
    "TA_BOTTOM",
    "TA_CENTER",
    "TA_LEFT",
    "TA_MASK",
    "TA_NOUPDATECP",
    "TA_RIGHT",
    "TA_RTLREADING",
    "TA_TOP",
    "TA_UPDATECP",
    "TC_CP_STROKE",
    "TC_CR_90",
    "TC_CR_ANY",
    "TC_EA_DOUBLE",
    "TC_IA_ABLE",
    "TC_OP_CHARACTER",
    "TC_OP_STROKE",
    "TC_RA_ABLE",
    "TC_RESERVED",
    "TC_SA_CONTIN",
    "TC_SA_DOUBLE",
    "TC_SA_INTEGER",
    "TC_SCROLLBLT",
    "TC_SF_X_YINDEP",
    "TC_SO_ABLE",
    "TC_UA_ABLE",
    "TC_VA_ABLE",
    "TECHNOLOGY",
    "TEXTCAPS",
    "TEXTMETRICA",
    "TEXTMETRICW",
    "TEXT_ALIGN_OPTIONS",
    "THAI_CHARSET",
    "TMPF_DEVICE",
    "TMPF_FIXED_PITCH",
    "TMPF_FLAGS",
    "TMPF_TRUETYPE",
    "TMPF_VECTOR",
    "TRANSFORM_CTM",
    "TRANSPARENT",
    "TRIVERTEX",
    "TRUETYPE_FONTTYPE",
    "TTCharToUnicode",
    "TTDELETE_DONTREMOVEFONT",
    "TTDeleteEmbeddedFont",
    "TTEMBEDINFO",
    "TTEMBED_EMBEDEUDC",
    "TTEMBED_EUDCEMBEDDED",
    "TTEMBED_FAILIFVARIATIONSIMULATED",
    "TTEMBED_FLAGS",
    "TTEMBED_RAW",
    "TTEMBED_SUBSET",
    "TTEMBED_SUBSETCANCEL",
    "TTEMBED_TTCOMPRESSED",
    "TTEMBED_VARIATIONSIMULATED",
    "TTEMBED_WEBOBJECT",
    "TTEMBED_XORENCRYPTDATA",
    "TTEmbedFont",
    "TTEmbedFontEx",
    "TTEmbedFontFromFileA",
    "TTEnableEmbeddingForFacename",
    "TTFCFP_APPLE_PLATFORMID",
    "TTFCFP_DELTA",
    "TTFCFP_DONT_CARE",
    "TTFCFP_FLAGS_COMPRESS",
    "TTFCFP_FLAGS_GLYPHLIST",
    "TTFCFP_FLAGS_SUBSET",
    "TTFCFP_FLAGS_TTC",
    "TTFCFP_ISO_PLATFORMID",
    "TTFCFP_LANG_KEEP_ALL",
    "TTFCFP_MS_PLATFORMID",
    "TTFCFP_STD_MAC_CHAR_SET",
    "TTFCFP_SUBSET",
    "TTFCFP_SUBSET1",
    "TTFCFP_SYMBOL_CHAR_SET",
    "TTFCFP_UNICODE_CHAR_SET",
    "TTFCFP_UNICODE_PLATFORMID",
    "TTFMFP_DELTA",
    "TTFMFP_SUBSET",
    "TTFMFP_SUBSET1",
    "TTGetEmbeddedFontInfo",
    "TTGetEmbeddingType",
    "TTGetNewFontName",
    "TTIsEmbeddingEnabled",
    "TTIsEmbeddingEnabledForFacename",
    "TTLOADINFO",
    "TTLOAD_EMBEDDED_FONT_STATUS",
    "TTLOAD_EUDC_OVERWRITE",
    "TTLOAD_EUDC_SET",
    "TTLOAD_FONT_IN_SYSSTARTUP",
    "TTLOAD_FONT_SUBSETTED",
    "TTLOAD_PRIVATE",
    "TTLoadEmbeddedFont",
    "TTPOLYCURVE",
    "TTPOLYGONHEADER",
    "TTRunValidationTests",
    "TTRunValidationTestsEx",
    "TTVALIDATIONTESTSPARAMS",
    "TTVALIDATIONTESTSPARAMSEX",
    "TT_AVAILABLE",
    "TT_ENABLED",
    "TT_POLYGON_TYPE",
    "TT_PRIM_CSPLINE",
    "TT_PRIM_LINE",
    "TT_PRIM_QSPLINE",
    "TURKISH_CHARSET",
    "TabbedTextOutA",
    "TabbedTextOutW",
    "TextOutA",
    "TextOutW",
    "TransparentBlt",
    "UnionRect",
    "UnrealizeObject",
    "UpdateColors",
    "UpdateWindow",
    "VARIABLE_PITCH",
    "VERTRES",
    "VERTSIZE",
    "VIETNAMESE_CHARSET",
    "VREFRESH",
    "VTA_BASELINE",
    "VTA_BOTTOM",
    "VTA_CENTER",
    "VTA_LEFT",
    "VTA_RIGHT",
    "VTA_TOP",
    "ValidateRect",
    "ValidateRgn",
    "WCRANGE",
    "WGLSWAP",
    "WGL_FONT_LINES",
    "WGL_FONT_POLYGONS",
    "WGL_SWAPMULTIPLE_MAX",
    "WGL_SWAP_MAIN_PLANE",
    "WGL_SWAP_OVERLAY1",
    "WGL_SWAP_OVERLAY10",
    "WGL_SWAP_OVERLAY11",
    "WGL_SWAP_OVERLAY12",
    "WGL_SWAP_OVERLAY13",
    "WGL_SWAP_OVERLAY14",
    "WGL_SWAP_OVERLAY15",
    "WGL_SWAP_OVERLAY2",
    "WGL_SWAP_OVERLAY3",
    "WGL_SWAP_OVERLAY4",
    "WGL_SWAP_OVERLAY5",
    "WGL_SWAP_OVERLAY6",
    "WGL_SWAP_OVERLAY7",
    "WGL_SWAP_OVERLAY8",
    "WGL_SWAP_OVERLAY9",
    "WGL_SWAP_UNDERLAY1",
    "WGL_SWAP_UNDERLAY10",
    "WGL_SWAP_UNDERLAY11",
    "WGL_SWAP_UNDERLAY12",
    "WGL_SWAP_UNDERLAY13",
    "WGL_SWAP_UNDERLAY14",
    "WGL_SWAP_UNDERLAY15",
    "WGL_SWAP_UNDERLAY2",
    "WGL_SWAP_UNDERLAY3",
    "WGL_SWAP_UNDERLAY4",
    "WGL_SWAP_UNDERLAY5",
    "WGL_SWAP_UNDERLAY6",
    "WGL_SWAP_UNDERLAY7",
    "WGL_SWAP_UNDERLAY8",
    "WGL_SWAP_UNDERLAY9",
    "WHITENESS",
    "WHITEONBLACK",
    "WHITE_BRUSH",
    "WHITE_PEN",
    "WINDING",
    "WRITEEMBEDPROC",
    "WidenPath",
    "WindowFromDC",
    "XFORM",
    "wglSwapMultipleBuffers",
]
