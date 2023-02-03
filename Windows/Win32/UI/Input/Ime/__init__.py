from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Globalization
import Windows.Win32.Graphics.Gdi
import Windows.Win32.System.Com
import Windows.Win32.UI.Input.Ime
import Windows.Win32.UI.TextServices
import Windows.Win32.UI.WindowsAndMessaging
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
class APPLETIDLIST(Structure):
    count: Int32
    pIIDList: POINTER(Guid)
class APPLYCANDEXPARAM(Structure):
    dwSize: UInt32
    lpwstrDisplay: Windows.Win32.Foundation.PWSTR
    lpwstrReading: Windows.Win32.Foundation.PWSTR
    dwReserved: UInt32
CATID_MSIME_IImePadApplet_VER7: Guid = Guid('4a0f8e31-c3ee-11d1-af-ef-00-80-5f-0c-8b-6d')
CATID_MSIME_IImePadApplet_VER80: Guid = Guid('56f7a792-fef1-11d3-84-63-00-c0-4f-7a-06-e5')
CATID_MSIME_IImePadApplet_VER81: Guid = Guid('656520b0-bb88-11d4-84-c0-00-c0-4f-7a-06-e5')
CATID_MSIME_IImePadApplet900: Guid = Guid('faae51bf-5e5b-4a1d-8d-e1-17-c1-d9-e1-72-8d')
CATID_MSIME_IImePadApplet1000: Guid = Guid('e081e1d6-2389-43cb-b6-6f-60-9f-82-3d-9f-9c')
CATID_MSIME_IImePadApplet1200: Guid = Guid('a47fb5fc-7d15-4223-a7-89-b7-81-bf-9a-e6-67')
CATID_MSIME_IImePadApplet: Guid = Guid('7566cad1-4ec9-4478-9f-e9-8e-d7-66-61-9e-df')
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
IME_SYSINFO_WOW16: UInt32 = 2
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
CLSID_VERSION_DEPENDENT_MSIME_JAPANESE: Guid = Guid('6a91029e-aa49-471b-ae-e7-7d-33-27-85-66-0d')
IFEC_S_ALREADY_DEFAULT: Windows.Win32.Foundation.HRESULT = 291840
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
IFED_S_MORE_ENTRIES: Windows.Win32.Foundation.HRESULT = 291328
IFED_S_EMPTY_DICTIONARY: Windows.Win32.Foundation.HRESULT = 291329
IFED_S_WORD_EXISTS: Windows.Win32.Foundation.HRESULT = 291330
IFED_S_COMMENT_CHANGED: Windows.Win32.Foundation.HRESULT = 291331
IFED_E_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -2147192064
IFED_E_INVALID_FORMAT: Windows.Win32.Foundation.HRESULT = -2147192063
IFED_E_OPEN_FAILED: Windows.Win32.Foundation.HRESULT = -2147192062
IFED_E_WRITE_FAILED: Windows.Win32.Foundation.HRESULT = -2147192061
IFED_E_NO_ENTRY: Windows.Win32.Foundation.HRESULT = -2147192060
IFED_E_REGISTER_FAILED: Windows.Win32.Foundation.HRESULT = -2147192059
IFED_E_NOT_USER_DIC: Windows.Win32.Foundation.HRESULT = -2147192058
IFED_E_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -2147192057
IFED_E_USER_COMMENT: Windows.Win32.Foundation.HRESULT = -2147192056
IFED_E_REGISTER_ILLEGAL_POS: Windows.Win32.Foundation.HRESULT = -2147192055
IFED_E_REGISTER_IMPROPER_WORD: Windows.Win32.Foundation.HRESULT = -2147192054
IFED_E_REGISTER_DISCONNECTED: Windows.Win32.Foundation.HRESULT = -2147192053
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
CLSID_ImePlugInDictDictionaryList_CHS: Guid = Guid('7bf0129b-5bef-4de4-9b-0b-5e-db-66-ac-2f-a6')
CLSID_ImePlugInDictDictionaryList_JPN: Guid = Guid('4fe2776b-b0f9-4396-b5-fc-e9-d4-cf-1e-c1-95')
@winfunctype('IMM32.dll')
def ImmInstallIMEA(lpszIMEFileName: Windows.Win32.Foundation.PSTR, lpszLayoutText: Windows.Win32.Foundation.PSTR) -> Windows.Win32.UI.TextServices.HKL: ...
@winfunctype('IMM32.dll')
def ImmInstallIMEW(lpszIMEFileName: Windows.Win32.Foundation.PWSTR, lpszLayoutText: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.UI.TextServices.HKL: ...
@winfunctype('IMM32.dll')
def ImmGetDefaultIMEWnd(param0: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HWND: ...
@winfunctype('IMM32.dll')
def ImmGetDescriptionA(param0: Windows.Win32.UI.TextServices.HKL, lpszDescription: Windows.Win32.Foundation.PSTR, uBufLen: UInt32) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmGetDescriptionW(param0: Windows.Win32.UI.TextServices.HKL, lpszDescription: Windows.Win32.Foundation.PWSTR, uBufLen: UInt32) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmGetIMEFileNameA(param0: Windows.Win32.UI.TextServices.HKL, lpszFileName: Windows.Win32.Foundation.PSTR, uBufLen: UInt32) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmGetIMEFileNameW(param0: Windows.Win32.UI.TextServices.HKL, lpszFileName: Windows.Win32.Foundation.PWSTR, uBufLen: UInt32) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmGetProperty(param0: Windows.Win32.UI.TextServices.HKL, param1: UInt32) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmIsIME(param0: Windows.Win32.UI.TextServices.HKL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmSimulateHotKey(param0: Windows.Win32.Foundation.HWND, param1: Windows.Win32.UI.Input.Ime.IME_HOTKEY_IDENTIFIER) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmCreateContext() -> Windows.Win32.Globalization.HIMC: ...
@winfunctype('IMM32.dll')
def ImmDestroyContext(param0: Windows.Win32.Globalization.HIMC) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmGetContext(param0: Windows.Win32.Foundation.HWND) -> Windows.Win32.Globalization.HIMC: ...
@winfunctype('IMM32.dll')
def ImmReleaseContext(param0: Windows.Win32.Foundation.HWND, param1: Windows.Win32.Globalization.HIMC) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmAssociateContext(param0: Windows.Win32.Foundation.HWND, param1: Windows.Win32.Globalization.HIMC) -> Windows.Win32.Globalization.HIMC: ...
@winfunctype('IMM32.dll')
def ImmAssociateContextEx(param0: Windows.Win32.Foundation.HWND, param1: Windows.Win32.Globalization.HIMC, param2: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmGetCompositionStringA(param0: Windows.Win32.Globalization.HIMC, param1: Windows.Win32.UI.Input.Ime.IME_COMPOSITION_STRING, lpBuf: c_void_p, dwBufLen: UInt32) -> Int32: ...
@winfunctype('IMM32.dll')
def ImmGetCompositionStringW(param0: Windows.Win32.Globalization.HIMC, param1: Windows.Win32.UI.Input.Ime.IME_COMPOSITION_STRING, lpBuf: c_void_p, dwBufLen: UInt32) -> Int32: ...
@winfunctype('IMM32.dll')
def ImmSetCompositionStringA(param0: Windows.Win32.Globalization.HIMC, dwIndex: Windows.Win32.UI.Input.Ime.SET_COMPOSITION_STRING_TYPE, lpComp: c_void_p, dwCompLen: UInt32, lpRead: c_void_p, dwReadLen: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmSetCompositionStringW(param0: Windows.Win32.Globalization.HIMC, dwIndex: Windows.Win32.UI.Input.Ime.SET_COMPOSITION_STRING_TYPE, lpComp: c_void_p, dwCompLen: UInt32, lpRead: c_void_p, dwReadLen: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmGetCandidateListCountA(param0: Windows.Win32.Globalization.HIMC, lpdwListCount: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmGetCandidateListCountW(param0: Windows.Win32.Globalization.HIMC, lpdwListCount: POINTER(UInt32)) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmGetCandidateListA(param0: Windows.Win32.Globalization.HIMC, deIndex: UInt32, lpCandList: POINTER(Windows.Win32.UI.Input.Ime.CANDIDATELIST_head), dwBufLen: UInt32) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmGetCandidateListW(param0: Windows.Win32.Globalization.HIMC, deIndex: UInt32, lpCandList: POINTER(Windows.Win32.UI.Input.Ime.CANDIDATELIST_head), dwBufLen: UInt32) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmGetGuideLineA(param0: Windows.Win32.Globalization.HIMC, dwIndex: Windows.Win32.UI.Input.Ime.GET_GUIDE_LINE_TYPE, lpBuf: Windows.Win32.Foundation.PSTR, dwBufLen: UInt32) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmGetGuideLineW(param0: Windows.Win32.Globalization.HIMC, dwIndex: Windows.Win32.UI.Input.Ime.GET_GUIDE_LINE_TYPE, lpBuf: Windows.Win32.Foundation.PWSTR, dwBufLen: UInt32) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmGetConversionStatus(param0: Windows.Win32.Globalization.HIMC, lpfdwConversion: POINTER(Windows.Win32.UI.Input.Ime.IME_CONVERSION_MODE), lpfdwSentence: POINTER(Windows.Win32.UI.Input.Ime.IME_SENTENCE_MODE)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmSetConversionStatus(param0: Windows.Win32.Globalization.HIMC, param1: Windows.Win32.UI.Input.Ime.IME_CONVERSION_MODE, param2: Windows.Win32.UI.Input.Ime.IME_SENTENCE_MODE) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmGetOpenStatus(param0: Windows.Win32.Globalization.HIMC) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmSetOpenStatus(param0: Windows.Win32.Globalization.HIMC, param1: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmGetCompositionFontA(param0: Windows.Win32.Globalization.HIMC, lplf: POINTER(Windows.Win32.Graphics.Gdi.LOGFONTA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmGetCompositionFontW(param0: Windows.Win32.Globalization.HIMC, lplf: POINTER(Windows.Win32.Graphics.Gdi.LOGFONTW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmSetCompositionFontA(param0: Windows.Win32.Globalization.HIMC, lplf: POINTER(Windows.Win32.Graphics.Gdi.LOGFONTA_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmSetCompositionFontW(param0: Windows.Win32.Globalization.HIMC, lplf: POINTER(Windows.Win32.Graphics.Gdi.LOGFONTW_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmConfigureIMEA(param0: Windows.Win32.UI.TextServices.HKL, param1: Windows.Win32.Foundation.HWND, param2: UInt32, param3: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmConfigureIMEW(param0: Windows.Win32.UI.TextServices.HKL, param1: Windows.Win32.Foundation.HWND, param2: UInt32, param3: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmEscapeA(param0: Windows.Win32.UI.TextServices.HKL, param1: Windows.Win32.Globalization.HIMC, param2: Windows.Win32.UI.Input.Ime.IME_ESCAPE, param3: c_void_p) -> Windows.Win32.Foundation.LRESULT: ...
@winfunctype('IMM32.dll')
def ImmEscapeW(param0: Windows.Win32.UI.TextServices.HKL, param1: Windows.Win32.Globalization.HIMC, param2: Windows.Win32.UI.Input.Ime.IME_ESCAPE, param3: c_void_p) -> Windows.Win32.Foundation.LRESULT: ...
@winfunctype('IMM32.dll')
def ImmGetConversionListA(param0: Windows.Win32.UI.TextServices.HKL, param1: Windows.Win32.Globalization.HIMC, lpSrc: Windows.Win32.Foundation.PSTR, lpDst: POINTER(Windows.Win32.UI.Input.Ime.CANDIDATELIST_head), dwBufLen: UInt32, uFlag: Windows.Win32.UI.Input.Ime.GET_CONVERSION_LIST_FLAG) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmGetConversionListW(param0: Windows.Win32.UI.TextServices.HKL, param1: Windows.Win32.Globalization.HIMC, lpSrc: Windows.Win32.Foundation.PWSTR, lpDst: POINTER(Windows.Win32.UI.Input.Ime.CANDIDATELIST_head), dwBufLen: UInt32, uFlag: Windows.Win32.UI.Input.Ime.GET_CONVERSION_LIST_FLAG) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmNotifyIME(param0: Windows.Win32.Globalization.HIMC, dwAction: Windows.Win32.UI.Input.Ime.NOTIFY_IME_ACTION, dwIndex: Windows.Win32.UI.Input.Ime.NOTIFY_IME_INDEX, dwValue: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmGetStatusWindowPos(param0: Windows.Win32.Globalization.HIMC, lpptPos: POINTER(Windows.Win32.Foundation.POINT_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmSetStatusWindowPos(param0: Windows.Win32.Globalization.HIMC, lpptPos: POINTER(Windows.Win32.Foundation.POINT_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmGetCompositionWindow(param0: Windows.Win32.Globalization.HIMC, lpCompForm: POINTER(Windows.Win32.UI.Input.Ime.COMPOSITIONFORM_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmSetCompositionWindow(param0: Windows.Win32.Globalization.HIMC, lpCompForm: POINTER(Windows.Win32.UI.Input.Ime.COMPOSITIONFORM_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmGetCandidateWindow(param0: Windows.Win32.Globalization.HIMC, param1: UInt32, lpCandidate: POINTER(Windows.Win32.UI.Input.Ime.CANDIDATEFORM_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmSetCandidateWindow(param0: Windows.Win32.Globalization.HIMC, lpCandidate: POINTER(Windows.Win32.UI.Input.Ime.CANDIDATEFORM_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmIsUIMessageA(param0: Windows.Win32.Foundation.HWND, param1: UInt32, param2: Windows.Win32.Foundation.WPARAM, param3: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmIsUIMessageW(param0: Windows.Win32.Foundation.HWND, param1: UInt32, param2: Windows.Win32.Foundation.WPARAM, param3: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmGetVirtualKey(param0: Windows.Win32.Foundation.HWND) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmRegisterWordA(param0: Windows.Win32.UI.TextServices.HKL, lpszReading: Windows.Win32.Foundation.PSTR, param2: UInt32, lpszRegister: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmRegisterWordW(param0: Windows.Win32.UI.TextServices.HKL, lpszReading: Windows.Win32.Foundation.PWSTR, param2: UInt32, lpszRegister: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmUnregisterWordA(param0: Windows.Win32.UI.TextServices.HKL, lpszReading: Windows.Win32.Foundation.PSTR, param2: UInt32, lpszUnregister: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmUnregisterWordW(param0: Windows.Win32.UI.TextServices.HKL, lpszReading: Windows.Win32.Foundation.PWSTR, param2: UInt32, lpszUnregister: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmGetRegisterWordStyleA(param0: Windows.Win32.UI.TextServices.HKL, nItem: UInt32, lpStyleBuf: POINTER(Windows.Win32.UI.Input.Ime.STYLEBUFA_head)) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmGetRegisterWordStyleW(param0: Windows.Win32.UI.TextServices.HKL, nItem: UInt32, lpStyleBuf: POINTER(Windows.Win32.UI.Input.Ime.STYLEBUFW_head)) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmEnumRegisterWordA(param0: Windows.Win32.UI.TextServices.HKL, param1: Windows.Win32.UI.Input.Ime.REGISTERWORDENUMPROCA, lpszReading: Windows.Win32.Foundation.PSTR, param3: UInt32, lpszRegister: Windows.Win32.Foundation.PSTR, param5: c_void_p) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmEnumRegisterWordW(param0: Windows.Win32.UI.TextServices.HKL, param1: Windows.Win32.UI.Input.Ime.REGISTERWORDENUMPROCW, lpszReading: Windows.Win32.Foundation.PWSTR, param3: UInt32, lpszRegister: Windows.Win32.Foundation.PWSTR, param5: c_void_p) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmDisableIME(param0: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmEnumInputContext(idThread: UInt32, lpfn: Windows.Win32.UI.Input.Ime.IMCENUMPROC, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmGetImeMenuItemsA(param0: Windows.Win32.Globalization.HIMC, param1: UInt32, param2: UInt32, lpImeParentMenu: POINTER(Windows.Win32.UI.Input.Ime.IMEMENUITEMINFOA_head), lpImeMenu: POINTER(Windows.Win32.UI.Input.Ime.IMEMENUITEMINFOA_head), dwSize: UInt32) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmGetImeMenuItemsW(param0: Windows.Win32.Globalization.HIMC, param1: UInt32, param2: UInt32, lpImeParentMenu: POINTER(Windows.Win32.UI.Input.Ime.IMEMENUITEMINFOW_head), lpImeMenu: POINTER(Windows.Win32.UI.Input.Ime.IMEMENUITEMINFOW_head), dwSize: UInt32) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmDisableTextFrameService(idThread: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmDisableLegacyIME() -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmGetHotKey(param0: UInt32, lpuModifiers: POINTER(UInt32), lpuVKey: POINTER(UInt32), phKL: POINTER(IntPtr)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmSetHotKey(param0: UInt32, param1: UInt32, param2: UInt32, param3: Windows.Win32.UI.TextServices.HKL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmGenerateMessage(param0: Windows.Win32.Globalization.HIMC) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmRequestMessageA(param0: Windows.Win32.Globalization.HIMC, param1: Windows.Win32.Foundation.WPARAM, param2: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.LRESULT: ...
@winfunctype('IMM32.dll')
def ImmRequestMessageW(param0: Windows.Win32.Globalization.HIMC, param1: Windows.Win32.Foundation.WPARAM, param2: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.LRESULT: ...
@winfunctype('IMM32.dll')
def ImmCreateSoftKeyboard(param0: UInt32, param1: Windows.Win32.Foundation.HWND, param2: Int32, param3: Int32) -> Windows.Win32.Foundation.HWND: ...
@winfunctype('IMM32.dll')
def ImmDestroySoftKeyboard(param0: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmShowSoftKeyboard(param0: Windows.Win32.Foundation.HWND, param1: Int32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmLockIMC(param0: Windows.Win32.Globalization.HIMC) -> POINTER(Windows.Win32.UI.Input.Ime.INPUTCONTEXT_head): ...
@winfunctype('IMM32.dll')
def ImmUnlockIMC(param0: Windows.Win32.Globalization.HIMC) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmGetIMCLockCount(param0: Windows.Win32.Globalization.HIMC) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmCreateIMCC(param0: UInt32) -> Windows.Win32.Globalization.HIMCC: ...
@winfunctype('IMM32.dll')
def ImmDestroyIMCC(param0: Windows.Win32.Globalization.HIMCC) -> Windows.Win32.Globalization.HIMCC: ...
@winfunctype('IMM32.dll')
def ImmLockIMCC(param0: Windows.Win32.Globalization.HIMCC) -> c_void_p: ...
@winfunctype('IMM32.dll')
def ImmUnlockIMCC(param0: Windows.Win32.Globalization.HIMCC) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('IMM32.dll')
def ImmGetIMCCLockCount(param0: Windows.Win32.Globalization.HIMCC) -> UInt32: ...
@winfunctype('IMM32.dll')
def ImmReSizeIMCC(param0: Windows.Win32.Globalization.HIMCC, param1: UInt32) -> Windows.Win32.Globalization.HIMCC: ...
@winfunctype('IMM32.dll')
def ImmGetIMCCSize(param0: Windows.Win32.Globalization.HIMCC) -> UInt32: ...
class CANDIDATEFORM(Structure):
    dwIndex: UInt32
    dwStyle: UInt32
    ptCurrentPos: Windows.Win32.Foundation.POINT
    rcArea: Windows.Win32.Foundation.RECT
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
CActiveIMM = Guid('4955dd33-b159-11d0-8f-cf-00-aa-00-6b-cc-59')
class COMPOSITIONFORM(Structure):
    dwStyle: UInt32
    ptCurrentPos: Windows.Win32.Foundation.POINT
    rcArea: Windows.Win32.Foundation.RECT
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
GCL_CONVERSION: GET_CONVERSION_LIST_FLAG = 1
GCL_REVERSECONVERSION: GET_CONVERSION_LIST_FLAG = 2
GCL_REVERSE_LENGTH: GET_CONVERSION_LIST_FLAG = 3
GET_GUIDE_LINE_TYPE = UInt32
GGL_LEVEL: GET_GUIDE_LINE_TYPE = 1
GGL_INDEX: GET_GUIDE_LINE_TYPE = 2
GGL_STRING: GET_GUIDE_LINE_TYPE = 3
GGL_PRIVATE: GET_GUIDE_LINE_TYPE = 4
class GUIDELINE(Structure):
    dwSize: UInt32
    dwLevel: UInt32
    dwIndex: UInt32
    dwStrLen: UInt32
    dwStrOffset: UInt32
    dwPrivateSize: UInt32
    dwPrivateOffset: UInt32
class IActiveIME(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6fe20962-d077-11d0-8f-e7-00-aa-00-6b-cc-59')
    @commethod(3)
    def Inquire(dwSystemInfoFlags: UInt32, pIMEInfo: POINTER(Windows.Win32.UI.Input.Ime.IMEINFO_head), szWndClass: Windows.Win32.Foundation.PWSTR, pdwPrivate: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ConversionList(hIMC: Windows.Win32.Globalization.HIMC, szSource: Windows.Win32.Foundation.PWSTR, uFlag: UInt32, uBufLen: UInt32, pDest: POINTER(Windows.Win32.UI.Input.Ime.CANDIDATELIST_head), puCopied: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Configure(hKL: Windows.Win32.UI.TextServices.HKL, hWnd: Windows.Win32.Foundation.HWND, dwMode: UInt32, pRegisterWord: POINTER(Windows.Win32.UI.Input.Ime.REGISTERWORDW_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Destroy(uReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Escape(hIMC: Windows.Win32.Globalization.HIMC, uEscape: UInt32, pData: c_void_p, plResult: POINTER(Windows.Win32.Foundation.LRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetActiveContext(hIMC: Windows.Win32.Globalization.HIMC, fFlag: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ProcessKey(hIMC: Windows.Win32.Globalization.HIMC, uVirKey: UInt32, lParam: UInt32, pbKeyState: c_char_p_no) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Notify(hIMC: Windows.Win32.Globalization.HIMC, dwAction: UInt32, dwIndex: UInt32, dwValue: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Select(hIMC: Windows.Win32.Globalization.HIMC, fSelect: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetCompositionString(hIMC: Windows.Win32.Globalization.HIMC, dwIndex: UInt32, pComp: c_void_p, dwCompLen: UInt32, pRead: c_void_p, dwReadLen: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def ToAsciiEx(uVirKey: UInt32, uScanCode: UInt32, pbKeyState: c_char_p_no, fuState: UInt32, hIMC: Windows.Win32.Globalization.HIMC, pdwTransBuf: POINTER(UInt32), puSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def RegisterWord(szReading: Windows.Win32.Foundation.PWSTR, dwStyle: UInt32, szString: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def UnregisterWord(szReading: Windows.Win32.Foundation.PWSTR, dwStyle: UInt32, szString: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetRegisterWordStyle(nItem: UInt32, pStyleBuf: POINTER(Windows.Win32.UI.Input.Ime.STYLEBUFW_head), puBufSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def EnumRegisterWord(szReading: Windows.Win32.Foundation.PWSTR, dwStyle: UInt32, szRegister: Windows.Win32.Foundation.PWSTR, pData: c_void_p, ppEnum: POINTER(Windows.Win32.UI.Input.Ime.IEnumRegisterWordW_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetCodePageA(uCodePage: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetLangId(plid: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
class IActiveIME2(c_void_p):
    extends: Windows.Win32.UI.Input.Ime.IActiveIME
    Guid = Guid('e1c4bf0e-2d53-11d2-93-e1-00-60-b0-67-b8-6e')
    @commethod(20)
    def Sleep() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Unsleep(fDead: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IActiveIMMApp(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('08c0e040-62d1-11d1-93-26-00-60-b0-67-b8-6e')
    @commethod(3)
    def AssociateContext(hWnd: Windows.Win32.Foundation.HWND, hIME: Windows.Win32.Globalization.HIMC, phPrev: POINTER(Windows.Win32.Globalization.HIMC)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ConfigureIMEA(hKL: Windows.Win32.UI.TextServices.HKL, hWnd: Windows.Win32.Foundation.HWND, dwMode: UInt32, pData: POINTER(Windows.Win32.UI.Input.Ime.REGISTERWORDA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ConfigureIMEW(hKL: Windows.Win32.UI.TextServices.HKL, hWnd: Windows.Win32.Foundation.HWND, dwMode: UInt32, pData: POINTER(Windows.Win32.UI.Input.Ime.REGISTERWORDW_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateContext(phIMC: POINTER(Windows.Win32.Globalization.HIMC)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DestroyContext(hIME: Windows.Win32.Globalization.HIMC) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def EnumRegisterWordA(hKL: Windows.Win32.UI.TextServices.HKL, szReading: Windows.Win32.Foundation.PSTR, dwStyle: UInt32, szRegister: Windows.Win32.Foundation.PSTR, pData: c_void_p, pEnum: POINTER(Windows.Win32.UI.Input.Ime.IEnumRegisterWordA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnumRegisterWordW(hKL: Windows.Win32.UI.TextServices.HKL, szReading: Windows.Win32.Foundation.PWSTR, dwStyle: UInt32, szRegister: Windows.Win32.Foundation.PWSTR, pData: c_void_p, pEnum: POINTER(Windows.Win32.UI.Input.Ime.IEnumRegisterWordW_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EscapeA(hKL: Windows.Win32.UI.TextServices.HKL, hIMC: Windows.Win32.Globalization.HIMC, uEscape: UInt32, pData: c_void_p, plResult: POINTER(Windows.Win32.Foundation.LRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EscapeW(hKL: Windows.Win32.UI.TextServices.HKL, hIMC: Windows.Win32.Globalization.HIMC, uEscape: UInt32, pData: c_void_p, plResult: POINTER(Windows.Win32.Foundation.LRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetCandidateListA(hIMC: Windows.Win32.Globalization.HIMC, dwIndex: UInt32, uBufLen: UInt32, pCandList: POINTER(Windows.Win32.UI.Input.Ime.CANDIDATELIST_head), puCopied: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetCandidateListW(hIMC: Windows.Win32.Globalization.HIMC, dwIndex: UInt32, uBufLen: UInt32, pCandList: POINTER(Windows.Win32.UI.Input.Ime.CANDIDATELIST_head), puCopied: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetCandidateListCountA(hIMC: Windows.Win32.Globalization.HIMC, pdwListSize: POINTER(UInt32), pdwBufLen: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetCandidateListCountW(hIMC: Windows.Win32.Globalization.HIMC, pdwListSize: POINTER(UInt32), pdwBufLen: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetCandidateWindow(hIMC: Windows.Win32.Globalization.HIMC, dwIndex: UInt32, pCandidate: POINTER(Windows.Win32.UI.Input.Ime.CANDIDATEFORM_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetCompositionFontA(hIMC: Windows.Win32.Globalization.HIMC, plf: POINTER(Windows.Win32.Graphics.Gdi.LOGFONTA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetCompositionFontW(hIMC: Windows.Win32.Globalization.HIMC, plf: POINTER(Windows.Win32.Graphics.Gdi.LOGFONTW_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetCompositionStringA(hIMC: Windows.Win32.Globalization.HIMC, dwIndex: UInt32, dwBufLen: UInt32, plCopied: POINTER(Int32), pBuf: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetCompositionStringW(hIMC: Windows.Win32.Globalization.HIMC, dwIndex: UInt32, dwBufLen: UInt32, plCopied: POINTER(Int32), pBuf: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetCompositionWindow(hIMC: Windows.Win32.Globalization.HIMC, pCompForm: POINTER(Windows.Win32.UI.Input.Ime.COMPOSITIONFORM_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetContext(hWnd: Windows.Win32.Foundation.HWND, phIMC: POINTER(Windows.Win32.Globalization.HIMC)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetConversionListA(hKL: Windows.Win32.UI.TextServices.HKL, hIMC: Windows.Win32.Globalization.HIMC, pSrc: Windows.Win32.Foundation.PSTR, uBufLen: UInt32, uFlag: UInt32, pDst: POINTER(Windows.Win32.UI.Input.Ime.CANDIDATELIST_head), puCopied: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetConversionListW(hKL: Windows.Win32.UI.TextServices.HKL, hIMC: Windows.Win32.Globalization.HIMC, pSrc: Windows.Win32.Foundation.PWSTR, uBufLen: UInt32, uFlag: UInt32, pDst: POINTER(Windows.Win32.UI.Input.Ime.CANDIDATELIST_head), puCopied: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetConversionStatus(hIMC: Windows.Win32.Globalization.HIMC, pfdwConversion: POINTER(UInt32), pfdwSentence: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetDefaultIMEWnd(hWnd: Windows.Win32.Foundation.HWND, phDefWnd: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def GetDescriptionA(hKL: Windows.Win32.UI.TextServices.HKL, uBufLen: UInt32, szDescription: Windows.Win32.Foundation.PSTR, puCopied: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetDescriptionW(hKL: Windows.Win32.UI.TextServices.HKL, uBufLen: UInt32, szDescription: Windows.Win32.Foundation.PWSTR, puCopied: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetGuideLineA(hIMC: Windows.Win32.Globalization.HIMC, dwIndex: UInt32, dwBufLen: UInt32, pBuf: Windows.Win32.Foundation.PSTR, pdwResult: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetGuideLineW(hIMC: Windows.Win32.Globalization.HIMC, dwIndex: UInt32, dwBufLen: UInt32, pBuf: Windows.Win32.Foundation.PWSTR, pdwResult: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetIMEFileNameA(hKL: Windows.Win32.UI.TextServices.HKL, uBufLen: UInt32, szFileName: Windows.Win32.Foundation.PSTR, puCopied: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetIMEFileNameW(hKL: Windows.Win32.UI.TextServices.HKL, uBufLen: UInt32, szFileName: Windows.Win32.Foundation.PWSTR, puCopied: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetOpenStatus(hIMC: Windows.Win32.Globalization.HIMC) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetProperty(hKL: Windows.Win32.UI.TextServices.HKL, fdwIndex: UInt32, pdwProperty: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetRegisterWordStyleA(hKL: Windows.Win32.UI.TextServices.HKL, nItem: UInt32, pStyleBuf: POINTER(Windows.Win32.UI.Input.Ime.STYLEBUFA_head), puCopied: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def GetRegisterWordStyleW(hKL: Windows.Win32.UI.TextServices.HKL, nItem: UInt32, pStyleBuf: POINTER(Windows.Win32.UI.Input.Ime.STYLEBUFW_head), puCopied: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def GetStatusWindowPos(hIMC: Windows.Win32.Globalization.HIMC, pptPos: POINTER(Windows.Win32.Foundation.POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def GetVirtualKey(hWnd: Windows.Win32.Foundation.HWND, puVirtualKey: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def InstallIMEA(szIMEFileName: Windows.Win32.Foundation.PSTR, szLayoutText: Windows.Win32.Foundation.PSTR, phKL: POINTER(Windows.Win32.UI.TextServices.HKL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def InstallIMEW(szIMEFileName: Windows.Win32.Foundation.PWSTR, szLayoutText: Windows.Win32.Foundation.PWSTR, phKL: POINTER(Windows.Win32.UI.TextServices.HKL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def IsIME(hKL: Windows.Win32.UI.TextServices.HKL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def IsUIMessageA(hWndIME: Windows.Win32.Foundation.HWND, msg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def IsUIMessageW(hWndIME: Windows.Win32.Foundation.HWND, msg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def NotifyIME(hIMC: Windows.Win32.Globalization.HIMC, dwAction: UInt32, dwIndex: UInt32, dwValue: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def RegisterWordA(hKL: Windows.Win32.UI.TextServices.HKL, szReading: Windows.Win32.Foundation.PSTR, dwStyle: UInt32, szRegister: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def RegisterWordW(hKL: Windows.Win32.UI.TextServices.HKL, szReading: Windows.Win32.Foundation.PWSTR, dwStyle: UInt32, szRegister: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def ReleaseContext(hWnd: Windows.Win32.Foundation.HWND, hIMC: Windows.Win32.Globalization.HIMC) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def SetCandidateWindow(hIMC: Windows.Win32.Globalization.HIMC, pCandidate: POINTER(Windows.Win32.UI.Input.Ime.CANDIDATEFORM_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def SetCompositionFontA(hIMC: Windows.Win32.Globalization.HIMC, plf: POINTER(Windows.Win32.Graphics.Gdi.LOGFONTA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def SetCompositionFontW(hIMC: Windows.Win32.Globalization.HIMC, plf: POINTER(Windows.Win32.Graphics.Gdi.LOGFONTW_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def SetCompositionStringA(hIMC: Windows.Win32.Globalization.HIMC, dwIndex: UInt32, pComp: c_void_p, dwCompLen: UInt32, pRead: c_void_p, dwReadLen: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def SetCompositionStringW(hIMC: Windows.Win32.Globalization.HIMC, dwIndex: UInt32, pComp: c_void_p, dwCompLen: UInt32, pRead: c_void_p, dwReadLen: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def SetCompositionWindow(hIMC: Windows.Win32.Globalization.HIMC, pCompForm: POINTER(Windows.Win32.UI.Input.Ime.COMPOSITIONFORM_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def SetConversionStatus(hIMC: Windows.Win32.Globalization.HIMC, fdwConversion: UInt32, fdwSentence: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def SetOpenStatus(hIMC: Windows.Win32.Globalization.HIMC, fOpen: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def SetStatusWindowPos(hIMC: Windows.Win32.Globalization.HIMC, pptPos: POINTER(Windows.Win32.Foundation.POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def SimulateHotKey(hWnd: Windows.Win32.Foundation.HWND, dwHotKeyID: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def UnregisterWordA(hKL: Windows.Win32.UI.TextServices.HKL, szReading: Windows.Win32.Foundation.PSTR, dwStyle: UInt32, szUnregister: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def UnregisterWordW(hKL: Windows.Win32.UI.TextServices.HKL, szReading: Windows.Win32.Foundation.PWSTR, dwStyle: UInt32, szUnregister: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def Activate(fRestoreLayout: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def Deactivate() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def OnDefWindowProc(hWnd: Windows.Win32.Foundation.HWND, Msg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM, plResult: POINTER(Windows.Win32.Foundation.LRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def FilterClientWindows(aaClassList: POINTER(UInt16), uSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def GetCodePageA(hKL: Windows.Win32.UI.TextServices.HKL, uCodePage: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def GetLangId(hKL: Windows.Win32.UI.TextServices.HKL, plid: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def AssociateContextEx(hWnd: Windows.Win32.Foundation.HWND, hIMC: Windows.Win32.Globalization.HIMC, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(67)
    def DisableIME(idThread: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(68)
    def GetImeMenuItemsA(hIMC: Windows.Win32.Globalization.HIMC, dwFlags: UInt32, dwType: UInt32, pImeParentMenu: POINTER(Windows.Win32.UI.Input.Ime.IMEMENUITEMINFOA_head), pImeMenu: POINTER(Windows.Win32.UI.Input.Ime.IMEMENUITEMINFOA_head), dwSize: UInt32, pdwResult: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def GetImeMenuItemsW(hIMC: Windows.Win32.Globalization.HIMC, dwFlags: UInt32, dwType: UInt32, pImeParentMenu: POINTER(Windows.Win32.UI.Input.Ime.IMEMENUITEMINFOW_head), pImeMenu: POINTER(Windows.Win32.UI.Input.Ime.IMEMENUITEMINFOW_head), dwSize: UInt32, pdwResult: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(70)
    def EnumInputContext(idThread: UInt32, ppEnum: POINTER(Windows.Win32.UI.Input.Ime.IEnumInputContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IActiveIMMIME(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('08c03411-f96b-11d0-a4-75-00-aa-00-6b-cc-59')
    @commethod(3)
    def AssociateContext(hWnd: Windows.Win32.Foundation.HWND, hIME: Windows.Win32.Globalization.HIMC, phPrev: POINTER(Windows.Win32.Globalization.HIMC)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ConfigureIMEA(hKL: Windows.Win32.UI.TextServices.HKL, hWnd: Windows.Win32.Foundation.HWND, dwMode: UInt32, pData: POINTER(Windows.Win32.UI.Input.Ime.REGISTERWORDA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ConfigureIMEW(hKL: Windows.Win32.UI.TextServices.HKL, hWnd: Windows.Win32.Foundation.HWND, dwMode: UInt32, pData: POINTER(Windows.Win32.UI.Input.Ime.REGISTERWORDW_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateContext(phIMC: POINTER(Windows.Win32.Globalization.HIMC)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DestroyContext(hIME: Windows.Win32.Globalization.HIMC) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def EnumRegisterWordA(hKL: Windows.Win32.UI.TextServices.HKL, szReading: Windows.Win32.Foundation.PSTR, dwStyle: UInt32, szRegister: Windows.Win32.Foundation.PSTR, pData: c_void_p, pEnum: POINTER(Windows.Win32.UI.Input.Ime.IEnumRegisterWordA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnumRegisterWordW(hKL: Windows.Win32.UI.TextServices.HKL, szReading: Windows.Win32.Foundation.PWSTR, dwStyle: UInt32, szRegister: Windows.Win32.Foundation.PWSTR, pData: c_void_p, pEnum: POINTER(Windows.Win32.UI.Input.Ime.IEnumRegisterWordW_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EscapeA(hKL: Windows.Win32.UI.TextServices.HKL, hIMC: Windows.Win32.Globalization.HIMC, uEscape: UInt32, pData: c_void_p, plResult: POINTER(Windows.Win32.Foundation.LRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EscapeW(hKL: Windows.Win32.UI.TextServices.HKL, hIMC: Windows.Win32.Globalization.HIMC, uEscape: UInt32, pData: c_void_p, plResult: POINTER(Windows.Win32.Foundation.LRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetCandidateListA(hIMC: Windows.Win32.Globalization.HIMC, dwIndex: UInt32, uBufLen: UInt32, pCandList: POINTER(Windows.Win32.UI.Input.Ime.CANDIDATELIST_head), puCopied: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetCandidateListW(hIMC: Windows.Win32.Globalization.HIMC, dwIndex: UInt32, uBufLen: UInt32, pCandList: POINTER(Windows.Win32.UI.Input.Ime.CANDIDATELIST_head), puCopied: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetCandidateListCountA(hIMC: Windows.Win32.Globalization.HIMC, pdwListSize: POINTER(UInt32), pdwBufLen: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetCandidateListCountW(hIMC: Windows.Win32.Globalization.HIMC, pdwListSize: POINTER(UInt32), pdwBufLen: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetCandidateWindow(hIMC: Windows.Win32.Globalization.HIMC, dwIndex: UInt32, pCandidate: POINTER(Windows.Win32.UI.Input.Ime.CANDIDATEFORM_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetCompositionFontA(hIMC: Windows.Win32.Globalization.HIMC, plf: POINTER(Windows.Win32.Graphics.Gdi.LOGFONTA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetCompositionFontW(hIMC: Windows.Win32.Globalization.HIMC, plf: POINTER(Windows.Win32.Graphics.Gdi.LOGFONTW_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetCompositionStringA(hIMC: Windows.Win32.Globalization.HIMC, dwIndex: UInt32, dwBufLen: UInt32, plCopied: POINTER(Int32), pBuf: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetCompositionStringW(hIMC: Windows.Win32.Globalization.HIMC, dwIndex: UInt32, dwBufLen: UInt32, plCopied: POINTER(Int32), pBuf: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetCompositionWindow(hIMC: Windows.Win32.Globalization.HIMC, pCompForm: POINTER(Windows.Win32.UI.Input.Ime.COMPOSITIONFORM_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetContext(hWnd: Windows.Win32.Foundation.HWND, phIMC: POINTER(Windows.Win32.Globalization.HIMC)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetConversionListA(hKL: Windows.Win32.UI.TextServices.HKL, hIMC: Windows.Win32.Globalization.HIMC, pSrc: Windows.Win32.Foundation.PSTR, uBufLen: UInt32, uFlag: UInt32, pDst: POINTER(Windows.Win32.UI.Input.Ime.CANDIDATELIST_head), puCopied: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetConversionListW(hKL: Windows.Win32.UI.TextServices.HKL, hIMC: Windows.Win32.Globalization.HIMC, pSrc: Windows.Win32.Foundation.PWSTR, uBufLen: UInt32, uFlag: UInt32, pDst: POINTER(Windows.Win32.UI.Input.Ime.CANDIDATELIST_head), puCopied: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetConversionStatus(hIMC: Windows.Win32.Globalization.HIMC, pfdwConversion: POINTER(UInt32), pfdwSentence: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetDefaultIMEWnd(hWnd: Windows.Win32.Foundation.HWND, phDefWnd: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def GetDescriptionA(hKL: Windows.Win32.UI.TextServices.HKL, uBufLen: UInt32, szDescription: Windows.Win32.Foundation.PSTR, puCopied: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetDescriptionW(hKL: Windows.Win32.UI.TextServices.HKL, uBufLen: UInt32, szDescription: Windows.Win32.Foundation.PWSTR, puCopied: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetGuideLineA(hIMC: Windows.Win32.Globalization.HIMC, dwIndex: UInt32, dwBufLen: UInt32, pBuf: Windows.Win32.Foundation.PSTR, pdwResult: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetGuideLineW(hIMC: Windows.Win32.Globalization.HIMC, dwIndex: UInt32, dwBufLen: UInt32, pBuf: Windows.Win32.Foundation.PWSTR, pdwResult: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetIMEFileNameA(hKL: Windows.Win32.UI.TextServices.HKL, uBufLen: UInt32, szFileName: Windows.Win32.Foundation.PSTR, puCopied: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetIMEFileNameW(hKL: Windows.Win32.UI.TextServices.HKL, uBufLen: UInt32, szFileName: Windows.Win32.Foundation.PWSTR, puCopied: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetOpenStatus(hIMC: Windows.Win32.Globalization.HIMC) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetProperty(hKL: Windows.Win32.UI.TextServices.HKL, fdwIndex: UInt32, pdwProperty: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetRegisterWordStyleA(hKL: Windows.Win32.UI.TextServices.HKL, nItem: UInt32, pStyleBuf: POINTER(Windows.Win32.UI.Input.Ime.STYLEBUFA_head), puCopied: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def GetRegisterWordStyleW(hKL: Windows.Win32.UI.TextServices.HKL, nItem: UInt32, pStyleBuf: POINTER(Windows.Win32.UI.Input.Ime.STYLEBUFW_head), puCopied: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def GetStatusWindowPos(hIMC: Windows.Win32.Globalization.HIMC, pptPos: POINTER(Windows.Win32.Foundation.POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def GetVirtualKey(hWnd: Windows.Win32.Foundation.HWND, puVirtualKey: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def InstallIMEA(szIMEFileName: Windows.Win32.Foundation.PSTR, szLayoutText: Windows.Win32.Foundation.PSTR, phKL: POINTER(Windows.Win32.UI.TextServices.HKL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def InstallIMEW(szIMEFileName: Windows.Win32.Foundation.PWSTR, szLayoutText: Windows.Win32.Foundation.PWSTR, phKL: POINTER(Windows.Win32.UI.TextServices.HKL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def IsIME(hKL: Windows.Win32.UI.TextServices.HKL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def IsUIMessageA(hWndIME: Windows.Win32.Foundation.HWND, msg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def IsUIMessageW(hWndIME: Windows.Win32.Foundation.HWND, msg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def NotifyIME(hIMC: Windows.Win32.Globalization.HIMC, dwAction: UInt32, dwIndex: UInt32, dwValue: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def RegisterWordA(hKL: Windows.Win32.UI.TextServices.HKL, szReading: Windows.Win32.Foundation.PSTR, dwStyle: UInt32, szRegister: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def RegisterWordW(hKL: Windows.Win32.UI.TextServices.HKL, szReading: Windows.Win32.Foundation.PWSTR, dwStyle: UInt32, szRegister: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def ReleaseContext(hWnd: Windows.Win32.Foundation.HWND, hIMC: Windows.Win32.Globalization.HIMC) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def SetCandidateWindow(hIMC: Windows.Win32.Globalization.HIMC, pCandidate: POINTER(Windows.Win32.UI.Input.Ime.CANDIDATEFORM_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def SetCompositionFontA(hIMC: Windows.Win32.Globalization.HIMC, plf: POINTER(Windows.Win32.Graphics.Gdi.LOGFONTA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def SetCompositionFontW(hIMC: Windows.Win32.Globalization.HIMC, plf: POINTER(Windows.Win32.Graphics.Gdi.LOGFONTW_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def SetCompositionStringA(hIMC: Windows.Win32.Globalization.HIMC, dwIndex: UInt32, pComp: c_void_p, dwCompLen: UInt32, pRead: c_void_p, dwReadLen: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def SetCompositionStringW(hIMC: Windows.Win32.Globalization.HIMC, dwIndex: UInt32, pComp: c_void_p, dwCompLen: UInt32, pRead: c_void_p, dwReadLen: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def SetCompositionWindow(hIMC: Windows.Win32.Globalization.HIMC, pCompForm: POINTER(Windows.Win32.UI.Input.Ime.COMPOSITIONFORM_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def SetConversionStatus(hIMC: Windows.Win32.Globalization.HIMC, fdwConversion: UInt32, fdwSentence: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def SetOpenStatus(hIMC: Windows.Win32.Globalization.HIMC, fOpen: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def SetStatusWindowPos(hIMC: Windows.Win32.Globalization.HIMC, pptPos: POINTER(Windows.Win32.Foundation.POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def SimulateHotKey(hWnd: Windows.Win32.Foundation.HWND, dwHotKeyID: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def UnregisterWordA(hKL: Windows.Win32.UI.TextServices.HKL, szReading: Windows.Win32.Foundation.PSTR, dwStyle: UInt32, szUnregister: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def UnregisterWordW(hKL: Windows.Win32.UI.TextServices.HKL, szReading: Windows.Win32.Foundation.PWSTR, dwStyle: UInt32, szUnregister: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def GenerateMessage(hIMC: Windows.Win32.Globalization.HIMC) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def LockIMC(hIMC: Windows.Win32.Globalization.HIMC, ppIMC: POINTER(POINTER(Windows.Win32.UI.Input.Ime.INPUTCONTEXT_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def UnlockIMC(hIMC: Windows.Win32.Globalization.HIMC) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def GetIMCLockCount(hIMC: Windows.Win32.Globalization.HIMC, pdwLockCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def CreateIMCC(dwSize: UInt32, phIMCC: POINTER(Windows.Win32.Globalization.HIMCC)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def DestroyIMCC(hIMCC: Windows.Win32.Globalization.HIMCC) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def LockIMCC(hIMCC: Windows.Win32.Globalization.HIMCC, ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(67)
    def UnlockIMCC(hIMCC: Windows.Win32.Globalization.HIMCC) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(68)
    def ReSizeIMCC(hIMCC: Windows.Win32.Globalization.HIMCC, dwSize: UInt32, phIMCC: POINTER(Windows.Win32.Globalization.HIMCC)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def GetIMCCSize(hIMCC: Windows.Win32.Globalization.HIMCC, pdwSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(70)
    def GetIMCCLockCount(hIMCC: Windows.Win32.Globalization.HIMCC, pdwLockCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(71)
    def GetHotKey(dwHotKeyID: UInt32, puModifiers: POINTER(UInt32), puVKey: POINTER(UInt32), phKL: POINTER(Windows.Win32.UI.TextServices.HKL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(72)
    def SetHotKey(dwHotKeyID: UInt32, uModifiers: UInt32, uVKey: UInt32, hKL: Windows.Win32.UI.TextServices.HKL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(73)
    def CreateSoftKeyboard(uType: UInt32, hOwner: Windows.Win32.Foundation.HWND, x: Int32, y: Int32, phSoftKbdWnd: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(74)
    def DestroySoftKeyboard(hSoftKbdWnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(75)
    def ShowSoftKeyboard(hSoftKbdWnd: Windows.Win32.Foundation.HWND, nCmdShow: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(76)
    def GetCodePageA(hKL: Windows.Win32.UI.TextServices.HKL, uCodePage: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(77)
    def GetLangId(hKL: Windows.Win32.UI.TextServices.HKL, plid: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(78)
    def KeybdEvent(lgidIME: UInt16, bVk: Byte, bScan: Byte, dwFlags: UInt32, dwExtraInfo: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(79)
    def LockModal() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(80)
    def UnlockModal() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(81)
    def AssociateContextEx(hWnd: Windows.Win32.Foundation.HWND, hIMC: Windows.Win32.Globalization.HIMC, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(82)
    def DisableIME(idThread: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(83)
    def GetImeMenuItemsA(hIMC: Windows.Win32.Globalization.HIMC, dwFlags: UInt32, dwType: UInt32, pImeParentMenu: POINTER(Windows.Win32.UI.Input.Ime.IMEMENUITEMINFOA_head), pImeMenu: POINTER(Windows.Win32.UI.Input.Ime.IMEMENUITEMINFOA_head), dwSize: UInt32, pdwResult: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(84)
    def GetImeMenuItemsW(hIMC: Windows.Win32.Globalization.HIMC, dwFlags: UInt32, dwType: UInt32, pImeParentMenu: POINTER(Windows.Win32.UI.Input.Ime.IMEMENUITEMINFOW_head), pImeMenu: POINTER(Windows.Win32.UI.Input.Ime.IMEMENUITEMINFOW_head), dwSize: UInt32, pdwResult: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(85)
    def EnumInputContext(idThread: UInt32, ppEnum: POINTER(Windows.Win32.UI.Input.Ime.IEnumInputContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(86)
    def RequestMessageA(hIMC: Windows.Win32.Globalization.HIMC, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM, plResult: POINTER(Windows.Win32.Foundation.LRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(87)
    def RequestMessageW(hIMC: Windows.Win32.Globalization.HIMC, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM, plResult: POINTER(Windows.Win32.Foundation.LRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(88)
    def SendIMCA(hWnd: Windows.Win32.Foundation.HWND, uMsg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM, plResult: POINTER(Windows.Win32.Foundation.LRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(89)
    def SendIMCW(hWnd: Windows.Win32.Foundation.HWND, uMsg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM, plResult: POINTER(Windows.Win32.Foundation.LRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(90)
    def IsSleeping() -> Windows.Win32.Foundation.HRESULT: ...
class IActiveIMMMessagePumpOwner(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b5cf2cfa-8aeb-11d1-93-64-00-60-b0-67-b8-6e')
    @commethod(3)
    def Start() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def End() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnTranslateMessage(pMsg: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Pause(pdwCookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Resume(dwCookie: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IActiveIMMRegistrar(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b3458082-bd00-11d1-93-9b-00-60-b0-67-b8-6e')
    @commethod(3)
    def RegisterIME(rclsid: POINTER(Guid), lgid: UInt16, pszIconFile: Windows.Win32.Foundation.PWSTR, pszDesc: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterIME(rclsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumInputContext(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('09b5eab0-f997-11d1-93-d4-00-60-b0-67-b8-6e')
    @commethod(3)
    def Clone(ppEnum: POINTER(Windows.Win32.UI.Input.Ime.IEnumInputContext_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(ulCount: UInt32, rgInputContext: POINTER(Windows.Win32.Globalization.HIMC), pcFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(ulCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumRegisterWordA(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('08c03412-f96b-11d0-a4-75-00-aa-00-6b-cc-59')
    @commethod(3)
    def Clone(ppEnum: POINTER(Windows.Win32.UI.Input.Ime.IEnumRegisterWordA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(ulCount: UInt32, rgRegisterWord: POINTER(Windows.Win32.UI.Input.Ime.REGISTERWORDA_head), pcFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(ulCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumRegisterWordW(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4955dd31-b159-11d0-8f-cf-00-aa-00-6b-cc-59')
    @commethod(3)
    def Clone(ppEnum: POINTER(Windows.Win32.UI.Input.Ime.IEnumRegisterWordW_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(ulCount: UInt32, rgRegisterWord: POINTER(Windows.Win32.UI.Input.Ime.REGISTERWORDW_head), pcFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(ulCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IFEClassFactory(c_void_p):
    extends: Windows.Win32.System.Com.IClassFactory
class IFECommon(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('019f7151-e6db-11d0-83-c3-00-c0-4f-dd-b8-2e')
    @commethod(3)
    def IsDefaultIME(szName: Windows.Win32.Foundation.PSTR, cszName: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetDefaultIME() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InvokeWordRegDialog(pimedlg: POINTER(Windows.Win32.UI.Input.Ime.IMEDLG_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def InvokeDictToolDialog(pimedlg: POINTER(Windows.Win32.UI.Input.Ime.IMEDLG_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFEDictionary(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('019f7153-e6db-11d0-83-c3-00-c0-4f-dd-b8-2e')
    @commethod(3)
    def Open(pchDictPath: Windows.Win32.Foundation.PSTR, pshf: POINTER(Windows.Win32.UI.Input.Ime.IMESHF_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetHeader(pchDictPath: Windows.Win32.Foundation.PSTR, pshf: POINTER(Windows.Win32.UI.Input.Ime.IMESHF_head), pjfmt: POINTER(Windows.Win32.UI.Input.Ime.IMEFMT), pulType: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DisplayProperty(hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPosTable(prgPosTbl: POINTER(POINTER(Windows.Win32.UI.Input.Ime.POSTBL_head)), pcPosTbl: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetWords(pwchFirst: Windows.Win32.Foundation.PWSTR, pwchLast: Windows.Win32.Foundation.PWSTR, pwchDisplay: Windows.Win32.Foundation.PWSTR, ulPos: UInt32, ulSelect: UInt32, ulWordSrc: UInt32, pchBuffer: c_char_p_no, cbBuffer: UInt32, pcWrd: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def NextWords(pchBuffer: c_char_p_no, cbBuffer: UInt32, pcWrd: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Create(pchDictPath: Windows.Win32.Foundation.PSTR, pshf: POINTER(Windows.Win32.UI.Input.Ime.IMESHF_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetHeader(pshf: POINTER(Windows.Win32.UI.Input.Ime.IMESHF_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ExistWord(pwrd: POINTER(Windows.Win32.UI.Input.Ime.IMEWRD_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def ExistDependency(pdp: POINTER(Windows.Win32.UI.Input.Ime.IMEDP_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def RegisterWord(reg: Windows.Win32.UI.Input.Ime.IMEREG, pwrd: POINTER(Windows.Win32.UI.Input.Ime.IMEWRD_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def RegisterDependency(reg: Windows.Win32.UI.Input.Ime.IMEREG, pdp: POINTER(Windows.Win32.UI.Input.Ime.IMEDP_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetDependencies(pwchKakariReading: Windows.Win32.Foundation.PWSTR, pwchKakariDisplay: Windows.Win32.Foundation.PWSTR, ulKakariPos: UInt32, pwchUkeReading: Windows.Win32.Foundation.PWSTR, pwchUkeDisplay: Windows.Win32.Foundation.PWSTR, ulUkePos: UInt32, jrel: Windows.Win32.UI.Input.Ime.IMEREL, ulWordSrc: UInt32, pchBuffer: c_char_p_no, cbBuffer: UInt32, pcdp: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def NextDependencies(pchBuffer: c_char_p_no, cbBuffer: UInt32, pcDp: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def ConvertFromOldMSIME(pchDic: Windows.Win32.Foundation.PSTR, pfnLog: Windows.Win32.UI.Input.Ime.PFNLOG, reg: Windows.Win32.UI.Input.Ime.IMEREG) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def ConvertFromUserToSys() -> Windows.Win32.Foundation.HRESULT: ...
class IFELanguage(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('019f7152-e6db-11d0-83-c3-00-c0-4f-dd-b8-2e')
    @commethod(3)
    def Open() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetJMorphResult(dwRequest: UInt32, dwCMode: UInt32, cwchInput: Int32, pwchInput: Windows.Win32.Foundation.PWSTR, pfCInfo: POINTER(UInt32), ppResult: POINTER(POINTER(Windows.Win32.UI.Input.Ime.MORRSLT_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetConversionModeCaps(pdwCaps: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPhonetic(string: Windows.Win32.Foundation.BSTR, start: Int32, length: Int32, phonetic: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetConversion(string: Windows.Win32.Foundation.BSTR, start: Int32, length: Int32, result: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IImePad(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5d8e643a-c3a9-11d1-af-ef-00-80-5f-0c-8b-6d')
    @commethod(3)
    def Request(pIImePadApplet: Windows.Win32.UI.Input.Ime.IImePadApplet_head, reqId: Windows.Win32.UI.Input.Ime.IME_PAD_REQUEST_FLAGS, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
class IImePadApplet(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5d8e643b-c3a9-11d1-af-ef-00-80-5f-0c-8b-6d')
    @commethod(3)
    def Initialize(lpIImePad: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Terminate() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAppletConfig(lpAppletCfg: POINTER(Windows.Win32.UI.Input.Ime.IMEAPPLETCFG_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateUI(hwndParent: Windows.Win32.Foundation.HWND, lpImeAppletUI: POINTER(Windows.Win32.UI.Input.Ime.IMEAPPLETUI_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Notify(lpImePad: Windows.Win32.System.Com.IUnknown_head, notify: Int32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.HRESULT: ...
class IImePlugInDictDictionaryList(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('98752974-b0a6-489b-8f-6f-bf-f3-76-9c-8e-eb')
    @commethod(3)
    def GetDictionariesInUse(prgDictionaryGUID: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head)), prgDateCreated: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head)), prgfEncrypted: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DeleteDictionary(bstrDictionaryGUID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IImeSpecifyApplets(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5d8e643c-c3a9-11d1-af-ef-00-80-5f-0c-8b-6d')
    @commethod(3)
    def GetAppletIIDList(refiid: POINTER(Guid), lpIIDList: POINTER(Windows.Win32.UI.Input.Ime.APPLETIDLIST_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def IMCENUMPROC(param0: Windows.Win32.Globalization.HIMC, param1: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.BOOL: ...
class IMEAPPLETCFG(Structure):
    dwConfig: UInt32
    wchTitle: Char * 64
    wchTitleFontFace: Char * 32
    dwCharSet: UInt32
    iCategory: Int32
    hIcon: Windows.Win32.UI.WindowsAndMessaging.HICON
    langID: UInt16
    dummy: UInt16
    lReserved1: Windows.Win32.Foundation.LPARAM
class IMEAPPLETUI(Structure):
    hwnd: Windows.Win32.Foundation.HWND
    dwStyle: UInt32
    width: Int32
    height: Int32
    minWidth: Int32
    minHeight: Int32
    maxWidth: Int32
    maxHeight: Int32
    lReserved1: Windows.Win32.Foundation.LPARAM
    lReserved2: Windows.Win32.Foundation.LPARAM
class IMECHARINFO(Structure):
    wch: Char
    dwCharInfo: UInt32
class IMECHARPOSITION(Structure):
    dwSize: UInt32
    dwCharPos: UInt32
    pt: Windows.Win32.Foundation.POINT
    cLineHeight: UInt32
    rcDocument: Windows.Win32.Foundation.RECT
class IMECOMPOSITIONSTRINGINFO(Structure):
    iCompStrLen: Int32
    iCaretPos: Int32
    iEditStart: Int32
    iEditLen: Int32
    iTargetStart: Int32
    iTargetLen: Int32
class IMEDLG(Structure):
    cbIMEDLG: Int32
    hwnd: Windows.Win32.Foundation.HWND
    lpwstrWord: Windows.Win32.Foundation.PWSTR
    nTabId: Int32
    _pack_ = 1
class IMEDP(Structure):
    wrdModifier: Windows.Win32.UI.Input.Ime.IMEWRD
    wrdModifiee: Windows.Win32.UI.Input.Ime.IMEWRD
    relID: Windows.Win32.UI.Input.Ime.IMEREL
    _pack_ = 1
class IMEFAREASTINFO(Structure):
    dwSize: UInt32
    dwType: UInt32
    dwData: UInt32 * 1
IMEFMT = Int32
IFED_UNKNOWN: IMEFMT = 0
IFED_MSIME2_BIN_SYSTEM: IMEFMT = 1
IFED_MSIME2_BIN_USER: IMEFMT = 2
IFED_MSIME2_TEXT_USER: IMEFMT = 3
IFED_MSIME95_BIN_SYSTEM: IMEFMT = 4
IFED_MSIME95_BIN_USER: IMEFMT = 5
IFED_MSIME95_TEXT_USER: IMEFMT = 6
IFED_MSIME97_BIN_SYSTEM: IMEFMT = 7
IFED_MSIME97_BIN_USER: IMEFMT = 8
IFED_MSIME97_TEXT_USER: IMEFMT = 9
IFED_MSIME98_BIN_SYSTEM: IMEFMT = 10
IFED_MSIME98_BIN_USER: IMEFMT = 11
IFED_MSIME98_TEXT_USER: IMEFMT = 12
IFED_ACTIVE_DICT: IMEFMT = 13
IFED_ATOK9: IMEFMT = 14
IFED_ATOK10: IMEFMT = 15
IFED_NEC_AI_: IMEFMT = 16
IFED_WX_II: IMEFMT = 17
IFED_WX_III: IMEFMT = 18
IFED_VJE_20: IMEFMT = 19
IFED_MSIME98_SYSTEM_CE: IMEFMT = 20
IFED_MSIME_BIN_SYSTEM: IMEFMT = 21
IFED_MSIME_BIN_USER: IMEFMT = 22
IFED_MSIME_TEXT_USER: IMEFMT = 23
IFED_PIME2_BIN_USER: IMEFMT = 24
IFED_PIME2_BIN_SYSTEM: IMEFMT = 25
IFED_PIME2_BIN_STANDARD_SYSTEM: IMEFMT = 26
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
    lpItemData: c_void_p
class IMEITEMCANDIDATE(Structure):
    uCount: UInt32
    imeItem: Windows.Win32.UI.Input.Ime.IMEITEM * 1
class IMEKMS(Structure):
    cbSize: Int32
    hIMC: Windows.Win32.Globalization.HIMC
    cKeyList: UInt32
    pKeyList: POINTER(Windows.Win32.UI.Input.Ime.IMEKMSKEY_head)
    _pack_ = 1
class IMEKMSFUNCDESC(Structure):
    cbSize: Int32
    idLang: UInt16
    dwControl: UInt32
    pwszDescription: Char * 128
    _pack_ = 1
class IMEKMSINIT(Structure):
    cbSize: Int32
    hWnd: Windows.Win32.Foundation.HWND
    _pack_ = 1
class IMEKMSINVK(Structure):
    cbSize: Int32
    hIMC: Windows.Win32.Globalization.HIMC
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
    hIMC: Windows.Win32.Globalization.HIMC
    idLang: UInt16
    wVKStart: UInt16
    wVKEnd: UInt16
    cKeyList: Int32
    pKeyList: POINTER(Windows.Win32.UI.Input.Ime.IMEKMSKEY_head)
    _pack_ = 1
class IMEKMSNTFY(Structure):
    cbSize: Int32
    hIMC: Windows.Win32.Globalization.HIMC
    fSelect: Windows.Win32.Foundation.BOOL
    _pack_ = 1
class IMEMENUITEMINFOA(Structure):
    cbSize: UInt32
    fType: UInt32
    fState: UInt32
    wID: UInt32
    hbmpChecked: Windows.Win32.Graphics.Gdi.HBITMAP
    hbmpUnchecked: Windows.Win32.Graphics.Gdi.HBITMAP
    dwItemData: UInt32
    szString: Windows.Win32.Foundation.CHAR * 80
    hbmpItem: Windows.Win32.Graphics.Gdi.HBITMAP
class IMEMENUITEMINFOW(Structure):
    cbSize: UInt32
    fType: UInt32
    fState: UInt32
    wID: UInt32
    hbmpChecked: Windows.Win32.Graphics.Gdi.HBITMAP
    hbmpUnchecked: Windows.Win32.Graphics.Gdi.HBITMAP
    dwItemData: UInt32
    szString: Char * 80
    hbmpItem: Windows.Win32.Graphics.Gdi.HBITMAP
IMEREG = Int32
IFED_REG_HEAD: IMEREG = 0
IFED_REG_TAIL: IMEREG = 1
IFED_REG_DEL: IMEREG = 2
IMEREL = Int32
IFED_REL_NONE: IMEREL = 0
IFED_REL_NO: IMEREL = 1
IFED_REL_GA: IMEREL = 2
IFED_REL_WO: IMEREL = 3
IFED_REL_NI: IMEREL = 4
IFED_REL_DE: IMEREL = 5
IFED_REL_YORI: IMEREL = 6
IFED_REL_KARA: IMEREL = 7
IFED_REL_MADE: IMEREL = 8
IFED_REL_HE: IMEREL = 9
IFED_REL_TO: IMEREL = 10
IFED_REL_IDEOM: IMEREL = 11
IFED_REL_FUKU_YOUGEN: IMEREL = 12
IFED_REL_KEIYOU_YOUGEN: IMEREL = 13
IFED_REL_KEIDOU1_YOUGEN: IMEREL = 14
IFED_REL_KEIDOU2_YOUGEN: IMEREL = 15
IFED_REL_TAIGEN: IMEREL = 16
IFED_REL_YOUGEN: IMEREL = 17
IFED_REL_RENTAI_MEI: IMEREL = 18
IFED_REL_RENSOU: IMEREL = 19
IFED_REL_KEIYOU_TO_YOUGEN: IMEREL = 20
IFED_REL_KEIYOU_TARU_YOUGEN: IMEREL = 21
IFED_REL_UNKNOWN1: IMEREL = 22
IFED_REL_UNKNOWN2: IMEREL = 23
IFED_REL_ALL: IMEREL = 24
class IMESHF(Structure):
    cbShf: UInt16
    verDic: UInt16
    szTitle: Windows.Win32.Foundation.CHAR * 48
    szDescription: Windows.Win32.Foundation.CHAR * 256
    szCopyright: Windows.Win32.Foundation.CHAR * 128
    _pack_ = 1
class IMESTRINGCANDIDATE(Structure):
    uCount: UInt32
    lpwstr: Windows.Win32.Foundation.PWSTR * 1
class IMESTRINGCANDIDATEINFO(Structure):
    dwFarEastId: UInt32
    lpFarEastInfo: POINTER(Windows.Win32.UI.Input.Ime.IMEFAREASTINFO_head)
    fInfoMask: UInt32
    iSelIndex: Int32
    uCount: UInt32
    lpwstr: Windows.Win32.Foundation.PWSTR * 1
class IMESTRINGINFO(Structure):
    dwFarEastId: UInt32
    lpwstr: Windows.Win32.Foundation.PWSTR
IMEUCT = Int32
IFED_UCT_NONE: IMEUCT = 0
IFED_UCT_STRING_SJIS: IMEUCT = 1
IFED_UCT_STRING_UNICODE: IMEUCT = 2
IFED_UCT_USER_DEFINED: IMEUCT = 3
IFED_UCT_MAX: IMEUCT = 4
class IMEWRD(Structure):
    pwchReading: Windows.Win32.Foundation.PWSTR
    pwchDisplay: Windows.Win32.Foundation.PWSTR
    Anonymous: _Anonymous_e__Union
    rgulAttrs: UInt32 * 2
    cbComment: Int32
    uct: Windows.Win32.UI.Input.Ime.IMEUCT
    pvComment: c_void_p
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
GCS_COMPREADSTR: IME_COMPOSITION_STRING = 1
GCS_COMPREADATTR: IME_COMPOSITION_STRING = 2
GCS_COMPREADCLAUSE: IME_COMPOSITION_STRING = 4
GCS_COMPSTR: IME_COMPOSITION_STRING = 8
GCS_COMPATTR: IME_COMPOSITION_STRING = 16
GCS_COMPCLAUSE: IME_COMPOSITION_STRING = 32
GCS_CURSORPOS: IME_COMPOSITION_STRING = 128
GCS_DELTASTART: IME_COMPOSITION_STRING = 256
GCS_RESULTREADSTR: IME_COMPOSITION_STRING = 512
GCS_RESULTREADCLAUSE: IME_COMPOSITION_STRING = 1024
GCS_RESULTSTR: IME_COMPOSITION_STRING = 2048
GCS_RESULTCLAUSE: IME_COMPOSITION_STRING = 4096
IME_CONVERSION_MODE = UInt32
IME_CMODE_ALPHANUMERIC: IME_CONVERSION_MODE = 0
IME_CMODE_NATIVE: IME_CONVERSION_MODE = 1
IME_CMODE_CHINESE: IME_CONVERSION_MODE = 1
IME_CMODE_HANGUL: IME_CONVERSION_MODE = 1
IME_CMODE_JAPANESE: IME_CONVERSION_MODE = 1
IME_CMODE_KATAKANA: IME_CONVERSION_MODE = 2
IME_CMODE_LANGUAGE: IME_CONVERSION_MODE = 3
IME_CMODE_FULLSHAPE: IME_CONVERSION_MODE = 8
IME_CMODE_ROMAN: IME_CONVERSION_MODE = 16
IME_CMODE_CHARCODE: IME_CONVERSION_MODE = 32
IME_CMODE_HANJACONVERT: IME_CONVERSION_MODE = 64
IME_CMODE_NATIVESYMBOL: IME_CONVERSION_MODE = 128
IME_CMODE_HANGEUL: IME_CONVERSION_MODE = 1
IME_CMODE_SOFTKBD: IME_CONVERSION_MODE = 128
IME_CMODE_NOCONVERSION: IME_CONVERSION_MODE = 256
IME_CMODE_EUDC: IME_CONVERSION_MODE = 512
IME_CMODE_SYMBOL: IME_CONVERSION_MODE = 1024
IME_CMODE_FIXED: IME_CONVERSION_MODE = 2048
IME_CMODE_RESERVED: IME_CONVERSION_MODE = 4026531840
IME_ESCAPE = UInt32
IME_ESC_QUERY_SUPPORT: IME_ESCAPE = 3
IME_ESC_RESERVED_FIRST: IME_ESCAPE = 4
IME_ESC_RESERVED_LAST: IME_ESCAPE = 2047
IME_ESC_PRIVATE_FIRST: IME_ESCAPE = 2048
IME_ESC_PRIVATE_LAST: IME_ESCAPE = 4095
IME_ESC_SEQUENCE_TO_INTERNAL: IME_ESCAPE = 4097
IME_ESC_GET_EUDC_DICTIONARY: IME_ESCAPE = 4099
IME_ESC_SET_EUDC_DICTIONARY: IME_ESCAPE = 4100
IME_ESC_MAX_KEY: IME_ESCAPE = 4101
IME_ESC_IME_NAME: IME_ESCAPE = 4102
IME_ESC_SYNC_HOTKEY: IME_ESCAPE = 4103
IME_ESC_HANJA_MODE: IME_ESCAPE = 4104
IME_ESC_AUTOMATA: IME_ESCAPE = 4105
IME_ESC_PRIVATE_HOTKEY: IME_ESCAPE = 4106
IME_ESC_GETHELPFILENAME: IME_ESCAPE = 4107
IME_HOTKEY_IDENTIFIER = UInt32
IME_CHOTKEY_IME_NONIME_TOGGLE: IME_HOTKEY_IDENTIFIER = 16
IME_CHOTKEY_SHAPE_TOGGLE: IME_HOTKEY_IDENTIFIER = 17
IME_CHOTKEY_SYMBOL_TOGGLE: IME_HOTKEY_IDENTIFIER = 18
IME_JHOTKEY_CLOSE_OPEN: IME_HOTKEY_IDENTIFIER = 48
IME_KHOTKEY_SHAPE_TOGGLE: IME_HOTKEY_IDENTIFIER = 80
IME_KHOTKEY_HANJACONVERT: IME_HOTKEY_IDENTIFIER = 81
IME_KHOTKEY_ENGLISH: IME_HOTKEY_IDENTIFIER = 82
IME_THOTKEY_IME_NONIME_TOGGLE: IME_HOTKEY_IDENTIFIER = 112
IME_THOTKEY_SHAPE_TOGGLE: IME_HOTKEY_IDENTIFIER = 113
IME_THOTKEY_SYMBOL_TOGGLE: IME_HOTKEY_IDENTIFIER = 114
IME_ITHOTKEY_RESEND_RESULTSTR: IME_HOTKEY_IDENTIFIER = 512
IME_ITHOTKEY_PREVIOUS_COMPOSITION: IME_HOTKEY_IDENTIFIER = 513
IME_ITHOTKEY_UISTYLE_TOGGLE: IME_HOTKEY_IDENTIFIER = 514
IME_ITHOTKEY_RECONVERTSTRING: IME_HOTKEY_IDENTIFIER = 515
IME_PAD_REQUEST_FLAGS = UInt32
IMEPADREQ_INSERTSTRING: IME_PAD_REQUEST_FLAGS = 4097
IMEPADREQ_SENDCONTROL: IME_PAD_REQUEST_FLAGS = 4100
IMEPADREQ_SETAPPLETSIZE: IME_PAD_REQUEST_FLAGS = 4104
IMEPADREQ_GETCOMPOSITIONSTRING: IME_PAD_REQUEST_FLAGS = 4102
IMEPADREQ_GETCOMPOSITIONSTRINGINFO: IME_PAD_REQUEST_FLAGS = 4108
IMEPADREQ_DELETESTRING: IME_PAD_REQUEST_FLAGS = 4112
IMEPADREQ_CHANGESTRING: IME_PAD_REQUEST_FLAGS = 4113
IMEPADREQ_GETAPPLHWND: IME_PAD_REQUEST_FLAGS = 4116
IMEPADREQ_FORCEIMEPADWINDOWSHOW: IME_PAD_REQUEST_FLAGS = 4117
IMEPADREQ_POSTMODALNOTIFY: IME_PAD_REQUEST_FLAGS = 4118
IMEPADREQ_GETDEFAULTUILANGID: IME_PAD_REQUEST_FLAGS = 4119
IMEPADREQ_GETAPPLETUISTYLE: IME_PAD_REQUEST_FLAGS = 4121
IMEPADREQ_SETAPPLETUISTYLE: IME_PAD_REQUEST_FLAGS = 4122
IMEPADREQ_ISAPPLETACTIVE: IME_PAD_REQUEST_FLAGS = 4123
IMEPADREQ_ISIMEPADWINDOWVISIBLE: IME_PAD_REQUEST_FLAGS = 4124
IMEPADREQ_SETAPPLETMINMAXSIZE: IME_PAD_REQUEST_FLAGS = 4125
IMEPADREQ_GETCONVERSIONSTATUS: IME_PAD_REQUEST_FLAGS = 4126
IMEPADREQ_GETVERSION: IME_PAD_REQUEST_FLAGS = 4127
IMEPADREQ_GETCURRENTIMEINFO: IME_PAD_REQUEST_FLAGS = 4128
IME_SENTENCE_MODE = UInt32
IME_SMODE_NONE: IME_SENTENCE_MODE = 0
IME_SMODE_PLAURALCLAUSE: IME_SENTENCE_MODE = 1
IME_SMODE_SINGLECONVERT: IME_SENTENCE_MODE = 2
IME_SMODE_AUTOMATIC: IME_SENTENCE_MODE = 4
IME_SMODE_PHRASEPREDICT: IME_SENTENCE_MODE = 8
IME_SMODE_CONVERSATION: IME_SENTENCE_MODE = 16
IME_SMODE_RESERVED: IME_SENTENCE_MODE = 61440
class INPUTCONTEXT(Structure):
    hWnd: Windows.Win32.Foundation.HWND
    fOpen: Windows.Win32.Foundation.BOOL
    ptStatusWndPos: Windows.Win32.Foundation.POINT
    ptSoftKbdPos: Windows.Win32.Foundation.POINT
    fdwConversion: UInt32
    fdwSentence: UInt32
    lfFont: _lfFont_e__Union
    cfCompForm: Windows.Win32.UI.Input.Ime.COMPOSITIONFORM
    cfCandForm: Windows.Win32.UI.Input.Ime.CANDIDATEFORM * 4
    hCompStr: Windows.Win32.Globalization.HIMCC
    hCandInfo: Windows.Win32.Globalization.HIMCC
    hGuideLine: Windows.Win32.Globalization.HIMCC
    hPrivate: Windows.Win32.Globalization.HIMCC
    dwNumMsgBuf: UInt32
    hMsgBuf: Windows.Win32.Globalization.HIMCC
    fdwInit: UInt32
    dwReserve: UInt32 * 3
    class _lfFont_e__Union(Union):
        A: Windows.Win32.Graphics.Gdi.LOGFONTA
        W: Windows.Win32.Graphics.Gdi.LOGFONTW
class MORRSLT(Structure):
    dwSize: UInt32
    pwchOutput: Windows.Win32.Foundation.PWSTR
    cchOutput: UInt16
    Anonymous1: _Anonymous1_e__Union
    Anonymous2: _Anonymous2_e__Union
    pchInputPos: POINTER(UInt16)
    pchOutputIdxWDD: POINTER(UInt16)
    Anonymous3: _Anonymous3_e__Union
    paMonoRubyPos: POINTER(UInt16)
    pWDD: POINTER(Windows.Win32.UI.Input.Ime.WDD_head)
    cWDD: Int32
    pPrivate: c_void_p
    BLKBuff: Char * 1
    _pack_ = 1
    class _Anonymous1_e__Union(Union):
        pwchRead: Windows.Win32.Foundation.PWSTR
        pwchComp: Windows.Win32.Foundation.PWSTR
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
NI_CHANGECANDIDATELIST: NOTIFY_IME_ACTION = 19
NI_CLOSECANDIDATE: NOTIFY_IME_ACTION = 17
NI_COMPOSITIONSTR: NOTIFY_IME_ACTION = 21
NI_IMEMENUSELECTED: NOTIFY_IME_ACTION = 24
NI_OPENCANDIDATE: NOTIFY_IME_ACTION = 16
NI_SELECTCANDIDATESTR: NOTIFY_IME_ACTION = 18
NI_SETCANDIDATE_PAGESIZE: NOTIFY_IME_ACTION = 23
NI_SETCANDIDATE_PAGESTART: NOTIFY_IME_ACTION = 22
NOTIFY_IME_INDEX = UInt32
CPS_CANCEL: NOTIFY_IME_INDEX = 4
CPS_COMPLETE: NOTIFY_IME_INDEX = 1
CPS_CONVERT: NOTIFY_IME_INDEX = 2
CPS_REVERT: NOTIFY_IME_INDEX = 3
@winfunctype_pointer
def PFNLOG(param0: POINTER(Windows.Win32.UI.Input.Ime.IMEDP_head), param1: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.BOOL: ...
class POSTBL(Structure):
    nPos: UInt16
    szName: c_char_p_no
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
    lpReading: Windows.Win32.Foundation.PSTR
    lpWord: Windows.Win32.Foundation.PSTR
@winfunctype_pointer
def REGISTERWORDENUMPROCA(lpszReading: Windows.Win32.Foundation.PSTR, param1: UInt32, lpszString: Windows.Win32.Foundation.PSTR, param3: c_void_p) -> Int32: ...
@winfunctype_pointer
def REGISTERWORDENUMPROCW(lpszReading: Windows.Win32.Foundation.PWSTR, param1: UInt32, lpszString: Windows.Win32.Foundation.PWSTR, param3: c_void_p) -> Int32: ...
class REGISTERWORDW(Structure):
    lpReading: Windows.Win32.Foundation.PWSTR
    lpWord: Windows.Win32.Foundation.PWSTR
SET_COMPOSITION_STRING_TYPE = UInt32
SCS_SETSTR: SET_COMPOSITION_STRING_TYPE = 9
SCS_CHANGEATTR: SET_COMPOSITION_STRING_TYPE = 18
SCS_CHANGECLAUSE: SET_COMPOSITION_STRING_TYPE = 36
SCS_SETRECONVERTSTRING: SET_COMPOSITION_STRING_TYPE = 65536
SCS_QUERYRECONVERTSTRING: SET_COMPOSITION_STRING_TYPE = 131072
class SOFTKBDDATA(Structure):
    uCount: UInt32
    wCode: UInt16 * 256
class STYLEBUFA(Structure):
    dwStyle: UInt32
    szDescription: Windows.Win32.Foundation.CHAR * 32
class STYLEBUFW(Structure):
    dwStyle: UInt32
    szDescription: Char * 32
class TRANSMSG(Structure):
    message: UInt32
    wParam: Windows.Win32.Foundation.WPARAM
    lParam: Windows.Win32.Foundation.LPARAM
class TRANSMSGLIST(Structure):
    uMsgCount: UInt32
    TransMsg: Windows.Win32.UI.Input.Ime.TRANSMSG * 1
class WDD(Structure):
    wDispPos: UInt16
    Anonymous1: _Anonymous1_e__Union
    cchDisp: UInt16
    Anonymous2: _Anonymous2_e__Union
    WDD_nReserve1: UInt32
    nPos: UInt16
    _bitfield: UInt16
    pReserved: c_void_p
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
def fpCreateIFECommonInstanceType(ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def fpCreateIFEDictionaryInstanceType(ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def fpCreateIFELanguageInstanceType(clsid: POINTER(Guid), ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'APPLETIDLIST')
make_head(_module, 'APPLYCANDEXPARAM')
make_head(_module, 'CANDIDATEFORM')
make_head(_module, 'CANDIDATEINFO')
make_head(_module, 'CANDIDATELIST')
make_head(_module, 'COMPOSITIONFORM')
make_head(_module, 'COMPOSITIONSTRING')
make_head(_module, 'GUIDELINE')
make_head(_module, 'IActiveIME')
make_head(_module, 'IActiveIME2')
make_head(_module, 'IActiveIMMApp')
make_head(_module, 'IActiveIMMIME')
make_head(_module, 'IActiveIMMMessagePumpOwner')
make_head(_module, 'IActiveIMMRegistrar')
make_head(_module, 'IEnumInputContext')
make_head(_module, 'IEnumRegisterWordA')
make_head(_module, 'IEnumRegisterWordW')
make_head(_module, 'IFEClassFactory')
make_head(_module, 'IFECommon')
make_head(_module, 'IFEDictionary')
make_head(_module, 'IFELanguage')
make_head(_module, 'IImePad')
make_head(_module, 'IImePadApplet')
make_head(_module, 'IImePlugInDictDictionaryList')
make_head(_module, 'IImeSpecifyApplets')
make_head(_module, 'IMCENUMPROC')
make_head(_module, 'IMEAPPLETCFG')
make_head(_module, 'IMEAPPLETUI')
make_head(_module, 'IMECHARINFO')
make_head(_module, 'IMECHARPOSITION')
make_head(_module, 'IMECOMPOSITIONSTRINGINFO')
make_head(_module, 'IMEDLG')
make_head(_module, 'IMEDP')
make_head(_module, 'IMEFAREASTINFO')
make_head(_module, 'IMEINFO')
make_head(_module, 'IMEITEM')
make_head(_module, 'IMEITEMCANDIDATE')
make_head(_module, 'IMEKMS')
make_head(_module, 'IMEKMSFUNCDESC')
make_head(_module, 'IMEKMSINIT')
make_head(_module, 'IMEKMSINVK')
make_head(_module, 'IMEKMSKEY')
make_head(_module, 'IMEKMSKMP')
make_head(_module, 'IMEKMSNTFY')
make_head(_module, 'IMEMENUITEMINFOA')
make_head(_module, 'IMEMENUITEMINFOW')
make_head(_module, 'IMESHF')
make_head(_module, 'IMESTRINGCANDIDATE')
make_head(_module, 'IMESTRINGCANDIDATEINFO')
make_head(_module, 'IMESTRINGINFO')
make_head(_module, 'IMEWRD')
make_head(_module, 'INPUTCONTEXT')
make_head(_module, 'MORRSLT')
make_head(_module, 'PFNLOG')
make_head(_module, 'POSTBL')
make_head(_module, 'RECONVERTSTRING')
make_head(_module, 'REGISTERWORDA')
make_head(_module, 'REGISTERWORDENUMPROCA')
make_head(_module, 'REGISTERWORDENUMPROCW')
make_head(_module, 'REGISTERWORDW')
make_head(_module, 'SOFTKBDDATA')
make_head(_module, 'STYLEBUFA')
make_head(_module, 'STYLEBUFW')
make_head(_module, 'TRANSMSG')
make_head(_module, 'TRANSMSGLIST')
make_head(_module, 'WDD')
make_head(_module, 'fpCreateIFECommonInstanceType')
make_head(_module, 'fpCreateIFEDictionaryInstanceType')
make_head(_module, 'fpCreateIFELanguageInstanceType')
__all__ = [
    "APPLETIDLIST",
    "APPLYCANDEXPARAM",
    "ATTR_CONVERTED",
    "ATTR_FIXEDCONVERTED",
    "ATTR_INPUT",
    "ATTR_INPUT_ERROR",
    "ATTR_TARGET_CONVERTED",
    "ATTR_TARGET_NOTCONVERTED",
    "CANDIDATEFORM",
    "CANDIDATEINFO",
    "CANDIDATELIST",
    "CATID_MSIME_IImePadApplet",
    "CATID_MSIME_IImePadApplet1000",
    "CATID_MSIME_IImePadApplet1200",
    "CATID_MSIME_IImePadApplet900",
    "CATID_MSIME_IImePadApplet_VER7",
    "CATID_MSIME_IImePadApplet_VER80",
    "CATID_MSIME_IImePadApplet_VER81",
    "CActiveIMM",
    "CFS_CANDIDATEPOS",
    "CFS_DEFAULT",
    "CFS_EXCLUDE",
    "CFS_FORCE_POSITION",
    "CFS_POINT",
    "CFS_RECT",
    "CHARINFO_APPLETID_MASK",
    "CHARINFO_CHARID_MASK",
    "CHARINFO_FEID_MASK",
    "CLSID_ImePlugInDictDictionaryList_CHS",
    "CLSID_ImePlugInDictDictionaryList_JPN",
    "CLSID_VERSION_DEPENDENT_MSIME_JAPANESE",
    "COMPOSITIONFORM",
    "COMPOSITIONSTRING",
    "CPS_CANCEL",
    "CPS_COMPLETE",
    "CPS_CONVERT",
    "CPS_REVERT",
    "CS_INSERTCHAR",
    "CS_NOMOVECARET",
    "E_LARGEINPUT",
    "E_NOCAND",
    "E_NOTENOUGH_BUFFER",
    "E_NOTENOUGH_WDD",
    "FEID_CHINESE_HONGKONG",
    "FEID_CHINESE_SIMPLIFIED",
    "FEID_CHINESE_SINGAPORE",
    "FEID_CHINESE_TRADITIONAL",
    "FEID_JAPANESE",
    "FEID_KOREAN",
    "FEID_KOREAN_JOHAB",
    "FEID_NONE",
    "FELANG_CLMN_FIXD",
    "FELANG_CLMN_FIXR",
    "FELANG_CLMN_NOPBREAK",
    "FELANG_CLMN_NOWBREAK",
    "FELANG_CLMN_PBREAK",
    "FELANG_CLMN_WBREAK",
    "FELANG_CMODE_AUTOMATIC",
    "FELANG_CMODE_BESTFIRST",
    "FELANG_CMODE_BOPOMOFO",
    "FELANG_CMODE_CONVERSATION",
    "FELANG_CMODE_FULLWIDTHOUT",
    "FELANG_CMODE_HALFWIDTHOUT",
    "FELANG_CMODE_HANGUL",
    "FELANG_CMODE_HIRAGANAOUT",
    "FELANG_CMODE_KATAKANAOUT",
    "FELANG_CMODE_MERGECAND",
    "FELANG_CMODE_MONORUBY",
    "FELANG_CMODE_NAME",
    "FELANG_CMODE_NOINVISIBLECHAR",
    "FELANG_CMODE_NONE",
    "FELANG_CMODE_NOPRUNING",
    "FELANG_CMODE_PHRASEPREDICT",
    "FELANG_CMODE_PINYIN",
    "FELANG_CMODE_PLAURALCLAUSE",
    "FELANG_CMODE_PRECONV",
    "FELANG_CMODE_RADICAL",
    "FELANG_CMODE_ROMAN",
    "FELANG_CMODE_SINGLECONVERT",
    "FELANG_CMODE_UNKNOWNREADING",
    "FELANG_CMODE_USENOREVWORDS",
    "FELANG_INVALD_PO",
    "FELANG_REQ_CONV",
    "FELANG_REQ_RECONV",
    "FELANG_REQ_REV",
    "FID_MSIME_KMS_DEL_KEYLIST",
    "FID_MSIME_KMS_FUNCDESC",
    "FID_MSIME_KMS_GETMAP",
    "FID_MSIME_KMS_GETMAPFAST",
    "FID_MSIME_KMS_GETMAPSEAMLESS",
    "FID_MSIME_KMS_INIT",
    "FID_MSIME_KMS_INVOKE",
    "FID_MSIME_KMS_NOTIFY",
    "FID_MSIME_KMS_SETMAP",
    "FID_MSIME_KMS_TERM",
    "FID_MSIME_KMS_VERSION",
    "FID_MSIME_VERSION",
    "FID_RECONVERT_VERSION",
    "GCL_CONVERSION",
    "GCL_REVERSECONVERSION",
    "GCL_REVERSE_LENGTH",
    "GCSEX_CANCELRECONVERT",
    "GCS_COMPATTR",
    "GCS_COMPCLAUSE",
    "GCS_COMPREADATTR",
    "GCS_COMPREADCLAUSE",
    "GCS_COMPREADSTR",
    "GCS_COMPSTR",
    "GCS_CURSORPOS",
    "GCS_DELTASTART",
    "GCS_RESULTCLAUSE",
    "GCS_RESULTREADCLAUSE",
    "GCS_RESULTREADSTR",
    "GCS_RESULTSTR",
    "GET_CONVERSION_LIST_FLAG",
    "GET_GUIDE_LINE_TYPE",
    "GGL_INDEX",
    "GGL_LEVEL",
    "GGL_PRIVATE",
    "GGL_STRING",
    "GL_ID_CANNOTSAVE",
    "GL_ID_CHOOSECANDIDATE",
    "GL_ID_INPUTCODE",
    "GL_ID_INPUTRADICAL",
    "GL_ID_INPUTREADING",
    "GL_ID_INPUTSYMBOL",
    "GL_ID_NOCONVERT",
    "GL_ID_NODICTIONARY",
    "GL_ID_NOMODULE",
    "GL_ID_PRIVATE_FIRST",
    "GL_ID_PRIVATE_LAST",
    "GL_ID_READINGCONFLICT",
    "GL_ID_REVERSECONVERSION",
    "GL_ID_TOOMANYSTROKE",
    "GL_ID_TYPINGERROR",
    "GL_ID_UNKNOWN",
    "GL_LEVEL_ERROR",
    "GL_LEVEL_FATAL",
    "GL_LEVEL_INFORMATION",
    "GL_LEVEL_NOGUIDELINE",
    "GL_LEVEL_WARNING",
    "GUIDELINE",
    "IACE_CHILDREN",
    "IACE_DEFAULT",
    "IACE_IGNORENOCONTEXT",
    "IActiveIME",
    "IActiveIME2",
    "IActiveIMMApp",
    "IActiveIMMIME",
    "IActiveIMMMessagePumpOwner",
    "IActiveIMMRegistrar",
    "IEnumInputContext",
    "IEnumRegisterWordA",
    "IEnumRegisterWordW",
    "IFEC_S_ALREADY_DEFAULT",
    "IFEClassFactory",
    "IFECommon",
    "IFED_ACTIVE_DICT",
    "IFED_ATOK10",
    "IFED_ATOK9",
    "IFED_E_INVALID_FORMAT",
    "IFED_E_NOT_FOUND",
    "IFED_E_NOT_SUPPORTED",
    "IFED_E_NOT_USER_DIC",
    "IFED_E_NO_ENTRY",
    "IFED_E_OPEN_FAILED",
    "IFED_E_REGISTER_DISCONNECTED",
    "IFED_E_REGISTER_FAILED",
    "IFED_E_REGISTER_ILLEGAL_POS",
    "IFED_E_REGISTER_IMPROPER_WORD",
    "IFED_E_USER_COMMENT",
    "IFED_E_WRITE_FAILED",
    "IFED_MSIME2_BIN_SYSTEM",
    "IFED_MSIME2_BIN_USER",
    "IFED_MSIME2_TEXT_USER",
    "IFED_MSIME95_BIN_SYSTEM",
    "IFED_MSIME95_BIN_USER",
    "IFED_MSIME95_TEXT_USER",
    "IFED_MSIME97_BIN_SYSTEM",
    "IFED_MSIME97_BIN_USER",
    "IFED_MSIME97_TEXT_USER",
    "IFED_MSIME98_BIN_SYSTEM",
    "IFED_MSIME98_BIN_USER",
    "IFED_MSIME98_SYSTEM_CE",
    "IFED_MSIME98_TEXT_USER",
    "IFED_MSIME_BIN_SYSTEM",
    "IFED_MSIME_BIN_USER",
    "IFED_MSIME_TEXT_USER",
    "IFED_NEC_AI_",
    "IFED_PIME2_BIN_STANDARD_SYSTEM",
    "IFED_PIME2_BIN_SYSTEM",
    "IFED_PIME2_BIN_USER",
    "IFED_POS_ADJECTIVE",
    "IFED_POS_ADJECTIVE_VERB",
    "IFED_POS_ADNOUN",
    "IFED_POS_ADVERB",
    "IFED_POS_AFFIX",
    "IFED_POS_ALL",
    "IFED_POS_AUXILIARY_VERB",
    "IFED_POS_CONJUNCTION",
    "IFED_POS_DEPENDENT",
    "IFED_POS_IDIOMS",
    "IFED_POS_INDEPENDENT",
    "IFED_POS_INFLECTIONALSUFFIX",
    "IFED_POS_INTERJECTION",
    "IFED_POS_NONE",
    "IFED_POS_NOUN",
    "IFED_POS_PARTICLE",
    "IFED_POS_PREFIX",
    "IFED_POS_SUB_VERB",
    "IFED_POS_SUFFIX",
    "IFED_POS_SYMBOLS",
    "IFED_POS_TANKANJI",
    "IFED_POS_VERB",
    "IFED_REG_ALL",
    "IFED_REG_AUTO",
    "IFED_REG_DEL",
    "IFED_REG_GRAMMAR",
    "IFED_REG_HEAD",
    "IFED_REG_NONE",
    "IFED_REG_TAIL",
    "IFED_REG_USER",
    "IFED_REL_ALL",
    "IFED_REL_DE",
    "IFED_REL_FUKU_YOUGEN",
    "IFED_REL_GA",
    "IFED_REL_HE",
    "IFED_REL_IDEOM",
    "IFED_REL_KARA",
    "IFED_REL_KEIDOU1_YOUGEN",
    "IFED_REL_KEIDOU2_YOUGEN",
    "IFED_REL_KEIYOU_TARU_YOUGEN",
    "IFED_REL_KEIYOU_TO_YOUGEN",
    "IFED_REL_KEIYOU_YOUGEN",
    "IFED_REL_MADE",
    "IFED_REL_NI",
    "IFED_REL_NO",
    "IFED_REL_NONE",
    "IFED_REL_RENSOU",
    "IFED_REL_RENTAI_MEI",
    "IFED_REL_TAIGEN",
    "IFED_REL_TO",
    "IFED_REL_UNKNOWN1",
    "IFED_REL_UNKNOWN2",
    "IFED_REL_WO",
    "IFED_REL_YORI",
    "IFED_REL_YOUGEN",
    "IFED_SELECT_ALL",
    "IFED_SELECT_COMMENT",
    "IFED_SELECT_DISPLAY",
    "IFED_SELECT_NONE",
    "IFED_SELECT_POS",
    "IFED_SELECT_READING",
    "IFED_S_COMMENT_CHANGED",
    "IFED_S_EMPTY_DICTIONARY",
    "IFED_S_MORE_ENTRIES",
    "IFED_S_WORD_EXISTS",
    "IFED_TYPE_ALL",
    "IFED_TYPE_ENGLISH",
    "IFED_TYPE_GENERAL",
    "IFED_TYPE_NAMEPLACE",
    "IFED_TYPE_NONE",
    "IFED_TYPE_REVERSE",
    "IFED_TYPE_SPEECH",
    "IFED_UCT_MAX",
    "IFED_UCT_NONE",
    "IFED_UCT_STRING_SJIS",
    "IFED_UCT_STRING_UNICODE",
    "IFED_UCT_USER_DEFINED",
    "IFED_UNKNOWN",
    "IFED_VJE_20",
    "IFED_WX_II",
    "IFED_WX_III",
    "IFEDictionary",
    "IFELanguage",
    "IGIMIF_RIGHTMENU",
    "IGIMII_CMODE",
    "IGIMII_CONFIGURE",
    "IGIMII_HELP",
    "IGIMII_INPUTTOOLS",
    "IGIMII_OTHER",
    "IGIMII_SMODE",
    "IGIMII_TOOLS",
    "IImePad",
    "IImePadApplet",
    "IImePlugInDictDictionaryList",
    "IImeSpecifyApplets",
    "IMCENUMPROC",
    "IMC_CLOSESTATUSWINDOW",
    "IMC_GETCANDIDATEPOS",
    "IMC_GETCOMPOSITIONFONT",
    "IMC_GETCOMPOSITIONWINDOW",
    "IMC_GETSOFTKBDFONT",
    "IMC_GETSOFTKBDPOS",
    "IMC_GETSOFTKBDSUBTYPE",
    "IMC_GETSTATUSWINDOWPOS",
    "IMC_OPENSTATUSWINDOW",
    "IMC_SETCANDIDATEPOS",
    "IMC_SETCOMPOSITIONFONT",
    "IMC_SETCOMPOSITIONWINDOW",
    "IMC_SETCONVERSIONMODE",
    "IMC_SETOPENSTATUS",
    "IMC_SETSENTENCEMODE",
    "IMC_SETSOFTKBDDATA",
    "IMC_SETSOFTKBDFONT",
    "IMC_SETSOFTKBDPOS",
    "IMC_SETSOFTKBDSUBTYPE",
    "IMC_SETSTATUSWINDOWPOS",
    "IMEAPPLETCFG",
    "IMEAPPLETUI",
    "IMECHARINFO",
    "IMECHARPOSITION",
    "IMECOMPOSITIONSTRINGINFO",
    "IMEDLG",
    "IMEDP",
    "IMEFAREASTINFO",
    "IMEFAREASTINFO_TYPE_COMMENT",
    "IMEFAREASTINFO_TYPE_COSTTIME",
    "IMEFAREASTINFO_TYPE_DEFAULT",
    "IMEFAREASTINFO_TYPE_READING",
    "IMEFMT",
    "IMEINFO",
    "IMEITEM",
    "IMEITEMCANDIDATE",
    "IMEKEYCTRLMASK_ALT",
    "IMEKEYCTRLMASK_CTRL",
    "IMEKEYCTRLMASK_SHIFT",
    "IMEKEYCTRL_DOWN",
    "IMEKEYCTRL_UP",
    "IMEKMS",
    "IMEKMSFUNCDESC",
    "IMEKMSINIT",
    "IMEKMSINVK",
    "IMEKMSKEY",
    "IMEKMSKMP",
    "IMEKMSNTFY",
    "IMEKMS_2NDLEVEL",
    "IMEKMS_CANDIDATE",
    "IMEKMS_COMPOSITION",
    "IMEKMS_IMEOFF",
    "IMEKMS_INPTGL",
    "IMEKMS_NOCOMPOSITION",
    "IMEKMS_SELECTION",
    "IMEKMS_TYPECAND",
    "IMEMENUITEMINFOA",
    "IMEMENUITEMINFOW",
    "IMEMENUITEM_STRING_SIZE",
    "IMEMOUSERET_NOTHANDLED",
    "IMEMOUSE_LDOWN",
    "IMEMOUSE_MDOWN",
    "IMEMOUSE_NONE",
    "IMEMOUSE_RDOWN",
    "IMEMOUSE_VERSION",
    "IMEMOUSE_WDOWN",
    "IMEMOUSE_WUP",
    "IMEPADCTRL_CARETBACKSPACE",
    "IMEPADCTRL_CARETBOTTOM",
    "IMEPADCTRL_CARETDELETE",
    "IMEPADCTRL_CARETLEFT",
    "IMEPADCTRL_CARETRIGHT",
    "IMEPADCTRL_CARETSET",
    "IMEPADCTRL_CARETTOP",
    "IMEPADCTRL_CLEARALL",
    "IMEPADCTRL_CONVERTALL",
    "IMEPADCTRL_DETERMINALL",
    "IMEPADCTRL_DETERMINCHAR",
    "IMEPADCTRL_INSERTFULLSPACE",
    "IMEPADCTRL_INSERTHALFSPACE",
    "IMEPADCTRL_INSERTSPACE",
    "IMEPADCTRL_OFFIME",
    "IMEPADCTRL_OFFPRECONVERSION",
    "IMEPADCTRL_ONIME",
    "IMEPADCTRL_ONPRECONVERSION",
    "IMEPADCTRL_PHONETICCANDIDATE",
    "IMEPADCTRL_PHRASEDELETE",
    "IMEPADREQ_CHANGESTRING",
    "IMEPADREQ_CHANGESTRINGCANDIDATEINFO",
    "IMEPADREQ_CHANGESTRINGINFO",
    "IMEPADREQ_DELETESTRING",
    "IMEPADREQ_FIRST",
    "IMEPADREQ_FORCEIMEPADWINDOWSHOW",
    "IMEPADREQ_GETAPPLETDATA",
    "IMEPADREQ_GETAPPLETUISTYLE",
    "IMEPADREQ_GETAPPLHWND",
    "IMEPADREQ_GETCOMPOSITIONSTRING",
    "IMEPADREQ_GETCOMPOSITIONSTRINGID",
    "IMEPADREQ_GETCOMPOSITIONSTRINGINFO",
    "IMEPADREQ_GETCONVERSIONSTATUS",
    "IMEPADREQ_GETCURRENTIMEINFO",
    "IMEPADREQ_GETCURRENTUILANGID",
    "IMEPADREQ_GETDEFAULTUILANGID",
    "IMEPADREQ_GETSELECTEDSTRING",
    "IMEPADREQ_GETVERSION",
    "IMEPADREQ_INSERTITEMCANDIDATE",
    "IMEPADREQ_INSERTSTRING",
    "IMEPADREQ_INSERTSTRINGCANDIDATE",
    "IMEPADREQ_INSERTSTRINGCANDIDATEINFO",
    "IMEPADREQ_INSERTSTRINGINFO",
    "IMEPADREQ_ISAPPLETACTIVE",
    "IMEPADREQ_ISIMEPADWINDOWVISIBLE",
    "IMEPADREQ_POSTMODALNOTIFY",
    "IMEPADREQ_SENDCONTROL",
    "IMEPADREQ_SENDKEYCONTROL",
    "IMEPADREQ_SETAPPLETDATA",
    "IMEPADREQ_SETAPPLETMINMAXSIZE",
    "IMEPADREQ_SETAPPLETSIZE",
    "IMEPADREQ_SETAPPLETUISTYLE",
    "IMEPADREQ_SETTITLEFONT",
    "IMEPN_ACTIVATE",
    "IMEPN_APPLYCAND",
    "IMEPN_APPLYCANDEX",
    "IMEPN_CONFIG",
    "IMEPN_FIRST",
    "IMEPN_HELP",
    "IMEPN_HIDE",
    "IMEPN_INACTIVATE",
    "IMEPN_QUERYCAND",
    "IMEPN_SETTINGCHANGED",
    "IMEPN_SHOW",
    "IMEPN_SIZECHANGED",
    "IMEPN_SIZECHANGING",
    "IMEPN_USER",
    "IMEREG",
    "IMEREL",
    "IMESHF",
    "IMESTRINGCANDIDATE",
    "IMESTRINGCANDIDATEINFO",
    "IMESTRINGINFO",
    "IMEUCT",
    "IMEVER_0310",
    "IMEVER_0400",
    "IMEWRD",
    "IME_CAND_CODE",
    "IME_CAND_MEANING",
    "IME_CAND_RADICAL",
    "IME_CAND_READ",
    "IME_CAND_STROKE",
    "IME_CAND_UNKNOWN",
    "IME_CHOTKEY_IME_NONIME_TOGGLE",
    "IME_CHOTKEY_SHAPE_TOGGLE",
    "IME_CHOTKEY_SYMBOL_TOGGLE",
    "IME_CMODE_ALPHANUMERIC",
    "IME_CMODE_CHARCODE",
    "IME_CMODE_CHINESE",
    "IME_CMODE_EUDC",
    "IME_CMODE_FIXED",
    "IME_CMODE_FULLSHAPE",
    "IME_CMODE_HANGEUL",
    "IME_CMODE_HANGUL",
    "IME_CMODE_HANJACONVERT",
    "IME_CMODE_JAPANESE",
    "IME_CMODE_KATAKANA",
    "IME_CMODE_LANGUAGE",
    "IME_CMODE_NATIVE",
    "IME_CMODE_NATIVESYMBOL",
    "IME_CMODE_NOCONVERSION",
    "IME_CMODE_RESERVED",
    "IME_CMODE_ROMAN",
    "IME_CMODE_SOFTKBD",
    "IME_CMODE_SYMBOL",
    "IME_COMPOSITION_STRING",
    "IME_CONFIG_GENERAL",
    "IME_CONFIG_REGISTERWORD",
    "IME_CONFIG_SELECTDICTIONARY",
    "IME_CONVERSION_MODE",
    "IME_ESCAPE",
    "IME_ESC_AUTOMATA",
    "IME_ESC_GETHELPFILENAME",
    "IME_ESC_GET_EUDC_DICTIONARY",
    "IME_ESC_HANJA_MODE",
    "IME_ESC_IME_NAME",
    "IME_ESC_MAX_KEY",
    "IME_ESC_PRIVATE_FIRST",
    "IME_ESC_PRIVATE_HOTKEY",
    "IME_ESC_PRIVATE_LAST",
    "IME_ESC_QUERY_SUPPORT",
    "IME_ESC_RESERVED_FIRST",
    "IME_ESC_RESERVED_LAST",
    "IME_ESC_SEQUENCE_TO_INTERNAL",
    "IME_ESC_SET_EUDC_DICTIONARY",
    "IME_ESC_STRING_BUFFER_SIZE",
    "IME_ESC_SYNC_HOTKEY",
    "IME_HOTKEY_DSWITCH_FIRST",
    "IME_HOTKEY_DSWITCH_LAST",
    "IME_HOTKEY_IDENTIFIER",
    "IME_HOTKEY_PRIVATE_FIRST",
    "IME_HOTKEY_PRIVATE_LAST",
    "IME_ITHOTKEY_PREVIOUS_COMPOSITION",
    "IME_ITHOTKEY_RECONVERTSTRING",
    "IME_ITHOTKEY_RESEND_RESULTSTR",
    "IME_ITHOTKEY_UISTYLE_TOGGLE",
    "IME_JHOTKEY_CLOSE_OPEN",
    "IME_KHOTKEY_ENGLISH",
    "IME_KHOTKEY_HANJACONVERT",
    "IME_KHOTKEY_SHAPE_TOGGLE",
    "IME_PAD_REQUEST_FLAGS",
    "IME_PROP_ACCEPT_WIDE_VKEY",
    "IME_PROP_AT_CARET",
    "IME_PROP_CANDLIST_START_FROM_1",
    "IME_PROP_COMPLETE_ON_UNSELECT",
    "IME_PROP_END_UNLOAD",
    "IME_PROP_IGNORE_UPKEYS",
    "IME_PROP_KBD_CHAR_FIRST",
    "IME_PROP_NEED_ALTKEY",
    "IME_PROP_NO_KEYS_ON_CLOSE",
    "IME_PROP_SPECIAL_UI",
    "IME_PROP_UNICODE",
    "IME_REGWORD_STYLE_EUDC",
    "IME_REGWORD_STYLE_USER_FIRST",
    "IME_REGWORD_STYLE_USER_LAST",
    "IME_SENTENCE_MODE",
    "IME_SMODE_AUTOMATIC",
    "IME_SMODE_CONVERSATION",
    "IME_SMODE_NONE",
    "IME_SMODE_PHRASEPREDICT",
    "IME_SMODE_PLAURALCLAUSE",
    "IME_SMODE_RESERVED",
    "IME_SMODE_SINGLECONVERT",
    "IME_SYSINFO_WINLOGON",
    "IME_SYSINFO_WOW16",
    "IME_THOTKEY_IME_NONIME_TOGGLE",
    "IME_THOTKEY_SHAPE_TOGGLE",
    "IME_THOTKEY_SYMBOL_TOGGLE",
    "IME_UI_CLASS_NAME_SIZE",
    "IMFT_RADIOCHECK",
    "IMFT_SEPARATOR",
    "IMFT_SUBMENU",
    "IMMGWLP_IMC",
    "IMMGWL_IMC",
    "IMM_ERROR_GENERAL",
    "IMM_ERROR_NODATA",
    "IMN_CHANGECANDIDATE",
    "IMN_CLOSECANDIDATE",
    "IMN_CLOSESTATUSWINDOW",
    "IMN_GUIDELINE",
    "IMN_OPENCANDIDATE",
    "IMN_OPENSTATUSWINDOW",
    "IMN_PRIVATE",
    "IMN_SETCANDIDATEPOS",
    "IMN_SETCOMPOSITIONFONT",
    "IMN_SETCOMPOSITIONWINDOW",
    "IMN_SETCONVERSIONMODE",
    "IMN_SETOPENSTATUS",
    "IMN_SETSENTENCEMODE",
    "IMN_SETSTATUSWINDOWPOS",
    "IMN_SOFTKBDDESTROYED",
    "IMR_CANDIDATEWINDOW",
    "IMR_COMPOSITIONFONT",
    "IMR_COMPOSITIONWINDOW",
    "IMR_CONFIRMRECONVERTSTRING",
    "IMR_DOCUMENTFEED",
    "IMR_QUERYCHARPOSITION",
    "IMR_RECONVERTSTRING",
    "INFOMASK_APPLY_CAND",
    "INFOMASK_APPLY_CAND_EX",
    "INFOMASK_BLOCK_CAND",
    "INFOMASK_HIDE_CAND",
    "INFOMASK_NONE",
    "INFOMASK_QUERY_CAND",
    "INFOMASK_STRING_FIX",
    "INIT_COMPFORM",
    "INIT_CONVERSION",
    "INIT_LOGFONT",
    "INIT_SENTENCE",
    "INIT_SOFTKBDPOS",
    "INIT_STATUSWNDPOS",
    "INPUTCONTEXT",
    "IPACFG_CATEGORY",
    "IPACFG_HELP",
    "IPACFG_LANG",
    "IPACFG_NONE",
    "IPACFG_PROPERTY",
    "IPACFG_TITLE",
    "IPACFG_TITLEFONTFACE",
    "IPACID_CHARLIST",
    "IPACID_EPWING",
    "IPACID_HANDWRITING",
    "IPACID_NONE",
    "IPACID_OCR",
    "IPACID_RADICALSEARCH",
    "IPACID_SOFTKEY",
    "IPACID_STROKESEARCH",
    "IPACID_SYMBOLSEARCH",
    "IPACID_USER",
    "IPACID_VOICE",
    "IPAWS_ENABLED",
    "IPAWS_HORIZONTALFIXED",
    "IPAWS_MAXHEIGHTFIXED",
    "IPAWS_MAXSIZEFIXED",
    "IPAWS_MAXWIDTHFIXED",
    "IPAWS_MINHEIGHTFIXED",
    "IPAWS_MINSIZEFIXED",
    "IPAWS_MINWIDTHFIXED",
    "IPAWS_SIZEFIXED",
    "IPAWS_SIZINGNOTIFY",
    "IPAWS_VERTICALFIXED",
    "ISC_SHOWUIALL",
    "ISC_SHOWUIALLCANDIDATEWINDOW",
    "ISC_SHOWUICANDIDATEWINDOW",
    "ISC_SHOWUICOMPOSITIONWINDOW",
    "ISC_SHOWUIGUIDELINE",
    "ImmAssociateContext",
    "ImmAssociateContextEx",
    "ImmConfigureIMEA",
    "ImmConfigureIMEW",
    "ImmCreateContext",
    "ImmCreateIMCC",
    "ImmCreateSoftKeyboard",
    "ImmDestroyContext",
    "ImmDestroyIMCC",
    "ImmDestroySoftKeyboard",
    "ImmDisableIME",
    "ImmDisableLegacyIME",
    "ImmDisableTextFrameService",
    "ImmEnumInputContext",
    "ImmEnumRegisterWordA",
    "ImmEnumRegisterWordW",
    "ImmEscapeA",
    "ImmEscapeW",
    "ImmGenerateMessage",
    "ImmGetCandidateListA",
    "ImmGetCandidateListCountA",
    "ImmGetCandidateListCountW",
    "ImmGetCandidateListW",
    "ImmGetCandidateWindow",
    "ImmGetCompositionFontA",
    "ImmGetCompositionFontW",
    "ImmGetCompositionStringA",
    "ImmGetCompositionStringW",
    "ImmGetCompositionWindow",
    "ImmGetContext",
    "ImmGetConversionListA",
    "ImmGetConversionListW",
    "ImmGetConversionStatus",
    "ImmGetDefaultIMEWnd",
    "ImmGetDescriptionA",
    "ImmGetDescriptionW",
    "ImmGetGuideLineA",
    "ImmGetGuideLineW",
    "ImmGetHotKey",
    "ImmGetIMCCLockCount",
    "ImmGetIMCCSize",
    "ImmGetIMCLockCount",
    "ImmGetIMEFileNameA",
    "ImmGetIMEFileNameW",
    "ImmGetImeMenuItemsA",
    "ImmGetImeMenuItemsW",
    "ImmGetOpenStatus",
    "ImmGetProperty",
    "ImmGetRegisterWordStyleA",
    "ImmGetRegisterWordStyleW",
    "ImmGetStatusWindowPos",
    "ImmGetVirtualKey",
    "ImmInstallIMEA",
    "ImmInstallIMEW",
    "ImmIsIME",
    "ImmIsUIMessageA",
    "ImmIsUIMessageW",
    "ImmLockIMC",
    "ImmLockIMCC",
    "ImmNotifyIME",
    "ImmReSizeIMCC",
    "ImmRegisterWordA",
    "ImmRegisterWordW",
    "ImmReleaseContext",
    "ImmRequestMessageA",
    "ImmRequestMessageW",
    "ImmSetCandidateWindow",
    "ImmSetCompositionFontA",
    "ImmSetCompositionFontW",
    "ImmSetCompositionStringA",
    "ImmSetCompositionStringW",
    "ImmSetCompositionWindow",
    "ImmSetConversionStatus",
    "ImmSetHotKey",
    "ImmSetOpenStatus",
    "ImmSetStatusWindowPos",
    "ImmShowSoftKeyboard",
    "ImmSimulateHotKey",
    "ImmUnlockIMC",
    "ImmUnlockIMCC",
    "ImmUnregisterWordA",
    "ImmUnregisterWordW",
    "JPOS_1DAN",
    "JPOS_4DAN_HA",
    "JPOS_5DAN_AWA",
    "JPOS_5DAN_AWAUON",
    "JPOS_5DAN_BA",
    "JPOS_5DAN_GA",
    "JPOS_5DAN_KA",
    "JPOS_5DAN_KASOKUON",
    "JPOS_5DAN_MA",
    "JPOS_5DAN_NA",
    "JPOS_5DAN_RA",
    "JPOS_5DAN_RAHEN",
    "JPOS_5DAN_SA",
    "JPOS_5DAN_TA",
    "JPOS_BUPPIN",
    "JPOS_CHIMEI",
    "JPOS_CHIMEI_EKI",
    "JPOS_CHIMEI_GUN",
    "JPOS_CHIMEI_KEN",
    "JPOS_CHIMEI_KU",
    "JPOS_CHIMEI_KUNI",
    "JPOS_CHIMEI_MACHI",
    "JPOS_CHIMEI_MURA",
    "JPOS_CHIMEI_SHI",
    "JPOS_CLOSEBRACE",
    "JPOS_DAIMEISHI",
    "JPOS_DAIMEISHI_NINSHOU",
    "JPOS_DAIMEISHI_SHIJI",
    "JPOS_DOKURITSUGO",
    "JPOS_EIJI",
    "JPOS_FUKUSHI",
    "JPOS_FUKUSHI_DA",
    "JPOS_FUKUSHI_NANO",
    "JPOS_FUKUSHI_NI",
    "JPOS_FUKUSHI_SAHEN",
    "JPOS_FUKUSHI_TO",
    "JPOS_FUKUSHI_TOSURU",
    "JPOS_FUTEIGO",
    "JPOS_HUKUSIMEISHI",
    "JPOS_JINMEI",
    "JPOS_JINMEI_MEI",
    "JPOS_JINMEI_SEI",
    "JPOS_KANDOUSHI",
    "JPOS_KANJI",
    "JPOS_KANYOUKU",
    "JPOS_KAZU",
    "JPOS_KAZU_SURYOU",
    "JPOS_KAZU_SUSHI",
    "JPOS_KEIDOU",
    "JPOS_KEIDOU_GARU",
    "JPOS_KEIDOU_NO",
    "JPOS_KEIDOU_TARU",
    "JPOS_KEIYOU",
    "JPOS_KEIYOU_GARU",
    "JPOS_KEIYOU_GE",
    "JPOS_KEIYOU_ME",
    "JPOS_KEIYOU_U",
    "JPOS_KEIYOU_YUU",
    "JPOS_KENCHIKU",
    "JPOS_KIGOU",
    "JPOS_KURU_KI",
    "JPOS_KURU_KITA",
    "JPOS_KURU_KITARA",
    "JPOS_KURU_KITARI",
    "JPOS_KURU_KITAROU",
    "JPOS_KURU_KITE",
    "JPOS_KURU_KO",
    "JPOS_KURU_KOI",
    "JPOS_KURU_KOYOU",
    "JPOS_KURU_KUREBA",
    "JPOS_KUTEN",
    "JPOS_MEISA_KEIDOU",
    "JPOS_MEISHI_FUTSU",
    "JPOS_MEISHI_KEIYOUDOUSHI",
    "JPOS_MEISHI_SAHEN",
    "JPOS_MEISHI_ZAHEN",
    "JPOS_OPENBRACE",
    "JPOS_RENTAISHI",
    "JPOS_RENTAISHI_SHIJI",
    "JPOS_RENYOU_SETSUBI",
    "JPOS_SETSUBI",
    "JPOS_SETSUBI_CHIMEI",
    "JPOS_SETSUBI_CHOU",
    "JPOS_SETSUBI_CHU",
    "JPOS_SETSUBI_DONO",
    "JPOS_SETSUBI_EKI",
    "JPOS_SETSUBI_FU",
    "JPOS_SETSUBI_FUKUSU",
    "JPOS_SETSUBI_GUN",
    "JPOS_SETSUBI_JIKAN",
    "JPOS_SETSUBI_JIKANPLUS",
    "JPOS_SETSUBI_JINMEI",
    "JPOS_SETSUBI_JOSUSHI",
    "JPOS_SETSUBI_JOSUSHIPLUS",
    "JPOS_SETSUBI_KA",
    "JPOS_SETSUBI_KATA",
    "JPOS_SETSUBI_KEN",
    "JPOS_SETSUBI_KENCHIKU",
    "JPOS_SETSUBI_KU",
    "JPOS_SETSUBI_KUN",
    "JPOS_SETSUBI_KUNI",
    "JPOS_SETSUBI_MACHI",
    "JPOS_SETSUBI_MEISHIRENDAKU",
    "JPOS_SETSUBI_MURA",
    "JPOS_SETSUBI_RA",
    "JPOS_SETSUBI_RYU",
    "JPOS_SETSUBI_SAMA",
    "JPOS_SETSUBI_SAN",
    "JPOS_SETSUBI_SEI",
    "JPOS_SETSUBI_SHAMEI",
    "JPOS_SETSUBI_SHI",
    "JPOS_SETSUBI_SON",
    "JPOS_SETSUBI_SONOTA",
    "JPOS_SETSUBI_SOSHIKI",
    "JPOS_SETSUBI_TACHI",
    "JPOS_SETSUBI_TEINEI",
    "JPOS_SETSUBI_TEKI",
    "JPOS_SETSUBI_YOU",
    "JPOS_SETSUZOKUSHI",
    "JPOS_SETTOU",
    "JPOS_SETTOU_CHIMEI",
    "JPOS_SETTOU_CHOUTAN",
    "JPOS_SETTOU_DAISHOU",
    "JPOS_SETTOU_FUKU",
    "JPOS_SETTOU_JINMEI",
    "JPOS_SETTOU_JOSUSHI",
    "JPOS_SETTOU_KAKU",
    "JPOS_SETTOU_KOUTEI",
    "JPOS_SETTOU_MI",
    "JPOS_SETTOU_SAI",
    "JPOS_SETTOU_SHINKYU",
    "JPOS_SETTOU_SONOTA",
    "JPOS_SETTOU_TEINEI_GO",
    "JPOS_SETTOU_TEINEI_O",
    "JPOS_SETTOU_TEINEI_ON",
    "JPOS_SHAMEI",
    "JPOS_SONOTA",
    "JPOS_SOSHIKI",
    "JPOS_SURU_SA",
    "JPOS_SURU_SE",
    "JPOS_SURU_SEYO",
    "JPOS_SURU_SI",
    "JPOS_SURU_SIATRI",
    "JPOS_SURU_SITA",
    "JPOS_SURU_SITARA",
    "JPOS_SURU_SITAROU",
    "JPOS_SURU_SITE",
    "JPOS_SURU_SIYOU",
    "JPOS_SURU_SUREBA",
    "JPOS_TANKANJI",
    "JPOS_TANKANJI_KAO",
    "JPOS_TANSHUKU",
    "JPOS_TOKUSHU_KAHEN",
    "JPOS_TOKUSHU_NAHEN",
    "JPOS_TOKUSHU_SAHEN",
    "JPOS_TOKUSHU_SAHENSURU",
    "JPOS_TOKUSHU_ZAHEN",
    "JPOS_TOUTEN",
    "JPOS_UNDEFINED",
    "JPOS_YOKUSEI",
    "MAX_APPLETTITLE",
    "MAX_FONTFACE",
    "MODEBIASMODE_DEFAULT",
    "MODEBIASMODE_DIGIT",
    "MODEBIASMODE_FILENAME",
    "MODEBIASMODE_READING",
    "MODEBIAS_GETVALUE",
    "MODEBIAS_GETVERSION",
    "MODEBIAS_SETVALUE",
    "MOD_IGNORE_ALL_MODIFIER",
    "MOD_LEFT",
    "MOD_ON_KEYUP",
    "MOD_RIGHT",
    "MORRSLT",
    "NI_CHANGECANDIDATELIST",
    "NI_CLOSECANDIDATE",
    "NI_COMPOSITIONSTR",
    "NI_CONTEXTUPDATED",
    "NI_FINALIZECONVERSIONRESULT",
    "NI_IMEMENUSELECTED",
    "NI_OPENCANDIDATE",
    "NI_SELECTCANDIDATESTR",
    "NI_SETCANDIDATE_PAGESIZE",
    "NI_SETCANDIDATE_PAGESTART",
    "NOTIFY_IME_ACTION",
    "NOTIFY_IME_INDEX",
    "PFNLOG",
    "POSTBL",
    "POS_UNDEFINED",
    "RECONVERTSTRING",
    "RECONVOPT_NONE",
    "RECONVOPT_USECANCELNOTIFY",
    "REGISTERWORDA",
    "REGISTERWORDENUMPROCA",
    "REGISTERWORDENUMPROCW",
    "REGISTERWORDW",
    "RWM_CHGKEYMAP",
    "RWM_DOCUMENTFEED",
    "RWM_KEYMAP",
    "RWM_MODEBIAS",
    "RWM_MOUSE",
    "RWM_NTFYKEYMAP",
    "RWM_QUERYPOSITION",
    "RWM_RECONVERT",
    "RWM_RECONVERTOPTIONS",
    "RWM_RECONVERTREQUEST",
    "RWM_SERVICE",
    "RWM_SHOWIMEPAD",
    "RWM_UIREADY",
    "SCS_CAP_COMPSTR",
    "SCS_CAP_MAKEREAD",
    "SCS_CAP_SETRECONVERTSTRING",
    "SCS_CHANGEATTR",
    "SCS_CHANGECLAUSE",
    "SCS_QUERYRECONVERTSTRING",
    "SCS_SETRECONVERTSTRING",
    "SCS_SETSTR",
    "SELECT_CAP_CONVERSION",
    "SELECT_CAP_SENTENCE",
    "SET_COMPOSITION_STRING_TYPE",
    "SHOWIMEPAD_CATEGORY",
    "SHOWIMEPAD_DEFAULT",
    "SHOWIMEPAD_GUID",
    "SOFTKBDDATA",
    "SOFTKEYBOARD_TYPE_C1",
    "SOFTKEYBOARD_TYPE_T1",
    "STYLEBUFA",
    "STYLEBUFW",
    "STYLE_DESCRIPTION_SIZE",
    "TRANSMSG",
    "TRANSMSGLIST",
    "UI_CAP_2700",
    "UI_CAP_ROT90",
    "UI_CAP_ROTANY",
    "UI_CAP_SOFTKBD",
    "VERSION_DOCUMENTFEED",
    "VERSION_ID_CHINESE_SIMPLIFIED",
    "VERSION_ID_CHINESE_TRADITIONAL",
    "VERSION_ID_JAPANESE",
    "VERSION_ID_KOREAN",
    "VERSION_MODEBIAS",
    "VERSION_MOUSE_OPERATION",
    "VERSION_QUERYPOSITION",
    "VERSION_RECONVERSION",
    "WDD",
    "cbCommentMax",
    "fpCreateIFECommonInstanceType",
    "fpCreateIFEDictionaryInstanceType",
    "fpCreateIFELanguageInstanceType",
    "szImeChina",
    "szImeJapan",
    "szImeKorea",
    "szImeTaiwan",
    "wchPrivate1",
]
_arch_optional = [
]
