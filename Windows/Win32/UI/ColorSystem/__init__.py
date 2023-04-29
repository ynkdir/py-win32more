from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Gdi
import Windows.Win32.System.Com
import Windows.Win32.UI.ColorSystem
import Windows.Win32.UI.WindowsAndMessaging
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
def SetICMMode(hdc: Windows.Win32.Graphics.Gdi.HDC, mode: Windows.Win32.UI.ColorSystem.ICM_MODE) -> Int32: ...
@winfunctype('GDI32.dll')
def CheckColorsInGamut(hdc: Windows.Win32.Graphics.Gdi.HDC, lpRGBTriple: POINTER(Windows.Win32.Graphics.Gdi.RGBTRIPLE_head), dlpBuffer: c_void_p, nCount: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def GetColorSpace(hdc: Windows.Win32.Graphics.Gdi.HDC) -> Windows.Win32.UI.ColorSystem.HCOLORSPACE: ...
@winfunctype('GDI32.dll')
def GetLogColorSpaceA(hColorSpace: Windows.Win32.UI.ColorSystem.HCOLORSPACE, lpBuffer: POINTER(Windows.Win32.UI.ColorSystem.LOGCOLORSPACEA_head), nSize: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def GetLogColorSpaceW(hColorSpace: Windows.Win32.UI.ColorSystem.HCOLORSPACE, lpBuffer: POINTER(Windows.Win32.UI.ColorSystem.LOGCOLORSPACEW_head), nSize: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def CreateColorSpaceA(lplcs: POINTER(Windows.Win32.UI.ColorSystem.LOGCOLORSPACEA_head)) -> Windows.Win32.UI.ColorSystem.HCOLORSPACE: ...
@winfunctype('GDI32.dll')
def CreateColorSpaceW(lplcs: POINTER(Windows.Win32.UI.ColorSystem.LOGCOLORSPACEW_head)) -> Windows.Win32.UI.ColorSystem.HCOLORSPACE: ...
@winfunctype('GDI32.dll')
def SetColorSpace(hdc: Windows.Win32.Graphics.Gdi.HDC, hcs: Windows.Win32.UI.ColorSystem.HCOLORSPACE) -> Windows.Win32.UI.ColorSystem.HCOLORSPACE: ...
@winfunctype('GDI32.dll')
def DeleteColorSpace(hcs: Windows.Win32.UI.ColorSystem.HCOLORSPACE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def GetICMProfileA(hdc: Windows.Win32.Graphics.Gdi.HDC, pBufSize: POINTER(UInt32), pszFilename: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def GetICMProfileW(hdc: Windows.Win32.Graphics.Gdi.HDC, pBufSize: POINTER(UInt32), pszFilename: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def SetICMProfileA(hdc: Windows.Win32.Graphics.Gdi.HDC, lpFileName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def SetICMProfileW(hdc: Windows.Win32.Graphics.Gdi.HDC, lpFileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def GetDeviceGammaRamp(hdc: Windows.Win32.Graphics.Gdi.HDC, lpRamp: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def SetDeviceGammaRamp(hdc: Windows.Win32.Graphics.Gdi.HDC, lpRamp: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def ColorMatchToTarget(hdc: Windows.Win32.Graphics.Gdi.HDC, hdcTarget: Windows.Win32.Graphics.Gdi.HDC, action: Windows.Win32.UI.ColorSystem.COLOR_MATCH_TO_TARGET_ACTION) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def EnumICMProfilesA(hdc: Windows.Win32.Graphics.Gdi.HDC, proc: Windows.Win32.UI.ColorSystem.ICMENUMPROCA, param2: Windows.Win32.Foundation.LPARAM) -> Int32: ...
@winfunctype('GDI32.dll')
def EnumICMProfilesW(hdc: Windows.Win32.Graphics.Gdi.HDC, proc: Windows.Win32.UI.ColorSystem.ICMENUMPROCW, param2: Windows.Win32.Foundation.LPARAM) -> Int32: ...
@winfunctype('GDI32.dll')
def UpdateICMRegKeyA(reserved: UInt32, lpszCMID: Windows.Win32.Foundation.PSTR, lpszFileName: Windows.Win32.Foundation.PSTR, command: Windows.Win32.UI.ColorSystem.ICM_COMMAND) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def UpdateICMRegKeyW(reserved: UInt32, lpszCMID: Windows.Win32.Foundation.PWSTR, lpszFileName: Windows.Win32.Foundation.PWSTR, command: Windows.Win32.UI.ColorSystem.ICM_COMMAND) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def ColorCorrectPalette(hdc: Windows.Win32.Graphics.Gdi.HDC, hPal: Windows.Win32.Graphics.Gdi.HPALETTE, deFirst: UInt32, num: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def OpenColorProfileA(pProfile: POINTER(Windows.Win32.UI.ColorSystem.PROFILE_head), dwDesiredAccess: UInt32, dwShareMode: UInt32, dwCreationMode: UInt32) -> IntPtr: ...
@winfunctype('mscms.dll')
def OpenColorProfileW(pProfile: POINTER(Windows.Win32.UI.ColorSystem.PROFILE_head), dwDesiredAccess: UInt32, dwShareMode: UInt32, dwCreationMode: UInt32) -> IntPtr: ...
@winfunctype('mscms.dll')
def CloseColorProfile(hProfile: IntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetColorProfileFromHandle(hProfile: IntPtr, pProfile: POINTER(Byte), pcbProfile: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def IsColorProfileValid(hProfile: IntPtr, pbValid: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def CreateProfileFromLogColorSpaceA(pLogColorSpace: POINTER(Windows.Win32.UI.ColorSystem.LOGCOLORSPACEA_head), pProfile: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def CreateProfileFromLogColorSpaceW(pLogColorSpace: POINTER(Windows.Win32.UI.ColorSystem.LOGCOLORSPACEW_head), pProfile: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetCountColorProfileElements(hProfile: IntPtr, pnElementCount: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetColorProfileHeader(hProfile: IntPtr, pHeader: POINTER(Windows.Win32.UI.ColorSystem.PROFILEHEADER_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetColorProfileElementTag(hProfile: IntPtr, dwIndex: UInt32, pTag: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def IsColorProfileTagPresent(hProfile: IntPtr, tag: UInt32, pbPresent: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetColorProfileElement(hProfile: IntPtr, tag: UInt32, dwOffset: UInt32, pcbElement: POINTER(UInt32), pElement: c_void_p, pbReference: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def SetColorProfileHeader(hProfile: IntPtr, pHeader: POINTER(Windows.Win32.UI.ColorSystem.PROFILEHEADER_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def SetColorProfileElementSize(hProfile: IntPtr, tagType: UInt32, pcbElement: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def SetColorProfileElement(hProfile: IntPtr, tag: UInt32, dwOffset: UInt32, pcbElement: POINTER(UInt32), pElement: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def SetColorProfileElementReference(hProfile: IntPtr, newTag: UInt32, refTag: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetPS2ColorSpaceArray(hProfile: IntPtr, dwIntent: UInt32, dwCSAType: UInt32, pPS2ColorSpaceArray: POINTER(Byte), pcbPS2ColorSpaceArray: POINTER(UInt32), pbBinary: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetPS2ColorRenderingIntent(hProfile: IntPtr, dwIntent: UInt32, pBuffer: POINTER(Byte), pcbPS2ColorRenderingIntent: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetPS2ColorRenderingDictionary(hProfile: IntPtr, dwIntent: UInt32, pPS2ColorRenderingDictionary: POINTER(Byte), pcbPS2ColorRenderingDictionary: POINTER(UInt32), pbBinary: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetNamedProfileInfo(hProfile: IntPtr, pNamedProfileInfo: POINTER(Windows.Win32.UI.ColorSystem.NAMED_PROFILE_INFO_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def ConvertColorNameToIndex(hProfile: IntPtr, paColorName: POINTER(POINTER(SByte)), paIndex: POINTER(UInt32), dwCount: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def ConvertIndexToColorName(hProfile: IntPtr, paIndex: POINTER(UInt32), paColorName: POINTER(POINTER(SByte)), dwCount: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def CreateDeviceLinkProfile(hProfile: POINTER(IntPtr), nProfiles: UInt32, padwIntent: POINTER(UInt32), nIntents: UInt32, dwFlags: UInt32, pProfileData: POINTER(POINTER(Byte)), indexPreferredCMM: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def CreateColorTransformA(pLogColorSpace: POINTER(Windows.Win32.UI.ColorSystem.LOGCOLORSPACEA_head), hDestProfile: IntPtr, hTargetProfile: IntPtr, dwFlags: UInt32) -> IntPtr: ...
@winfunctype('mscms.dll')
def CreateColorTransformW(pLogColorSpace: POINTER(Windows.Win32.UI.ColorSystem.LOGCOLORSPACEW_head), hDestProfile: IntPtr, hTargetProfile: IntPtr, dwFlags: UInt32) -> IntPtr: ...
@winfunctype('mscms.dll')
def CreateMultiProfileTransform(pahProfiles: POINTER(IntPtr), nProfiles: UInt32, padwIntent: POINTER(UInt32), nIntents: UInt32, dwFlags: UInt32, indexPreferredCMM: UInt32) -> IntPtr: ...
@winfunctype('mscms.dll')
def DeleteColorTransform(hxform: IntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def TranslateBitmapBits(hColorTransform: IntPtr, pSrcBits: c_void_p, bmInput: Windows.Win32.UI.ColorSystem.BMFORMAT, dwWidth: UInt32, dwHeight: UInt32, dwInputStride: UInt32, pDestBits: c_void_p, bmOutput: Windows.Win32.UI.ColorSystem.BMFORMAT, dwOutputStride: UInt32, pfnCallBack: Windows.Win32.UI.ColorSystem.LPBMCALLBACKFN, ulCallbackData: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def CheckBitmapBits(hColorTransform: IntPtr, pSrcBits: c_void_p, bmInput: Windows.Win32.UI.ColorSystem.BMFORMAT, dwWidth: UInt32, dwHeight: UInt32, dwStride: UInt32, paResult: POINTER(Byte), pfnCallback: Windows.Win32.UI.ColorSystem.LPBMCALLBACKFN, lpCallbackData: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def TranslateColors(hColorTransform: IntPtr, paInputColors: POINTER(Windows.Win32.UI.ColorSystem.COLOR_head), nColors: UInt32, ctInput: Windows.Win32.UI.ColorSystem.COLORTYPE, paOutputColors: POINTER(Windows.Win32.UI.ColorSystem.COLOR_head), ctOutput: Windows.Win32.UI.ColorSystem.COLORTYPE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def CheckColors(hColorTransform: IntPtr, paInputColors: POINTER(Windows.Win32.UI.ColorSystem.COLOR_head), nColors: UInt32, ctInput: Windows.Win32.UI.ColorSystem.COLORTYPE, paResult: POINTER(Byte)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetCMMInfo(hColorTransform: IntPtr, param1: UInt32) -> UInt32: ...
@winfunctype('mscms.dll')
def RegisterCMMA(pMachineName: Windows.Win32.Foundation.PSTR, cmmID: UInt32, pCMMdll: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def RegisterCMMW(pMachineName: Windows.Win32.Foundation.PWSTR, cmmID: UInt32, pCMMdll: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def UnregisterCMMA(pMachineName: Windows.Win32.Foundation.PSTR, cmmID: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def UnregisterCMMW(pMachineName: Windows.Win32.Foundation.PWSTR, cmmID: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def SelectCMM(dwCMMType: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetColorDirectoryA(pMachineName: Windows.Win32.Foundation.PSTR, pBuffer: Windows.Win32.Foundation.PSTR, pdwSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetColorDirectoryW(pMachineName: Windows.Win32.Foundation.PWSTR, pBuffer: Windows.Win32.Foundation.PWSTR, pdwSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def InstallColorProfileA(pMachineName: Windows.Win32.Foundation.PSTR, pProfileName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def InstallColorProfileW(pMachineName: Windows.Win32.Foundation.PWSTR, pProfileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def UninstallColorProfileA(pMachineName: Windows.Win32.Foundation.PSTR, pProfileName: Windows.Win32.Foundation.PSTR, bDelete: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def UninstallColorProfileW(pMachineName: Windows.Win32.Foundation.PWSTR, pProfileName: Windows.Win32.Foundation.PWSTR, bDelete: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def EnumColorProfilesA(pMachineName: Windows.Win32.Foundation.PSTR, pEnumRecord: POINTER(Windows.Win32.UI.ColorSystem.ENUMTYPEA_head), pEnumerationBuffer: POINTER(Byte), pdwSizeOfEnumerationBuffer: POINTER(UInt32), pnProfiles: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def EnumColorProfilesW(pMachineName: Windows.Win32.Foundation.PWSTR, pEnumRecord: POINTER(Windows.Win32.UI.ColorSystem.ENUMTYPEW_head), pEnumerationBuffer: POINTER(Byte), pdwSizeOfEnumerationBuffer: POINTER(UInt32), pnProfiles: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def SetStandardColorSpaceProfileA(pMachineName: Windows.Win32.Foundation.PSTR, dwProfileID: UInt32, pProfilename: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def SetStandardColorSpaceProfileW(pMachineName: Windows.Win32.Foundation.PWSTR, dwProfileID: UInt32, pProfileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetStandardColorSpaceProfileA(pMachineName: Windows.Win32.Foundation.PSTR, dwSCS: UInt32, pBuffer: Windows.Win32.Foundation.PSTR, pcbSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetStandardColorSpaceProfileW(pMachineName: Windows.Win32.Foundation.PWSTR, dwSCS: UInt32, pBuffer: Windows.Win32.Foundation.PWSTR, pcbSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def AssociateColorProfileWithDeviceA(pMachineName: Windows.Win32.Foundation.PSTR, pProfileName: Windows.Win32.Foundation.PSTR, pDeviceName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def AssociateColorProfileWithDeviceW(pMachineName: Windows.Win32.Foundation.PWSTR, pProfileName: Windows.Win32.Foundation.PWSTR, pDeviceName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def DisassociateColorProfileFromDeviceA(pMachineName: Windows.Win32.Foundation.PSTR, pProfileName: Windows.Win32.Foundation.PSTR, pDeviceName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def DisassociateColorProfileFromDeviceW(pMachineName: Windows.Win32.Foundation.PWSTR, pProfileName: Windows.Win32.Foundation.PWSTR, pDeviceName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ICMUI.dll')
def SetupColorMatchingW(pcms: POINTER(Windows.Win32.UI.ColorSystem.COLORMATCHSETUPW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ICMUI.dll')
def SetupColorMatchingA(pcms: POINTER(Windows.Win32.UI.ColorSystem.COLORMATCHSETUPA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsAssociateColorProfileWithDevice(scope: Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, pProfileName: Windows.Win32.Foundation.PWSTR, pDeviceName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsDisassociateColorProfileFromDevice(scope: Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, pProfileName: Windows.Win32.Foundation.PWSTR, pDeviceName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsEnumColorProfilesSize(scope: Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, pEnumRecord: POINTER(Windows.Win32.UI.ColorSystem.ENUMTYPEW_head), pdwSize: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsEnumColorProfiles(scope: Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, pEnumRecord: POINTER(Windows.Win32.UI.ColorSystem.ENUMTYPEW_head), pBuffer: POINTER(Byte), dwSize: UInt32, pnProfiles: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsGetDefaultColorProfileSize(scope: Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, pDeviceName: Windows.Win32.Foundation.PWSTR, cptColorProfileType: Windows.Win32.UI.ColorSystem.COLORPROFILETYPE, cpstColorProfileSubType: Windows.Win32.UI.ColorSystem.COLORPROFILESUBTYPE, dwProfileID: UInt32, pcbProfileName: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsGetDefaultColorProfile(scope: Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, pDeviceName: Windows.Win32.Foundation.PWSTR, cptColorProfileType: Windows.Win32.UI.ColorSystem.COLORPROFILETYPE, cpstColorProfileSubType: Windows.Win32.UI.ColorSystem.COLORPROFILESUBTYPE, dwProfileID: UInt32, cbProfileName: UInt32, pProfileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsSetDefaultColorProfile(scope: Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, pDeviceName: Windows.Win32.Foundation.PWSTR, cptColorProfileType: Windows.Win32.UI.ColorSystem.COLORPROFILETYPE, cpstColorProfileSubType: Windows.Win32.UI.ColorSystem.COLORPROFILESUBTYPE, dwProfileID: UInt32, pProfileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsSetDefaultRenderingIntent(scope: Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, dwRenderingIntent: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsGetDefaultRenderingIntent(scope: Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, pdwRenderingIntent: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsGetUsePerUserProfiles(pDeviceName: Windows.Win32.Foundation.PWSTR, dwDeviceClass: UInt32, pUsePerUserProfiles: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsSetUsePerUserProfiles(pDeviceName: Windows.Win32.Foundation.PWSTR, dwDeviceClass: UInt32, usePerUserProfiles: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsTranslateColors(hColorTransform: IntPtr, nColors: UInt32, nInputChannels: UInt32, cdtInput: Windows.Win32.UI.ColorSystem.COLORDATATYPE, cbInput: UInt32, pInputData: c_void_p, nOutputChannels: UInt32, cdtOutput: Windows.Win32.UI.ColorSystem.COLORDATATYPE, cbOutput: UInt32, pOutputData: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsCheckColors(hColorTransform: IntPtr, nColors: UInt32, nInputChannels: UInt32, cdtInput: Windows.Win32.UI.ColorSystem.COLORDATATYPE, cbInput: UInt32, pInputData: c_void_p, paResult: POINTER(Byte)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMCheckColors(hcmTransform: IntPtr, lpaInputColors: POINTER(Windows.Win32.UI.ColorSystem.COLOR_head), nColors: UInt32, ctInput: Windows.Win32.UI.ColorSystem.COLORTYPE, lpaResult: POINTER(Byte)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMCheckRGBs(hcmTransform: IntPtr, lpSrcBits: c_void_p, bmInput: Windows.Win32.UI.ColorSystem.BMFORMAT, dwWidth: UInt32, dwHeight: UInt32, dwStride: UInt32, lpaResult: POINTER(Byte), pfnCallback: Windows.Win32.UI.ColorSystem.LPBMCALLBACKFN, ulCallbackData: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMConvertColorNameToIndex(hProfile: IntPtr, paColorName: POINTER(POINTER(SByte)), paIndex: POINTER(UInt32), dwCount: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMConvertIndexToColorName(hProfile: IntPtr, paIndex: POINTER(UInt32), paColorName: POINTER(POINTER(SByte)), dwCount: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMCreateDeviceLinkProfile(pahProfiles: POINTER(IntPtr), nProfiles: UInt32, padwIntents: POINTER(UInt32), nIntents: UInt32, dwFlags: UInt32, lpProfileData: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMCreateMultiProfileTransform(pahProfiles: POINTER(IntPtr), nProfiles: UInt32, padwIntents: POINTER(UInt32), nIntents: UInt32, dwFlags: UInt32) -> IntPtr: ...
@winfunctype('ICM32.dll')
def CMCreateProfileW(lpColorSpace: POINTER(Windows.Win32.UI.ColorSystem.LOGCOLORSPACEW_head), lpProfileData: POINTER(c_void_p)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMCreateTransform(lpColorSpace: POINTER(Windows.Win32.UI.ColorSystem.LOGCOLORSPACEA_head), lpDevCharacter: c_void_p, lpTargetDevCharacter: c_void_p) -> IntPtr: ...
@winfunctype('ICM32.dll')
def CMCreateTransformW(lpColorSpace: POINTER(Windows.Win32.UI.ColorSystem.LOGCOLORSPACEW_head), lpDevCharacter: c_void_p, lpTargetDevCharacter: c_void_p) -> IntPtr: ...
@winfunctype('ICM32.dll')
def CMCreateTransformExt(lpColorSpace: POINTER(Windows.Win32.UI.ColorSystem.LOGCOLORSPACEA_head), lpDevCharacter: c_void_p, lpTargetDevCharacter: c_void_p, dwFlags: UInt32) -> IntPtr: ...
@winfunctype('ICM32.dll')
def CMCheckColorsInGamut(hcmTransform: IntPtr, lpaRGBTriple: POINTER(Windows.Win32.Graphics.Gdi.RGBTRIPLE_head), lpaResult: POINTER(Byte), nCount: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMCreateProfile(lpColorSpace: POINTER(Windows.Win32.UI.ColorSystem.LOGCOLORSPACEA_head), lpProfileData: POINTER(c_void_p)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMTranslateRGB(hcmTransform: IntPtr, ColorRef: Windows.Win32.Foundation.COLORREF, lpColorRef: POINTER(UInt32), dwFlags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMTranslateRGBs(hcmTransform: IntPtr, lpSrcBits: c_void_p, bmInput: Windows.Win32.UI.ColorSystem.BMFORMAT, dwWidth: UInt32, dwHeight: UInt32, dwStride: UInt32, lpDestBits: c_void_p, bmOutput: Windows.Win32.UI.ColorSystem.BMFORMAT, dwTranslateDirection: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMCreateTransformExtW(lpColorSpace: POINTER(Windows.Win32.UI.ColorSystem.LOGCOLORSPACEW_head), lpDevCharacter: c_void_p, lpTargetDevCharacter: c_void_p, dwFlags: UInt32) -> IntPtr: ...
@winfunctype('ICM32.dll')
def CMDeleteTransform(hcmTransform: IntPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMGetInfo(dwInfo: UInt32) -> UInt32: ...
@winfunctype('ICM32.dll')
def CMGetNamedProfileInfo(hProfile: IntPtr, pNamedProfileInfo: POINTER(Windows.Win32.UI.ColorSystem.NAMED_PROFILE_INFO_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMIsProfileValid(hProfile: IntPtr, lpbValid: POINTER(Int32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMTranslateColors(hcmTransform: IntPtr, lpaInputColors: POINTER(Windows.Win32.UI.ColorSystem.COLOR_head), nColors: UInt32, ctInput: Windows.Win32.UI.ColorSystem.COLORTYPE, lpaOutputColors: POINTER(Windows.Win32.UI.ColorSystem.COLOR_head), ctOutput: Windows.Win32.UI.ColorSystem.COLORTYPE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMTranslateRGBsExt(hcmTransform: IntPtr, lpSrcBits: c_void_p, bmInput: Windows.Win32.UI.ColorSystem.BMFORMAT, dwWidth: UInt32, dwHeight: UInt32, dwInputStride: UInt32, lpDestBits: c_void_p, bmOutput: Windows.Win32.UI.ColorSystem.BMFORMAT, dwOutputStride: UInt32, lpfnCallback: Windows.Win32.UI.ColorSystem.LPBMCALLBACKFN, ulCallbackData: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsOpenColorProfileA(pCDMPProfile: POINTER(Windows.Win32.UI.ColorSystem.PROFILE_head), pCAMPProfile: POINTER(Windows.Win32.UI.ColorSystem.PROFILE_head), pGMMPProfile: POINTER(Windows.Win32.UI.ColorSystem.PROFILE_head), dwDesireAccess: UInt32, dwShareMode: UInt32, dwCreationMode: UInt32, dwFlags: UInt32) -> IntPtr: ...
@winfunctype('mscms.dll')
def WcsOpenColorProfileW(pCDMPProfile: POINTER(Windows.Win32.UI.ColorSystem.PROFILE_head), pCAMPProfile: POINTER(Windows.Win32.UI.ColorSystem.PROFILE_head), pGMMPProfile: POINTER(Windows.Win32.UI.ColorSystem.PROFILE_head), dwDesireAccess: UInt32, dwShareMode: UInt32, dwCreationMode: UInt32, dwFlags: UInt32) -> IntPtr: ...
@winfunctype('mscms.dll')
def WcsCreateIccProfile(hWcsProfile: IntPtr, dwOptions: UInt32) -> IntPtr: ...
@winfunctype('mscms.dll')
def WcsGetCalibrationManagementState(pbIsEnabled: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsSetCalibrationManagementState(bIsEnabled: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def ColorProfileAddDisplayAssociation(scope: Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, profileName: Windows.Win32.Foundation.PWSTR, targetAdapterID: Windows.Win32.Foundation.LUID, sourceID: UInt32, setAsDefault: Windows.Win32.Foundation.BOOL, associateAsAdvancedColor: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('mscms.dll')
def ColorProfileRemoveDisplayAssociation(scope: Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, profileName: Windows.Win32.Foundation.PWSTR, targetAdapterID: Windows.Win32.Foundation.LUID, sourceID: UInt32, dissociateAdvancedColor: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('mscms.dll')
def ColorProfileSetDisplayDefaultAssociation(scope: Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, profileName: Windows.Win32.Foundation.PWSTR, profileType: Windows.Win32.UI.ColorSystem.COLORPROFILETYPE, profileSubType: Windows.Win32.UI.ColorSystem.COLORPROFILESUBTYPE, targetAdapterID: Windows.Win32.Foundation.LUID, sourceID: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('mscms.dll')
def ColorProfileGetDisplayList(scope: Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, targetAdapterID: Windows.Win32.Foundation.LUID, sourceID: UInt32, profileList: POINTER(POINTER(Windows.Win32.Foundation.PWSTR)), profileCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('mscms.dll')
def ColorProfileGetDisplayDefault(scope: Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, targetAdapterID: Windows.Win32.Foundation.LUID, sourceID: UInt32, profileType: Windows.Win32.UI.ColorSystem.COLORPROFILETYPE, profileSubType: Windows.Win32.UI.ColorSystem.COLORPROFILESUBTYPE, profileName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('mscms.dll')
def ColorProfileGetDisplayUserScope(targetAdapterID: Windows.Win32.Foundation.LUID, sourceID: UInt32, scope: POINTER(Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE)) -> Windows.Win32.Foundation.HRESULT: ...
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
class BlackInformation(EasyCastStructure):
    fBlackOnly: Windows.Win32.Foundation.BOOL
    blackWeight: Single
class CMYKCOLOR(EasyCastStructure):
    cyan: UInt16
    magenta: UInt16
    yellow: UInt16
    black: UInt16
class COLOR(EasyCastUnion):
    gray: Windows.Win32.UI.ColorSystem.GRAYCOLOR
    rgb: Windows.Win32.UI.ColorSystem.RGBCOLOR
    cmyk: Windows.Win32.UI.ColorSystem.CMYKCOLOR
    XYZ: Windows.Win32.UI.ColorSystem.XYZCOLOR
    Yxy: Windows.Win32.UI.ColorSystem.YxyCOLOR
    Lab: Windows.Win32.UI.ColorSystem.LabCOLOR
    gen3ch: Windows.Win32.UI.ColorSystem.GENERIC3CHANNEL
    named: Windows.Win32.UI.ColorSystem.NAMEDCOLOR
    hifi: Windows.Win32.UI.ColorSystem.HiFiCOLOR
    Anonymous: _Anonymous_e__Struct
    class _Anonymous_e__Struct(EasyCastStructure):
        reserved1: UInt32
        reserved2: c_void_p
COLORDATATYPE = Int32
COLOR_BYTE: COLORDATATYPE = 1
COLOR_WORD: COLORDATATYPE = 2
COLOR_FLOAT: COLORDATATYPE = 3
COLOR_S2DOT13FIXED: COLORDATATYPE = 4
COLOR_10b_R10G10B10A2: COLORDATATYPE = 5
COLOR_10b_R10G10B10A2_XR: COLORDATATYPE = 6
COLOR_FLOAT16: COLORDATATYPE = 7
class COLORMATCHSETUPA(EasyCastStructure):
    dwSize: UInt32
    dwVersion: UInt32
    dwFlags: UInt32
    hwndOwner: Windows.Win32.Foundation.HWND
    pSourceName: Windows.Win32.Foundation.PSTR
    pDisplayName: Windows.Win32.Foundation.PSTR
    pPrinterName: Windows.Win32.Foundation.PSTR
    dwRenderIntent: UInt32
    dwProofingIntent: UInt32
    pMonitorProfile: Windows.Win32.Foundation.PSTR
    ccMonitorProfile: UInt32
    pPrinterProfile: Windows.Win32.Foundation.PSTR
    ccPrinterProfile: UInt32
    pTargetProfile: Windows.Win32.Foundation.PSTR
    ccTargetProfile: UInt32
    lpfnHook: Windows.Win32.UI.WindowsAndMessaging.DLGPROC
    lParam: Windows.Win32.Foundation.LPARAM
    lpfnApplyCallback: Windows.Win32.UI.ColorSystem.PCMSCALLBACKA
    lParamApplyCallback: Windows.Win32.Foundation.LPARAM
class COLORMATCHSETUPW(EasyCastStructure):
    dwSize: UInt32
    dwVersion: UInt32
    dwFlags: UInt32
    hwndOwner: Windows.Win32.Foundation.HWND
    pSourceName: Windows.Win32.Foundation.PWSTR
    pDisplayName: Windows.Win32.Foundation.PWSTR
    pPrinterName: Windows.Win32.Foundation.PWSTR
    dwRenderIntent: UInt32
    dwProofingIntent: UInt32
    pMonitorProfile: Windows.Win32.Foundation.PWSTR
    ccMonitorProfile: UInt32
    pPrinterProfile: Windows.Win32.Foundation.PWSTR
    ccPrinterProfile: UInt32
    pTargetProfile: Windows.Win32.Foundation.PWSTR
    ccTargetProfile: UInt32
    lpfnHook: Windows.Win32.UI.WindowsAndMessaging.DLGPROC
    lParam: Windows.Win32.Foundation.LPARAM
    lpfnApplyCallback: Windows.Win32.UI.ColorSystem.PCMSCALLBACKW
    lParamApplyCallback: Windows.Win32.Foundation.LPARAM
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
COLOR_MATCH_TO_TARGET_ACTION = Int32
CS_ENABLE: COLOR_MATCH_TO_TARGET_ACTION = 1
CS_DISABLE: COLOR_MATCH_TO_TARGET_ACTION = 2
CS_DELETE_TRANSFORM: COLOR_MATCH_TO_TARGET_ACTION = 3
class EMRCREATECOLORSPACE(EasyCastStructure):
    emr: Windows.Win32.Graphics.Gdi.EMR
    ihCS: UInt32
    lcs: Windows.Win32.UI.ColorSystem.LOGCOLORSPACEA
class EMRCREATECOLORSPACEW(EasyCastStructure):
    emr: Windows.Win32.Graphics.Gdi.EMR
    ihCS: UInt32
    lcs: Windows.Win32.UI.ColorSystem.LOGCOLORSPACEW
    dwFlags: UInt32
    cbData: UInt32
    Data: Byte * 1
class ENUMTYPEA(EasyCastStructure):
    dwSize: UInt32
    dwVersion: UInt32
    dwFields: UInt32
    pDeviceName: Windows.Win32.Foundation.PSTR
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
class ENUMTYPEW(EasyCastStructure):
    dwSize: UInt32
    dwVersion: UInt32
    dwFields: UInt32
    pDeviceName: Windows.Win32.Foundation.PWSTR
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
class GENERIC3CHANNEL(EasyCastStructure):
    ch1: UInt16
    ch2: UInt16
    ch3: UInt16
class GRAYCOLOR(EasyCastStructure):
    gray: UInt16
class GamutBoundaryDescription(EasyCastStructure):
    pPrimaries: POINTER(Windows.Win32.UI.ColorSystem.PrimaryJabColors_head)
    cNeutralSamples: UInt32
    pNeutralSamples: POINTER(Windows.Win32.UI.ColorSystem.JabColorF_head)
    pReferenceShell: POINTER(Windows.Win32.UI.ColorSystem.GamutShell_head)
    pPlausibleShell: POINTER(Windows.Win32.UI.ColorSystem.GamutShell_head)
    pPossibleShell: POINTER(Windows.Win32.UI.ColorSystem.GamutShell_head)
class GamutShell(EasyCastStructure):
    JMin: Single
    JMax: Single
    cVertices: UInt32
    cTriangles: UInt32
    pVertices: POINTER(Windows.Win32.UI.ColorSystem.JabColorF_head)
    pTriangles: POINTER(Windows.Win32.UI.ColorSystem.GamutShellTriangle_head)
class GamutShellTriangle(EasyCastStructure):
    aVertexIndex: UInt32 * 3
HCOLORSPACE = IntPtr
class HiFiCOLOR(EasyCastStructure):
    channel: Byte * 8
@winfunctype_pointer
def ICMENUMPROCA(param0: Windows.Win32.Foundation.PSTR, param1: Windows.Win32.Foundation.LPARAM) -> Int32: ...
@winfunctype_pointer
def ICMENUMPROCW(param0: Windows.Win32.Foundation.PWSTR, param1: Windows.Win32.Foundation.LPARAM) -> Int32: ...
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
class IDeviceModelPlugIn(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('1cd63475-07c4-46fe-a9-03-d6-55-31-6d-11-fd')
    @commethod(3)
    def Initialize(self, bstrXml: Windows.Win32.Foundation.BSTR, cNumModels: UInt32, iModelPosition: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNumChannels(self, pNumChannels: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DeviceToColorimetricColors(self, cColors: UInt32, cChannels: UInt32, pDeviceValues: POINTER(Single), pXYZColors: POINTER(Windows.Win32.UI.ColorSystem.XYZColorF_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ColorimetricToDeviceColors(self, cColors: UInt32, cChannels: UInt32, pXYZColors: POINTER(Windows.Win32.UI.ColorSystem.XYZColorF_head), pDeviceValues: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ColorimetricToDeviceColorsWithBlack(self, cColors: UInt32, cChannels: UInt32, pXYZColors: POINTER(Windows.Win32.UI.ColorSystem.XYZColorF_head), pBlackInformation: POINTER(Windows.Win32.UI.ColorSystem.BlackInformation_head), pDeviceValues: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetTransformDeviceModelInfo(self, iModelPosition: UInt32, pIDeviceModelOther: Windows.Win32.UI.ColorSystem.IDeviceModelPlugIn_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetPrimarySamples(self, pPrimaryColor: POINTER(Windows.Win32.UI.ColorSystem.PrimaryXYZColors_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetGamutBoundaryMeshSize(self, pNumVertices: POINTER(UInt32), pNumTriangles: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetGamutBoundaryMesh(self, cChannels: UInt32, cVertices: UInt32, cTriangles: UInt32, pVertices: POINTER(Single), pTriangles: POINTER(Windows.Win32.UI.ColorSystem.GamutShellTriangle_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetNeutralAxisSize(self, pcColors: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetNeutralAxis(self, cColors: UInt32, pXYZColors: POINTER(Windows.Win32.UI.ColorSystem.XYZColorF_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IGamutMapModelPlugIn(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('2dd80115-ad1e-41f6-a2-19-a4-f4-b5-83-d1-f9')
    @commethod(3)
    def Initialize(self, bstrXml: Windows.Win32.Foundation.BSTR, pSrcPlugIn: Windows.Win32.UI.ColorSystem.IDeviceModelPlugIn_head, pDestPlugIn: Windows.Win32.UI.ColorSystem.IDeviceModelPlugIn_head, pSrcGBD: POINTER(Windows.Win32.UI.ColorSystem.GamutBoundaryDescription_head), pDestGBD: POINTER(Windows.Win32.UI.ColorSystem.GamutBoundaryDescription_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SourceToDestinationAppearanceColors(self, cColors: UInt32, pInputColors: POINTER(Windows.Win32.UI.ColorSystem.JChColorF_head), pOutputColors: POINTER(Windows.Win32.UI.ColorSystem.JChColorF_head)) -> Windows.Win32.Foundation.HRESULT: ...
class JChColorF(EasyCastStructure):
    J: Single
    C: Single
    h: Single
class JabColorF(EasyCastStructure):
    J: Single
    a: Single
    b: Single
class LOGCOLORSPACEA(EasyCastStructure):
    lcsSignature: UInt32
    lcsVersion: UInt32
    lcsSize: UInt32
    lcsCSType: Int32
    lcsIntent: Int32
    lcsEndpoints: Windows.Win32.Graphics.Gdi.CIEXYZTRIPLE
    lcsGammaRed: UInt32
    lcsGammaGreen: UInt32
    lcsGammaBlue: UInt32
    lcsFilename: Windows.Win32.Foundation.CHAR * 260
class LOGCOLORSPACEW(EasyCastStructure):
    lcsSignature: UInt32
    lcsVersion: UInt32
    lcsSize: UInt32
    lcsCSType: Int32
    lcsIntent: Int32
    lcsEndpoints: Windows.Win32.Graphics.Gdi.CIEXYZTRIPLE
    lcsGammaRed: UInt32
    lcsGammaGreen: UInt32
    lcsGammaBlue: UInt32
    lcsFilename: Char * 260
@winfunctype_pointer
def LPBMCALLBACKFN(param0: UInt32, param1: UInt32, param2: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.BOOL: ...
class LabCOLOR(EasyCastStructure):
    L: UInt16
    a: UInt16
    b: UInt16
class NAMEDCOLOR(EasyCastStructure):
    dwIndex: UInt32
class NAMED_PROFILE_INFO(EasyCastStructure):
    dwFlags: UInt32
    dwCount: UInt32
    dwCountDevCoordinates: UInt32
    szPrefix: SByte * 32
    szSuffix: SByte * 32
@winfunctype_pointer
def PCMSCALLBACKA(param0: POINTER(Windows.Win32.UI.ColorSystem.COLORMATCHSETUPA_head), param1: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PCMSCALLBACKW(param0: POINTER(Windows.Win32.UI.ColorSystem.COLORMATCHSETUPW_head), param1: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.BOOL: ...
class PROFILE(EasyCastStructure):
    dwType: UInt32
    pProfileData: c_void_p
    cbDataSize: UInt32
class PROFILEHEADER(EasyCastStructure):
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
    phIlluminant: Windows.Win32.Graphics.Gdi.CIEXYZ
    phCreator: UInt32
    phReserved: Byte * 44
class PrimaryJabColors(EasyCastStructure):
    red: Windows.Win32.UI.ColorSystem.JabColorF
    yellow: Windows.Win32.UI.ColorSystem.JabColorF
    green: Windows.Win32.UI.ColorSystem.JabColorF
    cyan: Windows.Win32.UI.ColorSystem.JabColorF
    blue: Windows.Win32.UI.ColorSystem.JabColorF
    magenta: Windows.Win32.UI.ColorSystem.JabColorF
    black: Windows.Win32.UI.ColorSystem.JabColorF
    white: Windows.Win32.UI.ColorSystem.JabColorF
class PrimaryXYZColors(EasyCastStructure):
    red: Windows.Win32.UI.ColorSystem.XYZColorF
    yellow: Windows.Win32.UI.ColorSystem.XYZColorF
    green: Windows.Win32.UI.ColorSystem.XYZColorF
    cyan: Windows.Win32.UI.ColorSystem.XYZColorF
    blue: Windows.Win32.UI.ColorSystem.XYZColorF
    magenta: Windows.Win32.UI.ColorSystem.XYZColorF
    black: Windows.Win32.UI.ColorSystem.XYZColorF
    white: Windows.Win32.UI.ColorSystem.XYZColorF
class RGBCOLOR(EasyCastStructure):
    red: UInt16
    green: UInt16
    blue: UInt16
WCS_DEVICE_CAPABILITIES_TYPE = Int32
WCS_DEVICE_CAPABILITIES_TYPE_VideoCardGammaTable: WCS_DEVICE_CAPABILITIES_TYPE = 1
WCS_DEVICE_CAPABILITIES_TYPE_MicrosoftHardwareColorV2: WCS_DEVICE_CAPABILITIES_TYPE = 2
class WCS_DEVICE_MHC2_CAPABILITIES(EasyCastStructure):
    Size: UInt32
    SupportsMhc2: Windows.Win32.Foundation.BOOL
    RegammaLutEntryCount: UInt32
    CscXyzMatrixRows: UInt32
    CscXyzMatrixColumns: UInt32
class WCS_DEVICE_VCGT_CAPABILITIES(EasyCastStructure):
    Size: UInt32
    SupportsVcgt: Windows.Win32.Foundation.BOOL
WCS_PROFILE_MANAGEMENT_SCOPE = Int32
WCS_PROFILE_MANAGEMENT_SCOPE_SYSTEM_WIDE: WCS_PROFILE_MANAGEMENT_SCOPE = 0
WCS_PROFILE_MANAGEMENT_SCOPE_CURRENT_USER: WCS_PROFILE_MANAGEMENT_SCOPE = 1
class XYZCOLOR(EasyCastStructure):
    X: UInt16
    Y: UInt16
    Z: UInt16
class XYZColorF(EasyCastStructure):
    X: Single
    Y: Single
    Z: Single
class YxyCOLOR(EasyCastStructure):
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
make_head(_module, 'GENERIC3CHANNEL')
make_head(_module, 'GRAYCOLOR')
make_head(_module, 'GamutBoundaryDescription')
make_head(_module, 'GamutShell')
make_head(_module, 'GamutShellTriangle')
make_head(_module, 'HiFiCOLOR')
make_head(_module, 'ICMENUMPROCA')
make_head(_module, 'ICMENUMPROCW')
make_head(_module, 'IDeviceModelPlugIn')
make_head(_module, 'IGamutMapModelPlugIn')
make_head(_module, 'JChColorF')
make_head(_module, 'JabColorF')
make_head(_module, 'LOGCOLORSPACEA')
make_head(_module, 'LOGCOLORSPACEW')
make_head(_module, 'LPBMCALLBACKFN')
make_head(_module, 'LabCOLOR')
make_head(_module, 'NAMEDCOLOR')
make_head(_module, 'NAMED_PROFILE_INFO')
make_head(_module, 'PCMSCALLBACKA')
make_head(_module, 'PCMSCALLBACKW')
make_head(_module, 'PROFILE')
make_head(_module, 'PROFILEHEADER')
make_head(_module, 'PrimaryJabColors')
make_head(_module, 'PrimaryXYZColors')
make_head(_module, 'RGBCOLOR')
make_head(_module, 'WCS_DEVICE_MHC2_CAPABILITIES')
make_head(_module, 'WCS_DEVICE_VCGT_CAPABILITIES')
make_head(_module, 'XYZCOLOR')
make_head(_module, 'XYZColorF')
make_head(_module, 'YxyCOLOR')
