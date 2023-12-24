from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer, ConstantLazyLoader
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Globalization
import win32more.Windows.Win32.Graphics.Direct2D.Common
import win32more.Windows.Win32.Graphics.DirectWrite
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.System.Com
DWRITE_ALPHA_MAX: UInt32 = 255
FACILITY_DWRITE: UInt32 = 2200
DWRITE_ERR_BASE: UInt32 = 20480
DWRITE_E_REMOTEFONT: win32more.Windows.Win32.Foundation.HRESULT = -2003283955
DWRITE_E_DOWNLOADCANCELLED: win32more.Windows.Win32.Foundation.HRESULT = -2003283954
DWRITE_E_DOWNLOADFAILED: win32more.Windows.Win32.Foundation.HRESULT = -2003283953
DWRITE_E_TOOMANYDOWNLOADS: win32more.Windows.Win32.Foundation.HRESULT = -2003283952
DWRITE_STANDARD_FONT_AXIS_COUNT: UInt32 = 5
@winfunctype('DWrite.dll')
def DWriteCreateFactory(factoryType: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FACTORY_TYPE, iid: POINTER(Guid), factory: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
DWRITE_AUTOMATIC_FONT_AXES = Int32
DWRITE_AUTOMATIC_FONT_AXES_NONE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_AUTOMATIC_FONT_AXES = 0
DWRITE_AUTOMATIC_FONT_AXES_OPTICAL_SIZE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_AUTOMATIC_FONT_AXES = 1
DWRITE_BASELINE = Int32
DWRITE_BASELINE_DEFAULT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_BASELINE = 0
DWRITE_BASELINE_ROMAN: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_BASELINE = 1
DWRITE_BASELINE_CENTRAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_BASELINE = 2
DWRITE_BASELINE_MATH: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_BASELINE = 3
DWRITE_BASELINE_HANGING: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_BASELINE = 4
DWRITE_BASELINE_IDEOGRAPHIC_BOTTOM: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_BASELINE = 5
DWRITE_BASELINE_IDEOGRAPHIC_TOP: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_BASELINE = 6
DWRITE_BASELINE_MINIMUM: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_BASELINE = 7
DWRITE_BASELINE_MAXIMUM: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_BASELINE = 8
DWRITE_BREAK_CONDITION = Int32
DWRITE_BREAK_CONDITION_NEUTRAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_BREAK_CONDITION = 0
DWRITE_BREAK_CONDITION_CAN_BREAK: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_BREAK_CONDITION = 1
DWRITE_BREAK_CONDITION_MAY_NOT_BREAK: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_BREAK_CONDITION = 2
DWRITE_BREAK_CONDITION_MUST_BREAK: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_BREAK_CONDITION = 3
class DWRITE_CARET_METRICS(EasyCastStructure):
    slopeRise: Int16
    slopeRun: Int16
    offset: Int16
class DWRITE_CLUSTER_METRICS(EasyCastStructure):
    width: Single
    length: UInt16
    _bitfield: UInt16
class DWRITE_COLOR_F(EasyCastStructure):
    r: Single
    g: Single
    b: Single
    a: Single
class DWRITE_COLOR_GLYPH_RUN(EasyCastStructure):
    glyphRun: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_RUN
    glyphRunDescription: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_RUN_DESCRIPTION)
    baselineOriginX: Single
    baselineOriginY: Single
    runColor: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_COLOR_F
    paletteIndex: UInt16
class DWRITE_COLOR_GLYPH_RUN1(EasyCastStructure):
    Base: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_COLOR_GLYPH_RUN
    glyphImageFormat: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_IMAGE_FORMATS
    measuringMode: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MEASURING_MODE
DWRITE_CONTAINER_TYPE = Int32
DWRITE_CONTAINER_TYPE_UNKNOWN: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_CONTAINER_TYPE = 0
DWRITE_CONTAINER_TYPE_WOFF: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_CONTAINER_TYPE = 1
DWRITE_CONTAINER_TYPE_WOFF2: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_CONTAINER_TYPE = 2
DWRITE_FACTORY_TYPE = Int32
DWRITE_FACTORY_TYPE_SHARED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FACTORY_TYPE = 0
DWRITE_FACTORY_TYPE_ISOLATED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FACTORY_TYPE = 1
class DWRITE_FILE_FRAGMENT(EasyCastStructure):
    fileOffset: UInt64
    fragmentSize: UInt64
DWRITE_FLOW_DIRECTION = Int32
DWRITE_FLOW_DIRECTION_TOP_TO_BOTTOM: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FLOW_DIRECTION = 0
DWRITE_FLOW_DIRECTION_BOTTOM_TO_TOP: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FLOW_DIRECTION = 1
DWRITE_FLOW_DIRECTION_LEFT_TO_RIGHT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FLOW_DIRECTION = 2
DWRITE_FLOW_DIRECTION_RIGHT_TO_LEFT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FLOW_DIRECTION = 3
DWRITE_FONT_AXIS_ATTRIBUTES = Int32
DWRITE_FONT_AXIS_ATTRIBUTES_NONE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_ATTRIBUTES = 0
DWRITE_FONT_AXIS_ATTRIBUTES_VARIABLE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_ATTRIBUTES = 1
DWRITE_FONT_AXIS_ATTRIBUTES_HIDDEN: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_ATTRIBUTES = 2
class DWRITE_FONT_AXIS_RANGE(EasyCastStructure):
    axisTag: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_TAG
    minValue: Single
    maxValue: Single
DWRITE_FONT_AXIS_TAG = UInt32
DWRITE_FONT_AXIS_TAG_WEIGHT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_TAG = 1952999287
DWRITE_FONT_AXIS_TAG_WIDTH: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_TAG = 1752458359
DWRITE_FONT_AXIS_TAG_SLANT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_TAG = 1953393779
DWRITE_FONT_AXIS_TAG_OPTICAL_SIZE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_TAG = 2054385775
DWRITE_FONT_AXIS_TAG_ITALIC: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_TAG = 1818326121
class DWRITE_FONT_AXIS_VALUE(EasyCastStructure):
    axisTag: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_TAG
    value: Single
DWRITE_FONT_FACE_TYPE = Int32
DWRITE_FONT_FACE_TYPE_CFF: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FACE_TYPE = 0
DWRITE_FONT_FACE_TYPE_TRUETYPE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FACE_TYPE = 1
DWRITE_FONT_FACE_TYPE_OPENTYPE_COLLECTION: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FACE_TYPE = 2
DWRITE_FONT_FACE_TYPE_TYPE1: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FACE_TYPE = 3
DWRITE_FONT_FACE_TYPE_VECTOR: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FACE_TYPE = 4
DWRITE_FONT_FACE_TYPE_BITMAP: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FACE_TYPE = 5
DWRITE_FONT_FACE_TYPE_UNKNOWN: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FACE_TYPE = 6
DWRITE_FONT_FACE_TYPE_RAW_CFF: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FACE_TYPE = 7
DWRITE_FONT_FACE_TYPE_TRUETYPE_COLLECTION: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FACE_TYPE = 2
DWRITE_FONT_FAMILY_MODEL = Int32
DWRITE_FONT_FAMILY_MODEL_TYPOGRAPHIC: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FAMILY_MODEL = 0
DWRITE_FONT_FAMILY_MODEL_WEIGHT_STRETCH_STYLE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FAMILY_MODEL = 1
class DWRITE_FONT_FEATURE(EasyCastStructure):
    nameTag: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG
    parameter: UInt32
DWRITE_FONT_FEATURE_TAG = UInt32
DWRITE_FONT_FEATURE_TAG_ALTERNATIVE_FRACTIONS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1668441697
DWRITE_FONT_FEATURE_TAG_PETITE_CAPITALS_FROM_CAPITALS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1668297315
DWRITE_FONT_FEATURE_TAG_SMALL_CAPITALS_FROM_CAPITALS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1668493923
DWRITE_FONT_FEATURE_TAG_CONTEXTUAL_ALTERNATES: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1953259875
DWRITE_FONT_FEATURE_TAG_CASE_SENSITIVE_FORMS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1702060387
DWRITE_FONT_FEATURE_TAG_GLYPH_COMPOSITION_DECOMPOSITION: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1886217059
DWRITE_FONT_FEATURE_TAG_CONTEXTUAL_LIGATURES: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1734962275
DWRITE_FONT_FEATURE_TAG_CAPITAL_SPACING: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1886613603
DWRITE_FONT_FEATURE_TAG_CONTEXTUAL_SWASH: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1752658787
DWRITE_FONT_FEATURE_TAG_CURSIVE_POSITIONING: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1936880995
DWRITE_FONT_FEATURE_TAG_DEFAULT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1953261156
DWRITE_FONT_FEATURE_TAG_DISCRETIONARY_LIGATURES: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1734962276
DWRITE_FONT_FEATURE_TAG_EXPERT_FORMS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1953527909
DWRITE_FONT_FEATURE_TAG_FRACTIONS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1667330662
DWRITE_FONT_FEATURE_TAG_FULL_WIDTH: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1684633446
DWRITE_FONT_FEATURE_TAG_HALF_FORMS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1718378856
DWRITE_FONT_FEATURE_TAG_HALANT_FORMS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1852596584
DWRITE_FONT_FEATURE_TAG_ALTERNATE_HALF_WIDTH: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1953259880
DWRITE_FONT_FEATURE_TAG_HISTORICAL_FORMS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1953720680
DWRITE_FONT_FEATURE_TAG_HORIZONTAL_KANA_ALTERNATES: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1634626408
DWRITE_FONT_FEATURE_TAG_HISTORICAL_LIGATURES: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1734962280
DWRITE_FONT_FEATURE_TAG_HALF_WIDTH: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1684633448
DWRITE_FONT_FEATURE_TAG_HOJO_KANJI_FORMS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1869246312
DWRITE_FONT_FEATURE_TAG_JIS04_FORMS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 875589738
DWRITE_FONT_FEATURE_TAG_JIS78_FORMS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 943157354
DWRITE_FONT_FEATURE_TAG_JIS83_FORMS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 859336810
DWRITE_FONT_FEATURE_TAG_JIS90_FORMS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 809070698
DWRITE_FONT_FEATURE_TAG_KERNING: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1852990827
DWRITE_FONT_FEATURE_TAG_STANDARD_LIGATURES: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1634167148
DWRITE_FONT_FEATURE_TAG_LINING_FIGURES: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1836412524
DWRITE_FONT_FEATURE_TAG_LOCALIZED_FORMS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1818455916
DWRITE_FONT_FEATURE_TAG_MARK_POSITIONING: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1802658157
DWRITE_FONT_FEATURE_TAG_MATHEMATICAL_GREEK: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1802659693
DWRITE_FONT_FEATURE_TAG_MARK_TO_MARK_POSITIONING: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1802333037
DWRITE_FONT_FEATURE_TAG_ALTERNATE_ANNOTATION_FORMS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1953259886
DWRITE_FONT_FEATURE_TAG_NLC_KANJI_FORMS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1801677934
DWRITE_FONT_FEATURE_TAG_OLD_STYLE_FIGURES: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1836412527
DWRITE_FONT_FEATURE_TAG_ORDINALS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1852076655
DWRITE_FONT_FEATURE_TAG_PROPORTIONAL_ALTERNATE_WIDTH: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1953259888
DWRITE_FONT_FEATURE_TAG_PETITE_CAPITALS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1885430640
DWRITE_FONT_FEATURE_TAG_PROPORTIONAL_FIGURES: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1836412528
DWRITE_FONT_FEATURE_TAG_PROPORTIONAL_WIDTHS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1684633456
DWRITE_FONT_FEATURE_TAG_QUARTER_WIDTHS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1684633457
DWRITE_FONT_FEATURE_TAG_REQUIRED_LIGATURES: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1734962290
DWRITE_FONT_FEATURE_TAG_RUBY_NOTATION_FORMS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 2036495730
DWRITE_FONT_FEATURE_TAG_STYLISTIC_ALTERNATES: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1953259891
DWRITE_FONT_FEATURE_TAG_SCIENTIFIC_INFERIORS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1718511987
DWRITE_FONT_FEATURE_TAG_SMALL_CAPITALS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1885564275
DWRITE_FONT_FEATURE_TAG_SIMPLIFIED_FORMS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1819307379
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_1: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 825258867
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_2: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 842036083
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_3: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 858813299
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_4: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 875590515
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_5: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 892367731
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_6: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 909144947
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_7: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 925922163
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_8: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 942699379
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_9: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 959476595
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_10: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 808547187
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_11: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 825324403
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_12: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 842101619
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_13: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 858878835
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_14: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 875656051
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_15: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 892433267
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_16: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 909210483
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_17: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 925987699
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_18: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 942764915
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_19: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 959542131
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_20: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 808612723
DWRITE_FONT_FEATURE_TAG_SUBSCRIPT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1935832435
DWRITE_FONT_FEATURE_TAG_SUPERSCRIPT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1936749939
DWRITE_FONT_FEATURE_TAG_SWASH: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1752397683
DWRITE_FONT_FEATURE_TAG_TITLING: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1819568500
DWRITE_FONT_FEATURE_TAG_TRADITIONAL_NAME_FORMS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1835101812
DWRITE_FONT_FEATURE_TAG_TABULAR_FIGURES: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1836412532
DWRITE_FONT_FEATURE_TAG_TRADITIONAL_FORMS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1684107892
DWRITE_FONT_FEATURE_TAG_THIRD_WIDTHS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1684633460
DWRITE_FONT_FEATURE_TAG_UNICASE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1667853941
DWRITE_FONT_FEATURE_TAG_VERTICAL_WRITING: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1953654134
DWRITE_FONT_FEATURE_TAG_VERTICAL_ALTERNATES_AND_ROTATION: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 846492278
DWRITE_FONT_FEATURE_TAG_SLASHED_ZERO: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG = 1869768058
DWRITE_FONT_FILE_TYPE = Int32
DWRITE_FONT_FILE_TYPE_UNKNOWN: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FILE_TYPE = 0
DWRITE_FONT_FILE_TYPE_CFF: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FILE_TYPE = 1
DWRITE_FONT_FILE_TYPE_TRUETYPE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FILE_TYPE = 2
DWRITE_FONT_FILE_TYPE_OPENTYPE_COLLECTION: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FILE_TYPE = 3
DWRITE_FONT_FILE_TYPE_TYPE1_PFM: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FILE_TYPE = 4
DWRITE_FONT_FILE_TYPE_TYPE1_PFB: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FILE_TYPE = 5
DWRITE_FONT_FILE_TYPE_VECTOR: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FILE_TYPE = 6
DWRITE_FONT_FILE_TYPE_BITMAP: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FILE_TYPE = 7
DWRITE_FONT_FILE_TYPE_TRUETYPE_COLLECTION: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FILE_TYPE = 3
DWRITE_FONT_LINE_GAP_USAGE = Int32
DWRITE_FONT_LINE_GAP_USAGE_DEFAULT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_LINE_GAP_USAGE = 0
DWRITE_FONT_LINE_GAP_USAGE_DISABLED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_LINE_GAP_USAGE = 1
DWRITE_FONT_LINE_GAP_USAGE_ENABLED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_LINE_GAP_USAGE = 2
class DWRITE_FONT_METRICS(EasyCastStructure):
    designUnitsPerEm: UInt16
    ascent: UInt16
    descent: UInt16
    lineGap: Int16
    capHeight: UInt16
    xHeight: UInt16
    underlinePosition: Int16
    underlineThickness: UInt16
    strikethroughPosition: Int16
    strikethroughThickness: UInt16
class DWRITE_FONT_METRICS1(EasyCastStructure):
    Base: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_METRICS
    glyphBoxLeft: Int16
    glyphBoxTop: Int16
    glyphBoxRight: Int16
    glyphBoxBottom: Int16
    subscriptPositionX: Int16
    subscriptPositionY: Int16
    subscriptSizeX: Int16
    subscriptSizeY: Int16
    superscriptPositionX: Int16
    superscriptPositionY: Int16
    superscriptSizeX: Int16
    superscriptSizeY: Int16
    hasTypographicMetrics: win32more.Windows.Win32.Foundation.BOOL
class DWRITE_FONT_PROPERTY(EasyCastStructure):
    propertyId: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_PROPERTY_ID
    propertyValue: win32more.Windows.Win32.Foundation.PWSTR
    localeName: win32more.Windows.Win32.Foundation.PWSTR
DWRITE_FONT_PROPERTY_ID = Int32
DWRITE_FONT_PROPERTY_ID_NONE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_PROPERTY_ID = 0
DWRITE_FONT_PROPERTY_ID_WEIGHT_STRETCH_STYLE_FAMILY_NAME: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_PROPERTY_ID = 1
DWRITE_FONT_PROPERTY_ID_TYPOGRAPHIC_FAMILY_NAME: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_PROPERTY_ID = 2
DWRITE_FONT_PROPERTY_ID_WEIGHT_STRETCH_STYLE_FACE_NAME: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_PROPERTY_ID = 3
DWRITE_FONT_PROPERTY_ID_FULL_NAME: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_PROPERTY_ID = 4
DWRITE_FONT_PROPERTY_ID_WIN32_FAMILY_NAME: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_PROPERTY_ID = 5
DWRITE_FONT_PROPERTY_ID_POSTSCRIPT_NAME: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_PROPERTY_ID = 6
DWRITE_FONT_PROPERTY_ID_DESIGN_SCRIPT_LANGUAGE_TAG: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_PROPERTY_ID = 7
DWRITE_FONT_PROPERTY_ID_SUPPORTED_SCRIPT_LANGUAGE_TAG: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_PROPERTY_ID = 8
DWRITE_FONT_PROPERTY_ID_SEMANTIC_TAG: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_PROPERTY_ID = 9
DWRITE_FONT_PROPERTY_ID_WEIGHT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_PROPERTY_ID = 10
DWRITE_FONT_PROPERTY_ID_STRETCH: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_PROPERTY_ID = 11
DWRITE_FONT_PROPERTY_ID_STYLE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_PROPERTY_ID = 12
DWRITE_FONT_PROPERTY_ID_TYPOGRAPHIC_FACE_NAME: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_PROPERTY_ID = 13
DWRITE_FONT_PROPERTY_ID_TOTAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_PROPERTY_ID = 13
DWRITE_FONT_PROPERTY_ID_TOTAL_RS3: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_PROPERTY_ID = 14
DWRITE_FONT_PROPERTY_ID_PREFERRED_FAMILY_NAME: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_PROPERTY_ID = 2
DWRITE_FONT_PROPERTY_ID_FAMILY_NAME: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_PROPERTY_ID = 1
DWRITE_FONT_PROPERTY_ID_FACE_NAME: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_PROPERTY_ID = 3
DWRITE_FONT_SIMULATIONS = Int32
DWRITE_FONT_SIMULATIONS_NONE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_SIMULATIONS = 0
DWRITE_FONT_SIMULATIONS_BOLD: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_SIMULATIONS = 1
DWRITE_FONT_SIMULATIONS_OBLIQUE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_SIMULATIONS = 2
DWRITE_FONT_SOURCE_TYPE = Int32
DWRITE_FONT_SOURCE_TYPE_UNKNOWN: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_SOURCE_TYPE = 0
DWRITE_FONT_SOURCE_TYPE_PER_MACHINE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_SOURCE_TYPE = 1
DWRITE_FONT_SOURCE_TYPE_PER_USER: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_SOURCE_TYPE = 2
DWRITE_FONT_SOURCE_TYPE_APPX_PACKAGE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_SOURCE_TYPE = 3
DWRITE_FONT_SOURCE_TYPE_REMOTE_FONT_PROVIDER: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_SOURCE_TYPE = 4
DWRITE_FONT_STRETCH = Int32
DWRITE_FONT_STRETCH_UNDEFINED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STRETCH = 0
DWRITE_FONT_STRETCH_ULTRA_CONDENSED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STRETCH = 1
DWRITE_FONT_STRETCH_EXTRA_CONDENSED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STRETCH = 2
DWRITE_FONT_STRETCH_CONDENSED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STRETCH = 3
DWRITE_FONT_STRETCH_SEMI_CONDENSED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STRETCH = 4
DWRITE_FONT_STRETCH_NORMAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STRETCH = 5
DWRITE_FONT_STRETCH_MEDIUM: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STRETCH = 5
DWRITE_FONT_STRETCH_SEMI_EXPANDED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STRETCH = 6
DWRITE_FONT_STRETCH_EXPANDED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STRETCH = 7
DWRITE_FONT_STRETCH_EXTRA_EXPANDED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STRETCH = 8
DWRITE_FONT_STRETCH_ULTRA_EXPANDED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STRETCH = 9
DWRITE_FONT_STYLE = Int32
DWRITE_FONT_STYLE_NORMAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STYLE = 0
DWRITE_FONT_STYLE_OBLIQUE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STYLE = 1
DWRITE_FONT_STYLE_ITALIC: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STYLE = 2
DWRITE_FONT_WEIGHT = Int32
DWRITE_FONT_WEIGHT_THIN: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_WEIGHT = 100
DWRITE_FONT_WEIGHT_EXTRA_LIGHT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_WEIGHT = 200
DWRITE_FONT_WEIGHT_ULTRA_LIGHT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_WEIGHT = 200
DWRITE_FONT_WEIGHT_LIGHT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_WEIGHT = 300
DWRITE_FONT_WEIGHT_SEMI_LIGHT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_WEIGHT = 350
DWRITE_FONT_WEIGHT_NORMAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_WEIGHT = 400
DWRITE_FONT_WEIGHT_REGULAR: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_WEIGHT = 400
DWRITE_FONT_WEIGHT_MEDIUM: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_WEIGHT = 500
DWRITE_FONT_WEIGHT_DEMI_BOLD: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_WEIGHT = 600
DWRITE_FONT_WEIGHT_SEMI_BOLD: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_WEIGHT = 600
DWRITE_FONT_WEIGHT_BOLD: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_WEIGHT = 700
DWRITE_FONT_WEIGHT_EXTRA_BOLD: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_WEIGHT = 800
DWRITE_FONT_WEIGHT_ULTRA_BOLD: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_WEIGHT = 800
DWRITE_FONT_WEIGHT_BLACK: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_WEIGHT = 900
DWRITE_FONT_WEIGHT_HEAVY: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_WEIGHT = 900
DWRITE_FONT_WEIGHT_EXTRA_BLACK: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_WEIGHT = 950
DWRITE_FONT_WEIGHT_ULTRA_BLACK: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_WEIGHT = 950
class DWRITE_GLYPH_IMAGE_DATA(EasyCastStructure):
    imageData: VoidPtr
    imageDataSize: UInt32
    uniqueDataId: UInt32
    pixelsPerEm: UInt32
    pixelSize: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D_SIZE_U
    horizontalLeftOrigin: win32more.Windows.Win32.Foundation.POINT
    horizontalRightOrigin: win32more.Windows.Win32.Foundation.POINT
    verticalTopOrigin: win32more.Windows.Win32.Foundation.POINT
    verticalBottomOrigin: win32more.Windows.Win32.Foundation.POINT
DWRITE_GLYPH_IMAGE_FORMATS = Int32
DWRITE_GLYPH_IMAGE_FORMATS_NONE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_IMAGE_FORMATS = 0
DWRITE_GLYPH_IMAGE_FORMATS_TRUETYPE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_IMAGE_FORMATS = 1
DWRITE_GLYPH_IMAGE_FORMATS_CFF: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_IMAGE_FORMATS = 2
DWRITE_GLYPH_IMAGE_FORMATS_COLR: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_IMAGE_FORMATS = 4
DWRITE_GLYPH_IMAGE_FORMATS_SVG: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_IMAGE_FORMATS = 8
DWRITE_GLYPH_IMAGE_FORMATS_PNG: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_IMAGE_FORMATS = 16
DWRITE_GLYPH_IMAGE_FORMATS_JPEG: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_IMAGE_FORMATS = 32
DWRITE_GLYPH_IMAGE_FORMATS_TIFF: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_IMAGE_FORMATS = 64
DWRITE_GLYPH_IMAGE_FORMATS_PREMULTIPLIED_B8G8R8A8: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_IMAGE_FORMATS = 128
class DWRITE_GLYPH_METRICS(EasyCastStructure):
    leftSideBearing: Int32
    advanceWidth: UInt32
    rightSideBearing: Int32
    topSideBearing: Int32
    advanceHeight: UInt32
    bottomSideBearing: Int32
    verticalOriginY: Int32
class DWRITE_GLYPH_OFFSET(EasyCastStructure):
    advanceOffset: Single
    ascenderOffset: Single
DWRITE_GLYPH_ORIENTATION_ANGLE = Int32
DWRITE_GLYPH_ORIENTATION_ANGLE_0_DEGREES: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_ORIENTATION_ANGLE = 0
DWRITE_GLYPH_ORIENTATION_ANGLE_90_DEGREES: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_ORIENTATION_ANGLE = 1
DWRITE_GLYPH_ORIENTATION_ANGLE_180_DEGREES: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_ORIENTATION_ANGLE = 2
DWRITE_GLYPH_ORIENTATION_ANGLE_270_DEGREES: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_ORIENTATION_ANGLE = 3
class DWRITE_GLYPH_RUN(EasyCastStructure):
    fontFace: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFace
    fontEmSize: Single
    glyphCount: UInt32
    glyphIndices: POINTER(UInt16)
    glyphAdvances: POINTER(Single)
    glyphOffsets: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_OFFSET)
    isSideways: win32more.Windows.Win32.Foundation.BOOL
    bidiLevel: UInt32
class DWRITE_GLYPH_RUN_DESCRIPTION(EasyCastStructure):
    localeName: win32more.Windows.Win32.Foundation.PWSTR
    string: win32more.Windows.Win32.Foundation.PWSTR
    stringLength: UInt32
    clusterMap: POINTER(UInt16)
    textPosition: UInt32
DWRITE_GRID_FIT_MODE = Int32
DWRITE_GRID_FIT_MODE_DEFAULT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GRID_FIT_MODE = 0
DWRITE_GRID_FIT_MODE_DISABLED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GRID_FIT_MODE = 1
DWRITE_GRID_FIT_MODE_ENABLED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GRID_FIT_MODE = 2
class DWRITE_HIT_TEST_METRICS(EasyCastStructure):
    textPosition: UInt32
    length: UInt32
    left: Single
    top: Single
    width: Single
    height: Single
    bidiLevel: UInt32
    isText: win32more.Windows.Win32.Foundation.BOOL
    isTrimmed: win32more.Windows.Win32.Foundation.BOOL
DWRITE_INFORMATIONAL_STRING_ID = Int32
DWRITE_INFORMATIONAL_STRING_NONE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_INFORMATIONAL_STRING_ID = 0
DWRITE_INFORMATIONAL_STRING_COPYRIGHT_NOTICE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_INFORMATIONAL_STRING_ID = 1
DWRITE_INFORMATIONAL_STRING_VERSION_STRINGS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_INFORMATIONAL_STRING_ID = 2
DWRITE_INFORMATIONAL_STRING_TRADEMARK: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_INFORMATIONAL_STRING_ID = 3
DWRITE_INFORMATIONAL_STRING_MANUFACTURER: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_INFORMATIONAL_STRING_ID = 4
DWRITE_INFORMATIONAL_STRING_DESIGNER: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_INFORMATIONAL_STRING_ID = 5
DWRITE_INFORMATIONAL_STRING_DESIGNER_URL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_INFORMATIONAL_STRING_ID = 6
DWRITE_INFORMATIONAL_STRING_DESCRIPTION: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_INFORMATIONAL_STRING_ID = 7
DWRITE_INFORMATIONAL_STRING_FONT_VENDOR_URL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_INFORMATIONAL_STRING_ID = 8
DWRITE_INFORMATIONAL_STRING_LICENSE_DESCRIPTION: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_INFORMATIONAL_STRING_ID = 9
DWRITE_INFORMATIONAL_STRING_LICENSE_INFO_URL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_INFORMATIONAL_STRING_ID = 10
DWRITE_INFORMATIONAL_STRING_WIN32_FAMILY_NAMES: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_INFORMATIONAL_STRING_ID = 11
DWRITE_INFORMATIONAL_STRING_WIN32_SUBFAMILY_NAMES: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_INFORMATIONAL_STRING_ID = 12
DWRITE_INFORMATIONAL_STRING_TYPOGRAPHIC_FAMILY_NAMES: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_INFORMATIONAL_STRING_ID = 13
DWRITE_INFORMATIONAL_STRING_TYPOGRAPHIC_SUBFAMILY_NAMES: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_INFORMATIONAL_STRING_ID = 14
DWRITE_INFORMATIONAL_STRING_SAMPLE_TEXT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_INFORMATIONAL_STRING_ID = 15
DWRITE_INFORMATIONAL_STRING_FULL_NAME: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_INFORMATIONAL_STRING_ID = 16
DWRITE_INFORMATIONAL_STRING_POSTSCRIPT_NAME: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_INFORMATIONAL_STRING_ID = 17
DWRITE_INFORMATIONAL_STRING_POSTSCRIPT_CID_NAME: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_INFORMATIONAL_STRING_ID = 18
DWRITE_INFORMATIONAL_STRING_WEIGHT_STRETCH_STYLE_FAMILY_NAME: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_INFORMATIONAL_STRING_ID = 19
DWRITE_INFORMATIONAL_STRING_DESIGN_SCRIPT_LANGUAGE_TAG: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_INFORMATIONAL_STRING_ID = 20
DWRITE_INFORMATIONAL_STRING_SUPPORTED_SCRIPT_LANGUAGE_TAG: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_INFORMATIONAL_STRING_ID = 21
DWRITE_INFORMATIONAL_STRING_PREFERRED_FAMILY_NAMES: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_INFORMATIONAL_STRING_ID = 13
DWRITE_INFORMATIONAL_STRING_PREFERRED_SUBFAMILY_NAMES: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_INFORMATIONAL_STRING_ID = 14
DWRITE_INFORMATIONAL_STRING_WWS_FAMILY_NAME: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_INFORMATIONAL_STRING_ID = 19
class DWRITE_INLINE_OBJECT_METRICS(EasyCastStructure):
    width: Single
    height: Single
    baseline: Single
    supportsSideways: win32more.Windows.Win32.Foundation.BOOL
class DWRITE_JUSTIFICATION_OPPORTUNITY(EasyCastStructure):
    expansionMinimum: Single
    expansionMaximum: Single
    compressionMaximum: Single
    _bitfield: UInt32
class DWRITE_LINE_BREAKPOINT(EasyCastStructure):
    _bitfield: Byte
class DWRITE_LINE_METRICS(EasyCastStructure):
    length: UInt32
    trailingWhitespaceLength: UInt32
    newlineLength: UInt32
    height: Single
    baseline: Single
    isTrimmed: win32more.Windows.Win32.Foundation.BOOL
class DWRITE_LINE_METRICS1(EasyCastStructure):
    Base: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_LINE_METRICS
    leadingBefore: Single
    leadingAfter: Single
class DWRITE_LINE_SPACING(EasyCastStructure):
    method: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_LINE_SPACING_METHOD
    height: Single
    baseline: Single
    leadingBefore: Single
    fontLineGapUsage: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_LINE_GAP_USAGE
DWRITE_LINE_SPACING_METHOD = Int32
DWRITE_LINE_SPACING_METHOD_DEFAULT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_LINE_SPACING_METHOD = 0
DWRITE_LINE_SPACING_METHOD_UNIFORM: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_LINE_SPACING_METHOD = 1
DWRITE_LINE_SPACING_METHOD_PROPORTIONAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_LINE_SPACING_METHOD = 2
DWRITE_LOCALITY = Int32
DWRITE_LOCALITY_REMOTE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_LOCALITY = 0
DWRITE_LOCALITY_PARTIAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_LOCALITY = 1
DWRITE_LOCALITY_LOCAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_LOCALITY = 2
class DWRITE_MATRIX(EasyCastStructure):
    m11: Single
    m12: Single
    m21: Single
    m22: Single
    dx: Single
    dy: Single
DWRITE_MEASURING_MODE = Int32
DWRITE_MEASURING_MODE_NATURAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MEASURING_MODE = 0
DWRITE_MEASURING_MODE_GDI_CLASSIC: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MEASURING_MODE = 1
DWRITE_MEASURING_MODE_GDI_NATURAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MEASURING_MODE = 2
DWRITE_NUMBER_SUBSTITUTION_METHOD = Int32
DWRITE_NUMBER_SUBSTITUTION_METHOD_FROM_CULTURE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_NUMBER_SUBSTITUTION_METHOD = 0
DWRITE_NUMBER_SUBSTITUTION_METHOD_CONTEXTUAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_NUMBER_SUBSTITUTION_METHOD = 1
DWRITE_NUMBER_SUBSTITUTION_METHOD_NONE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_NUMBER_SUBSTITUTION_METHOD = 2
DWRITE_NUMBER_SUBSTITUTION_METHOD_NATIONAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_NUMBER_SUBSTITUTION_METHOD = 3
DWRITE_NUMBER_SUBSTITUTION_METHOD_TRADITIONAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_NUMBER_SUBSTITUTION_METHOD = 4
DWRITE_OPTICAL_ALIGNMENT = Int32
DWRITE_OPTICAL_ALIGNMENT_NONE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_OPTICAL_ALIGNMENT = 0
DWRITE_OPTICAL_ALIGNMENT_NO_SIDE_BEARINGS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_OPTICAL_ALIGNMENT = 1
DWRITE_OUTLINE_THRESHOLD = Int32
DWRITE_OUTLINE_THRESHOLD_ANTIALIASED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_OUTLINE_THRESHOLD = 0
DWRITE_OUTLINE_THRESHOLD_ALIASED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_OUTLINE_THRESHOLD = 1
class DWRITE_OVERHANG_METRICS(EasyCastStructure):
    left: Single
    top: Single
    right: Single
    bottom: Single
class DWRITE_PANOSE(EasyCastUnion):
    values: Byte * 10
    familyKind: Byte
    text: _text_e__Struct
    script: _script_e__Struct
    decorative: _decorative_e__Struct
    symbol: _symbol_e__Struct
    class _text_e__Struct(EasyCastStructure):
        familyKind: Byte
        serifStyle: Byte
        weight: Byte
        proportion: Byte
        contrast: Byte
        strokeVariation: Byte
        armStyle: Byte
        letterform: Byte
        midline: Byte
        xHeight: Byte
    class _script_e__Struct(EasyCastStructure):
        familyKind: Byte
        toolKind: Byte
        weight: Byte
        spacing: Byte
        aspectRatio: Byte
        contrast: Byte
        scriptTopology: Byte
        scriptForm: Byte
        finials: Byte
        xAscent: Byte
    class _decorative_e__Struct(EasyCastStructure):
        familyKind: Byte
        decorativeClass: Byte
        weight: Byte
        aspect: Byte
        contrast: Byte
        serifVariant: Byte
        fill: Byte
        lining: Byte
        decorativeTopology: Byte
        characterRange: Byte
    class _symbol_e__Struct(EasyCastStructure):
        familyKind: Byte
        symbolKind: Byte
        weight: Byte
        spacing: Byte
        aspectRatioAndContrast: Byte
        aspectRatio94: Byte
        aspectRatio119: Byte
        aspectRatio157: Byte
        aspectRatio163: Byte
        aspectRatio211: Byte
DWRITE_PANOSE_ARM_STYLE = Int32
DWRITE_PANOSE_ARM_STYLE_ANY: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ARM_STYLE = 0
DWRITE_PANOSE_ARM_STYLE_NO_FIT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ARM_STYLE = 1
DWRITE_PANOSE_ARM_STYLE_STRAIGHT_ARMS_HORIZONTAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ARM_STYLE = 2
DWRITE_PANOSE_ARM_STYLE_STRAIGHT_ARMS_WEDGE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ARM_STYLE = 3
DWRITE_PANOSE_ARM_STYLE_STRAIGHT_ARMS_VERTICAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ARM_STYLE = 4
DWRITE_PANOSE_ARM_STYLE_STRAIGHT_ARMS_SINGLE_SERIF: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ARM_STYLE = 5
DWRITE_PANOSE_ARM_STYLE_STRAIGHT_ARMS_DOUBLE_SERIF: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ARM_STYLE = 6
DWRITE_PANOSE_ARM_STYLE_NONSTRAIGHT_ARMS_HORIZONTAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ARM_STYLE = 7
DWRITE_PANOSE_ARM_STYLE_NONSTRAIGHT_ARMS_WEDGE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ARM_STYLE = 8
DWRITE_PANOSE_ARM_STYLE_NONSTRAIGHT_ARMS_VERTICAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ARM_STYLE = 9
DWRITE_PANOSE_ARM_STYLE_NONSTRAIGHT_ARMS_SINGLE_SERIF: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ARM_STYLE = 10
DWRITE_PANOSE_ARM_STYLE_NONSTRAIGHT_ARMS_DOUBLE_SERIF: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ARM_STYLE = 11
DWRITE_PANOSE_ARM_STYLE_STRAIGHT_ARMS_HORZ: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ARM_STYLE = 2
DWRITE_PANOSE_ARM_STYLE_STRAIGHT_ARMS_VERT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ARM_STYLE = 4
DWRITE_PANOSE_ARM_STYLE_BENT_ARMS_HORZ: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ARM_STYLE = 7
DWRITE_PANOSE_ARM_STYLE_BENT_ARMS_WEDGE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ARM_STYLE = 8
DWRITE_PANOSE_ARM_STYLE_BENT_ARMS_VERT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ARM_STYLE = 9
DWRITE_PANOSE_ARM_STYLE_BENT_ARMS_SINGLE_SERIF: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ARM_STYLE = 10
DWRITE_PANOSE_ARM_STYLE_BENT_ARMS_DOUBLE_SERIF: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ARM_STYLE = 11
DWRITE_PANOSE_ASPECT = Int32
DWRITE_PANOSE_ASPECT_ANY: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ASPECT = 0
DWRITE_PANOSE_ASPECT_NO_FIT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ASPECT = 1
DWRITE_PANOSE_ASPECT_SUPER_CONDENSED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ASPECT = 2
DWRITE_PANOSE_ASPECT_VERY_CONDENSED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ASPECT = 3
DWRITE_PANOSE_ASPECT_CONDENSED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ASPECT = 4
DWRITE_PANOSE_ASPECT_NORMAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ASPECT = 5
DWRITE_PANOSE_ASPECT_EXTENDED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ASPECT = 6
DWRITE_PANOSE_ASPECT_VERY_EXTENDED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ASPECT = 7
DWRITE_PANOSE_ASPECT_SUPER_EXTENDED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ASPECT = 8
DWRITE_PANOSE_ASPECT_MONOSPACED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ASPECT = 9
DWRITE_PANOSE_ASPECT_RATIO = Int32
DWRITE_PANOSE_ASPECT_RATIO_ANY: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ASPECT_RATIO = 0
DWRITE_PANOSE_ASPECT_RATIO_NO_FIT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ASPECT_RATIO = 1
DWRITE_PANOSE_ASPECT_RATIO_VERY_CONDENSED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ASPECT_RATIO = 2
DWRITE_PANOSE_ASPECT_RATIO_CONDENSED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ASPECT_RATIO = 3
DWRITE_PANOSE_ASPECT_RATIO_NORMAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ASPECT_RATIO = 4
DWRITE_PANOSE_ASPECT_RATIO_EXPANDED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ASPECT_RATIO = 5
DWRITE_PANOSE_ASPECT_RATIO_VERY_EXPANDED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_ASPECT_RATIO = 6
DWRITE_PANOSE_CHARACTER_RANGES = Int32
DWRITE_PANOSE_CHARACTER_RANGES_ANY: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_CHARACTER_RANGES = 0
DWRITE_PANOSE_CHARACTER_RANGES_NO_FIT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_CHARACTER_RANGES = 1
DWRITE_PANOSE_CHARACTER_RANGES_EXTENDED_COLLECTION: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_CHARACTER_RANGES = 2
DWRITE_PANOSE_CHARACTER_RANGES_LITERALS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_CHARACTER_RANGES = 3
DWRITE_PANOSE_CHARACTER_RANGES_NO_LOWER_CASE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_CHARACTER_RANGES = 4
DWRITE_PANOSE_CHARACTER_RANGES_SMALL_CAPS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_CHARACTER_RANGES = 5
DWRITE_PANOSE_CONTRAST = Int32
DWRITE_PANOSE_CONTRAST_ANY: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_CONTRAST = 0
DWRITE_PANOSE_CONTRAST_NO_FIT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_CONTRAST = 1
DWRITE_PANOSE_CONTRAST_NONE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_CONTRAST = 2
DWRITE_PANOSE_CONTRAST_VERY_LOW: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_CONTRAST = 3
DWRITE_PANOSE_CONTRAST_LOW: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_CONTRAST = 4
DWRITE_PANOSE_CONTRAST_MEDIUM_LOW: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_CONTRAST = 5
DWRITE_PANOSE_CONTRAST_MEDIUM: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_CONTRAST = 6
DWRITE_PANOSE_CONTRAST_MEDIUM_HIGH: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_CONTRAST = 7
DWRITE_PANOSE_CONTRAST_HIGH: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_CONTRAST = 8
DWRITE_PANOSE_CONTRAST_VERY_HIGH: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_CONTRAST = 9
DWRITE_PANOSE_CONTRAST_HORIZONTAL_LOW: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_CONTRAST = 10
DWRITE_PANOSE_CONTRAST_HORIZONTAL_MEDIUM: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_CONTRAST = 11
DWRITE_PANOSE_CONTRAST_HORIZONTAL_HIGH: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_CONTRAST = 12
DWRITE_PANOSE_CONTRAST_BROKEN: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_CONTRAST = 13
DWRITE_PANOSE_DECORATIVE_CLASS = Int32
DWRITE_PANOSE_DECORATIVE_CLASS_ANY: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_DECORATIVE_CLASS = 0
DWRITE_PANOSE_DECORATIVE_CLASS_NO_FIT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_DECORATIVE_CLASS = 1
DWRITE_PANOSE_DECORATIVE_CLASS_DERIVATIVE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_DECORATIVE_CLASS = 2
DWRITE_PANOSE_DECORATIVE_CLASS_NONSTANDARD_TOPOLOGY: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_DECORATIVE_CLASS = 3
DWRITE_PANOSE_DECORATIVE_CLASS_NONSTANDARD_ELEMENTS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_DECORATIVE_CLASS = 4
DWRITE_PANOSE_DECORATIVE_CLASS_NONSTANDARD_ASPECT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_DECORATIVE_CLASS = 5
DWRITE_PANOSE_DECORATIVE_CLASS_INITIALS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_DECORATIVE_CLASS = 6
DWRITE_PANOSE_DECORATIVE_CLASS_CARTOON: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_DECORATIVE_CLASS = 7
DWRITE_PANOSE_DECORATIVE_CLASS_PICTURE_STEMS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_DECORATIVE_CLASS = 8
DWRITE_PANOSE_DECORATIVE_CLASS_ORNAMENTED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_DECORATIVE_CLASS = 9
DWRITE_PANOSE_DECORATIVE_CLASS_TEXT_AND_BACKGROUND: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_DECORATIVE_CLASS = 10
DWRITE_PANOSE_DECORATIVE_CLASS_COLLAGE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_DECORATIVE_CLASS = 11
DWRITE_PANOSE_DECORATIVE_CLASS_MONTAGE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_DECORATIVE_CLASS = 12
DWRITE_PANOSE_DECORATIVE_TOPOLOGY = Int32
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_ANY: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_DECORATIVE_TOPOLOGY = 0
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_NO_FIT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_DECORATIVE_TOPOLOGY = 1
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_STANDARD: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_DECORATIVE_TOPOLOGY = 2
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_SQUARE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_DECORATIVE_TOPOLOGY = 3
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_MULTIPLE_SEGMENT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_DECORATIVE_TOPOLOGY = 4
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_ART_DECO: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_DECORATIVE_TOPOLOGY = 5
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_UNEVEN_WEIGHTING: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_DECORATIVE_TOPOLOGY = 6
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_DIVERSE_ARMS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_DECORATIVE_TOPOLOGY = 7
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_DIVERSE_FORMS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_DECORATIVE_TOPOLOGY = 8
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_LOMBARDIC_FORMS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_DECORATIVE_TOPOLOGY = 9
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_UPPER_CASE_IN_LOWER_CASE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_DECORATIVE_TOPOLOGY = 10
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_IMPLIED_TOPOLOGY: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_DECORATIVE_TOPOLOGY = 11
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_HORSESHOE_E_AND_A: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_DECORATIVE_TOPOLOGY = 12
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_CURSIVE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_DECORATIVE_TOPOLOGY = 13
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_BLACKLETTER: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_DECORATIVE_TOPOLOGY = 14
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_SWASH_VARIANCE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_DECORATIVE_TOPOLOGY = 15
DWRITE_PANOSE_FAMILY = Int32
DWRITE_PANOSE_FAMILY_ANY: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_FAMILY = 0
DWRITE_PANOSE_FAMILY_NO_FIT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_FAMILY = 1
DWRITE_PANOSE_FAMILY_TEXT_DISPLAY: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_FAMILY = 2
DWRITE_PANOSE_FAMILY_SCRIPT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_FAMILY = 3
DWRITE_PANOSE_FAMILY_DECORATIVE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_FAMILY = 4
DWRITE_PANOSE_FAMILY_SYMBOL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_FAMILY = 5
DWRITE_PANOSE_FAMILY_PICTORIAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_FAMILY = 5
DWRITE_PANOSE_FILL = Int32
DWRITE_PANOSE_FILL_ANY: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_FILL = 0
DWRITE_PANOSE_FILL_NO_FIT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_FILL = 1
DWRITE_PANOSE_FILL_STANDARD_SOLID_FILL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_FILL = 2
DWRITE_PANOSE_FILL_NO_FILL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_FILL = 3
DWRITE_PANOSE_FILL_PATTERNED_FILL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_FILL = 4
DWRITE_PANOSE_FILL_COMPLEX_FILL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_FILL = 5
DWRITE_PANOSE_FILL_SHAPED_FILL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_FILL = 6
DWRITE_PANOSE_FILL_DRAWN_DISTRESSED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_FILL = 7
DWRITE_PANOSE_FINIALS = Int32
DWRITE_PANOSE_FINIALS_ANY: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_FINIALS = 0
DWRITE_PANOSE_FINIALS_NO_FIT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_FINIALS = 1
DWRITE_PANOSE_FINIALS_NONE_NO_LOOPS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_FINIALS = 2
DWRITE_PANOSE_FINIALS_NONE_CLOSED_LOOPS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_FINIALS = 3
DWRITE_PANOSE_FINIALS_NONE_OPEN_LOOPS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_FINIALS = 4
DWRITE_PANOSE_FINIALS_SHARP_NO_LOOPS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_FINIALS = 5
DWRITE_PANOSE_FINIALS_SHARP_CLOSED_LOOPS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_FINIALS = 6
DWRITE_PANOSE_FINIALS_SHARP_OPEN_LOOPS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_FINIALS = 7
DWRITE_PANOSE_FINIALS_TAPERED_NO_LOOPS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_FINIALS = 8
DWRITE_PANOSE_FINIALS_TAPERED_CLOSED_LOOPS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_FINIALS = 9
DWRITE_PANOSE_FINIALS_TAPERED_OPEN_LOOPS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_FINIALS = 10
DWRITE_PANOSE_FINIALS_ROUND_NO_LOOPS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_FINIALS = 11
DWRITE_PANOSE_FINIALS_ROUND_CLOSED_LOOPS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_FINIALS = 12
DWRITE_PANOSE_FINIALS_ROUND_OPEN_LOOPS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_FINIALS = 13
DWRITE_PANOSE_LETTERFORM = Int32
DWRITE_PANOSE_LETTERFORM_ANY: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_LETTERFORM = 0
DWRITE_PANOSE_LETTERFORM_NO_FIT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_LETTERFORM = 1
DWRITE_PANOSE_LETTERFORM_NORMAL_CONTACT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_LETTERFORM = 2
DWRITE_PANOSE_LETTERFORM_NORMAL_WEIGHTED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_LETTERFORM = 3
DWRITE_PANOSE_LETTERFORM_NORMAL_BOXED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_LETTERFORM = 4
DWRITE_PANOSE_LETTERFORM_NORMAL_FLATTENED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_LETTERFORM = 5
DWRITE_PANOSE_LETTERFORM_NORMAL_ROUNDED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_LETTERFORM = 6
DWRITE_PANOSE_LETTERFORM_NORMAL_OFF_CENTER: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_LETTERFORM = 7
DWRITE_PANOSE_LETTERFORM_NORMAL_SQUARE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_LETTERFORM = 8
DWRITE_PANOSE_LETTERFORM_OBLIQUE_CONTACT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_LETTERFORM = 9
DWRITE_PANOSE_LETTERFORM_OBLIQUE_WEIGHTED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_LETTERFORM = 10
DWRITE_PANOSE_LETTERFORM_OBLIQUE_BOXED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_LETTERFORM = 11
DWRITE_PANOSE_LETTERFORM_OBLIQUE_FLATTENED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_LETTERFORM = 12
DWRITE_PANOSE_LETTERFORM_OBLIQUE_ROUNDED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_LETTERFORM = 13
DWRITE_PANOSE_LETTERFORM_OBLIQUE_OFF_CENTER: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_LETTERFORM = 14
DWRITE_PANOSE_LETTERFORM_OBLIQUE_SQUARE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_LETTERFORM = 15
DWRITE_PANOSE_LINING = Int32
DWRITE_PANOSE_LINING_ANY: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_LINING = 0
DWRITE_PANOSE_LINING_NO_FIT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_LINING = 1
DWRITE_PANOSE_LINING_NONE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_LINING = 2
DWRITE_PANOSE_LINING_INLINE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_LINING = 3
DWRITE_PANOSE_LINING_OUTLINE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_LINING = 4
DWRITE_PANOSE_LINING_ENGRAVED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_LINING = 5
DWRITE_PANOSE_LINING_SHADOW: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_LINING = 6
DWRITE_PANOSE_LINING_RELIEF: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_LINING = 7
DWRITE_PANOSE_LINING_BACKDROP: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_LINING = 8
DWRITE_PANOSE_MIDLINE = Int32
DWRITE_PANOSE_MIDLINE_ANY: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_MIDLINE = 0
DWRITE_PANOSE_MIDLINE_NO_FIT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_MIDLINE = 1
DWRITE_PANOSE_MIDLINE_STANDARD_TRIMMED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_MIDLINE = 2
DWRITE_PANOSE_MIDLINE_STANDARD_POINTED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_MIDLINE = 3
DWRITE_PANOSE_MIDLINE_STANDARD_SERIFED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_MIDLINE = 4
DWRITE_PANOSE_MIDLINE_HIGH_TRIMMED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_MIDLINE = 5
DWRITE_PANOSE_MIDLINE_HIGH_POINTED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_MIDLINE = 6
DWRITE_PANOSE_MIDLINE_HIGH_SERIFED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_MIDLINE = 7
DWRITE_PANOSE_MIDLINE_CONSTANT_TRIMMED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_MIDLINE = 8
DWRITE_PANOSE_MIDLINE_CONSTANT_POINTED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_MIDLINE = 9
DWRITE_PANOSE_MIDLINE_CONSTANT_SERIFED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_MIDLINE = 10
DWRITE_PANOSE_MIDLINE_LOW_TRIMMED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_MIDLINE = 11
DWRITE_PANOSE_MIDLINE_LOW_POINTED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_MIDLINE = 12
DWRITE_PANOSE_MIDLINE_LOW_SERIFED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_MIDLINE = 13
DWRITE_PANOSE_PROPORTION = Int32
DWRITE_PANOSE_PROPORTION_ANY: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_PROPORTION = 0
DWRITE_PANOSE_PROPORTION_NO_FIT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_PROPORTION = 1
DWRITE_PANOSE_PROPORTION_OLD_STYLE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_PROPORTION = 2
DWRITE_PANOSE_PROPORTION_MODERN: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_PROPORTION = 3
DWRITE_PANOSE_PROPORTION_EVEN_WIDTH: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_PROPORTION = 4
DWRITE_PANOSE_PROPORTION_EXPANDED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_PROPORTION = 5
DWRITE_PANOSE_PROPORTION_CONDENSED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_PROPORTION = 6
DWRITE_PANOSE_PROPORTION_VERY_EXPANDED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_PROPORTION = 7
DWRITE_PANOSE_PROPORTION_VERY_CONDENSED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_PROPORTION = 8
DWRITE_PANOSE_PROPORTION_MONOSPACED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_PROPORTION = 9
DWRITE_PANOSE_SCRIPT_FORM = Int32
DWRITE_PANOSE_SCRIPT_FORM_ANY: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SCRIPT_FORM = 0
DWRITE_PANOSE_SCRIPT_FORM_NO_FIT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SCRIPT_FORM = 1
DWRITE_PANOSE_SCRIPT_FORM_UPRIGHT_NO_WRAPPING: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SCRIPT_FORM = 2
DWRITE_PANOSE_SCRIPT_FORM_UPRIGHT_SOME_WRAPPING: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SCRIPT_FORM = 3
DWRITE_PANOSE_SCRIPT_FORM_UPRIGHT_MORE_WRAPPING: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SCRIPT_FORM = 4
DWRITE_PANOSE_SCRIPT_FORM_UPRIGHT_EXTREME_WRAPPING: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SCRIPT_FORM = 5
DWRITE_PANOSE_SCRIPT_FORM_OBLIQUE_NO_WRAPPING: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SCRIPT_FORM = 6
DWRITE_PANOSE_SCRIPT_FORM_OBLIQUE_SOME_WRAPPING: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SCRIPT_FORM = 7
DWRITE_PANOSE_SCRIPT_FORM_OBLIQUE_MORE_WRAPPING: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SCRIPT_FORM = 8
DWRITE_PANOSE_SCRIPT_FORM_OBLIQUE_EXTREME_WRAPPING: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SCRIPT_FORM = 9
DWRITE_PANOSE_SCRIPT_FORM_EXAGGERATED_NO_WRAPPING: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SCRIPT_FORM = 10
DWRITE_PANOSE_SCRIPT_FORM_EXAGGERATED_SOME_WRAPPING: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SCRIPT_FORM = 11
DWRITE_PANOSE_SCRIPT_FORM_EXAGGERATED_MORE_WRAPPING: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SCRIPT_FORM = 12
DWRITE_PANOSE_SCRIPT_FORM_EXAGGERATED_EXTREME_WRAPPING: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SCRIPT_FORM = 13
DWRITE_PANOSE_SCRIPT_TOPOLOGY = Int32
DWRITE_PANOSE_SCRIPT_TOPOLOGY_ANY: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SCRIPT_TOPOLOGY = 0
DWRITE_PANOSE_SCRIPT_TOPOLOGY_NO_FIT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SCRIPT_TOPOLOGY = 1
DWRITE_PANOSE_SCRIPT_TOPOLOGY_ROMAN_DISCONNECTED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SCRIPT_TOPOLOGY = 2
DWRITE_PANOSE_SCRIPT_TOPOLOGY_ROMAN_TRAILING: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SCRIPT_TOPOLOGY = 3
DWRITE_PANOSE_SCRIPT_TOPOLOGY_ROMAN_CONNECTED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SCRIPT_TOPOLOGY = 4
DWRITE_PANOSE_SCRIPT_TOPOLOGY_CURSIVE_DISCONNECTED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SCRIPT_TOPOLOGY = 5
DWRITE_PANOSE_SCRIPT_TOPOLOGY_CURSIVE_TRAILING: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SCRIPT_TOPOLOGY = 6
DWRITE_PANOSE_SCRIPT_TOPOLOGY_CURSIVE_CONNECTED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SCRIPT_TOPOLOGY = 7
DWRITE_PANOSE_SCRIPT_TOPOLOGY_BLACKLETTER_DISCONNECTED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SCRIPT_TOPOLOGY = 8
DWRITE_PANOSE_SCRIPT_TOPOLOGY_BLACKLETTER_TRAILING: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SCRIPT_TOPOLOGY = 9
DWRITE_PANOSE_SCRIPT_TOPOLOGY_BLACKLETTER_CONNECTED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SCRIPT_TOPOLOGY = 10
DWRITE_PANOSE_SERIF_STYLE = Int32
DWRITE_PANOSE_SERIF_STYLE_ANY: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SERIF_STYLE = 0
DWRITE_PANOSE_SERIF_STYLE_NO_FIT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SERIF_STYLE = 1
DWRITE_PANOSE_SERIF_STYLE_COVE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SERIF_STYLE = 2
DWRITE_PANOSE_SERIF_STYLE_OBTUSE_COVE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SERIF_STYLE = 3
DWRITE_PANOSE_SERIF_STYLE_SQUARE_COVE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SERIF_STYLE = 4
DWRITE_PANOSE_SERIF_STYLE_OBTUSE_SQUARE_COVE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SERIF_STYLE = 5
DWRITE_PANOSE_SERIF_STYLE_SQUARE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SERIF_STYLE = 6
DWRITE_PANOSE_SERIF_STYLE_THIN: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SERIF_STYLE = 7
DWRITE_PANOSE_SERIF_STYLE_OVAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SERIF_STYLE = 8
DWRITE_PANOSE_SERIF_STYLE_EXAGGERATED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SERIF_STYLE = 9
DWRITE_PANOSE_SERIF_STYLE_TRIANGLE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SERIF_STYLE = 10
DWRITE_PANOSE_SERIF_STYLE_NORMAL_SANS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SERIF_STYLE = 11
DWRITE_PANOSE_SERIF_STYLE_OBTUSE_SANS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SERIF_STYLE = 12
DWRITE_PANOSE_SERIF_STYLE_PERPENDICULAR_SANS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SERIF_STYLE = 13
DWRITE_PANOSE_SERIF_STYLE_FLARED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SERIF_STYLE = 14
DWRITE_PANOSE_SERIF_STYLE_ROUNDED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SERIF_STYLE = 15
DWRITE_PANOSE_SERIF_STYLE_SCRIPT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SERIF_STYLE = 16
DWRITE_PANOSE_SERIF_STYLE_PERP_SANS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SERIF_STYLE = 13
DWRITE_PANOSE_SERIF_STYLE_BONE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SERIF_STYLE = 8
DWRITE_PANOSE_SPACING = Int32
DWRITE_PANOSE_SPACING_ANY: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SPACING = 0
DWRITE_PANOSE_SPACING_NO_FIT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SPACING = 1
DWRITE_PANOSE_SPACING_PROPORTIONAL_SPACED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SPACING = 2
DWRITE_PANOSE_SPACING_MONOSPACED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SPACING = 3
DWRITE_PANOSE_STROKE_VARIATION = Int32
DWRITE_PANOSE_STROKE_VARIATION_ANY: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_STROKE_VARIATION = 0
DWRITE_PANOSE_STROKE_VARIATION_NO_FIT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_STROKE_VARIATION = 1
DWRITE_PANOSE_STROKE_VARIATION_NO_VARIATION: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_STROKE_VARIATION = 2
DWRITE_PANOSE_STROKE_VARIATION_GRADUAL_DIAGONAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_STROKE_VARIATION = 3
DWRITE_PANOSE_STROKE_VARIATION_GRADUAL_TRANSITIONAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_STROKE_VARIATION = 4
DWRITE_PANOSE_STROKE_VARIATION_GRADUAL_VERTICAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_STROKE_VARIATION = 5
DWRITE_PANOSE_STROKE_VARIATION_GRADUAL_HORIZONTAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_STROKE_VARIATION = 6
DWRITE_PANOSE_STROKE_VARIATION_RAPID_VERTICAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_STROKE_VARIATION = 7
DWRITE_PANOSE_STROKE_VARIATION_RAPID_HORIZONTAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_STROKE_VARIATION = 8
DWRITE_PANOSE_STROKE_VARIATION_INSTANT_VERTICAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_STROKE_VARIATION = 9
DWRITE_PANOSE_STROKE_VARIATION_INSTANT_HORIZONTAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_STROKE_VARIATION = 10
DWRITE_PANOSE_SYMBOL_ASPECT_RATIO = Int32
DWRITE_PANOSE_SYMBOL_ASPECT_RATIO_ANY: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SYMBOL_ASPECT_RATIO = 0
DWRITE_PANOSE_SYMBOL_ASPECT_RATIO_NO_FIT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SYMBOL_ASPECT_RATIO = 1
DWRITE_PANOSE_SYMBOL_ASPECT_RATIO_NO_WIDTH: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SYMBOL_ASPECT_RATIO = 2
DWRITE_PANOSE_SYMBOL_ASPECT_RATIO_EXCEPTIONALLY_WIDE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SYMBOL_ASPECT_RATIO = 3
DWRITE_PANOSE_SYMBOL_ASPECT_RATIO_SUPER_WIDE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SYMBOL_ASPECT_RATIO = 4
DWRITE_PANOSE_SYMBOL_ASPECT_RATIO_VERY_WIDE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SYMBOL_ASPECT_RATIO = 5
DWRITE_PANOSE_SYMBOL_ASPECT_RATIO_WIDE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SYMBOL_ASPECT_RATIO = 6
DWRITE_PANOSE_SYMBOL_ASPECT_RATIO_NORMAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SYMBOL_ASPECT_RATIO = 7
DWRITE_PANOSE_SYMBOL_ASPECT_RATIO_NARROW: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SYMBOL_ASPECT_RATIO = 8
DWRITE_PANOSE_SYMBOL_ASPECT_RATIO_VERY_NARROW: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SYMBOL_ASPECT_RATIO = 9
DWRITE_PANOSE_SYMBOL_KIND = Int32
DWRITE_PANOSE_SYMBOL_KIND_ANY: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SYMBOL_KIND = 0
DWRITE_PANOSE_SYMBOL_KIND_NO_FIT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SYMBOL_KIND = 1
DWRITE_PANOSE_SYMBOL_KIND_MONTAGES: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SYMBOL_KIND = 2
DWRITE_PANOSE_SYMBOL_KIND_PICTURES: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SYMBOL_KIND = 3
DWRITE_PANOSE_SYMBOL_KIND_SHAPES: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SYMBOL_KIND = 4
DWRITE_PANOSE_SYMBOL_KIND_SCIENTIFIC: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SYMBOL_KIND = 5
DWRITE_PANOSE_SYMBOL_KIND_MUSIC: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SYMBOL_KIND = 6
DWRITE_PANOSE_SYMBOL_KIND_EXPERT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SYMBOL_KIND = 7
DWRITE_PANOSE_SYMBOL_KIND_PATTERNS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SYMBOL_KIND = 8
DWRITE_PANOSE_SYMBOL_KIND_BOARDERS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SYMBOL_KIND = 9
DWRITE_PANOSE_SYMBOL_KIND_ICONS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SYMBOL_KIND = 10
DWRITE_PANOSE_SYMBOL_KIND_LOGOS: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SYMBOL_KIND = 11
DWRITE_PANOSE_SYMBOL_KIND_INDUSTRY_SPECIFIC: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_SYMBOL_KIND = 12
DWRITE_PANOSE_TOOL_KIND = Int32
DWRITE_PANOSE_TOOL_KIND_ANY: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_TOOL_KIND = 0
DWRITE_PANOSE_TOOL_KIND_NO_FIT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_TOOL_KIND = 1
DWRITE_PANOSE_TOOL_KIND_FLAT_NIB: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_TOOL_KIND = 2
DWRITE_PANOSE_TOOL_KIND_PRESSURE_POINT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_TOOL_KIND = 3
DWRITE_PANOSE_TOOL_KIND_ENGRAVED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_TOOL_KIND = 4
DWRITE_PANOSE_TOOL_KIND_BALL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_TOOL_KIND = 5
DWRITE_PANOSE_TOOL_KIND_BRUSH: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_TOOL_KIND = 6
DWRITE_PANOSE_TOOL_KIND_ROUGH: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_TOOL_KIND = 7
DWRITE_PANOSE_TOOL_KIND_FELT_PEN_BRUSH_TIP: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_TOOL_KIND = 8
DWRITE_PANOSE_TOOL_KIND_WILD_BRUSH: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_TOOL_KIND = 9
DWRITE_PANOSE_WEIGHT = Int32
DWRITE_PANOSE_WEIGHT_ANY: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_WEIGHT = 0
DWRITE_PANOSE_WEIGHT_NO_FIT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_WEIGHT = 1
DWRITE_PANOSE_WEIGHT_VERY_LIGHT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_WEIGHT = 2
DWRITE_PANOSE_WEIGHT_LIGHT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_WEIGHT = 3
DWRITE_PANOSE_WEIGHT_THIN: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_WEIGHT = 4
DWRITE_PANOSE_WEIGHT_BOOK: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_WEIGHT = 5
DWRITE_PANOSE_WEIGHT_MEDIUM: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_WEIGHT = 6
DWRITE_PANOSE_WEIGHT_DEMI: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_WEIGHT = 7
DWRITE_PANOSE_WEIGHT_BOLD: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_WEIGHT = 8
DWRITE_PANOSE_WEIGHT_HEAVY: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_WEIGHT = 9
DWRITE_PANOSE_WEIGHT_BLACK: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_WEIGHT = 10
DWRITE_PANOSE_WEIGHT_EXTRA_BLACK: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_WEIGHT = 11
DWRITE_PANOSE_WEIGHT_NORD: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_WEIGHT = 11
DWRITE_PANOSE_XASCENT = Int32
DWRITE_PANOSE_XASCENT_ANY: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_XASCENT = 0
DWRITE_PANOSE_XASCENT_NO_FIT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_XASCENT = 1
DWRITE_PANOSE_XASCENT_VERY_LOW: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_XASCENT = 2
DWRITE_PANOSE_XASCENT_LOW: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_XASCENT = 3
DWRITE_PANOSE_XASCENT_MEDIUM: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_XASCENT = 4
DWRITE_PANOSE_XASCENT_HIGH: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_XASCENT = 5
DWRITE_PANOSE_XASCENT_VERY_HIGH: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_XASCENT = 6
DWRITE_PANOSE_XHEIGHT = Int32
DWRITE_PANOSE_XHEIGHT_ANY: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_XHEIGHT = 0
DWRITE_PANOSE_XHEIGHT_NO_FIT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_XHEIGHT = 1
DWRITE_PANOSE_XHEIGHT_CONSTANT_SMALL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_XHEIGHT = 2
DWRITE_PANOSE_XHEIGHT_CONSTANT_STANDARD: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_XHEIGHT = 3
DWRITE_PANOSE_XHEIGHT_CONSTANT_LARGE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_XHEIGHT = 4
DWRITE_PANOSE_XHEIGHT_DUCKING_SMALL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_XHEIGHT = 5
DWRITE_PANOSE_XHEIGHT_DUCKING_STANDARD: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_XHEIGHT = 6
DWRITE_PANOSE_XHEIGHT_DUCKING_LARGE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_XHEIGHT = 7
DWRITE_PANOSE_XHEIGHT_CONSTANT_STD: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_XHEIGHT = 3
DWRITE_PANOSE_XHEIGHT_DUCKING_STD: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE_XHEIGHT = 6
DWRITE_PARAGRAPH_ALIGNMENT = Int32
DWRITE_PARAGRAPH_ALIGNMENT_NEAR: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PARAGRAPH_ALIGNMENT = 0
DWRITE_PARAGRAPH_ALIGNMENT_FAR: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PARAGRAPH_ALIGNMENT = 1
DWRITE_PARAGRAPH_ALIGNMENT_CENTER: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PARAGRAPH_ALIGNMENT = 2
DWRITE_PIXEL_GEOMETRY = Int32
DWRITE_PIXEL_GEOMETRY_FLAT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PIXEL_GEOMETRY = 0
DWRITE_PIXEL_GEOMETRY_RGB: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PIXEL_GEOMETRY = 1
DWRITE_PIXEL_GEOMETRY_BGR: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PIXEL_GEOMETRY = 2
DWRITE_READING_DIRECTION = Int32
DWRITE_READING_DIRECTION_LEFT_TO_RIGHT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_READING_DIRECTION = 0
DWRITE_READING_DIRECTION_RIGHT_TO_LEFT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_READING_DIRECTION = 1
DWRITE_READING_DIRECTION_TOP_TO_BOTTOM: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_READING_DIRECTION = 2
DWRITE_READING_DIRECTION_BOTTOM_TO_TOP: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_READING_DIRECTION = 3
DWRITE_RENDERING_MODE = Int32
DWRITE_RENDERING_MODE_DEFAULT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE = 0
DWRITE_RENDERING_MODE_ALIASED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE = 1
DWRITE_RENDERING_MODE_GDI_CLASSIC: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE = 2
DWRITE_RENDERING_MODE_GDI_NATURAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE = 3
DWRITE_RENDERING_MODE_NATURAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE = 4
DWRITE_RENDERING_MODE_NATURAL_SYMMETRIC: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE = 5
DWRITE_RENDERING_MODE_OUTLINE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE = 6
DWRITE_RENDERING_MODE_CLEARTYPE_GDI_CLASSIC: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE = 2
DWRITE_RENDERING_MODE_CLEARTYPE_GDI_NATURAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE = 3
DWRITE_RENDERING_MODE_CLEARTYPE_NATURAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE = 4
DWRITE_RENDERING_MODE_CLEARTYPE_NATURAL_SYMMETRIC: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE = 5
DWRITE_RENDERING_MODE1 = Int32
DWRITE_RENDERING_MODE1_DEFAULT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE1 = 0
DWRITE_RENDERING_MODE1_ALIASED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE1 = 1
DWRITE_RENDERING_MODE1_GDI_CLASSIC: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE1 = 2
DWRITE_RENDERING_MODE1_GDI_NATURAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE1 = 3
DWRITE_RENDERING_MODE1_NATURAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE1 = 4
DWRITE_RENDERING_MODE1_NATURAL_SYMMETRIC: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE1 = 5
DWRITE_RENDERING_MODE1_OUTLINE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE1 = 6
DWRITE_RENDERING_MODE1_NATURAL_SYMMETRIC_DOWNSAMPLED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE1 = 7
class DWRITE_SCRIPT_ANALYSIS(EasyCastStructure):
    script: UInt16
    shapes: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_SCRIPT_SHAPES
class DWRITE_SCRIPT_PROPERTIES(EasyCastStructure):
    isoScriptCode: UInt32
    isoScriptNumber: UInt32
    clusterLookahead: UInt32
    justificationCharacter: UInt32
    _bitfield: UInt32
DWRITE_SCRIPT_SHAPES = Int32
DWRITE_SCRIPT_SHAPES_DEFAULT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_SCRIPT_SHAPES = 0
DWRITE_SCRIPT_SHAPES_NO_VISUAL: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_SCRIPT_SHAPES = 1
class DWRITE_SHAPING_GLYPH_PROPERTIES(EasyCastStructure):
    _bitfield: UInt16
class DWRITE_SHAPING_TEXT_PROPERTIES(EasyCastStructure):
    _bitfield: UInt16
class DWRITE_STRIKETHROUGH(EasyCastStructure):
    width: Single
    thickness: Single
    offset: Single
    readingDirection: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_READING_DIRECTION
    flowDirection: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FLOW_DIRECTION
    localeName: win32more.Windows.Win32.Foundation.PWSTR
    measuringMode: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MEASURING_MODE
DWRITE_TEXTURE_TYPE = Int32
DWRITE_TEXTURE_ALIASED_1x1: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXTURE_TYPE = 0
DWRITE_TEXTURE_CLEARTYPE_3x1: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXTURE_TYPE = 1
DWRITE_TEXT_ALIGNMENT = Int32
DWRITE_TEXT_ALIGNMENT_LEADING: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_ALIGNMENT = 0
DWRITE_TEXT_ALIGNMENT_TRAILING: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_ALIGNMENT = 1
DWRITE_TEXT_ALIGNMENT_CENTER: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_ALIGNMENT = 2
DWRITE_TEXT_ALIGNMENT_JUSTIFIED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_ALIGNMENT = 3
DWRITE_TEXT_ANTIALIAS_MODE = Int32
DWRITE_TEXT_ANTIALIAS_MODE_CLEARTYPE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_ANTIALIAS_MODE = 0
DWRITE_TEXT_ANTIALIAS_MODE_GRAYSCALE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_ANTIALIAS_MODE = 1
class DWRITE_TEXT_METRICS(EasyCastStructure):
    left: Single
    top: Single
    width: Single
    widthIncludingTrailingWhitespace: Single
    height: Single
    layoutWidth: Single
    layoutHeight: Single
    maxBidiReorderingDepth: UInt32
    lineCount: UInt32
class DWRITE_TEXT_METRICS1(EasyCastStructure):
    Base: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_METRICS
    heightIncludingTrailingWhitespace: Single
class DWRITE_TEXT_RANGE(EasyCastStructure):
    startPosition: UInt32
    length: UInt32
class DWRITE_TRIMMING(EasyCastStructure):
    granularity: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TRIMMING_GRANULARITY
    delimiter: UInt32
    delimiterCount: UInt32
DWRITE_TRIMMING_GRANULARITY = Int32
DWRITE_TRIMMING_GRANULARITY_NONE: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TRIMMING_GRANULARITY = 0
DWRITE_TRIMMING_GRANULARITY_CHARACTER: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TRIMMING_GRANULARITY = 1
DWRITE_TRIMMING_GRANULARITY_WORD: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TRIMMING_GRANULARITY = 2
class DWRITE_TYPOGRAPHIC_FEATURES(EasyCastStructure):
    features: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE)
    featureCount: UInt32
class DWRITE_UNDERLINE(EasyCastStructure):
    width: Single
    thickness: Single
    offset: Single
    runHeight: Single
    readingDirection: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_READING_DIRECTION
    flowDirection: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FLOW_DIRECTION
    localeName: win32more.Windows.Win32.Foundation.PWSTR
    measuringMode: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MEASURING_MODE
class DWRITE_UNICODE_RANGE(EasyCastStructure):
    first: UInt32
    last: UInt32
DWRITE_VERTICAL_GLYPH_ORIENTATION = Int32
DWRITE_VERTICAL_GLYPH_ORIENTATION_DEFAULT: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_VERTICAL_GLYPH_ORIENTATION = 0
DWRITE_VERTICAL_GLYPH_ORIENTATION_STACKED: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_VERTICAL_GLYPH_ORIENTATION = 1
DWRITE_WORD_WRAPPING = Int32
DWRITE_WORD_WRAPPING_WRAP: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_WORD_WRAPPING = 0
DWRITE_WORD_WRAPPING_NO_WRAP: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_WORD_WRAPPING = 1
DWRITE_WORD_WRAPPING_EMERGENCY_BREAK: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_WORD_WRAPPING = 2
DWRITE_WORD_WRAPPING_WHOLE_WORD: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_WORD_WRAPPING = 3
DWRITE_WORD_WRAPPING_CHARACTER: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_WORD_WRAPPING = 4
class IDWriteAsyncResult(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ce25f8fd-863b-4d13-9651-c1f88dc73fe2}')
    @commethod(3)
    def GetWaitHandle(self) -> win32more.Windows.Win32.Foundation.HANDLE: ...
    @commethod(4)
    def GetResult(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteBitmapRenderTarget(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5e5a32a3-8dff-4773-9ff6-0696eab77267}')
    @commethod(3)
    def DrawGlyphRun(self, baselineOriginX: Single, baselineOriginY: Single, measuringMode: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MEASURING_MODE, glyphRun: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_RUN), renderingParams: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteRenderingParams, textColor: win32more.Windows.Win32.Foundation.COLORREF, blackBoxRect: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMemoryDC(self) -> win32more.Windows.Win32.Graphics.Gdi.HDC: ...
    @commethod(5)
    def GetPixelsPerDip(self) -> Single: ...
    @commethod(6)
    def SetPixelsPerDip(self, pixelsPerDip: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCurrentTransform(self, transform: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MATRIX)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetCurrentTransform(self, transform: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MATRIX)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSize(self, size: POINTER(win32more.Windows.Win32.Foundation.SIZE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Resize(self, width: UInt32, height: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteBitmapRenderTarget1(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteBitmapRenderTarget
    _iid_ = Guid('{791e8298-3ef3-4230-9880-c9bdecc42064}')
    @commethod(11)
    def GetTextAntialiasMode(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_ANTIALIAS_MODE: ...
    @commethod(12)
    def SetTextAntialiasMode(self, antialiasMode: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_ANTIALIAS_MODE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteColorGlyphRunEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d31fbe17-f157-41a2-8d24-cb779e0560e8}')
    @commethod(3)
    def MoveNext(self, hasRun: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentRun(self, colorGlyphRun: POINTER(POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_COLOR_GLYPH_RUN))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteColorGlyphRunEnumerator1(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteColorGlyphRunEnumerator
    _iid_ = Guid('{7c5f86da-c7a1-4f05-b8e1-55a179fe5a35}')
    @commethod(5)
    def GetCurrentRun(self, colorGlyphRun: POINTER(POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_COLOR_GLYPH_RUN1))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b859ee5a-d838-4b5b-a2e8-1adc7d93db48}')
    @commethod(3)
    def GetSystemFontCollection(self, fontCollection: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontCollection), checkForUpdates: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateCustomFontCollection(self, collectionLoader: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontCollectionLoader, collectionKey: VoidPtr, collectionKeySize: UInt32, fontCollection: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RegisterFontCollectionLoader(self, fontCollectionLoader: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontCollectionLoader) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def UnregisterFontCollectionLoader(self, fontCollectionLoader: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontCollectionLoader) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateFontFileReference(self, filePath: win32more.Windows.Win32.Foundation.PWSTR, lastWriteTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), fontFile: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFile)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreateCustomFontFileReference(self, fontFileReferenceKey: VoidPtr, fontFileReferenceKeySize: UInt32, fontFileLoader: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFileLoader, fontFile: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFile)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CreateFontFace(self, fontFaceType: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FACE_TYPE, numberOfFiles: UInt32, fontFiles: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFile), faceIndex: UInt32, fontFaceSimulationFlags: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_SIMULATIONS, fontFace: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFace)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CreateRenderingParams(self, renderingParams: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteRenderingParams)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CreateMonitorRenderingParams(self, monitor: win32more.Windows.Win32.Graphics.Gdi.HMONITOR, renderingParams: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteRenderingParams)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def CreateCustomRenderingParams(self, gamma: Single, enhancedContrast: Single, clearTypeLevel: Single, pixelGeometry: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PIXEL_GEOMETRY, renderingMode: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE, renderingParams: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteRenderingParams)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def RegisterFontFileLoader(self, fontFileLoader: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFileLoader) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def UnregisterFontFileLoader(self, fontFileLoader: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFileLoader) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def CreateTextFormat(self, fontFamilyName: win32more.Windows.Win32.Foundation.PWSTR, fontCollection: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontCollection, fontWeight: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_WEIGHT, fontStyle: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STYLE, fontStretch: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STRETCH, fontSize: Single, localeName: win32more.Windows.Win32.Foundation.PWSTR, textFormat: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextFormat)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def CreateTypography(self, typography: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTypography)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetGdiInterop(self, gdiInterop: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteGdiInterop)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def CreateTextLayout(self, string: win32more.Windows.Win32.Foundation.PWSTR, stringLength: UInt32, textFormat: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextFormat, maxWidth: Single, maxHeight: Single, textLayout: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextLayout)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def CreateGdiCompatibleTextLayout(self, string: win32more.Windows.Win32.Foundation.PWSTR, stringLength: UInt32, textFormat: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextFormat, layoutWidth: Single, layoutHeight: Single, pixelsPerDip: Single, transform: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MATRIX), useGdiNatural: win32more.Windows.Win32.Foundation.BOOL, textLayout: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextLayout)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def CreateEllipsisTrimmingSign(self, textFormat: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextFormat, trimmingSign: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteInlineObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def CreateTextAnalyzer(self, textAnalyzer: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextAnalyzer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def CreateNumberSubstitution(self, substitutionMethod: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_NUMBER_SUBSTITUTION_METHOD, localeName: win32more.Windows.Win32.Foundation.PWSTR, ignoreUserOverride: win32more.Windows.Win32.Foundation.BOOL, numberSubstitution: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteNumberSubstitution)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def CreateGlyphRunAnalysis(self, glyphRun: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_RUN), pixelsPerDip: Single, transform: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MATRIX), renderingMode: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE, measuringMode: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MEASURING_MODE, baselineOriginX: Single, baselineOriginY: Single, glyphRunAnalysis: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteGlyphRunAnalysis)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFactory1(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFactory
    _iid_ = Guid('{30572f99-dac6-41db-a16e-0486307e606a}')
    @commethod(24)
    def GetEudcFontCollection(self, fontCollection: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontCollection), checkForUpdates: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def CreateCustomRenderingParams(self, gamma: Single, enhancedContrast: Single, enhancedContrastGrayscale: Single, clearTypeLevel: Single, pixelGeometry: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PIXEL_GEOMETRY, renderingMode: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE, renderingParams: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteRenderingParams1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFactory2(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFactory1
    _iid_ = Guid('{0439fc60-ca44-4994-8dee-3a9af7b732ec}')
    @commethod(26)
    def GetSystemFontFallback(self, fontFallback: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFallback)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def CreateFontFallbackBuilder(self, fontFallbackBuilder: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFallbackBuilder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def TranslateColorGlyphRun(self, baselineOriginX: Single, baselineOriginY: Single, glyphRun: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_RUN), glyphRunDescription: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_RUN_DESCRIPTION), measuringMode: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MEASURING_MODE, worldToDeviceTransform: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MATRIX), colorPaletteIndex: UInt32, colorLayers: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteColorGlyphRunEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def CreateCustomRenderingParams(self, gamma: Single, enhancedContrast: Single, grayscaleEnhancedContrast: Single, clearTypeLevel: Single, pixelGeometry: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PIXEL_GEOMETRY, renderingMode: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE, gridFitMode: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GRID_FIT_MODE, renderingParams: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteRenderingParams2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def CreateGlyphRunAnalysis(self, glyphRun: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_RUN), transform: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MATRIX), renderingMode: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE, measuringMode: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MEASURING_MODE, gridFitMode: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GRID_FIT_MODE, antialiasMode: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_ANTIALIAS_MODE, baselineOriginX: Single, baselineOriginY: Single, glyphRunAnalysis: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteGlyphRunAnalysis)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFactory3(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFactory2
    _iid_ = Guid('{9a1b41c3-d3bb-466a-87fc-fe67556a3b65}')
    @commethod(31)
    def CreateGlyphRunAnalysis(self, glyphRun: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_RUN), transform: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MATRIX), renderingMode: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE1, measuringMode: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MEASURING_MODE, gridFitMode: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GRID_FIT_MODE, antialiasMode: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_ANTIALIAS_MODE, baselineOriginX: Single, baselineOriginY: Single, glyphRunAnalysis: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteGlyphRunAnalysis)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def CreateCustomRenderingParams(self, gamma: Single, enhancedContrast: Single, grayscaleEnhancedContrast: Single, clearTypeLevel: Single, pixelGeometry: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PIXEL_GEOMETRY, renderingMode: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE1, gridFitMode: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GRID_FIT_MODE, renderingParams: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteRenderingParams3)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def CreateFontFaceReference(self, fontFile: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFile, faceIndex: UInt32, fontSimulations: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_SIMULATIONS, fontFaceReference: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFaceReference)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def CreateFontFaceReference(self, filePath: win32more.Windows.Win32.Foundation.PWSTR, lastWriteTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), faceIndex: UInt32, fontSimulations: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_SIMULATIONS, fontFaceReference: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFaceReference)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetSystemFontSet(self, fontSet: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def CreateFontSetBuilder(self, fontSetBuilder: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontSetBuilder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def CreateFontCollectionFromFontSet(self, fontSet: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontSet, fontCollection: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontCollection1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def GetSystemFontCollection(self, includeDownloadableFonts: win32more.Windows.Win32.Foundation.BOOL, fontCollection: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontCollection1), checkForUpdates: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def GetFontDownloadQueue(self, fontDownloadQueue: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontDownloadQueue)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFactory4(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFactory3
    _iid_ = Guid('{4b0b5bd3-0797-4549-8ac5-fe915cc53856}')
    @commethod(40)
    def TranslateColorGlyphRun(self, baselineOrigin: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D_POINT_2F, glyphRun: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_RUN), glyphRunDescription: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_RUN_DESCRIPTION), desiredGlyphImageFormats: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_IMAGE_FORMATS, measuringMode: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MEASURING_MODE, worldAndDpiTransform: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MATRIX), colorPaletteIndex: UInt32, colorLayers: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteColorGlyphRunEnumerator1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def ComputeGlyphOrigins(self, glyphRun: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_RUN), baselineOrigin: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D_POINT_2F, glyphOrigins: POINTER(win32more.Windows.Win32.Graphics.Direct2D.Common.D2D_POINT_2F)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def ComputeGlyphOrigins(self, glyphRun: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_RUN), measuringMode: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MEASURING_MODE, baselineOrigin: win32more.Windows.Win32.Graphics.Direct2D.Common.D2D_POINT_2F, worldAndDpiTransform: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MATRIX), glyphOrigins: POINTER(win32more.Windows.Win32.Graphics.Direct2D.Common.D2D_POINT_2F)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFactory5(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFactory4
    _iid_ = Guid('{958db99a-be2a-4f09-af7d-65189803d1d3}')
    @commethod(43)
    def CreateFontSetBuilder(self, fontSetBuilder: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontSetBuilder1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def CreateInMemoryFontFileLoader(self, newLoader: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteInMemoryFontFileLoader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def CreateHttpFontFileLoader(self, referrerUrl: win32more.Windows.Win32.Foundation.PWSTR, extraHeaders: win32more.Windows.Win32.Foundation.PWSTR, newLoader: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteRemoteFontFileLoader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def AnalyzeContainerType(self, fileData: VoidPtr, fileDataSize: UInt32) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_CONTAINER_TYPE: ...
    @commethod(47)
    def UnpackFontFile(self, containerType: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_CONTAINER_TYPE, fileData: VoidPtr, fileDataSize: UInt32, unpackedFontStream: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFileStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFactory6(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFactory5
    _iid_ = Guid('{f3744d80-21f7-42eb-b35d-995bc72fc223}')
    @commethod(48)
    def CreateFontFaceReference(self, fontFile: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFile, faceIndex: UInt32, fontSimulations: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_SIMULATIONS, fontAxisValues: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE), fontAxisValueCount: UInt32, fontFaceReference: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFaceReference1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def CreateFontResource(self, fontFile: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFile, faceIndex: UInt32, fontResource: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontResource)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def GetSystemFontSet(self, includeDownloadableFonts: win32more.Windows.Win32.Foundation.BOOL, fontSet: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontSet1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def GetSystemFontCollection(self, includeDownloadableFonts: win32more.Windows.Win32.Foundation.BOOL, fontFamilyModel: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FAMILY_MODEL, fontCollection: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontCollection2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def CreateFontCollectionFromFontSet(self, fontSet: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontSet, fontFamilyModel: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FAMILY_MODEL, fontCollection: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontCollection2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def CreateFontSetBuilder(self, fontSetBuilder: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontSetBuilder2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def CreateTextFormat(self, fontFamilyName: win32more.Windows.Win32.Foundation.PWSTR, fontCollection: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontCollection, fontAxisValues: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE), fontAxisValueCount: UInt32, fontSize: Single, localeName: win32more.Windows.Win32.Foundation.PWSTR, textFormat: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextFormat3)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFactory7(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFactory6
    _iid_ = Guid('{35d0e0b3-9076-4d2e-a016-a91b568a06b4}')
    @commethod(55)
    def GetSystemFontSet(self, includeDownloadableFonts: win32more.Windows.Win32.Foundation.BOOL, fontSet: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontSet2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def GetSystemFontCollection(self, includeDownloadableFonts: win32more.Windows.Win32.Foundation.BOOL, fontFamilyModel: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FAMILY_MODEL, fontCollection: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontCollection3)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFont(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{acd16696-8c14-4f5d-877e-fe3fc1d32737}')
    @commethod(3)
    def GetFontFamily(self, fontFamily: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFamily)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetWeight(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_WEIGHT: ...
    @commethod(5)
    def GetStretch(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STRETCH: ...
    @commethod(6)
    def GetStyle(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STYLE: ...
    @commethod(7)
    def IsSymbolFont(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(8)
    def GetFaceNames(self, names: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteLocalizedStrings)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetInformationalStrings(self, informationalStringID: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_INFORMATIONAL_STRING_ID, informationalStrings: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteLocalizedStrings), exists: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetSimulations(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_SIMULATIONS: ...
    @commethod(11)
    def GetMetrics(self, fontMetrics: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_METRICS)) -> Void: ...
    @commethod(12)
    def HasCharacter(self, unicodeValue: UInt32, exists: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def CreateFontFace(self, fontFace: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFace)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFont1(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFont
    _iid_ = Guid('{acd16696-8c14-4f5d-877e-fe3fc1d32738}')
    @commethod(14)
    def GetMetrics(self, fontMetrics: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_METRICS1)) -> Void: ...
    @commethod(15)
    def GetPanose(self, panose: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE)) -> Void: ...
    @commethod(16)
    def GetUnicodeRanges(self, maxRangeCount: UInt32, unicodeRanges: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_UNICODE_RANGE), actualRangeCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def IsMonospacedFont(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
class IDWriteFont2(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFont1
    _iid_ = Guid('{29748ed6-8c9c-4a6a-be0b-d912e8538944}')
    @commethod(18)
    def IsColorFont(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
class IDWriteFont3(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFont2
    _iid_ = Guid('{29748ed6-8c9c-4a6a-be0b-d912e8538944}')
    @commethod(19)
    def CreateFontFace(self, fontFace: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFace3)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def Equals(self, font: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFont) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(21)
    def GetFontFaceReference(self, fontFaceReference: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFaceReference)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def HasCharacter(self, unicodeValue: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(23)
    def GetLocality(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_LOCALITY: ...
class IDWriteFontCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a84cee02-3eea-4eee-a827-87c1a02a0fcc}')
    @commethod(3)
    def GetFontFamilyCount(self) -> UInt32: ...
    @commethod(4)
    def GetFontFamily(self, index: UInt32, fontFamily: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFamily)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def FindFamilyName(self, familyName: win32more.Windows.Win32.Foundation.PWSTR, index: POINTER(UInt32), exists: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFontFromFontFace(self, fontFace: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFace, font: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFont)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFontCollection1(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontCollection
    _iid_ = Guid('{53585141-d9f8-4095-8321-d73cf6bd116c}')
    @commethod(7)
    def GetFontSet(self, fontSet: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetFontFamily(self, index: UInt32, fontFamily: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFamily1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFontCollection2(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontCollection1
    _iid_ = Guid('{514039c6-4617-4064-bf8b-92ea83e506e0}')
    @commethod(9)
    def GetFontFamily(self, index: UInt32, fontFamily: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFamily2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetMatchingFonts(self, familyName: win32more.Windows.Win32.Foundation.PWSTR, fontAxisValues: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE), fontAxisValueCount: UInt32, fontList: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontList2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetFontFamilyModel(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FAMILY_MODEL: ...
    @commethod(12)
    def GetFontSet(self, fontSet: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontSet1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFontCollection3(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontCollection2
    _iid_ = Guid('{a4d055a6-f9e3-4e25-93b7-9e309f3af8e9}')
    @commethod(13)
    def GetExpirationEvent(self) -> win32more.Windows.Win32.Foundation.HANDLE: ...
class IDWriteFontCollectionLoader(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cca920e4-52f0-492b-bfa8-29c72ee0a468}')
    @commethod(3)
    def CreateEnumeratorFromKey(self, factory: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFactory, collectionKey: VoidPtr, collectionKeySize: UInt32, fontFileEnumerator: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFileEnumerator)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFontDownloadListener(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b06fe5b9-43ec-4393-881b-dbe4dc72fda7}')
    @commethod(3)
    def DownloadCompleted(self, downloadQueue: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontDownloadQueue, context: win32more.Windows.Win32.System.Com.IUnknown, downloadResult: win32more.Windows.Win32.Foundation.HRESULT) -> Void: ...
class IDWriteFontDownloadQueue(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b71e6052-5aea-4fa3-832e-f60d431f7e91}')
    @commethod(3)
    def AddListener(self, listener: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontDownloadListener, token: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveListener(self, token: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsEmpty(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(6)
    def BeginDownload(self, context: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CancelDownload(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetGenerationCount(self) -> UInt64: ...
class IDWriteFontFace(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5f49804d-7024-4d43-bfa9-d25984f53849}')
    @commethod(3)
    def GetType(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FACE_TYPE: ...
    @commethod(4)
    def GetFiles(self, numberOfFiles: POINTER(UInt32), fontFiles: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFile)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetIndex(self) -> UInt32: ...
    @commethod(6)
    def GetSimulations(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_SIMULATIONS: ...
    @commethod(7)
    def IsSymbolFont(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(8)
    def GetMetrics(self, fontFaceMetrics: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_METRICS)) -> Void: ...
    @commethod(9)
    def GetGlyphCount(self) -> UInt16: ...
    @commethod(10)
    def GetDesignGlyphMetrics(self, glyphIndices: POINTER(UInt16), glyphCount: UInt32, glyphMetrics: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_METRICS), isSideways: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetGlyphIndices(self, codePoints: POINTER(UInt32), codePointCount: UInt32, glyphIndices: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def TryGetFontTable(self, openTypeTableTag: UInt32, tableData: POINTER(VoidPtr), tableSize: POINTER(UInt32), tableContext: POINTER(VoidPtr), exists: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def ReleaseFontTable(self, tableContext: VoidPtr) -> Void: ...
    @commethod(14)
    def GetGlyphRunOutline(self, emSize: Single, glyphIndices: POINTER(UInt16), glyphAdvances: POINTER(Single), glyphOffsets: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_OFFSET), glyphCount: UInt32, isSideways: win32more.Windows.Win32.Foundation.BOOL, isRightToLeft: win32more.Windows.Win32.Foundation.BOOL, geometrySink: win32more.Windows.Win32.Graphics.Direct2D.Common.ID2D1SimplifiedGeometrySink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetRecommendedRenderingMode(self, emSize: Single, pixelsPerDip: Single, measuringMode: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MEASURING_MODE, renderingParams: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteRenderingParams, renderingMode: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetGdiCompatibleMetrics(self, emSize: Single, pixelsPerDip: Single, transform: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MATRIX), fontFaceMetrics: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_METRICS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetGdiCompatibleGlyphMetrics(self, emSize: Single, pixelsPerDip: Single, transform: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MATRIX), useGdiNatural: win32more.Windows.Win32.Foundation.BOOL, glyphIndices: POINTER(UInt16), glyphCount: UInt32, glyphMetrics: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_METRICS), isSideways: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFontFace1(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFace
    _iid_ = Guid('{a71efdb4-9fdb-4838-ad90-cfc3be8c3daf}')
    @commethod(18)
    def GetMetrics(self, fontMetrics: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_METRICS1)) -> Void: ...
    @commethod(19)
    def GetGdiCompatibleMetrics(self, emSize: Single, pixelsPerDip: Single, transform: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MATRIX), fontMetrics: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_METRICS1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetCaretMetrics(self, caretMetrics: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_CARET_METRICS)) -> Void: ...
    @commethod(21)
    def GetUnicodeRanges(self, maxRangeCount: UInt32, unicodeRanges: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_UNICODE_RANGE), actualRangeCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def IsMonospacedFont(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(23)
    def GetDesignGlyphAdvances(self, glyphCount: UInt32, glyphIndices: POINTER(UInt16), glyphAdvances: POINTER(Int32), isSideways: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetGdiCompatibleGlyphAdvances(self, emSize: Single, pixelsPerDip: Single, transform: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MATRIX), useGdiNatural: win32more.Windows.Win32.Foundation.BOOL, isSideways: win32more.Windows.Win32.Foundation.BOOL, glyphCount: UInt32, glyphIndices: POINTER(UInt16), glyphAdvances: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetKerningPairAdjustments(self, glyphCount: UInt32, glyphIndices: POINTER(UInt16), glyphAdvanceAdjustments: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def HasKerningPairs(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(27)
    def GetRecommendedRenderingMode(self, fontEmSize: Single, dpiX: Single, dpiY: Single, transform: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MATRIX), isSideways: win32more.Windows.Win32.Foundation.BOOL, outlineThreshold: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_OUTLINE_THRESHOLD, measuringMode: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MEASURING_MODE, renderingMode: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetVerticalGlyphVariants(self, glyphCount: UInt32, nominalGlyphIndices: POINTER(UInt16), verticalGlyphIndices: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def HasVerticalGlyphVariants(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
class IDWriteFontFace2(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFace1
    _iid_ = Guid('{d8b768ff-64bc-4e66-982b-ec8e87f693f7}')
    @commethod(30)
    def IsColorFont(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(31)
    def GetColorPaletteCount(self) -> UInt32: ...
    @commethod(32)
    def GetPaletteEntryCount(self) -> UInt32: ...
    @commethod(33)
    def GetPaletteEntries(self, colorPaletteIndex: UInt32, firstEntryIndex: UInt32, entryCount: UInt32, paletteEntries: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_COLOR_F)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetRecommendedRenderingMode(self, fontEmSize: Single, dpiX: Single, dpiY: Single, transform: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MATRIX), isSideways: win32more.Windows.Win32.Foundation.BOOL, outlineThreshold: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_OUTLINE_THRESHOLD, measuringMode: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MEASURING_MODE, renderingParams: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteRenderingParams, renderingMode: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE), gridFitMode: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GRID_FIT_MODE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFontFace3(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFace2
    _iid_ = Guid('{d37d7598-09be-4222-a236-2081341cc1f2}')
    @commethod(35)
    def GetFontFaceReference(self, fontFaceReference: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFaceReference)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def GetPanose(self, panose: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PANOSE)) -> Void: ...
    @commethod(37)
    def GetWeight(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_WEIGHT: ...
    @commethod(38)
    def GetStretch(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STRETCH: ...
    @commethod(39)
    def GetStyle(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STYLE: ...
    @commethod(40)
    def GetFamilyNames(self, names: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteLocalizedStrings)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def GetFaceNames(self, names: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteLocalizedStrings)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def GetInformationalStrings(self, informationalStringID: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_INFORMATIONAL_STRING_ID, informationalStrings: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteLocalizedStrings), exists: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def HasCharacter(self, unicodeValue: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(44)
    def GetRecommendedRenderingMode(self, fontEmSize: Single, dpiX: Single, dpiY: Single, transform: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MATRIX), isSideways: win32more.Windows.Win32.Foundation.BOOL, outlineThreshold: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_OUTLINE_THRESHOLD, measuringMode: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MEASURING_MODE, renderingParams: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteRenderingParams, renderingMode: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE1), gridFitMode: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GRID_FIT_MODE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def IsCharacterLocal(self, unicodeValue: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(46)
    def IsGlyphLocal(self, glyphId: UInt16) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(47)
    def AreCharactersLocal(self, characters: win32more.Windows.Win32.Foundation.PWSTR, characterCount: UInt32, enqueueIfNotLocal: win32more.Windows.Win32.Foundation.BOOL, isLocal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def AreGlyphsLocal(self, glyphIndices: POINTER(UInt16), glyphCount: UInt32, enqueueIfNotLocal: win32more.Windows.Win32.Foundation.BOOL, isLocal: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFontFace4(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFace3
    _iid_ = Guid('{27f2a904-4eb8-441d-9678-0563f53e3e2f}')
    @commethod(49)
    def GetGlyphImageFormats(self, glyphId: UInt16, pixelsPerEmFirst: UInt32, pixelsPerEmLast: UInt32, glyphImageFormats: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_IMAGE_FORMATS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def GetGlyphImageFormats(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_IMAGE_FORMATS: ...
    @commethod(51)
    def GetGlyphImageData(self, glyphId: UInt16, pixelsPerEm: UInt32, glyphImageFormat: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_IMAGE_FORMATS, glyphData: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_IMAGE_DATA), glyphDataContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def ReleaseGlyphImageData(self, glyphDataContext: VoidPtr) -> Void: ...
class IDWriteFontFace5(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFace4
    _iid_ = Guid('{98eff3a5-b667-479a-b145-e2fa5b9fdc29}')
    @commethod(53)
    def GetFontAxisValueCount(self) -> UInt32: ...
    @commethod(54)
    def GetFontAxisValues(self, fontAxisValues: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE), fontAxisValueCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def HasVariations(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(56)
    def GetFontResource(self, fontResource: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontResource)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def Equals(self, fontFace: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFace) -> win32more.Windows.Win32.Foundation.BOOL: ...
class IDWriteFontFace6(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFace5
    _iid_ = Guid('{c4b1fe1b-6e84-47d5-b54c-a597981b06ad}')
    @commethod(58)
    def GetFamilyNames(self, fontFamilyModel: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FAMILY_MODEL, names: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteLocalizedStrings)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def GetFaceNames(self, fontFamilyModel: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FAMILY_MODEL, names: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteLocalizedStrings)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFontFaceReference(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5e7fa7ca-dde3-424c-89f0-9fcd6fed58cd}')
    @commethod(3)
    def CreateFontFace(self, fontFace: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFace3)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateFontFaceWithSimulations(self, fontFaceSimulationFlags: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_SIMULATIONS, fontFace: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFace3)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Equals(self, fontFaceReference: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFaceReference) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(6)
    def GetFontFaceIndex(self) -> UInt32: ...
    @commethod(7)
    def GetSimulations(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_SIMULATIONS: ...
    @commethod(8)
    def GetFontFile(self, fontFile: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFile)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetLocalFileSize(self) -> UInt64: ...
    @commethod(10)
    def GetFileSize(self) -> UInt64: ...
    @commethod(11)
    def GetFileTime(self, lastWriteTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetLocality(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_LOCALITY: ...
    @commethod(13)
    def EnqueueFontDownloadRequest(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def EnqueueCharacterDownloadRequest(self, characters: win32more.Windows.Win32.Foundation.PWSTR, characterCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def EnqueueGlyphDownloadRequest(self, glyphIndices: POINTER(UInt16), glyphCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def EnqueueFileFragmentDownloadRequest(self, fileOffset: UInt64, fragmentSize: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFontFaceReference1(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFaceReference
    _iid_ = Guid('{c081fe77-2fd1-41ac-a5a3-34983c4ba61a}')
    @commethod(17)
    def CreateFontFace(self, fontFace: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFace5)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetFontAxisValueCount(self) -> UInt32: ...
    @commethod(19)
    def GetFontAxisValues(self, fontAxisValues: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE), fontAxisValueCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFontFallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{efa008f9-f7a1-48bf-b05c-f224713cc0ff}')
    @commethod(3)
    def MapCharacters(self, analysisSource: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextAnalysisSource, textPosition: UInt32, textLength: UInt32, baseFontCollection: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontCollection, baseFamilyName: win32more.Windows.Win32.Foundation.PWSTR, baseWeight: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_WEIGHT, baseStyle: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STYLE, baseStretch: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STRETCH, mappedLength: POINTER(UInt32), mappedFont: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFont), scale: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFontFallback1(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFallback
    _iid_ = Guid('{2397599d-dd0d-4681-bd6a-f4f31eaade77}')
    @commethod(4)
    def MapCharacters(self, analysisSource: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextAnalysisSource, textPosition: UInt32, textLength: UInt32, baseFontCollection: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontCollection, baseFamilyName: win32more.Windows.Win32.Foundation.PWSTR, fontAxisValues: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE), fontAxisValueCount: UInt32, mappedLength: POINTER(UInt32), scale: POINTER(Single), mappedFontFace: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFace5)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFontFallbackBuilder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fd882d06-8aba-4fb8-b849-8be8b73e14de}')
    @commethod(3)
    def AddMapping(self, ranges: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_UNICODE_RANGE), rangesCount: UInt32, targetFamilyNames: POINTER(POINTER(UInt16)), targetFamilyNamesCount: UInt32, fontCollection: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontCollection, localeName: win32more.Windows.Win32.Foundation.PWSTR, baseFamilyName: win32more.Windows.Win32.Foundation.PWSTR, scale: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddMappings(self, fontFallback: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateFontFallback(self, fontFallback: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFallback)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFontFamily(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontList
    _iid_ = Guid('{da20d8ef-812a-4c43-9802-62ec4abd7add}')
    @commethod(6)
    def GetFamilyNames(self, names: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteLocalizedStrings)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFirstMatchingFont(self, weight: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_WEIGHT, stretch: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STRETCH, style: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STYLE, matchingFont: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFont)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetMatchingFonts(self, weight: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_WEIGHT, stretch: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STRETCH, style: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STYLE, matchingFonts: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontList)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFontFamily1(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFamily
    _iid_ = Guid('{da20d8ef-812a-4c43-9802-62ec4abd7adf}')
    @commethod(9)
    def GetFontLocality(self, listIndex: UInt32) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_LOCALITY: ...
    @commethod(10)
    def GetFont(self, listIndex: UInt32, font: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFont3)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetFontFaceReference(self, listIndex: UInt32, fontFaceReference: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFaceReference)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFontFamily2(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFamily1
    _iid_ = Guid('{3ed49e77-a398-4261-b9cf-c126c2131ef3}')
    @commethod(12)
    def GetMatchingFonts(self, fontAxisValues: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE), fontAxisValueCount: UInt32, matchingFonts: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontList2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetFontSet(self, fontSet: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontSet1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFontFile(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{739d886a-cef5-47dc-8769-1a8b41bebbb0}')
    @commethod(3)
    def GetReferenceKey(self, fontFileReferenceKey: POINTER(VoidPtr), fontFileReferenceKeySize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLoader(self, fontFileLoader: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFileLoader)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Analyze(self, isSupportedFontType: POINTER(win32more.Windows.Win32.Foundation.BOOL), fontFileType: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FILE_TYPE), fontFaceType: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FACE_TYPE), numberOfFaces: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFontFileEnumerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{72755049-5ff7-435d-8348-4be97cfa6c7c}')
    @commethod(3)
    def MoveNext(self, hasCurrentFile: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentFontFile(self, fontFile: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFile)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFontFileLoader(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{727cad4e-d6af-4c9e-8a08-d695b11caa49}')
    @commethod(3)
    def CreateStreamFromKey(self, fontFileReferenceKey: VoidPtr, fontFileReferenceKeySize: UInt32, fontFileStream: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFileStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFontFileStream(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6d4865fe-0ab8-4d91-8f62-5dd6be34a3e0}')
    @commethod(3)
    def ReadFileFragment(self, fragmentStart: POINTER(VoidPtr), fileOffset: UInt64, fragmentSize: UInt64, fragmentContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReleaseFileFragment(self, fragmentContext: VoidPtr) -> Void: ...
    @commethod(5)
    def GetFileSize(self, fileSize: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetLastWriteTime(self, lastWriteTime: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFontList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1a0d8438-1d97-4ec1-aef9-a2fb86ed6acb}')
    @commethod(3)
    def GetFontCollection(self, fontCollection: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFontCount(self) -> UInt32: ...
    @commethod(5)
    def GetFont(self, index: UInt32, font: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFont)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFontList1(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontList
    _iid_ = Guid('{da20d8ef-812a-4c43-9802-62ec4abd7ade}')
    @commethod(6)
    def GetFontLocality(self, listIndex: UInt32) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_LOCALITY: ...
    @commethod(7)
    def GetFont(self, listIndex: UInt32, font: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFont3)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetFontFaceReference(self, listIndex: UInt32, fontFaceReference: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFaceReference)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFontList2(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontList1
    _iid_ = Guid('{c0763a34-77af-445a-b735-08c37b0a5bf5}')
    @commethod(9)
    def GetFontSet(self, fontSet: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontSet1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFontResource(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1f803a76-6871-48e8-987f-b975551c50f2}')
    @commethod(3)
    def GetFontFile(self, fontFile: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFile)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFontFaceIndex(self) -> UInt32: ...
    @commethod(5)
    def GetFontAxisCount(self) -> UInt32: ...
    @commethod(6)
    def GetDefaultFontAxisValues(self, fontAxisValues: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE), fontAxisValueCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFontAxisRanges(self, fontAxisRanges: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_RANGE), fontAxisRangeCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetFontAxisAttributes(self, axisIndex: UInt32) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_ATTRIBUTES: ...
    @commethod(9)
    def GetAxisNames(self, axisIndex: UInt32, names: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteLocalizedStrings)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetAxisValueNameCount(self, axisIndex: UInt32) -> UInt32: ...
    @commethod(11)
    def GetAxisValueNames(self, axisIndex: UInt32, axisValueIndex: UInt32, fontAxisRange: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_RANGE), names: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteLocalizedStrings)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def HasVariations(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(13)
    def CreateFontFace(self, fontSimulations: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_SIMULATIONS, fontAxisValues: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE), fontAxisValueCount: UInt32, fontFace: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFace5)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CreateFontFaceReference(self, fontSimulations: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_SIMULATIONS, fontAxisValues: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE), fontAxisValueCount: UInt32, fontFaceReference: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFaceReference1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFontSet(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{53585141-d9f8-4095-8321-d73cf6bd116b}')
    @commethod(3)
    def GetFontCount(self) -> UInt32: ...
    @commethod(4)
    def GetFontFaceReference(self, listIndex: UInt32, fontFaceReference: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFaceReference)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def FindFontFaceReference(self, fontFaceReference: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFaceReference, listIndex: POINTER(UInt32), exists: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FindFontFace(self, fontFace: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFace, listIndex: POINTER(UInt32), exists: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPropertyValues(self, propertyID: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_PROPERTY_ID, values: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteStringList)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetPropertyValues(self, propertyID: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_PROPERTY_ID, preferredLocaleNames: win32more.Windows.Win32.Foundation.PWSTR, values: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteStringList)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetPropertyValues(self, listIndex: UInt32, propertyId: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_PROPERTY_ID, exists: POINTER(win32more.Windows.Win32.Foundation.BOOL), values: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteLocalizedStrings)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetPropertyOccurrenceCount(self, property: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_PROPERTY), propertyOccurrenceCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetMatchingFonts(self, familyName: win32more.Windows.Win32.Foundation.PWSTR, fontWeight: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_WEIGHT, fontStretch: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STRETCH, fontStyle: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STYLE, filteredSet: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetMatchingFonts(self, properties: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_PROPERTY), propertyCount: UInt32, filteredSet: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFontSet1(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontSet
    _iid_ = Guid('{7e9fda85-6c92-4053-bc47-7ae3530db4d3}')
    @commethod(13)
    def GetMatchingFonts(self, fontProperty: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_PROPERTY), fontAxisValues: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE), fontAxisValueCount: UInt32, matchingFonts: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontSet1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetFirstFontResources(self, filteredFontSet: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontSet1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetFilteredFonts(self, indices: POINTER(UInt32), indexCount: UInt32, filteredFontSet: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontSet1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetFilteredFonts(self, fontAxisRanges: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_RANGE), fontAxisRangeCount: UInt32, selectAnyRange: win32more.Windows.Win32.Foundation.BOOL, filteredFontSet: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontSet1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetFilteredFonts(self, properties: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_PROPERTY), propertyCount: UInt32, selectAnyProperty: win32more.Windows.Win32.Foundation.BOOL, filteredFontSet: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontSet1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetFilteredFontIndices(self, fontAxisRanges: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_RANGE), fontAxisRangeCount: UInt32, selectAnyRange: win32more.Windows.Win32.Foundation.BOOL, indices: POINTER(UInt32), maxIndexCount: UInt32, actualIndexCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetFilteredFontIndices(self, properties: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_PROPERTY), propertyCount: UInt32, selectAnyProperty: win32more.Windows.Win32.Foundation.BOOL, indices: POINTER(UInt32), maxIndexCount: UInt32, actualIndexCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetFontAxisRanges(self, listIndex: UInt32, fontAxisRanges: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_RANGE), maxFontAxisRangeCount: UInt32, actualFontAxisRangeCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetFontAxisRanges(self, fontAxisRanges: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_RANGE), maxFontAxisRangeCount: UInt32, actualFontAxisRangeCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetFontFaceReference(self, listIndex: UInt32, fontFaceReference: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFaceReference1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def CreateFontResource(self, listIndex: UInt32, fontResource: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontResource)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def CreateFontFace(self, listIndex: UInt32, fontFace: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFace5)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetFontLocality(self, listIndex: UInt32) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_LOCALITY: ...
class IDWriteFontSet2(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontSet1
    _iid_ = Guid('{dc7ead19-e54c-43af-b2da-4e2b79ba3f7f}')
    @commethod(26)
    def GetExpirationEvent(self) -> win32more.Windows.Win32.Foundation.HANDLE: ...
class IDWriteFontSet3(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontSet2
    _iid_ = Guid('{7c073ef2-a7f4-4045-8c32-8ab8ae640f90}')
    @commethod(27)
    def GetFontSourceType(self, fontIndex: UInt32) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_SOURCE_TYPE: ...
    @commethod(28)
    def GetFontSourceNameLength(self, listIndex: UInt32) -> UInt32: ...
    @commethod(29)
    def GetFontSourceName(self, listIndex: UInt32, stringBuffer: win32more.Windows.Win32.Foundation.PWSTR, stringBufferSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFontSet4(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontSet3
    _iid_ = Guid('{eec175fc-bea9-4c86-8b53-ccbdd7df0c82}')
    @commethod(30)
    def ConvertWeightStretchStyleToFontAxisValues(self, inputAxisValues: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE), inputAxisCount: UInt32, fontWeight: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_WEIGHT, fontStretch: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STRETCH, fontStyle: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STYLE, fontSize: Single, outputAxisValues: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE)) -> UInt32: ...
    @commethod(31)
    def GetMatchingFonts(self, familyName: win32more.Windows.Win32.Foundation.PWSTR, fontAxisValues: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE), fontAxisValueCount: UInt32, allowedSimulations: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_SIMULATIONS, matchingFonts: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontSet4)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFontSetBuilder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2f642afe-9c68-4f40-b8be-457401afcb3d}')
    @commethod(3)
    def AddFontFaceReference(self, fontFaceReference: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFaceReference, properties: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_PROPERTY), propertyCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddFontFaceReference(self, fontFaceReference: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFaceReference) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddFontSet(self, fontSet: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontSet) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateFontSet(self, fontSet: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFontSetBuilder1(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontSetBuilder
    _iid_ = Guid('{3ff7715f-3cdc-4dc6-9b72-ec5621dccafd}')
    @commethod(7)
    def AddFontFile(self, fontFile: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFile) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteFontSetBuilder2(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontSetBuilder1
    _iid_ = Guid('{ee5ba612-b131-463c-8f4f-3189b9401e45}')
    @commethod(8)
    def AddFont(self, fontFile: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFile, fontFaceIndex: UInt32, fontSimulations: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_SIMULATIONS, fontAxisValues: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE), fontAxisValueCount: UInt32, fontAxisRanges: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_RANGE), fontAxisRangeCount: UInt32, properties: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_PROPERTY), propertyCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddFontFile(self, filePath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteGdiInterop(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1edd9491-9853-4299-898f-6432983b6f3a}')
    @commethod(3)
    def CreateFontFromLOGFONT(self, logFont: POINTER(win32more.Windows.Win32.Graphics.Gdi.LOGFONTW), font: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFont)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ConvertFontToLOGFONT(self, font: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFont, logFont: POINTER(win32more.Windows.Win32.Graphics.Gdi.LOGFONTW), isSystemFont: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ConvertFontFaceToLOGFONT(self, font: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFace, logFont: POINTER(win32more.Windows.Win32.Graphics.Gdi.LOGFONTW)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateFontFaceFromHdc(self, hdc: win32more.Windows.Win32.Graphics.Gdi.HDC, fontFace: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFace)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateBitmapRenderTarget(self, hdc: win32more.Windows.Win32.Graphics.Gdi.HDC, width: UInt32, height: UInt32, renderTarget: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteBitmapRenderTarget)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteGdiInterop1(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteGdiInterop
    _iid_ = Guid('{4556be70-3abd-4f70-90be-421780a6f515}')
    @commethod(8)
    def CreateFontFromLOGFONT(self, logFont: POINTER(win32more.Windows.Win32.Graphics.Gdi.LOGFONTW), fontCollection: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontCollection, font: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFont)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFontSignature(self, fontFace: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFace, fontSignature: POINTER(win32more.Windows.Win32.Globalization.FONTSIGNATURE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFontSignature(self, font: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFont, fontSignature: POINTER(win32more.Windows.Win32.Globalization.FONTSIGNATURE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetMatchingFontsByLOGFONT(self, logFont: POINTER(win32more.Windows.Win32.Graphics.Gdi.LOGFONTA), fontSet: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontSet, filteredSet: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontSet)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteGlyphRunAnalysis(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7d97dbf7-e085-42d4-81e3-6a883bded118}')
    @commethod(3)
    def GetAlphaTextureBounds(self, textureType: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXTURE_TYPE, textureBounds: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateAlphaTexture(self, textureType: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXTURE_TYPE, textureBounds: POINTER(win32more.Windows.Win32.Foundation.RECT), alphaValues: POINTER(Byte), bufferSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAlphaBlendParams(self, renderingParams: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteRenderingParams, blendGamma: POINTER(Single), blendEnhancedContrast: POINTER(Single), blendClearTypeLevel: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteInMemoryFontFileLoader(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFileLoader
    _iid_ = Guid('{dc102f47-a12d-4b1c-822d-9e117e33043f}')
    @commethod(4)
    def CreateInMemoryFontFileReference(self, factory: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFactory, fontData: VoidPtr, fontDataSize: UInt32, ownerObject: win32more.Windows.Win32.System.Com.IUnknown, fontFile: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFile)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFileCount(self) -> UInt32: ...
class IDWriteInlineObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8339fde3-106f-47ab-8373-1c6295eb10b3}')
    @commethod(3)
    def Draw(self, clientDrawingContext: VoidPtr, renderer: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextRenderer, originX: Single, originY: Single, isSideways: win32more.Windows.Win32.Foundation.BOOL, isRightToLeft: win32more.Windows.Win32.Foundation.BOOL, clientDrawingEffect: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMetrics(self, metrics: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_INLINE_OBJECT_METRICS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetOverhangMetrics(self, overhangs: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_OVERHANG_METRICS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetBreakConditions(self, breakConditionBefore: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_BREAK_CONDITION), breakConditionAfter: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_BREAK_CONDITION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteLocalFontFileLoader(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFileLoader
    _iid_ = Guid('{b2d9f3ec-c9fe-4a11-a2ec-d86208f7c0a2}')
    @commethod(4)
    def GetFilePathLengthFromKey(self, fontFileReferenceKey: VoidPtr, fontFileReferenceKeySize: UInt32, filePathLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFilePathFromKey(self, fontFileReferenceKey: VoidPtr, fontFileReferenceKeySize: UInt32, filePath: win32more.Windows.Win32.Foundation.PWSTR, filePathSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetLastWriteTimeFromKey(self, fontFileReferenceKey: VoidPtr, fontFileReferenceKeySize: UInt32, lastWriteTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteLocalizedStrings(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{08256209-099a-4b34-b86d-c22b110e7771}')
    @commethod(3)
    def GetCount(self) -> UInt32: ...
    @commethod(4)
    def FindLocaleName(self, localeName: win32more.Windows.Win32.Foundation.PWSTR, index: POINTER(UInt32), exists: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLocaleNameLength(self, index: UInt32, length: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetLocaleName(self, index: UInt32, localeName: win32more.Windows.Win32.Foundation.PWSTR, size: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetStringLength(self, index: UInt32, length: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetString(self, index: UInt32, stringBuffer: win32more.Windows.Win32.Foundation.PWSTR, size: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteNumberSubstitution(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{14885cc9-bab0-4f90-b6ed-5c366a2cd03d}')
class IDWritePixelSnapping(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{eaf3a2da-ecf4-4d24-b644-b34f6842024b}')
    @commethod(3)
    def IsPixelSnappingDisabled(self, clientDrawingContext: VoidPtr, isDisabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentTransform(self, clientDrawingContext: VoidPtr, transform: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MATRIX)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPixelsPerDip(self, clientDrawingContext: VoidPtr, pixelsPerDip: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteRemoteFontFileLoader(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFileLoader
    _iid_ = Guid('{68648c83-6ede-46c0-ab46-20083a887fde}')
    @commethod(4)
    def CreateRemoteStreamFromKey(self, fontFileReferenceKey: VoidPtr, fontFileReferenceKeySize: UInt32, fontFileStream: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteRemoteFontFileStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLocalityFromKey(self, fontFileReferenceKey: VoidPtr, fontFileReferenceKeySize: UInt32, locality: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_LOCALITY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateFontFileReferenceFromUrl(self, factory: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFactory, baseUrl: win32more.Windows.Win32.Foundation.PWSTR, fontFileUrl: win32more.Windows.Win32.Foundation.PWSTR, fontFile: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFile)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteRemoteFontFileStream(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFileStream
    _iid_ = Guid('{4db3757a-2c72-4ed9-b2b6-1ababe1aff9c}')
    @commethod(7)
    def GetLocalFileSize(self, localFileSize: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetFileFragmentLocality(self, fileOffset: UInt64, fragmentSize: UInt64, isLocal: POINTER(win32more.Windows.Win32.Foundation.BOOL), partialSize: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetLocality(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_LOCALITY: ...
    @commethod(10)
    def BeginDownload(self, downloadOperationID: POINTER(Guid), fileFragments: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FILE_FRAGMENT), fragmentCount: UInt32, asyncResult: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteAsyncResult)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteRenderingParams(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2f0da53a-2add-47cd-82ee-d9ec34688e75}')
    @commethod(3)
    def GetGamma(self) -> Single: ...
    @commethod(4)
    def GetEnhancedContrast(self) -> Single: ...
    @commethod(5)
    def GetClearTypeLevel(self) -> Single: ...
    @commethod(6)
    def GetPixelGeometry(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PIXEL_GEOMETRY: ...
    @commethod(7)
    def GetRenderingMode(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE: ...
class IDWriteRenderingParams1(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteRenderingParams
    _iid_ = Guid('{94413cf4-a6fc-4248-8b50-6674348fcad3}')
    @commethod(8)
    def GetGrayscaleEnhancedContrast(self) -> Single: ...
class IDWriteRenderingParams2(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteRenderingParams1
    _iid_ = Guid('{f9d711c3-9777-40ae-87e8-3e5af9bf0948}')
    @commethod(9)
    def GetGridFitMode(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GRID_FIT_MODE: ...
class IDWriteRenderingParams3(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteRenderingParams2
    _iid_ = Guid('{b7924baa-391b-412a-8c5c-e44cc2d867dc}')
    @commethod(10)
    def GetRenderingMode1(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_RENDERING_MODE1: ...
class IDWriteStringList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cfee3140-1157-47ca-8b85-31bfcf3f2d0e}')
    @commethod(3)
    def GetCount(self) -> UInt32: ...
    @commethod(4)
    def GetLocaleNameLength(self, listIndex: UInt32, length: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLocaleName(self, listIndex: UInt32, localeName: win32more.Windows.Win32.Foundation.PWSTR, size: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetStringLength(self, listIndex: UInt32, length: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetString(self, listIndex: UInt32, stringBuffer: win32more.Windows.Win32.Foundation.PWSTR, stringBufferSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteTextAnalysisSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5810cd44-0ca0-4701-b3fa-bec5182ae4f6}')
    @commethod(3)
    def SetScriptAnalysis(self, textPosition: UInt32, textLength: UInt32, scriptAnalysis: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_SCRIPT_ANALYSIS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetLineBreakpoints(self, textPosition: UInt32, textLength: UInt32, lineBreakpoints: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_LINE_BREAKPOINT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetBidiLevel(self, textPosition: UInt32, textLength: UInt32, explicitLevel: Byte, resolvedLevel: Byte) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetNumberSubstitution(self, textPosition: UInt32, textLength: UInt32, numberSubstitution: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteNumberSubstitution) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteTextAnalysisSink1(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextAnalysisSink
    _iid_ = Guid('{b0d941a0-85e7-4d8b-9fd3-5ced9934482a}')
    @commethod(7)
    def SetGlyphOrientation(self, textPosition: UInt32, textLength: UInt32, glyphOrientationAngle: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_ORIENTATION_ANGLE, adjustedBidiLevel: Byte, isSideways: win32more.Windows.Win32.Foundation.BOOL, isRightToLeft: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteTextAnalysisSource(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{688e1a58-5094-47c8-adc8-fbcea60ae92b}')
    @commethod(3)
    def GetTextAtPosition(self, textPosition: UInt32, textString: POINTER(POINTER(UInt16)), textLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTextBeforePosition(self, textPosition: UInt32, textString: POINTER(POINTER(UInt16)), textLength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetParagraphReadingDirection(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_READING_DIRECTION: ...
    @commethod(6)
    def GetLocaleName(self, textPosition: UInt32, textLength: POINTER(UInt32), localeName: POINTER(POINTER(UInt16))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetNumberSubstitution(self, textPosition: UInt32, textLength: POINTER(UInt32), numberSubstitution: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteNumberSubstitution)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteTextAnalysisSource1(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextAnalysisSource
    _iid_ = Guid('{639cfad8-0fb4-4b21-a58a-067920120009}')
    @commethod(8)
    def GetVerticalGlyphOrientation(self, textPosition: UInt32, textLength: POINTER(UInt32), glyphOrientation: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_VERTICAL_GLYPH_ORIENTATION), bidiLevel: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteTextAnalyzer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b7e6163e-7f46-43b4-84b3-e4e6249c365d}')
    @commethod(3)
    def AnalyzeScript(self, analysisSource: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextAnalysisSource, textPosition: UInt32, textLength: UInt32, analysisSink: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextAnalysisSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AnalyzeBidi(self, analysisSource: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextAnalysisSource, textPosition: UInt32, textLength: UInt32, analysisSink: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextAnalysisSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AnalyzeNumberSubstitution(self, analysisSource: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextAnalysisSource, textPosition: UInt32, textLength: UInt32, analysisSink: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextAnalysisSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AnalyzeLineBreakpoints(self, analysisSource: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextAnalysisSource, textPosition: UInt32, textLength: UInt32, analysisSink: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextAnalysisSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetGlyphs(self, textString: win32more.Windows.Win32.Foundation.PWSTR, textLength: UInt32, fontFace: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFace, isSideways: win32more.Windows.Win32.Foundation.BOOL, isRightToLeft: win32more.Windows.Win32.Foundation.BOOL, scriptAnalysis: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_SCRIPT_ANALYSIS), localeName: win32more.Windows.Win32.Foundation.PWSTR, numberSubstitution: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteNumberSubstitution, features: POINTER(POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TYPOGRAPHIC_FEATURES)), featureRangeLengths: POINTER(UInt32), featureRanges: UInt32, maxGlyphCount: UInt32, clusterMap: POINTER(UInt16), textProps: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_SHAPING_TEXT_PROPERTIES), glyphIndices: POINTER(UInt16), glyphProps: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_SHAPING_GLYPH_PROPERTIES), actualGlyphCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetGlyphPlacements(self, textString: win32more.Windows.Win32.Foundation.PWSTR, clusterMap: POINTER(UInt16), textProps: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_SHAPING_TEXT_PROPERTIES), textLength: UInt32, glyphIndices: POINTER(UInt16), glyphProps: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_SHAPING_GLYPH_PROPERTIES), glyphCount: UInt32, fontFace: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFace, fontEmSize: Single, isSideways: win32more.Windows.Win32.Foundation.BOOL, isRightToLeft: win32more.Windows.Win32.Foundation.BOOL, scriptAnalysis: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_SCRIPT_ANALYSIS), localeName: win32more.Windows.Win32.Foundation.PWSTR, features: POINTER(POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TYPOGRAPHIC_FEATURES)), featureRangeLengths: POINTER(UInt32), featureRanges: UInt32, glyphAdvances: POINTER(Single), glyphOffsets: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_OFFSET)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetGdiCompatibleGlyphPlacements(self, textString: win32more.Windows.Win32.Foundation.PWSTR, clusterMap: POINTER(UInt16), textProps: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_SHAPING_TEXT_PROPERTIES), textLength: UInt32, glyphIndices: POINTER(UInt16), glyphProps: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_SHAPING_GLYPH_PROPERTIES), glyphCount: UInt32, fontFace: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFace, fontEmSize: Single, pixelsPerDip: Single, transform: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MATRIX), useGdiNatural: win32more.Windows.Win32.Foundation.BOOL, isSideways: win32more.Windows.Win32.Foundation.BOOL, isRightToLeft: win32more.Windows.Win32.Foundation.BOOL, scriptAnalysis: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_SCRIPT_ANALYSIS), localeName: win32more.Windows.Win32.Foundation.PWSTR, features: POINTER(POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TYPOGRAPHIC_FEATURES)), featureRangeLengths: POINTER(UInt32), featureRanges: UInt32, glyphAdvances: POINTER(Single), glyphOffsets: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_OFFSET)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteTextAnalyzer1(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextAnalyzer
    _iid_ = Guid('{80dad800-e21f-4e83-96ce-bfcce500db7c}')
    @commethod(10)
    def ApplyCharacterSpacing(self, leadingSpacing: Single, trailingSpacing: Single, minimumAdvanceWidth: Single, textLength: UInt32, glyphCount: UInt32, clusterMap: POINTER(UInt16), glyphAdvances: POINTER(Single), glyphOffsets: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_OFFSET), glyphProperties: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_SHAPING_GLYPH_PROPERTIES), modifiedGlyphAdvances: POINTER(Single), modifiedGlyphOffsets: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_OFFSET)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetBaseline(self, fontFace: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFace, baseline: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_BASELINE, isVertical: win32more.Windows.Win32.Foundation.BOOL, isSimulationAllowed: win32more.Windows.Win32.Foundation.BOOL, scriptAnalysis: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_SCRIPT_ANALYSIS, localeName: win32more.Windows.Win32.Foundation.PWSTR, baselineCoordinate: POINTER(Int32), exists: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def AnalyzeVerticalGlyphOrientation(self, analysisSource: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextAnalysisSource1, textPosition: UInt32, textLength: UInt32, analysisSink: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextAnalysisSink1) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetGlyphOrientationTransform(self, glyphOrientationAngle: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_ORIENTATION_ANGLE, isSideways: win32more.Windows.Win32.Foundation.BOOL, transform: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MATRIX)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetScriptProperties(self, scriptAnalysis: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_SCRIPT_ANALYSIS, scriptProperties: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_SCRIPT_PROPERTIES)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetTextComplexity(self, textString: win32more.Windows.Win32.Foundation.PWSTR, textLength: UInt32, fontFace: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFace, isTextSimple: POINTER(win32more.Windows.Win32.Foundation.BOOL), textLengthRead: POINTER(UInt32), glyphIndices: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetJustificationOpportunities(self, fontFace: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFace, fontEmSize: Single, scriptAnalysis: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_SCRIPT_ANALYSIS, textLength: UInt32, glyphCount: UInt32, textString: win32more.Windows.Win32.Foundation.PWSTR, clusterMap: POINTER(UInt16), glyphProperties: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_SHAPING_GLYPH_PROPERTIES), justificationOpportunities: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_JUSTIFICATION_OPPORTUNITY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def JustifyGlyphAdvances(self, lineWidth: Single, glyphCount: UInt32, justificationOpportunities: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_JUSTIFICATION_OPPORTUNITY), glyphAdvances: POINTER(Single), glyphOffsets: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_OFFSET), justifiedGlyphAdvances: POINTER(Single), justifiedGlyphOffsets: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_OFFSET)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetJustifiedGlyphs(self, fontFace: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFace, fontEmSize: Single, scriptAnalysis: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_SCRIPT_ANALYSIS, textLength: UInt32, glyphCount: UInt32, maxGlyphCount: UInt32, clusterMap: POINTER(UInt16), glyphIndices: POINTER(UInt16), glyphAdvances: POINTER(Single), justifiedGlyphAdvances: POINTER(Single), justifiedGlyphOffsets: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_OFFSET), glyphProperties: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_SHAPING_GLYPH_PROPERTIES), actualGlyphCount: POINTER(UInt32), modifiedClusterMap: POINTER(UInt16), modifiedGlyphIndices: POINTER(UInt16), modifiedGlyphAdvances: POINTER(Single), modifiedGlyphOffsets: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_OFFSET)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteTextAnalyzer2(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextAnalyzer1
    _iid_ = Guid('{553a9ff3-5693-4df7-b52b-74806f7f2eb9}')
    @commethod(19)
    def GetGlyphOrientationTransform(self, glyphOrientationAngle: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_ORIENTATION_ANGLE, isSideways: win32more.Windows.Win32.Foundation.BOOL, originX: Single, originY: Single, transform: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MATRIX)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetTypographicFeatures(self, fontFace: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFace, scriptAnalysis: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_SCRIPT_ANALYSIS, localeName: win32more.Windows.Win32.Foundation.PWSTR, maxTagCount: UInt32, actualTagCount: POINTER(UInt32), tags: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def CheckTypographicFeature(self, fontFace: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFace, scriptAnalysis: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_SCRIPT_ANALYSIS, localeName: win32more.Windows.Win32.Foundation.PWSTR, featureTag: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG, glyphCount: UInt32, glyphIndices: POINTER(UInt16), featureApplies: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteTextFormat(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9c906818-31d7-4fd3-a151-7c5e225db55a}')
    @commethod(3)
    def SetTextAlignment(self, textAlignment: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_ALIGNMENT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetParagraphAlignment(self, paragraphAlignment: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PARAGRAPH_ALIGNMENT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetWordWrapping(self, wordWrapping: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_WORD_WRAPPING) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetReadingDirection(self, readingDirection: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_READING_DIRECTION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetFlowDirection(self, flowDirection: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FLOW_DIRECTION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetIncrementalTabStop(self, incrementalTabStop: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetTrimming(self, trimmingOptions: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TRIMMING), trimmingSign: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteInlineObject) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetLineSpacing(self, lineSpacingMethod: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_LINE_SPACING_METHOD, lineSpacing: Single, baseline: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetTextAlignment(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_ALIGNMENT: ...
    @commethod(12)
    def GetParagraphAlignment(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_PARAGRAPH_ALIGNMENT: ...
    @commethod(13)
    def GetWordWrapping(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_WORD_WRAPPING: ...
    @commethod(14)
    def GetReadingDirection(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_READING_DIRECTION: ...
    @commethod(15)
    def GetFlowDirection(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FLOW_DIRECTION: ...
    @commethod(16)
    def GetIncrementalTabStop(self) -> Single: ...
    @commethod(17)
    def GetTrimming(self, trimmingOptions: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TRIMMING), trimmingSign: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteInlineObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetLineSpacing(self, lineSpacingMethod: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_LINE_SPACING_METHOD), lineSpacing: POINTER(Single), baseline: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetFontCollection(self, fontCollection: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontCollection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetFontFamilyNameLength(self) -> UInt32: ...
    @commethod(21)
    def GetFontFamilyName(self, fontFamilyName: win32more.Windows.Win32.Foundation.PWSTR, nameSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetFontWeight(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_WEIGHT: ...
    @commethod(23)
    def GetFontStyle(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STYLE: ...
    @commethod(24)
    def GetFontStretch(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STRETCH: ...
    @commethod(25)
    def GetFontSize(self) -> Single: ...
    @commethod(26)
    def GetLocaleNameLength(self) -> UInt32: ...
    @commethod(27)
    def GetLocaleName(self, localeName: win32more.Windows.Win32.Foundation.PWSTR, nameSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteTextFormat1(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextFormat
    _iid_ = Guid('{5f174b49-0d8b-4cfb-8bca-f1cce9d06c67}')
    @commethod(28)
    def SetVerticalGlyphOrientation(self, glyphOrientation: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_VERTICAL_GLYPH_ORIENTATION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetVerticalGlyphOrientation(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_VERTICAL_GLYPH_ORIENTATION: ...
    @commethod(30)
    def SetLastLineWrapping(self, isLastLineWrappingEnabled: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetLastLineWrapping(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(32)
    def SetOpticalAlignment(self, opticalAlignment: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_OPTICAL_ALIGNMENT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetOpticalAlignment(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_OPTICAL_ALIGNMENT: ...
    @commethod(34)
    def SetFontFallback(self, fontFallback: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetFontFallback(self, fontFallback: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFallback)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteTextFormat2(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextFormat1
    _iid_ = Guid('{f67e0edd-9e3d-4ecc-8c32-4183253dfe70}')
    @commethod(36)
    def SetLineSpacing(self, lineSpacingOptions: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_LINE_SPACING)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def GetLineSpacing(self, lineSpacingOptions: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_LINE_SPACING)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteTextFormat3(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextFormat2
    _iid_ = Guid('{6d3b5641-e550-430d-a85b-b7bf48a93427}')
    @commethod(38)
    def SetFontAxisValues(self, fontAxisValues: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE), fontAxisValueCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def GetFontAxisValueCount(self) -> UInt32: ...
    @commethod(40)
    def GetFontAxisValues(self, fontAxisValues: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE), fontAxisValueCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def GetAutomaticFontAxes(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_AUTOMATIC_FONT_AXES: ...
    @commethod(42)
    def SetAutomaticFontAxes(self, automaticFontAxes: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_AUTOMATIC_FONT_AXES) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteTextLayout(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextFormat
    _iid_ = Guid('{53737037-6d14-410b-9bfe-0b182bb70961}')
    @commethod(28)
    def SetMaxWidth(self, maxWidth: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetMaxHeight(self, maxHeight: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def SetFontCollection(self, fontCollection: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontCollection, textRange: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def SetFontFamilyName(self, fontFamilyName: win32more.Windows.Win32.Foundation.PWSTR, textRange: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def SetFontWeight(self, fontWeight: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_WEIGHT, textRange: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def SetFontStyle(self, fontStyle: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STYLE, textRange: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def SetFontStretch(self, fontStretch: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STRETCH, textRange: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def SetFontSize(self, fontSize: Single, textRange: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def SetUnderline(self, hasUnderline: win32more.Windows.Win32.Foundation.BOOL, textRange: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def SetStrikethrough(self, hasStrikethrough: win32more.Windows.Win32.Foundation.BOOL, textRange: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def SetDrawingEffect(self, drawingEffect: win32more.Windows.Win32.System.Com.IUnknown, textRange: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def SetInlineObject(self, inlineObject: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteInlineObject, textRange: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def SetTypography(self, typography: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTypography, textRange: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def SetLocaleName(self, localeName: win32more.Windows.Win32.Foundation.PWSTR, textRange: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def GetMaxWidth(self) -> Single: ...
    @commethod(43)
    def GetMaxHeight(self) -> Single: ...
    @commethod(44)
    def GetFontCollection(self, currentPosition: UInt32, fontCollection: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontCollection), textRange: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def GetFontFamilyNameLength(self, currentPosition: UInt32, nameLength: POINTER(UInt32), textRange: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def GetFontFamilyName(self, currentPosition: UInt32, fontFamilyName: win32more.Windows.Win32.Foundation.PWSTR, nameSize: UInt32, textRange: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def GetFontWeight(self, currentPosition: UInt32, fontWeight: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_WEIGHT), textRange: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def GetFontStyle(self, currentPosition: UInt32, fontStyle: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STYLE), textRange: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def GetFontStretch(self, currentPosition: UInt32, fontStretch: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_STRETCH), textRange: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def GetFontSize(self, currentPosition: UInt32, fontSize: POINTER(Single), textRange: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def GetUnderline(self, currentPosition: UInt32, hasUnderline: POINTER(win32more.Windows.Win32.Foundation.BOOL), textRange: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def GetStrikethrough(self, currentPosition: UInt32, hasStrikethrough: POINTER(win32more.Windows.Win32.Foundation.BOOL), textRange: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def GetDrawingEffect(self, currentPosition: UInt32, drawingEffect: POINTER(win32more.Windows.Win32.System.Com.IUnknown), textRange: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def GetInlineObject(self, currentPosition: UInt32, inlineObject: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteInlineObject), textRange: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def GetTypography(self, currentPosition: UInt32, typography: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTypography), textRange: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def GetLocaleNameLength(self, currentPosition: UInt32, nameLength: POINTER(UInt32), textRange: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def GetLocaleName(self, currentPosition: UInt32, localeName: win32more.Windows.Win32.Foundation.PWSTR, nameSize: UInt32, textRange: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def Draw(self, clientDrawingContext: VoidPtr, renderer: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextRenderer, originX: Single, originY: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def GetLineMetrics(self, lineMetrics: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_LINE_METRICS), maxLineCount: UInt32, actualLineCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def GetMetrics(self, textMetrics: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_METRICS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def GetOverhangMetrics(self, overhangs: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_OVERHANG_METRICS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def GetClusterMetrics(self, clusterMetrics: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_CLUSTER_METRICS), maxClusterCount: UInt32, actualClusterCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def DetermineMinWidth(self, minWidth: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def HitTestPoint(self, pointX: Single, pointY: Single, isTrailingHit: POINTER(win32more.Windows.Win32.Foundation.BOOL), isInside: POINTER(win32more.Windows.Win32.Foundation.BOOL), hitTestMetrics: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_HIT_TEST_METRICS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def HitTestTextPosition(self, textPosition: UInt32, isTrailingHit: win32more.Windows.Win32.Foundation.BOOL, pointX: POINTER(Single), pointY: POINTER(Single), hitTestMetrics: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_HIT_TEST_METRICS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def HitTestTextRange(self, textPosition: UInt32, textLength: UInt32, originX: Single, originY: Single, hitTestMetrics: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_HIT_TEST_METRICS), maxHitTestMetricsCount: UInt32, actualHitTestMetricsCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteTextLayout1(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextLayout
    _iid_ = Guid('{9064d822-80a7-465c-a986-df65f78b8feb}')
    @commethod(67)
    def SetPairKerning(self, isPairKerningEnabled: win32more.Windows.Win32.Foundation.BOOL, textRange: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(68)
    def GetPairKerning(self, currentPosition: UInt32, isPairKerningEnabled: POINTER(win32more.Windows.Win32.Foundation.BOOL), textRange: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def SetCharacterSpacing(self, leadingSpacing: Single, trailingSpacing: Single, minimumAdvanceWidth: Single, textRange: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(70)
    def GetCharacterSpacing(self, currentPosition: UInt32, leadingSpacing: POINTER(Single), trailingSpacing: POINTER(Single), minimumAdvanceWidth: POINTER(Single), textRange: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteTextLayout2(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextLayout1
    _iid_ = Guid('{1093c18f-8d5e-43f0-b064-0917311b525e}')
    @commethod(71)
    def GetMetrics(self, textMetrics: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_METRICS1)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(72)
    def SetVerticalGlyphOrientation(self, glyphOrientation: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_VERTICAL_GLYPH_ORIENTATION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(73)
    def GetVerticalGlyphOrientation(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_VERTICAL_GLYPH_ORIENTATION: ...
    @commethod(74)
    def SetLastLineWrapping(self, isLastLineWrappingEnabled: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(75)
    def GetLastLineWrapping(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(76)
    def SetOpticalAlignment(self, opticalAlignment: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_OPTICAL_ALIGNMENT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(77)
    def GetOpticalAlignment(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_OPTICAL_ALIGNMENT: ...
    @commethod(78)
    def SetFontFallback(self, fontFallback: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(79)
    def GetFontFallback(self, fontFallback: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.IDWriteFontFallback)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteTextLayout3(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextLayout2
    _iid_ = Guid('{07ddcd52-020e-4de8-ac33-6c953d83f92d}')
    @commethod(80)
    def InvalidateLayout(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(81)
    def SetLineSpacing(self, lineSpacingOptions: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_LINE_SPACING)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(82)
    def GetLineSpacing(self, lineSpacingOptions: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_LINE_SPACING)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(83)
    def GetLineMetrics(self, lineMetrics: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_LINE_METRICS1), maxLineCount: UInt32, actualLineCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteTextLayout4(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextLayout3
    _iid_ = Guid('{05a9bf42-223f-4441-b5fb-8263685f55e9}')
    @commethod(84)
    def SetFontAxisValues(self, fontAxisValues: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE), fontAxisValueCount: UInt32, textRange: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(85)
    def GetFontAxisValueCount(self, currentPosition: UInt32) -> UInt32: ...
    @commethod(86)
    def GetFontAxisValues(self, currentPosition: UInt32, fontAxisValues: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE), fontAxisValueCount: UInt32, textRange: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_TEXT_RANGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(87)
    def GetAutomaticFontAxes(self) -> win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_AUTOMATIC_FONT_AXES: ...
    @commethod(88)
    def SetAutomaticFontAxes(self, automaticFontAxes: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_AUTOMATIC_FONT_AXES) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteTextRenderer(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWritePixelSnapping
    _iid_ = Guid('{ef8a8135-5cc6-45fe-8825-c5a0724eb819}')
    @commethod(6)
    def DrawGlyphRun(self, clientDrawingContext: VoidPtr, baselineOriginX: Single, baselineOriginY: Single, measuringMode: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MEASURING_MODE, glyphRun: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_RUN), glyphRunDescription: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_RUN_DESCRIPTION), clientDrawingEffect: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DrawUnderline(self, clientDrawingContext: VoidPtr, baselineOriginX: Single, baselineOriginY: Single, underline: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_UNDERLINE), clientDrawingEffect: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def DrawStrikethrough(self, clientDrawingContext: VoidPtr, baselineOriginX: Single, baselineOriginY: Single, strikethrough: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_STRIKETHROUGH), clientDrawingEffect: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def DrawInlineObject(self, clientDrawingContext: VoidPtr, originX: Single, originY: Single, inlineObject: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteInlineObject, isSideways: win32more.Windows.Win32.Foundation.BOOL, isRightToLeft: win32more.Windows.Win32.Foundation.BOOL, clientDrawingEffect: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteTextRenderer1(ComPtr):
    extends: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteTextRenderer
    _iid_ = Guid('{d3e0e934-22a0-427e-aae4-7d9574b59db1}')
    @commethod(10)
    def DrawGlyphRun(self, clientDrawingContext: VoidPtr, baselineOriginX: Single, baselineOriginY: Single, orientationAngle: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_ORIENTATION_ANGLE, measuringMode: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_MEASURING_MODE, glyphRun: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_RUN), glyphRunDescription: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_RUN_DESCRIPTION), clientDrawingEffect: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def DrawUnderline(self, clientDrawingContext: VoidPtr, baselineOriginX: Single, baselineOriginY: Single, orientationAngle: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_ORIENTATION_ANGLE, underline: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_UNDERLINE), clientDrawingEffect: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def DrawStrikethrough(self, clientDrawingContext: VoidPtr, baselineOriginX: Single, baselineOriginY: Single, orientationAngle: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_ORIENTATION_ANGLE, strikethrough: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_STRIKETHROUGH), clientDrawingEffect: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def DrawInlineObject(self, clientDrawingContext: VoidPtr, originX: Single, originY: Single, orientationAngle: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_GLYPH_ORIENTATION_ANGLE, inlineObject: win32more.Windows.Win32.Graphics.DirectWrite.IDWriteInlineObject, isSideways: win32more.Windows.Win32.Foundation.BOOL, isRightToLeft: win32more.Windows.Win32.Foundation.BOOL, clientDrawingEffect: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDWriteTypography(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{55f1112b-1dc2-4b3c-9541-f46894ed85b6}')
    @commethod(3)
    def AddFontFeature(self, fontFeature: win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFontFeatureCount(self) -> UInt32: ...
    @commethod(5)
    def GetFontFeature(self, fontFeatureIndex: UInt32, fontFeature: POINTER(win32more.Windows.Win32.Graphics.DirectWrite.DWRITE_FONT_FEATURE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
