from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Data.HtmlHelp
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.Search
import Windows.Win32.System.Variant
import Windows.Win32.UI.Controls
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
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
HHN_FIRST: UInt32 = 4294966436
HHN_LAST: UInt32 = 4294966417
HHN_NAVCOMPLETE: UInt32 = 4294966436
HHN_TRACK: UInt32 = 4294966435
HHN_WINDOW_CREATE: UInt32 = 4294966434
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
E_NOTEXIST: Windows.Win32.Foundation.HRESULT = -2147479552
E_DUPLICATE: Windows.Win32.Foundation.HRESULT = -2147479551
E_BADVERSION: Windows.Win32.Foundation.HRESULT = -2147479550
E_BADFILE: Windows.Win32.Foundation.HRESULT = -2147479549
E_BADFORMAT: Windows.Win32.Foundation.HRESULT = -2147479548
E_NOPERMISSION: Windows.Win32.Foundation.HRESULT = -2147479547
E_ASSERT: Windows.Win32.Foundation.HRESULT = -2147479546
E_INTERRUPT: Windows.Win32.Foundation.HRESULT = -2147479545
E_NOTSUPPORTED: Windows.Win32.Foundation.HRESULT = -2147479544
E_OUTOFRANGE: Windows.Win32.Foundation.HRESULT = -2147479543
E_GROUPIDTOOBIG: Windows.Win32.Foundation.HRESULT = -2147479542
E_TOOMANYTITLES: Windows.Win32.Foundation.HRESULT = -2147479541
E_NOMERGEDDATA: Windows.Win32.Foundation.HRESULT = -2147479540
E_NOTFOUND: Windows.Win32.Foundation.HRESULT = -2147479539
E_CANTFINDDLL: Windows.Win32.Foundation.HRESULT = -2147479538
E_NOHANDLE: Windows.Win32.Foundation.HRESULT = -2147479537
E_GETLASTERROR: Windows.Win32.Foundation.HRESULT = -2147479536
E_BADPARAM: Windows.Win32.Foundation.HRESULT = -2147479535
E_INVALIDSTATE: Windows.Win32.Foundation.HRESULT = -2147479534
E_NOTOPEN: Windows.Win32.Foundation.HRESULT = -2147479533
E_ALREADYOPEN: Windows.Win32.Foundation.HRESULT = -2147479533
E_UNKNOWN_TRANSPORT: Windows.Win32.Foundation.HRESULT = -2147479530
E_UNSUPPORTED_TRANSPORT: Windows.Win32.Foundation.HRESULT = -2147479529
E_BADFILTERSIZE: Windows.Win32.Foundation.HRESULT = -2147479528
E_TOOMANYOBJECTS: Windows.Win32.Foundation.HRESULT = -2147479527
E_NAMETOOLONG: Windows.Win32.Foundation.HRESULT = -2147479520
E_FILECREATE: Windows.Win32.Foundation.HRESULT = -2147479504
E_FILECLOSE: Windows.Win32.Foundation.HRESULT = -2147479503
E_FILEREAD: Windows.Win32.Foundation.HRESULT = -2147479502
E_FILESEEK: Windows.Win32.Foundation.HRESULT = -2147479501
E_FILEWRITE: Windows.Win32.Foundation.HRESULT = -2147479500
E_FILEDELETE: Windows.Win32.Foundation.HRESULT = -2147479499
E_FILEINVALID: Windows.Win32.Foundation.HRESULT = -2147479498
E_FILENOTFOUND: Windows.Win32.Foundation.HRESULT = -2147479497
E_DISKFULL: Windows.Win32.Foundation.HRESULT = -2147479496
E_TOOMANYTOPICS: Windows.Win32.Foundation.HRESULT = -2147479472
E_TOOMANYDUPS: Windows.Win32.Foundation.HRESULT = -2147479471
E_TREETOOBIG: Windows.Win32.Foundation.HRESULT = -2147479470
E_BADBREAKER: Windows.Win32.Foundation.HRESULT = -2147479469
E_BADVALUE: Windows.Win32.Foundation.HRESULT = -2147479468
E_ALL_WILD: Windows.Win32.Foundation.HRESULT = -2147479467
E_TOODEEP: Windows.Win32.Foundation.HRESULT = -2147479466
E_EXPECTEDTERM: Windows.Win32.Foundation.HRESULT = -2147479465
E_MISSLPAREN: Windows.Win32.Foundation.HRESULT = -2147479464
E_MISSRPAREN: Windows.Win32.Foundation.HRESULT = -2147479463
E_MISSQUOTE: Windows.Win32.Foundation.HRESULT = -2147479462
E_NULLQUERY: Windows.Win32.Foundation.HRESULT = -2147479461
E_STOPWORD: Windows.Win32.Foundation.HRESULT = -2147479460
E_BADRANGEOP: Windows.Win32.Foundation.HRESULT = -2147479459
E_UNMATCHEDTYPE: Windows.Win32.Foundation.HRESULT = -2147479458
E_WORDTOOLONG: Windows.Win32.Foundation.HRESULT = -2147479457
E_BADINDEXFLAGS: Windows.Win32.Foundation.HRESULT = -2147479456
E_WILD_IN_DTYPE: Windows.Win32.Foundation.HRESULT = -2147479455
E_NOSTEMMER: Windows.Win32.Foundation.HRESULT = -2147479454
E_MISSINGPROP: Windows.Win32.Foundation.HRESULT = -2147479424
E_PROPLISTNOTEMPTY: Windows.Win32.Foundation.HRESULT = -2147479423
E_PROPLISTEMPTY: Windows.Win32.Foundation.HRESULT = -2147479422
E_ALREADYINIT: Windows.Win32.Foundation.HRESULT = -2147479421
E_NOTINIT: Windows.Win32.Foundation.HRESULT = -2147479420
E_RESULTSETEMPTY: Windows.Win32.Foundation.HRESULT = -2147479419
E_TOOMANYCOLUMNS: Windows.Win32.Foundation.HRESULT = -2147479418
E_NOKEYPROP: Windows.Win32.Foundation.HRESULT = -2147479417
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
def HtmlHelpA(hwndCaller: Windows.Win32.Foundation.HWND, pszFile: Windows.Win32.Foundation.PSTR, uCommand: Windows.Win32.Data.HtmlHelp.HTML_HELP_COMMAND, dwData: UIntPtr) -> Windows.Win32.Foundation.HWND: ...
@winfunctype('htmlhelp.dll')
def HtmlHelpW(hwndCaller: Windows.Win32.Foundation.HWND, pszFile: Windows.Win32.Foundation.PWSTR, uCommand: Windows.Win32.Data.HtmlHelp.HTML_HELP_COMMAND, dwData: UIntPtr) -> Windows.Win32.Foundation.HWND: ...
class COLUMNSTATUS(EasyCastStructure):
    cPropCount: Int32
    cPropsLoaded: Int32
class CProperty(EasyCastStructure):
    dwPropID: UInt32
    cbData: UInt32
    dwType: UInt32
    Anonymous: _Anonymous_e__Union
    fPersist: Windows.Win32.Foundation.BOOL
    class _Anonymous_e__Union(EasyCastUnion):
        lpszwData: Windows.Win32.Foundation.PWSTR
        lpvData: c_void_p
        dwValue: UInt32
class HHNTRACK(EasyCastStructure):
    hdr: Windows.Win32.UI.Controls.NMHDR
    pszCurUrl: Windows.Win32.Foundation.PSTR
    idAction: Int32
    phhWinType: POINTER(Windows.Win32.Data.HtmlHelp.HH_WINTYPE_head)
class HHN_NOTIFY(EasyCastStructure):
    hdr: Windows.Win32.UI.Controls.NMHDR
    pszUrl: Windows.Win32.Foundation.PSTR
class HH_AKLINK(EasyCastStructure):
    cbStruct: Int32
    fReserved: Windows.Win32.Foundation.BOOL
    pszKeywords: POINTER(SByte)
    pszUrl: POINTER(SByte)
    pszMsgText: POINTER(SByte)
    pszMsgTitle: POINTER(SByte)
    pszWindow: POINTER(SByte)
    fIndexOnFail: Windows.Win32.Foundation.BOOL
class HH_ENUM_CAT(EasyCastStructure):
    cbStruct: Int32
    pszCatName: Windows.Win32.Foundation.PSTR
    pszCatDescription: Windows.Win32.Foundation.PSTR
class HH_ENUM_IT(EasyCastStructure):
    cbStruct: Int32
    iType: Int32
    pszCatName: Windows.Win32.Foundation.PSTR
    pszITName: Windows.Win32.Foundation.PSTR
    pszITDescription: Windows.Win32.Foundation.PSTR
class HH_FTS_QUERY(EasyCastStructure):
    cbStruct: Int32
    fUniCodeStrings: Windows.Win32.Foundation.BOOL
    pszSearchQuery: POINTER(SByte)
    iProximity: Int32
    fStemmedSearch: Windows.Win32.Foundation.BOOL
    fTitleOnly: Windows.Win32.Foundation.BOOL
    fExecute: Windows.Win32.Foundation.BOOL
    pszWindow: POINTER(SByte)
class HH_GLOBAL_PROPERTY(EasyCastStructure):
    id: Windows.Win32.Data.HtmlHelp.HH_GPROPID
    var: Windows.Win32.System.Variant.VARIANT
HH_GPROPID = Int32
HH_GPROPID_SINGLETHREAD: HH_GPROPID = 1
HH_GPROPID_TOOLBAR_MARGIN: HH_GPROPID = 2
HH_GPROPID_UI_LANGUAGE: HH_GPROPID = 3
HH_GPROPID_CURRENT_SUBSET: HH_GPROPID = 4
HH_GPROPID_CONTENT_LANGUAGE: HH_GPROPID = 5
class HH_POPUP(EasyCastStructure):
    cbStruct: Int32
    hinst: Windows.Win32.Foundation.HMODULE
    idString: UInt32
    pszText: POINTER(SByte)
    pt: Windows.Win32.Foundation.POINT
    clrForeground: Windows.Win32.Foundation.COLORREF
    clrBackground: Windows.Win32.Foundation.COLORREF
    rcMargins: Windows.Win32.Foundation.RECT
    pszFont: POINTER(SByte)
class HH_SET_INFOTYPE(EasyCastStructure):
    cbStruct: Int32
    pszCatName: Windows.Win32.Foundation.PSTR
    pszInfoTypeName: Windows.Win32.Foundation.PSTR
class HH_WINTYPE(EasyCastStructure):
    cbStruct: Int32
    fUniCodeStrings: Windows.Win32.Foundation.BOOL
    pszType: POINTER(SByte)
    fsValidMembers: UInt32
    fsWinProperties: UInt32
    pszCaption: POINTER(SByte)
    dwStyles: UInt32
    dwExStyles: UInt32
    rcWindowPos: Windows.Win32.Foundation.RECT
    nShowState: Int32
    hwndHelp: Windows.Win32.Foundation.HWND
    hwndCaller: Windows.Win32.Foundation.HWND
    paInfoTypes: POINTER(UInt32)
    hwndToolBar: Windows.Win32.Foundation.HWND
    hwndNavigation: Windows.Win32.Foundation.HWND
    hwndHTML: Windows.Win32.Foundation.HWND
    iNavWidth: Int32
    rcHTML: Windows.Win32.Foundation.RECT
    pszToc: POINTER(SByte)
    pszIndex: POINTER(SByte)
    pszFile: POINTER(SByte)
    pszHome: POINTER(SByte)
    fsToolBarFlags: UInt32
    fNotExpanded: Windows.Win32.Foundation.BOOL
    curNavType: Int32
    tabpos: Int32
    idNotify: Int32
    tabOrder: Byte * 20
    cHistory: Int32
    pszJump1: POINTER(SByte)
    pszJump2: POINTER(SByte)
    pszUrlJump1: POINTER(SByte)
    pszUrlJump2: POINTER(SByte)
    rcMinSize: Windows.Win32.Foundation.RECT
    cbInfoTypes: Int32
    pszCustomTabs: POINTER(SByte)
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
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8fa0d5a2-dedf-11d0-9a-61-00-c0-4f-b6-8b-f7')
    @commethod(3)
    def Open(self, lpszHost: Windows.Win32.Foundation.PWSTR, lpszMoniker: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateObject(self, rclsid: POINTER(Guid), pdwObjInstance: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetObject(self, dwObjInstance: UInt32, riid: POINTER(Guid), ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetObjectPersistence(self, lpwszObject: Windows.Win32.Foundation.PWSTR, dwObjInstance: UInt32, ppvPersistence: POINTER(c_void_p), fStream: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IITPropList(c_void_p):
    extends: Windows.Win32.System.Com.IPersistStreamInit
    Guid = Guid('1f403bb1-9997-11d0-a8-50-00-aa-00-6c-7d-01')
    @commethod(9)
    def Set(self, PropID: UInt32, lpszwString: Windows.Win32.Foundation.PWSTR, dwOperation: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Set(self, PropID: UInt32, lpvData: c_void_p, cbData: UInt32, dwOperation: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Set(self, PropID: UInt32, dwData: UInt32, dwOperation: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Add(self, Prop: POINTER(Windows.Win32.Data.HtmlHelp.CProperty_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Get(self, PropID: UInt32, Property: POINTER(Windows.Win32.Data.HtmlHelp.CProperty_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Clear(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetPersist(self, fPersist: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetPersist(self, PropID: UInt32, fPersist: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetFirst(self, Property: POINTER(Windows.Win32.Data.HtmlHelp.CProperty_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetNext(self, Property: POINTER(Windows.Win32.Data.HtmlHelp.CProperty_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetPropCount(self, cProp: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SaveHeader(self, lpvData: c_void_p, dwHdrSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SaveData(self, lpvHeader: c_void_p, dwHdrSize: UInt32, lpvData: c_void_p, dwBufSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetHeaderSize(self, dwHdrSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetDataSize(self, lpvHeader: c_void_p, dwHdrSize: UInt32, dwDataSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SaveDataToStream(self, lpvHeader: c_void_p, dwHdrSize: UInt32, pStream: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def LoadFromMem(self, lpvData: c_void_p, dwBufSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def SaveToMem(self, lpvData: c_void_p, dwBufSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IITResultSet(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3bb91d41-998b-11d0-a8-50-00-aa-00-6c-7d-01')
    @commethod(3)
    def SetColumnPriority(self, lColumnIndex: Int32, ColumnPriority: Windows.Win32.Data.HtmlHelp.PRIORITY) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetColumnHeap(self, lColumnIndex: Int32, lpvHeap: c_void_p, pfnColHeapFree: Windows.Win32.Data.HtmlHelp.PFNCOLHEAPFREE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetKeyProp(self, PropID: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Add(self, PropID: UInt32, dwDefaultData: UInt32, Priority: Windows.Win32.Data.HtmlHelp.PRIORITY) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Add(self, PropID: UInt32, lpszwDefault: Windows.Win32.Foundation.PWSTR, Priority: Windows.Win32.Data.HtmlHelp.PRIORITY) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Add(self, PropID: UInt32, lpvDefaultData: c_void_p, cbData: UInt32, Priority: Windows.Win32.Data.HtmlHelp.PRIORITY) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Add(self, lpvHdr: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Append(self, lpvHdr: c_void_p, lpvData: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Set(self, lRowIndex: Int32, lColumnIndex: Int32, lpvData: c_void_p, cbData: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Set(self, lRowIndex: Int32, lColumnIndex: Int32, lpwStr: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Set(self, lRowIndex: Int32, lColumnIndex: Int32, dwData: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Set(self, lRowIndex: Int32, lpvHdr: c_void_p, lpvData: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Copy(self, pRSCopy: Windows.Win32.Data.HtmlHelp.IITResultSet_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def AppendRows(self, pResSrc: Windows.Win32.Data.HtmlHelp.IITResultSet_head, lRowSrcFirst: Int32, cSrcRows: Int32, lRowFirstDest: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Get(self, lRowIndex: Int32, lColumnIndex: Int32, Prop: POINTER(Windows.Win32.Data.HtmlHelp.CProperty_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetKeyProp(self, KeyPropID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetColumnPriority(self, lColumnIndex: Int32, ColumnPriority: POINTER(Windows.Win32.Data.HtmlHelp.PRIORITY)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetRowCount(self, lNumberOfRows: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetColumnCount(self, lNumberOfColumns: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetColumn(self, lColumnIndex: Int32, PropID: POINTER(UInt32), dwType: POINTER(UInt32), lpvDefaultValue: POINTER(c_void_p), cbSize: POINTER(UInt32), ColumnPriority: POINTER(Windows.Win32.Data.HtmlHelp.PRIORITY)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetColumn(self, lColumnIndex: Int32, PropID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetColumnFromPropID(self, PropID: UInt32, lColumnIndex: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def Clear(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def ClearRows(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def Free(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def IsCompleted(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def Cancel(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def Pause(self, fPause: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetRowStatus(self, lRowFirst: Int32, cRows: Int32, lpRowStatus: POINTER(Windows.Win32.Data.HtmlHelp.ROWSTATUS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetColumnStatus(self, lpColStatus: POINTER(Windows.Win32.Data.HtmlHelp.COLUMNSTATUS_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IStemSink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('fe77c330-7f42-11ce-be-57-00-aa-00-51-fe-20')
    @commethod(3)
    def PutAltWord(self, pwcInBuf: Windows.Win32.Foundation.PWSTR, cwc: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PutWord(self, pwcInBuf: Windows.Win32.Foundation.PWSTR, cwc: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IStemmerConfig(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8fa0d5a7-dedf-11d0-9a-61-00-c0-4f-b6-8b-f7')
    @commethod(3)
    def SetLocaleInfo(self, dwCodePageID: UInt32, lcid: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLocaleInfo(self, pdwCodePageID: POINTER(UInt32), plcid: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetControlInfo(self, grfStemFlags: UInt32, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetControlInfo(self, pgrfStemFlags: POINTER(UInt32), pdwReserved: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def LoadExternalStemmerData(self, pStream: Windows.Win32.System.Com.IStream_head, dwExtDataType: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWordBreakerConfig(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8fa0d5a6-dedf-11d0-9a-61-00-c0-4f-b6-8b-f7')
    @commethod(3)
    def SetLocaleInfo(self, dwCodePageID: UInt32, lcid: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLocaleInfo(self, pdwCodePageID: POINTER(UInt32), plcid: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetBreakWordType(self, dwBreakWordType: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetBreakWordType(self, pdwBreakWordType: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetControlInfo(self, grfBreakFlags: UInt32, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetControlInfo(self, pgrfBreakFlags: POINTER(UInt32), pdwReserved: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def LoadExternalBreakerData(self, pStream: Windows.Win32.System.Com.IStream_head, dwExtDataType: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetWordStemmer(self, rclsid: POINTER(Guid), pStemmer: Windows.Win32.System.Search.IStemmer_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetWordStemmer(self, ppStemmer: POINTER(Windows.Win32.System.Search.IStemmer_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNCOLHEAPFREE(param0: c_void_p) -> Int32: ...
PRIORITY = Int32
PRIORITY_LOW: PRIORITY = 0
PRIORITY_NORMAL: PRIORITY = 1
PRIORITY_HIGH: PRIORITY = 2
class ROWSTATUS(EasyCastStructure):
    lRowFirst: Int32
    cRows: Int32
    cProperties: Int32
    cRowsTotal: Int32
make_head(_module, 'COLUMNSTATUS')
make_head(_module, 'CProperty')
make_head(_module, 'HHNTRACK')
make_head(_module, 'HHN_NOTIFY')
make_head(_module, 'HH_AKLINK')
make_head(_module, 'HH_ENUM_CAT')
make_head(_module, 'HH_ENUM_IT')
make_head(_module, 'HH_FTS_QUERY')
make_head(_module, 'HH_GLOBAL_PROPERTY')
make_head(_module, 'HH_POPUP')
make_head(_module, 'HH_SET_INFOTYPE')
make_head(_module, 'HH_WINTYPE')
make_head(_module, 'IITDatabase')
make_head(_module, 'IITPropList')
make_head(_module, 'IITResultSet')
make_head(_module, 'IStemSink')
make_head(_module, 'IStemmerConfig')
make_head(_module, 'IWordBreakerConfig')
make_head(_module, 'PFNCOLHEAPFREE')
make_head(_module, 'ROWSTATUS')
