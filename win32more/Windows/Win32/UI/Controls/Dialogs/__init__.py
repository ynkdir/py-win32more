from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.UI.Controls
import win32more.Windows.Win32.UI.Controls.Dialogs
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
def GetOpenFileNameA(param0: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.OPENFILENAMEA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('COMDLG32.dll')
def GetOpenFileNameW(param0: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.OPENFILENAMEW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
GetOpenFileName = UnicodeAlias('GetOpenFileNameW')
@winfunctype('COMDLG32.dll')
def GetSaveFileNameA(param0: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.OPENFILENAMEA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('COMDLG32.dll')
def GetSaveFileNameW(param0: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.OPENFILENAMEW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
GetSaveFileName = UnicodeAlias('GetSaveFileNameW')
@winfunctype('COMDLG32.dll')
def GetFileTitleA(param0: win32more.Windows.Win32.Foundation.PSTR, Buf: win32more.Windows.Win32.Foundation.PSTR, cchSize: UInt16) -> Int16: ...
@winfunctype('COMDLG32.dll')
def GetFileTitleW(param0: win32more.Windows.Win32.Foundation.PWSTR, Buf: win32more.Windows.Win32.Foundation.PWSTR, cchSize: UInt16) -> Int16: ...
GetFileTitle = UnicodeAlias('GetFileTitleW')
@winfunctype('COMDLG32.dll')
def ChooseColorA(param0: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSECOLORA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('COMDLG32.dll')
def ChooseColorW(param0: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSECOLORW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
ChooseColor = UnicodeAlias('ChooseColorW')
@winfunctype('COMDLG32.dll')
def FindTextA(param0: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACEA)) -> win32more.Windows.Win32.Foundation.HWND: ...
@winfunctype('COMDLG32.dll')
def FindTextW(param0: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACEW)) -> win32more.Windows.Win32.Foundation.HWND: ...
FindText = UnicodeAlias('FindTextW')
@winfunctype('COMDLG32.dll')
def ReplaceTextA(param0: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACEA)) -> win32more.Windows.Win32.Foundation.HWND: ...
@winfunctype('COMDLG32.dll')
def ReplaceTextW(param0: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACEW)) -> win32more.Windows.Win32.Foundation.HWND: ...
ReplaceText = UnicodeAlias('ReplaceTextW')
@winfunctype('COMDLG32.dll')
def ChooseFontA(param0: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONTA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('COMDLG32.dll')
def ChooseFontW(param0: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONTW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
ChooseFont = UnicodeAlias('ChooseFontW')
@winfunctype('COMDLG32.dll')
def PrintDlgA(pPD: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('COMDLG32.dll')
def PrintDlgW(pPD: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
PrintDlg = UnicodeAlias('PrintDlgW')
@winfunctype('COMDLG32.dll')
def PrintDlgExA(pPD: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEXA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('COMDLG32.dll')
def PrintDlgExW(pPD: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEXW)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
PrintDlgEx = UnicodeAlias('PrintDlgExW')
@winfunctype('COMDLG32.dll')
def CommDlgExtendedError() -> win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS: ...
@winfunctype('COMDLG32.dll')
def PageSetupDlgA(param0: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.PAGESETUPDLGA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('COMDLG32.dll')
def PageSetupDlgW(param0: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.PAGESETUPDLGW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
PageSetupDlg = UnicodeAlias('PageSetupDlgW')
if ARCH in 'X64,ARM64':
    class CHOOSECOLORA(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hInstance: win32more.Windows.Win32.Foundation.HWND
        rgbResult: win32more.Windows.Win32.Foundation.COLORREF
        lpCustColors: POINTER(win32more.Windows.Win32.Foundation.COLORREF)
        Flags: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSECOLOR_FLAGS
        lCustData: win32more.Windows.Win32.Foundation.LPARAM
        lpfnHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPCCHOOKPROC
        lpTemplateName: win32more.Windows.Win32.Foundation.PSTR
elif ARCH in 'X86':
    class CHOOSECOLORA(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hInstance: win32more.Windows.Win32.Foundation.HWND
        rgbResult: win32more.Windows.Win32.Foundation.COLORREF
        lpCustColors: POINTER(win32more.Windows.Win32.Foundation.COLORREF)
        Flags: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSECOLOR_FLAGS
        lCustData: win32more.Windows.Win32.Foundation.LPARAM
        lpfnHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPCCHOOKPROC
        lpTemplateName: win32more.Windows.Win32.Foundation.PSTR
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class CHOOSECOLORW(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hInstance: win32more.Windows.Win32.Foundation.HWND
        rgbResult: win32more.Windows.Win32.Foundation.COLORREF
        lpCustColors: POINTER(win32more.Windows.Win32.Foundation.COLORREF)
        Flags: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSECOLOR_FLAGS
        lCustData: win32more.Windows.Win32.Foundation.LPARAM
        lpfnHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPCCHOOKPROC
        lpTemplateName: win32more.Windows.Win32.Foundation.PWSTR
elif ARCH in 'X86':
    class CHOOSECOLORW(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hInstance: win32more.Windows.Win32.Foundation.HWND
        rgbResult: win32more.Windows.Win32.Foundation.COLORREF
        lpCustColors: POINTER(win32more.Windows.Win32.Foundation.COLORREF)
        Flags: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSECOLOR_FLAGS
        lCustData: win32more.Windows.Win32.Foundation.LPARAM
        lpfnHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPCCHOOKPROC
        lpTemplateName: win32more.Windows.Win32.Foundation.PWSTR
        _pack_ = 1
if ARCH in 'X64,ARM64':
    CHOOSECOLOR = UnicodeAlias('CHOOSECOLORW')
elif ARCH in 'X86':
    CHOOSECOLOR = UnicodeAlias('CHOOSECOLORW')
CHOOSECOLOR_FLAGS = UInt32
CC_RGBINIT: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSECOLOR_FLAGS = 1
CC_FULLOPEN: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSECOLOR_FLAGS = 2
CC_PREVENTFULLOPEN: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSECOLOR_FLAGS = 4
CC_SHOWHELP: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSECOLOR_FLAGS = 8
CC_ENABLEHOOK: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSECOLOR_FLAGS = 16
CC_ENABLETEMPLATE: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSECOLOR_FLAGS = 32
CC_ENABLETEMPLATEHANDLE: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSECOLOR_FLAGS = 64
CC_SOLIDCOLOR: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSECOLOR_FLAGS = 128
CC_ANYCOLOR: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSECOLOR_FLAGS = 256
if ARCH in 'X64,ARM64':
    class CHOOSEFONTA(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hDC: win32more.Windows.Win32.Graphics.Gdi.HDC
        lpLogFont: POINTER(win32more.Windows.Win32.Graphics.Gdi.LOGFONTA)
        iPointSize: Int32
        Flags: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS
        rgbColors: win32more.Windows.Win32.Foundation.COLORREF
        lCustData: win32more.Windows.Win32.Foundation.LPARAM
        lpfnHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPCFHOOKPROC
        lpTemplateName: win32more.Windows.Win32.Foundation.PSTR
        hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
        lpszStyle: win32more.Windows.Win32.Foundation.PSTR
        nFontType: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FONT_TYPE
        ___MISSING_ALIGNMENT__: UInt16
        nSizeMin: Int32
        nSizeMax: Int32
elif ARCH in 'X86':
    class CHOOSEFONTA(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hDC: win32more.Windows.Win32.Graphics.Gdi.HDC
        lpLogFont: POINTER(win32more.Windows.Win32.Graphics.Gdi.LOGFONTA)
        iPointSize: Int32
        Flags: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS
        rgbColors: win32more.Windows.Win32.Foundation.COLORREF
        lCustData: win32more.Windows.Win32.Foundation.LPARAM
        lpfnHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPCFHOOKPROC
        lpTemplateName: win32more.Windows.Win32.Foundation.PSTR
        hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
        lpszStyle: win32more.Windows.Win32.Foundation.PSTR
        nFontType: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FONT_TYPE
        ___MISSING_ALIGNMENT__: UInt16
        nSizeMin: Int32
        nSizeMax: Int32
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class CHOOSEFONTW(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hDC: win32more.Windows.Win32.Graphics.Gdi.HDC
        lpLogFont: POINTER(win32more.Windows.Win32.Graphics.Gdi.LOGFONTW)
        iPointSize: Int32
        Flags: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS
        rgbColors: win32more.Windows.Win32.Foundation.COLORREF
        lCustData: win32more.Windows.Win32.Foundation.LPARAM
        lpfnHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPCFHOOKPROC
        lpTemplateName: win32more.Windows.Win32.Foundation.PWSTR
        hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
        lpszStyle: win32more.Windows.Win32.Foundation.PWSTR
        nFontType: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FONT_TYPE
        ___MISSING_ALIGNMENT__: UInt16
        nSizeMin: Int32
        nSizeMax: Int32
elif ARCH in 'X86':
    class CHOOSEFONTW(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hDC: win32more.Windows.Win32.Graphics.Gdi.HDC
        lpLogFont: POINTER(win32more.Windows.Win32.Graphics.Gdi.LOGFONTW)
        iPointSize: Int32
        Flags: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS
        rgbColors: win32more.Windows.Win32.Foundation.COLORREF
        lCustData: win32more.Windows.Win32.Foundation.LPARAM
        lpfnHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPCFHOOKPROC
        lpTemplateName: win32more.Windows.Win32.Foundation.PWSTR
        hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
        lpszStyle: win32more.Windows.Win32.Foundation.PWSTR
        nFontType: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FONT_TYPE
        ___MISSING_ALIGNMENT__: UInt16
        nSizeMin: Int32
        nSizeMax: Int32
        _pack_ = 1
if ARCH in 'X64,ARM64':
    CHOOSEFONT = UnicodeAlias('CHOOSEFONTW')
elif ARCH in 'X86':
    CHOOSEFONT = UnicodeAlias('CHOOSEFONTW')
CHOOSEFONT_FLAGS = UInt32
CF_APPLY: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS = 512
CF_ANSIONLY: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS = 1024
CF_BOTH: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS = 3
CF_EFFECTS: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS = 256
CF_ENABLEHOOK: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS = 8
CF_ENABLETEMPLATE: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS = 16
CF_ENABLETEMPLATEHANDLE: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS = 32
CF_FIXEDPITCHONLY: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS = 16384
CF_FORCEFONTEXIST: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS = 65536
CF_INACTIVEFONTS: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS = 33554432
CF_INITTOLOGFONTSTRUCT: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS = 64
CF_LIMITSIZE: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS = 8192
CF_NOOEMFONTS: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS = 2048
CF_NOFACESEL: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS = 524288
CF_NOSCRIPTSEL: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS = 8388608
CF_NOSIMULATIONS: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS = 4096
CF_NOSIZESEL: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS = 2097152
CF_NOSTYLESEL: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS = 1048576
CF_NOVECTORFONTS: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS = 2048
CF_NOVERTFONTS: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS = 16777216
CF_PRINTERFONTS: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS = 2
CF_SCALABLEONLY: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS = 131072
CF_SCREENFONTS: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS = 1
CF_SCRIPTSONLY: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS = 1024
CF_SELECTSCRIPT: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS = 4194304
CF_SHOWHELP: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS = 4
CF_TTONLY: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS = 262144
CF_USESTYLE: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS = 128
CF_WYSIWYG: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FLAGS = 32768
CHOOSEFONT_FONT_TYPE = UInt16
BOLD_FONTTYPE: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FONT_TYPE = 256
ITALIC_FONTTYPE: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FONT_TYPE = 512
PRINTER_FONTTYPE: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FONT_TYPE = 16384
REGULAR_FONTTYPE: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FONT_TYPE = 1024
SCREEN_FONTTYPE: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FONT_TYPE = 8192
SIMULATED_FONTTYPE: win32more.Windows.Win32.UI.Controls.Dialogs.CHOOSEFONT_FONT_TYPE = 32768
COMMON_DLG_ERRORS = UInt32
CDERR_DIALOGFAILURE: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 65535
CDERR_GENERALCODES: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 0
CDERR_STRUCTSIZE: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 1
CDERR_INITIALIZATION: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 2
CDERR_NOTEMPLATE: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 3
CDERR_NOHINSTANCE: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 4
CDERR_LOADSTRFAILURE: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 5
CDERR_FINDRESFAILURE: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 6
CDERR_LOADRESFAILURE: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 7
CDERR_LOCKRESFAILURE: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 8
CDERR_MEMALLOCFAILURE: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 9
CDERR_MEMLOCKFAILURE: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 10
CDERR_NOHOOK: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 11
CDERR_REGISTERMSGFAIL: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 12
PDERR_PRINTERCODES: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 4096
PDERR_SETUPFAILURE: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 4097
PDERR_PARSEFAILURE: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 4098
PDERR_RETDEFFAILURE: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 4099
PDERR_LOADDRVFAILURE: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 4100
PDERR_GETDEVMODEFAIL: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 4101
PDERR_INITFAILURE: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 4102
PDERR_NODEVICES: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 4103
PDERR_NODEFAULTPRN: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 4104
PDERR_DNDMMISMATCH: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 4105
PDERR_CREATEICFAILURE: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 4106
PDERR_PRINTERNOTFOUND: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 4107
PDERR_DEFAULTDIFFERENT: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 4108
CFERR_CHOOSEFONTCODES: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 8192
CFERR_NOFONTS: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 8193
CFERR_MAXLESSTHANMIN: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 8194
FNERR_FILENAMECODES: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 12288
FNERR_SUBCLASSFAILURE: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 12289
FNERR_INVALIDFILENAME: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 12290
FNERR_BUFFERTOOSMALL: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 12291
FRERR_FINDREPLACECODES: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 16384
FRERR_BUFFERLENGTHZERO: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 16385
CCERR_CHOOSECOLORCODES: win32more.Windows.Win32.UI.Controls.Dialogs.COMMON_DLG_ERRORS = 20480
if ARCH in 'X64,ARM64':
    class DEVNAMES(Structure):
        wDriverOffset: UInt16
        wDeviceOffset: UInt16
        wOutputOffset: UInt16
        wDefault: UInt16
elif ARCH in 'X86':
    class DEVNAMES(Structure):
        wDriverOffset: UInt16
        wDeviceOffset: UInt16
        wOutputOffset: UInt16
        wDefault: UInt16
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class FINDREPLACEA(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
        Flags: win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS
        lpstrFindWhat: win32more.Windows.Win32.Foundation.PSTR
        lpstrReplaceWith: win32more.Windows.Win32.Foundation.PSTR
        wFindWhatLen: UInt16
        wReplaceWithLen: UInt16
        lCustData: win32more.Windows.Win32.Foundation.LPARAM
        lpfnHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPFRHOOKPROC
        lpTemplateName: win32more.Windows.Win32.Foundation.PSTR
elif ARCH in 'X86':
    class FINDREPLACEA(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
        Flags: win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS
        lpstrFindWhat: win32more.Windows.Win32.Foundation.PSTR
        lpstrReplaceWith: win32more.Windows.Win32.Foundation.PSTR
        wFindWhatLen: UInt16
        wReplaceWithLen: UInt16
        lCustData: win32more.Windows.Win32.Foundation.LPARAM
        lpfnHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPFRHOOKPROC
        lpTemplateName: win32more.Windows.Win32.Foundation.PSTR
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class FINDREPLACEW(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
        Flags: win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS
        lpstrFindWhat: win32more.Windows.Win32.Foundation.PWSTR
        lpstrReplaceWith: win32more.Windows.Win32.Foundation.PWSTR
        wFindWhatLen: UInt16
        wReplaceWithLen: UInt16
        lCustData: win32more.Windows.Win32.Foundation.LPARAM
        lpfnHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPFRHOOKPROC
        lpTemplateName: win32more.Windows.Win32.Foundation.PWSTR
elif ARCH in 'X86':
    class FINDREPLACEW(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
        Flags: win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS
        lpstrFindWhat: win32more.Windows.Win32.Foundation.PWSTR
        lpstrReplaceWith: win32more.Windows.Win32.Foundation.PWSTR
        wFindWhatLen: UInt16
        wReplaceWithLen: UInt16
        lCustData: win32more.Windows.Win32.Foundation.LPARAM
        lpfnHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPFRHOOKPROC
        lpTemplateName: win32more.Windows.Win32.Foundation.PWSTR
        _pack_ = 1
if ARCH in 'X64,ARM64':
    FINDREPLACE = UnicodeAlias('FINDREPLACEW')
elif ARCH in 'X86':
    FINDREPLACE = UnicodeAlias('FINDREPLACEW')
FINDREPLACE_FLAGS = UInt32
FR_DOWN: win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS = 1
FR_WHOLEWORD: win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS = 2
FR_MATCHCASE: win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS = 4
FR_FINDNEXT: win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS = 8
FR_REPLACE: win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS = 16
FR_REPLACEALL: win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS = 32
FR_DIALOGTERM: win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS = 64
FR_SHOWHELP: win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS = 128
FR_ENABLEHOOK: win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS = 256
FR_ENABLETEMPLATE: win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS = 512
FR_NOUPDOWN: win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS = 1024
FR_NOMATCHCASE: win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS = 2048
FR_NOWHOLEWORD: win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS = 4096
FR_ENABLETEMPLATEHANDLE: win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS = 8192
FR_HIDEUPDOWN: win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS = 16384
FR_HIDEMATCHCASE: win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS = 32768
FR_HIDEWHOLEWORD: win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS = 65536
FR_RAW: win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS = 131072
FR_SHOWWRAPAROUND: win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS = 262144
FR_NOWRAPAROUND: win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS = 524288
FR_WRAPAROUND: win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS = 1048576
FR_MATCHDIAC: win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS = 536870912
FR_MATCHKASHIDA: win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS = 1073741824
FR_MATCHALEFHAMZA: win32more.Windows.Win32.UI.Controls.Dialogs.FINDREPLACE_FLAGS = 2147483648
class IPrintDialogCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5852a2c3-6530-11d1-b6a3-0000f8757bf9}')
    @commethod(3)
    def InitDone(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SelectionChange(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def HandleMessage(self, hDlg: win32more.Windows.Win32.Foundation.HWND, uMsg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM, pResult: POINTER(win32more.Windows.Win32.Foundation.LRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPrintDialogServices(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{509aaeda-5639-11d1-b6a1-0000f8757bf9}')
    @commethod(3)
    def GetCurrentDevMode(self, pDevMode: POINTER(win32more.Windows.Win32.Graphics.Gdi.DEVMODEA), pcbSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCurrentPrinterName(self, pPrinterName: win32more.Windows.Win32.Foundation.PWSTR, pcchSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrentPortName(self, pPortName: win32more.Windows.Win32.Foundation.PWSTR, pcchSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def LPCCHOOKPROC(param0: win32more.Windows.Win32.Foundation.HWND, param1: UInt32, param2: win32more.Windows.Win32.Foundation.WPARAM, param3: win32more.Windows.Win32.Foundation.LPARAM) -> UIntPtr: ...
@winfunctype_pointer
def LPCFHOOKPROC(param0: win32more.Windows.Win32.Foundation.HWND, param1: UInt32, param2: win32more.Windows.Win32.Foundation.WPARAM, param3: win32more.Windows.Win32.Foundation.LPARAM) -> UIntPtr: ...
@winfunctype_pointer
def LPFRHOOKPROC(param0: win32more.Windows.Win32.Foundation.HWND, param1: UInt32, param2: win32more.Windows.Win32.Foundation.WPARAM, param3: win32more.Windows.Win32.Foundation.LPARAM) -> UIntPtr: ...
@winfunctype_pointer
def LPOFNHOOKPROC(param0: win32more.Windows.Win32.Foundation.HWND, param1: UInt32, param2: win32more.Windows.Win32.Foundation.WPARAM, param3: win32more.Windows.Win32.Foundation.LPARAM) -> UIntPtr: ...
@winfunctype_pointer
def LPPAGEPAINTHOOK(param0: win32more.Windows.Win32.Foundation.HWND, param1: UInt32, param2: win32more.Windows.Win32.Foundation.WPARAM, param3: win32more.Windows.Win32.Foundation.LPARAM) -> UIntPtr: ...
@winfunctype_pointer
def LPPAGESETUPHOOK(param0: win32more.Windows.Win32.Foundation.HWND, param1: UInt32, param2: win32more.Windows.Win32.Foundation.WPARAM, param3: win32more.Windows.Win32.Foundation.LPARAM) -> UIntPtr: ...
@winfunctype_pointer
def LPPRINTHOOKPROC(param0: win32more.Windows.Win32.Foundation.HWND, param1: UInt32, param2: win32more.Windows.Win32.Foundation.WPARAM, param3: win32more.Windows.Win32.Foundation.LPARAM) -> UIntPtr: ...
@winfunctype_pointer
def LPSETUPHOOKPROC(param0: win32more.Windows.Win32.Foundation.HWND, param1: UInt32, param2: win32more.Windows.Win32.Foundation.WPARAM, param3: win32more.Windows.Win32.Foundation.LPARAM) -> UIntPtr: ...
if ARCH in 'X64,ARM64':
    class OFNOTIFYA(Structure):
        hdr: win32more.Windows.Win32.UI.Controls.NMHDR
        lpOFN: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.OPENFILENAMEA)
        pszFile: win32more.Windows.Win32.Foundation.PSTR
elif ARCH in 'X86':
    class OFNOTIFYA(Structure):
        hdr: win32more.Windows.Win32.UI.Controls.NMHDR
        lpOFN: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.OPENFILENAMEA)
        pszFile: win32more.Windows.Win32.Foundation.PSTR
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class OFNOTIFYEXA(Structure):
        hdr: win32more.Windows.Win32.UI.Controls.NMHDR
        lpOFN: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.OPENFILENAMEA)
        psf: VoidPtr
        pidl: VoidPtr
elif ARCH in 'X86':
    class OFNOTIFYEXA(Structure):
        hdr: win32more.Windows.Win32.UI.Controls.NMHDR
        lpOFN: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.OPENFILENAMEA)
        psf: VoidPtr
        pidl: VoidPtr
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class OFNOTIFYEXW(Structure):
        hdr: win32more.Windows.Win32.UI.Controls.NMHDR
        lpOFN: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.OPENFILENAMEW)
        psf: VoidPtr
        pidl: VoidPtr
elif ARCH in 'X86':
    class OFNOTIFYEXW(Structure):
        hdr: win32more.Windows.Win32.UI.Controls.NMHDR
        lpOFN: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.OPENFILENAMEW)
        psf: VoidPtr
        pidl: VoidPtr
        _pack_ = 1
if ARCH in 'X64,ARM64':
    OFNOTIFYEX = UnicodeAlias('OFNOTIFYEXW')
elif ARCH in 'X86':
    OFNOTIFYEX = UnicodeAlias('OFNOTIFYEXW')
if ARCH in 'X64,ARM64':
    class OFNOTIFYW(Structure):
        hdr: win32more.Windows.Win32.UI.Controls.NMHDR
        lpOFN: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.OPENFILENAMEW)
        pszFile: win32more.Windows.Win32.Foundation.PWSTR
elif ARCH in 'X86':
    class OFNOTIFYW(Structure):
        hdr: win32more.Windows.Win32.UI.Controls.NMHDR
        lpOFN: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.OPENFILENAMEW)
        pszFile: win32more.Windows.Win32.Foundation.PWSTR
        _pack_ = 1
if ARCH in 'X64,ARM64':
    OFNOTIFY = UnicodeAlias('OFNOTIFYW')
elif ARCH in 'X86':
    OFNOTIFY = UnicodeAlias('OFNOTIFYW')
if ARCH in 'X64,ARM64':
    class OPENFILENAMEA(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
        lpstrFilter: win32more.Windows.Win32.Foundation.PSTR
        lpstrCustomFilter: win32more.Windows.Win32.Foundation.PSTR
        nMaxCustFilter: UInt32
        nFilterIndex: UInt32
        lpstrFile: win32more.Windows.Win32.Foundation.PSTR
        nMaxFile: UInt32
        lpstrFileTitle: win32more.Windows.Win32.Foundation.PSTR
        nMaxFileTitle: UInt32
        lpstrInitialDir: win32more.Windows.Win32.Foundation.PSTR
        lpstrTitle: win32more.Windows.Win32.Foundation.PSTR
        Flags: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS
        nFileOffset: UInt16
        nFileExtension: UInt16
        lpstrDefExt: win32more.Windows.Win32.Foundation.PSTR
        lCustData: win32more.Windows.Win32.Foundation.LPARAM
        lpfnHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPOFNHOOKPROC
        lpTemplateName: win32more.Windows.Win32.Foundation.PSTR
        pvReserved: VoidPtr
        dwReserved: UInt32
        FlagsEx: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS_EX
elif ARCH in 'X86':
    class OPENFILENAMEA(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
        lpstrFilter: win32more.Windows.Win32.Foundation.PSTR
        lpstrCustomFilter: win32more.Windows.Win32.Foundation.PSTR
        nMaxCustFilter: UInt32
        nFilterIndex: UInt32
        lpstrFile: win32more.Windows.Win32.Foundation.PSTR
        nMaxFile: UInt32
        lpstrFileTitle: win32more.Windows.Win32.Foundation.PSTR
        nMaxFileTitle: UInt32
        lpstrInitialDir: win32more.Windows.Win32.Foundation.PSTR
        lpstrTitle: win32more.Windows.Win32.Foundation.PSTR
        Flags: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS
        nFileOffset: UInt16
        nFileExtension: UInt16
        lpstrDefExt: win32more.Windows.Win32.Foundation.PSTR
        lCustData: win32more.Windows.Win32.Foundation.LPARAM
        lpfnHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPOFNHOOKPROC
        lpTemplateName: win32more.Windows.Win32.Foundation.PSTR
        pvReserved: VoidPtr
        dwReserved: UInt32
        FlagsEx: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS_EX
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class OPENFILENAMEW(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
        lpstrFilter: win32more.Windows.Win32.Foundation.PWSTR
        lpstrCustomFilter: win32more.Windows.Win32.Foundation.PWSTR
        nMaxCustFilter: UInt32
        nFilterIndex: UInt32
        lpstrFile: win32more.Windows.Win32.Foundation.PWSTR
        nMaxFile: UInt32
        lpstrFileTitle: win32more.Windows.Win32.Foundation.PWSTR
        nMaxFileTitle: UInt32
        lpstrInitialDir: win32more.Windows.Win32.Foundation.PWSTR
        lpstrTitle: win32more.Windows.Win32.Foundation.PWSTR
        Flags: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS
        nFileOffset: UInt16
        nFileExtension: UInt16
        lpstrDefExt: win32more.Windows.Win32.Foundation.PWSTR
        lCustData: win32more.Windows.Win32.Foundation.LPARAM
        lpfnHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPOFNHOOKPROC
        lpTemplateName: win32more.Windows.Win32.Foundation.PWSTR
        pvReserved: VoidPtr
        dwReserved: UInt32
        FlagsEx: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS_EX
elif ARCH in 'X86':
    class OPENFILENAMEW(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
        lpstrFilter: win32more.Windows.Win32.Foundation.PWSTR
        lpstrCustomFilter: win32more.Windows.Win32.Foundation.PWSTR
        nMaxCustFilter: UInt32
        nFilterIndex: UInt32
        lpstrFile: win32more.Windows.Win32.Foundation.PWSTR
        nMaxFile: UInt32
        lpstrFileTitle: win32more.Windows.Win32.Foundation.PWSTR
        nMaxFileTitle: UInt32
        lpstrInitialDir: win32more.Windows.Win32.Foundation.PWSTR
        lpstrTitle: win32more.Windows.Win32.Foundation.PWSTR
        Flags: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS
        nFileOffset: UInt16
        nFileExtension: UInt16
        lpstrDefExt: win32more.Windows.Win32.Foundation.PWSTR
        lCustData: win32more.Windows.Win32.Foundation.LPARAM
        lpfnHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPOFNHOOKPROC
        lpTemplateName: win32more.Windows.Win32.Foundation.PWSTR
        pvReserved: VoidPtr
        dwReserved: UInt32
        FlagsEx: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS_EX
        _pack_ = 1
if ARCH in 'X64,ARM64':
    OPENFILENAME = UnicodeAlias('OPENFILENAMEW')
elif ARCH in 'X86':
    OPENFILENAME = UnicodeAlias('OPENFILENAMEW')
if ARCH in 'X64,ARM64':
    class OPENFILENAME_NT4A(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
        lpstrFilter: win32more.Windows.Win32.Foundation.PSTR
        lpstrCustomFilter: win32more.Windows.Win32.Foundation.PSTR
        nMaxCustFilter: UInt32
        nFilterIndex: UInt32
        lpstrFile: win32more.Windows.Win32.Foundation.PSTR
        nMaxFile: UInt32
        lpstrFileTitle: win32more.Windows.Win32.Foundation.PSTR
        nMaxFileTitle: UInt32
        lpstrInitialDir: win32more.Windows.Win32.Foundation.PSTR
        lpstrTitle: win32more.Windows.Win32.Foundation.PSTR
        Flags: UInt32
        nFileOffset: UInt16
        nFileExtension: UInt16
        lpstrDefExt: win32more.Windows.Win32.Foundation.PSTR
        lCustData: win32more.Windows.Win32.Foundation.LPARAM
        lpfnHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPOFNHOOKPROC
        lpTemplateName: win32more.Windows.Win32.Foundation.PSTR
elif ARCH in 'X86':
    class OPENFILENAME_NT4A(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
        lpstrFilter: win32more.Windows.Win32.Foundation.PSTR
        lpstrCustomFilter: win32more.Windows.Win32.Foundation.PSTR
        nMaxCustFilter: UInt32
        nFilterIndex: UInt32
        lpstrFile: win32more.Windows.Win32.Foundation.PSTR
        nMaxFile: UInt32
        lpstrFileTitle: win32more.Windows.Win32.Foundation.PSTR
        nMaxFileTitle: UInt32
        lpstrInitialDir: win32more.Windows.Win32.Foundation.PSTR
        lpstrTitle: win32more.Windows.Win32.Foundation.PSTR
        Flags: UInt32
        nFileOffset: UInt16
        nFileExtension: UInt16
        lpstrDefExt: win32more.Windows.Win32.Foundation.PSTR
        lCustData: win32more.Windows.Win32.Foundation.LPARAM
        lpfnHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPOFNHOOKPROC
        lpTemplateName: win32more.Windows.Win32.Foundation.PSTR
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class OPENFILENAME_NT4W(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
        lpstrFilter: win32more.Windows.Win32.Foundation.PWSTR
        lpstrCustomFilter: win32more.Windows.Win32.Foundation.PWSTR
        nMaxCustFilter: UInt32
        nFilterIndex: UInt32
        lpstrFile: win32more.Windows.Win32.Foundation.PWSTR
        nMaxFile: UInt32
        lpstrFileTitle: win32more.Windows.Win32.Foundation.PWSTR
        nMaxFileTitle: UInt32
        lpstrInitialDir: win32more.Windows.Win32.Foundation.PWSTR
        lpstrTitle: win32more.Windows.Win32.Foundation.PWSTR
        Flags: UInt32
        nFileOffset: UInt16
        nFileExtension: UInt16
        lpstrDefExt: win32more.Windows.Win32.Foundation.PWSTR
        lCustData: win32more.Windows.Win32.Foundation.LPARAM
        lpfnHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPOFNHOOKPROC
        lpTemplateName: win32more.Windows.Win32.Foundation.PWSTR
elif ARCH in 'X86':
    class OPENFILENAME_NT4W(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
        lpstrFilter: win32more.Windows.Win32.Foundation.PWSTR
        lpstrCustomFilter: win32more.Windows.Win32.Foundation.PWSTR
        nMaxCustFilter: UInt32
        nFilterIndex: UInt32
        lpstrFile: win32more.Windows.Win32.Foundation.PWSTR
        nMaxFile: UInt32
        lpstrFileTitle: win32more.Windows.Win32.Foundation.PWSTR
        nMaxFileTitle: UInt32
        lpstrInitialDir: win32more.Windows.Win32.Foundation.PWSTR
        lpstrTitle: win32more.Windows.Win32.Foundation.PWSTR
        Flags: UInt32
        nFileOffset: UInt16
        nFileExtension: UInt16
        lpstrDefExt: win32more.Windows.Win32.Foundation.PWSTR
        lCustData: win32more.Windows.Win32.Foundation.LPARAM
        lpfnHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPOFNHOOKPROC
        lpTemplateName: win32more.Windows.Win32.Foundation.PWSTR
        _pack_ = 1
if ARCH in 'X64,ARM64':
    OPENFILENAME_NT4 = UnicodeAlias('OPENFILENAME_NT4W')
elif ARCH in 'X86':
    OPENFILENAME_NT4 = UnicodeAlias('OPENFILENAME_NT4W')
OPEN_FILENAME_FLAGS = UInt32
OFN_READONLY: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS = 1
OFN_OVERWRITEPROMPT: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS = 2
OFN_HIDEREADONLY: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS = 4
OFN_NOCHANGEDIR: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS = 8
OFN_SHOWHELP: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS = 16
OFN_ENABLEHOOK: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS = 32
OFN_ENABLETEMPLATE: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS = 64
OFN_ENABLETEMPLATEHANDLE: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS = 128
OFN_NOVALIDATE: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS = 256
OFN_ALLOWMULTISELECT: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS = 512
OFN_EXTENSIONDIFFERENT: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS = 1024
OFN_PATHMUSTEXIST: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS = 2048
OFN_FILEMUSTEXIST: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS = 4096
OFN_CREATEPROMPT: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS = 8192
OFN_SHAREAWARE: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS = 16384
OFN_NOREADONLYRETURN: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS = 32768
OFN_NOTESTFILECREATE: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS = 65536
OFN_NONETWORKBUTTON: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS = 131072
OFN_NOLONGNAMES: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS = 262144
OFN_EXPLORER: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS = 524288
OFN_NODEREFERENCELINKS: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS = 1048576
OFN_LONGNAMES: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS = 2097152
OFN_ENABLEINCLUDENOTIFY: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS = 4194304
OFN_ENABLESIZING: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS = 8388608
OFN_DONTADDTORECENT: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS = 33554432
OFN_FORCESHOWHIDDEN: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS = 268435456
OPEN_FILENAME_FLAGS_EX = UInt32
OFN_EX_NONE: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS_EX = 0
OFN_EX_NOPLACESBAR: win32more.Windows.Win32.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS_EX = 1
if ARCH in 'X64,ARM64':
    class PAGESETUPDLGA(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hDevMode: win32more.Windows.Win32.Foundation.HGLOBAL
        hDevNames: win32more.Windows.Win32.Foundation.HGLOBAL
        Flags: win32more.Windows.Win32.UI.Controls.Dialogs.PAGESETUPDLG_FLAGS
        ptPaperSize: win32more.Windows.Win32.Foundation.POINT
        rtMinMargin: win32more.Windows.Win32.Foundation.RECT
        rtMargin: win32more.Windows.Win32.Foundation.RECT
        hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
        lCustData: win32more.Windows.Win32.Foundation.LPARAM
        lpfnPageSetupHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPPAGESETUPHOOK
        lpfnPagePaintHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPPAGEPAINTHOOK
        lpPageSetupTemplateName: win32more.Windows.Win32.Foundation.PSTR
        hPageSetupTemplate: win32more.Windows.Win32.Foundation.HGLOBAL
elif ARCH in 'X86':
    class PAGESETUPDLGA(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hDevMode: win32more.Windows.Win32.Foundation.HGLOBAL
        hDevNames: win32more.Windows.Win32.Foundation.HGLOBAL
        Flags: win32more.Windows.Win32.UI.Controls.Dialogs.PAGESETUPDLG_FLAGS
        ptPaperSize: win32more.Windows.Win32.Foundation.POINT
        rtMinMargin: win32more.Windows.Win32.Foundation.RECT
        rtMargin: win32more.Windows.Win32.Foundation.RECT
        hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
        lCustData: win32more.Windows.Win32.Foundation.LPARAM
        lpfnPageSetupHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPPAGESETUPHOOK
        lpfnPagePaintHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPPAGEPAINTHOOK
        lpPageSetupTemplateName: win32more.Windows.Win32.Foundation.PSTR
        hPageSetupTemplate: win32more.Windows.Win32.Foundation.HGLOBAL
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class PAGESETUPDLGW(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hDevMode: win32more.Windows.Win32.Foundation.HGLOBAL
        hDevNames: win32more.Windows.Win32.Foundation.HGLOBAL
        Flags: win32more.Windows.Win32.UI.Controls.Dialogs.PAGESETUPDLG_FLAGS
        ptPaperSize: win32more.Windows.Win32.Foundation.POINT
        rtMinMargin: win32more.Windows.Win32.Foundation.RECT
        rtMargin: win32more.Windows.Win32.Foundation.RECT
        hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
        lCustData: win32more.Windows.Win32.Foundation.LPARAM
        lpfnPageSetupHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPPAGESETUPHOOK
        lpfnPagePaintHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPPAGEPAINTHOOK
        lpPageSetupTemplateName: win32more.Windows.Win32.Foundation.PWSTR
        hPageSetupTemplate: win32more.Windows.Win32.Foundation.HGLOBAL
elif ARCH in 'X86':
    class PAGESETUPDLGW(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hDevMode: win32more.Windows.Win32.Foundation.HGLOBAL
        hDevNames: win32more.Windows.Win32.Foundation.HGLOBAL
        Flags: win32more.Windows.Win32.UI.Controls.Dialogs.PAGESETUPDLG_FLAGS
        ptPaperSize: win32more.Windows.Win32.Foundation.POINT
        rtMinMargin: win32more.Windows.Win32.Foundation.RECT
        rtMargin: win32more.Windows.Win32.Foundation.RECT
        hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
        lCustData: win32more.Windows.Win32.Foundation.LPARAM
        lpfnPageSetupHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPPAGESETUPHOOK
        lpfnPagePaintHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPPAGEPAINTHOOK
        lpPageSetupTemplateName: win32more.Windows.Win32.Foundation.PWSTR
        hPageSetupTemplate: win32more.Windows.Win32.Foundation.HGLOBAL
        _pack_ = 1
if ARCH in 'X64,ARM64':
    PAGESETUPDLG = UnicodeAlias('PAGESETUPDLGW')
elif ARCH in 'X86':
    PAGESETUPDLG = UnicodeAlias('PAGESETUPDLGW')
PAGESETUPDLG_FLAGS = UInt32
PSD_DEFAULTMINMARGINS: win32more.Windows.Win32.UI.Controls.Dialogs.PAGESETUPDLG_FLAGS = 0
PSD_DISABLEMARGINS: win32more.Windows.Win32.UI.Controls.Dialogs.PAGESETUPDLG_FLAGS = 16
PSD_DISABLEORIENTATION: win32more.Windows.Win32.UI.Controls.Dialogs.PAGESETUPDLG_FLAGS = 256
PSD_DISABLEPAGEPAINTING: win32more.Windows.Win32.UI.Controls.Dialogs.PAGESETUPDLG_FLAGS = 524288
PSD_DISABLEPAPER: win32more.Windows.Win32.UI.Controls.Dialogs.PAGESETUPDLG_FLAGS = 512
PSD_DISABLEPRINTER: win32more.Windows.Win32.UI.Controls.Dialogs.PAGESETUPDLG_FLAGS = 32
PSD_ENABLEPAGEPAINTHOOK: win32more.Windows.Win32.UI.Controls.Dialogs.PAGESETUPDLG_FLAGS = 262144
PSD_ENABLEPAGESETUPHOOK: win32more.Windows.Win32.UI.Controls.Dialogs.PAGESETUPDLG_FLAGS = 8192
PSD_ENABLEPAGESETUPTEMPLATE: win32more.Windows.Win32.UI.Controls.Dialogs.PAGESETUPDLG_FLAGS = 32768
PSD_ENABLEPAGESETUPTEMPLATEHANDLE: win32more.Windows.Win32.UI.Controls.Dialogs.PAGESETUPDLG_FLAGS = 131072
PSD_INHUNDREDTHSOFMILLIMETERS: win32more.Windows.Win32.UI.Controls.Dialogs.PAGESETUPDLG_FLAGS = 8
PSD_INTHOUSANDTHSOFINCHES: win32more.Windows.Win32.UI.Controls.Dialogs.PAGESETUPDLG_FLAGS = 4
PSD_INWININIINTLMEASURE: win32more.Windows.Win32.UI.Controls.Dialogs.PAGESETUPDLG_FLAGS = 0
PSD_MARGINS: win32more.Windows.Win32.UI.Controls.Dialogs.PAGESETUPDLG_FLAGS = 2
PSD_MINMARGINS: win32more.Windows.Win32.UI.Controls.Dialogs.PAGESETUPDLG_FLAGS = 1
PSD_NONETWORKBUTTON: win32more.Windows.Win32.UI.Controls.Dialogs.PAGESETUPDLG_FLAGS = 2097152
PSD_NOWARNING: win32more.Windows.Win32.UI.Controls.Dialogs.PAGESETUPDLG_FLAGS = 128
PSD_RETURNDEFAULT: win32more.Windows.Win32.UI.Controls.Dialogs.PAGESETUPDLG_FLAGS = 1024
PSD_SHOWHELP: win32more.Windows.Win32.UI.Controls.Dialogs.PAGESETUPDLG_FLAGS = 2048
if ARCH in 'X64,ARM64':
    class PRINTDLGA(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hDevMode: win32more.Windows.Win32.Foundation.HGLOBAL
        hDevNames: win32more.Windows.Win32.Foundation.HGLOBAL
        hDC: win32more.Windows.Win32.Graphics.Gdi.HDC
        Flags: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS
        nFromPage: UInt16
        nToPage: UInt16
        nMinPage: UInt16
        nMaxPage: UInt16
        nCopies: UInt16
        hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
        lCustData: win32more.Windows.Win32.Foundation.LPARAM
        lpfnPrintHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPPRINTHOOKPROC
        lpfnSetupHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPSETUPHOOKPROC
        lpPrintTemplateName: win32more.Windows.Win32.Foundation.PSTR
        lpSetupTemplateName: win32more.Windows.Win32.Foundation.PSTR
        hPrintTemplate: win32more.Windows.Win32.Foundation.HGLOBAL
        hSetupTemplate: win32more.Windows.Win32.Foundation.HGLOBAL
elif ARCH in 'X86':
    class PRINTDLGA(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hDevMode: win32more.Windows.Win32.Foundation.HGLOBAL
        hDevNames: win32more.Windows.Win32.Foundation.HGLOBAL
        hDC: win32more.Windows.Win32.Graphics.Gdi.HDC
        Flags: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS
        nFromPage: UInt16
        nToPage: UInt16
        nMinPage: UInt16
        nMaxPage: UInt16
        nCopies: UInt16
        hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
        lCustData: win32more.Windows.Win32.Foundation.LPARAM
        lpfnPrintHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPPRINTHOOKPROC
        lpfnSetupHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPSETUPHOOKPROC
        lpPrintTemplateName: win32more.Windows.Win32.Foundation.PSTR
        lpSetupTemplateName: win32more.Windows.Win32.Foundation.PSTR
        hPrintTemplate: win32more.Windows.Win32.Foundation.HGLOBAL
        hSetupTemplate: win32more.Windows.Win32.Foundation.HGLOBAL
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class PRINTDLGEXA(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hDevMode: win32more.Windows.Win32.Foundation.HGLOBAL
        hDevNames: win32more.Windows.Win32.Foundation.HGLOBAL
        hDC: win32more.Windows.Win32.Graphics.Gdi.HDC
        Flags: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS
        Flags2: UInt32
        ExclusionFlags: UInt32
        nPageRanges: UInt32
        nMaxPageRanges: UInt32
        lpPageRanges: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.PRINTPAGERANGE)
        nMinPage: UInt32
        nMaxPage: UInt32
        nCopies: UInt32
        hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
        lpPrintTemplateName: win32more.Windows.Win32.Foundation.PSTR
        lpCallback: win32more.Windows.Win32.System.Com.IUnknown
        nPropertyPages: UInt32
        lphPropertyPages: POINTER(win32more.Windows.Win32.UI.Controls.HPROPSHEETPAGE)
        nStartPage: UInt32
        dwResultAction: UInt32
elif ARCH in 'X86':
    class PRINTDLGEXA(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hDevMode: win32more.Windows.Win32.Foundation.HGLOBAL
        hDevNames: win32more.Windows.Win32.Foundation.HGLOBAL
        hDC: win32more.Windows.Win32.Graphics.Gdi.HDC
        Flags: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS
        Flags2: UInt32
        ExclusionFlags: UInt32
        nPageRanges: UInt32
        nMaxPageRanges: UInt32
        lpPageRanges: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.PRINTPAGERANGE)
        nMinPage: UInt32
        nMaxPage: UInt32
        nCopies: UInt32
        hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
        lpPrintTemplateName: win32more.Windows.Win32.Foundation.PSTR
        lpCallback: win32more.Windows.Win32.System.Com.IUnknown
        nPropertyPages: UInt32
        lphPropertyPages: POINTER(win32more.Windows.Win32.UI.Controls.HPROPSHEETPAGE)
        nStartPage: UInt32
        dwResultAction: UInt32
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class PRINTDLGEXW(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hDevMode: win32more.Windows.Win32.Foundation.HGLOBAL
        hDevNames: win32more.Windows.Win32.Foundation.HGLOBAL
        hDC: win32more.Windows.Win32.Graphics.Gdi.HDC
        Flags: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS
        Flags2: UInt32
        ExclusionFlags: UInt32
        nPageRanges: UInt32
        nMaxPageRanges: UInt32
        lpPageRanges: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.PRINTPAGERANGE)
        nMinPage: UInt32
        nMaxPage: UInt32
        nCopies: UInt32
        hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
        lpPrintTemplateName: win32more.Windows.Win32.Foundation.PWSTR
        lpCallback: win32more.Windows.Win32.System.Com.IUnknown
        nPropertyPages: UInt32
        lphPropertyPages: POINTER(win32more.Windows.Win32.UI.Controls.HPROPSHEETPAGE)
        nStartPage: UInt32
        dwResultAction: UInt32
elif ARCH in 'X86':
    class PRINTDLGEXW(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hDevMode: win32more.Windows.Win32.Foundation.HGLOBAL
        hDevNames: win32more.Windows.Win32.Foundation.HGLOBAL
        hDC: win32more.Windows.Win32.Graphics.Gdi.HDC
        Flags: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS
        Flags2: UInt32
        ExclusionFlags: UInt32
        nPageRanges: UInt32
        nMaxPageRanges: UInt32
        lpPageRanges: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.PRINTPAGERANGE)
        nMinPage: UInt32
        nMaxPage: UInt32
        nCopies: UInt32
        hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
        lpPrintTemplateName: win32more.Windows.Win32.Foundation.PWSTR
        lpCallback: win32more.Windows.Win32.System.Com.IUnknown
        nPropertyPages: UInt32
        lphPropertyPages: POINTER(win32more.Windows.Win32.UI.Controls.HPROPSHEETPAGE)
        nStartPage: UInt32
        dwResultAction: UInt32
        _pack_ = 1
if ARCH in 'X64,ARM64':
    PRINTDLGEX = UnicodeAlias('PRINTDLGEXW')
elif ARCH in 'X86':
    PRINTDLGEX = UnicodeAlias('PRINTDLGEXW')
PRINTDLGEX_FLAGS = UInt32
PD_ALLPAGES: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS = 0
PD_COLLATE: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS = 16
PD_CURRENTPAGE: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS = 4194304
PD_DISABLEPRINTTOFILE: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS = 524288
PD_ENABLEPRINTTEMPLATE: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS = 16384
PD_ENABLEPRINTTEMPLATEHANDLE: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS = 65536
PD_EXCLUSIONFLAGS: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS = 16777216
PD_HIDEPRINTTOFILE: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS = 1048576
PD_NOCURRENTPAGE: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS = 8388608
PD_NOPAGENUMS: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS = 8
PD_NOSELECTION: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS = 4
PD_NOWARNING: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS = 128
PD_PAGENUMS: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS = 2
PD_PRINTTOFILE: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS = 32
PD_RETURNDC: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS = 256
PD_RETURNDEFAULT: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS = 1024
PD_RETURNIC: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS = 512
PD_SELECTION: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS = 1
PD_USEDEVMODECOPIES: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS = 262144
PD_USEDEVMODECOPIESANDCOLLATE: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS = 262144
PD_USELARGETEMPLATE: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS = 268435456
PD_ENABLEPRINTHOOK: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS = 4096
PD_ENABLESETUPHOOK: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS = 8192
PD_ENABLESETUPTEMPLATE: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS = 32768
PD_ENABLESETUPTEMPLATEHANDLE: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS = 131072
PD_NONETWORKBUTTON: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS = 2097152
PD_PRINTSETUP: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS = 64
PD_SHOWHELP: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS = 2048
if ARCH in 'X64,ARM64':
    class PRINTDLGW(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hDevMode: win32more.Windows.Win32.Foundation.HGLOBAL
        hDevNames: win32more.Windows.Win32.Foundation.HGLOBAL
        hDC: win32more.Windows.Win32.Graphics.Gdi.HDC
        Flags: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS
        nFromPage: UInt16
        nToPage: UInt16
        nMinPage: UInt16
        nMaxPage: UInt16
        nCopies: UInt16
        hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
        lCustData: win32more.Windows.Win32.Foundation.LPARAM
        lpfnPrintHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPPRINTHOOKPROC
        lpfnSetupHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPSETUPHOOKPROC
        lpPrintTemplateName: win32more.Windows.Win32.Foundation.PWSTR
        lpSetupTemplateName: win32more.Windows.Win32.Foundation.PWSTR
        hPrintTemplate: win32more.Windows.Win32.Foundation.HGLOBAL
        hSetupTemplate: win32more.Windows.Win32.Foundation.HGLOBAL
elif ARCH in 'X86':
    class PRINTDLGW(Structure):
        lStructSize: UInt32
        hwndOwner: win32more.Windows.Win32.Foundation.HWND
        hDevMode: win32more.Windows.Win32.Foundation.HGLOBAL
        hDevNames: win32more.Windows.Win32.Foundation.HGLOBAL
        hDC: win32more.Windows.Win32.Graphics.Gdi.HDC
        Flags: win32more.Windows.Win32.UI.Controls.Dialogs.PRINTDLGEX_FLAGS
        nFromPage: UInt16
        nToPage: UInt16
        nMinPage: UInt16
        nMaxPage: UInt16
        nCopies: UInt16
        hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
        lCustData: win32more.Windows.Win32.Foundation.LPARAM
        lpfnPrintHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPPRINTHOOKPROC
        lpfnSetupHook: win32more.Windows.Win32.UI.Controls.Dialogs.LPSETUPHOOKPROC
        lpPrintTemplateName: win32more.Windows.Win32.Foundation.PWSTR
        lpSetupTemplateName: win32more.Windows.Win32.Foundation.PWSTR
        hPrintTemplate: win32more.Windows.Win32.Foundation.HGLOBAL
        hSetupTemplate: win32more.Windows.Win32.Foundation.HGLOBAL
        _pack_ = 1
if ARCH in 'X64,ARM64':
    PRINTDLG = UnicodeAlias('PRINTDLGW')
elif ARCH in 'X86':
    PRINTDLG = UnicodeAlias('PRINTDLGW')
if ARCH in 'X64,ARM64':
    class PRINTPAGERANGE(Structure):
        nFromPage: UInt32
        nToPage: UInt32
elif ARCH in 'X86':
    class PRINTPAGERANGE(Structure):
        nFromPage: UInt32
        nToPage: UInt32
        _pack_ = 1


make_ready(__name__)
