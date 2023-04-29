from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Gdi
import Windows.Win32.System.Com
import Windows.Win32.UI.Controls
import Windows.Win32.UI.Controls.Dialogs
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
OFN_SHAREFALLTHROUGH: UInt32 = 2
OFN_SHARENOWARN: UInt32 = 1
OFN_SHAREWARN: UInt32 = 0
CDN_INITDONE: UInt32 = 4294966695
CDN_SELCHANGE: UInt32 = 4294966694
CDN_FOLDERCHANGE: UInt32 = 4294966693
CDN_SHAREVIOLATION: UInt32 = 4294966692
CDN_HELP: UInt32 = 4294966691
CDN_FILEOK: UInt32 = 4294966690
CDN_TYPECHANGE: UInt32 = 4294966689
CDN_INCLUDEITEM: UInt32 = 4294966688
CDM_FIRST: UInt32 = 1124
CDM_LAST: UInt32 = 1224
CDM_GETSPEC: UInt32 = 1124
CDM_GETFILEPATH: UInt32 = 1125
CDM_GETFOLDERPATH: UInt32 = 1126
CDM_GETFOLDERIDLIST: UInt32 = 1127
CDM_SETCONTROLTEXT: UInt32 = 1128
CDM_HIDECONTROL: UInt32 = 1129
CDM_SETDEFEXT: UInt32 = 1130
FR_RAW: UInt32 = 131072
FR_SHOWWRAPAROUND: UInt32 = 262144
FR_NOWRAPAROUND: UInt32 = 524288
FR_WRAPAROUND: UInt32 = 1048576
FRM_FIRST: UInt32 = 1124
FRM_LAST: UInt32 = 1224
FRM_SETOPERATIONRESULT: UInt32 = 1124
FRM_SETOPERATIONRESULTTEXT: UInt32 = 1125
PS_OPENTYPE_FONTTYPE: UInt32 = 65536
TT_OPENTYPE_FONTTYPE: UInt32 = 131072
TYPE1_FONTTYPE: UInt32 = 262144
SYMBOL_FONTTYPE: UInt32 = 524288
WM_CHOOSEFONT_GETLOGFONT: UInt32 = 1025
WM_CHOOSEFONT_SETLOGFONT: UInt32 = 1125
WM_CHOOSEFONT_SETFLAGS: UInt32 = 1126
LBSELCHSTRINGA: String = 'commdlg_LBSelChangedNotify'
SHAREVISTRINGA: String = 'commdlg_ShareViolation'
FILEOKSTRINGA: String = 'commdlg_FileNameOK'
COLOROKSTRINGA: String = 'commdlg_ColorOK'
SETRGBSTRINGA: String = 'commdlg_SetRGBColor'
HELPMSGSTRINGA: String = 'commdlg_help'
FINDMSGSTRINGA: String = 'commdlg_FindReplace'
LBSELCHSTRINGW: String = 'commdlg_LBSelChangedNotify'
SHAREVISTRINGW: String = 'commdlg_ShareViolation'
FILEOKSTRINGW: String = 'commdlg_FileNameOK'
COLOROKSTRINGW: String = 'commdlg_ColorOK'
SETRGBSTRINGW: String = 'commdlg_SetRGBColor'
HELPMSGSTRINGW: String = 'commdlg_help'
FINDMSGSTRINGW: String = 'commdlg_FindReplace'
LBSELCHSTRING: String = 'commdlg_LBSelChangedNotify'
SHAREVISTRING: String = 'commdlg_ShareViolation'
FILEOKSTRING: String = 'commdlg_FileNameOK'
COLOROKSTRING: String = 'commdlg_ColorOK'
SETRGBSTRING: String = 'commdlg_SetRGBColor'
HELPMSGSTRING: String = 'commdlg_help'
FINDMSGSTRING: String = 'commdlg_FindReplace'
CD_LBSELNOITEMS: Int32 = -1
CD_LBSELCHANGE: UInt32 = 0
CD_LBSELSUB: UInt32 = 1
CD_LBSELADD: UInt32 = 2
START_PAGE_GENERAL: UInt32 = 4294967295
PD_RESULT_CANCEL: UInt32 = 0
PD_RESULT_PRINT: UInt32 = 1
PD_RESULT_APPLY: UInt32 = 2
DN_DEFAULTPRN: UInt32 = 1
WM_PSD_FULLPAGERECT: UInt32 = 1025
WM_PSD_MINMARGINRECT: UInt32 = 1026
WM_PSD_MARGINRECT: UInt32 = 1027
WM_PSD_GREEKTEXTRECT: UInt32 = 1028
WM_PSD_ENVSTAMPRECT: UInt32 = 1029
WM_PSD_YAFULLPAGERECT: UInt32 = 1030
DLG_COLOR: UInt32 = 10
COLOR_HUESCROLL: UInt32 = 700
COLOR_SATSCROLL: UInt32 = 701
COLOR_LUMSCROLL: UInt32 = 702
COLOR_HUE: UInt32 = 703
COLOR_SAT: UInt32 = 704
COLOR_LUM: UInt32 = 705
COLOR_RED: UInt32 = 706
COLOR_GREEN: UInt32 = 707
COLOR_BLUE: UInt32 = 708
COLOR_CURRENT: UInt32 = 709
COLOR_RAINBOW: UInt32 = 710
COLOR_SAVE: UInt32 = 711
COLOR_ADD: UInt32 = 712
COLOR_SOLID: UInt32 = 713
COLOR_TUNE: UInt32 = 714
COLOR_SCHEMES: UInt32 = 715
COLOR_ELEMENT: UInt32 = 716
COLOR_SAMPLES: UInt32 = 717
COLOR_PALETTE: UInt32 = 718
COLOR_MIX: UInt32 = 719
COLOR_BOX1: UInt32 = 720
COLOR_CUSTOM1: UInt32 = 721
COLOR_HUEACCEL: UInt32 = 723
COLOR_SATACCEL: UInt32 = 724
COLOR_LUMACCEL: UInt32 = 725
COLOR_REDACCEL: UInt32 = 726
COLOR_GREENACCEL: UInt32 = 727
COLOR_BLUEACCEL: UInt32 = 728
COLOR_SOLID_LEFT: UInt32 = 730
COLOR_SOLID_RIGHT: UInt32 = 731
NUM_BASIC_COLORS: UInt32 = 48
NUM_CUSTOM_COLORS: UInt32 = 16
@winfunctype('COMDLG32.dll')
def GetOpenFileNameA(param0: POINTER(Windows.Win32.UI.Controls.Dialogs.OPENFILENAMEA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('COMDLG32.dll')
def GetOpenFileNameW(param0: POINTER(Windows.Win32.UI.Controls.Dialogs.OPENFILENAMEW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('COMDLG32.dll')
def GetSaveFileNameA(param0: POINTER(Windows.Win32.UI.Controls.Dialogs.OPENFILENAMEA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('COMDLG32.dll')
def GetSaveFileNameW(param0: POINTER(Windows.Win32.UI.Controls.Dialogs.OPENFILENAMEW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('COMDLG32.dll')
def GetFileTitleA(param0: Windows.Win32.Foundation.PSTR, Buf: Windows.Win32.Foundation.PSTR, cchSize: UInt16) -> Int16: ...
@winfunctype('COMDLG32.dll')
def GetFileTitleW(param0: Windows.Win32.Foundation.PWSTR, Buf: Windows.Win32.Foundation.PWSTR, cchSize: UInt16) -> Int16: ...
@winfunctype('COMDLG32.dll')
def ChooseColorA(param0: POINTER(Windows.Win32.UI.Controls.Dialogs.CHOOSECOLORA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('COMDLG32.dll')
def ChooseColorW(param0: POINTER(Windows.Win32.UI.Controls.Dialogs.CHOOSECOLORW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('COMDLG32.dll')
def FindTextA(param0: POINTER(Windows.Win32.UI.Controls.Dialogs.FINDREPLACEA_head)) -> Windows.Win32.Foundation.HWND: ...
@winfunctype('COMDLG32.dll')
def FindTextW(param0: POINTER(Windows.Win32.UI.Controls.Dialogs.FINDREPLACEW_head)) -> Windows.Win32.Foundation.HWND: ...
@winfunctype('COMDLG32.dll')
def ReplaceTextA(param0: POINTER(Windows.Win32.UI.Controls.Dialogs.FINDREPLACEA_head)) -> Windows.Win32.Foundation.HWND: ...
@winfunctype('COMDLG32.dll')
def ReplaceTextW(param0: POINTER(Windows.Win32.UI.Controls.Dialogs.FINDREPLACEW_head)) -> Windows.Win32.Foundation.HWND: ...
@winfunctype('COMDLG32.dll')
def ChooseFontA(param0: POINTER(Windows.Win32.UI.Controls.Dialogs.CHOOSEFONTA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('COMDLG32.dll')
def ChooseFontW(param0: POINTER(Windows.Win32.UI.Controls.Dialogs.CHOOSEFONTW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('COMDLG32.dll')
def PrintDlgA(pPD: POINTER(Windows.Win32.UI.Controls.Dialogs.PRINTDLGA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('COMDLG32.dll')
def PrintDlgW(pPD: POINTER(Windows.Win32.UI.Controls.Dialogs.PRINTDLGW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('COMDLG32.dll')
def PrintDlgExA(pPD: POINTER(Windows.Win32.UI.Controls.Dialogs.PRINTDLGEXA_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('COMDLG32.dll')
def PrintDlgExW(pPD: POINTER(Windows.Win32.UI.Controls.Dialogs.PRINTDLGEXW_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('COMDLG32.dll')
def CommDlgExtendedError() -> Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS: ...
@winfunctype('COMDLG32.dll')
def PageSetupDlgA(param0: POINTER(Windows.Win32.UI.Controls.Dialogs.PAGESETUPDLGA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('COMDLG32.dll')
def PageSetupDlgW(param0: POINTER(Windows.Win32.UI.Controls.Dialogs.PAGESETUPDLGW_head)) -> Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X64,ARM64':
    class CHOOSECOLORA(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hInstance: Windows.Win32.Foundation.HWND
        rgbResult: Windows.Win32.Foundation.COLORREF
        lpCustColors: POINTER(Windows.Win32.Foundation.COLORREF)
        Flags: Windows.Win32.UI.Controls.Dialogs.CHOOSECOLOR_FLAGS
        lCustData: Windows.Win32.Foundation.LPARAM
        lpfnHook: Windows.Win32.UI.Controls.Dialogs.LPCCHOOKPROC
        lpTemplateName: Windows.Win32.Foundation.PSTR
if ARCH in 'X86':
    class CHOOSECOLORA(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hInstance: Windows.Win32.Foundation.HWND
        rgbResult: Windows.Win32.Foundation.COLORREF
        lpCustColors: POINTER(Windows.Win32.Foundation.COLORREF)
        Flags: Windows.Win32.UI.Controls.Dialogs.CHOOSECOLOR_FLAGS
        lCustData: Windows.Win32.Foundation.LPARAM
        lpfnHook: Windows.Win32.UI.Controls.Dialogs.LPCCHOOKPROC
        lpTemplateName: Windows.Win32.Foundation.PSTR
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class CHOOSECOLORW(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hInstance: Windows.Win32.Foundation.HWND
        rgbResult: Windows.Win32.Foundation.COLORREF
        lpCustColors: POINTER(Windows.Win32.Foundation.COLORREF)
        Flags: Windows.Win32.UI.Controls.Dialogs.CHOOSECOLOR_FLAGS
        lCustData: Windows.Win32.Foundation.LPARAM
        lpfnHook: Windows.Win32.UI.Controls.Dialogs.LPCCHOOKPROC
        lpTemplateName: Windows.Win32.Foundation.PWSTR
if ARCH in 'X86':
    class CHOOSECOLORW(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hInstance: Windows.Win32.Foundation.HWND
        rgbResult: Windows.Win32.Foundation.COLORREF
        lpCustColors: POINTER(Windows.Win32.Foundation.COLORREF)
        Flags: Windows.Win32.UI.Controls.Dialogs.CHOOSECOLOR_FLAGS
        lCustData: Windows.Win32.Foundation.LPARAM
        lpfnHook: Windows.Win32.UI.Controls.Dialogs.LPCCHOOKPROC
        lpTemplateName: Windows.Win32.Foundation.PWSTR
        _pack_ = 1
CHOOSECOLOR_FLAGS = UInt32
CC_RGBINIT: CHOOSECOLOR_FLAGS = 1
CC_FULLOPEN: CHOOSECOLOR_FLAGS = 2
CC_PREVENTFULLOPEN: CHOOSECOLOR_FLAGS = 4
CC_SHOWHELP: CHOOSECOLOR_FLAGS = 8
CC_ENABLEHOOK: CHOOSECOLOR_FLAGS = 16
CC_ENABLETEMPLATE: CHOOSECOLOR_FLAGS = 32
CC_ENABLETEMPLATEHANDLE: CHOOSECOLOR_FLAGS = 64
CC_SOLIDCOLOR: CHOOSECOLOR_FLAGS = 128
CC_ANYCOLOR: CHOOSECOLOR_FLAGS = 256
if ARCH in 'X64,ARM64':
    class CHOOSEFONTA(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hDC: Windows.Win32.Graphics.Gdi.HDC
        lpLogFont: POINTER(Windows.Win32.Graphics.Gdi.LOGFONTA_head)
        iPointSize: Int32
        Flags: Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS
        rgbColors: Windows.Win32.Foundation.COLORREF
        lCustData: Windows.Win32.Foundation.LPARAM
        lpfnHook: Windows.Win32.UI.Controls.Dialogs.LPCFHOOKPROC
        lpTemplateName: Windows.Win32.Foundation.PSTR
        hInstance: Windows.Win32.Foundation.HMODULE
        lpszStyle: Windows.Win32.Foundation.PSTR
        nFontType: Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FONT_TYPE
        ___MISSING_ALIGNMENT__: UInt16
        nSizeMin: Int32
        nSizeMax: Int32
if ARCH in 'X86':
    class CHOOSEFONTA(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hDC: Windows.Win32.Graphics.Gdi.HDC
        lpLogFont: POINTER(Windows.Win32.Graphics.Gdi.LOGFONTA_head)
        iPointSize: Int32
        Flags: Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS
        rgbColors: Windows.Win32.Foundation.COLORREF
        lCustData: Windows.Win32.Foundation.LPARAM
        lpfnHook: Windows.Win32.UI.Controls.Dialogs.LPCFHOOKPROC
        lpTemplateName: Windows.Win32.Foundation.PSTR
        hInstance: Windows.Win32.Foundation.HMODULE
        lpszStyle: Windows.Win32.Foundation.PSTR
        nFontType: Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FONT_TYPE
        ___MISSING_ALIGNMENT__: UInt16
        nSizeMin: Int32
        nSizeMax: Int32
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class CHOOSEFONTW(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hDC: Windows.Win32.Graphics.Gdi.HDC
        lpLogFont: POINTER(Windows.Win32.Graphics.Gdi.LOGFONTW_head)
        iPointSize: Int32
        Flags: Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS
        rgbColors: Windows.Win32.Foundation.COLORREF
        lCustData: Windows.Win32.Foundation.LPARAM
        lpfnHook: Windows.Win32.UI.Controls.Dialogs.LPCFHOOKPROC
        lpTemplateName: Windows.Win32.Foundation.PWSTR
        hInstance: Windows.Win32.Foundation.HMODULE
        lpszStyle: Windows.Win32.Foundation.PWSTR
        nFontType: Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FONT_TYPE
        ___MISSING_ALIGNMENT__: UInt16
        nSizeMin: Int32
        nSizeMax: Int32
if ARCH in 'X86':
    class CHOOSEFONTW(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hDC: Windows.Win32.Graphics.Gdi.HDC
        lpLogFont: POINTER(Windows.Win32.Graphics.Gdi.LOGFONTW_head)
        iPointSize: Int32
        Flags: Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS
        rgbColors: Windows.Win32.Foundation.COLORREF
        lCustData: Windows.Win32.Foundation.LPARAM
        lpfnHook: Windows.Win32.UI.Controls.Dialogs.LPCFHOOKPROC
        lpTemplateName: Windows.Win32.Foundation.PWSTR
        hInstance: Windows.Win32.Foundation.HMODULE
        lpszStyle: Windows.Win32.Foundation.PWSTR
        nFontType: Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FONT_TYPE
        ___MISSING_ALIGNMENT__: UInt16
        nSizeMin: Int32
        nSizeMax: Int32
        _pack_ = 1
CHOOSEFONT_FLAGS = UInt32
CF_APPLY: CHOOSEFONT_FLAGS = 512
CF_ANSIONLY: CHOOSEFONT_FLAGS = 1024
CF_BOTH: CHOOSEFONT_FLAGS = 3
CF_EFFECTS: CHOOSEFONT_FLAGS = 256
CF_ENABLEHOOK: CHOOSEFONT_FLAGS = 8
CF_ENABLETEMPLATE: CHOOSEFONT_FLAGS = 16
CF_ENABLETEMPLATEHANDLE: CHOOSEFONT_FLAGS = 32
CF_FIXEDPITCHONLY: CHOOSEFONT_FLAGS = 16384
CF_FORCEFONTEXIST: CHOOSEFONT_FLAGS = 65536
CF_INACTIVEFONTS: CHOOSEFONT_FLAGS = 33554432
CF_INITTOLOGFONTSTRUCT: CHOOSEFONT_FLAGS = 64
CF_LIMITSIZE: CHOOSEFONT_FLAGS = 8192
CF_NOOEMFONTS: CHOOSEFONT_FLAGS = 2048
CF_NOFACESEL: CHOOSEFONT_FLAGS = 524288
CF_NOSCRIPTSEL: CHOOSEFONT_FLAGS = 8388608
CF_NOSIMULATIONS: CHOOSEFONT_FLAGS = 4096
CF_NOSIZESEL: CHOOSEFONT_FLAGS = 2097152
CF_NOSTYLESEL: CHOOSEFONT_FLAGS = 1048576
CF_NOVECTORFONTS: CHOOSEFONT_FLAGS = 2048
CF_NOVERTFONTS: CHOOSEFONT_FLAGS = 16777216
CF_PRINTERFONTS: CHOOSEFONT_FLAGS = 2
CF_SCALABLEONLY: CHOOSEFONT_FLAGS = 131072
CF_SCREENFONTS: CHOOSEFONT_FLAGS = 1
CF_SCRIPTSONLY: CHOOSEFONT_FLAGS = 1024
CF_SELECTSCRIPT: CHOOSEFONT_FLAGS = 4194304
CF_SHOWHELP: CHOOSEFONT_FLAGS = 4
CF_TTONLY: CHOOSEFONT_FLAGS = 262144
CF_USESTYLE: CHOOSEFONT_FLAGS = 128
CF_WYSIWYG: CHOOSEFONT_FLAGS = 32768
CHOOSEFONT_FONT_TYPE = UInt16
BOLD_FONTTYPE: CHOOSEFONT_FONT_TYPE = 256
ITALIC_FONTTYPE: CHOOSEFONT_FONT_TYPE = 512
PRINTER_FONTTYPE: CHOOSEFONT_FONT_TYPE = 16384
REGULAR_FONTTYPE: CHOOSEFONT_FONT_TYPE = 1024
SCREEN_FONTTYPE: CHOOSEFONT_FONT_TYPE = 8192
SIMULATED_FONTTYPE: CHOOSEFONT_FONT_TYPE = 32768
COMMON_DLG_ERRORS = UInt32
CDERR_DIALOGFAILURE: COMMON_DLG_ERRORS = 65535
CDERR_GENERALCODES: COMMON_DLG_ERRORS = 0
CDERR_STRUCTSIZE: COMMON_DLG_ERRORS = 1
CDERR_INITIALIZATION: COMMON_DLG_ERRORS = 2
CDERR_NOTEMPLATE: COMMON_DLG_ERRORS = 3
CDERR_NOHINSTANCE: COMMON_DLG_ERRORS = 4
CDERR_LOADSTRFAILURE: COMMON_DLG_ERRORS = 5
CDERR_FINDRESFAILURE: COMMON_DLG_ERRORS = 6
CDERR_LOADRESFAILURE: COMMON_DLG_ERRORS = 7
CDERR_LOCKRESFAILURE: COMMON_DLG_ERRORS = 8
CDERR_MEMALLOCFAILURE: COMMON_DLG_ERRORS = 9
CDERR_MEMLOCKFAILURE: COMMON_DLG_ERRORS = 10
CDERR_NOHOOK: COMMON_DLG_ERRORS = 11
CDERR_REGISTERMSGFAIL: COMMON_DLG_ERRORS = 12
PDERR_PRINTERCODES: COMMON_DLG_ERRORS = 4096
PDERR_SETUPFAILURE: COMMON_DLG_ERRORS = 4097
PDERR_PARSEFAILURE: COMMON_DLG_ERRORS = 4098
PDERR_RETDEFFAILURE: COMMON_DLG_ERRORS = 4099
PDERR_LOADDRVFAILURE: COMMON_DLG_ERRORS = 4100
PDERR_GETDEVMODEFAIL: COMMON_DLG_ERRORS = 4101
PDERR_INITFAILURE: COMMON_DLG_ERRORS = 4102
PDERR_NODEVICES: COMMON_DLG_ERRORS = 4103
PDERR_NODEFAULTPRN: COMMON_DLG_ERRORS = 4104
PDERR_DNDMMISMATCH: COMMON_DLG_ERRORS = 4105
PDERR_CREATEICFAILURE: COMMON_DLG_ERRORS = 4106
PDERR_PRINTERNOTFOUND: COMMON_DLG_ERRORS = 4107
PDERR_DEFAULTDIFFERENT: COMMON_DLG_ERRORS = 4108
CFERR_CHOOSEFONTCODES: COMMON_DLG_ERRORS = 8192
CFERR_NOFONTS: COMMON_DLG_ERRORS = 8193
CFERR_MAXLESSTHANMIN: COMMON_DLG_ERRORS = 8194
FNERR_FILENAMECODES: COMMON_DLG_ERRORS = 12288
FNERR_SUBCLASSFAILURE: COMMON_DLG_ERRORS = 12289
FNERR_INVALIDFILENAME: COMMON_DLG_ERRORS = 12290
FNERR_BUFFERTOOSMALL: COMMON_DLG_ERRORS = 12291
FRERR_FINDREPLACECODES: COMMON_DLG_ERRORS = 16384
FRERR_BUFFERLENGTHZERO: COMMON_DLG_ERRORS = 16385
CCERR_CHOOSECOLORCODES: COMMON_DLG_ERRORS = 20480
if ARCH in 'X64,ARM64':
    class DEVNAMES(EasyCastStructure):
        wDriverOffset: UInt16
        wDeviceOffset: UInt16
        wOutputOffset: UInt16
        wDefault: UInt16
if ARCH in 'X86':
    class DEVNAMES(EasyCastStructure):
        wDriverOffset: UInt16
        wDeviceOffset: UInt16
        wOutputOffset: UInt16
        wDefault: UInt16
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class FINDREPLACEA(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hInstance: Windows.Win32.Foundation.HMODULE
        Flags: Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS
        lpstrFindWhat: Windows.Win32.Foundation.PSTR
        lpstrReplaceWith: Windows.Win32.Foundation.PSTR
        wFindWhatLen: UInt16
        wReplaceWithLen: UInt16
        lCustData: Windows.Win32.Foundation.LPARAM
        lpfnHook: Windows.Win32.UI.Controls.Dialogs.LPFRHOOKPROC
        lpTemplateName: Windows.Win32.Foundation.PSTR
if ARCH in 'X86':
    class FINDREPLACEA(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hInstance: Windows.Win32.Foundation.HMODULE
        Flags: Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS
        lpstrFindWhat: Windows.Win32.Foundation.PSTR
        lpstrReplaceWith: Windows.Win32.Foundation.PSTR
        wFindWhatLen: UInt16
        wReplaceWithLen: UInt16
        lCustData: Windows.Win32.Foundation.LPARAM
        lpfnHook: Windows.Win32.UI.Controls.Dialogs.LPFRHOOKPROC
        lpTemplateName: Windows.Win32.Foundation.PSTR
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class FINDREPLACEW(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hInstance: Windows.Win32.Foundation.HMODULE
        Flags: Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS
        lpstrFindWhat: Windows.Win32.Foundation.PWSTR
        lpstrReplaceWith: Windows.Win32.Foundation.PWSTR
        wFindWhatLen: UInt16
        wReplaceWithLen: UInt16
        lCustData: Windows.Win32.Foundation.LPARAM
        lpfnHook: Windows.Win32.UI.Controls.Dialogs.LPFRHOOKPROC
        lpTemplateName: Windows.Win32.Foundation.PWSTR
if ARCH in 'X86':
    class FINDREPLACEW(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hInstance: Windows.Win32.Foundation.HMODULE
        Flags: Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS
        lpstrFindWhat: Windows.Win32.Foundation.PWSTR
        lpstrReplaceWith: Windows.Win32.Foundation.PWSTR
        wFindWhatLen: UInt16
        wReplaceWithLen: UInt16
        lCustData: Windows.Win32.Foundation.LPARAM
        lpfnHook: Windows.Win32.UI.Controls.Dialogs.LPFRHOOKPROC
        lpTemplateName: Windows.Win32.Foundation.PWSTR
        _pack_ = 1
FINDREPLACE_FLAGS = UInt32
FR_DIALOGTERM: FINDREPLACE_FLAGS = 64
FR_DOWN: FINDREPLACE_FLAGS = 1
FR_ENABLEHOOK: FINDREPLACE_FLAGS = 256
FR_ENABLETEMPLATE: FINDREPLACE_FLAGS = 512
FR_ENABLETEMPLATEHANDLE: FINDREPLACE_FLAGS = 8192
FR_FINDNEXT: FINDREPLACE_FLAGS = 8
FR_HIDEUPDOWN: FINDREPLACE_FLAGS = 16384
FR_HIDEMATCHCASE: FINDREPLACE_FLAGS = 32768
FR_HIDEWHOLEWORD: FINDREPLACE_FLAGS = 65536
FR_MATCHCASE: FINDREPLACE_FLAGS = 4
FR_NOMATCHCASE: FINDREPLACE_FLAGS = 2048
FR_NOUPDOWN: FINDREPLACE_FLAGS = 1024
FR_NOWHOLEWORD: FINDREPLACE_FLAGS = 4096
FR_REPLACE: FINDREPLACE_FLAGS = 16
FR_REPLACEALL: FINDREPLACE_FLAGS = 32
FR_SHOWHELP: FINDREPLACE_FLAGS = 128
FR_WHOLEWORD: FINDREPLACE_FLAGS = 2
class IPrintDialogCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5852a2c3-6530-11d1-b6-a3-00-00-f8-75-7b-f9')
    @commethod(3)
    def InitDone(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SelectionChange(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def HandleMessage(self, hDlg: Windows.Win32.Foundation.HWND, uMsg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM, pResult: POINTER(Windows.Win32.Foundation.LRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
class IPrintDialogServices(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('509aaeda-5639-11d1-b6-a1-00-00-f8-75-7b-f9')
    @commethod(3)
    def GetCurrentDevMode(self, pDevMode: POINTER(Windows.Win32.Graphics.Gdi.DEVMODEA_head), pcbSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentPrinterName(self, pPrinterName: Windows.Win32.Foundation.PWSTR, pcchSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrentPortName(self, pPortName: Windows.Win32.Foundation.PWSTR, pcchSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def LPCCHOOKPROC(param0: Windows.Win32.Foundation.HWND, param1: UInt32, param2: Windows.Win32.Foundation.WPARAM, param3: Windows.Win32.Foundation.LPARAM) -> UIntPtr: ...
@winfunctype_pointer
def LPCFHOOKPROC(param0: Windows.Win32.Foundation.HWND, param1: UInt32, param2: Windows.Win32.Foundation.WPARAM, param3: Windows.Win32.Foundation.LPARAM) -> UIntPtr: ...
@winfunctype_pointer
def LPFRHOOKPROC(param0: Windows.Win32.Foundation.HWND, param1: UInt32, param2: Windows.Win32.Foundation.WPARAM, param3: Windows.Win32.Foundation.LPARAM) -> UIntPtr: ...
@winfunctype_pointer
def LPOFNHOOKPROC(param0: Windows.Win32.Foundation.HWND, param1: UInt32, param2: Windows.Win32.Foundation.WPARAM, param3: Windows.Win32.Foundation.LPARAM) -> UIntPtr: ...
@winfunctype_pointer
def LPPAGEPAINTHOOK(param0: Windows.Win32.Foundation.HWND, param1: UInt32, param2: Windows.Win32.Foundation.WPARAM, param3: Windows.Win32.Foundation.LPARAM) -> UIntPtr: ...
@winfunctype_pointer
def LPPAGESETUPHOOK(param0: Windows.Win32.Foundation.HWND, param1: UInt32, param2: Windows.Win32.Foundation.WPARAM, param3: Windows.Win32.Foundation.LPARAM) -> UIntPtr: ...
@winfunctype_pointer
def LPPRINTHOOKPROC(param0: Windows.Win32.Foundation.HWND, param1: UInt32, param2: Windows.Win32.Foundation.WPARAM, param3: Windows.Win32.Foundation.LPARAM) -> UIntPtr: ...
@winfunctype_pointer
def LPSETUPHOOKPROC(param0: Windows.Win32.Foundation.HWND, param1: UInt32, param2: Windows.Win32.Foundation.WPARAM, param3: Windows.Win32.Foundation.LPARAM) -> UIntPtr: ...
if ARCH in 'X64,ARM64':
    class OFNOTIFYA(EasyCastStructure):
        hdr: Windows.Win32.UI.Controls.NMHDR
        lpOFN: POINTER(Windows.Win32.UI.Controls.Dialogs.OPENFILENAMEA_head)
        pszFile: Windows.Win32.Foundation.PSTR
if ARCH in 'X86':
    class OFNOTIFYA(EasyCastStructure):
        hdr: Windows.Win32.UI.Controls.NMHDR
        lpOFN: POINTER(Windows.Win32.UI.Controls.Dialogs.OPENFILENAMEA_head)
        pszFile: Windows.Win32.Foundation.PSTR
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class OFNOTIFYEXA(EasyCastStructure):
        hdr: Windows.Win32.UI.Controls.NMHDR
        lpOFN: POINTER(Windows.Win32.UI.Controls.Dialogs.OPENFILENAMEA_head)
        psf: c_void_p
        pidl: c_void_p
if ARCH in 'X86':
    class OFNOTIFYEXA(EasyCastStructure):
        hdr: Windows.Win32.UI.Controls.NMHDR
        lpOFN: POINTER(Windows.Win32.UI.Controls.Dialogs.OPENFILENAMEA_head)
        psf: c_void_p
        pidl: c_void_p
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class OFNOTIFYEXW(EasyCastStructure):
        hdr: Windows.Win32.UI.Controls.NMHDR
        lpOFN: POINTER(Windows.Win32.UI.Controls.Dialogs.OPENFILENAMEW_head)
        psf: c_void_p
        pidl: c_void_p
if ARCH in 'X86':
    class OFNOTIFYEXW(EasyCastStructure):
        hdr: Windows.Win32.UI.Controls.NMHDR
        lpOFN: POINTER(Windows.Win32.UI.Controls.Dialogs.OPENFILENAMEW_head)
        psf: c_void_p
        pidl: c_void_p
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class OFNOTIFYW(EasyCastStructure):
        hdr: Windows.Win32.UI.Controls.NMHDR
        lpOFN: POINTER(Windows.Win32.UI.Controls.Dialogs.OPENFILENAMEW_head)
        pszFile: Windows.Win32.Foundation.PWSTR
if ARCH in 'X86':
    class OFNOTIFYW(EasyCastStructure):
        hdr: Windows.Win32.UI.Controls.NMHDR
        lpOFN: POINTER(Windows.Win32.UI.Controls.Dialogs.OPENFILENAMEW_head)
        pszFile: Windows.Win32.Foundation.PWSTR
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class OPENFILENAMEA(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hInstance: Windows.Win32.Foundation.HMODULE
        lpstrFilter: Windows.Win32.Foundation.PSTR
        lpstrCustomFilter: Windows.Win32.Foundation.PSTR
        nMaxCustFilter: UInt32
        nFilterIndex: UInt32
        lpstrFile: Windows.Win32.Foundation.PSTR
        nMaxFile: UInt32
        lpstrFileTitle: Windows.Win32.Foundation.PSTR
        nMaxFileTitle: UInt32
        lpstrInitialDir: Windows.Win32.Foundation.PSTR
        lpstrTitle: Windows.Win32.Foundation.PSTR
        Flags: Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS
        nFileOffset: UInt16
        nFileExtension: UInt16
        lpstrDefExt: Windows.Win32.Foundation.PSTR
        lCustData: Windows.Win32.Foundation.LPARAM
        lpfnHook: Windows.Win32.UI.Controls.Dialogs.LPOFNHOOKPROC
        lpTemplateName: Windows.Win32.Foundation.PSTR
        pvReserved: c_void_p
        dwReserved: UInt32
        FlagsEx: Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS_EX
if ARCH in 'X86':
    class OPENFILENAMEA(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hInstance: Windows.Win32.Foundation.HMODULE
        lpstrFilter: Windows.Win32.Foundation.PSTR
        lpstrCustomFilter: Windows.Win32.Foundation.PSTR
        nMaxCustFilter: UInt32
        nFilterIndex: UInt32
        lpstrFile: Windows.Win32.Foundation.PSTR
        nMaxFile: UInt32
        lpstrFileTitle: Windows.Win32.Foundation.PSTR
        nMaxFileTitle: UInt32
        lpstrInitialDir: Windows.Win32.Foundation.PSTR
        lpstrTitle: Windows.Win32.Foundation.PSTR
        Flags: Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS
        nFileOffset: UInt16
        nFileExtension: UInt16
        lpstrDefExt: Windows.Win32.Foundation.PSTR
        lCustData: Windows.Win32.Foundation.LPARAM
        lpfnHook: Windows.Win32.UI.Controls.Dialogs.LPOFNHOOKPROC
        lpTemplateName: Windows.Win32.Foundation.PSTR
        pvReserved: c_void_p
        dwReserved: UInt32
        FlagsEx: Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS_EX
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class OPENFILENAMEW(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hInstance: Windows.Win32.Foundation.HMODULE
        lpstrFilter: Windows.Win32.Foundation.PWSTR
        lpstrCustomFilter: Windows.Win32.Foundation.PWSTR
        nMaxCustFilter: UInt32
        nFilterIndex: UInt32
        lpstrFile: Windows.Win32.Foundation.PWSTR
        nMaxFile: UInt32
        lpstrFileTitle: Windows.Win32.Foundation.PWSTR
        nMaxFileTitle: UInt32
        lpstrInitialDir: Windows.Win32.Foundation.PWSTR
        lpstrTitle: Windows.Win32.Foundation.PWSTR
        Flags: Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS
        nFileOffset: UInt16
        nFileExtension: UInt16
        lpstrDefExt: Windows.Win32.Foundation.PWSTR
        lCustData: Windows.Win32.Foundation.LPARAM
        lpfnHook: Windows.Win32.UI.Controls.Dialogs.LPOFNHOOKPROC
        lpTemplateName: Windows.Win32.Foundation.PWSTR
        pvReserved: c_void_p
        dwReserved: UInt32
        FlagsEx: Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS_EX
if ARCH in 'X86':
    class OPENFILENAMEW(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hInstance: Windows.Win32.Foundation.HMODULE
        lpstrFilter: Windows.Win32.Foundation.PWSTR
        lpstrCustomFilter: Windows.Win32.Foundation.PWSTR
        nMaxCustFilter: UInt32
        nFilterIndex: UInt32
        lpstrFile: Windows.Win32.Foundation.PWSTR
        nMaxFile: UInt32
        lpstrFileTitle: Windows.Win32.Foundation.PWSTR
        nMaxFileTitle: UInt32
        lpstrInitialDir: Windows.Win32.Foundation.PWSTR
        lpstrTitle: Windows.Win32.Foundation.PWSTR
        Flags: Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS
        nFileOffset: UInt16
        nFileExtension: UInt16
        lpstrDefExt: Windows.Win32.Foundation.PWSTR
        lCustData: Windows.Win32.Foundation.LPARAM
        lpfnHook: Windows.Win32.UI.Controls.Dialogs.LPOFNHOOKPROC
        lpTemplateName: Windows.Win32.Foundation.PWSTR
        pvReserved: c_void_p
        dwReserved: UInt32
        FlagsEx: Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS_EX
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class OPENFILENAME_NT4A(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hInstance: Windows.Win32.Foundation.HMODULE
        lpstrFilter: Windows.Win32.Foundation.PSTR
        lpstrCustomFilter: Windows.Win32.Foundation.PSTR
        nMaxCustFilter: UInt32
        nFilterIndex: UInt32
        lpstrFile: Windows.Win32.Foundation.PSTR
        nMaxFile: UInt32
        lpstrFileTitle: Windows.Win32.Foundation.PSTR
        nMaxFileTitle: UInt32
        lpstrInitialDir: Windows.Win32.Foundation.PSTR
        lpstrTitle: Windows.Win32.Foundation.PSTR
        Flags: UInt32
        nFileOffset: UInt16
        nFileExtension: UInt16
        lpstrDefExt: Windows.Win32.Foundation.PSTR
        lCustData: Windows.Win32.Foundation.LPARAM
        lpfnHook: Windows.Win32.UI.Controls.Dialogs.LPOFNHOOKPROC
        lpTemplateName: Windows.Win32.Foundation.PSTR
if ARCH in 'X86':
    class OPENFILENAME_NT4A(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hInstance: Windows.Win32.Foundation.HMODULE
        lpstrFilter: Windows.Win32.Foundation.PSTR
        lpstrCustomFilter: Windows.Win32.Foundation.PSTR
        nMaxCustFilter: UInt32
        nFilterIndex: UInt32
        lpstrFile: Windows.Win32.Foundation.PSTR
        nMaxFile: UInt32
        lpstrFileTitle: Windows.Win32.Foundation.PSTR
        nMaxFileTitle: UInt32
        lpstrInitialDir: Windows.Win32.Foundation.PSTR
        lpstrTitle: Windows.Win32.Foundation.PSTR
        Flags: UInt32
        nFileOffset: UInt16
        nFileExtension: UInt16
        lpstrDefExt: Windows.Win32.Foundation.PSTR
        lCustData: Windows.Win32.Foundation.LPARAM
        lpfnHook: Windows.Win32.UI.Controls.Dialogs.LPOFNHOOKPROC
        lpTemplateName: Windows.Win32.Foundation.PSTR
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class OPENFILENAME_NT4W(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hInstance: Windows.Win32.Foundation.HMODULE
        lpstrFilter: Windows.Win32.Foundation.PWSTR
        lpstrCustomFilter: Windows.Win32.Foundation.PWSTR
        nMaxCustFilter: UInt32
        nFilterIndex: UInt32
        lpstrFile: Windows.Win32.Foundation.PWSTR
        nMaxFile: UInt32
        lpstrFileTitle: Windows.Win32.Foundation.PWSTR
        nMaxFileTitle: UInt32
        lpstrInitialDir: Windows.Win32.Foundation.PWSTR
        lpstrTitle: Windows.Win32.Foundation.PWSTR
        Flags: UInt32
        nFileOffset: UInt16
        nFileExtension: UInt16
        lpstrDefExt: Windows.Win32.Foundation.PWSTR
        lCustData: Windows.Win32.Foundation.LPARAM
        lpfnHook: Windows.Win32.UI.Controls.Dialogs.LPOFNHOOKPROC
        lpTemplateName: Windows.Win32.Foundation.PWSTR
if ARCH in 'X86':
    class OPENFILENAME_NT4W(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hInstance: Windows.Win32.Foundation.HMODULE
        lpstrFilter: Windows.Win32.Foundation.PWSTR
        lpstrCustomFilter: Windows.Win32.Foundation.PWSTR
        nMaxCustFilter: UInt32
        nFilterIndex: UInt32
        lpstrFile: Windows.Win32.Foundation.PWSTR
        nMaxFile: UInt32
        lpstrFileTitle: Windows.Win32.Foundation.PWSTR
        nMaxFileTitle: UInt32
        lpstrInitialDir: Windows.Win32.Foundation.PWSTR
        lpstrTitle: Windows.Win32.Foundation.PWSTR
        Flags: UInt32
        nFileOffset: UInt16
        nFileExtension: UInt16
        lpstrDefExt: Windows.Win32.Foundation.PWSTR
        lCustData: Windows.Win32.Foundation.LPARAM
        lpfnHook: Windows.Win32.UI.Controls.Dialogs.LPOFNHOOKPROC
        lpTemplateName: Windows.Win32.Foundation.PWSTR
        _pack_ = 1
OPEN_FILENAME_FLAGS = UInt32
OFN_READONLY: OPEN_FILENAME_FLAGS = 1
OFN_OVERWRITEPROMPT: OPEN_FILENAME_FLAGS = 2
OFN_HIDEREADONLY: OPEN_FILENAME_FLAGS = 4
OFN_NOCHANGEDIR: OPEN_FILENAME_FLAGS = 8
OFN_SHOWHELP: OPEN_FILENAME_FLAGS = 16
OFN_ENABLEHOOK: OPEN_FILENAME_FLAGS = 32
OFN_ENABLETEMPLATE: OPEN_FILENAME_FLAGS = 64
OFN_ENABLETEMPLATEHANDLE: OPEN_FILENAME_FLAGS = 128
OFN_NOVALIDATE: OPEN_FILENAME_FLAGS = 256
OFN_ALLOWMULTISELECT: OPEN_FILENAME_FLAGS = 512
OFN_EXTENSIONDIFFERENT: OPEN_FILENAME_FLAGS = 1024
OFN_PATHMUSTEXIST: OPEN_FILENAME_FLAGS = 2048
OFN_FILEMUSTEXIST: OPEN_FILENAME_FLAGS = 4096
OFN_CREATEPROMPT: OPEN_FILENAME_FLAGS = 8192
OFN_SHAREAWARE: OPEN_FILENAME_FLAGS = 16384
OFN_NOREADONLYRETURN: OPEN_FILENAME_FLAGS = 32768
OFN_NOTESTFILECREATE: OPEN_FILENAME_FLAGS = 65536
OFN_NONETWORKBUTTON: OPEN_FILENAME_FLAGS = 131072
OFN_NOLONGNAMES: OPEN_FILENAME_FLAGS = 262144
OFN_EXPLORER: OPEN_FILENAME_FLAGS = 524288
OFN_NODEREFERENCELINKS: OPEN_FILENAME_FLAGS = 1048576
OFN_LONGNAMES: OPEN_FILENAME_FLAGS = 2097152
OFN_ENABLEINCLUDENOTIFY: OPEN_FILENAME_FLAGS = 4194304
OFN_ENABLESIZING: OPEN_FILENAME_FLAGS = 8388608
OFN_DONTADDTORECENT: OPEN_FILENAME_FLAGS = 33554432
OFN_FORCESHOWHIDDEN: OPEN_FILENAME_FLAGS = 268435456
OPEN_FILENAME_FLAGS_EX = UInt32
OFN_EX_NONE: OPEN_FILENAME_FLAGS_EX = 0
OFN_EX_NOPLACESBAR: OPEN_FILENAME_FLAGS_EX = 1
if ARCH in 'X64,ARM64':
    class PAGESETUPDLGA(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hDevMode: Windows.Win32.Foundation.HGLOBAL
        hDevNames: Windows.Win32.Foundation.HGLOBAL
        Flags: Windows.Win32.UI.Controls.Dialogs.PAGESETUPDLG_FLAGS
        ptPaperSize: Windows.Win32.Foundation.POINT
        rtMinMargin: Windows.Win32.Foundation.RECT
        rtMargin: Windows.Win32.Foundation.RECT
        hInstance: Windows.Win32.Foundation.HMODULE
        lCustData: Windows.Win32.Foundation.LPARAM
        lpfnPageSetupHook: Windows.Win32.UI.Controls.Dialogs.LPPAGESETUPHOOK
        lpfnPagePaintHook: Windows.Win32.UI.Controls.Dialogs.LPPAGEPAINTHOOK
        lpPageSetupTemplateName: Windows.Win32.Foundation.PSTR
        hPageSetupTemplate: Windows.Win32.Foundation.HGLOBAL
if ARCH in 'X86':
    class PAGESETUPDLGA(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hDevMode: Windows.Win32.Foundation.HGLOBAL
        hDevNames: Windows.Win32.Foundation.HGLOBAL
        Flags: Windows.Win32.UI.Controls.Dialogs.PAGESETUPDLG_FLAGS
        ptPaperSize: Windows.Win32.Foundation.POINT
        rtMinMargin: Windows.Win32.Foundation.RECT
        rtMargin: Windows.Win32.Foundation.RECT
        hInstance: Windows.Win32.Foundation.HMODULE
        lCustData: Windows.Win32.Foundation.LPARAM
        lpfnPageSetupHook: Windows.Win32.UI.Controls.Dialogs.LPPAGESETUPHOOK
        lpfnPagePaintHook: Windows.Win32.UI.Controls.Dialogs.LPPAGEPAINTHOOK
        lpPageSetupTemplateName: Windows.Win32.Foundation.PSTR
        hPageSetupTemplate: Windows.Win32.Foundation.HGLOBAL
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class PAGESETUPDLGW(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hDevMode: Windows.Win32.Foundation.HGLOBAL
        hDevNames: Windows.Win32.Foundation.HGLOBAL
        Flags: Windows.Win32.UI.Controls.Dialogs.PAGESETUPDLG_FLAGS
        ptPaperSize: Windows.Win32.Foundation.POINT
        rtMinMargin: Windows.Win32.Foundation.RECT
        rtMargin: Windows.Win32.Foundation.RECT
        hInstance: Windows.Win32.Foundation.HMODULE
        lCustData: Windows.Win32.Foundation.LPARAM
        lpfnPageSetupHook: Windows.Win32.UI.Controls.Dialogs.LPPAGESETUPHOOK
        lpfnPagePaintHook: Windows.Win32.UI.Controls.Dialogs.LPPAGEPAINTHOOK
        lpPageSetupTemplateName: Windows.Win32.Foundation.PWSTR
        hPageSetupTemplate: Windows.Win32.Foundation.HGLOBAL
if ARCH in 'X86':
    class PAGESETUPDLGW(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hDevMode: Windows.Win32.Foundation.HGLOBAL
        hDevNames: Windows.Win32.Foundation.HGLOBAL
        Flags: Windows.Win32.UI.Controls.Dialogs.PAGESETUPDLG_FLAGS
        ptPaperSize: Windows.Win32.Foundation.POINT
        rtMinMargin: Windows.Win32.Foundation.RECT
        rtMargin: Windows.Win32.Foundation.RECT
        hInstance: Windows.Win32.Foundation.HMODULE
        lCustData: Windows.Win32.Foundation.LPARAM
        lpfnPageSetupHook: Windows.Win32.UI.Controls.Dialogs.LPPAGESETUPHOOK
        lpfnPagePaintHook: Windows.Win32.UI.Controls.Dialogs.LPPAGEPAINTHOOK
        lpPageSetupTemplateName: Windows.Win32.Foundation.PWSTR
        hPageSetupTemplate: Windows.Win32.Foundation.HGLOBAL
        _pack_ = 1
PAGESETUPDLG_FLAGS = UInt32
PSD_DEFAULTMINMARGINS: PAGESETUPDLG_FLAGS = 0
PSD_DISABLEMARGINS: PAGESETUPDLG_FLAGS = 16
PSD_DISABLEORIENTATION: PAGESETUPDLG_FLAGS = 256
PSD_DISABLEPAGEPAINTING: PAGESETUPDLG_FLAGS = 524288
PSD_DISABLEPAPER: PAGESETUPDLG_FLAGS = 512
PSD_DISABLEPRINTER: PAGESETUPDLG_FLAGS = 32
PSD_ENABLEPAGEPAINTHOOK: PAGESETUPDLG_FLAGS = 262144
PSD_ENABLEPAGESETUPHOOK: PAGESETUPDLG_FLAGS = 8192
PSD_ENABLEPAGESETUPTEMPLATE: PAGESETUPDLG_FLAGS = 32768
PSD_ENABLEPAGESETUPTEMPLATEHANDLE: PAGESETUPDLG_FLAGS = 131072
PSD_INHUNDREDTHSOFMILLIMETERS: PAGESETUPDLG_FLAGS = 8
PSD_INTHOUSANDTHSOFINCHES: PAGESETUPDLG_FLAGS = 4
PSD_INWININIINTLMEASURE: PAGESETUPDLG_FLAGS = 0
PSD_MARGINS: PAGESETUPDLG_FLAGS = 2
PSD_MINMARGINS: PAGESETUPDLG_FLAGS = 1
PSD_NONETWORKBUTTON: PAGESETUPDLG_FLAGS = 2097152
PSD_NOWARNING: PAGESETUPDLG_FLAGS = 128
PSD_RETURNDEFAULT: PAGESETUPDLG_FLAGS = 1024
PSD_SHOWHELP: PAGESETUPDLG_FLAGS = 2048
if ARCH in 'X64,ARM64':
    class PRINTDLGA(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hDevMode: Windows.Win32.Foundation.HGLOBAL
        hDevNames: Windows.Win32.Foundation.HGLOBAL
        hDC: Windows.Win32.Graphics.Gdi.HDC
        Flags: Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS
        nFromPage: UInt16
        nToPage: UInt16
        nMinPage: UInt16
        nMaxPage: UInt16
        nCopies: UInt16
        hInstance: Windows.Win32.Foundation.HMODULE
        lCustData: Windows.Win32.Foundation.LPARAM
        lpfnPrintHook: Windows.Win32.UI.Controls.Dialogs.LPPRINTHOOKPROC
        lpfnSetupHook: Windows.Win32.UI.Controls.Dialogs.LPSETUPHOOKPROC
        lpPrintTemplateName: Windows.Win32.Foundation.PSTR
        lpSetupTemplateName: Windows.Win32.Foundation.PSTR
        hPrintTemplate: Windows.Win32.Foundation.HGLOBAL
        hSetupTemplate: Windows.Win32.Foundation.HGLOBAL
if ARCH in 'X86':
    class PRINTDLGA(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hDevMode: Windows.Win32.Foundation.HGLOBAL
        hDevNames: Windows.Win32.Foundation.HGLOBAL
        hDC: Windows.Win32.Graphics.Gdi.HDC
        Flags: Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS
        nFromPage: UInt16
        nToPage: UInt16
        nMinPage: UInt16
        nMaxPage: UInt16
        nCopies: UInt16
        hInstance: Windows.Win32.Foundation.HMODULE
        lCustData: Windows.Win32.Foundation.LPARAM
        lpfnPrintHook: Windows.Win32.UI.Controls.Dialogs.LPPRINTHOOKPROC
        lpfnSetupHook: Windows.Win32.UI.Controls.Dialogs.LPSETUPHOOKPROC
        lpPrintTemplateName: Windows.Win32.Foundation.PSTR
        lpSetupTemplateName: Windows.Win32.Foundation.PSTR
        hPrintTemplate: Windows.Win32.Foundation.HGLOBAL
        hSetupTemplate: Windows.Win32.Foundation.HGLOBAL
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class PRINTDLGEXA(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hDevMode: Windows.Win32.Foundation.HGLOBAL
        hDevNames: Windows.Win32.Foundation.HGLOBAL
        hDC: Windows.Win32.Graphics.Gdi.HDC
        Flags: Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS
        Flags2: UInt32
        ExclusionFlags: UInt32
        nPageRanges: UInt32
        nMaxPageRanges: UInt32
        lpPageRanges: POINTER(Windows.Win32.UI.Controls.Dialogs.PRINTPAGERANGE_head)
        nMinPage: UInt32
        nMaxPage: UInt32
        nCopies: UInt32
        hInstance: Windows.Win32.Foundation.HMODULE
        lpPrintTemplateName: Windows.Win32.Foundation.PSTR
        lpCallback: Windows.Win32.System.Com.IUnknown_head
        nPropertyPages: UInt32
        lphPropertyPages: POINTER(Windows.Win32.UI.Controls.HPROPSHEETPAGE)
        nStartPage: UInt32
        dwResultAction: UInt32
if ARCH in 'X86':
    class PRINTDLGEXA(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hDevMode: Windows.Win32.Foundation.HGLOBAL
        hDevNames: Windows.Win32.Foundation.HGLOBAL
        hDC: Windows.Win32.Graphics.Gdi.HDC
        Flags: Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS
        Flags2: UInt32
        ExclusionFlags: UInt32
        nPageRanges: UInt32
        nMaxPageRanges: UInt32
        lpPageRanges: POINTER(Windows.Win32.UI.Controls.Dialogs.PRINTPAGERANGE_head)
        nMinPage: UInt32
        nMaxPage: UInt32
        nCopies: UInt32
        hInstance: Windows.Win32.Foundation.HMODULE
        lpPrintTemplateName: Windows.Win32.Foundation.PSTR
        lpCallback: Windows.Win32.System.Com.IUnknown_head
        nPropertyPages: UInt32
        lphPropertyPages: POINTER(Windows.Win32.UI.Controls.HPROPSHEETPAGE)
        nStartPage: UInt32
        dwResultAction: UInt32
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class PRINTDLGEXW(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hDevMode: Windows.Win32.Foundation.HGLOBAL
        hDevNames: Windows.Win32.Foundation.HGLOBAL
        hDC: Windows.Win32.Graphics.Gdi.HDC
        Flags: Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS
        Flags2: UInt32
        ExclusionFlags: UInt32
        nPageRanges: UInt32
        nMaxPageRanges: UInt32
        lpPageRanges: POINTER(Windows.Win32.UI.Controls.Dialogs.PRINTPAGERANGE_head)
        nMinPage: UInt32
        nMaxPage: UInt32
        nCopies: UInt32
        hInstance: Windows.Win32.Foundation.HMODULE
        lpPrintTemplateName: Windows.Win32.Foundation.PWSTR
        lpCallback: Windows.Win32.System.Com.IUnknown_head
        nPropertyPages: UInt32
        lphPropertyPages: POINTER(Windows.Win32.UI.Controls.HPROPSHEETPAGE)
        nStartPage: UInt32
        dwResultAction: UInt32
if ARCH in 'X86':
    class PRINTDLGEXW(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hDevMode: Windows.Win32.Foundation.HGLOBAL
        hDevNames: Windows.Win32.Foundation.HGLOBAL
        hDC: Windows.Win32.Graphics.Gdi.HDC
        Flags: Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS
        Flags2: UInt32
        ExclusionFlags: UInt32
        nPageRanges: UInt32
        nMaxPageRanges: UInt32
        lpPageRanges: POINTER(Windows.Win32.UI.Controls.Dialogs.PRINTPAGERANGE_head)
        nMinPage: UInt32
        nMaxPage: UInt32
        nCopies: UInt32
        hInstance: Windows.Win32.Foundation.HMODULE
        lpPrintTemplateName: Windows.Win32.Foundation.PWSTR
        lpCallback: Windows.Win32.System.Com.IUnknown_head
        nPropertyPages: UInt32
        lphPropertyPages: POINTER(Windows.Win32.UI.Controls.HPROPSHEETPAGE)
        nStartPage: UInt32
        dwResultAction: UInt32
        _pack_ = 1
PRINTDLGEX_FLAGS = UInt32
PD_ALLPAGES: PRINTDLGEX_FLAGS = 0
PD_COLLATE: PRINTDLGEX_FLAGS = 16
PD_CURRENTPAGE: PRINTDLGEX_FLAGS = 4194304
PD_DISABLEPRINTTOFILE: PRINTDLGEX_FLAGS = 524288
PD_ENABLEPRINTTEMPLATE: PRINTDLGEX_FLAGS = 16384
PD_ENABLEPRINTTEMPLATEHANDLE: PRINTDLGEX_FLAGS = 65536
PD_EXCLUSIONFLAGS: PRINTDLGEX_FLAGS = 16777216
PD_HIDEPRINTTOFILE: PRINTDLGEX_FLAGS = 1048576
PD_NOCURRENTPAGE: PRINTDLGEX_FLAGS = 8388608
PD_NOPAGENUMS: PRINTDLGEX_FLAGS = 8
PD_NOSELECTION: PRINTDLGEX_FLAGS = 4
PD_NOWARNING: PRINTDLGEX_FLAGS = 128
PD_PAGENUMS: PRINTDLGEX_FLAGS = 2
PD_PRINTTOFILE: PRINTDLGEX_FLAGS = 32
PD_RETURNDC: PRINTDLGEX_FLAGS = 256
PD_RETURNDEFAULT: PRINTDLGEX_FLAGS = 1024
PD_RETURNIC: PRINTDLGEX_FLAGS = 512
PD_SELECTION: PRINTDLGEX_FLAGS = 1
PD_USEDEVMODECOPIES: PRINTDLGEX_FLAGS = 262144
PD_USEDEVMODECOPIESANDCOLLATE: PRINTDLGEX_FLAGS = 262144
PD_USELARGETEMPLATE: PRINTDLGEX_FLAGS = 268435456
PD_ENABLEPRINTHOOK: PRINTDLGEX_FLAGS = 4096
PD_ENABLESETUPHOOK: PRINTDLGEX_FLAGS = 8192
PD_ENABLESETUPTEMPLATE: PRINTDLGEX_FLAGS = 32768
PD_ENABLESETUPTEMPLATEHANDLE: PRINTDLGEX_FLAGS = 131072
PD_NONETWORKBUTTON: PRINTDLGEX_FLAGS = 2097152
PD_PRINTSETUP: PRINTDLGEX_FLAGS = 64
PD_SHOWHELP: PRINTDLGEX_FLAGS = 2048
if ARCH in 'X64,ARM64':
    class PRINTDLGW(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hDevMode: Windows.Win32.Foundation.HGLOBAL
        hDevNames: Windows.Win32.Foundation.HGLOBAL
        hDC: Windows.Win32.Graphics.Gdi.HDC
        Flags: Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS
        nFromPage: UInt16
        nToPage: UInt16
        nMinPage: UInt16
        nMaxPage: UInt16
        nCopies: UInt16
        hInstance: Windows.Win32.Foundation.HMODULE
        lCustData: Windows.Win32.Foundation.LPARAM
        lpfnPrintHook: Windows.Win32.UI.Controls.Dialogs.LPPRINTHOOKPROC
        lpfnSetupHook: Windows.Win32.UI.Controls.Dialogs.LPSETUPHOOKPROC
        lpPrintTemplateName: Windows.Win32.Foundation.PWSTR
        lpSetupTemplateName: Windows.Win32.Foundation.PWSTR
        hPrintTemplate: Windows.Win32.Foundation.HGLOBAL
        hSetupTemplate: Windows.Win32.Foundation.HGLOBAL
if ARCH in 'X86':
    class PRINTDLGW(EasyCastStructure):
        lStructSize: UInt32
        hwndOwner: Windows.Win32.Foundation.HWND
        hDevMode: Windows.Win32.Foundation.HGLOBAL
        hDevNames: Windows.Win32.Foundation.HGLOBAL
        hDC: Windows.Win32.Graphics.Gdi.HDC
        Flags: Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS
        nFromPage: UInt16
        nToPage: UInt16
        nMinPage: UInt16
        nMaxPage: UInt16
        nCopies: UInt16
        hInstance: Windows.Win32.Foundation.HMODULE
        lCustData: Windows.Win32.Foundation.LPARAM
        lpfnPrintHook: Windows.Win32.UI.Controls.Dialogs.LPPRINTHOOKPROC
        lpfnSetupHook: Windows.Win32.UI.Controls.Dialogs.LPSETUPHOOKPROC
        lpPrintTemplateName: Windows.Win32.Foundation.PWSTR
        lpSetupTemplateName: Windows.Win32.Foundation.PWSTR
        hPrintTemplate: Windows.Win32.Foundation.HGLOBAL
        hSetupTemplate: Windows.Win32.Foundation.HGLOBAL
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class PRINTPAGERANGE(EasyCastStructure):
        nFromPage: UInt32
        nToPage: UInt32
if ARCH in 'X86':
    class PRINTPAGERANGE(EasyCastStructure):
        nFromPage: UInt32
        nToPage: UInt32
        _pack_ = 1
if ARCH in 'X64,ARM64':
    make_head(_module, 'CHOOSECOLORA')
if ARCH in 'X86':
    make_head(_module, 'CHOOSECOLORA')
if ARCH in 'X64,ARM64':
    make_head(_module, 'CHOOSECOLORW')
if ARCH in 'X86':
    make_head(_module, 'CHOOSECOLORW')
if ARCH in 'X64,ARM64':
    make_head(_module, 'CHOOSEFONTA')
if ARCH in 'X86':
    make_head(_module, 'CHOOSEFONTA')
if ARCH in 'X64,ARM64':
    make_head(_module, 'CHOOSEFONTW')
if ARCH in 'X86':
    make_head(_module, 'CHOOSEFONTW')
if ARCH in 'X64,ARM64':
    make_head(_module, 'DEVNAMES')
if ARCH in 'X86':
    make_head(_module, 'DEVNAMES')
if ARCH in 'X64,ARM64':
    make_head(_module, 'FINDREPLACEA')
if ARCH in 'X86':
    make_head(_module, 'FINDREPLACEA')
if ARCH in 'X64,ARM64':
    make_head(_module, 'FINDREPLACEW')
if ARCH in 'X86':
    make_head(_module, 'FINDREPLACEW')
make_head(_module, 'IPrintDialogCallback')
make_head(_module, 'IPrintDialogServices')
make_head(_module, 'LPCCHOOKPROC')
make_head(_module, 'LPCFHOOKPROC')
make_head(_module, 'LPFRHOOKPROC')
make_head(_module, 'LPOFNHOOKPROC')
make_head(_module, 'LPPAGEPAINTHOOK')
make_head(_module, 'LPPAGESETUPHOOK')
make_head(_module, 'LPPRINTHOOKPROC')
make_head(_module, 'LPSETUPHOOKPROC')
if ARCH in 'X64,ARM64':
    make_head(_module, 'OFNOTIFYA')
if ARCH in 'X86':
    make_head(_module, 'OFNOTIFYA')
if ARCH in 'X64,ARM64':
    make_head(_module, 'OFNOTIFYEXA')
if ARCH in 'X86':
    make_head(_module, 'OFNOTIFYEXA')
if ARCH in 'X64,ARM64':
    make_head(_module, 'OFNOTIFYEXW')
if ARCH in 'X86':
    make_head(_module, 'OFNOTIFYEXW')
if ARCH in 'X64,ARM64':
    make_head(_module, 'OFNOTIFYW')
if ARCH in 'X86':
    make_head(_module, 'OFNOTIFYW')
if ARCH in 'X64,ARM64':
    make_head(_module, 'OPENFILENAMEA')
if ARCH in 'X86':
    make_head(_module, 'OPENFILENAMEA')
if ARCH in 'X64,ARM64':
    make_head(_module, 'OPENFILENAMEW')
if ARCH in 'X86':
    make_head(_module, 'OPENFILENAMEW')
if ARCH in 'X64,ARM64':
    make_head(_module, 'OPENFILENAME_NT4A')
if ARCH in 'X86':
    make_head(_module, 'OPENFILENAME_NT4A')
if ARCH in 'X64,ARM64':
    make_head(_module, 'OPENFILENAME_NT4W')
if ARCH in 'X86':
    make_head(_module, 'OPENFILENAME_NT4W')
if ARCH in 'X64,ARM64':
    make_head(_module, 'PAGESETUPDLGA')
if ARCH in 'X86':
    make_head(_module, 'PAGESETUPDLGA')
if ARCH in 'X64,ARM64':
    make_head(_module, 'PAGESETUPDLGW')
if ARCH in 'X86':
    make_head(_module, 'PAGESETUPDLGW')
if ARCH in 'X64,ARM64':
    make_head(_module, 'PRINTDLGA')
if ARCH in 'X86':
    make_head(_module, 'PRINTDLGA')
if ARCH in 'X64,ARM64':
    make_head(_module, 'PRINTDLGEXA')
if ARCH in 'X86':
    make_head(_module, 'PRINTDLGEXA')
if ARCH in 'X64,ARM64':
    make_head(_module, 'PRINTDLGEXW')
if ARCH in 'X86':
    make_head(_module, 'PRINTDLGEXW')
if ARCH in 'X64,ARM64':
    make_head(_module, 'PRINTDLGW')
if ARCH in 'X86':
    make_head(_module, 'PRINTDLGW')
if ARCH in 'X64,ARM64':
    make_head(_module, 'PRINTPAGERANGE')
if ARCH in 'X86':
    make_head(_module, 'PRINTPAGERANGE')
