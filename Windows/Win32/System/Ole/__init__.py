from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Gdi
import Windows.Win32.Media
import Windows.Win32.System.Com
import Windows.Win32.System.Com.StructuredStorage
import Windows.Win32.System.Memory
import Windows.Win32.System.Ole
import Windows.Win32.System.SystemServices
import Windows.Win32.System.Variant
import Windows.Win32.UI.Controls
import Windows.Win32.UI.Controls.Dialogs
import Windows.Win32.UI.WindowsAndMessaging
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
ACTIVATEFLAGS = Int32
ACTIVATE_WINDOWLESS: ACTIVATEFLAGS = 1
ACTIVEOBJECT_FLAGS = UInt32
ACTIVEOBJECT_STRONG: ACTIVEOBJECT_FLAGS = 0
ACTIVEOBJECT_WEAK: ACTIVEOBJECT_FLAGS = 1
class ARRAYDESC(EasyCastStructure):
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
CLSID_CFontPropPage: Guid = Guid('{0be35200-8f91-11ce-9de3-00aa004bb851}')
CLSID_CColorPropPage: Guid = Guid('{0be35201-8f91-11ce-9de3-00aa004bb851}')
CLSID_CPicturePropPage: Guid = Guid('{0be35202-8f91-11ce-9de3-00aa004bb851}')
CLSID_PersistPropset: Guid = Guid('{fb8f0821-0164-101b-84ed-08002b2ec713}')
CLSID_ConvertVBX: Guid = Guid('{fb8f0822-0164-101b-84ed-08002b2ec713}')
CLSID_StdFont: Guid = Guid('{0be35203-8f91-11ce-9de3-00aa004bb851}')
CLSID_StdPicture: Guid = Guid('{0be35204-8f91-11ce-9de3-00aa004bb851}')
GUID_HIMETRIC: Guid = Guid('{66504300-be0f-101a-8bbb-00aa00300cab}')
GUID_COLOR: Guid = Guid('{66504301-be0f-101a-8bbb-00aa00300cab}')
GUID_XPOSPIXEL: Guid = Guid('{66504302-be0f-101a-8bbb-00aa00300cab}')
GUID_YPOSPIXEL: Guid = Guid('{66504303-be0f-101a-8bbb-00aa00300cab}')
GUID_XSIZEPIXEL: Guid = Guid('{66504304-be0f-101a-8bbb-00aa00300cab}')
GUID_YSIZEPIXEL: Guid = Guid('{66504305-be0f-101a-8bbb-00aa00300cab}')
GUID_XPOS: Guid = Guid('{66504306-be0f-101a-8bbb-00aa00300cab}')
GUID_YPOS: Guid = Guid('{66504307-be0f-101a-8bbb-00aa00300cab}')
GUID_XSIZE: Guid = Guid('{66504308-be0f-101a-8bbb-00aa00300cab}')
GUID_YSIZE: Guid = Guid('{66504309-be0f-101a-8bbb-00aa00300cab}')
GUID_TRISTATE: Guid = Guid('{6650430a-be0f-101a-8bbb-00aa00300cab}')
GUID_OPTIONVALUEEXCLUSIVE: Guid = Guid('{6650430b-be0f-101a-8bbb-00aa00300cab}')
GUID_CHECKVALUEEXCLUSIVE: Guid = Guid('{6650430c-be0f-101a-8bbb-00aa00300cab}')
GUID_FONTNAME: Guid = Guid('{6650430d-be0f-101a-8bbb-00aa00300cab}')
GUID_FONTSIZE: Guid = Guid('{6650430e-be0f-101a-8bbb-00aa00300cab}')
GUID_FONTBOLD: Guid = Guid('{6650430f-be0f-101a-8bbb-00aa00300cab}')
GUID_FONTITALIC: Guid = Guid('{66504310-be0f-101a-8bbb-00aa00300cab}')
GUID_FONTUNDERSCORE: Guid = Guid('{66504311-be0f-101a-8bbb-00aa00300cab}')
GUID_FONTSTRIKETHROUGH: Guid = Guid('{66504312-be0f-101a-8bbb-00aa00300cab}')
GUID_HANDLE: Guid = Guid('{66504313-be0f-101a-8bbb-00aa00300cab}')
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
SID_VariantConversion: Guid = Guid('{1f101481-bccd-11d0-9336-00a0c90dcaa9}')
SID_GetCaller: Guid = Guid('{4717cc40-bcb9-11d0-9336-00a0c90dcaa9}')
SID_ProvideRuntimeContext: Guid = Guid('{74a5040c-dd0c-48f0-ac85-194c3259180a}')
@winfunctype('OLEAUT32.dll')
def SafeArrayAllocDescriptor(cDims: UInt32, ppsaOut: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayAllocDescriptorEx(vt: Windows.Win32.System.Variant.VARENUM, cDims: UInt32, ppsaOut: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayAllocData(psa: POINTER(Windows.Win32.System.Com.SAFEARRAY_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayCreate(vt: Windows.Win32.System.Variant.VARENUM, cDims: UInt32, rgsabound: POINTER(Windows.Win32.System.Com.SAFEARRAYBOUND_head)) -> POINTER(Windows.Win32.System.Com.SAFEARRAY_head): ...
@winfunctype('OLEAUT32.dll')
def SafeArrayCreateEx(vt: Windows.Win32.System.Variant.VARENUM, cDims: UInt32, rgsabound: POINTER(Windows.Win32.System.Com.SAFEARRAYBOUND_head), pvExtra: c_void_p) -> POINTER(Windows.Win32.System.Com.SAFEARRAY_head): ...
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
def SafeArrayGetVartype(psa: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), pvt: POINTER(Windows.Win32.System.Variant.VARENUM)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayCreateVector(vt: Windows.Win32.System.Variant.VARENUM, lLbound: Int32, cElements: UInt32) -> POINTER(Windows.Win32.System.Com.SAFEARRAY_head): ...
@winfunctype('OLEAUT32.dll')
def SafeArrayCreateVectorEx(vt: Windows.Win32.System.Variant.VARENUM, lLbound: Int32, cElements: UInt32, pvExtra: c_void_p) -> POINTER(Windows.Win32.System.Com.SAFEARRAY_head): ...
@winfunctype('OLEAUT32.dll')
def VectorFromBstr(bstr: Windows.Win32.Foundation.BSTR, ppsa: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def BstrFromVector(psa: POINTER(Windows.Win32.System.Com.SAFEARRAY_head), pbstr: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromI2(sIn: Int16, pbOut: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromI4(lIn: Int32, pbOut: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromI8(i64In: Int64, pbOut: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromR4(fltIn: Single, pbOut: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromR8(dblIn: Double, pbOut: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromCy(cyIn: Windows.Win32.System.Com.CY, pbOut: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromDate(dateIn: Double, pbOut: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromStr(strIn: Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, pbOut: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromDisp(pdispIn: Windows.Win32.System.Com.IDispatch_head, lcid: UInt32, pbOut: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromBool(boolIn: Windows.Win32.Foundation.VARIANT_BOOL, pbOut: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromI1(cIn: Windows.Win32.Foundation.CHAR, pbOut: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromUI2(uiIn: UInt16, pbOut: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromUI4(ulIn: UInt32, pbOut: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromUI8(ui64In: UInt64, pbOut: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromDec(pdecIn: POINTER(Windows.Win32.Foundation.DECIMAL_head), pbOut: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
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
def VarParseNumFromStr(strIn: Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, pnumprs: POINTER(Windows.Win32.System.Ole.NUMPARSE_head), rgbDig: POINTER(Byte)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarNumFromParseNum(pnumprs: POINTER(Windows.Win32.System.Ole.NUMPARSE_head), rgbDig: POINTER(Byte), dwVtBits: UInt32, pvar: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarAdd(pvarLeft: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarRight: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarAnd(pvarLeft: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarRight: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCat(pvarLeft: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarRight: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDiv(pvarLeft: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarRight: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarEqv(pvarLeft: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarRight: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarIdiv(pvarLeft: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarRight: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarImp(pvarLeft: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarRight: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarMod(pvarLeft: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarRight: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarMul(pvarLeft: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarRight: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarOr(pvarLeft: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarRight: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarPow(pvarLeft: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarRight: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarSub(pvarLeft: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarRight: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarXor(pvarLeft: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarRight: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarAbs(pvarIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarFix(pvarIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarInt(pvarIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarNeg(pvarIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarNot(pvarIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarResult: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarRound(pvarIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), cDecimals: Int32, pvarResult: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCmp(pvarLeft: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarRight: POINTER(Windows.Win32.System.Variant.VARIANT_head), lcid: UInt32, dwFlags: UInt32) -> Windows.Win32.System.Ole.VARCMP: ...
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
def VarFormat(pvarIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), pstrFormat: Windows.Win32.Foundation.PWSTR, iFirstDay: Windows.Win32.System.Ole.VARFORMAT_FIRST_DAY, iFirstWeek: Windows.Win32.System.Ole.VARFORMAT_FIRST_WEEK, dwFlags: UInt32, pbstrOut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarFormatDateTime(pvarIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), iNamedFormat: Windows.Win32.System.Ole.VARFORMAT_NAMED_FORMAT, dwFlags: UInt32, pbstrOut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarFormatNumber(pvarIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), iNumDig: Int32, iIncLead: Windows.Win32.System.Ole.VARFORMAT_LEADING_DIGIT, iUseParens: Windows.Win32.System.Ole.VARFORMAT_PARENTHESES, iGroup: Windows.Win32.System.Ole.VARFORMAT_GROUP, dwFlags: UInt32, pbstrOut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarFormatPercent(pvarIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), iNumDig: Int32, iIncLead: Windows.Win32.System.Ole.VARFORMAT_LEADING_DIGIT, iUseParens: Windows.Win32.System.Ole.VARFORMAT_PARENTHESES, iGroup: Windows.Win32.System.Ole.VARFORMAT_GROUP, dwFlags: UInt32, pbstrOut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarFormatCurrency(pvarIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), iNumDig: Int32, iIncLead: Int32, iUseParens: Int32, iGroup: Int32, dwFlags: UInt32, pbstrOut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarWeekdayName(iWeekday: Int32, fAbbrev: Int32, iFirstDay: Int32, dwFlags: UInt32, pbstrOut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarMonthName(iMonth: Int32, fAbbrev: Int32, dwFlags: UInt32, pbstrOut: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarFormatFromTokens(pvarIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), pstrFormat: Windows.Win32.Foundation.PWSTR, pbTokCur: POINTER(Byte), dwFlags: UInt32, pbstrOut: POINTER(Windows.Win32.Foundation.BSTR), lcid: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarTokenizeFormatString(pstrFormat: Windows.Win32.Foundation.PWSTR, rgbTok: POINTER(Byte), cbTok: Int32, iFirstDay: Windows.Win32.System.Ole.VARFORMAT_FIRST_DAY, iFirstWeek: Windows.Win32.System.Ole.VARFORMAT_FIRST_WEEK, lcid: UInt32, pcbActual: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
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
def DispGetParam(pdispparams: POINTER(Windows.Win32.System.Com.DISPPARAMS_head), position: UInt32, vtTarg: Windows.Win32.System.Variant.VARENUM, pvarResult: POINTER(Windows.Win32.System.Variant.VARIANT_head), puArgErr: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def DispGetIDsOfNames(ptinfo: Windows.Win32.System.Com.ITypeInfo_head, rgszNames: POINTER(Windows.Win32.Foundation.PWSTR), cNames: UInt32, rgdispid: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def DispInvoke(_this: c_void_p, ptinfo: Windows.Win32.System.Com.ITypeInfo_head, dispidMember: Int32, wFlags: UInt16, pparams: POINTER(Windows.Win32.System.Com.DISPPARAMS_head), pvarResult: POINTER(Windows.Win32.System.Variant.VARIANT_head), pexcepinfo: POINTER(Windows.Win32.System.Com.EXCEPINFO_head), puArgErr: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def CreateDispTypeInfo(pidata: POINTER(Windows.Win32.System.Ole.INTERFACEDATA_head), lcid: UInt32, pptinfo: POINTER(Windows.Win32.System.Com.ITypeInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def CreateStdDispatch(punkOuter: Windows.Win32.System.Com.IUnknown_head, pvThis: c_void_p, ptinfo: Windows.Win32.System.Com.ITypeInfo_head, ppunkStdDisp: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def DispCallFunc(pvInstance: c_void_p, oVft: UIntPtr, cc: Windows.Win32.System.Com.CALLCONV, vtReturn: Windows.Win32.System.Variant.VARENUM, cActuals: UInt32, prgvt: POINTER(UInt16), prgpvarg: POINTER(POINTER(Windows.Win32.System.Variant.VARIANT_head)), pvargResult: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
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
def OleCreate(rclsid: POINTER(Guid), riid: POINTER(Guid), renderopt: UInt32, pFormatEtc: POINTER(Windows.Win32.System.Com.FORMATETC_head), pClientSite: Windows.Win32.System.Ole.IOleClientSite_head, pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleCreateEx(rclsid: POINTER(Guid), riid: POINTER(Guid), dwFlags: Windows.Win32.System.Ole.OLECREATE, renderopt: UInt32, cFormats: UInt32, rgAdvf: POINTER(UInt32), rgFormatEtc: POINTER(Windows.Win32.System.Com.FORMATETC_head), lpAdviseSink: Windows.Win32.System.Com.IAdviseSink_head, rgdwConnection: POINTER(UInt32), pClientSite: Windows.Win32.System.Ole.IOleClientSite_head, pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleCreateFromData(pSrcDataObj: Windows.Win32.System.Com.IDataObject_head, riid: POINTER(Guid), renderopt: UInt32, pFormatEtc: POINTER(Windows.Win32.System.Com.FORMATETC_head), pClientSite: Windows.Win32.System.Ole.IOleClientSite_head, pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleCreateFromDataEx(pSrcDataObj: Windows.Win32.System.Com.IDataObject_head, riid: POINTER(Guid), dwFlags: Windows.Win32.System.Ole.OLECREATE, renderopt: UInt32, cFormats: UInt32, rgAdvf: POINTER(UInt32), rgFormatEtc: POINTER(Windows.Win32.System.Com.FORMATETC_head), lpAdviseSink: Windows.Win32.System.Com.IAdviseSink_head, rgdwConnection: POINTER(UInt32), pClientSite: Windows.Win32.System.Ole.IOleClientSite_head, pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleCreateLinkFromData(pSrcDataObj: Windows.Win32.System.Com.IDataObject_head, riid: POINTER(Guid), renderopt: UInt32, pFormatEtc: POINTER(Windows.Win32.System.Com.FORMATETC_head), pClientSite: Windows.Win32.System.Ole.IOleClientSite_head, pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleCreateLinkFromDataEx(pSrcDataObj: Windows.Win32.System.Com.IDataObject_head, riid: POINTER(Guid), dwFlags: Windows.Win32.System.Ole.OLECREATE, renderopt: UInt32, cFormats: UInt32, rgAdvf: POINTER(UInt32), rgFormatEtc: POINTER(Windows.Win32.System.Com.FORMATETC_head), lpAdviseSink: Windows.Win32.System.Com.IAdviseSink_head, rgdwConnection: POINTER(UInt32), pClientSite: Windows.Win32.System.Ole.IOleClientSite_head, pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleCreateStaticFromData(pSrcDataObj: Windows.Win32.System.Com.IDataObject_head, iid: POINTER(Guid), renderopt: UInt32, pFormatEtc: POINTER(Windows.Win32.System.Com.FORMATETC_head), pClientSite: Windows.Win32.System.Ole.IOleClientSite_head, pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleCreateLink(pmkLinkSrc: Windows.Win32.System.Com.IMoniker_head, riid: POINTER(Guid), renderopt: UInt32, lpFormatEtc: POINTER(Windows.Win32.System.Com.FORMATETC_head), pClientSite: Windows.Win32.System.Ole.IOleClientSite_head, pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleCreateLinkEx(pmkLinkSrc: Windows.Win32.System.Com.IMoniker_head, riid: POINTER(Guid), dwFlags: Windows.Win32.System.Ole.OLECREATE, renderopt: UInt32, cFormats: UInt32, rgAdvf: POINTER(UInt32), rgFormatEtc: POINTER(Windows.Win32.System.Com.FORMATETC_head), lpAdviseSink: Windows.Win32.System.Com.IAdviseSink_head, rgdwConnection: POINTER(UInt32), pClientSite: Windows.Win32.System.Ole.IOleClientSite_head, pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleCreateLinkToFile(lpszFileName: Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), renderopt: UInt32, lpFormatEtc: POINTER(Windows.Win32.System.Com.FORMATETC_head), pClientSite: Windows.Win32.System.Ole.IOleClientSite_head, pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleCreateLinkToFileEx(lpszFileName: Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), dwFlags: Windows.Win32.System.Ole.OLECREATE, renderopt: UInt32, cFormats: UInt32, rgAdvf: POINTER(UInt32), rgFormatEtc: POINTER(Windows.Win32.System.Com.FORMATETC_head), lpAdviseSink: Windows.Win32.System.Com.IAdviseSink_head, rgdwConnection: POINTER(UInt32), pClientSite: Windows.Win32.System.Ole.IOleClientSite_head, pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleCreateFromFile(rclsid: POINTER(Guid), lpszFileName: Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), renderopt: UInt32, lpFormatEtc: POINTER(Windows.Win32.System.Com.FORMATETC_head), pClientSite: Windows.Win32.System.Ole.IOleClientSite_head, pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleCreateFromFileEx(rclsid: POINTER(Guid), lpszFileName: Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), dwFlags: Windows.Win32.System.Ole.OLECREATE, renderopt: UInt32, cFormats: UInt32, rgAdvf: POINTER(UInt32), rgFormatEtc: POINTER(Windows.Win32.System.Com.FORMATETC_head), lpAdviseSink: Windows.Win32.System.Com.IAdviseSink_head, rgdwConnection: POINTER(UInt32), pClientSite: Windows.Win32.System.Ole.IOleClientSite_head, pStg: Windows.Win32.System.Com.StructuredStorage.IStorage_head, ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
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
def OleRegGetUserType(clsid: POINTER(Guid), dwFormOfType: UInt32, pszUserType: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
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
def HRGN_UserMarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.Graphics.Gdi.HRGN)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HRGN_UserUnmarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.Graphics.Gdi.HRGN)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HRGN_UserFree(param0: POINTER(UInt32), param1: POINTER(Windows.Win32.Graphics.Gdi.HRGN)) -> Void: ...
@winfunctype('api-ms-win-core-marshal-l1-1-0.dll')
def HRGN_UserSize64(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(Windows.Win32.Graphics.Gdi.HRGN)) -> UInt32: ...
@winfunctype('api-ms-win-core-marshal-l1-1-0.dll')
def HRGN_UserMarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.Graphics.Gdi.HRGN)) -> POINTER(Byte): ...
@winfunctype('api-ms-win-core-marshal-l1-1-0.dll')
def HRGN_UserUnmarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(Windows.Win32.Graphics.Gdi.HRGN)) -> POINTER(Byte): ...
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
def OleLoadPictureFile(varFileName: Windows.Win32.System.Variant.VARIANT, lplpdispPicture: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def OleLoadPictureFileEx(varFileName: Windows.Win32.System.Variant.VARIANT, xSizeDesired: UInt32, ySizeDesired: UInt32, dwFlags: Windows.Win32.System.Ole.LOAD_PICTURE_FLAGS, lplpdispPicture: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
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
@cfunctype('oledlg.dll', variadic=True)
def OleUIPromptUserW(nTemplate: Int32, hwndParent: Windows.Win32.Foundation.HWND, *__arglist) -> Int32: ...
@cfunctype('oledlg.dll', variadic=True)
def OleUIPromptUserA(nTemplate: Int32, hwndParent: Windows.Win32.Foundation.HWND, *__arglist) -> Int32: ...
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
class CADWORD(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(UInt32)
class CALPOLESTR(EasyCastStructure):
    cElems: UInt32
    pElems: POINTER(Windows.Win32.Foundation.PWSTR)
class CAUUID(EasyCastStructure):
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
CHANGE_ICON_FLAGS = UInt32
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
class CLEANLOCALSTORAGE(EasyCastStructure):
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
class CONTROLINFO(EasyCastStructure):
    cb: UInt32
    hAccel: Windows.Win32.UI.WindowsAndMessaging.HACCEL
    cAccel: UInt16
    dwFlags: UInt32
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
class DVASPECTINFO(EasyCastStructure):
    cb: UInt32
    dwFlags: UInt32
DVASPECTINFOFLAG = Int32
DVASPECTINFOFLAG_CANOPTIMIZE: DVASPECTINFOFLAG = 1
class DVEXTENTINFO(EasyCastStructure):
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
class FONTDESC(EasyCastStructure):
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
class IAdviseSinkEx(ComPtr):
    extends: Windows.Win32.System.Com.IAdviseSink
    _iid_ = Guid('{3af24290-0c96-11ce-a0cf-00aa00600ab8}')
    @commethod(8)
    def OnViewStatusChange(self, dwViewStatus: UInt32) -> Void: ...
class ICanHandleException(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c5598e60-b307-11d1-b27d-006008c3fbfb}')
    @commethod(3)
    def CanHandleException(self, pExcepInfo: POINTER(Windows.Win32.System.Com.EXCEPINFO_head), pvar: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IClassFactory2(ComPtr):
    extends: Windows.Win32.System.Com.IClassFactory
    _iid_ = Guid('{b196b28f-bab4-101a-b69c-00aa00341d07}')
    @commethod(5)
    def GetLicInfo(self, pLicInfo: POINTER(Windows.Win32.System.Ole.LICINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RequestLicKey(self, dwReserved: UInt32, pBstrKey: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateInstanceLic(self, pUnkOuter: Windows.Win32.System.Com.IUnknown_head, pUnkReserved: Windows.Win32.System.Com.IUnknown_head, riid: POINTER(Guid), bstrKey: Windows.Win32.Foundation.BSTR, ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IContinue(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000012a-0000-0000-c000-000000000046}')
    @commethod(3)
    def FContinue(self) -> Windows.Win32.Foundation.HRESULT: ...
class IContinueCallback(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b722bcca-4e68-101b-a2bc-00aa00404770}')
    @commethod(3)
    def FContinue(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FContinuePrinting(self, nCntPrinted: Int32, nCurPage: Int32, pwszPrintStatus: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ICreateErrorInfo(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{22f03340-547d-101b-8e65-08002b2bd119}')
    @commethod(3)
    def SetGUID(self, rguid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetSource(self, szSource: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetDescription(self, szDescription: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetHelpFile(self, szHelpFile: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetHelpContext(self, dwHelpContext: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ICreateTypeInfo(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00020405-0000-0000-c000-000000000046}')
    @commethod(3)
    def SetGuid(self, guid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetTypeFlags(self, uTypeFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetDocString(self, pStrDoc: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetHelpContext(self, dwHelpContext: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetVersion(self, wMajorVerNum: UInt16, wMinorVerNum: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AddRefTypeInfo(self, pTInfo: Windows.Win32.System.Com.ITypeInfo_head, phRefType: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddFuncDesc(self, index: UInt32, pFuncDesc: POINTER(Windows.Win32.System.Com.FUNCDESC_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def AddImplType(self, index: UInt32, hRefType: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetImplTypeFlags(self, index: UInt32, implTypeFlags: Windows.Win32.System.Com.IMPLTYPEFLAGS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetAlignment(self, cbAlignment: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetSchema(self, pStrSchema: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def AddVarDesc(self, index: UInt32, pVarDesc: POINTER(Windows.Win32.System.Com.VARDESC_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetFuncAndParamNames(self, index: UInt32, rgszNames: POINTER(Windows.Win32.Foundation.PWSTR), cNames: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetVarName(self, index: UInt32, szName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetTypeDescAlias(self, pTDescAlias: POINTER(Windows.Win32.System.Com.TYPEDESC_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def DefineFuncAsDllEntry(self, index: UInt32, szDllName: Windows.Win32.Foundation.PWSTR, szProcName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetFuncDocString(self, index: UInt32, szDocString: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetVarDocString(self, index: UInt32, szDocString: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetFuncHelpContext(self, index: UInt32, dwHelpContext: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetVarHelpContext(self, index: UInt32, dwHelpContext: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetMops(self, index: UInt32, bstrMops: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetTypeIdldesc(self, pIdlDesc: POINTER(Windows.Win32.System.Com.IDLDESC_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def LayOut(self) -> Windows.Win32.Foundation.HRESULT: ...
class ICreateTypeInfo2(ComPtr):
    extends: Windows.Win32.System.Ole.ICreateTypeInfo
    _iid_ = Guid('{0002040e-0000-0000-c000-000000000046}')
    @commethod(26)
    def DeleteFuncDesc(self, index: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def DeleteFuncDescByMemId(self, memid: Int32, invKind: Windows.Win32.System.Com.INVOKEKIND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def DeleteVarDesc(self, index: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def DeleteVarDescByMemId(self, memid: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def DeleteImplType(self, index: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def SetCustData(self, guid: POINTER(Guid), pVarVal: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def SetFuncCustData(self, index: UInt32, guid: POINTER(Guid), pVarVal: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def SetParamCustData(self, indexFunc: UInt32, indexParam: UInt32, guid: POINTER(Guid), pVarVal: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def SetVarCustData(self, index: UInt32, guid: POINTER(Guid), pVarVal: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def SetImplTypeCustData(self, index: UInt32, guid: POINTER(Guid), pVarVal: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def SetHelpStringContext(self, dwHelpStringContext: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def SetFuncHelpStringContext(self, index: UInt32, dwHelpStringContext: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def SetVarHelpStringContext(self, index: UInt32, dwHelpStringContext: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def Invalidate(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def SetName(self, szName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ICreateTypeLib(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00020406-0000-0000-c000-000000000046}')
    @commethod(3)
    def CreateTypeInfo(self, szName: Windows.Win32.Foundation.PWSTR, tkind: Windows.Win32.System.Com.TYPEKIND, ppCTInfo: POINTER(Windows.Win32.System.Ole.ICreateTypeInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetName(self, szName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetVersion(self, wMajorVerNum: UInt16, wMinorVerNum: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetGuid(self, guid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetDocString(self, szDoc: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetHelpFileName(self, szHelpFileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetHelpContext(self, dwHelpContext: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetLcid(self, lcid: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetLibFlags(self, uLibFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SaveAllChanges(self) -> Windows.Win32.Foundation.HRESULT: ...
class ICreateTypeLib2(ComPtr):
    extends: Windows.Win32.System.Ole.ICreateTypeLib
    _iid_ = Guid('{0002040f-0000-0000-c000-000000000046}')
    @commethod(13)
    def DeleteTypeInfo(self, szName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetCustData(self, guid: POINTER(Guid), pVarVal: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetHelpStringContext(self, dwHelpStringContext: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetHelpStringDll(self, szFileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IDispError(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a6ef9861-c720-11d0-9337-00a0c90dcaa9}')
    @commethod(3)
    def QueryErrorInfo(self, guidErrorType: Guid, ppde: POINTER(Windows.Win32.System.Ole.IDispError_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNext(self, ppde: POINTER(Windows.Win32.System.Ole.IDispError_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetHresult(self, phr: POINTER(Windows.Win32.Foundation.HRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSource(self, pbstrSource: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetHelpInfo(self, pbstrFileName: POINTER(Windows.Win32.Foundation.BSTR), pdwContext: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDescription(self, pbstrDescription: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IDispatchEx(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{a6ef9860-c720-11d0-9337-00a0c90dcaa9}')
    @commethod(7)
    def GetDispID(self, bstrName: Windows.Win32.Foundation.BSTR, grfdex: UInt32, pid: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def InvokeEx(self, id: Int32, lcid: UInt32, wFlags: UInt16, pdp: POINTER(Windows.Win32.System.Com.DISPPARAMS_head), pvarRes: POINTER(Windows.Win32.System.Variant.VARIANT_head), pei: POINTER(Windows.Win32.System.Com.EXCEPINFO_head), pspCaller: Windows.Win32.System.Com.IServiceProvider_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def DeleteMemberByName(self, bstrName: Windows.Win32.Foundation.BSTR, grfdex: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def DeleteMemberByDispID(self, id: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetMemberProperties(self, id: Int32, grfdexFetch: UInt32, pgrfdex: POINTER(Windows.Win32.System.Ole.FDEX_PROP_FLAGS)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetMemberName(self, id: Int32, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetNextDispID(self, grfdex: UInt32, id: Int32, pid: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetNameSpaceParent(self, ppunk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDropSource(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000121-0000-0000-c000-000000000046}')
    @commethod(3)
    def QueryContinueDrag(self, fEscapePressed: Windows.Win32.Foundation.BOOL, grfKeyState: Windows.Win32.System.SystemServices.MODIFIERKEYS_FLAGS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GiveFeedback(self, dwEffect: Windows.Win32.System.Ole.DROPEFFECT) -> Windows.Win32.Foundation.HRESULT: ...
class IDropSourceNotify(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000012b-0000-0000-c000-000000000046}')
    @commethod(3)
    def DragEnterTarget(self, hwndTarget: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DragLeaveTarget(self) -> Windows.Win32.Foundation.HRESULT: ...
class IDropTarget(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000122-0000-0000-c000-000000000046}')
    @commethod(3)
    def DragEnter(self, pDataObj: Windows.Win32.System.Com.IDataObject_head, grfKeyState: Windows.Win32.System.SystemServices.MODIFIERKEYS_FLAGS, pt: Windows.Win32.Foundation.POINTL, pdwEffect: POINTER(Windows.Win32.System.Ole.DROPEFFECT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DragOver(self, grfKeyState: Windows.Win32.System.SystemServices.MODIFIERKEYS_FLAGS, pt: Windows.Win32.Foundation.POINTL, pdwEffect: POINTER(Windows.Win32.System.Ole.DROPEFFECT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DragLeave(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Drop(self, pDataObj: Windows.Win32.System.Com.IDataObject_head, grfKeyState: Windows.Win32.System.SystemServices.MODIFIERKEYS_FLAGS, pt: Windows.Win32.Foundation.POINTL, pdwEffect: POINTER(Windows.Win32.System.Ole.DROPEFFECT)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnterpriseDropTarget(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{390e3878-fd55-4e18-819d-4682081c0cfd}')
    @commethod(3)
    def SetDropSourceEnterpriseId(self, identity: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsEvaluatingEdpPolicy(self, value: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumOLEVERB(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000104-0000-0000-c000-000000000046}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(Windows.Win32.System.Ole.OLEVERB_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(Windows.Win32.System.Ole.IEnumOLEVERB_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumOleDocumentViews(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b722bcc8-4e68-101b-a2bc-00aa00404770}')
    @commethod(3)
    def Next(self, cViews: UInt32, rgpView: POINTER(Windows.Win32.System.Ole.IOleDocumentView_head), pcFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cViews: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(Windows.Win32.System.Ole.IEnumOleDocumentViews_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumOleUndoUnits(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b3e7c340-ef97-11ce-9bc9-00aa00608e01}')
    @commethod(3)
    def Next(self, cElt: UInt32, rgElt: POINTER(Windows.Win32.System.Ole.IOleUndoUnit_head), pcEltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cElt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(Windows.Win32.System.Ole.IEnumOleUndoUnits_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumVARIANT(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00020404-0000-0000-c000-000000000046}')
    @commethod(3)
    def Next(self, celt: UInt32, rgVar: POINTER(Windows.Win32.System.Variant.VARIANT_head), pCeltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(Windows.Win32.System.Ole.IEnumVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IFont(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bef6e002-a874-101a-8bba-00aa00300cab}')
    @commethod(3)
    def get_Name(self, pName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_Name(self, name: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_Size(self, pSize: POINTER(Windows.Win32.System.Com.CY_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_Size(self, size: Windows.Win32.System.Com.CY) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Bold(self, pBold: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Bold(self, bold: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Italic(self, pItalic: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Italic(self, italic: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Underline(self, pUnderline: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Underline(self, underline: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Strikethrough(self, pStrikethrough: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Strikethrough(self, strikethrough: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Weight(self, pWeight: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Weight(self, weight: Int16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Charset(self, pCharset: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_Charset(self, charset: Int16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_hFont(self, phFont: POINTER(Windows.Win32.Graphics.Gdi.HFONT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def Clone(self, ppFont: POINTER(Windows.Win32.System.Ole.IFont_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def IsEqual(self, pFontOther: Windows.Win32.System.Ole.IFont_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetRatio(self, cyLogical: Int32, cyHimetric: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def QueryTextMetrics(self, pTM: POINTER(Windows.Win32.Graphics.Gdi.TEXTMETRICW_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def AddRefHfont(self, hFont: Windows.Win32.Graphics.Gdi.HFONT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def ReleaseHfont(self, hFont: Windows.Win32.Graphics.Gdi.HFONT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def SetHdc(self, hDC: Windows.Win32.Graphics.Gdi.HDC) -> Windows.Win32.Foundation.HRESULT: ...
class IFontDisp(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{bef6e003-a874-101a-8bba-00aa00300cab}')
class IFontEventsDisp(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{4ef6100a-af88-11d0-9846-00c04fc29993}')
IGNOREMIME = Int32
IGNOREMIME_PROMPT: IGNOREMIME = 1
IGNOREMIME_TEXT: IGNOREMIME = 2
class IGetOleObject(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8a701da0-4feb-101b-a82e-08002b2b2337}')
    @commethod(3)
    def GetOleObject(self, riid: POINTER(Guid), ppvObj: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IGetVBAObject(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{91733a60-3f4c-101b-a3f6-00aa0034e4e9}')
    @commethod(3)
    def GetObject(self, riid: POINTER(Guid), ppvObj: POINTER(c_void_p), dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
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
class INTERFACEDATA(EasyCastStructure):
    pmethdata: POINTER(Windows.Win32.System.Ole.METHODDATA_head)
    cMembers: UInt32
class IObjectIdentity(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ca04b7e6-0d21-11d1-8cc5-00c04fc2b085}')
    @commethod(3)
    def IsEqualObject(self, punk: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IObjectWithSite(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fc4801a3-2ba9-11cf-a229-00aa003d7352}')
    @commethod(3)
    def SetSite(self, pUnkSite: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSite(self, riid: POINTER(Guid), ppvSite: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IOleAdviseHolder(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000111-0000-0000-c000-000000000046}')
    @commethod(3)
    def Advise(self, pAdvise: Windows.Win32.System.Com.IAdviseSink_head, pdwConnection: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unadvise(self, dwConnection: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumAdvise(self, ppenumAdvise: POINTER(Windows.Win32.System.Com.IEnumSTATDATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SendOnRename(self, pmk: Windows.Win32.System.Com.IMoniker_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SendOnSave(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SendOnClose(self) -> Windows.Win32.Foundation.HRESULT: ...
class IOleCache(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000011e-0000-0000-c000-000000000046}')
    @commethod(3)
    def Cache(self, pformatetc: POINTER(Windows.Win32.System.Com.FORMATETC_head), advf: UInt32, pdwConnection: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Uncache(self, dwConnection: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumCache(self, ppenumSTATDATA: POINTER(Windows.Win32.System.Com.IEnumSTATDATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def InitCache(self, pDataObject: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetData(self, pformatetc: POINTER(Windows.Win32.System.Com.FORMATETC_head), pmedium: POINTER(Windows.Win32.System.Com.STGMEDIUM_head), fRelease: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IOleCache2(ComPtr):
    extends: Windows.Win32.System.Ole.IOleCache
    _iid_ = Guid('{00000128-0000-0000-c000-000000000046}')
    @commethod(8)
    def UpdateCache(self, pDataObject: Windows.Win32.System.Com.IDataObject_head, grfUpdf: Windows.Win32.System.Ole.UPDFCACHE_FLAGS, pReserved: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def DiscardCache(self, dwDiscardOptions: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IOleCacheControl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000129-0000-0000-c000-000000000046}')
    @commethod(3)
    def OnRun(self, pDataObject: Windows.Win32.System.Com.IDataObject_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnStop(self) -> Windows.Win32.Foundation.HRESULT: ...
class IOleClientSite(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000118-0000-0000-c000-000000000046}')
    @commethod(3)
    def SaveObject(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMoniker(self, dwAssign: UInt32, dwWhichMoniker: UInt32, ppmk: POINTER(Windows.Win32.System.Com.IMoniker_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetContainer(self, ppContainer: POINTER(Windows.Win32.System.Ole.IOleContainer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ShowObject(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnShowWindow(self, fShow: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RequestNewObjectLayout(self) -> Windows.Win32.Foundation.HRESULT: ...
class IOleCommandTarget(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b722bccb-4e68-101b-a2bc-00aa00404770}')
    @commethod(3)
    def QueryStatus(self, pguidCmdGroup: POINTER(Guid), cCmds: UInt32, prgCmds: POINTER(Windows.Win32.System.Ole.OLECMD_head), pCmdText: POINTER(Windows.Win32.System.Ole.OLECMDTEXT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Exec(self, pguidCmdGroup: POINTER(Guid), nCmdID: UInt32, nCmdexecopt: UInt32, pvaIn: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvaOut: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOleContainer(ComPtr):
    extends: Windows.Win32.System.Ole.IParseDisplayName
    _iid_ = Guid('{0000011b-0000-0000-c000-000000000046}')
    @commethod(4)
    def EnumObjects(self, grfFlags: UInt32, ppenum: POINTER(Windows.Win32.System.Com.IEnumUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def LockContainer(self, fLock: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IOleControl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b196b288-bab4-101a-b69c-00aa00341d07}')
    @commethod(3)
    def GetControlInfo(self, pCI: POINTER(Windows.Win32.System.Ole.CONTROLINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnMnemonic(self, pMsg: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnAmbientPropertyChange(self, dispID: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FreezeEvents(self, bFreeze: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IOleControlSite(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b196b289-bab4-101a-b69c-00aa00341d07}')
    @commethod(3)
    def OnControlInfoChanged(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LockInPlaceActive(self, fLock: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetExtendedControl(self, ppDisp: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def TransformCoords(self, pPtlHimetric: POINTER(Windows.Win32.Foundation.POINTL_head), pPtfContainer: POINTER(Windows.Win32.System.Ole.POINTF_head), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def TranslateAccelerator(self, pMsg: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head), grfModifiers: Windows.Win32.System.Ole.KEYMODIFIERS) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnFocus(self, fGotFocus: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ShowPropertyFrame(self) -> Windows.Win32.Foundation.HRESULT: ...
class IOleDocument(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b722bcc5-4e68-101b-a2bc-00aa00404770}')
    @commethod(3)
    def CreateView(self, pIPSite: Windows.Win32.System.Ole.IOleInPlaceSite_head, pstm: Windows.Win32.System.Com.IStream_head, dwReserved: UInt32, ppView: POINTER(Windows.Win32.System.Ole.IOleDocumentView_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDocMiscStatus(self, pdwStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumViews(self, ppEnum: POINTER(Windows.Win32.System.Ole.IEnumOleDocumentViews_head), ppView: POINTER(Windows.Win32.System.Ole.IOleDocumentView_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOleDocumentSite(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b722bcc7-4e68-101b-a2bc-00aa00404770}')
    @commethod(3)
    def ActivateMe(self, pViewToActivate: Windows.Win32.System.Ole.IOleDocumentView_head) -> Windows.Win32.Foundation.HRESULT: ...
class IOleDocumentView(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b722bcc6-4e68-101b-a2bc-00aa00404770}')
    @commethod(3)
    def SetInPlaceSite(self, pIPSite: Windows.Win32.System.Ole.IOleInPlaceSite_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInPlaceSite(self, ppIPSite: POINTER(Windows.Win32.System.Ole.IOleInPlaceSite_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDocument(self, ppunk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetRect(self, prcView: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRect(self, prcView: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetRectComplex(self, prcView: POINTER(Windows.Win32.Foundation.RECT_head), prcHScroll: POINTER(Windows.Win32.Foundation.RECT_head), prcVScroll: POINTER(Windows.Win32.Foundation.RECT_head), prcSizeBox: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Show(self, fShow: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def UIActivate(self, fUIActivate: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Open(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def CloseView(self, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SaveViewState(self, pstm: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def ApplyViewState(self, pstm: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Clone(self, pIPSiteNew: Windows.Win32.System.Ole.IOleInPlaceSite_head, ppViewNew: POINTER(Windows.Win32.System.Ole.IOleDocumentView_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOleInPlaceActiveObject(ComPtr):
    extends: Windows.Win32.System.Ole.IOleWindow
    _iid_ = Guid('{00000117-0000-0000-c000-000000000046}')
    @commethod(5)
    def TranslateAccelerator(self, lpmsg: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnFrameWindowActivate(self, fActivate: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnDocWindowActivate(self, fActivate: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ResizeBorder(self, prcBorder: POINTER(Windows.Win32.Foundation.RECT_head), pUIWindow: Windows.Win32.System.Ole.IOleInPlaceUIWindow_head, fFrameWindow: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnableModeless(self, fEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IOleInPlaceFrame(ComPtr):
    extends: Windows.Win32.System.Ole.IOleInPlaceUIWindow
    _iid_ = Guid('{00000116-0000-0000-c000-000000000046}')
    @commethod(9)
    def InsertMenus(self, hmenuShared: Windows.Win32.UI.WindowsAndMessaging.HMENU, lpMenuWidths: POINTER(Windows.Win32.System.Ole.OLEMENUGROUPWIDTHS_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetMenu(self, hmenuShared: Windows.Win32.UI.WindowsAndMessaging.HMENU, holemenu: IntPtr, hwndActiveObject: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RemoveMenus(self, hmenuShared: Windows.Win32.UI.WindowsAndMessaging.HMENU) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetStatusText(self, pszStatusText: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def EnableModeless(self, fEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def TranslateAccelerator(self, lpmsg: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head), wID: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
class IOleInPlaceObject(ComPtr):
    extends: Windows.Win32.System.Ole.IOleWindow
    _iid_ = Guid('{00000113-0000-0000-c000-000000000046}')
    @commethod(5)
    def InPlaceDeactivate(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def UIDeactivate(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetObjectRects(self, lprcPosRect: POINTER(Windows.Win32.Foundation.RECT_head), lprcClipRect: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ReactivateAndUndo(self) -> Windows.Win32.Foundation.HRESULT: ...
class IOleInPlaceObjectWindowless(ComPtr):
    extends: Windows.Win32.System.Ole.IOleInPlaceObject
    _iid_ = Guid('{1c2056cc-5ef4-101b-8bc8-00aa003e3b29}')
    @commethod(9)
    def OnWindowMessage(self, msg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM, plResult: POINTER(Windows.Win32.Foundation.LRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDropTarget(self, ppDropTarget: POINTER(Windows.Win32.System.Ole.IDropTarget_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOleInPlaceSite(ComPtr):
    extends: Windows.Win32.System.Ole.IOleWindow
    _iid_ = Guid('{00000119-0000-0000-c000-000000000046}')
    @commethod(5)
    def CanInPlaceActivate(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnInPlaceActivate(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnUIActivate(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetWindowContext(self, ppFrame: POINTER(Windows.Win32.System.Ole.IOleInPlaceFrame_head), ppDoc: POINTER(Windows.Win32.System.Ole.IOleInPlaceUIWindow_head), lprcPosRect: POINTER(Windows.Win32.Foundation.RECT_head), lprcClipRect: POINTER(Windows.Win32.Foundation.RECT_head), lpFrameInfo: POINTER(Windows.Win32.System.Ole.OLEINPLACEFRAMEINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Scroll(self, scrollExtant: Windows.Win32.Foundation.SIZE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OnUIDeactivate(self, fUndoable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def OnInPlaceDeactivate(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def DiscardUndoState(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def DeactivateAndUndo(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def OnPosRectChange(self, lprcPosRect: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOleInPlaceSiteEx(ComPtr):
    extends: Windows.Win32.System.Ole.IOleInPlaceSite
    _iid_ = Guid('{9c2cad80-3424-11cf-b670-00aa004cd6d8}')
    @commethod(15)
    def OnInPlaceActivateEx(self, pfNoRedraw: POINTER(Windows.Win32.Foundation.BOOL), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def OnInPlaceDeactivateEx(self, fNoRedraw: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def RequestUIActivate(self) -> Windows.Win32.Foundation.HRESULT: ...
class IOleInPlaceSiteWindowless(ComPtr):
    extends: Windows.Win32.System.Ole.IOleInPlaceSiteEx
    _iid_ = Guid('{922eada0-3424-11cf-b670-00aa004cd6d8}')
    @commethod(18)
    def CanWindowlessActivate(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetCapture(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetCapture(self, fCapture: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetFocus(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetFocus(self, fFocus: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetDC(self, pRect: POINTER(Windows.Win32.Foundation.RECT_head), grfFlags: UInt32, phDC: POINTER(Windows.Win32.Graphics.Gdi.HDC)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def ReleaseDC(self, hDC: Windows.Win32.Graphics.Gdi.HDC) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def InvalidateRect(self, pRect: POINTER(Windows.Win32.Foundation.RECT_head), fErase: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def InvalidateRgn(self, hRGN: Windows.Win32.Graphics.Gdi.HRGN, fErase: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def ScrollRect(self, dx: Int32, dy: Int32, pRectScroll: POINTER(Windows.Win32.Foundation.RECT_head), pRectClip: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def AdjustRect(self, prc: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def OnDefWindowMessage(self, msg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM, plResult: POINTER(Windows.Win32.Foundation.LRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
class IOleInPlaceUIWindow(ComPtr):
    extends: Windows.Win32.System.Ole.IOleWindow
    _iid_ = Guid('{00000115-0000-0000-c000-000000000046}')
    @commethod(5)
    def GetBorder(self, lprectBorder: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RequestBorderSpace(self, pborderwidths: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetBorderSpace(self, pborderwidths: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetActiveObject(self, pActiveObject: Windows.Win32.System.Ole.IOleInPlaceActiveObject_head, pszObjName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IOleItemContainer(ComPtr):
    extends: Windows.Win32.System.Ole.IOleContainer
    _iid_ = Guid('{0000011c-0000-0000-c000-000000000046}')
    @commethod(6)
    def GetObject(self, pszItem: Windows.Win32.Foundation.PWSTR, dwSpeedNeeded: UInt32, pbc: Windows.Win32.System.Com.IBindCtx_head, riid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetObjectStorage(self, pszItem: Windows.Win32.Foundation.PWSTR, pbc: Windows.Win32.System.Com.IBindCtx_head, riid: POINTER(Guid), ppvStorage: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsRunning(self, pszItem: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IOleLink(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000011d-0000-0000-c000-000000000046}')
    @commethod(3)
    def SetUpdateOptions(self, dwUpdateOpt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetUpdateOptions(self, pdwUpdateOpt: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetSourceMoniker(self, pmk: Windows.Win32.System.Com.IMoniker_head, rclsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSourceMoniker(self, ppmk: POINTER(Windows.Win32.System.Com.IMoniker_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetSourceDisplayName(self, pszStatusText: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSourceDisplayName(self, ppszDisplayName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def BindToSource(self, bindflags: UInt32, pbc: Windows.Win32.System.Com.IBindCtx_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def BindIfRunning(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetBoundSource(self, ppunk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def UnbindSource(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Update(self, pbc: Windows.Win32.System.Com.IBindCtx_head) -> Windows.Win32.Foundation.HRESULT: ...
class IOleObject(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000112-0000-0000-c000-000000000046}')
    @commethod(3)
    def SetClientSite(self, pClientSite: Windows.Win32.System.Ole.IOleClientSite_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetClientSite(self, ppClientSite: POINTER(Windows.Win32.System.Ole.IOleClientSite_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetHostNames(self, szContainerApp: Windows.Win32.Foundation.PWSTR, szContainerObj: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Close(self, dwSaveOption: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetMoniker(self, dwWhichMoniker: UInt32, pmk: Windows.Win32.System.Com.IMoniker_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetMoniker(self, dwAssign: UInt32, dwWhichMoniker: UInt32, ppmk: POINTER(Windows.Win32.System.Com.IMoniker_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def InitFromData(self, pDataObject: Windows.Win32.System.Com.IDataObject_head, fCreation: Windows.Win32.Foundation.BOOL, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetClipboardData(self, dwReserved: UInt32, ppDataObject: POINTER(Windows.Win32.System.Com.IDataObject_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def DoVerb(self, iVerb: Int32, lpmsg: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head), pActiveSite: Windows.Win32.System.Ole.IOleClientSite_head, lindex: Int32, hwndParent: Windows.Win32.Foundation.HWND, lprcPosRect: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def EnumVerbs(self, ppEnumOleVerb: POINTER(Windows.Win32.System.Ole.IEnumOLEVERB_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Update(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def IsUpToDate(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetUserClassID(self, pClsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetUserType(self, dwFormOfType: UInt32, pszUserType: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetExtent(self, dwDrawAspect: Windows.Win32.System.Com.DVASPECT, psizel: POINTER(Windows.Win32.Foundation.SIZE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetExtent(self, dwDrawAspect: Windows.Win32.System.Com.DVASPECT, psizel: POINTER(Windows.Win32.Foundation.SIZE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Advise(self, pAdvSink: Windows.Win32.System.Com.IAdviseSink_head, pdwConnection: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def Unadvise(self, dwConnection: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def EnumAdvise(self, ppenumAdvise: POINTER(Windows.Win32.System.Com.IEnumSTATDATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetMiscStatus(self, dwAspect: Windows.Win32.System.Com.DVASPECT, pdwStatus: POINTER(Windows.Win32.System.Ole.OLEMISC)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetColorScheme(self, pLogpal: POINTER(Windows.Win32.Graphics.Gdi.LOGPALETTE_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOleParentUndoUnit(ComPtr):
    extends: Windows.Win32.System.Ole.IOleUndoUnit
    _iid_ = Guid('{a1faf330-ef97-11ce-9bc9-00aa00608e01}')
    @commethod(7)
    def Open(self, pPUU: Windows.Win32.System.Ole.IOleParentUndoUnit_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Close(self, pPUU: Windows.Win32.System.Ole.IOleParentUndoUnit_head, fCommit: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Add(self, pUU: Windows.Win32.System.Ole.IOleUndoUnit_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def FindUnit(self, pUU: Windows.Win32.System.Ole.IOleUndoUnit_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetParentState(self, pdwState: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IOleUILinkContainerA(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def GetNextLink(self, dwLink: UInt32) -> UInt32: ...
    @commethod(4)
    def SetLinkUpdateOptions(self, dwLink: UInt32, dwUpdateOpt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLinkUpdateOptions(self, dwLink: UInt32, lpdwUpdateOpt: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetLinkSource(self, dwLink: UInt32, lpszDisplayName: Windows.Win32.Foundation.PSTR, lenFileName: UInt32, pchEaten: POINTER(UInt32), fValidateSource: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetLinkSource(self, dwLink: UInt32, lplpszDisplayName: POINTER(Windows.Win32.Foundation.PSTR), lplenFileName: POINTER(UInt32), lplpszFullLinkType: POINTER(Windows.Win32.Foundation.PSTR), lplpszShortLinkType: POINTER(Windows.Win32.Foundation.PSTR), lpfSourceAvailable: POINTER(Windows.Win32.Foundation.BOOL), lpfIsSelected: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OpenLinkSource(self, dwLink: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def UpdateLink(self, dwLink: UInt32, fErrorMessage: Windows.Win32.Foundation.BOOL, fReserved: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CancelLink(self, dwLink: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IOleUILinkContainerW(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def GetNextLink(self, dwLink: UInt32) -> UInt32: ...
    @commethod(4)
    def SetLinkUpdateOptions(self, dwLink: UInt32, dwUpdateOpt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLinkUpdateOptions(self, dwLink: UInt32, lpdwUpdateOpt: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetLinkSource(self, dwLink: UInt32, lpszDisplayName: Windows.Win32.Foundation.PWSTR, lenFileName: UInt32, pchEaten: POINTER(UInt32), fValidateSource: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetLinkSource(self, dwLink: UInt32, lplpszDisplayName: POINTER(Windows.Win32.Foundation.PWSTR), lplenFileName: POINTER(UInt32), lplpszFullLinkType: POINTER(Windows.Win32.Foundation.PWSTR), lplpszShortLinkType: POINTER(Windows.Win32.Foundation.PWSTR), lpfSourceAvailable: POINTER(Windows.Win32.Foundation.BOOL), lpfIsSelected: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OpenLinkSource(self, dwLink: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def UpdateLink(self, dwLink: UInt32, fErrorMessage: Windows.Win32.Foundation.BOOL, fReserved: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CancelLink(self, dwLink: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IOleUILinkInfoA(ComPtr):
    extends: Windows.Win32.System.Ole.IOleUILinkContainerA
    @commethod(11)
    def GetLastUpdate(self, dwLink: UInt32, lpLastUpdate: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOleUILinkInfoW(ComPtr):
    extends: Windows.Win32.System.Ole.IOleUILinkContainerW
    @commethod(11)
    def GetLastUpdate(self, dwLink: UInt32, lpLastUpdate: POINTER(Windows.Win32.Foundation.FILETIME_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOleUIObjInfoA(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def GetObjectInfo(self, dwObject: UInt32, lpdwObjSize: POINTER(UInt32), lplpszLabel: POINTER(Windows.Win32.Foundation.PSTR), lplpszType: POINTER(Windows.Win32.Foundation.PSTR), lplpszShortType: POINTER(Windows.Win32.Foundation.PSTR), lplpszLocation: POINTER(Windows.Win32.Foundation.PSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetConvertInfo(self, dwObject: UInt32, lpClassID: POINTER(Guid), lpwFormat: POINTER(UInt16), lpConvertDefaultClassID: POINTER(Guid), lplpClsidExclude: POINTER(POINTER(Guid)), lpcClsidExclude: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ConvertObject(self, dwObject: UInt32, clsidNew: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetViewInfo(self, dwObject: UInt32, phMetaPict: POINTER(Windows.Win32.Foundation.HGLOBAL), pdvAspect: POINTER(UInt32), pnCurrentScale: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetViewInfo(self, dwObject: UInt32, hMetaPict: Windows.Win32.Foundation.HGLOBAL, dvAspect: UInt32, nCurrentScale: Int32, bRelativeToOrig: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IOleUIObjInfoW(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def GetObjectInfo(self, dwObject: UInt32, lpdwObjSize: POINTER(UInt32), lplpszLabel: POINTER(Windows.Win32.Foundation.PWSTR), lplpszType: POINTER(Windows.Win32.Foundation.PWSTR), lplpszShortType: POINTER(Windows.Win32.Foundation.PWSTR), lplpszLocation: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetConvertInfo(self, dwObject: UInt32, lpClassID: POINTER(Guid), lpwFormat: POINTER(UInt16), lpConvertDefaultClassID: POINTER(Guid), lplpClsidExclude: POINTER(POINTER(Guid)), lpcClsidExclude: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ConvertObject(self, dwObject: UInt32, clsidNew: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetViewInfo(self, dwObject: UInt32, phMetaPict: POINTER(Windows.Win32.Foundation.HGLOBAL), pdvAspect: POINTER(UInt32), pnCurrentScale: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetViewInfo(self, dwObject: UInt32, hMetaPict: Windows.Win32.Foundation.HGLOBAL, dvAspect: UInt32, nCurrentScale: Int32, bRelativeToOrig: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IOleUndoManager(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d001f200-ef97-11ce-9bc9-00aa00608e01}')
    @commethod(3)
    def Open(self, pPUU: Windows.Win32.System.Ole.IOleParentUndoUnit_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self, pPUU: Windows.Win32.System.Ole.IOleParentUndoUnit_head, fCommit: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Add(self, pUU: Windows.Win32.System.Ole.IOleUndoUnit_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetOpenParentState(self, pdwState: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DiscardFrom(self, pUU: Windows.Win32.System.Ole.IOleUndoUnit_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def UndoTo(self, pUU: Windows.Win32.System.Ole.IOleUndoUnit_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RedoTo(self, pUU: Windows.Win32.System.Ole.IOleUndoUnit_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EnumUndoable(self, ppEnum: POINTER(Windows.Win32.System.Ole.IEnumOleUndoUnits_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EnumRedoable(self, ppEnum: POINTER(Windows.Win32.System.Ole.IEnumOleUndoUnits_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetLastUndoDescription(self, pBstr: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetLastRedoDescription(self, pBstr: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Enable(self, fEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IOleUndoUnit(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{894ad3b0-ef97-11ce-9bc9-00aa00608e01}')
    @commethod(3)
    def Do(self, pUndoManager: Windows.Win32.System.Ole.IOleUndoManager_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDescription(self, pBstr: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetUnitType(self, pClsid: POINTER(Guid), plID: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnNextAdd(self) -> Windows.Win32.Foundation.HRESULT: ...
class IOleWindow(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000114-0000-0000-c000-000000000046}')
    @commethod(3)
    def GetWindow(self, phwnd: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ContextSensitiveHelp(self, fEnterMode: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IParseDisplayName(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000011a-0000-0000-c000-000000000046}')
    @commethod(3)
    def ParseDisplayName(self, pbc: Windows.Win32.System.Com.IBindCtx_head, pszDisplayName: Windows.Win32.Foundation.PWSTR, pchEaten: POINTER(UInt32), ppmkOut: POINTER(Windows.Win32.System.Com.IMoniker_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPerPropertyBrowsing(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{376bd3aa-3845-101b-84ed-08002b2ec713}')
    @commethod(3)
    def GetDisplayString(self, dispID: Int32, pBstr: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MapPropertyToPage(self, dispID: Int32, pClsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPredefinedStrings(self, dispID: Int32, pCaStringsOut: POINTER(Windows.Win32.System.Ole.CALPOLESTR_head), pCaCookiesOut: POINTER(Windows.Win32.System.Ole.CADWORD_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPredefinedValue(self, dispID: Int32, dwCookie: UInt32, pVarOut: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPersistPropertyBag(ComPtr):
    extends: Windows.Win32.System.Com.IPersist
    _iid_ = Guid('{37d84f60-42cb-11ce-8135-00aa004bb851}')
    @commethod(4)
    def InitNew(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Load(self, pPropBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, pErrorLog: Windows.Win32.System.Com.IErrorLog_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Save(self, pPropBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag_head, fClearDirty: Windows.Win32.Foundation.BOOL, fSaveAllProperties: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IPersistPropertyBag2(ComPtr):
    extends: Windows.Win32.System.Com.IPersist
    _iid_ = Guid('{22f55881-280b-11d0-a8a9-00a0c90c2004}')
    @commethod(4)
    def InitNew(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Load(self, pPropBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag2_head, pErrLog: Windows.Win32.System.Com.IErrorLog_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Save(self, pPropBag: Windows.Win32.System.Com.StructuredStorage.IPropertyBag2_head, fClearDirty: Windows.Win32.Foundation.BOOL, fSaveAllProperties: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsDirty(self) -> Windows.Win32.Foundation.HRESULT: ...
class IPicture(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7bf80980-bf32-101a-8bbb-00aa00300cab}')
    @commethod(3)
    def get_Handle(self, pHandle: POINTER(Windows.Win32.System.Ole.OLE_HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_hPal(self, phPal: POINTER(Windows.Win32.System.Ole.OLE_HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_Type(self, pType: POINTER(Windows.Win32.System.Ole.PICTYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Width(self, pWidth: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Height(self, pHeight: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Render(self, hDC: Windows.Win32.Graphics.Gdi.HDC, x: Int32, y: Int32, cx: Int32, cy: Int32, xSrc: Int32, ySrc: Int32, cxSrc: Int32, cySrc: Int32, pRcWBounds: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def set_hPal(self, hPal: Windows.Win32.System.Ole.OLE_HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CurDC(self, phDC: POINTER(Windows.Win32.Graphics.Gdi.HDC)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SelectPicture(self, hDCIn: Windows.Win32.Graphics.Gdi.HDC, phDCOut: POINTER(Windows.Win32.Graphics.Gdi.HDC), phBmpOut: POINTER(Windows.Win32.System.Ole.OLE_HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_KeepOriginalFormat(self, pKeep: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_KeepOriginalFormat(self, keep: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def PictureChanged(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SaveAsFile(self, pStream: Windows.Win32.System.Com.IStream_head, fSaveMemCopy: Windows.Win32.Foundation.BOOL, pCbSize: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Attributes(self, pDwAttr: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IPicture2(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f5185dd8-2012-4b0b-aad9-f052c6bd482b}')
    @commethod(3)
    def get_Handle(self, pHandle: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_hPal(self, phPal: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_Type(self, pType: POINTER(Int16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Width(self, pWidth: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Height(self, pHeight: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Render(self, hDC: Windows.Win32.Graphics.Gdi.HDC, x: Int32, y: Int32, cx: Int32, cy: Int32, xSrc: Int32, ySrc: Int32, cxSrc: Int32, cySrc: Int32, pRcWBounds: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def set_hPal(self, hPal: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CurDC(self, phDC: POINTER(Windows.Win32.Graphics.Gdi.HDC)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SelectPicture(self, hDCIn: Windows.Win32.Graphics.Gdi.HDC, phDCOut: POINTER(Windows.Win32.Graphics.Gdi.HDC), phBmpOut: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_KeepOriginalFormat(self, pKeep: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_KeepOriginalFormat(self, keep: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def PictureChanged(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SaveAsFile(self, pStream: Windows.Win32.System.Com.IStream_head, fSaveMemCopy: Windows.Win32.Foundation.BOOL, pCbSize: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Attributes(self, pDwAttr: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IPictureDisp(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{7bf80981-bf32-101a-8bbb-00aa00300cab}')
class IPointerInactive(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{55980ba0-35aa-11cf-b671-00aa004cd6d8}')
    @commethod(3)
    def GetActivationPolicy(self, pdwPolicy: POINTER(Windows.Win32.System.Ole.POINTERINACTIVE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnInactiveMouseMove(self, pRectBounds: POINTER(Windows.Win32.Foundation.RECT_head), x: Int32, y: Int32, grfKeyState: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnInactiveSetCursor(self, pRectBounds: POINTER(Windows.Win32.Foundation.RECT_head), x: Int32, y: Int32, dwMouseMsg: UInt32, fSetAlways: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IPrint(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b722bcc9-4e68-101b-a2bc-00aa00404770}')
    @commethod(3)
    def SetInitialPageNum(self, nFirstPage: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPageInfo(self, pnFirstPage: POINTER(Int32), pcPages: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Print(self, grfFlags: UInt32, pptd: POINTER(POINTER(Windows.Win32.System.Com.DVTARGETDEVICE_head)), ppPageSet: POINTER(POINTER(Windows.Win32.System.Ole.PAGESET_head)), pstgmOptions: POINTER(Windows.Win32.System.Com.STGMEDIUM_head), pcallback: Windows.Win32.System.Ole.IContinueCallback_head, nFirstPage: Int32, pcPagesPrinted: POINTER(Int32), pnLastPage: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyNotifySink(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9bfbbc02-eff1-101a-84ed-00aa00341d07}')
    @commethod(3)
    def OnChanged(self, dispID: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnRequestEdit(self, dispID: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyPage(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b196b28d-bab4-101a-b69c-00aa00341d07}')
    @commethod(3)
    def SetPageSite(self, pPageSite: Windows.Win32.System.Ole.IPropertyPageSite_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Activate(self, hWndParent: Windows.Win32.Foundation.HWND, pRect: POINTER(Windows.Win32.Foundation.RECT_head), bModal: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Deactivate(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPageInfo(self, pPageInfo: POINTER(Windows.Win32.System.Ole.PROPPAGEINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetObjects(self, cObjects: UInt32, ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Show(self, nCmdShow: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Move(self, pRect: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IsPageDirty(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Apply(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Help(self, pszHelpDir: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def TranslateAccelerator(self, pMsg: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyPage2(ComPtr):
    extends: Windows.Win32.System.Ole.IPropertyPage
    _iid_ = Guid('{01e44665-24ac-101b-84ed-08002b2ec713}')
    @commethod(14)
    def EditProperty(self, dispID: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IPropertyPageSite(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b196b28c-bab4-101a-b69c-00aa00341d07}')
    @commethod(3)
    def OnStatusChange(self, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLocaleID(self, pLocaleID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPageContainer(self, ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def TranslateAccelerator(self, pMsg: POINTER(Windows.Win32.UI.WindowsAndMessaging.MSG_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IProtectFocus(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d81f90a3-8156-44f7-ad28-5abb87003274}')
    @commethod(3)
    def AllowFocusChange(self, pfAllow: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IProtectedModeMenuServices(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{73c105ee-9dff-4a07-b83c-7eff290c266e}')
    @commethod(3)
    def CreateMenu(self, phMenu: POINTER(Windows.Win32.UI.WindowsAndMessaging.HMENU)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LoadMenu(self, pszModuleName: Windows.Win32.Foundation.PWSTR, pszMenuName: Windows.Win32.Foundation.PWSTR, phMenu: POINTER(Windows.Win32.UI.WindowsAndMessaging.HMENU)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def LoadMenuID(self, pszModuleName: Windows.Win32.Foundation.PWSTR, wResourceID: UInt16, phMenu: POINTER(Windows.Win32.UI.WindowsAndMessaging.HMENU)) -> Windows.Win32.Foundation.HRESULT: ...
class IProvideClassInfo(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b196b283-bab4-101a-b69c-00aa00341d07}')
    @commethod(3)
    def GetClassInfo(self, ppTI: POINTER(Windows.Win32.System.Com.ITypeInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IProvideClassInfo2(ComPtr):
    extends: Windows.Win32.System.Ole.IProvideClassInfo
    _iid_ = Guid('{a6bc3ac0-dbaa-11ce-9de3-00aa004bb851}')
    @commethod(4)
    def GetGUID(self, dwGuidKind: UInt32, pGUID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IProvideMultipleClassInfo(ComPtr):
    extends: Windows.Win32.System.Ole.IProvideClassInfo2
    _iid_ = Guid('{a7aba9c1-8983-11cf-8f20-00805f2cd064}')
    @commethod(5)
    def GetMultiTypeInfoCount(self, pcti: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetInfoOfIndex(self, iti: UInt32, dwFlags: Windows.Win32.System.Ole.MULTICLASSINFO_FLAGS, pptiCoClass: POINTER(Windows.Win32.System.Com.ITypeInfo_head), pdwTIFlags: POINTER(UInt32), pcdispidReserved: POINTER(UInt32), piidPrimary: POINTER(Guid), piidSource: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IProvideRuntimeContext(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{10e2414a-ec59-49d2-bc51-5add2c36febc}')
    @commethod(3)
    def GetCurrentSourceContext(self, pdwContext: POINTER(UIntPtr), pfExecutingGlobalCode: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IQuickActivate(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cf51ed10-62fe-11cf-bf86-00a0c9034836}')
    @commethod(3)
    def QuickActivate(self, pQaContainer: POINTER(Windows.Win32.System.Ole.QACONTAINER_head), pQaControl: POINTER(Windows.Win32.System.Ole.QACONTROL_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetContentExtent(self, pSizel: POINTER(Windows.Win32.Foundation.SIZE_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetContentExtent(self, pSizel: POINTER(Windows.Win32.Foundation.SIZE_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRecordInfo(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000002f-0000-0000-c000-000000000046}')
    @commethod(3)
    def RecordInit(self, pvNew: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RecordClear(self, pvExisting: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RecordCopy(self, pvExisting: c_void_p, pvNew: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetGuid(self, pguid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetName(self, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSize(self, pcbSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetTypeInfo(self, ppTypeInfo: POINTER(Windows.Win32.System.Com.ITypeInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetField(self, pvData: c_void_p, szFieldName: Windows.Win32.Foundation.PWSTR, pvarField: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetFieldNoCopy(self, pvData: c_void_p, szFieldName: Windows.Win32.Foundation.PWSTR, pvarField: POINTER(Windows.Win32.System.Variant.VARIANT_head), ppvDataCArray: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def PutField(self, wFlags: UInt32, pvData: c_void_p, szFieldName: Windows.Win32.Foundation.PWSTR, pvarField: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def PutFieldNoCopy(self, wFlags: UInt32, pvData: c_void_p, szFieldName: Windows.Win32.Foundation.PWSTR, pvarField: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetFieldNames(self, pcNames: POINTER(UInt32), rgBstrNames: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def IsMatchingType(self, pRecordInfo: Windows.Win32.System.Ole.IRecordInfo_head) -> Windows.Win32.Foundation.BOOL: ...
    @commethod(16)
    def RecordCreate(self) -> c_void_p: ...
    @commethod(17)
    def RecordCreateCopy(self, pvSource: c_void_p, ppvDest: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def RecordDestroy(self, pvRecord: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
class ISimpleFrameSite(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{742b0e01-14e6-101b-914e-00aa00300cab}')
    @commethod(3)
    def PreMessageFilter(self, hWnd: Windows.Win32.Foundation.HWND, msg: UInt32, wp: Windows.Win32.Foundation.WPARAM, lp: Windows.Win32.Foundation.LPARAM, plResult: POINTER(Windows.Win32.Foundation.LRESULT), pdwCookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PostMessageFilter(self, hWnd: Windows.Win32.Foundation.HWND, msg: UInt32, wp: Windows.Win32.Foundation.WPARAM, lp: Windows.Win32.Foundation.LPARAM, plResult: POINTER(Windows.Win32.Foundation.LRESULT), dwCookie: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISpecifyPropertyPages(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b196b28b-bab4-101a-b69c-00aa00341d07}')
    @commethod(3)
    def GetPages(self, pPages: POINTER(Windows.Win32.System.Ole.CAUUID_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITypeChangeEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00020410-0000-0000-c000-000000000046}')
    @commethod(3)
    def RequestTypeChange(self, changeKind: Windows.Win32.System.Ole.CHANGEKIND, pTInfoBefore: Windows.Win32.System.Com.ITypeInfo_head, pStrName: Windows.Win32.Foundation.PWSTR, pfCancel: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AfterTypeChange(self, changeKind: Windows.Win32.System.Ole.CHANGEKIND, pTInfoAfter: Windows.Win32.System.Com.ITypeInfo_head, pStrName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ITypeFactory(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000002e-0000-0000-c000-000000000046}')
    @commethod(3)
    def CreateFromTypeInfo(self, pTypeInfo: Windows.Win32.System.Com.ITypeInfo_head, riid: POINTER(Guid), ppv: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITypeMarshal(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000002d-0000-0000-c000-000000000046}')
    @commethod(3)
    def Size(self, pvType: c_void_p, dwDestContext: UInt32, pvDestContext: c_void_p, pSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Marshal(self, pvType: c_void_p, dwDestContext: UInt32, pvDestContext: c_void_p, cbBufferLength: UInt32, pBuffer: POINTER(Byte), pcbWritten: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Unmarshal(self, pvType: c_void_p, dwFlags: UInt32, cbBufferLength: UInt32, pBuffer: POINTER(Byte), pcbRead: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Free(self, pvType: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
class IVBFormat(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9849fd60-3768-101b-8d72-ae6164ffe3cf}')
    @commethod(3)
    def Format(self, vData: POINTER(Windows.Win32.System.Variant.VARIANT_head), bstrFormat: Windows.Win32.Foundation.BSTR, lpBuffer: c_void_p, cb: UInt16, lcid: Int32, sFirstDayOfWeek: Int16, sFirstWeekOfYear: UInt16, rcb: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
class IVBGetControl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{40a050a0-3c31-101b-a82e-08002b2b2337}')
    @commethod(3)
    def EnumControls(self, dwOleContF: UInt32, dwWhich: Windows.Win32.System.Ole.ENUM_CONTROLS_WHICH_FLAGS, ppenumUnk: POINTER(Windows.Win32.System.Com.IEnumUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IVariantChangeType(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a6ef9862-c720-11d0-9337-00a0c90dcaa9}')
    @commethod(3)
    def ChangeType(self, pvarDst: POINTER(Windows.Win32.System.Variant.VARIANT_head), pvarSrc: POINTER(Windows.Win32.System.Variant.VARIANT_head), lcid: UInt32, vtNew: Windows.Win32.System.Variant.VARENUM) -> Windows.Win32.Foundation.HRESULT: ...
class IViewObject(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000010d-0000-0000-c000-000000000046}')
    @commethod(3)
    def Draw(self, dwDrawAspect: Windows.Win32.System.Com.DVASPECT, lindex: Int32, pvAspect: c_void_p, ptd: POINTER(Windows.Win32.System.Com.DVTARGETDEVICE_head), hdcTargetDev: Windows.Win32.Graphics.Gdi.HDC, hdcDraw: Windows.Win32.Graphics.Gdi.HDC, lprcBounds: POINTER(Windows.Win32.Foundation.RECTL_head), lprcWBounds: POINTER(Windows.Win32.Foundation.RECTL_head), pfnContinue: IntPtr, dwContinue: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetColorSet(self, dwDrawAspect: Windows.Win32.System.Com.DVASPECT, lindex: Int32, pvAspect: c_void_p, ptd: POINTER(Windows.Win32.System.Com.DVTARGETDEVICE_head), hicTargetDev: Windows.Win32.Graphics.Gdi.HDC, ppColorSet: POINTER(POINTER(Windows.Win32.Graphics.Gdi.LOGPALETTE_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Freeze(self, dwDrawAspect: Windows.Win32.System.Com.DVASPECT, lindex: Int32, pvAspect: c_void_p, pdwFreeze: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Unfreeze(self, dwFreeze: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetAdvise(self, aspects: Windows.Win32.System.Com.DVASPECT, advf: UInt32, pAdvSink: Windows.Win32.System.Com.IAdviseSink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetAdvise(self, pAspects: POINTER(UInt32), pAdvf: POINTER(UInt32), ppAdvSink: POINTER(Windows.Win32.System.Com.IAdviseSink_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IViewObject2(ComPtr):
    extends: Windows.Win32.System.Ole.IViewObject
    _iid_ = Guid('{00000127-0000-0000-c000-000000000046}')
    @commethod(9)
    def GetExtent(self, dwDrawAspect: Windows.Win32.System.Com.DVASPECT, lindex: Int32, ptd: POINTER(Windows.Win32.System.Com.DVTARGETDEVICE_head), lpsizel: POINTER(Windows.Win32.Foundation.SIZE_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IViewObjectEx(ComPtr):
    extends: Windows.Win32.System.Ole.IViewObject2
    _iid_ = Guid('{3af24292-0c96-11ce-a0cf-00aa00600ab8}')
    @commethod(10)
    def GetRect(self, dwAspect: UInt32, pRect: POINTER(Windows.Win32.Foundation.RECTL_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetViewStatus(self, pdwStatus: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def QueryHitPoint(self, dwAspect: UInt32, pRectBounds: POINTER(Windows.Win32.Foundation.RECT_head), ptlLoc: Windows.Win32.Foundation.POINT, lCloseHint: Int32, pHitResult: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def QueryHitRect(self, dwAspect: UInt32, pRectBounds: POINTER(Windows.Win32.Foundation.RECT_head), pRectLoc: POINTER(Windows.Win32.Foundation.RECT_head), lCloseHint: Int32, pHitResult: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetNaturalExtent(self, dwAspect: Windows.Win32.System.Com.DVASPECT, lindex: Int32, ptd: POINTER(Windows.Win32.System.Com.DVTARGETDEVICE_head), hicTargetDev: Windows.Win32.Graphics.Gdi.HDC, pExtentInfo: POINTER(Windows.Win32.System.Ole.DVEXTENTINFO_head), pSizel: POINTER(Windows.Win32.Foundation.SIZE_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IZoomEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{41b68150-904c-4e17-a0ba-a438182e359d}')
    @commethod(3)
    def OnZoomPercentChanged(self, ulZoomPercent: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
KEYMODIFIERS = UInt32
KEYMOD_SHIFT: KEYMODIFIERS = 1
KEYMOD_CONTROL: KEYMODIFIERS = 2
KEYMOD_ALT: KEYMODIFIERS = 4
LIBFLAGS = Int32
LIBFLAG_FRESTRICTED: LIBFLAGS = 1
LIBFLAG_FCONTROL: LIBFLAGS = 2
LIBFLAG_FHIDDEN: LIBFLAGS = 4
LIBFLAG_FHASDISKIMAGE: LIBFLAGS = 8
class LICINFO(EasyCastStructure):
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
class METHODDATA(EasyCastStructure):
    szName: Windows.Win32.Foundation.PWSTR
    ppdata: POINTER(Windows.Win32.System.Ole.PARAMDATA_head)
    dispid: Int32
    iMeth: UInt32
    cc: Windows.Win32.System.Com.CALLCONV
    cArgs: UInt32
    wFlags: UInt16
    vtReturn: Windows.Win32.System.Variant.VARENUM
MULTICLASSINFO_FLAGS = UInt32
MULTICLASSINFO_GETTYPEINFO: MULTICLASSINFO_FLAGS = 1
MULTICLASSINFO_GETNUMRESERVEDDISPIDS: MULTICLASSINFO_FLAGS = 2
MULTICLASSINFO_GETIIDPRIMARY: MULTICLASSINFO_FLAGS = 4
MULTICLASSINFO_GETIIDSOURCE: MULTICLASSINFO_FLAGS = 8
class NUMPARSE(EasyCastStructure):
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
class OBJECTDESCRIPTOR(EasyCastStructure):
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
class OCPFIPARAMS(EasyCastStructure):
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
class OLECMD(EasyCastStructure):
    cmdID: UInt32
    cmdf: UInt32
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
class OLECMDTEXT(EasyCastStructure):
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
class OLEINPLACEFRAMEINFO(EasyCastStructure):
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
class OLEMENUGROUPWIDTHS(EasyCastStructure):
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
class OLEUIBUSYA(EasyCastStructure):
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
class OLEUIBUSYW(EasyCastStructure):
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
class OLEUICHANGEICONA(EasyCastStructure):
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
class OLEUICHANGEICONW(EasyCastStructure):
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
class OLEUICHANGESOURCEA(EasyCastStructure):
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
class OLEUICHANGESOURCEW(EasyCastStructure):
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
class OLEUICONVERTA(EasyCastStructure):
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
class OLEUICONVERTW(EasyCastStructure):
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
class OLEUIEDITLINKSA(EasyCastStructure):
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
class OLEUIEDITLINKSW(EasyCastStructure):
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
class OLEUIGNRLPROPSA(EasyCastStructure):
    cbStruct: UInt32
    dwFlags: UInt32
    dwReserved1: UInt32 * 2
    lpfnHook: Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: Windows.Win32.Foundation.LPARAM
    dwReserved2: UInt32 * 3
    lpOP: POINTER(Windows.Win32.System.Ole.OLEUIOBJECTPROPSA_head)
class OLEUIGNRLPROPSW(EasyCastStructure):
    cbStruct: UInt32
    dwFlags: UInt32
    dwReserved1: UInt32 * 2
    lpfnHook: Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: Windows.Win32.Foundation.LPARAM
    dwReserved2: UInt32 * 3
    lpOP: POINTER(Windows.Win32.System.Ole.OLEUIOBJECTPROPSW_head)
class OLEUIINSERTOBJECTA(EasyCastStructure):
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
class OLEUIINSERTOBJECTW(EasyCastStructure):
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
class OLEUILINKPROPSA(EasyCastStructure):
    cbStruct: UInt32
    dwFlags: UInt32
    dwReserved1: UInt32 * 2
    lpfnHook: Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: Windows.Win32.Foundation.LPARAM
    dwReserved2: UInt32 * 3
    lpOP: POINTER(Windows.Win32.System.Ole.OLEUIOBJECTPROPSA_head)
class OLEUILINKPROPSW(EasyCastStructure):
    cbStruct: UInt32
    dwFlags: UInt32
    dwReserved1: UInt32 * 2
    lpfnHook: Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: Windows.Win32.Foundation.LPARAM
    dwReserved2: UInt32 * 3
    lpOP: POINTER(Windows.Win32.System.Ole.OLEUIOBJECTPROPSW_head)
class OLEUIOBJECTPROPSA(EasyCastStructure):
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
class OLEUIOBJECTPROPSW(EasyCastStructure):
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
class OLEUIPASTEENTRYA(EasyCastStructure):
    fmtetc: Windows.Win32.System.Com.FORMATETC
    lpstrFormatName: Windows.Win32.Foundation.PSTR
    lpstrResultText: Windows.Win32.Foundation.PSTR
    dwFlags: UInt32
    dwScratchSpace: UInt32
class OLEUIPASTEENTRYW(EasyCastStructure):
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
class OLEUIPASTESPECIALA(EasyCastStructure):
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
class OLEUIPASTESPECIALW(EasyCastStructure):
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
class OLEUIVIEWPROPSA(EasyCastStructure):
    cbStruct: UInt32
    dwFlags: Windows.Win32.System.Ole.VIEW_OBJECT_PROPERTIES_FLAGS
    dwReserved1: UInt32 * 2
    lpfnHook: Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: Windows.Win32.Foundation.LPARAM
    dwReserved2: UInt32 * 3
    lpOP: POINTER(Windows.Win32.System.Ole.OLEUIOBJECTPROPSA_head)
    nScaleMin: Int32
    nScaleMax: Int32
class OLEUIVIEWPROPSW(EasyCastStructure):
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
class OLEVERB(EasyCastStructure):
    lVerb: Windows.Win32.System.Ole.OLEIVERB
    lpszVerbName: Windows.Win32.Foundation.PWSTR
    fuFlags: Windows.Win32.UI.WindowsAndMessaging.MENU_ITEM_FLAGS
    grfAttribs: UInt32
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
class PAGERANGE(EasyCastStructure):
    nFromPage: Int32
    nToPage: Int32
class PAGESET(EasyCastStructure):
    cbStruct: UInt32
    fOddPages: Windows.Win32.Foundation.BOOL
    fEvenPages: Windows.Win32.Foundation.BOOL
    cPageRange: UInt32
    rgPages: Windows.Win32.System.Ole.PAGERANGE * 1
class PARAMDATA(EasyCastStructure):
    szName: Windows.Win32.Foundation.PWSTR
    vt: Windows.Win32.System.Variant.VARENUM
class PARAMDESC(EasyCastStructure):
    pparamdescex: POINTER(Windows.Win32.System.Ole.PARAMDESCEX_head)
    wParamFlags: Windows.Win32.System.Ole.PARAMFLAGS
class PARAMDESCEX(EasyCastStructure):
    cBytes: UInt32
    varDefaultValue: Windows.Win32.System.Variant.VARIANT
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
class PICTDESC(EasyCastStructure):
    cbSizeofstruct: UInt32
    picType: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        bmp: _bmp_e__Struct
        wmf: _wmf_e__Struct
        icon: _icon_e__Struct
        emf: _emf_e__Struct
        class _bmp_e__Struct(EasyCastStructure):
            hbitmap: Windows.Win32.Graphics.Gdi.HBITMAP
            hpal: Windows.Win32.Graphics.Gdi.HPALETTE
        class _wmf_e__Struct(EasyCastStructure):
            hmeta: Windows.Win32.Graphics.Gdi.HMETAFILE
            xExt: Int32
            yExt: Int32
        class _icon_e__Struct(EasyCastStructure):
            hicon: Windows.Win32.UI.WindowsAndMessaging.HICON
        class _emf_e__Struct(EasyCastStructure):
            hemf: Windows.Win32.Graphics.Gdi.HENHMETAFILE
PICTUREATTRIBUTES = Int32
PICTURE_SCALABLE: PICTUREATTRIBUTES = 1
PICTURE_TRANSPARENT: PICTUREATTRIBUTES = 2
PICTYPE = Int16
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
class POINTF(EasyCastStructure):
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
class PROPPAGEINFO(EasyCastStructure):
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
class QACONTAINER(EasyCastStructure):
    cbSize: UInt32
    pClientSite: Windows.Win32.System.Ole.IOleClientSite_head
    pAdviseSink: Windows.Win32.System.Ole.IAdviseSinkEx_head
    pPropertyNotifySink: Windows.Win32.System.Ole.IPropertyNotifySink_head
    pUnkEventSink: Windows.Win32.System.Com.IUnknown_head
    dwAmbientFlags: UInt32
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
class QACONTROL(EasyCastStructure):
    cbSize: UInt32
    dwMiscStatus: UInt32
    dwViewStatus: UInt32
    dwEventCookie: UInt32
    dwPropNotifyCookie: UInt32
    dwPointerActivationPolicy: UInt32
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
class SAFEARRAYUNION(EasyCastStructure):
    sfType: UInt32
    u: _u_e__Struct
    class _u_e__Struct(EasyCastUnion):
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
class SAFEARR_BRECORD(EasyCastStructure):
    Size: UInt32
    aRecord: POINTER(POINTER(Windows.Win32.System.Ole._wireBRECORD_head))
class SAFEARR_BSTR(EasyCastStructure):
    Size: UInt32
    aBstr: POINTER(POINTER(Windows.Win32.System.Com.FLAGGED_WORD_BLOB_head))
class SAFEARR_DISPATCH(EasyCastStructure):
    Size: UInt32
    apDispatch: POINTER(Windows.Win32.System.Com.IDispatch_head)
class SAFEARR_HAVEIID(EasyCastStructure):
    Size: UInt32
    apUnknown: POINTER(Windows.Win32.System.Com.IUnknown_head)
    iid: Guid
class SAFEARR_UNKNOWN(EasyCastStructure):
    Size: UInt32
    apUnknown: POINTER(Windows.Win32.System.Com.IUnknown_head)
class SAFEARR_VARIANT(EasyCastStructure):
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
class UDATE(EasyCastStructure):
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
class _wireBRECORD(EasyCastStructure):
    fFlags: UInt32
    clSize: UInt32
    pRecInfo: Windows.Win32.System.Ole.IRecordInfo_head
    pRecord: POINTER(Byte)
class _wireSAFEARRAY(EasyCastStructure):
    cDims: UInt16
    fFeatures: UInt16
    cbElements: UInt32
    cLocks: UInt32
    uArrayStructs: Windows.Win32.System.Ole.SAFEARRAYUNION
    rgsabound: Windows.Win32.System.Com.SAFEARRAYBOUND * 1
class _wireVARIANT(EasyCastStructure):
    clSize: UInt32
    rpcReserved: UInt32
    vt: UInt16
    wReserved1: UInt16
    wReserved2: UInt16
    wReserved3: UInt16
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
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
        pbVal: POINTER(Byte)
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
