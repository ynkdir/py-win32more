from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.UI.Input.Ime
import win32more.Windows.Win32.UI.Input.KeyboardAndMouse
import win32more.Windows.Win32.UI.WindowsAndMessaging
class APPLETIDLIST(Structure):
    count: Int32
    pIIDList: POINTER(Guid)
class APPLYCANDEXPARAM(Structure):
    dwSize: UInt32
    lpwstrDisplay: win32more.Windows.Win32.Foundation.PWSTR
    lpwstrReading: win32more.Windows.Win32.Foundation.PWSTR
    dwReserved: UInt32
CATID_MSIME_IImePadApplet_VER7: Guid = Guid('{4a0f8e31-c3ee-11d1-afef-00805f0c8b6d}')
CATID_MSIME_IImePadApplet_VER80: Guid = Guid('{56f7a792-fef1-11d3-8463-00c04f7a06e5}')
CATID_MSIME_IImePadApplet_VER81: Guid = Guid('{656520b0-bb88-11d4-84c0-00c04f7a06e5}')
CATID_MSIME_IImePadApplet900: Guid = Guid('{faae51bf-5e5b-4a1d-8de1-17c1d9e1728d}')
CATID_MSIME_IImePadApplet1000: Guid = Guid('{e081e1d6-2389-43cb-b66f-609f823d9f9c}')
CATID_MSIME_IImePadApplet1200: Guid = Guid('{a47fb5fc-7d15-4223-a789-b781bf9ae667}')
CATID_MSIME_IImePadApplet: Guid = Guid('{7566cad1-4ec9-4478-9fe9-8ed766619edf}')
FEID_NONE: UInt32 = 0
FEID_CHINESE_TRADITIONAL: UInt32 = 1
FEID_CHINESE_SIMPLIFIED: UInt32 = 2
FEID_CHINESE_HONGKONG: UInt32 = 3
FEID_CHINESE_SINGAPORE: UInt32 = 4
FEID_JAPANESE: UInt32 = 5
FEID_KOREAN: UInt32 = 6
FEID_KOREAN_JOHAB: UInt32 = 7
INFOMASK_NONE: UInt32 = 0
INFOMASK_QUERY_CAND: UInt32 = 1
INFOMASK_APPLY_CAND: UInt32 = 2
INFOMASK_APPLY_CAND_EX: UInt32 = 4
INFOMASK_STRING_FIX: UInt32 = 65536
INFOMASK_HIDE_CAND: UInt32 = 131072
INFOMASK_BLOCK_CAND: UInt32 = 262144
IMEFAREASTINFO_TYPE_DEFAULT: UInt32 = 0
IMEFAREASTINFO_TYPE_READING: UInt32 = 1
IMEFAREASTINFO_TYPE_COMMENT: UInt32 = 2
IMEFAREASTINFO_TYPE_COSTTIME: UInt32 = 3
CHARINFO_APPLETID_MASK: UInt32 = 4278190080
CHARINFO_FEID_MASK: UInt32 = 15728640
CHARINFO_CHARID_MASK: UInt32 = 65535
MAX_APPLETTITLE: UInt32 = 64
MAX_FONTFACE: UInt32 = 32
IPACFG_NONE: Int32 = 0
IPACFG_PROPERTY: Int32 = 1
IPACFG_HELP: Int32 = 2
IPACFG_TITLE: Int32 = 65536
IPACFG_TITLEFONTFACE: Int32 = 131072
IPACFG_CATEGORY: Int32 = 262144
IPACFG_LANG: Int32 = 16
IPACID_NONE: UInt32 = 0
IPACID_SOFTKEY: UInt32 = 1
IPACID_HANDWRITING: UInt32 = 2
IPACID_STROKESEARCH: UInt32 = 3
IPACID_RADICALSEARCH: UInt32 = 4
IPACID_SYMBOLSEARCH: UInt32 = 5
IPACID_VOICE: UInt32 = 6
IPACID_EPWING: UInt32 = 7
IPACID_OCR: UInt32 = 8
IPACID_CHARLIST: UInt32 = 9
IPACID_USER: UInt32 = 256
IMEPADREQ_FIRST: UInt32 = 4096
IMEPADREQ_INSERTSTRINGCANDIDATE: UInt32 = 4098
IMEPADREQ_INSERTITEMCANDIDATE: UInt32 = 4099
IMEPADREQ_SENDKEYCONTROL: UInt32 = 4101
IMEPADREQ_GETSELECTEDSTRING: UInt32 = 4103
IMEPADREQ_SETAPPLETDATA: UInt32 = 4105
IMEPADREQ_GETAPPLETDATA: UInt32 = 4106
IMEPADREQ_SETTITLEFONT: UInt32 = 4107
IMEPADREQ_GETCOMPOSITIONSTRINGID: UInt32 = 4109
IMEPADREQ_INSERTSTRINGCANDIDATEINFO: UInt32 = 4110
IMEPADREQ_CHANGESTRINGCANDIDATEINFO: UInt32 = 4111
IMEPADREQ_INSERTSTRINGINFO: UInt32 = 4114
IMEPADREQ_CHANGESTRINGINFO: UInt32 = 4115
IMEPADREQ_GETCURRENTUILANGID: UInt32 = 4120
IMEPADCTRL_CONVERTALL: UInt32 = 1
IMEPADCTRL_DETERMINALL: UInt32 = 2
IMEPADCTRL_DETERMINCHAR: UInt32 = 3
IMEPADCTRL_CLEARALL: UInt32 = 4
IMEPADCTRL_CARETSET: UInt32 = 5
IMEPADCTRL_CARETLEFT: UInt32 = 6
IMEPADCTRL_CARETRIGHT: UInt32 = 7
IMEPADCTRL_CARETTOP: UInt32 = 8
IMEPADCTRL_CARETBOTTOM: UInt32 = 9
IMEPADCTRL_CARETBACKSPACE: UInt32 = 10
IMEPADCTRL_CARETDELETE: UInt32 = 11
IMEPADCTRL_PHRASEDELETE: UInt32 = 12
IMEPADCTRL_INSERTSPACE: UInt32 = 13
IMEPADCTRL_INSERTFULLSPACE: UInt32 = 14
IMEPADCTRL_INSERTHALFSPACE: UInt32 = 15
IMEPADCTRL_ONIME: UInt32 = 16
IMEPADCTRL_OFFIME: UInt32 = 17
IMEPADCTRL_ONPRECONVERSION: UInt32 = 18
IMEPADCTRL_OFFPRECONVERSION: UInt32 = 19
IMEPADCTRL_PHONETICCANDIDATE: UInt32 = 20
IMEKEYCTRLMASK_ALT: UInt32 = 1
IMEKEYCTRLMASK_CTRL: UInt32 = 2
IMEKEYCTRLMASK_SHIFT: UInt32 = 4
IMEKEYCTRL_UP: UInt32 = 1
IMEKEYCTRL_DOWN: UInt32 = 0
IMEPN_FIRST: UInt32 = 256
IMEPN_ACTIVATE: UInt32 = 257
IMEPN_INACTIVATE: UInt32 = 258
IMEPN_SHOW: UInt32 = 260
IMEPN_HIDE: UInt32 = 261
IMEPN_SIZECHANGING: UInt32 = 262
IMEPN_SIZECHANGED: UInt32 = 263
IMEPN_CONFIG: UInt32 = 264
IMEPN_HELP: UInt32 = 265
IMEPN_QUERYCAND: UInt32 = 266
IMEPN_APPLYCAND: UInt32 = 267
IMEPN_APPLYCANDEX: UInt32 = 268
IMEPN_SETTINGCHANGED: UInt32 = 269
IMEPN_USER: UInt32 = 356
IPAWS_ENABLED: Int32 = 1
IPAWS_SIZINGNOTIFY: Int32 = 4
IPAWS_VERTICALFIXED: Int32 = 256
IPAWS_HORIZONTALFIXED: Int32 = 512
IPAWS_SIZEFIXED: Int32 = 768
IPAWS_MAXWIDTHFIXED: Int32 = 4096
IPAWS_MAXHEIGHTFIXED: Int32 = 8192
IPAWS_MAXSIZEFIXED: Int32 = 12288
IPAWS_MINWIDTHFIXED: Int32 = 65536
IPAWS_MINHEIGHTFIXED: Int32 = 131072
IPAWS_MINSIZEFIXED: Int32 = 196608
STYLE_DESCRIPTION_SIZE: UInt32 = 32
IMEMENUITEM_STRING_SIZE: UInt32 = 80
IMC_GETCANDIDATEPOS: UInt32 = 7
IMC_SETCANDIDATEPOS: UInt32 = 8
IMC_GETCOMPOSITIONFONT: UInt32 = 9
IMC_SETCOMPOSITIONFONT: UInt32 = 10
IMC_GETCOMPOSITIONWINDOW: UInt32 = 11
IMC_SETCOMPOSITIONWINDOW: UInt32 = 12
IMC_GETSTATUSWINDOWPOS: UInt32 = 15
IMC_SETSTATUSWINDOWPOS: UInt32 = 16
IMC_CLOSESTATUSWINDOW: UInt32 = 33
IMC_OPENSTATUSWINDOW: UInt32 = 34
NI_FINALIZECONVERSIONRESULT: UInt32 = 20
ISC_SHOWUICANDIDATEWINDOW: UInt32 = 1
ISC_SHOWUICOMPOSITIONWINDOW: UInt32 = 2147483648
ISC_SHOWUIGUIDELINE: UInt32 = 1073741824
ISC_SHOWUIALLCANDIDATEWINDOW: UInt32 = 15
ISC_SHOWUIALL: UInt32 = 3221225487
MOD_LEFT: UInt32 = 32768
MOD_RIGHT: UInt32 = 16384
MOD_ON_KEYUP: UInt32 = 2048
MOD_IGNORE_ALL_MODIFIER: UInt32 = 1024
IME_HOTKEY_DSWITCH_FIRST: UInt32 = 256
IME_HOTKEY_DSWITCH_LAST: UInt32 = 287
IME_HOTKEY_PRIVATE_FIRST: UInt32 = 512
IME_HOTKEY_PRIVATE_LAST: UInt32 = 543
CS_INSERTCHAR: UInt32 = 8192
CS_NOMOVECARET: UInt32 = 16384
IMEVER_0310: UInt32 = 196618
IMEVER_0400: UInt32 = 262144
IME_PROP_AT_CARET: UInt32 = 65536
IME_PROP_SPECIAL_UI: UInt32 = 131072
IME_PROP_CANDLIST_START_FROM_1: UInt32 = 262144
IME_PROP_UNICODE: UInt32 = 524288
IME_PROP_COMPLETE_ON_UNSELECT: UInt32 = 1048576
UI_CAP_2700: UInt32 = 1
UI_CAP_ROT90: UInt32 = 2
UI_CAP_ROTANY: UInt32 = 4
SCS_CAP_COMPSTR: UInt32 = 1
SCS_CAP_MAKEREAD: UInt32 = 2
SCS_CAP_SETRECONVERTSTRING: UInt32 = 4
SELECT_CAP_CONVERSION: UInt32 = 1
SELECT_CAP_SENTENCE: UInt32 = 2
GL_LEVEL_NOGUIDELINE: UInt32 = 0
GL_LEVEL_FATAL: UInt32 = 1
GL_LEVEL_ERROR: UInt32 = 2
GL_LEVEL_WARNING: UInt32 = 3
GL_LEVEL_INFORMATION: UInt32 = 4
GL_ID_UNKNOWN: UInt32 = 0
GL_ID_NOMODULE: UInt32 = 1
GL_ID_NODICTIONARY: UInt32 = 16
GL_ID_CANNOTSAVE: UInt32 = 17
GL_ID_NOCONVERT: UInt32 = 32
GL_ID_TYPINGERROR: UInt32 = 33
GL_ID_TOOMANYSTROKE: UInt32 = 34
GL_ID_READINGCONFLICT: UInt32 = 35
GL_ID_INPUTREADING: UInt32 = 36
GL_ID_INPUTRADICAL: UInt32 = 37
GL_ID_INPUTCODE: UInt32 = 38
GL_ID_INPUTSYMBOL: UInt32 = 39
GL_ID_CHOOSECANDIDATE: UInt32 = 40
GL_ID_REVERSECONVERSION: UInt32 = 41
GL_ID_PRIVATE_FIRST: UInt32 = 32768
GL_ID_PRIVATE_LAST: UInt32 = 65535
ATTR_INPUT: UInt32 = 0
ATTR_TARGET_CONVERTED: UInt32 = 1
ATTR_CONVERTED: UInt32 = 2
ATTR_TARGET_NOTCONVERTED: UInt32 = 3
ATTR_INPUT_ERROR: UInt32 = 4
ATTR_FIXEDCONVERTED: UInt32 = 5
CFS_DEFAULT: UInt32 = 0
CFS_RECT: UInt32 = 1
CFS_POINT: UInt32 = 2
CFS_FORCE_POSITION: UInt32 = 32
CFS_CANDIDATEPOS: UInt32 = 64
CFS_EXCLUDE: UInt32 = 128
IME_CAND_UNKNOWN: UInt32 = 0
IME_CAND_READ: UInt32 = 1
IME_CAND_CODE: UInt32 = 2
IME_CAND_MEANING: UInt32 = 3
IME_CAND_RADICAL: UInt32 = 4
IME_CAND_STROKE: UInt32 = 5
IMN_CLOSESTATUSWINDOW: UInt32 = 1
IMN_OPENSTATUSWINDOW: UInt32 = 2
IMN_CHANGECANDIDATE: UInt32 = 3
IMN_CLOSECANDIDATE: UInt32 = 4
IMN_OPENCANDIDATE: UInt32 = 5
IMN_SETCONVERSIONMODE: UInt32 = 6
IMN_SETSENTENCEMODE: UInt32 = 7
IMN_SETOPENSTATUS: UInt32 = 8
IMN_SETCANDIDATEPOS: UInt32 = 9
IMN_SETCOMPOSITIONFONT: UInt32 = 10
IMN_SETCOMPOSITIONWINDOW: UInt32 = 11
IMN_SETSTATUSWINDOWPOS: UInt32 = 12
IMN_GUIDELINE: UInt32 = 13
IMN_PRIVATE: UInt32 = 14
IMR_COMPOSITIONWINDOW: UInt32 = 1
IMR_CANDIDATEWINDOW: UInt32 = 2
IMR_COMPOSITIONFONT: UInt32 = 3
IMR_RECONVERTSTRING: UInt32 = 4
IMR_CONFIRMRECONVERTSTRING: UInt32 = 5
IMR_QUERYCHARPOSITION: UInt32 = 6
IMR_DOCUMENTFEED: UInt32 = 7
IMM_ERROR_NODATA: Int32 = -1
IMM_ERROR_GENERAL: Int32 = -2
IME_CONFIG_GENERAL: UInt32 = 1
IME_CONFIG_REGISTERWORD: UInt32 = 2
IME_CONFIG_SELECTDICTIONARY: UInt32 = 3
IME_REGWORD_STYLE_EUDC: UInt32 = 1
IME_REGWORD_STYLE_USER_FIRST: UInt32 = 2147483648
IME_REGWORD_STYLE_USER_LAST: UInt32 = 4294967295
IACE_CHILDREN: UInt32 = 1
IACE_DEFAULT: UInt32 = 16
IACE_IGNORENOCONTEXT: UInt32 = 32
IGIMIF_RIGHTMENU: UInt32 = 1
IGIMII_CMODE: UInt32 = 1
IGIMII_SMODE: UInt32 = 2
IGIMII_CONFIGURE: UInt32 = 4
IGIMII_TOOLS: UInt32 = 8
IGIMII_HELP: UInt32 = 16
IGIMII_OTHER: UInt32 = 32
IGIMII_INPUTTOOLS: UInt32 = 64
IMFT_RADIOCHECK: UInt32 = 1
IMFT_SEPARATOR: UInt32 = 2
IMFT_SUBMENU: UInt32 = 4
SOFTKEYBOARD_TYPE_T1: UInt32 = 1
SOFTKEYBOARD_TYPE_C1: UInt32 = 2
IMMGWL_IMC: UInt32 = 0
IMMGWLP_IMC: UInt32 = 0
IMC_SETCONVERSIONMODE: UInt32 = 2
IMC_SETSENTENCEMODE: UInt32 = 4
IMC_SETOPENSTATUS: UInt32 = 6
IMC_GETSOFTKBDFONT: UInt32 = 17
IMC_SETSOFTKBDFONT: UInt32 = 18
IMC_GETSOFTKBDPOS: UInt32 = 19
IMC_SETSOFTKBDPOS: UInt32 = 20
IMC_GETSOFTKBDSUBTYPE: UInt32 = 21
IMC_SETSOFTKBDSUBTYPE: UInt32 = 22
IMC_SETSOFTKBDDATA: UInt32 = 24
NI_CONTEXTUPDATED: UInt32 = 3
IME_SYSINFO_WINLOGON: UInt32 = 1
INIT_STATUSWNDPOS: UInt32 = 1
INIT_CONVERSION: UInt32 = 2
INIT_SENTENCE: UInt32 = 4
INIT_LOGFONT: UInt32 = 8
INIT_COMPFORM: UInt32 = 16
INIT_SOFTKBDPOS: UInt32 = 32
IME_PROP_END_UNLOAD: UInt32 = 1
IME_PROP_KBD_CHAR_FIRST: UInt32 = 2
IME_PROP_IGNORE_UPKEYS: UInt32 = 4
IME_PROP_NEED_ALTKEY: UInt32 = 8
IME_PROP_NO_KEYS_ON_CLOSE: UInt32 = 16
IME_PROP_ACCEPT_WIDE_VKEY: UInt32 = 32
UI_CAP_SOFTKBD: UInt32 = 65536
IMN_SOFTKBDDESTROYED: UInt32 = 17
IME_UI_CLASS_NAME_SIZE: UInt32 = 16
IME_ESC_STRING_BUFFER_SIZE: UInt32 = 80
szImeJapan: String = 'MSIME.Japan'
szImeKorea: String = 'MSIME.Korea'
szImeChina: String = 'MSIME.China'
szImeTaiwan: String = 'MSIME.Taiwan'
CLSID_VERSION_DEPENDENT_MSIME_JAPANESE: Guid = Guid('{6a91029e-aa49-471b-aee7-7d332785660d}')
IFEC_S_ALREADY_DEFAULT: win32more.Windows.Win32.Foundation.HRESULT = 291840
FELANG_REQ_CONV: UInt32 = 65536
FELANG_REQ_RECONV: UInt32 = 131072
FELANG_REQ_REV: UInt32 = 196608
FELANG_CMODE_MONORUBY: UInt32 = 2
FELANG_CMODE_NOPRUNING: UInt32 = 4
FELANG_CMODE_KATAKANAOUT: UInt32 = 8
FELANG_CMODE_HIRAGANAOUT: UInt32 = 0
FELANG_CMODE_HALFWIDTHOUT: UInt32 = 16
FELANG_CMODE_FULLWIDTHOUT: UInt32 = 32
FELANG_CMODE_BOPOMOFO: UInt32 = 64
FELANG_CMODE_HANGUL: UInt32 = 128
FELANG_CMODE_PINYIN: UInt32 = 256
FELANG_CMODE_PRECONV: UInt32 = 512
FELANG_CMODE_RADICAL: UInt32 = 1024
FELANG_CMODE_UNKNOWNREADING: UInt32 = 2048
FELANG_CMODE_MERGECAND: UInt32 = 4096
FELANG_CMODE_ROMAN: UInt32 = 8192
FELANG_CMODE_BESTFIRST: UInt32 = 16384
FELANG_CMODE_USENOREVWORDS: UInt32 = 32768
FELANG_CMODE_NONE: UInt32 = 16777216
FELANG_CMODE_PLAURALCLAUSE: UInt32 = 33554432
FELANG_CMODE_SINGLECONVERT: UInt32 = 67108864
FELANG_CMODE_AUTOMATIC: UInt32 = 134217728
FELANG_CMODE_PHRASEPREDICT: UInt32 = 268435456
FELANG_CMODE_CONVERSATION: UInt32 = 536870912
FELANG_CMODE_NAME: UInt32 = 268435456
FELANG_CMODE_NOINVISIBLECHAR: UInt32 = 1073741824
E_NOCAND: UInt32 = 48
E_NOTENOUGH_BUFFER: UInt32 = 49
E_NOTENOUGH_WDD: UInt32 = 50
E_LARGEINPUT: UInt32 = 51
FELANG_CLMN_WBREAK: UInt32 = 1
FELANG_CLMN_NOWBREAK: UInt32 = 2
FELANG_CLMN_PBREAK: UInt32 = 4
FELANG_CLMN_NOPBREAK: UInt32 = 8
FELANG_CLMN_FIXR: UInt32 = 16
FELANG_CLMN_FIXD: UInt32 = 32
FELANG_INVALD_PO: UInt32 = 65535
IFED_POS_NONE: UInt32 = 0
IFED_POS_NOUN: UInt32 = 1
IFED_POS_VERB: UInt32 = 2
IFED_POS_ADJECTIVE: UInt32 = 4
IFED_POS_ADJECTIVE_VERB: UInt32 = 8
IFED_POS_ADVERB: UInt32 = 16
IFED_POS_ADNOUN: UInt32 = 32
IFED_POS_CONJUNCTION: UInt32 = 64
IFED_POS_INTERJECTION: UInt32 = 128
IFED_POS_INDEPENDENT: UInt32 = 255
IFED_POS_INFLECTIONALSUFFIX: UInt32 = 256
IFED_POS_PREFIX: UInt32 = 512
IFED_POS_SUFFIX: UInt32 = 1024
IFED_POS_AFFIX: UInt32 = 1536
IFED_POS_TANKANJI: UInt32 = 2048
IFED_POS_IDIOMS: UInt32 = 4096
IFED_POS_SYMBOLS: UInt32 = 8192
IFED_POS_PARTICLE: UInt32 = 16384
IFED_POS_AUXILIARY_VERB: UInt32 = 32768
IFED_POS_SUB_VERB: UInt32 = 65536
IFED_POS_DEPENDENT: UInt32 = 114688
IFED_POS_ALL: UInt32 = 131071
IFED_SELECT_NONE: UInt32 = 0
IFED_SELECT_READING: UInt32 = 1
IFED_SELECT_DISPLAY: UInt32 = 2
IFED_SELECT_POS: UInt32 = 4
IFED_SELECT_COMMENT: UInt32 = 8
IFED_SELECT_ALL: UInt32 = 15
IFED_REG_NONE: UInt32 = 0
IFED_REG_USER: UInt32 = 1
IFED_REG_AUTO: UInt32 = 2
IFED_REG_GRAMMAR: UInt32 = 4
IFED_REG_ALL: UInt32 = 7
IFED_TYPE_NONE: UInt32 = 0
IFED_TYPE_GENERAL: UInt32 = 1
IFED_TYPE_NAMEPLACE: UInt32 = 2
IFED_TYPE_SPEECH: UInt32 = 4
IFED_TYPE_REVERSE: UInt32 = 8
IFED_TYPE_ENGLISH: UInt32 = 16
IFED_TYPE_ALL: UInt32 = 31
IFED_S_MORE_ENTRIES: win32more.Windows.Win32.Foundation.HRESULT = 291328
IFED_S_EMPTY_DICTIONARY: win32more.Windows.Win32.Foundation.HRESULT = 291329
IFED_S_WORD_EXISTS: win32more.Windows.Win32.Foundation.HRESULT = 291330
IFED_S_COMMENT_CHANGED: win32more.Windows.Win32.Foundation.HRESULT = 291331
IFED_E_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2147192064
IFED_E_INVALID_FORMAT: win32more.Windows.Win32.Foundation.HRESULT = -2147192063
IFED_E_OPEN_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -2147192062
IFED_E_WRITE_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -2147192061
IFED_E_NO_ENTRY: win32more.Windows.Win32.Foundation.HRESULT = -2147192060
IFED_E_REGISTER_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -2147192059
IFED_E_NOT_USER_DIC: win32more.Windows.Win32.Foundation.HRESULT = -2147192058
IFED_E_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -2147192057
IFED_E_USER_COMMENT: win32more.Windows.Win32.Foundation.HRESULT = -2147192056
IFED_E_REGISTER_ILLEGAL_POS: win32more.Windows.Win32.Foundation.HRESULT = -2147192055
IFED_E_REGISTER_IMPROPER_WORD: win32more.Windows.Win32.Foundation.HRESULT = -2147192054
IFED_E_REGISTER_DISCONNECTED: win32more.Windows.Win32.Foundation.HRESULT = -2147192053
cbCommentMax: UInt32 = 256
wchPrivate1: UInt32 = 57344
POS_UNDEFINED: UInt32 = 0
JPOS_UNDEFINED: UInt32 = 0
JPOS_MEISHI_FUTSU: UInt32 = 100
JPOS_MEISHI_SAHEN: UInt32 = 101
JPOS_MEISHI_ZAHEN: UInt32 = 102
JPOS_MEISHI_KEIYOUDOUSHI: UInt32 = 103
JPOS_HUKUSIMEISHI: UInt32 = 104
JPOS_MEISA_KEIDOU: UInt32 = 105
JPOS_JINMEI: UInt32 = 106
JPOS_JINMEI_SEI: UInt32 = 107
JPOS_JINMEI_MEI: UInt32 = 108
JPOS_CHIMEI: UInt32 = 109
JPOS_CHIMEI_KUNI: UInt32 = 110
JPOS_CHIMEI_KEN: UInt32 = 111
JPOS_CHIMEI_GUN: UInt32 = 112
JPOS_CHIMEI_KU: UInt32 = 113
JPOS_CHIMEI_SHI: UInt32 = 114
JPOS_CHIMEI_MACHI: UInt32 = 115
JPOS_CHIMEI_MURA: UInt32 = 116
JPOS_CHIMEI_EKI: UInt32 = 117
JPOS_SONOTA: UInt32 = 118
JPOS_SHAMEI: UInt32 = 119
JPOS_SOSHIKI: UInt32 = 120
JPOS_KENCHIKU: UInt32 = 121
JPOS_BUPPIN: UInt32 = 122
JPOS_DAIMEISHI: UInt32 = 123
JPOS_DAIMEISHI_NINSHOU: UInt32 = 124
JPOS_DAIMEISHI_SHIJI: UInt32 = 125
JPOS_KAZU: UInt32 = 126
JPOS_KAZU_SURYOU: UInt32 = 127
JPOS_KAZU_SUSHI: UInt32 = 128
JPOS_5DAN_AWA: UInt32 = 200
JPOS_5DAN_KA: UInt32 = 201
JPOS_5DAN_GA: UInt32 = 202
JPOS_5DAN_SA: UInt32 = 203
JPOS_5DAN_TA: UInt32 = 204
JPOS_5DAN_NA: UInt32 = 205
JPOS_5DAN_BA: UInt32 = 206
JPOS_5DAN_MA: UInt32 = 207
JPOS_5DAN_RA: UInt32 = 208
JPOS_5DAN_AWAUON: UInt32 = 209
JPOS_5DAN_KASOKUON: UInt32 = 210
JPOS_5DAN_RAHEN: UInt32 = 211
JPOS_4DAN_HA: UInt32 = 212
JPOS_1DAN: UInt32 = 213
JPOS_TOKUSHU_KAHEN: UInt32 = 214
JPOS_TOKUSHU_SAHENSURU: UInt32 = 215
JPOS_TOKUSHU_SAHEN: UInt32 = 216
JPOS_TOKUSHU_ZAHEN: UInt32 = 217
JPOS_TOKUSHU_NAHEN: UInt32 = 218
JPOS_KURU_KI: UInt32 = 219
JPOS_KURU_KITA: UInt32 = 220
JPOS_KURU_KITARA: UInt32 = 221
JPOS_KURU_KITARI: UInt32 = 222
JPOS_KURU_KITAROU: UInt32 = 223
JPOS_KURU_KITE: UInt32 = 224
JPOS_KURU_KUREBA: UInt32 = 225
JPOS_KURU_KO: UInt32 = 226
JPOS_KURU_KOI: UInt32 = 227
JPOS_KURU_KOYOU: UInt32 = 228
JPOS_SURU_SA: UInt32 = 229
JPOS_SURU_SI: UInt32 = 230
JPOS_SURU_SITA: UInt32 = 231
JPOS_SURU_SITARA: UInt32 = 232
JPOS_SURU_SIATRI: UInt32 = 233
JPOS_SURU_SITAROU: UInt32 = 234
JPOS_SURU_SITE: UInt32 = 235
JPOS_SURU_SIYOU: UInt32 = 236
JPOS_SURU_SUREBA: UInt32 = 237
JPOS_SURU_SE: UInt32 = 238
JPOS_SURU_SEYO: UInt32 = 239
JPOS_KEIYOU: UInt32 = 300
JPOS_KEIYOU_GARU: UInt32 = 301
JPOS_KEIYOU_GE: UInt32 = 302
JPOS_KEIYOU_ME: UInt32 = 303
JPOS_KEIYOU_YUU: UInt32 = 304
JPOS_KEIYOU_U: UInt32 = 305
JPOS_KEIDOU: UInt32 = 400
JPOS_KEIDOU_NO: UInt32 = 401
JPOS_KEIDOU_TARU: UInt32 = 402
JPOS_KEIDOU_GARU: UInt32 = 403
JPOS_FUKUSHI: UInt32 = 500
JPOS_FUKUSHI_SAHEN: UInt32 = 501
JPOS_FUKUSHI_NI: UInt32 = 502
JPOS_FUKUSHI_NANO: UInt32 = 503
JPOS_FUKUSHI_DA: UInt32 = 504
JPOS_FUKUSHI_TO: UInt32 = 505
JPOS_FUKUSHI_TOSURU: UInt32 = 506
JPOS_RENTAISHI: UInt32 = 600
JPOS_RENTAISHI_SHIJI: UInt32 = 601
JPOS_SETSUZOKUSHI: UInt32 = 650
JPOS_KANDOUSHI: UInt32 = 670
JPOS_SETTOU: UInt32 = 700
JPOS_SETTOU_KAKU: UInt32 = 701
JPOS_SETTOU_SAI: UInt32 = 702
JPOS_SETTOU_FUKU: UInt32 = 703
JPOS_SETTOU_MI: UInt32 = 704
JPOS_SETTOU_DAISHOU: UInt32 = 705
JPOS_SETTOU_KOUTEI: UInt32 = 706
JPOS_SETTOU_CHOUTAN: UInt32 = 707
JPOS_SETTOU_SHINKYU: UInt32 = 708
JPOS_SETTOU_JINMEI: UInt32 = 709
JPOS_SETTOU_CHIMEI: UInt32 = 710
JPOS_SETTOU_SONOTA: UInt32 = 711
JPOS_SETTOU_JOSUSHI: UInt32 = 712
JPOS_SETTOU_TEINEI_O: UInt32 = 713
JPOS_SETTOU_TEINEI_GO: UInt32 = 714
JPOS_SETTOU_TEINEI_ON: UInt32 = 715
JPOS_SETSUBI: UInt32 = 800
JPOS_SETSUBI_TEKI: UInt32 = 801
JPOS_SETSUBI_SEI: UInt32 = 802
JPOS_SETSUBI_KA: UInt32 = 803
JPOS_SETSUBI_CHU: UInt32 = 804
JPOS_SETSUBI_FU: UInt32 = 805
JPOS_SETSUBI_RYU: UInt32 = 806
JPOS_SETSUBI_YOU: UInt32 = 807
JPOS_SETSUBI_KATA: UInt32 = 808
JPOS_SETSUBI_MEISHIRENDAKU: UInt32 = 809
JPOS_SETSUBI_JINMEI: UInt32 = 810
JPOS_SETSUBI_CHIMEI: UInt32 = 811
JPOS_SETSUBI_KUNI: UInt32 = 812
JPOS_SETSUBI_KEN: UInt32 = 813
JPOS_SETSUBI_GUN: UInt32 = 814
JPOS_SETSUBI_KU: UInt32 = 815
JPOS_SETSUBI_SHI: UInt32 = 816
JPOS_SETSUBI_MACHI: UInt32 = 817
JPOS_SETSUBI_CHOU: UInt32 = 818
JPOS_SETSUBI_MURA: UInt32 = 819
JPOS_SETSUBI_SON: UInt32 = 820
JPOS_SETSUBI_EKI: UInt32 = 821
JPOS_SETSUBI_SONOTA: UInt32 = 822
JPOS_SETSUBI_SHAMEI: UInt32 = 823
JPOS_SETSUBI_SOSHIKI: UInt32 = 824
JPOS_SETSUBI_KENCHIKU: UInt32 = 825
JPOS_RENYOU_SETSUBI: UInt32 = 826
JPOS_SETSUBI_JOSUSHI: UInt32 = 827
JPOS_SETSUBI_JOSUSHIPLUS: UInt32 = 828
JPOS_SETSUBI_JIKAN: UInt32 = 829
JPOS_SETSUBI_JIKANPLUS: UInt32 = 830
JPOS_SETSUBI_TEINEI: UInt32 = 831
JPOS_SETSUBI_SAN: UInt32 = 832
JPOS_SETSUBI_KUN: UInt32 = 833
JPOS_SETSUBI_SAMA: UInt32 = 834
JPOS_SETSUBI_DONO: UInt32 = 835
JPOS_SETSUBI_FUKUSU: UInt32 = 836
JPOS_SETSUBI_TACHI: UInt32 = 837
JPOS_SETSUBI_RA: UInt32 = 838
JPOS_TANKANJI: UInt32 = 900
JPOS_TANKANJI_KAO: UInt32 = 901
JPOS_KANYOUKU: UInt32 = 902
JPOS_DOKURITSUGO: UInt32 = 903
JPOS_FUTEIGO: UInt32 = 904
JPOS_KIGOU: UInt32 = 905
JPOS_EIJI: UInt32 = 906
JPOS_KUTEN: UInt32 = 907
JPOS_TOUTEN: UInt32 = 908
JPOS_KANJI: UInt32 = 909
JPOS_OPENBRACE: UInt32 = 910
JPOS_CLOSEBRACE: UInt32 = 911
JPOS_YOKUSEI: UInt32 = 912
JPOS_TANSHUKU: UInt32 = 913
VERSION_ID_JAPANESE: UInt32 = 16777216
VERSION_ID_KOREAN: UInt32 = 33554432
VERSION_ID_CHINESE_TRADITIONAL: UInt32 = 67108864
VERSION_ID_CHINESE_SIMPLIFIED: UInt32 = 134217728
RWM_SERVICE: String = 'MSIMEService'
FID_MSIME_VERSION: UInt32 = 0
RWM_UIREADY: String = 'MSIMEUIReady'
RWM_MOUSE: String = 'MSIMEMouseOperation'
VERSION_MOUSE_OPERATION: UInt32 = 1
IMEMOUSERET_NOTHANDLED: Int32 = -1
IMEMOUSE_VERSION: UInt32 = 255
IMEMOUSE_NONE: UInt32 = 0
IMEMOUSE_LDOWN: UInt32 = 1
IMEMOUSE_RDOWN: UInt32 = 2
IMEMOUSE_MDOWN: UInt32 = 4
IMEMOUSE_WUP: UInt32 = 16
IMEMOUSE_WDOWN: UInt32 = 32
RWM_RECONVERT: String = 'MSIMEReconvert'
FID_RECONVERT_VERSION: UInt32 = 268435456
VERSION_RECONVERSION: UInt32 = 1
RWM_RECONVERTREQUEST: String = 'MSIMEReconvertRequest'
VERSION_DOCUMENTFEED: UInt32 = 1
RWM_DOCUMENTFEED: String = 'MSIMEDocumentFeed'
VERSION_QUERYPOSITION: UInt32 = 1
RWM_QUERYPOSITION: String = 'MSIMEQueryPosition'
RWM_MODEBIAS: String = 'MSIMEModeBias'
VERSION_MODEBIAS: UInt32 = 1
MODEBIAS_GETVERSION: UInt32 = 0
MODEBIAS_SETVALUE: UInt32 = 1
MODEBIAS_GETVALUE: UInt32 = 2
MODEBIASMODE_DEFAULT: UInt32 = 0
MODEBIASMODE_FILENAME: UInt32 = 1
MODEBIASMODE_READING: UInt32 = 2
MODEBIASMODE_DIGIT: UInt32 = 4
RWM_SHOWIMEPAD: String = 'MSIMEShowImePad'
SHOWIMEPAD_DEFAULT: UInt32 = 0
SHOWIMEPAD_CATEGORY: UInt32 = 1
SHOWIMEPAD_GUID: UInt32 = 2
RWM_KEYMAP: String = 'MSIMEKeyMap'
RWM_CHGKEYMAP: String = 'MSIMEChangeKeyMap'
RWM_NTFYKEYMAP: String = 'MSIMENotifyKeyMap'
FID_MSIME_KMS_VERSION: UInt32 = 1
FID_MSIME_KMS_INIT: UInt32 = 2
FID_MSIME_KMS_TERM: UInt32 = 3
FID_MSIME_KMS_DEL_KEYLIST: UInt32 = 4
FID_MSIME_KMS_NOTIFY: UInt32 = 5
FID_MSIME_KMS_GETMAP: UInt32 = 6
FID_MSIME_KMS_INVOKE: UInt32 = 7
FID_MSIME_KMS_SETMAP: UInt32 = 8
FID_MSIME_KMS_FUNCDESC: UInt32 = 9
FID_MSIME_KMS_GETMAPSEAMLESS: UInt32 = 10
FID_MSIME_KMS_GETMAPFAST: UInt32 = 11
IMEKMS_NOCOMPOSITION: UInt32 = 0
IMEKMS_COMPOSITION: UInt32 = 1
IMEKMS_SELECTION: UInt32 = 2
IMEKMS_IMEOFF: UInt32 = 3
IMEKMS_2NDLEVEL: UInt32 = 4
IMEKMS_INPTGL: UInt32 = 5
IMEKMS_CANDIDATE: UInt32 = 6
IMEKMS_TYPECAND: UInt32 = 7
RWM_RECONVERTOPTIONS: String = 'MSIMEReconvertOptions'
RECONVOPT_NONE: UInt32 = 0
RECONVOPT_USECANCELNOTIFY: UInt32 = 1
GCSEX_CANCELRECONVERT: UInt32 = 268435456
CLSID_ImePlugInDictDictionaryList_CHS: Guid = Guid('{7bf0129b-5bef-4de4-9b0b-5edb66ac2fa6}')
CLSID_ImePlugInDictDictionaryList_JPN: Guid = Guid('{4fe2776b-b0f9-4396-b5fc-e9d4cf1ec195}')
@winfunctype('IMM32.dll')
def ImmInstallIMEA(lpszIMEFileName: win32more.Windows.Win32.Foundation.PSTR, lpszLayoutText: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL: ...
@winfunctype('IMM32.dll')
def ImmInstallIMEW(lpszIMEFileName: win32more.Windows.Win32.Foundation.PWSTR, lpszLayoutText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL: ...
ImmInstallIME = UnicodeAlias('ImmInstallIMEW')
@winfunctype('IMM32.dll')
def ImmGetDefaultIMEWnd(param0: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HWND: ...
@winfunctype('IMM32.dll')
def ImmGetDescriptionA(param0: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, lpszDescription: win32more.Windows.Win32.Foundation.PSTR, uBufLen: UInt32) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmGetDescriptionW(param0: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, lpszDescription: win32more.Windows.Win32.Foundation.PWSTR, uBufLen: UInt32) -> UInt32: ...
ImmGetDescription = UnicodeAlias('ImmGetDescriptionW')
@winfunctype('IMM32.dll')
def ImmGetIMEFileNameA(param0: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, lpszFileName: win32more.Windows.Win32.Foundation.PSTR, uBufLen: UInt32) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmGetIMEFileNameW(param0: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, lpszFileName: win32more.Windows.Win32.Foundation.PWSTR, uBufLen: UInt32) -> UInt32: ...
ImmGetIMEFileName = UnicodeAlias('ImmGetIMEFileNameW')
@winfunctype('IMM32.dll')
def ImmGetProperty(param0: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, param1: UInt32) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmIsIME(param0: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmSimulateHotKey(param0: win32more.Windows.Win32.Foundation.HWND, param1: win32more.Windows.Win32.UI.Input.Ime.IME_HOTKEY_IDENTIFIER) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmCreateContext() -> win32more.Windows.Win32.UI.Input.Ime.HIMC: ...
@winfunctype('IMM32.dll')
def ImmDestroyContext(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmGetContext(param0: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.UI.Input.Ime.HIMC: ...
@winfunctype('IMM32.dll')
def ImmReleaseContext(param0: win32more.Windows.Win32.Foundation.HWND, param1: win32more.Windows.Win32.UI.Input.Ime.HIMC) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmAssociateContext(param0: win32more.Windows.Win32.Foundation.HWND, param1: win32more.Windows.Win32.UI.Input.Ime.HIMC) -> win32more.Windows.Win32.UI.Input.Ime.HIMC: ...
@winfunctype('IMM32.dll')
def ImmAssociateContextEx(param0: win32more.Windows.Win32.Foundation.HWND, param1: win32more.Windows.Win32.UI.Input.Ime.HIMC, param2: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmGetCompositionStringA(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC, param1: win32more.Windows.Win32.UI.Input.Ime.IME_COMPOSITION_STRING, lpBuf: VoidPtr, dwBufLen: UInt32) -> Int32: ...
@winfunctype('IMM32.dll')
def ImmGetCompositionStringW(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC, param1: win32more.Windows.Win32.UI.Input.Ime.IME_COMPOSITION_STRING, lpBuf: VoidPtr, dwBufLen: UInt32) -> Int32: ...
ImmGetCompositionString = UnicodeAlias('ImmGetCompositionStringW')
@winfunctype('IMM32.dll')
def ImmSetCompositionStringA(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwIndex: win32more.Windows.Win32.UI.Input.Ime.SET_COMPOSITION_STRING_TYPE, lpComp: VoidPtr, dwCompLen: UInt32, lpRead: VoidPtr, dwReadLen: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmSetCompositionStringW(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwIndex: win32more.Windows.Win32.UI.Input.Ime.SET_COMPOSITION_STRING_TYPE, lpComp: VoidPtr, dwCompLen: UInt32, lpRead: VoidPtr, dwReadLen: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
ImmSetCompositionString = UnicodeAlias('ImmSetCompositionStringW')
@winfunctype('IMM32.dll')
def ImmGetCandidateListCountA(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC, lpdwListCount: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmGetCandidateListCountW(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC, lpdwListCount: POINTER(UInt32)) -> UInt32: ...
ImmGetCandidateListCount = UnicodeAlias('ImmGetCandidateListCountW')
@winfunctype('IMM32.dll')
def ImmGetCandidateListA(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC, deIndex: UInt32, lpCandList: POINTER(win32more.Windows.Win32.UI.Input.Ime.CANDIDATELIST), dwBufLen: UInt32) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmGetCandidateListW(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC, deIndex: UInt32, lpCandList: POINTER(win32more.Windows.Win32.UI.Input.Ime.CANDIDATELIST), dwBufLen: UInt32) -> UInt32: ...
ImmGetCandidateList = UnicodeAlias('ImmGetCandidateListW')
@winfunctype('IMM32.dll')
def ImmGetGuideLineA(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwIndex: win32more.Windows.Win32.UI.Input.Ime.GET_GUIDE_LINE_TYPE, lpBuf: win32more.Windows.Win32.Foundation.PSTR, dwBufLen: UInt32) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmGetGuideLineW(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwIndex: win32more.Windows.Win32.UI.Input.Ime.GET_GUIDE_LINE_TYPE, lpBuf: win32more.Windows.Win32.Foundation.PWSTR, dwBufLen: UInt32) -> UInt32: ...
ImmGetGuideLine = UnicodeAlias('ImmGetGuideLineW')
@winfunctype('IMM32.dll')
def ImmGetConversionStatus(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC, lpfdwConversion: POINTER(win32more.Windows.Win32.UI.Input.Ime.IME_CONVERSION_MODE), lpfdwSentence: POINTER(win32more.Windows.Win32.UI.Input.Ime.IME_SENTENCE_MODE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmSetConversionStatus(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC, param1: win32more.Windows.Win32.UI.Input.Ime.IME_CONVERSION_MODE, param2: win32more.Windows.Win32.UI.Input.Ime.IME_SENTENCE_MODE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmGetOpenStatus(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmSetOpenStatus(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC, param1: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmGetCompositionFontA(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC, lplf: POINTER(win32more.Windows.Win32.Graphics.Gdi.LOGFONTA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmGetCompositionFontW(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC, lplf: POINTER(win32more.Windows.Win32.Graphics.Gdi.LOGFONTW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
ImmGetCompositionFont = UnicodeAlias('ImmGetCompositionFontW')
@winfunctype('IMM32.dll')
def ImmSetCompositionFontA(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC, lplf: POINTER(win32more.Windows.Win32.Graphics.Gdi.LOGFONTA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmSetCompositionFontW(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC, lplf: POINTER(win32more.Windows.Win32.Graphics.Gdi.LOGFONTW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
ImmSetCompositionFont = UnicodeAlias('ImmSetCompositionFontW')
@winfunctype('IMM32.dll')
def ImmConfigureIMEA(param0: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, param1: win32more.Windows.Win32.Foundation.HWND, param2: UInt32, param3: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmConfigureIMEW(param0: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, param1: win32more.Windows.Win32.Foundation.HWND, param2: UInt32, param3: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
ImmConfigureIME = UnicodeAlias('ImmConfigureIMEW')
@winfunctype('IMM32.dll')
def ImmEscapeA(param0: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, param1: win32more.Windows.Win32.UI.Input.Ime.HIMC, param2: win32more.Windows.Win32.UI.Input.Ime.IME_ESCAPE, param3: VoidPtr) -> win32more.Windows.Win32.Foundation.LRESULT: ...
@winfunctype('IMM32.dll')
def ImmEscapeW(param0: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, param1: win32more.Windows.Win32.UI.Input.Ime.HIMC, param2: win32more.Windows.Win32.UI.Input.Ime.IME_ESCAPE, param3: VoidPtr) -> win32more.Windows.Win32.Foundation.LRESULT: ...
ImmEscape = UnicodeAlias('ImmEscapeW')
@winfunctype('IMM32.dll')
def ImmGetConversionListA(param0: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, param1: win32more.Windows.Win32.UI.Input.Ime.HIMC, lpSrc: win32more.Windows.Win32.Foundation.PSTR, lpDst: POINTER(win32more.Windows.Win32.UI.Input.Ime.CANDIDATELIST), dwBufLen: UInt32, uFlag: win32more.Windows.Win32.UI.Input.Ime.GET_CONVERSION_LIST_FLAG) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmGetConversionListW(param0: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, param1: win32more.Windows.Win32.UI.Input.Ime.HIMC, lpSrc: win32more.Windows.Win32.Foundation.PWSTR, lpDst: POINTER(win32more.Windows.Win32.UI.Input.Ime.CANDIDATELIST), dwBufLen: UInt32, uFlag: win32more.Windows.Win32.UI.Input.Ime.GET_CONVERSION_LIST_FLAG) -> UInt32: ...
ImmGetConversionList = UnicodeAlias('ImmGetConversionListW')
@winfunctype('IMM32.dll')
def ImmNotifyIME(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwAction: win32more.Windows.Win32.UI.Input.Ime.NOTIFY_IME_ACTION, dwIndex: win32more.Windows.Win32.UI.Input.Ime.NOTIFY_IME_INDEX, dwValue: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmGetStatusWindowPos(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC, lpptPos: POINTER(win32more.Windows.Win32.Foundation.POINT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmSetStatusWindowPos(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC, lpptPos: POINTER(win32more.Windows.Win32.Foundation.POINT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmGetCompositionWindow(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC, lpCompForm: POINTER(win32more.Windows.Win32.UI.Input.Ime.COMPOSITIONFORM)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmSetCompositionWindow(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC, lpCompForm: POINTER(win32more.Windows.Win32.UI.Input.Ime.COMPOSITIONFORM)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmGetCandidateWindow(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC, param1: UInt32, lpCandidate: POINTER(win32more.Windows.Win32.UI.Input.Ime.CANDIDATEFORM)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmSetCandidateWindow(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC, lpCandidate: POINTER(win32more.Windows.Win32.UI.Input.Ime.CANDIDATEFORM)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmIsUIMessageA(param0: win32more.Windows.Win32.Foundation.HWND, param1: UInt32, param2: win32more.Windows.Win32.Foundation.WPARAM, param3: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmIsUIMessageW(param0: win32more.Windows.Win32.Foundation.HWND, param1: UInt32, param2: win32more.Windows.Win32.Foundation.WPARAM, param3: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.BOOL: ...
ImmIsUIMessage = UnicodeAlias('ImmIsUIMessageW')
@winfunctype('IMM32.dll')
def ImmGetVirtualKey(param0: win32more.Windows.Win32.Foundation.HWND) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmRegisterWordA(param0: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, lpszReading: win32more.Windows.Win32.Foundation.PSTR, param2: UInt32, lpszRegister: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmRegisterWordW(param0: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, lpszReading: win32more.Windows.Win32.Foundation.PWSTR, param2: UInt32, lpszRegister: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
ImmRegisterWord = UnicodeAlias('ImmRegisterWordW')
@winfunctype('IMM32.dll')
def ImmUnregisterWordA(param0: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, lpszReading: win32more.Windows.Win32.Foundation.PSTR, param2: UInt32, lpszUnregister: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmUnregisterWordW(param0: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, lpszReading: win32more.Windows.Win32.Foundation.PWSTR, param2: UInt32, lpszUnregister: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
ImmUnregisterWord = UnicodeAlias('ImmUnregisterWordW')
@winfunctype('IMM32.dll')
def ImmGetRegisterWordStyleA(param0: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, nItem: UInt32, lpStyleBuf: POINTER(win32more.Windows.Win32.UI.Input.Ime.STYLEBUFA)) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmGetRegisterWordStyleW(param0: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, nItem: UInt32, lpStyleBuf: POINTER(win32more.Windows.Win32.UI.Input.Ime.STYLEBUFW)) -> UInt32: ...
ImmGetRegisterWordStyle = UnicodeAlias('ImmGetRegisterWordStyleW')
@winfunctype('IMM32.dll')
def ImmEnumRegisterWordA(param0: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, param1: win32more.Windows.Win32.UI.Input.Ime.REGISTERWORDENUMPROCA, lpszReading: win32more.Windows.Win32.Foundation.PSTR, param3: UInt32, lpszRegister: win32more.Windows.Win32.Foundation.PSTR, param5: VoidPtr) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmEnumRegisterWordW(param0: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, param1: win32more.Windows.Win32.UI.Input.Ime.REGISTERWORDENUMPROCW, lpszReading: win32more.Windows.Win32.Foundation.PWSTR, param3: UInt32, lpszRegister: win32more.Windows.Win32.Foundation.PWSTR, param5: VoidPtr) -> UInt32: ...
ImmEnumRegisterWord = UnicodeAlias('ImmEnumRegisterWordW')
@winfunctype('IMM32.dll')
def ImmDisableIME(param0: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmEnumInputContext(idThread: UInt32, lpfn: win32more.Windows.Win32.UI.Input.Ime.IMCENUMPROC, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmGetImeMenuItemsA(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC, param1: UInt32, param2: UInt32, lpImeParentMenu: POINTER(win32more.Windows.Win32.UI.Input.Ime.IMEMENUITEMINFOA), lpImeMenu: POINTER(win32more.Windows.Win32.UI.Input.Ime.IMEMENUITEMINFOA), dwSize: UInt32) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmGetImeMenuItemsW(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC, param1: UInt32, param2: UInt32, lpImeParentMenu: POINTER(win32more.Windows.Win32.UI.Input.Ime.IMEMENUITEMINFOW), lpImeMenu: POINTER(win32more.Windows.Win32.UI.Input.Ime.IMEMENUITEMINFOW), dwSize: UInt32) -> UInt32: ...
ImmGetImeMenuItems = UnicodeAlias('ImmGetImeMenuItemsW')
@winfunctype('IMM32.dll')
def ImmDisableTextFrameService(idThread: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmDisableLegacyIME() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmGetHotKey(param0: UInt32, lpuModifiers: POINTER(UInt32), lpuVKey: POINTER(UInt32), phKL: POINTER(win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmSetHotKey(param0: UInt32, param1: UInt32, param2: UInt32, param3: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmGenerateMessage(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmRequestMessageA(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC, param1: win32more.Windows.Win32.Foundation.WPARAM, param2: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.LRESULT: ...
@winfunctype('IMM32.dll')
def ImmRequestMessageW(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC, param1: win32more.Windows.Win32.Foundation.WPARAM, param2: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.LRESULT: ...
ImmRequestMessage = UnicodeAlias('ImmRequestMessageW')
@winfunctype('IMM32.dll')
def ImmCreateSoftKeyboard(param0: UInt32, param1: win32more.Windows.Win32.Foundation.HWND, param2: Int32, param3: Int32) -> win32more.Windows.Win32.Foundation.HWND: ...
@winfunctype('IMM32.dll')
def ImmDestroySoftKeyboard(param0: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmShowSoftKeyboard(param0: win32more.Windows.Win32.Foundation.HWND, param1: Int32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmLockIMC(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC) -> POINTER(win32more.Windows.Win32.UI.Input.Ime.INPUTCONTEXT): ...
@winfunctype('IMM32.dll')
def ImmUnlockIMC(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmGetIMCLockCount(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmCreateIMCC(param0: UInt32) -> win32more.Windows.Win32.UI.Input.Ime.HIMCC: ...
@winfunctype('IMM32.dll')
def ImmDestroyIMCC(param0: win32more.Windows.Win32.UI.Input.Ime.HIMCC) -> win32more.Windows.Win32.UI.Input.Ime.HIMCC: ...
@winfunctype('IMM32.dll')
def ImmLockIMCC(param0: win32more.Windows.Win32.UI.Input.Ime.HIMCC) -> VoidPtr: ...
@winfunctype('IMM32.dll')
def ImmUnlockIMCC(param0: win32more.Windows.Win32.UI.Input.Ime.HIMCC) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmGetIMCCLockCount(param0: win32more.Windows.Win32.UI.Input.Ime.HIMCC) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmReSizeIMCC(param0: win32more.Windows.Win32.UI.Input.Ime.HIMCC, param1: UInt32) -> win32more.Windows.Win32.UI.Input.Ime.HIMCC: ...
@winfunctype('IMM32.dll')
def ImmGetIMCCSize(param0: win32more.Windows.Win32.UI.Input.Ime.HIMCC) -> UInt32: ...
class CANDIDATEFORM(Structure):
    dwIndex: UInt32
    dwStyle: UInt32
    ptCurrentPos: win32more.Windows.Win32.Foundation.POINT
    rcArea: win32more.Windows.Win32.Foundation.RECT
class CANDIDATEINFO(Structure):
    dwSize: UInt32
    dwCount: UInt32
    dwOffset: UInt32 * 32
    dwPrivateSize: UInt32
    dwPrivateOffset: UInt32
class CANDIDATELIST(Structure):
    dwSize: UInt32
    dwStyle: UInt32
    dwCount: UInt32
    dwSelection: UInt32
    dwPageStart: UInt32
    dwPageSize: UInt32
    dwOffset: UInt32 * 1
CActiveIMM = Guid('{4955dd33-b159-11d0-8fcf-00aa006bcc59}')
class COMPOSITIONFORM(Structure):
    dwStyle: UInt32
    ptCurrentPos: win32more.Windows.Win32.Foundation.POINT
    rcArea: win32more.Windows.Win32.Foundation.RECT
class COMPOSITIONSTRING(Structure):
    dwSize: UInt32
    dwCompReadAttrLen: UInt32
    dwCompReadAttrOffset: UInt32
    dwCompReadClauseLen: UInt32
    dwCompReadClauseOffset: UInt32
    dwCompReadStrLen: UInt32
    dwCompReadStrOffset: UInt32
    dwCompAttrLen: UInt32
    dwCompAttrOffset: UInt32
    dwCompClauseLen: UInt32
    dwCompClauseOffset: UInt32
    dwCompStrLen: UInt32
    dwCompStrOffset: UInt32
    dwCursorPos: UInt32
    dwDeltaStart: UInt32
    dwResultReadClauseLen: UInt32
    dwResultReadClauseOffset: UInt32
    dwResultReadStrLen: UInt32
    dwResultReadStrOffset: UInt32
    dwResultClauseLen: UInt32
    dwResultClauseOffset: UInt32
    dwResultStrLen: UInt32
    dwResultStrOffset: UInt32
    dwPrivateSize: UInt32
    dwPrivateOffset: UInt32
GET_CONVERSION_LIST_FLAG = UInt32
GCL_CONVERSION: win32more.Windows.Win32.UI.Input.Ime.GET_CONVERSION_LIST_FLAG = 1
GCL_REVERSECONVERSION: win32more.Windows.Win32.UI.Input.Ime.GET_CONVERSION_LIST_FLAG = 2
GCL_REVERSE_LENGTH: win32more.Windows.Win32.UI.Input.Ime.GET_CONVERSION_LIST_FLAG = 3
GET_GUIDE_LINE_TYPE = UInt32
GGL_LEVEL: win32more.Windows.Win32.UI.Input.Ime.GET_GUIDE_LINE_TYPE = 1
GGL_INDEX: win32more.Windows.Win32.UI.Input.Ime.GET_GUIDE_LINE_TYPE = 2
GGL_STRING: win32more.Windows.Win32.UI.Input.Ime.GET_GUIDE_LINE_TYPE = 3
GGL_PRIVATE: win32more.Windows.Win32.UI.Input.Ime.GET_GUIDE_LINE_TYPE = 4
class GUIDELINE(Structure):
    dwSize: UInt32
    dwLevel: UInt32
    dwIndex: UInt32
    dwStrLen: UInt32
    dwStrOffset: UInt32
    dwPrivateSize: UInt32
    dwPrivateOffset: UInt32
HIMC = VoidPtr
HIMCC = VoidPtr
class IActiveIME(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6fe20962-d077-11d0-8fe7-00aa006bcc59}')
    @commethod(3)
    def Inquire(self, dwSystemInfoFlags: UInt32, pIMEInfo: POINTER(win32more.Windows.Win32.UI.Input.Ime.IMEINFO), szWndClass: win32more.Windows.Win32.Foundation.PWSTR, pdwPrivate: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ConversionList(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, szSource: win32more.Windows.Win32.Foundation.PWSTR, uFlag: UInt32, uBufLen: UInt32, pDest: POINTER(win32more.Windows.Win32.UI.Input.Ime.CANDIDATELIST), puCopied: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Configure(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, hWnd: win32more.Windows.Win32.Foundation.HWND, dwMode: UInt32, pRegisterWord: POINTER(win32more.Windows.Win32.UI.Input.Ime.REGISTERWORDW)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Destroy(self, uReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Escape(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, uEscape: UInt32, pData: VoidPtr, plResult: POINTER(win32more.Windows.Win32.Foundation.LRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetActiveContext(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, fFlag: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ProcessKey(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, uVirKey: UInt32, lParam: UInt32, pbKeyState: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Notify(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwAction: UInt32, dwIndex: UInt32, dwValue: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Select(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, fSelect: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetCompositionString(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwIndex: UInt32, pComp: VoidPtr, dwCompLen: UInt32, pRead: VoidPtr, dwReadLen: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def ToAsciiEx(self, uVirKey: UInt32, uScanCode: UInt32, pbKeyState: POINTER(Byte), fuState: UInt32, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, pdwTransBuf: POINTER(UInt32), puSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def RegisterWord(self, szReading: win32more.Windows.Win32.Foundation.PWSTR, dwStyle: UInt32, szString: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def UnregisterWord(self, szReading: win32more.Windows.Win32.Foundation.PWSTR, dwStyle: UInt32, szString: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetRegisterWordStyle(self, nItem: UInt32, pStyleBuf: POINTER(win32more.Windows.Win32.UI.Input.Ime.STYLEBUFW), puBufSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def EnumRegisterWord(self, szReading: win32more.Windows.Win32.Foundation.PWSTR, dwStyle: UInt32, szRegister: win32more.Windows.Win32.Foundation.PWSTR, pData: VoidPtr, ppEnum: POINTER(win32more.Windows.Win32.UI.Input.Ime.IEnumRegisterWordW)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetCodePageA(self, uCodePage: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetLangId(self, plid: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveIME2(ComPtr):
    extends: win32more.Windows.Win32.UI.Input.Ime.IActiveIME
    _iid_ = Guid('{e1c4bf0e-2d53-11d2-93e1-0060b067b86e}')
    @commethod(20)
    def Sleep(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Unsleep(self, fDead: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveIMMApp(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{08c0e040-62d1-11d1-9326-0060b067b86e}')
    @commethod(3)
    def AssociateContext(self, hWnd: win32more.Windows.Win32.Foundation.HWND, hIME: win32more.Windows.Win32.UI.Input.Ime.HIMC, phPrev: POINTER(win32more.Windows.Win32.UI.Input.Ime.HIMC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ConfigureIMEA(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, hWnd: win32more.Windows.Win32.Foundation.HWND, dwMode: UInt32, pData: POINTER(win32more.Windows.Win32.UI.Input.Ime.REGISTERWORDA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ConfigureIMEW(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, hWnd: win32more.Windows.Win32.Foundation.HWND, dwMode: UInt32, pData: POINTER(win32more.Windows.Win32.UI.Input.Ime.REGISTERWORDW)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateContext(self, phIMC: POINTER(win32more.Windows.Win32.UI.Input.Ime.HIMC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DestroyContext(self, hIME: win32more.Windows.Win32.UI.Input.Ime.HIMC) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def EnumRegisterWordA(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, szReading: win32more.Windows.Win32.Foundation.PSTR, dwStyle: UInt32, szRegister: win32more.Windows.Win32.Foundation.PSTR, pData: VoidPtr, pEnum: POINTER(win32more.Windows.Win32.UI.Input.Ime.IEnumRegisterWordA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnumRegisterWordW(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, szReading: win32more.Windows.Win32.Foundation.PWSTR, dwStyle: UInt32, szRegister: win32more.Windows.Win32.Foundation.PWSTR, pData: VoidPtr, pEnum: POINTER(win32more.Windows.Win32.UI.Input.Ime.IEnumRegisterWordW)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EscapeA(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, uEscape: UInt32, pData: VoidPtr, plResult: POINTER(win32more.Windows.Win32.Foundation.LRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EscapeW(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, uEscape: UInt32, pData: VoidPtr, plResult: POINTER(win32more.Windows.Win32.Foundation.LRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetCandidateListA(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwIndex: UInt32, uBufLen: UInt32, pCandList: POINTER(win32more.Windows.Win32.UI.Input.Ime.CANDIDATELIST), puCopied: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetCandidateListW(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwIndex: UInt32, uBufLen: UInt32, pCandList: POINTER(win32more.Windows.Win32.UI.Input.Ime.CANDIDATELIST), puCopied: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetCandidateListCountA(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, pdwListSize: POINTER(UInt32), pdwBufLen: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetCandidateListCountW(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, pdwListSize: POINTER(UInt32), pdwBufLen: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetCandidateWindow(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwIndex: UInt32, pCandidate: POINTER(win32more.Windows.Win32.UI.Input.Ime.CANDIDATEFORM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetCompositionFontA(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, plf: POINTER(win32more.Windows.Win32.Graphics.Gdi.LOGFONTA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetCompositionFontW(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, plf: POINTER(win32more.Windows.Win32.Graphics.Gdi.LOGFONTW)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetCompositionStringA(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwIndex: UInt32, dwBufLen: UInt32, plCopied: POINTER(Int32), pBuf: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetCompositionStringW(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwIndex: UInt32, dwBufLen: UInt32, plCopied: POINTER(Int32), pBuf: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetCompositionWindow(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, pCompForm: POINTER(win32more.Windows.Win32.UI.Input.Ime.COMPOSITIONFORM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetContext(self, hWnd: win32more.Windows.Win32.Foundation.HWND, phIMC: POINTER(win32more.Windows.Win32.UI.Input.Ime.HIMC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetConversionListA(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, pSrc: win32more.Windows.Win32.Foundation.PSTR, uBufLen: UInt32, uFlag: UInt32, pDst: POINTER(win32more.Windows.Win32.UI.Input.Ime.CANDIDATELIST), puCopied: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetConversionListW(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, pSrc: win32more.Windows.Win32.Foundation.PWSTR, uBufLen: UInt32, uFlag: UInt32, pDst: POINTER(win32more.Windows.Win32.UI.Input.Ime.CANDIDATELIST), puCopied: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetConversionStatus(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, pfdwConversion: POINTER(UInt32), pfdwSentence: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetDefaultIMEWnd(self, hWnd: win32more.Windows.Win32.Foundation.HWND, phDefWnd: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def GetDescriptionA(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, uBufLen: UInt32, szDescription: win32more.Windows.Win32.Foundation.PSTR, puCopied: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetDescriptionW(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, uBufLen: UInt32, szDescription: win32more.Windows.Win32.Foundation.PWSTR, puCopied: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetGuideLineA(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwIndex: UInt32, dwBufLen: UInt32, pBuf: win32more.Windows.Win32.Foundation.PSTR, pdwResult: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetGuideLineW(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwIndex: UInt32, dwBufLen: UInt32, pBuf: win32more.Windows.Win32.Foundation.PWSTR, pdwResult: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetIMEFileNameA(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, uBufLen: UInt32, szFileName: win32more.Windows.Win32.Foundation.PSTR, puCopied: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetIMEFileNameW(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, uBufLen: UInt32, szFileName: win32more.Windows.Win32.Foundation.PWSTR, puCopied: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetOpenStatus(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetProperty(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, fdwIndex: UInt32, pdwProperty: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetRegisterWordStyleA(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, nItem: UInt32, pStyleBuf: POINTER(win32more.Windows.Win32.UI.Input.Ime.STYLEBUFA), puCopied: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def GetRegisterWordStyleW(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, nItem: UInt32, pStyleBuf: POINTER(win32more.Windows.Win32.UI.Input.Ime.STYLEBUFW), puCopied: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def GetStatusWindowPos(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, pptPos: POINTER(win32more.Windows.Win32.Foundation.POINT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def GetVirtualKey(self, hWnd: win32more.Windows.Win32.Foundation.HWND, puVirtualKey: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def InstallIMEA(self, szIMEFileName: win32more.Windows.Win32.Foundation.PSTR, szLayoutText: win32more.Windows.Win32.Foundation.PSTR, phKL: POINTER(win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def InstallIMEW(self, szIMEFileName: win32more.Windows.Win32.Foundation.PWSTR, szLayoutText: win32more.Windows.Win32.Foundation.PWSTR, phKL: POINTER(win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def IsIME(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def IsUIMessageA(self, hWndIME: win32more.Windows.Win32.Foundation.HWND, msg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def IsUIMessageW(self, hWndIME: win32more.Windows.Win32.Foundation.HWND, msg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def NotifyIME(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwAction: UInt32, dwIndex: UInt32, dwValue: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def RegisterWordA(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, szReading: win32more.Windows.Win32.Foundation.PSTR, dwStyle: UInt32, szRegister: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def RegisterWordW(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, szReading: win32more.Windows.Win32.Foundation.PWSTR, dwStyle: UInt32, szRegister: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def ReleaseContext(self, hWnd: win32more.Windows.Win32.Foundation.HWND, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def SetCandidateWindow(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, pCandidate: POINTER(win32more.Windows.Win32.UI.Input.Ime.CANDIDATEFORM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def SetCompositionFontA(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, plf: POINTER(win32more.Windows.Win32.Graphics.Gdi.LOGFONTA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def SetCompositionFontW(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, plf: POINTER(win32more.Windows.Win32.Graphics.Gdi.LOGFONTW)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def SetCompositionStringA(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwIndex: UInt32, pComp: VoidPtr, dwCompLen: UInt32, pRead: VoidPtr, dwReadLen: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def SetCompositionStringW(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwIndex: UInt32, pComp: VoidPtr, dwCompLen: UInt32, pRead: VoidPtr, dwReadLen: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def SetCompositionWindow(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, pCompForm: POINTER(win32more.Windows.Win32.UI.Input.Ime.COMPOSITIONFORM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def SetConversionStatus(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, fdwConversion: UInt32, fdwSentence: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def SetOpenStatus(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, fOpen: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def SetStatusWindowPos(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, pptPos: POINTER(win32more.Windows.Win32.Foundation.POINT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def SimulateHotKey(self, hWnd: win32more.Windows.Win32.Foundation.HWND, dwHotKeyID: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def UnregisterWordA(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, szReading: win32more.Windows.Win32.Foundation.PSTR, dwStyle: UInt32, szUnregister: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def UnregisterWordW(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, szReading: win32more.Windows.Win32.Foundation.PWSTR, dwStyle: UInt32, szUnregister: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def Activate(self, fRestoreLayout: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def Deactivate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def OnDefWindowProc(self, hWnd: win32more.Windows.Win32.Foundation.HWND, Msg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM, plResult: POINTER(win32more.Windows.Win32.Foundation.LRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def FilterClientWindows(self, aaClassList: POINTER(UInt16), uSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def GetCodePageA(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, uCodePage: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def GetLangId(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, plid: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def AssociateContextEx(self, hWnd: win32more.Windows.Win32.Foundation.HWND, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(67)
    def DisableIME(self, idThread: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(68)
    def GetImeMenuItemsA(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwFlags: UInt32, dwType: UInt32, pImeParentMenu: POINTER(win32more.Windows.Win32.UI.Input.Ime.IMEMENUITEMINFOA), pImeMenu: POINTER(win32more.Windows.Win32.UI.Input.Ime.IMEMENUITEMINFOA), dwSize: UInt32, pdwResult: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def GetImeMenuItemsW(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwFlags: UInt32, dwType: UInt32, pImeParentMenu: POINTER(win32more.Windows.Win32.UI.Input.Ime.IMEMENUITEMINFOW), pImeMenu: POINTER(win32more.Windows.Win32.UI.Input.Ime.IMEMENUITEMINFOW), dwSize: UInt32, pdwResult: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(70)
    def EnumInputContext(self, idThread: UInt32, ppEnum: POINTER(win32more.Windows.Win32.UI.Input.Ime.IEnumInputContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveIMMIME(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{08c03411-f96b-11d0-a475-00aa006bcc59}')
    @commethod(3)
    def AssociateContext(self, hWnd: win32more.Windows.Win32.Foundation.HWND, hIME: win32more.Windows.Win32.UI.Input.Ime.HIMC, phPrev: POINTER(win32more.Windows.Win32.UI.Input.Ime.HIMC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ConfigureIMEA(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, hWnd: win32more.Windows.Win32.Foundation.HWND, dwMode: UInt32, pData: POINTER(win32more.Windows.Win32.UI.Input.Ime.REGISTERWORDA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ConfigureIMEW(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, hWnd: win32more.Windows.Win32.Foundation.HWND, dwMode: UInt32, pData: POINTER(win32more.Windows.Win32.UI.Input.Ime.REGISTERWORDW)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateContext(self, phIMC: POINTER(win32more.Windows.Win32.UI.Input.Ime.HIMC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DestroyContext(self, hIME: win32more.Windows.Win32.UI.Input.Ime.HIMC) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def EnumRegisterWordA(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, szReading: win32more.Windows.Win32.Foundation.PSTR, dwStyle: UInt32, szRegister: win32more.Windows.Win32.Foundation.PSTR, pData: VoidPtr, pEnum: POINTER(win32more.Windows.Win32.UI.Input.Ime.IEnumRegisterWordA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnumRegisterWordW(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, szReading: win32more.Windows.Win32.Foundation.PWSTR, dwStyle: UInt32, szRegister: win32more.Windows.Win32.Foundation.PWSTR, pData: VoidPtr, pEnum: POINTER(win32more.Windows.Win32.UI.Input.Ime.IEnumRegisterWordW)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EscapeA(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, uEscape: UInt32, pData: VoidPtr, plResult: POINTER(win32more.Windows.Win32.Foundation.LRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EscapeW(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, uEscape: UInt32, pData: VoidPtr, plResult: POINTER(win32more.Windows.Win32.Foundation.LRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetCandidateListA(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwIndex: UInt32, uBufLen: UInt32, pCandList: POINTER(win32more.Windows.Win32.UI.Input.Ime.CANDIDATELIST), puCopied: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetCandidateListW(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwIndex: UInt32, uBufLen: UInt32, pCandList: POINTER(win32more.Windows.Win32.UI.Input.Ime.CANDIDATELIST), puCopied: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetCandidateListCountA(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, pdwListSize: POINTER(UInt32), pdwBufLen: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetCandidateListCountW(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, pdwListSize: POINTER(UInt32), pdwBufLen: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetCandidateWindow(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwIndex: UInt32, pCandidate: POINTER(win32more.Windows.Win32.UI.Input.Ime.CANDIDATEFORM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetCompositionFontA(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, plf: POINTER(win32more.Windows.Win32.Graphics.Gdi.LOGFONTA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetCompositionFontW(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, plf: POINTER(win32more.Windows.Win32.Graphics.Gdi.LOGFONTW)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetCompositionStringA(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwIndex: UInt32, dwBufLen: UInt32, plCopied: POINTER(Int32), pBuf: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetCompositionStringW(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwIndex: UInt32, dwBufLen: UInt32, plCopied: POINTER(Int32), pBuf: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetCompositionWindow(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, pCompForm: POINTER(win32more.Windows.Win32.UI.Input.Ime.COMPOSITIONFORM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetContext(self, hWnd: win32more.Windows.Win32.Foundation.HWND, phIMC: POINTER(win32more.Windows.Win32.UI.Input.Ime.HIMC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetConversionListA(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, pSrc: win32more.Windows.Win32.Foundation.PSTR, uBufLen: UInt32, uFlag: UInt32, pDst: POINTER(win32more.Windows.Win32.UI.Input.Ime.CANDIDATELIST), puCopied: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetConversionListW(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, pSrc: win32more.Windows.Win32.Foundation.PWSTR, uBufLen: UInt32, uFlag: UInt32, pDst: POINTER(win32more.Windows.Win32.UI.Input.Ime.CANDIDATELIST), puCopied: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetConversionStatus(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, pfdwConversion: POINTER(UInt32), pfdwSentence: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetDefaultIMEWnd(self, hWnd: win32more.Windows.Win32.Foundation.HWND, phDefWnd: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def GetDescriptionA(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, uBufLen: UInt32, szDescription: win32more.Windows.Win32.Foundation.PSTR, puCopied: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetDescriptionW(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, uBufLen: UInt32, szDescription: win32more.Windows.Win32.Foundation.PWSTR, puCopied: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetGuideLineA(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwIndex: UInt32, dwBufLen: UInt32, pBuf: win32more.Windows.Win32.Foundation.PSTR, pdwResult: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetGuideLineW(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwIndex: UInt32, dwBufLen: UInt32, pBuf: win32more.Windows.Win32.Foundation.PWSTR, pdwResult: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetIMEFileNameA(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, uBufLen: UInt32, szFileName: win32more.Windows.Win32.Foundation.PSTR, puCopied: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetIMEFileNameW(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, uBufLen: UInt32, szFileName: win32more.Windows.Win32.Foundation.PWSTR, puCopied: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetOpenStatus(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetProperty(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, fdwIndex: UInt32, pdwProperty: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetRegisterWordStyleA(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, nItem: UInt32, pStyleBuf: POINTER(win32more.Windows.Win32.UI.Input.Ime.STYLEBUFA), puCopied: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def GetRegisterWordStyleW(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, nItem: UInt32, pStyleBuf: POINTER(win32more.Windows.Win32.UI.Input.Ime.STYLEBUFW), puCopied: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def GetStatusWindowPos(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, pptPos: POINTER(win32more.Windows.Win32.Foundation.POINT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def GetVirtualKey(self, hWnd: win32more.Windows.Win32.Foundation.HWND, puVirtualKey: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def InstallIMEA(self, szIMEFileName: win32more.Windows.Win32.Foundation.PSTR, szLayoutText: win32more.Windows.Win32.Foundation.PSTR, phKL: POINTER(win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def InstallIMEW(self, szIMEFileName: win32more.Windows.Win32.Foundation.PWSTR, szLayoutText: win32more.Windows.Win32.Foundation.PWSTR, phKL: POINTER(win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def IsIME(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def IsUIMessageA(self, hWndIME: win32more.Windows.Win32.Foundation.HWND, msg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def IsUIMessageW(self, hWndIME: win32more.Windows.Win32.Foundation.HWND, msg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def NotifyIME(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwAction: UInt32, dwIndex: UInt32, dwValue: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def RegisterWordA(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, szReading: win32more.Windows.Win32.Foundation.PSTR, dwStyle: UInt32, szRegister: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def RegisterWordW(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, szReading: win32more.Windows.Win32.Foundation.PWSTR, dwStyle: UInt32, szRegister: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def ReleaseContext(self, hWnd: win32more.Windows.Win32.Foundation.HWND, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def SetCandidateWindow(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, pCandidate: POINTER(win32more.Windows.Win32.UI.Input.Ime.CANDIDATEFORM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def SetCompositionFontA(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, plf: POINTER(win32more.Windows.Win32.Graphics.Gdi.LOGFONTA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def SetCompositionFontW(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, plf: POINTER(win32more.Windows.Win32.Graphics.Gdi.LOGFONTW)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def SetCompositionStringA(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwIndex: UInt32, pComp: VoidPtr, dwCompLen: UInt32, pRead: VoidPtr, dwReadLen: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def SetCompositionStringW(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwIndex: UInt32, pComp: VoidPtr, dwCompLen: UInt32, pRead: VoidPtr, dwReadLen: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def SetCompositionWindow(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, pCompForm: POINTER(win32more.Windows.Win32.UI.Input.Ime.COMPOSITIONFORM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def SetConversionStatus(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, fdwConversion: UInt32, fdwSentence: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def SetOpenStatus(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, fOpen: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def SetStatusWindowPos(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, pptPos: POINTER(win32more.Windows.Win32.Foundation.POINT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def SimulateHotKey(self, hWnd: win32more.Windows.Win32.Foundation.HWND, dwHotKeyID: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def UnregisterWordA(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, szReading: win32more.Windows.Win32.Foundation.PSTR, dwStyle: UInt32, szUnregister: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def UnregisterWordW(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, szReading: win32more.Windows.Win32.Foundation.PWSTR, dwStyle: UInt32, szUnregister: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def GenerateMessage(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def LockIMC(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, ppIMC: POINTER(POINTER(win32more.Windows.Win32.UI.Input.Ime.INPUTCONTEXT))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def UnlockIMC(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def GetIMCLockCount(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, pdwLockCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def CreateIMCC(self, dwSize: UInt32, phIMCC: POINTER(win32more.Windows.Win32.UI.Input.Ime.HIMCC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def DestroyIMCC(self, hIMCC: win32more.Windows.Win32.UI.Input.Ime.HIMCC) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def LockIMCC(self, hIMCC: win32more.Windows.Win32.UI.Input.Ime.HIMCC, ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(67)
    def UnlockIMCC(self, hIMCC: win32more.Windows.Win32.UI.Input.Ime.HIMCC) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(68)
    def ReSizeIMCC(self, hIMCC: win32more.Windows.Win32.UI.Input.Ime.HIMCC, dwSize: UInt32, phIMCC: POINTER(win32more.Windows.Win32.UI.Input.Ime.HIMCC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def GetIMCCSize(self, hIMCC: win32more.Windows.Win32.UI.Input.Ime.HIMCC, pdwSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(70)
    def GetIMCCLockCount(self, hIMCC: win32more.Windows.Win32.UI.Input.Ime.HIMCC, pdwLockCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(71)
    def GetHotKey(self, dwHotKeyID: UInt32, puModifiers: POINTER(UInt32), puVKey: POINTER(UInt32), phKL: POINTER(win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(72)
    def SetHotKey(self, dwHotKeyID: UInt32, uModifiers: UInt32, uVKey: UInt32, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(73)
    def CreateSoftKeyboard(self, uType: UInt32, hOwner: win32more.Windows.Win32.Foundation.HWND, x: Int32, y: Int32, phSoftKbdWnd: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(74)
    def DestroySoftKeyboard(self, hSoftKbdWnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(75)
    def ShowSoftKeyboard(self, hSoftKbdWnd: win32more.Windows.Win32.Foundation.HWND, nCmdShow: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(76)
    def GetCodePageA(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, uCodePage: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(77)
    def GetLangId(self, hKL: win32more.Windows.Win32.UI.Input.KeyboardAndMouse.HKL, plid: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(78)
    def KeybdEvent(self, lgidIME: UInt16, bVk: Byte, bScan: Byte, dwFlags: UInt32, dwExtraInfo: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(79)
    def LockModal(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(80)
    def UnlockModal(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(81)
    def AssociateContextEx(self, hWnd: win32more.Windows.Win32.Foundation.HWND, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(82)
    def DisableIME(self, idThread: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(83)
    def GetImeMenuItemsA(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwFlags: UInt32, dwType: UInt32, pImeParentMenu: POINTER(win32more.Windows.Win32.UI.Input.Ime.IMEMENUITEMINFOA), pImeMenu: POINTER(win32more.Windows.Win32.UI.Input.Ime.IMEMENUITEMINFOA), dwSize: UInt32, pdwResult: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(84)
    def GetImeMenuItemsW(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, dwFlags: UInt32, dwType: UInt32, pImeParentMenu: POINTER(win32more.Windows.Win32.UI.Input.Ime.IMEMENUITEMINFOW), pImeMenu: POINTER(win32more.Windows.Win32.UI.Input.Ime.IMEMENUITEMINFOW), dwSize: UInt32, pdwResult: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(85)
    def EnumInputContext(self, idThread: UInt32, ppEnum: POINTER(win32more.Windows.Win32.UI.Input.Ime.IEnumInputContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(86)
    def RequestMessageA(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM, plResult: POINTER(win32more.Windows.Win32.Foundation.LRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(87)
    def RequestMessageW(self, hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM, plResult: POINTER(win32more.Windows.Win32.Foundation.LRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(88)
    def SendIMCA(self, hWnd: win32more.Windows.Win32.Foundation.HWND, uMsg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM, plResult: POINTER(win32more.Windows.Win32.Foundation.LRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(89)
    def SendIMCW(self, hWnd: win32more.Windows.Win32.Foundation.HWND, uMsg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM, plResult: POINTER(win32more.Windows.Win32.Foundation.LRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(90)
    def IsSleeping(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveIMMMessagePumpOwner(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b5cf2cfa-8aeb-11d1-9364-0060b067b86e}')
    @commethod(3)
    def Start(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def End(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnTranslateMessage(self, pMsg: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.MSG)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Pause(self, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Resume(self, dwCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveIMMRegistrar(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b3458082-bd00-11d1-939b-0060b067b86e}')
    @commethod(3)
    def RegisterIME(self, rclsid: POINTER(Guid), lgid: UInt16, pszIconFile: win32more.Windows.Win32.Foundation.PWSTR, pszDesc: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterIME(self, rclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumInputContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{09b5eab0-f997-11d1-93d4-0060b067b86e}')
    @commethod(3)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.UI.Input.Ime.IEnumInputContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(self, ulCount: UInt32, rgInputContext: POINTER(win32more.Windows.Win32.UI.Input.Ime.HIMC), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(self, ulCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumRegisterWordA(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{08c03412-f96b-11d0-a475-00aa006bcc59}')
    @commethod(3)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.UI.Input.Ime.IEnumRegisterWordA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(self, ulCount: UInt32, rgRegisterWord: POINTER(win32more.Windows.Win32.UI.Input.Ime.REGISTERWORDA), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(self, ulCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumRegisterWordW(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4955dd31-b159-11d0-8fcf-00aa006bcc59}')
    @commethod(3)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.UI.Input.Ime.IEnumRegisterWordW)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(self, ulCount: UInt32, rgRegisterWord: POINTER(win32more.Windows.Win32.UI.Input.Ime.REGISTERWORDW), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(self, ulCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
IEnumRegisterWord = UnicodeAlias('IEnumRegisterWordW')
class IFEClassFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IClassFactory
class IFECommon(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{019f7151-e6db-11d0-83c3-00c04fddb82e}')
    @commethod(3)
    def IsDefaultIME(self, szName: win32more.Windows.Win32.Foundation.PSTR, cszName: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetDefaultIME(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InvokeWordRegDialog(self, pimedlg: POINTER(win32more.Windows.Win32.UI.Input.Ime.IMEDLG)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def InvokeDictToolDialog(self, pimedlg: POINTER(win32more.Windows.Win32.UI.Input.Ime.IMEDLG)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFEDictionary(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{019f7153-e6db-11d0-83c3-00c04fddb82e}')
    @commethod(3)
    def Open(self, pchDictPath: win32more.Windows.Win32.Foundation.PSTR, pshf: POINTER(win32more.Windows.Win32.UI.Input.Ime.IMESHF)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetHeader(self, pchDictPath: win32more.Windows.Win32.Foundation.PSTR, pshf: POINTER(win32more.Windows.Win32.UI.Input.Ime.IMESHF), pjfmt: POINTER(win32more.Windows.Win32.UI.Input.Ime.IMEFMT), pulType: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DisplayProperty(self, hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPosTable(self, prgPosTbl: POINTER(POINTER(win32more.Windows.Win32.UI.Input.Ime.POSTBL)), pcPosTbl: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetWords(self, pwchFirst: win32more.Windows.Win32.Foundation.PWSTR, pwchLast: win32more.Windows.Win32.Foundation.PWSTR, pwchDisplay: win32more.Windows.Win32.Foundation.PWSTR, ulPos: UInt32, ulSelect: UInt32, ulWordSrc: UInt32, pchBuffer: POINTER(Byte), cbBuffer: UInt32, pcWrd: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def NextWords(self, pchBuffer: POINTER(Byte), cbBuffer: UInt32, pcWrd: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Create(self, pchDictPath: win32more.Windows.Win32.Foundation.PSTR, pshf: POINTER(win32more.Windows.Win32.UI.Input.Ime.IMESHF)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetHeader(self, pshf: POINTER(win32more.Windows.Win32.UI.Input.Ime.IMESHF)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ExistWord(self, pwrd: POINTER(win32more.Windows.Win32.UI.Input.Ime.IMEWRD)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def ExistDependency(self, pdp: POINTER(win32more.Windows.Win32.UI.Input.Ime.IMEDP)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def RegisterWord(self, reg: win32more.Windows.Win32.UI.Input.Ime.IMEREG, pwrd: POINTER(win32more.Windows.Win32.UI.Input.Ime.IMEWRD)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def RegisterDependency(self, reg: win32more.Windows.Win32.UI.Input.Ime.IMEREG, pdp: POINTER(win32more.Windows.Win32.UI.Input.Ime.IMEDP)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetDependencies(self, pwchKakariReading: win32more.Windows.Win32.Foundation.PWSTR, pwchKakariDisplay: win32more.Windows.Win32.Foundation.PWSTR, ulKakariPos: UInt32, pwchUkeReading: win32more.Windows.Win32.Foundation.PWSTR, pwchUkeDisplay: win32more.Windows.Win32.Foundation.PWSTR, ulUkePos: UInt32, jrel: win32more.Windows.Win32.UI.Input.Ime.IMEREL, ulWordSrc: UInt32, pchBuffer: POINTER(Byte), cbBuffer: UInt32, pcdp: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def NextDependencies(self, pchBuffer: POINTER(Byte), cbBuffer: UInt32, pcDp: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def ConvertFromOldMSIME(self, pchDic: win32more.Windows.Win32.Foundation.PSTR, pfnLog: win32more.Windows.Win32.UI.Input.Ime.PFNLOG, reg: win32more.Windows.Win32.UI.Input.Ime.IMEREG) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def ConvertFromUserToSys(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFELanguage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{019f7152-e6db-11d0-83c3-00c04fddb82e}')
    @commethod(3)
    def Open(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetJMorphResult(self, dwRequest: UInt32, dwCMode: UInt32, cwchInput: Int32, pwchInput: win32more.Windows.Win32.Foundation.PWSTR, pfCInfo: POINTER(UInt32), ppResult: POINTER(POINTER(win32more.Windows.Win32.UI.Input.Ime.MORRSLT))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetConversionModeCaps(self, pdwCaps: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPhonetic(self, string: win32more.Windows.Win32.Foundation.BSTR, start: Int32, length: Int32, phonetic: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetConversion(self, string: win32more.Windows.Win32.Foundation.BSTR, start: Int32, length: Int32, result: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IImePad(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5d8e643a-c3a9-11d1-afef-00805f0c8b6d}')
    @commethod(3)
    def Request(self, pIImePadApplet: win32more.Windows.Win32.UI.Input.Ime.IImePadApplet, reqId: Int32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IImePadApplet(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5d8e643b-c3a9-11d1-afef-00805f0c8b6d}')
    @commethod(3)
    def Initialize(self, lpIImePad: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Terminate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAppletConfig(self, lpAppletCfg: POINTER(win32more.Windows.Win32.UI.Input.Ime.IMEAPPLETCFG)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateUI(self, hwndParent: win32more.Windows.Win32.Foundation.HWND, lpImeAppletUI: POINTER(win32more.Windows.Win32.UI.Input.Ime.IMEAPPLETUI)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Notify(self, lpImePad: win32more.Windows.Win32.System.Com.IUnknown, notify: Int32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IImePlugInDictDictionaryList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{98752974-b0a6-489b-8f6f-bff3769c8eeb}')
    @commethod(3)
    def GetDictionariesInUse(self, prgDictionaryGUID: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)), prgDateCreated: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)), prgfEncrypted: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DeleteDictionary(self, bstrDictionaryGUID: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IImeSpecifyApplets(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5d8e643c-c3a9-11d1-afef-00805f0c8b6d}')
    @commethod(3)
    def GetAppletIIDList(self, refiid: POINTER(Guid), lpIIDList: POINTER(win32more.Windows.Win32.UI.Input.Ime.APPLETIDLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def IMCENUMPROC(param0: win32more.Windows.Win32.UI.Input.Ime.HIMC, param1: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.BOOL: ...
class IMEAPPLETCFG(Structure):
    dwConfig: UInt32
    wchTitle: Char * 64
    wchTitleFontFace: Char * 32
    dwCharSet: UInt32
    iCategory: Int32
    hIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON
    langID: UInt16
    dummy: UInt16
    lReserved1: win32more.Windows.Win32.Foundation.LPARAM
class IMEAPPLETUI(Structure):
    hwnd: win32more.Windows.Win32.Foundation.HWND
    dwStyle: UInt32
    width: Int32
    height: Int32
    minWidth: Int32
    minHeight: Int32
    maxWidth: Int32
    maxHeight: Int32
    lReserved1: win32more.Windows.Win32.Foundation.LPARAM
    lReserved2: win32more.Windows.Win32.Foundation.LPARAM
class IMECHARINFO(Structure):
    wch: Char
    dwCharInfo: UInt32
class IMECHARPOSITION(Structure):
    dwSize: UInt32
    dwCharPos: UInt32
    pt: win32more.Windows.Win32.Foundation.POINT
    cLineHeight: UInt32
    rcDocument: win32more.Windows.Win32.Foundation.RECT
class IMECOMPOSITIONSTRINGINFO(Structure):
    iCompStrLen: Int32
    iCaretPos: Int32
    iEditStart: Int32
    iEditLen: Int32
    iTargetStart: Int32
    iTargetLen: Int32
class IMEDLG(Structure):
    cbIMEDLG: Int32
    hwnd: win32more.Windows.Win32.Foundation.HWND
    lpwstrWord: win32more.Windows.Win32.Foundation.PWSTR
    nTabId: Int32
    _pack_ = 1
class IMEDP(Structure):
    wrdModifier: win32more.Windows.Win32.UI.Input.Ime.IMEWRD
    wrdModifiee: win32more.Windows.Win32.UI.Input.Ime.IMEWRD
    relID: win32more.Windows.Win32.UI.Input.Ime.IMEREL
    _pack_ = 1
class IMEFAREASTINFO(Structure):
    dwSize: UInt32
    dwType: UInt32
    dwData: UInt32 * 1
IMEFMT = Int32
IFED_UNKNOWN: win32more.Windows.Win32.UI.Input.Ime.IMEFMT = 0
IFED_MSIME2_BIN_SYSTEM: win32more.Windows.Win32.UI.Input.Ime.IMEFMT = 1
IFED_MSIME2_BIN_USER: win32more.Windows.Win32.UI.Input.Ime.IMEFMT = 2
IFED_MSIME2_TEXT_USER: win32more.Windows.Win32.UI.Input.Ime.IMEFMT = 3
IFED_MSIME95_BIN_SYSTEM: win32more.Windows.Win32.UI.Input.Ime.IMEFMT = 4
IFED_MSIME95_BIN_USER: win32more.Windows.Win32.UI.Input.Ime.IMEFMT = 5
IFED_MSIME95_TEXT_USER: win32more.Windows.Win32.UI.Input.Ime.IMEFMT = 6
IFED_MSIME97_BIN_SYSTEM: win32more.Windows.Win32.UI.Input.Ime.IMEFMT = 7
IFED_MSIME97_BIN_USER: win32more.Windows.Win32.UI.Input.Ime.IMEFMT = 8
IFED_MSIME97_TEXT_USER: win32more.Windows.Win32.UI.Input.Ime.IMEFMT = 9
IFED_MSIME98_BIN_SYSTEM: win32more.Windows.Win32.UI.Input.Ime.IMEFMT = 10
IFED_MSIME98_BIN_USER: win32more.Windows.Win32.UI.Input.Ime.IMEFMT = 11
IFED_MSIME98_TEXT_USER: win32more.Windows.Win32.UI.Input.Ime.IMEFMT = 12
IFED_ACTIVE_DICT: win32more.Windows.Win32.UI.Input.Ime.IMEFMT = 13
IFED_ATOK9: win32more.Windows.Win32.UI.Input.Ime.IMEFMT = 14
IFED_ATOK10: win32more.Windows.Win32.UI.Input.Ime.IMEFMT = 15
IFED_NEC_AI_: win32more.Windows.Win32.UI.Input.Ime.IMEFMT = 16
IFED_WX_II: win32more.Windows.Win32.UI.Input.Ime.IMEFMT = 17
IFED_WX_III: win32more.Windows.Win32.UI.Input.Ime.IMEFMT = 18
IFED_VJE_20: win32more.Windows.Win32.UI.Input.Ime.IMEFMT = 19
IFED_MSIME98_SYSTEM_CE: win32more.Windows.Win32.UI.Input.Ime.IMEFMT = 20
IFED_MSIME_BIN_SYSTEM: win32more.Windows.Win32.UI.Input.Ime.IMEFMT = 21
IFED_MSIME_BIN_USER: win32more.Windows.Win32.UI.Input.Ime.IMEFMT = 22
IFED_MSIME_TEXT_USER: win32more.Windows.Win32.UI.Input.Ime.IMEFMT = 23
IFED_PIME2_BIN_USER: win32more.Windows.Win32.UI.Input.Ime.IMEFMT = 24
IFED_PIME2_BIN_SYSTEM: win32more.Windows.Win32.UI.Input.Ime.IMEFMT = 25
IFED_PIME2_BIN_STANDARD_SYSTEM: win32more.Windows.Win32.UI.Input.Ime.IMEFMT = 26
class IMEINFO(Structure):
    dwPrivateDataSize: UInt32
    fdwProperty: UInt32
    fdwConversionCaps: UInt32
    fdwSentenceCaps: UInt32
    fdwUICaps: UInt32
    fdwSCSCaps: UInt32
    fdwSelectCaps: UInt32
class IMEITEM(Structure):
    cbSize: Int32
    iType: Int32
    lpItemData: VoidPtr
class IMEITEMCANDIDATE(Structure):
    uCount: UInt32
    imeItem: win32more.Windows.Win32.UI.Input.Ime.IMEITEM * 1
class IMEKMS(Structure):
    cbSize: Int32
    hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC
    cKeyList: UInt32
    pKeyList: POINTER(win32more.Windows.Win32.UI.Input.Ime.IMEKMSKEY)
    _pack_ = 1
class IMEKMSFUNCDESC(Structure):
    cbSize: Int32
    idLang: UInt16
    dwControl: UInt32
    pwszDescription: Char * 128
    _pack_ = 1
class IMEKMSINIT(Structure):
    cbSize: Int32
    hWnd: win32more.Windows.Win32.Foundation.HWND
    _pack_ = 1
class IMEKMSINVK(Structure):
    cbSize: Int32
    hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC
    dwControl: UInt32
    _pack_ = 1
class IMEKMSKEY(Structure):
    dwStatus: UInt32
    dwCompStatus: UInt32
    dwVKEY: UInt32
    Anonymous1: _Anonymous1_e__Union
    Anonymous2: _Anonymous2_e__Union
    _pack_ = 1
    class _Anonymous1_e__Union(Union):
        dwControl: UInt32
        dwNotUsed: UInt32
        _pack_ = 1
    class _Anonymous2_e__Union(Union):
        pwszDscr: Char * 31
        pwszNoUse: Char * 31
        _pack_ = 1
class IMEKMSKMP(Structure):
    cbSize: Int32
    hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC
    idLang: UInt16
    wVKStart: UInt16
    wVKEnd: UInt16
    cKeyList: Int32
    pKeyList: POINTER(win32more.Windows.Win32.UI.Input.Ime.IMEKMSKEY)
    _pack_ = 1
class IMEKMSNTFY(Structure):
    cbSize: Int32
    hIMC: win32more.Windows.Win32.UI.Input.Ime.HIMC
    fSelect: win32more.Windows.Win32.Foundation.BOOL
    _pack_ = 1
class IMEMENUITEMINFOA(Structure):
    cbSize: UInt32
    fType: UInt32
    fState: UInt32
    wID: UInt32
    hbmpChecked: win32more.Windows.Win32.Graphics.Gdi.HBITMAP
    hbmpUnchecked: win32more.Windows.Win32.Graphics.Gdi.HBITMAP
    dwItemData: UInt32
    szString: win32more.Windows.Win32.Foundation.CHAR * 80
    hbmpItem: win32more.Windows.Win32.Graphics.Gdi.HBITMAP
class IMEMENUITEMINFOW(Structure):
    cbSize: UInt32
    fType: UInt32
    fState: UInt32
    wID: UInt32
    hbmpChecked: win32more.Windows.Win32.Graphics.Gdi.HBITMAP
    hbmpUnchecked: win32more.Windows.Win32.Graphics.Gdi.HBITMAP
    dwItemData: UInt32
    szString: Char * 80
    hbmpItem: win32more.Windows.Win32.Graphics.Gdi.HBITMAP
IMEMENUITEMINFO = UnicodeAlias('IMEMENUITEMINFOW')
IMEREG = Int32
IFED_REG_HEAD: win32more.Windows.Win32.UI.Input.Ime.IMEREG = 0
IFED_REG_TAIL: win32more.Windows.Win32.UI.Input.Ime.IMEREG = 1
IFED_REG_DEL: win32more.Windows.Win32.UI.Input.Ime.IMEREG = 2
IMEREL = Int32
IFED_REL_NONE: win32more.Windows.Win32.UI.Input.Ime.IMEREL = 0
IFED_REL_NO: win32more.Windows.Win32.UI.Input.Ime.IMEREL = 1
IFED_REL_GA: win32more.Windows.Win32.UI.Input.Ime.IMEREL = 2
IFED_REL_WO: win32more.Windows.Win32.UI.Input.Ime.IMEREL = 3
IFED_REL_NI: win32more.Windows.Win32.UI.Input.Ime.IMEREL = 4
IFED_REL_DE: win32more.Windows.Win32.UI.Input.Ime.IMEREL = 5
IFED_REL_YORI: win32more.Windows.Win32.UI.Input.Ime.IMEREL = 6
IFED_REL_KARA: win32more.Windows.Win32.UI.Input.Ime.IMEREL = 7
IFED_REL_MADE: win32more.Windows.Win32.UI.Input.Ime.IMEREL = 8
IFED_REL_HE: win32more.Windows.Win32.UI.Input.Ime.IMEREL = 9
IFED_REL_TO: win32more.Windows.Win32.UI.Input.Ime.IMEREL = 10
IFED_REL_IDEOM: win32more.Windows.Win32.UI.Input.Ime.IMEREL = 11
IFED_REL_FUKU_YOUGEN: win32more.Windows.Win32.UI.Input.Ime.IMEREL = 12
IFED_REL_KEIYOU_YOUGEN: win32more.Windows.Win32.UI.Input.Ime.IMEREL = 13
IFED_REL_KEIDOU1_YOUGEN: win32more.Windows.Win32.UI.Input.Ime.IMEREL = 14
IFED_REL_KEIDOU2_YOUGEN: win32more.Windows.Win32.UI.Input.Ime.IMEREL = 15
IFED_REL_TAIGEN: win32more.Windows.Win32.UI.Input.Ime.IMEREL = 16
IFED_REL_YOUGEN: win32more.Windows.Win32.UI.Input.Ime.IMEREL = 17
IFED_REL_RENTAI_MEI: win32more.Windows.Win32.UI.Input.Ime.IMEREL = 18
IFED_REL_RENSOU: win32more.Windows.Win32.UI.Input.Ime.IMEREL = 19
IFED_REL_KEIYOU_TO_YOUGEN: win32more.Windows.Win32.UI.Input.Ime.IMEREL = 20
IFED_REL_KEIYOU_TARU_YOUGEN: win32more.Windows.Win32.UI.Input.Ime.IMEREL = 21
IFED_REL_UNKNOWN1: win32more.Windows.Win32.UI.Input.Ime.IMEREL = 22
IFED_REL_UNKNOWN2: win32more.Windows.Win32.UI.Input.Ime.IMEREL = 23
IFED_REL_ALL: win32more.Windows.Win32.UI.Input.Ime.IMEREL = 24
class IMESHF(Structure):
    cbShf: UInt16
    verDic: UInt16
    szTitle: win32more.Windows.Win32.Foundation.CHAR * 48
    szDescription: win32more.Windows.Win32.Foundation.CHAR * 256
    szCopyright: win32more.Windows.Win32.Foundation.CHAR * 128
    _pack_ = 1
class IMESTRINGCANDIDATE(Structure):
    uCount: UInt32
    lpwstr: win32more.Windows.Win32.Foundation.PWSTR * 1
class IMESTRINGCANDIDATEINFO(Structure):
    dwFarEastId: UInt32
    lpFarEastInfo: POINTER(win32more.Windows.Win32.UI.Input.Ime.IMEFAREASTINFO)
    fInfoMask: UInt32
    iSelIndex: Int32
    uCount: UInt32
    lpwstr: win32more.Windows.Win32.Foundation.PWSTR * 1
class IMESTRINGINFO(Structure):
    dwFarEastId: UInt32
    lpwstr: win32more.Windows.Win32.Foundation.PWSTR
IMEUCT = Int32
IFED_UCT_NONE: win32more.Windows.Win32.UI.Input.Ime.IMEUCT = 0
IFED_UCT_STRING_SJIS: win32more.Windows.Win32.UI.Input.Ime.IMEUCT = 1
IFED_UCT_STRING_UNICODE: win32more.Windows.Win32.UI.Input.Ime.IMEUCT = 2
IFED_UCT_USER_DEFINED: win32more.Windows.Win32.UI.Input.Ime.IMEUCT = 3
IFED_UCT_MAX: win32more.Windows.Win32.UI.Input.Ime.IMEUCT = 4
class IMEWRD(Structure):
    pwchReading: win32more.Windows.Win32.Foundation.PWSTR
    pwchDisplay: win32more.Windows.Win32.Foundation.PWSTR
    Anonymous: _Anonymous_e__Union
    rgulAttrs: UInt32 * 2
    cbComment: Int32
    uct: win32more.Windows.Win32.UI.Input.Ime.IMEUCT
    pvComment: VoidPtr
    _pack_ = 1
    class _Anonymous_e__Union(Union):
        ulPos: UInt32
        Anonymous: _Anonymous_e__Struct
        _pack_ = 1
        class _Anonymous_e__Struct(Structure):
            nPos1: UInt16
            nPos2: UInt16
            _pack_ = 1
IME_COMPOSITION_STRING = UInt32
GCS_COMPREADSTR: win32more.Windows.Win32.UI.Input.Ime.IME_COMPOSITION_STRING = 1
GCS_COMPREADATTR: win32more.Windows.Win32.UI.Input.Ime.IME_COMPOSITION_STRING = 2
GCS_COMPREADCLAUSE: win32more.Windows.Win32.UI.Input.Ime.IME_COMPOSITION_STRING = 4
GCS_COMPSTR: win32more.Windows.Win32.UI.Input.Ime.IME_COMPOSITION_STRING = 8
GCS_COMPATTR: win32more.Windows.Win32.UI.Input.Ime.IME_COMPOSITION_STRING = 16
GCS_COMPCLAUSE: win32more.Windows.Win32.UI.Input.Ime.IME_COMPOSITION_STRING = 32
GCS_CURSORPOS: win32more.Windows.Win32.UI.Input.Ime.IME_COMPOSITION_STRING = 128
GCS_DELTASTART: win32more.Windows.Win32.UI.Input.Ime.IME_COMPOSITION_STRING = 256
GCS_RESULTREADSTR: win32more.Windows.Win32.UI.Input.Ime.IME_COMPOSITION_STRING = 512
GCS_RESULTREADCLAUSE: win32more.Windows.Win32.UI.Input.Ime.IME_COMPOSITION_STRING = 1024
GCS_RESULTSTR: win32more.Windows.Win32.UI.Input.Ime.IME_COMPOSITION_STRING = 2048
GCS_RESULTCLAUSE: win32more.Windows.Win32.UI.Input.Ime.IME_COMPOSITION_STRING = 4096
IME_CONVERSION_MODE = UInt32
IME_CMODE_ALPHANUMERIC: win32more.Windows.Win32.UI.Input.Ime.IME_CONVERSION_MODE = 0
IME_CMODE_NATIVE: win32more.Windows.Win32.UI.Input.Ime.IME_CONVERSION_MODE = 1
IME_CMODE_CHINESE: win32more.Windows.Win32.UI.Input.Ime.IME_CONVERSION_MODE = 1
IME_CMODE_HANGUL: win32more.Windows.Win32.UI.Input.Ime.IME_CONVERSION_MODE = 1
IME_CMODE_JAPANESE: win32more.Windows.Win32.UI.Input.Ime.IME_CONVERSION_MODE = 1
IME_CMODE_KATAKANA: win32more.Windows.Win32.UI.Input.Ime.IME_CONVERSION_MODE = 2
IME_CMODE_LANGUAGE: win32more.Windows.Win32.UI.Input.Ime.IME_CONVERSION_MODE = 3
IME_CMODE_FULLSHAPE: win32more.Windows.Win32.UI.Input.Ime.IME_CONVERSION_MODE = 8
IME_CMODE_ROMAN: win32more.Windows.Win32.UI.Input.Ime.IME_CONVERSION_MODE = 16
IME_CMODE_CHARCODE: win32more.Windows.Win32.UI.Input.Ime.IME_CONVERSION_MODE = 32
IME_CMODE_HANJACONVERT: win32more.Windows.Win32.UI.Input.Ime.IME_CONVERSION_MODE = 64
IME_CMODE_NATIVESYMBOL: win32more.Windows.Win32.UI.Input.Ime.IME_CONVERSION_MODE = 128
IME_CMODE_HANGEUL: win32more.Windows.Win32.UI.Input.Ime.IME_CONVERSION_MODE = 1
IME_CMODE_SOFTKBD: win32more.Windows.Win32.UI.Input.Ime.IME_CONVERSION_MODE = 128
IME_CMODE_NOCONVERSION: win32more.Windows.Win32.UI.Input.Ime.IME_CONVERSION_MODE = 256
IME_CMODE_EUDC: win32more.Windows.Win32.UI.Input.Ime.IME_CONVERSION_MODE = 512
IME_CMODE_SYMBOL: win32more.Windows.Win32.UI.Input.Ime.IME_CONVERSION_MODE = 1024
IME_CMODE_FIXED: win32more.Windows.Win32.UI.Input.Ime.IME_CONVERSION_MODE = 2048
IME_CMODE_RESERVED: win32more.Windows.Win32.UI.Input.Ime.IME_CONVERSION_MODE = 4026531840
IME_ESCAPE = UInt32
IME_ESC_QUERY_SUPPORT: win32more.Windows.Win32.UI.Input.Ime.IME_ESCAPE = 3
IME_ESC_RESERVED_FIRST: win32more.Windows.Win32.UI.Input.Ime.IME_ESCAPE = 4
IME_ESC_RESERVED_LAST: win32more.Windows.Win32.UI.Input.Ime.IME_ESCAPE = 2047
IME_ESC_PRIVATE_FIRST: win32more.Windows.Win32.UI.Input.Ime.IME_ESCAPE = 2048
IME_ESC_PRIVATE_LAST: win32more.Windows.Win32.UI.Input.Ime.IME_ESCAPE = 4095
IME_ESC_SEQUENCE_TO_INTERNAL: win32more.Windows.Win32.UI.Input.Ime.IME_ESCAPE = 4097
IME_ESC_GET_EUDC_DICTIONARY: win32more.Windows.Win32.UI.Input.Ime.IME_ESCAPE = 4099
IME_ESC_SET_EUDC_DICTIONARY: win32more.Windows.Win32.UI.Input.Ime.IME_ESCAPE = 4100
IME_ESC_MAX_KEY: win32more.Windows.Win32.UI.Input.Ime.IME_ESCAPE = 4101
IME_ESC_IME_NAME: win32more.Windows.Win32.UI.Input.Ime.IME_ESCAPE = 4102
IME_ESC_SYNC_HOTKEY: win32more.Windows.Win32.UI.Input.Ime.IME_ESCAPE = 4103
IME_ESC_HANJA_MODE: win32more.Windows.Win32.UI.Input.Ime.IME_ESCAPE = 4104
IME_ESC_AUTOMATA: win32more.Windows.Win32.UI.Input.Ime.IME_ESCAPE = 4105
IME_ESC_PRIVATE_HOTKEY: win32more.Windows.Win32.UI.Input.Ime.IME_ESCAPE = 4106
IME_ESC_GETHELPFILENAME: win32more.Windows.Win32.UI.Input.Ime.IME_ESCAPE = 4107
IME_HOTKEY_IDENTIFIER = UInt32
IME_CHOTKEY_IME_NONIME_TOGGLE: win32more.Windows.Win32.UI.Input.Ime.IME_HOTKEY_IDENTIFIER = 16
IME_CHOTKEY_SHAPE_TOGGLE: win32more.Windows.Win32.UI.Input.Ime.IME_HOTKEY_IDENTIFIER = 17
IME_CHOTKEY_SYMBOL_TOGGLE: win32more.Windows.Win32.UI.Input.Ime.IME_HOTKEY_IDENTIFIER = 18
IME_JHOTKEY_CLOSE_OPEN: win32more.Windows.Win32.UI.Input.Ime.IME_HOTKEY_IDENTIFIER = 48
IME_KHOTKEY_SHAPE_TOGGLE: win32more.Windows.Win32.UI.Input.Ime.IME_HOTKEY_IDENTIFIER = 80
IME_KHOTKEY_HANJACONVERT: win32more.Windows.Win32.UI.Input.Ime.IME_HOTKEY_IDENTIFIER = 81
IME_KHOTKEY_ENGLISH: win32more.Windows.Win32.UI.Input.Ime.IME_HOTKEY_IDENTIFIER = 82
IME_THOTKEY_IME_NONIME_TOGGLE: win32more.Windows.Win32.UI.Input.Ime.IME_HOTKEY_IDENTIFIER = 112
IME_THOTKEY_SHAPE_TOGGLE: win32more.Windows.Win32.UI.Input.Ime.IME_HOTKEY_IDENTIFIER = 113
IME_THOTKEY_SYMBOL_TOGGLE: win32more.Windows.Win32.UI.Input.Ime.IME_HOTKEY_IDENTIFIER = 114
IME_ITHOTKEY_RESEND_RESULTSTR: win32more.Windows.Win32.UI.Input.Ime.IME_HOTKEY_IDENTIFIER = 512
IME_ITHOTKEY_PREVIOUS_COMPOSITION: win32more.Windows.Win32.UI.Input.Ime.IME_HOTKEY_IDENTIFIER = 513
IME_ITHOTKEY_UISTYLE_TOGGLE: win32more.Windows.Win32.UI.Input.Ime.IME_HOTKEY_IDENTIFIER = 514
IME_ITHOTKEY_RECONVERTSTRING: win32more.Windows.Win32.UI.Input.Ime.IME_HOTKEY_IDENTIFIER = 515
IME_PAD_REQUEST_FLAGS = UInt32
IMEPADREQ_INSERTSTRING: win32more.Windows.Win32.UI.Input.Ime.IME_PAD_REQUEST_FLAGS = 4097
IMEPADREQ_SENDCONTROL: win32more.Windows.Win32.UI.Input.Ime.IME_PAD_REQUEST_FLAGS = 4100
IMEPADREQ_SETAPPLETSIZE: win32more.Windows.Win32.UI.Input.Ime.IME_PAD_REQUEST_FLAGS = 4104
IMEPADREQ_GETCOMPOSITIONSTRING: win32more.Windows.Win32.UI.Input.Ime.IME_PAD_REQUEST_FLAGS = 4102
IMEPADREQ_GETCOMPOSITIONSTRINGINFO: win32more.Windows.Win32.UI.Input.Ime.IME_PAD_REQUEST_FLAGS = 4108
IMEPADREQ_DELETESTRING: win32more.Windows.Win32.UI.Input.Ime.IME_PAD_REQUEST_FLAGS = 4112
IMEPADREQ_CHANGESTRING: win32more.Windows.Win32.UI.Input.Ime.IME_PAD_REQUEST_FLAGS = 4113
IMEPADREQ_GETAPPLHWND: win32more.Windows.Win32.UI.Input.Ime.IME_PAD_REQUEST_FLAGS = 4116
IMEPADREQ_FORCEIMEPADWINDOWSHOW: win32more.Windows.Win32.UI.Input.Ime.IME_PAD_REQUEST_FLAGS = 4117
IMEPADREQ_POSTMODALNOTIFY: win32more.Windows.Win32.UI.Input.Ime.IME_PAD_REQUEST_FLAGS = 4118
IMEPADREQ_GETDEFAULTUILANGID: win32more.Windows.Win32.UI.Input.Ime.IME_PAD_REQUEST_FLAGS = 4119
IMEPADREQ_GETAPPLETUISTYLE: win32more.Windows.Win32.UI.Input.Ime.IME_PAD_REQUEST_FLAGS = 4121
IMEPADREQ_SETAPPLETUISTYLE: win32more.Windows.Win32.UI.Input.Ime.IME_PAD_REQUEST_FLAGS = 4122
IMEPADREQ_ISAPPLETACTIVE: win32more.Windows.Win32.UI.Input.Ime.IME_PAD_REQUEST_FLAGS = 4123
IMEPADREQ_ISIMEPADWINDOWVISIBLE: win32more.Windows.Win32.UI.Input.Ime.IME_PAD_REQUEST_FLAGS = 4124
IMEPADREQ_SETAPPLETMINMAXSIZE: win32more.Windows.Win32.UI.Input.Ime.IME_PAD_REQUEST_FLAGS = 4125
IMEPADREQ_GETCONVERSIONSTATUS: win32more.Windows.Win32.UI.Input.Ime.IME_PAD_REQUEST_FLAGS = 4126
IMEPADREQ_GETVERSION: win32more.Windows.Win32.UI.Input.Ime.IME_PAD_REQUEST_FLAGS = 4127
IMEPADREQ_GETCURRENTIMEINFO: win32more.Windows.Win32.UI.Input.Ime.IME_PAD_REQUEST_FLAGS = 4128
IME_SENTENCE_MODE = UInt32
IME_SMODE_NONE: win32more.Windows.Win32.UI.Input.Ime.IME_SENTENCE_MODE = 0
IME_SMODE_PLAURALCLAUSE: win32more.Windows.Win32.UI.Input.Ime.IME_SENTENCE_MODE = 1
IME_SMODE_SINGLECONVERT: win32more.Windows.Win32.UI.Input.Ime.IME_SENTENCE_MODE = 2
IME_SMODE_AUTOMATIC: win32more.Windows.Win32.UI.Input.Ime.IME_SENTENCE_MODE = 4
IME_SMODE_PHRASEPREDICT: win32more.Windows.Win32.UI.Input.Ime.IME_SENTENCE_MODE = 8
IME_SMODE_CONVERSATION: win32more.Windows.Win32.UI.Input.Ime.IME_SENTENCE_MODE = 16
IME_SMODE_RESERVED: win32more.Windows.Win32.UI.Input.Ime.IME_SENTENCE_MODE = 61440
class INPUTCONTEXT(Structure):
    hWnd: win32more.Windows.Win32.Foundation.HWND
    fOpen: win32more.Windows.Win32.Foundation.BOOL
    ptStatusWndPos: win32more.Windows.Win32.Foundation.POINT
    ptSoftKbdPos: win32more.Windows.Win32.Foundation.POINT
    fdwConversion: UInt32
    fdwSentence: UInt32
    lfFont: _lfFont_e__Union
    cfCompForm: win32more.Windows.Win32.UI.Input.Ime.COMPOSITIONFORM
    cfCandForm: win32more.Windows.Win32.UI.Input.Ime.CANDIDATEFORM * 4
    hCompStr: win32more.Windows.Win32.UI.Input.Ime.HIMCC
    hCandInfo: win32more.Windows.Win32.UI.Input.Ime.HIMCC
    hGuideLine: win32more.Windows.Win32.UI.Input.Ime.HIMCC
    hPrivate: win32more.Windows.Win32.UI.Input.Ime.HIMCC
    dwNumMsgBuf: UInt32
    hMsgBuf: win32more.Windows.Win32.UI.Input.Ime.HIMCC
    fdwInit: UInt32
    dwReserve: UInt32 * 3
    class _lfFont_e__Union(Union):
        A: win32more.Windows.Win32.Graphics.Gdi.LOGFONTA
        W: win32more.Windows.Win32.Graphics.Gdi.LOGFONTW
class MORRSLT(Structure):
    dwSize: UInt32
    pwchOutput: win32more.Windows.Win32.Foundation.PWSTR
    cchOutput: UInt16
    Anonymous1: _Anonymous1_e__Union
    Anonymous2: _Anonymous2_e__Union
    pchInputPos: POINTER(UInt16)
    pchOutputIdxWDD: POINTER(UInt16)
    Anonymous3: _Anonymous3_e__Union
    paMonoRubyPos: POINTER(UInt16)
    pWDD: POINTER(win32more.Windows.Win32.UI.Input.Ime.WDD)
    cWDD: Int32
    pPrivate: VoidPtr
    BLKBuff: Char * 1
    _pack_ = 1
    class _Anonymous1_e__Union(Union):
        pwchRead: win32more.Windows.Win32.Foundation.PWSTR
        pwchComp: win32more.Windows.Win32.Foundation.PWSTR
        _pack_ = 1
    class _Anonymous2_e__Union(Union):
        cchRead: UInt16
        cchComp: UInt16
        _pack_ = 1
    class _Anonymous3_e__Union(Union):
        pchReadIdxWDD: POINTER(UInt16)
        pchCompIdxWDD: POINTER(UInt16)
        _pack_ = 1
NOTIFY_IME_ACTION = UInt32
NI_CHANGECANDIDATELIST: win32more.Windows.Win32.UI.Input.Ime.NOTIFY_IME_ACTION = 19
NI_CLOSECANDIDATE: win32more.Windows.Win32.UI.Input.Ime.NOTIFY_IME_ACTION = 17
NI_COMPOSITIONSTR: win32more.Windows.Win32.UI.Input.Ime.NOTIFY_IME_ACTION = 21
NI_IMEMENUSELECTED: win32more.Windows.Win32.UI.Input.Ime.NOTIFY_IME_ACTION = 24
NI_OPENCANDIDATE: win32more.Windows.Win32.UI.Input.Ime.NOTIFY_IME_ACTION = 16
NI_SELECTCANDIDATESTR: win32more.Windows.Win32.UI.Input.Ime.NOTIFY_IME_ACTION = 18
NI_SETCANDIDATE_PAGESIZE: win32more.Windows.Win32.UI.Input.Ime.NOTIFY_IME_ACTION = 23
NI_SETCANDIDATE_PAGESTART: win32more.Windows.Win32.UI.Input.Ime.NOTIFY_IME_ACTION = 22
NOTIFY_IME_INDEX = UInt32
CPS_CANCEL: win32more.Windows.Win32.UI.Input.Ime.NOTIFY_IME_INDEX = 4
CPS_COMPLETE: win32more.Windows.Win32.UI.Input.Ime.NOTIFY_IME_INDEX = 1
CPS_CONVERT: win32more.Windows.Win32.UI.Input.Ime.NOTIFY_IME_INDEX = 2
CPS_REVERT: win32more.Windows.Win32.UI.Input.Ime.NOTIFY_IME_INDEX = 3
@winfunctype_pointer
def PFNLOG(param0: POINTER(win32more.Windows.Win32.UI.Input.Ime.IMEDP), param1: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.BOOL: ...
class POSTBL(Structure):
    nPos: UInt16
    szName: POINTER(Byte)
    _pack_ = 1
class RECONVERTSTRING(Structure):
    dwSize: UInt32
    dwVersion: UInt32
    dwStrLen: UInt32
    dwStrOffset: UInt32
    dwCompStrLen: UInt32
    dwCompStrOffset: UInt32
    dwTargetStrLen: UInt32
    dwTargetStrOffset: UInt32
class REGISTERWORDA(Structure):
    lpReading: win32more.Windows.Win32.Foundation.PSTR
    lpWord: win32more.Windows.Win32.Foundation.PSTR
@winfunctype_pointer
def REGISTERWORDENUMPROCA(lpszReading: win32more.Windows.Win32.Foundation.PSTR, param1: UInt32, lpszString: win32more.Windows.Win32.Foundation.PSTR, param3: VoidPtr) -> Int32: ...
@winfunctype_pointer
def REGISTERWORDENUMPROCW(lpszReading: win32more.Windows.Win32.Foundation.PWSTR, param1: UInt32, lpszString: win32more.Windows.Win32.Foundation.PWSTR, param3: VoidPtr) -> Int32: ...
REGISTERWORDENUMPROC = UnicodeAlias('REGISTERWORDENUMPROCW')
class REGISTERWORDW(Structure):
    lpReading: win32more.Windows.Win32.Foundation.PWSTR
    lpWord: win32more.Windows.Win32.Foundation.PWSTR
REGISTERWORD = UnicodeAlias('REGISTERWORDW')
SET_COMPOSITION_STRING_TYPE = UInt32
SCS_SETSTR: win32more.Windows.Win32.UI.Input.Ime.SET_COMPOSITION_STRING_TYPE = 9
SCS_CHANGEATTR: win32more.Windows.Win32.UI.Input.Ime.SET_COMPOSITION_STRING_TYPE = 18
SCS_CHANGECLAUSE: win32more.Windows.Win32.UI.Input.Ime.SET_COMPOSITION_STRING_TYPE = 36
SCS_SETRECONVERTSTRING: win32more.Windows.Win32.UI.Input.Ime.SET_COMPOSITION_STRING_TYPE = 65536
SCS_QUERYRECONVERTSTRING: win32more.Windows.Win32.UI.Input.Ime.SET_COMPOSITION_STRING_TYPE = 131072
class SOFTKBDDATA(Structure):
    uCount: UInt32
    wCode: UInt16 * 256
class STYLEBUFA(Structure):
    dwStyle: UInt32
    szDescription: win32more.Windows.Win32.Foundation.CHAR * 32
class STYLEBUFW(Structure):
    dwStyle: UInt32
    szDescription: Char * 32
STYLEBUF = UnicodeAlias('STYLEBUFW')
class TRANSMSG(Structure):
    message: UInt32
    wParam: win32more.Windows.Win32.Foundation.WPARAM
    lParam: win32more.Windows.Win32.Foundation.LPARAM
class TRANSMSGLIST(Structure):
    uMsgCount: UInt32
    TransMsg: win32more.Windows.Win32.UI.Input.Ime.TRANSMSG * 1
class WDD(Structure):
    wDispPos: UInt16
    Anonymous1: _Anonymous1_e__Union
    cchDisp: UInt16
    Anonymous2: _Anonymous2_e__Union
    WDD_nReserve1: UInt32
    nPos: UInt16
    fPhrase: Annotated[UInt16, 1]
    fAutoCorrect: Annotated[UInt16, 1]
    fNumericPrefix: Annotated[UInt16, 1]
    fUserRegistered: Annotated[UInt16, 1]
    fUnknown: Annotated[UInt16, 1]
    fRecentUsed: Annotated[UInt16, 1]
    Anonymous3: Annotated[UInt16, 10]
    pReserved: VoidPtr
    _pack_ = 1
    class _Anonymous1_e__Union(Union):
        wReadPos: UInt16
        wCompPos: UInt16
        _pack_ = 1
    class _Anonymous2_e__Union(Union):
        cchRead: UInt16
        cchComp: UInt16
        _pack_ = 1
@winfunctype_pointer
def fpCreateIFECommonInstanceType(ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def fpCreateIFEDictionaryInstanceType(ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def fpCreateIFELanguageInstanceType(clsid: POINTER(Guid), ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...


make_ready(__name__)
