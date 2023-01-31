from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Foundation
import win32more.Globalization
import win32more.Graphics.Direct2D
import win32more.Graphics.Gdi
import win32more.System.Com
import win32more.System.Com.StructuredStorage
import win32more.System.Ole
import win32more.System.SystemServices
import win32more.UI.Controls
import win32more.UI.Controls.RichEdit
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
cchTextLimitDefault: UInt32 = 32767
MSFTEDIT_CLASS: String = 'RICHEDIT50W'
CERICHEDIT_CLASSA: String = 'RichEditCEA'
CERICHEDIT_CLASSW: String = 'RichEditCEW'
RICHEDIT_CLASSA: String = 'RichEdit20A'
RICHEDIT_CLASS10A: String = 'RICHEDIT'
RICHEDIT_CLASSW: String = 'RichEdit20W'
RICHEDIT_CLASS: String = 'RichEdit20W'
EM_CANPASTE: UInt32 = 1074
EM_DISPLAYBAND: UInt32 = 1075
EM_EXGETSEL: UInt32 = 1076
EM_EXLIMITTEXT: UInt32 = 1077
EM_EXLINEFROMCHAR: UInt32 = 1078
EM_EXSETSEL: UInt32 = 1079
EM_FINDTEXT: UInt32 = 1080
EM_FORMATRANGE: UInt32 = 1081
EM_GETCHARFORMAT: UInt32 = 1082
EM_GETEVENTMASK: UInt32 = 1083
EM_GETOLEINTERFACE: UInt32 = 1084
EM_GETPARAFORMAT: UInt32 = 1085
EM_GETSELTEXT: UInt32 = 1086
EM_HIDESELECTION: UInt32 = 1087
EM_PASTESPECIAL: UInt32 = 1088
EM_REQUESTRESIZE: UInt32 = 1089
EM_SELECTIONTYPE: UInt32 = 1090
EM_SETBKGNDCOLOR: UInt32 = 1091
EM_SETCHARFORMAT: UInt32 = 1092
EM_SETEVENTMASK: UInt32 = 1093
EM_SETOLECALLBACK: UInt32 = 1094
EM_SETPARAFORMAT: UInt32 = 1095
EM_SETTARGETDEVICE: UInt32 = 1096
EM_STREAMIN: UInt32 = 1097
EM_STREAMOUT: UInt32 = 1098
EM_GETTEXTRANGE: UInt32 = 1099
EM_FINDWORDBREAK: UInt32 = 1100
EM_SETOPTIONS: UInt32 = 1101
EM_GETOPTIONS: UInt32 = 1102
EM_FINDTEXTEX: UInt32 = 1103
EM_GETWORDBREAKPROCEX: UInt32 = 1104
EM_SETWORDBREAKPROCEX: UInt32 = 1105
EM_SETUNDOLIMIT: UInt32 = 1106
EM_REDO: UInt32 = 1108
EM_CANREDO: UInt32 = 1109
EM_GETUNDONAME: UInt32 = 1110
EM_GETREDONAME: UInt32 = 1111
EM_STOPGROUPTYPING: UInt32 = 1112
EM_SETTEXTMODE: UInt32 = 1113
EM_GETTEXTMODE: UInt32 = 1114
EM_AUTOURLDETECT: UInt32 = 1115
AURL_ENABLEURL: UInt32 = 1
AURL_ENABLEEMAILADDR: UInt32 = 2
AURL_ENABLETELNO: UInt32 = 4
AURL_ENABLEEAURLS: UInt32 = 8
AURL_ENABLEDRIVELETTERS: UInt32 = 16
AURL_DISABLEMIXEDLGC: UInt32 = 32
EM_GETAUTOURLDETECT: UInt32 = 1116
EM_SETPALETTE: UInt32 = 1117
EM_GETTEXTEX: UInt32 = 1118
EM_GETTEXTLENGTHEX: UInt32 = 1119
EM_SHOWSCROLLBAR: UInt32 = 1120
EM_SETTEXTEX: UInt32 = 1121
EM_SETPUNCTUATION: UInt32 = 1124
EM_GETPUNCTUATION: UInt32 = 1125
EM_SETWORDWRAPMODE: UInt32 = 1126
EM_GETWORDWRAPMODE: UInt32 = 1127
EM_SETIMECOLOR: UInt32 = 1128
EM_GETIMECOLOR: UInt32 = 1129
EM_SETIMEOPTIONS: UInt32 = 1130
EM_GETIMEOPTIONS: UInt32 = 1131
EM_CONVPOSITION: UInt32 = 1132
EM_SETLANGOPTIONS: UInt32 = 1144
EM_GETLANGOPTIONS: UInt32 = 1145
EM_GETIMECOMPMODE: UInt32 = 1146
EM_FINDTEXTW: UInt32 = 1147
EM_FINDTEXTEXW: UInt32 = 1148
EM_RECONVERSION: UInt32 = 1149
EM_SETIMEMODEBIAS: UInt32 = 1150
EM_GETIMEMODEBIAS: UInt32 = 1151
EM_SETBIDIOPTIONS: UInt32 = 1224
EM_GETBIDIOPTIONS: UInt32 = 1225
EM_SETTYPOGRAPHYOPTIONS: UInt32 = 1226
EM_GETTYPOGRAPHYOPTIONS: UInt32 = 1227
EM_SETEDITSTYLE: UInt32 = 1228
EM_GETEDITSTYLE: UInt32 = 1229
SES_EMULATESYSEDIT: UInt32 = 1
SES_BEEPONMAXTEXT: UInt32 = 2
SES_EXTENDBACKCOLOR: UInt32 = 4
SES_MAPCPS: UInt32 = 8
SES_HYPERLINKTOOLTIPS: UInt32 = 8
SES_EMULATE10: UInt32 = 16
SES_DEFAULTLATINLIGA: UInt32 = 16
SES_USECRLF: UInt32 = 32
SES_NOFOCUSLINKNOTIFY: UInt32 = 32
SES_USEAIMM: UInt32 = 64
SES_NOIME: UInt32 = 128
SES_ALLOWBEEPS: UInt32 = 256
SES_UPPERCASE: UInt32 = 512
SES_LOWERCASE: UInt32 = 1024
SES_NOINPUTSEQUENCECHK: UInt32 = 2048
SES_BIDI: UInt32 = 4096
SES_SCROLLONKILLFOCUS: UInt32 = 8192
SES_XLTCRCRLFTOCR: UInt32 = 16384
SES_DRAFTMODE: UInt32 = 32768
SES_USECTF: UInt32 = 65536
SES_HIDEGRIDLINES: UInt32 = 131072
SES_USEATFONT: UInt32 = 262144
SES_CUSTOMLOOK: UInt32 = 524288
SES_LBSCROLLNOTIFY: UInt32 = 1048576
SES_CTFALLOWEMBED: UInt32 = 2097152
SES_CTFALLOWSMARTTAG: UInt32 = 4194304
SES_CTFALLOWPROOFING: UInt32 = 8388608
SES_LOGICALCARET: UInt32 = 16777216
SES_WORDDRAGDROP: UInt32 = 33554432
SES_SMARTDRAGDROP: UInt32 = 67108864
SES_MULTISELECT: UInt32 = 134217728
SES_CTFNOLOCK: UInt32 = 268435456
SES_NOEALINEHEIGHTADJUST: UInt32 = 536870912
SES_MAX: UInt32 = 536870912
IMF_AUTOKEYBOARD: UInt32 = 1
IMF_AUTOFONT: UInt32 = 2
IMF_IMECANCELCOMPLETE: UInt32 = 4
IMF_IMEALWAYSSENDNOTIFY: UInt32 = 8
IMF_AUTOFONTSIZEADJUST: UInt32 = 16
IMF_UIFONTS: UInt32 = 32
IMF_NOIMPLICITLANG: UInt32 = 64
IMF_DUALFONT: UInt32 = 128
IMF_NOKBDLIDFIXUP: UInt32 = 512
IMF_NORTFFONTSUBSTITUTE: UInt32 = 1024
IMF_SPELLCHECKING: UInt32 = 2048
IMF_TKBPREDICTION: UInt32 = 4096
IMF_IMEUIINTEGRATION: UInt32 = 8192
ICM_NOTOPEN: UInt32 = 0
ICM_LEVEL3: UInt32 = 1
ICM_LEVEL2: UInt32 = 2
ICM_LEVEL2_5: UInt32 = 3
ICM_LEVEL2_SUI: UInt32 = 4
ICM_CTF: UInt32 = 5
TO_ADVANCEDTYPOGRAPHY: UInt32 = 1
TO_SIMPLELINEBREAK: UInt32 = 2
TO_DISABLECUSTOMTEXTOUT: UInt32 = 4
TO_ADVANCEDLAYOUT: UInt32 = 8
EM_OUTLINE: UInt32 = 1244
EM_GETSCROLLPOS: UInt32 = 1245
EM_SETSCROLLPOS: UInt32 = 1246
EM_SETFONTSIZE: UInt32 = 1247
EM_GETZOOM: UInt32 = 1248
EM_SETZOOM: UInt32 = 1249
EM_GETVIEWKIND: UInt32 = 1250
EM_SETVIEWKIND: UInt32 = 1251
EM_GETPAGE: UInt32 = 1252
EM_SETPAGE: UInt32 = 1253
EM_GETHYPHENATEINFO: UInt32 = 1254
EM_SETHYPHENATEINFO: UInt32 = 1255
EM_GETPAGEROTATE: UInt32 = 1259
EM_SETPAGEROTATE: UInt32 = 1260
EM_GETCTFMODEBIAS: UInt32 = 1261
EM_SETCTFMODEBIAS: UInt32 = 1262
EM_GETCTFOPENSTATUS: UInt32 = 1264
EM_SETCTFOPENSTATUS: UInt32 = 1265
EM_GETIMECOMPTEXT: UInt32 = 1266
EM_ISIME: UInt32 = 1267
EM_GETIMEPROPERTY: UInt32 = 1268
EM_GETQUERYRTFOBJ: UInt32 = 1293
EM_SETQUERYRTFOBJ: UInt32 = 1294
EPR_0: UInt32 = 0
EPR_270: UInt32 = 1
EPR_180: UInt32 = 2
EPR_90: UInt32 = 3
EPR_SE: UInt32 = 5
CTFMODEBIAS_DEFAULT: UInt32 = 0
CTFMODEBIAS_FILENAME: UInt32 = 1
CTFMODEBIAS_NAME: UInt32 = 2
CTFMODEBIAS_READING: UInt32 = 3
CTFMODEBIAS_DATETIME: UInt32 = 4
CTFMODEBIAS_CONVERSATION: UInt32 = 5
CTFMODEBIAS_NUMERIC: UInt32 = 6
CTFMODEBIAS_HIRAGANA: UInt32 = 7
CTFMODEBIAS_KATAKANA: UInt32 = 8
CTFMODEBIAS_HANGUL: UInt32 = 9
CTFMODEBIAS_HALFWIDTHKATAKANA: UInt32 = 10
CTFMODEBIAS_FULLWIDTHALPHANUMERIC: UInt32 = 11
CTFMODEBIAS_HALFWIDTHALPHANUMERIC: UInt32 = 12
IMF_SMODE_PLAURALCLAUSE: UInt32 = 1
IMF_SMODE_NONE: UInt32 = 2
EMO_EXIT: UInt32 = 0
EMO_ENTER: UInt32 = 1
EMO_PROMOTE: UInt32 = 2
EMO_EXPAND: UInt32 = 3
EMO_MOVESELECTION: UInt32 = 4
EMO_GETVIEWMODE: UInt32 = 5
EMO_EXPANDSELECTION: UInt32 = 0
EMO_EXPANDDOCUMENT: UInt32 = 1
VM_NORMAL: UInt32 = 4
VM_OUTLINE: UInt32 = 2
VM_PAGE: UInt32 = 9
EM_INSERTTABLE: UInt32 = 1256
EM_GETAUTOCORRECTPROC: UInt32 = 1257
EM_SETAUTOCORRECTPROC: UInt32 = 1258
EM_CALLAUTOCORRECTPROC: UInt32 = 1279
ATP_NOCHANGE: UInt32 = 0
ATP_CHANGE: UInt32 = 1
ATP_NODELIMITER: UInt32 = 2
ATP_REPLACEALLTEXT: UInt32 = 4
EM_GETTABLEPARMS: UInt32 = 1289
EM_SETEDITSTYLEEX: UInt32 = 1299
EM_GETEDITSTYLEEX: UInt32 = 1300
SES_EX_NOTABLE: UInt32 = 4
SES_EX_NOMATH: UInt32 = 64
SES_EX_HANDLEFRIENDLYURL: UInt32 = 256
SES_EX_NOTHEMING: UInt32 = 524288
SES_EX_NOACETATESELECTION: UInt32 = 1048576
SES_EX_USESINGLELINE: UInt32 = 2097152
SES_EX_MULTITOUCH: UInt32 = 134217728
SES_EX_HIDETEMPFORMAT: UInt32 = 268435456
SES_EX_USEMOUSEWPARAM: UInt32 = 536870912
EM_GETSTORYTYPE: UInt32 = 1314
EM_SETSTORYTYPE: UInt32 = 1315
EM_GETELLIPSISMODE: UInt32 = 1329
EM_SETELLIPSISMODE: UInt32 = 1330
ELLIPSIS_MASK: UInt32 = 3
ELLIPSIS_NONE: UInt32 = 0
ELLIPSIS_END: UInt32 = 1
ELLIPSIS_WORD: UInt32 = 3
EM_SETTABLEPARMS: UInt32 = 1331
EM_GETTOUCHOPTIONS: UInt32 = 1334
EM_SETTOUCHOPTIONS: UInt32 = 1335
EM_INSERTIMAGE: UInt32 = 1338
EM_SETUIANAME: UInt32 = 1344
EM_GETELLIPSISSTATE: UInt32 = 1346
RTO_SHOWHANDLES: UInt32 = 1
RTO_DISABLEHANDLES: UInt32 = 2
RTO_READINGMODE: UInt32 = 3
EN_MSGFILTER: UInt32 = 1792
EN_REQUESTRESIZE: UInt32 = 1793
EN_SELCHANGE: UInt32 = 1794
EN_DROPFILES: UInt32 = 1795
EN_PROTECTED: UInt32 = 1796
EN_CORRECTTEXT: UInt32 = 1797
EN_STOPNOUNDO: UInt32 = 1798
EN_IMECHANGE: UInt32 = 1799
EN_SAVECLIPBOARD: UInt32 = 1800
EN_OLEOPFAILED: UInt32 = 1801
EN_OBJECTPOSITIONS: UInt32 = 1802
EN_LINK: UInt32 = 1803
EN_DRAGDROPDONE: UInt32 = 1804
EN_PARAGRAPHEXPANDED: UInt32 = 1805
EN_PAGECHANGE: UInt32 = 1806
EN_LOWFIRTF: UInt32 = 1807
EN_ALIGNLTR: UInt32 = 1808
EN_ALIGNRTL: UInt32 = 1809
EN_CLIPFORMAT: UInt32 = 1810
EN_STARTCOMPOSITION: UInt32 = 1811
EN_ENDCOMPOSITION: UInt32 = 1812
ENM_NONE: UInt32 = 0
ENM_CHANGE: UInt32 = 1
ENM_UPDATE: UInt32 = 2
ENM_SCROLL: UInt32 = 4
ENM_SCROLLEVENTS: UInt32 = 8
ENM_DRAGDROPDONE: UInt32 = 16
ENM_PARAGRAPHEXPANDED: UInt32 = 32
ENM_PAGECHANGE: UInt32 = 64
ENM_CLIPFORMAT: UInt32 = 128
ENM_KEYEVENTS: UInt32 = 65536
ENM_MOUSEEVENTS: UInt32 = 131072
ENM_REQUESTRESIZE: UInt32 = 262144
ENM_SELCHANGE: UInt32 = 524288
ENM_DROPFILES: UInt32 = 1048576
ENM_PROTECTED: UInt32 = 2097152
ENM_CORRECTTEXT: UInt32 = 4194304
ENM_IMECHANGE: UInt32 = 8388608
ENM_LANGCHANGE: UInt32 = 16777216
ENM_OBJECTPOSITIONS: UInt32 = 33554432
ENM_LINK: UInt32 = 67108864
ENM_LOWFIRTF: UInt32 = 134217728
ENM_STARTCOMPOSITION: UInt32 = 268435456
ENM_ENDCOMPOSITION: UInt32 = 536870912
ENM_GROUPTYPINGCHANGE: UInt32 = 1073741824
ENM_HIDELINKTOOLTIP: UInt32 = 2147483648
ES_SAVESEL: UInt32 = 32768
ES_SUNKEN: UInt32 = 16384
ES_DISABLENOSCROLL: UInt32 = 8192
ES_SELECTIONBAR: UInt32 = 16777216
ES_NOOLEDRAGDROP: UInt32 = 8
ES_EX_NOCALLOLEINIT: UInt32 = 0
ES_VERTICAL: UInt32 = 4194304
ES_NOIME: UInt32 = 524288
ES_SELFIME: UInt32 = 262144
ECO_AUTOWORDSELECTION: UInt32 = 1
ECO_AUTOVSCROLL: UInt32 = 64
ECO_AUTOHSCROLL: UInt32 = 128
ECO_NOHIDESEL: UInt32 = 256
ECO_READONLY: UInt32 = 2048
ECO_WANTRETURN: UInt32 = 4096
ECO_SAVESEL: UInt32 = 32768
ECO_SELECTIONBAR: UInt32 = 16777216
ECO_VERTICAL: UInt32 = 4194304
ECOOP_SET: UInt32 = 1
ECOOP_OR: UInt32 = 2
ECOOP_AND: UInt32 = 3
ECOOP_XOR: UInt32 = 4
WB_MOVEWORDPREV: UInt32 = 4
WB_MOVEWORDNEXT: UInt32 = 5
WB_PREVBREAK: UInt32 = 6
WB_NEXTBREAK: UInt32 = 7
PC_FOLLOWING: UInt32 = 1
PC_LEADING: UInt32 = 2
PC_OVERFLOW: UInt32 = 3
PC_DELIMITER: UInt32 = 4
WBF_WORDWRAP: UInt32 = 16
WBF_WORDBREAK: UInt32 = 32
WBF_OVERFLOW: UInt32 = 64
WBF_LEVEL1: UInt32 = 128
WBF_LEVEL2: UInt32 = 256
WBF_CUSTOM: UInt32 = 512
IMF_FORCENONE: UInt32 = 1
IMF_FORCEENABLE: UInt32 = 2
IMF_FORCEDISABLE: UInt32 = 4
IMF_CLOSESTATUSWINDOW: UInt32 = 8
IMF_VERTICAL: UInt32 = 32
IMF_FORCEACTIVE: UInt32 = 64
IMF_FORCEINACTIVE: UInt32 = 128
IMF_FORCEREMEMBER: UInt32 = 256
IMF_MULTIPLEEDIT: UInt32 = 1024
yHeightCharPtsMost: UInt32 = 1638
SCF_SELECTION: UInt32 = 1
SCF_WORD: UInt32 = 2
SCF_DEFAULT: UInt32 = 0
SCF_ALL: UInt32 = 4
SCF_USEUIRULES: UInt32 = 8
SCF_ASSOCIATEFONT: UInt32 = 16
SCF_NOKBUPDATE: UInt32 = 32
SCF_ASSOCIATEFONT2: UInt32 = 64
SCF_SMARTFONT: UInt32 = 128
SCF_CHARREPFROMLCID: UInt32 = 256
SPF_DONTSETDEFAULT: UInt32 = 2
SPF_SETDEFAULT: UInt32 = 4
SF_TEXT: UInt32 = 1
SF_RTF: UInt32 = 2
SF_RTFNOOBJS: UInt32 = 3
SF_TEXTIZED: UInt32 = 4
SF_UNICODE: UInt32 = 16
SF_USECODEPAGE: UInt32 = 32
SF_NCRFORNONASCII: UInt32 = 64
SFF_WRITEXTRAPAR: UInt32 = 128
SFF_SELECTION: UInt32 = 32768
SFF_PLAINRTF: UInt32 = 16384
SFF_PERSISTVIEWSCALE: UInt32 = 8192
SFF_KEEPDOCINFO: UInt32 = 4096
SFF_PWD: UInt32 = 2048
SF_RTFVAL: UInt32 = 1792
MAX_TAB_STOPS: UInt32 = 32
lDefaultTab: UInt32 = 720
MAX_TABLE_CELLS: UInt32 = 63
PFM_SPACEBEFORE: UInt32 = 64
PFM_SPACEAFTER: UInt32 = 128
PFM_LINESPACING: UInt32 = 256
PFM_STYLE: UInt32 = 1024
PFM_BORDER: UInt32 = 2048
PFM_SHADING: UInt32 = 4096
PFM_NUMBERINGSTYLE: UInt32 = 8192
PFM_NUMBERINGTAB: UInt32 = 16384
PFM_NUMBERINGSTART: UInt32 = 32768
PFM_KEEP: UInt32 = 131072
PFM_KEEPNEXT: UInt32 = 262144
PFM_PAGEBREAKBEFORE: UInt32 = 524288
PFM_NOLINENUMBER: UInt32 = 1048576
PFM_NOWIDOWCONTROL: UInt32 = 2097152
PFM_DONOTHYPHEN: UInt32 = 4194304
PFM_SIDEBYSIDE: UInt32 = 8388608
PFM_COLLAPSED: UInt32 = 16777216
PFM_OUTLINELEVEL: UInt32 = 33554432
PFM_BOX: UInt32 = 67108864
PFM_RESERVED2: UInt32 = 134217728
PFM_TABLEROWDELIMITER: UInt32 = 268435456
PFM_TEXTWRAPPINGBREAK: UInt32 = 536870912
PFM_TABLE: UInt32 = 1073741824
PFA_JUSTIFY: UInt32 = 4
PFA_FULL_INTERWORD: UInt32 = 4
GCMF_GRIPPER: UInt32 = 1
GCMF_SPELLING: UInt32 = 2
GCMF_TOUCHMENU: UInt32 = 16384
GCMF_MOUSEMENU: UInt32 = 8192
OLEOP_DOVERB: UInt32 = 1
CF_RTF: String = 'Rich Text Format'
CF_RTFNOOBJS: String = 'Rich Text Format Without Objects'
CF_RETEXTOBJ: String = 'RichEdit Text and Objects'
ST_DEFAULT: UInt32 = 0
ST_KEEPUNDO: UInt32 = 1
ST_SELECTION: UInt32 = 2
ST_NEWCHARS: UInt32 = 4
ST_UNICODE: UInt32 = 8
BOM_DEFPARADIR: UInt32 = 1
BOM_PLAINTEXT: UInt32 = 2
BOM_NEUTRALOVERRIDE: UInt32 = 4
BOM_CONTEXTREADING: UInt32 = 8
BOM_CONTEXTALIGNMENT: UInt32 = 16
BOM_LEGACYBIDICLASS: UInt32 = 64
BOM_UNICODEBIDI: UInt32 = 128
BOE_RTLDIR: UInt32 = 1
BOE_PLAINTEXT: UInt32 = 2
BOE_NEUTRALOVERRIDE: UInt32 = 4
BOE_CONTEXTREADING: UInt32 = 8
BOE_CONTEXTALIGNMENT: UInt32 = 16
BOE_FORCERECALC: UInt32 = 32
BOE_LEGACYBIDICLASS: UInt32 = 64
BOE_UNICODEBIDI: UInt32 = 128
FR_MATCHDIAC: UInt32 = 536870912
FR_MATCHKASHIDA: UInt32 = 1073741824
FR_MATCHALEFHAMZA: UInt32 = 2147483648
RICHEDIT60_CLASS: String = 'RICHEDIT60W'
PFA_FULL_NEWSPAPER: UInt32 = 5
PFA_FULL_INTERLETTER: UInt32 = 6
PFA_FULL_SCALED: UInt32 = 7
PFA_FULL_GLYPHS: UInt32 = 8
AURL_ENABLEEA: UInt32 = 1
GCM_TOUCHMENU: UInt32 = 16384
GCM_MOUSEMENU: UInt32 = 8192
S_MSG_KEY_IGNORED: win32more.Foundation.HRESULT = 262657
TXTBIT_RICHTEXT: UInt32 = 1
TXTBIT_MULTILINE: UInt32 = 2
TXTBIT_READONLY: UInt32 = 4
TXTBIT_SHOWACCELERATOR: UInt32 = 8
TXTBIT_USEPASSWORD: UInt32 = 16
TXTBIT_HIDESELECTION: UInt32 = 32
TXTBIT_SAVESELECTION: UInt32 = 64
TXTBIT_AUTOWORDSEL: UInt32 = 128
TXTBIT_VERTICAL: UInt32 = 256
TXTBIT_SELBARCHANGE: UInt32 = 512
TXTBIT_WORDWRAP: UInt32 = 1024
TXTBIT_ALLOWBEEP: UInt32 = 2048
TXTBIT_DISABLEDRAG: UInt32 = 4096
TXTBIT_VIEWINSETCHANGE: UInt32 = 8192
TXTBIT_BACKSTYLECHANGE: UInt32 = 16384
TXTBIT_MAXLENGTHCHANGE: UInt32 = 32768
TXTBIT_SCROLLBARCHANGE: UInt32 = 65536
TXTBIT_CHARFORMATCHANGE: UInt32 = 131072
TXTBIT_PARAFORMATCHANGE: UInt32 = 262144
TXTBIT_EXTENTCHANGE: UInt32 = 524288
TXTBIT_CLIENTRECTCHANGE: UInt32 = 1048576
TXTBIT_USECURRENTBKG: UInt32 = 2097152
TXTBIT_NOTHREADREFCOUNT: UInt32 = 4194304
TXTBIT_SHOWPASSWORD: UInt32 = 8388608
TXTBIT_D2DDWRITE: UInt32 = 16777216
TXTBIT_D2DSIMPLETYPOGRAPHY: UInt32 = 33554432
TXTBIT_D2DPIXELSNAPPED: UInt32 = 67108864
TXTBIT_D2DSUBPIXELLINES: UInt32 = 134217728
TXTBIT_FLASHLASTPASSWORDCHAR: UInt32 = 268435456
TXTBIT_ADVANCEDINPUT: UInt32 = 536870912
TXES_ISDIALOG: UInt32 = 1
REO_NULL: Int32 = 0
REO_READWRITEMASK: Int32 = 2047
@winfunctype_pointer
def AutoCorrectProc(langid: UInt16, pszBefore: win32more.Foundation.PWSTR, pszAfter: win32more.Foundation.PWSTR, cchAfter: Int32, pcchReplaced: POINTER(Int32)) -> Int32: ...
class BIDIOPTIONS(Structure):
    cbSize: UInt32
    wMask: UInt16
    wEffects: UInt16
CARET_FLAGS = Int32
CARET_NONE: CARET_FLAGS = 0
CARET_CUSTOM: CARET_FLAGS = 1
CARET_RTL: CARET_FLAGS = 2
CARET_ITALIC: CARET_FLAGS = 32
CARET_NULL: CARET_FLAGS = 64
CARET_ROTATE90: CARET_FLAGS = 128
class CARET_INFO(Union):
    hbitmap: win32more.Graphics.Gdi.HBITMAP
    caretFlags: win32more.UI.Controls.RichEdit.CARET_FLAGS
CFE_EFFECTS = UInt32
CFE_ALLCAPS: CFE_EFFECTS = 128
CFE_AUTOBACKCOLOR: CFE_EFFECTS = 67108864
CFE_DISABLED: CFE_EFFECTS = 8192
CFE_EMBOSS: CFE_EFFECTS = 2048
CFE_HIDDEN: CFE_EFFECTS = 256
CFE_IMPRINT: CFE_EFFECTS = 4096
CFE_OUTLINE: CFE_EFFECTS = 512
CFE_REVISED: CFE_EFFECTS = 16384
CFE_SHADOW: CFE_EFFECTS = 1024
CFE_SMALLCAPS: CFE_EFFECTS = 64
CFE_AUTOCOLOR: CFE_EFFECTS = 1073741824
CFE_BOLD: CFE_EFFECTS = 1
CFE_ITALIC: CFE_EFFECTS = 2
CFE_STRIKEOUT: CFE_EFFECTS = 8
CFE_UNDERLINE: CFE_EFFECTS = 4
CFE_PROTECTED: CFE_EFFECTS = 16
CFE_LINK: CFE_EFFECTS = 32
CFE_SUBSCRIPT: CFE_EFFECTS = 65536
CFE_SUPERSCRIPT: CFE_EFFECTS = 131072
CFE_FONTBOUND: CFE_EFFECTS = 1048576
CFE_LINKPROTECTED: CFE_EFFECTS = 8388608
CFE_EXTENDED: CFE_EFFECTS = 33554432
CFE_MATHNOBUILDUP: CFE_EFFECTS = 134217728
CFE_MATH: CFE_EFFECTS = 268435456
CFE_MATHORDINARY: CFE_EFFECTS = 536870912
CFM_MASK = UInt32
CFM_SUBSCRIPT: CFM_MASK = 196608
CFM_SUPERSCRIPT: CFM_MASK = 196608
CFM_EFFECTS: CFM_MASK = 1073741887
CFM_ALL: CFM_MASK = 4160749631
CFM_BOLD: CFM_MASK = 1
CFM_CHARSET: CFM_MASK = 134217728
CFM_COLOR: CFM_MASK = 1073741824
CFM_FACE: CFM_MASK = 536870912
CFM_ITALIC: CFM_MASK = 2
CFM_OFFSET: CFM_MASK = 268435456
CFM_PROTECTED: CFM_MASK = 16
CFM_SIZE: CFM_MASK = 2147483648
CFM_STRIKEOUT: CFM_MASK = 8
CFM_UNDERLINE: CFM_MASK = 4
CFM_LINK: CFM_MASK = 32
CFM_SMALLCAPS: CFM_MASK = 64
CFM_ALLCAPS: CFM_MASK = 128
CFM_HIDDEN: CFM_MASK = 256
CFM_OUTLINE: CFM_MASK = 512
CFM_SHADOW: CFM_MASK = 1024
CFM_EMBOSS: CFM_MASK = 2048
CFM_IMPRINT: CFM_MASK = 4096
CFM_DISABLED: CFM_MASK = 8192
CFM_REVISED: CFM_MASK = 16384
CFM_REVAUTHOR: CFM_MASK = 32768
CFM_ANIMATION: CFM_MASK = 262144
CFM_STYLE: CFM_MASK = 524288
CFM_KERNING: CFM_MASK = 1048576
CFM_SPACING: CFM_MASK = 2097152
CFM_WEIGHT: CFM_MASK = 4194304
CFM_UNDERLINETYPE: CFM_MASK = 8388608
CFM_COOKIE: CFM_MASK = 16777216
CFM_LCID: CFM_MASK = 33554432
CFM_BACKCOLOR: CFM_MASK = 67108864
CFM_EFFECTS2: CFM_MASK = 1141080063
CFM_ALL2: CFM_MASK = 4294967295
CFM_FONTBOUND: CFM_MASK = 1048576
CFM_LINKPROTECTED: CFM_MASK = 8388608
CFM_EXTENDED: CFM_MASK = 33554432
CFM_MATHNOBUILDUP: CFM_MASK = 134217728
CFM_MATH: CFM_MASK = 268435456
CFM_MATHORDINARY: CFM_MASK = 536870912
CFM_ALLEFFECTS: CFM_MASK = 2115207167
class CHANGENOTIFY(Structure):
    dwChangeType: win32more.UI.Controls.RichEdit.CHANGETYPE
    pvCookieData: c_void_p
CHANGETYPE = Int32
CN_GENERIC: CHANGETYPE = 0
CN_TEXTCHANGED: CHANGETYPE = 1
CN_NEWUNDO: CHANGETYPE = 2
CN_NEWREDO: CHANGETYPE = 4
class CHARFORMAT2A(Structure):
    Base: win32more.UI.Controls.RichEdit.CHARFORMATA
    wWeight: UInt16
    sSpacing: Int16
    crBackColor: win32more.Foundation.COLORREF
    lcid: UInt32
    Anonymous: _Anonymous_e__Union
    sStyle: Int16
    wKerning: UInt16
    bUnderlineType: Byte
    bAnimation: Byte
    bRevAuthor: Byte
    bUnderlineColor: Byte
    class _Anonymous_e__Union(Union):
        dwReserved: UInt32
        dwCookie: UInt32
class CHARFORMAT2W(Structure):
    Base: win32more.UI.Controls.RichEdit.CHARFORMATW
    wWeight: UInt16
    sSpacing: Int16
    crBackColor: win32more.Foundation.COLORREF
    lcid: UInt32
    Anonymous: _Anonymous_e__Union
    sStyle: Int16
    wKerning: UInt16
    bUnderlineType: Byte
    bAnimation: Byte
    bRevAuthor: Byte
    bUnderlineColor: Byte
    class _Anonymous_e__Union(Union):
        dwReserved: UInt32
        dwCookie: UInt32
class CHARFORMATA(Structure):
    cbSize: UInt32
    dwMask: win32more.UI.Controls.RichEdit.CFM_MASK
    dwEffects: win32more.UI.Controls.RichEdit.CFE_EFFECTS
    yHeight: Int32
    yOffset: Int32
    crTextColor: win32more.Foundation.COLORREF
    bCharSet: win32more.Graphics.Gdi.EMBED_FONT_CHARSET
    bPitchAndFamily: Byte
    szFaceName: win32more.Foundation.CHAR * 32
class CHARFORMATW(Structure):
    cbSize: UInt32
    dwMask: win32more.UI.Controls.RichEdit.CFM_MASK
    dwEffects: win32more.UI.Controls.RichEdit.CFE_EFFECTS
    yHeight: Int32
    yOffset: Int32
    crTextColor: win32more.Foundation.COLORREF
    bCharSet: win32more.Graphics.Gdi.EMBED_FONT_CHARSET
    bPitchAndFamily: Byte
    szFaceName: Char * 32
class CHARRANGE(Structure):
    cpMin: Int32
    cpMax: Int32
class CLIPBOARDFORMAT(Structure):
    nmhdr: win32more.UI.Controls.NMHDR
    cf: UInt16
    _pack_ = 4
class COMPCOLOR(Structure):
    crText: win32more.Foundation.COLORREF
    crBackground: win32more.Foundation.COLORREF
    dwEffects: UInt32
class EDITSTREAM(Structure):
    dwCookie: UIntPtr
    dwError: UInt32
    pfnCallback: win32more.UI.Controls.RichEdit.EDITSTREAMCALLBACK
    _pack_ = 4
@winfunctype_pointer
def EDITSTREAMCALLBACK(dwCookie: UIntPtr, pbBuff: c_char_p_no, cb: Int32, pcb: POINTER(Int32)) -> UInt32: ...
@winfunctype_pointer
def EDITWORDBREAKPROCEX(pchText: win32more.Foundation.PSTR, cchText: Int32, bCharSet: Byte, action: Int32) -> Int32: ...
class ENCORRECTTEXT(Structure):
    nmhdr: win32more.UI.Controls.NMHDR
    chrg: win32more.UI.Controls.RichEdit.CHARRANGE
    seltyp: win32more.UI.Controls.RichEdit.RICH_EDIT_GET_CONTEXT_MENU_SEL_TYPE
    _pack_ = 4
class ENDCOMPOSITIONNOTIFY(Structure):
    nmhdr: win32more.UI.Controls.NMHDR
    dwCode: win32more.UI.Controls.RichEdit.ENDCOMPOSITIONNOTIFY_CODE
    _pack_ = 4
ENDCOMPOSITIONNOTIFY_CODE = UInt32
ECN_ENDCOMPOSITION: ENDCOMPOSITIONNOTIFY_CODE = 1
ECN_NEWTEXT: ENDCOMPOSITIONNOTIFY_CODE = 2
class ENDROPFILES(Structure):
    nmhdr: win32more.UI.Controls.NMHDR
    hDrop: win32more.Foundation.HANDLE
    cp: Int32
    fProtected: win32more.Foundation.BOOL
    _pack_ = 4
class ENLINK(Structure):
    nmhdr: win32more.UI.Controls.NMHDR
    msg: UInt32
    wParam: win32more.Foundation.WPARAM
    lParam: win32more.Foundation.LPARAM
    chrg: win32more.UI.Controls.RichEdit.CHARRANGE
    _pack_ = 4
class ENLOWFIRTF(Structure):
    nmhdr: win32more.UI.Controls.NMHDR
    szControl: win32more.Foundation.PSTR
    _pack_ = 4
class ENOLEOPFAILED(Structure):
    nmhdr: win32more.UI.Controls.NMHDR
    iob: Int32
    lOper: Int32
    hr: win32more.Foundation.HRESULT
    _pack_ = 4
class ENPROTECTED(Structure):
    nmhdr: win32more.UI.Controls.NMHDR
    msg: UInt32
    wParam: win32more.Foundation.WPARAM
    lParam: win32more.Foundation.LPARAM
    chrg: win32more.UI.Controls.RichEdit.CHARRANGE
    _pack_ = 4
class ENSAVECLIPBOARD(Structure):
    nmhdr: win32more.UI.Controls.NMHDR
    cObjectCount: Int32
    cch: Int32
    _pack_ = 4
class FINDTEXTA(Structure):
    chrg: win32more.UI.Controls.RichEdit.CHARRANGE
    lpstrText: win32more.Foundation.PSTR
    _pack_ = 4
class FINDTEXTEXA(Structure):
    chrg: win32more.UI.Controls.RichEdit.CHARRANGE
    lpstrText: win32more.Foundation.PSTR
    chrgText: win32more.UI.Controls.RichEdit.CHARRANGE
    _pack_ = 4
class FINDTEXTEXW(Structure):
    chrg: win32more.UI.Controls.RichEdit.CHARRANGE
    lpstrText: win32more.Foundation.PWSTR
    chrgText: win32more.UI.Controls.RichEdit.CHARRANGE
    _pack_ = 4
class FINDTEXTW(Structure):
    chrg: win32more.UI.Controls.RichEdit.CHARRANGE
    lpstrText: win32more.Foundation.PWSTR
    _pack_ = 4
class FORMATRANGE(Structure):
    hdc: win32more.Graphics.Gdi.HDC
    hdcTarget: win32more.Graphics.Gdi.HDC
    rc: win32more.Foundation.RECT
    rcPage: win32more.Foundation.RECT
    chrg: win32more.UI.Controls.RichEdit.CHARRANGE
    _pack_ = 4
class GETCONTEXTMENUEX(Structure):
    chrg: win32more.UI.Controls.RichEdit.CHARRANGE
    dwFlags: UInt32
    pt: win32more.Foundation.POINT
    pvReserved: c_void_p
    _pack_ = 4
class GETTEXTEX(Structure):
    cb: UInt32
    flags: win32more.UI.Controls.RichEdit.GETTEXTEX_FLAGS
    codepage: UInt32
    lpDefaultChar: win32more.Foundation.PSTR
    lpUsedDefChar: POINTER(Int32)
    _pack_ = 4
GETTEXTEX_FLAGS = UInt32
GT_DEFAULT: GETTEXTEX_FLAGS = 0
GT_NOHIDDENTEXT: GETTEXTEX_FLAGS = 8
GT_RAWTEXT: GETTEXTEX_FLAGS = 4
GT_SELECTION: GETTEXTEX_FLAGS = 2
GT_USECRLF: GETTEXTEX_FLAGS = 1
class GETTEXTLENGTHEX(Structure):
    flags: win32more.UI.Controls.RichEdit.GETTEXTLENGTHEX_FLAGS
    codepage: UInt32
GETTEXTLENGTHEX_FLAGS = UInt32
GTL_DEFAULT: GETTEXTLENGTHEX_FLAGS = 0
GTL_USECRLF: GETTEXTLENGTHEX_FLAGS = 1
GTL_PRECISE: GETTEXTLENGTHEX_FLAGS = 2
GTL_CLOSE: GETTEXTLENGTHEX_FLAGS = 4
GTL_NUMCHARS: GETTEXTLENGTHEX_FLAGS = 8
GTL_NUMBYTES: GETTEXTLENGTHEX_FLAGS = 16
class GROUPTYPINGCHANGE(Structure):
    nmhdr: win32more.UI.Controls.NMHDR
    fGroupTyping: win32more.Foundation.BOOL
    _pack_ = 4
class HYPHENATEINFO(Structure):
    cbSize: Int16
    dxHyphenateZone: Int16
    pfnHyphenate: IntPtr
    _pack_ = 4
class HYPHRESULT(Structure):
    khyph: win32more.UI.Controls.RichEdit.KHYPH
    ichHyph: Int32
    chHyph: Char
class IMECOMPTEXT(Structure):
    cb: Int32
    flags: win32more.UI.Controls.RichEdit.IMECOMPTEXT_FLAGS
IMECOMPTEXT_FLAGS = UInt32
ICT_RESULTREADSTR: IMECOMPTEXT_FLAGS = 1
class IRichEditOle(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00020d00-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def GetClientSite(lplpolesite: POINTER(win32more.System.Ole.IOleClientSite_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetObjectCount() -> Int32: ...
    @commethod(5)
    def GetLinkCount() -> Int32: ...
    @commethod(6)
    def GetObject(iob: Int32, lpreobject: POINTER(win32more.UI.Controls.RichEdit.REOBJECT_head), dwFlags: win32more.UI.Controls.RichEdit.RICH_EDIT_GET_OBJECT_FLAGS) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def InsertObject(lpreobject: POINTER(win32more.UI.Controls.RichEdit.REOBJECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def ConvertObject(iob: Int32, rclsidNew: POINTER(Guid), lpstrUserTypeNew: win32more.Foundation.PSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def ActivateAs(rclsid: POINTER(Guid), rclsidAs: POINTER(Guid)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetHostNames(lpstrContainerApp: win32more.Foundation.PSTR, lpstrContainerObj: win32more.Foundation.PSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SetLinkAvailable(iob: Int32, fAvailable: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def SetDvaspect(iob: Int32, dvaspect: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def HandsOffStorage(iob: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SaveCompleted(iob: Int32, lpstg: win32more.System.Com.StructuredStorage.IStorage_head) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def InPlaceDeactivate() -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def ContextSensitiveHelp(fEnterMode: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetClipboardData(lpchrg: POINTER(win32more.UI.Controls.RichEdit.CHARRANGE_head), reco: UInt32, lplpdataobj: POINTER(win32more.System.Com.IDataObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def ImportDataObject(lpdataobj: win32more.System.Com.IDataObject_head, cf: UInt16, hMetaPict: IntPtr) -> win32more.Foundation.HRESULT: ...
class IRichEditOleCallback(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('00020d03-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def GetNewStorage(lplpstg: POINTER(win32more.System.Com.StructuredStorage.IStorage_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetInPlaceContext(lplpFrame: POINTER(win32more.System.Ole.IOleInPlaceFrame_head), lplpDoc: POINTER(win32more.System.Ole.IOleInPlaceUIWindow_head), lpFrameInfo: POINTER(win32more.System.Ole.OLEINPLACEFRAMEINFO_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def ShowContainerUI(fShow: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def QueryInsertObject(lpclsid: POINTER(Guid), lpstg: win32more.System.Com.StructuredStorage.IStorage_head, cp: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def DeleteObject(lpoleobj: win32more.System.Ole.IOleObject_head) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def QueryAcceptData(lpdataobj: win32more.System.Com.IDataObject_head, lpcfFormat: POINTER(UInt16), reco: win32more.System.SystemServices.RECO_FLAGS, fReally: win32more.Foundation.BOOL, hMetaPict: IntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def ContextSensitiveHelp(fEnterMode: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetClipboardData(lpchrg: POINTER(win32more.UI.Controls.RichEdit.CHARRANGE_head), reco: UInt32, lplpdataobj: POINTER(win32more.System.Com.IDataObject_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetDragDropEffect(fDrag: win32more.Foundation.BOOL, grfKeyState: win32more.System.SystemServices.MODIFIERKEYS_FLAGS, pdwEffect: POINTER(win32more.System.Ole.DROPEFFECT)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetContextMenu(seltype: win32more.UI.Controls.RichEdit.RICH_EDIT_GET_CONTEXT_MENU_SEL_TYPE, lpoleobj: win32more.System.Ole.IOleObject_head, lpchrg: POINTER(win32more.UI.Controls.RichEdit.CHARRANGE_head), lphmenu: POINTER(win32more.UI.WindowsAndMessaging.HMENU)) -> win32more.Foundation.HRESULT: ...
class IRicheditUiaOverrides(c_void_p):
    extends: win32more.System.Com.IUnknown
    @commethod(3)
    def GetPropertyOverrideValue(propertyId: Int32, pRetValue: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
class ITextDisplays(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('c241f5f2-7206-11d8-a2-c7-00-a0-d1-d6-c6-b3')
class ITextDocument(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('8cc497c0-a1df-11ce-80-98-00-aa-00-47-be-5d')
    @commethod(7)
    def GetName(pName: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetSelection(ppSel: POINTER(win32more.UI.Controls.RichEdit.ITextSelection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetStoryCount(pCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetStoryRanges(ppStories: POINTER(win32more.UI.Controls.RichEdit.ITextStoryRanges_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetSaved(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def SetSaved(Value: win32more.UI.Controls.RichEdit.tomConstants) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetDefaultTabStop(pValue: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetDefaultTabStop(Value: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def New() -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def Open(pVar: POINTER(win32more.System.Com.VARIANT_head), Flags: win32more.UI.Controls.RichEdit.tomConstants, CodePage: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def Save(pVar: POINTER(win32more.System.Com.VARIANT_head), Flags: win32more.UI.Controls.RichEdit.tomConstants, CodePage: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def Freeze(pCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def Unfreeze(pCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def BeginEditCollection() -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def EndEditCollection() -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def Undo(Count: Int32, pCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def Redo(Count: Int32, pCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def Range(cpActive: Int32, cpAnchor: Int32, ppRange: POINTER(win32more.UI.Controls.RichEdit.ITextRange_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def RangeFromPoint(x: Int32, y: Int32, ppRange: POINTER(win32more.UI.Controls.RichEdit.ITextRange_head)) -> win32more.Foundation.HRESULT: ...
class ITextDocument2(c_void_p):
    extends: win32more.UI.Controls.RichEdit.ITextDocument
    Guid = Guid('c241f5e0-7206-11d8-a2-c7-00-a0-d1-d6-c6-b3')
    @commethod(26)
    def GetCaretType(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def SetCaretType(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def GetDisplays(ppDisplays: POINTER(win32more.UI.Controls.RichEdit.ITextDisplays_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def GetDocumentFont(ppFont: POINTER(win32more.UI.Controls.RichEdit.ITextFont2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def SetDocumentFont(pFont: win32more.UI.Controls.RichEdit.ITextFont2_head) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def GetDocumentPara(ppPara: POINTER(win32more.UI.Controls.RichEdit.ITextPara2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def SetDocumentPara(pPara: win32more.UI.Controls.RichEdit.ITextPara2_head) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def GetEastAsianFlags(pFlags: POINTER(win32more.UI.Controls.RichEdit.tomConstants)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def GetGenerator(pbstr: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def SetIMEInProgress(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def GetNotificationMode(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def SetNotificationMode(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def GetSelection2(ppSel: POINTER(win32more.UI.Controls.RichEdit.ITextSelection2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def GetStoryRanges2(ppStories: POINTER(win32more.UI.Controls.RichEdit.ITextStoryRanges2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def GetTypographyOptions(pOptions: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def GetVersion(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def GetWindow(pHwnd: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def AttachMsgFilter(pFilter: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def CheckTextLimit(cch: Int32, pcch: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def GetCallManager(ppVoid: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def GetClientRect(Type: win32more.UI.Controls.RichEdit.tomConstants, pLeft: POINTER(Int32), pTop: POINTER(Int32), pRight: POINTER(Int32), pBottom: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def GetEffectColor(Index: Int32, pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def GetImmContext(pContext: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def GetPreferredFont(cp: Int32, CharRep: Int32, Options: Int32, curCharRep: Int32, curFontSize: Int32, pbstr: POINTER(win32more.Foundation.BSTR), pPitchAndFamily: POINTER(Int32), pNewFontSize: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(50)
    def GetProperty(Type: Int32, pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(51)
    def GetStrings(ppStrs: POINTER(win32more.UI.Controls.RichEdit.ITextStrings_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(52)
    def Notify(Notify: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(53)
    def Range2(cpActive: Int32, cpAnchor: Int32, ppRange: POINTER(win32more.UI.Controls.RichEdit.ITextRange2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(54)
    def RangeFromPoint2(x: Int32, y: Int32, Type: Int32, ppRange: POINTER(win32more.UI.Controls.RichEdit.ITextRange2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(55)
    def ReleaseCallManager(pVoid: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(56)
    def ReleaseImmContext(Context: Int64) -> win32more.Foundation.HRESULT: ...
    @commethod(57)
    def SetEffectColor(Index: Int32, Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(58)
    def SetProperty(Type: Int32, Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(59)
    def SetTypographyOptions(Options: Int32, Mask: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(60)
    def SysBeep() -> win32more.Foundation.HRESULT: ...
    @commethod(61)
    def Update(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(62)
    def UpdateWindow() -> win32more.Foundation.HRESULT: ...
    @commethod(63)
    def GetMathProperties(pOptions: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(64)
    def SetMathProperties(Options: Int32, Mask: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(65)
    def GetActiveStory(ppStory: POINTER(win32more.UI.Controls.RichEdit.ITextStory_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(66)
    def SetActiveStory(pStory: win32more.UI.Controls.RichEdit.ITextStory_head) -> win32more.Foundation.HRESULT: ...
    @commethod(67)
    def GetMainStory(ppStory: POINTER(win32more.UI.Controls.RichEdit.ITextStory_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(68)
    def GetNewStory(ppStory: POINTER(win32more.UI.Controls.RichEdit.ITextStory_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(69)
    def GetStory(Index: Int32, ppStory: POINTER(win32more.UI.Controls.RichEdit.ITextStory_head)) -> win32more.Foundation.HRESULT: ...
class ITextDocument2Old(c_void_p):
    extends: win32more.UI.Controls.RichEdit.ITextDocument
    Guid = Guid('01c25500-4268-11d1-88-3a-3c-8b-00-c1-00-00')
    @commethod(26)
    def AttachMsgFilter(pFilter: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def SetEffectColor(Index: Int32, cr: win32more.Foundation.COLORREF) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def GetEffectColor(Index: Int32, pcr: POINTER(win32more.Foundation.COLORREF)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def GetCaretType(pCaretType: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def SetCaretType(CaretType: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def GetImmContext(pContext: POINTER(Int64)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def ReleaseImmContext(Context: Int64) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def GetPreferredFont(cp: Int32, CharRep: Int32, Option: Int32, CharRepCur: Int32, curFontSize: Int32, pbstr: POINTER(win32more.Foundation.BSTR), pPitchAndFamily: POINTER(Int32), pNewFontSize: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def GetNotificationMode(pMode: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def SetNotificationMode(Mode: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def GetClientRect(Type: Int32, pLeft: POINTER(Int32), pTop: POINTER(Int32), pRight: POINTER(Int32), pBottom: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def GetSelection2(ppSel: POINTER(win32more.UI.Controls.RichEdit.ITextSelection_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def GetWindow(phWnd: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def GetFEFlags(pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def UpdateWindow() -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def CheckTextLimit(cch: Int32, pcch: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def IMEInProgress(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def SysBeep() -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def Update(Mode: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def Notify(Notify: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def GetDocumentFont(ppITextFont: POINTER(win32more.UI.Controls.RichEdit.ITextFont_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def GetDocumentPara(ppITextPara: POINTER(win32more.UI.Controls.RichEdit.ITextPara_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def GetCallManager(ppVoid: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def ReleaseCallManager(pVoid: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
class ITextFont(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('8cc497c3-a1df-11ce-80-98-00-aa-00-47-be-5d')
    @commethod(7)
    def GetDuplicate(ppFont: POINTER(win32more.UI.Controls.RichEdit.ITextFont_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetDuplicate(pFont: win32more.UI.Controls.RichEdit.ITextFont_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def CanChange(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def IsEqual(pFont: win32more.UI.Controls.RichEdit.ITextFont_head, pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Reset(Value: win32more.UI.Controls.RichEdit.tomConstants) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetStyle(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def SetStyle(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetAllCaps(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def SetAllCaps(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetAnimation(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def SetAnimation(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetBackColor(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def SetBackColor(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def GetBold(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def SetBold(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def GetEmboss(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def SetEmboss(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def GetForeColor(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def SetForeColor(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def GetHidden(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def SetHidden(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def GetEngrave(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def SetEngrave(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def GetItalic(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def SetItalic(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def GetKerning(pValue: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def SetKerning(Value: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def GetLanguageID(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def SetLanguageID(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def GetName(pbstr: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def SetName(bstr: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def GetOutline(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def SetOutline(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def GetPosition(pValue: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def SetPosition(Value: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def GetProtected(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def SetProtected(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def GetShadow(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def SetShadow(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def GetSize(pValue: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def SetSize(Value: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def GetSmallCaps(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def SetSmallCaps(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(50)
    def GetSpacing(pValue: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(51)
    def SetSpacing(Value: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(52)
    def GetStrikeThrough(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(53)
    def SetStrikeThrough(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(54)
    def GetSubscript(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(55)
    def SetSubscript(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(56)
    def GetSuperscript(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(57)
    def SetSuperscript(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(58)
    def GetUnderline(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(59)
    def SetUnderline(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(60)
    def GetWeight(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(61)
    def SetWeight(Value: Int32) -> win32more.Foundation.HRESULT: ...
class ITextFont2(c_void_p):
    extends: win32more.UI.Controls.RichEdit.ITextFont
    Guid = Guid('c241f5e3-7206-11d8-a2-c7-00-a0-d1-d6-c6-b3')
    @commethod(62)
    def GetCount(pCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(63)
    def GetAutoLigatures(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(64)
    def SetAutoLigatures(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(65)
    def GetAutospaceAlpha(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(66)
    def SetAutospaceAlpha(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(67)
    def GetAutospaceNumeric(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(68)
    def SetAutospaceNumeric(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(69)
    def GetAutospaceParens(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(70)
    def SetAutospaceParens(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(71)
    def GetCharRep(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(72)
    def SetCharRep(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(73)
    def GetCompressionMode(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(74)
    def SetCompressionMode(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(75)
    def GetCookie(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(76)
    def SetCookie(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(77)
    def GetDoubleStrike(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(78)
    def SetDoubleStrike(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(79)
    def GetDuplicate2(ppFont: POINTER(win32more.UI.Controls.RichEdit.ITextFont2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(80)
    def SetDuplicate2(pFont: win32more.UI.Controls.RichEdit.ITextFont2_head) -> win32more.Foundation.HRESULT: ...
    @commethod(81)
    def GetLinkType(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(82)
    def GetMathZone(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(83)
    def SetMathZone(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(84)
    def GetModWidthPairs(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(85)
    def SetModWidthPairs(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(86)
    def GetModWidthSpace(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(87)
    def SetModWidthSpace(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(88)
    def GetOldNumbers(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(89)
    def SetOldNumbers(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(90)
    def GetOverlapping(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(91)
    def SetOverlapping(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(92)
    def GetPositionSubSuper(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(93)
    def SetPositionSubSuper(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(94)
    def GetScaling(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(95)
    def SetScaling(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(96)
    def GetSpaceExtension(pValue: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(97)
    def SetSpaceExtension(Value: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(98)
    def GetUnderlinePositionMode(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(99)
    def SetUnderlinePositionMode(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(100)
    def GetEffects(pValue: POINTER(Int32), pMask: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(101)
    def GetEffects2(pValue: POINTER(Int32), pMask: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(102)
    def GetProperty(Type: Int32, pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(103)
    def GetPropertyInfo(Index: Int32, pType: POINTER(Int32), pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(104)
    def IsEqual2(pFont: win32more.UI.Controls.RichEdit.ITextFont2_head, pB: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(105)
    def SetEffects(Value: Int32, Mask: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(106)
    def SetEffects2(Value: Int32, Mask: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(107)
    def SetProperty(Type: Int32, Value: Int32) -> win32more.Foundation.HRESULT: ...
class ITextHost(c_void_p):
    extends: win32more.System.Com.IUnknown
    @commethod(3)
    def TxGetDC() -> win32more.Graphics.Gdi.HDC: ...
    @commethod(4)
    def TxReleaseDC(hdc: win32more.Graphics.Gdi.HDC) -> Int32: ...
    @commethod(5)
    def TxShowScrollBar(fnBar: Int32, fShow: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
    @commethod(6)
    def TxEnableScrollBar(fuSBFlags: win32more.UI.WindowsAndMessaging.SCROLLBAR_CONSTANTS, fuArrowflags: win32more.UI.Controls.ENABLE_SCROLL_BAR_ARROWS) -> win32more.Foundation.BOOL: ...
    @commethod(7)
    def TxSetScrollRange(fnBar: Int32, nMinPos: Int32, nMaxPos: Int32, fRedraw: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
    @commethod(8)
    def TxSetScrollPos(fnBar: Int32, nPos: Int32, fRedraw: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
    @commethod(9)
    def TxInvalidateRect(prc: POINTER(win32more.Foundation.RECT_head), fMode: win32more.Foundation.BOOL) -> Void: ...
    @commethod(10)
    def TxViewChange(fUpdate: win32more.Foundation.BOOL) -> Void: ...
    @commethod(11)
    def TxCreateCaret(hbmp: win32more.Graphics.Gdi.HBITMAP, xWidth: Int32, yHeight: Int32) -> win32more.Foundation.BOOL: ...
    @commethod(12)
    def TxShowCaret(fShow: win32more.Foundation.BOOL) -> win32more.Foundation.BOOL: ...
    @commethod(13)
    def TxSetCaretPos(x: Int32, y: Int32) -> win32more.Foundation.BOOL: ...
    @commethod(14)
    def TxSetTimer(idTimer: UInt32, uTimeout: UInt32) -> win32more.Foundation.BOOL: ...
    @commethod(15)
    def TxKillTimer(idTimer: UInt32) -> Void: ...
    @commethod(16)
    def TxScrollWindowEx(dx: Int32, dy: Int32, lprcScroll: POINTER(win32more.Foundation.RECT_head), lprcClip: POINTER(win32more.Foundation.RECT_head), hrgnUpdate: win32more.Graphics.Gdi.HRGN, lprcUpdate: POINTER(win32more.Foundation.RECT_head), fuScroll: win32more.UI.WindowsAndMessaging.SHOW_WINDOW_CMD) -> Void: ...
    @commethod(17)
    def TxSetCapture(fCapture: win32more.Foundation.BOOL) -> Void: ...
    @commethod(18)
    def TxSetFocus() -> Void: ...
    @commethod(19)
    def TxSetCursor(hcur: win32more.UI.WindowsAndMessaging.HCURSOR, fText: win32more.Foundation.BOOL) -> Void: ...
    @commethod(20)
    def TxScreenToClient(lppt: POINTER(win32more.Foundation.POINT_head)) -> win32more.Foundation.BOOL: ...
    @commethod(21)
    def TxClientToScreen(lppt: POINTER(win32more.Foundation.POINT_head)) -> win32more.Foundation.BOOL: ...
    @commethod(22)
    def TxActivate(plOldState: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def TxDeactivate(lNewState: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def TxGetClientRect(prc: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def TxGetViewInset(prc: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def TxGetCharFormat(ppCF: POINTER(POINTER(win32more.UI.Controls.RichEdit.CHARFORMATW_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def TxGetParaFormat(ppPF: POINTER(POINTER(win32more.UI.Controls.RichEdit.PARAFORMAT_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def TxGetSysColor(nIndex: win32more.Graphics.Gdi.SYS_COLOR_INDEX) -> win32more.Foundation.COLORREF: ...
    @commethod(29)
    def TxGetBackStyle(pstyle: POINTER(win32more.UI.Controls.RichEdit.TXTBACKSTYLE)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def TxGetMaxLength(plength: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def TxGetScrollBars(pdwScrollBar: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def TxGetPasswordChar(pch: POINTER(SByte)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def TxGetAcceleratorPos(pcp: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def TxGetExtent(lpExtent: POINTER(win32more.Foundation.SIZE_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def OnTxCharFormatChange(pCF: POINTER(win32more.UI.Controls.RichEdit.CHARFORMATW_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def OnTxParaFormatChange(pPF: POINTER(win32more.UI.Controls.RichEdit.PARAFORMAT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def TxGetPropertyBits(dwMask: UInt32, pdwBits: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def TxNotify(iNotify: UInt32, pv: c_void_p) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def TxImmGetContext() -> win32more.Globalization.HIMC: ...
    @commethod(40)
    def TxImmReleaseContext(himc: win32more.Globalization.HIMC) -> Void: ...
    @commethod(41)
    def TxGetSelectionBarWidth(lSelBarWidth: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class ITextHost2(c_void_p):
    extends: win32more.UI.Controls.RichEdit.ITextHost
    @commethod(42)
    def TxIsDoubleClickPending() -> win32more.Foundation.BOOL: ...
    @commethod(43)
    def TxGetWindow(phwnd: POINTER(win32more.Foundation.HWND)) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def TxSetForegroundWindow() -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def TxGetPalette() -> win32more.Graphics.Gdi.HPALETTE: ...
    @commethod(46)
    def TxGetEastAsianFlags(pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def TxSetCursor2(hcur: win32more.UI.WindowsAndMessaging.HCURSOR, bText: win32more.Foundation.BOOL) -> win32more.UI.WindowsAndMessaging.HCURSOR: ...
    @commethod(48)
    def TxFreeTextServicesNotification() -> Void: ...
    @commethod(49)
    def TxGetEditStyle(dwItem: UInt32, pdwData: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(50)
    def TxGetWindowStyles(pdwStyle: POINTER(UInt32), pdwExStyle: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(51)
    def TxShowDropCaret(fShow: win32more.Foundation.BOOL, hdc: win32more.Graphics.Gdi.HDC, prc: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(52)
    def TxDestroyCaret() -> win32more.Foundation.HRESULT: ...
    @commethod(53)
    def TxGetHorzExtent(plHorzExtent: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class ITextPara(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('8cc497c4-a1df-11ce-80-98-00-aa-00-47-be-5d')
    @commethod(7)
    def GetDuplicate(ppPara: POINTER(win32more.UI.Controls.RichEdit.ITextPara_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetDuplicate(pPara: win32more.UI.Controls.RichEdit.ITextPara_head) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def CanChange(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def IsEqual(pPara: win32more.UI.Controls.RichEdit.ITextPara_head, pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Reset(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetStyle(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def SetStyle(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetAlignment(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def SetAlignment(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetHyphenation(pValue: POINTER(win32more.UI.Controls.RichEdit.tomConstants)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def SetHyphenation(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetFirstLineIndent(pValue: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetKeepTogether(pValue: POINTER(win32more.UI.Controls.RichEdit.tomConstants)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def SetKeepTogether(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def GetKeepWithNext(pValue: POINTER(win32more.UI.Controls.RichEdit.tomConstants)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def SetKeepWithNext(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def GetLeftIndent(pValue: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def GetLineSpacing(pValue: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def GetLineSpacingRule(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def GetListAlignment(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def SetListAlignment(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def GetListLevelIndex(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def SetListLevelIndex(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def GetListStart(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def SetListStart(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def GetListTab(pValue: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def SetListTab(Value: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def GetListType(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def SetListType(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def GetNoLineNumber(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def SetNoLineNumber(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def GetPageBreakBefore(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def SetPageBreakBefore(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def GetRightIndent(pValue: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def SetRightIndent(Value: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def SetIndents(First: Single, Left: Single, Right: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def SetLineSpacing(Rule: Int32, Spacing: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def GetSpaceAfter(pValue: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def SetSpaceAfter(Value: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def GetSpaceBefore(pValue: POINTER(Single)) -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def SetSpaceBefore(Value: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def GetWidowControl(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def SetWidowControl(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(50)
    def GetTabCount(pCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(51)
    def AddTab(tbPos: Single, tbAlign: Int32, tbLeader: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(52)
    def ClearAllTabs() -> win32more.Foundation.HRESULT: ...
    @commethod(53)
    def DeleteTab(tbPos: Single) -> win32more.Foundation.HRESULT: ...
    @commethod(54)
    def GetTab(iTab: Int32, ptbPos: POINTER(Single), ptbAlign: POINTER(Int32), ptbLeader: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class ITextPara2(c_void_p):
    extends: win32more.UI.Controls.RichEdit.ITextPara
    Guid = Guid('c241f5e4-7206-11d8-a2-c7-00-a0-d1-d6-c6-b3')
    @commethod(55)
    def GetBorders(ppBorders: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(56)
    def GetDuplicate2(ppPara: POINTER(win32more.UI.Controls.RichEdit.ITextPara2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(57)
    def SetDuplicate2(pPara: win32more.UI.Controls.RichEdit.ITextPara2_head) -> win32more.Foundation.HRESULT: ...
    @commethod(58)
    def GetFontAlignment(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(59)
    def SetFontAlignment(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(60)
    def GetHangingPunctuation(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(61)
    def SetHangingPunctuation(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(62)
    def GetSnapToGrid(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(63)
    def SetSnapToGrid(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(64)
    def GetTrimPunctuationAtStart(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(65)
    def SetTrimPunctuationAtStart(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(66)
    def GetEffects(pValue: POINTER(Int32), pMask: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(67)
    def GetProperty(Type: Int32, pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(68)
    def IsEqual2(pPara: win32more.UI.Controls.RichEdit.ITextPara2_head, pB: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(69)
    def SetEffects(Value: Int32, Mask: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(70)
    def SetProperty(Type: Int32, Value: Int32) -> win32more.Foundation.HRESULT: ...
class ITextRange(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('8cc497c2-a1df-11ce-80-98-00-aa-00-47-be-5d')
    @commethod(7)
    def GetText(pbstr: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetText(bstr: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetChar(pChar: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetChar(Char: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetDuplicate(ppRange: POINTER(win32more.UI.Controls.RichEdit.ITextRange_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetFormattedText(ppRange: POINTER(win32more.UI.Controls.RichEdit.ITextRange_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def SetFormattedText(pRange: win32more.UI.Controls.RichEdit.ITextRange_head) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetStart(pcpFirst: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def SetStart(cpFirst: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def GetEnd(pcpLim: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def SetEnd(cpLim: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetFont(ppFont: POINTER(win32more.UI.Controls.RichEdit.ITextFont_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def SetFont(pFont: win32more.UI.Controls.RichEdit.ITextFont_head) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def GetPara(ppPara: POINTER(win32more.UI.Controls.RichEdit.ITextPara_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def SetPara(pPara: win32more.UI.Controls.RichEdit.ITextPara_head) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def GetStoryLength(pCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def GetStoryType(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def Collapse(bStart: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def Expand(Unit: Int32, pDelta: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def GetIndex(Unit: Int32, pIndex: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def SetIndex(Unit: Int32, Index: Int32, Extend: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def SetRange(cpAnchor: Int32, cpActive: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def InRange(pRange: win32more.UI.Controls.RichEdit.ITextRange_head, pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def InStory(pRange: win32more.UI.Controls.RichEdit.ITextRange_head, pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def IsEqual(pRange: win32more.UI.Controls.RichEdit.ITextRange_head, pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def Select() -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def StartOf(Unit: Int32, Extend: Int32, pDelta: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def EndOf(Unit: Int32, Extend: Int32, pDelta: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def Move(Unit: Int32, Count: Int32, pDelta: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def MoveStart(Unit: Int32, Count: Int32, pDelta: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def MoveEnd(Unit: Int32, Count: Int32, pDelta: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def MoveWhile(Cset: POINTER(win32more.System.Com.VARIANT_head), Count: Int32, pDelta: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def MoveStartWhile(Cset: POINTER(win32more.System.Com.VARIANT_head), Count: Int32, pDelta: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def MoveEndWhile(Cset: POINTER(win32more.System.Com.VARIANT_head), Count: Int32, pDelta: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def MoveUntil(Cset: POINTER(win32more.System.Com.VARIANT_head), Count: Int32, pDelta: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def MoveStartUntil(Cset: POINTER(win32more.System.Com.VARIANT_head), Count: Int32, pDelta: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def MoveEndUntil(Cset: POINTER(win32more.System.Com.VARIANT_head), Count: Int32, pDelta: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def FindText(bstr: win32more.Foundation.BSTR, Count: Int32, Flags: win32more.UI.Controls.RichEdit.tomConstants, pLength: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def FindTextStart(bstr: win32more.Foundation.BSTR, Count: Int32, Flags: win32more.UI.Controls.RichEdit.tomConstants, pLength: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def FindTextEnd(bstr: win32more.Foundation.BSTR, Count: Int32, Flags: win32more.UI.Controls.RichEdit.tomConstants, pLength: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def Delete(Unit: Int32, Count: Int32, pDelta: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def Cut(pVar: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def Copy(pVar: POINTER(win32more.System.Com.VARIANT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(50)
    def Paste(pVar: POINTER(win32more.System.Com.VARIANT_head), Format: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(51)
    def CanPaste(pVar: POINTER(win32more.System.Com.VARIANT_head), Format: Int32, pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(52)
    def CanEdit(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(53)
    def ChangeCase(Type: win32more.UI.Controls.RichEdit.tomConstants) -> win32more.Foundation.HRESULT: ...
    @commethod(54)
    def GetPoint(Type: win32more.UI.Controls.RichEdit.tomConstants, px: POINTER(Int32), py: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(55)
    def SetPoint(x: Int32, y: Int32, Type: win32more.UI.Controls.RichEdit.tomConstants, Extend: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(56)
    def ScrollIntoView(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(57)
    def GetEmbeddedObject(ppObject: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
class ITextRange2(c_void_p):
    extends: win32more.UI.Controls.RichEdit.ITextSelection
    Guid = Guid('c241f5e2-7206-11d8-a2-c7-00-a0-d1-d6-c6-b3')
    @commethod(68)
    def GetCch(pcch: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(69)
    def GetCells(ppCells: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(70)
    def GetColumn(ppColumn: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(71)
    def GetCount(pCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(72)
    def GetDuplicate2(ppRange: POINTER(win32more.UI.Controls.RichEdit.ITextRange2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(73)
    def GetFont2(ppFont: POINTER(win32more.UI.Controls.RichEdit.ITextFont2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(74)
    def SetFont2(pFont: win32more.UI.Controls.RichEdit.ITextFont2_head) -> win32more.Foundation.HRESULT: ...
    @commethod(75)
    def GetFormattedText2(ppRange: POINTER(win32more.UI.Controls.RichEdit.ITextRange2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(76)
    def SetFormattedText2(pRange: win32more.UI.Controls.RichEdit.ITextRange2_head) -> win32more.Foundation.HRESULT: ...
    @commethod(77)
    def GetGravity(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(78)
    def SetGravity(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(79)
    def GetPara2(ppPara: POINTER(win32more.UI.Controls.RichEdit.ITextPara2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(80)
    def SetPara2(pPara: win32more.UI.Controls.RichEdit.ITextPara2_head) -> win32more.Foundation.HRESULT: ...
    @commethod(81)
    def GetRow(ppRow: POINTER(win32more.UI.Controls.RichEdit.ITextRow_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(82)
    def GetStartPara(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(83)
    def GetTable(ppTable: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(84)
    def GetURL(pbstr: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(85)
    def SetURL(bstr: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(86)
    def AddSubrange(cp1: Int32, cp2: Int32, Activate: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(87)
    def BuildUpMath(Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(88)
    def DeleteSubrange(cpFirst: Int32, cpLim: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(89)
    def Find(pRange: win32more.UI.Controls.RichEdit.ITextRange2_head, Count: Int32, Flags: Int32, pDelta: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(90)
    def GetChar2(pChar: POINTER(Int32), Offset: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(91)
    def GetDropCap(pcLine: POINTER(Int32), pPosition: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(92)
    def GetInlineObject(pType: POINTER(Int32), pAlign: POINTER(Int32), pChar: POINTER(Int32), pChar1: POINTER(Int32), pChar2: POINTER(Int32), pCount: POINTER(Int32), pTeXStyle: POINTER(Int32), pcCol: POINTER(Int32), pLevel: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(93)
    def GetProperty(Type: Int32, pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(94)
    def GetRect(Type: Int32, pLeft: POINTER(Int32), pTop: POINTER(Int32), pRight: POINTER(Int32), pBottom: POINTER(Int32), pHit: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(95)
    def GetSubrange(iSubrange: Int32, pcpFirst: POINTER(Int32), pcpLim: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(96)
    def GetText2(Flags: Int32, pbstr: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(97)
    def HexToUnicode() -> win32more.Foundation.HRESULT: ...
    @commethod(98)
    def InsertTable(cCol: Int32, cRow: Int32, AutoFit: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(99)
    def Linearize(Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(100)
    def SetActiveSubrange(cpAnchor: Int32, cpActive: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(101)
    def SetDropCap(cLine: Int32, Position: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(102)
    def SetProperty(Type: Int32, Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(103)
    def SetText2(Flags: Int32, bstr: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(104)
    def UnicodeToHex() -> win32more.Foundation.HRESULT: ...
    @commethod(105)
    def SetInlineObject(Type: Int32, Align: Int32, Char: Int32, Char1: Int32, Char2: Int32, Count: Int32, TeXStyle: Int32, cCol: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(106)
    def GetMathFunctionType(bstr: win32more.Foundation.BSTR, pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(107)
    def InsertImage(width: Int32, height: Int32, ascent: Int32, Type: win32more.Graphics.Gdi.TEXT_ALIGN_OPTIONS, bstrAltText: win32more.Foundation.BSTR, pStream: win32more.System.Com.IStream_head) -> win32more.Foundation.HRESULT: ...
class ITextRow(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('c241f5ef-7206-11d8-a2-c7-00-a0-d1-d6-c6-b3')
    @commethod(7)
    def GetAlignment(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetAlignment(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetCellCount(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetCellCount(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetCellCountCache(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def SetCellCountCache(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetCellIndex(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetCellIndex(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetCellMargin(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def SetCellMargin(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetHeight(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def SetHeight(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetIndent(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def SetIndent(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def GetKeepTogether(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def SetKeepTogether(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def GetKeepWithNext(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def SetKeepWithNext(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def GetNestLevel(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def GetRTL(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def SetRTL(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def GetCellAlignment(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def SetCellAlignment(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def GetCellColorBack(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def SetCellColorBack(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def GetCellColorFore(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(33)
    def SetCellColorFore(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(34)
    def GetCellMergeFlags(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(35)
    def SetCellMergeFlags(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(36)
    def GetCellShading(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(37)
    def SetCellShading(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(38)
    def GetCellVerticalText(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(39)
    def SetCellVerticalText(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(40)
    def GetCellWidth(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(41)
    def SetCellWidth(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(42)
    def GetCellBorderColors(pcrLeft: POINTER(Int32), pcrTop: POINTER(Int32), pcrRight: POINTER(Int32), pcrBottom: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(43)
    def GetCellBorderWidths(pduLeft: POINTER(Int32), pduTop: POINTER(Int32), pduRight: POINTER(Int32), pduBottom: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(44)
    def SetCellBorderColors(crLeft: Int32, crTop: Int32, crRight: Int32, crBottom: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(45)
    def SetCellBorderWidths(duLeft: Int32, duTop: Int32, duRight: Int32, duBottom: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(46)
    def Apply(cRow: Int32, Flags: win32more.UI.Controls.RichEdit.tomConstants) -> win32more.Foundation.HRESULT: ...
    @commethod(47)
    def CanChange(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(48)
    def GetProperty(Type: Int32, pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(49)
    def Insert(cRow: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(50)
    def IsEqual(pRow: win32more.UI.Controls.RichEdit.ITextRow_head, pB: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(51)
    def Reset(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(52)
    def SetProperty(Type: Int32, Value: Int32) -> win32more.Foundation.HRESULT: ...
class ITextSelection(c_void_p):
    extends: win32more.UI.Controls.RichEdit.ITextRange
    Guid = Guid('8cc497c1-a1df-11ce-80-98-00-aa-00-47-be-5d')
    @commethod(58)
    def GetFlags(pFlags: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(59)
    def SetFlags(Flags: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(60)
    def GetType(pType: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(61)
    def MoveLeft(Unit: Int32, Count: Int32, Extend: Int32, pDelta: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(62)
    def MoveRight(Unit: Int32, Count: Int32, Extend: Int32, pDelta: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(63)
    def MoveUp(Unit: Int32, Count: Int32, Extend: Int32, pDelta: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(64)
    def MoveDown(Unit: Int32, Count: Int32, Extend: Int32, pDelta: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(65)
    def HomeKey(Unit: win32more.UI.Controls.RichEdit.tomConstants, Extend: Int32, pDelta: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(66)
    def EndKey(Unit: Int32, Extend: Int32, pDelta: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(67)
    def TypeText(bstr: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class ITextSelection2(c_void_p):
    extends: win32more.UI.Controls.RichEdit.ITextRange2
    Guid = Guid('c241f5e1-7206-11d8-a2-c7-00-a0-d1-d6-c6-b3')
class ITextServices(c_void_p):
    extends: win32more.System.Com.IUnknown
    @commethod(3)
    def TxSendMessage(msg: UInt32, wparam: win32more.Foundation.WPARAM, lparam: win32more.Foundation.LPARAM, plresult: POINTER(win32more.Foundation.LRESULT)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def TxDraw(dwDrawAspect: win32more.System.Com.DVASPECT, lindex: Int32, pvAspect: c_void_p, ptd: POINTER(win32more.System.Com.DVTARGETDEVICE_head), hdcDraw: win32more.Graphics.Gdi.HDC, hicTargetDev: win32more.Graphics.Gdi.HDC, lprcBounds: POINTER(win32more.Foundation.RECTL_head), lprcWBounds: POINTER(win32more.Foundation.RECTL_head), lprcUpdate: POINTER(win32more.Foundation.RECT_head), pfnContinue: IntPtr, dwContinue: UInt32, lViewId: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def TxGetHScroll(plMin: POINTER(Int32), plMax: POINTER(Int32), plPos: POINTER(Int32), plPage: POINTER(Int32), pfEnabled: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def TxGetVScroll(plMin: POINTER(Int32), plMax: POINTER(Int32), plPos: POINTER(Int32), plPage: POINTER(Int32), pfEnabled: POINTER(win32more.Foundation.BOOL)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def OnTxSetCursor(dwDrawAspect: win32more.System.Com.DVASPECT, lindex: Int32, pvAspect: c_void_p, ptd: POINTER(win32more.System.Com.DVTARGETDEVICE_head), hdcDraw: win32more.Graphics.Gdi.HDC, hicTargetDev: win32more.Graphics.Gdi.HDC, lprcClient: POINTER(win32more.Foundation.RECT_head), x: Int32, y: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def TxQueryHitPoint(dwDrawAspect: win32more.System.Com.DVASPECT, lindex: Int32, pvAspect: c_void_p, ptd: POINTER(win32more.System.Com.DVTARGETDEVICE_head), hdcDraw: win32more.Graphics.Gdi.HDC, hicTargetDev: win32more.Graphics.Gdi.HDC, lprcClient: POINTER(win32more.Foundation.RECT_head), x: Int32, y: Int32, pHitResult: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def OnTxInPlaceActivate(prcClient: POINTER(win32more.Foundation.RECT_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def OnTxInPlaceDeactivate() -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def OnTxUIActivate() -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def OnTxUIDeactivate() -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def TxGetText(pbstrText: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def TxSetText(pszText: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def TxGetCurTargetX(param0: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def TxGetBaseLinePos(param0: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def TxGetNaturalSize(dwAspect: UInt32, hdcDraw: win32more.Graphics.Gdi.HDC, hicTargetDev: win32more.Graphics.Gdi.HDC, ptd: POINTER(win32more.System.Com.DVTARGETDEVICE_head), dwMode: UInt32, psizelExtent: POINTER(win32more.Foundation.SIZE_head), pwidth: POINTER(Int32), pheight: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def TxGetDropTarget(ppDropTarget: POINTER(win32more.System.Ole.IDropTarget_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def OnTxPropertyBitsChange(dwMask: UInt32, dwBits: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def TxGetCachedSize(pdwWidth: POINTER(UInt32), pdwHeight: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
class ITextServices2(c_void_p):
    extends: win32more.UI.Controls.RichEdit.ITextServices
    @commethod(21)
    def TxGetNaturalSize2(dwAspect: UInt32, hdcDraw: win32more.Graphics.Gdi.HDC, hicTargetDev: win32more.Graphics.Gdi.HDC, ptd: POINTER(win32more.System.Com.DVTARGETDEVICE_head), dwMode: UInt32, psizelExtent: POINTER(win32more.Foundation.SIZE_head), pwidth: POINTER(Int32), pheight: POINTER(Int32), pascent: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def TxDrawD2D(pRenderTarget: win32more.Graphics.Direct2D.ID2D1RenderTarget_head, lprcBounds: POINTER(win32more.Foundation.RECTL_head), lprcUpdate: POINTER(win32more.Foundation.RECT_head), lViewId: Int32) -> win32more.Foundation.HRESULT: ...
class ITextStory(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('c241f5f3-7206-11d8-a2-c7-00-a0-d1-d6-c6-b3')
    @commethod(3)
    def GetActive(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetActive(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetDisplay(ppDisplay: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetIndex(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetType(pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def SetType(Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetProperty(Type: Int32, pValue: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def GetRange(cpActive: Int32, cpAnchor: Int32, ppRange: POINTER(win32more.UI.Controls.RichEdit.ITextRange2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetText(Flags: Int32, pbstr: POINTER(win32more.Foundation.BSTR)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def SetFormattedText(pUnk: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def SetProperty(Type: Int32, Value: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def SetText(Flags: Int32, bstr: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
class ITextStoryRanges(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('8cc497c5-a1df-11ce-80-98-00-aa-00-47-be-5d')
    @commethod(7)
    def _NewEnum(ppunkEnum: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Item(Index: Int32, ppRange: POINTER(win32more.UI.Controls.RichEdit.ITextRange_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def GetCount(pCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
class ITextStoryRanges2(c_void_p):
    extends: win32more.UI.Controls.RichEdit.ITextStoryRanges
    Guid = Guid('c241f5e5-7206-11d8-a2-c7-00-a0-d1-d6-c6-b3')
    @commethod(10)
    def Item2(Index: Int32, ppRange: POINTER(win32more.UI.Controls.RichEdit.ITextRange2_head)) -> win32more.Foundation.HRESULT: ...
class ITextStrings(c_void_p):
    extends: win32more.System.Com.IDispatch
    Guid = Guid('c241f5e7-7206-11d8-a2-c7-00-a0-d1-d6-c6-b3')
    @commethod(7)
    def Item(Index: Int32, ppRange: POINTER(win32more.UI.Controls.RichEdit.ITextRange2_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetCount(pCount: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Add(bstr: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Append(pRange: win32more.UI.Controls.RichEdit.ITextRange2_head, iString: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Cat2(iString: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def CatTop2(bstr: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def DeleteRange(pRange: win32more.UI.Controls.RichEdit.ITextRange2_head) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def EncodeFunction(Type: Int32, Align: Int32, Char: Int32, Char1: Int32, Char2: Int32, Count: Int32, TeXStyle: Int32, cCol: Int32, pRange: win32more.UI.Controls.RichEdit.ITextRange2_head) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetCch(iString: Int32, pcch: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def InsertNullStr(iString: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def MoveBoundary(iString: Int32, cch: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def PrefixTop(bstr: win32more.Foundation.BSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def Remove(iString: Int32, cString: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def SetFormattedText(pRangeD: win32more.UI.Controls.RichEdit.ITextRange2_head, pRangeS: win32more.UI.Controls.RichEdit.ITextRange2_head) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def SetOpCp(iString: Int32, cp: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def SuffixTop(bstr: win32more.Foundation.BSTR, pRange: win32more.UI.Controls.RichEdit.ITextRange2_head) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def Swap() -> win32more.Foundation.HRESULT: ...
KHYPH = Int32
KHYPH_khyphNil: KHYPH = 0
KHYPH_khyphNormal: KHYPH = 1
KHYPH_khyphAddBefore: KHYPH = 2
KHYPH_khyphChangeBefore: KHYPH = 3
KHYPH_khyphDeleteBefore: KHYPH = 4
KHYPH_khyphChangeAfter: KHYPH = 5
KHYPH_khyphDelAndChange: KHYPH = 6
MANCODE = Int32
MBOLD: MANCODE = 16
MITAL: MANCODE = 32
MGREEK: MANCODE = 64
MROMN: MANCODE = 0
MSCRP: MANCODE = 1
MFRAK: MANCODE = 2
MOPEN: MANCODE = 3
MSANS: MANCODE = 4
MMONO: MANCODE = 5
MMATH: MANCODE = 6
MISOL: MANCODE = 7
MINIT: MANCODE = 8
MTAIL: MANCODE = 9
MSTRCH: MANCODE = 10
MLOOP: MANCODE = 11
MOPENA: MANCODE = 12
class MSGFILTER(Structure):
    nmhdr: win32more.UI.Controls.NMHDR
    msg: UInt32
    wParam: win32more.Foundation.WPARAM
    lParam: win32more.Foundation.LPARAM
    _pack_ = 4
class OBJECTPOSITIONS(Structure):
    nmhdr: win32more.UI.Controls.NMHDR
    cObjectCount: Int32
    pcpPositions: POINTER(Int32)
    _pack_ = 4
OBJECTTYPE = Int32
OBJECTTYPE_tomSimpleText: OBJECTTYPE = 0
OBJECTTYPE_tomRuby: OBJECTTYPE = 1
OBJECTTYPE_tomHorzVert: OBJECTTYPE = 2
OBJECTTYPE_tomWarichu: OBJECTTYPE = 3
OBJECTTYPE_tomEq: OBJECTTYPE = 9
OBJECTTYPE_tomMath: OBJECTTYPE = 10
OBJECTTYPE_tomAccent: OBJECTTYPE = 10
OBJECTTYPE_tomBox: OBJECTTYPE = 11
OBJECTTYPE_tomBoxedFormula: OBJECTTYPE = 12
OBJECTTYPE_tomBrackets: OBJECTTYPE = 13
OBJECTTYPE_tomBracketsWithSeps: OBJECTTYPE = 14
OBJECTTYPE_tomEquationArray: OBJECTTYPE = 15
OBJECTTYPE_tomFraction: OBJECTTYPE = 16
OBJECTTYPE_tomFunctionApply: OBJECTTYPE = 17
OBJECTTYPE_tomLeftSubSup: OBJECTTYPE = 18
OBJECTTYPE_tomLowerLimit: OBJECTTYPE = 19
OBJECTTYPE_tomMatrix: OBJECTTYPE = 20
OBJECTTYPE_tomNary: OBJECTTYPE = 21
OBJECTTYPE_tomOpChar: OBJECTTYPE = 22
OBJECTTYPE_tomOverbar: OBJECTTYPE = 23
OBJECTTYPE_tomPhantom: OBJECTTYPE = 24
OBJECTTYPE_tomRadical: OBJECTTYPE = 25
OBJECTTYPE_tomSlashedFraction: OBJECTTYPE = 26
OBJECTTYPE_tomStack: OBJECTTYPE = 27
OBJECTTYPE_tomStretchStack: OBJECTTYPE = 28
OBJECTTYPE_tomSubscript: OBJECTTYPE = 29
OBJECTTYPE_tomSubSup: OBJECTTYPE = 30
OBJECTTYPE_tomSuperscript: OBJECTTYPE = 31
OBJECTTYPE_tomUnderbar: OBJECTTYPE = 32
OBJECTTYPE_tomUpperLimit: OBJECTTYPE = 33
OBJECTTYPE_tomObjectMax: OBJECTTYPE = 33
class PARAFORMAT(Structure):
    cbSize: UInt32
    dwMask: win32more.UI.Controls.RichEdit.PARAFORMAT_MASK
    wNumbering: win32more.UI.Controls.RichEdit.PARAFORMAT_NUMBERING
    Anonymous: _Anonymous_e__Union
    dxStartIndent: Int32
    dxRightIndent: Int32
    dxOffset: Int32
    wAlignment: win32more.UI.Controls.RichEdit.PARAFORMAT_ALIGNMENT
    cTabCount: Int16
    rgxTabs: UInt32 * 32
    class _Anonymous_e__Union(Union):
        wReserved: UInt16
        wEffects: UInt16
class PARAFORMAT2(Structure):
    Base: win32more.UI.Controls.RichEdit.PARAFORMAT
    dySpaceBefore: Int32
    dySpaceAfter: Int32
    dyLineSpacing: Int32
    sStyle: Int16
    bLineSpacingRule: Byte
    bOutlineLevel: Byte
    wShadingWeight: UInt16
    wShadingStyle: win32more.UI.Controls.RichEdit.PARAFORMAT_SHADING_STYLE
    wNumberingStart: UInt16
    wNumberingStyle: win32more.UI.Controls.RichEdit.PARAFORMAT_NUMBERING_STYLE
    wNumberingTab: UInt16
    wBorderSpace: UInt16
    wBorderWidth: UInt16
    wBorders: win32more.UI.Controls.RichEdit.PARAFORMAT_BORDERS
PARAFORMAT_ALIGNMENT = UInt16
PFA_CENTER: PARAFORMAT_ALIGNMENT = 3
PFA_LEFT: PARAFORMAT_ALIGNMENT = 1
PFA_RIGHT: PARAFORMAT_ALIGNMENT = 2
PARAFORMAT_BORDERS = UInt16
PARAFORMAT_BORDERS_LEFT: PARAFORMAT_BORDERS = 1
PARAFORMAT_BORDERS_RIGHT: PARAFORMAT_BORDERS = 2
PARAFORMAT_BORDERS_TOP: PARAFORMAT_BORDERS = 4
PARAFORMAT_BORDERS_BOTTOM: PARAFORMAT_BORDERS = 8
PARAFORMAT_BORDERS_INSIDE: PARAFORMAT_BORDERS = 16
PARAFORMAT_BORDERS_OUTSIDE: PARAFORMAT_BORDERS = 32
PARAFORMAT_BORDERS_AUTOCOLOR: PARAFORMAT_BORDERS = 64
PARAFORMAT_MASK = UInt32
PFM_ALIGNMENT: PARAFORMAT_MASK = 8
PFM_NUMBERING: PARAFORMAT_MASK = 32
PFM_OFFSET: PARAFORMAT_MASK = 4
PFM_OFFSETINDENT: PARAFORMAT_MASK = 2147483648
PFM_RIGHTINDENT: PARAFORMAT_MASK = 2
PFM_RTLPARA: PARAFORMAT_MASK = 65536
PFM_STARTINDENT: PARAFORMAT_MASK = 1
PFM_TABSTOPS: PARAFORMAT_MASK = 16
PARAFORMAT_NUMBERING = UInt16
PFN_BULLET: PARAFORMAT_NUMBERING = 1
PFN_ARABIC: PARAFORMAT_NUMBERING = 2
PFN_LCLETTER: PARAFORMAT_NUMBERING = 3
PFN_UCLETTER: PARAFORMAT_NUMBERING = 4
PFN_LCROMAN: PARAFORMAT_NUMBERING = 5
PFN_UCROMAN: PARAFORMAT_NUMBERING = 6
PARAFORMAT_NUMBERING_STYLE = UInt16
PFNS_PAREN: PARAFORMAT_NUMBERING_STYLE = 0
PFNS_PARENS: PARAFORMAT_NUMBERING_STYLE = 256
PFNS_PERIOD: PARAFORMAT_NUMBERING_STYLE = 512
PFNS_PLAIN: PARAFORMAT_NUMBERING_STYLE = 768
PFNS_NONUMBER: PARAFORMAT_NUMBERING_STYLE = 1024
PFNS_NEWNUMBER: PARAFORMAT_NUMBERING_STYLE = 32768
PARAFORMAT_SHADING_STYLE = UInt16
PARAFORMAT_SHADING_STYLE_NONE: PARAFORMAT_SHADING_STYLE = 0
PARAFORMAT_SHADING_STYLE_DARK_HORIZ: PARAFORMAT_SHADING_STYLE = 1
PARAFORMAT_SHADING_STYLE_DARK_VERT: PARAFORMAT_SHADING_STYLE = 2
PARAFORMAT_SHADING_STYLE_DARK_DOWN_DIAG: PARAFORMAT_SHADING_STYLE = 3
PARAFORMAT_SHADING_STYLE_DARK_UP_DIAG: PARAFORMAT_SHADING_STYLE = 4
PARAFORMAT_SHADING_STYLE_DARK_GRID: PARAFORMAT_SHADING_STYLE = 5
PARAFORMAT_SHADING_STYLE_DARK_TRELLIS: PARAFORMAT_SHADING_STYLE = 6
PARAFORMAT_SHADING_STYLE_LIGHT_HORZ: PARAFORMAT_SHADING_STYLE = 7
PARAFORMAT_SHADING_STYLE_LIGHT_VERT: PARAFORMAT_SHADING_STYLE = 8
PARAFORMAT_SHADING_STYLE_LIGHT_DOWN_DIAG: PARAFORMAT_SHADING_STYLE = 9
PARAFORMAT_SHADING_STYLE_LIGHT_UP_DIAG: PARAFORMAT_SHADING_STYLE = 10
PARAFORMAT_SHADING_STYLE_LIGHT_GRID: PARAFORMAT_SHADING_STYLE = 11
PARAFORMAT_SHADING_STYLE_LIGHT_TRELLIS: PARAFORMAT_SHADING_STYLE = 12
@winfunctype_pointer
def PCreateTextServices(punkOuter: win32more.System.Com.IUnknown_head, pITextHost: win32more.UI.Controls.RichEdit.ITextHost_head, ppUnk: POINTER(win32more.System.Com.IUnknown_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PShutdownTextServices(pTextServices: win32more.System.Com.IUnknown_head) -> win32more.Foundation.HRESULT: ...
class PUNCTUATION(Structure):
    iSize: UInt32
    szPunctuation: win32more.Foundation.PSTR
    _pack_ = 4
class REOBJECT(Structure):
    cbStruct: UInt32
    cp: Int32
    clsid: Guid
    poleobj: win32more.System.Ole.IOleObject_head
    pstg: win32more.System.Com.StructuredStorage.IStorage_head
    polesite: win32more.System.Ole.IOleClientSite_head
    sizel: win32more.Foundation.SIZE
    dvaspect: UInt32
    dwFlags: win32more.UI.Controls.RichEdit.REOBJECT_FLAGS
    dwUser: UInt32
REOBJECT_FLAGS = UInt32
REO_ALIGNTORIGHT: REOBJECT_FLAGS = 256
REO_BELOWBASELINE: REOBJECT_FLAGS = 2
REO_BLANK: REOBJECT_FLAGS = 16
REO_CANROTATE: REOBJECT_FLAGS = 128
REO_DONTNEEDPALETTE: REOBJECT_FLAGS = 32
REO_DYNAMICSIZE: REOBJECT_FLAGS = 8
REO_GETMETAFILE: REOBJECT_FLAGS = 4194304
REO_HILITED: REOBJECT_FLAGS = 16777216
REO_INPLACEACTIVE: REOBJECT_FLAGS = 33554432
REO_INVERTEDSELECT: REOBJECT_FLAGS = 4
REO_LINK: REOBJECT_FLAGS = 2147483648
REO_LINKAVAILABLE: REOBJECT_FLAGS = 8388608
REO_OPEN: REOBJECT_FLAGS = 67108864
REO_OWNERDRAWSELECT: REOBJECT_FLAGS = 64
REO_RESIZABLE: REOBJECT_FLAGS = 1
REO_SELECTED: REOBJECT_FLAGS = 134217728
REO_STATIC: REOBJECT_FLAGS = 1073741824
REO_USEASBACKGROUND: REOBJECT_FLAGS = 1024
REO_WRAPTEXTAROUND: REOBJECT_FLAGS = 512
class REPASTESPECIAL(Structure):
    dwAspect: win32more.System.Com.DVASPECT
    dwParam: UIntPtr
    _pack_ = 4
class REQRESIZE(Structure):
    nmhdr: win32more.UI.Controls.NMHDR
    rc: win32more.Foundation.RECT
    _pack_ = 4
class RICHEDIT_IMAGE_PARAMETERS(Structure):
    xWidth: Int32
    yHeight: Int32
    Ascent: Int32
    Type: win32more.Graphics.Gdi.TEXT_ALIGN_OPTIONS
    pwszAlternateText: win32more.Foundation.PWSTR
    pIStream: win32more.System.Com.IStream_head
    _pack_ = 4
RICH_EDIT_GET_CONTEXT_MENU_SEL_TYPE = UInt16
SEL_EMPTY: RICH_EDIT_GET_CONTEXT_MENU_SEL_TYPE = 0
SEL_TEXT: RICH_EDIT_GET_CONTEXT_MENU_SEL_TYPE = 1
SEL_OBJECT: RICH_EDIT_GET_CONTEXT_MENU_SEL_TYPE = 2
SEL_MULTICHAR: RICH_EDIT_GET_CONTEXT_MENU_SEL_TYPE = 4
SEL_MULTIOBJECT: RICH_EDIT_GET_CONTEXT_MENU_SEL_TYPE = 8
GCM_RIGHTMOUSEDROP: RICH_EDIT_GET_CONTEXT_MENU_SEL_TYPE = 32768
RICH_EDIT_GET_OBJECT_FLAGS = UInt32
REO_GETOBJ_POLEOBJ: RICH_EDIT_GET_OBJECT_FLAGS = 1
REO_GETOBJ_PSTG: RICH_EDIT_GET_OBJECT_FLAGS = 2
REO_GETOBJ_POLESITE: RICH_EDIT_GET_OBJECT_FLAGS = 4
REO_GETOBJ_NO_INTERFACES: RICH_EDIT_GET_OBJECT_FLAGS = 0
REO_GETOBJ_ALL_INTERFACES: RICH_EDIT_GET_OBJECT_FLAGS = 7
class SELCHANGE(Structure):
    nmhdr: win32more.UI.Controls.NMHDR
    chrg: win32more.UI.Controls.RichEdit.CHARRANGE
    seltyp: win32more.UI.Controls.RichEdit.RICH_EDIT_GET_CONTEXT_MENU_SEL_TYPE
    _pack_ = 4
class SETTEXTEX(Structure):
    flags: UInt32
    codepage: UInt32
class TABLECELLPARMS(Structure):
    dxWidth: Int32
    _bitfield: UInt16
    wShading: UInt16
    dxBrdrLeft: Int16
    dyBrdrTop: Int16
    dxBrdrRight: Int16
    dyBrdrBottom: Int16
    crBrdrLeft: win32more.Foundation.COLORREF
    crBrdrTop: win32more.Foundation.COLORREF
    crBrdrRight: win32more.Foundation.COLORREF
    crBrdrBottom: win32more.Foundation.COLORREF
    crBackPat: win32more.Foundation.COLORREF
    crForePat: win32more.Foundation.COLORREF
class TABLEROWPARMS(Structure):
    cbRow: Byte
    cbCell: Byte
    cCell: Byte
    cRow: Byte
    dxCellMargin: Int32
    dxIndent: Int32
    dyHeight: Int32
    _bitfield: UInt32
    cpStartRow: Int32
    bTableLevel: Byte
    iCell: Byte
TEXTMODE = Int32
TM_PLAINTEXT: TEXTMODE = 1
TM_RICHTEXT: TEXTMODE = 2
TM_SINGLELEVELUNDO: TEXTMODE = 4
TM_MULTILEVELUNDO: TEXTMODE = 8
TM_SINGLECODEPAGE: TEXTMODE = 16
TM_MULTICODEPAGE: TEXTMODE = 32
class TEXTRANGEA(Structure):
    chrg: win32more.UI.Controls.RichEdit.CHARRANGE
    lpstrText: win32more.Foundation.PSTR
    _pack_ = 4
class TEXTRANGEW(Structure):
    chrg: win32more.UI.Controls.RichEdit.CHARRANGE
    lpstrText: win32more.Foundation.PWSTR
    _pack_ = 4
TXTBACKSTYLE = Int32
TXTBACK_TRANSPARENT: TXTBACKSTYLE = 0
TXTBACK_OPAQUE: TXTBACKSTYLE = 1
TXTHITRESULT = Int32
TXTHITRESULT_NOHIT: TXTHITRESULT = 0
TXTHITRESULT_TRANSPARENT: TXTHITRESULT = 1
TXTHITRESULT_CLOSE: TXTHITRESULT = 2
TXTHITRESULT_HIT: TXTHITRESULT = 3
TXTNATURALSIZE = Int32
TXTNS_FITTOCONTENT2: TXTNATURALSIZE = 0
TXTNS_FITTOCONTENT: TXTNATURALSIZE = 1
TXTNS_ROUNDTOLINE: TXTNATURALSIZE = 2
TXTNS_FITTOCONTENT3: TXTNATURALSIZE = 3
TXTNS_FITTOCONTENTWSP: TXTNATURALSIZE = 4
TXTNS_INCLUDELASTLINE: TXTNATURALSIZE = 1073741824
TXTNS_EMU: TXTNATURALSIZE = -2147483648
TXTVIEW = Int32
TXTVIEW_ACTIVE: TXTVIEW = 0
TXTVIEW_INACTIVE: TXTVIEW = -1
UNDONAMEID = Int32
UID_UNKNOWN: UNDONAMEID = 0
UID_TYPING: UNDONAMEID = 1
UID_DELETE: UNDONAMEID = 2
UID_DRAGDROP: UNDONAMEID = 3
UID_CUT: UNDONAMEID = 4
UID_PASTE: UNDONAMEID = 5
UID_AUTOTABLE: UNDONAMEID = 6
tomConstants = Int32
tomConstants_tomFalse: tomConstants = 0
tomConstants_tomTrue: tomConstants = -1
tomConstants_tomUndefined: tomConstants = -9999999
tomConstants_tomToggle: tomConstants = -9999998
tomConstants_tomAutoColor: tomConstants = -9999997
tomConstants_tomDefault: tomConstants = -9999996
tomConstants_tomSuspend: tomConstants = -9999995
tomConstants_tomResume: tomConstants = -9999994
tomConstants_tomApplyNow: tomConstants = 0
tomConstants_tomApplyLater: tomConstants = 1
tomConstants_tomTrackParms: tomConstants = 2
tomConstants_tomCacheParms: tomConstants = 3
tomConstants_tomApplyTmp: tomConstants = 4
tomConstants_tomDisableSmartFont: tomConstants = 8
tomConstants_tomEnableSmartFont: tomConstants = 9
tomConstants_tomUsePoints: tomConstants = 10
tomConstants_tomUseTwips: tomConstants = 11
tomConstants_tomBackward: tomConstants = -1073741823
tomConstants_tomForward: tomConstants = 1073741823
tomConstants_tomMove: tomConstants = 0
tomConstants_tomExtend: tomConstants = 1
tomConstants_tomNoSelection: tomConstants = 0
tomConstants_tomSelectionIP: tomConstants = 1
tomConstants_tomSelectionNormal: tomConstants = 2
tomConstants_tomSelectionFrame: tomConstants = 3
tomConstants_tomSelectionColumn: tomConstants = 4
tomConstants_tomSelectionRow: tomConstants = 5
tomConstants_tomSelectionBlock: tomConstants = 6
tomConstants_tomSelectionInlineShape: tomConstants = 7
tomConstants_tomSelectionShape: tomConstants = 8
tomConstants_tomSelStartActive: tomConstants = 1
tomConstants_tomSelAtEOL: tomConstants = 2
tomConstants_tomSelOvertype: tomConstants = 4
tomConstants_tomSelActive: tomConstants = 8
tomConstants_tomSelReplace: tomConstants = 16
tomConstants_tomEnd: tomConstants = 0
tomConstants_tomStart: tomConstants = 32
tomConstants_tomCollapseEnd: tomConstants = 0
tomConstants_tomCollapseStart: tomConstants = 1
tomConstants_tomClientCoord: tomConstants = 256
tomConstants_tomAllowOffClient: tomConstants = 512
tomConstants_tomTransform: tomConstants = 1024
tomConstants_tomObjectArg: tomConstants = 2048
tomConstants_tomAtEnd: tomConstants = 4096
tomConstants_tomNone: tomConstants = 0
tomConstants_tomSingle: tomConstants = 1
tomConstants_tomWords: tomConstants = 2
tomConstants_tomDouble: tomConstants = 3
tomConstants_tomDotted: tomConstants = 4
tomConstants_tomDash: tomConstants = 5
tomConstants_tomDashDot: tomConstants = 6
tomConstants_tomDashDotDot: tomConstants = 7
tomConstants_tomWave: tomConstants = 8
tomConstants_tomThick: tomConstants = 9
tomConstants_tomHair: tomConstants = 10
tomConstants_tomDoubleWave: tomConstants = 11
tomConstants_tomHeavyWave: tomConstants = 12
tomConstants_tomLongDash: tomConstants = 13
tomConstants_tomThickDash: tomConstants = 14
tomConstants_tomThickDashDot: tomConstants = 15
tomConstants_tomThickDashDotDot: tomConstants = 16
tomConstants_tomThickDotted: tomConstants = 17
tomConstants_tomThickLongDash: tomConstants = 18
tomConstants_tomLineSpaceSingle: tomConstants = 0
tomConstants_tomLineSpace1pt5: tomConstants = 1
tomConstants_tomLineSpaceDouble: tomConstants = 2
tomConstants_tomLineSpaceAtLeast: tomConstants = 3
tomConstants_tomLineSpaceExactly: tomConstants = 4
tomConstants_tomLineSpaceMultiple: tomConstants = 5
tomConstants_tomLineSpacePercent: tomConstants = 6
tomConstants_tomAlignLeft: tomConstants = 0
tomConstants_tomAlignCenter: tomConstants = 1
tomConstants_tomAlignRight: tomConstants = 2
tomConstants_tomAlignJustify: tomConstants = 3
tomConstants_tomAlignDecimal: tomConstants = 3
tomConstants_tomAlignBar: tomConstants = 4
tomConstants_tomDefaultTab: tomConstants = 5
tomConstants_tomAlignInterWord: tomConstants = 3
tomConstants_tomAlignNewspaper: tomConstants = 4
tomConstants_tomAlignInterLetter: tomConstants = 5
tomConstants_tomAlignScaled: tomConstants = 6
tomConstants_tomSpaces: tomConstants = 0
tomConstants_tomDots: tomConstants = 1
tomConstants_tomDashes: tomConstants = 2
tomConstants_tomLines: tomConstants = 3
tomConstants_tomThickLines: tomConstants = 4
tomConstants_tomEquals: tomConstants = 5
tomConstants_tomTabBack: tomConstants = -3
tomConstants_tomTabNext: tomConstants = -2
tomConstants_tomTabHere: tomConstants = -1
tomConstants_tomListNone: tomConstants = 0
tomConstants_tomListBullet: tomConstants = 1
tomConstants_tomListNumberAsArabic: tomConstants = 2
tomConstants_tomListNumberAsLCLetter: tomConstants = 3
tomConstants_tomListNumberAsUCLetter: tomConstants = 4
tomConstants_tomListNumberAsLCRoman: tomConstants = 5
tomConstants_tomListNumberAsUCRoman: tomConstants = 6
tomConstants_tomListNumberAsSequence: tomConstants = 7
tomConstants_tomListNumberedCircle: tomConstants = 8
tomConstants_tomListNumberedBlackCircleWingding: tomConstants = 9
tomConstants_tomListNumberedWhiteCircleWingding: tomConstants = 10
tomConstants_tomListNumberedArabicWide: tomConstants = 11
tomConstants_tomListNumberedChS: tomConstants = 12
tomConstants_tomListNumberedChT: tomConstants = 13
tomConstants_tomListNumberedJpnChS: tomConstants = 14
tomConstants_tomListNumberedJpnKor: tomConstants = 15
tomConstants_tomListNumberedArabic1: tomConstants = 16
tomConstants_tomListNumberedArabic2: tomConstants = 17
tomConstants_tomListNumberedHebrew: tomConstants = 18
tomConstants_tomListNumberedThaiAlpha: tomConstants = 19
tomConstants_tomListNumberedThaiNum: tomConstants = 20
tomConstants_tomListNumberedHindiAlpha: tomConstants = 21
tomConstants_tomListNumberedHindiAlpha1: tomConstants = 22
tomConstants_tomListNumberedHindiNum: tomConstants = 23
tomConstants_tomListParentheses: tomConstants = 65536
tomConstants_tomListPeriod: tomConstants = 131072
tomConstants_tomListPlain: tomConstants = 196608
tomConstants_tomListNoNumber: tomConstants = 262144
tomConstants_tomListMinus: tomConstants = 524288
tomConstants_tomIgnoreNumberStyle: tomConstants = 16777216
tomConstants_tomParaStyleNormal: tomConstants = -1
tomConstants_tomParaStyleHeading1: tomConstants = -2
tomConstants_tomParaStyleHeading2: tomConstants = -3
tomConstants_tomParaStyleHeading3: tomConstants = -4
tomConstants_tomParaStyleHeading4: tomConstants = -5
tomConstants_tomParaStyleHeading5: tomConstants = -6
tomConstants_tomParaStyleHeading6: tomConstants = -7
tomConstants_tomParaStyleHeading7: tomConstants = -8
tomConstants_tomParaStyleHeading8: tomConstants = -9
tomConstants_tomParaStyleHeading9: tomConstants = -10
tomConstants_tomCharacter: tomConstants = 1
tomConstants_tomWord: tomConstants = 2
tomConstants_tomSentence: tomConstants = 3
tomConstants_tomParagraph: tomConstants = 4
tomConstants_tomLine: tomConstants = 5
tomConstants_tomStory: tomConstants = 6
tomConstants_tomScreen: tomConstants = 7
tomConstants_tomSection: tomConstants = 8
tomConstants_tomTableColumn: tomConstants = 9
tomConstants_tomColumn: tomConstants = 9
tomConstants_tomRow: tomConstants = 10
tomConstants_tomWindow: tomConstants = 11
tomConstants_tomCell: tomConstants = 12
tomConstants_tomCharFormat: tomConstants = 13
tomConstants_tomParaFormat: tomConstants = 14
tomConstants_tomTable: tomConstants = 15
tomConstants_tomObject: tomConstants = 16
tomConstants_tomPage: tomConstants = 17
tomConstants_tomHardParagraph: tomConstants = 18
tomConstants_tomCluster: tomConstants = 19
tomConstants_tomInlineObject: tomConstants = 20
tomConstants_tomInlineObjectArg: tomConstants = 21
tomConstants_tomLeafLine: tomConstants = 22
tomConstants_tomLayoutColumn: tomConstants = 23
tomConstants_tomProcessId: tomConstants = 1073741825
tomConstants_tomMatchWord: tomConstants = 2
tomConstants_tomMatchCase: tomConstants = 4
tomConstants_tomMatchPattern: tomConstants = 8
tomConstants_tomUnknownStory: tomConstants = 0
tomConstants_tomMainTextStory: tomConstants = 1
tomConstants_tomFootnotesStory: tomConstants = 2
tomConstants_tomEndnotesStory: tomConstants = 3
tomConstants_tomCommentsStory: tomConstants = 4
tomConstants_tomTextFrameStory: tomConstants = 5
tomConstants_tomEvenPagesHeaderStory: tomConstants = 6
tomConstants_tomPrimaryHeaderStory: tomConstants = 7
tomConstants_tomEvenPagesFooterStory: tomConstants = 8
tomConstants_tomPrimaryFooterStory: tomConstants = 9
tomConstants_tomFirstPageHeaderStory: tomConstants = 10
tomConstants_tomFirstPageFooterStory: tomConstants = 11
tomConstants_tomScratchStory: tomConstants = 127
tomConstants_tomFindStory: tomConstants = 128
tomConstants_tomReplaceStory: tomConstants = 129
tomConstants_tomStoryInactive: tomConstants = 0
tomConstants_tomStoryActiveDisplay: tomConstants = 1
tomConstants_tomStoryActiveUI: tomConstants = 2
tomConstants_tomStoryActiveDisplayUI: tomConstants = 3
tomConstants_tomNoAnimation: tomConstants = 0
tomConstants_tomLasVegasLights: tomConstants = 1
tomConstants_tomBlinkingBackground: tomConstants = 2
tomConstants_tomSparkleText: tomConstants = 3
tomConstants_tomMarchingBlackAnts: tomConstants = 4
tomConstants_tomMarchingRedAnts: tomConstants = 5
tomConstants_tomShimmer: tomConstants = 6
tomConstants_tomWipeDown: tomConstants = 7
tomConstants_tomWipeRight: tomConstants = 8
tomConstants_tomAnimationMax: tomConstants = 8
tomConstants_tomLowerCase: tomConstants = 0
tomConstants_tomUpperCase: tomConstants = 1
tomConstants_tomTitleCase: tomConstants = 2
tomConstants_tomSentenceCase: tomConstants = 4
tomConstants_tomToggleCase: tomConstants = 5
tomConstants_tomReadOnly: tomConstants = 256
tomConstants_tomShareDenyRead: tomConstants = 512
tomConstants_tomShareDenyWrite: tomConstants = 1024
tomConstants_tomPasteFile: tomConstants = 4096
tomConstants_tomCreateNew: tomConstants = 16
tomConstants_tomCreateAlways: tomConstants = 32
tomConstants_tomOpenExisting: tomConstants = 48
tomConstants_tomOpenAlways: tomConstants = 64
tomConstants_tomTruncateExisting: tomConstants = 80
tomConstants_tomRTF: tomConstants = 1
tomConstants_tomText: tomConstants = 2
tomConstants_tomHTML: tomConstants = 3
tomConstants_tomWordDocument: tomConstants = 4
tomConstants_tomBold: tomConstants = -2147483647
tomConstants_tomItalic: tomConstants = -2147483646
tomConstants_tomUnderline: tomConstants = -2147483644
tomConstants_tomStrikeout: tomConstants = -2147483640
tomConstants_tomProtected: tomConstants = -2147483632
tomConstants_tomLink: tomConstants = -2147483616
tomConstants_tomSmallCaps: tomConstants = -2147483584
tomConstants_tomAllCaps: tomConstants = -2147483520
tomConstants_tomHidden: tomConstants = -2147483392
tomConstants_tomOutline: tomConstants = -2147483136
tomConstants_tomShadow: tomConstants = -2147482624
tomConstants_tomEmboss: tomConstants = -2147481600
tomConstants_tomImprint: tomConstants = -2147479552
tomConstants_tomDisabled: tomConstants = -2147475456
tomConstants_tomRevised: tomConstants = -2147467264
tomConstants_tomSubscriptCF: tomConstants = -2147418112
tomConstants_tomSuperscriptCF: tomConstants = -2147352576
tomConstants_tomFontBound: tomConstants = -2146435072
tomConstants_tomLinkProtected: tomConstants = -2139095040
tomConstants_tomInlineObjectStart: tomConstants = -2130706432
tomConstants_tomExtendedChar: tomConstants = -2113929216
tomConstants_tomAutoBackColor: tomConstants = -2080374784
tomConstants_tomMathZoneNoBuildUp: tomConstants = -2013265920
tomConstants_tomMathZone: tomConstants = -1879048192
tomConstants_tomMathZoneOrdinary: tomConstants = -1610612736
tomConstants_tomAutoTextColor: tomConstants = -1073741824
tomConstants_tomMathZoneDisplay: tomConstants = 262144
tomConstants_tomParaEffectRTL: tomConstants = 1
tomConstants_tomParaEffectKeep: tomConstants = 2
tomConstants_tomParaEffectKeepNext: tomConstants = 4
tomConstants_tomParaEffectPageBreakBefore: tomConstants = 8
tomConstants_tomParaEffectNoLineNumber: tomConstants = 16
tomConstants_tomParaEffectNoWidowControl: tomConstants = 32
tomConstants_tomParaEffectDoNotHyphen: tomConstants = 64
tomConstants_tomParaEffectSideBySide: tomConstants = 128
tomConstants_tomParaEffectCollapsed: tomConstants = 256
tomConstants_tomParaEffectOutlineLevel: tomConstants = 512
tomConstants_tomParaEffectBox: tomConstants = 1024
tomConstants_tomParaEffectTableRowDelimiter: tomConstants = 4096
tomConstants_tomParaEffectTable: tomConstants = 16384
tomConstants_tomModWidthPairs: tomConstants = 1
tomConstants_tomModWidthSpace: tomConstants = 2
tomConstants_tomAutoSpaceAlpha: tomConstants = 4
tomConstants_tomAutoSpaceNumeric: tomConstants = 8
tomConstants_tomAutoSpaceParens: tomConstants = 16
tomConstants_tomEmbeddedFont: tomConstants = 32
tomConstants_tomDoublestrike: tomConstants = 64
tomConstants_tomOverlapping: tomConstants = 128
tomConstants_tomNormalCaret: tomConstants = 0
tomConstants_tomKoreanBlockCaret: tomConstants = 1
tomConstants_tomNullCaret: tomConstants = 2
tomConstants_tomIncludeInset: tomConstants = 1
tomConstants_tomUnicodeBiDi: tomConstants = 1
tomConstants_tomMathCFCheck: tomConstants = 4
tomConstants_tomUnlink: tomConstants = 8
tomConstants_tomUnhide: tomConstants = 16
tomConstants_tomCheckTextLimit: tomConstants = 32
tomConstants_tomIgnoreCurrentFont: tomConstants = 0
tomConstants_tomMatchCharRep: tomConstants = 1
tomConstants_tomMatchFontSignature: tomConstants = 2
tomConstants_tomMatchAscii: tomConstants = 4
tomConstants_tomGetHeightOnly: tomConstants = 8
tomConstants_tomMatchMathFont: tomConstants = 16
tomConstants_tomCharset: tomConstants = -2147483648
tomConstants_tomCharRepFromLcid: tomConstants = 1073741824
tomConstants_tomAnsi: tomConstants = 0
tomConstants_tomEastEurope: tomConstants = 1
tomConstants_tomCyrillic: tomConstants = 2
tomConstants_tomGreek: tomConstants = 3
tomConstants_tomTurkish: tomConstants = 4
tomConstants_tomHebrew: tomConstants = 5
tomConstants_tomArabic: tomConstants = 6
tomConstants_tomBaltic: tomConstants = 7
tomConstants_tomVietnamese: tomConstants = 8
tomConstants_tomDefaultCharRep: tomConstants = 9
tomConstants_tomSymbol: tomConstants = 10
tomConstants_tomThai: tomConstants = 11
tomConstants_tomShiftJIS: tomConstants = 12
tomConstants_tomGB2312: tomConstants = 13
tomConstants_tomHangul: tomConstants = 14
tomConstants_tomBIG5: tomConstants = 15
tomConstants_tomPC437: tomConstants = 16
tomConstants_tomOEM: tomConstants = 17
tomConstants_tomMac: tomConstants = 18
tomConstants_tomArmenian: tomConstants = 19
tomConstants_tomSyriac: tomConstants = 20
tomConstants_tomThaana: tomConstants = 21
tomConstants_tomDevanagari: tomConstants = 22
tomConstants_tomBengali: tomConstants = 23
tomConstants_tomGurmukhi: tomConstants = 24
tomConstants_tomGujarati: tomConstants = 25
tomConstants_tomOriya: tomConstants = 26
tomConstants_tomTamil: tomConstants = 27
tomConstants_tomTelugu: tomConstants = 28
tomConstants_tomKannada: tomConstants = 29
tomConstants_tomMalayalam: tomConstants = 30
tomConstants_tomSinhala: tomConstants = 31
tomConstants_tomLao: tomConstants = 32
tomConstants_tomTibetan: tomConstants = 33
tomConstants_tomMyanmar: tomConstants = 34
tomConstants_tomGeorgian: tomConstants = 35
tomConstants_tomJamo: tomConstants = 36
tomConstants_tomEthiopic: tomConstants = 37
tomConstants_tomCherokee: tomConstants = 38
tomConstants_tomAboriginal: tomConstants = 39
tomConstants_tomOgham: tomConstants = 40
tomConstants_tomRunic: tomConstants = 41
tomConstants_tomKhmer: tomConstants = 42
tomConstants_tomMongolian: tomConstants = 43
tomConstants_tomBraille: tomConstants = 44
tomConstants_tomYi: tomConstants = 45
tomConstants_tomLimbu: tomConstants = 46
tomConstants_tomTaiLe: tomConstants = 47
tomConstants_tomNewTaiLue: tomConstants = 48
tomConstants_tomSylotiNagri: tomConstants = 49
tomConstants_tomKharoshthi: tomConstants = 50
tomConstants_tomKayahli: tomConstants = 51
tomConstants_tomUsymbol: tomConstants = 52
tomConstants_tomEmoji: tomConstants = 53
tomConstants_tomGlagolitic: tomConstants = 54
tomConstants_tomLisu: tomConstants = 55
tomConstants_tomVai: tomConstants = 56
tomConstants_tomNKo: tomConstants = 57
tomConstants_tomOsmanya: tomConstants = 58
tomConstants_tomPhagsPa: tomConstants = 59
tomConstants_tomGothic: tomConstants = 60
tomConstants_tomDeseret: tomConstants = 61
tomConstants_tomTifinagh: tomConstants = 62
tomConstants_tomCharRepMax: tomConstants = 63
tomConstants_tomRE10Mode: tomConstants = 1
tomConstants_tomUseAtFont: tomConstants = 2
tomConstants_tomTextFlowMask: tomConstants = 12
tomConstants_tomTextFlowES: tomConstants = 0
tomConstants_tomTextFlowSW: tomConstants = 4
tomConstants_tomTextFlowWN: tomConstants = 8
tomConstants_tomTextFlowNE: tomConstants = 12
tomConstants_tomNoIME: tomConstants = 524288
tomConstants_tomSelfIME: tomConstants = 262144
tomConstants_tomNoUpScroll: tomConstants = 65536
tomConstants_tomNoVpScroll: tomConstants = 262144
tomConstants_tomNoLink: tomConstants = 0
tomConstants_tomClientLink: tomConstants = 1
tomConstants_tomFriendlyLinkName: tomConstants = 2
tomConstants_tomFriendlyLinkAddress: tomConstants = 3
tomConstants_tomAutoLinkURL: tomConstants = 4
tomConstants_tomAutoLinkEmail: tomConstants = 5
tomConstants_tomAutoLinkPhone: tomConstants = 6
tomConstants_tomAutoLinkPath: tomConstants = 7
tomConstants_tomCompressNone: tomConstants = 0
tomConstants_tomCompressPunctuation: tomConstants = 1
tomConstants_tomCompressPunctuationAndKana: tomConstants = 2
tomConstants_tomCompressMax: tomConstants = 2
tomConstants_tomUnderlinePositionAuto: tomConstants = 0
tomConstants_tomUnderlinePositionBelow: tomConstants = 1
tomConstants_tomUnderlinePositionAbove: tomConstants = 2
tomConstants_tomUnderlinePositionMax: tomConstants = 2
tomConstants_tomFontAlignmentAuto: tomConstants = 0
tomConstants_tomFontAlignmentTop: tomConstants = 1
tomConstants_tomFontAlignmentBaseline: tomConstants = 2
tomConstants_tomFontAlignmentBottom: tomConstants = 3
tomConstants_tomFontAlignmentCenter: tomConstants = 4
tomConstants_tomFontAlignmentMax: tomConstants = 4
tomConstants_tomRubyBelow: tomConstants = 128
tomConstants_tomRubyAlignCenter: tomConstants = 0
tomConstants_tomRubyAlign010: tomConstants = 1
tomConstants_tomRubyAlign121: tomConstants = 2
tomConstants_tomRubyAlignLeft: tomConstants = 3
tomConstants_tomRubyAlignRight: tomConstants = 4
tomConstants_tomLimitsDefault: tomConstants = 0
tomConstants_tomLimitsUnderOver: tomConstants = 1
tomConstants_tomLimitsSubSup: tomConstants = 2
tomConstants_tomUpperLimitAsSuperScript: tomConstants = 3
tomConstants_tomLimitsOpposite: tomConstants = 4
tomConstants_tomShowLLimPlaceHldr: tomConstants = 8
tomConstants_tomShowULimPlaceHldr: tomConstants = 16
tomConstants_tomDontGrowWithContent: tomConstants = 64
tomConstants_tomGrowWithContent: tomConstants = 128
tomConstants_tomSubSupAlign: tomConstants = 1
tomConstants_tomLimitAlignMask: tomConstants = 3
tomConstants_tomLimitAlignCenter: tomConstants = 0
tomConstants_tomLimitAlignLeft: tomConstants = 1
tomConstants_tomLimitAlignRight: tomConstants = 2
tomConstants_tomShowDegPlaceHldr: tomConstants = 8
tomConstants_tomAlignDefault: tomConstants = 0
tomConstants_tomAlignMatchAscentDescent: tomConstants = 2
tomConstants_tomMathVariant: tomConstants = 32
tomConstants_tomStyleDefault: tomConstants = 0
tomConstants_tomStyleScriptScriptCramped: tomConstants = 1
tomConstants_tomStyleScriptScript: tomConstants = 2
tomConstants_tomStyleScriptCramped: tomConstants = 3
tomConstants_tomStyleScript: tomConstants = 4
tomConstants_tomStyleTextCramped: tomConstants = 5
tomConstants_tomStyleText: tomConstants = 6
tomConstants_tomStyleDisplayCramped: tomConstants = 7
tomConstants_tomStyleDisplay: tomConstants = 8
tomConstants_tomMathRelSize: tomConstants = 64
tomConstants_tomDecDecSize: tomConstants = 254
tomConstants_tomDecSize: tomConstants = 255
tomConstants_tomIncSize: tomConstants = 65
tomConstants_tomIncIncSize: tomConstants = 66
tomConstants_tomGravityUI: tomConstants = 0
tomConstants_tomGravityBack: tomConstants = 1
tomConstants_tomGravityFore: tomConstants = 2
tomConstants_tomGravityIn: tomConstants = 3
tomConstants_tomGravityOut: tomConstants = 4
tomConstants_tomGravityBackward: tomConstants = 536870912
tomConstants_tomGravityForward: tomConstants = 1073741824
tomConstants_tomAdjustCRLF: tomConstants = 1
tomConstants_tomUseCRLF: tomConstants = 2
tomConstants_tomTextize: tomConstants = 4
tomConstants_tomAllowFinalEOP: tomConstants = 8
tomConstants_tomFoldMathAlpha: tomConstants = 16
tomConstants_tomNoHidden: tomConstants = 32
tomConstants_tomIncludeNumbering: tomConstants = 64
tomConstants_tomTranslateTableCell: tomConstants = 128
tomConstants_tomNoMathZoneBrackets: tomConstants = 256
tomConstants_tomConvertMathChar: tomConstants = 512
tomConstants_tomNoUCGreekItalic: tomConstants = 1024
tomConstants_tomAllowMathBold: tomConstants = 2048
tomConstants_tomLanguageTag: tomConstants = 4096
tomConstants_tomConvertRTF: tomConstants = 8192
tomConstants_tomApplyRtfDocProps: tomConstants = 16384
tomConstants_tomPhantomShow: tomConstants = 1
tomConstants_tomPhantomZeroWidth: tomConstants = 2
tomConstants_tomPhantomZeroAscent: tomConstants = 4
tomConstants_tomPhantomZeroDescent: tomConstants = 8
tomConstants_tomPhantomTransparent: tomConstants = 16
tomConstants_tomPhantomASmash: tomConstants = 5
tomConstants_tomPhantomDSmash: tomConstants = 9
tomConstants_tomPhantomHSmash: tomConstants = 3
tomConstants_tomPhantomSmash: tomConstants = 13
tomConstants_tomPhantomHorz: tomConstants = 12
tomConstants_tomPhantomVert: tomConstants = 2
tomConstants_tomBoxHideTop: tomConstants = 1
tomConstants_tomBoxHideBottom: tomConstants = 2
tomConstants_tomBoxHideLeft: tomConstants = 4
tomConstants_tomBoxHideRight: tomConstants = 8
tomConstants_tomBoxStrikeH: tomConstants = 16
tomConstants_tomBoxStrikeV: tomConstants = 32
tomConstants_tomBoxStrikeTLBR: tomConstants = 64
tomConstants_tomBoxStrikeBLTR: tomConstants = 128
tomConstants_tomBoxAlignCenter: tomConstants = 1
tomConstants_tomSpaceMask: tomConstants = 28
tomConstants_tomSpaceDefault: tomConstants = 0
tomConstants_tomSpaceUnary: tomConstants = 4
tomConstants_tomSpaceBinary: tomConstants = 8
tomConstants_tomSpaceRelational: tomConstants = 12
tomConstants_tomSpaceSkip: tomConstants = 16
tomConstants_tomSpaceOrd: tomConstants = 20
tomConstants_tomSpaceDifferential: tomConstants = 24
tomConstants_tomSizeText: tomConstants = 32
tomConstants_tomSizeScript: tomConstants = 64
tomConstants_tomSizeScriptScript: tomConstants = 96
tomConstants_tomNoBreak: tomConstants = 128
tomConstants_tomTransparentForPositioning: tomConstants = 256
tomConstants_tomTransparentForSpacing: tomConstants = 512
tomConstants_tomStretchCharBelow: tomConstants = 0
tomConstants_tomStretchCharAbove: tomConstants = 1
tomConstants_tomStretchBaseBelow: tomConstants = 2
tomConstants_tomStretchBaseAbove: tomConstants = 3
tomConstants_tomMatrixAlignMask: tomConstants = 3
tomConstants_tomMatrixAlignCenter: tomConstants = 0
tomConstants_tomMatrixAlignTopRow: tomConstants = 1
tomConstants_tomMatrixAlignBottomRow: tomConstants = 3
tomConstants_tomShowMatPlaceHldr: tomConstants = 8
tomConstants_tomEqArrayLayoutWidth: tomConstants = 1
tomConstants_tomEqArrayAlignMask: tomConstants = 12
tomConstants_tomEqArrayAlignCenter: tomConstants = 0
tomConstants_tomEqArrayAlignTopRow: tomConstants = 4
tomConstants_tomEqArrayAlignBottomRow: tomConstants = 12
tomConstants_tomMathManualBreakMask: tomConstants = 127
tomConstants_tomMathBreakLeft: tomConstants = 125
tomConstants_tomMathBreakCenter: tomConstants = 126
tomConstants_tomMathBreakRight: tomConstants = 127
tomConstants_tomMathEqAlign: tomConstants = 128
tomConstants_tomMathArgShadingStart: tomConstants = 593
tomConstants_tomMathArgShadingEnd: tomConstants = 594
tomConstants_tomMathObjShadingStart: tomConstants = 595
tomConstants_tomMathObjShadingEnd: tomConstants = 596
tomConstants_tomFunctionTypeNone: tomConstants = 0
tomConstants_tomFunctionTypeTakesArg: tomConstants = 1
tomConstants_tomFunctionTypeTakesLim: tomConstants = 2
tomConstants_tomFunctionTypeTakesLim2: tomConstants = 3
tomConstants_tomFunctionTypeIsLim: tomConstants = 4
tomConstants_tomMathParaAlignDefault: tomConstants = 0
tomConstants_tomMathParaAlignCenterGroup: tomConstants = 1
tomConstants_tomMathParaAlignCenter: tomConstants = 2
tomConstants_tomMathParaAlignLeft: tomConstants = 3
tomConstants_tomMathParaAlignRight: tomConstants = 4
tomConstants_tomMathDispAlignMask: tomConstants = 3
tomConstants_tomMathDispAlignCenterGroup: tomConstants = 0
tomConstants_tomMathDispAlignCenter: tomConstants = 1
tomConstants_tomMathDispAlignLeft: tomConstants = 2
tomConstants_tomMathDispAlignRight: tomConstants = 3
tomConstants_tomMathDispIntUnderOver: tomConstants = 4
tomConstants_tomMathDispFracTeX: tomConstants = 8
tomConstants_tomMathDispNaryGrow: tomConstants = 16
tomConstants_tomMathDocEmptyArgMask: tomConstants = 96
tomConstants_tomMathDocEmptyArgAuto: tomConstants = 0
tomConstants_tomMathDocEmptyArgAlways: tomConstants = 32
tomConstants_tomMathDocEmptyArgNever: tomConstants = 64
tomConstants_tomMathDocSbSpOpUnchanged: tomConstants = 128
tomConstants_tomMathDocDiffMask: tomConstants = 768
tomConstants_tomMathDocDiffDefault: tomConstants = 0
tomConstants_tomMathDocDiffUpright: tomConstants = 256
tomConstants_tomMathDocDiffItalic: tomConstants = 512
tomConstants_tomMathDocDiffOpenItalic: tomConstants = 768
tomConstants_tomMathDispNarySubSup: tomConstants = 1024
tomConstants_tomMathDispDef: tomConstants = 2048
tomConstants_tomMathEnableRtl: tomConstants = 4096
tomConstants_tomMathBrkBinMask: tomConstants = 196608
tomConstants_tomMathBrkBinBefore: tomConstants = 0
tomConstants_tomMathBrkBinAfter: tomConstants = 65536
tomConstants_tomMathBrkBinDup: tomConstants = 131072
tomConstants_tomMathBrkBinSubMask: tomConstants = 786432
tomConstants_tomMathBrkBinSubMM: tomConstants = 0
tomConstants_tomMathBrkBinSubPM: tomConstants = 262144
tomConstants_tomMathBrkBinSubMP: tomConstants = 524288
tomConstants_tomSelRange: tomConstants = 597
tomConstants_tomHstring: tomConstants = 596
tomConstants_tomFontPropTeXStyle: tomConstants = 828
tomConstants_tomFontPropAlign: tomConstants = 829
tomConstants_tomFontStretch: tomConstants = 830
tomConstants_tomFontStyle: tomConstants = 831
tomConstants_tomFontStyleUpright: tomConstants = 0
tomConstants_tomFontStyleOblique: tomConstants = 1
tomConstants_tomFontStyleItalic: tomConstants = 2
tomConstants_tomFontStretchDefault: tomConstants = 0
tomConstants_tomFontStretchUltraCondensed: tomConstants = 1
tomConstants_tomFontStretchExtraCondensed: tomConstants = 2
tomConstants_tomFontStretchCondensed: tomConstants = 3
tomConstants_tomFontStretchSemiCondensed: tomConstants = 4
tomConstants_tomFontStretchNormal: tomConstants = 5
tomConstants_tomFontStretchSemiExpanded: tomConstants = 6
tomConstants_tomFontStretchExpanded: tomConstants = 7
tomConstants_tomFontStretchExtraExpanded: tomConstants = 8
tomConstants_tomFontStretchUltraExpanded: tomConstants = 9
tomConstants_tomFontWeightDefault: tomConstants = 0
tomConstants_tomFontWeightThin: tomConstants = 100
tomConstants_tomFontWeightExtraLight: tomConstants = 200
tomConstants_tomFontWeightLight: tomConstants = 300
tomConstants_tomFontWeightNormal: tomConstants = 400
tomConstants_tomFontWeightRegular: tomConstants = 400
tomConstants_tomFontWeightMedium: tomConstants = 500
tomConstants_tomFontWeightSemiBold: tomConstants = 600
tomConstants_tomFontWeightBold: tomConstants = 700
tomConstants_tomFontWeightExtraBold: tomConstants = 800
tomConstants_tomFontWeightBlack: tomConstants = 900
tomConstants_tomFontWeightHeavy: tomConstants = 900
tomConstants_tomFontWeightExtraBlack: tomConstants = 950
tomConstants_tomParaPropMathAlign: tomConstants = 1079
tomConstants_tomDocMathBuild: tomConstants = 128
tomConstants_tomMathLMargin: tomConstants = 129
tomConstants_tomMathRMargin: tomConstants = 130
tomConstants_tomMathWrapIndent: tomConstants = 131
tomConstants_tomMathWrapRight: tomConstants = 132
tomConstants_tomMathPostSpace: tomConstants = 134
tomConstants_tomMathPreSpace: tomConstants = 133
tomConstants_tomMathInterSpace: tomConstants = 135
tomConstants_tomMathIntraSpace: tomConstants = 136
tomConstants_tomCanCopy: tomConstants = 137
tomConstants_tomCanRedo: tomConstants = 138
tomConstants_tomCanUndo: tomConstants = 139
tomConstants_tomUndoLimit: tomConstants = 140
tomConstants_tomDocAutoLink: tomConstants = 141
tomConstants_tomEllipsisMode: tomConstants = 142
tomConstants_tomEllipsisState: tomConstants = 143
tomConstants_tomEllipsisNone: tomConstants = 0
tomConstants_tomEllipsisEnd: tomConstants = 1
tomConstants_tomEllipsisWord: tomConstants = 3
tomConstants_tomEllipsisPresent: tomConstants = 1
tomConstants_tomVTopCell: tomConstants = 1
tomConstants_tomVLowCell: tomConstants = 2
tomConstants_tomHStartCell: tomConstants = 4
tomConstants_tomHContCell: tomConstants = 8
tomConstants_tomRowUpdate: tomConstants = 1
tomConstants_tomRowApplyDefault: tomConstants = 0
tomConstants_tomCellStructureChangeOnly: tomConstants = 1
tomConstants_tomRowHeightActual: tomConstants = 2059
make_head(_module, 'AutoCorrectProc')
make_head(_module, 'BIDIOPTIONS')
make_head(_module, 'CARET_INFO')
make_head(_module, 'CHANGENOTIFY')
make_head(_module, 'CHARFORMAT2A')
make_head(_module, 'CHARFORMAT2W')
make_head(_module, 'CHARFORMATA')
make_head(_module, 'CHARFORMATW')
make_head(_module, 'CHARRANGE')
make_head(_module, 'CLIPBOARDFORMAT')
make_head(_module, 'COMPCOLOR')
make_head(_module, 'EDITSTREAM')
make_head(_module, 'EDITSTREAMCALLBACK')
make_head(_module, 'EDITWORDBREAKPROCEX')
make_head(_module, 'ENCORRECTTEXT')
make_head(_module, 'ENDCOMPOSITIONNOTIFY')
make_head(_module, 'ENDROPFILES')
make_head(_module, 'ENLINK')
make_head(_module, 'ENLOWFIRTF')
make_head(_module, 'ENOLEOPFAILED')
make_head(_module, 'ENPROTECTED')
make_head(_module, 'ENSAVECLIPBOARD')
make_head(_module, 'FINDTEXTA')
make_head(_module, 'FINDTEXTEXA')
make_head(_module, 'FINDTEXTEXW')
make_head(_module, 'FINDTEXTW')
make_head(_module, 'FORMATRANGE')
make_head(_module, 'GETCONTEXTMENUEX')
make_head(_module, 'GETTEXTEX')
make_head(_module, 'GETTEXTLENGTHEX')
make_head(_module, 'GROUPTYPINGCHANGE')
make_head(_module, 'HYPHENATEINFO')
make_head(_module, 'HYPHRESULT')
make_head(_module, 'IMECOMPTEXT')
make_head(_module, 'IRichEditOle')
make_head(_module, 'IRichEditOleCallback')
make_head(_module, 'IRicheditUiaOverrides')
make_head(_module, 'ITextDisplays')
make_head(_module, 'ITextDocument')
make_head(_module, 'ITextDocument2')
make_head(_module, 'ITextDocument2Old')
make_head(_module, 'ITextFont')
make_head(_module, 'ITextFont2')
make_head(_module, 'ITextHost')
make_head(_module, 'ITextHost2')
make_head(_module, 'ITextPara')
make_head(_module, 'ITextPara2')
make_head(_module, 'ITextRange')
make_head(_module, 'ITextRange2')
make_head(_module, 'ITextRow')
make_head(_module, 'ITextSelection')
make_head(_module, 'ITextSelection2')
make_head(_module, 'ITextServices')
make_head(_module, 'ITextServices2')
make_head(_module, 'ITextStory')
make_head(_module, 'ITextStoryRanges')
make_head(_module, 'ITextStoryRanges2')
make_head(_module, 'ITextStrings')
make_head(_module, 'MSGFILTER')
make_head(_module, 'OBJECTPOSITIONS')
make_head(_module, 'PARAFORMAT')
make_head(_module, 'PARAFORMAT2')
make_head(_module, 'PCreateTextServices')
make_head(_module, 'PShutdownTextServices')
make_head(_module, 'PUNCTUATION')
make_head(_module, 'REOBJECT')
make_head(_module, 'REPASTESPECIAL')
make_head(_module, 'REQRESIZE')
make_head(_module, 'RICHEDIT_IMAGE_PARAMETERS')
make_head(_module, 'SELCHANGE')
make_head(_module, 'SETTEXTEX')
make_head(_module, 'TABLECELLPARMS')
make_head(_module, 'TABLEROWPARMS')
make_head(_module, 'TEXTRANGEA')
make_head(_module, 'TEXTRANGEW')
__all__ = [
    "ATP_CHANGE",
    "ATP_NOCHANGE",
    "ATP_NODELIMITER",
    "ATP_REPLACEALLTEXT",
    "AURL_DISABLEMIXEDLGC",
    "AURL_ENABLEDRIVELETTERS",
    "AURL_ENABLEEA",
    "AURL_ENABLEEAURLS",
    "AURL_ENABLEEMAILADDR",
    "AURL_ENABLETELNO",
    "AURL_ENABLEURL",
    "AutoCorrectProc",
    "BIDIOPTIONS",
    "BOE_CONTEXTALIGNMENT",
    "BOE_CONTEXTREADING",
    "BOE_FORCERECALC",
    "BOE_LEGACYBIDICLASS",
    "BOE_NEUTRALOVERRIDE",
    "BOE_PLAINTEXT",
    "BOE_RTLDIR",
    "BOE_UNICODEBIDI",
    "BOM_CONTEXTALIGNMENT",
    "BOM_CONTEXTREADING",
    "BOM_DEFPARADIR",
    "BOM_LEGACYBIDICLASS",
    "BOM_NEUTRALOVERRIDE",
    "BOM_PLAINTEXT",
    "BOM_UNICODEBIDI",
    "CARET_CUSTOM",
    "CARET_FLAGS",
    "CARET_INFO",
    "CARET_ITALIC",
    "CARET_NONE",
    "CARET_NULL",
    "CARET_ROTATE90",
    "CARET_RTL",
    "CERICHEDIT_CLASSA",
    "CERICHEDIT_CLASSW",
    "CFE_ALLCAPS",
    "CFE_AUTOBACKCOLOR",
    "CFE_AUTOCOLOR",
    "CFE_BOLD",
    "CFE_DISABLED",
    "CFE_EFFECTS",
    "CFE_EMBOSS",
    "CFE_EXTENDED",
    "CFE_FONTBOUND",
    "CFE_HIDDEN",
    "CFE_IMPRINT",
    "CFE_ITALIC",
    "CFE_LINK",
    "CFE_LINKPROTECTED",
    "CFE_MATH",
    "CFE_MATHNOBUILDUP",
    "CFE_MATHORDINARY",
    "CFE_OUTLINE",
    "CFE_PROTECTED",
    "CFE_REVISED",
    "CFE_SHADOW",
    "CFE_SMALLCAPS",
    "CFE_STRIKEOUT",
    "CFE_SUBSCRIPT",
    "CFE_SUPERSCRIPT",
    "CFE_UNDERLINE",
    "CFM_ALL",
    "CFM_ALL2",
    "CFM_ALLCAPS",
    "CFM_ALLEFFECTS",
    "CFM_ANIMATION",
    "CFM_BACKCOLOR",
    "CFM_BOLD",
    "CFM_CHARSET",
    "CFM_COLOR",
    "CFM_COOKIE",
    "CFM_DISABLED",
    "CFM_EFFECTS",
    "CFM_EFFECTS2",
    "CFM_EMBOSS",
    "CFM_EXTENDED",
    "CFM_FACE",
    "CFM_FONTBOUND",
    "CFM_HIDDEN",
    "CFM_IMPRINT",
    "CFM_ITALIC",
    "CFM_KERNING",
    "CFM_LCID",
    "CFM_LINK",
    "CFM_LINKPROTECTED",
    "CFM_MASK",
    "CFM_MATH",
    "CFM_MATHNOBUILDUP",
    "CFM_MATHORDINARY",
    "CFM_OFFSET",
    "CFM_OUTLINE",
    "CFM_PROTECTED",
    "CFM_REVAUTHOR",
    "CFM_REVISED",
    "CFM_SHADOW",
    "CFM_SIZE",
    "CFM_SMALLCAPS",
    "CFM_SPACING",
    "CFM_STRIKEOUT",
    "CFM_STYLE",
    "CFM_SUBSCRIPT",
    "CFM_SUPERSCRIPT",
    "CFM_UNDERLINE",
    "CFM_UNDERLINETYPE",
    "CFM_WEIGHT",
    "CF_RETEXTOBJ",
    "CF_RTF",
    "CF_RTFNOOBJS",
    "CHANGENOTIFY",
    "CHANGETYPE",
    "CHARFORMAT2A",
    "CHARFORMAT2W",
    "CHARFORMATA",
    "CHARFORMATW",
    "CHARRANGE",
    "CLIPBOARDFORMAT",
    "CN_GENERIC",
    "CN_NEWREDO",
    "CN_NEWUNDO",
    "CN_TEXTCHANGED",
    "COMPCOLOR",
    "CTFMODEBIAS_CONVERSATION",
    "CTFMODEBIAS_DATETIME",
    "CTFMODEBIAS_DEFAULT",
    "CTFMODEBIAS_FILENAME",
    "CTFMODEBIAS_FULLWIDTHALPHANUMERIC",
    "CTFMODEBIAS_HALFWIDTHALPHANUMERIC",
    "CTFMODEBIAS_HALFWIDTHKATAKANA",
    "CTFMODEBIAS_HANGUL",
    "CTFMODEBIAS_HIRAGANA",
    "CTFMODEBIAS_KATAKANA",
    "CTFMODEBIAS_NAME",
    "CTFMODEBIAS_NUMERIC",
    "CTFMODEBIAS_READING",
    "ECN_ENDCOMPOSITION",
    "ECN_NEWTEXT",
    "ECOOP_AND",
    "ECOOP_OR",
    "ECOOP_SET",
    "ECOOP_XOR",
    "ECO_AUTOHSCROLL",
    "ECO_AUTOVSCROLL",
    "ECO_AUTOWORDSELECTION",
    "ECO_NOHIDESEL",
    "ECO_READONLY",
    "ECO_SAVESEL",
    "ECO_SELECTIONBAR",
    "ECO_VERTICAL",
    "ECO_WANTRETURN",
    "EDITSTREAM",
    "EDITSTREAMCALLBACK",
    "EDITWORDBREAKPROCEX",
    "ELLIPSIS_END",
    "ELLIPSIS_MASK",
    "ELLIPSIS_NONE",
    "ELLIPSIS_WORD",
    "EMO_ENTER",
    "EMO_EXIT",
    "EMO_EXPAND",
    "EMO_EXPANDDOCUMENT",
    "EMO_EXPANDSELECTION",
    "EMO_GETVIEWMODE",
    "EMO_MOVESELECTION",
    "EMO_PROMOTE",
    "EM_AUTOURLDETECT",
    "EM_CALLAUTOCORRECTPROC",
    "EM_CANPASTE",
    "EM_CANREDO",
    "EM_CONVPOSITION",
    "EM_DISPLAYBAND",
    "EM_EXGETSEL",
    "EM_EXLIMITTEXT",
    "EM_EXLINEFROMCHAR",
    "EM_EXSETSEL",
    "EM_FINDTEXT",
    "EM_FINDTEXTEX",
    "EM_FINDTEXTEXW",
    "EM_FINDTEXTW",
    "EM_FINDWORDBREAK",
    "EM_FORMATRANGE",
    "EM_GETAUTOCORRECTPROC",
    "EM_GETAUTOURLDETECT",
    "EM_GETBIDIOPTIONS",
    "EM_GETCHARFORMAT",
    "EM_GETCTFMODEBIAS",
    "EM_GETCTFOPENSTATUS",
    "EM_GETEDITSTYLE",
    "EM_GETEDITSTYLEEX",
    "EM_GETELLIPSISMODE",
    "EM_GETELLIPSISSTATE",
    "EM_GETEVENTMASK",
    "EM_GETHYPHENATEINFO",
    "EM_GETIMECOLOR",
    "EM_GETIMECOMPMODE",
    "EM_GETIMECOMPTEXT",
    "EM_GETIMEMODEBIAS",
    "EM_GETIMEOPTIONS",
    "EM_GETIMEPROPERTY",
    "EM_GETLANGOPTIONS",
    "EM_GETOLEINTERFACE",
    "EM_GETOPTIONS",
    "EM_GETPAGE",
    "EM_GETPAGEROTATE",
    "EM_GETPARAFORMAT",
    "EM_GETPUNCTUATION",
    "EM_GETQUERYRTFOBJ",
    "EM_GETREDONAME",
    "EM_GETSCROLLPOS",
    "EM_GETSELTEXT",
    "EM_GETSTORYTYPE",
    "EM_GETTABLEPARMS",
    "EM_GETTEXTEX",
    "EM_GETTEXTLENGTHEX",
    "EM_GETTEXTMODE",
    "EM_GETTEXTRANGE",
    "EM_GETTOUCHOPTIONS",
    "EM_GETTYPOGRAPHYOPTIONS",
    "EM_GETUNDONAME",
    "EM_GETVIEWKIND",
    "EM_GETWORDBREAKPROCEX",
    "EM_GETWORDWRAPMODE",
    "EM_GETZOOM",
    "EM_HIDESELECTION",
    "EM_INSERTIMAGE",
    "EM_INSERTTABLE",
    "EM_ISIME",
    "EM_OUTLINE",
    "EM_PASTESPECIAL",
    "EM_RECONVERSION",
    "EM_REDO",
    "EM_REQUESTRESIZE",
    "EM_SELECTIONTYPE",
    "EM_SETAUTOCORRECTPROC",
    "EM_SETBIDIOPTIONS",
    "EM_SETBKGNDCOLOR",
    "EM_SETCHARFORMAT",
    "EM_SETCTFMODEBIAS",
    "EM_SETCTFOPENSTATUS",
    "EM_SETEDITSTYLE",
    "EM_SETEDITSTYLEEX",
    "EM_SETELLIPSISMODE",
    "EM_SETEVENTMASK",
    "EM_SETFONTSIZE",
    "EM_SETHYPHENATEINFO",
    "EM_SETIMECOLOR",
    "EM_SETIMEMODEBIAS",
    "EM_SETIMEOPTIONS",
    "EM_SETLANGOPTIONS",
    "EM_SETOLECALLBACK",
    "EM_SETOPTIONS",
    "EM_SETPAGE",
    "EM_SETPAGEROTATE",
    "EM_SETPALETTE",
    "EM_SETPARAFORMAT",
    "EM_SETPUNCTUATION",
    "EM_SETQUERYRTFOBJ",
    "EM_SETSCROLLPOS",
    "EM_SETSTORYTYPE",
    "EM_SETTABLEPARMS",
    "EM_SETTARGETDEVICE",
    "EM_SETTEXTEX",
    "EM_SETTEXTMODE",
    "EM_SETTOUCHOPTIONS",
    "EM_SETTYPOGRAPHYOPTIONS",
    "EM_SETUIANAME",
    "EM_SETUNDOLIMIT",
    "EM_SETVIEWKIND",
    "EM_SETWORDBREAKPROCEX",
    "EM_SETWORDWRAPMODE",
    "EM_SETZOOM",
    "EM_SHOWSCROLLBAR",
    "EM_STOPGROUPTYPING",
    "EM_STREAMIN",
    "EM_STREAMOUT",
    "ENCORRECTTEXT",
    "ENDCOMPOSITIONNOTIFY",
    "ENDCOMPOSITIONNOTIFY_CODE",
    "ENDROPFILES",
    "ENLINK",
    "ENLOWFIRTF",
    "ENM_CHANGE",
    "ENM_CLIPFORMAT",
    "ENM_CORRECTTEXT",
    "ENM_DRAGDROPDONE",
    "ENM_DROPFILES",
    "ENM_ENDCOMPOSITION",
    "ENM_GROUPTYPINGCHANGE",
    "ENM_HIDELINKTOOLTIP",
    "ENM_IMECHANGE",
    "ENM_KEYEVENTS",
    "ENM_LANGCHANGE",
    "ENM_LINK",
    "ENM_LOWFIRTF",
    "ENM_MOUSEEVENTS",
    "ENM_NONE",
    "ENM_OBJECTPOSITIONS",
    "ENM_PAGECHANGE",
    "ENM_PARAGRAPHEXPANDED",
    "ENM_PROTECTED",
    "ENM_REQUESTRESIZE",
    "ENM_SCROLL",
    "ENM_SCROLLEVENTS",
    "ENM_SELCHANGE",
    "ENM_STARTCOMPOSITION",
    "ENM_UPDATE",
    "ENOLEOPFAILED",
    "ENPROTECTED",
    "ENSAVECLIPBOARD",
    "EN_ALIGNLTR",
    "EN_ALIGNRTL",
    "EN_CLIPFORMAT",
    "EN_CORRECTTEXT",
    "EN_DRAGDROPDONE",
    "EN_DROPFILES",
    "EN_ENDCOMPOSITION",
    "EN_IMECHANGE",
    "EN_LINK",
    "EN_LOWFIRTF",
    "EN_MSGFILTER",
    "EN_OBJECTPOSITIONS",
    "EN_OLEOPFAILED",
    "EN_PAGECHANGE",
    "EN_PARAGRAPHEXPANDED",
    "EN_PROTECTED",
    "EN_REQUESTRESIZE",
    "EN_SAVECLIPBOARD",
    "EN_SELCHANGE",
    "EN_STARTCOMPOSITION",
    "EN_STOPNOUNDO",
    "EPR_0",
    "EPR_180",
    "EPR_270",
    "EPR_90",
    "EPR_SE",
    "ES_DISABLENOSCROLL",
    "ES_EX_NOCALLOLEINIT",
    "ES_NOIME",
    "ES_NOOLEDRAGDROP",
    "ES_SAVESEL",
    "ES_SELECTIONBAR",
    "ES_SELFIME",
    "ES_SUNKEN",
    "ES_VERTICAL",
    "FINDTEXTA",
    "FINDTEXTEXA",
    "FINDTEXTEXW",
    "FINDTEXTW",
    "FORMATRANGE",
    "FR_MATCHALEFHAMZA",
    "FR_MATCHDIAC",
    "FR_MATCHKASHIDA",
    "GCMF_GRIPPER",
    "GCMF_MOUSEMENU",
    "GCMF_SPELLING",
    "GCMF_TOUCHMENU",
    "GCM_MOUSEMENU",
    "GCM_RIGHTMOUSEDROP",
    "GCM_TOUCHMENU",
    "GETCONTEXTMENUEX",
    "GETTEXTEX",
    "GETTEXTEX_FLAGS",
    "GETTEXTLENGTHEX",
    "GETTEXTLENGTHEX_FLAGS",
    "GROUPTYPINGCHANGE",
    "GTL_CLOSE",
    "GTL_DEFAULT",
    "GTL_NUMBYTES",
    "GTL_NUMCHARS",
    "GTL_PRECISE",
    "GTL_USECRLF",
    "GT_DEFAULT",
    "GT_NOHIDDENTEXT",
    "GT_RAWTEXT",
    "GT_SELECTION",
    "GT_USECRLF",
    "HYPHENATEINFO",
    "HYPHRESULT",
    "ICM_CTF",
    "ICM_LEVEL2",
    "ICM_LEVEL2_5",
    "ICM_LEVEL2_SUI",
    "ICM_LEVEL3",
    "ICM_NOTOPEN",
    "ICT_RESULTREADSTR",
    "IMECOMPTEXT",
    "IMECOMPTEXT_FLAGS",
    "IMF_AUTOFONT",
    "IMF_AUTOFONTSIZEADJUST",
    "IMF_AUTOKEYBOARD",
    "IMF_CLOSESTATUSWINDOW",
    "IMF_DUALFONT",
    "IMF_FORCEACTIVE",
    "IMF_FORCEDISABLE",
    "IMF_FORCEENABLE",
    "IMF_FORCEINACTIVE",
    "IMF_FORCENONE",
    "IMF_FORCEREMEMBER",
    "IMF_IMEALWAYSSENDNOTIFY",
    "IMF_IMECANCELCOMPLETE",
    "IMF_IMEUIINTEGRATION",
    "IMF_MULTIPLEEDIT",
    "IMF_NOIMPLICITLANG",
    "IMF_NOKBDLIDFIXUP",
    "IMF_NORTFFONTSUBSTITUTE",
    "IMF_SMODE_NONE",
    "IMF_SMODE_PLAURALCLAUSE",
    "IMF_SPELLCHECKING",
    "IMF_TKBPREDICTION",
    "IMF_UIFONTS",
    "IMF_VERTICAL",
    "IRichEditOle",
    "IRichEditOleCallback",
    "IRicheditUiaOverrides",
    "ITextDisplays",
    "ITextDocument",
    "ITextDocument2",
    "ITextDocument2Old",
    "ITextFont",
    "ITextFont2",
    "ITextHost",
    "ITextHost2",
    "ITextPara",
    "ITextPara2",
    "ITextRange",
    "ITextRange2",
    "ITextRow",
    "ITextSelection",
    "ITextSelection2",
    "ITextServices",
    "ITextServices2",
    "ITextStory",
    "ITextStoryRanges",
    "ITextStoryRanges2",
    "ITextStrings",
    "KHYPH",
    "KHYPH_khyphAddBefore",
    "KHYPH_khyphChangeAfter",
    "KHYPH_khyphChangeBefore",
    "KHYPH_khyphDelAndChange",
    "KHYPH_khyphDeleteBefore",
    "KHYPH_khyphNil",
    "KHYPH_khyphNormal",
    "MANCODE",
    "MAX_TABLE_CELLS",
    "MAX_TAB_STOPS",
    "MBOLD",
    "MFRAK",
    "MGREEK",
    "MINIT",
    "MISOL",
    "MITAL",
    "MLOOP",
    "MMATH",
    "MMONO",
    "MOPEN",
    "MOPENA",
    "MROMN",
    "MSANS",
    "MSCRP",
    "MSFTEDIT_CLASS",
    "MSGFILTER",
    "MSTRCH",
    "MTAIL",
    "OBJECTPOSITIONS",
    "OBJECTTYPE",
    "OBJECTTYPE_tomAccent",
    "OBJECTTYPE_tomBox",
    "OBJECTTYPE_tomBoxedFormula",
    "OBJECTTYPE_tomBrackets",
    "OBJECTTYPE_tomBracketsWithSeps",
    "OBJECTTYPE_tomEq",
    "OBJECTTYPE_tomEquationArray",
    "OBJECTTYPE_tomFraction",
    "OBJECTTYPE_tomFunctionApply",
    "OBJECTTYPE_tomHorzVert",
    "OBJECTTYPE_tomLeftSubSup",
    "OBJECTTYPE_tomLowerLimit",
    "OBJECTTYPE_tomMath",
    "OBJECTTYPE_tomMatrix",
    "OBJECTTYPE_tomNary",
    "OBJECTTYPE_tomObjectMax",
    "OBJECTTYPE_tomOpChar",
    "OBJECTTYPE_tomOverbar",
    "OBJECTTYPE_tomPhantom",
    "OBJECTTYPE_tomRadical",
    "OBJECTTYPE_tomRuby",
    "OBJECTTYPE_tomSimpleText",
    "OBJECTTYPE_tomSlashedFraction",
    "OBJECTTYPE_tomStack",
    "OBJECTTYPE_tomStretchStack",
    "OBJECTTYPE_tomSubSup",
    "OBJECTTYPE_tomSubscript",
    "OBJECTTYPE_tomSuperscript",
    "OBJECTTYPE_tomUnderbar",
    "OBJECTTYPE_tomUpperLimit",
    "OBJECTTYPE_tomWarichu",
    "OLEOP_DOVERB",
    "PARAFORMAT",
    "PARAFORMAT2",
    "PARAFORMAT_ALIGNMENT",
    "PARAFORMAT_BORDERS",
    "PARAFORMAT_BORDERS_AUTOCOLOR",
    "PARAFORMAT_BORDERS_BOTTOM",
    "PARAFORMAT_BORDERS_INSIDE",
    "PARAFORMAT_BORDERS_LEFT",
    "PARAFORMAT_BORDERS_OUTSIDE",
    "PARAFORMAT_BORDERS_RIGHT",
    "PARAFORMAT_BORDERS_TOP",
    "PARAFORMAT_MASK",
    "PARAFORMAT_NUMBERING",
    "PARAFORMAT_NUMBERING_STYLE",
    "PARAFORMAT_SHADING_STYLE",
    "PARAFORMAT_SHADING_STYLE_DARK_DOWN_DIAG",
    "PARAFORMAT_SHADING_STYLE_DARK_GRID",
    "PARAFORMAT_SHADING_STYLE_DARK_HORIZ",
    "PARAFORMAT_SHADING_STYLE_DARK_TRELLIS",
    "PARAFORMAT_SHADING_STYLE_DARK_UP_DIAG",
    "PARAFORMAT_SHADING_STYLE_DARK_VERT",
    "PARAFORMAT_SHADING_STYLE_LIGHT_DOWN_DIAG",
    "PARAFORMAT_SHADING_STYLE_LIGHT_GRID",
    "PARAFORMAT_SHADING_STYLE_LIGHT_HORZ",
    "PARAFORMAT_SHADING_STYLE_LIGHT_TRELLIS",
    "PARAFORMAT_SHADING_STYLE_LIGHT_UP_DIAG",
    "PARAFORMAT_SHADING_STYLE_LIGHT_VERT",
    "PARAFORMAT_SHADING_STYLE_NONE",
    "PC_DELIMITER",
    "PC_FOLLOWING",
    "PC_LEADING",
    "PC_OVERFLOW",
    "PCreateTextServices",
    "PFA_CENTER",
    "PFA_FULL_GLYPHS",
    "PFA_FULL_INTERLETTER",
    "PFA_FULL_INTERWORD",
    "PFA_FULL_NEWSPAPER",
    "PFA_FULL_SCALED",
    "PFA_JUSTIFY",
    "PFA_LEFT",
    "PFA_RIGHT",
    "PFM_ALIGNMENT",
    "PFM_BORDER",
    "PFM_BOX",
    "PFM_COLLAPSED",
    "PFM_DONOTHYPHEN",
    "PFM_KEEP",
    "PFM_KEEPNEXT",
    "PFM_LINESPACING",
    "PFM_NOLINENUMBER",
    "PFM_NOWIDOWCONTROL",
    "PFM_NUMBERING",
    "PFM_NUMBERINGSTART",
    "PFM_NUMBERINGSTYLE",
    "PFM_NUMBERINGTAB",
    "PFM_OFFSET",
    "PFM_OFFSETINDENT",
    "PFM_OUTLINELEVEL",
    "PFM_PAGEBREAKBEFORE",
    "PFM_RESERVED2",
    "PFM_RIGHTINDENT",
    "PFM_RTLPARA",
    "PFM_SHADING",
    "PFM_SIDEBYSIDE",
    "PFM_SPACEAFTER",
    "PFM_SPACEBEFORE",
    "PFM_STARTINDENT",
    "PFM_STYLE",
    "PFM_TABLE",
    "PFM_TABLEROWDELIMITER",
    "PFM_TABSTOPS",
    "PFM_TEXTWRAPPINGBREAK",
    "PFNS_NEWNUMBER",
    "PFNS_NONUMBER",
    "PFNS_PAREN",
    "PFNS_PARENS",
    "PFNS_PERIOD",
    "PFNS_PLAIN",
    "PFN_ARABIC",
    "PFN_BULLET",
    "PFN_LCLETTER",
    "PFN_LCROMAN",
    "PFN_UCLETTER",
    "PFN_UCROMAN",
    "PShutdownTextServices",
    "PUNCTUATION",
    "REOBJECT",
    "REOBJECT_FLAGS",
    "REO_ALIGNTORIGHT",
    "REO_BELOWBASELINE",
    "REO_BLANK",
    "REO_CANROTATE",
    "REO_DONTNEEDPALETTE",
    "REO_DYNAMICSIZE",
    "REO_GETMETAFILE",
    "REO_GETOBJ_ALL_INTERFACES",
    "REO_GETOBJ_NO_INTERFACES",
    "REO_GETOBJ_POLEOBJ",
    "REO_GETOBJ_POLESITE",
    "REO_GETOBJ_PSTG",
    "REO_HILITED",
    "REO_INPLACEACTIVE",
    "REO_INVERTEDSELECT",
    "REO_LINK",
    "REO_LINKAVAILABLE",
    "REO_NULL",
    "REO_OPEN",
    "REO_OWNERDRAWSELECT",
    "REO_READWRITEMASK",
    "REO_RESIZABLE",
    "REO_SELECTED",
    "REO_STATIC",
    "REO_USEASBACKGROUND",
    "REO_WRAPTEXTAROUND",
    "REPASTESPECIAL",
    "REQRESIZE",
    "RICHEDIT60_CLASS",
    "RICHEDIT_CLASS",
    "RICHEDIT_CLASS10A",
    "RICHEDIT_CLASSA",
    "RICHEDIT_CLASSW",
    "RICHEDIT_IMAGE_PARAMETERS",
    "RICH_EDIT_GET_CONTEXT_MENU_SEL_TYPE",
    "RICH_EDIT_GET_OBJECT_FLAGS",
    "RTO_DISABLEHANDLES",
    "RTO_READINGMODE",
    "RTO_SHOWHANDLES",
    "SCF_ALL",
    "SCF_ASSOCIATEFONT",
    "SCF_ASSOCIATEFONT2",
    "SCF_CHARREPFROMLCID",
    "SCF_DEFAULT",
    "SCF_NOKBUPDATE",
    "SCF_SELECTION",
    "SCF_SMARTFONT",
    "SCF_USEUIRULES",
    "SCF_WORD",
    "SELCHANGE",
    "SEL_EMPTY",
    "SEL_MULTICHAR",
    "SEL_MULTIOBJECT",
    "SEL_OBJECT",
    "SEL_TEXT",
    "SES_ALLOWBEEPS",
    "SES_BEEPONMAXTEXT",
    "SES_BIDI",
    "SES_CTFALLOWEMBED",
    "SES_CTFALLOWPROOFING",
    "SES_CTFALLOWSMARTTAG",
    "SES_CTFNOLOCK",
    "SES_CUSTOMLOOK",
    "SES_DEFAULTLATINLIGA",
    "SES_DRAFTMODE",
    "SES_EMULATE10",
    "SES_EMULATESYSEDIT",
    "SES_EXTENDBACKCOLOR",
    "SES_EX_HANDLEFRIENDLYURL",
    "SES_EX_HIDETEMPFORMAT",
    "SES_EX_MULTITOUCH",
    "SES_EX_NOACETATESELECTION",
    "SES_EX_NOMATH",
    "SES_EX_NOTABLE",
    "SES_EX_NOTHEMING",
    "SES_EX_USEMOUSEWPARAM",
    "SES_EX_USESINGLELINE",
    "SES_HIDEGRIDLINES",
    "SES_HYPERLINKTOOLTIPS",
    "SES_LBSCROLLNOTIFY",
    "SES_LOGICALCARET",
    "SES_LOWERCASE",
    "SES_MAPCPS",
    "SES_MAX",
    "SES_MULTISELECT",
    "SES_NOEALINEHEIGHTADJUST",
    "SES_NOFOCUSLINKNOTIFY",
    "SES_NOIME",
    "SES_NOINPUTSEQUENCECHK",
    "SES_SCROLLONKILLFOCUS",
    "SES_SMARTDRAGDROP",
    "SES_UPPERCASE",
    "SES_USEAIMM",
    "SES_USEATFONT",
    "SES_USECRLF",
    "SES_USECTF",
    "SES_WORDDRAGDROP",
    "SES_XLTCRCRLFTOCR",
    "SETTEXTEX",
    "SFF_KEEPDOCINFO",
    "SFF_PERSISTVIEWSCALE",
    "SFF_PLAINRTF",
    "SFF_PWD",
    "SFF_SELECTION",
    "SFF_WRITEXTRAPAR",
    "SF_NCRFORNONASCII",
    "SF_RTF",
    "SF_RTFNOOBJS",
    "SF_RTFVAL",
    "SF_TEXT",
    "SF_TEXTIZED",
    "SF_UNICODE",
    "SF_USECODEPAGE",
    "SPF_DONTSETDEFAULT",
    "SPF_SETDEFAULT",
    "ST_DEFAULT",
    "ST_KEEPUNDO",
    "ST_NEWCHARS",
    "ST_SELECTION",
    "ST_UNICODE",
    "S_MSG_KEY_IGNORED",
    "TABLECELLPARMS",
    "TABLEROWPARMS",
    "TEXTMODE",
    "TEXTRANGEA",
    "TEXTRANGEW",
    "TM_MULTICODEPAGE",
    "TM_MULTILEVELUNDO",
    "TM_PLAINTEXT",
    "TM_RICHTEXT",
    "TM_SINGLECODEPAGE",
    "TM_SINGLELEVELUNDO",
    "TO_ADVANCEDLAYOUT",
    "TO_ADVANCEDTYPOGRAPHY",
    "TO_DISABLECUSTOMTEXTOUT",
    "TO_SIMPLELINEBREAK",
    "TXES_ISDIALOG",
    "TXTBACKSTYLE",
    "TXTBACK_OPAQUE",
    "TXTBACK_TRANSPARENT",
    "TXTBIT_ADVANCEDINPUT",
    "TXTBIT_ALLOWBEEP",
    "TXTBIT_AUTOWORDSEL",
    "TXTBIT_BACKSTYLECHANGE",
    "TXTBIT_CHARFORMATCHANGE",
    "TXTBIT_CLIENTRECTCHANGE",
    "TXTBIT_D2DDWRITE",
    "TXTBIT_D2DPIXELSNAPPED",
    "TXTBIT_D2DSIMPLETYPOGRAPHY",
    "TXTBIT_D2DSUBPIXELLINES",
    "TXTBIT_DISABLEDRAG",
    "TXTBIT_EXTENTCHANGE",
    "TXTBIT_FLASHLASTPASSWORDCHAR",
    "TXTBIT_HIDESELECTION",
    "TXTBIT_MAXLENGTHCHANGE",
    "TXTBIT_MULTILINE",
    "TXTBIT_NOTHREADREFCOUNT",
    "TXTBIT_PARAFORMATCHANGE",
    "TXTBIT_READONLY",
    "TXTBIT_RICHTEXT",
    "TXTBIT_SAVESELECTION",
    "TXTBIT_SCROLLBARCHANGE",
    "TXTBIT_SELBARCHANGE",
    "TXTBIT_SHOWACCELERATOR",
    "TXTBIT_SHOWPASSWORD",
    "TXTBIT_USECURRENTBKG",
    "TXTBIT_USEPASSWORD",
    "TXTBIT_VERTICAL",
    "TXTBIT_VIEWINSETCHANGE",
    "TXTBIT_WORDWRAP",
    "TXTHITRESULT",
    "TXTHITRESULT_CLOSE",
    "TXTHITRESULT_HIT",
    "TXTHITRESULT_NOHIT",
    "TXTHITRESULT_TRANSPARENT",
    "TXTNATURALSIZE",
    "TXTNS_EMU",
    "TXTNS_FITTOCONTENT",
    "TXTNS_FITTOCONTENT2",
    "TXTNS_FITTOCONTENT3",
    "TXTNS_FITTOCONTENTWSP",
    "TXTNS_INCLUDELASTLINE",
    "TXTNS_ROUNDTOLINE",
    "TXTVIEW",
    "TXTVIEW_ACTIVE",
    "TXTVIEW_INACTIVE",
    "UID_AUTOTABLE",
    "UID_CUT",
    "UID_DELETE",
    "UID_DRAGDROP",
    "UID_PASTE",
    "UID_TYPING",
    "UID_UNKNOWN",
    "UNDONAMEID",
    "VM_NORMAL",
    "VM_OUTLINE",
    "VM_PAGE",
    "WBF_CUSTOM",
    "WBF_LEVEL1",
    "WBF_LEVEL2",
    "WBF_OVERFLOW",
    "WBF_WORDBREAK",
    "WBF_WORDWRAP",
    "WB_MOVEWORDNEXT",
    "WB_MOVEWORDPREV",
    "WB_NEXTBREAK",
    "WB_PREVBREAK",
    "cchTextLimitDefault",
    "lDefaultTab",
    "tomConstants",
    "tomConstants_tomAboriginal",
    "tomConstants_tomAdjustCRLF",
    "tomConstants_tomAlignBar",
    "tomConstants_tomAlignCenter",
    "tomConstants_tomAlignDecimal",
    "tomConstants_tomAlignDefault",
    "tomConstants_tomAlignInterLetter",
    "tomConstants_tomAlignInterWord",
    "tomConstants_tomAlignJustify",
    "tomConstants_tomAlignLeft",
    "tomConstants_tomAlignMatchAscentDescent",
    "tomConstants_tomAlignNewspaper",
    "tomConstants_tomAlignRight",
    "tomConstants_tomAlignScaled",
    "tomConstants_tomAllCaps",
    "tomConstants_tomAllowFinalEOP",
    "tomConstants_tomAllowMathBold",
    "tomConstants_tomAllowOffClient",
    "tomConstants_tomAnimationMax",
    "tomConstants_tomAnsi",
    "tomConstants_tomApplyLater",
    "tomConstants_tomApplyNow",
    "tomConstants_tomApplyRtfDocProps",
    "tomConstants_tomApplyTmp",
    "tomConstants_tomArabic",
    "tomConstants_tomArmenian",
    "tomConstants_tomAtEnd",
    "tomConstants_tomAutoBackColor",
    "tomConstants_tomAutoColor",
    "tomConstants_tomAutoLinkEmail",
    "tomConstants_tomAutoLinkPath",
    "tomConstants_tomAutoLinkPhone",
    "tomConstants_tomAutoLinkURL",
    "tomConstants_tomAutoSpaceAlpha",
    "tomConstants_tomAutoSpaceNumeric",
    "tomConstants_tomAutoSpaceParens",
    "tomConstants_tomAutoTextColor",
    "tomConstants_tomBIG5",
    "tomConstants_tomBackward",
    "tomConstants_tomBaltic",
    "tomConstants_tomBengali",
    "tomConstants_tomBlinkingBackground",
    "tomConstants_tomBold",
    "tomConstants_tomBoxAlignCenter",
    "tomConstants_tomBoxHideBottom",
    "tomConstants_tomBoxHideLeft",
    "tomConstants_tomBoxHideRight",
    "tomConstants_tomBoxHideTop",
    "tomConstants_tomBoxStrikeBLTR",
    "tomConstants_tomBoxStrikeH",
    "tomConstants_tomBoxStrikeTLBR",
    "tomConstants_tomBoxStrikeV",
    "tomConstants_tomBraille",
    "tomConstants_tomCacheParms",
    "tomConstants_tomCanCopy",
    "tomConstants_tomCanRedo",
    "tomConstants_tomCanUndo",
    "tomConstants_tomCell",
    "tomConstants_tomCellStructureChangeOnly",
    "tomConstants_tomCharFormat",
    "tomConstants_tomCharRepFromLcid",
    "tomConstants_tomCharRepMax",
    "tomConstants_tomCharacter",
    "tomConstants_tomCharset",
    "tomConstants_tomCheckTextLimit",
    "tomConstants_tomCherokee",
    "tomConstants_tomClientCoord",
    "tomConstants_tomClientLink",
    "tomConstants_tomCluster",
    "tomConstants_tomCollapseEnd",
    "tomConstants_tomCollapseStart",
    "tomConstants_tomColumn",
    "tomConstants_tomCommentsStory",
    "tomConstants_tomCompressMax",
    "tomConstants_tomCompressNone",
    "tomConstants_tomCompressPunctuation",
    "tomConstants_tomCompressPunctuationAndKana",
    "tomConstants_tomConvertMathChar",
    "tomConstants_tomConvertRTF",
    "tomConstants_tomCreateAlways",
    "tomConstants_tomCreateNew",
    "tomConstants_tomCyrillic",
    "tomConstants_tomDash",
    "tomConstants_tomDashDot",
    "tomConstants_tomDashDotDot",
    "tomConstants_tomDashes",
    "tomConstants_tomDecDecSize",
    "tomConstants_tomDecSize",
    "tomConstants_tomDefault",
    "tomConstants_tomDefaultCharRep",
    "tomConstants_tomDefaultTab",
    "tomConstants_tomDeseret",
    "tomConstants_tomDevanagari",
    "tomConstants_tomDisableSmartFont",
    "tomConstants_tomDisabled",
    "tomConstants_tomDocAutoLink",
    "tomConstants_tomDocMathBuild",
    "tomConstants_tomDontGrowWithContent",
    "tomConstants_tomDots",
    "tomConstants_tomDotted",
    "tomConstants_tomDouble",
    "tomConstants_tomDoubleWave",
    "tomConstants_tomDoublestrike",
    "tomConstants_tomEastEurope",
    "tomConstants_tomEllipsisEnd",
    "tomConstants_tomEllipsisMode",
    "tomConstants_tomEllipsisNone",
    "tomConstants_tomEllipsisPresent",
    "tomConstants_tomEllipsisState",
    "tomConstants_tomEllipsisWord",
    "tomConstants_tomEmbeddedFont",
    "tomConstants_tomEmboss",
    "tomConstants_tomEmoji",
    "tomConstants_tomEnableSmartFont",
    "tomConstants_tomEnd",
    "tomConstants_tomEndnotesStory",
    "tomConstants_tomEqArrayAlignBottomRow",
    "tomConstants_tomEqArrayAlignCenter",
    "tomConstants_tomEqArrayAlignMask",
    "tomConstants_tomEqArrayAlignTopRow",
    "tomConstants_tomEqArrayLayoutWidth",
    "tomConstants_tomEquals",
    "tomConstants_tomEthiopic",
    "tomConstants_tomEvenPagesFooterStory",
    "tomConstants_tomEvenPagesHeaderStory",
    "tomConstants_tomExtend",
    "tomConstants_tomExtendedChar",
    "tomConstants_tomFalse",
    "tomConstants_tomFindStory",
    "tomConstants_tomFirstPageFooterStory",
    "tomConstants_tomFirstPageHeaderStory",
    "tomConstants_tomFoldMathAlpha",
    "tomConstants_tomFontAlignmentAuto",
    "tomConstants_tomFontAlignmentBaseline",
    "tomConstants_tomFontAlignmentBottom",
    "tomConstants_tomFontAlignmentCenter",
    "tomConstants_tomFontAlignmentMax",
    "tomConstants_tomFontAlignmentTop",
    "tomConstants_tomFontBound",
    "tomConstants_tomFontPropAlign",
    "tomConstants_tomFontPropTeXStyle",
    "tomConstants_tomFontStretch",
    "tomConstants_tomFontStretchCondensed",
    "tomConstants_tomFontStretchDefault",
    "tomConstants_tomFontStretchExpanded",
    "tomConstants_tomFontStretchExtraCondensed",
    "tomConstants_tomFontStretchExtraExpanded",
    "tomConstants_tomFontStretchNormal",
    "tomConstants_tomFontStretchSemiCondensed",
    "tomConstants_tomFontStretchSemiExpanded",
    "tomConstants_tomFontStretchUltraCondensed",
    "tomConstants_tomFontStretchUltraExpanded",
    "tomConstants_tomFontStyle",
    "tomConstants_tomFontStyleItalic",
    "tomConstants_tomFontStyleOblique",
    "tomConstants_tomFontStyleUpright",
    "tomConstants_tomFontWeightBlack",
    "tomConstants_tomFontWeightBold",
    "tomConstants_tomFontWeightDefault",
    "tomConstants_tomFontWeightExtraBlack",
    "tomConstants_tomFontWeightExtraBold",
    "tomConstants_tomFontWeightExtraLight",
    "tomConstants_tomFontWeightHeavy",
    "tomConstants_tomFontWeightLight",
    "tomConstants_tomFontWeightMedium",
    "tomConstants_tomFontWeightNormal",
    "tomConstants_tomFontWeightRegular",
    "tomConstants_tomFontWeightSemiBold",
    "tomConstants_tomFontWeightThin",
    "tomConstants_tomFootnotesStory",
    "tomConstants_tomForward",
    "tomConstants_tomFriendlyLinkAddress",
    "tomConstants_tomFriendlyLinkName",
    "tomConstants_tomFunctionTypeIsLim",
    "tomConstants_tomFunctionTypeNone",
    "tomConstants_tomFunctionTypeTakesArg",
    "tomConstants_tomFunctionTypeTakesLim",
    "tomConstants_tomFunctionTypeTakesLim2",
    "tomConstants_tomGB2312",
    "tomConstants_tomGeorgian",
    "tomConstants_tomGetHeightOnly",
    "tomConstants_tomGlagolitic",
    "tomConstants_tomGothic",
    "tomConstants_tomGravityBack",
    "tomConstants_tomGravityBackward",
    "tomConstants_tomGravityFore",
    "tomConstants_tomGravityForward",
    "tomConstants_tomGravityIn",
    "tomConstants_tomGravityOut",
    "tomConstants_tomGravityUI",
    "tomConstants_tomGreek",
    "tomConstants_tomGrowWithContent",
    "tomConstants_tomGujarati",
    "tomConstants_tomGurmukhi",
    "tomConstants_tomHContCell",
    "tomConstants_tomHStartCell",
    "tomConstants_tomHTML",
    "tomConstants_tomHair",
    "tomConstants_tomHangul",
    "tomConstants_tomHardParagraph",
    "tomConstants_tomHeavyWave",
    "tomConstants_tomHebrew",
    "tomConstants_tomHidden",
    "tomConstants_tomHstring",
    "tomConstants_tomIgnoreCurrentFont",
    "tomConstants_tomIgnoreNumberStyle",
    "tomConstants_tomImprint",
    "tomConstants_tomIncIncSize",
    "tomConstants_tomIncSize",
    "tomConstants_tomIncludeInset",
    "tomConstants_tomIncludeNumbering",
    "tomConstants_tomInlineObject",
    "tomConstants_tomInlineObjectArg",
    "tomConstants_tomInlineObjectStart",
    "tomConstants_tomItalic",
    "tomConstants_tomJamo",
    "tomConstants_tomKannada",
    "tomConstants_tomKayahli",
    "tomConstants_tomKharoshthi",
    "tomConstants_tomKhmer",
    "tomConstants_tomKoreanBlockCaret",
    "tomConstants_tomLanguageTag",
    "tomConstants_tomLao",
    "tomConstants_tomLasVegasLights",
    "tomConstants_tomLayoutColumn",
    "tomConstants_tomLeafLine",
    "tomConstants_tomLimbu",
    "tomConstants_tomLimitAlignCenter",
    "tomConstants_tomLimitAlignLeft",
    "tomConstants_tomLimitAlignMask",
    "tomConstants_tomLimitAlignRight",
    "tomConstants_tomLimitsDefault",
    "tomConstants_tomLimitsOpposite",
    "tomConstants_tomLimitsSubSup",
    "tomConstants_tomLimitsUnderOver",
    "tomConstants_tomLine",
    "tomConstants_tomLineSpace1pt5",
    "tomConstants_tomLineSpaceAtLeast",
    "tomConstants_tomLineSpaceDouble",
    "tomConstants_tomLineSpaceExactly",
    "tomConstants_tomLineSpaceMultiple",
    "tomConstants_tomLineSpacePercent",
    "tomConstants_tomLineSpaceSingle",
    "tomConstants_tomLines",
    "tomConstants_tomLink",
    "tomConstants_tomLinkProtected",
    "tomConstants_tomListBullet",
    "tomConstants_tomListMinus",
    "tomConstants_tomListNoNumber",
    "tomConstants_tomListNone",
    "tomConstants_tomListNumberAsArabic",
    "tomConstants_tomListNumberAsLCLetter",
    "tomConstants_tomListNumberAsLCRoman",
    "tomConstants_tomListNumberAsSequence",
    "tomConstants_tomListNumberAsUCLetter",
    "tomConstants_tomListNumberAsUCRoman",
    "tomConstants_tomListNumberedArabic1",
    "tomConstants_tomListNumberedArabic2",
    "tomConstants_tomListNumberedArabicWide",
    "tomConstants_tomListNumberedBlackCircleWingding",
    "tomConstants_tomListNumberedChS",
    "tomConstants_tomListNumberedChT",
    "tomConstants_tomListNumberedCircle",
    "tomConstants_tomListNumberedHebrew",
    "tomConstants_tomListNumberedHindiAlpha",
    "tomConstants_tomListNumberedHindiAlpha1",
    "tomConstants_tomListNumberedHindiNum",
    "tomConstants_tomListNumberedJpnChS",
    "tomConstants_tomListNumberedJpnKor",
    "tomConstants_tomListNumberedThaiAlpha",
    "tomConstants_tomListNumberedThaiNum",
    "tomConstants_tomListNumberedWhiteCircleWingding",
    "tomConstants_tomListParentheses",
    "tomConstants_tomListPeriod",
    "tomConstants_tomListPlain",
    "tomConstants_tomLisu",
    "tomConstants_tomLongDash",
    "tomConstants_tomLowerCase",
    "tomConstants_tomMac",
    "tomConstants_tomMainTextStory",
    "tomConstants_tomMalayalam",
    "tomConstants_tomMarchingBlackAnts",
    "tomConstants_tomMarchingRedAnts",
    "tomConstants_tomMatchAscii",
    "tomConstants_tomMatchCase",
    "tomConstants_tomMatchCharRep",
    "tomConstants_tomMatchFontSignature",
    "tomConstants_tomMatchMathFont",
    "tomConstants_tomMatchPattern",
    "tomConstants_tomMatchWord",
    "tomConstants_tomMathArgShadingEnd",
    "tomConstants_tomMathArgShadingStart",
    "tomConstants_tomMathBreakCenter",
    "tomConstants_tomMathBreakLeft",
    "tomConstants_tomMathBreakRight",
    "tomConstants_tomMathBrkBinAfter",
    "tomConstants_tomMathBrkBinBefore",
    "tomConstants_tomMathBrkBinDup",
    "tomConstants_tomMathBrkBinMask",
    "tomConstants_tomMathBrkBinSubMM",
    "tomConstants_tomMathBrkBinSubMP",
    "tomConstants_tomMathBrkBinSubMask",
    "tomConstants_tomMathBrkBinSubPM",
    "tomConstants_tomMathCFCheck",
    "tomConstants_tomMathDispAlignCenter",
    "tomConstants_tomMathDispAlignCenterGroup",
    "tomConstants_tomMathDispAlignLeft",
    "tomConstants_tomMathDispAlignMask",
    "tomConstants_tomMathDispAlignRight",
    "tomConstants_tomMathDispDef",
    "tomConstants_tomMathDispFracTeX",
    "tomConstants_tomMathDispIntUnderOver",
    "tomConstants_tomMathDispNaryGrow",
    "tomConstants_tomMathDispNarySubSup",
    "tomConstants_tomMathDocDiffDefault",
    "tomConstants_tomMathDocDiffItalic",
    "tomConstants_tomMathDocDiffMask",
    "tomConstants_tomMathDocDiffOpenItalic",
    "tomConstants_tomMathDocDiffUpright",
    "tomConstants_tomMathDocEmptyArgAlways",
    "tomConstants_tomMathDocEmptyArgAuto",
    "tomConstants_tomMathDocEmptyArgMask",
    "tomConstants_tomMathDocEmptyArgNever",
    "tomConstants_tomMathDocSbSpOpUnchanged",
    "tomConstants_tomMathEnableRtl",
    "tomConstants_tomMathEqAlign",
    "tomConstants_tomMathInterSpace",
    "tomConstants_tomMathIntraSpace",
    "tomConstants_tomMathLMargin",
    "tomConstants_tomMathManualBreakMask",
    "tomConstants_tomMathObjShadingEnd",
    "tomConstants_tomMathObjShadingStart",
    "tomConstants_tomMathParaAlignCenter",
    "tomConstants_tomMathParaAlignCenterGroup",
    "tomConstants_tomMathParaAlignDefault",
    "tomConstants_tomMathParaAlignLeft",
    "tomConstants_tomMathParaAlignRight",
    "tomConstants_tomMathPostSpace",
    "tomConstants_tomMathPreSpace",
    "tomConstants_tomMathRMargin",
    "tomConstants_tomMathRelSize",
    "tomConstants_tomMathVariant",
    "tomConstants_tomMathWrapIndent",
    "tomConstants_tomMathWrapRight",
    "tomConstants_tomMathZone",
    "tomConstants_tomMathZoneDisplay",
    "tomConstants_tomMathZoneNoBuildUp",
    "tomConstants_tomMathZoneOrdinary",
    "tomConstants_tomMatrixAlignBottomRow",
    "tomConstants_tomMatrixAlignCenter",
    "tomConstants_tomMatrixAlignMask",
    "tomConstants_tomMatrixAlignTopRow",
    "tomConstants_tomModWidthPairs",
    "tomConstants_tomModWidthSpace",
    "tomConstants_tomMongolian",
    "tomConstants_tomMove",
    "tomConstants_tomMyanmar",
    "tomConstants_tomNKo",
    "tomConstants_tomNewTaiLue",
    "tomConstants_tomNoAnimation",
    "tomConstants_tomNoBreak",
    "tomConstants_tomNoHidden",
    "tomConstants_tomNoIME",
    "tomConstants_tomNoLink",
    "tomConstants_tomNoMathZoneBrackets",
    "tomConstants_tomNoSelection",
    "tomConstants_tomNoUCGreekItalic",
    "tomConstants_tomNoUpScroll",
    "tomConstants_tomNoVpScroll",
    "tomConstants_tomNone",
    "tomConstants_tomNormalCaret",
    "tomConstants_tomNullCaret",
    "tomConstants_tomOEM",
    "tomConstants_tomObject",
    "tomConstants_tomObjectArg",
    "tomConstants_tomOgham",
    "tomConstants_tomOpenAlways",
    "tomConstants_tomOpenExisting",
    "tomConstants_tomOriya",
    "tomConstants_tomOsmanya",
    "tomConstants_tomOutline",
    "tomConstants_tomOverlapping",
    "tomConstants_tomPC437",
    "tomConstants_tomPage",
    "tomConstants_tomParaEffectBox",
    "tomConstants_tomParaEffectCollapsed",
    "tomConstants_tomParaEffectDoNotHyphen",
    "tomConstants_tomParaEffectKeep",
    "tomConstants_tomParaEffectKeepNext",
    "tomConstants_tomParaEffectNoLineNumber",
    "tomConstants_tomParaEffectNoWidowControl",
    "tomConstants_tomParaEffectOutlineLevel",
    "tomConstants_tomParaEffectPageBreakBefore",
    "tomConstants_tomParaEffectRTL",
    "tomConstants_tomParaEffectSideBySide",
    "tomConstants_tomParaEffectTable",
    "tomConstants_tomParaEffectTableRowDelimiter",
    "tomConstants_tomParaFormat",
    "tomConstants_tomParaPropMathAlign",
    "tomConstants_tomParaStyleHeading1",
    "tomConstants_tomParaStyleHeading2",
    "tomConstants_tomParaStyleHeading3",
    "tomConstants_tomParaStyleHeading4",
    "tomConstants_tomParaStyleHeading5",
    "tomConstants_tomParaStyleHeading6",
    "tomConstants_tomParaStyleHeading7",
    "tomConstants_tomParaStyleHeading8",
    "tomConstants_tomParaStyleHeading9",
    "tomConstants_tomParaStyleNormal",
    "tomConstants_tomParagraph",
    "tomConstants_tomPasteFile",
    "tomConstants_tomPhagsPa",
    "tomConstants_tomPhantomASmash",
    "tomConstants_tomPhantomDSmash",
    "tomConstants_tomPhantomHSmash",
    "tomConstants_tomPhantomHorz",
    "tomConstants_tomPhantomShow",
    "tomConstants_tomPhantomSmash",
    "tomConstants_tomPhantomTransparent",
    "tomConstants_tomPhantomVert",
    "tomConstants_tomPhantomZeroAscent",
    "tomConstants_tomPhantomZeroDescent",
    "tomConstants_tomPhantomZeroWidth",
    "tomConstants_tomPrimaryFooterStory",
    "tomConstants_tomPrimaryHeaderStory",
    "tomConstants_tomProcessId",
    "tomConstants_tomProtected",
    "tomConstants_tomRE10Mode",
    "tomConstants_tomRTF",
    "tomConstants_tomReadOnly",
    "tomConstants_tomReplaceStory",
    "tomConstants_tomResume",
    "tomConstants_tomRevised",
    "tomConstants_tomRow",
    "tomConstants_tomRowApplyDefault",
    "tomConstants_tomRowHeightActual",
    "tomConstants_tomRowUpdate",
    "tomConstants_tomRubyAlign010",
    "tomConstants_tomRubyAlign121",
    "tomConstants_tomRubyAlignCenter",
    "tomConstants_tomRubyAlignLeft",
    "tomConstants_tomRubyAlignRight",
    "tomConstants_tomRubyBelow",
    "tomConstants_tomRunic",
    "tomConstants_tomScratchStory",
    "tomConstants_tomScreen",
    "tomConstants_tomSection",
    "tomConstants_tomSelActive",
    "tomConstants_tomSelAtEOL",
    "tomConstants_tomSelOvertype",
    "tomConstants_tomSelRange",
    "tomConstants_tomSelReplace",
    "tomConstants_tomSelStartActive",
    "tomConstants_tomSelectionBlock",
    "tomConstants_tomSelectionColumn",
    "tomConstants_tomSelectionFrame",
    "tomConstants_tomSelectionIP",
    "tomConstants_tomSelectionInlineShape",
    "tomConstants_tomSelectionNormal",
    "tomConstants_tomSelectionRow",
    "tomConstants_tomSelectionShape",
    "tomConstants_tomSelfIME",
    "tomConstants_tomSentence",
    "tomConstants_tomSentenceCase",
    "tomConstants_tomShadow",
    "tomConstants_tomShareDenyRead",
    "tomConstants_tomShareDenyWrite",
    "tomConstants_tomShiftJIS",
    "tomConstants_tomShimmer",
    "tomConstants_tomShowDegPlaceHldr",
    "tomConstants_tomShowLLimPlaceHldr",
    "tomConstants_tomShowMatPlaceHldr",
    "tomConstants_tomShowULimPlaceHldr",
    "tomConstants_tomSingle",
    "tomConstants_tomSinhala",
    "tomConstants_tomSizeScript",
    "tomConstants_tomSizeScriptScript",
    "tomConstants_tomSizeText",
    "tomConstants_tomSmallCaps",
    "tomConstants_tomSpaceBinary",
    "tomConstants_tomSpaceDefault",
    "tomConstants_tomSpaceDifferential",
    "tomConstants_tomSpaceMask",
    "tomConstants_tomSpaceOrd",
    "tomConstants_tomSpaceRelational",
    "tomConstants_tomSpaceSkip",
    "tomConstants_tomSpaceUnary",
    "tomConstants_tomSpaces",
    "tomConstants_tomSparkleText",
    "tomConstants_tomStart",
    "tomConstants_tomStory",
    "tomConstants_tomStoryActiveDisplay",
    "tomConstants_tomStoryActiveDisplayUI",
    "tomConstants_tomStoryActiveUI",
    "tomConstants_tomStoryInactive",
    "tomConstants_tomStretchBaseAbove",
    "tomConstants_tomStretchBaseBelow",
    "tomConstants_tomStretchCharAbove",
    "tomConstants_tomStretchCharBelow",
    "tomConstants_tomStrikeout",
    "tomConstants_tomStyleDefault",
    "tomConstants_tomStyleDisplay",
    "tomConstants_tomStyleDisplayCramped",
    "tomConstants_tomStyleScript",
    "tomConstants_tomStyleScriptCramped",
    "tomConstants_tomStyleScriptScript",
    "tomConstants_tomStyleScriptScriptCramped",
    "tomConstants_tomStyleText",
    "tomConstants_tomStyleTextCramped",
    "tomConstants_tomSubSupAlign",
    "tomConstants_tomSubscriptCF",
    "tomConstants_tomSuperscriptCF",
    "tomConstants_tomSuspend",
    "tomConstants_tomSylotiNagri",
    "tomConstants_tomSymbol",
    "tomConstants_tomSyriac",
    "tomConstants_tomTabBack",
    "tomConstants_tomTabHere",
    "tomConstants_tomTabNext",
    "tomConstants_tomTable",
    "tomConstants_tomTableColumn",
    "tomConstants_tomTaiLe",
    "tomConstants_tomTamil",
    "tomConstants_tomTelugu",
    "tomConstants_tomText",
    "tomConstants_tomTextFlowES",
    "tomConstants_tomTextFlowMask",
    "tomConstants_tomTextFlowNE",
    "tomConstants_tomTextFlowSW",
    "tomConstants_tomTextFlowWN",
    "tomConstants_tomTextFrameStory",
    "tomConstants_tomTextize",
    "tomConstants_tomThaana",
    "tomConstants_tomThai",
    "tomConstants_tomThick",
    "tomConstants_tomThickDash",
    "tomConstants_tomThickDashDot",
    "tomConstants_tomThickDashDotDot",
    "tomConstants_tomThickDotted",
    "tomConstants_tomThickLines",
    "tomConstants_tomThickLongDash",
    "tomConstants_tomTibetan",
    "tomConstants_tomTifinagh",
    "tomConstants_tomTitleCase",
    "tomConstants_tomToggle",
    "tomConstants_tomToggleCase",
    "tomConstants_tomTrackParms",
    "tomConstants_tomTransform",
    "tomConstants_tomTranslateTableCell",
    "tomConstants_tomTransparentForPositioning",
    "tomConstants_tomTransparentForSpacing",
    "tomConstants_tomTrue",
    "tomConstants_tomTruncateExisting",
    "tomConstants_tomTurkish",
    "tomConstants_tomUndefined",
    "tomConstants_tomUnderline",
    "tomConstants_tomUnderlinePositionAbove",
    "tomConstants_tomUnderlinePositionAuto",
    "tomConstants_tomUnderlinePositionBelow",
    "tomConstants_tomUnderlinePositionMax",
    "tomConstants_tomUndoLimit",
    "tomConstants_tomUnhide",
    "tomConstants_tomUnicodeBiDi",
    "tomConstants_tomUnknownStory",
    "tomConstants_tomUnlink",
    "tomConstants_tomUpperCase",
    "tomConstants_tomUpperLimitAsSuperScript",
    "tomConstants_tomUseAtFont",
    "tomConstants_tomUseCRLF",
    "tomConstants_tomUsePoints",
    "tomConstants_tomUseTwips",
    "tomConstants_tomUsymbol",
    "tomConstants_tomVLowCell",
    "tomConstants_tomVTopCell",
    "tomConstants_tomVai",
    "tomConstants_tomVietnamese",
    "tomConstants_tomWave",
    "tomConstants_tomWindow",
    "tomConstants_tomWipeDown",
    "tomConstants_tomWipeRight",
    "tomConstants_tomWord",
    "tomConstants_tomWordDocument",
    "tomConstants_tomWords",
    "tomConstants_tomYi",
    "yHeightCharPtsMost",
]
_arch_optional = [
]
