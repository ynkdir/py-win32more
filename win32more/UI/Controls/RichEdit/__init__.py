from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Globalization
import win32more.Graphics.Direct2D
import win32more.Graphics.Gdi
import win32more.System.Com
import win32more.System.Com.StructuredStorage
import win32more.System.Ole
import win32more.UI.Controls
import win32more.UI.Controls.RichEdit
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
WM_CONTEXTMENU = 123
WM_UNICHAR = 265
WM_PRINTCLIENT = 792
EM_CANPASTE = 1074
EM_DISPLAYBAND = 1075
EM_EXGETSEL = 1076
EM_EXLIMITTEXT = 1077
EM_EXLINEFROMCHAR = 1078
EM_EXSETSEL = 1079
EM_FINDTEXT = 1080
EM_FORMATRANGE = 1081
EM_GETCHARFORMAT = 1082
EM_GETEVENTMASK = 1083
EM_GETOLEINTERFACE = 1084
EM_GETPARAFORMAT = 1085
EM_GETSELTEXT = 1086
EM_HIDESELECTION = 1087
EM_PASTESPECIAL = 1088
EM_REQUESTRESIZE = 1089
EM_SELECTIONTYPE = 1090
EM_SETBKGNDCOLOR = 1091
EM_SETCHARFORMAT = 1092
EM_SETEVENTMASK = 1093
EM_SETOLECALLBACK = 1094
EM_SETPARAFORMAT = 1095
EM_SETTARGETDEVICE = 1096
EM_STREAMIN = 1097
EM_STREAMOUT = 1098
EM_GETTEXTRANGE = 1099
EM_FINDWORDBREAK = 1100
EM_SETOPTIONS = 1101
EM_GETOPTIONS = 1102
EM_FINDTEXTEX = 1103
EM_GETWORDBREAKPROCEX = 1104
EM_SETWORDBREAKPROCEX = 1105
EM_SETUNDOLIMIT = 1106
EM_REDO = 1108
EM_CANREDO = 1109
EM_GETUNDONAME = 1110
EM_GETREDONAME = 1111
EM_STOPGROUPTYPING = 1112
EM_SETTEXTMODE = 1113
EM_GETTEXTMODE = 1114
EM_AUTOURLDETECT = 1115
AURL_ENABLEURL = 1
AURL_ENABLEEMAILADDR = 2
AURL_ENABLETELNO = 4
AURL_ENABLEEAURLS = 8
AURL_ENABLEDRIVELETTERS = 16
AURL_DISABLEMIXEDLGC = 32
EM_GETAUTOURLDETECT = 1116
EM_SETPALETTE = 1117
EM_GETTEXTEX = 1118
EM_GETTEXTLENGTHEX = 1119
EM_SHOWSCROLLBAR = 1120
EM_SETTEXTEX = 1121
EM_SETPUNCTUATION = 1124
EM_GETPUNCTUATION = 1125
EM_SETWORDWRAPMODE = 1126
EM_GETWORDWRAPMODE = 1127
EM_SETIMECOLOR = 1128
EM_GETIMECOLOR = 1129
EM_SETIMEOPTIONS = 1130
EM_GETIMEOPTIONS = 1131
EM_CONVPOSITION = 1132
EM_SETLANGOPTIONS = 1144
EM_GETLANGOPTIONS = 1145
EM_GETIMECOMPMODE = 1146
EM_FINDTEXTW = 1147
EM_FINDTEXTEXW = 1148
EM_RECONVERSION = 1149
EM_SETIMEMODEBIAS = 1150
EM_GETIMEMODEBIAS = 1151
EM_SETBIDIOPTIONS = 1224
EM_GETBIDIOPTIONS = 1225
EM_SETTYPOGRAPHYOPTIONS = 1226
EM_GETTYPOGRAPHYOPTIONS = 1227
EM_SETEDITSTYLE = 1228
EM_GETEDITSTYLE = 1229
SES_EMULATESYSEDIT = 1
SES_BEEPONMAXTEXT = 2
SES_EXTENDBACKCOLOR = 4
SES_MAPCPS = 8
SES_HYPERLINKTOOLTIPS = 8
SES_EMULATE10 = 16
SES_DEFAULTLATINLIGA = 16
SES_USECRLF = 32
SES_NOFOCUSLINKNOTIFY = 32
SES_USEAIMM = 64
SES_NOIME = 128
SES_ALLOWBEEPS = 256
SES_UPPERCASE = 512
SES_LOWERCASE = 1024
SES_NOINPUTSEQUENCECHK = 2048
SES_BIDI = 4096
SES_SCROLLONKILLFOCUS = 8192
SES_XLTCRCRLFTOCR = 16384
SES_DRAFTMODE = 32768
SES_USECTF = 65536
SES_HIDEGRIDLINES = 131072
SES_USEATFONT = 262144
SES_CUSTOMLOOK = 524288
SES_LBSCROLLNOTIFY = 1048576
SES_CTFALLOWEMBED = 2097152
SES_CTFALLOWSMARTTAG = 4194304
SES_CTFALLOWPROOFING = 8388608
SES_LOGICALCARET = 16777216
SES_WORDDRAGDROP = 33554432
SES_SMARTDRAGDROP = 67108864
SES_MULTISELECT = 134217728
SES_CTFNOLOCK = 268435456
SES_NOEALINEHEIGHTADJUST = 536870912
SES_MAX = 536870912
IMF_AUTOKEYBOARD = 1
IMF_AUTOFONT = 2
IMF_IMECANCELCOMPLETE = 4
IMF_IMEALWAYSSENDNOTIFY = 8
IMF_AUTOFONTSIZEADJUST = 16
IMF_UIFONTS = 32
IMF_NOIMPLICITLANG = 64
IMF_DUALFONT = 128
IMF_NOKBDLIDFIXUP = 512
IMF_NORTFFONTSUBSTITUTE = 1024
IMF_SPELLCHECKING = 2048
IMF_TKBPREDICTION = 4096
IMF_IMEUIINTEGRATION = 8192
ICM_NOTOPEN = 0
ICM_LEVEL3 = 1
ICM_LEVEL2 = 2
ICM_LEVEL2_5 = 3
ICM_LEVEL2_SUI = 4
ICM_CTF = 5
TO_ADVANCEDTYPOGRAPHY = 1
TO_SIMPLELINEBREAK = 2
TO_DISABLECUSTOMTEXTOUT = 4
TO_ADVANCEDLAYOUT = 8
EM_OUTLINE = 1244
EM_GETSCROLLPOS = 1245
EM_SETSCROLLPOS = 1246
EM_SETFONTSIZE = 1247
EM_GETZOOM = 1248
EM_SETZOOM = 1249
EM_GETVIEWKIND = 1250
EM_SETVIEWKIND = 1251
EM_GETPAGE = 1252
EM_SETPAGE = 1253
EM_GETHYPHENATEINFO = 1254
EM_SETHYPHENATEINFO = 1255
EM_GETPAGEROTATE = 1259
EM_SETPAGEROTATE = 1260
EM_GETCTFMODEBIAS = 1261
EM_SETCTFMODEBIAS = 1262
EM_GETCTFOPENSTATUS = 1264
EM_SETCTFOPENSTATUS = 1265
EM_GETIMECOMPTEXT = 1266
EM_ISIME = 1267
EM_GETIMEPROPERTY = 1268
EM_GETQUERYRTFOBJ = 1293
EM_SETQUERYRTFOBJ = 1294
EPR_0 = 0
EPR_270 = 1
EPR_180 = 2
EPR_90 = 3
EPR_SE = 5
CTFMODEBIAS_DEFAULT = 0
CTFMODEBIAS_FILENAME = 1
CTFMODEBIAS_NAME = 2
CTFMODEBIAS_READING = 3
CTFMODEBIAS_DATETIME = 4
CTFMODEBIAS_CONVERSATION = 5
CTFMODEBIAS_NUMERIC = 6
CTFMODEBIAS_HIRAGANA = 7
CTFMODEBIAS_KATAKANA = 8
CTFMODEBIAS_HANGUL = 9
CTFMODEBIAS_HALFWIDTHKATAKANA = 10
CTFMODEBIAS_FULLWIDTHALPHANUMERIC = 11
CTFMODEBIAS_HALFWIDTHALPHANUMERIC = 12
IMF_SMODE_PLAURALCLAUSE = 1
IMF_SMODE_NONE = 2
EMO_EXIT = 0
EMO_ENTER = 1
EMO_PROMOTE = 2
EMO_EXPAND = 3
EMO_MOVESELECTION = 4
EMO_GETVIEWMODE = 5
EMO_EXPANDSELECTION = 0
EMO_EXPANDDOCUMENT = 1
VM_NORMAL = 4
VM_OUTLINE = 2
VM_PAGE = 9
EM_INSERTTABLE = 1256
EM_GETAUTOCORRECTPROC = 1257
EM_SETAUTOCORRECTPROC = 1258
EM_CALLAUTOCORRECTPROC = 1279
ATP_NOCHANGE = 0
ATP_CHANGE = 1
ATP_NODELIMITER = 2
ATP_REPLACEALLTEXT = 4
EM_GETTABLEPARMS = 1289
EM_SETEDITSTYLEEX = 1299
EM_GETEDITSTYLEEX = 1300
SES_EX_NOTABLE = 4
SES_EX_NOMATH = 64
SES_EX_HANDLEFRIENDLYURL = 256
SES_EX_NOTHEMING = 524288
SES_EX_NOACETATESELECTION = 1048576
SES_EX_USESINGLELINE = 2097152
SES_EX_MULTITOUCH = 134217728
SES_EX_HIDETEMPFORMAT = 268435456
SES_EX_USEMOUSEWPARAM = 536870912
EM_GETSTORYTYPE = 1314
EM_SETSTORYTYPE = 1315
EM_GETELLIPSISMODE = 1329
EM_SETELLIPSISMODE = 1330
ELLIPSIS_MASK = 3
ELLIPSIS_NONE = 0
ELLIPSIS_END = 1
ELLIPSIS_WORD = 3
EM_SETTABLEPARMS = 1331
EM_GETTOUCHOPTIONS = 1334
EM_SETTOUCHOPTIONS = 1335
EM_INSERTIMAGE = 1338
EM_SETUIANAME = 1344
EM_GETELLIPSISSTATE = 1346
RTO_SHOWHANDLES = 1
RTO_DISABLEHANDLES = 2
RTO_READINGMODE = 3
EN_MSGFILTER = 1792
EN_REQUESTRESIZE = 1793
EN_SELCHANGE = 1794
EN_DROPFILES = 1795
EN_PROTECTED = 1796
EN_CORRECTTEXT = 1797
EN_STOPNOUNDO = 1798
EN_IMECHANGE = 1799
EN_SAVECLIPBOARD = 1800
EN_OLEOPFAILED = 1801
EN_OBJECTPOSITIONS = 1802
EN_LINK = 1803
EN_DRAGDROPDONE = 1804
EN_PARAGRAPHEXPANDED = 1805
EN_PAGECHANGE = 1806
EN_LOWFIRTF = 1807
EN_ALIGNLTR = 1808
EN_ALIGNRTL = 1809
EN_CLIPFORMAT = 1810
EN_STARTCOMPOSITION = 1811
EN_ENDCOMPOSITION = 1812
ENM_NONE = 0
ENM_CHANGE = 1
ENM_UPDATE = 2
ENM_SCROLL = 4
ENM_SCROLLEVENTS = 8
ENM_DRAGDROPDONE = 16
ENM_PARAGRAPHEXPANDED = 32
ENM_PAGECHANGE = 64
ENM_CLIPFORMAT = 128
ENM_KEYEVENTS = 65536
ENM_MOUSEEVENTS = 131072
ENM_REQUESTRESIZE = 262144
ENM_SELCHANGE = 524288
ENM_DROPFILES = 1048576
ENM_PROTECTED = 2097152
ENM_CORRECTTEXT = 4194304
ENM_IMECHANGE = 8388608
ENM_LANGCHANGE = 16777216
ENM_OBJECTPOSITIONS = 33554432
ENM_LINK = 67108864
ENM_LOWFIRTF = 134217728
ENM_STARTCOMPOSITION = 268435456
ENM_ENDCOMPOSITION = 536870912
ENM_GROUPTYPINGCHANGE = 1073741824
ENM_HIDELINKTOOLTIP = 2147483648
ES_SAVESEL = 32768
ES_SUNKEN = 16384
ES_DISABLENOSCROLL = 8192
ES_SELECTIONBAR = 16777216
ES_NOOLEDRAGDROP = 8
ES_EX_NOCALLOLEINIT = 0
ES_VERTICAL = 4194304
ES_NOIME = 524288
ES_SELFIME = 262144
ECO_AUTOWORDSELECTION = 1
ECO_AUTOVSCROLL = 64
ECO_AUTOHSCROLL = 128
ECO_NOHIDESEL = 256
ECO_READONLY = 2048
ECO_WANTRETURN = 4096
ECO_SAVESEL = 32768
ECO_SELECTIONBAR = 16777216
ECO_VERTICAL = 4194304
ECOOP_SET = 1
ECOOP_OR = 2
ECOOP_AND = 3
ECOOP_XOR = 4
WB_MOVEWORDPREV = 4
WB_MOVEWORDNEXT = 5
WB_PREVBREAK = 6
WB_NEXTBREAK = 7
PC_FOLLOWING = 1
PC_LEADING = 2
PC_OVERFLOW = 3
PC_DELIMITER = 4
WBF_WORDWRAP = 16
WBF_WORDBREAK = 32
WBF_OVERFLOW = 64
WBF_LEVEL1 = 128
WBF_LEVEL2 = 256
WBF_CUSTOM = 512
IMF_FORCENONE = 1
IMF_FORCEENABLE = 2
IMF_FORCEDISABLE = 4
IMF_CLOSESTATUSWINDOW = 8
IMF_VERTICAL = 32
IMF_FORCEACTIVE = 64
IMF_FORCEINACTIVE = 128
IMF_FORCEREMEMBER = 256
IMF_MULTIPLEEDIT = 1024
SCF_SELECTION = 1
SCF_WORD = 2
SCF_DEFAULT = 0
SCF_ALL = 4
SCF_USEUIRULES = 8
SCF_ASSOCIATEFONT = 16
SCF_NOKBUPDATE = 32
SCF_ASSOCIATEFONT2 = 64
SCF_SMARTFONT = 128
SCF_CHARREPFROMLCID = 256
SPF_DONTSETDEFAULT = 2
SPF_SETDEFAULT = 4
SF_TEXT = 1
SF_RTF = 2
SF_RTFNOOBJS = 3
SF_TEXTIZED = 4
SF_UNICODE = 16
SF_USECODEPAGE = 32
SF_NCRFORNONASCII = 64
SFF_WRITEXTRAPAR = 128
SFF_SELECTION = 32768
SFF_PLAINRTF = 16384
SFF_PERSISTVIEWSCALE = 8192
SFF_KEEPDOCINFO = 4096
SFF_PWD = 2048
SF_RTFVAL = 1792
MAX_TAB_STOPS = 32
MAX_TABLE_CELLS = 63
PFM_SPACEBEFORE = 64
PFM_SPACEAFTER = 128
PFM_LINESPACING = 256
PFM_STYLE = 1024
PFM_BORDER = 2048
PFM_SHADING = 4096
PFM_NUMBERINGSTYLE = 8192
PFM_NUMBERINGTAB = 16384
PFM_NUMBERINGSTART = 32768
PFM_KEEP = 131072
PFM_KEEPNEXT = 262144
PFM_PAGEBREAKBEFORE = 524288
PFM_NOLINENUMBER = 1048576
PFM_NOWIDOWCONTROL = 2097152
PFM_DONOTHYPHEN = 4194304
PFM_SIDEBYSIDE = 8388608
PFM_COLLAPSED = 16777216
PFM_OUTLINELEVEL = 33554432
PFM_BOX = 67108864
PFM_RESERVED2 = 134217728
PFM_TABLEROWDELIMITER = 268435456
PFM_TEXTWRAPPINGBREAK = 536870912
PFM_TABLE = 1073741824
PFN_BULLET = 1
PFN_ARABIC = 2
PFN_LCLETTER = 3
PFN_UCLETTER = 4
PFN_LCROMAN = 5
PFN_UCROMAN = 6
PFA_JUSTIFY = 4
PFA_FULL_INTERWORD = 4
WM_NOTIFY = 78
GCMF_GRIPPER = 1
GCMF_SPELLING = 2
GCMF_TOUCHMENU = 16384
GCMF_MOUSEMENU = 8192
OLEOP_DOVERB = 1
ST_DEFAULT = 0
ST_KEEPUNDO = 1
ST_SELECTION = 2
ST_NEWCHARS = 4
ST_UNICODE = 8
BOM_DEFPARADIR = 1
BOM_PLAINTEXT = 2
BOM_NEUTRALOVERRIDE = 4
BOM_CONTEXTREADING = 8
BOM_CONTEXTALIGNMENT = 16
BOM_LEGACYBIDICLASS = 64
BOM_UNICODEBIDI = 128
BOE_RTLDIR = 1
BOE_PLAINTEXT = 2
BOE_NEUTRALOVERRIDE = 4
BOE_CONTEXTREADING = 8
BOE_CONTEXTALIGNMENT = 16
BOE_FORCERECALC = 32
BOE_LEGACYBIDICLASS = 64
BOE_UNICODEBIDI = 128
FR_MATCHDIAC = 536870912
FR_MATCHKASHIDA = 1073741824
FR_MATCHALEFHAMZA = 2147483648
PFA_FULL_NEWSPAPER = 5
PFA_FULL_INTERLETTER = 6
PFA_FULL_SCALED = 7
PFA_FULL_GLYPHS = 8
AURL_ENABLEEA = 1
GCM_TOUCHMENU = 16384
GCM_MOUSEMENU = 8192
S_MSG_KEY_IGNORED = 262657
TXTBIT_RICHTEXT = 1
TXTBIT_MULTILINE = 2
TXTBIT_READONLY = 4
TXTBIT_SHOWACCELERATOR = 8
TXTBIT_USEPASSWORD = 16
TXTBIT_HIDESELECTION = 32
TXTBIT_SAVESELECTION = 64
TXTBIT_AUTOWORDSEL = 128
TXTBIT_VERTICAL = 256
TXTBIT_SELBARCHANGE = 512
TXTBIT_WORDWRAP = 1024
TXTBIT_ALLOWBEEP = 2048
TXTBIT_DISABLEDRAG = 4096
TXTBIT_VIEWINSETCHANGE = 8192
TXTBIT_BACKSTYLECHANGE = 16384
TXTBIT_MAXLENGTHCHANGE = 32768
TXTBIT_SCROLLBARCHANGE = 65536
TXTBIT_CHARFORMATCHANGE = 131072
TXTBIT_PARAFORMATCHANGE = 262144
TXTBIT_EXTENTCHANGE = 524288
TXTBIT_CLIENTRECTCHANGE = 1048576
TXTBIT_USECURRENTBKG = 2097152
TXTBIT_NOTHREADREFCOUNT = 4194304
TXTBIT_SHOWPASSWORD = 8388608
TXTBIT_D2DDWRITE = 16777216
TXTBIT_D2DSIMPLETYPOGRAPHY = 33554432
TXTBIT_D2DPIXELSNAPPED = 67108864
TXTBIT_D2DSUBPIXELLINES = 134217728
TXTBIT_FLASHLASTPASSWORDCHAR = 268435456
TXTBIT_ADVANCEDINPUT = 536870912
TXES_ISDIALOG = 1
REO_NULL = 0
REO_READWRITEMASK = 2047
RECO_PASTE = 0
RECO_DROP = 1
RECO_COPY = 2
RECO_CUT = 3
RECO_DRAG = 4
CFM_MASK = UInt32
CFM_SUBSCRIPT = 196608
CFM_SUPERSCRIPT = 196608
CFM_EFFECTS = 1073741887
CFM_ALL = 4160749631
CFM_BOLD = 1
CFM_CHARSET = 134217728
CFM_COLOR = 1073741824
CFM_FACE = 536870912
CFM_ITALIC = 2
CFM_OFFSET = 268435456
CFM_PROTECTED = 16
CFM_SIZE = 2147483648
CFM_STRIKEOUT = 8
CFM_UNDERLINE = 4
CFM_LINK = 32
CFM_SMALLCAPS = 64
CFM_ALLCAPS = 128
CFM_HIDDEN = 256
CFM_OUTLINE = 512
CFM_SHADOW = 1024
CFM_EMBOSS = 2048
CFM_IMPRINT = 4096
CFM_DISABLED = 8192
CFM_REVISED = 16384
CFM_REVAUTHOR = 32768
CFM_ANIMATION = 262144
CFM_STYLE = 524288
CFM_KERNING = 1048576
CFM_SPACING = 2097152
CFM_WEIGHT = 4194304
CFM_UNDERLINETYPE = 8388608
CFM_COOKIE = 16777216
CFM_LCID = 33554432
CFM_BACKCOLOR = 67108864
CFM_EFFECTS2 = 1141080063
CFM_ALL2 = 4294967295
CFM_FONTBOUND = 1048576
CFM_LINKPROTECTED = 8388608
CFM_EXTENDED = 33554432
CFM_MATHNOBUILDUP = 134217728
CFM_MATH = 268435456
CFM_MATHORDINARY = 536870912
CFM_ALLEFFECTS = 2115207167
CFE_EFFECTS = UInt32
CFE_ALLCAPS = 128
CFE_AUTOBACKCOLOR = 67108864
CFE_DISABLED = 8192
CFE_EMBOSS = 2048
CFE_HIDDEN = 256
CFE_IMPRINT = 4096
CFE_OUTLINE = 512
CFE_REVISED = 16384
CFE_SHADOW = 1024
CFE_SMALLCAPS = 64
CFE_AUTOCOLOR = 1073741824
CFE_BOLD = 1
CFE_ITALIC = 2
CFE_STRIKEOUT = 8
CFE_UNDERLINE = 4
CFE_PROTECTED = 16
CFE_LINK = 32
CFE_SUBSCRIPT = 65536
CFE_SUPERSCRIPT = 131072
CFE_FONTBOUND = 1048576
CFE_LINKPROTECTED = 8388608
CFE_EXTENDED = 33554432
CFE_MATHNOBUILDUP = 134217728
CFE_MATH = 268435456
CFE_MATHORDINARY = 536870912
PARAFORMAT_MASK = UInt32
PFM_ALIGNMENT = 8
PFM_NUMBERING = 32
PFM_OFFSET = 4
PFM_OFFSETINDENT = 2147483648
PFM_RIGHTINDENT = 2
PFM_RTLPARA = 65536
PFM_STARTINDENT = 1
PFM_TABSTOPS = 16
RICH_EDIT_GET_CONTEXT_MENU_SEL_TYPE = UInt16
SEL_EMPTY = 0
SEL_TEXT = 1
SEL_OBJECT = 2
SEL_MULTICHAR = 4
SEL_MULTIOBJECT = 8
GCM_RIGHTMOUSEDROP = 32768
RICH_EDIT_GET_OBJECT_FLAGS = UInt32
REO_GETOBJ_POLEOBJ = 1
REO_GETOBJ_PSTG = 2
REO_GETOBJ_POLESITE = 4
REO_GETOBJ_NO_INTERFACES = 0
REO_GETOBJ_ALL_INTERFACES = 7
PARAFORMAT_BORDERS = UInt16
PARAFORMAT_BORDERS_LEFT = 1
PARAFORMAT_BORDERS_RIGHT = 2
PARAFORMAT_BORDERS_TOP = 4
PARAFORMAT_BORDERS_BOTTOM = 8
PARAFORMAT_BORDERS_INSIDE = 16
PARAFORMAT_BORDERS_OUTSIDE = 32
PARAFORMAT_BORDERS_AUTOCOLOR = 64
PARAFORMAT_SHADING_STYLE = UInt16
PARAFORMAT_SHADING_STYLE_NONE = 0
PARAFORMAT_SHADING_STYLE_DARK_HORIZ = 1
PARAFORMAT_SHADING_STYLE_DARK_VERT = 2
PARAFORMAT_SHADING_STYLE_DARK_DOWN_DIAG = 3
PARAFORMAT_SHADING_STYLE_DARK_UP_DIAG = 4
PARAFORMAT_SHADING_STYLE_DARK_GRID = 5
PARAFORMAT_SHADING_STYLE_DARK_TRELLIS = 6
PARAFORMAT_SHADING_STYLE_LIGHT_HORZ = 7
PARAFORMAT_SHADING_STYLE_LIGHT_VERT = 8
PARAFORMAT_SHADING_STYLE_LIGHT_DOWN_DIAG = 9
PARAFORMAT_SHADING_STYLE_LIGHT_UP_DIAG = 10
PARAFORMAT_SHADING_STYLE_LIGHT_GRID = 11
PARAFORMAT_SHADING_STYLE_LIGHT_TRELLIS = 12
GETTEXTEX_FLAGS = UInt32
GT_DEFAULT = 0
GT_NOHIDDENTEXT = 8
GT_RAWTEXT = 4
GT_SELECTION = 2
GT_USECRLF = 1
ENDCOMPOSITIONNOTIFY_CODE = UInt32
ECN_ENDCOMPOSITION = 1
ECN_NEWTEXT = 2
IMECOMPTEXT_FLAGS = UInt32
ICT_RESULTREADSTR = 1
GETTEXTLENGTHEX_FLAGS = UInt32
GTL_DEFAULT = 0
GTL_USECRLF = 1
GTL_PRECISE = 2
GTL_CLOSE = 4
GTL_NUMCHARS = 8
GTL_NUMBYTES = 16
REOBJECT_FLAGS = UInt32
REO_ALIGNTORIGHT = 256
REO_BELOWBASELINE = 2
REO_BLANK = 16
REO_CANROTATE = 128
REO_DONTNEEDPALETTE = 32
REO_DYNAMICSIZE = 8
REO_GETMETAFILE = 4194304
REO_HILITED = 16777216
REO_INPLACEACTIVE = 33554432
REO_INVERTEDSELECT = 4
REO_LINK = 2147483648
REO_LINKAVAILABLE = 8388608
REO_OPEN = 67108864
REO_OWNERDRAWSELECT = 64
REO_RESIZABLE = 1
REO_SELECTED = 134217728
REO_STATIC = 1073741824
REO_USEASBACKGROUND = 1024
REO_WRAPTEXTAROUND = 512
PARAFORMAT_NUMBERING_STYLE = UInt16
PFNS_PAREN = 0
PFNS_PARENS = 256
PFNS_PERIOD = 512
PFNS_PLAIN = 768
PFNS_NONUMBER = 1024
PFNS_NEWNUMBER = 32768
PARAFORMAT_ALIGNMENT = UInt16
PFA_CENTER = 3
PFA_LEFT = 1
PFA_RIGHT = 2
TEXTMODE = Int32
TM_PLAINTEXT = 1
TM_RICHTEXT = 2
TM_SINGLELEVELUNDO = 4
TM_MULTILEVELUNDO = 8
TM_SINGLECODEPAGE = 16
TM_MULTICODEPAGE = 32
def _define_IMECOMPTEXT_head():
    class IMECOMPTEXT(Structure):
        pass
    return IMECOMPTEXT
def _define_IMECOMPTEXT():
    IMECOMPTEXT = win32more.UI.Controls.RichEdit.IMECOMPTEXT_head
    IMECOMPTEXT._fields_ = [
        ("cb", Int32),
        ("flags", win32more.UI.Controls.RichEdit.IMECOMPTEXT_FLAGS),
    ]
    return IMECOMPTEXT
def _define_TABLEROWPARMS_head():
    class TABLEROWPARMS(Structure):
        pass
    return TABLEROWPARMS
def _define_TABLEROWPARMS():
    TABLEROWPARMS = win32more.UI.Controls.RichEdit.TABLEROWPARMS_head
    TABLEROWPARMS._fields_ = [
        ("cbRow", Byte),
        ("cbCell", Byte),
        ("cCell", Byte),
        ("cRow", Byte),
        ("dxCellMargin", Int32),
        ("dxIndent", Int32),
        ("dyHeight", Int32),
        ("_bitfield", UInt32),
        ("cpStartRow", Int32),
        ("bTableLevel", Byte),
        ("iCell", Byte),
    ]
    return TABLEROWPARMS
def _define_TABLECELLPARMS_head():
    class TABLECELLPARMS(Structure):
        pass
    return TABLECELLPARMS
def _define_TABLECELLPARMS():
    TABLECELLPARMS = win32more.UI.Controls.RichEdit.TABLECELLPARMS_head
    TABLECELLPARMS._fields_ = [
        ("dxWidth", Int32),
        ("_bitfield", UInt16),
        ("wShading", UInt16),
        ("dxBrdrLeft", Int16),
        ("dyBrdrTop", Int16),
        ("dxBrdrRight", Int16),
        ("dyBrdrBottom", Int16),
        ("crBrdrLeft", UInt32),
        ("crBrdrTop", UInt32),
        ("crBrdrRight", UInt32),
        ("crBrdrBottom", UInt32),
        ("crBackPat", UInt32),
        ("crForePat", UInt32),
    ]
    return TABLECELLPARMS
def _define_AutoCorrectProc():
    return CFUNCTYPE(Int32,UInt16,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Int32,POINTER(Int32), use_last_error=False)
def _define_RICHEDIT_IMAGE_PARAMETERS_head():
    class RICHEDIT_IMAGE_PARAMETERS(Structure):
        pass
    return RICHEDIT_IMAGE_PARAMETERS
def _define_RICHEDIT_IMAGE_PARAMETERS():
    RICHEDIT_IMAGE_PARAMETERS = win32more.UI.Controls.RichEdit.RICHEDIT_IMAGE_PARAMETERS_head
    RICHEDIT_IMAGE_PARAMETERS._pack_ = 4
    RICHEDIT_IMAGE_PARAMETERS._fields_ = [
        ("xWidth", Int32),
        ("yHeight", Int32),
        ("Ascent", Int32),
        ("Type", win32more.Graphics.Gdi.TEXT_ALIGN_OPTIONS),
        ("pwszAlternateText", win32more.Foundation.PWSTR),
        ("pIStream", win32more.System.Com.IStream_head),
    ]
    return RICHEDIT_IMAGE_PARAMETERS
def _define_ENDCOMPOSITIONNOTIFY_head():
    class ENDCOMPOSITIONNOTIFY(Structure):
        pass
    return ENDCOMPOSITIONNOTIFY
def _define_ENDCOMPOSITIONNOTIFY():
    ENDCOMPOSITIONNOTIFY = win32more.UI.Controls.RichEdit.ENDCOMPOSITIONNOTIFY_head
    ENDCOMPOSITIONNOTIFY._pack_ = 4
    ENDCOMPOSITIONNOTIFY._fields_ = [
        ("nmhdr", win32more.UI.Controls.NMHDR),
        ("dwCode", win32more.UI.Controls.RichEdit.ENDCOMPOSITIONNOTIFY_CODE),
    ]
    return ENDCOMPOSITIONNOTIFY
def _define_EDITWORDBREAKPROCEX():
    return CFUNCTYPE(Int32,win32more.Foundation.PSTR,Int32,Byte,Int32, use_last_error=False)
def _define_CHARFORMATA_head():
    class CHARFORMATA(Structure):
        pass
    return CHARFORMATA
def _define_CHARFORMATA():
    CHARFORMATA = win32more.UI.Controls.RichEdit.CHARFORMATA_head
    CHARFORMATA._fields_ = [
        ("cbSize", UInt32),
        ("dwMask", win32more.UI.Controls.RichEdit.CFM_MASK),
        ("dwEffects", win32more.UI.Controls.RichEdit.CFE_EFFECTS),
        ("yHeight", Int32),
        ("yOffset", Int32),
        ("crTextColor", UInt32),
        ("bCharSet", Byte),
        ("bPitchAndFamily", Byte),
        ("szFaceName", win32more.Foundation.CHAR * 32),
    ]
    return CHARFORMATA
def _define_CHARFORMATW_head():
    class CHARFORMATW(Structure):
        pass
    return CHARFORMATW
def _define_CHARFORMATW():
    CHARFORMATW = win32more.UI.Controls.RichEdit.CHARFORMATW_head
    CHARFORMATW._fields_ = [
        ("cbSize", UInt32),
        ("dwMask", win32more.UI.Controls.RichEdit.CFM_MASK),
        ("dwEffects", win32more.UI.Controls.RichEdit.CFE_EFFECTS),
        ("yHeight", Int32),
        ("yOffset", Int32),
        ("crTextColor", UInt32),
        ("bCharSet", Byte),
        ("bPitchAndFamily", Byte),
        ("szFaceName", Char * 32),
    ]
    return CHARFORMATW
def _define_CHARFORMAT2W_head():
    class CHARFORMAT2W(Structure):
        pass
    return CHARFORMAT2W
def _define_CHARFORMAT2W():
    CHARFORMAT2W = win32more.UI.Controls.RichEdit.CHARFORMAT2W_head
    class CHARFORMAT2W__Anonymous_e__Union(Union):
        pass
    CHARFORMAT2W__Anonymous_e__Union._fields_ = [
        ("dwReserved", UInt32),
        ("dwCookie", UInt32),
    ]
    CHARFORMAT2W._anonymous_ = [
        'Anonymous',
    ]
    CHARFORMAT2W._fields_ = [
        ("__AnonymousBase_richedit_L711_C23", win32more.UI.Controls.RichEdit.CHARFORMATW),
        ("wWeight", UInt16),
        ("sSpacing", Int16),
        ("crBackColor", UInt32),
        ("lcid", UInt32),
        ("Anonymous", CHARFORMAT2W__Anonymous_e__Union),
        ("sStyle", Int16),
        ("wKerning", UInt16),
        ("bUnderlineType", Byte),
        ("bAnimation", Byte),
        ("bRevAuthor", Byte),
        ("bUnderlineColor", Byte),
    ]
    return CHARFORMAT2W
def _define_CHARFORMAT2A_head():
    class CHARFORMAT2A(Structure):
        pass
    return CHARFORMAT2A
def _define_CHARFORMAT2A():
    CHARFORMAT2A = win32more.UI.Controls.RichEdit.CHARFORMAT2A_head
    class CHARFORMAT2A__Anonymous_e__Union(Union):
        pass
    CHARFORMAT2A__Anonymous_e__Union._fields_ = [
        ("dwReserved", UInt32),
        ("dwCookie", UInt32),
    ]
    CHARFORMAT2A._anonymous_ = [
        'Anonymous',
    ]
    CHARFORMAT2A._fields_ = [
        ("__AnonymousBase_richedit_L736_C23", win32more.UI.Controls.RichEdit.CHARFORMATA),
        ("wWeight", UInt16),
        ("sSpacing", Int16),
        ("crBackColor", UInt32),
        ("lcid", UInt32),
        ("Anonymous", CHARFORMAT2A__Anonymous_e__Union),
        ("sStyle", Int16),
        ("wKerning", UInt16),
        ("bUnderlineType", Byte),
        ("bAnimation", Byte),
        ("bRevAuthor", Byte),
        ("bUnderlineColor", Byte),
    ]
    return CHARFORMAT2A
def _define_CHARRANGE_head():
    class CHARRANGE(Structure):
        pass
    return CHARRANGE
def _define_CHARRANGE():
    CHARRANGE = win32more.UI.Controls.RichEdit.CHARRANGE_head
    CHARRANGE._fields_ = [
        ("cpMin", Int32),
        ("cpMax", Int32),
    ]
    return CHARRANGE
def _define_TEXTRANGEA_head():
    class TEXTRANGEA(Structure):
        pass
    return TEXTRANGEA
def _define_TEXTRANGEA():
    TEXTRANGEA = win32more.UI.Controls.RichEdit.TEXTRANGEA_head
    TEXTRANGEA._pack_ = 4
    TEXTRANGEA._fields_ = [
        ("chrg", win32more.UI.Controls.RichEdit.CHARRANGE),
        ("lpstrText", win32more.Foundation.PSTR),
    ]
    return TEXTRANGEA
def _define_TEXTRANGEW_head():
    class TEXTRANGEW(Structure):
        pass
    return TEXTRANGEW
def _define_TEXTRANGEW():
    TEXTRANGEW = win32more.UI.Controls.RichEdit.TEXTRANGEW_head
    TEXTRANGEW._pack_ = 4
    TEXTRANGEW._fields_ = [
        ("chrg", win32more.UI.Controls.RichEdit.CHARRANGE),
        ("lpstrText", win32more.Foundation.PWSTR),
    ]
    return TEXTRANGEW
def _define_EDITSTREAMCALLBACK():
    return CFUNCTYPE(UInt32,UIntPtr,c_char_p_no,Int32,POINTER(Int32), use_last_error=False)
def _define_EDITSTREAM_head():
    class EDITSTREAM(Structure):
        pass
    return EDITSTREAM
def _define_EDITSTREAM():
    EDITSTREAM = win32more.UI.Controls.RichEdit.EDITSTREAM_head
    EDITSTREAM._pack_ = 4
    EDITSTREAM._fields_ = [
        ("dwCookie", UIntPtr),
        ("dwError", UInt32),
        ("pfnCallback", win32more.UI.Controls.RichEdit.EDITSTREAMCALLBACK),
    ]
    return EDITSTREAM
def _define_FINDTEXTA_head():
    class FINDTEXTA(Structure):
        pass
    return FINDTEXTA
def _define_FINDTEXTA():
    FINDTEXTA = win32more.UI.Controls.RichEdit.FINDTEXTA_head
    FINDTEXTA._pack_ = 4
    FINDTEXTA._fields_ = [
        ("chrg", win32more.UI.Controls.RichEdit.CHARRANGE),
        ("lpstrText", win32more.Foundation.PSTR),
    ]
    return FINDTEXTA
def _define_FINDTEXTW_head():
    class FINDTEXTW(Structure):
        pass
    return FINDTEXTW
def _define_FINDTEXTW():
    FINDTEXTW = win32more.UI.Controls.RichEdit.FINDTEXTW_head
    FINDTEXTW._pack_ = 4
    FINDTEXTW._fields_ = [
        ("chrg", win32more.UI.Controls.RichEdit.CHARRANGE),
        ("lpstrText", win32more.Foundation.PWSTR),
    ]
    return FINDTEXTW
def _define_FINDTEXTEXA_head():
    class FINDTEXTEXA(Structure):
        pass
    return FINDTEXTEXA
def _define_FINDTEXTEXA():
    FINDTEXTEXA = win32more.UI.Controls.RichEdit.FINDTEXTEXA_head
    FINDTEXTEXA._pack_ = 4
    FINDTEXTEXA._fields_ = [
        ("chrg", win32more.UI.Controls.RichEdit.CHARRANGE),
        ("lpstrText", win32more.Foundation.PSTR),
        ("chrgText", win32more.UI.Controls.RichEdit.CHARRANGE),
    ]
    return FINDTEXTEXA
def _define_FINDTEXTEXW_head():
    class FINDTEXTEXW(Structure):
        pass
    return FINDTEXTEXW
def _define_FINDTEXTEXW():
    FINDTEXTEXW = win32more.UI.Controls.RichEdit.FINDTEXTEXW_head
    FINDTEXTEXW._pack_ = 4
    FINDTEXTEXW._fields_ = [
        ("chrg", win32more.UI.Controls.RichEdit.CHARRANGE),
        ("lpstrText", win32more.Foundation.PWSTR),
        ("chrgText", win32more.UI.Controls.RichEdit.CHARRANGE),
    ]
    return FINDTEXTEXW
def _define_FORMATRANGE_head():
    class FORMATRANGE(Structure):
        pass
    return FORMATRANGE
def _define_FORMATRANGE():
    FORMATRANGE = win32more.UI.Controls.RichEdit.FORMATRANGE_head
    FORMATRANGE._pack_ = 4
    FORMATRANGE._fields_ = [
        ("hdc", win32more.Graphics.Gdi.HDC),
        ("hdcTarget", win32more.Graphics.Gdi.HDC),
        ("rc", win32more.Foundation.RECT),
        ("rcPage", win32more.Foundation.RECT),
        ("chrg", win32more.UI.Controls.RichEdit.CHARRANGE),
    ]
    return FORMATRANGE
def _define_PARAFORMAT_head():
    class PARAFORMAT(Structure):
        pass
    return PARAFORMAT
def _define_PARAFORMAT():
    PARAFORMAT = win32more.UI.Controls.RichEdit.PARAFORMAT_head
    class PARAFORMAT__Anonymous_e__Union(Union):
        pass
    PARAFORMAT__Anonymous_e__Union._fields_ = [
        ("wReserved", UInt16),
        ("wEffects", UInt16),
    ]
    PARAFORMAT._anonymous_ = [
        'Anonymous',
    ]
    PARAFORMAT._fields_ = [
        ("cbSize", UInt32),
        ("dwMask", win32more.UI.Controls.RichEdit.PARAFORMAT_MASK),
        ("wNumbering", UInt16),
        ("Anonymous", PARAFORMAT__Anonymous_e__Union),
        ("dxStartIndent", Int32),
        ("dxRightIndent", Int32),
        ("dxOffset", Int32),
        ("wAlignment", win32more.UI.Controls.RichEdit.PARAFORMAT_ALIGNMENT),
        ("cTabCount", Int16),
        ("rgxTabs", UInt32 * 32),
    ]
    return PARAFORMAT
def _define_PARAFORMAT2_head():
    class PARAFORMAT2(Structure):
        pass
    return PARAFORMAT2
def _define_PARAFORMAT2():
    PARAFORMAT2 = win32more.UI.Controls.RichEdit.PARAFORMAT2_head
    PARAFORMAT2._fields_ = [
        ("__AnonymousBase_richedit_L1149_C22", win32more.UI.Controls.RichEdit.PARAFORMAT),
        ("dySpaceBefore", Int32),
        ("dySpaceAfter", Int32),
        ("dyLineSpacing", Int32),
        ("sStyle", Int16),
        ("bLineSpacingRule", Byte),
        ("bOutlineLevel", Byte),
        ("wShadingWeight", UInt16),
        ("wShadingStyle", win32more.UI.Controls.RichEdit.PARAFORMAT_SHADING_STYLE),
        ("wNumberingStart", UInt16),
        ("wNumberingStyle", win32more.UI.Controls.RichEdit.PARAFORMAT_NUMBERING_STYLE),
        ("wNumberingTab", UInt16),
        ("wBorderSpace", UInt16),
        ("wBorderWidth", UInt16),
        ("wBorders", win32more.UI.Controls.RichEdit.PARAFORMAT_BORDERS),
    ]
    return PARAFORMAT2
def _define_MSGFILTER_head():
    class MSGFILTER(Structure):
        pass
    return MSGFILTER
def _define_MSGFILTER():
    MSGFILTER = win32more.UI.Controls.RichEdit.MSGFILTER_head
    MSGFILTER._pack_ = 4
    MSGFILTER._fields_ = [
        ("nmhdr", win32more.UI.Controls.NMHDR),
        ("msg", UInt32),
        ("wParam", win32more.Foundation.WPARAM),
        ("lParam", win32more.Foundation.LPARAM),
    ]
    return MSGFILTER
def _define_REQRESIZE_head():
    class REQRESIZE(Structure):
        pass
    return REQRESIZE
def _define_REQRESIZE():
    REQRESIZE = win32more.UI.Controls.RichEdit.REQRESIZE_head
    REQRESIZE._pack_ = 4
    REQRESIZE._fields_ = [
        ("nmhdr", win32more.UI.Controls.NMHDR),
        ("rc", win32more.Foundation.RECT),
    ]
    return REQRESIZE
def _define_SELCHANGE_head():
    class SELCHANGE(Structure):
        pass
    return SELCHANGE
def _define_SELCHANGE():
    SELCHANGE = win32more.UI.Controls.RichEdit.SELCHANGE_head
    SELCHANGE._pack_ = 4
    SELCHANGE._fields_ = [
        ("nmhdr", win32more.UI.Controls.NMHDR),
        ("chrg", win32more.UI.Controls.RichEdit.CHARRANGE),
        ("seltyp", win32more.UI.Controls.RichEdit.RICH_EDIT_GET_CONTEXT_MENU_SEL_TYPE),
    ]
    return SELCHANGE
def _define__grouptypingchange_head():
    class _grouptypingchange(Structure):
        pass
    return _grouptypingchange
def _define__grouptypingchange():
    _grouptypingchange = win32more.UI.Controls.RichEdit._grouptypingchange_head
    _grouptypingchange._pack_ = 4
    _grouptypingchange._fields_ = [
        ("nmhdr", win32more.UI.Controls.NMHDR),
        ("fGroupTyping", win32more.Foundation.BOOL),
    ]
    return _grouptypingchange
def _define_CLIPBOARDFORMAT_head():
    class CLIPBOARDFORMAT(Structure):
        pass
    return CLIPBOARDFORMAT
def _define_CLIPBOARDFORMAT():
    CLIPBOARDFORMAT = win32more.UI.Controls.RichEdit.CLIPBOARDFORMAT_head
    CLIPBOARDFORMAT._pack_ = 4
    CLIPBOARDFORMAT._fields_ = [
        ("nmhdr", win32more.UI.Controls.NMHDR),
        ("cf", UInt16),
    ]
    return CLIPBOARDFORMAT
def _define_GETCONTEXTMENUEX_head():
    class GETCONTEXTMENUEX(Structure):
        pass
    return GETCONTEXTMENUEX
def _define_GETCONTEXTMENUEX():
    GETCONTEXTMENUEX = win32more.UI.Controls.RichEdit.GETCONTEXTMENUEX_head
    GETCONTEXTMENUEX._pack_ = 4
    GETCONTEXTMENUEX._fields_ = [
        ("chrg", win32more.UI.Controls.RichEdit.CHARRANGE),
        ("dwFlags", UInt32),
        ("pt", win32more.Foundation.POINT),
        ("pvReserved", c_void_p),
    ]
    return GETCONTEXTMENUEX
def _define_ENDROPFILES_head():
    class ENDROPFILES(Structure):
        pass
    return ENDROPFILES
def _define_ENDROPFILES():
    ENDROPFILES = win32more.UI.Controls.RichEdit.ENDROPFILES_head
    ENDROPFILES._pack_ = 4
    ENDROPFILES._fields_ = [
        ("nmhdr", win32more.UI.Controls.NMHDR),
        ("hDrop", win32more.Foundation.HANDLE),
        ("cp", Int32),
        ("fProtected", win32more.Foundation.BOOL),
    ]
    return ENDROPFILES
def _define_ENPROTECTED_head():
    class ENPROTECTED(Structure):
        pass
    return ENPROTECTED
def _define_ENPROTECTED():
    ENPROTECTED = win32more.UI.Controls.RichEdit.ENPROTECTED_head
    ENPROTECTED._pack_ = 4
    ENPROTECTED._fields_ = [
        ("nmhdr", win32more.UI.Controls.NMHDR),
        ("msg", UInt32),
        ("wParam", win32more.Foundation.WPARAM),
        ("lParam", win32more.Foundation.LPARAM),
        ("chrg", win32more.UI.Controls.RichEdit.CHARRANGE),
    ]
    return ENPROTECTED
def _define_ENSAVECLIPBOARD_head():
    class ENSAVECLIPBOARD(Structure):
        pass
    return ENSAVECLIPBOARD
def _define_ENSAVECLIPBOARD():
    ENSAVECLIPBOARD = win32more.UI.Controls.RichEdit.ENSAVECLIPBOARD_head
    ENSAVECLIPBOARD._pack_ = 4
    ENSAVECLIPBOARD._fields_ = [
        ("nmhdr", win32more.UI.Controls.NMHDR),
        ("cObjectCount", Int32),
        ("cch", Int32),
    ]
    return ENSAVECLIPBOARD
def _define_ENOLEOPFAILED_head():
    class ENOLEOPFAILED(Structure):
        pass
    return ENOLEOPFAILED
def _define_ENOLEOPFAILED():
    ENOLEOPFAILED = win32more.UI.Controls.RichEdit.ENOLEOPFAILED_head
    ENOLEOPFAILED._pack_ = 4
    ENOLEOPFAILED._fields_ = [
        ("nmhdr", win32more.UI.Controls.NMHDR),
        ("iob", Int32),
        ("lOper", Int32),
        ("hr", win32more.Foundation.HRESULT),
    ]
    return ENOLEOPFAILED
def _define_OBJECTPOSITIONS_head():
    class OBJECTPOSITIONS(Structure):
        pass
    return OBJECTPOSITIONS
def _define_OBJECTPOSITIONS():
    OBJECTPOSITIONS = win32more.UI.Controls.RichEdit.OBJECTPOSITIONS_head
    OBJECTPOSITIONS._pack_ = 4
    OBJECTPOSITIONS._fields_ = [
        ("nmhdr", win32more.UI.Controls.NMHDR),
        ("cObjectCount", Int32),
        ("pcpPositions", POINTER(Int32)),
    ]
    return OBJECTPOSITIONS
def _define_ENLINK_head():
    class ENLINK(Structure):
        pass
    return ENLINK
def _define_ENLINK():
    ENLINK = win32more.UI.Controls.RichEdit.ENLINK_head
    ENLINK._pack_ = 4
    ENLINK._fields_ = [
        ("nmhdr", win32more.UI.Controls.NMHDR),
        ("msg", UInt32),
        ("wParam", win32more.Foundation.WPARAM),
        ("lParam", win32more.Foundation.LPARAM),
        ("chrg", win32more.UI.Controls.RichEdit.CHARRANGE),
    ]
    return ENLINK
def _define_ENLOWFIRTF_head():
    class ENLOWFIRTF(Structure):
        pass
    return ENLOWFIRTF
def _define_ENLOWFIRTF():
    ENLOWFIRTF = win32more.UI.Controls.RichEdit.ENLOWFIRTF_head
    ENLOWFIRTF._pack_ = 4
    ENLOWFIRTF._fields_ = [
        ("nmhdr", win32more.UI.Controls.NMHDR),
        ("szControl", win32more.Foundation.PSTR),
    ]
    return ENLOWFIRTF
def _define_ENCORRECTTEXT_head():
    class ENCORRECTTEXT(Structure):
        pass
    return ENCORRECTTEXT
def _define_ENCORRECTTEXT():
    ENCORRECTTEXT = win32more.UI.Controls.RichEdit.ENCORRECTTEXT_head
    ENCORRECTTEXT._pack_ = 4
    ENCORRECTTEXT._fields_ = [
        ("nmhdr", win32more.UI.Controls.NMHDR),
        ("chrg", win32more.UI.Controls.RichEdit.CHARRANGE),
        ("seltyp", win32more.UI.Controls.RichEdit.RICH_EDIT_GET_CONTEXT_MENU_SEL_TYPE),
    ]
    return ENCORRECTTEXT
def _define_PUNCTUATION_head():
    class PUNCTUATION(Structure):
        pass
    return PUNCTUATION
def _define_PUNCTUATION():
    PUNCTUATION = win32more.UI.Controls.RichEdit.PUNCTUATION_head
    PUNCTUATION._pack_ = 4
    PUNCTUATION._fields_ = [
        ("iSize", UInt32),
        ("szPunctuation", win32more.Foundation.PSTR),
    ]
    return PUNCTUATION
def _define_COMPCOLOR_head():
    class COMPCOLOR(Structure):
        pass
    return COMPCOLOR
def _define_COMPCOLOR():
    COMPCOLOR = win32more.UI.Controls.RichEdit.COMPCOLOR_head
    COMPCOLOR._fields_ = [
        ("crText", UInt32),
        ("crBackground", UInt32),
        ("dwEffects", UInt32),
    ]
    return COMPCOLOR
def _define_REPASTESPECIAL_head():
    class REPASTESPECIAL(Structure):
        pass
    return REPASTESPECIAL
def _define_REPASTESPECIAL():
    REPASTESPECIAL = win32more.UI.Controls.RichEdit.REPASTESPECIAL_head
    REPASTESPECIAL._pack_ = 4
    REPASTESPECIAL._fields_ = [
        ("dwAspect", win32more.System.Com.DVASPECT),
        ("dwParam", UIntPtr),
    ]
    return REPASTESPECIAL
UNDONAMEID = Int32
UID_UNKNOWN = 0
UID_TYPING = 1
UID_DELETE = 2
UID_DRAGDROP = 3
UID_CUT = 4
UID_PASTE = 5
UID_AUTOTABLE = 6
def _define_SETTEXTEX_head():
    class SETTEXTEX(Structure):
        pass
    return SETTEXTEX
def _define_SETTEXTEX():
    SETTEXTEX = win32more.UI.Controls.RichEdit.SETTEXTEX_head
    SETTEXTEX._fields_ = [
        ("flags", UInt32),
        ("codepage", UInt32),
    ]
    return SETTEXTEX
def _define_GETTEXTEX_head():
    class GETTEXTEX(Structure):
        pass
    return GETTEXTEX
def _define_GETTEXTEX():
    GETTEXTEX = win32more.UI.Controls.RichEdit.GETTEXTEX_head
    GETTEXTEX._pack_ = 4
    GETTEXTEX._fields_ = [
        ("cb", UInt32),
        ("flags", win32more.UI.Controls.RichEdit.GETTEXTEX_FLAGS),
        ("codepage", UInt32),
        ("lpDefaultChar", win32more.Foundation.PSTR),
        ("lpUsedDefChar", POINTER(Int32)),
    ]
    return GETTEXTEX
def _define_GETTEXTLENGTHEX_head():
    class GETTEXTLENGTHEX(Structure):
        pass
    return GETTEXTLENGTHEX
def _define_GETTEXTLENGTHEX():
    GETTEXTLENGTHEX = win32more.UI.Controls.RichEdit.GETTEXTLENGTHEX_head
    GETTEXTLENGTHEX._fields_ = [
        ("flags", win32more.UI.Controls.RichEdit.GETTEXTLENGTHEX_FLAGS),
        ("codepage", UInt32),
    ]
    return GETTEXTLENGTHEX
def _define_BIDIOPTIONS_head():
    class BIDIOPTIONS(Structure):
        pass
    return BIDIOPTIONS
def _define_BIDIOPTIONS():
    BIDIOPTIONS = win32more.UI.Controls.RichEdit.BIDIOPTIONS_head
    BIDIOPTIONS._fields_ = [
        ("cbSize", UInt32),
        ("wMask", UInt16),
        ("wEffects", UInt16),
    ]
    return BIDIOPTIONS
KHYPH = Int32
KHYPH_khyphNil = 0
KHYPH_khyphNormal = 1
KHYPH_khyphAddBefore = 2
KHYPH_khyphChangeBefore = 3
KHYPH_khyphDeleteBefore = 4
KHYPH_khyphChangeAfter = 5
KHYPH_khyphDelAndChange = 6
def _define_hyphresult_head():
    class hyphresult(Structure):
        pass
    return hyphresult
def _define_hyphresult():
    hyphresult = win32more.UI.Controls.RichEdit.hyphresult_head
    hyphresult._fields_ = [
        ("khyph", win32more.UI.Controls.RichEdit.KHYPH),
        ("ichHyph", Int32),
        ("chHyph", Char),
    ]
    return hyphresult
def _define_HYPHENATEINFO_head():
    class HYPHENATEINFO(Structure):
        pass
    return HYPHENATEINFO
def _define_HYPHENATEINFO():
    HYPHENATEINFO = win32more.UI.Controls.RichEdit.HYPHENATEINFO_head
    HYPHENATEINFO._pack_ = 4
    HYPHENATEINFO._fields_ = [
        ("cbSize", Int16),
        ("dxHyphenateZone", Int16),
        ("pfnHyphenate", IntPtr),
    ]
    return HYPHENATEINFO
TXTBACKSTYLE = Int32
TXTBACK_TRANSPARENT = 0
TXTBACK_OPAQUE = 1
TXTHITRESULT = Int32
TXTHITRESULT_NOHIT = 0
TXTHITRESULT_TRANSPARENT = 1
TXTHITRESULT_CLOSE = 2
TXTHITRESULT_HIT = 3
TXTNATURALSIZE = Int32
TXTNS_FITTOCONTENT2 = 0
TXTNS_FITTOCONTENT = 1
TXTNS_ROUNDTOLINE = 2
TXTNS_FITTOCONTENT3 = 3
TXTNS_FITTOCONTENTWSP = 4
TXTNS_INCLUDELASTLINE = 1073741824
TXTNS_EMU = -2147483648
TXTVIEW = Int32
TXTVIEW_ACTIVE = 0
TXTVIEW_INACTIVE = -1
CHANGETYPE = Int32
CN_GENERIC = 0
CN_TEXTCHANGED = 1
CN_NEWUNDO = 2
CN_NEWREDO = 4
def _define_CHANGENOTIFY_head():
    class CHANGENOTIFY(Structure):
        pass
    return CHANGENOTIFY
def _define_CHANGENOTIFY():
    CHANGENOTIFY = win32more.UI.Controls.RichEdit.CHANGENOTIFY_head
    CHANGENOTIFY._fields_ = [
        ("dwChangeType", win32more.UI.Controls.RichEdit.CHANGETYPE),
        ("pvCookieData", c_void_p),
    ]
    return CHANGENOTIFY
def _define_ITextServices_head():
    class ITextServices(win32more.System.Com.IUnknown_head):
        Guid = Guid(None)
    return ITextServices
def _define_ITextServices():
    ITextServices = win32more.UI.Controls.RichEdit.ITextServices_head
    ITextServices.TxSendMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.LRESULT), use_last_error=False)(3, 'TxSendMessage', ((1, 'msg'),(1, 'wparam'),(1, 'lparam'),(1, 'plresult'),)))
    ITextServices.TxDraw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.DVASPECT,Int32,c_void_p,POINTER(win32more.System.Com.DVTARGETDEVICE_head),win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.RECTL_head),POINTER(win32more.Foundation.RECTL_head),POINTER(win32more.Foundation.RECT_head),IntPtr,UInt32,Int32, use_last_error=False)(4, 'TxDraw', ((1, 'dwDrawAspect'),(1, 'lindex'),(1, 'pvAspect'),(1, 'ptd'),(1, 'hdcDraw'),(1, 'hicTargetDev'),(1, 'lprcBounds'),(1, 'lprcWBounds'),(1, 'lprcUpdate'),(1, 'pfnContinue'),(1, 'dwContinue'),(1, 'lViewId'),)))
    ITextServices.TxGetHScroll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),POINTER(Int32),POINTER(Int32),POINTER(Int32),POINTER(win32more.Foundation.BOOL), use_last_error=False)(5, 'TxGetHScroll', ((1, 'plMin'),(1, 'plMax'),(1, 'plPos'),(1, 'plPage'),(1, 'pfEnabled'),)))
    ITextServices.TxGetVScroll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),POINTER(Int32),POINTER(Int32),POINTER(Int32),POINTER(win32more.Foundation.BOOL), use_last_error=False)(6, 'TxGetVScroll', ((1, 'plMin'),(1, 'plMax'),(1, 'plPos'),(1, 'plPage'),(1, 'pfEnabled'),)))
    ITextServices.OnTxSetCursor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.DVASPECT,Int32,c_void_p,POINTER(win32more.System.Com.DVTARGETDEVICE_head),win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.RECT_head),Int32,Int32, use_last_error=False)(7, 'OnTxSetCursor', ((1, 'dwDrawAspect'),(1, 'lindex'),(1, 'pvAspect'),(1, 'ptd'),(1, 'hdcDraw'),(1, 'hicTargetDev'),(1, 'lprcClient'),(1, 'x'),(1, 'y'),)))
    ITextServices.TxQueryHitPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.DVASPECT,Int32,c_void_p,POINTER(win32more.System.Com.DVTARGETDEVICE_head),win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.RECT_head),Int32,Int32,POINTER(UInt32), use_last_error=False)(8, 'TxQueryHitPoint', ((1, 'dwDrawAspect'),(1, 'lindex'),(1, 'pvAspect'),(1, 'ptd'),(1, 'hdcDraw'),(1, 'hicTargetDev'),(1, 'lprcClient'),(1, 'x'),(1, 'y'),(1, 'pHitResult'),)))
    ITextServices.OnTxInPlaceActivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(9, 'OnTxInPlaceActivate', ((1, 'prcClient'),)))
    ITextServices.OnTxInPlaceDeactivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'OnTxInPlaceDeactivate', ()))
    ITextServices.OnTxUIActivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'OnTxUIActivate', ()))
    ITextServices.OnTxUIDeactivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'OnTxUIDeactivate', ()))
    ITextServices.TxGetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'TxGetText', ((1, 'pbstrText'),)))
    ITextServices.TxSetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(14, 'TxSetText', ((1, 'pszText'),)))
    ITextServices.TxGetCurTargetX = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(15, 'TxGetCurTargetX', ((1, 'param0'),)))
    ITextServices.TxGetBaseLinePos = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(16, 'TxGetBaseLinePos', ((1, 'param0'),)))
    ITextServices.TxGetNaturalSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HDC,POINTER(win32more.System.Com.DVTARGETDEVICE_head),UInt32,POINTER(win32more.Foundation.SIZE_head),POINTER(Int32),POINTER(Int32), use_last_error=False)(17, 'TxGetNaturalSize', ((1, 'dwAspect'),(1, 'hdcDraw'),(1, 'hicTargetDev'),(1, 'ptd'),(1, 'dwMode'),(1, 'psizelExtent'),(1, 'pwidth'),(1, 'pheight'),)))
    ITextServices.TxGetDropTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IDropTarget_head), use_last_error=False)(18, 'TxGetDropTarget', ((1, 'ppDropTarget'),)))
    ITextServices.OnTxPropertyBitsChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(19, 'OnTxPropertyBitsChange', ((1, 'dwMask'),(1, 'dwBits'),)))
    ITextServices.TxGetCachedSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(20, 'TxGetCachedSize', ((1, 'pdwWidth'),(1, 'pdwHeight'),)))
    win32more.System.Com.IUnknown
    return ITextServices
CARET_FLAGS = Int32
CARET_NONE = 0
CARET_CUSTOM = 1
CARET_RTL = 2
CARET_ITALIC = 32
CARET_NULL = 64
CARET_ROTATE90 = 128
def _define_CARET_INFO_head():
    class CARET_INFO(Union):
        pass
    return CARET_INFO
def _define_CARET_INFO():
    CARET_INFO = win32more.UI.Controls.RichEdit.CARET_INFO_head
    CARET_INFO._fields_ = [
        ("hbitmap", win32more.Graphics.Gdi.HBITMAP),
        ("caretFlags", win32more.UI.Controls.RichEdit.CARET_FLAGS),
    ]
    return CARET_INFO
def _define_ITextHost_head():
    class ITextHost(win32more.System.Com.IUnknown_head):
        Guid = Guid(None)
    return ITextHost
def _define_ITextHost():
    ITextHost = win32more.UI.Controls.RichEdit.ITextHost_head
    ITextHost.TxGetDC = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Gdi.HDC, use_last_error=False)(3, 'TxGetDC', ()))
    ITextHost.TxReleaseDC = COMMETHOD(WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC, use_last_error=False)(4, 'TxReleaseDC', ((1, 'hdc'),)))
    ITextHost.TxShowScrollBar = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,Int32,win32more.Foundation.BOOL, use_last_error=False)(5, 'TxShowScrollBar', ((1, 'fnBar'),(1, 'fShow'),)))
    ITextHost.TxEnableScrollBar = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.WindowsAndMessaging.SCROLLBAR_CONSTANTS,win32more.UI.Controls.ENABLE_SCROLL_BAR_ARROWS, use_last_error=False)(6, 'TxEnableScrollBar', ((1, 'fuSBFlags'),(1, 'fuArrowflags'),)))
    ITextHost.TxSetScrollRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,Int32,Int32,Int32,win32more.Foundation.BOOL, use_last_error=False)(7, 'TxSetScrollRange', ((1, 'fnBar'),(1, 'nMinPos'),(1, 'nMaxPos'),(1, 'fRedraw'),)))
    ITextHost.TxSetScrollPos = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,Int32,Int32,win32more.Foundation.BOOL, use_last_error=False)(8, 'TxSetScrollPos', ((1, 'fnBar'),(1, 'nPos'),(1, 'fRedraw'),)))
    ITextHost.TxInvalidateRect = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Foundation.RECT_head),win32more.Foundation.BOOL, use_last_error=False)(9, 'TxInvalidateRect', ((1, 'prc'),(1, 'fMode'),)))
    ITextHost.TxViewChange = COMMETHOD(WINFUNCTYPE(Void,win32more.Foundation.BOOL, use_last_error=False)(10, 'TxViewChange', ((1, 'fUpdate'),)))
    ITextHost.TxCreateCaret = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HBITMAP,Int32,Int32, use_last_error=False)(11, 'TxCreateCaret', ((1, 'hbmp'),(1, 'xWidth'),(1, 'yHeight'),)))
    ITextHost.TxShowCaret = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.BOOL, use_last_error=False)(12, 'TxShowCaret', ((1, 'fShow'),)))
    ITextHost.TxSetCaretPos = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,Int32,Int32, use_last_error=False)(13, 'TxSetCaretPos', ((1, 'x'),(1, 'y'),)))
    ITextHost.TxSetTimer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,UInt32, use_last_error=False)(14, 'TxSetTimer', ((1, 'idTimer'),(1, 'uTimeout'),)))
    ITextHost.TxKillTimer = COMMETHOD(WINFUNCTYPE(Void,UInt32, use_last_error=False)(15, 'TxKillTimer', ((1, 'idTimer'),)))
    ITextHost.TxScrollWindowEx = COMMETHOD(WINFUNCTYPE(Void,Int32,Int32,POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.RECT_head),win32more.Graphics.Gdi.HRGN,POINTER(win32more.Foundation.RECT_head),win32more.UI.WindowsAndMessaging.SHOW_WINDOW_CMD, use_last_error=False)(16, 'TxScrollWindowEx', ((1, 'dx'),(1, 'dy'),(1, 'lprcScroll'),(1, 'lprcClip'),(1, 'hrgnUpdate'),(1, 'lprcUpdate'),(1, 'fuScroll'),)))
    ITextHost.TxSetCapture = COMMETHOD(WINFUNCTYPE(Void,win32more.Foundation.BOOL, use_last_error=False)(17, 'TxSetCapture', ((1, 'fCapture'),)))
    ITextHost.TxSetFocus = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(18, 'TxSetFocus', ()))
    ITextHost.TxSetCursor = COMMETHOD(WINFUNCTYPE(Void,win32more.UI.WindowsAndMessaging.HCURSOR,win32more.Foundation.BOOL, use_last_error=False)(19, 'TxSetCursor', ((1, 'hcur'),(1, 'fText'),)))
    ITextHost.TxScreenToClient = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.POINT_head), use_last_error=False)(20, 'TxScreenToClient', ((1, 'lppt'),)))
    ITextHost.TxClientToScreen = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.POINT_head), use_last_error=False)(21, 'TxClientToScreen', ((1, 'lppt'),)))
    ITextHost.TxActivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(22, 'TxActivate', ((1, 'plOldState'),)))
    ITextHost.TxDeactivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(23, 'TxDeactivate', ((1, 'lNewState'),)))
    ITextHost.TxGetClientRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(24, 'TxGetClientRect', ((1, 'prc'),)))
    ITextHost.TxGetViewInset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(25, 'TxGetViewInset', ((1, 'prc'),)))
    ITextHost.TxGetCharFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.UI.Controls.RichEdit.CHARFORMATW_head)), use_last_error=False)(26, 'TxGetCharFormat', ((1, 'ppCF'),)))
    ITextHost.TxGetParaFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.UI.Controls.RichEdit.PARAFORMAT_head)), use_last_error=False)(27, 'TxGetParaFormat', ((1, 'ppPF'),)))
    ITextHost.TxGetSysColor = COMMETHOD(WINFUNCTYPE(UInt32,Int32, use_last_error=False)(28, 'TxGetSysColor', ((1, 'nIndex'),)))
    ITextHost.TxGetBackStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.TXTBACKSTYLE), use_last_error=False)(29, 'TxGetBackStyle', ((1, 'pstyle'),)))
    ITextHost.TxGetMaxLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(30, 'TxGetMaxLength', ((1, 'plength'),)))
    ITextHost.TxGetScrollBars = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(31, 'TxGetScrollBars', ((1, 'pdwScrollBar'),)))
    ITextHost.TxGetPasswordChar = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(SByte), use_last_error=False)(32, 'TxGetPasswordChar', ((1, 'pch'),)))
    ITextHost.TxGetAcceleratorPos = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(33, 'TxGetAcceleratorPos', ((1, 'pcp'),)))
    ITextHost.TxGetExtent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.SIZE_head), use_last_error=False)(34, 'TxGetExtent', ((1, 'lpExtent'),)))
    ITextHost.OnTxCharFormatChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.CHARFORMATW_head), use_last_error=False)(35, 'OnTxCharFormatChange', ((1, 'pCF'),)))
    ITextHost.OnTxParaFormatChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.PARAFORMAT_head), use_last_error=False)(36, 'OnTxParaFormatChange', ((1, 'pPF'),)))
    ITextHost.TxGetPropertyBits = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(37, 'TxGetPropertyBits', ((1, 'dwMask'),(1, 'pdwBits'),)))
    ITextHost.TxNotify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p, use_last_error=False)(38, 'TxNotify', ((1, 'iNotify'),(1, 'pv'),)))
    ITextHost.TxImmGetContext = COMMETHOD(WINFUNCTYPE(win32more.Globalization.HIMC, use_last_error=False)(39, 'TxImmGetContext', ()))
    ITextHost.TxImmReleaseContext = COMMETHOD(WINFUNCTYPE(Void,win32more.Globalization.HIMC, use_last_error=False)(40, 'TxImmReleaseContext', ((1, 'himc'),)))
    ITextHost.TxGetSelectionBarWidth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(41, 'TxGetSelectionBarWidth', ((1, 'lSelBarWidth'),)))
    win32more.System.Com.IUnknown
    return ITextHost
def _define_IRicheditUiaOverrides_head():
    class IRicheditUiaOverrides(win32more.System.Com.IUnknown_head):
        Guid = Guid(None)
    return IRicheditUiaOverrides
def _define_IRicheditUiaOverrides():
    IRicheditUiaOverrides = win32more.UI.Controls.RichEdit.IRicheditUiaOverrides_head
    IRicheditUiaOverrides.GetPropertyOverrideValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(3, 'GetPropertyOverrideValue', ((1, 'propertyId'),(1, 'pRetValue'),)))
    win32more.System.Com.IUnknown
    return IRicheditUiaOverrides
def _define_PCreateTextServices():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.UI.Controls.RichEdit.ITextHost_head,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)
def _define_PShutdownTextServices():
    return CFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)
def _define_ITextHost2_head():
    class ITextHost2(win32more.UI.Controls.RichEdit.ITextHost_head):
        Guid = Guid(None)
    return ITextHost2
def _define_ITextHost2():
    ITextHost2 = win32more.UI.Controls.RichEdit.ITextHost2_head
    ITextHost2.TxIsDoubleClickPending = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(42, 'TxIsDoubleClickPending', ()))
    ITextHost2.TxGetWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HWND), use_last_error=False)(43, 'TxGetWindow', ((1, 'phwnd'),)))
    ITextHost2.TxSetForegroundWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(44, 'TxSetForegroundWindow', ()))
    ITextHost2.TxGetPalette = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Gdi.HPALETTE, use_last_error=False)(45, 'TxGetPalette', ()))
    ITextHost2.TxGetEastAsianFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(46, 'TxGetEastAsianFlags', ((1, 'pFlags'),)))
    ITextHost2.TxSetCursor2 = COMMETHOD(WINFUNCTYPE(win32more.UI.WindowsAndMessaging.HCURSOR,win32more.UI.WindowsAndMessaging.HCURSOR,win32more.Foundation.BOOL, use_last_error=False)(47, 'TxSetCursor2', ((1, 'hcur'),(1, 'bText'),)))
    ITextHost2.TxFreeTextServicesNotification = COMMETHOD(WINFUNCTYPE(Void, use_last_error=False)(48, 'TxFreeTextServicesNotification', ()))
    ITextHost2.TxGetEditStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(49, 'TxGetEditStyle', ((1, 'dwItem'),(1, 'pdwData'),)))
    ITextHost2.TxGetWindowStyles = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(50, 'TxGetWindowStyles', ((1, 'pdwStyle'),(1, 'pdwExStyle'),)))
    ITextHost2.TxShowDropCaret = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(51, 'TxShowDropCaret', ((1, 'fShow'),(1, 'hdc'),(1, 'prc'),)))
    ITextHost2.TxDestroyCaret = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(52, 'TxDestroyCaret', ()))
    ITextHost2.TxGetHorzExtent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(53, 'TxGetHorzExtent', ((1, 'plHorzExtent'),)))
    win32more.UI.Controls.RichEdit.ITextHost
    return ITextHost2
def _define_ITextServices2_head():
    class ITextServices2(win32more.UI.Controls.RichEdit.ITextServices_head):
        Guid = Guid(None)
    return ITextServices2
def _define_ITextServices2():
    ITextServices2 = win32more.UI.Controls.RichEdit.ITextServices2_head
    ITextServices2.TxGetNaturalSize2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HDC,POINTER(win32more.System.Com.DVTARGETDEVICE_head),UInt32,POINTER(win32more.Foundation.SIZE_head),POINTER(Int32),POINTER(Int32),POINTER(Int32), use_last_error=False)(21, 'TxGetNaturalSize2', ((1, 'dwAspect'),(1, 'hdcDraw'),(1, 'hicTargetDev'),(1, 'ptd'),(1, 'dwMode'),(1, 'psizelExtent'),(1, 'pwidth'),(1, 'pheight'),(1, 'pascent'),)))
    ITextServices2.TxDrawD2D = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct2D.ID2D1RenderTarget_head,POINTER(win32more.Foundation.RECTL_head),POINTER(win32more.Foundation.RECT_head),Int32, use_last_error=False)(22, 'TxDrawD2D', ((1, 'pRenderTarget'),(1, 'lprcBounds'),(1, 'lprcUpdate'),(1, 'lViewId'),)))
    win32more.UI.Controls.RichEdit.ITextServices
    return ITextServices2
def _define_REOBJECT_head():
    class REOBJECT(Structure):
        pass
    return REOBJECT
def _define_REOBJECT():
    REOBJECT = win32more.UI.Controls.RichEdit.REOBJECT_head
    REOBJECT._fields_ = [
        ("cbStruct", UInt32),
        ("cp", Int32),
        ("clsid", Guid),
        ("poleobj", win32more.System.Ole.IOleObject_head),
        ("pstg", win32more.System.Com.StructuredStorage.IStorage_head),
        ("polesite", win32more.System.Ole.IOleClientSite_head),
        ("sizel", win32more.Foundation.SIZE),
        ("dvaspect", UInt32),
        ("dwFlags", win32more.UI.Controls.RichEdit.REOBJECT_FLAGS),
        ("dwUser", UInt32),
    ]
    return REOBJECT
def _define_IRichEditOle_head():
    class IRichEditOle(win32more.System.Com.IUnknown_head):
        Guid = Guid('00020d00-0000-0000-c000-000000000046')
    return IRichEditOle
def _define_IRichEditOle():
    IRichEditOle = win32more.UI.Controls.RichEdit.IRichEditOle_head
    IRichEditOle.GetClientSite = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IOleClientSite_head), use_last_error=False)(3, 'GetClientSite', ((1, 'lplpolesite'),)))
    IRichEditOle.GetObjectCount = COMMETHOD(WINFUNCTYPE(Int32, use_last_error=False)(4, 'GetObjectCount', ()))
    IRichEditOle.GetLinkCount = COMMETHOD(WINFUNCTYPE(Int32, use_last_error=False)(5, 'GetLinkCount', ()))
    IRichEditOle.GetObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.UI.Controls.RichEdit.REOBJECT_head),win32more.UI.Controls.RichEdit.RICH_EDIT_GET_OBJECT_FLAGS, use_last_error=False)(6, 'GetObject', ((1, 'iob'),(1, 'lpreobject'),(1, 'dwFlags'),)))
    IRichEditOle.InsertObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.REOBJECT_head), use_last_error=False)(7, 'InsertObject', ((1, 'lpreobject'),)))
    IRichEditOle.ConvertObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Guid),win32more.Foundation.PSTR, use_last_error=False)(8, 'ConvertObject', ((1, 'iob'),(1, 'rclsidNew'),(1, 'lpstrUserTypeNew'),)))
    IRichEditOle.ActivateAs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid), use_last_error=False)(9, 'ActivateAs', ((1, 'rclsid'),(1, 'rclsidAs'),)))
    IRichEditOle.SetHostNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(10, 'SetHostNames', ((1, 'lpstrContainerApp'),(1, 'lpstrContainerObj'),)))
    IRichEditOle.SetLinkAvailable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BOOL, use_last_error=False)(11, 'SetLinkAvailable', ((1, 'iob'),(1, 'fAvailable'),)))
    IRichEditOle.SetDvaspect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,UInt32, use_last_error=False)(12, 'SetDvaspect', ((1, 'iob'),(1, 'dvaspect'),)))
    IRichEditOle.HandsOffStorage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(13, 'HandsOffStorage', ((1, 'iob'),)))
    IRichEditOle.SaveCompleted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.StructuredStorage.IStorage_head, use_last_error=False)(14, 'SaveCompleted', ((1, 'iob'),(1, 'lpstg'),)))
    IRichEditOle.InPlaceDeactivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(15, 'InPlaceDeactivate', ()))
    IRichEditOle.ContextSensitiveHelp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(16, 'ContextSensitiveHelp', ((1, 'fEnterMode'),)))
    IRichEditOle.GetClipboardData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.CHARRANGE_head),UInt32,POINTER(win32more.System.Com.IDataObject_head), use_last_error=False)(17, 'GetClipboardData', ((1, 'lpchrg'),(1, 'reco'),(1, 'lplpdataobj'),)))
    IRichEditOle.ImportDataObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head,UInt16,IntPtr, use_last_error=False)(18, 'ImportDataObject', ((1, 'lpdataobj'),(1, 'cf'),(1, 'hMetaPict'),)))
    win32more.System.Com.IUnknown
    return IRichEditOle
def _define_IRichEditOleCallback_head():
    class IRichEditOleCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('00020d03-0000-0000-c000-000000000046')
    return IRichEditOleCallback
def _define_IRichEditOleCallback():
    IRichEditOleCallback = win32more.UI.Controls.RichEdit.IRichEditOleCallback_head
    IRichEditOleCallback.GetNewStorage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.StructuredStorage.IStorage_head), use_last_error=False)(3, 'GetNewStorage', ((1, 'lplpstg'),)))
    IRichEditOleCallback.GetInPlaceContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IOleInPlaceFrame_head),POINTER(win32more.System.Ole.IOleInPlaceUIWindow_head),POINTER(win32more.System.Ole.OIFI_head), use_last_error=False)(4, 'GetInPlaceContext', ((1, 'lplpFrame'),(1, 'lplpDoc'),(1, 'lpFrameInfo'),)))
    IRichEditOleCallback.ShowContainerUI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(5, 'ShowContainerUI', ((1, 'fShow'),)))
    IRichEditOleCallback.QueryInsertObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.StructuredStorage.IStorage_head,Int32, use_last_error=False)(6, 'QueryInsertObject', ((1, 'lpclsid'),(1, 'lpstg'),(1, 'cp'),)))
    IRichEditOleCallback.DeleteObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IOleObject_head, use_last_error=False)(7, 'DeleteObject', ((1, 'lpoleobj'),)))
    IRichEditOleCallback.QueryAcceptData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head,POINTER(UInt16),UInt32,win32more.Foundation.BOOL,IntPtr, use_last_error=False)(8, 'QueryAcceptData', ((1, 'lpdataobj'),(1, 'lpcfFormat'),(1, 'reco'),(1, 'fReally'),(1, 'hMetaPict'),)))
    IRichEditOleCallback.ContextSensitiveHelp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(9, 'ContextSensitiveHelp', ((1, 'fEnterMode'),)))
    IRichEditOleCallback.GetClipboardData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.CHARRANGE_head),UInt32,POINTER(win32more.System.Com.IDataObject_head), use_last_error=False)(10, 'GetClipboardData', ((1, 'lpchrg'),(1, 'reco'),(1, 'lplpdataobj'),)))
    IRichEditOleCallback.GetDragDropEffect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,UInt32,POINTER(UInt32), use_last_error=False)(11, 'GetDragDropEffect', ((1, 'fDrag'),(1, 'grfKeyState'),(1, 'pdwEffect'),)))
    IRichEditOleCallback.GetContextMenu = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.RichEdit.RICH_EDIT_GET_CONTEXT_MENU_SEL_TYPE,win32more.System.Ole.IOleObject_head,POINTER(win32more.UI.Controls.RichEdit.CHARRANGE_head),POINTER(win32more.UI.WindowsAndMessaging.HMENU), use_last_error=False)(12, 'GetContextMenu', ((1, 'seltype'),(1, 'lpoleobj'),(1, 'lpchrg'),(1, 'lphmenu'),)))
    win32more.System.Com.IUnknown
    return IRichEditOleCallback
tomConstants = Int32
tomConstants_tomFalse = 0
tomConstants_tomTrue = -1
tomConstants_tomUndefined = -9999999
tomConstants_tomToggle = -9999998
tomConstants_tomAutoColor = -9999997
tomConstants_tomDefault = -9999996
tomConstants_tomSuspend = -9999995
tomConstants_tomResume = -9999994
tomConstants_tomApplyNow = 0
tomConstants_tomApplyLater = 1
tomConstants_tomTrackParms = 2
tomConstants_tomCacheParms = 3
tomConstants_tomApplyTmp = 4
tomConstants_tomDisableSmartFont = 8
tomConstants_tomEnableSmartFont = 9
tomConstants_tomUsePoints = 10
tomConstants_tomUseTwips = 11
tomConstants_tomBackward = -1073741823
tomConstants_tomForward = 1073741823
tomConstants_tomMove = 0
tomConstants_tomExtend = 1
tomConstants_tomNoSelection = 0
tomConstants_tomSelectionIP = 1
tomConstants_tomSelectionNormal = 2
tomConstants_tomSelectionFrame = 3
tomConstants_tomSelectionColumn = 4
tomConstants_tomSelectionRow = 5
tomConstants_tomSelectionBlock = 6
tomConstants_tomSelectionInlineShape = 7
tomConstants_tomSelectionShape = 8
tomConstants_tomSelStartActive = 1
tomConstants_tomSelAtEOL = 2
tomConstants_tomSelOvertype = 4
tomConstants_tomSelActive = 8
tomConstants_tomSelReplace = 16
tomConstants_tomEnd = 0
tomConstants_tomStart = 32
tomConstants_tomCollapseEnd = 0
tomConstants_tomCollapseStart = 1
tomConstants_tomClientCoord = 256
tomConstants_tomAllowOffClient = 512
tomConstants_tomTransform = 1024
tomConstants_tomObjectArg = 2048
tomConstants_tomAtEnd = 4096
tomConstants_tomNone = 0
tomConstants_tomSingle = 1
tomConstants_tomWords = 2
tomConstants_tomDouble = 3
tomConstants_tomDotted = 4
tomConstants_tomDash = 5
tomConstants_tomDashDot = 6
tomConstants_tomDashDotDot = 7
tomConstants_tomWave = 8
tomConstants_tomThick = 9
tomConstants_tomHair = 10
tomConstants_tomDoubleWave = 11
tomConstants_tomHeavyWave = 12
tomConstants_tomLongDash = 13
tomConstants_tomThickDash = 14
tomConstants_tomThickDashDot = 15
tomConstants_tomThickDashDotDot = 16
tomConstants_tomThickDotted = 17
tomConstants_tomThickLongDash = 18
tomConstants_tomLineSpaceSingle = 0
tomConstants_tomLineSpace1pt5 = 1
tomConstants_tomLineSpaceDouble = 2
tomConstants_tomLineSpaceAtLeast = 3
tomConstants_tomLineSpaceExactly = 4
tomConstants_tomLineSpaceMultiple = 5
tomConstants_tomLineSpacePercent = 6
tomConstants_tomAlignLeft = 0
tomConstants_tomAlignCenter = 1
tomConstants_tomAlignRight = 2
tomConstants_tomAlignJustify = 3
tomConstants_tomAlignDecimal = 3
tomConstants_tomAlignBar = 4
tomConstants_tomDefaultTab = 5
tomConstants_tomAlignInterWord = 3
tomConstants_tomAlignNewspaper = 4
tomConstants_tomAlignInterLetter = 5
tomConstants_tomAlignScaled = 6
tomConstants_tomSpaces = 0
tomConstants_tomDots = 1
tomConstants_tomDashes = 2
tomConstants_tomLines = 3
tomConstants_tomThickLines = 4
tomConstants_tomEquals = 5
tomConstants_tomTabBack = -3
tomConstants_tomTabNext = -2
tomConstants_tomTabHere = -1
tomConstants_tomListNone = 0
tomConstants_tomListBullet = 1
tomConstants_tomListNumberAsArabic = 2
tomConstants_tomListNumberAsLCLetter = 3
tomConstants_tomListNumberAsUCLetter = 4
tomConstants_tomListNumberAsLCRoman = 5
tomConstants_tomListNumberAsUCRoman = 6
tomConstants_tomListNumberAsSequence = 7
tomConstants_tomListNumberedCircle = 8
tomConstants_tomListNumberedBlackCircleWingding = 9
tomConstants_tomListNumberedWhiteCircleWingding = 10
tomConstants_tomListNumberedArabicWide = 11
tomConstants_tomListNumberedChS = 12
tomConstants_tomListNumberedChT = 13
tomConstants_tomListNumberedJpnChS = 14
tomConstants_tomListNumberedJpnKor = 15
tomConstants_tomListNumberedArabic1 = 16
tomConstants_tomListNumberedArabic2 = 17
tomConstants_tomListNumberedHebrew = 18
tomConstants_tomListNumberedThaiAlpha = 19
tomConstants_tomListNumberedThaiNum = 20
tomConstants_tomListNumberedHindiAlpha = 21
tomConstants_tomListNumberedHindiAlpha1 = 22
tomConstants_tomListNumberedHindiNum = 23
tomConstants_tomListParentheses = 65536
tomConstants_tomListPeriod = 131072
tomConstants_tomListPlain = 196608
tomConstants_tomListNoNumber = 262144
tomConstants_tomListMinus = 524288
tomConstants_tomIgnoreNumberStyle = 16777216
tomConstants_tomParaStyleNormal = -1
tomConstants_tomParaStyleHeading1 = -2
tomConstants_tomParaStyleHeading2 = -3
tomConstants_tomParaStyleHeading3 = -4
tomConstants_tomParaStyleHeading4 = -5
tomConstants_tomParaStyleHeading5 = -6
tomConstants_tomParaStyleHeading6 = -7
tomConstants_tomParaStyleHeading7 = -8
tomConstants_tomParaStyleHeading8 = -9
tomConstants_tomParaStyleHeading9 = -10
tomConstants_tomCharacter = 1
tomConstants_tomWord = 2
tomConstants_tomSentence = 3
tomConstants_tomParagraph = 4
tomConstants_tomLine = 5
tomConstants_tomStory = 6
tomConstants_tomScreen = 7
tomConstants_tomSection = 8
tomConstants_tomTableColumn = 9
tomConstants_tomColumn = 9
tomConstants_tomRow = 10
tomConstants_tomWindow = 11
tomConstants_tomCell = 12
tomConstants_tomCharFormat = 13
tomConstants_tomParaFormat = 14
tomConstants_tomTable = 15
tomConstants_tomObject = 16
tomConstants_tomPage = 17
tomConstants_tomHardParagraph = 18
tomConstants_tomCluster = 19
tomConstants_tomInlineObject = 20
tomConstants_tomInlineObjectArg = 21
tomConstants_tomLeafLine = 22
tomConstants_tomLayoutColumn = 23
tomConstants_tomProcessId = 1073741825
tomConstants_tomMatchWord = 2
tomConstants_tomMatchCase = 4
tomConstants_tomMatchPattern = 8
tomConstants_tomUnknownStory = 0
tomConstants_tomMainTextStory = 1
tomConstants_tomFootnotesStory = 2
tomConstants_tomEndnotesStory = 3
tomConstants_tomCommentsStory = 4
tomConstants_tomTextFrameStory = 5
tomConstants_tomEvenPagesHeaderStory = 6
tomConstants_tomPrimaryHeaderStory = 7
tomConstants_tomEvenPagesFooterStory = 8
tomConstants_tomPrimaryFooterStory = 9
tomConstants_tomFirstPageHeaderStory = 10
tomConstants_tomFirstPageFooterStory = 11
tomConstants_tomScratchStory = 127
tomConstants_tomFindStory = 128
tomConstants_tomReplaceStory = 129
tomConstants_tomStoryInactive = 0
tomConstants_tomStoryActiveDisplay = 1
tomConstants_tomStoryActiveUI = 2
tomConstants_tomStoryActiveDisplayUI = 3
tomConstants_tomNoAnimation = 0
tomConstants_tomLasVegasLights = 1
tomConstants_tomBlinkingBackground = 2
tomConstants_tomSparkleText = 3
tomConstants_tomMarchingBlackAnts = 4
tomConstants_tomMarchingRedAnts = 5
tomConstants_tomShimmer = 6
tomConstants_tomWipeDown = 7
tomConstants_tomWipeRight = 8
tomConstants_tomAnimationMax = 8
tomConstants_tomLowerCase = 0
tomConstants_tomUpperCase = 1
tomConstants_tomTitleCase = 2
tomConstants_tomSentenceCase = 4
tomConstants_tomToggleCase = 5
tomConstants_tomReadOnly = 256
tomConstants_tomShareDenyRead = 512
tomConstants_tomShareDenyWrite = 1024
tomConstants_tomPasteFile = 4096
tomConstants_tomCreateNew = 16
tomConstants_tomCreateAlways = 32
tomConstants_tomOpenExisting = 48
tomConstants_tomOpenAlways = 64
tomConstants_tomTruncateExisting = 80
tomConstants_tomRTF = 1
tomConstants_tomText = 2
tomConstants_tomHTML = 3
tomConstants_tomWordDocument = 4
tomConstants_tomBold = -2147483647
tomConstants_tomItalic = -2147483646
tomConstants_tomUnderline = -2147483644
tomConstants_tomStrikeout = -2147483640
tomConstants_tomProtected = -2147483632
tomConstants_tomLink = -2147483616
tomConstants_tomSmallCaps = -2147483584
tomConstants_tomAllCaps = -2147483520
tomConstants_tomHidden = -2147483392
tomConstants_tomOutline = -2147483136
tomConstants_tomShadow = -2147482624
tomConstants_tomEmboss = -2147481600
tomConstants_tomImprint = -2147479552
tomConstants_tomDisabled = -2147475456
tomConstants_tomRevised = -2147467264
tomConstants_tomSubscriptCF = -2147418112
tomConstants_tomSuperscriptCF = -2147352576
tomConstants_tomFontBound = -2146435072
tomConstants_tomLinkProtected = -2139095040
tomConstants_tomInlineObjectStart = -2130706432
tomConstants_tomExtendedChar = -2113929216
tomConstants_tomAutoBackColor = -2080374784
tomConstants_tomMathZoneNoBuildUp = -2013265920
tomConstants_tomMathZone = -1879048192
tomConstants_tomMathZoneOrdinary = -1610612736
tomConstants_tomAutoTextColor = -1073741824
tomConstants_tomMathZoneDisplay = 262144
tomConstants_tomParaEffectRTL = 1
tomConstants_tomParaEffectKeep = 2
tomConstants_tomParaEffectKeepNext = 4
tomConstants_tomParaEffectPageBreakBefore = 8
tomConstants_tomParaEffectNoLineNumber = 16
tomConstants_tomParaEffectNoWidowControl = 32
tomConstants_tomParaEffectDoNotHyphen = 64
tomConstants_tomParaEffectSideBySide = 128
tomConstants_tomParaEffectCollapsed = 256
tomConstants_tomParaEffectOutlineLevel = 512
tomConstants_tomParaEffectBox = 1024
tomConstants_tomParaEffectTableRowDelimiter = 4096
tomConstants_tomParaEffectTable = 16384
tomConstants_tomModWidthPairs = 1
tomConstants_tomModWidthSpace = 2
tomConstants_tomAutoSpaceAlpha = 4
tomConstants_tomAutoSpaceNumeric = 8
tomConstants_tomAutoSpaceParens = 16
tomConstants_tomEmbeddedFont = 32
tomConstants_tomDoublestrike = 64
tomConstants_tomOverlapping = 128
tomConstants_tomNormalCaret = 0
tomConstants_tomKoreanBlockCaret = 1
tomConstants_tomNullCaret = 2
tomConstants_tomIncludeInset = 1
tomConstants_tomUnicodeBiDi = 1
tomConstants_tomMathCFCheck = 4
tomConstants_tomUnlink = 8
tomConstants_tomUnhide = 16
tomConstants_tomCheckTextLimit = 32
tomConstants_tomIgnoreCurrentFont = 0
tomConstants_tomMatchCharRep = 1
tomConstants_tomMatchFontSignature = 2
tomConstants_tomMatchAscii = 4
tomConstants_tomGetHeightOnly = 8
tomConstants_tomMatchMathFont = 16
tomConstants_tomCharset = -2147483648
tomConstants_tomCharRepFromLcid = 1073741824
tomConstants_tomAnsi = 0
tomConstants_tomEastEurope = 1
tomConstants_tomCyrillic = 2
tomConstants_tomGreek = 3
tomConstants_tomTurkish = 4
tomConstants_tomHebrew = 5
tomConstants_tomArabic = 6
tomConstants_tomBaltic = 7
tomConstants_tomVietnamese = 8
tomConstants_tomDefaultCharRep = 9
tomConstants_tomSymbol = 10
tomConstants_tomThai = 11
tomConstants_tomShiftJIS = 12
tomConstants_tomGB2312 = 13
tomConstants_tomHangul = 14
tomConstants_tomBIG5 = 15
tomConstants_tomPC437 = 16
tomConstants_tomOEM = 17
tomConstants_tomMac = 18
tomConstants_tomArmenian = 19
tomConstants_tomSyriac = 20
tomConstants_tomThaana = 21
tomConstants_tomDevanagari = 22
tomConstants_tomBengali = 23
tomConstants_tomGurmukhi = 24
tomConstants_tomGujarati = 25
tomConstants_tomOriya = 26
tomConstants_tomTamil = 27
tomConstants_tomTelugu = 28
tomConstants_tomKannada = 29
tomConstants_tomMalayalam = 30
tomConstants_tomSinhala = 31
tomConstants_tomLao = 32
tomConstants_tomTibetan = 33
tomConstants_tomMyanmar = 34
tomConstants_tomGeorgian = 35
tomConstants_tomJamo = 36
tomConstants_tomEthiopic = 37
tomConstants_tomCherokee = 38
tomConstants_tomAboriginal = 39
tomConstants_tomOgham = 40
tomConstants_tomRunic = 41
tomConstants_tomKhmer = 42
tomConstants_tomMongolian = 43
tomConstants_tomBraille = 44
tomConstants_tomYi = 45
tomConstants_tomLimbu = 46
tomConstants_tomTaiLe = 47
tomConstants_tomNewTaiLue = 48
tomConstants_tomSylotiNagri = 49
tomConstants_tomKharoshthi = 50
tomConstants_tomKayahli = 51
tomConstants_tomUsymbol = 52
tomConstants_tomEmoji = 53
tomConstants_tomGlagolitic = 54
tomConstants_tomLisu = 55
tomConstants_tomVai = 56
tomConstants_tomNKo = 57
tomConstants_tomOsmanya = 58
tomConstants_tomPhagsPa = 59
tomConstants_tomGothic = 60
tomConstants_tomDeseret = 61
tomConstants_tomTifinagh = 62
tomConstants_tomCharRepMax = 63
tomConstants_tomRE10Mode = 1
tomConstants_tomUseAtFont = 2
tomConstants_tomTextFlowMask = 12
tomConstants_tomTextFlowES = 0
tomConstants_tomTextFlowSW = 4
tomConstants_tomTextFlowWN = 8
tomConstants_tomTextFlowNE = 12
tomConstants_tomNoIME = 524288
tomConstants_tomSelfIME = 262144
tomConstants_tomNoUpScroll = 65536
tomConstants_tomNoVpScroll = 262144
tomConstants_tomNoLink = 0
tomConstants_tomClientLink = 1
tomConstants_tomFriendlyLinkName = 2
tomConstants_tomFriendlyLinkAddress = 3
tomConstants_tomAutoLinkURL = 4
tomConstants_tomAutoLinkEmail = 5
tomConstants_tomAutoLinkPhone = 6
tomConstants_tomAutoLinkPath = 7
tomConstants_tomCompressNone = 0
tomConstants_tomCompressPunctuation = 1
tomConstants_tomCompressPunctuationAndKana = 2
tomConstants_tomCompressMax = 2
tomConstants_tomUnderlinePositionAuto = 0
tomConstants_tomUnderlinePositionBelow = 1
tomConstants_tomUnderlinePositionAbove = 2
tomConstants_tomUnderlinePositionMax = 2
tomConstants_tomFontAlignmentAuto = 0
tomConstants_tomFontAlignmentTop = 1
tomConstants_tomFontAlignmentBaseline = 2
tomConstants_tomFontAlignmentBottom = 3
tomConstants_tomFontAlignmentCenter = 4
tomConstants_tomFontAlignmentMax = 4
tomConstants_tomRubyBelow = 128
tomConstants_tomRubyAlignCenter = 0
tomConstants_tomRubyAlign010 = 1
tomConstants_tomRubyAlign121 = 2
tomConstants_tomRubyAlignLeft = 3
tomConstants_tomRubyAlignRight = 4
tomConstants_tomLimitsDefault = 0
tomConstants_tomLimitsUnderOver = 1
tomConstants_tomLimitsSubSup = 2
tomConstants_tomUpperLimitAsSuperScript = 3
tomConstants_tomLimitsOpposite = 4
tomConstants_tomShowLLimPlaceHldr = 8
tomConstants_tomShowULimPlaceHldr = 16
tomConstants_tomDontGrowWithContent = 64
tomConstants_tomGrowWithContent = 128
tomConstants_tomSubSupAlign = 1
tomConstants_tomLimitAlignMask = 3
tomConstants_tomLimitAlignCenter = 0
tomConstants_tomLimitAlignLeft = 1
tomConstants_tomLimitAlignRight = 2
tomConstants_tomShowDegPlaceHldr = 8
tomConstants_tomAlignDefault = 0
tomConstants_tomAlignMatchAscentDescent = 2
tomConstants_tomMathVariant = 32
tomConstants_tomStyleDefault = 0
tomConstants_tomStyleScriptScriptCramped = 1
tomConstants_tomStyleScriptScript = 2
tomConstants_tomStyleScriptCramped = 3
tomConstants_tomStyleScript = 4
tomConstants_tomStyleTextCramped = 5
tomConstants_tomStyleText = 6
tomConstants_tomStyleDisplayCramped = 7
tomConstants_tomStyleDisplay = 8
tomConstants_tomMathRelSize = 64
tomConstants_tomDecDecSize = 254
tomConstants_tomDecSize = 255
tomConstants_tomIncSize = 65
tomConstants_tomIncIncSize = 66
tomConstants_tomGravityUI = 0
tomConstants_tomGravityBack = 1
tomConstants_tomGravityFore = 2
tomConstants_tomGravityIn = 3
tomConstants_tomGravityOut = 4
tomConstants_tomGravityBackward = 536870912
tomConstants_tomGravityForward = 1073741824
tomConstants_tomAdjustCRLF = 1
tomConstants_tomUseCRLF = 2
tomConstants_tomTextize = 4
tomConstants_tomAllowFinalEOP = 8
tomConstants_tomFoldMathAlpha = 16
tomConstants_tomNoHidden = 32
tomConstants_tomIncludeNumbering = 64
tomConstants_tomTranslateTableCell = 128
tomConstants_tomNoMathZoneBrackets = 256
tomConstants_tomConvertMathChar = 512
tomConstants_tomNoUCGreekItalic = 1024
tomConstants_tomAllowMathBold = 2048
tomConstants_tomLanguageTag = 4096
tomConstants_tomConvertRTF = 8192
tomConstants_tomApplyRtfDocProps = 16384
tomConstants_tomPhantomShow = 1
tomConstants_tomPhantomZeroWidth = 2
tomConstants_tomPhantomZeroAscent = 4
tomConstants_tomPhantomZeroDescent = 8
tomConstants_tomPhantomTransparent = 16
tomConstants_tomPhantomASmash = 5
tomConstants_tomPhantomDSmash = 9
tomConstants_tomPhantomHSmash = 3
tomConstants_tomPhantomSmash = 13
tomConstants_tomPhantomHorz = 12
tomConstants_tomPhantomVert = 2
tomConstants_tomBoxHideTop = 1
tomConstants_tomBoxHideBottom = 2
tomConstants_tomBoxHideLeft = 4
tomConstants_tomBoxHideRight = 8
tomConstants_tomBoxStrikeH = 16
tomConstants_tomBoxStrikeV = 32
tomConstants_tomBoxStrikeTLBR = 64
tomConstants_tomBoxStrikeBLTR = 128
tomConstants_tomBoxAlignCenter = 1
tomConstants_tomSpaceMask = 28
tomConstants_tomSpaceDefault = 0
tomConstants_tomSpaceUnary = 4
tomConstants_tomSpaceBinary = 8
tomConstants_tomSpaceRelational = 12
tomConstants_tomSpaceSkip = 16
tomConstants_tomSpaceOrd = 20
tomConstants_tomSpaceDifferential = 24
tomConstants_tomSizeText = 32
tomConstants_tomSizeScript = 64
tomConstants_tomSizeScriptScript = 96
tomConstants_tomNoBreak = 128
tomConstants_tomTransparentForPositioning = 256
tomConstants_tomTransparentForSpacing = 512
tomConstants_tomStretchCharBelow = 0
tomConstants_tomStretchCharAbove = 1
tomConstants_tomStretchBaseBelow = 2
tomConstants_tomStretchBaseAbove = 3
tomConstants_tomMatrixAlignMask = 3
tomConstants_tomMatrixAlignCenter = 0
tomConstants_tomMatrixAlignTopRow = 1
tomConstants_tomMatrixAlignBottomRow = 3
tomConstants_tomShowMatPlaceHldr = 8
tomConstants_tomEqArrayLayoutWidth = 1
tomConstants_tomEqArrayAlignMask = 12
tomConstants_tomEqArrayAlignCenter = 0
tomConstants_tomEqArrayAlignTopRow = 4
tomConstants_tomEqArrayAlignBottomRow = 12
tomConstants_tomMathManualBreakMask = 127
tomConstants_tomMathBreakLeft = 125
tomConstants_tomMathBreakCenter = 126
tomConstants_tomMathBreakRight = 127
tomConstants_tomMathEqAlign = 128
tomConstants_tomMathArgShadingStart = 593
tomConstants_tomMathArgShadingEnd = 594
tomConstants_tomMathObjShadingStart = 595
tomConstants_tomMathObjShadingEnd = 596
tomConstants_tomFunctionTypeNone = 0
tomConstants_tomFunctionTypeTakesArg = 1
tomConstants_tomFunctionTypeTakesLim = 2
tomConstants_tomFunctionTypeTakesLim2 = 3
tomConstants_tomFunctionTypeIsLim = 4
tomConstants_tomMathParaAlignDefault = 0
tomConstants_tomMathParaAlignCenterGroup = 1
tomConstants_tomMathParaAlignCenter = 2
tomConstants_tomMathParaAlignLeft = 3
tomConstants_tomMathParaAlignRight = 4
tomConstants_tomMathDispAlignMask = 3
tomConstants_tomMathDispAlignCenterGroup = 0
tomConstants_tomMathDispAlignCenter = 1
tomConstants_tomMathDispAlignLeft = 2
tomConstants_tomMathDispAlignRight = 3
tomConstants_tomMathDispIntUnderOver = 4
tomConstants_tomMathDispFracTeX = 8
tomConstants_tomMathDispNaryGrow = 16
tomConstants_tomMathDocEmptyArgMask = 96
tomConstants_tomMathDocEmptyArgAuto = 0
tomConstants_tomMathDocEmptyArgAlways = 32
tomConstants_tomMathDocEmptyArgNever = 64
tomConstants_tomMathDocSbSpOpUnchanged = 128
tomConstants_tomMathDocDiffMask = 768
tomConstants_tomMathDocDiffDefault = 0
tomConstants_tomMathDocDiffUpright = 256
tomConstants_tomMathDocDiffItalic = 512
tomConstants_tomMathDocDiffOpenItalic = 768
tomConstants_tomMathDispNarySubSup = 1024
tomConstants_tomMathDispDef = 2048
tomConstants_tomMathEnableRtl = 4096
tomConstants_tomMathBrkBinMask = 196608
tomConstants_tomMathBrkBinBefore = 0
tomConstants_tomMathBrkBinAfter = 65536
tomConstants_tomMathBrkBinDup = 131072
tomConstants_tomMathBrkBinSubMask = 786432
tomConstants_tomMathBrkBinSubMM = 0
tomConstants_tomMathBrkBinSubPM = 262144
tomConstants_tomMathBrkBinSubMP = 524288
tomConstants_tomSelRange = 597
tomConstants_tomHstring = 596
tomConstants_tomFontPropTeXStyle = 828
tomConstants_tomFontPropAlign = 829
tomConstants_tomFontStretch = 830
tomConstants_tomFontStyle = 831
tomConstants_tomFontStyleUpright = 0
tomConstants_tomFontStyleOblique = 1
tomConstants_tomFontStyleItalic = 2
tomConstants_tomFontStretchDefault = 0
tomConstants_tomFontStretchUltraCondensed = 1
tomConstants_tomFontStretchExtraCondensed = 2
tomConstants_tomFontStretchCondensed = 3
tomConstants_tomFontStretchSemiCondensed = 4
tomConstants_tomFontStretchNormal = 5
tomConstants_tomFontStretchSemiExpanded = 6
tomConstants_tomFontStretchExpanded = 7
tomConstants_tomFontStretchExtraExpanded = 8
tomConstants_tomFontStretchUltraExpanded = 9
tomConstants_tomFontWeightDefault = 0
tomConstants_tomFontWeightThin = 100
tomConstants_tomFontWeightExtraLight = 200
tomConstants_tomFontWeightLight = 300
tomConstants_tomFontWeightNormal = 400
tomConstants_tomFontWeightRegular = 400
tomConstants_tomFontWeightMedium = 500
tomConstants_tomFontWeightSemiBold = 600
tomConstants_tomFontWeightBold = 700
tomConstants_tomFontWeightExtraBold = 800
tomConstants_tomFontWeightBlack = 900
tomConstants_tomFontWeightHeavy = 900
tomConstants_tomFontWeightExtraBlack = 950
tomConstants_tomParaPropMathAlign = 1079
tomConstants_tomDocMathBuild = 128
tomConstants_tomMathLMargin = 129
tomConstants_tomMathRMargin = 130
tomConstants_tomMathWrapIndent = 131
tomConstants_tomMathWrapRight = 132
tomConstants_tomMathPostSpace = 134
tomConstants_tomMathPreSpace = 133
tomConstants_tomMathInterSpace = 135
tomConstants_tomMathIntraSpace = 136
tomConstants_tomCanCopy = 137
tomConstants_tomCanRedo = 138
tomConstants_tomCanUndo = 139
tomConstants_tomUndoLimit = 140
tomConstants_tomDocAutoLink = 141
tomConstants_tomEllipsisMode = 142
tomConstants_tomEllipsisState = 143
tomConstants_tomEllipsisNone = 0
tomConstants_tomEllipsisEnd = 1
tomConstants_tomEllipsisWord = 3
tomConstants_tomEllipsisPresent = 1
tomConstants_tomVTopCell = 1
tomConstants_tomVLowCell = 2
tomConstants_tomHStartCell = 4
tomConstants_tomHContCell = 8
tomConstants_tomRowUpdate = 1
tomConstants_tomRowApplyDefault = 0
tomConstants_tomCellStructureChangeOnly = 1
tomConstants_tomRowHeightActual = 2059
OBJECTTYPE = Int32
OBJECTTYPE_tomSimpleText = 0
OBJECTTYPE_tomRuby = 1
OBJECTTYPE_tomHorzVert = 2
OBJECTTYPE_tomWarichu = 3
OBJECTTYPE_tomEq = 9
OBJECTTYPE_tomMath = 10
OBJECTTYPE_tomAccent = 10
OBJECTTYPE_tomBox = 11
OBJECTTYPE_tomBoxedFormula = 12
OBJECTTYPE_tomBrackets = 13
OBJECTTYPE_tomBracketsWithSeps = 14
OBJECTTYPE_tomEquationArray = 15
OBJECTTYPE_tomFraction = 16
OBJECTTYPE_tomFunctionApply = 17
OBJECTTYPE_tomLeftSubSup = 18
OBJECTTYPE_tomLowerLimit = 19
OBJECTTYPE_tomMatrix = 20
OBJECTTYPE_tomNary = 21
OBJECTTYPE_tomOpChar = 22
OBJECTTYPE_tomOverbar = 23
OBJECTTYPE_tomPhantom = 24
OBJECTTYPE_tomRadical = 25
OBJECTTYPE_tomSlashedFraction = 26
OBJECTTYPE_tomStack = 27
OBJECTTYPE_tomStretchStack = 28
OBJECTTYPE_tomSubscript = 29
OBJECTTYPE_tomSubSup = 30
OBJECTTYPE_tomSuperscript = 31
OBJECTTYPE_tomUnderbar = 32
OBJECTTYPE_tomUpperLimit = 33
OBJECTTYPE_tomObjectMax = 33
MANCODE = Int32
MBOLD = 16
MITAL = 32
MGREEK = 64
MROMN = 0
MSCRP = 1
MFRAK = 2
MOPEN = 3
MSANS = 4
MMONO = 5
MMATH = 6
MISOL = 7
MINIT = 8
MTAIL = 9
MSTRCH = 10
MLOOP = 11
MOPENA = 12
def _define_ITextDocument_head():
    class ITextDocument(win32more.System.Com.IDispatch_head):
        Guid = Guid('8cc497c0-a1df-11ce-8098-00aa0047be5d')
    return ITextDocument
def _define_ITextDocument():
    ITextDocument = win32more.UI.Controls.RichEdit.ITextDocument_head
    ITextDocument.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'GetName', ((1, 'pName'),)))
    ITextDocument.GetSelection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.ITextSelection_head), use_last_error=False)(8, 'GetSelection', ((1, 'ppSel'),)))
    ITextDocument.GetStoryCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'GetStoryCount', ((1, 'pCount'),)))
    ITextDocument.GetStoryRanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.ITextStoryRanges_head), use_last_error=False)(10, 'GetStoryRanges', ((1, 'ppStories'),)))
    ITextDocument.GetSaved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(11, 'GetSaved', ((1, 'pValue'),)))
    ITextDocument.SetSaved = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.RichEdit.tomConstants, use_last_error=False)(12, 'SetSaved', ((1, 'Value'),)))
    ITextDocument.GetDefaultTabStop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(13, 'GetDefaultTabStop', ((1, 'pValue'),)))
    ITextDocument.SetDefaultTabStop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(14, 'SetDefaultTabStop', ((1, 'Value'),)))
    ITextDocument.New = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(15, 'New', ()))
    ITextDocument.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),Int32,Int32, use_last_error=False)(16, 'Open', ((1, 'pVar'),(1, 'Flags'),(1, 'CodePage'),)))
    ITextDocument.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),Int32,Int32, use_last_error=False)(17, 'Save', ((1, 'pVar'),(1, 'Flags'),(1, 'CodePage'),)))
    ITextDocument.Freeze = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(18, 'Freeze', ((1, 'pCount'),)))
    ITextDocument.Unfreeze = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(19, 'Unfreeze', ((1, 'pCount'),)))
    ITextDocument.BeginEditCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(20, 'BeginEditCollection', ()))
    ITextDocument.EndEditCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(21, 'EndEditCollection', ()))
    ITextDocument.Undo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int32), use_last_error=False)(22, 'Undo', ((1, 'Count'),(1, 'pCount'),)))
    ITextDocument.Redo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int32), use_last_error=False)(23, 'Redo', ((1, 'Count'),(1, 'pCount'),)))
    ITextDocument.Range = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.UI.Controls.RichEdit.ITextRange_head), use_last_error=False)(24, 'Range', ((1, 'cpActive'),(1, 'cpAnchor'),(1, 'ppRange'),)))
    ITextDocument.RangeFromPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.UI.Controls.RichEdit.ITextRange_head), use_last_error=False)(25, 'RangeFromPoint', ((1, 'x'),(1, 'y'),(1, 'ppRange'),)))
    win32more.System.Com.IDispatch
    return ITextDocument
def _define_ITextRange_head():
    class ITextRange(win32more.System.Com.IDispatch_head):
        Guid = Guid('8cc497c2-a1df-11ce-8098-00aa0047be5d')
    return ITextRange
def _define_ITextRange():
    ITextRange = win32more.UI.Controls.RichEdit.ITextRange_head
    ITextRange.GetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'GetText', ((1, 'pbstr'),)))
    ITextRange.SetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(8, 'SetText', ((1, 'bstr'),)))
    ITextRange.GetChar = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'GetChar', ((1, 'pChar'),)))
    ITextRange.SetChar = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(10, 'SetChar', ((1, 'Char'),)))
    ITextRange.GetDuplicate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.ITextRange_head), use_last_error=False)(11, 'GetDuplicate', ((1, 'ppRange'),)))
    ITextRange.GetFormattedText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.ITextRange_head), use_last_error=False)(12, 'GetFormattedText', ((1, 'ppRange'),)))
    ITextRange.SetFormattedText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.RichEdit.ITextRange_head, use_last_error=False)(13, 'SetFormattedText', ((1, 'pRange'),)))
    ITextRange.GetStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(14, 'GetStart', ((1, 'pcpFirst'),)))
    ITextRange.SetStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(15, 'SetStart', ((1, 'cpFirst'),)))
    ITextRange.GetEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(16, 'GetEnd', ((1, 'pcpLim'),)))
    ITextRange.SetEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(17, 'SetEnd', ((1, 'cpLim'),)))
    ITextRange.GetFont = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.ITextFont_head), use_last_error=False)(18, 'GetFont', ((1, 'ppFont'),)))
    ITextRange.SetFont = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.RichEdit.ITextFont_head, use_last_error=False)(19, 'SetFont', ((1, 'pFont'),)))
    ITextRange.GetPara = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.ITextPara_head), use_last_error=False)(20, 'GetPara', ((1, 'ppPara'),)))
    ITextRange.SetPara = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.RichEdit.ITextPara_head, use_last_error=False)(21, 'SetPara', ((1, 'pPara'),)))
    ITextRange.GetStoryLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(22, 'GetStoryLength', ((1, 'pCount'),)))
    ITextRange.GetStoryType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(23, 'GetStoryType', ((1, 'pValue'),)))
    ITextRange.Collapse = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(24, 'Collapse', ((1, 'bStart'),)))
    ITextRange.Expand = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int32), use_last_error=False)(25, 'Expand', ((1, 'Unit'),(1, 'pDelta'),)))
    ITextRange.GetIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int32), use_last_error=False)(26, 'GetIndex', ((1, 'Unit'),(1, 'pIndex'),)))
    ITextRange.SetIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Int32, use_last_error=False)(27, 'SetIndex', ((1, 'Unit'),(1, 'Index'),(1, 'Extend'),)))
    ITextRange.SetRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(28, 'SetRange', ((1, 'cpAnchor'),(1, 'cpActive'),)))
    ITextRange.InRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.RichEdit.ITextRange_head,POINTER(Int32), use_last_error=False)(29, 'InRange', ((1, 'pRange'),(1, 'pValue'),)))
    ITextRange.InStory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.RichEdit.ITextRange_head,POINTER(Int32), use_last_error=False)(30, 'InStory', ((1, 'pRange'),(1, 'pValue'),)))
    ITextRange.IsEqual = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.RichEdit.ITextRange_head,POINTER(Int32), use_last_error=False)(31, 'IsEqual', ((1, 'pRange'),(1, 'pValue'),)))
    ITextRange.Select = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(32, 'Select', ()))
    ITextRange.StartOf = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(Int32), use_last_error=False)(33, 'StartOf', ((1, 'Unit'),(1, 'Extend'),(1, 'pDelta'),)))
    ITextRange.EndOf = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(Int32), use_last_error=False)(34, 'EndOf', ((1, 'Unit'),(1, 'Extend'),(1, 'pDelta'),)))
    ITextRange.Move = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(Int32), use_last_error=False)(35, 'Move', ((1, 'Unit'),(1, 'Count'),(1, 'pDelta'),)))
    ITextRange.MoveStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(Int32), use_last_error=False)(36, 'MoveStart', ((1, 'Unit'),(1, 'Count'),(1, 'pDelta'),)))
    ITextRange.MoveEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(Int32), use_last_error=False)(37, 'MoveEnd', ((1, 'Unit'),(1, 'Count'),(1, 'pDelta'),)))
    ITextRange.MoveWhile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),Int32,POINTER(Int32), use_last_error=False)(38, 'MoveWhile', ((1, 'Cset'),(1, 'Count'),(1, 'pDelta'),)))
    ITextRange.MoveStartWhile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),Int32,POINTER(Int32), use_last_error=False)(39, 'MoveStartWhile', ((1, 'Cset'),(1, 'Count'),(1, 'pDelta'),)))
    ITextRange.MoveEndWhile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),Int32,POINTER(Int32), use_last_error=False)(40, 'MoveEndWhile', ((1, 'Cset'),(1, 'Count'),(1, 'pDelta'),)))
    ITextRange.MoveUntil = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),Int32,POINTER(Int32), use_last_error=False)(41, 'MoveUntil', ((1, 'Cset'),(1, 'Count'),(1, 'pDelta'),)))
    ITextRange.MoveStartUntil = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),Int32,POINTER(Int32), use_last_error=False)(42, 'MoveStartUntil', ((1, 'Cset'),(1, 'Count'),(1, 'pDelta'),)))
    ITextRange.MoveEndUntil = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),Int32,POINTER(Int32), use_last_error=False)(43, 'MoveEndUntil', ((1, 'Cset'),(1, 'Count'),(1, 'pDelta'),)))
    ITextRange.FindText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,Int32,POINTER(Int32), use_last_error=False)(44, 'FindText', ((1, 'bstr'),(1, 'Count'),(1, 'Flags'),(1, 'pLength'),)))
    ITextRange.FindTextStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,Int32,POINTER(Int32), use_last_error=False)(45, 'FindTextStart', ((1, 'bstr'),(1, 'Count'),(1, 'Flags'),(1, 'pLength'),)))
    ITextRange.FindTextEnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,Int32,POINTER(Int32), use_last_error=False)(46, 'FindTextEnd', ((1, 'bstr'),(1, 'Count'),(1, 'Flags'),(1, 'pLength'),)))
    ITextRange.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(Int32), use_last_error=False)(47, 'Delete', ((1, 'Unit'),(1, 'Count'),(1, 'pDelta'),)))
    ITextRange.Cut = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(48, 'Cut', ((1, 'pVar'),)))
    ITextRange.Copy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(49, 'Copy', ((1, 'pVar'),)))
    ITextRange.Paste = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),Int32, use_last_error=False)(50, 'Paste', ((1, 'pVar'),(1, 'Format'),)))
    ITextRange.CanPaste = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),Int32,POINTER(Int32), use_last_error=False)(51, 'CanPaste', ((1, 'pVar'),(1, 'Format'),(1, 'pValue'),)))
    ITextRange.CanEdit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(52, 'CanEdit', ((1, 'pValue'),)))
    ITextRange.ChangeCase = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(53, 'ChangeCase', ((1, 'Type'),)))
    ITextRange.GetPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int32),POINTER(Int32), use_last_error=False)(54, 'GetPoint', ((1, 'Type'),(1, 'px'),(1, 'py'),)))
    ITextRange.SetPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Int32,Int32, use_last_error=False)(55, 'SetPoint', ((1, 'x'),(1, 'y'),(1, 'Type'),(1, 'Extend'),)))
    ITextRange.ScrollIntoView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(56, 'ScrollIntoView', ((1, 'Value'),)))
    ITextRange.GetEmbeddedObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(57, 'GetEmbeddedObject', ((1, 'ppObject'),)))
    win32more.System.Com.IDispatch
    return ITextRange
def _define_ITextSelection_head():
    class ITextSelection(win32more.UI.Controls.RichEdit.ITextRange_head):
        Guid = Guid('8cc497c1-a1df-11ce-8098-00aa0047be5d')
    return ITextSelection
def _define_ITextSelection():
    ITextSelection = win32more.UI.Controls.RichEdit.ITextSelection_head
    ITextSelection.GetFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(58, 'GetFlags', ((1, 'pFlags'),)))
    ITextSelection.SetFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(59, 'SetFlags', ((1, 'Flags'),)))
    ITextSelection.GetType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(60, 'GetType', ((1, 'pType'),)))
    ITextSelection.MoveLeft = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Int32,POINTER(Int32), use_last_error=False)(61, 'MoveLeft', ((1, 'Unit'),(1, 'Count'),(1, 'Extend'),(1, 'pDelta'),)))
    ITextSelection.MoveRight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Int32,POINTER(Int32), use_last_error=False)(62, 'MoveRight', ((1, 'Unit'),(1, 'Count'),(1, 'Extend'),(1, 'pDelta'),)))
    ITextSelection.MoveUp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Int32,POINTER(Int32), use_last_error=False)(63, 'MoveUp', ((1, 'Unit'),(1, 'Count'),(1, 'Extend'),(1, 'pDelta'),)))
    ITextSelection.MoveDown = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Int32,POINTER(Int32), use_last_error=False)(64, 'MoveDown', ((1, 'Unit'),(1, 'Count'),(1, 'Extend'),(1, 'pDelta'),)))
    ITextSelection.HomeKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.RichEdit.tomConstants,Int32,POINTER(Int32), use_last_error=False)(65, 'HomeKey', ((1, 'Unit'),(1, 'Extend'),(1, 'pDelta'),)))
    ITextSelection.EndKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(Int32), use_last_error=False)(66, 'EndKey', ((1, 'Unit'),(1, 'Extend'),(1, 'pDelta'),)))
    ITextSelection.TypeText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(67, 'TypeText', ((1, 'bstr'),)))
    win32more.UI.Controls.RichEdit.ITextRange
    return ITextSelection
def _define_ITextFont_head():
    class ITextFont(win32more.System.Com.IDispatch_head):
        Guid = Guid('8cc497c3-a1df-11ce-8098-00aa0047be5d')
    return ITextFont
def _define_ITextFont():
    ITextFont = win32more.UI.Controls.RichEdit.ITextFont_head
    ITextFont.GetDuplicate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.ITextFont_head), use_last_error=False)(7, 'GetDuplicate', ((1, 'ppFont'),)))
    ITextFont.SetDuplicate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.RichEdit.ITextFont_head, use_last_error=False)(8, 'SetDuplicate', ((1, 'pFont'),)))
    ITextFont.CanChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'CanChange', ((1, 'pValue'),)))
    ITextFont.IsEqual = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.RichEdit.ITextFont_head,POINTER(Int32), use_last_error=False)(10, 'IsEqual', ((1, 'pFont'),(1, 'pValue'),)))
    ITextFont.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.RichEdit.tomConstants, use_last_error=False)(11, 'Reset', ((1, 'Value'),)))
    ITextFont.GetStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(12, 'GetStyle', ((1, 'pValue'),)))
    ITextFont.SetStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(13, 'SetStyle', ((1, 'Value'),)))
    ITextFont.GetAllCaps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(14, 'GetAllCaps', ((1, 'pValue'),)))
    ITextFont.SetAllCaps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(15, 'SetAllCaps', ((1, 'Value'),)))
    ITextFont.GetAnimation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(16, 'GetAnimation', ((1, 'pValue'),)))
    ITextFont.SetAnimation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(17, 'SetAnimation', ((1, 'Value'),)))
    ITextFont.GetBackColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(18, 'GetBackColor', ((1, 'pValue'),)))
    ITextFont.SetBackColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(19, 'SetBackColor', ((1, 'Value'),)))
    ITextFont.GetBold = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(20, 'GetBold', ((1, 'pValue'),)))
    ITextFont.SetBold = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(21, 'SetBold', ((1, 'Value'),)))
    ITextFont.GetEmboss = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(22, 'GetEmboss', ((1, 'pValue'),)))
    ITextFont.SetEmboss = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(23, 'SetEmboss', ((1, 'Value'),)))
    ITextFont.GetForeColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(24, 'GetForeColor', ((1, 'pValue'),)))
    ITextFont.SetForeColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(25, 'SetForeColor', ((1, 'Value'),)))
    ITextFont.GetHidden = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(26, 'GetHidden', ((1, 'pValue'),)))
    ITextFont.SetHidden = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(27, 'SetHidden', ((1, 'Value'),)))
    ITextFont.GetEngrave = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(28, 'GetEngrave', ((1, 'pValue'),)))
    ITextFont.SetEngrave = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(29, 'SetEngrave', ((1, 'Value'),)))
    ITextFont.GetItalic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(30, 'GetItalic', ((1, 'pValue'),)))
    ITextFont.SetItalic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(31, 'SetItalic', ((1, 'Value'),)))
    ITextFont.GetKerning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(32, 'GetKerning', ((1, 'pValue'),)))
    ITextFont.SetKerning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(33, 'SetKerning', ((1, 'Value'),)))
    ITextFont.GetLanguageID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(34, 'GetLanguageID', ((1, 'pValue'),)))
    ITextFont.SetLanguageID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(35, 'SetLanguageID', ((1, 'Value'),)))
    ITextFont.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(36, 'GetName', ((1, 'pbstr'),)))
    ITextFont.SetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(37, 'SetName', ((1, 'bstr'),)))
    ITextFont.GetOutline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(38, 'GetOutline', ((1, 'pValue'),)))
    ITextFont.SetOutline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(39, 'SetOutline', ((1, 'Value'),)))
    ITextFont.GetPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(40, 'GetPosition', ((1, 'pValue'),)))
    ITextFont.SetPosition = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(41, 'SetPosition', ((1, 'Value'),)))
    ITextFont.GetProtected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(42, 'GetProtected', ((1, 'pValue'),)))
    ITextFont.SetProtected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(43, 'SetProtected', ((1, 'Value'),)))
    ITextFont.GetShadow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(44, 'GetShadow', ((1, 'pValue'),)))
    ITextFont.SetShadow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(45, 'SetShadow', ((1, 'Value'),)))
    ITextFont.GetSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(46, 'GetSize', ((1, 'pValue'),)))
    ITextFont.SetSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(47, 'SetSize', ((1, 'Value'),)))
    ITextFont.GetSmallCaps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(48, 'GetSmallCaps', ((1, 'pValue'),)))
    ITextFont.SetSmallCaps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(49, 'SetSmallCaps', ((1, 'Value'),)))
    ITextFont.GetSpacing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(50, 'GetSpacing', ((1, 'pValue'),)))
    ITextFont.SetSpacing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(51, 'SetSpacing', ((1, 'Value'),)))
    ITextFont.GetStrikeThrough = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(52, 'GetStrikeThrough', ((1, 'pValue'),)))
    ITextFont.SetStrikeThrough = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(53, 'SetStrikeThrough', ((1, 'Value'),)))
    ITextFont.GetSubscript = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(54, 'GetSubscript', ((1, 'pValue'),)))
    ITextFont.SetSubscript = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(55, 'SetSubscript', ((1, 'Value'),)))
    ITextFont.GetSuperscript = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(56, 'GetSuperscript', ((1, 'pValue'),)))
    ITextFont.SetSuperscript = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(57, 'SetSuperscript', ((1, 'Value'),)))
    ITextFont.GetUnderline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(58, 'GetUnderline', ((1, 'pValue'),)))
    ITextFont.SetUnderline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(59, 'SetUnderline', ((1, 'Value'),)))
    ITextFont.GetWeight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(60, 'GetWeight', ((1, 'pValue'),)))
    ITextFont.SetWeight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(61, 'SetWeight', ((1, 'Value'),)))
    win32more.System.Com.IDispatch
    return ITextFont
def _define_ITextPara_head():
    class ITextPara(win32more.System.Com.IDispatch_head):
        Guid = Guid('8cc497c4-a1df-11ce-8098-00aa0047be5d')
    return ITextPara
def _define_ITextPara():
    ITextPara = win32more.UI.Controls.RichEdit.ITextPara_head
    ITextPara.GetDuplicate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.ITextPara_head), use_last_error=False)(7, 'GetDuplicate', ((1, 'ppPara'),)))
    ITextPara.SetDuplicate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.RichEdit.ITextPara_head, use_last_error=False)(8, 'SetDuplicate', ((1, 'pPara'),)))
    ITextPara.CanChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'CanChange', ((1, 'pValue'),)))
    ITextPara.IsEqual = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.RichEdit.ITextPara_head,POINTER(Int32), use_last_error=False)(10, 'IsEqual', ((1, 'pPara'),(1, 'pValue'),)))
    ITextPara.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'Reset', ((1, 'Value'),)))
    ITextPara.GetStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(12, 'GetStyle', ((1, 'pValue'),)))
    ITextPara.SetStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(13, 'SetStyle', ((1, 'Value'),)))
    ITextPara.GetAlignment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(14, 'GetAlignment', ((1, 'pValue'),)))
    ITextPara.SetAlignment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(15, 'SetAlignment', ((1, 'Value'),)))
    ITextPara.GetHyphenation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.tomConstants), use_last_error=False)(16, 'GetHyphenation', ((1, 'pValue'),)))
    ITextPara.SetHyphenation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(17, 'SetHyphenation', ((1, 'Value'),)))
    ITextPara.GetFirstLineIndent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(18, 'GetFirstLineIndent', ((1, 'pValue'),)))
    ITextPara.GetKeepTogether = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.tomConstants), use_last_error=False)(19, 'GetKeepTogether', ((1, 'pValue'),)))
    ITextPara.SetKeepTogether = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(20, 'SetKeepTogether', ((1, 'Value'),)))
    ITextPara.GetKeepWithNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.tomConstants), use_last_error=False)(21, 'GetKeepWithNext', ((1, 'pValue'),)))
    ITextPara.SetKeepWithNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(22, 'SetKeepWithNext', ((1, 'Value'),)))
    ITextPara.GetLeftIndent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(23, 'GetLeftIndent', ((1, 'pValue'),)))
    ITextPara.GetLineSpacing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(24, 'GetLineSpacing', ((1, 'pValue'),)))
    ITextPara.GetLineSpacingRule = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(25, 'GetLineSpacingRule', ((1, 'pValue'),)))
    ITextPara.GetListAlignment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(26, 'GetListAlignment', ((1, 'pValue'),)))
    ITextPara.SetListAlignment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(27, 'SetListAlignment', ((1, 'Value'),)))
    ITextPara.GetListLevelIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(28, 'GetListLevelIndex', ((1, 'pValue'),)))
    ITextPara.SetListLevelIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(29, 'SetListLevelIndex', ((1, 'Value'),)))
    ITextPara.GetListStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(30, 'GetListStart', ((1, 'pValue'),)))
    ITextPara.SetListStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(31, 'SetListStart', ((1, 'Value'),)))
    ITextPara.GetListTab = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(32, 'GetListTab', ((1, 'pValue'),)))
    ITextPara.SetListTab = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(33, 'SetListTab', ((1, 'Value'),)))
    ITextPara.GetListType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(34, 'GetListType', ((1, 'pValue'),)))
    ITextPara.SetListType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(35, 'SetListType', ((1, 'Value'),)))
    ITextPara.GetNoLineNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(36, 'GetNoLineNumber', ((1, 'pValue'),)))
    ITextPara.SetNoLineNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(37, 'SetNoLineNumber', ((1, 'Value'),)))
    ITextPara.GetPageBreakBefore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(38, 'GetPageBreakBefore', ((1, 'pValue'),)))
    ITextPara.SetPageBreakBefore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(39, 'SetPageBreakBefore', ((1, 'Value'),)))
    ITextPara.GetRightIndent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(40, 'GetRightIndent', ((1, 'pValue'),)))
    ITextPara.SetRightIndent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(41, 'SetRightIndent', ((1, 'Value'),)))
    ITextPara.SetIndents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Single,Single, use_last_error=False)(42, 'SetIndents', ((1, 'First'),(1, 'Left'),(1, 'Right'),)))
    ITextPara.SetLineSpacing = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Single, use_last_error=False)(43, 'SetLineSpacing', ((1, 'Rule'),(1, 'Spacing'),)))
    ITextPara.GetSpaceAfter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(44, 'GetSpaceAfter', ((1, 'pValue'),)))
    ITextPara.SetSpaceAfter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(45, 'SetSpaceAfter', ((1, 'Value'),)))
    ITextPara.GetSpaceBefore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(46, 'GetSpaceBefore', ((1, 'pValue'),)))
    ITextPara.SetSpaceBefore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(47, 'SetSpaceBefore', ((1, 'Value'),)))
    ITextPara.GetWidowControl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(48, 'GetWidowControl', ((1, 'pValue'),)))
    ITextPara.SetWidowControl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(49, 'SetWidowControl', ((1, 'Value'),)))
    ITextPara.GetTabCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(50, 'GetTabCount', ((1, 'pCount'),)))
    ITextPara.AddTab = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Int32,Int32, use_last_error=False)(51, 'AddTab', ((1, 'tbPos'),(1, 'tbAlign'),(1, 'tbLeader'),)))
    ITextPara.ClearAllTabs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(52, 'ClearAllTabs', ()))
    ITextPara.DeleteTab = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(53, 'DeleteTab', ((1, 'tbPos'),)))
    ITextPara.GetTab = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Single),POINTER(Int32),POINTER(Int32), use_last_error=False)(54, 'GetTab', ((1, 'iTab'),(1, 'ptbPos'),(1, 'ptbAlign'),(1, 'ptbLeader'),)))
    win32more.System.Com.IDispatch
    return ITextPara
def _define_ITextStoryRanges_head():
    class ITextStoryRanges(win32more.System.Com.IDispatch_head):
        Guid = Guid('8cc497c5-a1df-11ce-8098-00aa0047be5d')
    return ITextStoryRanges
def _define_ITextStoryRanges():
    ITextStoryRanges = win32more.UI.Controls.RichEdit.ITextStoryRanges_head
    ITextStoryRanges._NewEnum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, '_NewEnum', ((1, 'ppunkEnum'),)))
    ITextStoryRanges.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.UI.Controls.RichEdit.ITextRange_head), use_last_error=False)(8, 'Item', ((1, 'Index'),(1, 'ppRange'),)))
    ITextStoryRanges.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'GetCount', ((1, 'pCount'),)))
    win32more.System.Com.IDispatch
    return ITextStoryRanges
def _define_ITextDocument2_head():
    class ITextDocument2(win32more.UI.Controls.RichEdit.ITextDocument_head):
        Guid = Guid('c241f5e0-7206-11d8-a2c7-00a0d1d6c6b3')
    return ITextDocument2
def _define_ITextDocument2():
    ITextDocument2 = win32more.UI.Controls.RichEdit.ITextDocument2_head
    ITextDocument2.GetCaretType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(26, 'GetCaretType', ((1, 'pValue'),)))
    ITextDocument2.SetCaretType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(27, 'SetCaretType', ((1, 'Value'),)))
    ITextDocument2.GetDisplays = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.ITextDisplays_head), use_last_error=False)(28, 'GetDisplays', ((1, 'ppDisplays'),)))
    ITextDocument2.GetDocumentFont = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.ITextFont2_head), use_last_error=False)(29, 'GetDocumentFont', ((1, 'ppFont'),)))
    ITextDocument2.SetDocumentFont = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.RichEdit.ITextFont2_head, use_last_error=False)(30, 'SetDocumentFont', ((1, 'pFont'),)))
    ITextDocument2.GetDocumentPara = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.ITextPara2_head), use_last_error=False)(31, 'GetDocumentPara', ((1, 'ppPara'),)))
    ITextDocument2.SetDocumentPara = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.RichEdit.ITextPara2_head, use_last_error=False)(32, 'SetDocumentPara', ((1, 'pPara'),)))
    ITextDocument2.GetEastAsianFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.tomConstants), use_last_error=False)(33, 'GetEastAsianFlags', ((1, 'pFlags'),)))
    ITextDocument2.GetGenerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(34, 'GetGenerator', ((1, 'pbstr'),)))
    ITextDocument2.SetIMEInProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(35, 'SetIMEInProgress', ((1, 'Value'),)))
    ITextDocument2.GetNotificationMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(36, 'GetNotificationMode', ((1, 'pValue'),)))
    ITextDocument2.SetNotificationMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(37, 'SetNotificationMode', ((1, 'Value'),)))
    ITextDocument2.GetSelection2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.ITextSelection2_head), use_last_error=False)(38, 'GetSelection2', ((1, 'ppSel'),)))
    ITextDocument2.GetStoryRanges2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.ITextStoryRanges2_head), use_last_error=False)(39, 'GetStoryRanges2', ((1, 'ppStories'),)))
    ITextDocument2.GetTypographyOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(40, 'GetTypographyOptions', ((1, 'pOptions'),)))
    ITextDocument2.GetVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(41, 'GetVersion', ((1, 'pValue'),)))
    ITextDocument2.GetWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int64), use_last_error=False)(42, 'GetWindow', ((1, 'pHwnd'),)))
    ITextDocument2.AttachMsgFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(43, 'AttachMsgFilter', ((1, 'pFilter'),)))
    ITextDocument2.CheckTextLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int32), use_last_error=False)(44, 'CheckTextLimit', ((1, 'cch'),(1, 'pcch'),)))
    ITextDocument2.GetCallManager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(45, 'GetCallManager', ((1, 'ppVoid'),)))
    ITextDocument2.GetClientRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.RichEdit.tomConstants,POINTER(Int32),POINTER(Int32),POINTER(Int32),POINTER(Int32), use_last_error=False)(46, 'GetClientRect', ((1, 'Type'),(1, 'pLeft'),(1, 'pTop'),(1, 'pRight'),(1, 'pBottom'),)))
    ITextDocument2.GetEffectColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int32), use_last_error=False)(47, 'GetEffectColor', ((1, 'Index'),(1, 'pValue'),)))
    ITextDocument2.GetImmContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int64), use_last_error=False)(48, 'GetImmContext', ((1, 'pContext'),)))
    ITextDocument2.GetPreferredFont = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Int32,Int32,Int32,POINTER(win32more.Foundation.BSTR),POINTER(Int32),POINTER(Int32), use_last_error=False)(49, 'GetPreferredFont', ((1, 'cp'),(1, 'CharRep'),(1, 'Options'),(1, 'curCharRep'),(1, 'curFontSize'),(1, 'pbstr'),(1, 'pPitchAndFamily'),(1, 'pNewFontSize'),)))
    ITextDocument2.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int32), use_last_error=False)(50, 'GetProperty', ((1, 'Type'),(1, 'pValue'),)))
    ITextDocument2.GetStrings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.ITextStrings_head), use_last_error=False)(51, 'GetStrings', ((1, 'ppStrs'),)))
    ITextDocument2.Notify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(52, 'Notify', ((1, 'Notify'),)))
    ITextDocument2.Range2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.UI.Controls.RichEdit.ITextRange2_head), use_last_error=False)(53, 'Range2', ((1, 'cpActive'),(1, 'cpAnchor'),(1, 'ppRange'),)))
    ITextDocument2.RangeFromPoint2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Int32,POINTER(win32more.UI.Controls.RichEdit.ITextRange2_head), use_last_error=False)(54, 'RangeFromPoint2', ((1, 'x'),(1, 'y'),(1, 'Type'),(1, 'ppRange'),)))
    ITextDocument2.ReleaseCallManager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(55, 'ReleaseCallManager', ((1, 'pVoid'),)))
    ITextDocument2.ReleaseImmContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int64, use_last_error=False)(56, 'ReleaseImmContext', ((1, 'Context'),)))
    ITextDocument2.SetEffectColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(57, 'SetEffectColor', ((1, 'Index'),(1, 'Value'),)))
    ITextDocument2.SetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(58, 'SetProperty', ((1, 'Type'),(1, 'Value'),)))
    ITextDocument2.SetTypographyOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(59, 'SetTypographyOptions', ((1, 'Options'),(1, 'Mask'),)))
    ITextDocument2.SysBeep = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(60, 'SysBeep', ()))
    ITextDocument2.Update = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(61, 'Update', ((1, 'Value'),)))
    ITextDocument2.UpdateWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(62, 'UpdateWindow', ()))
    ITextDocument2.GetMathProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(63, 'GetMathProperties', ((1, 'pOptions'),)))
    ITextDocument2.SetMathProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(64, 'SetMathProperties', ((1, 'Options'),(1, 'Mask'),)))
    ITextDocument2.GetActiveStory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.ITextStory_head), use_last_error=False)(65, 'GetActiveStory', ((1, 'ppStory'),)))
    ITextDocument2.SetActiveStory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.RichEdit.ITextStory_head, use_last_error=False)(66, 'SetActiveStory', ((1, 'pStory'),)))
    ITextDocument2.GetMainStory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.ITextStory_head), use_last_error=False)(67, 'GetMainStory', ((1, 'ppStory'),)))
    ITextDocument2.GetNewStory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.ITextStory_head), use_last_error=False)(68, 'GetNewStory', ((1, 'ppStory'),)))
    ITextDocument2.GetStory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.UI.Controls.RichEdit.ITextStory_head), use_last_error=False)(69, 'GetStory', ((1, 'Index'),(1, 'ppStory'),)))
    win32more.UI.Controls.RichEdit.ITextDocument
    return ITextDocument2
def _define_ITextRange2_head():
    class ITextRange2(win32more.UI.Controls.RichEdit.ITextSelection_head):
        Guid = Guid('c241f5e2-7206-11d8-a2c7-00a0d1d6c6b3')
    return ITextRange2
def _define_ITextRange2():
    ITextRange2 = win32more.UI.Controls.RichEdit.ITextRange2_head
    ITextRange2.GetCch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(68, 'GetCch', ((1, 'pcch'),)))
    ITextRange2.GetCells = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(69, 'GetCells', ((1, 'ppCells'),)))
    ITextRange2.GetColumn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(70, 'GetColumn', ((1, 'ppColumn'),)))
    ITextRange2.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(71, 'GetCount', ((1, 'pCount'),)))
    ITextRange2.GetDuplicate2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.ITextRange2_head), use_last_error=False)(72, 'GetDuplicate2', ((1, 'ppRange'),)))
    ITextRange2.GetFont2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.ITextFont2_head), use_last_error=False)(73, 'GetFont2', ((1, 'ppFont'),)))
    ITextRange2.SetFont2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.RichEdit.ITextFont2_head, use_last_error=False)(74, 'SetFont2', ((1, 'pFont'),)))
    ITextRange2.GetFormattedText2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.ITextRange2_head), use_last_error=False)(75, 'GetFormattedText2', ((1, 'ppRange'),)))
    ITextRange2.SetFormattedText2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.RichEdit.ITextRange2_head, use_last_error=False)(76, 'SetFormattedText2', ((1, 'pRange'),)))
    ITextRange2.GetGravity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(77, 'GetGravity', ((1, 'pValue'),)))
    ITextRange2.SetGravity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(78, 'SetGravity', ((1, 'Value'),)))
    ITextRange2.GetPara2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.ITextPara2_head), use_last_error=False)(79, 'GetPara2', ((1, 'ppPara'),)))
    ITextRange2.SetPara2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.RichEdit.ITextPara2_head, use_last_error=False)(80, 'SetPara2', ((1, 'pPara'),)))
    ITextRange2.GetRow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.ITextRow_head), use_last_error=False)(81, 'GetRow', ((1, 'ppRow'),)))
    ITextRange2.GetStartPara = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(82, 'GetStartPara', ((1, 'pValue'),)))
    ITextRange2.GetTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(83, 'GetTable', ((1, 'ppTable'),)))
    ITextRange2.GetURL = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(84, 'GetURL', ((1, 'pbstr'),)))
    ITextRange2.SetURL = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(85, 'SetURL', ((1, 'bstr'),)))
    ITextRange2.AddSubrange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Int32, use_last_error=False)(86, 'AddSubrange', ((1, 'cp1'),(1, 'cp2'),(1, 'Activate'),)))
    ITextRange2.BuildUpMath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(87, 'BuildUpMath', ((1, 'Flags'),)))
    ITextRange2.DeleteSubrange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(88, 'DeleteSubrange', ((1, 'cpFirst'),(1, 'cpLim'),)))
    ITextRange2.Find = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.RichEdit.ITextRange2_head,Int32,Int32,POINTER(Int32), use_last_error=False)(89, 'Find', ((1, 'pRange'),(1, 'Count'),(1, 'Flags'),(1, 'pDelta'),)))
    ITextRange2.GetChar2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),Int32, use_last_error=False)(90, 'GetChar2', ((1, 'pChar'),(1, 'Offset'),)))
    ITextRange2.GetDropCap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),POINTER(Int32), use_last_error=False)(91, 'GetDropCap', ((1, 'pcLine'),(1, 'pPosition'),)))
    ITextRange2.GetInlineObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),POINTER(Int32),POINTER(Int32),POINTER(Int32),POINTER(Int32),POINTER(Int32),POINTER(Int32),POINTER(Int32),POINTER(Int32), use_last_error=False)(92, 'GetInlineObject', ((1, 'pType'),(1, 'pAlign'),(1, 'pChar'),(1, 'pChar1'),(1, 'pChar2'),(1, 'pCount'),(1, 'pTeXStyle'),(1, 'pcCol'),(1, 'pLevel'),)))
    ITextRange2.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int32), use_last_error=False)(93, 'GetProperty', ((1, 'Type'),(1, 'pValue'),)))
    ITextRange2.GetRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int32),POINTER(Int32),POINTER(Int32),POINTER(Int32),POINTER(Int32), use_last_error=False)(94, 'GetRect', ((1, 'Type'),(1, 'pLeft'),(1, 'pTop'),(1, 'pRight'),(1, 'pBottom'),(1, 'pHit'),)))
    ITextRange2.GetSubrange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int32),POINTER(Int32), use_last_error=False)(95, 'GetSubrange', ((1, 'iSubrange'),(1, 'pcpFirst'),(1, 'pcpLim'),)))
    ITextRange2.GetText2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(96, 'GetText2', ((1, 'Flags'),(1, 'pbstr'),)))
    ITextRange2.HexToUnicode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(97, 'HexToUnicode', ()))
    ITextRange2.InsertTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Int32, use_last_error=False)(98, 'InsertTable', ((1, 'cCol'),(1, 'cRow'),(1, 'AutoFit'),)))
    ITextRange2.Linearize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(99, 'Linearize', ((1, 'Flags'),)))
    ITextRange2.SetActiveSubrange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(100, 'SetActiveSubrange', ((1, 'cpAnchor'),(1, 'cpActive'),)))
    ITextRange2.SetDropCap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(101, 'SetDropCap', ((1, 'cLine'),(1, 'Position'),)))
    ITextRange2.SetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(102, 'SetProperty', ((1, 'Type'),(1, 'Value'),)))
    ITextRange2.SetText2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR, use_last_error=False)(103, 'SetText2', ((1, 'Flags'),(1, 'bstr'),)))
    ITextRange2.UnicodeToHex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(104, 'UnicodeToHex', ()))
    ITextRange2.SetInlineObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Int32,Int32,Int32,Int32,Int32,Int32, use_last_error=False)(105, 'SetInlineObject', ((1, 'Type'),(1, 'Align'),(1, 'Char'),(1, 'Char1'),(1, 'Char2'),(1, 'Count'),(1, 'TeXStyle'),(1, 'cCol'),)))
    ITextRange2.GetMathFunctionType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(Int32), use_last_error=False)(106, 'GetMathFunctionType', ((1, 'bstr'),(1, 'pValue'),)))
    ITextRange2.InsertImage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Int32,win32more.Graphics.Gdi.TEXT_ALIGN_OPTIONS,win32more.Foundation.BSTR,win32more.System.Com.IStream_head, use_last_error=False)(107, 'InsertImage', ((1, 'width'),(1, 'height'),(1, 'ascent'),(1, 'Type'),(1, 'bstrAltText'),(1, 'pStream'),)))
    win32more.UI.Controls.RichEdit.ITextSelection
    return ITextRange2
def _define_ITextSelection2_head():
    class ITextSelection2(win32more.UI.Controls.RichEdit.ITextRange2_head):
        Guid = Guid('c241f5e1-7206-11d8-a2c7-00a0d1d6c6b3')
    return ITextSelection2
def _define_ITextSelection2():
    ITextSelection2 = win32more.UI.Controls.RichEdit.ITextSelection2_head
    win32more.UI.Controls.RichEdit.ITextRange2
    return ITextSelection2
def _define_ITextFont2_head():
    class ITextFont2(win32more.UI.Controls.RichEdit.ITextFont_head):
        Guid = Guid('c241f5e3-7206-11d8-a2c7-00a0d1d6c6b3')
    return ITextFont2
def _define_ITextFont2():
    ITextFont2 = win32more.UI.Controls.RichEdit.ITextFont2_head
    ITextFont2.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(62, 'GetCount', ((1, 'pCount'),)))
    ITextFont2.GetAutoLigatures = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(63, 'GetAutoLigatures', ((1, 'pValue'),)))
    ITextFont2.SetAutoLigatures = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(64, 'SetAutoLigatures', ((1, 'Value'),)))
    ITextFont2.GetAutospaceAlpha = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(65, 'GetAutospaceAlpha', ((1, 'pValue'),)))
    ITextFont2.SetAutospaceAlpha = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(66, 'SetAutospaceAlpha', ((1, 'Value'),)))
    ITextFont2.GetAutospaceNumeric = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(67, 'GetAutospaceNumeric', ((1, 'pValue'),)))
    ITextFont2.SetAutospaceNumeric = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(68, 'SetAutospaceNumeric', ((1, 'Value'),)))
    ITextFont2.GetAutospaceParens = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(69, 'GetAutospaceParens', ((1, 'pValue'),)))
    ITextFont2.SetAutospaceParens = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(70, 'SetAutospaceParens', ((1, 'Value'),)))
    ITextFont2.GetCharRep = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(71, 'GetCharRep', ((1, 'pValue'),)))
    ITextFont2.SetCharRep = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(72, 'SetCharRep', ((1, 'Value'),)))
    ITextFont2.GetCompressionMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(73, 'GetCompressionMode', ((1, 'pValue'),)))
    ITextFont2.SetCompressionMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(74, 'SetCompressionMode', ((1, 'Value'),)))
    ITextFont2.GetCookie = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(75, 'GetCookie', ((1, 'pValue'),)))
    ITextFont2.SetCookie = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(76, 'SetCookie', ((1, 'Value'),)))
    ITextFont2.GetDoubleStrike = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(77, 'GetDoubleStrike', ((1, 'pValue'),)))
    ITextFont2.SetDoubleStrike = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(78, 'SetDoubleStrike', ((1, 'Value'),)))
    ITextFont2.GetDuplicate2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.ITextFont2_head), use_last_error=False)(79, 'GetDuplicate2', ((1, 'ppFont'),)))
    ITextFont2.SetDuplicate2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.RichEdit.ITextFont2_head, use_last_error=False)(80, 'SetDuplicate2', ((1, 'pFont'),)))
    ITextFont2.GetLinkType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(81, 'GetLinkType', ((1, 'pValue'),)))
    ITextFont2.GetMathZone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(82, 'GetMathZone', ((1, 'pValue'),)))
    ITextFont2.SetMathZone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(83, 'SetMathZone', ((1, 'Value'),)))
    ITextFont2.GetModWidthPairs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(84, 'GetModWidthPairs', ((1, 'pValue'),)))
    ITextFont2.SetModWidthPairs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(85, 'SetModWidthPairs', ((1, 'Value'),)))
    ITextFont2.GetModWidthSpace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(86, 'GetModWidthSpace', ((1, 'pValue'),)))
    ITextFont2.SetModWidthSpace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(87, 'SetModWidthSpace', ((1, 'Value'),)))
    ITextFont2.GetOldNumbers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(88, 'GetOldNumbers', ((1, 'pValue'),)))
    ITextFont2.SetOldNumbers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(89, 'SetOldNumbers', ((1, 'Value'),)))
    ITextFont2.GetOverlapping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(90, 'GetOverlapping', ((1, 'pValue'),)))
    ITextFont2.SetOverlapping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(91, 'SetOverlapping', ((1, 'Value'),)))
    ITextFont2.GetPositionSubSuper = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(92, 'GetPositionSubSuper', ((1, 'pValue'),)))
    ITextFont2.SetPositionSubSuper = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(93, 'SetPositionSubSuper', ((1, 'Value'),)))
    ITextFont2.GetScaling = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(94, 'GetScaling', ((1, 'pValue'),)))
    ITextFont2.SetScaling = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(95, 'SetScaling', ((1, 'Value'),)))
    ITextFont2.GetSpaceExtension = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single), use_last_error=False)(96, 'GetSpaceExtension', ((1, 'pValue'),)))
    ITextFont2.SetSpaceExtension = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single, use_last_error=False)(97, 'SetSpaceExtension', ((1, 'Value'),)))
    ITextFont2.GetUnderlinePositionMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(98, 'GetUnderlinePositionMode', ((1, 'pValue'),)))
    ITextFont2.SetUnderlinePositionMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(99, 'SetUnderlinePositionMode', ((1, 'Value'),)))
    ITextFont2.GetEffects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),POINTER(Int32), use_last_error=False)(100, 'GetEffects', ((1, 'pValue'),(1, 'pMask'),)))
    ITextFont2.GetEffects2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),POINTER(Int32), use_last_error=False)(101, 'GetEffects2', ((1, 'pValue'),(1, 'pMask'),)))
    ITextFont2.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int32), use_last_error=False)(102, 'GetProperty', ((1, 'Type'),(1, 'pValue'),)))
    ITextFont2.GetPropertyInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int32),POINTER(Int32), use_last_error=False)(103, 'GetPropertyInfo', ((1, 'Index'),(1, 'pType'),(1, 'pValue'),)))
    ITextFont2.IsEqual2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.RichEdit.ITextFont2_head,POINTER(Int32), use_last_error=False)(104, 'IsEqual2', ((1, 'pFont'),(1, 'pB'),)))
    ITextFont2.SetEffects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(105, 'SetEffects', ((1, 'Value'),(1, 'Mask'),)))
    ITextFont2.SetEffects2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(106, 'SetEffects2', ((1, 'Value'),(1, 'Mask'),)))
    ITextFont2.SetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(107, 'SetProperty', ((1, 'Type'),(1, 'Value'),)))
    win32more.UI.Controls.RichEdit.ITextFont
    return ITextFont2
def _define_ITextPara2_head():
    class ITextPara2(win32more.UI.Controls.RichEdit.ITextPara_head):
        Guid = Guid('c241f5e4-7206-11d8-a2c7-00a0d1d6c6b3')
    return ITextPara2
def _define_ITextPara2():
    ITextPara2 = win32more.UI.Controls.RichEdit.ITextPara2_head
    ITextPara2.GetBorders = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(55, 'GetBorders', ((1, 'ppBorders'),)))
    ITextPara2.GetDuplicate2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.ITextPara2_head), use_last_error=False)(56, 'GetDuplicate2', ((1, 'ppPara'),)))
    ITextPara2.SetDuplicate2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.RichEdit.ITextPara2_head, use_last_error=False)(57, 'SetDuplicate2', ((1, 'pPara'),)))
    ITextPara2.GetFontAlignment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(58, 'GetFontAlignment', ((1, 'pValue'),)))
    ITextPara2.SetFontAlignment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(59, 'SetFontAlignment', ((1, 'Value'),)))
    ITextPara2.GetHangingPunctuation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(60, 'GetHangingPunctuation', ((1, 'pValue'),)))
    ITextPara2.SetHangingPunctuation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(61, 'SetHangingPunctuation', ((1, 'Value'),)))
    ITextPara2.GetSnapToGrid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(62, 'GetSnapToGrid', ((1, 'pValue'),)))
    ITextPara2.SetSnapToGrid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(63, 'SetSnapToGrid', ((1, 'Value'),)))
    ITextPara2.GetTrimPunctuationAtStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(64, 'GetTrimPunctuationAtStart', ((1, 'pValue'),)))
    ITextPara2.SetTrimPunctuationAtStart = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(65, 'SetTrimPunctuationAtStart', ((1, 'Value'),)))
    ITextPara2.GetEffects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),POINTER(Int32), use_last_error=False)(66, 'GetEffects', ((1, 'pValue'),(1, 'pMask'),)))
    ITextPara2.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int32), use_last_error=False)(67, 'GetProperty', ((1, 'Type'),(1, 'pValue'),)))
    ITextPara2.IsEqual2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.RichEdit.ITextPara2_head,POINTER(Int32), use_last_error=False)(68, 'IsEqual2', ((1, 'pPara'),(1, 'pB'),)))
    ITextPara2.SetEffects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(69, 'SetEffects', ((1, 'Value'),(1, 'Mask'),)))
    ITextPara2.SetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(70, 'SetProperty', ((1, 'Type'),(1, 'Value'),)))
    win32more.UI.Controls.RichEdit.ITextPara
    return ITextPara2
def _define_ITextStoryRanges2_head():
    class ITextStoryRanges2(win32more.UI.Controls.RichEdit.ITextStoryRanges_head):
        Guid = Guid('c241f5e5-7206-11d8-a2c7-00a0d1d6c6b3')
    return ITextStoryRanges2
def _define_ITextStoryRanges2():
    ITextStoryRanges2 = win32more.UI.Controls.RichEdit.ITextStoryRanges2_head
    ITextStoryRanges2.Item2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.UI.Controls.RichEdit.ITextRange2_head), use_last_error=False)(10, 'Item2', ((1, 'Index'),(1, 'ppRange'),)))
    win32more.UI.Controls.RichEdit.ITextStoryRanges
    return ITextStoryRanges2
def _define_ITextStory_head():
    class ITextStory(win32more.System.Com.IUnknown_head):
        Guid = Guid('c241f5f3-7206-11d8-a2c7-00a0d1d6c6b3')
    return ITextStory
def _define_ITextStory():
    ITextStory = win32more.UI.Controls.RichEdit.ITextStory_head
    ITextStory.GetActive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(3, 'GetActive', ((1, 'pValue'),)))
    ITextStory.SetActive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(4, 'SetActive', ((1, 'Value'),)))
    ITextStory.GetDisplay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(5, 'GetDisplay', ((1, 'ppDisplay'),)))
    ITextStory.GetIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(6, 'GetIndex', ((1, 'pValue'),)))
    ITextStory.GetType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'GetType', ((1, 'pValue'),)))
    ITextStory.SetType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(8, 'SetType', ((1, 'Value'),)))
    ITextStory.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int32), use_last_error=False)(9, 'GetProperty', ((1, 'Type'),(1, 'pValue'),)))
    ITextStory.GetRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.UI.Controls.RichEdit.ITextRange2_head), use_last_error=False)(10, 'GetRange', ((1, 'cpActive'),(1, 'cpAnchor'),(1, 'ppRange'),)))
    ITextStory.GetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(11, 'GetText', ((1, 'Flags'),(1, 'pbstr'),)))
    ITextStory.SetFormattedText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(12, 'SetFormattedText', ((1, 'pUnk'),)))
    ITextStory.SetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(13, 'SetProperty', ((1, 'Type'),(1, 'Value'),)))
    ITextStory.SetText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.BSTR, use_last_error=False)(14, 'SetText', ((1, 'Flags'),(1, 'bstr'),)))
    win32more.System.Com.IUnknown
    return ITextStory
def _define_ITextStrings_head():
    class ITextStrings(win32more.System.Com.IDispatch_head):
        Guid = Guid('c241f5e7-7206-11d8-a2c7-00a0d1d6c6b3')
    return ITextStrings
def _define_ITextStrings():
    ITextStrings = win32more.UI.Controls.RichEdit.ITextStrings_head
    ITextStrings.Item = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.UI.Controls.RichEdit.ITextRange2_head), use_last_error=False)(7, 'Item', ((1, 'Index'),(1, 'ppRange'),)))
    ITextStrings.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(8, 'GetCount', ((1, 'pCount'),)))
    ITextStrings.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(9, 'Add', ((1, 'bstr'),)))
    ITextStrings.Append = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.RichEdit.ITextRange2_head,Int32, use_last_error=False)(10, 'Append', ((1, 'pRange'),(1, 'iString'),)))
    ITextStrings.Cat2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(11, 'Cat2', ((1, 'iString'),)))
    ITextStrings.CatTop2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(12, 'CatTop2', ((1, 'bstr'),)))
    ITextStrings.DeleteRange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.RichEdit.ITextRange2_head, use_last_error=False)(13, 'DeleteRange', ((1, 'pRange'),)))
    ITextStrings.EncodeFunction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Int32,Int32,Int32,Int32,Int32,Int32,win32more.UI.Controls.RichEdit.ITextRange2_head, use_last_error=False)(14, 'EncodeFunction', ((1, 'Type'),(1, 'Align'),(1, 'Char'),(1, 'Char1'),(1, 'Char2'),(1, 'Count'),(1, 'TeXStyle'),(1, 'cCol'),(1, 'pRange'),)))
    ITextStrings.GetCch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int32), use_last_error=False)(15, 'GetCch', ((1, 'iString'),(1, 'pcch'),)))
    ITextStrings.InsertNullStr = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(16, 'InsertNullStr', ((1, 'iString'),)))
    ITextStrings.MoveBoundary = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(17, 'MoveBoundary', ((1, 'iString'),(1, 'cch'),)))
    ITextStrings.PrefixTop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(18, 'PrefixTop', ((1, 'bstr'),)))
    ITextStrings.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(19, 'Remove', ((1, 'iString'),(1, 'cString'),)))
    ITextStrings.SetFormattedText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.RichEdit.ITextRange2_head,win32more.UI.Controls.RichEdit.ITextRange2_head, use_last_error=False)(20, 'SetFormattedText', ((1, 'pRangeD'),(1, 'pRangeS'),)))
    ITextStrings.SetOpCp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(21, 'SetOpCp', ((1, 'iString'),(1, 'cp'),)))
    ITextStrings.SuffixTop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.UI.Controls.RichEdit.ITextRange2_head, use_last_error=False)(22, 'SuffixTop', ((1, 'bstr'),(1, 'pRange'),)))
    ITextStrings.Swap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(23, 'Swap', ()))
    win32more.System.Com.IDispatch
    return ITextStrings
def _define_ITextRow_head():
    class ITextRow(win32more.System.Com.IDispatch_head):
        Guid = Guid('c241f5ef-7206-11d8-a2c7-00a0d1d6c6b3')
    return ITextRow
def _define_ITextRow():
    ITextRow = win32more.UI.Controls.RichEdit.ITextRow_head
    ITextRow.GetAlignment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'GetAlignment', ((1, 'pValue'),)))
    ITextRow.SetAlignment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(8, 'SetAlignment', ((1, 'Value'),)))
    ITextRow.GetCellCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(9, 'GetCellCount', ((1, 'pValue'),)))
    ITextRow.SetCellCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(10, 'SetCellCount', ((1, 'Value'),)))
    ITextRow.GetCellCountCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(11, 'GetCellCountCache', ((1, 'pValue'),)))
    ITextRow.SetCellCountCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(12, 'SetCellCountCache', ((1, 'Value'),)))
    ITextRow.GetCellIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(13, 'GetCellIndex', ((1, 'pValue'),)))
    ITextRow.SetCellIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(14, 'SetCellIndex', ((1, 'Value'),)))
    ITextRow.GetCellMargin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(15, 'GetCellMargin', ((1, 'pValue'),)))
    ITextRow.SetCellMargin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(16, 'SetCellMargin', ((1, 'Value'),)))
    ITextRow.GetHeight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(17, 'GetHeight', ((1, 'pValue'),)))
    ITextRow.SetHeight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(18, 'SetHeight', ((1, 'Value'),)))
    ITextRow.GetIndent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(19, 'GetIndent', ((1, 'pValue'),)))
    ITextRow.SetIndent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(20, 'SetIndent', ((1, 'Value'),)))
    ITextRow.GetKeepTogether = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(21, 'GetKeepTogether', ((1, 'pValue'),)))
    ITextRow.SetKeepTogether = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(22, 'SetKeepTogether', ((1, 'Value'),)))
    ITextRow.GetKeepWithNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(23, 'GetKeepWithNext', ((1, 'pValue'),)))
    ITextRow.SetKeepWithNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(24, 'SetKeepWithNext', ((1, 'Value'),)))
    ITextRow.GetNestLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(25, 'GetNestLevel', ((1, 'pValue'),)))
    ITextRow.GetRTL = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(26, 'GetRTL', ((1, 'pValue'),)))
    ITextRow.SetRTL = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(27, 'SetRTL', ((1, 'Value'),)))
    ITextRow.GetCellAlignment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(28, 'GetCellAlignment', ((1, 'pValue'),)))
    ITextRow.SetCellAlignment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(29, 'SetCellAlignment', ((1, 'Value'),)))
    ITextRow.GetCellColorBack = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(30, 'GetCellColorBack', ((1, 'pValue'),)))
    ITextRow.SetCellColorBack = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(31, 'SetCellColorBack', ((1, 'Value'),)))
    ITextRow.GetCellColorFore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(32, 'GetCellColorFore', ((1, 'pValue'),)))
    ITextRow.SetCellColorFore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(33, 'SetCellColorFore', ((1, 'Value'),)))
    ITextRow.GetCellMergeFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(34, 'GetCellMergeFlags', ((1, 'pValue'),)))
    ITextRow.SetCellMergeFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(35, 'SetCellMergeFlags', ((1, 'Value'),)))
    ITextRow.GetCellShading = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(36, 'GetCellShading', ((1, 'pValue'),)))
    ITextRow.SetCellShading = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(37, 'SetCellShading', ((1, 'Value'),)))
    ITextRow.GetCellVerticalText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(38, 'GetCellVerticalText', ((1, 'pValue'),)))
    ITextRow.SetCellVerticalText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(39, 'SetCellVerticalText', ((1, 'Value'),)))
    ITextRow.GetCellWidth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(40, 'GetCellWidth', ((1, 'pValue'),)))
    ITextRow.SetCellWidth = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(41, 'SetCellWidth', ((1, 'Value'),)))
    ITextRow.GetCellBorderColors = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),POINTER(Int32),POINTER(Int32),POINTER(Int32), use_last_error=False)(42, 'GetCellBorderColors', ((1, 'pcrLeft'),(1, 'pcrTop'),(1, 'pcrRight'),(1, 'pcrBottom'),)))
    ITextRow.GetCellBorderWidths = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),POINTER(Int32),POINTER(Int32),POINTER(Int32), use_last_error=False)(43, 'GetCellBorderWidths', ((1, 'pduLeft'),(1, 'pduTop'),(1, 'pduRight'),(1, 'pduBottom'),)))
    ITextRow.SetCellBorderColors = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Int32,Int32, use_last_error=False)(44, 'SetCellBorderColors', ((1, 'crLeft'),(1, 'crTop'),(1, 'crRight'),(1, 'crBottom'),)))
    ITextRow.SetCellBorderWidths = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Int32,Int32, use_last_error=False)(45, 'SetCellBorderWidths', ((1, 'duLeft'),(1, 'duTop'),(1, 'duRight'),(1, 'duBottom'),)))
    ITextRow.Apply = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.UI.Controls.RichEdit.tomConstants, use_last_error=False)(46, 'Apply', ((1, 'cRow'),(1, 'Flags'),)))
    ITextRow.CanChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(47, 'CanChange', ((1, 'pValue'),)))
    ITextRow.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int32), use_last_error=False)(48, 'GetProperty', ((1, 'Type'),(1, 'pValue'),)))
    ITextRow.Insert = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(49, 'Insert', ((1, 'cRow'),)))
    ITextRow.IsEqual = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Controls.RichEdit.ITextRow_head,POINTER(Int32), use_last_error=False)(50, 'IsEqual', ((1, 'pRow'),(1, 'pB'),)))
    ITextRow.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(51, 'Reset', ((1, 'Value'),)))
    ITextRow.SetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(52, 'SetProperty', ((1, 'Type'),(1, 'Value'),)))
    win32more.System.Com.IDispatch
    return ITextRow
def _define_ITextDisplays_head():
    class ITextDisplays(win32more.System.Com.IDispatch_head):
        Guid = Guid('c241f5f2-7206-11d8-a2c7-00a0d1d6c6b3')
    return ITextDisplays
def _define_ITextDisplays():
    ITextDisplays = win32more.UI.Controls.RichEdit.ITextDisplays_head
    win32more.System.Com.IDispatch
    return ITextDisplays
def _define_ITextDocument2Old_head():
    class ITextDocument2Old(win32more.UI.Controls.RichEdit.ITextDocument_head):
        Guid = Guid('01c25500-4268-11d1-883a-3c8b00c10000')
    return ITextDocument2Old
def _define_ITextDocument2Old():
    ITextDocument2Old = win32more.UI.Controls.RichEdit.ITextDocument2Old_head
    ITextDocument2Old.AttachMsgFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(26, 'AttachMsgFilter', ((1, 'pFilter'),)))
    ITextDocument2Old.SetEffectColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,UInt32, use_last_error=False)(27, 'SetEffectColor', ((1, 'Index'),(1, 'cr'),)))
    ITextDocument2Old.GetEffectColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(UInt32), use_last_error=False)(28, 'GetEffectColor', ((1, 'Index'),(1, 'pcr'),)))
    ITextDocument2Old.GetCaretType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(29, 'GetCaretType', ((1, 'pCaretType'),)))
    ITextDocument2Old.SetCaretType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(30, 'SetCaretType', ((1, 'CaretType'),)))
    ITextDocument2Old.GetImmContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int64), use_last_error=False)(31, 'GetImmContext', ((1, 'pContext'),)))
    ITextDocument2Old.ReleaseImmContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int64, use_last_error=False)(32, 'ReleaseImmContext', ((1, 'Context'),)))
    ITextDocument2Old.GetPreferredFont = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Int32,Int32,Int32,POINTER(win32more.Foundation.BSTR),POINTER(Int32),POINTER(Int32), use_last_error=False)(33, 'GetPreferredFont', ((1, 'cp'),(1, 'CharRep'),(1, 'Option'),(1, 'CharRepCur'),(1, 'curFontSize'),(1, 'pbstr'),(1, 'pPitchAndFamily'),(1, 'pNewFontSize'),)))
    ITextDocument2Old.GetNotificationMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(34, 'GetNotificationMode', ((1, 'pMode'),)))
    ITextDocument2Old.SetNotificationMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(35, 'SetNotificationMode', ((1, 'Mode'),)))
    ITextDocument2Old.GetClientRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int32),POINTER(Int32),POINTER(Int32),POINTER(Int32), use_last_error=False)(36, 'GetClientRect', ((1, 'Type'),(1, 'pLeft'),(1, 'pTop'),(1, 'pRight'),(1, 'pBottom'),)))
    ITextDocument2Old.GetSelection2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.ITextSelection_head), use_last_error=False)(37, 'GetSelection2', ((1, 'ppSel'),)))
    ITextDocument2Old.GetWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(38, 'GetWindow', ((1, 'phWnd'),)))
    ITextDocument2Old.GetFEFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(39, 'GetFEFlags', ((1, 'pFlags'),)))
    ITextDocument2Old.UpdateWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(40, 'UpdateWindow', ()))
    ITextDocument2Old.CheckTextLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int32), use_last_error=False)(41, 'CheckTextLimit', ((1, 'cch'),(1, 'pcch'),)))
    ITextDocument2Old.IMEInProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(42, 'IMEInProgress', ((1, 'Value'),)))
    ITextDocument2Old.SysBeep = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(43, 'SysBeep', ()))
    ITextDocument2Old.Update = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(44, 'Update', ((1, 'Mode'),)))
    ITextDocument2Old.Notify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(45, 'Notify', ((1, 'Notify'),)))
    ITextDocument2Old.GetDocumentFont = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.ITextFont_head), use_last_error=False)(46, 'GetDocumentFont', ((1, 'ppITextFont'),)))
    ITextDocument2Old.GetDocumentPara = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Controls.RichEdit.ITextPara_head), use_last_error=False)(47, 'GetDocumentPara', ((1, 'ppITextPara'),)))
    ITextDocument2Old.GetCallManager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(48, 'GetCallManager', ((1, 'ppVoid'),)))
    ITextDocument2Old.ReleaseCallManager = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(49, 'ReleaseCallManager', ((1, 'pVoid'),)))
    win32more.UI.Controls.RichEdit.ITextDocument
    return ITextDocument2Old
__all__ = [
    "WM_CONTEXTMENU",
    "WM_UNICHAR",
    "WM_PRINTCLIENT",
    "EM_CANPASTE",
    "EM_DISPLAYBAND",
    "EM_EXGETSEL",
    "EM_EXLIMITTEXT",
    "EM_EXLINEFROMCHAR",
    "EM_EXSETSEL",
    "EM_FINDTEXT",
    "EM_FORMATRANGE",
    "EM_GETCHARFORMAT",
    "EM_GETEVENTMASK",
    "EM_GETOLEINTERFACE",
    "EM_GETPARAFORMAT",
    "EM_GETSELTEXT",
    "EM_HIDESELECTION",
    "EM_PASTESPECIAL",
    "EM_REQUESTRESIZE",
    "EM_SELECTIONTYPE",
    "EM_SETBKGNDCOLOR",
    "EM_SETCHARFORMAT",
    "EM_SETEVENTMASK",
    "EM_SETOLECALLBACK",
    "EM_SETPARAFORMAT",
    "EM_SETTARGETDEVICE",
    "EM_STREAMIN",
    "EM_STREAMOUT",
    "EM_GETTEXTRANGE",
    "EM_FINDWORDBREAK",
    "EM_SETOPTIONS",
    "EM_GETOPTIONS",
    "EM_FINDTEXTEX",
    "EM_GETWORDBREAKPROCEX",
    "EM_SETWORDBREAKPROCEX",
    "EM_SETUNDOLIMIT",
    "EM_REDO",
    "EM_CANREDO",
    "EM_GETUNDONAME",
    "EM_GETREDONAME",
    "EM_STOPGROUPTYPING",
    "EM_SETTEXTMODE",
    "EM_GETTEXTMODE",
    "EM_AUTOURLDETECT",
    "AURL_ENABLEURL",
    "AURL_ENABLEEMAILADDR",
    "AURL_ENABLETELNO",
    "AURL_ENABLEEAURLS",
    "AURL_ENABLEDRIVELETTERS",
    "AURL_DISABLEMIXEDLGC",
    "EM_GETAUTOURLDETECT",
    "EM_SETPALETTE",
    "EM_GETTEXTEX",
    "EM_GETTEXTLENGTHEX",
    "EM_SHOWSCROLLBAR",
    "EM_SETTEXTEX",
    "EM_SETPUNCTUATION",
    "EM_GETPUNCTUATION",
    "EM_SETWORDWRAPMODE",
    "EM_GETWORDWRAPMODE",
    "EM_SETIMECOLOR",
    "EM_GETIMECOLOR",
    "EM_SETIMEOPTIONS",
    "EM_GETIMEOPTIONS",
    "EM_CONVPOSITION",
    "EM_SETLANGOPTIONS",
    "EM_GETLANGOPTIONS",
    "EM_GETIMECOMPMODE",
    "EM_FINDTEXTW",
    "EM_FINDTEXTEXW",
    "EM_RECONVERSION",
    "EM_SETIMEMODEBIAS",
    "EM_GETIMEMODEBIAS",
    "EM_SETBIDIOPTIONS",
    "EM_GETBIDIOPTIONS",
    "EM_SETTYPOGRAPHYOPTIONS",
    "EM_GETTYPOGRAPHYOPTIONS",
    "EM_SETEDITSTYLE",
    "EM_GETEDITSTYLE",
    "SES_EMULATESYSEDIT",
    "SES_BEEPONMAXTEXT",
    "SES_EXTENDBACKCOLOR",
    "SES_MAPCPS",
    "SES_HYPERLINKTOOLTIPS",
    "SES_EMULATE10",
    "SES_DEFAULTLATINLIGA",
    "SES_USECRLF",
    "SES_NOFOCUSLINKNOTIFY",
    "SES_USEAIMM",
    "SES_NOIME",
    "SES_ALLOWBEEPS",
    "SES_UPPERCASE",
    "SES_LOWERCASE",
    "SES_NOINPUTSEQUENCECHK",
    "SES_BIDI",
    "SES_SCROLLONKILLFOCUS",
    "SES_XLTCRCRLFTOCR",
    "SES_DRAFTMODE",
    "SES_USECTF",
    "SES_HIDEGRIDLINES",
    "SES_USEATFONT",
    "SES_CUSTOMLOOK",
    "SES_LBSCROLLNOTIFY",
    "SES_CTFALLOWEMBED",
    "SES_CTFALLOWSMARTTAG",
    "SES_CTFALLOWPROOFING",
    "SES_LOGICALCARET",
    "SES_WORDDRAGDROP",
    "SES_SMARTDRAGDROP",
    "SES_MULTISELECT",
    "SES_CTFNOLOCK",
    "SES_NOEALINEHEIGHTADJUST",
    "SES_MAX",
    "IMF_AUTOKEYBOARD",
    "IMF_AUTOFONT",
    "IMF_IMECANCELCOMPLETE",
    "IMF_IMEALWAYSSENDNOTIFY",
    "IMF_AUTOFONTSIZEADJUST",
    "IMF_UIFONTS",
    "IMF_NOIMPLICITLANG",
    "IMF_DUALFONT",
    "IMF_NOKBDLIDFIXUP",
    "IMF_NORTFFONTSUBSTITUTE",
    "IMF_SPELLCHECKING",
    "IMF_TKBPREDICTION",
    "IMF_IMEUIINTEGRATION",
    "ICM_NOTOPEN",
    "ICM_LEVEL3",
    "ICM_LEVEL2",
    "ICM_LEVEL2_5",
    "ICM_LEVEL2_SUI",
    "ICM_CTF",
    "TO_ADVANCEDTYPOGRAPHY",
    "TO_SIMPLELINEBREAK",
    "TO_DISABLECUSTOMTEXTOUT",
    "TO_ADVANCEDLAYOUT",
    "EM_OUTLINE",
    "EM_GETSCROLLPOS",
    "EM_SETSCROLLPOS",
    "EM_SETFONTSIZE",
    "EM_GETZOOM",
    "EM_SETZOOM",
    "EM_GETVIEWKIND",
    "EM_SETVIEWKIND",
    "EM_GETPAGE",
    "EM_SETPAGE",
    "EM_GETHYPHENATEINFO",
    "EM_SETHYPHENATEINFO",
    "EM_GETPAGEROTATE",
    "EM_SETPAGEROTATE",
    "EM_GETCTFMODEBIAS",
    "EM_SETCTFMODEBIAS",
    "EM_GETCTFOPENSTATUS",
    "EM_SETCTFOPENSTATUS",
    "EM_GETIMECOMPTEXT",
    "EM_ISIME",
    "EM_GETIMEPROPERTY",
    "EM_GETQUERYRTFOBJ",
    "EM_SETQUERYRTFOBJ",
    "EPR_0",
    "EPR_270",
    "EPR_180",
    "EPR_90",
    "EPR_SE",
    "CTFMODEBIAS_DEFAULT",
    "CTFMODEBIAS_FILENAME",
    "CTFMODEBIAS_NAME",
    "CTFMODEBIAS_READING",
    "CTFMODEBIAS_DATETIME",
    "CTFMODEBIAS_CONVERSATION",
    "CTFMODEBIAS_NUMERIC",
    "CTFMODEBIAS_HIRAGANA",
    "CTFMODEBIAS_KATAKANA",
    "CTFMODEBIAS_HANGUL",
    "CTFMODEBIAS_HALFWIDTHKATAKANA",
    "CTFMODEBIAS_FULLWIDTHALPHANUMERIC",
    "CTFMODEBIAS_HALFWIDTHALPHANUMERIC",
    "IMF_SMODE_PLAURALCLAUSE",
    "IMF_SMODE_NONE",
    "EMO_EXIT",
    "EMO_ENTER",
    "EMO_PROMOTE",
    "EMO_EXPAND",
    "EMO_MOVESELECTION",
    "EMO_GETVIEWMODE",
    "EMO_EXPANDSELECTION",
    "EMO_EXPANDDOCUMENT",
    "VM_NORMAL",
    "VM_OUTLINE",
    "VM_PAGE",
    "EM_INSERTTABLE",
    "EM_GETAUTOCORRECTPROC",
    "EM_SETAUTOCORRECTPROC",
    "EM_CALLAUTOCORRECTPROC",
    "ATP_NOCHANGE",
    "ATP_CHANGE",
    "ATP_NODELIMITER",
    "ATP_REPLACEALLTEXT",
    "EM_GETTABLEPARMS",
    "EM_SETEDITSTYLEEX",
    "EM_GETEDITSTYLEEX",
    "SES_EX_NOTABLE",
    "SES_EX_NOMATH",
    "SES_EX_HANDLEFRIENDLYURL",
    "SES_EX_NOTHEMING",
    "SES_EX_NOACETATESELECTION",
    "SES_EX_USESINGLELINE",
    "SES_EX_MULTITOUCH",
    "SES_EX_HIDETEMPFORMAT",
    "SES_EX_USEMOUSEWPARAM",
    "EM_GETSTORYTYPE",
    "EM_SETSTORYTYPE",
    "EM_GETELLIPSISMODE",
    "EM_SETELLIPSISMODE",
    "ELLIPSIS_MASK",
    "ELLIPSIS_NONE",
    "ELLIPSIS_END",
    "ELLIPSIS_WORD",
    "EM_SETTABLEPARMS",
    "EM_GETTOUCHOPTIONS",
    "EM_SETTOUCHOPTIONS",
    "EM_INSERTIMAGE",
    "EM_SETUIANAME",
    "EM_GETELLIPSISSTATE",
    "RTO_SHOWHANDLES",
    "RTO_DISABLEHANDLES",
    "RTO_READINGMODE",
    "EN_MSGFILTER",
    "EN_REQUESTRESIZE",
    "EN_SELCHANGE",
    "EN_DROPFILES",
    "EN_PROTECTED",
    "EN_CORRECTTEXT",
    "EN_STOPNOUNDO",
    "EN_IMECHANGE",
    "EN_SAVECLIPBOARD",
    "EN_OLEOPFAILED",
    "EN_OBJECTPOSITIONS",
    "EN_LINK",
    "EN_DRAGDROPDONE",
    "EN_PARAGRAPHEXPANDED",
    "EN_PAGECHANGE",
    "EN_LOWFIRTF",
    "EN_ALIGNLTR",
    "EN_ALIGNRTL",
    "EN_CLIPFORMAT",
    "EN_STARTCOMPOSITION",
    "EN_ENDCOMPOSITION",
    "ENM_NONE",
    "ENM_CHANGE",
    "ENM_UPDATE",
    "ENM_SCROLL",
    "ENM_SCROLLEVENTS",
    "ENM_DRAGDROPDONE",
    "ENM_PARAGRAPHEXPANDED",
    "ENM_PAGECHANGE",
    "ENM_CLIPFORMAT",
    "ENM_KEYEVENTS",
    "ENM_MOUSEEVENTS",
    "ENM_REQUESTRESIZE",
    "ENM_SELCHANGE",
    "ENM_DROPFILES",
    "ENM_PROTECTED",
    "ENM_CORRECTTEXT",
    "ENM_IMECHANGE",
    "ENM_LANGCHANGE",
    "ENM_OBJECTPOSITIONS",
    "ENM_LINK",
    "ENM_LOWFIRTF",
    "ENM_STARTCOMPOSITION",
    "ENM_ENDCOMPOSITION",
    "ENM_GROUPTYPINGCHANGE",
    "ENM_HIDELINKTOOLTIP",
    "ES_SAVESEL",
    "ES_SUNKEN",
    "ES_DISABLENOSCROLL",
    "ES_SELECTIONBAR",
    "ES_NOOLEDRAGDROP",
    "ES_EX_NOCALLOLEINIT",
    "ES_VERTICAL",
    "ES_NOIME",
    "ES_SELFIME",
    "ECO_AUTOWORDSELECTION",
    "ECO_AUTOVSCROLL",
    "ECO_AUTOHSCROLL",
    "ECO_NOHIDESEL",
    "ECO_READONLY",
    "ECO_WANTRETURN",
    "ECO_SAVESEL",
    "ECO_SELECTIONBAR",
    "ECO_VERTICAL",
    "ECOOP_SET",
    "ECOOP_OR",
    "ECOOP_AND",
    "ECOOP_XOR",
    "WB_MOVEWORDPREV",
    "WB_MOVEWORDNEXT",
    "WB_PREVBREAK",
    "WB_NEXTBREAK",
    "PC_FOLLOWING",
    "PC_LEADING",
    "PC_OVERFLOW",
    "PC_DELIMITER",
    "WBF_WORDWRAP",
    "WBF_WORDBREAK",
    "WBF_OVERFLOW",
    "WBF_LEVEL1",
    "WBF_LEVEL2",
    "WBF_CUSTOM",
    "IMF_FORCENONE",
    "IMF_FORCEENABLE",
    "IMF_FORCEDISABLE",
    "IMF_CLOSESTATUSWINDOW",
    "IMF_VERTICAL",
    "IMF_FORCEACTIVE",
    "IMF_FORCEINACTIVE",
    "IMF_FORCEREMEMBER",
    "IMF_MULTIPLEEDIT",
    "SCF_SELECTION",
    "SCF_WORD",
    "SCF_DEFAULT",
    "SCF_ALL",
    "SCF_USEUIRULES",
    "SCF_ASSOCIATEFONT",
    "SCF_NOKBUPDATE",
    "SCF_ASSOCIATEFONT2",
    "SCF_SMARTFONT",
    "SCF_CHARREPFROMLCID",
    "SPF_DONTSETDEFAULT",
    "SPF_SETDEFAULT",
    "SF_TEXT",
    "SF_RTF",
    "SF_RTFNOOBJS",
    "SF_TEXTIZED",
    "SF_UNICODE",
    "SF_USECODEPAGE",
    "SF_NCRFORNONASCII",
    "SFF_WRITEXTRAPAR",
    "SFF_SELECTION",
    "SFF_PLAINRTF",
    "SFF_PERSISTVIEWSCALE",
    "SFF_KEEPDOCINFO",
    "SFF_PWD",
    "SF_RTFVAL",
    "MAX_TAB_STOPS",
    "MAX_TABLE_CELLS",
    "PFM_SPACEBEFORE",
    "PFM_SPACEAFTER",
    "PFM_LINESPACING",
    "PFM_STYLE",
    "PFM_BORDER",
    "PFM_SHADING",
    "PFM_NUMBERINGSTYLE",
    "PFM_NUMBERINGTAB",
    "PFM_NUMBERINGSTART",
    "PFM_KEEP",
    "PFM_KEEPNEXT",
    "PFM_PAGEBREAKBEFORE",
    "PFM_NOLINENUMBER",
    "PFM_NOWIDOWCONTROL",
    "PFM_DONOTHYPHEN",
    "PFM_SIDEBYSIDE",
    "PFM_COLLAPSED",
    "PFM_OUTLINELEVEL",
    "PFM_BOX",
    "PFM_RESERVED2",
    "PFM_TABLEROWDELIMITER",
    "PFM_TEXTWRAPPINGBREAK",
    "PFM_TABLE",
    "PFN_BULLET",
    "PFN_ARABIC",
    "PFN_LCLETTER",
    "PFN_UCLETTER",
    "PFN_LCROMAN",
    "PFN_UCROMAN",
    "PFA_JUSTIFY",
    "PFA_FULL_INTERWORD",
    "WM_NOTIFY",
    "GCMF_GRIPPER",
    "GCMF_SPELLING",
    "GCMF_TOUCHMENU",
    "GCMF_MOUSEMENU",
    "OLEOP_DOVERB",
    "ST_DEFAULT",
    "ST_KEEPUNDO",
    "ST_SELECTION",
    "ST_NEWCHARS",
    "ST_UNICODE",
    "BOM_DEFPARADIR",
    "BOM_PLAINTEXT",
    "BOM_NEUTRALOVERRIDE",
    "BOM_CONTEXTREADING",
    "BOM_CONTEXTALIGNMENT",
    "BOM_LEGACYBIDICLASS",
    "BOM_UNICODEBIDI",
    "BOE_RTLDIR",
    "BOE_PLAINTEXT",
    "BOE_NEUTRALOVERRIDE",
    "BOE_CONTEXTREADING",
    "BOE_CONTEXTALIGNMENT",
    "BOE_FORCERECALC",
    "BOE_LEGACYBIDICLASS",
    "BOE_UNICODEBIDI",
    "FR_MATCHDIAC",
    "FR_MATCHKASHIDA",
    "FR_MATCHALEFHAMZA",
    "PFA_FULL_NEWSPAPER",
    "PFA_FULL_INTERLETTER",
    "PFA_FULL_SCALED",
    "PFA_FULL_GLYPHS",
    "AURL_ENABLEEA",
    "GCM_TOUCHMENU",
    "GCM_MOUSEMENU",
    "S_MSG_KEY_IGNORED",
    "TXTBIT_RICHTEXT",
    "TXTBIT_MULTILINE",
    "TXTBIT_READONLY",
    "TXTBIT_SHOWACCELERATOR",
    "TXTBIT_USEPASSWORD",
    "TXTBIT_HIDESELECTION",
    "TXTBIT_SAVESELECTION",
    "TXTBIT_AUTOWORDSEL",
    "TXTBIT_VERTICAL",
    "TXTBIT_SELBARCHANGE",
    "TXTBIT_WORDWRAP",
    "TXTBIT_ALLOWBEEP",
    "TXTBIT_DISABLEDRAG",
    "TXTBIT_VIEWINSETCHANGE",
    "TXTBIT_BACKSTYLECHANGE",
    "TXTBIT_MAXLENGTHCHANGE",
    "TXTBIT_SCROLLBARCHANGE",
    "TXTBIT_CHARFORMATCHANGE",
    "TXTBIT_PARAFORMATCHANGE",
    "TXTBIT_EXTENTCHANGE",
    "TXTBIT_CLIENTRECTCHANGE",
    "TXTBIT_USECURRENTBKG",
    "TXTBIT_NOTHREADREFCOUNT",
    "TXTBIT_SHOWPASSWORD",
    "TXTBIT_D2DDWRITE",
    "TXTBIT_D2DSIMPLETYPOGRAPHY",
    "TXTBIT_D2DPIXELSNAPPED",
    "TXTBIT_D2DSUBPIXELLINES",
    "TXTBIT_FLASHLASTPASSWORDCHAR",
    "TXTBIT_ADVANCEDINPUT",
    "TXES_ISDIALOG",
    "REO_NULL",
    "REO_READWRITEMASK",
    "RECO_PASTE",
    "RECO_DROP",
    "RECO_COPY",
    "RECO_CUT",
    "RECO_DRAG",
    "CFM_MASK",
    "CFM_SUBSCRIPT",
    "CFM_SUPERSCRIPT",
    "CFM_EFFECTS",
    "CFM_ALL",
    "CFM_BOLD",
    "CFM_CHARSET",
    "CFM_COLOR",
    "CFM_FACE",
    "CFM_ITALIC",
    "CFM_OFFSET",
    "CFM_PROTECTED",
    "CFM_SIZE",
    "CFM_STRIKEOUT",
    "CFM_UNDERLINE",
    "CFM_LINK",
    "CFM_SMALLCAPS",
    "CFM_ALLCAPS",
    "CFM_HIDDEN",
    "CFM_OUTLINE",
    "CFM_SHADOW",
    "CFM_EMBOSS",
    "CFM_IMPRINT",
    "CFM_DISABLED",
    "CFM_REVISED",
    "CFM_REVAUTHOR",
    "CFM_ANIMATION",
    "CFM_STYLE",
    "CFM_KERNING",
    "CFM_SPACING",
    "CFM_WEIGHT",
    "CFM_UNDERLINETYPE",
    "CFM_COOKIE",
    "CFM_LCID",
    "CFM_BACKCOLOR",
    "CFM_EFFECTS2",
    "CFM_ALL2",
    "CFM_FONTBOUND",
    "CFM_LINKPROTECTED",
    "CFM_EXTENDED",
    "CFM_MATHNOBUILDUP",
    "CFM_MATH",
    "CFM_MATHORDINARY",
    "CFM_ALLEFFECTS",
    "CFE_EFFECTS",
    "CFE_ALLCAPS",
    "CFE_AUTOBACKCOLOR",
    "CFE_DISABLED",
    "CFE_EMBOSS",
    "CFE_HIDDEN",
    "CFE_IMPRINT",
    "CFE_OUTLINE",
    "CFE_REVISED",
    "CFE_SHADOW",
    "CFE_SMALLCAPS",
    "CFE_AUTOCOLOR",
    "CFE_BOLD",
    "CFE_ITALIC",
    "CFE_STRIKEOUT",
    "CFE_UNDERLINE",
    "CFE_PROTECTED",
    "CFE_LINK",
    "CFE_SUBSCRIPT",
    "CFE_SUPERSCRIPT",
    "CFE_FONTBOUND",
    "CFE_LINKPROTECTED",
    "CFE_EXTENDED",
    "CFE_MATHNOBUILDUP",
    "CFE_MATH",
    "CFE_MATHORDINARY",
    "PARAFORMAT_MASK",
    "PFM_ALIGNMENT",
    "PFM_NUMBERING",
    "PFM_OFFSET",
    "PFM_OFFSETINDENT",
    "PFM_RIGHTINDENT",
    "PFM_RTLPARA",
    "PFM_STARTINDENT",
    "PFM_TABSTOPS",
    "RICH_EDIT_GET_CONTEXT_MENU_SEL_TYPE",
    "SEL_EMPTY",
    "SEL_TEXT",
    "SEL_OBJECT",
    "SEL_MULTICHAR",
    "SEL_MULTIOBJECT",
    "GCM_RIGHTMOUSEDROP",
    "RICH_EDIT_GET_OBJECT_FLAGS",
    "REO_GETOBJ_POLEOBJ",
    "REO_GETOBJ_PSTG",
    "REO_GETOBJ_POLESITE",
    "REO_GETOBJ_NO_INTERFACES",
    "REO_GETOBJ_ALL_INTERFACES",
    "PARAFORMAT_BORDERS",
    "PARAFORMAT_BORDERS_LEFT",
    "PARAFORMAT_BORDERS_RIGHT",
    "PARAFORMAT_BORDERS_TOP",
    "PARAFORMAT_BORDERS_BOTTOM",
    "PARAFORMAT_BORDERS_INSIDE",
    "PARAFORMAT_BORDERS_OUTSIDE",
    "PARAFORMAT_BORDERS_AUTOCOLOR",
    "PARAFORMAT_SHADING_STYLE",
    "PARAFORMAT_SHADING_STYLE_NONE",
    "PARAFORMAT_SHADING_STYLE_DARK_HORIZ",
    "PARAFORMAT_SHADING_STYLE_DARK_VERT",
    "PARAFORMAT_SHADING_STYLE_DARK_DOWN_DIAG",
    "PARAFORMAT_SHADING_STYLE_DARK_UP_DIAG",
    "PARAFORMAT_SHADING_STYLE_DARK_GRID",
    "PARAFORMAT_SHADING_STYLE_DARK_TRELLIS",
    "PARAFORMAT_SHADING_STYLE_LIGHT_HORZ",
    "PARAFORMAT_SHADING_STYLE_LIGHT_VERT",
    "PARAFORMAT_SHADING_STYLE_LIGHT_DOWN_DIAG",
    "PARAFORMAT_SHADING_STYLE_LIGHT_UP_DIAG",
    "PARAFORMAT_SHADING_STYLE_LIGHT_GRID",
    "PARAFORMAT_SHADING_STYLE_LIGHT_TRELLIS",
    "GETTEXTEX_FLAGS",
    "GT_DEFAULT",
    "GT_NOHIDDENTEXT",
    "GT_RAWTEXT",
    "GT_SELECTION",
    "GT_USECRLF",
    "ENDCOMPOSITIONNOTIFY_CODE",
    "ECN_ENDCOMPOSITION",
    "ECN_NEWTEXT",
    "IMECOMPTEXT_FLAGS",
    "ICT_RESULTREADSTR",
    "GETTEXTLENGTHEX_FLAGS",
    "GTL_DEFAULT",
    "GTL_USECRLF",
    "GTL_PRECISE",
    "GTL_CLOSE",
    "GTL_NUMCHARS",
    "GTL_NUMBYTES",
    "REOBJECT_FLAGS",
    "REO_ALIGNTORIGHT",
    "REO_BELOWBASELINE",
    "REO_BLANK",
    "REO_CANROTATE",
    "REO_DONTNEEDPALETTE",
    "REO_DYNAMICSIZE",
    "REO_GETMETAFILE",
    "REO_HILITED",
    "REO_INPLACEACTIVE",
    "REO_INVERTEDSELECT",
    "REO_LINK",
    "REO_LINKAVAILABLE",
    "REO_OPEN",
    "REO_OWNERDRAWSELECT",
    "REO_RESIZABLE",
    "REO_SELECTED",
    "REO_STATIC",
    "REO_USEASBACKGROUND",
    "REO_WRAPTEXTAROUND",
    "PARAFORMAT_NUMBERING_STYLE",
    "PFNS_PAREN",
    "PFNS_PARENS",
    "PFNS_PERIOD",
    "PFNS_PLAIN",
    "PFNS_NONUMBER",
    "PFNS_NEWNUMBER",
    "PARAFORMAT_ALIGNMENT",
    "PFA_CENTER",
    "PFA_LEFT",
    "PFA_RIGHT",
    "TEXTMODE",
    "TM_PLAINTEXT",
    "TM_RICHTEXT",
    "TM_SINGLELEVELUNDO",
    "TM_MULTILEVELUNDO",
    "TM_SINGLECODEPAGE",
    "TM_MULTICODEPAGE",
    "IMECOMPTEXT",
    "TABLEROWPARMS",
    "TABLECELLPARMS",
    "AutoCorrectProc",
    "RICHEDIT_IMAGE_PARAMETERS",
    "ENDCOMPOSITIONNOTIFY",
    "EDITWORDBREAKPROCEX",
    "CHARFORMATA",
    "CHARFORMATW",
    "CHARFORMAT2W",
    "CHARFORMAT2A",
    "CHARRANGE",
    "TEXTRANGEA",
    "TEXTRANGEW",
    "EDITSTREAMCALLBACK",
    "EDITSTREAM",
    "FINDTEXTA",
    "FINDTEXTW",
    "FINDTEXTEXA",
    "FINDTEXTEXW",
    "FORMATRANGE",
    "PARAFORMAT",
    "PARAFORMAT2",
    "MSGFILTER",
    "REQRESIZE",
    "SELCHANGE",
    "_grouptypingchange",
    "CLIPBOARDFORMAT",
    "GETCONTEXTMENUEX",
    "ENDROPFILES",
    "ENPROTECTED",
    "ENSAVECLIPBOARD",
    "ENOLEOPFAILED",
    "OBJECTPOSITIONS",
    "ENLINK",
    "ENLOWFIRTF",
    "ENCORRECTTEXT",
    "PUNCTUATION",
    "COMPCOLOR",
    "REPASTESPECIAL",
    "UNDONAMEID",
    "UID_UNKNOWN",
    "UID_TYPING",
    "UID_DELETE",
    "UID_DRAGDROP",
    "UID_CUT",
    "UID_PASTE",
    "UID_AUTOTABLE",
    "SETTEXTEX",
    "GETTEXTEX",
    "GETTEXTLENGTHEX",
    "BIDIOPTIONS",
    "KHYPH",
    "KHYPH_khyphNil",
    "KHYPH_khyphNormal",
    "KHYPH_khyphAddBefore",
    "KHYPH_khyphChangeBefore",
    "KHYPH_khyphDeleteBefore",
    "KHYPH_khyphChangeAfter",
    "KHYPH_khyphDelAndChange",
    "hyphresult",
    "HYPHENATEINFO",
    "TXTBACKSTYLE",
    "TXTBACK_TRANSPARENT",
    "TXTBACK_OPAQUE",
    "TXTHITRESULT",
    "TXTHITRESULT_NOHIT",
    "TXTHITRESULT_TRANSPARENT",
    "TXTHITRESULT_CLOSE",
    "TXTHITRESULT_HIT",
    "TXTNATURALSIZE",
    "TXTNS_FITTOCONTENT2",
    "TXTNS_FITTOCONTENT",
    "TXTNS_ROUNDTOLINE",
    "TXTNS_FITTOCONTENT3",
    "TXTNS_FITTOCONTENTWSP",
    "TXTNS_INCLUDELASTLINE",
    "TXTNS_EMU",
    "TXTVIEW",
    "TXTVIEW_ACTIVE",
    "TXTVIEW_INACTIVE",
    "CHANGETYPE",
    "CN_GENERIC",
    "CN_TEXTCHANGED",
    "CN_NEWUNDO",
    "CN_NEWREDO",
    "CHANGENOTIFY",
    "ITextServices",
    "CARET_FLAGS",
    "CARET_NONE",
    "CARET_CUSTOM",
    "CARET_RTL",
    "CARET_ITALIC",
    "CARET_NULL",
    "CARET_ROTATE90",
    "CARET_INFO",
    "ITextHost",
    "IRicheditUiaOverrides",
    "PCreateTextServices",
    "PShutdownTextServices",
    "ITextHost2",
    "ITextServices2",
    "REOBJECT",
    "IRichEditOle",
    "IRichEditOleCallback",
    "tomConstants",
    "tomConstants_tomFalse",
    "tomConstants_tomTrue",
    "tomConstants_tomUndefined",
    "tomConstants_tomToggle",
    "tomConstants_tomAutoColor",
    "tomConstants_tomDefault",
    "tomConstants_tomSuspend",
    "tomConstants_tomResume",
    "tomConstants_tomApplyNow",
    "tomConstants_tomApplyLater",
    "tomConstants_tomTrackParms",
    "tomConstants_tomCacheParms",
    "tomConstants_tomApplyTmp",
    "tomConstants_tomDisableSmartFont",
    "tomConstants_tomEnableSmartFont",
    "tomConstants_tomUsePoints",
    "tomConstants_tomUseTwips",
    "tomConstants_tomBackward",
    "tomConstants_tomForward",
    "tomConstants_tomMove",
    "tomConstants_tomExtend",
    "tomConstants_tomNoSelection",
    "tomConstants_tomSelectionIP",
    "tomConstants_tomSelectionNormal",
    "tomConstants_tomSelectionFrame",
    "tomConstants_tomSelectionColumn",
    "tomConstants_tomSelectionRow",
    "tomConstants_tomSelectionBlock",
    "tomConstants_tomSelectionInlineShape",
    "tomConstants_tomSelectionShape",
    "tomConstants_tomSelStartActive",
    "tomConstants_tomSelAtEOL",
    "tomConstants_tomSelOvertype",
    "tomConstants_tomSelActive",
    "tomConstants_tomSelReplace",
    "tomConstants_tomEnd",
    "tomConstants_tomStart",
    "tomConstants_tomCollapseEnd",
    "tomConstants_tomCollapseStart",
    "tomConstants_tomClientCoord",
    "tomConstants_tomAllowOffClient",
    "tomConstants_tomTransform",
    "tomConstants_tomObjectArg",
    "tomConstants_tomAtEnd",
    "tomConstants_tomNone",
    "tomConstants_tomSingle",
    "tomConstants_tomWords",
    "tomConstants_tomDouble",
    "tomConstants_tomDotted",
    "tomConstants_tomDash",
    "tomConstants_tomDashDot",
    "tomConstants_tomDashDotDot",
    "tomConstants_tomWave",
    "tomConstants_tomThick",
    "tomConstants_tomHair",
    "tomConstants_tomDoubleWave",
    "tomConstants_tomHeavyWave",
    "tomConstants_tomLongDash",
    "tomConstants_tomThickDash",
    "tomConstants_tomThickDashDot",
    "tomConstants_tomThickDashDotDot",
    "tomConstants_tomThickDotted",
    "tomConstants_tomThickLongDash",
    "tomConstants_tomLineSpaceSingle",
    "tomConstants_tomLineSpace1pt5",
    "tomConstants_tomLineSpaceDouble",
    "tomConstants_tomLineSpaceAtLeast",
    "tomConstants_tomLineSpaceExactly",
    "tomConstants_tomLineSpaceMultiple",
    "tomConstants_tomLineSpacePercent",
    "tomConstants_tomAlignLeft",
    "tomConstants_tomAlignCenter",
    "tomConstants_tomAlignRight",
    "tomConstants_tomAlignJustify",
    "tomConstants_tomAlignDecimal",
    "tomConstants_tomAlignBar",
    "tomConstants_tomDefaultTab",
    "tomConstants_tomAlignInterWord",
    "tomConstants_tomAlignNewspaper",
    "tomConstants_tomAlignInterLetter",
    "tomConstants_tomAlignScaled",
    "tomConstants_tomSpaces",
    "tomConstants_tomDots",
    "tomConstants_tomDashes",
    "tomConstants_tomLines",
    "tomConstants_tomThickLines",
    "tomConstants_tomEquals",
    "tomConstants_tomTabBack",
    "tomConstants_tomTabNext",
    "tomConstants_tomTabHere",
    "tomConstants_tomListNone",
    "tomConstants_tomListBullet",
    "tomConstants_tomListNumberAsArabic",
    "tomConstants_tomListNumberAsLCLetter",
    "tomConstants_tomListNumberAsUCLetter",
    "tomConstants_tomListNumberAsLCRoman",
    "tomConstants_tomListNumberAsUCRoman",
    "tomConstants_tomListNumberAsSequence",
    "tomConstants_tomListNumberedCircle",
    "tomConstants_tomListNumberedBlackCircleWingding",
    "tomConstants_tomListNumberedWhiteCircleWingding",
    "tomConstants_tomListNumberedArabicWide",
    "tomConstants_tomListNumberedChS",
    "tomConstants_tomListNumberedChT",
    "tomConstants_tomListNumberedJpnChS",
    "tomConstants_tomListNumberedJpnKor",
    "tomConstants_tomListNumberedArabic1",
    "tomConstants_tomListNumberedArabic2",
    "tomConstants_tomListNumberedHebrew",
    "tomConstants_tomListNumberedThaiAlpha",
    "tomConstants_tomListNumberedThaiNum",
    "tomConstants_tomListNumberedHindiAlpha",
    "tomConstants_tomListNumberedHindiAlpha1",
    "tomConstants_tomListNumberedHindiNum",
    "tomConstants_tomListParentheses",
    "tomConstants_tomListPeriod",
    "tomConstants_tomListPlain",
    "tomConstants_tomListNoNumber",
    "tomConstants_tomListMinus",
    "tomConstants_tomIgnoreNumberStyle",
    "tomConstants_tomParaStyleNormal",
    "tomConstants_tomParaStyleHeading1",
    "tomConstants_tomParaStyleHeading2",
    "tomConstants_tomParaStyleHeading3",
    "tomConstants_tomParaStyleHeading4",
    "tomConstants_tomParaStyleHeading5",
    "tomConstants_tomParaStyleHeading6",
    "tomConstants_tomParaStyleHeading7",
    "tomConstants_tomParaStyleHeading8",
    "tomConstants_tomParaStyleHeading9",
    "tomConstants_tomCharacter",
    "tomConstants_tomWord",
    "tomConstants_tomSentence",
    "tomConstants_tomParagraph",
    "tomConstants_tomLine",
    "tomConstants_tomStory",
    "tomConstants_tomScreen",
    "tomConstants_tomSection",
    "tomConstants_tomTableColumn",
    "tomConstants_tomColumn",
    "tomConstants_tomRow",
    "tomConstants_tomWindow",
    "tomConstants_tomCell",
    "tomConstants_tomCharFormat",
    "tomConstants_tomParaFormat",
    "tomConstants_tomTable",
    "tomConstants_tomObject",
    "tomConstants_tomPage",
    "tomConstants_tomHardParagraph",
    "tomConstants_tomCluster",
    "tomConstants_tomInlineObject",
    "tomConstants_tomInlineObjectArg",
    "tomConstants_tomLeafLine",
    "tomConstants_tomLayoutColumn",
    "tomConstants_tomProcessId",
    "tomConstants_tomMatchWord",
    "tomConstants_tomMatchCase",
    "tomConstants_tomMatchPattern",
    "tomConstants_tomUnknownStory",
    "tomConstants_tomMainTextStory",
    "tomConstants_tomFootnotesStory",
    "tomConstants_tomEndnotesStory",
    "tomConstants_tomCommentsStory",
    "tomConstants_tomTextFrameStory",
    "tomConstants_tomEvenPagesHeaderStory",
    "tomConstants_tomPrimaryHeaderStory",
    "tomConstants_tomEvenPagesFooterStory",
    "tomConstants_tomPrimaryFooterStory",
    "tomConstants_tomFirstPageHeaderStory",
    "tomConstants_tomFirstPageFooterStory",
    "tomConstants_tomScratchStory",
    "tomConstants_tomFindStory",
    "tomConstants_tomReplaceStory",
    "tomConstants_tomStoryInactive",
    "tomConstants_tomStoryActiveDisplay",
    "tomConstants_tomStoryActiveUI",
    "tomConstants_tomStoryActiveDisplayUI",
    "tomConstants_tomNoAnimation",
    "tomConstants_tomLasVegasLights",
    "tomConstants_tomBlinkingBackground",
    "tomConstants_tomSparkleText",
    "tomConstants_tomMarchingBlackAnts",
    "tomConstants_tomMarchingRedAnts",
    "tomConstants_tomShimmer",
    "tomConstants_tomWipeDown",
    "tomConstants_tomWipeRight",
    "tomConstants_tomAnimationMax",
    "tomConstants_tomLowerCase",
    "tomConstants_tomUpperCase",
    "tomConstants_tomTitleCase",
    "tomConstants_tomSentenceCase",
    "tomConstants_tomToggleCase",
    "tomConstants_tomReadOnly",
    "tomConstants_tomShareDenyRead",
    "tomConstants_tomShareDenyWrite",
    "tomConstants_tomPasteFile",
    "tomConstants_tomCreateNew",
    "tomConstants_tomCreateAlways",
    "tomConstants_tomOpenExisting",
    "tomConstants_tomOpenAlways",
    "tomConstants_tomTruncateExisting",
    "tomConstants_tomRTF",
    "tomConstants_tomText",
    "tomConstants_tomHTML",
    "tomConstants_tomWordDocument",
    "tomConstants_tomBold",
    "tomConstants_tomItalic",
    "tomConstants_tomUnderline",
    "tomConstants_tomStrikeout",
    "tomConstants_tomProtected",
    "tomConstants_tomLink",
    "tomConstants_tomSmallCaps",
    "tomConstants_tomAllCaps",
    "tomConstants_tomHidden",
    "tomConstants_tomOutline",
    "tomConstants_tomShadow",
    "tomConstants_tomEmboss",
    "tomConstants_tomImprint",
    "tomConstants_tomDisabled",
    "tomConstants_tomRevised",
    "tomConstants_tomSubscriptCF",
    "tomConstants_tomSuperscriptCF",
    "tomConstants_tomFontBound",
    "tomConstants_tomLinkProtected",
    "tomConstants_tomInlineObjectStart",
    "tomConstants_tomExtendedChar",
    "tomConstants_tomAutoBackColor",
    "tomConstants_tomMathZoneNoBuildUp",
    "tomConstants_tomMathZone",
    "tomConstants_tomMathZoneOrdinary",
    "tomConstants_tomAutoTextColor",
    "tomConstants_tomMathZoneDisplay",
    "tomConstants_tomParaEffectRTL",
    "tomConstants_tomParaEffectKeep",
    "tomConstants_tomParaEffectKeepNext",
    "tomConstants_tomParaEffectPageBreakBefore",
    "tomConstants_tomParaEffectNoLineNumber",
    "tomConstants_tomParaEffectNoWidowControl",
    "tomConstants_tomParaEffectDoNotHyphen",
    "tomConstants_tomParaEffectSideBySide",
    "tomConstants_tomParaEffectCollapsed",
    "tomConstants_tomParaEffectOutlineLevel",
    "tomConstants_tomParaEffectBox",
    "tomConstants_tomParaEffectTableRowDelimiter",
    "tomConstants_tomParaEffectTable",
    "tomConstants_tomModWidthPairs",
    "tomConstants_tomModWidthSpace",
    "tomConstants_tomAutoSpaceAlpha",
    "tomConstants_tomAutoSpaceNumeric",
    "tomConstants_tomAutoSpaceParens",
    "tomConstants_tomEmbeddedFont",
    "tomConstants_tomDoublestrike",
    "tomConstants_tomOverlapping",
    "tomConstants_tomNormalCaret",
    "tomConstants_tomKoreanBlockCaret",
    "tomConstants_tomNullCaret",
    "tomConstants_tomIncludeInset",
    "tomConstants_tomUnicodeBiDi",
    "tomConstants_tomMathCFCheck",
    "tomConstants_tomUnlink",
    "tomConstants_tomUnhide",
    "tomConstants_tomCheckTextLimit",
    "tomConstants_tomIgnoreCurrentFont",
    "tomConstants_tomMatchCharRep",
    "tomConstants_tomMatchFontSignature",
    "tomConstants_tomMatchAscii",
    "tomConstants_tomGetHeightOnly",
    "tomConstants_tomMatchMathFont",
    "tomConstants_tomCharset",
    "tomConstants_tomCharRepFromLcid",
    "tomConstants_tomAnsi",
    "tomConstants_tomEastEurope",
    "tomConstants_tomCyrillic",
    "tomConstants_tomGreek",
    "tomConstants_tomTurkish",
    "tomConstants_tomHebrew",
    "tomConstants_tomArabic",
    "tomConstants_tomBaltic",
    "tomConstants_tomVietnamese",
    "tomConstants_tomDefaultCharRep",
    "tomConstants_tomSymbol",
    "tomConstants_tomThai",
    "tomConstants_tomShiftJIS",
    "tomConstants_tomGB2312",
    "tomConstants_tomHangul",
    "tomConstants_tomBIG5",
    "tomConstants_tomPC437",
    "tomConstants_tomOEM",
    "tomConstants_tomMac",
    "tomConstants_tomArmenian",
    "tomConstants_tomSyriac",
    "tomConstants_tomThaana",
    "tomConstants_tomDevanagari",
    "tomConstants_tomBengali",
    "tomConstants_tomGurmukhi",
    "tomConstants_tomGujarati",
    "tomConstants_tomOriya",
    "tomConstants_tomTamil",
    "tomConstants_tomTelugu",
    "tomConstants_tomKannada",
    "tomConstants_tomMalayalam",
    "tomConstants_tomSinhala",
    "tomConstants_tomLao",
    "tomConstants_tomTibetan",
    "tomConstants_tomMyanmar",
    "tomConstants_tomGeorgian",
    "tomConstants_tomJamo",
    "tomConstants_tomEthiopic",
    "tomConstants_tomCherokee",
    "tomConstants_tomAboriginal",
    "tomConstants_tomOgham",
    "tomConstants_tomRunic",
    "tomConstants_tomKhmer",
    "tomConstants_tomMongolian",
    "tomConstants_tomBraille",
    "tomConstants_tomYi",
    "tomConstants_tomLimbu",
    "tomConstants_tomTaiLe",
    "tomConstants_tomNewTaiLue",
    "tomConstants_tomSylotiNagri",
    "tomConstants_tomKharoshthi",
    "tomConstants_tomKayahli",
    "tomConstants_tomUsymbol",
    "tomConstants_tomEmoji",
    "tomConstants_tomGlagolitic",
    "tomConstants_tomLisu",
    "tomConstants_tomVai",
    "tomConstants_tomNKo",
    "tomConstants_tomOsmanya",
    "tomConstants_tomPhagsPa",
    "tomConstants_tomGothic",
    "tomConstants_tomDeseret",
    "tomConstants_tomTifinagh",
    "tomConstants_tomCharRepMax",
    "tomConstants_tomRE10Mode",
    "tomConstants_tomUseAtFont",
    "tomConstants_tomTextFlowMask",
    "tomConstants_tomTextFlowES",
    "tomConstants_tomTextFlowSW",
    "tomConstants_tomTextFlowWN",
    "tomConstants_tomTextFlowNE",
    "tomConstants_tomNoIME",
    "tomConstants_tomSelfIME",
    "tomConstants_tomNoUpScroll",
    "tomConstants_tomNoVpScroll",
    "tomConstants_tomNoLink",
    "tomConstants_tomClientLink",
    "tomConstants_tomFriendlyLinkName",
    "tomConstants_tomFriendlyLinkAddress",
    "tomConstants_tomAutoLinkURL",
    "tomConstants_tomAutoLinkEmail",
    "tomConstants_tomAutoLinkPhone",
    "tomConstants_tomAutoLinkPath",
    "tomConstants_tomCompressNone",
    "tomConstants_tomCompressPunctuation",
    "tomConstants_tomCompressPunctuationAndKana",
    "tomConstants_tomCompressMax",
    "tomConstants_tomUnderlinePositionAuto",
    "tomConstants_tomUnderlinePositionBelow",
    "tomConstants_tomUnderlinePositionAbove",
    "tomConstants_tomUnderlinePositionMax",
    "tomConstants_tomFontAlignmentAuto",
    "tomConstants_tomFontAlignmentTop",
    "tomConstants_tomFontAlignmentBaseline",
    "tomConstants_tomFontAlignmentBottom",
    "tomConstants_tomFontAlignmentCenter",
    "tomConstants_tomFontAlignmentMax",
    "tomConstants_tomRubyBelow",
    "tomConstants_tomRubyAlignCenter",
    "tomConstants_tomRubyAlign010",
    "tomConstants_tomRubyAlign121",
    "tomConstants_tomRubyAlignLeft",
    "tomConstants_tomRubyAlignRight",
    "tomConstants_tomLimitsDefault",
    "tomConstants_tomLimitsUnderOver",
    "tomConstants_tomLimitsSubSup",
    "tomConstants_tomUpperLimitAsSuperScript",
    "tomConstants_tomLimitsOpposite",
    "tomConstants_tomShowLLimPlaceHldr",
    "tomConstants_tomShowULimPlaceHldr",
    "tomConstants_tomDontGrowWithContent",
    "tomConstants_tomGrowWithContent",
    "tomConstants_tomSubSupAlign",
    "tomConstants_tomLimitAlignMask",
    "tomConstants_tomLimitAlignCenter",
    "tomConstants_tomLimitAlignLeft",
    "tomConstants_tomLimitAlignRight",
    "tomConstants_tomShowDegPlaceHldr",
    "tomConstants_tomAlignDefault",
    "tomConstants_tomAlignMatchAscentDescent",
    "tomConstants_tomMathVariant",
    "tomConstants_tomStyleDefault",
    "tomConstants_tomStyleScriptScriptCramped",
    "tomConstants_tomStyleScriptScript",
    "tomConstants_tomStyleScriptCramped",
    "tomConstants_tomStyleScript",
    "tomConstants_tomStyleTextCramped",
    "tomConstants_tomStyleText",
    "tomConstants_tomStyleDisplayCramped",
    "tomConstants_tomStyleDisplay",
    "tomConstants_tomMathRelSize",
    "tomConstants_tomDecDecSize",
    "tomConstants_tomDecSize",
    "tomConstants_tomIncSize",
    "tomConstants_tomIncIncSize",
    "tomConstants_tomGravityUI",
    "tomConstants_tomGravityBack",
    "tomConstants_tomGravityFore",
    "tomConstants_tomGravityIn",
    "tomConstants_tomGravityOut",
    "tomConstants_tomGravityBackward",
    "tomConstants_tomGravityForward",
    "tomConstants_tomAdjustCRLF",
    "tomConstants_tomUseCRLF",
    "tomConstants_tomTextize",
    "tomConstants_tomAllowFinalEOP",
    "tomConstants_tomFoldMathAlpha",
    "tomConstants_tomNoHidden",
    "tomConstants_tomIncludeNumbering",
    "tomConstants_tomTranslateTableCell",
    "tomConstants_tomNoMathZoneBrackets",
    "tomConstants_tomConvertMathChar",
    "tomConstants_tomNoUCGreekItalic",
    "tomConstants_tomAllowMathBold",
    "tomConstants_tomLanguageTag",
    "tomConstants_tomConvertRTF",
    "tomConstants_tomApplyRtfDocProps",
    "tomConstants_tomPhantomShow",
    "tomConstants_tomPhantomZeroWidth",
    "tomConstants_tomPhantomZeroAscent",
    "tomConstants_tomPhantomZeroDescent",
    "tomConstants_tomPhantomTransparent",
    "tomConstants_tomPhantomASmash",
    "tomConstants_tomPhantomDSmash",
    "tomConstants_tomPhantomHSmash",
    "tomConstants_tomPhantomSmash",
    "tomConstants_tomPhantomHorz",
    "tomConstants_tomPhantomVert",
    "tomConstants_tomBoxHideTop",
    "tomConstants_tomBoxHideBottom",
    "tomConstants_tomBoxHideLeft",
    "tomConstants_tomBoxHideRight",
    "tomConstants_tomBoxStrikeH",
    "tomConstants_tomBoxStrikeV",
    "tomConstants_tomBoxStrikeTLBR",
    "tomConstants_tomBoxStrikeBLTR",
    "tomConstants_tomBoxAlignCenter",
    "tomConstants_tomSpaceMask",
    "tomConstants_tomSpaceDefault",
    "tomConstants_tomSpaceUnary",
    "tomConstants_tomSpaceBinary",
    "tomConstants_tomSpaceRelational",
    "tomConstants_tomSpaceSkip",
    "tomConstants_tomSpaceOrd",
    "tomConstants_tomSpaceDifferential",
    "tomConstants_tomSizeText",
    "tomConstants_tomSizeScript",
    "tomConstants_tomSizeScriptScript",
    "tomConstants_tomNoBreak",
    "tomConstants_tomTransparentForPositioning",
    "tomConstants_tomTransparentForSpacing",
    "tomConstants_tomStretchCharBelow",
    "tomConstants_tomStretchCharAbove",
    "tomConstants_tomStretchBaseBelow",
    "tomConstants_tomStretchBaseAbove",
    "tomConstants_tomMatrixAlignMask",
    "tomConstants_tomMatrixAlignCenter",
    "tomConstants_tomMatrixAlignTopRow",
    "tomConstants_tomMatrixAlignBottomRow",
    "tomConstants_tomShowMatPlaceHldr",
    "tomConstants_tomEqArrayLayoutWidth",
    "tomConstants_tomEqArrayAlignMask",
    "tomConstants_tomEqArrayAlignCenter",
    "tomConstants_tomEqArrayAlignTopRow",
    "tomConstants_tomEqArrayAlignBottomRow",
    "tomConstants_tomMathManualBreakMask",
    "tomConstants_tomMathBreakLeft",
    "tomConstants_tomMathBreakCenter",
    "tomConstants_tomMathBreakRight",
    "tomConstants_tomMathEqAlign",
    "tomConstants_tomMathArgShadingStart",
    "tomConstants_tomMathArgShadingEnd",
    "tomConstants_tomMathObjShadingStart",
    "tomConstants_tomMathObjShadingEnd",
    "tomConstants_tomFunctionTypeNone",
    "tomConstants_tomFunctionTypeTakesArg",
    "tomConstants_tomFunctionTypeTakesLim",
    "tomConstants_tomFunctionTypeTakesLim2",
    "tomConstants_tomFunctionTypeIsLim",
    "tomConstants_tomMathParaAlignDefault",
    "tomConstants_tomMathParaAlignCenterGroup",
    "tomConstants_tomMathParaAlignCenter",
    "tomConstants_tomMathParaAlignLeft",
    "tomConstants_tomMathParaAlignRight",
    "tomConstants_tomMathDispAlignMask",
    "tomConstants_tomMathDispAlignCenterGroup",
    "tomConstants_tomMathDispAlignCenter",
    "tomConstants_tomMathDispAlignLeft",
    "tomConstants_tomMathDispAlignRight",
    "tomConstants_tomMathDispIntUnderOver",
    "tomConstants_tomMathDispFracTeX",
    "tomConstants_tomMathDispNaryGrow",
    "tomConstants_tomMathDocEmptyArgMask",
    "tomConstants_tomMathDocEmptyArgAuto",
    "tomConstants_tomMathDocEmptyArgAlways",
    "tomConstants_tomMathDocEmptyArgNever",
    "tomConstants_tomMathDocSbSpOpUnchanged",
    "tomConstants_tomMathDocDiffMask",
    "tomConstants_tomMathDocDiffDefault",
    "tomConstants_tomMathDocDiffUpright",
    "tomConstants_tomMathDocDiffItalic",
    "tomConstants_tomMathDocDiffOpenItalic",
    "tomConstants_tomMathDispNarySubSup",
    "tomConstants_tomMathDispDef",
    "tomConstants_tomMathEnableRtl",
    "tomConstants_tomMathBrkBinMask",
    "tomConstants_tomMathBrkBinBefore",
    "tomConstants_tomMathBrkBinAfter",
    "tomConstants_tomMathBrkBinDup",
    "tomConstants_tomMathBrkBinSubMask",
    "tomConstants_tomMathBrkBinSubMM",
    "tomConstants_tomMathBrkBinSubPM",
    "tomConstants_tomMathBrkBinSubMP",
    "tomConstants_tomSelRange",
    "tomConstants_tomHstring",
    "tomConstants_tomFontPropTeXStyle",
    "tomConstants_tomFontPropAlign",
    "tomConstants_tomFontStretch",
    "tomConstants_tomFontStyle",
    "tomConstants_tomFontStyleUpright",
    "tomConstants_tomFontStyleOblique",
    "tomConstants_tomFontStyleItalic",
    "tomConstants_tomFontStretchDefault",
    "tomConstants_tomFontStretchUltraCondensed",
    "tomConstants_tomFontStretchExtraCondensed",
    "tomConstants_tomFontStretchCondensed",
    "tomConstants_tomFontStretchSemiCondensed",
    "tomConstants_tomFontStretchNormal",
    "tomConstants_tomFontStretchSemiExpanded",
    "tomConstants_tomFontStretchExpanded",
    "tomConstants_tomFontStretchExtraExpanded",
    "tomConstants_tomFontStretchUltraExpanded",
    "tomConstants_tomFontWeightDefault",
    "tomConstants_tomFontWeightThin",
    "tomConstants_tomFontWeightExtraLight",
    "tomConstants_tomFontWeightLight",
    "tomConstants_tomFontWeightNormal",
    "tomConstants_tomFontWeightRegular",
    "tomConstants_tomFontWeightMedium",
    "tomConstants_tomFontWeightSemiBold",
    "tomConstants_tomFontWeightBold",
    "tomConstants_tomFontWeightExtraBold",
    "tomConstants_tomFontWeightBlack",
    "tomConstants_tomFontWeightHeavy",
    "tomConstants_tomFontWeightExtraBlack",
    "tomConstants_tomParaPropMathAlign",
    "tomConstants_tomDocMathBuild",
    "tomConstants_tomMathLMargin",
    "tomConstants_tomMathRMargin",
    "tomConstants_tomMathWrapIndent",
    "tomConstants_tomMathWrapRight",
    "tomConstants_tomMathPostSpace",
    "tomConstants_tomMathPreSpace",
    "tomConstants_tomMathInterSpace",
    "tomConstants_tomMathIntraSpace",
    "tomConstants_tomCanCopy",
    "tomConstants_tomCanRedo",
    "tomConstants_tomCanUndo",
    "tomConstants_tomUndoLimit",
    "tomConstants_tomDocAutoLink",
    "tomConstants_tomEllipsisMode",
    "tomConstants_tomEllipsisState",
    "tomConstants_tomEllipsisNone",
    "tomConstants_tomEllipsisEnd",
    "tomConstants_tomEllipsisWord",
    "tomConstants_tomEllipsisPresent",
    "tomConstants_tomVTopCell",
    "tomConstants_tomVLowCell",
    "tomConstants_tomHStartCell",
    "tomConstants_tomHContCell",
    "tomConstants_tomRowUpdate",
    "tomConstants_tomRowApplyDefault",
    "tomConstants_tomCellStructureChangeOnly",
    "tomConstants_tomRowHeightActual",
    "OBJECTTYPE",
    "OBJECTTYPE_tomSimpleText",
    "OBJECTTYPE_tomRuby",
    "OBJECTTYPE_tomHorzVert",
    "OBJECTTYPE_tomWarichu",
    "OBJECTTYPE_tomEq",
    "OBJECTTYPE_tomMath",
    "OBJECTTYPE_tomAccent",
    "OBJECTTYPE_tomBox",
    "OBJECTTYPE_tomBoxedFormula",
    "OBJECTTYPE_tomBrackets",
    "OBJECTTYPE_tomBracketsWithSeps",
    "OBJECTTYPE_tomEquationArray",
    "OBJECTTYPE_tomFraction",
    "OBJECTTYPE_tomFunctionApply",
    "OBJECTTYPE_tomLeftSubSup",
    "OBJECTTYPE_tomLowerLimit",
    "OBJECTTYPE_tomMatrix",
    "OBJECTTYPE_tomNary",
    "OBJECTTYPE_tomOpChar",
    "OBJECTTYPE_tomOverbar",
    "OBJECTTYPE_tomPhantom",
    "OBJECTTYPE_tomRadical",
    "OBJECTTYPE_tomSlashedFraction",
    "OBJECTTYPE_tomStack",
    "OBJECTTYPE_tomStretchStack",
    "OBJECTTYPE_tomSubscript",
    "OBJECTTYPE_tomSubSup",
    "OBJECTTYPE_tomSuperscript",
    "OBJECTTYPE_tomUnderbar",
    "OBJECTTYPE_tomUpperLimit",
    "OBJECTTYPE_tomObjectMax",
    "MANCODE",
    "MBOLD",
    "MITAL",
    "MGREEK",
    "MROMN",
    "MSCRP",
    "MFRAK",
    "MOPEN",
    "MSANS",
    "MMONO",
    "MMATH",
    "MISOL",
    "MINIT",
    "MTAIL",
    "MSTRCH",
    "MLOOP",
    "MOPENA",
    "ITextDocument",
    "ITextRange",
    "ITextSelection",
    "ITextFont",
    "ITextPara",
    "ITextStoryRanges",
    "ITextDocument2",
    "ITextRange2",
    "ITextSelection2",
    "ITextFont2",
    "ITextPara2",
    "ITextStoryRanges2",
    "ITextStory",
    "ITextStrings",
    "ITextRow",
    "ITextDisplays",
    "ITextDocument2Old",
]
