from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.System.Com
import win32more.UI.ColorSystem
import win32more.UI.WindowsAndMessaging

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
CATID_WcsPlugin = 'a0b402e0-8240-405f-8a16-8a5b4df2f0dd'
MAX_COLOR_CHANNELS = 8
INTENT_PERCEPTUAL = 0
INTENT_RELATIVE_COLORIMETRIC = 1
INTENT_SATURATION = 2
INTENT_ABSOLUTE_COLORIMETRIC = 3
FLAG_EMBEDDEDPROFILE = 1
FLAG_DEPENDENTONDATA = 2
FLAG_ENABLE_CHROMATIC_ADAPTATION = 33554432
ATTRIB_TRANSPARENCY = 1
ATTRIB_MATTE = 2
PROFILE_FILENAME = 1
PROFILE_MEMBUFFER = 2
PROFILE_READ = 1
PROFILE_READWRITE = 2
INDEX_DONT_CARE = 0
CMM_FROM_PROFILE = 0
ENUM_TYPE_VERSION = 768
ET_DEVICENAME = 1
ET_MEDIATYPE = 2
ET_DITHERMODE = 4
ET_RESOLUTION = 8
ET_CMMTYPE = 16
ET_CLASS = 32
ET_DATACOLORSPACE = 64
ET_CONNECTIONSPACE = 128
ET_SIGNATURE = 256
ET_PLATFORM = 512
ET_PROFILEFLAGS = 1024
ET_MANUFACTURER = 2048
ET_MODEL = 4096
ET_ATTRIBUTES = 8192
ET_RENDERINGINTENT = 16384
ET_CREATOR = 32768
ET_DEVICECLASS = 65536
ET_STANDARDDISPLAYCOLOR = 131072
ET_EXTENDEDDISPLAYCOLOR = 262144
PROOF_MODE = 1
NORMAL_MODE = 2
BEST_MODE = 3
ENABLE_GAMUT_CHECKING = 65536
USE_RELATIVE_COLORIMETRIC = 131072
FAST_TRANSLATE = 262144
PRESERVEBLACK = 1048576
WCS_ALWAYS = 2097152
SEQUENTIAL_TRANSFORM = 2155872256
RESERVED = 2147483648
CSA_A = 1
CSA_ABC = 2
CSA_DEF = 3
CSA_DEFG = 4
CSA_GRAY = 5
CSA_RGB = 6
CSA_CMYK = 7
CSA_Lab = 8
CMM_WIN_VERSION = 0
CMM_IDENT = 1
CMM_DRIVER_VERSION = 2
CMM_DLL_VERSION = 3
CMM_VERSION = 4
CMM_DESCRIPTION = 5
CMM_LOGOICON = 6
CMS_FORWARD = 0
CMS_BACKWARD = 1
COLOR_MATCH_VERSION = 512
CMS_DISABLEICM = 1
CMS_ENABLEPROOFING = 2
CMS_SETRENDERINTENT = 4
CMS_SETPROOFINTENT = 8
CMS_SETMONITORPROFILE = 16
CMS_SETPRINTERPROFILE = 32
CMS_SETTARGETPROFILE = 64
CMS_USEHOOK = 128
CMS_USEAPPLYCALLBACK = 256
CMS_USEDESCRIPTION = 512
CMS_DISABLEINTENT = 1024
CMS_DISABLERENDERINTENT = 2048
CMS_MONITOROVERFLOW = -2147483648
CMS_PRINTEROVERFLOW = 1073741824
CMS_TARGETOVERFLOW = 536870912
DONT_USE_EMBEDDED_WCS_PROFILES = 1
WCS_DEFAULT = 0
WCS_ICCONLY = 65536
ICM_COMMAND = UInt32
ICM_ADDPROFILE = 1
ICM_DELETEPROFILE = 2
ICM_QUERYPROFILE = 3
ICM_SETDEFAULTPROFILE = 4
ICM_REGISTERICMATCHER = 5
ICM_UNREGISTERICMATCHER = 6
ICM_QUERYMATCH = 7
COLOR_MATCH_TO_TARGET_ACTION = Int32
CS_ENABLE = 1
CS_DISABLE = 2
CS_DELETE_TRANSFORM = 3
HCOLORSPACE = IntPtr
def _define_LOGCOLORSPACEA_head():
    class LOGCOLORSPACEA(Structure):
        pass
    return LOGCOLORSPACEA
def _define_LOGCOLORSPACEA():
    LOGCOLORSPACEA = win32more.UI.ColorSystem.LOGCOLORSPACEA_head
    LOGCOLORSPACEA._fields_ = [
        ("lcsSignature", UInt32),
        ("lcsVersion", UInt32),
        ("lcsSize", UInt32),
        ("lcsCSType", Int32),
        ("lcsIntent", Int32),
        ("lcsEndpoints", win32more.Graphics.Gdi.CIEXYZTRIPLE),
        ("lcsGammaRed", UInt32),
        ("lcsGammaGreen", UInt32),
        ("lcsGammaBlue", UInt32),
        ("lcsFilename", win32more.Foundation.CHAR * 260),
    ]
    return LOGCOLORSPACEA
def _define_LOGCOLORSPACEW_head():
    class LOGCOLORSPACEW(Structure):
        pass
    return LOGCOLORSPACEW
def _define_LOGCOLORSPACEW():
    LOGCOLORSPACEW = win32more.UI.ColorSystem.LOGCOLORSPACEW_head
    LOGCOLORSPACEW._fields_ = [
        ("lcsSignature", UInt32),
        ("lcsVersion", UInt32),
        ("lcsSize", UInt32),
        ("lcsCSType", Int32),
        ("lcsIntent", Int32),
        ("lcsEndpoints", win32more.Graphics.Gdi.CIEXYZTRIPLE),
        ("lcsGammaRed", UInt32),
        ("lcsGammaGreen", UInt32),
        ("lcsGammaBlue", UInt32),
        ("lcsFilename", Char * 260),
    ]
    return LOGCOLORSPACEW
def _define_ICMENUMPROCA():
    return CFUNCTYPE(Int32,win32more.Foundation.PSTR,win32more.Foundation.LPARAM, use_last_error=False)
def _define_ICMENUMPROCW():
    return CFUNCTYPE(Int32,win32more.Foundation.PWSTR,win32more.Foundation.LPARAM, use_last_error=False)
def _define_EMRCREATECOLORSPACE_head():
    class EMRCREATECOLORSPACE(Structure):
        pass
    return EMRCREATECOLORSPACE
def _define_EMRCREATECOLORSPACE():
    EMRCREATECOLORSPACE = win32more.UI.ColorSystem.EMRCREATECOLORSPACE_head
    EMRCREATECOLORSPACE._fields_ = [
        ("emr", win32more.Graphics.Gdi.EMR),
        ("ihCS", UInt32),
        ("lcs", win32more.UI.ColorSystem.LOGCOLORSPACEA),
    ]
    return EMRCREATECOLORSPACE
def _define_EMRCREATECOLORSPACEW_head():
    class EMRCREATECOLORSPACEW(Structure):
        pass
    return EMRCREATECOLORSPACEW
def _define_EMRCREATECOLORSPACEW():
    EMRCREATECOLORSPACEW = win32more.UI.ColorSystem.EMRCREATECOLORSPACEW_head
    EMRCREATECOLORSPACEW._fields_ = [
        ("emr", win32more.Graphics.Gdi.EMR),
        ("ihCS", UInt32),
        ("lcs", win32more.UI.ColorSystem.LOGCOLORSPACEW),
        ("dwFlags", UInt32),
        ("cbData", UInt32),
        ("Data", Byte * 0),
    ]
    return EMRCREATECOLORSPACEW
def _define_XYZColorF_head():
    class XYZColorF(Structure):
        pass
    return XYZColorF
def _define_XYZColorF():
    XYZColorF = win32more.UI.ColorSystem.XYZColorF_head
    XYZColorF._fields_ = [
        ("X", Single),
        ("Y", Single),
        ("Z", Single),
    ]
    return XYZColorF
def _define_JChColorF_head():
    class JChColorF(Structure):
        pass
    return JChColorF
def _define_JChColorF():
    JChColorF = win32more.UI.ColorSystem.JChColorF_head
    JChColorF._fields_ = [
        ("J", Single),
        ("C", Single),
        ("h", Single),
    ]
    return JChColorF
def _define_JabColorF_head():
    class JabColorF(Structure):
        pass
    return JabColorF
def _define_JabColorF():
    JabColorF = win32more.UI.ColorSystem.JabColorF_head
    JabColorF._fields_ = [
        ("J", Single),
        ("a", Single),
        ("b", Single),
    ]
    return JabColorF
def _define_GamutShellTriangle_head():
    class GamutShellTriangle(Structure):
        pass
    return GamutShellTriangle
def _define_GamutShellTriangle():
    GamutShellTriangle = win32more.UI.ColorSystem.GamutShellTriangle_head
    GamutShellTriangle._fields_ = [
        ("aVertexIndex", UInt32 * 3),
    ]
    return GamutShellTriangle
def _define_GamutShell_head():
    class GamutShell(Structure):
        pass
    return GamutShell
def _define_GamutShell():
    GamutShell = win32more.UI.ColorSystem.GamutShell_head
    GamutShell._fields_ = [
        ("JMin", Single),
        ("JMax", Single),
        ("cVertices", UInt32),
        ("cTriangles", UInt32),
        ("pVertices", POINTER(win32more.UI.ColorSystem.JabColorF_head)),
        ("pTriangles", POINTER(win32more.UI.ColorSystem.GamutShellTriangle_head)),
    ]
    return GamutShell
def _define_PrimaryJabColors_head():
    class PrimaryJabColors(Structure):
        pass
    return PrimaryJabColors
def _define_PrimaryJabColors():
    PrimaryJabColors = win32more.UI.ColorSystem.PrimaryJabColors_head
    PrimaryJabColors._fields_ = [
        ("red", win32more.UI.ColorSystem.JabColorF),
        ("yellow", win32more.UI.ColorSystem.JabColorF),
        ("green", win32more.UI.ColorSystem.JabColorF),
        ("cyan", win32more.UI.ColorSystem.JabColorF),
        ("blue", win32more.UI.ColorSystem.JabColorF),
        ("magenta", win32more.UI.ColorSystem.JabColorF),
        ("black", win32more.UI.ColorSystem.JabColorF),
        ("white", win32more.UI.ColorSystem.JabColorF),
    ]
    return PrimaryJabColors
def _define_PrimaryXYZColors_head():
    class PrimaryXYZColors(Structure):
        pass
    return PrimaryXYZColors
def _define_PrimaryXYZColors():
    PrimaryXYZColors = win32more.UI.ColorSystem.PrimaryXYZColors_head
    PrimaryXYZColors._fields_ = [
        ("red", win32more.UI.ColorSystem.XYZColorF),
        ("yellow", win32more.UI.ColorSystem.XYZColorF),
        ("green", win32more.UI.ColorSystem.XYZColorF),
        ("cyan", win32more.UI.ColorSystem.XYZColorF),
        ("blue", win32more.UI.ColorSystem.XYZColorF),
        ("magenta", win32more.UI.ColorSystem.XYZColorF),
        ("black", win32more.UI.ColorSystem.XYZColorF),
        ("white", win32more.UI.ColorSystem.XYZColorF),
    ]
    return PrimaryXYZColors
def _define_GamutBoundaryDescription_head():
    class GamutBoundaryDescription(Structure):
        pass
    return GamutBoundaryDescription
def _define_GamutBoundaryDescription():
    GamutBoundaryDescription = win32more.UI.ColorSystem.GamutBoundaryDescription_head
    GamutBoundaryDescription._fields_ = [
        ("pPrimaries", POINTER(win32more.UI.ColorSystem.PrimaryJabColors_head)),
        ("cNeutralSamples", UInt32),
        ("pNeutralSamples", POINTER(win32more.UI.ColorSystem.JabColorF_head)),
        ("pReferenceShell", POINTER(win32more.UI.ColorSystem.GamutShell_head)),
        ("pPlausibleShell", POINTER(win32more.UI.ColorSystem.GamutShell_head)),
        ("pPossibleShell", POINTER(win32more.UI.ColorSystem.GamutShell_head)),
    ]
    return GamutBoundaryDescription
def _define_BlackInformation_head():
    class BlackInformation(Structure):
        pass
    return BlackInformation
def _define_BlackInformation():
    BlackInformation = win32more.UI.ColorSystem.BlackInformation_head
    BlackInformation._fields_ = [
        ("fBlackOnly", win32more.Foundation.BOOL),
        ("blackWeight", Single),
    ]
    return BlackInformation
def _define_IDeviceModelPlugIn_head():
    class IDeviceModelPlugIn(win32more.System.Com.IUnknown_head):
        Guid = Guid('1cd63475-07c4-46fe-a903-d655316d11fd')
    return IDeviceModelPlugIn
def _define_IDeviceModelPlugIn():
    IDeviceModelPlugIn = win32more.UI.ColorSystem.IDeviceModelPlugIn_head
    IDeviceModelPlugIn.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,UInt32,UInt32, use_last_error=False)(3, 'Initialize', ((1, 'bstrXml'),(1, 'cNumModels'),(1, 'iModelPosition'),)))
    IDeviceModelPlugIn.GetNumChannels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetNumChannels', ((1, 'pNumChannels'),)))
    IDeviceModelPlugIn.DeviceToColorimetricColors = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(Single),POINTER(win32more.UI.ColorSystem.XYZColorF), use_last_error=False)(5, 'DeviceToColorimetricColors', ((1, 'cColors'),(1, 'cChannels'),(1, 'pDeviceValues'),(1, 'pXYZColors'),)))
    IDeviceModelPlugIn.ColorimetricToDeviceColors = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.UI.ColorSystem.XYZColorF),POINTER(Single), use_last_error=False)(6, 'ColorimetricToDeviceColors', ((1, 'cColors'),(1, 'cChannels'),(1, 'pXYZColors'),(1, 'pDeviceValues'),)))
    IDeviceModelPlugIn.ColorimetricToDeviceColorsWithBlack = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.UI.ColorSystem.XYZColorF),POINTER(win32more.UI.ColorSystem.BlackInformation),POINTER(Single), use_last_error=False)(7, 'ColorimetricToDeviceColorsWithBlack', ((1, 'cColors'),(1, 'cChannels'),(1, 'pXYZColors'),(1, 'pBlackInformation'),(1, 'pDeviceValues'),)))
    IDeviceModelPlugIn.SetTransformDeviceModelInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.UI.ColorSystem.IDeviceModelPlugIn_head, use_last_error=False)(8, 'SetTransformDeviceModelInfo', ((1, 'iModelPosition'),(1, 'pIDeviceModelOther'),)))
    IDeviceModelPlugIn.GetPrimarySamples = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.ColorSystem.PrimaryXYZColors_head), use_last_error=False)(9, 'GetPrimarySamples', ((1, 'pPrimaryColor'),)))
    IDeviceModelPlugIn.GetGamutBoundaryMeshSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(10, 'GetGamutBoundaryMeshSize', ((1, 'pNumVertices'),(1, 'pNumTriangles'),)))
    IDeviceModelPlugIn.GetGamutBoundaryMesh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,POINTER(Single),POINTER(win32more.UI.ColorSystem.GamutShellTriangle), use_last_error=False)(11, 'GetGamutBoundaryMesh', ((1, 'cChannels'),(1, 'cVertices'),(1, 'cTriangles'),(1, 'pVertices'),(1, 'pTriangles'),)))
    IDeviceModelPlugIn.GetNeutralAxisSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(12, 'GetNeutralAxisSize', ((1, 'pcColors'),)))
    IDeviceModelPlugIn.GetNeutralAxis = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.ColorSystem.XYZColorF), use_last_error=False)(13, 'GetNeutralAxis', ((1, 'cColors'),(1, 'pXYZColors'),)))
    win32more.System.Com.IUnknown
    return IDeviceModelPlugIn
def _define_IGamutMapModelPlugIn_head():
    class IGamutMapModelPlugIn(win32more.System.Com.IUnknown_head):
        Guid = Guid('2dd80115-ad1e-41f6-a219-a4f4b583d1f9')
    return IGamutMapModelPlugIn
def _define_IGamutMapModelPlugIn():
    IGamutMapModelPlugIn = win32more.UI.ColorSystem.IGamutMapModelPlugIn_head
    IGamutMapModelPlugIn.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.UI.ColorSystem.IDeviceModelPlugIn_head,win32more.UI.ColorSystem.IDeviceModelPlugIn_head,POINTER(win32more.UI.ColorSystem.GamutBoundaryDescription_head),POINTER(win32more.UI.ColorSystem.GamutBoundaryDescription_head), use_last_error=False)(3, 'Initialize', ((1, 'bstrXml'),(1, 'pSrcPlugIn'),(1, 'pDestPlugIn'),(1, 'pSrcGBD'),(1, 'pDestGBD'),)))
    IGamutMapModelPlugIn.SourceToDestinationAppearanceColors = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.ColorSystem.JChColorF),POINTER(win32more.UI.ColorSystem.JChColorF), use_last_error=False)(4, 'SourceToDestinationAppearanceColors', ((1, 'cColors'),(1, 'pInputColors'),(1, 'pOutputColors'),)))
    win32more.System.Com.IUnknown
    return IGamutMapModelPlugIn
def _define_NAMED_PROFILE_INFO_head():
    class NAMED_PROFILE_INFO(Structure):
        pass
    return NAMED_PROFILE_INFO
def _define_NAMED_PROFILE_INFO():
    NAMED_PROFILE_INFO = win32more.UI.ColorSystem.NAMED_PROFILE_INFO_head
    NAMED_PROFILE_INFO._fields_ = [
        ("dwFlags", UInt32),
        ("dwCount", UInt32),
        ("dwCountDevCoordinates", UInt32),
        ("szPrefix", SByte * 32),
        ("szSuffix", SByte * 32),
    ]
    return NAMED_PROFILE_INFO
def _define_GRAYCOLOR_head():
    class GRAYCOLOR(Structure):
        pass
    return GRAYCOLOR
def _define_GRAYCOLOR():
    GRAYCOLOR = win32more.UI.ColorSystem.GRAYCOLOR_head
    GRAYCOLOR._fields_ = [
        ("gray", UInt16),
    ]
    return GRAYCOLOR
def _define_RGBCOLOR_head():
    class RGBCOLOR(Structure):
        pass
    return RGBCOLOR
def _define_RGBCOLOR():
    RGBCOLOR = win32more.UI.ColorSystem.RGBCOLOR_head
    RGBCOLOR._fields_ = [
        ("red", UInt16),
        ("green", UInt16),
        ("blue", UInt16),
    ]
    return RGBCOLOR
def _define_CMYKCOLOR_head():
    class CMYKCOLOR(Structure):
        pass
    return CMYKCOLOR
def _define_CMYKCOLOR():
    CMYKCOLOR = win32more.UI.ColorSystem.CMYKCOLOR_head
    CMYKCOLOR._fields_ = [
        ("cyan", UInt16),
        ("magenta", UInt16),
        ("yellow", UInt16),
        ("black", UInt16),
    ]
    return CMYKCOLOR
def _define_XYZCOLOR_head():
    class XYZCOLOR(Structure):
        pass
    return XYZCOLOR
def _define_XYZCOLOR():
    XYZCOLOR = win32more.UI.ColorSystem.XYZCOLOR_head
    XYZCOLOR._fields_ = [
        ("X", UInt16),
        ("Y", UInt16),
        ("Z", UInt16),
    ]
    return XYZCOLOR
def _define_YxyCOLOR_head():
    class YxyCOLOR(Structure):
        pass
    return YxyCOLOR
def _define_YxyCOLOR():
    YxyCOLOR = win32more.UI.ColorSystem.YxyCOLOR_head
    YxyCOLOR._fields_ = [
        ("Y", UInt16),
        ("x", UInt16),
        ("y", UInt16),
    ]
    return YxyCOLOR
def _define_LabCOLOR_head():
    class LabCOLOR(Structure):
        pass
    return LabCOLOR
def _define_LabCOLOR():
    LabCOLOR = win32more.UI.ColorSystem.LabCOLOR_head
    LabCOLOR._fields_ = [
        ("L", UInt16),
        ("a", UInt16),
        ("b", UInt16),
    ]
    return LabCOLOR
def _define_GENERIC3CHANNEL_head():
    class GENERIC3CHANNEL(Structure):
        pass
    return GENERIC3CHANNEL
def _define_GENERIC3CHANNEL():
    GENERIC3CHANNEL = win32more.UI.ColorSystem.GENERIC3CHANNEL_head
    GENERIC3CHANNEL._fields_ = [
        ("ch1", UInt16),
        ("ch2", UInt16),
        ("ch3", UInt16),
    ]
    return GENERIC3CHANNEL
def _define_NAMEDCOLOR_head():
    class NAMEDCOLOR(Structure):
        pass
    return NAMEDCOLOR
def _define_NAMEDCOLOR():
    NAMEDCOLOR = win32more.UI.ColorSystem.NAMEDCOLOR_head
    NAMEDCOLOR._fields_ = [
        ("dwIndex", UInt32),
    ]
    return NAMEDCOLOR
def _define_HiFiCOLOR_head():
    class HiFiCOLOR(Structure):
        pass
    return HiFiCOLOR
def _define_HiFiCOLOR():
    HiFiCOLOR = win32more.UI.ColorSystem.HiFiCOLOR_head
    HiFiCOLOR._fields_ = [
        ("channel", Byte * 8),
    ]
    return HiFiCOLOR
def _define_COLOR_head():
    class COLOR(Union):
        pass
    return COLOR
def _define_COLOR():
    COLOR = win32more.UI.ColorSystem.COLOR_head
    class COLOR__Anonymous_e__Struct(Structure):
        pass
    COLOR__Anonymous_e__Struct._fields_ = [
        ("reserved1", UInt32),
        ("reserved2", c_void_p),
    ]
    COLOR._anonymous_ = [
        'Anonymous',
    ]
    COLOR._fields_ = [
        ("gray", win32more.UI.ColorSystem.GRAYCOLOR),
        ("rgb", win32more.UI.ColorSystem.RGBCOLOR),
        ("cmyk", win32more.UI.ColorSystem.CMYKCOLOR),
        ("XYZ", win32more.UI.ColorSystem.XYZCOLOR),
        ("Yxy", win32more.UI.ColorSystem.YxyCOLOR),
        ("Lab", win32more.UI.ColorSystem.LabCOLOR),
        ("gen3ch", win32more.UI.ColorSystem.GENERIC3CHANNEL),
        ("named", win32more.UI.ColorSystem.NAMEDCOLOR),
        ("hifi", win32more.UI.ColorSystem.HiFiCOLOR),
        ("Anonymous", COLOR__Anonymous_e__Struct),
    ]
    return COLOR
COLORTYPE = Int32
COLOR_GRAY = 1
COLOR_RGB = 2
COLOR_XYZ = 3
COLOR_Yxy = 4
COLOR_Lab = 5
COLOR_3_CHANNEL = 6
COLOR_CMYK = 7
COLOR_5_CHANNEL = 8
COLOR_6_CHANNEL = 9
COLOR_7_CHANNEL = 10
COLOR_8_CHANNEL = 11
COLOR_NAMED = 12
COLORPROFILETYPE = Int32
CPT_ICC = 0
CPT_DMP = 1
CPT_CAMP = 2
CPT_GMMP = 3
COLORPROFILESUBTYPE = Int32
CPST_PERCEPTUAL = 0
CPST_RELATIVE_COLORIMETRIC = 1
CPST_SATURATION = 2
CPST_ABSOLUTE_COLORIMETRIC = 3
CPST_NONE = 4
CPST_RGB_WORKING_SPACE = 5
CPST_CUSTOM_WORKING_SPACE = 6
CPST_STANDARD_DISPLAY_COLOR_MODE = 7
CPST_EXTENDED_DISPLAY_COLOR_MODE = 8
COLORDATATYPE = Int32
COLOR_BYTE = 1
COLOR_WORD = 2
COLOR_FLOAT = 3
COLOR_S2DOT13FIXED = 4
COLOR_10b_R10G10B10A2 = 5
COLOR_10b_R10G10B10A2_XR = 6
COLOR_FLOAT16 = 7
BMFORMAT = Int32
BM_x555RGB = 0
BM_x555XYZ = 257
BM_x555Yxy = 258
BM_x555Lab = 259
BM_x555G3CH = 260
BM_RGBTRIPLETS = 2
BM_BGRTRIPLETS = 4
BM_XYZTRIPLETS = 513
BM_YxyTRIPLETS = 514
BM_LabTRIPLETS = 515
BM_G3CHTRIPLETS = 516
BM_5CHANNEL = 517
BM_6CHANNEL = 518
BM_7CHANNEL = 519
BM_8CHANNEL = 520
BM_GRAY = 521
BM_xRGBQUADS = 8
BM_xBGRQUADS = 16
BM_xG3CHQUADS = 772
BM_KYMCQUADS = 773
BM_CMYKQUADS = 32
BM_10b_RGB = 9
BM_10b_XYZ = 1025
BM_10b_Yxy = 1026
BM_10b_Lab = 1027
BM_10b_G3CH = 1028
BM_NAMED_INDEX = 1029
BM_16b_RGB = 10
BM_16b_XYZ = 1281
BM_16b_Yxy = 1282
BM_16b_Lab = 1283
BM_16b_G3CH = 1284
BM_16b_GRAY = 1285
BM_565RGB = 1
BM_32b_scRGB = 1537
BM_32b_scARGB = 1538
BM_S2DOT13FIXED_scRGB = 1539
BM_S2DOT13FIXED_scARGB = 1540
BM_R10G10B10A2 = 1793
BM_R10G10B10A2_XR = 1794
BM_R16G16B16A16_FLOAT = 1795
def _define_LPBMCALLBACKFN():
    return CFUNCTYPE(win32more.Foundation.BOOL,UInt32,UInt32,win32more.Foundation.LPARAM, use_last_error=False)
def _define_PROFILEHEADER_head():
    class PROFILEHEADER(Structure):
        pass
    return PROFILEHEADER
def _define_PROFILEHEADER():
    PROFILEHEADER = win32more.UI.ColorSystem.PROFILEHEADER_head
    PROFILEHEADER._fields_ = [
        ("phSize", UInt32),
        ("phCMMType", UInt32),
        ("phVersion", UInt32),
        ("phClass", UInt32),
        ("phDataColorSpace", UInt32),
        ("phConnectionSpace", UInt32),
        ("phDateTime", UInt32 * 3),
        ("phSignature", UInt32),
        ("phPlatform", UInt32),
        ("phProfileFlags", UInt32),
        ("phManufacturer", UInt32),
        ("phModel", UInt32),
        ("phAttributes", UInt32 * 2),
        ("phRenderingIntent", UInt32),
        ("phIlluminant", win32more.Graphics.Gdi.CIEXYZ),
        ("phCreator", UInt32),
        ("phReserved", Byte * 44),
    ]
    return PROFILEHEADER
def _define_PROFILE_head():
    class PROFILE(Structure):
        pass
    return PROFILE
def _define_PROFILE():
    PROFILE = win32more.UI.ColorSystem.PROFILE_head
    PROFILE._fields_ = [
        ("dwType", UInt32),
        ("pProfileData", c_void_p),
        ("cbDataSize", UInt32),
    ]
    return PROFILE
def _define_ENUMTYPEA_head():
    class ENUMTYPEA(Structure):
        pass
    return ENUMTYPEA
def _define_ENUMTYPEA():
    ENUMTYPEA = win32more.UI.ColorSystem.ENUMTYPEA_head
    ENUMTYPEA._fields_ = [
        ("dwSize", UInt32),
        ("dwVersion", UInt32),
        ("dwFields", UInt32),
        ("pDeviceName", win32more.Foundation.PSTR),
        ("dwMediaType", UInt32),
        ("dwDitheringMode", UInt32),
        ("dwResolution", UInt32 * 2),
        ("dwCMMType", UInt32),
        ("dwClass", UInt32),
        ("dwDataColorSpace", UInt32),
        ("dwConnectionSpace", UInt32),
        ("dwSignature", UInt32),
        ("dwPlatform", UInt32),
        ("dwProfileFlags", UInt32),
        ("dwManufacturer", UInt32),
        ("dwModel", UInt32),
        ("dwAttributes", UInt32 * 2),
        ("dwRenderingIntent", UInt32),
        ("dwCreator", UInt32),
        ("dwDeviceClass", UInt32),
    ]
    return ENUMTYPEA
def _define_ENUMTYPEW_head():
    class ENUMTYPEW(Structure):
        pass
    return ENUMTYPEW
def _define_ENUMTYPEW():
    ENUMTYPEW = win32more.UI.ColorSystem.ENUMTYPEW_head
    ENUMTYPEW._fields_ = [
        ("dwSize", UInt32),
        ("dwVersion", UInt32),
        ("dwFields", UInt32),
        ("pDeviceName", win32more.Foundation.PWSTR),
        ("dwMediaType", UInt32),
        ("dwDitheringMode", UInt32),
        ("dwResolution", UInt32 * 2),
        ("dwCMMType", UInt32),
        ("dwClass", UInt32),
        ("dwDataColorSpace", UInt32),
        ("dwConnectionSpace", UInt32),
        ("dwSignature", UInt32),
        ("dwPlatform", UInt32),
        ("dwProfileFlags", UInt32),
        ("dwManufacturer", UInt32),
        ("dwModel", UInt32),
        ("dwAttributes", UInt32 * 2),
        ("dwRenderingIntent", UInt32),
        ("dwCreator", UInt32),
        ("dwDeviceClass", UInt32),
    ]
    return ENUMTYPEW
WCS_PROFILE_MANAGEMENT_SCOPE = Int32
WCS_PROFILE_MANAGEMENT_SCOPE_SYSTEM_WIDE = 0
WCS_PROFILE_MANAGEMENT_SCOPE_CURRENT_USER = 1
def _define_PCMSCALLBACKW():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.UI.ColorSystem.COLORMATCHSETUPW_head),win32more.Foundation.LPARAM, use_last_error=False)
def _define_PCMSCALLBACKA():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.UI.ColorSystem.COLORMATCHSETUPA_head),win32more.Foundation.LPARAM, use_last_error=False)
def _define_COLORMATCHSETUPW_head():
    class COLORMATCHSETUPW(Structure):
        pass
    return COLORMATCHSETUPW
def _define_COLORMATCHSETUPW():
    COLORMATCHSETUPW = win32more.UI.ColorSystem.COLORMATCHSETUPW_head
    COLORMATCHSETUPW._fields_ = [
        ("dwSize", UInt32),
        ("dwVersion", UInt32),
        ("dwFlags", UInt32),
        ("hwndOwner", win32more.Foundation.HWND),
        ("pSourceName", win32more.Foundation.PWSTR),
        ("pDisplayName", win32more.Foundation.PWSTR),
        ("pPrinterName", win32more.Foundation.PWSTR),
        ("dwRenderIntent", UInt32),
        ("dwProofingIntent", UInt32),
        ("pMonitorProfile", win32more.Foundation.PWSTR),
        ("ccMonitorProfile", UInt32),
        ("pPrinterProfile", win32more.Foundation.PWSTR),
        ("ccPrinterProfile", UInt32),
        ("pTargetProfile", win32more.Foundation.PWSTR),
        ("ccTargetProfile", UInt32),
        ("lpfnHook", win32more.UI.WindowsAndMessaging.DLGPROC),
        ("lParam", win32more.Foundation.LPARAM),
        ("lpfnApplyCallback", win32more.UI.ColorSystem.PCMSCALLBACKW),
        ("lParamApplyCallback", win32more.Foundation.LPARAM),
    ]
    return COLORMATCHSETUPW
def _define_COLORMATCHSETUPA_head():
    class COLORMATCHSETUPA(Structure):
        pass
    return COLORMATCHSETUPA
def _define_COLORMATCHSETUPA():
    COLORMATCHSETUPA = win32more.UI.ColorSystem.COLORMATCHSETUPA_head
    COLORMATCHSETUPA._fields_ = [
        ("dwSize", UInt32),
        ("dwVersion", UInt32),
        ("dwFlags", UInt32),
        ("hwndOwner", win32more.Foundation.HWND),
        ("pSourceName", win32more.Foundation.PSTR),
        ("pDisplayName", win32more.Foundation.PSTR),
        ("pPrinterName", win32more.Foundation.PSTR),
        ("dwRenderIntent", UInt32),
        ("dwProofingIntent", UInt32),
        ("pMonitorProfile", win32more.Foundation.PSTR),
        ("ccMonitorProfile", UInt32),
        ("pPrinterProfile", win32more.Foundation.PSTR),
        ("ccPrinterProfile", UInt32),
        ("pTargetProfile", win32more.Foundation.PSTR),
        ("ccTargetProfile", UInt32),
        ("lpfnHook", win32more.UI.WindowsAndMessaging.DLGPROC),
        ("lParam", win32more.Foundation.LPARAM),
        ("lpfnApplyCallback", win32more.UI.ColorSystem.PCMSCALLBACKA),
        ("lParamApplyCallback", win32more.Foundation.LPARAM),
    ]
    return COLORMATCHSETUPA
def _define_WCS_DEVICE_VCGT_CAPABILITIES_head():
    class WCS_DEVICE_VCGT_CAPABILITIES(Structure):
        pass
    return WCS_DEVICE_VCGT_CAPABILITIES
def _define_WCS_DEVICE_VCGT_CAPABILITIES():
    WCS_DEVICE_VCGT_CAPABILITIES = win32more.UI.ColorSystem.WCS_DEVICE_VCGT_CAPABILITIES_head
    WCS_DEVICE_VCGT_CAPABILITIES._fields_ = [
        ("Size", UInt32),
        ("SupportsVcgt", win32more.Foundation.BOOL),
    ]
    return WCS_DEVICE_VCGT_CAPABILITIES
def _define_WCS_DEVICE_MHC2_CAPABILITIES_head():
    class WCS_DEVICE_MHC2_CAPABILITIES(Structure):
        pass
    return WCS_DEVICE_MHC2_CAPABILITIES
def _define_WCS_DEVICE_MHC2_CAPABILITIES():
    WCS_DEVICE_MHC2_CAPABILITIES = win32more.UI.ColorSystem.WCS_DEVICE_MHC2_CAPABILITIES_head
    WCS_DEVICE_MHC2_CAPABILITIES._fields_ = [
        ("Size", UInt32),
        ("SupportsMhc2", win32more.Foundation.BOOL),
        ("RegammaLutEntryCount", UInt32),
        ("CscXyzMatrixRows", UInt32),
        ("CscXyzMatrixColumns", UInt32),
    ]
    return WCS_DEVICE_MHC2_CAPABILITIES
WCS_DEVICE_CAPABILITIES_TYPE = Int32
WCS_DEVICE_CAPABILITIES_TYPE_VideoCardGammaTable = 1
WCS_DEVICE_CAPABILITIES_TYPE_MicrosoftHardwareColorV2 = 2
def _define_SetICMMode():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,Int32, use_last_error=False)(("SetICMMode", windll["GDI32"]), ((1, 'hdc'),(1, 'mode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CheckColorsInGamut():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Graphics.Gdi.RGBTRIPLE),c_void_p,UInt32, use_last_error=False)(("CheckColorsInGamut", windll["GDI32"]), ((1, 'hdc'),(1, 'lpRGBTriple'),(1, 'dlpBuffer'),(1, 'nCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetColorSpace():
    try:
        return WINFUNCTYPE(win32more.UI.ColorSystem.HCOLORSPACE,win32more.Graphics.Gdi.HDC, use_last_error=False)(("GetColorSpace", windll["GDI32"]), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetLogColorSpaceA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.ColorSystem.HCOLORSPACE,POINTER(win32more.UI.ColorSystem.LOGCOLORSPACEA_head),UInt32, use_last_error=False)(("GetLogColorSpaceA", windll["GDI32"]), ((1, 'hColorSpace'),(1, 'lpBuffer'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetLogColorSpaceW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.ColorSystem.HCOLORSPACE,POINTER(win32more.UI.ColorSystem.LOGCOLORSPACEW_head),UInt32, use_last_error=False)(("GetLogColorSpaceW", windll["GDI32"]), ((1, 'hColorSpace'),(1, 'lpBuffer'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetLogColorSpace():
    return win32more.UI.ColorSystem.GetLogColorSpaceW
def _define_CreateColorSpaceA():
    try:
        return WINFUNCTYPE(win32more.UI.ColorSystem.HCOLORSPACE,POINTER(win32more.UI.ColorSystem.LOGCOLORSPACEA_head), use_last_error=False)(("CreateColorSpaceA", windll["GDI32"]), ((1, 'lplcs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateColorSpaceW():
    try:
        return WINFUNCTYPE(win32more.UI.ColorSystem.HCOLORSPACE,POINTER(win32more.UI.ColorSystem.LOGCOLORSPACEW_head), use_last_error=False)(("CreateColorSpaceW", windll["GDI32"]), ((1, 'lplcs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateColorSpace():
    return win32more.UI.ColorSystem.CreateColorSpaceW
def _define_SetColorSpace():
    try:
        return WINFUNCTYPE(win32more.UI.ColorSystem.HCOLORSPACE,win32more.Graphics.Gdi.HDC,win32more.UI.ColorSystem.HCOLORSPACE, use_last_error=False)(("SetColorSpace", windll["GDI32"]), ((1, 'hdc'),(1, 'hcs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteColorSpace():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.ColorSystem.HCOLORSPACE, use_last_error=False)(("DeleteColorSpace", windll["GDI32"]), ((1, 'hcs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetICMProfileA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(UInt32),POINTER(Byte), use_last_error=False)(("GetICMProfileA", windll["GDI32"]), ((1, 'hdc'),(1, 'pBufSize'),(1, 'pszFilename'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetICMProfileW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(UInt32),POINTER(Char), use_last_error=False)(("GetICMProfileW", windll["GDI32"]), ((1, 'hdc'),(1, 'pBufSize'),(1, 'pszFilename'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetICMProfile():
    return win32more.UI.ColorSystem.GetICMProfileW
def _define_SetICMProfileA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,win32more.Foundation.PSTR, use_last_error=False)(("SetICMProfileA", windll["GDI32"]), ((1, 'hdc'),(1, 'lpFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetICMProfileW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,win32more.Foundation.PWSTR, use_last_error=False)(("SetICMProfileW", windll["GDI32"]), ((1, 'hdc'),(1, 'lpFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetICMProfile():
    return win32more.UI.ColorSystem.SetICMProfileW
def _define_GetDeviceGammaRamp():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,c_void_p, use_last_error=False)(("GetDeviceGammaRamp", windll["GDI32"]), ((1, 'hdc'),(1, 'lpRamp'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetDeviceGammaRamp():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,c_void_p, use_last_error=False)(("SetDeviceGammaRamp", windll["GDI32"]), ((1, 'hdc'),(1, 'lpRamp'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ColorMatchToTarget():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HDC,win32more.UI.ColorSystem.COLOR_MATCH_TO_TARGET_ACTION, use_last_error=False)(("ColorMatchToTarget", windll["GDI32"]), ((1, 'hdc'),(1, 'hdcTarget'),(1, 'action'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumICMProfilesA():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,win32more.UI.ColorSystem.ICMENUMPROCA,win32more.Foundation.LPARAM, use_last_error=False)(("EnumICMProfilesA", windll["GDI32"]), ((1, 'hdc'),(1, 'proc'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumICMProfilesW():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,win32more.UI.ColorSystem.ICMENUMPROCW,win32more.Foundation.LPARAM, use_last_error=False)(("EnumICMProfilesW", windll["GDI32"]), ((1, 'hdc'),(1, 'proc'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumICMProfiles():
    return win32more.UI.ColorSystem.EnumICMProfilesW
def _define_UpdateICMRegKeyA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.UI.ColorSystem.ICM_COMMAND, use_last_error=False)(("UpdateICMRegKeyA", windll["GDI32"]), ((1, 'reserved'),(1, 'lpszCMID'),(1, 'lpszFileName'),(1, 'command'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UpdateICMRegKeyW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.UI.ColorSystem.ICM_COMMAND, use_last_error=False)(("UpdateICMRegKeyW", windll["GDI32"]), ((1, 'reserved'),(1, 'lpszCMID'),(1, 'lpszFileName'),(1, 'command'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UpdateICMRegKey():
    return win32more.UI.ColorSystem.UpdateICMRegKeyW
def _define_ColorCorrectPalette():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HPALETTE,UInt32,UInt32, use_last_error=False)(("ColorCorrectPalette", windll["GDI32"]), ((1, 'hdc'),(1, 'hPal'),(1, 'deFirst'),(1, 'num'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenColorProfileA():
    try:
        return WINFUNCTYPE(IntPtr,POINTER(win32more.UI.ColorSystem.PROFILE_head),UInt32,UInt32,UInt32, use_last_error=False)(("OpenColorProfileA", windll["mscms"]), ((1, 'pProfile'),(1, 'dwDesiredAccess'),(1, 'dwShareMode'),(1, 'dwCreationMode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenColorProfileW():
    try:
        return WINFUNCTYPE(IntPtr,POINTER(win32more.UI.ColorSystem.PROFILE_head),UInt32,UInt32,UInt32, use_last_error=False)(("OpenColorProfileW", windll["mscms"]), ((1, 'pProfile'),(1, 'dwDesiredAccess'),(1, 'dwShareMode'),(1, 'dwCreationMode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenColorProfile():
    return win32more.UI.ColorSystem.OpenColorProfileW
def _define_CloseColorProfile():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr, use_last_error=False)(("CloseColorProfile", windll["mscms"]), ((1, 'hProfile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetColorProfileFromHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,c_char_p_no,POINTER(UInt32), use_last_error=False)(("GetColorProfileFromHandle", windll["mscms"]), ((1, 'hProfile'),(1, 'pProfile'),(1, 'pcbProfile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsColorProfileValid():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("IsColorProfileValid", windll["mscms"]), ((1, 'hProfile'),(1, 'pbValid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateProfileFromLogColorSpaceA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.UI.ColorSystem.LOGCOLORSPACEA_head),POINTER(c_char_p_no), use_last_error=False)(("CreateProfileFromLogColorSpaceA", windll["mscms"]), ((1, 'pLogColorSpace'),(1, 'pProfile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateProfileFromLogColorSpaceW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.UI.ColorSystem.LOGCOLORSPACEW_head),POINTER(c_char_p_no), use_last_error=False)(("CreateProfileFromLogColorSpaceW", windll["mscms"]), ((1, 'pLogColorSpace'),(1, 'pProfile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateProfileFromLogColorSpace():
    return win32more.UI.ColorSystem.CreateProfileFromLogColorSpaceW
def _define_GetCountColorProfileElements():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,POINTER(UInt32), use_last_error=False)(("GetCountColorProfileElements", windll["mscms"]), ((1, 'hProfile'),(1, 'pnElementCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetColorProfileHeader():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,POINTER(win32more.UI.ColorSystem.PROFILEHEADER_head), use_last_error=False)(("GetColorProfileHeader", windll["mscms"]), ((1, 'hProfile'),(1, 'pHeader'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetColorProfileElementTag():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,UInt32,POINTER(UInt32), use_last_error=False)(("GetColorProfileElementTag", windll["mscms"]), ((1, 'hProfile'),(1, 'dwIndex'),(1, 'pTag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsColorProfileTagPresent():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,UInt32,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("IsColorProfileTagPresent", windll["mscms"]), ((1, 'hProfile'),(1, 'tag'),(1, 'pbPresent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetColorProfileElement():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,UInt32,UInt32,POINTER(UInt32),c_void_p,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("GetColorProfileElement", windll["mscms"]), ((1, 'hProfile'),(1, 'tag'),(1, 'dwOffset'),(1, 'pcbElement'),(1, 'pElement'),(1, 'pbReference'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetColorProfileHeader():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,POINTER(win32more.UI.ColorSystem.PROFILEHEADER_head), use_last_error=False)(("SetColorProfileHeader", windll["mscms"]), ((1, 'hProfile'),(1, 'pHeader'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetColorProfileElementSize():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,UInt32,UInt32, use_last_error=False)(("SetColorProfileElementSize", windll["mscms"]), ((1, 'hProfile'),(1, 'tagType'),(1, 'pcbElement'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetColorProfileElement():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,UInt32,UInt32,POINTER(UInt32),POINTER(Void), use_last_error=False)(("SetColorProfileElement", windll["mscms"]), ((1, 'hProfile'),(1, 'tag'),(1, 'dwOffset'),(1, 'pcbElement'),(1, 'pElement'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetColorProfileElementReference():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,UInt32,UInt32, use_last_error=False)(("SetColorProfileElementReference", windll["mscms"]), ((1, 'hProfile'),(1, 'newTag'),(1, 'refTag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPS2ColorSpaceArray():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,UInt32,UInt32,c_char_p_no,POINTER(UInt32),POINTER(win32more.Foundation.BOOL), use_last_error=False)(("GetPS2ColorSpaceArray", windll["mscms"]), ((1, 'hProfile'),(1, 'dwIntent'),(1, 'dwCSAType'),(1, 'pPS2ColorSpaceArray'),(1, 'pcbPS2ColorSpaceArray'),(1, 'pbBinary'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPS2ColorRenderingIntent():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,UInt32,c_char_p_no,POINTER(UInt32), use_last_error=False)(("GetPS2ColorRenderingIntent", windll["mscms"]), ((1, 'hProfile'),(1, 'dwIntent'),(1, 'pBuffer'),(1, 'pcbPS2ColorRenderingIntent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPS2ColorRenderingDictionary():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,UInt32,c_char_p_no,POINTER(UInt32),POINTER(win32more.Foundation.BOOL), use_last_error=False)(("GetPS2ColorRenderingDictionary", windll["mscms"]), ((1, 'hProfile'),(1, 'dwIntent'),(1, 'pPS2ColorRenderingDictionary'),(1, 'pcbPS2ColorRenderingDictionary'),(1, 'pbBinary'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNamedProfileInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,POINTER(win32more.UI.ColorSystem.NAMED_PROFILE_INFO_head), use_last_error=False)(("GetNamedProfileInfo", windll["mscms"]), ((1, 'hProfile'),(1, 'pNamedProfileInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ConvertColorNameToIndex():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,POINTER(POINTER(SByte)),POINTER(UInt32),UInt32, use_last_error=False)(("ConvertColorNameToIndex", windll["mscms"]), ((1, 'hProfile'),(1, 'paColorName'),(1, 'paIndex'),(1, 'dwCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ConvertIndexToColorName():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,POINTER(UInt32),POINTER(POINTER(SByte)),UInt32, use_last_error=False)(("ConvertIndexToColorName", windll["mscms"]), ((1, 'hProfile'),(1, 'paIndex'),(1, 'paColorName'),(1, 'dwCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateDeviceLinkProfile():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(IntPtr),UInt32,POINTER(UInt32),UInt32,UInt32,POINTER(c_char_p_no),UInt32, use_last_error=False)(("CreateDeviceLinkProfile", windll["mscms"]), ((1, 'hProfile'),(1, 'nProfiles'),(1, 'padwIntent'),(1, 'nIntents'),(1, 'dwFlags'),(1, 'pProfileData'),(1, 'indexPreferredCMM'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateColorTransformA():
    try:
        return WINFUNCTYPE(IntPtr,POINTER(win32more.UI.ColorSystem.LOGCOLORSPACEA_head),IntPtr,IntPtr,UInt32, use_last_error=False)(("CreateColorTransformA", windll["mscms"]), ((1, 'pLogColorSpace'),(1, 'hDestProfile'),(1, 'hTargetProfile'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateColorTransformW():
    try:
        return WINFUNCTYPE(IntPtr,POINTER(win32more.UI.ColorSystem.LOGCOLORSPACEW_head),IntPtr,IntPtr,UInt32, use_last_error=False)(("CreateColorTransformW", windll["mscms"]), ((1, 'pLogColorSpace'),(1, 'hDestProfile'),(1, 'hTargetProfile'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateColorTransform():
    return win32more.UI.ColorSystem.CreateColorTransformW
def _define_CreateMultiProfileTransform():
    try:
        return WINFUNCTYPE(IntPtr,POINTER(IntPtr),UInt32,POINTER(UInt32),UInt32,UInt32,UInt32, use_last_error=False)(("CreateMultiProfileTransform", windll["mscms"]), ((1, 'pahProfiles'),(1, 'nProfiles'),(1, 'padwIntent'),(1, 'nIntents'),(1, 'dwFlags'),(1, 'indexPreferredCMM'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteColorTransform():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr, use_last_error=False)(("DeleteColorTransform", windll["mscms"]), ((1, 'hxform'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TranslateBitmapBits():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,c_void_p,win32more.UI.ColorSystem.BMFORMAT,UInt32,UInt32,UInt32,c_void_p,win32more.UI.ColorSystem.BMFORMAT,UInt32,win32more.UI.ColorSystem.LPBMCALLBACKFN,win32more.Foundation.LPARAM, use_last_error=False)(("TranslateBitmapBits", windll["mscms"]), ((1, 'hColorTransform'),(1, 'pSrcBits'),(1, 'bmInput'),(1, 'dwWidth'),(1, 'dwHeight'),(1, 'dwInputStride'),(1, 'pDestBits'),(1, 'bmOutput'),(1, 'dwOutputStride'),(1, 'pfnCallBack'),(1, 'ulCallbackData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CheckBitmapBits():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,c_void_p,win32more.UI.ColorSystem.BMFORMAT,UInt32,UInt32,UInt32,c_char_p_no,win32more.UI.ColorSystem.LPBMCALLBACKFN,win32more.Foundation.LPARAM, use_last_error=False)(("CheckBitmapBits", windll["mscms"]), ((1, 'hColorTransform'),(1, 'pSrcBits'),(1, 'bmInput'),(1, 'dwWidth'),(1, 'dwHeight'),(1, 'dwStride'),(1, 'paResult'),(1, 'pfnCallback'),(1, 'lpCallbackData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TranslateColors():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,POINTER(win32more.UI.ColorSystem.COLOR),UInt32,win32more.UI.ColorSystem.COLORTYPE,POINTER(win32more.UI.ColorSystem.COLOR),win32more.UI.ColorSystem.COLORTYPE, use_last_error=False)(("TranslateColors", windll["mscms"]), ((1, 'hColorTransform'),(1, 'paInputColors'),(1, 'nColors'),(1, 'ctInput'),(1, 'paOutputColors'),(1, 'ctOutput'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CheckColors():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,POINTER(win32more.UI.ColorSystem.COLOR),UInt32,win32more.UI.ColorSystem.COLORTYPE,POINTER(Byte), use_last_error=False)(("CheckColors", windll["mscms"]), ((1, 'hColorTransform'),(1, 'paInputColors'),(1, 'nColors'),(1, 'ctInput'),(1, 'paResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCMMInfo():
    try:
        return WINFUNCTYPE(UInt32,IntPtr,UInt32, use_last_error=False)(("GetCMMInfo", windll["mscms"]), ((1, 'hColorTransform'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterCMMA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR, use_last_error=False)(("RegisterCMMA", windll["mscms"]), ((1, 'pMachineName'),(1, 'cmmID'),(1, 'pCMMdll'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterCMMW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("RegisterCMMW", windll["mscms"]), ((1, 'pMachineName'),(1, 'cmmID'),(1, 'pCMMdll'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterCMM():
    return win32more.UI.ColorSystem.RegisterCMMW
def _define_UnregisterCMMA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,UInt32, use_last_error=False)(("UnregisterCMMA", windll["mscms"]), ((1, 'pMachineName'),(1, 'cmmID'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnregisterCMMW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("UnregisterCMMW", windll["mscms"]), ((1, 'pMachineName'),(1, 'cmmID'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnregisterCMM():
    return win32more.UI.ColorSystem.UnregisterCMMW
def _define_SelectCMM():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32, use_last_error=False)(("SelectCMM", windll["mscms"]), ((1, 'dwCMMType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetColorDirectoryA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt32), use_last_error=False)(("GetColorDirectoryA", windll["mscms"]), ((1, 'pMachineName'),(1, 'pBuffer'),(1, 'pdwSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetColorDirectoryW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("GetColorDirectoryW", windll["mscms"]), ((1, 'pMachineName'),(1, 'pBuffer'),(1, 'pdwSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetColorDirectory():
    return win32more.UI.ColorSystem.GetColorDirectoryW
def _define_InstallColorProfileA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("InstallColorProfileA", windll["mscms"]), ((1, 'pMachineName'),(1, 'pProfileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InstallColorProfileW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("InstallColorProfileW", windll["mscms"]), ((1, 'pMachineName'),(1, 'pProfileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InstallColorProfile():
    return win32more.UI.ColorSystem.InstallColorProfileW
def _define_UninstallColorProfileA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.BOOL, use_last_error=False)(("UninstallColorProfileA", windll["mscms"]), ((1, 'pMachineName'),(1, 'pProfileName'),(1, 'bDelete'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UninstallColorProfileW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.BOOL, use_last_error=False)(("UninstallColorProfileW", windll["mscms"]), ((1, 'pMachineName'),(1, 'pProfileName'),(1, 'bDelete'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UninstallColorProfile():
    return win32more.UI.ColorSystem.UninstallColorProfileW
def _define_EnumColorProfilesA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,POINTER(win32more.UI.ColorSystem.ENUMTYPEA_head),c_char_p_no,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("EnumColorProfilesA", windll["mscms"]), ((1, 'pMachineName'),(1, 'pEnumRecord'),(1, 'pEnumerationBuffer'),(1, 'pdwSizeOfEnumerationBuffer'),(1, 'pnProfiles'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumColorProfilesW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(win32more.UI.ColorSystem.ENUMTYPEW_head),c_char_p_no,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("EnumColorProfilesW", windll["mscms"]), ((1, 'pMachineName'),(1, 'pEnumRecord'),(1, 'pEnumerationBuffer'),(1, 'pdwSizeOfEnumerationBuffer'),(1, 'pnProfiles'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumColorProfiles():
    return win32more.UI.ColorSystem.EnumColorProfilesW
def _define_SetStandardColorSpaceProfileA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR, use_last_error=False)(("SetStandardColorSpaceProfileA", windll["mscms"]), ((1, 'pMachineName'),(1, 'dwProfileID'),(1, 'pProfilename'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetStandardColorSpaceProfileW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("SetStandardColorSpaceProfileW", windll["mscms"]), ((1, 'pMachineName'),(1, 'dwProfileID'),(1, 'pProfileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetStandardColorSpaceProfile():
    return win32more.UI.ColorSystem.SetStandardColorSpaceProfileW
def _define_GetStandardColorSpaceProfileA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(UInt32), use_last_error=False)(("GetStandardColorSpaceProfileA", windll["mscms"]), ((1, 'pMachineName'),(1, 'dwSCS'),(1, 'pBuffer'),(1, 'pcbSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetStandardColorSpaceProfileW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(("GetStandardColorSpaceProfileW", windll["mscms"]), ((1, 'pMachineName'),(1, 'dwSCS'),(1, 'pBuffer'),(1, 'pcbSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetStandardColorSpaceProfile():
    return win32more.UI.ColorSystem.GetStandardColorSpaceProfileW
def _define_AssociateColorProfileWithDeviceA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("AssociateColorProfileWithDeviceA", windll["mscms"]), ((1, 'pMachineName'),(1, 'pProfileName'),(1, 'pDeviceName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AssociateColorProfileWithDeviceW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("AssociateColorProfileWithDeviceW", windll["mscms"]), ((1, 'pMachineName'),(1, 'pProfileName'),(1, 'pDeviceName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AssociateColorProfileWithDevice():
    return win32more.UI.ColorSystem.AssociateColorProfileWithDeviceW
def _define_DisassociateColorProfileFromDeviceA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("DisassociateColorProfileFromDeviceA", windll["mscms"]), ((1, 'pMachineName'),(1, 'pProfileName'),(1, 'pDeviceName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DisassociateColorProfileFromDeviceW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("DisassociateColorProfileFromDeviceW", windll["mscms"]), ((1, 'pMachineName'),(1, 'pProfileName'),(1, 'pDeviceName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DisassociateColorProfileFromDevice():
    return win32more.UI.ColorSystem.DisassociateColorProfileFromDeviceW
def _define_SetupColorMatchingW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.UI.ColorSystem.COLORMATCHSETUPW_head), use_last_error=False)(("SetupColorMatchingW", windll["ICMUI"]), ((1, 'pcms'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetupColorMatching():
    return win32more.UI.ColorSystem.SetupColorMatchingW
def _define_SetupColorMatchingA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.UI.ColorSystem.COLORMATCHSETUPA_head), use_last_error=False)(("SetupColorMatchingA", windll["ICMUI"]), ((1, 'pcms'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WcsAssociateColorProfileWithDevice():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("WcsAssociateColorProfileWithDevice", windll["mscms"]), ((1, 'scope'),(1, 'pProfileName'),(1, 'pDeviceName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WcsDisassociateColorProfileFromDevice():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("WcsDisassociateColorProfileFromDevice", windll["mscms"]), ((1, 'scope'),(1, 'pProfileName'),(1, 'pDeviceName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WcsEnumColorProfilesSize():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE,POINTER(win32more.UI.ColorSystem.ENUMTYPEW_head),POINTER(UInt32), use_last_error=False)(("WcsEnumColorProfilesSize", windll["mscms"]), ((1, 'scope'),(1, 'pEnumRecord'),(1, 'pdwSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WcsEnumColorProfiles():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE,POINTER(win32more.UI.ColorSystem.ENUMTYPEW_head),c_char_p_no,UInt32,POINTER(UInt32), use_last_error=False)(("WcsEnumColorProfiles", windll["mscms"]), ((1, 'scope'),(1, 'pEnumRecord'),(1, 'pBuffer'),(1, 'dwSize'),(1, 'pnProfiles'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WcsGetDefaultColorProfileSize():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE,win32more.Foundation.PWSTR,win32more.UI.ColorSystem.COLORPROFILETYPE,win32more.UI.ColorSystem.COLORPROFILESUBTYPE,UInt32,POINTER(UInt32), use_last_error=False)(("WcsGetDefaultColorProfileSize", windll["mscms"]), ((1, 'scope'),(1, 'pDeviceName'),(1, 'cptColorProfileType'),(1, 'cpstColorProfileSubType'),(1, 'dwProfileID'),(1, 'pcbProfileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WcsGetDefaultColorProfile():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE,win32more.Foundation.PWSTR,win32more.UI.ColorSystem.COLORPROFILETYPE,win32more.UI.ColorSystem.COLORPROFILESUBTYPE,UInt32,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("WcsGetDefaultColorProfile", windll["mscms"]), ((1, 'scope'),(1, 'pDeviceName'),(1, 'cptColorProfileType'),(1, 'cpstColorProfileSubType'),(1, 'dwProfileID'),(1, 'cbProfileName'),(1, 'pProfileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WcsSetDefaultColorProfile():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE,win32more.Foundation.PWSTR,win32more.UI.ColorSystem.COLORPROFILETYPE,win32more.UI.ColorSystem.COLORPROFILESUBTYPE,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("WcsSetDefaultColorProfile", windll["mscms"]), ((1, 'scope'),(1, 'pDeviceName'),(1, 'cptColorProfileType'),(1, 'cpstColorProfileSubType'),(1, 'dwProfileID'),(1, 'pProfileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WcsSetDefaultRenderingIntent():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE,UInt32, use_last_error=False)(("WcsSetDefaultRenderingIntent", windll["mscms"]), ((1, 'scope'),(1, 'dwRenderingIntent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WcsGetDefaultRenderingIntent():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE,POINTER(UInt32), use_last_error=False)(("WcsGetDefaultRenderingIntent", windll["mscms"]), ((1, 'scope'),(1, 'pdwRenderingIntent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WcsGetUsePerUserProfiles():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("WcsGetUsePerUserProfiles", windll["mscms"]), ((1, 'pDeviceName'),(1, 'dwDeviceClass'),(1, 'pUsePerUserProfiles'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WcsSetUsePerUserProfiles():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.BOOL, use_last_error=False)(("WcsSetUsePerUserProfiles", windll["mscms"]), ((1, 'pDeviceName'),(1, 'dwDeviceClass'),(1, 'usePerUserProfiles'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WcsTranslateColors():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,UInt32,UInt32,win32more.UI.ColorSystem.COLORDATATYPE,UInt32,c_void_p,UInt32,win32more.UI.ColorSystem.COLORDATATYPE,UInt32,c_void_p, use_last_error=False)(("WcsTranslateColors", windll["mscms"]), ((1, 'hColorTransform'),(1, 'nColors'),(1, 'nInputChannels'),(1, 'cdtInput'),(1, 'cbInput'),(1, 'pInputData'),(1, 'nOutputChannels'),(1, 'cdtOutput'),(1, 'cbOutput'),(1, 'pOutputData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WcsCheckColors():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,UInt32,UInt32,win32more.UI.ColorSystem.COLORDATATYPE,UInt32,c_void_p,POINTER(Byte), use_last_error=False)(("WcsCheckColors", windll["mscms"]), ((1, 'hColorTransform'),(1, 'nColors'),(1, 'nInputChannels'),(1, 'cdtInput'),(1, 'cbInput'),(1, 'pInputData'),(1, 'paResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CMCheckColors():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,POINTER(win32more.UI.ColorSystem.COLOR),UInt32,win32more.UI.ColorSystem.COLORTYPE,POINTER(Byte), use_last_error=False)(("CMCheckColors", windll["ICM32"]), ((1, 'hcmTransform'),(1, 'lpaInputColors'),(1, 'nColors'),(1, 'ctInput'),(1, 'lpaResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CMCheckRGBs():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,c_void_p,win32more.UI.ColorSystem.BMFORMAT,UInt32,UInt32,UInt32,c_char_p_no,win32more.UI.ColorSystem.LPBMCALLBACKFN,win32more.Foundation.LPARAM, use_last_error=False)(("CMCheckRGBs", windll["ICM32"]), ((1, 'hcmTransform'),(1, 'lpSrcBits'),(1, 'bmInput'),(1, 'dwWidth'),(1, 'dwHeight'),(1, 'dwStride'),(1, 'lpaResult'),(1, 'pfnCallback'),(1, 'ulCallbackData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CMConvertColorNameToIndex():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,POINTER(POINTER(SByte)),POINTER(UInt32),UInt32, use_last_error=False)(("CMConvertColorNameToIndex", windll["ICM32"]), ((1, 'hProfile'),(1, 'paColorName'),(1, 'paIndex'),(1, 'dwCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CMConvertIndexToColorName():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,POINTER(UInt32),POINTER(POINTER(SByte)),UInt32, use_last_error=False)(("CMConvertIndexToColorName", windll["ICM32"]), ((1, 'hProfile'),(1, 'paIndex'),(1, 'paColorName'),(1, 'dwCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CMCreateDeviceLinkProfile():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(IntPtr),UInt32,POINTER(UInt32),UInt32,UInt32,POINTER(c_char_p_no), use_last_error=False)(("CMCreateDeviceLinkProfile", windll["ICM32"]), ((1, 'pahProfiles'),(1, 'nProfiles'),(1, 'padwIntents'),(1, 'nIntents'),(1, 'dwFlags'),(1, 'lpProfileData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CMCreateMultiProfileTransform():
    try:
        return WINFUNCTYPE(IntPtr,POINTER(IntPtr),UInt32,POINTER(UInt32),UInt32,UInt32, use_last_error=False)(("CMCreateMultiProfileTransform", windll["ICM32"]), ((1, 'pahProfiles'),(1, 'nProfiles'),(1, 'padwIntents'),(1, 'nIntents'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CMCreateProfileW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.UI.ColorSystem.LOGCOLORSPACEW_head),POINTER(c_void_p), use_last_error=False)(("CMCreateProfileW", windll["ICM32"]), ((1, 'lpColorSpace'),(1, 'lpProfileData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CMCreateTransform():
    try:
        return WINFUNCTYPE(IntPtr,POINTER(win32more.UI.ColorSystem.LOGCOLORSPACEA_head),c_void_p,c_void_p, use_last_error=False)(("CMCreateTransform", windll["ICM32"]), ((1, 'lpColorSpace'),(1, 'lpDevCharacter'),(1, 'lpTargetDevCharacter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CMCreateTransformW():
    try:
        return WINFUNCTYPE(IntPtr,POINTER(win32more.UI.ColorSystem.LOGCOLORSPACEW_head),c_void_p,c_void_p, use_last_error=False)(("CMCreateTransformW", windll["ICM32"]), ((1, 'lpColorSpace'),(1, 'lpDevCharacter'),(1, 'lpTargetDevCharacter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CMCreateTransformExt():
    try:
        return WINFUNCTYPE(IntPtr,POINTER(win32more.UI.ColorSystem.LOGCOLORSPACEA_head),c_void_p,c_void_p,UInt32, use_last_error=False)(("CMCreateTransformExt", windll["ICM32"]), ((1, 'lpColorSpace'),(1, 'lpDevCharacter'),(1, 'lpTargetDevCharacter'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CMCheckColorsInGamut():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,POINTER(win32more.Graphics.Gdi.RGBTRIPLE),c_char_p_no,UInt32, use_last_error=False)(("CMCheckColorsInGamut", windll["ICM32"]), ((1, 'hcmTransform'),(1, 'lpaRGBTriple'),(1, 'lpaResult'),(1, 'nCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CMCreateProfile():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.UI.ColorSystem.LOGCOLORSPACEA_head),POINTER(c_void_p), use_last_error=False)(("CMCreateProfile", windll["ICM32"]), ((1, 'lpColorSpace'),(1, 'lpProfileData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CMTranslateRGB():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,UInt32,POINTER(UInt32),UInt32, use_last_error=False)(("CMTranslateRGB", windll["ICM32"]), ((1, 'hcmTransform'),(1, 'ColorRef'),(1, 'lpColorRef'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CMTranslateRGBs():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,c_void_p,win32more.UI.ColorSystem.BMFORMAT,UInt32,UInt32,UInt32,c_void_p,win32more.UI.ColorSystem.BMFORMAT,UInt32, use_last_error=False)(("CMTranslateRGBs", windll["ICM32"]), ((1, 'hcmTransform'),(1, 'lpSrcBits'),(1, 'bmInput'),(1, 'dwWidth'),(1, 'dwHeight'),(1, 'dwStride'),(1, 'lpDestBits'),(1, 'bmOutput'),(1, 'dwTranslateDirection'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CMCreateTransformExtW():
    try:
        return WINFUNCTYPE(IntPtr,POINTER(win32more.UI.ColorSystem.LOGCOLORSPACEW_head),c_void_p,c_void_p,UInt32, use_last_error=False)(("CMCreateTransformExtW", windll["ICM32"]), ((1, 'lpColorSpace'),(1, 'lpDevCharacter'),(1, 'lpTargetDevCharacter'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CMDeleteTransform():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr, use_last_error=False)(("CMDeleteTransform", windll["ICM32"]), ((1, 'hcmTransform'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CMGetInfo():
    try:
        return WINFUNCTYPE(UInt32,UInt32, use_last_error=False)(("CMGetInfo", windll["ICM32"]), ((1, 'dwInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CMGetNamedProfileInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,POINTER(win32more.UI.ColorSystem.NAMED_PROFILE_INFO_head), use_last_error=False)(("CMGetNamedProfileInfo", windll["ICM32"]), ((1, 'hProfile'),(1, 'pNamedProfileInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CMIsProfileValid():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,POINTER(Int32), use_last_error=False)(("CMIsProfileValid", windll["ICM32"]), ((1, 'hProfile'),(1, 'lpbValid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CMTranslateColors():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,POINTER(win32more.UI.ColorSystem.COLOR),UInt32,win32more.UI.ColorSystem.COLORTYPE,POINTER(win32more.UI.ColorSystem.COLOR),win32more.UI.ColorSystem.COLORTYPE, use_last_error=False)(("CMTranslateColors", windll["ICM32"]), ((1, 'hcmTransform'),(1, 'lpaInputColors'),(1, 'nColors'),(1, 'ctInput'),(1, 'lpaOutputColors'),(1, 'ctOutput'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CMTranslateRGBsExt():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,IntPtr,c_void_p,win32more.UI.ColorSystem.BMFORMAT,UInt32,UInt32,UInt32,c_void_p,win32more.UI.ColorSystem.BMFORMAT,UInt32,win32more.UI.ColorSystem.LPBMCALLBACKFN,win32more.Foundation.LPARAM, use_last_error=False)(("CMTranslateRGBsExt", windll["ICM32"]), ((1, 'hcmTransform'),(1, 'lpSrcBits'),(1, 'bmInput'),(1, 'dwWidth'),(1, 'dwHeight'),(1, 'dwInputStride'),(1, 'lpDestBits'),(1, 'bmOutput'),(1, 'dwOutputStride'),(1, 'lpfnCallback'),(1, 'ulCallbackData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WcsOpenColorProfileA():
    try:
        return WINFUNCTYPE(IntPtr,POINTER(win32more.UI.ColorSystem.PROFILE_head),POINTER(win32more.UI.ColorSystem.PROFILE_head),POINTER(win32more.UI.ColorSystem.PROFILE_head),UInt32,UInt32,UInt32,UInt32, use_last_error=False)(("WcsOpenColorProfileA", windll["mscms"]), ((1, 'pCDMPProfile'),(1, 'pCAMPProfile'),(1, 'pGMMPProfile'),(1, 'dwDesireAccess'),(1, 'dwShareMode'),(1, 'dwCreationMode'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WcsOpenColorProfileW():
    try:
        return WINFUNCTYPE(IntPtr,POINTER(win32more.UI.ColorSystem.PROFILE_head),POINTER(win32more.UI.ColorSystem.PROFILE_head),POINTER(win32more.UI.ColorSystem.PROFILE_head),UInt32,UInt32,UInt32,UInt32, use_last_error=False)(("WcsOpenColorProfileW", windll["mscms"]), ((1, 'pCDMPProfile'),(1, 'pCAMPProfile'),(1, 'pGMMPProfile'),(1, 'dwDesireAccess'),(1, 'dwShareMode'),(1, 'dwCreationMode'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WcsOpenColorProfile():
    return win32more.UI.ColorSystem.WcsOpenColorProfileW
def _define_WcsCreateIccProfile():
    try:
        return WINFUNCTYPE(IntPtr,IntPtr,UInt32, use_last_error=False)(("WcsCreateIccProfile", windll["mscms"]), ((1, 'hWcsProfile'),(1, 'dwOptions'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WcsGetCalibrationManagementState():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.BOOL), use_last_error=False)(("WcsGetCalibrationManagementState", windll["mscms"]), ((1, 'pbIsEnabled'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WcsSetCalibrationManagementState():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.BOOL, use_last_error=False)(("WcsSetCalibrationManagementState", windll["mscms"]), ((1, 'bIsEnabled'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ColorProfileAddDisplayAssociation():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE,win32more.Foundation.PWSTR,win32more.Foundation.LUID,UInt32,win32more.Foundation.BOOL,win32more.Foundation.BOOL, use_last_error=False)(("ColorProfileAddDisplayAssociation", windll["mscms"]), ((1, 'scope'),(1, 'profileName'),(1, 'targetAdapterID'),(1, 'sourceID'),(1, 'setAsDefault'),(1, 'associateAsAdvancedColor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ColorProfileRemoveDisplayAssociation():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE,win32more.Foundation.PWSTR,win32more.Foundation.LUID,UInt32,win32more.Foundation.BOOL, use_last_error=False)(("ColorProfileRemoveDisplayAssociation", windll["mscms"]), ((1, 'scope'),(1, 'profileName'),(1, 'targetAdapterID'),(1, 'sourceID'),(1, 'dissociateAdvancedColor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ColorProfileSetDisplayDefaultAssociation():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE,win32more.Foundation.PWSTR,win32more.UI.ColorSystem.COLORPROFILETYPE,win32more.UI.ColorSystem.COLORPROFILESUBTYPE,win32more.Foundation.LUID,UInt32, use_last_error=False)(("ColorProfileSetDisplayDefaultAssociation", windll["mscms"]), ((1, 'scope'),(1, 'profileName'),(1, 'profileType'),(1, 'profileSubType'),(1, 'targetAdapterID'),(1, 'sourceID'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ColorProfileGetDisplayList():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE,win32more.Foundation.LUID,UInt32,POINTER(POINTER(win32more.Foundation.PWSTR)),POINTER(UInt32), use_last_error=False)(("ColorProfileGetDisplayList", windll["mscms"]), ((1, 'scope'),(1, 'targetAdapterID'),(1, 'sourceID'),(1, 'profileList'),(1, 'profileCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ColorProfileGetDisplayDefault():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE,win32more.Foundation.LUID,UInt32,win32more.UI.ColorSystem.COLORPROFILETYPE,win32more.UI.ColorSystem.COLORPROFILESUBTYPE,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("ColorProfileGetDisplayDefault", windll["mscms"]), ((1, 'scope'),(1, 'targetAdapterID'),(1, 'sourceID'),(1, 'profileType'),(1, 'profileSubType'),(1, 'profileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ColorProfileGetDisplayUserScope():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.LUID,UInt32,POINTER(win32more.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE), use_last_error=False)(("ColorProfileGetDisplayUserScope", windll["mscms"]), ((1, 'targetAdapterID'),(1, 'sourceID'),(1, 'scope'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "CATID_WcsPlugin",
    "MAX_COLOR_CHANNELS",
    "INTENT_PERCEPTUAL",
    "INTENT_RELATIVE_COLORIMETRIC",
    "INTENT_SATURATION",
    "INTENT_ABSOLUTE_COLORIMETRIC",
    "FLAG_EMBEDDEDPROFILE",
    "FLAG_DEPENDENTONDATA",
    "FLAG_ENABLE_CHROMATIC_ADAPTATION",
    "ATTRIB_TRANSPARENCY",
    "ATTRIB_MATTE",
    "PROFILE_FILENAME",
    "PROFILE_MEMBUFFER",
    "PROFILE_READ",
    "PROFILE_READWRITE",
    "INDEX_DONT_CARE",
    "CMM_FROM_PROFILE",
    "ENUM_TYPE_VERSION",
    "ET_DEVICENAME",
    "ET_MEDIATYPE",
    "ET_DITHERMODE",
    "ET_RESOLUTION",
    "ET_CMMTYPE",
    "ET_CLASS",
    "ET_DATACOLORSPACE",
    "ET_CONNECTIONSPACE",
    "ET_SIGNATURE",
    "ET_PLATFORM",
    "ET_PROFILEFLAGS",
    "ET_MANUFACTURER",
    "ET_MODEL",
    "ET_ATTRIBUTES",
    "ET_RENDERINGINTENT",
    "ET_CREATOR",
    "ET_DEVICECLASS",
    "ET_STANDARDDISPLAYCOLOR",
    "ET_EXTENDEDDISPLAYCOLOR",
    "PROOF_MODE",
    "NORMAL_MODE",
    "BEST_MODE",
    "ENABLE_GAMUT_CHECKING",
    "USE_RELATIVE_COLORIMETRIC",
    "FAST_TRANSLATE",
    "PRESERVEBLACK",
    "WCS_ALWAYS",
    "SEQUENTIAL_TRANSFORM",
    "RESERVED",
    "CSA_A",
    "CSA_ABC",
    "CSA_DEF",
    "CSA_DEFG",
    "CSA_GRAY",
    "CSA_RGB",
    "CSA_CMYK",
    "CSA_Lab",
    "CMM_WIN_VERSION",
    "CMM_IDENT",
    "CMM_DRIVER_VERSION",
    "CMM_DLL_VERSION",
    "CMM_VERSION",
    "CMM_DESCRIPTION",
    "CMM_LOGOICON",
    "CMS_FORWARD",
    "CMS_BACKWARD",
    "COLOR_MATCH_VERSION",
    "CMS_DISABLEICM",
    "CMS_ENABLEPROOFING",
    "CMS_SETRENDERINTENT",
    "CMS_SETPROOFINTENT",
    "CMS_SETMONITORPROFILE",
    "CMS_SETPRINTERPROFILE",
    "CMS_SETTARGETPROFILE",
    "CMS_USEHOOK",
    "CMS_USEAPPLYCALLBACK",
    "CMS_USEDESCRIPTION",
    "CMS_DISABLEINTENT",
    "CMS_DISABLERENDERINTENT",
    "CMS_MONITOROVERFLOW",
    "CMS_PRINTEROVERFLOW",
    "CMS_TARGETOVERFLOW",
    "DONT_USE_EMBEDDED_WCS_PROFILES",
    "WCS_DEFAULT",
    "WCS_ICCONLY",
    "ICM_COMMAND",
    "ICM_ADDPROFILE",
    "ICM_DELETEPROFILE",
    "ICM_QUERYPROFILE",
    "ICM_SETDEFAULTPROFILE",
    "ICM_REGISTERICMATCHER",
    "ICM_UNREGISTERICMATCHER",
    "ICM_QUERYMATCH",
    "COLOR_MATCH_TO_TARGET_ACTION",
    "CS_ENABLE",
    "CS_DISABLE",
    "CS_DELETE_TRANSFORM",
    "HCOLORSPACE",
    "LOGCOLORSPACEA",
    "LOGCOLORSPACEW",
    "ICMENUMPROCA",
    "ICMENUMPROCW",
    "EMRCREATECOLORSPACE",
    "EMRCREATECOLORSPACEW",
    "XYZColorF",
    "JChColorF",
    "JabColorF",
    "GamutShellTriangle",
    "GamutShell",
    "PrimaryJabColors",
    "PrimaryXYZColors",
    "GamutBoundaryDescription",
    "BlackInformation",
    "IDeviceModelPlugIn",
    "IGamutMapModelPlugIn",
    "NAMED_PROFILE_INFO",
    "GRAYCOLOR",
    "RGBCOLOR",
    "CMYKCOLOR",
    "XYZCOLOR",
    "YxyCOLOR",
    "LabCOLOR",
    "GENERIC3CHANNEL",
    "NAMEDCOLOR",
    "HiFiCOLOR",
    "COLOR",
    "COLORTYPE",
    "COLOR_GRAY",
    "COLOR_RGB",
    "COLOR_XYZ",
    "COLOR_Yxy",
    "COLOR_Lab",
    "COLOR_3_CHANNEL",
    "COLOR_CMYK",
    "COLOR_5_CHANNEL",
    "COLOR_6_CHANNEL",
    "COLOR_7_CHANNEL",
    "COLOR_8_CHANNEL",
    "COLOR_NAMED",
    "COLORPROFILETYPE",
    "CPT_ICC",
    "CPT_DMP",
    "CPT_CAMP",
    "CPT_GMMP",
    "COLORPROFILESUBTYPE",
    "CPST_PERCEPTUAL",
    "CPST_RELATIVE_COLORIMETRIC",
    "CPST_SATURATION",
    "CPST_ABSOLUTE_COLORIMETRIC",
    "CPST_NONE",
    "CPST_RGB_WORKING_SPACE",
    "CPST_CUSTOM_WORKING_SPACE",
    "CPST_STANDARD_DISPLAY_COLOR_MODE",
    "CPST_EXTENDED_DISPLAY_COLOR_MODE",
    "COLORDATATYPE",
    "COLOR_BYTE",
    "COLOR_WORD",
    "COLOR_FLOAT",
    "COLOR_S2DOT13FIXED",
    "COLOR_10b_R10G10B10A2",
    "COLOR_10b_R10G10B10A2_XR",
    "COLOR_FLOAT16",
    "BMFORMAT",
    "BM_x555RGB",
    "BM_x555XYZ",
    "BM_x555Yxy",
    "BM_x555Lab",
    "BM_x555G3CH",
    "BM_RGBTRIPLETS",
    "BM_BGRTRIPLETS",
    "BM_XYZTRIPLETS",
    "BM_YxyTRIPLETS",
    "BM_LabTRIPLETS",
    "BM_G3CHTRIPLETS",
    "BM_5CHANNEL",
    "BM_6CHANNEL",
    "BM_7CHANNEL",
    "BM_8CHANNEL",
    "BM_GRAY",
    "BM_xRGBQUADS",
    "BM_xBGRQUADS",
    "BM_xG3CHQUADS",
    "BM_KYMCQUADS",
    "BM_CMYKQUADS",
    "BM_10b_RGB",
    "BM_10b_XYZ",
    "BM_10b_Yxy",
    "BM_10b_Lab",
    "BM_10b_G3CH",
    "BM_NAMED_INDEX",
    "BM_16b_RGB",
    "BM_16b_XYZ",
    "BM_16b_Yxy",
    "BM_16b_Lab",
    "BM_16b_G3CH",
    "BM_16b_GRAY",
    "BM_565RGB",
    "BM_32b_scRGB",
    "BM_32b_scARGB",
    "BM_S2DOT13FIXED_scRGB",
    "BM_S2DOT13FIXED_scARGB",
    "BM_R10G10B10A2",
    "BM_R10G10B10A2_XR",
    "BM_R16G16B16A16_FLOAT",
    "LPBMCALLBACKFN",
    "PROFILEHEADER",
    "PROFILE",
    "ENUMTYPEA",
    "ENUMTYPEW",
    "WCS_PROFILE_MANAGEMENT_SCOPE",
    "WCS_PROFILE_MANAGEMENT_SCOPE_SYSTEM_WIDE",
    "WCS_PROFILE_MANAGEMENT_SCOPE_CURRENT_USER",
    "PCMSCALLBACKW",
    "PCMSCALLBACKA",
    "COLORMATCHSETUPW",
    "COLORMATCHSETUPA",
    "WCS_DEVICE_VCGT_CAPABILITIES",
    "WCS_DEVICE_MHC2_CAPABILITIES",
    "WCS_DEVICE_CAPABILITIES_TYPE",
    "WCS_DEVICE_CAPABILITIES_TYPE_VideoCardGammaTable",
    "WCS_DEVICE_CAPABILITIES_TYPE_MicrosoftHardwareColorV2",
    "SetICMMode",
    "CheckColorsInGamut",
    "GetColorSpace",
    "GetLogColorSpaceA",
    "GetLogColorSpaceW",
    "GetLogColorSpace",
    "CreateColorSpaceA",
    "CreateColorSpaceW",
    "CreateColorSpace",
    "SetColorSpace",
    "DeleteColorSpace",
    "GetICMProfileA",
    "GetICMProfileW",
    "GetICMProfile",
    "SetICMProfileA",
    "SetICMProfileW",
    "SetICMProfile",
    "GetDeviceGammaRamp",
    "SetDeviceGammaRamp",
    "ColorMatchToTarget",
    "EnumICMProfilesA",
    "EnumICMProfilesW",
    "EnumICMProfiles",
    "UpdateICMRegKeyA",
    "UpdateICMRegKeyW",
    "UpdateICMRegKey",
    "ColorCorrectPalette",
    "OpenColorProfileA",
    "OpenColorProfileW",
    "OpenColorProfile",
    "CloseColorProfile",
    "GetColorProfileFromHandle",
    "IsColorProfileValid",
    "CreateProfileFromLogColorSpaceA",
    "CreateProfileFromLogColorSpaceW",
    "CreateProfileFromLogColorSpace",
    "GetCountColorProfileElements",
    "GetColorProfileHeader",
    "GetColorProfileElementTag",
    "IsColorProfileTagPresent",
    "GetColorProfileElement",
    "SetColorProfileHeader",
    "SetColorProfileElementSize",
    "SetColorProfileElement",
    "SetColorProfileElementReference",
    "GetPS2ColorSpaceArray",
    "GetPS2ColorRenderingIntent",
    "GetPS2ColorRenderingDictionary",
    "GetNamedProfileInfo",
    "ConvertColorNameToIndex",
    "ConvertIndexToColorName",
    "CreateDeviceLinkProfile",
    "CreateColorTransformA",
    "CreateColorTransformW",
    "CreateColorTransform",
    "CreateMultiProfileTransform",
    "DeleteColorTransform",
    "TranslateBitmapBits",
    "CheckBitmapBits",
    "TranslateColors",
    "CheckColors",
    "GetCMMInfo",
    "RegisterCMMA",
    "RegisterCMMW",
    "RegisterCMM",
    "UnregisterCMMA",
    "UnregisterCMMW",
    "UnregisterCMM",
    "SelectCMM",
    "GetColorDirectoryA",
    "GetColorDirectoryW",
    "GetColorDirectory",
    "InstallColorProfileA",
    "InstallColorProfileW",
    "InstallColorProfile",
    "UninstallColorProfileA",
    "UninstallColorProfileW",
    "UninstallColorProfile",
    "EnumColorProfilesA",
    "EnumColorProfilesW",
    "EnumColorProfiles",
    "SetStandardColorSpaceProfileA",
    "SetStandardColorSpaceProfileW",
    "SetStandardColorSpaceProfile",
    "GetStandardColorSpaceProfileA",
    "GetStandardColorSpaceProfileW",
    "GetStandardColorSpaceProfile",
    "AssociateColorProfileWithDeviceA",
    "AssociateColorProfileWithDeviceW",
    "AssociateColorProfileWithDevice",
    "DisassociateColorProfileFromDeviceA",
    "DisassociateColorProfileFromDeviceW",
    "DisassociateColorProfileFromDevice",
    "SetupColorMatchingW",
    "SetupColorMatching",
    "SetupColorMatchingA",
    "WcsAssociateColorProfileWithDevice",
    "WcsDisassociateColorProfileFromDevice",
    "WcsEnumColorProfilesSize",
    "WcsEnumColorProfiles",
    "WcsGetDefaultColorProfileSize",
    "WcsGetDefaultColorProfile",
    "WcsSetDefaultColorProfile",
    "WcsSetDefaultRenderingIntent",
    "WcsGetDefaultRenderingIntent",
    "WcsGetUsePerUserProfiles",
    "WcsSetUsePerUserProfiles",
    "WcsTranslateColors",
    "WcsCheckColors",
    "CMCheckColors",
    "CMCheckRGBs",
    "CMConvertColorNameToIndex",
    "CMConvertIndexToColorName",
    "CMCreateDeviceLinkProfile",
    "CMCreateMultiProfileTransform",
    "CMCreateProfileW",
    "CMCreateTransform",
    "CMCreateTransformW",
    "CMCreateTransformExt",
    "CMCheckColorsInGamut",
    "CMCreateProfile",
    "CMTranslateRGB",
    "CMTranslateRGBs",
    "CMCreateTransformExtW",
    "CMDeleteTransform",
    "CMGetInfo",
    "CMGetNamedProfileInfo",
    "CMIsProfileValid",
    "CMTranslateColors",
    "CMTranslateRGBsExt",
    "WcsOpenColorProfileA",
    "WcsOpenColorProfileW",
    "WcsOpenColorProfile",
    "WcsCreateIccProfile",
    "WcsGetCalibrationManagementState",
    "WcsSetCalibrationManagementState",
    "ColorProfileAddDisplayAssociation",
    "ColorProfileRemoveDisplayAssociation",
    "ColorProfileSetDisplayDefaultAssociation",
    "ColorProfileGetDisplayList",
    "ColorProfileGetDisplayDefault",
    "ColorProfileGetDisplayUserScope",
]
