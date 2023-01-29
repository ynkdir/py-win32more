from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import win32more.Data.HtmlHelp
import win32more.Foundation
import win32more.System.Com
import win32more.System.Search
import win32more.UI.Controls
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
HHWIN_PROP_TAB_AUTOHIDESHOW: UInt32 = 1
HHWIN_PROP_ONTOP: UInt32 = 2
HHWIN_PROP_NOTITLEBAR: UInt32 = 4
HHWIN_PROP_NODEF_STYLES: UInt32 = 8
HHWIN_PROP_NODEF_EXSTYLES: UInt32 = 16
HHWIN_PROP_TRI_PANE: UInt32 = 32
HHWIN_PROP_NOTB_TEXT: UInt32 = 64
HHWIN_PROP_POST_QUIT: UInt32 = 128
HHWIN_PROP_AUTO_SYNC: UInt32 = 256
HHWIN_PROP_TRACKING: UInt32 = 512
HHWIN_PROP_TAB_SEARCH: UInt32 = 1024
HHWIN_PROP_TAB_HISTORY: UInt32 = 2048
HHWIN_PROP_TAB_FAVORITES: UInt32 = 4096
HHWIN_PROP_CHANGE_TITLE: UInt32 = 8192
HHWIN_PROP_NAV_ONLY_WIN: UInt32 = 16384
HHWIN_PROP_NO_TOOLBAR: UInt32 = 32768
HHWIN_PROP_MENU: UInt32 = 65536
HHWIN_PROP_TAB_ADVSEARCH: UInt32 = 131072
HHWIN_PROP_USER_POS: UInt32 = 262144
HHWIN_PROP_TAB_CUSTOM1: UInt32 = 524288
HHWIN_PROP_TAB_CUSTOM2: UInt32 = 1048576
HHWIN_PROP_TAB_CUSTOM3: UInt32 = 2097152
HHWIN_PROP_TAB_CUSTOM4: UInt32 = 4194304
HHWIN_PROP_TAB_CUSTOM5: UInt32 = 8388608
HHWIN_PROP_TAB_CUSTOM6: UInt32 = 16777216
HHWIN_PROP_TAB_CUSTOM7: UInt32 = 33554432
HHWIN_PROP_TAB_CUSTOM8: UInt32 = 67108864
HHWIN_PROP_TAB_CUSTOM9: UInt32 = 134217728
HHWIN_TB_MARGIN: UInt32 = 268435456
HHWIN_PARAM_PROPERTIES: UInt32 = 2
HHWIN_PARAM_STYLES: UInt32 = 4
HHWIN_PARAM_EXSTYLES: UInt32 = 8
HHWIN_PARAM_RECT: UInt32 = 16
HHWIN_PARAM_NAV_WIDTH: UInt32 = 32
HHWIN_PARAM_SHOWSTATE: UInt32 = 64
HHWIN_PARAM_INFOTYPES: UInt32 = 128
HHWIN_PARAM_TB_FLAGS: UInt32 = 256
HHWIN_PARAM_EXPANSION: UInt32 = 512
HHWIN_PARAM_TABPOS: UInt32 = 1024
HHWIN_PARAM_TABORDER: UInt32 = 2048
HHWIN_PARAM_HISTORY_COUNT: UInt32 = 4096
HHWIN_PARAM_CUR_TAB: UInt32 = 8192
HHWIN_BUTTON_EXPAND: UInt32 = 2
HHWIN_BUTTON_BACK: UInt32 = 4
HHWIN_BUTTON_FORWARD: UInt32 = 8
HHWIN_BUTTON_STOP: UInt32 = 16
HHWIN_BUTTON_REFRESH: UInt32 = 32
HHWIN_BUTTON_HOME: UInt32 = 64
HHWIN_BUTTON_BROWSE_FWD: UInt32 = 128
HHWIN_BUTTON_BROWSE_BCK: UInt32 = 256
HHWIN_BUTTON_NOTES: UInt32 = 512
HHWIN_BUTTON_CONTENTS: UInt32 = 1024
HHWIN_BUTTON_SYNC: UInt32 = 2048
HHWIN_BUTTON_OPTIONS: UInt32 = 4096
HHWIN_BUTTON_PRINT: UInt32 = 8192
HHWIN_BUTTON_INDEX: UInt32 = 16384
HHWIN_BUTTON_SEARCH: UInt32 = 32768
HHWIN_BUTTON_HISTORY: UInt32 = 65536
HHWIN_BUTTON_FAVORITES: UInt32 = 131072
HHWIN_BUTTON_JUMP1: UInt32 = 262144
HHWIN_BUTTON_JUMP2: UInt32 = 524288
HHWIN_BUTTON_ZOOM: UInt32 = 1048576
HHWIN_BUTTON_TOC_NEXT: UInt32 = 2097152
HHWIN_BUTTON_TOC_PREV: UInt32 = 4194304
IDTB_EXPAND: UInt32 = 200
IDTB_CONTRACT: UInt32 = 201
IDTB_STOP: UInt32 = 202
IDTB_REFRESH: UInt32 = 203
IDTB_BACK: UInt32 = 204
IDTB_HOME: UInt32 = 205
IDTB_SYNC: UInt32 = 206
IDTB_PRINT: UInt32 = 207
IDTB_OPTIONS: UInt32 = 208
IDTB_FORWARD: UInt32 = 209
IDTB_NOTES: UInt32 = 210
IDTB_BROWSE_FWD: UInt32 = 211
IDTB_BROWSE_BACK: UInt32 = 212
IDTB_CONTENTS: UInt32 = 213
IDTB_INDEX: UInt32 = 214
IDTB_SEARCH: UInt32 = 215
IDTB_HISTORY: UInt32 = 216
IDTB_FAVORITES: UInt32 = 217
IDTB_JUMP1: UInt32 = 218
IDTB_JUMP2: UInt32 = 219
IDTB_CUSTOMIZE: UInt32 = 221
IDTB_ZOOM: UInt32 = 222
IDTB_TOC_NEXT: UInt32 = 223
IDTB_TOC_PREV: UInt32 = 224
CLSID_IITPropList: Guid = Guid('4662daae-d393-11d0-9a-56-00-c0-4f-b6-8b-f7')
PROP_ADD: UInt32 = 0
PROP_DELETE: UInt32 = 1
PROP_UPDATE: UInt32 = 2
TYPE_VALUE: UInt32 = 0
TYPE_POINTER: UInt32 = 1
TYPE_STRING: UInt32 = 2
CLSID_IITDatabase: Guid = Guid('66673452-8c23-11d0-a8-4e-00-aa-00-6c-7d-01')
CLSID_IITDatabaseLocal: Guid = Guid('4662daa9-d393-11d0-9a-56-00-c0-4f-b6-8b-f7')
STDPROP_UID: UInt32 = 1
STDPROP_TITLE: UInt32 = 2
STDPROP_USERDATA: UInt32 = 3
STDPROP_KEY: UInt32 = 4
STDPROP_SORTKEY: UInt32 = 100
STDPROP_DISPLAYKEY: UInt32 = 101
STDPROP_SORTORDINAL: UInt32 = 102
STDPROP_INDEX_TEXT: UInt32 = 200
STDPROP_INDEX_VFLD: UInt32 = 201
STDPROP_INDEX_DTYPE: UInt32 = 202
STDPROP_INDEX_LENGTH: UInt32 = 203
STDPROP_INDEX_BREAK: UInt32 = 204
STDPROP_INDEX_TERM: UInt32 = 210
STDPROP_INDEX_TERM_RAW_LENGTH: UInt32 = 211
STDPROP_USERPROP_BASE: UInt32 = 65536
STDPROP_USERPROP_MAX: UInt32 = 2147483647
SZ_WWDEST_GLOBAL: String = 'GLOBAL'
SZ_WWDEST_KEY: String = 'KEY'
SZ_WWDEST_OCC: String = 'OCC'
CLSID_IITCmdInt: Guid = Guid('4662daa2-d393-11d0-9a-56-00-c0-4f-b6-8b-f7')
CLSID_IITSvMgr: Guid = Guid('4662daa3-d393-11d0-9a-56-00-c0-4f-b6-8b-f7')
CLSID_IITWordWheelUpdate: Guid = Guid('4662daa5-d393-11d0-9a-56-00-c0-4f-b6-8b-f7')
CLSID_IITGroupUpdate: Guid = Guid('4662daa4-d393-11d0-9a-56-00-c0-4f-b6-8b-f7')
CLSID_IITIndexBuild: Guid = Guid('8fa0d5aa-dedf-11d0-9a-61-00-c0-4f-b6-8b-f7')
CLSID_IITWWFilterBuild: Guid = Guid('8fa0d5ab-dedf-11d0-9a-61-00-c0-4f-b6-8b-f7')
CLSID_IITWordWheel: Guid = Guid('d73725c2-8c12-11d0-a8-4e-00-aa-00-6c-7d-01')
CLSID_IITWordWheelLocal: Guid = Guid('4662daa8-d393-11d0-9a-56-00-c0-4f-b6-8b-f7')
ITWW_OPEN_NOCONNECT: UInt32 = 1
ITWW_CBKEY_MAX: UInt32 = 1024
IITWBC_BREAK_ACCEPT_WILDCARDS: UInt32 = 1
IITWBC_BREAK_AND_STEM: UInt32 = 2
E_NOTEXIST: win32more.Foundation.HRESULT = -2147479552
E_DUPLICATE: win32more.Foundation.HRESULT = -2147479551
E_BADVERSION: win32more.Foundation.HRESULT = -2147479550
E_BADFILE: win32more.Foundation.HRESULT = -2147479549
E_BADFORMAT: win32more.Foundation.HRESULT = -2147479548
E_NOPERMISSION: win32more.Foundation.HRESULT = -2147479547
E_ASSERT: win32more.Foundation.HRESULT = -2147479546
E_INTERRUPT: win32more.Foundation.HRESULT = -2147479545
E_NOTSUPPORTED: win32more.Foundation.HRESULT = -2147479544
E_OUTOFRANGE: win32more.Foundation.HRESULT = -2147479543
E_GROUPIDTOOBIG: win32more.Foundation.HRESULT = -2147479542
E_TOOMANYTITLES: win32more.Foundation.HRESULT = -2147479541
E_NOMERGEDDATA: win32more.Foundation.HRESULT = -2147479540
E_NOTFOUND: win32more.Foundation.HRESULT = -2147479539
E_CANTFINDDLL: win32more.Foundation.HRESULT = -2147479538
E_NOHANDLE: win32more.Foundation.HRESULT = -2147479537
E_GETLASTERROR: win32more.Foundation.HRESULT = -2147479536
E_BADPARAM: win32more.Foundation.HRESULT = -2147479535
E_INVALIDSTATE: win32more.Foundation.HRESULT = -2147479534
E_NOTOPEN: win32more.Foundation.HRESULT = -2147479533
E_ALREADYOPEN: win32more.Foundation.HRESULT = -2147479533
E_UNKNOWN_TRANSPORT: win32more.Foundation.HRESULT = -2147479530
E_UNSUPPORTED_TRANSPORT: win32more.Foundation.HRESULT = -2147479529
E_BADFILTERSIZE: win32more.Foundation.HRESULT = -2147479528
E_TOOMANYOBJECTS: win32more.Foundation.HRESULT = -2147479527
E_NAMETOOLONG: win32more.Foundation.HRESULT = -2147479520
E_FILECREATE: win32more.Foundation.HRESULT = -2147479504
E_FILECLOSE: win32more.Foundation.HRESULT = -2147479503
E_FILEREAD: win32more.Foundation.HRESULT = -2147479502
E_FILESEEK: win32more.Foundation.HRESULT = -2147479501
E_FILEWRITE: win32more.Foundation.HRESULT = -2147479500
E_FILEDELETE: win32more.Foundation.HRESULT = -2147479499
E_FILEINVALID: win32more.Foundation.HRESULT = -2147479498
E_FILENOTFOUND: win32more.Foundation.HRESULT = -2147479497
E_DISKFULL: win32more.Foundation.HRESULT = -2147479496
E_TOOMANYTOPICS: win32more.Foundation.HRESULT = -2147479472
E_TOOMANYDUPS: win32more.Foundation.HRESULT = -2147479471
E_TREETOOBIG: win32more.Foundation.HRESULT = -2147479470
E_BADBREAKER: win32more.Foundation.HRESULT = -2147479469
E_BADVALUE: win32more.Foundation.HRESULT = -2147479468
E_ALL_WILD: win32more.Foundation.HRESULT = -2147479467
E_TOODEEP: win32more.Foundation.HRESULT = -2147479466
E_EXPECTEDTERM: win32more.Foundation.HRESULT = -2147479465
E_MISSLPAREN: win32more.Foundation.HRESULT = -2147479464
E_MISSRPAREN: win32more.Foundation.HRESULT = -2147479463
E_MISSQUOTE: win32more.Foundation.HRESULT = -2147479462
E_NULLQUERY: win32more.Foundation.HRESULT = -2147479461
E_STOPWORD: win32more.Foundation.HRESULT = -2147479460
E_BADRANGEOP: win32more.Foundation.HRESULT = -2147479459
E_UNMATCHEDTYPE: win32more.Foundation.HRESULT = -2147479458
E_WORDTOOLONG: win32more.Foundation.HRESULT = -2147479457
E_BADINDEXFLAGS: win32more.Foundation.HRESULT = -2147479456
E_WILD_IN_DTYPE: win32more.Foundation.HRESULT = -2147479455
E_NOSTEMMER: win32more.Foundation.HRESULT = -2147479454
E_MISSINGPROP: win32more.Foundation.HRESULT = -2147479424
E_PROPLISTNOTEMPTY: win32more.Foundation.HRESULT = -2147479423
E_PROPLISTEMPTY: win32more.Foundation.HRESULT = -2147479422
E_ALREADYINIT: win32more.Foundation.HRESULT = -2147479421
E_NOTINIT: win32more.Foundation.HRESULT = -2147479420
E_RESULTSETEMPTY: win32more.Foundation.HRESULT = -2147479419
E_TOOMANYCOLUMNS: win32more.Foundation.HRESULT = -2147479418
E_NOKEYPROP: win32more.Foundation.HRESULT = -2147479417
CLSID_IITResultSet: Guid = Guid('4662daa7-d393-11d0-9a-56-00-c0-4f-b6-8b-f7')
MAX_COLUMNS: UInt32 = 256
CLSID_ITStdBreaker: Guid = Guid('4662daaf-d393-11d0-9a-56-00-c0-4f-b6-8b-f7')
CLSID_ITEngStemmer: Guid = Guid('8fa0d5a8-dedf-11d0-9a-61-00-c0-4f-b6-8b-f7')
HHWIN_NAVTYPE_TOC: Int32 = 0
HHWIN_NAVTYPE_INDEX: Int32 = 1
HHWIN_NAVTYPE_SEARCH: Int32 = 2
HHWIN_NAVTYPE_FAVORITES: Int32 = 3
HHWIN_NAVTYPE_HISTORY: Int32 = 4
HHWIN_NAVTYPE_AUTHOR: Int32 = 5
HHWIN_NAVTYPE_CUSTOM_FIRST: Int32 = 11
IT_INCLUSIVE: Int32 = 0
IT_EXCLUSIVE: Int32 = 1
IT_HIDDEN: Int32 = 2
HHWIN_NAVTAB_TOP: Int32 = 0
HHWIN_NAVTAB_LEFT: Int32 = 1
HHWIN_NAVTAB_BOTTOM: Int32 = 2
HH_TAB_CONTENTS: Int32 = 0
HH_TAB_INDEX: Int32 = 1
HH_TAB_SEARCH: Int32 = 2
HH_TAB_FAVORITES: Int32 = 3
HH_TAB_HISTORY: Int32 = 4
HH_TAB_AUTHOR: Int32 = 5
HH_TAB_CUSTOM_FIRST: Int32 = 11
HH_TAB_CUSTOM_LAST: Int32 = 19
HHACT_TAB_CONTENTS: Int32 = 0
HHACT_TAB_INDEX: Int32 = 1
HHACT_TAB_SEARCH: Int32 = 2
HHACT_TAB_HISTORY: Int32 = 3
HHACT_TAB_FAVORITES: Int32 = 4
HHACT_EXPAND: Int32 = 5
HHACT_CONTRACT: Int32 = 6
HHACT_BACK: Int32 = 7
HHACT_FORWARD: Int32 = 8
HHACT_STOP: Int32 = 9
HHACT_REFRESH: Int32 = 10
HHACT_HOME: Int32 = 11
HHACT_SYNC: Int32 = 12
HHACT_OPTIONS: Int32 = 13
HHACT_PRINT: Int32 = 14
HHACT_HIGHLIGHT: Int32 = 15
HHACT_CUSTOMIZE: Int32 = 16
HHACT_JUMP1: Int32 = 17
HHACT_JUMP2: Int32 = 18
HHACT_ZOOM: Int32 = 19
HHACT_TOC_NEXT: Int32 = 20
HHACT_TOC_PREV: Int32 = 21
HHACT_NOTES: Int32 = 22
HHACT_LAST_ENUM: Int32 = 23
@winfunctype('htmlhelp.dll')
def HtmlHelpA(hwndCaller: win32more.Foundation.HWND, pszFile: win32more.Foundation.PSTR, uCommand: win32more.Data.HtmlHelp.HTML_HELP_COMMAND, dwData: UIntPtr) -> win32more.Foundation.HWND: ...
@winfunctype('htmlhelp.dll')
def HtmlHelpW(hwndCaller: win32more.Foundation.HWND, pszFile: win32more.Foundation.PWSTR, uCommand: win32more.Data.HtmlHelp.HTML_HELP_COMMAND, dwData: UIntPtr) -> win32more.Foundation.HWND: ...
class COLUMNSTATUS(Structure):
    cPropCount: Int32
    cPropsLoaded: Int32
class CProperty(Structure):
    dwPropID: UInt32
    cbData: UInt32
    dwType: UInt32
    Anonymous: _Anonymous_e__Union
    fPersist: win32more.Foundation.BOOL
    class _Anonymous_e__Union(Union):
        lpszwData: win32more.Foundation.PWSTR
        lpvData: c_void_p
        dwValue: UInt32
class HH_AKLINK(Structure):
    cbStruct: Int32
    fReserved: win32more.Foundation.BOOL
    pszKeywords: POINTER(SByte)
    pszUrl: POINTER(SByte)
    pszMsgText: POINTER(SByte)
    pszMsgTitle: POINTER(SByte)
    pszWindow: POINTER(SByte)
    fIndexOnFail: win32more.Foundation.BOOL
class HH_ENUM_CAT(Structure):
    cbStruct: Int32
    pszCatName: win32more.Foundation.PSTR
    pszCatDescription: win32more.Foundation.PSTR
class HH_ENUM_IT(Structure):
    cbStruct: Int32
    iType: Int32
    pszCatName: win32more.Foundation.PSTR
    pszITName: win32more.Foundation.PSTR
    pszITDescription: win32more.Foundation.PSTR
class HH_FTS_QUERY(Structure):
    cbStruct: Int32
    fUniCodeStrings: win32more.Foundation.BOOL
    pszSearchQuery: POINTER(SByte)
    iProximity: Int32
    fStemmedSearch: win32more.Foundation.BOOL
    fTitleOnly: win32more.Foundation.BOOL
    fExecute: win32more.Foundation.BOOL
    pszWindow: POINTER(SByte)
class HH_GLOBAL_PROPERTY(Structure):
    id: win32more.Data.HtmlHelp.HH_GPROPID
    var: win32more.System.Com.VARIANT
HH_GPROPID = Int32
HH_GPROPID_SINGLETHREAD: HH_GPROPID = 1
HH_GPROPID_TOOLBAR_MARGIN: HH_GPROPID = 2
HH_GPROPID_UI_LANGUAGE: HH_GPROPID = 3
HH_GPROPID_CURRENT_SUBSET: HH_GPROPID = 4
HH_GPROPID_CONTENT_LANGUAGE: HH_GPROPID = 5
class HH_POPUP(Structure):
    cbStruct: Int32
    hinst: win32more.Foundation.HINSTANCE
    idString: UInt32
    pszText: POINTER(SByte)
    pt: win32more.Foundation.POINT
    clrForeground: win32more.Foundation.COLORREF
    clrBackground: win32more.Foundation.COLORREF
    rcMargins: win32more.Foundation.RECT
    pszFont: POINTER(SByte)
class HH_SET_INFOTYPE(Structure):
    cbStruct: Int32
    pszCatName: win32more.Foundation.PSTR
    pszInfoTypeName: win32more.Foundation.PSTR
class HH_WINTYPE(Structure):
    cbStruct: Int32
    fUniCodeStrings: win32more.Foundation.BOOL
    pszType: POINTER(SByte)
    fsValidMembers: UInt32
    fsWinProperties: UInt32
    pszCaption: POINTER(SByte)
    dwStyles: UInt32
    dwExStyles: UInt32
    rcWindowPos: win32more.Foundation.RECT
    nShowState: Int32
    hwndHelp: win32more.Foundation.HWND
    hwndCaller: win32more.Foundation.HWND
    paInfoTypes: POINTER(UInt32)
    hwndToolBar: win32more.Foundation.HWND
    hwndNavigation: win32more.Foundation.HWND
    hwndHTML: win32more.Foundation.HWND
    iNavWidth: Int32
    rcHTML: win32more.Foundation.RECT
    pszToc: POINTER(SByte)
    pszIndex: POINTER(SByte)
    pszFile: POINTER(SByte)
    pszHome: POINTER(SByte)
    fsToolBarFlags: UInt32
    fNotExpanded: win32more.Foundation.BOOL
    curNavType: Int32
    tabpos: Int32
    idNotify: Int32
    tabOrder: Byte * 20
    cHistory: Int32
    pszJump1: POINTER(SByte)
    pszJump2: POINTER(SByte)
    pszUrlJump1: POINTER(SByte)
    pszUrlJump2: POINTER(SByte)
    rcMinSize: win32more.Foundation.RECT
    cbInfoTypes: Int32
    pszCustomTabs: POINTER(SByte)
class HHN_NOTIFY(Structure):
    hdr: win32more.UI.Controls.NMHDR
    pszUrl: win32more.Foundation.PSTR
class HHNTRACK(Structure):
    hdr: win32more.UI.Controls.NMHDR
    pszCurUrl: win32more.Foundation.PSTR
    idAction: Int32
    phhWinType: POINTER(win32more.Data.HtmlHelp.HH_WINTYPE_head)
HTML_HELP_COMMAND = Int32
HH_DISPLAY_TOPIC: HTML_HELP_COMMAND = 0
HH_HELP_FINDER: HTML_HELP_COMMAND = 0
HH_DISPLAY_TOC: HTML_HELP_COMMAND = 1
HH_DISPLAY_INDEX: HTML_HELP_COMMAND = 2
HH_DISPLAY_SEARCH: HTML_HELP_COMMAND = 3
HH_SET_WIN_TYPE: HTML_HELP_COMMAND = 4
HH_GET_WIN_TYPE: HTML_HELP_COMMAND = 5
HH_GET_WIN_HANDLE: HTML_HELP_COMMAND = 6
HH_ENUM_INFO_TYPE: HTML_HELP_COMMAND = 7
HH_SET_INFO_TYPE: HTML_HELP_COMMAND = 8
HH_SYNC: HTML_HELP_COMMAND = 9
HH_RESERVED1: HTML_HELP_COMMAND = 10
HH_RESERVED2: HTML_HELP_COMMAND = 11
HH_RESERVED3: HTML_HELP_COMMAND = 12
HH_KEYWORD_LOOKUP: HTML_HELP_COMMAND = 13
HH_DISPLAY_TEXT_POPUP: HTML_HELP_COMMAND = 14
HH_HELP_CONTEXT: HTML_HELP_COMMAND = 15
HH_TP_HELP_CONTEXTMENU: HTML_HELP_COMMAND = 16
HH_TP_HELP_WM_HELP: HTML_HELP_COMMAND = 17
HH_CLOSE_ALL: HTML_HELP_COMMAND = 18
HH_ALINK_LOOKUP: HTML_HELP_COMMAND = 19
HH_GET_LAST_ERROR: HTML_HELP_COMMAND = 20
HH_ENUM_CATEGORY: HTML_HELP_COMMAND = 21
HH_ENUM_CATEGORY_IT: HTML_HELP_COMMAND = 22
HH_RESET_IT_FILTER: HTML_HELP_COMMAND = 23
HH_SET_INCLUSIVE_FILTER: HTML_HELP_COMMAND = 24
HH_SET_EXCLUSIVE_FILTER: HTML_HELP_COMMAND = 25
HH_INITIALIZE: HTML_HELP_COMMAND = 28
HH_UNINITIALIZE: HTML_HELP_COMMAND = 29
HH_SET_QUERYSERVICE: HTML_HELP_COMMAND = 30
HH_PRETRANSLATEMESSAGE: HTML_HELP_COMMAND = 253
HH_SET_GLOBAL_PROPERTY: HTML_HELP_COMMAND = 252
HH_SAFE_DISPLAY_TOPIC: HTML_HELP_COMMAND = 32
HH_MAX_TABS: HTML_HELP_COMMAND = 19
HH_MAX_TABS_CUSTOM: HTML_HELP_COMMAND = 9
HH_FTS_DEFAULT_PROXIMITY: HTML_HELP_COMMAND = -1
class IITDatabase(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('8fa0d5a2-dedf-11d0-9a-61-00-c0-4f-b6-8b-f7')
    @commethod(3)
    def Open(lpszHost: win32more.Foundation.PWSTR, lpszMoniker: win32more.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Close() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def CreateObject(rclsid: POINTER(Guid), pdwObjInstance: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetObject(dwObjInstance: UInt32, riid: POINTER(Guid), ppvObj: POINTER(c_void_p)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def GetObjectPersistence(lpwszObject: win32more.Foundation.PWSTR, dwObjInstance: UInt32, ppvPersistence: POINTER(c_void_p), fStream: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
class IITGroup(Structure):
    pass
class IITPropList(c_void_p):
    extends: win32more.System.Com.IPersistStreamInit
    Guid = Guid('1f403bb1-9997-11d0-a8-50-00-aa-00-6c-7d-01')
    @commethod(9)
    def Set(PropID: UInt32, lpszwString: win32more.Foundation.PWSTR, dwOperation: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Set(PropID: UInt32, lpvData: c_void_p, cbData: UInt32, dwOperation: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Set(PropID: UInt32, dwData: UInt32, dwOperation: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Add(Prop: POINTER(win32more.Data.HtmlHelp.CProperty_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def Get(PropID: UInt32, Property: POINTER(win32more.Data.HtmlHelp.CProperty_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def Clear() -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def SetPersist(fPersist: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def SetPersist(PropID: UInt32, fPersist: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def GetFirst(Property: POINTER(win32more.Data.HtmlHelp.CProperty_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetNext(Property: POINTER(win32more.Data.HtmlHelp.CProperty_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetPropCount(cProp: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def SaveHeader(lpvData: c_void_p, dwHdrSize: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def SaveData(lpvHeader: c_void_p, dwHdrSize: UInt32, lpvData: c_void_p, dwBufSize: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def GetHeaderSize(dwHdrSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def GetDataSize(lpvHeader: c_void_p, dwHdrSize: UInt32, dwDataSize: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def SaveDataToStream(lpvHeader: c_void_p, dwHdrSize: UInt32, pStream: win32more.System.Com.IStream_head) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def LoadFromMem(lpvData: c_void_p, dwBufSize: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def SaveToMem(lpvData: c_void_p, dwBufSize: UInt32) -> win32more.Foundation.HRESULT: ...
class IITQuery(Structure):
    pass
class IITResultSet(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('3bb91d41-998b-11d0-a8-50-00-aa-00-6c-7d-01')
    @commethod(3)
    def SetColumnPriority(lColumnIndex: Int32, ColumnPriority: win32more.Data.HtmlHelp.PRIORITY) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def SetColumnHeap(lColumnIndex: Int32, lpvHeap: c_void_p, pfnColHeapFree: win32more.Data.HtmlHelp.PFNCOLHEAPFREE) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetKeyProp(PropID: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def Add(PropID: UInt32, dwDefaultData: UInt32, Priority: win32more.Data.HtmlHelp.PRIORITY) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Add(PropID: UInt32, lpszwDefault: win32more.Foundation.PWSTR, Priority: win32more.Data.HtmlHelp.PRIORITY) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Add(PropID: UInt32, lpvDefaultData: c_void_p, cbData: UInt32, Priority: win32more.Data.HtmlHelp.PRIORITY) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Add(lpvHdr: c_void_p) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Append(lpvHdr: c_void_p, lpvData: c_void_p) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def Set(lRowIndex: Int32, lColumnIndex: Int32, lpvData: c_void_p, cbData: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def Set(lRowIndex: Int32, lColumnIndex: Int32, lpwStr: win32more.Foundation.PWSTR) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def Set(lRowIndex: Int32, lColumnIndex: Int32, dwData: UIntPtr) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def Set(lRowIndex: Int32, lpvHdr: c_void_p, lpvData: c_void_p) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def Copy(pRSCopy: win32more.Data.HtmlHelp.IITResultSet_head) -> win32more.Foundation.HRESULT: ...
    @commethod(16)
    def AppendRows(pResSrc: win32more.Data.HtmlHelp.IITResultSet_head, lRowSrcFirst: Int32, cSrcRows: Int32, lRowFirstDest: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(17)
    def Get(lRowIndex: Int32, lColumnIndex: Int32, Prop: POINTER(win32more.Data.HtmlHelp.CProperty_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(18)
    def GetKeyProp(KeyPropID: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(19)
    def GetColumnPriority(lColumnIndex: Int32, ColumnPriority: POINTER(win32more.Data.HtmlHelp.PRIORITY)) -> win32more.Foundation.HRESULT: ...
    @commethod(20)
    def GetRowCount(lNumberOfRows: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(21)
    def GetColumnCount(lNumberOfColumns: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(22)
    def GetColumn(lColumnIndex: Int32, PropID: POINTER(UInt32), dwType: POINTER(UInt32), lpvDefaultValue: POINTER(c_void_p), cbSize: POINTER(UInt32), ColumnPriority: POINTER(win32more.Data.HtmlHelp.PRIORITY)) -> win32more.Foundation.HRESULT: ...
    @commethod(23)
    def GetColumn(lColumnIndex: Int32, PropID: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(24)
    def GetColumnFromPropID(PropID: UInt32, lColumnIndex: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(25)
    def Clear() -> win32more.Foundation.HRESULT: ...
    @commethod(26)
    def ClearRows() -> win32more.Foundation.HRESULT: ...
    @commethod(27)
    def Free() -> win32more.Foundation.HRESULT: ...
    @commethod(28)
    def IsCompleted() -> win32more.Foundation.HRESULT: ...
    @commethod(29)
    def Cancel() -> win32more.Foundation.HRESULT: ...
    @commethod(30)
    def Pause(fPause: win32more.Foundation.BOOL) -> win32more.Foundation.HRESULT: ...
    @commethod(31)
    def GetRowStatus(lRowFirst: Int32, cRows: Int32, lpRowStatus: POINTER(win32more.Data.HtmlHelp.ROWSTATUS_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(32)
    def GetColumnStatus(lpColStatus: POINTER(win32more.Data.HtmlHelp.COLUMNSTATUS_head)) -> win32more.Foundation.HRESULT: ...
class IITStopWordList(Structure):
    pass
class IITWordWheel(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('8fa0d5a4-dedf-11d0-9a-61-00-c0-4f-b6-8b-f7')
    @commethod(3)
    def Open(lpITDB: win32more.Data.HtmlHelp.IITDatabase_head, lpszMoniker: win32more.Foundation.PWSTR, dwFlags: win32more.Data.HtmlHelp.WORD_WHEEL_OPEN_FLAGS) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def Close() -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def GetLocaleInfo(pdwCodePageID: POINTER(UInt32), plcid: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetSorterInstance(pdwObjInstance: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def Count(pcEntries: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def Lookup(lpcvPrefix: c_void_p, fExactMatch: win32more.Foundation.BOOL, plEntry: POINTER(Int32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def Lookup(lEntry: Int32, lpITResult: win32more.Data.HtmlHelp.IITResultSet_head, cEntries: Int32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def Lookup(lEntry: Int32, lpvKeyBuf: c_void_p, cbKeyBuf: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def SetGroup(piitGroup: POINTER(win32more.Data.HtmlHelp.IITGroup_head)) -> win32more.Foundation.HRESULT: ...
    @commethod(12)
    def GetGroup(ppiitGroup: POINTER(POINTER(win32more.Data.HtmlHelp.IITGroup_head))) -> win32more.Foundation.HRESULT: ...
    @commethod(13)
    def GetDataCount(lEntry: Int32, pdwCount: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(14)
    def GetData(lEntry: Int32, lpITResult: win32more.Data.HtmlHelp.IITResultSet_head) -> win32more.Foundation.HRESULT: ...
    @commethod(15)
    def GetDataColumns(pRS: win32more.Data.HtmlHelp.IITResultSet_head) -> win32more.Foundation.HRESULT: ...
class IStemmerConfig(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('8fa0d5a7-dedf-11d0-9a-61-00-c0-4f-b6-8b-f7')
    @commethod(3)
    def SetLocaleInfo(dwCodePageID: UInt32, lcid: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLocaleInfo(pdwCodePageID: POINTER(UInt32), plcid: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetControlInfo(grfStemFlags: UInt32, dwReserved: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetControlInfo(pgrfStemFlags: POINTER(UInt32), pdwReserved: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def LoadExternalStemmerData(pStream: win32more.System.Com.IStream_head, dwExtDataType: UInt32) -> win32more.Foundation.HRESULT: ...
class IStemSink(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('fe77c330-7f42-11ce-be-57-00-aa-00-51-fe-20')
    @commethod(3)
    def PutAltWord(pwcInBuf: win32more.Foundation.PWSTR, cwc: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def PutWord(pwcInBuf: win32more.Foundation.PWSTR, cwc: UInt32) -> win32more.Foundation.HRESULT: ...
class IWordBreakerConfig(c_void_p):
    extends: win32more.System.Com.IUnknown
    Guid = Guid('8fa0d5a6-dedf-11d0-9a-61-00-c0-4f-b6-8b-f7')
    @commethod(3)
    def SetLocaleInfo(dwCodePageID: UInt32, lcid: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(4)
    def GetLocaleInfo(pdwCodePageID: POINTER(UInt32), plcid: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(5)
    def SetBreakWordType(dwBreakWordType: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(6)
    def GetBreakWordType(pdwBreakWordType: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(7)
    def SetControlInfo(grfBreakFlags: UInt32, dwReserved: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(8)
    def GetControlInfo(pgrfBreakFlags: POINTER(UInt32), pdwReserved: POINTER(UInt32)) -> win32more.Foundation.HRESULT: ...
    @commethod(9)
    def LoadExternalBreakerData(pStream: win32more.System.Com.IStream_head, dwExtDataType: UInt32) -> win32more.Foundation.HRESULT: ...
    @commethod(10)
    def SetWordStemmer(rclsid: POINTER(Guid), pStemmer: win32more.System.Search.IStemmer_head) -> win32more.Foundation.HRESULT: ...
    @commethod(11)
    def GetWordStemmer(ppStemmer: POINTER(win32more.System.Search.IStemmer_head)) -> win32more.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNCOLHEAPFREE(param0: c_void_p) -> Int32: ...
PRIORITY = Int32
PRIORITY_LOW: PRIORITY = 0
PRIORITY_NORMAL: PRIORITY = 1
PRIORITY_HIGH: PRIORITY = 2
class ROWSTATUS(Structure):
    lRowFirst: Int32
    cRows: Int32
    cProperties: Int32
    cRowsTotal: Int32
WORD_WHEEL_OPEN_FLAGS = UInt32
ITWW_OPEN_CONNECT: WORD_WHEEL_OPEN_FLAGS = 0
make_head(_module, 'COLUMNSTATUS')
make_head(_module, 'CProperty')
make_head(_module, 'HH_AKLINK')
make_head(_module, 'HH_ENUM_CAT')
make_head(_module, 'HH_ENUM_IT')
make_head(_module, 'HH_FTS_QUERY')
make_head(_module, 'HH_GLOBAL_PROPERTY')
make_head(_module, 'HH_POPUP')
make_head(_module, 'HH_SET_INFOTYPE')
make_head(_module, 'HH_WINTYPE')
make_head(_module, 'HHN_NOTIFY')
make_head(_module, 'HHNTRACK')
make_head(_module, 'IITDatabase')
make_head(_module, 'IITGroup')
make_head(_module, 'IITPropList')
make_head(_module, 'IITQuery')
make_head(_module, 'IITResultSet')
make_head(_module, 'IITStopWordList')
make_head(_module, 'IITWordWheel')
make_head(_module, 'IStemmerConfig')
make_head(_module, 'IStemSink')
make_head(_module, 'IWordBreakerConfig')
make_head(_module, 'PFNCOLHEAPFREE')
make_head(_module, 'ROWSTATUS')
__all__ = [
    "CLSID_IITCmdInt",
    "CLSID_IITDatabase",
    "CLSID_IITDatabaseLocal",
    "CLSID_IITGroupUpdate",
    "CLSID_IITIndexBuild",
    "CLSID_IITPropList",
    "CLSID_IITResultSet",
    "CLSID_IITSvMgr",
    "CLSID_IITWWFilterBuild",
    "CLSID_IITWordWheel",
    "CLSID_IITWordWheelLocal",
    "CLSID_IITWordWheelUpdate",
    "CLSID_ITEngStemmer",
    "CLSID_ITStdBreaker",
    "COLUMNSTATUS",
    "CProperty",
    "E_ALL_WILD",
    "E_ALREADYINIT",
    "E_ALREADYOPEN",
    "E_ASSERT",
    "E_BADBREAKER",
    "E_BADFILE",
    "E_BADFILTERSIZE",
    "E_BADFORMAT",
    "E_BADINDEXFLAGS",
    "E_BADPARAM",
    "E_BADRANGEOP",
    "E_BADVALUE",
    "E_BADVERSION",
    "E_CANTFINDDLL",
    "E_DISKFULL",
    "E_DUPLICATE",
    "E_EXPECTEDTERM",
    "E_FILECLOSE",
    "E_FILECREATE",
    "E_FILEDELETE",
    "E_FILEINVALID",
    "E_FILENOTFOUND",
    "E_FILEREAD",
    "E_FILESEEK",
    "E_FILEWRITE",
    "E_GETLASTERROR",
    "E_GROUPIDTOOBIG",
    "E_INTERRUPT",
    "E_INVALIDSTATE",
    "E_MISSINGPROP",
    "E_MISSLPAREN",
    "E_MISSQUOTE",
    "E_MISSRPAREN",
    "E_NAMETOOLONG",
    "E_NOHANDLE",
    "E_NOKEYPROP",
    "E_NOMERGEDDATA",
    "E_NOPERMISSION",
    "E_NOSTEMMER",
    "E_NOTEXIST",
    "E_NOTFOUND",
    "E_NOTINIT",
    "E_NOTOPEN",
    "E_NOTSUPPORTED",
    "E_NULLQUERY",
    "E_OUTOFRANGE",
    "E_PROPLISTEMPTY",
    "E_PROPLISTNOTEMPTY",
    "E_RESULTSETEMPTY",
    "E_STOPWORD",
    "E_TOODEEP",
    "E_TOOMANYCOLUMNS",
    "E_TOOMANYDUPS",
    "E_TOOMANYOBJECTS",
    "E_TOOMANYTITLES",
    "E_TOOMANYTOPICS",
    "E_TREETOOBIG",
    "E_UNKNOWN_TRANSPORT",
    "E_UNMATCHEDTYPE",
    "E_UNSUPPORTED_TRANSPORT",
    "E_WILD_IN_DTYPE",
    "E_WORDTOOLONG",
    "HHACT_BACK",
    "HHACT_CONTRACT",
    "HHACT_CUSTOMIZE",
    "HHACT_EXPAND",
    "HHACT_FORWARD",
    "HHACT_HIGHLIGHT",
    "HHACT_HOME",
    "HHACT_JUMP1",
    "HHACT_JUMP2",
    "HHACT_LAST_ENUM",
    "HHACT_NOTES",
    "HHACT_OPTIONS",
    "HHACT_PRINT",
    "HHACT_REFRESH",
    "HHACT_STOP",
    "HHACT_SYNC",
    "HHACT_TAB_CONTENTS",
    "HHACT_TAB_FAVORITES",
    "HHACT_TAB_HISTORY",
    "HHACT_TAB_INDEX",
    "HHACT_TAB_SEARCH",
    "HHACT_TOC_NEXT",
    "HHACT_TOC_PREV",
    "HHACT_ZOOM",
    "HHNTRACK",
    "HHN_NOTIFY",
    "HHWIN_BUTTON_BACK",
    "HHWIN_BUTTON_BROWSE_BCK",
    "HHWIN_BUTTON_BROWSE_FWD",
    "HHWIN_BUTTON_CONTENTS",
    "HHWIN_BUTTON_EXPAND",
    "HHWIN_BUTTON_FAVORITES",
    "HHWIN_BUTTON_FORWARD",
    "HHWIN_BUTTON_HISTORY",
    "HHWIN_BUTTON_HOME",
    "HHWIN_BUTTON_INDEX",
    "HHWIN_BUTTON_JUMP1",
    "HHWIN_BUTTON_JUMP2",
    "HHWIN_BUTTON_NOTES",
    "HHWIN_BUTTON_OPTIONS",
    "HHWIN_BUTTON_PRINT",
    "HHWIN_BUTTON_REFRESH",
    "HHWIN_BUTTON_SEARCH",
    "HHWIN_BUTTON_STOP",
    "HHWIN_BUTTON_SYNC",
    "HHWIN_BUTTON_TOC_NEXT",
    "HHWIN_BUTTON_TOC_PREV",
    "HHWIN_BUTTON_ZOOM",
    "HHWIN_NAVTAB_BOTTOM",
    "HHWIN_NAVTAB_LEFT",
    "HHWIN_NAVTAB_TOP",
    "HHWIN_NAVTYPE_AUTHOR",
    "HHWIN_NAVTYPE_CUSTOM_FIRST",
    "HHWIN_NAVTYPE_FAVORITES",
    "HHWIN_NAVTYPE_HISTORY",
    "HHWIN_NAVTYPE_INDEX",
    "HHWIN_NAVTYPE_SEARCH",
    "HHWIN_NAVTYPE_TOC",
    "HHWIN_PARAM_CUR_TAB",
    "HHWIN_PARAM_EXPANSION",
    "HHWIN_PARAM_EXSTYLES",
    "HHWIN_PARAM_HISTORY_COUNT",
    "HHWIN_PARAM_INFOTYPES",
    "HHWIN_PARAM_NAV_WIDTH",
    "HHWIN_PARAM_PROPERTIES",
    "HHWIN_PARAM_RECT",
    "HHWIN_PARAM_SHOWSTATE",
    "HHWIN_PARAM_STYLES",
    "HHWIN_PARAM_TABORDER",
    "HHWIN_PARAM_TABPOS",
    "HHWIN_PARAM_TB_FLAGS",
    "HHWIN_PROP_AUTO_SYNC",
    "HHWIN_PROP_CHANGE_TITLE",
    "HHWIN_PROP_MENU",
    "HHWIN_PROP_NAV_ONLY_WIN",
    "HHWIN_PROP_NODEF_EXSTYLES",
    "HHWIN_PROP_NODEF_STYLES",
    "HHWIN_PROP_NOTB_TEXT",
    "HHWIN_PROP_NOTITLEBAR",
    "HHWIN_PROP_NO_TOOLBAR",
    "HHWIN_PROP_ONTOP",
    "HHWIN_PROP_POST_QUIT",
    "HHWIN_PROP_TAB_ADVSEARCH",
    "HHWIN_PROP_TAB_AUTOHIDESHOW",
    "HHWIN_PROP_TAB_CUSTOM1",
    "HHWIN_PROP_TAB_CUSTOM2",
    "HHWIN_PROP_TAB_CUSTOM3",
    "HHWIN_PROP_TAB_CUSTOM4",
    "HHWIN_PROP_TAB_CUSTOM5",
    "HHWIN_PROP_TAB_CUSTOM6",
    "HHWIN_PROP_TAB_CUSTOM7",
    "HHWIN_PROP_TAB_CUSTOM8",
    "HHWIN_PROP_TAB_CUSTOM9",
    "HHWIN_PROP_TAB_FAVORITES",
    "HHWIN_PROP_TAB_HISTORY",
    "HHWIN_PROP_TAB_SEARCH",
    "HHWIN_PROP_TRACKING",
    "HHWIN_PROP_TRI_PANE",
    "HHWIN_PROP_USER_POS",
    "HHWIN_TB_MARGIN",
    "HH_AKLINK",
    "HH_ALINK_LOOKUP",
    "HH_CLOSE_ALL",
    "HH_DISPLAY_INDEX",
    "HH_DISPLAY_SEARCH",
    "HH_DISPLAY_TEXT_POPUP",
    "HH_DISPLAY_TOC",
    "HH_DISPLAY_TOPIC",
    "HH_ENUM_CAT",
    "HH_ENUM_CATEGORY",
    "HH_ENUM_CATEGORY_IT",
    "HH_ENUM_INFO_TYPE",
    "HH_ENUM_IT",
    "HH_FTS_DEFAULT_PROXIMITY",
    "HH_FTS_QUERY",
    "HH_GET_LAST_ERROR",
    "HH_GET_WIN_HANDLE",
    "HH_GET_WIN_TYPE",
    "HH_GLOBAL_PROPERTY",
    "HH_GPROPID",
    "HH_GPROPID_CONTENT_LANGUAGE",
    "HH_GPROPID_CURRENT_SUBSET",
    "HH_GPROPID_SINGLETHREAD",
    "HH_GPROPID_TOOLBAR_MARGIN",
    "HH_GPROPID_UI_LANGUAGE",
    "HH_HELP_CONTEXT",
    "HH_HELP_FINDER",
    "HH_INITIALIZE",
    "HH_KEYWORD_LOOKUP",
    "HH_MAX_TABS",
    "HH_MAX_TABS_CUSTOM",
    "HH_POPUP",
    "HH_PRETRANSLATEMESSAGE",
    "HH_RESERVED1",
    "HH_RESERVED2",
    "HH_RESERVED3",
    "HH_RESET_IT_FILTER",
    "HH_SAFE_DISPLAY_TOPIC",
    "HH_SET_EXCLUSIVE_FILTER",
    "HH_SET_GLOBAL_PROPERTY",
    "HH_SET_INCLUSIVE_FILTER",
    "HH_SET_INFOTYPE",
    "HH_SET_INFO_TYPE",
    "HH_SET_QUERYSERVICE",
    "HH_SET_WIN_TYPE",
    "HH_SYNC",
    "HH_TAB_AUTHOR",
    "HH_TAB_CONTENTS",
    "HH_TAB_CUSTOM_FIRST",
    "HH_TAB_CUSTOM_LAST",
    "HH_TAB_FAVORITES",
    "HH_TAB_HISTORY",
    "HH_TAB_INDEX",
    "HH_TAB_SEARCH",
    "HH_TP_HELP_CONTEXTMENU",
    "HH_TP_HELP_WM_HELP",
    "HH_UNINITIALIZE",
    "HH_WINTYPE",
    "HTML_HELP_COMMAND",
    "HtmlHelpA",
    "HtmlHelpW",
    "IDTB_BACK",
    "IDTB_BROWSE_BACK",
    "IDTB_BROWSE_FWD",
    "IDTB_CONTENTS",
    "IDTB_CONTRACT",
    "IDTB_CUSTOMIZE",
    "IDTB_EXPAND",
    "IDTB_FAVORITES",
    "IDTB_FORWARD",
    "IDTB_HISTORY",
    "IDTB_HOME",
    "IDTB_INDEX",
    "IDTB_JUMP1",
    "IDTB_JUMP2",
    "IDTB_NOTES",
    "IDTB_OPTIONS",
    "IDTB_PRINT",
    "IDTB_REFRESH",
    "IDTB_SEARCH",
    "IDTB_STOP",
    "IDTB_SYNC",
    "IDTB_TOC_NEXT",
    "IDTB_TOC_PREV",
    "IDTB_ZOOM",
    "IITDatabase",
    "IITGroup",
    "IITPropList",
    "IITQuery",
    "IITResultSet",
    "IITStopWordList",
    "IITWBC_BREAK_ACCEPT_WILDCARDS",
    "IITWBC_BREAK_AND_STEM",
    "IITWordWheel",
    "IStemSink",
    "IStemmerConfig",
    "ITWW_CBKEY_MAX",
    "ITWW_OPEN_CONNECT",
    "ITWW_OPEN_NOCONNECT",
    "IT_EXCLUSIVE",
    "IT_HIDDEN",
    "IT_INCLUSIVE",
    "IWordBreakerConfig",
    "MAX_COLUMNS",
    "PFNCOLHEAPFREE",
    "PRIORITY",
    "PRIORITY_HIGH",
    "PRIORITY_LOW",
    "PRIORITY_NORMAL",
    "PROP_ADD",
    "PROP_DELETE",
    "PROP_UPDATE",
    "ROWSTATUS",
    "STDPROP_DISPLAYKEY",
    "STDPROP_INDEX_BREAK",
    "STDPROP_INDEX_DTYPE",
    "STDPROP_INDEX_LENGTH",
    "STDPROP_INDEX_TERM",
    "STDPROP_INDEX_TERM_RAW_LENGTH",
    "STDPROP_INDEX_TEXT",
    "STDPROP_INDEX_VFLD",
    "STDPROP_KEY",
    "STDPROP_SORTKEY",
    "STDPROP_SORTORDINAL",
    "STDPROP_TITLE",
    "STDPROP_UID",
    "STDPROP_USERDATA",
    "STDPROP_USERPROP_BASE",
    "STDPROP_USERPROP_MAX",
    "SZ_WWDEST_GLOBAL",
    "SZ_WWDEST_KEY",
    "SZ_WWDEST_OCC",
    "TYPE_POINTER",
    "TYPE_STRING",
    "TYPE_VALUE",
    "WORD_WHEEL_OPEN_FLAGS",
]
_arch_optional = [
]
