from win32more import *
import win32more.UI.Input.Ime
import win32more.Foundation
import win32more.Globalization
import win32more.Graphics.Gdi
import win32more.System.Com
import win32more.UI.TextServices
import win32more.UI.WindowsAndMessaging

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.UI.Input.Ime, name, eval(f"_define_{name}()"))
    return getattr(win32more.UI.Input.Ime, name)
CLSID_VERSION_DEPENDENT_MSIME_JAPANESE = '6a91029e-aa49-471b-aee7-7d332785660d'
IFEC_S_ALREADY_DEFAULT = 291840
FELANG_REQ_CONV = 65536
FELANG_REQ_RECONV = 131072
FELANG_REQ_REV = 196608
FELANG_CMODE_MONORUBY = 2
FELANG_CMODE_NOPRUNING = 4
FELANG_CMODE_KATAKANAOUT = 8
FELANG_CMODE_HIRAGANAOUT = 0
FELANG_CMODE_HALFWIDTHOUT = 16
FELANG_CMODE_FULLWIDTHOUT = 32
FELANG_CMODE_BOPOMOFO = 64
FELANG_CMODE_HANGUL = 128
FELANG_CMODE_PINYIN = 256
FELANG_CMODE_PRECONV = 512
FELANG_CMODE_RADICAL = 1024
FELANG_CMODE_UNKNOWNREADING = 2048
FELANG_CMODE_MERGECAND = 4096
FELANG_CMODE_ROMAN = 8192
FELANG_CMODE_BESTFIRST = 16384
FELANG_CMODE_USENOREVWORDS = 32768
FELANG_CMODE_NONE = 16777216
FELANG_CMODE_PLAURALCLAUSE = 33554432
FELANG_CMODE_SINGLECONVERT = 67108864
FELANG_CMODE_AUTOMATIC = 134217728
FELANG_CMODE_PHRASEPREDICT = 268435456
FELANG_CMODE_CONVERSATION = 536870912
FELANG_CMODE_NAME = 268435456
FELANG_CMODE_NOINVISIBLECHAR = 1073741824
E_NOCAND = 48
E_NOTENOUGH_BUFFER = 49
E_NOTENOUGH_WDD = 50
E_LARGEINPUT = 51
FELANG_CLMN_WBREAK = 1
FELANG_CLMN_NOWBREAK = 2
FELANG_CLMN_PBREAK = 4
FELANG_CLMN_NOPBREAK = 8
FELANG_CLMN_FIXR = 16
FELANG_CLMN_FIXD = 32
FELANG_INVALD_PO = 65535
IFED_POS_NONE = 0
IFED_POS_NOUN = 1
IFED_POS_VERB = 2
IFED_POS_ADJECTIVE = 4
IFED_POS_ADJECTIVE_VERB = 8
IFED_POS_ADVERB = 16
IFED_POS_ADNOUN = 32
IFED_POS_CONJUNCTION = 64
IFED_POS_INTERJECTION = 128
IFED_POS_INDEPENDENT = 255
IFED_POS_INFLECTIONALSUFFIX = 256
IFED_POS_PREFIX = 512
IFED_POS_SUFFIX = 1024
IFED_POS_AFFIX = 1536
IFED_POS_TANKANJI = 2048
IFED_POS_IDIOMS = 4096
IFED_POS_SYMBOLS = 8192
IFED_POS_PARTICLE = 16384
IFED_POS_AUXILIARY_VERB = 32768
IFED_POS_SUB_VERB = 65536
IFED_POS_DEPENDENT = 114688
IFED_POS_ALL = 131071
IFED_SELECT_NONE = 0
IFED_SELECT_READING = 1
IFED_SELECT_DISPLAY = 2
IFED_SELECT_POS = 4
IFED_SELECT_COMMENT = 8
IFED_SELECT_ALL = 15
IFED_REG_NONE = 0
IFED_REG_USER = 1
IFED_REG_AUTO = 2
IFED_REG_GRAMMAR = 4
IFED_REG_ALL = 7
IFED_TYPE_NONE = 0
IFED_TYPE_GENERAL = 1
IFED_TYPE_NAMEPLACE = 2
IFED_TYPE_SPEECH = 4
IFED_TYPE_REVERSE = 8
IFED_TYPE_ENGLISH = 16
IFED_TYPE_ALL = 31
IFED_S_MORE_ENTRIES = 291328
IFED_S_EMPTY_DICTIONARY = 291329
IFED_S_WORD_EXISTS = 291330
IFED_S_COMMENT_CHANGED = 291331
IFED_E_NOT_FOUND = -2147192064
IFED_E_INVALID_FORMAT = -2147192063
IFED_E_OPEN_FAILED = -2147192062
IFED_E_WRITE_FAILED = -2147192061
IFED_E_NO_ENTRY = -2147192060
IFED_E_REGISTER_FAILED = -2147192059
IFED_E_NOT_USER_DIC = -2147192058
IFED_E_NOT_SUPPORTED = -2147192057
IFED_E_USER_COMMENT = -2147192056
IFED_E_REGISTER_ILLEGAL_POS = -2147192055
IFED_E_REGISTER_IMPROPER_WORD = -2147192054
IFED_E_REGISTER_DISCONNECTED = -2147192053
POS_UNDEFINED = 0
JPOS_UNDEFINED = 0
JPOS_MEISHI_FUTSU = 100
JPOS_MEISHI_SAHEN = 101
JPOS_MEISHI_ZAHEN = 102
JPOS_MEISHI_KEIYOUDOUSHI = 103
JPOS_HUKUSIMEISHI = 104
JPOS_MEISA_KEIDOU = 105
JPOS_JINMEI = 106
JPOS_JINMEI_SEI = 107
JPOS_JINMEI_MEI = 108
JPOS_CHIMEI = 109
JPOS_CHIMEI_KUNI = 110
JPOS_CHIMEI_KEN = 111
JPOS_CHIMEI_GUN = 112
JPOS_CHIMEI_KU = 113
JPOS_CHIMEI_SHI = 114
JPOS_CHIMEI_MACHI = 115
JPOS_CHIMEI_MURA = 116
JPOS_CHIMEI_EKI = 117
JPOS_SONOTA = 118
JPOS_SHAMEI = 119
JPOS_SOSHIKI = 120
JPOS_KENCHIKU = 121
JPOS_BUPPIN = 122
JPOS_DAIMEISHI = 123
JPOS_DAIMEISHI_NINSHOU = 124
JPOS_DAIMEISHI_SHIJI = 125
JPOS_KAZU = 126
JPOS_KAZU_SURYOU = 127
JPOS_KAZU_SUSHI = 128
JPOS_5DAN_AWA = 200
JPOS_5DAN_KA = 201
JPOS_5DAN_GA = 202
JPOS_5DAN_SA = 203
JPOS_5DAN_TA = 204
JPOS_5DAN_NA = 205
JPOS_5DAN_BA = 206
JPOS_5DAN_MA = 207
JPOS_5DAN_RA = 208
JPOS_5DAN_AWAUON = 209
JPOS_5DAN_KASOKUON = 210
JPOS_5DAN_RAHEN = 211
JPOS_4DAN_HA = 212
JPOS_1DAN = 213
JPOS_TOKUSHU_KAHEN = 214
JPOS_TOKUSHU_SAHENSURU = 215
JPOS_TOKUSHU_SAHEN = 216
JPOS_TOKUSHU_ZAHEN = 217
JPOS_TOKUSHU_NAHEN = 218
JPOS_KURU_KI = 219
JPOS_KURU_KITA = 220
JPOS_KURU_KITARA = 221
JPOS_KURU_KITARI = 222
JPOS_KURU_KITAROU = 223
JPOS_KURU_KITE = 224
JPOS_KURU_KUREBA = 225
JPOS_KURU_KO = 226
JPOS_KURU_KOI = 227
JPOS_KURU_KOYOU = 228
JPOS_SURU_SA = 229
JPOS_SURU_SI = 230
JPOS_SURU_SITA = 231
JPOS_SURU_SITARA = 232
JPOS_SURU_SIATRI = 233
JPOS_SURU_SITAROU = 234
JPOS_SURU_SITE = 235
JPOS_SURU_SIYOU = 236
JPOS_SURU_SUREBA = 237
JPOS_SURU_SE = 238
JPOS_SURU_SEYO = 239
JPOS_KEIYOU = 300
JPOS_KEIYOU_GARU = 301
JPOS_KEIYOU_GE = 302
JPOS_KEIYOU_ME = 303
JPOS_KEIYOU_YUU = 304
JPOS_KEIYOU_U = 305
JPOS_KEIDOU = 400
JPOS_KEIDOU_NO = 401
JPOS_KEIDOU_TARU = 402
JPOS_KEIDOU_GARU = 403
JPOS_FUKUSHI = 500
JPOS_FUKUSHI_SAHEN = 501
JPOS_FUKUSHI_NI = 502
JPOS_FUKUSHI_NANO = 503
JPOS_FUKUSHI_DA = 504
JPOS_FUKUSHI_TO = 505
JPOS_FUKUSHI_TOSURU = 506
JPOS_RENTAISHI = 600
JPOS_RENTAISHI_SHIJI = 601
JPOS_SETSUZOKUSHI = 650
JPOS_KANDOUSHI = 670
JPOS_SETTOU = 700
JPOS_SETTOU_KAKU = 701
JPOS_SETTOU_SAI = 702
JPOS_SETTOU_FUKU = 703
JPOS_SETTOU_MI = 704
JPOS_SETTOU_DAISHOU = 705
JPOS_SETTOU_KOUTEI = 706
JPOS_SETTOU_CHOUTAN = 707
JPOS_SETTOU_SHINKYU = 708
JPOS_SETTOU_JINMEI = 709
JPOS_SETTOU_CHIMEI = 710
JPOS_SETTOU_SONOTA = 711
JPOS_SETTOU_JOSUSHI = 712
JPOS_SETTOU_TEINEI_O = 713
JPOS_SETTOU_TEINEI_GO = 714
JPOS_SETTOU_TEINEI_ON = 715
JPOS_SETSUBI = 800
JPOS_SETSUBI_TEKI = 801
JPOS_SETSUBI_SEI = 802
JPOS_SETSUBI_KA = 803
JPOS_SETSUBI_CHU = 804
JPOS_SETSUBI_FU = 805
JPOS_SETSUBI_RYU = 806
JPOS_SETSUBI_YOU = 807
JPOS_SETSUBI_KATA = 808
JPOS_SETSUBI_MEISHIRENDAKU = 809
JPOS_SETSUBI_JINMEI = 810
JPOS_SETSUBI_CHIMEI = 811
JPOS_SETSUBI_KUNI = 812
JPOS_SETSUBI_KEN = 813
JPOS_SETSUBI_GUN = 814
JPOS_SETSUBI_KU = 815
JPOS_SETSUBI_SHI = 816
JPOS_SETSUBI_MACHI = 817
JPOS_SETSUBI_CHOU = 818
JPOS_SETSUBI_MURA = 819
JPOS_SETSUBI_SON = 820
JPOS_SETSUBI_EKI = 821
JPOS_SETSUBI_SONOTA = 822
JPOS_SETSUBI_SHAMEI = 823
JPOS_SETSUBI_SOSHIKI = 824
JPOS_SETSUBI_KENCHIKU = 825
JPOS_RENYOU_SETSUBI = 826
JPOS_SETSUBI_JOSUSHI = 827
JPOS_SETSUBI_JOSUSHIPLUS = 828
JPOS_SETSUBI_JIKAN = 829
JPOS_SETSUBI_JIKANPLUS = 830
JPOS_SETSUBI_TEINEI = 831
JPOS_SETSUBI_SAN = 832
JPOS_SETSUBI_KUN = 833
JPOS_SETSUBI_SAMA = 834
JPOS_SETSUBI_DONO = 835
JPOS_SETSUBI_FUKUSU = 836
JPOS_SETSUBI_TACHI = 837
JPOS_SETSUBI_RA = 838
JPOS_TANKANJI = 900
JPOS_TANKANJI_KAO = 901
JPOS_KANYOUKU = 902
JPOS_DOKURITSUGO = 903
JPOS_FUTEIGO = 904
JPOS_KIGOU = 905
JPOS_EIJI = 906
JPOS_KUTEN = 907
JPOS_TOUTEN = 908
JPOS_KANJI = 909
JPOS_OPENBRACE = 910
JPOS_CLOSEBRACE = 911
JPOS_YOKUSEI = 912
JPOS_TANSHUKU = 913
VERSION_ID_JAPANESE = 16777216
VERSION_ID_KOREAN = 33554432
VERSION_ID_CHINESE_TRADITIONAL = 67108864
VERSION_ID_CHINESE_SIMPLIFIED = 134217728
FID_MSIME_VERSION = 0
VERSION_MOUSE_OPERATION = 1
IMEMOUSERET_NOTHANDLED = -1
IMEMOUSE_VERSION = 255
IMEMOUSE_NONE = 0
IMEMOUSE_LDOWN = 1
IMEMOUSE_RDOWN = 2
IMEMOUSE_MDOWN = 4
IMEMOUSE_WUP = 16
IMEMOUSE_WDOWN = 32
FID_RECONVERT_VERSION = 268435456
VERSION_RECONVERSION = 1
VERSION_DOCUMENTFEED = 1
VERSION_QUERYPOSITION = 1
VERSION_MODEBIAS = 1
MODEBIAS_GETVERSION = 0
MODEBIAS_SETVALUE = 1
MODEBIAS_GETVALUE = 2
MODEBIASMODE_DEFAULT = 0
MODEBIASMODE_FILENAME = 1
MODEBIASMODE_READING = 2
MODEBIASMODE_DIGIT = 4
SHOWIMEPAD_DEFAULT = 0
SHOWIMEPAD_CATEGORY = 1
SHOWIMEPAD_GUID = 2
FID_MSIME_KMS_VERSION = 1
FID_MSIME_KMS_INIT = 2
FID_MSIME_KMS_TERM = 3
FID_MSIME_KMS_DEL_KEYLIST = 4
FID_MSIME_KMS_NOTIFY = 5
FID_MSIME_KMS_GETMAP = 6
FID_MSIME_KMS_INVOKE = 7
FID_MSIME_KMS_SETMAP = 8
FID_MSIME_KMS_FUNCDESC = 9
FID_MSIME_KMS_GETMAPSEAMLESS = 10
FID_MSIME_KMS_GETMAPFAST = 11
IMEKMS_NOCOMPOSITION = 0
IMEKMS_COMPOSITION = 1
IMEKMS_SELECTION = 2
IMEKMS_IMEOFF = 3
IMEKMS_2NDLEVEL = 4
IMEKMS_INPTGL = 5
IMEKMS_CANDIDATE = 6
IMEKMS_TYPECAND = 7
RECONVOPT_NONE = 0
RECONVOPT_USECANCELNOTIFY = 1
GCSEX_CANCELRECONVERT = 268435456
STYLE_DESCRIPTION_SIZE = 32
IMEMENUITEM_STRING_SIZE = 80
IMC_GETCANDIDATEPOS = 7
IMC_SETCANDIDATEPOS = 8
IMC_GETCOMPOSITIONFONT = 9
IMC_SETCOMPOSITIONFONT = 10
IMC_GETCOMPOSITIONWINDOW = 11
IMC_SETCOMPOSITIONWINDOW = 12
IMC_GETSTATUSWINDOWPOS = 15
IMC_SETSTATUSWINDOWPOS = 16
IMC_CLOSESTATUSWINDOW = 33
IMC_OPENSTATUSWINDOW = 34
NI_FINALIZECONVERSIONRESULT = 20
ISC_SHOWUICANDIDATEWINDOW = 1
ISC_SHOWUICOMPOSITIONWINDOW = 2147483648
ISC_SHOWUIGUIDELINE = 1073741824
ISC_SHOWUIALLCANDIDATEWINDOW = 15
ISC_SHOWUIALL = 3221225487
MOD_LEFT = 32768
MOD_RIGHT = 16384
MOD_ON_KEYUP = 2048
MOD_IGNORE_ALL_MODIFIER = 1024
IME_CHOTKEY_IME_NONIME_TOGGLE = 16
IME_CHOTKEY_SHAPE_TOGGLE = 17
IME_CHOTKEY_SYMBOL_TOGGLE = 18
IME_JHOTKEY_CLOSE_OPEN = 48
IME_KHOTKEY_SHAPE_TOGGLE = 80
IME_KHOTKEY_HANJACONVERT = 81
IME_KHOTKEY_ENGLISH = 82
IME_THOTKEY_IME_NONIME_TOGGLE = 112
IME_THOTKEY_SHAPE_TOGGLE = 113
IME_THOTKEY_SYMBOL_TOGGLE = 114
IME_HOTKEY_DSWITCH_FIRST = 256
IME_HOTKEY_DSWITCH_LAST = 287
IME_HOTKEY_PRIVATE_FIRST = 512
IME_ITHOTKEY_RESEND_RESULTSTR = 512
IME_ITHOTKEY_PREVIOUS_COMPOSITION = 513
IME_ITHOTKEY_UISTYLE_TOGGLE = 514
IME_ITHOTKEY_RECONVERTSTRING = 515
IME_HOTKEY_PRIVATE_LAST = 543
GCS_COMPREADSTR = 1
GCS_COMPREADATTR = 2
GCS_COMPREADCLAUSE = 4
GCS_COMPSTR = 8
GCS_COMPATTR = 16
GCS_COMPCLAUSE = 32
GCS_CURSORPOS = 128
GCS_DELTASTART = 256
GCS_RESULTREADSTR = 512
GCS_RESULTREADCLAUSE = 1024
GCS_RESULTSTR = 2048
GCS_RESULTCLAUSE = 4096
CS_INSERTCHAR = 8192
CS_NOMOVECARET = 16384
IMEVER_0310 = 196618
IMEVER_0400 = 262144
IME_PROP_AT_CARET = 65536
IME_PROP_SPECIAL_UI = 131072
IME_PROP_CANDLIST_START_FROM_1 = 262144
IME_PROP_UNICODE = 524288
IME_PROP_COMPLETE_ON_UNSELECT = 1048576
UI_CAP_2700 = 1
UI_CAP_ROT90 = 2
UI_CAP_ROTANY = 4
SCS_CAP_COMPSTR = 1
SCS_CAP_MAKEREAD = 2
SCS_CAP_SETRECONVERTSTRING = 4
SELECT_CAP_CONVERSION = 1
SELECT_CAP_SENTENCE = 2
GL_LEVEL_NOGUIDELINE = 0
GL_LEVEL_FATAL = 1
GL_LEVEL_ERROR = 2
GL_LEVEL_WARNING = 3
GL_LEVEL_INFORMATION = 4
GL_ID_UNKNOWN = 0
GL_ID_NOMODULE = 1
GL_ID_NODICTIONARY = 16
GL_ID_CANNOTSAVE = 17
GL_ID_NOCONVERT = 32
GL_ID_TYPINGERROR = 33
GL_ID_TOOMANYSTROKE = 34
GL_ID_READINGCONFLICT = 35
GL_ID_INPUTREADING = 36
GL_ID_INPUTRADICAL = 37
GL_ID_INPUTCODE = 38
GL_ID_INPUTSYMBOL = 39
GL_ID_CHOOSECANDIDATE = 40
GL_ID_REVERSECONVERSION = 41
GL_ID_PRIVATE_FIRST = 32768
GL_ID_PRIVATE_LAST = 65535
ATTR_INPUT = 0
ATTR_TARGET_CONVERTED = 1
ATTR_CONVERTED = 2
ATTR_TARGET_NOTCONVERTED = 3
ATTR_INPUT_ERROR = 4
ATTR_FIXEDCONVERTED = 5
CFS_DEFAULT = 0
CFS_RECT = 1
CFS_POINT = 2
CFS_FORCE_POSITION = 32
CFS_CANDIDATEPOS = 64
CFS_EXCLUDE = 128
IME_CMODE_SOFTKBD = 128
IME_CMODE_NOCONVERSION = 256
IME_CMODE_EUDC = 512
IME_CMODE_SYMBOL = 1024
IME_CMODE_FIXED = 2048
IME_CMODE_RESERVED = 4026531840
IME_SMODE_NONE = 0
IME_SMODE_PLAURALCLAUSE = 1
IME_SMODE_SINGLECONVERT = 2
IME_SMODE_AUTOMATIC = 4
IME_SMODE_PHRASEPREDICT = 8
IME_SMODE_CONVERSATION = 16
IME_SMODE_RESERVED = 61440
IME_CAND_UNKNOWN = 0
IME_CAND_READ = 1
IME_CAND_CODE = 2
IME_CAND_MEANING = 3
IME_CAND_RADICAL = 4
IME_CAND_STROKE = 5
IMN_CLOSESTATUSWINDOW = 1
IMN_OPENSTATUSWINDOW = 2
IMN_CHANGECANDIDATE = 3
IMN_CLOSECANDIDATE = 4
IMN_OPENCANDIDATE = 5
IMN_SETCONVERSIONMODE = 6
IMN_SETSENTENCEMODE = 7
IMN_SETOPENSTATUS = 8
IMN_SETCANDIDATEPOS = 9
IMN_SETCOMPOSITIONFONT = 10
IMN_SETCOMPOSITIONWINDOW = 11
IMN_SETSTATUSWINDOWPOS = 12
IMN_GUIDELINE = 13
IMN_PRIVATE = 14
IMR_COMPOSITIONWINDOW = 1
IMR_CANDIDATEWINDOW = 2
IMR_COMPOSITIONFONT = 3
IMR_RECONVERTSTRING = 4
IMR_CONFIRMRECONVERTSTRING = 5
IMR_QUERYCHARPOSITION = 6
IMR_DOCUMENTFEED = 7
IMM_ERROR_NODATA = -1
IMM_ERROR_GENERAL = -2
IME_CONFIG_GENERAL = 1
IME_CONFIG_REGISTERWORD = 2
IME_CONFIG_SELECTDICTIONARY = 3
IME_ESC_QUERY_SUPPORT = 3
IME_ESC_RESERVED_FIRST = 4
IME_ESC_RESERVED_LAST = 2047
IME_ESC_PRIVATE_FIRST = 2048
IME_ESC_PRIVATE_LAST = 4095
IME_ESC_SEQUENCE_TO_INTERNAL = 4097
IME_ESC_GET_EUDC_DICTIONARY = 4099
IME_ESC_SET_EUDC_DICTIONARY = 4100
IME_ESC_MAX_KEY = 4101
IME_ESC_IME_NAME = 4102
IME_ESC_SYNC_HOTKEY = 4103
IME_ESC_HANJA_MODE = 4104
IME_ESC_AUTOMATA = 4105
IME_ESC_PRIVATE_HOTKEY = 4106
IME_ESC_GETHELPFILENAME = 4107
IME_REGWORD_STYLE_EUDC = 1
IME_REGWORD_STYLE_USER_FIRST = 2147483648
IME_REGWORD_STYLE_USER_LAST = 4294967295
IACE_CHILDREN = 1
IACE_DEFAULT = 16
IACE_IGNORENOCONTEXT = 32
IGIMIF_RIGHTMENU = 1
IGIMII_CMODE = 1
IGIMII_SMODE = 2
IGIMII_CONFIGURE = 4
IGIMII_TOOLS = 8
IGIMII_HELP = 16
IGIMII_OTHER = 32
IGIMII_INPUTTOOLS = 64
IMFT_RADIOCHECK = 1
IMFT_SEPARATOR = 2
IMFT_SUBMENU = 4
SOFTKEYBOARD_TYPE_T1 = 1
SOFTKEYBOARD_TYPE_C1 = 2
IMMGWL_IMC = 0
IMMGWLP_IMC = 0
IMC_SETCONVERSIONMODE = 2
IMC_SETSENTENCEMODE = 4
IMC_SETOPENSTATUS = 6
IMC_GETSOFTKBDFONT = 17
IMC_SETSOFTKBDFONT = 18
IMC_GETSOFTKBDPOS = 19
IMC_SETSOFTKBDPOS = 20
IMC_GETSOFTKBDSUBTYPE = 21
IMC_SETSOFTKBDSUBTYPE = 22
IMC_SETSOFTKBDDATA = 24
NI_CONTEXTUPDATED = 3
IME_SYSINFO_WINLOGON = 1
IME_SYSINFO_WOW16 = 2
INIT_STATUSWNDPOS = 1
INIT_CONVERSION = 2
INIT_SENTENCE = 4
INIT_LOGFONT = 8
INIT_COMPFORM = 16
INIT_SOFTKBDPOS = 32
IME_PROP_END_UNLOAD = 1
IME_PROP_KBD_CHAR_FIRST = 2
IME_PROP_IGNORE_UPKEYS = 4
IME_PROP_NEED_ALTKEY = 8
IME_PROP_NO_KEYS_ON_CLOSE = 16
IME_PROP_ACCEPT_WIDE_VKEY = 32
UI_CAP_SOFTKBD = 65536
IMN_SOFTKBDDESTROYED = 17
IME_UI_CLASS_NAME_SIZE = 16
IME_ESC_STRING_BUFFER_SIZE = 80
CATID_MSIME_IImePadApplet_VER7 = '4a0f8e31-c3ee-11d1-afef-00805f0c8b6d'
CATID_MSIME_IImePadApplet_VER80 = '56f7a792-fef1-11d3-8463-00c04f7a06e5'
CATID_MSIME_IImePadApplet_VER81 = '656520b0-bb88-11d4-84c0-00c04f7a06e5'
CATID_MSIME_IImePadApplet900 = 'faae51bf-5e5b-4a1d-8de1-17c1d9e1728d'
CATID_MSIME_IImePadApplet1000 = 'e081e1d6-2389-43cb-b66f-609f823d9f9c'
CATID_MSIME_IImePadApplet1200 = 'a47fb5fc-7d15-4223-a789-b781bf9ae667'
CATID_MSIME_IImePadApplet = '7566cad1-4ec9-4478-9fe9-8ed766619edf'
FEID_NONE = 0
FEID_CHINESE_TRADITIONAL = 1
FEID_CHINESE_SIMPLIFIED = 2
FEID_CHINESE_HONGKONG = 3
FEID_CHINESE_SINGAPORE = 4
FEID_JAPANESE = 5
FEID_KOREAN = 6
FEID_KOREAN_JOHAB = 7
INFOMASK_NONE = 0
INFOMASK_QUERY_CAND = 1
INFOMASK_APPLY_CAND = 2
INFOMASK_APPLY_CAND_EX = 4
INFOMASK_STRING_FIX = 65536
INFOMASK_HIDE_CAND = 131072
INFOMASK_BLOCK_CAND = 262144
IMEFAREASTINFO_TYPE_DEFAULT = 0
IMEFAREASTINFO_TYPE_READING = 1
IMEFAREASTINFO_TYPE_COMMENT = 2
IMEFAREASTINFO_TYPE_COSTTIME = 3
CHARINFO_APPLETID_MASK = 4278190080
CHARINFO_FEID_MASK = 15728640
CHARINFO_CHARID_MASK = 65535
MAX_APPLETTITLE = 64
MAX_FONTFACE = 32
IPACFG_NONE = 0
IPACFG_PROPERTY = 1
IPACFG_HELP = 2
IPACFG_TITLE = 65536
IPACFG_TITLEFONTFACE = 131072
IPACFG_CATEGORY = 262144
IPACFG_LANG = 16
IPACID_NONE = 0
IPACID_SOFTKEY = 1
IPACID_HANDWRITING = 2
IPACID_STROKESEARCH = 3
IPACID_RADICALSEARCH = 4
IPACID_SYMBOLSEARCH = 5
IPACID_VOICE = 6
IPACID_EPWING = 7
IPACID_OCR = 8
IPACID_CHARLIST = 9
IPACID_USER = 256
IMEPADREQ_FIRST = 4096
IMEPADREQ_INSERTSTRINGCANDIDATE = 4098
IMEPADREQ_INSERTITEMCANDIDATE = 4099
IMEPADREQ_SENDKEYCONTROL = 4101
IMEPADREQ_GETSELECTEDSTRING = 4103
IMEPADREQ_SETAPPLETDATA = 4105
IMEPADREQ_GETAPPLETDATA = 4106
IMEPADREQ_SETTITLEFONT = 4107
IMEPADREQ_GETCOMPOSITIONSTRINGID = 4109
IMEPADREQ_INSERTSTRINGCANDIDATEINFO = 4110
IMEPADREQ_CHANGESTRINGCANDIDATEINFO = 4111
IMEPADREQ_INSERTSTRINGINFO = 4114
IMEPADREQ_CHANGESTRINGINFO = 4115
IMEPADREQ_GETCURRENTUILANGID = 4120
IMEPADCTRL_CONVERTALL = 1
IMEPADCTRL_DETERMINALL = 2
IMEPADCTRL_DETERMINCHAR = 3
IMEPADCTRL_CLEARALL = 4
IMEPADCTRL_CARETSET = 5
IMEPADCTRL_CARETLEFT = 6
IMEPADCTRL_CARETRIGHT = 7
IMEPADCTRL_CARETTOP = 8
IMEPADCTRL_CARETBOTTOM = 9
IMEPADCTRL_CARETBACKSPACE = 10
IMEPADCTRL_CARETDELETE = 11
IMEPADCTRL_PHRASEDELETE = 12
IMEPADCTRL_INSERTSPACE = 13
IMEPADCTRL_INSERTFULLSPACE = 14
IMEPADCTRL_INSERTHALFSPACE = 15
IMEPADCTRL_ONIME = 16
IMEPADCTRL_OFFIME = 17
IMEPADCTRL_ONPRECONVERSION = 18
IMEPADCTRL_OFFPRECONVERSION = 19
IMEPADCTRL_PHONETICCANDIDATE = 20
IMEKEYCTRLMASK_ALT = 1
IMEKEYCTRLMASK_CTRL = 2
IMEKEYCTRLMASK_SHIFT = 4
IMEKEYCTRL_UP = 1
IMEKEYCTRL_DOWN = 0
IMEPN_FIRST = 256
IMEPN_ACTIVATE = 257
IMEPN_INACTIVATE = 258
IMEPN_SHOW = 260
IMEPN_HIDE = 261
IMEPN_SIZECHANGING = 262
IMEPN_SIZECHANGED = 263
IMEPN_CONFIG = 264
IMEPN_HELP = 265
IMEPN_QUERYCAND = 266
IMEPN_APPLYCAND = 267
IMEPN_APPLYCANDEX = 268
IMEPN_SETTINGCHANGED = 269
IMEPN_USER = 356
IPAWS_ENABLED = 1
IPAWS_SIZINGNOTIFY = 4
IPAWS_VERTICALFIXED = 256
IPAWS_HORIZONTALFIXED = 512
IPAWS_SIZEFIXED = 768
IPAWS_MAXWIDTHFIXED = 4096
IPAWS_MAXHEIGHTFIXED = 8192
IPAWS_MAXSIZEFIXED = 12288
IPAWS_MINWIDTHFIXED = 65536
IPAWS_MINHEIGHTFIXED = 131072
IPAWS_MINSIZEFIXED = 196608
CLSID_ImePlugInDictDictionaryList_CHS = '7bf0129b-5bef-4de4-9b0b-5edb66ac2fa6'
CLSID_ImePlugInDictDictionaryList_JPN = '4fe2776b-b0f9-4396-b5fc-e9d4cf1ec195'
SET_COMPOSITION_STRING_TYPE = UInt32
SCS_SETSTR = 9
SCS_CHANGEATTR = 18
SCS_CHANGECLAUSE = 36
SCS_SETRECONVERTSTRING = 65536
SCS_QUERYRECONVERTSTRING = 131072
GET_GUIDE_LINE_TYPE = UInt32
GGL_LEVEL = 1
GGL_INDEX = 2
GGL_STRING = 3
GGL_PRIVATE = 4
NOTIFY_IME_INDEX = UInt32
CPS_CANCEL = 4
CPS_COMPLETE = 1
CPS_CONVERT = 2
CPS_REVERT = 3
NOTIFY_IME_ACTION = UInt32
NI_CHANGECANDIDATELIST = 19
NI_CLOSECANDIDATE = 17
NI_COMPOSITIONSTR = 21
NI_IMEMENUSELECTED = 24
NI_OPENCANDIDATE = 16
NI_SELECTCANDIDATESTR = 18
NI_SETCANDIDATE_PAGESIZE = 23
NI_SETCANDIDATE_PAGESTART = 22
GET_CONVERSION_LIST_FLAG = UInt32
GCL_CONVERSION = 1
GCL_REVERSECONVERSION = 2
GCL_REVERSE_LENGTH = 3
IME_PAD_REQUEST_FLAGS = UInt32
IMEPADREQ_INSERTSTRING = 4097
IMEPADREQ_SENDCONTROL = 4100
IMEPADREQ_SETAPPLETSIZE = 4104
IMEPADREQ_GETCOMPOSITIONSTRING = 4102
IMEPADREQ_GETCOMPOSITIONSTRINGINFO = 4108
IMEPADREQ_DELETESTRING = 4112
IMEPADREQ_CHANGESTRING = 4113
IMEPADREQ_GETAPPLHWND = 4116
IMEPADREQ_FORCEIMEPADWINDOWSHOW = 4117
IMEPADREQ_POSTMODALNOTIFY = 4118
IMEPADREQ_GETDEFAULTUILANGID = 4119
IMEPADREQ_GETAPPLETUISTYLE = 4121
IMEPADREQ_SETAPPLETUISTYLE = 4122
IMEPADREQ_ISAPPLETACTIVE = 4123
IMEPADREQ_ISIMEPADWINDOWVISIBLE = 4124
IMEPADREQ_SETAPPLETMINMAXSIZE = 4125
IMEPADREQ_GETCONVERSIONSTATUS = 4126
IMEPADREQ_GETVERSION = 4127
IMEPADREQ_GETCURRENTIMEINFO = 4128
def _define_COMPOSITIONFORM_head():
    class COMPOSITIONFORM(Structure):
        pass
    return COMPOSITIONFORM
def _define_COMPOSITIONFORM():
    COMPOSITIONFORM = win32more.UI.Input.Ime.COMPOSITIONFORM_head
    COMPOSITIONFORM._fields_ = [
        ("dwStyle", UInt32),
        ("ptCurrentPos", win32more.Foundation.POINT),
        ("rcArea", win32more.Foundation.RECT),
    ]
    return COMPOSITIONFORM
def _define_CANDIDATEFORM_head():
    class CANDIDATEFORM(Structure):
        pass
    return CANDIDATEFORM
def _define_CANDIDATEFORM():
    CANDIDATEFORM = win32more.UI.Input.Ime.CANDIDATEFORM_head
    CANDIDATEFORM._fields_ = [
        ("dwIndex", UInt32),
        ("dwStyle", UInt32),
        ("ptCurrentPos", win32more.Foundation.POINT),
        ("rcArea", win32more.Foundation.RECT),
    ]
    return CANDIDATEFORM
def _define_CANDIDATELIST_head():
    class CANDIDATELIST(Structure):
        pass
    return CANDIDATELIST
def _define_CANDIDATELIST():
    CANDIDATELIST = win32more.UI.Input.Ime.CANDIDATELIST_head
    CANDIDATELIST._fields_ = [
        ("dwSize", UInt32),
        ("dwStyle", UInt32),
        ("dwCount", UInt32),
        ("dwSelection", UInt32),
        ("dwPageStart", UInt32),
        ("dwPageSize", UInt32),
        ("dwOffset", UInt32 * 0),
    ]
    return CANDIDATELIST
def _define_REGISTERWORDA_head():
    class REGISTERWORDA(Structure):
        pass
    return REGISTERWORDA
def _define_REGISTERWORDA():
    REGISTERWORDA = win32more.UI.Input.Ime.REGISTERWORDA_head
    REGISTERWORDA._fields_ = [
        ("lpReading", win32more.Foundation.PSTR),
        ("lpWord", win32more.Foundation.PSTR),
    ]
    return REGISTERWORDA
def _define_REGISTERWORDW_head():
    class REGISTERWORDW(Structure):
        pass
    return REGISTERWORDW
def _define_REGISTERWORDW():
    REGISTERWORDW = win32more.UI.Input.Ime.REGISTERWORDW_head
    REGISTERWORDW._fields_ = [
        ("lpReading", win32more.Foundation.PWSTR),
        ("lpWord", win32more.Foundation.PWSTR),
    ]
    return REGISTERWORDW
def _define_RECONVERTSTRING_head():
    class RECONVERTSTRING(Structure):
        pass
    return RECONVERTSTRING
def _define_RECONVERTSTRING():
    RECONVERTSTRING = win32more.UI.Input.Ime.RECONVERTSTRING_head
    RECONVERTSTRING._fields_ = [
        ("dwSize", UInt32),
        ("dwVersion", UInt32),
        ("dwStrLen", UInt32),
        ("dwStrOffset", UInt32),
        ("dwCompStrLen", UInt32),
        ("dwCompStrOffset", UInt32),
        ("dwTargetStrLen", UInt32),
        ("dwTargetStrOffset", UInt32),
    ]
    return RECONVERTSTRING
def _define_STYLEBUFA_head():
    class STYLEBUFA(Structure):
        pass
    return STYLEBUFA
def _define_STYLEBUFA():
    STYLEBUFA = win32more.UI.Input.Ime.STYLEBUFA_head
    STYLEBUFA._fields_ = [
        ("dwStyle", UInt32),
        ("szDescription", win32more.Foundation.CHAR * 32),
    ]
    return STYLEBUFA
def _define_STYLEBUFW_head():
    class STYLEBUFW(Structure):
        pass
    return STYLEBUFW
def _define_STYLEBUFW():
    STYLEBUFW = win32more.UI.Input.Ime.STYLEBUFW_head
    STYLEBUFW._fields_ = [
        ("dwStyle", UInt32),
        ("szDescription", Char * 32),
    ]
    return STYLEBUFW
def _define_IMEMENUITEMINFOA_head():
    class IMEMENUITEMINFOA(Structure):
        pass
    return IMEMENUITEMINFOA
def _define_IMEMENUITEMINFOA():
    IMEMENUITEMINFOA = win32more.UI.Input.Ime.IMEMENUITEMINFOA_head
    IMEMENUITEMINFOA._fields_ = [
        ("cbSize", UInt32),
        ("fType", UInt32),
        ("fState", UInt32),
        ("wID", UInt32),
        ("hbmpChecked", win32more.Graphics.Gdi.HBITMAP),
        ("hbmpUnchecked", win32more.Graphics.Gdi.HBITMAP),
        ("dwItemData", UInt32),
        ("szString", win32more.Foundation.CHAR * 80),
        ("hbmpItem", win32more.Graphics.Gdi.HBITMAP),
    ]
    return IMEMENUITEMINFOA
def _define_IMEMENUITEMINFOW_head():
    class IMEMENUITEMINFOW(Structure):
        pass
    return IMEMENUITEMINFOW
def _define_IMEMENUITEMINFOW():
    IMEMENUITEMINFOW = win32more.UI.Input.Ime.IMEMENUITEMINFOW_head
    IMEMENUITEMINFOW._fields_ = [
        ("cbSize", UInt32),
        ("fType", UInt32),
        ("fState", UInt32),
        ("wID", UInt32),
        ("hbmpChecked", win32more.Graphics.Gdi.HBITMAP),
        ("hbmpUnchecked", win32more.Graphics.Gdi.HBITMAP),
        ("dwItemData", UInt32),
        ("szString", Char * 80),
        ("hbmpItem", win32more.Graphics.Gdi.HBITMAP),
    ]
    return IMEMENUITEMINFOW
def _define_IMECHARPOSITION_head():
    class IMECHARPOSITION(Structure):
        pass
    return IMECHARPOSITION
def _define_IMECHARPOSITION():
    IMECHARPOSITION = win32more.UI.Input.Ime.IMECHARPOSITION_head
    IMECHARPOSITION._fields_ = [
        ("dwSize", UInt32),
        ("dwCharPos", UInt32),
        ("pt", win32more.Foundation.POINT),
        ("cLineHeight", UInt32),
        ("rcDocument", win32more.Foundation.RECT),
    ]
    return IMECHARPOSITION
def _define_IMCENUMPROC():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Globalization.HIMC,win32more.Foundation.LPARAM, use_last_error=False)
def _define_REGISTERWORDENUMPROCA():
    return CFUNCTYPE(Int32,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,c_void_p, use_last_error=False)
def _define_REGISTERWORDENUMPROCW():
    return CFUNCTYPE(Int32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,c_void_p, use_last_error=False)
def _define_IFEClassFactory_head():
    class IFEClassFactory(win32more.System.Com.IClassFactory_head):
        Guid = Guid(None)
    return IFEClassFactory
def _define_IFEClassFactory():
    IFEClassFactory = win32more.UI.Input.Ime.IFEClassFactory_head
    return IFEClassFactory
def _define_IMEDLG_head():
    class IMEDLG(Structure):
        pass
    return IMEDLG
def _define_IMEDLG():
    IMEDLG = win32more.UI.Input.Ime.IMEDLG_head
    IMEDLG._pack_ = 1
    IMEDLG._fields_ = [
        ("cbIMEDLG", Int32),
        ("hwnd", win32more.Foundation.HWND),
        ("lpwstrWord", win32more.Foundation.PWSTR),
        ("nTabId", Int32),
    ]
    return IMEDLG
def _define_IFECommon_head():
    class IFECommon(win32more.System.Com.IUnknown_head):
        Guid = Guid('019f7151-e6db-11d0-83c3-00c04fddb82e')
    return IFECommon
def _define_IFECommon():
    IFECommon = win32more.UI.Input.Ime.IFECommon_head
    IFECommon.IsDefaultIME = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),Int32, use_last_error=False)(3, 'IsDefaultIME', ((1, 'szName'),(1, 'cszName'),)))
    IFECommon.SetDefaultIME = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'SetDefaultIME', ()))
    IFECommon.InvokeWordRegDialog = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Input.Ime.IMEDLG_head), use_last_error=False)(5, 'InvokeWordRegDialog', ((1, 'pimedlg'),)))
    IFECommon.InvokeDictToolDialog = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Input.Ime.IMEDLG_head), use_last_error=False)(6, 'InvokeDictToolDialog', ((1, 'pimedlg'),)))
    return IFECommon
def _define_WDD_head():
    class WDD(Structure):
        pass
    return WDD
def _define_WDD():
    WDD = win32more.UI.Input.Ime.WDD_head
    class WDD__Anonymous2_e__Union(Union):
        pass
    WDD__Anonymous2_e__Union._pack_ = 1
    WDD__Anonymous2_e__Union._fields_ = [
        ("cchRead", UInt16),
        ("cchComp", UInt16),
    ]
    class WDD__Anonymous1_e__Union(Union):
        pass
    WDD__Anonymous1_e__Union._pack_ = 1
    WDD__Anonymous1_e__Union._fields_ = [
        ("wReadPos", UInt16),
        ("wCompPos", UInt16),
    ]
    WDD._pack_ = 1
    WDD._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    WDD._fields_ = [
        ("wDispPos", UInt16),
        ("Anonymous1", WDD__Anonymous1_e__Union),
        ("cchDisp", UInt16),
        ("Anonymous2", WDD__Anonymous2_e__Union),
        ("WDD_nReserve1", UInt32),
        ("nPos", UInt16),
        ("_bitfield", UInt16),
        ("pReserved", c_void_p),
    ]
    return WDD
def _define_MORRSLT_head():
    class MORRSLT(Structure):
        pass
    return MORRSLT
def _define_MORRSLT():
    MORRSLT = win32more.UI.Input.Ime.MORRSLT_head
    class MORRSLT__Anonymous2_e__Union(Union):
        pass
    MORRSLT__Anonymous2_e__Union._pack_ = 1
    MORRSLT__Anonymous2_e__Union._fields_ = [
        ("cchRead", UInt16),
        ("cchComp", UInt16),
    ]
    class MORRSLT__Anonymous3_e__Union(Union):
        pass
    MORRSLT__Anonymous3_e__Union._pack_ = 1
    MORRSLT__Anonymous3_e__Union._fields_ = [
        ("pchReadIdxWDD", POINTER(UInt16)),
        ("pchCompIdxWDD", POINTER(UInt16)),
    ]
    class MORRSLT__Anonymous1_e__Union(Union):
        pass
    MORRSLT__Anonymous1_e__Union._pack_ = 1
    MORRSLT__Anonymous1_e__Union._fields_ = [
        ("pwchRead", win32more.Foundation.PWSTR),
        ("pwchComp", win32more.Foundation.PWSTR),
    ]
    MORRSLT._pack_ = 1
    MORRSLT._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
        'Anonymous3',
    ]
    MORRSLT._fields_ = [
        ("dwSize", UInt32),
        ("pwchOutput", win32more.Foundation.PWSTR),
        ("cchOutput", UInt16),
        ("Anonymous1", MORRSLT__Anonymous1_e__Union),
        ("Anonymous2", MORRSLT__Anonymous2_e__Union),
        ("pchInputPos", POINTER(UInt16)),
        ("pchOutputIdxWDD", POINTER(UInt16)),
        ("Anonymous3", MORRSLT__Anonymous3_e__Union),
        ("paMonoRubyPos", POINTER(UInt16)),
        ("pWDD", POINTER(win32more.UI.Input.Ime.WDD_head)),
        ("cWDD", Int32),
        ("pPrivate", c_void_p),
        ("BLKBuff", Char * 0),
    ]
    return MORRSLT
def _define_IFELanguage_head():
    class IFELanguage(win32more.System.Com.IUnknown_head):
        Guid = Guid('019f7152-e6db-11d0-83c3-00c04fddb82e')
    return IFELanguage
def _define_IFELanguage():
    IFELanguage = win32more.UI.Input.Ime.IFELanguage_head
    IFELanguage.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Open', ()))
    IFELanguage.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Close', ()))
    IFELanguage.GetJMorphResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,Int32,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(POINTER(win32more.UI.Input.Ime.MORRSLT_head)), use_last_error=False)(5, 'GetJMorphResult', ((1, 'dwRequest'),(1, 'dwCMode'),(1, 'cwchInput'),(1, 'pwchInput'),(1, 'pfCInfo'),(1, 'ppResult'),)))
    IFELanguage.GetConversionModeCaps = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(6, 'GetConversionModeCaps', ((1, 'pdwCaps'),)))
    IFELanguage.GetPhonetic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'GetPhonetic', ((1, 'string'),(1, 'start'),(1, 'length'),(1, 'phonetic'),)))
    IFELanguage.GetConversion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,Int32,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'GetConversion', ((1, 'string'),(1, 'start'),(1, 'length'),(1, 'result'),)))
    return IFELanguage
IMEREG = Int32
IFED_REG_HEAD = 0
IFED_REG_TAIL = 1
IFED_REG_DEL = 2
IMEFMT = Int32
IFED_UNKNOWN = 0
IFED_MSIME2_BIN_SYSTEM = 1
IFED_MSIME2_BIN_USER = 2
IFED_MSIME2_TEXT_USER = 3
IFED_MSIME95_BIN_SYSTEM = 4
IFED_MSIME95_BIN_USER = 5
IFED_MSIME95_TEXT_USER = 6
IFED_MSIME97_BIN_SYSTEM = 7
IFED_MSIME97_BIN_USER = 8
IFED_MSIME97_TEXT_USER = 9
IFED_MSIME98_BIN_SYSTEM = 10
IFED_MSIME98_BIN_USER = 11
IFED_MSIME98_TEXT_USER = 12
IFED_ACTIVE_DICT = 13
IFED_ATOK9 = 14
IFED_ATOK10 = 15
IFED_NEC_AI_ = 16
IFED_WX_II = 17
IFED_WX_III = 18
IFED_VJE_20 = 19
IFED_MSIME98_SYSTEM_CE = 20
IFED_MSIME_BIN_SYSTEM = 21
IFED_MSIME_BIN_USER = 22
IFED_MSIME_TEXT_USER = 23
IFED_PIME2_BIN_USER = 24
IFED_PIME2_BIN_SYSTEM = 25
IFED_PIME2_BIN_STANDARD_SYSTEM = 26
IMEUCT = Int32
IFED_UCT_NONE = 0
IFED_UCT_STRING_SJIS = 1
IFED_UCT_STRING_UNICODE = 2
IFED_UCT_USER_DEFINED = 3
IFED_UCT_MAX = 4
def _define_IMEWRD_head():
    class IMEWRD(Structure):
        pass
    return IMEWRD
def _define_IMEWRD():
    IMEWRD = win32more.UI.Input.Ime.IMEWRD_head
    class IMEWRD__Anonymous_e__Union(Union):
        pass
    class IMEWRD__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    IMEWRD__Anonymous_e__Union__Anonymous_e__Struct._pack_ = 1
    IMEWRD__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ("nPos1", UInt16),
        ("nPos2", UInt16),
    ]
    IMEWRD__Anonymous_e__Union._pack_ = 1
    IMEWRD__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    IMEWRD__Anonymous_e__Union._fields_ = [
        ("ulPos", UInt32),
        ("Anonymous", IMEWRD__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    IMEWRD._pack_ = 1
    IMEWRD._anonymous_ = [
        'Anonymous',
    ]
    IMEWRD._fields_ = [
        ("pwchReading", win32more.Foundation.PWSTR),
        ("pwchDisplay", win32more.Foundation.PWSTR),
        ("Anonymous", IMEWRD__Anonymous_e__Union),
        ("rgulAttrs", UInt32 * 2),
        ("cbComment", Int32),
        ("uct", win32more.UI.Input.Ime.IMEUCT),
        ("pvComment", c_void_p),
    ]
    return IMEWRD
def _define_IMESHF_head():
    class IMESHF(Structure):
        pass
    return IMESHF
def _define_IMESHF():
    IMESHF = win32more.UI.Input.Ime.IMESHF_head
    IMESHF._pack_ = 1
    IMESHF._fields_ = [
        ("cbShf", UInt16),
        ("verDic", UInt16),
        ("szTitle", win32more.Foundation.CHAR * 48),
        ("szDescription", win32more.Foundation.CHAR * 256),
        ("szCopyright", win32more.Foundation.CHAR * 128),
    ]
    return IMESHF
def _define_POSTBL_head():
    class POSTBL(Structure):
        pass
    return POSTBL
def _define_POSTBL():
    POSTBL = win32more.UI.Input.Ime.POSTBL_head
    POSTBL._pack_ = 1
    POSTBL._fields_ = [
        ("nPos", UInt16),
        ("szName", c_char_p_no),
    ]
    return POSTBL
IMEREL = Int32
IFED_REL_NONE = 0
IFED_REL_NO = 1
IFED_REL_GA = 2
IFED_REL_WO = 3
IFED_REL_NI = 4
IFED_REL_DE = 5
IFED_REL_YORI = 6
IFED_REL_KARA = 7
IFED_REL_MADE = 8
IFED_REL_HE = 9
IFED_REL_TO = 10
IFED_REL_IDEOM = 11
IFED_REL_FUKU_YOUGEN = 12
IFED_REL_KEIYOU_YOUGEN = 13
IFED_REL_KEIDOU1_YOUGEN = 14
IFED_REL_KEIDOU2_YOUGEN = 15
IFED_REL_TAIGEN = 16
IFED_REL_YOUGEN = 17
IFED_REL_RENTAI_MEI = 18
IFED_REL_RENSOU = 19
IFED_REL_KEIYOU_TO_YOUGEN = 20
IFED_REL_KEIYOU_TARU_YOUGEN = 21
IFED_REL_UNKNOWN1 = 22
IFED_REL_UNKNOWN2 = 23
IFED_REL_ALL = 24
def _define_IMEDP_head():
    class IMEDP(Structure):
        pass
    return IMEDP
def _define_IMEDP():
    IMEDP = win32more.UI.Input.Ime.IMEDP_head
    IMEDP._pack_ = 1
    IMEDP._fields_ = [
        ("wrdModifier", win32more.UI.Input.Ime.IMEWRD),
        ("wrdModifiee", win32more.UI.Input.Ime.IMEWRD),
        ("relID", win32more.UI.Input.Ime.IMEREL),
    ]
    return IMEDP
def _define_PFNLOG():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.UI.Input.Ime.IMEDP_head),win32more.Foundation.HRESULT, use_last_error=False)
def _define_IFEDictionary_head():
    class IFEDictionary(win32more.System.Com.IUnknown_head):
        Guid = Guid('019f7153-e6db-11d0-83c3-00c04fddb82e')
    return IFEDictionary
def _define_IFEDictionary():
    IFEDictionary = win32more.UI.Input.Ime.IFEDictionary_head
    IFEDictionary.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),POINTER(win32more.UI.Input.Ime.IMESHF_head), use_last_error=False)(3, 'Open', ((1, 'pchDictPath'),(1, 'pshf'),)))
    IFEDictionary.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Close', ()))
    IFEDictionary.GetHeader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),POINTER(win32more.UI.Input.Ime.IMESHF_head),POINTER(win32more.UI.Input.Ime.IMEFMT),POINTER(UInt32), use_last_error=False)(5, 'GetHeader', ((1, 'pchDictPath'),(1, 'pshf'),(1, 'pjfmt'),(1, 'pulType'),)))
    IFEDictionary.DisplayProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND, use_last_error=False)(6, 'DisplayProperty', ((1, 'hwnd'),)))
    IFEDictionary.GetPosTable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.UI.Input.Ime.POSTBL_head)),POINTER(Int32), use_last_error=False)(7, 'GetPosTable', ((1, 'prgPosTbl'),(1, 'pcPosTbl'),)))
    IFEDictionary.GetWords = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,UInt32,UInt32,c_char_p_no,UInt32,POINTER(UInt32), use_last_error=False)(8, 'GetWords', ((1, 'pwchFirst'),(1, 'pwchLast'),(1, 'pwchDisplay'),(1, 'ulPos'),(1, 'ulSelect'),(1, 'ulWordSrc'),(1, 'pchBuffer'),(1, 'cbBuffer'),(1, 'pcWrd'),)))
    IFEDictionary.NextWords = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32,POINTER(UInt32), use_last_error=False)(9, 'NextWords', ((1, 'pchBuffer'),(1, 'cbBuffer'),(1, 'pcWrd'),)))
    IFEDictionary.Create = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,POINTER(win32more.UI.Input.Ime.IMESHF_head), use_last_error=False)(10, 'Create', ((1, 'pchDictPath'),(1, 'pshf'),)))
    IFEDictionary.SetHeader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Input.Ime.IMESHF_head), use_last_error=False)(11, 'SetHeader', ((1, 'pshf'),)))
    IFEDictionary.ExistWord = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Input.Ime.IMEWRD_head), use_last_error=False)(12, 'ExistWord', ((1, 'pwrd'),)))
    IFEDictionary.ExistDependency = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Input.Ime.IMEDP_head), use_last_error=False)(13, 'ExistDependency', ((1, 'pdp'),)))
    IFEDictionary.RegisterWord = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Input.Ime.IMEREG,POINTER(win32more.UI.Input.Ime.IMEWRD_head), use_last_error=False)(14, 'RegisterWord', ((1, 'reg'),(1, 'pwrd'),)))
    IFEDictionary.RegisterDependency = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Input.Ime.IMEREG,POINTER(win32more.UI.Input.Ime.IMEDP_head), use_last_error=False)(15, 'RegisterDependency', ((1, 'reg'),(1, 'pdp'),)))
    IFEDictionary.GetDependencies = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,win32more.UI.Input.Ime.IMEREL,UInt32,c_char_p_no,UInt32,POINTER(UInt32), use_last_error=False)(16, 'GetDependencies', ((1, 'pwchKakariReading'),(1, 'pwchKakariDisplay'),(1, 'ulKakariPos'),(1, 'pwchUkeReading'),(1, 'pwchUkeDisplay'),(1, 'ulUkePos'),(1, 'jrel'),(1, 'ulWordSrc'),(1, 'pchBuffer'),(1, 'cbBuffer'),(1, 'pcdp'),)))
    IFEDictionary.NextDependencies = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32,POINTER(UInt32), use_last_error=False)(17, 'NextDependencies', ((1, 'pchBuffer'),(1, 'cbBuffer'),(1, 'pcDp'),)))
    IFEDictionary.ConvertFromOldMSIME = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,win32more.UI.Input.Ime.PFNLOG,win32more.UI.Input.Ime.IMEREG, use_last_error=False)(18, 'ConvertFromOldMSIME', ((1, 'pchDic'),(1, 'pfnLog'),(1, 'reg'),)))
    IFEDictionary.ConvertFromUserToSys = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(19, 'ConvertFromUserToSys', ()))
    return IFEDictionary
def _define_IMEKMSINIT_head():
    class IMEKMSINIT(Structure):
        pass
    return IMEKMSINIT
def _define_IMEKMSINIT():
    IMEKMSINIT = win32more.UI.Input.Ime.IMEKMSINIT_head
    IMEKMSINIT._pack_ = 1
    IMEKMSINIT._fields_ = [
        ("cbSize", Int32),
        ("hWnd", win32more.Foundation.HWND),
    ]
    return IMEKMSINIT
def _define_IMEKMSKEY_head():
    class IMEKMSKEY(Structure):
        pass
    return IMEKMSKEY
def _define_IMEKMSKEY():
    IMEKMSKEY = win32more.UI.Input.Ime.IMEKMSKEY_head
    class IMEKMSKEY__Anonymous1_e__Union(Union):
        pass
    IMEKMSKEY__Anonymous1_e__Union._pack_ = 1
    IMEKMSKEY__Anonymous1_e__Union._fields_ = [
        ("dwControl", UInt32),
        ("dwNotUsed", UInt32),
    ]
    class IMEKMSKEY__Anonymous2_e__Union(Union):
        pass
    IMEKMSKEY__Anonymous2_e__Union._pack_ = 1
    IMEKMSKEY__Anonymous2_e__Union._fields_ = [
        ("pwszDscr", Char * 31),
        ("pwszNoUse", Char * 31),
    ]
    IMEKMSKEY._pack_ = 1
    IMEKMSKEY._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    IMEKMSKEY._fields_ = [
        ("dwStatus", UInt32),
        ("dwCompStatus", UInt32),
        ("dwVKEY", UInt32),
        ("Anonymous1", IMEKMSKEY__Anonymous1_e__Union),
        ("Anonymous2", IMEKMSKEY__Anonymous2_e__Union),
    ]
    return IMEKMSKEY
def _define_IMEKMS_head():
    class IMEKMS(Structure):
        pass
    return IMEKMS
def _define_IMEKMS():
    IMEKMS = win32more.UI.Input.Ime.IMEKMS_head
    IMEKMS._pack_ = 1
    IMEKMS._fields_ = [
        ("cbSize", Int32),
        ("hIMC", win32more.Globalization.HIMC),
        ("cKeyList", UInt32),
        ("pKeyList", POINTER(win32more.UI.Input.Ime.IMEKMSKEY_head)),
    ]
    return IMEKMS
def _define_IMEKMSNTFY_head():
    class IMEKMSNTFY(Structure):
        pass
    return IMEKMSNTFY
def _define_IMEKMSNTFY():
    IMEKMSNTFY = win32more.UI.Input.Ime.IMEKMSNTFY_head
    IMEKMSNTFY._pack_ = 1
    IMEKMSNTFY._fields_ = [
        ("cbSize", Int32),
        ("hIMC", win32more.Globalization.HIMC),
        ("fSelect", win32more.Foundation.BOOL),
    ]
    return IMEKMSNTFY
def _define_IMEKMSKMP_head():
    class IMEKMSKMP(Structure):
        pass
    return IMEKMSKMP
def _define_IMEKMSKMP():
    IMEKMSKMP = win32more.UI.Input.Ime.IMEKMSKMP_head
    IMEKMSKMP._pack_ = 1
    IMEKMSKMP._fields_ = [
        ("cbSize", Int32),
        ("hIMC", win32more.Globalization.HIMC),
        ("idLang", UInt16),
        ("wVKStart", UInt16),
        ("wVKEnd", UInt16),
        ("cKeyList", Int32),
        ("pKeyList", POINTER(win32more.UI.Input.Ime.IMEKMSKEY_head)),
    ]
    return IMEKMSKMP
def _define_IMEKMSINVK_head():
    class IMEKMSINVK(Structure):
        pass
    return IMEKMSINVK
def _define_IMEKMSINVK():
    IMEKMSINVK = win32more.UI.Input.Ime.IMEKMSINVK_head
    IMEKMSINVK._pack_ = 1
    IMEKMSINVK._fields_ = [
        ("cbSize", Int32),
        ("hIMC", win32more.Globalization.HIMC),
        ("dwControl", UInt32),
    ]
    return IMEKMSINVK
def _define_IMEKMSFUNCDESC_head():
    class IMEKMSFUNCDESC(Structure):
        pass
    return IMEKMSFUNCDESC
def _define_IMEKMSFUNCDESC():
    IMEKMSFUNCDESC = win32more.UI.Input.Ime.IMEKMSFUNCDESC_head
    IMEKMSFUNCDESC._pack_ = 1
    IMEKMSFUNCDESC._fields_ = [
        ("cbSize", Int32),
        ("idLang", UInt16),
        ("dwControl", UInt32),
        ("pwszDescription", Char * 128),
    ]
    return IMEKMSFUNCDESC
def _define_fpCreateIFECommonInstanceType():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_void_p), use_last_error=False)
def _define_fpCreateIFELanguageInstanceType():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)
def _define_fpCreateIFEDictionaryInstanceType():
    return CFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_void_p), use_last_error=False)
def _define_COMPOSITIONSTRING_head():
    class COMPOSITIONSTRING(Structure):
        pass
    return COMPOSITIONSTRING
def _define_COMPOSITIONSTRING():
    COMPOSITIONSTRING = win32more.UI.Input.Ime.COMPOSITIONSTRING_head
    COMPOSITIONSTRING._fields_ = [
        ("dwSize", UInt32),
        ("dwCompReadAttrLen", UInt32),
        ("dwCompReadAttrOffset", UInt32),
        ("dwCompReadClauseLen", UInt32),
        ("dwCompReadClauseOffset", UInt32),
        ("dwCompReadStrLen", UInt32),
        ("dwCompReadStrOffset", UInt32),
        ("dwCompAttrLen", UInt32),
        ("dwCompAttrOffset", UInt32),
        ("dwCompClauseLen", UInt32),
        ("dwCompClauseOffset", UInt32),
        ("dwCompStrLen", UInt32),
        ("dwCompStrOffset", UInt32),
        ("dwCursorPos", UInt32),
        ("dwDeltaStart", UInt32),
        ("dwResultReadClauseLen", UInt32),
        ("dwResultReadClauseOffset", UInt32),
        ("dwResultReadStrLen", UInt32),
        ("dwResultReadStrOffset", UInt32),
        ("dwResultClauseLen", UInt32),
        ("dwResultClauseOffset", UInt32),
        ("dwResultStrLen", UInt32),
        ("dwResultStrOffset", UInt32),
        ("dwPrivateSize", UInt32),
        ("dwPrivateOffset", UInt32),
    ]
    return COMPOSITIONSTRING
def _define_GUIDELINE_head():
    class GUIDELINE(Structure):
        pass
    return GUIDELINE
def _define_GUIDELINE():
    GUIDELINE = win32more.UI.Input.Ime.GUIDELINE_head
    GUIDELINE._fields_ = [
        ("dwSize", UInt32),
        ("dwLevel", UInt32),
        ("dwIndex", UInt32),
        ("dwStrLen", UInt32),
        ("dwStrOffset", UInt32),
        ("dwPrivateSize", UInt32),
        ("dwPrivateOffset", UInt32),
    ]
    return GUIDELINE
def _define_TRANSMSG_head():
    class TRANSMSG(Structure):
        pass
    return TRANSMSG
def _define_TRANSMSG():
    TRANSMSG = win32more.UI.Input.Ime.TRANSMSG_head
    TRANSMSG._fields_ = [
        ("message", UInt32),
        ("wParam", win32more.Foundation.WPARAM),
        ("lParam", win32more.Foundation.LPARAM),
    ]
    return TRANSMSG
def _define_TRANSMSGLIST_head():
    class TRANSMSGLIST(Structure):
        pass
    return TRANSMSGLIST
def _define_TRANSMSGLIST():
    TRANSMSGLIST = win32more.UI.Input.Ime.TRANSMSGLIST_head
    TRANSMSGLIST._fields_ = [
        ("uMsgCount", UInt32),
        ("TransMsg", win32more.UI.Input.Ime.TRANSMSG * 0),
    ]
    return TRANSMSGLIST
def _define_CANDIDATEINFO_head():
    class CANDIDATEINFO(Structure):
        pass
    return CANDIDATEINFO
def _define_CANDIDATEINFO():
    CANDIDATEINFO = win32more.UI.Input.Ime.CANDIDATEINFO_head
    CANDIDATEINFO._fields_ = [
        ("dwSize", UInt32),
        ("dwCount", UInt32),
        ("dwOffset", UInt32 * 32),
        ("dwPrivateSize", UInt32),
        ("dwPrivateOffset", UInt32),
    ]
    return CANDIDATEINFO
def _define_INPUTCONTEXT_head():
    class INPUTCONTEXT(Structure):
        pass
    return INPUTCONTEXT
def _define_INPUTCONTEXT():
    INPUTCONTEXT = win32more.UI.Input.Ime.INPUTCONTEXT_head
    class INPUTCONTEXT__lfFont_e__Union(Union):
        pass
    INPUTCONTEXT__lfFont_e__Union._fields_ = [
        ("A", win32more.Graphics.Gdi.LOGFONTA),
        ("W", win32more.Graphics.Gdi.LOGFONTW),
    ]
    INPUTCONTEXT._fields_ = [
        ("hWnd", win32more.Foundation.HWND),
        ("fOpen", win32more.Foundation.BOOL),
        ("ptStatusWndPos", win32more.Foundation.POINT),
        ("ptSoftKbdPos", win32more.Foundation.POINT),
        ("fdwConversion", UInt32),
        ("fdwSentence", UInt32),
        ("lfFont", INPUTCONTEXT__lfFont_e__Union),
        ("cfCompForm", win32more.UI.Input.Ime.COMPOSITIONFORM),
        ("cfCandForm", win32more.UI.Input.Ime.CANDIDATEFORM * 4),
        ("hCompStr", win32more.Globalization.HIMCC),
        ("hCandInfo", win32more.Globalization.HIMCC),
        ("hGuideLine", win32more.Globalization.HIMCC),
        ("hPrivate", win32more.Globalization.HIMCC),
        ("dwNumMsgBuf", UInt32),
        ("hMsgBuf", win32more.Globalization.HIMCC),
        ("fdwInit", UInt32),
        ("dwReserve", UInt32 * 3),
    ]
    return INPUTCONTEXT
def _define_IMEINFO_head():
    class IMEINFO(Structure):
        pass
    return IMEINFO
def _define_IMEINFO():
    IMEINFO = win32more.UI.Input.Ime.IMEINFO_head
    IMEINFO._fields_ = [
        ("dwPrivateDataSize", UInt32),
        ("fdwProperty", UInt32),
        ("fdwConversionCaps", UInt32),
        ("fdwSentenceCaps", UInt32),
        ("fdwUICaps", UInt32),
        ("fdwSCSCaps", UInt32),
        ("fdwSelectCaps", UInt32),
    ]
    return IMEINFO
def _define_SOFTKBDDATA_head():
    class SOFTKBDDATA(Structure):
        pass
    return SOFTKBDDATA
def _define_SOFTKBDDATA():
    SOFTKBDDATA = win32more.UI.Input.Ime.SOFTKBDDATA_head
    SOFTKBDDATA._fields_ = [
        ("uCount", UInt32),
        ("wCode", UInt16 * 256),
    ]
    return SOFTKBDDATA
def _define_APPLETIDLIST_head():
    class APPLETIDLIST(Structure):
        pass
    return APPLETIDLIST
def _define_APPLETIDLIST():
    APPLETIDLIST = win32more.UI.Input.Ime.APPLETIDLIST_head
    APPLETIDLIST._fields_ = [
        ("count", Int32),
        ("pIIDList", POINTER(Guid)),
    ]
    return APPLETIDLIST
def _define_IMESTRINGCANDIDATE_head():
    class IMESTRINGCANDIDATE(Structure):
        pass
    return IMESTRINGCANDIDATE
def _define_IMESTRINGCANDIDATE():
    IMESTRINGCANDIDATE = win32more.UI.Input.Ime.IMESTRINGCANDIDATE_head
    IMESTRINGCANDIDATE._fields_ = [
        ("uCount", UInt32),
        ("lpwstr", win32more.Foundation.PWSTR * 0),
    ]
    return IMESTRINGCANDIDATE
def _define_IMEITEM_head():
    class IMEITEM(Structure):
        pass
    return IMEITEM
def _define_IMEITEM():
    IMEITEM = win32more.UI.Input.Ime.IMEITEM_head
    IMEITEM._fields_ = [
        ("cbSize", Int32),
        ("iType", Int32),
        ("lpItemData", c_void_p),
    ]
    return IMEITEM
def _define_IMEITEMCANDIDATE_head():
    class IMEITEMCANDIDATE(Structure):
        pass
    return IMEITEMCANDIDATE
def _define_IMEITEMCANDIDATE():
    IMEITEMCANDIDATE = win32more.UI.Input.Ime.IMEITEMCANDIDATE_head
    IMEITEMCANDIDATE._fields_ = [
        ("uCount", UInt32),
        ("imeItem", win32more.UI.Input.Ime.IMEITEM * 0),
    ]
    return IMEITEMCANDIDATE
def _define_tabIMESTRINGINFO_head():
    class tabIMESTRINGINFO(Structure):
        pass
    return tabIMESTRINGINFO
def _define_tabIMESTRINGINFO():
    tabIMESTRINGINFO = win32more.UI.Input.Ime.tabIMESTRINGINFO_head
    tabIMESTRINGINFO._fields_ = [
        ("dwFarEastId", UInt32),
        ("lpwstr", win32more.Foundation.PWSTR),
    ]
    return tabIMESTRINGINFO
def _define_tabIMEFAREASTINFO_head():
    class tabIMEFAREASTINFO(Structure):
        pass
    return tabIMEFAREASTINFO
def _define_tabIMEFAREASTINFO():
    tabIMEFAREASTINFO = win32more.UI.Input.Ime.tabIMEFAREASTINFO_head
    tabIMEFAREASTINFO._fields_ = [
        ("dwSize", UInt32),
        ("dwType", UInt32),
        ("dwData", UInt32 * 0),
    ]
    return tabIMEFAREASTINFO
def _define_IMESTRINGCANDIDATEINFO_head():
    class IMESTRINGCANDIDATEINFO(Structure):
        pass
    return IMESTRINGCANDIDATEINFO
def _define_IMESTRINGCANDIDATEINFO():
    IMESTRINGCANDIDATEINFO = win32more.UI.Input.Ime.IMESTRINGCANDIDATEINFO_head
    IMESTRINGCANDIDATEINFO._fields_ = [
        ("dwFarEastId", UInt32),
        ("lpFarEastInfo", POINTER(win32more.UI.Input.Ime.tabIMEFAREASTINFO_head)),
        ("fInfoMask", UInt32),
        ("iSelIndex", Int32),
        ("uCount", UInt32),
        ("lpwstr", win32more.Foundation.PWSTR * 0),
    ]
    return IMESTRINGCANDIDATEINFO
def _define_IMECOMPOSITIONSTRINGINFO_head():
    class IMECOMPOSITIONSTRINGINFO(Structure):
        pass
    return IMECOMPOSITIONSTRINGINFO
def _define_IMECOMPOSITIONSTRINGINFO():
    IMECOMPOSITIONSTRINGINFO = win32more.UI.Input.Ime.IMECOMPOSITIONSTRINGINFO_head
    IMECOMPOSITIONSTRINGINFO._fields_ = [
        ("iCompStrLen", Int32),
        ("iCaretPos", Int32),
        ("iEditStart", Int32),
        ("iEditLen", Int32),
        ("iTargetStart", Int32),
        ("iTargetLen", Int32),
    ]
    return IMECOMPOSITIONSTRINGINFO
def _define_IMECHARINFO_head():
    class IMECHARINFO(Structure):
        pass
    return IMECHARINFO
def _define_IMECHARINFO():
    IMECHARINFO = win32more.UI.Input.Ime.IMECHARINFO_head
    IMECHARINFO._fields_ = [
        ("wch", Char),
        ("dwCharInfo", UInt32),
    ]
    return IMECHARINFO
def _define_IMEAPPLETCFG_head():
    class IMEAPPLETCFG(Structure):
        pass
    return IMEAPPLETCFG
def _define_IMEAPPLETCFG():
    IMEAPPLETCFG = win32more.UI.Input.Ime.IMEAPPLETCFG_head
    IMEAPPLETCFG._fields_ = [
        ("dwConfig", UInt32),
        ("wchTitle", Char * 64),
        ("wchTitleFontFace", Char * 32),
        ("dwCharSet", UInt32),
        ("iCategory", Int32),
        ("hIcon", win32more.UI.WindowsAndMessaging.HICON),
        ("langID", UInt16),
        ("dummy", UInt16),
        ("lReserved1", win32more.Foundation.LPARAM),
    ]
    return IMEAPPLETCFG
def _define_IMEAPPLETUI_head():
    class IMEAPPLETUI(Structure):
        pass
    return IMEAPPLETUI
def _define_IMEAPPLETUI():
    IMEAPPLETUI = win32more.UI.Input.Ime.IMEAPPLETUI_head
    IMEAPPLETUI._fields_ = [
        ("hwnd", win32more.Foundation.HWND),
        ("dwStyle", UInt32),
        ("width", Int32),
        ("height", Int32),
        ("minWidth", Int32),
        ("minHeight", Int32),
        ("maxWidth", Int32),
        ("maxHeight", Int32),
        ("lReserved1", win32more.Foundation.LPARAM),
        ("lReserved2", win32more.Foundation.LPARAM),
    ]
    return IMEAPPLETUI
def _define_APPLYCANDEXPARAM_head():
    class APPLYCANDEXPARAM(Structure):
        pass
    return APPLYCANDEXPARAM
def _define_APPLYCANDEXPARAM():
    APPLYCANDEXPARAM = win32more.UI.Input.Ime.APPLYCANDEXPARAM_head
    APPLYCANDEXPARAM._fields_ = [
        ("dwSize", UInt32),
        ("lpwstrDisplay", win32more.Foundation.PWSTR),
        ("lpwstrReading", win32more.Foundation.PWSTR),
        ("dwReserved", UInt32),
    ]
    return APPLYCANDEXPARAM
def _define_IImeSpecifyApplets_head():
    class IImeSpecifyApplets(win32more.System.Com.IUnknown_head):
        Guid = Guid('5d8e643c-c3a9-11d1-afef-00805f0c8b6d')
    return IImeSpecifyApplets
def _define_IImeSpecifyApplets():
    IImeSpecifyApplets = win32more.UI.Input.Ime.IImeSpecifyApplets_head
    IImeSpecifyApplets.GetAppletIIDList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.UI.Input.Ime.APPLETIDLIST_head), use_last_error=False)(3, 'GetAppletIIDList', ((1, 'refiid'),(1, 'lpIIDList'),)))
    return IImeSpecifyApplets
def _define_IImePadApplet_head():
    class IImePadApplet(win32more.System.Com.IUnknown_head):
        Guid = Guid('5d8e643b-c3a9-11d1-afef-00805f0c8b6d')
    return IImePadApplet
def _define_IImePadApplet():
    IImePadApplet = win32more.UI.Input.Ime.IImePadApplet_head
    IImePadApplet.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(3, 'Initialize', ((1, 'lpIImePad'),)))
    IImePadApplet.Terminate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Terminate', ()))
    IImePadApplet.GetAppletConfig = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Input.Ime.IMEAPPLETCFG_head), use_last_error=False)(5, 'GetAppletConfig', ((1, 'lpAppletCfg'),)))
    IImePadApplet.CreateUI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.UI.Input.Ime.IMEAPPLETUI_head), use_last_error=False)(6, 'CreateUI', ((1, 'hwndParent'),(1, 'lpImeAppletUI'),)))
    IImePadApplet.Notify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,Int32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM, use_last_error=False)(7, 'Notify', ((1, 'lpImePad'),(1, 'notify'),(1, 'wParam'),(1, 'lParam'),)))
    return IImePadApplet
def _define_IImePad_head():
    class IImePad(win32more.System.Com.IUnknown_head):
        Guid = Guid('5d8e643a-c3a9-11d1-afef-00805f0c8b6d')
    return IImePad
def _define_IImePad():
    IImePad = win32more.UI.Input.Ime.IImePad_head
    IImePad.Request = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.Input.Ime.IImePadApplet_head,win32more.UI.Input.Ime.IME_PAD_REQUEST_FLAGS,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM, use_last_error=False)(3, 'Request', ((1, 'pIImePadApplet'),(1, 'reqId'),(1, 'wParam'),(1, 'lParam'),)))
    return IImePad
def _define_IImePlugInDictDictionaryList_head():
    class IImePlugInDictDictionaryList(win32more.System.Com.IUnknown_head):
        Guid = Guid('98752974-b0a6-489b-8f6f-bff3769c8eeb')
    return IImePlugInDictDictionaryList
def _define_IImePlugInDictDictionaryList():
    IImePlugInDictDictionaryList = win32more.UI.Input.Ime.IImePlugInDictDictionaryList_head
    IImePlugInDictDictionaryList.GetDictionariesInUse = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(3, 'GetDictionariesInUse', ((1, 'prgDictionaryGUID'),(1, 'prgDateCreated'),(1, 'prgfEncrypted'),)))
    IImePlugInDictDictionaryList.DeleteDictionary = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(4, 'DeleteDictionary', ((1, 'bstrDictionaryGUID'),)))
    return IImePlugInDictDictionaryList
CActiveIMM = Guid('4955dd33-b159-11d0-8fcf-00aa006bcc59')
def _define_IEnumRegisterWordA_head():
    class IEnumRegisterWordA(win32more.System.Com.IUnknown_head):
        Guid = Guid('08c03412-f96b-11d0-a475-00aa006bcc59')
    return IEnumRegisterWordA
def _define_IEnumRegisterWordA():
    IEnumRegisterWordA = win32more.UI.Input.Ime.IEnumRegisterWordA_head
    IEnumRegisterWordA.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Input.Ime.IEnumRegisterWordA_head), use_last_error=False)(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumRegisterWordA.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Input.Ime.REGISTERWORDA_head),POINTER(UInt32), use_last_error=False)(4, 'Next', ((1, 'ulCount'),(1, 'rgRegisterWord'),(1, 'pcFetched'),)))
    IEnumRegisterWordA.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumRegisterWordA.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'Skip', ((1, 'ulCount'),)))
    return IEnumRegisterWordA
def _define_IEnumRegisterWordW_head():
    class IEnumRegisterWordW(win32more.System.Com.IUnknown_head):
        Guid = Guid('4955dd31-b159-11d0-8fcf-00aa006bcc59')
    return IEnumRegisterWordW
def _define_IEnumRegisterWordW():
    IEnumRegisterWordW = win32more.UI.Input.Ime.IEnumRegisterWordW_head
    IEnumRegisterWordW.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Input.Ime.IEnumRegisterWordW_head), use_last_error=False)(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumRegisterWordW.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Input.Ime.REGISTERWORDW_head),POINTER(UInt32), use_last_error=False)(4, 'Next', ((1, 'ulCount'),(1, 'rgRegisterWord'),(1, 'pcFetched'),)))
    IEnumRegisterWordW.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumRegisterWordW.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'Skip', ((1, 'ulCount'),)))
    return IEnumRegisterWordW
def _define_IEnumInputContext_head():
    class IEnumInputContext(win32more.System.Com.IUnknown_head):
        Guid = Guid('09b5eab0-f997-11d1-93d4-0060b067b86e')
    return IEnumInputContext
def _define_IEnumInputContext():
    IEnumInputContext = win32more.UI.Input.Ime.IEnumInputContext_head
    IEnumInputContext.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.Input.Ime.IEnumInputContext_head), use_last_error=False)(3, 'Clone', ((1, 'ppEnum'),)))
    IEnumInputContext.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Globalization.HIMC),POINTER(UInt32), use_last_error=False)(4, 'Next', ((1, 'ulCount'),(1, 'rgInputContext'),(1, 'pcFetched'),)))
    IEnumInputContext.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumInputContext.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'Skip', ((1, 'ulCount'),)))
    return IEnumInputContext
def _define_IActiveIMMRegistrar_head():
    class IActiveIMMRegistrar(win32more.System.Com.IUnknown_head):
        Guid = Guid('b3458082-bd00-11d1-939b-0060b067b86e')
    return IActiveIMMRegistrar
def _define_IActiveIMMRegistrar():
    IActiveIMMRegistrar = win32more.UI.Input.Ime.IActiveIMMRegistrar_head
    IActiveIMMRegistrar.RegisterIME = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt16,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(3, 'RegisterIME', ((1, 'rclsid'),(1, 'lgid'),(1, 'pszIconFile'),(1, 'pszDesc'),)))
    IActiveIMMRegistrar.UnregisterIME = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(4, 'UnregisterIME', ((1, 'rclsid'),)))
    return IActiveIMMRegistrar
def _define_IActiveIMMMessagePumpOwner_head():
    class IActiveIMMMessagePumpOwner(win32more.System.Com.IUnknown_head):
        Guid = Guid('b5cf2cfa-8aeb-11d1-9364-0060b067b86e')
    return IActiveIMMMessagePumpOwner
def _define_IActiveIMMMessagePumpOwner():
    IActiveIMMMessagePumpOwner = win32more.UI.Input.Ime.IActiveIMMMessagePumpOwner_head
    IActiveIMMMessagePumpOwner.Start = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Start', ()))
    IActiveIMMMessagePumpOwner.End = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'End', ()))
    IActiveIMMMessagePumpOwner.OnTranslateMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.WindowsAndMessaging.MSG_head), use_last_error=False)(5, 'OnTranslateMessage', ((1, 'pMsg'),)))
    IActiveIMMMessagePumpOwner.Pause = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(6, 'Pause', ((1, 'pdwCookie'),)))
    IActiveIMMMessagePumpOwner.Resume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(7, 'Resume', ((1, 'dwCookie'),)))
    return IActiveIMMMessagePumpOwner
def _define_IActiveIMMApp_head():
    class IActiveIMMApp(win32more.System.Com.IUnknown_head):
        Guid = Guid('08c0e040-62d1-11d1-9326-0060b067b86e')
    return IActiveIMMApp
def _define_IActiveIMMApp():
    IActiveIMMApp = win32more.UI.Input.Ime.IActiveIMMApp_head
    IActiveIMMApp.AssociateContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Globalization.HIMC,POINTER(win32more.Globalization.HIMC), use_last_error=False)(3, 'AssociateContext', ((1, 'hWnd'),(1, 'hIME'),(1, 'phPrev'),)))
    IActiveIMMApp.ConfigureIMEA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,win32more.Foundation.HWND,UInt32,POINTER(win32more.UI.Input.Ime.REGISTERWORDA_head), use_last_error=False)(4, 'ConfigureIMEA', ((1, 'hKL'),(1, 'hWnd'),(1, 'dwMode'),(1, 'pData'),)))
    IActiveIMMApp.ConfigureIMEW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,win32more.Foundation.HWND,UInt32,POINTER(win32more.UI.Input.Ime.REGISTERWORDW_head), use_last_error=False)(5, 'ConfigureIMEW', ((1, 'hKL'),(1, 'hWnd'),(1, 'dwMode'),(1, 'pData'),)))
    IActiveIMMApp.CreateContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Globalization.HIMC), use_last_error=False)(6, 'CreateContext', ((1, 'phIMC'),)))
    IActiveIMMApp.DestroyContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC, use_last_error=False)(7, 'DestroyContext', ((1, 'hIME'),)))
    IActiveIMMApp.EnumRegisterWordA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,c_void_p,POINTER(win32more.UI.Input.Ime.IEnumRegisterWordA_head), use_last_error=False)(8, 'EnumRegisterWordA', ((1, 'hKL'),(1, 'szReading'),(1, 'dwStyle'),(1, 'szRegister'),(1, 'pData'),(1, 'pEnum'),)))
    IActiveIMMApp.EnumRegisterWordW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,c_void_p,POINTER(win32more.UI.Input.Ime.IEnumRegisterWordW_head), use_last_error=False)(9, 'EnumRegisterWordW', ((1, 'hKL'),(1, 'szReading'),(1, 'dwStyle'),(1, 'szRegister'),(1, 'pData'),(1, 'pEnum'),)))
    IActiveIMMApp.EscapeA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,win32more.Globalization.HIMC,UInt32,c_void_p,POINTER(win32more.Foundation.LRESULT), use_last_error=False)(10, 'EscapeA', ((1, 'hKL'),(1, 'hIMC'),(1, 'uEscape'),(1, 'pData'),(1, 'plResult'),)))
    IActiveIMMApp.EscapeW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,win32more.Globalization.HIMC,UInt32,c_void_p,POINTER(win32more.Foundation.LRESULT), use_last_error=False)(11, 'EscapeW', ((1, 'hKL'),(1, 'hIMC'),(1, 'uEscape'),(1, 'pData'),(1, 'plResult'),)))
    IActiveIMMApp.GetCandidateListA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,UInt32,UInt32,POINTER(win32more.UI.Input.Ime.CANDIDATELIST_head),POINTER(UInt32), use_last_error=False)(12, 'GetCandidateListA', ((1, 'hIMC'),(1, 'dwIndex'),(1, 'uBufLen'),(1, 'pCandList'),(1, 'puCopied'),)))
    IActiveIMMApp.GetCandidateListW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,UInt32,UInt32,POINTER(win32more.UI.Input.Ime.CANDIDATELIST_head),POINTER(UInt32), use_last_error=False)(13, 'GetCandidateListW', ((1, 'hIMC'),(1, 'dwIndex'),(1, 'uBufLen'),(1, 'pCandList'),(1, 'puCopied'),)))
    IActiveIMMApp.GetCandidateListCountA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(14, 'GetCandidateListCountA', ((1, 'hIMC'),(1, 'pdwListSize'),(1, 'pdwBufLen'),)))
    IActiveIMMApp.GetCandidateListCountW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(15, 'GetCandidateListCountW', ((1, 'hIMC'),(1, 'pdwListSize'),(1, 'pdwBufLen'),)))
    IActiveIMMApp.GetCandidateWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,UInt32,POINTER(win32more.UI.Input.Ime.CANDIDATEFORM_head), use_last_error=False)(16, 'GetCandidateWindow', ((1, 'hIMC'),(1, 'dwIndex'),(1, 'pCandidate'),)))
    IActiveIMMApp.GetCompositionFontA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,POINTER(win32more.Graphics.Gdi.LOGFONTA_head), use_last_error=False)(17, 'GetCompositionFontA', ((1, 'hIMC'),(1, 'plf'),)))
    IActiveIMMApp.GetCompositionFontW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,POINTER(win32more.Graphics.Gdi.LOGFONTW_head), use_last_error=False)(18, 'GetCompositionFontW', ((1, 'hIMC'),(1, 'plf'),)))
    IActiveIMMApp.GetCompositionStringA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,UInt32,UInt32,POINTER(Int32),c_void_p, use_last_error=False)(19, 'GetCompositionStringA', ((1, 'hIMC'),(1, 'dwIndex'),(1, 'dwBufLen'),(1, 'plCopied'),(1, 'pBuf'),)))
    IActiveIMMApp.GetCompositionStringW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,UInt32,UInt32,POINTER(Int32),c_void_p, use_last_error=False)(20, 'GetCompositionStringW', ((1, 'hIMC'),(1, 'dwIndex'),(1, 'dwBufLen'),(1, 'plCopied'),(1, 'pBuf'),)))
    IActiveIMMApp.GetCompositionWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,POINTER(win32more.UI.Input.Ime.COMPOSITIONFORM_head), use_last_error=False)(21, 'GetCompositionWindow', ((1, 'hIMC'),(1, 'pCompForm'),)))
    IActiveIMMApp.GetContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.Globalization.HIMC), use_last_error=False)(22, 'GetContext', ((1, 'hWnd'),(1, 'phIMC'),)))
    IActiveIMMApp.GetConversionListA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,win32more.Globalization.HIMC,win32more.Foundation.PSTR,UInt32,UInt32,POINTER(win32more.UI.Input.Ime.CANDIDATELIST_head),POINTER(UInt32), use_last_error=False)(23, 'GetConversionListA', ((1, 'hKL'),(1, 'hIMC'),(1, 'pSrc'),(1, 'uBufLen'),(1, 'uFlag'),(1, 'pDst'),(1, 'puCopied'),)))
    IActiveIMMApp.GetConversionListW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,win32more.Globalization.HIMC,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(win32more.UI.Input.Ime.CANDIDATELIST_head),POINTER(UInt32), use_last_error=False)(24, 'GetConversionListW', ((1, 'hKL'),(1, 'hIMC'),(1, 'pSrc'),(1, 'uBufLen'),(1, 'uFlag'),(1, 'pDst'),(1, 'puCopied'),)))
    IActiveIMMApp.GetConversionStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(25, 'GetConversionStatus', ((1, 'hIMC'),(1, 'pfdwConversion'),(1, 'pfdwSentence'),)))
    IActiveIMMApp.GetDefaultIMEWnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.Foundation.HWND), use_last_error=False)(26, 'GetDefaultIMEWnd', ((1, 'hWnd'),(1, 'phDefWnd'),)))
    IActiveIMMApp.GetDescriptionA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,UInt32,win32more.Foundation.PSTR,POINTER(UInt32), use_last_error=False)(27, 'GetDescriptionA', ((1, 'hKL'),(1, 'uBufLen'),(1, 'szDescription'),(1, 'puCopied'),)))
    IActiveIMMApp.GetDescriptionW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(28, 'GetDescriptionW', ((1, 'hKL'),(1, 'uBufLen'),(1, 'szDescription'),(1, 'puCopied'),)))
    IActiveIMMApp.GetGuideLineA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,UInt32,UInt32,win32more.Foundation.PSTR,POINTER(UInt32), use_last_error=False)(29, 'GetGuideLineA', ((1, 'hIMC'),(1, 'dwIndex'),(1, 'dwBufLen'),(1, 'pBuf'),(1, 'pdwResult'),)))
    IActiveIMMApp.GetGuideLineW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,UInt32,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(30, 'GetGuideLineW', ((1, 'hIMC'),(1, 'dwIndex'),(1, 'dwBufLen'),(1, 'pBuf'),(1, 'pdwResult'),)))
    IActiveIMMApp.GetIMEFileNameA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,UInt32,win32more.Foundation.PSTR,POINTER(UInt32), use_last_error=False)(31, 'GetIMEFileNameA', ((1, 'hKL'),(1, 'uBufLen'),(1, 'szFileName'),(1, 'puCopied'),)))
    IActiveIMMApp.GetIMEFileNameW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(32, 'GetIMEFileNameW', ((1, 'hKL'),(1, 'uBufLen'),(1, 'szFileName'),(1, 'puCopied'),)))
    IActiveIMMApp.GetOpenStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC, use_last_error=False)(33, 'GetOpenStatus', ((1, 'hIMC'),)))
    IActiveIMMApp.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,UInt32,POINTER(UInt32), use_last_error=False)(34, 'GetProperty', ((1, 'hKL'),(1, 'fdwIndex'),(1, 'pdwProperty'),)))
    IActiveIMMApp.GetRegisterWordStyleA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,UInt32,POINTER(win32more.UI.Input.Ime.STYLEBUFA_head),POINTER(UInt32), use_last_error=False)(35, 'GetRegisterWordStyleA', ((1, 'hKL'),(1, 'nItem'),(1, 'pStyleBuf'),(1, 'puCopied'),)))
    IActiveIMMApp.GetRegisterWordStyleW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,UInt32,POINTER(win32more.UI.Input.Ime.STYLEBUFW_head),POINTER(UInt32), use_last_error=False)(36, 'GetRegisterWordStyleW', ((1, 'hKL'),(1, 'nItem'),(1, 'pStyleBuf'),(1, 'puCopied'),)))
    IActiveIMMApp.GetStatusWindowPos = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,POINTER(win32more.Foundation.POINT_head), use_last_error=False)(37, 'GetStatusWindowPos', ((1, 'hIMC'),(1, 'pptPos'),)))
    IActiveIMMApp.GetVirtualKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(UInt32), use_last_error=False)(38, 'GetVirtualKey', ((1, 'hWnd'),(1, 'puVirtualKey'),)))
    IActiveIMMApp.InstallIMEA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.UI.TextServices.HKL), use_last_error=False)(39, 'InstallIMEA', ((1, 'szIMEFileName'),(1, 'szLayoutText'),(1, 'phKL'),)))
    IActiveIMMApp.InstallIMEW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.UI.TextServices.HKL), use_last_error=False)(40, 'InstallIMEW', ((1, 'szIMEFileName'),(1, 'szLayoutText'),(1, 'phKL'),)))
    IActiveIMMApp.IsIME = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL, use_last_error=False)(41, 'IsIME', ((1, 'hKL'),)))
    IActiveIMMApp.IsUIMessageA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM, use_last_error=False)(42, 'IsUIMessageA', ((1, 'hWndIME'),(1, 'msg'),(1, 'wParam'),(1, 'lParam'),)))
    IActiveIMMApp.IsUIMessageW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM, use_last_error=False)(43, 'IsUIMessageW', ((1, 'hWndIME'),(1, 'msg'),(1, 'wParam'),(1, 'lParam'),)))
    IActiveIMMApp.NotifyIME = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,UInt32,UInt32,UInt32, use_last_error=False)(44, 'NotifyIME', ((1, 'hIMC'),(1, 'dwAction'),(1, 'dwIndex'),(1, 'dwValue'),)))
    IActiveIMMApp.RegisterWordA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR, use_last_error=False)(45, 'RegisterWordA', ((1, 'hKL'),(1, 'szReading'),(1, 'dwStyle'),(1, 'szRegister'),)))
    IActiveIMMApp.RegisterWordW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(46, 'RegisterWordW', ((1, 'hKL'),(1, 'szReading'),(1, 'dwStyle'),(1, 'szRegister'),)))
    IActiveIMMApp.ReleaseContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Globalization.HIMC, use_last_error=False)(47, 'ReleaseContext', ((1, 'hWnd'),(1, 'hIMC'),)))
    IActiveIMMApp.SetCandidateWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,POINTER(win32more.UI.Input.Ime.CANDIDATEFORM_head), use_last_error=False)(48, 'SetCandidateWindow', ((1, 'hIMC'),(1, 'pCandidate'),)))
    IActiveIMMApp.SetCompositionFontA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,POINTER(win32more.Graphics.Gdi.LOGFONTA_head), use_last_error=False)(49, 'SetCompositionFontA', ((1, 'hIMC'),(1, 'plf'),)))
    IActiveIMMApp.SetCompositionFontW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,POINTER(win32more.Graphics.Gdi.LOGFONTW_head), use_last_error=False)(50, 'SetCompositionFontW', ((1, 'hIMC'),(1, 'plf'),)))
    IActiveIMMApp.SetCompositionStringA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,UInt32,c_void_p,UInt32,c_void_p,UInt32, use_last_error=False)(51, 'SetCompositionStringA', ((1, 'hIMC'),(1, 'dwIndex'),(1, 'pComp'),(1, 'dwCompLen'),(1, 'pRead'),(1, 'dwReadLen'),)))
    IActiveIMMApp.SetCompositionStringW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,UInt32,c_void_p,UInt32,c_void_p,UInt32, use_last_error=False)(52, 'SetCompositionStringW', ((1, 'hIMC'),(1, 'dwIndex'),(1, 'pComp'),(1, 'dwCompLen'),(1, 'pRead'),(1, 'dwReadLen'),)))
    IActiveIMMApp.SetCompositionWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,POINTER(win32more.UI.Input.Ime.COMPOSITIONFORM_head), use_last_error=False)(53, 'SetCompositionWindow', ((1, 'hIMC'),(1, 'pCompForm'),)))
    IActiveIMMApp.SetConversionStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,UInt32,UInt32, use_last_error=False)(54, 'SetConversionStatus', ((1, 'hIMC'),(1, 'fdwConversion'),(1, 'fdwSentence'),)))
    IActiveIMMApp.SetOpenStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,win32more.Foundation.BOOL, use_last_error=False)(55, 'SetOpenStatus', ((1, 'hIMC'),(1, 'fOpen'),)))
    IActiveIMMApp.SetStatusWindowPos = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,POINTER(win32more.Foundation.POINT_head), use_last_error=False)(56, 'SetStatusWindowPos', ((1, 'hIMC'),(1, 'pptPos'),)))
    IActiveIMMApp.SimulateHotKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32, use_last_error=False)(57, 'SimulateHotKey', ((1, 'hWnd'),(1, 'dwHotKeyID'),)))
    IActiveIMMApp.UnregisterWordA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR, use_last_error=False)(58, 'UnregisterWordA', ((1, 'hKL'),(1, 'szReading'),(1, 'dwStyle'),(1, 'szUnregister'),)))
    IActiveIMMApp.UnregisterWordW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(59, 'UnregisterWordW', ((1, 'hKL'),(1, 'szReading'),(1, 'dwStyle'),(1, 'szUnregister'),)))
    IActiveIMMApp.Activate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(60, 'Activate', ((1, 'fRestoreLayout'),)))
    IActiveIMMApp.Deactivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(61, 'Deactivate', ()))
    IActiveIMMApp.OnDefWindowProc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.LRESULT), use_last_error=False)(62, 'OnDefWindowProc', ((1, 'hWnd'),(1, 'Msg'),(1, 'wParam'),(1, 'lParam'),(1, 'plResult'),)))
    IActiveIMMApp.FilterClientWindows = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16),UInt32, use_last_error=False)(63, 'FilterClientWindows', ((1, 'aaClassList'),(1, 'uSize'),)))
    IActiveIMMApp.GetCodePageA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,POINTER(UInt32), use_last_error=False)(64, 'GetCodePageA', ((1, 'hKL'),(1, 'uCodePage'),)))
    IActiveIMMApp.GetLangId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,POINTER(UInt16), use_last_error=False)(65, 'GetLangId', ((1, 'hKL'),(1, 'plid'),)))
    IActiveIMMApp.AssociateContextEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Globalization.HIMC,UInt32, use_last_error=False)(66, 'AssociateContextEx', ((1, 'hWnd'),(1, 'hIMC'),(1, 'dwFlags'),)))
    IActiveIMMApp.DisableIME = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(67, 'DisableIME', ((1, 'idThread'),)))
    IActiveIMMApp.GetImeMenuItemsA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,UInt32,UInt32,POINTER(win32more.UI.Input.Ime.IMEMENUITEMINFOA_head),POINTER(win32more.UI.Input.Ime.IMEMENUITEMINFOA_head),UInt32,POINTER(UInt32), use_last_error=False)(68, 'GetImeMenuItemsA', ((1, 'hIMC'),(1, 'dwFlags'),(1, 'dwType'),(1, 'pImeParentMenu'),(1, 'pImeMenu'),(1, 'dwSize'),(1, 'pdwResult'),)))
    IActiveIMMApp.GetImeMenuItemsW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,UInt32,UInt32,POINTER(win32more.UI.Input.Ime.IMEMENUITEMINFOW_head),POINTER(win32more.UI.Input.Ime.IMEMENUITEMINFOW_head),UInt32,POINTER(UInt32), use_last_error=False)(69, 'GetImeMenuItemsW', ((1, 'hIMC'),(1, 'dwFlags'),(1, 'dwType'),(1, 'pImeParentMenu'),(1, 'pImeMenu'),(1, 'dwSize'),(1, 'pdwResult'),)))
    IActiveIMMApp.EnumInputContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Input.Ime.IEnumInputContext_head), use_last_error=False)(70, 'EnumInputContext', ((1, 'idThread'),(1, 'ppEnum'),)))
    return IActiveIMMApp
def _define_IActiveIMMIME_head():
    class IActiveIMMIME(win32more.System.Com.IUnknown_head):
        Guid = Guid('08c03411-f96b-11d0-a475-00aa006bcc59')
    return IActiveIMMIME
def _define_IActiveIMMIME():
    IActiveIMMIME = win32more.UI.Input.Ime.IActiveIMMIME_head
    IActiveIMMIME.AssociateContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Globalization.HIMC,POINTER(win32more.Globalization.HIMC), use_last_error=False)(3, 'AssociateContext', ((1, 'hWnd'),(1, 'hIME'),(1, 'phPrev'),)))
    IActiveIMMIME.ConfigureIMEA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,win32more.Foundation.HWND,UInt32,POINTER(win32more.UI.Input.Ime.REGISTERWORDA_head), use_last_error=False)(4, 'ConfigureIMEA', ((1, 'hKL'),(1, 'hWnd'),(1, 'dwMode'),(1, 'pData'),)))
    IActiveIMMIME.ConfigureIMEW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,win32more.Foundation.HWND,UInt32,POINTER(win32more.UI.Input.Ime.REGISTERWORDW_head), use_last_error=False)(5, 'ConfigureIMEW', ((1, 'hKL'),(1, 'hWnd'),(1, 'dwMode'),(1, 'pData'),)))
    IActiveIMMIME.CreateContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Globalization.HIMC), use_last_error=False)(6, 'CreateContext', ((1, 'phIMC'),)))
    IActiveIMMIME.DestroyContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC, use_last_error=False)(7, 'DestroyContext', ((1, 'hIME'),)))
    IActiveIMMIME.EnumRegisterWordA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,c_void_p,POINTER(win32more.UI.Input.Ime.IEnumRegisterWordA_head), use_last_error=False)(8, 'EnumRegisterWordA', ((1, 'hKL'),(1, 'szReading'),(1, 'dwStyle'),(1, 'szRegister'),(1, 'pData'),(1, 'pEnum'),)))
    IActiveIMMIME.EnumRegisterWordW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,c_void_p,POINTER(win32more.UI.Input.Ime.IEnumRegisterWordW_head), use_last_error=False)(9, 'EnumRegisterWordW', ((1, 'hKL'),(1, 'szReading'),(1, 'dwStyle'),(1, 'szRegister'),(1, 'pData'),(1, 'pEnum'),)))
    IActiveIMMIME.EscapeA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,win32more.Globalization.HIMC,UInt32,c_void_p,POINTER(win32more.Foundation.LRESULT), use_last_error=False)(10, 'EscapeA', ((1, 'hKL'),(1, 'hIMC'),(1, 'uEscape'),(1, 'pData'),(1, 'plResult'),)))
    IActiveIMMIME.EscapeW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,win32more.Globalization.HIMC,UInt32,c_void_p,POINTER(win32more.Foundation.LRESULT), use_last_error=False)(11, 'EscapeW', ((1, 'hKL'),(1, 'hIMC'),(1, 'uEscape'),(1, 'pData'),(1, 'plResult'),)))
    IActiveIMMIME.GetCandidateListA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,UInt32,UInt32,POINTER(win32more.UI.Input.Ime.CANDIDATELIST_head),POINTER(UInt32), use_last_error=False)(12, 'GetCandidateListA', ((1, 'hIMC'),(1, 'dwIndex'),(1, 'uBufLen'),(1, 'pCandList'),(1, 'puCopied'),)))
    IActiveIMMIME.GetCandidateListW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,UInt32,UInt32,POINTER(win32more.UI.Input.Ime.CANDIDATELIST_head),POINTER(UInt32), use_last_error=False)(13, 'GetCandidateListW', ((1, 'hIMC'),(1, 'dwIndex'),(1, 'uBufLen'),(1, 'pCandList'),(1, 'puCopied'),)))
    IActiveIMMIME.GetCandidateListCountA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(14, 'GetCandidateListCountA', ((1, 'hIMC'),(1, 'pdwListSize'),(1, 'pdwBufLen'),)))
    IActiveIMMIME.GetCandidateListCountW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(15, 'GetCandidateListCountW', ((1, 'hIMC'),(1, 'pdwListSize'),(1, 'pdwBufLen'),)))
    IActiveIMMIME.GetCandidateWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,UInt32,POINTER(win32more.UI.Input.Ime.CANDIDATEFORM_head), use_last_error=False)(16, 'GetCandidateWindow', ((1, 'hIMC'),(1, 'dwIndex'),(1, 'pCandidate'),)))
    IActiveIMMIME.GetCompositionFontA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,POINTER(win32more.Graphics.Gdi.LOGFONTA_head), use_last_error=False)(17, 'GetCompositionFontA', ((1, 'hIMC'),(1, 'plf'),)))
    IActiveIMMIME.GetCompositionFontW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,POINTER(win32more.Graphics.Gdi.LOGFONTW_head), use_last_error=False)(18, 'GetCompositionFontW', ((1, 'hIMC'),(1, 'plf'),)))
    IActiveIMMIME.GetCompositionStringA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,UInt32,UInt32,POINTER(Int32),c_void_p, use_last_error=False)(19, 'GetCompositionStringA', ((1, 'hIMC'),(1, 'dwIndex'),(1, 'dwBufLen'),(1, 'plCopied'),(1, 'pBuf'),)))
    IActiveIMMIME.GetCompositionStringW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,UInt32,UInt32,POINTER(Int32),c_void_p, use_last_error=False)(20, 'GetCompositionStringW', ((1, 'hIMC'),(1, 'dwIndex'),(1, 'dwBufLen'),(1, 'plCopied'),(1, 'pBuf'),)))
    IActiveIMMIME.GetCompositionWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,POINTER(win32more.UI.Input.Ime.COMPOSITIONFORM_head), use_last_error=False)(21, 'GetCompositionWindow', ((1, 'hIMC'),(1, 'pCompForm'),)))
    IActiveIMMIME.GetContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.Globalization.HIMC), use_last_error=False)(22, 'GetContext', ((1, 'hWnd'),(1, 'phIMC'),)))
    IActiveIMMIME.GetConversionListA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,win32more.Globalization.HIMC,win32more.Foundation.PSTR,UInt32,UInt32,POINTER(win32more.UI.Input.Ime.CANDIDATELIST_head),POINTER(UInt32), use_last_error=False)(23, 'GetConversionListA', ((1, 'hKL'),(1, 'hIMC'),(1, 'pSrc'),(1, 'uBufLen'),(1, 'uFlag'),(1, 'pDst'),(1, 'puCopied'),)))
    IActiveIMMIME.GetConversionListW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,win32more.Globalization.HIMC,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(win32more.UI.Input.Ime.CANDIDATELIST_head),POINTER(UInt32), use_last_error=False)(24, 'GetConversionListW', ((1, 'hKL'),(1, 'hIMC'),(1, 'pSrc'),(1, 'uBufLen'),(1, 'uFlag'),(1, 'pDst'),(1, 'puCopied'),)))
    IActiveIMMIME.GetConversionStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(25, 'GetConversionStatus', ((1, 'hIMC'),(1, 'pfdwConversion'),(1, 'pfdwSentence'),)))
    IActiveIMMIME.GetDefaultIMEWnd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.Foundation.HWND), use_last_error=False)(26, 'GetDefaultIMEWnd', ((1, 'hWnd'),(1, 'phDefWnd'),)))
    IActiveIMMIME.GetDescriptionA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,UInt32,win32more.Foundation.PSTR,POINTER(UInt32), use_last_error=False)(27, 'GetDescriptionA', ((1, 'hKL'),(1, 'uBufLen'),(1, 'szDescription'),(1, 'puCopied'),)))
    IActiveIMMIME.GetDescriptionW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(28, 'GetDescriptionW', ((1, 'hKL'),(1, 'uBufLen'),(1, 'szDescription'),(1, 'puCopied'),)))
    IActiveIMMIME.GetGuideLineA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,UInt32,UInt32,win32more.Foundation.PSTR,POINTER(UInt32), use_last_error=False)(29, 'GetGuideLineA', ((1, 'hIMC'),(1, 'dwIndex'),(1, 'dwBufLen'),(1, 'pBuf'),(1, 'pdwResult'),)))
    IActiveIMMIME.GetGuideLineW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,UInt32,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(30, 'GetGuideLineW', ((1, 'hIMC'),(1, 'dwIndex'),(1, 'dwBufLen'),(1, 'pBuf'),(1, 'pdwResult'),)))
    IActiveIMMIME.GetIMEFileNameA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,UInt32,win32more.Foundation.PSTR,POINTER(UInt32), use_last_error=False)(31, 'GetIMEFileNameA', ((1, 'hKL'),(1, 'uBufLen'),(1, 'szFileName'),(1, 'puCopied'),)))
    IActiveIMMIME.GetIMEFileNameW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(32, 'GetIMEFileNameW', ((1, 'hKL'),(1, 'uBufLen'),(1, 'szFileName'),(1, 'puCopied'),)))
    IActiveIMMIME.GetOpenStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC, use_last_error=False)(33, 'GetOpenStatus', ((1, 'hIMC'),)))
    IActiveIMMIME.GetProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,UInt32,POINTER(UInt32), use_last_error=False)(34, 'GetProperty', ((1, 'hKL'),(1, 'fdwIndex'),(1, 'pdwProperty'),)))
    IActiveIMMIME.GetRegisterWordStyleA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,UInt32,POINTER(win32more.UI.Input.Ime.STYLEBUFA_head),POINTER(UInt32), use_last_error=False)(35, 'GetRegisterWordStyleA', ((1, 'hKL'),(1, 'nItem'),(1, 'pStyleBuf'),(1, 'puCopied'),)))
    IActiveIMMIME.GetRegisterWordStyleW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,UInt32,POINTER(win32more.UI.Input.Ime.STYLEBUFW_head),POINTER(UInt32), use_last_error=False)(36, 'GetRegisterWordStyleW', ((1, 'hKL'),(1, 'nItem'),(1, 'pStyleBuf'),(1, 'puCopied'),)))
    IActiveIMMIME.GetStatusWindowPos = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,POINTER(win32more.Foundation.POINT_head), use_last_error=False)(37, 'GetStatusWindowPos', ((1, 'hIMC'),(1, 'pptPos'),)))
    IActiveIMMIME.GetVirtualKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(UInt32), use_last_error=False)(38, 'GetVirtualKey', ((1, 'hWnd'),(1, 'puVirtualKey'),)))
    IActiveIMMIME.InstallIMEA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.UI.TextServices.HKL), use_last_error=False)(39, 'InstallIMEA', ((1, 'szIMEFileName'),(1, 'szLayoutText'),(1, 'phKL'),)))
    IActiveIMMIME.InstallIMEW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.UI.TextServices.HKL), use_last_error=False)(40, 'InstallIMEW', ((1, 'szIMEFileName'),(1, 'szLayoutText'),(1, 'phKL'),)))
    IActiveIMMIME.IsIME = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL, use_last_error=False)(41, 'IsIME', ((1, 'hKL'),)))
    IActiveIMMIME.IsUIMessageA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM, use_last_error=False)(42, 'IsUIMessageA', ((1, 'hWndIME'),(1, 'msg'),(1, 'wParam'),(1, 'lParam'),)))
    IActiveIMMIME.IsUIMessageW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM, use_last_error=False)(43, 'IsUIMessageW', ((1, 'hWndIME'),(1, 'msg'),(1, 'wParam'),(1, 'lParam'),)))
    IActiveIMMIME.NotifyIME = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,UInt32,UInt32,UInt32, use_last_error=False)(44, 'NotifyIME', ((1, 'hIMC'),(1, 'dwAction'),(1, 'dwIndex'),(1, 'dwValue'),)))
    IActiveIMMIME.RegisterWordA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR, use_last_error=False)(45, 'RegisterWordA', ((1, 'hKL'),(1, 'szReading'),(1, 'dwStyle'),(1, 'szRegister'),)))
    IActiveIMMIME.RegisterWordW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(46, 'RegisterWordW', ((1, 'hKL'),(1, 'szReading'),(1, 'dwStyle'),(1, 'szRegister'),)))
    IActiveIMMIME.ReleaseContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Globalization.HIMC, use_last_error=False)(47, 'ReleaseContext', ((1, 'hWnd'),(1, 'hIMC'),)))
    IActiveIMMIME.SetCandidateWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,POINTER(win32more.UI.Input.Ime.CANDIDATEFORM_head), use_last_error=False)(48, 'SetCandidateWindow', ((1, 'hIMC'),(1, 'pCandidate'),)))
    IActiveIMMIME.SetCompositionFontA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,POINTER(win32more.Graphics.Gdi.LOGFONTA_head), use_last_error=False)(49, 'SetCompositionFontA', ((1, 'hIMC'),(1, 'plf'),)))
    IActiveIMMIME.SetCompositionFontW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,POINTER(win32more.Graphics.Gdi.LOGFONTW_head), use_last_error=False)(50, 'SetCompositionFontW', ((1, 'hIMC'),(1, 'plf'),)))
    IActiveIMMIME.SetCompositionStringA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,UInt32,c_void_p,UInt32,c_void_p,UInt32, use_last_error=False)(51, 'SetCompositionStringA', ((1, 'hIMC'),(1, 'dwIndex'),(1, 'pComp'),(1, 'dwCompLen'),(1, 'pRead'),(1, 'dwReadLen'),)))
    IActiveIMMIME.SetCompositionStringW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,UInt32,c_void_p,UInt32,c_void_p,UInt32, use_last_error=False)(52, 'SetCompositionStringW', ((1, 'hIMC'),(1, 'dwIndex'),(1, 'pComp'),(1, 'dwCompLen'),(1, 'pRead'),(1, 'dwReadLen'),)))
    IActiveIMMIME.SetCompositionWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,POINTER(win32more.UI.Input.Ime.COMPOSITIONFORM_head), use_last_error=False)(53, 'SetCompositionWindow', ((1, 'hIMC'),(1, 'pCompForm'),)))
    IActiveIMMIME.SetConversionStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,UInt32,UInt32, use_last_error=False)(54, 'SetConversionStatus', ((1, 'hIMC'),(1, 'fdwConversion'),(1, 'fdwSentence'),)))
    IActiveIMMIME.SetOpenStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,win32more.Foundation.BOOL, use_last_error=False)(55, 'SetOpenStatus', ((1, 'hIMC'),(1, 'fOpen'),)))
    IActiveIMMIME.SetStatusWindowPos = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,POINTER(win32more.Foundation.POINT_head), use_last_error=False)(56, 'SetStatusWindowPos', ((1, 'hIMC'),(1, 'pptPos'),)))
    IActiveIMMIME.SimulateHotKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32, use_last_error=False)(57, 'SimulateHotKey', ((1, 'hWnd'),(1, 'dwHotKeyID'),)))
    IActiveIMMIME.UnregisterWordA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR, use_last_error=False)(58, 'UnregisterWordA', ((1, 'hKL'),(1, 'szReading'),(1, 'dwStyle'),(1, 'szUnregister'),)))
    IActiveIMMIME.UnregisterWordW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(59, 'UnregisterWordW', ((1, 'hKL'),(1, 'szReading'),(1, 'dwStyle'),(1, 'szUnregister'),)))
    IActiveIMMIME.GenerateMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC, use_last_error=False)(60, 'GenerateMessage', ((1, 'hIMC'),)))
    IActiveIMMIME.LockIMC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,POINTER(POINTER(win32more.UI.Input.Ime.INPUTCONTEXT_head)), use_last_error=False)(61, 'LockIMC', ((1, 'hIMC'),(1, 'ppIMC'),)))
    IActiveIMMIME.UnlockIMC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC, use_last_error=False)(62, 'UnlockIMC', ((1, 'hIMC'),)))
    IActiveIMMIME.GetIMCLockCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,POINTER(UInt32), use_last_error=False)(63, 'GetIMCLockCount', ((1, 'hIMC'),(1, 'pdwLockCount'),)))
    IActiveIMMIME.CreateIMCC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Globalization.HIMCC), use_last_error=False)(64, 'CreateIMCC', ((1, 'dwSize'),(1, 'phIMCC'),)))
    IActiveIMMIME.DestroyIMCC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMCC, use_last_error=False)(65, 'DestroyIMCC', ((1, 'hIMCC'),)))
    IActiveIMMIME.LockIMCC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMCC,POINTER(c_void_p), use_last_error=False)(66, 'LockIMCC', ((1, 'hIMCC'),(1, 'ppv'),)))
    IActiveIMMIME.UnlockIMCC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMCC, use_last_error=False)(67, 'UnlockIMCC', ((1, 'hIMCC'),)))
    IActiveIMMIME.ReSizeIMCC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMCC,UInt32,POINTER(win32more.Globalization.HIMCC), use_last_error=False)(68, 'ReSizeIMCC', ((1, 'hIMCC'),(1, 'dwSize'),(1, 'phIMCC'),)))
    IActiveIMMIME.GetIMCCSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMCC,POINTER(UInt32), use_last_error=False)(69, 'GetIMCCSize', ((1, 'hIMCC'),(1, 'pdwSize'),)))
    IActiveIMMIME.GetIMCCLockCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMCC,POINTER(UInt32), use_last_error=False)(70, 'GetIMCCLockCount', ((1, 'hIMCC'),(1, 'pdwLockCount'),)))
    IActiveIMMIME.GetHotKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(win32more.UI.TextServices.HKL), use_last_error=False)(71, 'GetHotKey', ((1, 'dwHotKeyID'),(1, 'puModifiers'),(1, 'puVKey'),(1, 'phKL'),)))
    IActiveIMMIME.SetHotKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,win32more.UI.TextServices.HKL, use_last_error=False)(72, 'SetHotKey', ((1, 'dwHotKeyID'),(1, 'uModifiers'),(1, 'uVKey'),(1, 'hKL'),)))
    IActiveIMMIME.CreateSoftKeyboard = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.HWND,Int32,Int32,POINTER(win32more.Foundation.HWND), use_last_error=False)(73, 'CreateSoftKeyboard', ((1, 'uType'),(1, 'hOwner'),(1, 'x'),(1, 'y'),(1, 'phSoftKbdWnd'),)))
    IActiveIMMIME.DestroySoftKeyboard = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND, use_last_error=False)(74, 'DestroySoftKeyboard', ((1, 'hSoftKbdWnd'),)))
    IActiveIMMIME.ShowSoftKeyboard = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,Int32, use_last_error=False)(75, 'ShowSoftKeyboard', ((1, 'hSoftKbdWnd'),(1, 'nCmdShow'),)))
    IActiveIMMIME.GetCodePageA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,POINTER(UInt32), use_last_error=False)(76, 'GetCodePageA', ((1, 'hKL'),(1, 'uCodePage'),)))
    IActiveIMMIME.GetLangId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,POINTER(UInt16), use_last_error=False)(77, 'GetLangId', ((1, 'hKL'),(1, 'plid'),)))
    IActiveIMMIME.KeybdEvent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,Byte,Byte,UInt32,UInt32, use_last_error=False)(78, 'KeybdEvent', ((1, 'lgidIME'),(1, 'bVk'),(1, 'bScan'),(1, 'dwFlags'),(1, 'dwExtraInfo'),)))
    IActiveIMMIME.LockModal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(79, 'LockModal', ()))
    IActiveIMMIME.UnlockModal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(80, 'UnlockModal', ()))
    IActiveIMMIME.AssociateContextEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Globalization.HIMC,UInt32, use_last_error=False)(81, 'AssociateContextEx', ((1, 'hWnd'),(1, 'hIMC'),(1, 'dwFlags'),)))
    IActiveIMMIME.DisableIME = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(82, 'DisableIME', ((1, 'idThread'),)))
    IActiveIMMIME.GetImeMenuItemsA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,UInt32,UInt32,POINTER(win32more.UI.Input.Ime.IMEMENUITEMINFOA_head),POINTER(win32more.UI.Input.Ime.IMEMENUITEMINFOA_head),UInt32,POINTER(UInt32), use_last_error=False)(83, 'GetImeMenuItemsA', ((1, 'hIMC'),(1, 'dwFlags'),(1, 'dwType'),(1, 'pImeParentMenu'),(1, 'pImeMenu'),(1, 'dwSize'),(1, 'pdwResult'),)))
    IActiveIMMIME.GetImeMenuItemsW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,UInt32,UInt32,POINTER(win32more.UI.Input.Ime.IMEMENUITEMINFOW_head),POINTER(win32more.UI.Input.Ime.IMEMENUITEMINFOW_head),UInt32,POINTER(UInt32), use_last_error=False)(84, 'GetImeMenuItemsW', ((1, 'hIMC'),(1, 'dwFlags'),(1, 'dwType'),(1, 'pImeParentMenu'),(1, 'pImeMenu'),(1, 'dwSize'),(1, 'pdwResult'),)))
    IActiveIMMIME.EnumInputContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Input.Ime.IEnumInputContext_head), use_last_error=False)(85, 'EnumInputContext', ((1, 'idThread'),(1, 'ppEnum'),)))
    IActiveIMMIME.RequestMessageA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.LRESULT), use_last_error=False)(86, 'RequestMessageA', ((1, 'hIMC'),(1, 'wParam'),(1, 'lParam'),(1, 'plResult'),)))
    IActiveIMMIME.RequestMessageW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.LRESULT), use_last_error=False)(87, 'RequestMessageW', ((1, 'hIMC'),(1, 'wParam'),(1, 'lParam'),(1, 'plResult'),)))
    IActiveIMMIME.SendIMCA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.LRESULT), use_last_error=False)(88, 'SendIMCA', ((1, 'hWnd'),(1, 'uMsg'),(1, 'wParam'),(1, 'lParam'),(1, 'plResult'),)))
    IActiveIMMIME.SendIMCW = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.LRESULT), use_last_error=False)(89, 'SendIMCW', ((1, 'hWnd'),(1, 'uMsg'),(1, 'wParam'),(1, 'lParam'),(1, 'plResult'),)))
    IActiveIMMIME.IsSleeping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(90, 'IsSleeping', ()))
    return IActiveIMMIME
def _define_IActiveIME_head():
    class IActiveIME(win32more.System.Com.IUnknown_head):
        Guid = Guid('6fe20962-d077-11d0-8fe7-00aa006bcc59')
    return IActiveIME
def _define_IActiveIME():
    IActiveIME = win32more.UI.Input.Ime.IActiveIME_head
    IActiveIME.Inquire = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Input.Ime.IMEINFO_head),win32more.Foundation.PWSTR,POINTER(UInt32), use_last_error=False)(3, 'Inquire', ((1, 'dwSystemInfoFlags'),(1, 'pIMEInfo'),(1, 'szWndClass'),(1, 'pdwPrivate'),)))
    IActiveIME.ConversionList = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(win32more.UI.Input.Ime.CANDIDATELIST_head),POINTER(UInt32), use_last_error=False)(4, 'ConversionList', ((1, 'hIMC'),(1, 'szSource'),(1, 'uFlag'),(1, 'uBufLen'),(1, 'pDest'),(1, 'puCopied'),)))
    IActiveIME.Configure = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.TextServices.HKL,win32more.Foundation.HWND,UInt32,POINTER(win32more.UI.Input.Ime.REGISTERWORDW_head), use_last_error=False)(5, 'Configure', ((1, 'hKL'),(1, 'hWnd'),(1, 'dwMode'),(1, 'pRegisterWord'),)))
    IActiveIME.Destroy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'Destroy', ((1, 'uReserved'),)))
    IActiveIME.Escape = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,UInt32,c_void_p,POINTER(win32more.Foundation.LRESULT), use_last_error=False)(7, 'Escape', ((1, 'hIMC'),(1, 'uEscape'),(1, 'pData'),(1, 'plResult'),)))
    IActiveIME.SetActiveContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,win32more.Foundation.BOOL, use_last_error=False)(8, 'SetActiveContext', ((1, 'hIMC'),(1, 'fFlag'),)))
    IActiveIME.ProcessKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,UInt32,UInt32,c_char_p_no, use_last_error=False)(9, 'ProcessKey', ((1, 'hIMC'),(1, 'uVirKey'),(1, 'lParam'),(1, 'pbKeyState'),)))
    IActiveIME.Notify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,UInt32,UInt32,UInt32, use_last_error=False)(10, 'Notify', ((1, 'hIMC'),(1, 'dwAction'),(1, 'dwIndex'),(1, 'dwValue'),)))
    IActiveIME.Select = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,win32more.Foundation.BOOL, use_last_error=False)(11, 'Select', ((1, 'hIMC'),(1, 'fSelect'),)))
    IActiveIME.SetCompositionString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Globalization.HIMC,UInt32,c_void_p,UInt32,c_void_p,UInt32, use_last_error=False)(12, 'SetCompositionString', ((1, 'hIMC'),(1, 'dwIndex'),(1, 'pComp'),(1, 'dwCompLen'),(1, 'pRead'),(1, 'dwReadLen'),)))
    IActiveIME.ToAsciiEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,c_char_p_no,UInt32,win32more.Globalization.HIMC,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(13, 'ToAsciiEx', ((1, 'uVirKey'),(1, 'uScanCode'),(1, 'pbKeyState'),(1, 'fuState'),(1, 'hIMC'),(1, 'pdwTransBuf'),(1, 'puSize'),)))
    IActiveIME.RegisterWord = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(14, 'RegisterWord', ((1, 'szReading'),(1, 'dwStyle'),(1, 'szString'),)))
    IActiveIME.UnregisterWord = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(15, 'UnregisterWord', ((1, 'szReading'),(1, 'dwStyle'),(1, 'szString'),)))
    IActiveIME.GetRegisterWordStyle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.UI.Input.Ime.STYLEBUFW_head),POINTER(UInt32), use_last_error=False)(16, 'GetRegisterWordStyle', ((1, 'nItem'),(1, 'pStyleBuf'),(1, 'puBufSize'),)))
    IActiveIME.EnumRegisterWord = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,c_void_p,POINTER(win32more.UI.Input.Ime.IEnumRegisterWordW_head), use_last_error=False)(17, 'EnumRegisterWord', ((1, 'szReading'),(1, 'dwStyle'),(1, 'szRegister'),(1, 'pData'),(1, 'ppEnum'),)))
    IActiveIME.GetCodePageA = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(18, 'GetCodePageA', ((1, 'uCodePage'),)))
    IActiveIME.GetLangId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt16), use_last_error=False)(19, 'GetLangId', ((1, 'plid'),)))
    return IActiveIME
def _define_IActiveIME2_head():
    class IActiveIME2(win32more.UI.Input.Ime.IActiveIME_head):
        Guid = Guid('e1c4bf0e-2d53-11d2-93e1-0060b067b86e')
    return IActiveIME2
def _define_IActiveIME2():
    IActiveIME2 = win32more.UI.Input.Ime.IActiveIME2_head
    IActiveIME2.Sleep = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(20, 'Sleep', ()))
    IActiveIME2.Unsleep = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(21, 'Unsleep', ((1, 'fDead'),)))
    return IActiveIME2
def _define_ImmInstallIMEA():
    try:
        return WINFUNCTYPE(win32more.UI.TextServices.HKL,win32more.Foundation.PSTR,win32more.Foundation.PSTR, use_last_error=False)(("ImmInstallIMEA", windll["IMM32"]), ((1, 'lpszIMEFileName'),(1, 'lpszLayoutText'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmInstallIMEW():
    try:
        return WINFUNCTYPE(win32more.UI.TextServices.HKL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("ImmInstallIMEW", windll["IMM32"]), ((1, 'lpszIMEFileName'),(1, 'lpszLayoutText'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmInstallIME():
    return win32more.UI.Input.Ime.ImmInstallIMEW
def _define_ImmGetDefaultIMEWnd():
    try:
        return WINFUNCTYPE(win32more.Foundation.HWND,win32more.Foundation.HWND, use_last_error=False)(("ImmGetDefaultIMEWnd", windll["IMM32"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetDescriptionA():
    try:
        return WINFUNCTYPE(UInt32,win32more.UI.TextServices.HKL,POINTER(Byte),UInt32, use_last_error=False)(("ImmGetDescriptionA", windll["IMM32"]), ((1, 'param0'),(1, 'lpszDescription'),(1, 'uBufLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetDescriptionW():
    try:
        return WINFUNCTYPE(UInt32,win32more.UI.TextServices.HKL,POINTER(Char),UInt32, use_last_error=False)(("ImmGetDescriptionW", windll["IMM32"]), ((1, 'param0'),(1, 'lpszDescription'),(1, 'uBufLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetDescription():
    return win32more.UI.Input.Ime.ImmGetDescriptionW
def _define_ImmGetIMEFileNameA():
    try:
        return WINFUNCTYPE(UInt32,win32more.UI.TextServices.HKL,POINTER(Byte),UInt32, use_last_error=False)(("ImmGetIMEFileNameA", windll["IMM32"]), ((1, 'param0'),(1, 'lpszFileName'),(1, 'uBufLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetIMEFileNameW():
    try:
        return WINFUNCTYPE(UInt32,win32more.UI.TextServices.HKL,POINTER(Char),UInt32, use_last_error=False)(("ImmGetIMEFileNameW", windll["IMM32"]), ((1, 'param0'),(1, 'lpszFileName'),(1, 'uBufLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetIMEFileName():
    return win32more.UI.Input.Ime.ImmGetIMEFileNameW
def _define_ImmGetProperty():
    try:
        return WINFUNCTYPE(UInt32,win32more.UI.TextServices.HKL,UInt32, use_last_error=False)(("ImmGetProperty", windll["IMM32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmIsIME():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.TextServices.HKL, use_last_error=False)(("ImmIsIME", windll["IMM32"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmSimulateHotKey():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,UInt32, use_last_error=False)(("ImmSimulateHotKey", windll["IMM32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmCreateContext():
    try:
        return WINFUNCTYPE(win32more.Globalization.HIMC, use_last_error=False)(("ImmCreateContext", windll["IMM32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmDestroyContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Globalization.HIMC, use_last_error=False)(("ImmDestroyContext", windll["IMM32"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetContext():
    try:
        return WINFUNCTYPE(win32more.Globalization.HIMC,win32more.Foundation.HWND, use_last_error=False)(("ImmGetContext", windll["IMM32"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmReleaseContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.Globalization.HIMC, use_last_error=False)(("ImmReleaseContext", windll["IMM32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmAssociateContext():
    try:
        return WINFUNCTYPE(win32more.Globalization.HIMC,win32more.Foundation.HWND,win32more.Globalization.HIMC, use_last_error=False)(("ImmAssociateContext", windll["IMM32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmAssociateContextEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.Globalization.HIMC,UInt32, use_last_error=False)(("ImmAssociateContextEx", windll["IMM32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetCompositionStringA():
    try:
        return WINFUNCTYPE(Int32,win32more.Globalization.HIMC,UInt32,c_void_p,UInt32, use_last_error=False)(("ImmGetCompositionStringA", windll["IMM32"]), ((1, 'param0'),(1, 'param1'),(1, 'lpBuf'),(1, 'dwBufLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetCompositionStringW():
    try:
        return WINFUNCTYPE(Int32,win32more.Globalization.HIMC,UInt32,c_void_p,UInt32, use_last_error=False)(("ImmGetCompositionStringW", windll["IMM32"]), ((1, 'param0'),(1, 'param1'),(1, 'lpBuf'),(1, 'dwBufLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetCompositionString():
    return win32more.UI.Input.Ime.ImmGetCompositionStringW
def _define_ImmSetCompositionStringA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Globalization.HIMC,win32more.UI.Input.Ime.SET_COMPOSITION_STRING_TYPE,c_void_p,UInt32,c_void_p,UInt32, use_last_error=False)(("ImmSetCompositionStringA", windll["IMM32"]), ((1, 'param0'),(1, 'dwIndex'),(1, 'lpComp'),(1, 'dwCompLen'),(1, 'lpRead'),(1, 'dwReadLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmSetCompositionStringW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Globalization.HIMC,win32more.UI.Input.Ime.SET_COMPOSITION_STRING_TYPE,c_void_p,UInt32,c_void_p,UInt32, use_last_error=False)(("ImmSetCompositionStringW", windll["IMM32"]), ((1, 'param0'),(1, 'dwIndex'),(1, 'lpComp'),(1, 'dwCompLen'),(1, 'lpRead'),(1, 'dwReadLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmSetCompositionString():
    return win32more.UI.Input.Ime.ImmSetCompositionStringW
def _define_ImmGetCandidateListCountA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Globalization.HIMC,POINTER(UInt32), use_last_error=False)(("ImmGetCandidateListCountA", windll["IMM32"]), ((1, 'param0'),(1, 'lpdwListCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetCandidateListCountW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Globalization.HIMC,POINTER(UInt32), use_last_error=False)(("ImmGetCandidateListCountW", windll["IMM32"]), ((1, 'param0'),(1, 'lpdwListCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetCandidateListCount():
    return win32more.UI.Input.Ime.ImmGetCandidateListCountW
def _define_ImmGetCandidateListA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Globalization.HIMC,UInt32,POINTER(win32more.UI.Input.Ime.CANDIDATELIST_head),UInt32, use_last_error=False)(("ImmGetCandidateListA", windll["IMM32"]), ((1, 'param0'),(1, 'deIndex'),(1, 'lpCandList'),(1, 'dwBufLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetCandidateListW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Globalization.HIMC,UInt32,POINTER(win32more.UI.Input.Ime.CANDIDATELIST_head),UInt32, use_last_error=False)(("ImmGetCandidateListW", windll["IMM32"]), ((1, 'param0'),(1, 'deIndex'),(1, 'lpCandList'),(1, 'dwBufLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetCandidateList():
    return win32more.UI.Input.Ime.ImmGetCandidateListW
def _define_ImmGetGuideLineA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Globalization.HIMC,win32more.UI.Input.Ime.GET_GUIDE_LINE_TYPE,win32more.Foundation.PSTR,UInt32, use_last_error=False)(("ImmGetGuideLineA", windll["IMM32"]), ((1, 'param0'),(1, 'dwIndex'),(1, 'lpBuf'),(1, 'dwBufLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetGuideLineW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Globalization.HIMC,win32more.UI.Input.Ime.GET_GUIDE_LINE_TYPE,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("ImmGetGuideLineW", windll["IMM32"]), ((1, 'param0'),(1, 'dwIndex'),(1, 'lpBuf'),(1, 'dwBufLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetGuideLine():
    return win32more.UI.Input.Ime.ImmGetGuideLineW
def _define_ImmGetConversionStatus():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Globalization.HIMC,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("ImmGetConversionStatus", windll["IMM32"]), ((1, 'param0'),(1, 'lpfdwConversion'),(1, 'lpfdwSentence'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmSetConversionStatus():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Globalization.HIMC,UInt32,UInt32, use_last_error=False)(("ImmSetConversionStatus", windll["IMM32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetOpenStatus():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Globalization.HIMC, use_last_error=False)(("ImmGetOpenStatus", windll["IMM32"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmSetOpenStatus():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Globalization.HIMC,win32more.Foundation.BOOL, use_last_error=False)(("ImmSetOpenStatus", windll["IMM32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetCompositionFontA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Globalization.HIMC,POINTER(win32more.Graphics.Gdi.LOGFONTA_head), use_last_error=False)(("ImmGetCompositionFontA", windll["IMM32"]), ((1, 'param0'),(1, 'lplf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetCompositionFontW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Globalization.HIMC,POINTER(win32more.Graphics.Gdi.LOGFONTW_head), use_last_error=False)(("ImmGetCompositionFontW", windll["IMM32"]), ((1, 'param0'),(1, 'lplf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetCompositionFont():
    return win32more.UI.Input.Ime.ImmGetCompositionFontW
def _define_ImmSetCompositionFontA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Globalization.HIMC,POINTER(win32more.Graphics.Gdi.LOGFONTA_head), use_last_error=False)(("ImmSetCompositionFontA", windll["IMM32"]), ((1, 'param0'),(1, 'lplf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmSetCompositionFontW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Globalization.HIMC,POINTER(win32more.Graphics.Gdi.LOGFONTW_head), use_last_error=False)(("ImmSetCompositionFontW", windll["IMM32"]), ((1, 'param0'),(1, 'lplf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmSetCompositionFont():
    return win32more.UI.Input.Ime.ImmSetCompositionFontW
def _define_ImmConfigureIMEA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.TextServices.HKL,win32more.Foundation.HWND,UInt32,c_void_p, use_last_error=False)(("ImmConfigureIMEA", windll["IMM32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmConfigureIMEW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.TextServices.HKL,win32more.Foundation.HWND,UInt32,c_void_p, use_last_error=False)(("ImmConfigureIMEW", windll["IMM32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmConfigureIME():
    return win32more.UI.Input.Ime.ImmConfigureIMEW
def _define_ImmEscapeA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LRESULT,win32more.UI.TextServices.HKL,win32more.Globalization.HIMC,UInt32,c_void_p, use_last_error=False)(("ImmEscapeA", windll["IMM32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmEscapeW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LRESULT,win32more.UI.TextServices.HKL,win32more.Globalization.HIMC,UInt32,c_void_p, use_last_error=False)(("ImmEscapeW", windll["IMM32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmEscape():
    return win32more.UI.Input.Ime.ImmEscapeW
def _define_ImmGetConversionListA():
    try:
        return WINFUNCTYPE(UInt32,win32more.UI.TextServices.HKL,win32more.Globalization.HIMC,win32more.Foundation.PSTR,POINTER(win32more.UI.Input.Ime.CANDIDATELIST_head),UInt32,win32more.UI.Input.Ime.GET_CONVERSION_LIST_FLAG, use_last_error=False)(("ImmGetConversionListA", windll["IMM32"]), ((1, 'param0'),(1, 'param1'),(1, 'lpSrc'),(1, 'lpDst'),(1, 'dwBufLen'),(1, 'uFlag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetConversionListW():
    try:
        return WINFUNCTYPE(UInt32,win32more.UI.TextServices.HKL,win32more.Globalization.HIMC,win32more.Foundation.PWSTR,POINTER(win32more.UI.Input.Ime.CANDIDATELIST_head),UInt32,win32more.UI.Input.Ime.GET_CONVERSION_LIST_FLAG, use_last_error=False)(("ImmGetConversionListW", windll["IMM32"]), ((1, 'param0'),(1, 'param1'),(1, 'lpSrc'),(1, 'lpDst'),(1, 'dwBufLen'),(1, 'uFlag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetConversionList():
    return win32more.UI.Input.Ime.ImmGetConversionListW
def _define_ImmNotifyIME():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Globalization.HIMC,win32more.UI.Input.Ime.NOTIFY_IME_ACTION,win32more.UI.Input.Ime.NOTIFY_IME_INDEX,UInt32, use_last_error=False)(("ImmNotifyIME", windll["IMM32"]), ((1, 'param0'),(1, 'dwAction'),(1, 'dwIndex'),(1, 'dwValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetStatusWindowPos():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Globalization.HIMC,POINTER(win32more.Foundation.POINT_head), use_last_error=False)(("ImmGetStatusWindowPos", windll["IMM32"]), ((1, 'param0'),(1, 'lpptPos'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmSetStatusWindowPos():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Globalization.HIMC,POINTER(win32more.Foundation.POINT_head), use_last_error=False)(("ImmSetStatusWindowPos", windll["IMM32"]), ((1, 'param0'),(1, 'lpptPos'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetCompositionWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Globalization.HIMC,POINTER(win32more.UI.Input.Ime.COMPOSITIONFORM_head), use_last_error=False)(("ImmGetCompositionWindow", windll["IMM32"]), ((1, 'param0'),(1, 'lpCompForm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmSetCompositionWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Globalization.HIMC,POINTER(win32more.UI.Input.Ime.COMPOSITIONFORM_head), use_last_error=False)(("ImmSetCompositionWindow", windll["IMM32"]), ((1, 'param0'),(1, 'lpCompForm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetCandidateWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Globalization.HIMC,UInt32,POINTER(win32more.UI.Input.Ime.CANDIDATEFORM_head), use_last_error=False)(("ImmGetCandidateWindow", windll["IMM32"]), ((1, 'param0'),(1, 'param1'),(1, 'lpCandidate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmSetCandidateWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Globalization.HIMC,POINTER(win32more.UI.Input.Ime.CANDIDATEFORM_head), use_last_error=False)(("ImmSetCandidateWindow", windll["IMM32"]), ((1, 'param0'),(1, 'lpCandidate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmIsUIMessageA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM, use_last_error=False)(("ImmIsUIMessageA", windll["IMM32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmIsUIMessageW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM, use_last_error=False)(("ImmIsUIMessageW", windll["IMM32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmIsUIMessage():
    return win32more.UI.Input.Ime.ImmIsUIMessageW
def _define_ImmGetVirtualKey():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HWND, use_last_error=False)(("ImmGetVirtualKey", windll["IMM32"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmRegisterWordA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.TextServices.HKL,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR, use_last_error=False)(("ImmRegisterWordA", windll["IMM32"]), ((1, 'param0'),(1, 'lpszReading'),(1, 'param2'),(1, 'lpszRegister'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmRegisterWordW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.TextServices.HKL,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("ImmRegisterWordW", windll["IMM32"]), ((1, 'param0'),(1, 'lpszReading'),(1, 'param2'),(1, 'lpszRegister'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmRegisterWord():
    return win32more.UI.Input.Ime.ImmRegisterWordW
def _define_ImmUnregisterWordA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.TextServices.HKL,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR, use_last_error=False)(("ImmUnregisterWordA", windll["IMM32"]), ((1, 'param0'),(1, 'lpszReading'),(1, 'param2'),(1, 'lpszUnregister'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmUnregisterWordW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.TextServices.HKL,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("ImmUnregisterWordW", windll["IMM32"]), ((1, 'param0'),(1, 'lpszReading'),(1, 'param2'),(1, 'lpszUnregister'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmUnregisterWord():
    return win32more.UI.Input.Ime.ImmUnregisterWordW
def _define_ImmGetRegisterWordStyleA():
    try:
        return WINFUNCTYPE(UInt32,win32more.UI.TextServices.HKL,UInt32,POINTER(win32more.UI.Input.Ime.STYLEBUFA), use_last_error=False)(("ImmGetRegisterWordStyleA", windll["IMM32"]), ((1, 'param0'),(1, 'nItem'),(1, 'lpStyleBuf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetRegisterWordStyleW():
    try:
        return WINFUNCTYPE(UInt32,win32more.UI.TextServices.HKL,UInt32,POINTER(win32more.UI.Input.Ime.STYLEBUFW), use_last_error=False)(("ImmGetRegisterWordStyleW", windll["IMM32"]), ((1, 'param0'),(1, 'nItem'),(1, 'lpStyleBuf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetRegisterWordStyle():
    return win32more.UI.Input.Ime.ImmGetRegisterWordStyleW
def _define_ImmEnumRegisterWordA():
    try:
        return WINFUNCTYPE(UInt32,win32more.UI.TextServices.HKL,win32more.UI.Input.Ime.REGISTERWORDENUMPROCA,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,c_void_p, use_last_error=False)(("ImmEnumRegisterWordA", windll["IMM32"]), ((1, 'param0'),(1, 'param1'),(1, 'lpszReading'),(1, 'param3'),(1, 'lpszRegister'),(1, 'param5'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmEnumRegisterWordW():
    try:
        return WINFUNCTYPE(UInt32,win32more.UI.TextServices.HKL,win32more.UI.Input.Ime.REGISTERWORDENUMPROCW,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,c_void_p, use_last_error=False)(("ImmEnumRegisterWordW", windll["IMM32"]), ((1, 'param0'),(1, 'param1'),(1, 'lpszReading'),(1, 'param3'),(1, 'lpszRegister'),(1, 'param5'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmEnumRegisterWord():
    return win32more.UI.Input.Ime.ImmEnumRegisterWordW
def _define_ImmDisableIME():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32, use_last_error=False)(("ImmDisableIME", windll["IMM32"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmEnumInputContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.UI.Input.Ime.IMCENUMPROC,win32more.Foundation.LPARAM, use_last_error=False)(("ImmEnumInputContext", windll["IMM32"]), ((1, 'idThread'),(1, 'lpfn'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetImeMenuItemsA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Globalization.HIMC,UInt32,UInt32,POINTER(win32more.UI.Input.Ime.IMEMENUITEMINFOA_head),POINTER(win32more.UI.Input.Ime.IMEMENUITEMINFOA_head),UInt32, use_last_error=False)(("ImmGetImeMenuItemsA", windll["IMM32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'lpImeParentMenu'),(1, 'lpImeMenu'),(1, 'dwSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetImeMenuItemsW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Globalization.HIMC,UInt32,UInt32,POINTER(win32more.UI.Input.Ime.IMEMENUITEMINFOW_head),POINTER(win32more.UI.Input.Ime.IMEMENUITEMINFOW_head),UInt32, use_last_error=False)(("ImmGetImeMenuItemsW", windll["IMM32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'lpImeParentMenu'),(1, 'lpImeMenu'),(1, 'dwSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetImeMenuItems():
    return win32more.UI.Input.Ime.ImmGetImeMenuItemsW
def _define_ImmDisableTextFrameService():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32, use_last_error=False)(("ImmDisableTextFrameService", windll["IMM32"]), ((1, 'idThread'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmDisableLegacyIME():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL, use_last_error=False)(("ImmDisableLegacyIME", windll["IMM32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetHotKey():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(IntPtr), use_last_error=False)(("ImmGetHotKey", windll["IMM32"]), ((1, 'param0'),(1, 'lpuModifiers'),(1, 'lpuVKey'),(1, 'phKL'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmSetHotKey():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,UInt32,UInt32,win32more.UI.TextServices.HKL, use_last_error=False)(("ImmSetHotKey", windll["IMM32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGenerateMessage():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Globalization.HIMC, use_last_error=False)(("ImmGenerateMessage", windll["IMM32"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmRequestMessageA():
    try:
        return WINFUNCTYPE(win32more.Foundation.LRESULT,win32more.Globalization.HIMC,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM, use_last_error=False)(("ImmRequestMessageA", windll["IMM32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmRequestMessageW():
    try:
        return WINFUNCTYPE(win32more.Foundation.LRESULT,win32more.Globalization.HIMC,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM, use_last_error=False)(("ImmRequestMessageW", windll["IMM32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmRequestMessage():
    return win32more.UI.Input.Ime.ImmRequestMessageW
def _define_ImmCreateSoftKeyboard():
    try:
        return WINFUNCTYPE(win32more.Foundation.HWND,UInt32,win32more.Foundation.HWND,Int32,Int32, use_last_error=False)(("ImmCreateSoftKeyboard", windll["IMM32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmDestroySoftKeyboard():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND, use_last_error=False)(("ImmDestroySoftKeyboard", windll["IMM32"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmShowSoftKeyboard():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,Int32, use_last_error=False)(("ImmShowSoftKeyboard", windll["IMM32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmLockIMC():
    try:
        return WINFUNCTYPE(POINTER(win32more.UI.Input.Ime.INPUTCONTEXT_head),win32more.Globalization.HIMC, use_last_error=False)(("ImmLockIMC", windll["IMM32"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmUnlockIMC():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Globalization.HIMC, use_last_error=False)(("ImmUnlockIMC", windll["IMM32"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetIMCLockCount():
    try:
        return WINFUNCTYPE(UInt32,win32more.Globalization.HIMC, use_last_error=False)(("ImmGetIMCLockCount", windll["IMM32"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmCreateIMCC():
    try:
        return WINFUNCTYPE(win32more.Globalization.HIMCC,UInt32, use_last_error=False)(("ImmCreateIMCC", windll["IMM32"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmDestroyIMCC():
    try:
        return WINFUNCTYPE(win32more.Globalization.HIMCC,win32more.Globalization.HIMCC, use_last_error=False)(("ImmDestroyIMCC", windll["IMM32"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmLockIMCC():
    try:
        return WINFUNCTYPE(c_void_p,win32more.Globalization.HIMCC, use_last_error=False)(("ImmLockIMCC", windll["IMM32"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmUnlockIMCC():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Globalization.HIMCC, use_last_error=False)(("ImmUnlockIMCC", windll["IMM32"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetIMCCLockCount():
    try:
        return WINFUNCTYPE(UInt32,win32more.Globalization.HIMCC, use_last_error=False)(("ImmGetIMCCLockCount", windll["IMM32"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmReSizeIMCC():
    try:
        return WINFUNCTYPE(win32more.Globalization.HIMCC,win32more.Globalization.HIMCC,UInt32, use_last_error=False)(("ImmReSizeIMCC", windll["IMM32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImmGetIMCCSize():
    try:
        return WINFUNCTYPE(UInt32,win32more.Globalization.HIMCC, use_last_error=False)(("ImmGetIMCCSize", windll["IMM32"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "CLSID_VERSION_DEPENDENT_MSIME_JAPANESE",
    "IFEC_S_ALREADY_DEFAULT",
    "FELANG_REQ_CONV",
    "FELANG_REQ_RECONV",
    "FELANG_REQ_REV",
    "FELANG_CMODE_MONORUBY",
    "FELANG_CMODE_NOPRUNING",
    "FELANG_CMODE_KATAKANAOUT",
    "FELANG_CMODE_HIRAGANAOUT",
    "FELANG_CMODE_HALFWIDTHOUT",
    "FELANG_CMODE_FULLWIDTHOUT",
    "FELANG_CMODE_BOPOMOFO",
    "FELANG_CMODE_HANGUL",
    "FELANG_CMODE_PINYIN",
    "FELANG_CMODE_PRECONV",
    "FELANG_CMODE_RADICAL",
    "FELANG_CMODE_UNKNOWNREADING",
    "FELANG_CMODE_MERGECAND",
    "FELANG_CMODE_ROMAN",
    "FELANG_CMODE_BESTFIRST",
    "FELANG_CMODE_USENOREVWORDS",
    "FELANG_CMODE_NONE",
    "FELANG_CMODE_PLAURALCLAUSE",
    "FELANG_CMODE_SINGLECONVERT",
    "FELANG_CMODE_AUTOMATIC",
    "FELANG_CMODE_PHRASEPREDICT",
    "FELANG_CMODE_CONVERSATION",
    "FELANG_CMODE_NAME",
    "FELANG_CMODE_NOINVISIBLECHAR",
    "E_NOCAND",
    "E_NOTENOUGH_BUFFER",
    "E_NOTENOUGH_WDD",
    "E_LARGEINPUT",
    "FELANG_CLMN_WBREAK",
    "FELANG_CLMN_NOWBREAK",
    "FELANG_CLMN_PBREAK",
    "FELANG_CLMN_NOPBREAK",
    "FELANG_CLMN_FIXR",
    "FELANG_CLMN_FIXD",
    "FELANG_INVALD_PO",
    "IFED_POS_NONE",
    "IFED_POS_NOUN",
    "IFED_POS_VERB",
    "IFED_POS_ADJECTIVE",
    "IFED_POS_ADJECTIVE_VERB",
    "IFED_POS_ADVERB",
    "IFED_POS_ADNOUN",
    "IFED_POS_CONJUNCTION",
    "IFED_POS_INTERJECTION",
    "IFED_POS_INDEPENDENT",
    "IFED_POS_INFLECTIONALSUFFIX",
    "IFED_POS_PREFIX",
    "IFED_POS_SUFFIX",
    "IFED_POS_AFFIX",
    "IFED_POS_TANKANJI",
    "IFED_POS_IDIOMS",
    "IFED_POS_SYMBOLS",
    "IFED_POS_PARTICLE",
    "IFED_POS_AUXILIARY_VERB",
    "IFED_POS_SUB_VERB",
    "IFED_POS_DEPENDENT",
    "IFED_POS_ALL",
    "IFED_SELECT_NONE",
    "IFED_SELECT_READING",
    "IFED_SELECT_DISPLAY",
    "IFED_SELECT_POS",
    "IFED_SELECT_COMMENT",
    "IFED_SELECT_ALL",
    "IFED_REG_NONE",
    "IFED_REG_USER",
    "IFED_REG_AUTO",
    "IFED_REG_GRAMMAR",
    "IFED_REG_ALL",
    "IFED_TYPE_NONE",
    "IFED_TYPE_GENERAL",
    "IFED_TYPE_NAMEPLACE",
    "IFED_TYPE_SPEECH",
    "IFED_TYPE_REVERSE",
    "IFED_TYPE_ENGLISH",
    "IFED_TYPE_ALL",
    "IFED_S_MORE_ENTRIES",
    "IFED_S_EMPTY_DICTIONARY",
    "IFED_S_WORD_EXISTS",
    "IFED_S_COMMENT_CHANGED",
    "IFED_E_NOT_FOUND",
    "IFED_E_INVALID_FORMAT",
    "IFED_E_OPEN_FAILED",
    "IFED_E_WRITE_FAILED",
    "IFED_E_NO_ENTRY",
    "IFED_E_REGISTER_FAILED",
    "IFED_E_NOT_USER_DIC",
    "IFED_E_NOT_SUPPORTED",
    "IFED_E_USER_COMMENT",
    "IFED_E_REGISTER_ILLEGAL_POS",
    "IFED_E_REGISTER_IMPROPER_WORD",
    "IFED_E_REGISTER_DISCONNECTED",
    "POS_UNDEFINED",
    "JPOS_UNDEFINED",
    "JPOS_MEISHI_FUTSU",
    "JPOS_MEISHI_SAHEN",
    "JPOS_MEISHI_ZAHEN",
    "JPOS_MEISHI_KEIYOUDOUSHI",
    "JPOS_HUKUSIMEISHI",
    "JPOS_MEISA_KEIDOU",
    "JPOS_JINMEI",
    "JPOS_JINMEI_SEI",
    "JPOS_JINMEI_MEI",
    "JPOS_CHIMEI",
    "JPOS_CHIMEI_KUNI",
    "JPOS_CHIMEI_KEN",
    "JPOS_CHIMEI_GUN",
    "JPOS_CHIMEI_KU",
    "JPOS_CHIMEI_SHI",
    "JPOS_CHIMEI_MACHI",
    "JPOS_CHIMEI_MURA",
    "JPOS_CHIMEI_EKI",
    "JPOS_SONOTA",
    "JPOS_SHAMEI",
    "JPOS_SOSHIKI",
    "JPOS_KENCHIKU",
    "JPOS_BUPPIN",
    "JPOS_DAIMEISHI",
    "JPOS_DAIMEISHI_NINSHOU",
    "JPOS_DAIMEISHI_SHIJI",
    "JPOS_KAZU",
    "JPOS_KAZU_SURYOU",
    "JPOS_KAZU_SUSHI",
    "JPOS_5DAN_AWA",
    "JPOS_5DAN_KA",
    "JPOS_5DAN_GA",
    "JPOS_5DAN_SA",
    "JPOS_5DAN_TA",
    "JPOS_5DAN_NA",
    "JPOS_5DAN_BA",
    "JPOS_5DAN_MA",
    "JPOS_5DAN_RA",
    "JPOS_5DAN_AWAUON",
    "JPOS_5DAN_KASOKUON",
    "JPOS_5DAN_RAHEN",
    "JPOS_4DAN_HA",
    "JPOS_1DAN",
    "JPOS_TOKUSHU_KAHEN",
    "JPOS_TOKUSHU_SAHENSURU",
    "JPOS_TOKUSHU_SAHEN",
    "JPOS_TOKUSHU_ZAHEN",
    "JPOS_TOKUSHU_NAHEN",
    "JPOS_KURU_KI",
    "JPOS_KURU_KITA",
    "JPOS_KURU_KITARA",
    "JPOS_KURU_KITARI",
    "JPOS_KURU_KITAROU",
    "JPOS_KURU_KITE",
    "JPOS_KURU_KUREBA",
    "JPOS_KURU_KO",
    "JPOS_KURU_KOI",
    "JPOS_KURU_KOYOU",
    "JPOS_SURU_SA",
    "JPOS_SURU_SI",
    "JPOS_SURU_SITA",
    "JPOS_SURU_SITARA",
    "JPOS_SURU_SIATRI",
    "JPOS_SURU_SITAROU",
    "JPOS_SURU_SITE",
    "JPOS_SURU_SIYOU",
    "JPOS_SURU_SUREBA",
    "JPOS_SURU_SE",
    "JPOS_SURU_SEYO",
    "JPOS_KEIYOU",
    "JPOS_KEIYOU_GARU",
    "JPOS_KEIYOU_GE",
    "JPOS_KEIYOU_ME",
    "JPOS_KEIYOU_YUU",
    "JPOS_KEIYOU_U",
    "JPOS_KEIDOU",
    "JPOS_KEIDOU_NO",
    "JPOS_KEIDOU_TARU",
    "JPOS_KEIDOU_GARU",
    "JPOS_FUKUSHI",
    "JPOS_FUKUSHI_SAHEN",
    "JPOS_FUKUSHI_NI",
    "JPOS_FUKUSHI_NANO",
    "JPOS_FUKUSHI_DA",
    "JPOS_FUKUSHI_TO",
    "JPOS_FUKUSHI_TOSURU",
    "JPOS_RENTAISHI",
    "JPOS_RENTAISHI_SHIJI",
    "JPOS_SETSUZOKUSHI",
    "JPOS_KANDOUSHI",
    "JPOS_SETTOU",
    "JPOS_SETTOU_KAKU",
    "JPOS_SETTOU_SAI",
    "JPOS_SETTOU_FUKU",
    "JPOS_SETTOU_MI",
    "JPOS_SETTOU_DAISHOU",
    "JPOS_SETTOU_KOUTEI",
    "JPOS_SETTOU_CHOUTAN",
    "JPOS_SETTOU_SHINKYU",
    "JPOS_SETTOU_JINMEI",
    "JPOS_SETTOU_CHIMEI",
    "JPOS_SETTOU_SONOTA",
    "JPOS_SETTOU_JOSUSHI",
    "JPOS_SETTOU_TEINEI_O",
    "JPOS_SETTOU_TEINEI_GO",
    "JPOS_SETTOU_TEINEI_ON",
    "JPOS_SETSUBI",
    "JPOS_SETSUBI_TEKI",
    "JPOS_SETSUBI_SEI",
    "JPOS_SETSUBI_KA",
    "JPOS_SETSUBI_CHU",
    "JPOS_SETSUBI_FU",
    "JPOS_SETSUBI_RYU",
    "JPOS_SETSUBI_YOU",
    "JPOS_SETSUBI_KATA",
    "JPOS_SETSUBI_MEISHIRENDAKU",
    "JPOS_SETSUBI_JINMEI",
    "JPOS_SETSUBI_CHIMEI",
    "JPOS_SETSUBI_KUNI",
    "JPOS_SETSUBI_KEN",
    "JPOS_SETSUBI_GUN",
    "JPOS_SETSUBI_KU",
    "JPOS_SETSUBI_SHI",
    "JPOS_SETSUBI_MACHI",
    "JPOS_SETSUBI_CHOU",
    "JPOS_SETSUBI_MURA",
    "JPOS_SETSUBI_SON",
    "JPOS_SETSUBI_EKI",
    "JPOS_SETSUBI_SONOTA",
    "JPOS_SETSUBI_SHAMEI",
    "JPOS_SETSUBI_SOSHIKI",
    "JPOS_SETSUBI_KENCHIKU",
    "JPOS_RENYOU_SETSUBI",
    "JPOS_SETSUBI_JOSUSHI",
    "JPOS_SETSUBI_JOSUSHIPLUS",
    "JPOS_SETSUBI_JIKAN",
    "JPOS_SETSUBI_JIKANPLUS",
    "JPOS_SETSUBI_TEINEI",
    "JPOS_SETSUBI_SAN",
    "JPOS_SETSUBI_KUN",
    "JPOS_SETSUBI_SAMA",
    "JPOS_SETSUBI_DONO",
    "JPOS_SETSUBI_FUKUSU",
    "JPOS_SETSUBI_TACHI",
    "JPOS_SETSUBI_RA",
    "JPOS_TANKANJI",
    "JPOS_TANKANJI_KAO",
    "JPOS_KANYOUKU",
    "JPOS_DOKURITSUGO",
    "JPOS_FUTEIGO",
    "JPOS_KIGOU",
    "JPOS_EIJI",
    "JPOS_KUTEN",
    "JPOS_TOUTEN",
    "JPOS_KANJI",
    "JPOS_OPENBRACE",
    "JPOS_CLOSEBRACE",
    "JPOS_YOKUSEI",
    "JPOS_TANSHUKU",
    "VERSION_ID_JAPANESE",
    "VERSION_ID_KOREAN",
    "VERSION_ID_CHINESE_TRADITIONAL",
    "VERSION_ID_CHINESE_SIMPLIFIED",
    "FID_MSIME_VERSION",
    "VERSION_MOUSE_OPERATION",
    "IMEMOUSERET_NOTHANDLED",
    "IMEMOUSE_VERSION",
    "IMEMOUSE_NONE",
    "IMEMOUSE_LDOWN",
    "IMEMOUSE_RDOWN",
    "IMEMOUSE_MDOWN",
    "IMEMOUSE_WUP",
    "IMEMOUSE_WDOWN",
    "FID_RECONVERT_VERSION",
    "VERSION_RECONVERSION",
    "VERSION_DOCUMENTFEED",
    "VERSION_QUERYPOSITION",
    "VERSION_MODEBIAS",
    "MODEBIAS_GETVERSION",
    "MODEBIAS_SETVALUE",
    "MODEBIAS_GETVALUE",
    "MODEBIASMODE_DEFAULT",
    "MODEBIASMODE_FILENAME",
    "MODEBIASMODE_READING",
    "MODEBIASMODE_DIGIT",
    "SHOWIMEPAD_DEFAULT",
    "SHOWIMEPAD_CATEGORY",
    "SHOWIMEPAD_GUID",
    "FID_MSIME_KMS_VERSION",
    "FID_MSIME_KMS_INIT",
    "FID_MSIME_KMS_TERM",
    "FID_MSIME_KMS_DEL_KEYLIST",
    "FID_MSIME_KMS_NOTIFY",
    "FID_MSIME_KMS_GETMAP",
    "FID_MSIME_KMS_INVOKE",
    "FID_MSIME_KMS_SETMAP",
    "FID_MSIME_KMS_FUNCDESC",
    "FID_MSIME_KMS_GETMAPSEAMLESS",
    "FID_MSIME_KMS_GETMAPFAST",
    "IMEKMS_NOCOMPOSITION",
    "IMEKMS_COMPOSITION",
    "IMEKMS_SELECTION",
    "IMEKMS_IMEOFF",
    "IMEKMS_2NDLEVEL",
    "IMEKMS_INPTGL",
    "IMEKMS_CANDIDATE",
    "IMEKMS_TYPECAND",
    "RECONVOPT_NONE",
    "RECONVOPT_USECANCELNOTIFY",
    "GCSEX_CANCELRECONVERT",
    "STYLE_DESCRIPTION_SIZE",
    "IMEMENUITEM_STRING_SIZE",
    "IMC_GETCANDIDATEPOS",
    "IMC_SETCANDIDATEPOS",
    "IMC_GETCOMPOSITIONFONT",
    "IMC_SETCOMPOSITIONFONT",
    "IMC_GETCOMPOSITIONWINDOW",
    "IMC_SETCOMPOSITIONWINDOW",
    "IMC_GETSTATUSWINDOWPOS",
    "IMC_SETSTATUSWINDOWPOS",
    "IMC_CLOSESTATUSWINDOW",
    "IMC_OPENSTATUSWINDOW",
    "NI_FINALIZECONVERSIONRESULT",
    "ISC_SHOWUICANDIDATEWINDOW",
    "ISC_SHOWUICOMPOSITIONWINDOW",
    "ISC_SHOWUIGUIDELINE",
    "ISC_SHOWUIALLCANDIDATEWINDOW",
    "ISC_SHOWUIALL",
    "MOD_LEFT",
    "MOD_RIGHT",
    "MOD_ON_KEYUP",
    "MOD_IGNORE_ALL_MODIFIER",
    "IME_CHOTKEY_IME_NONIME_TOGGLE",
    "IME_CHOTKEY_SHAPE_TOGGLE",
    "IME_CHOTKEY_SYMBOL_TOGGLE",
    "IME_JHOTKEY_CLOSE_OPEN",
    "IME_KHOTKEY_SHAPE_TOGGLE",
    "IME_KHOTKEY_HANJACONVERT",
    "IME_KHOTKEY_ENGLISH",
    "IME_THOTKEY_IME_NONIME_TOGGLE",
    "IME_THOTKEY_SHAPE_TOGGLE",
    "IME_THOTKEY_SYMBOL_TOGGLE",
    "IME_HOTKEY_DSWITCH_FIRST",
    "IME_HOTKEY_DSWITCH_LAST",
    "IME_HOTKEY_PRIVATE_FIRST",
    "IME_ITHOTKEY_RESEND_RESULTSTR",
    "IME_ITHOTKEY_PREVIOUS_COMPOSITION",
    "IME_ITHOTKEY_UISTYLE_TOGGLE",
    "IME_ITHOTKEY_RECONVERTSTRING",
    "IME_HOTKEY_PRIVATE_LAST",
    "GCS_COMPREADSTR",
    "GCS_COMPREADATTR",
    "GCS_COMPREADCLAUSE",
    "GCS_COMPSTR",
    "GCS_COMPATTR",
    "GCS_COMPCLAUSE",
    "GCS_CURSORPOS",
    "GCS_DELTASTART",
    "GCS_RESULTREADSTR",
    "GCS_RESULTREADCLAUSE",
    "GCS_RESULTSTR",
    "GCS_RESULTCLAUSE",
    "CS_INSERTCHAR",
    "CS_NOMOVECARET",
    "IMEVER_0310",
    "IMEVER_0400",
    "IME_PROP_AT_CARET",
    "IME_PROP_SPECIAL_UI",
    "IME_PROP_CANDLIST_START_FROM_1",
    "IME_PROP_UNICODE",
    "IME_PROP_COMPLETE_ON_UNSELECT",
    "UI_CAP_2700",
    "UI_CAP_ROT90",
    "UI_CAP_ROTANY",
    "SCS_CAP_COMPSTR",
    "SCS_CAP_MAKEREAD",
    "SCS_CAP_SETRECONVERTSTRING",
    "SELECT_CAP_CONVERSION",
    "SELECT_CAP_SENTENCE",
    "GL_LEVEL_NOGUIDELINE",
    "GL_LEVEL_FATAL",
    "GL_LEVEL_ERROR",
    "GL_LEVEL_WARNING",
    "GL_LEVEL_INFORMATION",
    "GL_ID_UNKNOWN",
    "GL_ID_NOMODULE",
    "GL_ID_NODICTIONARY",
    "GL_ID_CANNOTSAVE",
    "GL_ID_NOCONVERT",
    "GL_ID_TYPINGERROR",
    "GL_ID_TOOMANYSTROKE",
    "GL_ID_READINGCONFLICT",
    "GL_ID_INPUTREADING",
    "GL_ID_INPUTRADICAL",
    "GL_ID_INPUTCODE",
    "GL_ID_INPUTSYMBOL",
    "GL_ID_CHOOSECANDIDATE",
    "GL_ID_REVERSECONVERSION",
    "GL_ID_PRIVATE_FIRST",
    "GL_ID_PRIVATE_LAST",
    "ATTR_INPUT",
    "ATTR_TARGET_CONVERTED",
    "ATTR_CONVERTED",
    "ATTR_TARGET_NOTCONVERTED",
    "ATTR_INPUT_ERROR",
    "ATTR_FIXEDCONVERTED",
    "CFS_DEFAULT",
    "CFS_RECT",
    "CFS_POINT",
    "CFS_FORCE_POSITION",
    "CFS_CANDIDATEPOS",
    "CFS_EXCLUDE",
    "IME_CMODE_SOFTKBD",
    "IME_CMODE_NOCONVERSION",
    "IME_CMODE_EUDC",
    "IME_CMODE_SYMBOL",
    "IME_CMODE_FIXED",
    "IME_CMODE_RESERVED",
    "IME_SMODE_NONE",
    "IME_SMODE_PLAURALCLAUSE",
    "IME_SMODE_SINGLECONVERT",
    "IME_SMODE_AUTOMATIC",
    "IME_SMODE_PHRASEPREDICT",
    "IME_SMODE_CONVERSATION",
    "IME_SMODE_RESERVED",
    "IME_CAND_UNKNOWN",
    "IME_CAND_READ",
    "IME_CAND_CODE",
    "IME_CAND_MEANING",
    "IME_CAND_RADICAL",
    "IME_CAND_STROKE",
    "IMN_CLOSESTATUSWINDOW",
    "IMN_OPENSTATUSWINDOW",
    "IMN_CHANGECANDIDATE",
    "IMN_CLOSECANDIDATE",
    "IMN_OPENCANDIDATE",
    "IMN_SETCONVERSIONMODE",
    "IMN_SETSENTENCEMODE",
    "IMN_SETOPENSTATUS",
    "IMN_SETCANDIDATEPOS",
    "IMN_SETCOMPOSITIONFONT",
    "IMN_SETCOMPOSITIONWINDOW",
    "IMN_SETSTATUSWINDOWPOS",
    "IMN_GUIDELINE",
    "IMN_PRIVATE",
    "IMR_COMPOSITIONWINDOW",
    "IMR_CANDIDATEWINDOW",
    "IMR_COMPOSITIONFONT",
    "IMR_RECONVERTSTRING",
    "IMR_CONFIRMRECONVERTSTRING",
    "IMR_QUERYCHARPOSITION",
    "IMR_DOCUMENTFEED",
    "IMM_ERROR_NODATA",
    "IMM_ERROR_GENERAL",
    "IME_CONFIG_GENERAL",
    "IME_CONFIG_REGISTERWORD",
    "IME_CONFIG_SELECTDICTIONARY",
    "IME_ESC_QUERY_SUPPORT",
    "IME_ESC_RESERVED_FIRST",
    "IME_ESC_RESERVED_LAST",
    "IME_ESC_PRIVATE_FIRST",
    "IME_ESC_PRIVATE_LAST",
    "IME_ESC_SEQUENCE_TO_INTERNAL",
    "IME_ESC_GET_EUDC_DICTIONARY",
    "IME_ESC_SET_EUDC_DICTIONARY",
    "IME_ESC_MAX_KEY",
    "IME_ESC_IME_NAME",
    "IME_ESC_SYNC_HOTKEY",
    "IME_ESC_HANJA_MODE",
    "IME_ESC_AUTOMATA",
    "IME_ESC_PRIVATE_HOTKEY",
    "IME_ESC_GETHELPFILENAME",
    "IME_REGWORD_STYLE_EUDC",
    "IME_REGWORD_STYLE_USER_FIRST",
    "IME_REGWORD_STYLE_USER_LAST",
    "IACE_CHILDREN",
    "IACE_DEFAULT",
    "IACE_IGNORENOCONTEXT",
    "IGIMIF_RIGHTMENU",
    "IGIMII_CMODE",
    "IGIMII_SMODE",
    "IGIMII_CONFIGURE",
    "IGIMII_TOOLS",
    "IGIMII_HELP",
    "IGIMII_OTHER",
    "IGIMII_INPUTTOOLS",
    "IMFT_RADIOCHECK",
    "IMFT_SEPARATOR",
    "IMFT_SUBMENU",
    "SOFTKEYBOARD_TYPE_T1",
    "SOFTKEYBOARD_TYPE_C1",
    "IMMGWL_IMC",
    "IMMGWLP_IMC",
    "IMC_SETCONVERSIONMODE",
    "IMC_SETSENTENCEMODE",
    "IMC_SETOPENSTATUS",
    "IMC_GETSOFTKBDFONT",
    "IMC_SETSOFTKBDFONT",
    "IMC_GETSOFTKBDPOS",
    "IMC_SETSOFTKBDPOS",
    "IMC_GETSOFTKBDSUBTYPE",
    "IMC_SETSOFTKBDSUBTYPE",
    "IMC_SETSOFTKBDDATA",
    "NI_CONTEXTUPDATED",
    "IME_SYSINFO_WINLOGON",
    "IME_SYSINFO_WOW16",
    "INIT_STATUSWNDPOS",
    "INIT_CONVERSION",
    "INIT_SENTENCE",
    "INIT_LOGFONT",
    "INIT_COMPFORM",
    "INIT_SOFTKBDPOS",
    "IME_PROP_END_UNLOAD",
    "IME_PROP_KBD_CHAR_FIRST",
    "IME_PROP_IGNORE_UPKEYS",
    "IME_PROP_NEED_ALTKEY",
    "IME_PROP_NO_KEYS_ON_CLOSE",
    "IME_PROP_ACCEPT_WIDE_VKEY",
    "UI_CAP_SOFTKBD",
    "IMN_SOFTKBDDESTROYED",
    "IME_UI_CLASS_NAME_SIZE",
    "IME_ESC_STRING_BUFFER_SIZE",
    "CATID_MSIME_IImePadApplet_VER7",
    "CATID_MSIME_IImePadApplet_VER80",
    "CATID_MSIME_IImePadApplet_VER81",
    "CATID_MSIME_IImePadApplet900",
    "CATID_MSIME_IImePadApplet1000",
    "CATID_MSIME_IImePadApplet1200",
    "CATID_MSIME_IImePadApplet",
    "FEID_NONE",
    "FEID_CHINESE_TRADITIONAL",
    "FEID_CHINESE_SIMPLIFIED",
    "FEID_CHINESE_HONGKONG",
    "FEID_CHINESE_SINGAPORE",
    "FEID_JAPANESE",
    "FEID_KOREAN",
    "FEID_KOREAN_JOHAB",
    "INFOMASK_NONE",
    "INFOMASK_QUERY_CAND",
    "INFOMASK_APPLY_CAND",
    "INFOMASK_APPLY_CAND_EX",
    "INFOMASK_STRING_FIX",
    "INFOMASK_HIDE_CAND",
    "INFOMASK_BLOCK_CAND",
    "IMEFAREASTINFO_TYPE_DEFAULT",
    "IMEFAREASTINFO_TYPE_READING",
    "IMEFAREASTINFO_TYPE_COMMENT",
    "IMEFAREASTINFO_TYPE_COSTTIME",
    "CHARINFO_APPLETID_MASK",
    "CHARINFO_FEID_MASK",
    "CHARINFO_CHARID_MASK",
    "MAX_APPLETTITLE",
    "MAX_FONTFACE",
    "IPACFG_NONE",
    "IPACFG_PROPERTY",
    "IPACFG_HELP",
    "IPACFG_TITLE",
    "IPACFG_TITLEFONTFACE",
    "IPACFG_CATEGORY",
    "IPACFG_LANG",
    "IPACID_NONE",
    "IPACID_SOFTKEY",
    "IPACID_HANDWRITING",
    "IPACID_STROKESEARCH",
    "IPACID_RADICALSEARCH",
    "IPACID_SYMBOLSEARCH",
    "IPACID_VOICE",
    "IPACID_EPWING",
    "IPACID_OCR",
    "IPACID_CHARLIST",
    "IPACID_USER",
    "IMEPADREQ_FIRST",
    "IMEPADREQ_INSERTSTRINGCANDIDATE",
    "IMEPADREQ_INSERTITEMCANDIDATE",
    "IMEPADREQ_SENDKEYCONTROL",
    "IMEPADREQ_GETSELECTEDSTRING",
    "IMEPADREQ_SETAPPLETDATA",
    "IMEPADREQ_GETAPPLETDATA",
    "IMEPADREQ_SETTITLEFONT",
    "IMEPADREQ_GETCOMPOSITIONSTRINGID",
    "IMEPADREQ_INSERTSTRINGCANDIDATEINFO",
    "IMEPADREQ_CHANGESTRINGCANDIDATEINFO",
    "IMEPADREQ_INSERTSTRINGINFO",
    "IMEPADREQ_CHANGESTRINGINFO",
    "IMEPADREQ_GETCURRENTUILANGID",
    "IMEPADCTRL_CONVERTALL",
    "IMEPADCTRL_DETERMINALL",
    "IMEPADCTRL_DETERMINCHAR",
    "IMEPADCTRL_CLEARALL",
    "IMEPADCTRL_CARETSET",
    "IMEPADCTRL_CARETLEFT",
    "IMEPADCTRL_CARETRIGHT",
    "IMEPADCTRL_CARETTOP",
    "IMEPADCTRL_CARETBOTTOM",
    "IMEPADCTRL_CARETBACKSPACE",
    "IMEPADCTRL_CARETDELETE",
    "IMEPADCTRL_PHRASEDELETE",
    "IMEPADCTRL_INSERTSPACE",
    "IMEPADCTRL_INSERTFULLSPACE",
    "IMEPADCTRL_INSERTHALFSPACE",
    "IMEPADCTRL_ONIME",
    "IMEPADCTRL_OFFIME",
    "IMEPADCTRL_ONPRECONVERSION",
    "IMEPADCTRL_OFFPRECONVERSION",
    "IMEPADCTRL_PHONETICCANDIDATE",
    "IMEKEYCTRLMASK_ALT",
    "IMEKEYCTRLMASK_CTRL",
    "IMEKEYCTRLMASK_SHIFT",
    "IMEKEYCTRL_UP",
    "IMEKEYCTRL_DOWN",
    "IMEPN_FIRST",
    "IMEPN_ACTIVATE",
    "IMEPN_INACTIVATE",
    "IMEPN_SHOW",
    "IMEPN_HIDE",
    "IMEPN_SIZECHANGING",
    "IMEPN_SIZECHANGED",
    "IMEPN_CONFIG",
    "IMEPN_HELP",
    "IMEPN_QUERYCAND",
    "IMEPN_APPLYCAND",
    "IMEPN_APPLYCANDEX",
    "IMEPN_SETTINGCHANGED",
    "IMEPN_USER",
    "IPAWS_ENABLED",
    "IPAWS_SIZINGNOTIFY",
    "IPAWS_VERTICALFIXED",
    "IPAWS_HORIZONTALFIXED",
    "IPAWS_SIZEFIXED",
    "IPAWS_MAXWIDTHFIXED",
    "IPAWS_MAXHEIGHTFIXED",
    "IPAWS_MAXSIZEFIXED",
    "IPAWS_MINWIDTHFIXED",
    "IPAWS_MINHEIGHTFIXED",
    "IPAWS_MINSIZEFIXED",
    "CLSID_ImePlugInDictDictionaryList_CHS",
    "CLSID_ImePlugInDictDictionaryList_JPN",
    "SET_COMPOSITION_STRING_TYPE",
    "SCS_SETSTR",
    "SCS_CHANGEATTR",
    "SCS_CHANGECLAUSE",
    "SCS_SETRECONVERTSTRING",
    "SCS_QUERYRECONVERTSTRING",
    "GET_GUIDE_LINE_TYPE",
    "GGL_LEVEL",
    "GGL_INDEX",
    "GGL_STRING",
    "GGL_PRIVATE",
    "NOTIFY_IME_INDEX",
    "CPS_CANCEL",
    "CPS_COMPLETE",
    "CPS_CONVERT",
    "CPS_REVERT",
    "NOTIFY_IME_ACTION",
    "NI_CHANGECANDIDATELIST",
    "NI_CLOSECANDIDATE",
    "NI_COMPOSITIONSTR",
    "NI_IMEMENUSELECTED",
    "NI_OPENCANDIDATE",
    "NI_SELECTCANDIDATESTR",
    "NI_SETCANDIDATE_PAGESIZE",
    "NI_SETCANDIDATE_PAGESTART",
    "GET_CONVERSION_LIST_FLAG",
    "GCL_CONVERSION",
    "GCL_REVERSECONVERSION",
    "GCL_REVERSE_LENGTH",
    "IME_PAD_REQUEST_FLAGS",
    "IMEPADREQ_INSERTSTRING",
    "IMEPADREQ_SENDCONTROL",
    "IMEPADREQ_SETAPPLETSIZE",
    "IMEPADREQ_GETCOMPOSITIONSTRING",
    "IMEPADREQ_GETCOMPOSITIONSTRINGINFO",
    "IMEPADREQ_DELETESTRING",
    "IMEPADREQ_CHANGESTRING",
    "IMEPADREQ_GETAPPLHWND",
    "IMEPADREQ_FORCEIMEPADWINDOWSHOW",
    "IMEPADREQ_POSTMODALNOTIFY",
    "IMEPADREQ_GETDEFAULTUILANGID",
    "IMEPADREQ_GETAPPLETUISTYLE",
    "IMEPADREQ_SETAPPLETUISTYLE",
    "IMEPADREQ_ISAPPLETACTIVE",
    "IMEPADREQ_ISIMEPADWINDOWVISIBLE",
    "IMEPADREQ_SETAPPLETMINMAXSIZE",
    "IMEPADREQ_GETCONVERSIONSTATUS",
    "IMEPADREQ_GETVERSION",
    "IMEPADREQ_GETCURRENTIMEINFO",
    "COMPOSITIONFORM",
    "CANDIDATEFORM",
    "CANDIDATELIST",
    "REGISTERWORDA",
    "REGISTERWORDW",
    "RECONVERTSTRING",
    "STYLEBUFA",
    "STYLEBUFW",
    "IMEMENUITEMINFOA",
    "IMEMENUITEMINFOW",
    "IMECHARPOSITION",
    "IMCENUMPROC",
    "REGISTERWORDENUMPROCA",
    "REGISTERWORDENUMPROCW",
    "IFEClassFactory",
    "IMEDLG",
    "IFECommon",
    "WDD",
    "MORRSLT",
    "IFELanguage",
    "IMEREG",
    "IFED_REG_HEAD",
    "IFED_REG_TAIL",
    "IFED_REG_DEL",
    "IMEFMT",
    "IFED_UNKNOWN",
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
    "IFED_MSIME98_TEXT_USER",
    "IFED_ACTIVE_DICT",
    "IFED_ATOK9",
    "IFED_ATOK10",
    "IFED_NEC_AI_",
    "IFED_WX_II",
    "IFED_WX_III",
    "IFED_VJE_20",
    "IFED_MSIME98_SYSTEM_CE",
    "IFED_MSIME_BIN_SYSTEM",
    "IFED_MSIME_BIN_USER",
    "IFED_MSIME_TEXT_USER",
    "IFED_PIME2_BIN_USER",
    "IFED_PIME2_BIN_SYSTEM",
    "IFED_PIME2_BIN_STANDARD_SYSTEM",
    "IMEUCT",
    "IFED_UCT_NONE",
    "IFED_UCT_STRING_SJIS",
    "IFED_UCT_STRING_UNICODE",
    "IFED_UCT_USER_DEFINED",
    "IFED_UCT_MAX",
    "IMEWRD",
    "IMESHF",
    "POSTBL",
    "IMEREL",
    "IFED_REL_NONE",
    "IFED_REL_NO",
    "IFED_REL_GA",
    "IFED_REL_WO",
    "IFED_REL_NI",
    "IFED_REL_DE",
    "IFED_REL_YORI",
    "IFED_REL_KARA",
    "IFED_REL_MADE",
    "IFED_REL_HE",
    "IFED_REL_TO",
    "IFED_REL_IDEOM",
    "IFED_REL_FUKU_YOUGEN",
    "IFED_REL_KEIYOU_YOUGEN",
    "IFED_REL_KEIDOU1_YOUGEN",
    "IFED_REL_KEIDOU2_YOUGEN",
    "IFED_REL_TAIGEN",
    "IFED_REL_YOUGEN",
    "IFED_REL_RENTAI_MEI",
    "IFED_REL_RENSOU",
    "IFED_REL_KEIYOU_TO_YOUGEN",
    "IFED_REL_KEIYOU_TARU_YOUGEN",
    "IFED_REL_UNKNOWN1",
    "IFED_REL_UNKNOWN2",
    "IFED_REL_ALL",
    "IMEDP",
    "PFNLOG",
    "IFEDictionary",
    "IMEKMSINIT",
    "IMEKMSKEY",
    "IMEKMS",
    "IMEKMSNTFY",
    "IMEKMSKMP",
    "IMEKMSINVK",
    "IMEKMSFUNCDESC",
    "fpCreateIFECommonInstanceType",
    "fpCreateIFELanguageInstanceType",
    "fpCreateIFEDictionaryInstanceType",
    "COMPOSITIONSTRING",
    "GUIDELINE",
    "TRANSMSG",
    "TRANSMSGLIST",
    "CANDIDATEINFO",
    "INPUTCONTEXT",
    "IMEINFO",
    "SOFTKBDDATA",
    "APPLETIDLIST",
    "IMESTRINGCANDIDATE",
    "IMEITEM",
    "IMEITEMCANDIDATE",
    "tabIMESTRINGINFO",
    "tabIMEFAREASTINFO",
    "IMESTRINGCANDIDATEINFO",
    "IMECOMPOSITIONSTRINGINFO",
    "IMECHARINFO",
    "IMEAPPLETCFG",
    "IMEAPPLETUI",
    "APPLYCANDEXPARAM",
    "IImeSpecifyApplets",
    "IImePadApplet",
    "IImePad",
    "IImePlugInDictDictionaryList",
    "CActiveIMM",
    "IEnumRegisterWordA",
    "IEnumRegisterWordW",
    "IEnumInputContext",
    "IActiveIMMRegistrar",
    "IActiveIMMMessagePumpOwner",
    "IActiveIMMApp",
    "IActiveIMMIME",
    "IActiveIME",
    "IActiveIME2",
    "ImmInstallIMEA",
    "ImmInstallIMEW",
    "ImmInstallIME",
    "ImmGetDefaultIMEWnd",
    "ImmGetDescriptionA",
    "ImmGetDescriptionW",
    "ImmGetDescription",
    "ImmGetIMEFileNameA",
    "ImmGetIMEFileNameW",
    "ImmGetIMEFileName",
    "ImmGetProperty",
    "ImmIsIME",
    "ImmSimulateHotKey",
    "ImmCreateContext",
    "ImmDestroyContext",
    "ImmGetContext",
    "ImmReleaseContext",
    "ImmAssociateContext",
    "ImmAssociateContextEx",
    "ImmGetCompositionStringA",
    "ImmGetCompositionStringW",
    "ImmGetCompositionString",
    "ImmSetCompositionStringA",
    "ImmSetCompositionStringW",
    "ImmSetCompositionString",
    "ImmGetCandidateListCountA",
    "ImmGetCandidateListCountW",
    "ImmGetCandidateListCount",
    "ImmGetCandidateListA",
    "ImmGetCandidateListW",
    "ImmGetCandidateList",
    "ImmGetGuideLineA",
    "ImmGetGuideLineW",
    "ImmGetGuideLine",
    "ImmGetConversionStatus",
    "ImmSetConversionStatus",
    "ImmGetOpenStatus",
    "ImmSetOpenStatus",
    "ImmGetCompositionFontA",
    "ImmGetCompositionFontW",
    "ImmGetCompositionFont",
    "ImmSetCompositionFontA",
    "ImmSetCompositionFontW",
    "ImmSetCompositionFont",
    "ImmConfigureIMEA",
    "ImmConfigureIMEW",
    "ImmConfigureIME",
    "ImmEscapeA",
    "ImmEscapeW",
    "ImmEscape",
    "ImmGetConversionListA",
    "ImmGetConversionListW",
    "ImmGetConversionList",
    "ImmNotifyIME",
    "ImmGetStatusWindowPos",
    "ImmSetStatusWindowPos",
    "ImmGetCompositionWindow",
    "ImmSetCompositionWindow",
    "ImmGetCandidateWindow",
    "ImmSetCandidateWindow",
    "ImmIsUIMessageA",
    "ImmIsUIMessageW",
    "ImmIsUIMessage",
    "ImmGetVirtualKey",
    "ImmRegisterWordA",
    "ImmRegisterWordW",
    "ImmRegisterWord",
    "ImmUnregisterWordA",
    "ImmUnregisterWordW",
    "ImmUnregisterWord",
    "ImmGetRegisterWordStyleA",
    "ImmGetRegisterWordStyleW",
    "ImmGetRegisterWordStyle",
    "ImmEnumRegisterWordA",
    "ImmEnumRegisterWordW",
    "ImmEnumRegisterWord",
    "ImmDisableIME",
    "ImmEnumInputContext",
    "ImmGetImeMenuItemsA",
    "ImmGetImeMenuItemsW",
    "ImmGetImeMenuItems",
    "ImmDisableTextFrameService",
    "ImmDisableLegacyIME",
    "ImmGetHotKey",
    "ImmSetHotKey",
    "ImmGenerateMessage",
    "ImmRequestMessageA",
    "ImmRequestMessageW",
    "ImmRequestMessage",
    "ImmCreateSoftKeyboard",
    "ImmDestroySoftKeyboard",
    "ImmShowSoftKeyboard",
    "ImmLockIMC",
    "ImmUnlockIMC",
    "ImmGetIMCLockCount",
    "ImmCreateIMCC",
    "ImmDestroyIMCC",
    "ImmLockIMCC",
    "ImmUnlockIMCC",
    "ImmGetIMCCLockCount",
    "ImmReSizeIMCC",
    "ImmGetIMCCSize",
]
