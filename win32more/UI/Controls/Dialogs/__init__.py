from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.System.Com
import win32more.UI.Controls
import win32more.UI.Controls.Dialogs
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
OFN_SHAREFALLTHROUGH: UInt32 = 2
OFN_SHARENOWARN: UInt32 = 1
OFN_SHAREWARN: UInt32 = 0
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
def GetOpenFileNameA(param0: POINTER(win32more.UI.Controls.Dialogs.OPENFILENAMEA_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('COMDLG32.dll')
def GetOpenFileNameW(param0: POINTER(win32more.UI.Controls.Dialogs.OPENFILENAMEW_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('COMDLG32.dll')
def GetSaveFileNameA(param0: POINTER(win32more.UI.Controls.Dialogs.OPENFILENAMEA_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('COMDLG32.dll')
def GetSaveFileNameW(param0: POINTER(win32more.UI.Controls.Dialogs.OPENFILENAMEW_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('COMDLG32.dll')
def GetFileTitleA(param0: win32more.Foundation.PSTR, Buf: win32more.Foundation.PSTR, cchSize: UInt16) -> Int16: ...
@winfunctype('COMDLG32.dll')
def GetFileTitleW(param0: win32more.Foundation.PWSTR, Buf: win32more.Foundation.PWSTR, cchSize: UInt16) -> Int16: ...
@winfunctype('COMDLG32.dll')
def ChooseColorA(param0: POINTER(win32more.UI.Controls.Dialogs.CHOOSECOLORA_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('COMDLG32.dll')
def ChooseColorW(param0: POINTER(win32more.UI.Controls.Dialogs.CHOOSECOLORW_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('COMDLG32.dll')
def FindTextA(param0: POINTER(win32more.UI.Controls.Dialogs.FINDREPLACEA_head)) -> win32more.Foundation.HWND: ...
@winfunctype('COMDLG32.dll')
def FindTextW(param0: POINTER(win32more.UI.Controls.Dialogs.FINDREPLACEW_head)) -> win32more.Foundation.HWND: ...
@winfunctype('COMDLG32.dll')
def ReplaceTextA(param0: POINTER(win32more.UI.Controls.Dialogs.FINDREPLACEA_head)) -> win32more.Foundation.HWND: ...
@winfunctype('COMDLG32.dll')
def ReplaceTextW(param0: POINTER(win32more.UI.Controls.Dialogs.FINDREPLACEW_head)) -> win32more.Foundation.HWND: ...
@winfunctype('COMDLG32.dll')
def ChooseFontA(param0: POINTER(win32more.UI.Controls.Dialogs.CHOOSEFONTA_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('COMDLG32.dll')
def ChooseFontW(param0: POINTER(win32more.UI.Controls.Dialogs.CHOOSEFONTW_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('COMDLG32.dll')
def PrintDlgA(pPD: POINTER(win32more.UI.Controls.Dialogs.PRINTDLGA_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('COMDLG32.dll')
def PrintDlgW(pPD: POINTER(win32more.UI.Controls.Dialogs.PRINTDLGW_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('COMDLG32.dll')
def PrintDlgExA(pPD: POINTER(win32more.UI.Controls.Dialogs.PRINTDLGEXA_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('COMDLG32.dll')
def PrintDlgExW(pPD: POINTER(win32more.UI.Controls.Dialogs.PRINTDLGEXW_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype('COMDLG32.dll')
def CommDlgExtendedError() -> win32more.UI.Controls.Dialogs.COMMON_DLG_ERRORS: ...
@winfunctype('COMDLG32.dll')
def PageSetupDlgA(param0: POINTER(win32more.UI.Controls.Dialogs.PAGESETUPDLGA_head)) -> win32more.Foundation.BOOL: ...
@winfunctype('COMDLG32.dll')
def PageSetupDlgW(param0: POINTER(win32more.UI.Controls.Dialogs.PAGESETUPDLGW_head)) -> win32more.Foundation.BOOL: ...
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
class CHOOSECOLORA(Structure):
    lStructSize: UInt32
    hwndOwner: win32more.Foundation.HWND
    hInstance: win32more.Foundation.HWND
    rgbResult: win32more.Foundation.COLORREF
    lpCustColors: POINTER(win32more.Foundation.COLORREF)
    Flags: win32more.UI.Controls.Dialogs.CHOOSECOLOR_FLAGS
    lCustData: win32more.Foundation.LPARAM
    lpfnHook: win32more.UI.Controls.Dialogs.LPCCHOOKPROC
    lpTemplateName: win32more.Foundation.PSTR
class CHOOSECOLORW(Structure):
    lStructSize: UInt32
    hwndOwner: win32more.Foundation.HWND
    hInstance: win32more.Foundation.HWND
    rgbResult: win32more.Foundation.COLORREF
    lpCustColors: POINTER(win32more.Foundation.COLORREF)
    Flags: win32more.UI.Controls.Dialogs.CHOOSECOLOR_FLAGS
    lCustData: win32more.Foundation.LPARAM
    lpfnHook: win32more.UI.Controls.Dialogs.LPCCHOOKPROC
    lpTemplateName: win32more.Foundation.PWSTR
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
class CHOOSEFONTA(Structure):
    lStructSize: UInt32
    hwndOwner: win32more.Foundation.HWND
    hDC: win32more.Graphics.Gdi.HDC
    lpLogFont: POINTER(win32more.Graphics.Gdi.LOGFONTA_head)
    iPointSize: Int32
    Flags: win32more.UI.Controls.Dialogs.CHOOSEFONT_FLAGS
    rgbColors: win32more.Foundation.COLORREF
    lCustData: win32more.Foundation.LPARAM
    lpfnHook: win32more.UI.Controls.Dialogs.LPCFHOOKPROC
    lpTemplateName: win32more.Foundation.PSTR
    hInstance: win32more.Foundation.HINSTANCE
    lpszStyle: win32more.Foundation.PSTR
    nFontType: win32more.UI.Controls.Dialogs.CHOOSEFONT_FONT_TYPE
    ___MISSING_ALIGNMENT__: UInt16
    nSizeMin: Int32
    nSizeMax: Int32
class CHOOSEFONTW(Structure):
    lStructSize: UInt32
    hwndOwner: win32more.Foundation.HWND
    hDC: win32more.Graphics.Gdi.HDC
    lpLogFont: POINTER(win32more.Graphics.Gdi.LOGFONTW_head)
    iPointSize: Int32
    Flags: win32more.UI.Controls.Dialogs.CHOOSEFONT_FLAGS
    rgbColors: win32more.Foundation.COLORREF
    lCustData: win32more.Foundation.LPARAM
    lpfnHook: win32more.UI.Controls.Dialogs.LPCFHOOKPROC
    lpTemplateName: win32more.Foundation.PWSTR
    hInstance: win32more.Foundation.HINSTANCE
    lpszStyle: win32more.Foundation.PWSTR
    nFontType: win32more.UI.Controls.Dialogs.CHOOSEFONT_FONT_TYPE
    ___MISSING_ALIGNMENT__: UInt16
    nSizeMin: Int32
    nSizeMax: Int32
COMMON_DIALOG_NOTIFICATION = Int32
CDN_FIRST: COMMON_DIALOG_NOTIFICATION = -601
CDN_LAST: COMMON_DIALOG_NOTIFICATION = -699
CDN_INITDONE: COMMON_DIALOG_NOTIFICATION = -601
CDN_SELCHANGE: COMMON_DIALOG_NOTIFICATION = -602
CDN_FOLDERCHANGE: COMMON_DIALOG_NOTIFICATION = -603
CDN_SHAREVIOLATION: COMMON_DIALOG_NOTIFICATION = -604
CDN_HELP: COMMON_DIALOG_NOTIFICATION = -605
CDN_FILEOK: COMMON_DIALOG_NOTIFICATION = -606
CDN_TYPECHANGE: COMMON_DIALOG_NOTIFICATION = -607
CDN_INCLUDEITEM: COMMON_DIALOG_NOTIFICATION = -608
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
class DEVNAMES(Structure):
    wDriverOffset: UInt16
    wDeviceOffset: UInt16
    wOutputOffset: UInt16
    wDefault: UInt16
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
class FINDREPLACEA(Structure):
    lStructSize: UInt32
    hwndOwner: win32more.Foundation.HWND
    hInstance: win32more.Foundation.HINSTANCE
    Flags: win32more.UI.Controls.Dialogs.FINDREPLACE_FLAGS
    lpstrFindWhat: win32more.Foundation.PSTR
    lpstrReplaceWith: win32more.Foundation.PSTR
    wFindWhatLen: UInt16
    wReplaceWithLen: UInt16
    lCustData: win32more.Foundation.LPARAM
    lpfnHook: win32more.UI.Controls.Dialogs.LPFRHOOKPROC
    lpTemplateName: win32more.Foundation.PSTR
class FINDREPLACEW(Structure):
    lStructSize: UInt32
    hwndOwner: win32more.Foundation.HWND
    hInstance: win32more.Foundation.HINSTANCE
    Flags: win32more.UI.Controls.Dialogs.FINDREPLACE_FLAGS
    lpstrFindWhat: win32more.Foundation.PWSTR
    lpstrReplaceWith: win32more.Foundation.PWSTR
    wFindWhatLen: UInt16
    wReplaceWithLen: UInt16
    lCustData: win32more.Foundation.LPARAM
    lpfnHook: win32more.UI.Controls.Dialogs.LPFRHOOKPROC
    lpTemplateName: win32more.Foundation.PWSTR
class IPrintDialogCallback(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('5852a2c3-6530-11d1-b6-a3-00-00-f8-75-7b-f9')
    @commethod(3)
    def InitDone() -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SelectionChange() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def HandleMessage(hDlg: win32more.Foundation.HWND, uMsg: UInt32, wParam: win32more.Foundation.WPARAM, lParam: win32more.Foundation.LPARAM, pResult: POINTER(win32more.Foundation.LRESULT)) -> win32more.Foundation.HRESULT: ...
class IPrintDialogServices(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('509aaeda-5639-11d1-b6-a1-00-00-f8-75-7b-f9')
    @commethod(3)
    def GetCurrentDevMode(pDevMode: POINTER(win32more.Graphics.Gdi.DEVMODEA_head), pcbSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentPrinterName(pPrinterName: win32more.Foundation.PWSTR, pcchSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrentPortName(pPortName: win32more.Foundation.PWSTR, pcchSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def LPCCHOOKPROC(param0: win32more.Foundation.HWND, param1: UInt32, param2: win32more.Foundation.WPARAM, param3: win32more.Foundation.LPARAM) -> UIntPtr: ...
@winfunctype_pointer
def LPCFHOOKPROC(param0: win32more.Foundation.HWND, param1: UInt32, param2: win32more.Foundation.WPARAM, param3: win32more.Foundation.LPARAM) -> UIntPtr: ...
@winfunctype_pointer
def LPFRHOOKPROC(param0: win32more.Foundation.HWND, param1: UInt32, param2: win32more.Foundation.WPARAM, param3: win32more.Foundation.LPARAM) -> UIntPtr: ...
@winfunctype_pointer
def LPOFNHOOKPROC(param0: win32more.Foundation.HWND, param1: UInt32, param2: win32more.Foundation.WPARAM, param3: win32more.Foundation.LPARAM) -> UIntPtr: ...
@winfunctype_pointer
def LPPAGEPAINTHOOK(param0: win32more.Foundation.HWND, param1: UInt32, param2: win32more.Foundation.WPARAM, param3: win32more.Foundation.LPARAM) -> UIntPtr: ...
@winfunctype_pointer
def LPPAGESETUPHOOK(param0: win32more.Foundation.HWND, param1: UInt32, param2: win32more.Foundation.WPARAM, param3: win32more.Foundation.LPARAM) -> UIntPtr: ...
@winfunctype_pointer
def LPPRINTHOOKPROC(param0: win32more.Foundation.HWND, param1: UInt32, param2: win32more.Foundation.WPARAM, param3: win32more.Foundation.LPARAM) -> UIntPtr: ...
@winfunctype_pointer
def LPSETUPHOOKPROC(param0: win32more.Foundation.HWND, param1: UInt32, param2: win32more.Foundation.WPARAM, param3: win32more.Foundation.LPARAM) -> UIntPtr: ...
class OFNOTIFYA(Structure):
    hdr: win32more.UI.Controls.NMHDR
    lpOFN: POINTER(win32more.UI.Controls.Dialogs.OPENFILENAMEA_head)
    pszFile: win32more.Foundation.PSTR
class OFNOTIFYEXA(Structure):
    hdr: win32more.UI.Controls.NMHDR
    lpOFN: POINTER(win32more.UI.Controls.Dialogs.OPENFILENAMEA_head)
    psf: c_void_p
    pidl: c_void_p
class OFNOTIFYEXW(Structure):
    hdr: win32more.UI.Controls.NMHDR
    lpOFN: POINTER(win32more.UI.Controls.Dialogs.OPENFILENAMEW_head)
    psf: c_void_p
    pidl: c_void_p
class OFNOTIFYW(Structure):
    hdr: win32more.UI.Controls.NMHDR
    lpOFN: POINTER(win32more.UI.Controls.Dialogs.OPENFILENAMEW_head)
    pszFile: win32more.Foundation.PWSTR
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
class OPENFILENAME_NT4A(Structure):
    lStructSize: UInt32
    hwndOwner: win32more.Foundation.HWND
    hInstance: win32more.Foundation.HINSTANCE
    lpstrFilter: win32more.Foundation.PSTR
    lpstrCustomFilter: win32more.Foundation.PSTR
    nMaxCustFilter: UInt32
    nFilterIndex: UInt32
    lpstrFile: win32more.Foundation.PSTR
    nMaxFile: UInt32
    lpstrFileTitle: win32more.Foundation.PSTR
    nMaxFileTitle: UInt32
    lpstrInitialDir: win32more.Foundation.PSTR
    lpstrTitle: win32more.Foundation.PSTR
    Flags: UInt32
    nFileOffset: UInt16
    nFileExtension: UInt16
    lpstrDefExt: win32more.Foundation.PSTR
    lCustData: win32more.Foundation.LPARAM
    lpfnHook: win32more.UI.Controls.Dialogs.LPOFNHOOKPROC
    lpTemplateName: win32more.Foundation.PSTR
class OPENFILENAME_NT4W(Structure):
    lStructSize: UInt32
    hwndOwner: win32more.Foundation.HWND
    hInstance: win32more.Foundation.HINSTANCE
    lpstrFilter: win32more.Foundation.PWSTR
    lpstrCustomFilter: win32more.Foundation.PWSTR
    nMaxCustFilter: UInt32
    nFilterIndex: UInt32
    lpstrFile: win32more.Foundation.PWSTR
    nMaxFile: UInt32
    lpstrFileTitle: win32more.Foundation.PWSTR
    nMaxFileTitle: UInt32
    lpstrInitialDir: win32more.Foundation.PWSTR
    lpstrTitle: win32more.Foundation.PWSTR
    Flags: UInt32
    nFileOffset: UInt16
    nFileExtension: UInt16
    lpstrDefExt: win32more.Foundation.PWSTR
    lCustData: win32more.Foundation.LPARAM
    lpfnHook: win32more.UI.Controls.Dialogs.LPOFNHOOKPROC
    lpTemplateName: win32more.Foundation.PWSTR
class OPENFILENAMEA(Structure):
    lStructSize: UInt32
    hwndOwner: win32more.Foundation.HWND
    hInstance: win32more.Foundation.HINSTANCE
    lpstrFilter: win32more.Foundation.PSTR
    lpstrCustomFilter: win32more.Foundation.PSTR
    nMaxCustFilter: UInt32
    nFilterIndex: UInt32
    lpstrFile: win32more.Foundation.PSTR
    nMaxFile: UInt32
    lpstrFileTitle: win32more.Foundation.PSTR
    nMaxFileTitle: UInt32
    lpstrInitialDir: win32more.Foundation.PSTR
    lpstrTitle: win32more.Foundation.PSTR
    Flags: win32more.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS
    nFileOffset: UInt16
    nFileExtension: UInt16
    lpstrDefExt: win32more.Foundation.PSTR
    lCustData: win32more.Foundation.LPARAM
    lpfnHook: win32more.UI.Controls.Dialogs.LPOFNHOOKPROC
    lpTemplateName: win32more.Foundation.PSTR
    pvReserved: c_void_p
    dwReserved: UInt32
    FlagsEx: win32more.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS_EX
class OPENFILENAMEW(Structure):
    lStructSize: UInt32
    hwndOwner: win32more.Foundation.HWND
    hInstance: win32more.Foundation.HINSTANCE
    lpstrFilter: win32more.Foundation.PWSTR
    lpstrCustomFilter: win32more.Foundation.PWSTR
    nMaxCustFilter: UInt32
    nFilterIndex: UInt32
    lpstrFile: win32more.Foundation.PWSTR
    nMaxFile: UInt32
    lpstrFileTitle: win32more.Foundation.PWSTR
    nMaxFileTitle: UInt32
    lpstrInitialDir: win32more.Foundation.PWSTR
    lpstrTitle: win32more.Foundation.PWSTR
    Flags: win32more.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS
    nFileOffset: UInt16
    nFileExtension: UInt16
    lpstrDefExt: win32more.Foundation.PWSTR
    lCustData: win32more.Foundation.LPARAM
    lpfnHook: win32more.UI.Controls.Dialogs.LPOFNHOOKPROC
    lpTemplateName: win32more.Foundation.PWSTR
    pvReserved: c_void_p
    dwReserved: UInt32
    FlagsEx: win32more.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS_EX
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
class PAGESETUPDLGA(Structure):
    lStructSize: UInt32
    hwndOwner: win32more.Foundation.HWND
    hDevMode: IntPtr
    hDevNames: IntPtr
    Flags: win32more.UI.Controls.Dialogs.PAGESETUPDLG_FLAGS
    ptPaperSize: win32more.Foundation.POINT
    rtMinMargin: win32more.Foundation.RECT
    rtMargin: win32more.Foundation.RECT
    hInstance: win32more.Foundation.HINSTANCE
    lCustData: win32more.Foundation.LPARAM
    lpfnPageSetupHook: win32more.UI.Controls.Dialogs.LPPAGESETUPHOOK
    lpfnPagePaintHook: win32more.UI.Controls.Dialogs.LPPAGEPAINTHOOK
    lpPageSetupTemplateName: win32more.Foundation.PSTR
    hPageSetupTemplate: IntPtr
class PAGESETUPDLGW(Structure):
    lStructSize: UInt32
    hwndOwner: win32more.Foundation.HWND
    hDevMode: IntPtr
    hDevNames: IntPtr
    Flags: win32more.UI.Controls.Dialogs.PAGESETUPDLG_FLAGS
    ptPaperSize: win32more.Foundation.POINT
    rtMinMargin: win32more.Foundation.RECT
    rtMargin: win32more.Foundation.RECT
    hInstance: win32more.Foundation.HINSTANCE
    lCustData: win32more.Foundation.LPARAM
    lpfnPageSetupHook: win32more.UI.Controls.Dialogs.LPPAGESETUPHOOK
    lpfnPagePaintHook: win32more.UI.Controls.Dialogs.LPPAGEPAINTHOOK
    lpPageSetupTemplateName: win32more.Foundation.PWSTR
    hPageSetupTemplate: IntPtr
class PRINTDLGA(Structure):
    lStructSize: UInt32
    hwndOwner: win32more.Foundation.HWND
    hDevMode: IntPtr
    hDevNames: IntPtr
    hDC: win32more.Graphics.Gdi.HDC
    Flags: win32more.UI.Controls.Dialogs.PRINTDLGEX_FLAGS
    nFromPage: UInt16
    nToPage: UInt16
    nMinPage: UInt16
    nMaxPage: UInt16
    nCopies: UInt16
    hInstance: win32more.Foundation.HINSTANCE
    lCustData: win32more.Foundation.LPARAM
    lpfnPrintHook: win32more.UI.Controls.Dialogs.LPPRINTHOOKPROC
    lpfnSetupHook: win32more.UI.Controls.Dialogs.LPSETUPHOOKPROC
    lpPrintTemplateName: win32more.Foundation.PSTR
    lpSetupTemplateName: win32more.Foundation.PSTR
    hPrintTemplate: IntPtr
    hSetupTemplate: IntPtr
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
class PRINTDLGEXA(Structure):
    lStructSize: UInt32
    hwndOwner: win32more.Foundation.HWND
    hDevMode: IntPtr
    hDevNames: IntPtr
    hDC: win32more.Graphics.Gdi.HDC
    Flags: win32more.UI.Controls.Dialogs.PRINTDLGEX_FLAGS
    Flags2: UInt32
    ExclusionFlags: UInt32
    nPageRanges: UInt32
    nMaxPageRanges: UInt32
    lpPageRanges: POINTER(win32more.UI.Controls.Dialogs.PRINTPAGERANGE_head)
    nMinPage: UInt32
    nMaxPage: UInt32
    nCopies: UInt32
    hInstance: win32more.Foundation.HINSTANCE
    lpPrintTemplateName: win32more.Foundation.PSTR
    lpCallback: win32more.System.Com.IUnknown_head
    nPropertyPages: UInt32
    lphPropertyPages: POINTER(win32more.UI.Controls.HPROPSHEETPAGE)
    nStartPage: UInt32
    dwResultAction: UInt32
class PRINTDLGEXW(Structure):
    lStructSize: UInt32
    hwndOwner: win32more.Foundation.HWND
    hDevMode: IntPtr
    hDevNames: IntPtr
    hDC: win32more.Graphics.Gdi.HDC
    Flags: win32more.UI.Controls.Dialogs.PRINTDLGEX_FLAGS
    Flags2: UInt32
    ExclusionFlags: UInt32
    nPageRanges: UInt32
    nMaxPageRanges: UInt32
    lpPageRanges: POINTER(win32more.UI.Controls.Dialogs.PRINTPAGERANGE_head)
    nMinPage: UInt32
    nMaxPage: UInt32
    nCopies: UInt32
    hInstance: win32more.Foundation.HINSTANCE
    lpPrintTemplateName: win32more.Foundation.PWSTR
    lpCallback: win32more.System.Com.IUnknown_head
    nPropertyPages: UInt32
    lphPropertyPages: POINTER(win32more.UI.Controls.HPROPSHEETPAGE)
    nStartPage: UInt32
    dwResultAction: UInt32
class PRINTDLGW(Structure):
    lStructSize: UInt32
    hwndOwner: win32more.Foundation.HWND
    hDevMode: IntPtr
    hDevNames: IntPtr
    hDC: win32more.Graphics.Gdi.HDC
    Flags: win32more.UI.Controls.Dialogs.PRINTDLGEX_FLAGS
    nFromPage: UInt16
    nToPage: UInt16
    nMinPage: UInt16
    nMaxPage: UInt16
    nCopies: UInt16
    hInstance: win32more.Foundation.HINSTANCE
    lCustData: win32more.Foundation.LPARAM
    lpfnPrintHook: win32more.UI.Controls.Dialogs.LPPRINTHOOKPROC
    lpfnSetupHook: win32more.UI.Controls.Dialogs.LPSETUPHOOKPROC
    lpPrintTemplateName: win32more.Foundation.PWSTR
    lpSetupTemplateName: win32more.Foundation.PWSTR
    hPrintTemplate: IntPtr
    hSetupTemplate: IntPtr
class PRINTPAGERANGE(Structure):
    nFromPage: UInt32
    nToPage: UInt32
make_head(_module, 'CHOOSECOLORA')
make_head(_module, 'CHOOSECOLORW')
make_head(_module, 'CHOOSEFONTA')
make_head(_module, 'CHOOSEFONTW')
make_head(_module, 'DEVNAMES')
make_head(_module, 'FINDREPLACEA')
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
make_head(_module, 'OFNOTIFYA')
make_head(_module, 'OFNOTIFYEXA')
make_head(_module, 'OFNOTIFYEXW')
make_head(_module, 'OFNOTIFYW')
make_head(_module, 'OPENFILENAME_NT4A')
make_head(_module, 'OPENFILENAME_NT4W')
make_head(_module, 'OPENFILENAMEA')
make_head(_module, 'OPENFILENAMEW')
make_head(_module, 'PAGESETUPDLGA')
make_head(_module, 'PAGESETUPDLGW')
make_head(_module, 'PRINTDLGA')
make_head(_module, 'PRINTDLGEXA')
make_head(_module, 'PRINTDLGEXW')
make_head(_module, 'PRINTDLGW')
make_head(_module, 'PRINTPAGERANGE')
__all__ = [
    "BOLD_FONTTYPE",
    "CCERR_CHOOSECOLORCODES",
    "CC_ANYCOLOR",
    "CC_ENABLEHOOK",
    "CC_ENABLETEMPLATE",
    "CC_ENABLETEMPLATEHANDLE",
    "CC_FULLOPEN",
    "CC_PREVENTFULLOPEN",
    "CC_RGBINIT",
    "CC_SHOWHELP",
    "CC_SOLIDCOLOR",
    "CDERR_DIALOGFAILURE",
    "CDERR_FINDRESFAILURE",
    "CDERR_GENERALCODES",
    "CDERR_INITIALIZATION",
    "CDERR_LOADRESFAILURE",
    "CDERR_LOADSTRFAILURE",
    "CDERR_LOCKRESFAILURE",
    "CDERR_MEMALLOCFAILURE",
    "CDERR_MEMLOCKFAILURE",
    "CDERR_NOHINSTANCE",
    "CDERR_NOHOOK",
    "CDERR_NOTEMPLATE",
    "CDERR_REGISTERMSGFAIL",
    "CDERR_STRUCTSIZE",
    "CDM_FIRST",
    "CDM_GETFILEPATH",
    "CDM_GETFOLDERIDLIST",
    "CDM_GETFOLDERPATH",
    "CDM_GETSPEC",
    "CDM_HIDECONTROL",
    "CDM_LAST",
    "CDM_SETCONTROLTEXT",
    "CDM_SETDEFEXT",
    "CDN_FILEOK",
    "CDN_FIRST",
    "CDN_FOLDERCHANGE",
    "CDN_HELP",
    "CDN_INCLUDEITEM",
    "CDN_INITDONE",
    "CDN_LAST",
    "CDN_SELCHANGE",
    "CDN_SHAREVIOLATION",
    "CDN_TYPECHANGE",
    "CD_LBSELADD",
    "CD_LBSELCHANGE",
    "CD_LBSELNOITEMS",
    "CD_LBSELSUB",
    "CFERR_CHOOSEFONTCODES",
    "CFERR_MAXLESSTHANMIN",
    "CFERR_NOFONTS",
    "CF_ANSIONLY",
    "CF_APPLY",
    "CF_BOTH",
    "CF_EFFECTS",
    "CF_ENABLEHOOK",
    "CF_ENABLETEMPLATE",
    "CF_ENABLETEMPLATEHANDLE",
    "CF_FIXEDPITCHONLY",
    "CF_FORCEFONTEXIST",
    "CF_INACTIVEFONTS",
    "CF_INITTOLOGFONTSTRUCT",
    "CF_LIMITSIZE",
    "CF_NOFACESEL",
    "CF_NOOEMFONTS",
    "CF_NOSCRIPTSEL",
    "CF_NOSIMULATIONS",
    "CF_NOSIZESEL",
    "CF_NOSTYLESEL",
    "CF_NOVECTORFONTS",
    "CF_NOVERTFONTS",
    "CF_PRINTERFONTS",
    "CF_SCALABLEONLY",
    "CF_SCREENFONTS",
    "CF_SCRIPTSONLY",
    "CF_SELECTSCRIPT",
    "CF_SHOWHELP",
    "CF_TTONLY",
    "CF_USESTYLE",
    "CF_WYSIWYG",
    "CHOOSECOLORA",
    "CHOOSECOLORW",
    "CHOOSECOLOR_FLAGS",
    "CHOOSEFONTA",
    "CHOOSEFONTW",
    "CHOOSEFONT_FLAGS",
    "CHOOSEFONT_FONT_TYPE",
    "COLOROKSTRING",
    "COLOROKSTRINGA",
    "COLOROKSTRINGW",
    "COLOR_ADD",
    "COLOR_BLUE",
    "COLOR_BLUEACCEL",
    "COLOR_BOX1",
    "COLOR_CURRENT",
    "COLOR_CUSTOM1",
    "COLOR_ELEMENT",
    "COLOR_GREEN",
    "COLOR_GREENACCEL",
    "COLOR_HUE",
    "COLOR_HUEACCEL",
    "COLOR_HUESCROLL",
    "COLOR_LUM",
    "COLOR_LUMACCEL",
    "COLOR_LUMSCROLL",
    "COLOR_MIX",
    "COLOR_PALETTE",
    "COLOR_RAINBOW",
    "COLOR_RED",
    "COLOR_REDACCEL",
    "COLOR_SAMPLES",
    "COLOR_SAT",
    "COLOR_SATACCEL",
    "COLOR_SATSCROLL",
    "COLOR_SAVE",
    "COLOR_SCHEMES",
    "COLOR_SOLID",
    "COLOR_SOLID_LEFT",
    "COLOR_SOLID_RIGHT",
    "COLOR_TUNE",
    "COMMON_DIALOG_NOTIFICATION",
    "COMMON_DLG_ERRORS",
    "ChooseColorA",
    "ChooseColorW",
    "ChooseFontA",
    "ChooseFontW",
    "CommDlgExtendedError",
    "DEVNAMES",
    "DLG_COLOR",
    "DN_DEFAULTPRN",
    "FILEOKSTRING",
    "FILEOKSTRINGA",
    "FILEOKSTRINGW",
    "FINDMSGSTRING",
    "FINDMSGSTRINGA",
    "FINDMSGSTRINGW",
    "FINDREPLACEA",
    "FINDREPLACEW",
    "FINDREPLACE_FLAGS",
    "FNERR_BUFFERTOOSMALL",
    "FNERR_FILENAMECODES",
    "FNERR_INVALIDFILENAME",
    "FNERR_SUBCLASSFAILURE",
    "FRERR_BUFFERLENGTHZERO",
    "FRERR_FINDREPLACECODES",
    "FRM_FIRST",
    "FRM_LAST",
    "FRM_SETOPERATIONRESULT",
    "FRM_SETOPERATIONRESULTTEXT",
    "FR_DIALOGTERM",
    "FR_DOWN",
    "FR_ENABLEHOOK",
    "FR_ENABLETEMPLATE",
    "FR_ENABLETEMPLATEHANDLE",
    "FR_FINDNEXT",
    "FR_HIDEMATCHCASE",
    "FR_HIDEUPDOWN",
    "FR_HIDEWHOLEWORD",
    "FR_MATCHCASE",
    "FR_NOMATCHCASE",
    "FR_NOUPDOWN",
    "FR_NOWHOLEWORD",
    "FR_NOWRAPAROUND",
    "FR_RAW",
    "FR_REPLACE",
    "FR_REPLACEALL",
    "FR_SHOWHELP",
    "FR_SHOWWRAPAROUND",
    "FR_WHOLEWORD",
    "FR_WRAPAROUND",
    "FindTextA",
    "FindTextW",
    "GetFileTitleA",
    "GetFileTitleW",
    "GetOpenFileNameA",
    "GetOpenFileNameW",
    "GetSaveFileNameA",
    "GetSaveFileNameW",
    "HELPMSGSTRING",
    "HELPMSGSTRINGA",
    "HELPMSGSTRINGW",
    "IPrintDialogCallback",
    "IPrintDialogServices",
    "ITALIC_FONTTYPE",
    "LBSELCHSTRING",
    "LBSELCHSTRINGA",
    "LBSELCHSTRINGW",
    "LPCCHOOKPROC",
    "LPCFHOOKPROC",
    "LPFRHOOKPROC",
    "LPOFNHOOKPROC",
    "LPPAGEPAINTHOOK",
    "LPPAGESETUPHOOK",
    "LPPRINTHOOKPROC",
    "LPSETUPHOOKPROC",
    "NUM_BASIC_COLORS",
    "NUM_CUSTOM_COLORS",
    "OFNOTIFYA",
    "OFNOTIFYEXA",
    "OFNOTIFYEXW",
    "OFNOTIFYW",
    "OFN_ALLOWMULTISELECT",
    "OFN_CREATEPROMPT",
    "OFN_DONTADDTORECENT",
    "OFN_ENABLEHOOK",
    "OFN_ENABLEINCLUDENOTIFY",
    "OFN_ENABLESIZING",
    "OFN_ENABLETEMPLATE",
    "OFN_ENABLETEMPLATEHANDLE",
    "OFN_EXPLORER",
    "OFN_EXTENSIONDIFFERENT",
    "OFN_EX_NONE",
    "OFN_EX_NOPLACESBAR",
    "OFN_FILEMUSTEXIST",
    "OFN_FORCESHOWHIDDEN",
    "OFN_HIDEREADONLY",
    "OFN_LONGNAMES",
    "OFN_NOCHANGEDIR",
    "OFN_NODEREFERENCELINKS",
    "OFN_NOLONGNAMES",
    "OFN_NONETWORKBUTTON",
    "OFN_NOREADONLYRETURN",
    "OFN_NOTESTFILECREATE",
    "OFN_NOVALIDATE",
    "OFN_OVERWRITEPROMPT",
    "OFN_PATHMUSTEXIST",
    "OFN_READONLY",
    "OFN_SHAREAWARE",
    "OFN_SHAREFALLTHROUGH",
    "OFN_SHARENOWARN",
    "OFN_SHAREWARN",
    "OFN_SHOWHELP",
    "OPENFILENAMEA",
    "OPENFILENAMEW",
    "OPENFILENAME_NT4A",
    "OPENFILENAME_NT4W",
    "OPEN_FILENAME_FLAGS",
    "OPEN_FILENAME_FLAGS_EX",
    "PAGESETUPDLGA",
    "PAGESETUPDLGW",
    "PAGESETUPDLG_FLAGS",
    "PDERR_CREATEICFAILURE",
    "PDERR_DEFAULTDIFFERENT",
    "PDERR_DNDMMISMATCH",
    "PDERR_GETDEVMODEFAIL",
    "PDERR_INITFAILURE",
    "PDERR_LOADDRVFAILURE",
    "PDERR_NODEFAULTPRN",
    "PDERR_NODEVICES",
    "PDERR_PARSEFAILURE",
    "PDERR_PRINTERCODES",
    "PDERR_PRINTERNOTFOUND",
    "PDERR_RETDEFFAILURE",
    "PDERR_SETUPFAILURE",
    "PD_ALLPAGES",
    "PD_COLLATE",
    "PD_CURRENTPAGE",
    "PD_DISABLEPRINTTOFILE",
    "PD_ENABLEPRINTHOOK",
    "PD_ENABLEPRINTTEMPLATE",
    "PD_ENABLEPRINTTEMPLATEHANDLE",
    "PD_ENABLESETUPHOOK",
    "PD_ENABLESETUPTEMPLATE",
    "PD_ENABLESETUPTEMPLATEHANDLE",
    "PD_EXCLUSIONFLAGS",
    "PD_HIDEPRINTTOFILE",
    "PD_NOCURRENTPAGE",
    "PD_NONETWORKBUTTON",
    "PD_NOPAGENUMS",
    "PD_NOSELECTION",
    "PD_NOWARNING",
    "PD_PAGENUMS",
    "PD_PRINTSETUP",
    "PD_PRINTTOFILE",
    "PD_RESULT_APPLY",
    "PD_RESULT_CANCEL",
    "PD_RESULT_PRINT",
    "PD_RETURNDC",
    "PD_RETURNDEFAULT",
    "PD_RETURNIC",
    "PD_SELECTION",
    "PD_SHOWHELP",
    "PD_USEDEVMODECOPIES",
    "PD_USEDEVMODECOPIESANDCOLLATE",
    "PD_USELARGETEMPLATE",
    "PRINTDLGA",
    "PRINTDLGEXA",
    "PRINTDLGEXW",
    "PRINTDLGEX_FLAGS",
    "PRINTDLGW",
    "PRINTER_FONTTYPE",
    "PRINTPAGERANGE",
    "PSD_DEFAULTMINMARGINS",
    "PSD_DISABLEMARGINS",
    "PSD_DISABLEORIENTATION",
    "PSD_DISABLEPAGEPAINTING",
    "PSD_DISABLEPAPER",
    "PSD_DISABLEPRINTER",
    "PSD_ENABLEPAGEPAINTHOOK",
    "PSD_ENABLEPAGESETUPHOOK",
    "PSD_ENABLEPAGESETUPTEMPLATE",
    "PSD_ENABLEPAGESETUPTEMPLATEHANDLE",
    "PSD_INHUNDREDTHSOFMILLIMETERS",
    "PSD_INTHOUSANDTHSOFINCHES",
    "PSD_INWININIINTLMEASURE",
    "PSD_MARGINS",
    "PSD_MINMARGINS",
    "PSD_NONETWORKBUTTON",
    "PSD_NOWARNING",
    "PSD_RETURNDEFAULT",
    "PSD_SHOWHELP",
    "PS_OPENTYPE_FONTTYPE",
    "PageSetupDlgA",
    "PageSetupDlgW",
    "PrintDlgA",
    "PrintDlgExA",
    "PrintDlgExW",
    "PrintDlgW",
    "REGULAR_FONTTYPE",
    "ReplaceTextA",
    "ReplaceTextW",
    "SCREEN_FONTTYPE",
    "SETRGBSTRING",
    "SETRGBSTRINGA",
    "SETRGBSTRINGW",
    "SHAREVISTRING",
    "SHAREVISTRINGA",
    "SHAREVISTRINGW",
    "SIMULATED_FONTTYPE",
    "START_PAGE_GENERAL",
    "SYMBOL_FONTTYPE",
    "TT_OPENTYPE_FONTTYPE",
    "TYPE1_FONTTYPE",
    "WM_CHOOSEFONT_GETLOGFONT",
    "WM_CHOOSEFONT_SETFLAGS",
    "WM_CHOOSEFONT_SETLOGFONT",
    "WM_PSD_ENVSTAMPRECT",
    "WM_PSD_FULLPAGERECT",
    "WM_PSD_GREEKTEXTRECT",
    "WM_PSD_MARGINRECT",
    "WM_PSD_MINMARGINRECT",
    "WM_PSD_YAFULLPAGERECT",
]
