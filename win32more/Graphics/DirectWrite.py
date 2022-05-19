from win32more import *
import win32more.Foundation
import win32more.Globalization
import win32more.Graphics.Direct2D.Common
import win32more.Graphics.DirectWrite
import win32more.Graphics.Gdi
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
DWRITE_ALPHA_MAX = 255
FACILITY_DWRITE = 2200
DWRITE_ERR_BASE = 20480
DWRITE_E_REMOTEFONT = -2003283955
DWRITE_E_DOWNLOADCANCELLED = -2003283954
DWRITE_E_DOWNLOADFAILED = -2003283953
DWRITE_E_TOOMANYDOWNLOADS = -2003283952
DWRITE_FONT_AXIS_TAG = UInt32
DWRITE_FONT_AXIS_TAG_WEIGHT = 1952999287
DWRITE_FONT_AXIS_TAG_WIDTH = 1752458359
DWRITE_FONT_AXIS_TAG_SLANT = 1953393779
DWRITE_FONT_AXIS_TAG_OPTICAL_SIZE = 2054385775
DWRITE_FONT_AXIS_TAG_ITALIC = 1818326121
def _define_DWRITE_COLOR_F_head():
    class DWRITE_COLOR_F(Structure):
        pass
    return DWRITE_COLOR_F
def _define_DWRITE_COLOR_F():
    DWRITE_COLOR_F = win32more.Graphics.DirectWrite.DWRITE_COLOR_F_head
    DWRITE_COLOR_F._fields_ = [
        ("r", Single),
        ("g", Single),
        ("b", Single),
        ("a", Single),
    ]
    return DWRITE_COLOR_F
DWRITE_MEASURING_MODE = Int32
DWRITE_MEASURING_MODE_NATURAL = 0
DWRITE_MEASURING_MODE_GDI_CLASSIC = 1
DWRITE_MEASURING_MODE_GDI_NATURAL = 2
DWRITE_GLYPH_IMAGE_FORMATS = UInt32
DWRITE_GLYPH_IMAGE_FORMATS_NONE = 0
DWRITE_GLYPH_IMAGE_FORMATS_TRUETYPE = 1
DWRITE_GLYPH_IMAGE_FORMATS_CFF = 2
DWRITE_GLYPH_IMAGE_FORMATS_COLR = 4
DWRITE_GLYPH_IMAGE_FORMATS_SVG = 8
DWRITE_GLYPH_IMAGE_FORMATS_PNG = 16
DWRITE_GLYPH_IMAGE_FORMATS_JPEG = 32
DWRITE_GLYPH_IMAGE_FORMATS_TIFF = 64
DWRITE_GLYPH_IMAGE_FORMATS_PREMULTIPLIED_B8G8R8A8 = 128
DWRITE_FONT_FILE_TYPE = Int32
DWRITE_FONT_FILE_TYPE_UNKNOWN = 0
DWRITE_FONT_FILE_TYPE_CFF = 1
DWRITE_FONT_FILE_TYPE_TRUETYPE = 2
DWRITE_FONT_FILE_TYPE_OPENTYPE_COLLECTION = 3
DWRITE_FONT_FILE_TYPE_TYPE1_PFM = 4
DWRITE_FONT_FILE_TYPE_TYPE1_PFB = 5
DWRITE_FONT_FILE_TYPE_VECTOR = 6
DWRITE_FONT_FILE_TYPE_BITMAP = 7
DWRITE_FONT_FILE_TYPE_TRUETYPE_COLLECTION = 3
DWRITE_FONT_FACE_TYPE = Int32
DWRITE_FONT_FACE_TYPE_CFF = 0
DWRITE_FONT_FACE_TYPE_TRUETYPE = 1
DWRITE_FONT_FACE_TYPE_OPENTYPE_COLLECTION = 2
DWRITE_FONT_FACE_TYPE_TYPE1 = 3
DWRITE_FONT_FACE_TYPE_VECTOR = 4
DWRITE_FONT_FACE_TYPE_BITMAP = 5
DWRITE_FONT_FACE_TYPE_UNKNOWN = 6
DWRITE_FONT_FACE_TYPE_RAW_CFF = 7
DWRITE_FONT_FACE_TYPE_TRUETYPE_COLLECTION = 2
DWRITE_FONT_SIMULATIONS = UInt32
DWRITE_FONT_SIMULATIONS_NONE = 0
DWRITE_FONT_SIMULATIONS_BOLD = 1
DWRITE_FONT_SIMULATIONS_OBLIQUE = 2
DWRITE_FONT_WEIGHT = Int32
DWRITE_FONT_WEIGHT_THIN = 100
DWRITE_FONT_WEIGHT_EXTRA_LIGHT = 200
DWRITE_FONT_WEIGHT_ULTRA_LIGHT = 200
DWRITE_FONT_WEIGHT_LIGHT = 300
DWRITE_FONT_WEIGHT_SEMI_LIGHT = 350
DWRITE_FONT_WEIGHT_NORMAL = 400
DWRITE_FONT_WEIGHT_REGULAR = 400
DWRITE_FONT_WEIGHT_MEDIUM = 500
DWRITE_FONT_WEIGHT_DEMI_BOLD = 600
DWRITE_FONT_WEIGHT_SEMI_BOLD = 600
DWRITE_FONT_WEIGHT_BOLD = 700
DWRITE_FONT_WEIGHT_EXTRA_BOLD = 800
DWRITE_FONT_WEIGHT_ULTRA_BOLD = 800
DWRITE_FONT_WEIGHT_BLACK = 900
DWRITE_FONT_WEIGHT_HEAVY = 900
DWRITE_FONT_WEIGHT_EXTRA_BLACK = 950
DWRITE_FONT_WEIGHT_ULTRA_BLACK = 950
DWRITE_FONT_STRETCH = Int32
DWRITE_FONT_STRETCH_UNDEFINED = 0
DWRITE_FONT_STRETCH_ULTRA_CONDENSED = 1
DWRITE_FONT_STRETCH_EXTRA_CONDENSED = 2
DWRITE_FONT_STRETCH_CONDENSED = 3
DWRITE_FONT_STRETCH_SEMI_CONDENSED = 4
DWRITE_FONT_STRETCH_NORMAL = 5
DWRITE_FONT_STRETCH_MEDIUM = 5
DWRITE_FONT_STRETCH_SEMI_EXPANDED = 6
DWRITE_FONT_STRETCH_EXPANDED = 7
DWRITE_FONT_STRETCH_EXTRA_EXPANDED = 8
DWRITE_FONT_STRETCH_ULTRA_EXPANDED = 9
DWRITE_FONT_STYLE = Int32
DWRITE_FONT_STYLE_NORMAL = 0
DWRITE_FONT_STYLE_OBLIQUE = 1
DWRITE_FONT_STYLE_ITALIC = 2
DWRITE_INFORMATIONAL_STRING_ID = Int32
DWRITE_INFORMATIONAL_STRING_NONE = 0
DWRITE_INFORMATIONAL_STRING_COPYRIGHT_NOTICE = 1
DWRITE_INFORMATIONAL_STRING_VERSION_STRINGS = 2
DWRITE_INFORMATIONAL_STRING_TRADEMARK = 3
DWRITE_INFORMATIONAL_STRING_MANUFACTURER = 4
DWRITE_INFORMATIONAL_STRING_DESIGNER = 5
DWRITE_INFORMATIONAL_STRING_DESIGNER_URL = 6
DWRITE_INFORMATIONAL_STRING_DESCRIPTION = 7
DWRITE_INFORMATIONAL_STRING_FONT_VENDOR_URL = 8
DWRITE_INFORMATIONAL_STRING_LICENSE_DESCRIPTION = 9
DWRITE_INFORMATIONAL_STRING_LICENSE_INFO_URL = 10
DWRITE_INFORMATIONAL_STRING_WIN32_FAMILY_NAMES = 11
DWRITE_INFORMATIONAL_STRING_WIN32_SUBFAMILY_NAMES = 12
DWRITE_INFORMATIONAL_STRING_TYPOGRAPHIC_FAMILY_NAMES = 13
DWRITE_INFORMATIONAL_STRING_TYPOGRAPHIC_SUBFAMILY_NAMES = 14
DWRITE_INFORMATIONAL_STRING_SAMPLE_TEXT = 15
DWRITE_INFORMATIONAL_STRING_FULL_NAME = 16
DWRITE_INFORMATIONAL_STRING_POSTSCRIPT_NAME = 17
DWRITE_INFORMATIONAL_STRING_POSTSCRIPT_CID_NAME = 18
DWRITE_INFORMATIONAL_STRING_WEIGHT_STRETCH_STYLE_FAMILY_NAME = 19
DWRITE_INFORMATIONAL_STRING_DESIGN_SCRIPT_LANGUAGE_TAG = 20
DWRITE_INFORMATIONAL_STRING_SUPPORTED_SCRIPT_LANGUAGE_TAG = 21
DWRITE_INFORMATIONAL_STRING_PREFERRED_FAMILY_NAMES = 13
DWRITE_INFORMATIONAL_STRING_PREFERRED_SUBFAMILY_NAMES = 14
DWRITE_INFORMATIONAL_STRING_WWS_FAMILY_NAME = 19
def _define_DWRITE_FONT_METRICS_head():
    class DWRITE_FONT_METRICS(Structure):
        pass
    return DWRITE_FONT_METRICS
def _define_DWRITE_FONT_METRICS():
    DWRITE_FONT_METRICS = win32more.Graphics.DirectWrite.DWRITE_FONT_METRICS_head
    DWRITE_FONT_METRICS._fields_ = [
        ("designUnitsPerEm", UInt16),
        ("ascent", UInt16),
        ("descent", UInt16),
        ("lineGap", Int16),
        ("capHeight", UInt16),
        ("xHeight", UInt16),
        ("underlinePosition", Int16),
        ("underlineThickness", UInt16),
        ("strikethroughPosition", Int16),
        ("strikethroughThickness", UInt16),
    ]
    return DWRITE_FONT_METRICS
def _define_DWRITE_GLYPH_METRICS_head():
    class DWRITE_GLYPH_METRICS(Structure):
        pass
    return DWRITE_GLYPH_METRICS
def _define_DWRITE_GLYPH_METRICS():
    DWRITE_GLYPH_METRICS = win32more.Graphics.DirectWrite.DWRITE_GLYPH_METRICS_head
    DWRITE_GLYPH_METRICS._fields_ = [
        ("leftSideBearing", Int32),
        ("advanceWidth", UInt32),
        ("rightSideBearing", Int32),
        ("topSideBearing", Int32),
        ("advanceHeight", UInt32),
        ("bottomSideBearing", Int32),
        ("verticalOriginY", Int32),
    ]
    return DWRITE_GLYPH_METRICS
def _define_DWRITE_GLYPH_OFFSET_head():
    class DWRITE_GLYPH_OFFSET(Structure):
        pass
    return DWRITE_GLYPH_OFFSET
def _define_DWRITE_GLYPH_OFFSET():
    DWRITE_GLYPH_OFFSET = win32more.Graphics.DirectWrite.DWRITE_GLYPH_OFFSET_head
    DWRITE_GLYPH_OFFSET._fields_ = [
        ("advanceOffset", Single),
        ("ascenderOffset", Single),
    ]
    return DWRITE_GLYPH_OFFSET
DWRITE_FACTORY_TYPE = Int32
DWRITE_FACTORY_TYPE_SHARED = 0
DWRITE_FACTORY_TYPE_ISOLATED = 1
def _define_IDWriteFontFileLoader_head():
    class IDWriteFontFileLoader(win32more.System.Com.IUnknown_head):
        Guid = Guid('727cad4e-d6af-4c9e-8a08-d695b11caa49')
    return IDWriteFontFileLoader
def _define_IDWriteFontFileLoader():
    IDWriteFontFileLoader = win32more.Graphics.DirectWrite.IDWriteFontFileLoader_head
    IDWriteFontFileLoader.CreateStreamFromKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFileStream_head), use_last_error=False)(3, 'CreateStreamFromKey', ((1, 'fontFileReferenceKey'),(1, 'fontFileReferenceKeySize'),(1, 'fontFileStream'),)))
    return IDWriteFontFileLoader
def _define_IDWriteLocalFontFileLoader_head():
    class IDWriteLocalFontFileLoader(win32more.Graphics.DirectWrite.IDWriteFontFileLoader_head):
        Guid = Guid('b2d9f3ec-c9fe-4a11-a2ec-d86208f7c0a2')
    return IDWriteLocalFontFileLoader
def _define_IDWriteLocalFontFileLoader():
    IDWriteLocalFontFileLoader = win32more.Graphics.DirectWrite.IDWriteLocalFontFileLoader_head
    IDWriteLocalFontFileLoader.GetFilePathLengthFromKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(4, 'GetFilePathLengthFromKey', ((1, 'fontFileReferenceKey'),(1, 'fontFileReferenceKeySize'),(1, 'filePathLength'),)))
    IDWriteLocalFontFileLoader.GetFilePathFromKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(Char),UInt32, use_last_error=False)(5, 'GetFilePathFromKey', ((1, 'fontFileReferenceKey'),(1, 'fontFileReferenceKeySize'),(1, 'filePath'),(1, 'filePathSize'),)))
    IDWriteLocalFontFileLoader.GetLastWriteTimeFromKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(6, 'GetLastWriteTimeFromKey', ((1, 'fontFileReferenceKey'),(1, 'fontFileReferenceKeySize'),(1, 'lastWriteTime'),)))
    return IDWriteLocalFontFileLoader
def _define_IDWriteFontFileStream_head():
    class IDWriteFontFileStream(win32more.System.Com.IUnknown_head):
        Guid = Guid('6d4865fe-0ab8-4d91-8f62-5dd6be34a3e0')
    return IDWriteFontFileStream
def _define_IDWriteFontFileStream():
    IDWriteFontFileStream = win32more.Graphics.DirectWrite.IDWriteFontFileStream_head
    IDWriteFontFileStream.ReadFileFragment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_void_p),UInt64,UInt64,POINTER(c_void_p), use_last_error=False)(3, 'ReadFileFragment', ((1, 'fragmentStart'),(1, 'fileOffset'),(1, 'fragmentSize'),(1, 'fragmentContext'),)))
    IDWriteFontFileStream.ReleaseFileFragment = COMMETHOD(WINFUNCTYPE(Void,c_void_p, use_last_error=False)(4, 'ReleaseFileFragment', ((1, 'fragmentContext'),)))
    IDWriteFontFileStream.GetFileSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(5, 'GetFileSize', ((1, 'fileSize'),)))
    IDWriteFontFileStream.GetLastWriteTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(6, 'GetLastWriteTime', ((1, 'lastWriteTime'),)))
    return IDWriteFontFileStream
def _define_IDWriteFontFile_head():
    class IDWriteFontFile(win32more.System.Com.IUnknown_head):
        Guid = Guid('739d886a-cef5-47dc-8769-1a8b41bebbb0')
    return IDWriteFontFile
def _define_IDWriteFontFile():
    IDWriteFontFile = win32more.Graphics.DirectWrite.IDWriteFontFile_head
    IDWriteFontFile.GetReferenceKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_void_p),POINTER(UInt32), use_last_error=False)(3, 'GetReferenceKey', ((1, 'fontFileReferenceKey'),(1, 'fontFileReferenceKeySize'),)))
    IDWriteFontFile.GetLoader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFileLoader_head), use_last_error=False)(4, 'GetLoader', ((1, 'fontFileLoader'),)))
    IDWriteFontFile.Analyze = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_FILE_TYPE),POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_FACE_TYPE),POINTER(UInt32), use_last_error=False)(5, 'Analyze', ((1, 'isSupportedFontType'),(1, 'fontFileType'),(1, 'fontFaceType'),(1, 'numberOfFaces'),)))
    return IDWriteFontFile
DWRITE_PIXEL_GEOMETRY = Int32
DWRITE_PIXEL_GEOMETRY_FLAT = 0
DWRITE_PIXEL_GEOMETRY_RGB = 1
DWRITE_PIXEL_GEOMETRY_BGR = 2
DWRITE_RENDERING_MODE = Int32
DWRITE_RENDERING_MODE_DEFAULT = 0
DWRITE_RENDERING_MODE_ALIASED = 1
DWRITE_RENDERING_MODE_GDI_CLASSIC = 2
DWRITE_RENDERING_MODE_GDI_NATURAL = 3
DWRITE_RENDERING_MODE_NATURAL = 4
DWRITE_RENDERING_MODE_NATURAL_SYMMETRIC = 5
DWRITE_RENDERING_MODE_OUTLINE = 6
DWRITE_RENDERING_MODE_CLEARTYPE_GDI_CLASSIC = 2
DWRITE_RENDERING_MODE_CLEARTYPE_GDI_NATURAL = 3
DWRITE_RENDERING_MODE_CLEARTYPE_NATURAL = 4
DWRITE_RENDERING_MODE_CLEARTYPE_NATURAL_SYMMETRIC = 5
def _define_DWRITE_MATRIX_head():
    class DWRITE_MATRIX(Structure):
        pass
    return DWRITE_MATRIX
def _define_DWRITE_MATRIX():
    DWRITE_MATRIX = win32more.Graphics.DirectWrite.DWRITE_MATRIX_head
    DWRITE_MATRIX._fields_ = [
        ("m11", Single),
        ("m12", Single),
        ("m21", Single),
        ("m22", Single),
        ("dx", Single),
        ("dy", Single),
    ]
    return DWRITE_MATRIX
def _define_IDWriteRenderingParams_head():
    class IDWriteRenderingParams(win32more.System.Com.IUnknown_head):
        Guid = Guid('2f0da53a-2add-47cd-82ee-d9ec34688e75')
    return IDWriteRenderingParams
def _define_IDWriteRenderingParams():
    IDWriteRenderingParams = win32more.Graphics.DirectWrite.IDWriteRenderingParams_head
    IDWriteRenderingParams.GetGamma = COMMETHOD(WINFUNCTYPE(Single, use_last_error=False)(3, 'GetGamma', ()))
    IDWriteRenderingParams.GetEnhancedContrast = COMMETHOD(WINFUNCTYPE(Single, use_last_error=False)(4, 'GetEnhancedContrast', ()))
    IDWriteRenderingParams.GetClearTypeLevel = COMMETHOD(WINFUNCTYPE(Single, use_last_error=False)(5, 'GetClearTypeLevel', ()))
    IDWriteRenderingParams.GetPixelGeometry = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_PIXEL_GEOMETRY, use_last_error=False)(6, 'GetPixelGeometry', ()))
    IDWriteRenderingParams.GetRenderingMode = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_RENDERING_MODE, use_last_error=False)(7, 'GetRenderingMode', ()))
    return IDWriteRenderingParams
def _define_IDWriteFontFace_head():
    class IDWriteFontFace(win32more.System.Com.IUnknown_head):
        Guid = Guid('5f49804d-7024-4d43-bfa9-d25984f53849')
    return IDWriteFontFace
def _define_IDWriteFontFace():
    IDWriteFontFace = win32more.Graphics.DirectWrite.IDWriteFontFace_head
    IDWriteFontFace.GetType = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_FONT_FACE_TYPE, use_last_error=False)(3, 'GetType', ()))
    IDWriteFontFace.GetFiles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(win32more.Graphics.DirectWrite.IDWriteFontFile_head), use_last_error=False)(4, 'GetFiles', ((1, 'numberOfFiles'),(1, 'fontFiles'),)))
    IDWriteFontFace.GetIndex = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(5, 'GetIndex', ()))
    IDWriteFontFace.GetSimulations = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_FONT_SIMULATIONS, use_last_error=False)(6, 'GetSimulations', ()))
    IDWriteFontFace.IsSymbolFont = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(7, 'IsSymbolFont', ()))
    IDWriteFontFace.GetMetrics = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_METRICS_head), use_last_error=False)(8, 'GetMetrics', ((1, 'fontFaceMetrics'),)))
    IDWriteFontFace.GetGlyphCount = COMMETHOD(WINFUNCTYPE(UInt16, use_last_error=False)(9, 'GetGlyphCount', ()))
    IDWriteFontFace.GetDesignGlyphMetrics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),UInt32,POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_METRICS),win32more.Foundation.BOOL, use_last_error=False)(10, 'GetDesignGlyphMetrics', ((1, 'glyphIndices'),(1, 'glyphCount'),(1, 'glyphMetrics'),(1, 'isSideways'),)))
    IDWriteFontFace.GetGlyphIndices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),UInt32,POINTER(UInt16), use_last_error=False)(11, 'GetGlyphIndices', ((1, 'codePoints'),(1, 'codePointCount'),(1, 'glyphIndices'),)))
    IDWriteFontFace.TryGetFontTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(c_void_p),POINTER(UInt32),POINTER(c_void_p),POINTER(win32more.Foundation.BOOL), use_last_error=False)(12, 'TryGetFontTable', ((1, 'openTypeTableTag'),(1, 'tableData'),(1, 'tableSize'),(1, 'tableContext'),(1, 'exists'),)))
    IDWriteFontFace.ReleaseFontTable = COMMETHOD(WINFUNCTYPE(Void,c_void_p, use_last_error=False)(13, 'ReleaseFontTable', ((1, 'tableContext'),)))
    IDWriteFontFace.GetGlyphRunOutline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,POINTER(UInt16),POINTER(Single),POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_OFFSET),UInt32,win32more.Foundation.BOOL,win32more.Foundation.BOOL,win32more.Graphics.Direct2D.Common.ID2D1SimplifiedGeometrySink_head, use_last_error=False)(14, 'GetGlyphRunOutline', ((1, 'emSize'),(1, 'glyphIndices'),(1, 'glyphAdvances'),(1, 'glyphOffsets'),(1, 'glyphCount'),(1, 'isSideways'),(1, 'isRightToLeft'),(1, 'geometrySink'),)))
    IDWriteFontFace.GetRecommendedRenderingMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,win32more.Graphics.DirectWrite.DWRITE_MEASURING_MODE,win32more.Graphics.DirectWrite.IDWriteRenderingParams_head,POINTER(win32more.Graphics.DirectWrite.DWRITE_RENDERING_MODE), use_last_error=False)(15, 'GetRecommendedRenderingMode', ((1, 'emSize'),(1, 'pixelsPerDip'),(1, 'measuringMode'),(1, 'renderingParams'),(1, 'renderingMode'),)))
    IDWriteFontFace.GetGdiCompatibleMetrics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,POINTER(win32more.Graphics.DirectWrite.DWRITE_MATRIX_head),POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_METRICS_head), use_last_error=False)(16, 'GetGdiCompatibleMetrics', ((1, 'emSize'),(1, 'pixelsPerDip'),(1, 'transform'),(1, 'fontFaceMetrics'),)))
    IDWriteFontFace.GetGdiCompatibleGlyphMetrics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,POINTER(win32more.Graphics.DirectWrite.DWRITE_MATRIX_head),win32more.Foundation.BOOL,POINTER(UInt16),UInt32,POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_METRICS),win32more.Foundation.BOOL, use_last_error=False)(17, 'GetGdiCompatibleGlyphMetrics', ((1, 'emSize'),(1, 'pixelsPerDip'),(1, 'transform'),(1, 'useGdiNatural'),(1, 'glyphIndices'),(1, 'glyphCount'),(1, 'glyphMetrics'),(1, 'isSideways'),)))
    return IDWriteFontFace
def _define_IDWriteFontCollectionLoader_head():
    class IDWriteFontCollectionLoader(win32more.System.Com.IUnknown_head):
        Guid = Guid('cca920e4-52f0-492b-bfa8-29c72ee0a468')
    return IDWriteFontCollectionLoader
def _define_IDWriteFontCollectionLoader():
    IDWriteFontCollectionLoader = win32more.Graphics.DirectWrite.IDWriteFontCollectionLoader_head
    IDWriteFontCollectionLoader.CreateEnumeratorFromKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFactory_head,c_void_p,UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFileEnumerator_head), use_last_error=False)(3, 'CreateEnumeratorFromKey', ((1, 'factory'),(1, 'collectionKey'),(1, 'collectionKeySize'),(1, 'fontFileEnumerator'),)))
    return IDWriteFontCollectionLoader
def _define_IDWriteFontFileEnumerator_head():
    class IDWriteFontFileEnumerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('72755049-5ff7-435d-8348-4be97cfa6c7c')
    return IDWriteFontFileEnumerator
def _define_IDWriteFontFileEnumerator():
    IDWriteFontFileEnumerator = win32more.Graphics.DirectWrite.IDWriteFontFileEnumerator_head
    IDWriteFontFileEnumerator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'MoveNext', ((1, 'hasCurrentFile'),)))
    IDWriteFontFileEnumerator.GetCurrentFontFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFile_head), use_last_error=False)(4, 'GetCurrentFontFile', ((1, 'fontFile'),)))
    return IDWriteFontFileEnumerator
def _define_IDWriteLocalizedStrings_head():
    class IDWriteLocalizedStrings(win32more.System.Com.IUnknown_head):
        Guid = Guid('08256209-099a-4b34-b86d-c22b110e7771')
    return IDWriteLocalizedStrings
def _define_IDWriteLocalizedStrings():
    IDWriteLocalizedStrings = win32more.Graphics.DirectWrite.IDWriteLocalizedStrings_head
    IDWriteLocalizedStrings.GetCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(3, 'GetCount', ()))
    IDWriteLocalizedStrings.FindLocaleName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'FindLocaleName', ((1, 'localeName'),(1, 'index'),(1, 'exists'),)))
    IDWriteLocalizedStrings.GetLocaleNameLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(5, 'GetLocaleNameLength', ((1, 'index'),(1, 'length'),)))
    IDWriteLocalizedStrings.GetLocaleName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Char),UInt32, use_last_error=False)(6, 'GetLocaleName', ((1, 'index'),(1, 'localeName'),(1, 'size'),)))
    IDWriteLocalizedStrings.GetStringLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(7, 'GetStringLength', ((1, 'index'),(1, 'length'),)))
    IDWriteLocalizedStrings.GetString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Char),UInt32, use_last_error=False)(8, 'GetString', ((1, 'index'),(1, 'stringBuffer'),(1, 'size'),)))
    return IDWriteLocalizedStrings
def _define_IDWriteFontCollection_head():
    class IDWriteFontCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('a84cee02-3eea-4eee-a827-87c1a02a0fcc')
    return IDWriteFontCollection
def _define_IDWriteFontCollection():
    IDWriteFontCollection = win32more.Graphics.DirectWrite.IDWriteFontCollection_head
    IDWriteFontCollection.GetFontFamilyCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(3, 'GetFontFamilyCount', ()))
    IDWriteFontCollection.GetFontFamily = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFamily_head), use_last_error=False)(4, 'GetFontFamily', ((1, 'index'),(1, 'fontFamily'),)))
    IDWriteFontCollection.FindFamilyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'FindFamilyName', ((1, 'familyName'),(1, 'index'),(1, 'exists'),)))
    IDWriteFontCollection.GetFontFromFontFace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFontFace_head,POINTER(win32more.Graphics.DirectWrite.IDWriteFont_head), use_last_error=False)(6, 'GetFontFromFontFace', ((1, 'fontFace'),(1, 'font'),)))
    return IDWriteFontCollection
def _define_IDWriteFontList_head():
    class IDWriteFontList(win32more.System.Com.IUnknown_head):
        Guid = Guid('1a0d8438-1d97-4ec1-aef9-a2fb86ed6acb')
    return IDWriteFontList
def _define_IDWriteFontList():
    IDWriteFontList = win32more.Graphics.DirectWrite.IDWriteFontList_head
    IDWriteFontList.GetFontCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontCollection_head), use_last_error=False)(3, 'GetFontCollection', ((1, 'fontCollection'),)))
    IDWriteFontList.GetFontCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(4, 'GetFontCount', ()))
    IDWriteFontList.GetFont = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteFont_head), use_last_error=False)(5, 'GetFont', ((1, 'index'),(1, 'font'),)))
    return IDWriteFontList
def _define_IDWriteFontFamily_head():
    class IDWriteFontFamily(win32more.Graphics.DirectWrite.IDWriteFontList_head):
        Guid = Guid('da20d8ef-812a-4c43-9802-62ec4abd7add')
    return IDWriteFontFamily
def _define_IDWriteFontFamily():
    IDWriteFontFamily = win32more.Graphics.DirectWrite.IDWriteFontFamily_head
    IDWriteFontFamily.GetFamilyNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteLocalizedStrings_head), use_last_error=False)(6, 'GetFamilyNames', ((1, 'names'),)))
    IDWriteFontFamily.GetFirstMatchingFont = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_FONT_WEIGHT,win32more.Graphics.DirectWrite.DWRITE_FONT_STRETCH,win32more.Graphics.DirectWrite.DWRITE_FONT_STYLE,POINTER(win32more.Graphics.DirectWrite.IDWriteFont_head), use_last_error=False)(7, 'GetFirstMatchingFont', ((1, 'weight'),(1, 'stretch'),(1, 'style'),(1, 'matchingFont'),)))
    IDWriteFontFamily.GetMatchingFonts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_FONT_WEIGHT,win32more.Graphics.DirectWrite.DWRITE_FONT_STRETCH,win32more.Graphics.DirectWrite.DWRITE_FONT_STYLE,POINTER(win32more.Graphics.DirectWrite.IDWriteFontList_head), use_last_error=False)(8, 'GetMatchingFonts', ((1, 'weight'),(1, 'stretch'),(1, 'style'),(1, 'matchingFonts'),)))
    return IDWriteFontFamily
def _define_IDWriteFont_head():
    class IDWriteFont(win32more.System.Com.IUnknown_head):
        Guid = Guid('acd16696-8c14-4f5d-877e-fe3fc1d32737')
    return IDWriteFont
def _define_IDWriteFont():
    IDWriteFont = win32more.Graphics.DirectWrite.IDWriteFont_head
    IDWriteFont.GetFontFamily = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFamily_head), use_last_error=False)(3, 'GetFontFamily', ((1, 'fontFamily'),)))
    IDWriteFont.GetWeight = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_FONT_WEIGHT, use_last_error=False)(4, 'GetWeight', ()))
    IDWriteFont.GetStretch = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_FONT_STRETCH, use_last_error=False)(5, 'GetStretch', ()))
    IDWriteFont.GetStyle = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_FONT_STYLE, use_last_error=False)(6, 'GetStyle', ()))
    IDWriteFont.IsSymbolFont = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(7, 'IsSymbolFont', ()))
    IDWriteFont.GetFaceNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteLocalizedStrings_head), use_last_error=False)(8, 'GetFaceNames', ((1, 'names'),)))
    IDWriteFont.GetInformationalStrings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_INFORMATIONAL_STRING_ID,POINTER(win32more.Graphics.DirectWrite.IDWriteLocalizedStrings_head),POINTER(win32more.Foundation.BOOL), use_last_error=False)(9, 'GetInformationalStrings', ((1, 'informationalStringID'),(1, 'informationalStrings'),(1, 'exists'),)))
    IDWriteFont.GetSimulations = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_FONT_SIMULATIONS, use_last_error=False)(10, 'GetSimulations', ()))
    IDWriteFont.GetMetrics = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_METRICS_head), use_last_error=False)(11, 'GetMetrics', ((1, 'fontMetrics'),)))
    IDWriteFont.HasCharacter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BOOL), use_last_error=False)(12, 'HasCharacter', ((1, 'unicodeValue'),(1, 'exists'),)))
    IDWriteFont.CreateFontFace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFace_head), use_last_error=False)(13, 'CreateFontFace', ((1, 'fontFace'),)))
    return IDWriteFont
DWRITE_READING_DIRECTION = Int32
DWRITE_READING_DIRECTION_LEFT_TO_RIGHT = 0
DWRITE_READING_DIRECTION_RIGHT_TO_LEFT = 1
DWRITE_READING_DIRECTION_TOP_TO_BOTTOM = 2
DWRITE_READING_DIRECTION_BOTTOM_TO_TOP = 3
DWRITE_FLOW_DIRECTION = Int32
DWRITE_FLOW_DIRECTION_TOP_TO_BOTTOM = 0
DWRITE_FLOW_DIRECTION_BOTTOM_TO_TOP = 1
DWRITE_FLOW_DIRECTION_LEFT_TO_RIGHT = 2
DWRITE_FLOW_DIRECTION_RIGHT_TO_LEFT = 3
DWRITE_TEXT_ALIGNMENT = Int32
DWRITE_TEXT_ALIGNMENT_LEADING = 0
DWRITE_TEXT_ALIGNMENT_TRAILING = 1
DWRITE_TEXT_ALIGNMENT_CENTER = 2
DWRITE_TEXT_ALIGNMENT_JUSTIFIED = 3
DWRITE_PARAGRAPH_ALIGNMENT = Int32
DWRITE_PARAGRAPH_ALIGNMENT_NEAR = 0
DWRITE_PARAGRAPH_ALIGNMENT_FAR = 1
DWRITE_PARAGRAPH_ALIGNMENT_CENTER = 2
DWRITE_WORD_WRAPPING = Int32
DWRITE_WORD_WRAPPING_WRAP = 0
DWRITE_WORD_WRAPPING_NO_WRAP = 1
DWRITE_WORD_WRAPPING_EMERGENCY_BREAK = 2
DWRITE_WORD_WRAPPING_WHOLE_WORD = 3
DWRITE_WORD_WRAPPING_CHARACTER = 4
DWRITE_LINE_SPACING_METHOD = Int32
DWRITE_LINE_SPACING_METHOD_DEFAULT = 0
DWRITE_LINE_SPACING_METHOD_UNIFORM = 1
DWRITE_LINE_SPACING_METHOD_PROPORTIONAL = 2
DWRITE_TRIMMING_GRANULARITY = Int32
DWRITE_TRIMMING_GRANULARITY_NONE = 0
DWRITE_TRIMMING_GRANULARITY_CHARACTER = 1
DWRITE_TRIMMING_GRANULARITY_WORD = 2
DWRITE_FONT_FEATURE_TAG = UInt32
DWRITE_FONT_FEATURE_TAG_ALTERNATIVE_FRACTIONS = 1668441697
DWRITE_FONT_FEATURE_TAG_PETITE_CAPITALS_FROM_CAPITALS = 1668297315
DWRITE_FONT_FEATURE_TAG_SMALL_CAPITALS_FROM_CAPITALS = 1668493923
DWRITE_FONT_FEATURE_TAG_CONTEXTUAL_ALTERNATES = 1953259875
DWRITE_FONT_FEATURE_TAG_CASE_SENSITIVE_FORMS = 1702060387
DWRITE_FONT_FEATURE_TAG_GLYPH_COMPOSITION_DECOMPOSITION = 1886217059
DWRITE_FONT_FEATURE_TAG_CONTEXTUAL_LIGATURES = 1734962275
DWRITE_FONT_FEATURE_TAG_CAPITAL_SPACING = 1886613603
DWRITE_FONT_FEATURE_TAG_CONTEXTUAL_SWASH = 1752658787
DWRITE_FONT_FEATURE_TAG_CURSIVE_POSITIONING = 1936880995
DWRITE_FONT_FEATURE_TAG_DEFAULT = 1953261156
DWRITE_FONT_FEATURE_TAG_DISCRETIONARY_LIGATURES = 1734962276
DWRITE_FONT_FEATURE_TAG_EXPERT_FORMS = 1953527909
DWRITE_FONT_FEATURE_TAG_FRACTIONS = 1667330662
DWRITE_FONT_FEATURE_TAG_FULL_WIDTH = 1684633446
DWRITE_FONT_FEATURE_TAG_HALF_FORMS = 1718378856
DWRITE_FONT_FEATURE_TAG_HALANT_FORMS = 1852596584
DWRITE_FONT_FEATURE_TAG_ALTERNATE_HALF_WIDTH = 1953259880
DWRITE_FONT_FEATURE_TAG_HISTORICAL_FORMS = 1953720680
DWRITE_FONT_FEATURE_TAG_HORIZONTAL_KANA_ALTERNATES = 1634626408
DWRITE_FONT_FEATURE_TAG_HISTORICAL_LIGATURES = 1734962280
DWRITE_FONT_FEATURE_TAG_HALF_WIDTH = 1684633448
DWRITE_FONT_FEATURE_TAG_HOJO_KANJI_FORMS = 1869246312
DWRITE_FONT_FEATURE_TAG_JIS04_FORMS = 875589738
DWRITE_FONT_FEATURE_TAG_JIS78_FORMS = 943157354
DWRITE_FONT_FEATURE_TAG_JIS83_FORMS = 859336810
DWRITE_FONT_FEATURE_TAG_JIS90_FORMS = 809070698
DWRITE_FONT_FEATURE_TAG_KERNING = 1852990827
DWRITE_FONT_FEATURE_TAG_STANDARD_LIGATURES = 1634167148
DWRITE_FONT_FEATURE_TAG_LINING_FIGURES = 1836412524
DWRITE_FONT_FEATURE_TAG_LOCALIZED_FORMS = 1818455916
DWRITE_FONT_FEATURE_TAG_MARK_POSITIONING = 1802658157
DWRITE_FONT_FEATURE_TAG_MATHEMATICAL_GREEK = 1802659693
DWRITE_FONT_FEATURE_TAG_MARK_TO_MARK_POSITIONING = 1802333037
DWRITE_FONT_FEATURE_TAG_ALTERNATE_ANNOTATION_FORMS = 1953259886
DWRITE_FONT_FEATURE_TAG_NLC_KANJI_FORMS = 1801677934
DWRITE_FONT_FEATURE_TAG_OLD_STYLE_FIGURES = 1836412527
DWRITE_FONT_FEATURE_TAG_ORDINALS = 1852076655
DWRITE_FONT_FEATURE_TAG_PROPORTIONAL_ALTERNATE_WIDTH = 1953259888
DWRITE_FONT_FEATURE_TAG_PETITE_CAPITALS = 1885430640
DWRITE_FONT_FEATURE_TAG_PROPORTIONAL_FIGURES = 1836412528
DWRITE_FONT_FEATURE_TAG_PROPORTIONAL_WIDTHS = 1684633456
DWRITE_FONT_FEATURE_TAG_QUARTER_WIDTHS = 1684633457
DWRITE_FONT_FEATURE_TAG_REQUIRED_LIGATURES = 1734962290
DWRITE_FONT_FEATURE_TAG_RUBY_NOTATION_FORMS = 2036495730
DWRITE_FONT_FEATURE_TAG_STYLISTIC_ALTERNATES = 1953259891
DWRITE_FONT_FEATURE_TAG_SCIENTIFIC_INFERIORS = 1718511987
DWRITE_FONT_FEATURE_TAG_SMALL_CAPITALS = 1885564275
DWRITE_FONT_FEATURE_TAG_SIMPLIFIED_FORMS = 1819307379
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_1 = 825258867
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_2 = 842036083
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_3 = 858813299
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_4 = 875590515
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_5 = 892367731
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_6 = 909144947
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_7 = 925922163
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_8 = 942699379
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_9 = 959476595
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_10 = 808547187
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_11 = 825324403
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_12 = 842101619
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_13 = 858878835
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_14 = 875656051
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_15 = 892433267
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_16 = 909210483
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_17 = 925987699
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_18 = 942764915
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_19 = 959542131
DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_20 = 808612723
DWRITE_FONT_FEATURE_TAG_SUBSCRIPT = 1935832435
DWRITE_FONT_FEATURE_TAG_SUPERSCRIPT = 1936749939
DWRITE_FONT_FEATURE_TAG_SWASH = 1752397683
DWRITE_FONT_FEATURE_TAG_TITLING = 1819568500
DWRITE_FONT_FEATURE_TAG_TRADITIONAL_NAME_FORMS = 1835101812
DWRITE_FONT_FEATURE_TAG_TABULAR_FIGURES = 1836412532
DWRITE_FONT_FEATURE_TAG_TRADITIONAL_FORMS = 1684107892
DWRITE_FONT_FEATURE_TAG_THIRD_WIDTHS = 1684633460
DWRITE_FONT_FEATURE_TAG_UNICASE = 1667853941
DWRITE_FONT_FEATURE_TAG_VERTICAL_WRITING = 1953654134
DWRITE_FONT_FEATURE_TAG_VERTICAL_ALTERNATES_AND_ROTATION = 846492278
DWRITE_FONT_FEATURE_TAG_SLASHED_ZERO = 1869768058
def _define_DWRITE_TEXT_RANGE_head():
    class DWRITE_TEXT_RANGE(Structure):
        pass
    return DWRITE_TEXT_RANGE
def _define_DWRITE_TEXT_RANGE():
    DWRITE_TEXT_RANGE = win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE_head
    DWRITE_TEXT_RANGE._fields_ = [
        ("startPosition", UInt32),
        ("length", UInt32),
    ]
    return DWRITE_TEXT_RANGE
def _define_DWRITE_FONT_FEATURE_head():
    class DWRITE_FONT_FEATURE(Structure):
        pass
    return DWRITE_FONT_FEATURE
def _define_DWRITE_FONT_FEATURE():
    DWRITE_FONT_FEATURE = win32more.Graphics.DirectWrite.DWRITE_FONT_FEATURE_head
    DWRITE_FONT_FEATURE._fields_ = [
        ("nameTag", win32more.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG),
        ("parameter", UInt32),
    ]
    return DWRITE_FONT_FEATURE
def _define_DWRITE_TYPOGRAPHIC_FEATURES_head():
    class DWRITE_TYPOGRAPHIC_FEATURES(Structure):
        pass
    return DWRITE_TYPOGRAPHIC_FEATURES
def _define_DWRITE_TYPOGRAPHIC_FEATURES():
    DWRITE_TYPOGRAPHIC_FEATURES = win32more.Graphics.DirectWrite.DWRITE_TYPOGRAPHIC_FEATURES_head
    DWRITE_TYPOGRAPHIC_FEATURES._fields_ = [
        ("features", POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_FEATURE_head)),
        ("featureCount", UInt32),
    ]
    return DWRITE_TYPOGRAPHIC_FEATURES
def _define_DWRITE_TRIMMING_head():
    class DWRITE_TRIMMING(Structure):
        pass
    return DWRITE_TRIMMING
def _define_DWRITE_TRIMMING():
    DWRITE_TRIMMING = win32more.Graphics.DirectWrite.DWRITE_TRIMMING_head
    DWRITE_TRIMMING._fields_ = [
        ("granularity", win32more.Graphics.DirectWrite.DWRITE_TRIMMING_GRANULARITY),
        ("delimiter", UInt32),
        ("delimiterCount", UInt32),
    ]
    return DWRITE_TRIMMING
def _define_IDWriteTextFormat_head():
    class IDWriteTextFormat(win32more.System.Com.IUnknown_head):
        Guid = Guid('9c906818-31d7-4fd3-a151-7c5e225db55a')
    return IDWriteTextFormat
def _define_IDWriteTextFormat():
    IDWriteTextFormat = win32more.Graphics.DirectWrite.IDWriteTextFormat_head
    IDWriteTextFormat.SetTextAlignment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_TEXT_ALIGNMENT, use_last_error=False)(3, 'SetTextAlignment', ((1, 'textAlignment'),)))
    IDWriteTextFormat.SetParagraphAlignment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_PARAGRAPH_ALIGNMENT, use_last_error=False)(4, 'SetParagraphAlignment', ((1, 'paragraphAlignment'),)))
    IDWriteTextFormat.SetWordWrapping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_WORD_WRAPPING, use_last_error=False)(5, 'SetWordWrapping', ((1, 'wordWrapping'),)))
    IDWriteTextFormat.SetReadingDirection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_READING_DIRECTION, use_last_error=False)(6, 'SetReadingDirection', ((1, 'readingDirection'),)))
    IDWriteTextFormat.SetFlowDirection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_FLOW_DIRECTION, use_last_error=False)(7, 'SetFlowDirection', ((1, 'flowDirection'),)))
    IDWriteTextFormat.SetIncrementalTabStop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(8, 'SetIncrementalTabStop', ((1, 'incrementalTabStop'),)))
    IDWriteTextFormat.SetTrimming = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_TRIMMING_head),win32more.Graphics.DirectWrite.IDWriteInlineObject_head, use_last_error=False)(9, 'SetTrimming', ((1, 'trimmingOptions'),(1, 'trimmingSign'),)))
    IDWriteTextFormat.SetLineSpacing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_LINE_SPACING_METHOD,Single,Single, use_last_error=False)(10, 'SetLineSpacing', ((1, 'lineSpacingMethod'),(1, 'lineSpacing'),(1, 'baseline'),)))
    IDWriteTextFormat.GetTextAlignment = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_TEXT_ALIGNMENT, use_last_error=False)(11, 'GetTextAlignment', ()))
    IDWriteTextFormat.GetParagraphAlignment = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_PARAGRAPH_ALIGNMENT, use_last_error=False)(12, 'GetParagraphAlignment', ()))
    IDWriteTextFormat.GetWordWrapping = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_WORD_WRAPPING, use_last_error=False)(13, 'GetWordWrapping', ()))
    IDWriteTextFormat.GetReadingDirection = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_READING_DIRECTION, use_last_error=False)(14, 'GetReadingDirection', ()))
    IDWriteTextFormat.GetFlowDirection = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_FLOW_DIRECTION, use_last_error=False)(15, 'GetFlowDirection', ()))
    IDWriteTextFormat.GetIncrementalTabStop = COMMETHOD(WINFUNCTYPE(Single, use_last_error=False)(16, 'GetIncrementalTabStop', ()))
    IDWriteTextFormat.GetTrimming = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_TRIMMING_head),POINTER(win32more.Graphics.DirectWrite.IDWriteInlineObject_head), use_last_error=False)(17, 'GetTrimming', ((1, 'trimmingOptions'),(1, 'trimmingSign'),)))
    IDWriteTextFormat.GetLineSpacing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_LINE_SPACING_METHOD),POINTER(Single),POINTER(Single), use_last_error=False)(18, 'GetLineSpacing', ((1, 'lineSpacingMethod'),(1, 'lineSpacing'),(1, 'baseline'),)))
    IDWriteTextFormat.GetFontCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontCollection_head), use_last_error=False)(19, 'GetFontCollection', ((1, 'fontCollection'),)))
    IDWriteTextFormat.GetFontFamilyNameLength = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(20, 'GetFontFamilyNameLength', ()))
    IDWriteTextFormat.GetFontFamilyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32, use_last_error=False)(21, 'GetFontFamilyName', ((1, 'fontFamilyName'),(1, 'nameSize'),)))
    IDWriteTextFormat.GetFontWeight = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_FONT_WEIGHT, use_last_error=False)(22, 'GetFontWeight', ()))
    IDWriteTextFormat.GetFontStyle = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_FONT_STYLE, use_last_error=False)(23, 'GetFontStyle', ()))
    IDWriteTextFormat.GetFontStretch = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_FONT_STRETCH, use_last_error=False)(24, 'GetFontStretch', ()))
    IDWriteTextFormat.GetFontSize = COMMETHOD(WINFUNCTYPE(Single, use_last_error=False)(25, 'GetFontSize', ()))
    IDWriteTextFormat.GetLocaleNameLength = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(26, 'GetLocaleNameLength', ()))
    IDWriteTextFormat.GetLocaleName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32, use_last_error=False)(27, 'GetLocaleName', ((1, 'localeName'),(1, 'nameSize'),)))
    return IDWriteTextFormat
def _define_IDWriteTypography_head():
    class IDWriteTypography(win32more.System.Com.IUnknown_head):
        Guid = Guid('55f1112b-1dc2-4b3c-9541-f46894ed85b6')
    return IDWriteTypography
def _define_IDWriteTypography():
    IDWriteTypography = win32more.Graphics.DirectWrite.IDWriteTypography_head
    IDWriteTypography.AddFontFeature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_FONT_FEATURE, use_last_error=False)(3, 'AddFontFeature', ((1, 'fontFeature'),)))
    IDWriteTypography.GetFontFeatureCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(4, 'GetFontFeatureCount', ()))
    IDWriteTypography.GetFontFeature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_FEATURE_head), use_last_error=False)(5, 'GetFontFeature', ((1, 'fontFeatureIndex'),(1, 'fontFeature'),)))
    return IDWriteTypography
DWRITE_SCRIPT_SHAPES = UInt32
DWRITE_SCRIPT_SHAPES_DEFAULT = 0
DWRITE_SCRIPT_SHAPES_NO_VISUAL = 1
def _define_DWRITE_SCRIPT_ANALYSIS_head():
    class DWRITE_SCRIPT_ANALYSIS(Structure):
        pass
    return DWRITE_SCRIPT_ANALYSIS
def _define_DWRITE_SCRIPT_ANALYSIS():
    DWRITE_SCRIPT_ANALYSIS = win32more.Graphics.DirectWrite.DWRITE_SCRIPT_ANALYSIS_head
    DWRITE_SCRIPT_ANALYSIS._fields_ = [
        ("script", UInt16),
        ("shapes", win32more.Graphics.DirectWrite.DWRITE_SCRIPT_SHAPES),
    ]
    return DWRITE_SCRIPT_ANALYSIS
DWRITE_BREAK_CONDITION = Int32
DWRITE_BREAK_CONDITION_NEUTRAL = 0
DWRITE_BREAK_CONDITION_CAN_BREAK = 1
DWRITE_BREAK_CONDITION_MAY_NOT_BREAK = 2
DWRITE_BREAK_CONDITION_MUST_BREAK = 3
def _define_DWRITE_LINE_BREAKPOINT_head():
    class DWRITE_LINE_BREAKPOINT(Structure):
        pass
    return DWRITE_LINE_BREAKPOINT
def _define_DWRITE_LINE_BREAKPOINT():
    DWRITE_LINE_BREAKPOINT = win32more.Graphics.DirectWrite.DWRITE_LINE_BREAKPOINT_head
    DWRITE_LINE_BREAKPOINT._fields_ = [
        ("_bitfield", Byte),
    ]
    return DWRITE_LINE_BREAKPOINT
DWRITE_NUMBER_SUBSTITUTION_METHOD = Int32
DWRITE_NUMBER_SUBSTITUTION_METHOD_FROM_CULTURE = 0
DWRITE_NUMBER_SUBSTITUTION_METHOD_CONTEXTUAL = 1
DWRITE_NUMBER_SUBSTITUTION_METHOD_NONE = 2
DWRITE_NUMBER_SUBSTITUTION_METHOD_NATIONAL = 3
DWRITE_NUMBER_SUBSTITUTION_METHOD_TRADITIONAL = 4
def _define_IDWriteNumberSubstitution_head():
    class IDWriteNumberSubstitution(win32more.System.Com.IUnknown_head):
        Guid = Guid('14885cc9-bab0-4f90-b6ed-5c366a2cd03d')
    return IDWriteNumberSubstitution
def _define_IDWriteNumberSubstitution():
    IDWriteNumberSubstitution = win32more.Graphics.DirectWrite.IDWriteNumberSubstitution_head
    return IDWriteNumberSubstitution
def _define_DWRITE_SHAPING_TEXT_PROPERTIES_head():
    class DWRITE_SHAPING_TEXT_PROPERTIES(Structure):
        pass
    return DWRITE_SHAPING_TEXT_PROPERTIES
def _define_DWRITE_SHAPING_TEXT_PROPERTIES():
    DWRITE_SHAPING_TEXT_PROPERTIES = win32more.Graphics.DirectWrite.DWRITE_SHAPING_TEXT_PROPERTIES_head
    DWRITE_SHAPING_TEXT_PROPERTIES._fields_ = [
        ("_bitfield", UInt16),
    ]
    return DWRITE_SHAPING_TEXT_PROPERTIES
def _define_DWRITE_SHAPING_GLYPH_PROPERTIES_head():
    class DWRITE_SHAPING_GLYPH_PROPERTIES(Structure):
        pass
    return DWRITE_SHAPING_GLYPH_PROPERTIES
def _define_DWRITE_SHAPING_GLYPH_PROPERTIES():
    DWRITE_SHAPING_GLYPH_PROPERTIES = win32more.Graphics.DirectWrite.DWRITE_SHAPING_GLYPH_PROPERTIES_head
    DWRITE_SHAPING_GLYPH_PROPERTIES._fields_ = [
        ("_bitfield", UInt16),
    ]
    return DWRITE_SHAPING_GLYPH_PROPERTIES
def _define_IDWriteTextAnalysisSource_head():
    class IDWriteTextAnalysisSource(win32more.System.Com.IUnknown_head):
        Guid = Guid('688e1a58-5094-47c8-adc8-fbcea60ae92b')
    return IDWriteTextAnalysisSource
def _define_IDWriteTextAnalysisSource():
    IDWriteTextAnalysisSource = win32more.Graphics.DirectWrite.IDWriteTextAnalysisSource_head
    IDWriteTextAnalysisSource.GetTextAtPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(UInt16)),POINTER(UInt32), use_last_error=False)(3, 'GetTextAtPosition', ((1, 'textPosition'),(1, 'textString'),(1, 'textLength'),)))
    IDWriteTextAnalysisSource.GetTextBeforePosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(UInt16)),POINTER(UInt32), use_last_error=False)(4, 'GetTextBeforePosition', ((1, 'textPosition'),(1, 'textString'),(1, 'textLength'),)))
    IDWriteTextAnalysisSource.GetParagraphReadingDirection = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_READING_DIRECTION, use_last_error=False)(5, 'GetParagraphReadingDirection', ()))
    IDWriteTextAnalysisSource.GetLocaleName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(POINTER(UInt16)), use_last_error=False)(6, 'GetLocaleName', ((1, 'textPosition'),(1, 'textLength'),(1, 'localeName'),)))
    IDWriteTextAnalysisSource.GetNumberSubstitution = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(win32more.Graphics.DirectWrite.IDWriteNumberSubstitution_head), use_last_error=False)(7, 'GetNumberSubstitution', ((1, 'textPosition'),(1, 'textLength'),(1, 'numberSubstitution'),)))
    return IDWriteTextAnalysisSource
def _define_IDWriteTextAnalysisSink_head():
    class IDWriteTextAnalysisSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('5810cd44-0ca0-4701-b3fa-bec5182ae4f6')
    return IDWriteTextAnalysisSink
def _define_IDWriteTextAnalysisSink():
    IDWriteTextAnalysisSink = win32more.Graphics.DirectWrite.IDWriteTextAnalysisSink_head
    IDWriteTextAnalysisSink.SetScriptAnalysis = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Graphics.DirectWrite.DWRITE_SCRIPT_ANALYSIS_head), use_last_error=False)(3, 'SetScriptAnalysis', ((1, 'textPosition'),(1, 'textLength'),(1, 'scriptAnalysis'),)))
    IDWriteTextAnalysisSink.SetLineBreakpoints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Graphics.DirectWrite.DWRITE_LINE_BREAKPOINT), use_last_error=False)(4, 'SetLineBreakpoints', ((1, 'textPosition'),(1, 'textLength'),(1, 'lineBreakpoints'),)))
    IDWriteTextAnalysisSink.SetBidiLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,Byte,Byte, use_last_error=False)(5, 'SetBidiLevel', ((1, 'textPosition'),(1, 'textLength'),(1, 'explicitLevel'),(1, 'resolvedLevel'),)))
    IDWriteTextAnalysisSink.SetNumberSubstitution = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Graphics.DirectWrite.IDWriteNumberSubstitution_head, use_last_error=False)(6, 'SetNumberSubstitution', ((1, 'textPosition'),(1, 'textLength'),(1, 'numberSubstitution'),)))
    return IDWriteTextAnalysisSink
def _define_IDWriteTextAnalyzer_head():
    class IDWriteTextAnalyzer(win32more.System.Com.IUnknown_head):
        Guid = Guid('b7e6163e-7f46-43b4-84b3-e4e6249c365d')
    return IDWriteTextAnalyzer
def _define_IDWriteTextAnalyzer():
    IDWriteTextAnalyzer = win32more.Graphics.DirectWrite.IDWriteTextAnalyzer_head
    IDWriteTextAnalyzer.AnalyzeScript = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteTextAnalysisSource_head,UInt32,UInt32,win32more.Graphics.DirectWrite.IDWriteTextAnalysisSink_head, use_last_error=False)(3, 'AnalyzeScript', ((1, 'analysisSource'),(1, 'textPosition'),(1, 'textLength'),(1, 'analysisSink'),)))
    IDWriteTextAnalyzer.AnalyzeBidi = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteTextAnalysisSource_head,UInt32,UInt32,win32more.Graphics.DirectWrite.IDWriteTextAnalysisSink_head, use_last_error=False)(4, 'AnalyzeBidi', ((1, 'analysisSource'),(1, 'textPosition'),(1, 'textLength'),(1, 'analysisSink'),)))
    IDWriteTextAnalyzer.AnalyzeNumberSubstitution = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteTextAnalysisSource_head,UInt32,UInt32,win32more.Graphics.DirectWrite.IDWriteTextAnalysisSink_head, use_last_error=False)(5, 'AnalyzeNumberSubstitution', ((1, 'analysisSource'),(1, 'textPosition'),(1, 'textLength'),(1, 'analysisSink'),)))
    IDWriteTextAnalyzer.AnalyzeLineBreakpoints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteTextAnalysisSource_head,UInt32,UInt32,win32more.Graphics.DirectWrite.IDWriteTextAnalysisSink_head, use_last_error=False)(6, 'AnalyzeLineBreakpoints', ((1, 'analysisSource'),(1, 'textPosition'),(1, 'textLength'),(1, 'analysisSink'),)))
    IDWriteTextAnalyzer.GetGlyphs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32,win32more.Graphics.DirectWrite.IDWriteFontFace_head,win32more.Foundation.BOOL,win32more.Foundation.BOOL,POINTER(win32more.Graphics.DirectWrite.DWRITE_SCRIPT_ANALYSIS_head),win32more.Foundation.PWSTR,win32more.Graphics.DirectWrite.IDWriteNumberSubstitution_head,POINTER(POINTER(win32more.Graphics.DirectWrite.DWRITE_TYPOGRAPHIC_FEATURES_head)),POINTER(UInt32),UInt32,UInt32,POINTER(UInt16),POINTER(win32more.Graphics.DirectWrite.DWRITE_SHAPING_TEXT_PROPERTIES),POINTER(UInt16),POINTER(win32more.Graphics.DirectWrite.DWRITE_SHAPING_GLYPH_PROPERTIES),POINTER(UInt32), use_last_error=False)(7, 'GetGlyphs', ((1, 'textString'),(1, 'textLength'),(1, 'fontFace'),(1, 'isSideways'),(1, 'isRightToLeft'),(1, 'scriptAnalysis'),(1, 'localeName'),(1, 'numberSubstitution'),(1, 'features'),(1, 'featureRangeLengths'),(1, 'featureRanges'),(1, 'maxGlyphCount'),(1, 'clusterMap'),(1, 'textProps'),(1, 'glyphIndices'),(1, 'glyphProps'),(1, 'actualGlyphCount'),)))
    IDWriteTextAnalyzer.GetGlyphPlacements = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),POINTER(UInt16),POINTER(win32more.Graphics.DirectWrite.DWRITE_SHAPING_TEXT_PROPERTIES),UInt32,POINTER(UInt16),POINTER(win32more.Graphics.DirectWrite.DWRITE_SHAPING_GLYPH_PROPERTIES),UInt32,win32more.Graphics.DirectWrite.IDWriteFontFace_head,Single,win32more.Foundation.BOOL,win32more.Foundation.BOOL,POINTER(win32more.Graphics.DirectWrite.DWRITE_SCRIPT_ANALYSIS_head),win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Graphics.DirectWrite.DWRITE_TYPOGRAPHIC_FEATURES_head)),POINTER(UInt32),UInt32,POINTER(Single),POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_OFFSET), use_last_error=False)(8, 'GetGlyphPlacements', ((1, 'textString'),(1, 'clusterMap'),(1, 'textProps'),(1, 'textLength'),(1, 'glyphIndices'),(1, 'glyphProps'),(1, 'glyphCount'),(1, 'fontFace'),(1, 'fontEmSize'),(1, 'isSideways'),(1, 'isRightToLeft'),(1, 'scriptAnalysis'),(1, 'localeName'),(1, 'features'),(1, 'featureRangeLengths'),(1, 'featureRanges'),(1, 'glyphAdvances'),(1, 'glyphOffsets'),)))
    IDWriteTextAnalyzer.GetGdiCompatibleGlyphPlacements = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),POINTER(UInt16),POINTER(win32more.Graphics.DirectWrite.DWRITE_SHAPING_TEXT_PROPERTIES),UInt32,POINTER(UInt16),POINTER(win32more.Graphics.DirectWrite.DWRITE_SHAPING_GLYPH_PROPERTIES),UInt32,win32more.Graphics.DirectWrite.IDWriteFontFace_head,Single,Single,POINTER(win32more.Graphics.DirectWrite.DWRITE_MATRIX_head),win32more.Foundation.BOOL,win32more.Foundation.BOOL,win32more.Foundation.BOOL,POINTER(win32more.Graphics.DirectWrite.DWRITE_SCRIPT_ANALYSIS_head),win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Graphics.DirectWrite.DWRITE_TYPOGRAPHIC_FEATURES_head)),POINTER(UInt32),UInt32,POINTER(Single),POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_OFFSET), use_last_error=False)(9, 'GetGdiCompatibleGlyphPlacements', ((1, 'textString'),(1, 'clusterMap'),(1, 'textProps'),(1, 'textLength'),(1, 'glyphIndices'),(1, 'glyphProps'),(1, 'glyphCount'),(1, 'fontFace'),(1, 'fontEmSize'),(1, 'pixelsPerDip'),(1, 'transform'),(1, 'useGdiNatural'),(1, 'isSideways'),(1, 'isRightToLeft'),(1, 'scriptAnalysis'),(1, 'localeName'),(1, 'features'),(1, 'featureRangeLengths'),(1, 'featureRanges'),(1, 'glyphAdvances'),(1, 'glyphOffsets'),)))
    return IDWriteTextAnalyzer
def _define_DWRITE_GLYPH_RUN_head():
    class DWRITE_GLYPH_RUN(Structure):
        pass
    return DWRITE_GLYPH_RUN
def _define_DWRITE_GLYPH_RUN():
    DWRITE_GLYPH_RUN = win32more.Graphics.DirectWrite.DWRITE_GLYPH_RUN_head
    DWRITE_GLYPH_RUN._fields_ = [
        ("fontFace", win32more.Graphics.DirectWrite.IDWriteFontFace_head),
        ("fontEmSize", Single),
        ("glyphCount", UInt32),
        ("glyphIndices", POINTER(UInt16)),
        ("glyphAdvances", POINTER(Single)),
        ("glyphOffsets", POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_OFFSET_head)),
        ("isSideways", win32more.Foundation.BOOL),
        ("bidiLevel", UInt32),
    ]
    return DWRITE_GLYPH_RUN
def _define_DWRITE_GLYPH_RUN_DESCRIPTION_head():
    class DWRITE_GLYPH_RUN_DESCRIPTION(Structure):
        pass
    return DWRITE_GLYPH_RUN_DESCRIPTION
def _define_DWRITE_GLYPH_RUN_DESCRIPTION():
    DWRITE_GLYPH_RUN_DESCRIPTION = win32more.Graphics.DirectWrite.DWRITE_GLYPH_RUN_DESCRIPTION_head
    DWRITE_GLYPH_RUN_DESCRIPTION._fields_ = [
        ("localeName", win32more.Foundation.PWSTR),
        ("string", win32more.Foundation.PWSTR),
        ("stringLength", UInt32),
        ("clusterMap", POINTER(UInt16)),
        ("textPosition", UInt32),
    ]
    return DWRITE_GLYPH_RUN_DESCRIPTION
def _define_DWRITE_UNDERLINE_head():
    class DWRITE_UNDERLINE(Structure):
        pass
    return DWRITE_UNDERLINE
def _define_DWRITE_UNDERLINE():
    DWRITE_UNDERLINE = win32more.Graphics.DirectWrite.DWRITE_UNDERLINE_head
    DWRITE_UNDERLINE._fields_ = [
        ("width", Single),
        ("thickness", Single),
        ("offset", Single),
        ("runHeight", Single),
        ("readingDirection", win32more.Graphics.DirectWrite.DWRITE_READING_DIRECTION),
        ("flowDirection", win32more.Graphics.DirectWrite.DWRITE_FLOW_DIRECTION),
        ("localeName", win32more.Foundation.PWSTR),
        ("measuringMode", win32more.Graphics.DirectWrite.DWRITE_MEASURING_MODE),
    ]
    return DWRITE_UNDERLINE
def _define_DWRITE_STRIKETHROUGH_head():
    class DWRITE_STRIKETHROUGH(Structure):
        pass
    return DWRITE_STRIKETHROUGH
def _define_DWRITE_STRIKETHROUGH():
    DWRITE_STRIKETHROUGH = win32more.Graphics.DirectWrite.DWRITE_STRIKETHROUGH_head
    DWRITE_STRIKETHROUGH._fields_ = [
        ("width", Single),
        ("thickness", Single),
        ("offset", Single),
        ("readingDirection", win32more.Graphics.DirectWrite.DWRITE_READING_DIRECTION),
        ("flowDirection", win32more.Graphics.DirectWrite.DWRITE_FLOW_DIRECTION),
        ("localeName", win32more.Foundation.PWSTR),
        ("measuringMode", win32more.Graphics.DirectWrite.DWRITE_MEASURING_MODE),
    ]
    return DWRITE_STRIKETHROUGH
def _define_DWRITE_LINE_METRICS_head():
    class DWRITE_LINE_METRICS(Structure):
        pass
    return DWRITE_LINE_METRICS
def _define_DWRITE_LINE_METRICS():
    DWRITE_LINE_METRICS = win32more.Graphics.DirectWrite.DWRITE_LINE_METRICS_head
    DWRITE_LINE_METRICS._fields_ = [
        ("length", UInt32),
        ("trailingWhitespaceLength", UInt32),
        ("newlineLength", UInt32),
        ("height", Single),
        ("baseline", Single),
        ("isTrimmed", win32more.Foundation.BOOL),
    ]
    return DWRITE_LINE_METRICS
def _define_DWRITE_CLUSTER_METRICS_head():
    class DWRITE_CLUSTER_METRICS(Structure):
        pass
    return DWRITE_CLUSTER_METRICS
def _define_DWRITE_CLUSTER_METRICS():
    DWRITE_CLUSTER_METRICS = win32more.Graphics.DirectWrite.DWRITE_CLUSTER_METRICS_head
    DWRITE_CLUSTER_METRICS._fields_ = [
        ("width", Single),
        ("length", UInt16),
        ("_bitfield", UInt16),
    ]
    return DWRITE_CLUSTER_METRICS
def _define_DWRITE_TEXT_METRICS_head():
    class DWRITE_TEXT_METRICS(Structure):
        pass
    return DWRITE_TEXT_METRICS
def _define_DWRITE_TEXT_METRICS():
    DWRITE_TEXT_METRICS = win32more.Graphics.DirectWrite.DWRITE_TEXT_METRICS_head
    DWRITE_TEXT_METRICS._fields_ = [
        ("left", Single),
        ("top", Single),
        ("width", Single),
        ("widthIncludingTrailingWhitespace", Single),
        ("height", Single),
        ("layoutWidth", Single),
        ("layoutHeight", Single),
        ("maxBidiReorderingDepth", UInt32),
        ("lineCount", UInt32),
    ]
    return DWRITE_TEXT_METRICS
def _define_DWRITE_INLINE_OBJECT_METRICS_head():
    class DWRITE_INLINE_OBJECT_METRICS(Structure):
        pass
    return DWRITE_INLINE_OBJECT_METRICS
def _define_DWRITE_INLINE_OBJECT_METRICS():
    DWRITE_INLINE_OBJECT_METRICS = win32more.Graphics.DirectWrite.DWRITE_INLINE_OBJECT_METRICS_head
    DWRITE_INLINE_OBJECT_METRICS._fields_ = [
        ("width", Single),
        ("height", Single),
        ("baseline", Single),
        ("supportsSideways", win32more.Foundation.BOOL),
    ]
    return DWRITE_INLINE_OBJECT_METRICS
def _define_DWRITE_OVERHANG_METRICS_head():
    class DWRITE_OVERHANG_METRICS(Structure):
        pass
    return DWRITE_OVERHANG_METRICS
def _define_DWRITE_OVERHANG_METRICS():
    DWRITE_OVERHANG_METRICS = win32more.Graphics.DirectWrite.DWRITE_OVERHANG_METRICS_head
    DWRITE_OVERHANG_METRICS._fields_ = [
        ("left", Single),
        ("top", Single),
        ("right", Single),
        ("bottom", Single),
    ]
    return DWRITE_OVERHANG_METRICS
def _define_DWRITE_HIT_TEST_METRICS_head():
    class DWRITE_HIT_TEST_METRICS(Structure):
        pass
    return DWRITE_HIT_TEST_METRICS
def _define_DWRITE_HIT_TEST_METRICS():
    DWRITE_HIT_TEST_METRICS = win32more.Graphics.DirectWrite.DWRITE_HIT_TEST_METRICS_head
    DWRITE_HIT_TEST_METRICS._fields_ = [
        ("textPosition", UInt32),
        ("length", UInt32),
        ("left", Single),
        ("top", Single),
        ("width", Single),
        ("height", Single),
        ("bidiLevel", UInt32),
        ("isText", win32more.Foundation.BOOL),
        ("isTrimmed", win32more.Foundation.BOOL),
    ]
    return DWRITE_HIT_TEST_METRICS
def _define_IDWriteInlineObject_head():
    class IDWriteInlineObject(win32more.System.Com.IUnknown_head):
        Guid = Guid('8339fde3-106f-47ab-8373-1c6295eb10b3')
    return IDWriteInlineObject
def _define_IDWriteInlineObject():
    IDWriteInlineObject = win32more.Graphics.DirectWrite.IDWriteInlineObject_head
    IDWriteInlineObject.Draw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Graphics.DirectWrite.IDWriteTextRenderer_head,Single,Single,win32more.Foundation.BOOL,win32more.Foundation.BOOL,win32more.System.Com.IUnknown_head, use_last_error=False)(3, 'Draw', ((1, 'clientDrawingContext'),(1, 'renderer'),(1, 'originX'),(1, 'originY'),(1, 'isSideways'),(1, 'isRightToLeft'),(1, 'clientDrawingEffect'),)))
    IDWriteInlineObject.GetMetrics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_INLINE_OBJECT_METRICS_head), use_last_error=False)(4, 'GetMetrics', ((1, 'metrics'),)))
    IDWriteInlineObject.GetOverhangMetrics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_OVERHANG_METRICS_head), use_last_error=False)(5, 'GetOverhangMetrics', ((1, 'overhangs'),)))
    IDWriteInlineObject.GetBreakConditions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_BREAK_CONDITION),POINTER(win32more.Graphics.DirectWrite.DWRITE_BREAK_CONDITION), use_last_error=False)(6, 'GetBreakConditions', ((1, 'breakConditionBefore'),(1, 'breakConditionAfter'),)))
    return IDWriteInlineObject
def _define_IDWritePixelSnapping_head():
    class IDWritePixelSnapping(win32more.System.Com.IUnknown_head):
        Guid = Guid('eaf3a2da-ecf4-4d24-b644-b34f6842024b')
    return IDWritePixelSnapping
def _define_IDWritePixelSnapping():
    IDWritePixelSnapping = win32more.Graphics.DirectWrite.IDWritePixelSnapping_head
    IDWritePixelSnapping.IsPixelSnappingDisabled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'IsPixelSnappingDisabled', ((1, 'clientDrawingContext'),(1, 'isDisabled'),)))
    IDWritePixelSnapping.GetCurrentTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Graphics.DirectWrite.DWRITE_MATRIX_head), use_last_error=False)(4, 'GetCurrentTransform', ((1, 'clientDrawingContext'),(1, 'transform'),)))
    IDWritePixelSnapping.GetPixelsPerDip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(Single), use_last_error=False)(5, 'GetPixelsPerDip', ((1, 'clientDrawingContext'),(1, 'pixelsPerDip'),)))
    return IDWritePixelSnapping
def _define_IDWriteTextRenderer_head():
    class IDWriteTextRenderer(win32more.Graphics.DirectWrite.IDWritePixelSnapping_head):
        Guid = Guid('ef8a8135-5cc6-45fe-8825-c5a0724eb819')
    return IDWriteTextRenderer
def _define_IDWriteTextRenderer():
    IDWriteTextRenderer = win32more.Graphics.DirectWrite.IDWriteTextRenderer_head
    IDWriteTextRenderer.DrawGlyphRun = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,Single,Single,win32more.Graphics.DirectWrite.DWRITE_MEASURING_MODE,POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_RUN_head),POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_RUN_DESCRIPTION_head),win32more.System.Com.IUnknown_head, use_last_error=False)(6, 'DrawGlyphRun', ((1, 'clientDrawingContext'),(1, 'baselineOriginX'),(1, 'baselineOriginY'),(1, 'measuringMode'),(1, 'glyphRun'),(1, 'glyphRunDescription'),(1, 'clientDrawingEffect'),)))
    IDWriteTextRenderer.DrawUnderline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,Single,Single,POINTER(win32more.Graphics.DirectWrite.DWRITE_UNDERLINE_head),win32more.System.Com.IUnknown_head, use_last_error=False)(7, 'DrawUnderline', ((1, 'clientDrawingContext'),(1, 'baselineOriginX'),(1, 'baselineOriginY'),(1, 'underline'),(1, 'clientDrawingEffect'),)))
    IDWriteTextRenderer.DrawStrikethrough = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,Single,Single,POINTER(win32more.Graphics.DirectWrite.DWRITE_STRIKETHROUGH_head),win32more.System.Com.IUnknown_head, use_last_error=False)(8, 'DrawStrikethrough', ((1, 'clientDrawingContext'),(1, 'baselineOriginX'),(1, 'baselineOriginY'),(1, 'strikethrough'),(1, 'clientDrawingEffect'),)))
    IDWriteTextRenderer.DrawInlineObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,Single,Single,win32more.Graphics.DirectWrite.IDWriteInlineObject_head,win32more.Foundation.BOOL,win32more.Foundation.BOOL,win32more.System.Com.IUnknown_head, use_last_error=False)(9, 'DrawInlineObject', ((1, 'clientDrawingContext'),(1, 'originX'),(1, 'originY'),(1, 'inlineObject'),(1, 'isSideways'),(1, 'isRightToLeft'),(1, 'clientDrawingEffect'),)))
    return IDWriteTextRenderer
def _define_IDWriteTextLayout_head():
    class IDWriteTextLayout(win32more.Graphics.DirectWrite.IDWriteTextFormat_head):
        Guid = Guid('53737037-6d14-410b-9bfe-0b182bb70961')
    return IDWriteTextLayout
def _define_IDWriteTextLayout():
    IDWriteTextLayout = win32more.Graphics.DirectWrite.IDWriteTextLayout_head
    IDWriteTextLayout.SetMaxWidth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(28, 'SetMaxWidth', ((1, 'maxWidth'),)))
    IDWriteTextLayout.SetMaxHeight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(29, 'SetMaxHeight', ((1, 'maxHeight'),)))
    IDWriteTextLayout.SetFontCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFontCollection_head,win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE, use_last_error=False)(30, 'SetFontCollection', ((1, 'fontCollection'),(1, 'textRange'),)))
    IDWriteTextLayout.SetFontFamilyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE, use_last_error=False)(31, 'SetFontFamilyName', ((1, 'fontFamilyName'),(1, 'textRange'),)))
    IDWriteTextLayout.SetFontWeight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_FONT_WEIGHT,win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE, use_last_error=False)(32, 'SetFontWeight', ((1, 'fontWeight'),(1, 'textRange'),)))
    IDWriteTextLayout.SetFontStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_FONT_STYLE,win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE, use_last_error=False)(33, 'SetFontStyle', ((1, 'fontStyle'),(1, 'textRange'),)))
    IDWriteTextLayout.SetFontStretch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_FONT_STRETCH,win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE, use_last_error=False)(34, 'SetFontStretch', ((1, 'fontStretch'),(1, 'textRange'),)))
    IDWriteTextLayout.SetFontSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE, use_last_error=False)(35, 'SetFontSize', ((1, 'fontSize'),(1, 'textRange'),)))
    IDWriteTextLayout.SetUnderline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE, use_last_error=False)(36, 'SetUnderline', ((1, 'hasUnderline'),(1, 'textRange'),)))
    IDWriteTextLayout.SetStrikethrough = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE, use_last_error=False)(37, 'SetStrikethrough', ((1, 'hasStrikethrough'),(1, 'textRange'),)))
    IDWriteTextLayout.SetDrawingEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE, use_last_error=False)(38, 'SetDrawingEffect', ((1, 'drawingEffect'),(1, 'textRange'),)))
    IDWriteTextLayout.SetInlineObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteInlineObject_head,win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE, use_last_error=False)(39, 'SetInlineObject', ((1, 'inlineObject'),(1, 'textRange'),)))
    IDWriteTextLayout.SetTypography = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteTypography_head,win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE, use_last_error=False)(40, 'SetTypography', ((1, 'typography'),(1, 'textRange'),)))
    IDWriteTextLayout.SetLocaleName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE, use_last_error=False)(41, 'SetLocaleName', ((1, 'localeName'),(1, 'textRange'),)))
    IDWriteTextLayout.GetMaxWidth = COMMETHOD(WINFUNCTYPE(Single, use_last_error=False)(42, 'GetMaxWidth', ()))
    IDWriteTextLayout.GetMaxHeight = COMMETHOD(WINFUNCTYPE(Single, use_last_error=False)(43, 'GetMaxHeight', ()))
    IDWriteTextLayout.GetFontCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteFontCollection_head),POINTER(win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE_head), use_last_error=False)(44, 'GetFontCollection', ((1, 'currentPosition'),(1, 'fontCollection'),(1, 'textRange'),)))
    IDWriteTextLayout.GetFontFamilyNameLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE_head), use_last_error=False)(45, 'GetFontFamilyNameLength', ((1, 'currentPosition'),(1, 'nameLength'),(1, 'textRange'),)))
    IDWriteTextLayout.GetFontFamilyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Char),UInt32,POINTER(win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE_head), use_last_error=False)(46, 'GetFontFamilyName', ((1, 'currentPosition'),(1, 'fontFamilyName'),(1, 'nameSize'),(1, 'textRange'),)))
    IDWriteTextLayout.GetFontWeight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_WEIGHT),POINTER(win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE_head), use_last_error=False)(47, 'GetFontWeight', ((1, 'currentPosition'),(1, 'fontWeight'),(1, 'textRange'),)))
    IDWriteTextLayout.GetFontStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_STYLE),POINTER(win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE_head), use_last_error=False)(48, 'GetFontStyle', ((1, 'currentPosition'),(1, 'fontStyle'),(1, 'textRange'),)))
    IDWriteTextLayout.GetFontStretch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_STRETCH),POINTER(win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE_head), use_last_error=False)(49, 'GetFontStretch', ((1, 'currentPosition'),(1, 'fontStretch'),(1, 'textRange'),)))
    IDWriteTextLayout.GetFontSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Single),POINTER(win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE_head), use_last_error=False)(50, 'GetFontSize', ((1, 'currentPosition'),(1, 'fontSize'),(1, 'textRange'),)))
    IDWriteTextLayout.GetUnderline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE_head), use_last_error=False)(51, 'GetUnderline', ((1, 'currentPosition'),(1, 'hasUnderline'),(1, 'textRange'),)))
    IDWriteTextLayout.GetStrikethrough = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE_head), use_last_error=False)(52, 'GetStrikethrough', ((1, 'currentPosition'),(1, 'hasStrikethrough'),(1, 'textRange'),)))
    IDWriteTextLayout.GetDrawingEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.IUnknown_head),POINTER(win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE_head), use_last_error=False)(53, 'GetDrawingEffect', ((1, 'currentPosition'),(1, 'drawingEffect'),(1, 'textRange'),)))
    IDWriteTextLayout.GetInlineObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteInlineObject_head),POINTER(win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE_head), use_last_error=False)(54, 'GetInlineObject', ((1, 'currentPosition'),(1, 'inlineObject'),(1, 'textRange'),)))
    IDWriteTextLayout.GetTypography = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteTypography_head),POINTER(win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE_head), use_last_error=False)(55, 'GetTypography', ((1, 'currentPosition'),(1, 'typography'),(1, 'textRange'),)))
    IDWriteTextLayout.GetLocaleNameLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE_head), use_last_error=False)(56, 'GetLocaleNameLength', ((1, 'currentPosition'),(1, 'nameLength'),(1, 'textRange'),)))
    IDWriteTextLayout.GetLocaleName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Char),UInt32,POINTER(win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE_head), use_last_error=False)(57, 'GetLocaleName', ((1, 'currentPosition'),(1, 'localeName'),(1, 'nameSize'),(1, 'textRange'),)))
    IDWriteTextLayout.Draw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Graphics.DirectWrite.IDWriteTextRenderer_head,Single,Single, use_last_error=False)(58, 'Draw', ((1, 'clientDrawingContext'),(1, 'renderer'),(1, 'originX'),(1, 'originY'),)))
    IDWriteTextLayout.GetLineMetrics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_LINE_METRICS),UInt32,POINTER(UInt32), use_last_error=False)(59, 'GetLineMetrics', ((1, 'lineMetrics'),(1, 'maxLineCount'),(1, 'actualLineCount'),)))
    IDWriteTextLayout.GetMetrics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_TEXT_METRICS_head), use_last_error=False)(60, 'GetMetrics', ((1, 'textMetrics'),)))
    IDWriteTextLayout.GetOverhangMetrics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_OVERHANG_METRICS_head), use_last_error=False)(61, 'GetOverhangMetrics', ((1, 'overhangs'),)))
    IDWriteTextLayout.GetClusterMetrics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_CLUSTER_METRICS),UInt32,POINTER(UInt32), use_last_error=False)(62, 'GetClusterMetrics', ((1, 'clusterMetrics'),(1, 'maxClusterCount'),(1, 'actualClusterCount'),)))
    IDWriteTextLayout.DetermineMinWidth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(63, 'DetermineMinWidth', ((1, 'minWidth'),)))
    IDWriteTextLayout.HitTestPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Foundation.BOOL),POINTER(win32more.Graphics.DirectWrite.DWRITE_HIT_TEST_METRICS_head), use_last_error=False)(64, 'HitTestPoint', ((1, 'pointX'),(1, 'pointY'),(1, 'isTrailingHit'),(1, 'isInside'),(1, 'hitTestMetrics'),)))
    IDWriteTextLayout.HitTestTextPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.BOOL,POINTER(Single),POINTER(Single),POINTER(win32more.Graphics.DirectWrite.DWRITE_HIT_TEST_METRICS_head), use_last_error=False)(65, 'HitTestTextPosition', ((1, 'textPosition'),(1, 'isTrailingHit'),(1, 'pointX'),(1, 'pointY'),(1, 'hitTestMetrics'),)))
    IDWriteTextLayout.HitTestTextRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,Single,Single,POINTER(win32more.Graphics.DirectWrite.DWRITE_HIT_TEST_METRICS),UInt32,POINTER(UInt32), use_last_error=False)(66, 'HitTestTextRange', ((1, 'textPosition'),(1, 'textLength'),(1, 'originX'),(1, 'originY'),(1, 'hitTestMetrics'),(1, 'maxHitTestMetricsCount'),(1, 'actualHitTestMetricsCount'),)))
    return IDWriteTextLayout
def _define_IDWriteBitmapRenderTarget_head():
    class IDWriteBitmapRenderTarget(win32more.System.Com.IUnknown_head):
        Guid = Guid('5e5a32a3-8dff-4773-9ff6-0696eab77267')
    return IDWriteBitmapRenderTarget
def _define_IDWriteBitmapRenderTarget():
    IDWriteBitmapRenderTarget = win32more.Graphics.DirectWrite.IDWriteBitmapRenderTarget_head
    IDWriteBitmapRenderTarget.DrawGlyphRun = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,win32more.Graphics.DirectWrite.DWRITE_MEASURING_MODE,POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_RUN_head),win32more.Graphics.DirectWrite.IDWriteRenderingParams_head,UInt32,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(3, 'DrawGlyphRun', ((1, 'baselineOriginX'),(1, 'baselineOriginY'),(1, 'measuringMode'),(1, 'glyphRun'),(1, 'renderingParams'),(1, 'textColor'),(1, 'blackBoxRect'),)))
    IDWriteBitmapRenderTarget.GetMemoryDC = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Gdi.HDC, use_last_error=False)(4, 'GetMemoryDC', ()))
    IDWriteBitmapRenderTarget.GetPixelsPerDip = COMMETHOD(WINFUNCTYPE(Single, use_last_error=False)(5, 'GetPixelsPerDip', ()))
    IDWriteBitmapRenderTarget.SetPixelsPerDip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(6, 'SetPixelsPerDip', ((1, 'pixelsPerDip'),)))
    IDWriteBitmapRenderTarget.GetCurrentTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_MATRIX_head), use_last_error=False)(7, 'GetCurrentTransform', ((1, 'transform'),)))
    IDWriteBitmapRenderTarget.SetCurrentTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_MATRIX_head), use_last_error=False)(8, 'SetCurrentTransform', ((1, 'transform'),)))
    IDWriteBitmapRenderTarget.GetSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.SIZE_head), use_last_error=False)(9, 'GetSize', ((1, 'size'),)))
    IDWriteBitmapRenderTarget.Resize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(10, 'Resize', ((1, 'width'),(1, 'height'),)))
    return IDWriteBitmapRenderTarget
def _define_IDWriteGdiInterop_head():
    class IDWriteGdiInterop(win32more.System.Com.IUnknown_head):
        Guid = Guid('1edd9491-9853-4299-898f-6432983b6f3a')
    return IDWriteGdiInterop
def _define_IDWriteGdiInterop():
    IDWriteGdiInterop = win32more.Graphics.DirectWrite.IDWriteGdiInterop_head
    IDWriteGdiInterop.CreateFontFromLOGFONT = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Gdi.LOGFONTW_head),POINTER(win32more.Graphics.DirectWrite.IDWriteFont_head), use_last_error=False)(3, 'CreateFontFromLOGFONT', ((1, 'logFont'),(1, 'font'),)))
    IDWriteGdiInterop.ConvertFontToLOGFONT = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFont_head,POINTER(win32more.Graphics.Gdi.LOGFONTW_head),POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'ConvertFontToLOGFONT', ((1, 'font'),(1, 'logFont'),(1, 'isSystemFont'),)))
    IDWriteGdiInterop.ConvertFontFaceToLOGFONT = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFontFace_head,POINTER(win32more.Graphics.Gdi.LOGFONTW_head), use_last_error=False)(5, 'ConvertFontFaceToLOGFONT', ((1, 'font'),(1, 'logFont'),)))
    IDWriteGdiInterop.CreateFontFaceFromHdc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Gdi.HDC,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFace_head), use_last_error=False)(6, 'CreateFontFaceFromHdc', ((1, 'hdc'),(1, 'fontFace'),)))
    IDWriteGdiInterop.CreateBitmapRenderTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Gdi.HDC,UInt32,UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteBitmapRenderTarget_head), use_last_error=False)(7, 'CreateBitmapRenderTarget', ((1, 'hdc'),(1, 'width'),(1, 'height'),(1, 'renderTarget'),)))
    return IDWriteGdiInterop
DWRITE_TEXTURE_TYPE = Int32
DWRITE_TEXTURE_ALIASED_1x1 = 0
DWRITE_TEXTURE_CLEARTYPE_3x1 = 1
def _define_IDWriteGlyphRunAnalysis_head():
    class IDWriteGlyphRunAnalysis(win32more.System.Com.IUnknown_head):
        Guid = Guid('7d97dbf7-e085-42d4-81e3-6a883bded118')
    return IDWriteGlyphRunAnalysis
def _define_IDWriteGlyphRunAnalysis():
    IDWriteGlyphRunAnalysis = win32more.Graphics.DirectWrite.IDWriteGlyphRunAnalysis_head
    IDWriteGlyphRunAnalysis.GetAlphaTextureBounds = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_TEXTURE_TYPE,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(3, 'GetAlphaTextureBounds', ((1, 'textureType'),(1, 'textureBounds'),)))
    IDWriteGlyphRunAnalysis.CreateAlphaTexture = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_TEXTURE_TYPE,POINTER(win32more.Foundation.RECT_head),c_char_p_no,UInt32, use_last_error=False)(4, 'CreateAlphaTexture', ((1, 'textureType'),(1, 'textureBounds'),(1, 'alphaValues'),(1, 'bufferSize'),)))
    IDWriteGlyphRunAnalysis.GetAlphaBlendParams = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteRenderingParams_head,POINTER(Single),POINTER(Single),POINTER(Single), use_last_error=False)(5, 'GetAlphaBlendParams', ((1, 'renderingParams'),(1, 'blendGamma'),(1, 'blendEnhancedContrast'),(1, 'blendClearTypeLevel'),)))
    return IDWriteGlyphRunAnalysis
def _define_IDWriteFactory_head():
    class IDWriteFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('b859ee5a-d838-4b5b-a2e8-1adc7d93db48')
    return IDWriteFactory
def _define_IDWriteFactory():
    IDWriteFactory = win32more.Graphics.DirectWrite.IDWriteFactory_head
    IDWriteFactory.GetSystemFontCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontCollection_head),win32more.Foundation.BOOL, use_last_error=False)(3, 'GetSystemFontCollection', ((1, 'fontCollection'),(1, 'checkForUpdates'),)))
    IDWriteFactory.CreateCustomFontCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFontCollectionLoader_head,c_void_p,UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteFontCollection_head), use_last_error=False)(4, 'CreateCustomFontCollection', ((1, 'collectionLoader'),(1, 'collectionKey'),(1, 'collectionKeySize'),(1, 'fontCollection'),)))
    IDWriteFactory.RegisterFontCollectionLoader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFontCollectionLoader_head, use_last_error=False)(5, 'RegisterFontCollectionLoader', ((1, 'fontCollectionLoader'),)))
    IDWriteFactory.UnregisterFontCollectionLoader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFontCollectionLoader_head, use_last_error=False)(6, 'UnregisterFontCollectionLoader', ((1, 'fontCollectionLoader'),)))
    IDWriteFactory.CreateFontFileReference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Graphics.DirectWrite.IDWriteFontFile_head), use_last_error=False)(7, 'CreateFontFileReference', ((1, 'filePath'),(1, 'lastWriteTime'),(1, 'fontFile'),)))
    IDWriteFactory.CreateCustomFontFileReference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,win32more.Graphics.DirectWrite.IDWriteFontFileLoader_head,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFile_head), use_last_error=False)(8, 'CreateCustomFontFileReference', ((1, 'fontFileReferenceKey'),(1, 'fontFileReferenceKeySize'),(1, 'fontFileLoader'),(1, 'fontFile'),)))
    IDWriteFactory.CreateFontFace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_FONT_FACE_TYPE,UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFile_head),UInt32,win32more.Graphics.DirectWrite.DWRITE_FONT_SIMULATIONS,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFace_head), use_last_error=False)(9, 'CreateFontFace', ((1, 'fontFaceType'),(1, 'numberOfFiles'),(1, 'fontFiles'),(1, 'faceIndex'),(1, 'fontFaceSimulationFlags'),(1, 'fontFace'),)))
    IDWriteFactory.CreateRenderingParams = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteRenderingParams_head), use_last_error=False)(10, 'CreateRenderingParams', ((1, 'renderingParams'),)))
    IDWriteFactory.CreateMonitorRenderingParams = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Gdi.HMONITOR,POINTER(win32more.Graphics.DirectWrite.IDWriteRenderingParams_head), use_last_error=False)(11, 'CreateMonitorRenderingParams', ((1, 'monitor'),(1, 'renderingParams'),)))
    IDWriteFactory.CreateCustomRenderingParams = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,Single,win32more.Graphics.DirectWrite.DWRITE_PIXEL_GEOMETRY,win32more.Graphics.DirectWrite.DWRITE_RENDERING_MODE,POINTER(win32more.Graphics.DirectWrite.IDWriteRenderingParams_head), use_last_error=False)(12, 'CreateCustomRenderingParams', ((1, 'gamma'),(1, 'enhancedContrast'),(1, 'clearTypeLevel'),(1, 'pixelGeometry'),(1, 'renderingMode'),(1, 'renderingParams'),)))
    IDWriteFactory.RegisterFontFileLoader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFontFileLoader_head, use_last_error=False)(13, 'RegisterFontFileLoader', ((1, 'fontFileLoader'),)))
    IDWriteFactory.UnregisterFontFileLoader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFontFileLoader_head, use_last_error=False)(14, 'UnregisterFontFileLoader', ((1, 'fontFileLoader'),)))
    IDWriteFactory.CreateTextFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Graphics.DirectWrite.IDWriteFontCollection_head,win32more.Graphics.DirectWrite.DWRITE_FONT_WEIGHT,win32more.Graphics.DirectWrite.DWRITE_FONT_STYLE,win32more.Graphics.DirectWrite.DWRITE_FONT_STRETCH,Single,win32more.Foundation.PWSTR,POINTER(win32more.Graphics.DirectWrite.IDWriteTextFormat_head), use_last_error=False)(15, 'CreateTextFormat', ((1, 'fontFamilyName'),(1, 'fontCollection'),(1, 'fontWeight'),(1, 'fontStyle'),(1, 'fontStretch'),(1, 'fontSize'),(1, 'localeName'),(1, 'textFormat'),)))
    IDWriteFactory.CreateTypography = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteTypography_head), use_last_error=False)(16, 'CreateTypography', ((1, 'typography'),)))
    IDWriteFactory.GetGdiInterop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteGdiInterop_head), use_last_error=False)(17, 'GetGdiInterop', ((1, 'gdiInterop'),)))
    IDWriteFactory.CreateTextLayout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32,win32more.Graphics.DirectWrite.IDWriteTextFormat_head,Single,Single,POINTER(win32more.Graphics.DirectWrite.IDWriteTextLayout_head), use_last_error=False)(18, 'CreateTextLayout', ((1, 'string'),(1, 'stringLength'),(1, 'textFormat'),(1, 'maxWidth'),(1, 'maxHeight'),(1, 'textLayout'),)))
    IDWriteFactory.CreateGdiCompatibleTextLayout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32,win32more.Graphics.DirectWrite.IDWriteTextFormat_head,Single,Single,Single,POINTER(win32more.Graphics.DirectWrite.DWRITE_MATRIX_head),win32more.Foundation.BOOL,POINTER(win32more.Graphics.DirectWrite.IDWriteTextLayout_head), use_last_error=False)(19, 'CreateGdiCompatibleTextLayout', ((1, 'string'),(1, 'stringLength'),(1, 'textFormat'),(1, 'layoutWidth'),(1, 'layoutHeight'),(1, 'pixelsPerDip'),(1, 'transform'),(1, 'useGdiNatural'),(1, 'textLayout'),)))
    IDWriteFactory.CreateEllipsisTrimmingSign = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteTextFormat_head,POINTER(win32more.Graphics.DirectWrite.IDWriteInlineObject_head), use_last_error=False)(20, 'CreateEllipsisTrimmingSign', ((1, 'textFormat'),(1, 'trimmingSign'),)))
    IDWriteFactory.CreateTextAnalyzer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteTextAnalyzer_head), use_last_error=False)(21, 'CreateTextAnalyzer', ((1, 'textAnalyzer'),)))
    IDWriteFactory.CreateNumberSubstitution = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_NUMBER_SUBSTITUTION_METHOD,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,POINTER(win32more.Graphics.DirectWrite.IDWriteNumberSubstitution_head), use_last_error=False)(22, 'CreateNumberSubstitution', ((1, 'substitutionMethod'),(1, 'localeName'),(1, 'ignoreUserOverride'),(1, 'numberSubstitution'),)))
    IDWriteFactory.CreateGlyphRunAnalysis = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_RUN_head),Single,POINTER(win32more.Graphics.DirectWrite.DWRITE_MATRIX_head),win32more.Graphics.DirectWrite.DWRITE_RENDERING_MODE,win32more.Graphics.DirectWrite.DWRITE_MEASURING_MODE,Single,Single,POINTER(win32more.Graphics.DirectWrite.IDWriteGlyphRunAnalysis_head), use_last_error=False)(23, 'CreateGlyphRunAnalysis', ((1, 'glyphRun'),(1, 'pixelsPerDip'),(1, 'transform'),(1, 'renderingMode'),(1, 'measuringMode'),(1, 'baselineOriginX'),(1, 'baselineOriginY'),(1, 'glyphRunAnalysis'),)))
    return IDWriteFactory
DWRITE_PANOSE_FAMILY = Int32
DWRITE_PANOSE_FAMILY_ANY = 0
DWRITE_PANOSE_FAMILY_NO_FIT = 1
DWRITE_PANOSE_FAMILY_TEXT_DISPLAY = 2
DWRITE_PANOSE_FAMILY_SCRIPT = 3
DWRITE_PANOSE_FAMILY_DECORATIVE = 4
DWRITE_PANOSE_FAMILY_SYMBOL = 5
DWRITE_PANOSE_FAMILY_PICTORIAL = 5
DWRITE_PANOSE_SERIF_STYLE = Int32
DWRITE_PANOSE_SERIF_STYLE_ANY = 0
DWRITE_PANOSE_SERIF_STYLE_NO_FIT = 1
DWRITE_PANOSE_SERIF_STYLE_COVE = 2
DWRITE_PANOSE_SERIF_STYLE_OBTUSE_COVE = 3
DWRITE_PANOSE_SERIF_STYLE_SQUARE_COVE = 4
DWRITE_PANOSE_SERIF_STYLE_OBTUSE_SQUARE_COVE = 5
DWRITE_PANOSE_SERIF_STYLE_SQUARE = 6
DWRITE_PANOSE_SERIF_STYLE_THIN = 7
DWRITE_PANOSE_SERIF_STYLE_OVAL = 8
DWRITE_PANOSE_SERIF_STYLE_EXAGGERATED = 9
DWRITE_PANOSE_SERIF_STYLE_TRIANGLE = 10
DWRITE_PANOSE_SERIF_STYLE_NORMAL_SANS = 11
DWRITE_PANOSE_SERIF_STYLE_OBTUSE_SANS = 12
DWRITE_PANOSE_SERIF_STYLE_PERPENDICULAR_SANS = 13
DWRITE_PANOSE_SERIF_STYLE_FLARED = 14
DWRITE_PANOSE_SERIF_STYLE_ROUNDED = 15
DWRITE_PANOSE_SERIF_STYLE_SCRIPT = 16
DWRITE_PANOSE_SERIF_STYLE_PERP_SANS = 13
DWRITE_PANOSE_SERIF_STYLE_BONE = 8
DWRITE_PANOSE_WEIGHT = Int32
DWRITE_PANOSE_WEIGHT_ANY = 0
DWRITE_PANOSE_WEIGHT_NO_FIT = 1
DWRITE_PANOSE_WEIGHT_VERY_LIGHT = 2
DWRITE_PANOSE_WEIGHT_LIGHT = 3
DWRITE_PANOSE_WEIGHT_THIN = 4
DWRITE_PANOSE_WEIGHT_BOOK = 5
DWRITE_PANOSE_WEIGHT_MEDIUM = 6
DWRITE_PANOSE_WEIGHT_DEMI = 7
DWRITE_PANOSE_WEIGHT_BOLD = 8
DWRITE_PANOSE_WEIGHT_HEAVY = 9
DWRITE_PANOSE_WEIGHT_BLACK = 10
DWRITE_PANOSE_WEIGHT_EXTRA_BLACK = 11
DWRITE_PANOSE_WEIGHT_NORD = 11
DWRITE_PANOSE_PROPORTION = Int32
DWRITE_PANOSE_PROPORTION_ANY = 0
DWRITE_PANOSE_PROPORTION_NO_FIT = 1
DWRITE_PANOSE_PROPORTION_OLD_STYLE = 2
DWRITE_PANOSE_PROPORTION_MODERN = 3
DWRITE_PANOSE_PROPORTION_EVEN_WIDTH = 4
DWRITE_PANOSE_PROPORTION_EXPANDED = 5
DWRITE_PANOSE_PROPORTION_CONDENSED = 6
DWRITE_PANOSE_PROPORTION_VERY_EXPANDED = 7
DWRITE_PANOSE_PROPORTION_VERY_CONDENSED = 8
DWRITE_PANOSE_PROPORTION_MONOSPACED = 9
DWRITE_PANOSE_CONTRAST = Int32
DWRITE_PANOSE_CONTRAST_ANY = 0
DWRITE_PANOSE_CONTRAST_NO_FIT = 1
DWRITE_PANOSE_CONTRAST_NONE = 2
DWRITE_PANOSE_CONTRAST_VERY_LOW = 3
DWRITE_PANOSE_CONTRAST_LOW = 4
DWRITE_PANOSE_CONTRAST_MEDIUM_LOW = 5
DWRITE_PANOSE_CONTRAST_MEDIUM = 6
DWRITE_PANOSE_CONTRAST_MEDIUM_HIGH = 7
DWRITE_PANOSE_CONTRAST_HIGH = 8
DWRITE_PANOSE_CONTRAST_VERY_HIGH = 9
DWRITE_PANOSE_CONTRAST_HORIZONTAL_LOW = 10
DWRITE_PANOSE_CONTRAST_HORIZONTAL_MEDIUM = 11
DWRITE_PANOSE_CONTRAST_HORIZONTAL_HIGH = 12
DWRITE_PANOSE_CONTRAST_BROKEN = 13
DWRITE_PANOSE_STROKE_VARIATION = Int32
DWRITE_PANOSE_STROKE_VARIATION_ANY = 0
DWRITE_PANOSE_STROKE_VARIATION_NO_FIT = 1
DWRITE_PANOSE_STROKE_VARIATION_NO_VARIATION = 2
DWRITE_PANOSE_STROKE_VARIATION_GRADUAL_DIAGONAL = 3
DWRITE_PANOSE_STROKE_VARIATION_GRADUAL_TRANSITIONAL = 4
DWRITE_PANOSE_STROKE_VARIATION_GRADUAL_VERTICAL = 5
DWRITE_PANOSE_STROKE_VARIATION_GRADUAL_HORIZONTAL = 6
DWRITE_PANOSE_STROKE_VARIATION_RAPID_VERTICAL = 7
DWRITE_PANOSE_STROKE_VARIATION_RAPID_HORIZONTAL = 8
DWRITE_PANOSE_STROKE_VARIATION_INSTANT_VERTICAL = 9
DWRITE_PANOSE_STROKE_VARIATION_INSTANT_HORIZONTAL = 10
DWRITE_PANOSE_ARM_STYLE = Int32
DWRITE_PANOSE_ARM_STYLE_ANY = 0
DWRITE_PANOSE_ARM_STYLE_NO_FIT = 1
DWRITE_PANOSE_ARM_STYLE_STRAIGHT_ARMS_HORIZONTAL = 2
DWRITE_PANOSE_ARM_STYLE_STRAIGHT_ARMS_WEDGE = 3
DWRITE_PANOSE_ARM_STYLE_STRAIGHT_ARMS_VERTICAL = 4
DWRITE_PANOSE_ARM_STYLE_STRAIGHT_ARMS_SINGLE_SERIF = 5
DWRITE_PANOSE_ARM_STYLE_STRAIGHT_ARMS_DOUBLE_SERIF = 6
DWRITE_PANOSE_ARM_STYLE_NONSTRAIGHT_ARMS_HORIZONTAL = 7
DWRITE_PANOSE_ARM_STYLE_NONSTRAIGHT_ARMS_WEDGE = 8
DWRITE_PANOSE_ARM_STYLE_NONSTRAIGHT_ARMS_VERTICAL = 9
DWRITE_PANOSE_ARM_STYLE_NONSTRAIGHT_ARMS_SINGLE_SERIF = 10
DWRITE_PANOSE_ARM_STYLE_NONSTRAIGHT_ARMS_DOUBLE_SERIF = 11
DWRITE_PANOSE_ARM_STYLE_STRAIGHT_ARMS_HORZ = 2
DWRITE_PANOSE_ARM_STYLE_STRAIGHT_ARMS_VERT = 4
DWRITE_PANOSE_ARM_STYLE_BENT_ARMS_HORZ = 7
DWRITE_PANOSE_ARM_STYLE_BENT_ARMS_WEDGE = 8
DWRITE_PANOSE_ARM_STYLE_BENT_ARMS_VERT = 9
DWRITE_PANOSE_ARM_STYLE_BENT_ARMS_SINGLE_SERIF = 10
DWRITE_PANOSE_ARM_STYLE_BENT_ARMS_DOUBLE_SERIF = 11
DWRITE_PANOSE_LETTERFORM = Int32
DWRITE_PANOSE_LETTERFORM_ANY = 0
DWRITE_PANOSE_LETTERFORM_NO_FIT = 1
DWRITE_PANOSE_LETTERFORM_NORMAL_CONTACT = 2
DWRITE_PANOSE_LETTERFORM_NORMAL_WEIGHTED = 3
DWRITE_PANOSE_LETTERFORM_NORMAL_BOXED = 4
DWRITE_PANOSE_LETTERFORM_NORMAL_FLATTENED = 5
DWRITE_PANOSE_LETTERFORM_NORMAL_ROUNDED = 6
DWRITE_PANOSE_LETTERFORM_NORMAL_OFF_CENTER = 7
DWRITE_PANOSE_LETTERFORM_NORMAL_SQUARE = 8
DWRITE_PANOSE_LETTERFORM_OBLIQUE_CONTACT = 9
DWRITE_PANOSE_LETTERFORM_OBLIQUE_WEIGHTED = 10
DWRITE_PANOSE_LETTERFORM_OBLIQUE_BOXED = 11
DWRITE_PANOSE_LETTERFORM_OBLIQUE_FLATTENED = 12
DWRITE_PANOSE_LETTERFORM_OBLIQUE_ROUNDED = 13
DWRITE_PANOSE_LETTERFORM_OBLIQUE_OFF_CENTER = 14
DWRITE_PANOSE_LETTERFORM_OBLIQUE_SQUARE = 15
DWRITE_PANOSE_MIDLINE = Int32
DWRITE_PANOSE_MIDLINE_ANY = 0
DWRITE_PANOSE_MIDLINE_NO_FIT = 1
DWRITE_PANOSE_MIDLINE_STANDARD_TRIMMED = 2
DWRITE_PANOSE_MIDLINE_STANDARD_POINTED = 3
DWRITE_PANOSE_MIDLINE_STANDARD_SERIFED = 4
DWRITE_PANOSE_MIDLINE_HIGH_TRIMMED = 5
DWRITE_PANOSE_MIDLINE_HIGH_POINTED = 6
DWRITE_PANOSE_MIDLINE_HIGH_SERIFED = 7
DWRITE_PANOSE_MIDLINE_CONSTANT_TRIMMED = 8
DWRITE_PANOSE_MIDLINE_CONSTANT_POINTED = 9
DWRITE_PANOSE_MIDLINE_CONSTANT_SERIFED = 10
DWRITE_PANOSE_MIDLINE_LOW_TRIMMED = 11
DWRITE_PANOSE_MIDLINE_LOW_POINTED = 12
DWRITE_PANOSE_MIDLINE_LOW_SERIFED = 13
DWRITE_PANOSE_XHEIGHT = Int32
DWRITE_PANOSE_XHEIGHT_ANY = 0
DWRITE_PANOSE_XHEIGHT_NO_FIT = 1
DWRITE_PANOSE_XHEIGHT_CONSTANT_SMALL = 2
DWRITE_PANOSE_XHEIGHT_CONSTANT_STANDARD = 3
DWRITE_PANOSE_XHEIGHT_CONSTANT_LARGE = 4
DWRITE_PANOSE_XHEIGHT_DUCKING_SMALL = 5
DWRITE_PANOSE_XHEIGHT_DUCKING_STANDARD = 6
DWRITE_PANOSE_XHEIGHT_DUCKING_LARGE = 7
DWRITE_PANOSE_XHEIGHT_CONSTANT_STD = 3
DWRITE_PANOSE_XHEIGHT_DUCKING_STD = 6
DWRITE_PANOSE_TOOL_KIND = Int32
DWRITE_PANOSE_TOOL_KIND_ANY = 0
DWRITE_PANOSE_TOOL_KIND_NO_FIT = 1
DWRITE_PANOSE_TOOL_KIND_FLAT_NIB = 2
DWRITE_PANOSE_TOOL_KIND_PRESSURE_POINT = 3
DWRITE_PANOSE_TOOL_KIND_ENGRAVED = 4
DWRITE_PANOSE_TOOL_KIND_BALL = 5
DWRITE_PANOSE_TOOL_KIND_BRUSH = 6
DWRITE_PANOSE_TOOL_KIND_ROUGH = 7
DWRITE_PANOSE_TOOL_KIND_FELT_PEN_BRUSH_TIP = 8
DWRITE_PANOSE_TOOL_KIND_WILD_BRUSH = 9
DWRITE_PANOSE_SPACING = Int32
DWRITE_PANOSE_SPACING_ANY = 0
DWRITE_PANOSE_SPACING_NO_FIT = 1
DWRITE_PANOSE_SPACING_PROPORTIONAL_SPACED = 2
DWRITE_PANOSE_SPACING_MONOSPACED = 3
DWRITE_PANOSE_ASPECT_RATIO = Int32
DWRITE_PANOSE_ASPECT_RATIO_ANY = 0
DWRITE_PANOSE_ASPECT_RATIO_NO_FIT = 1
DWRITE_PANOSE_ASPECT_RATIO_VERY_CONDENSED = 2
DWRITE_PANOSE_ASPECT_RATIO_CONDENSED = 3
DWRITE_PANOSE_ASPECT_RATIO_NORMAL = 4
DWRITE_PANOSE_ASPECT_RATIO_EXPANDED = 5
DWRITE_PANOSE_ASPECT_RATIO_VERY_EXPANDED = 6
DWRITE_PANOSE_SCRIPT_TOPOLOGY = Int32
DWRITE_PANOSE_SCRIPT_TOPOLOGY_ANY = 0
DWRITE_PANOSE_SCRIPT_TOPOLOGY_NO_FIT = 1
DWRITE_PANOSE_SCRIPT_TOPOLOGY_ROMAN_DISCONNECTED = 2
DWRITE_PANOSE_SCRIPT_TOPOLOGY_ROMAN_TRAILING = 3
DWRITE_PANOSE_SCRIPT_TOPOLOGY_ROMAN_CONNECTED = 4
DWRITE_PANOSE_SCRIPT_TOPOLOGY_CURSIVE_DISCONNECTED = 5
DWRITE_PANOSE_SCRIPT_TOPOLOGY_CURSIVE_TRAILING = 6
DWRITE_PANOSE_SCRIPT_TOPOLOGY_CURSIVE_CONNECTED = 7
DWRITE_PANOSE_SCRIPT_TOPOLOGY_BLACKLETTER_DISCONNECTED = 8
DWRITE_PANOSE_SCRIPT_TOPOLOGY_BLACKLETTER_TRAILING = 9
DWRITE_PANOSE_SCRIPT_TOPOLOGY_BLACKLETTER_CONNECTED = 10
DWRITE_PANOSE_SCRIPT_FORM = Int32
DWRITE_PANOSE_SCRIPT_FORM_ANY = 0
DWRITE_PANOSE_SCRIPT_FORM_NO_FIT = 1
DWRITE_PANOSE_SCRIPT_FORM_UPRIGHT_NO_WRAPPING = 2
DWRITE_PANOSE_SCRIPT_FORM_UPRIGHT_SOME_WRAPPING = 3
DWRITE_PANOSE_SCRIPT_FORM_UPRIGHT_MORE_WRAPPING = 4
DWRITE_PANOSE_SCRIPT_FORM_UPRIGHT_EXTREME_WRAPPING = 5
DWRITE_PANOSE_SCRIPT_FORM_OBLIQUE_NO_WRAPPING = 6
DWRITE_PANOSE_SCRIPT_FORM_OBLIQUE_SOME_WRAPPING = 7
DWRITE_PANOSE_SCRIPT_FORM_OBLIQUE_MORE_WRAPPING = 8
DWRITE_PANOSE_SCRIPT_FORM_OBLIQUE_EXTREME_WRAPPING = 9
DWRITE_PANOSE_SCRIPT_FORM_EXAGGERATED_NO_WRAPPING = 10
DWRITE_PANOSE_SCRIPT_FORM_EXAGGERATED_SOME_WRAPPING = 11
DWRITE_PANOSE_SCRIPT_FORM_EXAGGERATED_MORE_WRAPPING = 12
DWRITE_PANOSE_SCRIPT_FORM_EXAGGERATED_EXTREME_WRAPPING = 13
DWRITE_PANOSE_FINIALS = Int32
DWRITE_PANOSE_FINIALS_ANY = 0
DWRITE_PANOSE_FINIALS_NO_FIT = 1
DWRITE_PANOSE_FINIALS_NONE_NO_LOOPS = 2
DWRITE_PANOSE_FINIALS_NONE_CLOSED_LOOPS = 3
DWRITE_PANOSE_FINIALS_NONE_OPEN_LOOPS = 4
DWRITE_PANOSE_FINIALS_SHARP_NO_LOOPS = 5
DWRITE_PANOSE_FINIALS_SHARP_CLOSED_LOOPS = 6
DWRITE_PANOSE_FINIALS_SHARP_OPEN_LOOPS = 7
DWRITE_PANOSE_FINIALS_TAPERED_NO_LOOPS = 8
DWRITE_PANOSE_FINIALS_TAPERED_CLOSED_LOOPS = 9
DWRITE_PANOSE_FINIALS_TAPERED_OPEN_LOOPS = 10
DWRITE_PANOSE_FINIALS_ROUND_NO_LOOPS = 11
DWRITE_PANOSE_FINIALS_ROUND_CLOSED_LOOPS = 12
DWRITE_PANOSE_FINIALS_ROUND_OPEN_LOOPS = 13
DWRITE_PANOSE_XASCENT = Int32
DWRITE_PANOSE_XASCENT_ANY = 0
DWRITE_PANOSE_XASCENT_NO_FIT = 1
DWRITE_PANOSE_XASCENT_VERY_LOW = 2
DWRITE_PANOSE_XASCENT_LOW = 3
DWRITE_PANOSE_XASCENT_MEDIUM = 4
DWRITE_PANOSE_XASCENT_HIGH = 5
DWRITE_PANOSE_XASCENT_VERY_HIGH = 6
DWRITE_PANOSE_DECORATIVE_CLASS = Int32
DWRITE_PANOSE_DECORATIVE_CLASS_ANY = 0
DWRITE_PANOSE_DECORATIVE_CLASS_NO_FIT = 1
DWRITE_PANOSE_DECORATIVE_CLASS_DERIVATIVE = 2
DWRITE_PANOSE_DECORATIVE_CLASS_NONSTANDARD_TOPOLOGY = 3
DWRITE_PANOSE_DECORATIVE_CLASS_NONSTANDARD_ELEMENTS = 4
DWRITE_PANOSE_DECORATIVE_CLASS_NONSTANDARD_ASPECT = 5
DWRITE_PANOSE_DECORATIVE_CLASS_INITIALS = 6
DWRITE_PANOSE_DECORATIVE_CLASS_CARTOON = 7
DWRITE_PANOSE_DECORATIVE_CLASS_PICTURE_STEMS = 8
DWRITE_PANOSE_DECORATIVE_CLASS_ORNAMENTED = 9
DWRITE_PANOSE_DECORATIVE_CLASS_TEXT_AND_BACKGROUND = 10
DWRITE_PANOSE_DECORATIVE_CLASS_COLLAGE = 11
DWRITE_PANOSE_DECORATIVE_CLASS_MONTAGE = 12
DWRITE_PANOSE_ASPECT = Int32
DWRITE_PANOSE_ASPECT_ANY = 0
DWRITE_PANOSE_ASPECT_NO_FIT = 1
DWRITE_PANOSE_ASPECT_SUPER_CONDENSED = 2
DWRITE_PANOSE_ASPECT_VERY_CONDENSED = 3
DWRITE_PANOSE_ASPECT_CONDENSED = 4
DWRITE_PANOSE_ASPECT_NORMAL = 5
DWRITE_PANOSE_ASPECT_EXTENDED = 6
DWRITE_PANOSE_ASPECT_VERY_EXTENDED = 7
DWRITE_PANOSE_ASPECT_SUPER_EXTENDED = 8
DWRITE_PANOSE_ASPECT_MONOSPACED = 9
DWRITE_PANOSE_FILL = Int32
DWRITE_PANOSE_FILL_ANY = 0
DWRITE_PANOSE_FILL_NO_FIT = 1
DWRITE_PANOSE_FILL_STANDARD_SOLID_FILL = 2
DWRITE_PANOSE_FILL_NO_FILL = 3
DWRITE_PANOSE_FILL_PATTERNED_FILL = 4
DWRITE_PANOSE_FILL_COMPLEX_FILL = 5
DWRITE_PANOSE_FILL_SHAPED_FILL = 6
DWRITE_PANOSE_FILL_DRAWN_DISTRESSED = 7
DWRITE_PANOSE_LINING = Int32
DWRITE_PANOSE_LINING_ANY = 0
DWRITE_PANOSE_LINING_NO_FIT = 1
DWRITE_PANOSE_LINING_NONE = 2
DWRITE_PANOSE_LINING_INLINE = 3
DWRITE_PANOSE_LINING_OUTLINE = 4
DWRITE_PANOSE_LINING_ENGRAVED = 5
DWRITE_PANOSE_LINING_SHADOW = 6
DWRITE_PANOSE_LINING_RELIEF = 7
DWRITE_PANOSE_LINING_BACKDROP = 8
DWRITE_PANOSE_DECORATIVE_TOPOLOGY = Int32
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_ANY = 0
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_NO_FIT = 1
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_STANDARD = 2
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_SQUARE = 3
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_MULTIPLE_SEGMENT = 4
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_ART_DECO = 5
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_UNEVEN_WEIGHTING = 6
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_DIVERSE_ARMS = 7
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_DIVERSE_FORMS = 8
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_LOMBARDIC_FORMS = 9
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_UPPER_CASE_IN_LOWER_CASE = 10
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_IMPLIED_TOPOLOGY = 11
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_HORSESHOE_E_AND_A = 12
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_CURSIVE = 13
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_BLACKLETTER = 14
DWRITE_PANOSE_DECORATIVE_TOPOLOGY_SWASH_VARIANCE = 15
DWRITE_PANOSE_CHARACTER_RANGES = Int32
DWRITE_PANOSE_CHARACTER_RANGES_ANY = 0
DWRITE_PANOSE_CHARACTER_RANGES_NO_FIT = 1
DWRITE_PANOSE_CHARACTER_RANGES_EXTENDED_COLLECTION = 2
DWRITE_PANOSE_CHARACTER_RANGES_LITERALS = 3
DWRITE_PANOSE_CHARACTER_RANGES_NO_LOWER_CASE = 4
DWRITE_PANOSE_CHARACTER_RANGES_SMALL_CAPS = 5
DWRITE_PANOSE_SYMBOL_KIND = Int32
DWRITE_PANOSE_SYMBOL_KIND_ANY = 0
DWRITE_PANOSE_SYMBOL_KIND_NO_FIT = 1
DWRITE_PANOSE_SYMBOL_KIND_MONTAGES = 2
DWRITE_PANOSE_SYMBOL_KIND_PICTURES = 3
DWRITE_PANOSE_SYMBOL_KIND_SHAPES = 4
DWRITE_PANOSE_SYMBOL_KIND_SCIENTIFIC = 5
DWRITE_PANOSE_SYMBOL_KIND_MUSIC = 6
DWRITE_PANOSE_SYMBOL_KIND_EXPERT = 7
DWRITE_PANOSE_SYMBOL_KIND_PATTERNS = 8
DWRITE_PANOSE_SYMBOL_KIND_BOARDERS = 9
DWRITE_PANOSE_SYMBOL_KIND_ICONS = 10
DWRITE_PANOSE_SYMBOL_KIND_LOGOS = 11
DWRITE_PANOSE_SYMBOL_KIND_INDUSTRY_SPECIFIC = 12
DWRITE_PANOSE_SYMBOL_ASPECT_RATIO = Int32
DWRITE_PANOSE_SYMBOL_ASPECT_RATIO_ANY = 0
DWRITE_PANOSE_SYMBOL_ASPECT_RATIO_NO_FIT = 1
DWRITE_PANOSE_SYMBOL_ASPECT_RATIO_NO_WIDTH = 2
DWRITE_PANOSE_SYMBOL_ASPECT_RATIO_EXCEPTIONALLY_WIDE = 3
DWRITE_PANOSE_SYMBOL_ASPECT_RATIO_SUPER_WIDE = 4
DWRITE_PANOSE_SYMBOL_ASPECT_RATIO_VERY_WIDE = 5
DWRITE_PANOSE_SYMBOL_ASPECT_RATIO_WIDE = 6
DWRITE_PANOSE_SYMBOL_ASPECT_RATIO_NORMAL = 7
DWRITE_PANOSE_SYMBOL_ASPECT_RATIO_NARROW = 8
DWRITE_PANOSE_SYMBOL_ASPECT_RATIO_VERY_NARROW = 9
DWRITE_OUTLINE_THRESHOLD = Int32
DWRITE_OUTLINE_THRESHOLD_ANTIALIASED = 0
DWRITE_OUTLINE_THRESHOLD_ALIASED = 1
DWRITE_BASELINE = Int32
DWRITE_BASELINE_DEFAULT = 0
DWRITE_BASELINE_ROMAN = 1
DWRITE_BASELINE_CENTRAL = 2
DWRITE_BASELINE_MATH = 3
DWRITE_BASELINE_HANGING = 4
DWRITE_BASELINE_IDEOGRAPHIC_BOTTOM = 5
DWRITE_BASELINE_IDEOGRAPHIC_TOP = 6
DWRITE_BASELINE_MINIMUM = 7
DWRITE_BASELINE_MAXIMUM = 8
DWRITE_VERTICAL_GLYPH_ORIENTATION = Int32
DWRITE_VERTICAL_GLYPH_ORIENTATION_DEFAULT = 0
DWRITE_VERTICAL_GLYPH_ORIENTATION_STACKED = 1
DWRITE_GLYPH_ORIENTATION_ANGLE = Int32
DWRITE_GLYPH_ORIENTATION_ANGLE_0_DEGREES = 0
DWRITE_GLYPH_ORIENTATION_ANGLE_90_DEGREES = 1
DWRITE_GLYPH_ORIENTATION_ANGLE_180_DEGREES = 2
DWRITE_GLYPH_ORIENTATION_ANGLE_270_DEGREES = 3
def _define_DWRITE_FONT_METRICS1_head():
    class DWRITE_FONT_METRICS1(Structure):
        pass
    return DWRITE_FONT_METRICS1
def _define_DWRITE_FONT_METRICS1():
    DWRITE_FONT_METRICS1 = win32more.Graphics.DirectWrite.DWRITE_FONT_METRICS1_head
    DWRITE_FONT_METRICS1._fields_ = [
        ("__AnonymousBase_DWrite_1_L627_C38", win32more.Graphics.DirectWrite.DWRITE_FONT_METRICS),
        ("glyphBoxLeft", Int16),
        ("glyphBoxTop", Int16),
        ("glyphBoxRight", Int16),
        ("glyphBoxBottom", Int16),
        ("subscriptPositionX", Int16),
        ("subscriptPositionY", Int16),
        ("subscriptSizeX", Int16),
        ("subscriptSizeY", Int16),
        ("superscriptPositionX", Int16),
        ("superscriptPositionY", Int16),
        ("superscriptSizeX", Int16),
        ("superscriptSizeY", Int16),
        ("hasTypographicMetrics", win32more.Foundation.BOOL),
    ]
    return DWRITE_FONT_METRICS1
def _define_DWRITE_CARET_METRICS_head():
    class DWRITE_CARET_METRICS(Structure):
        pass
    return DWRITE_CARET_METRICS
def _define_DWRITE_CARET_METRICS():
    DWRITE_CARET_METRICS = win32more.Graphics.DirectWrite.DWRITE_CARET_METRICS_head
    DWRITE_CARET_METRICS._fields_ = [
        ("slopeRise", Int16),
        ("slopeRun", Int16),
        ("offset", Int16),
    ]
    return DWRITE_CARET_METRICS
def _define_DWRITE_PANOSE_head():
    class DWRITE_PANOSE(Union):
        pass
    return DWRITE_PANOSE
def _define_DWRITE_PANOSE():
    DWRITE_PANOSE = win32more.Graphics.DirectWrite.DWRITE_PANOSE_head
    class DWRITE_PANOSE__decorative_e__Struct(Structure):
        pass
    DWRITE_PANOSE__decorative_e__Struct._fields_ = [
        ("familyKind", Byte),
        ("decorativeClass", Byte),
        ("weight", Byte),
        ("aspect", Byte),
        ("contrast", Byte),
        ("serifVariant", Byte),
        ("fill", Byte),
        ("lining", Byte),
        ("decorativeTopology", Byte),
        ("characterRange", Byte),
    ]
    class DWRITE_PANOSE__text_e__Struct(Structure):
        pass
    DWRITE_PANOSE__text_e__Struct._fields_ = [
        ("familyKind", Byte),
        ("serifStyle", Byte),
        ("weight", Byte),
        ("proportion", Byte),
        ("contrast", Byte),
        ("strokeVariation", Byte),
        ("armStyle", Byte),
        ("letterform", Byte),
        ("midline", Byte),
        ("xHeight", Byte),
    ]
    class DWRITE_PANOSE__symbol_e__Struct(Structure):
        pass
    DWRITE_PANOSE__symbol_e__Struct._fields_ = [
        ("familyKind", Byte),
        ("symbolKind", Byte),
        ("weight", Byte),
        ("spacing", Byte),
        ("aspectRatioAndContrast", Byte),
        ("aspectRatio94", Byte),
        ("aspectRatio119", Byte),
        ("aspectRatio157", Byte),
        ("aspectRatio163", Byte),
        ("aspectRatio211", Byte),
    ]
    class DWRITE_PANOSE__script_e__Struct(Structure):
        pass
    DWRITE_PANOSE__script_e__Struct._fields_ = [
        ("familyKind", Byte),
        ("toolKind", Byte),
        ("weight", Byte),
        ("spacing", Byte),
        ("aspectRatio", Byte),
        ("contrast", Byte),
        ("scriptTopology", Byte),
        ("scriptForm", Byte),
        ("finials", Byte),
        ("xAscent", Byte),
    ]
    DWRITE_PANOSE._fields_ = [
        ("values", Byte * 10),
        ("familyKind", Byte),
        ("text", DWRITE_PANOSE__text_e__Struct),
        ("script", DWRITE_PANOSE__script_e__Struct),
        ("decorative", DWRITE_PANOSE__decorative_e__Struct),
        ("symbol", DWRITE_PANOSE__symbol_e__Struct),
    ]
    return DWRITE_PANOSE
def _define_DWRITE_UNICODE_RANGE_head():
    class DWRITE_UNICODE_RANGE(Structure):
        pass
    return DWRITE_UNICODE_RANGE
def _define_DWRITE_UNICODE_RANGE():
    DWRITE_UNICODE_RANGE = win32more.Graphics.DirectWrite.DWRITE_UNICODE_RANGE_head
    DWRITE_UNICODE_RANGE._fields_ = [
        ("first", UInt32),
        ("last", UInt32),
    ]
    return DWRITE_UNICODE_RANGE
def _define_DWRITE_SCRIPT_PROPERTIES_head():
    class DWRITE_SCRIPT_PROPERTIES(Structure):
        pass
    return DWRITE_SCRIPT_PROPERTIES
def _define_DWRITE_SCRIPT_PROPERTIES():
    DWRITE_SCRIPT_PROPERTIES = win32more.Graphics.DirectWrite.DWRITE_SCRIPT_PROPERTIES_head
    DWRITE_SCRIPT_PROPERTIES._fields_ = [
        ("isoScriptCode", UInt32),
        ("isoScriptNumber", UInt32),
        ("clusterLookahead", UInt32),
        ("justificationCharacter", UInt32),
        ("_bitfield", UInt32),
    ]
    return DWRITE_SCRIPT_PROPERTIES
def _define_DWRITE_JUSTIFICATION_OPPORTUNITY_head():
    class DWRITE_JUSTIFICATION_OPPORTUNITY(Structure):
        pass
    return DWRITE_JUSTIFICATION_OPPORTUNITY
def _define_DWRITE_JUSTIFICATION_OPPORTUNITY():
    DWRITE_JUSTIFICATION_OPPORTUNITY = win32more.Graphics.DirectWrite.DWRITE_JUSTIFICATION_OPPORTUNITY_head
    DWRITE_JUSTIFICATION_OPPORTUNITY._fields_ = [
        ("expansionMinimum", Single),
        ("expansionMaximum", Single),
        ("compressionMaximum", Single),
        ("_bitfield", UInt32),
    ]
    return DWRITE_JUSTIFICATION_OPPORTUNITY
def _define_IDWriteFactory1_head():
    class IDWriteFactory1(win32more.Graphics.DirectWrite.IDWriteFactory_head):
        Guid = Guid('30572f99-dac6-41db-a16e-0486307e606a')
    return IDWriteFactory1
def _define_IDWriteFactory1():
    IDWriteFactory1 = win32more.Graphics.DirectWrite.IDWriteFactory1_head
    IDWriteFactory1.GetEudcFontCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontCollection_head),win32more.Foundation.BOOL, use_last_error=False)(24, 'GetEudcFontCollection', ((1, 'fontCollection'),(1, 'checkForUpdates'),)))
    IDWriteFactory1.CreateCustomRenderingParams = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,Single,Single,win32more.Graphics.DirectWrite.DWRITE_PIXEL_GEOMETRY,win32more.Graphics.DirectWrite.DWRITE_RENDERING_MODE,POINTER(win32more.Graphics.DirectWrite.IDWriteRenderingParams1_head), use_last_error=False)(25, 'CreateCustomRenderingParams', ((1, 'gamma'),(1, 'enhancedContrast'),(1, 'enhancedContrastGrayscale'),(1, 'clearTypeLevel'),(1, 'pixelGeometry'),(1, 'renderingMode'),(1, 'renderingParams'),)))
    return IDWriteFactory1
def _define_IDWriteFontFace1_head():
    class IDWriteFontFace1(win32more.Graphics.DirectWrite.IDWriteFontFace_head):
        Guid = Guid('a71efdb4-9fdb-4838-ad90-cfc3be8c3daf')
    return IDWriteFontFace1
def _define_IDWriteFontFace1():
    IDWriteFontFace1 = win32more.Graphics.DirectWrite.IDWriteFontFace1_head
    IDWriteFontFace1.GetMetrics = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_METRICS1_head), use_last_error=False)(18, 'GetMetrics', ((1, 'fontMetrics'),)))
    IDWriteFontFace1.GetGdiCompatibleMetrics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,POINTER(win32more.Graphics.DirectWrite.DWRITE_MATRIX_head),POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_METRICS1_head), use_last_error=False)(19, 'GetGdiCompatibleMetrics', ((1, 'emSize'),(1, 'pixelsPerDip'),(1, 'transform'),(1, 'fontMetrics'),)))
    IDWriteFontFace1.GetCaretMetrics = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.DirectWrite.DWRITE_CARET_METRICS_head), use_last_error=False)(20, 'GetCaretMetrics', ((1, 'caretMetrics'),)))
    IDWriteFontFace1.GetUnicodeRanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.DirectWrite.DWRITE_UNICODE_RANGE),POINTER(UInt32), use_last_error=False)(21, 'GetUnicodeRanges', ((1, 'maxRangeCount'),(1, 'unicodeRanges'),(1, 'actualRangeCount'),)))
    IDWriteFontFace1.IsMonospacedFont = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(22, 'IsMonospacedFont', ()))
    IDWriteFontFace1.GetDesignGlyphAdvances = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt16),POINTER(Int32),win32more.Foundation.BOOL, use_last_error=False)(23, 'GetDesignGlyphAdvances', ((1, 'glyphCount'),(1, 'glyphIndices'),(1, 'glyphAdvances'),(1, 'isSideways'),)))
    IDWriteFontFace1.GetGdiCompatibleGlyphAdvances = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,POINTER(win32more.Graphics.DirectWrite.DWRITE_MATRIX_head),win32more.Foundation.BOOL,win32more.Foundation.BOOL,UInt32,POINTER(UInt16),POINTER(Int32), use_last_error=False)(24, 'GetGdiCompatibleGlyphAdvances', ((1, 'emSize'),(1, 'pixelsPerDip'),(1, 'transform'),(1, 'useGdiNatural'),(1, 'isSideways'),(1, 'glyphCount'),(1, 'glyphIndices'),(1, 'glyphAdvances'),)))
    IDWriteFontFace1.GetKerningPairAdjustments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt16),POINTER(Int32), use_last_error=False)(25, 'GetKerningPairAdjustments', ((1, 'glyphCount'),(1, 'glyphIndices'),(1, 'glyphAdvanceAdjustments'),)))
    IDWriteFontFace1.HasKerningPairs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(26, 'HasKerningPairs', ()))
    IDWriteFontFace1.GetRecommendedRenderingMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,Single,POINTER(win32more.Graphics.DirectWrite.DWRITE_MATRIX_head),win32more.Foundation.BOOL,win32more.Graphics.DirectWrite.DWRITE_OUTLINE_THRESHOLD,win32more.Graphics.DirectWrite.DWRITE_MEASURING_MODE,POINTER(win32more.Graphics.DirectWrite.DWRITE_RENDERING_MODE), use_last_error=False)(27, 'GetRecommendedRenderingMode', ((1, 'fontEmSize'),(1, 'dpiX'),(1, 'dpiY'),(1, 'transform'),(1, 'isSideways'),(1, 'outlineThreshold'),(1, 'measuringMode'),(1, 'renderingMode'),)))
    IDWriteFontFace1.GetVerticalGlyphVariants = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt16),POINTER(UInt16), use_last_error=False)(28, 'GetVerticalGlyphVariants', ((1, 'glyphCount'),(1, 'nominalGlyphIndices'),(1, 'verticalGlyphIndices'),)))
    IDWriteFontFace1.HasVerticalGlyphVariants = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(29, 'HasVerticalGlyphVariants', ()))
    return IDWriteFontFace1
def _define_IDWriteFont1_head():
    class IDWriteFont1(win32more.Graphics.DirectWrite.IDWriteFont_head):
        Guid = Guid('acd16696-8c14-4f5d-877e-fe3fc1d32738')
    return IDWriteFont1
def _define_IDWriteFont1():
    IDWriteFont1 = win32more.Graphics.DirectWrite.IDWriteFont1_head
    IDWriteFont1.GetMetrics = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_METRICS1_head), use_last_error=False)(14, 'GetMetrics', ((1, 'fontMetrics'),)))
    IDWriteFont1.GetPanose = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.DirectWrite.DWRITE_PANOSE_head), use_last_error=False)(15, 'GetPanose', ((1, 'panose'),)))
    IDWriteFont1.GetUnicodeRanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.DirectWrite.DWRITE_UNICODE_RANGE),POINTER(UInt32), use_last_error=False)(16, 'GetUnicodeRanges', ((1, 'maxRangeCount'),(1, 'unicodeRanges'),(1, 'actualRangeCount'),)))
    IDWriteFont1.IsMonospacedFont = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(17, 'IsMonospacedFont', ()))
    return IDWriteFont1
def _define_IDWriteRenderingParams1_head():
    class IDWriteRenderingParams1(win32more.Graphics.DirectWrite.IDWriteRenderingParams_head):
        Guid = Guid('94413cf4-a6fc-4248-8b50-6674348fcad3')
    return IDWriteRenderingParams1
def _define_IDWriteRenderingParams1():
    IDWriteRenderingParams1 = win32more.Graphics.DirectWrite.IDWriteRenderingParams1_head
    IDWriteRenderingParams1.GetGrayscaleEnhancedContrast = COMMETHOD(WINFUNCTYPE(Single, use_last_error=False)(8, 'GetGrayscaleEnhancedContrast', ()))
    return IDWriteRenderingParams1
def _define_IDWriteTextAnalyzer1_head():
    class IDWriteTextAnalyzer1(win32more.Graphics.DirectWrite.IDWriteTextAnalyzer_head):
        Guid = Guid('80dad800-e21f-4e83-96ce-bfcce500db7c')
    return IDWriteTextAnalyzer1
def _define_IDWriteTextAnalyzer1():
    IDWriteTextAnalyzer1 = win32more.Graphics.DirectWrite.IDWriteTextAnalyzer1_head
    IDWriteTextAnalyzer1.ApplyCharacterSpacing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,Single,UInt32,UInt32,POINTER(UInt16),POINTER(Single),POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_OFFSET),POINTER(win32more.Graphics.DirectWrite.DWRITE_SHAPING_GLYPH_PROPERTIES),POINTER(Single),POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_OFFSET), use_last_error=False)(10, 'ApplyCharacterSpacing', ((1, 'leadingSpacing'),(1, 'trailingSpacing'),(1, 'minimumAdvanceWidth'),(1, 'textLength'),(1, 'glyphCount'),(1, 'clusterMap'),(1, 'glyphAdvances'),(1, 'glyphOffsets'),(1, 'glyphProperties'),(1, 'modifiedGlyphAdvances'),(1, 'modifiedGlyphOffsets'),)))
    IDWriteTextAnalyzer1.GetBaseline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFontFace_head,win32more.Graphics.DirectWrite.DWRITE_BASELINE,win32more.Foundation.BOOL,win32more.Foundation.BOOL,win32more.Graphics.DirectWrite.DWRITE_SCRIPT_ANALYSIS,win32more.Foundation.PWSTR,POINTER(Int32),POINTER(win32more.Foundation.BOOL), use_last_error=False)(11, 'GetBaseline', ((1, 'fontFace'),(1, 'baseline'),(1, 'isVertical'),(1, 'isSimulationAllowed'),(1, 'scriptAnalysis'),(1, 'localeName'),(1, 'baselineCoordinate'),(1, 'exists'),)))
    IDWriteTextAnalyzer1.AnalyzeVerticalGlyphOrientation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteTextAnalysisSource1_head,UInt32,UInt32,win32more.Graphics.DirectWrite.IDWriteTextAnalysisSink1_head, use_last_error=False)(12, 'AnalyzeVerticalGlyphOrientation', ((1, 'analysisSource'),(1, 'textPosition'),(1, 'textLength'),(1, 'analysisSink'),)))
    IDWriteTextAnalyzer1.GetGlyphOrientationTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_GLYPH_ORIENTATION_ANGLE,win32more.Foundation.BOOL,POINTER(win32more.Graphics.DirectWrite.DWRITE_MATRIX_head), use_last_error=False)(13, 'GetGlyphOrientationTransform', ((1, 'glyphOrientationAngle'),(1, 'isSideways'),(1, 'transform'),)))
    IDWriteTextAnalyzer1.GetScriptProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_SCRIPT_ANALYSIS,POINTER(win32more.Graphics.DirectWrite.DWRITE_SCRIPT_PROPERTIES_head), use_last_error=False)(14, 'GetScriptProperties', ((1, 'scriptAnalysis'),(1, 'scriptProperties'),)))
    IDWriteTextAnalyzer1.GetTextComplexity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32,win32more.Graphics.DirectWrite.IDWriteFontFace_head,POINTER(win32more.Foundation.BOOL),POINTER(UInt32),POINTER(UInt16), use_last_error=False)(15, 'GetTextComplexity', ((1, 'textString'),(1, 'textLength'),(1, 'fontFace'),(1, 'isTextSimple'),(1, 'textLengthRead'),(1, 'glyphIndices'),)))
    IDWriteTextAnalyzer1.GetJustificationOpportunities = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFontFace_head,Single,win32more.Graphics.DirectWrite.DWRITE_SCRIPT_ANALYSIS,UInt32,UInt32,POINTER(Char),POINTER(UInt16),POINTER(win32more.Graphics.DirectWrite.DWRITE_SHAPING_GLYPH_PROPERTIES),POINTER(win32more.Graphics.DirectWrite.DWRITE_JUSTIFICATION_OPPORTUNITY), use_last_error=False)(16, 'GetJustificationOpportunities', ((1, 'fontFace'),(1, 'fontEmSize'),(1, 'scriptAnalysis'),(1, 'textLength'),(1, 'glyphCount'),(1, 'textString'),(1, 'clusterMap'),(1, 'glyphProperties'),(1, 'justificationOpportunities'),)))
    IDWriteTextAnalyzer1.JustifyGlyphAdvances = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,UInt32,POINTER(win32more.Graphics.DirectWrite.DWRITE_JUSTIFICATION_OPPORTUNITY),POINTER(Single),POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_OFFSET),POINTER(Single),POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_OFFSET), use_last_error=False)(17, 'JustifyGlyphAdvances', ((1, 'lineWidth'),(1, 'glyphCount'),(1, 'justificationOpportunities'),(1, 'glyphAdvances'),(1, 'glyphOffsets'),(1, 'justifiedGlyphAdvances'),(1, 'justifiedGlyphOffsets'),)))
    IDWriteTextAnalyzer1.GetJustifiedGlyphs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFontFace_head,Single,win32more.Graphics.DirectWrite.DWRITE_SCRIPT_ANALYSIS,UInt32,UInt32,UInt32,POINTER(UInt16),POINTER(UInt16),POINTER(Single),POINTER(Single),POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_OFFSET),POINTER(win32more.Graphics.DirectWrite.DWRITE_SHAPING_GLYPH_PROPERTIES),POINTER(UInt32),POINTER(UInt16),POINTER(UInt16),POINTER(Single),POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_OFFSET), use_last_error=False)(18, 'GetJustifiedGlyphs', ((1, 'fontFace'),(1, 'fontEmSize'),(1, 'scriptAnalysis'),(1, 'textLength'),(1, 'glyphCount'),(1, 'maxGlyphCount'),(1, 'clusterMap'),(1, 'glyphIndices'),(1, 'glyphAdvances'),(1, 'justifiedGlyphAdvances'),(1, 'justifiedGlyphOffsets'),(1, 'glyphProperties'),(1, 'actualGlyphCount'),(1, 'modifiedClusterMap'),(1, 'modifiedGlyphIndices'),(1, 'modifiedGlyphAdvances'),(1, 'modifiedGlyphOffsets'),)))
    return IDWriteTextAnalyzer1
def _define_IDWriteTextAnalysisSource1_head():
    class IDWriteTextAnalysisSource1(win32more.Graphics.DirectWrite.IDWriteTextAnalysisSource_head):
        Guid = Guid('639cfad8-0fb4-4b21-a58a-067920120009')
    return IDWriteTextAnalysisSource1
def _define_IDWriteTextAnalysisSource1():
    IDWriteTextAnalysisSource1 = win32more.Graphics.DirectWrite.IDWriteTextAnalysisSource1_head
    IDWriteTextAnalysisSource1.GetVerticalGlyphOrientation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(win32more.Graphics.DirectWrite.DWRITE_VERTICAL_GLYPH_ORIENTATION),c_char_p_no, use_last_error=False)(8, 'GetVerticalGlyphOrientation', ((1, 'textPosition'),(1, 'textLength'),(1, 'glyphOrientation'),(1, 'bidiLevel'),)))
    return IDWriteTextAnalysisSource1
def _define_IDWriteTextAnalysisSink1_head():
    class IDWriteTextAnalysisSink1(win32more.Graphics.DirectWrite.IDWriteTextAnalysisSink_head):
        Guid = Guid('b0d941a0-85e7-4d8b-9fd3-5ced9934482a')
    return IDWriteTextAnalysisSink1
def _define_IDWriteTextAnalysisSink1():
    IDWriteTextAnalysisSink1 = win32more.Graphics.DirectWrite.IDWriteTextAnalysisSink1_head
    IDWriteTextAnalysisSink1.SetGlyphOrientation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Graphics.DirectWrite.DWRITE_GLYPH_ORIENTATION_ANGLE,Byte,win32more.Foundation.BOOL,win32more.Foundation.BOOL, use_last_error=False)(7, 'SetGlyphOrientation', ((1, 'textPosition'),(1, 'textLength'),(1, 'glyphOrientationAngle'),(1, 'adjustedBidiLevel'),(1, 'isSideways'),(1, 'isRightToLeft'),)))
    return IDWriteTextAnalysisSink1
def _define_IDWriteTextLayout1_head():
    class IDWriteTextLayout1(win32more.Graphics.DirectWrite.IDWriteTextLayout_head):
        Guid = Guid('9064d822-80a7-465c-a986-df65f78b8feb')
    return IDWriteTextLayout1
def _define_IDWriteTextLayout1():
    IDWriteTextLayout1 = win32more.Graphics.DirectWrite.IDWriteTextLayout1_head
    IDWriteTextLayout1.SetPairKerning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE, use_last_error=False)(67, 'SetPairKerning', ((1, 'isPairKerningEnabled'),(1, 'textRange'),)))
    IDWriteTextLayout1.GetPairKerning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE_head), use_last_error=False)(68, 'GetPairKerning', ((1, 'currentPosition'),(1, 'isPairKerningEnabled'),(1, 'textRange'),)))
    IDWriteTextLayout1.SetCharacterSpacing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,Single,win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE, use_last_error=False)(69, 'SetCharacterSpacing', ((1, 'leadingSpacing'),(1, 'trailingSpacing'),(1, 'minimumAdvanceWidth'),(1, 'textRange'),)))
    IDWriteTextLayout1.GetCharacterSpacing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Single),POINTER(Single),POINTER(Single),POINTER(win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE_head), use_last_error=False)(70, 'GetCharacterSpacing', ((1, 'currentPosition'),(1, 'leadingSpacing'),(1, 'trailingSpacing'),(1, 'minimumAdvanceWidth'),(1, 'textRange'),)))
    return IDWriteTextLayout1
DWRITE_TEXT_ANTIALIAS_MODE = Int32
DWRITE_TEXT_ANTIALIAS_MODE_CLEARTYPE = 0
DWRITE_TEXT_ANTIALIAS_MODE_GRAYSCALE = 1
def _define_IDWriteBitmapRenderTarget1_head():
    class IDWriteBitmapRenderTarget1(win32more.Graphics.DirectWrite.IDWriteBitmapRenderTarget_head):
        Guid = Guid('791e8298-3ef3-4230-9880-c9bdecc42064')
    return IDWriteBitmapRenderTarget1
def _define_IDWriteBitmapRenderTarget1():
    IDWriteBitmapRenderTarget1 = win32more.Graphics.DirectWrite.IDWriteBitmapRenderTarget1_head
    IDWriteBitmapRenderTarget1.GetTextAntialiasMode = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_TEXT_ANTIALIAS_MODE, use_last_error=False)(11, 'GetTextAntialiasMode', ()))
    IDWriteBitmapRenderTarget1.SetTextAntialiasMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_TEXT_ANTIALIAS_MODE, use_last_error=False)(12, 'SetTextAntialiasMode', ((1, 'antialiasMode'),)))
    return IDWriteBitmapRenderTarget1
DWRITE_OPTICAL_ALIGNMENT = Int32
DWRITE_OPTICAL_ALIGNMENT_NONE = 0
DWRITE_OPTICAL_ALIGNMENT_NO_SIDE_BEARINGS = 1
DWRITE_GRID_FIT_MODE = Int32
DWRITE_GRID_FIT_MODE_DEFAULT = 0
DWRITE_GRID_FIT_MODE_DISABLED = 1
DWRITE_GRID_FIT_MODE_ENABLED = 2
def _define_DWRITE_TEXT_METRICS1_head():
    class DWRITE_TEXT_METRICS1(Structure):
        pass
    return DWRITE_TEXT_METRICS1
def _define_DWRITE_TEXT_METRICS1():
    DWRITE_TEXT_METRICS1 = win32more.Graphics.DirectWrite.DWRITE_TEXT_METRICS1_head
    DWRITE_TEXT_METRICS1._fields_ = [
        ("Base", win32more.Graphics.DirectWrite.DWRITE_TEXT_METRICS),
        ("heightIncludingTrailingWhitespace", Single),
    ]
    return DWRITE_TEXT_METRICS1
def _define_IDWriteTextRenderer1_head():
    class IDWriteTextRenderer1(win32more.Graphics.DirectWrite.IDWriteTextRenderer_head):
        Guid = Guid('d3e0e934-22a0-427e-aae4-7d9574b59db1')
    return IDWriteTextRenderer1
def _define_IDWriteTextRenderer1():
    IDWriteTextRenderer1 = win32more.Graphics.DirectWrite.IDWriteTextRenderer1_head
    IDWriteTextRenderer1.DrawGlyphRun = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,Single,Single,win32more.Graphics.DirectWrite.DWRITE_GLYPH_ORIENTATION_ANGLE,win32more.Graphics.DirectWrite.DWRITE_MEASURING_MODE,POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_RUN_head),POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_RUN_DESCRIPTION_head),win32more.System.Com.IUnknown_head, use_last_error=False)(10, 'DrawGlyphRun', ((1, 'clientDrawingContext'),(1, 'baselineOriginX'),(1, 'baselineOriginY'),(1, 'orientationAngle'),(1, 'measuringMode'),(1, 'glyphRun'),(1, 'glyphRunDescription'),(1, 'clientDrawingEffect'),)))
    IDWriteTextRenderer1.DrawUnderline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,Single,Single,win32more.Graphics.DirectWrite.DWRITE_GLYPH_ORIENTATION_ANGLE,POINTER(win32more.Graphics.DirectWrite.DWRITE_UNDERLINE_head),win32more.System.Com.IUnknown_head, use_last_error=False)(11, 'DrawUnderline', ((1, 'clientDrawingContext'),(1, 'baselineOriginX'),(1, 'baselineOriginY'),(1, 'orientationAngle'),(1, 'underline'),(1, 'clientDrawingEffect'),)))
    IDWriteTextRenderer1.DrawStrikethrough = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,Single,Single,win32more.Graphics.DirectWrite.DWRITE_GLYPH_ORIENTATION_ANGLE,POINTER(win32more.Graphics.DirectWrite.DWRITE_STRIKETHROUGH_head),win32more.System.Com.IUnknown_head, use_last_error=False)(12, 'DrawStrikethrough', ((1, 'clientDrawingContext'),(1, 'baselineOriginX'),(1, 'baselineOriginY'),(1, 'orientationAngle'),(1, 'strikethrough'),(1, 'clientDrawingEffect'),)))
    IDWriteTextRenderer1.DrawInlineObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,Single,Single,win32more.Graphics.DirectWrite.DWRITE_GLYPH_ORIENTATION_ANGLE,win32more.Graphics.DirectWrite.IDWriteInlineObject_head,win32more.Foundation.BOOL,win32more.Foundation.BOOL,win32more.System.Com.IUnknown_head, use_last_error=False)(13, 'DrawInlineObject', ((1, 'clientDrawingContext'),(1, 'originX'),(1, 'originY'),(1, 'orientationAngle'),(1, 'inlineObject'),(1, 'isSideways'),(1, 'isRightToLeft'),(1, 'clientDrawingEffect'),)))
    return IDWriteTextRenderer1
def _define_IDWriteTextFormat1_head():
    class IDWriteTextFormat1(win32more.Graphics.DirectWrite.IDWriteTextFormat_head):
        Guid = Guid('5f174b49-0d8b-4cfb-8bca-f1cce9d06c67')
    return IDWriteTextFormat1
def _define_IDWriteTextFormat1():
    IDWriteTextFormat1 = win32more.Graphics.DirectWrite.IDWriteTextFormat1_head
    IDWriteTextFormat1.SetVerticalGlyphOrientation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_VERTICAL_GLYPH_ORIENTATION, use_last_error=False)(28, 'SetVerticalGlyphOrientation', ((1, 'glyphOrientation'),)))
    IDWriteTextFormat1.GetVerticalGlyphOrientation = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_VERTICAL_GLYPH_ORIENTATION, use_last_error=False)(29, 'GetVerticalGlyphOrientation', ()))
    IDWriteTextFormat1.SetLastLineWrapping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(30, 'SetLastLineWrapping', ((1, 'isLastLineWrappingEnabled'),)))
    IDWriteTextFormat1.GetLastLineWrapping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(31, 'GetLastLineWrapping', ()))
    IDWriteTextFormat1.SetOpticalAlignment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_OPTICAL_ALIGNMENT, use_last_error=False)(32, 'SetOpticalAlignment', ((1, 'opticalAlignment'),)))
    IDWriteTextFormat1.GetOpticalAlignment = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_OPTICAL_ALIGNMENT, use_last_error=False)(33, 'GetOpticalAlignment', ()))
    IDWriteTextFormat1.SetFontFallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFontFallback_head, use_last_error=False)(34, 'SetFontFallback', ((1, 'fontFallback'),)))
    IDWriteTextFormat1.GetFontFallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFallback_head), use_last_error=False)(35, 'GetFontFallback', ((1, 'fontFallback'),)))
    return IDWriteTextFormat1
def _define_IDWriteTextLayout2_head():
    class IDWriteTextLayout2(win32more.Graphics.DirectWrite.IDWriteTextLayout1_head):
        Guid = Guid('1093c18f-8d5e-43f0-b064-0917311b525e')
    return IDWriteTextLayout2
def _define_IDWriteTextLayout2():
    IDWriteTextLayout2 = win32more.Graphics.DirectWrite.IDWriteTextLayout2_head
    IDWriteTextLayout2.GetMetrics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_TEXT_METRICS1_head), use_last_error=False)(71, 'GetMetrics', ((1, 'textMetrics'),)))
    IDWriteTextLayout2.SetVerticalGlyphOrientation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_VERTICAL_GLYPH_ORIENTATION, use_last_error=False)(72, 'SetVerticalGlyphOrientation', ((1, 'glyphOrientation'),)))
    IDWriteTextLayout2.GetVerticalGlyphOrientation = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_VERTICAL_GLYPH_ORIENTATION, use_last_error=False)(73, 'GetVerticalGlyphOrientation', ()))
    IDWriteTextLayout2.SetLastLineWrapping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(74, 'SetLastLineWrapping', ((1, 'isLastLineWrappingEnabled'),)))
    IDWriteTextLayout2.GetLastLineWrapping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(75, 'GetLastLineWrapping', ()))
    IDWriteTextLayout2.SetOpticalAlignment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_OPTICAL_ALIGNMENT, use_last_error=False)(76, 'SetOpticalAlignment', ((1, 'opticalAlignment'),)))
    IDWriteTextLayout2.GetOpticalAlignment = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_OPTICAL_ALIGNMENT, use_last_error=False)(77, 'GetOpticalAlignment', ()))
    IDWriteTextLayout2.SetFontFallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFontFallback_head, use_last_error=False)(78, 'SetFontFallback', ((1, 'fontFallback'),)))
    IDWriteTextLayout2.GetFontFallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFallback_head), use_last_error=False)(79, 'GetFontFallback', ((1, 'fontFallback'),)))
    return IDWriteTextLayout2
def _define_IDWriteTextAnalyzer2_head():
    class IDWriteTextAnalyzer2(win32more.Graphics.DirectWrite.IDWriteTextAnalyzer1_head):
        Guid = Guid('553a9ff3-5693-4df7-b52b-74806f7f2eb9')
    return IDWriteTextAnalyzer2
def _define_IDWriteTextAnalyzer2():
    IDWriteTextAnalyzer2 = win32more.Graphics.DirectWrite.IDWriteTextAnalyzer2_head
    IDWriteTextAnalyzer2.GetGlyphOrientationTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_GLYPH_ORIENTATION_ANGLE,win32more.Foundation.BOOL,Single,Single,POINTER(win32more.Graphics.DirectWrite.DWRITE_MATRIX_head), use_last_error=False)(19, 'GetGlyphOrientationTransform', ((1, 'glyphOrientationAngle'),(1, 'isSideways'),(1, 'originX'),(1, 'originY'),(1, 'transform'),)))
    IDWriteTextAnalyzer2.GetTypographicFeatures = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFontFace_head,win32more.Graphics.DirectWrite.DWRITE_SCRIPT_ANALYSIS,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG), use_last_error=False)(20, 'GetTypographicFeatures', ((1, 'fontFace'),(1, 'scriptAnalysis'),(1, 'localeName'),(1, 'maxTagCount'),(1, 'actualTagCount'),(1, 'tags'),)))
    IDWriteTextAnalyzer2.CheckTypographicFeature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFontFace_head,win32more.Graphics.DirectWrite.DWRITE_SCRIPT_ANALYSIS,win32more.Foundation.PWSTR,win32more.Graphics.DirectWrite.DWRITE_FONT_FEATURE_TAG,UInt32,POINTER(UInt16),POINTER(Byte), use_last_error=False)(21, 'CheckTypographicFeature', ((1, 'fontFace'),(1, 'scriptAnalysis'),(1, 'localeName'),(1, 'featureTag'),(1, 'glyphCount'),(1, 'glyphIndices'),(1, 'featureApplies'),)))
    return IDWriteTextAnalyzer2
def _define_IDWriteFontFallback_head():
    class IDWriteFontFallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('efa008f9-f7a1-48bf-b05c-f224713cc0ff')
    return IDWriteFontFallback
def _define_IDWriteFontFallback():
    IDWriteFontFallback = win32more.Graphics.DirectWrite.IDWriteFontFallback_head
    IDWriteFontFallback.MapCharacters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteTextAnalysisSource_head,UInt32,UInt32,win32more.Graphics.DirectWrite.IDWriteFontCollection_head,win32more.Foundation.PWSTR,win32more.Graphics.DirectWrite.DWRITE_FONT_WEIGHT,win32more.Graphics.DirectWrite.DWRITE_FONT_STYLE,win32more.Graphics.DirectWrite.DWRITE_FONT_STRETCH,POINTER(UInt32),POINTER(win32more.Graphics.DirectWrite.IDWriteFont_head),POINTER(Single), use_last_error=False)(3, 'MapCharacters', ((1, 'analysisSource'),(1, 'textPosition'),(1, 'textLength'),(1, 'baseFontCollection'),(1, 'baseFamilyName'),(1, 'baseWeight'),(1, 'baseStyle'),(1, 'baseStretch'),(1, 'mappedLength'),(1, 'mappedFont'),(1, 'scale'),)))
    return IDWriteFontFallback
def _define_IDWriteFontFallbackBuilder_head():
    class IDWriteFontFallbackBuilder(win32more.System.Com.IUnknown_head):
        Guid = Guid('fd882d06-8aba-4fb8-b849-8be8b73e14de')
    return IDWriteFontFallbackBuilder
def _define_IDWriteFontFallbackBuilder():
    IDWriteFontFallbackBuilder = win32more.Graphics.DirectWrite.IDWriteFontFallbackBuilder_head
    IDWriteFontFallbackBuilder.AddMapping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_UNICODE_RANGE),UInt32,POINTER(POINTER(UInt16)),UInt32,win32more.Graphics.DirectWrite.IDWriteFontCollection_head,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Single, use_last_error=False)(3, 'AddMapping', ((1, 'ranges'),(1, 'rangesCount'),(1, 'targetFamilyNames'),(1, 'targetFamilyNamesCount'),(1, 'fontCollection'),(1, 'localeName'),(1, 'baseFamilyName'),(1, 'scale'),)))
    IDWriteFontFallbackBuilder.AddMappings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFontFallback_head, use_last_error=False)(4, 'AddMappings', ((1, 'fontFallback'),)))
    IDWriteFontFallbackBuilder.CreateFontFallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFallback_head), use_last_error=False)(5, 'CreateFontFallback', ((1, 'fontFallback'),)))
    return IDWriteFontFallbackBuilder
def _define_IDWriteFont2_head():
    class IDWriteFont2(win32more.Graphics.DirectWrite.IDWriteFont1_head):
        Guid = Guid('29748ed6-8c9c-4a6a-be0b-d912e8538944')
    return IDWriteFont2
def _define_IDWriteFont2():
    IDWriteFont2 = win32more.Graphics.DirectWrite.IDWriteFont2_head
    IDWriteFont2.IsColorFont = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(18, 'IsColorFont', ()))
    return IDWriteFont2
def _define_IDWriteFontFace2_head():
    class IDWriteFontFace2(win32more.Graphics.DirectWrite.IDWriteFontFace1_head):
        Guid = Guid('d8b768ff-64bc-4e66-982b-ec8e87f693f7')
    return IDWriteFontFace2
def _define_IDWriteFontFace2():
    IDWriteFontFace2 = win32more.Graphics.DirectWrite.IDWriteFontFace2_head
    IDWriteFontFace2.IsColorFont = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(30, 'IsColorFont', ()))
    IDWriteFontFace2.GetColorPaletteCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(31, 'GetColorPaletteCount', ()))
    IDWriteFontFace2.GetPaletteEntryCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(32, 'GetPaletteEntryCount', ()))
    IDWriteFontFace2.GetPaletteEntries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,POINTER(win32more.Graphics.DirectWrite.DWRITE_COLOR_F), use_last_error=False)(33, 'GetPaletteEntries', ((1, 'colorPaletteIndex'),(1, 'firstEntryIndex'),(1, 'entryCount'),(1, 'paletteEntries'),)))
    IDWriteFontFace2.GetRecommendedRenderingMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,Single,POINTER(win32more.Graphics.DirectWrite.DWRITE_MATRIX_head),win32more.Foundation.BOOL,win32more.Graphics.DirectWrite.DWRITE_OUTLINE_THRESHOLD,win32more.Graphics.DirectWrite.DWRITE_MEASURING_MODE,win32more.Graphics.DirectWrite.IDWriteRenderingParams_head,POINTER(win32more.Graphics.DirectWrite.DWRITE_RENDERING_MODE),POINTER(win32more.Graphics.DirectWrite.DWRITE_GRID_FIT_MODE), use_last_error=False)(34, 'GetRecommendedRenderingMode', ((1, 'fontEmSize'),(1, 'dpiX'),(1, 'dpiY'),(1, 'transform'),(1, 'isSideways'),(1, 'outlineThreshold'),(1, 'measuringMode'),(1, 'renderingParams'),(1, 'renderingMode'),(1, 'gridFitMode'),)))
    return IDWriteFontFace2
def _define_DWRITE_COLOR_GLYPH_RUN_head():
    class DWRITE_COLOR_GLYPH_RUN(Structure):
        pass
    return DWRITE_COLOR_GLYPH_RUN
def _define_DWRITE_COLOR_GLYPH_RUN():
    DWRITE_COLOR_GLYPH_RUN = win32more.Graphics.DirectWrite.DWRITE_COLOR_GLYPH_RUN_head
    DWRITE_COLOR_GLYPH_RUN._fields_ = [
        ("glyphRun", win32more.Graphics.DirectWrite.DWRITE_GLYPH_RUN),
        ("glyphRunDescription", POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_RUN_DESCRIPTION_head)),
        ("baselineOriginX", Single),
        ("baselineOriginY", Single),
        ("runColor", win32more.Graphics.DirectWrite.DWRITE_COLOR_F),
        ("paletteIndex", UInt16),
    ]
    return DWRITE_COLOR_GLYPH_RUN
def _define_IDWriteColorGlyphRunEnumerator_head():
    class IDWriteColorGlyphRunEnumerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('d31fbe17-f157-41a2-8d24-cb779e0560e8')
    return IDWriteColorGlyphRunEnumerator
def _define_IDWriteColorGlyphRunEnumerator():
    IDWriteColorGlyphRunEnumerator = win32more.Graphics.DirectWrite.IDWriteColorGlyphRunEnumerator_head
    IDWriteColorGlyphRunEnumerator.MoveNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'MoveNext', ((1, 'hasRun'),)))
    IDWriteColorGlyphRunEnumerator.GetCurrentRun = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Graphics.DirectWrite.DWRITE_COLOR_GLYPH_RUN_head)), use_last_error=False)(4, 'GetCurrentRun', ((1, 'colorGlyphRun'),)))
    return IDWriteColorGlyphRunEnumerator
def _define_IDWriteRenderingParams2_head():
    class IDWriteRenderingParams2(win32more.Graphics.DirectWrite.IDWriteRenderingParams1_head):
        Guid = Guid('f9d711c3-9777-40ae-87e8-3e5af9bf0948')
    return IDWriteRenderingParams2
def _define_IDWriteRenderingParams2():
    IDWriteRenderingParams2 = win32more.Graphics.DirectWrite.IDWriteRenderingParams2_head
    IDWriteRenderingParams2.GetGridFitMode = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_GRID_FIT_MODE, use_last_error=False)(9, 'GetGridFitMode', ()))
    return IDWriteRenderingParams2
def _define_IDWriteFactory2_head():
    class IDWriteFactory2(win32more.Graphics.DirectWrite.IDWriteFactory1_head):
        Guid = Guid('0439fc60-ca44-4994-8dee-3a9af7b732ec')
    return IDWriteFactory2
def _define_IDWriteFactory2():
    IDWriteFactory2 = win32more.Graphics.DirectWrite.IDWriteFactory2_head
    IDWriteFactory2.GetSystemFontFallback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFallback_head), use_last_error=False)(26, 'GetSystemFontFallback', ((1, 'fontFallback'),)))
    IDWriteFactory2.CreateFontFallbackBuilder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFallbackBuilder_head), use_last_error=False)(27, 'CreateFontFallbackBuilder', ((1, 'fontFallbackBuilder'),)))
    IDWriteFactory2.TranslateColorGlyphRun = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_RUN_head),POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_RUN_DESCRIPTION_head),win32more.Graphics.DirectWrite.DWRITE_MEASURING_MODE,POINTER(win32more.Graphics.DirectWrite.DWRITE_MATRIX_head),UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteColorGlyphRunEnumerator_head), use_last_error=False)(28, 'TranslateColorGlyphRun', ((1, 'baselineOriginX'),(1, 'baselineOriginY'),(1, 'glyphRun'),(1, 'glyphRunDescription'),(1, 'measuringMode'),(1, 'worldToDeviceTransform'),(1, 'colorPaletteIndex'),(1, 'colorLayers'),)))
    IDWriteFactory2.CreateCustomRenderingParams = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,Single,Single,win32more.Graphics.DirectWrite.DWRITE_PIXEL_GEOMETRY,win32more.Graphics.DirectWrite.DWRITE_RENDERING_MODE,win32more.Graphics.DirectWrite.DWRITE_GRID_FIT_MODE,POINTER(win32more.Graphics.DirectWrite.IDWriteRenderingParams2_head), use_last_error=False)(29, 'CreateCustomRenderingParams', ((1, 'gamma'),(1, 'enhancedContrast'),(1, 'grayscaleEnhancedContrast'),(1, 'clearTypeLevel'),(1, 'pixelGeometry'),(1, 'renderingMode'),(1, 'gridFitMode'),(1, 'renderingParams'),)))
    IDWriteFactory2.CreateGlyphRunAnalysis = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_RUN_head),POINTER(win32more.Graphics.DirectWrite.DWRITE_MATRIX_head),win32more.Graphics.DirectWrite.DWRITE_RENDERING_MODE,win32more.Graphics.DirectWrite.DWRITE_MEASURING_MODE,win32more.Graphics.DirectWrite.DWRITE_GRID_FIT_MODE,win32more.Graphics.DirectWrite.DWRITE_TEXT_ANTIALIAS_MODE,Single,Single,POINTER(win32more.Graphics.DirectWrite.IDWriteGlyphRunAnalysis_head), use_last_error=False)(30, 'CreateGlyphRunAnalysis', ((1, 'glyphRun'),(1, 'transform'),(1, 'renderingMode'),(1, 'measuringMode'),(1, 'gridFitMode'),(1, 'antialiasMode'),(1, 'baselineOriginX'),(1, 'baselineOriginY'),(1, 'glyphRunAnalysis'),)))
    return IDWriteFactory2
DWRITE_FONT_PROPERTY_ID = Int32
DWRITE_FONT_PROPERTY_ID_NONE = 0
DWRITE_FONT_PROPERTY_ID_WEIGHT_STRETCH_STYLE_FAMILY_NAME = 1
DWRITE_FONT_PROPERTY_ID_TYPOGRAPHIC_FAMILY_NAME = 2
DWRITE_FONT_PROPERTY_ID_WEIGHT_STRETCH_STYLE_FACE_NAME = 3
DWRITE_FONT_PROPERTY_ID_FULL_NAME = 4
DWRITE_FONT_PROPERTY_ID_WIN32_FAMILY_NAME = 5
DWRITE_FONT_PROPERTY_ID_POSTSCRIPT_NAME = 6
DWRITE_FONT_PROPERTY_ID_DESIGN_SCRIPT_LANGUAGE_TAG = 7
DWRITE_FONT_PROPERTY_ID_SUPPORTED_SCRIPT_LANGUAGE_TAG = 8
DWRITE_FONT_PROPERTY_ID_SEMANTIC_TAG = 9
DWRITE_FONT_PROPERTY_ID_WEIGHT = 10
DWRITE_FONT_PROPERTY_ID_STRETCH = 11
DWRITE_FONT_PROPERTY_ID_STYLE = 12
DWRITE_FONT_PROPERTY_ID_TYPOGRAPHIC_FACE_NAME = 13
DWRITE_FONT_PROPERTY_ID_TOTAL = 13
DWRITE_FONT_PROPERTY_ID_TOTAL_RS3 = 14
DWRITE_FONT_PROPERTY_ID_PREFERRED_FAMILY_NAME = 2
DWRITE_FONT_PROPERTY_ID_FAMILY_NAME = 1
DWRITE_FONT_PROPERTY_ID_FACE_NAME = 3
def _define_DWRITE_FONT_PROPERTY_head():
    class DWRITE_FONT_PROPERTY(Structure):
        pass
    return DWRITE_FONT_PROPERTY
def _define_DWRITE_FONT_PROPERTY():
    DWRITE_FONT_PROPERTY = win32more.Graphics.DirectWrite.DWRITE_FONT_PROPERTY_head
    DWRITE_FONT_PROPERTY._fields_ = [
        ("propertyId", win32more.Graphics.DirectWrite.DWRITE_FONT_PROPERTY_ID),
        ("propertyValue", win32more.Foundation.PWSTR),
        ("localeName", win32more.Foundation.PWSTR),
    ]
    return DWRITE_FONT_PROPERTY
DWRITE_LOCALITY = Int32
DWRITE_LOCALITY_REMOTE = 0
DWRITE_LOCALITY_PARTIAL = 1
DWRITE_LOCALITY_LOCAL = 2
DWRITE_RENDERING_MODE1 = Int32
DWRITE_RENDERING_MODE1_DEFAULT = 0
DWRITE_RENDERING_MODE1_ALIASED = 1
DWRITE_RENDERING_MODE1_GDI_CLASSIC = 2
DWRITE_RENDERING_MODE1_GDI_NATURAL = 3
DWRITE_RENDERING_MODE1_NATURAL = 4
DWRITE_RENDERING_MODE1_NATURAL_SYMMETRIC = 5
DWRITE_RENDERING_MODE1_OUTLINE = 6
DWRITE_RENDERING_MODE1_NATURAL_SYMMETRIC_DOWNSAMPLED = 7
def _define_IDWriteRenderingParams3_head():
    class IDWriteRenderingParams3(win32more.Graphics.DirectWrite.IDWriteRenderingParams2_head):
        Guid = Guid('b7924baa-391b-412a-8c5c-e44cc2d867dc')
    return IDWriteRenderingParams3
def _define_IDWriteRenderingParams3():
    IDWriteRenderingParams3 = win32more.Graphics.DirectWrite.IDWriteRenderingParams3_head
    IDWriteRenderingParams3.GetRenderingMode1 = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_RENDERING_MODE1, use_last_error=False)(10, 'GetRenderingMode1', ()))
    return IDWriteRenderingParams3
def _define_IDWriteFactory3_head():
    class IDWriteFactory3(win32more.Graphics.DirectWrite.IDWriteFactory2_head):
        Guid = Guid('9a1b41c3-d3bb-466a-87fc-fe67556a3b65')
    return IDWriteFactory3
def _define_IDWriteFactory3():
    IDWriteFactory3 = win32more.Graphics.DirectWrite.IDWriteFactory3_head
    IDWriteFactory3.CreateGlyphRunAnalysis = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_RUN_head),POINTER(win32more.Graphics.DirectWrite.DWRITE_MATRIX_head),win32more.Graphics.DirectWrite.DWRITE_RENDERING_MODE1,win32more.Graphics.DirectWrite.DWRITE_MEASURING_MODE,win32more.Graphics.DirectWrite.DWRITE_GRID_FIT_MODE,win32more.Graphics.DirectWrite.DWRITE_TEXT_ANTIALIAS_MODE,Single,Single,POINTER(win32more.Graphics.DirectWrite.IDWriteGlyphRunAnalysis_head), use_last_error=False)(31, 'CreateGlyphRunAnalysis', ((1, 'glyphRun'),(1, 'transform'),(1, 'renderingMode'),(1, 'measuringMode'),(1, 'gridFitMode'),(1, 'antialiasMode'),(1, 'baselineOriginX'),(1, 'baselineOriginY'),(1, 'glyphRunAnalysis'),)))
    IDWriteFactory3.CreateCustomRenderingParams = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,Single,Single,win32more.Graphics.DirectWrite.DWRITE_PIXEL_GEOMETRY,win32more.Graphics.DirectWrite.DWRITE_RENDERING_MODE1,win32more.Graphics.DirectWrite.DWRITE_GRID_FIT_MODE,POINTER(win32more.Graphics.DirectWrite.IDWriteRenderingParams3_head), use_last_error=False)(32, 'CreateCustomRenderingParams', ((1, 'gamma'),(1, 'enhancedContrast'),(1, 'grayscaleEnhancedContrast'),(1, 'clearTypeLevel'),(1, 'pixelGeometry'),(1, 'renderingMode'),(1, 'gridFitMode'),(1, 'renderingParams'),)))
    IDWriteFactory3.CreateFontFaceReference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFontFile_head,UInt32,win32more.Graphics.DirectWrite.DWRITE_FONT_SIMULATIONS,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFaceReference_head), use_last_error=False)(33, 'CreateFontFaceReference', ((1, 'fontFile'),(1, 'faceIndex'),(1, 'fontSimulations'),(1, 'fontFaceReference'),)))
    IDWriteFactory3.CreateFontFaceReference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.FILETIME_head),UInt32,win32more.Graphics.DirectWrite.DWRITE_FONT_SIMULATIONS,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFaceReference_head), use_last_error=False)(34, 'CreateFontFaceReference', ((1, 'filePath'),(1, 'lastWriteTime'),(1, 'faceIndex'),(1, 'fontSimulations'),(1, 'fontFaceReference'),)))
    IDWriteFactory3.GetSystemFontSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontSet_head), use_last_error=False)(35, 'GetSystemFontSet', ((1, 'fontSet'),)))
    IDWriteFactory3.CreateFontSetBuilder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontSetBuilder_head), use_last_error=False)(36, 'CreateFontSetBuilder', ((1, 'fontSetBuilder'),)))
    IDWriteFactory3.CreateFontCollectionFromFontSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFontSet_head,POINTER(win32more.Graphics.DirectWrite.IDWriteFontCollection1_head), use_last_error=False)(37, 'CreateFontCollectionFromFontSet', ((1, 'fontSet'),(1, 'fontCollection'),)))
    IDWriteFactory3.GetSystemFontCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,POINTER(win32more.Graphics.DirectWrite.IDWriteFontCollection1_head),win32more.Foundation.BOOL, use_last_error=False)(38, 'GetSystemFontCollection', ((1, 'includeDownloadableFonts'),(1, 'fontCollection'),(1, 'checkForUpdates'),)))
    IDWriteFactory3.GetFontDownloadQueue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontDownloadQueue_head), use_last_error=False)(39, 'GetFontDownloadQueue', ((1, 'fontDownloadQueue'),)))
    return IDWriteFactory3
def _define_IDWriteFontSet_head():
    class IDWriteFontSet(win32more.System.Com.IUnknown_head):
        Guid = Guid('53585141-d9f8-4095-8321-d73cf6bd116b')
    return IDWriteFontSet
def _define_IDWriteFontSet():
    IDWriteFontSet = win32more.Graphics.DirectWrite.IDWriteFontSet_head
    IDWriteFontSet.GetFontCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(3, 'GetFontCount', ()))
    IDWriteFontSet.GetFontFaceReference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFaceReference_head), use_last_error=False)(4, 'GetFontFaceReference', ((1, 'listIndex'),(1, 'fontFaceReference'),)))
    IDWriteFontSet.FindFontFaceReference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFontFaceReference_head,POINTER(UInt32),POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'FindFontFaceReference', ((1, 'fontFaceReference'),(1, 'listIndex'),(1, 'exists'),)))
    IDWriteFontSet.FindFontFace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFontFace_head,POINTER(UInt32),POINTER(win32more.Foundation.BOOL), use_last_error=False)(6, 'FindFontFace', ((1, 'fontFace'),(1, 'listIndex'),(1, 'exists'),)))
    IDWriteFontSet.GetPropertyValues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_FONT_PROPERTY_ID,POINTER(win32more.Graphics.DirectWrite.IDWriteStringList_head), use_last_error=False)(7, 'GetPropertyValues', ((1, 'propertyID'),(1, 'values'),)))
    IDWriteFontSet.GetPropertyValues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_FONT_PROPERTY_ID,win32more.Foundation.PWSTR,POINTER(win32more.Graphics.DirectWrite.IDWriteStringList_head), use_last_error=False)(8, 'GetPropertyValues', ((1, 'propertyID'),(1, 'preferredLocaleNames'),(1, 'values'),)))
    IDWriteFontSet.GetPropertyValues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Graphics.DirectWrite.DWRITE_FONT_PROPERTY_ID,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Graphics.DirectWrite.IDWriteLocalizedStrings_head), use_last_error=False)(9, 'GetPropertyValues', ((1, 'listIndex'),(1, 'propertyId'),(1, 'exists'),(1, 'values'),)))
    IDWriteFontSet.GetPropertyOccurrenceCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_PROPERTY_head),POINTER(UInt32), use_last_error=False)(10, 'GetPropertyOccurrenceCount', ((1, 'property'),(1, 'propertyOccurrenceCount'),)))
    IDWriteFontSet.GetMatchingFonts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Graphics.DirectWrite.DWRITE_FONT_WEIGHT,win32more.Graphics.DirectWrite.DWRITE_FONT_STRETCH,win32more.Graphics.DirectWrite.DWRITE_FONT_STYLE,POINTER(win32more.Graphics.DirectWrite.IDWriteFontSet_head), use_last_error=False)(11, 'GetMatchingFonts', ((1, 'familyName'),(1, 'fontWeight'),(1, 'fontStretch'),(1, 'fontStyle'),(1, 'filteredSet'),)))
    IDWriteFontSet.GetMatchingFonts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_PROPERTY),UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteFontSet_head), use_last_error=False)(12, 'GetMatchingFonts', ((1, 'properties'),(1, 'propertyCount'),(1, 'filteredSet'),)))
    return IDWriteFontSet
def _define_IDWriteFontSetBuilder_head():
    class IDWriteFontSetBuilder(win32more.System.Com.IUnknown_head):
        Guid = Guid('2f642afe-9c68-4f40-b8be-457401afcb3d')
    return IDWriteFontSetBuilder
def _define_IDWriteFontSetBuilder():
    IDWriteFontSetBuilder = win32more.Graphics.DirectWrite.IDWriteFontSetBuilder_head
    IDWriteFontSetBuilder.AddFontFaceReference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFontFaceReference_head,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_PROPERTY),UInt32, use_last_error=False)(3, 'AddFontFaceReference', ((1, 'fontFaceReference'),(1, 'properties'),(1, 'propertyCount'),)))
    IDWriteFontSetBuilder.AddFontFaceReference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFontFaceReference_head, use_last_error=False)(4, 'AddFontFaceReference', ((1, 'fontFaceReference'),)))
    IDWriteFontSetBuilder.AddFontSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFontSet_head, use_last_error=False)(5, 'AddFontSet', ((1, 'fontSet'),)))
    IDWriteFontSetBuilder.CreateFontSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontSet_head), use_last_error=False)(6, 'CreateFontSet', ((1, 'fontSet'),)))
    return IDWriteFontSetBuilder
def _define_IDWriteFontCollection1_head():
    class IDWriteFontCollection1(win32more.Graphics.DirectWrite.IDWriteFontCollection_head):
        Guid = Guid('53585141-d9f8-4095-8321-d73cf6bd116c')
    return IDWriteFontCollection1
def _define_IDWriteFontCollection1():
    IDWriteFontCollection1 = win32more.Graphics.DirectWrite.IDWriteFontCollection1_head
    IDWriteFontCollection1.GetFontSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontSet_head), use_last_error=False)(7, 'GetFontSet', ((1, 'fontSet'),)))
    IDWriteFontCollection1.GetFontFamily = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFamily1_head), use_last_error=False)(8, 'GetFontFamily', ((1, 'index'),(1, 'fontFamily'),)))
    return IDWriteFontCollection1
def _define_IDWriteFontFamily1_head():
    class IDWriteFontFamily1(win32more.Graphics.DirectWrite.IDWriteFontFamily_head):
        Guid = Guid('da20d8ef-812a-4c43-9802-62ec4abd7adf')
    return IDWriteFontFamily1
def _define_IDWriteFontFamily1():
    IDWriteFontFamily1 = win32more.Graphics.DirectWrite.IDWriteFontFamily1_head
    IDWriteFontFamily1.GetFontLocality = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_LOCALITY,UInt32, use_last_error=False)(9, 'GetFontLocality', ((1, 'listIndex'),)))
    IDWriteFontFamily1.GetFont = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteFont3_head), use_last_error=False)(10, 'GetFont', ((1, 'listIndex'),(1, 'font'),)))
    IDWriteFontFamily1.GetFontFaceReference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFaceReference_head), use_last_error=False)(11, 'GetFontFaceReference', ((1, 'listIndex'),(1, 'fontFaceReference'),)))
    return IDWriteFontFamily1
def _define_IDWriteFontList1_head():
    class IDWriteFontList1(win32more.Graphics.DirectWrite.IDWriteFontList_head):
        Guid = Guid('da20d8ef-812a-4c43-9802-62ec4abd7ade')
    return IDWriteFontList1
def _define_IDWriteFontList1():
    IDWriteFontList1 = win32more.Graphics.DirectWrite.IDWriteFontList1_head
    IDWriteFontList1.GetFontLocality = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_LOCALITY,UInt32, use_last_error=False)(6, 'GetFontLocality', ((1, 'listIndex'),)))
    IDWriteFontList1.GetFont = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteFont3_head), use_last_error=False)(7, 'GetFont', ((1, 'listIndex'),(1, 'font'),)))
    IDWriteFontList1.GetFontFaceReference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFaceReference_head), use_last_error=False)(8, 'GetFontFaceReference', ((1, 'listIndex'),(1, 'fontFaceReference'),)))
    return IDWriteFontList1
def _define_IDWriteFontFaceReference_head():
    class IDWriteFontFaceReference(win32more.System.Com.IUnknown_head):
        Guid = Guid('5e7fa7ca-dde3-424c-89f0-9fcd6fed58cd')
    return IDWriteFontFaceReference
def _define_IDWriteFontFaceReference():
    IDWriteFontFaceReference = win32more.Graphics.DirectWrite.IDWriteFontFaceReference_head
    IDWriteFontFaceReference.CreateFontFace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFace3_head), use_last_error=False)(3, 'CreateFontFace', ((1, 'fontFace'),)))
    IDWriteFontFaceReference.CreateFontFaceWithSimulations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_FONT_SIMULATIONS,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFace3_head), use_last_error=False)(4, 'CreateFontFaceWithSimulations', ((1, 'fontFaceSimulationFlags'),(1, 'fontFace'),)))
    IDWriteFontFaceReference.Equals = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.DirectWrite.IDWriteFontFaceReference_head, use_last_error=False)(5, 'Equals', ((1, 'fontFaceReference'),)))
    IDWriteFontFaceReference.GetFontFaceIndex = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(6, 'GetFontFaceIndex', ()))
    IDWriteFontFaceReference.GetSimulations = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_FONT_SIMULATIONS, use_last_error=False)(7, 'GetSimulations', ()))
    IDWriteFontFaceReference.GetFontFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFile_head), use_last_error=False)(8, 'GetFontFile', ((1, 'fontFile'),)))
    IDWriteFontFaceReference.GetLocalFileSize = COMMETHOD(WINFUNCTYPE(UInt64, use_last_error=False)(9, 'GetLocalFileSize', ()))
    IDWriteFontFaceReference.GetFileSize = COMMETHOD(WINFUNCTYPE(UInt64, use_last_error=False)(10, 'GetFileSize', ()))
    IDWriteFontFaceReference.GetFileTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(11, 'GetFileTime', ((1, 'lastWriteTime'),)))
    IDWriteFontFaceReference.GetLocality = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_LOCALITY, use_last_error=False)(12, 'GetLocality', ()))
    IDWriteFontFaceReference.EnqueueFontDownloadRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(13, 'EnqueueFontDownloadRequest', ()))
    IDWriteFontFaceReference.EnqueueCharacterDownloadRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32, use_last_error=False)(14, 'EnqueueCharacterDownloadRequest', ((1, 'characters'),(1, 'characterCount'),)))
    IDWriteFontFaceReference.EnqueueGlyphDownloadRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),UInt32, use_last_error=False)(15, 'EnqueueGlyphDownloadRequest', ((1, 'glyphIndices'),(1, 'glyphCount'),)))
    IDWriteFontFaceReference.EnqueueFileFragmentDownloadRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,UInt64, use_last_error=False)(16, 'EnqueueFileFragmentDownloadRequest', ((1, 'fileOffset'),(1, 'fragmentSize'),)))
    return IDWriteFontFaceReference
def _define_IDWriteFont3_head():
    class IDWriteFont3(win32more.Graphics.DirectWrite.IDWriteFont2_head):
        Guid = Guid('29748ed6-8c9c-4a6a-be0b-d912e8538944')
    return IDWriteFont3
def _define_IDWriteFont3():
    IDWriteFont3 = win32more.Graphics.DirectWrite.IDWriteFont3_head
    IDWriteFont3.CreateFontFace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFace3_head), use_last_error=False)(19, 'CreateFontFace', ((1, 'fontFace'),)))
    IDWriteFont3.Equals = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.DirectWrite.IDWriteFont_head, use_last_error=False)(20, 'Equals', ((1, 'font'),)))
    IDWriteFont3.GetFontFaceReference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFaceReference_head), use_last_error=False)(21, 'GetFontFaceReference', ((1, 'fontFaceReference'),)))
    IDWriteFont3.HasCharacter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,UInt32, use_last_error=False)(22, 'HasCharacter', ((1, 'unicodeValue'),)))
    IDWriteFont3.GetLocality = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_LOCALITY, use_last_error=False)(23, 'GetLocality', ()))
    return IDWriteFont3
def _define_IDWriteFontFace3_head():
    class IDWriteFontFace3(win32more.Graphics.DirectWrite.IDWriteFontFace2_head):
        Guid = Guid('d37d7598-09be-4222-a236-2081341cc1f2')
    return IDWriteFontFace3
def _define_IDWriteFontFace3():
    IDWriteFontFace3 = win32more.Graphics.DirectWrite.IDWriteFontFace3_head
    IDWriteFontFace3.GetFontFaceReference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFaceReference_head), use_last_error=False)(35, 'GetFontFaceReference', ((1, 'fontFaceReference'),)))
    IDWriteFontFace3.GetPanose = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.DirectWrite.DWRITE_PANOSE_head), use_last_error=False)(36, 'GetPanose', ((1, 'panose'),)))
    IDWriteFontFace3.GetWeight = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_FONT_WEIGHT, use_last_error=False)(37, 'GetWeight', ()))
    IDWriteFontFace3.GetStretch = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_FONT_STRETCH, use_last_error=False)(38, 'GetStretch', ()))
    IDWriteFontFace3.GetStyle = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_FONT_STYLE, use_last_error=False)(39, 'GetStyle', ()))
    IDWriteFontFace3.GetFamilyNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteLocalizedStrings_head), use_last_error=False)(40, 'GetFamilyNames', ((1, 'names'),)))
    IDWriteFontFace3.GetFaceNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteLocalizedStrings_head), use_last_error=False)(41, 'GetFaceNames', ((1, 'names'),)))
    IDWriteFontFace3.GetInformationalStrings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_INFORMATIONAL_STRING_ID,POINTER(win32more.Graphics.DirectWrite.IDWriteLocalizedStrings_head),POINTER(win32more.Foundation.BOOL), use_last_error=False)(42, 'GetInformationalStrings', ((1, 'informationalStringID'),(1, 'informationalStrings'),(1, 'exists'),)))
    IDWriteFontFace3.HasCharacter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,UInt32, use_last_error=False)(43, 'HasCharacter', ((1, 'unicodeValue'),)))
    IDWriteFontFace3.GetRecommendedRenderingMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,Single,POINTER(win32more.Graphics.DirectWrite.DWRITE_MATRIX_head),win32more.Foundation.BOOL,win32more.Graphics.DirectWrite.DWRITE_OUTLINE_THRESHOLD,win32more.Graphics.DirectWrite.DWRITE_MEASURING_MODE,win32more.Graphics.DirectWrite.IDWriteRenderingParams_head,POINTER(win32more.Graphics.DirectWrite.DWRITE_RENDERING_MODE1),POINTER(win32more.Graphics.DirectWrite.DWRITE_GRID_FIT_MODE), use_last_error=False)(44, 'GetRecommendedRenderingMode', ((1, 'fontEmSize'),(1, 'dpiX'),(1, 'dpiY'),(1, 'transform'),(1, 'isSideways'),(1, 'outlineThreshold'),(1, 'measuringMode'),(1, 'renderingParams'),(1, 'renderingMode'),(1, 'gridFitMode'),)))
    IDWriteFontFace3.IsCharacterLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,UInt32, use_last_error=False)(45, 'IsCharacterLocal', ((1, 'unicodeValue'),)))
    IDWriteFontFace3.IsGlyphLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,UInt16, use_last_error=False)(46, 'IsGlyphLocal', ((1, 'glyphId'),)))
    IDWriteFontFace3.AreCharactersLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Char),UInt32,win32more.Foundation.BOOL,POINTER(win32more.Foundation.BOOL), use_last_error=False)(47, 'AreCharactersLocal', ((1, 'characters'),(1, 'characterCount'),(1, 'enqueueIfNotLocal'),(1, 'isLocal'),)))
    IDWriteFontFace3.AreGlyphsLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),UInt32,win32more.Foundation.BOOL,POINTER(win32more.Foundation.BOOL), use_last_error=False)(48, 'AreGlyphsLocal', ((1, 'glyphIndices'),(1, 'glyphCount'),(1, 'enqueueIfNotLocal'),(1, 'isLocal'),)))
    return IDWriteFontFace3
def _define_IDWriteStringList_head():
    class IDWriteStringList(win32more.System.Com.IUnknown_head):
        Guid = Guid('cfee3140-1157-47ca-8b85-31bfcf3f2d0e')
    return IDWriteStringList
def _define_IDWriteStringList():
    IDWriteStringList = win32more.Graphics.DirectWrite.IDWriteStringList_head
    IDWriteStringList.GetCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(3, 'GetCount', ()))
    IDWriteStringList.GetLocaleNameLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(4, 'GetLocaleNameLength', ((1, 'listIndex'),(1, 'length'),)))
    IDWriteStringList.GetLocaleName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Char),UInt32, use_last_error=False)(5, 'GetLocaleName', ((1, 'listIndex'),(1, 'localeName'),(1, 'size'),)))
    IDWriteStringList.GetStringLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(6, 'GetStringLength', ((1, 'listIndex'),(1, 'length'),)))
    IDWriteStringList.GetString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Char),UInt32, use_last_error=False)(7, 'GetString', ((1, 'listIndex'),(1, 'stringBuffer'),(1, 'stringBufferSize'),)))
    return IDWriteStringList
def _define_IDWriteFontDownloadListener_head():
    class IDWriteFontDownloadListener(win32more.System.Com.IUnknown_head):
        Guid = Guid('b06fe5b9-43ec-4393-881b-dbe4dc72fda7')
    return IDWriteFontDownloadListener
def _define_IDWriteFontDownloadListener():
    IDWriteFontDownloadListener = win32more.Graphics.DirectWrite.IDWriteFontDownloadListener_head
    IDWriteFontDownloadListener.DownloadCompleted = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.DirectWrite.IDWriteFontDownloadQueue_head,win32more.System.Com.IUnknown_head,win32more.Foundation.HRESULT, use_last_error=False)(3, 'DownloadCompleted', ((1, 'downloadQueue'),(1, 'context'),(1, 'downloadResult'),)))
    return IDWriteFontDownloadListener
def _define_IDWriteFontDownloadQueue_head():
    class IDWriteFontDownloadQueue(win32more.System.Com.IUnknown_head):
        Guid = Guid('b71e6052-5aea-4fa3-832e-f60d431f7e91')
    return IDWriteFontDownloadQueue
def _define_IDWriteFontDownloadQueue():
    IDWriteFontDownloadQueue = win32more.Graphics.DirectWrite.IDWriteFontDownloadQueue_head
    IDWriteFontDownloadQueue.AddListener = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFontDownloadListener_head,POINTER(UInt32), use_last_error=False)(3, 'AddListener', ((1, 'listener'),(1, 'token'),)))
    IDWriteFontDownloadQueue.RemoveListener = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'RemoveListener', ((1, 'token'),)))
    IDWriteFontDownloadQueue.IsEmpty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(5, 'IsEmpty', ()))
    IDWriteFontDownloadQueue.BeginDownload = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(6, 'BeginDownload', ((1, 'context'),)))
    IDWriteFontDownloadQueue.CancelDownload = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'CancelDownload', ()))
    IDWriteFontDownloadQueue.GetGenerationCount = COMMETHOD(WINFUNCTYPE(UInt64, use_last_error=False)(8, 'GetGenerationCount', ()))
    return IDWriteFontDownloadQueue
def _define_IDWriteGdiInterop1_head():
    class IDWriteGdiInterop1(win32more.Graphics.DirectWrite.IDWriteGdiInterop_head):
        Guid = Guid('4556be70-3abd-4f70-90be-421780a6f515')
    return IDWriteGdiInterop1
def _define_IDWriteGdiInterop1():
    IDWriteGdiInterop1 = win32more.Graphics.DirectWrite.IDWriteGdiInterop1_head
    IDWriteGdiInterop1.CreateFontFromLOGFONT = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Gdi.LOGFONTW_head),win32more.Graphics.DirectWrite.IDWriteFontCollection_head,POINTER(win32more.Graphics.DirectWrite.IDWriteFont_head), use_last_error=False)(8, 'CreateFontFromLOGFONT', ((1, 'logFont'),(1, 'fontCollection'),(1, 'font'),)))
    IDWriteGdiInterop1.GetFontSignature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFontFace_head,POINTER(win32more.Globalization.FONTSIGNATURE_head), use_last_error=False)(9, 'GetFontSignature', ((1, 'fontFace'),(1, 'fontSignature'),)))
    IDWriteGdiInterop1.GetFontSignature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFont_head,POINTER(win32more.Globalization.FONTSIGNATURE_head), use_last_error=False)(10, 'GetFontSignature', ((1, 'font'),(1, 'fontSignature'),)))
    IDWriteGdiInterop1.GetMatchingFontsByLOGFONT = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Gdi.LOGFONTA_head),win32more.Graphics.DirectWrite.IDWriteFontSet_head,POINTER(win32more.Graphics.DirectWrite.IDWriteFontSet_head), use_last_error=False)(11, 'GetMatchingFontsByLOGFONT', ((1, 'logFont'),(1, 'fontSet'),(1, 'filteredSet'),)))
    return IDWriteGdiInterop1
def _define_DWRITE_LINE_METRICS1_head():
    class DWRITE_LINE_METRICS1(Structure):
        pass
    return DWRITE_LINE_METRICS1
def _define_DWRITE_LINE_METRICS1():
    DWRITE_LINE_METRICS1 = win32more.Graphics.DirectWrite.DWRITE_LINE_METRICS1_head
    DWRITE_LINE_METRICS1._fields_ = [
        ("Base", win32more.Graphics.DirectWrite.DWRITE_LINE_METRICS),
        ("leadingBefore", Single),
        ("leadingAfter", Single),
    ]
    return DWRITE_LINE_METRICS1
DWRITE_FONT_LINE_GAP_USAGE = Int32
DWRITE_FONT_LINE_GAP_USAGE_DEFAULT = 0
DWRITE_FONT_LINE_GAP_USAGE_DISABLED = 1
DWRITE_FONT_LINE_GAP_USAGE_ENABLED = 2
def _define_DWRITE_LINE_SPACING_head():
    class DWRITE_LINE_SPACING(Structure):
        pass
    return DWRITE_LINE_SPACING
def _define_DWRITE_LINE_SPACING():
    DWRITE_LINE_SPACING = win32more.Graphics.DirectWrite.DWRITE_LINE_SPACING_head
    DWRITE_LINE_SPACING._fields_ = [
        ("method", win32more.Graphics.DirectWrite.DWRITE_LINE_SPACING_METHOD),
        ("height", Single),
        ("baseline", Single),
        ("leadingBefore", Single),
        ("fontLineGapUsage", win32more.Graphics.DirectWrite.DWRITE_FONT_LINE_GAP_USAGE),
    ]
    return DWRITE_LINE_SPACING
def _define_IDWriteTextFormat2_head():
    class IDWriteTextFormat2(win32more.Graphics.DirectWrite.IDWriteTextFormat1_head):
        Guid = Guid('f67e0edd-9e3d-4ecc-8c32-4183253dfe70')
    return IDWriteTextFormat2
def _define_IDWriteTextFormat2():
    IDWriteTextFormat2 = win32more.Graphics.DirectWrite.IDWriteTextFormat2_head
    IDWriteTextFormat2.SetLineSpacing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_LINE_SPACING_head), use_last_error=False)(36, 'SetLineSpacing', ((1, 'lineSpacingOptions'),)))
    IDWriteTextFormat2.GetLineSpacing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_LINE_SPACING_head), use_last_error=False)(37, 'GetLineSpacing', ((1, 'lineSpacingOptions'),)))
    return IDWriteTextFormat2
def _define_IDWriteTextLayout3_head():
    class IDWriteTextLayout3(win32more.Graphics.DirectWrite.IDWriteTextLayout2_head):
        Guid = Guid('07ddcd52-020e-4de8-ac33-6c953d83f92d')
    return IDWriteTextLayout3
def _define_IDWriteTextLayout3():
    IDWriteTextLayout3 = win32more.Graphics.DirectWrite.IDWriteTextLayout3_head
    IDWriteTextLayout3.InvalidateLayout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(80, 'InvalidateLayout', ()))
    IDWriteTextLayout3.SetLineSpacing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_LINE_SPACING_head), use_last_error=False)(81, 'SetLineSpacing', ((1, 'lineSpacingOptions'),)))
    IDWriteTextLayout3.GetLineSpacing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_LINE_SPACING_head), use_last_error=False)(82, 'GetLineSpacing', ((1, 'lineSpacingOptions'),)))
    IDWriteTextLayout3.GetLineMetrics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_LINE_METRICS1),UInt32,POINTER(UInt32), use_last_error=False)(83, 'GetLineMetrics', ((1, 'lineMetrics'),(1, 'maxLineCount'),(1, 'actualLineCount'),)))
    return IDWriteTextLayout3
def _define_DWRITE_COLOR_GLYPH_RUN1_head():
    class DWRITE_COLOR_GLYPH_RUN1(Structure):
        pass
    return DWRITE_COLOR_GLYPH_RUN1
def _define_DWRITE_COLOR_GLYPH_RUN1():
    DWRITE_COLOR_GLYPH_RUN1 = win32more.Graphics.DirectWrite.DWRITE_COLOR_GLYPH_RUN1_head
    DWRITE_COLOR_GLYPH_RUN1._fields_ = [
        ("Base", win32more.Graphics.DirectWrite.DWRITE_COLOR_GLYPH_RUN),
        ("glyphImageFormat", win32more.Graphics.DirectWrite.DWRITE_GLYPH_IMAGE_FORMATS),
        ("measuringMode", win32more.Graphics.DirectWrite.DWRITE_MEASURING_MODE),
    ]
    return DWRITE_COLOR_GLYPH_RUN1
def _define_DWRITE_GLYPH_IMAGE_DATA_head():
    class DWRITE_GLYPH_IMAGE_DATA(Structure):
        pass
    return DWRITE_GLYPH_IMAGE_DATA
def _define_DWRITE_GLYPH_IMAGE_DATA():
    DWRITE_GLYPH_IMAGE_DATA = win32more.Graphics.DirectWrite.DWRITE_GLYPH_IMAGE_DATA_head
    DWRITE_GLYPH_IMAGE_DATA._fields_ = [
        ("imageData", c_void_p),
        ("imageDataSize", UInt32),
        ("uniqueDataId", UInt32),
        ("pixelsPerEm", UInt32),
        ("pixelSize", win32more.Graphics.Direct2D.Common.D2D_SIZE_U),
        ("horizontalLeftOrigin", win32more.Foundation.POINT),
        ("horizontalRightOrigin", win32more.Foundation.POINT),
        ("verticalTopOrigin", win32more.Foundation.POINT),
        ("verticalBottomOrigin", win32more.Foundation.POINT),
    ]
    return DWRITE_GLYPH_IMAGE_DATA
def _define_IDWriteColorGlyphRunEnumerator1_head():
    class IDWriteColorGlyphRunEnumerator1(win32more.Graphics.DirectWrite.IDWriteColorGlyphRunEnumerator_head):
        Guid = Guid('7c5f86da-c7a1-4f05-b8e1-55a179fe5a35')
    return IDWriteColorGlyphRunEnumerator1
def _define_IDWriteColorGlyphRunEnumerator1():
    IDWriteColorGlyphRunEnumerator1 = win32more.Graphics.DirectWrite.IDWriteColorGlyphRunEnumerator1_head
    IDWriteColorGlyphRunEnumerator1.GetCurrentRun = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Graphics.DirectWrite.DWRITE_COLOR_GLYPH_RUN1_head)), use_last_error=False)(5, 'GetCurrentRun', ((1, 'colorGlyphRun'),)))
    return IDWriteColorGlyphRunEnumerator1
def _define_IDWriteFontFace4_head():
    class IDWriteFontFace4(win32more.Graphics.DirectWrite.IDWriteFontFace3_head):
        Guid = Guid('27f2a904-4eb8-441d-9678-0563f53e3e2f')
    return IDWriteFontFace4
def _define_IDWriteFontFace4():
    IDWriteFontFace4 = win32more.Graphics.DirectWrite.IDWriteFontFace4_head
    IDWriteFontFace4.GetGlyphImageFormats = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,UInt32,UInt32,POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_IMAGE_FORMATS), use_last_error=False)(49, 'GetGlyphImageFormats', ((1, 'glyphId'),(1, 'pixelsPerEmFirst'),(1, 'pixelsPerEmLast'),(1, 'glyphImageFormats'),)))
    IDWriteFontFace4.GetGlyphImageFormats = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_GLYPH_IMAGE_FORMATS, use_last_error=False)(50, 'GetGlyphImageFormats', ()))
    IDWriteFontFace4.GetGlyphImageData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,UInt32,win32more.Graphics.DirectWrite.DWRITE_GLYPH_IMAGE_FORMATS,POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_IMAGE_DATA_head),POINTER(c_void_p), use_last_error=False)(51, 'GetGlyphImageData', ((1, 'glyphId'),(1, 'pixelsPerEm'),(1, 'glyphImageFormat'),(1, 'glyphData'),(1, 'glyphDataContext'),)))
    IDWriteFontFace4.ReleaseGlyphImageData = COMMETHOD(WINFUNCTYPE(Void,c_void_p, use_last_error=False)(52, 'ReleaseGlyphImageData', ((1, 'glyphDataContext'),)))
    return IDWriteFontFace4
def _define_IDWriteFactory4_head():
    class IDWriteFactory4(win32more.Graphics.DirectWrite.IDWriteFactory3_head):
        Guid = Guid('4b0b5bd3-0797-4549-8ac5-fe915cc53856')
    return IDWriteFactory4
def _define_IDWriteFactory4():
    IDWriteFactory4 = win32more.Graphics.DirectWrite.IDWriteFactory4_head
    IDWriteFactory4.TranslateColorGlyphRun = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.Common.D2D_POINT_2F,POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_RUN_head),POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_RUN_DESCRIPTION_head),win32more.Graphics.DirectWrite.DWRITE_GLYPH_IMAGE_FORMATS,win32more.Graphics.DirectWrite.DWRITE_MEASURING_MODE,POINTER(win32more.Graphics.DirectWrite.DWRITE_MATRIX_head),UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteColorGlyphRunEnumerator1_head), use_last_error=False)(40, 'TranslateColorGlyphRun', ((1, 'baselineOrigin'),(1, 'glyphRun'),(1, 'glyphRunDescription'),(1, 'desiredGlyphImageFormats'),(1, 'measuringMode'),(1, 'worldAndDpiTransform'),(1, 'colorPaletteIndex'),(1, 'colorLayers'),)))
    IDWriteFactory4.ComputeGlyphOrigins = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_RUN_head),win32more.Graphics.Direct2D.Common.D2D_POINT_2F,POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2F_head), use_last_error=False)(41, 'ComputeGlyphOrigins', ((1, 'glyphRun'),(1, 'baselineOrigin'),(1, 'glyphOrigins'),)))
    IDWriteFactory4.ComputeGlyphOrigins = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_GLYPH_RUN_head),win32more.Graphics.DirectWrite.DWRITE_MEASURING_MODE,win32more.Graphics.Direct2D.Common.D2D_POINT_2F,POINTER(win32more.Graphics.DirectWrite.DWRITE_MATRIX_head),POINTER(win32more.Graphics.Direct2D.Common.D2D_POINT_2F_head), use_last_error=False)(42, 'ComputeGlyphOrigins', ((1, 'glyphRun'),(1, 'measuringMode'),(1, 'baselineOrigin'),(1, 'worldAndDpiTransform'),(1, 'glyphOrigins'),)))
    return IDWriteFactory4
def _define_IDWriteFontSetBuilder1_head():
    class IDWriteFontSetBuilder1(win32more.Graphics.DirectWrite.IDWriteFontSetBuilder_head):
        Guid = Guid('3ff7715f-3cdc-4dc6-9b72-ec5621dccafd')
    return IDWriteFontSetBuilder1
def _define_IDWriteFontSetBuilder1():
    IDWriteFontSetBuilder1 = win32more.Graphics.DirectWrite.IDWriteFontSetBuilder1_head
    IDWriteFontSetBuilder1.AddFontFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFontFile_head, use_last_error=False)(7, 'AddFontFile', ((1, 'fontFile'),)))
    return IDWriteFontSetBuilder1
def _define_IDWriteAsyncResult_head():
    class IDWriteAsyncResult(win32more.System.Com.IUnknown_head):
        Guid = Guid('ce25f8fd-863b-4d13-9651-c1f88dc73fe2')
    return IDWriteAsyncResult
def _define_IDWriteAsyncResult():
    IDWriteAsyncResult = win32more.Graphics.DirectWrite.IDWriteAsyncResult_head
    IDWriteAsyncResult.GetWaitHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HANDLE, use_last_error=False)(3, 'GetWaitHandle', ()))
    IDWriteAsyncResult.GetResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'GetResult', ()))
    return IDWriteAsyncResult
def _define_DWRITE_FILE_FRAGMENT_head():
    class DWRITE_FILE_FRAGMENT(Structure):
        pass
    return DWRITE_FILE_FRAGMENT
def _define_DWRITE_FILE_FRAGMENT():
    DWRITE_FILE_FRAGMENT = win32more.Graphics.DirectWrite.DWRITE_FILE_FRAGMENT_head
    DWRITE_FILE_FRAGMENT._fields_ = [
        ("fileOffset", UInt64),
        ("fragmentSize", UInt64),
    ]
    return DWRITE_FILE_FRAGMENT
def _define_IDWriteRemoteFontFileStream_head():
    class IDWriteRemoteFontFileStream(win32more.Graphics.DirectWrite.IDWriteFontFileStream_head):
        Guid = Guid('4db3757a-2c72-4ed9-b2b6-1ababe1aff9c')
    return IDWriteRemoteFontFileStream
def _define_IDWriteRemoteFontFileStream():
    IDWriteRemoteFontFileStream = win32more.Graphics.DirectWrite.IDWriteRemoteFontFileStream_head
    IDWriteRemoteFontFileStream.GetLocalFileSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt64), use_last_error=False)(7, 'GetLocalFileSize', ((1, 'localFileSize'),)))
    IDWriteRemoteFontFileStream.GetFileFragmentLocality = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,UInt64,POINTER(win32more.Foundation.BOOL),POINTER(UInt64), use_last_error=False)(8, 'GetFileFragmentLocality', ((1, 'fileOffset'),(1, 'fragmentSize'),(1, 'isLocal'),(1, 'partialSize'),)))
    IDWriteRemoteFontFileStream.GetLocality = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_LOCALITY, use_last_error=False)(9, 'GetLocality', ()))
    IDWriteRemoteFontFileStream.BeginDownload = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Graphics.DirectWrite.DWRITE_FILE_FRAGMENT),UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteAsyncResult_head), use_last_error=False)(10, 'BeginDownload', ((1, 'downloadOperationID'),(1, 'fileFragments'),(1, 'fragmentCount'),(1, 'asyncResult'),)))
    return IDWriteRemoteFontFileStream
DWRITE_CONTAINER_TYPE = Int32
DWRITE_CONTAINER_TYPE_UNKNOWN = 0
DWRITE_CONTAINER_TYPE_WOFF = 1
DWRITE_CONTAINER_TYPE_WOFF2 = 2
def _define_IDWriteRemoteFontFileLoader_head():
    class IDWriteRemoteFontFileLoader(win32more.Graphics.DirectWrite.IDWriteFontFileLoader_head):
        Guid = Guid('68648c83-6ede-46c0-ab46-20083a887fde')
    return IDWriteRemoteFontFileLoader
def _define_IDWriteRemoteFontFileLoader():
    IDWriteRemoteFontFileLoader = win32more.Graphics.DirectWrite.IDWriteRemoteFontFileLoader_head
    IDWriteRemoteFontFileLoader.CreateRemoteStreamFromKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteRemoteFontFileStream_head), use_last_error=False)(4, 'CreateRemoteStreamFromKey', ((1, 'fontFileReferenceKey'),(1, 'fontFileReferenceKeySize'),(1, 'fontFileStream'),)))
    IDWriteRemoteFontFileLoader.GetLocalityFromKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(win32more.Graphics.DirectWrite.DWRITE_LOCALITY), use_last_error=False)(5, 'GetLocalityFromKey', ((1, 'fontFileReferenceKey'),(1, 'fontFileReferenceKeySize'),(1, 'locality'),)))
    IDWriteRemoteFontFileLoader.CreateFontFileReferenceFromUrl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFactory_head,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFile_head), use_last_error=False)(6, 'CreateFontFileReferenceFromUrl', ((1, 'factory'),(1, 'baseUrl'),(1, 'fontFileUrl'),(1, 'fontFile'),)))
    return IDWriteRemoteFontFileLoader
def _define_IDWriteInMemoryFontFileLoader_head():
    class IDWriteInMemoryFontFileLoader(win32more.Graphics.DirectWrite.IDWriteFontFileLoader_head):
        Guid = Guid('dc102f47-a12d-4b1c-822d-9e117e33043f')
    return IDWriteInMemoryFontFileLoader
def _define_IDWriteInMemoryFontFileLoader():
    IDWriteInMemoryFontFileLoader = win32more.Graphics.DirectWrite.IDWriteInMemoryFontFileLoader_head
    IDWriteInMemoryFontFileLoader.CreateInMemoryFontFileReference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFactory_head,c_void_p,UInt32,win32more.System.Com.IUnknown_head,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFile_head), use_last_error=False)(4, 'CreateInMemoryFontFileReference', ((1, 'factory'),(1, 'fontData'),(1, 'fontDataSize'),(1, 'ownerObject'),(1, 'fontFile'),)))
    IDWriteInMemoryFontFileLoader.GetFileCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(5, 'GetFileCount', ()))
    return IDWriteInMemoryFontFileLoader
def _define_IDWriteFactory5_head():
    class IDWriteFactory5(win32more.Graphics.DirectWrite.IDWriteFactory4_head):
        Guid = Guid('958db99a-be2a-4f09-af7d-65189803d1d3')
    return IDWriteFactory5
def _define_IDWriteFactory5():
    IDWriteFactory5 = win32more.Graphics.DirectWrite.IDWriteFactory5_head
    IDWriteFactory5.CreateFontSetBuilder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontSetBuilder1_head), use_last_error=False)(43, 'CreateFontSetBuilder', ((1, 'fontSetBuilder'),)))
    IDWriteFactory5.CreateInMemoryFontFileLoader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteInMemoryFontFileLoader_head), use_last_error=False)(44, 'CreateInMemoryFontFileLoader', ((1, 'newLoader'),)))
    IDWriteFactory5.CreateHttpFontFileLoader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Graphics.DirectWrite.IDWriteRemoteFontFileLoader_head), use_last_error=False)(45, 'CreateHttpFontFileLoader', ((1, 'referrerUrl'),(1, 'extraHeaders'),(1, 'newLoader'),)))
    IDWriteFactory5.AnalyzeContainerType = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_CONTAINER_TYPE,c_void_p,UInt32, use_last_error=False)(46, 'AnalyzeContainerType', ((1, 'fileData'),(1, 'fileDataSize'),)))
    IDWriteFactory5.UnpackFontFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_CONTAINER_TYPE,c_void_p,UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFileStream_head), use_last_error=False)(47, 'UnpackFontFile', ((1, 'containerType'),(1, 'fileData'),(1, 'fileDataSize'),(1, 'unpackedFontStream'),)))
    return IDWriteFactory5
def _define_DWRITE_FONT_AXIS_VALUE_head():
    class DWRITE_FONT_AXIS_VALUE(Structure):
        pass
    return DWRITE_FONT_AXIS_VALUE
def _define_DWRITE_FONT_AXIS_VALUE():
    DWRITE_FONT_AXIS_VALUE = win32more.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE_head
    DWRITE_FONT_AXIS_VALUE._fields_ = [
        ("axisTag", win32more.Graphics.DirectWrite.DWRITE_FONT_AXIS_TAG),
        ("value", Single),
    ]
    return DWRITE_FONT_AXIS_VALUE
def _define_DWRITE_FONT_AXIS_RANGE_head():
    class DWRITE_FONT_AXIS_RANGE(Structure):
        pass
    return DWRITE_FONT_AXIS_RANGE
def _define_DWRITE_FONT_AXIS_RANGE():
    DWRITE_FONT_AXIS_RANGE = win32more.Graphics.DirectWrite.DWRITE_FONT_AXIS_RANGE_head
    DWRITE_FONT_AXIS_RANGE._fields_ = [
        ("axisTag", win32more.Graphics.DirectWrite.DWRITE_FONT_AXIS_TAG),
        ("minValue", Single),
        ("maxValue", Single),
    ]
    return DWRITE_FONT_AXIS_RANGE
DWRITE_FONT_FAMILY_MODEL = Int32
DWRITE_FONT_FAMILY_MODEL_TYPOGRAPHIC = 0
DWRITE_FONT_FAMILY_MODEL_WEIGHT_STRETCH_STYLE = 1
DWRITE_AUTOMATIC_FONT_AXES = UInt32
DWRITE_AUTOMATIC_FONT_AXES_NONE = 0
DWRITE_AUTOMATIC_FONT_AXES_OPTICAL_SIZE = 1
DWRITE_FONT_AXIS_ATTRIBUTES = UInt32
DWRITE_FONT_AXIS_ATTRIBUTES_NONE = 0
DWRITE_FONT_AXIS_ATTRIBUTES_VARIABLE = 1
DWRITE_FONT_AXIS_ATTRIBUTES_HIDDEN = 2
def _define_IDWriteFactory6_head():
    class IDWriteFactory6(win32more.Graphics.DirectWrite.IDWriteFactory5_head):
        Guid = Guid('f3744d80-21f7-42eb-b35d-995bc72fc223')
    return IDWriteFactory6
def _define_IDWriteFactory6():
    IDWriteFactory6 = win32more.Graphics.DirectWrite.IDWriteFactory6_head
    IDWriteFactory6.CreateFontFaceReference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFontFile_head,UInt32,win32more.Graphics.DirectWrite.DWRITE_FONT_SIMULATIONS,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE),UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFaceReference1_head), use_last_error=False)(48, 'CreateFontFaceReference', ((1, 'fontFile'),(1, 'faceIndex'),(1, 'fontSimulations'),(1, 'fontAxisValues'),(1, 'fontAxisValueCount'),(1, 'fontFaceReference'),)))
    IDWriteFactory6.CreateFontResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFontFile_head,UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteFontResource_head), use_last_error=False)(49, 'CreateFontResource', ((1, 'fontFile'),(1, 'faceIndex'),(1, 'fontResource'),)))
    IDWriteFactory6.GetSystemFontSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,POINTER(win32more.Graphics.DirectWrite.IDWriteFontSet1_head), use_last_error=False)(50, 'GetSystemFontSet', ((1, 'includeDownloadableFonts'),(1, 'fontSet'),)))
    IDWriteFactory6.GetSystemFontCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.Graphics.DirectWrite.DWRITE_FONT_FAMILY_MODEL,POINTER(win32more.Graphics.DirectWrite.IDWriteFontCollection2_head), use_last_error=False)(51, 'GetSystemFontCollection', ((1, 'includeDownloadableFonts'),(1, 'fontFamilyModel'),(1, 'fontCollection'),)))
    IDWriteFactory6.CreateFontCollectionFromFontSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFontSet_head,win32more.Graphics.DirectWrite.DWRITE_FONT_FAMILY_MODEL,POINTER(win32more.Graphics.DirectWrite.IDWriteFontCollection2_head), use_last_error=False)(52, 'CreateFontCollectionFromFontSet', ((1, 'fontSet'),(1, 'fontFamilyModel'),(1, 'fontCollection'),)))
    IDWriteFactory6.CreateFontSetBuilder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontSetBuilder2_head), use_last_error=False)(53, 'CreateFontSetBuilder', ((1, 'fontSetBuilder'),)))
    IDWriteFactory6.CreateTextFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Graphics.DirectWrite.IDWriteFontCollection_head,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE),UInt32,Single,win32more.Foundation.PWSTR,POINTER(win32more.Graphics.DirectWrite.IDWriteTextFormat3_head), use_last_error=False)(54, 'CreateTextFormat', ((1, 'fontFamilyName'),(1, 'fontCollection'),(1, 'fontAxisValues'),(1, 'fontAxisValueCount'),(1, 'fontSize'),(1, 'localeName'),(1, 'textFormat'),)))
    return IDWriteFactory6
def _define_IDWriteFontFace5_head():
    class IDWriteFontFace5(win32more.Graphics.DirectWrite.IDWriteFontFace4_head):
        Guid = Guid('98eff3a5-b667-479a-b145-e2fa5b9fdc29')
    return IDWriteFontFace5
def _define_IDWriteFontFace5():
    IDWriteFontFace5 = win32more.Graphics.DirectWrite.IDWriteFontFace5_head
    IDWriteFontFace5.GetFontAxisValueCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(53, 'GetFontAxisValueCount', ()))
    IDWriteFontFace5.GetFontAxisValues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE),UInt32, use_last_error=False)(54, 'GetFontAxisValues', ((1, 'fontAxisValues'),(1, 'fontAxisValueCount'),)))
    IDWriteFontFace5.HasVariations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(55, 'HasVariations', ()))
    IDWriteFontFace5.GetFontResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontResource_head), use_last_error=False)(56, 'GetFontResource', ((1, 'fontResource'),)))
    IDWriteFontFace5.Equals = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.DirectWrite.IDWriteFontFace_head, use_last_error=False)(57, 'Equals', ((1, 'fontFace'),)))
    return IDWriteFontFace5
def _define_IDWriteFontResource_head():
    class IDWriteFontResource(win32more.System.Com.IUnknown_head):
        Guid = Guid('1f803a76-6871-48e8-987f-b975551c50f2')
    return IDWriteFontResource
def _define_IDWriteFontResource():
    IDWriteFontResource = win32more.Graphics.DirectWrite.IDWriteFontResource_head
    IDWriteFontResource.GetFontFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFile_head), use_last_error=False)(3, 'GetFontFile', ((1, 'fontFile'),)))
    IDWriteFontResource.GetFontFaceIndex = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(4, 'GetFontFaceIndex', ()))
    IDWriteFontResource.GetFontAxisCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(5, 'GetFontAxisCount', ()))
    IDWriteFontResource.GetDefaultFontAxisValues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE),UInt32, use_last_error=False)(6, 'GetDefaultFontAxisValues', ((1, 'fontAxisValues'),(1, 'fontAxisValueCount'),)))
    IDWriteFontResource.GetFontAxisRanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_AXIS_RANGE),UInt32, use_last_error=False)(7, 'GetFontAxisRanges', ((1, 'fontAxisRanges'),(1, 'fontAxisRangeCount'),)))
    IDWriteFontResource.GetFontAxisAttributes = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_FONT_AXIS_ATTRIBUTES,UInt32, use_last_error=False)(8, 'GetFontAxisAttributes', ((1, 'axisIndex'),)))
    IDWriteFontResource.GetAxisNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteLocalizedStrings_head), use_last_error=False)(9, 'GetAxisNames', ((1, 'axisIndex'),(1, 'names'),)))
    IDWriteFontResource.GetAxisValueNameCount = COMMETHOD(WINFUNCTYPE(UInt32,UInt32, use_last_error=False)(10, 'GetAxisValueNameCount', ((1, 'axisIndex'),)))
    IDWriteFontResource.GetAxisValueNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_AXIS_RANGE_head),POINTER(win32more.Graphics.DirectWrite.IDWriteLocalizedStrings_head), use_last_error=False)(11, 'GetAxisValueNames', ((1, 'axisIndex'),(1, 'axisValueIndex'),(1, 'fontAxisRange'),(1, 'names'),)))
    IDWriteFontResource.HasVariations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(12, 'HasVariations', ()))
    IDWriteFontResource.CreateFontFace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_FONT_SIMULATIONS,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE),UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFace5_head), use_last_error=False)(13, 'CreateFontFace', ((1, 'fontSimulations'),(1, 'fontAxisValues'),(1, 'fontAxisValueCount'),(1, 'fontFace'),)))
    IDWriteFontResource.CreateFontFaceReference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_FONT_SIMULATIONS,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE),UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFaceReference1_head), use_last_error=False)(14, 'CreateFontFaceReference', ((1, 'fontSimulations'),(1, 'fontAxisValues'),(1, 'fontAxisValueCount'),(1, 'fontFaceReference'),)))
    return IDWriteFontResource
def _define_IDWriteFontFaceReference1_head():
    class IDWriteFontFaceReference1(win32more.Graphics.DirectWrite.IDWriteFontFaceReference_head):
        Guid = Guid('c081fe77-2fd1-41ac-a5a3-34983c4ba61a')
    return IDWriteFontFaceReference1
def _define_IDWriteFontFaceReference1():
    IDWriteFontFaceReference1 = win32more.Graphics.DirectWrite.IDWriteFontFaceReference1_head
    IDWriteFontFaceReference1.CreateFontFace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFace5_head), use_last_error=False)(17, 'CreateFontFace', ((1, 'fontFace'),)))
    IDWriteFontFaceReference1.GetFontAxisValueCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(18, 'GetFontAxisValueCount', ()))
    IDWriteFontFaceReference1.GetFontAxisValues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE),UInt32, use_last_error=False)(19, 'GetFontAxisValues', ((1, 'fontAxisValues'),(1, 'fontAxisValueCount'),)))
    return IDWriteFontFaceReference1
def _define_IDWriteFontSetBuilder2_head():
    class IDWriteFontSetBuilder2(win32more.Graphics.DirectWrite.IDWriteFontSetBuilder1_head):
        Guid = Guid('ee5ba612-b131-463c-8f4f-3189b9401e45')
    return IDWriteFontSetBuilder2
def _define_IDWriteFontSetBuilder2():
    IDWriteFontSetBuilder2 = win32more.Graphics.DirectWrite.IDWriteFontSetBuilder2_head
    IDWriteFontSetBuilder2.AddFont = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteFontFile_head,UInt32,win32more.Graphics.DirectWrite.DWRITE_FONT_SIMULATIONS,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE),UInt32,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_AXIS_RANGE),UInt32,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_PROPERTY),UInt32, use_last_error=False)(8, 'AddFont', ((1, 'fontFile'),(1, 'fontFaceIndex'),(1, 'fontSimulations'),(1, 'fontAxisValues'),(1, 'fontAxisValueCount'),(1, 'fontAxisRanges'),(1, 'fontAxisRangeCount'),(1, 'properties'),(1, 'propertyCount'),)))
    IDWriteFontSetBuilder2.AddFontFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(9, 'AddFontFile', ((1, 'filePath'),)))
    return IDWriteFontSetBuilder2
def _define_IDWriteFontSet1_head():
    class IDWriteFontSet1(win32more.Graphics.DirectWrite.IDWriteFontSet_head):
        Guid = Guid('7e9fda85-6c92-4053-bc47-7ae3530db4d3')
    return IDWriteFontSet1
def _define_IDWriteFontSet1():
    IDWriteFontSet1 = win32more.Graphics.DirectWrite.IDWriteFontSet1_head
    IDWriteFontSet1.GetMatchingFonts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_PROPERTY_head),POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE),UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteFontSet1_head), use_last_error=False)(13, 'GetMatchingFonts', ((1, 'fontProperty'),(1, 'fontAxisValues'),(1, 'fontAxisValueCount'),(1, 'matchingFonts'),)))
    IDWriteFontSet1.GetFirstFontResources = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontSet1_head), use_last_error=False)(14, 'GetFirstFontResources', ((1, 'filteredFontSet'),)))
    IDWriteFontSet1.GetFilteredFonts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteFontSet1_head), use_last_error=False)(15, 'GetFilteredFonts', ((1, 'indices'),(1, 'indexCount'),(1, 'filteredFontSet'),)))
    IDWriteFontSet1.GetFilteredFonts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_AXIS_RANGE),UInt32,win32more.Foundation.BOOL,POINTER(win32more.Graphics.DirectWrite.IDWriteFontSet1_head), use_last_error=False)(16, 'GetFilteredFonts', ((1, 'fontAxisRanges'),(1, 'fontAxisRangeCount'),(1, 'selectAnyRange'),(1, 'filteredFontSet'),)))
    IDWriteFontSet1.GetFilteredFonts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_PROPERTY),UInt32,win32more.Foundation.BOOL,POINTER(win32more.Graphics.DirectWrite.IDWriteFontSet1_head), use_last_error=False)(17, 'GetFilteredFonts', ((1, 'properties'),(1, 'propertyCount'),(1, 'selectAnyProperty'),(1, 'filteredFontSet'),)))
    IDWriteFontSet1.GetFilteredFontIndices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_AXIS_RANGE),UInt32,win32more.Foundation.BOOL,POINTER(UInt32),UInt32,POINTER(UInt32), use_last_error=False)(18, 'GetFilteredFontIndices', ((1, 'fontAxisRanges'),(1, 'fontAxisRangeCount'),(1, 'selectAnyRange'),(1, 'indices'),(1, 'maxIndexCount'),(1, 'actualIndexCount'),)))
    IDWriteFontSet1.GetFilteredFontIndices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_PROPERTY),UInt32,win32more.Foundation.BOOL,POINTER(UInt32),UInt32,POINTER(UInt32), use_last_error=False)(19, 'GetFilteredFontIndices', ((1, 'properties'),(1, 'propertyCount'),(1, 'selectAnyProperty'),(1, 'indices'),(1, 'maxIndexCount'),(1, 'actualIndexCount'),)))
    IDWriteFontSet1.GetFontAxisRanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_AXIS_RANGE),UInt32,POINTER(UInt32), use_last_error=False)(20, 'GetFontAxisRanges', ((1, 'listIndex'),(1, 'fontAxisRanges'),(1, 'maxFontAxisRangeCount'),(1, 'actualFontAxisRangeCount'),)))
    IDWriteFontSet1.GetFontAxisRanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_AXIS_RANGE),UInt32,POINTER(UInt32), use_last_error=False)(21, 'GetFontAxisRanges', ((1, 'fontAxisRanges'),(1, 'maxFontAxisRangeCount'),(1, 'actualFontAxisRangeCount'),)))
    IDWriteFontSet1.GetFontFaceReference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFaceReference1_head), use_last_error=False)(22, 'GetFontFaceReference', ((1, 'listIndex'),(1, 'fontFaceReference'),)))
    IDWriteFontSet1.CreateFontResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteFontResource_head), use_last_error=False)(23, 'CreateFontResource', ((1, 'listIndex'),(1, 'fontResource'),)))
    IDWriteFontSet1.CreateFontFace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFace5_head), use_last_error=False)(24, 'CreateFontFace', ((1, 'listIndex'),(1, 'fontFace'),)))
    IDWriteFontSet1.GetFontLocality = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_LOCALITY,UInt32, use_last_error=False)(25, 'GetFontLocality', ((1, 'listIndex'),)))
    return IDWriteFontSet1
def _define_IDWriteFontList2_head():
    class IDWriteFontList2(win32more.Graphics.DirectWrite.IDWriteFontList1_head):
        Guid = Guid('c0763a34-77af-445a-b735-08c37b0a5bf5')
    return IDWriteFontList2
def _define_IDWriteFontList2():
    IDWriteFontList2 = win32more.Graphics.DirectWrite.IDWriteFontList2_head
    IDWriteFontList2.GetFontSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontSet1_head), use_last_error=False)(9, 'GetFontSet', ((1, 'fontSet'),)))
    return IDWriteFontList2
def _define_IDWriteFontFamily2_head():
    class IDWriteFontFamily2(win32more.Graphics.DirectWrite.IDWriteFontFamily1_head):
        Guid = Guid('3ed49e77-a398-4261-b9cf-c126c2131ef3')
    return IDWriteFontFamily2
def _define_IDWriteFontFamily2():
    IDWriteFontFamily2 = win32more.Graphics.DirectWrite.IDWriteFontFamily2_head
    IDWriteFontFamily2.GetMatchingFonts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE),UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteFontList2_head), use_last_error=False)(12, 'GetMatchingFonts', ((1, 'fontAxisValues'),(1, 'fontAxisValueCount'),(1, 'matchingFonts'),)))
    IDWriteFontFamily2.GetFontSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontSet1_head), use_last_error=False)(13, 'GetFontSet', ((1, 'fontSet'),)))
    return IDWriteFontFamily2
def _define_IDWriteFontCollection2_head():
    class IDWriteFontCollection2(win32more.Graphics.DirectWrite.IDWriteFontCollection1_head):
        Guid = Guid('514039c6-4617-4064-bf8b-92ea83e506e0')
    return IDWriteFontCollection2
def _define_IDWriteFontCollection2():
    IDWriteFontCollection2 = win32more.Graphics.DirectWrite.IDWriteFontCollection2_head
    IDWriteFontCollection2.GetFontFamily = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteFontFamily2_head), use_last_error=False)(9, 'GetFontFamily', ((1, 'index'),(1, 'fontFamily'),)))
    IDWriteFontCollection2.GetMatchingFonts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE),UInt32,POINTER(win32more.Graphics.DirectWrite.IDWriteFontList2_head), use_last_error=False)(10, 'GetMatchingFonts', ((1, 'familyName'),(1, 'fontAxisValues'),(1, 'fontAxisValueCount'),(1, 'fontList'),)))
    IDWriteFontCollection2.GetFontFamilyModel = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_FONT_FAMILY_MODEL, use_last_error=False)(11, 'GetFontFamilyModel', ()))
    IDWriteFontCollection2.GetFontSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.IDWriteFontSet1_head), use_last_error=False)(12, 'GetFontSet', ((1, 'fontSet'),)))
    return IDWriteFontCollection2
def _define_IDWriteTextLayout4_head():
    class IDWriteTextLayout4(win32more.Graphics.DirectWrite.IDWriteTextLayout3_head):
        Guid = Guid('05a9bf42-223f-4441-b5fb-8263685f55e9')
    return IDWriteTextLayout4
def _define_IDWriteTextLayout4():
    IDWriteTextLayout4 = win32more.Graphics.DirectWrite.IDWriteTextLayout4_head
    IDWriteTextLayout4.SetFontAxisValues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE),UInt32,win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE, use_last_error=False)(84, 'SetFontAxisValues', ((1, 'fontAxisValues'),(1, 'fontAxisValueCount'),(1, 'textRange'),)))
    IDWriteTextLayout4.GetFontAxisValueCount = COMMETHOD(WINFUNCTYPE(UInt32,UInt32, use_last_error=False)(85, 'GetFontAxisValueCount', ((1, 'currentPosition'),)))
    IDWriteTextLayout4.GetFontAxisValues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE),UInt32,POINTER(win32more.Graphics.DirectWrite.DWRITE_TEXT_RANGE_head), use_last_error=False)(86, 'GetFontAxisValues', ((1, 'currentPosition'),(1, 'fontAxisValues'),(1, 'fontAxisValueCount'),(1, 'textRange'),)))
    IDWriteTextLayout4.GetAutomaticFontAxes = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_AUTOMATIC_FONT_AXES, use_last_error=False)(87, 'GetAutomaticFontAxes', ()))
    IDWriteTextLayout4.SetAutomaticFontAxes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_AUTOMATIC_FONT_AXES, use_last_error=False)(88, 'SetAutomaticFontAxes', ((1, 'automaticFontAxes'),)))
    return IDWriteTextLayout4
def _define_IDWriteTextFormat3_head():
    class IDWriteTextFormat3(win32more.Graphics.DirectWrite.IDWriteTextFormat2_head):
        Guid = Guid('6d3b5641-e550-430d-a85b-b7bf48a93427')
    return IDWriteTextFormat3
def _define_IDWriteTextFormat3():
    IDWriteTextFormat3 = win32more.Graphics.DirectWrite.IDWriteTextFormat3_head
    IDWriteTextFormat3.SetFontAxisValues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE),UInt32, use_last_error=False)(38, 'SetFontAxisValues', ((1, 'fontAxisValues'),(1, 'fontAxisValueCount'),)))
    IDWriteTextFormat3.GetFontAxisValueCount = COMMETHOD(WINFUNCTYPE(UInt32, use_last_error=False)(39, 'GetFontAxisValueCount', ()))
    IDWriteTextFormat3.GetFontAxisValues = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE),UInt32, use_last_error=False)(40, 'GetFontAxisValues', ((1, 'fontAxisValues'),(1, 'fontAxisValueCount'),)))
    IDWriteTextFormat3.GetAutomaticFontAxes = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_AUTOMATIC_FONT_AXES, use_last_error=False)(41, 'GetAutomaticFontAxes', ()))
    IDWriteTextFormat3.SetAutomaticFontAxes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_AUTOMATIC_FONT_AXES, use_last_error=False)(42, 'SetAutomaticFontAxes', ((1, 'automaticFontAxes'),)))
    return IDWriteTextFormat3
def _define_IDWriteFontFallback1_head():
    class IDWriteFontFallback1(win32more.Graphics.DirectWrite.IDWriteFontFallback_head):
        Guid = Guid('2397599d-dd0d-4681-bd6a-f4f31eaade77')
    return IDWriteFontFallback1
def _define_IDWriteFontFallback1():
    IDWriteFontFallback1 = win32more.Graphics.DirectWrite.IDWriteFontFallback1_head
    IDWriteFontFallback1.MapCharacters = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.IDWriteTextAnalysisSource_head,UInt32,UInt32,win32more.Graphics.DirectWrite.IDWriteFontCollection_head,win32more.Foundation.PWSTR,POINTER(win32more.Graphics.DirectWrite.DWRITE_FONT_AXIS_VALUE),UInt32,POINTER(UInt32),POINTER(Single),POINTER(win32more.Graphics.DirectWrite.IDWriteFontFace5_head), use_last_error=False)(4, 'MapCharacters', ((1, 'analysisSource'),(1, 'textPosition'),(1, 'textLength'),(1, 'baseFontCollection'),(1, 'baseFamilyName'),(1, 'fontAxisValues'),(1, 'fontAxisValueCount'),(1, 'mappedLength'),(1, 'scale'),(1, 'mappedFontFace'),)))
    return IDWriteFontFallback1
def _define_IDWriteFontSet2_head():
    class IDWriteFontSet2(win32more.Graphics.DirectWrite.IDWriteFontSet1_head):
        Guid = Guid('dc7ead19-e54c-43af-b2da-4e2b79ba3f7f')
    return IDWriteFontSet2
def _define_IDWriteFontSet2():
    IDWriteFontSet2 = win32more.Graphics.DirectWrite.IDWriteFontSet2_head
    IDWriteFontSet2.GetExpirationEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HANDLE, use_last_error=False)(26, 'GetExpirationEvent', ()))
    return IDWriteFontSet2
def _define_IDWriteFontCollection3_head():
    class IDWriteFontCollection3(win32more.Graphics.DirectWrite.IDWriteFontCollection2_head):
        Guid = Guid('a4d055a6-f9e3-4e25-93b7-9e309f3af8e9')
    return IDWriteFontCollection3
def _define_IDWriteFontCollection3():
    IDWriteFontCollection3 = win32more.Graphics.DirectWrite.IDWriteFontCollection3_head
    IDWriteFontCollection3.GetExpirationEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HANDLE, use_last_error=False)(13, 'GetExpirationEvent', ()))
    return IDWriteFontCollection3
def _define_IDWriteFactory7_head():
    class IDWriteFactory7(win32more.Graphics.DirectWrite.IDWriteFactory6_head):
        Guid = Guid('35d0e0b3-9076-4d2e-a016-a91b568a06b4')
    return IDWriteFactory7
def _define_IDWriteFactory7():
    IDWriteFactory7 = win32more.Graphics.DirectWrite.IDWriteFactory7_head
    IDWriteFactory7.GetSystemFontSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,POINTER(win32more.Graphics.DirectWrite.IDWriteFontSet2_head), use_last_error=False)(55, 'GetSystemFontSet', ((1, 'includeDownloadableFonts'),(1, 'fontSet'),)))
    IDWriteFactory7.GetSystemFontCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.Graphics.DirectWrite.DWRITE_FONT_FAMILY_MODEL,POINTER(win32more.Graphics.DirectWrite.IDWriteFontCollection3_head), use_last_error=False)(56, 'GetSystemFontCollection', ((1, 'includeDownloadableFonts'),(1, 'fontFamilyModel'),(1, 'fontCollection'),)))
    return IDWriteFactory7
DWRITE_FONT_SOURCE_TYPE = Int32
DWRITE_FONT_SOURCE_TYPE_UNKNOWN = 0
DWRITE_FONT_SOURCE_TYPE_PER_MACHINE = 1
DWRITE_FONT_SOURCE_TYPE_PER_USER = 2
DWRITE_FONT_SOURCE_TYPE_APPX_PACKAGE = 3
DWRITE_FONT_SOURCE_TYPE_REMOTE_FONT_PROVIDER = 4
def _define_IDWriteFontSet3_head():
    class IDWriteFontSet3(win32more.Graphics.DirectWrite.IDWriteFontSet2_head):
        Guid = Guid('7c073ef2-a7f4-4045-8c32-8ab8ae640f90')
    return IDWriteFontSet3
def _define_IDWriteFontSet3():
    IDWriteFontSet3 = win32more.Graphics.DirectWrite.IDWriteFontSet3_head
    IDWriteFontSet3.GetFontSourceType = COMMETHOD(WINFUNCTYPE(win32more.Graphics.DirectWrite.DWRITE_FONT_SOURCE_TYPE,UInt32, use_last_error=False)(27, 'GetFontSourceType', ((1, 'fontIndex'),)))
    IDWriteFontSet3.GetFontSourceNameLength = COMMETHOD(WINFUNCTYPE(UInt32,UInt32, use_last_error=False)(28, 'GetFontSourceNameLength', ((1, 'listIndex'),)))
    IDWriteFontSet3.GetFontSourceName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Char),UInt32, use_last_error=False)(29, 'GetFontSourceName', ((1, 'listIndex'),(1, 'stringBuffer'),(1, 'stringBufferSize'),)))
    return IDWriteFontSet3
def _define_IDWriteFontFace6_head():
    class IDWriteFontFace6(win32more.Graphics.DirectWrite.IDWriteFontFace5_head):
        Guid = Guid('c4b1fe1b-6e84-47d5-b54c-a597981b06ad')
    return IDWriteFontFace6
def _define_IDWriteFontFace6():
    IDWriteFontFace6 = win32more.Graphics.DirectWrite.IDWriteFontFace6_head
    IDWriteFontFace6.GetFamilyNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_FONT_FAMILY_MODEL,POINTER(win32more.Graphics.DirectWrite.IDWriteLocalizedStrings_head), use_last_error=False)(58, 'GetFamilyNames', ((1, 'fontFamilyModel'),(1, 'names'),)))
    IDWriteFontFace6.GetFaceNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_FONT_FAMILY_MODEL,POINTER(win32more.Graphics.DirectWrite.IDWriteLocalizedStrings_head), use_last_error=False)(59, 'GetFaceNames', ((1, 'fontFamilyModel'),(1, 'names'),)))
    return IDWriteFontFace6
def _define_DWriteCreateFactory():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.DirectWrite.DWRITE_FACTORY_TYPE,POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(("DWriteCreateFactory", windll["DWrite"]), ((1, 'factoryType'),(1, 'iid'),(1, 'factory'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "DWRITE_ALPHA_MAX",
    "FACILITY_DWRITE",
    "DWRITE_ERR_BASE",
    "DWRITE_E_REMOTEFONT",
    "DWRITE_E_DOWNLOADCANCELLED",
    "DWRITE_E_DOWNLOADFAILED",
    "DWRITE_E_TOOMANYDOWNLOADS",
    "DWRITE_FONT_AXIS_TAG",
    "DWRITE_FONT_AXIS_TAG_WEIGHT",
    "DWRITE_FONT_AXIS_TAG_WIDTH",
    "DWRITE_FONT_AXIS_TAG_SLANT",
    "DWRITE_FONT_AXIS_TAG_OPTICAL_SIZE",
    "DWRITE_FONT_AXIS_TAG_ITALIC",
    "DWRITE_COLOR_F",
    "DWRITE_MEASURING_MODE",
    "DWRITE_MEASURING_MODE_NATURAL",
    "DWRITE_MEASURING_MODE_GDI_CLASSIC",
    "DWRITE_MEASURING_MODE_GDI_NATURAL",
    "DWRITE_GLYPH_IMAGE_FORMATS",
    "DWRITE_GLYPH_IMAGE_FORMATS_NONE",
    "DWRITE_GLYPH_IMAGE_FORMATS_TRUETYPE",
    "DWRITE_GLYPH_IMAGE_FORMATS_CFF",
    "DWRITE_GLYPH_IMAGE_FORMATS_COLR",
    "DWRITE_GLYPH_IMAGE_FORMATS_SVG",
    "DWRITE_GLYPH_IMAGE_FORMATS_PNG",
    "DWRITE_GLYPH_IMAGE_FORMATS_JPEG",
    "DWRITE_GLYPH_IMAGE_FORMATS_TIFF",
    "DWRITE_GLYPH_IMAGE_FORMATS_PREMULTIPLIED_B8G8R8A8",
    "DWRITE_FONT_FILE_TYPE",
    "DWRITE_FONT_FILE_TYPE_UNKNOWN",
    "DWRITE_FONT_FILE_TYPE_CFF",
    "DWRITE_FONT_FILE_TYPE_TRUETYPE",
    "DWRITE_FONT_FILE_TYPE_OPENTYPE_COLLECTION",
    "DWRITE_FONT_FILE_TYPE_TYPE1_PFM",
    "DWRITE_FONT_FILE_TYPE_TYPE1_PFB",
    "DWRITE_FONT_FILE_TYPE_VECTOR",
    "DWRITE_FONT_FILE_TYPE_BITMAP",
    "DWRITE_FONT_FILE_TYPE_TRUETYPE_COLLECTION",
    "DWRITE_FONT_FACE_TYPE",
    "DWRITE_FONT_FACE_TYPE_CFF",
    "DWRITE_FONT_FACE_TYPE_TRUETYPE",
    "DWRITE_FONT_FACE_TYPE_OPENTYPE_COLLECTION",
    "DWRITE_FONT_FACE_TYPE_TYPE1",
    "DWRITE_FONT_FACE_TYPE_VECTOR",
    "DWRITE_FONT_FACE_TYPE_BITMAP",
    "DWRITE_FONT_FACE_TYPE_UNKNOWN",
    "DWRITE_FONT_FACE_TYPE_RAW_CFF",
    "DWRITE_FONT_FACE_TYPE_TRUETYPE_COLLECTION",
    "DWRITE_FONT_SIMULATIONS",
    "DWRITE_FONT_SIMULATIONS_NONE",
    "DWRITE_FONT_SIMULATIONS_BOLD",
    "DWRITE_FONT_SIMULATIONS_OBLIQUE",
    "DWRITE_FONT_WEIGHT",
    "DWRITE_FONT_WEIGHT_THIN",
    "DWRITE_FONT_WEIGHT_EXTRA_LIGHT",
    "DWRITE_FONT_WEIGHT_ULTRA_LIGHT",
    "DWRITE_FONT_WEIGHT_LIGHT",
    "DWRITE_FONT_WEIGHT_SEMI_LIGHT",
    "DWRITE_FONT_WEIGHT_NORMAL",
    "DWRITE_FONT_WEIGHT_REGULAR",
    "DWRITE_FONT_WEIGHT_MEDIUM",
    "DWRITE_FONT_WEIGHT_DEMI_BOLD",
    "DWRITE_FONT_WEIGHT_SEMI_BOLD",
    "DWRITE_FONT_WEIGHT_BOLD",
    "DWRITE_FONT_WEIGHT_EXTRA_BOLD",
    "DWRITE_FONT_WEIGHT_ULTRA_BOLD",
    "DWRITE_FONT_WEIGHT_BLACK",
    "DWRITE_FONT_WEIGHT_HEAVY",
    "DWRITE_FONT_WEIGHT_EXTRA_BLACK",
    "DWRITE_FONT_WEIGHT_ULTRA_BLACK",
    "DWRITE_FONT_STRETCH",
    "DWRITE_FONT_STRETCH_UNDEFINED",
    "DWRITE_FONT_STRETCH_ULTRA_CONDENSED",
    "DWRITE_FONT_STRETCH_EXTRA_CONDENSED",
    "DWRITE_FONT_STRETCH_CONDENSED",
    "DWRITE_FONT_STRETCH_SEMI_CONDENSED",
    "DWRITE_FONT_STRETCH_NORMAL",
    "DWRITE_FONT_STRETCH_MEDIUM",
    "DWRITE_FONT_STRETCH_SEMI_EXPANDED",
    "DWRITE_FONT_STRETCH_EXPANDED",
    "DWRITE_FONT_STRETCH_EXTRA_EXPANDED",
    "DWRITE_FONT_STRETCH_ULTRA_EXPANDED",
    "DWRITE_FONT_STYLE",
    "DWRITE_FONT_STYLE_NORMAL",
    "DWRITE_FONT_STYLE_OBLIQUE",
    "DWRITE_FONT_STYLE_ITALIC",
    "DWRITE_INFORMATIONAL_STRING_ID",
    "DWRITE_INFORMATIONAL_STRING_NONE",
    "DWRITE_INFORMATIONAL_STRING_COPYRIGHT_NOTICE",
    "DWRITE_INFORMATIONAL_STRING_VERSION_STRINGS",
    "DWRITE_INFORMATIONAL_STRING_TRADEMARK",
    "DWRITE_INFORMATIONAL_STRING_MANUFACTURER",
    "DWRITE_INFORMATIONAL_STRING_DESIGNER",
    "DWRITE_INFORMATIONAL_STRING_DESIGNER_URL",
    "DWRITE_INFORMATIONAL_STRING_DESCRIPTION",
    "DWRITE_INFORMATIONAL_STRING_FONT_VENDOR_URL",
    "DWRITE_INFORMATIONAL_STRING_LICENSE_DESCRIPTION",
    "DWRITE_INFORMATIONAL_STRING_LICENSE_INFO_URL",
    "DWRITE_INFORMATIONAL_STRING_WIN32_FAMILY_NAMES",
    "DWRITE_INFORMATIONAL_STRING_WIN32_SUBFAMILY_NAMES",
    "DWRITE_INFORMATIONAL_STRING_TYPOGRAPHIC_FAMILY_NAMES",
    "DWRITE_INFORMATIONAL_STRING_TYPOGRAPHIC_SUBFAMILY_NAMES",
    "DWRITE_INFORMATIONAL_STRING_SAMPLE_TEXT",
    "DWRITE_INFORMATIONAL_STRING_FULL_NAME",
    "DWRITE_INFORMATIONAL_STRING_POSTSCRIPT_NAME",
    "DWRITE_INFORMATIONAL_STRING_POSTSCRIPT_CID_NAME",
    "DWRITE_INFORMATIONAL_STRING_WEIGHT_STRETCH_STYLE_FAMILY_NAME",
    "DWRITE_INFORMATIONAL_STRING_DESIGN_SCRIPT_LANGUAGE_TAG",
    "DWRITE_INFORMATIONAL_STRING_SUPPORTED_SCRIPT_LANGUAGE_TAG",
    "DWRITE_INFORMATIONAL_STRING_PREFERRED_FAMILY_NAMES",
    "DWRITE_INFORMATIONAL_STRING_PREFERRED_SUBFAMILY_NAMES",
    "DWRITE_INFORMATIONAL_STRING_WWS_FAMILY_NAME",
    "DWRITE_FONT_METRICS",
    "DWRITE_GLYPH_METRICS",
    "DWRITE_GLYPH_OFFSET",
    "DWRITE_FACTORY_TYPE",
    "DWRITE_FACTORY_TYPE_SHARED",
    "DWRITE_FACTORY_TYPE_ISOLATED",
    "IDWriteFontFileLoader",
    "IDWriteLocalFontFileLoader",
    "IDWriteFontFileStream",
    "IDWriteFontFile",
    "DWRITE_PIXEL_GEOMETRY",
    "DWRITE_PIXEL_GEOMETRY_FLAT",
    "DWRITE_PIXEL_GEOMETRY_RGB",
    "DWRITE_PIXEL_GEOMETRY_BGR",
    "DWRITE_RENDERING_MODE",
    "DWRITE_RENDERING_MODE_DEFAULT",
    "DWRITE_RENDERING_MODE_ALIASED",
    "DWRITE_RENDERING_MODE_GDI_CLASSIC",
    "DWRITE_RENDERING_MODE_GDI_NATURAL",
    "DWRITE_RENDERING_MODE_NATURAL",
    "DWRITE_RENDERING_MODE_NATURAL_SYMMETRIC",
    "DWRITE_RENDERING_MODE_OUTLINE",
    "DWRITE_RENDERING_MODE_CLEARTYPE_GDI_CLASSIC",
    "DWRITE_RENDERING_MODE_CLEARTYPE_GDI_NATURAL",
    "DWRITE_RENDERING_MODE_CLEARTYPE_NATURAL",
    "DWRITE_RENDERING_MODE_CLEARTYPE_NATURAL_SYMMETRIC",
    "DWRITE_MATRIX",
    "IDWriteRenderingParams",
    "IDWriteFontFace",
    "IDWriteFontCollectionLoader",
    "IDWriteFontFileEnumerator",
    "IDWriteLocalizedStrings",
    "IDWriteFontCollection",
    "IDWriteFontList",
    "IDWriteFontFamily",
    "IDWriteFont",
    "DWRITE_READING_DIRECTION",
    "DWRITE_READING_DIRECTION_LEFT_TO_RIGHT",
    "DWRITE_READING_DIRECTION_RIGHT_TO_LEFT",
    "DWRITE_READING_DIRECTION_TOP_TO_BOTTOM",
    "DWRITE_READING_DIRECTION_BOTTOM_TO_TOP",
    "DWRITE_FLOW_DIRECTION",
    "DWRITE_FLOW_DIRECTION_TOP_TO_BOTTOM",
    "DWRITE_FLOW_DIRECTION_BOTTOM_TO_TOP",
    "DWRITE_FLOW_DIRECTION_LEFT_TO_RIGHT",
    "DWRITE_FLOW_DIRECTION_RIGHT_TO_LEFT",
    "DWRITE_TEXT_ALIGNMENT",
    "DWRITE_TEXT_ALIGNMENT_LEADING",
    "DWRITE_TEXT_ALIGNMENT_TRAILING",
    "DWRITE_TEXT_ALIGNMENT_CENTER",
    "DWRITE_TEXT_ALIGNMENT_JUSTIFIED",
    "DWRITE_PARAGRAPH_ALIGNMENT",
    "DWRITE_PARAGRAPH_ALIGNMENT_NEAR",
    "DWRITE_PARAGRAPH_ALIGNMENT_FAR",
    "DWRITE_PARAGRAPH_ALIGNMENT_CENTER",
    "DWRITE_WORD_WRAPPING",
    "DWRITE_WORD_WRAPPING_WRAP",
    "DWRITE_WORD_WRAPPING_NO_WRAP",
    "DWRITE_WORD_WRAPPING_EMERGENCY_BREAK",
    "DWRITE_WORD_WRAPPING_WHOLE_WORD",
    "DWRITE_WORD_WRAPPING_CHARACTER",
    "DWRITE_LINE_SPACING_METHOD",
    "DWRITE_LINE_SPACING_METHOD_DEFAULT",
    "DWRITE_LINE_SPACING_METHOD_UNIFORM",
    "DWRITE_LINE_SPACING_METHOD_PROPORTIONAL",
    "DWRITE_TRIMMING_GRANULARITY",
    "DWRITE_TRIMMING_GRANULARITY_NONE",
    "DWRITE_TRIMMING_GRANULARITY_CHARACTER",
    "DWRITE_TRIMMING_GRANULARITY_WORD",
    "DWRITE_FONT_FEATURE_TAG",
    "DWRITE_FONT_FEATURE_TAG_ALTERNATIVE_FRACTIONS",
    "DWRITE_FONT_FEATURE_TAG_PETITE_CAPITALS_FROM_CAPITALS",
    "DWRITE_FONT_FEATURE_TAG_SMALL_CAPITALS_FROM_CAPITALS",
    "DWRITE_FONT_FEATURE_TAG_CONTEXTUAL_ALTERNATES",
    "DWRITE_FONT_FEATURE_TAG_CASE_SENSITIVE_FORMS",
    "DWRITE_FONT_FEATURE_TAG_GLYPH_COMPOSITION_DECOMPOSITION",
    "DWRITE_FONT_FEATURE_TAG_CONTEXTUAL_LIGATURES",
    "DWRITE_FONT_FEATURE_TAG_CAPITAL_SPACING",
    "DWRITE_FONT_FEATURE_TAG_CONTEXTUAL_SWASH",
    "DWRITE_FONT_FEATURE_TAG_CURSIVE_POSITIONING",
    "DWRITE_FONT_FEATURE_TAG_DEFAULT",
    "DWRITE_FONT_FEATURE_TAG_DISCRETIONARY_LIGATURES",
    "DWRITE_FONT_FEATURE_TAG_EXPERT_FORMS",
    "DWRITE_FONT_FEATURE_TAG_FRACTIONS",
    "DWRITE_FONT_FEATURE_TAG_FULL_WIDTH",
    "DWRITE_FONT_FEATURE_TAG_HALF_FORMS",
    "DWRITE_FONT_FEATURE_TAG_HALANT_FORMS",
    "DWRITE_FONT_FEATURE_TAG_ALTERNATE_HALF_WIDTH",
    "DWRITE_FONT_FEATURE_TAG_HISTORICAL_FORMS",
    "DWRITE_FONT_FEATURE_TAG_HORIZONTAL_KANA_ALTERNATES",
    "DWRITE_FONT_FEATURE_TAG_HISTORICAL_LIGATURES",
    "DWRITE_FONT_FEATURE_TAG_HALF_WIDTH",
    "DWRITE_FONT_FEATURE_TAG_HOJO_KANJI_FORMS",
    "DWRITE_FONT_FEATURE_TAG_JIS04_FORMS",
    "DWRITE_FONT_FEATURE_TAG_JIS78_FORMS",
    "DWRITE_FONT_FEATURE_TAG_JIS83_FORMS",
    "DWRITE_FONT_FEATURE_TAG_JIS90_FORMS",
    "DWRITE_FONT_FEATURE_TAG_KERNING",
    "DWRITE_FONT_FEATURE_TAG_STANDARD_LIGATURES",
    "DWRITE_FONT_FEATURE_TAG_LINING_FIGURES",
    "DWRITE_FONT_FEATURE_TAG_LOCALIZED_FORMS",
    "DWRITE_FONT_FEATURE_TAG_MARK_POSITIONING",
    "DWRITE_FONT_FEATURE_TAG_MATHEMATICAL_GREEK",
    "DWRITE_FONT_FEATURE_TAG_MARK_TO_MARK_POSITIONING",
    "DWRITE_FONT_FEATURE_TAG_ALTERNATE_ANNOTATION_FORMS",
    "DWRITE_FONT_FEATURE_TAG_NLC_KANJI_FORMS",
    "DWRITE_FONT_FEATURE_TAG_OLD_STYLE_FIGURES",
    "DWRITE_FONT_FEATURE_TAG_ORDINALS",
    "DWRITE_FONT_FEATURE_TAG_PROPORTIONAL_ALTERNATE_WIDTH",
    "DWRITE_FONT_FEATURE_TAG_PETITE_CAPITALS",
    "DWRITE_FONT_FEATURE_TAG_PROPORTIONAL_FIGURES",
    "DWRITE_FONT_FEATURE_TAG_PROPORTIONAL_WIDTHS",
    "DWRITE_FONT_FEATURE_TAG_QUARTER_WIDTHS",
    "DWRITE_FONT_FEATURE_TAG_REQUIRED_LIGATURES",
    "DWRITE_FONT_FEATURE_TAG_RUBY_NOTATION_FORMS",
    "DWRITE_FONT_FEATURE_TAG_STYLISTIC_ALTERNATES",
    "DWRITE_FONT_FEATURE_TAG_SCIENTIFIC_INFERIORS",
    "DWRITE_FONT_FEATURE_TAG_SMALL_CAPITALS",
    "DWRITE_FONT_FEATURE_TAG_SIMPLIFIED_FORMS",
    "DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_1",
    "DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_2",
    "DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_3",
    "DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_4",
    "DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_5",
    "DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_6",
    "DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_7",
    "DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_8",
    "DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_9",
    "DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_10",
    "DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_11",
    "DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_12",
    "DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_13",
    "DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_14",
    "DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_15",
    "DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_16",
    "DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_17",
    "DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_18",
    "DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_19",
    "DWRITE_FONT_FEATURE_TAG_STYLISTIC_SET_20",
    "DWRITE_FONT_FEATURE_TAG_SUBSCRIPT",
    "DWRITE_FONT_FEATURE_TAG_SUPERSCRIPT",
    "DWRITE_FONT_FEATURE_TAG_SWASH",
    "DWRITE_FONT_FEATURE_TAG_TITLING",
    "DWRITE_FONT_FEATURE_TAG_TRADITIONAL_NAME_FORMS",
    "DWRITE_FONT_FEATURE_TAG_TABULAR_FIGURES",
    "DWRITE_FONT_FEATURE_TAG_TRADITIONAL_FORMS",
    "DWRITE_FONT_FEATURE_TAG_THIRD_WIDTHS",
    "DWRITE_FONT_FEATURE_TAG_UNICASE",
    "DWRITE_FONT_FEATURE_TAG_VERTICAL_WRITING",
    "DWRITE_FONT_FEATURE_TAG_VERTICAL_ALTERNATES_AND_ROTATION",
    "DWRITE_FONT_FEATURE_TAG_SLASHED_ZERO",
    "DWRITE_TEXT_RANGE",
    "DWRITE_FONT_FEATURE",
    "DWRITE_TYPOGRAPHIC_FEATURES",
    "DWRITE_TRIMMING",
    "IDWriteTextFormat",
    "IDWriteTypography",
    "DWRITE_SCRIPT_SHAPES",
    "DWRITE_SCRIPT_SHAPES_DEFAULT",
    "DWRITE_SCRIPT_SHAPES_NO_VISUAL",
    "DWRITE_SCRIPT_ANALYSIS",
    "DWRITE_BREAK_CONDITION",
    "DWRITE_BREAK_CONDITION_NEUTRAL",
    "DWRITE_BREAK_CONDITION_CAN_BREAK",
    "DWRITE_BREAK_CONDITION_MAY_NOT_BREAK",
    "DWRITE_BREAK_CONDITION_MUST_BREAK",
    "DWRITE_LINE_BREAKPOINT",
    "DWRITE_NUMBER_SUBSTITUTION_METHOD",
    "DWRITE_NUMBER_SUBSTITUTION_METHOD_FROM_CULTURE",
    "DWRITE_NUMBER_SUBSTITUTION_METHOD_CONTEXTUAL",
    "DWRITE_NUMBER_SUBSTITUTION_METHOD_NONE",
    "DWRITE_NUMBER_SUBSTITUTION_METHOD_NATIONAL",
    "DWRITE_NUMBER_SUBSTITUTION_METHOD_TRADITIONAL",
    "IDWriteNumberSubstitution",
    "DWRITE_SHAPING_TEXT_PROPERTIES",
    "DWRITE_SHAPING_GLYPH_PROPERTIES",
    "IDWriteTextAnalysisSource",
    "IDWriteTextAnalysisSink",
    "IDWriteTextAnalyzer",
    "DWRITE_GLYPH_RUN",
    "DWRITE_GLYPH_RUN_DESCRIPTION",
    "DWRITE_UNDERLINE",
    "DWRITE_STRIKETHROUGH",
    "DWRITE_LINE_METRICS",
    "DWRITE_CLUSTER_METRICS",
    "DWRITE_TEXT_METRICS",
    "DWRITE_INLINE_OBJECT_METRICS",
    "DWRITE_OVERHANG_METRICS",
    "DWRITE_HIT_TEST_METRICS",
    "IDWriteInlineObject",
    "IDWritePixelSnapping",
    "IDWriteTextRenderer",
    "IDWriteTextLayout",
    "IDWriteBitmapRenderTarget",
    "IDWriteGdiInterop",
    "DWRITE_TEXTURE_TYPE",
    "DWRITE_TEXTURE_ALIASED_1x1",
    "DWRITE_TEXTURE_CLEARTYPE_3x1",
    "IDWriteGlyphRunAnalysis",
    "IDWriteFactory",
    "DWRITE_PANOSE_FAMILY",
    "DWRITE_PANOSE_FAMILY_ANY",
    "DWRITE_PANOSE_FAMILY_NO_FIT",
    "DWRITE_PANOSE_FAMILY_TEXT_DISPLAY",
    "DWRITE_PANOSE_FAMILY_SCRIPT",
    "DWRITE_PANOSE_FAMILY_DECORATIVE",
    "DWRITE_PANOSE_FAMILY_SYMBOL",
    "DWRITE_PANOSE_FAMILY_PICTORIAL",
    "DWRITE_PANOSE_SERIF_STYLE",
    "DWRITE_PANOSE_SERIF_STYLE_ANY",
    "DWRITE_PANOSE_SERIF_STYLE_NO_FIT",
    "DWRITE_PANOSE_SERIF_STYLE_COVE",
    "DWRITE_PANOSE_SERIF_STYLE_OBTUSE_COVE",
    "DWRITE_PANOSE_SERIF_STYLE_SQUARE_COVE",
    "DWRITE_PANOSE_SERIF_STYLE_OBTUSE_SQUARE_COVE",
    "DWRITE_PANOSE_SERIF_STYLE_SQUARE",
    "DWRITE_PANOSE_SERIF_STYLE_THIN",
    "DWRITE_PANOSE_SERIF_STYLE_OVAL",
    "DWRITE_PANOSE_SERIF_STYLE_EXAGGERATED",
    "DWRITE_PANOSE_SERIF_STYLE_TRIANGLE",
    "DWRITE_PANOSE_SERIF_STYLE_NORMAL_SANS",
    "DWRITE_PANOSE_SERIF_STYLE_OBTUSE_SANS",
    "DWRITE_PANOSE_SERIF_STYLE_PERPENDICULAR_SANS",
    "DWRITE_PANOSE_SERIF_STYLE_FLARED",
    "DWRITE_PANOSE_SERIF_STYLE_ROUNDED",
    "DWRITE_PANOSE_SERIF_STYLE_SCRIPT",
    "DWRITE_PANOSE_SERIF_STYLE_PERP_SANS",
    "DWRITE_PANOSE_SERIF_STYLE_BONE",
    "DWRITE_PANOSE_WEIGHT",
    "DWRITE_PANOSE_WEIGHT_ANY",
    "DWRITE_PANOSE_WEIGHT_NO_FIT",
    "DWRITE_PANOSE_WEIGHT_VERY_LIGHT",
    "DWRITE_PANOSE_WEIGHT_LIGHT",
    "DWRITE_PANOSE_WEIGHT_THIN",
    "DWRITE_PANOSE_WEIGHT_BOOK",
    "DWRITE_PANOSE_WEIGHT_MEDIUM",
    "DWRITE_PANOSE_WEIGHT_DEMI",
    "DWRITE_PANOSE_WEIGHT_BOLD",
    "DWRITE_PANOSE_WEIGHT_HEAVY",
    "DWRITE_PANOSE_WEIGHT_BLACK",
    "DWRITE_PANOSE_WEIGHT_EXTRA_BLACK",
    "DWRITE_PANOSE_WEIGHT_NORD",
    "DWRITE_PANOSE_PROPORTION",
    "DWRITE_PANOSE_PROPORTION_ANY",
    "DWRITE_PANOSE_PROPORTION_NO_FIT",
    "DWRITE_PANOSE_PROPORTION_OLD_STYLE",
    "DWRITE_PANOSE_PROPORTION_MODERN",
    "DWRITE_PANOSE_PROPORTION_EVEN_WIDTH",
    "DWRITE_PANOSE_PROPORTION_EXPANDED",
    "DWRITE_PANOSE_PROPORTION_CONDENSED",
    "DWRITE_PANOSE_PROPORTION_VERY_EXPANDED",
    "DWRITE_PANOSE_PROPORTION_VERY_CONDENSED",
    "DWRITE_PANOSE_PROPORTION_MONOSPACED",
    "DWRITE_PANOSE_CONTRAST",
    "DWRITE_PANOSE_CONTRAST_ANY",
    "DWRITE_PANOSE_CONTRAST_NO_FIT",
    "DWRITE_PANOSE_CONTRAST_NONE",
    "DWRITE_PANOSE_CONTRAST_VERY_LOW",
    "DWRITE_PANOSE_CONTRAST_LOW",
    "DWRITE_PANOSE_CONTRAST_MEDIUM_LOW",
    "DWRITE_PANOSE_CONTRAST_MEDIUM",
    "DWRITE_PANOSE_CONTRAST_MEDIUM_HIGH",
    "DWRITE_PANOSE_CONTRAST_HIGH",
    "DWRITE_PANOSE_CONTRAST_VERY_HIGH",
    "DWRITE_PANOSE_CONTRAST_HORIZONTAL_LOW",
    "DWRITE_PANOSE_CONTRAST_HORIZONTAL_MEDIUM",
    "DWRITE_PANOSE_CONTRAST_HORIZONTAL_HIGH",
    "DWRITE_PANOSE_CONTRAST_BROKEN",
    "DWRITE_PANOSE_STROKE_VARIATION",
    "DWRITE_PANOSE_STROKE_VARIATION_ANY",
    "DWRITE_PANOSE_STROKE_VARIATION_NO_FIT",
    "DWRITE_PANOSE_STROKE_VARIATION_NO_VARIATION",
    "DWRITE_PANOSE_STROKE_VARIATION_GRADUAL_DIAGONAL",
    "DWRITE_PANOSE_STROKE_VARIATION_GRADUAL_TRANSITIONAL",
    "DWRITE_PANOSE_STROKE_VARIATION_GRADUAL_VERTICAL",
    "DWRITE_PANOSE_STROKE_VARIATION_GRADUAL_HORIZONTAL",
    "DWRITE_PANOSE_STROKE_VARIATION_RAPID_VERTICAL",
    "DWRITE_PANOSE_STROKE_VARIATION_RAPID_HORIZONTAL",
    "DWRITE_PANOSE_STROKE_VARIATION_INSTANT_VERTICAL",
    "DWRITE_PANOSE_STROKE_VARIATION_INSTANT_HORIZONTAL",
    "DWRITE_PANOSE_ARM_STYLE",
    "DWRITE_PANOSE_ARM_STYLE_ANY",
    "DWRITE_PANOSE_ARM_STYLE_NO_FIT",
    "DWRITE_PANOSE_ARM_STYLE_STRAIGHT_ARMS_HORIZONTAL",
    "DWRITE_PANOSE_ARM_STYLE_STRAIGHT_ARMS_WEDGE",
    "DWRITE_PANOSE_ARM_STYLE_STRAIGHT_ARMS_VERTICAL",
    "DWRITE_PANOSE_ARM_STYLE_STRAIGHT_ARMS_SINGLE_SERIF",
    "DWRITE_PANOSE_ARM_STYLE_STRAIGHT_ARMS_DOUBLE_SERIF",
    "DWRITE_PANOSE_ARM_STYLE_NONSTRAIGHT_ARMS_HORIZONTAL",
    "DWRITE_PANOSE_ARM_STYLE_NONSTRAIGHT_ARMS_WEDGE",
    "DWRITE_PANOSE_ARM_STYLE_NONSTRAIGHT_ARMS_VERTICAL",
    "DWRITE_PANOSE_ARM_STYLE_NONSTRAIGHT_ARMS_SINGLE_SERIF",
    "DWRITE_PANOSE_ARM_STYLE_NONSTRAIGHT_ARMS_DOUBLE_SERIF",
    "DWRITE_PANOSE_ARM_STYLE_STRAIGHT_ARMS_HORZ",
    "DWRITE_PANOSE_ARM_STYLE_STRAIGHT_ARMS_VERT",
    "DWRITE_PANOSE_ARM_STYLE_BENT_ARMS_HORZ",
    "DWRITE_PANOSE_ARM_STYLE_BENT_ARMS_WEDGE",
    "DWRITE_PANOSE_ARM_STYLE_BENT_ARMS_VERT",
    "DWRITE_PANOSE_ARM_STYLE_BENT_ARMS_SINGLE_SERIF",
    "DWRITE_PANOSE_ARM_STYLE_BENT_ARMS_DOUBLE_SERIF",
    "DWRITE_PANOSE_LETTERFORM",
    "DWRITE_PANOSE_LETTERFORM_ANY",
    "DWRITE_PANOSE_LETTERFORM_NO_FIT",
    "DWRITE_PANOSE_LETTERFORM_NORMAL_CONTACT",
    "DWRITE_PANOSE_LETTERFORM_NORMAL_WEIGHTED",
    "DWRITE_PANOSE_LETTERFORM_NORMAL_BOXED",
    "DWRITE_PANOSE_LETTERFORM_NORMAL_FLATTENED",
    "DWRITE_PANOSE_LETTERFORM_NORMAL_ROUNDED",
    "DWRITE_PANOSE_LETTERFORM_NORMAL_OFF_CENTER",
    "DWRITE_PANOSE_LETTERFORM_NORMAL_SQUARE",
    "DWRITE_PANOSE_LETTERFORM_OBLIQUE_CONTACT",
    "DWRITE_PANOSE_LETTERFORM_OBLIQUE_WEIGHTED",
    "DWRITE_PANOSE_LETTERFORM_OBLIQUE_BOXED",
    "DWRITE_PANOSE_LETTERFORM_OBLIQUE_FLATTENED",
    "DWRITE_PANOSE_LETTERFORM_OBLIQUE_ROUNDED",
    "DWRITE_PANOSE_LETTERFORM_OBLIQUE_OFF_CENTER",
    "DWRITE_PANOSE_LETTERFORM_OBLIQUE_SQUARE",
    "DWRITE_PANOSE_MIDLINE",
    "DWRITE_PANOSE_MIDLINE_ANY",
    "DWRITE_PANOSE_MIDLINE_NO_FIT",
    "DWRITE_PANOSE_MIDLINE_STANDARD_TRIMMED",
    "DWRITE_PANOSE_MIDLINE_STANDARD_POINTED",
    "DWRITE_PANOSE_MIDLINE_STANDARD_SERIFED",
    "DWRITE_PANOSE_MIDLINE_HIGH_TRIMMED",
    "DWRITE_PANOSE_MIDLINE_HIGH_POINTED",
    "DWRITE_PANOSE_MIDLINE_HIGH_SERIFED",
    "DWRITE_PANOSE_MIDLINE_CONSTANT_TRIMMED",
    "DWRITE_PANOSE_MIDLINE_CONSTANT_POINTED",
    "DWRITE_PANOSE_MIDLINE_CONSTANT_SERIFED",
    "DWRITE_PANOSE_MIDLINE_LOW_TRIMMED",
    "DWRITE_PANOSE_MIDLINE_LOW_POINTED",
    "DWRITE_PANOSE_MIDLINE_LOW_SERIFED",
    "DWRITE_PANOSE_XHEIGHT",
    "DWRITE_PANOSE_XHEIGHT_ANY",
    "DWRITE_PANOSE_XHEIGHT_NO_FIT",
    "DWRITE_PANOSE_XHEIGHT_CONSTANT_SMALL",
    "DWRITE_PANOSE_XHEIGHT_CONSTANT_STANDARD",
    "DWRITE_PANOSE_XHEIGHT_CONSTANT_LARGE",
    "DWRITE_PANOSE_XHEIGHT_DUCKING_SMALL",
    "DWRITE_PANOSE_XHEIGHT_DUCKING_STANDARD",
    "DWRITE_PANOSE_XHEIGHT_DUCKING_LARGE",
    "DWRITE_PANOSE_XHEIGHT_CONSTANT_STD",
    "DWRITE_PANOSE_XHEIGHT_DUCKING_STD",
    "DWRITE_PANOSE_TOOL_KIND",
    "DWRITE_PANOSE_TOOL_KIND_ANY",
    "DWRITE_PANOSE_TOOL_KIND_NO_FIT",
    "DWRITE_PANOSE_TOOL_KIND_FLAT_NIB",
    "DWRITE_PANOSE_TOOL_KIND_PRESSURE_POINT",
    "DWRITE_PANOSE_TOOL_KIND_ENGRAVED",
    "DWRITE_PANOSE_TOOL_KIND_BALL",
    "DWRITE_PANOSE_TOOL_KIND_BRUSH",
    "DWRITE_PANOSE_TOOL_KIND_ROUGH",
    "DWRITE_PANOSE_TOOL_KIND_FELT_PEN_BRUSH_TIP",
    "DWRITE_PANOSE_TOOL_KIND_WILD_BRUSH",
    "DWRITE_PANOSE_SPACING",
    "DWRITE_PANOSE_SPACING_ANY",
    "DWRITE_PANOSE_SPACING_NO_FIT",
    "DWRITE_PANOSE_SPACING_PROPORTIONAL_SPACED",
    "DWRITE_PANOSE_SPACING_MONOSPACED",
    "DWRITE_PANOSE_ASPECT_RATIO",
    "DWRITE_PANOSE_ASPECT_RATIO_ANY",
    "DWRITE_PANOSE_ASPECT_RATIO_NO_FIT",
    "DWRITE_PANOSE_ASPECT_RATIO_VERY_CONDENSED",
    "DWRITE_PANOSE_ASPECT_RATIO_CONDENSED",
    "DWRITE_PANOSE_ASPECT_RATIO_NORMAL",
    "DWRITE_PANOSE_ASPECT_RATIO_EXPANDED",
    "DWRITE_PANOSE_ASPECT_RATIO_VERY_EXPANDED",
    "DWRITE_PANOSE_SCRIPT_TOPOLOGY",
    "DWRITE_PANOSE_SCRIPT_TOPOLOGY_ANY",
    "DWRITE_PANOSE_SCRIPT_TOPOLOGY_NO_FIT",
    "DWRITE_PANOSE_SCRIPT_TOPOLOGY_ROMAN_DISCONNECTED",
    "DWRITE_PANOSE_SCRIPT_TOPOLOGY_ROMAN_TRAILING",
    "DWRITE_PANOSE_SCRIPT_TOPOLOGY_ROMAN_CONNECTED",
    "DWRITE_PANOSE_SCRIPT_TOPOLOGY_CURSIVE_DISCONNECTED",
    "DWRITE_PANOSE_SCRIPT_TOPOLOGY_CURSIVE_TRAILING",
    "DWRITE_PANOSE_SCRIPT_TOPOLOGY_CURSIVE_CONNECTED",
    "DWRITE_PANOSE_SCRIPT_TOPOLOGY_BLACKLETTER_DISCONNECTED",
    "DWRITE_PANOSE_SCRIPT_TOPOLOGY_BLACKLETTER_TRAILING",
    "DWRITE_PANOSE_SCRIPT_TOPOLOGY_BLACKLETTER_CONNECTED",
    "DWRITE_PANOSE_SCRIPT_FORM",
    "DWRITE_PANOSE_SCRIPT_FORM_ANY",
    "DWRITE_PANOSE_SCRIPT_FORM_NO_FIT",
    "DWRITE_PANOSE_SCRIPT_FORM_UPRIGHT_NO_WRAPPING",
    "DWRITE_PANOSE_SCRIPT_FORM_UPRIGHT_SOME_WRAPPING",
    "DWRITE_PANOSE_SCRIPT_FORM_UPRIGHT_MORE_WRAPPING",
    "DWRITE_PANOSE_SCRIPT_FORM_UPRIGHT_EXTREME_WRAPPING",
    "DWRITE_PANOSE_SCRIPT_FORM_OBLIQUE_NO_WRAPPING",
    "DWRITE_PANOSE_SCRIPT_FORM_OBLIQUE_SOME_WRAPPING",
    "DWRITE_PANOSE_SCRIPT_FORM_OBLIQUE_MORE_WRAPPING",
    "DWRITE_PANOSE_SCRIPT_FORM_OBLIQUE_EXTREME_WRAPPING",
    "DWRITE_PANOSE_SCRIPT_FORM_EXAGGERATED_NO_WRAPPING",
    "DWRITE_PANOSE_SCRIPT_FORM_EXAGGERATED_SOME_WRAPPING",
    "DWRITE_PANOSE_SCRIPT_FORM_EXAGGERATED_MORE_WRAPPING",
    "DWRITE_PANOSE_SCRIPT_FORM_EXAGGERATED_EXTREME_WRAPPING",
    "DWRITE_PANOSE_FINIALS",
    "DWRITE_PANOSE_FINIALS_ANY",
    "DWRITE_PANOSE_FINIALS_NO_FIT",
    "DWRITE_PANOSE_FINIALS_NONE_NO_LOOPS",
    "DWRITE_PANOSE_FINIALS_NONE_CLOSED_LOOPS",
    "DWRITE_PANOSE_FINIALS_NONE_OPEN_LOOPS",
    "DWRITE_PANOSE_FINIALS_SHARP_NO_LOOPS",
    "DWRITE_PANOSE_FINIALS_SHARP_CLOSED_LOOPS",
    "DWRITE_PANOSE_FINIALS_SHARP_OPEN_LOOPS",
    "DWRITE_PANOSE_FINIALS_TAPERED_NO_LOOPS",
    "DWRITE_PANOSE_FINIALS_TAPERED_CLOSED_LOOPS",
    "DWRITE_PANOSE_FINIALS_TAPERED_OPEN_LOOPS",
    "DWRITE_PANOSE_FINIALS_ROUND_NO_LOOPS",
    "DWRITE_PANOSE_FINIALS_ROUND_CLOSED_LOOPS",
    "DWRITE_PANOSE_FINIALS_ROUND_OPEN_LOOPS",
    "DWRITE_PANOSE_XASCENT",
    "DWRITE_PANOSE_XASCENT_ANY",
    "DWRITE_PANOSE_XASCENT_NO_FIT",
    "DWRITE_PANOSE_XASCENT_VERY_LOW",
    "DWRITE_PANOSE_XASCENT_LOW",
    "DWRITE_PANOSE_XASCENT_MEDIUM",
    "DWRITE_PANOSE_XASCENT_HIGH",
    "DWRITE_PANOSE_XASCENT_VERY_HIGH",
    "DWRITE_PANOSE_DECORATIVE_CLASS",
    "DWRITE_PANOSE_DECORATIVE_CLASS_ANY",
    "DWRITE_PANOSE_DECORATIVE_CLASS_NO_FIT",
    "DWRITE_PANOSE_DECORATIVE_CLASS_DERIVATIVE",
    "DWRITE_PANOSE_DECORATIVE_CLASS_NONSTANDARD_TOPOLOGY",
    "DWRITE_PANOSE_DECORATIVE_CLASS_NONSTANDARD_ELEMENTS",
    "DWRITE_PANOSE_DECORATIVE_CLASS_NONSTANDARD_ASPECT",
    "DWRITE_PANOSE_DECORATIVE_CLASS_INITIALS",
    "DWRITE_PANOSE_DECORATIVE_CLASS_CARTOON",
    "DWRITE_PANOSE_DECORATIVE_CLASS_PICTURE_STEMS",
    "DWRITE_PANOSE_DECORATIVE_CLASS_ORNAMENTED",
    "DWRITE_PANOSE_DECORATIVE_CLASS_TEXT_AND_BACKGROUND",
    "DWRITE_PANOSE_DECORATIVE_CLASS_COLLAGE",
    "DWRITE_PANOSE_DECORATIVE_CLASS_MONTAGE",
    "DWRITE_PANOSE_ASPECT",
    "DWRITE_PANOSE_ASPECT_ANY",
    "DWRITE_PANOSE_ASPECT_NO_FIT",
    "DWRITE_PANOSE_ASPECT_SUPER_CONDENSED",
    "DWRITE_PANOSE_ASPECT_VERY_CONDENSED",
    "DWRITE_PANOSE_ASPECT_CONDENSED",
    "DWRITE_PANOSE_ASPECT_NORMAL",
    "DWRITE_PANOSE_ASPECT_EXTENDED",
    "DWRITE_PANOSE_ASPECT_VERY_EXTENDED",
    "DWRITE_PANOSE_ASPECT_SUPER_EXTENDED",
    "DWRITE_PANOSE_ASPECT_MONOSPACED",
    "DWRITE_PANOSE_FILL",
    "DWRITE_PANOSE_FILL_ANY",
    "DWRITE_PANOSE_FILL_NO_FIT",
    "DWRITE_PANOSE_FILL_STANDARD_SOLID_FILL",
    "DWRITE_PANOSE_FILL_NO_FILL",
    "DWRITE_PANOSE_FILL_PATTERNED_FILL",
    "DWRITE_PANOSE_FILL_COMPLEX_FILL",
    "DWRITE_PANOSE_FILL_SHAPED_FILL",
    "DWRITE_PANOSE_FILL_DRAWN_DISTRESSED",
    "DWRITE_PANOSE_LINING",
    "DWRITE_PANOSE_LINING_ANY",
    "DWRITE_PANOSE_LINING_NO_FIT",
    "DWRITE_PANOSE_LINING_NONE",
    "DWRITE_PANOSE_LINING_INLINE",
    "DWRITE_PANOSE_LINING_OUTLINE",
    "DWRITE_PANOSE_LINING_ENGRAVED",
    "DWRITE_PANOSE_LINING_SHADOW",
    "DWRITE_PANOSE_LINING_RELIEF",
    "DWRITE_PANOSE_LINING_BACKDROP",
    "DWRITE_PANOSE_DECORATIVE_TOPOLOGY",
    "DWRITE_PANOSE_DECORATIVE_TOPOLOGY_ANY",
    "DWRITE_PANOSE_DECORATIVE_TOPOLOGY_NO_FIT",
    "DWRITE_PANOSE_DECORATIVE_TOPOLOGY_STANDARD",
    "DWRITE_PANOSE_DECORATIVE_TOPOLOGY_SQUARE",
    "DWRITE_PANOSE_DECORATIVE_TOPOLOGY_MULTIPLE_SEGMENT",
    "DWRITE_PANOSE_DECORATIVE_TOPOLOGY_ART_DECO",
    "DWRITE_PANOSE_DECORATIVE_TOPOLOGY_UNEVEN_WEIGHTING",
    "DWRITE_PANOSE_DECORATIVE_TOPOLOGY_DIVERSE_ARMS",
    "DWRITE_PANOSE_DECORATIVE_TOPOLOGY_DIVERSE_FORMS",
    "DWRITE_PANOSE_DECORATIVE_TOPOLOGY_LOMBARDIC_FORMS",
    "DWRITE_PANOSE_DECORATIVE_TOPOLOGY_UPPER_CASE_IN_LOWER_CASE",
    "DWRITE_PANOSE_DECORATIVE_TOPOLOGY_IMPLIED_TOPOLOGY",
    "DWRITE_PANOSE_DECORATIVE_TOPOLOGY_HORSESHOE_E_AND_A",
    "DWRITE_PANOSE_DECORATIVE_TOPOLOGY_CURSIVE",
    "DWRITE_PANOSE_DECORATIVE_TOPOLOGY_BLACKLETTER",
    "DWRITE_PANOSE_DECORATIVE_TOPOLOGY_SWASH_VARIANCE",
    "DWRITE_PANOSE_CHARACTER_RANGES",
    "DWRITE_PANOSE_CHARACTER_RANGES_ANY",
    "DWRITE_PANOSE_CHARACTER_RANGES_NO_FIT",
    "DWRITE_PANOSE_CHARACTER_RANGES_EXTENDED_COLLECTION",
    "DWRITE_PANOSE_CHARACTER_RANGES_LITERALS",
    "DWRITE_PANOSE_CHARACTER_RANGES_NO_LOWER_CASE",
    "DWRITE_PANOSE_CHARACTER_RANGES_SMALL_CAPS",
    "DWRITE_PANOSE_SYMBOL_KIND",
    "DWRITE_PANOSE_SYMBOL_KIND_ANY",
    "DWRITE_PANOSE_SYMBOL_KIND_NO_FIT",
    "DWRITE_PANOSE_SYMBOL_KIND_MONTAGES",
    "DWRITE_PANOSE_SYMBOL_KIND_PICTURES",
    "DWRITE_PANOSE_SYMBOL_KIND_SHAPES",
    "DWRITE_PANOSE_SYMBOL_KIND_SCIENTIFIC",
    "DWRITE_PANOSE_SYMBOL_KIND_MUSIC",
    "DWRITE_PANOSE_SYMBOL_KIND_EXPERT",
    "DWRITE_PANOSE_SYMBOL_KIND_PATTERNS",
    "DWRITE_PANOSE_SYMBOL_KIND_BOARDERS",
    "DWRITE_PANOSE_SYMBOL_KIND_ICONS",
    "DWRITE_PANOSE_SYMBOL_KIND_LOGOS",
    "DWRITE_PANOSE_SYMBOL_KIND_INDUSTRY_SPECIFIC",
    "DWRITE_PANOSE_SYMBOL_ASPECT_RATIO",
    "DWRITE_PANOSE_SYMBOL_ASPECT_RATIO_ANY",
    "DWRITE_PANOSE_SYMBOL_ASPECT_RATIO_NO_FIT",
    "DWRITE_PANOSE_SYMBOL_ASPECT_RATIO_NO_WIDTH",
    "DWRITE_PANOSE_SYMBOL_ASPECT_RATIO_EXCEPTIONALLY_WIDE",
    "DWRITE_PANOSE_SYMBOL_ASPECT_RATIO_SUPER_WIDE",
    "DWRITE_PANOSE_SYMBOL_ASPECT_RATIO_VERY_WIDE",
    "DWRITE_PANOSE_SYMBOL_ASPECT_RATIO_WIDE",
    "DWRITE_PANOSE_SYMBOL_ASPECT_RATIO_NORMAL",
    "DWRITE_PANOSE_SYMBOL_ASPECT_RATIO_NARROW",
    "DWRITE_PANOSE_SYMBOL_ASPECT_RATIO_VERY_NARROW",
    "DWRITE_OUTLINE_THRESHOLD",
    "DWRITE_OUTLINE_THRESHOLD_ANTIALIASED",
    "DWRITE_OUTLINE_THRESHOLD_ALIASED",
    "DWRITE_BASELINE",
    "DWRITE_BASELINE_DEFAULT",
    "DWRITE_BASELINE_ROMAN",
    "DWRITE_BASELINE_CENTRAL",
    "DWRITE_BASELINE_MATH",
    "DWRITE_BASELINE_HANGING",
    "DWRITE_BASELINE_IDEOGRAPHIC_BOTTOM",
    "DWRITE_BASELINE_IDEOGRAPHIC_TOP",
    "DWRITE_BASELINE_MINIMUM",
    "DWRITE_BASELINE_MAXIMUM",
    "DWRITE_VERTICAL_GLYPH_ORIENTATION",
    "DWRITE_VERTICAL_GLYPH_ORIENTATION_DEFAULT",
    "DWRITE_VERTICAL_GLYPH_ORIENTATION_STACKED",
    "DWRITE_GLYPH_ORIENTATION_ANGLE",
    "DWRITE_GLYPH_ORIENTATION_ANGLE_0_DEGREES",
    "DWRITE_GLYPH_ORIENTATION_ANGLE_90_DEGREES",
    "DWRITE_GLYPH_ORIENTATION_ANGLE_180_DEGREES",
    "DWRITE_GLYPH_ORIENTATION_ANGLE_270_DEGREES",
    "DWRITE_FONT_METRICS1",
    "DWRITE_CARET_METRICS",
    "DWRITE_PANOSE",
    "DWRITE_UNICODE_RANGE",
    "DWRITE_SCRIPT_PROPERTIES",
    "DWRITE_JUSTIFICATION_OPPORTUNITY",
    "IDWriteFactory1",
    "IDWriteFontFace1",
    "IDWriteFont1",
    "IDWriteRenderingParams1",
    "IDWriteTextAnalyzer1",
    "IDWriteTextAnalysisSource1",
    "IDWriteTextAnalysisSink1",
    "IDWriteTextLayout1",
    "DWRITE_TEXT_ANTIALIAS_MODE",
    "DWRITE_TEXT_ANTIALIAS_MODE_CLEARTYPE",
    "DWRITE_TEXT_ANTIALIAS_MODE_GRAYSCALE",
    "IDWriteBitmapRenderTarget1",
    "DWRITE_OPTICAL_ALIGNMENT",
    "DWRITE_OPTICAL_ALIGNMENT_NONE",
    "DWRITE_OPTICAL_ALIGNMENT_NO_SIDE_BEARINGS",
    "DWRITE_GRID_FIT_MODE",
    "DWRITE_GRID_FIT_MODE_DEFAULT",
    "DWRITE_GRID_FIT_MODE_DISABLED",
    "DWRITE_GRID_FIT_MODE_ENABLED",
    "DWRITE_TEXT_METRICS1",
    "IDWriteTextRenderer1",
    "IDWriteTextFormat1",
    "IDWriteTextLayout2",
    "IDWriteTextAnalyzer2",
    "IDWriteFontFallback",
    "IDWriteFontFallbackBuilder",
    "IDWriteFont2",
    "IDWriteFontFace2",
    "DWRITE_COLOR_GLYPH_RUN",
    "IDWriteColorGlyphRunEnumerator",
    "IDWriteRenderingParams2",
    "IDWriteFactory2",
    "DWRITE_FONT_PROPERTY_ID",
    "DWRITE_FONT_PROPERTY_ID_NONE",
    "DWRITE_FONT_PROPERTY_ID_WEIGHT_STRETCH_STYLE_FAMILY_NAME",
    "DWRITE_FONT_PROPERTY_ID_TYPOGRAPHIC_FAMILY_NAME",
    "DWRITE_FONT_PROPERTY_ID_WEIGHT_STRETCH_STYLE_FACE_NAME",
    "DWRITE_FONT_PROPERTY_ID_FULL_NAME",
    "DWRITE_FONT_PROPERTY_ID_WIN32_FAMILY_NAME",
    "DWRITE_FONT_PROPERTY_ID_POSTSCRIPT_NAME",
    "DWRITE_FONT_PROPERTY_ID_DESIGN_SCRIPT_LANGUAGE_TAG",
    "DWRITE_FONT_PROPERTY_ID_SUPPORTED_SCRIPT_LANGUAGE_TAG",
    "DWRITE_FONT_PROPERTY_ID_SEMANTIC_TAG",
    "DWRITE_FONT_PROPERTY_ID_WEIGHT",
    "DWRITE_FONT_PROPERTY_ID_STRETCH",
    "DWRITE_FONT_PROPERTY_ID_STYLE",
    "DWRITE_FONT_PROPERTY_ID_TYPOGRAPHIC_FACE_NAME",
    "DWRITE_FONT_PROPERTY_ID_TOTAL",
    "DWRITE_FONT_PROPERTY_ID_TOTAL_RS3",
    "DWRITE_FONT_PROPERTY_ID_PREFERRED_FAMILY_NAME",
    "DWRITE_FONT_PROPERTY_ID_FAMILY_NAME",
    "DWRITE_FONT_PROPERTY_ID_FACE_NAME",
    "DWRITE_FONT_PROPERTY",
    "DWRITE_LOCALITY",
    "DWRITE_LOCALITY_REMOTE",
    "DWRITE_LOCALITY_PARTIAL",
    "DWRITE_LOCALITY_LOCAL",
    "DWRITE_RENDERING_MODE1",
    "DWRITE_RENDERING_MODE1_DEFAULT",
    "DWRITE_RENDERING_MODE1_ALIASED",
    "DWRITE_RENDERING_MODE1_GDI_CLASSIC",
    "DWRITE_RENDERING_MODE1_GDI_NATURAL",
    "DWRITE_RENDERING_MODE1_NATURAL",
    "DWRITE_RENDERING_MODE1_NATURAL_SYMMETRIC",
    "DWRITE_RENDERING_MODE1_OUTLINE",
    "DWRITE_RENDERING_MODE1_NATURAL_SYMMETRIC_DOWNSAMPLED",
    "IDWriteRenderingParams3",
    "IDWriteFactory3",
    "IDWriteFontSet",
    "IDWriteFontSetBuilder",
    "IDWriteFontCollection1",
    "IDWriteFontFamily1",
    "IDWriteFontList1",
    "IDWriteFontFaceReference",
    "IDWriteFont3",
    "IDWriteFontFace3",
    "IDWriteStringList",
    "IDWriteFontDownloadListener",
    "IDWriteFontDownloadQueue",
    "IDWriteGdiInterop1",
    "DWRITE_LINE_METRICS1",
    "DWRITE_FONT_LINE_GAP_USAGE",
    "DWRITE_FONT_LINE_GAP_USAGE_DEFAULT",
    "DWRITE_FONT_LINE_GAP_USAGE_DISABLED",
    "DWRITE_FONT_LINE_GAP_USAGE_ENABLED",
    "DWRITE_LINE_SPACING",
    "IDWriteTextFormat2",
    "IDWriteTextLayout3",
    "DWRITE_COLOR_GLYPH_RUN1",
    "DWRITE_GLYPH_IMAGE_DATA",
    "IDWriteColorGlyphRunEnumerator1",
    "IDWriteFontFace4",
    "IDWriteFactory4",
    "IDWriteFontSetBuilder1",
    "IDWriteAsyncResult",
    "DWRITE_FILE_FRAGMENT",
    "IDWriteRemoteFontFileStream",
    "DWRITE_CONTAINER_TYPE",
    "DWRITE_CONTAINER_TYPE_UNKNOWN",
    "DWRITE_CONTAINER_TYPE_WOFF",
    "DWRITE_CONTAINER_TYPE_WOFF2",
    "IDWriteRemoteFontFileLoader",
    "IDWriteInMemoryFontFileLoader",
    "IDWriteFactory5",
    "DWRITE_FONT_AXIS_VALUE",
    "DWRITE_FONT_AXIS_RANGE",
    "DWRITE_FONT_FAMILY_MODEL",
    "DWRITE_FONT_FAMILY_MODEL_TYPOGRAPHIC",
    "DWRITE_FONT_FAMILY_MODEL_WEIGHT_STRETCH_STYLE",
    "DWRITE_AUTOMATIC_FONT_AXES",
    "DWRITE_AUTOMATIC_FONT_AXES_NONE",
    "DWRITE_AUTOMATIC_FONT_AXES_OPTICAL_SIZE",
    "DWRITE_FONT_AXIS_ATTRIBUTES",
    "DWRITE_FONT_AXIS_ATTRIBUTES_NONE",
    "DWRITE_FONT_AXIS_ATTRIBUTES_VARIABLE",
    "DWRITE_FONT_AXIS_ATTRIBUTES_HIDDEN",
    "IDWriteFactory6",
    "IDWriteFontFace5",
    "IDWriteFontResource",
    "IDWriteFontFaceReference1",
    "IDWriteFontSetBuilder2",
    "IDWriteFontSet1",
    "IDWriteFontList2",
    "IDWriteFontFamily2",
    "IDWriteFontCollection2",
    "IDWriteTextLayout4",
    "IDWriteTextFormat3",
    "IDWriteFontFallback1",
    "IDWriteFontSet2",
    "IDWriteFontCollection3",
    "IDWriteFactory7",
    "DWRITE_FONT_SOURCE_TYPE",
    "DWRITE_FONT_SOURCE_TYPE_UNKNOWN",
    "DWRITE_FONT_SOURCE_TYPE_PER_MACHINE",
    "DWRITE_FONT_SOURCE_TYPE_PER_USER",
    "DWRITE_FONT_SOURCE_TYPE_APPX_PACKAGE",
    "DWRITE_FONT_SOURCE_TYPE_REMOTE_FONT_PROVIDER",
    "IDWriteFontSet3",
    "IDWriteFontFace6",
    "DWriteCreateFactory",
]
