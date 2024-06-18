from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Direct2D
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.StructuredStorage
import win32more.Windows.Win32.System.Ole
import win32more.Windows.Win32.System.SystemServices
import win32more.Windows.Win32.System.Variant
import win32more.Windows.Win32.UI.Controls
import win32more.Windows.Win32.UI.Controls.RichEdit
import win32more.Windows.Win32.UI.Input.Ime
import win32more.Windows.Win32.UI.WindowsAndMessaging
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
EM_SETQUERYCONVERTOLELINKCALLBACK: UInt32 = 1427
EM_SETDISABLEOLELINKCONVERSION: UInt32 = 1428
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
RICHEDIT60_CLASS: String = 'RICHEDIT60W'
AURL_ENABLEEA: UInt32 = 1
GCM_TOUCHMENU: UInt32 = 16384
GCM_MOUSEMENU: UInt32 = 8192
S_MSG_KEY_IGNORED: win32more.Windows.Win32.Foundation.HRESULT = 262657
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
def AutoCorrectProc(langid: UInt16, pszBefore: win32more.Windows.Win32.Foundation.PWSTR, pszAfter: win32more.Windows.Win32.Foundation.PWSTR, cchAfter: Int32, pcchReplaced: POINTER(Int32)) -> Int32: ...
class BIDIOPTIONS(Structure):
    cbSize: UInt32
    wMask: UInt16
    wEffects: UInt16
CARET_FLAGS = Int32
CARET_NONE: win32more.Windows.Win32.UI.Controls.RichEdit.CARET_FLAGS = 0
CARET_CUSTOM: win32more.Windows.Win32.UI.Controls.RichEdit.CARET_FLAGS = 1
CARET_RTL: win32more.Windows.Win32.UI.Controls.RichEdit.CARET_FLAGS = 2
CARET_ITALIC: win32more.Windows.Win32.UI.Controls.RichEdit.CARET_FLAGS = 32
CARET_NULL: win32more.Windows.Win32.UI.Controls.RichEdit.CARET_FLAGS = 64
CARET_ROTATE90: win32more.Windows.Win32.UI.Controls.RichEdit.CARET_FLAGS = 128
class CARET_INFO(Union):
    hbitmap: win32more.Windows.Win32.Graphics.Gdi.HBITMAP
    caretFlags: win32more.Windows.Win32.UI.Controls.RichEdit.CARET_FLAGS
CFE_EFFECTS = UInt32
CFE_ALLCAPS: win32more.Windows.Win32.UI.Controls.RichEdit.CFE_EFFECTS = 128
CFE_AUTOBACKCOLOR: win32more.Windows.Win32.UI.Controls.RichEdit.CFE_EFFECTS = 67108864
CFE_DISABLED: win32more.Windows.Win32.UI.Controls.RichEdit.CFE_EFFECTS = 8192
CFE_EMBOSS: win32more.Windows.Win32.UI.Controls.RichEdit.CFE_EFFECTS = 2048
CFE_HIDDEN: win32more.Windows.Win32.UI.Controls.RichEdit.CFE_EFFECTS = 256
CFE_IMPRINT: win32more.Windows.Win32.UI.Controls.RichEdit.CFE_EFFECTS = 4096
CFE_OUTLINE: win32more.Windows.Win32.UI.Controls.RichEdit.CFE_EFFECTS = 512
CFE_REVISED: win32more.Windows.Win32.UI.Controls.RichEdit.CFE_EFFECTS = 16384
CFE_SHADOW: win32more.Windows.Win32.UI.Controls.RichEdit.CFE_EFFECTS = 1024
CFE_SMALLCAPS: win32more.Windows.Win32.UI.Controls.RichEdit.CFE_EFFECTS = 64
CFE_AUTOCOLOR: win32more.Windows.Win32.UI.Controls.RichEdit.CFE_EFFECTS = 1073741824
CFE_BOLD: win32more.Windows.Win32.UI.Controls.RichEdit.CFE_EFFECTS = 1
CFE_ITALIC: win32more.Windows.Win32.UI.Controls.RichEdit.CFE_EFFECTS = 2
CFE_STRIKEOUT: win32more.Windows.Win32.UI.Controls.RichEdit.CFE_EFFECTS = 8
CFE_UNDERLINE: win32more.Windows.Win32.UI.Controls.RichEdit.CFE_EFFECTS = 4
CFE_PROTECTED: win32more.Windows.Win32.UI.Controls.RichEdit.CFE_EFFECTS = 16
CFE_LINK: win32more.Windows.Win32.UI.Controls.RichEdit.CFE_EFFECTS = 32
CFE_SUBSCRIPT: win32more.Windows.Win32.UI.Controls.RichEdit.CFE_EFFECTS = 65536
CFE_SUPERSCRIPT: win32more.Windows.Win32.UI.Controls.RichEdit.CFE_EFFECTS = 131072
CFE_FONTBOUND: win32more.Windows.Win32.UI.Controls.RichEdit.CFE_EFFECTS = 1048576
CFE_LINKPROTECTED: win32more.Windows.Win32.UI.Controls.RichEdit.CFE_EFFECTS = 8388608
CFE_EXTENDED: win32more.Windows.Win32.UI.Controls.RichEdit.CFE_EFFECTS = 33554432
CFE_MATHNOBUILDUP: win32more.Windows.Win32.UI.Controls.RichEdit.CFE_EFFECTS = 134217728
CFE_MATH: win32more.Windows.Win32.UI.Controls.RichEdit.CFE_EFFECTS = 268435456
CFE_MATHORDINARY: win32more.Windows.Win32.UI.Controls.RichEdit.CFE_EFFECTS = 536870912
CFM_MASK = UInt32
CFM_SUBSCRIPT: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 196608
CFM_SUPERSCRIPT: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 196608
CFM_EFFECTS: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 1073741887
CFM_ALL: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 4160749631
CFM_BOLD: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 1
CFM_CHARSET: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 134217728
CFM_COLOR: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 1073741824
CFM_FACE: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 536870912
CFM_ITALIC: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 2
CFM_OFFSET: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 268435456
CFM_PROTECTED: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 16
CFM_SIZE: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 2147483648
CFM_STRIKEOUT: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 8
CFM_UNDERLINE: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 4
CFM_LINK: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 32
CFM_SMALLCAPS: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 64
CFM_ALLCAPS: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 128
CFM_HIDDEN: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 256
CFM_OUTLINE: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 512
CFM_SHADOW: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 1024
CFM_EMBOSS: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 2048
CFM_IMPRINT: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 4096
CFM_DISABLED: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 8192
CFM_REVISED: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 16384
CFM_REVAUTHOR: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 32768
CFM_ANIMATION: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 262144
CFM_STYLE: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 524288
CFM_KERNING: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 1048576
CFM_SPACING: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 2097152
CFM_WEIGHT: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 4194304
CFM_UNDERLINETYPE: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 8388608
CFM_COOKIE: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 16777216
CFM_LCID: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 33554432
CFM_BACKCOLOR: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 67108864
CFM_EFFECTS2: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 1141080063
CFM_ALL2: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 4294967295
CFM_FONTBOUND: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 1048576
CFM_LINKPROTECTED: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 8388608
CFM_EXTENDED: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 33554432
CFM_MATHNOBUILDUP: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 134217728
CFM_MATH: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 268435456
CFM_MATHORDINARY: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 536870912
CFM_ALLEFFECTS: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK = 2115207167
class CHANGENOTIFY(Structure):
    dwChangeType: UInt32
    pvCookieData: VoidPtr
CHANGETYPE = Int32
CN_GENERIC: win32more.Windows.Win32.UI.Controls.RichEdit.CHANGETYPE = 0
CN_TEXTCHANGED: win32more.Windows.Win32.UI.Controls.RichEdit.CHANGETYPE = 1
CN_NEWUNDO: win32more.Windows.Win32.UI.Controls.RichEdit.CHANGETYPE = 2
CN_NEWREDO: win32more.Windows.Win32.UI.Controls.RichEdit.CHANGETYPE = 4
class CHARFORMAT2A(Structure):
    Base: win32more.Windows.Win32.UI.Controls.RichEdit.CHARFORMATA
    wWeight: UInt16
    sSpacing: Int16
    crBackColor: win32more.Windows.Win32.Foundation.COLORREF
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
    Base: win32more.Windows.Win32.UI.Controls.RichEdit.CHARFORMATW
    wWeight: UInt16
    sSpacing: Int16
    crBackColor: win32more.Windows.Win32.Foundation.COLORREF
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
CHARFORMAT2 = UnicodeAlias('CHARFORMAT2W')
class CHARFORMATA(Structure):
    cbSize: UInt32
    dwMask: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK
    dwEffects: win32more.Windows.Win32.UI.Controls.RichEdit.CFE_EFFECTS
    yHeight: Int32
    yOffset: Int32
    crTextColor: win32more.Windows.Win32.Foundation.COLORREF
    bCharSet: win32more.Windows.Win32.Graphics.Gdi.FONT_CHARSET
    bPitchAndFamily: Byte
    szFaceName: win32more.Windows.Win32.Foundation.CHAR * 32
class CHARFORMATW(Structure):
    cbSize: UInt32
    dwMask: win32more.Windows.Win32.UI.Controls.RichEdit.CFM_MASK
    dwEffects: win32more.Windows.Win32.UI.Controls.RichEdit.CFE_EFFECTS
    yHeight: Int32
    yOffset: Int32
    crTextColor: win32more.Windows.Win32.Foundation.COLORREF
    bCharSet: win32more.Windows.Win32.Graphics.Gdi.FONT_CHARSET
    bPitchAndFamily: Byte
    szFaceName: Char * 32
CHARFORMAT = UnicodeAlias('CHARFORMATW')
class CHARRANGE(Structure):
    cpMin: Int32
    cpMax: Int32
if ARCH in 'X64,ARM64':
    class CLIPBOARDFORMAT(Structure):
        nmhdr: win32more.Windows.Win32.UI.Controls.NMHDR
        cf: UInt16
        _pack_ = 4
elif ARCH in 'X86':
    class CLIPBOARDFORMAT(Structure):
        nmhdr: win32more.Windows.Win32.UI.Controls.NMHDR
        cf: UInt16
class COMPCOLOR(Structure):
    crText: win32more.Windows.Win32.Foundation.COLORREF
    crBackground: win32more.Windows.Win32.Foundation.COLORREF
    dwEffects: UInt32
if ARCH in 'X64,ARM64':
    class EDITSTREAM(Structure):
        dwCookie: UIntPtr
        dwError: UInt32
        pfnCallback: win32more.Windows.Win32.UI.Controls.RichEdit.EDITSTREAMCALLBACK
        _pack_ = 4
elif ARCH in 'X86':
    class EDITSTREAM(Structure):
        dwCookie: UIntPtr
        dwError: UInt32
        pfnCallback: win32more.Windows.Win32.UI.Controls.RichEdit.EDITSTREAMCALLBACK
@winfunctype_pointer
def EDITSTREAMCALLBACK(dwCookie: UIntPtr, pbBuff: POINTER(Byte), cb: Int32, pcb: POINTER(Int32)) -> UInt32: ...
@winfunctype_pointer
def EDITWORDBREAKPROCEX(pchText: win32more.Windows.Win32.Foundation.PSTR, cchText: Int32, bCharSet: Byte, action: Int32) -> Int32: ...
if ARCH in 'X64,ARM64':
    class ENCORRECTTEXT(Structure):
        nmhdr: win32more.Windows.Win32.UI.Controls.NMHDR
        chrg: win32more.Windows.Win32.UI.Controls.RichEdit.CHARRANGE
        seltyp: win32more.Windows.Win32.UI.Controls.RichEdit.RICH_EDIT_GET_CONTEXT_MENU_SEL_TYPE
        _pack_ = 4
elif ARCH in 'X86':
    class ENCORRECTTEXT(Structure):
        nmhdr: win32more.Windows.Win32.UI.Controls.NMHDR
        chrg: win32more.Windows.Win32.UI.Controls.RichEdit.CHARRANGE
        seltyp: win32more.Windows.Win32.UI.Controls.RichEdit.RICH_EDIT_GET_CONTEXT_MENU_SEL_TYPE
if ARCH in 'X64,ARM64':
    class ENDCOMPOSITIONNOTIFY(Structure):
        nmhdr: win32more.Windows.Win32.UI.Controls.NMHDR
        dwCode: win32more.Windows.Win32.UI.Controls.RichEdit.ENDCOMPOSITIONNOTIFY_CODE
        _pack_ = 4
elif ARCH in 'X86':
    class ENDCOMPOSITIONNOTIFY(Structure):
        nmhdr: win32more.Windows.Win32.UI.Controls.NMHDR
        dwCode: win32more.Windows.Win32.UI.Controls.RichEdit.ENDCOMPOSITIONNOTIFY_CODE
ENDCOMPOSITIONNOTIFY_CODE = UInt32
ECN_ENDCOMPOSITION: win32more.Windows.Win32.UI.Controls.RichEdit.ENDCOMPOSITIONNOTIFY_CODE = 1
ECN_NEWTEXT: win32more.Windows.Win32.UI.Controls.RichEdit.ENDCOMPOSITIONNOTIFY_CODE = 2
if ARCH in 'X64,ARM64':
    class ENDROPFILES(Structure):
        nmhdr: win32more.Windows.Win32.UI.Controls.NMHDR
        hDrop: win32more.Windows.Win32.Foundation.HANDLE
        cp: Int32
        fProtected: win32more.Windows.Win32.Foundation.BOOL
        _pack_ = 4
elif ARCH in 'X86':
    class ENDROPFILES(Structure):
        nmhdr: win32more.Windows.Win32.UI.Controls.NMHDR
        hDrop: win32more.Windows.Win32.Foundation.HANDLE
        cp: Int32
        fProtected: win32more.Windows.Win32.Foundation.BOOL
if ARCH in 'X64,ARM64':
    class ENLINK(Structure):
        nmhdr: win32more.Windows.Win32.UI.Controls.NMHDR
        msg: UInt32
        wParam: win32more.Windows.Win32.Foundation.WPARAM
        lParam: win32more.Windows.Win32.Foundation.LPARAM
        chrg: win32more.Windows.Win32.UI.Controls.RichEdit.CHARRANGE
        _pack_ = 4
elif ARCH in 'X86':
    class ENLINK(Structure):
        nmhdr: win32more.Windows.Win32.UI.Controls.NMHDR
        msg: UInt32
        wParam: win32more.Windows.Win32.Foundation.WPARAM
        lParam: win32more.Windows.Win32.Foundation.LPARAM
        chrg: win32more.Windows.Win32.UI.Controls.RichEdit.CHARRANGE
if ARCH in 'X64,ARM64':
    class ENLOWFIRTF(Structure):
        nmhdr: win32more.Windows.Win32.UI.Controls.NMHDR
        szControl: win32more.Windows.Win32.Foundation.PSTR
        _pack_ = 4
elif ARCH in 'X86':
    class ENLOWFIRTF(Structure):
        nmhdr: win32more.Windows.Win32.UI.Controls.NMHDR
        szControl: win32more.Windows.Win32.Foundation.PSTR
if ARCH in 'X64,ARM64':
    class ENOLEOPFAILED(Structure):
        nmhdr: win32more.Windows.Win32.UI.Controls.NMHDR
        iob: Int32
        lOper: Int32
        hr: win32more.Windows.Win32.Foundation.HRESULT
        _pack_ = 4
elif ARCH in 'X86':
    class ENOLEOPFAILED(Structure):
        nmhdr: win32more.Windows.Win32.UI.Controls.NMHDR
        iob: Int32
        lOper: Int32
        hr: win32more.Windows.Win32.Foundation.HRESULT
if ARCH in 'X64,ARM64':
    class ENPROTECTED(Structure):
        nmhdr: win32more.Windows.Win32.UI.Controls.NMHDR
        msg: UInt32
        wParam: win32more.Windows.Win32.Foundation.WPARAM
        lParam: win32more.Windows.Win32.Foundation.LPARAM
        chrg: win32more.Windows.Win32.UI.Controls.RichEdit.CHARRANGE
        _pack_ = 4
elif ARCH in 'X86':
    class ENPROTECTED(Structure):
        nmhdr: win32more.Windows.Win32.UI.Controls.NMHDR
        msg: UInt32
        wParam: win32more.Windows.Win32.Foundation.WPARAM
        lParam: win32more.Windows.Win32.Foundation.LPARAM
        chrg: win32more.Windows.Win32.UI.Controls.RichEdit.CHARRANGE
if ARCH in 'X64,ARM64':
    class ENSAVECLIPBOARD(Structure):
        nmhdr: win32more.Windows.Win32.UI.Controls.NMHDR
        cObjectCount: Int32
        cch: Int32
        _pack_ = 4
elif ARCH in 'X86':
    class ENSAVECLIPBOARD(Structure):
        nmhdr: win32more.Windows.Win32.UI.Controls.NMHDR
        cObjectCount: Int32
        cch: Int32
if ARCH in 'X64,ARM64':
    class FINDTEXTA(Structure):
        chrg: win32more.Windows.Win32.UI.Controls.RichEdit.CHARRANGE
        lpstrText: win32more.Windows.Win32.Foundation.PSTR
        _pack_ = 4
elif ARCH in 'X86':
    class FINDTEXTA(Structure):
        chrg: win32more.Windows.Win32.UI.Controls.RichEdit.CHARRANGE
        lpstrText: win32more.Windows.Win32.Foundation.PSTR
if ARCH in 'X64,ARM64':
    class FINDTEXTEXA(Structure):
        chrg: win32more.Windows.Win32.UI.Controls.RichEdit.CHARRANGE
        lpstrText: win32more.Windows.Win32.Foundation.PSTR
        chrgText: win32more.Windows.Win32.UI.Controls.RichEdit.CHARRANGE
        _pack_ = 4
elif ARCH in 'X86':
    class FINDTEXTEXA(Structure):
        chrg: win32more.Windows.Win32.UI.Controls.RichEdit.CHARRANGE
        lpstrText: win32more.Windows.Win32.Foundation.PSTR
        chrgText: win32more.Windows.Win32.UI.Controls.RichEdit.CHARRANGE
if ARCH in 'X64,ARM64':
    class FINDTEXTEXW(Structure):
        chrg: win32more.Windows.Win32.UI.Controls.RichEdit.CHARRANGE
        lpstrText: win32more.Windows.Win32.Foundation.PWSTR
        chrgText: win32more.Windows.Win32.UI.Controls.RichEdit.CHARRANGE
        _pack_ = 4
elif ARCH in 'X86':
    class FINDTEXTEXW(Structure):
        chrg: win32more.Windows.Win32.UI.Controls.RichEdit.CHARRANGE
        lpstrText: win32more.Windows.Win32.Foundation.PWSTR
        chrgText: win32more.Windows.Win32.UI.Controls.RichEdit.CHARRANGE
if ARCH in 'X64,ARM64':
    FINDTEXTEX = UnicodeAlias('FINDTEXTEXW')
elif ARCH in 'X86':
    FINDTEXTEX = UnicodeAlias('FINDTEXTEXW')
if ARCH in 'X64,ARM64':
    class FINDTEXTW(Structure):
        chrg: win32more.Windows.Win32.UI.Controls.RichEdit.CHARRANGE
        lpstrText: win32more.Windows.Win32.Foundation.PWSTR
        _pack_ = 4
elif ARCH in 'X86':
    class FINDTEXTW(Structure):
        chrg: win32more.Windows.Win32.UI.Controls.RichEdit.CHARRANGE
        lpstrText: win32more.Windows.Win32.Foundation.PWSTR
if ARCH in 'X64,ARM64':
    FINDTEXT = UnicodeAlias('FINDTEXTW')
elif ARCH in 'X86':
    FINDTEXT = UnicodeAlias('FINDTEXTW')
if ARCH in 'X64,ARM64':
    class FORMATRANGE(Structure):
        hdc: win32more.Windows.Win32.Graphics.Gdi.HDC
        hdcTarget: win32more.Windows.Win32.Graphics.Gdi.HDC
        rc: win32more.Windows.Win32.Foundation.RECT
        rcPage: win32more.Windows.Win32.Foundation.RECT
        chrg: win32more.Windows.Win32.UI.Controls.RichEdit.CHARRANGE
        _pack_ = 4
elif ARCH in 'X86':
    class FORMATRANGE(Structure):
        hdc: win32more.Windows.Win32.Graphics.Gdi.HDC
        hdcTarget: win32more.Windows.Win32.Graphics.Gdi.HDC
        rc: win32more.Windows.Win32.Foundation.RECT
        rcPage: win32more.Windows.Win32.Foundation.RECT
        chrg: win32more.Windows.Win32.UI.Controls.RichEdit.CHARRANGE
if ARCH in 'X64,ARM64':
    class GETCONTEXTMENUEX(Structure):
        chrg: win32more.Windows.Win32.UI.Controls.RichEdit.CHARRANGE
        dwFlags: UInt32
        pt: win32more.Windows.Win32.Foundation.POINT
        pvReserved: VoidPtr
        _pack_ = 4
elif ARCH in 'X86':
    class GETCONTEXTMENUEX(Structure):
        chrg: win32more.Windows.Win32.UI.Controls.RichEdit.CHARRANGE
        dwFlags: UInt32
        pt: win32more.Windows.Win32.Foundation.POINT
        pvReserved: VoidPtr
if ARCH in 'X64,ARM64':
    class GETTEXTEX(Structure):
        cb: UInt32
        flags: win32more.Windows.Win32.UI.Controls.RichEdit.GETTEXTEX_FLAGS
        codepage: UInt32
        lpDefaultChar: win32more.Windows.Win32.Foundation.PSTR
        lpUsedDefChar: POINTER(win32more.Windows.Win32.Foundation.BOOL)
        _pack_ = 4
elif ARCH in 'X86':
    class GETTEXTEX(Structure):
        cb: UInt32
        flags: win32more.Windows.Win32.UI.Controls.RichEdit.GETTEXTEX_FLAGS
        codepage: UInt32
        lpDefaultChar: win32more.Windows.Win32.Foundation.PSTR
        lpUsedDefChar: POINTER(win32more.Windows.Win32.Foundation.BOOL)
GETTEXTEX_FLAGS = UInt32
GT_DEFAULT: win32more.Windows.Win32.UI.Controls.RichEdit.GETTEXTEX_FLAGS = 0
GT_NOHIDDENTEXT: win32more.Windows.Win32.UI.Controls.RichEdit.GETTEXTEX_FLAGS = 8
GT_RAWTEXT: win32more.Windows.Win32.UI.Controls.RichEdit.GETTEXTEX_FLAGS = 4
GT_SELECTION: win32more.Windows.Win32.UI.Controls.RichEdit.GETTEXTEX_FLAGS = 2
GT_USECRLF: win32more.Windows.Win32.UI.Controls.RichEdit.GETTEXTEX_FLAGS = 1
class GETTEXTLENGTHEX(Structure):
    flags: win32more.Windows.Win32.UI.Controls.RichEdit.GETTEXTLENGTHEX_FLAGS
    codepage: UInt32
GETTEXTLENGTHEX_FLAGS = UInt32
GTL_DEFAULT: win32more.Windows.Win32.UI.Controls.RichEdit.GETTEXTLENGTHEX_FLAGS = 0
GTL_USECRLF: win32more.Windows.Win32.UI.Controls.RichEdit.GETTEXTLENGTHEX_FLAGS = 1
GTL_PRECISE: win32more.Windows.Win32.UI.Controls.RichEdit.GETTEXTLENGTHEX_FLAGS = 2
GTL_CLOSE: win32more.Windows.Win32.UI.Controls.RichEdit.GETTEXTLENGTHEX_FLAGS = 4
GTL_NUMCHARS: win32more.Windows.Win32.UI.Controls.RichEdit.GETTEXTLENGTHEX_FLAGS = 8
GTL_NUMBYTES: win32more.Windows.Win32.UI.Controls.RichEdit.GETTEXTLENGTHEX_FLAGS = 16
class GROUPTYPINGCHANGE(Structure):
    nmhdr: win32more.Windows.Win32.UI.Controls.NMHDR
    fGroupTyping: win32more.Windows.Win32.Foundation.BOOL
    _pack_ = 4
if ARCH in 'X64,ARM64':
    class HYPHENATEINFO(Structure):
        cbSize: Int16
        dxHyphenateZone: Int16
        pfnHyphenate: IntPtr
        _pack_ = 4
elif ARCH in 'X86':
    class HYPHENATEINFO(Structure):
        cbSize: Int16
        dxHyphenateZone: Int16
        pfnHyphenate: IntPtr
class HYPHRESULT(Structure):
    khyph: win32more.Windows.Win32.UI.Controls.RichEdit.KHYPH
    ichHyph: Int32
    chHyph: Char
class IMECOMPTEXT(Structure):
    cb: Int32
    flags: win32more.Windows.Win32.UI.Controls.RichEdit.IMECOMPTEXT_FLAGS
IMECOMPTEXT_FLAGS = UInt32
ICT_RESULTREADSTR: win32more.Windows.Win32.UI.Controls.RichEdit.IMECOMPTEXT_FLAGS = 1
class IRichEditOle(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00020d00-0000-0000-c000-000000000046}')
    @commethod(3)
    def GetClientSite(self, lplpolesite: POINTER(win32more.Windows.Win32.System.Ole.IOleClientSite)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetObjectCount(self) -> Int32: ...
    @commethod(5)
    def GetLinkCount(self) -> Int32: ...
    @commethod(6)
    def GetObject(self, iob: Int32, lpreobject: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.REOBJECT), dwFlags: win32more.Windows.Win32.UI.Controls.RichEdit.RICH_EDIT_GET_OBJECT_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def InsertObject(self, lpreobject: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.REOBJECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ConvertObject(self, iob: Int32, rclsidNew: POINTER(Guid), lpstrUserTypeNew: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ActivateAs(self, rclsid: POINTER(Guid), rclsidAs: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetHostNames(self, lpstrContainerApp: win32more.Windows.Win32.Foundation.PSTR, lpstrContainerObj: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetLinkAvailable(self, iob: Int32, fAvailable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetDvaspect(self, iob: Int32, dvaspect: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def HandsOffStorage(self, iob: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SaveCompleted(self, iob: Int32, lpstg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def InPlaceDeactivate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def ContextSensitiveHelp(self, fEnterMode: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetClipboardData(self, lpchrg: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.CHARRANGE), reco: UInt32, lplpdataobj: POINTER(win32more.Windows.Win32.System.Com.IDataObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def ImportDataObject(self, lpdataobj: win32more.Windows.Win32.System.Com.IDataObject, cf: UInt16, hMetaPict: win32more.Windows.Win32.Foundation.HGLOBAL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRichEditOleCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00020d03-0000-0000-c000-000000000046}')
    @commethod(3)
    def GetNewStorage(self, lplpstg: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInPlaceContext(self, lplpFrame: POINTER(win32more.Windows.Win32.System.Ole.IOleInPlaceFrame), lplpDoc: POINTER(win32more.Windows.Win32.System.Ole.IOleInPlaceUIWindow), lpFrameInfo: POINTER(win32more.Windows.Win32.System.Ole.OLEINPLACEFRAMEINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ShowContainerUI(self, fShow: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def QueryInsertObject(self, lpclsid: POINTER(Guid), lpstg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, cp: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DeleteObject(self, lpoleobj: win32more.Windows.Win32.System.Ole.IOleObject) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def QueryAcceptData(self, lpdataobj: win32more.Windows.Win32.System.Com.IDataObject, lpcfFormat: POINTER(UInt16), reco: win32more.Windows.Win32.System.SystemServices.RECO_FLAGS, fReally: win32more.Windows.Win32.Foundation.BOOL, hMetaPict: win32more.Windows.Win32.Foundation.HGLOBAL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ContextSensitiveHelp(self, fEnterMode: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetClipboardData(self, lpchrg: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.CHARRANGE), reco: UInt32, lplpdataobj: POINTER(win32more.Windows.Win32.System.Com.IDataObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetDragDropEffect(self, fDrag: win32more.Windows.Win32.Foundation.BOOL, grfKeyState: win32more.Windows.Win32.System.SystemServices.MODIFIERKEYS_FLAGS, pdwEffect: POINTER(win32more.Windows.Win32.System.Ole.DROPEFFECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetContextMenu(self, seltype: win32more.Windows.Win32.UI.Controls.RichEdit.RICH_EDIT_GET_CONTEXT_MENU_SEL_TYPE, lpoleobj: win32more.Windows.Win32.System.Ole.IOleObject, lpchrg: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.CHARRANGE), lphmenu: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRicheditUiaOverrides(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def GetPropertyOverrideValue(self, propertyId: Int32, pRetValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextDisplays(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c241f5f2-7206-11d8-a2c7-00a0d1d6c6b3}')
class ITextDocument(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{8cc497c0-a1df-11ce-8098-00aa0047be5d}')
    @commethod(7)
    def GetName(self, pName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSelection(self, ppSel: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextSelection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetStoryCount(self, pCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetStoryRanges(self, ppStories: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextStoryRanges)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetSaved(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetSaved(self, Value: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetDefaultTabStop(self, pValue: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetDefaultTabStop(self, Value: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def New(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Open(self, pVar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), Flags: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants, CodePage: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Save(self, pVar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), Flags: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants, CodePage: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def Freeze(self, pCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Unfreeze(self, pCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def BeginEditCollection(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def EndEditCollection(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def Undo(self, Count: Int32, pCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Redo(self, Count: Int32, pCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def Range(self, cpActive: Int32, cpAnchor: Int32, ppRange: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextRange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def RangeFromPoint(self, x: Int32, y: Int32, ppRange: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextRange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextDocument2(ComPtr):
    extends: win32more.Windows.Win32.UI.Controls.RichEdit.ITextDocument
    _iid_ = Guid('{c241f5e0-7206-11d8-a2c7-00a0d1d6c6b3}')
    @commethod(26)
    def GetCaretType(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetCaretType(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetDisplays(self, ppDisplays: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextDisplays)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetDocumentFont(self, ppFont: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextFont2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def SetDocumentFont(self, pFont: win32more.Windows.Win32.UI.Controls.RichEdit.ITextFont2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetDocumentPara(self, ppPara: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextPara2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def SetDocumentPara(self, pPara: win32more.Windows.Win32.UI.Controls.RichEdit.ITextPara2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetEastAsianFlags(self, pFlags: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetGenerator(self, pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def SetIMEInProgress(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def GetNotificationMode(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def SetNotificationMode(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def GetSelection2(self, ppSel: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextSelection2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def GetStoryRanges2(self, ppStories: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextStoryRanges2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def GetTypographyOptions(self, pOptions: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def GetVersion(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def GetWindow(self, pHwnd: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def AttachMsgFilter(self, pFilter: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def CheckTextLimit(self, cch: Int32, pcch: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def GetCallManager(self, ppVoid: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def GetClientRect(self, Type: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants, pLeft: POINTER(Int32), pTop: POINTER(Int32), pRight: POINTER(Int32), pBottom: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def GetEffectColor(self, Index: Int32, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def GetImmContext(self, pContext: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def GetPreferredFont(self, cp: Int32, CharRep: Int32, Options: Int32, curCharRep: Int32, curFontSize: Int32, pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR), pPitchAndFamily: POINTER(Int32), pNewFontSize: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def GetProperty(self, Type: Int32, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def GetStrings(self, ppStrs: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextStrings)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def Notify(self, Notify: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def Range2(self, cpActive: Int32, cpAnchor: Int32, ppRange: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextRange2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def RangeFromPoint2(self, x: Int32, y: Int32, Type: Int32, ppRange: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextRange2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def ReleaseCallManager(self, pVoid: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def ReleaseImmContext(self, Context: Int64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def SetEffectColor(self, Index: Int32, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def SetProperty(self, Type: Int32, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def SetTypographyOptions(self, Options: Int32, Mask: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def SysBeep(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def Update(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def UpdateWindow(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def GetMathProperties(self, pOptions: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def SetMathProperties(self, Options: Int32, Mask: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def GetActiveStory(self, ppStory: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextStory)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def SetActiveStory(self, pStory: win32more.Windows.Win32.UI.Controls.RichEdit.ITextStory) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(67)
    def GetMainStory(self, ppStory: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextStory)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(68)
    def GetNewStory(self, ppStory: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextStory)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def GetStory(self, Index: Int32, ppStory: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextStory)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextDocument2Old(ComPtr):
    extends: win32more.Windows.Win32.UI.Controls.RichEdit.ITextDocument
    _iid_ = Guid('{01c25500-4268-11d1-883a-3c8b00c10000}')
    @commethod(26)
    def AttachMsgFilter(self, pFilter: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetEffectColor(self, Index: Int32, cr: win32more.Windows.Win32.Foundation.COLORREF) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetEffectColor(self, Index: Int32, pcr: POINTER(win32more.Windows.Win32.Foundation.COLORREF)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetCaretType(self, pCaretType: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def SetCaretType(self, CaretType: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetImmContext(self, pContext: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def ReleaseImmContext(self, Context: Int64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetPreferredFont(self, cp: Int32, CharRep: Int32, Option: Int32, CharRepCur: Int32, curFontSize: Int32, pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR), pPitchAndFamily: POINTER(Int32), pNewFontSize: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetNotificationMode(self, pMode: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def SetNotificationMode(self, Mode: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def GetClientRect(self, Type: Int32, pLeft: POINTER(Int32), pTop: POINTER(Int32), pRight: POINTER(Int32), pBottom: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def GetSelection2(self, ppSel: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextSelection)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def GetWindow(self, phWnd: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def GetFEFlags(self, pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def UpdateWindow(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def CheckTextLimit(self, cch: Int32, pcch: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def IMEInProgress(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def SysBeep(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def Update(self, Mode: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def Notify(self, Notify: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def GetDocumentFont(self, ppITextFont: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextFont)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def GetDocumentPara(self, ppITextPara: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextPara)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def GetCallManager(self, ppVoid: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def ReleaseCallManager(self, pVoid: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextFont(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{8cc497c3-a1df-11ce-8098-00aa0047be5d}')
    @commethod(7)
    def GetDuplicate(self, ppFont: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextFont)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetDuplicate(self, pFont: win32more.Windows.Win32.UI.Controls.RichEdit.ITextFont) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CanChange(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IsEqual(self, pFont: win32more.Windows.Win32.UI.Controls.RichEdit.ITextFont, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Reset(self, Value: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetStyle(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetStyle(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetAllCaps(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetAllCaps(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetAnimation(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetAnimation(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetBackColor(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetBackColor(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetBold(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetBold(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetEmboss(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetEmboss(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetForeColor(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetForeColor(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetHidden(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetHidden(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetEngrave(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetEngrave(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetItalic(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def SetItalic(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetKerning(self, pValue: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def SetKerning(self, Value: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetLanguageID(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def SetLanguageID(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def GetName(self, pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def SetName(self, bstr: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def GetOutline(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def SetOutline(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def GetPosition(self, pValue: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def SetPosition(self, Value: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def GetProtected(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def SetProtected(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def GetShadow(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def SetShadow(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def GetSize(self, pValue: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def SetSize(self, Value: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def GetSmallCaps(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def SetSmallCaps(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def GetSpacing(self, pValue: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def SetSpacing(self, Value: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def GetStrikeThrough(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def SetStrikeThrough(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def GetSubscript(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def SetSubscript(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def GetSuperscript(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def SetSuperscript(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def GetUnderline(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def SetUnderline(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def GetWeight(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def SetWeight(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextFont2(ComPtr):
    extends: win32more.Windows.Win32.UI.Controls.RichEdit.ITextFont
    _iid_ = Guid('{c241f5e3-7206-11d8-a2c7-00a0d1d6c6b3}')
    @commethod(62)
    def GetCount(self, pCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def GetAutoLigatures(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def SetAutoLigatures(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def GetAutospaceAlpha(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def SetAutospaceAlpha(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(67)
    def GetAutospaceNumeric(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(68)
    def SetAutospaceNumeric(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def GetAutospaceParens(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(70)
    def SetAutospaceParens(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(71)
    def GetCharRep(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(72)
    def SetCharRep(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(73)
    def GetCompressionMode(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(74)
    def SetCompressionMode(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(75)
    def GetCookie(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(76)
    def SetCookie(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(77)
    def GetDoubleStrike(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(78)
    def SetDoubleStrike(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(79)
    def GetDuplicate2(self, ppFont: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextFont2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(80)
    def SetDuplicate2(self, pFont: win32more.Windows.Win32.UI.Controls.RichEdit.ITextFont2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(81)
    def GetLinkType(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(82)
    def GetMathZone(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(83)
    def SetMathZone(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(84)
    def GetModWidthPairs(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(85)
    def SetModWidthPairs(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(86)
    def GetModWidthSpace(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(87)
    def SetModWidthSpace(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(88)
    def GetOldNumbers(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(89)
    def SetOldNumbers(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(90)
    def GetOverlapping(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(91)
    def SetOverlapping(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(92)
    def GetPositionSubSuper(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(93)
    def SetPositionSubSuper(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(94)
    def GetScaling(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(95)
    def SetScaling(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(96)
    def GetSpaceExtension(self, pValue: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(97)
    def SetSpaceExtension(self, Value: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(98)
    def GetUnderlinePositionMode(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(99)
    def SetUnderlinePositionMode(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(100)
    def GetEffects(self, pValue: POINTER(Int32), pMask: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(101)
    def GetEffects2(self, pValue: POINTER(Int32), pMask: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(102)
    def GetProperty(self, Type: Int32, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(103)
    def GetPropertyInfo(self, Index: Int32, pType: POINTER(Int32), pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(104)
    def IsEqual2(self, pFont: win32more.Windows.Win32.UI.Controls.RichEdit.ITextFont2, pB: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(105)
    def SetEffects(self, Value: Int32, Mask: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(106)
    def SetEffects2(self, Value: Int32, Mask: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(107)
    def SetProperty(self, Type: Int32, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextHost(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def TxGetDC(self) -> win32more.Windows.Win32.Graphics.Gdi.HDC: ...
    @commethod(4)
    def TxReleaseDC(self, hdc: win32more.Windows.Win32.Graphics.Gdi.HDC) -> Int32: ...
    @commethod(5)
    def TxShowScrollBar(self, fnBar: Int32, fShow: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(6)
    def TxEnableScrollBar(self, fuSBFlags: win32more.Windows.Win32.UI.WindowsAndMessaging.SCROLLBAR_CONSTANTS, fuArrowflags: Int32) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(7)
    def TxSetScrollRange(self, fnBar: Int32, nMinPos: Int32, nMaxPos: Int32, fRedraw: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(8)
    def TxSetScrollPos(self, fnBar: Int32, nPos: Int32, fRedraw: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(9)
    def TxInvalidateRect(self, prc: POINTER(win32more.Windows.Win32.Foundation.RECT), fMode: win32more.Windows.Win32.Foundation.BOOL) -> Void: ...
    @commethod(10)
    def TxViewChange(self, fUpdate: win32more.Windows.Win32.Foundation.BOOL) -> Void: ...
    @commethod(11)
    def TxCreateCaret(self, hbmp: win32more.Windows.Win32.Graphics.Gdi.HBITMAP, xWidth: Int32, yHeight: Int32) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(12)
    def TxShowCaret(self, fShow: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(13)
    def TxSetCaretPos(self, x: Int32, y: Int32) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(14)
    def TxSetTimer(self, idTimer: UInt32, uTimeout: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(15)
    def TxKillTimer(self, idTimer: UInt32) -> Void: ...
    @commethod(16)
    def TxScrollWindowEx(self, dx: Int32, dy: Int32, lprcScroll: POINTER(win32more.Windows.Win32.Foundation.RECT), lprcClip: POINTER(win32more.Windows.Win32.Foundation.RECT), hrgnUpdate: win32more.Windows.Win32.Graphics.Gdi.HRGN, lprcUpdate: POINTER(win32more.Windows.Win32.Foundation.RECT), fuScroll: win32more.Windows.Win32.UI.WindowsAndMessaging.SCROLL_WINDOW_FLAGS) -> Void: ...
    @commethod(17)
    def TxSetCapture(self, fCapture: win32more.Windows.Win32.Foundation.BOOL) -> Void: ...
    @commethod(18)
    def TxSetFocus(self) -> Void: ...
    @commethod(19)
    def TxSetCursor(self, hcur: win32more.Windows.Win32.UI.WindowsAndMessaging.HCURSOR, fText: win32more.Windows.Win32.Foundation.BOOL) -> Void: ...
    @commethod(20)
    def TxScreenToClient(self, lppt: POINTER(win32more.Windows.Win32.Foundation.POINT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(21)
    def TxClientToScreen(self, lppt: POINTER(win32more.Windows.Win32.Foundation.POINT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(22)
    def TxActivate(self, plOldState: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def TxDeactivate(self, lNewState: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def TxGetClientRect(self, prc: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def TxGetViewInset(self, prc: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def TxGetCharFormat(self, ppCF: POINTER(POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.CHARFORMATW))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def TxGetParaFormat(self, ppPF: POINTER(POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def TxGetSysColor(self, nIndex: win32more.Windows.Win32.Graphics.Gdi.SYS_COLOR_INDEX) -> win32more.Windows.Win32.Foundation.COLORREF: ...
    @commethod(29)
    def TxGetBackStyle(self, pstyle: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.TXTBACKSTYLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def TxGetMaxLength(self, plength: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def TxGetScrollBars(self, pdwScrollBar: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def TxGetPasswordChar(self, pch: POINTER(SByte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def TxGetAcceleratorPos(self, pcp: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def TxGetExtent(self, lpExtent: POINTER(win32more.Windows.Win32.Foundation.SIZE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def OnTxCharFormatChange(self, pCF: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.CHARFORMATW)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def OnTxParaFormatChange(self, pPF: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def TxGetPropertyBits(self, dwMask: UInt32, pdwBits: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def TxNotify(self, iNotify: UInt32, pv: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def TxImmGetContext(self) -> win32more.Windows.Win32.UI.Input.Ime.HIMC: ...
    @commethod(40)
    def TxImmReleaseContext(self, himc: win32more.Windows.Win32.UI.Input.Ime.HIMC) -> Void: ...
    @commethod(41)
    def TxGetSelectionBarWidth(self, lSelBarWidth: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextHost2(ComPtr):
    extends: win32more.Windows.Win32.UI.Controls.RichEdit.ITextHost
    @commethod(42)
    def TxIsDoubleClickPending(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(43)
    def TxGetWindow(self, phwnd: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def TxSetForegroundWindow(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def TxGetPalette(self) -> win32more.Windows.Win32.Graphics.Gdi.HPALETTE: ...
    @commethod(46)
    def TxGetEastAsianFlags(self, pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def TxSetCursor2(self, hcur: win32more.Windows.Win32.UI.WindowsAndMessaging.HCURSOR, bText: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.UI.WindowsAndMessaging.HCURSOR: ...
    @commethod(48)
    def TxFreeTextServicesNotification(self) -> Void: ...
    @commethod(49)
    def TxGetEditStyle(self, dwItem: UInt32, pdwData: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def TxGetWindowStyles(self, pdwStyle: POINTER(UInt32), pdwExStyle: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def TxShowDropCaret(self, fShow: win32more.Windows.Win32.Foundation.BOOL, hdc: win32more.Windows.Win32.Graphics.Gdi.HDC, prc: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def TxDestroyCaret(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def TxGetHorzExtent(self, plHorzExtent: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextPara(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{8cc497c4-a1df-11ce-8098-00aa0047be5d}')
    @commethod(7)
    def GetDuplicate(self, ppPara: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextPara)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetDuplicate(self, pPara: win32more.Windows.Win32.UI.Controls.RichEdit.ITextPara) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CanChange(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IsEqual(self, pPara: win32more.Windows.Win32.UI.Controls.RichEdit.ITextPara, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Reset(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetStyle(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetStyle(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetAlignment(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetAlignment(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetHyphenation(self, pValue: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetHyphenation(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetFirstLineIndent(self, pValue: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetKeepTogether(self, pValue: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetKeepTogether(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetKeepWithNext(self, pValue: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetKeepWithNext(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetLeftIndent(self, pValue: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetLineSpacing(self, pValue: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetLineSpacingRule(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetListAlignment(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetListAlignment(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetListLevelIndex(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetListLevelIndex(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetListStart(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def SetListStart(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetListTab(self, pValue: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def SetListTab(self, Value: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetListType(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def SetListType(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def GetNoLineNumber(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def SetNoLineNumber(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def GetPageBreakBefore(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def SetPageBreakBefore(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def GetRightIndent(self, pValue: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def SetRightIndent(self, Value: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def SetIndents(self, First: Single, Left: Single, Right: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def SetLineSpacing(self, Rule: Int32, Spacing: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def GetSpaceAfter(self, pValue: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def SetSpaceAfter(self, Value: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def GetSpaceBefore(self, pValue: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def SetSpaceBefore(self, Value: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def GetWidowControl(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def SetWidowControl(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def GetTabCount(self, pCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def AddTab(self, tbPos: Single, tbAlign: Int32, tbLeader: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def ClearAllTabs(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def DeleteTab(self, tbPos: Single) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def GetTab(self, iTab: Int32, ptbPos: POINTER(Single), ptbAlign: POINTER(Int32), ptbLeader: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextPara2(ComPtr):
    extends: win32more.Windows.Win32.UI.Controls.RichEdit.ITextPara
    _iid_ = Guid('{c241f5e4-7206-11d8-a2c7-00a0d1d6c6b3}')
    @commethod(55)
    def GetBorders(self, ppBorders: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def GetDuplicate2(self, ppPara: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextPara2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def SetDuplicate2(self, pPara: win32more.Windows.Win32.UI.Controls.RichEdit.ITextPara2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def GetFontAlignment(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def SetFontAlignment(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def GetHangingPunctuation(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def SetHangingPunctuation(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def GetSnapToGrid(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def SetSnapToGrid(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def GetTrimPunctuationAtStart(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def SetTrimPunctuationAtStart(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def GetEffects(self, pValue: POINTER(Int32), pMask: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(67)
    def GetProperty(self, Type: Int32, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(68)
    def IsEqual2(self, pPara: win32more.Windows.Win32.UI.Controls.RichEdit.ITextPara2, pB: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def SetEffects(self, Value: Int32, Mask: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(70)
    def SetProperty(self, Type: Int32, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextRange(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{8cc497c2-a1df-11ce-8098-00aa0047be5d}')
    @commethod(7)
    def GetText(self, pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetText(self, bstr: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetChar(self, pChar: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetChar(self, Char: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetDuplicate(self, ppRange: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextRange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetFormattedText(self, ppRange: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextRange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetFormattedText(self, pRange: win32more.Windows.Win32.UI.Controls.RichEdit.ITextRange) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetStart(self, pcpFirst: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetStart(self, cpFirst: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetEnd(self, pcpLim: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetEnd(self, cpLim: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetFont(self, ppFont: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextFont)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetFont(self, pFont: win32more.Windows.Win32.UI.Controls.RichEdit.ITextFont) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetPara(self, ppPara: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextPara)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetPara(self, pPara: win32more.Windows.Win32.UI.Controls.RichEdit.ITextPara) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetStoryLength(self, pCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetStoryType(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def Collapse(self, bStart: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def Expand(self, Unit: Int32, pDelta: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetIndex(self, Unit: Int32, pIndex: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetIndex(self, Unit: Int32, Index: Int32, Extend: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def SetRange(self, cpAnchor: Int32, cpActive: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def InRange(self, pRange: win32more.Windows.Win32.UI.Controls.RichEdit.ITextRange, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def InStory(self, pRange: win32more.Windows.Win32.UI.Controls.RichEdit.ITextRange, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def IsEqual(self, pRange: win32more.Windows.Win32.UI.Controls.RichEdit.ITextRange, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def Select(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def StartOf(self, Unit: Int32, Extend: Int32, pDelta: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def EndOf(self, Unit: Int32, Extend: Int32, pDelta: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def Move(self, Unit: Int32, Count: Int32, pDelta: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def MoveStart(self, Unit: Int32, Count: Int32, pDelta: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def MoveEnd(self, Unit: Int32, Count: Int32, pDelta: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def MoveWhile(self, Cset: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), Count: Int32, pDelta: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def MoveStartWhile(self, Cset: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), Count: Int32, pDelta: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def MoveEndWhile(self, Cset: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), Count: Int32, pDelta: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def MoveUntil(self, Cset: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), Count: Int32, pDelta: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def MoveStartUntil(self, Cset: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), Count: Int32, pDelta: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def MoveEndUntil(self, Cset: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), Count: Int32, pDelta: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def FindText(self, bstr: win32more.Windows.Win32.Foundation.BSTR, Count: Int32, Flags: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants, pLength: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def FindTextStart(self, bstr: win32more.Windows.Win32.Foundation.BSTR, Count: Int32, Flags: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants, pLength: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def FindTextEnd(self, bstr: win32more.Windows.Win32.Foundation.BSTR, Count: Int32, Flags: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants, pLength: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def Delete(self, Unit: Int32, Count: Int32, pDelta: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def Cut(self, pVar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def Copy(self, pVar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def Paste(self, pVar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), Format: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def CanPaste(self, pVar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), Format: Int32, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def CanEdit(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def ChangeCase(self, Type: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def GetPoint(self, Type: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants, px: POINTER(Int32), py: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def SetPoint(self, x: Int32, y: Int32, Type: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants, Extend: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def ScrollIntoView(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def GetEmbeddedObject(self, ppObject: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextRange2(ComPtr):
    extends: win32more.Windows.Win32.UI.Controls.RichEdit.ITextSelection
    _iid_ = Guid('{c241f5e2-7206-11d8-a2c7-00a0d1d6c6b3}')
    @commethod(68)
    def GetCch(self, pcch: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def GetCells(self, ppCells: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(70)
    def GetColumn(self, ppColumn: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(71)
    def GetCount(self, pCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(72)
    def GetDuplicate2(self, ppRange: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextRange2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(73)
    def GetFont2(self, ppFont: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextFont2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(74)
    def SetFont2(self, pFont: win32more.Windows.Win32.UI.Controls.RichEdit.ITextFont2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(75)
    def GetFormattedText2(self, ppRange: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextRange2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(76)
    def SetFormattedText2(self, pRange: win32more.Windows.Win32.UI.Controls.RichEdit.ITextRange2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(77)
    def GetGravity(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(78)
    def SetGravity(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(79)
    def GetPara2(self, ppPara: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextPara2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(80)
    def SetPara2(self, pPara: win32more.Windows.Win32.UI.Controls.RichEdit.ITextPara2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(81)
    def GetRow(self, ppRow: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextRow)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(82)
    def GetStartPara(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(83)
    def GetTable(self, ppTable: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(84)
    def GetURL(self, pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(85)
    def SetURL(self, bstr: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(86)
    def AddSubrange(self, cp1: Int32, cp2: Int32, Activate: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(87)
    def BuildUpMath(self, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(88)
    def DeleteSubrange(self, cpFirst: Int32, cpLim: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(89)
    def Find(self, pRange: win32more.Windows.Win32.UI.Controls.RichEdit.ITextRange2, Count: Int32, Flags: Int32, pDelta: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(90)
    def GetChar2(self, pChar: POINTER(Int32), Offset: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(91)
    def GetDropCap(self, pcLine: POINTER(Int32), pPosition: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(92)
    def GetInlineObject(self, pType: POINTER(Int32), pAlign: POINTER(Int32), pChar: POINTER(Int32), pChar1: POINTER(Int32), pChar2: POINTER(Int32), pCount: POINTER(Int32), pTeXStyle: POINTER(Int32), pcCol: POINTER(Int32), pLevel: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(93)
    def GetProperty(self, Type: Int32, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(94)
    def GetRect(self, Type: Int32, pLeft: POINTER(Int32), pTop: POINTER(Int32), pRight: POINTER(Int32), pBottom: POINTER(Int32), pHit: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(95)
    def GetSubrange(self, iSubrange: Int32, pcpFirst: POINTER(Int32), pcpLim: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(96)
    def GetText2(self, Flags: Int32, pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(97)
    def HexToUnicode(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(98)
    def InsertTable(self, cCol: Int32, cRow: Int32, AutoFit: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(99)
    def Linearize(self, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(100)
    def SetActiveSubrange(self, cpAnchor: Int32, cpActive: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(101)
    def SetDropCap(self, cLine: Int32, Position: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(102)
    def SetProperty(self, Type: Int32, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(103)
    def SetText2(self, Flags: Int32, bstr: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(104)
    def UnicodeToHex(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(105)
    def SetInlineObject(self, Type: Int32, Align: Int32, Char: Int32, Char1: Int32, Char2: Int32, Count: Int32, TeXStyle: Int32, cCol: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(106)
    def GetMathFunctionType(self, bstr: win32more.Windows.Win32.Foundation.BSTR, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(107)
    def InsertImage(self, width: Int32, height: Int32, ascent: Int32, Type: Int32, bstrAltText: win32more.Windows.Win32.Foundation.BSTR, pStream: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextRow(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c241f5ef-7206-11d8-a2c7-00a0d1d6c6b3}')
    @commethod(7)
    def GetAlignment(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetAlignment(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCellCount(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetCellCount(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetCellCountCache(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetCellCountCache(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetCellIndex(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetCellIndex(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetCellMargin(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetCellMargin(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetHeight(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetHeight(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetIndent(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetIndent(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetKeepTogether(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetKeepTogether(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetKeepWithNext(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetKeepWithNext(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetNestLevel(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetRTL(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetRTL(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetCellAlignment(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetCellAlignment(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetCellColorBack(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def SetCellColorBack(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetCellColorFore(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def SetCellColorFore(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetCellMergeFlags(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def SetCellMergeFlags(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def GetCellShading(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def SetCellShading(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def GetCellVerticalText(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def SetCellVerticalText(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def GetCellWidth(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def SetCellWidth(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def GetCellBorderColors(self, pcrLeft: POINTER(Int32), pcrTop: POINTER(Int32), pcrRight: POINTER(Int32), pcrBottom: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def GetCellBorderWidths(self, pduLeft: POINTER(Int32), pduTop: POINTER(Int32), pduRight: POINTER(Int32), pduBottom: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def SetCellBorderColors(self, crLeft: Int32, crTop: Int32, crRight: Int32, crBottom: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def SetCellBorderWidths(self, duLeft: Int32, duTop: Int32, duRight: Int32, duBottom: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def Apply(self, cRow: Int32, Flags: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def CanChange(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def GetProperty(self, Type: Int32, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def Insert(self, cRow: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def IsEqual(self, pRow: win32more.Windows.Win32.UI.Controls.RichEdit.ITextRow, pB: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def Reset(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def SetProperty(self, Type: Int32, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextSelection(ComPtr):
    extends: win32more.Windows.Win32.UI.Controls.RichEdit.ITextRange
    _iid_ = Guid('{8cc497c1-a1df-11ce-8098-00aa0047be5d}')
    @commethod(58)
    def GetFlags(self, pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def SetFlags(self, Flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def GetType(self, pType: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def MoveLeft(self, Unit: Int32, Count: Int32, Extend: Int32, pDelta: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def MoveRight(self, Unit: Int32, Count: Int32, Extend: Int32, pDelta: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def MoveUp(self, Unit: Int32, Count: Int32, Extend: Int32, pDelta: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def MoveDown(self, Unit: Int32, Count: Int32, Extend: Int32, pDelta: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def HomeKey(self, Unit: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants, Extend: Int32, pDelta: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def EndKey(self, Unit: Int32, Extend: Int32, pDelta: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(67)
    def TypeText(self, bstr: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextSelection2(ComPtr):
    extends: win32more.Windows.Win32.UI.Controls.RichEdit.ITextRange2
    _iid_ = Guid('{c241f5e1-7206-11d8-a2c7-00a0d1d6c6b3}')
class ITextServices(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def TxSendMessage(self, msg: UInt32, wparam: win32more.Windows.Win32.Foundation.WPARAM, lparam: win32more.Windows.Win32.Foundation.LPARAM, plresult: POINTER(win32more.Windows.Win32.Foundation.LRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def TxDraw(self, dwDrawAspect: win32more.Windows.Win32.System.Com.DVASPECT, lindex: Int32, pvAspect: VoidPtr, ptd: POINTER(win32more.Windows.Win32.System.Com.DVTARGETDEVICE), hdcDraw: win32more.Windows.Win32.Graphics.Gdi.HDC, hicTargetDev: win32more.Windows.Win32.Graphics.Gdi.HDC, lprcBounds: POINTER(win32more.Windows.Win32.Foundation.RECTL), lprcWBounds: POINTER(win32more.Windows.Win32.Foundation.RECTL), lprcUpdate: POINTER(win32more.Windows.Win32.Foundation.RECT), pfnContinue: IntPtr, dwContinue: UInt32, lViewId: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def TxGetHScroll(self, plMin: POINTER(Int32), plMax: POINTER(Int32), plPos: POINTER(Int32), plPage: POINTER(Int32), pfEnabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def TxGetVScroll(self, plMin: POINTER(Int32), plMax: POINTER(Int32), plPos: POINTER(Int32), plPage: POINTER(Int32), pfEnabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnTxSetCursor(self, dwDrawAspect: win32more.Windows.Win32.System.Com.DVASPECT, lindex: Int32, pvAspect: VoidPtr, ptd: POINTER(win32more.Windows.Win32.System.Com.DVTARGETDEVICE), hdcDraw: win32more.Windows.Win32.Graphics.Gdi.HDC, hicTargetDev: win32more.Windows.Win32.Graphics.Gdi.HDC, lprcClient: POINTER(win32more.Windows.Win32.Foundation.RECT), x: Int32, y: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def TxQueryHitPoint(self, dwDrawAspect: win32more.Windows.Win32.System.Com.DVASPECT, lindex: Int32, pvAspect: VoidPtr, ptd: POINTER(win32more.Windows.Win32.System.Com.DVTARGETDEVICE), hdcDraw: win32more.Windows.Win32.Graphics.Gdi.HDC, hicTargetDev: win32more.Windows.Win32.Graphics.Gdi.HDC, lprcClient: POINTER(win32more.Windows.Win32.Foundation.RECT), x: Int32, y: Int32, pHitResult: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnTxInPlaceActivate(self, prcClient: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OnTxInPlaceDeactivate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def OnTxUIActivate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def OnTxUIDeactivate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def TxGetText(self, pbstrText: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def TxSetText(self, pszText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def TxGetCurTargetX(self, param0: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def TxGetBaseLinePos(self, param0: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def TxGetNaturalSize(self, dwAspect: UInt32, hdcDraw: win32more.Windows.Win32.Graphics.Gdi.HDC, hicTargetDev: win32more.Windows.Win32.Graphics.Gdi.HDC, ptd: POINTER(win32more.Windows.Win32.System.Com.DVTARGETDEVICE), dwMode: UInt32, psizelExtent: POINTER(win32more.Windows.Win32.Foundation.SIZE), pwidth: POINTER(Int32), pheight: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def TxGetDropTarget(self, ppDropTarget: POINTER(win32more.Windows.Win32.System.Ole.IDropTarget)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def OnTxPropertyBitsChange(self, dwMask: UInt32, dwBits: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def TxGetCachedSize(self, pdwWidth: POINTER(UInt32), pdwHeight: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextServices2(ComPtr):
    extends: win32more.Windows.Win32.UI.Controls.RichEdit.ITextServices
    @commethod(21)
    def TxGetNaturalSize2(self, dwAspect: UInt32, hdcDraw: win32more.Windows.Win32.Graphics.Gdi.HDC, hicTargetDev: win32more.Windows.Win32.Graphics.Gdi.HDC, ptd: POINTER(win32more.Windows.Win32.System.Com.DVTARGETDEVICE), dwMode: UInt32, psizelExtent: POINTER(win32more.Windows.Win32.Foundation.SIZE), pwidth: POINTER(Int32), pheight: POINTER(Int32), pascent: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def TxDrawD2D(self, pRenderTarget: win32more.Windows.Win32.Graphics.Direct2D.ID2D1RenderTarget, lprcBounds: POINTER(win32more.Windows.Win32.Foundation.RECTL), lprcUpdate: POINTER(win32more.Windows.Win32.Foundation.RECT), lViewId: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextStory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c241f5f3-7206-11d8-a2c7-00a0d1d6c6b3}')
    @commethod(3)
    def GetActive(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetActive(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDisplay(self, ppDisplay: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetIndex(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetType(self, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetType(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetProperty(self, Type: Int32, pValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRange(self, cpActive: Int32, cpAnchor: Int32, ppRange: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextRange2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetText(self, Flags: Int32, pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetFormattedText(self, pUnk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetProperty(self, Type: Int32, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetText(self, Flags: Int32, bstr: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextStoryRanges(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{8cc497c5-a1df-11ce-8098-00aa0047be5d}')
    @commethod(7)
    def _NewEnum(self, ppunkEnum: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, Index: Int32, ppRange: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextRange)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCount(self, pCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextStoryRanges2(ComPtr):
    extends: win32more.Windows.Win32.UI.Controls.RichEdit.ITextStoryRanges
    _iid_ = Guid('{c241f5e5-7206-11d8-a2c7-00a0d1d6c6b3}')
    @commethod(10)
    def Item2(self, Index: Int32, ppRange: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextRange2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITextStrings(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{c241f5e7-7206-11d8-a2c7-00a0d1d6c6b3}')
    @commethod(7)
    def Item(self, Index: Int32, ppRange: POINTER(win32more.Windows.Win32.UI.Controls.RichEdit.ITextRange2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetCount(self, pCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Add(self, bstr: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Append(self, pRange: win32more.Windows.Win32.UI.Controls.RichEdit.ITextRange2, iString: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Cat2(self, iString: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def CatTop2(self, bstr: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def DeleteRange(self, pRange: win32more.Windows.Win32.UI.Controls.RichEdit.ITextRange2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def EncodeFunction(self, Type: Int32, Align: Int32, Char: Int32, Char1: Int32, Char2: Int32, Count: Int32, TeXStyle: Int32, cCol: Int32, pRange: win32more.Windows.Win32.UI.Controls.RichEdit.ITextRange2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetCch(self, iString: Int32, pcch: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def InsertNullStr(self, iString: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def MoveBoundary(self, iString: Int32, cch: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def PrefixTop(self, bstr: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Remove(self, iString: Int32, cString: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetFormattedText(self, pRangeD: win32more.Windows.Win32.UI.Controls.RichEdit.ITextRange2, pRangeS: win32more.Windows.Win32.UI.Controls.RichEdit.ITextRange2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetOpCp(self, iString: Int32, cp: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SuffixTop(self, bstr: win32more.Windows.Win32.Foundation.BSTR, pRange: win32more.Windows.Win32.UI.Controls.RichEdit.ITextRange2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Swap(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
KHYPH = Int32
khyphNil: win32more.Windows.Win32.UI.Controls.RichEdit.KHYPH = 0
khyphNormal: win32more.Windows.Win32.UI.Controls.RichEdit.KHYPH = 1
khyphAddBefore: win32more.Windows.Win32.UI.Controls.RichEdit.KHYPH = 2
khyphChangeBefore: win32more.Windows.Win32.UI.Controls.RichEdit.KHYPH = 3
khyphDeleteBefore: win32more.Windows.Win32.UI.Controls.RichEdit.KHYPH = 4
khyphChangeAfter: win32more.Windows.Win32.UI.Controls.RichEdit.KHYPH = 5
khyphDelAndChange: win32more.Windows.Win32.UI.Controls.RichEdit.KHYPH = 6
MANCODE = Int32
MBOLD: win32more.Windows.Win32.UI.Controls.RichEdit.MANCODE = 16
MITAL: win32more.Windows.Win32.UI.Controls.RichEdit.MANCODE = 32
MGREEK: win32more.Windows.Win32.UI.Controls.RichEdit.MANCODE = 64
MROMN: win32more.Windows.Win32.UI.Controls.RichEdit.MANCODE = 0
MSCRP: win32more.Windows.Win32.UI.Controls.RichEdit.MANCODE = 1
MFRAK: win32more.Windows.Win32.UI.Controls.RichEdit.MANCODE = 2
MOPEN: win32more.Windows.Win32.UI.Controls.RichEdit.MANCODE = 3
MSANS: win32more.Windows.Win32.UI.Controls.RichEdit.MANCODE = 4
MMONO: win32more.Windows.Win32.UI.Controls.RichEdit.MANCODE = 5
MMATH: win32more.Windows.Win32.UI.Controls.RichEdit.MANCODE = 6
MISOL: win32more.Windows.Win32.UI.Controls.RichEdit.MANCODE = 7
MINIT: win32more.Windows.Win32.UI.Controls.RichEdit.MANCODE = 8
MTAIL: win32more.Windows.Win32.UI.Controls.RichEdit.MANCODE = 9
MSTRCH: win32more.Windows.Win32.UI.Controls.RichEdit.MANCODE = 10
MLOOP: win32more.Windows.Win32.UI.Controls.RichEdit.MANCODE = 11
MOPENA: win32more.Windows.Win32.UI.Controls.RichEdit.MANCODE = 12
if ARCH in 'X64,ARM64':
    class MSGFILTER(Structure):
        nmhdr: win32more.Windows.Win32.UI.Controls.NMHDR
        msg: UInt32
        wParam: win32more.Windows.Win32.Foundation.WPARAM
        lParam: win32more.Windows.Win32.Foundation.LPARAM
        _pack_ = 4
elif ARCH in 'X86':
    class MSGFILTER(Structure):
        nmhdr: win32more.Windows.Win32.UI.Controls.NMHDR
        msg: UInt32
        wParam: win32more.Windows.Win32.Foundation.WPARAM
        lParam: win32more.Windows.Win32.Foundation.LPARAM
if ARCH in 'X64,ARM64':
    class OBJECTPOSITIONS(Structure):
        nmhdr: win32more.Windows.Win32.UI.Controls.NMHDR
        cObjectCount: Int32
        pcpPositions: POINTER(Int32)
        _pack_ = 4
elif ARCH in 'X86':
    class OBJECTPOSITIONS(Structure):
        nmhdr: win32more.Windows.Win32.UI.Controls.NMHDR
        cObjectCount: Int32
        pcpPositions: POINTER(Int32)
OBJECTTYPE = Int32
tomSimpleText: win32more.Windows.Win32.UI.Controls.RichEdit.OBJECTTYPE = 0
tomRuby: win32more.Windows.Win32.UI.Controls.RichEdit.OBJECTTYPE = 1
tomHorzVert: win32more.Windows.Win32.UI.Controls.RichEdit.OBJECTTYPE = 2
tomWarichu: win32more.Windows.Win32.UI.Controls.RichEdit.OBJECTTYPE = 3
tomEq: win32more.Windows.Win32.UI.Controls.RichEdit.OBJECTTYPE = 9
tomMath: win32more.Windows.Win32.UI.Controls.RichEdit.OBJECTTYPE = 10
tomAccent: win32more.Windows.Win32.UI.Controls.RichEdit.OBJECTTYPE = 10
tomBox: win32more.Windows.Win32.UI.Controls.RichEdit.OBJECTTYPE = 11
tomBoxedFormula: win32more.Windows.Win32.UI.Controls.RichEdit.OBJECTTYPE = 12
tomBrackets: win32more.Windows.Win32.UI.Controls.RichEdit.OBJECTTYPE = 13
tomBracketsWithSeps: win32more.Windows.Win32.UI.Controls.RichEdit.OBJECTTYPE = 14
tomEquationArray: win32more.Windows.Win32.UI.Controls.RichEdit.OBJECTTYPE = 15
tomFraction: win32more.Windows.Win32.UI.Controls.RichEdit.OBJECTTYPE = 16
tomFunctionApply: win32more.Windows.Win32.UI.Controls.RichEdit.OBJECTTYPE = 17
tomLeftSubSup: win32more.Windows.Win32.UI.Controls.RichEdit.OBJECTTYPE = 18
tomLowerLimit: win32more.Windows.Win32.UI.Controls.RichEdit.OBJECTTYPE = 19
tomMatrix: win32more.Windows.Win32.UI.Controls.RichEdit.OBJECTTYPE = 20
tomNary: win32more.Windows.Win32.UI.Controls.RichEdit.OBJECTTYPE = 21
tomOpChar: win32more.Windows.Win32.UI.Controls.RichEdit.OBJECTTYPE = 22
tomOverbar: win32more.Windows.Win32.UI.Controls.RichEdit.OBJECTTYPE = 23
tomPhantom: win32more.Windows.Win32.UI.Controls.RichEdit.OBJECTTYPE = 24
tomRadical: win32more.Windows.Win32.UI.Controls.RichEdit.OBJECTTYPE = 25
tomSlashedFraction: win32more.Windows.Win32.UI.Controls.RichEdit.OBJECTTYPE = 26
tomStack: win32more.Windows.Win32.UI.Controls.RichEdit.OBJECTTYPE = 27
tomStretchStack: win32more.Windows.Win32.UI.Controls.RichEdit.OBJECTTYPE = 28
tomSubscript: win32more.Windows.Win32.UI.Controls.RichEdit.OBJECTTYPE = 29
tomSubSup: win32more.Windows.Win32.UI.Controls.RichEdit.OBJECTTYPE = 30
tomSuperscript: win32more.Windows.Win32.UI.Controls.RichEdit.OBJECTTYPE = 31
tomUnderbar: win32more.Windows.Win32.UI.Controls.RichEdit.OBJECTTYPE = 32
tomUpperLimit: win32more.Windows.Win32.UI.Controls.RichEdit.OBJECTTYPE = 33
tomObjectMax: win32more.Windows.Win32.UI.Controls.RichEdit.OBJECTTYPE = 33
class PARAFORMAT(Structure):
    cbSize: UInt32
    dwMask: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK
    wNumbering: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_NUMBERING
    Anonymous: _Anonymous_e__Union
    dxStartIndent: Int32
    dxRightIndent: Int32
    dxOffset: Int32
    wAlignment: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_ALIGNMENT
    cTabCount: Int16
    rgxTabs: UInt32 * 32
    class _Anonymous_e__Union(Union):
        wReserved: UInt16
        wEffects: UInt16
class PARAFORMAT2(Structure):
    Base: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT
    dySpaceBefore: Int32
    dySpaceAfter: Int32
    dyLineSpacing: Int32
    sStyle: Int16
    bLineSpacingRule: Byte
    bOutlineLevel: Byte
    wShadingWeight: UInt16
    wShadingStyle: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_SHADING_STYLE
    wNumberingStart: UInt16
    wNumberingStyle: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_NUMBERING_STYLE
    wNumberingTab: UInt16
    wBorderSpace: UInt16
    wBorderWidth: UInt16
    wBorders: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_BORDERS
PARAFORMAT_ALIGNMENT = UInt16
PFA_LEFT: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_ALIGNMENT = 1
PFA_RIGHT: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_ALIGNMENT = 2
PFA_CENTER: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_ALIGNMENT = 3
PFA_JUSTIFY: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_ALIGNMENT = 4
PFA_FULL_INTERWORD: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_ALIGNMENT = 4
PFA_FULL_NEWSPAPER: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_ALIGNMENT = 5
PFA_FULL_INTERLETTER: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_ALIGNMENT = 6
PFA_FULL_SCALED: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_ALIGNMENT = 7
PFA_FULL_GLYPHS: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_ALIGNMENT = 8
PARAFORMAT_BORDERS = UInt16
PARAFORMAT_BORDERS_LEFT: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_BORDERS = 1
PARAFORMAT_BORDERS_RIGHT: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_BORDERS = 2
PARAFORMAT_BORDERS_TOP: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_BORDERS = 4
PARAFORMAT_BORDERS_BOTTOM: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_BORDERS = 8
PARAFORMAT_BORDERS_INSIDE: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_BORDERS = 16
PARAFORMAT_BORDERS_OUTSIDE: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_BORDERS = 32
PARAFORMAT_BORDERS_AUTOCOLOR: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_BORDERS = 64
PARAFORMAT_MASK = UInt32
PFM_STARTINDENT: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 1
PFM_RIGHTINDENT: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 2
PFM_OFFSET: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 4
PFM_ALIGNMENT: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 8
PFM_TABSTOPS: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 16
PFM_NUMBERING: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 32
PFM_OFFSETINDENT: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 2147483648
PFM_SPACEBEFORE: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 64
PFM_SPACEAFTER: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 128
PFM_LINESPACING: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 256
PFM_STYLE: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 1024
PFM_BORDER: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 2048
PFM_SHADING: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 4096
PFM_NUMBERINGSTYLE: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 8192
PFM_NUMBERINGTAB: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 16384
PFM_NUMBERINGSTART: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 32768
PFM_RTLPARA: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 65536
PFM_KEEP: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 131072
PFM_KEEPNEXT: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 262144
PFM_PAGEBREAKBEFORE: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 524288
PFM_NOLINENUMBER: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 1048576
PFM_NOWIDOWCONTROL: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 2097152
PFM_DONOTHYPHEN: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 4194304
PFM_SIDEBYSIDE: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 8388608
PFM_COLLAPSED: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 16777216
PFM_OUTLINELEVEL: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 33554432
PFM_BOX: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 67108864
PFM_RESERVED2: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 134217728
PFM_TABLEROWDELIMITER: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 268435456
PFM_TEXTWRAPPINGBREAK: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 536870912
PFM_TABLE: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 1073741824
PFM_ALL: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 2147549247
PFM_EFFECTS: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 1358888960
PFM_ALL2: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_MASK = 3506437631
PARAFORMAT_NUMBERING = UInt16
PFN_BULLET: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_NUMBERING = 1
PFN_ARABIC: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_NUMBERING = 2
PFN_LCLETTER: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_NUMBERING = 3
PFN_UCLETTER: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_NUMBERING = 4
PFN_LCROMAN: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_NUMBERING = 5
PFN_UCROMAN: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_NUMBERING = 6
PARAFORMAT_NUMBERING_STYLE = UInt16
PFNS_PAREN: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_NUMBERING_STYLE = 0
PFNS_PARENS: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_NUMBERING_STYLE = 256
PFNS_PERIOD: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_NUMBERING_STYLE = 512
PFNS_PLAIN: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_NUMBERING_STYLE = 768
PFNS_NONUMBER: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_NUMBERING_STYLE = 1024
PFNS_NEWNUMBER: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_NUMBERING_STYLE = 32768
PARAFORMAT_SHADING_STYLE = UInt16
PARAFORMAT_SHADING_STYLE_NONE: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_SHADING_STYLE = 0
PARAFORMAT_SHADING_STYLE_DARK_HORIZ: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_SHADING_STYLE = 1
PARAFORMAT_SHADING_STYLE_DARK_VERT: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_SHADING_STYLE = 2
PARAFORMAT_SHADING_STYLE_DARK_DOWN_DIAG: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_SHADING_STYLE = 3
PARAFORMAT_SHADING_STYLE_DARK_UP_DIAG: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_SHADING_STYLE = 4
PARAFORMAT_SHADING_STYLE_DARK_GRID: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_SHADING_STYLE = 5
PARAFORMAT_SHADING_STYLE_DARK_TRELLIS: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_SHADING_STYLE = 6
PARAFORMAT_SHADING_STYLE_LIGHT_HORZ: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_SHADING_STYLE = 7
PARAFORMAT_SHADING_STYLE_LIGHT_VERT: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_SHADING_STYLE = 8
PARAFORMAT_SHADING_STYLE_LIGHT_DOWN_DIAG: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_SHADING_STYLE = 9
PARAFORMAT_SHADING_STYLE_LIGHT_UP_DIAG: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_SHADING_STYLE = 10
PARAFORMAT_SHADING_STYLE_LIGHT_GRID: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_SHADING_STYLE = 11
PARAFORMAT_SHADING_STYLE_LIGHT_TRELLIS: win32more.Windows.Win32.UI.Controls.RichEdit.PARAFORMAT_SHADING_STYLE = 12
@winfunctype_pointer
def PCreateTextServices(punkOuter: win32more.Windows.Win32.System.Com.IUnknown, pITextHost: win32more.Windows.Win32.UI.Controls.RichEdit.ITextHost, ppUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PShutdownTextServices(pTextServices: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
if ARCH in 'X64,ARM64':
    class PUNCTUATION(Structure):
        iSize: UInt32
        szPunctuation: win32more.Windows.Win32.Foundation.PSTR
        _pack_ = 4
elif ARCH in 'X86':
    class PUNCTUATION(Structure):
        iSize: UInt32
        szPunctuation: win32more.Windows.Win32.Foundation.PSTR
class REOBJECT(Structure):
    cbStruct: UInt32
    cp: Int32
    clsid: Guid
    poleobj: win32more.Windows.Win32.System.Ole.IOleObject
    pstg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage
    polesite: win32more.Windows.Win32.System.Ole.IOleClientSite
    sizel: win32more.Windows.Win32.Foundation.SIZE
    dvaspect: UInt32
    dwFlags: win32more.Windows.Win32.UI.Controls.RichEdit.REOBJECT_FLAGS
    dwUser: UInt32
REOBJECT_FLAGS = UInt32
REO_ALIGNTORIGHT: win32more.Windows.Win32.UI.Controls.RichEdit.REOBJECT_FLAGS = 256
REO_BELOWBASELINE: win32more.Windows.Win32.UI.Controls.RichEdit.REOBJECT_FLAGS = 2
REO_BLANK: win32more.Windows.Win32.UI.Controls.RichEdit.REOBJECT_FLAGS = 16
REO_CANROTATE: win32more.Windows.Win32.UI.Controls.RichEdit.REOBJECT_FLAGS = 128
REO_DONTNEEDPALETTE: win32more.Windows.Win32.UI.Controls.RichEdit.REOBJECT_FLAGS = 32
REO_DYNAMICSIZE: win32more.Windows.Win32.UI.Controls.RichEdit.REOBJECT_FLAGS = 8
REO_GETMETAFILE: win32more.Windows.Win32.UI.Controls.RichEdit.REOBJECT_FLAGS = 4194304
REO_HILITED: win32more.Windows.Win32.UI.Controls.RichEdit.REOBJECT_FLAGS = 16777216
REO_INPLACEACTIVE: win32more.Windows.Win32.UI.Controls.RichEdit.REOBJECT_FLAGS = 33554432
REO_INVERTEDSELECT: win32more.Windows.Win32.UI.Controls.RichEdit.REOBJECT_FLAGS = 4
REO_LINK: win32more.Windows.Win32.UI.Controls.RichEdit.REOBJECT_FLAGS = 2147483648
REO_LINKAVAILABLE: win32more.Windows.Win32.UI.Controls.RichEdit.REOBJECT_FLAGS = 8388608
REO_OPEN: win32more.Windows.Win32.UI.Controls.RichEdit.REOBJECT_FLAGS = 67108864
REO_OWNERDRAWSELECT: win32more.Windows.Win32.UI.Controls.RichEdit.REOBJECT_FLAGS = 64
REO_RESIZABLE: win32more.Windows.Win32.UI.Controls.RichEdit.REOBJECT_FLAGS = 1
REO_SELECTED: win32more.Windows.Win32.UI.Controls.RichEdit.REOBJECT_FLAGS = 134217728
REO_STATIC: win32more.Windows.Win32.UI.Controls.RichEdit.REOBJECT_FLAGS = 1073741824
REO_USEASBACKGROUND: win32more.Windows.Win32.UI.Controls.RichEdit.REOBJECT_FLAGS = 1024
REO_WRAPTEXTAROUND: win32more.Windows.Win32.UI.Controls.RichEdit.REOBJECT_FLAGS = 512
if ARCH in 'X64,ARM64':
    class REPASTESPECIAL(Structure):
        dwAspect: win32more.Windows.Win32.System.Com.DVASPECT
        dwParam: UIntPtr
        _pack_ = 4
elif ARCH in 'X86':
    class REPASTESPECIAL(Structure):
        dwAspect: win32more.Windows.Win32.System.Com.DVASPECT
        dwParam: UIntPtr
if ARCH in 'X64,ARM64':
    class REQRESIZE(Structure):
        nmhdr: win32more.Windows.Win32.UI.Controls.NMHDR
        rc: win32more.Windows.Win32.Foundation.RECT
        _pack_ = 4
elif ARCH in 'X86':
    class REQRESIZE(Structure):
        nmhdr: win32more.Windows.Win32.UI.Controls.NMHDR
        rc: win32more.Windows.Win32.Foundation.RECT
if ARCH in 'X64,ARM64':
    class RICHEDIT_IMAGE_PARAMETERS(Structure):
        xWidth: Int32
        yHeight: Int32
        Ascent: Int32
        Type: Int32
        pwszAlternateText: win32more.Windows.Win32.Foundation.PWSTR
        pIStream: win32more.Windows.Win32.System.Com.IStream
        _pack_ = 4
elif ARCH in 'X86':
    class RICHEDIT_IMAGE_PARAMETERS(Structure):
        xWidth: Int32
        yHeight: Int32
        Ascent: Int32
        Type: Int32
        pwszAlternateText: win32more.Windows.Win32.Foundation.PWSTR
        pIStream: win32more.Windows.Win32.System.Com.IStream
RICH_EDIT_GET_CONTEXT_MENU_SEL_TYPE = UInt16
SEL_EMPTY: win32more.Windows.Win32.UI.Controls.RichEdit.RICH_EDIT_GET_CONTEXT_MENU_SEL_TYPE = 0
SEL_TEXT: win32more.Windows.Win32.UI.Controls.RichEdit.RICH_EDIT_GET_CONTEXT_MENU_SEL_TYPE = 1
SEL_OBJECT: win32more.Windows.Win32.UI.Controls.RichEdit.RICH_EDIT_GET_CONTEXT_MENU_SEL_TYPE = 2
SEL_MULTICHAR: win32more.Windows.Win32.UI.Controls.RichEdit.RICH_EDIT_GET_CONTEXT_MENU_SEL_TYPE = 4
SEL_MULTIOBJECT: win32more.Windows.Win32.UI.Controls.RichEdit.RICH_EDIT_GET_CONTEXT_MENU_SEL_TYPE = 8
GCM_RIGHTMOUSEDROP: win32more.Windows.Win32.UI.Controls.RichEdit.RICH_EDIT_GET_CONTEXT_MENU_SEL_TYPE = 32768
RICH_EDIT_GET_OBJECT_FLAGS = UInt32
REO_GETOBJ_POLEOBJ: win32more.Windows.Win32.UI.Controls.RichEdit.RICH_EDIT_GET_OBJECT_FLAGS = 1
REO_GETOBJ_PSTG: win32more.Windows.Win32.UI.Controls.RichEdit.RICH_EDIT_GET_OBJECT_FLAGS = 2
REO_GETOBJ_POLESITE: win32more.Windows.Win32.UI.Controls.RichEdit.RICH_EDIT_GET_OBJECT_FLAGS = 4
REO_GETOBJ_NO_INTERFACES: win32more.Windows.Win32.UI.Controls.RichEdit.RICH_EDIT_GET_OBJECT_FLAGS = 0
REO_GETOBJ_ALL_INTERFACES: win32more.Windows.Win32.UI.Controls.RichEdit.RICH_EDIT_GET_OBJECT_FLAGS = 7
if ARCH in 'X64,ARM64':
    class SELCHANGE(Structure):
        nmhdr: win32more.Windows.Win32.UI.Controls.NMHDR
        chrg: win32more.Windows.Win32.UI.Controls.RichEdit.CHARRANGE
        seltyp: win32more.Windows.Win32.UI.Controls.RichEdit.RICH_EDIT_GET_CONTEXT_MENU_SEL_TYPE
        _pack_ = 4
elif ARCH in 'X86':
    class SELCHANGE(Structure):
        nmhdr: win32more.Windows.Win32.UI.Controls.NMHDR
        chrg: win32more.Windows.Win32.UI.Controls.RichEdit.CHARRANGE
        seltyp: win32more.Windows.Win32.UI.Controls.RichEdit.RICH_EDIT_GET_CONTEXT_MENU_SEL_TYPE
class SETTEXTEX(Structure):
    flags: UInt32
    codepage: UInt32
class TABLECELLPARMS(Structure):
    dxWidth: Int32
    nVertAlign: Annotated[UInt16, 2]
    fMergeTop: Annotated[UInt16, 1]
    fMergePrev: Annotated[UInt16, 1]
    fVertical: Annotated[UInt16, 1]
    fMergeStart: Annotated[UInt16, 1]
    fMergeCont: Annotated[UInt16, 1]
    wShading: UInt16
    dxBrdrLeft: Int16
    dyBrdrTop: Int16
    dxBrdrRight: Int16
    dyBrdrBottom: Int16
    crBrdrLeft: win32more.Windows.Win32.Foundation.COLORREF
    crBrdrTop: win32more.Windows.Win32.Foundation.COLORREF
    crBrdrRight: win32more.Windows.Win32.Foundation.COLORREF
    crBrdrBottom: win32more.Windows.Win32.Foundation.COLORREF
    crBackPat: win32more.Windows.Win32.Foundation.COLORREF
    crForePat: win32more.Windows.Win32.Foundation.COLORREF
class TABLEROWPARMS(Structure):
    cbRow: Byte
    cbCell: Byte
    cCell: Byte
    cRow: Byte
    dxCellMargin: Int32
    dxIndent: Int32
    dyHeight: Int32
    nAlignment: Annotated[UInt32, 3]
    fRTL: Annotated[UInt32, 1]
    fKeep: Annotated[UInt32, 1]
    fKeepFollow: Annotated[UInt32, 1]
    fWrap: Annotated[UInt32, 1]
    fIdentCells: Annotated[UInt32, 1]
    cpStartRow: Int32
    bTableLevel: Byte
    iCell: Byte
TEXTMODE = Int32
TM_PLAINTEXT: win32more.Windows.Win32.UI.Controls.RichEdit.TEXTMODE = 1
TM_RICHTEXT: win32more.Windows.Win32.UI.Controls.RichEdit.TEXTMODE = 2
TM_SINGLELEVELUNDO: win32more.Windows.Win32.UI.Controls.RichEdit.TEXTMODE = 4
TM_MULTILEVELUNDO: win32more.Windows.Win32.UI.Controls.RichEdit.TEXTMODE = 8
TM_SINGLECODEPAGE: win32more.Windows.Win32.UI.Controls.RichEdit.TEXTMODE = 16
TM_MULTICODEPAGE: win32more.Windows.Win32.UI.Controls.RichEdit.TEXTMODE = 32
if ARCH in 'X64,ARM64':
    class TEXTRANGEA(Structure):
        chrg: win32more.Windows.Win32.UI.Controls.RichEdit.CHARRANGE
        lpstrText: win32more.Windows.Win32.Foundation.PSTR
        _pack_ = 4
elif ARCH in 'X86':
    class TEXTRANGEA(Structure):
        chrg: win32more.Windows.Win32.UI.Controls.RichEdit.CHARRANGE
        lpstrText: win32more.Windows.Win32.Foundation.PSTR
if ARCH in 'X64,ARM64':
    class TEXTRANGEW(Structure):
        chrg: win32more.Windows.Win32.UI.Controls.RichEdit.CHARRANGE
        lpstrText: win32more.Windows.Win32.Foundation.PWSTR
        _pack_ = 4
elif ARCH in 'X86':
    class TEXTRANGEW(Structure):
        chrg: win32more.Windows.Win32.UI.Controls.RichEdit.CHARRANGE
        lpstrText: win32more.Windows.Win32.Foundation.PWSTR
if ARCH in 'X64,ARM64':
    TEXTRANGE = UnicodeAlias('TEXTRANGEW')
elif ARCH in 'X86':
    TEXTRANGE = UnicodeAlias('TEXTRANGEW')
TXTBACKSTYLE = Int32
TXTBACK_TRANSPARENT: win32more.Windows.Win32.UI.Controls.RichEdit.TXTBACKSTYLE = 0
TXTBACK_OPAQUE: win32more.Windows.Win32.UI.Controls.RichEdit.TXTBACKSTYLE = 1
TXTHITRESULT = Int32
TXTHITRESULT_NOHIT: win32more.Windows.Win32.UI.Controls.RichEdit.TXTHITRESULT = 0
TXTHITRESULT_TRANSPARENT: win32more.Windows.Win32.UI.Controls.RichEdit.TXTHITRESULT = 1
TXTHITRESULT_CLOSE: win32more.Windows.Win32.UI.Controls.RichEdit.TXTHITRESULT = 2
TXTHITRESULT_HIT: win32more.Windows.Win32.UI.Controls.RichEdit.TXTHITRESULT = 3
TXTNATURALSIZE = Int32
TXTNS_FITTOCONTENT2: win32more.Windows.Win32.UI.Controls.RichEdit.TXTNATURALSIZE = 0
TXTNS_FITTOCONTENT: win32more.Windows.Win32.UI.Controls.RichEdit.TXTNATURALSIZE = 1
TXTNS_ROUNDTOLINE: win32more.Windows.Win32.UI.Controls.RichEdit.TXTNATURALSIZE = 2
TXTNS_FITTOCONTENT3: win32more.Windows.Win32.UI.Controls.RichEdit.TXTNATURALSIZE = 3
TXTNS_FITTOCONTENTWSP: win32more.Windows.Win32.UI.Controls.RichEdit.TXTNATURALSIZE = 4
TXTNS_INCLUDELASTLINE: win32more.Windows.Win32.UI.Controls.RichEdit.TXTNATURALSIZE = 1073741824
TXTNS_EMU: win32more.Windows.Win32.UI.Controls.RichEdit.TXTNATURALSIZE = -2147483648
TXTVIEW = Int32
TXTVIEW_ACTIVE: win32more.Windows.Win32.UI.Controls.RichEdit.TXTVIEW = 0
TXTVIEW_INACTIVE: win32more.Windows.Win32.UI.Controls.RichEdit.TXTVIEW = -1
UNDONAMEID = Int32
UID_UNKNOWN: win32more.Windows.Win32.UI.Controls.RichEdit.UNDONAMEID = 0
UID_TYPING: win32more.Windows.Win32.UI.Controls.RichEdit.UNDONAMEID = 1
UID_DELETE: win32more.Windows.Win32.UI.Controls.RichEdit.UNDONAMEID = 2
UID_DRAGDROP: win32more.Windows.Win32.UI.Controls.RichEdit.UNDONAMEID = 3
UID_CUT: win32more.Windows.Win32.UI.Controls.RichEdit.UNDONAMEID = 4
UID_PASTE: win32more.Windows.Win32.UI.Controls.RichEdit.UNDONAMEID = 5
UID_AUTOTABLE: win32more.Windows.Win32.UI.Controls.RichEdit.UNDONAMEID = 6
tomConstants = Int32
tomFalse: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomTrue: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -1
tomUndefined: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -9999999
tomToggle: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -9999998
tomAutoColor: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -9999997
tomDefault: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -9999996
tomSuspend: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -9999995
tomResume: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -9999994
tomApplyNow: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomApplyLater: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomTrackParms: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomCacheParms: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomApplyTmp: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomDisableSmartFont: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 8
tomEnableSmartFont: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 9
tomUsePoints: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 10
tomUseTwips: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 11
tomBackward: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -1073741823
tomForward: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1073741823
tomMove: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomExtend: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomNoSelection: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomSelectionIP: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomSelectionNormal: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomSelectionFrame: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomSelectionColumn: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomSelectionRow: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 5
tomSelectionBlock: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 6
tomSelectionInlineShape: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 7
tomSelectionShape: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 8
tomSelStartActive: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomSelAtEOL: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomSelOvertype: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomSelActive: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 8
tomSelReplace: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 16
tomEnd: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomStart: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 32
tomCollapseEnd: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomCollapseStart: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomClientCoord: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 256
tomAllowOffClient: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 512
tomTransform: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1024
tomObjectArg: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2048
tomAtEnd: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4096
tomNone: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomSingle: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomWords: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomDouble: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomDotted: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomDash: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 5
tomDashDot: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 6
tomDashDotDot: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 7
tomWave: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 8
tomThick: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 9
tomHair: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 10
tomDoubleWave: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 11
tomHeavyWave: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 12
tomLongDash: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 13
tomThickDash: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 14
tomThickDashDot: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 15
tomThickDashDotDot: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 16
tomThickDotted: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 17
tomThickLongDash: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 18
tomLineSpaceSingle: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomLineSpace1pt5: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomLineSpaceDouble: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomLineSpaceAtLeast: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomLineSpaceExactly: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomLineSpaceMultiple: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 5
tomLineSpacePercent: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 6
tomAlignLeft: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomAlignCenter: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomAlignRight: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomAlignJustify: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomAlignDecimal: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomAlignBar: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomDefaultTab: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 5
tomAlignInterWord: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomAlignNewspaper: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomAlignInterLetter: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 5
tomAlignScaled: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 6
tomSpaces: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomDots: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomDashes: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomLines: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomThickLines: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomEquals: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 5
tomTabBack: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -3
tomTabNext: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -2
tomTabHere: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -1
tomListNone: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomListBullet: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomListNumberAsArabic: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomListNumberAsLCLetter: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomListNumberAsUCLetter: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomListNumberAsLCRoman: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 5
tomListNumberAsUCRoman: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 6
tomListNumberAsSequence: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 7
tomListNumberedCircle: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 8
tomListNumberedBlackCircleWingding: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 9
tomListNumberedWhiteCircleWingding: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 10
tomListNumberedArabicWide: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 11
tomListNumberedChS: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 12
tomListNumberedChT: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 13
tomListNumberedJpnChS: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 14
tomListNumberedJpnKor: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 15
tomListNumberedArabic1: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 16
tomListNumberedArabic2: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 17
tomListNumberedHebrew: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 18
tomListNumberedThaiAlpha: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 19
tomListNumberedThaiNum: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 20
tomListNumberedHindiAlpha: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 21
tomListNumberedHindiAlpha1: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 22
tomListNumberedHindiNum: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 23
tomListParentheses: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 65536
tomListPeriod: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 131072
tomListPlain: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 196608
tomListNoNumber: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 262144
tomListMinus: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 524288
tomIgnoreNumberStyle: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 16777216
tomParaStyleNormal: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -1
tomParaStyleHeading1: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -2
tomParaStyleHeading2: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -3
tomParaStyleHeading3: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -4
tomParaStyleHeading4: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -5
tomParaStyleHeading5: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -6
tomParaStyleHeading6: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -7
tomParaStyleHeading7: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -8
tomParaStyleHeading8: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -9
tomParaStyleHeading9: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -10
tomCharacter: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomWord: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomSentence: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomParagraph: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomLine: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 5
tomStory: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 6
tomScreen: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 7
tomSection: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 8
tomTableColumn: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 9
tomColumn: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 9
tomRow: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 10
tomWindow: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 11
tomCell: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 12
tomCharFormat: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 13
tomParaFormat: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 14
tomTable: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 15
tomObject: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 16
tomPage: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 17
tomHardParagraph: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 18
tomCluster: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 19
tomInlineObject: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 20
tomInlineObjectArg: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 21
tomLeafLine: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 22
tomLayoutColumn: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 23
tomProcessId: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1073741825
tomMatchWord: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomMatchCase: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomMatchPattern: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 8
tomUnknownStory: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomMainTextStory: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomFootnotesStory: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomEndnotesStory: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomCommentsStory: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomTextFrameStory: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 5
tomEvenPagesHeaderStory: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 6
tomPrimaryHeaderStory: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 7
tomEvenPagesFooterStory: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 8
tomPrimaryFooterStory: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 9
tomFirstPageHeaderStory: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 10
tomFirstPageFooterStory: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 11
tomScratchStory: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 127
tomFindStory: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 128
tomReplaceStory: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 129
tomStoryInactive: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomStoryActiveDisplay: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomStoryActiveUI: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomStoryActiveDisplayUI: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomNoAnimation: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomLasVegasLights: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomBlinkingBackground: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomSparkleText: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomMarchingBlackAnts: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomMarchingRedAnts: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 5
tomShimmer: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 6
tomWipeDown: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 7
tomWipeRight: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 8
tomAnimationMax: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 8
tomLowerCase: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomUpperCase: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomTitleCase: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomSentenceCase: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomToggleCase: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 5
tomReadOnly: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 256
tomShareDenyRead: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 512
tomShareDenyWrite: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1024
tomPasteFile: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4096
tomCreateNew: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 16
tomCreateAlways: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 32
tomOpenExisting: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 48
tomOpenAlways: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 64
tomTruncateExisting: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 80
tomRTF: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomText: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomHTML: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomWordDocument: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomBold: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -2147483647
tomItalic: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -2147483646
tomUnderline: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -2147483644
tomStrikeout: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -2147483640
tomProtected: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -2147483632
tomLink: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -2147483616
tomSmallCaps: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -2147483584
tomAllCaps: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -2147483520
tomHidden: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -2147483392
tomOutline: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -2147483136
tomShadow: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -2147482624
tomEmboss: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -2147481600
tomImprint: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -2147479552
tomDisabled: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -2147475456
tomRevised: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -2147467264
tomSubscriptCF: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -2147418112
tomSuperscriptCF: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -2147352576
tomFontBound: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -2146435072
tomLinkProtected: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -2139095040
tomInlineObjectStart: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -2130706432
tomExtendedChar: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -2113929216
tomAutoBackColor: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -2080374784
tomMathZoneNoBuildUp: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -2013265920
tomMathZone: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -1879048192
tomMathZoneOrdinary: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -1610612736
tomAutoTextColor: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -1073741824
tomMathZoneDisplay: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 262144
tomParaEffectRTL: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomParaEffectKeep: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomParaEffectKeepNext: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomParaEffectPageBreakBefore: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 8
tomParaEffectNoLineNumber: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 16
tomParaEffectNoWidowControl: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 32
tomParaEffectDoNotHyphen: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 64
tomParaEffectSideBySide: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 128
tomParaEffectCollapsed: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 256
tomParaEffectOutlineLevel: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 512
tomParaEffectBox: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1024
tomParaEffectTableRowDelimiter: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4096
tomParaEffectTable: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 16384
tomModWidthPairs: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomModWidthSpace: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomAutoSpaceAlpha: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomAutoSpaceNumeric: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 8
tomAutoSpaceParens: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 16
tomEmbeddedFont: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 32
tomDoublestrike: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 64
tomOverlapping: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 128
tomNormalCaret: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomKoreanBlockCaret: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomNullCaret: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomIncludeInset: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomUnicodeBiDi: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomMathCFCheck: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomUnlink: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 8
tomUnhide: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 16
tomCheckTextLimit: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 32
tomIgnoreCurrentFont: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomMatchCharRep: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomMatchFontSignature: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomMatchAscii: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomGetHeightOnly: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 8
tomMatchMathFont: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 16
tomCharset: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = -2147483648
tomCharRepFromLcid: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1073741824
tomAnsi: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomEastEurope: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomCyrillic: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomGreek: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomTurkish: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomHebrew: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 5
tomArabic: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 6
tomBaltic: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 7
tomVietnamese: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 8
tomDefaultCharRep: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 9
tomSymbol: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 10
tomThai: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 11
tomShiftJIS: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 12
tomGB2312: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 13
tomHangul: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 14
tomBIG5: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 15
tomPC437: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 16
tomOEM: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 17
tomMac: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 18
tomArmenian: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 19
tomSyriac: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 20
tomThaana: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 21
tomDevanagari: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 22
tomBengali: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 23
tomGurmukhi: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 24
tomGujarati: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 25
tomOriya: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 26
tomTamil: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 27
tomTelugu: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 28
tomKannada: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 29
tomMalayalam: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 30
tomSinhala: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 31
tomLao: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 32
tomTibetan: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 33
tomMyanmar: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 34
tomGeorgian: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 35
tomJamo: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 36
tomEthiopic: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 37
tomCherokee: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 38
tomAboriginal: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 39
tomOgham: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 40
tomRunic: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 41
tomKhmer: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 42
tomMongolian: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 43
tomBraille: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 44
tomYi: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 45
tomLimbu: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 46
tomTaiLe: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 47
tomNewTaiLue: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 48
tomSylotiNagri: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 49
tomKharoshthi: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 50
tomKayahli: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 51
tomUsymbol: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 52
tomEmoji: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 53
tomGlagolitic: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 54
tomLisu: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 55
tomVai: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 56
tomNKo: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 57
tomOsmanya: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 58
tomPhagsPa: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 59
tomGothic: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 60
tomDeseret: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 61
tomTifinagh: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 62
tomCharRepMax: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 63
tomRE10Mode: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomUseAtFont: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomTextFlowMask: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 12
tomTextFlowES: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomTextFlowSW: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomTextFlowWN: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 8
tomTextFlowNE: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 12
tomNoIME: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 524288
tomSelfIME: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 262144
tomNoUpScroll: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 65536
tomNoVpScroll: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 262144
tomNoLink: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomClientLink: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomFriendlyLinkName: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomFriendlyLinkAddress: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomAutoLinkURL: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomAutoLinkEmail: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 5
tomAutoLinkPhone: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 6
tomAutoLinkPath: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 7
tomCompressNone: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomCompressPunctuation: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomCompressPunctuationAndKana: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomCompressMax: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomUnderlinePositionAuto: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomUnderlinePositionBelow: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomUnderlinePositionAbove: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomUnderlinePositionMax: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomFontAlignmentAuto: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomFontAlignmentTop: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomFontAlignmentBaseline: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomFontAlignmentBottom: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomFontAlignmentCenter: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomFontAlignmentMax: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomRubyBelow: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 128
tomRubyAlignCenter: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomRubyAlign010: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomRubyAlign121: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomRubyAlignLeft: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomRubyAlignRight: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomLimitsDefault: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomLimitsUnderOver: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomLimitsSubSup: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomUpperLimitAsSuperScript: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomLimitsOpposite: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomShowLLimPlaceHldr: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 8
tomShowULimPlaceHldr: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 16
tomDontGrowWithContent: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 64
tomGrowWithContent: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 128
tomSubSupAlign: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomLimitAlignMask: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomLimitAlignCenter: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomLimitAlignLeft: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomLimitAlignRight: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomShowDegPlaceHldr: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 8
tomAlignDefault: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomAlignMatchAscentDescent: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomMathVariant: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 32
tomStyleDefault: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomStyleScriptScriptCramped: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomStyleScriptScript: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomStyleScriptCramped: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomStyleScript: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomStyleTextCramped: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 5
tomStyleText: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 6
tomStyleDisplayCramped: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 7
tomStyleDisplay: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 8
tomMathRelSize: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 64
tomDecDecSize: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 254
tomDecSize: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 255
tomIncSize: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 65
tomIncIncSize: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 66
tomGravityUI: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomGravityBack: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomGravityFore: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomGravityIn: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomGravityOut: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomGravityBackward: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 536870912
tomGravityForward: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1073741824
tomAdjustCRLF: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomUseCRLF: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomTextize: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomAllowFinalEOP: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 8
tomFoldMathAlpha: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 16
tomNoHidden: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 32
tomIncludeNumbering: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 64
tomTranslateTableCell: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 128
tomNoMathZoneBrackets: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 256
tomConvertMathChar: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 512
tomNoUCGreekItalic: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1024
tomAllowMathBold: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2048
tomLanguageTag: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4096
tomConvertRTF: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 8192
tomApplyRtfDocProps: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 16384
tomPhantomShow: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomPhantomZeroWidth: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomPhantomZeroAscent: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomPhantomZeroDescent: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 8
tomPhantomTransparent: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 16
tomPhantomASmash: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 5
tomPhantomDSmash: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 9
tomPhantomHSmash: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomPhantomSmash: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 13
tomPhantomHorz: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 12
tomPhantomVert: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomBoxHideTop: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomBoxHideBottom: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomBoxHideLeft: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomBoxHideRight: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 8
tomBoxStrikeH: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 16
tomBoxStrikeV: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 32
tomBoxStrikeTLBR: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 64
tomBoxStrikeBLTR: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 128
tomBoxAlignCenter: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomSpaceMask: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 28
tomSpaceDefault: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomSpaceUnary: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomSpaceBinary: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 8
tomSpaceRelational: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 12
tomSpaceSkip: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 16
tomSpaceOrd: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 20
tomSpaceDifferential: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 24
tomSizeText: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 32
tomSizeScript: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 64
tomSizeScriptScript: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 96
tomNoBreak: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 128
tomTransparentForPositioning: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 256
tomTransparentForSpacing: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 512
tomStretchCharBelow: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomStretchCharAbove: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomStretchBaseBelow: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomStretchBaseAbove: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomMatrixAlignMask: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomMatrixAlignCenter: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomMatrixAlignTopRow: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomMatrixAlignBottomRow: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomShowMatPlaceHldr: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 8
tomEqArrayLayoutWidth: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomEqArrayAlignMask: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 12
tomEqArrayAlignCenter: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomEqArrayAlignTopRow: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomEqArrayAlignBottomRow: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 12
tomMathManualBreakMask: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 127
tomMathBreakLeft: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 125
tomMathBreakCenter: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 126
tomMathBreakRight: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 127
tomMathEqAlign: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 128
tomMathArgShadingStart: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 593
tomMathArgShadingEnd: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 594
tomMathObjShadingStart: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 595
tomMathObjShadingEnd: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 596
tomFunctionTypeNone: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomFunctionTypeTakesArg: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomFunctionTypeTakesLim: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomFunctionTypeTakesLim2: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomFunctionTypeIsLim: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomMathParaAlignDefault: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomMathParaAlignCenterGroup: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomMathParaAlignCenter: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomMathParaAlignLeft: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomMathParaAlignRight: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomMathDispAlignMask: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomMathDispAlignCenterGroup: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomMathDispAlignCenter: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomMathDispAlignLeft: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomMathDispAlignRight: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomMathDispIntUnderOver: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomMathDispFracTeX: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 8
tomMathDispNaryGrow: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 16
tomMathDocEmptyArgMask: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 96
tomMathDocEmptyArgAuto: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomMathDocEmptyArgAlways: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 32
tomMathDocEmptyArgNever: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 64
tomMathDocSbSpOpUnchanged: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 128
tomMathDocDiffMask: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 768
tomMathDocDiffDefault: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomMathDocDiffUpright: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 256
tomMathDocDiffItalic: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 512
tomMathDocDiffOpenItalic: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 768
tomMathDispNarySubSup: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1024
tomMathDispDef: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2048
tomMathEnableRtl: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4096
tomMathBrkBinMask: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 196608
tomMathBrkBinBefore: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomMathBrkBinAfter: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 65536
tomMathBrkBinDup: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 131072
tomMathBrkBinSubMask: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 786432
tomMathBrkBinSubMM: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomMathBrkBinSubPM: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 262144
tomMathBrkBinSubMP: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 524288
tomSelRange: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 597
tomHstring: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 596
tomFontPropTeXStyle: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 828
tomFontPropAlign: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 829
tomFontStretch: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 830
tomFontStyle: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 831
tomFontStyleUpright: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomFontStyleOblique: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomFontStyleItalic: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomFontStretchDefault: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomFontStretchUltraCondensed: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomFontStretchExtraCondensed: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomFontStretchCondensed: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomFontStretchSemiCondensed: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomFontStretchNormal: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 5
tomFontStretchSemiExpanded: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 6
tomFontStretchExpanded: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 7
tomFontStretchExtraExpanded: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 8
tomFontStretchUltraExpanded: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 9
tomFontWeightDefault: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomFontWeightThin: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 100
tomFontWeightExtraLight: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 200
tomFontWeightLight: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 300
tomFontWeightNormal: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 400
tomFontWeightRegular: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 400
tomFontWeightMedium: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 500
tomFontWeightSemiBold: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 600
tomFontWeightBold: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 700
tomFontWeightExtraBold: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 800
tomFontWeightBlack: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 900
tomFontWeightHeavy: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 900
tomFontWeightExtraBlack: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 950
tomParaPropMathAlign: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1079
tomDocMathBuild: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 128
tomMathLMargin: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 129
tomMathRMargin: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 130
tomMathWrapIndent: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 131
tomMathWrapRight: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 132
tomMathPostSpace: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 134
tomMathPreSpace: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 133
tomMathInterSpace: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 135
tomMathIntraSpace: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 136
tomCanCopy: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 137
tomCanRedo: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 138
tomCanUndo: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 139
tomUndoLimit: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 140
tomDocAutoLink: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 141
tomEllipsisMode: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 142
tomEllipsisState: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 143
tomEllipsisNone: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomEllipsisEnd: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomEllipsisWord: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 3
tomEllipsisPresent: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomVTopCell: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomVLowCell: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2
tomHStartCell: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 4
tomHContCell: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 8
tomRowUpdate: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomRowApplyDefault: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 0
tomCellStructureChangeOnly: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 1
tomRowHeightActual: win32more.Windows.Win32.UI.Controls.RichEdit.tomConstants = 2059


make_ready(__name__)
