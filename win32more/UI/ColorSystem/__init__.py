from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.System.Com
import win32more.UI.ColorSystem
import win32more.UI.WindowsAndMessaging
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
CATID_WcsPlugin: Guid = Guid('a0b402e0-8240-405f-8a-16-8a-5b-4d-f2-f0-dd')
MAX_COLOR_CHANNELS: UInt32 = 8
INTENT_PERCEPTUAL: UInt32 = 0
INTENT_RELATIVE_COLORIMETRIC: UInt32 = 1
INTENT_SATURATION: UInt32 = 2
INTENT_ABSOLUTE_COLORIMETRIC: UInt32 = 3
FLAG_EMBEDDEDPROFILE: UInt32 = 1
FLAG_DEPENDENTONDATA: UInt32 = 2
FLAG_ENABLE_CHROMATIC_ADAPTATION: UInt32 = 33554432
ATTRIB_TRANSPARENCY: UInt32 = 1
ATTRIB_MATTE: UInt32 = 2
PROFILE_FILENAME: UInt32 = 1
PROFILE_MEMBUFFER: UInt32 = 2
PROFILE_READ: UInt32 = 1
PROFILE_READWRITE: UInt32 = 2
INDEX_DONT_CARE: UInt32 = 0
CMM_FROM_PROFILE: UInt32 = 0
ENUM_TYPE_VERSION: UInt32 = 768
ET_DEVICENAME: UInt32 = 1
ET_MEDIATYPE: UInt32 = 2
ET_DITHERMODE: UInt32 = 4
ET_RESOLUTION: UInt32 = 8
ET_CMMTYPE: UInt32 = 16
ET_CLASS: UInt32 = 32
ET_DATACOLORSPACE: UInt32 = 64
ET_CONNECTIONSPACE: UInt32 = 128
ET_SIGNATURE: UInt32 = 256
ET_PLATFORM: UInt32 = 512
ET_PROFILEFLAGS: UInt32 = 1024
ET_MANUFACTURER: UInt32 = 2048
ET_MODEL: UInt32 = 4096
ET_ATTRIBUTES: UInt32 = 8192
ET_RENDERINGINTENT: UInt32 = 16384
ET_CREATOR: UInt32 = 32768
ET_DEVICECLASS: UInt32 = 65536
ET_STANDARDDISPLAYCOLOR: UInt32 = 131072
ET_EXTENDEDDISPLAYCOLOR: UInt32 = 262144
PROOF_MODE: UInt32 = 1
NORMAL_MODE: UInt32 = 2
BEST_MODE: UInt32 = 3
ENABLE_GAMUT_CHECKING: UInt32 = 65536
USE_RELATIVE_COLORIMETRIC: UInt32 = 131072
FAST_TRANSLATE: UInt32 = 262144
PRESERVEBLACK: UInt32 = 1048576
WCS_ALWAYS: UInt32 = 2097152
SEQUENTIAL_TRANSFORM: UInt32 = 2155872256
RESERVED: UInt32 = 2147483648
CSA_A: UInt32 = 1
CSA_ABC: UInt32 = 2
CSA_DEF: UInt32 = 3
CSA_DEFG: UInt32 = 4
CSA_GRAY: UInt32 = 5
CSA_RGB: UInt32 = 6
CSA_CMYK: UInt32 = 7
CSA_Lab: UInt32 = 8
CMM_WIN_VERSION: UInt32 = 0
CMM_IDENT: UInt32 = 1
CMM_DRIVER_VERSION: UInt32 = 2
CMM_DLL_VERSION: UInt32 = 3
CMM_VERSION: UInt32 = 4
CMM_DESCRIPTION: UInt32 = 5
CMM_LOGOICON: UInt32 = 6
CMS_FORWARD: UInt32 = 0
CMS_BACKWARD: UInt32 = 1
COLOR_MATCH_VERSION: UInt32 = 512
CMS_DISABLEICM: UInt32 = 1
CMS_ENABLEPROOFING: UInt32 = 2
CMS_SETRENDERINTENT: UInt32 = 4
CMS_SETPROOFINTENT: UInt32 = 8
CMS_SETMONITORPROFILE: UInt32 = 16
CMS_SETPRINTERPROFILE: UInt32 = 32
CMS_SETTARGETPROFILE: UInt32 = 64
CMS_USEHOOK: UInt32 = 128
CMS_USEAPPLYCALLBACK: UInt32 = 256
CMS_USEDESCRIPTION: UInt32 = 512
CMS_DISABLEINTENT: UInt32 = 1024
CMS_DISABLERENDERINTENT: UInt32 = 2048
CMS_MONITOROVERFLOW: Int32 = -2147483648
CMS_PRINTEROVERFLOW: Int32 = 1073741824
CMS_TARGETOVERFLOW: Int32 = 536870912
DONT_USE_EMBEDDED_WCS_PROFILES: Int32 = 1
WCS_DEFAULT: Int32 = 0
WCS_ICCONLY: Int32 = 65536
@winfunctype('GDI32.dll')
def SetICMMode(hdc: win32more.Graphics.Gdi.HDC, mode: win32more.UI.ColorSystem.ICM_MODE) -> Int32: ...
@winfunctype('GDI32.dll')
def CheckColorsInGamut(hdc: win32more.Graphics.Gdi.HDC, lpRGBTriple: POINTER(win32more.Graphics.Gdi.RGBTRIPLE_head), dlpBuffer: c_void_p, nCount: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def GetColorSpace(hdc: win32more.Graphics.Gdi.HDC) -> win32more.UI.ColorSystem.HCOLORSPACE: ...
@winfunctype('GDI32.dll')
def GetLogColorSpaceA(hColorSpace: win32more.UI.ColorSystem.HCOLORSPACE, lpBuffer: POINTER(win32more.UI.ColorSystem.LOGCOLORSPACEA_head), nSize: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def GetLogColorSpaceW(hColorSpace: win32more.UI.ColorSystem.HCOLORSPACE, lpBuffer: POINTER(win32more.UI.ColorSystem.LOGCOLORSPACEW_head), nSize: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def CreateColorSpaceA(lplcs: POINTER(win32more.UI.ColorSystem.LOGCOLORSPACEA_head)) -> win32more.UI.ColorSystem.HCOLORSPACE: ...
@winfunctype('GDI32.dll')
def CreateColorSpaceW(lplcs: POINTER(win32more.UI.ColorSystem.LOGCOLORSPACEW_head)) -> win32more.UI.ColorSystem.HCOLORSPACE: ...
@winfunctype('GDI32.dll')
def SetColorSpace(hdc: win32more.Graphics.Gdi.HDC, hcs: win32more.UI.ColorSystem.HCOLORSPACE) -> win32more.UI.ColorSystem.HCOLORSPACE: ...
@winfunctype('GDI32.dll')
def DeleteColorSpace(hcs: win32more.UI.ColorSystem.HCOLORSPACE) -> win32more.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def GetICMProfileA(hdc: win32more.Graphics.Gdi.HDC, pBufSize: POINTER(UInt32), pszFilename: win32more.Foundation.PSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def GetICMProfileW(hdc: win32more.Graphics.Gdi.HDC, pBufSize: POINTER(UInt32), pszFilename: win32more.Foundation.PWSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def SetICMProfileA(hdc: win32more.Graphics.Gdi.HDC, lpFileName: win32more.Foundation.PSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def SetICMProfileW(hdc: win32more.Graphics.Gdi.HDC, lpFileName: win32more.Foundation.PWSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def GetDeviceGammaRamp(hdc: win32more.Graphics.Gdi.HDC, lpRamp: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def SetDeviceGammaRamp(hdc: win32more.Graphics.Gdi.HDC, lpRamp: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def ColorMatchToTarget(hdc: win32more.Graphics.Gdi.HDC, hdcTarget: win32more.Graphics.Gdi.HDC, action: win32more.UI.ColorSystem.COLOR_MATCH_TO_TARGET_ACTION) -> win32more.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def EnumICMProfilesA(hdc: win32more.Graphics.Gdi.HDC, proc: win32more.UI.ColorSystem.ICMENUMPROCA, param2: win32more.Foundation.LPARAM) -> Int32: ...
@winfunctype('GDI32.dll')
def EnumICMProfilesW(hdc: win32more.Graphics.Gdi.HDC, proc: win32more.UI.ColorSystem.ICMENUMPROCW, param2: win32more.Foundation.LPARAM) -> Int32: ...
@winfunctype('GDI32.dll')
def UpdateICMRegKeyA(reserved: UInt32, lpszCMID: win32more.Foundation.PSTR, lpszFileName: win32more.Foundation.PSTR, command: win32more.UI.ColorSystem.ICM_COMMAND) -> win32more.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def UpdateICMRegKeyW(reserved: UInt32, lpszCMID: win32more.Foundation.PWSTR, lpszFileName: win32more.Foundation.PWSTR, command: win32more.UI.ColorSystem.ICM_COMMAND) -> win32more.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def ColorCorrectPalette(hdc: win32more.Graphics.Gdi.HDC, hPal: win32more.Graphics.Gdi.HPALETTE, deFirst: UInt32, num: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def OpenColorProfileA(pProfile: POINTER(win32more.UI.ColorSystem.PROFILE_head), dwDesiredAccess: UInt32, dwShareMode: UInt32, dwCreationMode: UInt32) -> IntPtr: ...
@winfunctype('mscms.dll')
def OpenColorProfileW(pProfile: POINTER(win32more.UI.ColorSystem.PROFILE_head), dwDesiredAccess: UInt32, dwShareMode: UInt32, dwCreationMode: UInt32) -> IntPtr: ...
@winfunctype('mscms.dll')
def CloseColorProfile(hProfile: IntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetColorProfileFromHandle(hProfile: IntPtr, pProfile: c_char_p_no, pcbProfile: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def IsColorProfileValid(hProfile: IntPtr, pbValid: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def CreateProfileFromLogColorSpaceA(pLogColorSpace: POINTER(win32more.UI.ColorSystem.LOGCOLORSPACEA_head), pProfile: POINTER(c_char_p_no)) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def CreateProfileFromLogColorSpaceW(pLogColorSpace: POINTER(win32more.UI.ColorSystem.LOGCOLORSPACEW_head), pProfile: POINTER(c_char_p_no)) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetCountColorProfileElements(hProfile: IntPtr, pnElementCount: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetColorProfileHeader(hProfile: IntPtr, pHeader: POINTER(win32more.UI.ColorSystem.PROFILEHEADER_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetColorProfileElementTag(hProfile: IntPtr, dwIndex: UInt32, pTag: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def IsColorProfileTagPresent(hProfile: IntPtr, tag: UInt32, pbPresent: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetColorProfileElement(hProfile: IntPtr, tag: UInt32, dwOffset: UInt32, pcbElement: POINTER(UInt32), pElement: c_void_p, pbReference: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def SetColorProfileHeader(hProfile: IntPtr, pHeader: POINTER(win32more.UI.ColorSystem.PROFILEHEADER_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def SetColorProfileElementSize(hProfile: IntPtr, tagType: UInt32, pcbElement: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def SetColorProfileElement(hProfile: IntPtr, tag: UInt32, dwOffset: UInt32, pcbElement: POINTER(UInt32), pElement: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def SetColorProfileElementReference(hProfile: IntPtr, newTag: UInt32, refTag: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetPS2ColorSpaceArray(hProfile: IntPtr, dwIntent: UInt32, dwCSAType: UInt32, pPS2ColorSpaceArray: c_char_p_no, pcbPS2ColorSpaceArray: POINTER(UInt32), pbBinary: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetPS2ColorRenderingIntent(hProfile: IntPtr, dwIntent: UInt32, pBuffer: c_char_p_no, pcbPS2ColorRenderingIntent: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetPS2ColorRenderingDictionary(hProfile: IntPtr, dwIntent: UInt32, pPS2ColorRenderingDictionary: c_char_p_no, pcbPS2ColorRenderingDictionary: POINTER(UInt32), pbBinary: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetNamedProfileInfo(hProfile: IntPtr, pNamedProfileInfo: POINTER(win32more.UI.ColorSystem.NAMED_PROFILE_INFO_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def ConvertColorNameToIndex(hProfile: IntPtr, paColorName: POINTER(POINTER(SByte)), paIndex: POINTER(UInt32), dwCount: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def ConvertIndexToColorName(hProfile: IntPtr, paIndex: POINTER(UInt32), paColorName: POINTER(POINTER(SByte)), dwCount: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def CreateDeviceLinkProfile(hProfile: POINTER(IntPtr), nProfiles: UInt32, padwIntent: POINTER(UInt32), nIntents: UInt32, dwFlags: UInt32, pProfileData: POINTER(c_char_p_no), indexPreferredCMM: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def CreateColorTransformA(pLogColorSpace: POINTER(win32more.UI.ColorSystem.LOGCOLORSPACEA_head), hDestProfile: IntPtr, hTargetProfile: IntPtr, dwFlags: UInt32) -> IntPtr: ...
@winfunctype('mscms.dll')
def CreateColorTransformW(pLogColorSpace: POINTER(win32more.UI.ColorSystem.LOGCOLORSPACEW_head), hDestProfile: IntPtr, hTargetProfile: IntPtr, dwFlags: UInt32) -> IntPtr: ...
@winfunctype('mscms.dll')
def CreateMultiProfileTransform(pahProfiles: POINTER(IntPtr), nProfiles: UInt32, padwIntent: POINTER(UInt32), nIntents: UInt32, dwFlags: UInt32, indexPreferredCMM: UInt32) -> IntPtr: ...
@winfunctype('mscms.dll')
def DeleteColorTransform(hxform: IntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def TranslateBitmapBits(hColorTransform: IntPtr, pSrcBits: c_void_p, bmInput: win32more.UI.ColorSystem.BMFORMAT, dwWidth: UInt32, dwHeight: UInt32, dwInputStride: UInt32, pDestBits: c_void_p, bmOutput: win32more.UI.ColorSystem.BMFORMAT, dwOutputStride: UInt32, pfnCallBack: win32more.UI.ColorSystem.LPBMCALLBACKFN, ulCallbackData: win32more.Foundation.LPARAM) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def CheckBitmapBits(hColorTransform: IntPtr, pSrcBits: c_void_p, bmInput: win32more.UI.ColorSystem.BMFORMAT, dwWidth: UInt32, dwHeight: UInt32, dwStride: UInt32, paResult: c_char_p_no, pfnCallback: win32more.UI.ColorSystem.LPBMCALLBACKFN, lpCallbackData: win32more.Foundation.LPARAM) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def TranslateColors(hColorTransform: IntPtr, paInputColors: POINTER(win32more.UI.ColorSystem.COLOR_head), nColors: UInt32, ctInput: win32more.UI.ColorSystem.COLORTYPE, paOutputColors: POINTER(win32more.UI.ColorSystem.COLOR_head), ctOutput: win32more.UI.ColorSystem.COLORTYPE) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def CheckColors(hColorTransform: IntPtr, paInputColors: POINTER(win32more.UI.ColorSystem.COLOR_head), nColors: UInt32, ctInput: win32more.UI.ColorSystem.COLORTYPE, paResult: c_char_p_no) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetCMMInfo(hColorTransform: IntPtr, param1: UInt32) -> UInt32: ...
@winfunctype('mscms.dll')
def RegisterCMMA(pMachineName: win32more.Foundation.PSTR, cmmID: UInt32, pCMMdll: win32more.Foundation.PSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def RegisterCMMW(pMachineName: win32more.Foundation.PWSTR, cmmID: UInt32, pCMMdll: win32more.Foundation.PWSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def UnregisterCMMA(pMachineName: win32more.Foundation.PSTR, cmmID: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def UnregisterCMMW(pMachineName: win32more.Foundation.PWSTR, cmmID: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def SelectCMM(dwCMMType: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetColorDirectoryA(pMachineName: win32more.Foundation.PSTR, pBuffer: win32more.Foundation.PSTR, pdwSize: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetColorDirectoryW(pMachineName: win32more.Foundation.PWSTR, pBuffer: win32more.Foundation.PWSTR, pdwSize: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def InstallColorProfileA(pMachineName: win32more.Foundation.PSTR, pProfileName: win32more.Foundation.PSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def InstallColorProfileW(pMachineName: win32more.Foundation.PWSTR, pProfileName: win32more.Foundation.PWSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def UninstallColorProfileA(pMachineName: win32more.Foundation.PSTR, pProfileName: win32more.Foundation.PSTR, bDelete: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def UninstallColorProfileW(pMachineName: win32more.Foundation.PWSTR, pProfileName: win32more.Foundation.PWSTR, bDelete: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def EnumColorProfilesA(pMachineName: win32more.Foundation.PSTR, pEnumRecord: POINTER(win32more.UI.ColorSystem.ENUMTYPEA_head), pEnumerationBuffer: c_char_p_no, pdwSizeOfEnumerationBuffer: POINTER(UInt32), pnProfiles: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def EnumColorProfilesW(pMachineName: win32more.Foundation.PWSTR, pEnumRecord: POINTER(win32more.UI.ColorSystem.ENUMTYPEW_head), pEnumerationBuffer: c_char_p_no, pdwSizeOfEnumerationBuffer: POINTER(UInt32), pnProfiles: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def SetStandardColorSpaceProfileA(pMachineName: win32more.Foundation.PSTR, dwProfileID: UInt32, pProfilename: win32more.Foundation.PSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def SetStandardColorSpaceProfileW(pMachineName: win32more.Foundation.PWSTR, dwProfileID: UInt32, pProfileName: win32more.Foundation.PWSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetStandardColorSpaceProfileA(pMachineName: win32more.Foundation.PSTR, dwSCS: UInt32, pBuffer: win32more.Foundation.PSTR, pcbSize: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetStandardColorSpaceProfileW(pMachineName: win32more.Foundation.PWSTR, dwSCS: UInt32, pBuffer: win32more.Foundation.PWSTR, pcbSize: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def AssociateColorProfileWithDeviceA(pMachineName: win32more.Foundation.PSTR, pProfileName: win32more.Foundation.PSTR, pDeviceName: win32more.Foundation.PSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def AssociateColorProfileWithDeviceW(pMachineName: win32more.Foundation.PWSTR, pProfileName: win32more.Foundation.PWSTR, pDeviceName: win32more.Foundation.PWSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def DisassociateColorProfileFromDeviceA(pMachineName: win32more.Foundation.PSTR, pProfileName: win32more.Foundation.PSTR, pDeviceName: win32more.Foundation.PSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def DisassociateColorProfileFromDeviceW(pMachineName: win32more.Foundation.PWSTR, pProfileName: win32more.Foundation.PWSTR, pDeviceName: win32more.Foundation.PWSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('ICMUI.dll')
def SetupColorMatchingW(pcms: POINTER(win32more.UI.ColorSystem.COLORMATCHSETUPW_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('ICMUI.dll')
def SetupColorMatchingA(pcms: POINTER(win32more.UI.ColorSystem.COLORMATCHSETUPA_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsAssociateColorProfileWithDevice(scope: win32more.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, pProfileName: win32more.Foundation.PWSTR, pDeviceName: win32more.Foundation.PWSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsDisassociateColorProfileFromDevice(scope: win32more.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, pProfileName: win32more.Foundation.PWSTR, pDeviceName: win32more.Foundation.PWSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsEnumColorProfilesSize(scope: win32more.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, pEnumRecord: POINTER(win32more.UI.ColorSystem.ENUMTYPEW_head), pdwSize: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsEnumColorProfiles(scope: win32more.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, pEnumRecord: POINTER(win32more.UI.ColorSystem.ENUMTYPEW_head), pBuffer: c_char_p_no, dwSize: UInt32, pnProfiles: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsGetDefaultColorProfileSize(scope: win32more.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, pDeviceName: win32more.Foundation.PWSTR, cptColorProfileType: win32more.UI.ColorSystem.COLORPROFILETYPE, cpstColorProfileSubType: win32more.UI.ColorSystem.COLORPROFILESUBTYPE, dwProfileID: UInt32, pcbProfileName: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsGetDefaultColorProfile(scope: win32more.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, pDeviceName: win32more.Foundation.PWSTR, cptColorProfileType: win32more.UI.ColorSystem.COLORPROFILETYPE, cpstColorProfileSubType: win32more.UI.ColorSystem.COLORPROFILESUBTYPE, dwProfileID: UInt32, cbProfileName: UInt32, pProfileName: win32more.Foundation.PWSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsSetDefaultColorProfile(scope: win32more.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, pDeviceName: win32more.Foundation.PWSTR, cptColorProfileType: win32more.UI.ColorSystem.COLORPROFILETYPE, cpstColorProfileSubType: win32more.UI.ColorSystem.COLORPROFILESUBTYPE, dwProfileID: UInt32, pProfileName: win32more.Foundation.PWSTR) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsSetDefaultRenderingIntent(scope: win32more.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, dwRenderingIntent: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsGetDefaultRenderingIntent(scope: win32more.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, pdwRenderingIntent: POINTER(UInt32)) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsGetUsePerUserProfiles(pDeviceName: win32more.Foundation.PWSTR, dwDeviceClass: UInt32, pUsePerUserProfiles: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsSetUsePerUserProfiles(pDeviceName: win32more.Foundation.PWSTR, dwDeviceClass: UInt32, usePerUserProfiles: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsTranslateColors(hColorTransform: IntPtr, nColors: UInt32, nInputChannels: UInt32, cdtInput: win32more.UI.ColorSystem.COLORDATATYPE, cbInput: UInt32, pInputData: c_void_p, nOutputChannels: UInt32, cdtOutput: win32more.UI.ColorSystem.COLORDATATYPE, cbOutput: UInt32, pOutputData: c_void_p) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsCheckColors(hColorTransform: IntPtr, nColors: UInt32, nInputChannels: UInt32, cdtInput: win32more.UI.ColorSystem.COLORDATATYPE, cbInput: UInt32, pInputData: c_void_p, paResult: c_char_p_no) -> win32more.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMCheckColors(hcmTransform: IntPtr, lpaInputColors: POINTER(win32more.UI.ColorSystem.COLOR_head), nColors: UInt32, ctInput: win32more.UI.ColorSystem.COLORTYPE, lpaResult: c_char_p_no) -> win32more.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMCheckRGBs(hcmTransform: IntPtr, lpSrcBits: c_void_p, bmInput: win32more.UI.ColorSystem.BMFORMAT, dwWidth: UInt32, dwHeight: UInt32, dwStride: UInt32, lpaResult: c_char_p_no, pfnCallback: win32more.UI.ColorSystem.LPBMCALLBACKFN, ulCallbackData: win32more.Foundation.LPARAM) -> win32more.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMConvertColorNameToIndex(hProfile: IntPtr, paColorName: POINTER(POINTER(SByte)), paIndex: POINTER(UInt32), dwCount: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMConvertIndexToColorName(hProfile: IntPtr, paIndex: POINTER(UInt32), paColorName: POINTER(POINTER(SByte)), dwCount: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMCreateDeviceLinkProfile(pahProfiles: POINTER(IntPtr), nProfiles: UInt32, padwIntents: POINTER(UInt32), nIntents: UInt32, dwFlags: UInt32, lpProfileData: POINTER(c_char_p_no)) -> win32more.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMCreateMultiProfileTransform(pahProfiles: POINTER(IntPtr), nProfiles: UInt32, padwIntents: POINTER(UInt32), nIntents: UInt32, dwFlags: UInt32) -> IntPtr: ...
@winfunctype('ICM32.dll')
def CMCreateProfileW(lpColorSpace: POINTER(win32more.UI.ColorSystem.LOGCOLORSPACEW_head), lpProfileData: POINTER(c_void_p)) -> win32more.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMCreateTransform(lpColorSpace: POINTER(win32more.UI.ColorSystem.LOGCOLORSPACEA_head), lpDevCharacter: c_void_p, lpTargetDevCharacter: c_void_p) -> IntPtr: ...
@winfunctype('ICM32.dll')
def CMCreateTransformW(lpColorSpace: POINTER(win32more.UI.ColorSystem.LOGCOLORSPACEW_head), lpDevCharacter: c_void_p, lpTargetDevCharacter: c_void_p) -> IntPtr: ...
@winfunctype('ICM32.dll')
def CMCreateTransformExt(lpColorSpace: POINTER(win32more.UI.ColorSystem.LOGCOLORSPACEA_head), lpDevCharacter: c_void_p, lpTargetDevCharacter: c_void_p, dwFlags: UInt32) -> IntPtr: ...
@winfunctype('ICM32.dll')
def CMCheckColorsInGamut(hcmTransform: IntPtr, lpaRGBTriple: POINTER(win32more.Graphics.Gdi.RGBTRIPLE_head), lpaResult: c_char_p_no, nCount: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMCreateProfile(lpColorSpace: POINTER(win32more.UI.ColorSystem.LOGCOLORSPACEA_head), lpProfileData: POINTER(c_void_p)) -> win32more.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMTranslateRGB(hcmTransform: IntPtr, ColorRef: win32more.Foundation.COLORREF, lpColorRef: POINTER(UInt32), dwFlags: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMTranslateRGBs(hcmTransform: IntPtr, lpSrcBits: c_void_p, bmInput: win32more.UI.ColorSystem.BMFORMAT, dwWidth: UInt32, dwHeight: UInt32, dwStride: UInt32, lpDestBits: c_void_p, bmOutput: win32more.UI.ColorSystem.BMFORMAT, dwTranslateDirection: UInt32) -> win32more.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMCreateTransformExtW(lpColorSpace: POINTER(win32more.UI.ColorSystem.LOGCOLORSPACEW_head), lpDevCharacter: c_void_p, lpTargetDevCharacter: c_void_p, dwFlags: UInt32) -> IntPtr: ...
@winfunctype('ICM32.dll')
def CMDeleteTransform(hcmTransform: IntPtr) -> win32more.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMGetInfo(dwInfo: UInt32) -> UInt32: ...
@winfunctype('ICM32.dll')
def CMGetNamedProfileInfo(hProfile: IntPtr, pNamedProfileInfo: POINTER(win32more.UI.ColorSystem.NAMED_PROFILE_INFO_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMIsProfileValid(hProfile: IntPtr, lpbValid: POINTER(Int32)) -> win32more.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMTranslateColors(hcmTransform: IntPtr, lpaInputColors: POINTER(win32more.UI.ColorSystem.COLOR_head), nColors: UInt32, ctInput: win32more.UI.ColorSystem.COLORTYPE, lpaOutputColors: POINTER(win32more.UI.ColorSystem.COLOR_head), ctOutput: win32more.UI.ColorSystem.COLORTYPE) -> win32more.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMTranslateRGBsExt(hcmTransform: IntPtr, lpSrcBits: c_void_p, bmInput: win32more.UI.ColorSystem.BMFORMAT, dwWidth: UInt32, dwHeight: UInt32, dwInputStride: UInt32, lpDestBits: c_void_p, bmOutput: win32more.UI.ColorSystem.BMFORMAT, dwOutputStride: UInt32, lpfnCallback: win32more.UI.ColorSystem.LPBMCALLBACKFN, ulCallbackData: win32more.Foundation.LPARAM) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsOpenColorProfileA(pCDMPProfile: POINTER(win32more.UI.ColorSystem.PROFILE_head), pCAMPProfile: POINTER(win32more.UI.ColorSystem.PROFILE_head), pGMMPProfile: POINTER(win32more.UI.ColorSystem.PROFILE_head), dwDesireAccess: UInt32, dwShareMode: UInt32, dwCreationMode: UInt32, dwFlags: UInt32) -> IntPtr: ...
@winfunctype('mscms.dll')
def WcsOpenColorProfileW(pCDMPProfile: POINTER(win32more.UI.ColorSystem.PROFILE_head), pCAMPProfile: POINTER(win32more.UI.ColorSystem.PROFILE_head), pGMMPProfile: POINTER(win32more.UI.ColorSystem.PROFILE_head), dwDesireAccess: UInt32, dwShareMode: UInt32, dwCreationMode: UInt32, dwFlags: UInt32) -> IntPtr: ...
@winfunctype('mscms.dll')
def WcsCreateIccProfile(hWcsProfile: IntPtr, dwOptions: UInt32) -> IntPtr: ...
@winfunctype('mscms.dll')
def WcsGetCalibrationManagementState(pbIsEnabled: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsSetCalibrationManagementState(bIsEnabled: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def ColorProfileAddDisplayAssociation(scope: win32more.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, profileName: win32more.Foundation.PWSTR, targetAdapterID: win32more.Foundation.LUID, sourceID: UInt32, setAsDefault: win32more.Foundation.BOOL, associateAsAdvancedColor: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
@winfunctype('mscms.dll')
def ColorProfileRemoveDisplayAssociation(scope: win32more.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, profileName: win32more.Foundation.PWSTR, targetAdapterID: win32more.Foundation.LUID, sourceID: UInt32, dissociateAdvancedColor: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
@winfunctype('mscms.dll')
def ColorProfileSetDisplayDefaultAssociation(scope: win32more.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, profileName: win32more.Foundation.PWSTR, profileType: win32more.UI.ColorSystem.COLORPROFILETYPE, profileSubType: win32more.UI.ColorSystem.COLORPROFILESUBTYPE, targetAdapterID: win32more.Foundation.LUID, sourceID: UInt32) -> win32more.Foundation.HRESULT: ...
@winfunctype('mscms.dll')
def ColorProfileGetDisplayList(scope: win32more.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, targetAdapterID: win32more.Foundation.LUID, sourceID: UInt32, profileList: POINTER(POINTER(win32more.Foundation.PWSTR)), profileCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype('mscms.dll')
def ColorProfileGetDisplayDefault(scope: win32more.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, targetAdapterID: win32more.Foundation.LUID, sourceID: UInt32, profileType: win32more.UI.ColorSystem.COLORPROFILETYPE, profileSubType: win32more.UI.ColorSystem.COLORPROFILESUBTYPE, profileName: POINTER(win32more.Foundation.PWSTR)) -> win32more.Foundation.HRESULT: ...
@winfunctype('mscms.dll')
def ColorProfileGetDisplayUserScope(targetAdapterID: win32more.Foundation.LUID, sourceID: UInt32, scope: POINTER(win32more.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE)) -> win32more.Foundation.HRESULT: ...
class BlackInformation(Structure):
    fBlackOnly: win32more.Foundation.BOOL
    blackWeight: Single
BMFORMAT = Int32
BM_x555RGB: BMFORMAT = 0
BM_x555XYZ: BMFORMAT = 257
BM_x555Yxy: BMFORMAT = 258
BM_x555Lab: BMFORMAT = 259
BM_x555G3CH: BMFORMAT = 260
BM_RGBTRIPLETS: BMFORMAT = 2
BM_BGRTRIPLETS: BMFORMAT = 4
BM_XYZTRIPLETS: BMFORMAT = 513
BM_YxyTRIPLETS: BMFORMAT = 514
BM_LabTRIPLETS: BMFORMAT = 515
BM_G3CHTRIPLETS: BMFORMAT = 516
BM_5CHANNEL: BMFORMAT = 517
BM_6CHANNEL: BMFORMAT = 518
BM_7CHANNEL: BMFORMAT = 519
BM_8CHANNEL: BMFORMAT = 520
BM_GRAY: BMFORMAT = 521
BM_xRGBQUADS: BMFORMAT = 8
BM_xBGRQUADS: BMFORMAT = 16
BM_xG3CHQUADS: BMFORMAT = 772
BM_KYMCQUADS: BMFORMAT = 773
BM_CMYKQUADS: BMFORMAT = 32
BM_10b_RGB: BMFORMAT = 9
BM_10b_XYZ: BMFORMAT = 1025
BM_10b_Yxy: BMFORMAT = 1026
BM_10b_Lab: BMFORMAT = 1027
BM_10b_G3CH: BMFORMAT = 1028
BM_NAMED_INDEX: BMFORMAT = 1029
BM_16b_RGB: BMFORMAT = 10
BM_16b_XYZ: BMFORMAT = 1281
BM_16b_Yxy: BMFORMAT = 1282
BM_16b_Lab: BMFORMAT = 1283
BM_16b_G3CH: BMFORMAT = 1284
BM_16b_GRAY: BMFORMAT = 1285
BM_565RGB: BMFORMAT = 1
BM_32b_scRGB: BMFORMAT = 1537
BM_32b_scARGB: BMFORMAT = 1538
BM_S2DOT13FIXED_scRGB: BMFORMAT = 1539
BM_S2DOT13FIXED_scARGB: BMFORMAT = 1540
BM_R10G10B10A2: BMFORMAT = 1793
BM_R10G10B10A2_XR: BMFORMAT = 1794
BM_R16G16B16A16_FLOAT: BMFORMAT = 1795
class CMYKCOLOR(Structure):
    cyan: UInt16
    magenta: UInt16
    yellow: UInt16
    black: UInt16
class COLOR(Union):
    gray: win32more.UI.ColorSystem.GRAYCOLOR
    rgb: win32more.UI.ColorSystem.RGBCOLOR
    cmyk: win32more.UI.ColorSystem.CMYKCOLOR
    XYZ: win32more.UI.ColorSystem.XYZCOLOR
    Yxy: win32more.UI.ColorSystem.YxyCOLOR
    Lab: win32more.UI.ColorSystem.LabCOLOR
    gen3ch: win32more.UI.ColorSystem.GENERIC3CHANNEL
    named: win32more.UI.ColorSystem.NAMEDCOLOR
    hifi: win32more.UI.ColorSystem.HiFiCOLOR
    Anonymous: _Anonymous_e__Struct
    class _Anonymous_e__Struct(Structure):
        reserved1: UInt32
        reserved2: c_void_p
COLOR_MATCH_TO_TARGET_ACTION = Int32
CS_ENABLE: COLOR_MATCH_TO_TARGET_ACTION = 1
CS_DISABLE: COLOR_MATCH_TO_TARGET_ACTION = 2
CS_DELETE_TRANSFORM: COLOR_MATCH_TO_TARGET_ACTION = 3
COLORDATATYPE = Int32
COLOR_BYTE: COLORDATATYPE = 1
COLOR_WORD: COLORDATATYPE = 2
COLOR_FLOAT: COLORDATATYPE = 3
COLOR_S2DOT13FIXED: COLORDATATYPE = 4
COLOR_10b_R10G10B10A2: COLORDATATYPE = 5
COLOR_10b_R10G10B10A2_XR: COLORDATATYPE = 6
COLOR_FLOAT16: COLORDATATYPE = 7
class COLORMATCHSETUPA(Structure):
    dwSize: UInt32
    dwVersion: UInt32
    dwFlags: UInt32
    hwndOwner: win32more.Foundation.HWND
    pSourceName: win32more.Foundation.PSTR
    pDisplayName: win32more.Foundation.PSTR
    pPrinterName: win32more.Foundation.PSTR
    dwRenderIntent: UInt32
    dwProofingIntent: UInt32
    pMonitorProfile: win32more.Foundation.PSTR
    ccMonitorProfile: UInt32
    pPrinterProfile: win32more.Foundation.PSTR
    ccPrinterProfile: UInt32
    pTargetProfile: win32more.Foundation.PSTR
    ccTargetProfile: UInt32
    lpfnHook: win32more.UI.WindowsAndMessaging.DLGPROC
    lParam: win32more.Foundation.LPARAM
    lpfnApplyCallback: win32more.UI.ColorSystem.PCMSCALLBACKA
    lParamApplyCallback: win32more.Foundation.LPARAM
class COLORMATCHSETUPW(Structure):
    dwSize: UInt32
    dwVersion: UInt32
    dwFlags: UInt32
    hwndOwner: win32more.Foundation.HWND
    pSourceName: win32more.Foundation.PWSTR
    pDisplayName: win32more.Foundation.PWSTR
    pPrinterName: win32more.Foundation.PWSTR
    dwRenderIntent: UInt32
    dwProofingIntent: UInt32
    pMonitorProfile: win32more.Foundation.PWSTR
    ccMonitorProfile: UInt32
    pPrinterProfile: win32more.Foundation.PWSTR
    ccPrinterProfile: UInt32
    pTargetProfile: win32more.Foundation.PWSTR
    ccTargetProfile: UInt32
    lpfnHook: win32more.UI.WindowsAndMessaging.DLGPROC
    lParam: win32more.Foundation.LPARAM
    lpfnApplyCallback: win32more.UI.ColorSystem.PCMSCALLBACKW
    lParamApplyCallback: win32more.Foundation.LPARAM
COLORPROFILESUBTYPE = Int32
CPST_PERCEPTUAL: COLORPROFILESUBTYPE = 0
CPST_RELATIVE_COLORIMETRIC: COLORPROFILESUBTYPE = 1
CPST_SATURATION: COLORPROFILESUBTYPE = 2
CPST_ABSOLUTE_COLORIMETRIC: COLORPROFILESUBTYPE = 3
CPST_NONE: COLORPROFILESUBTYPE = 4
CPST_RGB_WORKING_SPACE: COLORPROFILESUBTYPE = 5
CPST_CUSTOM_WORKING_SPACE: COLORPROFILESUBTYPE = 6
CPST_STANDARD_DISPLAY_COLOR_MODE: COLORPROFILESUBTYPE = 7
CPST_EXTENDED_DISPLAY_COLOR_MODE: COLORPROFILESUBTYPE = 8
COLORPROFILETYPE = Int32
CPT_ICC: COLORPROFILETYPE = 0
CPT_DMP: COLORPROFILETYPE = 1
CPT_CAMP: COLORPROFILETYPE = 2
CPT_GMMP: COLORPROFILETYPE = 3
COLORTYPE = Int32
COLOR_GRAY: COLORTYPE = 1
COLOR_RGB: COLORTYPE = 2
COLOR_XYZ: COLORTYPE = 3
COLOR_Yxy: COLORTYPE = 4
COLOR_Lab: COLORTYPE = 5
COLOR_3_CHANNEL: COLORTYPE = 6
COLOR_CMYK: COLORTYPE = 7
COLOR_5_CHANNEL: COLORTYPE = 8
COLOR_6_CHANNEL: COLORTYPE = 9
COLOR_7_CHANNEL: COLORTYPE = 10
COLOR_8_CHANNEL: COLORTYPE = 11
COLOR_NAMED: COLORTYPE = 12
class EMRCREATECOLORSPACE(Structure):
    emr: win32more.Graphics.Gdi.EMR
    ihCS: UInt32
    lcs: win32more.UI.ColorSystem.LOGCOLORSPACEA
class EMRCREATECOLORSPACEW(Structure):
    emr: win32more.Graphics.Gdi.EMR
    ihCS: UInt32
    lcs: win32more.UI.ColorSystem.LOGCOLORSPACEW
    dwFlags: UInt32
    cbData: UInt32
    Data: Byte * 1
class ENUMTYPEA(Structure):
    dwSize: UInt32
    dwVersion: UInt32
    dwFields: UInt32
    pDeviceName: win32more.Foundation.PSTR
    dwMediaType: UInt32
    dwDitheringMode: UInt32
    dwResolution: UInt32 * 2
    dwCMMType: UInt32
    dwClass: UInt32
    dwDataColorSpace: UInt32
    dwConnectionSpace: UInt32
    dwSignature: UInt32
    dwPlatform: UInt32
    dwProfileFlags: UInt32
    dwManufacturer: UInt32
    dwModel: UInt32
    dwAttributes: UInt32 * 2
    dwRenderingIntent: UInt32
    dwCreator: UInt32
    dwDeviceClass: UInt32
class ENUMTYPEW(Structure):
    dwSize: UInt32
    dwVersion: UInt32
    dwFields: UInt32
    pDeviceName: win32more.Foundation.PWSTR
    dwMediaType: UInt32
    dwDitheringMode: UInt32
    dwResolution: UInt32 * 2
    dwCMMType: UInt32
    dwClass: UInt32
    dwDataColorSpace: UInt32
    dwConnectionSpace: UInt32
    dwSignature: UInt32
    dwPlatform: UInt32
    dwProfileFlags: UInt32
    dwManufacturer: UInt32
    dwModel: UInt32
    dwAttributes: UInt32 * 2
    dwRenderingIntent: UInt32
    dwCreator: UInt32
    dwDeviceClass: UInt32
class GamutBoundaryDescription(Structure):
    pPrimaries: POINTER(win32more.UI.ColorSystem.PrimaryJabColors_head)
    cNeutralSamples: UInt32
    pNeutralSamples: POINTER(win32more.UI.ColorSystem.JabColorF_head)
    pReferenceShell: POINTER(win32more.UI.ColorSystem.GamutShell_head)
    pPlausibleShell: POINTER(win32more.UI.ColorSystem.GamutShell_head)
    pPossibleShell: POINTER(win32more.UI.ColorSystem.GamutShell_head)
class GamutShell(Structure):
    JMin: Single
    JMax: Single
    cVertices: UInt32
    cTriangles: UInt32
    pVertices: POINTER(win32more.UI.ColorSystem.JabColorF_head)
    pTriangles: POINTER(win32more.UI.ColorSystem.GamutShellTriangle_head)
class GamutShellTriangle(Structure):
    aVertexIndex: UInt32 * 3
class GENERIC3CHANNEL(Structure):
    ch1: UInt16
    ch2: UInt16
    ch3: UInt16
class GRAYCOLOR(Structure):
    gray: UInt16
HCOLORSPACE = IntPtr
class HiFiCOLOR(Structure):
    channel: Byte * 8
ICM_COMMAND = UInt32
ICM_ADDPROFILE: ICM_COMMAND = 1
ICM_DELETEPROFILE: ICM_COMMAND = 2
ICM_QUERYPROFILE: ICM_COMMAND = 3
ICM_SETDEFAULTPROFILE: ICM_COMMAND = 4
ICM_REGISTERICMATCHER: ICM_COMMAND = 5
ICM_UNREGISTERICMATCHER: ICM_COMMAND = 6
ICM_QUERYMATCH: ICM_COMMAND = 7
ICM_MODE = Int32
ICM_OFF: ICM_MODE = 1
ICM_ON: ICM_MODE = 2
ICM_QUERY: ICM_MODE = 3
ICM_DONE_OUTSIDEDC: ICM_MODE = 4
@winfunctype_pointer
def ICMENUMPROCA(param0: win32more.Foundation.PSTR, param1: win32more.Foundation.LPARAM) -> Int32: ...
@winfunctype_pointer
def ICMENUMPROCW(param0: win32more.Foundation.PWSTR, param1: win32more.Foundation.LPARAM) -> Int32: ...
class IDeviceModelPlugIn(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('1cd63475-07c4-46fe-a9-03-d6-55-31-6d-11-fd')
    @commethod(3)
    def Initialize(bstrXml: win32more.Foundation.BSTR, cNumModels: UInt32, iModelPosition: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetNumChannels(pNumChannels: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def DeviceToColorimetricColors(cColors: UInt32, cChannels: UInt32, pDeviceValues: POINTER(Single), pXYZColors: POINTER(win32more.UI.ColorSystem.XYZColorF_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def ColorimetricToDeviceColors(cColors: UInt32, cChannels: UInt32, pXYZColors: POINTER(win32more.UI.ColorSystem.XYZColorF_head), pDeviceValues: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def ColorimetricToDeviceColorsWithBlack(cColors: UInt32, cChannels: UInt32, pXYZColors: POINTER(win32more.UI.ColorSystem.XYZColorF_head), pBlackInformation: POINTER(win32more.UI.ColorSystem.BlackInformation_head), pDeviceValues: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetTransformDeviceModelInfo(iModelPosition: UInt32, pIDeviceModelOther: win32more.UI.ColorSystem.IDeviceModelPlugIn_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetPrimarySamples(pPrimaryColor: POINTER(win32more.UI.ColorSystem.PrimaryXYZColors_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetGamutBoundaryMeshSize(pNumVertices: POINTER(UInt32), pNumTriangles: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetGamutBoundaryMesh(cChannels: UInt32, cVertices: UInt32, cTriangles: UInt32, pVertices: POINTER(Single), pTriangles: POINTER(win32more.UI.ColorSystem.GamutShellTriangle_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetNeutralAxisSize(pcColors: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetNeutralAxis(cColors: UInt32, pXYZColors: POINTER(win32more.UI.ColorSystem.XYZColorF_head)) -> win32more.Foundation.HRESULT: ...
class IGamutMapModelPlugIn(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('2dd80115-ad1e-41f6-a2-19-a4-f4-b5-83-d1-f9')
    @commethod(3)
    def Initialize(bstrXml: win32more.Foundation.BSTR, pSrcPlugIn: win32more.UI.ColorSystem.IDeviceModelPlugIn_head, pDestPlugIn: win32more.UI.ColorSystem.IDeviceModelPlugIn_head, pSrcGBD: POINTER(win32more.UI.ColorSystem.GamutBoundaryDescription_head), pDestGBD: POINTER(win32more.UI.ColorSystem.GamutBoundaryDescription_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SourceToDestinationAppearanceColors(cColors: UInt32, pInputColors: POINTER(win32more.UI.ColorSystem.JChColorF_head), pOutputColors: POINTER(win32more.UI.ColorSystem.JChColorF_head)) -> win32more.Foundation.HRESULT: ...
class JabColorF(Structure):
    J: Single
    a: Single
    b: Single
class JChColorF(Structure):
    J: Single
    C: Single
    h: Single
class LabCOLOR(Structure):
    L: UInt16
    a: UInt16
    b: UInt16
class LOGCOLORSPACEA(Structure):
    lcsSignature: UInt32
    lcsVersion: UInt32
    lcsSize: UInt32
    lcsCSType: Int32
    lcsIntent: Int32
    lcsEndpoints: win32more.Graphics.Gdi.CIEXYZTRIPLE
    lcsGammaRed: UInt32
    lcsGammaGreen: UInt32
    lcsGammaBlue: UInt32
    lcsFilename: win32more.Foundation.CHAR * 260
class LOGCOLORSPACEW(Structure):
    lcsSignature: UInt32
    lcsVersion: UInt32
    lcsSize: UInt32
    lcsCSType: Int32
    lcsIntent: Int32
    lcsEndpoints: win32more.Graphics.Gdi.CIEXYZTRIPLE
    lcsGammaRed: UInt32
    lcsGammaGreen: UInt32
    lcsGammaBlue: UInt32
    lcsFilename: Char * 260
@winfunctype_pointer
def LPBMCALLBACKFN(param0: UInt32, param1: UInt32, param2: win32more.Foundation.LPARAM) -> win32more.Foundation.BOOL: ...
class NAMED_PROFILE_INFO(Structure):
    dwFlags: UInt32
    dwCount: UInt32
    dwCountDevCoordinates: UInt32
    szPrefix: SByte * 32
    szSuffix: SByte * 32
class NAMEDCOLOR(Structure):
    dwIndex: UInt32
@winfunctype_pointer
def PCMSCALLBACKA(param0: POINTER(win32more.UI.ColorSystem.COLORMATCHSETUPA_head), param1: win32more.Foundation.LPARAM) -> win32more.Foundation.BOOL: ...
@winfunctype_pointer
def PCMSCALLBACKW(param0: POINTER(win32more.UI.ColorSystem.COLORMATCHSETUPW_head), param1: win32more.Foundation.LPARAM) -> win32more.Foundation.BOOL: ...
class PrimaryJabColors(Structure):
    red: win32more.UI.ColorSystem.JabColorF
    yellow: win32more.UI.ColorSystem.JabColorF
    green: win32more.UI.ColorSystem.JabColorF
    cyan: win32more.UI.ColorSystem.JabColorF
    blue: win32more.UI.ColorSystem.JabColorF
    magenta: win32more.UI.ColorSystem.JabColorF
    black: win32more.UI.ColorSystem.JabColorF
    white: win32more.UI.ColorSystem.JabColorF
class PrimaryXYZColors(Structure):
    red: win32more.UI.ColorSystem.XYZColorF
    yellow: win32more.UI.ColorSystem.XYZColorF
    green: win32more.UI.ColorSystem.XYZColorF
    cyan: win32more.UI.ColorSystem.XYZColorF
    blue: win32more.UI.ColorSystem.XYZColorF
    magenta: win32more.UI.ColorSystem.XYZColorF
    black: win32more.UI.ColorSystem.XYZColorF
    white: win32more.UI.ColorSystem.XYZColorF
class PROFILE(Structure):
    dwType: UInt32
    pProfileData: c_void_p
    cbDataSize: UInt32
class PROFILEHEADER(Structure):
    phSize: UInt32
    phCMMType: UInt32
    phVersion: UInt32
    phClass: UInt32
    phDataColorSpace: UInt32
    phConnectionSpace: UInt32
    phDateTime: UInt32 * 3
    phSignature: UInt32
    phPlatform: UInt32
    phProfileFlags: UInt32
    phManufacturer: UInt32
    phModel: UInt32
    phAttributes: UInt32 * 2
    phRenderingIntent: UInt32
    phIlluminant: win32more.Graphics.Gdi.CIEXYZ
    phCreator: UInt32
    phReserved: Byte * 44
class RGBCOLOR(Structure):
    red: UInt16
    green: UInt16
    blue: UInt16
WCS_DEVICE_CAPABILITIES_TYPE = Int32
WCS_DEVICE_CAPABILITIES_TYPE_VideoCardGammaTable: WCS_DEVICE_CAPABILITIES_TYPE = 1
WCS_DEVICE_CAPABILITIES_TYPE_MicrosoftHardwareColorV2: WCS_DEVICE_CAPABILITIES_TYPE = 2
class WCS_DEVICE_MHC2_CAPABILITIES(Structure):
    Size: UInt32
    SupportsMhc2: win32more.Foundation.BOOL
    RegammaLutEntryCount: UInt32
    CscXyzMatrixRows: UInt32
    CscXyzMatrixColumns: UInt32
class WCS_DEVICE_VCGT_CAPABILITIES(Structure):
    Size: UInt32
    SupportsVcgt: win32more.Foundation.BOOL
WCS_PROFILE_MANAGEMENT_SCOPE = Int32
WCS_PROFILE_MANAGEMENT_SCOPE_SYSTEM_WIDE: WCS_PROFILE_MANAGEMENT_SCOPE = 0
WCS_PROFILE_MANAGEMENT_SCOPE_CURRENT_USER: WCS_PROFILE_MANAGEMENT_SCOPE = 1
class XYZCOLOR(Structure):
    X: UInt16
    Y: UInt16
    Z: UInt16
class XYZColorF(Structure):
    X: Single
    Y: Single
    Z: Single
class YxyCOLOR(Structure):
    Y: UInt16
    x: UInt16
    y: UInt16
make_head(_module, 'BlackInformation')
make_head(_module, 'CMYKCOLOR')
make_head(_module, 'COLOR')
make_head(_module, 'COLORMATCHSETUPA')
make_head(_module, 'COLORMATCHSETUPW')
make_head(_module, 'EMRCREATECOLORSPACE')
make_head(_module, 'EMRCREATECOLORSPACEW')
make_head(_module, 'ENUMTYPEA')
make_head(_module, 'ENUMTYPEW')
make_head(_module, 'GamutBoundaryDescription')
make_head(_module, 'GamutShell')
make_head(_module, 'GamutShellTriangle')
make_head(_module, 'GENERIC3CHANNEL')
make_head(_module, 'GRAYCOLOR')
make_head(_module, 'HiFiCOLOR')
make_head(_module, 'ICMENUMPROCA')
make_head(_module, 'ICMENUMPROCW')
make_head(_module, 'IDeviceModelPlugIn')
make_head(_module, 'IGamutMapModelPlugIn')
make_head(_module, 'JabColorF')
make_head(_module, 'JChColorF')
make_head(_module, 'LabCOLOR')
make_head(_module, 'LOGCOLORSPACEA')
make_head(_module, 'LOGCOLORSPACEW')
make_head(_module, 'LPBMCALLBACKFN')
make_head(_module, 'NAMED_PROFILE_INFO')
make_head(_module, 'NAMEDCOLOR')
make_head(_module, 'PCMSCALLBACKA')
make_head(_module, 'PCMSCALLBACKW')
make_head(_module, 'PrimaryJabColors')
make_head(_module, 'PrimaryXYZColors')
make_head(_module, 'PROFILE')
make_head(_module, 'PROFILEHEADER')
make_head(_module, 'RGBCOLOR')
make_head(_module, 'WCS_DEVICE_MHC2_CAPABILITIES')
make_head(_module, 'WCS_DEVICE_VCGT_CAPABILITIES')
make_head(_module, 'XYZCOLOR')
make_head(_module, 'XYZColorF')
make_head(_module, 'YxyCOLOR')
__all__ = [
    "ATTRIB_MATTE",
    "ATTRIB_TRANSPARENCY",
    "AssociateColorProfileWithDeviceA",
    "AssociateColorProfileWithDeviceW",
    "BEST_MODE",
    "BMFORMAT",
    "BM_10b_G3CH",
    "BM_10b_Lab",
    "BM_10b_RGB",
    "BM_10b_XYZ",
    "BM_10b_Yxy",
    "BM_16b_G3CH",
    "BM_16b_GRAY",
    "BM_16b_Lab",
    "BM_16b_RGB",
    "BM_16b_XYZ",
    "BM_16b_Yxy",
    "BM_32b_scARGB",
    "BM_32b_scRGB",
    "BM_565RGB",
    "BM_5CHANNEL",
    "BM_6CHANNEL",
    "BM_7CHANNEL",
    "BM_8CHANNEL",
    "BM_BGRTRIPLETS",
    "BM_CMYKQUADS",
    "BM_G3CHTRIPLETS",
    "BM_GRAY",
    "BM_KYMCQUADS",
    "BM_LabTRIPLETS",
    "BM_NAMED_INDEX",
    "BM_R10G10B10A2",
    "BM_R10G10B10A2_XR",
    "BM_R16G16B16A16_FLOAT",
    "BM_RGBTRIPLETS",
    "BM_S2DOT13FIXED_scARGB",
    "BM_S2DOT13FIXED_scRGB",
    "BM_XYZTRIPLETS",
    "BM_YxyTRIPLETS",
    "BM_x555G3CH",
    "BM_x555Lab",
    "BM_x555RGB",
    "BM_x555XYZ",
    "BM_x555Yxy",
    "BM_xBGRQUADS",
    "BM_xG3CHQUADS",
    "BM_xRGBQUADS",
    "BlackInformation",
    "CATID_WcsPlugin",
    "CMCheckColors",
    "CMCheckColorsInGamut",
    "CMCheckRGBs",
    "CMConvertColorNameToIndex",
    "CMConvertIndexToColorName",
    "CMCreateDeviceLinkProfile",
    "CMCreateMultiProfileTransform",
    "CMCreateProfile",
    "CMCreateProfileW",
    "CMCreateTransform",
    "CMCreateTransformExt",
    "CMCreateTransformExtW",
    "CMCreateTransformW",
    "CMDeleteTransform",
    "CMGetInfo",
    "CMGetNamedProfileInfo",
    "CMIsProfileValid",
    "CMM_DESCRIPTION",
    "CMM_DLL_VERSION",
    "CMM_DRIVER_VERSION",
    "CMM_FROM_PROFILE",
    "CMM_IDENT",
    "CMM_LOGOICON",
    "CMM_VERSION",
    "CMM_WIN_VERSION",
    "CMS_BACKWARD",
    "CMS_DISABLEICM",
    "CMS_DISABLEINTENT",
    "CMS_DISABLERENDERINTENT",
    "CMS_ENABLEPROOFING",
    "CMS_FORWARD",
    "CMS_MONITOROVERFLOW",
    "CMS_PRINTEROVERFLOW",
    "CMS_SETMONITORPROFILE",
    "CMS_SETPRINTERPROFILE",
    "CMS_SETPROOFINTENT",
    "CMS_SETRENDERINTENT",
    "CMS_SETTARGETPROFILE",
    "CMS_TARGETOVERFLOW",
    "CMS_USEAPPLYCALLBACK",
    "CMS_USEDESCRIPTION",
    "CMS_USEHOOK",
    "CMTranslateColors",
    "CMTranslateRGB",
    "CMTranslateRGBs",
    "CMTranslateRGBsExt",
    "CMYKCOLOR",
    "COLOR",
    "COLORDATATYPE",
    "COLORMATCHSETUPA",
    "COLORMATCHSETUPW",
    "COLORPROFILESUBTYPE",
    "COLORPROFILETYPE",
    "COLORTYPE",
    "COLOR_10b_R10G10B10A2",
    "COLOR_10b_R10G10B10A2_XR",
    "COLOR_3_CHANNEL",
    "COLOR_5_CHANNEL",
    "COLOR_6_CHANNEL",
    "COLOR_7_CHANNEL",
    "COLOR_8_CHANNEL",
    "COLOR_BYTE",
    "COLOR_CMYK",
    "COLOR_FLOAT",
    "COLOR_FLOAT16",
    "COLOR_GRAY",
    "COLOR_Lab",
    "COLOR_MATCH_TO_TARGET_ACTION",
    "COLOR_MATCH_VERSION",
    "COLOR_NAMED",
    "COLOR_RGB",
    "COLOR_S2DOT13FIXED",
    "COLOR_WORD",
    "COLOR_XYZ",
    "COLOR_Yxy",
    "CPST_ABSOLUTE_COLORIMETRIC",
    "CPST_CUSTOM_WORKING_SPACE",
    "CPST_EXTENDED_DISPLAY_COLOR_MODE",
    "CPST_NONE",
    "CPST_PERCEPTUAL",
    "CPST_RELATIVE_COLORIMETRIC",
    "CPST_RGB_WORKING_SPACE",
    "CPST_SATURATION",
    "CPST_STANDARD_DISPLAY_COLOR_MODE",
    "CPT_CAMP",
    "CPT_DMP",
    "CPT_GMMP",
    "CPT_ICC",
    "CSA_A",
    "CSA_ABC",
    "CSA_CMYK",
    "CSA_DEF",
    "CSA_DEFG",
    "CSA_GRAY",
    "CSA_Lab",
    "CSA_RGB",
    "CS_DELETE_TRANSFORM",
    "CS_DISABLE",
    "CS_ENABLE",
    "CheckBitmapBits",
    "CheckColors",
    "CheckColorsInGamut",
    "CloseColorProfile",
    "ColorCorrectPalette",
    "ColorMatchToTarget",
    "ColorProfileAddDisplayAssociation",
    "ColorProfileGetDisplayDefault",
    "ColorProfileGetDisplayList",
    "ColorProfileGetDisplayUserScope",
    "ColorProfileRemoveDisplayAssociation",
    "ColorProfileSetDisplayDefaultAssociation",
    "ConvertColorNameToIndex",
    "ConvertIndexToColorName",
    "CreateColorSpaceA",
    "CreateColorSpaceW",
    "CreateColorTransformA",
    "CreateColorTransformW",
    "CreateDeviceLinkProfile",
    "CreateMultiProfileTransform",
    "CreateProfileFromLogColorSpaceA",
    "CreateProfileFromLogColorSpaceW",
    "DONT_USE_EMBEDDED_WCS_PROFILES",
    "DeleteColorSpace",
    "DeleteColorTransform",
    "DisassociateColorProfileFromDeviceA",
    "DisassociateColorProfileFromDeviceW",
    "EMRCREATECOLORSPACE",
    "EMRCREATECOLORSPACEW",
    "ENABLE_GAMUT_CHECKING",
    "ENUMTYPEA",
    "ENUMTYPEW",
    "ENUM_TYPE_VERSION",
    "ET_ATTRIBUTES",
    "ET_CLASS",
    "ET_CMMTYPE",
    "ET_CONNECTIONSPACE",
    "ET_CREATOR",
    "ET_DATACOLORSPACE",
    "ET_DEVICECLASS",
    "ET_DEVICENAME",
    "ET_DITHERMODE",
    "ET_EXTENDEDDISPLAYCOLOR",
    "ET_MANUFACTURER",
    "ET_MEDIATYPE",
    "ET_MODEL",
    "ET_PLATFORM",
    "ET_PROFILEFLAGS",
    "ET_RENDERINGINTENT",
    "ET_RESOLUTION",
    "ET_SIGNATURE",
    "ET_STANDARDDISPLAYCOLOR",
    "EnumColorProfilesA",
    "EnumColorProfilesW",
    "EnumICMProfilesA",
    "EnumICMProfilesW",
    "FAST_TRANSLATE",
    "FLAG_DEPENDENTONDATA",
    "FLAG_EMBEDDEDPROFILE",
    "FLAG_ENABLE_CHROMATIC_ADAPTATION",
    "GENERIC3CHANNEL",
    "GRAYCOLOR",
    "GamutBoundaryDescription",
    "GamutShell",
    "GamutShellTriangle",
    "GetCMMInfo",
    "GetColorDirectoryA",
    "GetColorDirectoryW",
    "GetColorProfileElement",
    "GetColorProfileElementTag",
    "GetColorProfileFromHandle",
    "GetColorProfileHeader",
    "GetColorSpace",
    "GetCountColorProfileElements",
    "GetDeviceGammaRamp",
    "GetICMProfileA",
    "GetICMProfileW",
    "GetLogColorSpaceA",
    "GetLogColorSpaceW",
    "GetNamedProfileInfo",
    "GetPS2ColorRenderingDictionary",
    "GetPS2ColorRenderingIntent",
    "GetPS2ColorSpaceArray",
    "GetStandardColorSpaceProfileA",
    "GetStandardColorSpaceProfileW",
    "HCOLORSPACE",
    "HiFiCOLOR",
    "ICMENUMPROCA",
    "ICMENUMPROCW",
    "ICM_ADDPROFILE",
    "ICM_COMMAND",
    "ICM_DELETEPROFILE",
    "ICM_DONE_OUTSIDEDC",
    "ICM_MODE",
    "ICM_OFF",
    "ICM_ON",
    "ICM_QUERY",
    "ICM_QUERYMATCH",
    "ICM_QUERYPROFILE",
    "ICM_REGISTERICMATCHER",
    "ICM_SETDEFAULTPROFILE",
    "ICM_UNREGISTERICMATCHER",
    "IDeviceModelPlugIn",
    "IGamutMapModelPlugIn",
    "INDEX_DONT_CARE",
    "INTENT_ABSOLUTE_COLORIMETRIC",
    "INTENT_PERCEPTUAL",
    "INTENT_RELATIVE_COLORIMETRIC",
    "INTENT_SATURATION",
    "InstallColorProfileA",
    "InstallColorProfileW",
    "IsColorProfileTagPresent",
    "IsColorProfileValid",
    "JChColorF",
    "JabColorF",
    "LOGCOLORSPACEA",
    "LOGCOLORSPACEW",
    "LPBMCALLBACKFN",
    "LabCOLOR",
    "MAX_COLOR_CHANNELS",
    "NAMEDCOLOR",
    "NAMED_PROFILE_INFO",
    "NORMAL_MODE",
    "OpenColorProfileA",
    "OpenColorProfileW",
    "PCMSCALLBACKA",
    "PCMSCALLBACKW",
    "PRESERVEBLACK",
    "PROFILE",
    "PROFILEHEADER",
    "PROFILE_FILENAME",
    "PROFILE_MEMBUFFER",
    "PROFILE_READ",
    "PROFILE_READWRITE",
    "PROOF_MODE",
    "PrimaryJabColors",
    "PrimaryXYZColors",
    "RESERVED",
    "RGBCOLOR",
    "RegisterCMMA",
    "RegisterCMMW",
    "SEQUENTIAL_TRANSFORM",
    "SelectCMM",
    "SetColorProfileElement",
    "SetColorProfileElementReference",
    "SetColorProfileElementSize",
    "SetColorProfileHeader",
    "SetColorSpace",
    "SetDeviceGammaRamp",
    "SetICMMode",
    "SetICMProfileA",
    "SetICMProfileW",
    "SetStandardColorSpaceProfileA",
    "SetStandardColorSpaceProfileW",
    "SetupColorMatchingA",
    "SetupColorMatchingW",
    "TranslateBitmapBits",
    "TranslateColors",
    "USE_RELATIVE_COLORIMETRIC",
    "UninstallColorProfileA",
    "UninstallColorProfileW",
    "UnregisterCMMA",
    "UnregisterCMMW",
    "UpdateICMRegKeyA",
    "UpdateICMRegKeyW",
    "WCS_ALWAYS",
    "WCS_DEFAULT",
    "WCS_DEVICE_CAPABILITIES_TYPE",
    "WCS_DEVICE_CAPABILITIES_TYPE_MicrosoftHardwareColorV2",
    "WCS_DEVICE_CAPABILITIES_TYPE_VideoCardGammaTable",
    "WCS_DEVICE_MHC2_CAPABILITIES",
    "WCS_DEVICE_VCGT_CAPABILITIES",
    "WCS_ICCONLY",
    "WCS_PROFILE_MANAGEMENT_SCOPE",
    "WCS_PROFILE_MANAGEMENT_SCOPE_CURRENT_USER",
    "WCS_PROFILE_MANAGEMENT_SCOPE_SYSTEM_WIDE",
    "WcsAssociateColorProfileWithDevice",
    "WcsCheckColors",
    "WcsCreateIccProfile",
    "WcsDisassociateColorProfileFromDevice",
    "WcsEnumColorProfiles",
    "WcsEnumColorProfilesSize",
    "WcsGetCalibrationManagementState",
    "WcsGetDefaultColorProfile",
    "WcsGetDefaultColorProfileSize",
    "WcsGetDefaultRenderingIntent",
    "WcsGetUsePerUserProfiles",
    "WcsOpenColorProfileA",
    "WcsOpenColorProfileW",
    "WcsSetCalibrationManagementState",
    "WcsSetDefaultColorProfile",
    "WcsSetDefaultRenderingIntent",
    "WcsSetUsePerUserProfiles",
    "WcsTranslateColors",
    "XYZCOLOR",
    "XYZColorF",
    "YxyCOLOR",
]
_arch_optional = [
]
