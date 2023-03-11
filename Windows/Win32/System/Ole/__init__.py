from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Gdi
import Windows.Win32.Media
import Windows.Win32.System.Com
import Windows.Win32.System.Com.StructuredStorage
import Windows.Win32.System.Memory
import Windows.Win32.System.Ole
import Windows.Win32.System.SystemServices
import Windows.Win32.UI.Controls
import Windows.Win32.UI.Controls.Dialogs
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
ACTIVATEFLAGS = Int32
ACTIVATE_WINDOWLESS: ACTIVATEFLAGS = 1
ACTIVEOBJECT_FLAGS = UInt32
ACTIVEOBJECT_STRONG: ACTIVEOBJECT_FLAGS = 0
ACTIVEOBJECT_WEAK: ACTIVEOBJECT_FLAGS = 1
class ARRAYDESC(Structure):
    tdescElem: Windows.Win32.System.Com.TYPEDESC
    cDims: UInt16
    rgbounds: Windows.Win32.System.Com.SAFEARRAYBOUND * 1
CTL_E_ILLEGALFUNCTIONCALL: Int32 = -2146828283
CONNECT_E_FIRST: Int32 = -2147220992
SELFREG_E_FIRST: Int32 = -2147220992
PERPROP_E_FIRST: Int32 = -2147220992
OLECMDERR_E_FIRST: Windows.Win32.Foundation.HRESULT = -2147221248
OLECMDERR_E_DISABLED: Windows.Win32.Foundation.HRESULT = -2147221247
OLECMDERR_E_NOHELP: Windows.Win32.Foundation.HRESULT = -2147221246
OLECMDERR_E_CANCELED: Windows.Win32.Foundation.HRESULT = -2147221245
OLECMDERR_E_UNKNOWNGROUP: Windows.Win32.Foundation.HRESULT = -2147221244
CONNECT_E_NOCONNECTION: Windows.Win32.Foundation.HRESULT = -2147220992
CONNECT_E_ADVISELIMIT: Windows.Win32.Foundation.HRESULT = -2147220991
CONNECT_E_CANNOTCONNECT: Windows.Win32.Foundation.HRESULT = -2147220990
CONNECT_E_OVERRIDDEN: Windows.Win32.Foundation.HRESULT = -2147220989
SELFREG_E_TYPELIB: Windows.Win32.Foundation.HRESULT = -2147220992
SELFREG_E_CLASS: Windows.Win32.Foundation.HRESULT = -2147220991
PERPROP_E_NOPAGEAVAILABLE: Windows.Win32.Foundation.HRESULT = -2147220992
CLSID_CFontPropPage: Guid = Guid('0be35200-8f91-11ce-9d-e3-00-aa-00-4b-b8-51')
CLSID_CColorPropPage: Guid = Guid('0be35201-8f91-11ce-9d-e3-00-aa-00-4b-b8-51')
CLSID_CPicturePropPage: Guid = Guid('0be35202-8f91-11ce-9d-e3-00-aa-00-4b-b8-51')
CLSID_PersistPropset: Guid = Guid('fb8f0821-0164-101b-84-ed-08-00-2b-2e-c7-13')
CLSID_ConvertVBX: Guid = Guid('fb8f0822-0164-101b-84-ed-08-00-2b-2e-c7-13')
CLSID_StdFont: Guid = Guid('0be35203-8f91-11ce-9d-e3-00-aa-00-4b-b8-51')
CLSID_StdPicture: Guid = Guid('0be35204-8f91-11ce-9d-e3-00-aa-00-4b-b8-51')
GUID_HIMETRIC: Guid = Guid('66504300-be0f-101a-8b-bb-00-aa-00-30-0c-ab')
GUID_COLOR: Guid = Guid('66504301-be0f-101a-8b-bb-00-aa-00-30-0c-ab')
GUID_XPOSPIXEL: Guid = Guid('66504302-be0f-101a-8b-bb-00-aa-00-30-0c-ab')
GUID_YPOSPIXEL: Guid = Guid('66504303-be0f-101a-8b-bb-00-aa-00-30-0c-ab')
GUID_XSIZEPIXEL: Guid = Guid('66504304-be0f-101a-8b-bb-00-aa-00-30-0c-ab')
GUID_YSIZEPIXEL: Guid = Guid('66504305-be0f-101a-8b-bb-00-aa-00-30-0c-ab')
GUID_XPOS: Guid = Guid('66504306-be0f-101a-8b-bb-00-aa-00-30-0c-ab')
GUID_YPOS: Guid = Guid('66504307-be0f-101a-8b-bb-00-aa-00-30-0c-ab')
GUID_XSIZE: Guid = Guid('66504308-be0f-101a-8b-bb-00-aa-00-30-0c-ab')
GUID_YSIZE: Guid = Guid('66504309-be0f-101a-8b-bb-00-aa-00-30-0c-ab')
GUID_TRISTATE: Guid = Guid('6650430a-be0f-101a-8b-bb-00-aa-00-30-0c-ab')
GUID_OPTIONVALUEEXCLUSIVE: Guid = Guid('6650430b-be0f-101a-8b-bb-00-aa-00-30-0c-ab')
GUID_CHECKVALUEEXCLUSIVE: Guid = Guid('6650430c-be0f-101a-8b-bb-00-aa-00-30-0c-ab')
GUID_FONTNAME: Guid = Guid('6650430d-be0f-101a-8b-bb-00-aa-00-30-0c-ab')
GUID_FONTSIZE: Guid = Guid('6650430e-be0f-101a-8b-bb-00-aa-00-30-0c-ab')
GUID_FONTBOLD: Guid = Guid('6650430f-be0f-101a-8b-bb-00-aa-00-30-0c-ab')
GUID_FONTITALIC: Guid = Guid('66504310-be0f-101a-8b-bb-00-aa-00-30-0c-ab')
GUID_FONTUNDERSCORE: Guid = Guid('66504311-be0f-101a-8b-bb-00-aa-00-30-0c-ab')
GUID_FONTSTRIKETHROUGH: Guid = Guid('66504312-be0f-101a-8b-bb-00-aa-00-30-0c-ab')
GUID_HANDLE: Guid = Guid('66504313-be0f-101a-8b-bb-00-aa-00-30-0c-ab')
CONNECT_E_LAST: Windows.Win32.Foundation.HRESULT = -2147220977
CONNECT_S_FIRST: Windows.Win32.Foundation.HRESULT = 262656
CONNECT_S_LAST: Windows.Win32.Foundation.HRESULT = 262671
SELFREG_E_LAST: Windows.Win32.Foundation.HRESULT = -2147220977
SELFREG_S_FIRST: Windows.Win32.Foundation.HRESULT = 262656
SELFREG_S_LAST: Windows.Win32.Foundation.HRESULT = 262671
PERPROP_E_LAST: Windows.Win32.Foundation.HRESULT = -2147220977
PERPROP_S_FIRST: Windows.Win32.Foundation.HRESULT = 262656
PERPROP_S_LAST: Windows.Win32.Foundation.HRESULT = 262671
OLEIVERB_PROPERTIES: Int32 = -7
VT_STREAMED_PROPSET: UInt32 = 73
VT_STORED_PROPSET: UInt32 = 74
VT_BLOB_PROPSET: UInt32 = 75
VT_VERBOSE_ENUM: UInt32 = 76
OCM__BASE: UInt32 = 8192
DISPID_AUTOSIZE: Int32 = -500
DISPID_BACKCOLOR: Int32 = -501
DISPID_BACKSTYLE: Int32 = -502
DISPID_BORDERCOLOR: Int32 = -503
DISPID_BORDERSTYLE: Int32 = -504
DISPID_BORDERWIDTH: Int32 = -505
DISPID_DRAWMODE: Int32 = -507
DISPID_DRAWSTYLE: Int32 = -508
DISPID_DRAWWIDTH: Int32 = -509
DISPID_FILLCOLOR: Int32 = -510
DISPID_FILLSTYLE: Int32 = -511
DISPID_FONT: Int32 = -512
DISPID_FORECOLOR: Int32 = -513
DISPID_ENABLED: Int32 = -514
DISPID_HWND: Int32 = -515
DISPID_TABSTOP: Int32 = -516
DISPID_TEXT: Int32 = -517
DISPID_CAPTION: Int32 = -518
DISPID_BORDERVISIBLE: Int32 = -519
DISPID_APPEARANCE: Int32 = -520
DISPID_MOUSEPOINTER: Int32 = -521
DISPID_MOUSEICON: Int32 = -522
DISPID_PICTURE: Int32 = -523
DISPID_VALID: Int32 = -524
DISPID_READYSTATE: Int32 = -525
DISPID_LISTINDEX: Int32 = -526
DISPID_SELECTED: Int32 = -527
DISPID_LIST: Int32 = -528
DISPID_COLUMN: Int32 = -529
DISPID_LISTCOUNT: Int32 = -531
DISPID_MULTISELECT: Int32 = -532
DISPID_MAXLENGTH: Int32 = -533
DISPID_PASSWORDCHAR: Int32 = -534
DISPID_SCROLLBARS: Int32 = -535
DISPID_WORDWRAP: Int32 = -536
DISPID_MULTILINE: Int32 = -537
DISPID_NUMBEROFROWS: Int32 = -538
DISPID_NUMBEROFCOLUMNS: Int32 = -539
DISPID_DISPLAYSTYLE: Int32 = -540
DISPID_GROUPNAME: Int32 = -541
DISPID_IMEMODE: Int32 = -542
DISPID_ACCELERATOR: Int32 = -543
DISPID_ENTERKEYBEHAVIOR: Int32 = -544
DISPID_TABKEYBEHAVIOR: Int32 = -545
DISPID_SELTEXT: Int32 = -546
DISPID_SELSTART: Int32 = -547
DISPID_SELLENGTH: Int32 = -548
DISPID_REFRESH: Int32 = -550
DISPID_DOCLICK: Int32 = -551
DISPID_ABOUTBOX: Int32 = -552
DISPID_ADDITEM: Int32 = -553
DISPID_CLEAR: Int32 = -554
DISPID_REMOVEITEM: Int32 = -555
DISPID_CLICK: Int32 = -600
DISPID_DBLCLICK: Int32 = -601
DISPID_KEYDOWN: Int32 = -602
DISPID_KEYPRESS: Int32 = -603
DISPID_KEYUP: Int32 = -604
DISPID_MOUSEDOWN: Int32 = -605
DISPID_MOUSEMOVE: Int32 = -606
DISPID_MOUSEUP: Int32 = -607
DISPID_ERROREVENT: Int32 = -608
DISPID_READYSTATECHANGE: Int32 = -609
DISPID_CLICK_VALUE: Int32 = -610
DISPID_RIGHTTOLEFT: Int32 = -611
DISPID_TOPTOBOTTOM: Int32 = -612
DISPID_THIS: Int32 = -613
DISPID_AMBIENT_BACKCOLOR: Int32 = -701
DISPID_AMBIENT_DISPLAYNAME: Int32 = -702
DISPID_AMBIENT_FONT: Int32 = -703
DISPID_AMBIENT_FORECOLOR: Int32 = -704
DISPID_AMBIENT_LOCALEID: Int32 = -705
DISPID_AMBIENT_MESSAGEREFLECT: Int32 = -706
DISPID_AMBIENT_SCALEUNITS: Int32 = -707
DISPID_AMBIENT_TEXTALIGN: Int32 = -708
DISPID_AMBIENT_USERMODE: Int32 = -709
DISPID_AMBIENT_UIDEAD: Int32 = -710
DISPID_AMBIENT_SHOWGRABHANDLES: Int32 = -711
DISPID_AMBIENT_SHOWHATCHING: Int32 = -712
DISPID_AMBIENT_DISPLAYASDEFAULT: Int32 = -713
DISPID_AMBIENT_SUPPORTSMNEMONICS: Int32 = -714
DISPID_AMBIENT_AUTOCLIP: Int32 = -715
DISPID_AMBIENT_APPEARANCE: Int32 = -716
DISPID_AMBIENT_CODEPAGE: Int32 = -725
DISPID_AMBIENT_PALETTE: Int32 = -726
DISPID_AMBIENT_CHARSET: Int32 = -727
DISPID_AMBIENT_TRANSFERPRIORITY: Int32 = -728
DISPID_AMBIENT_RIGHTTOLEFT: Int32 = -732
DISPID_AMBIENT_TOPTOBOTTOM: Int32 = -733
DISPID_Name: Int32 = -800
DISPID_Delete: Int32 = -801
DISPID_Object: Int32 = -802
DISPID_Parent: Int32 = -803
DISPID_FONT_NAME: UInt32 = 0
DISPID_FONT_SIZE: UInt32 = 2
DISPID_FONT_BOLD: UInt32 = 3
DISPID_FONT_ITALIC: UInt32 = 4
DISPID_FONT_UNDER: UInt32 = 5
DISPID_FONT_STRIKE: UInt32 = 6
DISPID_FONT_WEIGHT: UInt32 = 7
DISPID_FONT_CHARSET: UInt32 = 8
DISPID_FONT_CHANGED: UInt32 = 9
DISPID_PICT_HANDLE: UInt32 = 0
DISPID_PICT_HPAL: UInt32 = 2
DISPID_PICT_TYPE: UInt32 = 3
DISPID_PICT_WIDTH: UInt32 = 4
DISPID_PICT_HEIGHT: UInt32 = 5
DISPID_PICT_RENDER: UInt32 = 6
STDOLE_TLB: String = 'stdole2.tlb'
STDTYPE_TLB: String = 'stdole2.tlb'
GC_WCH_SIBLING: Int32 = 1
TIFLAGS_EXTENDDISPATCHONLY: UInt32 = 1
OLECMDERR_E_NOTSUPPORTED: Int32 = -2147221248
MSOCMDERR_E_FIRST: Int32 = -2147221248
MSOCMDERR_E_NOTSUPPORTED: Int32 = -2147221248
MSOCMDERR_E_DISABLED: Int32 = -2147221247
MSOCMDERR_E_NOHELP: Int32 = -2147221246
MSOCMDERR_E_CANCELED: Int32 = -2147221245
MSOCMDERR_E_UNKNOWNGROUP: Int32 = -2147221244
OLECMD_TASKDLGID_ONBEFOREUNLOAD: UInt32 = 1
OLECMDARGINDEX_SHOWPAGEACTIONMENU_HWND: UInt32 = 0
OLECMDARGINDEX_SHOWPAGEACTIONMENU_X: UInt32 = 1
OLECMDARGINDEX_SHOWPAGEACTIONMENU_Y: UInt32 = 2
OLECMDARGINDEX_ACTIVEXINSTALL_PUBLISHER: UInt32 = 0
OLECMDARGINDEX_ACTIVEXINSTALL_DISPLAYNAME: UInt32 = 1
OLECMDARGINDEX_ACTIVEXINSTALL_CLSID: UInt32 = 2
OLECMDARGINDEX_ACTIVEXINSTALL_INSTALLSCOPE: UInt32 = 3
OLECMDARGINDEX_ACTIVEXINSTALL_SOURCEURL: UInt32 = 4
INSTALL_SCOPE_INVALID: UInt32 = 0
INSTALL_SCOPE_MACHINE: UInt32 = 1
INSTALL_SCOPE_USER: UInt32 = 2
MK_ALT: UInt32 = 32
DD_DEFSCROLLINSET: UInt32 = 11
DD_DEFSCROLLDELAY: UInt32 = 50
DD_DEFSCROLLINTERVAL: UInt32 = 50
DD_DEFDRAGDELAY: UInt32 = 200
DD_DEFDRAGMINDIST: UInt32 = 2
OT_LINK: Int32 = 1
OT_EMBEDDED: Int32 = 2
OT_STATIC: Int32 = 3
OLEVERB_PRIMARY: UInt32 = 0
OF_SET: UInt32 = 1
OF_GET: UInt32 = 2
OF_HANDLER: UInt32 = 4
WIN32: UInt32 = 100
IDC_OLEUIHELP: UInt32 = 99
IDC_IO_CREATENEW: UInt32 = 2100
IDC_IO_CREATEFROMFILE: UInt32 = 2101
IDC_IO_LINKFILE: UInt32 = 2102
IDC_IO_OBJECTTYPELIST: UInt32 = 2103
IDC_IO_DISPLAYASICON: UInt32 = 2104
IDC_IO_CHANGEICON: UInt32 = 2105
IDC_IO_FILE: UInt32 = 2106
IDC_IO_FILEDISPLAY: UInt32 = 2107
IDC_IO_RESULTIMAGE: UInt32 = 2108
IDC_IO_RESULTTEXT: UInt32 = 2109
IDC_IO_ICONDISPLAY: UInt32 = 2110
IDC_IO_OBJECTTYPETEXT: UInt32 = 2111
IDC_IO_FILETEXT: UInt32 = 2112
IDC_IO_FILETYPE: UInt32 = 2113
IDC_IO_INSERTCONTROL: UInt32 = 2114
IDC_IO_ADDCONTROL: UInt32 = 2115
IDC_IO_CONTROLTYPELIST: UInt32 = 2116
IDC_PS_PASTE: UInt32 = 500
IDC_PS_PASTELINK: UInt32 = 501
IDC_PS_SOURCETEXT: UInt32 = 502
IDC_PS_PASTELIST: UInt32 = 503
IDC_PS_PASTELINKLIST: UInt32 = 504
IDC_PS_DISPLAYLIST: UInt32 = 505
IDC_PS_DISPLAYASICON: UInt32 = 506
IDC_PS_ICONDISPLAY: UInt32 = 507
IDC_PS_CHANGEICON: UInt32 = 508
IDC_PS_RESULTIMAGE: UInt32 = 509
IDC_PS_RESULTTEXT: UInt32 = 510
IDC_CI_GROUP: UInt32 = 120
IDC_CI_CURRENT: UInt32 = 121
IDC_CI_CURRENTICON: UInt32 = 122
IDC_CI_DEFAULT: UInt32 = 123
IDC_CI_DEFAULTICON: UInt32 = 124
IDC_CI_FROMFILE: UInt32 = 125
IDC_CI_FROMFILEEDIT: UInt32 = 126
IDC_CI_ICONLIST: UInt32 = 127
IDC_CI_LABEL: UInt32 = 128
IDC_CI_LABELEDIT: UInt32 = 129
IDC_CI_BROWSE: UInt32 = 130
IDC_CI_ICONDISPLAY: UInt32 = 131
IDC_CV_OBJECTTYPE: UInt32 = 150
IDC_CV_DISPLAYASICON: UInt32 = 152
IDC_CV_CHANGEICON: UInt32 = 153
IDC_CV_ACTIVATELIST: UInt32 = 154
IDC_CV_CONVERTTO: UInt32 = 155
IDC_CV_ACTIVATEAS: UInt32 = 156
IDC_CV_RESULTTEXT: UInt32 = 157
IDC_CV_CONVERTLIST: UInt32 = 158
IDC_CV_ICONDISPLAY: UInt32 = 165
IDC_EL_CHANGESOURCE: UInt32 = 201
IDC_EL_AUTOMATIC: UInt32 = 202
IDC_EL_CANCELLINK: UInt32 = 209
IDC_EL_UPDATENOW: UInt32 = 210
IDC_EL_OPENSOURCE: UInt32 = 211
IDC_EL_MANUAL: UInt32 = 212
IDC_EL_LINKSOURCE: UInt32 = 216
IDC_EL_LINKTYPE: UInt32 = 217
IDC_EL_LINKSLISTBOX: UInt32 = 206
IDC_EL_COL1: UInt32 = 220
IDC_EL_COL2: UInt32 = 221
IDC_EL_COL3: UInt32 = 222
IDC_BZ_RETRY: UInt32 = 600
IDC_BZ_ICON: UInt32 = 601
IDC_BZ_MESSAGE1: UInt32 = 602
IDC_BZ_SWITCHTO: UInt32 = 604
IDC_UL_METER: UInt32 = 1029
IDC_UL_STOP: UInt32 = 1030
IDC_UL_PERCENT: UInt32 = 1031
IDC_UL_PROGRESS: UInt32 = 1032
IDC_PU_LINKS: UInt32 = 900
IDC_PU_TEXT: UInt32 = 901
IDC_PU_CONVERT: UInt32 = 902
IDC_PU_ICON: UInt32 = 908
IDC_GP_OBJECTNAME: UInt32 = 1009
IDC_GP_OBJECTTYPE: UInt32 = 1010
IDC_GP_OBJECTSIZE: UInt32 = 1011
IDC_GP_CONVERT: UInt32 = 1013
IDC_GP_OBJECTICON: UInt32 = 1014
IDC_GP_OBJECTLOCATION: UInt32 = 1022
IDC_VP_PERCENT: UInt32 = 1000
IDC_VP_CHANGEICON: UInt32 = 1001
IDC_VP_EDITABLE: UInt32 = 1002
IDC_VP_ASICON: UInt32 = 1003
IDC_VP_RELATIVE: UInt32 = 1005
IDC_VP_SPIN: UInt32 = 1006
IDC_VP_SCALETXT: UInt32 = 1034
IDC_VP_ICONDISPLAY: UInt32 = 1021
IDC_VP_RESULTIMAGE: UInt32 = 1033
IDC_LP_OPENSOURCE: UInt32 = 1006
IDC_LP_UPDATENOW: UInt32 = 1007
IDC_LP_BREAKLINK: UInt32 = 1008
IDC_LP_LINKSOURCE: UInt32 = 1012
IDC_LP_CHANGESOURCE: UInt32 = 1015
IDC_LP_AUTOMATIC: UInt32 = 1016
IDC_LP_MANUAL: UInt32 = 1017
IDC_LP_DATE: UInt32 = 1018
IDC_LP_TIME: UInt32 = 1019
IDD_INSERTOBJECT: UInt32 = 1000
IDD_CHANGEICON: UInt32 = 1001
IDD_CONVERT: UInt32 = 1002
IDD_PASTESPECIAL: UInt32 = 1003
IDD_EDITLINKS: UInt32 = 1004
IDD_BUSY: UInt32 = 1006
IDD_UPDATELINKS: UInt32 = 1007
IDD_CHANGESOURCE: UInt32 = 1009
IDD_INSERTFILEBROWSE: UInt32 = 1010
IDD_CHANGEICONBROWSE: UInt32 = 1011
IDD_CONVERTONLY: UInt32 = 1012
IDD_CHANGESOURCE4: UInt32 = 1013
IDD_GNRLPROPS: UInt32 = 1100
IDD_VIEWPROPS: UInt32 = 1101
IDD_LINKPROPS: UInt32 = 1102
IDD_CONVERT4: UInt32 = 1103
IDD_CONVERTONLY4: UInt32 = 1104
IDD_EDITLINKS4: UInt32 = 1105
IDD_GNRLPROPS4: UInt32 = 1106
IDD_LINKPROPS4: UInt32 = 1107
IDD_PASTESPECIAL4: UInt32 = 1108
IDD_CANNOTUPDATELINK: UInt32 = 1008
IDD_LINKSOURCEUNAVAILABLE: UInt32 = 1020
IDD_SERVERNOTFOUND: UInt32 = 1023
IDD_OUTOFMEMORY: UInt32 = 1024
IDD_SERVERNOTREGW: UInt32 = 1021
IDD_LINKTYPECHANGEDW: UInt32 = 1022
IDD_SERVERNOTREGA: UInt32 = 1025
IDD_LINKTYPECHANGEDA: UInt32 = 1026
IDD_SERVERNOTREG: UInt32 = 1021
IDD_LINKTYPECHANGED: UInt32 = 1022
OLESTDDELIM: String = '\\'
SZOLEUI_MSG_HELP: String = 'OLEUI_MSG_HELP'
SZOLEUI_MSG_ENDDIALOG: String = 'OLEUI_MSG_ENDDIALOG'
SZOLEUI_MSG_BROWSE: String = 'OLEUI_MSG_BROWSE'
SZOLEUI_MSG_CHANGEICON: String = 'OLEUI_MSG_CHANGEICON'
SZOLEUI_MSG_CLOSEBUSYDIALOG: String = 'OLEUI_MSG_CLOSEBUSYDIALOG'
SZOLEUI_MSG_CONVERT: String = 'OLEUI_MSG_CONVERT'
SZOLEUI_MSG_CHANGESOURCE: String = 'OLEUI_MSG_CHANGESOURCE'
SZOLEUI_MSG_ADDCONTROL: String = 'OLEUI_MSG_ADDCONTROL'
SZOLEUI_MSG_BROWSE_OFN: String = 'OLEUI_MSG_BROWSE_OFN'
ID_BROWSE_CHANGEICON: UInt32 = 1
ID_BROWSE_INSERTFILE: UInt32 = 2
ID_BROWSE_ADDCONTROL: UInt32 = 3
ID_BROWSE_CHANGESOURCE: UInt32 = 4
OLEUI_FALSE: UInt32 = 0
OLEUI_SUCCESS: UInt32 = 1
OLEUI_OK: UInt32 = 1
OLEUI_CANCEL: UInt32 = 2
OLEUI_ERR_STANDARDMIN: UInt32 = 100
OLEUI_ERR_OLEMEMALLOC: UInt32 = 100
OLEUI_ERR_STRUCTURENULL: UInt32 = 101
OLEUI_ERR_STRUCTUREINVALID: UInt32 = 102
OLEUI_ERR_CBSTRUCTINCORRECT: UInt32 = 103
OLEUI_ERR_HWNDOWNERINVALID: UInt32 = 104
OLEUI_ERR_LPSZCAPTIONINVALID: UInt32 = 105
OLEUI_ERR_LPFNHOOKINVALID: UInt32 = 106
OLEUI_ERR_HINSTANCEINVALID: UInt32 = 107
OLEUI_ERR_LPSZTEMPLATEINVALID: UInt32 = 108
OLEUI_ERR_HRESOURCEINVALID: UInt32 = 109
OLEUI_ERR_FINDTEMPLATEFAILURE: UInt32 = 110
OLEUI_ERR_LOADTEMPLATEFAILURE: UInt32 = 111
OLEUI_ERR_DIALOGFAILURE: UInt32 = 112
OLEUI_ERR_LOCALMEMALLOC: UInt32 = 113
OLEUI_ERR_GLOBALMEMALLOC: UInt32 = 114
OLEUI_ERR_LOADSTRING: UInt32 = 115
OLEUI_ERR_STANDARDMAX: UInt32 = 116
OLEUI_IOERR_LPSZFILEINVALID: UInt32 = 116
OLEUI_IOERR_LPSZLABELINVALID: UInt32 = 117
OLEUI_IOERR_HICONINVALID: UInt32 = 118
OLEUI_IOERR_LPFORMATETCINVALID: UInt32 = 119
OLEUI_IOERR_PPVOBJINVALID: UInt32 = 120
OLEUI_IOERR_LPIOLECLIENTSITEINVALID: UInt32 = 121
OLEUI_IOERR_LPISTORAGEINVALID: UInt32 = 122
OLEUI_IOERR_SCODEHASERROR: UInt32 = 123
OLEUI_IOERR_LPCLSIDEXCLUDEINVALID: UInt32 = 124
OLEUI_IOERR_CCHFILEINVALID: UInt32 = 125
PS_MAXLINKTYPES: UInt32 = 8
OLEUI_IOERR_SRCDATAOBJECTINVALID: UInt32 = 116
OLEUI_IOERR_ARRPASTEENTRIESINVALID: UInt32 = 117
OLEUI_IOERR_ARRLINKTYPESINVALID: UInt32 = 118
OLEUI_PSERR_CLIPBOARDCHANGED: UInt32 = 119
OLEUI_PSERR_GETCLIPBOARDFAILED: UInt32 = 120
OLEUI_ELERR_LINKCNTRNULL: UInt32 = 116
OLEUI_ELERR_LINKCNTRINVALID: UInt32 = 117
OLEUI_CIERR_MUSTHAVECLSID: UInt32 = 116
OLEUI_CIERR_MUSTHAVECURRENTMETAFILE: UInt32 = 117
OLEUI_CIERR_SZICONEXEINVALID: UInt32 = 118
PROP_HWND_CHGICONDLG: String = 'HWND_CIDLG'
OLEUI_CTERR_CLASSIDINVALID: UInt32 = 117
OLEUI_CTERR_DVASPECTINVALID: UInt32 = 118
OLEUI_CTERR_CBFORMATINVALID: UInt32 = 119
OLEUI_CTERR_HMETAPICTINVALID: UInt32 = 120
OLEUI_CTERR_STRINGINVALID: UInt32 = 121
OLEUI_BZERR_HTASKINVALID: UInt32 = 116
OLEUI_BZ_SWITCHTOSELECTED: UInt32 = 117
OLEUI_BZ_RETRYSELECTED: UInt32 = 118
OLEUI_BZ_CALLUNBLOCKED: UInt32 = 119
OLEUI_CSERR_LINKCNTRNULL: UInt32 = 116
OLEUI_CSERR_LINKCNTRINVALID: UInt32 = 117
OLEUI_CSERR_FROMNOTNULL: UInt32 = 118
OLEUI_CSERR_TONOTNULL: UInt32 = 119
OLEUI_CSERR_SOURCENULL: UInt32 = 120
OLEUI_CSERR_SOURCEINVALID: UInt32 = 121
OLEUI_CSERR_SOURCEPARSERROR: UInt32 = 122
OLEUI_CSERR_SOURCEPARSEERROR: UInt32 = 122
OLEUI_OPERR_SUBPROPNULL: UInt32 = 116
OLEUI_OPERR_SUBPROPINVALID: UInt32 = 117
OLEUI_OPERR_PROPSHEETNULL: UInt32 = 118
OLEUI_OPERR_PROPSHEETINVALID: UInt32 = 119
OLEUI_OPERR_SUPPROP: UInt32 = 120
OLEUI_OPERR_PROPSINVALID: UInt32 = 121
OLEUI_OPERR_PAGESINCORRECT: UInt32 = 122
OLEUI_OPERR_INVALIDPAGES: UInt32 = 123
OLEUI_OPERR_NOTSUPPORTED: UInt32 = 124
OLEUI_OPERR_DLGPROCNOTNULL: UInt32 = 125
OLEUI_OPERR_LPARAMNOTZERO: UInt32 = 126
OLEUI_GPERR_STRINGINVALID: UInt32 = 127
OLEUI_GPERR_CLASSIDINVALID: UInt32 = 128
OLEUI_GPERR_LPCLSIDEXCLUDEINVALID: UInt32 = 129
OLEUI_GPERR_CBFORMATINVALID: UInt32 = 130
OLEUI_VPERR_METAPICTINVALID: UInt32 = 131
OLEUI_VPERR_DVASPECTINVALID: UInt32 = 132
OLEUI_LPERR_LINKCNTRNULL: UInt32 = 133
OLEUI_LPERR_LINKCNTRINVALID: UInt32 = 134
OLEUI_OPERR_PROPERTYSHEET: UInt32 = 135
OLEUI_OPERR_OBJINFOINVALID: UInt32 = 136
OLEUI_OPERR_LINKINFOINVALID: UInt32 = 137
OLEUI_QUERY_GETCLASSID: UInt32 = 65280
OLEUI_QUERY_LINKBROKEN: UInt32 = 65281
DISPID_UNKNOWN: Int32 = -1
DISPID_VALUE: UInt32 = 0
DISPID_PROPERTYPUT: Int32 = -3
DISPID_NEWENUM: Int32 = -4
DISPID_EVALUATE: Int32 = -5
DISPID_CONSTRUCTOR: Int32 = -6
DISPID_DESTRUCTOR: Int32 = -7
DISPID_COLLECT: Int32 = -8
STDOLE_MAJORVERNUM: UInt32 = 1
STDOLE_MINORVERNUM: UInt32 = 0
STDOLE_LCID: UInt32 = 0
STDOLE2_MAJORVERNUM: UInt32 = 2
STDOLE2_MINORVERNUM: UInt32 = 0
STDOLE2_LCID: UInt32 = 0
VARIANT_NOVALUEPROP: UInt32 = 1
VARIANT_ALPHABOOL: UInt32 = 2
VARIANT_NOUSEROVERRIDE: UInt32 = 4
VARIANT_CALENDAR_HIJRI: UInt32 = 8
VARIANT_LOCALBOOL: UInt32 = 16
VARIANT_CALENDAR_THAI: UInt32 = 32
VARIANT_CALENDAR_GREGORIAN: UInt32 = 64
VARIANT_USE_NLS: UInt32 = 128
VAR_TIMEVALUEONLY: UInt32 = 1
VAR_DATEVALUEONLY: UInt32 = 2
VAR_VALIDDATE: UInt32 = 4
VAR_CALENDAR_HIJRI: UInt32 = 8
VAR_LOCALBOOL: UInt32 = 16
VAR_FORMAT_NOSUBSTITUTE: UInt32 = 32
VAR_FOURDIGITYEARS: UInt32 = 64
LOCALE_USE_NLS: UInt32 = 268435456
VAR_CALENDAR_THAI: UInt32 = 128
VAR_CALENDAR_GREGORIAN: UInt32 = 256
VTDATEGRE_MAX: UInt32 = 2958465
VTDATEGRE_MIN: Int32 = -657434
MEMBERID_NIL: Int32 = -1
ID_DEFAULTINST: Int32 = -2
LOAD_TLB_AS_32BIT: UInt32 = 32
LOAD_TLB_AS_64BIT: UInt32 = 64
fdexNameCaseSensitive: Int32 = 1
fdexNameEnsure: Int32 = 2
fdexNameImplicit: Int32 = 4
fdexNameCaseInsensitive: Int32 = 8
fdexNameInternal: Int32 = 16
fdexNameNoDynamicProperties: Int32 = 32
fdexEnumDefault: Int32 = 1
fdexEnumAll: Int32 = 2
DISPATCH_CONSTRUCT: UInt32 = 16384
DISPID_STARTENUM: Int32 = -1
SID_VariantConversion: Guid = Guid('1f101481-bccd-11d0-93-36-00-a0-c9-0d-ca-a9')
SID_GetCaller: Guid = Guid('4717cc40-bcb9-11d0-93-36-00-a0-c9-0d-ca-a9')
SID_ProvideRuntimeContext: Guid = Guid('74a5040c-dd0c-48f0-ac-85-19-4c-32-59-18-0a')
@winfunctype('OLEAUT32.dll')
def DosDateTimeToVariantTime(wDosDate: UInt16, wDosTime: UInt16, pvtime: POINTER(Double)) -> Int32: ...
@winfunctype('OLEAUT32.dll')
def VariantTimeToDosDateTime(vtime: Double, pwDosDate: POINTER(UInt16), pwDosTime: POINTER(UInt16)) -> Int32: ...
@winfunctype('OLEAUT32.dll')
def SystemTimeToVariantTime(lpSystemTime: POINTER(Windows.Win32.Foundation.SYSTEMTIME_head), pvtime: POINTER(Double)) -> Int32: ...
@winfunctype('OLEAUT32.dll')
def VariantTimeToSystemTime(vtime: Double, lpSystemTime: POINTER(Windows.Win32.Foundation.SYSTEMTIME_head)) -> Int32: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayAllocDescriptor(cDims: UInt32, ppsaOut: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayAllocDescriptorEx(vt: Windows.Win32.System.Com.VARENUM, cDims: UInt32, ppsaOut: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayAllocData(psa: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayCreate(vt: Windows.Win32.System.Com.VARENUM, cDims: UInt32, rgsabound: POINTER(Windows.Win32.System.Com.SAFEARRAYBOUND_head)) -> POINTER(Windows.Win32.System.Com.SAFEARRAY_head): ...
@winfunctype('OLEAUT32.dll')
def SafeArrayCreateEx(vt: Windows.Win32.System.Com.VARENUM, cDims: UInt32, rgsabound: POINTER(Windows.Win32.System.Com.SAFEARRAYBOUND_head), pvExtra: c_void_p) -> POINTER(Windows.Win32.System.Com.SAFEARRAY_head): ...
@winfunctype('OLEAUT32.dll')
def SafeArrayCopyData(psaSource: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), psaTarget: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayReleaseDescriptor(psa: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Void: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayDestroyDescriptor(psa: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayReleaseData(pData: c_void_p) -> Void: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayDestroyData(psa: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayAddRef(psa: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), ppDataToRelease: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayDestroy(psa: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayRedim(psa: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), psaboundNew: POINTER(Windows.Win32.System.Com.SAFEARRAYBOUND_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayGetDim(psa: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> UInt32: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayGetElemsize(psa: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> UInt32: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayGetUBound(psa: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), nDim: UInt32, plUbound: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayGetLBound(psa: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), nDim: UInt32, plLbound: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayLock(psa: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayUnlock(psa: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayAccessData(psa: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), ppvData: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayUnaccessData(psa: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayGetElement(psa: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), rgIndices: POINTER(Int32), pv: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayPutElement(psa: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), rgIndices: POINTER(Int32), pv: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayCopy(psa: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), ppsaOut: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayPtrOfIndex(psa: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), rgIndices: POINTER(Int32), ppvData: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArraySetRecordInfo(psa: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), prinfo: Windows.Win32.System.Ole.IRecordInfo_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayGetRecordInfo(psa: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), prinfo: POINTER(Windows.Win32.System.Ole.IRecordInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArraySetIID(psa: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), guid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayGetIID(psa: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), pguid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayGetVartype(psa: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), pvt: POINTER(Windows.Win32.System.Com.VARENUM)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayCreateVector(vt: Windows.Win32.System.Com.VARENUM, lLbound: Int32, cElements: UInt32) -> POINTER(Windows.Win32.System.Com.SAFEARRAY_head): ...
@winfunctype('OLEAUT32.dll')
def SafeArrayCreateVectorEx(vt: Windows.Win32.System.Com.VARENUM, lLbound: Int32, cElements: UInt32, pvExtra: c_void_p) -> POINTER(Windows.Win32.System.Com.SAFEARRAY_head): ...
@winfunctype('OLEAUT32.dll')
def VariantInit(pvarg: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Void: ...
@winfunctype('OLEAUT32.dll')
def VariantClear(pvarg: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VariantCopy(pvargDest: POINTER(Windows.Win32.System.Com.VARIANT_head), pvargSrc: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VariantCopyInd(pvarDest: POINTER(Windows.Win32.System.Com.VARIANT_head), pvargSrc: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VariantChangeType(pvargDest: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarSrc: POINTER(Windows.Win32.System.Com.VARIANT_head), wFlags: UInt16, vt: Windows.Win32.System.Com.VARENUM) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VariantChangeTypeEx(pvargDest: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarSrc: POINTER(Windows.Win32.System.Com.VARIANT_head), lcid: UInt32, wFlags: UInt16, vt: Windows.Win32.System.Com.VARENUM) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VectorFromBstr(bstr: Windows.Win32.Foundation.BSTR, ppsa: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def BstrFromVector(psa: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), pbstr: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromI2(sIn: Int16, pbOut: c_char_p_no) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromI4(lIn: Int32, pbOut: c_char_p_no) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromI8(i64In: Int64, pbOut: c_char_p_no) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromR4(fltIn: Single, pbOut: c_char_p_no) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromR8(dblIn: Double, pbOut: c_char_p_no) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromCy(cyIn: Windows.Win32.System.Com.CY, pbOut: c_char_p_no) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromDate(dateIn: Double, pbOut: c_char_p_no) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromStr(strIn: Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, pbOut: c_char_p_no) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromDisp(pdispIn: Windows.Win32.System.Com.IDispatch_head, lcid: UInt32, pbOut: c_char_p_no) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromBool(boolIn: Windows.Win32.Foundation.VARIANT_BOOL, pbOut: c_char_p_no) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromI1(cIn: Windows.Win32.Foundation.CHAR, pbOut: c_char_p_no) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromUI2(uiIn: UInt16, pbOut: c_char_p_no) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromUI4(ulIn: UInt32, pbOut: c_char_p_no) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromUI8(ui64In: UInt64, pbOut: c_char_p_no) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromDec(pdecIn: POINTER(Windows.Win32.Foundation.DECIMAL_head), pbOut: c_char_p_no) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI2FromUI1(bIn: Byte, psOut: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI2FromI4(lIn: Int32, psOut: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI2FromI8(i64In: Int64, psOut: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI2FromR4(fltIn: Single, psOut: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI2FromR8(dblIn: Double, psOut: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI2FromCy(cyIn: Windows.Win32.System.Com.CY, psOut: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI2FromDate(dateIn: Double, psOut: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI2FromStr(strIn: Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, psOut: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI2FromDisp(pdispIn: Windows.Win32.System.Com.IDispatch_head, lcid: UInt32, psOut: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI2FromBool(boolIn: Windows.Win32.Foundation.VARIANT_BOOL, psOut: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI2FromI1(cIn: Windows.Win32.Foundation.CHAR, psOut: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI2FromUI2(uiIn: UInt16, psOut: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI2FromUI4(ulIn: UInt32, psOut: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI2FromUI8(ui64In: UInt64, psOut: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI2FromDec(pdecIn: POINTER(Windows.Win32.Foundation.DECIMAL_head), psOut: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI4FromUI1(bIn: Byte, plOut: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI4FromI2(sIn: Int16, plOut: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI4FromI8(i64In: Int64, plOut: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI4FromR4(fltIn: Single, plOut: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI4FromR8(dblIn: Double, plOut: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI4FromCy(cyIn: Windows.Win32.System.Com.CY, plOut: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI4FromDate(dateIn: Double, plOut: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI4FromStr(strIn: Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, plOut: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI4FromDisp(pdispIn: Windows.Win32.System.Com.IDispatch_head, lcid: UInt32, plOut: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI4FromBool(boolIn: Windows.Win32.Foundation.VARIANT_BOOL, plOut: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI4FromI1(cIn: Windows.Win32.Foundation.CHAR, plOut: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI4FromUI2(uiIn: UInt16, plOut: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI4FromUI4(ulIn: UInt32, plOut: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI4FromUI8(ui64In: UInt64, plOut: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI4FromDec(pdecIn: POINTER(Windows.Win32.Foundation.DECIMAL_head), plOut: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI8FromUI1(bIn: Byte, pi64Out: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI8FromI2(sIn: Int16, pi64Out: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI8FromR4(fltIn: Single, pi64Out: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI8FromR8(dblIn: Double, pi64Out: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI8FromCy(cyIn: Windows.Win32.System.Com.CY, pi64Out: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI8FromDate(dateIn: Double, pi64Out: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI8FromStr(strIn: Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, pi64Out: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI8FromDisp(pdispIn: Windows.Win32.System.Com.IDispatch_head, lcid: UInt32, pi64Out: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI8FromBool(boolIn: Windows.Win32.Foundation.VARIANT_BOOL, pi64Out: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI8FromI1(cIn: Windows.Win32.Foundation.CHAR, pi64Out: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI8FromUI2(uiIn: UInt16, pi64Out: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI8FromUI4(ulIn: UInt32, pi64Out: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI8FromUI8(ui64In: UInt64, pi64Out: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI8FromDec(pdecIn: POINTER(Windows.Win32.Foundation.DECIMAL_head), pi64Out: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4FromUI1(bIn: Byte, pfltOut: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4FromI2(sIn: Int16, pfltOut: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4FromI4(lIn: Int32, pfltOut: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4FromI8(i64In: Int64, pfltOut: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4FromR8(dblIn: Double, pfltOut: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4FromCy(cyIn: Windows.Win32.System.Com.CY, pfltOut: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4FromDate(dateIn: Double, pfltOut: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4FromStr(strIn: Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, pfltOut: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4FromDisp(pdispIn: Windows.Win32.System.Com.IDispatch_head, lcid: UInt32, pfltOut: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4FromBool(boolIn: Windows.Win32.Foundation.VARIANT_BOOL, pfltOut: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4FromI1(cIn: Windows.Win32.Foundation.CHAR, pfltOut: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4FromUI2(uiIn: UInt16, pfltOut: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4FromUI4(ulIn: UInt32, pfltOut: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4FromUI8(ui64In: UInt64, pfltOut: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4FromDec(pdecIn: POINTER(Windows.Win32.Foundation.DECIMAL_head), pfltOut: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8FromUI1(bIn: Byte, pdblOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8FromI2(sIn: Int16, pdblOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8FromI4(lIn: Int32, pdblOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8FromI8(i64In: Int64, pdblOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8FromR4(fltIn: Single, pdblOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8FromCy(cyIn: Windows.Win32.System.Com.CY, pdblOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8FromDate(dateIn: Double, pdblOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8FromStr(strIn: Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, pdblOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8FromDisp(pdispIn: Windows.Win32.System.Com.IDispatch_head, lcid: UInt32, pdblOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8FromBool(boolIn: Windows.Win32.Foundation.VARIANT_BOOL, pdblOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8FromI1(cIn: Windows.Win32.Foundation.CHAR, pdblOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8FromUI2(uiIn: UInt16, pdblOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8FromUI4(ulIn: UInt32, pdblOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8FromUI8(ui64In: UInt64, pdblOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8FromDec(pdecIn: POINTER(Windows.Win32.Foundation.DECIMAL_head), pdblOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromUI1(bIn: Byte, pdateOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromI2(sIn: Int16, pdateOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromI4(lIn: Int32, pdateOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromI8(i64In: Int64, pdateOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromR4(fltIn: Single, pdateOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromR8(dblIn: Double, pdateOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromCy(cyIn: Windows.Win32.System.Com.CY, pdateOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromStr(strIn: Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, pdateOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromDisp(pdispIn: Windows.Win32.System.Com.IDispatch_head, lcid: UInt32, pdateOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromBool(boolIn: Windows.Win32.Foundation.VARIANT_BOOL, pdateOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromI1(cIn: Windows.Win32.Foundation.CHAR, pdateOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromUI2(uiIn: UInt16, pdateOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromUI4(ulIn: UInt32, pdateOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromUI8(ui64In: UInt64, pdateOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromDec(pdecIn: POINTER(Windows.Win32.Foundation.DECIMAL_head), pdateOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFromUI1(bIn: Byte, pcyOut: POINTER(Windows.Win32.System.Com.CY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFromI2(sIn: Int16, pcyOut: POINTER(Windows.Win32.System.Com.CY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFromI4(lIn: Int32, pcyOut: POINTER(Windows.Win32.System.Com.CY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFromI8(i64In: Int64, pcyOut: POINTER(Windows.Win32.System.Com.CY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFromR4(fltIn: Single, pcyOut: POINTER(Windows.Win32.System.Com.CY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFromR8(dblIn: Double, pcyOut: POINTER(Windows.Win32.System.Com.CY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFromDate(dateIn: Double, pcyOut: POINTER(Windows.Win32.System.Com.CY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFromStr(strIn: Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, pcyOut: POINTER(Windows.Win32.System.Com.CY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFromDisp(pdispIn: Windows.Win32.System.Com.IDispatch_head, lcid: UInt32, pcyOut: POINTER(Windows.Win32.System.Com.CY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFromBool(boolIn: Windows.Win32.Foundation.VARIANT_BOOL, pcyOut: POINTER(Windows.Win32.System.Com.CY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFromI1(cIn: Windows.Win32.Foundation.CHAR, pcyOut: POINTER(Windows.Win32.System.Com.CY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFromUI2(uiIn: UInt16, pcyOut: POINTER(Windows.Win32.System.Com.CY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFromUI4(ulIn: UInt32, pcyOut: POINTER(Windows.Win32.System.Com.CY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFromUI8(ui64In: UInt64, pcyOut: POINTER(Windows.Win32.System.Com.CY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFromDec(pdecIn: POINTER(Windows.Win32.Foundation.DECIMAL_head), pcyOut: POINTER(Windows.Win32.System.Com.CY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrFromUI1(bVal: Byte, lcid: UInt32, dwFlags: UInt32, pbstrOut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrFromI2(iVal: Int16, lcid: UInt32, dwFlags: UInt32, pbstrOut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrFromI4(lIn: Int32, lcid: UInt32, dwFlags: UInt32, pbstrOut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrFromI8(i64In: Int64, lcid: UInt32, dwFlags: UInt32, pbstrOut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrFromR4(fltIn: Single, lcid: UInt32, dwFlags: UInt32, pbstrOut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrFromR8(dblIn: Double, lcid: UInt32, dwFlags: UInt32, pbstrOut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrFromCy(cyIn: Windows.Win32.System.Com.CY, lcid: UInt32, dwFlags: UInt32, pbstrOut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrFromDate(dateIn: Double, lcid: UInt32, dwFlags: UInt32, pbstrOut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrFromDisp(pdispIn: Windows.Win32.System.Com.IDispatch_head, lcid: UInt32, dwFlags: UInt32, pbstrOut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrFromBool(boolIn: Windows.Win32.Foundation.VARIANT_BOOL, lcid: UInt32, dwFlags: UInt32, pbstrOut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrFromI1(cIn: Windows.Win32.Foundation.CHAR, lcid: UInt32, dwFlags: UInt32, pbstrOut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrFromUI2(uiIn: UInt16, lcid: UInt32, dwFlags: UInt32, pbstrOut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrFromUI4(ulIn: UInt32, lcid: UInt32, dwFlags: UInt32, pbstrOut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrFromUI8(ui64In: UInt64, lcid: UInt32, dwFlags: UInt32, pbstrOut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrFromDec(pdecIn: POINTER(Windows.Win32.Foundation.DECIMAL_head), lcid: UInt32, dwFlags: UInt32, pbstrOut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBoolFromUI1(bIn: Byte, pboolOut: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBoolFromI2(sIn: Int16, pboolOut: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBoolFromI4(lIn: Int32, pboolOut: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBoolFromI8(i64In: Int64, pboolOut: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBoolFromR4(fltIn: Single, pboolOut: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBoolFromR8(dblIn: Double, pboolOut: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBoolFromDate(dateIn: Double, pboolOut: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBoolFromCy(cyIn: Windows.Win32.System.Com.CY, pboolOut: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBoolFromStr(strIn: Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, pboolOut: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBoolFromDisp(pdispIn: Windows.Win32.System.Com.IDispatch_head, lcid: UInt32, pboolOut: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBoolFromI1(cIn: Windows.Win32.Foundation.CHAR, pboolOut: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBoolFromUI2(uiIn: UInt16, pboolOut: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBoolFromUI4(ulIn: UInt32, pboolOut: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBoolFromUI8(i64In: UInt64, pboolOut: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBoolFromDec(pdecIn: POINTER(Windows.Win32.Foundation.DECIMAL_head), pboolOut: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI1FromUI1(bIn: Byte, pcOut: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI1FromI2(uiIn: Int16, pcOut: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI1FromI4(lIn: Int32, pcOut: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI1FromI8(i64In: Int64, pcOut: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI1FromR4(fltIn: Single, pcOut: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI1FromR8(dblIn: Double, pcOut: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI1FromDate(dateIn: Double, pcOut: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI1FromCy(cyIn: Windows.Win32.System.Com.CY, pcOut: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI1FromStr(strIn: Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, pcOut: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI1FromDisp(pdispIn: Windows.Win32.System.Com.IDispatch_head, lcid: UInt32, pcOut: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI1FromBool(boolIn: Windows.Win32.Foundation.VARIANT_BOOL, pcOut: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI1FromUI2(uiIn: UInt16, pcOut: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI1FromUI4(ulIn: UInt32, pcOut: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI1FromUI8(i64In: UInt64, pcOut: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI1FromDec(pdecIn: POINTER(Windows.Win32.Foundation.DECIMAL_head), pcOut: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI2FromUI1(bIn: Byte, puiOut: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI2FromI2(uiIn: Int16, puiOut: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI2FromI4(lIn: Int32, puiOut: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI2FromI8(i64In: Int64, puiOut: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI2FromR4(fltIn: Single, puiOut: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI2FromR8(dblIn: Double, puiOut: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI2FromDate(dateIn: Double, puiOut: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI2FromCy(cyIn: Windows.Win32.System.Com.CY, puiOut: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI2FromStr(strIn: Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, puiOut: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI2FromDisp(pdispIn: Windows.Win32.System.Com.IDispatch_head, lcid: UInt32, puiOut: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI2FromBool(boolIn: Windows.Win32.Foundation.VARIANT_BOOL, puiOut: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI2FromI1(cIn: Windows.Win32.Foundation.CHAR, puiOut: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI2FromUI4(ulIn: UInt32, puiOut: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI2FromUI8(i64In: UInt64, puiOut: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI2FromDec(pdecIn: POINTER(Windows.Win32.Foundation.DECIMAL_head), puiOut: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI4FromUI1(bIn: Byte, pulOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI4FromI2(uiIn: Int16, pulOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI4FromI4(lIn: Int32, pulOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI4FromI8(i64In: Int64, plOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI4FromR4(fltIn: Single, pulOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI4FromR8(dblIn: Double, pulOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI4FromDate(dateIn: Double, pulOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI4FromCy(cyIn: Windows.Win32.System.Com.CY, pulOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI4FromStr(strIn: Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, pulOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI4FromDisp(pdispIn: Windows.Win32.System.Com.IDispatch_head, lcid: UInt32, pulOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI4FromBool(boolIn: Windows.Win32.Foundation.VARIANT_BOOL, pulOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI4FromI1(cIn: Windows.Win32.Foundation.CHAR, pulOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI4FromUI2(uiIn: UInt16, pulOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI4FromUI8(ui64In: UInt64, plOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI4FromDec(pdecIn: POINTER(Windows.Win32.Foundation.DECIMAL_head), pulOut: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI8FromUI1(bIn: Byte, pi64Out: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI8FromI2(sIn: Int16, pi64Out: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI8FromI8(ui64In: Int64, pi64Out: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI8FromR4(fltIn: Single, pi64Out: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI8FromR8(dblIn: Double, pi64Out: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI8FromCy(cyIn: Windows.Win32.System.Com.CY, pi64Out: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI8FromDate(dateIn: Double, pi64Out: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI8FromStr(strIn: Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, pi64Out: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI8FromDisp(pdispIn: Windows.Win32.System.Com.IDispatch_head, lcid: UInt32, pi64Out: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI8FromBool(boolIn: Windows.Win32.Foundation.VARIANT_BOOL, pi64Out: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI8FromI1(cIn: Windows.Win32.Foundation.CHAR, pi64Out: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI8FromUI2(uiIn: UInt16, pi64Out: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI8FromUI4(ulIn: UInt32, pi64Out: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI8FromDec(pdecIn: POINTER(Windows.Win32.Foundation.DECIMAL_head), pi64Out: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFromUI1(bIn: Byte, pdecOut: POINTER(Windows.Win32.Foundation.DECIMAL_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFromI2(uiIn: Int16, pdecOut: POINTER(Windows.Win32.Foundation.DECIMAL_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFromI4(lIn: Int32, pdecOut: POINTER(Windows.Win32.Foundation.DECIMAL_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFromI8(i64In: Int64, pdecOut: POINTER(Windows.Win32.Foundation.DECIMAL_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFromR4(fltIn: Single, pdecOut: POINTER(Windows.Win32.Foundation.DECIMAL_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFromR8(dblIn: Double, pdecOut: POINTER(Windows.Win32.Foundation.DECIMAL_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFromDate(dateIn: Double, pdecOut: POINTER(Windows.Win32.Foundation.DECIMAL_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFromCy(cyIn: Windows.Win32.System.Com.CY, pdecOut: POINTER(Windows.Win32.Foundation.DECIMAL_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFromStr(strIn: Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, pdecOut: POINTER(Windows.Win32.Foundation.DECIMAL_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFromDisp(pdispIn: Windows.Win32.System.Com.IDispatch_head, lcid: UInt32, pdecOut: POINTER(Windows.Win32.Foundation.DECIMAL_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFromBool(boolIn: Windows.Win32.Foundation.VARIANT_BOOL, pdecOut: POINTER(Windows.Win32.Foundation.DECIMAL_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFromI1(cIn: Windows.Win32.Foundation.CHAR, pdecOut: POINTER(Windows.Win32.Foundation.DECIMAL_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFromUI2(uiIn: UInt16, pdecOut: POINTER(Windows.Win32.Foundation.DECIMAL_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFromUI4(ulIn: UInt32, pdecOut: POINTER(Windows.Win32.Foundation.DECIMAL_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFromUI8(ui64In: UInt64, pdecOut: POINTER(Windows.Win32.Foundation.DECIMAL_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarParseNumFromStr(strIn: Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, pnumprs: POINTER(Windows.Win32.System.Ole.NUMPARSE_head), rgbDig: c_char_p_no) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarNumFromParseNum(pnumprs: POINTER(Windows.Win32.System.Ole.NUMPARSE_head), rgbDig: c_char_p_no, dwVtBits: UInt32, pvar: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarAdd(pvarLeft: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarRight: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarAnd(pvarLeft: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarRight: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCat(pvarLeft: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarRight: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDiv(pvarLeft: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarRight: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarEqv(pvarLeft: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarRight: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarIdiv(pvarLeft: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarRight: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarImp(pvarLeft: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarRight: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarMod(pvarLeft: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarRight: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarMul(pvarLeft: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarRight: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarOr(pvarLeft: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarRight: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarPow(pvarLeft: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarRight: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarSub(pvarLeft: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarRight: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarXor(pvarLeft: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarRight: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarAbs(pvarIn: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarFix(pvarIn: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarInt(pvarIn: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarNeg(pvarIn: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarNot(pvarIn: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarRound(pvarIn: POINTER(Windows.Win32.System.Com.VARIANT_head), cDecimals: Int32, pvarResult: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCmp(pvarLeft: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarRight: POINTER(Windows.Win32.System.Com.VARIANT_head), lcid: UInt32, dwFlags: UInt32) -> Windows.Win32.System.Ole.VARCMP: ...
@winfunctype('OLEAUT32.dll')
def VarDecAdd(pdecLeft: POINTER(Windows.Win32.Foundation.DECIMAL_head), pdecRight: POINTER(Windows.Win32.Foundation.DECIMAL_head), pdecResult: POINTER(Windows.Win32.Foundation.DECIMAL_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecDiv(pdecLeft: POINTER(Windows.Win32.Foundation.DECIMAL_head), pdecRight: POINTER(Windows.Win32.Foundation.DECIMAL_head), pdecResult: POINTER(Windows.Win32.Foundation.DECIMAL_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecMul(pdecLeft: POINTER(Windows.Win32.Foundation.DECIMAL_head), pdecRight: POINTER(Windows.Win32.Foundation.DECIMAL_head), pdecResult: POINTER(Windows.Win32.Foundation.DECIMAL_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecSub(pdecLeft: POINTER(Windows.Win32.Foundation.DECIMAL_head), pdecRight: POINTER(Windows.Win32.Foundation.DECIMAL_head), pdecResult: POINTER(Windows.Win32.Foundation.DECIMAL_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecAbs(pdecIn: POINTER(Windows.Win32.Foundation.DECIMAL_head), pdecResult: POINTER(Windows.Win32.Foundation.DECIMAL_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFix(pdecIn: POINTER(Windows.Win32.Foundation.DECIMAL_head), pdecResult: POINTER(Windows.Win32.Foundation.DECIMAL_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecInt(pdecIn: POINTER(Windows.Win32.Foundation.DECIMAL_head), pdecResult: POINTER(Windows.Win32.Foundation.DECIMAL_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecNeg(pdecIn: POINTER(Windows.Win32.Foundation.DECIMAL_head), pdecResult: POINTER(Windows.Win32.Foundation.DECIMAL_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecRound(pdecIn: POINTER(Windows.Win32.Foundation.DECIMAL_head), cDecimals: Int32, pdecResult: POINTER(Windows.Win32.Foundation.DECIMAL_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecCmp(pdecLeft: POINTER(Windows.Win32.Foundation.DECIMAL_head), pdecRight: POINTER(Windows.Win32.Foundation.DECIMAL_head)) -> Windows.Win32.System.Ole.VARCMP: ...
@winfunctype('OLEAUT32.dll')
def VarDecCmpR8(pdecLeft: POINTER(Windows.Win32.Foundation.DECIMAL_head), dblRight: Double) -> Windows.Win32.System.Ole.VARCMP: ...
@winfunctype('OLEAUT32.dll')
def VarCyAdd(cyLeft: Windows.Win32.System.Com.CY, cyRight: Windows.Win32.System.Com.CY, pcyResult: POINTER(Windows.Win32.System.Com.CY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyMul(cyLeft: Windows.Win32.System.Com.CY, cyRight: Windows.Win32.System.Com.CY, pcyResult: POINTER(Windows.Win32.System.Com.CY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyMulI4(cyLeft: Windows.Win32.System.Com.CY, lRight: Int32, pcyResult: POINTER(Windows.Win32.System.Com.CY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyMulI8(cyLeft: Windows.Win32.System.Com.CY, lRight: Int64, pcyResult: POINTER(Windows.Win32.System.Com.CY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCySub(cyLeft: Windows.Win32.System.Com.CY, cyRight: Windows.Win32.System.Com.CY, pcyResult: POINTER(Windows.Win32.System.Com.CY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyAbs(cyIn: Windows.Win32.System.Com.CY, pcyResult: POINTER(Windows.Win32.System.Com.CY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFix(cyIn: Windows.Win32.System.Com.CY, pcyResult: POINTER(Windows.Win32.System.Com.CY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyInt(cyIn: Windows.Win32.System.Com.CY, pcyResult: POINTER(Windows.Win32.System.Com.CY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyNeg(cyIn: Windows.Win32.System.Com.CY, pcyResult: POINTER(Windows.Win32.System.Com.CY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyRound(cyIn: Windows.Win32.System.Com.CY, cDecimals: Int32, pcyResult: POINTER(Windows.Win32.System.Com.CY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyCmp(cyLeft: Windows.Win32.System.Com.CY, cyRight: Windows.Win32.System.Com.CY) -> Windows.Win32.System.Ole.VARCMP: ...
@winfunctype('OLEAUT32.dll')
def VarCyCmpR8(cyLeft: Windows.Win32.System.Com.CY, dblRight: Double) -> Windows.Win32.System.Ole.VARCMP: ...
@winfunctype('OLEAUT32.dll')
def VarBstrCat(bstrLeft: Windows.Win32.Foundation.BSTR, bstrRight: Windows.Win32.Foundation.BSTR, pbstrResult: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrCmp(bstrLeft: Windows.Win32.Foundation.BSTR, bstrRight: Windows.Win32.Foundation.BSTR, lcid: UInt32, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8Pow(dblLeft: Double, dblRight: Double, pdblResult: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4CmpR8(fltLeft: Single, dblRight: Double) -> Windows.Win32.System.Ole.VARCMP: ...
@winfunctype('OLEAUT32.dll')
def VarR8Round(dblIn: Double, cDecimals: Int32, pdblResult: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromUdate(pudateIn: POINTER(Windows.Win32.System.Ole.UDATE_head), dwFlags: UInt32, pdateOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromUdateEx(pudateIn: POINTER(Windows.Win32.System.Ole.UDATE_head), lcid: UInt32, dwFlags: UInt32, pdateOut: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUdateFromDate(dateIn: Double, dwFlags: UInt32, pudateOut: POINTER(Windows.Win32.System.Ole.UDATE_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def GetAltMonthNames(lcid: UInt32, prgp: POINTER(POINTER(Windows.Win32.Foundation.PWSTR))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarFormat(pvarIn: POINTER(Windows.Win32.System.Com.VARIANT_head), pstrFormat: Windows.Win32.Foundation.PWSTR, iFirstDay: Windows.Win32.System.Ole.VARFORMAT_FIRST_DAY, iFirstWeek: Windows.Win32.System.Ole.VARFORMAT_FIRST_WEEK, dwFlags: UInt32, pbstrOut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarFormatDateTime(pvarIn: POINTER(Windows.Win32.System.Com.VARIANT_head), iNamedFormat: Windows.Win32.System.Ole.VARFORMAT_NAMED_FORMAT, dwFlags: UInt32, pbstrOut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarFormatNumber(pvarIn: POINTER(Windows.Win32.System.Com.VARIANT_head), iNumDig: Int32, iIncLead: Windows.Win32.System.Ole.VARFORMAT_LEADING_DIGIT, iUseParens: Windows.Win32.System.Ole.VARFORMAT_PARENTHESES, iGroup: Windows.Win32.System.Ole.VARFORMAT_GROUP, dwFlags: UInt32, pbstrOut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarFormatPercent(pvarIn: POINTER(Windows.Win32.System.Com.VARIANT_head), iNumDig: Int32, iIncLead: Windows.Win32.System.Ole.VARFORMAT_LEADING_DIGIT, iUseParens: Windows.Win32.System.Ole.VARFORMAT_PARENTHESES, iGroup: Windows.Win32.System.Ole.VARFORMAT_GROUP, dwFlags: UInt32, pbstrOut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarFormatCurrency(pvarIn: POINTER(Windows.Win32.System.Com.VARIANT_head), iNumDig: Int32, iIncLead: Int32, iUseParens: Int32, iGroup: Int32, dwFlags: UInt32, pbstrOut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarWeekdayName(iWeekday: Int32, fAbbrev: Int32, iFirstDay: Int32, dwFlags: UInt32, pbstrOut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarMonthName(iMonth: Int32, fAbbrev: Int32, dwFlags: UInt32, pbstrOut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarFormatFromTokens(pvarIn: POINTER(Windows.Win32.System.Com.VARIANT_head), pstrFormat: Windows.Win32.Foundation.PWSTR, pbTokCur: c_char_p_no, dwFlags: UInt32, pbstrOut: POINTER(Windows.Win32.Foundation.BSTR), lcid: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarTokenizeFormatString(pstrFormat: Windows.Win32.Foundation.PWSTR, rgbTok: c_char_p_no, cbTok: Int32, iFirstDay: Windows.Win32.System.Ole.VARFORMAT_FIRST_DAY, iFirstWeek: Windows.Win32.System.Ole.VARFORMAT_FIRST_WEEK, lcid: UInt32, pcbActual: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def LHashValOfNameSysA(syskind: Windows.Win32.System.Com.SYSKIND, lcid: UInt32, szName: Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('OLEAUT32.dll')
def LHashValOfNameSys(syskind: Windows.Win32.System.Com.SYSKIND, lcid: UInt32, szName: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('OLEAUT32.dll')
def LoadTypeLib(szFile: Windows.Win32.Foundation.PWSTR, pptlib: POINTER(Windows.Win32.System.Com.ITypeLib_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def LoadTypeLibEx(szFile: Windows.Win32.Foundation.PWSTR, regkind: Windows.Win32.System.Ole.REGKIND, pptlib: POINTER(Windows.Win32.System.Com.ITypeLib_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def LoadRegTypeLib(rguid: POINTER(Guid), wVerMajor: UInt16, wVerMinor: UInt16, lcid: UInt32, pptlib: POINTER(Windows.Win32.System.Com.ITypeLib_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def QueryPathOfRegTypeLib(guid: POINTER(Guid), wMaj: UInt16, wMin: UInt16, lcid: UInt32, lpbstrPathName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def RegisterTypeLib(ptlib: Windows.Win32.System.Com.ITypeLib_head, szFullPath: Windows.Win32.Foundation.PWSTR, szHelpDir: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def UnRegisterTypeLib(libID: POINTER(Guid), wVerMajor: UInt16, wVerMinor: UInt16, lcid: UInt32, syskind: Windows.Win32.System.Com.SYSKIND) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def RegisterTypeLibForUser(ptlib: Windows.Win32.System.Com.ITypeLib_head, szFullPath: Windows.Win32.Foundation.PWSTR, szHelpDir: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def UnRegisterTypeLibForUser(libID: POINTER(Guid), wMajorVerNum: UInt16, wMinorVerNum: UInt16, lcid: UInt32, syskind: Windows.Win32.System.Com.SYSKIND) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def CreateTypeLib(syskind: Windows.Win32.System.Com.SYSKIND, szFile: Windows.Win32.Foundation.PWSTR, ppctlib: POINTER(Windows.Win32.System.Ole.ICreateTypeLib_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def CreateTypeLib2(syskind: Windows.Win32.System.Com.SYSKIND, szFile: Windows.Win32.Foundation.PWSTR, ppctlib: POINTER(Windows.Win32.System.Ole.ICreateTypeLib2_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def DispGetParam(pdispparams: POINTER(Windows.Win32.System.Com.DISPPARAMS_head), position: UInt32, vtTarg: Windows.Win32.System.Com.VARENUM, pvarResult: POINTER(Windows.Win32.System.Com.VARIANT_head), puArgErr: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def DispGetIDsOfNames(ptinfo: Windows.Win32.System.Com.ITypeInfo_head, rgszNames: POINTER(Windows.Win32.Foundation.PWSTR), cNames: UInt32, rgdispid: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def DispInvoke(_this: c_void_p, ptinfo: Windows.Win32.System.Com.ITypeInfo_head, dispidMember: Int32, wFlags: UInt16, pparams: POINTER(Windows.Win32.System.Com.DISPPARAMS_head), pvarResult: POINTER(Windows.Win32.System.Com.VARIANT_head), pexcepinfo: POINTER(Windows.Win32.System.Com.EXCEPINFO_head), puArgErr: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def CreateDispTypeInfo(pidata: POINTER(Windows.Win32.System.Ole.INTERFACEDATA_head), lcid: UInt32, pptinfo: POINTER(Windows.Win32.System.Com.ITypeInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def CreateStdDispatch(punkOuter: Windows.Win32.System.Com.IUnknown_head, pvThis: c_void_p, ptinfo: Windows.Win32.System.Com.ITypeInfo_head, ppunkStdDisp: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def DispCallFunc(pvInstance: c_void_p, oVft: UIntPtr, cc: Windows.Win32.System.Com.CALLCONV, vtReturn: Windows.Win32.System.Com.VARENUM, cActuals: UInt32, prgvt: POINTER(UInt16), prgpvarg: POINTER(POINTER(Windows.Win32.System.Com.VARIANT_head)), pvargResult: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def RegisterActiveObject(punk: Windows.Win32.System.Com.IUnknown_head, rclsid: POINTER(Guid), dwFlags: Windows.Win32.System.Ole.ACTIVEOBJECT_FLAGS, pdwRegister: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def RevokeActiveObject(dwRegister: UInt32, pvReserved: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def GetActiveObject(rclsid: POINTER(Guid), pvReserved: c_void_p, ppunk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def CreateErrorInfo(pperrinfo: POINTER(Windows.Win32.System.Ole.ICreateErrorInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def GetRecordInfoFromTypeInfo(pTypeInfo: Windows.Win32.System.Com.ITypeInfo_head, ppRecInfo: POINTER(Windows.Win32.System.Ole.IRecordInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def GetRecordInfoFromGuids(rGuidTypeLib: POINTER(Guid), uVerMajor: UInt32, uVerMinor: UInt32, lcid: UInt32, rGuidTypeInfo: POINTER(Guid), ppRecInfo: POINTER(Windows.Win32.System.Ole.IRecordInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def OaBuildVersion() -> UInt32: ...
@winfunctype('OLEAUT32.dll')
def ClearCustData(pCustData: POINTER(Windows.Win32.System.Com.CUSTDATA_head)) -> Void: ...
@winfunctype('OLEAUT32.dll')
def OaEnablePerUserTLibRegistration() -> Void: ...
@winfunctype('ole32.dll')
def OleBuildVersion() -> UInt32: ...
@winfunctype('OLE32.dll')
def OleInitialize(pvReserved: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleUninitialize() -> Void: ...
@winfunctype('OLE32.dll')
def OleQueryLinkFromData(pSrcDataObject: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleQueryCreateFromData(pSrcDataObject: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleCreate(rclsid: POINTER(Guid), riid: POINTER(Guid), renderopt: Windows.Win32.System.Ole.OLERENDER, pFormatEtc: POINTER(Windows.Win32.System.Com.FORMATETC_head), pClientSite: Windows.Win32.System.Ole.IOleClientSite_head, pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleCreateEx(rclsid: POINTER(Guid), riid: POINTER(Guid), dwFlags: Windows.Win32.System.Ole.OLECREATE, renderopt: Windows.Win32.System.Ole.OLERENDER, cFormats: UInt32, rgAdvf: POINTER(UInt32), rgFormatEtc: POINTER(Windows.Win32.System.Com.FORMATETC_head), lpAdviseSink: Windows.Win32.System.Com.IAdviseSink_head, rgdwConnection: POINTER(UInt32), pClientSite: Windows.Win32.System.Ole.IOleClientSite_head, pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleCreateFromData(pSrcDataObj: Windows.Win32.System.Com.IDataObject_head, riid: POINTER(Guid), renderopt: Windows.Win32.System.Ole.OLERENDER, pFormatEtc: POINTER(Windows.Win32.System.Com.FORMATETC_head), pClientSite: Windows.Win32.System.Ole.IOleClientSite_head, pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleCreateFromDataEx(pSrcDataObj: Windows.Win32.System.Com.IDataObject_head, riid: POINTER(Guid), dwFlags: Windows.Win32.System.Ole.OLECREATE, renderopt: Windows.Win32.System.Ole.OLERENDER, cFormats: UInt32, rgAdvf: POINTER(UInt32), rgFormatEtc: POINTER(Windows.Win32.System.Com.FORMATETC_head), lpAdviseSink: Windows.Win32.System.Com.IAdviseSink_head, rgdwConnection: POINTER(UInt32), pClientSite: Windows.Win32.System.Ole.IOleClientSite_head, pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleCreateLinkFromData(pSrcDataObj: Windows.Win32.System.Com.IDataObject_head, riid: POINTER(Guid), renderopt: Windows.Win32.System.Ole.OLERENDER, pFormatEtc: POINTER(Windows.Win32.System.Com.FORMATETC_head), pClientSite: Windows.Win32.System.Ole.IOleClientSite_head, pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleCreateLinkFromDataEx(pSrcDataObj: Windows.Win32.System.Com.IDataObject_head, riid: POINTER(Guid), dwFlags: Windows.Win32.System.Ole.OLECREATE, renderopt: Windows.Win32.System.Ole.OLERENDER, cFormats: UInt32, rgAdvf: POINTER(UInt32), rgFormatEtc: POINTER(Windows.Win32.System.Com.FORMATETC_head), lpAdviseSink: Windows.Win32.System.Com.IAdviseSink_head, rgdwConnection: POINTER(UInt32), pClientSite: Windows.Win32.System.Ole.IOleClientSite_head, pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleCreateStaticFromData(pSrcDataObj: Windows.Win32.System.Com.IDataObject_head, iid: POINTER(Guid), renderopt: Windows.Win32.System.Ole.OLERENDER, pFormatEtc: POINTER(Windows.Win32.System.Com.FORMATETC_head), pClientSite: Windows.Win32.System.Ole.IOleClientSite_head, pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleCreateLink(pmkLinkSrc: Windows.Win32.System.Com.IMoniker_head, riid: POINTER(Guid), renderopt: Windows.Win32.System.Ole.OLERENDER, lpFormatEtc: POINTER(Windows.Win32.System.Com.FORMATETC_head), pClientSite: Windows.Win32.System.Ole.IOleClientSite_head, pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleCreateLinkEx(pmkLinkSrc: Windows.Win32.System.Com.IMoniker_head, riid: POINTER(Guid), dwFlags: Windows.Win32.System.Ole.OLECREATE, renderopt: Windows.Win32.System.Ole.OLERENDER, cFormats: UInt32, rgAdvf: POINTER(UInt32), rgFormatEtc: POINTER(Windows.Win32.System.Com.FORMATETC_head), lpAdviseSink: Windows.Win32.System.Com.IAdviseSink_head, rgdwConnection: POINTER(UInt32), pClientSite: Windows.Win32.System.Ole.IOleClientSite_head, pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleCreateLinkToFile(lpszFileName: Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), renderopt: Windows.Win32.System.Ole.OLERENDER, lpFormatEtc: POINTER(Windows.Win32.System.Com.FORMATETC_head), pClientSite: Windows.Win32.System.Ole.IOleClientSite_head, pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleCreateLinkToFileEx(lpszFileName: Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), dwFlags: Windows.Win32.System.Ole.OLECREATE, renderopt: Windows.Win32.System.Ole.OLERENDER, cFormats: UInt32, rgAdvf: POINTER(UInt32), rgFormatEtc: POINTER(Windows.Win32.System.Com.FORMATETC_head), lpAdviseSink: Windows.Win32.System.Com.IAdviseSink_head, rgdwConnection: POINTER(UInt32), pClientSite: Windows.Win32.System.Ole.IOleClientSite_head, pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleCreateFromFile(rclsid: POINTER(Guid), lpszFileName: Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), renderopt: Windows.Win32.System.Ole.OLERENDER, lpFormatEtc: POINTER(Windows.Win32.System.Com.FORMATETC_head), pClientSite: Windows.Win32.System.Ole.IOleClientSite_head, pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleCreateFromFileEx(rclsid: POINTER(Guid), lpszFileName: Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), dwFlags: Windows.Win32.System.Ole.OLECREATE, renderopt: Windows.Win32.System.Ole.OLERENDER, cFormats: UInt32, rgAdvf: POINTER(UInt32), rgFormatEtc: POINTER(Windows.Win32.System.Com.FORMATETC_head), lpAdviseSink: Windows.Win32.System.Com.IAdviseSink_head, rgdwConnection: POINTER(UInt32), pClientSite: Windows.Win32.System.Ole.IOleClientSite_head, pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleLoad(pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, riid: POINTER(Guid), pClientSite: Windows.Win32.System.Ole.IOleClientSite_head, ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleSave(pPS: Windows.Win32.System.Com.StructuredStorage.IPersistStorage_head, pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, fSameAsLoad: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleLoadFromStream(pStm: Windows.Win32.System.Com.IStream_head, iidInterface: POINTER(Guid), ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleSaveToStream(pPStm: Windows.Win32.System.Com.IPersistStream_head, pStm: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleSetContainedObject(pUnknown: Windows.Win32.System.Com.IUnknown_head, fContained: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleNoteObjectVisible(pUnknown: Windows.Win32.System.Com.IUnknown_head, fVisible: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def RegisterDragDrop(hwnd: Windows.Win32.Foundation.HWND, pDropTarget: Windows.Win32.System.Ole.IDropTarget_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def RevokeDragDrop(hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def DoDragDrop(pDataObj: Windows.Win32.System.Com.IDataObject_head, pDropSource: Windows.Win32.System.Ole.IDropSource_head, dwOKEffects: Windows.Win32.System.Ole.DROPEFFECT, pdwEffect: POINTER(Windows.Win32.System.Ole.DROPEFFECT)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleSetClipboard(pDataObj: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleGetClipboard(ppDataObj: POINTER(Windows.Win32.System.Com.IDataObject_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleGetClipboardWithEnterpriseInfo(dataObject: POINTER(Windows.Win32.System.Com.IDataObject_head), dataEnterpriseId: POINTER(Windows.Win32.Foundation.PWSTR), sourceDescription: POINTER(Windows.Win32.Foundation.PWSTR), targetDescription: POINTER(Windows.Win32.Foundation.PWSTR), dataDescription: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleFlushClipboard() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleIsCurrentClipboard(pDataObj: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleCreateMenuDescriptor(hmenuCombined: Windows.Win32.UI.WindowsAndMessaging.HMENU, lpMenuWidths: POINTER(Windows.Win32.System.Ole.OLEMENUGROUPWIDTHS_head)) -> IntPtr: ...
@winfunctype('OLE32.dll')
def OleSetMenuDescriptor(holemenu: IntPtr, hwndFrame: Windows.Win32.Foundation.HWND, hwndActiveObject: Windows.Win32.Foundation.HWND, lpFrame: Windows.Win32.System.Ole.IOleInPlaceFrame_head, lpActiveObj: Windows.Win32.System.Ole.IOleInPlaceActiveObject_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleDestroyMenuDescriptor(holemenu: IntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleTranslateAccelerator(lpFrame: Windows.Win32.System.Ole.IOleInPlaceFrame_head, lpFrameInfo: POINTER(Windows.Win32.System.Ole.OLEINPLACEFRAMEINFO_head), lpmsg: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleDuplicateData(hSrc: Windows.Win32.Foundation.HANDLE, cfFormat: Windows.Win32.System.Ole.CLIPBOARD_FORMAT, uiFlags: Windows.Win32.System.Memory.GLOBAL_ALLOC_FLAGS) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('OLE32.dll')
def OleDraw(pUnknown: Windows.Win32.System.Com.IUnknown_head, dwAspect: UInt32, hdcDraw: Windows.Win32.Graphics.Gdi.HDC, lprcBounds: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleRun(pUnknown: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleIsRunning(pObject: Windows.Win32.System.Ole.IOleObject_head) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('OLE32.dll')
def OleLockRunning(pUnknown: Windows.Win32.System.Com.IUnknown_head, fLock: Windows.Win32.Foundation.BOOL, fLastUnlockCloses: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def ReleaseStgMedium(param0: POINTER(Windows.Win32.System.Com.STGMEDIUM_head)) -> Void: ...
@winfunctype('OLE32.dll')
def CreateOleAdviseHolder(ppOAHolder: POINTER(Windows.Win32.System.Ole.IOleAdviseHolder_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleCreateDefaultHandler(clsid: POINTER(Guid), pUnkOuter: Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), lplpObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleCreateEmbeddingHelper(clsid: POINTER(Guid), pUnkOuter: Windows.Win32.System.Com.IUnknown_head, flags: Windows.Win32.System.Ole.EMBDHLP_FLAGS, pCF: Windows.Win32.System.Com.IClassFactory_head, riid: POINTER(Guid), lplpObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def IsAccelerator(hAccel: Windows.Win32.UI.WindowsAndMessaging.HACCEL, cAccelEntries: Int32, lpMsg: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head), lpwCmd: POINTER(UInt16)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ole32.dll')
def OleGetIconOfFile(lpszPath: Windows.Win32.Foundation.PWSTR, fUseFileAsLabel: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HGLOBAL: ...
@winfunctype('OLE32.dll')
def OleGetIconOfClass(rclsid: POINTER(Guid), lpszLabel: Windows.Win32.Foundation.PWSTR, fUseTypeAsLabel: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HGLOBAL: ...
@winfunctype('ole32.dll')
def OleMetafilePictFromIconAndLabel(hIcon: Windows.Win32.UI.WindowsAndMessaging.HICON, lpszLabel: Windows.Win32.Foundation.PWSTR, lpszSourceFile: Windows.Win32.Foundation.PWSTR, iIconIndex: UInt32) -> Windows.Win32.Foundation.HGLOBAL: ...
@winfunctype('OLE32.dll')
def OleRegGetUserType(clsid: POINTER(Guid), dwFormOfType: Windows.Win32.System.Ole.USERCLASSTYPE, pszUserType: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleRegGetMiscStatus(clsid: POINTER(Guid), dwAspect: UInt32, pdwStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleRegEnumFormatEtc(clsid: POINTER(Guid), dwDirection: UInt32, ppenum: POINTER(Windows.Win32.System.Com.IEnumFORMATETC_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleRegEnumVerbs(clsid: POINTER(Guid), ppenum: POINTER(Windows.Win32.System.Ole.IEnumOLEVERB_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleDoAutoConvert(pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, pClsidNew: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleGetAutoConvert(clsidOld: POINTER(Guid), pClsidNew: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleSetAutoConvert(clsidOld: POINTER(Guid), clsidNew: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def HRGN_UserSize(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(Windows.Win32.Graphics.Gdi.HRGN)) -> UInt32: ...
@winfunctype('OLE32.dll')
def HRGN_UserMarshal(param0: POINTER(UInt32), param1: c_char_p_no, param2: POINTER(Windows.Win32.Graphics.Gdi.HRGN)) -> c_char_p_no: ...
@winfunctype('OLE32.dll')
def HRGN_UserUnmarshal(param0: POINTER(UInt32), param1: c_char_p_no, param2: POINTER(Windows.Win32.Graphics.Gdi.HRGN)) -> c_char_p_no: ...
@winfunctype('OLE32.dll')
def HRGN_UserFree(param0: POINTER(UInt32), param1: POINTER(Windows.Win32.Graphics.Gdi.HRGN)) -> Void: ...
@winfunctype('api-ms-win-core-marshal-l1-1-0.dll')
def HRGN_UserSize64(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(Windows.Win32.Graphics.Gdi.HRGN)) -> UInt32: ...
@winfunctype('api-ms-win-core-marshal-l1-1-0.dll')
def HRGN_UserMarshal64(param0: POINTER(UInt32), param1: c_char_p_no, param2: POINTER(Windows.Win32.Graphics.Gdi.HRGN)) -> c_char_p_no: ...
@winfunctype('api-ms-win-core-marshal-l1-1-0.dll')
def HRGN_UserUnmarshal64(param0: POINTER(UInt32), param1: c_char_p_no, param2: POINTER(Windows.Win32.Graphics.Gdi.HRGN)) -> c_char_p_no: ...
@winfunctype('api-ms-win-core-marshal-l1-1-0.dll')
def HRGN_UserFree64(param0: POINTER(UInt32), param1: POINTER(Windows.Win32.Graphics.Gdi.HRGN)) -> Void: ...
@winfunctype('OLEAUT32.dll')
def OleCreatePropertyFrame(hwndOwner: Windows.Win32.Foundation.HWND, x: UInt32, y: UInt32, lpszCaption: Windows.Win32.Foundation.PWSTR, cObjects: UInt32, ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head), cPages: UInt32, pPageClsID: POINTER(Guid), lcid: UInt32, dwReserved: UInt32, pvReserved: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def OleCreatePropertyFrameIndirect(lpParams: POINTER(Windows.Win32.System.Ole.OCPFIPARAMS_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def OleTranslateColor(clr: UInt32, hpal: Windows.Win32.Graphics.Gdi.HPALETTE, lpcolorref: POINTER(Windows.Win32.Foundation.COLORREF)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def OleCreateFontIndirect(lpFontDesc: POINTER(Windows.Win32.System.Ole.FONTDESC_head), riid: POINTER(Guid), lplpvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def OleCreatePictureIndirect(lpPictDesc: POINTER(Windows.Win32.System.Ole.PICTDESC_head), riid: POINTER(Guid), fOwn: Windows.Win32.Foundation.BOOL, lplpvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def OleLoadPicture(lpstream: Windows.Win32.System.Com.IStream_head, lSize: Int32, fRunmode: Windows.Win32.Foundation.BOOL, riid: POINTER(Guid), lplpvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def OleLoadPictureEx(lpstream: Windows.Win32.System.Com.IStream_head, lSize: Int32, fRunmode: Windows.Win32.Foundation.BOOL, riid: POINTER(Guid), xSizeDesired: UInt32, ySizeDesired: UInt32, dwFlags: Windows.Win32.System.Ole.LOAD_PICTURE_FLAGS, lplpvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def OleLoadPicturePath(szURLorPath: Windows.Win32.Foundation.PWSTR, punkCaller: Windows.Win32.System.Com.IUnknown_head, dwReserved: UInt32, clrReserved: UInt32, riid: POINTER(Guid), ppvRet: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def OleLoadPictureFile(varFileName: Windows.Win32.System.Com.VARIANT, lplpdispPicture: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def OleLoadPictureFileEx(varFileName: Windows.Win32.System.Com.VARIANT, xSizeDesired: UInt32, ySizeDesired: UInt32, dwFlags: Windows.Win32.System.Ole.LOAD_PICTURE_FLAGS, lplpdispPicture: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def OleSavePictureFile(lpdispPicture: Windows.Win32.System.Com.IDispatch_head, bstrFileName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def OleIconToCursor(hinstExe: Windows.Win32.Foundation.HINSTANCE, hIcon: Windows.Win32.UI.WindowsAndMessaging.HICON) -> Windows.Win32.UI.WindowsAndMessaging.HCURSOR: ...
@winfunctype('oledlg.dll')
def OleUIAddVerbMenuW(lpOleObj: Windows.Win32.System.Ole.IOleObject_head, lpszShortType: Windows.Win32.Foundation.PWSTR, hMenu: Windows.Win32.UI.WindowsAndMessaging.HMENU, uPos: UInt32, uIDVerbMin: UInt32, uIDVerbMax: UInt32, bAddConvert: Windows.Win32.Foundation.BOOL, idConvert: UInt32, lphMenu: POINTER(Windows.Win32.UI.WindowsAndMessaging.HMENU)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('oledlg.dll')
def OleUIAddVerbMenuA(lpOleObj: Windows.Win32.System.Ole.IOleObject_head, lpszShortType: Windows.Win32.Foundation.PSTR, hMenu: Windows.Win32.UI.WindowsAndMessaging.HMENU, uPos: UInt32, uIDVerbMin: UInt32, uIDVerbMax: UInt32, bAddConvert: Windows.Win32.Foundation.BOOL, idConvert: UInt32, lphMenu: POINTER(Windows.Win32.UI.WindowsAndMessaging.HMENU)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('oledlg.dll')
def OleUIInsertObjectW(param0: POINTER(Windows.Win32.System.Ole.OLEUIINSERTOBJECTW_head)) -> UInt32: ...
@winfunctype('oledlg.dll')
def OleUIInsertObjectA(param0: POINTER(Windows.Win32.System.Ole.OLEUIINSERTOBJECTA_head)) -> UInt32: ...
@winfunctype('oledlg.dll')
def OleUIPasteSpecialW(param0: POINTER(Windows.Win32.System.Ole.OLEUIPASTESPECIALW_head)) -> UInt32: ...
@winfunctype('oledlg.dll')
def OleUIPasteSpecialA(param0: POINTER(Windows.Win32.System.Ole.OLEUIPASTESPECIALA_head)) -> UInt32: ...
@winfunctype('oledlg.dll')
def OleUIEditLinksW(param0: POINTER(Windows.Win32.System.Ole.OLEUIEDITLINKSW_head)) -> UInt32: ...
@winfunctype('oledlg.dll')
def OleUIEditLinksA(param0: POINTER(Windows.Win32.System.Ole.OLEUIEDITLINKSA_head)) -> UInt32: ...
@winfunctype('oledlg.dll')
def OleUIChangeIconW(param0: POINTER(Windows.Win32.System.Ole.OLEUICHANGEICONW_head)) -> UInt32: ...
@winfunctype('oledlg.dll')
def OleUIChangeIconA(param0: POINTER(Windows.Win32.System.Ole.OLEUICHANGEICONA_head)) -> UInt32: ...
@winfunctype('oledlg.dll')
def OleUIConvertW(param0: POINTER(Windows.Win32.System.Ole.OLEUICONVERTW_head)) -> UInt32: ...
@winfunctype('oledlg.dll')
def OleUIConvertA(param0: POINTER(Windows.Win32.System.Ole.OLEUICONVERTA_head)) -> UInt32: ...
@winfunctype('oledlg.dll')
def OleUICanConvertOrActivateAs(rClsid: POINTER(Guid), fIsLinkedObject: Windows.Win32.Foundation.BOOL, wFormat: UInt16) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('oledlg.dll')
def OleUIBusyW(param0: POINTER(Windows.Win32.System.Ole.OLEUIBUSYW_head)) -> UInt32: ...
@winfunctype('oledlg.dll')
def OleUIBusyA(param0: POINTER(Windows.Win32.System.Ole.OLEUIBUSYA_head)) -> UInt32: ...
@winfunctype('oledlg.dll')
def OleUIChangeSourceW(param0: POINTER(Windows.Win32.System.Ole.OLEUICHANGESOURCEW_head)) -> UInt32: ...
@winfunctype('oledlg.dll')
def OleUIChangeSourceA(param0: POINTER(Windows.Win32.System.Ole.OLEUICHANGESOURCEA_head)) -> UInt32: ...
@winfunctype('oledlg.dll')
def OleUIObjectPropertiesW(param0: POINTER(Windows.Win32.System.Ole.OLEUIOBJECTPROPSW_head)) -> UInt32: ...
@winfunctype('oledlg.dll')
def OleUIObjectPropertiesA(param0: POINTER(Windows.Win32.System.Ole.OLEUIOBJECTPROPSA_head)) -> UInt32: ...
@cfunctype('oledlg.dll')
def OleUIPromptUserW(nTemplate: Int32, hwndParent: Windows.Win32.Foundation.HWND) -> Int32: ...
@cfunctype('oledlg.dll')
def OleUIPromptUserA(nTemplate: Int32, hwndParent: Windows.Win32.Foundation.HWND) -> Int32: ...
@winfunctype('oledlg.dll')
def OleUIUpdateLinksW(lpOleUILinkCntr: Windows.Win32.System.Ole.IOleUILinkContainerW_head, hwndParent: Windows.Win32.Foundation.HWND, lpszTitle: Windows.Win32.Foundation.PWSTR, cLinks: Int32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('oledlg.dll')
def OleUIUpdateLinksA(lpOleUILinkCntr: Windows.Win32.System.Ole.IOleUILinkContainerA_head, hwndParent: Windows.Win32.Foundation.HWND, lpszTitle: Windows.Win32.Foundation.PSTR, cLinks: Int32) -> Windows.Win32.Foundation.BOOL: ...
BINDSPEED = Int32
BINDSPEED_INDEFINITE: BINDSPEED = 1
BINDSPEED_MODERATE: BINDSPEED = 2
BINDSPEED_IMMEDIATE: BINDSPEED = 3
BUSY_DIALOG_FLAGS = UInt32
BZ_DISABLECANCELBUTTON: BUSY_DIALOG_FLAGS = 1
BZ_DISABLESWITCHTOBUTTON: BUSY_DIALOG_FLAGS = 2
BZ_DISABLERETRYBUTTON: BUSY_DIALOG_FLAGS = 4
BZ_NOTRESPONDINGDIALOG: BUSY_DIALOG_FLAGS = 8
class CADWORD(Structure):
    cElems: UInt32
    pElems: POINTER(UInt32)
class CALPOLESTR(Structure):
    cElems: UInt32
    pElems: POINTER(Windows.Win32.Foundation.PWSTR)
class CAUUID(Structure):
    cElems: UInt32
    pElems: POINTER(Guid)
CHANGEKIND = Int32
CHANGEKIND_ADDMEMBER: CHANGEKIND = 0
CHANGEKIND_DELETEMEMBER: CHANGEKIND = 1
CHANGEKIND_SETNAMES: CHANGEKIND = 2
CHANGEKIND_SETDOCUMENTATION: CHANGEKIND = 3
CHANGEKIND_GENERAL: CHANGEKIND = 4
CHANGEKIND_INVALIDATE: CHANGEKIND = 5
CHANGEKIND_CHANGEFAILED: CHANGEKIND = 6
CHANGEKIND_MAX: CHANGEKIND = 7
CHANGE_ICON_FLAGS = Int32
CIF_SHOWHELP: CHANGE_ICON_FLAGS = 1
CIF_SELECTCURRENT: CHANGE_ICON_FLAGS = 2
CIF_SELECTDEFAULT: CHANGE_ICON_FLAGS = 4
CIF_SELECTFROMFILE: CHANGE_ICON_FLAGS = 8
CIF_USEICONEXE: CHANGE_ICON_FLAGS = 16
CHANGE_SOURCE_FLAGS = UInt32
CSF_SHOWHELP: CHANGE_SOURCE_FLAGS = 1
CSF_VALIDSOURCE: CHANGE_SOURCE_FLAGS = 2
CSF_ONLYGETSOURCE: CHANGE_SOURCE_FLAGS = 4
CSF_EXPLORER: CHANGE_SOURCE_FLAGS = 8
class CLEANLOCALSTORAGE(Structure):
    pInterface: Windows.Win32.System.Com.IUnknown_head
    pStorage: c_void_p
    flags: UInt32
CLIPBOARD_FORMAT = UInt16
CF_TEXT: CLIPBOARD_FORMAT = 1
CF_BITMAP: CLIPBOARD_FORMAT = 2
CF_METAFILEPICT: CLIPBOARD_FORMAT = 3
CF_SYLK: CLIPBOARD_FORMAT = 4
CF_DIF: CLIPBOARD_FORMAT = 5
CF_TIFF: CLIPBOARD_FORMAT = 6
CF_OEMTEXT: CLIPBOARD_FORMAT = 7
CF_DIB: CLIPBOARD_FORMAT = 8
CF_PALETTE: CLIPBOARD_FORMAT = 9
CF_PENDATA: CLIPBOARD_FORMAT = 10
CF_RIFF: CLIPBOARD_FORMAT = 11
CF_WAVE: CLIPBOARD_FORMAT = 12
CF_UNICODETEXT: CLIPBOARD_FORMAT = 13
CF_ENHMETAFILE: CLIPBOARD_FORMAT = 14
CF_HDROP: CLIPBOARD_FORMAT = 15
CF_LOCALE: CLIPBOARD_FORMAT = 16
CF_DIBV5: CLIPBOARD_FORMAT = 17
CF_MAX: CLIPBOARD_FORMAT = 18
CF_OWNERDISPLAY: CLIPBOARD_FORMAT = 128
CF_DSPTEXT: CLIPBOARD_FORMAT = 129
CF_DSPBITMAP: CLIPBOARD_FORMAT = 130
CF_DSPMETAFILEPICT: CLIPBOARD_FORMAT = 131
CF_DSPENHMETAFILE: CLIPBOARD_FORMAT = 142
CF_PRIVATEFIRST: CLIPBOARD_FORMAT = 512
CF_PRIVATELAST: CLIPBOARD_FORMAT = 767
CF_GDIOBJFIRST: CLIPBOARD_FORMAT = 768
CF_GDIOBJLAST: CLIPBOARD_FORMAT = 1023
class CONTROLINFO(Structure):
    cb: UInt32
    hAccel: Windows.Win32.UI.WindowsAndMessaging.HACCEL
    cAccel: UInt16
    dwFlags: Windows.Win32.System.Ole.CTRLINFO
CTRLINFO = Int32
CTRLINFO_EATS_RETURN: CTRLINFO = 1
CTRLINFO_EATS_ESCAPE: CTRLINFO = 2
DISCARDCACHE = Int32
DISCARDCACHE_SAVEIFDIRTY: DISCARDCACHE = 0
DISCARDCACHE_NOSAVE: DISCARDCACHE = 1
DOCMISC = Int32
DOCMISC_CANCREATEMULTIPLEVIEWS: DOCMISC = 1
DOCMISC_SUPPORTCOMPLEXRECTANGLES: DOCMISC = 2
DOCMISC_CANTOPENEDIT: DOCMISC = 4
DOCMISC_NOFILESUPPORT: DOCMISC = 8
DROPEFFECT = UInt32
DROPEFFECT_NONE: DROPEFFECT = 0
DROPEFFECT_COPY: DROPEFFECT = 1
DROPEFFECT_MOVE: DROPEFFECT = 2
DROPEFFECT_LINK: DROPEFFECT = 4
DROPEFFECT_SCROLL: DROPEFFECT = 2147483648
class DVASPECTINFO(Structure):
    cb: UInt32
    dwFlags: UInt32
DVASPECTINFOFLAG = Int32
DVASPECTINFOFLAG_CANOPTIMIZE: DVASPECTINFOFLAG = 1
class DVEXTENTINFO(Structure):
    cb: UInt32
    dwExtentMode: UInt32
    sizelProposed: Windows.Win32.Foundation.SIZE
DVEXTENTMODE = Int32
DVEXTENT_CONTENT: DVEXTENTMODE = 0
DVEXTENT_INTEGRAL: DVEXTENTMODE = 1
EDIT_LINKS_FLAGS = UInt32
ELF_SHOWHELP: EDIT_LINKS_FLAGS = 1
ELF_DISABLEUPDATENOW: EDIT_LINKS_FLAGS = 2
ELF_DISABLEOPENSOURCE: EDIT_LINKS_FLAGS = 4
ELF_DISABLECHANGESOURCE: EDIT_LINKS_FLAGS = 8
ELF_DISABLECANCELLINK: EDIT_LINKS_FLAGS = 16
EMBDHLP_FLAGS = UInt32
EMBDHLP_INPROC_HANDLER: EMBDHLP_FLAGS = 0
EMBDHLP_INPROC_SERVER: EMBDHLP_FLAGS = 1
EMBDHLP_CREATENOW: EMBDHLP_FLAGS = 0
EMBDHLP_DELAYCREATE: EMBDHLP_FLAGS = 65536
ENUM_CONTROLS_WHICH_FLAGS = UInt32
GCW_WCH_SIBLING: ENUM_CONTROLS_WHICH_FLAGS = 1
GC_WCH_CONTAINER: ENUM_CONTROLS_WHICH_FLAGS = 2
GC_WCH_CONTAINED: ENUM_CONTROLS_WHICH_FLAGS = 3
GC_WCH_ALL: ENUM_CONTROLS_WHICH_FLAGS = 4
GC_WCH_FREVERSEDIR: ENUM_CONTROLS_WHICH_FLAGS = 134217728
GC_WCH_FONLYAFTER: ENUM_CONTROLS_WHICH_FLAGS = 268435456
GC_WCH_FONLYBEFORE: ENUM_CONTROLS_WHICH_FLAGS = 536870912
GC_WCH_FSELECTED: ENUM_CONTROLS_WHICH_FLAGS = 1073741824
FDEX_PROP_FLAGS = UInt32
FDEX_PROP_FLAGS_fdexPropCanGet: FDEX_PROP_FLAGS = 1
FDEX_PROP_FLAGS_fdexPropCannotGet: FDEX_PROP_FLAGS = 2
FDEX_PROP_FLAGS_fdexPropCanPut: FDEX_PROP_FLAGS = 4
FDEX_PROP_FLAGS_fdexPropCannotPut: FDEX_PROP_FLAGS = 8
FDEX_PROP_FLAGS_fdexPropCanPutRef: FDEX_PROP_FLAGS = 16
FDEX_PROP_FLAGS_fdexPropCannotPutRef: FDEX_PROP_FLAGS = 32
FDEX_PROP_FLAGS_fdexPropNoSideEffects: FDEX_PROP_FLAGS = 64
FDEX_PROP_FLAGS_fdexPropDynamicType: FDEX_PROP_FLAGS = 128
FDEX_PROP_FLAGS_fdexPropCanCall: FDEX_PROP_FLAGS = 256
FDEX_PROP_FLAGS_fdexPropCannotCall: FDEX_PROP_FLAGS = 512
FDEX_PROP_FLAGS_fdexPropCanConstruct: FDEX_PROP_FLAGS = 1024
FDEX_PROP_FLAGS_fdexPropCannotConstruct: FDEX_PROP_FLAGS = 2048
FDEX_PROP_FLAGS_fdexPropCanSourceEvents: FDEX_PROP_FLAGS = 4096
FDEX_PROP_FLAGS_fdexPropCannotSourceEvents: FDEX_PROP_FLAGS = 8192
class FONTDESC(Structure):
    cbSizeofstruct: UInt32
    lpstrName: Windows.Win32.Foundation.PWSTR
    cySize: Windows.Win32.System.Com.CY
    sWeight: Int16
    sCharset: Int16
    fItalic: Windows.Win32.Foundation.BOOL
    fUnderline: Windows.Win32.Foundation.BOOL
    fStrikethrough: Windows.Win32.Foundation.BOOL
GUIDKIND = Int32
GUIDKIND_DEFAULT_SOURCE_DISP_IID: GUIDKIND = 1
HITRESULT = Int32
HITRESULT_OUTSIDE: HITRESULT = 0
HITRESULT_TRANSPARENT: HITRESULT = 1
HITRESULT_CLOSE: HITRESULT = 2
HITRESULT_HIT: HITRESULT = 3
class IAdviseSinkEx(c_void_p):
    extends: Windows.Win32.System.Com.IAdviseSink
    Guid = Guid('3af24290-0c96-11ce-a0-cf-00-aa-00-60-0a-b8')
    @commethod(8)
    def OnViewStatusChange(dwViewStatus: UInt32) -> Void: ...
class ICanHandleException(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c5598e60-b307-11d1-b2-7d-00-60-08-c3-fb-fb')
    @commethod(3)
    def CanHandleException(pExcepInfo: POINTER(Windows.Win32.System.Com.EXCEPINFO_head), pvar: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IClassFactory2(c_void_p):
    extends: Windows.Win32.System.Com.IClassFactory
    Guid = Guid('b196b28f-bab4-101a-b6-9c-00-aa-00-34-1d-07')
    @commethod(5)
    def GetLicInfo(pLicInfo: POINTER(Windows.Win32.System.Ole.LICINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RequestLicKey(dwReserved: UInt32, pBstrKey: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateInstanceLic(pUnkOuter: Windows.Win32.System.Com.IUnknown_head, pUnkReserved: Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), bstrKey: Windows.Win32.Foundation.BSTR, ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IContinue(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0000012a-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def FContinue() -> Windows.Win32.Foundation.HRESULT: ...
class IContinueCallback(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b722bcca-4e68-101b-a2-bc-00-aa-00-40-47-70')
    @commethod(3)
    def FContinue() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FContinuePrinting(nCntPrinted: Int32, nCurPage: Int32, pwszPrintStatus: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ICreateErrorInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('22f03340-547d-101b-8e-65-08-00-2b-2b-d1-19')
    @commethod(3)
    def SetGUID(rguid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetSource(szSource: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetDescription(szDescription: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetHelpFile(szHelpFile: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetHelpContext(dwHelpContext: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ICreateTypeInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('00020405-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def SetGuid(guid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetTypeFlags(uTypeFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetDocString(pStrDoc: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetHelpContext(dwHelpContext: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetVersion(wMajorVerNum: UInt16, wMinorVerNum: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AddRefTypeInfo(pTInfo: Windows.Win32.System.Com.ITypeInfo_head, phRefType: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddFuncDesc(index: UInt32, pFuncDesc: POINTER(Windows.Win32.System.Com.FUNCDESC_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def AddImplType(index: UInt32, hRefType: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetImplTypeFlags(index: UInt32, implTypeFlags: Windows.Win32.System.Com.IMPLTYPEFLAGS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetAlignment(cbAlignment: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetSchema(pStrSchema: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def AddVarDesc(index: UInt32, pVarDesc: POINTER(Windows.Win32.System.Com.VARDESC_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetFuncAndParamNames(index: UInt32, rgszNames: POINTER(Windows.Win32.Foundation.PWSTR), cNames: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetVarName(index: UInt32, szName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetTypeDescAlias(pTDescAlias: POINTER(Windows.Win32.System.Com.TYPEDESC_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def DefineFuncAsDllEntry(index: UInt32, szDllName: Windows.Win32.Foundation.PWSTR, szProcName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetFuncDocString(index: UInt32, szDocString: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetVarDocString(index: UInt32, szDocString: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetFuncHelpContext(index: UInt32, dwHelpContext: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetVarHelpContext(index: UInt32, dwHelpContext: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetMops(index: UInt32, bstrMops: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetTypeIdldesc(pIdlDesc: POINTER(Windows.Win32.System.Com.IDLDESC_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def LayOut() -> Windows.Win32.Foundation.HRESULT: ...
class ICreateTypeInfo2(c_void_p):
    extends: Windows.Win32.System.Ole.ICreateTypeInfo
    Guid = Guid('0002040e-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(26)
    def DeleteFuncDesc(index: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def DeleteFuncDescByMemId(memid: Int32, invKind: Windows.Win32.System.Com.INVOKEKIND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def DeleteVarDesc(index: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def DeleteVarDescByMemId(memid: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def DeleteImplType(index: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def SetCustData(guid: POINTER(Guid), pVarVal: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def SetFuncCustData(index: UInt32, guid: POINTER(Guid), pVarVal: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def SetParamCustData(indexFunc: UInt32, indexParam: UInt32, guid: POINTER(Guid), pVarVal: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def SetVarCustData(index: UInt32, guid: POINTER(Guid), pVarVal: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def SetImplTypeCustData(index: UInt32, guid: POINTER(Guid), pVarVal: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def SetHelpStringContext(dwHelpStringContext: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def SetFuncHelpStringContext(index: UInt32, dwHelpStringContext: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def SetVarHelpStringContext(index: UInt32, dwHelpStringContext: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def Invalidate() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def SetName(szName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ICreateTypeLib(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('00020406-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def CreateTypeInfo(szName: Windows.Win32.Foundation.PWSTR, tkind: Windows.Win32.System.Com.TYPEKIND, ppCTInfo: POINTER(Windows.Win32.System.Ole.ICreateTypeInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetName(szName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetVersion(wMajorVerNum: UInt16, wMinorVerNum: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetGuid(guid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetDocString(szDoc: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetHelpFileName(szHelpFileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetHelpContext(dwHelpContext: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetLcid(lcid: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetLibFlags(uLibFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SaveAllChanges() -> Windows.Win32.Foundation.HRESULT: ...
class ICreateTypeLib2(c_void_p):
    extends: Windows.Win32.System.Ole.ICreateTypeLib
    Guid = Guid('0002040f-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(13)
    def DeleteTypeInfo(szName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetCustData(guid: POINTER(Guid), pVarVal: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetHelpStringContext(dwHelpStringContext: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetHelpStringDll(szFileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IDispError(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a6ef9861-c720-11d0-93-37-00-a0-c9-0d-ca-a9')
    @commethod(3)
    def QueryErrorInfo(guidErrorType: Guid, ppde: POINTER(Windows.Win32.System.Ole.IDispError_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNext(ppde: POINTER(Windows.Win32.System.Ole.IDispError_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetHresult(phr: POINTER(Windows.Win32.Foundation.HRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSource(pbstrSource: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetHelpInfo(pbstrFileName: POINTER(Windows.Win32.Foundation.BSTR), pdwContext: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDescription(pbstrDescription: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IDispatchEx(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('a6ef9860-c720-11d0-93-37-00-a0-c9-0d-ca-a9')
    @commethod(7)
    def GetDispID(bstrName: Windows.Win32.Foundation.BSTR, grfdex: UInt32, pid: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def InvokeEx(id: Int32, lcid: UInt32, wFlags: UInt16, pdp: POINTER(Windows.Win32.System.Com.DISPPARAMS_head), pvarRes: POINTER(Windows.Win32.System.Com.VARIANT_head), pei: POINTER(Windows.Win32.System.Com.EXCEPINFO_head), pspCaller: Windows.Win32.System.Com.IServiceProvider_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def DeleteMemberByName(bstrName: Windows.Win32.Foundation.BSTR, grfdex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def DeleteMemberByDispID(id: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetMemberProperties(id: Int32, grfdexFetch: UInt32, pgrfdex: POINTER(Windows.Win32.System.Ole.FDEX_PROP_FLAGS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetMemberName(id: Int32, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetNextDispID(grfdex: UInt32, id: Int32, pid: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetNameSpaceParent(ppunk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDropSource(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('00000121-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def QueryContinueDrag(fEscapePressed: Windows.Win32.Foundation.BOOL, grfKeyState: Windows.Win32.System.SystemServices.MODIFIERKEYS_FLAGS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GiveFeedback(dwEffect: Windows.Win32.System.Ole.DROPEFFECT) -> Windows.Win32.Foundation.HRESULT: ...
class IDropSourceNotify(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0000012b-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def DragEnterTarget(hwndTarget: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DragLeaveTarget() -> Windows.Win32.Foundation.HRESULT: ...
class IDropTarget(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('00000122-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def DragEnter(pDataObj: Windows.Win32.System.Com.IDataObject_head, grfKeyState: Windows.Win32.System.SystemServices.MODIFIERKEYS_FLAGS, pt: Windows.Win32.Foundation.POINTL, pdwEffect: POINTER(Windows.Win32.System.Ole.DROPEFFECT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DragOver(grfKeyState: Windows.Win32.System.SystemServices.MODIFIERKEYS_FLAGS, pt: Windows.Win32.Foundation.POINTL, pdwEffect: POINTER(Windows.Win32.System.Ole.DROPEFFECT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DragLeave() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Drop(pDataObj: Windows.Win32.System.Com.IDataObject_head, grfKeyState: Windows.Win32.System.SystemServices.MODIFIERKEYS_FLAGS, pt: Windows.Win32.Foundation.POINTL, pdwEffect: POINTER(Windows.Win32.System.Ole.DROPEFFECT)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnterpriseDropTarget(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('390e3878-fd55-4e18-81-9d-46-82-08-1c-0c-fd')
    @commethod(3)
    def SetDropSourceEnterpriseId(identity: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsEvaluatingEdpPolicy(value: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumOLEVERB(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('00000104-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(Windows.Win32.System.Ole.OLEVERB_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(Windows.Win32.System.Ole.IEnumOLEVERB_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumOleDocumentViews(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b722bcc8-4e68-101b-a2-bc-00-aa-00-40-47-70')
    @commethod(3)
    def Next(cViews: UInt32, rgpView: POINTER(Windows.Win32.System.Ole.IOleDocumentView_head), pcFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(cViews: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(Windows.Win32.System.Ole.IEnumOleDocumentViews_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumOleUndoUnits(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b3e7c340-ef97-11ce-9b-c9-00-aa-00-60-8e-01')
    @commethod(3)
    def Next(cElt: UInt32, rgElt: POINTER(Windows.Win32.System.Ole.IOleUndoUnit_head), pcEltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(cElt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(Windows.Win32.System.Ole.IEnumOleUndoUnits_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumVARIANT(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('00020404-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Next(celt: UInt32, rgVar: POINTER(Windows.Win32.System.Com.VARIANT_head), pCeltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppEnum: POINTER(Windows.Win32.System.Ole.IEnumVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFont(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('bef6e002-a874-101a-8b-ba-00-aa-00-30-0c-ab')
    @commethod(3)
    def get_Name(pName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_Name(name: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_Size(pSize: POINTER(Windows.Win32.System.Com.CY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_Size(size: Windows.Win32.System.Com.CY) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Bold(pBold: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Bold(bold: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Italic(pItalic: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Italic(italic: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Underline(pUnderline: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Underline(underline: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Strikethrough(pStrikethrough: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Strikethrough(strikethrough: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Weight(pWeight: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Weight(weight: Int16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Charset(pCharset: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_Charset(charset: Int16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_hFont(phFont: POINTER(Windows.Win32.Graphics.Gdi.HFONT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def Clone(ppFont: POINTER(Windows.Win32.System.Ole.IFont_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def IsEqual(pFontOther: Windows.Win32.System.Ole.IFont_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetRatio(cyLogical: Int32, cyHimetric: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def QueryTextMetrics(pTM: POINTER(Windows.Win32.Graphics.Gdi.TEXTMETRICW_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def AddRefHfont(hFont: Windows.Win32.Graphics.Gdi.HFONT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def ReleaseHfont(hFont: Windows.Win32.Graphics.Gdi.HFONT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def SetHdc(hDC: Windows.Win32.Graphics.Gdi.HDC) -> Windows.Win32.Foundation.HRESULT: ...
class IFontDisp(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('bef6e003-a874-101a-8b-ba-00-aa-00-30-0c-ab')
class IFontEventsDisp(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('4ef6100a-af88-11d0-98-46-00-c0-4f-c2-99-93')
IGNOREMIME = Int32
IGNOREMIME_PROMPT: IGNOREMIME = 1
IGNOREMIME_TEXT: IGNOREMIME = 2
class IGetOleObject(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8a701da0-4feb-101b-a8-2e-08-00-2b-2b-23-37')
    @commethod(3)
    def GetOleObject(riid: POINTER(Guid), ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IGetVBAObject(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('91733a60-3f4c-101b-a3-f6-00-aa-00-34-e4-e9')
    @commethod(3)
    def GetObject(riid: POINTER(Guid), ppvObj: POINTER(c_void_p), dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
INSERT_OBJECT_FLAGS = UInt32
IOF_SHOWHELP: INSERT_OBJECT_FLAGS = 1
IOF_SELECTCREATENEW: INSERT_OBJECT_FLAGS = 2
IOF_SELECTCREATEFROMFILE: INSERT_OBJECT_FLAGS = 4
IOF_CHECKLINK: INSERT_OBJECT_FLAGS = 8
IOF_CHECKDISPLAYASICON: INSERT_OBJECT_FLAGS = 16
IOF_CREATENEWOBJECT: INSERT_OBJECT_FLAGS = 32
IOF_CREATEFILEOBJECT: INSERT_OBJECT_FLAGS = 64
IOF_CREATELINKOBJECT: INSERT_OBJECT_FLAGS = 128
IOF_DISABLELINK: INSERT_OBJECT_FLAGS = 256
IOF_VERIFYSERVERSEXIST: INSERT_OBJECT_FLAGS = 512
IOF_DISABLEDISPLAYASICON: INSERT_OBJECT_FLAGS = 1024
IOF_HIDECHANGEICON: INSERT_OBJECT_FLAGS = 2048
IOF_SHOWINSERTCONTROL: INSERT_OBJECT_FLAGS = 4096
IOF_SELECTCREATECONTROL: INSERT_OBJECT_FLAGS = 8192
class INTERFACEDATA(Structure):
    pmethdata: POINTER(Windows.Win32.System.Ole.METHODDATA_head)
    cMembers: UInt32
class IObjectIdentity(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ca04b7e6-0d21-11d1-8c-c5-00-c0-4f-c2-b0-85')
    @commethod(3)
    def IsEqualObject(punk: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IObjectWithSite(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('fc4801a3-2ba9-11cf-a2-29-00-aa-00-3d-73-52')
    @commethod(3)
    def SetSite(pUnkSite: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSite(riid: POINTER(Guid), ppvSite: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IOleAdviseHolder(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('00000111-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Advise(pAdvise: Windows.Win32.System.Com.IAdviseSink_head, pdwConnection: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unadvise(dwConnection: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumAdvise(ppenumAdvise: POINTER(Windows.Win32.System.Com.IEnumSTATDATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SendOnRename(pmk: Windows.Win32.System.Com.IMoniker_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SendOnSave() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SendOnClose() -> Windows.Win32.Foundation.HRESULT: ...
class IOleCache(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0000011e-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Cache(pformatetc: POINTER(Windows.Win32.System.Com.FORMATETC_head), advf: UInt32, pdwConnection: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Uncache(dwConnection: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumCache(ppenumSTATDATA: POINTER(Windows.Win32.System.Com.IEnumSTATDATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def InitCache(pDataObject: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetData(pformatetc: POINTER(Windows.Win32.System.Com.FORMATETC_head), pmedium: POINTER(Windows.Win32.System.Com.STGMEDIUM_head), fRelease: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IOleCache2(c_void_p):
    extends: Windows.Win32.System.Ole.IOleCache
    Guid = Guid('00000128-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(8)
    def UpdateCache(pDataObject: Windows.Win32.System.Com.IDataObject_head, grfUpdf: Windows.Win32.System.Ole.UPDFCACHE_FLAGS, pReserved: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def DiscardCache(dwDiscardOptions: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IOleCacheControl(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('00000129-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def OnRun(pDataObject: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnStop() -> Windows.Win32.Foundation.HRESULT: ...
class IOleClientSite(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('00000118-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def SaveObject() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMoniker(dwAssign: Windows.Win32.System.Ole.OLEGETMONIKER, dwWhichMoniker: Windows.Win32.System.Ole.OLEWHICHMK, ppmk: POINTER(Windows.Win32.System.Com.IMoniker_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetContainer(ppContainer: POINTER(Windows.Win32.System.Ole.IOleContainer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ShowObject() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnShowWindow(fShow: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RequestNewObjectLayout() -> Windows.Win32.Foundation.HRESULT: ...
class IOleCommandTarget(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b722bccb-4e68-101b-a2-bc-00-aa-00-40-47-70')
    @commethod(3)
    def QueryStatus(pguidCmdGroup: POINTER(Guid), cCmds: UInt32, prgCmds: POINTER(Windows.Win32.System.Ole.OLECMD_head), pCmdText: POINTER(Windows.Win32.System.Ole.OLECMDTEXT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Exec(pguidCmdGroup: POINTER(Guid), nCmdID: UInt32, nCmdexecopt: UInt32, pvaIn: POINTER(Windows.Win32.System.Com.VARIANT_head), pvaOut: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOleContainer(c_void_p):
    extends: Windows.Win32.System.Ole.IParseDisplayName
    Guid = Guid('0000011b-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(4)
    def EnumObjects(grfFlags: Windows.Win32.System.Ole.OLECONTF, ppenum: POINTER(Windows.Win32.System.Com.IEnumUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def LockContainer(fLock: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IOleControl(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b196b288-bab4-101a-b6-9c-00-aa-00-34-1d-07')
    @commethod(3)
    def GetControlInfo(pCI: POINTER(Windows.Win32.System.Ole.CONTROLINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnMnemonic(pMsg: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnAmbientPropertyChange(dispID: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FreezeEvents(bFreeze: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IOleControlSite(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b196b289-bab4-101a-b6-9c-00-aa-00-34-1d-07')
    @commethod(3)
    def OnControlInfoChanged() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LockInPlaceActive(fLock: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetExtendedControl(ppDisp: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def TransformCoords(pPtlHimetric: POINTER(Windows.Win32.Foundation.POINTL_head), pPtfContainer: POINTER(Windows.Win32.System.Ole.POINTF_head), dwFlags: Windows.Win32.System.Ole.XFORMCOORDS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def TranslateAccelerator(pMsg: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head), grfModifiers: Windows.Win32.System.Ole.KEYMODIFIERS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnFocus(fGotFocus: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ShowPropertyFrame() -> Windows.Win32.Foundation.HRESULT: ...
class IOleDocument(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b722bcc5-4e68-101b-a2-bc-00-aa-00-40-47-70')
    @commethod(3)
    def CreateView(pIPSite: Windows.Win32.System.Ole.IOleInPlaceSite_head, pstm: Windows.Win32.System.Com.IStream_head, dwReserved: UInt32, ppView: POINTER(Windows.Win32.System.Ole.IOleDocumentView_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDocMiscStatus(pdwStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumViews(ppEnum: POINTER(Windows.Win32.System.Ole.IEnumOleDocumentViews_head), ppView: POINTER(Windows.Win32.System.Ole.IOleDocumentView_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOleDocumentSite(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b722bcc7-4e68-101b-a2-bc-00-aa-00-40-47-70')
    @commethod(3)
    def ActivateMe(pViewToActivate: Windows.Win32.System.Ole.IOleDocumentView_head) -> Windows.Win32.Foundation.HRESULT: ...
class IOleDocumentView(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b722bcc6-4e68-101b-a2-bc-00-aa-00-40-47-70')
    @commethod(3)
    def SetInPlaceSite(pIPSite: Windows.Win32.System.Ole.IOleInPlaceSite_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInPlaceSite(ppIPSite: POINTER(Windows.Win32.System.Ole.IOleInPlaceSite_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDocument(ppunk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetRect(prcView: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRect(prcView: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetRectComplex(prcView: POINTER(Windows.Win32.Foundation.RECT_head), prcHScroll: POINTER(Windows.Win32.Foundation.RECT_head), prcVScroll: POINTER(Windows.Win32.Foundation.RECT_head), prcSizeBox: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Show(fShow: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def UIActivate(fUIActivate: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Open() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def CloseView(dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SaveViewState(pstm: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def ApplyViewState(pstm: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Clone(pIPSiteNew: Windows.Win32.System.Ole.IOleInPlaceSite_head, ppViewNew: POINTER(Windows.Win32.System.Ole.IOleDocumentView_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOleInPlaceActiveObject(c_void_p):
    extends: Windows.Win32.System.Ole.IOleWindow
    Guid = Guid('00000117-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(5)
    def TranslateAccelerator(lpmsg: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnFrameWindowActivate(fActivate: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnDocWindowActivate(fActivate: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ResizeBorder(prcBorder: POINTER(Windows.Win32.Foundation.RECT_head), pUIWindow: Windows.Win32.System.Ole.IOleInPlaceUIWindow_head, fFrameWindow: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnableModeless(fEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IOleInPlaceFrame(c_void_p):
    extends: Windows.Win32.System.Ole.IOleInPlaceUIWindow
    Guid = Guid('00000116-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(9)
    def InsertMenus(hmenuShared: Windows.Win32.UI.WindowsAndMessaging.HMENU, lpMenuWidths: POINTER(Windows.Win32.System.Ole.OLEMENUGROUPWIDTHS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetMenu(hmenuShared: Windows.Win32.UI.WindowsAndMessaging.HMENU, holemenu: IntPtr, hwndActiveObject: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RemoveMenus(hmenuShared: Windows.Win32.UI.WindowsAndMessaging.HMENU) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetStatusText(pszStatusText: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def EnableModeless(fEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def TranslateAccelerator(lpmsg: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head), wID: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
class IOleInPlaceObject(c_void_p):
    extends: Windows.Win32.System.Ole.IOleWindow
    Guid = Guid('00000113-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(5)
    def InPlaceDeactivate() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def UIDeactivate() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetObjectRects(lprcPosRect: POINTER(Windows.Win32.Foundation.RECT_head), lprcClipRect: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ReactivateAndUndo() -> Windows.Win32.Foundation.HRESULT: ...
class IOleInPlaceObjectWindowless(c_void_p):
    extends: Windows.Win32.System.Ole.IOleInPlaceObject
    Guid = Guid('1c2056cc-5ef4-101b-8b-c8-00-aa-00-3e-3b-29')
    @commethod(9)
    def OnWindowMessage(msg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM, plResult: POINTER(Windows.Win32.Foundation.LRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDropTarget(ppDropTarget: POINTER(Windows.Win32.System.Ole.IDropTarget_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOleInPlaceSite(c_void_p):
    extends: Windows.Win32.System.Ole.IOleWindow
    Guid = Guid('00000119-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(5)
    def CanInPlaceActivate() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnInPlaceActivate() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnUIActivate() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetWindowContext(ppFrame: POINTER(Windows.Win32.System.Ole.IOleInPlaceFrame_head), ppDoc: POINTER(Windows.Win32.System.Ole.IOleInPlaceUIWindow_head), lprcPosRect: POINTER(Windows.Win32.Foundation.RECT_head), lprcClipRect: POINTER(Windows.Win32.Foundation.RECT_head), lpFrameInfo: POINTER(Windows.Win32.System.Ole.OLEINPLACEFRAMEINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Scroll(scrollExtant: Windows.Win32.Foundation.SIZE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OnUIDeactivate(fUndoable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def OnInPlaceDeactivate() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def DiscardUndoState() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def DeactivateAndUndo() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def OnPosRectChange(lprcPosRect: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOleInPlaceSiteEx(c_void_p):
    extends: Windows.Win32.System.Ole.IOleInPlaceSite
    Guid = Guid('9c2cad80-3424-11cf-b6-70-00-aa-00-4c-d6-d8')
    @commethod(15)
    def OnInPlaceActivateEx(pfNoRedraw: POINTER(Windows.Win32.Foundation.BOOL), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def OnInPlaceDeactivateEx(fNoRedraw: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def RequestUIActivate() -> Windows.Win32.Foundation.HRESULT: ...
class IOleInPlaceSiteWindowless(c_void_p):
    extends: Windows.Win32.System.Ole.IOleInPlaceSiteEx
    Guid = Guid('922eada0-3424-11cf-b6-70-00-aa-00-4c-d6-d8')
    @commethod(18)
    def CanWindowlessActivate() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetCapture() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetCapture(fCapture: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetFocus() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetFocus(fFocus: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetDC(pRect: POINTER(Windows.Win32.Foundation.RECT_head), grfFlags: UInt32, phDC: POINTER(Windows.Win32.Graphics.Gdi.HDC)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def ReleaseDC(hDC: Windows.Win32.Graphics.Gdi.HDC) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def InvalidateRect(pRect: POINTER(Windows.Win32.Foundation.RECT_head), fErase: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def InvalidateRgn(hRGN: Windows.Win32.Graphics.Gdi.HRGN, fErase: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def ScrollRect(dx: Int32, dy: Int32, pRectScroll: POINTER(Windows.Win32.Foundation.RECT_head), pRectClip: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def AdjustRect(prc: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def OnDefWindowMessage(msg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM, plResult: POINTER(Windows.Win32.Foundation.LRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
class IOleInPlaceUIWindow(c_void_p):
    extends: Windows.Win32.System.Ole.IOleWindow
    Guid = Guid('00000115-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(5)
    def GetBorder(lprectBorder: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RequestBorderSpace(pborderwidths: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetBorderSpace(pborderwidths: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetActiveObject(pActiveObject: Windows.Win32.System.Ole.IOleInPlaceActiveObject_head, pszObjName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IOleItemContainer(c_void_p):
    extends: Windows.Win32.System.Ole.IOleContainer
    Guid = Guid('0000011c-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(6)
    def GetObject(pszItem: Windows.Win32.Foundation.PWSTR, dwSpeedNeeded: UInt32, pbc: Windows.Win32.System.Com.IBindCtx_head, riid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetObjectStorage(pszItem: Windows.Win32.Foundation.PWSTR, pbc: Windows.Win32.System.Com.IBindCtx_head, riid: POINTER(Guid), ppvStorage: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsRunning(pszItem: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IOleLink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0000011d-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def SetUpdateOptions(dwUpdateOpt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetUpdateOptions(pdwUpdateOpt: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetSourceMoniker(pmk: Windows.Win32.System.Com.IMoniker_head, rclsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSourceMoniker(ppmk: POINTER(Windows.Win32.System.Com.IMoniker_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetSourceDisplayName(pszStatusText: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSourceDisplayName(ppszDisplayName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def BindToSource(bindflags: UInt32, pbc: Windows.Win32.System.Com.IBindCtx_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def BindIfRunning() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetBoundSource(ppunk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def UnbindSource() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Update(pbc: Windows.Win32.System.Com.IBindCtx_head) -> Windows.Win32.Foundation.HRESULT: ...
class IOleObject(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('00000112-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def SetClientSite(pClientSite: Windows.Win32.System.Ole.IOleClientSite_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetClientSite(ppClientSite: POINTER(Windows.Win32.System.Ole.IOleClientSite_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetHostNames(szContainerApp: Windows.Win32.Foundation.PWSTR, szContainerObj: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Close(dwSaveOption: Windows.Win32.System.Ole.OLECLOSE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetMoniker(dwWhichMoniker: Windows.Win32.System.Ole.OLEWHICHMK, pmk: Windows.Win32.System.Com.IMoniker_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetMoniker(dwAssign: Windows.Win32.System.Ole.OLEGETMONIKER, dwWhichMoniker: Windows.Win32.System.Ole.OLEWHICHMK, ppmk: POINTER(Windows.Win32.System.Com.IMoniker_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def InitFromData(pDataObject: Windows.Win32.System.Com.IDataObject_head, fCreation: Windows.Win32.Foundation.BOOL, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetClipboardData(dwReserved: UInt32, ppDataObject: POINTER(Windows.Win32.System.Com.IDataObject_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def DoVerb(iVerb: Int32, lpmsg: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head), pActiveSite: Windows.Win32.System.Ole.IOleClientSite_head, lindex: Int32, hwndParent: Windows.Win32.Foundation.HWND, lprcPosRect: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def EnumVerbs(ppEnumOleVerb: POINTER(Windows.Win32.System.Ole.IEnumOLEVERB_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Update() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def IsUpToDate() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetUserClassID(pClsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetUserType(dwFormOfType: Windows.Win32.System.Ole.USERCLASSTYPE, pszUserType: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetExtent(dwDrawAspect: Windows.Win32.System.Com.DVASPECT, psizel: POINTER(Windows.Win32.Foundation.SIZE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetExtent(dwDrawAspect: Windows.Win32.System.Com.DVASPECT, psizel: POINTER(Windows.Win32.Foundation.SIZE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Advise(pAdvSink: Windows.Win32.System.Com.IAdviseSink_head, pdwConnection: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def Unadvise(dwConnection: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def EnumAdvise(ppenumAdvise: POINTER(Windows.Win32.System.Com.IEnumSTATDATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetMiscStatus(dwAspect: Windows.Win32.System.Com.DVASPECT, pdwStatus: POINTER(Windows.Win32.System.Ole.OLEMISC)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetColorScheme(pLogpal: POINTER(Windows.Win32.Graphics.Gdi.LOGPALETTE_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOleParentUndoUnit(c_void_p):
    extends: Windows.Win32.System.Ole.IOleUndoUnit
    Guid = Guid('a1faf330-ef97-11ce-9b-c9-00-aa-00-60-8e-01')
    @commethod(7)
    def Open(pPUU: Windows.Win32.System.Ole.IOleParentUndoUnit_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Close(pPUU: Windows.Win32.System.Ole.IOleParentUndoUnit_head, fCommit: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Add(pUU: Windows.Win32.System.Ole.IOleUndoUnit_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def FindUnit(pUU: Windows.Win32.System.Ole.IOleUndoUnit_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetParentState(pdwState: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IOleUILinkContainerA(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def GetNextLink(dwLink: UInt32) -> UInt32: ...
    @commethod(4)
    def SetLinkUpdateOptions(dwLink: UInt32, dwUpdateOpt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLinkUpdateOptions(dwLink: UInt32, lpdwUpdateOpt: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetLinkSource(dwLink: UInt32, lpszDisplayName: Windows.Win32.Foundation.PSTR, lenFileName: UInt32, pchEaten: POINTER(UInt32), fValidateSource: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetLinkSource(dwLink: UInt32, lplpszDisplayName: POINTER(Windows.Win32.Foundation.PSTR), lplenFileName: POINTER(UInt32), lplpszFullLinkType: POINTER(Windows.Win32.Foundation.PSTR), lplpszShortLinkType: POINTER(Windows.Win32.Foundation.PSTR), lpfSourceAvailable: POINTER(Windows.Win32.Foundation.BOOL), lpfIsSelected: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OpenLinkSource(dwLink: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def UpdateLink(dwLink: UInt32, fErrorMessage: Windows.Win32.Foundation.BOOL, fReserved: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CancelLink(dwLink: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IOleUILinkContainerW(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def GetNextLink(dwLink: UInt32) -> UInt32: ...
    @commethod(4)
    def SetLinkUpdateOptions(dwLink: UInt32, dwUpdateOpt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLinkUpdateOptions(dwLink: UInt32, lpdwUpdateOpt: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetLinkSource(dwLink: UInt32, lpszDisplayName: Windows.Win32.Foundation.PWSTR, lenFileName: UInt32, pchEaten: POINTER(UInt32), fValidateSource: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetLinkSource(dwLink: UInt32, lplpszDisplayName: POINTER(Windows.Win32.Foundation.PWSTR), lplenFileName: POINTER(UInt32), lplpszFullLinkType: POINTER(Windows.Win32.Foundation.PWSTR), lplpszShortLinkType: POINTER(Windows.Win32.Foundation.PWSTR), lpfSourceAvailable: POINTER(Windows.Win32.Foundation.BOOL), lpfIsSelected: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OpenLinkSource(dwLink: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def UpdateLink(dwLink: UInt32, fErrorMessage: Windows.Win32.Foundation.BOOL, fReserved: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CancelLink(dwLink: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IOleUILinkInfoA(c_void_p):
    extends: Windows.Win32.System.Ole.IOleUILinkContainerA
    @commethod(11)
    def GetLastUpdate(dwLink: UInt32, lpLastUpdate: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOleUILinkInfoW(c_void_p):
    extends: Windows.Win32.System.Ole.IOleUILinkContainerW
    @commethod(11)
    def GetLastUpdate(dwLink: UInt32, lpLastUpdate: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOleUIObjInfoA(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def GetObjectInfo(dwObject: UInt32, lpdwObjSize: POINTER(UInt32), lplpszLabel: POINTER(Windows.Win32.Foundation.PSTR), lplpszType: POINTER(Windows.Win32.Foundation.PSTR), lplpszShortType: POINTER(Windows.Win32.Foundation.PSTR), lplpszLocation: POINTER(Windows.Win32.Foundation.PSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetConvertInfo(dwObject: UInt32, lpClassID: POINTER(Guid), lpwFormat: POINTER(UInt16), lpConvertDefaultClassID: POINTER(Guid), lplpClsidExclude: POINTER(POINTER(Guid)), lpcClsidExclude: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ConvertObject(dwObject: UInt32, clsidNew: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetViewInfo(dwObject: UInt32, phMetaPict: POINTER(Windows.Win32.Foundation.HGLOBAL), pdvAspect: POINTER(UInt32), pnCurrentScale: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetViewInfo(dwObject: UInt32, hMetaPict: Windows.Win32.Foundation.HGLOBAL, dvAspect: UInt32, nCurrentScale: Int32, bRelativeToOrig: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IOleUIObjInfoW(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def GetObjectInfo(dwObject: UInt32, lpdwObjSize: POINTER(UInt32), lplpszLabel: POINTER(Windows.Win32.Foundation.PWSTR), lplpszType: POINTER(Windows.Win32.Foundation.PWSTR), lplpszShortType: POINTER(Windows.Win32.Foundation.PWSTR), lplpszLocation: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetConvertInfo(dwObject: UInt32, lpClassID: POINTER(Guid), lpwFormat: POINTER(UInt16), lpConvertDefaultClassID: POINTER(Guid), lplpClsidExclude: POINTER(POINTER(Guid)), lpcClsidExclude: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ConvertObject(dwObject: UInt32, clsidNew: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetViewInfo(dwObject: UInt32, phMetaPict: POINTER(Windows.Win32.Foundation.HGLOBAL), pdvAspect: POINTER(UInt32), pnCurrentScale: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetViewInfo(dwObject: UInt32, hMetaPict: Windows.Win32.Foundation.HGLOBAL, dvAspect: UInt32, nCurrentScale: Int32, bRelativeToOrig: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IOleUndoManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d001f200-ef97-11ce-9b-c9-00-aa-00-60-8e-01')
    @commethod(3)
    def Open(pPUU: Windows.Win32.System.Ole.IOleParentUndoUnit_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(pPUU: Windows.Win32.System.Ole.IOleParentUndoUnit_head, fCommit: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Add(pUU: Windows.Win32.System.Ole.IOleUndoUnit_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetOpenParentState(pdwState: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DiscardFrom(pUU: Windows.Win32.System.Ole.IOleUndoUnit_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def UndoTo(pUU: Windows.Win32.System.Ole.IOleUndoUnit_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RedoTo(pUU: Windows.Win32.System.Ole.IOleUndoUnit_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EnumUndoable(ppEnum: POINTER(Windows.Win32.System.Ole.IEnumOleUndoUnits_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EnumRedoable(ppEnum: POINTER(Windows.Win32.System.Ole.IEnumOleUndoUnits_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetLastUndoDescription(pBstr: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetLastRedoDescription(pBstr: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Enable(fEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IOleUndoUnit(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('894ad3b0-ef97-11ce-9b-c9-00-aa-00-60-8e-01')
    @commethod(3)
    def Do(pUndoManager: Windows.Win32.System.Ole.IOleUndoManager_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDescription(pBstr: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetUnitType(pClsid: POINTER(Guid), plID: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnNextAdd() -> Windows.Win32.Foundation.HRESULT: ...
class IOleWindow(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('00000114-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def GetWindow(phwnd: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ContextSensitiveHelp(fEnterMode: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IParseDisplayName(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0000011a-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def ParseDisplayName(pbc: Windows.Win32.System.Com.IBindCtx_head, pszDisplayName: Windows.Win32.Foundation.PWSTR, pchEaten: POINTER(UInt32), ppmkOut: POINTER(Windows.Win32.System.Com.IMoniker_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPerPropertyBrowsing(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('376bd3aa-3845-101b-84-ed-08-00-2b-2e-c7-13')
    @commethod(3)
    def GetDisplayString(dispID: Int32, pBstr: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MapPropertyToPage(dispID: Int32, pClsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPredefinedStrings(dispID: Int32, pCaStringsOut: POINTER(Windows.Win32.System.Ole.CALPOLESTR_head), pCaCookiesOut: POINTER(Windows.Win32.System.Ole.CADWORD_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPredefinedValue(dispID: Int32, dwCookie: UInt32, pVarOut: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPersistPropertyBag(c_void_p):
    extends: Windows.Win32.System.Com.IPersist
    Guid = Guid('37d84f60-42cb-11ce-81-35-00-aa-00-4b-b8-51')
    @commethod(4)
    def InitNew() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Load(pPropBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, pErrorLog: Windows.Win32.System.Com.IErrorLog_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Save(pPropBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, fClearDirty: Windows.Win32.Foundation.BOOL, fSaveAllProperties: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IPersistPropertyBag2(c_void_p):
    extends: Windows.Win32.System.Com.IPersist
    Guid = Guid('22f55881-280b-11d0-a8-a9-00-a0-c9-0c-20-04')
    @commethod(4)
    def InitNew() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Load(pPropBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag2_head, pErrLog: Windows.Win32.System.Com.IErrorLog_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Save(pPropBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag2_head, fClearDirty: Windows.Win32.Foundation.BOOL, fSaveAllProperties: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsDirty() -> Windows.Win32.Foundation.HRESULT: ...
class IPicture(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7bf80980-bf32-101a-8b-bb-00-aa-00-30-0c-ab')
    @commethod(3)
    def get_Handle(pHandle: POINTER(Windows.Win32.System.Ole.OLE_HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_hPal(phPal: POINTER(Windows.Win32.System.Ole.OLE_HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_Type(pType: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Width(pWidth: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Height(pHeight: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Render(hDC: Windows.Win32.Graphics.Gdi.HDC, x: Int32, y: Int32, cx: Int32, cy: Int32, xSrc: Int32, ySrc: Int32, cxSrc: Int32, cySrc: Int32, pRcWBounds: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def set_hPal(hPal: Windows.Win32.System.Ole.OLE_HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CurDC(phDC: POINTER(Windows.Win32.Graphics.Gdi.HDC)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SelectPicture(hDCIn: Windows.Win32.Graphics.Gdi.HDC, phDCOut: POINTER(Windows.Win32.Graphics.Gdi.HDC), phBmpOut: POINTER(Windows.Win32.System.Ole.OLE_HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_KeepOriginalFormat(pKeep: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_KeepOriginalFormat(keep: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def PictureChanged() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SaveAsFile(pStream: Windows.Win32.System.Com.IStream_head, fSaveMemCopy: Windows.Win32.Foundation.BOOL, pCbSize: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Attributes(pDwAttr: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IPicture2(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f5185dd8-2012-4b0b-aa-d9-f0-52-c6-bd-48-2b')
    @commethod(3)
    def get_Handle(pHandle: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_hPal(phPal: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_Type(pType: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Width(pWidth: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Height(pHeight: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Render(hDC: Windows.Win32.Graphics.Gdi.HDC, x: Int32, y: Int32, cx: Int32, cy: Int32, xSrc: Int32, ySrc: Int32, cxSrc: Int32, cySrc: Int32, pRcWBounds: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def set_hPal(hPal: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CurDC(phDC: POINTER(Windows.Win32.Graphics.Gdi.HDC)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SelectPicture(hDCIn: Windows.Win32.Graphics.Gdi.HDC, phDCOut: POINTER(Windows.Win32.Graphics.Gdi.HDC), phBmpOut: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_KeepOriginalFormat(pKeep: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_KeepOriginalFormat(keep: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def PictureChanged() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SaveAsFile(pStream: Windows.Win32.System.Com.IStream_head, fSaveMemCopy: Windows.Win32.Foundation.BOOL, pCbSize: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Attributes(pDwAttr: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IPictureDisp(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('7bf80981-bf32-101a-8b-bb-00-aa-00-30-0c-ab')
class IPointerInactive(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('55980ba0-35aa-11cf-b6-71-00-aa-00-4c-d6-d8')
    @commethod(3)
    def GetActivationPolicy(pdwPolicy: POINTER(Windows.Win32.System.Ole.POINTERINACTIVE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnInactiveMouseMove(pRectBounds: POINTER(Windows.Win32.Foundation.RECT_head), x: Int32, y: Int32, grfKeyState: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnInactiveSetCursor(pRectBounds: POINTER(Windows.Win32.Foundation.RECT_head), x: Int32, y: Int32, dwMouseMsg: UInt32, fSetAlways: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IPrint(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b722bcc9-4e68-101b-a2-bc-00-aa-00-40-47-70')
    @commethod(3)
    def SetInitialPageNum(nFirstPage: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPageInfo(pnFirstPage: POINTER(Int32), pcPages: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Print(grfFlags: UInt32, pptd: POINTER(POINTER(Windows.Win32.System.Com.DVTARGETDEVICE_head)), ppPageSet: POINTER(POINTER(Windows.Win32.System.Ole.PAGESET_head)), pstgmOptions: POINTER(Windows.Win32.System.Com.STGMEDIUM_head), pcallback: Windows.Win32.System.Ole.IContinueCallback_head, nFirstPage: Int32, pcPagesPrinted: POINTER(Int32), pnLastPage: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyNotifySink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9bfbbc02-eff1-101a-84-ed-00-aa-00-34-1d-07')
    @commethod(3)
    def OnChanged(dispID: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnRequestEdit(dispID: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyPage(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b196b28d-bab4-101a-b6-9c-00-aa-00-34-1d-07')
    @commethod(3)
    def SetPageSite(pPageSite: Windows.Win32.System.Ole.IPropertyPageSite_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Activate(hWndParent: Windows.Win32.Foundation.HWND, pRect: POINTER(Windows.Win32.Foundation.RECT_head), bModal: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Deactivate() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPageInfo(pPageInfo: POINTER(Windows.Win32.System.Ole.PROPPAGEINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetObjects(cObjects: UInt32, ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Show(nCmdShow: Windows.Win32.UI.WindowsAndMessaging.SHOW_WINDOW_CMD) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Move(pRect: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IsPageDirty() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Apply() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Help(pszHelpDir: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def TranslateAccelerator(pMsg: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyPage2(c_void_p):
    extends: Windows.Win32.System.Ole.IPropertyPage
    Guid = Guid('01e44665-24ac-101b-84-ed-08-00-2b-2e-c7-13')
    @commethod(14)
    def EditProperty(dispID: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyPageSite(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b196b28c-bab4-101a-b6-9c-00-aa-00-34-1d-07')
    @commethod(3)
    def OnStatusChange(dwFlags: Windows.Win32.System.Ole.PROPPAGESTATUS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLocaleID(pLocaleID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPageContainer(ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def TranslateAccelerator(pMsg: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IProtectFocus(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d81f90a3-8156-44f7-ad-28-5a-bb-87-00-32-74')
    @commethod(3)
    def AllowFocusChange(pfAllow: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IProtectedModeMenuServices(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('73c105ee-9dff-4a07-b8-3c-7e-ff-29-0c-26-6e')
    @commethod(3)
    def CreateMenu(phMenu: POINTER(Windows.Win32.UI.WindowsAndMessaging.HMENU)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LoadMenu(pszModuleName: Windows.Win32.Foundation.PWSTR, pszMenuName: Windows.Win32.Foundation.PWSTR, phMenu: POINTER(Windows.Win32.UI.WindowsAndMessaging.HMENU)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def LoadMenuID(pszModuleName: Windows.Win32.Foundation.PWSTR, wResourceID: UInt16, phMenu: POINTER(Windows.Win32.UI.WindowsAndMessaging.HMENU)) -> Windows.Win32.Foundation.HRESULT: ...
class IProvideClassInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b196b283-bab4-101a-b6-9c-00-aa-00-34-1d-07')
    @commethod(3)
    def GetClassInfo(ppTI: POINTER(Windows.Win32.System.Com.ITypeInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IProvideClassInfo2(c_void_p):
    extends: Windows.Win32.System.Ole.IProvideClassInfo
    Guid = Guid('a6bc3ac0-dbaa-11ce-9d-e3-00-aa-00-4b-b8-51')
    @commethod(4)
    def GetGUID(dwGuidKind: UInt32, pGUID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IProvideMultipleClassInfo(c_void_p):
    extends: Windows.Win32.System.Ole.IProvideClassInfo2
    Guid = Guid('a7aba9c1-8983-11cf-8f-20-00-80-5f-2c-d0-64')
    @commethod(5)
    def GetMultiTypeInfoCount(pcti: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetInfoOfIndex(iti: UInt32, dwFlags: Windows.Win32.System.Ole.MULTICLASSINFO_FLAGS, pptiCoClass: POINTER(Windows.Win32.System.Com.ITypeInfo_head), pdwTIFlags: POINTER(UInt32), pcdispidReserved: POINTER(UInt32), piidPrimary: POINTER(Guid), piidSource: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IProvideRuntimeContext(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('10e2414a-ec59-49d2-bc-51-5a-dd-2c-36-fe-bc')
    @commethod(3)
    def GetCurrentSourceContext(pdwContext: POINTER(UIntPtr), pfExecutingGlobalCode: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IQuickActivate(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('cf51ed10-62fe-11cf-bf-86-00-a0-c9-03-48-36')
    @commethod(3)
    def QuickActivate(pQaContainer: POINTER(Windows.Win32.System.Ole.QACONTAINER_head), pQaControl: POINTER(Windows.Win32.System.Ole.QACONTROL_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetContentExtent(pSizel: POINTER(Windows.Win32.Foundation.SIZE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetContentExtent(pSizel: POINTER(Windows.Win32.Foundation.SIZE_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRecordInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0000002f-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def RecordInit(pvNew: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RecordClear(pvExisting: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RecordCopy(pvExisting: c_void_p, pvNew: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetGuid(pguid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetName(pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSize(pcbSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetTypeInfo(ppTypeInfo: POINTER(Windows.Win32.System.Com.ITypeInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetField(pvData: c_void_p, szFieldName: Windows.Win32.Foundation.PWSTR, pvarField: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetFieldNoCopy(pvData: c_void_p, szFieldName: Windows.Win32.Foundation.PWSTR, pvarField: POINTER(Windows.Win32.System.Com.VARIANT_head), ppvDataCArray: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def PutField(wFlags: Windows.Win32.System.Com.INVOKEKIND, pvData: c_void_p, szFieldName: Windows.Win32.Foundation.PWSTR, pvarField: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def PutFieldNoCopy(wFlags: Windows.Win32.System.Com.INVOKEKIND, pvData: c_void_p, szFieldName: Windows.Win32.Foundation.PWSTR, pvarField: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetFieldNames(pcNames: POINTER(UInt32), rgBstrNames: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def IsMatchingType(pRecordInfo: Windows.Win32.System.Ole.IRecordInfo_head) -> Windows.Win32.Foundation.BOOL: ...
    @commethod(16)
    def RecordCreate() -> c_void_p: ...
    @commethod(17)
    def RecordCreateCopy(pvSource: c_void_p, ppvDest: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def RecordDestroy(pvRecord: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
class ISimpleFrameSite(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('742b0e01-14e6-101b-91-4e-00-aa-00-30-0c-ab')
    @commethod(3)
    def PreMessageFilter(hWnd: Windows.Win32.Foundation.HWND, msg: UInt32, wp: Windows.Win32.Foundation.WPARAM, lp: Windows.Win32.Foundation.LPARAM, plResult: POINTER(Windows.Win32.Foundation.LRESULT), pdwCookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PostMessageFilter(hWnd: Windows.Win32.Foundation.HWND, msg: UInt32, wp: Windows.Win32.Foundation.WPARAM, lp: Windows.Win32.Foundation.LPARAM, plResult: POINTER(Windows.Win32.Foundation.LRESULT), dwCookie: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISpecifyPropertyPages(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b196b28b-bab4-101a-b6-9c-00-aa-00-34-1d-07')
    @commethod(3)
    def GetPages(pPages: POINTER(Windows.Win32.System.Ole.CAUUID_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITypeChangeEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('00020410-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def RequestTypeChange(changeKind: Windows.Win32.System.Ole.CHANGEKIND, pTInfoBefore: Windows.Win32.System.Com.ITypeInfo_head, pStrName: Windows.Win32.Foundation.PWSTR, pfCancel: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AfterTypeChange(changeKind: Windows.Win32.System.Ole.CHANGEKIND, pTInfoAfter: Windows.Win32.System.Com.ITypeInfo_head, pStrName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ITypeFactory(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0000002e-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def CreateFromTypeInfo(pTypeInfo: Windows.Win32.System.Com.ITypeInfo_head, riid: POINTER(Guid), ppv: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITypeMarshal(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0000002d-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Size(pvType: c_void_p, dwDestContext: UInt32, pvDestContext: c_void_p, pSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Marshal(pvType: c_void_p, dwDestContext: UInt32, pvDestContext: c_void_p, cbBufferLength: UInt32, pBuffer: c_char_p_no, pcbWritten: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Unmarshal(pvType: c_void_p, dwFlags: UInt32, cbBufferLength: UInt32, pBuffer: c_char_p_no, pcbRead: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Free(pvType: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
class IVBFormat(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9849fd60-3768-101b-8d-72-ae-61-64-ff-e3-cf')
    @commethod(3)
    def Format(vData: POINTER(Windows.Win32.System.Com.VARIANT_head), bstrFormat: Windows.Win32.Foundation.BSTR, lpBuffer: c_void_p, cb: UInt16, lcid: Int32, sFirstDayOfWeek: Int16, sFirstWeekOfYear: UInt16, rcb: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
class IVBGetControl(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('40a050a0-3c31-101b-a8-2e-08-00-2b-2b-23-37')
    @commethod(3)
    def EnumControls(dwOleContF: Windows.Win32.System.Ole.OLECONTF, dwWhich: Windows.Win32.System.Ole.ENUM_CONTROLS_WHICH_FLAGS, ppenumUnk: POINTER(Windows.Win32.System.Com.IEnumUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IVariantChangeType(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a6ef9862-c720-11d0-93-37-00-a0-c9-0d-ca-a9')
    @commethod(3)
    def ChangeType(pvarDst: POINTER(Windows.Win32.System.Com.VARIANT_head), pvarSrc: POINTER(Windows.Win32.System.Com.VARIANT_head), lcid: UInt32, vtNew: Windows.Win32.System.Com.VARENUM) -> Windows.Win32.Foundation.HRESULT: ...
class IViewObject(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0000010d-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def Draw(dwDrawAspect: Windows.Win32.System.Com.DVASPECT, lindex: Int32, pvAspect: c_void_p, ptd: POINTER(Windows.Win32.System.Com.DVTARGETDEVICE_head), hdcTargetDev: Windows.Win32.Graphics.Gdi.HDC, hdcDraw: Windows.Win32.Graphics.Gdi.HDC, lprcBounds: POINTER(Windows.Win32.Foundation.RECTL_head), lprcWBounds: POINTER(Windows.Win32.Foundation.RECTL_head), pfnContinue: IntPtr, dwContinue: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetColorSet(dwDrawAspect: Windows.Win32.System.Com.DVASPECT, lindex: Int32, pvAspect: c_void_p, ptd: POINTER(Windows.Win32.System.Com.DVTARGETDEVICE_head), hicTargetDev: Windows.Win32.Graphics.Gdi.HDC, ppColorSet: POINTER(POINTER(Windows.Win32.Graphics.Gdi.LOGPALETTE_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Freeze(dwDrawAspect: Windows.Win32.System.Com.DVASPECT, lindex: Int32, pvAspect: c_void_p, pdwFreeze: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Unfreeze(dwFreeze: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetAdvise(aspects: Windows.Win32.System.Com.DVASPECT, advf: Windows.Win32.System.Com.ADVF, pAdvSink: Windows.Win32.System.Com.IAdviseSink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetAdvise(pAspects: POINTER(UInt32), pAdvf: POINTER(UInt32), ppAdvSink: POINTER(Windows.Win32.System.Com.IAdviseSink_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IViewObject2(c_void_p):
    extends: Windows.Win32.System.Ole.IViewObject
    Guid = Guid('00000127-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(9)
    def GetExtent(dwDrawAspect: Windows.Win32.System.Com.DVASPECT, lindex: Int32, ptd: POINTER(Windows.Win32.System.Com.DVTARGETDEVICE_head), lpsizel: POINTER(Windows.Win32.Foundation.SIZE_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IViewObjectEx(c_void_p):
    extends: Windows.Win32.System.Ole.IViewObject2
    Guid = Guid('3af24292-0c96-11ce-a0-cf-00-aa-00-60-0a-b8')
    @commethod(10)
    def GetRect(dwAspect: UInt32, pRect: POINTER(Windows.Win32.Foundation.RECTL_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetViewStatus(pdwStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def QueryHitPoint(dwAspect: UInt32, pRectBounds: POINTER(Windows.Win32.Foundation.RECT_head), ptlLoc: Windows.Win32.Foundation.POINT, lCloseHint: Int32, pHitResult: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def QueryHitRect(dwAspect: UInt32, pRectBounds: POINTER(Windows.Win32.Foundation.RECT_head), pRectLoc: POINTER(Windows.Win32.Foundation.RECT_head), lCloseHint: Int32, pHitResult: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetNaturalExtent(dwAspect: Windows.Win32.System.Com.DVASPECT, lindex: Int32, ptd: POINTER(Windows.Win32.System.Com.DVTARGETDEVICE_head), hicTargetDev: Windows.Win32.Graphics.Gdi.HDC, pExtentInfo: POINTER(Windows.Win32.System.Ole.DVEXTENTINFO_head), pSizel: POINTER(Windows.Win32.Foundation.SIZE_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IZoomEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('41b68150-904c-4e17-a0-ba-a4-38-18-2e-35-9d')
    @commethod(3)
    def OnZoomPercentChanged(ulZoomPercent: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
KEYMODIFIERS = UInt32
KEYMOD_SHIFT: KEYMODIFIERS = 1
KEYMOD_CONTROL: KEYMODIFIERS = 2
KEYMOD_ALT: KEYMODIFIERS = 4
LIBFLAGS = Int32
LIBFLAG_FRESTRICTED: LIBFLAGS = 1
LIBFLAG_FCONTROL: LIBFLAGS = 2
LIBFLAG_FHIDDEN: LIBFLAGS = 4
LIBFLAG_FHASDISKIMAGE: LIBFLAGS = 8
class LICINFO(Structure):
    cbLicInfo: Int32
    fRuntimeKeyAvail: Windows.Win32.Foundation.BOOL
    fLicVerified: Windows.Win32.Foundation.BOOL
LOAD_PICTURE_FLAGS = UInt32
LP_DEFAULT: LOAD_PICTURE_FLAGS = 0
LP_MONOCHROME: LOAD_PICTURE_FLAGS = 1
LP_VGACOLOR: LOAD_PICTURE_FLAGS = 2
LP_COLOR: LOAD_PICTURE_FLAGS = 4
@winfunctype_pointer
def LPFNOLEUIHOOK(param0: Windows.Win32.Foundation.HWND, param1: UInt32, param2: Windows.Win32.Foundation.WPARAM, param3: Windows.Win32.Foundation.LPARAM) -> UInt32: ...
MEDIAPLAYBACK_STATE = Int32
MEDIAPLAYBACK_RESUME: MEDIAPLAYBACK_STATE = 0
MEDIAPLAYBACK_PAUSE: MEDIAPLAYBACK_STATE = 1
MEDIAPLAYBACK_PAUSE_AND_SUSPEND: MEDIAPLAYBACK_STATE = 2
MEDIAPLAYBACK_RESUME_FROM_SUSPEND: MEDIAPLAYBACK_STATE = 3
class METHODDATA(Structure):
    szName: Windows.Win32.Foundation.PWSTR
    ppdata: POINTER(Windows.Win32.System.Ole.PARAMDATA_head)
    dispid: Int32
    iMeth: UInt32
    cc: Windows.Win32.System.Com.CALLCONV
    cArgs: UInt32
    wFlags: UInt16
    vtReturn: Windows.Win32.System.Com.VARENUM
MULTICLASSINFO_FLAGS = UInt32
MULTICLASSINFO_GETTYPEINFO: MULTICLASSINFO_FLAGS = 1
MULTICLASSINFO_GETNUMRESERVEDDISPIDS: MULTICLASSINFO_FLAGS = 2
MULTICLASSINFO_GETIIDPRIMARY: MULTICLASSINFO_FLAGS = 4
MULTICLASSINFO_GETIIDSOURCE: MULTICLASSINFO_FLAGS = 8
class NUMPARSE(Structure):
    cDig: Int32
    dwInFlags: Windows.Win32.System.Ole.NUMPARSE_FLAGS
    dwOutFlags: Windows.Win32.System.Ole.NUMPARSE_FLAGS
    cchUsed: Int32
    nBaseShift: Int32
    nPwr10: Int32
NUMPARSE_FLAGS = UInt32
NUMPRS_LEADING_WHITE: NUMPARSE_FLAGS = 1
NUMPRS_TRAILING_WHITE: NUMPARSE_FLAGS = 2
NUMPRS_LEADING_PLUS: NUMPARSE_FLAGS = 4
NUMPRS_TRAILING_PLUS: NUMPARSE_FLAGS = 8
NUMPRS_LEADING_MINUS: NUMPARSE_FLAGS = 16
NUMPRS_TRAILING_MINUS: NUMPARSE_FLAGS = 32
NUMPRS_HEX_OCT: NUMPARSE_FLAGS = 64
NUMPRS_PARENS: NUMPARSE_FLAGS = 128
NUMPRS_DECIMAL: NUMPARSE_FLAGS = 256
NUMPRS_THOUSANDS: NUMPARSE_FLAGS = 512
NUMPRS_CURRENCY: NUMPARSE_FLAGS = 1024
NUMPRS_EXPONENT: NUMPARSE_FLAGS = 2048
NUMPRS_USE_ALL: NUMPARSE_FLAGS = 4096
NUMPRS_STD: NUMPARSE_FLAGS = 8191
NUMPRS_NEG: NUMPARSE_FLAGS = 65536
NUMPRS_INEXACT: NUMPARSE_FLAGS = 131072
class OBJECTDESCRIPTOR(Structure):
    cbSize: UInt32
    clsid: Guid
    dwDrawAspect: UInt32
    sizel: Windows.Win32.Foundation.SIZE
    pointl: Windows.Win32.Foundation.POINTL
    dwStatus: UInt32
    dwFullUserTypeName: UInt32
    dwSrcOfCopy: UInt32
OBJECT_PROPERTIES_FLAGS = UInt32
OPF_OBJECTISLINK: OBJECT_PROPERTIES_FLAGS = 1
OPF_NOFILLDEFAULT: OBJECT_PROPERTIES_FLAGS = 2
OPF_SHOWHELP: OBJECT_PROPERTIES_FLAGS = 4
OPF_DISABLECONVERT: OBJECT_PROPERTIES_FLAGS = 8
class OCPFIPARAMS(Structure):
    cbStructSize: UInt32
    hWndOwner: Windows.Win32.Foundation.HWND
    x: Int32
    y: Int32
    lpszCaption: Windows.Win32.Foundation.PWSTR
    cObjects: UInt32
    lplpUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)
    cPages: UInt32
    lpPages: POINTER(Guid)
    lcid: UInt32
    dispidInitialProperty: Int32
OLECLOSE = Int32
OLECLOSE_SAVEIFDIRTY: OLECLOSE = 0
OLECLOSE_NOSAVE: OLECLOSE = 1
OLECLOSE_PROMPTSAVE: OLECLOSE = 2
class OLECMD(Structure):
    cmdID: Windows.Win32.System.Ole.OLECMDID
    cmdf: Windows.Win32.System.Ole.OLECMDF
OLECMDEXECOPT = Int32
OLECMDEXECOPT_DODEFAULT: OLECMDEXECOPT = 0
OLECMDEXECOPT_PROMPTUSER: OLECMDEXECOPT = 1
OLECMDEXECOPT_DONTPROMPTUSER: OLECMDEXECOPT = 2
OLECMDEXECOPT_SHOWHELP: OLECMDEXECOPT = 3
OLECMDF = Int32
OLECMDF_SUPPORTED: OLECMDF = 1
OLECMDF_ENABLED: OLECMDF = 2
OLECMDF_LATCHED: OLECMDF = 4
OLECMDF_NINCHED: OLECMDF = 8
OLECMDF_INVISIBLE: OLECMDF = 16
OLECMDF_DEFHIDEONCTXTMENU: OLECMDF = 32
OLECMDID = Int32
OLECMDID_OPEN: OLECMDID = 1
OLECMDID_NEW: OLECMDID = 2
OLECMDID_SAVE: OLECMDID = 3
OLECMDID_SAVEAS: OLECMDID = 4
OLECMDID_SAVECOPYAS: OLECMDID = 5
OLECMDID_PRINT: OLECMDID = 6
OLECMDID_PRINTPREVIEW: OLECMDID = 7
OLECMDID_PAGESETUP: OLECMDID = 8
OLECMDID_SPELL: OLECMDID = 9
OLECMDID_PROPERTIES: OLECMDID = 10
OLECMDID_CUT: OLECMDID = 11
OLECMDID_COPY: OLECMDID = 12
OLECMDID_PASTE: OLECMDID = 13
OLECMDID_PASTESPECIAL: OLECMDID = 14
OLECMDID_UNDO: OLECMDID = 15
OLECMDID_REDO: OLECMDID = 16
OLECMDID_SELECTALL: OLECMDID = 17
OLECMDID_CLEARSELECTION: OLECMDID = 18
OLECMDID_ZOOM: OLECMDID = 19
OLECMDID_GETZOOMRANGE: OLECMDID = 20
OLECMDID_UPDATECOMMANDS: OLECMDID = 21
OLECMDID_REFRESH: OLECMDID = 22
OLECMDID_STOP: OLECMDID = 23
OLECMDID_HIDETOOLBARS: OLECMDID = 24
OLECMDID_SETPROGRESSMAX: OLECMDID = 25
OLECMDID_SETPROGRESSPOS: OLECMDID = 26
OLECMDID_SETPROGRESSTEXT: OLECMDID = 27
OLECMDID_SETTITLE: OLECMDID = 28
OLECMDID_SETDOWNLOADSTATE: OLECMDID = 29
OLECMDID_STOPDOWNLOAD: OLECMDID = 30
OLECMDID_ONTOOLBARACTIVATED: OLECMDID = 31
OLECMDID_FIND: OLECMDID = 32
OLECMDID_DELETE: OLECMDID = 33
OLECMDID_HTTPEQUIV: OLECMDID = 34
OLECMDID_HTTPEQUIV_DONE: OLECMDID = 35
OLECMDID_ENABLE_INTERACTION: OLECMDID = 36
OLECMDID_ONUNLOAD: OLECMDID = 37
OLECMDID_PROPERTYBAG2: OLECMDID = 38
OLECMDID_PREREFRESH: OLECMDID = 39
OLECMDID_SHOWSCRIPTERROR: OLECMDID = 40
OLECMDID_SHOWMESSAGE: OLECMDID = 41
OLECMDID_SHOWFIND: OLECMDID = 42
OLECMDID_SHOWPAGESETUP: OLECMDID = 43
OLECMDID_SHOWPRINT: OLECMDID = 44
OLECMDID_CLOSE: OLECMDID = 45
OLECMDID_ALLOWUILESSSAVEAS: OLECMDID = 46
OLECMDID_DONTDOWNLOADCSS: OLECMDID = 47
OLECMDID_UPDATEPAGESTATUS: OLECMDID = 48
OLECMDID_PRINT2: OLECMDID = 49
OLECMDID_PRINTPREVIEW2: OLECMDID = 50
OLECMDID_SETPRINTTEMPLATE: OLECMDID = 51
OLECMDID_GETPRINTTEMPLATE: OLECMDID = 52
OLECMDID_PAGEACTIONBLOCKED: OLECMDID = 55
OLECMDID_PAGEACTIONUIQUERY: OLECMDID = 56
OLECMDID_FOCUSVIEWCONTROLS: OLECMDID = 57
OLECMDID_FOCUSVIEWCONTROLSQUERY: OLECMDID = 58
OLECMDID_SHOWPAGEACTIONMENU: OLECMDID = 59
OLECMDID_ADDTRAVELENTRY: OLECMDID = 60
OLECMDID_UPDATETRAVELENTRY: OLECMDID = 61
OLECMDID_UPDATEBACKFORWARDSTATE: OLECMDID = 62
OLECMDID_OPTICAL_ZOOM: OLECMDID = 63
OLECMDID_OPTICAL_GETZOOMRANGE: OLECMDID = 64
OLECMDID_WINDOWSTATECHANGED: OLECMDID = 65
OLECMDID_ACTIVEXINSTALLSCOPE: OLECMDID = 66
OLECMDID_UPDATETRAVELENTRY_DATARECOVERY: OLECMDID = 67
OLECMDID_SHOWTASKDLG: OLECMDID = 68
OLECMDID_POPSTATEEVENT: OLECMDID = 69
OLECMDID_VIEWPORT_MODE: OLECMDID = 70
OLECMDID_LAYOUT_VIEWPORT_WIDTH: OLECMDID = 71
OLECMDID_VISUAL_VIEWPORT_EXCLUDE_BOTTOM: OLECMDID = 72
OLECMDID_USER_OPTICAL_ZOOM: OLECMDID = 73
OLECMDID_PAGEAVAILABLE: OLECMDID = 74
OLECMDID_GETUSERSCALABLE: OLECMDID = 75
OLECMDID_UPDATE_CARET: OLECMDID = 76
OLECMDID_ENABLE_VISIBILITY: OLECMDID = 77
OLECMDID_MEDIA_PLAYBACK: OLECMDID = 78
OLECMDID_SETFAVICON: OLECMDID = 79
OLECMDID_SET_HOST_FULLSCREENMODE: OLECMDID = 80
OLECMDID_EXITFULLSCREEN: OLECMDID = 81
OLECMDID_SCROLLCOMPLETE: OLECMDID = 82
OLECMDID_ONBEFOREUNLOAD: OLECMDID = 83
OLECMDID_SHOWMESSAGE_BLOCKABLE: OLECMDID = 84
OLECMDID_SHOWTASKDLG_BLOCKABLE: OLECMDID = 85
OLECMDID_BROWSERSTATEFLAG = Int32
OLECMDIDF_BROWSERSTATE_EXTENSIONSOFF: OLECMDID_BROWSERSTATEFLAG = 1
OLECMDIDF_BROWSERSTATE_IESECURITY: OLECMDID_BROWSERSTATEFLAG = 2
OLECMDIDF_BROWSERSTATE_PROTECTEDMODE_OFF: OLECMDID_BROWSERSTATEFLAG = 4
OLECMDIDF_BROWSERSTATE_RESET: OLECMDID_BROWSERSTATEFLAG = 8
OLECMDIDF_BROWSERSTATE_REQUIRESACTIVEX: OLECMDID_BROWSERSTATEFLAG = 16
OLECMDIDF_BROWSERSTATE_DESKTOPHTMLDIALOG: OLECMDID_BROWSERSTATEFLAG = 32
OLECMDIDF_BROWSERSTATE_BLOCKEDVERSION: OLECMDID_BROWSERSTATEFLAG = 64
OLECMDID_OPTICAL_ZOOMFLAG = Int32
OLECMDIDF_OPTICAL_ZOOM_NOPERSIST: OLECMDID_OPTICAL_ZOOMFLAG = 1
OLECMDIDF_OPTICAL_ZOOM_NOLAYOUT: OLECMDID_OPTICAL_ZOOMFLAG = 16
OLECMDIDF_OPTICAL_ZOOM_NOTRANSIENT: OLECMDID_OPTICAL_ZOOMFLAG = 32
OLECMDIDF_OPTICAL_ZOOM_RELOADFORNEWTAB: OLECMDID_OPTICAL_ZOOMFLAG = 64
OLECMDID_PAGEACTIONFLAG = Int32
OLECMDIDF_PAGEACTION_FILEDOWNLOAD: OLECMDID_PAGEACTIONFLAG = 1
OLECMDIDF_PAGEACTION_ACTIVEXINSTALL: OLECMDID_PAGEACTIONFLAG = 2
OLECMDIDF_PAGEACTION_ACTIVEXTRUSTFAIL: OLECMDID_PAGEACTIONFLAG = 4
OLECMDIDF_PAGEACTION_ACTIVEXUSERDISABLE: OLECMDID_PAGEACTIONFLAG = 8
OLECMDIDF_PAGEACTION_ACTIVEXDISALLOW: OLECMDID_PAGEACTIONFLAG = 16
OLECMDIDF_PAGEACTION_ACTIVEXUNSAFE: OLECMDID_PAGEACTIONFLAG = 32
OLECMDIDF_PAGEACTION_POPUPWINDOW: OLECMDID_PAGEACTIONFLAG = 64
OLECMDIDF_PAGEACTION_LOCALMACHINE: OLECMDID_PAGEACTIONFLAG = 128
OLECMDIDF_PAGEACTION_MIMETEXTPLAIN: OLECMDID_PAGEACTIONFLAG = 256
OLECMDIDF_PAGEACTION_SCRIPTNAVIGATE: OLECMDID_PAGEACTIONFLAG = 512
OLECMDIDF_PAGEACTION_SCRIPTNAVIGATE_ACTIVEXINSTALL: OLECMDID_PAGEACTIONFLAG = 512
OLECMDIDF_PAGEACTION_PROTLOCKDOWNLOCALMACHINE: OLECMDID_PAGEACTIONFLAG = 1024
OLECMDIDF_PAGEACTION_PROTLOCKDOWNTRUSTED: OLECMDID_PAGEACTIONFLAG = 2048
OLECMDIDF_PAGEACTION_PROTLOCKDOWNINTRANET: OLECMDID_PAGEACTIONFLAG = 4096
OLECMDIDF_PAGEACTION_PROTLOCKDOWNINTERNET: OLECMDID_PAGEACTIONFLAG = 8192
OLECMDIDF_PAGEACTION_PROTLOCKDOWNRESTRICTED: OLECMDID_PAGEACTIONFLAG = 16384
OLECMDIDF_PAGEACTION_PROTLOCKDOWNDENY: OLECMDID_PAGEACTIONFLAG = 32768
OLECMDIDF_PAGEACTION_POPUPALLOWED: OLECMDID_PAGEACTIONFLAG = 65536
OLECMDIDF_PAGEACTION_SCRIPTPROMPT: OLECMDID_PAGEACTIONFLAG = 131072
OLECMDIDF_PAGEACTION_ACTIVEXUSERAPPROVAL: OLECMDID_PAGEACTIONFLAG = 262144
OLECMDIDF_PAGEACTION_MIXEDCONTENT: OLECMDID_PAGEACTIONFLAG = 524288
OLECMDIDF_PAGEACTION_INVALID_CERT: OLECMDID_PAGEACTIONFLAG = 1048576
OLECMDIDF_PAGEACTION_INTRANETZONEREQUEST: OLECMDID_PAGEACTIONFLAG = 2097152
OLECMDIDF_PAGEACTION_XSSFILTERED: OLECMDID_PAGEACTIONFLAG = 4194304
OLECMDIDF_PAGEACTION_SPOOFABLEIDNHOST: OLECMDID_PAGEACTIONFLAG = 8388608
OLECMDIDF_PAGEACTION_ACTIVEX_EPM_INCOMPATIBLE: OLECMDID_PAGEACTIONFLAG = 16777216
OLECMDIDF_PAGEACTION_SCRIPTNAVIGATE_ACTIVEXUSERAPPROVAL: OLECMDID_PAGEACTIONFLAG = 33554432
OLECMDIDF_PAGEACTION_WPCBLOCKED: OLECMDID_PAGEACTIONFLAG = 67108864
OLECMDIDF_PAGEACTION_WPCBLOCKED_ACTIVEX: OLECMDID_PAGEACTIONFLAG = 134217728
OLECMDIDF_PAGEACTION_EXTENSION_COMPAT_BLOCKED: OLECMDID_PAGEACTIONFLAG = 268435456
OLECMDIDF_PAGEACTION_NORESETACTIVEX: OLECMDID_PAGEACTIONFLAG = 536870912
OLECMDIDF_PAGEACTION_GENERIC_STATE: OLECMDID_PAGEACTIONFLAG = 1073741824
OLECMDIDF_PAGEACTION_RESET: OLECMDID_PAGEACTIONFLAG = -2147483648
OLECMDID_REFRESHFLAG = Int32
OLECMDIDF_REFRESH_NORMAL: OLECMDID_REFRESHFLAG = 0
OLECMDIDF_REFRESH_IFEXPIRED: OLECMDID_REFRESHFLAG = 1
OLECMDIDF_REFRESH_CONTINUE: OLECMDID_REFRESHFLAG = 2
OLECMDIDF_REFRESH_COMPLETELY: OLECMDID_REFRESHFLAG = 3
OLECMDIDF_REFRESH_NO_CACHE: OLECMDID_REFRESHFLAG = 4
OLECMDIDF_REFRESH_RELOAD: OLECMDID_REFRESHFLAG = 5
OLECMDIDF_REFRESH_LEVELMASK: OLECMDID_REFRESHFLAG = 255
OLECMDIDF_REFRESH_CLEARUSERINPUT: OLECMDID_REFRESHFLAG = 4096
OLECMDIDF_REFRESH_PROMPTIFOFFLINE: OLECMDID_REFRESHFLAG = 8192
OLECMDIDF_REFRESH_THROUGHSCRIPT: OLECMDID_REFRESHFLAG = 16384
OLECMDIDF_REFRESH_SKIPBEFOREUNLOADEVENT: OLECMDID_REFRESHFLAG = 32768
OLECMDIDF_REFRESH_PAGEACTION_ACTIVEXINSTALL: OLECMDID_REFRESHFLAG = 65536
OLECMDIDF_REFRESH_PAGEACTION_FILEDOWNLOAD: OLECMDID_REFRESHFLAG = 131072
OLECMDIDF_REFRESH_PAGEACTION_LOCALMACHINE: OLECMDID_REFRESHFLAG = 262144
OLECMDIDF_REFRESH_PAGEACTION_POPUPWINDOW: OLECMDID_REFRESHFLAG = 524288
OLECMDIDF_REFRESH_PAGEACTION_PROTLOCKDOWNLOCALMACHINE: OLECMDID_REFRESHFLAG = 1048576
OLECMDIDF_REFRESH_PAGEACTION_PROTLOCKDOWNTRUSTED: OLECMDID_REFRESHFLAG = 2097152
OLECMDIDF_REFRESH_PAGEACTION_PROTLOCKDOWNINTRANET: OLECMDID_REFRESHFLAG = 4194304
OLECMDIDF_REFRESH_PAGEACTION_PROTLOCKDOWNINTERNET: OLECMDID_REFRESHFLAG = 8388608
OLECMDIDF_REFRESH_PAGEACTION_PROTLOCKDOWNRESTRICTED: OLECMDID_REFRESHFLAG = 16777216
OLECMDIDF_REFRESH_PAGEACTION_MIXEDCONTENT: OLECMDID_REFRESHFLAG = 33554432
OLECMDIDF_REFRESH_PAGEACTION_INVALID_CERT: OLECMDID_REFRESHFLAG = 67108864
OLECMDIDF_REFRESH_PAGEACTION_ALLOW_VERSION: OLECMDID_REFRESHFLAG = 134217728
OLECMDID_VIEWPORT_MODE_FLAG = Int32
OLECMDIDF_VIEWPORTMODE_FIXED_LAYOUT_WIDTH: OLECMDID_VIEWPORT_MODE_FLAG = 1
OLECMDIDF_VIEWPORTMODE_EXCLUDE_VISUAL_BOTTOM: OLECMDID_VIEWPORT_MODE_FLAG = 2
OLECMDIDF_VIEWPORTMODE_FIXED_LAYOUT_WIDTH_VALID: OLECMDID_VIEWPORT_MODE_FLAG = 65536
OLECMDIDF_VIEWPORTMODE_EXCLUDE_VISUAL_BOTTOM_VALID: OLECMDID_VIEWPORT_MODE_FLAG = 131072
OLECMDID_WINDOWSTATE_FLAG = Int32
OLECMDIDF_WINDOWSTATE_USERVISIBLE: OLECMDID_WINDOWSTATE_FLAG = 1
OLECMDIDF_WINDOWSTATE_ENABLED: OLECMDID_WINDOWSTATE_FLAG = 2
OLECMDIDF_WINDOWSTATE_USERVISIBLE_VALID: OLECMDID_WINDOWSTATE_FLAG = 65536
OLECMDIDF_WINDOWSTATE_ENABLED_VALID: OLECMDID_WINDOWSTATE_FLAG = 131072
class OLECMDTEXT(Structure):
    cmdtextf: UInt32
    cwActual: UInt32
    cwBuf: UInt32
    rgwz: Char * 1
OLECMDTEXTF = Int32
OLECMDTEXTF_NONE: OLECMDTEXTF = 0
OLECMDTEXTF_NAME: OLECMDTEXTF = 1
OLECMDTEXTF_STATUS: OLECMDTEXTF = 2
OLECONTF = Int32
OLECONTF_EMBEDDINGS: OLECONTF = 1
OLECONTF_LINKS: OLECONTF = 2
OLECONTF_OTHERS: OLECONTF = 4
OLECONTF_ONLYUSER: OLECONTF = 8
OLECONTF_ONLYIFRUNNING: OLECONTF = 16
OLECREATE = UInt32
OLECREATE_ZERO: OLECREATE = 0
OLECREATE_LEAVERUNNING: OLECREATE = 1
OLEDCFLAGS = Int32
OLEDC_NODRAW: OLEDCFLAGS = 1
OLEDC_PAINTBKGND: OLEDCFLAGS = 2
OLEDC_OFFSCREEN: OLEDCFLAGS = 4
OLEGETMONIKER = Int32
OLEGETMONIKER_ONLYIFTHERE: OLEGETMONIKER = 1
OLEGETMONIKER_FORCEASSIGN: OLEGETMONIKER = 2
OLEGETMONIKER_UNASSIGN: OLEGETMONIKER = 3
OLEGETMONIKER_TEMPFORUSER: OLEGETMONIKER = 4
class OLEINPLACEFRAMEINFO(Structure):
    cb: UInt32
    fMDIApp: Windows.Win32.Foundation.BOOL
    hwndFrame: Windows.Win32.Foundation.HWND
    haccel: Windows.Win32.UI.WindowsAndMessaging.HACCEL
    cAccelEntries: UInt32
OLEIVERB = Int32
OLEIVERB_PRIMARY: OLEIVERB = 0
OLEIVERB_SHOW: OLEIVERB = -1
OLEIVERB_OPEN: OLEIVERB = -2
OLEIVERB_HIDE: OLEIVERB = -3
OLEIVERB_UIACTIVATE: OLEIVERB = -4
OLEIVERB_INPLACEACTIVATE: OLEIVERB = -5
OLEIVERB_DISCARDUNDOSTATE: OLEIVERB = -6
OLELINKBIND = Int32
OLELINKBIND_EVENIFCLASSDIFF: OLELINKBIND = 1
class OLEMENUGROUPWIDTHS(Structure):
    width: Int32 * 6
OLEMISC = Int32
OLEMISC_RECOMPOSEONRESIZE: OLEMISC = 1
OLEMISC_ONLYICONIC: OLEMISC = 2
OLEMISC_INSERTNOTREPLACE: OLEMISC = 4
OLEMISC_STATIC: OLEMISC = 8
OLEMISC_CANTLINKINSIDE: OLEMISC = 16
OLEMISC_CANLINKBYOLE1: OLEMISC = 32
OLEMISC_ISLINKOBJECT: OLEMISC = 64
OLEMISC_INSIDEOUT: OLEMISC = 128
OLEMISC_ACTIVATEWHENVISIBLE: OLEMISC = 256
OLEMISC_RENDERINGISDEVICEINDEPENDENT: OLEMISC = 512
OLEMISC_INVISIBLEATRUNTIME: OLEMISC = 1024
OLEMISC_ALWAYSRUN: OLEMISC = 2048
OLEMISC_ACTSLIKEBUTTON: OLEMISC = 4096
OLEMISC_ACTSLIKELABEL: OLEMISC = 8192
OLEMISC_NOUIACTIVATE: OLEMISC = 16384
OLEMISC_ALIGNABLE: OLEMISC = 32768
OLEMISC_SIMPLEFRAME: OLEMISC = 65536
OLEMISC_SETCLIENTSITEFIRST: OLEMISC = 131072
OLEMISC_IMEMODE: OLEMISC = 262144
OLEMISC_IGNOREACTIVATEWHENVISIBLE: OLEMISC = 524288
OLEMISC_WANTSTOMENUMERGE: OLEMISC = 1048576
OLEMISC_SUPPORTSMULTILEVELUNDO: OLEMISC = 2097152
OLERENDER = Int32
OLERENDER_NONE: OLERENDER = 0
OLERENDER_DRAW: OLERENDER = 1
OLERENDER_FORMAT: OLERENDER = 2
OLERENDER_ASIS: OLERENDER = 3
class OLEUIBUSYA(Structure):
    cbStruct: UInt32
    dwFlags: Windows.Win32.System.Ole.BUSY_DIALOG_FLAGS
    hWndOwner: Windows.Win32.Foundation.HWND
    lpszCaption: Windows.Win32.Foundation.PSTR
    lpfnHook: Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: Windows.Win32.Foundation.LPARAM
    hInstance: Windows.Win32.Foundation.HINSTANCE
    lpszTemplate: Windows.Win32.Foundation.PSTR
    hResource: Windows.Win32.Foundation.HRSRC
    hTask: Windows.Win32.Media.HTASK
    lphWndDialog: POINTER(Windows.Win32.Foundation.HWND)
class OLEUIBUSYW(Structure):
    cbStruct: UInt32
    dwFlags: Windows.Win32.System.Ole.BUSY_DIALOG_FLAGS
    hWndOwner: Windows.Win32.Foundation.HWND
    lpszCaption: Windows.Win32.Foundation.PWSTR
    lpfnHook: Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: Windows.Win32.Foundation.LPARAM
    hInstance: Windows.Win32.Foundation.HINSTANCE
    lpszTemplate: Windows.Win32.Foundation.PWSTR
    hResource: Windows.Win32.Foundation.HRSRC
    hTask: Windows.Win32.Media.HTASK
    lphWndDialog: POINTER(Windows.Win32.Foundation.HWND)
class OLEUICHANGEICONA(Structure):
    cbStruct: UInt32
    dwFlags: Windows.Win32.System.Ole.CHANGE_ICON_FLAGS
    hWndOwner: Windows.Win32.Foundation.HWND
    lpszCaption: Windows.Win32.Foundation.PSTR
    lpfnHook: Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: Windows.Win32.Foundation.LPARAM
    hInstance: Windows.Win32.Foundation.HINSTANCE
    lpszTemplate: Windows.Win32.Foundation.PSTR
    hResource: Windows.Win32.Foundation.HRSRC
    hMetaPict: Windows.Win32.Foundation.HGLOBAL
    clsid: Guid
    szIconExe: Windows.Win32.Foundation.CHAR * 260
    cchIconExe: Int32
class OLEUICHANGEICONW(Structure):
    cbStruct: UInt32
    dwFlags: Windows.Win32.System.Ole.CHANGE_ICON_FLAGS
    hWndOwner: Windows.Win32.Foundation.HWND
    lpszCaption: Windows.Win32.Foundation.PWSTR
    lpfnHook: Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: Windows.Win32.Foundation.LPARAM
    hInstance: Windows.Win32.Foundation.HINSTANCE
    lpszTemplate: Windows.Win32.Foundation.PWSTR
    hResource: Windows.Win32.Foundation.HRSRC
    hMetaPict: Windows.Win32.Foundation.HGLOBAL
    clsid: Guid
    szIconExe: Char * 260
    cchIconExe: Int32
class OLEUICHANGESOURCEA(Structure):
    cbStruct: UInt32
    dwFlags: Windows.Win32.System.Ole.CHANGE_SOURCE_FLAGS
    hWndOwner: Windows.Win32.Foundation.HWND
    lpszCaption: Windows.Win32.Foundation.PSTR
    lpfnHook: Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: Windows.Win32.Foundation.LPARAM
    hInstance: Windows.Win32.Foundation.HINSTANCE
    lpszTemplate: Windows.Win32.Foundation.PSTR
    hResource: Windows.Win32.Foundation.HRSRC
    lpOFN: POINTER(Windows.Win32.UI.Controls.Dialogs.OPENFILENAMEA_head)
    dwReserved1: UInt32 * 4
    lpOleUILinkContainer: Windows.Win32.System.Ole.IOleUILinkContainerA_head
    dwLink: UInt32
    lpszDisplayName: Windows.Win32.Foundation.PSTR
    nFileLength: UInt32
    lpszFrom: Windows.Win32.Foundation.PSTR
    lpszTo: Windows.Win32.Foundation.PSTR
class OLEUICHANGESOURCEW(Structure):
    cbStruct: UInt32
    dwFlags: Windows.Win32.System.Ole.CHANGE_SOURCE_FLAGS
    hWndOwner: Windows.Win32.Foundation.HWND
    lpszCaption: Windows.Win32.Foundation.PWSTR
    lpfnHook: Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: Windows.Win32.Foundation.LPARAM
    hInstance: Windows.Win32.Foundation.HINSTANCE
    lpszTemplate: Windows.Win32.Foundation.PWSTR
    hResource: Windows.Win32.Foundation.HRSRC
    lpOFN: POINTER(Windows.Win32.UI.Controls.Dialogs.OPENFILENAMEW_head)
    dwReserved1: UInt32 * 4
    lpOleUILinkContainer: Windows.Win32.System.Ole.IOleUILinkContainerW_head
    dwLink: UInt32
    lpszDisplayName: Windows.Win32.Foundation.PWSTR
    nFileLength: UInt32
    lpszFrom: Windows.Win32.Foundation.PWSTR
    lpszTo: Windows.Win32.Foundation.PWSTR
class OLEUICONVERTA(Structure):
    cbStruct: UInt32
    dwFlags: Windows.Win32.System.Ole.UI_CONVERT_FLAGS
    hWndOwner: Windows.Win32.Foundation.HWND
    lpszCaption: Windows.Win32.Foundation.PSTR
    lpfnHook: Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: Windows.Win32.Foundation.LPARAM
    hInstance: Windows.Win32.Foundation.HINSTANCE
    lpszTemplate: Windows.Win32.Foundation.PSTR
    hResource: Windows.Win32.Foundation.HRSRC
    clsid: Guid
    clsidConvertDefault: Guid
    clsidActivateDefault: Guid
    clsidNew: Guid
    dvAspect: UInt32
    wFormat: UInt16
    fIsLinkedObject: Windows.Win32.Foundation.BOOL
    hMetaPict: Windows.Win32.Foundation.HGLOBAL
    lpszUserType: Windows.Win32.Foundation.PSTR
    fObjectsIconChanged: Windows.Win32.Foundation.BOOL
    lpszDefLabel: Windows.Win32.Foundation.PSTR
    cClsidExclude: UInt32
    lpClsidExclude: POINTER(Guid)
class OLEUICONVERTW(Structure):
    cbStruct: UInt32
    dwFlags: Windows.Win32.System.Ole.UI_CONVERT_FLAGS
    hWndOwner: Windows.Win32.Foundation.HWND
    lpszCaption: Windows.Win32.Foundation.PWSTR
    lpfnHook: Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: Windows.Win32.Foundation.LPARAM
    hInstance: Windows.Win32.Foundation.HINSTANCE
    lpszTemplate: Windows.Win32.Foundation.PWSTR
    hResource: Windows.Win32.Foundation.HRSRC
    clsid: Guid
    clsidConvertDefault: Guid
    clsidActivateDefault: Guid
    clsidNew: Guid
    dvAspect: UInt32
    wFormat: UInt16
    fIsLinkedObject: Windows.Win32.Foundation.BOOL
    hMetaPict: Windows.Win32.Foundation.HGLOBAL
    lpszUserType: Windows.Win32.Foundation.PWSTR
    fObjectsIconChanged: Windows.Win32.Foundation.BOOL
    lpszDefLabel: Windows.Win32.Foundation.PWSTR
    cClsidExclude: UInt32
    lpClsidExclude: POINTER(Guid)
class OLEUIEDITLINKSA(Structure):
    cbStruct: UInt32
    dwFlags: Windows.Win32.System.Ole.EDIT_LINKS_FLAGS
    hWndOwner: Windows.Win32.Foundation.HWND
    lpszCaption: Windows.Win32.Foundation.PSTR
    lpfnHook: Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: Windows.Win32.Foundation.LPARAM
    hInstance: Windows.Win32.Foundation.HINSTANCE
    lpszTemplate: Windows.Win32.Foundation.PSTR
    hResource: Windows.Win32.Foundation.HRSRC
    lpOleUILinkContainer: Windows.Win32.System.Ole.IOleUILinkContainerA_head
class OLEUIEDITLINKSW(Structure):
    cbStruct: UInt32
    dwFlags: Windows.Win32.System.Ole.EDIT_LINKS_FLAGS
    hWndOwner: Windows.Win32.Foundation.HWND
    lpszCaption: Windows.Win32.Foundation.PWSTR
    lpfnHook: Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: Windows.Win32.Foundation.LPARAM
    hInstance: Windows.Win32.Foundation.HINSTANCE
    lpszTemplate: Windows.Win32.Foundation.PWSTR
    hResource: Windows.Win32.Foundation.HRSRC
    lpOleUILinkContainer: Windows.Win32.System.Ole.IOleUILinkContainerW_head
class OLEUIGNRLPROPSA(Structure):
    cbStruct: UInt32
    dwFlags: UInt32
    dwReserved1: UInt32 * 2
    lpfnHook: Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: Windows.Win32.Foundation.LPARAM
    dwReserved2: UInt32 * 3
    lpOP: POINTER(Windows.Win32.System.Ole.OLEUIOBJECTPROPSA_head)
class OLEUIGNRLPROPSW(Structure):
    cbStruct: UInt32
    dwFlags: UInt32
    dwReserved1: UInt32 * 2
    lpfnHook: Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: Windows.Win32.Foundation.LPARAM
    dwReserved2: UInt32 * 3
    lpOP: POINTER(Windows.Win32.System.Ole.OLEUIOBJECTPROPSW_head)
class OLEUIINSERTOBJECTA(Structure):
    cbStruct: UInt32
    dwFlags: Windows.Win32.System.Ole.INSERT_OBJECT_FLAGS
    hWndOwner: Windows.Win32.Foundation.HWND
    lpszCaption: Windows.Win32.Foundation.PSTR
    lpfnHook: Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: Windows.Win32.Foundation.LPARAM
    hInstance: Windows.Win32.Foundation.HINSTANCE
    lpszTemplate: Windows.Win32.Foundation.PSTR
    hResource: Windows.Win32.Foundation.HRSRC
    clsid: Guid
    lpszFile: Windows.Win32.Foundation.PSTR
    cchFile: UInt32
    cClsidExclude: UInt32
    lpClsidExclude: POINTER(Guid)
    iid: Guid
    oleRender: UInt32
    lpFormatEtc: POINTER(Windows.Win32.System.Com.FORMATETC_head)
    lpIOleClientSite: Windows.Win32.System.Ole.IOleClientSite_head
    lpIStorage: Windows.Win32.System.Com.StructuredStorage.IStorage_head
    ppvObj: POINTER(c_void_p)
    sc: Int32
    hMetaPict: Windows.Win32.Foundation.HGLOBAL
class OLEUIINSERTOBJECTW(Structure):
    cbStruct: UInt32
    dwFlags: Windows.Win32.System.Ole.INSERT_OBJECT_FLAGS
    hWndOwner: Windows.Win32.Foundation.HWND
    lpszCaption: Windows.Win32.Foundation.PWSTR
    lpfnHook: Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: Windows.Win32.Foundation.LPARAM
    hInstance: Windows.Win32.Foundation.HINSTANCE
    lpszTemplate: Windows.Win32.Foundation.PWSTR
    hResource: Windows.Win32.Foundation.HRSRC
    clsid: Guid
    lpszFile: Windows.Win32.Foundation.PWSTR
    cchFile: UInt32
    cClsidExclude: UInt32
    lpClsidExclude: POINTER(Guid)
    iid: Guid
    oleRender: UInt32
    lpFormatEtc: POINTER(Windows.Win32.System.Com.FORMATETC_head)
    lpIOleClientSite: Windows.Win32.System.Ole.IOleClientSite_head
    lpIStorage: Windows.Win32.System.Com.StructuredStorage.IStorage_head
    ppvObj: POINTER(c_void_p)
    sc: Int32
    hMetaPict: Windows.Win32.Foundation.HGLOBAL
class OLEUILINKPROPSA(Structure):
    cbStruct: UInt32
    dwFlags: UInt32
    dwReserved1: UInt32 * 2
    lpfnHook: Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: Windows.Win32.Foundation.LPARAM
    dwReserved2: UInt32 * 3
    lpOP: POINTER(Windows.Win32.System.Ole.OLEUIOBJECTPROPSA_head)
class OLEUILINKPROPSW(Structure):
    cbStruct: UInt32
    dwFlags: UInt32
    dwReserved1: UInt32 * 2
    lpfnHook: Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: Windows.Win32.Foundation.LPARAM
    dwReserved2: UInt32 * 3
    lpOP: POINTER(Windows.Win32.System.Ole.OLEUIOBJECTPROPSW_head)
class OLEUIOBJECTPROPSA(Structure):
    cbStruct: UInt32
    dwFlags: Windows.Win32.System.Ole.OBJECT_PROPERTIES_FLAGS
    lpPS: POINTER(Windows.Win32.UI.Controls.PROPSHEETHEADERA_V2_head)
    dwObject: UInt32
    lpObjInfo: Windows.Win32.System.Ole.IOleUIObjInfoA_head
    dwLink: UInt32
    lpLinkInfo: Windows.Win32.System.Ole.IOleUILinkInfoA_head
    lpGP: POINTER(Windows.Win32.System.Ole.OLEUIGNRLPROPSA_head)
    lpVP: POINTER(Windows.Win32.System.Ole.OLEUIVIEWPROPSA_head)
    lpLP: POINTER(Windows.Win32.System.Ole.OLEUILINKPROPSA_head)
class OLEUIOBJECTPROPSW(Structure):
    cbStruct: UInt32
    dwFlags: Windows.Win32.System.Ole.OBJECT_PROPERTIES_FLAGS
    lpPS: POINTER(Windows.Win32.UI.Controls.PROPSHEETHEADERW_V2_head)
    dwObject: UInt32
    lpObjInfo: Windows.Win32.System.Ole.IOleUIObjInfoW_head
    dwLink: UInt32
    lpLinkInfo: Windows.Win32.System.Ole.IOleUILinkInfoW_head
    lpGP: POINTER(Windows.Win32.System.Ole.OLEUIGNRLPROPSW_head)
    lpVP: POINTER(Windows.Win32.System.Ole.OLEUIVIEWPROPSW_head)
    lpLP: POINTER(Windows.Win32.System.Ole.OLEUILINKPROPSW_head)
class OLEUIPASTEENTRYA(Structure):
    fmtetc: Windows.Win32.System.Com.FORMATETC
    lpstrFormatName: Windows.Win32.Foundation.PSTR
    lpstrResultText: Windows.Win32.Foundation.PSTR
    dwFlags: UInt32
    dwScratchSpace: UInt32
class OLEUIPASTEENTRYW(Structure):
    fmtetc: Windows.Win32.System.Com.FORMATETC
    lpstrFormatName: Windows.Win32.Foundation.PWSTR
    lpstrResultText: Windows.Win32.Foundation.PWSTR
    dwFlags: UInt32
    dwScratchSpace: UInt32
OLEUIPASTEFLAG = Int32
OLEUIPASTE_ENABLEICON: OLEUIPASTEFLAG = 2048
OLEUIPASTE_PASTEONLY: OLEUIPASTEFLAG = 0
OLEUIPASTE_PASTE: OLEUIPASTEFLAG = 512
OLEUIPASTE_LINKANYTYPE: OLEUIPASTEFLAG = 1024
OLEUIPASTE_LINKTYPE1: OLEUIPASTEFLAG = 1
OLEUIPASTE_LINKTYPE2: OLEUIPASTEFLAG = 2
OLEUIPASTE_LINKTYPE3: OLEUIPASTEFLAG = 4
OLEUIPASTE_LINKTYPE4: OLEUIPASTEFLAG = 8
OLEUIPASTE_LINKTYPE5: OLEUIPASTEFLAG = 16
OLEUIPASTE_LINKTYPE6: OLEUIPASTEFLAG = 32
OLEUIPASTE_LINKTYPE7: OLEUIPASTEFLAG = 64
OLEUIPASTE_LINKTYPE8: OLEUIPASTEFLAG = 128
class OLEUIPASTESPECIALA(Structure):
    cbStruct: UInt32
    dwFlags: Windows.Win32.System.Ole.PASTE_SPECIAL_FLAGS
    hWndOwner: Windows.Win32.Foundation.HWND
    lpszCaption: Windows.Win32.Foundation.PSTR
    lpfnHook: Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: Windows.Win32.Foundation.LPARAM
    hInstance: Windows.Win32.Foundation.HINSTANCE
    lpszTemplate: Windows.Win32.Foundation.PSTR
    hResource: Windows.Win32.Foundation.HRSRC
    lpSrcDataObj: Windows.Win32.System.Com.IDataObject_head
    arrPasteEntries: POINTER(Windows.Win32.System.Ole.OLEUIPASTEENTRYA_head)
    cPasteEntries: Int32
    arrLinkTypes: POINTER(UInt32)
    cLinkTypes: Int32
    cClsidExclude: UInt32
    lpClsidExclude: POINTER(Guid)
    nSelectedIndex: Int32
    fLink: Windows.Win32.Foundation.BOOL
    hMetaPict: Windows.Win32.Foundation.HGLOBAL
    sizel: Windows.Win32.Foundation.SIZE
class OLEUIPASTESPECIALW(Structure):
    cbStruct: UInt32
    dwFlags: Windows.Win32.System.Ole.PASTE_SPECIAL_FLAGS
    hWndOwner: Windows.Win32.Foundation.HWND
    lpszCaption: Windows.Win32.Foundation.PWSTR
    lpfnHook: Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: Windows.Win32.Foundation.LPARAM
    hInstance: Windows.Win32.Foundation.HINSTANCE
    lpszTemplate: Windows.Win32.Foundation.PWSTR
    hResource: Windows.Win32.Foundation.HRSRC
    lpSrcDataObj: Windows.Win32.System.Com.IDataObject_head
    arrPasteEntries: POINTER(Windows.Win32.System.Ole.OLEUIPASTEENTRYW_head)
    cPasteEntries: Int32
    arrLinkTypes: POINTER(UInt32)
    cLinkTypes: Int32
    cClsidExclude: UInt32
    lpClsidExclude: POINTER(Guid)
    nSelectedIndex: Int32
    fLink: Windows.Win32.Foundation.BOOL
    hMetaPict: Windows.Win32.Foundation.HGLOBAL
    sizel: Windows.Win32.Foundation.SIZE
class OLEUIVIEWPROPSA(Structure):
    cbStruct: UInt32
    dwFlags: Windows.Win32.System.Ole.VIEW_OBJECT_PROPERTIES_FLAGS
    dwReserved1: UInt32 * 2
    lpfnHook: Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: Windows.Win32.Foundation.LPARAM
    dwReserved2: UInt32 * 3
    lpOP: POINTER(Windows.Win32.System.Ole.OLEUIOBJECTPROPSA_head)
    nScaleMin: Int32
    nScaleMax: Int32
class OLEUIVIEWPROPSW(Structure):
    cbStruct: UInt32
    dwFlags: Windows.Win32.System.Ole.VIEW_OBJECT_PROPERTIES_FLAGS
    dwReserved1: UInt32 * 2
    lpfnHook: Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: Windows.Win32.Foundation.LPARAM
    dwReserved2: UInt32 * 3
    lpOP: POINTER(Windows.Win32.System.Ole.OLEUIOBJECTPROPSW_head)
    nScaleMin: Int32
    nScaleMax: Int32
OLEUPDATE = Int32
OLEUPDATE_ALWAYS: OLEUPDATE = 1
OLEUPDATE_ONCALL: OLEUPDATE = 3
class OLEVERB(Structure):
    lVerb: Windows.Win32.System.Ole.OLEIVERB
    lpszVerbName: Windows.Win32.Foundation.PWSTR
    fuFlags: Windows.Win32.UI.WindowsAndMessaging.MENU_ITEM_FLAGS
    grfAttribs: Windows.Win32.System.Ole.OLEVERBATTRIB
OLEVERBATTRIB = Int32
OLEVERBATTRIB_NEVERDIRTIES: OLEVERBATTRIB = 1
OLEVERBATTRIB_ONCONTAINERMENU: OLEVERBATTRIB = 2
OLEWHICHMK = Int32
OLEWHICHMK_CONTAINER: OLEWHICHMK = 1
OLEWHICHMK_OBJREL: OLEWHICHMK = 2
OLEWHICHMK_OBJFULL: OLEWHICHMK = 3
OLE_HANDLE = UInt32
OLE_TRISTATE = Int32
OLE_TRISTATE_triUnchecked: OLE_TRISTATE = 0
OLE_TRISTATE_triChecked: OLE_TRISTATE = 1
OLE_TRISTATE_triGray: OLE_TRISTATE = 2
PAGEACTION_UI = Int32
PAGEACTION_UI_DEFAULT: PAGEACTION_UI = 0
PAGEACTION_UI_MODAL: PAGEACTION_UI = 1
PAGEACTION_UI_MODELESS: PAGEACTION_UI = 2
PAGEACTION_UI_SILENT: PAGEACTION_UI = 3
class PAGERANGE(Structure):
    nFromPage: Int32
    nToPage: Int32
class PAGESET(Structure):
    cbStruct: UInt32
    fOddPages: Windows.Win32.Foundation.BOOL
    fEvenPages: Windows.Win32.Foundation.BOOL
    cPageRange: UInt32
    rgPages: Windows.Win32.System.Ole.PAGERANGE * 1
class PARAMDATA(Structure):
    szName: Windows.Win32.Foundation.PWSTR
    vt: Windows.Win32.System.Com.VARENUM
class PARAMDESC(Structure):
    pparamdescex: POINTER(Windows.Win32.System.Ole.PARAMDESCEX_head)
    wParamFlags: Windows.Win32.System.Ole.PARAMFLAGS
class PARAMDESCEX(Structure):
    cBytes: UInt32
    varDefaultValue: Windows.Win32.System.Com.VARIANT
PARAMFLAGS = UInt16
PARAMFLAG_NONE: PARAMFLAGS = 0
PARAMFLAG_FIN: PARAMFLAGS = 1
PARAMFLAG_FOUT: PARAMFLAGS = 2
PARAMFLAG_FLCID: PARAMFLAGS = 4
PARAMFLAG_FRETVAL: PARAMFLAGS = 8
PARAMFLAG_FOPT: PARAMFLAGS = 16
PARAMFLAG_FHASDEFAULT: PARAMFLAGS = 32
PARAMFLAG_FHASCUSTDATA: PARAMFLAGS = 64
PASTE_SPECIAL_FLAGS = UInt32
PSF_SHOWHELP: PASTE_SPECIAL_FLAGS = 1
PSF_SELECTPASTE: PASTE_SPECIAL_FLAGS = 2
PSF_SELECTPASTELINK: PASTE_SPECIAL_FLAGS = 4
PSF_CHECKDISPLAYASICON: PASTE_SPECIAL_FLAGS = 8
PSF_DISABLEDISPLAYASICON: PASTE_SPECIAL_FLAGS = 16
PSF_HIDECHANGEICON: PASTE_SPECIAL_FLAGS = 32
PSF_STAYONCLIPBOARDCHANGE: PASTE_SPECIAL_FLAGS = 64
PSF_NOREFRESHDATAOBJECT: PASTE_SPECIAL_FLAGS = 128
class PICTDESC(Structure):
    cbSizeofstruct: UInt32
    picType: Windows.Win32.System.Ole.PICTYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        bmp: _bmp_e__Struct
        wmf: _wmf_e__Struct
        icon: _icon_e__Struct
        emf: _emf_e__Struct
        class _bmp_e__Struct(Structure):
            hbitmap: Windows.Win32.Graphics.Gdi.HBITMAP
            hpal: Windows.Win32.Graphics.Gdi.HPALETTE
        class _wmf_e__Struct(Structure):
            hmeta: Windows.Win32.Graphics.Gdi.HMETAFILE
            xExt: Int32
            yExt: Int32
        class _icon_e__Struct(Structure):
            hicon: Windows.Win32.UI.WindowsAndMessaging.HICON
        class _emf_e__Struct(Structure):
            hemf: Windows.Win32.Graphics.Gdi.HENHMETAFILE
PICTUREATTRIBUTES = Int32
PICTURE_SCALABLE: PICTUREATTRIBUTES = 1
PICTURE_TRANSPARENT: PICTUREATTRIBUTES = 2
PICTYPE = Int32
PICTYPE_UNINITIALIZED: PICTYPE = -1
PICTYPE_NONE: PICTYPE = 0
PICTYPE_BITMAP: PICTYPE = 1
PICTYPE_METAFILE: PICTYPE = 2
PICTYPE_ICON: PICTYPE = 3
PICTYPE_ENHMETAFILE: PICTYPE = 4
POINTERINACTIVE = Int32
POINTERINACTIVE_ACTIVATEONENTRY: POINTERINACTIVE = 1
POINTERINACTIVE_DEACTIVATEONLEAVE: POINTERINACTIVE = 2
POINTERINACTIVE_ACTIVATEONDRAG: POINTERINACTIVE = 4
class POINTF(Structure):
    x: Single
    y: Single
PRINTFLAG = Int32
PRINTFLAG_MAYBOTHERUSER: PRINTFLAG = 1
PRINTFLAG_PROMPTUSER: PRINTFLAG = 2
PRINTFLAG_USERMAYCHANGEPRINTER: PRINTFLAG = 4
PRINTFLAG_RECOMPOSETODEVICE: PRINTFLAG = 8
PRINTFLAG_DONTACTUALLYPRINT: PRINTFLAG = 16
PRINTFLAG_FORCEPROPERTIES: PRINTFLAG = 32
PRINTFLAG_PRINTTOFILE: PRINTFLAG = 64
PROPBAG2_TYPE = Int32
PROPBAG2_TYPE_UNDEFINED: PROPBAG2_TYPE = 0
PROPBAG2_TYPE_DATA: PROPBAG2_TYPE = 1
PROPBAG2_TYPE_URL: PROPBAG2_TYPE = 2
PROPBAG2_TYPE_OBJECT: PROPBAG2_TYPE = 3
PROPBAG2_TYPE_STREAM: PROPBAG2_TYPE = 4
PROPBAG2_TYPE_STORAGE: PROPBAG2_TYPE = 5
PROPBAG2_TYPE_MONIKER: PROPBAG2_TYPE = 6
class PROPPAGEINFO(Structure):
    cb: UInt32
    pszTitle: Windows.Win32.Foundation.PWSTR
    size: Windows.Win32.Foundation.SIZE
    pszDocString: Windows.Win32.Foundation.PWSTR
    pszHelpFile: Windows.Win32.Foundation.PWSTR
    dwHelpContext: UInt32
PROPPAGESTATUS = Int32
PROPPAGESTATUS_DIRTY: PROPPAGESTATUS = 1
PROPPAGESTATUS_VALIDATE: PROPPAGESTATUS = 2
PROPPAGESTATUS_CLEAN: PROPPAGESTATUS = 4
class QACONTAINER(Structure):
    cbSize: UInt32
    pClientSite: Windows.Win32.System.Ole.IOleClientSite_head
    pAdviseSink: Windows.Win32.System.Ole.IAdviseSinkEx_head
    pPropertyNotifySink: Windows.Win32.System.Ole.IPropertyNotifySink_head
    pUnkEventSink: Windows.Win32.System.Com.IUnknown_head
    dwAmbientFlags: Windows.Win32.System.Ole.QACONTAINERFLAGS
    colorFore: UInt32
    colorBack: UInt32
    pFont: Windows.Win32.System.Ole.IFont_head
    pUndoMgr: Windows.Win32.System.Ole.IOleUndoManager_head
    dwAppearance: UInt32
    lcid: Int32
    hpal: Windows.Win32.Graphics.Gdi.HPALETTE
    pBindHost: Windows.Win32.System.Com.IBindHost_head
    pOleControlSite: Windows.Win32.System.Ole.IOleControlSite_head
    pServiceProvider: Windows.Win32.System.Com.IServiceProvider_head
QACONTAINERFLAGS = Int32
QACONTAINER_SHOWHATCHING: QACONTAINERFLAGS = 1
QACONTAINER_SHOWGRABHANDLES: QACONTAINERFLAGS = 2
QACONTAINER_USERMODE: QACONTAINERFLAGS = 4
QACONTAINER_DISPLAYASDEFAULT: QACONTAINERFLAGS = 8
QACONTAINER_UIDEAD: QACONTAINERFLAGS = 16
QACONTAINER_AUTOCLIP: QACONTAINERFLAGS = 32
QACONTAINER_MESSAGEREFLECT: QACONTAINERFLAGS = 64
QACONTAINER_SUPPORTSMNEMONICS: QACONTAINERFLAGS = 128
class QACONTROL(Structure):
    cbSize: UInt32
    dwMiscStatus: Windows.Win32.System.Ole.OLEMISC
    dwViewStatus: Windows.Win32.System.Ole.VIEWSTATUS
    dwEventCookie: UInt32
    dwPropNotifyCookie: UInt32
    dwPointerActivationPolicy: Windows.Win32.System.Ole.POINTERINACTIVE
READYSTATE = Int32
READYSTATE_UNINITIALIZED: READYSTATE = 0
READYSTATE_LOADING: READYSTATE = 1
READYSTATE_LOADED: READYSTATE = 2
READYSTATE_INTERACTIVE: READYSTATE = 3
READYSTATE_COMPLETE: READYSTATE = 4
REGKIND = Int32
REGKIND_DEFAULT: REGKIND = 0
REGKIND_REGISTER: REGKIND = 1
REGKIND_NONE: REGKIND = 2
class SAFEARRAYUNION(Structure):
    sfType: UInt32
    u: _u_e__Struct
    class _u_e__Struct(Union):
        BstrStr: Windows.Win32.System.Ole.SAFEARR_BSTR
        UnknownStr: Windows.Win32.System.Ole.SAFEARR_UNKNOWN
        DispatchStr: Windows.Win32.System.Ole.SAFEARR_DISPATCH
        VariantStr: Windows.Win32.System.Ole.SAFEARR_VARIANT
        RecordStr: Windows.Win32.System.Ole.SAFEARR_BRECORD
        HaveIidStr: Windows.Win32.System.Ole.SAFEARR_HAVEIID
        ByteStr: Windows.Win32.System.Com.BYTE_SIZEDARR
        WordStr: Windows.Win32.System.Com.WORD_SIZEDARR
        LongStr: Windows.Win32.System.Com.DWORD_SIZEDARR
        HyperStr: Windows.Win32.System.Com.HYPER_SIZEDARR
class SAFEARR_BRECORD(Structure):
    Size: UInt32
    aRecord: POINTER(POINTER(Windows.Win32.System.Ole._wireBRECORD_head))
class SAFEARR_BSTR(Structure):
    Size: UInt32
    aBstr: POINTER(POINTER(Windows.Win32.System.Com.FLAGGED_WORD_BLOB_head))
class SAFEARR_DISPATCH(Structure):
    Size: UInt32
    apDispatch: POINTER(Windows.Win32.System.Com.IDispatch_head)
class SAFEARR_HAVEIID(Structure):
    Size: UInt32
    apUnknown: POINTER(Windows.Win32.System.Com.IUnknown_head)
    iid: Guid
class SAFEARR_UNKNOWN(Structure):
    Size: UInt32
    apUnknown: POINTER(Windows.Win32.System.Com.IUnknown_head)
class SAFEARR_VARIANT(Structure):
    Size: UInt32
    aVariant: POINTER(POINTER(Windows.Win32.System.Ole._wireVARIANT_head))
SF_TYPE = Int32
SF_ERROR: SF_TYPE = 10
SF_I1: SF_TYPE = 16
SF_I2: SF_TYPE = 2
SF_I4: SF_TYPE = 3
SF_I8: SF_TYPE = 20
SF_BSTR: SF_TYPE = 8
SF_UNKNOWN: SF_TYPE = 13
SF_DISPATCH: SF_TYPE = 9
SF_VARIANT: SF_TYPE = 12
SF_RECORD: SF_TYPE = 36
SF_HAVEIID: SF_TYPE = 32781
TYPEFLAGS = Int32
TYPEFLAG_FAPPOBJECT: TYPEFLAGS = 1
TYPEFLAG_FCANCREATE: TYPEFLAGS = 2
TYPEFLAG_FLICENSED: TYPEFLAGS = 4
TYPEFLAG_FPREDECLID: TYPEFLAGS = 8
TYPEFLAG_FHIDDEN: TYPEFLAGS = 16
TYPEFLAG_FCONTROL: TYPEFLAGS = 32
TYPEFLAG_FDUAL: TYPEFLAGS = 64
TYPEFLAG_FNONEXTENSIBLE: TYPEFLAGS = 128
TYPEFLAG_FOLEAUTOMATION: TYPEFLAGS = 256
TYPEFLAG_FRESTRICTED: TYPEFLAGS = 512
TYPEFLAG_FAGGREGATABLE: TYPEFLAGS = 1024
TYPEFLAG_FREPLACEABLE: TYPEFLAGS = 2048
TYPEFLAG_FDISPATCHABLE: TYPEFLAGS = 4096
TYPEFLAG_FREVERSEBIND: TYPEFLAGS = 8192
TYPEFLAG_FPROXY: TYPEFLAGS = 16384
UASFLAGS = Int32
UAS_NORMAL: UASFLAGS = 0
UAS_BLOCKED: UASFLAGS = 1
UAS_NOPARENTENABLE: UASFLAGS = 2
UAS_MASK: UASFLAGS = 3
class UDATE(Structure):
    st: Windows.Win32.Foundation.SYSTEMTIME
    wDayOfYear: UInt16
UI_CONVERT_FLAGS = UInt32
CF_SHOWHELPBUTTON: UI_CONVERT_FLAGS = 1
CF_SETCONVERTDEFAULT: UI_CONVERT_FLAGS = 2
CF_SETACTIVATEDEFAULT: UI_CONVERT_FLAGS = 4
CF_SELECTCONVERTTO: UI_CONVERT_FLAGS = 8
CF_SELECTACTIVATEAS: UI_CONVERT_FLAGS = 16
CF_DISABLEDISPLAYASICON: UI_CONVERT_FLAGS = 32
CF_DISABLEACTIVATEAS: UI_CONVERT_FLAGS = 64
CF_HIDECHANGEICON: UI_CONVERT_FLAGS = 128
CF_CONVERTONLY: UI_CONVERT_FLAGS = 256
UPDFCACHE_FLAGS = UInt32
UPDFCACHE_ALL: UPDFCACHE_FLAGS = 2147483647
UPDFCACHE_ALLBUTNODATACACHE: UPDFCACHE_FLAGS = 2147483646
UPDFCACHE_NORMALCACHE: UPDFCACHE_FLAGS = 8
UPDFCACHE_IFBLANK: UPDFCACHE_FLAGS = 16
UPDFCACHE_ONLYIFBLANK: UPDFCACHE_FLAGS = 2147483648
UPDFCACHE_NODATACACHE: UPDFCACHE_FLAGS = 1
UPDFCACHE_ONSAVECACHE: UPDFCACHE_FLAGS = 2
UPDFCACHE_ONSTOPCACHE: UPDFCACHE_FLAGS = 4
UPDFCACHE_IFBLANKORONSAVECACHE: UPDFCACHE_FLAGS = 18
USERCLASSTYPE = Int32
USERCLASSTYPE_FULL: USERCLASSTYPE = 1
USERCLASSTYPE_SHORT: USERCLASSTYPE = 2
USERCLASSTYPE_APPNAME: USERCLASSTYPE = 3
VARCMP = UInt32
VARCMP_LT: VARCMP = 0
VARCMP_EQ: VARCMP = 1
VARCMP_GT: VARCMP = 2
VARCMP_NULL: VARCMP = 3
VARFORMAT_FIRST_DAY = Int32
VARFORMAT_FIRST_DAY_SYSTEMDEFAULT: VARFORMAT_FIRST_DAY = 0
VARFORMAT_FIRST_DAY_MONDAY: VARFORMAT_FIRST_DAY = 1
VARFORMAT_FIRST_DAY_TUESDAY: VARFORMAT_FIRST_DAY = 2
VARFORMAT_FIRST_DAY_WEDNESDAY: VARFORMAT_FIRST_DAY = 3
VARFORMAT_FIRST_DAY_THURSDAY: VARFORMAT_FIRST_DAY = 4
VARFORMAT_FIRST_DAY_FRIDAY: VARFORMAT_FIRST_DAY = 5
VARFORMAT_FIRST_DAY_SATURDAY: VARFORMAT_FIRST_DAY = 6
VARFORMAT_FIRST_DAY_SUNDAY: VARFORMAT_FIRST_DAY = 7
VARFORMAT_FIRST_WEEK = Int32
VARFORMAT_FIRST_WEEK_SYSTEMDEFAULT: VARFORMAT_FIRST_WEEK = 0
VARFORMAT_FIRST_WEEK_CONTAINS_JANUARY_FIRST: VARFORMAT_FIRST_WEEK = 1
VARFORMAT_FIRST_WEEK_LARGER_HALF_IN_CURRENT_YEAR: VARFORMAT_FIRST_WEEK = 2
VARFORMAT_FIRST_WEEK_HAS_SEVEN_DAYS: VARFORMAT_FIRST_WEEK = 3
VARFORMAT_GROUP = Int32
VARFORMAT_GROUP_SYSTEMDEFAULT: VARFORMAT_GROUP = -2
VARFORMAT_GROUP_THOUSANDS: VARFORMAT_GROUP = -1
VARFORMAT_GROUP_NOTTHOUSANDS: VARFORMAT_GROUP = 0
VARFORMAT_LEADING_DIGIT = Int32
VARFORMAT_LEADING_DIGIT_SYSTEMDEFAULT: VARFORMAT_LEADING_DIGIT = -2
VARFORMAT_LEADING_DIGIT_INCLUDED: VARFORMAT_LEADING_DIGIT = -1
VARFORMAT_LEADING_DIGIT_NOTINCLUDED: VARFORMAT_LEADING_DIGIT = 0
VARFORMAT_NAMED_FORMAT = Int32
VARFORMAT_NAMED_FORMAT_GENERALDATE: VARFORMAT_NAMED_FORMAT = 0
VARFORMAT_NAMED_FORMAT_LONGDATE: VARFORMAT_NAMED_FORMAT = 1
VARFORMAT_NAMED_FORMAT_SHORTDATE: VARFORMAT_NAMED_FORMAT = 2
VARFORMAT_NAMED_FORMAT_LONGTIME: VARFORMAT_NAMED_FORMAT = 3
VARFORMAT_NAMED_FORMAT_SHORTTIME: VARFORMAT_NAMED_FORMAT = 4
VARFORMAT_PARENTHESES = Int32
VARFORMAT_PARENTHESES_SYSTEMDEFAULT: VARFORMAT_PARENTHESES = -2
VARFORMAT_PARENTHESES_USED: VARFORMAT_PARENTHESES = -1
VARFORMAT_PARENTHESES_NOTUSED: VARFORMAT_PARENTHESES = 0
VIEWSTATUS = Int32
VIEWSTATUS_OPAQUE: VIEWSTATUS = 1
VIEWSTATUS_SOLIDBKGND: VIEWSTATUS = 2
VIEWSTATUS_DVASPECTOPAQUE: VIEWSTATUS = 4
VIEWSTATUS_DVASPECTTRANSPARENT: VIEWSTATUS = 8
VIEWSTATUS_SURFACE: VIEWSTATUS = 16
VIEWSTATUS_3DSURFACE: VIEWSTATUS = 32
VIEW_OBJECT_PROPERTIES_FLAGS = UInt32
VPF_SELECTRELATIVE: VIEW_OBJECT_PROPERTIES_FLAGS = 1
VPF_DISABLERELATIVE: VIEW_OBJECT_PROPERTIES_FLAGS = 2
VPF_DISABLESCALE: VIEW_OBJECT_PROPERTIES_FLAGS = 4
WPCSETTING = Int32
WPCSETTING_LOGGING_ENABLED: WPCSETTING = 1
WPCSETTING_FILEDOWNLOAD_BLOCKED: WPCSETTING = 2
XFORMCOORDS = Int32
XFORMCOORDS_POSITION: XFORMCOORDS = 1
XFORMCOORDS_SIZE: XFORMCOORDS = 2
XFORMCOORDS_HIMETRICTOCONTAINER: XFORMCOORDS = 4
XFORMCOORDS_CONTAINERTOHIMETRIC: XFORMCOORDS = 8
XFORMCOORDS_EVENTCOMPAT: XFORMCOORDS = 16
class _wireBRECORD(Structure):
    fFlags: UInt32
    clSize: UInt32
    pRecInfo: Windows.Win32.System.Ole.IRecordInfo_head
    pRecord: c_char_p_no
class _wireSAFEARRAY(Structure):
    cDims: UInt16
    fFeatures: UInt16
    cbElements: UInt32
    cLocks: UInt32
    uArrayStructs: Windows.Win32.System.Ole.SAFEARRAYUNION
    rgsabound: Windows.Win32.System.Com.SAFEARRAYBOUND * 1
class _wireVARIANT(Structure):
    clSize: UInt32
    rpcReserved: UInt32
    vt: UInt16
    wReserved1: UInt16
    wReserved2: UInt16
    wReserved3: UInt16
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        llVal: Int64
        lVal: Int32
        bVal: Byte
        iVal: Int16
        fltVal: Single
        dblVal: Double
        boolVal: Windows.Win32.Foundation.VARIANT_BOOL
        scode: Int32
        cyVal: Windows.Win32.System.Com.CY
        date: Double
        bstrVal: POINTER(Windows.Win32.System.Com.FLAGGED_WORD_BLOB_head)
        punkVal: Windows.Win32.System.Com.IUnknown_head
        pdispVal: Windows.Win32.System.Com.IDispatch_head
        parray: POINTER(POINTER(Windows.Win32.System.Ole._wireSAFEARRAY_head))
        brecVal: POINTER(Windows.Win32.System.Ole._wireBRECORD_head)
        pbVal: c_char_p_no
        piVal: POINTER(Int16)
        plVal: POINTER(Int32)
        pllVal: POINTER(Int64)
        pfltVal: POINTER(Single)
        pdblVal: POINTER(Double)
        pboolVal: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)
        pscode: POINTER(Int32)
        pcyVal: POINTER(Windows.Win32.System.Com.CY_head)
        pdate: POINTER(Double)
        pbstrVal: POINTER(POINTER(Windows.Win32.System.Com.FLAGGED_WORD_BLOB_head))
        ppunkVal: POINTER(Windows.Win32.System.Com.IUnknown_head)
        ppdispVal: POINTER(Windows.Win32.System.Com.IDispatch_head)
        pparray: POINTER(POINTER(POINTER(Windows.Win32.System.Ole._wireSAFEARRAY_head)))
        pvarVal: POINTER(POINTER(Windows.Win32.System.Ole._wireVARIANT_head))
        cVal: Windows.Win32.Foundation.CHAR
        uiVal: UInt16
        ulVal: UInt32
        ullVal: UInt64
        intVal: Int32
        uintVal: UInt32
        decVal: Windows.Win32.Foundation.DECIMAL
        pdecVal: POINTER(Windows.Win32.Foundation.DECIMAL_head)
        pcVal: Windows.Win32.Foundation.PSTR
        puiVal: POINTER(UInt16)
        pulVal: POINTER(UInt32)
        pullVal: POINTER(UInt64)
        pintVal: POINTER(Int32)
        puintVal: POINTER(UInt32)
make_head(_module, 'ARRAYDESC')
make_head(_module, 'CADWORD')
make_head(_module, 'CALPOLESTR')
make_head(_module, 'CAUUID')
make_head(_module, 'CLEANLOCALSTORAGE')
make_head(_module, 'CONTROLINFO')
make_head(_module, 'DVASPECTINFO')
make_head(_module, 'DVEXTENTINFO')
make_head(_module, 'FONTDESC')
make_head(_module, 'IAdviseSinkEx')
make_head(_module, 'ICanHandleException')
make_head(_module, 'IClassFactory2')
make_head(_module, 'IContinue')
make_head(_module, 'IContinueCallback')
make_head(_module, 'ICreateErrorInfo')
make_head(_module, 'ICreateTypeInfo')
make_head(_module, 'ICreateTypeInfo2')
make_head(_module, 'ICreateTypeLib')
make_head(_module, 'ICreateTypeLib2')
make_head(_module, 'IDispError')
make_head(_module, 'IDispatchEx')
make_head(_module, 'IDropSource')
make_head(_module, 'IDropSourceNotify')
make_head(_module, 'IDropTarget')
make_head(_module, 'IEnterpriseDropTarget')
make_head(_module, 'IEnumOLEVERB')
make_head(_module, 'IEnumOleDocumentViews')
make_head(_module, 'IEnumOleUndoUnits')
make_head(_module, 'IEnumVARIANT')
make_head(_module, 'IFont')
make_head(_module, 'IFontDisp')
make_head(_module, 'IFontEventsDisp')
make_head(_module, 'IGetOleObject')
make_head(_module, 'IGetVBAObject')
make_head(_module, 'INTERFACEDATA')
make_head(_module, 'IObjectIdentity')
make_head(_module, 'IObjectWithSite')
make_head(_module, 'IOleAdviseHolder')
make_head(_module, 'IOleCache')
make_head(_module, 'IOleCache2')
make_head(_module, 'IOleCacheControl')
make_head(_module, 'IOleClientSite')
make_head(_module, 'IOleCommandTarget')
make_head(_module, 'IOleContainer')
make_head(_module, 'IOleControl')
make_head(_module, 'IOleControlSite')
make_head(_module, 'IOleDocument')
make_head(_module, 'IOleDocumentSite')
make_head(_module, 'IOleDocumentView')
make_head(_module, 'IOleInPlaceActiveObject')
make_head(_module, 'IOleInPlaceFrame')
make_head(_module, 'IOleInPlaceObject')
make_head(_module, 'IOleInPlaceObjectWindowless')
make_head(_module, 'IOleInPlaceSite')
make_head(_module, 'IOleInPlaceSiteEx')
make_head(_module, 'IOleInPlaceSiteWindowless')
make_head(_module, 'IOleInPlaceUIWindow')
make_head(_module, 'IOleItemContainer')
make_head(_module, 'IOleLink')
make_head(_module, 'IOleObject')
make_head(_module, 'IOleParentUndoUnit')
make_head(_module, 'IOleUILinkContainerA')
make_head(_module, 'IOleUILinkContainerW')
make_head(_module, 'IOleUILinkInfoA')
make_head(_module, 'IOleUILinkInfoW')
make_head(_module, 'IOleUIObjInfoA')
make_head(_module, 'IOleUIObjInfoW')
make_head(_module, 'IOleUndoManager')
make_head(_module, 'IOleUndoUnit')
make_head(_module, 'IOleWindow')
make_head(_module, 'IParseDisplayName')
make_head(_module, 'IPerPropertyBrowsing')
make_head(_module, 'IPersistPropertyBag')
make_head(_module, 'IPersistPropertyBag2')
make_head(_module, 'IPicture')
make_head(_module, 'IPicture2')
make_head(_module, 'IPictureDisp')
make_head(_module, 'IPointerInactive')
make_head(_module, 'IPrint')
make_head(_module, 'IPropertyNotifySink')
make_head(_module, 'IPropertyPage')
make_head(_module, 'IPropertyPage2')
make_head(_module, 'IPropertyPageSite')
make_head(_module, 'IProtectFocus')
make_head(_module, 'IProtectedModeMenuServices')
make_head(_module, 'IProvideClassInfo')
make_head(_module, 'IProvideClassInfo2')
make_head(_module, 'IProvideMultipleClassInfo')
make_head(_module, 'IProvideRuntimeContext')
make_head(_module, 'IQuickActivate')
make_head(_module, 'IRecordInfo')
make_head(_module, 'ISimpleFrameSite')
make_head(_module, 'ISpecifyPropertyPages')
make_head(_module, 'ITypeChangeEvents')
make_head(_module, 'ITypeFactory')
make_head(_module, 'ITypeMarshal')
make_head(_module, 'IVBFormat')
make_head(_module, 'IVBGetControl')
make_head(_module, 'IVariantChangeType')
make_head(_module, 'IViewObject')
make_head(_module, 'IViewObject2')
make_head(_module, 'IViewObjectEx')
make_head(_module, 'IZoomEvents')
make_head(_module, 'LICINFO')
make_head(_module, 'LPFNOLEUIHOOK')
make_head(_module, 'METHODDATA')
make_head(_module, 'NUMPARSE')
make_head(_module, 'OBJECTDESCRIPTOR')
make_head(_module, 'OCPFIPARAMS')
make_head(_module, 'OLECMD')
make_head(_module, 'OLECMDTEXT')
make_head(_module, 'OLEINPLACEFRAMEINFO')
make_head(_module, 'OLEMENUGROUPWIDTHS')
make_head(_module, 'OLEUIBUSYA')
make_head(_module, 'OLEUIBUSYW')
make_head(_module, 'OLEUICHANGEICONA')
make_head(_module, 'OLEUICHANGEICONW')
make_head(_module, 'OLEUICHANGESOURCEA')
make_head(_module, 'OLEUICHANGESOURCEW')
make_head(_module, 'OLEUICONVERTA')
make_head(_module, 'OLEUICONVERTW')
make_head(_module, 'OLEUIEDITLINKSA')
make_head(_module, 'OLEUIEDITLINKSW')
make_head(_module, 'OLEUIGNRLPROPSA')
make_head(_module, 'OLEUIGNRLPROPSW')
make_head(_module, 'OLEUIINSERTOBJECTA')
make_head(_module, 'OLEUIINSERTOBJECTW')
make_head(_module, 'OLEUILINKPROPSA')
make_head(_module, 'OLEUILINKPROPSW')
make_head(_module, 'OLEUIOBJECTPROPSA')
make_head(_module, 'OLEUIOBJECTPROPSW')
make_head(_module, 'OLEUIPASTEENTRYA')
make_head(_module, 'OLEUIPASTEENTRYW')
make_head(_module, 'OLEUIPASTESPECIALA')
make_head(_module, 'OLEUIPASTESPECIALW')
make_head(_module, 'OLEUIVIEWPROPSA')
make_head(_module, 'OLEUIVIEWPROPSW')
make_head(_module, 'OLEVERB')
make_head(_module, 'PAGERANGE')
make_head(_module, 'PAGESET')
make_head(_module, 'PARAMDATA')
make_head(_module, 'PARAMDESC')
make_head(_module, 'PARAMDESCEX')
make_head(_module, 'PICTDESC')
make_head(_module, 'POINTF')
make_head(_module, 'PROPPAGEINFO')
make_head(_module, 'QACONTAINER')
make_head(_module, 'QACONTROL')
make_head(_module, 'SAFEARRAYUNION')
make_head(_module, 'SAFEARR_BRECORD')
make_head(_module, 'SAFEARR_BSTR')
make_head(_module, 'SAFEARR_DISPATCH')
make_head(_module, 'SAFEARR_HAVEIID')
make_head(_module, 'SAFEARR_UNKNOWN')
make_head(_module, 'SAFEARR_VARIANT')
make_head(_module, 'UDATE')
make_head(_module, '_wireBRECORD')
make_head(_module, '_wireSAFEARRAY')
make_head(_module, '_wireVARIANT')
__all__ = [
    "ACTIVATEFLAGS",
    "ACTIVATE_WINDOWLESS",
    "ACTIVEOBJECT_FLAGS",
    "ACTIVEOBJECT_STRONG",
    "ACTIVEOBJECT_WEAK",
    "ARRAYDESC",
    "BINDSPEED",
    "BINDSPEED_IMMEDIATE",
    "BINDSPEED_INDEFINITE",
    "BINDSPEED_MODERATE",
    "BUSY_DIALOG_FLAGS",
    "BZ_DISABLECANCELBUTTON",
    "BZ_DISABLERETRYBUTTON",
    "BZ_DISABLESWITCHTOBUTTON",
    "BZ_NOTRESPONDINGDIALOG",
    "BstrFromVector",
    "CADWORD",
    "CALPOLESTR",
    "CAUUID",
    "CF_BITMAP",
    "CF_CONVERTONLY",
    "CF_DIB",
    "CF_DIBV5",
    "CF_DIF",
    "CF_DISABLEACTIVATEAS",
    "CF_DISABLEDISPLAYASICON",
    "CF_DSPBITMAP",
    "CF_DSPENHMETAFILE",
    "CF_DSPMETAFILEPICT",
    "CF_DSPTEXT",
    "CF_ENHMETAFILE",
    "CF_GDIOBJFIRST",
    "CF_GDIOBJLAST",
    "CF_HDROP",
    "CF_HIDECHANGEICON",
    "CF_LOCALE",
    "CF_MAX",
    "CF_METAFILEPICT",
    "CF_OEMTEXT",
    "CF_OWNERDISPLAY",
    "CF_PALETTE",
    "CF_PENDATA",
    "CF_PRIVATEFIRST",
    "CF_PRIVATELAST",
    "CF_RIFF",
    "CF_SELECTACTIVATEAS",
    "CF_SELECTCONVERTTO",
    "CF_SETACTIVATEDEFAULT",
    "CF_SETCONVERTDEFAULT",
    "CF_SHOWHELPBUTTON",
    "CF_SYLK",
    "CF_TEXT",
    "CF_TIFF",
    "CF_UNICODETEXT",
    "CF_WAVE",
    "CHANGEKIND",
    "CHANGEKIND_ADDMEMBER",
    "CHANGEKIND_CHANGEFAILED",
    "CHANGEKIND_DELETEMEMBER",
    "CHANGEKIND_GENERAL",
    "CHANGEKIND_INVALIDATE",
    "CHANGEKIND_MAX",
    "CHANGEKIND_SETDOCUMENTATION",
    "CHANGEKIND_SETNAMES",
    "CHANGE_ICON_FLAGS",
    "CHANGE_SOURCE_FLAGS",
    "CIF_SELECTCURRENT",
    "CIF_SELECTDEFAULT",
    "CIF_SELECTFROMFILE",
    "CIF_SHOWHELP",
    "CIF_USEICONEXE",
    "CLEANLOCALSTORAGE",
    "CLIPBOARD_FORMAT",
    "CLSID_CColorPropPage",
    "CLSID_CFontPropPage",
    "CLSID_CPicturePropPage",
    "CLSID_ConvertVBX",
    "CLSID_PersistPropset",
    "CLSID_StdFont",
    "CLSID_StdPicture",
    "CONNECT_E_ADVISELIMIT",
    "CONNECT_E_CANNOTCONNECT",
    "CONNECT_E_FIRST",
    "CONNECT_E_LAST",
    "CONNECT_E_NOCONNECTION",
    "CONNECT_E_OVERRIDDEN",
    "CONNECT_S_FIRST",
    "CONNECT_S_LAST",
    "CONTROLINFO",
    "CSF_EXPLORER",
    "CSF_ONLYGETSOURCE",
    "CSF_SHOWHELP",
    "CSF_VALIDSOURCE",
    "CTL_E_ILLEGALFUNCTIONCALL",
    "CTRLINFO",
    "CTRLINFO_EATS_ESCAPE",
    "CTRLINFO_EATS_RETURN",
    "ClearCustData",
    "CreateDispTypeInfo",
    "CreateErrorInfo",
    "CreateOleAdviseHolder",
    "CreateStdDispatch",
    "CreateTypeLib",
    "CreateTypeLib2",
    "DD_DEFDRAGDELAY",
    "DD_DEFDRAGMINDIST",
    "DD_DEFSCROLLDELAY",
    "DD_DEFSCROLLINSET",
    "DD_DEFSCROLLINTERVAL",
    "DISCARDCACHE",
    "DISCARDCACHE_NOSAVE",
    "DISCARDCACHE_SAVEIFDIRTY",
    "DISPATCH_CONSTRUCT",
    "DISPID_ABOUTBOX",
    "DISPID_ACCELERATOR",
    "DISPID_ADDITEM",
    "DISPID_AMBIENT_APPEARANCE",
    "DISPID_AMBIENT_AUTOCLIP",
    "DISPID_AMBIENT_BACKCOLOR",
    "DISPID_AMBIENT_CHARSET",
    "DISPID_AMBIENT_CODEPAGE",
    "DISPID_AMBIENT_DISPLAYASDEFAULT",
    "DISPID_AMBIENT_DISPLAYNAME",
    "DISPID_AMBIENT_FONT",
    "DISPID_AMBIENT_FORECOLOR",
    "DISPID_AMBIENT_LOCALEID",
    "DISPID_AMBIENT_MESSAGEREFLECT",
    "DISPID_AMBIENT_PALETTE",
    "DISPID_AMBIENT_RIGHTTOLEFT",
    "DISPID_AMBIENT_SCALEUNITS",
    "DISPID_AMBIENT_SHOWGRABHANDLES",
    "DISPID_AMBIENT_SHOWHATCHING",
    "DISPID_AMBIENT_SUPPORTSMNEMONICS",
    "DISPID_AMBIENT_TEXTALIGN",
    "DISPID_AMBIENT_TOPTOBOTTOM",
    "DISPID_AMBIENT_TRANSFERPRIORITY",
    "DISPID_AMBIENT_UIDEAD",
    "DISPID_AMBIENT_USERMODE",
    "DISPID_APPEARANCE",
    "DISPID_AUTOSIZE",
    "DISPID_BACKCOLOR",
    "DISPID_BACKSTYLE",
    "DISPID_BORDERCOLOR",
    "DISPID_BORDERSTYLE",
    "DISPID_BORDERVISIBLE",
    "DISPID_BORDERWIDTH",
    "DISPID_CAPTION",
    "DISPID_CLEAR",
    "DISPID_CLICK",
    "DISPID_CLICK_VALUE",
    "DISPID_COLLECT",
    "DISPID_COLUMN",
    "DISPID_CONSTRUCTOR",
    "DISPID_DBLCLICK",
    "DISPID_DESTRUCTOR",
    "DISPID_DISPLAYSTYLE",
    "DISPID_DOCLICK",
    "DISPID_DRAWMODE",
    "DISPID_DRAWSTYLE",
    "DISPID_DRAWWIDTH",
    "DISPID_Delete",
    "DISPID_ENABLED",
    "DISPID_ENTERKEYBEHAVIOR",
    "DISPID_ERROREVENT",
    "DISPID_EVALUATE",
    "DISPID_FILLCOLOR",
    "DISPID_FILLSTYLE",
    "DISPID_FONT",
    "DISPID_FONT_BOLD",
    "DISPID_FONT_CHANGED",
    "DISPID_FONT_CHARSET",
    "DISPID_FONT_ITALIC",
    "DISPID_FONT_NAME",
    "DISPID_FONT_SIZE",
    "DISPID_FONT_STRIKE",
    "DISPID_FONT_UNDER",
    "DISPID_FONT_WEIGHT",
    "DISPID_FORECOLOR",
    "DISPID_GROUPNAME",
    "DISPID_HWND",
    "DISPID_IMEMODE",
    "DISPID_KEYDOWN",
    "DISPID_KEYPRESS",
    "DISPID_KEYUP",
    "DISPID_LIST",
    "DISPID_LISTCOUNT",
    "DISPID_LISTINDEX",
    "DISPID_MAXLENGTH",
    "DISPID_MOUSEDOWN",
    "DISPID_MOUSEICON",
    "DISPID_MOUSEMOVE",
    "DISPID_MOUSEPOINTER",
    "DISPID_MOUSEUP",
    "DISPID_MULTILINE",
    "DISPID_MULTISELECT",
    "DISPID_NEWENUM",
    "DISPID_NUMBEROFCOLUMNS",
    "DISPID_NUMBEROFROWS",
    "DISPID_Name",
    "DISPID_Object",
    "DISPID_PASSWORDCHAR",
    "DISPID_PICTURE",
    "DISPID_PICT_HANDLE",
    "DISPID_PICT_HEIGHT",
    "DISPID_PICT_HPAL",
    "DISPID_PICT_RENDER",
    "DISPID_PICT_TYPE",
    "DISPID_PICT_WIDTH",
    "DISPID_PROPERTYPUT",
    "DISPID_Parent",
    "DISPID_READYSTATE",
    "DISPID_READYSTATECHANGE",
    "DISPID_REFRESH",
    "DISPID_REMOVEITEM",
    "DISPID_RIGHTTOLEFT",
    "DISPID_SCROLLBARS",
    "DISPID_SELECTED",
    "DISPID_SELLENGTH",
    "DISPID_SELSTART",
    "DISPID_SELTEXT",
    "DISPID_STARTENUM",
    "DISPID_TABKEYBEHAVIOR",
    "DISPID_TABSTOP",
    "DISPID_TEXT",
    "DISPID_THIS",
    "DISPID_TOPTOBOTTOM",
    "DISPID_UNKNOWN",
    "DISPID_VALID",
    "DISPID_VALUE",
    "DISPID_WORDWRAP",
    "DOCMISC",
    "DOCMISC_CANCREATEMULTIPLEVIEWS",
    "DOCMISC_CANTOPENEDIT",
    "DOCMISC_NOFILESUPPORT",
    "DOCMISC_SUPPORTCOMPLEXRECTANGLES",
    "DROPEFFECT",
    "DROPEFFECT_COPY",
    "DROPEFFECT_LINK",
    "DROPEFFECT_MOVE",
    "DROPEFFECT_NONE",
    "DROPEFFECT_SCROLL",
    "DVASPECTINFO",
    "DVASPECTINFOFLAG",
    "DVASPECTINFOFLAG_CANOPTIMIZE",
    "DVEXTENTINFO",
    "DVEXTENTMODE",
    "DVEXTENT_CONTENT",
    "DVEXTENT_INTEGRAL",
    "DispCallFunc",
    "DispGetIDsOfNames",
    "DispGetParam",
    "DispInvoke",
    "DoDragDrop",
    "DosDateTimeToVariantTime",
    "EDIT_LINKS_FLAGS",
    "ELF_DISABLECANCELLINK",
    "ELF_DISABLECHANGESOURCE",
    "ELF_DISABLEOPENSOURCE",
    "ELF_DISABLEUPDATENOW",
    "ELF_SHOWHELP",
    "EMBDHLP_CREATENOW",
    "EMBDHLP_DELAYCREATE",
    "EMBDHLP_FLAGS",
    "EMBDHLP_INPROC_HANDLER",
    "EMBDHLP_INPROC_SERVER",
    "ENUM_CONTROLS_WHICH_FLAGS",
    "FDEX_PROP_FLAGS",
    "FDEX_PROP_FLAGS_fdexPropCanCall",
    "FDEX_PROP_FLAGS_fdexPropCanConstruct",
    "FDEX_PROP_FLAGS_fdexPropCanGet",
    "FDEX_PROP_FLAGS_fdexPropCanPut",
    "FDEX_PROP_FLAGS_fdexPropCanPutRef",
    "FDEX_PROP_FLAGS_fdexPropCanSourceEvents",
    "FDEX_PROP_FLAGS_fdexPropCannotCall",
    "FDEX_PROP_FLAGS_fdexPropCannotConstruct",
    "FDEX_PROP_FLAGS_fdexPropCannotGet",
    "FDEX_PROP_FLAGS_fdexPropCannotPut",
    "FDEX_PROP_FLAGS_fdexPropCannotPutRef",
    "FDEX_PROP_FLAGS_fdexPropCannotSourceEvents",
    "FDEX_PROP_FLAGS_fdexPropDynamicType",
    "FDEX_PROP_FLAGS_fdexPropNoSideEffects",
    "FONTDESC",
    "GCW_WCH_SIBLING",
    "GC_WCH_ALL",
    "GC_WCH_CONTAINED",
    "GC_WCH_CONTAINER",
    "GC_WCH_FONLYAFTER",
    "GC_WCH_FONLYBEFORE",
    "GC_WCH_FREVERSEDIR",
    "GC_WCH_FSELECTED",
    "GC_WCH_SIBLING",
    "GUIDKIND",
    "GUIDKIND_DEFAULT_SOURCE_DISP_IID",
    "GUID_CHECKVALUEEXCLUSIVE",
    "GUID_COLOR",
    "GUID_FONTBOLD",
    "GUID_FONTITALIC",
    "GUID_FONTNAME",
    "GUID_FONTSIZE",
    "GUID_FONTSTRIKETHROUGH",
    "GUID_FONTUNDERSCORE",
    "GUID_HANDLE",
    "GUID_HIMETRIC",
    "GUID_OPTIONVALUEEXCLUSIVE",
    "GUID_TRISTATE",
    "GUID_XPOS",
    "GUID_XPOSPIXEL",
    "GUID_XSIZE",
    "GUID_XSIZEPIXEL",
    "GUID_YPOS",
    "GUID_YPOSPIXEL",
    "GUID_YSIZE",
    "GUID_YSIZEPIXEL",
    "GetActiveObject",
    "GetAltMonthNames",
    "GetRecordInfoFromGuids",
    "GetRecordInfoFromTypeInfo",
    "HITRESULT",
    "HITRESULT_CLOSE",
    "HITRESULT_HIT",
    "HITRESULT_OUTSIDE",
    "HITRESULT_TRANSPARENT",
    "HRGN_UserFree",
    "HRGN_UserFree64",
    "HRGN_UserMarshal",
    "HRGN_UserMarshal64",
    "HRGN_UserSize",
    "HRGN_UserSize64",
    "HRGN_UserUnmarshal",
    "HRGN_UserUnmarshal64",
    "IAdviseSinkEx",
    "ICanHandleException",
    "IClassFactory2",
    "IContinue",
    "IContinueCallback",
    "ICreateErrorInfo",
    "ICreateTypeInfo",
    "ICreateTypeInfo2",
    "ICreateTypeLib",
    "ICreateTypeLib2",
    "IDC_BZ_ICON",
    "IDC_BZ_MESSAGE1",
    "IDC_BZ_RETRY",
    "IDC_BZ_SWITCHTO",
    "IDC_CI_BROWSE",
    "IDC_CI_CURRENT",
    "IDC_CI_CURRENTICON",
    "IDC_CI_DEFAULT",
    "IDC_CI_DEFAULTICON",
    "IDC_CI_FROMFILE",
    "IDC_CI_FROMFILEEDIT",
    "IDC_CI_GROUP",
    "IDC_CI_ICONDISPLAY",
    "IDC_CI_ICONLIST",
    "IDC_CI_LABEL",
    "IDC_CI_LABELEDIT",
    "IDC_CV_ACTIVATEAS",
    "IDC_CV_ACTIVATELIST",
    "IDC_CV_CHANGEICON",
    "IDC_CV_CONVERTLIST",
    "IDC_CV_CONVERTTO",
    "IDC_CV_DISPLAYASICON",
    "IDC_CV_ICONDISPLAY",
    "IDC_CV_OBJECTTYPE",
    "IDC_CV_RESULTTEXT",
    "IDC_EL_AUTOMATIC",
    "IDC_EL_CANCELLINK",
    "IDC_EL_CHANGESOURCE",
    "IDC_EL_COL1",
    "IDC_EL_COL2",
    "IDC_EL_COL3",
    "IDC_EL_LINKSLISTBOX",
    "IDC_EL_LINKSOURCE",
    "IDC_EL_LINKTYPE",
    "IDC_EL_MANUAL",
    "IDC_EL_OPENSOURCE",
    "IDC_EL_UPDATENOW",
    "IDC_GP_CONVERT",
    "IDC_GP_OBJECTICON",
    "IDC_GP_OBJECTLOCATION",
    "IDC_GP_OBJECTNAME",
    "IDC_GP_OBJECTSIZE",
    "IDC_GP_OBJECTTYPE",
    "IDC_IO_ADDCONTROL",
    "IDC_IO_CHANGEICON",
    "IDC_IO_CONTROLTYPELIST",
    "IDC_IO_CREATEFROMFILE",
    "IDC_IO_CREATENEW",
    "IDC_IO_DISPLAYASICON",
    "IDC_IO_FILE",
    "IDC_IO_FILEDISPLAY",
    "IDC_IO_FILETEXT",
    "IDC_IO_FILETYPE",
    "IDC_IO_ICONDISPLAY",
    "IDC_IO_INSERTCONTROL",
    "IDC_IO_LINKFILE",
    "IDC_IO_OBJECTTYPELIST",
    "IDC_IO_OBJECTTYPETEXT",
    "IDC_IO_RESULTIMAGE",
    "IDC_IO_RESULTTEXT",
    "IDC_LP_AUTOMATIC",
    "IDC_LP_BREAKLINK",
    "IDC_LP_CHANGESOURCE",
    "IDC_LP_DATE",
    "IDC_LP_LINKSOURCE",
    "IDC_LP_MANUAL",
    "IDC_LP_OPENSOURCE",
    "IDC_LP_TIME",
    "IDC_LP_UPDATENOW",
    "IDC_OLEUIHELP",
    "IDC_PS_CHANGEICON",
    "IDC_PS_DISPLAYASICON",
    "IDC_PS_DISPLAYLIST",
    "IDC_PS_ICONDISPLAY",
    "IDC_PS_PASTE",
    "IDC_PS_PASTELINK",
    "IDC_PS_PASTELINKLIST",
    "IDC_PS_PASTELIST",
    "IDC_PS_RESULTIMAGE",
    "IDC_PS_RESULTTEXT",
    "IDC_PS_SOURCETEXT",
    "IDC_PU_CONVERT",
    "IDC_PU_ICON",
    "IDC_PU_LINKS",
    "IDC_PU_TEXT",
    "IDC_UL_METER",
    "IDC_UL_PERCENT",
    "IDC_UL_PROGRESS",
    "IDC_UL_STOP",
    "IDC_VP_ASICON",
    "IDC_VP_CHANGEICON",
    "IDC_VP_EDITABLE",
    "IDC_VP_ICONDISPLAY",
    "IDC_VP_PERCENT",
    "IDC_VP_RELATIVE",
    "IDC_VP_RESULTIMAGE",
    "IDC_VP_SCALETXT",
    "IDC_VP_SPIN",
    "IDD_BUSY",
    "IDD_CANNOTUPDATELINK",
    "IDD_CHANGEICON",
    "IDD_CHANGEICONBROWSE",
    "IDD_CHANGESOURCE",
    "IDD_CHANGESOURCE4",
    "IDD_CONVERT",
    "IDD_CONVERT4",
    "IDD_CONVERTONLY",
    "IDD_CONVERTONLY4",
    "IDD_EDITLINKS",
    "IDD_EDITLINKS4",
    "IDD_GNRLPROPS",
    "IDD_GNRLPROPS4",
    "IDD_INSERTFILEBROWSE",
    "IDD_INSERTOBJECT",
    "IDD_LINKPROPS",
    "IDD_LINKPROPS4",
    "IDD_LINKSOURCEUNAVAILABLE",
    "IDD_LINKTYPECHANGED",
    "IDD_LINKTYPECHANGEDA",
    "IDD_LINKTYPECHANGEDW",
    "IDD_OUTOFMEMORY",
    "IDD_PASTESPECIAL",
    "IDD_PASTESPECIAL4",
    "IDD_SERVERNOTFOUND",
    "IDD_SERVERNOTREG",
    "IDD_SERVERNOTREGA",
    "IDD_SERVERNOTREGW",
    "IDD_UPDATELINKS",
    "IDD_VIEWPROPS",
    "ID_BROWSE_ADDCONTROL",
    "ID_BROWSE_CHANGEICON",
    "ID_BROWSE_CHANGESOURCE",
    "ID_BROWSE_INSERTFILE",
    "ID_DEFAULTINST",
    "IDispError",
    "IDispatchEx",
    "IDropSource",
    "IDropSourceNotify",
    "IDropTarget",
    "IEnterpriseDropTarget",
    "IEnumOLEVERB",
    "IEnumOleDocumentViews",
    "IEnumOleUndoUnits",
    "IEnumVARIANT",
    "IFont",
    "IFontDisp",
    "IFontEventsDisp",
    "IGNOREMIME",
    "IGNOREMIME_PROMPT",
    "IGNOREMIME_TEXT",
    "IGetOleObject",
    "IGetVBAObject",
    "INSERT_OBJECT_FLAGS",
    "INSTALL_SCOPE_INVALID",
    "INSTALL_SCOPE_MACHINE",
    "INSTALL_SCOPE_USER",
    "INTERFACEDATA",
    "IOF_CHECKDISPLAYASICON",
    "IOF_CHECKLINK",
    "IOF_CREATEFILEOBJECT",
    "IOF_CREATELINKOBJECT",
    "IOF_CREATENEWOBJECT",
    "IOF_DISABLEDISPLAYASICON",
    "IOF_DISABLELINK",
    "IOF_HIDECHANGEICON",
    "IOF_SELECTCREATECONTROL",
    "IOF_SELECTCREATEFROMFILE",
    "IOF_SELECTCREATENEW",
    "IOF_SHOWHELP",
    "IOF_SHOWINSERTCONTROL",
    "IOF_VERIFYSERVERSEXIST",
    "IObjectIdentity",
    "IObjectWithSite",
    "IOleAdviseHolder",
    "IOleCache",
    "IOleCache2",
    "IOleCacheControl",
    "IOleClientSite",
    "IOleCommandTarget",
    "IOleContainer",
    "IOleControl",
    "IOleControlSite",
    "IOleDocument",
    "IOleDocumentSite",
    "IOleDocumentView",
    "IOleInPlaceActiveObject",
    "IOleInPlaceFrame",
    "IOleInPlaceObject",
    "IOleInPlaceObjectWindowless",
    "IOleInPlaceSite",
    "IOleInPlaceSiteEx",
    "IOleInPlaceSiteWindowless",
    "IOleInPlaceUIWindow",
    "IOleItemContainer",
    "IOleLink",
    "IOleObject",
    "IOleParentUndoUnit",
    "IOleUILinkContainerA",
    "IOleUILinkContainerW",
    "IOleUILinkInfoA",
    "IOleUILinkInfoW",
    "IOleUIObjInfoA",
    "IOleUIObjInfoW",
    "IOleUndoManager",
    "IOleUndoUnit",
    "IOleWindow",
    "IParseDisplayName",
    "IPerPropertyBrowsing",
    "IPersistPropertyBag",
    "IPersistPropertyBag2",
    "IPicture",
    "IPicture2",
    "IPictureDisp",
    "IPointerInactive",
    "IPrint",
    "IPropertyNotifySink",
    "IPropertyPage",
    "IPropertyPage2",
    "IPropertyPageSite",
    "IProtectFocus",
    "IProtectedModeMenuServices",
    "IProvideClassInfo",
    "IProvideClassInfo2",
    "IProvideMultipleClassInfo",
    "IProvideRuntimeContext",
    "IQuickActivate",
    "IRecordInfo",
    "ISimpleFrameSite",
    "ISpecifyPropertyPages",
    "ITypeChangeEvents",
    "ITypeFactory",
    "ITypeMarshal",
    "IVBFormat",
    "IVBGetControl",
    "IVariantChangeType",
    "IViewObject",
    "IViewObject2",
    "IViewObjectEx",
    "IZoomEvents",
    "IsAccelerator",
    "KEYMODIFIERS",
    "KEYMOD_ALT",
    "KEYMOD_CONTROL",
    "KEYMOD_SHIFT",
    "LHashValOfNameSys",
    "LHashValOfNameSysA",
    "LIBFLAGS",
    "LIBFLAG_FCONTROL",
    "LIBFLAG_FHASDISKIMAGE",
    "LIBFLAG_FHIDDEN",
    "LIBFLAG_FRESTRICTED",
    "LICINFO",
    "LOAD_PICTURE_FLAGS",
    "LOAD_TLB_AS_32BIT",
    "LOAD_TLB_AS_64BIT",
    "LOCALE_USE_NLS",
    "LPFNOLEUIHOOK",
    "LP_COLOR",
    "LP_DEFAULT",
    "LP_MONOCHROME",
    "LP_VGACOLOR",
    "LoadRegTypeLib",
    "LoadTypeLib",
    "LoadTypeLibEx",
    "MEDIAPLAYBACK_PAUSE",
    "MEDIAPLAYBACK_PAUSE_AND_SUSPEND",
    "MEDIAPLAYBACK_RESUME",
    "MEDIAPLAYBACK_RESUME_FROM_SUSPEND",
    "MEDIAPLAYBACK_STATE",
    "MEMBERID_NIL",
    "METHODDATA",
    "MK_ALT",
    "MSOCMDERR_E_CANCELED",
    "MSOCMDERR_E_DISABLED",
    "MSOCMDERR_E_FIRST",
    "MSOCMDERR_E_NOHELP",
    "MSOCMDERR_E_NOTSUPPORTED",
    "MSOCMDERR_E_UNKNOWNGROUP",
    "MULTICLASSINFO_FLAGS",
    "MULTICLASSINFO_GETIIDPRIMARY",
    "MULTICLASSINFO_GETIIDSOURCE",
    "MULTICLASSINFO_GETNUMRESERVEDDISPIDS",
    "MULTICLASSINFO_GETTYPEINFO",
    "NUMPARSE",
    "NUMPARSE_FLAGS",
    "NUMPRS_CURRENCY",
    "NUMPRS_DECIMAL",
    "NUMPRS_EXPONENT",
    "NUMPRS_HEX_OCT",
    "NUMPRS_INEXACT",
    "NUMPRS_LEADING_MINUS",
    "NUMPRS_LEADING_PLUS",
    "NUMPRS_LEADING_WHITE",
    "NUMPRS_NEG",
    "NUMPRS_PARENS",
    "NUMPRS_STD",
    "NUMPRS_THOUSANDS",
    "NUMPRS_TRAILING_MINUS",
    "NUMPRS_TRAILING_PLUS",
    "NUMPRS_TRAILING_WHITE",
    "NUMPRS_USE_ALL",
    "OBJECTDESCRIPTOR",
    "OBJECT_PROPERTIES_FLAGS",
    "OCM__BASE",
    "OCPFIPARAMS",
    "OF_GET",
    "OF_HANDLER",
    "OF_SET",
    "OLECLOSE",
    "OLECLOSE_NOSAVE",
    "OLECLOSE_PROMPTSAVE",
    "OLECLOSE_SAVEIFDIRTY",
    "OLECMD",
    "OLECMDARGINDEX_ACTIVEXINSTALL_CLSID",
    "OLECMDARGINDEX_ACTIVEXINSTALL_DISPLAYNAME",
    "OLECMDARGINDEX_ACTIVEXINSTALL_INSTALLSCOPE",
    "OLECMDARGINDEX_ACTIVEXINSTALL_PUBLISHER",
    "OLECMDARGINDEX_ACTIVEXINSTALL_SOURCEURL",
    "OLECMDARGINDEX_SHOWPAGEACTIONMENU_HWND",
    "OLECMDARGINDEX_SHOWPAGEACTIONMENU_X",
    "OLECMDARGINDEX_SHOWPAGEACTIONMENU_Y",
    "OLECMDERR_E_CANCELED",
    "OLECMDERR_E_DISABLED",
    "OLECMDERR_E_FIRST",
    "OLECMDERR_E_NOHELP",
    "OLECMDERR_E_NOTSUPPORTED",
    "OLECMDERR_E_UNKNOWNGROUP",
    "OLECMDEXECOPT",
    "OLECMDEXECOPT_DODEFAULT",
    "OLECMDEXECOPT_DONTPROMPTUSER",
    "OLECMDEXECOPT_PROMPTUSER",
    "OLECMDEXECOPT_SHOWHELP",
    "OLECMDF",
    "OLECMDF_DEFHIDEONCTXTMENU",
    "OLECMDF_ENABLED",
    "OLECMDF_INVISIBLE",
    "OLECMDF_LATCHED",
    "OLECMDF_NINCHED",
    "OLECMDF_SUPPORTED",
    "OLECMDID",
    "OLECMDIDF_BROWSERSTATE_BLOCKEDVERSION",
    "OLECMDIDF_BROWSERSTATE_DESKTOPHTMLDIALOG",
    "OLECMDIDF_BROWSERSTATE_EXTENSIONSOFF",
    "OLECMDIDF_BROWSERSTATE_IESECURITY",
    "OLECMDIDF_BROWSERSTATE_PROTECTEDMODE_OFF",
    "OLECMDIDF_BROWSERSTATE_REQUIRESACTIVEX",
    "OLECMDIDF_BROWSERSTATE_RESET",
    "OLECMDIDF_OPTICAL_ZOOM_NOLAYOUT",
    "OLECMDIDF_OPTICAL_ZOOM_NOPERSIST",
    "OLECMDIDF_OPTICAL_ZOOM_NOTRANSIENT",
    "OLECMDIDF_OPTICAL_ZOOM_RELOADFORNEWTAB",
    "OLECMDIDF_PAGEACTION_ACTIVEXDISALLOW",
    "OLECMDIDF_PAGEACTION_ACTIVEXINSTALL",
    "OLECMDIDF_PAGEACTION_ACTIVEXTRUSTFAIL",
    "OLECMDIDF_PAGEACTION_ACTIVEXUNSAFE",
    "OLECMDIDF_PAGEACTION_ACTIVEXUSERAPPROVAL",
    "OLECMDIDF_PAGEACTION_ACTIVEXUSERDISABLE",
    "OLECMDIDF_PAGEACTION_ACTIVEX_EPM_INCOMPATIBLE",
    "OLECMDIDF_PAGEACTION_EXTENSION_COMPAT_BLOCKED",
    "OLECMDIDF_PAGEACTION_FILEDOWNLOAD",
    "OLECMDIDF_PAGEACTION_GENERIC_STATE",
    "OLECMDIDF_PAGEACTION_INTRANETZONEREQUEST",
    "OLECMDIDF_PAGEACTION_INVALID_CERT",
    "OLECMDIDF_PAGEACTION_LOCALMACHINE",
    "OLECMDIDF_PAGEACTION_MIMETEXTPLAIN",
    "OLECMDIDF_PAGEACTION_MIXEDCONTENT",
    "OLECMDIDF_PAGEACTION_NORESETACTIVEX",
    "OLECMDIDF_PAGEACTION_POPUPALLOWED",
    "OLECMDIDF_PAGEACTION_POPUPWINDOW",
    "OLECMDIDF_PAGEACTION_PROTLOCKDOWNDENY",
    "OLECMDIDF_PAGEACTION_PROTLOCKDOWNINTERNET",
    "OLECMDIDF_PAGEACTION_PROTLOCKDOWNINTRANET",
    "OLECMDIDF_PAGEACTION_PROTLOCKDOWNLOCALMACHINE",
    "OLECMDIDF_PAGEACTION_PROTLOCKDOWNRESTRICTED",
    "OLECMDIDF_PAGEACTION_PROTLOCKDOWNTRUSTED",
    "OLECMDIDF_PAGEACTION_RESET",
    "OLECMDIDF_PAGEACTION_SCRIPTNAVIGATE",
    "OLECMDIDF_PAGEACTION_SCRIPTNAVIGATE_ACTIVEXINSTALL",
    "OLECMDIDF_PAGEACTION_SCRIPTNAVIGATE_ACTIVEXUSERAPPROVAL",
    "OLECMDIDF_PAGEACTION_SCRIPTPROMPT",
    "OLECMDIDF_PAGEACTION_SPOOFABLEIDNHOST",
    "OLECMDIDF_PAGEACTION_WPCBLOCKED",
    "OLECMDIDF_PAGEACTION_WPCBLOCKED_ACTIVEX",
    "OLECMDIDF_PAGEACTION_XSSFILTERED",
    "OLECMDIDF_REFRESH_CLEARUSERINPUT",
    "OLECMDIDF_REFRESH_COMPLETELY",
    "OLECMDIDF_REFRESH_CONTINUE",
    "OLECMDIDF_REFRESH_IFEXPIRED",
    "OLECMDIDF_REFRESH_LEVELMASK",
    "OLECMDIDF_REFRESH_NORMAL",
    "OLECMDIDF_REFRESH_NO_CACHE",
    "OLECMDIDF_REFRESH_PAGEACTION_ACTIVEXINSTALL",
    "OLECMDIDF_REFRESH_PAGEACTION_ALLOW_VERSION",
    "OLECMDIDF_REFRESH_PAGEACTION_FILEDOWNLOAD",
    "OLECMDIDF_REFRESH_PAGEACTION_INVALID_CERT",
    "OLECMDIDF_REFRESH_PAGEACTION_LOCALMACHINE",
    "OLECMDIDF_REFRESH_PAGEACTION_MIXEDCONTENT",
    "OLECMDIDF_REFRESH_PAGEACTION_POPUPWINDOW",
    "OLECMDIDF_REFRESH_PAGEACTION_PROTLOCKDOWNINTERNET",
    "OLECMDIDF_REFRESH_PAGEACTION_PROTLOCKDOWNINTRANET",
    "OLECMDIDF_REFRESH_PAGEACTION_PROTLOCKDOWNLOCALMACHINE",
    "OLECMDIDF_REFRESH_PAGEACTION_PROTLOCKDOWNRESTRICTED",
    "OLECMDIDF_REFRESH_PAGEACTION_PROTLOCKDOWNTRUSTED",
    "OLECMDIDF_REFRESH_PROMPTIFOFFLINE",
    "OLECMDIDF_REFRESH_RELOAD",
    "OLECMDIDF_REFRESH_SKIPBEFOREUNLOADEVENT",
    "OLECMDIDF_REFRESH_THROUGHSCRIPT",
    "OLECMDIDF_VIEWPORTMODE_EXCLUDE_VISUAL_BOTTOM",
    "OLECMDIDF_VIEWPORTMODE_EXCLUDE_VISUAL_BOTTOM_VALID",
    "OLECMDIDF_VIEWPORTMODE_FIXED_LAYOUT_WIDTH",
    "OLECMDIDF_VIEWPORTMODE_FIXED_LAYOUT_WIDTH_VALID",
    "OLECMDIDF_WINDOWSTATE_ENABLED",
    "OLECMDIDF_WINDOWSTATE_ENABLED_VALID",
    "OLECMDIDF_WINDOWSTATE_USERVISIBLE",
    "OLECMDIDF_WINDOWSTATE_USERVISIBLE_VALID",
    "OLECMDID_ACTIVEXINSTALLSCOPE",
    "OLECMDID_ADDTRAVELENTRY",
    "OLECMDID_ALLOWUILESSSAVEAS",
    "OLECMDID_BROWSERSTATEFLAG",
    "OLECMDID_CLEARSELECTION",
    "OLECMDID_CLOSE",
    "OLECMDID_COPY",
    "OLECMDID_CUT",
    "OLECMDID_DELETE",
    "OLECMDID_DONTDOWNLOADCSS",
    "OLECMDID_ENABLE_INTERACTION",
    "OLECMDID_ENABLE_VISIBILITY",
    "OLECMDID_EXITFULLSCREEN",
    "OLECMDID_FIND",
    "OLECMDID_FOCUSVIEWCONTROLS",
    "OLECMDID_FOCUSVIEWCONTROLSQUERY",
    "OLECMDID_GETPRINTTEMPLATE",
    "OLECMDID_GETUSERSCALABLE",
    "OLECMDID_GETZOOMRANGE",
    "OLECMDID_HIDETOOLBARS",
    "OLECMDID_HTTPEQUIV",
    "OLECMDID_HTTPEQUIV_DONE",
    "OLECMDID_LAYOUT_VIEWPORT_WIDTH",
    "OLECMDID_MEDIA_PLAYBACK",
    "OLECMDID_NEW",
    "OLECMDID_ONBEFOREUNLOAD",
    "OLECMDID_ONTOOLBARACTIVATED",
    "OLECMDID_ONUNLOAD",
    "OLECMDID_OPEN",
    "OLECMDID_OPTICAL_GETZOOMRANGE",
    "OLECMDID_OPTICAL_ZOOM",
    "OLECMDID_OPTICAL_ZOOMFLAG",
    "OLECMDID_PAGEACTIONBLOCKED",
    "OLECMDID_PAGEACTIONFLAG",
    "OLECMDID_PAGEACTIONUIQUERY",
    "OLECMDID_PAGEAVAILABLE",
    "OLECMDID_PAGESETUP",
    "OLECMDID_PASTE",
    "OLECMDID_PASTESPECIAL",
    "OLECMDID_POPSTATEEVENT",
    "OLECMDID_PREREFRESH",
    "OLECMDID_PRINT",
    "OLECMDID_PRINT2",
    "OLECMDID_PRINTPREVIEW",
    "OLECMDID_PRINTPREVIEW2",
    "OLECMDID_PROPERTIES",
    "OLECMDID_PROPERTYBAG2",
    "OLECMDID_REDO",
    "OLECMDID_REFRESH",
    "OLECMDID_REFRESHFLAG",
    "OLECMDID_SAVE",
    "OLECMDID_SAVEAS",
    "OLECMDID_SAVECOPYAS",
    "OLECMDID_SCROLLCOMPLETE",
    "OLECMDID_SELECTALL",
    "OLECMDID_SETDOWNLOADSTATE",
    "OLECMDID_SETFAVICON",
    "OLECMDID_SETPRINTTEMPLATE",
    "OLECMDID_SETPROGRESSMAX",
    "OLECMDID_SETPROGRESSPOS",
    "OLECMDID_SETPROGRESSTEXT",
    "OLECMDID_SETTITLE",
    "OLECMDID_SET_HOST_FULLSCREENMODE",
    "OLECMDID_SHOWFIND",
    "OLECMDID_SHOWMESSAGE",
    "OLECMDID_SHOWMESSAGE_BLOCKABLE",
    "OLECMDID_SHOWPAGEACTIONMENU",
    "OLECMDID_SHOWPAGESETUP",
    "OLECMDID_SHOWPRINT",
    "OLECMDID_SHOWSCRIPTERROR",
    "OLECMDID_SHOWTASKDLG",
    "OLECMDID_SHOWTASKDLG_BLOCKABLE",
    "OLECMDID_SPELL",
    "OLECMDID_STOP",
    "OLECMDID_STOPDOWNLOAD",
    "OLECMDID_UNDO",
    "OLECMDID_UPDATEBACKFORWARDSTATE",
    "OLECMDID_UPDATECOMMANDS",
    "OLECMDID_UPDATEPAGESTATUS",
    "OLECMDID_UPDATETRAVELENTRY",
    "OLECMDID_UPDATETRAVELENTRY_DATARECOVERY",
    "OLECMDID_UPDATE_CARET",
    "OLECMDID_USER_OPTICAL_ZOOM",
    "OLECMDID_VIEWPORT_MODE",
    "OLECMDID_VIEWPORT_MODE_FLAG",
    "OLECMDID_VISUAL_VIEWPORT_EXCLUDE_BOTTOM",
    "OLECMDID_WINDOWSTATECHANGED",
    "OLECMDID_WINDOWSTATE_FLAG",
    "OLECMDID_ZOOM",
    "OLECMDTEXT",
    "OLECMDTEXTF",
    "OLECMDTEXTF_NAME",
    "OLECMDTEXTF_NONE",
    "OLECMDTEXTF_STATUS",
    "OLECMD_TASKDLGID_ONBEFOREUNLOAD",
    "OLECONTF",
    "OLECONTF_EMBEDDINGS",
    "OLECONTF_LINKS",
    "OLECONTF_ONLYIFRUNNING",
    "OLECONTF_ONLYUSER",
    "OLECONTF_OTHERS",
    "OLECREATE",
    "OLECREATE_LEAVERUNNING",
    "OLECREATE_ZERO",
    "OLEDCFLAGS",
    "OLEDC_NODRAW",
    "OLEDC_OFFSCREEN",
    "OLEDC_PAINTBKGND",
    "OLEGETMONIKER",
    "OLEGETMONIKER_FORCEASSIGN",
    "OLEGETMONIKER_ONLYIFTHERE",
    "OLEGETMONIKER_TEMPFORUSER",
    "OLEGETMONIKER_UNASSIGN",
    "OLEINPLACEFRAMEINFO",
    "OLEIVERB",
    "OLEIVERB_DISCARDUNDOSTATE",
    "OLEIVERB_HIDE",
    "OLEIVERB_INPLACEACTIVATE",
    "OLEIVERB_OPEN",
    "OLEIVERB_PRIMARY",
    "OLEIVERB_PROPERTIES",
    "OLEIVERB_SHOW",
    "OLEIVERB_UIACTIVATE",
    "OLELINKBIND",
    "OLELINKBIND_EVENIFCLASSDIFF",
    "OLEMENUGROUPWIDTHS",
    "OLEMISC",
    "OLEMISC_ACTIVATEWHENVISIBLE",
    "OLEMISC_ACTSLIKEBUTTON",
    "OLEMISC_ACTSLIKELABEL",
    "OLEMISC_ALIGNABLE",
    "OLEMISC_ALWAYSRUN",
    "OLEMISC_CANLINKBYOLE1",
    "OLEMISC_CANTLINKINSIDE",
    "OLEMISC_IGNOREACTIVATEWHENVISIBLE",
    "OLEMISC_IMEMODE",
    "OLEMISC_INSERTNOTREPLACE",
    "OLEMISC_INSIDEOUT",
    "OLEMISC_INVISIBLEATRUNTIME",
    "OLEMISC_ISLINKOBJECT",
    "OLEMISC_NOUIACTIVATE",
    "OLEMISC_ONLYICONIC",
    "OLEMISC_RECOMPOSEONRESIZE",
    "OLEMISC_RENDERINGISDEVICEINDEPENDENT",
    "OLEMISC_SETCLIENTSITEFIRST",
    "OLEMISC_SIMPLEFRAME",
    "OLEMISC_STATIC",
    "OLEMISC_SUPPORTSMULTILEVELUNDO",
    "OLEMISC_WANTSTOMENUMERGE",
    "OLERENDER",
    "OLERENDER_ASIS",
    "OLERENDER_DRAW",
    "OLERENDER_FORMAT",
    "OLERENDER_NONE",
    "OLESTDDELIM",
    "OLEUIBUSYA",
    "OLEUIBUSYW",
    "OLEUICHANGEICONA",
    "OLEUICHANGEICONW",
    "OLEUICHANGESOURCEA",
    "OLEUICHANGESOURCEW",
    "OLEUICONVERTA",
    "OLEUICONVERTW",
    "OLEUIEDITLINKSA",
    "OLEUIEDITLINKSW",
    "OLEUIGNRLPROPSA",
    "OLEUIGNRLPROPSW",
    "OLEUIINSERTOBJECTA",
    "OLEUIINSERTOBJECTW",
    "OLEUILINKPROPSA",
    "OLEUILINKPROPSW",
    "OLEUIOBJECTPROPSA",
    "OLEUIOBJECTPROPSW",
    "OLEUIPASTEENTRYA",
    "OLEUIPASTEENTRYW",
    "OLEUIPASTEFLAG",
    "OLEUIPASTESPECIALA",
    "OLEUIPASTESPECIALW",
    "OLEUIPASTE_ENABLEICON",
    "OLEUIPASTE_LINKANYTYPE",
    "OLEUIPASTE_LINKTYPE1",
    "OLEUIPASTE_LINKTYPE2",
    "OLEUIPASTE_LINKTYPE3",
    "OLEUIPASTE_LINKTYPE4",
    "OLEUIPASTE_LINKTYPE5",
    "OLEUIPASTE_LINKTYPE6",
    "OLEUIPASTE_LINKTYPE7",
    "OLEUIPASTE_LINKTYPE8",
    "OLEUIPASTE_PASTE",
    "OLEUIPASTE_PASTEONLY",
    "OLEUIVIEWPROPSA",
    "OLEUIVIEWPROPSW",
    "OLEUI_BZERR_HTASKINVALID",
    "OLEUI_BZ_CALLUNBLOCKED",
    "OLEUI_BZ_RETRYSELECTED",
    "OLEUI_BZ_SWITCHTOSELECTED",
    "OLEUI_CANCEL",
    "OLEUI_CIERR_MUSTHAVECLSID",
    "OLEUI_CIERR_MUSTHAVECURRENTMETAFILE",
    "OLEUI_CIERR_SZICONEXEINVALID",
    "OLEUI_CSERR_FROMNOTNULL",
    "OLEUI_CSERR_LINKCNTRINVALID",
    "OLEUI_CSERR_LINKCNTRNULL",
    "OLEUI_CSERR_SOURCEINVALID",
    "OLEUI_CSERR_SOURCENULL",
    "OLEUI_CSERR_SOURCEPARSEERROR",
    "OLEUI_CSERR_SOURCEPARSERROR",
    "OLEUI_CSERR_TONOTNULL",
    "OLEUI_CTERR_CBFORMATINVALID",
    "OLEUI_CTERR_CLASSIDINVALID",
    "OLEUI_CTERR_DVASPECTINVALID",
    "OLEUI_CTERR_HMETAPICTINVALID",
    "OLEUI_CTERR_STRINGINVALID",
    "OLEUI_ELERR_LINKCNTRINVALID",
    "OLEUI_ELERR_LINKCNTRNULL",
    "OLEUI_ERR_CBSTRUCTINCORRECT",
    "OLEUI_ERR_DIALOGFAILURE",
    "OLEUI_ERR_FINDTEMPLATEFAILURE",
    "OLEUI_ERR_GLOBALMEMALLOC",
    "OLEUI_ERR_HINSTANCEINVALID",
    "OLEUI_ERR_HRESOURCEINVALID",
    "OLEUI_ERR_HWNDOWNERINVALID",
    "OLEUI_ERR_LOADSTRING",
    "OLEUI_ERR_LOADTEMPLATEFAILURE",
    "OLEUI_ERR_LOCALMEMALLOC",
    "OLEUI_ERR_LPFNHOOKINVALID",
    "OLEUI_ERR_LPSZCAPTIONINVALID",
    "OLEUI_ERR_LPSZTEMPLATEINVALID",
    "OLEUI_ERR_OLEMEMALLOC",
    "OLEUI_ERR_STANDARDMAX",
    "OLEUI_ERR_STANDARDMIN",
    "OLEUI_ERR_STRUCTUREINVALID",
    "OLEUI_ERR_STRUCTURENULL",
    "OLEUI_FALSE",
    "OLEUI_GPERR_CBFORMATINVALID",
    "OLEUI_GPERR_CLASSIDINVALID",
    "OLEUI_GPERR_LPCLSIDEXCLUDEINVALID",
    "OLEUI_GPERR_STRINGINVALID",
    "OLEUI_IOERR_ARRLINKTYPESINVALID",
    "OLEUI_IOERR_ARRPASTEENTRIESINVALID",
    "OLEUI_IOERR_CCHFILEINVALID",
    "OLEUI_IOERR_HICONINVALID",
    "OLEUI_IOERR_LPCLSIDEXCLUDEINVALID",
    "OLEUI_IOERR_LPFORMATETCINVALID",
    "OLEUI_IOERR_LPIOLECLIENTSITEINVALID",
    "OLEUI_IOERR_LPISTORAGEINVALID",
    "OLEUI_IOERR_LPSZFILEINVALID",
    "OLEUI_IOERR_LPSZLABELINVALID",
    "OLEUI_IOERR_PPVOBJINVALID",
    "OLEUI_IOERR_SCODEHASERROR",
    "OLEUI_IOERR_SRCDATAOBJECTINVALID",
    "OLEUI_LPERR_LINKCNTRINVALID",
    "OLEUI_LPERR_LINKCNTRNULL",
    "OLEUI_OK",
    "OLEUI_OPERR_DLGPROCNOTNULL",
    "OLEUI_OPERR_INVALIDPAGES",
    "OLEUI_OPERR_LINKINFOINVALID",
    "OLEUI_OPERR_LPARAMNOTZERO",
    "OLEUI_OPERR_NOTSUPPORTED",
    "OLEUI_OPERR_OBJINFOINVALID",
    "OLEUI_OPERR_PAGESINCORRECT",
    "OLEUI_OPERR_PROPERTYSHEET",
    "OLEUI_OPERR_PROPSHEETINVALID",
    "OLEUI_OPERR_PROPSHEETNULL",
    "OLEUI_OPERR_PROPSINVALID",
    "OLEUI_OPERR_SUBPROPINVALID",
    "OLEUI_OPERR_SUBPROPNULL",
    "OLEUI_OPERR_SUPPROP",
    "OLEUI_PSERR_CLIPBOARDCHANGED",
    "OLEUI_PSERR_GETCLIPBOARDFAILED",
    "OLEUI_QUERY_GETCLASSID",
    "OLEUI_QUERY_LINKBROKEN",
    "OLEUI_SUCCESS",
    "OLEUI_VPERR_DVASPECTINVALID",
    "OLEUI_VPERR_METAPICTINVALID",
    "OLEUPDATE",
    "OLEUPDATE_ALWAYS",
    "OLEUPDATE_ONCALL",
    "OLEVERB",
    "OLEVERBATTRIB",
    "OLEVERBATTRIB_NEVERDIRTIES",
    "OLEVERBATTRIB_ONCONTAINERMENU",
    "OLEVERB_PRIMARY",
    "OLEWHICHMK",
    "OLEWHICHMK_CONTAINER",
    "OLEWHICHMK_OBJFULL",
    "OLEWHICHMK_OBJREL",
    "OLE_HANDLE",
    "OLE_TRISTATE",
    "OLE_TRISTATE_triChecked",
    "OLE_TRISTATE_triGray",
    "OLE_TRISTATE_triUnchecked",
    "OPF_DISABLECONVERT",
    "OPF_NOFILLDEFAULT",
    "OPF_OBJECTISLINK",
    "OPF_SHOWHELP",
    "OT_EMBEDDED",
    "OT_LINK",
    "OT_STATIC",
    "OaBuildVersion",
    "OaEnablePerUserTLibRegistration",
    "OleBuildVersion",
    "OleCreate",
    "OleCreateDefaultHandler",
    "OleCreateEmbeddingHelper",
    "OleCreateEx",
    "OleCreateFontIndirect",
    "OleCreateFromData",
    "OleCreateFromDataEx",
    "OleCreateFromFile",
    "OleCreateFromFileEx",
    "OleCreateLink",
    "OleCreateLinkEx",
    "OleCreateLinkFromData",
    "OleCreateLinkFromDataEx",
    "OleCreateLinkToFile",
    "OleCreateLinkToFileEx",
    "OleCreateMenuDescriptor",
    "OleCreatePictureIndirect",
    "OleCreatePropertyFrame",
    "OleCreatePropertyFrameIndirect",
    "OleCreateStaticFromData",
    "OleDestroyMenuDescriptor",
    "OleDoAutoConvert",
    "OleDraw",
    "OleDuplicateData",
    "OleFlushClipboard",
    "OleGetAutoConvert",
    "OleGetClipboard",
    "OleGetClipboardWithEnterpriseInfo",
    "OleGetIconOfClass",
    "OleGetIconOfFile",
    "OleIconToCursor",
    "OleInitialize",
    "OleIsCurrentClipboard",
    "OleIsRunning",
    "OleLoad",
    "OleLoadFromStream",
    "OleLoadPicture",
    "OleLoadPictureEx",
    "OleLoadPictureFile",
    "OleLoadPictureFileEx",
    "OleLoadPicturePath",
    "OleLockRunning",
    "OleMetafilePictFromIconAndLabel",
    "OleNoteObjectVisible",
    "OleQueryCreateFromData",
    "OleQueryLinkFromData",
    "OleRegEnumFormatEtc",
    "OleRegEnumVerbs",
    "OleRegGetMiscStatus",
    "OleRegGetUserType",
    "OleRun",
    "OleSave",
    "OleSavePictureFile",
    "OleSaveToStream",
    "OleSetAutoConvert",
    "OleSetClipboard",
    "OleSetContainedObject",
    "OleSetMenuDescriptor",
    "OleTranslateAccelerator",
    "OleTranslateColor",
    "OleUIAddVerbMenuA",
    "OleUIAddVerbMenuW",
    "OleUIBusyA",
    "OleUIBusyW",
    "OleUICanConvertOrActivateAs",
    "OleUIChangeIconA",
    "OleUIChangeIconW",
    "OleUIChangeSourceA",
    "OleUIChangeSourceW",
    "OleUIConvertA",
    "OleUIConvertW",
    "OleUIEditLinksA",
    "OleUIEditLinksW",
    "OleUIInsertObjectA",
    "OleUIInsertObjectW",
    "OleUIObjectPropertiesA",
    "OleUIObjectPropertiesW",
    "OleUIPasteSpecialA",
    "OleUIPasteSpecialW",
    "OleUIPromptUserA",
    "OleUIPromptUserW",
    "OleUIUpdateLinksA",
    "OleUIUpdateLinksW",
    "OleUninitialize",
    "PAGEACTION_UI",
    "PAGEACTION_UI_DEFAULT",
    "PAGEACTION_UI_MODAL",
    "PAGEACTION_UI_MODELESS",
    "PAGEACTION_UI_SILENT",
    "PAGERANGE",
    "PAGESET",
    "PARAMDATA",
    "PARAMDESC",
    "PARAMDESCEX",
    "PARAMFLAGS",
    "PARAMFLAG_FHASCUSTDATA",
    "PARAMFLAG_FHASDEFAULT",
    "PARAMFLAG_FIN",
    "PARAMFLAG_FLCID",
    "PARAMFLAG_FOPT",
    "PARAMFLAG_FOUT",
    "PARAMFLAG_FRETVAL",
    "PARAMFLAG_NONE",
    "PASTE_SPECIAL_FLAGS",
    "PERPROP_E_FIRST",
    "PERPROP_E_LAST",
    "PERPROP_E_NOPAGEAVAILABLE",
    "PERPROP_S_FIRST",
    "PERPROP_S_LAST",
    "PICTDESC",
    "PICTUREATTRIBUTES",
    "PICTURE_SCALABLE",
    "PICTURE_TRANSPARENT",
    "PICTYPE",
    "PICTYPE_BITMAP",
    "PICTYPE_ENHMETAFILE",
    "PICTYPE_ICON",
    "PICTYPE_METAFILE",
    "PICTYPE_NONE",
    "PICTYPE_UNINITIALIZED",
    "POINTERINACTIVE",
    "POINTERINACTIVE_ACTIVATEONDRAG",
    "POINTERINACTIVE_ACTIVATEONENTRY",
    "POINTERINACTIVE_DEACTIVATEONLEAVE",
    "POINTF",
    "PRINTFLAG",
    "PRINTFLAG_DONTACTUALLYPRINT",
    "PRINTFLAG_FORCEPROPERTIES",
    "PRINTFLAG_MAYBOTHERUSER",
    "PRINTFLAG_PRINTTOFILE",
    "PRINTFLAG_PROMPTUSER",
    "PRINTFLAG_RECOMPOSETODEVICE",
    "PRINTFLAG_USERMAYCHANGEPRINTER",
    "PROPBAG2_TYPE",
    "PROPBAG2_TYPE_DATA",
    "PROPBAG2_TYPE_MONIKER",
    "PROPBAG2_TYPE_OBJECT",
    "PROPBAG2_TYPE_STORAGE",
    "PROPBAG2_TYPE_STREAM",
    "PROPBAG2_TYPE_UNDEFINED",
    "PROPBAG2_TYPE_URL",
    "PROPPAGEINFO",
    "PROPPAGESTATUS",
    "PROPPAGESTATUS_CLEAN",
    "PROPPAGESTATUS_DIRTY",
    "PROPPAGESTATUS_VALIDATE",
    "PROP_HWND_CHGICONDLG",
    "PSF_CHECKDISPLAYASICON",
    "PSF_DISABLEDISPLAYASICON",
    "PSF_HIDECHANGEICON",
    "PSF_NOREFRESHDATAOBJECT",
    "PSF_SELECTPASTE",
    "PSF_SELECTPASTELINK",
    "PSF_SHOWHELP",
    "PSF_STAYONCLIPBOARDCHANGE",
    "PS_MAXLINKTYPES",
    "QACONTAINER",
    "QACONTAINERFLAGS",
    "QACONTAINER_AUTOCLIP",
    "QACONTAINER_DISPLAYASDEFAULT",
    "QACONTAINER_MESSAGEREFLECT",
    "QACONTAINER_SHOWGRABHANDLES",
    "QACONTAINER_SHOWHATCHING",
    "QACONTAINER_SUPPORTSMNEMONICS",
    "QACONTAINER_UIDEAD",
    "QACONTAINER_USERMODE",
    "QACONTROL",
    "QueryPathOfRegTypeLib",
    "READYSTATE",
    "READYSTATE_COMPLETE",
    "READYSTATE_INTERACTIVE",
    "READYSTATE_LOADED",
    "READYSTATE_LOADING",
    "READYSTATE_UNINITIALIZED",
    "REGKIND",
    "REGKIND_DEFAULT",
    "REGKIND_NONE",
    "REGKIND_REGISTER",
    "RegisterActiveObject",
    "RegisterDragDrop",
    "RegisterTypeLib",
    "RegisterTypeLibForUser",
    "ReleaseStgMedium",
    "RevokeActiveObject",
    "RevokeDragDrop",
    "SAFEARRAYUNION",
    "SAFEARR_BRECORD",
    "SAFEARR_BSTR",
    "SAFEARR_DISPATCH",
    "SAFEARR_HAVEIID",
    "SAFEARR_UNKNOWN",
    "SAFEARR_VARIANT",
    "SELFREG_E_CLASS",
    "SELFREG_E_FIRST",
    "SELFREG_E_LAST",
    "SELFREG_E_TYPELIB",
    "SELFREG_S_FIRST",
    "SELFREG_S_LAST",
    "SF_BSTR",
    "SF_DISPATCH",
    "SF_ERROR",
    "SF_HAVEIID",
    "SF_I1",
    "SF_I2",
    "SF_I4",
    "SF_I8",
    "SF_RECORD",
    "SF_TYPE",
    "SF_UNKNOWN",
    "SF_VARIANT",
    "SID_GetCaller",
    "SID_ProvideRuntimeContext",
    "SID_VariantConversion",
    "STDOLE2_LCID",
    "STDOLE2_MAJORVERNUM",
    "STDOLE2_MINORVERNUM",
    "STDOLE_LCID",
    "STDOLE_MAJORVERNUM",
    "STDOLE_MINORVERNUM",
    "STDOLE_TLB",
    "STDTYPE_TLB",
    "SZOLEUI_MSG_ADDCONTROL",
    "SZOLEUI_MSG_BROWSE",
    "SZOLEUI_MSG_BROWSE_OFN",
    "SZOLEUI_MSG_CHANGEICON",
    "SZOLEUI_MSG_CHANGESOURCE",
    "SZOLEUI_MSG_CLOSEBUSYDIALOG",
    "SZOLEUI_MSG_CONVERT",
    "SZOLEUI_MSG_ENDDIALOG",
    "SZOLEUI_MSG_HELP",
    "SafeArrayAccessData",
    "SafeArrayAddRef",
    "SafeArrayAllocData",
    "SafeArrayAllocDescriptor",
    "SafeArrayAllocDescriptorEx",
    "SafeArrayCopy",
    "SafeArrayCopyData",
    "SafeArrayCreate",
    "SafeArrayCreateEx",
    "SafeArrayCreateVector",
    "SafeArrayCreateVectorEx",
    "SafeArrayDestroy",
    "SafeArrayDestroyData",
    "SafeArrayDestroyDescriptor",
    "SafeArrayGetDim",
    "SafeArrayGetElement",
    "SafeArrayGetElemsize",
    "SafeArrayGetIID",
    "SafeArrayGetLBound",
    "SafeArrayGetRecordInfo",
    "SafeArrayGetUBound",
    "SafeArrayGetVartype",
    "SafeArrayLock",
    "SafeArrayPtrOfIndex",
    "SafeArrayPutElement",
    "SafeArrayRedim",
    "SafeArrayReleaseData",
    "SafeArrayReleaseDescriptor",
    "SafeArraySetIID",
    "SafeArraySetRecordInfo",
    "SafeArrayUnaccessData",
    "SafeArrayUnlock",
    "SystemTimeToVariantTime",
    "TIFLAGS_EXTENDDISPATCHONLY",
    "TYPEFLAGS",
    "TYPEFLAG_FAGGREGATABLE",
    "TYPEFLAG_FAPPOBJECT",
    "TYPEFLAG_FCANCREATE",
    "TYPEFLAG_FCONTROL",
    "TYPEFLAG_FDISPATCHABLE",
    "TYPEFLAG_FDUAL",
    "TYPEFLAG_FHIDDEN",
    "TYPEFLAG_FLICENSED",
    "TYPEFLAG_FNONEXTENSIBLE",
    "TYPEFLAG_FOLEAUTOMATION",
    "TYPEFLAG_FPREDECLID",
    "TYPEFLAG_FPROXY",
    "TYPEFLAG_FREPLACEABLE",
    "TYPEFLAG_FRESTRICTED",
    "TYPEFLAG_FREVERSEBIND",
    "UASFLAGS",
    "UAS_BLOCKED",
    "UAS_MASK",
    "UAS_NOPARENTENABLE",
    "UAS_NORMAL",
    "UDATE",
    "UI_CONVERT_FLAGS",
    "UPDFCACHE_ALL",
    "UPDFCACHE_ALLBUTNODATACACHE",
    "UPDFCACHE_FLAGS",
    "UPDFCACHE_IFBLANK",
    "UPDFCACHE_IFBLANKORONSAVECACHE",
    "UPDFCACHE_NODATACACHE",
    "UPDFCACHE_NORMALCACHE",
    "UPDFCACHE_ONLYIFBLANK",
    "UPDFCACHE_ONSAVECACHE",
    "UPDFCACHE_ONSTOPCACHE",
    "USERCLASSTYPE",
    "USERCLASSTYPE_APPNAME",
    "USERCLASSTYPE_FULL",
    "USERCLASSTYPE_SHORT",
    "UnRegisterTypeLib",
    "UnRegisterTypeLibForUser",
    "VARCMP",
    "VARCMP_EQ",
    "VARCMP_GT",
    "VARCMP_LT",
    "VARCMP_NULL",
    "VARFORMAT_FIRST_DAY",
    "VARFORMAT_FIRST_DAY_FRIDAY",
    "VARFORMAT_FIRST_DAY_MONDAY",
    "VARFORMAT_FIRST_DAY_SATURDAY",
    "VARFORMAT_FIRST_DAY_SUNDAY",
    "VARFORMAT_FIRST_DAY_SYSTEMDEFAULT",
    "VARFORMAT_FIRST_DAY_THURSDAY",
    "VARFORMAT_FIRST_DAY_TUESDAY",
    "VARFORMAT_FIRST_DAY_WEDNESDAY",
    "VARFORMAT_FIRST_WEEK",
    "VARFORMAT_FIRST_WEEK_CONTAINS_JANUARY_FIRST",
    "VARFORMAT_FIRST_WEEK_HAS_SEVEN_DAYS",
    "VARFORMAT_FIRST_WEEK_LARGER_HALF_IN_CURRENT_YEAR",
    "VARFORMAT_FIRST_WEEK_SYSTEMDEFAULT",
    "VARFORMAT_GROUP",
    "VARFORMAT_GROUP_NOTTHOUSANDS",
    "VARFORMAT_GROUP_SYSTEMDEFAULT",
    "VARFORMAT_GROUP_THOUSANDS",
    "VARFORMAT_LEADING_DIGIT",
    "VARFORMAT_LEADING_DIGIT_INCLUDED",
    "VARFORMAT_LEADING_DIGIT_NOTINCLUDED",
    "VARFORMAT_LEADING_DIGIT_SYSTEMDEFAULT",
    "VARFORMAT_NAMED_FORMAT",
    "VARFORMAT_NAMED_FORMAT_GENERALDATE",
    "VARFORMAT_NAMED_FORMAT_LONGDATE",
    "VARFORMAT_NAMED_FORMAT_LONGTIME",
    "VARFORMAT_NAMED_FORMAT_SHORTDATE",
    "VARFORMAT_NAMED_FORMAT_SHORTTIME",
    "VARFORMAT_PARENTHESES",
    "VARFORMAT_PARENTHESES_NOTUSED",
    "VARFORMAT_PARENTHESES_SYSTEMDEFAULT",
    "VARFORMAT_PARENTHESES_USED",
    "VARIANT_ALPHABOOL",
    "VARIANT_CALENDAR_GREGORIAN",
    "VARIANT_CALENDAR_HIJRI",
    "VARIANT_CALENDAR_THAI",
    "VARIANT_LOCALBOOL",
    "VARIANT_NOUSEROVERRIDE",
    "VARIANT_NOVALUEPROP",
    "VARIANT_USE_NLS",
    "VAR_CALENDAR_GREGORIAN",
    "VAR_CALENDAR_HIJRI",
    "VAR_CALENDAR_THAI",
    "VAR_DATEVALUEONLY",
    "VAR_FORMAT_NOSUBSTITUTE",
    "VAR_FOURDIGITYEARS",
    "VAR_LOCALBOOL",
    "VAR_TIMEVALUEONLY",
    "VAR_VALIDDATE",
    "VIEWSTATUS",
    "VIEWSTATUS_3DSURFACE",
    "VIEWSTATUS_DVASPECTOPAQUE",
    "VIEWSTATUS_DVASPECTTRANSPARENT",
    "VIEWSTATUS_OPAQUE",
    "VIEWSTATUS_SOLIDBKGND",
    "VIEWSTATUS_SURFACE",
    "VIEW_OBJECT_PROPERTIES_FLAGS",
    "VPF_DISABLERELATIVE",
    "VPF_DISABLESCALE",
    "VPF_SELECTRELATIVE",
    "VTDATEGRE_MAX",
    "VTDATEGRE_MIN",
    "VT_BLOB_PROPSET",
    "VT_STORED_PROPSET",
    "VT_STREAMED_PROPSET",
    "VT_VERBOSE_ENUM",
    "VarAbs",
    "VarAdd",
    "VarAnd",
    "VarBoolFromCy",
    "VarBoolFromDate",
    "VarBoolFromDec",
    "VarBoolFromDisp",
    "VarBoolFromI1",
    "VarBoolFromI2",
    "VarBoolFromI4",
    "VarBoolFromI8",
    "VarBoolFromR4",
    "VarBoolFromR8",
    "VarBoolFromStr",
    "VarBoolFromUI1",
    "VarBoolFromUI2",
    "VarBoolFromUI4",
    "VarBoolFromUI8",
    "VarBstrCat",
    "VarBstrCmp",
    "VarBstrFromBool",
    "VarBstrFromCy",
    "VarBstrFromDate",
    "VarBstrFromDec",
    "VarBstrFromDisp",
    "VarBstrFromI1",
    "VarBstrFromI2",
    "VarBstrFromI4",
    "VarBstrFromI8",
    "VarBstrFromR4",
    "VarBstrFromR8",
    "VarBstrFromUI1",
    "VarBstrFromUI2",
    "VarBstrFromUI4",
    "VarBstrFromUI8",
    "VarCat",
    "VarCmp",
    "VarCyAbs",
    "VarCyAdd",
    "VarCyCmp",
    "VarCyCmpR8",
    "VarCyFix",
    "VarCyFromBool",
    "VarCyFromDate",
    "VarCyFromDec",
    "VarCyFromDisp",
    "VarCyFromI1",
    "VarCyFromI2",
    "VarCyFromI4",
    "VarCyFromI8",
    "VarCyFromR4",
    "VarCyFromR8",
    "VarCyFromStr",
    "VarCyFromUI1",
    "VarCyFromUI2",
    "VarCyFromUI4",
    "VarCyFromUI8",
    "VarCyInt",
    "VarCyMul",
    "VarCyMulI4",
    "VarCyMulI8",
    "VarCyNeg",
    "VarCyRound",
    "VarCySub",
    "VarDateFromBool",
    "VarDateFromCy",
    "VarDateFromDec",
    "VarDateFromDisp",
    "VarDateFromI1",
    "VarDateFromI2",
    "VarDateFromI4",
    "VarDateFromI8",
    "VarDateFromR4",
    "VarDateFromR8",
    "VarDateFromStr",
    "VarDateFromUI1",
    "VarDateFromUI2",
    "VarDateFromUI4",
    "VarDateFromUI8",
    "VarDateFromUdate",
    "VarDateFromUdateEx",
    "VarDecAbs",
    "VarDecAdd",
    "VarDecCmp",
    "VarDecCmpR8",
    "VarDecDiv",
    "VarDecFix",
    "VarDecFromBool",
    "VarDecFromCy",
    "VarDecFromDate",
    "VarDecFromDisp",
    "VarDecFromI1",
    "VarDecFromI2",
    "VarDecFromI4",
    "VarDecFromI8",
    "VarDecFromR4",
    "VarDecFromR8",
    "VarDecFromStr",
    "VarDecFromUI1",
    "VarDecFromUI2",
    "VarDecFromUI4",
    "VarDecFromUI8",
    "VarDecInt",
    "VarDecMul",
    "VarDecNeg",
    "VarDecRound",
    "VarDecSub",
    "VarDiv",
    "VarEqv",
    "VarFix",
    "VarFormat",
    "VarFormatCurrency",
    "VarFormatDateTime",
    "VarFormatFromTokens",
    "VarFormatNumber",
    "VarFormatPercent",
    "VarI1FromBool",
    "VarI1FromCy",
    "VarI1FromDate",
    "VarI1FromDec",
    "VarI1FromDisp",
    "VarI1FromI2",
    "VarI1FromI4",
    "VarI1FromI8",
    "VarI1FromR4",
    "VarI1FromR8",
    "VarI1FromStr",
    "VarI1FromUI1",
    "VarI1FromUI2",
    "VarI1FromUI4",
    "VarI1FromUI8",
    "VarI2FromBool",
    "VarI2FromCy",
    "VarI2FromDate",
    "VarI2FromDec",
    "VarI2FromDisp",
    "VarI2FromI1",
    "VarI2FromI4",
    "VarI2FromI8",
    "VarI2FromR4",
    "VarI2FromR8",
    "VarI2FromStr",
    "VarI2FromUI1",
    "VarI2FromUI2",
    "VarI2FromUI4",
    "VarI2FromUI8",
    "VarI4FromBool",
    "VarI4FromCy",
    "VarI4FromDate",
    "VarI4FromDec",
    "VarI4FromDisp",
    "VarI4FromI1",
    "VarI4FromI2",
    "VarI4FromI8",
    "VarI4FromR4",
    "VarI4FromR8",
    "VarI4FromStr",
    "VarI4FromUI1",
    "VarI4FromUI2",
    "VarI4FromUI4",
    "VarI4FromUI8",
    "VarI8FromBool",
    "VarI8FromCy",
    "VarI8FromDate",
    "VarI8FromDec",
    "VarI8FromDisp",
    "VarI8FromI1",
    "VarI8FromI2",
    "VarI8FromR4",
    "VarI8FromR8",
    "VarI8FromStr",
    "VarI8FromUI1",
    "VarI8FromUI2",
    "VarI8FromUI4",
    "VarI8FromUI8",
    "VarIdiv",
    "VarImp",
    "VarInt",
    "VarMod",
    "VarMonthName",
    "VarMul",
    "VarNeg",
    "VarNot",
    "VarNumFromParseNum",
    "VarOr",
    "VarParseNumFromStr",
    "VarPow",
    "VarR4CmpR8",
    "VarR4FromBool",
    "VarR4FromCy",
    "VarR4FromDate",
    "VarR4FromDec",
    "VarR4FromDisp",
    "VarR4FromI1",
    "VarR4FromI2",
    "VarR4FromI4",
    "VarR4FromI8",
    "VarR4FromR8",
    "VarR4FromStr",
    "VarR4FromUI1",
    "VarR4FromUI2",
    "VarR4FromUI4",
    "VarR4FromUI8",
    "VarR8FromBool",
    "VarR8FromCy",
    "VarR8FromDate",
    "VarR8FromDec",
    "VarR8FromDisp",
    "VarR8FromI1",
    "VarR8FromI2",
    "VarR8FromI4",
    "VarR8FromI8",
    "VarR8FromR4",
    "VarR8FromStr",
    "VarR8FromUI1",
    "VarR8FromUI2",
    "VarR8FromUI4",
    "VarR8FromUI8",
    "VarR8Pow",
    "VarR8Round",
    "VarRound",
    "VarSub",
    "VarTokenizeFormatString",
    "VarUI1FromBool",
    "VarUI1FromCy",
    "VarUI1FromDate",
    "VarUI1FromDec",
    "VarUI1FromDisp",
    "VarUI1FromI1",
    "VarUI1FromI2",
    "VarUI1FromI4",
    "VarUI1FromI8",
    "VarUI1FromR4",
    "VarUI1FromR8",
    "VarUI1FromStr",
    "VarUI1FromUI2",
    "VarUI1FromUI4",
    "VarUI1FromUI8",
    "VarUI2FromBool",
    "VarUI2FromCy",
    "VarUI2FromDate",
    "VarUI2FromDec",
    "VarUI2FromDisp",
    "VarUI2FromI1",
    "VarUI2FromI2",
    "VarUI2FromI4",
    "VarUI2FromI8",
    "VarUI2FromR4",
    "VarUI2FromR8",
    "VarUI2FromStr",
    "VarUI2FromUI1",
    "VarUI2FromUI4",
    "VarUI2FromUI8",
    "VarUI4FromBool",
    "VarUI4FromCy",
    "VarUI4FromDate",
    "VarUI4FromDec",
    "VarUI4FromDisp",
    "VarUI4FromI1",
    "VarUI4FromI2",
    "VarUI4FromI4",
    "VarUI4FromI8",
    "VarUI4FromR4",
    "VarUI4FromR8",
    "VarUI4FromStr",
    "VarUI4FromUI1",
    "VarUI4FromUI2",
    "VarUI4FromUI8",
    "VarUI8FromBool",
    "VarUI8FromCy",
    "VarUI8FromDate",
    "VarUI8FromDec",
    "VarUI8FromDisp",
    "VarUI8FromI1",
    "VarUI8FromI2",
    "VarUI8FromI8",
    "VarUI8FromR4",
    "VarUI8FromR8",
    "VarUI8FromStr",
    "VarUI8FromUI1",
    "VarUI8FromUI2",
    "VarUI8FromUI4",
    "VarUdateFromDate",
    "VarWeekdayName",
    "VarXor",
    "VariantChangeType",
    "VariantChangeTypeEx",
    "VariantClear",
    "VariantCopy",
    "VariantCopyInd",
    "VariantInit",
    "VariantTimeToDosDateTime",
    "VariantTimeToSystemTime",
    "VectorFromBstr",
    "WIN32",
    "WPCSETTING",
    "WPCSETTING_FILEDOWNLOAD_BLOCKED",
    "WPCSETTING_LOGGING_ENABLED",
    "XFORMCOORDS",
    "XFORMCOORDS_CONTAINERTOHIMETRIC",
    "XFORMCOORDS_EVENTCOMPAT",
    "XFORMCOORDS_HIMETRICTOCONTAINER",
    "XFORMCOORDS_POSITION",
    "XFORMCOORDS_SIZE",
    "_wireBRECORD",
    "_wireSAFEARRAY",
    "_wireVARIANT",
    "fdexEnumAll",
    "fdexEnumDefault",
    "fdexNameCaseInsensitive",
    "fdexNameCaseSensitive",
    "fdexNameEnsure",
    "fdexNameImplicit",
    "fdexNameInternal",
    "fdexNameNoDynamicProperties",
]
_arch_optional = [
]
