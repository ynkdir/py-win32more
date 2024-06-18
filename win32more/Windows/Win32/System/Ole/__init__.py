from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.Media
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.StructuredStorage
import win32more.Windows.Win32.System.Memory
import win32more.Windows.Win32.System.Ole
import win32more.Windows.Win32.System.SystemServices
import win32more.Windows.Win32.System.Variant
import win32more.Windows.Win32.UI.Controls
import win32more.Windows.Win32.UI.Controls.Dialogs
import win32more.Windows.Win32.UI.WindowsAndMessaging
ACTIVATEFLAGS = Int32
ACTIVATE_WINDOWLESS: win32more.Windows.Win32.System.Ole.ACTIVATEFLAGS = 1
ACTIVEOBJECT_FLAGS = UInt32
ACTIVEOBJECT_STRONG: win32more.Windows.Win32.System.Ole.ACTIVEOBJECT_FLAGS = 0
ACTIVEOBJECT_WEAK: win32more.Windows.Win32.System.Ole.ACTIVEOBJECT_FLAGS = 1
class ARRAYDESC(Structure):
    tdescElem: win32more.Windows.Win32.System.Com.TYPEDESC
    cDims: UInt16
    rgbounds: win32more.Windows.Win32.System.Com.SAFEARRAYBOUND * 1
CTL_E_ILLEGALFUNCTIONCALL: Int32 = -2146828283
CONNECT_E_FIRST: Int32 = -2147220992
SELFREG_E_FIRST: Int32 = -2147220992
PERPROP_E_FIRST: Int32 = -2147220992
OLECMDERR_E_FIRST: win32more.Windows.Win32.Foundation.HRESULT = -2147221248
OLECMDERR_E_DISABLED: win32more.Windows.Win32.Foundation.HRESULT = -2147221247
OLECMDERR_E_NOHELP: win32more.Windows.Win32.Foundation.HRESULT = -2147221246
OLECMDERR_E_CANCELED: win32more.Windows.Win32.Foundation.HRESULT = -2147221245
OLECMDERR_E_UNKNOWNGROUP: win32more.Windows.Win32.Foundation.HRESULT = -2147221244
CONNECT_E_NOCONNECTION: win32more.Windows.Win32.Foundation.HRESULT = -2147220992
CONNECT_E_ADVISELIMIT: win32more.Windows.Win32.Foundation.HRESULT = -2147220991
CONNECT_E_CANNOTCONNECT: win32more.Windows.Win32.Foundation.HRESULT = -2147220990
CONNECT_E_OVERRIDDEN: win32more.Windows.Win32.Foundation.HRESULT = -2147220989
SELFREG_E_TYPELIB: win32more.Windows.Win32.Foundation.HRESULT = -2147220992
SELFREG_E_CLASS: win32more.Windows.Win32.Foundation.HRESULT = -2147220991
PERPROP_E_NOPAGEAVAILABLE: win32more.Windows.Win32.Foundation.HRESULT = -2147220992
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
CONNECT_E_LAST: win32more.Windows.Win32.Foundation.HRESULT = -2147220977
CONNECT_S_FIRST: win32more.Windows.Win32.Foundation.HRESULT = 262656
CONNECT_S_LAST: win32more.Windows.Win32.Foundation.HRESULT = 262671
SELFREG_E_LAST: win32more.Windows.Win32.Foundation.HRESULT = -2147220977
SELFREG_S_FIRST: win32more.Windows.Win32.Foundation.HRESULT = 262656
SELFREG_S_LAST: win32more.Windows.Win32.Foundation.HRESULT = 262671
PERPROP_E_LAST: win32more.Windows.Win32.Foundation.HRESULT = -2147220977
PERPROP_S_FIRST: win32more.Windows.Win32.Foundation.HRESULT = 262656
PERPROP_S_LAST: win32more.Windows.Win32.Foundation.HRESULT = 262671
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
OLESTREAM_CONVERSION_DEFAULT: Int32 = 0
OLESTREAM_CONVERSION_DISABLEOLELINK: Int32 = 1
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
def SafeArrayAllocDescriptor(cDims: UInt32, ppsaOut: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayAllocDescriptorEx(vt: win32more.Windows.Win32.System.Variant.VARENUM, cDims: UInt32, ppsaOut: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayAllocData(psa: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayCreate(vt: win32more.Windows.Win32.System.Variant.VARENUM, cDims: UInt32, rgsabound: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAYBOUND)) -> POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY): ...
@winfunctype('OLEAUT32.dll')
def SafeArrayCreateEx(vt: win32more.Windows.Win32.System.Variant.VARENUM, cDims: UInt32, rgsabound: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAYBOUND), pvExtra: VoidPtr) -> POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY): ...
@winfunctype('OLEAUT32.dll')
def SafeArrayCopyData(psaSource: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), psaTarget: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayReleaseDescriptor(psa: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> Void: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayDestroyDescriptor(psa: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayReleaseData(pData: VoidPtr) -> Void: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayDestroyData(psa: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayAddRef(psa: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), ppDataToRelease: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayDestroy(psa: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayRedim(psa: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), psaboundNew: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAYBOUND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayGetDim(psa: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> UInt32: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayGetElemsize(psa: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> UInt32: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayGetUBound(psa: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), nDim: UInt32, plUbound: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayGetLBound(psa: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), nDim: UInt32, plLbound: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayLock(psa: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayUnlock(psa: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayAccessData(psa: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), ppvData: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayUnaccessData(psa: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayGetElement(psa: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), rgIndices: POINTER(Int32), pv: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayPutElement(psa: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), rgIndices: POINTER(Int32), pv: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayCopy(psa: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), ppsaOut: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayPtrOfIndex(psa: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), rgIndices: POINTER(Int32), ppvData: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArraySetRecordInfo(psa: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), prinfo: win32more.Windows.Win32.System.Ole.IRecordInfo) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayGetRecordInfo(psa: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), prinfo: POINTER(win32more.Windows.Win32.System.Ole.IRecordInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArraySetIID(psa: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), guid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayGetIID(psa: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), pguid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayGetVartype(psa: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), pvt: POINTER(win32more.Windows.Win32.System.Variant.VARENUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def SafeArrayCreateVector(vt: win32more.Windows.Win32.System.Variant.VARENUM, lLbound: Int32, cElements: UInt32) -> POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY): ...
@winfunctype('OLEAUT32.dll')
def SafeArrayCreateVectorEx(vt: win32more.Windows.Win32.System.Variant.VARENUM, lLbound: Int32, cElements: UInt32, pvExtra: VoidPtr) -> POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY): ...
@winfunctype('OLEAUT32.dll')
def VectorFromBstr(bstr: win32more.Windows.Win32.Foundation.BSTR, ppsa: POINTER(POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def BstrFromVector(psa: POINTER(win32more.Windows.Win32.System.Com.SAFEARRAY), pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromI2(sIn: Int16, pbOut: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromI4(lIn: Int32, pbOut: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromI8(i64In: Int64, pbOut: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromR4(fltIn: Single, pbOut: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromR8(dblIn: Double, pbOut: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromCy(cyIn: win32more.Windows.Win32.System.Com.CY, pbOut: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromDate(dateIn: Double, pbOut: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromStr(strIn: win32more.Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, pbOut: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromDisp(pdispIn: win32more.Windows.Win32.System.Com.IDispatch, lcid: UInt32, pbOut: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromBool(boolIn: win32more.Windows.Win32.Foundation.VARIANT_BOOL, pbOut: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromI1(cIn: win32more.Windows.Win32.Foundation.CHAR, pbOut: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromUI2(uiIn: UInt16, pbOut: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromUI4(ulIn: UInt32, pbOut: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromUI8(ui64In: UInt64, pbOut: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI1FromDec(pdecIn: POINTER(win32more.Windows.Win32.Foundation.DECIMAL), pbOut: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI2FromUI1(bIn: Byte, psOut: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI2FromI4(lIn: Int32, psOut: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI2FromI8(i64In: Int64, psOut: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI2FromR4(fltIn: Single, psOut: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI2FromR8(dblIn: Double, psOut: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI2FromCy(cyIn: win32more.Windows.Win32.System.Com.CY, psOut: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI2FromDate(dateIn: Double, psOut: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI2FromStr(strIn: win32more.Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, psOut: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI2FromDisp(pdispIn: win32more.Windows.Win32.System.Com.IDispatch, lcid: UInt32, psOut: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI2FromBool(boolIn: win32more.Windows.Win32.Foundation.VARIANT_BOOL, psOut: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI2FromI1(cIn: win32more.Windows.Win32.Foundation.CHAR, psOut: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI2FromUI2(uiIn: UInt16, psOut: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI2FromUI4(ulIn: UInt32, psOut: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI2FromUI8(ui64In: UInt64, psOut: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI2FromDec(pdecIn: POINTER(win32more.Windows.Win32.Foundation.DECIMAL), psOut: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI4FromUI1(bIn: Byte, plOut: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI4FromI2(sIn: Int16, plOut: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI4FromI8(i64In: Int64, plOut: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI4FromR4(fltIn: Single, plOut: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI4FromR8(dblIn: Double, plOut: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI4FromCy(cyIn: win32more.Windows.Win32.System.Com.CY, plOut: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI4FromDate(dateIn: Double, plOut: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI4FromStr(strIn: win32more.Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, plOut: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI4FromDisp(pdispIn: win32more.Windows.Win32.System.Com.IDispatch, lcid: UInt32, plOut: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI4FromBool(boolIn: win32more.Windows.Win32.Foundation.VARIANT_BOOL, plOut: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI4FromI1(cIn: win32more.Windows.Win32.Foundation.CHAR, plOut: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI4FromUI2(uiIn: UInt16, plOut: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI4FromUI4(ulIn: UInt32, plOut: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI4FromUI8(ui64In: UInt64, plOut: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI4FromDec(pdecIn: POINTER(win32more.Windows.Win32.Foundation.DECIMAL), plOut: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI8FromUI1(bIn: Byte, pi64Out: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI8FromI2(sIn: Int16, pi64Out: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI8FromR4(fltIn: Single, pi64Out: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI8FromR8(dblIn: Double, pi64Out: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI8FromCy(cyIn: win32more.Windows.Win32.System.Com.CY, pi64Out: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI8FromDate(dateIn: Double, pi64Out: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI8FromStr(strIn: win32more.Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, pi64Out: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI8FromDisp(pdispIn: win32more.Windows.Win32.System.Com.IDispatch, lcid: UInt32, pi64Out: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI8FromBool(boolIn: win32more.Windows.Win32.Foundation.VARIANT_BOOL, pi64Out: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI8FromI1(cIn: win32more.Windows.Win32.Foundation.CHAR, pi64Out: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI8FromUI2(uiIn: UInt16, pi64Out: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI8FromUI4(ulIn: UInt32, pi64Out: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI8FromUI8(ui64In: UInt64, pi64Out: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI8FromDec(pdecIn: POINTER(win32more.Windows.Win32.Foundation.DECIMAL), pi64Out: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4FromUI1(bIn: Byte, pfltOut: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4FromI2(sIn: Int16, pfltOut: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4FromI4(lIn: Int32, pfltOut: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4FromI8(i64In: Int64, pfltOut: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4FromR8(dblIn: Double, pfltOut: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4FromCy(cyIn: win32more.Windows.Win32.System.Com.CY, pfltOut: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4FromDate(dateIn: Double, pfltOut: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4FromStr(strIn: win32more.Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, pfltOut: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4FromDisp(pdispIn: win32more.Windows.Win32.System.Com.IDispatch, lcid: UInt32, pfltOut: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4FromBool(boolIn: win32more.Windows.Win32.Foundation.VARIANT_BOOL, pfltOut: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4FromI1(cIn: win32more.Windows.Win32.Foundation.CHAR, pfltOut: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4FromUI2(uiIn: UInt16, pfltOut: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4FromUI4(ulIn: UInt32, pfltOut: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4FromUI8(ui64In: UInt64, pfltOut: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4FromDec(pdecIn: POINTER(win32more.Windows.Win32.Foundation.DECIMAL), pfltOut: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8FromUI1(bIn: Byte, pdblOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8FromI2(sIn: Int16, pdblOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8FromI4(lIn: Int32, pdblOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8FromI8(i64In: Int64, pdblOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8FromR4(fltIn: Single, pdblOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8FromCy(cyIn: win32more.Windows.Win32.System.Com.CY, pdblOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8FromDate(dateIn: Double, pdblOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8FromStr(strIn: win32more.Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, pdblOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8FromDisp(pdispIn: win32more.Windows.Win32.System.Com.IDispatch, lcid: UInt32, pdblOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8FromBool(boolIn: win32more.Windows.Win32.Foundation.VARIANT_BOOL, pdblOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8FromI1(cIn: win32more.Windows.Win32.Foundation.CHAR, pdblOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8FromUI2(uiIn: UInt16, pdblOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8FromUI4(ulIn: UInt32, pdblOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8FromUI8(ui64In: UInt64, pdblOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8FromDec(pdecIn: POINTER(win32more.Windows.Win32.Foundation.DECIMAL), pdblOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromUI1(bIn: Byte, pdateOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromI2(sIn: Int16, pdateOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromI4(lIn: Int32, pdateOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromI8(i64In: Int64, pdateOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromR4(fltIn: Single, pdateOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromR8(dblIn: Double, pdateOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromCy(cyIn: win32more.Windows.Win32.System.Com.CY, pdateOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromStr(strIn: win32more.Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, pdateOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromDisp(pdispIn: win32more.Windows.Win32.System.Com.IDispatch, lcid: UInt32, pdateOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromBool(boolIn: win32more.Windows.Win32.Foundation.VARIANT_BOOL, pdateOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromI1(cIn: win32more.Windows.Win32.Foundation.CHAR, pdateOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromUI2(uiIn: UInt16, pdateOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromUI4(ulIn: UInt32, pdateOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromUI8(ui64In: UInt64, pdateOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromDec(pdecIn: POINTER(win32more.Windows.Win32.Foundation.DECIMAL), pdateOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFromUI1(bIn: Byte, pcyOut: POINTER(win32more.Windows.Win32.System.Com.CY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFromI2(sIn: Int16, pcyOut: POINTER(win32more.Windows.Win32.System.Com.CY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFromI4(lIn: Int32, pcyOut: POINTER(win32more.Windows.Win32.System.Com.CY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFromI8(i64In: Int64, pcyOut: POINTER(win32more.Windows.Win32.System.Com.CY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFromR4(fltIn: Single, pcyOut: POINTER(win32more.Windows.Win32.System.Com.CY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFromR8(dblIn: Double, pcyOut: POINTER(win32more.Windows.Win32.System.Com.CY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFromDate(dateIn: Double, pcyOut: POINTER(win32more.Windows.Win32.System.Com.CY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFromStr(strIn: win32more.Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, pcyOut: POINTER(win32more.Windows.Win32.System.Com.CY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFromDisp(pdispIn: win32more.Windows.Win32.System.Com.IDispatch, lcid: UInt32, pcyOut: POINTER(win32more.Windows.Win32.System.Com.CY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFromBool(boolIn: win32more.Windows.Win32.Foundation.VARIANT_BOOL, pcyOut: POINTER(win32more.Windows.Win32.System.Com.CY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFromI1(cIn: win32more.Windows.Win32.Foundation.CHAR, pcyOut: POINTER(win32more.Windows.Win32.System.Com.CY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFromUI2(uiIn: UInt16, pcyOut: POINTER(win32more.Windows.Win32.System.Com.CY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFromUI4(ulIn: UInt32, pcyOut: POINTER(win32more.Windows.Win32.System.Com.CY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFromUI8(ui64In: UInt64, pcyOut: POINTER(win32more.Windows.Win32.System.Com.CY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFromDec(pdecIn: POINTER(win32more.Windows.Win32.Foundation.DECIMAL), pcyOut: POINTER(win32more.Windows.Win32.System.Com.CY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrFromUI1(bVal: Byte, lcid: UInt32, dwFlags: UInt32, pbstrOut: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrFromI2(iVal: Int16, lcid: UInt32, dwFlags: UInt32, pbstrOut: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrFromI4(lIn: Int32, lcid: UInt32, dwFlags: UInt32, pbstrOut: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrFromI8(i64In: Int64, lcid: UInt32, dwFlags: UInt32, pbstrOut: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrFromR4(fltIn: Single, lcid: UInt32, dwFlags: UInt32, pbstrOut: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrFromR8(dblIn: Double, lcid: UInt32, dwFlags: UInt32, pbstrOut: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrFromCy(cyIn: win32more.Windows.Win32.System.Com.CY, lcid: UInt32, dwFlags: UInt32, pbstrOut: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrFromDate(dateIn: Double, lcid: UInt32, dwFlags: UInt32, pbstrOut: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrFromDisp(pdispIn: win32more.Windows.Win32.System.Com.IDispatch, lcid: UInt32, dwFlags: UInt32, pbstrOut: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrFromBool(boolIn: win32more.Windows.Win32.Foundation.VARIANT_BOOL, lcid: UInt32, dwFlags: UInt32, pbstrOut: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrFromI1(cIn: win32more.Windows.Win32.Foundation.CHAR, lcid: UInt32, dwFlags: UInt32, pbstrOut: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrFromUI2(uiIn: UInt16, lcid: UInt32, dwFlags: UInt32, pbstrOut: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrFromUI4(ulIn: UInt32, lcid: UInt32, dwFlags: UInt32, pbstrOut: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrFromUI8(ui64In: UInt64, lcid: UInt32, dwFlags: UInt32, pbstrOut: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrFromDec(pdecIn: POINTER(win32more.Windows.Win32.Foundation.DECIMAL), lcid: UInt32, dwFlags: UInt32, pbstrOut: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBoolFromUI1(bIn: Byte, pboolOut: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBoolFromI2(sIn: Int16, pboolOut: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBoolFromI4(lIn: Int32, pboolOut: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBoolFromI8(i64In: Int64, pboolOut: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBoolFromR4(fltIn: Single, pboolOut: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBoolFromR8(dblIn: Double, pboolOut: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBoolFromDate(dateIn: Double, pboolOut: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBoolFromCy(cyIn: win32more.Windows.Win32.System.Com.CY, pboolOut: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBoolFromStr(strIn: win32more.Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, pboolOut: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBoolFromDisp(pdispIn: win32more.Windows.Win32.System.Com.IDispatch, lcid: UInt32, pboolOut: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBoolFromI1(cIn: win32more.Windows.Win32.Foundation.CHAR, pboolOut: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBoolFromUI2(uiIn: UInt16, pboolOut: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBoolFromUI4(ulIn: UInt32, pboolOut: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBoolFromUI8(i64In: UInt64, pboolOut: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBoolFromDec(pdecIn: POINTER(win32more.Windows.Win32.Foundation.DECIMAL), pboolOut: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI1FromUI1(bIn: Byte, pcOut: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI1FromI2(uiIn: Int16, pcOut: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI1FromI4(lIn: Int32, pcOut: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI1FromI8(i64In: Int64, pcOut: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI1FromR4(fltIn: Single, pcOut: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI1FromR8(dblIn: Double, pcOut: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI1FromDate(dateIn: Double, pcOut: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI1FromCy(cyIn: win32more.Windows.Win32.System.Com.CY, pcOut: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI1FromStr(strIn: win32more.Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, pcOut: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI1FromDisp(pdispIn: win32more.Windows.Win32.System.Com.IDispatch, lcid: UInt32, pcOut: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI1FromBool(boolIn: win32more.Windows.Win32.Foundation.VARIANT_BOOL, pcOut: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI1FromUI2(uiIn: UInt16, pcOut: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI1FromUI4(ulIn: UInt32, pcOut: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI1FromUI8(i64In: UInt64, pcOut: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarI1FromDec(pdecIn: POINTER(win32more.Windows.Win32.Foundation.DECIMAL), pcOut: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI2FromUI1(bIn: Byte, puiOut: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI2FromI2(uiIn: Int16, puiOut: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI2FromI4(lIn: Int32, puiOut: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI2FromI8(i64In: Int64, puiOut: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI2FromR4(fltIn: Single, puiOut: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI2FromR8(dblIn: Double, puiOut: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI2FromDate(dateIn: Double, puiOut: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI2FromCy(cyIn: win32more.Windows.Win32.System.Com.CY, puiOut: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI2FromStr(strIn: win32more.Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, puiOut: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI2FromDisp(pdispIn: win32more.Windows.Win32.System.Com.IDispatch, lcid: UInt32, puiOut: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI2FromBool(boolIn: win32more.Windows.Win32.Foundation.VARIANT_BOOL, puiOut: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI2FromI1(cIn: win32more.Windows.Win32.Foundation.CHAR, puiOut: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI2FromUI4(ulIn: UInt32, puiOut: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI2FromUI8(i64In: UInt64, puiOut: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI2FromDec(pdecIn: POINTER(win32more.Windows.Win32.Foundation.DECIMAL), puiOut: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI4FromUI1(bIn: Byte, pulOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI4FromI2(uiIn: Int16, pulOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI4FromI4(lIn: Int32, pulOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI4FromI8(i64In: Int64, plOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI4FromR4(fltIn: Single, pulOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI4FromR8(dblIn: Double, pulOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI4FromDate(dateIn: Double, pulOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI4FromCy(cyIn: win32more.Windows.Win32.System.Com.CY, pulOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI4FromStr(strIn: win32more.Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, pulOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI4FromDisp(pdispIn: win32more.Windows.Win32.System.Com.IDispatch, lcid: UInt32, pulOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI4FromBool(boolIn: win32more.Windows.Win32.Foundation.VARIANT_BOOL, pulOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI4FromI1(cIn: win32more.Windows.Win32.Foundation.CHAR, pulOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI4FromUI2(uiIn: UInt16, pulOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI4FromUI8(ui64In: UInt64, plOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI4FromDec(pdecIn: POINTER(win32more.Windows.Win32.Foundation.DECIMAL), pulOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI8FromUI1(bIn: Byte, pi64Out: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI8FromI2(sIn: Int16, pi64Out: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI8FromI8(ui64In: Int64, pi64Out: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI8FromR4(fltIn: Single, pi64Out: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI8FromR8(dblIn: Double, pi64Out: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI8FromCy(cyIn: win32more.Windows.Win32.System.Com.CY, pi64Out: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI8FromDate(dateIn: Double, pi64Out: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI8FromStr(strIn: win32more.Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, pi64Out: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI8FromDisp(pdispIn: win32more.Windows.Win32.System.Com.IDispatch, lcid: UInt32, pi64Out: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI8FromBool(boolIn: win32more.Windows.Win32.Foundation.VARIANT_BOOL, pi64Out: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI8FromI1(cIn: win32more.Windows.Win32.Foundation.CHAR, pi64Out: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI8FromUI2(uiIn: UInt16, pi64Out: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI8FromUI4(ulIn: UInt32, pi64Out: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUI8FromDec(pdecIn: POINTER(win32more.Windows.Win32.Foundation.DECIMAL), pi64Out: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFromUI1(bIn: Byte, pdecOut: POINTER(win32more.Windows.Win32.Foundation.DECIMAL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFromI2(uiIn: Int16, pdecOut: POINTER(win32more.Windows.Win32.Foundation.DECIMAL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFromI4(lIn: Int32, pdecOut: POINTER(win32more.Windows.Win32.Foundation.DECIMAL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFromI8(i64In: Int64, pdecOut: POINTER(win32more.Windows.Win32.Foundation.DECIMAL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFromR4(fltIn: Single, pdecOut: POINTER(win32more.Windows.Win32.Foundation.DECIMAL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFromR8(dblIn: Double, pdecOut: POINTER(win32more.Windows.Win32.Foundation.DECIMAL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFromDate(dateIn: Double, pdecOut: POINTER(win32more.Windows.Win32.Foundation.DECIMAL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFromCy(cyIn: win32more.Windows.Win32.System.Com.CY, pdecOut: POINTER(win32more.Windows.Win32.Foundation.DECIMAL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFromStr(strIn: win32more.Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, pdecOut: POINTER(win32more.Windows.Win32.Foundation.DECIMAL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFromDisp(pdispIn: win32more.Windows.Win32.System.Com.IDispatch, lcid: UInt32, pdecOut: POINTER(win32more.Windows.Win32.Foundation.DECIMAL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFromBool(boolIn: win32more.Windows.Win32.Foundation.VARIANT_BOOL, pdecOut: POINTER(win32more.Windows.Win32.Foundation.DECIMAL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFromI1(cIn: win32more.Windows.Win32.Foundation.CHAR, pdecOut: POINTER(win32more.Windows.Win32.Foundation.DECIMAL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFromUI2(uiIn: UInt16, pdecOut: POINTER(win32more.Windows.Win32.Foundation.DECIMAL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFromUI4(ulIn: UInt32, pdecOut: POINTER(win32more.Windows.Win32.Foundation.DECIMAL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFromUI8(ui64In: UInt64, pdecOut: POINTER(win32more.Windows.Win32.Foundation.DECIMAL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarParseNumFromStr(strIn: win32more.Windows.Win32.Foundation.PWSTR, lcid: UInt32, dwFlags: UInt32, pnumprs: POINTER(win32more.Windows.Win32.System.Ole.NUMPARSE), rgbDig: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarNumFromParseNum(pnumprs: POINTER(win32more.Windows.Win32.System.Ole.NUMPARSE), rgbDig: POINTER(Byte), dwVtBits: UInt32, pvar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarAdd(pvarLeft: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarRight: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarAnd(pvarLeft: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarRight: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCat(pvarLeft: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarRight: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDiv(pvarLeft: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarRight: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarEqv(pvarLeft: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarRight: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarIdiv(pvarLeft: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarRight: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarImp(pvarLeft: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarRight: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarMod(pvarLeft: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarRight: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarMul(pvarLeft: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarRight: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarOr(pvarLeft: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarRight: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarPow(pvarLeft: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarRight: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarSub(pvarLeft: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarRight: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarXor(pvarLeft: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarRight: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarAbs(pvarIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarFix(pvarIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarInt(pvarIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarNeg(pvarIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarNot(pvarIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarRound(pvarIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), cDecimals: Int32, pvarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCmp(pvarLeft: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarRight: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), lcid: UInt32, dwFlags: UInt32) -> win32more.Windows.Win32.System.Ole.VARCMP: ...
@winfunctype('OLEAUT32.dll')
def VarDecAdd(pdecLeft: POINTER(win32more.Windows.Win32.Foundation.DECIMAL), pdecRight: POINTER(win32more.Windows.Win32.Foundation.DECIMAL), pdecResult: POINTER(win32more.Windows.Win32.Foundation.DECIMAL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecDiv(pdecLeft: POINTER(win32more.Windows.Win32.Foundation.DECIMAL), pdecRight: POINTER(win32more.Windows.Win32.Foundation.DECIMAL), pdecResult: POINTER(win32more.Windows.Win32.Foundation.DECIMAL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecMul(pdecLeft: POINTER(win32more.Windows.Win32.Foundation.DECIMAL), pdecRight: POINTER(win32more.Windows.Win32.Foundation.DECIMAL), pdecResult: POINTER(win32more.Windows.Win32.Foundation.DECIMAL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecSub(pdecLeft: POINTER(win32more.Windows.Win32.Foundation.DECIMAL), pdecRight: POINTER(win32more.Windows.Win32.Foundation.DECIMAL), pdecResult: POINTER(win32more.Windows.Win32.Foundation.DECIMAL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecAbs(pdecIn: POINTER(win32more.Windows.Win32.Foundation.DECIMAL), pdecResult: POINTER(win32more.Windows.Win32.Foundation.DECIMAL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecFix(pdecIn: POINTER(win32more.Windows.Win32.Foundation.DECIMAL), pdecResult: POINTER(win32more.Windows.Win32.Foundation.DECIMAL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecInt(pdecIn: POINTER(win32more.Windows.Win32.Foundation.DECIMAL), pdecResult: POINTER(win32more.Windows.Win32.Foundation.DECIMAL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecNeg(pdecIn: POINTER(win32more.Windows.Win32.Foundation.DECIMAL), pdecResult: POINTER(win32more.Windows.Win32.Foundation.DECIMAL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecRound(pdecIn: POINTER(win32more.Windows.Win32.Foundation.DECIMAL), cDecimals: Int32, pdecResult: POINTER(win32more.Windows.Win32.Foundation.DECIMAL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDecCmp(pdecLeft: POINTER(win32more.Windows.Win32.Foundation.DECIMAL), pdecRight: POINTER(win32more.Windows.Win32.Foundation.DECIMAL)) -> win32more.Windows.Win32.System.Ole.VARCMP: ...
@winfunctype('OLEAUT32.dll')
def VarDecCmpR8(pdecLeft: POINTER(win32more.Windows.Win32.Foundation.DECIMAL), dblRight: Double) -> win32more.Windows.Win32.System.Ole.VARCMP: ...
@winfunctype('OLEAUT32.dll')
def VarCyAdd(cyLeft: win32more.Windows.Win32.System.Com.CY, cyRight: win32more.Windows.Win32.System.Com.CY, pcyResult: POINTER(win32more.Windows.Win32.System.Com.CY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyMul(cyLeft: win32more.Windows.Win32.System.Com.CY, cyRight: win32more.Windows.Win32.System.Com.CY, pcyResult: POINTER(win32more.Windows.Win32.System.Com.CY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyMulI4(cyLeft: win32more.Windows.Win32.System.Com.CY, lRight: Int32, pcyResult: POINTER(win32more.Windows.Win32.System.Com.CY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyMulI8(cyLeft: win32more.Windows.Win32.System.Com.CY, lRight: Int64, pcyResult: POINTER(win32more.Windows.Win32.System.Com.CY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCySub(cyLeft: win32more.Windows.Win32.System.Com.CY, cyRight: win32more.Windows.Win32.System.Com.CY, pcyResult: POINTER(win32more.Windows.Win32.System.Com.CY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyAbs(cyIn: win32more.Windows.Win32.System.Com.CY, pcyResult: POINTER(win32more.Windows.Win32.System.Com.CY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyFix(cyIn: win32more.Windows.Win32.System.Com.CY, pcyResult: POINTER(win32more.Windows.Win32.System.Com.CY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyInt(cyIn: win32more.Windows.Win32.System.Com.CY, pcyResult: POINTER(win32more.Windows.Win32.System.Com.CY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyNeg(cyIn: win32more.Windows.Win32.System.Com.CY, pcyResult: POINTER(win32more.Windows.Win32.System.Com.CY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyRound(cyIn: win32more.Windows.Win32.System.Com.CY, cDecimals: Int32, pcyResult: POINTER(win32more.Windows.Win32.System.Com.CY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarCyCmp(cyLeft: win32more.Windows.Win32.System.Com.CY, cyRight: win32more.Windows.Win32.System.Com.CY) -> win32more.Windows.Win32.System.Ole.VARCMP: ...
@winfunctype('OLEAUT32.dll')
def VarCyCmpR8(cyLeft: win32more.Windows.Win32.System.Com.CY, dblRight: Double) -> win32more.Windows.Win32.System.Ole.VARCMP: ...
@winfunctype('OLEAUT32.dll')
def VarBstrCat(bstrLeft: win32more.Windows.Win32.Foundation.BSTR, bstrRight: win32more.Windows.Win32.Foundation.BSTR, pbstrResult: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarBstrCmp(bstrLeft: win32more.Windows.Win32.Foundation.BSTR, bstrRight: win32more.Windows.Win32.Foundation.BSTR, lcid: UInt32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR8Pow(dblLeft: Double, dblRight: Double, pdblResult: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarR4CmpR8(fltLeft: Single, dblRight: Double) -> win32more.Windows.Win32.System.Ole.VARCMP: ...
@winfunctype('OLEAUT32.dll')
def VarR8Round(dblIn: Double, cDecimals: Int32, pdblResult: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromUdate(pudateIn: POINTER(win32more.Windows.Win32.System.Ole.UDATE), dwFlags: UInt32, pdateOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarDateFromUdateEx(pudateIn: POINTER(win32more.Windows.Win32.System.Ole.UDATE), lcid: UInt32, dwFlags: UInt32, pdateOut: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarUdateFromDate(dateIn: Double, dwFlags: UInt32, pudateOut: POINTER(win32more.Windows.Win32.System.Ole.UDATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def GetAltMonthNames(lcid: UInt32, prgp: POINTER(POINTER(win32more.Windows.Win32.Foundation.PWSTR))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarFormat(pvarIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pstrFormat: win32more.Windows.Win32.Foundation.PWSTR, iFirstDay: win32more.Windows.Win32.System.Ole.VARFORMAT_FIRST_DAY, iFirstWeek: win32more.Windows.Win32.System.Ole.VARFORMAT_FIRST_WEEK, dwFlags: UInt32, pbstrOut: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarFormatDateTime(pvarIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), iNamedFormat: win32more.Windows.Win32.System.Ole.VARFORMAT_NAMED_FORMAT, dwFlags: UInt32, pbstrOut: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarFormatNumber(pvarIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), iNumDig: Int32, iIncLead: win32more.Windows.Win32.System.Ole.VARFORMAT_LEADING_DIGIT, iUseParens: win32more.Windows.Win32.System.Ole.VARFORMAT_PARENTHESES, iGroup: win32more.Windows.Win32.System.Ole.VARFORMAT_GROUP, dwFlags: UInt32, pbstrOut: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarFormatPercent(pvarIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), iNumDig: Int32, iIncLead: win32more.Windows.Win32.System.Ole.VARFORMAT_LEADING_DIGIT, iUseParens: win32more.Windows.Win32.System.Ole.VARFORMAT_PARENTHESES, iGroup: win32more.Windows.Win32.System.Ole.VARFORMAT_GROUP, dwFlags: UInt32, pbstrOut: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarFormatCurrency(pvarIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), iNumDig: Int32, iIncLead: Int32, iUseParens: Int32, iGroup: Int32, dwFlags: UInt32, pbstrOut: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarWeekdayName(iWeekday: Int32, fAbbrev: Int32, iFirstDay: Int32, dwFlags: UInt32, pbstrOut: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarMonthName(iMonth: Int32, fAbbrev: Int32, dwFlags: UInt32, pbstrOut: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarFormatFromTokens(pvarIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pstrFormat: win32more.Windows.Win32.Foundation.PWSTR, pbTokCur: POINTER(Byte), dwFlags: UInt32, pbstrOut: POINTER(win32more.Windows.Win32.Foundation.BSTR), lcid: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def VarTokenizeFormatString(pstrFormat: win32more.Windows.Win32.Foundation.PWSTR, rgbTok: POINTER(Byte), cbTok: Int32, iFirstDay: win32more.Windows.Win32.System.Ole.VARFORMAT_FIRST_DAY, iFirstWeek: win32more.Windows.Win32.System.Ole.VARFORMAT_FIRST_WEEK, lcid: UInt32, pcbActual: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def LHashValOfNameSysA(syskind: win32more.Windows.Win32.System.Com.SYSKIND, lcid: UInt32, szName: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('OLEAUT32.dll')
def LHashValOfNameSys(syskind: win32more.Windows.Win32.System.Com.SYSKIND, lcid: UInt32, szName: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('OLEAUT32.dll')
def LoadTypeLib(szFile: win32more.Windows.Win32.Foundation.PWSTR, pptlib: POINTER(win32more.Windows.Win32.System.Com.ITypeLib)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def LoadTypeLibEx(szFile: win32more.Windows.Win32.Foundation.PWSTR, regkind: win32more.Windows.Win32.System.Ole.REGKIND, pptlib: POINTER(win32more.Windows.Win32.System.Com.ITypeLib)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def LoadRegTypeLib(rguid: POINTER(Guid), wVerMajor: UInt16, wVerMinor: UInt16, lcid: UInt32, pptlib: POINTER(win32more.Windows.Win32.System.Com.ITypeLib)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def QueryPathOfRegTypeLib(guid: POINTER(Guid), wMaj: UInt16, wMin: UInt16, lcid: UInt32, lpbstrPathName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def RegisterTypeLib(ptlib: win32more.Windows.Win32.System.Com.ITypeLib, szFullPath: win32more.Windows.Win32.Foundation.PWSTR, szHelpDir: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def UnRegisterTypeLib(libID: POINTER(Guid), wVerMajor: UInt16, wVerMinor: UInt16, lcid: UInt32, syskind: win32more.Windows.Win32.System.Com.SYSKIND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def RegisterTypeLibForUser(ptlib: win32more.Windows.Win32.System.Com.ITypeLib, szFullPath: win32more.Windows.Win32.Foundation.PWSTR, szHelpDir: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def UnRegisterTypeLibForUser(libID: POINTER(Guid), wMajorVerNum: UInt16, wMinorVerNum: UInt16, lcid: UInt32, syskind: win32more.Windows.Win32.System.Com.SYSKIND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def CreateTypeLib(syskind: win32more.Windows.Win32.System.Com.SYSKIND, szFile: win32more.Windows.Win32.Foundation.PWSTR, ppctlib: POINTER(win32more.Windows.Win32.System.Ole.ICreateTypeLib)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def CreateTypeLib2(syskind: win32more.Windows.Win32.System.Com.SYSKIND, szFile: win32more.Windows.Win32.Foundation.PWSTR, ppctlib: POINTER(win32more.Windows.Win32.System.Ole.ICreateTypeLib2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def DispGetParam(pdispparams: POINTER(win32more.Windows.Win32.System.Com.DISPPARAMS), position: UInt32, vtTarg: win32more.Windows.Win32.System.Variant.VARENUM, pvarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), puArgErr: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def DispGetIDsOfNames(ptinfo: win32more.Windows.Win32.System.Com.ITypeInfo, rgszNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR), cNames: UInt32, rgdispid: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def DispInvoke(_this: VoidPtr, ptinfo: win32more.Windows.Win32.System.Com.ITypeInfo, dispidMember: Int32, wFlags: UInt16, pparams: POINTER(win32more.Windows.Win32.System.Com.DISPPARAMS), pvarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pexcepinfo: POINTER(win32more.Windows.Win32.System.Com.EXCEPINFO), puArgErr: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def CreateDispTypeInfo(pidata: POINTER(win32more.Windows.Win32.System.Ole.INTERFACEDATA), lcid: UInt32, pptinfo: POINTER(win32more.Windows.Win32.System.Com.ITypeInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def CreateStdDispatch(punkOuter: win32more.Windows.Win32.System.Com.IUnknown, pvThis: VoidPtr, ptinfo: win32more.Windows.Win32.System.Com.ITypeInfo, ppunkStdDisp: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def DispCallFunc(pvInstance: VoidPtr, oVft: UIntPtr, cc: win32more.Windows.Win32.System.Com.CALLCONV, vtReturn: win32more.Windows.Win32.System.Variant.VARENUM, cActuals: UInt32, prgvt: POINTER(UInt16), prgpvarg: POINTER(POINTER(win32more.Windows.Win32.System.Variant.VARIANT)), pvargResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def RegisterActiveObject(punk: win32more.Windows.Win32.System.Com.IUnknown, rclsid: POINTER(Guid), dwFlags: win32more.Windows.Win32.System.Ole.ACTIVEOBJECT_FLAGS, pdwRegister: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def RevokeActiveObject(dwRegister: UInt32, pvReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def GetActiveObject(rclsid: POINTER(Guid), pvReserved: VoidPtr, ppunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def CreateErrorInfo(pperrinfo: POINTER(win32more.Windows.Win32.System.Ole.ICreateErrorInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def GetRecordInfoFromTypeInfo(pTypeInfo: win32more.Windows.Win32.System.Com.ITypeInfo, ppRecInfo: POINTER(win32more.Windows.Win32.System.Ole.IRecordInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def GetRecordInfoFromGuids(rGuidTypeLib: POINTER(Guid), uVerMajor: UInt32, uVerMinor: UInt32, lcid: UInt32, rGuidTypeInfo: POINTER(Guid), ppRecInfo: POINTER(win32more.Windows.Win32.System.Ole.IRecordInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def OaBuildVersion() -> UInt32: ...
@winfunctype('OLEAUT32.dll')
def ClearCustData(pCustData: POINTER(win32more.Windows.Win32.System.Com.CUSTDATA)) -> Void: ...
@winfunctype('OLEAUT32.dll')
def OaEnablePerUserTLibRegistration() -> Void: ...
@winfunctype('ole32.dll')
def OleBuildVersion() -> UInt32: ...
@winfunctype('OLE32.dll')
def OleInitialize(pvReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleUninitialize() -> Void: ...
@winfunctype('OLE32.dll')
def OleQueryLinkFromData(pSrcDataObject: win32more.Windows.Win32.System.Com.IDataObject) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleQueryCreateFromData(pSrcDataObject: win32more.Windows.Win32.System.Com.IDataObject) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleCreate(rclsid: POINTER(Guid), riid: POINTER(Guid), renderopt: UInt32, pFormatEtc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC), pClientSite: win32more.Windows.Win32.System.Ole.IOleClientSite, pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleCreateEx(rclsid: POINTER(Guid), riid: POINTER(Guid), dwFlags: win32more.Windows.Win32.System.Ole.OLECREATE, renderopt: UInt32, cFormats: UInt32, rgAdvf: POINTER(UInt32), rgFormatEtc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC), lpAdviseSink: win32more.Windows.Win32.System.Com.IAdviseSink, rgdwConnection: POINTER(UInt32), pClientSite: win32more.Windows.Win32.System.Ole.IOleClientSite, pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleCreateFromData(pSrcDataObj: win32more.Windows.Win32.System.Com.IDataObject, riid: POINTER(Guid), renderopt: UInt32, pFormatEtc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC), pClientSite: win32more.Windows.Win32.System.Ole.IOleClientSite, pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleCreateFromDataEx(pSrcDataObj: win32more.Windows.Win32.System.Com.IDataObject, riid: POINTER(Guid), dwFlags: win32more.Windows.Win32.System.Ole.OLECREATE, renderopt: UInt32, cFormats: UInt32, rgAdvf: POINTER(UInt32), rgFormatEtc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC), lpAdviseSink: win32more.Windows.Win32.System.Com.IAdviseSink, rgdwConnection: POINTER(UInt32), pClientSite: win32more.Windows.Win32.System.Ole.IOleClientSite, pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleCreateLinkFromData(pSrcDataObj: win32more.Windows.Win32.System.Com.IDataObject, riid: POINTER(Guid), renderopt: UInt32, pFormatEtc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC), pClientSite: win32more.Windows.Win32.System.Ole.IOleClientSite, pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleCreateLinkFromDataEx(pSrcDataObj: win32more.Windows.Win32.System.Com.IDataObject, riid: POINTER(Guid), dwFlags: win32more.Windows.Win32.System.Ole.OLECREATE, renderopt: UInt32, cFormats: UInt32, rgAdvf: POINTER(UInt32), rgFormatEtc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC), lpAdviseSink: win32more.Windows.Win32.System.Com.IAdviseSink, rgdwConnection: POINTER(UInt32), pClientSite: win32more.Windows.Win32.System.Ole.IOleClientSite, pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleCreateStaticFromData(pSrcDataObj: win32more.Windows.Win32.System.Com.IDataObject, iid: POINTER(Guid), renderopt: UInt32, pFormatEtc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC), pClientSite: win32more.Windows.Win32.System.Ole.IOleClientSite, pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleCreateLink(pmkLinkSrc: win32more.Windows.Win32.System.Com.IMoniker, riid: POINTER(Guid), renderopt: UInt32, lpFormatEtc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC), pClientSite: win32more.Windows.Win32.System.Ole.IOleClientSite, pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleCreateLinkEx(pmkLinkSrc: win32more.Windows.Win32.System.Com.IMoniker, riid: POINTER(Guid), dwFlags: win32more.Windows.Win32.System.Ole.OLECREATE, renderopt: UInt32, cFormats: UInt32, rgAdvf: POINTER(UInt32), rgFormatEtc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC), lpAdviseSink: win32more.Windows.Win32.System.Com.IAdviseSink, rgdwConnection: POINTER(UInt32), pClientSite: win32more.Windows.Win32.System.Ole.IOleClientSite, pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleCreateLinkToFile(lpszFileName: win32more.Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), renderopt: UInt32, lpFormatEtc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC), pClientSite: win32more.Windows.Win32.System.Ole.IOleClientSite, pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleCreateLinkToFileEx(lpszFileName: win32more.Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), dwFlags: win32more.Windows.Win32.System.Ole.OLECREATE, renderopt: UInt32, cFormats: UInt32, rgAdvf: POINTER(UInt32), rgFormatEtc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC), lpAdviseSink: win32more.Windows.Win32.System.Com.IAdviseSink, rgdwConnection: POINTER(UInt32), pClientSite: win32more.Windows.Win32.System.Ole.IOleClientSite, pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleCreateFromFile(rclsid: POINTER(Guid), lpszFileName: win32more.Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), renderopt: UInt32, lpFormatEtc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC), pClientSite: win32more.Windows.Win32.System.Ole.IOleClientSite, pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleCreateFromFileEx(rclsid: POINTER(Guid), lpszFileName: win32more.Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), dwFlags: win32more.Windows.Win32.System.Ole.OLECREATE, renderopt: UInt32, cFormats: UInt32, rgAdvf: POINTER(UInt32), rgFormatEtc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC), lpAdviseSink: win32more.Windows.Win32.System.Com.IAdviseSink, rgdwConnection: POINTER(UInt32), pClientSite: win32more.Windows.Win32.System.Ole.IOleClientSite, pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleLoad(pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, riid: POINTER(Guid), pClientSite: win32more.Windows.Win32.System.Ole.IOleClientSite, ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleSave(pPS: win32more.Windows.Win32.System.Com.StructuredStorage.IPersistStorage, pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, fSameAsLoad: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleLoadFromStream(pStm: win32more.Windows.Win32.System.Com.IStream, iidInterface: POINTER(Guid), ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleSaveToStream(pPStm: win32more.Windows.Win32.System.Com.IPersistStream, pStm: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleSetContainedObject(pUnknown: win32more.Windows.Win32.System.Com.IUnknown, fContained: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleNoteObjectVisible(pUnknown: win32more.Windows.Win32.System.Com.IUnknown, fVisible: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def RegisterDragDrop(hwnd: win32more.Windows.Win32.Foundation.HWND, pDropTarget: win32more.Windows.Win32.System.Ole.IDropTarget) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def RevokeDragDrop(hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def DoDragDrop(pDataObj: win32more.Windows.Win32.System.Com.IDataObject, pDropSource: win32more.Windows.Win32.System.Ole.IDropSource, dwOKEffects: win32more.Windows.Win32.System.Ole.DROPEFFECT, pdwEffect: POINTER(win32more.Windows.Win32.System.Ole.DROPEFFECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleSetClipboard(pDataObj: win32more.Windows.Win32.System.Com.IDataObject) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleGetClipboard(ppDataObj: POINTER(win32more.Windows.Win32.System.Com.IDataObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleGetClipboardWithEnterpriseInfo(dataObject: POINTER(win32more.Windows.Win32.System.Com.IDataObject), dataEnterpriseId: POINTER(win32more.Windows.Win32.Foundation.PWSTR), sourceDescription: POINTER(win32more.Windows.Win32.Foundation.PWSTR), targetDescription: POINTER(win32more.Windows.Win32.Foundation.PWSTR), dataDescription: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleFlushClipboard() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleIsCurrentClipboard(pDataObj: win32more.Windows.Win32.System.Com.IDataObject) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleCreateMenuDescriptor(hmenuCombined: win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU, lpMenuWidths: POINTER(win32more.Windows.Win32.System.Ole.OLEMENUGROUPWIDTHS)) -> IntPtr: ...
@winfunctype('OLE32.dll')
def OleSetMenuDescriptor(holemenu: IntPtr, hwndFrame: win32more.Windows.Win32.Foundation.HWND, hwndActiveObject: win32more.Windows.Win32.Foundation.HWND, lpFrame: win32more.Windows.Win32.System.Ole.IOleInPlaceFrame, lpActiveObj: win32more.Windows.Win32.System.Ole.IOleInPlaceActiveObject) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleDestroyMenuDescriptor(holemenu: IntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleTranslateAccelerator(lpFrame: win32more.Windows.Win32.System.Ole.IOleInPlaceFrame, lpFrameInfo: POINTER(win32more.Windows.Win32.System.Ole.OLEINPLACEFRAMEINFO), lpmsg: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.MSG)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleDuplicateData(hSrc: win32more.Windows.Win32.Foundation.HANDLE, cfFormat: win32more.Windows.Win32.System.Ole.CLIPBOARD_FORMAT, uiFlags: win32more.Windows.Win32.System.Memory.GLOBAL_ALLOC_FLAGS) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('OLE32.dll')
def OleDraw(pUnknown: win32more.Windows.Win32.System.Com.IUnknown, dwAspect: UInt32, hdcDraw: win32more.Windows.Win32.Graphics.Gdi.HDC, lprcBounds: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleRun(pUnknown: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleIsRunning(pObject: win32more.Windows.Win32.System.Ole.IOleObject) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('OLE32.dll')
def OleLockRunning(pUnknown: win32more.Windows.Win32.System.Com.IUnknown, fLock: win32more.Windows.Win32.Foundation.BOOL, fLastUnlockCloses: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def ReleaseStgMedium(param0: POINTER(win32more.Windows.Win32.System.Com.STGMEDIUM)) -> Void: ...
@winfunctype('OLE32.dll')
def CreateOleAdviseHolder(ppOAHolder: POINTER(win32more.Windows.Win32.System.Ole.IOleAdviseHolder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleCreateDefaultHandler(clsid: POINTER(Guid), pUnkOuter: win32more.Windows.Win32.System.Com.IUnknown, riid: POINTER(Guid), lplpObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleCreateEmbeddingHelper(clsid: POINTER(Guid), pUnkOuter: win32more.Windows.Win32.System.Com.IUnknown, flags: win32more.Windows.Win32.System.Ole.EMBDHLP_FLAGS, pCF: win32more.Windows.Win32.System.Com.IClassFactory, riid: POINTER(Guid), lplpObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def IsAccelerator(hAccel: win32more.Windows.Win32.UI.WindowsAndMessaging.HACCEL, cAccelEntries: Int32, lpMsg: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.MSG), lpwCmd: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('ole32.dll')
def OleGetIconOfFile(lpszPath: win32more.Windows.Win32.Foundation.PWSTR, fUseFileAsLabel: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HGLOBAL: ...
@winfunctype('OLE32.dll')
def OleGetIconOfClass(rclsid: POINTER(Guid), lpszLabel: win32more.Windows.Win32.Foundation.PWSTR, fUseTypeAsLabel: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HGLOBAL: ...
@winfunctype('ole32.dll')
def OleMetafilePictFromIconAndLabel(hIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON, lpszLabel: win32more.Windows.Win32.Foundation.PWSTR, lpszSourceFile: win32more.Windows.Win32.Foundation.PWSTR, iIconIndex: UInt32) -> win32more.Windows.Win32.Foundation.HGLOBAL: ...
@winfunctype('OLE32.dll')
def OleRegGetUserType(clsid: POINTER(Guid), dwFormOfType: UInt32, pszUserType: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleRegGetMiscStatus(clsid: POINTER(Guid), dwAspect: UInt32, pdwStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleRegEnumFormatEtc(clsid: POINTER(Guid), dwDirection: UInt32, ppenum: POINTER(win32more.Windows.Win32.System.Com.IEnumFORMATETC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleRegEnumVerbs(clsid: POINTER(Guid), ppenum: POINTER(win32more.Windows.Win32.System.Ole.IEnumOLEVERB)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleConvertOLESTREAMToIStorage2(lpolestream: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.OLESTREAM), pstg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, ptd: POINTER(win32more.Windows.Win32.System.Com.DVTARGETDEVICE), opt: UInt32, pvCallbackContext: VoidPtr, pQueryConvertOLELinkCallback: win32more.Windows.Win32.System.Ole.OLESTREAMQUERYCONVERTOLELINKCALLBACK) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleDoAutoConvert(pStg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, pClsidNew: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def OleGetAutoConvert(clsidOld: POINTER(Guid), pClsidNew: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleSetAutoConvert(clsidOld: POINTER(Guid), clsidNew: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ole32.dll')
def OleConvertOLESTREAMToIStorageEx2(polestm: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.OLESTREAM), pstg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, pcfFormat: POINTER(UInt16), plwWidth: POINTER(Int32), plHeight: POINTER(Int32), pdwSize: POINTER(UInt32), pmedium: POINTER(win32more.Windows.Win32.System.Com.STGMEDIUM), opt: UInt32, pvCallbackContext: VoidPtr, pQueryConvertOLELinkCallback: win32more.Windows.Win32.System.Ole.OLESTREAMQUERYCONVERTOLELINKCALLBACK) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def HRGN_UserSize(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(win32more.Windows.Win32.Graphics.Gdi.HRGN)) -> UInt32: ...
@winfunctype('OLE32.dll')
def HRGN_UserMarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(win32more.Windows.Win32.Graphics.Gdi.HRGN)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HRGN_UserUnmarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(win32more.Windows.Win32.Graphics.Gdi.HRGN)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HRGN_UserFree(param0: POINTER(UInt32), param1: POINTER(win32more.Windows.Win32.Graphics.Gdi.HRGN)) -> Void: ...
@winfunctype('api-ms-win-core-marshal-l1-1-0.dll')
def HRGN_UserSize64(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(win32more.Windows.Win32.Graphics.Gdi.HRGN)) -> UInt32: ...
@winfunctype('api-ms-win-core-marshal-l1-1-0.dll')
def HRGN_UserMarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(win32more.Windows.Win32.Graphics.Gdi.HRGN)) -> POINTER(Byte): ...
@winfunctype('api-ms-win-core-marshal-l1-1-0.dll')
def HRGN_UserUnmarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(win32more.Windows.Win32.Graphics.Gdi.HRGN)) -> POINTER(Byte): ...
@winfunctype('api-ms-win-core-marshal-l1-1-0.dll')
def HRGN_UserFree64(param0: POINTER(UInt32), param1: POINTER(win32more.Windows.Win32.Graphics.Gdi.HRGN)) -> Void: ...
@winfunctype('OLEAUT32.dll')
def OleCreatePropertyFrame(hwndOwner: win32more.Windows.Win32.Foundation.HWND, x: UInt32, y: UInt32, lpszCaption: win32more.Windows.Win32.Foundation.PWSTR, cObjects: UInt32, ppUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown), cPages: UInt32, pPageClsID: POINTER(Guid), lcid: UInt32, dwReserved: UInt32, pvReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def OleCreatePropertyFrameIndirect(lpParams: POINTER(win32more.Windows.Win32.System.Ole.OCPFIPARAMS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def OleTranslateColor(clr: UInt32, hpal: win32more.Windows.Win32.Graphics.Gdi.HPALETTE, lpcolorref: POINTER(win32more.Windows.Win32.Foundation.COLORREF)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def OleCreateFontIndirect(lpFontDesc: POINTER(win32more.Windows.Win32.System.Ole.FONTDESC), riid: POINTER(Guid), lplpvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def OleCreatePictureIndirect(lpPictDesc: POINTER(win32more.Windows.Win32.System.Ole.PICTDESC), riid: POINTER(Guid), fOwn: win32more.Windows.Win32.Foundation.BOOL, lplpvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def OleLoadPicture(lpstream: win32more.Windows.Win32.System.Com.IStream, lSize: Int32, fRunmode: win32more.Windows.Win32.Foundation.BOOL, riid: POINTER(Guid), lplpvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def OleLoadPictureEx(lpstream: win32more.Windows.Win32.System.Com.IStream, lSize: Int32, fRunmode: win32more.Windows.Win32.Foundation.BOOL, riid: POINTER(Guid), xSizeDesired: UInt32, ySizeDesired: UInt32, dwFlags: win32more.Windows.Win32.System.Ole.LOAD_PICTURE_FLAGS, lplpvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def OleLoadPicturePath(szURLorPath: win32more.Windows.Win32.Foundation.PWSTR, punkCaller: win32more.Windows.Win32.System.Com.IUnknown, dwReserved: UInt32, clrReserved: UInt32, riid: POINTER(Guid), ppvRet: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def OleLoadPictureFile(varFileName: win32more.Windows.Win32.System.Variant.VARIANT, lplpdispPicture: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def OleLoadPictureFileEx(varFileName: win32more.Windows.Win32.System.Variant.VARIANT, xSizeDesired: UInt32, ySizeDesired: UInt32, dwFlags: win32more.Windows.Win32.System.Ole.LOAD_PICTURE_FLAGS, lplpdispPicture: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def OleSavePictureFile(lpdispPicture: win32more.Windows.Win32.System.Com.IDispatch, bstrFileName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLEAUT32.dll')
def OleIconToCursor(hinstExe: win32more.Windows.Win32.Foundation.HINSTANCE, hIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON) -> win32more.Windows.Win32.UI.WindowsAndMessaging.HCURSOR: ...
@winfunctype('oledlg.dll')
def OleUIAddVerbMenuW(lpOleObj: win32more.Windows.Win32.System.Ole.IOleObject, lpszShortType: win32more.Windows.Win32.Foundation.PWSTR, hMenu: win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU, uPos: UInt32, uIDVerbMin: UInt32, uIDVerbMax: UInt32, bAddConvert: win32more.Windows.Win32.Foundation.BOOL, idConvert: UInt32, lphMenu: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU)) -> win32more.Windows.Win32.Foundation.BOOL: ...
OleUIAddVerbMenu = UnicodeAlias('OleUIAddVerbMenuW')
@winfunctype('oledlg.dll')
def OleUIAddVerbMenuA(lpOleObj: win32more.Windows.Win32.System.Ole.IOleObject, lpszShortType: win32more.Windows.Win32.Foundation.PSTR, hMenu: win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU, uPos: UInt32, uIDVerbMin: UInt32, uIDVerbMax: UInt32, bAddConvert: win32more.Windows.Win32.Foundation.BOOL, idConvert: UInt32, lphMenu: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('oledlg.dll')
def OleUIInsertObjectW(param0: POINTER(win32more.Windows.Win32.System.Ole.OLEUIINSERTOBJECTW)) -> UInt32: ...
OleUIInsertObject = UnicodeAlias('OleUIInsertObjectW')
@winfunctype('oledlg.dll')
def OleUIInsertObjectA(param0: POINTER(win32more.Windows.Win32.System.Ole.OLEUIINSERTOBJECTA)) -> UInt32: ...
@winfunctype('oledlg.dll')
def OleUIPasteSpecialW(param0: POINTER(win32more.Windows.Win32.System.Ole.OLEUIPASTESPECIALW)) -> UInt32: ...
OleUIPasteSpecial = UnicodeAlias('OleUIPasteSpecialW')
@winfunctype('oledlg.dll')
def OleUIPasteSpecialA(param0: POINTER(win32more.Windows.Win32.System.Ole.OLEUIPASTESPECIALA)) -> UInt32: ...
@winfunctype('oledlg.dll')
def OleUIEditLinksW(param0: POINTER(win32more.Windows.Win32.System.Ole.OLEUIEDITLINKSW)) -> UInt32: ...
OleUIEditLinks = UnicodeAlias('OleUIEditLinksW')
@winfunctype('oledlg.dll')
def OleUIEditLinksA(param0: POINTER(win32more.Windows.Win32.System.Ole.OLEUIEDITLINKSA)) -> UInt32: ...
@winfunctype('oledlg.dll')
def OleUIChangeIconW(param0: POINTER(win32more.Windows.Win32.System.Ole.OLEUICHANGEICONW)) -> UInt32: ...
OleUIChangeIcon = UnicodeAlias('OleUIChangeIconW')
@winfunctype('oledlg.dll')
def OleUIChangeIconA(param0: POINTER(win32more.Windows.Win32.System.Ole.OLEUICHANGEICONA)) -> UInt32: ...
@winfunctype('oledlg.dll')
def OleUIConvertW(param0: POINTER(win32more.Windows.Win32.System.Ole.OLEUICONVERTW)) -> UInt32: ...
OleUIConvert = UnicodeAlias('OleUIConvertW')
@winfunctype('oledlg.dll')
def OleUIConvertA(param0: POINTER(win32more.Windows.Win32.System.Ole.OLEUICONVERTA)) -> UInt32: ...
@winfunctype('oledlg.dll')
def OleUICanConvertOrActivateAs(rClsid: POINTER(Guid), fIsLinkedObject: win32more.Windows.Win32.Foundation.BOOL, wFormat: UInt16) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('oledlg.dll')
def OleUIBusyW(param0: POINTER(win32more.Windows.Win32.System.Ole.OLEUIBUSYW)) -> UInt32: ...
OleUIBusy = UnicodeAlias('OleUIBusyW')
@winfunctype('oledlg.dll')
def OleUIBusyA(param0: POINTER(win32more.Windows.Win32.System.Ole.OLEUIBUSYA)) -> UInt32: ...
@winfunctype('oledlg.dll')
def OleUIChangeSourceW(param0: POINTER(win32more.Windows.Win32.System.Ole.OLEUICHANGESOURCEW)) -> UInt32: ...
OleUIChangeSource = UnicodeAlias('OleUIChangeSourceW')
@winfunctype('oledlg.dll')
def OleUIChangeSourceA(param0: POINTER(win32more.Windows.Win32.System.Ole.OLEUICHANGESOURCEA)) -> UInt32: ...
@winfunctype('oledlg.dll')
def OleUIObjectPropertiesW(param0: POINTER(win32more.Windows.Win32.System.Ole.OLEUIOBJECTPROPSW)) -> UInt32: ...
OleUIObjectProperties = UnicodeAlias('OleUIObjectPropertiesW')
@winfunctype('oledlg.dll')
def OleUIObjectPropertiesA(param0: POINTER(win32more.Windows.Win32.System.Ole.OLEUIOBJECTPROPSA)) -> UInt32: ...
@cfunctype('oledlg.dll', variadic=True)
def OleUIPromptUserW(nTemplate: Int32, hwndParent: win32more.Windows.Win32.Foundation.HWND, *__arglist) -> Int32: ...
OleUIPromptUser = UnicodeAlias('OleUIPromptUserW')
@cfunctype('oledlg.dll', variadic=True)
def OleUIPromptUserA(nTemplate: Int32, hwndParent: win32more.Windows.Win32.Foundation.HWND, *__arglist) -> Int32: ...
@winfunctype('oledlg.dll')
def OleUIUpdateLinksW(lpOleUILinkCntr: win32more.Windows.Win32.System.Ole.IOleUILinkContainerW, hwndParent: win32more.Windows.Win32.Foundation.HWND, lpszTitle: win32more.Windows.Win32.Foundation.PWSTR, cLinks: Int32) -> win32more.Windows.Win32.Foundation.BOOL: ...
OleUIUpdateLinks = UnicodeAlias('OleUIUpdateLinksW')
@winfunctype('oledlg.dll')
def OleUIUpdateLinksA(lpOleUILinkCntr: win32more.Windows.Win32.System.Ole.IOleUILinkContainerA, hwndParent: win32more.Windows.Win32.Foundation.HWND, lpszTitle: win32more.Windows.Win32.Foundation.PSTR, cLinks: Int32) -> win32more.Windows.Win32.Foundation.BOOL: ...
BINDSPEED = Int32
BINDSPEED_INDEFINITE: win32more.Windows.Win32.System.Ole.BINDSPEED = 1
BINDSPEED_MODERATE: win32more.Windows.Win32.System.Ole.BINDSPEED = 2
BINDSPEED_IMMEDIATE: win32more.Windows.Win32.System.Ole.BINDSPEED = 3
BUSY_DIALOG_FLAGS = UInt32
BZ_DISABLECANCELBUTTON: win32more.Windows.Win32.System.Ole.BUSY_DIALOG_FLAGS = 1
BZ_DISABLESWITCHTOBUTTON: win32more.Windows.Win32.System.Ole.BUSY_DIALOG_FLAGS = 2
BZ_DISABLERETRYBUTTON: win32more.Windows.Win32.System.Ole.BUSY_DIALOG_FLAGS = 4
BZ_NOTRESPONDINGDIALOG: win32more.Windows.Win32.System.Ole.BUSY_DIALOG_FLAGS = 8
class CADWORD(Structure):
    cElems: UInt32
    pElems: POINTER(UInt32)
class CALPOLESTR(Structure):
    cElems: UInt32
    pElems: POINTER(win32more.Windows.Win32.Foundation.PWSTR)
class CAUUID(Structure):
    cElems: UInt32
    pElems: POINTER(Guid)
CHANGEKIND = Int32
CHANGEKIND_ADDMEMBER: win32more.Windows.Win32.System.Ole.CHANGEKIND = 0
CHANGEKIND_DELETEMEMBER: win32more.Windows.Win32.System.Ole.CHANGEKIND = 1
CHANGEKIND_SETNAMES: win32more.Windows.Win32.System.Ole.CHANGEKIND = 2
CHANGEKIND_SETDOCUMENTATION: win32more.Windows.Win32.System.Ole.CHANGEKIND = 3
CHANGEKIND_GENERAL: win32more.Windows.Win32.System.Ole.CHANGEKIND = 4
CHANGEKIND_INVALIDATE: win32more.Windows.Win32.System.Ole.CHANGEKIND = 5
CHANGEKIND_CHANGEFAILED: win32more.Windows.Win32.System.Ole.CHANGEKIND = 6
CHANGEKIND_MAX: win32more.Windows.Win32.System.Ole.CHANGEKIND = 7
CHANGE_ICON_FLAGS = UInt32
CIF_SHOWHELP: win32more.Windows.Win32.System.Ole.CHANGE_ICON_FLAGS = 1
CIF_SELECTCURRENT: win32more.Windows.Win32.System.Ole.CHANGE_ICON_FLAGS = 2
CIF_SELECTDEFAULT: win32more.Windows.Win32.System.Ole.CHANGE_ICON_FLAGS = 4
CIF_SELECTFROMFILE: win32more.Windows.Win32.System.Ole.CHANGE_ICON_FLAGS = 8
CIF_USEICONEXE: win32more.Windows.Win32.System.Ole.CHANGE_ICON_FLAGS = 16
CHANGE_SOURCE_FLAGS = UInt32
CSF_SHOWHELP: win32more.Windows.Win32.System.Ole.CHANGE_SOURCE_FLAGS = 1
CSF_VALIDSOURCE: win32more.Windows.Win32.System.Ole.CHANGE_SOURCE_FLAGS = 2
CSF_ONLYGETSOURCE: win32more.Windows.Win32.System.Ole.CHANGE_SOURCE_FLAGS = 4
CSF_EXPLORER: win32more.Windows.Win32.System.Ole.CHANGE_SOURCE_FLAGS = 8
class CLEANLOCALSTORAGE(Structure):
    pInterface: win32more.Windows.Win32.System.Com.IUnknown
    pStorage: VoidPtr
    flags: UInt32
CLIPBOARD_FORMAT = UInt16
CF_TEXT: win32more.Windows.Win32.System.Ole.CLIPBOARD_FORMAT = 1
CF_BITMAP: win32more.Windows.Win32.System.Ole.CLIPBOARD_FORMAT = 2
CF_METAFILEPICT: win32more.Windows.Win32.System.Ole.CLIPBOARD_FORMAT = 3
CF_SYLK: win32more.Windows.Win32.System.Ole.CLIPBOARD_FORMAT = 4
CF_DIF: win32more.Windows.Win32.System.Ole.CLIPBOARD_FORMAT = 5
CF_TIFF: win32more.Windows.Win32.System.Ole.CLIPBOARD_FORMAT = 6
CF_OEMTEXT: win32more.Windows.Win32.System.Ole.CLIPBOARD_FORMAT = 7
CF_DIB: win32more.Windows.Win32.System.Ole.CLIPBOARD_FORMAT = 8
CF_PALETTE: win32more.Windows.Win32.System.Ole.CLIPBOARD_FORMAT = 9
CF_PENDATA: win32more.Windows.Win32.System.Ole.CLIPBOARD_FORMAT = 10
CF_RIFF: win32more.Windows.Win32.System.Ole.CLIPBOARD_FORMAT = 11
CF_WAVE: win32more.Windows.Win32.System.Ole.CLIPBOARD_FORMAT = 12
CF_UNICODETEXT: win32more.Windows.Win32.System.Ole.CLIPBOARD_FORMAT = 13
CF_ENHMETAFILE: win32more.Windows.Win32.System.Ole.CLIPBOARD_FORMAT = 14
CF_HDROP: win32more.Windows.Win32.System.Ole.CLIPBOARD_FORMAT = 15
CF_LOCALE: win32more.Windows.Win32.System.Ole.CLIPBOARD_FORMAT = 16
CF_DIBV5: win32more.Windows.Win32.System.Ole.CLIPBOARD_FORMAT = 17
CF_MAX: win32more.Windows.Win32.System.Ole.CLIPBOARD_FORMAT = 18
CF_OWNERDISPLAY: win32more.Windows.Win32.System.Ole.CLIPBOARD_FORMAT = 128
CF_DSPTEXT: win32more.Windows.Win32.System.Ole.CLIPBOARD_FORMAT = 129
CF_DSPBITMAP: win32more.Windows.Win32.System.Ole.CLIPBOARD_FORMAT = 130
CF_DSPMETAFILEPICT: win32more.Windows.Win32.System.Ole.CLIPBOARD_FORMAT = 131
CF_DSPENHMETAFILE: win32more.Windows.Win32.System.Ole.CLIPBOARD_FORMAT = 142
CF_PRIVATEFIRST: win32more.Windows.Win32.System.Ole.CLIPBOARD_FORMAT = 512
CF_PRIVATELAST: win32more.Windows.Win32.System.Ole.CLIPBOARD_FORMAT = 767
CF_GDIOBJFIRST: win32more.Windows.Win32.System.Ole.CLIPBOARD_FORMAT = 768
CF_GDIOBJLAST: win32more.Windows.Win32.System.Ole.CLIPBOARD_FORMAT = 1023
class CONTROLINFO(Structure):
    cb: UInt32
    hAccel: win32more.Windows.Win32.UI.WindowsAndMessaging.HACCEL
    cAccel: UInt16
    dwFlags: UInt32
CTRLINFO = Int32
CTRLINFO_EATS_RETURN: win32more.Windows.Win32.System.Ole.CTRLINFO = 1
CTRLINFO_EATS_ESCAPE: win32more.Windows.Win32.System.Ole.CTRLINFO = 2
DISCARDCACHE = Int32
DISCARDCACHE_SAVEIFDIRTY: win32more.Windows.Win32.System.Ole.DISCARDCACHE = 0
DISCARDCACHE_NOSAVE: win32more.Windows.Win32.System.Ole.DISCARDCACHE = 1
DOCMISC = Int32
DOCMISC_CANCREATEMULTIPLEVIEWS: win32more.Windows.Win32.System.Ole.DOCMISC = 1
DOCMISC_SUPPORTCOMPLEXRECTANGLES: win32more.Windows.Win32.System.Ole.DOCMISC = 2
DOCMISC_CANTOPENEDIT: win32more.Windows.Win32.System.Ole.DOCMISC = 4
DOCMISC_NOFILESUPPORT: win32more.Windows.Win32.System.Ole.DOCMISC = 8
DROPEFFECT = UInt32
DROPEFFECT_NONE: win32more.Windows.Win32.System.Ole.DROPEFFECT = 0
DROPEFFECT_COPY: win32more.Windows.Win32.System.Ole.DROPEFFECT = 1
DROPEFFECT_MOVE: win32more.Windows.Win32.System.Ole.DROPEFFECT = 2
DROPEFFECT_LINK: win32more.Windows.Win32.System.Ole.DROPEFFECT = 4
DROPEFFECT_SCROLL: win32more.Windows.Win32.System.Ole.DROPEFFECT = 2147483648
class DVASPECTINFO(Structure):
    cb: UInt32
    dwFlags: UInt32
DVASPECTINFOFLAG = Int32
DVASPECTINFOFLAG_CANOPTIMIZE: win32more.Windows.Win32.System.Ole.DVASPECTINFOFLAG = 1
class DVEXTENTINFO(Structure):
    cb: UInt32
    dwExtentMode: UInt32
    sizelProposed: win32more.Windows.Win32.Foundation.SIZE
DVEXTENTMODE = Int32
DVEXTENT_CONTENT: win32more.Windows.Win32.System.Ole.DVEXTENTMODE = 0
DVEXTENT_INTEGRAL: win32more.Windows.Win32.System.Ole.DVEXTENTMODE = 1
EDIT_LINKS_FLAGS = UInt32
ELF_SHOWHELP: win32more.Windows.Win32.System.Ole.EDIT_LINKS_FLAGS = 1
ELF_DISABLEUPDATENOW: win32more.Windows.Win32.System.Ole.EDIT_LINKS_FLAGS = 2
ELF_DISABLEOPENSOURCE: win32more.Windows.Win32.System.Ole.EDIT_LINKS_FLAGS = 4
ELF_DISABLECHANGESOURCE: win32more.Windows.Win32.System.Ole.EDIT_LINKS_FLAGS = 8
ELF_DISABLECANCELLINK: win32more.Windows.Win32.System.Ole.EDIT_LINKS_FLAGS = 16
EMBDHLP_FLAGS = UInt32
EMBDHLP_INPROC_HANDLER: win32more.Windows.Win32.System.Ole.EMBDHLP_FLAGS = 0
EMBDHLP_INPROC_SERVER: win32more.Windows.Win32.System.Ole.EMBDHLP_FLAGS = 1
EMBDHLP_CREATENOW: win32more.Windows.Win32.System.Ole.EMBDHLP_FLAGS = 0
EMBDHLP_DELAYCREATE: win32more.Windows.Win32.System.Ole.EMBDHLP_FLAGS = 65536
ENUM_CONTROLS_WHICH_FLAGS = UInt32
GCW_WCH_SIBLING: win32more.Windows.Win32.System.Ole.ENUM_CONTROLS_WHICH_FLAGS = 1
GC_WCH_CONTAINER: win32more.Windows.Win32.System.Ole.ENUM_CONTROLS_WHICH_FLAGS = 2
GC_WCH_CONTAINED: win32more.Windows.Win32.System.Ole.ENUM_CONTROLS_WHICH_FLAGS = 3
GC_WCH_ALL: win32more.Windows.Win32.System.Ole.ENUM_CONTROLS_WHICH_FLAGS = 4
GC_WCH_FREVERSEDIR: win32more.Windows.Win32.System.Ole.ENUM_CONTROLS_WHICH_FLAGS = 134217728
GC_WCH_FONLYAFTER: win32more.Windows.Win32.System.Ole.ENUM_CONTROLS_WHICH_FLAGS = 268435456
GC_WCH_FONLYBEFORE: win32more.Windows.Win32.System.Ole.ENUM_CONTROLS_WHICH_FLAGS = 536870912
GC_WCH_FSELECTED: win32more.Windows.Win32.System.Ole.ENUM_CONTROLS_WHICH_FLAGS = 1073741824
FDEX_PROP_FLAGS = UInt32
fdexPropCanGet: win32more.Windows.Win32.System.Ole.FDEX_PROP_FLAGS = 1
fdexPropCannotGet: win32more.Windows.Win32.System.Ole.FDEX_PROP_FLAGS = 2
fdexPropCanPut: win32more.Windows.Win32.System.Ole.FDEX_PROP_FLAGS = 4
fdexPropCannotPut: win32more.Windows.Win32.System.Ole.FDEX_PROP_FLAGS = 8
fdexPropCanPutRef: win32more.Windows.Win32.System.Ole.FDEX_PROP_FLAGS = 16
fdexPropCannotPutRef: win32more.Windows.Win32.System.Ole.FDEX_PROP_FLAGS = 32
fdexPropNoSideEffects: win32more.Windows.Win32.System.Ole.FDEX_PROP_FLAGS = 64
fdexPropDynamicType: win32more.Windows.Win32.System.Ole.FDEX_PROP_FLAGS = 128
fdexPropCanCall: win32more.Windows.Win32.System.Ole.FDEX_PROP_FLAGS = 256
fdexPropCannotCall: win32more.Windows.Win32.System.Ole.FDEX_PROP_FLAGS = 512
fdexPropCanConstruct: win32more.Windows.Win32.System.Ole.FDEX_PROP_FLAGS = 1024
fdexPropCannotConstruct: win32more.Windows.Win32.System.Ole.FDEX_PROP_FLAGS = 2048
fdexPropCanSourceEvents: win32more.Windows.Win32.System.Ole.FDEX_PROP_FLAGS = 4096
fdexPropCannotSourceEvents: win32more.Windows.Win32.System.Ole.FDEX_PROP_FLAGS = 8192
class FONTDESC(Structure):
    cbSizeofstruct: UInt32
    lpstrName: win32more.Windows.Win32.Foundation.PWSTR
    cySize: win32more.Windows.Win32.System.Com.CY
    sWeight: Int16
    sCharset: Int16
    fItalic: win32more.Windows.Win32.Foundation.BOOL
    fUnderline: win32more.Windows.Win32.Foundation.BOOL
    fStrikethrough: win32more.Windows.Win32.Foundation.BOOL
GUIDKIND = Int32
GUIDKIND_DEFAULT_SOURCE_DISP_IID: win32more.Windows.Win32.System.Ole.GUIDKIND = 1
HITRESULT = Int32
HITRESULT_OUTSIDE: win32more.Windows.Win32.System.Ole.HITRESULT = 0
HITRESULT_TRANSPARENT: win32more.Windows.Win32.System.Ole.HITRESULT = 1
HITRESULT_CLOSE: win32more.Windows.Win32.System.Ole.HITRESULT = 2
HITRESULT_HIT: win32more.Windows.Win32.System.Ole.HITRESULT = 3
class IAdviseSinkEx(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IAdviseSink
    _iid_ = Guid('{3af24290-0c96-11ce-a0cf-00aa00600ab8}')
    @commethod(8)
    def OnViewStatusChange(self, dwViewStatus: UInt32) -> Void: ...
class ICanHandleException(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c5598e60-b307-11d1-b27d-006008c3fbfb}')
    @commethod(3)
    def CanHandleException(self, pExcepInfo: POINTER(win32more.Windows.Win32.System.Com.EXCEPINFO), pvar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IClassFactory2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IClassFactory
    _iid_ = Guid('{b196b28f-bab4-101a-b69c-00aa00341d07}')
    @commethod(5)
    def GetLicInfo(self, pLicInfo: POINTER(win32more.Windows.Win32.System.Ole.LICINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RequestLicKey(self, dwReserved: UInt32, pBstrKey: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateInstanceLic(self, pUnkOuter: win32more.Windows.Win32.System.Com.IUnknown, pUnkReserved: win32more.Windows.Win32.System.Com.IUnknown, riid: POINTER(Guid), bstrKey: win32more.Windows.Win32.Foundation.BSTR, ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IContinue(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000012a-0000-0000-c000-000000000046}')
    @commethod(3)
    def FContinue(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IContinueCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b722bcca-4e68-101b-a2bc-00aa00404770}')
    @commethod(3)
    def FContinue(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FContinuePrinting(self, nCntPrinted: Int32, nCurPage: Int32, pwszPrintStatus: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICreateErrorInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{22f03340-547d-101b-8e65-08002b2bd119}')
    @commethod(3)
    def SetGUID(self, rguid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetSource(self, szSource: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetDescription(self, szDescription: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetHelpFile(self, szHelpFile: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetHelpContext(self, dwHelpContext: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICreateTypeInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00020405-0000-0000-c000-000000000046}')
    @commethod(3)
    def SetGuid(self, guid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetTypeFlags(self, uTypeFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetDocString(self, pStrDoc: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetHelpContext(self, dwHelpContext: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetVersion(self, wMajorVerNum: UInt16, wMinorVerNum: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AddRefTypeInfo(self, pTInfo: win32more.Windows.Win32.System.Com.ITypeInfo, phRefType: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddFuncDesc(self, index: UInt32, pFuncDesc: POINTER(win32more.Windows.Win32.System.Com.FUNCDESC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def AddImplType(self, index: UInt32, hRefType: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetImplTypeFlags(self, index: UInt32, implTypeFlags: win32more.Windows.Win32.System.Com.IMPLTYPEFLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetAlignment(self, cbAlignment: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetSchema(self, pStrSchema: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def AddVarDesc(self, index: UInt32, pVarDesc: POINTER(win32more.Windows.Win32.System.Com.VARDESC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetFuncAndParamNames(self, index: UInt32, rgszNames: POINTER(win32more.Windows.Win32.Foundation.PWSTR), cNames: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetVarName(self, index: UInt32, szName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetTypeDescAlias(self, pTDescAlias: POINTER(win32more.Windows.Win32.System.Com.TYPEDESC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def DefineFuncAsDllEntry(self, index: UInt32, szDllName: win32more.Windows.Win32.Foundation.PWSTR, szProcName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetFuncDocString(self, index: UInt32, szDocString: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetVarDocString(self, index: UInt32, szDocString: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetFuncHelpContext(self, index: UInt32, dwHelpContext: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetVarHelpContext(self, index: UInt32, dwHelpContext: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetMops(self, index: UInt32, bstrMops: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetTypeIdldesc(self, pIdlDesc: POINTER(win32more.Windows.Win32.System.Com.IDLDESC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def LayOut(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICreateTypeInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.Ole.ICreateTypeInfo
    _iid_ = Guid('{0002040e-0000-0000-c000-000000000046}')
    @commethod(26)
    def DeleteFuncDesc(self, index: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def DeleteFuncDescByMemId(self, memid: Int32, invKind: win32more.Windows.Win32.System.Com.INVOKEKIND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def DeleteVarDesc(self, index: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def DeleteVarDescByMemId(self, memid: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def DeleteImplType(self, index: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def SetCustData(self, guid: POINTER(Guid), pVarVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def SetFuncCustData(self, index: UInt32, guid: POINTER(Guid), pVarVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def SetParamCustData(self, indexFunc: UInt32, indexParam: UInt32, guid: POINTER(Guid), pVarVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def SetVarCustData(self, index: UInt32, guid: POINTER(Guid), pVarVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def SetImplTypeCustData(self, index: UInt32, guid: POINTER(Guid), pVarVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def SetHelpStringContext(self, dwHelpStringContext: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def SetFuncHelpStringContext(self, index: UInt32, dwHelpStringContext: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def SetVarHelpStringContext(self, index: UInt32, dwHelpStringContext: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def Invalidate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def SetName(self, szName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICreateTypeLib(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00020406-0000-0000-c000-000000000046}')
    @commethod(3)
    def CreateTypeInfo(self, szName: win32more.Windows.Win32.Foundation.PWSTR, tkind: win32more.Windows.Win32.System.Com.TYPEKIND, ppCTInfo: POINTER(win32more.Windows.Win32.System.Ole.ICreateTypeInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetName(self, szName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetVersion(self, wMajorVerNum: UInt16, wMinorVerNum: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetGuid(self, guid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetDocString(self, szDoc: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetHelpFileName(self, szHelpFileName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetHelpContext(self, dwHelpContext: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetLcid(self, lcid: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetLibFlags(self, uLibFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SaveAllChanges(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICreateTypeLib2(ComPtr):
    extends: win32more.Windows.Win32.System.Ole.ICreateTypeLib
    _iid_ = Guid('{0002040f-0000-0000-c000-000000000046}')
    @commethod(13)
    def DeleteTypeInfo(self, szName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetCustData(self, guid: POINTER(Guid), pVarVal: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetHelpStringContext(self, dwHelpStringContext: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetHelpStringDll(self, szFileName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDispError(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a6ef9861-c720-11d0-9337-00a0c90dcaa9}')
    @commethod(3)
    def QueryErrorInfo(self, guidErrorType: Guid, ppde: POINTER(win32more.Windows.Win32.System.Ole.IDispError)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNext(self, ppde: POINTER(win32more.Windows.Win32.System.Ole.IDispError)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetHresult(self, phr: POINTER(win32more.Windows.Win32.Foundation.HRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSource(self, pbstrSource: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetHelpInfo(self, pbstrFileName: POINTER(win32more.Windows.Win32.Foundation.BSTR), pdwContext: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDescription(self, pbstrDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDispatchEx(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{a6ef9860-c720-11d0-9337-00a0c90dcaa9}')
    @commethod(7)
    def GetDispID(self, bstrName: win32more.Windows.Win32.Foundation.BSTR, grfdex: UInt32, pid: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def InvokeEx(self, id: Int32, lcid: UInt32, wFlags: UInt16, pdp: POINTER(win32more.Windows.Win32.System.Com.DISPPARAMS), pvarRes: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pei: POINTER(win32more.Windows.Win32.System.Com.EXCEPINFO), pspCaller: win32more.Windows.Win32.System.Com.IServiceProvider) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def DeleteMemberByName(self, bstrName: win32more.Windows.Win32.Foundation.BSTR, grfdex: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def DeleteMemberByDispID(self, id: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetMemberProperties(self, id: Int32, grfdexFetch: UInt32, pgrfdex: POINTER(win32more.Windows.Win32.System.Ole.FDEX_PROP_FLAGS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetMemberName(self, id: Int32, pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetNextDispID(self, grfdex: UInt32, id: Int32, pid: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetNameSpaceParent(self, ppunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDropSource(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000121-0000-0000-c000-000000000046}')
    @commethod(3)
    def QueryContinueDrag(self, fEscapePressed: win32more.Windows.Win32.Foundation.BOOL, grfKeyState: win32more.Windows.Win32.System.SystemServices.MODIFIERKEYS_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GiveFeedback(self, dwEffect: win32more.Windows.Win32.System.Ole.DROPEFFECT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDropSourceNotify(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000012b-0000-0000-c000-000000000046}')
    @commethod(3)
    def DragEnterTarget(self, hwndTarget: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DragLeaveTarget(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDropTarget(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000122-0000-0000-c000-000000000046}')
    @commethod(3)
    def DragEnter(self, pDataObj: win32more.Windows.Win32.System.Com.IDataObject, grfKeyState: win32more.Windows.Win32.System.SystemServices.MODIFIERKEYS_FLAGS, pt: win32more.Windows.Win32.Foundation.POINTL, pdwEffect: POINTER(win32more.Windows.Win32.System.Ole.DROPEFFECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DragOver(self, grfKeyState: win32more.Windows.Win32.System.SystemServices.MODIFIERKEYS_FLAGS, pt: win32more.Windows.Win32.Foundation.POINTL, pdwEffect: POINTER(win32more.Windows.Win32.System.Ole.DROPEFFECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DragLeave(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Drop(self, pDataObj: win32more.Windows.Win32.System.Com.IDataObject, grfKeyState: win32more.Windows.Win32.System.SystemServices.MODIFIERKEYS_FLAGS, pt: win32more.Windows.Win32.Foundation.POINTL, pdwEffect: POINTER(win32more.Windows.Win32.System.Ole.DROPEFFECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnterpriseDropTarget(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{390e3878-fd55-4e18-819d-4682081c0cfd}')
    @commethod(3)
    def SetDropSourceEnterpriseId(self, identity: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsEvaluatingEdpPolicy(self, value: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumOLEVERB(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000104-0000-0000-c000-000000000046}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.System.Ole.OLEVERB), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.System.Ole.IEnumOLEVERB)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumOleDocumentViews(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b722bcc8-4e68-101b-a2bc-00aa00404770}')
    @commethod(3)
    def Next(self, cViews: UInt32, rgpView: POINTER(win32more.Windows.Win32.System.Ole.IOleDocumentView), pcFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cViews: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.System.Ole.IEnumOleDocumentViews)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumOleUndoUnits(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b3e7c340-ef97-11ce-9bc9-00aa00608e01}')
    @commethod(3)
    def Next(self, cElt: UInt32, rgElt: POINTER(win32more.Windows.Win32.System.Ole.IOleUndoUnit), pcEltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cElt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.System.Ole.IEnumOleUndoUnits)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumVARIANT(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00020404-0000-0000-c000-000000000046}')
    @commethod(3)
    def Next(self, celt: UInt32, rgVar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pCeltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.System.Ole.IEnumVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFont(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bef6e002-a874-101a-8bba-00aa00300cab}')
    @commethod(3)
    def get_Name(self, pName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def put_Name(self, name: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_Size(self, pSize: POINTER(win32more.Windows.Win32.System.Com.CY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_Size(self, size: win32more.Windows.Win32.System.Com.CY) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Bold(self, pBold: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Bold(self, bold: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Italic(self, pItalic: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Italic(self, italic: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Underline(self, pUnderline: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Underline(self, underline: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Strikethrough(self, pStrikethrough: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Strikethrough(self, strikethrough: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Weight(self, pWeight: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Weight(self, weight: Int16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Charset(self, pCharset: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_Charset(self, charset: Int16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_hFont(self, phFont: POINTER(win32more.Windows.Win32.Graphics.Gdi.HFONT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def Clone(self, ppFont: POINTER(win32more.Windows.Win32.System.Ole.IFont)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def IsEqual(self, pFontOther: win32more.Windows.Win32.System.Ole.IFont) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetRatio(self, cyLogical: Int32, cyHimetric: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def QueryTextMetrics(self, pTM: POINTER(win32more.Windows.Win32.Graphics.Gdi.TEXTMETRICW)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def AddRefHfont(self, hFont: win32more.Windows.Win32.Graphics.Gdi.HFONT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def ReleaseHfont(self, hFont: win32more.Windows.Win32.Graphics.Gdi.HFONT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def SetHdc(self, hDC: win32more.Windows.Win32.Graphics.Gdi.HDC) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFontDisp(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{bef6e003-a874-101a-8bba-00aa00300cab}')
class IFontEventsDisp(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{4ef6100a-af88-11d0-9846-00c04fc29993}')
IGNOREMIME = Int32
IGNOREMIME_PROMPT: win32more.Windows.Win32.System.Ole.IGNOREMIME = 1
IGNOREMIME_TEXT: win32more.Windows.Win32.System.Ole.IGNOREMIME = 2
class IGetOleObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8a701da0-4feb-101b-a82e-08002b2b2337}')
    @commethod(3)
    def GetOleObject(self, riid: POINTER(Guid), ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IGetVBAObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{91733a60-3f4c-101b-a3f6-00aa0034e4e9}')
    @commethod(3)
    def GetObject(self, riid: POINTER(Guid), ppvObj: POINTER(VoidPtr), dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
INSERT_OBJECT_FLAGS = UInt32
IOF_SHOWHELP: win32more.Windows.Win32.System.Ole.INSERT_OBJECT_FLAGS = 1
IOF_SELECTCREATENEW: win32more.Windows.Win32.System.Ole.INSERT_OBJECT_FLAGS = 2
IOF_SELECTCREATEFROMFILE: win32more.Windows.Win32.System.Ole.INSERT_OBJECT_FLAGS = 4
IOF_CHECKLINK: win32more.Windows.Win32.System.Ole.INSERT_OBJECT_FLAGS = 8
IOF_CHECKDISPLAYASICON: win32more.Windows.Win32.System.Ole.INSERT_OBJECT_FLAGS = 16
IOF_CREATENEWOBJECT: win32more.Windows.Win32.System.Ole.INSERT_OBJECT_FLAGS = 32
IOF_CREATEFILEOBJECT: win32more.Windows.Win32.System.Ole.INSERT_OBJECT_FLAGS = 64
IOF_CREATELINKOBJECT: win32more.Windows.Win32.System.Ole.INSERT_OBJECT_FLAGS = 128
IOF_DISABLELINK: win32more.Windows.Win32.System.Ole.INSERT_OBJECT_FLAGS = 256
IOF_VERIFYSERVERSEXIST: win32more.Windows.Win32.System.Ole.INSERT_OBJECT_FLAGS = 512
IOF_DISABLEDISPLAYASICON: win32more.Windows.Win32.System.Ole.INSERT_OBJECT_FLAGS = 1024
IOF_HIDECHANGEICON: win32more.Windows.Win32.System.Ole.INSERT_OBJECT_FLAGS = 2048
IOF_SHOWINSERTCONTROL: win32more.Windows.Win32.System.Ole.INSERT_OBJECT_FLAGS = 4096
IOF_SELECTCREATECONTROL: win32more.Windows.Win32.System.Ole.INSERT_OBJECT_FLAGS = 8192
class INTERFACEDATA(Structure):
    pmethdata: POINTER(win32more.Windows.Win32.System.Ole.METHODDATA)
    cMembers: UInt32
class IObjectIdentity(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ca04b7e6-0d21-11d1-8cc5-00c04fc2b085}')
    @commethod(3)
    def IsEqualObject(self, punk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IObjectWithSite(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fc4801a3-2ba9-11cf-a229-00aa003d7352}')
    @commethod(3)
    def SetSite(self, pUnkSite: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSite(self, riid: POINTER(Guid), ppvSite: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOleAdviseHolder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000111-0000-0000-c000-000000000046}')
    @commethod(3)
    def Advise(self, pAdvise: win32more.Windows.Win32.System.Com.IAdviseSink, pdwConnection: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unadvise(self, dwConnection: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumAdvise(self, ppenumAdvise: POINTER(win32more.Windows.Win32.System.Com.IEnumSTATDATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SendOnRename(self, pmk: win32more.Windows.Win32.System.Com.IMoniker) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SendOnSave(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SendOnClose(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOleCache(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000011e-0000-0000-c000-000000000046}')
    @commethod(3)
    def Cache(self, pformatetc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC), advf: UInt32, pdwConnection: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Uncache(self, dwConnection: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumCache(self, ppenumSTATDATA: POINTER(win32more.Windows.Win32.System.Com.IEnumSTATDATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def InitCache(self, pDataObject: win32more.Windows.Win32.System.Com.IDataObject) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetData(self, pformatetc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC), pmedium: POINTER(win32more.Windows.Win32.System.Com.STGMEDIUM), fRelease: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOleCache2(ComPtr):
    extends: win32more.Windows.Win32.System.Ole.IOleCache
    _iid_ = Guid('{00000128-0000-0000-c000-000000000046}')
    @commethod(8)
    def UpdateCache(self, pDataObject: win32more.Windows.Win32.System.Com.IDataObject, grfUpdf: win32more.Windows.Win32.System.Ole.UPDFCACHE_FLAGS, pReserved: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def DiscardCache(self, dwDiscardOptions: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOleCacheControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000129-0000-0000-c000-000000000046}')
    @commethod(3)
    def OnRun(self, pDataObject: win32more.Windows.Win32.System.Com.IDataObject) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnStop(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOleClientSite(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000118-0000-0000-c000-000000000046}')
    @commethod(3)
    def SaveObject(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMoniker(self, dwAssign: UInt32, dwWhichMoniker: UInt32, ppmk: POINTER(win32more.Windows.Win32.System.Com.IMoniker)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetContainer(self, ppContainer: POINTER(win32more.Windows.Win32.System.Ole.IOleContainer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ShowObject(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnShowWindow(self, fShow: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RequestNewObjectLayout(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOleCommandTarget(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b722bccb-4e68-101b-a2bc-00aa00404770}')
    @commethod(3)
    def QueryStatus(self, pguidCmdGroup: POINTER(Guid), cCmds: UInt32, prgCmds: POINTER(win32more.Windows.Win32.System.Ole.OLECMD), pCmdText: POINTER(win32more.Windows.Win32.System.Ole.OLECMDTEXT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Exec(self, pguidCmdGroup: POINTER(Guid), nCmdID: UInt32, nCmdexecopt: UInt32, pvaIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvaOut: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOleContainer(ComPtr):
    extends: win32more.Windows.Win32.System.Ole.IParseDisplayName
    _iid_ = Guid('{0000011b-0000-0000-c000-000000000046}')
    @commethod(4)
    def EnumObjects(self, grfFlags: UInt32, ppenum: POINTER(win32more.Windows.Win32.System.Com.IEnumUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def LockContainer(self, fLock: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOleControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b196b288-bab4-101a-b69c-00aa00341d07}')
    @commethod(3)
    def GetControlInfo(self, pCI: POINTER(win32more.Windows.Win32.System.Ole.CONTROLINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnMnemonic(self, pMsg: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.MSG)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnAmbientPropertyChange(self, dispID: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FreezeEvents(self, bFreeze: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOleControlSite(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b196b289-bab4-101a-b69c-00aa00341d07}')
    @commethod(3)
    def OnControlInfoChanged(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LockInPlaceActive(self, fLock: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetExtendedControl(self, ppDisp: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def TransformCoords(self, pPtlHimetric: POINTER(win32more.Windows.Win32.Foundation.POINTL), pPtfContainer: POINTER(win32more.Windows.Win32.System.Ole.POINTF), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def TranslateAccelerator(self, pMsg: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.MSG), grfModifiers: win32more.Windows.Win32.System.Ole.KEYMODIFIERS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnFocus(self, fGotFocus: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ShowPropertyFrame(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOleDocument(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b722bcc5-4e68-101b-a2bc-00aa00404770}')
    @commethod(3)
    def CreateView(self, pIPSite: win32more.Windows.Win32.System.Ole.IOleInPlaceSite, pstm: win32more.Windows.Win32.System.Com.IStream, dwReserved: UInt32, ppView: POINTER(win32more.Windows.Win32.System.Ole.IOleDocumentView)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDocMiscStatus(self, pdwStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumViews(self, ppEnum: POINTER(win32more.Windows.Win32.System.Ole.IEnumOleDocumentViews), ppView: POINTER(win32more.Windows.Win32.System.Ole.IOleDocumentView)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOleDocumentSite(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b722bcc7-4e68-101b-a2bc-00aa00404770}')
    @commethod(3)
    def ActivateMe(self, pViewToActivate: win32more.Windows.Win32.System.Ole.IOleDocumentView) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOleDocumentView(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b722bcc6-4e68-101b-a2bc-00aa00404770}')
    @commethod(3)
    def SetInPlaceSite(self, pIPSite: win32more.Windows.Win32.System.Ole.IOleInPlaceSite) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInPlaceSite(self, ppIPSite: POINTER(win32more.Windows.Win32.System.Ole.IOleInPlaceSite)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDocument(self, ppunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetRect(self, prcView: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetRect(self, prcView: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetRectComplex(self, prcView: POINTER(win32more.Windows.Win32.Foundation.RECT), prcHScroll: POINTER(win32more.Windows.Win32.Foundation.RECT), prcVScroll: POINTER(win32more.Windows.Win32.Foundation.RECT), prcSizeBox: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Show(self, fShow: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def UIActivate(self, fUIActivate: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Open(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def CloseView(self, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SaveViewState(self, pstm: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def ApplyViewState(self, pstm: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Clone(self, pIPSiteNew: win32more.Windows.Win32.System.Ole.IOleInPlaceSite, ppViewNew: POINTER(win32more.Windows.Win32.System.Ole.IOleDocumentView)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOleInPlaceActiveObject(ComPtr):
    extends: win32more.Windows.Win32.System.Ole.IOleWindow
    _iid_ = Guid('{00000117-0000-0000-c000-000000000046}')
    @commethod(5)
    def TranslateAccelerator(self, lpmsg: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.MSG)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnFrameWindowActivate(self, fActivate: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnDocWindowActivate(self, fActivate: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ResizeBorder(self, prcBorder: POINTER(win32more.Windows.Win32.Foundation.RECT), pUIWindow: win32more.Windows.Win32.System.Ole.IOleInPlaceUIWindow, fFrameWindow: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnableModeless(self, fEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOleInPlaceFrame(ComPtr):
    extends: win32more.Windows.Win32.System.Ole.IOleInPlaceUIWindow
    _iid_ = Guid('{00000116-0000-0000-c000-000000000046}')
    @commethod(9)
    def InsertMenus(self, hmenuShared: win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU, lpMenuWidths: POINTER(win32more.Windows.Win32.System.Ole.OLEMENUGROUPWIDTHS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetMenu(self, hmenuShared: win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU, holemenu: IntPtr, hwndActiveObject: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RemoveMenus(self, hmenuShared: win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetStatusText(self, pszStatusText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def EnableModeless(self, fEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def TranslateAccelerator(self, lpmsg: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.MSG), wID: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOleInPlaceObject(ComPtr):
    extends: win32more.Windows.Win32.System.Ole.IOleWindow
    _iid_ = Guid('{00000113-0000-0000-c000-000000000046}')
    @commethod(5)
    def InPlaceDeactivate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def UIDeactivate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetObjectRects(self, lprcPosRect: POINTER(win32more.Windows.Win32.Foundation.RECT), lprcClipRect: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ReactivateAndUndo(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOleInPlaceObjectWindowless(ComPtr):
    extends: win32more.Windows.Win32.System.Ole.IOleInPlaceObject
    _iid_ = Guid('{1c2056cc-5ef4-101b-8bc8-00aa003e3b29}')
    @commethod(9)
    def OnWindowMessage(self, msg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM, plResult: POINTER(win32more.Windows.Win32.Foundation.LRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDropTarget(self, ppDropTarget: POINTER(win32more.Windows.Win32.System.Ole.IDropTarget)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOleInPlaceSite(ComPtr):
    extends: win32more.Windows.Win32.System.Ole.IOleWindow
    _iid_ = Guid('{00000119-0000-0000-c000-000000000046}')
    @commethod(5)
    def CanInPlaceActivate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnInPlaceActivate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnUIActivate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetWindowContext(self, ppFrame: POINTER(win32more.Windows.Win32.System.Ole.IOleInPlaceFrame), ppDoc: POINTER(win32more.Windows.Win32.System.Ole.IOleInPlaceUIWindow), lprcPosRect: POINTER(win32more.Windows.Win32.Foundation.RECT), lprcClipRect: POINTER(win32more.Windows.Win32.Foundation.RECT), lpFrameInfo: POINTER(win32more.Windows.Win32.System.Ole.OLEINPLACEFRAMEINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Scroll(self, scrollExtant: win32more.Windows.Win32.Foundation.SIZE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OnUIDeactivate(self, fUndoable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def OnInPlaceDeactivate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def DiscardUndoState(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def DeactivateAndUndo(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def OnPosRectChange(self, lprcPosRect: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOleInPlaceSiteEx(ComPtr):
    extends: win32more.Windows.Win32.System.Ole.IOleInPlaceSite
    _iid_ = Guid('{9c2cad80-3424-11cf-b670-00aa004cd6d8}')
    @commethod(15)
    def OnInPlaceActivateEx(self, pfNoRedraw: POINTER(win32more.Windows.Win32.Foundation.BOOL), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def OnInPlaceDeactivateEx(self, fNoRedraw: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def RequestUIActivate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOleInPlaceSiteWindowless(ComPtr):
    extends: win32more.Windows.Win32.System.Ole.IOleInPlaceSiteEx
    _iid_ = Guid('{922eada0-3424-11cf-b670-00aa004cd6d8}')
    @commethod(18)
    def CanWindowlessActivate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetCapture(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetCapture(self, fCapture: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetFocus(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetFocus(self, fFocus: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetDC(self, pRect: POINTER(win32more.Windows.Win32.Foundation.RECT), grfFlags: UInt32, phDC: POINTER(win32more.Windows.Win32.Graphics.Gdi.HDC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def ReleaseDC(self, hDC: win32more.Windows.Win32.Graphics.Gdi.HDC) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def InvalidateRect(self, pRect: POINTER(win32more.Windows.Win32.Foundation.RECT), fErase: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def InvalidateRgn(self, hRGN: win32more.Windows.Win32.Graphics.Gdi.HRGN, fErase: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def ScrollRect(self, dx: Int32, dy: Int32, pRectScroll: POINTER(win32more.Windows.Win32.Foundation.RECT), pRectClip: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def AdjustRect(self, prc: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def OnDefWindowMessage(self, msg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM, plResult: POINTER(win32more.Windows.Win32.Foundation.LRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOleInPlaceUIWindow(ComPtr):
    extends: win32more.Windows.Win32.System.Ole.IOleWindow
    _iid_ = Guid('{00000115-0000-0000-c000-000000000046}')
    @commethod(5)
    def GetBorder(self, lprectBorder: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RequestBorderSpace(self, pborderwidths: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetBorderSpace(self, pborderwidths: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetActiveObject(self, pActiveObject: win32more.Windows.Win32.System.Ole.IOleInPlaceActiveObject, pszObjName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOleItemContainer(ComPtr):
    extends: win32more.Windows.Win32.System.Ole.IOleContainer
    _iid_ = Guid('{0000011c-0000-0000-c000-000000000046}')
    @commethod(6)
    def GetObject(self, pszItem: win32more.Windows.Win32.Foundation.PWSTR, dwSpeedNeeded: UInt32, pbc: win32more.Windows.Win32.System.Com.IBindCtx, riid: POINTER(Guid), ppvObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetObjectStorage(self, pszItem: win32more.Windows.Win32.Foundation.PWSTR, pbc: win32more.Windows.Win32.System.Com.IBindCtx, riid: POINTER(Guid), ppvStorage: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsRunning(self, pszItem: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOleLink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000011d-0000-0000-c000-000000000046}')
    @commethod(3)
    def SetUpdateOptions(self, dwUpdateOpt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetUpdateOptions(self, pdwUpdateOpt: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetSourceMoniker(self, pmk: win32more.Windows.Win32.System.Com.IMoniker, rclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSourceMoniker(self, ppmk: POINTER(win32more.Windows.Win32.System.Com.IMoniker)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetSourceDisplayName(self, pszStatusText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSourceDisplayName(self, ppszDisplayName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def BindToSource(self, bindflags: UInt32, pbc: win32more.Windows.Win32.System.Com.IBindCtx) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def BindIfRunning(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetBoundSource(self, ppunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def UnbindSource(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Update(self, pbc: win32more.Windows.Win32.System.Com.IBindCtx) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOleObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000112-0000-0000-c000-000000000046}')
    @commethod(3)
    def SetClientSite(self, pClientSite: win32more.Windows.Win32.System.Ole.IOleClientSite) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetClientSite(self, ppClientSite: POINTER(win32more.Windows.Win32.System.Ole.IOleClientSite)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetHostNames(self, szContainerApp: win32more.Windows.Win32.Foundation.PWSTR, szContainerObj: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Close(self, dwSaveOption: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetMoniker(self, dwWhichMoniker: UInt32, pmk: win32more.Windows.Win32.System.Com.IMoniker) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetMoniker(self, dwAssign: UInt32, dwWhichMoniker: UInt32, ppmk: POINTER(win32more.Windows.Win32.System.Com.IMoniker)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def InitFromData(self, pDataObject: win32more.Windows.Win32.System.Com.IDataObject, fCreation: win32more.Windows.Win32.Foundation.BOOL, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetClipboardData(self, dwReserved: UInt32, ppDataObject: POINTER(win32more.Windows.Win32.System.Com.IDataObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def DoVerb(self, iVerb: Int32, lpmsg: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.MSG), pActiveSite: win32more.Windows.Win32.System.Ole.IOleClientSite, lindex: Int32, hwndParent: win32more.Windows.Win32.Foundation.HWND, lprcPosRect: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def EnumVerbs(self, ppEnumOleVerb: POINTER(win32more.Windows.Win32.System.Ole.IEnumOLEVERB)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Update(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def IsUpToDate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetUserClassID(self, pClsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetUserType(self, dwFormOfType: UInt32, pszUserType: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetExtent(self, dwDrawAspect: win32more.Windows.Win32.System.Com.DVASPECT, psizel: POINTER(win32more.Windows.Win32.Foundation.SIZE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetExtent(self, dwDrawAspect: win32more.Windows.Win32.System.Com.DVASPECT, psizel: POINTER(win32more.Windows.Win32.Foundation.SIZE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Advise(self, pAdvSink: win32more.Windows.Win32.System.Com.IAdviseSink, pdwConnection: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def Unadvise(self, dwConnection: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def EnumAdvise(self, ppenumAdvise: POINTER(win32more.Windows.Win32.System.Com.IEnumSTATDATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetMiscStatus(self, dwAspect: win32more.Windows.Win32.System.Com.DVASPECT, pdwStatus: POINTER(win32more.Windows.Win32.System.Ole.OLEMISC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetColorScheme(self, pLogpal: POINTER(win32more.Windows.Win32.Graphics.Gdi.LOGPALETTE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOleParentUndoUnit(ComPtr):
    extends: win32more.Windows.Win32.System.Ole.IOleUndoUnit
    _iid_ = Guid('{a1faf330-ef97-11ce-9bc9-00aa00608e01}')
    @commethod(7)
    def Open(self, pPUU: win32more.Windows.Win32.System.Ole.IOleParentUndoUnit) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Close(self, pPUU: win32more.Windows.Win32.System.Ole.IOleParentUndoUnit, fCommit: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Add(self, pUU: win32more.Windows.Win32.System.Ole.IOleUndoUnit) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def FindUnit(self, pUU: win32more.Windows.Win32.System.Ole.IOleUndoUnit) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetParentState(self, pdwState: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOleUILinkContainerA(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def GetNextLink(self, dwLink: UInt32) -> UInt32: ...
    @commethod(4)
    def SetLinkUpdateOptions(self, dwLink: UInt32, dwUpdateOpt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLinkUpdateOptions(self, dwLink: UInt32, lpdwUpdateOpt: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetLinkSource(self, dwLink: UInt32, lpszDisplayName: win32more.Windows.Win32.Foundation.PSTR, lenFileName: UInt32, pchEaten: POINTER(UInt32), fValidateSource: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetLinkSource(self, dwLink: UInt32, lplpszDisplayName: POINTER(win32more.Windows.Win32.Foundation.PSTR), lplenFileName: POINTER(UInt32), lplpszFullLinkType: POINTER(win32more.Windows.Win32.Foundation.PSTR), lplpszShortLinkType: POINTER(win32more.Windows.Win32.Foundation.PSTR), lpfSourceAvailable: POINTER(win32more.Windows.Win32.Foundation.BOOL), lpfIsSelected: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OpenLinkSource(self, dwLink: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def UpdateLink(self, dwLink: UInt32, fErrorMessage: win32more.Windows.Win32.Foundation.BOOL, fReserved: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CancelLink(self, dwLink: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOleUILinkContainerW(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def GetNextLink(self, dwLink: UInt32) -> UInt32: ...
    @commethod(4)
    def SetLinkUpdateOptions(self, dwLink: UInt32, dwUpdateOpt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLinkUpdateOptions(self, dwLink: UInt32, lpdwUpdateOpt: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetLinkSource(self, dwLink: UInt32, lpszDisplayName: win32more.Windows.Win32.Foundation.PWSTR, lenFileName: UInt32, pchEaten: POINTER(UInt32), fValidateSource: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetLinkSource(self, dwLink: UInt32, lplpszDisplayName: POINTER(win32more.Windows.Win32.Foundation.PWSTR), lplenFileName: POINTER(UInt32), lplpszFullLinkType: POINTER(win32more.Windows.Win32.Foundation.PWSTR), lplpszShortLinkType: POINTER(win32more.Windows.Win32.Foundation.PWSTR), lpfSourceAvailable: POINTER(win32more.Windows.Win32.Foundation.BOOL), lpfIsSelected: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OpenLinkSource(self, dwLink: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def UpdateLink(self, dwLink: UInt32, fErrorMessage: win32more.Windows.Win32.Foundation.BOOL, fReserved: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CancelLink(self, dwLink: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
IOleUILinkContainer = UnicodeAlias('IOleUILinkContainerW')
class IOleUILinkInfoA(ComPtr):
    extends: win32more.Windows.Win32.System.Ole.IOleUILinkContainerA
    @commethod(11)
    def GetLastUpdate(self, dwLink: UInt32, lpLastUpdate: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOleUILinkInfoW(ComPtr):
    extends: win32more.Windows.Win32.System.Ole.IOleUILinkContainerW
    @commethod(11)
    def GetLastUpdate(self, dwLink: UInt32, lpLastUpdate: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
IOleUILinkInfo = UnicodeAlias('IOleUILinkInfoW')
class IOleUIObjInfoA(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def GetObjectInfo(self, dwObject: UInt32, lpdwObjSize: POINTER(UInt32), lplpszLabel: POINTER(win32more.Windows.Win32.Foundation.PSTR), lplpszType: POINTER(win32more.Windows.Win32.Foundation.PSTR), lplpszShortType: POINTER(win32more.Windows.Win32.Foundation.PSTR), lplpszLocation: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetConvertInfo(self, dwObject: UInt32, lpClassID: POINTER(Guid), lpwFormat: POINTER(UInt16), lpConvertDefaultClassID: POINTER(Guid), lplpClsidExclude: POINTER(POINTER(Guid)), lpcClsidExclude: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ConvertObject(self, dwObject: UInt32, clsidNew: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetViewInfo(self, dwObject: UInt32, phMetaPict: POINTER(win32more.Windows.Win32.Foundation.HGLOBAL), pdvAspect: POINTER(UInt32), pnCurrentScale: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetViewInfo(self, dwObject: UInt32, hMetaPict: win32more.Windows.Win32.Foundation.HGLOBAL, dvAspect: UInt32, nCurrentScale: Int32, bRelativeToOrig: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOleUIObjInfoW(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    @commethod(3)
    def GetObjectInfo(self, dwObject: UInt32, lpdwObjSize: POINTER(UInt32), lplpszLabel: POINTER(win32more.Windows.Win32.Foundation.PWSTR), lplpszType: POINTER(win32more.Windows.Win32.Foundation.PWSTR), lplpszShortType: POINTER(win32more.Windows.Win32.Foundation.PWSTR), lplpszLocation: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetConvertInfo(self, dwObject: UInt32, lpClassID: POINTER(Guid), lpwFormat: POINTER(UInt16), lpConvertDefaultClassID: POINTER(Guid), lplpClsidExclude: POINTER(POINTER(Guid)), lpcClsidExclude: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ConvertObject(self, dwObject: UInt32, clsidNew: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetViewInfo(self, dwObject: UInt32, phMetaPict: POINTER(win32more.Windows.Win32.Foundation.HGLOBAL), pdvAspect: POINTER(UInt32), pnCurrentScale: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetViewInfo(self, dwObject: UInt32, hMetaPict: win32more.Windows.Win32.Foundation.HGLOBAL, dvAspect: UInt32, nCurrentScale: Int32, bRelativeToOrig: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
IOleUIObjInfo = UnicodeAlias('IOleUIObjInfoW')
class IOleUndoManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d001f200-ef97-11ce-9bc9-00aa00608e01}')
    @commethod(3)
    def Open(self, pPUU: win32more.Windows.Win32.System.Ole.IOleParentUndoUnit) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Close(self, pPUU: win32more.Windows.Win32.System.Ole.IOleParentUndoUnit, fCommit: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Add(self, pUU: win32more.Windows.Win32.System.Ole.IOleUndoUnit) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetOpenParentState(self, pdwState: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def DiscardFrom(self, pUU: win32more.Windows.Win32.System.Ole.IOleUndoUnit) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def UndoTo(self, pUU: win32more.Windows.Win32.System.Ole.IOleUndoUnit) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RedoTo(self, pUU: win32more.Windows.Win32.System.Ole.IOleUndoUnit) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EnumUndoable(self, ppEnum: POINTER(win32more.Windows.Win32.System.Ole.IEnumOleUndoUnits)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EnumRedoable(self, ppEnum: POINTER(win32more.Windows.Win32.System.Ole.IEnumOleUndoUnits)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetLastUndoDescription(self, pBstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetLastRedoDescription(self, pBstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Enable(self, fEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOleUndoUnit(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{894ad3b0-ef97-11ce-9bc9-00aa00608e01}')
    @commethod(3)
    def Do(self, pUndoManager: win32more.Windows.Win32.System.Ole.IOleUndoManager) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDescription(self, pBstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetUnitType(self, pClsid: POINTER(Guid), plID: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnNextAdd(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOleWindow(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00000114-0000-0000-c000-000000000046}')
    @commethod(3)
    def GetWindow(self, phwnd: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ContextSensitiveHelp(self, fEnterMode: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IParseDisplayName(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000011a-0000-0000-c000-000000000046}')
    @commethod(3)
    def ParseDisplayName(self, pbc: win32more.Windows.Win32.System.Com.IBindCtx, pszDisplayName: win32more.Windows.Win32.Foundation.PWSTR, pchEaten: POINTER(UInt32), ppmkOut: POINTER(win32more.Windows.Win32.System.Com.IMoniker)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPerPropertyBrowsing(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{376bd3aa-3845-101b-84ed-08002b2ec713}')
    @commethod(3)
    def GetDisplayString(self, dispID: Int32, pBstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MapPropertyToPage(self, dispID: Int32, pClsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPredefinedStrings(self, dispID: Int32, pCaStringsOut: POINTER(win32more.Windows.Win32.System.Ole.CALPOLESTR), pCaCookiesOut: POINTER(win32more.Windows.Win32.System.Ole.CADWORD)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPredefinedValue(self, dispID: Int32, dwCookie: UInt32, pVarOut: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPersistPropertyBag(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IPersist
    _iid_ = Guid('{37d84f60-42cb-11ce-8135-00aa004bb851}')
    @commethod(4)
    def InitNew(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Load(self, pPropBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, pErrorLog: win32more.Windows.Win32.System.Com.IErrorLog) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Save(self, pPropBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag, fClearDirty: win32more.Windows.Win32.Foundation.BOOL, fSaveAllProperties: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPersistPropertyBag2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IPersist
    _iid_ = Guid('{22f55881-280b-11d0-a8a9-00a0c90c2004}')
    @commethod(4)
    def InitNew(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Load(self, pPropBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag2, pErrLog: win32more.Windows.Win32.System.Com.IErrorLog) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Save(self, pPropBag: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag2, fClearDirty: win32more.Windows.Win32.Foundation.BOOL, fSaveAllProperties: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsDirty(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPicture(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7bf80980-bf32-101a-8bbb-00aa00300cab}')
    @commethod(3)
    def get_Handle(self, pHandle: POINTER(win32more.Windows.Win32.System.Ole.OLE_HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_hPal(self, phPal: POINTER(win32more.Windows.Win32.System.Ole.OLE_HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_Type(self, pType: POINTER(win32more.Windows.Win32.System.Ole.PICTYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Width(self, pWidth: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Height(self, pHeight: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Render(self, hDC: win32more.Windows.Win32.Graphics.Gdi.HDC, x: Int32, y: Int32, cx: Int32, cy: Int32, xSrc: Int32, ySrc: Int32, cxSrc: Int32, cySrc: Int32, pRcWBounds: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def set_hPal(self, hPal: win32more.Windows.Win32.System.Ole.OLE_HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CurDC(self, phDC: POINTER(win32more.Windows.Win32.Graphics.Gdi.HDC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SelectPicture(self, hDCIn: win32more.Windows.Win32.Graphics.Gdi.HDC, phDCOut: POINTER(win32more.Windows.Win32.Graphics.Gdi.HDC), phBmpOut: POINTER(win32more.Windows.Win32.System.Ole.OLE_HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_KeepOriginalFormat(self, pKeep: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_KeepOriginalFormat(self, keep: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def PictureChanged(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SaveAsFile(self, pStream: win32more.Windows.Win32.System.Com.IStream, fSaveMemCopy: win32more.Windows.Win32.Foundation.BOOL, pCbSize: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Attributes(self, pDwAttr: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPicture2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f5185dd8-2012-4b0b-aad9-f052c6bd482b}')
    @commethod(3)
    def get_Handle(self, pHandle: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_hPal(self, phPal: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_Type(self, pType: POINTER(Int16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_Width(self, pWidth: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_Height(self, pHeight: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Render(self, hDC: win32more.Windows.Win32.Graphics.Gdi.HDC, x: Int32, y: Int32, cx: Int32, cy: Int32, xSrc: Int32, ySrc: Int32, cxSrc: Int32, cySrc: Int32, pRcWBounds: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def set_hPal(self, hPal: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CurDC(self, phDC: POINTER(win32more.Windows.Win32.Graphics.Gdi.HDC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SelectPicture(self, hDCIn: win32more.Windows.Win32.Graphics.Gdi.HDC, phDCOut: POINTER(win32more.Windows.Win32.Graphics.Gdi.HDC), phBmpOut: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_KeepOriginalFormat(self, pKeep: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_KeepOriginalFormat(self, keep: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def PictureChanged(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SaveAsFile(self, pStream: win32more.Windows.Win32.System.Com.IStream, fSaveMemCopy: win32more.Windows.Win32.Foundation.BOOL, pCbSize: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Attributes(self, pDwAttr: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPictureDisp(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{7bf80981-bf32-101a-8bbb-00aa00300cab}')
class IPointerInactive(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{55980ba0-35aa-11cf-b671-00aa004cd6d8}')
    @commethod(3)
    def GetActivationPolicy(self, pdwPolicy: POINTER(win32more.Windows.Win32.System.Ole.POINTERINACTIVE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnInactiveMouseMove(self, pRectBounds: POINTER(win32more.Windows.Win32.Foundation.RECT), x: Int32, y: Int32, grfKeyState: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnInactiveSetCursor(self, pRectBounds: POINTER(win32more.Windows.Win32.Foundation.RECT), x: Int32, y: Int32, dwMouseMsg: UInt32, fSetAlways: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPrint(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b722bcc9-4e68-101b-a2bc-00aa00404770}')
    @commethod(3)
    def SetInitialPageNum(self, nFirstPage: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPageInfo(self, pnFirstPage: POINTER(Int32), pcPages: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Print(self, grfFlags: UInt32, pptd: POINTER(POINTER(win32more.Windows.Win32.System.Com.DVTARGETDEVICE)), ppPageSet: POINTER(POINTER(win32more.Windows.Win32.System.Ole.PAGESET)), pstgmOptions: POINTER(win32more.Windows.Win32.System.Com.STGMEDIUM), pcallback: win32more.Windows.Win32.System.Ole.IContinueCallback, nFirstPage: Int32, pcPagesPrinted: POINTER(Int32), pnLastPage: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertyNotifySink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9bfbbc02-eff1-101a-84ed-00aa00341d07}')
    @commethod(3)
    def OnChanged(self, dispID: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnRequestEdit(self, dispID: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertyPage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b196b28d-bab4-101a-b69c-00aa00341d07}')
    @commethod(3)
    def SetPageSite(self, pPageSite: win32more.Windows.Win32.System.Ole.IPropertyPageSite) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Activate(self, hWndParent: win32more.Windows.Win32.Foundation.HWND, pRect: POINTER(win32more.Windows.Win32.Foundation.RECT), bModal: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Deactivate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPageInfo(self, pPageInfo: POINTER(win32more.Windows.Win32.System.Ole.PROPPAGEINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetObjects(self, cObjects: UInt32, ppUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Show(self, nCmdShow: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Move(self, pRect: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IsPageDirty(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Apply(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Help(self, pszHelpDir: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def TranslateAccelerator(self, pMsg: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.MSG)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertyPage2(ComPtr):
    extends: win32more.Windows.Win32.System.Ole.IPropertyPage
    _iid_ = Guid('{01e44665-24ac-101b-84ed-08002b2ec713}')
    @commethod(14)
    def EditProperty(self, dispID: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertyPageSite(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b196b28c-bab4-101a-b69c-00aa00341d07}')
    @commethod(3)
    def OnStatusChange(self, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLocaleID(self, pLocaleID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPageContainer(self, ppUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def TranslateAccelerator(self, pMsg: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.MSG)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProtectFocus(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d81f90a3-8156-44f7-ad28-5abb87003274}')
    @commethod(3)
    def AllowFocusChange(self, pfAllow: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProtectedModeMenuServices(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{73c105ee-9dff-4a07-b83c-7eff290c266e}')
    @commethod(3)
    def CreateMenu(self, phMenu: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LoadMenu(self, pszModuleName: win32more.Windows.Win32.Foundation.PWSTR, pszMenuName: win32more.Windows.Win32.Foundation.PWSTR, phMenu: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def LoadMenuID(self, pszModuleName: win32more.Windows.Win32.Foundation.PWSTR, wResourceID: UInt16, phMenu: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProvideClassInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b196b283-bab4-101a-b69c-00aa00341d07}')
    @commethod(3)
    def GetClassInfo(self, ppTI: POINTER(win32more.Windows.Win32.System.Com.ITypeInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProvideClassInfo2(ComPtr):
    extends: win32more.Windows.Win32.System.Ole.IProvideClassInfo
    _iid_ = Guid('{a6bc3ac0-dbaa-11ce-9de3-00aa004bb851}')
    @commethod(4)
    def GetGUID(self, dwGuidKind: UInt32, pGUID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProvideMultipleClassInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Ole.IProvideClassInfo2
    _iid_ = Guid('{a7aba9c1-8983-11cf-8f20-00805f2cd064}')
    @commethod(5)
    def GetMultiTypeInfoCount(self, pcti: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetInfoOfIndex(self, iti: UInt32, dwFlags: win32more.Windows.Win32.System.Ole.MULTICLASSINFO_FLAGS, pptiCoClass: POINTER(win32more.Windows.Win32.System.Com.ITypeInfo), pdwTIFlags: POINTER(UInt32), pcdispidReserved: POINTER(UInt32), piidPrimary: POINTER(Guid), piidSource: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProvideRuntimeContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{10e2414a-ec59-49d2-bc51-5add2c36febc}')
    @commethod(3)
    def GetCurrentSourceContext(self, pdwContext: POINTER(UIntPtr), pfExecutingGlobalCode: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IQuickActivate(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cf51ed10-62fe-11cf-bf86-00a0c9034836}')
    @commethod(3)
    def QuickActivate(self, pQaContainer: POINTER(win32more.Windows.Win32.System.Ole.QACONTAINER), pQaControl: POINTER(win32more.Windows.Win32.System.Ole.QACONTROL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetContentExtent(self, pSizel: POINTER(win32more.Windows.Win32.Foundation.SIZE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetContentExtent(self, pSizel: POINTER(win32more.Windows.Win32.Foundation.SIZE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRecordInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000002f-0000-0000-c000-000000000046}')
    @commethod(3)
    def RecordInit(self, pvNew: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RecordClear(self, pvExisting: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RecordCopy(self, pvExisting: VoidPtr, pvNew: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetGuid(self, pguid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetName(self, pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSize(self, pcbSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetTypeInfo(self, ppTypeInfo: POINTER(win32more.Windows.Win32.System.Com.ITypeInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetField(self, pvData: VoidPtr, szFieldName: win32more.Windows.Win32.Foundation.PWSTR, pvarField: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetFieldNoCopy(self, pvData: VoidPtr, szFieldName: win32more.Windows.Win32.Foundation.PWSTR, pvarField: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), ppvDataCArray: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def PutField(self, wFlags: UInt32, pvData: VoidPtr, szFieldName: win32more.Windows.Win32.Foundation.PWSTR, pvarField: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def PutFieldNoCopy(self, wFlags: UInt32, pvData: VoidPtr, szFieldName: win32more.Windows.Win32.Foundation.PWSTR, pvarField: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetFieldNames(self, pcNames: POINTER(UInt32), rgBstrNames: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def IsMatchingType(self, pRecordInfo: win32more.Windows.Win32.System.Ole.IRecordInfo) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(16)
    def RecordCreate(self) -> VoidPtr: ...
    @commethod(17)
    def RecordCreateCopy(self, pvSource: VoidPtr, ppvDest: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def RecordDestroy(self, pvRecord: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISimpleFrameSite(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{742b0e01-14e6-101b-914e-00aa00300cab}')
    @commethod(3)
    def PreMessageFilter(self, hWnd: win32more.Windows.Win32.Foundation.HWND, msg: UInt32, wp: win32more.Windows.Win32.Foundation.WPARAM, lp: win32more.Windows.Win32.Foundation.LPARAM, plResult: POINTER(win32more.Windows.Win32.Foundation.LRESULT), pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PostMessageFilter(self, hWnd: win32more.Windows.Win32.Foundation.HWND, msg: UInt32, wp: win32more.Windows.Win32.Foundation.WPARAM, lp: win32more.Windows.Win32.Foundation.LPARAM, plResult: POINTER(win32more.Windows.Win32.Foundation.LRESULT), dwCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISpecifyPropertyPages(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b196b28b-bab4-101a-b69c-00aa00341d07}')
    @commethod(3)
    def GetPages(self, pPages: POINTER(win32more.Windows.Win32.System.Ole.CAUUID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITypeChangeEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00020410-0000-0000-c000-000000000046}')
    @commethod(3)
    def RequestTypeChange(self, changeKind: win32more.Windows.Win32.System.Ole.CHANGEKIND, pTInfoBefore: win32more.Windows.Win32.System.Com.ITypeInfo, pStrName: win32more.Windows.Win32.Foundation.PWSTR, pfCancel: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AfterTypeChange(self, changeKind: win32more.Windows.Win32.System.Ole.CHANGEKIND, pTInfoAfter: win32more.Windows.Win32.System.Com.ITypeInfo, pStrName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITypeFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000002e-0000-0000-c000-000000000046}')
    @commethod(3)
    def CreateFromTypeInfo(self, pTypeInfo: win32more.Windows.Win32.System.Com.ITypeInfo, riid: POINTER(Guid), ppv: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITypeMarshal(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000002d-0000-0000-c000-000000000046}')
    @commethod(3)
    def Size(self, pvType: VoidPtr, dwDestContext: UInt32, pvDestContext: VoidPtr, pSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Marshal(self, pvType: VoidPtr, dwDestContext: UInt32, pvDestContext: VoidPtr, cbBufferLength: UInt32, pBuffer: POINTER(Byte), pcbWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Unmarshal(self, pvType: VoidPtr, dwFlags: UInt32, cbBufferLength: UInt32, pBuffer: POINTER(Byte), pcbRead: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Free(self, pvType: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVBFormat(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9849fd60-3768-101b-8d72-ae6164ffe3cf}')
    @commethod(3)
    def Format(self, vData: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), bstrFormat: win32more.Windows.Win32.Foundation.BSTR, lpBuffer: VoidPtr, cb: UInt16, lcid: Int32, sFirstDayOfWeek: Int16, sFirstWeekOfYear: UInt16, rcb: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVBGetControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{40a050a0-3c31-101b-a82e-08002b2b2337}')
    @commethod(3)
    def EnumControls(self, dwOleContF: UInt32, dwWhich: win32more.Windows.Win32.System.Ole.ENUM_CONTROLS_WHICH_FLAGS, ppenumUnk: POINTER(win32more.Windows.Win32.System.Com.IEnumUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVariantChangeType(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a6ef9862-c720-11d0-9337-00a0c90dcaa9}')
    @commethod(3)
    def ChangeType(self, pvarDst: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarSrc: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), lcid: UInt32, vtNew: win32more.Windows.Win32.System.Variant.VARENUM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IViewObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0000010d-0000-0000-c000-000000000046}')
    @commethod(3)
    def Draw(self, dwDrawAspect: win32more.Windows.Win32.System.Com.DVASPECT, lindex: Int32, pvAspect: VoidPtr, ptd: POINTER(win32more.Windows.Win32.System.Com.DVTARGETDEVICE), hdcTargetDev: win32more.Windows.Win32.Graphics.Gdi.HDC, hdcDraw: win32more.Windows.Win32.Graphics.Gdi.HDC, lprcBounds: POINTER(win32more.Windows.Win32.Foundation.RECTL), lprcWBounds: POINTER(win32more.Windows.Win32.Foundation.RECTL), pfnContinue: IntPtr, dwContinue: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetColorSet(self, dwDrawAspect: win32more.Windows.Win32.System.Com.DVASPECT, lindex: Int32, pvAspect: VoidPtr, ptd: POINTER(win32more.Windows.Win32.System.Com.DVTARGETDEVICE), hicTargetDev: win32more.Windows.Win32.Graphics.Gdi.HDC, ppColorSet: POINTER(POINTER(win32more.Windows.Win32.Graphics.Gdi.LOGPALETTE))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Freeze(self, dwDrawAspect: win32more.Windows.Win32.System.Com.DVASPECT, lindex: Int32, pvAspect: VoidPtr, pdwFreeze: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Unfreeze(self, dwFreeze: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetAdvise(self, aspects: win32more.Windows.Win32.System.Com.DVASPECT, advf: UInt32, pAdvSink: win32more.Windows.Win32.System.Com.IAdviseSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetAdvise(self, pAspects: POINTER(UInt32), pAdvf: POINTER(UInt32), ppAdvSink: POINTER(win32more.Windows.Win32.System.Com.IAdviseSink)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IViewObject2(ComPtr):
    extends: win32more.Windows.Win32.System.Ole.IViewObject
    _iid_ = Guid('{00000127-0000-0000-c000-000000000046}')
    @commethod(9)
    def GetExtent(self, dwDrawAspect: win32more.Windows.Win32.System.Com.DVASPECT, lindex: Int32, ptd: POINTER(win32more.Windows.Win32.System.Com.DVTARGETDEVICE), lpsizel: POINTER(win32more.Windows.Win32.Foundation.SIZE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IViewObjectEx(ComPtr):
    extends: win32more.Windows.Win32.System.Ole.IViewObject2
    _iid_ = Guid('{3af24292-0c96-11ce-a0cf-00aa00600ab8}')
    @commethod(10)
    def GetRect(self, dwAspect: UInt32, pRect: POINTER(win32more.Windows.Win32.Foundation.RECTL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetViewStatus(self, pdwStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def QueryHitPoint(self, dwAspect: UInt32, pRectBounds: POINTER(win32more.Windows.Win32.Foundation.RECT), ptlLoc: win32more.Windows.Win32.Foundation.POINT, lCloseHint: Int32, pHitResult: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def QueryHitRect(self, dwAspect: UInt32, pRectBounds: POINTER(win32more.Windows.Win32.Foundation.RECT), pRectLoc: POINTER(win32more.Windows.Win32.Foundation.RECT), lCloseHint: Int32, pHitResult: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetNaturalExtent(self, dwAspect: win32more.Windows.Win32.System.Com.DVASPECT, lindex: Int32, ptd: POINTER(win32more.Windows.Win32.System.Com.DVTARGETDEVICE), hicTargetDev: win32more.Windows.Win32.Graphics.Gdi.HDC, pExtentInfo: POINTER(win32more.Windows.Win32.System.Ole.DVEXTENTINFO), pSizel: POINTER(win32more.Windows.Win32.Foundation.SIZE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IZoomEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{41b68150-904c-4e17-a0ba-a438182e359d}')
    @commethod(3)
    def OnZoomPercentChanged(self, ulZoomPercent: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
KEYMODIFIERS = UInt32
KEYMOD_SHIFT: win32more.Windows.Win32.System.Ole.KEYMODIFIERS = 1
KEYMOD_CONTROL: win32more.Windows.Win32.System.Ole.KEYMODIFIERS = 2
KEYMOD_ALT: win32more.Windows.Win32.System.Ole.KEYMODIFIERS = 4
LIBFLAGS = Int32
LIBFLAG_FRESTRICTED: win32more.Windows.Win32.System.Ole.LIBFLAGS = 1
LIBFLAG_FCONTROL: win32more.Windows.Win32.System.Ole.LIBFLAGS = 2
LIBFLAG_FHIDDEN: win32more.Windows.Win32.System.Ole.LIBFLAGS = 4
LIBFLAG_FHASDISKIMAGE: win32more.Windows.Win32.System.Ole.LIBFLAGS = 8
class LICINFO(Structure):
    cbLicInfo: Int32
    fRuntimeKeyAvail: win32more.Windows.Win32.Foundation.BOOL
    fLicVerified: win32more.Windows.Win32.Foundation.BOOL
LOAD_PICTURE_FLAGS = UInt32
LP_DEFAULT: win32more.Windows.Win32.System.Ole.LOAD_PICTURE_FLAGS = 0
LP_MONOCHROME: win32more.Windows.Win32.System.Ole.LOAD_PICTURE_FLAGS = 1
LP_VGACOLOR: win32more.Windows.Win32.System.Ole.LOAD_PICTURE_FLAGS = 2
LP_COLOR: win32more.Windows.Win32.System.Ole.LOAD_PICTURE_FLAGS = 4
@winfunctype_pointer
def LPFNOLEUIHOOK(param0: win32more.Windows.Win32.Foundation.HWND, param1: UInt32, param2: win32more.Windows.Win32.Foundation.WPARAM, param3: win32more.Windows.Win32.Foundation.LPARAM) -> UInt32: ...
MEDIAPLAYBACK_STATE = Int32
MEDIAPLAYBACK_RESUME: win32more.Windows.Win32.System.Ole.MEDIAPLAYBACK_STATE = 0
MEDIAPLAYBACK_PAUSE: win32more.Windows.Win32.System.Ole.MEDIAPLAYBACK_STATE = 1
MEDIAPLAYBACK_PAUSE_AND_SUSPEND: win32more.Windows.Win32.System.Ole.MEDIAPLAYBACK_STATE = 2
MEDIAPLAYBACK_RESUME_FROM_SUSPEND: win32more.Windows.Win32.System.Ole.MEDIAPLAYBACK_STATE = 3
class METHODDATA(Structure):
    szName: win32more.Windows.Win32.Foundation.PWSTR
    ppdata: POINTER(win32more.Windows.Win32.System.Ole.PARAMDATA)
    dispid: Int32
    iMeth: UInt32
    cc: win32more.Windows.Win32.System.Com.CALLCONV
    cArgs: UInt32
    wFlags: UInt16
    vtReturn: win32more.Windows.Win32.System.Variant.VARENUM
MULTICLASSINFO_FLAGS = UInt32
MULTICLASSINFO_GETTYPEINFO: win32more.Windows.Win32.System.Ole.MULTICLASSINFO_FLAGS = 1
MULTICLASSINFO_GETNUMRESERVEDDISPIDS: win32more.Windows.Win32.System.Ole.MULTICLASSINFO_FLAGS = 2
MULTICLASSINFO_GETIIDPRIMARY: win32more.Windows.Win32.System.Ole.MULTICLASSINFO_FLAGS = 4
MULTICLASSINFO_GETIIDSOURCE: win32more.Windows.Win32.System.Ole.MULTICLASSINFO_FLAGS = 8
class NUMPARSE(Structure):
    cDig: Int32
    dwInFlags: win32more.Windows.Win32.System.Ole.NUMPARSE_FLAGS
    dwOutFlags: win32more.Windows.Win32.System.Ole.NUMPARSE_FLAGS
    cchUsed: Int32
    nBaseShift: Int32
    nPwr10: Int32
NUMPARSE_FLAGS = UInt32
NUMPRS_LEADING_WHITE: win32more.Windows.Win32.System.Ole.NUMPARSE_FLAGS = 1
NUMPRS_TRAILING_WHITE: win32more.Windows.Win32.System.Ole.NUMPARSE_FLAGS = 2
NUMPRS_LEADING_PLUS: win32more.Windows.Win32.System.Ole.NUMPARSE_FLAGS = 4
NUMPRS_TRAILING_PLUS: win32more.Windows.Win32.System.Ole.NUMPARSE_FLAGS = 8
NUMPRS_LEADING_MINUS: win32more.Windows.Win32.System.Ole.NUMPARSE_FLAGS = 16
NUMPRS_TRAILING_MINUS: win32more.Windows.Win32.System.Ole.NUMPARSE_FLAGS = 32
NUMPRS_HEX_OCT: win32more.Windows.Win32.System.Ole.NUMPARSE_FLAGS = 64
NUMPRS_PARENS: win32more.Windows.Win32.System.Ole.NUMPARSE_FLAGS = 128
NUMPRS_DECIMAL: win32more.Windows.Win32.System.Ole.NUMPARSE_FLAGS = 256
NUMPRS_THOUSANDS: win32more.Windows.Win32.System.Ole.NUMPARSE_FLAGS = 512
NUMPRS_CURRENCY: win32more.Windows.Win32.System.Ole.NUMPARSE_FLAGS = 1024
NUMPRS_EXPONENT: win32more.Windows.Win32.System.Ole.NUMPARSE_FLAGS = 2048
NUMPRS_USE_ALL: win32more.Windows.Win32.System.Ole.NUMPARSE_FLAGS = 4096
NUMPRS_STD: win32more.Windows.Win32.System.Ole.NUMPARSE_FLAGS = 8191
NUMPRS_NEG: win32more.Windows.Win32.System.Ole.NUMPARSE_FLAGS = 65536
NUMPRS_INEXACT: win32more.Windows.Win32.System.Ole.NUMPARSE_FLAGS = 131072
class OBJECTDESCRIPTOR(Structure):
    cbSize: UInt32
    clsid: Guid
    dwDrawAspect: UInt32
    sizel: win32more.Windows.Win32.Foundation.SIZE
    pointl: win32more.Windows.Win32.Foundation.POINTL
    dwStatus: UInt32
    dwFullUserTypeName: UInt32
    dwSrcOfCopy: UInt32
OBJECT_PROPERTIES_FLAGS = UInt32
OPF_OBJECTISLINK: win32more.Windows.Win32.System.Ole.OBJECT_PROPERTIES_FLAGS = 1
OPF_NOFILLDEFAULT: win32more.Windows.Win32.System.Ole.OBJECT_PROPERTIES_FLAGS = 2
OPF_SHOWHELP: win32more.Windows.Win32.System.Ole.OBJECT_PROPERTIES_FLAGS = 4
OPF_DISABLECONVERT: win32more.Windows.Win32.System.Ole.OBJECT_PROPERTIES_FLAGS = 8
class OCPFIPARAMS(Structure):
    cbStructSize: UInt32
    hWndOwner: win32more.Windows.Win32.Foundation.HWND
    x: Int32
    y: Int32
    lpszCaption: win32more.Windows.Win32.Foundation.PWSTR
    cObjects: UInt32
    lplpUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)
    cPages: UInt32
    lpPages: POINTER(Guid)
    lcid: UInt32
    dispidInitialProperty: Int32
OLECLOSE = Int32
OLECLOSE_SAVEIFDIRTY: win32more.Windows.Win32.System.Ole.OLECLOSE = 0
OLECLOSE_NOSAVE: win32more.Windows.Win32.System.Ole.OLECLOSE = 1
OLECLOSE_PROMPTSAVE: win32more.Windows.Win32.System.Ole.OLECLOSE = 2
class OLECMD(Structure):
    cmdID: UInt32
    cmdf: UInt32
OLECMDEXECOPT = Int32
OLECMDEXECOPT_DODEFAULT: win32more.Windows.Win32.System.Ole.OLECMDEXECOPT = 0
OLECMDEXECOPT_PROMPTUSER: win32more.Windows.Win32.System.Ole.OLECMDEXECOPT = 1
OLECMDEXECOPT_DONTPROMPTUSER: win32more.Windows.Win32.System.Ole.OLECMDEXECOPT = 2
OLECMDEXECOPT_SHOWHELP: win32more.Windows.Win32.System.Ole.OLECMDEXECOPT = 3
OLECMDF = Int32
OLECMDF_SUPPORTED: win32more.Windows.Win32.System.Ole.OLECMDF = 1
OLECMDF_ENABLED: win32more.Windows.Win32.System.Ole.OLECMDF = 2
OLECMDF_LATCHED: win32more.Windows.Win32.System.Ole.OLECMDF = 4
OLECMDF_NINCHED: win32more.Windows.Win32.System.Ole.OLECMDF = 8
OLECMDF_INVISIBLE: win32more.Windows.Win32.System.Ole.OLECMDF = 16
OLECMDF_DEFHIDEONCTXTMENU: win32more.Windows.Win32.System.Ole.OLECMDF = 32
OLECMDID = Int32
OLECMDID_OPEN: win32more.Windows.Win32.System.Ole.OLECMDID = 1
OLECMDID_NEW: win32more.Windows.Win32.System.Ole.OLECMDID = 2
OLECMDID_SAVE: win32more.Windows.Win32.System.Ole.OLECMDID = 3
OLECMDID_SAVEAS: win32more.Windows.Win32.System.Ole.OLECMDID = 4
OLECMDID_SAVECOPYAS: win32more.Windows.Win32.System.Ole.OLECMDID = 5
OLECMDID_PRINT: win32more.Windows.Win32.System.Ole.OLECMDID = 6
OLECMDID_PRINTPREVIEW: win32more.Windows.Win32.System.Ole.OLECMDID = 7
OLECMDID_PAGESETUP: win32more.Windows.Win32.System.Ole.OLECMDID = 8
OLECMDID_SPELL: win32more.Windows.Win32.System.Ole.OLECMDID = 9
OLECMDID_PROPERTIES: win32more.Windows.Win32.System.Ole.OLECMDID = 10
OLECMDID_CUT: win32more.Windows.Win32.System.Ole.OLECMDID = 11
OLECMDID_COPY: win32more.Windows.Win32.System.Ole.OLECMDID = 12
OLECMDID_PASTE: win32more.Windows.Win32.System.Ole.OLECMDID = 13
OLECMDID_PASTESPECIAL: win32more.Windows.Win32.System.Ole.OLECMDID = 14
OLECMDID_UNDO: win32more.Windows.Win32.System.Ole.OLECMDID = 15
OLECMDID_REDO: win32more.Windows.Win32.System.Ole.OLECMDID = 16
OLECMDID_SELECTALL: win32more.Windows.Win32.System.Ole.OLECMDID = 17
OLECMDID_CLEARSELECTION: win32more.Windows.Win32.System.Ole.OLECMDID = 18
OLECMDID_ZOOM: win32more.Windows.Win32.System.Ole.OLECMDID = 19
OLECMDID_GETZOOMRANGE: win32more.Windows.Win32.System.Ole.OLECMDID = 20
OLECMDID_UPDATECOMMANDS: win32more.Windows.Win32.System.Ole.OLECMDID = 21
OLECMDID_REFRESH: win32more.Windows.Win32.System.Ole.OLECMDID = 22
OLECMDID_STOP: win32more.Windows.Win32.System.Ole.OLECMDID = 23
OLECMDID_HIDETOOLBARS: win32more.Windows.Win32.System.Ole.OLECMDID = 24
OLECMDID_SETPROGRESSMAX: win32more.Windows.Win32.System.Ole.OLECMDID = 25
OLECMDID_SETPROGRESSPOS: win32more.Windows.Win32.System.Ole.OLECMDID = 26
OLECMDID_SETPROGRESSTEXT: win32more.Windows.Win32.System.Ole.OLECMDID = 27
OLECMDID_SETTITLE: win32more.Windows.Win32.System.Ole.OLECMDID = 28
OLECMDID_SETDOWNLOADSTATE: win32more.Windows.Win32.System.Ole.OLECMDID = 29
OLECMDID_STOPDOWNLOAD: win32more.Windows.Win32.System.Ole.OLECMDID = 30
OLECMDID_ONTOOLBARACTIVATED: win32more.Windows.Win32.System.Ole.OLECMDID = 31
OLECMDID_FIND: win32more.Windows.Win32.System.Ole.OLECMDID = 32
OLECMDID_DELETE: win32more.Windows.Win32.System.Ole.OLECMDID = 33
OLECMDID_HTTPEQUIV: win32more.Windows.Win32.System.Ole.OLECMDID = 34
OLECMDID_HTTPEQUIV_DONE: win32more.Windows.Win32.System.Ole.OLECMDID = 35
OLECMDID_ENABLE_INTERACTION: win32more.Windows.Win32.System.Ole.OLECMDID = 36
OLECMDID_ONUNLOAD: win32more.Windows.Win32.System.Ole.OLECMDID = 37
OLECMDID_PROPERTYBAG2: win32more.Windows.Win32.System.Ole.OLECMDID = 38
OLECMDID_PREREFRESH: win32more.Windows.Win32.System.Ole.OLECMDID = 39
OLECMDID_SHOWSCRIPTERROR: win32more.Windows.Win32.System.Ole.OLECMDID = 40
OLECMDID_SHOWMESSAGE: win32more.Windows.Win32.System.Ole.OLECMDID = 41
OLECMDID_SHOWFIND: win32more.Windows.Win32.System.Ole.OLECMDID = 42
OLECMDID_SHOWPAGESETUP: win32more.Windows.Win32.System.Ole.OLECMDID = 43
OLECMDID_SHOWPRINT: win32more.Windows.Win32.System.Ole.OLECMDID = 44
OLECMDID_CLOSE: win32more.Windows.Win32.System.Ole.OLECMDID = 45
OLECMDID_ALLOWUILESSSAVEAS: win32more.Windows.Win32.System.Ole.OLECMDID = 46
OLECMDID_DONTDOWNLOADCSS: win32more.Windows.Win32.System.Ole.OLECMDID = 47
OLECMDID_UPDATEPAGESTATUS: win32more.Windows.Win32.System.Ole.OLECMDID = 48
OLECMDID_PRINT2: win32more.Windows.Win32.System.Ole.OLECMDID = 49
OLECMDID_PRINTPREVIEW2: win32more.Windows.Win32.System.Ole.OLECMDID = 50
OLECMDID_SETPRINTTEMPLATE: win32more.Windows.Win32.System.Ole.OLECMDID = 51
OLECMDID_GETPRINTTEMPLATE: win32more.Windows.Win32.System.Ole.OLECMDID = 52
OLECMDID_PAGEACTIONBLOCKED: win32more.Windows.Win32.System.Ole.OLECMDID = 55
OLECMDID_PAGEACTIONUIQUERY: win32more.Windows.Win32.System.Ole.OLECMDID = 56
OLECMDID_FOCUSVIEWCONTROLS: win32more.Windows.Win32.System.Ole.OLECMDID = 57
OLECMDID_FOCUSVIEWCONTROLSQUERY: win32more.Windows.Win32.System.Ole.OLECMDID = 58
OLECMDID_SHOWPAGEACTIONMENU: win32more.Windows.Win32.System.Ole.OLECMDID = 59
OLECMDID_ADDTRAVELENTRY: win32more.Windows.Win32.System.Ole.OLECMDID = 60
OLECMDID_UPDATETRAVELENTRY: win32more.Windows.Win32.System.Ole.OLECMDID = 61
OLECMDID_UPDATEBACKFORWARDSTATE: win32more.Windows.Win32.System.Ole.OLECMDID = 62
OLECMDID_OPTICAL_ZOOM: win32more.Windows.Win32.System.Ole.OLECMDID = 63
OLECMDID_OPTICAL_GETZOOMRANGE: win32more.Windows.Win32.System.Ole.OLECMDID = 64
OLECMDID_WINDOWSTATECHANGED: win32more.Windows.Win32.System.Ole.OLECMDID = 65
OLECMDID_ACTIVEXINSTALLSCOPE: win32more.Windows.Win32.System.Ole.OLECMDID = 66
OLECMDID_UPDATETRAVELENTRY_DATARECOVERY: win32more.Windows.Win32.System.Ole.OLECMDID = 67
OLECMDID_SHOWTASKDLG: win32more.Windows.Win32.System.Ole.OLECMDID = 68
OLECMDID_POPSTATEEVENT: win32more.Windows.Win32.System.Ole.OLECMDID = 69
OLECMDID_VIEWPORT_MODE: win32more.Windows.Win32.System.Ole.OLECMDID = 70
OLECMDID_LAYOUT_VIEWPORT_WIDTH: win32more.Windows.Win32.System.Ole.OLECMDID = 71
OLECMDID_VISUAL_VIEWPORT_EXCLUDE_BOTTOM: win32more.Windows.Win32.System.Ole.OLECMDID = 72
OLECMDID_USER_OPTICAL_ZOOM: win32more.Windows.Win32.System.Ole.OLECMDID = 73
OLECMDID_PAGEAVAILABLE: win32more.Windows.Win32.System.Ole.OLECMDID = 74
OLECMDID_GETUSERSCALABLE: win32more.Windows.Win32.System.Ole.OLECMDID = 75
OLECMDID_UPDATE_CARET: win32more.Windows.Win32.System.Ole.OLECMDID = 76
OLECMDID_ENABLE_VISIBILITY: win32more.Windows.Win32.System.Ole.OLECMDID = 77
OLECMDID_MEDIA_PLAYBACK: win32more.Windows.Win32.System.Ole.OLECMDID = 78
OLECMDID_SETFAVICON: win32more.Windows.Win32.System.Ole.OLECMDID = 79
OLECMDID_SET_HOST_FULLSCREENMODE: win32more.Windows.Win32.System.Ole.OLECMDID = 80
OLECMDID_EXITFULLSCREEN: win32more.Windows.Win32.System.Ole.OLECMDID = 81
OLECMDID_SCROLLCOMPLETE: win32more.Windows.Win32.System.Ole.OLECMDID = 82
OLECMDID_ONBEFOREUNLOAD: win32more.Windows.Win32.System.Ole.OLECMDID = 83
OLECMDID_SHOWMESSAGE_BLOCKABLE: win32more.Windows.Win32.System.Ole.OLECMDID = 84
OLECMDID_SHOWTASKDLG_BLOCKABLE: win32more.Windows.Win32.System.Ole.OLECMDID = 85
OLECMDID_BROWSERSTATEFLAG = Int32
OLECMDIDF_BROWSERSTATE_EXTENSIONSOFF: win32more.Windows.Win32.System.Ole.OLECMDID_BROWSERSTATEFLAG = 1
OLECMDIDF_BROWSERSTATE_IESECURITY: win32more.Windows.Win32.System.Ole.OLECMDID_BROWSERSTATEFLAG = 2
OLECMDIDF_BROWSERSTATE_PROTECTEDMODE_OFF: win32more.Windows.Win32.System.Ole.OLECMDID_BROWSERSTATEFLAG = 4
OLECMDIDF_BROWSERSTATE_RESET: win32more.Windows.Win32.System.Ole.OLECMDID_BROWSERSTATEFLAG = 8
OLECMDIDF_BROWSERSTATE_REQUIRESACTIVEX: win32more.Windows.Win32.System.Ole.OLECMDID_BROWSERSTATEFLAG = 16
OLECMDIDF_BROWSERSTATE_DESKTOPHTMLDIALOG: win32more.Windows.Win32.System.Ole.OLECMDID_BROWSERSTATEFLAG = 32
OLECMDIDF_BROWSERSTATE_BLOCKEDVERSION: win32more.Windows.Win32.System.Ole.OLECMDID_BROWSERSTATEFLAG = 64
OLECMDID_OPTICAL_ZOOMFLAG = Int32
OLECMDIDF_OPTICAL_ZOOM_NOPERSIST: win32more.Windows.Win32.System.Ole.OLECMDID_OPTICAL_ZOOMFLAG = 1
OLECMDIDF_OPTICAL_ZOOM_NOLAYOUT: win32more.Windows.Win32.System.Ole.OLECMDID_OPTICAL_ZOOMFLAG = 16
OLECMDIDF_OPTICAL_ZOOM_NOTRANSIENT: win32more.Windows.Win32.System.Ole.OLECMDID_OPTICAL_ZOOMFLAG = 32
OLECMDIDF_OPTICAL_ZOOM_RELOADFORNEWTAB: win32more.Windows.Win32.System.Ole.OLECMDID_OPTICAL_ZOOMFLAG = 64
OLECMDID_PAGEACTIONFLAG = Int32
OLECMDIDF_PAGEACTION_FILEDOWNLOAD: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 1
OLECMDIDF_PAGEACTION_ACTIVEXINSTALL: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 2
OLECMDIDF_PAGEACTION_ACTIVEXTRUSTFAIL: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 4
OLECMDIDF_PAGEACTION_ACTIVEXUSERDISABLE: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 8
OLECMDIDF_PAGEACTION_ACTIVEXDISALLOW: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 16
OLECMDIDF_PAGEACTION_ACTIVEXUNSAFE: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 32
OLECMDIDF_PAGEACTION_POPUPWINDOW: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 64
OLECMDIDF_PAGEACTION_LOCALMACHINE: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 128
OLECMDIDF_PAGEACTION_MIMETEXTPLAIN: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 256
OLECMDIDF_PAGEACTION_SCRIPTNAVIGATE: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 512
OLECMDIDF_PAGEACTION_SCRIPTNAVIGATE_ACTIVEXINSTALL: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 512
OLECMDIDF_PAGEACTION_PROTLOCKDOWNLOCALMACHINE: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 1024
OLECMDIDF_PAGEACTION_PROTLOCKDOWNTRUSTED: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 2048
OLECMDIDF_PAGEACTION_PROTLOCKDOWNINTRANET: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 4096
OLECMDIDF_PAGEACTION_PROTLOCKDOWNINTERNET: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 8192
OLECMDIDF_PAGEACTION_PROTLOCKDOWNRESTRICTED: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 16384
OLECMDIDF_PAGEACTION_PROTLOCKDOWNDENY: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 32768
OLECMDIDF_PAGEACTION_POPUPALLOWED: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 65536
OLECMDIDF_PAGEACTION_SCRIPTPROMPT: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 131072
OLECMDIDF_PAGEACTION_ACTIVEXUSERAPPROVAL: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 262144
OLECMDIDF_PAGEACTION_MIXEDCONTENT: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 524288
OLECMDIDF_PAGEACTION_INVALID_CERT: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 1048576
OLECMDIDF_PAGEACTION_INTRANETZONEREQUEST: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 2097152
OLECMDIDF_PAGEACTION_XSSFILTERED: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 4194304
OLECMDIDF_PAGEACTION_SPOOFABLEIDNHOST: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 8388608
OLECMDIDF_PAGEACTION_ACTIVEX_EPM_INCOMPATIBLE: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 16777216
OLECMDIDF_PAGEACTION_SCRIPTNAVIGATE_ACTIVEXUSERAPPROVAL: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 33554432
OLECMDIDF_PAGEACTION_WPCBLOCKED: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 67108864
OLECMDIDF_PAGEACTION_WPCBLOCKED_ACTIVEX: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 134217728
OLECMDIDF_PAGEACTION_EXTENSION_COMPAT_BLOCKED: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 268435456
OLECMDIDF_PAGEACTION_NORESETACTIVEX: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 536870912
OLECMDIDF_PAGEACTION_GENERIC_STATE: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = 1073741824
OLECMDIDF_PAGEACTION_RESET: win32more.Windows.Win32.System.Ole.OLECMDID_PAGEACTIONFLAG = -2147483648
OLECMDID_REFRESHFLAG = Int32
OLECMDIDF_REFRESH_NORMAL: win32more.Windows.Win32.System.Ole.OLECMDID_REFRESHFLAG = 0
OLECMDIDF_REFRESH_IFEXPIRED: win32more.Windows.Win32.System.Ole.OLECMDID_REFRESHFLAG = 1
OLECMDIDF_REFRESH_CONTINUE: win32more.Windows.Win32.System.Ole.OLECMDID_REFRESHFLAG = 2
OLECMDIDF_REFRESH_COMPLETELY: win32more.Windows.Win32.System.Ole.OLECMDID_REFRESHFLAG = 3
OLECMDIDF_REFRESH_NO_CACHE: win32more.Windows.Win32.System.Ole.OLECMDID_REFRESHFLAG = 4
OLECMDIDF_REFRESH_RELOAD: win32more.Windows.Win32.System.Ole.OLECMDID_REFRESHFLAG = 5
OLECMDIDF_REFRESH_LEVELMASK: win32more.Windows.Win32.System.Ole.OLECMDID_REFRESHFLAG = 255
OLECMDIDF_REFRESH_CLEARUSERINPUT: win32more.Windows.Win32.System.Ole.OLECMDID_REFRESHFLAG = 4096
OLECMDIDF_REFRESH_PROMPTIFOFFLINE: win32more.Windows.Win32.System.Ole.OLECMDID_REFRESHFLAG = 8192
OLECMDIDF_REFRESH_THROUGHSCRIPT: win32more.Windows.Win32.System.Ole.OLECMDID_REFRESHFLAG = 16384
OLECMDIDF_REFRESH_SKIPBEFOREUNLOADEVENT: win32more.Windows.Win32.System.Ole.OLECMDID_REFRESHFLAG = 32768
OLECMDIDF_REFRESH_PAGEACTION_ACTIVEXINSTALL: win32more.Windows.Win32.System.Ole.OLECMDID_REFRESHFLAG = 65536
OLECMDIDF_REFRESH_PAGEACTION_FILEDOWNLOAD: win32more.Windows.Win32.System.Ole.OLECMDID_REFRESHFLAG = 131072
OLECMDIDF_REFRESH_PAGEACTION_LOCALMACHINE: win32more.Windows.Win32.System.Ole.OLECMDID_REFRESHFLAG = 262144
OLECMDIDF_REFRESH_PAGEACTION_POPUPWINDOW: win32more.Windows.Win32.System.Ole.OLECMDID_REFRESHFLAG = 524288
OLECMDIDF_REFRESH_PAGEACTION_PROTLOCKDOWNLOCALMACHINE: win32more.Windows.Win32.System.Ole.OLECMDID_REFRESHFLAG = 1048576
OLECMDIDF_REFRESH_PAGEACTION_PROTLOCKDOWNTRUSTED: win32more.Windows.Win32.System.Ole.OLECMDID_REFRESHFLAG = 2097152
OLECMDIDF_REFRESH_PAGEACTION_PROTLOCKDOWNINTRANET: win32more.Windows.Win32.System.Ole.OLECMDID_REFRESHFLAG = 4194304
OLECMDIDF_REFRESH_PAGEACTION_PROTLOCKDOWNINTERNET: win32more.Windows.Win32.System.Ole.OLECMDID_REFRESHFLAG = 8388608
OLECMDIDF_REFRESH_PAGEACTION_PROTLOCKDOWNRESTRICTED: win32more.Windows.Win32.System.Ole.OLECMDID_REFRESHFLAG = 16777216
OLECMDIDF_REFRESH_PAGEACTION_MIXEDCONTENT: win32more.Windows.Win32.System.Ole.OLECMDID_REFRESHFLAG = 33554432
OLECMDIDF_REFRESH_PAGEACTION_INVALID_CERT: win32more.Windows.Win32.System.Ole.OLECMDID_REFRESHFLAG = 67108864
OLECMDIDF_REFRESH_PAGEACTION_ALLOW_VERSION: win32more.Windows.Win32.System.Ole.OLECMDID_REFRESHFLAG = 134217728
OLECMDID_VIEWPORT_MODE_FLAG = Int32
OLECMDIDF_VIEWPORTMODE_FIXED_LAYOUT_WIDTH: win32more.Windows.Win32.System.Ole.OLECMDID_VIEWPORT_MODE_FLAG = 1
OLECMDIDF_VIEWPORTMODE_EXCLUDE_VISUAL_BOTTOM: win32more.Windows.Win32.System.Ole.OLECMDID_VIEWPORT_MODE_FLAG = 2
OLECMDIDF_VIEWPORTMODE_FIXED_LAYOUT_WIDTH_VALID: win32more.Windows.Win32.System.Ole.OLECMDID_VIEWPORT_MODE_FLAG = 65536
OLECMDIDF_VIEWPORTMODE_EXCLUDE_VISUAL_BOTTOM_VALID: win32more.Windows.Win32.System.Ole.OLECMDID_VIEWPORT_MODE_FLAG = 131072
OLECMDID_WINDOWSTATE_FLAG = Int32
OLECMDIDF_WINDOWSTATE_USERVISIBLE: win32more.Windows.Win32.System.Ole.OLECMDID_WINDOWSTATE_FLAG = 1
OLECMDIDF_WINDOWSTATE_ENABLED: win32more.Windows.Win32.System.Ole.OLECMDID_WINDOWSTATE_FLAG = 2
OLECMDIDF_WINDOWSTATE_USERVISIBLE_VALID: win32more.Windows.Win32.System.Ole.OLECMDID_WINDOWSTATE_FLAG = 65536
OLECMDIDF_WINDOWSTATE_ENABLED_VALID: win32more.Windows.Win32.System.Ole.OLECMDID_WINDOWSTATE_FLAG = 131072
class OLECMDTEXT(Structure):
    cmdtextf: UInt32
    cwActual: UInt32
    cwBuf: UInt32
    rgwz: Char * 1
OLECMDTEXTF = Int32
OLECMDTEXTF_NONE: win32more.Windows.Win32.System.Ole.OLECMDTEXTF = 0
OLECMDTEXTF_NAME: win32more.Windows.Win32.System.Ole.OLECMDTEXTF = 1
OLECMDTEXTF_STATUS: win32more.Windows.Win32.System.Ole.OLECMDTEXTF = 2
OLECONTF = Int32
OLECONTF_EMBEDDINGS: win32more.Windows.Win32.System.Ole.OLECONTF = 1
OLECONTF_LINKS: win32more.Windows.Win32.System.Ole.OLECONTF = 2
OLECONTF_OTHERS: win32more.Windows.Win32.System.Ole.OLECONTF = 4
OLECONTF_ONLYUSER: win32more.Windows.Win32.System.Ole.OLECONTF = 8
OLECONTF_ONLYIFRUNNING: win32more.Windows.Win32.System.Ole.OLECONTF = 16
OLECREATE = UInt32
OLECREATE_ZERO: win32more.Windows.Win32.System.Ole.OLECREATE = 0
OLECREATE_LEAVERUNNING: win32more.Windows.Win32.System.Ole.OLECREATE = 1
OLEDCFLAGS = Int32
OLEDC_NODRAW: win32more.Windows.Win32.System.Ole.OLEDCFLAGS = 1
OLEDC_PAINTBKGND: win32more.Windows.Win32.System.Ole.OLEDCFLAGS = 2
OLEDC_OFFSCREEN: win32more.Windows.Win32.System.Ole.OLEDCFLAGS = 4
OLEGETMONIKER = Int32
OLEGETMONIKER_ONLYIFTHERE: win32more.Windows.Win32.System.Ole.OLEGETMONIKER = 1
OLEGETMONIKER_FORCEASSIGN: win32more.Windows.Win32.System.Ole.OLEGETMONIKER = 2
OLEGETMONIKER_UNASSIGN: win32more.Windows.Win32.System.Ole.OLEGETMONIKER = 3
OLEGETMONIKER_TEMPFORUSER: win32more.Windows.Win32.System.Ole.OLEGETMONIKER = 4
class OLEINPLACEFRAMEINFO(Structure):
    cb: UInt32
    fMDIApp: win32more.Windows.Win32.Foundation.BOOL
    hwndFrame: win32more.Windows.Win32.Foundation.HWND
    haccel: win32more.Windows.Win32.UI.WindowsAndMessaging.HACCEL
    cAccelEntries: UInt32
OLEIVERB = Int32
OLEIVERB_PRIMARY: win32more.Windows.Win32.System.Ole.OLEIVERB = 0
OLEIVERB_SHOW: win32more.Windows.Win32.System.Ole.OLEIVERB = -1
OLEIVERB_OPEN: win32more.Windows.Win32.System.Ole.OLEIVERB = -2
OLEIVERB_HIDE: win32more.Windows.Win32.System.Ole.OLEIVERB = -3
OLEIVERB_UIACTIVATE: win32more.Windows.Win32.System.Ole.OLEIVERB = -4
OLEIVERB_INPLACEACTIVATE: win32more.Windows.Win32.System.Ole.OLEIVERB = -5
OLEIVERB_DISCARDUNDOSTATE: win32more.Windows.Win32.System.Ole.OLEIVERB = -6
OLELINKBIND = Int32
OLELINKBIND_EVENIFCLASSDIFF: win32more.Windows.Win32.System.Ole.OLELINKBIND = 1
class OLEMENUGROUPWIDTHS(Structure):
    width: Int32 * 6
OLEMISC = Int32
OLEMISC_RECOMPOSEONRESIZE: win32more.Windows.Win32.System.Ole.OLEMISC = 1
OLEMISC_ONLYICONIC: win32more.Windows.Win32.System.Ole.OLEMISC = 2
OLEMISC_INSERTNOTREPLACE: win32more.Windows.Win32.System.Ole.OLEMISC = 4
OLEMISC_STATIC: win32more.Windows.Win32.System.Ole.OLEMISC = 8
OLEMISC_CANTLINKINSIDE: win32more.Windows.Win32.System.Ole.OLEMISC = 16
OLEMISC_CANLINKBYOLE1: win32more.Windows.Win32.System.Ole.OLEMISC = 32
OLEMISC_ISLINKOBJECT: win32more.Windows.Win32.System.Ole.OLEMISC = 64
OLEMISC_INSIDEOUT: win32more.Windows.Win32.System.Ole.OLEMISC = 128
OLEMISC_ACTIVATEWHENVISIBLE: win32more.Windows.Win32.System.Ole.OLEMISC = 256
OLEMISC_RENDERINGISDEVICEINDEPENDENT: win32more.Windows.Win32.System.Ole.OLEMISC = 512
OLEMISC_INVISIBLEATRUNTIME: win32more.Windows.Win32.System.Ole.OLEMISC = 1024
OLEMISC_ALWAYSRUN: win32more.Windows.Win32.System.Ole.OLEMISC = 2048
OLEMISC_ACTSLIKEBUTTON: win32more.Windows.Win32.System.Ole.OLEMISC = 4096
OLEMISC_ACTSLIKELABEL: win32more.Windows.Win32.System.Ole.OLEMISC = 8192
OLEMISC_NOUIACTIVATE: win32more.Windows.Win32.System.Ole.OLEMISC = 16384
OLEMISC_ALIGNABLE: win32more.Windows.Win32.System.Ole.OLEMISC = 32768
OLEMISC_SIMPLEFRAME: win32more.Windows.Win32.System.Ole.OLEMISC = 65536
OLEMISC_SETCLIENTSITEFIRST: win32more.Windows.Win32.System.Ole.OLEMISC = 131072
OLEMISC_IMEMODE: win32more.Windows.Win32.System.Ole.OLEMISC = 262144
OLEMISC_IGNOREACTIVATEWHENVISIBLE: win32more.Windows.Win32.System.Ole.OLEMISC = 524288
OLEMISC_WANTSTOMENUMERGE: win32more.Windows.Win32.System.Ole.OLEMISC = 1048576
OLEMISC_SUPPORTSMULTILEVELUNDO: win32more.Windows.Win32.System.Ole.OLEMISC = 2097152
OLERENDER = Int32
OLERENDER_NONE: win32more.Windows.Win32.System.Ole.OLERENDER = 0
OLERENDER_DRAW: win32more.Windows.Win32.System.Ole.OLERENDER = 1
OLERENDER_FORMAT: win32more.Windows.Win32.System.Ole.OLERENDER = 2
OLERENDER_ASIS: win32more.Windows.Win32.System.Ole.OLERENDER = 3
@winfunctype_pointer
def OLESTREAMQUERYCONVERTOLELINKCALLBACK(pClsid: POINTER(Guid), szClass: win32more.Windows.Win32.Foundation.PWSTR, szTopicName: win32more.Windows.Win32.Foundation.PWSTR, szItemName: win32more.Windows.Win32.Foundation.PWSTR, szUNCName: win32more.Windows.Win32.Foundation.PWSTR, linkUpdatingOption: UInt32, pvContext: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class OLEUIBUSYA(Structure):
    cbStruct: UInt32
    dwFlags: win32more.Windows.Win32.System.Ole.BUSY_DIALOG_FLAGS
    hWndOwner: win32more.Windows.Win32.Foundation.HWND
    lpszCaption: win32more.Windows.Win32.Foundation.PSTR
    lpfnHook: win32more.Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: win32more.Windows.Win32.Foundation.LPARAM
    hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
    lpszTemplate: win32more.Windows.Win32.Foundation.PSTR
    hResource: win32more.Windows.Win32.Foundation.HRSRC
    hTask: win32more.Windows.Win32.Media.HTASK
    lphWndDialog: POINTER(win32more.Windows.Win32.Foundation.HWND)
class OLEUIBUSYW(Structure):
    cbStruct: UInt32
    dwFlags: win32more.Windows.Win32.System.Ole.BUSY_DIALOG_FLAGS
    hWndOwner: win32more.Windows.Win32.Foundation.HWND
    lpszCaption: win32more.Windows.Win32.Foundation.PWSTR
    lpfnHook: win32more.Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: win32more.Windows.Win32.Foundation.LPARAM
    hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
    lpszTemplate: win32more.Windows.Win32.Foundation.PWSTR
    hResource: win32more.Windows.Win32.Foundation.HRSRC
    hTask: win32more.Windows.Win32.Media.HTASK
    lphWndDialog: POINTER(win32more.Windows.Win32.Foundation.HWND)
OLEUIBUSY = UnicodeAlias('OLEUIBUSYW')
class OLEUICHANGEICONA(Structure):
    cbStruct: UInt32
    dwFlags: win32more.Windows.Win32.System.Ole.CHANGE_ICON_FLAGS
    hWndOwner: win32more.Windows.Win32.Foundation.HWND
    lpszCaption: win32more.Windows.Win32.Foundation.PSTR
    lpfnHook: win32more.Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: win32more.Windows.Win32.Foundation.LPARAM
    hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
    lpszTemplate: win32more.Windows.Win32.Foundation.PSTR
    hResource: win32more.Windows.Win32.Foundation.HRSRC
    hMetaPict: win32more.Windows.Win32.Foundation.HGLOBAL
    clsid: Guid
    szIconExe: win32more.Windows.Win32.Foundation.CHAR * 260
    cchIconExe: Int32
class OLEUICHANGEICONW(Structure):
    cbStruct: UInt32
    dwFlags: win32more.Windows.Win32.System.Ole.CHANGE_ICON_FLAGS
    hWndOwner: win32more.Windows.Win32.Foundation.HWND
    lpszCaption: win32more.Windows.Win32.Foundation.PWSTR
    lpfnHook: win32more.Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: win32more.Windows.Win32.Foundation.LPARAM
    hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
    lpszTemplate: win32more.Windows.Win32.Foundation.PWSTR
    hResource: win32more.Windows.Win32.Foundation.HRSRC
    hMetaPict: win32more.Windows.Win32.Foundation.HGLOBAL
    clsid: Guid
    szIconExe: Char * 260
    cchIconExe: Int32
OLEUICHANGEICON = UnicodeAlias('OLEUICHANGEICONW')
class OLEUICHANGESOURCEA(Structure):
    cbStruct: UInt32
    dwFlags: win32more.Windows.Win32.System.Ole.CHANGE_SOURCE_FLAGS
    hWndOwner: win32more.Windows.Win32.Foundation.HWND
    lpszCaption: win32more.Windows.Win32.Foundation.PSTR
    lpfnHook: win32more.Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: win32more.Windows.Win32.Foundation.LPARAM
    hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
    lpszTemplate: win32more.Windows.Win32.Foundation.PSTR
    hResource: win32more.Windows.Win32.Foundation.HRSRC
    lpOFN: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.OPENFILENAMEA)
    dwReserved1: UInt32 * 4
    lpOleUILinkContainer: win32more.Windows.Win32.System.Ole.IOleUILinkContainerA
    dwLink: UInt32
    lpszDisplayName: win32more.Windows.Win32.Foundation.PSTR
    nFileLength: UInt32
    lpszFrom: win32more.Windows.Win32.Foundation.PSTR
    lpszTo: win32more.Windows.Win32.Foundation.PSTR
class OLEUICHANGESOURCEW(Structure):
    cbStruct: UInt32
    dwFlags: win32more.Windows.Win32.System.Ole.CHANGE_SOURCE_FLAGS
    hWndOwner: win32more.Windows.Win32.Foundation.HWND
    lpszCaption: win32more.Windows.Win32.Foundation.PWSTR
    lpfnHook: win32more.Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: win32more.Windows.Win32.Foundation.LPARAM
    hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
    lpszTemplate: win32more.Windows.Win32.Foundation.PWSTR
    hResource: win32more.Windows.Win32.Foundation.HRSRC
    lpOFN: POINTER(win32more.Windows.Win32.UI.Controls.Dialogs.OPENFILENAMEW)
    dwReserved1: UInt32 * 4
    lpOleUILinkContainer: win32more.Windows.Win32.System.Ole.IOleUILinkContainerW
    dwLink: UInt32
    lpszDisplayName: win32more.Windows.Win32.Foundation.PWSTR
    nFileLength: UInt32
    lpszFrom: win32more.Windows.Win32.Foundation.PWSTR
    lpszTo: win32more.Windows.Win32.Foundation.PWSTR
OLEUICHANGESOURCE = UnicodeAlias('OLEUICHANGESOURCEW')
class OLEUICONVERTA(Structure):
    cbStruct: UInt32
    dwFlags: win32more.Windows.Win32.System.Ole.UI_CONVERT_FLAGS
    hWndOwner: win32more.Windows.Win32.Foundation.HWND
    lpszCaption: win32more.Windows.Win32.Foundation.PSTR
    lpfnHook: win32more.Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: win32more.Windows.Win32.Foundation.LPARAM
    hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
    lpszTemplate: win32more.Windows.Win32.Foundation.PSTR
    hResource: win32more.Windows.Win32.Foundation.HRSRC
    clsid: Guid
    clsidConvertDefault: Guid
    clsidActivateDefault: Guid
    clsidNew: Guid
    dvAspect: UInt32
    wFormat: UInt16
    fIsLinkedObject: win32more.Windows.Win32.Foundation.BOOL
    hMetaPict: win32more.Windows.Win32.Foundation.HGLOBAL
    lpszUserType: win32more.Windows.Win32.Foundation.PSTR
    fObjectsIconChanged: win32more.Windows.Win32.Foundation.BOOL
    lpszDefLabel: win32more.Windows.Win32.Foundation.PSTR
    cClsidExclude: UInt32
    lpClsidExclude: POINTER(Guid)
class OLEUICONVERTW(Structure):
    cbStruct: UInt32
    dwFlags: win32more.Windows.Win32.System.Ole.UI_CONVERT_FLAGS
    hWndOwner: win32more.Windows.Win32.Foundation.HWND
    lpszCaption: win32more.Windows.Win32.Foundation.PWSTR
    lpfnHook: win32more.Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: win32more.Windows.Win32.Foundation.LPARAM
    hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
    lpszTemplate: win32more.Windows.Win32.Foundation.PWSTR
    hResource: win32more.Windows.Win32.Foundation.HRSRC
    clsid: Guid
    clsidConvertDefault: Guid
    clsidActivateDefault: Guid
    clsidNew: Guid
    dvAspect: UInt32
    wFormat: UInt16
    fIsLinkedObject: win32more.Windows.Win32.Foundation.BOOL
    hMetaPict: win32more.Windows.Win32.Foundation.HGLOBAL
    lpszUserType: win32more.Windows.Win32.Foundation.PWSTR
    fObjectsIconChanged: win32more.Windows.Win32.Foundation.BOOL
    lpszDefLabel: win32more.Windows.Win32.Foundation.PWSTR
    cClsidExclude: UInt32
    lpClsidExclude: POINTER(Guid)
OLEUICONVERT = UnicodeAlias('OLEUICONVERTW')
class OLEUIEDITLINKSA(Structure):
    cbStruct: UInt32
    dwFlags: win32more.Windows.Win32.System.Ole.EDIT_LINKS_FLAGS
    hWndOwner: win32more.Windows.Win32.Foundation.HWND
    lpszCaption: win32more.Windows.Win32.Foundation.PSTR
    lpfnHook: win32more.Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: win32more.Windows.Win32.Foundation.LPARAM
    hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
    lpszTemplate: win32more.Windows.Win32.Foundation.PSTR
    hResource: win32more.Windows.Win32.Foundation.HRSRC
    lpOleUILinkContainer: win32more.Windows.Win32.System.Ole.IOleUILinkContainerA
class OLEUIEDITLINKSW(Structure):
    cbStruct: UInt32
    dwFlags: win32more.Windows.Win32.System.Ole.EDIT_LINKS_FLAGS
    hWndOwner: win32more.Windows.Win32.Foundation.HWND
    lpszCaption: win32more.Windows.Win32.Foundation.PWSTR
    lpfnHook: win32more.Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: win32more.Windows.Win32.Foundation.LPARAM
    hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
    lpszTemplate: win32more.Windows.Win32.Foundation.PWSTR
    hResource: win32more.Windows.Win32.Foundation.HRSRC
    lpOleUILinkContainer: win32more.Windows.Win32.System.Ole.IOleUILinkContainerW
OLEUIEDITLINKS = UnicodeAlias('OLEUIEDITLINKSW')
class OLEUIGNRLPROPSA(Structure):
    cbStruct: UInt32
    dwFlags: UInt32
    dwReserved1: UInt32 * 2
    lpfnHook: win32more.Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: win32more.Windows.Win32.Foundation.LPARAM
    dwReserved2: UInt32 * 3
    lpOP: POINTER(win32more.Windows.Win32.System.Ole.OLEUIOBJECTPROPSA)
class OLEUIGNRLPROPSW(Structure):
    cbStruct: UInt32
    dwFlags: UInt32
    dwReserved1: UInt32 * 2
    lpfnHook: win32more.Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: win32more.Windows.Win32.Foundation.LPARAM
    dwReserved2: UInt32 * 3
    lpOP: POINTER(win32more.Windows.Win32.System.Ole.OLEUIOBJECTPROPSW)
OLEUIGNRLPROPS = UnicodeAlias('OLEUIGNRLPROPSW')
class OLEUIINSERTOBJECTA(Structure):
    cbStruct: UInt32
    dwFlags: win32more.Windows.Win32.System.Ole.INSERT_OBJECT_FLAGS
    hWndOwner: win32more.Windows.Win32.Foundation.HWND
    lpszCaption: win32more.Windows.Win32.Foundation.PSTR
    lpfnHook: win32more.Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: win32more.Windows.Win32.Foundation.LPARAM
    hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
    lpszTemplate: win32more.Windows.Win32.Foundation.PSTR
    hResource: win32more.Windows.Win32.Foundation.HRSRC
    clsid: Guid
    lpszFile: win32more.Windows.Win32.Foundation.PSTR
    cchFile: UInt32
    cClsidExclude: UInt32
    lpClsidExclude: POINTER(Guid)
    iid: Guid
    oleRender: UInt32
    lpFormatEtc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC)
    lpIOleClientSite: win32more.Windows.Win32.System.Ole.IOleClientSite
    lpIStorage: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage
    ppvObj: POINTER(VoidPtr)
    sc: Int32
    hMetaPict: win32more.Windows.Win32.Foundation.HGLOBAL
class OLEUIINSERTOBJECTW(Structure):
    cbStruct: UInt32
    dwFlags: win32more.Windows.Win32.System.Ole.INSERT_OBJECT_FLAGS
    hWndOwner: win32more.Windows.Win32.Foundation.HWND
    lpszCaption: win32more.Windows.Win32.Foundation.PWSTR
    lpfnHook: win32more.Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: win32more.Windows.Win32.Foundation.LPARAM
    hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
    lpszTemplate: win32more.Windows.Win32.Foundation.PWSTR
    hResource: win32more.Windows.Win32.Foundation.HRSRC
    clsid: Guid
    lpszFile: win32more.Windows.Win32.Foundation.PWSTR
    cchFile: UInt32
    cClsidExclude: UInt32
    lpClsidExclude: POINTER(Guid)
    iid: Guid
    oleRender: UInt32
    lpFormatEtc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC)
    lpIOleClientSite: win32more.Windows.Win32.System.Ole.IOleClientSite
    lpIStorage: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage
    ppvObj: POINTER(VoidPtr)
    sc: Int32
    hMetaPict: win32more.Windows.Win32.Foundation.HGLOBAL
OLEUIINSERTOBJECT = UnicodeAlias('OLEUIINSERTOBJECTW')
class OLEUILINKPROPSA(Structure):
    cbStruct: UInt32
    dwFlags: UInt32
    dwReserved1: UInt32 * 2
    lpfnHook: win32more.Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: win32more.Windows.Win32.Foundation.LPARAM
    dwReserved2: UInt32 * 3
    lpOP: POINTER(win32more.Windows.Win32.System.Ole.OLEUIOBJECTPROPSA)
class OLEUILINKPROPSW(Structure):
    cbStruct: UInt32
    dwFlags: UInt32
    dwReserved1: UInt32 * 2
    lpfnHook: win32more.Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: win32more.Windows.Win32.Foundation.LPARAM
    dwReserved2: UInt32 * 3
    lpOP: POINTER(win32more.Windows.Win32.System.Ole.OLEUIOBJECTPROPSW)
OLEUILINKPROPS = UnicodeAlias('OLEUILINKPROPSW')
class OLEUIOBJECTPROPSA(Structure):
    cbStruct: UInt32
    dwFlags: win32more.Windows.Win32.System.Ole.OBJECT_PROPERTIES_FLAGS
    lpPS: POINTER(win32more.Windows.Win32.UI.Controls.PROPSHEETHEADERA_V2)
    dwObject: UInt32
    lpObjInfo: win32more.Windows.Win32.System.Ole.IOleUIObjInfoA
    dwLink: UInt32
    lpLinkInfo: win32more.Windows.Win32.System.Ole.IOleUILinkInfoA
    lpGP: POINTER(win32more.Windows.Win32.System.Ole.OLEUIGNRLPROPSA)
    lpVP: POINTER(win32more.Windows.Win32.System.Ole.OLEUIVIEWPROPSA)
    lpLP: POINTER(win32more.Windows.Win32.System.Ole.OLEUILINKPROPSA)
class OLEUIOBJECTPROPSW(Structure):
    cbStruct: UInt32
    dwFlags: win32more.Windows.Win32.System.Ole.OBJECT_PROPERTIES_FLAGS
    lpPS: POINTER(win32more.Windows.Win32.UI.Controls.PROPSHEETHEADERW_V2)
    dwObject: UInt32
    lpObjInfo: win32more.Windows.Win32.System.Ole.IOleUIObjInfoW
    dwLink: UInt32
    lpLinkInfo: win32more.Windows.Win32.System.Ole.IOleUILinkInfoW
    lpGP: POINTER(win32more.Windows.Win32.System.Ole.OLEUIGNRLPROPSW)
    lpVP: POINTER(win32more.Windows.Win32.System.Ole.OLEUIVIEWPROPSW)
    lpLP: POINTER(win32more.Windows.Win32.System.Ole.OLEUILINKPROPSW)
OLEUIOBJECTPROPS = UnicodeAlias('OLEUIOBJECTPROPSW')
class OLEUIPASTEENTRYA(Structure):
    fmtetc: win32more.Windows.Win32.System.Com.FORMATETC
    lpstrFormatName: win32more.Windows.Win32.Foundation.PSTR
    lpstrResultText: win32more.Windows.Win32.Foundation.PSTR
    dwFlags: UInt32
    dwScratchSpace: UInt32
class OLEUIPASTEENTRYW(Structure):
    fmtetc: win32more.Windows.Win32.System.Com.FORMATETC
    lpstrFormatName: win32more.Windows.Win32.Foundation.PWSTR
    lpstrResultText: win32more.Windows.Win32.Foundation.PWSTR
    dwFlags: UInt32
    dwScratchSpace: UInt32
OLEUIPASTEENTRY = UnicodeAlias('OLEUIPASTEENTRYW')
OLEUIPASTEFLAG = Int32
OLEUIPASTE_ENABLEICON: win32more.Windows.Win32.System.Ole.OLEUIPASTEFLAG = 2048
OLEUIPASTE_PASTEONLY: win32more.Windows.Win32.System.Ole.OLEUIPASTEFLAG = 0
OLEUIPASTE_PASTE: win32more.Windows.Win32.System.Ole.OLEUIPASTEFLAG = 512
OLEUIPASTE_LINKANYTYPE: win32more.Windows.Win32.System.Ole.OLEUIPASTEFLAG = 1024
OLEUIPASTE_LINKTYPE1: win32more.Windows.Win32.System.Ole.OLEUIPASTEFLAG = 1
OLEUIPASTE_LINKTYPE2: win32more.Windows.Win32.System.Ole.OLEUIPASTEFLAG = 2
OLEUIPASTE_LINKTYPE3: win32more.Windows.Win32.System.Ole.OLEUIPASTEFLAG = 4
OLEUIPASTE_LINKTYPE4: win32more.Windows.Win32.System.Ole.OLEUIPASTEFLAG = 8
OLEUIPASTE_LINKTYPE5: win32more.Windows.Win32.System.Ole.OLEUIPASTEFLAG = 16
OLEUIPASTE_LINKTYPE6: win32more.Windows.Win32.System.Ole.OLEUIPASTEFLAG = 32
OLEUIPASTE_LINKTYPE7: win32more.Windows.Win32.System.Ole.OLEUIPASTEFLAG = 64
OLEUIPASTE_LINKTYPE8: win32more.Windows.Win32.System.Ole.OLEUIPASTEFLAG = 128
class OLEUIPASTESPECIALA(Structure):
    cbStruct: UInt32
    dwFlags: win32more.Windows.Win32.System.Ole.PASTE_SPECIAL_FLAGS
    hWndOwner: win32more.Windows.Win32.Foundation.HWND
    lpszCaption: win32more.Windows.Win32.Foundation.PSTR
    lpfnHook: win32more.Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: win32more.Windows.Win32.Foundation.LPARAM
    hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
    lpszTemplate: win32more.Windows.Win32.Foundation.PSTR
    hResource: win32more.Windows.Win32.Foundation.HRSRC
    lpSrcDataObj: win32more.Windows.Win32.System.Com.IDataObject
    arrPasteEntries: POINTER(win32more.Windows.Win32.System.Ole.OLEUIPASTEENTRYA)
    cPasteEntries: Int32
    arrLinkTypes: POINTER(UInt32)
    cLinkTypes: Int32
    cClsidExclude: UInt32
    lpClsidExclude: POINTER(Guid)
    nSelectedIndex: Int32
    fLink: win32more.Windows.Win32.Foundation.BOOL
    hMetaPict: win32more.Windows.Win32.Foundation.HGLOBAL
    sizel: win32more.Windows.Win32.Foundation.SIZE
class OLEUIPASTESPECIALW(Structure):
    cbStruct: UInt32
    dwFlags: win32more.Windows.Win32.System.Ole.PASTE_SPECIAL_FLAGS
    hWndOwner: win32more.Windows.Win32.Foundation.HWND
    lpszCaption: win32more.Windows.Win32.Foundation.PWSTR
    lpfnHook: win32more.Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: win32more.Windows.Win32.Foundation.LPARAM
    hInstance: win32more.Windows.Win32.Foundation.HINSTANCE
    lpszTemplate: win32more.Windows.Win32.Foundation.PWSTR
    hResource: win32more.Windows.Win32.Foundation.HRSRC
    lpSrcDataObj: win32more.Windows.Win32.System.Com.IDataObject
    arrPasteEntries: POINTER(win32more.Windows.Win32.System.Ole.OLEUIPASTEENTRYW)
    cPasteEntries: Int32
    arrLinkTypes: POINTER(UInt32)
    cLinkTypes: Int32
    cClsidExclude: UInt32
    lpClsidExclude: POINTER(Guid)
    nSelectedIndex: Int32
    fLink: win32more.Windows.Win32.Foundation.BOOL
    hMetaPict: win32more.Windows.Win32.Foundation.HGLOBAL
    sizel: win32more.Windows.Win32.Foundation.SIZE
OLEUIPASTESPECIAL = UnicodeAlias('OLEUIPASTESPECIALW')
class OLEUIVIEWPROPSA(Structure):
    cbStruct: UInt32
    dwFlags: win32more.Windows.Win32.System.Ole.VIEW_OBJECT_PROPERTIES_FLAGS
    dwReserved1: UInt32 * 2
    lpfnHook: win32more.Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: win32more.Windows.Win32.Foundation.LPARAM
    dwReserved2: UInt32 * 3
    lpOP: POINTER(win32more.Windows.Win32.System.Ole.OLEUIOBJECTPROPSA)
    nScaleMin: Int32
    nScaleMax: Int32
class OLEUIVIEWPROPSW(Structure):
    cbStruct: UInt32
    dwFlags: win32more.Windows.Win32.System.Ole.VIEW_OBJECT_PROPERTIES_FLAGS
    dwReserved1: UInt32 * 2
    lpfnHook: win32more.Windows.Win32.System.Ole.LPFNOLEUIHOOK
    lCustData: win32more.Windows.Win32.Foundation.LPARAM
    dwReserved2: UInt32 * 3
    lpOP: POINTER(win32more.Windows.Win32.System.Ole.OLEUIOBJECTPROPSW)
    nScaleMin: Int32
    nScaleMax: Int32
OLEUIVIEWPROPS = UnicodeAlias('OLEUIVIEWPROPSW')
OLEUPDATE = Int32
OLEUPDATE_ALWAYS: win32more.Windows.Win32.System.Ole.OLEUPDATE = 1
OLEUPDATE_ONCALL: win32more.Windows.Win32.System.Ole.OLEUPDATE = 3
class OLEVERB(Structure):
    lVerb: win32more.Windows.Win32.System.Ole.OLEIVERB
    lpszVerbName: win32more.Windows.Win32.Foundation.PWSTR
    fuFlags: win32more.Windows.Win32.UI.WindowsAndMessaging.MENU_ITEM_FLAGS
    grfAttribs: UInt32
OLEVERBATTRIB = Int32
OLEVERBATTRIB_NEVERDIRTIES: win32more.Windows.Win32.System.Ole.OLEVERBATTRIB = 1
OLEVERBATTRIB_ONCONTAINERMENU: win32more.Windows.Win32.System.Ole.OLEVERBATTRIB = 2
OLEWHICHMK = Int32
OLEWHICHMK_CONTAINER: win32more.Windows.Win32.System.Ole.OLEWHICHMK = 1
OLEWHICHMK_OBJREL: win32more.Windows.Win32.System.Ole.OLEWHICHMK = 2
OLEWHICHMK_OBJFULL: win32more.Windows.Win32.System.Ole.OLEWHICHMK = 3
OLE_HANDLE = UInt32
OLE_TRISTATE = Int32
triUnchecked: win32more.Windows.Win32.System.Ole.OLE_TRISTATE = 0
triChecked: win32more.Windows.Win32.System.Ole.OLE_TRISTATE = 1
triGray: win32more.Windows.Win32.System.Ole.OLE_TRISTATE = 2
PAGEACTION_UI = Int32
PAGEACTION_UI_DEFAULT: win32more.Windows.Win32.System.Ole.PAGEACTION_UI = 0
PAGEACTION_UI_MODAL: win32more.Windows.Win32.System.Ole.PAGEACTION_UI = 1
PAGEACTION_UI_MODELESS: win32more.Windows.Win32.System.Ole.PAGEACTION_UI = 2
PAGEACTION_UI_SILENT: win32more.Windows.Win32.System.Ole.PAGEACTION_UI = 3
class PAGERANGE(Structure):
    nFromPage: Int32
    nToPage: Int32
class PAGESET(Structure):
    cbStruct: UInt32
    fOddPages: win32more.Windows.Win32.Foundation.BOOL
    fEvenPages: win32more.Windows.Win32.Foundation.BOOL
    cPageRange: UInt32
    rgPages: win32more.Windows.Win32.System.Ole.PAGERANGE * 1
class PARAMDATA(Structure):
    szName: win32more.Windows.Win32.Foundation.PWSTR
    vt: win32more.Windows.Win32.System.Variant.VARENUM
class PARAMDESC(Structure):
    pparamdescex: POINTER(win32more.Windows.Win32.System.Ole.PARAMDESCEX)
    wParamFlags: win32more.Windows.Win32.System.Ole.PARAMFLAGS
class PARAMDESCEX(Structure):
    cBytes: UInt32
    varDefaultValue: win32more.Windows.Win32.System.Variant.VARIANT
PARAMFLAGS = UInt16
PARAMFLAG_NONE: win32more.Windows.Win32.System.Ole.PARAMFLAGS = 0
PARAMFLAG_FIN: win32more.Windows.Win32.System.Ole.PARAMFLAGS = 1
PARAMFLAG_FOUT: win32more.Windows.Win32.System.Ole.PARAMFLAGS = 2
PARAMFLAG_FLCID: win32more.Windows.Win32.System.Ole.PARAMFLAGS = 4
PARAMFLAG_FRETVAL: win32more.Windows.Win32.System.Ole.PARAMFLAGS = 8
PARAMFLAG_FOPT: win32more.Windows.Win32.System.Ole.PARAMFLAGS = 16
PARAMFLAG_FHASDEFAULT: win32more.Windows.Win32.System.Ole.PARAMFLAGS = 32
PARAMFLAG_FHASCUSTDATA: win32more.Windows.Win32.System.Ole.PARAMFLAGS = 64
PASTE_SPECIAL_FLAGS = UInt32
PSF_SHOWHELP: win32more.Windows.Win32.System.Ole.PASTE_SPECIAL_FLAGS = 1
PSF_SELECTPASTE: win32more.Windows.Win32.System.Ole.PASTE_SPECIAL_FLAGS = 2
PSF_SELECTPASTELINK: win32more.Windows.Win32.System.Ole.PASTE_SPECIAL_FLAGS = 4
PSF_CHECKDISPLAYASICON: win32more.Windows.Win32.System.Ole.PASTE_SPECIAL_FLAGS = 8
PSF_DISABLEDISPLAYASICON: win32more.Windows.Win32.System.Ole.PASTE_SPECIAL_FLAGS = 16
PSF_HIDECHANGEICON: win32more.Windows.Win32.System.Ole.PASTE_SPECIAL_FLAGS = 32
PSF_STAYONCLIPBOARDCHANGE: win32more.Windows.Win32.System.Ole.PASTE_SPECIAL_FLAGS = 64
PSF_NOREFRESHDATAOBJECT: win32more.Windows.Win32.System.Ole.PASTE_SPECIAL_FLAGS = 128
class PICTDESC(Structure):
    cbSizeofstruct: UInt32
    picType: UInt32
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        bmp: _bmp_e__Struct
        wmf: _wmf_e__Struct
        icon: _icon_e__Struct
        emf: _emf_e__Struct
        class _bmp_e__Struct(Structure):
            hbitmap: win32more.Windows.Win32.Graphics.Gdi.HBITMAP
            hpal: win32more.Windows.Win32.Graphics.Gdi.HPALETTE
        class _wmf_e__Struct(Structure):
            hmeta: win32more.Windows.Win32.Graphics.Gdi.HMETAFILE
            xExt: Int32
            yExt: Int32
        class _icon_e__Struct(Structure):
            hicon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON
        class _emf_e__Struct(Structure):
            hemf: win32more.Windows.Win32.Graphics.Gdi.HENHMETAFILE
PICTUREATTRIBUTES = Int32
PICTURE_SCALABLE: win32more.Windows.Win32.System.Ole.PICTUREATTRIBUTES = 1
PICTURE_TRANSPARENT: win32more.Windows.Win32.System.Ole.PICTUREATTRIBUTES = 2
PICTYPE = Int16
PICTYPE_UNINITIALIZED: win32more.Windows.Win32.System.Ole.PICTYPE = -1
PICTYPE_NONE: win32more.Windows.Win32.System.Ole.PICTYPE = 0
PICTYPE_BITMAP: win32more.Windows.Win32.System.Ole.PICTYPE = 1
PICTYPE_METAFILE: win32more.Windows.Win32.System.Ole.PICTYPE = 2
PICTYPE_ICON: win32more.Windows.Win32.System.Ole.PICTYPE = 3
PICTYPE_ENHMETAFILE: win32more.Windows.Win32.System.Ole.PICTYPE = 4
POINTERINACTIVE = Int32
POINTERINACTIVE_ACTIVATEONENTRY: win32more.Windows.Win32.System.Ole.POINTERINACTIVE = 1
POINTERINACTIVE_DEACTIVATEONLEAVE: win32more.Windows.Win32.System.Ole.POINTERINACTIVE = 2
POINTERINACTIVE_ACTIVATEONDRAG: win32more.Windows.Win32.System.Ole.POINTERINACTIVE = 4
class POINTF(Structure):
    x: Single
    y: Single
PRINTFLAG = Int32
PRINTFLAG_MAYBOTHERUSER: win32more.Windows.Win32.System.Ole.PRINTFLAG = 1
PRINTFLAG_PROMPTUSER: win32more.Windows.Win32.System.Ole.PRINTFLAG = 2
PRINTFLAG_USERMAYCHANGEPRINTER: win32more.Windows.Win32.System.Ole.PRINTFLAG = 4
PRINTFLAG_RECOMPOSETODEVICE: win32more.Windows.Win32.System.Ole.PRINTFLAG = 8
PRINTFLAG_DONTACTUALLYPRINT: win32more.Windows.Win32.System.Ole.PRINTFLAG = 16
PRINTFLAG_FORCEPROPERTIES: win32more.Windows.Win32.System.Ole.PRINTFLAG = 32
PRINTFLAG_PRINTTOFILE: win32more.Windows.Win32.System.Ole.PRINTFLAG = 64
PROPBAG2_TYPE = Int32
PROPBAG2_TYPE_UNDEFINED: win32more.Windows.Win32.System.Ole.PROPBAG2_TYPE = 0
PROPBAG2_TYPE_DATA: win32more.Windows.Win32.System.Ole.PROPBAG2_TYPE = 1
PROPBAG2_TYPE_URL: win32more.Windows.Win32.System.Ole.PROPBAG2_TYPE = 2
PROPBAG2_TYPE_OBJECT: win32more.Windows.Win32.System.Ole.PROPBAG2_TYPE = 3
PROPBAG2_TYPE_STREAM: win32more.Windows.Win32.System.Ole.PROPBAG2_TYPE = 4
PROPBAG2_TYPE_STORAGE: win32more.Windows.Win32.System.Ole.PROPBAG2_TYPE = 5
PROPBAG2_TYPE_MONIKER: win32more.Windows.Win32.System.Ole.PROPBAG2_TYPE = 6
class PROPPAGEINFO(Structure):
    cb: UInt32
    pszTitle: win32more.Windows.Win32.Foundation.PWSTR
    size: win32more.Windows.Win32.Foundation.SIZE
    pszDocString: win32more.Windows.Win32.Foundation.PWSTR
    pszHelpFile: win32more.Windows.Win32.Foundation.PWSTR
    dwHelpContext: UInt32
PROPPAGESTATUS = Int32
PROPPAGESTATUS_DIRTY: win32more.Windows.Win32.System.Ole.PROPPAGESTATUS = 1
PROPPAGESTATUS_VALIDATE: win32more.Windows.Win32.System.Ole.PROPPAGESTATUS = 2
PROPPAGESTATUS_CLEAN: win32more.Windows.Win32.System.Ole.PROPPAGESTATUS = 4
class QACONTAINER(Structure):
    cbSize: UInt32
    pClientSite: win32more.Windows.Win32.System.Ole.IOleClientSite
    pAdviseSink: win32more.Windows.Win32.System.Ole.IAdviseSinkEx
    pPropertyNotifySink: win32more.Windows.Win32.System.Ole.IPropertyNotifySink
    pUnkEventSink: win32more.Windows.Win32.System.Com.IUnknown
    dwAmbientFlags: UInt32
    colorFore: UInt32
    colorBack: UInt32
    pFont: win32more.Windows.Win32.System.Ole.IFont
    pUndoMgr: win32more.Windows.Win32.System.Ole.IOleUndoManager
    dwAppearance: UInt32
    lcid: Int32
    hpal: win32more.Windows.Win32.Graphics.Gdi.HPALETTE
    pBindHost: win32more.Windows.Win32.System.Com.IBindHost
    pOleControlSite: win32more.Windows.Win32.System.Ole.IOleControlSite
    pServiceProvider: win32more.Windows.Win32.System.Com.IServiceProvider
QACONTAINERFLAGS = Int32
QACONTAINER_SHOWHATCHING: win32more.Windows.Win32.System.Ole.QACONTAINERFLAGS = 1
QACONTAINER_SHOWGRABHANDLES: win32more.Windows.Win32.System.Ole.QACONTAINERFLAGS = 2
QACONTAINER_USERMODE: win32more.Windows.Win32.System.Ole.QACONTAINERFLAGS = 4
QACONTAINER_DISPLAYASDEFAULT: win32more.Windows.Win32.System.Ole.QACONTAINERFLAGS = 8
QACONTAINER_UIDEAD: win32more.Windows.Win32.System.Ole.QACONTAINERFLAGS = 16
QACONTAINER_AUTOCLIP: win32more.Windows.Win32.System.Ole.QACONTAINERFLAGS = 32
QACONTAINER_MESSAGEREFLECT: win32more.Windows.Win32.System.Ole.QACONTAINERFLAGS = 64
QACONTAINER_SUPPORTSMNEMONICS: win32more.Windows.Win32.System.Ole.QACONTAINERFLAGS = 128
class QACONTROL(Structure):
    cbSize: UInt32
    dwMiscStatus: UInt32
    dwViewStatus: UInt32
    dwEventCookie: UInt32
    dwPropNotifyCookie: UInt32
    dwPointerActivationPolicy: UInt32
READYSTATE = Int32
READYSTATE_UNINITIALIZED: win32more.Windows.Win32.System.Ole.READYSTATE = 0
READYSTATE_LOADING: win32more.Windows.Win32.System.Ole.READYSTATE = 1
READYSTATE_LOADED: win32more.Windows.Win32.System.Ole.READYSTATE = 2
READYSTATE_INTERACTIVE: win32more.Windows.Win32.System.Ole.READYSTATE = 3
READYSTATE_COMPLETE: win32more.Windows.Win32.System.Ole.READYSTATE = 4
REGKIND = Int32
REGKIND_DEFAULT: win32more.Windows.Win32.System.Ole.REGKIND = 0
REGKIND_REGISTER: win32more.Windows.Win32.System.Ole.REGKIND = 1
REGKIND_NONE: win32more.Windows.Win32.System.Ole.REGKIND = 2
class SAFEARRAYUNION(Structure):
    sfType: UInt32
    u: _u_e__Struct
    class _u_e__Struct(Union):
        BstrStr: win32more.Windows.Win32.System.Ole.SAFEARR_BSTR
        UnknownStr: win32more.Windows.Win32.System.Ole.SAFEARR_UNKNOWN
        DispatchStr: win32more.Windows.Win32.System.Ole.SAFEARR_DISPATCH
        VariantStr: win32more.Windows.Win32.System.Ole.SAFEARR_VARIANT
        RecordStr: win32more.Windows.Win32.System.Ole.SAFEARR_BRECORD
        HaveIidStr: win32more.Windows.Win32.System.Ole.SAFEARR_HAVEIID
        ByteStr: win32more.Windows.Win32.System.Com.BYTE_SIZEDARR
        WordStr: win32more.Windows.Win32.System.Com.WORD_SIZEDARR
        LongStr: win32more.Windows.Win32.System.Com.DWORD_SIZEDARR
        HyperStr: win32more.Windows.Win32.System.Com.HYPER_SIZEDARR
class SAFEARR_BRECORD(Structure):
    Size: UInt32
    aRecord: POINTER(POINTER(win32more.Windows.Win32.System.Ole._wireBRECORD))
class SAFEARR_BSTR(Structure):
    Size: UInt32
    aBstr: POINTER(POINTER(win32more.Windows.Win32.System.Com.FLAGGED_WORD_BLOB))
class SAFEARR_DISPATCH(Structure):
    Size: UInt32
    apDispatch: POINTER(win32more.Windows.Win32.System.Com.IDispatch)
class SAFEARR_HAVEIID(Structure):
    Size: UInt32
    apUnknown: POINTER(win32more.Windows.Win32.System.Com.IUnknown)
    iid: Guid
class SAFEARR_UNKNOWN(Structure):
    Size: UInt32
    apUnknown: POINTER(win32more.Windows.Win32.System.Com.IUnknown)
class SAFEARR_VARIANT(Structure):
    Size: UInt32
    aVariant: POINTER(POINTER(win32more.Windows.Win32.System.Ole._wireVARIANT))
SF_TYPE = Int32
SF_ERROR: win32more.Windows.Win32.System.Ole.SF_TYPE = 10
SF_I1: win32more.Windows.Win32.System.Ole.SF_TYPE = 16
SF_I2: win32more.Windows.Win32.System.Ole.SF_TYPE = 2
SF_I4: win32more.Windows.Win32.System.Ole.SF_TYPE = 3
SF_I8: win32more.Windows.Win32.System.Ole.SF_TYPE = 20
SF_BSTR: win32more.Windows.Win32.System.Ole.SF_TYPE = 8
SF_UNKNOWN: win32more.Windows.Win32.System.Ole.SF_TYPE = 13
SF_DISPATCH: win32more.Windows.Win32.System.Ole.SF_TYPE = 9
SF_VARIANT: win32more.Windows.Win32.System.Ole.SF_TYPE = 12
SF_RECORD: win32more.Windows.Win32.System.Ole.SF_TYPE = 36
SF_HAVEIID: win32more.Windows.Win32.System.Ole.SF_TYPE = 32781
TYPEFLAGS = Int32
TYPEFLAG_FAPPOBJECT: win32more.Windows.Win32.System.Ole.TYPEFLAGS = 1
TYPEFLAG_FCANCREATE: win32more.Windows.Win32.System.Ole.TYPEFLAGS = 2
TYPEFLAG_FLICENSED: win32more.Windows.Win32.System.Ole.TYPEFLAGS = 4
TYPEFLAG_FPREDECLID: win32more.Windows.Win32.System.Ole.TYPEFLAGS = 8
TYPEFLAG_FHIDDEN: win32more.Windows.Win32.System.Ole.TYPEFLAGS = 16
TYPEFLAG_FCONTROL: win32more.Windows.Win32.System.Ole.TYPEFLAGS = 32
TYPEFLAG_FDUAL: win32more.Windows.Win32.System.Ole.TYPEFLAGS = 64
TYPEFLAG_FNONEXTENSIBLE: win32more.Windows.Win32.System.Ole.TYPEFLAGS = 128
TYPEFLAG_FOLEAUTOMATION: win32more.Windows.Win32.System.Ole.TYPEFLAGS = 256
TYPEFLAG_FRESTRICTED: win32more.Windows.Win32.System.Ole.TYPEFLAGS = 512
TYPEFLAG_FAGGREGATABLE: win32more.Windows.Win32.System.Ole.TYPEFLAGS = 1024
TYPEFLAG_FREPLACEABLE: win32more.Windows.Win32.System.Ole.TYPEFLAGS = 2048
TYPEFLAG_FDISPATCHABLE: win32more.Windows.Win32.System.Ole.TYPEFLAGS = 4096
TYPEFLAG_FREVERSEBIND: win32more.Windows.Win32.System.Ole.TYPEFLAGS = 8192
TYPEFLAG_FPROXY: win32more.Windows.Win32.System.Ole.TYPEFLAGS = 16384
UASFLAGS = Int32
UAS_NORMAL: win32more.Windows.Win32.System.Ole.UASFLAGS = 0
UAS_BLOCKED: win32more.Windows.Win32.System.Ole.UASFLAGS = 1
UAS_NOPARENTENABLE: win32more.Windows.Win32.System.Ole.UASFLAGS = 2
UAS_MASK: win32more.Windows.Win32.System.Ole.UASFLAGS = 3
class UDATE(Structure):
    st: win32more.Windows.Win32.Foundation.SYSTEMTIME
    wDayOfYear: UInt16
UI_CONVERT_FLAGS = UInt32
CF_SHOWHELPBUTTON: win32more.Windows.Win32.System.Ole.UI_CONVERT_FLAGS = 1
CF_SETCONVERTDEFAULT: win32more.Windows.Win32.System.Ole.UI_CONVERT_FLAGS = 2
CF_SETACTIVATEDEFAULT: win32more.Windows.Win32.System.Ole.UI_CONVERT_FLAGS = 4
CF_SELECTCONVERTTO: win32more.Windows.Win32.System.Ole.UI_CONVERT_FLAGS = 8
CF_SELECTACTIVATEAS: win32more.Windows.Win32.System.Ole.UI_CONVERT_FLAGS = 16
CF_DISABLEDISPLAYASICON: win32more.Windows.Win32.System.Ole.UI_CONVERT_FLAGS = 32
CF_DISABLEACTIVATEAS: win32more.Windows.Win32.System.Ole.UI_CONVERT_FLAGS = 64
CF_HIDECHANGEICON: win32more.Windows.Win32.System.Ole.UI_CONVERT_FLAGS = 128
CF_CONVERTONLY: win32more.Windows.Win32.System.Ole.UI_CONVERT_FLAGS = 256
UPDFCACHE_FLAGS = UInt32
UPDFCACHE_ALL: win32more.Windows.Win32.System.Ole.UPDFCACHE_FLAGS = 2147483647
UPDFCACHE_ALLBUTNODATACACHE: win32more.Windows.Win32.System.Ole.UPDFCACHE_FLAGS = 2147483646
UPDFCACHE_NORMALCACHE: win32more.Windows.Win32.System.Ole.UPDFCACHE_FLAGS = 8
UPDFCACHE_IFBLANK: win32more.Windows.Win32.System.Ole.UPDFCACHE_FLAGS = 16
UPDFCACHE_ONLYIFBLANK: win32more.Windows.Win32.System.Ole.UPDFCACHE_FLAGS = 2147483648
UPDFCACHE_NODATACACHE: win32more.Windows.Win32.System.Ole.UPDFCACHE_FLAGS = 1
UPDFCACHE_ONSAVECACHE: win32more.Windows.Win32.System.Ole.UPDFCACHE_FLAGS = 2
UPDFCACHE_ONSTOPCACHE: win32more.Windows.Win32.System.Ole.UPDFCACHE_FLAGS = 4
UPDFCACHE_IFBLANKORONSAVECACHE: win32more.Windows.Win32.System.Ole.UPDFCACHE_FLAGS = 18
USERCLASSTYPE = Int32
USERCLASSTYPE_FULL: win32more.Windows.Win32.System.Ole.USERCLASSTYPE = 1
USERCLASSTYPE_SHORT: win32more.Windows.Win32.System.Ole.USERCLASSTYPE = 2
USERCLASSTYPE_APPNAME: win32more.Windows.Win32.System.Ole.USERCLASSTYPE = 3
VARCMP = UInt32
VARCMP_LT: win32more.Windows.Win32.System.Ole.VARCMP = 0
VARCMP_EQ: win32more.Windows.Win32.System.Ole.VARCMP = 1
VARCMP_GT: win32more.Windows.Win32.System.Ole.VARCMP = 2
VARCMP_NULL: win32more.Windows.Win32.System.Ole.VARCMP = 3
VARFORMAT_FIRST_DAY = Int32
VARFORMAT_FIRST_DAY_SYSTEMDEFAULT: win32more.Windows.Win32.System.Ole.VARFORMAT_FIRST_DAY = 0
VARFORMAT_FIRST_DAY_MONDAY: win32more.Windows.Win32.System.Ole.VARFORMAT_FIRST_DAY = 1
VARFORMAT_FIRST_DAY_TUESDAY: win32more.Windows.Win32.System.Ole.VARFORMAT_FIRST_DAY = 2
VARFORMAT_FIRST_DAY_WEDNESDAY: win32more.Windows.Win32.System.Ole.VARFORMAT_FIRST_DAY = 3
VARFORMAT_FIRST_DAY_THURSDAY: win32more.Windows.Win32.System.Ole.VARFORMAT_FIRST_DAY = 4
VARFORMAT_FIRST_DAY_FRIDAY: win32more.Windows.Win32.System.Ole.VARFORMAT_FIRST_DAY = 5
VARFORMAT_FIRST_DAY_SATURDAY: win32more.Windows.Win32.System.Ole.VARFORMAT_FIRST_DAY = 6
VARFORMAT_FIRST_DAY_SUNDAY: win32more.Windows.Win32.System.Ole.VARFORMAT_FIRST_DAY = 7
VARFORMAT_FIRST_WEEK = Int32
VARFORMAT_FIRST_WEEK_SYSTEMDEFAULT: win32more.Windows.Win32.System.Ole.VARFORMAT_FIRST_WEEK = 0
VARFORMAT_FIRST_WEEK_CONTAINS_JANUARY_FIRST: win32more.Windows.Win32.System.Ole.VARFORMAT_FIRST_WEEK = 1
VARFORMAT_FIRST_WEEK_LARGER_HALF_IN_CURRENT_YEAR: win32more.Windows.Win32.System.Ole.VARFORMAT_FIRST_WEEK = 2
VARFORMAT_FIRST_WEEK_HAS_SEVEN_DAYS: win32more.Windows.Win32.System.Ole.VARFORMAT_FIRST_WEEK = 3
VARFORMAT_GROUP = Int32
VARFORMAT_GROUP_SYSTEMDEFAULT: win32more.Windows.Win32.System.Ole.VARFORMAT_GROUP = -2
VARFORMAT_GROUP_THOUSANDS: win32more.Windows.Win32.System.Ole.VARFORMAT_GROUP = -1
VARFORMAT_GROUP_NOTTHOUSANDS: win32more.Windows.Win32.System.Ole.VARFORMAT_GROUP = 0
VARFORMAT_LEADING_DIGIT = Int32
VARFORMAT_LEADING_DIGIT_SYSTEMDEFAULT: win32more.Windows.Win32.System.Ole.VARFORMAT_LEADING_DIGIT = -2
VARFORMAT_LEADING_DIGIT_INCLUDED: win32more.Windows.Win32.System.Ole.VARFORMAT_LEADING_DIGIT = -1
VARFORMAT_LEADING_DIGIT_NOTINCLUDED: win32more.Windows.Win32.System.Ole.VARFORMAT_LEADING_DIGIT = 0
VARFORMAT_NAMED_FORMAT = Int32
VARFORMAT_NAMED_FORMAT_GENERALDATE: win32more.Windows.Win32.System.Ole.VARFORMAT_NAMED_FORMAT = 0
VARFORMAT_NAMED_FORMAT_LONGDATE: win32more.Windows.Win32.System.Ole.VARFORMAT_NAMED_FORMAT = 1
VARFORMAT_NAMED_FORMAT_SHORTDATE: win32more.Windows.Win32.System.Ole.VARFORMAT_NAMED_FORMAT = 2
VARFORMAT_NAMED_FORMAT_LONGTIME: win32more.Windows.Win32.System.Ole.VARFORMAT_NAMED_FORMAT = 3
VARFORMAT_NAMED_FORMAT_SHORTTIME: win32more.Windows.Win32.System.Ole.VARFORMAT_NAMED_FORMAT = 4
VARFORMAT_PARENTHESES = Int32
VARFORMAT_PARENTHESES_SYSTEMDEFAULT: win32more.Windows.Win32.System.Ole.VARFORMAT_PARENTHESES = -2
VARFORMAT_PARENTHESES_USED: win32more.Windows.Win32.System.Ole.VARFORMAT_PARENTHESES = -1
VARFORMAT_PARENTHESES_NOTUSED: win32more.Windows.Win32.System.Ole.VARFORMAT_PARENTHESES = 0
VIEWSTATUS = Int32
VIEWSTATUS_OPAQUE: win32more.Windows.Win32.System.Ole.VIEWSTATUS = 1
VIEWSTATUS_SOLIDBKGND: win32more.Windows.Win32.System.Ole.VIEWSTATUS = 2
VIEWSTATUS_DVASPECTOPAQUE: win32more.Windows.Win32.System.Ole.VIEWSTATUS = 4
VIEWSTATUS_DVASPECTTRANSPARENT: win32more.Windows.Win32.System.Ole.VIEWSTATUS = 8
VIEWSTATUS_SURFACE: win32more.Windows.Win32.System.Ole.VIEWSTATUS = 16
VIEWSTATUS_3DSURFACE: win32more.Windows.Win32.System.Ole.VIEWSTATUS = 32
VIEW_OBJECT_PROPERTIES_FLAGS = UInt32
VPF_SELECTRELATIVE: win32more.Windows.Win32.System.Ole.VIEW_OBJECT_PROPERTIES_FLAGS = 1
VPF_DISABLERELATIVE: win32more.Windows.Win32.System.Ole.VIEW_OBJECT_PROPERTIES_FLAGS = 2
VPF_DISABLESCALE: win32more.Windows.Win32.System.Ole.VIEW_OBJECT_PROPERTIES_FLAGS = 4
WPCSETTING = Int32
WPCSETTING_LOGGING_ENABLED: win32more.Windows.Win32.System.Ole.WPCSETTING = 1
WPCSETTING_FILEDOWNLOAD_BLOCKED: win32more.Windows.Win32.System.Ole.WPCSETTING = 2
XFORMCOORDS = Int32
XFORMCOORDS_POSITION: win32more.Windows.Win32.System.Ole.XFORMCOORDS = 1
XFORMCOORDS_SIZE: win32more.Windows.Win32.System.Ole.XFORMCOORDS = 2
XFORMCOORDS_HIMETRICTOCONTAINER: win32more.Windows.Win32.System.Ole.XFORMCOORDS = 4
XFORMCOORDS_CONTAINERTOHIMETRIC: win32more.Windows.Win32.System.Ole.XFORMCOORDS = 8
XFORMCOORDS_EVENTCOMPAT: win32more.Windows.Win32.System.Ole.XFORMCOORDS = 16
class _wireBRECORD(Structure):
    fFlags: UInt32
    clSize: UInt32
    pRecInfo: win32more.Windows.Win32.System.Ole.IRecordInfo
    pRecord: POINTER(Byte)
class _wireSAFEARRAY(Structure):
    cDims: UInt16
    fFeatures: UInt16
    cbElements: UInt32
    cLocks: UInt32
    uArrayStructs: win32more.Windows.Win32.System.Ole.SAFEARRAYUNION
    rgsabound: win32more.Windows.Win32.System.Com.SAFEARRAYBOUND * 1
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
        boolVal: win32more.Windows.Win32.Foundation.VARIANT_BOOL
        scode: Int32
        cyVal: win32more.Windows.Win32.System.Com.CY
        date: Double
        bstrVal: POINTER(win32more.Windows.Win32.System.Com.FLAGGED_WORD_BLOB)
        punkVal: win32more.Windows.Win32.System.Com.IUnknown
        pdispVal: win32more.Windows.Win32.System.Com.IDispatch
        parray: POINTER(POINTER(win32more.Windows.Win32.System.Ole._wireSAFEARRAY))
        brecVal: POINTER(win32more.Windows.Win32.System.Ole._wireBRECORD)
        pbVal: POINTER(Byte)
        piVal: POINTER(Int16)
        plVal: POINTER(Int32)
        pllVal: POINTER(Int64)
        pfltVal: POINTER(Single)
        pdblVal: POINTER(Double)
        pboolVal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)
        pscode: POINTER(Int32)
        pcyVal: POINTER(win32more.Windows.Win32.System.Com.CY)
        pdate: POINTER(Double)
        pbstrVal: POINTER(POINTER(win32more.Windows.Win32.System.Com.FLAGGED_WORD_BLOB))
        ppunkVal: POINTER(win32more.Windows.Win32.System.Com.IUnknown)
        ppdispVal: POINTER(win32more.Windows.Win32.System.Com.IDispatch)
        pparray: POINTER(POINTER(POINTER(win32more.Windows.Win32.System.Ole._wireSAFEARRAY)))
        pvarVal: POINTER(POINTER(win32more.Windows.Win32.System.Ole._wireVARIANT))
        cVal: win32more.Windows.Win32.Foundation.CHAR
        uiVal: UInt16
        ulVal: UInt32
        ullVal: UInt64
        intVal: Int32
        uintVal: UInt32
        decVal: win32more.Windows.Win32.Foundation.DECIMAL
        pdecVal: POINTER(win32more.Windows.Win32.Foundation.DECIMAL)
        pcVal: win32more.Windows.Win32.Foundation.PSTR
        puiVal: POINTER(UInt16)
        pulVal: POINTER(UInt32)
        pullVal: POINTER(UInt64)
        pintVal: POINTER(Int32)
        puintVal: POINTER(UInt32)


make_ready(__name__)
