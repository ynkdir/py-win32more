from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.System.Com
import win32more.UI.Controls
import win32more.UI.Controls.Dialogs
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
OFN_SHAREFALLTHROUGH = 2
OFN_SHARENOWARN = 1
OFN_SHAREWARN = 0
CDM_FIRST = 1124
CDM_LAST = 1224
CDM_GETSPEC = 1124
CDM_GETFILEPATH = 1125
CDM_GETFOLDERPATH = 1126
CDM_GETFOLDERIDLIST = 1127
CDM_SETCONTROLTEXT = 1128
CDM_HIDECONTROL = 1129
CDM_SETDEFEXT = 1130
FR_RAW = 131072
FR_SHOWWRAPAROUND = 262144
FR_NOWRAPAROUND = 524288
FR_WRAPAROUND = 1048576
FRM_FIRST = 1124
FRM_LAST = 1224
FRM_SETOPERATIONRESULT = 1124
FRM_SETOPERATIONRESULTTEXT = 1125
PS_OPENTYPE_FONTTYPE = 65536
TT_OPENTYPE_FONTTYPE = 131072
TYPE1_FONTTYPE = 262144
SYMBOL_FONTTYPE = 524288
WM_CHOOSEFONT_GETLOGFONT = 1025
WM_CHOOSEFONT_SETLOGFONT = 1125
WM_CHOOSEFONT_SETFLAGS = 1126
LBSELCHSTRINGA = 'commdlg_LBSelChangedNotify'
SHAREVISTRINGA = 'commdlg_ShareViolation'
FILEOKSTRINGA = 'commdlg_FileNameOK'
COLOROKSTRINGA = 'commdlg_ColorOK'
SETRGBSTRINGA = 'commdlg_SetRGBColor'
HELPMSGSTRINGA = 'commdlg_help'
FINDMSGSTRINGA = 'commdlg_FindReplace'
LBSELCHSTRINGW = 'commdlg_LBSelChangedNotify'
SHAREVISTRINGW = 'commdlg_ShareViolation'
FILEOKSTRINGW = 'commdlg_FileNameOK'
COLOROKSTRINGW = 'commdlg_ColorOK'
SETRGBSTRINGW = 'commdlg_SetRGBColor'
HELPMSGSTRINGW = 'commdlg_help'
FINDMSGSTRINGW = 'commdlg_FindReplace'
LBSELCHSTRING = 'commdlg_LBSelChangedNotify'
SHAREVISTRING = 'commdlg_ShareViolation'
FILEOKSTRING = 'commdlg_FileNameOK'
COLOROKSTRING = 'commdlg_ColorOK'
SETRGBSTRING = 'commdlg_SetRGBColor'
HELPMSGSTRING = 'commdlg_help'
FINDMSGSTRING = 'commdlg_FindReplace'
CD_LBSELNOITEMS = -1
CD_LBSELCHANGE = 0
CD_LBSELSUB = 1
CD_LBSELADD = 2
START_PAGE_GENERAL = 4294967295
PD_RESULT_CANCEL = 0
PD_RESULT_PRINT = 1
PD_RESULT_APPLY = 2
DN_DEFAULTPRN = 1
WM_PSD_FULLPAGERECT = 1025
WM_PSD_MINMARGINRECT = 1026
WM_PSD_MARGINRECT = 1027
WM_PSD_GREEKTEXTRECT = 1028
WM_PSD_ENVSTAMPRECT = 1029
WM_PSD_YAFULLPAGERECT = 1030
DLG_COLOR = 10
COLOR_HUESCROLL = 700
COLOR_SATSCROLL = 701
COLOR_LUMSCROLL = 702
COLOR_HUE = 703
COLOR_SAT = 704
COLOR_LUM = 705
COLOR_RED = 706
COLOR_GREEN = 707
COLOR_BLUE = 708
COLOR_CURRENT = 709
COLOR_RAINBOW = 710
COLOR_SAVE = 711
COLOR_ADD = 712
COLOR_SOLID = 713
COLOR_TUNE = 714
COLOR_SCHEMES = 715
COLOR_ELEMENT = 716
COLOR_SAMPLES = 717
COLOR_PALETTE = 718
COLOR_MIX = 719
COLOR_BOX1 = 720
COLOR_CUSTOM1 = 721
COLOR_HUEACCEL = 723
COLOR_SATACCEL = 724
COLOR_LUMACCEL = 725
COLOR_REDACCEL = 726
COLOR_GREENACCEL = 727
COLOR_BLUEACCEL = 728
COLOR_SOLID_LEFT = 730
COLOR_SOLID_RIGHT = 731
NUM_BASIC_COLORS = 48
NUM_CUSTOM_COLORS = 16
def _define_GetOpenFileNameA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.UI.Controls.Dialogs.OPENFILENAMEA_head))(('GetOpenFileNameA', windll['COMDLG32.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetOpenFileNameW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.UI.Controls.Dialogs.OPENFILENAMEW_head))(('GetOpenFileNameW', windll['COMDLG32.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSaveFileNameA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.UI.Controls.Dialogs.OPENFILENAMEA_head))(('GetSaveFileNameA', windll['COMDLG32.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSaveFileNameW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.UI.Controls.Dialogs.OPENFILENAMEW_head))(('GetSaveFileNameW', windll['COMDLG32.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFileTitleA():
    try:
        return WINFUNCTYPE(Int16,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt16)(('GetFileTitleA', windll['COMDLG32.dll']), ((1, 'param0'),(1, 'Buf'),(1, 'cchSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFileTitleW():
    try:
        return WINFUNCTYPE(Int16,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt16)(('GetFileTitleW', windll['COMDLG32.dll']), ((1, 'param0'),(1, 'Buf'),(1, 'cchSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ChooseColorA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.UI.Controls.Dialogs.CHOOSECOLORA_head))(('ChooseColorA', windll['COMDLG32.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ChooseColorW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.UI.Controls.Dialogs.CHOOSECOLORW_head))(('ChooseColorW', windll['COMDLG32.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindTextA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HWND,POINTER(win32more.UI.Controls.Dialogs.FINDREPLACEA_head))(('FindTextA', windll['COMDLG32.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindTextW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HWND,POINTER(win32more.UI.Controls.Dialogs.FINDREPLACEW_head))(('FindTextW', windll['COMDLG32.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReplaceTextA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HWND,POINTER(win32more.UI.Controls.Dialogs.FINDREPLACEA_head))(('ReplaceTextA', windll['COMDLG32.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReplaceTextW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HWND,POINTER(win32more.UI.Controls.Dialogs.FINDREPLACEW_head))(('ReplaceTextW', windll['COMDLG32.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ChooseFontA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.UI.Controls.Dialogs.CHOOSEFONTA_head))(('ChooseFontA', windll['COMDLG32.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ChooseFontW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.UI.Controls.Dialogs.CHOOSEFONTW_head))(('ChooseFontW', windll['COMDLG32.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrintDlgA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.UI.Controls.Dialogs.PRINTDLGA_head))(('PrintDlgA', windll['COMDLG32.dll']), ((1, 'pPD'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrintDlgW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.UI.Controls.Dialogs.PRINTDLGW_head))(('PrintDlgW', windll['COMDLG32.dll']), ((1, 'pPD'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrintDlgExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.Dialogs.PRINTDLGEXA_head))(('PrintDlgExA', windll['COMDLG32.dll']), ((1, 'pPD'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrintDlgExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.Dialogs.PRINTDLGEXW_head))(('PrintDlgExW', windll['COMDLG32.dll']), ((1, 'pPD'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CommDlgExtendedError():
    try:
        return WINFUNCTYPE(win32more.UI.Controls.Dialogs.COMMON_DLG_ERRORS,)(('CommDlgExtendedError', windll['COMDLG32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_PageSetupDlgA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.UI.Controls.Dialogs.PAGESETUPDLGA_head))(('PageSetupDlgA', windll['COMDLG32.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PageSetupDlgW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.UI.Controls.Dialogs.PAGESETUPDLGW_head))(('PageSetupDlgW', windll['COMDLG32.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
CHOOSECOLOR_FLAGS = UInt32
CC_RGBINIT = 1
CC_FULLOPEN = 2
CC_PREVENTFULLOPEN = 4
CC_SHOWHELP = 8
CC_ENABLEHOOK = 16
CC_ENABLETEMPLATE = 32
CC_ENABLETEMPLATEHANDLE = 64
CC_SOLIDCOLOR = 128
CC_ANYCOLOR = 256
def _define_CHOOSECOLORA_head():
    class CHOOSECOLORA(Structure):
        pass
    return CHOOSECOLORA
def _define_CHOOSECOLORA():
    CHOOSECOLORA = win32more.UI.Controls.Dialogs.CHOOSECOLORA_head
    CHOOSECOLORA._fields_ = [
        ('lStructSize', UInt32),
        ('hwndOwner', win32more.Foundation.HWND),
        ('hInstance', win32more.Foundation.HWND),
        ('rgbResult', win32more.Foundation.COLORREF),
        ('lpCustColors', POINTER(win32more.Foundation.COLORREF)),
        ('Flags', win32more.UI.Controls.Dialogs.CHOOSECOLOR_FLAGS),
        ('lCustData', win32more.Foundation.LPARAM),
        ('lpfnHook', win32more.UI.Controls.Dialogs.LPCCHOOKPROC),
        ('lpTemplateName', win32more.Foundation.PSTR),
    ]
    return CHOOSECOLORA
def _define_CHOOSECOLORW_head():
    class CHOOSECOLORW(Structure):
        pass
    return CHOOSECOLORW
def _define_CHOOSECOLORW():
    CHOOSECOLORW = win32more.UI.Controls.Dialogs.CHOOSECOLORW_head
    CHOOSECOLORW._fields_ = [
        ('lStructSize', UInt32),
        ('hwndOwner', win32more.Foundation.HWND),
        ('hInstance', win32more.Foundation.HWND),
        ('rgbResult', win32more.Foundation.COLORREF),
        ('lpCustColors', POINTER(win32more.Foundation.COLORREF)),
        ('Flags', win32more.UI.Controls.Dialogs.CHOOSECOLOR_FLAGS),
        ('lCustData', win32more.Foundation.LPARAM),
        ('lpfnHook', win32more.UI.Controls.Dialogs.LPCCHOOKPROC),
        ('lpTemplateName', win32more.Foundation.PWSTR),
    ]
    return CHOOSECOLORW
CHOOSEFONT_FLAGS = UInt32
CF_APPLY = 512
CF_ANSIONLY = 1024
CF_BOTH = 3
CF_EFFECTS = 256
CF_ENABLEHOOK = 8
CF_ENABLETEMPLATE = 16
CF_ENABLETEMPLATEHANDLE = 32
CF_FIXEDPITCHONLY = 16384
CF_FORCEFONTEXIST = 65536
CF_INACTIVEFONTS = 33554432
CF_INITTOLOGFONTSTRUCT = 64
CF_LIMITSIZE = 8192
CF_NOOEMFONTS = 2048
CF_NOFACESEL = 524288
CF_NOSCRIPTSEL = 8388608
CF_NOSIMULATIONS = 4096
CF_NOSIZESEL = 2097152
CF_NOSTYLESEL = 1048576
CF_NOVECTORFONTS = 2048
CF_NOVERTFONTS = 16777216
CF_PRINTERFONTS = 2
CF_SCALABLEONLY = 131072
CF_SCREENFONTS = 1
CF_SCRIPTSONLY = 1024
CF_SELECTSCRIPT = 4194304
CF_SHOWHELP = 4
CF_TTONLY = 262144
CF_USESTYLE = 128
CF_WYSIWYG = 32768
CHOOSEFONT_FONT_TYPE = UInt16
BOLD_FONTTYPE = 256
ITALIC_FONTTYPE = 512
PRINTER_FONTTYPE = 16384
REGULAR_FONTTYPE = 1024
SCREEN_FONTTYPE = 8192
SIMULATED_FONTTYPE = 32768
def _define_CHOOSEFONTA_head():
    class CHOOSEFONTA(Structure):
        pass
    return CHOOSEFONTA
def _define_CHOOSEFONTA():
    CHOOSEFONTA = win32more.UI.Controls.Dialogs.CHOOSEFONTA_head
    CHOOSEFONTA._fields_ = [
        ('lStructSize', UInt32),
        ('hwndOwner', win32more.Foundation.HWND),
        ('hDC', win32more.Graphics.Gdi.HDC),
        ('lpLogFont', POINTER(win32more.Graphics.Gdi.LOGFONTA_head)),
        ('iPointSize', Int32),
        ('Flags', win32more.UI.Controls.Dialogs.CHOOSEFONT_FLAGS),
        ('rgbColors', win32more.Foundation.COLORREF),
        ('lCustData', win32more.Foundation.LPARAM),
        ('lpfnHook', win32more.UI.Controls.Dialogs.LPCFHOOKPROC),
        ('lpTemplateName', win32more.Foundation.PSTR),
        ('hInstance', win32more.Foundation.HINSTANCE),
        ('lpszStyle', win32more.Foundation.PSTR),
        ('nFontType', win32more.UI.Controls.Dialogs.CHOOSEFONT_FONT_TYPE),
        ('___MISSING_ALIGNMENT__', UInt16),
        ('nSizeMin', Int32),
        ('nSizeMax', Int32),
    ]
    return CHOOSEFONTA
def _define_CHOOSEFONTW_head():
    class CHOOSEFONTW(Structure):
        pass
    return CHOOSEFONTW
def _define_CHOOSEFONTW():
    CHOOSEFONTW = win32more.UI.Controls.Dialogs.CHOOSEFONTW_head
    CHOOSEFONTW._fields_ = [
        ('lStructSize', UInt32),
        ('hwndOwner', win32more.Foundation.HWND),
        ('hDC', win32more.Graphics.Gdi.HDC),
        ('lpLogFont', POINTER(win32more.Graphics.Gdi.LOGFONTW_head)),
        ('iPointSize', Int32),
        ('Flags', win32more.UI.Controls.Dialogs.CHOOSEFONT_FLAGS),
        ('rgbColors', win32more.Foundation.COLORREF),
        ('lCustData', win32more.Foundation.LPARAM),
        ('lpfnHook', win32more.UI.Controls.Dialogs.LPCFHOOKPROC),
        ('lpTemplateName', win32more.Foundation.PWSTR),
        ('hInstance', win32more.Foundation.HINSTANCE),
        ('lpszStyle', win32more.Foundation.PWSTR),
        ('nFontType', win32more.UI.Controls.Dialogs.CHOOSEFONT_FONT_TYPE),
        ('___MISSING_ALIGNMENT__', UInt16),
        ('nSizeMin', Int32),
        ('nSizeMax', Int32),
    ]
    return CHOOSEFONTW
COMMON_DIALOG_NOTIFICATION = Int32
CDN_FIRST = -601
CDN_LAST = -699
CDN_INITDONE = -601
CDN_SELCHANGE = -602
CDN_FOLDERCHANGE = -603
CDN_SHAREVIOLATION = -604
CDN_HELP = -605
CDN_FILEOK = -606
CDN_TYPECHANGE = -607
CDN_INCLUDEITEM = -608
COMMON_DLG_ERRORS = UInt32
CDERR_DIALOGFAILURE = 65535
CDERR_GENERALCODES = 0
CDERR_STRUCTSIZE = 1
CDERR_INITIALIZATION = 2
CDERR_NOTEMPLATE = 3
CDERR_NOHINSTANCE = 4
CDERR_LOADSTRFAILURE = 5
CDERR_FINDRESFAILURE = 6
CDERR_LOADRESFAILURE = 7
CDERR_LOCKRESFAILURE = 8
CDERR_MEMALLOCFAILURE = 9
CDERR_MEMLOCKFAILURE = 10
CDERR_NOHOOK = 11
CDERR_REGISTERMSGFAIL = 12
PDERR_PRINTERCODES = 4096
PDERR_SETUPFAILURE = 4097
PDERR_PARSEFAILURE = 4098
PDERR_RETDEFFAILURE = 4099
PDERR_LOADDRVFAILURE = 4100
PDERR_GETDEVMODEFAIL = 4101
PDERR_INITFAILURE = 4102
PDERR_NODEVICES = 4103
PDERR_NODEFAULTPRN = 4104
PDERR_DNDMMISMATCH = 4105
PDERR_CREATEICFAILURE = 4106
PDERR_PRINTERNOTFOUND = 4107
PDERR_DEFAULTDIFFERENT = 4108
CFERR_CHOOSEFONTCODES = 8192
CFERR_NOFONTS = 8193
CFERR_MAXLESSTHANMIN = 8194
FNERR_FILENAMECODES = 12288
FNERR_SUBCLASSFAILURE = 12289
FNERR_INVALIDFILENAME = 12290
FNERR_BUFFERTOOSMALL = 12291
FRERR_FINDREPLACECODES = 16384
FRERR_BUFFERLENGTHZERO = 16385
CCERR_CHOOSECOLORCODES = 20480
def _define_DEVNAMES_head():
    class DEVNAMES(Structure):
        pass
    return DEVNAMES
def _define_DEVNAMES():
    DEVNAMES = win32more.UI.Controls.Dialogs.DEVNAMES_head
    DEVNAMES._fields_ = [
        ('wDriverOffset', UInt16),
        ('wDeviceOffset', UInt16),
        ('wOutputOffset', UInt16),
        ('wDefault', UInt16),
    ]
    return DEVNAMES
FINDREPLACE_FLAGS = UInt32
FR_DIALOGTERM = 64
FR_DOWN = 1
FR_ENABLEHOOK = 256
FR_ENABLETEMPLATE = 512
FR_ENABLETEMPLATEHANDLE = 8192
FR_FINDNEXT = 8
FR_HIDEUPDOWN = 16384
FR_HIDEMATCHCASE = 32768
FR_HIDEWHOLEWORD = 65536
FR_MATCHCASE = 4
FR_NOMATCHCASE = 2048
FR_NOUPDOWN = 1024
FR_NOWHOLEWORD = 4096
FR_REPLACE = 16
FR_REPLACEALL = 32
FR_SHOWHELP = 128
FR_WHOLEWORD = 2
def _define_FINDREPLACEA_head():
    class FINDREPLACEA(Structure):
        pass
    return FINDREPLACEA
def _define_FINDREPLACEA():
    FINDREPLACEA = win32more.UI.Controls.Dialogs.FINDREPLACEA_head
    FINDREPLACEA._fields_ = [
        ('lStructSize', UInt32),
        ('hwndOwner', win32more.Foundation.HWND),
        ('hInstance', win32more.Foundation.HINSTANCE),
        ('Flags', win32more.UI.Controls.Dialogs.FINDREPLACE_FLAGS),
        ('lpstrFindWhat', win32more.Foundation.PSTR),
        ('lpstrReplaceWith', win32more.Foundation.PSTR),
        ('wFindWhatLen', UInt16),
        ('wReplaceWithLen', UInt16),
        ('lCustData', win32more.Foundation.LPARAM),
        ('lpfnHook', win32more.UI.Controls.Dialogs.LPFRHOOKPROC),
        ('lpTemplateName', win32more.Foundation.PSTR),
    ]
    return FINDREPLACEA
def _define_FINDREPLACEW_head():
    class FINDREPLACEW(Structure):
        pass
    return FINDREPLACEW
def _define_FINDREPLACEW():
    FINDREPLACEW = win32more.UI.Controls.Dialogs.FINDREPLACEW_head
    FINDREPLACEW._fields_ = [
        ('lStructSize', UInt32),
        ('hwndOwner', win32more.Foundation.HWND),
        ('hInstance', win32more.Foundation.HINSTANCE),
        ('Flags', win32more.UI.Controls.Dialogs.FINDREPLACE_FLAGS),
        ('lpstrFindWhat', win32more.Foundation.PWSTR),
        ('lpstrReplaceWith', win32more.Foundation.PWSTR),
        ('wFindWhatLen', UInt16),
        ('wReplaceWithLen', UInt16),
        ('lCustData', win32more.Foundation.LPARAM),
        ('lpfnHook', win32more.UI.Controls.Dialogs.LPFRHOOKPROC),
        ('lpTemplateName', win32more.Foundation.PWSTR),
    ]
    return FINDREPLACEW
def _define_IPrintDialogCallback_head():
    class IPrintDialogCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('5852a2c3-6530-11d1-b6-a3-00-00-f8-75-7b-f9')
    return IPrintDialogCallback
def _define_IPrintDialogCallback():
    IPrintDialogCallback = win32more.UI.Controls.Dialogs.IPrintDialogCallback_head
    IPrintDialogCallback.InitDone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'InitDone', ()))
    IPrintDialogCallback.SelectionChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'SelectionChange', ()))
    IPrintDialogCallback.HandleMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.LRESULT))(5, 'HandleMessage', ((1, 'hDlg'),(1, 'uMsg'),(1, 'wParam'),(1, 'lParam'),(1, 'pResult'),)))
    win32more.System.Com.IUnknown
    return IPrintDialogCallback
def _define_IPrintDialogServices_head():
    class IPrintDialogServices(win32more.System.Com.IUnknown_head):
        Guid = Guid('509aaeda-5639-11d1-b6-a1-00-00-f8-75-7b-f9')
    return IPrintDialogServices
def _define_IPrintDialogServices():
    IPrintDialogServices = win32more.UI.Controls.Dialogs.IPrintDialogServices_head
    IPrintDialogServices.GetCurrentDevMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Gdi.DEVMODEA_head),POINTER(UInt32))(3, 'GetCurrentDevMode', ((1, 'pDevMode'),(1, 'pcbSize'),)))
    IPrintDialogServices.GetCurrentPrinterName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32))(4, 'GetCurrentPrinterName', ((1, 'pPrinterName'),(1, 'pcchSize'),)))
    IPrintDialogServices.GetCurrentPortName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32))(5, 'GetCurrentPortName', ((1, 'pPortName'),(1, 'pcchSize'),)))
    win32more.System.Com.IUnknown
    return IPrintDialogServices
def _define_LPCCHOOKPROC():
    return WINFUNCTYPE(UIntPtr,win32more.Foundation.HWND,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM)
def _define_LPCFHOOKPROC():
    return WINFUNCTYPE(UIntPtr,win32more.Foundation.HWND,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM)
def _define_LPFRHOOKPROC():
    return WINFUNCTYPE(UIntPtr,win32more.Foundation.HWND,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM)
def _define_LPOFNHOOKPROC():
    return WINFUNCTYPE(UIntPtr,win32more.Foundation.HWND,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM)
def _define_LPPAGEPAINTHOOK():
    return WINFUNCTYPE(UIntPtr,win32more.Foundation.HWND,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM)
def _define_LPPAGESETUPHOOK():
    return WINFUNCTYPE(UIntPtr,win32more.Foundation.HWND,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM)
def _define_LPPRINTHOOKPROC():
    return WINFUNCTYPE(UIntPtr,win32more.Foundation.HWND,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM)
def _define_LPSETUPHOOKPROC():
    return WINFUNCTYPE(UIntPtr,win32more.Foundation.HWND,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM)
def _define_OFNOTIFYA_head():
    class OFNOTIFYA(Structure):
        pass
    return OFNOTIFYA
def _define_OFNOTIFYA():
    OFNOTIFYA = win32more.UI.Controls.Dialogs.OFNOTIFYA_head
    OFNOTIFYA._fields_ = [
        ('hdr', win32more.UI.Controls.NMHDR),
        ('lpOFN', POINTER(win32more.UI.Controls.Dialogs.OPENFILENAMEA_head)),
        ('pszFile', win32more.Foundation.PSTR),
    ]
    return OFNOTIFYA
def _define_OFNOTIFYEXA_head():
    class OFNOTIFYEXA(Structure):
        pass
    return OFNOTIFYEXA
def _define_OFNOTIFYEXA():
    OFNOTIFYEXA = win32more.UI.Controls.Dialogs.OFNOTIFYEXA_head
    OFNOTIFYEXA._fields_ = [
        ('hdr', win32more.UI.Controls.NMHDR),
        ('lpOFN', POINTER(win32more.UI.Controls.Dialogs.OPENFILENAMEA_head)),
        ('psf', c_void_p),
        ('pidl', c_void_p),
    ]
    return OFNOTIFYEXA
def _define_OFNOTIFYEXW_head():
    class OFNOTIFYEXW(Structure):
        pass
    return OFNOTIFYEXW
def _define_OFNOTIFYEXW():
    OFNOTIFYEXW = win32more.UI.Controls.Dialogs.OFNOTIFYEXW_head
    OFNOTIFYEXW._fields_ = [
        ('hdr', win32more.UI.Controls.NMHDR),
        ('lpOFN', POINTER(win32more.UI.Controls.Dialogs.OPENFILENAMEW_head)),
        ('psf', c_void_p),
        ('pidl', c_void_p),
    ]
    return OFNOTIFYEXW
def _define_OFNOTIFYW_head():
    class OFNOTIFYW(Structure):
        pass
    return OFNOTIFYW
def _define_OFNOTIFYW():
    OFNOTIFYW = win32more.UI.Controls.Dialogs.OFNOTIFYW_head
    OFNOTIFYW._fields_ = [
        ('hdr', win32more.UI.Controls.NMHDR),
        ('lpOFN', POINTER(win32more.UI.Controls.Dialogs.OPENFILENAMEW_head)),
        ('pszFile', win32more.Foundation.PWSTR),
    ]
    return OFNOTIFYW
OPEN_FILENAME_FLAGS = UInt32
OFN_READONLY = 1
OFN_OVERWRITEPROMPT = 2
OFN_HIDEREADONLY = 4
OFN_NOCHANGEDIR = 8
OFN_SHOWHELP = 16
OFN_ENABLEHOOK = 32
OFN_ENABLETEMPLATE = 64
OFN_ENABLETEMPLATEHANDLE = 128
OFN_NOVALIDATE = 256
OFN_ALLOWMULTISELECT = 512
OFN_EXTENSIONDIFFERENT = 1024
OFN_PATHMUSTEXIST = 2048
OFN_FILEMUSTEXIST = 4096
OFN_CREATEPROMPT = 8192
OFN_SHAREAWARE = 16384
OFN_NOREADONLYRETURN = 32768
OFN_NOTESTFILECREATE = 65536
OFN_NONETWORKBUTTON = 131072
OFN_NOLONGNAMES = 262144
OFN_EXPLORER = 524288
OFN_NODEREFERENCELINKS = 1048576
OFN_LONGNAMES = 2097152
OFN_ENABLEINCLUDENOTIFY = 4194304
OFN_ENABLESIZING = 8388608
OFN_DONTADDTORECENT = 33554432
OFN_FORCESHOWHIDDEN = 268435456
OPEN_FILENAME_FLAGS_EX = UInt32
OFN_EX_NONE = 0
OFN_EX_NOPLACESBAR = 1
def _define_OPENFILENAME_NT4A_head():
    class OPENFILENAME_NT4A(Structure):
        pass
    return OPENFILENAME_NT4A
def _define_OPENFILENAME_NT4A():
    OPENFILENAME_NT4A = win32more.UI.Controls.Dialogs.OPENFILENAME_NT4A_head
    OPENFILENAME_NT4A._fields_ = [
        ('lStructSize', UInt32),
        ('hwndOwner', win32more.Foundation.HWND),
        ('hInstance', win32more.Foundation.HINSTANCE),
        ('lpstrFilter', win32more.Foundation.PSTR),
        ('lpstrCustomFilter', win32more.Foundation.PSTR),
        ('nMaxCustFilter', UInt32),
        ('nFilterIndex', UInt32),
        ('lpstrFile', win32more.Foundation.PSTR),
        ('nMaxFile', UInt32),
        ('lpstrFileTitle', win32more.Foundation.PSTR),
        ('nMaxFileTitle', UInt32),
        ('lpstrInitialDir', win32more.Foundation.PSTR),
        ('lpstrTitle', win32more.Foundation.PSTR),
        ('Flags', UInt32),
        ('nFileOffset', UInt16),
        ('nFileExtension', UInt16),
        ('lpstrDefExt', win32more.Foundation.PSTR),
        ('lCustData', win32more.Foundation.LPARAM),
        ('lpfnHook', win32more.UI.Controls.Dialogs.LPOFNHOOKPROC),
        ('lpTemplateName', win32more.Foundation.PSTR),
    ]
    return OPENFILENAME_NT4A
def _define_OPENFILENAME_NT4W_head():
    class OPENFILENAME_NT4W(Structure):
        pass
    return OPENFILENAME_NT4W
def _define_OPENFILENAME_NT4W():
    OPENFILENAME_NT4W = win32more.UI.Controls.Dialogs.OPENFILENAME_NT4W_head
    OPENFILENAME_NT4W._fields_ = [
        ('lStructSize', UInt32),
        ('hwndOwner', win32more.Foundation.HWND),
        ('hInstance', win32more.Foundation.HINSTANCE),
        ('lpstrFilter', win32more.Foundation.PWSTR),
        ('lpstrCustomFilter', win32more.Foundation.PWSTR),
        ('nMaxCustFilter', UInt32),
        ('nFilterIndex', UInt32),
        ('lpstrFile', win32more.Foundation.PWSTR),
        ('nMaxFile', UInt32),
        ('lpstrFileTitle', win32more.Foundation.PWSTR),
        ('nMaxFileTitle', UInt32),
        ('lpstrInitialDir', win32more.Foundation.PWSTR),
        ('lpstrTitle', win32more.Foundation.PWSTR),
        ('Flags', UInt32),
        ('nFileOffset', UInt16),
        ('nFileExtension', UInt16),
        ('lpstrDefExt', win32more.Foundation.PWSTR),
        ('lCustData', win32more.Foundation.LPARAM),
        ('lpfnHook', win32more.UI.Controls.Dialogs.LPOFNHOOKPROC),
        ('lpTemplateName', win32more.Foundation.PWSTR),
    ]
    return OPENFILENAME_NT4W
def _define_OPENFILENAMEA_head():
    class OPENFILENAMEA(Structure):
        pass
    return OPENFILENAMEA
def _define_OPENFILENAMEA():
    OPENFILENAMEA = win32more.UI.Controls.Dialogs.OPENFILENAMEA_head
    OPENFILENAMEA._fields_ = [
        ('lStructSize', UInt32),
        ('hwndOwner', win32more.Foundation.HWND),
        ('hInstance', win32more.Foundation.HINSTANCE),
        ('lpstrFilter', win32more.Foundation.PSTR),
        ('lpstrCustomFilter', win32more.Foundation.PSTR),
        ('nMaxCustFilter', UInt32),
        ('nFilterIndex', UInt32),
        ('lpstrFile', win32more.Foundation.PSTR),
        ('nMaxFile', UInt32),
        ('lpstrFileTitle', win32more.Foundation.PSTR),
        ('nMaxFileTitle', UInt32),
        ('lpstrInitialDir', win32more.Foundation.PSTR),
        ('lpstrTitle', win32more.Foundation.PSTR),
        ('Flags', win32more.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS),
        ('nFileOffset', UInt16),
        ('nFileExtension', UInt16),
        ('lpstrDefExt', win32more.Foundation.PSTR),
        ('lCustData', win32more.Foundation.LPARAM),
        ('lpfnHook', win32more.UI.Controls.Dialogs.LPOFNHOOKPROC),
        ('lpTemplateName', win32more.Foundation.PSTR),
        ('pvReserved', c_void_p),
        ('dwReserved', UInt32),
        ('FlagsEx', win32more.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS_EX),
    ]
    return OPENFILENAMEA
def _define_OPENFILENAMEW_head():
    class OPENFILENAMEW(Structure):
        pass
    return OPENFILENAMEW
def _define_OPENFILENAMEW():
    OPENFILENAMEW = win32more.UI.Controls.Dialogs.OPENFILENAMEW_head
    OPENFILENAMEW._fields_ = [
        ('lStructSize', UInt32),
        ('hwndOwner', win32more.Foundation.HWND),
        ('hInstance', win32more.Foundation.HINSTANCE),
        ('lpstrFilter', win32more.Foundation.PWSTR),
        ('lpstrCustomFilter', win32more.Foundation.PWSTR),
        ('nMaxCustFilter', UInt32),
        ('nFilterIndex', UInt32),
        ('lpstrFile', win32more.Foundation.PWSTR),
        ('nMaxFile', UInt32),
        ('lpstrFileTitle', win32more.Foundation.PWSTR),
        ('nMaxFileTitle', UInt32),
        ('lpstrInitialDir', win32more.Foundation.PWSTR),
        ('lpstrTitle', win32more.Foundation.PWSTR),
        ('Flags', win32more.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS),
        ('nFileOffset', UInt16),
        ('nFileExtension', UInt16),
        ('lpstrDefExt', win32more.Foundation.PWSTR),
        ('lCustData', win32more.Foundation.LPARAM),
        ('lpfnHook', win32more.UI.Controls.Dialogs.LPOFNHOOKPROC),
        ('lpTemplateName', win32more.Foundation.PWSTR),
        ('pvReserved', c_void_p),
        ('dwReserved', UInt32),
        ('FlagsEx', win32more.UI.Controls.Dialogs.OPEN_FILENAME_FLAGS_EX),
    ]
    return OPENFILENAMEW
PAGESETUPDLG_FLAGS = UInt32
PSD_DEFAULTMINMARGINS = 0
PSD_DISABLEMARGINS = 16
PSD_DISABLEORIENTATION = 256
PSD_DISABLEPAGEPAINTING = 524288
PSD_DISABLEPAPER = 512
PSD_DISABLEPRINTER = 32
PSD_ENABLEPAGEPAINTHOOK = 262144
PSD_ENABLEPAGESETUPHOOK = 8192
PSD_ENABLEPAGESETUPTEMPLATE = 32768
PSD_ENABLEPAGESETUPTEMPLATEHANDLE = 131072
PSD_INHUNDREDTHSOFMILLIMETERS = 8
PSD_INTHOUSANDTHSOFINCHES = 4
PSD_INWININIINTLMEASURE = 0
PSD_MARGINS = 2
PSD_MINMARGINS = 1
PSD_NONETWORKBUTTON = 2097152
PSD_NOWARNING = 128
PSD_RETURNDEFAULT = 1024
PSD_SHOWHELP = 2048
def _define_PAGESETUPDLGA_head():
    class PAGESETUPDLGA(Structure):
        pass
    return PAGESETUPDLGA
def _define_PAGESETUPDLGA():
    PAGESETUPDLGA = win32more.UI.Controls.Dialogs.PAGESETUPDLGA_head
    PAGESETUPDLGA._fields_ = [
        ('lStructSize', UInt32),
        ('hwndOwner', win32more.Foundation.HWND),
        ('hDevMode', IntPtr),
        ('hDevNames', IntPtr),
        ('Flags', win32more.UI.Controls.Dialogs.PAGESETUPDLG_FLAGS),
        ('ptPaperSize', win32more.Foundation.POINT),
        ('rtMinMargin', win32more.Foundation.RECT),
        ('rtMargin', win32more.Foundation.RECT),
        ('hInstance', win32more.Foundation.HINSTANCE),
        ('lCustData', win32more.Foundation.LPARAM),
        ('lpfnPageSetupHook', win32more.UI.Controls.Dialogs.LPPAGESETUPHOOK),
        ('lpfnPagePaintHook', win32more.UI.Controls.Dialogs.LPPAGEPAINTHOOK),
        ('lpPageSetupTemplateName', win32more.Foundation.PSTR),
        ('hPageSetupTemplate', IntPtr),
    ]
    return PAGESETUPDLGA
def _define_PAGESETUPDLGW_head():
    class PAGESETUPDLGW(Structure):
        pass
    return PAGESETUPDLGW
def _define_PAGESETUPDLGW():
    PAGESETUPDLGW = win32more.UI.Controls.Dialogs.PAGESETUPDLGW_head
    PAGESETUPDLGW._fields_ = [
        ('lStructSize', UInt32),
        ('hwndOwner', win32more.Foundation.HWND),
        ('hDevMode', IntPtr),
        ('hDevNames', IntPtr),
        ('Flags', win32more.UI.Controls.Dialogs.PAGESETUPDLG_FLAGS),
        ('ptPaperSize', win32more.Foundation.POINT),
        ('rtMinMargin', win32more.Foundation.RECT),
        ('rtMargin', win32more.Foundation.RECT),
        ('hInstance', win32more.Foundation.HINSTANCE),
        ('lCustData', win32more.Foundation.LPARAM),
        ('lpfnPageSetupHook', win32more.UI.Controls.Dialogs.LPPAGESETUPHOOK),
        ('lpfnPagePaintHook', win32more.UI.Controls.Dialogs.LPPAGEPAINTHOOK),
        ('lpPageSetupTemplateName', win32more.Foundation.PWSTR),
        ('hPageSetupTemplate', IntPtr),
    ]
    return PAGESETUPDLGW
def _define_PRINTDLGA_head():
    class PRINTDLGA(Structure):
        pass
    return PRINTDLGA
def _define_PRINTDLGA():
    PRINTDLGA = win32more.UI.Controls.Dialogs.PRINTDLGA_head
    PRINTDLGA._fields_ = [
        ('lStructSize', UInt32),
        ('hwndOwner', win32more.Foundation.HWND),
        ('hDevMode', IntPtr),
        ('hDevNames', IntPtr),
        ('hDC', win32more.Graphics.Gdi.HDC),
        ('Flags', win32more.UI.Controls.Dialogs.PRINTDLGEX_FLAGS),
        ('nFromPage', UInt16),
        ('nToPage', UInt16),
        ('nMinPage', UInt16),
        ('nMaxPage', UInt16),
        ('nCopies', UInt16),
        ('hInstance', win32more.Foundation.HINSTANCE),
        ('lCustData', win32more.Foundation.LPARAM),
        ('lpfnPrintHook', win32more.UI.Controls.Dialogs.LPPRINTHOOKPROC),
        ('lpfnSetupHook', win32more.UI.Controls.Dialogs.LPSETUPHOOKPROC),
        ('lpPrintTemplateName', win32more.Foundation.PSTR),
        ('lpSetupTemplateName', win32more.Foundation.PSTR),
        ('hPrintTemplate', IntPtr),
        ('hSetupTemplate', IntPtr),
    ]
    return PRINTDLGA
PRINTDLGEX_FLAGS = UInt32
PD_ALLPAGES = 0
PD_COLLATE = 16
PD_CURRENTPAGE = 4194304
PD_DISABLEPRINTTOFILE = 524288
PD_ENABLEPRINTTEMPLATE = 16384
PD_ENABLEPRINTTEMPLATEHANDLE = 65536
PD_EXCLUSIONFLAGS = 16777216
PD_HIDEPRINTTOFILE = 1048576
PD_NOCURRENTPAGE = 8388608
PD_NOPAGENUMS = 8
PD_NOSELECTION = 4
PD_NOWARNING = 128
PD_PAGENUMS = 2
PD_PRINTTOFILE = 32
PD_RETURNDC = 256
PD_RETURNDEFAULT = 1024
PD_RETURNIC = 512
PD_SELECTION = 1
PD_USEDEVMODECOPIES = 262144
PD_USEDEVMODECOPIESANDCOLLATE = 262144
PD_USELARGETEMPLATE = 268435456
PD_ENABLEPRINTHOOK = 4096
PD_ENABLESETUPHOOK = 8192
PD_ENABLESETUPTEMPLATE = 32768
PD_ENABLESETUPTEMPLATEHANDLE = 131072
PD_NONETWORKBUTTON = 2097152
PD_PRINTSETUP = 64
PD_SHOWHELP = 2048
def _define_PRINTDLGEXA_head():
    class PRINTDLGEXA(Structure):
        pass
    return PRINTDLGEXA
def _define_PRINTDLGEXA():
    PRINTDLGEXA = win32more.UI.Controls.Dialogs.PRINTDLGEXA_head
    PRINTDLGEXA._fields_ = [
        ('lStructSize', UInt32),
        ('hwndOwner', win32more.Foundation.HWND),
        ('hDevMode', IntPtr),
        ('hDevNames', IntPtr),
        ('hDC', win32more.Graphics.Gdi.HDC),
        ('Flags', win32more.UI.Controls.Dialogs.PRINTDLGEX_FLAGS),
        ('Flags2', UInt32),
        ('ExclusionFlags', UInt32),
        ('nPageRanges', UInt32),
        ('nMaxPageRanges', UInt32),
        ('lpPageRanges', POINTER(win32more.UI.Controls.Dialogs.PRINTPAGERANGE_head)),
        ('nMinPage', UInt32),
        ('nMaxPage', UInt32),
        ('nCopies', UInt32),
        ('hInstance', win32more.Foundation.HINSTANCE),
        ('lpPrintTemplateName', win32more.Foundation.PSTR),
        ('lpCallback', win32more.System.Com.IUnknown_head),
        ('nPropertyPages', UInt32),
        ('lphPropertyPages', POINTER(win32more.UI.Controls.HPROPSHEETPAGE)),
        ('nStartPage', UInt32),
        ('dwResultAction', UInt32),
    ]
    return PRINTDLGEXA
def _define_PRINTDLGEXW_head():
    class PRINTDLGEXW(Structure):
        pass
    return PRINTDLGEXW
def _define_PRINTDLGEXW():
    PRINTDLGEXW = win32more.UI.Controls.Dialogs.PRINTDLGEXW_head
    PRINTDLGEXW._fields_ = [
        ('lStructSize', UInt32),
        ('hwndOwner', win32more.Foundation.HWND),
        ('hDevMode', IntPtr),
        ('hDevNames', IntPtr),
        ('hDC', win32more.Graphics.Gdi.HDC),
        ('Flags', win32more.UI.Controls.Dialogs.PRINTDLGEX_FLAGS),
        ('Flags2', UInt32),
        ('ExclusionFlags', UInt32),
        ('nPageRanges', UInt32),
        ('nMaxPageRanges', UInt32),
        ('lpPageRanges', POINTER(win32more.UI.Controls.Dialogs.PRINTPAGERANGE_head)),
        ('nMinPage', UInt32),
        ('nMaxPage', UInt32),
        ('nCopies', UInt32),
        ('hInstance', win32more.Foundation.HINSTANCE),
        ('lpPrintTemplateName', win32more.Foundation.PWSTR),
        ('lpCallback', win32more.System.Com.IUnknown_head),
        ('nPropertyPages', UInt32),
        ('lphPropertyPages', POINTER(win32more.UI.Controls.HPROPSHEETPAGE)),
        ('nStartPage', UInt32),
        ('dwResultAction', UInt32),
    ]
    return PRINTDLGEXW
def _define_PRINTDLGW_head():
    class PRINTDLGW(Structure):
        pass
    return PRINTDLGW
def _define_PRINTDLGW():
    PRINTDLGW = win32more.UI.Controls.Dialogs.PRINTDLGW_head
    PRINTDLGW._fields_ = [
        ('lStructSize', UInt32),
        ('hwndOwner', win32more.Foundation.HWND),
        ('hDevMode', IntPtr),
        ('hDevNames', IntPtr),
        ('hDC', win32more.Graphics.Gdi.HDC),
        ('Flags', win32more.UI.Controls.Dialogs.PRINTDLGEX_FLAGS),
        ('nFromPage', UInt16),
        ('nToPage', UInt16),
        ('nMinPage', UInt16),
        ('nMaxPage', UInt16),
        ('nCopies', UInt16),
        ('hInstance', win32more.Foundation.HINSTANCE),
        ('lCustData', win32more.Foundation.LPARAM),
        ('lpfnPrintHook', win32more.UI.Controls.Dialogs.LPPRINTHOOKPROC),
        ('lpfnSetupHook', win32more.UI.Controls.Dialogs.LPSETUPHOOKPROC),
        ('lpPrintTemplateName', win32more.Foundation.PWSTR),
        ('lpSetupTemplateName', win32more.Foundation.PWSTR),
        ('hPrintTemplate', IntPtr),
        ('hSetupTemplate', IntPtr),
    ]
    return PRINTDLGW
def _define_PRINTPAGERANGE_head():
    class PRINTPAGERANGE(Structure):
        pass
    return PRINTPAGERANGE
def _define_PRINTPAGERANGE():
    PRINTPAGERANGE = win32more.UI.Controls.Dialogs.PRINTPAGERANGE_head
    PRINTPAGERANGE._fields_ = [
        ('nFromPage', UInt32),
        ('nToPage', UInt32),
    ]
    return PRINTPAGERANGE
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
