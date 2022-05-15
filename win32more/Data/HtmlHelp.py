from win32more import *
import win32more.Data.HtmlHelp
import win32more.Foundation
import win32more.System.Com
import win32more.System.Search
import win32more.UI.Controls

def __getattr__(name):
    if f"_define_{name}" not in globals():
        raise AttributeError()
    setattr(win32more.Data.HtmlHelp, name, globals()[f"_define_{name}"]())
    return getattr(win32more.Data.HtmlHelp, name)
def __dir__():
    return __all__
HH_DISPLAY_TOPIC = 0
HH_HELP_FINDER = 0
HH_DISPLAY_TOC = 1
HH_DISPLAY_INDEX = 2
HH_DISPLAY_SEARCH = 3
HH_SET_WIN_TYPE = 4
HH_GET_WIN_TYPE = 5
HH_GET_WIN_HANDLE = 6
HH_ENUM_INFO_TYPE = 7
HH_SET_INFO_TYPE = 8
HH_SYNC = 9
HH_RESERVED1 = 10
HH_RESERVED2 = 11
HH_RESERVED3 = 12
HH_KEYWORD_LOOKUP = 13
HH_DISPLAY_TEXT_POPUP = 14
HH_HELP_CONTEXT = 15
HH_TP_HELP_CONTEXTMENU = 16
HH_TP_HELP_WM_HELP = 17
HH_CLOSE_ALL = 18
HH_ALINK_LOOKUP = 19
HH_GET_LAST_ERROR = 20
HH_ENUM_CATEGORY = 21
HH_ENUM_CATEGORY_IT = 22
HH_RESET_IT_FILTER = 23
HH_SET_INCLUSIVE_FILTER = 24
HH_SET_EXCLUSIVE_FILTER = 25
HH_INITIALIZE = 28
HH_UNINITIALIZE = 29
HH_SET_QUERYSERVICE = 30
HH_PRETRANSLATEMESSAGE = 253
HH_SET_GLOBAL_PROPERTY = 252
HH_SAFE_DISPLAY_TOPIC = 32
HHWIN_PROP_TAB_AUTOHIDESHOW = 1
HHWIN_PROP_ONTOP = 2
HHWIN_PROP_NOTITLEBAR = 4
HHWIN_PROP_NODEF_STYLES = 8
HHWIN_PROP_NODEF_EXSTYLES = 16
HHWIN_PROP_TRI_PANE = 32
HHWIN_PROP_NOTB_TEXT = 64
HHWIN_PROP_POST_QUIT = 128
HHWIN_PROP_AUTO_SYNC = 256
HHWIN_PROP_TRACKING = 512
HHWIN_PROP_TAB_SEARCH = 1024
HHWIN_PROP_TAB_HISTORY = 2048
HHWIN_PROP_TAB_FAVORITES = 4096
HHWIN_PROP_CHANGE_TITLE = 8192
HHWIN_PROP_NAV_ONLY_WIN = 16384
HHWIN_PROP_NO_TOOLBAR = 32768
HHWIN_PROP_MENU = 65536
HHWIN_PROP_TAB_ADVSEARCH = 131072
HHWIN_PROP_USER_POS = 262144
HHWIN_PROP_TAB_CUSTOM1 = 524288
HHWIN_PROP_TAB_CUSTOM2 = 1048576
HHWIN_PROP_TAB_CUSTOM3 = 2097152
HHWIN_PROP_TAB_CUSTOM4 = 4194304
HHWIN_PROP_TAB_CUSTOM5 = 8388608
HHWIN_PROP_TAB_CUSTOM6 = 16777216
HHWIN_PROP_TAB_CUSTOM7 = 33554432
HHWIN_PROP_TAB_CUSTOM8 = 67108864
HHWIN_PROP_TAB_CUSTOM9 = 134217728
HHWIN_TB_MARGIN = 268435456
HHWIN_PARAM_PROPERTIES = 2
HHWIN_PARAM_STYLES = 4
HHWIN_PARAM_EXSTYLES = 8
HHWIN_PARAM_RECT = 16
HHWIN_PARAM_NAV_WIDTH = 32
HHWIN_PARAM_SHOWSTATE = 64
HHWIN_PARAM_INFOTYPES = 128
HHWIN_PARAM_TB_FLAGS = 256
HHWIN_PARAM_EXPANSION = 512
HHWIN_PARAM_TABPOS = 1024
HHWIN_PARAM_TABORDER = 2048
HHWIN_PARAM_HISTORY_COUNT = 4096
HHWIN_PARAM_CUR_TAB = 8192
HHWIN_BUTTON_EXPAND = 2
HHWIN_BUTTON_BACK = 4
HHWIN_BUTTON_FORWARD = 8
HHWIN_BUTTON_STOP = 16
HHWIN_BUTTON_REFRESH = 32
HHWIN_BUTTON_HOME = 64
HHWIN_BUTTON_BROWSE_FWD = 128
HHWIN_BUTTON_BROWSE_BCK = 256
HHWIN_BUTTON_NOTES = 512
HHWIN_BUTTON_CONTENTS = 1024
HHWIN_BUTTON_SYNC = 2048
HHWIN_BUTTON_OPTIONS = 4096
HHWIN_BUTTON_PRINT = 8192
HHWIN_BUTTON_INDEX = 16384
HHWIN_BUTTON_SEARCH = 32768
HHWIN_BUTTON_HISTORY = 65536
HHWIN_BUTTON_FAVORITES = 131072
HHWIN_BUTTON_JUMP1 = 262144
HHWIN_BUTTON_JUMP2 = 524288
HHWIN_BUTTON_ZOOM = 1048576
HHWIN_BUTTON_TOC_NEXT = 2097152
HHWIN_BUTTON_TOC_PREV = 4194304
IDTB_EXPAND = 200
IDTB_CONTRACT = 201
IDTB_STOP = 202
IDTB_REFRESH = 203
IDTB_BACK = 204
IDTB_HOME = 205
IDTB_SYNC = 206
IDTB_PRINT = 207
IDTB_OPTIONS = 208
IDTB_FORWARD = 209
IDTB_NOTES = 210
IDTB_BROWSE_FWD = 211
IDTB_BROWSE_BACK = 212
IDTB_CONTENTS = 213
IDTB_INDEX = 214
IDTB_SEARCH = 215
IDTB_HISTORY = 216
IDTB_FAVORITES = 217
IDTB_JUMP1 = 218
IDTB_JUMP2 = 219
IDTB_CUSTOMIZE = 221
IDTB_ZOOM = 222
IDTB_TOC_NEXT = 223
IDTB_TOC_PREV = 224
HH_MAX_TABS = 19
HH_FTS_DEFAULT_PROXIMITY = -1
CLSID_IITPropList = '4662daae-d393-11d0-9a56-00c04fb68bf7'
PROP_ADD = 0
PROP_DELETE = 1
PROP_UPDATE = 2
TYPE_VALUE = 0
TYPE_POINTER = 1
TYPE_STRING = 2
CLSID_IITDatabase = '66673452-8c23-11d0-a84e-00aa006c7d01'
CLSID_IITDatabaseLocal = '4662daa9-d393-11d0-9a56-00c04fb68bf7'
STDPROP_UID = 1
STDPROP_TITLE = 2
STDPROP_USERDATA = 3
STDPROP_KEY = 4
STDPROP_SORTKEY = 100
STDPROP_DISPLAYKEY = 101
STDPROP_SORTORDINAL = 102
STDPROP_INDEX_TEXT = 200
STDPROP_INDEX_VFLD = 201
STDPROP_INDEX_DTYPE = 202
STDPROP_INDEX_LENGTH = 203
STDPROP_INDEX_BREAK = 204
STDPROP_INDEX_TERM = 210
STDPROP_INDEX_TERM_RAW_LENGTH = 211
STDPROP_USERPROP_BASE = 65536
STDPROP_USERPROP_MAX = 2147483647
CLSID_IITCmdInt = '4662daa2-d393-11d0-9a56-00c04fb68bf7'
CLSID_IITSvMgr = '4662daa3-d393-11d0-9a56-00c04fb68bf7'
CLSID_IITWordWheelUpdate = '4662daa5-d393-11d0-9a56-00c04fb68bf7'
CLSID_IITGroupUpdate = '4662daa4-d393-11d0-9a56-00c04fb68bf7'
CLSID_IITIndexBuild = '8fa0d5aa-dedf-11d0-9a61-00c04fb68bf7'
CLSID_IITWWFilterBuild = '8fa0d5ab-dedf-11d0-9a61-00c04fb68bf7'
CLSID_IITWordWheel = 'd73725c2-8c12-11d0-a84e-00aa006c7d01'
CLSID_IITWordWheelLocal = '4662daa8-d393-11d0-9a56-00c04fb68bf7'
ITWW_OPEN_NOCONNECT = 1
ITWW_CBKEY_MAX = 1024
IITWBC_BREAK_ACCEPT_WILDCARDS = 1
IITWBC_BREAK_AND_STEM = 2
E_NOTEXIST = -2147479552
E_DUPLICATE = -2147479551
E_BADVERSION = -2147479550
E_BADFILE = -2147479549
E_BADFORMAT = -2147479548
E_NOPERMISSION = -2147479547
E_ASSERT = -2147479546
E_INTERRUPT = -2147479545
E_NOTSUPPORTED = -2147479544
E_OUTOFRANGE = -2147479543
E_GROUPIDTOOBIG = -2147479542
E_TOOMANYTITLES = -2147479541
E_NOMERGEDDATA = -2147479540
E_NOTFOUND = -2147479539
E_CANTFINDDLL = -2147479538
E_NOHANDLE = -2147479537
E_GETLASTERROR = -2147479536
E_BADPARAM = -2147479535
E_INVALIDSTATE = -2147479534
E_NOTOPEN = -2147479533
E_ALREADYOPEN = -2147479533
E_UNKNOWN_TRANSPORT = -2147479530
E_UNSUPPORTED_TRANSPORT = -2147479529
E_BADFILTERSIZE = -2147479528
E_TOOMANYOBJECTS = -2147479527
E_NAMETOOLONG = -2147479520
E_FILECREATE = -2147479504
E_FILECLOSE = -2147479503
E_FILEREAD = -2147479502
E_FILESEEK = -2147479501
E_FILEWRITE = -2147479500
E_FILEDELETE = -2147479499
E_FILEINVALID = -2147479498
E_FILENOTFOUND = -2147479497
E_DISKFULL = -2147479496
E_TOOMANYTOPICS = -2147479472
E_TOOMANYDUPS = -2147479471
E_TREETOOBIG = -2147479470
E_BADBREAKER = -2147479469
E_BADVALUE = -2147479468
E_ALL_WILD = -2147479467
E_TOODEEP = -2147479466
E_EXPECTEDTERM = -2147479465
E_MISSLPAREN = -2147479464
E_MISSRPAREN = -2147479463
E_MISSQUOTE = -2147479462
E_NULLQUERY = -2147479461
E_STOPWORD = -2147479460
E_BADRANGEOP = -2147479459
E_UNMATCHEDTYPE = -2147479458
E_WORDTOOLONG = -2147479457
E_BADINDEXFLAGS = -2147479456
E_WILD_IN_DTYPE = -2147479455
E_NOSTEMMER = -2147479454
E_MISSINGPROP = -2147479424
E_PROPLISTNOTEMPTY = -2147479423
E_PROPLISTEMPTY = -2147479422
E_ALREADYINIT = -2147479421
E_NOTINIT = -2147479420
E_RESULTSETEMPTY = -2147479419
E_TOOMANYCOLUMNS = -2147479418
E_NOKEYPROP = -2147479417
CLSID_IITResultSet = '4662daa7-d393-11d0-9a56-00c04fb68bf7'
MAX_COLUMNS = 256
CLSID_ITStdBreaker = '4662daaf-d393-11d0-9a56-00c04fb68bf7'
CLSID_ITEngStemmer = '8fa0d5a8-dedf-11d0-9a61-00c04fb68bf7'
HHWIN_NAVTYPE_TOC = 0
HHWIN_NAVTYPE_INDEX = 1
HHWIN_NAVTYPE_SEARCH = 2
HHWIN_NAVTYPE_FAVORITES = 3
HHWIN_NAVTYPE_HISTORY = 4
HHWIN_NAVTYPE_AUTHOR = 5
HHWIN_NAVTYPE_CUSTOM_FIRST = 11
IT_INCLUSIVE = 0
IT_EXCLUSIVE = 1
IT_HIDDEN = 2
HHWIN_NAVTAB_TOP = 0
HHWIN_NAVTAB_LEFT = 1
HHWIN_NAVTAB_BOTTOM = 2
HH_TAB_CONTENTS = 0
HH_TAB_INDEX = 1
HH_TAB_SEARCH = 2
HH_TAB_FAVORITES = 3
HH_TAB_HISTORY = 4
HH_TAB_AUTHOR = 5
HH_TAB_CUSTOM_FIRST = 11
HH_TAB_CUSTOM_LAST = 19
HHACT_TAB_CONTENTS = 0
HHACT_TAB_INDEX = 1
HHACT_TAB_SEARCH = 2
HHACT_TAB_HISTORY = 3
HHACT_TAB_FAVORITES = 4
HHACT_EXPAND = 5
HHACT_CONTRACT = 6
HHACT_BACK = 7
HHACT_FORWARD = 8
HHACT_STOP = 9
HHACT_REFRESH = 10
HHACT_HOME = 11
HHACT_SYNC = 12
HHACT_OPTIONS = 13
HHACT_PRINT = 14
HHACT_HIGHLIGHT = 15
HHACT_CUSTOMIZE = 16
HHACT_JUMP1 = 17
HHACT_JUMP2 = 18
HHACT_ZOOM = 19
HHACT_TOC_NEXT = 20
HHACT_TOC_PREV = 21
HHACT_NOTES = 22
HHACT_LAST_ENUM = 23
WORD_WHEEL_OPEN_FLAGS = UInt32
ITWW_OPEN_CONNECT = 0
def _define_HHN_NOTIFY_head():
    class HHN_NOTIFY(Structure):
        pass
    return HHN_NOTIFY
def _define_HHN_NOTIFY():
    HHN_NOTIFY = win32more.Data.HtmlHelp.HHN_NOTIFY_head
    HHN_NOTIFY._fields_ = [
        ("hdr", win32more.UI.Controls.NMHDR),
        ("pszUrl", win32more.Foundation.PSTR),
    ]
    return HHN_NOTIFY
def _define_HH_POPUP_head():
    class HH_POPUP(Structure):
        pass
    return HH_POPUP
def _define_HH_POPUP():
    HH_POPUP = win32more.Data.HtmlHelp.HH_POPUP_head
    HH_POPUP._fields_ = [
        ("cbStruct", Int32),
        ("hinst", win32more.Foundation.HINSTANCE),
        ("idString", UInt32),
        ("pszText", POINTER(SByte)),
        ("pt", win32more.Foundation.POINT),
        ("clrForeground", UInt32),
        ("clrBackground", UInt32),
        ("rcMargins", win32more.Foundation.RECT),
        ("pszFont", POINTER(SByte)),
    ]
    return HH_POPUP
def _define_HH_AKLINK_head():
    class HH_AKLINK(Structure):
        pass
    return HH_AKLINK
def _define_HH_AKLINK():
    HH_AKLINK = win32more.Data.HtmlHelp.HH_AKLINK_head
    HH_AKLINK._fields_ = [
        ("cbStruct", Int32),
        ("fReserved", win32more.Foundation.BOOL),
        ("pszKeywords", POINTER(SByte)),
        ("pszUrl", POINTER(SByte)),
        ("pszMsgText", POINTER(SByte)),
        ("pszMsgTitle", POINTER(SByte)),
        ("pszWindow", POINTER(SByte)),
        ("fIndexOnFail", win32more.Foundation.BOOL),
    ]
    return HH_AKLINK
def _define_HH_ENUM_IT_head():
    class HH_ENUM_IT(Structure):
        pass
    return HH_ENUM_IT
def _define_HH_ENUM_IT():
    HH_ENUM_IT = win32more.Data.HtmlHelp.HH_ENUM_IT_head
    HH_ENUM_IT._fields_ = [
        ("cbStruct", Int32),
        ("iType", Int32),
        ("pszCatName", win32more.Foundation.PSTR),
        ("pszITName", win32more.Foundation.PSTR),
        ("pszITDescription", win32more.Foundation.PSTR),
    ]
    return HH_ENUM_IT
def _define_HH_ENUM_CAT_head():
    class HH_ENUM_CAT(Structure):
        pass
    return HH_ENUM_CAT
def _define_HH_ENUM_CAT():
    HH_ENUM_CAT = win32more.Data.HtmlHelp.HH_ENUM_CAT_head
    HH_ENUM_CAT._fields_ = [
        ("cbStruct", Int32),
        ("pszCatName", win32more.Foundation.PSTR),
        ("pszCatDescription", win32more.Foundation.PSTR),
    ]
    return HH_ENUM_CAT
def _define_HH_SET_INFOTYPE_head():
    class HH_SET_INFOTYPE(Structure):
        pass
    return HH_SET_INFOTYPE
def _define_HH_SET_INFOTYPE():
    HH_SET_INFOTYPE = win32more.Data.HtmlHelp.HH_SET_INFOTYPE_head
    HH_SET_INFOTYPE._fields_ = [
        ("cbStruct", Int32),
        ("pszCatName", win32more.Foundation.PSTR),
        ("pszInfoTypeName", win32more.Foundation.PSTR),
    ]
    return HH_SET_INFOTYPE
def _define_HH_FTS_QUERY_head():
    class HH_FTS_QUERY(Structure):
        pass
    return HH_FTS_QUERY
def _define_HH_FTS_QUERY():
    HH_FTS_QUERY = win32more.Data.HtmlHelp.HH_FTS_QUERY_head
    HH_FTS_QUERY._fields_ = [
        ("cbStruct", Int32),
        ("fUniCodeStrings", win32more.Foundation.BOOL),
        ("pszSearchQuery", POINTER(SByte)),
        ("iProximity", Int32),
        ("fStemmedSearch", win32more.Foundation.BOOL),
        ("fTitleOnly", win32more.Foundation.BOOL),
        ("fExecute", win32more.Foundation.BOOL),
        ("pszWindow", POINTER(SByte)),
    ]
    return HH_FTS_QUERY
def _define_HH_WINTYPE_head():
    class HH_WINTYPE(Structure):
        pass
    return HH_WINTYPE
def _define_HH_WINTYPE():
    HH_WINTYPE = win32more.Data.HtmlHelp.HH_WINTYPE_head
    HH_WINTYPE._fields_ = [
        ("cbStruct", Int32),
        ("fUniCodeStrings", win32more.Foundation.BOOL),
        ("pszType", POINTER(SByte)),
        ("fsValidMembers", UInt32),
        ("fsWinProperties", UInt32),
        ("pszCaption", POINTER(SByte)),
        ("dwStyles", UInt32),
        ("dwExStyles", UInt32),
        ("rcWindowPos", win32more.Foundation.RECT),
        ("nShowState", Int32),
        ("hwndHelp", win32more.Foundation.HWND),
        ("hwndCaller", win32more.Foundation.HWND),
        ("paInfoTypes", POINTER(UInt32)),
        ("hwndToolBar", win32more.Foundation.HWND),
        ("hwndNavigation", win32more.Foundation.HWND),
        ("hwndHTML", win32more.Foundation.HWND),
        ("iNavWidth", Int32),
        ("rcHTML", win32more.Foundation.RECT),
        ("pszToc", POINTER(SByte)),
        ("pszIndex", POINTER(SByte)),
        ("pszFile", POINTER(SByte)),
        ("pszHome", POINTER(SByte)),
        ("fsToolBarFlags", UInt32),
        ("fNotExpanded", win32more.Foundation.BOOL),
        ("curNavType", Int32),
        ("tabpos", Int32),
        ("idNotify", Int32),
        ("tabOrder", Byte * 20),
        ("cHistory", Int32),
        ("pszJump1", POINTER(SByte)),
        ("pszJump2", POINTER(SByte)),
        ("pszUrlJump1", POINTER(SByte)),
        ("pszUrlJump2", POINTER(SByte)),
        ("rcMinSize", win32more.Foundation.RECT),
        ("cbInfoTypes", Int32),
        ("pszCustomTabs", POINTER(SByte)),
    ]
    return HH_WINTYPE
def _define_HHNTRACK_head():
    class HHNTRACK(Structure):
        pass
    return HHNTRACK
def _define_HHNTRACK():
    HHNTRACK = win32more.Data.HtmlHelp.HHNTRACK_head
    HHNTRACK._fields_ = [
        ("hdr", win32more.UI.Controls.NMHDR),
        ("pszCurUrl", win32more.Foundation.PSTR),
        ("idAction", Int32),
        ("phhWinType", POINTER(win32more.Data.HtmlHelp.HH_WINTYPE_head)),
    ]
    return HHNTRACK
HH_GPROPID = Int32
HH_GPROPID_SINGLETHREAD = 1
HH_GPROPID_TOOLBAR_MARGIN = 2
HH_GPROPID_UI_LANGUAGE = 3
HH_GPROPID_CURRENT_SUBSET = 4
HH_GPROPID_CONTENT_LANGUAGE = 5
def _define_HH_GLOBAL_PROPERTY_head():
    class HH_GLOBAL_PROPERTY(Structure):
        pass
    return HH_GLOBAL_PROPERTY
def _define_HH_GLOBAL_PROPERTY():
    HH_GLOBAL_PROPERTY = win32more.Data.HtmlHelp.HH_GLOBAL_PROPERTY_head
    HH_GLOBAL_PROPERTY._fields_ = [
        ("id", win32more.Data.HtmlHelp.HH_GPROPID),
        ("var", win32more.System.Com.VARIANT),
    ]
    return HH_GLOBAL_PROPERTY
def _define_CProperty_head():
    class CProperty(Structure):
        pass
    return CProperty
def _define_CProperty():
    CProperty = win32more.Data.HtmlHelp.CProperty_head
    class CProperty__Anonymous_e__Union(Union):
        pass
    CProperty__Anonymous_e__Union._fields_ = [
        ("lpszwData", win32more.Foundation.PWSTR),
        ("lpvData", c_void_p),
        ("dwValue", UInt32),
    ]
    CProperty._anonymous_ = [
        'Anonymous',
    ]
    CProperty._fields_ = [
        ("dwPropID", UInt32),
        ("cbData", UInt32),
        ("dwType", UInt32),
        ("Anonymous", CProperty__Anonymous_e__Union),
        ("fPersist", win32more.Foundation.BOOL),
    ]
    return CProperty
def _define_IITPropList_head():
    class IITPropList(win32more.System.Com.IPersistStreamInit_head):
        Guid = Guid('1f403bb1-9997-11d0-a850-00aa006c7d01')
    return IITPropList
def _define_IITPropList():
    IITPropList = win32more.Data.HtmlHelp.IITPropList_head
    IITPropList.Set = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(9, 'Set', ((1, 'PropID'),(1, 'lpszwString'),(1, 'dwOperation'),)))
    IITPropList.Set = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p,UInt32,UInt32, use_last_error=False)(10, 'Set', ((1, 'PropID'),(1, 'lpvData'),(1, 'cbData'),(1, 'dwOperation'),)))
    IITPropList.Set = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32, use_last_error=False)(11, 'Set', ((1, 'PropID'),(1, 'dwData'),(1, 'dwOperation'),)))
    IITPropList.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Data.HtmlHelp.CProperty_head), use_last_error=False)(12, 'Add', ((1, 'Prop'),)))
    IITPropList.Get = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Data.HtmlHelp.CProperty_head), use_last_error=False)(13, 'Get', ((1, 'PropID'),(1, 'Property'),)))
    IITPropList.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(14, 'Clear', ()))
    IITPropList.SetPersist = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(15, 'SetPersist', ((1, 'fPersist'),)))
    IITPropList.SetPersist = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.BOOL, use_last_error=False)(16, 'SetPersist', ((1, 'PropID'),(1, 'fPersist'),)))
    IITPropList.GetFirst = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Data.HtmlHelp.CProperty_head), use_last_error=False)(17, 'GetFirst', ((1, 'Property'),)))
    IITPropList.GetNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Data.HtmlHelp.CProperty_head), use_last_error=False)(18, 'GetNext', ((1, 'Property'),)))
    IITPropList.GetPropCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(19, 'GetPropCount', ((1, 'cProp'),)))
    IITPropList.SaveHeader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32, use_last_error=False)(20, 'SaveHeader', ((1, 'lpvData'),(1, 'dwHdrSize'),)))
    IITPropList.SaveData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,c_void_p,UInt32, use_last_error=False)(21, 'SaveData', ((1, 'lpvHeader'),(1, 'dwHdrSize'),(1, 'lpvData'),(1, 'dwBufSize'),)))
    IITPropList.GetHeaderSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(22, 'GetHeaderSize', ((1, 'dwHdrSize'),)))
    IITPropList.GetDataSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(23, 'GetDataSize', ((1, 'lpvHeader'),(1, 'dwHdrSize'),(1, 'dwDataSize'),)))
    IITPropList.SaveDataToStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,win32more.System.Com.IStream_head, use_last_error=False)(24, 'SaveDataToStream', ((1, 'lpvHeader'),(1, 'dwHdrSize'),(1, 'pStream'),)))
    IITPropList.LoadFromMem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32, use_last_error=False)(25, 'LoadFromMem', ((1, 'lpvData'),(1, 'dwBufSize'),)))
    IITPropList.SaveToMem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32, use_last_error=False)(26, 'SaveToMem', ((1, 'lpvData'),(1, 'dwBufSize'),)))
    return IITPropList
def _define_IITDatabase_head():
    class IITDatabase(win32more.System.Com.IUnknown_head):
        Guid = Guid('8fa0d5a2-dedf-11d0-9a61-00c04fb68bf7')
    return IITDatabase
def _define_IITDatabase():
    IITDatabase = win32more.Data.HtmlHelp.IITDatabase_head
    IITDatabase.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(3, 'Open', ((1, 'lpszHost'),(1, 'lpszMoniker'),(1, 'dwFlags'),)))
    IITDatabase.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Close', ()))
    IITDatabase.CreateObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(UInt32), use_last_error=False)(5, 'CreateObject', ((1, 'rclsid'),(1, 'pdwObjInstance'),)))
    IITDatabase.GetObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(6, 'GetObject', ((1, 'dwObjInstance'),(1, 'riid'),(1, 'ppvObj'),)))
    IITDatabase.GetObjectPersistence = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(c_void_p),win32more.Foundation.BOOL, use_last_error=False)(7, 'GetObjectPersistence', ((1, 'lpwszObject'),(1, 'dwObjInstance'),(1, 'ppvPersistence'),(1, 'fStream'),)))
    return IITDatabase
def _define_IITGroup_head():
    class IITGroup(Structure):
        pass
    return IITGroup
def _define_IITGroup():
    IITGroup = win32more.Data.HtmlHelp.IITGroup_head
    return IITGroup
def _define_IITQuery_head():
    class IITQuery(Structure):
        pass
    return IITQuery
def _define_IITQuery():
    IITQuery = win32more.Data.HtmlHelp.IITQuery_head
    return IITQuery
def _define_IITWordWheel_head():
    class IITWordWheel(win32more.System.Com.IUnknown_head):
        Guid = Guid('8fa0d5a4-dedf-11d0-9a61-00c04fb68bf7')
    return IITWordWheel
def _define_IITWordWheel():
    IITWordWheel = win32more.Data.HtmlHelp.IITWordWheel_head
    IITWordWheel.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Data.HtmlHelp.IITDatabase_head,win32more.Foundation.PWSTR,win32more.Data.HtmlHelp.WORD_WHEEL_OPEN_FLAGS, use_last_error=False)(3, 'Open', ((1, 'lpITDB'),(1, 'lpszMoniker'),(1, 'dwFlags'),)))
    IITWordWheel.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Close', ()))
    IITWordWheel.GetLocaleInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(5, 'GetLocaleInfo', ((1, 'pdwCodePageID'),(1, 'plcid'),)))
    IITWordWheel.GetSorterInstance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(6, 'GetSorterInstance', ((1, 'pdwObjInstance'),)))
    IITWordWheel.Count = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'Count', ((1, 'pcEntries'),)))
    IITWordWheel.Lookup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.BOOL,POINTER(Int32), use_last_error=False)(8, 'Lookup', ((1, 'lpcvPrefix'),(1, 'fExactMatch'),(1, 'plEntry'),)))
    IITWordWheel.Lookup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Data.HtmlHelp.IITResultSet_head,Int32, use_last_error=False)(9, 'Lookup', ((1, 'lEntry'),(1, 'lpITResult'),(1, 'cEntries'),)))
    IITWordWheel.Lookup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,c_void_p,UInt32, use_last_error=False)(10, 'Lookup', ((1, 'lEntry'),(1, 'lpvKeyBuf'),(1, 'cbKeyBuf'),)))
    IITWordWheel.SetGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Data.HtmlHelp.IITGroup_head), use_last_error=False)(11, 'SetGroup', ((1, 'piitGroup'),)))
    IITWordWheel.GetGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Data.HtmlHelp.IITGroup_head)), use_last_error=False)(12, 'GetGroup', ((1, 'ppiitGroup'),)))
    IITWordWheel.GetDataCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(UInt32), use_last_error=False)(13, 'GetDataCount', ((1, 'lEntry'),(1, 'pdwCount'),)))
    IITWordWheel.GetData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Data.HtmlHelp.IITResultSet_head, use_last_error=False)(14, 'GetData', ((1, 'lEntry'),(1, 'lpITResult'),)))
    IITWordWheel.GetDataColumns = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Data.HtmlHelp.IITResultSet_head, use_last_error=False)(15, 'GetDataColumns', ((1, 'pRS'),)))
    return IITWordWheel
def _define_IStemSink_head():
    class IStemSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('fe77c330-7f42-11ce-be57-00aa0051fe20')
    return IStemSink
def _define_IStemSink():
    IStemSink = win32more.Data.HtmlHelp.IStemSink_head
    IStemSink.PutAltWord = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(3, 'PutAltWord', ((1, 'pwcInBuf'),(1, 'cwc'),)))
    IStemSink.PutWord = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(4, 'PutWord', ((1, 'pwcInBuf'),(1, 'cwc'),)))
    return IStemSink
def _define_IStemmerConfig_head():
    class IStemmerConfig(win32more.System.Com.IUnknown_head):
        Guid = Guid('8fa0d5a7-dedf-11d0-9a61-00c04fb68bf7')
    return IStemmerConfig
def _define_IStemmerConfig():
    IStemmerConfig = win32more.Data.HtmlHelp.IStemmerConfig_head
    IStemmerConfig.SetLocaleInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(3, 'SetLocaleInfo', ((1, 'dwCodePageID'),(1, 'lcid'),)))
    IStemmerConfig.GetLocaleInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(4, 'GetLocaleInfo', ((1, 'pdwCodePageID'),(1, 'plcid'),)))
    IStemmerConfig.SetControlInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(5, 'SetControlInfo', ((1, 'grfStemFlags'),(1, 'dwReserved'),)))
    IStemmerConfig.GetControlInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(6, 'GetControlInfo', ((1, 'pgrfStemFlags'),(1, 'pdwReserved'),)))
    IStemmerConfig.LoadExternalStemmerData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,UInt32, use_last_error=False)(7, 'LoadExternalStemmerData', ((1, 'pStream'),(1, 'dwExtDataType'),)))
    return IStemmerConfig
def _define_IITStopWordList_head():
    class IITStopWordList(Structure):
        pass
    return IITStopWordList
def _define_IITStopWordList():
    IITStopWordList = win32more.Data.HtmlHelp.IITStopWordList_head
    return IITStopWordList
def _define_IWordBreakerConfig_head():
    class IWordBreakerConfig(win32more.System.Com.IUnknown_head):
        Guid = Guid('8fa0d5a6-dedf-11d0-9a61-00c04fb68bf7')
    return IWordBreakerConfig
def _define_IWordBreakerConfig():
    IWordBreakerConfig = win32more.Data.HtmlHelp.IWordBreakerConfig_head
    IWordBreakerConfig.SetLocaleInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(3, 'SetLocaleInfo', ((1, 'dwCodePageID'),(1, 'lcid'),)))
    IWordBreakerConfig.GetLocaleInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(4, 'GetLocaleInfo', ((1, 'pdwCodePageID'),(1, 'plcid'),)))
    IWordBreakerConfig.SetBreakWordType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'SetBreakWordType', ((1, 'dwBreakWordType'),)))
    IWordBreakerConfig.GetBreakWordType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(6, 'GetBreakWordType', ((1, 'pdwBreakWordType'),)))
    IWordBreakerConfig.SetControlInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(7, 'SetControlInfo', ((1, 'grfBreakFlags'),(1, 'dwReserved'),)))
    IWordBreakerConfig.GetControlInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32), use_last_error=False)(8, 'GetControlInfo', ((1, 'pgrfBreakFlags'),(1, 'pdwReserved'),)))
    IWordBreakerConfig.LoadExternalBreakerData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,UInt32, use_last_error=False)(9, 'LoadExternalBreakerData', ((1, 'pStream'),(1, 'dwExtDataType'),)))
    IWordBreakerConfig.SetWordStemmer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Search.IStemmer_head, use_last_error=False)(10, 'SetWordStemmer', ((1, 'rclsid'),(1, 'pStemmer'),)))
    IWordBreakerConfig.GetWordStemmer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Search.IStemmer_head), use_last_error=False)(11, 'GetWordStemmer', ((1, 'ppStemmer'),)))
    return IWordBreakerConfig
PRIORITY = Int32
PRIORITY_LOW = 0
PRIORITY_NORMAL = 1
PRIORITY_HIGH = 2
def _define_ROWSTATUS_head():
    class ROWSTATUS(Structure):
        pass
    return ROWSTATUS
def _define_ROWSTATUS():
    ROWSTATUS = win32more.Data.HtmlHelp.ROWSTATUS_head
    ROWSTATUS._fields_ = [
        ("lRowFirst", Int32),
        ("cRows", Int32),
        ("cProperties", Int32),
        ("cRowsTotal", Int32),
    ]
    return ROWSTATUS
def _define_COLUMNSTATUS_head():
    class COLUMNSTATUS(Structure):
        pass
    return COLUMNSTATUS
def _define_COLUMNSTATUS():
    COLUMNSTATUS = win32more.Data.HtmlHelp.COLUMNSTATUS_head
    COLUMNSTATUS._fields_ = [
        ("cPropCount", Int32),
        ("cPropsLoaded", Int32),
    ]
    return COLUMNSTATUS
def _define_PFNCOLHEAPFREE():
    return CFUNCTYPE(Int32,c_void_p, use_last_error=False)
def _define_IITResultSet_head():
    class IITResultSet(win32more.System.Com.IUnknown_head):
        Guid = Guid('3bb91d41-998b-11d0-a850-00aa006c7d01')
    return IITResultSet
def _define_IITResultSet():
    IITResultSet = win32more.Data.HtmlHelp.IITResultSet_head
    IITResultSet.SetColumnPriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Data.HtmlHelp.PRIORITY, use_last_error=False)(3, 'SetColumnPriority', ((1, 'lColumnIndex'),(1, 'ColumnPriority'),)))
    IITResultSet.SetColumnHeap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,c_void_p,win32more.Data.HtmlHelp.PFNCOLHEAPFREE, use_last_error=False)(4, 'SetColumnHeap', ((1, 'lColumnIndex'),(1, 'lpvHeap'),(1, 'pfnColHeapFree'),)))
    IITResultSet.SetKeyProp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'SetKeyProp', ((1, 'PropID'),)))
    IITResultSet.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.Data.HtmlHelp.PRIORITY, use_last_error=False)(6, 'Add', ((1, 'PropID'),(1, 'dwDefaultData'),(1, 'Priority'),)))
    IITResultSet.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,win32more.Data.HtmlHelp.PRIORITY, use_last_error=False)(7, 'Add', ((1, 'PropID'),(1, 'lpszwDefault'),(1, 'Priority'),)))
    IITResultSet.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p,UInt32,win32more.Data.HtmlHelp.PRIORITY, use_last_error=False)(8, 'Add', ((1, 'PropID'),(1, 'lpvDefaultData'),(1, 'cbData'),(1, 'Priority'),)))
    IITResultSet.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(9, 'Add', ((1, 'lpvHdr'),)))
    IITResultSet.Append = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,c_void_p, use_last_error=False)(10, 'Append', ((1, 'lpvHdr'),(1, 'lpvData'),)))
    IITResultSet.Set = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,c_void_p,UInt32, use_last_error=False)(11, 'Set', ((1, 'lRowIndex'),(1, 'lColumnIndex'),(1, 'lpvData'),(1, 'cbData'),)))
    IITResultSet.Set = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,win32more.Foundation.PWSTR, use_last_error=False)(12, 'Set', ((1, 'lRowIndex'),(1, 'lColumnIndex'),(1, 'lpwStr'),)))
    IITResultSet.Set = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,UIntPtr, use_last_error=False)(13, 'Set', ((1, 'lRowIndex'),(1, 'lColumnIndex'),(1, 'dwData'),)))
    IITResultSet.Set = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,c_void_p,c_void_p, use_last_error=False)(14, 'Set', ((1, 'lRowIndex'),(1, 'lpvHdr'),(1, 'lpvData'),)))
    IITResultSet.Copy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Data.HtmlHelp.IITResultSet_head, use_last_error=False)(15, 'Copy', ((1, 'pRSCopy'),)))
    IITResultSet.AppendRows = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Data.HtmlHelp.IITResultSet_head,Int32,Int32,POINTER(Int32), use_last_error=False)(16, 'AppendRows', ((1, 'pResSrc'),(1, 'lRowSrcFirst'),(1, 'cSrcRows'),(1, 'lRowFirstDest'),)))
    IITResultSet.Get = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.Data.HtmlHelp.CProperty_head), use_last_error=False)(17, 'Get', ((1, 'lRowIndex'),(1, 'lColumnIndex'),(1, 'Prop'),)))
    IITResultSet.GetKeyProp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(18, 'GetKeyProp', ((1, 'KeyPropID'),)))
    IITResultSet.GetColumnPriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Data.HtmlHelp.PRIORITY), use_last_error=False)(19, 'GetColumnPriority', ((1, 'lColumnIndex'),(1, 'ColumnPriority'),)))
    IITResultSet.GetRowCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(20, 'GetRowCount', ((1, 'lNumberOfRows'),)))
    IITResultSet.GetColumnCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(21, 'GetColumnCount', ((1, 'lNumberOfColumns'),)))
    IITResultSet.GetColumn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(UInt32),POINTER(UInt32),POINTER(c_void_p),POINTER(UInt32),POINTER(win32more.Data.HtmlHelp.PRIORITY), use_last_error=False)(22, 'GetColumn', ((1, 'lColumnIndex'),(1, 'PropID'),(1, 'dwType'),(1, 'lpvDefaultValue'),(1, 'cbSize'),(1, 'ColumnPriority'),)))
    IITResultSet.GetColumn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(UInt32), use_last_error=False)(23, 'GetColumn', ((1, 'lColumnIndex'),(1, 'PropID'),)))
    IITResultSet.GetColumnFromPropID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Int32), use_last_error=False)(24, 'GetColumnFromPropID', ((1, 'PropID'),(1, 'lColumnIndex'),)))
    IITResultSet.Clear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(25, 'Clear', ()))
    IITResultSet.ClearRows = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(26, 'ClearRows', ()))
    IITResultSet.Free = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(27, 'Free', ()))
    IITResultSet.IsCompleted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(28, 'IsCompleted', ()))
    IITResultSet.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(29, 'Cancel', ()))
    IITResultSet.Pause = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(30, 'Pause', ((1, 'fPause'),)))
    IITResultSet.GetRowStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.Data.HtmlHelp.ROWSTATUS_head), use_last_error=False)(31, 'GetRowStatus', ((1, 'lRowFirst'),(1, 'cRows'),(1, 'lpRowStatus'),)))
    IITResultSet.GetColumnStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Data.HtmlHelp.COLUMNSTATUS_head), use_last_error=False)(32, 'GetColumnStatus', ((1, 'lpColStatus'),)))
    return IITResultSet
__all__ = [
    "HH_DISPLAY_TOPIC",
    "HH_HELP_FINDER",
    "HH_DISPLAY_TOC",
    "HH_DISPLAY_INDEX",
    "HH_DISPLAY_SEARCH",
    "HH_SET_WIN_TYPE",
    "HH_GET_WIN_TYPE",
    "HH_GET_WIN_HANDLE",
    "HH_ENUM_INFO_TYPE",
    "HH_SET_INFO_TYPE",
    "HH_SYNC",
    "HH_RESERVED1",
    "HH_RESERVED2",
    "HH_RESERVED3",
    "HH_KEYWORD_LOOKUP",
    "HH_DISPLAY_TEXT_POPUP",
    "HH_HELP_CONTEXT",
    "HH_TP_HELP_CONTEXTMENU",
    "HH_TP_HELP_WM_HELP",
    "HH_CLOSE_ALL",
    "HH_ALINK_LOOKUP",
    "HH_GET_LAST_ERROR",
    "HH_ENUM_CATEGORY",
    "HH_ENUM_CATEGORY_IT",
    "HH_RESET_IT_FILTER",
    "HH_SET_INCLUSIVE_FILTER",
    "HH_SET_EXCLUSIVE_FILTER",
    "HH_INITIALIZE",
    "HH_UNINITIALIZE",
    "HH_SET_QUERYSERVICE",
    "HH_PRETRANSLATEMESSAGE",
    "HH_SET_GLOBAL_PROPERTY",
    "HH_SAFE_DISPLAY_TOPIC",
    "HHWIN_PROP_TAB_AUTOHIDESHOW",
    "HHWIN_PROP_ONTOP",
    "HHWIN_PROP_NOTITLEBAR",
    "HHWIN_PROP_NODEF_STYLES",
    "HHWIN_PROP_NODEF_EXSTYLES",
    "HHWIN_PROP_TRI_PANE",
    "HHWIN_PROP_NOTB_TEXT",
    "HHWIN_PROP_POST_QUIT",
    "HHWIN_PROP_AUTO_SYNC",
    "HHWIN_PROP_TRACKING",
    "HHWIN_PROP_TAB_SEARCH",
    "HHWIN_PROP_TAB_HISTORY",
    "HHWIN_PROP_TAB_FAVORITES",
    "HHWIN_PROP_CHANGE_TITLE",
    "HHWIN_PROP_NAV_ONLY_WIN",
    "HHWIN_PROP_NO_TOOLBAR",
    "HHWIN_PROP_MENU",
    "HHWIN_PROP_TAB_ADVSEARCH",
    "HHWIN_PROP_USER_POS",
    "HHWIN_PROP_TAB_CUSTOM1",
    "HHWIN_PROP_TAB_CUSTOM2",
    "HHWIN_PROP_TAB_CUSTOM3",
    "HHWIN_PROP_TAB_CUSTOM4",
    "HHWIN_PROP_TAB_CUSTOM5",
    "HHWIN_PROP_TAB_CUSTOM6",
    "HHWIN_PROP_TAB_CUSTOM7",
    "HHWIN_PROP_TAB_CUSTOM8",
    "HHWIN_PROP_TAB_CUSTOM9",
    "HHWIN_TB_MARGIN",
    "HHWIN_PARAM_PROPERTIES",
    "HHWIN_PARAM_STYLES",
    "HHWIN_PARAM_EXSTYLES",
    "HHWIN_PARAM_RECT",
    "HHWIN_PARAM_NAV_WIDTH",
    "HHWIN_PARAM_SHOWSTATE",
    "HHWIN_PARAM_INFOTYPES",
    "HHWIN_PARAM_TB_FLAGS",
    "HHWIN_PARAM_EXPANSION",
    "HHWIN_PARAM_TABPOS",
    "HHWIN_PARAM_TABORDER",
    "HHWIN_PARAM_HISTORY_COUNT",
    "HHWIN_PARAM_CUR_TAB",
    "HHWIN_BUTTON_EXPAND",
    "HHWIN_BUTTON_BACK",
    "HHWIN_BUTTON_FORWARD",
    "HHWIN_BUTTON_STOP",
    "HHWIN_BUTTON_REFRESH",
    "HHWIN_BUTTON_HOME",
    "HHWIN_BUTTON_BROWSE_FWD",
    "HHWIN_BUTTON_BROWSE_BCK",
    "HHWIN_BUTTON_NOTES",
    "HHWIN_BUTTON_CONTENTS",
    "HHWIN_BUTTON_SYNC",
    "HHWIN_BUTTON_OPTIONS",
    "HHWIN_BUTTON_PRINT",
    "HHWIN_BUTTON_INDEX",
    "HHWIN_BUTTON_SEARCH",
    "HHWIN_BUTTON_HISTORY",
    "HHWIN_BUTTON_FAVORITES",
    "HHWIN_BUTTON_JUMP1",
    "HHWIN_BUTTON_JUMP2",
    "HHWIN_BUTTON_ZOOM",
    "HHWIN_BUTTON_TOC_NEXT",
    "HHWIN_BUTTON_TOC_PREV",
    "IDTB_EXPAND",
    "IDTB_CONTRACT",
    "IDTB_STOP",
    "IDTB_REFRESH",
    "IDTB_BACK",
    "IDTB_HOME",
    "IDTB_SYNC",
    "IDTB_PRINT",
    "IDTB_OPTIONS",
    "IDTB_FORWARD",
    "IDTB_NOTES",
    "IDTB_BROWSE_FWD",
    "IDTB_BROWSE_BACK",
    "IDTB_CONTENTS",
    "IDTB_INDEX",
    "IDTB_SEARCH",
    "IDTB_HISTORY",
    "IDTB_FAVORITES",
    "IDTB_JUMP1",
    "IDTB_JUMP2",
    "IDTB_CUSTOMIZE",
    "IDTB_ZOOM",
    "IDTB_TOC_NEXT",
    "IDTB_TOC_PREV",
    "HH_MAX_TABS",
    "HH_FTS_DEFAULT_PROXIMITY",
    "CLSID_IITPropList",
    "PROP_ADD",
    "PROP_DELETE",
    "PROP_UPDATE",
    "TYPE_VALUE",
    "TYPE_POINTER",
    "TYPE_STRING",
    "CLSID_IITDatabase",
    "CLSID_IITDatabaseLocal",
    "STDPROP_UID",
    "STDPROP_TITLE",
    "STDPROP_USERDATA",
    "STDPROP_KEY",
    "STDPROP_SORTKEY",
    "STDPROP_DISPLAYKEY",
    "STDPROP_SORTORDINAL",
    "STDPROP_INDEX_TEXT",
    "STDPROP_INDEX_VFLD",
    "STDPROP_INDEX_DTYPE",
    "STDPROP_INDEX_LENGTH",
    "STDPROP_INDEX_BREAK",
    "STDPROP_INDEX_TERM",
    "STDPROP_INDEX_TERM_RAW_LENGTH",
    "STDPROP_USERPROP_BASE",
    "STDPROP_USERPROP_MAX",
    "CLSID_IITCmdInt",
    "CLSID_IITSvMgr",
    "CLSID_IITWordWheelUpdate",
    "CLSID_IITGroupUpdate",
    "CLSID_IITIndexBuild",
    "CLSID_IITWWFilterBuild",
    "CLSID_IITWordWheel",
    "CLSID_IITWordWheelLocal",
    "ITWW_OPEN_NOCONNECT",
    "ITWW_CBKEY_MAX",
    "IITWBC_BREAK_ACCEPT_WILDCARDS",
    "IITWBC_BREAK_AND_STEM",
    "E_NOTEXIST",
    "E_DUPLICATE",
    "E_BADVERSION",
    "E_BADFILE",
    "E_BADFORMAT",
    "E_NOPERMISSION",
    "E_ASSERT",
    "E_INTERRUPT",
    "E_NOTSUPPORTED",
    "E_OUTOFRANGE",
    "E_GROUPIDTOOBIG",
    "E_TOOMANYTITLES",
    "E_NOMERGEDDATA",
    "E_NOTFOUND",
    "E_CANTFINDDLL",
    "E_NOHANDLE",
    "E_GETLASTERROR",
    "E_BADPARAM",
    "E_INVALIDSTATE",
    "E_NOTOPEN",
    "E_ALREADYOPEN",
    "E_UNKNOWN_TRANSPORT",
    "E_UNSUPPORTED_TRANSPORT",
    "E_BADFILTERSIZE",
    "E_TOOMANYOBJECTS",
    "E_NAMETOOLONG",
    "E_FILECREATE",
    "E_FILECLOSE",
    "E_FILEREAD",
    "E_FILESEEK",
    "E_FILEWRITE",
    "E_FILEDELETE",
    "E_FILEINVALID",
    "E_FILENOTFOUND",
    "E_DISKFULL",
    "E_TOOMANYTOPICS",
    "E_TOOMANYDUPS",
    "E_TREETOOBIG",
    "E_BADBREAKER",
    "E_BADVALUE",
    "E_ALL_WILD",
    "E_TOODEEP",
    "E_EXPECTEDTERM",
    "E_MISSLPAREN",
    "E_MISSRPAREN",
    "E_MISSQUOTE",
    "E_NULLQUERY",
    "E_STOPWORD",
    "E_BADRANGEOP",
    "E_UNMATCHEDTYPE",
    "E_WORDTOOLONG",
    "E_BADINDEXFLAGS",
    "E_WILD_IN_DTYPE",
    "E_NOSTEMMER",
    "E_MISSINGPROP",
    "E_PROPLISTNOTEMPTY",
    "E_PROPLISTEMPTY",
    "E_ALREADYINIT",
    "E_NOTINIT",
    "E_RESULTSETEMPTY",
    "E_TOOMANYCOLUMNS",
    "E_NOKEYPROP",
    "CLSID_IITResultSet",
    "MAX_COLUMNS",
    "CLSID_ITStdBreaker",
    "CLSID_ITEngStemmer",
    "HHWIN_NAVTYPE_TOC",
    "HHWIN_NAVTYPE_INDEX",
    "HHWIN_NAVTYPE_SEARCH",
    "HHWIN_NAVTYPE_FAVORITES",
    "HHWIN_NAVTYPE_HISTORY",
    "HHWIN_NAVTYPE_AUTHOR",
    "HHWIN_NAVTYPE_CUSTOM_FIRST",
    "IT_INCLUSIVE",
    "IT_EXCLUSIVE",
    "IT_HIDDEN",
    "HHWIN_NAVTAB_TOP",
    "HHWIN_NAVTAB_LEFT",
    "HHWIN_NAVTAB_BOTTOM",
    "HH_TAB_CONTENTS",
    "HH_TAB_INDEX",
    "HH_TAB_SEARCH",
    "HH_TAB_FAVORITES",
    "HH_TAB_HISTORY",
    "HH_TAB_AUTHOR",
    "HH_TAB_CUSTOM_FIRST",
    "HH_TAB_CUSTOM_LAST",
    "HHACT_TAB_CONTENTS",
    "HHACT_TAB_INDEX",
    "HHACT_TAB_SEARCH",
    "HHACT_TAB_HISTORY",
    "HHACT_TAB_FAVORITES",
    "HHACT_EXPAND",
    "HHACT_CONTRACT",
    "HHACT_BACK",
    "HHACT_FORWARD",
    "HHACT_STOP",
    "HHACT_REFRESH",
    "HHACT_HOME",
    "HHACT_SYNC",
    "HHACT_OPTIONS",
    "HHACT_PRINT",
    "HHACT_HIGHLIGHT",
    "HHACT_CUSTOMIZE",
    "HHACT_JUMP1",
    "HHACT_JUMP2",
    "HHACT_ZOOM",
    "HHACT_TOC_NEXT",
    "HHACT_TOC_PREV",
    "HHACT_NOTES",
    "HHACT_LAST_ENUM",
    "WORD_WHEEL_OPEN_FLAGS",
    "ITWW_OPEN_CONNECT",
    "HHN_NOTIFY",
    "HH_POPUP",
    "HH_AKLINK",
    "HH_ENUM_IT",
    "HH_ENUM_CAT",
    "HH_SET_INFOTYPE",
    "HH_FTS_QUERY",
    "HH_WINTYPE",
    "HHNTRACK",
    "HH_GPROPID",
    "HH_GPROPID_SINGLETHREAD",
    "HH_GPROPID_TOOLBAR_MARGIN",
    "HH_GPROPID_UI_LANGUAGE",
    "HH_GPROPID_CURRENT_SUBSET",
    "HH_GPROPID_CONTENT_LANGUAGE",
    "HH_GLOBAL_PROPERTY",
    "CProperty",
    "IITPropList",
    "IITDatabase",
    "IITGroup",
    "IITQuery",
    "IITWordWheel",
    "IStemSink",
    "IStemmerConfig",
    "IITStopWordList",
    "IWordBreakerConfig",
    "PRIORITY",
    "PRIORITY_LOW",
    "PRIORITY_NORMAL",
    "PRIORITY_HIGH",
    "ROWSTATUS",
    "COLUMNSTATUS",
    "PFNCOLHEAPFREE",
    "IITResultSet",
]
