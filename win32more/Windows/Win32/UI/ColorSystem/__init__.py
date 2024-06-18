from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.UI.ColorSystem
import win32more.Windows.Win32.UI.WindowsAndMessaging
CATID_WcsPlugin: Guid = Guid('{a0b402e0-8240-405f-8a16-8a5b4df2f0dd}')
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
def SetICMMode(hdc: win32more.Windows.Win32.Graphics.Gdi.HDC, mode: win32more.Windows.Win32.UI.ColorSystem.ICM_MODE) -> Int32: ...
@winfunctype('GDI32.dll')
def CheckColorsInGamut(hdc: win32more.Windows.Win32.Graphics.Gdi.HDC, lpRGBTriple: POINTER(win32more.Windows.Win32.Graphics.Gdi.RGBTRIPLE), dlpBuffer: VoidPtr, nCount: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def GetColorSpace(hdc: win32more.Windows.Win32.Graphics.Gdi.HDC) -> win32more.Windows.Win32.UI.ColorSystem.HCOLORSPACE: ...
@winfunctype('GDI32.dll')
def GetLogColorSpaceA(hColorSpace: win32more.Windows.Win32.UI.ColorSystem.HCOLORSPACE, lpBuffer: POINTER(win32more.Windows.Win32.UI.ColorSystem.LOGCOLORSPACEA), nSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def GetLogColorSpaceW(hColorSpace: win32more.Windows.Win32.UI.ColorSystem.HCOLORSPACE, lpBuffer: POINTER(win32more.Windows.Win32.UI.ColorSystem.LOGCOLORSPACEW), nSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
GetLogColorSpace = UnicodeAlias('GetLogColorSpaceW')
@winfunctype('GDI32.dll')
def CreateColorSpaceA(lplcs: POINTER(win32more.Windows.Win32.UI.ColorSystem.LOGCOLORSPACEA)) -> win32more.Windows.Win32.UI.ColorSystem.HCOLORSPACE: ...
@winfunctype('GDI32.dll')
def CreateColorSpaceW(lplcs: POINTER(win32more.Windows.Win32.UI.ColorSystem.LOGCOLORSPACEW)) -> win32more.Windows.Win32.UI.ColorSystem.HCOLORSPACE: ...
CreateColorSpace = UnicodeAlias('CreateColorSpaceW')
@winfunctype('GDI32.dll')
def SetColorSpace(hdc: win32more.Windows.Win32.Graphics.Gdi.HDC, hcs: win32more.Windows.Win32.UI.ColorSystem.HCOLORSPACE) -> win32more.Windows.Win32.UI.ColorSystem.HCOLORSPACE: ...
@winfunctype('GDI32.dll')
def DeleteColorSpace(hcs: win32more.Windows.Win32.UI.ColorSystem.HCOLORSPACE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def GetICMProfileA(hdc: win32more.Windows.Win32.Graphics.Gdi.HDC, pBufSize: POINTER(UInt32), pszFilename: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def GetICMProfileW(hdc: win32more.Windows.Win32.Graphics.Gdi.HDC, pBufSize: POINTER(UInt32), pszFilename: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
GetICMProfile = UnicodeAlias('GetICMProfileW')
@winfunctype('GDI32.dll')
def SetICMProfileA(hdc: win32more.Windows.Win32.Graphics.Gdi.HDC, lpFileName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def SetICMProfileW(hdc: win32more.Windows.Win32.Graphics.Gdi.HDC, lpFileName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
SetICMProfile = UnicodeAlias('SetICMProfileW')
@winfunctype('GDI32.dll')
def GetDeviceGammaRamp(hdc: win32more.Windows.Win32.Graphics.Gdi.HDC, lpRamp: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def SetDeviceGammaRamp(hdc: win32more.Windows.Win32.Graphics.Gdi.HDC, lpRamp: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def ColorMatchToTarget(hdc: win32more.Windows.Win32.Graphics.Gdi.HDC, hdcTarget: win32more.Windows.Win32.Graphics.Gdi.HDC, action: win32more.Windows.Win32.UI.ColorSystem.COLOR_MATCH_TO_TARGET_ACTION) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def EnumICMProfilesA(hdc: win32more.Windows.Win32.Graphics.Gdi.HDC, proc: win32more.Windows.Win32.UI.ColorSystem.ICMENUMPROCA, param2: win32more.Windows.Win32.Foundation.LPARAM) -> Int32: ...
@winfunctype('GDI32.dll')
def EnumICMProfilesW(hdc: win32more.Windows.Win32.Graphics.Gdi.HDC, proc: win32more.Windows.Win32.UI.ColorSystem.ICMENUMPROCW, param2: win32more.Windows.Win32.Foundation.LPARAM) -> Int32: ...
EnumICMProfiles = UnicodeAlias('EnumICMProfilesW')
@winfunctype('GDI32.dll')
def UpdateICMRegKeyA(reserved: UInt32, lpszCMID: win32more.Windows.Win32.Foundation.PSTR, lpszFileName: win32more.Windows.Win32.Foundation.PSTR, command: win32more.Windows.Win32.UI.ColorSystem.ICM_COMMAND) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('GDI32.dll')
def UpdateICMRegKeyW(reserved: UInt32, lpszCMID: win32more.Windows.Win32.Foundation.PWSTR, lpszFileName: win32more.Windows.Win32.Foundation.PWSTR, command: win32more.Windows.Win32.UI.ColorSystem.ICM_COMMAND) -> win32more.Windows.Win32.Foundation.BOOL: ...
UpdateICMRegKey = UnicodeAlias('UpdateICMRegKeyW')
@winfunctype('GDI32.dll')
def ColorCorrectPalette(hdc: win32more.Windows.Win32.Graphics.Gdi.HDC, hPal: win32more.Windows.Win32.Graphics.Gdi.HPALETTE, deFirst: UInt32, num: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def OpenColorProfileA(pProfile: POINTER(win32more.Windows.Win32.UI.ColorSystem.PROFILE), dwDesiredAccess: UInt32, dwShareMode: UInt32, dwCreationMode: UInt32) -> IntPtr: ...
@winfunctype('mscms.dll')
def OpenColorProfileW(pProfile: POINTER(win32more.Windows.Win32.UI.ColorSystem.PROFILE), dwDesiredAccess: UInt32, dwShareMode: UInt32, dwCreationMode: UInt32) -> IntPtr: ...
OpenColorProfile = UnicodeAlias('OpenColorProfileW')
@winfunctype('mscms.dll')
def CloseColorProfile(hProfile: IntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetColorProfileFromHandle(hProfile: IntPtr, pProfile: POINTER(Byte), pcbProfile: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def IsColorProfileValid(hProfile: IntPtr, pbValid: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def CreateProfileFromLogColorSpaceA(pLogColorSpace: POINTER(win32more.Windows.Win32.UI.ColorSystem.LOGCOLORSPACEA), pProfile: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def CreateProfileFromLogColorSpaceW(pLogColorSpace: POINTER(win32more.Windows.Win32.UI.ColorSystem.LOGCOLORSPACEW), pProfile: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.BOOL: ...
CreateProfileFromLogColorSpace = UnicodeAlias('CreateProfileFromLogColorSpaceW')
@winfunctype('mscms.dll')
def GetCountColorProfileElements(hProfile: IntPtr, pnElementCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetColorProfileHeader(hProfile: IntPtr, pHeader: POINTER(win32more.Windows.Win32.UI.ColorSystem.PROFILEHEADER)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetColorProfileElementTag(hProfile: IntPtr, dwIndex: UInt32, pTag: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def IsColorProfileTagPresent(hProfile: IntPtr, tag: UInt32, pbPresent: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetColorProfileElement(hProfile: IntPtr, tag: UInt32, dwOffset: UInt32, pcbElement: POINTER(UInt32), pElement: VoidPtr, pbReference: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def SetColorProfileHeader(hProfile: IntPtr, pHeader: POINTER(win32more.Windows.Win32.UI.ColorSystem.PROFILEHEADER)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def SetColorProfileElementSize(hProfile: IntPtr, tagType: UInt32, pcbElement: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def SetColorProfileElement(hProfile: IntPtr, tag: UInt32, dwOffset: UInt32, pcbElement: POINTER(UInt32), pElement: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def SetColorProfileElementReference(hProfile: IntPtr, newTag: UInt32, refTag: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetPS2ColorSpaceArray(hProfile: IntPtr, dwIntent: UInt32, dwCSAType: UInt32, pPS2ColorSpaceArray: POINTER(Byte), pcbPS2ColorSpaceArray: POINTER(UInt32), pbBinary: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetPS2ColorRenderingIntent(hProfile: IntPtr, dwIntent: UInt32, pBuffer: POINTER(Byte), pcbPS2ColorRenderingIntent: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetPS2ColorRenderingDictionary(hProfile: IntPtr, dwIntent: UInt32, pPS2ColorRenderingDictionary: POINTER(Byte), pcbPS2ColorRenderingDictionary: POINTER(UInt32), pbBinary: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetNamedProfileInfo(hProfile: IntPtr, pNamedProfileInfo: POINTER(win32more.Windows.Win32.UI.ColorSystem.NAMED_PROFILE_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def ConvertColorNameToIndex(hProfile: IntPtr, paColorName: POINTER(POINTER(SByte)), paIndex: POINTER(UInt32), dwCount: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def ConvertIndexToColorName(hProfile: IntPtr, paIndex: POINTER(UInt32), paColorName: POINTER(POINTER(SByte)), dwCount: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def CreateDeviceLinkProfile(hProfile: POINTER(IntPtr), nProfiles: UInt32, padwIntent: POINTER(UInt32), nIntents: UInt32, dwFlags: UInt32, pProfileData: POINTER(POINTER(Byte)), indexPreferredCMM: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def CreateColorTransformA(pLogColorSpace: POINTER(win32more.Windows.Win32.UI.ColorSystem.LOGCOLORSPACEA), hDestProfile: IntPtr, hTargetProfile: IntPtr, dwFlags: UInt32) -> IntPtr: ...
@winfunctype('mscms.dll')
def CreateColorTransformW(pLogColorSpace: POINTER(win32more.Windows.Win32.UI.ColorSystem.LOGCOLORSPACEW), hDestProfile: IntPtr, hTargetProfile: IntPtr, dwFlags: UInt32) -> IntPtr: ...
CreateColorTransform = UnicodeAlias('CreateColorTransformW')
@winfunctype('mscms.dll')
def CreateMultiProfileTransform(pahProfiles: POINTER(IntPtr), nProfiles: UInt32, padwIntent: POINTER(UInt32), nIntents: UInt32, dwFlags: UInt32, indexPreferredCMM: UInt32) -> IntPtr: ...
@winfunctype('mscms.dll')
def DeleteColorTransform(hxform: IntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def TranslateBitmapBits(hColorTransform: IntPtr, pSrcBits: VoidPtr, bmInput: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT, dwWidth: UInt32, dwHeight: UInt32, dwInputStride: UInt32, pDestBits: VoidPtr, bmOutput: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT, dwOutputStride: UInt32, pfnCallBack: win32more.Windows.Win32.UI.ColorSystem.LPBMCALLBACKFN, ulCallbackData: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def CheckBitmapBits(hColorTransform: IntPtr, pSrcBits: VoidPtr, bmInput: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT, dwWidth: UInt32, dwHeight: UInt32, dwStride: UInt32, paResult: POINTER(Byte), pfnCallback: win32more.Windows.Win32.UI.ColorSystem.LPBMCALLBACKFN, lpCallbackData: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def TranslateColors(hColorTransform: IntPtr, paInputColors: POINTER(win32more.Windows.Win32.UI.ColorSystem.COLOR), nColors: UInt32, ctInput: win32more.Windows.Win32.UI.ColorSystem.COLORTYPE, paOutputColors: POINTER(win32more.Windows.Win32.UI.ColorSystem.COLOR), ctOutput: win32more.Windows.Win32.UI.ColorSystem.COLORTYPE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def CheckColors(hColorTransform: IntPtr, paInputColors: POINTER(win32more.Windows.Win32.UI.ColorSystem.COLOR), nColors: UInt32, ctInput: win32more.Windows.Win32.UI.ColorSystem.COLORTYPE, paResult: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetCMMInfo(hColorTransform: IntPtr, param1: UInt32) -> UInt32: ...
@winfunctype('mscms.dll')
def RegisterCMMA(pMachineName: win32more.Windows.Win32.Foundation.PSTR, cmmID: UInt32, pCMMdll: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def RegisterCMMW(pMachineName: win32more.Windows.Win32.Foundation.PWSTR, cmmID: UInt32, pCMMdll: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
RegisterCMM = UnicodeAlias('RegisterCMMW')
@winfunctype('mscms.dll')
def UnregisterCMMA(pMachineName: win32more.Windows.Win32.Foundation.PSTR, cmmID: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def UnregisterCMMW(pMachineName: win32more.Windows.Win32.Foundation.PWSTR, cmmID: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
UnregisterCMM = UnicodeAlias('UnregisterCMMW')
@winfunctype('mscms.dll')
def SelectCMM(dwCMMType: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetColorDirectoryA(pMachineName: win32more.Windows.Win32.Foundation.PSTR, pBuffer: win32more.Windows.Win32.Foundation.PSTR, pdwSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetColorDirectoryW(pMachineName: win32more.Windows.Win32.Foundation.PWSTR, pBuffer: win32more.Windows.Win32.Foundation.PWSTR, pdwSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
GetColorDirectory = UnicodeAlias('GetColorDirectoryW')
@winfunctype('mscms.dll')
def InstallColorProfileA(pMachineName: win32more.Windows.Win32.Foundation.PSTR, pProfileName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def InstallColorProfileW(pMachineName: win32more.Windows.Win32.Foundation.PWSTR, pProfileName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
InstallColorProfile = UnicodeAlias('InstallColorProfileW')
@winfunctype('mscms.dll')
def UninstallColorProfileA(pMachineName: win32more.Windows.Win32.Foundation.PSTR, pProfileName: win32more.Windows.Win32.Foundation.PSTR, bDelete: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def UninstallColorProfileW(pMachineName: win32more.Windows.Win32.Foundation.PWSTR, pProfileName: win32more.Windows.Win32.Foundation.PWSTR, bDelete: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
UninstallColorProfile = UnicodeAlias('UninstallColorProfileW')
@winfunctype('mscms.dll')
def EnumColorProfilesA(pMachineName: win32more.Windows.Win32.Foundation.PSTR, pEnumRecord: POINTER(win32more.Windows.Win32.UI.ColorSystem.ENUMTYPEA), pEnumerationBuffer: POINTER(Byte), pdwSizeOfEnumerationBuffer: POINTER(UInt32), pnProfiles: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def EnumColorProfilesW(pMachineName: win32more.Windows.Win32.Foundation.PWSTR, pEnumRecord: POINTER(win32more.Windows.Win32.UI.ColorSystem.ENUMTYPEW), pEnumerationBuffer: POINTER(Byte), pdwSizeOfEnumerationBuffer: POINTER(UInt32), pnProfiles: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
EnumColorProfiles = UnicodeAlias('EnumColorProfilesW')
@winfunctype('mscms.dll')
def SetStandardColorSpaceProfileA(pMachineName: win32more.Windows.Win32.Foundation.PSTR, dwProfileID: UInt32, pProfilename: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def SetStandardColorSpaceProfileW(pMachineName: win32more.Windows.Win32.Foundation.PWSTR, dwProfileID: UInt32, pProfileName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
SetStandardColorSpaceProfile = UnicodeAlias('SetStandardColorSpaceProfileW')
@winfunctype('mscms.dll')
def GetStandardColorSpaceProfileA(pMachineName: win32more.Windows.Win32.Foundation.PSTR, dwSCS: UInt32, pBuffer: win32more.Windows.Win32.Foundation.PSTR, pcbSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def GetStandardColorSpaceProfileW(pMachineName: win32more.Windows.Win32.Foundation.PWSTR, dwSCS: UInt32, pBuffer: win32more.Windows.Win32.Foundation.PWSTR, pcbSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
GetStandardColorSpaceProfile = UnicodeAlias('GetStandardColorSpaceProfileW')
@winfunctype('mscms.dll')
def AssociateColorProfileWithDeviceA(pMachineName: win32more.Windows.Win32.Foundation.PSTR, pProfileName: win32more.Windows.Win32.Foundation.PSTR, pDeviceName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def AssociateColorProfileWithDeviceW(pMachineName: win32more.Windows.Win32.Foundation.PWSTR, pProfileName: win32more.Windows.Win32.Foundation.PWSTR, pDeviceName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
AssociateColorProfileWithDevice = UnicodeAlias('AssociateColorProfileWithDeviceW')
@winfunctype('mscms.dll')
def DisassociateColorProfileFromDeviceA(pMachineName: win32more.Windows.Win32.Foundation.PSTR, pProfileName: win32more.Windows.Win32.Foundation.PSTR, pDeviceName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def DisassociateColorProfileFromDeviceW(pMachineName: win32more.Windows.Win32.Foundation.PWSTR, pProfileName: win32more.Windows.Win32.Foundation.PWSTR, pDeviceName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
DisassociateColorProfileFromDevice = UnicodeAlias('DisassociateColorProfileFromDeviceW')
@winfunctype('ICMUI.dll')
def SetupColorMatchingW(pcms: POINTER(win32more.Windows.Win32.UI.ColorSystem.COLORMATCHSETUPW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
SetupColorMatching = UnicodeAlias('SetupColorMatchingW')
@winfunctype('ICMUI.dll')
def SetupColorMatchingA(pcms: POINTER(win32more.Windows.Win32.UI.ColorSystem.COLORMATCHSETUPA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsAssociateColorProfileWithDevice(scope: win32more.Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, pProfileName: win32more.Windows.Win32.Foundation.PWSTR, pDeviceName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsDisassociateColorProfileFromDevice(scope: win32more.Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, pProfileName: win32more.Windows.Win32.Foundation.PWSTR, pDeviceName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsEnumColorProfilesSize(scope: win32more.Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, pEnumRecord: POINTER(win32more.Windows.Win32.UI.ColorSystem.ENUMTYPEW), pdwSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsEnumColorProfiles(scope: win32more.Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, pEnumRecord: POINTER(win32more.Windows.Win32.UI.ColorSystem.ENUMTYPEW), pBuffer: POINTER(Byte), dwSize: UInt32, pnProfiles: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsGetDefaultColorProfileSize(scope: win32more.Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, pDeviceName: win32more.Windows.Win32.Foundation.PWSTR, cptColorProfileType: win32more.Windows.Win32.UI.ColorSystem.COLORPROFILETYPE, cpstColorProfileSubType: win32more.Windows.Win32.UI.ColorSystem.COLORPROFILESUBTYPE, dwProfileID: UInt32, pcbProfileName: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsGetDefaultColorProfile(scope: win32more.Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, pDeviceName: win32more.Windows.Win32.Foundation.PWSTR, cptColorProfileType: win32more.Windows.Win32.UI.ColorSystem.COLORPROFILETYPE, cpstColorProfileSubType: win32more.Windows.Win32.UI.ColorSystem.COLORPROFILESUBTYPE, dwProfileID: UInt32, cbProfileName: UInt32, pProfileName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsSetDefaultColorProfile(scope: win32more.Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, pDeviceName: win32more.Windows.Win32.Foundation.PWSTR, cptColorProfileType: win32more.Windows.Win32.UI.ColorSystem.COLORPROFILETYPE, cpstColorProfileSubType: win32more.Windows.Win32.UI.ColorSystem.COLORPROFILESUBTYPE, dwProfileID: UInt32, pProfileName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsSetDefaultRenderingIntent(scope: win32more.Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, dwRenderingIntent: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsGetDefaultRenderingIntent(scope: win32more.Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, pdwRenderingIntent: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsGetUsePerUserProfiles(pDeviceName: win32more.Windows.Win32.Foundation.PWSTR, dwDeviceClass: UInt32, pUsePerUserProfiles: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsSetUsePerUserProfiles(pDeviceName: win32more.Windows.Win32.Foundation.PWSTR, dwDeviceClass: UInt32, usePerUserProfiles: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsTranslateColors(hColorTransform: IntPtr, nColors: UInt32, nInputChannels: UInt32, cdtInput: win32more.Windows.Win32.UI.ColorSystem.COLORDATATYPE, cbInput: UInt32, pInputData: VoidPtr, nOutputChannels: UInt32, cdtOutput: win32more.Windows.Win32.UI.ColorSystem.COLORDATATYPE, cbOutput: UInt32, pOutputData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsCheckColors(hColorTransform: IntPtr, nColors: UInt32, nInputChannels: UInt32, cdtInput: win32more.Windows.Win32.UI.ColorSystem.COLORDATATYPE, cbInput: UInt32, pInputData: VoidPtr, paResult: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMCheckColors(hcmTransform: IntPtr, lpaInputColors: POINTER(win32more.Windows.Win32.UI.ColorSystem.COLOR), nColors: UInt32, ctInput: win32more.Windows.Win32.UI.ColorSystem.COLORTYPE, lpaResult: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMCheckRGBs(hcmTransform: IntPtr, lpSrcBits: VoidPtr, bmInput: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT, dwWidth: UInt32, dwHeight: UInt32, dwStride: UInt32, lpaResult: POINTER(Byte), pfnCallback: win32more.Windows.Win32.UI.ColorSystem.LPBMCALLBACKFN, ulCallbackData: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMConvertColorNameToIndex(hProfile: IntPtr, paColorName: POINTER(POINTER(SByte)), paIndex: POINTER(UInt32), dwCount: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMConvertIndexToColorName(hProfile: IntPtr, paIndex: POINTER(UInt32), paColorName: POINTER(POINTER(SByte)), dwCount: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMCreateDeviceLinkProfile(pahProfiles: POINTER(IntPtr), nProfiles: UInt32, padwIntents: POINTER(UInt32), nIntents: UInt32, dwFlags: UInt32, lpProfileData: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMCreateMultiProfileTransform(pahProfiles: POINTER(IntPtr), nProfiles: UInt32, padwIntents: POINTER(UInt32), nIntents: UInt32, dwFlags: UInt32) -> IntPtr: ...
@winfunctype('ICM32.dll')
def CMCreateProfileW(lpColorSpace: POINTER(win32more.Windows.Win32.UI.ColorSystem.LOGCOLORSPACEW), lpProfileData: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
CMCreateProfile = UnicodeAlias('CMCreateProfileW')
@winfunctype('ICM32.dll')
def CMCreateTransformW(lpColorSpace: POINTER(win32more.Windows.Win32.UI.ColorSystem.LOGCOLORSPACEW), lpDevCharacter: VoidPtr, lpTargetDevCharacter: VoidPtr) -> IntPtr: ...
CMCreateTransform = UnicodeAlias('CMCreateTransformW')
@winfunctype('ICM32.dll')
def CMCheckColorsInGamut(hcmTransform: IntPtr, lpaRGBTriple: POINTER(win32more.Windows.Win32.Graphics.Gdi.RGBTRIPLE), lpaResult: POINTER(Byte), nCount: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMTranslateRGB(hcmTransform: IntPtr, ColorRef: win32more.Windows.Win32.Foundation.COLORREF, lpColorRef: POINTER(UInt32), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMTranslateRGBs(hcmTransform: IntPtr, lpSrcBits: VoidPtr, bmInput: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT, dwWidth: UInt32, dwHeight: UInt32, dwStride: UInt32, lpDestBits: VoidPtr, bmOutput: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT, dwTranslateDirection: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMCreateTransformExtW(lpColorSpace: POINTER(win32more.Windows.Win32.UI.ColorSystem.LOGCOLORSPACEW), lpDevCharacter: VoidPtr, lpTargetDevCharacter: VoidPtr, dwFlags: UInt32) -> IntPtr: ...
CMCreateTransformExt = UnicodeAlias('CMCreateTransformExtW')
@winfunctype('ICM32.dll')
def CMDeleteTransform(hcmTransform: IntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMGetInfo(dwInfo: UInt32) -> UInt32: ...
@winfunctype('ICM32.dll')
def CMGetNamedProfileInfo(hProfile: IntPtr, pNamedProfileInfo: POINTER(win32more.Windows.Win32.UI.ColorSystem.NAMED_PROFILE_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMIsProfileValid(hProfile: IntPtr, lpbValid: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMTranslateColors(hcmTransform: IntPtr, lpaInputColors: POINTER(win32more.Windows.Win32.UI.ColorSystem.COLOR), nColors: UInt32, ctInput: win32more.Windows.Win32.UI.ColorSystem.COLORTYPE, lpaOutputColors: POINTER(win32more.Windows.Win32.UI.ColorSystem.COLOR), ctOutput: win32more.Windows.Win32.UI.ColorSystem.COLORTYPE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ICM32.dll')
def CMTranslateRGBsExt(hcmTransform: IntPtr, lpSrcBits: VoidPtr, bmInput: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT, dwWidth: UInt32, dwHeight: UInt32, dwInputStride: UInt32, lpDestBits: VoidPtr, bmOutput: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT, dwOutputStride: UInt32, lpfnCallback: win32more.Windows.Win32.UI.ColorSystem.LPBMCALLBACKFN, ulCallbackData: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsOpenColorProfileA(pCDMPProfile: POINTER(win32more.Windows.Win32.UI.ColorSystem.PROFILE), pCAMPProfile: POINTER(win32more.Windows.Win32.UI.ColorSystem.PROFILE), pGMMPProfile: POINTER(win32more.Windows.Win32.UI.ColorSystem.PROFILE), dwDesireAccess: UInt32, dwShareMode: UInt32, dwCreationMode: UInt32, dwFlags: UInt32) -> IntPtr: ...
@winfunctype('mscms.dll')
def WcsOpenColorProfileW(pCDMPProfile: POINTER(win32more.Windows.Win32.UI.ColorSystem.PROFILE), pCAMPProfile: POINTER(win32more.Windows.Win32.UI.ColorSystem.PROFILE), pGMMPProfile: POINTER(win32more.Windows.Win32.UI.ColorSystem.PROFILE), dwDesireAccess: UInt32, dwShareMode: UInt32, dwCreationMode: UInt32, dwFlags: UInt32) -> IntPtr: ...
WcsOpenColorProfile = UnicodeAlias('WcsOpenColorProfileW')
@winfunctype('mscms.dll')
def WcsCreateIccProfile(hWcsProfile: IntPtr, dwOptions: UInt32) -> IntPtr: ...
@winfunctype('mscms.dll')
def WcsGetCalibrationManagementState(pbIsEnabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def WcsSetCalibrationManagementState(bIsEnabled: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('mscms.dll')
def ColorProfileAddDisplayAssociation(scope: win32more.Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, profileName: win32more.Windows.Win32.Foundation.PWSTR, targetAdapterID: win32more.Windows.Win32.Foundation.LUID, sourceID: UInt32, setAsDefault: win32more.Windows.Win32.Foundation.BOOL, associateAsAdvancedColor: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('mscms.dll')
def ColorProfileRemoveDisplayAssociation(scope: win32more.Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, profileName: win32more.Windows.Win32.Foundation.PWSTR, targetAdapterID: win32more.Windows.Win32.Foundation.LUID, sourceID: UInt32, dissociateAdvancedColor: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('mscms.dll')
def ColorProfileSetDisplayDefaultAssociation(scope: win32more.Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, profileName: win32more.Windows.Win32.Foundation.PWSTR, profileType: win32more.Windows.Win32.UI.ColorSystem.COLORPROFILETYPE, profileSubType: win32more.Windows.Win32.UI.ColorSystem.COLORPROFILESUBTYPE, targetAdapterID: win32more.Windows.Win32.Foundation.LUID, sourceID: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('mscms.dll')
def ColorProfileGetDisplayList(scope: win32more.Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, targetAdapterID: win32more.Windows.Win32.Foundation.LUID, sourceID: UInt32, profileList: POINTER(POINTER(win32more.Windows.Win32.Foundation.PWSTR)), profileCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('mscms.dll')
def ColorProfileGetDisplayDefault(scope: win32more.Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE, targetAdapterID: win32more.Windows.Win32.Foundation.LUID, sourceID: UInt32, profileType: win32more.Windows.Win32.UI.ColorSystem.COLORPROFILETYPE, profileSubType: win32more.Windows.Win32.UI.ColorSystem.COLORPROFILESUBTYPE, profileName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('mscms.dll')
def ColorProfileGetDisplayUserScope(targetAdapterID: win32more.Windows.Win32.Foundation.LUID, sourceID: UInt32, scope: POINTER(win32more.Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
BMFORMAT = Int32
BM_x555RGB: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 0
BM_x555XYZ: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 257
BM_x555Yxy: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 258
BM_x555Lab: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 259
BM_x555G3CH: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 260
BM_RGBTRIPLETS: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 2
BM_BGRTRIPLETS: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 4
BM_XYZTRIPLETS: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 513
BM_YxyTRIPLETS: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 514
BM_LabTRIPLETS: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 515
BM_G3CHTRIPLETS: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 516
BM_5CHANNEL: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 517
BM_6CHANNEL: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 518
BM_7CHANNEL: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 519
BM_8CHANNEL: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 520
BM_GRAY: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 521
BM_xRGBQUADS: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 8
BM_xBGRQUADS: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 16
BM_xG3CHQUADS: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 772
BM_KYMCQUADS: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 773
BM_CMYKQUADS: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 32
BM_10b_RGB: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 9
BM_10b_XYZ: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 1025
BM_10b_Yxy: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 1026
BM_10b_Lab: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 1027
BM_10b_G3CH: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 1028
BM_NAMED_INDEX: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 1029
BM_16b_RGB: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 10
BM_16b_XYZ: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 1281
BM_16b_Yxy: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 1282
BM_16b_Lab: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 1283
BM_16b_G3CH: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 1284
BM_16b_GRAY: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 1285
BM_565RGB: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 1
BM_32b_scRGB: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 1537
BM_32b_scARGB: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 1538
BM_S2DOT13FIXED_scRGB: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 1539
BM_S2DOT13FIXED_scARGB: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 1540
BM_R10G10B10A2: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 1793
BM_R10G10B10A2_XR: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 1794
BM_R16G16B16A16_FLOAT: win32more.Windows.Win32.UI.ColorSystem.BMFORMAT = 1795
class BlackInformation(Structure):
    fBlackOnly: win32more.Windows.Win32.Foundation.BOOL
    blackWeight: Single
class CMYKCOLOR(Structure):
    cyan: UInt16
    magenta: UInt16
    yellow: UInt16
    black: UInt16
class COLOR(Union):
    gray: win32more.Windows.Win32.UI.ColorSystem.GRAYCOLOR
    rgb: win32more.Windows.Win32.UI.ColorSystem.RGBCOLOR
    cmyk: win32more.Windows.Win32.UI.ColorSystem.CMYKCOLOR
    XYZ: win32more.Windows.Win32.UI.ColorSystem.XYZCOLOR
    Yxy: win32more.Windows.Win32.UI.ColorSystem.YxyCOLOR
    Lab: win32more.Windows.Win32.UI.ColorSystem.LabCOLOR
    gen3ch: win32more.Windows.Win32.UI.ColorSystem.GENERIC3CHANNEL
    named: win32more.Windows.Win32.UI.ColorSystem.NAMEDCOLOR
    hifi: win32more.Windows.Win32.UI.ColorSystem.HiFiCOLOR
    Anonymous: _Anonymous_e__Struct
    class _Anonymous_e__Struct(Structure):
        reserved1: UInt32
        reserved2: VoidPtr
COLORDATATYPE = Int32
COLOR_BYTE: win32more.Windows.Win32.UI.ColorSystem.COLORDATATYPE = 1
COLOR_WORD: win32more.Windows.Win32.UI.ColorSystem.COLORDATATYPE = 2
COLOR_FLOAT: win32more.Windows.Win32.UI.ColorSystem.COLORDATATYPE = 3
COLOR_S2DOT13FIXED: win32more.Windows.Win32.UI.ColorSystem.COLORDATATYPE = 4
COLOR_10b_R10G10B10A2: win32more.Windows.Win32.UI.ColorSystem.COLORDATATYPE = 5
COLOR_10b_R10G10B10A2_XR: win32more.Windows.Win32.UI.ColorSystem.COLORDATATYPE = 6
COLOR_FLOAT16: win32more.Windows.Win32.UI.ColorSystem.COLORDATATYPE = 7
class COLORMATCHSETUPA(Structure):
    dwSize: UInt32
    dwVersion: UInt32
    dwFlags: UInt32
    hwndOwner: win32more.Windows.Win32.Foundation.HWND
    pSourceName: win32more.Windows.Win32.Foundation.PSTR
    pDisplayName: win32more.Windows.Win32.Foundation.PSTR
    pPrinterName: win32more.Windows.Win32.Foundation.PSTR
    dwRenderIntent: UInt32
    dwProofingIntent: UInt32
    pMonitorProfile: win32more.Windows.Win32.Foundation.PSTR
    ccMonitorProfile: UInt32
    pPrinterProfile: win32more.Windows.Win32.Foundation.PSTR
    ccPrinterProfile: UInt32
    pTargetProfile: win32more.Windows.Win32.Foundation.PSTR
    ccTargetProfile: UInt32
    lpfnHook: win32more.Windows.Win32.UI.WindowsAndMessaging.DLGPROC
    lParam: win32more.Windows.Win32.Foundation.LPARAM
    lpfnApplyCallback: win32more.Windows.Win32.UI.ColorSystem.PCMSCALLBACKA
    lParamApplyCallback: win32more.Windows.Win32.Foundation.LPARAM
class COLORMATCHSETUPW(Structure):
    dwSize: UInt32
    dwVersion: UInt32
    dwFlags: UInt32
    hwndOwner: win32more.Windows.Win32.Foundation.HWND
    pSourceName: win32more.Windows.Win32.Foundation.PWSTR
    pDisplayName: win32more.Windows.Win32.Foundation.PWSTR
    pPrinterName: win32more.Windows.Win32.Foundation.PWSTR
    dwRenderIntent: UInt32
    dwProofingIntent: UInt32
    pMonitorProfile: win32more.Windows.Win32.Foundation.PWSTR
    ccMonitorProfile: UInt32
    pPrinterProfile: win32more.Windows.Win32.Foundation.PWSTR
    ccPrinterProfile: UInt32
    pTargetProfile: win32more.Windows.Win32.Foundation.PWSTR
    ccTargetProfile: UInt32
    lpfnHook: win32more.Windows.Win32.UI.WindowsAndMessaging.DLGPROC
    lParam: win32more.Windows.Win32.Foundation.LPARAM
    lpfnApplyCallback: win32more.Windows.Win32.UI.ColorSystem.PCMSCALLBACKW
    lParamApplyCallback: win32more.Windows.Win32.Foundation.LPARAM
COLORMATCHSETUP = UnicodeAlias('COLORMATCHSETUPW')
COLORPROFILESUBTYPE = Int32
CPST_PERCEPTUAL: win32more.Windows.Win32.UI.ColorSystem.COLORPROFILESUBTYPE = 0
CPST_RELATIVE_COLORIMETRIC: win32more.Windows.Win32.UI.ColorSystem.COLORPROFILESUBTYPE = 1
CPST_SATURATION: win32more.Windows.Win32.UI.ColorSystem.COLORPROFILESUBTYPE = 2
CPST_ABSOLUTE_COLORIMETRIC: win32more.Windows.Win32.UI.ColorSystem.COLORPROFILESUBTYPE = 3
CPST_NONE: win32more.Windows.Win32.UI.ColorSystem.COLORPROFILESUBTYPE = 4
CPST_RGB_WORKING_SPACE: win32more.Windows.Win32.UI.ColorSystem.COLORPROFILESUBTYPE = 5
CPST_CUSTOM_WORKING_SPACE: win32more.Windows.Win32.UI.ColorSystem.COLORPROFILESUBTYPE = 6
CPST_STANDARD_DISPLAY_COLOR_MODE: win32more.Windows.Win32.UI.ColorSystem.COLORPROFILESUBTYPE = 7
CPST_EXTENDED_DISPLAY_COLOR_MODE: win32more.Windows.Win32.UI.ColorSystem.COLORPROFILESUBTYPE = 8
COLORPROFILETYPE = Int32
CPT_ICC: win32more.Windows.Win32.UI.ColorSystem.COLORPROFILETYPE = 0
CPT_DMP: win32more.Windows.Win32.UI.ColorSystem.COLORPROFILETYPE = 1
CPT_CAMP: win32more.Windows.Win32.UI.ColorSystem.COLORPROFILETYPE = 2
CPT_GMMP: win32more.Windows.Win32.UI.ColorSystem.COLORPROFILETYPE = 3
COLORTYPE = Int32
COLOR_GRAY: win32more.Windows.Win32.UI.ColorSystem.COLORTYPE = 1
COLOR_RGB: win32more.Windows.Win32.UI.ColorSystem.COLORTYPE = 2
COLOR_XYZ: win32more.Windows.Win32.UI.ColorSystem.COLORTYPE = 3
COLOR_Yxy: win32more.Windows.Win32.UI.ColorSystem.COLORTYPE = 4
COLOR_Lab: win32more.Windows.Win32.UI.ColorSystem.COLORTYPE = 5
COLOR_3_CHANNEL: win32more.Windows.Win32.UI.ColorSystem.COLORTYPE = 6
COLOR_CMYK: win32more.Windows.Win32.UI.ColorSystem.COLORTYPE = 7
COLOR_5_CHANNEL: win32more.Windows.Win32.UI.ColorSystem.COLORTYPE = 8
COLOR_6_CHANNEL: win32more.Windows.Win32.UI.ColorSystem.COLORTYPE = 9
COLOR_7_CHANNEL: win32more.Windows.Win32.UI.ColorSystem.COLORTYPE = 10
COLOR_8_CHANNEL: win32more.Windows.Win32.UI.ColorSystem.COLORTYPE = 11
COLOR_NAMED: win32more.Windows.Win32.UI.ColorSystem.COLORTYPE = 12
COLOR_MATCH_TO_TARGET_ACTION = UInt32
CS_ENABLE: win32more.Windows.Win32.UI.ColorSystem.COLOR_MATCH_TO_TARGET_ACTION = 1
CS_DISABLE: win32more.Windows.Win32.UI.ColorSystem.COLOR_MATCH_TO_TARGET_ACTION = 2
CS_DELETE_TRANSFORM: win32more.Windows.Win32.UI.ColorSystem.COLOR_MATCH_TO_TARGET_ACTION = 3
class EMRCREATECOLORSPACEW(Structure):
    emr: win32more.Windows.Win32.Graphics.Gdi.EMR
    ihCS: UInt32
    lcs: win32more.Windows.Win32.UI.ColorSystem.LOGCOLORSPACEW
    dwFlags: UInt32
    cbData: UInt32
    Data: Byte * 1
EMRCREATECOLORSPACE = UnicodeAlias('EMRCREATECOLORSPACEW')
class ENUMTYPEA(Structure):
    dwSize: UInt32
    dwVersion: UInt32
    dwFields: UInt32
    pDeviceName: win32more.Windows.Win32.Foundation.PSTR
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
    pDeviceName: win32more.Windows.Win32.Foundation.PWSTR
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
ENUMTYPE = UnicodeAlias('ENUMTYPEW')
class GENERIC3CHANNEL(Structure):
    ch1: UInt16
    ch2: UInt16
    ch3: UInt16
class GRAYCOLOR(Structure):
    gray: UInt16
class GamutBoundaryDescription(Structure):
    pPrimaries: POINTER(win32more.Windows.Win32.UI.ColorSystem.PrimaryJabColors)
    cNeutralSamples: UInt32
    pNeutralSamples: POINTER(win32more.Windows.Win32.UI.ColorSystem.JabColorF)
    pReferenceShell: POINTER(win32more.Windows.Win32.UI.ColorSystem.GamutShell)
    pPlausibleShell: POINTER(win32more.Windows.Win32.UI.ColorSystem.GamutShell)
    pPossibleShell: POINTER(win32more.Windows.Win32.UI.ColorSystem.GamutShell)
class GamutShell(Structure):
    JMin: Single
    JMax: Single
    cVertices: UInt32
    cTriangles: UInt32
    pVertices: POINTER(win32more.Windows.Win32.UI.ColorSystem.JabColorF)
    pTriangles: POINTER(win32more.Windows.Win32.UI.ColorSystem.GamutShellTriangle)
class GamutShellTriangle(Structure):
    aVertexIndex: UInt32 * 3
HCOLORSPACE = VoidPtr
class HiFiCOLOR(Structure):
    channel: Byte * 8
@winfunctype_pointer
def ICMENUMPROCA(param0: win32more.Windows.Win32.Foundation.PSTR, param1: win32more.Windows.Win32.Foundation.LPARAM) -> Int32: ...
@winfunctype_pointer
def ICMENUMPROCW(param0: win32more.Windows.Win32.Foundation.PWSTR, param1: win32more.Windows.Win32.Foundation.LPARAM) -> Int32: ...
ICMENUMPROC = UnicodeAlias('ICMENUMPROCW')
ICM_COMMAND = UInt32
ICM_ADDPROFILE: win32more.Windows.Win32.UI.ColorSystem.ICM_COMMAND = 1
ICM_DELETEPROFILE: win32more.Windows.Win32.UI.ColorSystem.ICM_COMMAND = 2
ICM_QUERYPROFILE: win32more.Windows.Win32.UI.ColorSystem.ICM_COMMAND = 3
ICM_SETDEFAULTPROFILE: win32more.Windows.Win32.UI.ColorSystem.ICM_COMMAND = 4
ICM_REGISTERICMATCHER: win32more.Windows.Win32.UI.ColorSystem.ICM_COMMAND = 5
ICM_UNREGISTERICMATCHER: win32more.Windows.Win32.UI.ColorSystem.ICM_COMMAND = 6
ICM_QUERYMATCH: win32more.Windows.Win32.UI.ColorSystem.ICM_COMMAND = 7
ICM_MODE = Int32
ICM_OFF: win32more.Windows.Win32.UI.ColorSystem.ICM_MODE = 1
ICM_ON: win32more.Windows.Win32.UI.ColorSystem.ICM_MODE = 2
ICM_QUERY: win32more.Windows.Win32.UI.ColorSystem.ICM_MODE = 3
ICM_DONE_OUTSIDEDC: win32more.Windows.Win32.UI.ColorSystem.ICM_MODE = 4
class IDeviceModelPlugIn(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1cd63475-07c4-46fe-a903-d655316d11fd}')
    @commethod(3)
    def Initialize(self, bstrXml: win32more.Windows.Win32.Foundation.BSTR, cNumModels: UInt32, iModelPosition: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNumChannels(self, pNumChannels: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DeviceToColorimetricColors(self, cColors: UInt32, cChannels: UInt32, pDeviceValues: POINTER(Single), pXYZColors: POINTER(win32more.Windows.Win32.UI.ColorSystem.XYZColorF)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ColorimetricToDeviceColors(self, cColors: UInt32, cChannels: UInt32, pXYZColors: POINTER(win32more.Windows.Win32.UI.ColorSystem.XYZColorF), pDeviceValues: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ColorimetricToDeviceColorsWithBlack(self, cColors: UInt32, cChannels: UInt32, pXYZColors: POINTER(win32more.Windows.Win32.UI.ColorSystem.XYZColorF), pBlackInformation: POINTER(win32more.Windows.Win32.UI.ColorSystem.BlackInformation), pDeviceValues: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetTransformDeviceModelInfo(self, iModelPosition: UInt32, pIDeviceModelOther: win32more.Windows.Win32.UI.ColorSystem.IDeviceModelPlugIn) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetPrimarySamples(self, pPrimaryColor: POINTER(win32more.Windows.Win32.UI.ColorSystem.PrimaryXYZColors)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetGamutBoundaryMeshSize(self, pNumVertices: POINTER(UInt32), pNumTriangles: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetGamutBoundaryMesh(self, cChannels: UInt32, cVertices: UInt32, cTriangles: UInt32, pVertices: POINTER(Single), pTriangles: POINTER(win32more.Windows.Win32.UI.ColorSystem.GamutShellTriangle)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetNeutralAxisSize(self, pcColors: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetNeutralAxis(self, cColors: UInt32, pXYZColors: POINTER(win32more.Windows.Win32.UI.ColorSystem.XYZColorF)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IGamutMapModelPlugIn(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2dd80115-ad1e-41f6-a219-a4f4b583d1f9}')
    @commethod(3)
    def Initialize(self, bstrXml: win32more.Windows.Win32.Foundation.BSTR, pSrcPlugIn: win32more.Windows.Win32.UI.ColorSystem.IDeviceModelPlugIn, pDestPlugIn: win32more.Windows.Win32.UI.ColorSystem.IDeviceModelPlugIn, pSrcGBD: POINTER(win32more.Windows.Win32.UI.ColorSystem.GamutBoundaryDescription), pDestGBD: POINTER(win32more.Windows.Win32.UI.ColorSystem.GamutBoundaryDescription)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SourceToDestinationAppearanceColors(self, cColors: UInt32, pInputColors: POINTER(win32more.Windows.Win32.UI.ColorSystem.JChColorF), pOutputColors: POINTER(win32more.Windows.Win32.UI.ColorSystem.JChColorF)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class JChColorF(Structure):
    J: Single
    C: Single
    h: Single
class JabColorF(Structure):
    J: Single
    a: Single
    b: Single
LCSCSTYPE = Int32
LCS_CALIBRATED_RGB: win32more.Windows.Win32.UI.ColorSystem.LCSCSTYPE = 0
LCS_sRGB: win32more.Windows.Win32.UI.ColorSystem.LCSCSTYPE = 1934772034
LCS_WINDOWS_COLOR_SPACE: win32more.Windows.Win32.UI.ColorSystem.LCSCSTYPE = 1466527264
class LOGCOLORSPACEA(Structure):
    lcsSignature: UInt32
    lcsVersion: UInt32
    lcsSize: UInt32
    lcsCSType: win32more.Windows.Win32.UI.ColorSystem.LCSCSTYPE
    lcsIntent: Int32
    lcsEndpoints: win32more.Windows.Win32.Graphics.Gdi.CIEXYZTRIPLE
    lcsGammaRed: UInt32
    lcsGammaGreen: UInt32
    lcsGammaBlue: UInt32
    lcsFilename: win32more.Windows.Win32.Foundation.CHAR * 260
class LOGCOLORSPACEW(Structure):
    lcsSignature: UInt32
    lcsVersion: UInt32
    lcsSize: UInt32
    lcsCSType: win32more.Windows.Win32.UI.ColorSystem.LCSCSTYPE
    lcsIntent: Int32
    lcsEndpoints: win32more.Windows.Win32.Graphics.Gdi.CIEXYZTRIPLE
    lcsGammaRed: UInt32
    lcsGammaGreen: UInt32
    lcsGammaBlue: UInt32
    lcsFilename: Char * 260
LOGCOLORSPACE = UnicodeAlias('LOGCOLORSPACEW')
@winfunctype_pointer
def LPBMCALLBACKFN(param0: UInt32, param1: UInt32, param2: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.BOOL: ...
class LabCOLOR(Structure):
    L: UInt16
    a: UInt16
    b: UInt16
class NAMEDCOLOR(Structure):
    dwIndex: UInt32
class NAMED_PROFILE_INFO(Structure):
    dwFlags: UInt32
    dwCount: UInt32
    dwCountDevCoordinates: UInt32
    szPrefix: SByte * 32
    szSuffix: SByte * 32
@winfunctype_pointer
def PCMSCALLBACKA(param0: POINTER(win32more.Windows.Win32.UI.ColorSystem.COLORMATCHSETUPA), param1: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PCMSCALLBACKW(param0: POINTER(win32more.Windows.Win32.UI.ColorSystem.COLORMATCHSETUPW), param1: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.BOOL: ...
PCMSCALLBACK = UnicodeAlias('PCMSCALLBACKW')
class PROFILE(Structure):
    dwType: UInt32
    pProfileData: VoidPtr
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
    phIlluminant: win32more.Windows.Win32.Graphics.Gdi.CIEXYZ
    phCreator: UInt32
    phReserved: Byte * 44
class PrimaryJabColors(Structure):
    red: win32more.Windows.Win32.UI.ColorSystem.JabColorF
    yellow: win32more.Windows.Win32.UI.ColorSystem.JabColorF
    green: win32more.Windows.Win32.UI.ColorSystem.JabColorF
    cyan: win32more.Windows.Win32.UI.ColorSystem.JabColorF
    blue: win32more.Windows.Win32.UI.ColorSystem.JabColorF
    magenta: win32more.Windows.Win32.UI.ColorSystem.JabColorF
    black: win32more.Windows.Win32.UI.ColorSystem.JabColorF
    white: win32more.Windows.Win32.UI.ColorSystem.JabColorF
class PrimaryXYZColors(Structure):
    red: win32more.Windows.Win32.UI.ColorSystem.XYZColorF
    yellow: win32more.Windows.Win32.UI.ColorSystem.XYZColorF
    green: win32more.Windows.Win32.UI.ColorSystem.XYZColorF
    cyan: win32more.Windows.Win32.UI.ColorSystem.XYZColorF
    blue: win32more.Windows.Win32.UI.ColorSystem.XYZColorF
    magenta: win32more.Windows.Win32.UI.ColorSystem.XYZColorF
    black: win32more.Windows.Win32.UI.ColorSystem.XYZColorF
    white: win32more.Windows.Win32.UI.ColorSystem.XYZColorF
class RGBCOLOR(Structure):
    red: UInt16
    green: UInt16
    blue: UInt16
WCS_DEVICE_CAPABILITIES_TYPE = Int32
VideoCardGammaTable: win32more.Windows.Win32.UI.ColorSystem.WCS_DEVICE_CAPABILITIES_TYPE = 1
MicrosoftHardwareColorV2: win32more.Windows.Win32.UI.ColorSystem.WCS_DEVICE_CAPABILITIES_TYPE = 2
class WCS_DEVICE_MHC2_CAPABILITIES(Structure):
    Size: UInt32
    SupportsMhc2: win32more.Windows.Win32.Foundation.BOOL
    RegammaLutEntryCount: UInt32
    CscXyzMatrixRows: UInt32
    CscXyzMatrixColumns: UInt32
class WCS_DEVICE_VCGT_CAPABILITIES(Structure):
    Size: UInt32
    SupportsVcgt: win32more.Windows.Win32.Foundation.BOOL
WCS_PROFILE_MANAGEMENT_SCOPE = Int32
WCS_PROFILE_MANAGEMENT_SCOPE_SYSTEM_WIDE: win32more.Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE = 0
WCS_PROFILE_MANAGEMENT_SCOPE_CURRENT_USER: win32more.Windows.Win32.UI.ColorSystem.WCS_PROFILE_MANAGEMENT_SCOPE = 1
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


make_ready(__name__)
