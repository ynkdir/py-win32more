from win32more import *
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.Media
import win32more.System.Com
import win32more.System.Com.StructuredStorage
import win32more.System.Ole
import win32more.UI.Controls
import win32more.UI.Controls.Dialogs
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
CTL_E_ILLEGALFUNCTIONCALL = -2146828283
CONNECT_E_FIRST = -2147220992
SELFREG_E_FIRST = -2147220992
PERPROP_E_FIRST = -2147220992
OLECMDERR_E_FIRST = -2147221248
OLECMDERR_E_DISABLED = -2147221247
OLECMDERR_E_NOHELP = -2147221246
OLECMDERR_E_CANCELED = -2147221245
OLECMDERR_E_UNKNOWNGROUP = -2147221244
CONNECT_E_NOCONNECTION = -2147220992
CONNECT_E_ADVISELIMIT = -2147220991
CONNECT_E_CANNOTCONNECT = -2147220990
CONNECT_E_OVERRIDDEN = -2147220989
SELFREG_E_TYPELIB = -2147220992
SELFREG_E_CLASS = -2147220991
PERPROP_E_NOPAGEAVAILABLE = -2147220992
CLSID_CFontPropPage = '0be35200-8f91-11ce-9de3-00aa004bb851'
CLSID_CColorPropPage = '0be35201-8f91-11ce-9de3-00aa004bb851'
CLSID_CPicturePropPage = '0be35202-8f91-11ce-9de3-00aa004bb851'
CLSID_PersistPropset = 'fb8f0821-0164-101b-84ed-08002b2ec713'
CLSID_ConvertVBX = 'fb8f0822-0164-101b-84ed-08002b2ec713'
CLSID_StdFont = '0be35203-8f91-11ce-9de3-00aa004bb851'
CLSID_StdPicture = '0be35204-8f91-11ce-9de3-00aa004bb851'
GUID_HIMETRIC = '66504300-be0f-101a-8bbb-00aa00300cab'
GUID_COLOR = '66504301-be0f-101a-8bbb-00aa00300cab'
GUID_XPOSPIXEL = '66504302-be0f-101a-8bbb-00aa00300cab'
GUID_YPOSPIXEL = '66504303-be0f-101a-8bbb-00aa00300cab'
GUID_XSIZEPIXEL = '66504304-be0f-101a-8bbb-00aa00300cab'
GUID_YSIZEPIXEL = '66504305-be0f-101a-8bbb-00aa00300cab'
GUID_XPOS = '66504306-be0f-101a-8bbb-00aa00300cab'
GUID_YPOS = '66504307-be0f-101a-8bbb-00aa00300cab'
GUID_XSIZE = '66504308-be0f-101a-8bbb-00aa00300cab'
GUID_YSIZE = '66504309-be0f-101a-8bbb-00aa00300cab'
GUID_TRISTATE = '6650430a-be0f-101a-8bbb-00aa00300cab'
GUID_OPTIONVALUEEXCLUSIVE = '6650430b-be0f-101a-8bbb-00aa00300cab'
GUID_CHECKVALUEEXCLUSIVE = '6650430c-be0f-101a-8bbb-00aa00300cab'
GUID_FONTNAME = '6650430d-be0f-101a-8bbb-00aa00300cab'
GUID_FONTSIZE = '6650430e-be0f-101a-8bbb-00aa00300cab'
GUID_FONTBOLD = '6650430f-be0f-101a-8bbb-00aa00300cab'
GUID_FONTITALIC = '66504310-be0f-101a-8bbb-00aa00300cab'
GUID_FONTUNDERSCORE = '66504311-be0f-101a-8bbb-00aa00300cab'
GUID_FONTSTRIKETHROUGH = '66504312-be0f-101a-8bbb-00aa00300cab'
GUID_HANDLE = '66504313-be0f-101a-8bbb-00aa00300cab'
PICTYPE_UNINITIALIZED = -1
PICTYPE_NONE = 0
PICTYPE_BITMAP = 1
PICTYPE_METAFILE = 2
PICTYPE_ICON = 3
PICTYPE_ENHMETAFILE = 4
CONNECT_E_LAST = -2147220977
CONNECT_S_FIRST = 262656
CONNECT_S_LAST = 262671
SELFREG_E_LAST = -2147220977
SELFREG_S_FIRST = 262656
SELFREG_S_LAST = 262671
PERPROP_E_LAST = -2147220977
PERPROP_S_FIRST = 262656
PERPROP_S_LAST = 262671
OLEIVERB_PROPERTIES = -7
VT_STREAMED_PROPSET = 73
VT_STORED_PROPSET = 74
VT_BLOB_PROPSET = 75
VT_VERBOSE_ENUM = 76
OCM__BASE = 8192
LP_DEFAULT = 0
LP_MONOCHROME = 1
LP_VGACOLOR = 2
LP_COLOR = 4
DISPID_AUTOSIZE = -500
DISPID_BACKCOLOR = -501
DISPID_BACKSTYLE = -502
DISPID_BORDERCOLOR = -503
DISPID_BORDERSTYLE = -504
DISPID_BORDERWIDTH = -505
DISPID_DRAWMODE = -507
DISPID_DRAWSTYLE = -508
DISPID_DRAWWIDTH = -509
DISPID_FILLCOLOR = -510
DISPID_FILLSTYLE = -511
DISPID_FONT = -512
DISPID_FORECOLOR = -513
DISPID_ENABLED = -514
DISPID_HWND = -515
DISPID_TABSTOP = -516
DISPID_TEXT = -517
DISPID_CAPTION = -518
DISPID_BORDERVISIBLE = -519
DISPID_APPEARANCE = -520
DISPID_MOUSEPOINTER = -521
DISPID_MOUSEICON = -522
DISPID_PICTURE = -523
DISPID_VALID = -524
DISPID_READYSTATE = -525
DISPID_LISTINDEX = -526
DISPID_SELECTED = -527
DISPID_LIST = -528
DISPID_COLUMN = -529
DISPID_LISTCOUNT = -531
DISPID_MULTISELECT = -532
DISPID_MAXLENGTH = -533
DISPID_PASSWORDCHAR = -534
DISPID_SCROLLBARS = -535
DISPID_WORDWRAP = -536
DISPID_MULTILINE = -537
DISPID_NUMBEROFROWS = -538
DISPID_NUMBEROFCOLUMNS = -539
DISPID_DISPLAYSTYLE = -540
DISPID_GROUPNAME = -541
DISPID_IMEMODE = -542
DISPID_ACCELERATOR = -543
DISPID_ENTERKEYBEHAVIOR = -544
DISPID_TABKEYBEHAVIOR = -545
DISPID_SELTEXT = -546
DISPID_SELSTART = -547
DISPID_SELLENGTH = -548
DISPID_REFRESH = -550
DISPID_DOCLICK = -551
DISPID_ABOUTBOX = -552
DISPID_ADDITEM = -553
DISPID_CLEAR = -554
DISPID_REMOVEITEM = -555
DISPID_CLICK = -600
DISPID_DBLCLICK = -601
DISPID_KEYDOWN = -602
DISPID_KEYPRESS = -603
DISPID_KEYUP = -604
DISPID_MOUSEDOWN = -605
DISPID_MOUSEMOVE = -606
DISPID_MOUSEUP = -607
DISPID_ERROREVENT = -608
DISPID_READYSTATECHANGE = -609
DISPID_CLICK_VALUE = -610
DISPID_RIGHTTOLEFT = -611
DISPID_TOPTOBOTTOM = -612
DISPID_THIS = -613
DISPID_AMBIENT_BACKCOLOR = -701
DISPID_AMBIENT_DISPLAYNAME = -702
DISPID_AMBIENT_FONT = -703
DISPID_AMBIENT_FORECOLOR = -704
DISPID_AMBIENT_LOCALEID = -705
DISPID_AMBIENT_MESSAGEREFLECT = -706
DISPID_AMBIENT_SCALEUNITS = -707
DISPID_AMBIENT_TEXTALIGN = -708
DISPID_AMBIENT_USERMODE = -709
DISPID_AMBIENT_UIDEAD = -710
DISPID_AMBIENT_SHOWGRABHANDLES = -711
DISPID_AMBIENT_SHOWHATCHING = -712
DISPID_AMBIENT_DISPLAYASDEFAULT = -713
DISPID_AMBIENT_SUPPORTSMNEMONICS = -714
DISPID_AMBIENT_AUTOCLIP = -715
DISPID_AMBIENT_APPEARANCE = -716
DISPID_AMBIENT_CODEPAGE = -725
DISPID_AMBIENT_PALETTE = -726
DISPID_AMBIENT_CHARSET = -727
DISPID_AMBIENT_TRANSFERPRIORITY = -728
DISPID_AMBIENT_RIGHTTOLEFT = -732
DISPID_AMBIENT_TOPTOBOTTOM = -733
DISPID_Name = -800
DISPID_Delete = -801
DISPID_Object = -802
DISPID_Parent = -803
DISPID_FONT_NAME = 0
DISPID_FONT_SIZE = 2
DISPID_FONT_BOLD = 3
DISPID_FONT_ITALIC = 4
DISPID_FONT_UNDER = 5
DISPID_FONT_STRIKE = 6
DISPID_FONT_WEIGHT = 7
DISPID_FONT_CHARSET = 8
DISPID_FONT_CHANGED = 9
DISPID_PICT_HANDLE = 0
DISPID_PICT_HPAL = 2
DISPID_PICT_TYPE = 3
DISPID_PICT_WIDTH = 4
DISPID_PICT_HEIGHT = 5
DISPID_PICT_RENDER = 6
GC_WCH_SIBLING = 1
TIFLAGS_EXTENDDISPATCHONLY = 1
OLECMDERR_E_NOTSUPPORTED = -2147221248
MSOCMDERR_E_FIRST = -2147221248
MSOCMDERR_E_NOTSUPPORTED = -2147221248
MSOCMDERR_E_DISABLED = -2147221247
MSOCMDERR_E_NOHELP = -2147221246
MSOCMDERR_E_CANCELED = -2147221245
MSOCMDERR_E_UNKNOWNGROUP = -2147221244
OLECMD_TASKDLGID_ONBEFOREUNLOAD = 1
OLECMDARGINDEX_SHOWPAGEACTIONMENU_HWND = 0
OLECMDARGINDEX_SHOWPAGEACTIONMENU_X = 1
OLECMDARGINDEX_SHOWPAGEACTIONMENU_Y = 2
OLECMDARGINDEX_ACTIVEXINSTALL_PUBLISHER = 0
OLECMDARGINDEX_ACTIVEXINSTALL_DISPLAYNAME = 1
OLECMDARGINDEX_ACTIVEXINSTALL_CLSID = 2
OLECMDARGINDEX_ACTIVEXINSTALL_INSTALLSCOPE = 3
OLECMDARGINDEX_ACTIVEXINSTALL_SOURCEURL = 4
INSTALL_SCOPE_INVALID = 0
INSTALL_SCOPE_MACHINE = 1
INSTALL_SCOPE_USER = 2
MK_ALT = 32
DROPEFFECT_NONE = 0
DROPEFFECT_COPY = 1
DROPEFFECT_MOVE = 2
DROPEFFECT_LINK = 4
DROPEFFECT_SCROLL = 2147483648
DD_DEFSCROLLINSET = 11
DD_DEFSCROLLDELAY = 50
DD_DEFSCROLLINTERVAL = 50
DD_DEFDRAGDELAY = 200
DD_DEFDRAGMINDIST = 2
OT_LINK = 1
OT_EMBEDDED = 2
OT_STATIC = 3
OLEVERB_PRIMARY = 0
OF_SET = 1
OF_GET = 2
OF_HANDLER = 4
WIN32 = 100
OLEIVERB_PRIMARY = 0
OLEIVERB_SHOW = -1
OLEIVERB_OPEN = -2
OLEIVERB_HIDE = -3
OLEIVERB_UIACTIVATE = -4
OLEIVERB_INPLACEACTIVATE = -5
OLEIVERB_DISCARDUNDOSTATE = -6
EMBDHLP_INPROC_HANDLER = 0
EMBDHLP_INPROC_SERVER = 1
EMBDHLP_CREATENOW = 0
EMBDHLP_DELAYCREATE = 65536
OLECREATE_LEAVERUNNING = 1
IDC_OLEUIHELP = 99
IDC_IO_CREATENEW = 2100
IDC_IO_CREATEFROMFILE = 2101
IDC_IO_LINKFILE = 2102
IDC_IO_OBJECTTYPELIST = 2103
IDC_IO_DISPLAYASICON = 2104
IDC_IO_CHANGEICON = 2105
IDC_IO_FILE = 2106
IDC_IO_FILEDISPLAY = 2107
IDC_IO_RESULTIMAGE = 2108
IDC_IO_RESULTTEXT = 2109
IDC_IO_ICONDISPLAY = 2110
IDC_IO_OBJECTTYPETEXT = 2111
IDC_IO_FILETEXT = 2112
IDC_IO_FILETYPE = 2113
IDC_IO_INSERTCONTROL = 2114
IDC_IO_ADDCONTROL = 2115
IDC_IO_CONTROLTYPELIST = 2116
IDC_PS_PASTE = 500
IDC_PS_PASTELINK = 501
IDC_PS_SOURCETEXT = 502
IDC_PS_PASTELIST = 503
IDC_PS_PASTELINKLIST = 504
IDC_PS_DISPLAYLIST = 505
IDC_PS_DISPLAYASICON = 506
IDC_PS_ICONDISPLAY = 507
IDC_PS_CHANGEICON = 508
IDC_PS_RESULTIMAGE = 509
IDC_PS_RESULTTEXT = 510
IDC_CI_GROUP = 120
IDC_CI_CURRENT = 121
IDC_CI_CURRENTICON = 122
IDC_CI_DEFAULT = 123
IDC_CI_DEFAULTICON = 124
IDC_CI_FROMFILE = 125
IDC_CI_FROMFILEEDIT = 126
IDC_CI_ICONLIST = 127
IDC_CI_LABEL = 128
IDC_CI_LABELEDIT = 129
IDC_CI_BROWSE = 130
IDC_CI_ICONDISPLAY = 131
IDC_CV_OBJECTTYPE = 150
IDC_CV_DISPLAYASICON = 152
IDC_CV_CHANGEICON = 153
IDC_CV_ACTIVATELIST = 154
IDC_CV_CONVERTTO = 155
IDC_CV_ACTIVATEAS = 156
IDC_CV_RESULTTEXT = 157
IDC_CV_CONVERTLIST = 158
IDC_CV_ICONDISPLAY = 165
IDC_EL_CHANGESOURCE = 201
IDC_EL_AUTOMATIC = 202
IDC_EL_CANCELLINK = 209
IDC_EL_UPDATENOW = 210
IDC_EL_OPENSOURCE = 211
IDC_EL_MANUAL = 212
IDC_EL_LINKSOURCE = 216
IDC_EL_LINKTYPE = 217
IDC_EL_LINKSLISTBOX = 206
IDC_EL_COL1 = 220
IDC_EL_COL2 = 221
IDC_EL_COL3 = 222
IDC_BZ_RETRY = 600
IDC_BZ_ICON = 601
IDC_BZ_MESSAGE1 = 602
IDC_BZ_SWITCHTO = 604
IDC_UL_METER = 1029
IDC_UL_STOP = 1030
IDC_UL_PERCENT = 1031
IDC_UL_PROGRESS = 1032
IDC_PU_LINKS = 900
IDC_PU_TEXT = 901
IDC_PU_CONVERT = 902
IDC_PU_ICON = 908
IDC_GP_OBJECTNAME = 1009
IDC_GP_OBJECTTYPE = 1010
IDC_GP_OBJECTSIZE = 1011
IDC_GP_CONVERT = 1013
IDC_GP_OBJECTICON = 1014
IDC_GP_OBJECTLOCATION = 1022
IDC_VP_PERCENT = 1000
IDC_VP_CHANGEICON = 1001
IDC_VP_EDITABLE = 1002
IDC_VP_ASICON = 1003
IDC_VP_RELATIVE = 1005
IDC_VP_SPIN = 1006
IDC_VP_SCALETXT = 1034
IDC_VP_ICONDISPLAY = 1021
IDC_VP_RESULTIMAGE = 1033
IDC_LP_OPENSOURCE = 1006
IDC_LP_UPDATENOW = 1007
IDC_LP_BREAKLINK = 1008
IDC_LP_LINKSOURCE = 1012
IDC_LP_CHANGESOURCE = 1015
IDC_LP_AUTOMATIC = 1016
IDC_LP_MANUAL = 1017
IDC_LP_DATE = 1018
IDC_LP_TIME = 1019
IDD_INSERTOBJECT = 1000
IDD_CHANGEICON = 1001
IDD_CONVERT = 1002
IDD_PASTESPECIAL = 1003
IDD_EDITLINKS = 1004
IDD_BUSY = 1006
IDD_UPDATELINKS = 1007
IDD_CHANGESOURCE = 1009
IDD_INSERTFILEBROWSE = 1010
IDD_CHANGEICONBROWSE = 1011
IDD_CONVERTONLY = 1012
IDD_CHANGESOURCE4 = 1013
IDD_GNRLPROPS = 1100
IDD_VIEWPROPS = 1101
IDD_LINKPROPS = 1102
IDD_CONVERT4 = 1103
IDD_CONVERTONLY4 = 1104
IDD_EDITLINKS4 = 1105
IDD_GNRLPROPS4 = 1106
IDD_LINKPROPS4 = 1107
IDD_PASTESPECIAL4 = 1108
IDD_CANNOTUPDATELINK = 1008
IDD_LINKSOURCEUNAVAILABLE = 1020
IDD_SERVERNOTFOUND = 1023
IDD_OUTOFMEMORY = 1024
IDD_SERVERNOTREGW = 1021
IDD_LINKTYPECHANGEDW = 1022
IDD_SERVERNOTREGA = 1025
IDD_LINKTYPECHANGEDA = 1026
IDD_SERVERNOTREG = 1021
IDD_LINKTYPECHANGED = 1022
ID_BROWSE_CHANGEICON = 1
ID_BROWSE_INSERTFILE = 2
ID_BROWSE_ADDCONTROL = 3
ID_BROWSE_CHANGESOURCE = 4
OLEUI_FALSE = 0
OLEUI_SUCCESS = 1
OLEUI_OK = 1
OLEUI_CANCEL = 2
OLEUI_ERR_STANDARDMIN = 100
OLEUI_ERR_OLEMEMALLOC = 100
OLEUI_ERR_STRUCTURENULL = 101
OLEUI_ERR_STRUCTUREINVALID = 102
OLEUI_ERR_CBSTRUCTINCORRECT = 103
OLEUI_ERR_HWNDOWNERINVALID = 104
OLEUI_ERR_LPSZCAPTIONINVALID = 105
OLEUI_ERR_LPFNHOOKINVALID = 106
OLEUI_ERR_HINSTANCEINVALID = 107
OLEUI_ERR_LPSZTEMPLATEINVALID = 108
OLEUI_ERR_HRESOURCEINVALID = 109
OLEUI_ERR_FINDTEMPLATEFAILURE = 110
OLEUI_ERR_LOADTEMPLATEFAILURE = 111
OLEUI_ERR_DIALOGFAILURE = 112
OLEUI_ERR_LOCALMEMALLOC = 113
OLEUI_ERR_GLOBALMEMALLOC = 114
OLEUI_ERR_LOADSTRING = 115
OLEUI_ERR_STANDARDMAX = 116
IOF_SHOWHELP = 1
IOF_SELECTCREATENEW = 2
IOF_SELECTCREATEFROMFILE = 4
IOF_CHECKLINK = 8
IOF_CHECKDISPLAYASICON = 16
IOF_CREATENEWOBJECT = 32
IOF_CREATEFILEOBJECT = 64
IOF_CREATELINKOBJECT = 128
IOF_DISABLELINK = 256
IOF_VERIFYSERVERSEXIST = 512
IOF_DISABLEDISPLAYASICON = 1024
IOF_HIDECHANGEICON = 2048
IOF_SHOWINSERTCONTROL = 4096
IOF_SELECTCREATECONTROL = 8192
OLEUI_IOERR_LPSZFILEINVALID = 116
OLEUI_IOERR_LPSZLABELINVALID = 117
OLEUI_IOERR_HICONINVALID = 118
OLEUI_IOERR_LPFORMATETCINVALID = 119
OLEUI_IOERR_PPVOBJINVALID = 120
OLEUI_IOERR_LPIOLECLIENTSITEINVALID = 121
OLEUI_IOERR_LPISTORAGEINVALID = 122
OLEUI_IOERR_SCODEHASERROR = 123
OLEUI_IOERR_LPCLSIDEXCLUDEINVALID = 124
OLEUI_IOERR_CCHFILEINVALID = 125
PS_MAXLINKTYPES = 8
PSF_SHOWHELP = 1
PSF_SELECTPASTE = 2
PSF_SELECTPASTELINK = 4
PSF_CHECKDISPLAYASICON = 8
PSF_DISABLEDISPLAYASICON = 16
PSF_HIDECHANGEICON = 32
PSF_STAYONCLIPBOARDCHANGE = 64
PSF_NOREFRESHDATAOBJECT = 128
OLEUI_IOERR_SRCDATAOBJECTINVALID = 116
OLEUI_IOERR_ARRPASTEENTRIESINVALID = 117
OLEUI_IOERR_ARRLINKTYPESINVALID = 118
OLEUI_PSERR_CLIPBOARDCHANGED = 119
OLEUI_PSERR_GETCLIPBOARDFAILED = 120
OLEUI_ELERR_LINKCNTRNULL = 116
OLEUI_ELERR_LINKCNTRINVALID = 117
ELF_SHOWHELP = 1
ELF_DISABLEUPDATENOW = 2
ELF_DISABLEOPENSOURCE = 4
ELF_DISABLECHANGESOURCE = 8
ELF_DISABLECANCELLINK = 16
CIF_SHOWHELP = 1
CIF_SELECTCURRENT = 2
CIF_SELECTDEFAULT = 4
CIF_SELECTFROMFILE = 8
CIF_USEICONEXE = 16
OLEUI_CIERR_MUSTHAVECLSID = 116
OLEUI_CIERR_MUSTHAVECURRENTMETAFILE = 117
OLEUI_CIERR_SZICONEXEINVALID = 118
CF_SHOWHELPBUTTON = 1
CF_SETCONVERTDEFAULT = 2
CF_SETACTIVATEDEFAULT = 4
CF_SELECTCONVERTTO = 8
CF_SELECTACTIVATEAS = 16
CF_DISABLEDISPLAYASICON = 32
CF_DISABLEACTIVATEAS = 64
CF_HIDECHANGEICON = 128
CF_CONVERTONLY = 256
OLEUI_CTERR_CLASSIDINVALID = 117
OLEUI_CTERR_DVASPECTINVALID = 118
OLEUI_CTERR_CBFORMATINVALID = 119
OLEUI_CTERR_HMETAPICTINVALID = 120
OLEUI_CTERR_STRINGINVALID = 121
BZ_DISABLECANCELBUTTON = 1
BZ_DISABLESWITCHTOBUTTON = 2
BZ_DISABLERETRYBUTTON = 4
BZ_NOTRESPONDINGDIALOG = 8
OLEUI_BZERR_HTASKINVALID = 116
OLEUI_BZ_SWITCHTOSELECTED = 117
OLEUI_BZ_RETRYSELECTED = 118
OLEUI_BZ_CALLUNBLOCKED = 119
CSF_SHOWHELP = 1
CSF_VALIDSOURCE = 2
CSF_ONLYGETSOURCE = 4
CSF_EXPLORER = 8
OLEUI_CSERR_LINKCNTRNULL = 116
OLEUI_CSERR_LINKCNTRINVALID = 117
OLEUI_CSERR_FROMNOTNULL = 118
OLEUI_CSERR_TONOTNULL = 119
OLEUI_CSERR_SOURCENULL = 120
OLEUI_CSERR_SOURCEINVALID = 121
OLEUI_CSERR_SOURCEPARSERROR = 122
OLEUI_CSERR_SOURCEPARSEERROR = 122
VPF_SELECTRELATIVE = 1
VPF_DISABLERELATIVE = 2
VPF_DISABLESCALE = 4
OPF_OBJECTISLINK = 1
OPF_NOFILLDEFAULT = 2
OPF_SHOWHELP = 4
OPF_DISABLECONVERT = 8
OLEUI_OPERR_SUBPROPNULL = 116
OLEUI_OPERR_SUBPROPINVALID = 117
OLEUI_OPERR_PROPSHEETNULL = 118
OLEUI_OPERR_PROPSHEETINVALID = 119
OLEUI_OPERR_SUPPROP = 120
OLEUI_OPERR_PROPSINVALID = 121
OLEUI_OPERR_PAGESINCORRECT = 122
OLEUI_OPERR_INVALIDPAGES = 123
OLEUI_OPERR_NOTSUPPORTED = 124
OLEUI_OPERR_DLGPROCNOTNULL = 125
OLEUI_OPERR_LPARAMNOTZERO = 126
OLEUI_GPERR_STRINGINVALID = 127
OLEUI_GPERR_CLASSIDINVALID = 128
OLEUI_GPERR_LPCLSIDEXCLUDEINVALID = 129
OLEUI_GPERR_CBFORMATINVALID = 130
OLEUI_VPERR_METAPICTINVALID = 131
OLEUI_VPERR_DVASPECTINVALID = 132
OLEUI_LPERR_LINKCNTRNULL = 133
OLEUI_LPERR_LINKCNTRINVALID = 134
OLEUI_OPERR_PROPERTYSHEET = 135
OLEUI_OPERR_OBJINFOINVALID = 136
OLEUI_OPERR_LINKINFOINVALID = 137
OLEUI_QUERY_GETCLASSID = 65280
OLEUI_QUERY_LINKBROKEN = 65281
FADF_AUTO = 1
FADF_STATIC = 2
FADF_EMBEDDED = 4
FADF_FIXEDSIZE = 16
FADF_RECORD = 32
FADF_HAVEIID = 64
FADF_HAVEVARTYPE = 128
FADF_BSTR = 256
FADF_UNKNOWN = 512
FADF_DISPATCH = 1024
FADF_VARIANT = 2048
FADF_RESERVED = 61448
PARAMFLAG_NONE = 0
PARAMFLAG_FIN = 1
PARAMFLAG_FOUT = 2
PARAMFLAG_FLCID = 4
PARAMFLAG_FRETVAL = 8
PARAMFLAG_FOPT = 16
PARAMFLAG_FHASDEFAULT = 32
PARAMFLAG_FHASCUSTDATA = 64
IDLFLAG_NONE = 0
IDLFLAG_FIN = 1
IDLFLAG_FOUT = 2
IDLFLAG_FLCID = 4
IDLFLAG_FRETVAL = 8
IMPLTYPEFLAG_FDEFAULT = 1
IMPLTYPEFLAG_FSOURCE = 2
IMPLTYPEFLAG_FRESTRICTED = 4
IMPLTYPEFLAG_FDEFAULTVTABLE = 8
DISPID_UNKNOWN = -1
DISPID_VALUE = 0
DISPID_PROPERTYPUT = -3
DISPID_NEWENUM = -4
DISPID_EVALUATE = -5
DISPID_CONSTRUCTOR = -6
DISPID_DESTRUCTOR = -7
DISPID_COLLECT = -8
STDOLE_MAJORVERNUM = 1
STDOLE_MINORVERNUM = 0
STDOLE_LCID = 0
STDOLE2_MAJORVERNUM = 2
STDOLE2_MINORVERNUM = 0
STDOLE2_LCID = 0
VARIANT_NOVALUEPROP = 1
VARIANT_ALPHABOOL = 2
VARIANT_NOUSEROVERRIDE = 4
VARIANT_CALENDAR_HIJRI = 8
VARIANT_LOCALBOOL = 16
VARIANT_CALENDAR_THAI = 32
VARIANT_CALENDAR_GREGORIAN = 64
VARIANT_USE_NLS = 128
LOCALE_USE_NLS = 268435456
VTDATEGRE_MAX = 2958465
VTDATEGRE_MIN = -657434
NUMPRS_LEADING_WHITE = 1
NUMPRS_TRAILING_WHITE = 2
NUMPRS_LEADING_PLUS = 4
NUMPRS_TRAILING_PLUS = 8
NUMPRS_LEADING_MINUS = 16
NUMPRS_TRAILING_MINUS = 32
NUMPRS_HEX_OCT = 64
NUMPRS_PARENS = 128
NUMPRS_DECIMAL = 256
NUMPRS_THOUSANDS = 512
NUMPRS_CURRENCY = 1024
NUMPRS_EXPONENT = 2048
NUMPRS_USE_ALL = 4096
NUMPRS_STD = 8191
NUMPRS_NEG = 65536
NUMPRS_INEXACT = 131072
VARCMP_LT = 0
VARCMP_EQ = 1
VARCMP_GT = 2
VARCMP_NULL = 3
MEMBERID_NIL = -1
ID_DEFAULTINST = -2
DISPATCH_METHOD = 1
DISPATCH_PROPERTYGET = 2
DISPATCH_PROPERTYPUT = 4
DISPATCH_PROPERTYPUTREF = 8
LOAD_TLB_AS_32BIT = 32
LOAD_TLB_AS_64BIT = 64
ACTIVEOBJECT_STRONG = 0
ACTIVEOBJECT_WEAK = 1
DISPATCH_CONSTRUCT = 16384
DISPID_STARTENUM = -1
SID_VariantConversion = '1f101481-bccd-11d0-9336-00a0c90dcaa9'
SID_GetCaller = '4717cc40-bcb9-11d0-9336-00a0c90dcaa9'
SID_ProvideRuntimeContext = '74a5040c-dd0c-48f0-ac85-194c3259180a'
UPDFCACHE_FLAGS = UInt32
UPDFCACHE_ALL = 2147483647
UPDFCACHE_ALLBUTNODATACACHE = 2147483646
UPDFCACHE_NORMALCACHE = 8
UPDFCACHE_IFBLANK = 16
UPDFCACHE_ONLYIFBLANK = 2147483648
UPDFCACHE_NODATACACHE = 1
UPDFCACHE_ONSAVECACHE = 2
UPDFCACHE_ONSTOPCACHE = 4
UPDFCACHE_IFBLANKORONSAVECACHE = 18
ENUM_CONTROLS_WHICH_FLAGS = UInt32
GCW_WCH_SIBLING = 1
GC_WCH_CONTAINER = 2
GC_WCH_CONTAINED = 3
GC_WCH_ALL = 4
GC_WCH_FREVERSEDIR = 134217728
GC_WCH_FONLYAFTER = 268435456
GC_WCH_FONLYBEFORE = 536870912
GC_WCH_FSELECTED = 1073741824
MULTICLASSINFO_FLAGS = UInt32
MULTICLASSINFO_GETTYPEINFO = 1
MULTICLASSINFO_GETNUMRESERVEDDISPIDS = 2
MULTICLASSINFO_GETIIDPRIMARY = 4
MULTICLASSINFO_GETIIDSOURCE = 8
VARENUM = Int32
VT_EMPTY = 0
VT_NULL = 1
VT_I2 = 2
VT_I4 = 3
VT_R4 = 4
VT_R8 = 5
VT_CY = 6
VT_DATE = 7
VT_BSTR = 8
VT_DISPATCH = 9
VT_ERROR = 10
VT_BOOL = 11
VT_VARIANT = 12
VT_UNKNOWN = 13
VT_DECIMAL = 14
VT_I1 = 16
VT_UI1 = 17
VT_UI2 = 18
VT_UI4 = 19
VT_I8 = 20
VT_UI8 = 21
VT_INT = 22
VT_UINT = 23
VT_VOID = 24
VT_HRESULT = 25
VT_PTR = 26
VT_SAFEARRAY = 27
VT_CARRAY = 28
VT_USERDEFINED = 29
VT_LPSTR = 30
VT_LPWSTR = 31
VT_RECORD = 36
VT_INT_PTR = 37
VT_UINT_PTR = 38
VT_FILETIME = 64
VT_BLOB = 65
VT_STREAM = 66
VT_STORAGE = 67
VT_STREAMED_OBJECT = 68
VT_STORED_OBJECT = 69
VT_BLOB_OBJECT = 70
VT_CF = 71
VT_CLSID = 72
VT_VERSIONED_STREAM = 73
VT_BSTR_BLOB = 4095
VT_VECTOR = 4096
VT_ARRAY = 8192
VT_BYREF = 16384
VT_RESERVED = 32768
VT_ILLEGAL = 65535
VT_ILLEGALMASKED = 4095
VT_TYPEMASK = 4095
def _define__wireSAFEARR_BSTR_head():
    class _wireSAFEARR_BSTR(Structure):
        pass
    return _wireSAFEARR_BSTR
def _define__wireSAFEARR_BSTR():
    _wireSAFEARR_BSTR = win32more.System.Ole._wireSAFEARR_BSTR_head
    _wireSAFEARR_BSTR._fields_ = [
        ("Size", UInt32),
        ("aBstr", POINTER(POINTER(win32more.System.Com.FLAGGED_WORD_BLOB_head))),
    ]
    return _wireSAFEARR_BSTR
def _define__wireSAFEARR_UNKNOWN_head():
    class _wireSAFEARR_UNKNOWN(Structure):
        pass
    return _wireSAFEARR_UNKNOWN
def _define__wireSAFEARR_UNKNOWN():
    _wireSAFEARR_UNKNOWN = win32more.System.Ole._wireSAFEARR_UNKNOWN_head
    _wireSAFEARR_UNKNOWN._fields_ = [
        ("Size", UInt32),
        ("apUnknown", POINTER(win32more.System.Com.IUnknown_head)),
    ]
    return _wireSAFEARR_UNKNOWN
def _define__wireSAFEARR_DISPATCH_head():
    class _wireSAFEARR_DISPATCH(Structure):
        pass
    return _wireSAFEARR_DISPATCH
def _define__wireSAFEARR_DISPATCH():
    _wireSAFEARR_DISPATCH = win32more.System.Ole._wireSAFEARR_DISPATCH_head
    _wireSAFEARR_DISPATCH._fields_ = [
        ("Size", UInt32),
        ("apDispatch", POINTER(win32more.System.Com.IDispatch_head)),
    ]
    return _wireSAFEARR_DISPATCH
def _define__wireSAFEARR_VARIANT_head():
    class _wireSAFEARR_VARIANT(Structure):
        pass
    return _wireSAFEARR_VARIANT
def _define__wireSAFEARR_VARIANT():
    _wireSAFEARR_VARIANT = win32more.System.Ole._wireSAFEARR_VARIANT_head
    _wireSAFEARR_VARIANT._fields_ = [
        ("Size", UInt32),
        ("aVariant", POINTER(POINTER(win32more.System.Ole._wireVARIANT_head))),
    ]
    return _wireSAFEARR_VARIANT
def _define__wireSAFEARR_BRECORD_head():
    class _wireSAFEARR_BRECORD(Structure):
        pass
    return _wireSAFEARR_BRECORD
def _define__wireSAFEARR_BRECORD():
    _wireSAFEARR_BRECORD = win32more.System.Ole._wireSAFEARR_BRECORD_head
    _wireSAFEARR_BRECORD._fields_ = [
        ("Size", UInt32),
        ("aRecord", POINTER(POINTER(win32more.System.Ole._wireBRECORD_head))),
    ]
    return _wireSAFEARR_BRECORD
def _define__wireSAFEARR_HAVEIID_head():
    class _wireSAFEARR_HAVEIID(Structure):
        pass
    return _wireSAFEARR_HAVEIID
def _define__wireSAFEARR_HAVEIID():
    _wireSAFEARR_HAVEIID = win32more.System.Ole._wireSAFEARR_HAVEIID_head
    _wireSAFEARR_HAVEIID._fields_ = [
        ("Size", UInt32),
        ("apUnknown", POINTER(win32more.System.Com.IUnknown_head)),
        ("iid", Guid),
    ]
    return _wireSAFEARR_HAVEIID
SF_TYPE = Int32
SF_ERROR = 10
SF_I1 = 16
SF_I2 = 2
SF_I4 = 3
SF_I8 = 20
SF_BSTR = 8
SF_UNKNOWN = 13
SF_DISPATCH = 9
SF_VARIANT = 12
SF_RECORD = 36
SF_HAVEIID = 32781
def _define__wireSAFEARRAY_UNION_head():
    class _wireSAFEARRAY_UNION(Structure):
        pass
    return _wireSAFEARRAY_UNION
def _define__wireSAFEARRAY_UNION():
    _wireSAFEARRAY_UNION = win32more.System.Ole._wireSAFEARRAY_UNION_head
    class _wireSAFEARRAY_UNION__u_e__Struct(Union):
        pass
    _wireSAFEARRAY_UNION__u_e__Struct._fields_ = [
        ("BstrStr", win32more.System.Ole._wireSAFEARR_BSTR),
        ("UnknownStr", win32more.System.Ole._wireSAFEARR_UNKNOWN),
        ("DispatchStr", win32more.System.Ole._wireSAFEARR_DISPATCH),
        ("VariantStr", win32more.System.Ole._wireSAFEARR_VARIANT),
        ("RecordStr", win32more.System.Ole._wireSAFEARR_BRECORD),
        ("HaveIidStr", win32more.System.Ole._wireSAFEARR_HAVEIID),
        ("ByteStr", win32more.System.Com.BYTE_SIZEDARR),
        ("WordStr", win32more.System.Com.SHORT_SIZEDARR),
        ("LongStr", win32more.System.Com.LONG_SIZEDARR),
        ("HyperStr", win32more.System.Com.HYPER_SIZEDARR),
    ]
    _wireSAFEARRAY_UNION._fields_ = [
        ("sfType", UInt32),
        ("u", _wireSAFEARRAY_UNION__u_e__Struct),
    ]
    return _wireSAFEARRAY_UNION
def _define__wireSAFEARRAY_head():
    class _wireSAFEARRAY(Structure):
        pass
    return _wireSAFEARRAY
def _define__wireSAFEARRAY():
    _wireSAFEARRAY = win32more.System.Ole._wireSAFEARRAY_head
    _wireSAFEARRAY._fields_ = [
        ("cDims", UInt16),
        ("fFeatures", UInt16),
        ("cbElements", UInt32),
        ("cLocks", UInt32),
        ("uArrayStructs", win32more.System.Ole._wireSAFEARRAY_UNION),
        ("rgsabound", win32more.System.Com.SAFEARRAYBOUND * 0),
    ]
    return _wireSAFEARRAY
def _define__wireBRECORD_head():
    class _wireBRECORD(Structure):
        pass
    return _wireBRECORD
def _define__wireBRECORD():
    _wireBRECORD = win32more.System.Ole._wireBRECORD_head
    _wireBRECORD._fields_ = [
        ("fFlags", UInt32),
        ("clSize", UInt32),
        ("pRecInfo", win32more.System.Ole.IRecordInfo_head),
        ("pRecord", c_char_p_no),
    ]
    return _wireBRECORD
def _define__wireVARIANT_head():
    class _wireVARIANT(Structure):
        pass
    return _wireVARIANT
def _define__wireVARIANT():
    _wireVARIANT = win32more.System.Ole._wireVARIANT_head
    class _wireVARIANT__Anonymous_e__Union(Union):
        pass
    _wireVARIANT__Anonymous_e__Union._fields_ = [
        ("llVal", Int64),
        ("lVal", Int32),
        ("bVal", Byte),
        ("iVal", Int16),
        ("fltVal", Single),
        ("dblVal", Double),
        ("boolVal", Int16),
        ("scode", Int32),
        ("cyVal", win32more.System.Com.CY),
        ("date", Double),
        ("bstrVal", POINTER(win32more.System.Com.FLAGGED_WORD_BLOB_head)),
        ("punkVal", win32more.System.Com.IUnknown_head),
        ("pdispVal", win32more.System.Com.IDispatch_head),
        ("parray", POINTER(POINTER(win32more.System.Ole._wireSAFEARRAY_head))),
        ("brecVal", POINTER(win32more.System.Ole._wireBRECORD_head)),
        ("pbVal", c_char_p_no),
        ("piVal", POINTER(Int16)),
        ("plVal", POINTER(Int32)),
        ("pllVal", POINTER(Int64)),
        ("pfltVal", POINTER(Single)),
        ("pdblVal", POINTER(Double)),
        ("pboolVal", POINTER(Int16)),
        ("pscode", POINTER(Int32)),
        ("pcyVal", POINTER(win32more.System.Com.CY_head)),
        ("pdate", POINTER(Double)),
        ("pbstrVal", POINTER(POINTER(win32more.System.Com.FLAGGED_WORD_BLOB_head))),
        ("ppunkVal", POINTER(win32more.System.Com.IUnknown_head)),
        ("ppdispVal", POINTER(win32more.System.Com.IDispatch_head)),
        ("pparray", POINTER(POINTER(POINTER(win32more.System.Ole._wireSAFEARRAY_head)))),
        ("pvarVal", POINTER(POINTER(win32more.System.Ole._wireVARIANT_head))),
        ("cVal", win32more.Foundation.CHAR),
        ("uiVal", UInt16),
        ("ulVal", UInt32),
        ("ullVal", UInt64),
        ("intVal", Int32),
        ("uintVal", UInt32),
        ("decVal", win32more.Foundation.DECIMAL),
        ("pdecVal", POINTER(win32more.Foundation.DECIMAL_head)),
        ("pcVal", win32more.Foundation.PSTR),
        ("puiVal", POINTER(UInt16)),
        ("pulVal", POINTER(UInt32)),
        ("pullVal", POINTER(UInt64)),
        ("pintVal", POINTER(Int32)),
        ("puintVal", POINTER(UInt32)),
    ]
    _wireVARIANT._anonymous_ = [
        'Anonymous',
    ]
    _wireVARIANT._fields_ = [
        ("clSize", UInt32),
        ("rpcReserved", UInt32),
        ("vt", UInt16),
        ("wReserved1", UInt16),
        ("wReserved2", UInt16),
        ("wReserved3", UInt16),
        ("Anonymous", _wireVARIANT__Anonymous_e__Union),
    ]
    return _wireVARIANT
def _define_ARRAYDESC_head():
    class ARRAYDESC(Structure):
        pass
    return ARRAYDESC
def _define_ARRAYDESC():
    ARRAYDESC = win32more.System.Ole.ARRAYDESC_head
    ARRAYDESC._fields_ = [
        ("tdescElem", win32more.System.Com.TYPEDESC),
        ("cDims", UInt16),
        ("rgbounds", win32more.System.Com.SAFEARRAYBOUND * 0),
    ]
    return ARRAYDESC
def _define_PARAMDESCEX_head():
    class PARAMDESCEX(Structure):
        pass
    return PARAMDESCEX
def _define_PARAMDESCEX():
    PARAMDESCEX = win32more.System.Ole.PARAMDESCEX_head
    PARAMDESCEX._fields_ = [
        ("cBytes", UInt32),
        ("varDefaultValue", win32more.System.Com.VARIANT),
    ]
    return PARAMDESCEX
def _define_PARAMDESC_head():
    class PARAMDESC(Structure):
        pass
    return PARAMDESC
def _define_PARAMDESC():
    PARAMDESC = win32more.System.Ole.PARAMDESC_head
    PARAMDESC._fields_ = [
        ("pparamdescex", POINTER(win32more.System.Ole.PARAMDESCEX_head)),
        ("wParamFlags", UInt16),
    ]
    return PARAMDESC
TYPEFLAGS = Int32
TYPEFLAG_FAPPOBJECT = 1
TYPEFLAG_FCANCREATE = 2
TYPEFLAG_FLICENSED = 4
TYPEFLAG_FPREDECLID = 8
TYPEFLAG_FHIDDEN = 16
TYPEFLAG_FCONTROL = 32
TYPEFLAG_FDUAL = 64
TYPEFLAG_FNONEXTENSIBLE = 128
TYPEFLAG_FOLEAUTOMATION = 256
TYPEFLAG_FRESTRICTED = 512
TYPEFLAG_FAGGREGATABLE = 1024
TYPEFLAG_FREPLACEABLE = 2048
TYPEFLAG_FDISPATCHABLE = 4096
TYPEFLAG_FREVERSEBIND = 8192
TYPEFLAG_FPROXY = 16384
FUNCFLAGS = Int32
FUNCFLAG_FRESTRICTED = 1
FUNCFLAG_FSOURCE = 2
FUNCFLAG_FBINDABLE = 4
FUNCFLAG_FREQUESTEDIT = 8
FUNCFLAG_FDISPLAYBIND = 16
FUNCFLAG_FDEFAULTBIND = 32
FUNCFLAG_FHIDDEN = 64
FUNCFLAG_FUSESGETLASTERROR = 128
FUNCFLAG_FDEFAULTCOLLELEM = 256
FUNCFLAG_FUIDEFAULT = 512
FUNCFLAG_FNONBROWSABLE = 1024
FUNCFLAG_FREPLACEABLE = 2048
FUNCFLAG_FIMMEDIATEBIND = 4096
VARFLAGS = Int32
VARFLAG_FREADONLY = 1
VARFLAG_FSOURCE = 2
VARFLAG_FBINDABLE = 4
VARFLAG_FREQUESTEDIT = 8
VARFLAG_FDISPLAYBIND = 16
VARFLAG_FDEFAULTBIND = 32
VARFLAG_FHIDDEN = 64
VARFLAG_FRESTRICTED = 128
VARFLAG_FDEFAULTCOLLELEM = 256
VARFLAG_FUIDEFAULT = 512
VARFLAG_FNONBROWSABLE = 1024
VARFLAG_FREPLACEABLE = 2048
VARFLAG_FIMMEDIATEBIND = 4096
def _define_CLEANLOCALSTORAGE_head():
    class CLEANLOCALSTORAGE(Structure):
        pass
    return CLEANLOCALSTORAGE
def _define_CLEANLOCALSTORAGE():
    CLEANLOCALSTORAGE = win32more.System.Ole.CLEANLOCALSTORAGE_head
    CLEANLOCALSTORAGE._fields_ = [
        ("pInterface", win32more.System.Com.IUnknown_head),
        ("pStorage", c_void_p),
        ("flags", UInt32),
    ]
    return CLEANLOCALSTORAGE
def _define_ICreateTypeInfo_head():
    class ICreateTypeInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('00020405-0000-0000-c000-000000000046')
    return ICreateTypeInfo
def _define_ICreateTypeInfo():
    ICreateTypeInfo = win32more.System.Ole.ICreateTypeInfo_head
    ICreateTypeInfo.SetGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(3, 'SetGuid', ((1, 'guid'),)))
    ICreateTypeInfo.SetTypeFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'SetTypeFlags', ((1, 'uTypeFlags'),)))
    ICreateTypeInfo.SetDocString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(5, 'SetDocString', ((1, 'pStrDoc'),)))
    ICreateTypeInfo.SetHelpContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'SetHelpContext', ((1, 'dwHelpContext'),)))
    ICreateTypeInfo.SetVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,UInt16, use_last_error=False)(7, 'SetVersion', ((1, 'wMajorVerNum'),(1, 'wMinorVerNum'),)))
    ICreateTypeInfo.AddRefTypeInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.ITypeInfo_head,POINTER(UInt32), use_last_error=False)(8, 'AddRefTypeInfo', ((1, 'pTInfo'),(1, 'phRefType'),)))
    ICreateTypeInfo.AddFuncDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.FUNCDESC_head), use_last_error=False)(9, 'AddFuncDesc', ((1, 'index'),(1, 'pFuncDesc'),)))
    ICreateTypeInfo.AddImplType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(10, 'AddImplType', ((1, 'index'),(1, 'hRefType'),)))
    ICreateTypeInfo.SetImplTypeFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Int32, use_last_error=False)(11, 'SetImplTypeFlags', ((1, 'index'),(1, 'implTypeFlags'),)))
    ICreateTypeInfo.SetAlignment = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16, use_last_error=False)(12, 'SetAlignment', ((1, 'cbAlignment'),)))
    ICreateTypeInfo.SetSchema = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(13, 'SetSchema', ((1, 'pStrSchema'),)))
    ICreateTypeInfo.AddVarDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.VARDESC_head), use_last_error=False)(14, 'AddVarDesc', ((1, 'index'),(1, 'pVarDesc'),)))
    ICreateTypeInfo.SetFuncAndParamNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.PWSTR),UInt32, use_last_error=False)(15, 'SetFuncAndParamNames', ((1, 'index'),(1, 'rgszNames'),(1, 'cNames'),)))
    ICreateTypeInfo.SetVarName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(16, 'SetVarName', ((1, 'index'),(1, 'szName'),)))
    ICreateTypeInfo.SetTypeDescAlias = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.TYPEDESC_head), use_last_error=False)(17, 'SetTypeDescAlias', ((1, 'pTDescAlias'),)))
    ICreateTypeInfo.DefineFuncAsDllEntry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(18, 'DefineFuncAsDllEntry', ((1, 'index'),(1, 'szDllName'),(1, 'szProcName'),)))
    ICreateTypeInfo.SetFuncDocString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(19, 'SetFuncDocString', ((1, 'index'),(1, 'szDocString'),)))
    ICreateTypeInfo.SetVarDocString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(20, 'SetVarDocString', ((1, 'index'),(1, 'szDocString'),)))
    ICreateTypeInfo.SetFuncHelpContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(21, 'SetFuncHelpContext', ((1, 'index'),(1, 'dwHelpContext'),)))
    ICreateTypeInfo.SetVarHelpContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(22, 'SetVarHelpContext', ((1, 'index'),(1, 'dwHelpContext'),)))
    ICreateTypeInfo.SetMops = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.BSTR, use_last_error=False)(23, 'SetMops', ((1, 'index'),(1, 'bstrMops'),)))
    ICreateTypeInfo.SetTypeIdldesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDLDESC_head), use_last_error=False)(24, 'SetTypeIdldesc', ((1, 'pIdlDesc'),)))
    ICreateTypeInfo.LayOut = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(25, 'LayOut', ()))
    win32more.System.Com.IUnknown
    return ICreateTypeInfo
def _define_ICreateTypeInfo2_head():
    class ICreateTypeInfo2(win32more.System.Ole.ICreateTypeInfo_head):
        Guid = Guid('0002040e-0000-0000-c000-000000000046')
    return ICreateTypeInfo2
def _define_ICreateTypeInfo2():
    ICreateTypeInfo2 = win32more.System.Ole.ICreateTypeInfo2_head
    ICreateTypeInfo2.DeleteFuncDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(26, 'DeleteFuncDesc', ((1, 'index'),)))
    ICreateTypeInfo2.DeleteFuncDescByMemId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.System.Com.INVOKEKIND, use_last_error=False)(27, 'DeleteFuncDescByMemId', ((1, 'memid'),(1, 'invKind'),)))
    ICreateTypeInfo2.DeleteVarDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(28, 'DeleteVarDesc', ((1, 'index'),)))
    ICreateTypeInfo2.DeleteVarDescByMemId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(29, 'DeleteVarDescByMemId', ((1, 'memid'),)))
    ICreateTypeInfo2.DeleteImplType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(30, 'DeleteImplType', ((1, 'index'),)))
    ICreateTypeInfo2.SetCustData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(31, 'SetCustData', ((1, 'guid'),(1, 'pVarVal'),)))
    ICreateTypeInfo2.SetFuncCustData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(32, 'SetFuncCustData', ((1, 'index'),(1, 'guid'),(1, 'pVarVal'),)))
    ICreateTypeInfo2.SetParamCustData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(Guid),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(33, 'SetParamCustData', ((1, 'indexFunc'),(1, 'indexParam'),(1, 'guid'),(1, 'pVarVal'),)))
    ICreateTypeInfo2.SetVarCustData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(34, 'SetVarCustData', ((1, 'index'),(1, 'guid'),(1, 'pVarVal'),)))
    ICreateTypeInfo2.SetImplTypeCustData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(35, 'SetImplTypeCustData', ((1, 'index'),(1, 'guid'),(1, 'pVarVal'),)))
    ICreateTypeInfo2.SetHelpStringContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(36, 'SetHelpStringContext', ((1, 'dwHelpStringContext'),)))
    ICreateTypeInfo2.SetFuncHelpStringContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(37, 'SetFuncHelpStringContext', ((1, 'index'),(1, 'dwHelpStringContext'),)))
    ICreateTypeInfo2.SetVarHelpStringContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(38, 'SetVarHelpStringContext', ((1, 'index'),(1, 'dwHelpStringContext'),)))
    ICreateTypeInfo2.Invalidate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(39, 'Invalidate', ()))
    ICreateTypeInfo2.SetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(40, 'SetName', ((1, 'szName'),)))
    win32more.System.Ole.ICreateTypeInfo
    return ICreateTypeInfo2
def _define_ICreateTypeLib_head():
    class ICreateTypeLib(win32more.System.Com.IUnknown_head):
        Guid = Guid('00020406-0000-0000-c000-000000000046')
    return ICreateTypeLib
def _define_ICreateTypeLib():
    ICreateTypeLib = win32more.System.Ole.ICreateTypeLib_head
    ICreateTypeLib.CreateTypeInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.TYPEKIND,POINTER(win32more.System.Ole.ICreateTypeInfo_head), use_last_error=False)(3, 'CreateTypeInfo', ((1, 'szName'),(1, 'tkind'),(1, 'ppCTInfo'),)))
    ICreateTypeLib.SetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(4, 'SetName', ((1, 'szName'),)))
    ICreateTypeLib.SetVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,UInt16, use_last_error=False)(5, 'SetVersion', ((1, 'wMajorVerNum'),(1, 'wMinorVerNum'),)))
    ICreateTypeLib.SetGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(6, 'SetGuid', ((1, 'guid'),)))
    ICreateTypeLib.SetDocString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(7, 'SetDocString', ((1, 'szDoc'),)))
    ICreateTypeLib.SetHelpFileName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(8, 'SetHelpFileName', ((1, 'szHelpFileName'),)))
    ICreateTypeLib.SetHelpContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(9, 'SetHelpContext', ((1, 'dwHelpContext'),)))
    ICreateTypeLib.SetLcid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(10, 'SetLcid', ((1, 'lcid'),)))
    ICreateTypeLib.SetLibFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(11, 'SetLibFlags', ((1, 'uLibFlags'),)))
    ICreateTypeLib.SaveAllChanges = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'SaveAllChanges', ()))
    win32more.System.Com.IUnknown
    return ICreateTypeLib
def _define_ICreateTypeLib2_head():
    class ICreateTypeLib2(win32more.System.Ole.ICreateTypeLib_head):
        Guid = Guid('0002040f-0000-0000-c000-000000000046')
    return ICreateTypeLib2
def _define_ICreateTypeLib2():
    ICreateTypeLib2 = win32more.System.Ole.ICreateTypeLib2_head
    ICreateTypeLib2.DeleteTypeInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(13, 'DeleteTypeInfo', ((1, 'szName'),)))
    ICreateTypeLib2.SetCustData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(14, 'SetCustData', ((1, 'guid'),(1, 'pVarVal'),)))
    ICreateTypeLib2.SetHelpStringContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(15, 'SetHelpStringContext', ((1, 'dwHelpStringContext'),)))
    ICreateTypeLib2.SetHelpStringDll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(16, 'SetHelpStringDll', ((1, 'szFileName'),)))
    win32more.System.Ole.ICreateTypeLib
    return ICreateTypeLib2
def _define_IEnumVARIANT_head():
    class IEnumVARIANT(win32more.System.Com.IUnknown_head):
        Guid = Guid('00020404-0000-0000-c000-000000000046')
    return IEnumVARIANT
def _define_IEnumVARIANT():
    IEnumVARIANT = win32more.System.Ole.IEnumVARIANT_head
    IEnumVARIANT.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.VARIANT),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'rgVar'),(1, 'pCeltFetched'),)))
    IEnumVARIANT.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'celt'),)))
    IEnumVARIANT.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumVARIANT.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IEnumVARIANT_head), use_last_error=False)(6, 'Clone', ((1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return IEnumVARIANT
LIBFLAGS = Int32
LIBFLAG_FRESTRICTED = 1
LIBFLAG_FCONTROL = 2
LIBFLAG_FHIDDEN = 4
LIBFLAG_FHASDISKIMAGE = 8
CHANGEKIND = Int32
CHANGEKIND_ADDMEMBER = 0
CHANGEKIND_DELETEMEMBER = 1
CHANGEKIND_SETNAMES = 2
CHANGEKIND_SETDOCUMENTATION = 3
CHANGEKIND_GENERAL = 4
CHANGEKIND_INVALIDATE = 5
CHANGEKIND_CHANGEFAILED = 6
CHANGEKIND_MAX = 7
def _define_ITypeChangeEvents_head():
    class ITypeChangeEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('00020410-0000-0000-c000-000000000046')
    return ITypeChangeEvents
def _define_ITypeChangeEvents():
    ITypeChangeEvents = win32more.System.Ole.ITypeChangeEvents_head
    ITypeChangeEvents.RequestTypeChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.CHANGEKIND,win32more.System.Com.ITypeInfo_head,win32more.Foundation.PWSTR,POINTER(Int32), use_last_error=False)(3, 'RequestTypeChange', ((1, 'changeKind'),(1, 'pTInfoBefore'),(1, 'pStrName'),(1, 'pfCancel'),)))
    ITypeChangeEvents.AfterTypeChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.CHANGEKIND,win32more.System.Com.ITypeInfo_head,win32more.Foundation.PWSTR, use_last_error=False)(4, 'AfterTypeChange', ((1, 'changeKind'),(1, 'pTInfoAfter'),(1, 'pStrName'),)))
    win32more.System.Com.IUnknown
    return ITypeChangeEvents
def _define_ICreateErrorInfo_head():
    class ICreateErrorInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('22f03340-547d-101b-8e65-08002b2bd119')
    return ICreateErrorInfo
def _define_ICreateErrorInfo():
    ICreateErrorInfo = win32more.System.Ole.ICreateErrorInfo_head
    ICreateErrorInfo.SetGUID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(3, 'SetGUID', ((1, 'rguid'),)))
    ICreateErrorInfo.SetSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(4, 'SetSource', ((1, 'szSource'),)))
    ICreateErrorInfo.SetDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(5, 'SetDescription', ((1, 'szDescription'),)))
    ICreateErrorInfo.SetHelpFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(6, 'SetHelpFile', ((1, 'szHelpFile'),)))
    ICreateErrorInfo.SetHelpContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(7, 'SetHelpContext', ((1, 'dwHelpContext'),)))
    win32more.System.Com.IUnknown
    return ICreateErrorInfo
def _define_ITypeFactory_head():
    class ITypeFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('0000002e-0000-0000-c000-000000000046')
    return ITypeFactory
def _define_ITypeFactory():
    ITypeFactory = win32more.System.Ole.ITypeFactory_head
    ITypeFactory.CreateFromTypeInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.ITypeInfo_head,POINTER(Guid),POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(3, 'CreateFromTypeInfo', ((1, 'pTypeInfo'),(1, 'riid'),(1, 'ppv'),)))
    win32more.System.Com.IUnknown
    return ITypeFactory
def _define_ITypeMarshal_head():
    class ITypeMarshal(win32more.System.Com.IUnknown_head):
        Guid = Guid('0000002d-0000-0000-c000-000000000046')
    return ITypeMarshal
def _define_ITypeMarshal():
    ITypeMarshal = win32more.System.Ole.ITypeMarshal_head
    ITypeMarshal.Size = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,c_void_p,POINTER(UInt32), use_last_error=False)(3, 'Size', ((1, 'pvType'),(1, 'dwDestContext'),(1, 'pvDestContext'),(1, 'pSize'),)))
    ITypeMarshal.Marshal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,c_void_p,UInt32,c_char_p_no,POINTER(UInt32), use_last_error=False)(4, 'Marshal', ((1, 'pvType'),(1, 'dwDestContext'),(1, 'pvDestContext'),(1, 'cbBufferLength'),(1, 'pBuffer'),(1, 'pcbWritten'),)))
    ITypeMarshal.Unmarshal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,UInt32,POINTER(Byte),POINTER(UInt32), use_last_error=False)(5, 'Unmarshal', ((1, 'pvType'),(1, 'dwFlags'),(1, 'cbBufferLength'),(1, 'pBuffer'),(1, 'pcbRead'),)))
    ITypeMarshal.Free = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(6, 'Free', ((1, 'pvType'),)))
    win32more.System.Com.IUnknown
    return ITypeMarshal
def _define_IRecordInfo_head():
    class IRecordInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('0000002f-0000-0000-c000-000000000046')
    return IRecordInfo
def _define_IRecordInfo():
    IRecordInfo = win32more.System.Ole.IRecordInfo_head
    IRecordInfo.RecordInit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(3, 'RecordInit', ((1, 'pvNew'),)))
    IRecordInfo.RecordClear = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(4, 'RecordClear', ((1, 'pvExisting'),)))
    IRecordInfo.RecordCopy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,c_void_p, use_last_error=False)(5, 'RecordCopy', ((1, 'pvExisting'),(1, 'pvNew'),)))
    IRecordInfo.GetGuid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(6, 'GetGuid', ((1, 'pguid'),)))
    IRecordInfo.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(7, 'GetName', ((1, 'pbstrName'),)))
    IRecordInfo.GetSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(8, 'GetSize', ((1, 'pcbSize'),)))
    IRecordInfo.GetTypeInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.ITypeInfo_head), use_last_error=False)(9, 'GetTypeInfo', ((1, 'ppTypeInfo'),)))
    IRecordInfo.GetField = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(10, 'GetField', ((1, 'pvData'),(1, 'szFieldName'),(1, 'pvarField'),)))
    IRecordInfo.GetFieldNoCopy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.VARIANT_head),POINTER(c_void_p), use_last_error=False)(11, 'GetFieldNoCopy', ((1, 'pvData'),(1, 'szFieldName'),(1, 'pvarField'),(1, 'ppvDataCArray'),)))
    IRecordInfo.PutField = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(12, 'PutField', ((1, 'wFlags'),(1, 'pvData'),(1, 'szFieldName'),(1, 'pvarField'),)))
    IRecordInfo.PutFieldNoCopy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(13, 'PutFieldNoCopy', ((1, 'wFlags'),(1, 'pvData'),(1, 'szFieldName'),(1, 'pvarField'),)))
    IRecordInfo.GetFieldNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(win32more.Foundation.BSTR), use_last_error=False)(14, 'GetFieldNames', ((1, 'pcNames'),(1, 'rgBstrNames'),)))
    IRecordInfo.IsMatchingType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Ole.IRecordInfo_head, use_last_error=False)(15, 'IsMatchingType', ((1, 'pRecordInfo'),)))
    IRecordInfo.RecordCreate = COMMETHOD(WINFUNCTYPE(c_void_p, use_last_error=False)(16, 'RecordCreate', ()))
    IRecordInfo.RecordCreateCopy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(c_void_p), use_last_error=False)(17, 'RecordCreateCopy', ((1, 'pvSource'),(1, 'ppvDest'),)))
    IRecordInfo.RecordDestroy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(18, 'RecordDestroy', ((1, 'pvRecord'),)))
    win32more.System.Com.IUnknown
    return IRecordInfo
def _define_IOleAdviseHolder_head():
    class IOleAdviseHolder(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000111-0000-0000-c000-000000000046')
    return IOleAdviseHolder
def _define_IOleAdviseHolder():
    IOleAdviseHolder = win32more.System.Ole.IOleAdviseHolder_head
    IOleAdviseHolder.Advise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IAdviseSink_head,POINTER(UInt32), use_last_error=False)(3, 'Advise', ((1, 'pAdvise'),(1, 'pdwConnection'),)))
    IOleAdviseHolder.Unadvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Unadvise', ((1, 'dwConnection'),)))
    IOleAdviseHolder.EnumAdvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumSTATDATA_head), use_last_error=False)(5, 'EnumAdvise', ((1, 'ppenumAdvise'),)))
    IOleAdviseHolder.SendOnRename = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IMoniker_head, use_last_error=False)(6, 'SendOnRename', ((1, 'pmk'),)))
    IOleAdviseHolder.SendOnSave = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'SendOnSave', ()))
    IOleAdviseHolder.SendOnClose = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'SendOnClose', ()))
    win32more.System.Com.IUnknown
    return IOleAdviseHolder
def _define_IOleCache_head():
    class IOleCache(win32more.System.Com.IUnknown_head):
        Guid = Guid('0000011e-0000-0000-c000-000000000046')
    return IOleCache
def _define_IOleCache():
    IOleCache = win32more.System.Ole.IOleCache_head
    IOleCache.Cache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.FORMATETC_head),UInt32,POINTER(UInt32), use_last_error=False)(3, 'Cache', ((1, 'pformatetc'),(1, 'advf'),(1, 'pdwConnection'),)))
    IOleCache.Uncache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Uncache', ((1, 'dwConnection'),)))
    IOleCache.EnumCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumSTATDATA_head), use_last_error=False)(5, 'EnumCache', ((1, 'ppenumSTATDATA'),)))
    IOleCache.InitCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head, use_last_error=False)(6, 'InitCache', ((1, 'pDataObject'),)))
    IOleCache.SetData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.FORMATETC_head),POINTER(win32more.System.Com.STGMEDIUM_head),win32more.Foundation.BOOL, use_last_error=False)(7, 'SetData', ((1, 'pformatetc'),(1, 'pmedium'),(1, 'fRelease'),)))
    win32more.System.Com.IUnknown
    return IOleCache
DISCARDCACHE = Int32
DISCARDCACHE_SAVEIFDIRTY = 0
DISCARDCACHE_NOSAVE = 1
def _define_IOleCache2_head():
    class IOleCache2(win32more.System.Ole.IOleCache_head):
        Guid = Guid('00000128-0000-0000-c000-000000000046')
    return IOleCache2
def _define_IOleCache2():
    IOleCache2 = win32more.System.Ole.IOleCache2_head
    IOleCache2.UpdateCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head,win32more.System.Ole.UPDFCACHE_FLAGS,c_void_p, use_last_error=False)(8, 'UpdateCache', ((1, 'pDataObject'),(1, 'grfUpdf'),(1, 'pReserved'),)))
    IOleCache2.DiscardCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(9, 'DiscardCache', ((1, 'dwDiscardOptions'),)))
    win32more.System.Ole.IOleCache
    return IOleCache2
def _define_IOleCacheControl_head():
    class IOleCacheControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000129-0000-0000-c000-000000000046')
    return IOleCacheControl
def _define_IOleCacheControl():
    IOleCacheControl = win32more.System.Ole.IOleCacheControl_head
    IOleCacheControl.OnRun = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head, use_last_error=False)(3, 'OnRun', ((1, 'pDataObject'),)))
    IOleCacheControl.OnStop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'OnStop', ()))
    win32more.System.Com.IUnknown
    return IOleCacheControl
def _define_IParseDisplayName_head():
    class IParseDisplayName(win32more.System.Com.IUnknown_head):
        Guid = Guid('0000011a-0000-0000-c000-000000000046')
    return IParseDisplayName
def _define_IParseDisplayName():
    IParseDisplayName = win32more.System.Ole.IParseDisplayName_head
    IParseDisplayName.ParseDisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IBindCtx_head,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(win32more.System.Com.IMoniker_head), use_last_error=False)(3, 'ParseDisplayName', ((1, 'pbc'),(1, 'pszDisplayName'),(1, 'pchEaten'),(1, 'ppmkOut'),)))
    win32more.System.Com.IUnknown
    return IParseDisplayName
def _define_IOleContainer_head():
    class IOleContainer(win32more.System.Ole.IParseDisplayName_head):
        Guid = Guid('0000011b-0000-0000-c000-000000000046')
    return IOleContainer
def _define_IOleContainer():
    IOleContainer = win32more.System.Ole.IOleContainer_head
    IOleContainer.EnumObjects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.IEnumUnknown_head), use_last_error=False)(4, 'EnumObjects', ((1, 'grfFlags'),(1, 'ppenum'),)))
    IOleContainer.LockContainer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(5, 'LockContainer', ((1, 'fLock'),)))
    win32more.System.Ole.IParseDisplayName
    return IOleContainer
def _define_IOleClientSite_head():
    class IOleClientSite(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000118-0000-0000-c000-000000000046')
    return IOleClientSite
def _define_IOleClientSite():
    IOleClientSite = win32more.System.Ole.IOleClientSite_head
    IOleClientSite.SaveObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'SaveObject', ()))
    IOleClientSite.GetMoniker = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.System.Com.IMoniker_head), use_last_error=False)(4, 'GetMoniker', ((1, 'dwAssign'),(1, 'dwWhichMoniker'),(1, 'ppmk'),)))
    IOleClientSite.GetContainer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IOleContainer_head), use_last_error=False)(5, 'GetContainer', ((1, 'ppContainer'),)))
    IOleClientSite.ShowObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'ShowObject', ()))
    IOleClientSite.OnShowWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(7, 'OnShowWindow', ((1, 'fShow'),)))
    IOleClientSite.RequestNewObjectLayout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'RequestNewObjectLayout', ()))
    win32more.System.Com.IUnknown
    return IOleClientSite
OLEGETMONIKER = Int32
OLEGETMONIKER_ONLYIFTHERE = 1
OLEGETMONIKER_FORCEASSIGN = 2
OLEGETMONIKER_UNASSIGN = 3
OLEGETMONIKER_TEMPFORUSER = 4
OLEWHICHMK = Int32
OLEWHICHMK_CONTAINER = 1
OLEWHICHMK_OBJREL = 2
OLEWHICHMK_OBJFULL = 3
USERCLASSTYPE = Int32
USERCLASSTYPE_FULL = 1
USERCLASSTYPE_SHORT = 2
USERCLASSTYPE_APPNAME = 3
OLEMISC = Int32
OLEMISC_RECOMPOSEONRESIZE = 1
OLEMISC_ONLYICONIC = 2
OLEMISC_INSERTNOTREPLACE = 4
OLEMISC_STATIC = 8
OLEMISC_CANTLINKINSIDE = 16
OLEMISC_CANLINKBYOLE1 = 32
OLEMISC_ISLINKOBJECT = 64
OLEMISC_INSIDEOUT = 128
OLEMISC_ACTIVATEWHENVISIBLE = 256
OLEMISC_RENDERINGISDEVICEINDEPENDENT = 512
OLEMISC_INVISIBLEATRUNTIME = 1024
OLEMISC_ALWAYSRUN = 2048
OLEMISC_ACTSLIKEBUTTON = 4096
OLEMISC_ACTSLIKELABEL = 8192
OLEMISC_NOUIACTIVATE = 16384
OLEMISC_ALIGNABLE = 32768
OLEMISC_SIMPLEFRAME = 65536
OLEMISC_SETCLIENTSITEFIRST = 131072
OLEMISC_IMEMODE = 262144
OLEMISC_IGNOREACTIVATEWHENVISIBLE = 524288
OLEMISC_WANTSTOMENUMERGE = 1048576
OLEMISC_SUPPORTSMULTILEVELUNDO = 2097152
OLECLOSE = Int32
OLECLOSE_SAVEIFDIRTY = 0
OLECLOSE_NOSAVE = 1
OLECLOSE_PROMPTSAVE = 2
def _define_IOleObject_head():
    class IOleObject(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000112-0000-0000-c000-000000000046')
    return IOleObject
def _define_IOleObject():
    IOleObject = win32more.System.Ole.IOleObject_head
    IOleObject.SetClientSite = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IOleClientSite_head, use_last_error=False)(3, 'SetClientSite', ((1, 'pClientSite'),)))
    IOleObject.GetClientSite = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IOleClientSite_head), use_last_error=False)(4, 'GetClientSite', ((1, 'ppClientSite'),)))
    IOleObject.SetHostNames = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(5, 'SetHostNames', ((1, 'szContainerApp'),(1, 'szContainerObj'),)))
    IOleObject.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'Close', ((1, 'dwSaveOption'),)))
    IOleObject.SetMoniker = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.Com.IMoniker_head, use_last_error=False)(7, 'SetMoniker', ((1, 'dwWhichMoniker'),(1, 'pmk'),)))
    IOleObject.GetMoniker = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.System.Com.IMoniker_head), use_last_error=False)(8, 'GetMoniker', ((1, 'dwAssign'),(1, 'dwWhichMoniker'),(1, 'ppmk'),)))
    IOleObject.InitFromData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head,win32more.Foundation.BOOL,UInt32, use_last_error=False)(9, 'InitFromData', ((1, 'pDataObject'),(1, 'fCreation'),(1, 'dwReserved'),)))
    IOleObject.GetClipboardData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.IDataObject_head), use_last_error=False)(10, 'GetClipboardData', ((1, 'dwReserved'),(1, 'ppDataObject'),)))
    IOleObject.DoVerb = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.UI.WindowsAndMessaging.MSG_head),win32more.System.Ole.IOleClientSite_head,Int32,win32more.Foundation.HWND,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(11, 'DoVerb', ((1, 'iVerb'),(1, 'lpmsg'),(1, 'pActiveSite'),(1, 'lindex'),(1, 'hwndParent'),(1, 'lprcPosRect'),)))
    IOleObject.EnumVerbs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IEnumOLEVERB_head), use_last_error=False)(12, 'EnumVerbs', ((1, 'ppEnumOleVerb'),)))
    IOleObject.Update = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(13, 'Update', ()))
    IOleObject.IsUpToDate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(14, 'IsUpToDate', ()))
    IOleObject.GetUserClassID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(15, 'GetUserClassID', ((1, 'pClsid'),)))
    IOleObject.GetUserType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(16, 'GetUserType', ((1, 'dwFormOfType'),(1, 'pszUserType'),)))
    IOleObject.SetExtent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.SIZE_head), use_last_error=False)(17, 'SetExtent', ((1, 'dwDrawAspect'),(1, 'psizel'),)))
    IOleObject.GetExtent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.SIZE_head), use_last_error=False)(18, 'GetExtent', ((1, 'dwDrawAspect'),(1, 'psizel'),)))
    IOleObject.Advise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IAdviseSink_head,POINTER(UInt32), use_last_error=False)(19, 'Advise', ((1, 'pAdvSink'),(1, 'pdwConnection'),)))
    IOleObject.Unadvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(20, 'Unadvise', ((1, 'dwConnection'),)))
    IOleObject.EnumAdvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IEnumSTATDATA_head), use_last_error=False)(21, 'EnumAdvise', ((1, 'ppenumAdvise'),)))
    IOleObject.GetMiscStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(22, 'GetMiscStatus', ((1, 'dwAspect'),(1, 'pdwStatus'),)))
    IOleObject.SetColorScheme = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Gdi.LOGPALETTE_head), use_last_error=False)(23, 'SetColorScheme', ((1, 'pLogpal'),)))
    win32more.System.Com.IUnknown
    return IOleObject
OLERENDER = Int32
OLERENDER_NONE = 0
OLERENDER_DRAW = 1
OLERENDER_FORMAT = 2
OLERENDER_ASIS = 3
def _define_OBJECTDESCRIPTOR_head():
    class OBJECTDESCRIPTOR(Structure):
        pass
    return OBJECTDESCRIPTOR
def _define_OBJECTDESCRIPTOR():
    OBJECTDESCRIPTOR = win32more.System.Ole.OBJECTDESCRIPTOR_head
    OBJECTDESCRIPTOR._fields_ = [
        ("cbSize", UInt32),
        ("clsid", Guid),
        ("dwDrawAspect", UInt32),
        ("sizel", win32more.Foundation.SIZE),
        ("pointl", win32more.Foundation.POINTL),
        ("dwStatus", UInt32),
        ("dwFullUserTypeName", UInt32),
        ("dwSrcOfCopy", UInt32),
    ]
    return OBJECTDESCRIPTOR
def _define_IOleWindow_head():
    class IOleWindow(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000114-0000-0000-c000-000000000046')
    return IOleWindow
def _define_IOleWindow():
    IOleWindow = win32more.System.Ole.IOleWindow_head
    IOleWindow.GetWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HWND), use_last_error=False)(3, 'GetWindow', ((1, 'phwnd'),)))
    IOleWindow.ContextSensitiveHelp = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(4, 'ContextSensitiveHelp', ((1, 'fEnterMode'),)))
    win32more.System.Com.IUnknown
    return IOleWindow
OLEUPDATE = Int32
OLEUPDATE_ALWAYS = 1
OLEUPDATE_ONCALL = 3
OLELINKBIND = Int32
OLELINKBIND_EVENIFCLASSDIFF = 1
def _define_IOleLink_head():
    class IOleLink(win32more.System.Com.IUnknown_head):
        Guid = Guid('0000011d-0000-0000-c000-000000000046')
    return IOleLink
def _define_IOleLink():
    IOleLink = win32more.System.Ole.IOleLink_head
    IOleLink.SetUpdateOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(3, 'SetUpdateOptions', ((1, 'dwUpdateOpt'),)))
    IOleLink.GetUpdateOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetUpdateOptions', ((1, 'pdwUpdateOpt'),)))
    IOleLink.SetSourceMoniker = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IMoniker_head,POINTER(Guid), use_last_error=False)(5, 'SetSourceMoniker', ((1, 'pmk'),(1, 'rclsid'),)))
    IOleLink.GetSourceMoniker = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IMoniker_head), use_last_error=False)(6, 'GetSourceMoniker', ((1, 'ppmk'),)))
    IOleLink.SetSourceDisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(7, 'SetSourceDisplayName', ((1, 'pszStatusText'),)))
    IOleLink.GetSourceDisplayName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(8, 'GetSourceDisplayName', ((1, 'ppszDisplayName'),)))
    IOleLink.BindToSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.Com.IBindCtx_head, use_last_error=False)(9, 'BindToSource', ((1, 'bindflags'),(1, 'pbc'),)))
    IOleLink.BindIfRunning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'BindIfRunning', ()))
    IOleLink.GetBoundSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(11, 'GetBoundSource', ((1, 'ppunk'),)))
    IOleLink.UnbindSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'UnbindSource', ()))
    IOleLink.Update = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IBindCtx_head, use_last_error=False)(13, 'Update', ((1, 'pbc'),)))
    win32more.System.Com.IUnknown
    return IOleLink
BINDSPEED = Int32
BINDSPEED_INDEFINITE = 1
BINDSPEED_MODERATE = 2
BINDSPEED_IMMEDIATE = 3
OLECONTF = Int32
OLECONTF_EMBEDDINGS = 1
OLECONTF_LINKS = 2
OLECONTF_OTHERS = 4
OLECONTF_ONLYUSER = 8
OLECONTF_ONLYIFRUNNING = 16
def _define_IOleItemContainer_head():
    class IOleItemContainer(win32more.System.Ole.IOleContainer_head):
        Guid = Guid('0000011c-0000-0000-c000-000000000046')
    return IOleItemContainer
def _define_IOleItemContainer():
    IOleItemContainer = win32more.System.Ole.IOleItemContainer_head
    IOleItemContainer.GetObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.System.Com.IBindCtx_head,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(6, 'GetObject', ((1, 'pszItem'),(1, 'dwSpeedNeeded'),(1, 'pbc'),(1, 'riid'),(1, 'ppvObject'),)))
    IOleItemContainer.GetObjectStorage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.IBindCtx_head,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(7, 'GetObjectStorage', ((1, 'pszItem'),(1, 'pbc'),(1, 'riid'),(1, 'ppvStorage'),)))
    IOleItemContainer.IsRunning = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(8, 'IsRunning', ((1, 'pszItem'),)))
    win32more.System.Ole.IOleContainer
    return IOleItemContainer
def _define_IOleInPlaceUIWindow_head():
    class IOleInPlaceUIWindow(win32more.System.Ole.IOleWindow_head):
        Guid = Guid('00000115-0000-0000-c000-000000000046')
    return IOleInPlaceUIWindow
def _define_IOleInPlaceUIWindow():
    IOleInPlaceUIWindow = win32more.System.Ole.IOleInPlaceUIWindow_head
    IOleInPlaceUIWindow.GetBorder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(5, 'GetBorder', ((1, 'lprectBorder'),)))
    IOleInPlaceUIWindow.RequestBorderSpace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(6, 'RequestBorderSpace', ((1, 'pborderwidths'),)))
    IOleInPlaceUIWindow.SetBorderSpace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(7, 'SetBorderSpace', ((1, 'pborderwidths'),)))
    IOleInPlaceUIWindow.SetActiveObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IOleInPlaceActiveObject_head,win32more.Foundation.PWSTR, use_last_error=False)(8, 'SetActiveObject', ((1, 'pActiveObject'),(1, 'pszObjName'),)))
    win32more.System.Ole.IOleWindow
    return IOleInPlaceUIWindow
def _define_IOleInPlaceActiveObject_head():
    class IOleInPlaceActiveObject(win32more.System.Ole.IOleWindow_head):
        Guid = Guid('00000117-0000-0000-c000-000000000046')
    return IOleInPlaceActiveObject
def _define_IOleInPlaceActiveObject():
    IOleInPlaceActiveObject = win32more.System.Ole.IOleInPlaceActiveObject_head
    IOleInPlaceActiveObject.TranslateAccelerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.WindowsAndMessaging.MSG_head), use_last_error=False)(5, 'TranslateAccelerator', ((1, 'lpmsg'),)))
    IOleInPlaceActiveObject.OnFrameWindowActivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(6, 'OnFrameWindowActivate', ((1, 'fActivate'),)))
    IOleInPlaceActiveObject.OnDocWindowActivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(7, 'OnDocWindowActivate', ((1, 'fActivate'),)))
    IOleInPlaceActiveObject.ResizeBorder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head),win32more.System.Ole.IOleInPlaceUIWindow_head,win32more.Foundation.BOOL, use_last_error=False)(8, 'ResizeBorder', ((1, 'prcBorder'),(1, 'pUIWindow'),(1, 'fFrameWindow'),)))
    IOleInPlaceActiveObject.EnableModeless = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(9, 'EnableModeless', ((1, 'fEnable'),)))
    win32more.System.Ole.IOleWindow
    return IOleInPlaceActiveObject
def _define_OIFI_head():
    class OIFI(Structure):
        pass
    return OIFI
def _define_OIFI():
    OIFI = win32more.System.Ole.OIFI_head
    OIFI._fields_ = [
        ("cb", UInt32),
        ("fMDIApp", win32more.Foundation.BOOL),
        ("hwndFrame", win32more.Foundation.HWND),
        ("haccel", win32more.UI.WindowsAndMessaging.HACCEL),
        ("cAccelEntries", UInt32),
    ]
    return OIFI
def _define_OleMenuGroupWidths_head():
    class OleMenuGroupWidths(Structure):
        pass
    return OleMenuGroupWidths
def _define_OleMenuGroupWidths():
    OleMenuGroupWidths = win32more.System.Ole.OleMenuGroupWidths_head
    OleMenuGroupWidths._fields_ = [
        ("width", Int32 * 6),
    ]
    return OleMenuGroupWidths
def _define_IOleInPlaceFrame_head():
    class IOleInPlaceFrame(win32more.System.Ole.IOleInPlaceUIWindow_head):
        Guid = Guid('00000116-0000-0000-c000-000000000046')
    return IOleInPlaceFrame
def _define_IOleInPlaceFrame():
    IOleInPlaceFrame = win32more.System.Ole.IOleInPlaceFrame_head
    IOleInPlaceFrame.InsertMenus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.WindowsAndMessaging.HMENU,POINTER(win32more.System.Ole.OleMenuGroupWidths_head), use_last_error=False)(9, 'InsertMenus', ((1, 'hmenuShared'),(1, 'lpMenuWidths'),)))
    IOleInPlaceFrame.SetMenu = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.WindowsAndMessaging.HMENU,IntPtr,win32more.Foundation.HWND, use_last_error=False)(10, 'SetMenu', ((1, 'hmenuShared'),(1, 'holemenu'),(1, 'hwndActiveObject'),)))
    IOleInPlaceFrame.RemoveMenus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.UI.WindowsAndMessaging.HMENU, use_last_error=False)(11, 'RemoveMenus', ((1, 'hmenuShared'),)))
    IOleInPlaceFrame.SetStatusText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(12, 'SetStatusText', ((1, 'pszStatusText'),)))
    IOleInPlaceFrame.EnableModeless = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(13, 'EnableModeless', ((1, 'fEnable'),)))
    IOleInPlaceFrame.TranslateAccelerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.WindowsAndMessaging.MSG_head),UInt16, use_last_error=False)(14, 'TranslateAccelerator', ((1, 'lpmsg'),(1, 'wID'),)))
    win32more.System.Ole.IOleInPlaceUIWindow
    return IOleInPlaceFrame
def _define_IOleInPlaceObject_head():
    class IOleInPlaceObject(win32more.System.Ole.IOleWindow_head):
        Guid = Guid('00000113-0000-0000-c000-000000000046')
    return IOleInPlaceObject
def _define_IOleInPlaceObject():
    IOleInPlaceObject = win32more.System.Ole.IOleInPlaceObject_head
    IOleInPlaceObject.InPlaceDeactivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'InPlaceDeactivate', ()))
    IOleInPlaceObject.UIDeactivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'UIDeactivate', ()))
    IOleInPlaceObject.SetObjectRects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.RECT_head), use_last_error=False)(7, 'SetObjectRects', ((1, 'lprcPosRect'),(1, 'lprcClipRect'),)))
    IOleInPlaceObject.ReactivateAndUndo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'ReactivateAndUndo', ()))
    win32more.System.Ole.IOleWindow
    return IOleInPlaceObject
def _define_IOleInPlaceSite_head():
    class IOleInPlaceSite(win32more.System.Ole.IOleWindow_head):
        Guid = Guid('00000119-0000-0000-c000-000000000046')
    return IOleInPlaceSite
def _define_IOleInPlaceSite():
    IOleInPlaceSite = win32more.System.Ole.IOleInPlaceSite_head
    IOleInPlaceSite.CanInPlaceActivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'CanInPlaceActivate', ()))
    IOleInPlaceSite.OnInPlaceActivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'OnInPlaceActivate', ()))
    IOleInPlaceSite.OnUIActivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'OnUIActivate', ()))
    IOleInPlaceSite.GetWindowContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IOleInPlaceFrame_head),POINTER(win32more.System.Ole.IOleInPlaceUIWindow_head),POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.RECT_head),POINTER(win32more.System.Ole.OIFI_head), use_last_error=False)(8, 'GetWindowContext', ((1, 'ppFrame'),(1, 'ppDoc'),(1, 'lprcPosRect'),(1, 'lprcClipRect'),(1, 'lpFrameInfo'),)))
    IOleInPlaceSite.Scroll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.SIZE, use_last_error=False)(9, 'Scroll', ((1, 'scrollExtant'),)))
    IOleInPlaceSite.OnUIDeactivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(10, 'OnUIDeactivate', ((1, 'fUndoable'),)))
    IOleInPlaceSite.OnInPlaceDeactivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'OnInPlaceDeactivate', ()))
    IOleInPlaceSite.DiscardUndoState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'DiscardUndoState', ()))
    IOleInPlaceSite.DeactivateAndUndo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(13, 'DeactivateAndUndo', ()))
    IOleInPlaceSite.OnPosRectChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(14, 'OnPosRectChange', ((1, 'lprcPosRect'),)))
    win32more.System.Ole.IOleWindow
    return IOleInPlaceSite
def _define_IContinue_head():
    class IContinue(win32more.System.Com.IUnknown_head):
        Guid = Guid('0000012a-0000-0000-c000-000000000046')
    return IContinue
def _define_IContinue():
    IContinue = win32more.System.Ole.IContinue_head
    IContinue.FContinue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'FContinue', ()))
    win32more.System.Com.IUnknown
    return IContinue
def _define_IViewObject_head():
    class IViewObject(win32more.System.Com.IUnknown_head):
        Guid = Guid('0000010d-0000-0000-c000-000000000046')
    return IViewObject
def _define_IViewObject():
    IViewObject = win32more.System.Ole.IViewObject_head
    IViewObject.Draw = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Int32,c_void_p,POINTER(win32more.System.Com.DVTARGETDEVICE_head),win32more.Graphics.Gdi.HDC,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.RECTL_head),POINTER(win32more.Foundation.RECTL_head),IntPtr,UIntPtr, use_last_error=False)(3, 'Draw', ((1, 'dwDrawAspect'),(1, 'lindex'),(1, 'pvAspect'),(1, 'ptd'),(1, 'hdcTargetDev'),(1, 'hdcDraw'),(1, 'lprcBounds'),(1, 'lprcWBounds'),(1, 'pfnContinue'),(1, 'dwContinue'),)))
    IViewObject.GetColorSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Int32,c_void_p,POINTER(win32more.System.Com.DVTARGETDEVICE_head),win32more.Graphics.Gdi.HDC,POINTER(POINTER(win32more.Graphics.Gdi.LOGPALETTE_head)), use_last_error=False)(4, 'GetColorSet', ((1, 'dwDrawAspect'),(1, 'lindex'),(1, 'pvAspect'),(1, 'ptd'),(1, 'hicTargetDev'),(1, 'ppColorSet'),)))
    IViewObject.Freeze = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Int32,c_void_p,POINTER(UInt32), use_last_error=False)(5, 'Freeze', ((1, 'dwDrawAspect'),(1, 'lindex'),(1, 'pvAspect'),(1, 'pdwFreeze'),)))
    IViewObject.Unfreeze = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'Unfreeze', ((1, 'dwFreeze'),)))
    IViewObject.SetAdvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,win32more.System.Com.IAdviseSink_head, use_last_error=False)(7, 'SetAdvise', ((1, 'aspects'),(1, 'advf'),(1, 'pAdvSink'),)))
    IViewObject.GetAdvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32),POINTER(win32more.System.Com.IAdviseSink_head), use_last_error=False)(8, 'GetAdvise', ((1, 'pAspects'),(1, 'pAdvf'),(1, 'ppAdvSink'),)))
    win32more.System.Com.IUnknown
    return IViewObject
def _define_IViewObject2_head():
    class IViewObject2(win32more.System.Ole.IViewObject_head):
        Guid = Guid('00000127-0000-0000-c000-000000000046')
    return IViewObject2
def _define_IViewObject2():
    IViewObject2 = win32more.System.Ole.IViewObject2_head
    IViewObject2.GetExtent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Int32,POINTER(win32more.System.Com.DVTARGETDEVICE_head),POINTER(win32more.Foundation.SIZE_head), use_last_error=False)(9, 'GetExtent', ((1, 'dwDrawAspect'),(1, 'lindex'),(1, 'ptd'),(1, 'lpsizel'),)))
    win32more.System.Ole.IViewObject
    return IViewObject2
def _define_IDropSource_head():
    class IDropSource(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000121-0000-0000-c000-000000000046')
    return IDropSource
def _define_IDropSource():
    IDropSource = win32more.System.Ole.IDropSource_head
    IDropSource.QueryContinueDrag = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,UInt32, use_last_error=False)(3, 'QueryContinueDrag', ((1, 'fEscapePressed'),(1, 'grfKeyState'),)))
    IDropSource.GiveFeedback = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'GiveFeedback', ((1, 'dwEffect'),)))
    win32more.System.Com.IUnknown
    return IDropSource
def _define_IDropTarget_head():
    class IDropTarget(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000122-0000-0000-c000-000000000046')
    return IDropTarget
def _define_IDropTarget():
    IDropTarget = win32more.System.Ole.IDropTarget_head
    IDropTarget.DragEnter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head,UInt32,win32more.Foundation.POINTL,POINTER(UInt32), use_last_error=False)(3, 'DragEnter', ((1, 'pDataObj'),(1, 'grfKeyState'),(1, 'pt'),(1, 'pdwEffect'),)))
    IDropTarget.DragOver = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.POINTL,POINTER(UInt32), use_last_error=False)(4, 'DragOver', ((1, 'grfKeyState'),(1, 'pt'),(1, 'pdwEffect'),)))
    IDropTarget.DragLeave = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'DragLeave', ()))
    IDropTarget.Drop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head,UInt32,win32more.Foundation.POINTL,POINTER(UInt32), use_last_error=False)(6, 'Drop', ((1, 'pDataObj'),(1, 'grfKeyState'),(1, 'pt'),(1, 'pdwEffect'),)))
    win32more.System.Com.IUnknown
    return IDropTarget
def _define_IDropSourceNotify_head():
    class IDropSourceNotify(win32more.System.Com.IUnknown_head):
        Guid = Guid('0000012b-0000-0000-c000-000000000046')
    return IDropSourceNotify
def _define_IDropSourceNotify():
    IDropSourceNotify = win32more.System.Ole.IDropSourceNotify_head
    IDropSourceNotify.DragEnterTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND, use_last_error=False)(3, 'DragEnterTarget', ((1, 'hwndTarget'),)))
    IDropSourceNotify.DragLeaveTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'DragLeaveTarget', ()))
    win32more.System.Com.IUnknown
    return IDropSourceNotify
def _define_IEnterpriseDropTarget_head():
    class IEnterpriseDropTarget(win32more.System.Com.IUnknown_head):
        Guid = Guid('390e3878-fd55-4e18-819d-4682081c0cfd')
    return IEnterpriseDropTarget
def _define_IEnterpriseDropTarget():
    IEnterpriseDropTarget = win32more.System.Ole.IEnterpriseDropTarget_head
    IEnterpriseDropTarget.SetDropSourceEnterpriseId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(3, 'SetDropSourceEnterpriseId', ((1, 'identity'),)))
    IEnterpriseDropTarget.IsEvaluatingEdpPolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(4, 'IsEvaluatingEdpPolicy', ((1, 'value'),)))
    win32more.System.Com.IUnknown
    return IEnterpriseDropTarget
def _define_OLEVERB_head():
    class OLEVERB(Structure):
        pass
    return OLEVERB
def _define_OLEVERB():
    OLEVERB = win32more.System.Ole.OLEVERB_head
    OLEVERB._fields_ = [
        ("lVerb", Int32),
        ("lpszVerbName", win32more.Foundation.PWSTR),
        ("fuFlags", UInt32),
        ("grfAttribs", UInt32),
    ]
    return OLEVERB
OLEVERBATTRIB = Int32
OLEVERBATTRIB_NEVERDIRTIES = 1
OLEVERBATTRIB_ONCONTAINERMENU = 2
def _define_IEnumOLEVERB_head():
    class IEnumOLEVERB(win32more.System.Com.IUnknown_head):
        Guid = Guid('00000104-0000-0000-c000-000000000046')
    return IEnumOLEVERB
def _define_IEnumOLEVERB():
    IEnumOLEVERB = win32more.System.Ole.IEnumOLEVERB_head
    IEnumOLEVERB.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Ole.OLEVERB),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'celt'),(1, 'rgelt'),(1, 'pceltFetched'),)))
    IEnumOLEVERB.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'celt'),)))
    IEnumOLEVERB.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumOLEVERB.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IEnumOLEVERB_head), use_last_error=False)(6, 'Clone', ((1, 'ppenum'),)))
    win32more.System.Com.IUnknown
    return IEnumOLEVERB
def _define_NUMPARSE_head():
    class NUMPARSE(Structure):
        pass
    return NUMPARSE
def _define_NUMPARSE():
    NUMPARSE = win32more.System.Ole.NUMPARSE_head
    NUMPARSE._fields_ = [
        ("cDig", Int32),
        ("dwInFlags", UInt32),
        ("dwOutFlags", UInt32),
        ("cchUsed", Int32),
        ("nBaseShift", Int32),
        ("nPwr10", Int32),
    ]
    return NUMPARSE
def _define_UDATE_head():
    class UDATE(Structure):
        pass
    return UDATE
def _define_UDATE():
    UDATE = win32more.System.Ole.UDATE_head
    UDATE._fields_ = [
        ("st", win32more.Foundation.SYSTEMTIME),
        ("wDayOfYear", UInt16),
    ]
    return UDATE
REGKIND = Int32
REGKIND_DEFAULT = 0
REGKIND_REGISTER = 1
REGKIND_NONE = 2
def _define_PARAMDATA_head():
    class PARAMDATA(Structure):
        pass
    return PARAMDATA
def _define_PARAMDATA():
    PARAMDATA = win32more.System.Ole.PARAMDATA_head
    PARAMDATA._fields_ = [
        ("szName", win32more.Foundation.PWSTR),
        ("vt", UInt16),
    ]
    return PARAMDATA
def _define_METHODDATA_head():
    class METHODDATA(Structure):
        pass
    return METHODDATA
def _define_METHODDATA():
    METHODDATA = win32more.System.Ole.METHODDATA_head
    METHODDATA._fields_ = [
        ("szName", win32more.Foundation.PWSTR),
        ("ppdata", POINTER(win32more.System.Ole.PARAMDATA_head)),
        ("dispid", Int32),
        ("iMeth", UInt32),
        ("cc", win32more.System.Com.CALLCONV),
        ("cArgs", UInt32),
        ("wFlags", UInt16),
        ("vtReturn", UInt16),
    ]
    return METHODDATA
def _define_INTERFACEDATA_head():
    class INTERFACEDATA(Structure):
        pass
    return INTERFACEDATA
def _define_INTERFACEDATA():
    INTERFACEDATA = win32more.System.Ole.INTERFACEDATA_head
    INTERFACEDATA._fields_ = [
        ("pmethdata", POINTER(win32more.System.Ole.METHODDATA_head)),
        ("cMembers", UInt32),
    ]
    return INTERFACEDATA
UASFLAGS = Int32
UAS_NORMAL = 0
UAS_BLOCKED = 1
UAS_NOPARENTENABLE = 2
UAS_MASK = 3
READYSTATE = Int32
READYSTATE_UNINITIALIZED = 0
READYSTATE_LOADING = 1
READYSTATE_LOADED = 2
READYSTATE_INTERACTIVE = 3
READYSTATE_COMPLETE = 4
def _define_LICINFO_head():
    class LICINFO(Structure):
        pass
    return LICINFO
def _define_LICINFO():
    LICINFO = win32more.System.Ole.LICINFO_head
    LICINFO._fields_ = [
        ("cbLicInfo", Int32),
        ("fRuntimeKeyAvail", win32more.Foundation.BOOL),
        ("fLicVerified", win32more.Foundation.BOOL),
    ]
    return LICINFO
def _define_IClassFactory2_head():
    class IClassFactory2(win32more.System.Com.IClassFactory_head):
        Guid = Guid('b196b28f-bab4-101a-b69c-00aa00341d07')
    return IClassFactory2
def _define_IClassFactory2():
    IClassFactory2 = win32more.System.Ole.IClassFactory2_head
    IClassFactory2.GetLicInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.LICINFO_head), use_last_error=False)(5, 'GetLicInfo', ((1, 'pLicInfo'),)))
    IClassFactory2.RequestLicKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(6, 'RequestLicKey', ((1, 'dwReserved'),(1, 'pBstrKey'),)))
    IClassFactory2.CreateInstanceLic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.System.Com.IUnknown_head,POINTER(Guid),win32more.Foundation.BSTR,POINTER(c_void_p), use_last_error=False)(7, 'CreateInstanceLic', ((1, 'pUnkOuter'),(1, 'pUnkReserved'),(1, 'riid'),(1, 'bstrKey'),(1, 'ppvObj'),)))
    win32more.System.Com.IClassFactory
    return IClassFactory2
def _define_IProvideClassInfo_head():
    class IProvideClassInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('b196b283-bab4-101a-b69c-00aa00341d07')
    return IProvideClassInfo
def _define_IProvideClassInfo():
    IProvideClassInfo = win32more.System.Ole.IProvideClassInfo_head
    IProvideClassInfo.GetClassInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.ITypeInfo_head), use_last_error=False)(3, 'GetClassInfo', ((1, 'ppTI'),)))
    win32more.System.Com.IUnknown
    return IProvideClassInfo
GUIDKIND = Int32
GUIDKIND_DEFAULT_SOURCE_DISP_IID = 1
def _define_IProvideClassInfo2_head():
    class IProvideClassInfo2(win32more.System.Ole.IProvideClassInfo_head):
        Guid = Guid('a6bc3ac0-dbaa-11ce-9de3-00aa004bb851')
    return IProvideClassInfo2
def _define_IProvideClassInfo2():
    IProvideClassInfo2 = win32more.System.Ole.IProvideClassInfo2_head
    IProvideClassInfo2.GetGUID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid), use_last_error=False)(4, 'GetGUID', ((1, 'dwGuidKind'),(1, 'pGUID'),)))
    win32more.System.Ole.IProvideClassInfo
    return IProvideClassInfo2
def _define_IProvideMultipleClassInfo_head():
    class IProvideMultipleClassInfo(win32more.System.Ole.IProvideClassInfo2_head):
        Guid = Guid('a7aba9c1-8983-11cf-8f20-00805f2cd064')
    return IProvideMultipleClassInfo
def _define_IProvideMultipleClassInfo():
    IProvideMultipleClassInfo = win32more.System.Ole.IProvideMultipleClassInfo_head
    IProvideMultipleClassInfo.GetMultiTypeInfoCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(5, 'GetMultiTypeInfoCount', ((1, 'pcti'),)))
    IProvideMultipleClassInfo.GetInfoOfIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.Ole.MULTICLASSINFO_FLAGS,POINTER(win32more.System.Com.ITypeInfo_head),POINTER(UInt32),POINTER(UInt32),POINTER(Guid),POINTER(Guid), use_last_error=False)(6, 'GetInfoOfIndex', ((1, 'iti'),(1, 'dwFlags'),(1, 'pptiCoClass'),(1, 'pdwTIFlags'),(1, 'pcdispidReserved'),(1, 'piidPrimary'),(1, 'piidSource'),)))
    win32more.System.Ole.IProvideClassInfo2
    return IProvideMultipleClassInfo
def _define_CONTROLINFO_head():
    class CONTROLINFO(Structure):
        pass
    return CONTROLINFO
def _define_CONTROLINFO():
    CONTROLINFO = win32more.System.Ole.CONTROLINFO_head
    CONTROLINFO._fields_ = [
        ("cb", UInt32),
        ("hAccel", win32more.UI.WindowsAndMessaging.HACCEL),
        ("cAccel", UInt16),
        ("dwFlags", UInt32),
    ]
    return CONTROLINFO
CTRLINFO = Int32
CTRLINFO_EATS_RETURN = 1
CTRLINFO_EATS_ESCAPE = 2
def _define_IOleControl_head():
    class IOleControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('b196b288-bab4-101a-b69c-00aa00341d07')
    return IOleControl
def _define_IOleControl():
    IOleControl = win32more.System.Ole.IOleControl_head
    IOleControl.GetControlInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.CONTROLINFO_head), use_last_error=False)(3, 'GetControlInfo', ((1, 'pCI'),)))
    IOleControl.OnMnemonic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.WindowsAndMessaging.MSG_head), use_last_error=False)(4, 'OnMnemonic', ((1, 'pMsg'),)))
    IOleControl.OnAmbientPropertyChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(5, 'OnAmbientPropertyChange', ((1, 'dispID'),)))
    IOleControl.FreezeEvents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(6, 'FreezeEvents', ((1, 'bFreeze'),)))
    win32more.System.Com.IUnknown
    return IOleControl
def _define_POINTF_head():
    class POINTF(Structure):
        pass
    return POINTF
def _define_POINTF():
    POINTF = win32more.System.Ole.POINTF_head
    POINTF._fields_ = [
        ("x", Single),
        ("y", Single),
    ]
    return POINTF
XFORMCOORDS = Int32
XFORMCOORDS_POSITION = 1
XFORMCOORDS_SIZE = 2
XFORMCOORDS_HIMETRICTOCONTAINER = 4
XFORMCOORDS_CONTAINERTOHIMETRIC = 8
XFORMCOORDS_EVENTCOMPAT = 16
def _define_IOleControlSite_head():
    class IOleControlSite(win32more.System.Com.IUnknown_head):
        Guid = Guid('b196b289-bab4-101a-b69c-00aa00341d07')
    return IOleControlSite
def _define_IOleControlSite():
    IOleControlSite = win32more.System.Ole.IOleControlSite_head
    IOleControlSite.OnControlInfoChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'OnControlInfoChanged', ()))
    IOleControlSite.LockInPlaceActive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(4, 'LockInPlaceActive', ((1, 'fLock'),)))
    IOleControlSite.GetExtendedControl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(5, 'GetExtendedControl', ((1, 'ppDisp'),)))
    IOleControlSite.TransformCoords = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.POINTL_head),POINTER(win32more.System.Ole.POINTF_head),win32more.System.Ole.XFORMCOORDS, use_last_error=False)(6, 'TransformCoords', ((1, 'pPtlHimetric'),(1, 'pPtfContainer'),(1, 'dwFlags'),)))
    IOleControlSite.TranslateAccelerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.WindowsAndMessaging.MSG_head),UInt32, use_last_error=False)(7, 'TranslateAccelerator', ((1, 'pMsg'),(1, 'grfModifiers'),)))
    IOleControlSite.OnFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(8, 'OnFocus', ((1, 'fGotFocus'),)))
    IOleControlSite.ShowPropertyFrame = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(9, 'ShowPropertyFrame', ()))
    win32more.System.Com.IUnknown
    return IOleControlSite
def _define_PROPPAGEINFO_head():
    class PROPPAGEINFO(Structure):
        pass
    return PROPPAGEINFO
def _define_PROPPAGEINFO():
    PROPPAGEINFO = win32more.System.Ole.PROPPAGEINFO_head
    PROPPAGEINFO._fields_ = [
        ("cb", UInt32),
        ("pszTitle", win32more.Foundation.PWSTR),
        ("size", win32more.Foundation.SIZE),
        ("pszDocString", win32more.Foundation.PWSTR),
        ("pszHelpFile", win32more.Foundation.PWSTR),
        ("dwHelpContext", UInt32),
    ]
    return PROPPAGEINFO
def _define_IPropertyPage_head():
    class IPropertyPage(win32more.System.Com.IUnknown_head):
        Guid = Guid('b196b28d-bab4-101a-b69c-00aa00341d07')
    return IPropertyPage
def _define_IPropertyPage():
    IPropertyPage = win32more.System.Ole.IPropertyPage_head
    IPropertyPage.SetPageSite = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IPropertyPageSite_head, use_last_error=False)(3, 'SetPageSite', ((1, 'pPageSite'),)))
    IPropertyPage.Activate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.Foundation.RECT_head),win32more.Foundation.BOOL, use_last_error=False)(4, 'Activate', ((1, 'hWndParent'),(1, 'pRect'),(1, 'bModal'),)))
    IPropertyPage.Deactivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Deactivate', ()))
    IPropertyPage.GetPageInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.PROPPAGEINFO_head), use_last_error=False)(6, 'GetPageInfo', ((1, 'pPageInfo'),)))
    IPropertyPage.SetObjects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(7, 'SetObjects', ((1, 'cObjects'),(1, 'ppUnk'),)))
    IPropertyPage.Show = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(8, 'Show', ((1, 'nCmdShow'),)))
    IPropertyPage.Move = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(9, 'Move', ((1, 'pRect'),)))
    IPropertyPage.IsPageDirty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(10, 'IsPageDirty', ()))
    IPropertyPage.Apply = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'Apply', ()))
    IPropertyPage.Help = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(12, 'Help', ((1, 'pszHelpDir'),)))
    IPropertyPage.TranslateAccelerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.WindowsAndMessaging.MSG_head), use_last_error=False)(13, 'TranslateAccelerator', ((1, 'pMsg'),)))
    win32more.System.Com.IUnknown
    return IPropertyPage
def _define_IPropertyPage2_head():
    class IPropertyPage2(win32more.System.Ole.IPropertyPage_head):
        Guid = Guid('01e44665-24ac-101b-84ed-08002b2ec713')
    return IPropertyPage2
def _define_IPropertyPage2():
    IPropertyPage2 = win32more.System.Ole.IPropertyPage2_head
    IPropertyPage2.EditProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(14, 'EditProperty', ((1, 'dispID'),)))
    win32more.System.Ole.IPropertyPage
    return IPropertyPage2
PROPPAGESTATUS = Int32
PROPPAGESTATUS_DIRTY = 1
PROPPAGESTATUS_VALIDATE = 2
PROPPAGESTATUS_CLEAN = 4
def _define_IPropertyPageSite_head():
    class IPropertyPageSite(win32more.System.Com.IUnknown_head):
        Guid = Guid('b196b28c-bab4-101a-b69c-00aa00341d07')
    return IPropertyPageSite
def _define_IPropertyPageSite():
    IPropertyPageSite = win32more.System.Ole.IPropertyPageSite_head
    IPropertyPageSite.OnStatusChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.PROPPAGESTATUS, use_last_error=False)(3, 'OnStatusChange', ((1, 'dwFlags'),)))
    IPropertyPageSite.GetLocaleID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetLocaleID', ((1, 'pLocaleID'),)))
    IPropertyPageSite.GetPageContainer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(5, 'GetPageContainer', ((1, 'ppUnk'),)))
    IPropertyPageSite.TranslateAccelerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.WindowsAndMessaging.MSG_head), use_last_error=False)(6, 'TranslateAccelerator', ((1, 'pMsg'),)))
    win32more.System.Com.IUnknown
    return IPropertyPageSite
def _define_IPropertyNotifySink_head():
    class IPropertyNotifySink(win32more.System.Com.IUnknown_head):
        Guid = Guid('9bfbbc02-eff1-101a-84ed-00aa00341d07')
    return IPropertyNotifySink
def _define_IPropertyNotifySink():
    IPropertyNotifySink = win32more.System.Ole.IPropertyNotifySink_head
    IPropertyNotifySink.OnChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(3, 'OnChanged', ((1, 'dispID'),)))
    IPropertyNotifySink.OnRequestEdit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(4, 'OnRequestEdit', ((1, 'dispID'),)))
    win32more.System.Com.IUnknown
    return IPropertyNotifySink
def _define_CAUUID_head():
    class CAUUID(Structure):
        pass
    return CAUUID
def _define_CAUUID():
    CAUUID = win32more.System.Ole.CAUUID_head
    CAUUID._fields_ = [
        ("cElems", UInt32),
        ("pElems", POINTER(Guid)),
    ]
    return CAUUID
def _define_ISpecifyPropertyPages_head():
    class ISpecifyPropertyPages(win32more.System.Com.IUnknown_head):
        Guid = Guid('b196b28b-bab4-101a-b69c-00aa00341d07')
    return ISpecifyPropertyPages
def _define_ISpecifyPropertyPages():
    ISpecifyPropertyPages = win32more.System.Ole.ISpecifyPropertyPages_head
    ISpecifyPropertyPages.GetPages = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.CAUUID_head), use_last_error=False)(3, 'GetPages', ((1, 'pPages'),)))
    win32more.System.Com.IUnknown
    return ISpecifyPropertyPages
def _define_IPersistPropertyBag_head():
    class IPersistPropertyBag(win32more.System.Com.IPersist_head):
        Guid = Guid('37d84f60-42cb-11ce-8135-00aa004bb851')
    return IPersistPropertyBag
def _define_IPersistPropertyBag():
    IPersistPropertyBag = win32more.System.Ole.IPersistPropertyBag_head
    IPersistPropertyBag.InitNew = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'InitNew', ()))
    IPersistPropertyBag.Load = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.System.Com.IErrorLog_head, use_last_error=False)(5, 'Load', ((1, 'pPropBag'),(1, 'pErrorLog'),)))
    IPersistPropertyBag.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag_head,win32more.Foundation.BOOL,win32more.Foundation.BOOL, use_last_error=False)(6, 'Save', ((1, 'pPropBag'),(1, 'fClearDirty'),(1, 'fSaveAllProperties'),)))
    win32more.System.Com.IPersist
    return IPersistPropertyBag
def _define_ISimpleFrameSite_head():
    class ISimpleFrameSite(win32more.System.Com.IUnknown_head):
        Guid = Guid('742b0e01-14e6-101b-914e-00aa00300cab')
    return ISimpleFrameSite
def _define_ISimpleFrameSite():
    ISimpleFrameSite = win32more.System.Ole.ISimpleFrameSite_head
    ISimpleFrameSite.PreMessageFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.LRESULT),POINTER(UInt32), use_last_error=False)(3, 'PreMessageFilter', ((1, 'hWnd'),(1, 'msg'),(1, 'wp'),(1, 'lp'),(1, 'plResult'),(1, 'pdwCookie'),)))
    ISimpleFrameSite.PostMessageFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.LRESULT),UInt32, use_last_error=False)(4, 'PostMessageFilter', ((1, 'hWnd'),(1, 'msg'),(1, 'wp'),(1, 'lp'),(1, 'plResult'),(1, 'dwCookie'),)))
    win32more.System.Com.IUnknown
    return ISimpleFrameSite
def _define_IFont_head():
    class IFont(win32more.System.Com.IUnknown_head):
        Guid = Guid('bef6e002-a874-101a-8bba-00aa00300cab')
    return IFont
def _define_IFont():
    IFont = win32more.System.Ole.IFont_head
    IFont.get_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'get_Name', ((1, 'pName'),)))
    IFont.put_Name = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR, use_last_error=False)(4, 'put_Name', ((1, 'name'),)))
    IFont.get_Size = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.CY_head), use_last_error=False)(5, 'get_Size', ((1, 'pSize'),)))
    IFont.put_Size = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CY, use_last_error=False)(6, 'put_Size', ((1, 'size'),)))
    IFont.get_Bold = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(7, 'get_Bold', ((1, 'pBold'),)))
    IFont.put_Bold = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(8, 'put_Bold', ((1, 'bold'),)))
    IFont.get_Italic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(9, 'get_Italic', ((1, 'pItalic'),)))
    IFont.put_Italic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(10, 'put_Italic', ((1, 'italic'),)))
    IFont.get_Underline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(11, 'get_Underline', ((1, 'pUnderline'),)))
    IFont.put_Underline = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(12, 'put_Underline', ((1, 'underline'),)))
    IFont.get_Strikethrough = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(13, 'get_Strikethrough', ((1, 'pStrikethrough'),)))
    IFont.put_Strikethrough = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(14, 'put_Strikethrough', ((1, 'strikethrough'),)))
    IFont.get_Weight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(15, 'get_Weight', ((1, 'pWeight'),)))
    IFont.put_Weight = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(16, 'put_Weight', ((1, 'weight'),)))
    IFont.get_Charset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(17, 'get_Charset', ((1, 'pCharset'),)))
    IFont.put_Charset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16, use_last_error=False)(18, 'put_Charset', ((1, 'charset'),)))
    IFont.get_hFont = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Gdi.HFONT), use_last_error=False)(19, 'get_hFont', ((1, 'phFont'),)))
    IFont.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IFont_head), use_last_error=False)(20, 'Clone', ((1, 'ppFont'),)))
    IFont.IsEqual = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IFont_head, use_last_error=False)(21, 'IsEqual', ((1, 'pFontOther'),)))
    IFont.SetRatio = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32, use_last_error=False)(22, 'SetRatio', ((1, 'cyLogical'),(1, 'cyHimetric'),)))
    IFont.QueryTextMetrics = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Gdi.TEXTMETRICW_head), use_last_error=False)(23, 'QueryTextMetrics', ((1, 'pTM'),)))
    IFont.AddRefHfont = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Gdi.HFONT, use_last_error=False)(24, 'AddRefHfont', ((1, 'hFont'),)))
    IFont.ReleaseHfont = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Gdi.HFONT, use_last_error=False)(25, 'ReleaseHfont', ((1, 'hFont'),)))
    IFont.SetHdc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Gdi.HDC, use_last_error=False)(26, 'SetHdc', ((1, 'hDC'),)))
    win32more.System.Com.IUnknown
    return IFont
PictureAttributes = Int32
PICTURE_SCALABLE = 1
PICTURE_TRANSPARENT = 2
def _define_IPicture_head():
    class IPicture(win32more.System.Com.IUnknown_head):
        Guid = Guid('7bf80980-bf32-101a-8bbb-00aa00300cab')
    return IPicture
def _define_IPicture():
    IPicture = win32more.System.Ole.IPicture_head
    IPicture.get_Handle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'get_Handle', ((1, 'pHandle'),)))
    IPicture.get_hPal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'get_hPal', ((1, 'phPal'),)))
    IPicture.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(5, 'get_Type', ((1, 'pType'),)))
    IPicture.get_Width = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(6, 'get_Width', ((1, 'pWidth'),)))
    IPicture.get_Height = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Height', ((1, 'pHeight'),)))
    IPicture.Render = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Gdi.HDC,Int32,Int32,Int32,Int32,Int32,Int32,Int32,Int32,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(8, 'Render', ((1, 'hDC'),(1, 'x'),(1, 'y'),(1, 'cx'),(1, 'cy'),(1, 'xSrc'),(1, 'ySrc'),(1, 'cxSrc'),(1, 'cySrc'),(1, 'pRcWBounds'),)))
    IPicture.set_hPal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(9, 'set_hPal', ((1, 'hPal'),)))
    IPicture.get_CurDC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Gdi.HDC), use_last_error=False)(10, 'get_CurDC', ((1, 'phDC'),)))
    IPicture.SelectPicture = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Gdi.HDC,POINTER(win32more.Graphics.Gdi.HDC),POINTER(UInt32), use_last_error=False)(11, 'SelectPicture', ((1, 'hDCIn'),(1, 'phDCOut'),(1, 'phBmpOut'),)))
    IPicture.get_KeepOriginalFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(12, 'get_KeepOriginalFormat', ((1, 'pKeep'),)))
    IPicture.put_KeepOriginalFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(13, 'put_KeepOriginalFormat', ((1, 'keep'),)))
    IPicture.PictureChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(14, 'PictureChanged', ()))
    IPicture.SaveAsFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Foundation.BOOL,POINTER(Int32), use_last_error=False)(15, 'SaveAsFile', ((1, 'pStream'),(1, 'fSaveMemCopy'),(1, 'pCbSize'),)))
    IPicture.get_Attributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(16, 'get_Attributes', ((1, 'pDwAttr'),)))
    win32more.System.Com.IUnknown
    return IPicture
def _define_IPicture2_head():
    class IPicture2(win32more.System.Com.IUnknown_head):
        Guid = Guid('f5185dd8-2012-4b0b-aad9-f052c6bd482b')
    return IPicture2
def _define_IPicture2():
    IPicture2 = win32more.System.Ole.IPicture2_head
    IPicture2.get_Handle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UIntPtr), use_last_error=False)(3, 'get_Handle', ((1, 'pHandle'),)))
    IPicture2.get_hPal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UIntPtr), use_last_error=False)(4, 'get_hPal', ((1, 'phPal'),)))
    IPicture2.get_Type = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16), use_last_error=False)(5, 'get_Type', ((1, 'pType'),)))
    IPicture2.get_Width = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(6, 'get_Width', ((1, 'pWidth'),)))
    IPicture2.get_Height = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(7, 'get_Height', ((1, 'pHeight'),)))
    IPicture2.Render = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Gdi.HDC,Int32,Int32,Int32,Int32,Int32,Int32,Int32,Int32,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(8, 'Render', ((1, 'hDC'),(1, 'x'),(1, 'y'),(1, 'cx'),(1, 'cy'),(1, 'xSrc'),(1, 'ySrc'),(1, 'cxSrc'),(1, 'cySrc'),(1, 'pRcWBounds'),)))
    IPicture2.set_hPal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr, use_last_error=False)(9, 'set_hPal', ((1, 'hPal'),)))
    IPicture2.get_CurDC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Gdi.HDC), use_last_error=False)(10, 'get_CurDC', ((1, 'phDC'),)))
    IPicture2.SelectPicture = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Gdi.HDC,POINTER(win32more.Graphics.Gdi.HDC),POINTER(UIntPtr), use_last_error=False)(11, 'SelectPicture', ((1, 'hDCIn'),(1, 'phDCOut'),(1, 'phBmpOut'),)))
    IPicture2.get_KeepOriginalFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(12, 'get_KeepOriginalFormat', ((1, 'pKeep'),)))
    IPicture2.put_KeepOriginalFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(13, 'put_KeepOriginalFormat', ((1, 'keep'),)))
    IPicture2.PictureChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(14, 'PictureChanged', ()))
    IPicture2.SaveAsFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Foundation.BOOL,POINTER(Int32), use_last_error=False)(15, 'SaveAsFile', ((1, 'pStream'),(1, 'fSaveMemCopy'),(1, 'pCbSize'),)))
    IPicture2.get_Attributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(16, 'get_Attributes', ((1, 'pDwAttr'),)))
    win32more.System.Com.IUnknown
    return IPicture2
def _define_IFontEventsDisp_head():
    class IFontEventsDisp(win32more.System.Com.IDispatch_head):
        Guid = Guid('4ef6100a-af88-11d0-9846-00c04fc29993')
    return IFontEventsDisp
def _define_IFontEventsDisp():
    IFontEventsDisp = win32more.System.Ole.IFontEventsDisp_head
    win32more.System.Com.IDispatch
    return IFontEventsDisp
def _define_IFontDisp_head():
    class IFontDisp(win32more.System.Com.IDispatch_head):
        Guid = Guid('bef6e003-a874-101a-8bba-00aa00300cab')
    return IFontDisp
def _define_IFontDisp():
    IFontDisp = win32more.System.Ole.IFontDisp_head
    win32more.System.Com.IDispatch
    return IFontDisp
def _define_IPictureDisp_head():
    class IPictureDisp(win32more.System.Com.IDispatch_head):
        Guid = Guid('7bf80981-bf32-101a-8bbb-00aa00300cab')
    return IPictureDisp
def _define_IPictureDisp():
    IPictureDisp = win32more.System.Ole.IPictureDisp_head
    win32more.System.Com.IDispatch
    return IPictureDisp
def _define_IOleInPlaceObjectWindowless_head():
    class IOleInPlaceObjectWindowless(win32more.System.Ole.IOleInPlaceObject_head):
        Guid = Guid('1c2056cc-5ef4-101b-8bc8-00aa003e3b29')
    return IOleInPlaceObjectWindowless
def _define_IOleInPlaceObjectWindowless():
    IOleInPlaceObjectWindowless = win32more.System.Ole.IOleInPlaceObjectWindowless_head
    IOleInPlaceObjectWindowless.OnWindowMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.LRESULT), use_last_error=False)(9, 'OnWindowMessage', ((1, 'msg'),(1, 'wParam'),(1, 'lParam'),(1, 'plResult'),)))
    IOleInPlaceObjectWindowless.GetDropTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IDropTarget_head), use_last_error=False)(10, 'GetDropTarget', ((1, 'ppDropTarget'),)))
    win32more.System.Ole.IOleInPlaceObject
    return IOleInPlaceObjectWindowless
ACTIVATEFLAGS = Int32
ACTIVATE_WINDOWLESS = 1
def _define_IOleInPlaceSiteEx_head():
    class IOleInPlaceSiteEx(win32more.System.Ole.IOleInPlaceSite_head):
        Guid = Guid('9c2cad80-3424-11cf-b670-00aa004cd6d8')
    return IOleInPlaceSiteEx
def _define_IOleInPlaceSiteEx():
    IOleInPlaceSiteEx = win32more.System.Ole.IOleInPlaceSiteEx_head
    IOleInPlaceSiteEx.OnInPlaceActivateEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),UInt32, use_last_error=False)(15, 'OnInPlaceActivateEx', ((1, 'pfNoRedraw'),(1, 'dwFlags'),)))
    IOleInPlaceSiteEx.OnInPlaceDeactivateEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(16, 'OnInPlaceDeactivateEx', ((1, 'fNoRedraw'),)))
    IOleInPlaceSiteEx.RequestUIActivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(17, 'RequestUIActivate', ()))
    win32more.System.Ole.IOleInPlaceSite
    return IOleInPlaceSiteEx
OLEDCFLAGS = Int32
OLEDC_NODRAW = 1
OLEDC_PAINTBKGND = 2
OLEDC_OFFSCREEN = 4
def _define_IOleInPlaceSiteWindowless_head():
    class IOleInPlaceSiteWindowless(win32more.System.Ole.IOleInPlaceSiteEx_head):
        Guid = Guid('922eada0-3424-11cf-b670-00aa004cd6d8')
    return IOleInPlaceSiteWindowless
def _define_IOleInPlaceSiteWindowless():
    IOleInPlaceSiteWindowless = win32more.System.Ole.IOleInPlaceSiteWindowless_head
    IOleInPlaceSiteWindowless.CanWindowlessActivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(18, 'CanWindowlessActivate', ()))
    IOleInPlaceSiteWindowless.GetCapture = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(19, 'GetCapture', ()))
    IOleInPlaceSiteWindowless.SetCapture = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(20, 'SetCapture', ((1, 'fCapture'),)))
    IOleInPlaceSiteWindowless.GetFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(21, 'GetFocus', ()))
    IOleInPlaceSiteWindowless.SetFocus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(22, 'SetFocus', ((1, 'fFocus'),)))
    IOleInPlaceSiteWindowless.GetDC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head),UInt32,POINTER(win32more.Graphics.Gdi.HDC), use_last_error=False)(23, 'GetDC', ((1, 'pRect'),(1, 'grfFlags'),(1, 'phDC'),)))
    IOleInPlaceSiteWindowless.ReleaseDC = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Gdi.HDC, use_last_error=False)(24, 'ReleaseDC', ((1, 'hDC'),)))
    IOleInPlaceSiteWindowless.InvalidateRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head),win32more.Foundation.BOOL, use_last_error=False)(25, 'InvalidateRect', ((1, 'pRect'),(1, 'fErase'),)))
    IOleInPlaceSiteWindowless.InvalidateRgn = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Gdi.HRGN,win32more.Foundation.BOOL, use_last_error=False)(26, 'InvalidateRgn', ((1, 'hRGN'),(1, 'fErase'),)))
    IOleInPlaceSiteWindowless.ScrollRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.RECT_head), use_last_error=False)(27, 'ScrollRect', ((1, 'dx'),(1, 'dy'),(1, 'pRectScroll'),(1, 'pRectClip'),)))
    IOleInPlaceSiteWindowless.AdjustRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(28, 'AdjustRect', ((1, 'prc'),)))
    IOleInPlaceSiteWindowless.OnDefWindowMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM,POINTER(win32more.Foundation.LRESULT), use_last_error=False)(29, 'OnDefWindowMessage', ((1, 'msg'),(1, 'wParam'),(1, 'lParam'),(1, 'plResult'),)))
    win32more.System.Ole.IOleInPlaceSiteEx
    return IOleInPlaceSiteWindowless
VIEWSTATUS = Int32
VIEWSTATUS_OPAQUE = 1
VIEWSTATUS_SOLIDBKGND = 2
VIEWSTATUS_DVASPECTOPAQUE = 4
VIEWSTATUS_DVASPECTTRANSPARENT = 8
VIEWSTATUS_SURFACE = 16
VIEWSTATUS_3DSURFACE = 32
HITRESULT = Int32
HITRESULT_OUTSIDE = 0
HITRESULT_TRANSPARENT = 1
HITRESULT_CLOSE = 2
HITRESULT_HIT = 3
DVASPECT2 = Int32
DVASPECT_OPAQUE = 16
DVASPECT_TRANSPARENT = 32
def _define_ExtentInfo_head():
    class ExtentInfo(Structure):
        pass
    return ExtentInfo
def _define_ExtentInfo():
    ExtentInfo = win32more.System.Ole.ExtentInfo_head
    ExtentInfo._fields_ = [
        ("cb", UInt32),
        ("dwExtentMode", UInt32),
        ("sizelProposed", win32more.Foundation.SIZE),
    ]
    return ExtentInfo
ExtentMode = Int32
DVEXTENT_CONTENT = 0
DVEXTENT_INTEGRAL = 1
AspectInfoFlag = Int32
DVASPECTINFOFLAG_CANOPTIMIZE = 1
def _define_AspectInfo_head():
    class AspectInfo(Structure):
        pass
    return AspectInfo
def _define_AspectInfo():
    AspectInfo = win32more.System.Ole.AspectInfo_head
    AspectInfo._fields_ = [
        ("cb", UInt32),
        ("dwFlags", UInt32),
    ]
    return AspectInfo
def _define_IViewObjectEx_head():
    class IViewObjectEx(win32more.System.Ole.IViewObject2_head):
        Guid = Guid('3af24292-0c96-11ce-a0cf-00aa00600ab8')
    return IViewObjectEx
def _define_IViewObjectEx():
    IViewObjectEx = win32more.System.Ole.IViewObjectEx_head
    IViewObjectEx.GetRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.RECTL_head), use_last_error=False)(10, 'GetRect', ((1, 'dwAspect'),(1, 'pRect'),)))
    IViewObjectEx.GetViewStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(11, 'GetViewStatus', ((1, 'pdwStatus'),)))
    IViewObjectEx.QueryHitPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.RECT_head),win32more.Foundation.POINT,Int32,POINTER(UInt32), use_last_error=False)(12, 'QueryHitPoint', ((1, 'dwAspect'),(1, 'pRectBounds'),(1, 'ptlLoc'),(1, 'lCloseHint'),(1, 'pHitResult'),)))
    IViewObjectEx.QueryHitRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.RECT_head),Int32,POINTER(UInt32), use_last_error=False)(13, 'QueryHitRect', ((1, 'dwAspect'),(1, 'pRectBounds'),(1, 'pRectLoc'),(1, 'lCloseHint'),(1, 'pHitResult'),)))
    IViewObjectEx.GetNaturalExtent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.DVASPECT,Int32,POINTER(win32more.System.Com.DVTARGETDEVICE_head),win32more.Graphics.Gdi.HDC,POINTER(win32more.System.Ole.ExtentInfo_head),POINTER(win32more.Foundation.SIZE_head), use_last_error=False)(14, 'GetNaturalExtent', ((1, 'dwAspect'),(1, 'lindex'),(1, 'ptd'),(1, 'hicTargetDev'),(1, 'pExtentInfo'),(1, 'pSizel'),)))
    win32more.System.Ole.IViewObject2
    return IViewObjectEx
def _define_IOleUndoUnit_head():
    class IOleUndoUnit(win32more.System.Com.IUnknown_head):
        Guid = Guid('894ad3b0-ef97-11ce-9bc9-00aa00608e01')
    return IOleUndoUnit
def _define_IOleUndoUnit():
    IOleUndoUnit = win32more.System.Ole.IOleUndoUnit_head
    IOleUndoUnit.Do = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IOleUndoManager_head, use_last_error=False)(3, 'Do', ((1, 'pUndoManager'),)))
    IOleUndoUnit.GetDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(4, 'GetDescription', ((1, 'pBstr'),)))
    IOleUndoUnit.GetUnitType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Int32), use_last_error=False)(5, 'GetUnitType', ((1, 'pClsid'),(1, 'plID'),)))
    IOleUndoUnit.OnNextAdd = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(6, 'OnNextAdd', ()))
    win32more.System.Com.IUnknown
    return IOleUndoUnit
def _define_IOleParentUndoUnit_head():
    class IOleParentUndoUnit(win32more.System.Ole.IOleUndoUnit_head):
        Guid = Guid('a1faf330-ef97-11ce-9bc9-00aa00608e01')
    return IOleParentUndoUnit
def _define_IOleParentUndoUnit():
    IOleParentUndoUnit = win32more.System.Ole.IOleParentUndoUnit_head
    IOleParentUndoUnit.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IOleParentUndoUnit_head, use_last_error=False)(7, 'Open', ((1, 'pPUU'),)))
    IOleParentUndoUnit.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IOleParentUndoUnit_head,win32more.Foundation.BOOL, use_last_error=False)(8, 'Close', ((1, 'pPUU'),(1, 'fCommit'),)))
    IOleParentUndoUnit.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IOleUndoUnit_head, use_last_error=False)(9, 'Add', ((1, 'pUU'),)))
    IOleParentUndoUnit.FindUnit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IOleUndoUnit_head, use_last_error=False)(10, 'FindUnit', ((1, 'pUU'),)))
    IOleParentUndoUnit.GetParentState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(11, 'GetParentState', ((1, 'pdwState'),)))
    win32more.System.Ole.IOleUndoUnit
    return IOleParentUndoUnit
def _define_IEnumOleUndoUnits_head():
    class IEnumOleUndoUnits(win32more.System.Com.IUnknown_head):
        Guid = Guid('b3e7c340-ef97-11ce-9bc9-00aa00608e01')
    return IEnumOleUndoUnits
def _define_IEnumOleUndoUnits():
    IEnumOleUndoUnits = win32more.System.Ole.IEnumOleUndoUnits_head
    IEnumOleUndoUnits.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Ole.IOleUndoUnit_head),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'cElt'),(1, 'rgElt'),(1, 'pcEltFetched'),)))
    IEnumOleUndoUnits.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'cElt'),)))
    IEnumOleUndoUnits.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumOleUndoUnits.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IEnumOleUndoUnits_head), use_last_error=False)(6, 'Clone', ((1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return IEnumOleUndoUnits
def _define_IOleUndoManager_head():
    class IOleUndoManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('d001f200-ef97-11ce-9bc9-00aa00608e01')
    return IOleUndoManager
def _define_IOleUndoManager():
    IOleUndoManager = win32more.System.Ole.IOleUndoManager_head
    IOleUndoManager.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IOleParentUndoUnit_head, use_last_error=False)(3, 'Open', ((1, 'pPUU'),)))
    IOleUndoManager.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IOleParentUndoUnit_head,win32more.Foundation.BOOL, use_last_error=False)(4, 'Close', ((1, 'pPUU'),(1, 'fCommit'),)))
    IOleUndoManager.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IOleUndoUnit_head, use_last_error=False)(5, 'Add', ((1, 'pUU'),)))
    IOleUndoManager.GetOpenParentState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(6, 'GetOpenParentState', ((1, 'pdwState'),)))
    IOleUndoManager.DiscardFrom = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IOleUndoUnit_head, use_last_error=False)(7, 'DiscardFrom', ((1, 'pUU'),)))
    IOleUndoManager.UndoTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IOleUndoUnit_head, use_last_error=False)(8, 'UndoTo', ((1, 'pUU'),)))
    IOleUndoManager.RedoTo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IOleUndoUnit_head, use_last_error=False)(9, 'RedoTo', ((1, 'pUU'),)))
    IOleUndoManager.EnumUndoable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IEnumOleUndoUnits_head), use_last_error=False)(10, 'EnumUndoable', ((1, 'ppEnum'),)))
    IOleUndoManager.EnumRedoable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IEnumOleUndoUnits_head), use_last_error=False)(11, 'EnumRedoable', ((1, 'ppEnum'),)))
    IOleUndoManager.GetLastUndoDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'GetLastUndoDescription', ((1, 'pBstr'),)))
    IOleUndoManager.GetLastRedoDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(13, 'GetLastRedoDescription', ((1, 'pBstr'),)))
    IOleUndoManager.Enable = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(14, 'Enable', ((1, 'fEnable'),)))
    win32more.System.Com.IUnknown
    return IOleUndoManager
POINTERINACTIVE = Int32
POINTERINACTIVE_ACTIVATEONENTRY = 1
POINTERINACTIVE_DEACTIVATEONLEAVE = 2
POINTERINACTIVE_ACTIVATEONDRAG = 4
def _define_IPointerInactive_head():
    class IPointerInactive(win32more.System.Com.IUnknown_head):
        Guid = Guid('55980ba0-35aa-11cf-b671-00aa004cd6d8')
    return IPointerInactive
def _define_IPointerInactive():
    IPointerInactive = win32more.System.Ole.IPointerInactive_head
    IPointerInactive.GetActivationPolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetActivationPolicy', ((1, 'pdwPolicy'),)))
    IPointerInactive.OnInactiveMouseMove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head),Int32,Int32,UInt32, use_last_error=False)(4, 'OnInactiveMouseMove', ((1, 'pRectBounds'),(1, 'x'),(1, 'y'),(1, 'grfKeyState'),)))
    IPointerInactive.OnInactiveSetCursor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head),Int32,Int32,UInt32,win32more.Foundation.BOOL, use_last_error=False)(5, 'OnInactiveSetCursor', ((1, 'pRectBounds'),(1, 'x'),(1, 'y'),(1, 'dwMouseMsg'),(1, 'fSetAlways'),)))
    win32more.System.Com.IUnknown
    return IPointerInactive
def _define_IObjectWithSite_head():
    class IObjectWithSite(win32more.System.Com.IUnknown_head):
        Guid = Guid('fc4801a3-2ba9-11cf-a229-00aa003d7352')
    return IObjectWithSite
def _define_IObjectWithSite():
    IObjectWithSite = win32more.System.Ole.IObjectWithSite_head
    IObjectWithSite.SetSite = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(3, 'SetSite', ((1, 'pUnkSite'),)))
    IObjectWithSite.GetSite = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(4, 'GetSite', ((1, 'riid'),(1, 'ppvSite'),)))
    win32more.System.Com.IUnknown
    return IObjectWithSite
def _define_CALPOLESTR_head():
    class CALPOLESTR(Structure):
        pass
    return CALPOLESTR
def _define_CALPOLESTR():
    CALPOLESTR = win32more.System.Ole.CALPOLESTR_head
    CALPOLESTR._fields_ = [
        ("cElems", UInt32),
        ("pElems", POINTER(win32more.Foundation.PWSTR)),
    ]
    return CALPOLESTR
def _define_CADWORD_head():
    class CADWORD(Structure):
        pass
    return CADWORD
def _define_CADWORD():
    CADWORD = win32more.System.Ole.CADWORD_head
    CADWORD._fields_ = [
        ("cElems", UInt32),
        ("pElems", POINTER(UInt32)),
    ]
    return CADWORD
def _define_IPerPropertyBrowsing_head():
    class IPerPropertyBrowsing(win32more.System.Com.IUnknown_head):
        Guid = Guid('376bd3aa-3845-101b-84ed-08002b2ec713')
    return IPerPropertyBrowsing
def _define_IPerPropertyBrowsing():
    IPerPropertyBrowsing = win32more.System.Ole.IPerPropertyBrowsing_head
    IPerPropertyBrowsing.GetDisplayString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(3, 'GetDisplayString', ((1, 'dispID'),(1, 'pBstr'),)))
    IPerPropertyBrowsing.MapPropertyToPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Guid), use_last_error=False)(4, 'MapPropertyToPage', ((1, 'dispID'),(1, 'pClsid'),)))
    IPerPropertyBrowsing.GetPredefinedStrings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Ole.CALPOLESTR_head),POINTER(win32more.System.Ole.CADWORD_head), use_last_error=False)(5, 'GetPredefinedStrings', ((1, 'dispID'),(1, 'pCaStringsOut'),(1, 'pCaCookiesOut'),)))
    IPerPropertyBrowsing.GetPredefinedValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,UInt32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(6, 'GetPredefinedValue', ((1, 'dispID'),(1, 'dwCookie'),(1, 'pVarOut'),)))
    win32more.System.Com.IUnknown
    return IPerPropertyBrowsing
PROPBAG2_TYPE = Int32
PROPBAG2_TYPE_UNDEFINED = 0
PROPBAG2_TYPE_DATA = 1
PROPBAG2_TYPE_URL = 2
PROPBAG2_TYPE_OBJECT = 3
PROPBAG2_TYPE_STREAM = 4
PROPBAG2_TYPE_STORAGE = 5
PROPBAG2_TYPE_MONIKER = 6
def _define_IPersistPropertyBag2_head():
    class IPersistPropertyBag2(win32more.System.Com.IPersist_head):
        Guid = Guid('22f55881-280b-11d0-a8a9-00a0c90c2004')
    return IPersistPropertyBag2
def _define_IPersistPropertyBag2():
    IPersistPropertyBag2 = win32more.System.Ole.IPersistPropertyBag2_head
    IPersistPropertyBag2.InitNew = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'InitNew', ()))
    IPersistPropertyBag2.Load = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag2_head,win32more.System.Com.IErrorLog_head, use_last_error=False)(5, 'Load', ((1, 'pPropBag'),(1, 'pErrLog'),)))
    IPersistPropertyBag2.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPropertyBag2_head,win32more.Foundation.BOOL,win32more.Foundation.BOOL, use_last_error=False)(6, 'Save', ((1, 'pPropBag'),(1, 'fClearDirty'),(1, 'fSaveAllProperties'),)))
    IPersistPropertyBag2.IsDirty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'IsDirty', ()))
    win32more.System.Com.IPersist
    return IPersistPropertyBag2
def _define_IAdviseSinkEx_head():
    class IAdviseSinkEx(win32more.System.Com.IAdviseSink_head):
        Guid = Guid('3af24290-0c96-11ce-a0cf-00aa00600ab8')
    return IAdviseSinkEx
def _define_IAdviseSinkEx():
    IAdviseSinkEx = win32more.System.Ole.IAdviseSinkEx_head
    IAdviseSinkEx.OnViewStatusChange = COMMETHOD(WINFUNCTYPE(Void,UInt32, use_last_error=False)(8, 'OnViewStatusChange', ((1, 'dwViewStatus'),)))
    win32more.System.Com.IAdviseSink
    return IAdviseSinkEx
QACONTAINERFLAGS = Int32
QACONTAINER_SHOWHATCHING = 1
QACONTAINER_SHOWGRABHANDLES = 2
QACONTAINER_USERMODE = 4
QACONTAINER_DISPLAYASDEFAULT = 8
QACONTAINER_UIDEAD = 16
QACONTAINER_AUTOCLIP = 32
QACONTAINER_MESSAGEREFLECT = 64
QACONTAINER_SUPPORTSMNEMONICS = 128
def _define_QACONTAINER_head():
    class QACONTAINER(Structure):
        pass
    return QACONTAINER
def _define_QACONTAINER():
    QACONTAINER = win32more.System.Ole.QACONTAINER_head
    QACONTAINER._fields_ = [
        ("cbSize", UInt32),
        ("pClientSite", win32more.System.Ole.IOleClientSite_head),
        ("pAdviseSink", win32more.System.Ole.IAdviseSinkEx_head),
        ("pPropertyNotifySink", win32more.System.Ole.IPropertyNotifySink_head),
        ("pUnkEventSink", win32more.System.Com.IUnknown_head),
        ("dwAmbientFlags", UInt32),
        ("colorFore", UInt32),
        ("colorBack", UInt32),
        ("pFont", win32more.System.Ole.IFont_head),
        ("pUndoMgr", win32more.System.Ole.IOleUndoManager_head),
        ("dwAppearance", UInt32),
        ("lcid", Int32),
        ("hpal", win32more.Graphics.Gdi.HPALETTE),
        ("pBindHost", win32more.System.Com.IBindHost_head),
        ("pOleControlSite", win32more.System.Ole.IOleControlSite_head),
        ("pServiceProvider", win32more.System.Com.IServiceProvider_head),
    ]
    return QACONTAINER
def _define_QACONTROL_head():
    class QACONTROL(Structure):
        pass
    return QACONTROL
def _define_QACONTROL():
    QACONTROL = win32more.System.Ole.QACONTROL_head
    QACONTROL._fields_ = [
        ("cbSize", UInt32),
        ("dwMiscStatus", UInt32),
        ("dwViewStatus", UInt32),
        ("dwEventCookie", UInt32),
        ("dwPropNotifyCookie", UInt32),
        ("dwPointerActivationPolicy", UInt32),
    ]
    return QACONTROL
def _define_IQuickActivate_head():
    class IQuickActivate(win32more.System.Com.IUnknown_head):
        Guid = Guid('cf51ed10-62fe-11cf-bf86-00a0c9034836')
    return IQuickActivate
def _define_IQuickActivate():
    IQuickActivate = win32more.System.Ole.IQuickActivate_head
    IQuickActivate.QuickActivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.QACONTAINER_head),POINTER(win32more.System.Ole.QACONTROL_head), use_last_error=False)(3, 'QuickActivate', ((1, 'pQaContainer'),(1, 'pQaControl'),)))
    IQuickActivate.SetContentExtent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.SIZE_head), use_last_error=False)(4, 'SetContentExtent', ((1, 'pSizel'),)))
    IQuickActivate.GetContentExtent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.SIZE_head), use_last_error=False)(5, 'GetContentExtent', ((1, 'pSizel'),)))
    win32more.System.Com.IUnknown
    return IQuickActivate
def _define_OCPFIPARAMS_head():
    class OCPFIPARAMS(Structure):
        pass
    return OCPFIPARAMS
def _define_OCPFIPARAMS():
    OCPFIPARAMS = win32more.System.Ole.OCPFIPARAMS_head
    OCPFIPARAMS._fields_ = [
        ("cbStructSize", UInt32),
        ("hWndOwner", win32more.Foundation.HWND),
        ("x", Int32),
        ("y", Int32),
        ("lpszCaption", win32more.Foundation.PWSTR),
        ("cObjects", UInt32),
        ("lplpUnk", POINTER(win32more.System.Com.IUnknown_head)),
        ("cPages", UInt32),
        ("lpPages", POINTER(Guid)),
        ("lcid", UInt32),
        ("dispidInitialProperty", Int32),
    ]
    return OCPFIPARAMS
def _define_FONTDESC_head():
    class FONTDESC(Structure):
        pass
    return FONTDESC
def _define_FONTDESC():
    FONTDESC = win32more.System.Ole.FONTDESC_head
    FONTDESC._fields_ = [
        ("cbSizeofstruct", UInt32),
        ("lpstrName", win32more.Foundation.PWSTR),
        ("cySize", win32more.System.Com.CY),
        ("sWeight", Int16),
        ("sCharset", Int16),
        ("fItalic", win32more.Foundation.BOOL),
        ("fUnderline", win32more.Foundation.BOOL),
        ("fStrikethrough", win32more.Foundation.BOOL),
    ]
    return FONTDESC
def _define_PICTDESC_head():
    class PICTDESC(Structure):
        pass
    return PICTDESC
def _define_PICTDESC():
    PICTDESC = win32more.System.Ole.PICTDESC_head
    class PICTDESC__Anonymous_e__Union(Union):
        pass
    class PICTDESC__Anonymous_e__Union__icon_e__Struct(Structure):
        pass
    PICTDESC__Anonymous_e__Union__icon_e__Struct._fields_ = [
        ("hicon", win32more.UI.WindowsAndMessaging.HICON),
    ]
    class PICTDESC__Anonymous_e__Union__bmp_e__Struct(Structure):
        pass
    PICTDESC__Anonymous_e__Union__bmp_e__Struct._fields_ = [
        ("hbitmap", win32more.Graphics.Gdi.HBITMAP),
        ("hpal", win32more.Graphics.Gdi.HPALETTE),
    ]
    class PICTDESC__Anonymous_e__Union__wmf_e__Struct(Structure):
        pass
    PICTDESC__Anonymous_e__Union__wmf_e__Struct._fields_ = [
        ("hmeta", win32more.Graphics.Gdi.HMETAFILE),
        ("xExt", Int32),
        ("yExt", Int32),
    ]
    class PICTDESC__Anonymous_e__Union__emf_e__Struct(Structure):
        pass
    PICTDESC__Anonymous_e__Union__emf_e__Struct._fields_ = [
        ("hemf", win32more.Graphics.Gdi.HENHMETAFILE),
    ]
    PICTDESC__Anonymous_e__Union._fields_ = [
        ("bmp", PICTDESC__Anonymous_e__Union__bmp_e__Struct),
        ("wmf", PICTDESC__Anonymous_e__Union__wmf_e__Struct),
        ("icon", PICTDESC__Anonymous_e__Union__icon_e__Struct),
        ("emf", PICTDESC__Anonymous_e__Union__emf_e__Struct),
    ]
    PICTDESC._anonymous_ = [
        'Anonymous',
    ]
    PICTDESC._fields_ = [
        ("cbSizeofstruct", UInt32),
        ("picType", UInt32),
        ("Anonymous", PICTDESC__Anonymous_e__Union),
    ]
    return PICTDESC
OLE_TRISTATE = Int32
OLE_TRISTATE_triUnchecked = 0
OLE_TRISTATE_triChecked = 1
OLE_TRISTATE_triGray = 2
def _define_IVBGetControl_head():
    class IVBGetControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('40a050a0-3c31-101b-a82e-08002b2b2337')
    return IVBGetControl
def _define_IVBGetControl():
    IVBGetControl = win32more.System.Ole.IVBGetControl_head
    IVBGetControl.EnumControls = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.OLECONTF,win32more.System.Ole.ENUM_CONTROLS_WHICH_FLAGS,POINTER(win32more.System.Com.IEnumUnknown_head), use_last_error=False)(3, 'EnumControls', ((1, 'dwOleContF'),(1, 'dwWhich'),(1, 'ppenumUnk'),)))
    win32more.System.Com.IUnknown
    return IVBGetControl
def _define_IGetOleObject_head():
    class IGetOleObject(win32more.System.Com.IUnknown_head):
        Guid = Guid('8a701da0-4feb-101b-a82e-08002b2b2337')
    return IGetOleObject
def _define_IGetOleObject():
    IGetOleObject = win32more.System.Ole.IGetOleObject_head
    IGetOleObject.GetOleObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(3, 'GetOleObject', ((1, 'riid'),(1, 'ppvObj'),)))
    win32more.System.Com.IUnknown
    return IGetOleObject
def _define_IVBFormat_head():
    class IVBFormat(win32more.System.Com.IUnknown_head):
        Guid = Guid('9849fd60-3768-101b-8d72-ae6164ffe3cf')
    return IVBFormat
def _define_IVBFormat():
    IVBFormat = win32more.System.Ole.IVBFormat_head
    IVBFormat.Format = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),win32more.Foundation.BSTR,c_void_p,UInt16,Int32,Int16,UInt16,POINTER(UInt16), use_last_error=False)(3, 'Format', ((1, 'vData'),(1, 'bstrFormat'),(1, 'lpBuffer'),(1, 'cb'),(1, 'lcid'),(1, 'sFirstDayOfWeek'),(1, 'sFirstWeekOfYear'),(1, 'rcb'),)))
    win32more.System.Com.IUnknown
    return IVBFormat
def _define_IGetVBAObject_head():
    class IGetVBAObject(win32more.System.Com.IUnknown_head):
        Guid = Guid('91733a60-3f4c-101b-a3f6-00aa0034e4e9')
    return IGetVBAObject
def _define_IGetVBAObject():
    IGetVBAObject = win32more.System.Ole.IGetVBAObject_head
    IGetVBAObject.GetObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_void_p),UInt32, use_last_error=False)(3, 'GetObject', ((1, 'riid'),(1, 'ppvObj'),(1, 'dwReserved'),)))
    win32more.System.Com.IUnknown
    return IGetVBAObject
DOCMISC = Int32
DOCMISC_CANCREATEMULTIPLEVIEWS = 1
DOCMISC_SUPPORTCOMPLEXRECTANGLES = 2
DOCMISC_CANTOPENEDIT = 4
DOCMISC_NOFILESUPPORT = 8
def _define_IOleDocument_head():
    class IOleDocument(win32more.System.Com.IUnknown_head):
        Guid = Guid('b722bcc5-4e68-101b-a2bc-00aa00404770')
    return IOleDocument
def _define_IOleDocument():
    IOleDocument = win32more.System.Ole.IOleDocument_head
    IOleDocument.CreateView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IOleInPlaceSite_head,win32more.System.Com.IStream_head,UInt32,POINTER(win32more.System.Ole.IOleDocumentView_head), use_last_error=False)(3, 'CreateView', ((1, 'pIPSite'),(1, 'pstm'),(1, 'dwReserved'),(1, 'ppView'),)))
    IOleDocument.GetDocMiscStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(4, 'GetDocMiscStatus', ((1, 'pdwStatus'),)))
    IOleDocument.EnumViews = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IEnumOleDocumentViews_head),POINTER(win32more.System.Ole.IOleDocumentView_head), use_last_error=False)(5, 'EnumViews', ((1, 'ppEnum'),(1, 'ppView'),)))
    win32more.System.Com.IUnknown
    return IOleDocument
def _define_IOleDocumentSite_head():
    class IOleDocumentSite(win32more.System.Com.IUnknown_head):
        Guid = Guid('b722bcc7-4e68-101b-a2bc-00aa00404770')
    return IOleDocumentSite
def _define_IOleDocumentSite():
    IOleDocumentSite = win32more.System.Ole.IOleDocumentSite_head
    IOleDocumentSite.ActivateMe = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IOleDocumentView_head, use_last_error=False)(3, 'ActivateMe', ((1, 'pViewToActivate'),)))
    win32more.System.Com.IUnknown
    return IOleDocumentSite
def _define_IOleDocumentView_head():
    class IOleDocumentView(win32more.System.Com.IUnknown_head):
        Guid = Guid('b722bcc6-4e68-101b-a2bc-00aa00404770')
    return IOleDocumentView
def _define_IOleDocumentView():
    IOleDocumentView = win32more.System.Ole.IOleDocumentView_head
    IOleDocumentView.SetInPlaceSite = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IOleInPlaceSite_head, use_last_error=False)(3, 'SetInPlaceSite', ((1, 'pIPSite'),)))
    IOleDocumentView.GetInPlaceSite = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IOleInPlaceSite_head), use_last_error=False)(4, 'GetInPlaceSite', ((1, 'ppIPSite'),)))
    IOleDocumentView.GetDocument = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(5, 'GetDocument', ((1, 'ppunk'),)))
    IOleDocumentView.SetRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(6, 'SetRect', ((1, 'prcView'),)))
    IOleDocumentView.GetRect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(7, 'GetRect', ((1, 'prcView'),)))
    IOleDocumentView.SetRectComplex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.RECT_head),POINTER(win32more.Foundation.RECT_head), use_last_error=False)(8, 'SetRectComplex', ((1, 'prcView'),(1, 'prcHScroll'),(1, 'prcVScroll'),(1, 'prcSizeBox'),)))
    IOleDocumentView.Show = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(9, 'Show', ((1, 'fShow'),)))
    IOleDocumentView.UIActivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(10, 'UIActivate', ((1, 'fUIActivate'),)))
    IOleDocumentView.Open = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'Open', ()))
    IOleDocumentView.CloseView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(12, 'CloseView', ((1, 'dwReserved'),)))
    IOleDocumentView.SaveViewState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head, use_last_error=False)(13, 'SaveViewState', ((1, 'pstm'),)))
    IOleDocumentView.ApplyViewState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head, use_last_error=False)(14, 'ApplyViewState', ((1, 'pstm'),)))
    IOleDocumentView.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IOleInPlaceSite_head,POINTER(win32more.System.Ole.IOleDocumentView_head), use_last_error=False)(15, 'Clone', ((1, 'pIPSiteNew'),(1, 'ppViewNew'),)))
    win32more.System.Com.IUnknown
    return IOleDocumentView
def _define_IEnumOleDocumentViews_head():
    class IEnumOleDocumentViews(win32more.System.Com.IUnknown_head):
        Guid = Guid('b722bcc8-4e68-101b-a2bc-00aa00404770')
    return IEnumOleDocumentViews
def _define_IEnumOleDocumentViews():
    IEnumOleDocumentViews = win32more.System.Ole.IEnumOleDocumentViews_head
    IEnumOleDocumentViews.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Ole.IOleDocumentView_head),POINTER(UInt32), use_last_error=False)(3, 'Next', ((1, 'cViews'),(1, 'rgpView'),(1, 'pcFetched'),)))
    IEnumOleDocumentViews.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'Skip', ((1, 'cViews'),)))
    IEnumOleDocumentViews.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Reset', ()))
    IEnumOleDocumentViews.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IEnumOleDocumentViews_head), use_last_error=False)(6, 'Clone', ((1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return IEnumOleDocumentViews
def _define_IContinueCallback_head():
    class IContinueCallback(win32more.System.Com.IUnknown_head):
        Guid = Guid('b722bcca-4e68-101b-a2bc-00aa00404770')
    return IContinueCallback
def _define_IContinueCallback():
    IContinueCallback = win32more.System.Ole.IContinueCallback_head
    IContinueCallback.FContinue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'FContinue', ()))
    IContinueCallback.FContinuePrinting = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,win32more.Foundation.PWSTR, use_last_error=False)(4, 'FContinuePrinting', ((1, 'nCntPrinted'),(1, 'nCurPage'),(1, 'pwszPrintStatus'),)))
    win32more.System.Com.IUnknown
    return IContinueCallback
PRINTFLAG = UInt32
PRINTFLAG_MAYBOTHERUSER = 1
PRINTFLAG_PROMPTUSER = 2
PRINTFLAG_USERMAYCHANGEPRINTER = 4
PRINTFLAG_RECOMPOSETODEVICE = 8
PRINTFLAG_DONTACTUALLYPRINT = 16
PRINTFLAG_FORCEPROPERTIES = 32
PRINTFLAG_PRINTTOFILE = 64
def _define_PAGERANGE_head():
    class PAGERANGE(Structure):
        pass
    return PAGERANGE
def _define_PAGERANGE():
    PAGERANGE = win32more.System.Ole.PAGERANGE_head
    PAGERANGE._fields_ = [
        ("nFromPage", Int32),
        ("nToPage", Int32),
    ]
    return PAGERANGE
def _define_PAGESET_head():
    class PAGESET(Structure):
        pass
    return PAGESET
def _define_PAGESET():
    PAGESET = win32more.System.Ole.PAGESET_head
    PAGESET._fields_ = [
        ("cbStruct", UInt32),
        ("fOddPages", win32more.Foundation.BOOL),
        ("fEvenPages", win32more.Foundation.BOOL),
        ("cPageRange", UInt32),
        ("rgPages", win32more.System.Ole.PAGERANGE * 0),
    ]
    return PAGESET
def _define_IPrint_head():
    class IPrint(win32more.System.Com.IUnknown_head):
        Guid = Guid('b722bcc9-4e68-101b-a2bc-00aa00404770')
    return IPrint
def _define_IPrint():
    IPrint = win32more.System.Ole.IPrint_head
    IPrint.SetInitialPageNum = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(3, 'SetInitialPageNum', ((1, 'nFirstPage'),)))
    IPrint.GetPageInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),POINTER(Int32), use_last_error=False)(4, 'GetPageInfo', ((1, 'pnFirstPage'),(1, 'pcPages'),)))
    IPrint.Print = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(win32more.System.Com.DVTARGETDEVICE_head)),POINTER(POINTER(win32more.System.Ole.PAGESET_head)),POINTER(win32more.System.Com.STGMEDIUM_head),win32more.System.Ole.IContinueCallback_head,Int32,POINTER(Int32),POINTER(Int32), use_last_error=False)(5, 'Print', ((1, 'grfFlags'),(1, 'pptd'),(1, 'ppPageSet'),(1, 'pstgmOptions'),(1, 'pcallback'),(1, 'nFirstPage'),(1, 'pcPagesPrinted'),(1, 'pnLastPage'),)))
    win32more.System.Com.IUnknown
    return IPrint
OLECMDF = Int32
OLECMDF_SUPPORTED = 1
OLECMDF_ENABLED = 2
OLECMDF_LATCHED = 4
OLECMDF_NINCHED = 8
OLECMDF_INVISIBLE = 16
OLECMDF_DEFHIDEONCTXTMENU = 32
def _define_OLECMD_head():
    class OLECMD(Structure):
        pass
    return OLECMD
def _define_OLECMD():
    OLECMD = win32more.System.Ole.OLECMD_head
    OLECMD._fields_ = [
        ("cmdID", UInt32),
        ("cmdf", UInt32),
    ]
    return OLECMD
def _define_OLECMDTEXT_head():
    class OLECMDTEXT(Structure):
        pass
    return OLECMDTEXT
def _define_OLECMDTEXT():
    OLECMDTEXT = win32more.System.Ole.OLECMDTEXT_head
    OLECMDTEXT._fields_ = [
        ("cmdtextf", UInt32),
        ("cwActual", UInt32),
        ("cwBuf", UInt32),
        ("rgwz", Char * 0),
    ]
    return OLECMDTEXT
OLECMDTEXTF = Int32
OLECMDTEXTF_NONE = 0
OLECMDTEXTF_NAME = 1
OLECMDTEXTF_STATUS = 2
OLECMDEXECOPT = Int32
OLECMDEXECOPT_DODEFAULT = 0
OLECMDEXECOPT_PROMPTUSER = 1
OLECMDEXECOPT_DONTPROMPTUSER = 2
OLECMDEXECOPT_SHOWHELP = 3
OLECMDID = Int32
OLECMDID_OPEN = 1
OLECMDID_NEW = 2
OLECMDID_SAVE = 3
OLECMDID_SAVEAS = 4
OLECMDID_SAVECOPYAS = 5
OLECMDID_PRINT = 6
OLECMDID_PRINTPREVIEW = 7
OLECMDID_PAGESETUP = 8
OLECMDID_SPELL = 9
OLECMDID_PROPERTIES = 10
OLECMDID_CUT = 11
OLECMDID_COPY = 12
OLECMDID_PASTE = 13
OLECMDID_PASTESPECIAL = 14
OLECMDID_UNDO = 15
OLECMDID_REDO = 16
OLECMDID_SELECTALL = 17
OLECMDID_CLEARSELECTION = 18
OLECMDID_ZOOM = 19
OLECMDID_GETZOOMRANGE = 20
OLECMDID_UPDATECOMMANDS = 21
OLECMDID_REFRESH = 22
OLECMDID_STOP = 23
OLECMDID_HIDETOOLBARS = 24
OLECMDID_SETPROGRESSMAX = 25
OLECMDID_SETPROGRESSPOS = 26
OLECMDID_SETPROGRESSTEXT = 27
OLECMDID_SETTITLE = 28
OLECMDID_SETDOWNLOADSTATE = 29
OLECMDID_STOPDOWNLOAD = 30
OLECMDID_ONTOOLBARACTIVATED = 31
OLECMDID_FIND = 32
OLECMDID_DELETE = 33
OLECMDID_HTTPEQUIV = 34
OLECMDID_HTTPEQUIV_DONE = 35
OLECMDID_ENABLE_INTERACTION = 36
OLECMDID_ONUNLOAD = 37
OLECMDID_PROPERTYBAG2 = 38
OLECMDID_PREREFRESH = 39
OLECMDID_SHOWSCRIPTERROR = 40
OLECMDID_SHOWMESSAGE = 41
OLECMDID_SHOWFIND = 42
OLECMDID_SHOWPAGESETUP = 43
OLECMDID_SHOWPRINT = 44
OLECMDID_CLOSE = 45
OLECMDID_ALLOWUILESSSAVEAS = 46
OLECMDID_DONTDOWNLOADCSS = 47
OLECMDID_UPDATEPAGESTATUS = 48
OLECMDID_PRINT2 = 49
OLECMDID_PRINTPREVIEW2 = 50
OLECMDID_SETPRINTTEMPLATE = 51
OLECMDID_GETPRINTTEMPLATE = 52
OLECMDID_PAGEACTIONBLOCKED = 55
OLECMDID_PAGEACTIONUIQUERY = 56
OLECMDID_FOCUSVIEWCONTROLS = 57
OLECMDID_FOCUSVIEWCONTROLSQUERY = 58
OLECMDID_SHOWPAGEACTIONMENU = 59
OLECMDID_ADDTRAVELENTRY = 60
OLECMDID_UPDATETRAVELENTRY = 61
OLECMDID_UPDATEBACKFORWARDSTATE = 62
OLECMDID_OPTICAL_ZOOM = 63
OLECMDID_OPTICAL_GETZOOMRANGE = 64
OLECMDID_WINDOWSTATECHANGED = 65
OLECMDID_ACTIVEXINSTALLSCOPE = 66
OLECMDID_UPDATETRAVELENTRY_DATARECOVERY = 67
OLECMDID_SHOWTASKDLG = 68
OLECMDID_POPSTATEEVENT = 69
OLECMDID_VIEWPORT_MODE = 70
OLECMDID_LAYOUT_VIEWPORT_WIDTH = 71
OLECMDID_VISUAL_VIEWPORT_EXCLUDE_BOTTOM = 72
OLECMDID_USER_OPTICAL_ZOOM = 73
OLECMDID_PAGEAVAILABLE = 74
OLECMDID_GETUSERSCALABLE = 75
OLECMDID_UPDATE_CARET = 76
OLECMDID_ENABLE_VISIBILITY = 77
OLECMDID_MEDIA_PLAYBACK = 78
OLECMDID_SETFAVICON = 79
OLECMDID_SET_HOST_FULLSCREENMODE = 80
OLECMDID_EXITFULLSCREEN = 81
OLECMDID_SCROLLCOMPLETE = 82
OLECMDID_ONBEFOREUNLOAD = 83
OLECMDID_SHOWMESSAGE_BLOCKABLE = 84
OLECMDID_SHOWTASKDLG_BLOCKABLE = 85
MEDIAPLAYBACK_STATE = Int32
MEDIAPLAYBACK_RESUME = 0
MEDIAPLAYBACK_PAUSE = 1
MEDIAPLAYBACK_PAUSE_AND_SUSPEND = 2
MEDIAPLAYBACK_RESUME_FROM_SUSPEND = 3
IGNOREMIME = Int32
IGNOREMIME_PROMPT = 1
IGNOREMIME_TEXT = 2
WPCSETTING = Int32
WPCSETTING_LOGGING_ENABLED = 1
WPCSETTING_FILEDOWNLOAD_BLOCKED = 2
def _define_IOleCommandTarget_head():
    class IOleCommandTarget(win32more.System.Com.IUnknown_head):
        Guid = Guid('b722bccb-4e68-101b-a2bc-00aa00404770')
    return IOleCommandTarget
def _define_IOleCommandTarget():
    IOleCommandTarget = win32more.System.Ole.IOleCommandTarget_head
    IOleCommandTarget.QueryStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(win32more.System.Ole.OLECMD_head),POINTER(win32more.System.Ole.OLECMDTEXT_head), use_last_error=False)(3, 'QueryStatus', ((1, 'pguidCmdGroup'),(1, 'cCmds'),(1, 'prgCmds'),(1, 'pCmdText'),)))
    IOleCommandTarget.Exec = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,UInt32,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(4, 'Exec', ((1, 'pguidCmdGroup'),(1, 'nCmdID'),(1, 'nCmdexecopt'),(1, 'pvaIn'),(1, 'pvaOut'),)))
    win32more.System.Com.IUnknown
    return IOleCommandTarget
OLECMDID_REFRESHFLAG = Int32
OLECMDIDF_REFRESH_NORMAL = 0
OLECMDIDF_REFRESH_IFEXPIRED = 1
OLECMDIDF_REFRESH_CONTINUE = 2
OLECMDIDF_REFRESH_COMPLETELY = 3
OLECMDIDF_REFRESH_NO_CACHE = 4
OLECMDIDF_REFRESH_RELOAD = 5
OLECMDIDF_REFRESH_LEVELMASK = 255
OLECMDIDF_REFRESH_CLEARUSERINPUT = 4096
OLECMDIDF_REFRESH_PROMPTIFOFFLINE = 8192
OLECMDIDF_REFRESH_THROUGHSCRIPT = 16384
OLECMDIDF_REFRESH_SKIPBEFOREUNLOADEVENT = 32768
OLECMDIDF_REFRESH_PAGEACTION_ACTIVEXINSTALL = 65536
OLECMDIDF_REFRESH_PAGEACTION_FILEDOWNLOAD = 131072
OLECMDIDF_REFRESH_PAGEACTION_LOCALMACHINE = 262144
OLECMDIDF_REFRESH_PAGEACTION_POPUPWINDOW = 524288
OLECMDIDF_REFRESH_PAGEACTION_PROTLOCKDOWNLOCALMACHINE = 1048576
OLECMDIDF_REFRESH_PAGEACTION_PROTLOCKDOWNTRUSTED = 2097152
OLECMDIDF_REFRESH_PAGEACTION_PROTLOCKDOWNINTRANET = 4194304
OLECMDIDF_REFRESH_PAGEACTION_PROTLOCKDOWNINTERNET = 8388608
OLECMDIDF_REFRESH_PAGEACTION_PROTLOCKDOWNRESTRICTED = 16777216
OLECMDIDF_REFRESH_PAGEACTION_MIXEDCONTENT = 33554432
OLECMDIDF_REFRESH_PAGEACTION_INVALID_CERT = 67108864
OLECMDIDF_REFRESH_PAGEACTION_ALLOW_VERSION = 134217728
OLECMDID_PAGEACTIONFLAG = Int32
OLECMDIDF_PAGEACTION_FILEDOWNLOAD = 1
OLECMDIDF_PAGEACTION_ACTIVEXINSTALL = 2
OLECMDIDF_PAGEACTION_ACTIVEXTRUSTFAIL = 4
OLECMDIDF_PAGEACTION_ACTIVEXUSERDISABLE = 8
OLECMDIDF_PAGEACTION_ACTIVEXDISALLOW = 16
OLECMDIDF_PAGEACTION_ACTIVEXUNSAFE = 32
OLECMDIDF_PAGEACTION_POPUPWINDOW = 64
OLECMDIDF_PAGEACTION_LOCALMACHINE = 128
OLECMDIDF_PAGEACTION_MIMETEXTPLAIN = 256
OLECMDIDF_PAGEACTION_SCRIPTNAVIGATE = 512
OLECMDIDF_PAGEACTION_SCRIPTNAVIGATE_ACTIVEXINSTALL = 512
OLECMDIDF_PAGEACTION_PROTLOCKDOWNLOCALMACHINE = 1024
OLECMDIDF_PAGEACTION_PROTLOCKDOWNTRUSTED = 2048
OLECMDIDF_PAGEACTION_PROTLOCKDOWNINTRANET = 4096
OLECMDIDF_PAGEACTION_PROTLOCKDOWNINTERNET = 8192
OLECMDIDF_PAGEACTION_PROTLOCKDOWNRESTRICTED = 16384
OLECMDIDF_PAGEACTION_PROTLOCKDOWNDENY = 32768
OLECMDIDF_PAGEACTION_POPUPALLOWED = 65536
OLECMDIDF_PAGEACTION_SCRIPTPROMPT = 131072
OLECMDIDF_PAGEACTION_ACTIVEXUSERAPPROVAL = 262144
OLECMDIDF_PAGEACTION_MIXEDCONTENT = 524288
OLECMDIDF_PAGEACTION_INVALID_CERT = 1048576
OLECMDIDF_PAGEACTION_INTRANETZONEREQUEST = 2097152
OLECMDIDF_PAGEACTION_XSSFILTERED = 4194304
OLECMDIDF_PAGEACTION_SPOOFABLEIDNHOST = 8388608
OLECMDIDF_PAGEACTION_ACTIVEX_EPM_INCOMPATIBLE = 16777216
OLECMDIDF_PAGEACTION_SCRIPTNAVIGATE_ACTIVEXUSERAPPROVAL = 33554432
OLECMDIDF_PAGEACTION_WPCBLOCKED = 67108864
OLECMDIDF_PAGEACTION_WPCBLOCKED_ACTIVEX = 134217728
OLECMDIDF_PAGEACTION_EXTENSION_COMPAT_BLOCKED = 268435456
OLECMDIDF_PAGEACTION_NORESETACTIVEX = 536870912
OLECMDIDF_PAGEACTION_GENERIC_STATE = 1073741824
OLECMDIDF_PAGEACTION_RESET = -2147483648
OLECMDID_BROWSERSTATEFLAG = Int32
OLECMDIDF_BROWSERSTATE_EXTENSIONSOFF = 1
OLECMDIDF_BROWSERSTATE_IESECURITY = 2
OLECMDIDF_BROWSERSTATE_PROTECTEDMODE_OFF = 4
OLECMDIDF_BROWSERSTATE_RESET = 8
OLECMDIDF_BROWSERSTATE_REQUIRESACTIVEX = 16
OLECMDIDF_BROWSERSTATE_DESKTOPHTMLDIALOG = 32
OLECMDIDF_BROWSERSTATE_BLOCKEDVERSION = 64
OLECMDID_OPTICAL_ZOOMFLAG = Int32
OLECMDIDF_OPTICAL_ZOOM_NOPERSIST = 1
OLECMDIDF_OPTICAL_ZOOM_NOLAYOUT = 16
OLECMDIDF_OPTICAL_ZOOM_NOTRANSIENT = 32
OLECMDIDF_OPTICAL_ZOOM_RELOADFORNEWTAB = 64
PAGEACTION_UI = Int32
PAGEACTION_UI_DEFAULT = 0
PAGEACTION_UI_MODAL = 1
PAGEACTION_UI_MODELESS = 2
PAGEACTION_UI_SILENT = 3
OLECMDID_WINDOWSTATE_FLAG = Int32
OLECMDIDF_WINDOWSTATE_USERVISIBLE = 1
OLECMDIDF_WINDOWSTATE_ENABLED = 2
OLECMDIDF_WINDOWSTATE_USERVISIBLE_VALID = 65536
OLECMDIDF_WINDOWSTATE_ENABLED_VALID = 131072
OLECMDID_VIEWPORT_MODE_FLAG = Int32
OLECMDIDF_VIEWPORTMODE_FIXED_LAYOUT_WIDTH = 1
OLECMDIDF_VIEWPORTMODE_EXCLUDE_VISUAL_BOTTOM = 2
OLECMDIDF_VIEWPORTMODE_FIXED_LAYOUT_WIDTH_VALID = 65536
OLECMDIDF_VIEWPORTMODE_EXCLUDE_VISUAL_BOTTOM_VALID = 131072
def _define_IZoomEvents_head():
    class IZoomEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('41b68150-904c-4e17-a0ba-a438182e359d')
    return IZoomEvents
def _define_IZoomEvents():
    IZoomEvents = win32more.System.Ole.IZoomEvents_head
    IZoomEvents.OnZoomPercentChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(3, 'OnZoomPercentChanged', ((1, 'ulZoomPercent'),)))
    win32more.System.Com.IUnknown
    return IZoomEvents
def _define_IProtectFocus_head():
    class IProtectFocus(win32more.System.Com.IUnknown_head):
        Guid = Guid('d81f90a3-8156-44f7-ad28-5abb87003274')
    return IProtectFocus
def _define_IProtectFocus():
    IProtectFocus = win32more.System.Ole.IProtectFocus_head
    IProtectFocus.AllowFocusChange = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL), use_last_error=False)(3, 'AllowFocusChange', ((1, 'pfAllow'),)))
    win32more.System.Com.IUnknown
    return IProtectFocus
def _define_IProtectedModeMenuServices_head():
    class IProtectedModeMenuServices(win32more.System.Com.IUnknown_head):
        Guid = Guid('73c105ee-9dff-4a07-b83c-7eff290c266e')
    return IProtectedModeMenuServices
def _define_IProtectedModeMenuServices():
    IProtectedModeMenuServices = win32more.System.Ole.IProtectedModeMenuServices_head
    IProtectedModeMenuServices.CreateMenu = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.UI.WindowsAndMessaging.HMENU), use_last_error=False)(3, 'CreateMenu', ((1, 'phMenu'),)))
    IProtectedModeMenuServices.LoadMenu = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.UI.WindowsAndMessaging.HMENU), use_last_error=False)(4, 'LoadMenu', ((1, 'pszModuleName'),(1, 'pszMenuName'),(1, 'phMenu'),)))
    IProtectedModeMenuServices.LoadMenuID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt16,POINTER(win32more.UI.WindowsAndMessaging.HMENU), use_last_error=False)(5, 'LoadMenuID', ((1, 'pszModuleName'),(1, 'wResourceID'),(1, 'phMenu'),)))
    win32more.System.Com.IUnknown
    return IProtectedModeMenuServices
def _define_LPFNOLEUIHOOK():
    return CFUNCTYPE(UInt32,win32more.Foundation.HWND,UInt32,win32more.Foundation.WPARAM,win32more.Foundation.LPARAM, use_last_error=False)
def _define_OLEUIINSERTOBJECTW_head():
    class OLEUIINSERTOBJECTW(Structure):
        pass
    return OLEUIINSERTOBJECTW
def _define_OLEUIINSERTOBJECTW():
    OLEUIINSERTOBJECTW = win32more.System.Ole.OLEUIINSERTOBJECTW_head
    OLEUIINSERTOBJECTW._fields_ = [
        ("cbStruct", UInt32),
        ("dwFlags", UInt32),
        ("hWndOwner", win32more.Foundation.HWND),
        ("lpszCaption", win32more.Foundation.PWSTR),
        ("lpfnHook", win32more.System.Ole.LPFNOLEUIHOOK),
        ("lCustData", win32more.Foundation.LPARAM),
        ("hInstance", win32more.Foundation.HINSTANCE),
        ("lpszTemplate", win32more.Foundation.PWSTR),
        ("hResource", win32more.Foundation.HRSRC),
        ("clsid", Guid),
        ("lpszFile", win32more.Foundation.PWSTR),
        ("cchFile", UInt32),
        ("cClsidExclude", UInt32),
        ("lpClsidExclude", POINTER(Guid)),
        ("iid", Guid),
        ("oleRender", UInt32),
        ("lpFormatEtc", POINTER(win32more.System.Com.FORMATETC_head)),
        ("lpIOleClientSite", win32more.System.Ole.IOleClientSite_head),
        ("lpIStorage", win32more.System.Com.StructuredStorage.IStorage_head),
        ("ppvObj", POINTER(c_void_p)),
        ("sc", Int32),
        ("hMetaPict", IntPtr),
    ]
    return OLEUIINSERTOBJECTW
def _define_OLEUIINSERTOBJECTA_head():
    class OLEUIINSERTOBJECTA(Structure):
        pass
    return OLEUIINSERTOBJECTA
def _define_OLEUIINSERTOBJECTA():
    OLEUIINSERTOBJECTA = win32more.System.Ole.OLEUIINSERTOBJECTA_head
    OLEUIINSERTOBJECTA._fields_ = [
        ("cbStruct", UInt32),
        ("dwFlags", UInt32),
        ("hWndOwner", win32more.Foundation.HWND),
        ("lpszCaption", win32more.Foundation.PSTR),
        ("lpfnHook", win32more.System.Ole.LPFNOLEUIHOOK),
        ("lCustData", win32more.Foundation.LPARAM),
        ("hInstance", win32more.Foundation.HINSTANCE),
        ("lpszTemplate", win32more.Foundation.PSTR),
        ("hResource", win32more.Foundation.HRSRC),
        ("clsid", Guid),
        ("lpszFile", win32more.Foundation.PSTR),
        ("cchFile", UInt32),
        ("cClsidExclude", UInt32),
        ("lpClsidExclude", POINTER(Guid)),
        ("iid", Guid),
        ("oleRender", UInt32),
        ("lpFormatEtc", POINTER(win32more.System.Com.FORMATETC_head)),
        ("lpIOleClientSite", win32more.System.Ole.IOleClientSite_head),
        ("lpIStorage", win32more.System.Com.StructuredStorage.IStorage_head),
        ("ppvObj", POINTER(c_void_p)),
        ("sc", Int32),
        ("hMetaPict", IntPtr),
    ]
    return OLEUIINSERTOBJECTA
OLEUIPASTEFLAG = Int32
OLEUIPASTE_ENABLEICON = 2048
OLEUIPASTE_PASTEONLY = 0
OLEUIPASTE_PASTE = 512
OLEUIPASTE_LINKANYTYPE = 1024
OLEUIPASTE_LINKTYPE1 = 1
OLEUIPASTE_LINKTYPE2 = 2
OLEUIPASTE_LINKTYPE3 = 4
OLEUIPASTE_LINKTYPE4 = 8
OLEUIPASTE_LINKTYPE5 = 16
OLEUIPASTE_LINKTYPE6 = 32
OLEUIPASTE_LINKTYPE7 = 64
OLEUIPASTE_LINKTYPE8 = 128
def _define_OLEUIPASTEENTRYW_head():
    class OLEUIPASTEENTRYW(Structure):
        pass
    return OLEUIPASTEENTRYW
def _define_OLEUIPASTEENTRYW():
    OLEUIPASTEENTRYW = win32more.System.Ole.OLEUIPASTEENTRYW_head
    OLEUIPASTEENTRYW._fields_ = [
        ("fmtetc", win32more.System.Com.FORMATETC),
        ("lpstrFormatName", win32more.Foundation.PWSTR),
        ("lpstrResultText", win32more.Foundation.PWSTR),
        ("dwFlags", UInt32),
        ("dwScratchSpace", UInt32),
    ]
    return OLEUIPASTEENTRYW
def _define_OLEUIPASTEENTRYA_head():
    class OLEUIPASTEENTRYA(Structure):
        pass
    return OLEUIPASTEENTRYA
def _define_OLEUIPASTEENTRYA():
    OLEUIPASTEENTRYA = win32more.System.Ole.OLEUIPASTEENTRYA_head
    OLEUIPASTEENTRYA._fields_ = [
        ("fmtetc", win32more.System.Com.FORMATETC),
        ("lpstrFormatName", win32more.Foundation.PSTR),
        ("lpstrResultText", win32more.Foundation.PSTR),
        ("dwFlags", UInt32),
        ("dwScratchSpace", UInt32),
    ]
    return OLEUIPASTEENTRYA
def _define_OLEUIPASTESPECIALW_head():
    class OLEUIPASTESPECIALW(Structure):
        pass
    return OLEUIPASTESPECIALW
def _define_OLEUIPASTESPECIALW():
    OLEUIPASTESPECIALW = win32more.System.Ole.OLEUIPASTESPECIALW_head
    OLEUIPASTESPECIALW._fields_ = [
        ("cbStruct", UInt32),
        ("dwFlags", UInt32),
        ("hWndOwner", win32more.Foundation.HWND),
        ("lpszCaption", win32more.Foundation.PWSTR),
        ("lpfnHook", win32more.System.Ole.LPFNOLEUIHOOK),
        ("lCustData", win32more.Foundation.LPARAM),
        ("hInstance", win32more.Foundation.HINSTANCE),
        ("lpszTemplate", win32more.Foundation.PWSTR),
        ("hResource", win32more.Foundation.HRSRC),
        ("lpSrcDataObj", win32more.System.Com.IDataObject_head),
        ("arrPasteEntries", POINTER(win32more.System.Ole.OLEUIPASTEENTRYW_head)),
        ("cPasteEntries", Int32),
        ("arrLinkTypes", POINTER(UInt32)),
        ("cLinkTypes", Int32),
        ("cClsidExclude", UInt32),
        ("lpClsidExclude", POINTER(Guid)),
        ("nSelectedIndex", Int32),
        ("fLink", win32more.Foundation.BOOL),
        ("hMetaPict", IntPtr),
        ("sizel", win32more.Foundation.SIZE),
    ]
    return OLEUIPASTESPECIALW
def _define_OLEUIPASTESPECIALA_head():
    class OLEUIPASTESPECIALA(Structure):
        pass
    return OLEUIPASTESPECIALA
def _define_OLEUIPASTESPECIALA():
    OLEUIPASTESPECIALA = win32more.System.Ole.OLEUIPASTESPECIALA_head
    OLEUIPASTESPECIALA._fields_ = [
        ("cbStruct", UInt32),
        ("dwFlags", UInt32),
        ("hWndOwner", win32more.Foundation.HWND),
        ("lpszCaption", win32more.Foundation.PSTR),
        ("lpfnHook", win32more.System.Ole.LPFNOLEUIHOOK),
        ("lCustData", win32more.Foundation.LPARAM),
        ("hInstance", win32more.Foundation.HINSTANCE),
        ("lpszTemplate", win32more.Foundation.PSTR),
        ("hResource", win32more.Foundation.HRSRC),
        ("lpSrcDataObj", win32more.System.Com.IDataObject_head),
        ("arrPasteEntries", POINTER(win32more.System.Ole.OLEUIPASTEENTRYA_head)),
        ("cPasteEntries", Int32),
        ("arrLinkTypes", POINTER(UInt32)),
        ("cLinkTypes", Int32),
        ("cClsidExclude", UInt32),
        ("lpClsidExclude", POINTER(Guid)),
        ("nSelectedIndex", Int32),
        ("fLink", win32more.Foundation.BOOL),
        ("hMetaPict", IntPtr),
        ("sizel", win32more.Foundation.SIZE),
    ]
    return OLEUIPASTESPECIALA
def _define_IOleUILinkContainerW_head():
    class IOleUILinkContainerW(win32more.System.Com.IUnknown_head):
        Guid = Guid(None)
    return IOleUILinkContainerW
def _define_IOleUILinkContainerW():
    IOleUILinkContainerW = win32more.System.Ole.IOleUILinkContainerW_head
    IOleUILinkContainerW.GetNextLink = COMMETHOD(WINFUNCTYPE(UInt32,UInt32, use_last_error=False)(3, 'GetNextLink', ((1, 'dwLink'),)))
    IOleUILinkContainerW.SetLinkUpdateOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(4, 'SetLinkUpdateOptions', ((1, 'dwLink'),(1, 'dwUpdateOpt'),)))
    IOleUILinkContainerW.GetLinkUpdateOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(5, 'GetLinkUpdateOptions', ((1, 'dwLink'),(1, 'lpdwUpdateOpt'),)))
    IOleUILinkContainerW.SetLinkSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),win32more.Foundation.BOOL, use_last_error=False)(6, 'SetLinkSource', ((1, 'dwLink'),(1, 'lpszDisplayName'),(1, 'lenFileName'),(1, 'pchEaten'),(1, 'fValidateSource'),)))
    IOleUILinkContainerW.GetLinkSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32),POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.BOOL),POINTER(win32more.Foundation.BOOL), use_last_error=False)(7, 'GetLinkSource', ((1, 'dwLink'),(1, 'lplpszDisplayName'),(1, 'lplenFileName'),(1, 'lplpszFullLinkType'),(1, 'lplpszShortLinkType'),(1, 'lpfSourceAvailable'),(1, 'lpfIsSelected'),)))
    IOleUILinkContainerW.OpenLinkSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(8, 'OpenLinkSource', ((1, 'dwLink'),)))
    IOleUILinkContainerW.UpdateLink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.BOOL,win32more.Foundation.BOOL, use_last_error=False)(9, 'UpdateLink', ((1, 'dwLink'),(1, 'fErrorMessage'),(1, 'fReserved'),)))
    IOleUILinkContainerW.CancelLink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(10, 'CancelLink', ((1, 'dwLink'),)))
    win32more.System.Com.IUnknown
    return IOleUILinkContainerW
def _define_IOleUILinkContainerA_head():
    class IOleUILinkContainerA(win32more.System.Com.IUnknown_head):
        Guid = Guid(None)
    return IOleUILinkContainerA
def _define_IOleUILinkContainerA():
    IOleUILinkContainerA = win32more.System.Ole.IOleUILinkContainerA_head
    IOleUILinkContainerA.GetNextLink = COMMETHOD(WINFUNCTYPE(UInt32,UInt32, use_last_error=False)(3, 'GetNextLink', ((1, 'dwLink'),)))
    IOleUILinkContainerA.SetLinkUpdateOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32, use_last_error=False)(4, 'SetLinkUpdateOptions', ((1, 'dwLink'),(1, 'dwUpdateOpt'),)))
    IOleUILinkContainerA.GetLinkUpdateOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32), use_last_error=False)(5, 'GetLinkUpdateOptions', ((1, 'dwLink'),(1, 'lpdwUpdateOpt'),)))
    IOleUILinkContainerA.SetLinkSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PSTR,UInt32,POINTER(UInt32),win32more.Foundation.BOOL, use_last_error=False)(6, 'SetLinkSource', ((1, 'dwLink'),(1, 'lpszDisplayName'),(1, 'lenFileName'),(1, 'pchEaten'),(1, 'fValidateSource'),)))
    IOleUILinkContainerA.GetLinkSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.PSTR),POINTER(UInt32),POINTER(win32more.Foundation.PSTR),POINTER(win32more.Foundation.PSTR),POINTER(win32more.Foundation.BOOL),POINTER(win32more.Foundation.BOOL), use_last_error=False)(7, 'GetLinkSource', ((1, 'dwLink'),(1, 'lplpszDisplayName'),(1, 'lplenFileName'),(1, 'lplpszFullLinkType'),(1, 'lplpszShortLinkType'),(1, 'lpfSourceAvailable'),(1, 'lpfIsSelected'),)))
    IOleUILinkContainerA.OpenLinkSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(8, 'OpenLinkSource', ((1, 'dwLink'),)))
    IOleUILinkContainerA.UpdateLink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.BOOL,win32more.Foundation.BOOL, use_last_error=False)(9, 'UpdateLink', ((1, 'dwLink'),(1, 'fErrorMessage'),(1, 'fReserved'),)))
    IOleUILinkContainerA.CancelLink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(10, 'CancelLink', ((1, 'dwLink'),)))
    win32more.System.Com.IUnknown
    return IOleUILinkContainerA
def _define_OLEUIEDITLINKSW_head():
    class OLEUIEDITLINKSW(Structure):
        pass
    return OLEUIEDITLINKSW
def _define_OLEUIEDITLINKSW():
    OLEUIEDITLINKSW = win32more.System.Ole.OLEUIEDITLINKSW_head
    OLEUIEDITLINKSW._fields_ = [
        ("cbStruct", UInt32),
        ("dwFlags", UInt32),
        ("hWndOwner", win32more.Foundation.HWND),
        ("lpszCaption", win32more.Foundation.PWSTR),
        ("lpfnHook", win32more.System.Ole.LPFNOLEUIHOOK),
        ("lCustData", win32more.Foundation.LPARAM),
        ("hInstance", win32more.Foundation.HINSTANCE),
        ("lpszTemplate", win32more.Foundation.PWSTR),
        ("hResource", win32more.Foundation.HRSRC),
        ("lpOleUILinkContainer", win32more.System.Ole.IOleUILinkContainerW_head),
    ]
    return OLEUIEDITLINKSW
def _define_OLEUIEDITLINKSA_head():
    class OLEUIEDITLINKSA(Structure):
        pass
    return OLEUIEDITLINKSA
def _define_OLEUIEDITLINKSA():
    OLEUIEDITLINKSA = win32more.System.Ole.OLEUIEDITLINKSA_head
    OLEUIEDITLINKSA._fields_ = [
        ("cbStruct", UInt32),
        ("dwFlags", UInt32),
        ("hWndOwner", win32more.Foundation.HWND),
        ("lpszCaption", win32more.Foundation.PSTR),
        ("lpfnHook", win32more.System.Ole.LPFNOLEUIHOOK),
        ("lCustData", win32more.Foundation.LPARAM),
        ("hInstance", win32more.Foundation.HINSTANCE),
        ("lpszTemplate", win32more.Foundation.PSTR),
        ("hResource", win32more.Foundation.HRSRC),
        ("lpOleUILinkContainer", win32more.System.Ole.IOleUILinkContainerA_head),
    ]
    return OLEUIEDITLINKSA
def _define_OLEUICHANGEICONW_head():
    class OLEUICHANGEICONW(Structure):
        pass
    return OLEUICHANGEICONW
def _define_OLEUICHANGEICONW():
    OLEUICHANGEICONW = win32more.System.Ole.OLEUICHANGEICONW_head
    OLEUICHANGEICONW._fields_ = [
        ("cbStruct", UInt32),
        ("dwFlags", UInt32),
        ("hWndOwner", win32more.Foundation.HWND),
        ("lpszCaption", win32more.Foundation.PWSTR),
        ("lpfnHook", win32more.System.Ole.LPFNOLEUIHOOK),
        ("lCustData", win32more.Foundation.LPARAM),
        ("hInstance", win32more.Foundation.HINSTANCE),
        ("lpszTemplate", win32more.Foundation.PWSTR),
        ("hResource", win32more.Foundation.HRSRC),
        ("hMetaPict", IntPtr),
        ("clsid", Guid),
        ("szIconExe", Char * 260),
        ("cchIconExe", Int32),
    ]
    return OLEUICHANGEICONW
def _define_OLEUICHANGEICONA_head():
    class OLEUICHANGEICONA(Structure):
        pass
    return OLEUICHANGEICONA
def _define_OLEUICHANGEICONA():
    OLEUICHANGEICONA = win32more.System.Ole.OLEUICHANGEICONA_head
    OLEUICHANGEICONA._fields_ = [
        ("cbStruct", UInt32),
        ("dwFlags", UInt32),
        ("hWndOwner", win32more.Foundation.HWND),
        ("lpszCaption", win32more.Foundation.PSTR),
        ("lpfnHook", win32more.System.Ole.LPFNOLEUIHOOK),
        ("lCustData", win32more.Foundation.LPARAM),
        ("hInstance", win32more.Foundation.HINSTANCE),
        ("lpszTemplate", win32more.Foundation.PSTR),
        ("hResource", win32more.Foundation.HRSRC),
        ("hMetaPict", IntPtr),
        ("clsid", Guid),
        ("szIconExe", win32more.Foundation.CHAR * 260),
        ("cchIconExe", Int32),
    ]
    return OLEUICHANGEICONA
def _define_OLEUICONVERTW_head():
    class OLEUICONVERTW(Structure):
        pass
    return OLEUICONVERTW
def _define_OLEUICONVERTW():
    OLEUICONVERTW = win32more.System.Ole.OLEUICONVERTW_head
    OLEUICONVERTW._fields_ = [
        ("cbStruct", UInt32),
        ("dwFlags", UInt32),
        ("hWndOwner", win32more.Foundation.HWND),
        ("lpszCaption", win32more.Foundation.PWSTR),
        ("lpfnHook", win32more.System.Ole.LPFNOLEUIHOOK),
        ("lCustData", win32more.Foundation.LPARAM),
        ("hInstance", win32more.Foundation.HINSTANCE),
        ("lpszTemplate", win32more.Foundation.PWSTR),
        ("hResource", win32more.Foundation.HRSRC),
        ("clsid", Guid),
        ("clsidConvertDefault", Guid),
        ("clsidActivateDefault", Guid),
        ("clsidNew", Guid),
        ("dvAspect", UInt32),
        ("wFormat", UInt16),
        ("fIsLinkedObject", win32more.Foundation.BOOL),
        ("hMetaPict", IntPtr),
        ("lpszUserType", win32more.Foundation.PWSTR),
        ("fObjectsIconChanged", win32more.Foundation.BOOL),
        ("lpszDefLabel", win32more.Foundation.PWSTR),
        ("cClsidExclude", UInt32),
        ("lpClsidExclude", POINTER(Guid)),
    ]
    return OLEUICONVERTW
def _define_OLEUICONVERTA_head():
    class OLEUICONVERTA(Structure):
        pass
    return OLEUICONVERTA
def _define_OLEUICONVERTA():
    OLEUICONVERTA = win32more.System.Ole.OLEUICONVERTA_head
    OLEUICONVERTA._fields_ = [
        ("cbStruct", UInt32),
        ("dwFlags", UInt32),
        ("hWndOwner", win32more.Foundation.HWND),
        ("lpszCaption", win32more.Foundation.PSTR),
        ("lpfnHook", win32more.System.Ole.LPFNOLEUIHOOK),
        ("lCustData", win32more.Foundation.LPARAM),
        ("hInstance", win32more.Foundation.HINSTANCE),
        ("lpszTemplate", win32more.Foundation.PSTR),
        ("hResource", win32more.Foundation.HRSRC),
        ("clsid", Guid),
        ("clsidConvertDefault", Guid),
        ("clsidActivateDefault", Guid),
        ("clsidNew", Guid),
        ("dvAspect", UInt32),
        ("wFormat", UInt16),
        ("fIsLinkedObject", win32more.Foundation.BOOL),
        ("hMetaPict", IntPtr),
        ("lpszUserType", win32more.Foundation.PSTR),
        ("fObjectsIconChanged", win32more.Foundation.BOOL),
        ("lpszDefLabel", win32more.Foundation.PSTR),
        ("cClsidExclude", UInt32),
        ("lpClsidExclude", POINTER(Guid)),
    ]
    return OLEUICONVERTA
def _define_OLEUIBUSYW_head():
    class OLEUIBUSYW(Structure):
        pass
    return OLEUIBUSYW
def _define_OLEUIBUSYW():
    OLEUIBUSYW = win32more.System.Ole.OLEUIBUSYW_head
    OLEUIBUSYW._fields_ = [
        ("cbStruct", UInt32),
        ("dwFlags", UInt32),
        ("hWndOwner", win32more.Foundation.HWND),
        ("lpszCaption", win32more.Foundation.PWSTR),
        ("lpfnHook", win32more.System.Ole.LPFNOLEUIHOOK),
        ("lCustData", win32more.Foundation.LPARAM),
        ("hInstance", win32more.Foundation.HINSTANCE),
        ("lpszTemplate", win32more.Foundation.PWSTR),
        ("hResource", win32more.Foundation.HRSRC),
        ("hTask", win32more.Media.HTASK),
        ("lphWndDialog", POINTER(win32more.Foundation.HWND)),
    ]
    return OLEUIBUSYW
def _define_OLEUIBUSYA_head():
    class OLEUIBUSYA(Structure):
        pass
    return OLEUIBUSYA
def _define_OLEUIBUSYA():
    OLEUIBUSYA = win32more.System.Ole.OLEUIBUSYA_head
    OLEUIBUSYA._fields_ = [
        ("cbStruct", UInt32),
        ("dwFlags", UInt32),
        ("hWndOwner", win32more.Foundation.HWND),
        ("lpszCaption", win32more.Foundation.PSTR),
        ("lpfnHook", win32more.System.Ole.LPFNOLEUIHOOK),
        ("lCustData", win32more.Foundation.LPARAM),
        ("hInstance", win32more.Foundation.HINSTANCE),
        ("lpszTemplate", win32more.Foundation.PSTR),
        ("hResource", win32more.Foundation.HRSRC),
        ("hTask", win32more.Media.HTASK),
        ("lphWndDialog", POINTER(win32more.Foundation.HWND)),
    ]
    return OLEUIBUSYA
def _define_OLEUICHANGESOURCEW_head():
    class OLEUICHANGESOURCEW(Structure):
        pass
    return OLEUICHANGESOURCEW
def _define_OLEUICHANGESOURCEW():
    OLEUICHANGESOURCEW = win32more.System.Ole.OLEUICHANGESOURCEW_head
    OLEUICHANGESOURCEW._fields_ = [
        ("cbStruct", UInt32),
        ("dwFlags", UInt32),
        ("hWndOwner", win32more.Foundation.HWND),
        ("lpszCaption", win32more.Foundation.PWSTR),
        ("lpfnHook", win32more.System.Ole.LPFNOLEUIHOOK),
        ("lCustData", win32more.Foundation.LPARAM),
        ("hInstance", win32more.Foundation.HINSTANCE),
        ("lpszTemplate", win32more.Foundation.PWSTR),
        ("hResource", win32more.Foundation.HRSRC),
        ("lpOFN", POINTER(win32more.UI.Controls.Dialogs.OPENFILENAMEW_head)),
        ("dwReserved1", UInt32 * 4),
        ("lpOleUILinkContainer", win32more.System.Ole.IOleUILinkContainerW_head),
        ("dwLink", UInt32),
        ("lpszDisplayName", win32more.Foundation.PWSTR),
        ("nFileLength", UInt32),
        ("lpszFrom", win32more.Foundation.PWSTR),
        ("lpszTo", win32more.Foundation.PWSTR),
    ]
    return OLEUICHANGESOURCEW
def _define_OLEUICHANGESOURCEA_head():
    class OLEUICHANGESOURCEA(Structure):
        pass
    return OLEUICHANGESOURCEA
def _define_OLEUICHANGESOURCEA():
    OLEUICHANGESOURCEA = win32more.System.Ole.OLEUICHANGESOURCEA_head
    OLEUICHANGESOURCEA._fields_ = [
        ("cbStruct", UInt32),
        ("dwFlags", UInt32),
        ("hWndOwner", win32more.Foundation.HWND),
        ("lpszCaption", win32more.Foundation.PSTR),
        ("lpfnHook", win32more.System.Ole.LPFNOLEUIHOOK),
        ("lCustData", win32more.Foundation.LPARAM),
        ("hInstance", win32more.Foundation.HINSTANCE),
        ("lpszTemplate", win32more.Foundation.PSTR),
        ("hResource", win32more.Foundation.HRSRC),
        ("lpOFN", POINTER(win32more.UI.Controls.Dialogs.OPENFILENAMEA_head)),
        ("dwReserved1", UInt32 * 4),
        ("lpOleUILinkContainer", win32more.System.Ole.IOleUILinkContainerA_head),
        ("dwLink", UInt32),
        ("lpszDisplayName", win32more.Foundation.PSTR),
        ("nFileLength", UInt32),
        ("lpszFrom", win32more.Foundation.PSTR),
        ("lpszTo", win32more.Foundation.PSTR),
    ]
    return OLEUICHANGESOURCEA
def _define_IOleUIObjInfoW_head():
    class IOleUIObjInfoW(win32more.System.Com.IUnknown_head):
        Guid = Guid(None)
    return IOleUIObjInfoW
def _define_IOleUIObjInfoW():
    IOleUIObjInfoW = win32more.System.Ole.IOleUIObjInfoW_head
    IOleUIObjInfoW.GetObjectInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'GetObjectInfo', ((1, 'dwObject'),(1, 'lpdwObjSize'),(1, 'lplpszLabel'),(1, 'lplpszType'),(1, 'lplpszShortType'),(1, 'lplpszLocation'),)))
    IOleUIObjInfoW.GetConvertInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(UInt16),POINTER(Guid),POINTER(POINTER(Guid)),POINTER(UInt32), use_last_error=False)(4, 'GetConvertInfo', ((1, 'dwObject'),(1, 'lpClassID'),(1, 'lpwFormat'),(1, 'lpConvertDefaultClassID'),(1, 'lplpClsidExclude'),(1, 'lpcClsidExclude'),)))
    IOleUIObjInfoW.ConvertObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid), use_last_error=False)(5, 'ConvertObject', ((1, 'dwObject'),(1, 'clsidNew'),)))
    IOleUIObjInfoW.GetViewInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(IntPtr),POINTER(UInt32),POINTER(Int32), use_last_error=False)(6, 'GetViewInfo', ((1, 'dwObject'),(1, 'phMetaPict'),(1, 'pdvAspect'),(1, 'pnCurrentScale'),)))
    IOleUIObjInfoW.SetViewInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,IntPtr,UInt32,Int32,win32more.Foundation.BOOL, use_last_error=False)(7, 'SetViewInfo', ((1, 'dwObject'),(1, 'hMetaPict'),(1, 'dvAspect'),(1, 'nCurrentScale'),(1, 'bRelativeToOrig'),)))
    win32more.System.Com.IUnknown
    return IOleUIObjInfoW
def _define_IOleUIObjInfoA_head():
    class IOleUIObjInfoA(win32more.System.Com.IUnknown_head):
        Guid = Guid(None)
    return IOleUIObjInfoA
def _define_IOleUIObjInfoA():
    IOleUIObjInfoA = win32more.System.Ole.IOleUIObjInfoA_head
    IOleUIObjInfoA.GetObjectInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32),POINTER(win32more.Foundation.PSTR),POINTER(win32more.Foundation.PSTR),POINTER(win32more.Foundation.PSTR),POINTER(win32more.Foundation.PSTR), use_last_error=False)(3, 'GetObjectInfo', ((1, 'dwObject'),(1, 'lpdwObjSize'),(1, 'lplpszLabel'),(1, 'lplpszType'),(1, 'lplpszShortType'),(1, 'lplpszLocation'),)))
    IOleUIObjInfoA.GetConvertInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(UInt16),POINTER(Guid),POINTER(POINTER(Guid)),POINTER(UInt32), use_last_error=False)(4, 'GetConvertInfo', ((1, 'dwObject'),(1, 'lpClassID'),(1, 'lpwFormat'),(1, 'lpConvertDefaultClassID'),(1, 'lplpClsidExclude'),(1, 'lpcClsidExclude'),)))
    IOleUIObjInfoA.ConvertObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid), use_last_error=False)(5, 'ConvertObject', ((1, 'dwObject'),(1, 'clsidNew'),)))
    IOleUIObjInfoA.GetViewInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(IntPtr),POINTER(UInt32),POINTER(Int32), use_last_error=False)(6, 'GetViewInfo', ((1, 'dwObject'),(1, 'phMetaPict'),(1, 'pdvAspect'),(1, 'pnCurrentScale'),)))
    IOleUIObjInfoA.SetViewInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,IntPtr,UInt32,Int32,win32more.Foundation.BOOL, use_last_error=False)(7, 'SetViewInfo', ((1, 'dwObject'),(1, 'hMetaPict'),(1, 'dvAspect'),(1, 'nCurrentScale'),(1, 'bRelativeToOrig'),)))
    win32more.System.Com.IUnknown
    return IOleUIObjInfoA
def _define_IOleUILinkInfoW_head():
    class IOleUILinkInfoW(win32more.System.Ole.IOleUILinkContainerW_head):
        Guid = Guid(None)
    return IOleUILinkInfoW
def _define_IOleUILinkInfoW():
    IOleUILinkInfoW = win32more.System.Ole.IOleUILinkInfoW_head
    IOleUILinkInfoW.GetLastUpdate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(11, 'GetLastUpdate', ((1, 'dwLink'),(1, 'lpLastUpdate'),)))
    win32more.System.Ole.IOleUILinkContainerW
    return IOleUILinkInfoW
def _define_IOleUILinkInfoA_head():
    class IOleUILinkInfoA(win32more.System.Ole.IOleUILinkContainerA_head):
        Guid = Guid(None)
    return IOleUILinkInfoA
def _define_IOleUILinkInfoA():
    IOleUILinkInfoA = win32more.System.Ole.IOleUILinkInfoA_head
    IOleUILinkInfoA.GetLastUpdate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.FILETIME_head), use_last_error=False)(11, 'GetLastUpdate', ((1, 'dwLink'),(1, 'lpLastUpdate'),)))
    win32more.System.Ole.IOleUILinkContainerA
    return IOleUILinkInfoA
def _define_OLEUIGNRLPROPSW_head():
    class OLEUIGNRLPROPSW(Structure):
        pass
    return OLEUIGNRLPROPSW
def _define_OLEUIGNRLPROPSW():
    OLEUIGNRLPROPSW = win32more.System.Ole.OLEUIGNRLPROPSW_head
    OLEUIGNRLPROPSW._fields_ = [
        ("cbStruct", UInt32),
        ("dwFlags", UInt32),
        ("dwReserved1", UInt32 * 2),
        ("lpfnHook", win32more.System.Ole.LPFNOLEUIHOOK),
        ("lCustData", win32more.Foundation.LPARAM),
        ("dwReserved2", UInt32 * 3),
        ("lpOP", POINTER(win32more.System.Ole.OLEUIOBJECTPROPSW_head)),
    ]
    return OLEUIGNRLPROPSW
def _define_OLEUIGNRLPROPSA_head():
    class OLEUIGNRLPROPSA(Structure):
        pass
    return OLEUIGNRLPROPSA
def _define_OLEUIGNRLPROPSA():
    OLEUIGNRLPROPSA = win32more.System.Ole.OLEUIGNRLPROPSA_head
    OLEUIGNRLPROPSA._fields_ = [
        ("cbStruct", UInt32),
        ("dwFlags", UInt32),
        ("dwReserved1", UInt32 * 2),
        ("lpfnHook", win32more.System.Ole.LPFNOLEUIHOOK),
        ("lCustData", win32more.Foundation.LPARAM),
        ("dwReserved2", UInt32 * 3),
        ("lpOP", POINTER(win32more.System.Ole.OLEUIOBJECTPROPSA_head)),
    ]
    return OLEUIGNRLPROPSA
def _define_OLEUIVIEWPROPSW_head():
    class OLEUIVIEWPROPSW(Structure):
        pass
    return OLEUIVIEWPROPSW
def _define_OLEUIVIEWPROPSW():
    OLEUIVIEWPROPSW = win32more.System.Ole.OLEUIVIEWPROPSW_head
    OLEUIVIEWPROPSW._fields_ = [
        ("cbStruct", UInt32),
        ("dwFlags", UInt32),
        ("dwReserved1", UInt32 * 2),
        ("lpfnHook", win32more.System.Ole.LPFNOLEUIHOOK),
        ("lCustData", win32more.Foundation.LPARAM),
        ("dwReserved2", UInt32 * 3),
        ("lpOP", POINTER(win32more.System.Ole.OLEUIOBJECTPROPSW_head)),
        ("nScaleMin", Int32),
        ("nScaleMax", Int32),
    ]
    return OLEUIVIEWPROPSW
def _define_OLEUIVIEWPROPSA_head():
    class OLEUIVIEWPROPSA(Structure):
        pass
    return OLEUIVIEWPROPSA
def _define_OLEUIVIEWPROPSA():
    OLEUIVIEWPROPSA = win32more.System.Ole.OLEUIVIEWPROPSA_head
    OLEUIVIEWPROPSA._fields_ = [
        ("cbStruct", UInt32),
        ("dwFlags", UInt32),
        ("dwReserved1", UInt32 * 2),
        ("lpfnHook", win32more.System.Ole.LPFNOLEUIHOOK),
        ("lCustData", win32more.Foundation.LPARAM),
        ("dwReserved2", UInt32 * 3),
        ("lpOP", POINTER(win32more.System.Ole.OLEUIOBJECTPROPSA_head)),
        ("nScaleMin", Int32),
        ("nScaleMax", Int32),
    ]
    return OLEUIVIEWPROPSA
def _define_OLEUILINKPROPSW_head():
    class OLEUILINKPROPSW(Structure):
        pass
    return OLEUILINKPROPSW
def _define_OLEUILINKPROPSW():
    OLEUILINKPROPSW = win32more.System.Ole.OLEUILINKPROPSW_head
    OLEUILINKPROPSW._fields_ = [
        ("cbStruct", UInt32),
        ("dwFlags", UInt32),
        ("dwReserved1", UInt32 * 2),
        ("lpfnHook", win32more.System.Ole.LPFNOLEUIHOOK),
        ("lCustData", win32more.Foundation.LPARAM),
        ("dwReserved2", UInt32 * 3),
        ("lpOP", POINTER(win32more.System.Ole.OLEUIOBJECTPROPSW_head)),
    ]
    return OLEUILINKPROPSW
def _define_OLEUILINKPROPSA_head():
    class OLEUILINKPROPSA(Structure):
        pass
    return OLEUILINKPROPSA
def _define_OLEUILINKPROPSA():
    OLEUILINKPROPSA = win32more.System.Ole.OLEUILINKPROPSA_head
    OLEUILINKPROPSA._fields_ = [
        ("cbStruct", UInt32),
        ("dwFlags", UInt32),
        ("dwReserved1", UInt32 * 2),
        ("lpfnHook", win32more.System.Ole.LPFNOLEUIHOOK),
        ("lCustData", win32more.Foundation.LPARAM),
        ("dwReserved2", UInt32 * 3),
        ("lpOP", POINTER(win32more.System.Ole.OLEUIOBJECTPROPSA_head)),
    ]
    return OLEUILINKPROPSA
def _define_OLEUIOBJECTPROPSW_head():
    class OLEUIOBJECTPROPSW(Structure):
        pass
    return OLEUIOBJECTPROPSW
def _define_OLEUIOBJECTPROPSW():
    OLEUIOBJECTPROPSW = win32more.System.Ole.OLEUIOBJECTPROPSW_head
    OLEUIOBJECTPROPSW._fields_ = [
        ("cbStruct", UInt32),
        ("dwFlags", UInt32),
        ("lpPS", POINTER(win32more.UI.Controls.PROPSHEETHEADERW_V2_head)),
        ("dwObject", UInt32),
        ("lpObjInfo", win32more.System.Ole.IOleUIObjInfoW_head),
        ("dwLink", UInt32),
        ("lpLinkInfo", win32more.System.Ole.IOleUILinkInfoW_head),
        ("lpGP", POINTER(win32more.System.Ole.OLEUIGNRLPROPSW_head)),
        ("lpVP", POINTER(win32more.System.Ole.OLEUIVIEWPROPSW_head)),
        ("lpLP", POINTER(win32more.System.Ole.OLEUILINKPROPSW_head)),
    ]
    return OLEUIOBJECTPROPSW
def _define_OLEUIOBJECTPROPSA_head():
    class OLEUIOBJECTPROPSA(Structure):
        pass
    return OLEUIOBJECTPROPSA
def _define_OLEUIOBJECTPROPSA():
    OLEUIOBJECTPROPSA = win32more.System.Ole.OLEUIOBJECTPROPSA_head
    OLEUIOBJECTPROPSA._fields_ = [
        ("cbStruct", UInt32),
        ("dwFlags", UInt32),
        ("lpPS", POINTER(win32more.UI.Controls.PROPSHEETHEADERA_V2_head)),
        ("dwObject", UInt32),
        ("lpObjInfo", win32more.System.Ole.IOleUIObjInfoA_head),
        ("dwLink", UInt32),
        ("lpLinkInfo", win32more.System.Ole.IOleUILinkInfoA_head),
        ("lpGP", POINTER(win32more.System.Ole.OLEUIGNRLPROPSA_head)),
        ("lpVP", POINTER(win32more.System.Ole.OLEUIVIEWPROPSA_head)),
        ("lpLP", POINTER(win32more.System.Ole.OLEUILINKPROPSA_head)),
    ]
    return OLEUIOBJECTPROPSA
def _define_IDispatchEx_head():
    class IDispatchEx(win32more.System.Com.IDispatch_head):
        Guid = Guid('a6ef9860-c720-11d0-9337-00a0c90dcaa9')
    return IDispatchEx
def _define_IDispatchEx():
    IDispatchEx = win32more.System.Ole.IDispatchEx_head
    IDispatchEx.GetDispID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,UInt32,POINTER(Int32), use_last_error=False)(7, 'GetDispID', ((1, 'bstrName'),(1, 'grfdex'),(1, 'pid'),)))
    IDispatchEx.InvokeEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,UInt32,UInt16,POINTER(win32more.System.Com.DISPPARAMS_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.EXCEPINFO_head),win32more.System.Com.IServiceProvider_head, use_last_error=False)(8, 'InvokeEx', ((1, 'id'),(1, 'lcid'),(1, 'wFlags'),(1, 'pdp'),(1, 'pvarRes'),(1, 'pei'),(1, 'pspCaller'),)))
    IDispatchEx.DeleteMemberByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,UInt32, use_last_error=False)(9, 'DeleteMemberByName', ((1, 'bstrName'),(1, 'grfdex'),)))
    IDispatchEx.DeleteMemberByDispID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(10, 'DeleteMemberByDispID', ((1, 'id'),)))
    IDispatchEx.GetMemberProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,UInt32,POINTER(UInt32), use_last_error=False)(11, 'GetMemberProperties', ((1, 'id'),(1, 'grfdexFetch'),(1, 'pgrfdex'),)))
    IDispatchEx.GetMemberName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(12, 'GetMemberName', ((1, 'id'),(1, 'pbstrName'),)))
    IDispatchEx.GetNextDispID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Int32,POINTER(Int32), use_last_error=False)(13, 'GetNextDispID', ((1, 'grfdex'),(1, 'id'),(1, 'pid'),)))
    IDispatchEx.GetNameSpaceParent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(14, 'GetNameSpaceParent', ((1, 'ppunk'),)))
    win32more.System.Com.IDispatch
    return IDispatchEx
def _define_IDispError_head():
    class IDispError(win32more.System.Com.IUnknown_head):
        Guid = Guid('a6ef9861-c720-11d0-9337-00a0c90dcaa9')
    return IDispError
def _define_IDispError():
    IDispError = win32more.System.Ole.IDispError_head
    IDispError.QueryErrorInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,POINTER(win32more.System.Ole.IDispError_head), use_last_error=False)(3, 'QueryErrorInfo', ((1, 'guidErrorType'),(1, 'ppde'),)))
    IDispError.GetNext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IDispError_head), use_last_error=False)(4, 'GetNext', ((1, 'ppde'),)))
    IDispError.GetHresult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HRESULT), use_last_error=False)(5, 'GetHresult', ((1, 'phr'),)))
    IDispError.GetSource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(6, 'GetSource', ((1, 'pbstrSource'),)))
    IDispError.GetHelpInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR),POINTER(UInt32), use_last_error=False)(7, 'GetHelpInfo', ((1, 'pbstrFileName'),(1, 'pdwContext'),)))
    IDispError.GetDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BSTR), use_last_error=False)(8, 'GetDescription', ((1, 'pbstrDescription'),)))
    win32more.System.Com.IUnknown
    return IDispError
def _define_IVariantChangeType_head():
    class IVariantChangeType(win32more.System.Com.IUnknown_head):
        Guid = Guid('a6ef9862-c720-11d0-9337-00a0c90dcaa9')
    return IVariantChangeType
def _define_IVariantChangeType():
    IVariantChangeType = win32more.System.Ole.IVariantChangeType_head
    IVariantChangeType.ChangeType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),UInt32,UInt16, use_last_error=False)(3, 'ChangeType', ((1, 'pvarDst'),(1, 'pvarSrc'),(1, 'lcid'),(1, 'vtNew'),)))
    win32more.System.Com.IUnknown
    return IVariantChangeType
def _define_IObjectIdentity_head():
    class IObjectIdentity(win32more.System.Com.IUnknown_head):
        Guid = Guid('ca04b7e6-0d21-11d1-8cc5-00c04fc2b085')
    return IObjectIdentity
def _define_IObjectIdentity():
    IObjectIdentity = win32more.System.Ole.IObjectIdentity_head
    IObjectIdentity.IsEqualObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(3, 'IsEqualObject', ((1, 'punk'),)))
    win32more.System.Com.IUnknown
    return IObjectIdentity
def _define_ICanHandleException_head():
    class ICanHandleException(win32more.System.Com.IUnknown_head):
        Guid = Guid('c5598e60-b307-11d1-b27d-006008c3fbfb')
    return ICanHandleException
def _define_ICanHandleException():
    ICanHandleException = win32more.System.Ole.ICanHandleException_head
    ICanHandleException.CanHandleException = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.EXCEPINFO_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(3, 'CanHandleException', ((1, 'pExcepInfo'),(1, 'pvar'),)))
    win32more.System.Com.IUnknown
    return ICanHandleException
def _define_IProvideRuntimeContext_head():
    class IProvideRuntimeContext(win32more.System.Com.IUnknown_head):
        Guid = Guid('10e2414a-ec59-49d2-bc51-5add2c36febc')
    return IProvideRuntimeContext
def _define_IProvideRuntimeContext():
    IProvideRuntimeContext = win32more.System.Ole.IProvideRuntimeContext_head
    IProvideRuntimeContext.GetCurrentSourceContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UIntPtr),POINTER(Int16), use_last_error=False)(3, 'GetCurrentSourceContext', ((1, 'pdwContext'),(1, 'pfExecutingGlobalCode'),)))
    win32more.System.Com.IUnknown
    return IProvideRuntimeContext
def _define_DosDateTimeToVariantTime():
    try:
        return WINFUNCTYPE(Int32,UInt16,UInt16,POINTER(Double), use_last_error=False)(("DosDateTimeToVariantTime", windll["OLEAUT32"]), ((1, 'wDosDate'),(1, 'wDosTime'),(1, 'pvtime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantTimeToDosDateTime():
    try:
        return WINFUNCTYPE(Int32,Double,POINTER(UInt16),POINTER(UInt16), use_last_error=False)(("VariantTimeToDosDateTime", windll["OLEAUT32"]), ((1, 'vtime'),(1, 'pwDosDate'),(1, 'pwDosTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SystemTimeToVariantTime():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Foundation.SYSTEMTIME_head),POINTER(Double), use_last_error=False)(("SystemTimeToVariantTime", windll["OLEAUT32"]), ((1, 'lpSystemTime'),(1, 'pvtime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantTimeToSystemTime():
    try:
        return WINFUNCTYPE(Int32,Double,POINTER(win32more.Foundation.SYSTEMTIME_head), use_last_error=False)(("VariantTimeToSystemTime", windll["OLEAUT32"]), ((1, 'vtime'),(1, 'lpSystemTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArrayAllocDescriptor():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(("SafeArrayAllocDescriptor", windll["OLEAUT32"]), ((1, 'cDims'),(1, 'ppsaOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArrayAllocDescriptorEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,UInt32,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(("SafeArrayAllocDescriptorEx", windll["OLEAUT32"]), ((1, 'vt'),(1, 'cDims'),(1, 'ppsaOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArrayAllocData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(("SafeArrayAllocData", windll["OLEAUT32"]), ((1, 'psa'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArrayCreate():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.Com.SAFEARRAY_head),UInt16,UInt32,POINTER(win32more.System.Com.SAFEARRAYBOUND_head), use_last_error=False)(("SafeArrayCreate", windll["OLEAUT32"]), ((1, 'vt'),(1, 'cDims'),(1, 'rgsabound'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArrayCreateEx():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.Com.SAFEARRAY_head),UInt16,UInt32,POINTER(win32more.System.Com.SAFEARRAYBOUND_head),c_void_p, use_last_error=False)(("SafeArrayCreateEx", windll["OLEAUT32"]), ((1, 'vt'),(1, 'cDims'),(1, 'rgsabound'),(1, 'pvExtra'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArrayCopyData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(("SafeArrayCopyData", windll["OLEAUT32"]), ((1, 'psaSource'),(1, 'psaTarget'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArrayReleaseDescriptor():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(("SafeArrayReleaseDescriptor", windll["OLEAUT32"]), ((1, 'psa'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArrayDestroyDescriptor():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(("SafeArrayDestroyDescriptor", windll["OLEAUT32"]), ((1, 'psa'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArrayReleaseData():
    try:
        return WINFUNCTYPE(Void,c_void_p, use_last_error=False)(("SafeArrayReleaseData", windll["OLEAUT32"]), ((1, 'pData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArrayDestroyData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(("SafeArrayDestroyData", windll["OLEAUT32"]), ((1, 'psa'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArrayAddRef():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(c_void_p), use_last_error=False)(("SafeArrayAddRef", windll["OLEAUT32"]), ((1, 'psa'),(1, 'ppDataToRelease'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArrayDestroy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(("SafeArrayDestroy", windll["OLEAUT32"]), ((1, 'psa'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArrayRedim():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(win32more.System.Com.SAFEARRAYBOUND_head), use_last_error=False)(("SafeArrayRedim", windll["OLEAUT32"]), ((1, 'psa'),(1, 'psaboundNew'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArrayGetDim():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(("SafeArrayGetDim", windll["OLEAUT32"]), ((1, 'psa'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArrayGetElemsize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(("SafeArrayGetElemsize", windll["OLEAUT32"]), ((1, 'psa'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArrayGetUBound():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),UInt32,POINTER(Int32), use_last_error=False)(("SafeArrayGetUBound", windll["OLEAUT32"]), ((1, 'psa'),(1, 'nDim'),(1, 'plUbound'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArrayGetLBound():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),UInt32,POINTER(Int32), use_last_error=False)(("SafeArrayGetLBound", windll["OLEAUT32"]), ((1, 'psa'),(1, 'nDim'),(1, 'plLbound'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArrayLock():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(("SafeArrayLock", windll["OLEAUT32"]), ((1, 'psa'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArrayUnlock():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(("SafeArrayUnlock", windll["OLEAUT32"]), ((1, 'psa'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArrayAccessData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(c_void_p), use_last_error=False)(("SafeArrayAccessData", windll["OLEAUT32"]), ((1, 'psa'),(1, 'ppvData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArrayUnaccessData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head), use_last_error=False)(("SafeArrayUnaccessData", windll["OLEAUT32"]), ((1, 'psa'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArrayGetElement():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(Int32),c_void_p, use_last_error=False)(("SafeArrayGetElement", windll["OLEAUT32"]), ((1, 'psa'),(1, 'rgIndices'),(1, 'pv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArrayPutElement():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(Int32),c_void_p, use_last_error=False)(("SafeArrayPutElement", windll["OLEAUT32"]), ((1, 'psa'),(1, 'rgIndices'),(1, 'pv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArrayCopy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(("SafeArrayCopy", windll["OLEAUT32"]), ((1, 'psa'),(1, 'ppsaOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArrayPtrOfIndex():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(Int32),POINTER(c_void_p), use_last_error=False)(("SafeArrayPtrOfIndex", windll["OLEAUT32"]), ((1, 'psa'),(1, 'rgIndices'),(1, 'ppvData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArraySetRecordInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),win32more.System.Ole.IRecordInfo_head, use_last_error=False)(("SafeArraySetRecordInfo", windll["OLEAUT32"]), ((1, 'psa'),(1, 'prinfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArrayGetRecordInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(win32more.System.Ole.IRecordInfo_head), use_last_error=False)(("SafeArrayGetRecordInfo", windll["OLEAUT32"]), ((1, 'psa'),(1, 'prinfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArraySetIID():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(Guid), use_last_error=False)(("SafeArraySetIID", windll["OLEAUT32"]), ((1, 'psa'),(1, 'guid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArrayGetIID():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(Guid), use_last_error=False)(("SafeArrayGetIID", windll["OLEAUT32"]), ((1, 'psa'),(1, 'pguid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArrayGetVartype():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(UInt16), use_last_error=False)(("SafeArrayGetVartype", windll["OLEAUT32"]), ((1, 'psa'),(1, 'pvt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArrayCreateVector():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.Com.SAFEARRAY_head),UInt16,Int32,UInt32, use_last_error=False)(("SafeArrayCreateVector", windll["OLEAUT32"]), ((1, 'vt'),(1, 'lLbound'),(1, 'cElements'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SafeArrayCreateVectorEx():
    try:
        return WINFUNCTYPE(POINTER(win32more.System.Com.SAFEARRAY_head),UInt16,Int32,UInt32,c_void_p, use_last_error=False)(("SafeArrayCreateVectorEx", windll["OLEAUT32"]), ((1, 'vt'),(1, 'lLbound'),(1, 'cElements'),(1, 'pvExtra'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantInit():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VariantInit", windll["OLEAUT32"]), ((1, 'pvarg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantClear():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VariantClear", windll["OLEAUT32"]), ((1, 'pvarg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantCopy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VariantCopy", windll["OLEAUT32"]), ((1, 'pvargDest'),(1, 'pvargSrc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantCopyInd():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VariantCopyInd", windll["OLEAUT32"]), ((1, 'pvarDest'),(1, 'pvargSrc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantChangeType():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),UInt16,UInt16, use_last_error=False)(("VariantChangeType", windll["OLEAUT32"]), ((1, 'pvargDest'),(1, 'pvarSrc'),(1, 'wFlags'),(1, 'vt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VariantChangeTypeEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),UInt32,UInt16,UInt16, use_last_error=False)(("VariantChangeTypeEx", windll["OLEAUT32"]), ((1, 'pvargDest'),(1, 'pvarSrc'),(1, 'lcid'),(1, 'wFlags'),(1, 'vt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VectorFromBstr():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,POINTER(POINTER(win32more.System.Com.SAFEARRAY_head)), use_last_error=False)(("VectorFromBstr", windll["OLEAUT32"]), ((1, 'bstr'),(1, 'ppsa'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BstrFromVector():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.SAFEARRAY_head),POINTER(win32more.Foundation.BSTR), use_last_error=False)(("BstrFromVector", windll["OLEAUT32"]), ((1, 'psa'),(1, 'pbstr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI1FromI2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,c_char_p_no, use_last_error=False)(("VarUI1FromI2", windll["OLEAUT32"]), ((1, 'sIn'),(1, 'pbOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI1FromI4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,c_char_p_no, use_last_error=False)(("VarUI1FromI4", windll["OLEAUT32"]), ((1, 'lIn'),(1, 'pbOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI1FromI8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int64,c_char_p_no, use_last_error=False)(("VarUI1FromI8", windll["OLEAUT32"]), ((1, 'i64In'),(1, 'pbOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI1FromR4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Single,c_char_p_no, use_last_error=False)(("VarUI1FromR4", windll["OLEAUT32"]), ((1, 'fltIn'),(1, 'pbOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI1FromR8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,c_char_p_no, use_last_error=False)(("VarUI1FromR8", windll["OLEAUT32"]), ((1, 'dblIn'),(1, 'pbOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI1FromCy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CY,c_char_p_no, use_last_error=False)(("VarUI1FromCy", windll["OLEAUT32"]), ((1, 'cyIn'),(1, 'pbOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI1FromDate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,c_char_p_no, use_last_error=False)(("VarUI1FromDate", windll["OLEAUT32"]), ((1, 'dateIn'),(1, 'pbOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI1FromStr():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,c_char_p_no, use_last_error=False)(("VarUI1FromStr", windll["OLEAUT32"]), ((1, 'strIn'),(1, 'lcid'),(1, 'dwFlags'),(1, 'pbOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI1FromDisp():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,UInt32,c_char_p_no, use_last_error=False)(("VarUI1FromDisp", windll["OLEAUT32"]), ((1, 'pdispIn'),(1, 'lcid'),(1, 'pbOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI1FromBool():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,c_char_p_no, use_last_error=False)(("VarUI1FromBool", windll["OLEAUT32"]), ((1, 'boolIn'),(1, 'pbOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI1FromI1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.CHAR,c_char_p_no, use_last_error=False)(("VarUI1FromI1", windll["OLEAUT32"]), ((1, 'cIn'),(1, 'pbOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI1FromUI2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,c_char_p_no, use_last_error=False)(("VarUI1FromUI2", windll["OLEAUT32"]), ((1, 'uiIn'),(1, 'pbOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI1FromUI4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_char_p_no, use_last_error=False)(("VarUI1FromUI4", windll["OLEAUT32"]), ((1, 'ulIn'),(1, 'pbOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI1FromUI8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,c_char_p_no, use_last_error=False)(("VarUI1FromUI8", windll["OLEAUT32"]), ((1, 'ui64In'),(1, 'pbOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI1FromDec():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.DECIMAL_head),c_char_p_no, use_last_error=False)(("VarUI1FromDec", windll["OLEAUT32"]), ((1, 'pdecIn'),(1, 'pbOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI2FromUI1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Byte,POINTER(Int16), use_last_error=False)(("VarI2FromUI1", windll["OLEAUT32"]), ((1, 'bIn'),(1, 'psOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI2FromI4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int16), use_last_error=False)(("VarI2FromI4", windll["OLEAUT32"]), ((1, 'lIn'),(1, 'psOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI2FromI8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int64,POINTER(Int16), use_last_error=False)(("VarI2FromI8", windll["OLEAUT32"]), ((1, 'i64In'),(1, 'psOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI2FromR4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Single,POINTER(Int16), use_last_error=False)(("VarI2FromR4", windll["OLEAUT32"]), ((1, 'fltIn'),(1, 'psOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI2FromR8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(Int16), use_last_error=False)(("VarI2FromR8", windll["OLEAUT32"]), ((1, 'dblIn'),(1, 'psOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI2FromCy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CY,POINTER(Int16), use_last_error=False)(("VarI2FromCy", windll["OLEAUT32"]), ((1, 'cyIn'),(1, 'psOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI2FromDate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(Int16), use_last_error=False)(("VarI2FromDate", windll["OLEAUT32"]), ((1, 'dateIn'),(1, 'psOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI2FromStr():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(Int16), use_last_error=False)(("VarI2FromStr", windll["OLEAUT32"]), ((1, 'strIn'),(1, 'lcid'),(1, 'dwFlags'),(1, 'psOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI2FromDisp():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,UInt32,POINTER(Int16), use_last_error=False)(("VarI2FromDisp", windll["OLEAUT32"]), ((1, 'pdispIn'),(1, 'lcid'),(1, 'psOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI2FromBool():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,POINTER(Int16), use_last_error=False)(("VarI2FromBool", windll["OLEAUT32"]), ((1, 'boolIn'),(1, 'psOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI2FromI1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.CHAR,POINTER(Int16), use_last_error=False)(("VarI2FromI1", windll["OLEAUT32"]), ((1, 'cIn'),(1, 'psOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI2FromUI2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(Int16), use_last_error=False)(("VarI2FromUI2", windll["OLEAUT32"]), ((1, 'uiIn'),(1, 'psOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI2FromUI4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Int16), use_last_error=False)(("VarI2FromUI4", windll["OLEAUT32"]), ((1, 'ulIn'),(1, 'psOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI2FromUI8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(Int16), use_last_error=False)(("VarI2FromUI8", windll["OLEAUT32"]), ((1, 'ui64In'),(1, 'psOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI2FromDec():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.DECIMAL_head),POINTER(Int16), use_last_error=False)(("VarI2FromDec", windll["OLEAUT32"]), ((1, 'pdecIn'),(1, 'psOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI4FromUI1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Byte,POINTER(Int32), use_last_error=False)(("VarI4FromUI1", windll["OLEAUT32"]), ((1, 'bIn'),(1, 'plOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI4FromI2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,POINTER(Int32), use_last_error=False)(("VarI4FromI2", windll["OLEAUT32"]), ((1, 'sIn'),(1, 'plOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI4FromI8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int64,POINTER(Int32), use_last_error=False)(("VarI4FromI8", windll["OLEAUT32"]), ((1, 'i64In'),(1, 'plOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI4FromR4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Single,POINTER(Int32), use_last_error=False)(("VarI4FromR4", windll["OLEAUT32"]), ((1, 'fltIn'),(1, 'plOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI4FromR8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(Int32), use_last_error=False)(("VarI4FromR8", windll["OLEAUT32"]), ((1, 'dblIn'),(1, 'plOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI4FromCy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CY,POINTER(Int32), use_last_error=False)(("VarI4FromCy", windll["OLEAUT32"]), ((1, 'cyIn'),(1, 'plOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI4FromDate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(Int32), use_last_error=False)(("VarI4FromDate", windll["OLEAUT32"]), ((1, 'dateIn'),(1, 'plOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI4FromStr():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(Int32), use_last_error=False)(("VarI4FromStr", windll["OLEAUT32"]), ((1, 'strIn'),(1, 'lcid'),(1, 'dwFlags'),(1, 'plOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI4FromDisp():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,UInt32,POINTER(Int32), use_last_error=False)(("VarI4FromDisp", windll["OLEAUT32"]), ((1, 'pdispIn'),(1, 'lcid'),(1, 'plOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI4FromBool():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,POINTER(Int32), use_last_error=False)(("VarI4FromBool", windll["OLEAUT32"]), ((1, 'boolIn'),(1, 'plOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI4FromI1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.CHAR,POINTER(Int32), use_last_error=False)(("VarI4FromI1", windll["OLEAUT32"]), ((1, 'cIn'),(1, 'plOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI4FromUI2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(Int32), use_last_error=False)(("VarI4FromUI2", windll["OLEAUT32"]), ((1, 'uiIn'),(1, 'plOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI4FromUI4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Int32), use_last_error=False)(("VarI4FromUI4", windll["OLEAUT32"]), ((1, 'ulIn'),(1, 'plOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI4FromUI8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(Int32), use_last_error=False)(("VarI4FromUI8", windll["OLEAUT32"]), ((1, 'ui64In'),(1, 'plOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI4FromDec():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.DECIMAL_head),POINTER(Int32), use_last_error=False)(("VarI4FromDec", windll["OLEAUT32"]), ((1, 'pdecIn'),(1, 'plOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI8FromUI1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Byte,POINTER(Int64), use_last_error=False)(("VarI8FromUI1", windll["OLEAUT32"]), ((1, 'bIn'),(1, 'pi64Out'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI8FromI2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,POINTER(Int64), use_last_error=False)(("VarI8FromI2", windll["OLEAUT32"]), ((1, 'sIn'),(1, 'pi64Out'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI8FromR4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Single,POINTER(Int64), use_last_error=False)(("VarI8FromR4", windll["OLEAUT32"]), ((1, 'fltIn'),(1, 'pi64Out'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI8FromR8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(Int64), use_last_error=False)(("VarI8FromR8", windll["OLEAUT32"]), ((1, 'dblIn'),(1, 'pi64Out'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI8FromCy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CY,POINTER(Int64), use_last_error=False)(("VarI8FromCy", windll["OLEAUT32"]), ((1, 'cyIn'),(1, 'pi64Out'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI8FromDate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(Int64), use_last_error=False)(("VarI8FromDate", windll["OLEAUT32"]), ((1, 'dateIn'),(1, 'pi64Out'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI8FromStr():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(Int64), use_last_error=False)(("VarI8FromStr", windll["OLEAUT32"]), ((1, 'strIn'),(1, 'lcid'),(1, 'dwFlags'),(1, 'pi64Out'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI8FromDisp():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,UInt32,POINTER(Int64), use_last_error=False)(("VarI8FromDisp", windll["OLEAUT32"]), ((1, 'pdispIn'),(1, 'lcid'),(1, 'pi64Out'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI8FromBool():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,POINTER(Int64), use_last_error=False)(("VarI8FromBool", windll["OLEAUT32"]), ((1, 'boolIn'),(1, 'pi64Out'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI8FromI1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.CHAR,POINTER(Int64), use_last_error=False)(("VarI8FromI1", windll["OLEAUT32"]), ((1, 'cIn'),(1, 'pi64Out'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI8FromUI2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(Int64), use_last_error=False)(("VarI8FromUI2", windll["OLEAUT32"]), ((1, 'uiIn'),(1, 'pi64Out'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI8FromUI4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Int64), use_last_error=False)(("VarI8FromUI4", windll["OLEAUT32"]), ((1, 'ulIn'),(1, 'pi64Out'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI8FromUI8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(Int64), use_last_error=False)(("VarI8FromUI8", windll["OLEAUT32"]), ((1, 'ui64In'),(1, 'pi64Out'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI8FromDec():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.DECIMAL_head),POINTER(Int64), use_last_error=False)(("VarI8FromDec", windll["OLEAUT32"]), ((1, 'pdecIn'),(1, 'pi64Out'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR4FromUI1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Byte,POINTER(Single), use_last_error=False)(("VarR4FromUI1", windll["OLEAUT32"]), ((1, 'bIn'),(1, 'pfltOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR4FromI2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,POINTER(Single), use_last_error=False)(("VarR4FromI2", windll["OLEAUT32"]), ((1, 'sIn'),(1, 'pfltOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR4FromI4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Single), use_last_error=False)(("VarR4FromI4", windll["OLEAUT32"]), ((1, 'lIn'),(1, 'pfltOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR4FromI8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int64,POINTER(Single), use_last_error=False)(("VarR4FromI8", windll["OLEAUT32"]), ((1, 'i64In'),(1, 'pfltOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR4FromR8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(Single), use_last_error=False)(("VarR4FromR8", windll["OLEAUT32"]), ((1, 'dblIn'),(1, 'pfltOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR4FromCy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CY,POINTER(Single), use_last_error=False)(("VarR4FromCy", windll["OLEAUT32"]), ((1, 'cyIn'),(1, 'pfltOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR4FromDate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(Single), use_last_error=False)(("VarR4FromDate", windll["OLEAUT32"]), ((1, 'dateIn'),(1, 'pfltOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR4FromStr():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(Single), use_last_error=False)(("VarR4FromStr", windll["OLEAUT32"]), ((1, 'strIn'),(1, 'lcid'),(1, 'dwFlags'),(1, 'pfltOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR4FromDisp():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,UInt32,POINTER(Single), use_last_error=False)(("VarR4FromDisp", windll["OLEAUT32"]), ((1, 'pdispIn'),(1, 'lcid'),(1, 'pfltOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR4FromBool():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,POINTER(Single), use_last_error=False)(("VarR4FromBool", windll["OLEAUT32"]), ((1, 'boolIn'),(1, 'pfltOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR4FromI1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.CHAR,POINTER(Single), use_last_error=False)(("VarR4FromI1", windll["OLEAUT32"]), ((1, 'cIn'),(1, 'pfltOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR4FromUI2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(Single), use_last_error=False)(("VarR4FromUI2", windll["OLEAUT32"]), ((1, 'uiIn'),(1, 'pfltOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR4FromUI4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Single), use_last_error=False)(("VarR4FromUI4", windll["OLEAUT32"]), ((1, 'ulIn'),(1, 'pfltOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR4FromUI8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(Single), use_last_error=False)(("VarR4FromUI8", windll["OLEAUT32"]), ((1, 'ui64In'),(1, 'pfltOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR4FromDec():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.DECIMAL_head),POINTER(Single), use_last_error=False)(("VarR4FromDec", windll["OLEAUT32"]), ((1, 'pdecIn'),(1, 'pfltOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR8FromUI1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Byte,POINTER(Double), use_last_error=False)(("VarR8FromUI1", windll["OLEAUT32"]), ((1, 'bIn'),(1, 'pdblOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR8FromI2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,POINTER(Double), use_last_error=False)(("VarR8FromI2", windll["OLEAUT32"]), ((1, 'sIn'),(1, 'pdblOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR8FromI4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Double), use_last_error=False)(("VarR8FromI4", windll["OLEAUT32"]), ((1, 'lIn'),(1, 'pdblOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR8FromI8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int64,POINTER(Double), use_last_error=False)(("VarR8FromI8", windll["OLEAUT32"]), ((1, 'i64In'),(1, 'pdblOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR8FromR4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Single,POINTER(Double), use_last_error=False)(("VarR8FromR4", windll["OLEAUT32"]), ((1, 'fltIn'),(1, 'pdblOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR8FromCy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CY,POINTER(Double), use_last_error=False)(("VarR8FromCy", windll["OLEAUT32"]), ((1, 'cyIn'),(1, 'pdblOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR8FromDate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(Double), use_last_error=False)(("VarR8FromDate", windll["OLEAUT32"]), ((1, 'dateIn'),(1, 'pdblOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR8FromStr():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(Double), use_last_error=False)(("VarR8FromStr", windll["OLEAUT32"]), ((1, 'strIn'),(1, 'lcid'),(1, 'dwFlags'),(1, 'pdblOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR8FromDisp():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,UInt32,POINTER(Double), use_last_error=False)(("VarR8FromDisp", windll["OLEAUT32"]), ((1, 'pdispIn'),(1, 'lcid'),(1, 'pdblOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR8FromBool():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,POINTER(Double), use_last_error=False)(("VarR8FromBool", windll["OLEAUT32"]), ((1, 'boolIn'),(1, 'pdblOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR8FromI1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.CHAR,POINTER(Double), use_last_error=False)(("VarR8FromI1", windll["OLEAUT32"]), ((1, 'cIn'),(1, 'pdblOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR8FromUI2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(Double), use_last_error=False)(("VarR8FromUI2", windll["OLEAUT32"]), ((1, 'uiIn'),(1, 'pdblOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR8FromUI4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Double), use_last_error=False)(("VarR8FromUI4", windll["OLEAUT32"]), ((1, 'ulIn'),(1, 'pdblOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR8FromUI8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(Double), use_last_error=False)(("VarR8FromUI8", windll["OLEAUT32"]), ((1, 'ui64In'),(1, 'pdblOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR8FromDec():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.DECIMAL_head),POINTER(Double), use_last_error=False)(("VarR8FromDec", windll["OLEAUT32"]), ((1, 'pdecIn'),(1, 'pdblOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDateFromUI1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Byte,POINTER(Double), use_last_error=False)(("VarDateFromUI1", windll["OLEAUT32"]), ((1, 'bIn'),(1, 'pdateOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDateFromI2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,POINTER(Double), use_last_error=False)(("VarDateFromI2", windll["OLEAUT32"]), ((1, 'sIn'),(1, 'pdateOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDateFromI4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Double), use_last_error=False)(("VarDateFromI4", windll["OLEAUT32"]), ((1, 'lIn'),(1, 'pdateOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDateFromI8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int64,POINTER(Double), use_last_error=False)(("VarDateFromI8", windll["OLEAUT32"]), ((1, 'i64In'),(1, 'pdateOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDateFromR4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Single,POINTER(Double), use_last_error=False)(("VarDateFromR4", windll["OLEAUT32"]), ((1, 'fltIn'),(1, 'pdateOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDateFromR8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(Double), use_last_error=False)(("VarDateFromR8", windll["OLEAUT32"]), ((1, 'dblIn'),(1, 'pdateOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDateFromCy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CY,POINTER(Double), use_last_error=False)(("VarDateFromCy", windll["OLEAUT32"]), ((1, 'cyIn'),(1, 'pdateOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDateFromStr():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(Double), use_last_error=False)(("VarDateFromStr", windll["OLEAUT32"]), ((1, 'strIn'),(1, 'lcid'),(1, 'dwFlags'),(1, 'pdateOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDateFromDisp():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,UInt32,POINTER(Double), use_last_error=False)(("VarDateFromDisp", windll["OLEAUT32"]), ((1, 'pdispIn'),(1, 'lcid'),(1, 'pdateOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDateFromBool():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,POINTER(Double), use_last_error=False)(("VarDateFromBool", windll["OLEAUT32"]), ((1, 'boolIn'),(1, 'pdateOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDateFromI1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.CHAR,POINTER(Double), use_last_error=False)(("VarDateFromI1", windll["OLEAUT32"]), ((1, 'cIn'),(1, 'pdateOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDateFromUI2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(Double), use_last_error=False)(("VarDateFromUI2", windll["OLEAUT32"]), ((1, 'uiIn'),(1, 'pdateOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDateFromUI4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Double), use_last_error=False)(("VarDateFromUI4", windll["OLEAUT32"]), ((1, 'ulIn'),(1, 'pdateOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDateFromUI8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(Double), use_last_error=False)(("VarDateFromUI8", windll["OLEAUT32"]), ((1, 'ui64In'),(1, 'pdateOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDateFromDec():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.DECIMAL_head),POINTER(Double), use_last_error=False)(("VarDateFromDec", windll["OLEAUT32"]), ((1, 'pdecIn'),(1, 'pdateOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarCyFromUI1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Byte,POINTER(win32more.System.Com.CY_head), use_last_error=False)(("VarCyFromUI1", windll["OLEAUT32"]), ((1, 'bIn'),(1, 'pcyOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarCyFromI2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,POINTER(win32more.System.Com.CY_head), use_last_error=False)(("VarCyFromI2", windll["OLEAUT32"]), ((1, 'sIn'),(1, 'pcyOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarCyFromI4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.System.Com.CY_head), use_last_error=False)(("VarCyFromI4", windll["OLEAUT32"]), ((1, 'lIn'),(1, 'pcyOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarCyFromI8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int64,POINTER(win32more.System.Com.CY_head), use_last_error=False)(("VarCyFromI8", windll["OLEAUT32"]), ((1, 'i64In'),(1, 'pcyOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarCyFromR4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Single,POINTER(win32more.System.Com.CY_head), use_last_error=False)(("VarCyFromR4", windll["OLEAUT32"]), ((1, 'fltIn'),(1, 'pcyOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarCyFromR8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(win32more.System.Com.CY_head), use_last_error=False)(("VarCyFromR8", windll["OLEAUT32"]), ((1, 'dblIn'),(1, 'pcyOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarCyFromDate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(win32more.System.Com.CY_head), use_last_error=False)(("VarCyFromDate", windll["OLEAUT32"]), ((1, 'dateIn'),(1, 'pcyOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarCyFromStr():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(win32more.System.Com.CY_head), use_last_error=False)(("VarCyFromStr", windll["OLEAUT32"]), ((1, 'strIn'),(1, 'lcid'),(1, 'dwFlags'),(1, 'pcyOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarCyFromDisp():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,UInt32,POINTER(win32more.System.Com.CY_head), use_last_error=False)(("VarCyFromDisp", windll["OLEAUT32"]), ((1, 'pdispIn'),(1, 'lcid'),(1, 'pcyOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarCyFromBool():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,POINTER(win32more.System.Com.CY_head), use_last_error=False)(("VarCyFromBool", windll["OLEAUT32"]), ((1, 'boolIn'),(1, 'pcyOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarCyFromI1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.CHAR,POINTER(win32more.System.Com.CY_head), use_last_error=False)(("VarCyFromI1", windll["OLEAUT32"]), ((1, 'cIn'),(1, 'pcyOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarCyFromUI2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.System.Com.CY_head), use_last_error=False)(("VarCyFromUI2", windll["OLEAUT32"]), ((1, 'uiIn'),(1, 'pcyOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarCyFromUI4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.CY_head), use_last_error=False)(("VarCyFromUI4", windll["OLEAUT32"]), ((1, 'ulIn'),(1, 'pcyOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarCyFromUI8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(win32more.System.Com.CY_head), use_last_error=False)(("VarCyFromUI8", windll["OLEAUT32"]), ((1, 'ui64In'),(1, 'pcyOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarCyFromDec():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.DECIMAL_head),POINTER(win32more.System.Com.CY_head), use_last_error=False)(("VarCyFromDec", windll["OLEAUT32"]), ((1, 'pdecIn'),(1, 'pcyOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBstrFromUI1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Byte,UInt32,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("VarBstrFromUI1", windll["OLEAUT32"]), ((1, 'bVal'),(1, 'lcid'),(1, 'dwFlags'),(1, 'pbstrOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBstrFromI2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,UInt32,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("VarBstrFromI2", windll["OLEAUT32"]), ((1, 'iVal'),(1, 'lcid'),(1, 'dwFlags'),(1, 'pbstrOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBstrFromI4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,UInt32,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("VarBstrFromI4", windll["OLEAUT32"]), ((1, 'lIn'),(1, 'lcid'),(1, 'dwFlags'),(1, 'pbstrOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBstrFromI8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int64,UInt32,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("VarBstrFromI8", windll["OLEAUT32"]), ((1, 'i64In'),(1, 'lcid'),(1, 'dwFlags'),(1, 'pbstrOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBstrFromR4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Single,UInt32,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("VarBstrFromR4", windll["OLEAUT32"]), ((1, 'fltIn'),(1, 'lcid'),(1, 'dwFlags'),(1, 'pbstrOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBstrFromR8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,UInt32,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("VarBstrFromR8", windll["OLEAUT32"]), ((1, 'dblIn'),(1, 'lcid'),(1, 'dwFlags'),(1, 'pbstrOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBstrFromCy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CY,UInt32,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("VarBstrFromCy", windll["OLEAUT32"]), ((1, 'cyIn'),(1, 'lcid'),(1, 'dwFlags'),(1, 'pbstrOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBstrFromDate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,UInt32,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("VarBstrFromDate", windll["OLEAUT32"]), ((1, 'dateIn'),(1, 'lcid'),(1, 'dwFlags'),(1, 'pbstrOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBstrFromDisp():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,UInt32,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("VarBstrFromDisp", windll["OLEAUT32"]), ((1, 'pdispIn'),(1, 'lcid'),(1, 'dwFlags'),(1, 'pbstrOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBstrFromBool():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,UInt32,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("VarBstrFromBool", windll["OLEAUT32"]), ((1, 'boolIn'),(1, 'lcid'),(1, 'dwFlags'),(1, 'pbstrOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBstrFromI1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.CHAR,UInt32,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("VarBstrFromI1", windll["OLEAUT32"]), ((1, 'cIn'),(1, 'lcid'),(1, 'dwFlags'),(1, 'pbstrOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBstrFromUI2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,UInt32,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("VarBstrFromUI2", windll["OLEAUT32"]), ((1, 'uiIn'),(1, 'lcid'),(1, 'dwFlags'),(1, 'pbstrOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBstrFromUI4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("VarBstrFromUI4", windll["OLEAUT32"]), ((1, 'ulIn'),(1, 'lcid'),(1, 'dwFlags'),(1, 'pbstrOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBstrFromUI8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,UInt32,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("VarBstrFromUI8", windll["OLEAUT32"]), ((1, 'ui64In'),(1, 'lcid'),(1, 'dwFlags'),(1, 'pbstrOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBstrFromDec():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.DECIMAL_head),UInt32,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("VarBstrFromDec", windll["OLEAUT32"]), ((1, 'pdecIn'),(1, 'lcid'),(1, 'dwFlags'),(1, 'pbstrOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBoolFromUI1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Byte,POINTER(Int16), use_last_error=False)(("VarBoolFromUI1", windll["OLEAUT32"]), ((1, 'bIn'),(1, 'pboolOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBoolFromI2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,POINTER(Int16), use_last_error=False)(("VarBoolFromI2", windll["OLEAUT32"]), ((1, 'sIn'),(1, 'pboolOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBoolFromI4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(Int16), use_last_error=False)(("VarBoolFromI4", windll["OLEAUT32"]), ((1, 'lIn'),(1, 'pboolOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBoolFromI8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int64,POINTER(Int16), use_last_error=False)(("VarBoolFromI8", windll["OLEAUT32"]), ((1, 'i64In'),(1, 'pboolOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBoolFromR4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Single,POINTER(Int16), use_last_error=False)(("VarBoolFromR4", windll["OLEAUT32"]), ((1, 'fltIn'),(1, 'pboolOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBoolFromR8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(Int16), use_last_error=False)(("VarBoolFromR8", windll["OLEAUT32"]), ((1, 'dblIn'),(1, 'pboolOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBoolFromDate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(Int16), use_last_error=False)(("VarBoolFromDate", windll["OLEAUT32"]), ((1, 'dateIn'),(1, 'pboolOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBoolFromCy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CY,POINTER(Int16), use_last_error=False)(("VarBoolFromCy", windll["OLEAUT32"]), ((1, 'cyIn'),(1, 'pboolOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBoolFromStr():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(Int16), use_last_error=False)(("VarBoolFromStr", windll["OLEAUT32"]), ((1, 'strIn'),(1, 'lcid'),(1, 'dwFlags'),(1, 'pboolOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBoolFromDisp():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,UInt32,POINTER(Int16), use_last_error=False)(("VarBoolFromDisp", windll["OLEAUT32"]), ((1, 'pdispIn'),(1, 'lcid'),(1, 'pboolOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBoolFromI1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.CHAR,POINTER(Int16), use_last_error=False)(("VarBoolFromI1", windll["OLEAUT32"]), ((1, 'cIn'),(1, 'pboolOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBoolFromUI2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(Int16), use_last_error=False)(("VarBoolFromUI2", windll["OLEAUT32"]), ((1, 'uiIn'),(1, 'pboolOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBoolFromUI4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Int16), use_last_error=False)(("VarBoolFromUI4", windll["OLEAUT32"]), ((1, 'ulIn'),(1, 'pboolOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBoolFromUI8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(Int16), use_last_error=False)(("VarBoolFromUI8", windll["OLEAUT32"]), ((1, 'i64In'),(1, 'pboolOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBoolFromDec():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.DECIMAL_head),POINTER(Int16), use_last_error=False)(("VarBoolFromDec", windll["OLEAUT32"]), ((1, 'pdecIn'),(1, 'pboolOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI1FromUI1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Byte,win32more.Foundation.PSTR, use_last_error=False)(("VarI1FromUI1", windll["OLEAUT32"]), ((1, 'bIn'),(1, 'pcOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI1FromI2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,win32more.Foundation.PSTR, use_last_error=False)(("VarI1FromI2", windll["OLEAUT32"]), ((1, 'uiIn'),(1, 'pcOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI1FromI4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,win32more.Foundation.PSTR, use_last_error=False)(("VarI1FromI4", windll["OLEAUT32"]), ((1, 'lIn'),(1, 'pcOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI1FromI8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int64,win32more.Foundation.PSTR, use_last_error=False)(("VarI1FromI8", windll["OLEAUT32"]), ((1, 'i64In'),(1, 'pcOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI1FromR4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Single,win32more.Foundation.PSTR, use_last_error=False)(("VarI1FromR4", windll["OLEAUT32"]), ((1, 'fltIn'),(1, 'pcOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI1FromR8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,win32more.Foundation.PSTR, use_last_error=False)(("VarI1FromR8", windll["OLEAUT32"]), ((1, 'dblIn'),(1, 'pcOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI1FromDate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,win32more.Foundation.PSTR, use_last_error=False)(("VarI1FromDate", windll["OLEAUT32"]), ((1, 'dateIn'),(1, 'pcOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI1FromCy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CY,win32more.Foundation.PSTR, use_last_error=False)(("VarI1FromCy", windll["OLEAUT32"]), ((1, 'cyIn'),(1, 'pcOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI1FromStr():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,win32more.Foundation.PSTR, use_last_error=False)(("VarI1FromStr", windll["OLEAUT32"]), ((1, 'strIn'),(1, 'lcid'),(1, 'dwFlags'),(1, 'pcOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI1FromDisp():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,UInt32,win32more.Foundation.PSTR, use_last_error=False)(("VarI1FromDisp", windll["OLEAUT32"]), ((1, 'pdispIn'),(1, 'lcid'),(1, 'pcOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI1FromBool():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,win32more.Foundation.PSTR, use_last_error=False)(("VarI1FromBool", windll["OLEAUT32"]), ((1, 'boolIn'),(1, 'pcOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI1FromUI2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,win32more.Foundation.PSTR, use_last_error=False)(("VarI1FromUI2", windll["OLEAUT32"]), ((1, 'uiIn'),(1, 'pcOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI1FromUI4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PSTR, use_last_error=False)(("VarI1FromUI4", windll["OLEAUT32"]), ((1, 'ulIn'),(1, 'pcOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI1FromUI8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,win32more.Foundation.PSTR, use_last_error=False)(("VarI1FromUI8", windll["OLEAUT32"]), ((1, 'i64In'),(1, 'pcOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarI1FromDec():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.DECIMAL_head),win32more.Foundation.PSTR, use_last_error=False)(("VarI1FromDec", windll["OLEAUT32"]), ((1, 'pdecIn'),(1, 'pcOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI2FromUI1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Byte,POINTER(UInt16), use_last_error=False)(("VarUI2FromUI1", windll["OLEAUT32"]), ((1, 'bIn'),(1, 'puiOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI2FromI2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,POINTER(UInt16), use_last_error=False)(("VarUI2FromI2", windll["OLEAUT32"]), ((1, 'uiIn'),(1, 'puiOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI2FromI4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(UInt16), use_last_error=False)(("VarUI2FromI4", windll["OLEAUT32"]), ((1, 'lIn'),(1, 'puiOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI2FromI8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int64,POINTER(UInt16), use_last_error=False)(("VarUI2FromI8", windll["OLEAUT32"]), ((1, 'i64In'),(1, 'puiOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI2FromR4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Single,POINTER(UInt16), use_last_error=False)(("VarUI2FromR4", windll["OLEAUT32"]), ((1, 'fltIn'),(1, 'puiOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI2FromR8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(UInt16), use_last_error=False)(("VarUI2FromR8", windll["OLEAUT32"]), ((1, 'dblIn'),(1, 'puiOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI2FromDate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(UInt16), use_last_error=False)(("VarUI2FromDate", windll["OLEAUT32"]), ((1, 'dateIn'),(1, 'puiOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI2FromCy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CY,POINTER(UInt16), use_last_error=False)(("VarUI2FromCy", windll["OLEAUT32"]), ((1, 'cyIn'),(1, 'puiOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI2FromStr():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(UInt16), use_last_error=False)(("VarUI2FromStr", windll["OLEAUT32"]), ((1, 'strIn'),(1, 'lcid'),(1, 'dwFlags'),(1, 'puiOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI2FromDisp():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,UInt32,POINTER(UInt16), use_last_error=False)(("VarUI2FromDisp", windll["OLEAUT32"]), ((1, 'pdispIn'),(1, 'lcid'),(1, 'puiOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI2FromBool():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,POINTER(UInt16), use_last_error=False)(("VarUI2FromBool", windll["OLEAUT32"]), ((1, 'boolIn'),(1, 'puiOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI2FromI1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.CHAR,POINTER(UInt16), use_last_error=False)(("VarUI2FromI1", windll["OLEAUT32"]), ((1, 'cIn'),(1, 'puiOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI2FromUI4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt16), use_last_error=False)(("VarUI2FromUI4", windll["OLEAUT32"]), ((1, 'ulIn'),(1, 'puiOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI2FromUI8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(UInt16), use_last_error=False)(("VarUI2FromUI8", windll["OLEAUT32"]), ((1, 'i64In'),(1, 'puiOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI2FromDec():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.DECIMAL_head),POINTER(UInt16), use_last_error=False)(("VarUI2FromDec", windll["OLEAUT32"]), ((1, 'pdecIn'),(1, 'puiOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI4FromUI1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Byte,POINTER(UInt32), use_last_error=False)(("VarUI4FromUI1", windll["OLEAUT32"]), ((1, 'bIn'),(1, 'pulOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI4FromI2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,POINTER(UInt32), use_last_error=False)(("VarUI4FromI2", windll["OLEAUT32"]), ((1, 'uiIn'),(1, 'pulOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI4FromI4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(UInt32), use_last_error=False)(("VarUI4FromI4", windll["OLEAUT32"]), ((1, 'lIn'),(1, 'pulOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI4FromI8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int64,POINTER(UInt32), use_last_error=False)(("VarUI4FromI8", windll["OLEAUT32"]), ((1, 'i64In'),(1, 'plOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI4FromR4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Single,POINTER(UInt32), use_last_error=False)(("VarUI4FromR4", windll["OLEAUT32"]), ((1, 'fltIn'),(1, 'pulOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI4FromR8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(UInt32), use_last_error=False)(("VarUI4FromR8", windll["OLEAUT32"]), ((1, 'dblIn'),(1, 'pulOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI4FromDate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(UInt32), use_last_error=False)(("VarUI4FromDate", windll["OLEAUT32"]), ((1, 'dateIn'),(1, 'pulOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI4FromCy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CY,POINTER(UInt32), use_last_error=False)(("VarUI4FromCy", windll["OLEAUT32"]), ((1, 'cyIn'),(1, 'pulOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI4FromStr():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(UInt32), use_last_error=False)(("VarUI4FromStr", windll["OLEAUT32"]), ((1, 'strIn'),(1, 'lcid'),(1, 'dwFlags'),(1, 'pulOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI4FromDisp():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,UInt32,POINTER(UInt32), use_last_error=False)(("VarUI4FromDisp", windll["OLEAUT32"]), ((1, 'pdispIn'),(1, 'lcid'),(1, 'pulOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI4FromBool():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,POINTER(UInt32), use_last_error=False)(("VarUI4FromBool", windll["OLEAUT32"]), ((1, 'boolIn'),(1, 'pulOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI4FromI1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.CHAR,POINTER(UInt32), use_last_error=False)(("VarUI4FromI1", windll["OLEAUT32"]), ((1, 'cIn'),(1, 'pulOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI4FromUI2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(UInt32), use_last_error=False)(("VarUI4FromUI2", windll["OLEAUT32"]), ((1, 'uiIn'),(1, 'pulOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI4FromUI8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(UInt32), use_last_error=False)(("VarUI4FromUI8", windll["OLEAUT32"]), ((1, 'ui64In'),(1, 'plOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI4FromDec():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.DECIMAL_head),POINTER(UInt32), use_last_error=False)(("VarUI4FromDec", windll["OLEAUT32"]), ((1, 'pdecIn'),(1, 'pulOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI8FromUI1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Byte,POINTER(UInt64), use_last_error=False)(("VarUI8FromUI1", windll["OLEAUT32"]), ((1, 'bIn'),(1, 'pi64Out'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI8FromI2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,POINTER(UInt64), use_last_error=False)(("VarUI8FromI2", windll["OLEAUT32"]), ((1, 'sIn'),(1, 'pi64Out'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI8FromI8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int64,POINTER(UInt64), use_last_error=False)(("VarUI8FromI8", windll["OLEAUT32"]), ((1, 'ui64In'),(1, 'pi64Out'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI8FromR4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Single,POINTER(UInt64), use_last_error=False)(("VarUI8FromR4", windll["OLEAUT32"]), ((1, 'fltIn'),(1, 'pi64Out'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI8FromR8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(UInt64), use_last_error=False)(("VarUI8FromR8", windll["OLEAUT32"]), ((1, 'dblIn'),(1, 'pi64Out'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI8FromCy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CY,POINTER(UInt64), use_last_error=False)(("VarUI8FromCy", windll["OLEAUT32"]), ((1, 'cyIn'),(1, 'pi64Out'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI8FromDate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(UInt64), use_last_error=False)(("VarUI8FromDate", windll["OLEAUT32"]), ((1, 'dateIn'),(1, 'pi64Out'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI8FromStr():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(UInt64), use_last_error=False)(("VarUI8FromStr", windll["OLEAUT32"]), ((1, 'strIn'),(1, 'lcid'),(1, 'dwFlags'),(1, 'pi64Out'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI8FromDisp():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,UInt32,POINTER(UInt64), use_last_error=False)(("VarUI8FromDisp", windll["OLEAUT32"]), ((1, 'pdispIn'),(1, 'lcid'),(1, 'pi64Out'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI8FromBool():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,POINTER(UInt64), use_last_error=False)(("VarUI8FromBool", windll["OLEAUT32"]), ((1, 'boolIn'),(1, 'pi64Out'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI8FromI1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.CHAR,POINTER(UInt64), use_last_error=False)(("VarUI8FromI1", windll["OLEAUT32"]), ((1, 'cIn'),(1, 'pi64Out'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI8FromUI2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(UInt64), use_last_error=False)(("VarUI8FromUI2", windll["OLEAUT32"]), ((1, 'uiIn'),(1, 'pi64Out'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI8FromUI4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt64), use_last_error=False)(("VarUI8FromUI4", windll["OLEAUT32"]), ((1, 'ulIn'),(1, 'pi64Out'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUI8FromDec():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.DECIMAL_head),POINTER(UInt64), use_last_error=False)(("VarUI8FromDec", windll["OLEAUT32"]), ((1, 'pdecIn'),(1, 'pi64Out'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDecFromUI1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Byte,POINTER(win32more.Foundation.DECIMAL_head), use_last_error=False)(("VarDecFromUI1", windll["OLEAUT32"]), ((1, 'bIn'),(1, 'pdecOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDecFromI2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,POINTER(win32more.Foundation.DECIMAL_head), use_last_error=False)(("VarDecFromI2", windll["OLEAUT32"]), ((1, 'uiIn'),(1, 'pdecOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDecFromI4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Foundation.DECIMAL_head), use_last_error=False)(("VarDecFromI4", windll["OLEAUT32"]), ((1, 'lIn'),(1, 'pdecOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDecFromI8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int64,POINTER(win32more.Foundation.DECIMAL_head), use_last_error=False)(("VarDecFromI8", windll["OLEAUT32"]), ((1, 'i64In'),(1, 'pdecOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDecFromR4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Single,POINTER(win32more.Foundation.DECIMAL_head), use_last_error=False)(("VarDecFromR4", windll["OLEAUT32"]), ((1, 'fltIn'),(1, 'pdecOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDecFromR8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(win32more.Foundation.DECIMAL_head), use_last_error=False)(("VarDecFromR8", windll["OLEAUT32"]), ((1, 'dblIn'),(1, 'pdecOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDecFromDate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,POINTER(win32more.Foundation.DECIMAL_head), use_last_error=False)(("VarDecFromDate", windll["OLEAUT32"]), ((1, 'dateIn'),(1, 'pdecOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDecFromCy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CY,POINTER(win32more.Foundation.DECIMAL_head), use_last_error=False)(("VarDecFromCy", windll["OLEAUT32"]), ((1, 'cyIn'),(1, 'pdecOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDecFromStr():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(win32more.Foundation.DECIMAL_head), use_last_error=False)(("VarDecFromStr", windll["OLEAUT32"]), ((1, 'strIn'),(1, 'lcid'),(1, 'dwFlags'),(1, 'pdecOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDecFromDisp():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,UInt32,POINTER(win32more.Foundation.DECIMAL_head), use_last_error=False)(("VarDecFromDisp", windll["OLEAUT32"]), ((1, 'pdispIn'),(1, 'lcid'),(1, 'pdecOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDecFromBool():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,POINTER(win32more.Foundation.DECIMAL_head), use_last_error=False)(("VarDecFromBool", windll["OLEAUT32"]), ((1, 'boolIn'),(1, 'pdecOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDecFromI1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.CHAR,POINTER(win32more.Foundation.DECIMAL_head), use_last_error=False)(("VarDecFromI1", windll["OLEAUT32"]), ((1, 'cIn'),(1, 'pdecOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDecFromUI2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt16,POINTER(win32more.Foundation.DECIMAL_head), use_last_error=False)(("VarDecFromUI2", windll["OLEAUT32"]), ((1, 'uiIn'),(1, 'pdecOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDecFromUI4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.DECIMAL_head), use_last_error=False)(("VarDecFromUI4", windll["OLEAUT32"]), ((1, 'ulIn'),(1, 'pdecOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDecFromUI8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(win32more.Foundation.DECIMAL_head), use_last_error=False)(("VarDecFromUI8", windll["OLEAUT32"]), ((1, 'ui64In'),(1, 'pdecOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarParseNumFromStr():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(win32more.System.Ole.NUMPARSE_head),c_char_p_no, use_last_error=False)(("VarParseNumFromStr", windll["OLEAUT32"]), ((1, 'strIn'),(1, 'lcid'),(1, 'dwFlags'),(1, 'pnumprs'),(1, 'rgbDig'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarNumFromParseNum():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.NUMPARSE_head),c_char_p_no,UInt32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VarNumFromParseNum", windll["OLEAUT32"]), ((1, 'pnumprs'),(1, 'rgbDig'),(1, 'dwVtBits'),(1, 'pvar'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarAdd():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VarAdd", windll["OLEAUT32"]), ((1, 'pvarLeft'),(1, 'pvarRight'),(1, 'pvarResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarAnd():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VarAnd", windll["OLEAUT32"]), ((1, 'pvarLeft'),(1, 'pvarRight'),(1, 'pvarResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarCat():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VarCat", windll["OLEAUT32"]), ((1, 'pvarLeft'),(1, 'pvarRight'),(1, 'pvarResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDiv():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VarDiv", windll["OLEAUT32"]), ((1, 'pvarLeft'),(1, 'pvarRight'),(1, 'pvarResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarEqv():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VarEqv", windll["OLEAUT32"]), ((1, 'pvarLeft'),(1, 'pvarRight'),(1, 'pvarResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarIdiv():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VarIdiv", windll["OLEAUT32"]), ((1, 'pvarLeft'),(1, 'pvarRight'),(1, 'pvarResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarImp():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VarImp", windll["OLEAUT32"]), ((1, 'pvarLeft'),(1, 'pvarRight'),(1, 'pvarResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarMod():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VarMod", windll["OLEAUT32"]), ((1, 'pvarLeft'),(1, 'pvarRight'),(1, 'pvarResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarMul():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VarMul", windll["OLEAUT32"]), ((1, 'pvarLeft'),(1, 'pvarRight'),(1, 'pvarResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarOr():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VarOr", windll["OLEAUT32"]), ((1, 'pvarLeft'),(1, 'pvarRight'),(1, 'pvarResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarPow():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VarPow", windll["OLEAUT32"]), ((1, 'pvarLeft'),(1, 'pvarRight'),(1, 'pvarResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarSub():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VarSub", windll["OLEAUT32"]), ((1, 'pvarLeft'),(1, 'pvarRight'),(1, 'pvarResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarXor():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VarXor", windll["OLEAUT32"]), ((1, 'pvarLeft'),(1, 'pvarRight'),(1, 'pvarResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarAbs():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VarAbs", windll["OLEAUT32"]), ((1, 'pvarIn'),(1, 'pvarResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarFix():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VarFix", windll["OLEAUT32"]), ((1, 'pvarIn'),(1, 'pvarResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarInt():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VarInt", windll["OLEAUT32"]), ((1, 'pvarIn'),(1, 'pvarResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarNeg():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VarNeg", windll["OLEAUT32"]), ((1, 'pvarIn'),(1, 'pvarResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarNot():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VarNot", windll["OLEAUT32"]), ((1, 'pvarIn'),(1, 'pvarResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarRound():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),Int32,POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("VarRound", windll["OLEAUT32"]), ((1, 'pvarIn'),(1, 'cDecimals'),(1, 'pvarResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarCmp():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.VARIANT_head),UInt32,UInt32, use_last_error=False)(("VarCmp", windll["OLEAUT32"]), ((1, 'pvarLeft'),(1, 'pvarRight'),(1, 'lcid'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDecAdd():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.DECIMAL_head),POINTER(win32more.Foundation.DECIMAL_head),POINTER(win32more.Foundation.DECIMAL_head), use_last_error=False)(("VarDecAdd", windll["OLEAUT32"]), ((1, 'pdecLeft'),(1, 'pdecRight'),(1, 'pdecResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDecDiv():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.DECIMAL_head),POINTER(win32more.Foundation.DECIMAL_head),POINTER(win32more.Foundation.DECIMAL_head), use_last_error=False)(("VarDecDiv", windll["OLEAUT32"]), ((1, 'pdecLeft'),(1, 'pdecRight'),(1, 'pdecResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDecMul():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.DECIMAL_head),POINTER(win32more.Foundation.DECIMAL_head),POINTER(win32more.Foundation.DECIMAL_head), use_last_error=False)(("VarDecMul", windll["OLEAUT32"]), ((1, 'pdecLeft'),(1, 'pdecRight'),(1, 'pdecResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDecSub():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.DECIMAL_head),POINTER(win32more.Foundation.DECIMAL_head),POINTER(win32more.Foundation.DECIMAL_head), use_last_error=False)(("VarDecSub", windll["OLEAUT32"]), ((1, 'pdecLeft'),(1, 'pdecRight'),(1, 'pdecResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDecAbs():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.DECIMAL_head),POINTER(win32more.Foundation.DECIMAL_head), use_last_error=False)(("VarDecAbs", windll["OLEAUT32"]), ((1, 'pdecIn'),(1, 'pdecResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDecFix():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.DECIMAL_head),POINTER(win32more.Foundation.DECIMAL_head), use_last_error=False)(("VarDecFix", windll["OLEAUT32"]), ((1, 'pdecIn'),(1, 'pdecResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDecInt():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.DECIMAL_head),POINTER(win32more.Foundation.DECIMAL_head), use_last_error=False)(("VarDecInt", windll["OLEAUT32"]), ((1, 'pdecIn'),(1, 'pdecResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDecNeg():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.DECIMAL_head),POINTER(win32more.Foundation.DECIMAL_head), use_last_error=False)(("VarDecNeg", windll["OLEAUT32"]), ((1, 'pdecIn'),(1, 'pdecResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDecRound():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.DECIMAL_head),Int32,POINTER(win32more.Foundation.DECIMAL_head), use_last_error=False)(("VarDecRound", windll["OLEAUT32"]), ((1, 'pdecIn'),(1, 'cDecimals'),(1, 'pdecResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDecCmp():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.DECIMAL_head),POINTER(win32more.Foundation.DECIMAL_head), use_last_error=False)(("VarDecCmp", windll["OLEAUT32"]), ((1, 'pdecLeft'),(1, 'pdecRight'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDecCmpR8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.DECIMAL_head),Double, use_last_error=False)(("VarDecCmpR8", windll["OLEAUT32"]), ((1, 'pdecLeft'),(1, 'dblRight'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarCyAdd():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CY,win32more.System.Com.CY,POINTER(win32more.System.Com.CY_head), use_last_error=False)(("VarCyAdd", windll["OLEAUT32"]), ((1, 'cyLeft'),(1, 'cyRight'),(1, 'pcyResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarCyMul():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CY,win32more.System.Com.CY,POINTER(win32more.System.Com.CY_head), use_last_error=False)(("VarCyMul", windll["OLEAUT32"]), ((1, 'cyLeft'),(1, 'cyRight'),(1, 'pcyResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarCyMulI4():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CY,Int32,POINTER(win32more.System.Com.CY_head), use_last_error=False)(("VarCyMulI4", windll["OLEAUT32"]), ((1, 'cyLeft'),(1, 'lRight'),(1, 'pcyResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarCyMulI8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CY,Int64,POINTER(win32more.System.Com.CY_head), use_last_error=False)(("VarCyMulI8", windll["OLEAUT32"]), ((1, 'cyLeft'),(1, 'lRight'),(1, 'pcyResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarCySub():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CY,win32more.System.Com.CY,POINTER(win32more.System.Com.CY_head), use_last_error=False)(("VarCySub", windll["OLEAUT32"]), ((1, 'cyLeft'),(1, 'cyRight'),(1, 'pcyResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarCyAbs():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CY,POINTER(win32more.System.Com.CY_head), use_last_error=False)(("VarCyAbs", windll["OLEAUT32"]), ((1, 'cyIn'),(1, 'pcyResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarCyFix():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CY,POINTER(win32more.System.Com.CY_head), use_last_error=False)(("VarCyFix", windll["OLEAUT32"]), ((1, 'cyIn'),(1, 'pcyResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarCyInt():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CY,POINTER(win32more.System.Com.CY_head), use_last_error=False)(("VarCyInt", windll["OLEAUT32"]), ((1, 'cyIn'),(1, 'pcyResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarCyNeg():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CY,POINTER(win32more.System.Com.CY_head), use_last_error=False)(("VarCyNeg", windll["OLEAUT32"]), ((1, 'cyIn'),(1, 'pcyResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarCyRound():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CY,Int32,POINTER(win32more.System.Com.CY_head), use_last_error=False)(("VarCyRound", windll["OLEAUT32"]), ((1, 'cyIn'),(1, 'cDecimals'),(1, 'pcyResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarCyCmp():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CY,win32more.System.Com.CY, use_last_error=False)(("VarCyCmp", windll["OLEAUT32"]), ((1, 'cyLeft'),(1, 'cyRight'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarCyCmpR8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.CY,Double, use_last_error=False)(("VarCyCmpR8", windll["OLEAUT32"]), ((1, 'cyLeft'),(1, 'dblRight'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBstrCat():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,POINTER(POINTER(UInt16)), use_last_error=False)(("VarBstrCat", windll["OLEAUT32"]), ((1, 'bstrLeft'),(1, 'bstrRight'),(1, 'pbstrResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarBstrCmp():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BSTR,win32more.Foundation.BSTR,UInt32,UInt32, use_last_error=False)(("VarBstrCmp", windll["OLEAUT32"]), ((1, 'bstrLeft'),(1, 'bstrRight'),(1, 'lcid'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR8Pow():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Double,POINTER(Double), use_last_error=False)(("VarR8Pow", windll["OLEAUT32"]), ((1, 'dblLeft'),(1, 'dblRight'),(1, 'pdblResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR4CmpR8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Single,Double, use_last_error=False)(("VarR4CmpR8", windll["OLEAUT32"]), ((1, 'fltLeft'),(1, 'dblRight'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarR8Round():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,Int32,POINTER(Double), use_last_error=False)(("VarR8Round", windll["OLEAUT32"]), ((1, 'dblIn'),(1, 'cDecimals'),(1, 'pdblResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDateFromUdate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.UDATE_head),UInt32,POINTER(Double), use_last_error=False)(("VarDateFromUdate", windll["OLEAUT32"]), ((1, 'pudateIn'),(1, 'dwFlags'),(1, 'pdateOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarDateFromUdateEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.UDATE_head),UInt32,UInt32,POINTER(Double), use_last_error=False)(("VarDateFromUdateEx", windll["OLEAUT32"]), ((1, 'pudateIn'),(1, 'lcid'),(1, 'dwFlags'),(1, 'pdateOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarUdateFromDate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Double,UInt32,POINTER(win32more.System.Ole.UDATE_head), use_last_error=False)(("VarUdateFromDate", windll["OLEAUT32"]), ((1, 'dateIn'),(1, 'dwFlags'),(1, 'pudateOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetAltMonthNames():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(POINTER(win32more.Foundation.PWSTR)), use_last_error=False)(("GetAltMonthNames", windll["OLEAUT32"]), ((1, 'lcid'),(1, 'prgp'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarFormat():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),win32more.Foundation.PWSTR,Int32,Int32,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("VarFormat", windll["OLEAUT32"]), ((1, 'pvarIn'),(1, 'pstrFormat'),(1, 'iFirstDay'),(1, 'iFirstWeek'),(1, 'dwFlags'),(1, 'pbstrOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarFormatDateTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),Int32,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("VarFormatDateTime", windll["OLEAUT32"]), ((1, 'pvarIn'),(1, 'iNamedFormat'),(1, 'dwFlags'),(1, 'pbstrOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarFormatNumber():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),Int32,Int32,Int32,Int32,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("VarFormatNumber", windll["OLEAUT32"]), ((1, 'pvarIn'),(1, 'iNumDig'),(1, 'iIncLead'),(1, 'iUseParens'),(1, 'iGroup'),(1, 'dwFlags'),(1, 'pbstrOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarFormatPercent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),Int32,Int32,Int32,Int32,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("VarFormatPercent", windll["OLEAUT32"]), ((1, 'pvarIn'),(1, 'iNumDig'),(1, 'iIncLead'),(1, 'iUseParens'),(1, 'iGroup'),(1, 'dwFlags'),(1, 'pbstrOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarFormatCurrency():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),Int32,Int32,Int32,Int32,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("VarFormatCurrency", windll["OLEAUT32"]), ((1, 'pvarIn'),(1, 'iNumDig'),(1, 'iIncLead'),(1, 'iUseParens'),(1, 'iGroup'),(1, 'dwFlags'),(1, 'pbstrOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarWeekdayName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,Int32,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("VarWeekdayName", windll["OLEAUT32"]), ((1, 'iWeekday'),(1, 'fAbbrev'),(1, 'iFirstDay'),(1, 'dwFlags'),(1, 'pbstrOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarMonthName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Int32,UInt32,POINTER(win32more.Foundation.BSTR), use_last_error=False)(("VarMonthName", windll["OLEAUT32"]), ((1, 'iMonth'),(1, 'fAbbrev'),(1, 'dwFlags'),(1, 'pbstrOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarFormatFromTokens():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.VARIANT_head),win32more.Foundation.PWSTR,c_char_p_no,UInt32,POINTER(win32more.Foundation.BSTR),UInt32, use_last_error=False)(("VarFormatFromTokens", windll["OLEAUT32"]), ((1, 'pvarIn'),(1, 'pstrFormat'),(1, 'pbTokCur'),(1, 'dwFlags'),(1, 'pbstrOut'),(1, 'lcid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VarTokenizeFormatString():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Byte),Int32,Int32,Int32,UInt32,POINTER(Int32), use_last_error=False)(("VarTokenizeFormatString", windll["OLEAUT32"]), ((1, 'pstrFormat'),(1, 'rgbTok'),(1, 'cbTok'),(1, 'iFirstDay'),(1, 'iFirstWeek'),(1, 'lcid'),(1, 'pcbActual'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LHashValOfNameSysA():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Com.SYSKIND,UInt32,win32more.Foundation.PSTR, use_last_error=False)(("LHashValOfNameSysA", windll["OLEAUT32"]), ((1, 'syskind'),(1, 'lcid'),(1, 'szName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LHashValOfNameSys():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.Com.SYSKIND,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(("LHashValOfNameSys", windll["OLEAUT32"]), ((1, 'syskind'),(1, 'lcid'),(1, 'szName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadTypeLib():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.ITypeLib_head), use_last_error=False)(("LoadTypeLib", windll["OLEAUT32"]), ((1, 'szFile'),(1, 'pptlib'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadTypeLibEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Ole.REGKIND,POINTER(win32more.System.Com.ITypeLib_head), use_last_error=False)(("LoadTypeLibEx", windll["OLEAUT32"]), ((1, 'szFile'),(1, 'regkind'),(1, 'pptlib'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LoadRegTypeLib():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt16,UInt16,UInt32,POINTER(win32more.System.Com.ITypeLib_head), use_last_error=False)(("LoadRegTypeLib", windll["OLEAUT32"]), ((1, 'rguid'),(1, 'wVerMajor'),(1, 'wVerMinor'),(1, 'lcid'),(1, 'pptlib'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryPathOfRegTypeLib():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt16,UInt16,UInt32,POINTER(POINTER(UInt16)), use_last_error=False)(("QueryPathOfRegTypeLib", windll["OLEAUT32"]), ((1, 'guid'),(1, 'wMaj'),(1, 'wMin'),(1, 'lcid'),(1, 'lpbstrPathName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterTypeLib():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.ITypeLib_head,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("RegisterTypeLib", windll["OLEAUT32"]), ((1, 'ptlib'),(1, 'szFullPath'),(1, 'szHelpDir'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnRegisterTypeLib():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt16,UInt16,UInt32,win32more.System.Com.SYSKIND, use_last_error=False)(("UnRegisterTypeLib", windll["OLEAUT32"]), ((1, 'libID'),(1, 'wVerMajor'),(1, 'wVerMinor'),(1, 'lcid'),(1, 'syskind'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterTypeLibForUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.ITypeLib_head,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR, use_last_error=False)(("RegisterTypeLibForUser", windll["OLEAUT32"]), ((1, 'ptlib'),(1, 'szFullPath'),(1, 'szHelpDir'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnRegisterTypeLibForUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt16,UInt16,UInt32,win32more.System.Com.SYSKIND, use_last_error=False)(("UnRegisterTypeLibForUser", windll["OLEAUT32"]), ((1, 'libID'),(1, 'wMajorVerNum'),(1, 'wMinorVerNum'),(1, 'lcid'),(1, 'syskind'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateTypeLib():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.SYSKIND,win32more.Foundation.PWSTR,POINTER(win32more.System.Ole.ICreateTypeLib_head), use_last_error=False)(("CreateTypeLib", windll["OLEAUT32"]), ((1, 'syskind'),(1, 'szFile'),(1, 'ppctlib'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateTypeLib2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.SYSKIND,win32more.Foundation.PWSTR,POINTER(win32more.System.Ole.ICreateTypeLib2_head), use_last_error=False)(("CreateTypeLib2", windll["OLEAUT32"]), ((1, 'syskind'),(1, 'szFile'),(1, 'ppctlib'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DispGetParam():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.DISPPARAMS_head),UInt32,UInt16,POINTER(win32more.System.Com.VARIANT_head),POINTER(UInt32), use_last_error=False)(("DispGetParam", windll["OLEAUT32"]), ((1, 'pdispparams'),(1, 'position'),(1, 'vtTarg'),(1, 'pvarResult'),(1, 'puArgErr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DispGetIDsOfNames():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.ITypeInfo_head,POINTER(win32more.Foundation.PWSTR),UInt32,POINTER(Int32), use_last_error=False)(("DispGetIDsOfNames", windll["OLEAUT32"]), ((1, 'ptinfo'),(1, 'rgszNames'),(1, 'cNames'),(1, 'rgdispid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DispInvoke():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.System.Com.ITypeInfo_head,Int32,UInt16,POINTER(win32more.System.Com.DISPPARAMS_head),POINTER(win32more.System.Com.VARIANT_head),POINTER(win32more.System.Com.EXCEPINFO_head),POINTER(UInt32), use_last_error=False)(("DispInvoke", windll["OLEAUT32"]), ((1, '_this'),(1, 'ptinfo'),(1, 'dispidMember'),(1, 'wFlags'),(1, 'pparams'),(1, 'pvarResult'),(1, 'pexcepinfo'),(1, 'puArgErr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateDispTypeInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.INTERFACEDATA_head),UInt32,POINTER(win32more.System.Com.ITypeInfo_head), use_last_error=False)(("CreateDispTypeInfo", windll["OLEAUT32"]), ((1, 'pidata'),(1, 'lcid'),(1, 'pptinfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateStdDispatch():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,c_void_p,win32more.System.Com.ITypeInfo_head,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(("CreateStdDispatch", windll["OLEAUT32"]), ((1, 'punkOuter'),(1, 'pvThis'),(1, 'ptinfo'),(1, 'ppunkStdDisp'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DispCallFunc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,win32more.System.Com.CALLCONV,UInt16,UInt32,POINTER(UInt16),POINTER(POINTER(win32more.System.Com.VARIANT_head)),POINTER(win32more.System.Com.VARIANT_head), use_last_error=False)(("DispCallFunc", windll["OLEAUT32"]), ((1, 'pvInstance'),(1, 'oVft'),(1, 'cc'),(1, 'vtReturn'),(1, 'cActuals'),(1, 'prgvt'),(1, 'prgpvarg'),(1, 'pvargResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterActiveObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,POINTER(Guid),UInt32,POINTER(UInt32), use_last_error=False)(("RegisterActiveObject", windll["OLEAUT32"]), ((1, 'punk'),(1, 'rclsid'),(1, 'dwFlags'),(1, 'pdwRegister'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RevokeActiveObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p, use_last_error=False)(("RevokeActiveObject", windll["OLEAUT32"]), ((1, 'dwRegister'),(1, 'pvReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetActiveObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),c_void_p,POINTER(win32more.System.Com.IUnknown_head), use_last_error=False)(("GetActiveObject", windll["OLEAUT32"]), ((1, 'rclsid'),(1, 'pvReserved'),(1, 'ppunk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateErrorInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.ICreateErrorInfo_head), use_last_error=False)(("CreateErrorInfo", windll["OLEAUT32"]), ((1, 'pperrinfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetRecordInfoFromTypeInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.ITypeInfo_head,POINTER(win32more.System.Ole.IRecordInfo_head), use_last_error=False)(("GetRecordInfoFromTypeInfo", windll["OLEAUT32"]), ((1, 'pTypeInfo'),(1, 'ppRecInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetRecordInfoFromGuids():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,UInt32,UInt32,POINTER(Guid),POINTER(win32more.System.Ole.IRecordInfo_head), use_last_error=False)(("GetRecordInfoFromGuids", windll["OLEAUT32"]), ((1, 'rGuidTypeLib'),(1, 'uVerMajor'),(1, 'uVerMinor'),(1, 'lcid'),(1, 'rGuidTypeInfo'),(1, 'ppRecInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OaBuildVersion():
    try:
        return WINFUNCTYPE(UInt32, use_last_error=False)(("OaBuildVersion", windll["OLEAUT32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_ClearCustData():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Com.CUSTDATA_head), use_last_error=False)(("ClearCustData", windll["OLEAUT32"]), ((1, 'pCustData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OaEnablePerUserTLibRegistration():
    try:
        return WINFUNCTYPE(Void, use_last_error=False)(("OaEnablePerUserTLibRegistration", windll["OLEAUT32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleBuildVersion():
    try:
        return WINFUNCTYPE(UInt32, use_last_error=False)(("OleBuildVersion", windll["ole32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleInitialize():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p, use_last_error=False)(("OleInitialize", windll["OLE32"]), ((1, 'pvReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleUninitialize():
    try:
        return WINFUNCTYPE(Void, use_last_error=False)(("OleUninitialize", windll["OLE32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleQueryLinkFromData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head, use_last_error=False)(("OleQueryLinkFromData", windll["OLE32"]), ((1, 'pSrcDataObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleQueryCreateFromData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head, use_last_error=False)(("OleQueryCreateFromData", windll["OLE32"]), ((1, 'pSrcDataObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleCreate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),UInt32,POINTER(win32more.System.Com.FORMATETC_head),win32more.System.Ole.IOleClientSite_head,win32more.System.Com.StructuredStorage.IStorage_head,POINTER(c_void_p), use_last_error=False)(("OleCreate", windll["OLE32"]), ((1, 'rclsid'),(1, 'riid'),(1, 'renderopt'),(1, 'pFormatEtc'),(1, 'pClientSite'),(1, 'pStg'),(1, 'ppvObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleCreateEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid),UInt32,UInt32,UInt32,POINTER(UInt32),POINTER(win32more.System.Com.FORMATETC_head),win32more.System.Com.IAdviseSink_head,POINTER(UInt32),win32more.System.Ole.IOleClientSite_head,win32more.System.Com.StructuredStorage.IStorage_head,POINTER(c_void_p), use_last_error=False)(("OleCreateEx", windll["ole32"]), ((1, 'rclsid'),(1, 'riid'),(1, 'dwFlags'),(1, 'renderopt'),(1, 'cFormats'),(1, 'rgAdvf'),(1, 'rgFormatEtc'),(1, 'lpAdviseSink'),(1, 'rgdwConnection'),(1, 'pClientSite'),(1, 'pStg'),(1, 'ppvObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleCreateFromData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head,POINTER(Guid),UInt32,POINTER(win32more.System.Com.FORMATETC_head),win32more.System.Ole.IOleClientSite_head,win32more.System.Com.StructuredStorage.IStorage_head,POINTER(c_void_p), use_last_error=False)(("OleCreateFromData", windll["OLE32"]), ((1, 'pSrcDataObj'),(1, 'riid'),(1, 'renderopt'),(1, 'pFormatEtc'),(1, 'pClientSite'),(1, 'pStg'),(1, 'ppvObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleCreateFromDataEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head,POINTER(Guid),UInt32,UInt32,UInt32,POINTER(UInt32),POINTER(win32more.System.Com.FORMATETC_head),win32more.System.Com.IAdviseSink_head,POINTER(UInt32),win32more.System.Ole.IOleClientSite_head,win32more.System.Com.StructuredStorage.IStorage_head,POINTER(c_void_p), use_last_error=False)(("OleCreateFromDataEx", windll["ole32"]), ((1, 'pSrcDataObj'),(1, 'riid'),(1, 'dwFlags'),(1, 'renderopt'),(1, 'cFormats'),(1, 'rgAdvf'),(1, 'rgFormatEtc'),(1, 'lpAdviseSink'),(1, 'rgdwConnection'),(1, 'pClientSite'),(1, 'pStg'),(1, 'ppvObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleCreateLinkFromData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head,POINTER(Guid),UInt32,POINTER(win32more.System.Com.FORMATETC_head),win32more.System.Ole.IOleClientSite_head,win32more.System.Com.StructuredStorage.IStorage_head,POINTER(c_void_p), use_last_error=False)(("OleCreateLinkFromData", windll["OLE32"]), ((1, 'pSrcDataObj'),(1, 'riid'),(1, 'renderopt'),(1, 'pFormatEtc'),(1, 'pClientSite'),(1, 'pStg'),(1, 'ppvObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleCreateLinkFromDataEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head,POINTER(Guid),UInt32,UInt32,UInt32,POINTER(UInt32),POINTER(win32more.System.Com.FORMATETC_head),win32more.System.Com.IAdviseSink_head,POINTER(UInt32),win32more.System.Ole.IOleClientSite_head,win32more.System.Com.StructuredStorage.IStorage_head,POINTER(c_void_p), use_last_error=False)(("OleCreateLinkFromDataEx", windll["ole32"]), ((1, 'pSrcDataObj'),(1, 'riid'),(1, 'dwFlags'),(1, 'renderopt'),(1, 'cFormats'),(1, 'rgAdvf'),(1, 'rgFormatEtc'),(1, 'lpAdviseSink'),(1, 'rgdwConnection'),(1, 'pClientSite'),(1, 'pStg'),(1, 'ppvObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleCreateStaticFromData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head,POINTER(Guid),UInt32,POINTER(win32more.System.Com.FORMATETC_head),win32more.System.Ole.IOleClientSite_head,win32more.System.Com.StructuredStorage.IStorage_head,POINTER(c_void_p), use_last_error=False)(("OleCreateStaticFromData", windll["OLE32"]), ((1, 'pSrcDataObj'),(1, 'iid'),(1, 'renderopt'),(1, 'pFormatEtc'),(1, 'pClientSite'),(1, 'pStg'),(1, 'ppvObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleCreateLink():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IMoniker_head,POINTER(Guid),UInt32,POINTER(win32more.System.Com.FORMATETC_head),win32more.System.Ole.IOleClientSite_head,win32more.System.Com.StructuredStorage.IStorage_head,POINTER(c_void_p), use_last_error=False)(("OleCreateLink", windll["ole32"]), ((1, 'pmkLinkSrc'),(1, 'riid'),(1, 'renderopt'),(1, 'lpFormatEtc'),(1, 'pClientSite'),(1, 'pStg'),(1, 'ppvObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleCreateLinkEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IMoniker_head,POINTER(Guid),UInt32,UInt32,UInt32,POINTER(UInt32),POINTER(win32more.System.Com.FORMATETC_head),win32more.System.Com.IAdviseSink_head,POINTER(UInt32),win32more.System.Ole.IOleClientSite_head,win32more.System.Com.StructuredStorage.IStorage_head,POINTER(c_void_p), use_last_error=False)(("OleCreateLinkEx", windll["ole32"]), ((1, 'pmkLinkSrc'),(1, 'riid'),(1, 'dwFlags'),(1, 'renderopt'),(1, 'cFormats'),(1, 'rgAdvf'),(1, 'rgFormatEtc'),(1, 'lpAdviseSink'),(1, 'rgdwConnection'),(1, 'pClientSite'),(1, 'pStg'),(1, 'ppvObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleCreateLinkToFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid),UInt32,POINTER(win32more.System.Com.FORMATETC_head),win32more.System.Ole.IOleClientSite_head,win32more.System.Com.StructuredStorage.IStorage_head,POINTER(c_void_p), use_last_error=False)(("OleCreateLinkToFile", windll["OLE32"]), ((1, 'lpszFileName'),(1, 'riid'),(1, 'renderopt'),(1, 'lpFormatEtc'),(1, 'pClientSite'),(1, 'pStg'),(1, 'ppvObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleCreateLinkToFileEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid),UInt32,UInt32,UInt32,POINTER(UInt32),POINTER(win32more.System.Com.FORMATETC_head),win32more.System.Com.IAdviseSink_head,POINTER(UInt32),win32more.System.Ole.IOleClientSite_head,win32more.System.Com.StructuredStorage.IStorage_head,POINTER(c_void_p), use_last_error=False)(("OleCreateLinkToFileEx", windll["ole32"]), ((1, 'lpszFileName'),(1, 'riid'),(1, 'dwFlags'),(1, 'renderopt'),(1, 'cFormats'),(1, 'rgAdvf'),(1, 'rgFormatEtc'),(1, 'lpAdviseSink'),(1, 'rgdwConnection'),(1, 'pClientSite'),(1, 'pStg'),(1, 'ppvObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleCreateFromFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.PWSTR,POINTER(Guid),UInt32,POINTER(win32more.System.Com.FORMATETC_head),win32more.System.Ole.IOleClientSite_head,win32more.System.Com.StructuredStorage.IStorage_head,POINTER(c_void_p), use_last_error=False)(("OleCreateFromFile", windll["OLE32"]), ((1, 'rclsid'),(1, 'lpszFileName'),(1, 'riid'),(1, 'renderopt'),(1, 'lpFormatEtc'),(1, 'pClientSite'),(1, 'pStg'),(1, 'ppvObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleCreateFromFileEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.PWSTR,POINTER(Guid),UInt32,UInt32,UInt32,POINTER(UInt32),POINTER(win32more.System.Com.FORMATETC_head),win32more.System.Com.IAdviseSink_head,POINTER(UInt32),win32more.System.Ole.IOleClientSite_head,win32more.System.Com.StructuredStorage.IStorage_head,POINTER(c_void_p), use_last_error=False)(("OleCreateFromFileEx", windll["ole32"]), ((1, 'rclsid'),(1, 'lpszFileName'),(1, 'riid'),(1, 'dwFlags'),(1, 'renderopt'),(1, 'cFormats'),(1, 'rgAdvf'),(1, 'rgFormatEtc'),(1, 'lpAdviseSink'),(1, 'rgdwConnection'),(1, 'pClientSite'),(1, 'pStg'),(1, 'ppvObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleLoad():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IStorage_head,POINTER(Guid),win32more.System.Ole.IOleClientSite_head,POINTER(c_void_p), use_last_error=False)(("OleLoad", windll["OLE32"]), ((1, 'pStg'),(1, 'riid'),(1, 'pClientSite'),(1, 'ppvObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleSave():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IPersistStorage_head,win32more.System.Com.StructuredStorage.IStorage_head,win32more.Foundation.BOOL, use_last_error=False)(("OleSave", windll["OLE32"]), ((1, 'pPS'),(1, 'pStg'),(1, 'fSameAsLoad'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleLoadFromStream():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("OleLoadFromStream", windll["OLE32"]), ((1, 'pStm'),(1, 'iidInterface'),(1, 'ppvObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleSaveToStream():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IPersistStream_head,win32more.System.Com.IStream_head, use_last_error=False)(("OleSaveToStream", windll["OLE32"]), ((1, 'pPStm'),(1, 'pStm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleSetContainedObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Foundation.BOOL, use_last_error=False)(("OleSetContainedObject", windll["OLE32"]), ((1, 'pUnknown'),(1, 'fContained'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleNoteObjectVisible():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Foundation.BOOL, use_last_error=False)(("OleNoteObjectVisible", windll["ole32"]), ((1, 'pUnknown'),(1, 'fVisible'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterDragDrop():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.System.Ole.IDropTarget_head, use_last_error=False)(("RegisterDragDrop", windll["OLE32"]), ((1, 'hwnd'),(1, 'pDropTarget'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RevokeDragDrop():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND, use_last_error=False)(("RevokeDragDrop", windll["OLE32"]), ((1, 'hwnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DoDragDrop():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head,win32more.System.Ole.IDropSource_head,UInt32,POINTER(UInt32), use_last_error=False)(("DoDragDrop", windll["OLE32"]), ((1, 'pDataObj'),(1, 'pDropSource'),(1, 'dwOKEffects'),(1, 'pdwEffect'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleSetClipboard():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head, use_last_error=False)(("OleSetClipboard", windll["OLE32"]), ((1, 'pDataObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleGetClipboard():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDataObject_head), use_last_error=False)(("OleGetClipboard", windll["OLE32"]), ((1, 'ppDataObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleGetClipboardWithEnterpriseInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IDataObject_head),POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("OleGetClipboardWithEnterpriseInfo", windll["ole32"]), ((1, 'dataObject'),(1, 'dataEnterpriseId'),(1, 'sourceDescription'),(1, 'targetDescription'),(1, 'dataDescription'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleFlushClipboard():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(("OleFlushClipboard", windll["OLE32"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleIsCurrentClipboard():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDataObject_head, use_last_error=False)(("OleIsCurrentClipboard", windll["OLE32"]), ((1, 'pDataObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleCreateMenuDescriptor():
    try:
        return WINFUNCTYPE(IntPtr,win32more.UI.WindowsAndMessaging.HMENU,POINTER(win32more.System.Ole.OleMenuGroupWidths_head), use_last_error=False)(("OleCreateMenuDescriptor", windll["OLE32"]), ((1, 'hmenuCombined'),(1, 'lpMenuWidths'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleSetMenuDescriptor():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr,win32more.Foundation.HWND,win32more.Foundation.HWND,win32more.System.Ole.IOleInPlaceFrame_head,win32more.System.Ole.IOleInPlaceActiveObject_head, use_last_error=False)(("OleSetMenuDescriptor", windll["OLE32"]), ((1, 'holemenu'),(1, 'hwndFrame'),(1, 'hwndActiveObject'),(1, 'lpFrame'),(1, 'lpActiveObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleDestroyMenuDescriptor():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,IntPtr, use_last_error=False)(("OleDestroyMenuDescriptor", windll["OLE32"]), ((1, 'holemenu'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleTranslateAccelerator():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Ole.IOleInPlaceFrame_head,POINTER(win32more.System.Ole.OIFI_head),POINTER(win32more.UI.WindowsAndMessaging.MSG_head), use_last_error=False)(("OleTranslateAccelerator", windll["OLE32"]), ((1, 'lpFrame'),(1, 'lpFrameInfo'),(1, 'lpmsg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleDuplicateData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,UInt16,UInt32, use_last_error=False)(("OleDuplicateData", windll["OLE32"]), ((1, 'hSrc'),(1, 'cfFormat'),(1, 'uiFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleDraw():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,UInt32,win32more.Graphics.Gdi.HDC,POINTER(win32more.Foundation.RECT_head), use_last_error=False)(("OleDraw", windll["OLE32"]), ((1, 'pUnknown'),(1, 'dwAspect'),(1, 'hdcDraw'),(1, 'lprcBounds'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleRun():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(("OleRun", windll["OLE32"]), ((1, 'pUnknown'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleIsRunning():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Ole.IOleObject_head, use_last_error=False)(("OleIsRunning", windll["OLE32"]), ((1, 'pObject'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleLockRunning():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Foundation.BOOL,win32more.Foundation.BOOL, use_last_error=False)(("OleLockRunning", windll["OLE32"]), ((1, 'pUnknown'),(1, 'fLock'),(1, 'fLastUnlockCloses'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReleaseStgMedium():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Com.STGMEDIUM_head), use_last_error=False)(("ReleaseStgMedium", windll["OLE32"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateOleAdviseHolder():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.IOleAdviseHolder_head), use_last_error=False)(("CreateOleAdviseHolder", windll["OLE32"]), ((1, 'ppOAHolder'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleCreateDefaultHandler():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("OleCreateDefaultHandler", windll["ole32"]), ((1, 'clsid'),(1, 'pUnkOuter'),(1, 'riid'),(1, 'lplpObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleCreateEmbeddingHelper():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head,UInt32,win32more.System.Com.IClassFactory_head,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("OleCreateEmbeddingHelper", windll["OLE32"]), ((1, 'clsid'),(1, 'pUnkOuter'),(1, 'flags'),(1, 'pCF'),(1, 'riid'),(1, 'lplpObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsAccelerator():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.UI.WindowsAndMessaging.HACCEL,Int32,POINTER(win32more.UI.WindowsAndMessaging.MSG_head),POINTER(UInt16), use_last_error=False)(("IsAccelerator", windll["OLE32"]), ((1, 'hAccel'),(1, 'cAccelEntries'),(1, 'lpMsg'),(1, 'lpwCmd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleGetIconOfFile():
    try:
        return WINFUNCTYPE(IntPtr,win32more.Foundation.PWSTR,win32more.Foundation.BOOL, use_last_error=False)(("OleGetIconOfFile", windll["ole32"]), ((1, 'lpszPath'),(1, 'fUseFileAsLabel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleGetIconOfClass():
    try:
        return WINFUNCTYPE(IntPtr,POINTER(Guid),win32more.Foundation.PWSTR,win32more.Foundation.BOOL, use_last_error=False)(("OleGetIconOfClass", windll["OLE32"]), ((1, 'rclsid'),(1, 'lpszLabel'),(1, 'fUseTypeAsLabel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleMetafilePictFromIconAndLabel():
    try:
        return WINFUNCTYPE(IntPtr,win32more.UI.WindowsAndMessaging.HICON,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=True)(("OleMetafilePictFromIconAndLabel", windll["ole32"]), ((1, 'hIcon'),(1, 'lpszLabel'),(1, 'lpszSourceFile'),(1, 'iIconIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleRegGetUserType():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("OleRegGetUserType", windll["OLE32"]), ((1, 'clsid'),(1, 'dwFormOfType'),(1, 'pszUserType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleRegGetMiscStatus():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(UInt32), use_last_error=False)(("OleRegGetMiscStatus", windll["OLE32"]), ((1, 'clsid'),(1, 'dwAspect'),(1, 'pdwStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleRegEnumFormatEtc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,POINTER(win32more.System.Com.IEnumFORMATETC_head), use_last_error=False)(("OleRegEnumFormatEtc", windll["ole32"]), ((1, 'clsid'),(1, 'dwDirection'),(1, 'ppenum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleRegEnumVerbs():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.System.Ole.IEnumOLEVERB_head), use_last_error=False)(("OleRegEnumVerbs", windll["OLE32"]), ((1, 'clsid'),(1, 'ppenum'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleDoAutoConvert():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.StructuredStorage.IStorage_head,POINTER(Guid), use_last_error=False)(("OleDoAutoConvert", windll["ole32"]), ((1, 'pStg'),(1, 'pClsidNew'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleGetAutoConvert():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid), use_last_error=False)(("OleGetAutoConvert", windll["OLE32"]), ((1, 'clsidOld'),(1, 'pClsidNew'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleSetAutoConvert():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(Guid), use_last_error=False)(("OleSetAutoConvert", windll["ole32"]), ((1, 'clsidOld'),(1, 'clsidNew'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HRGN_UserSize():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.Graphics.Gdi.HRGN), use_last_error=False)(("HRGN_UserSize", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HRGN_UserMarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Graphics.Gdi.HRGN), use_last_error=False)(("HRGN_UserMarshal", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HRGN_UserUnmarshal():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),POINTER(Byte),POINTER(win32more.Graphics.Gdi.HRGN), use_last_error=False)(("HRGN_UserUnmarshal", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HRGN_UserFree():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.Graphics.Gdi.HRGN), use_last_error=False)(("HRGN_UserFree", windll["OLE32"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HRGN_UserSize64():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),UInt32,POINTER(win32more.Graphics.Gdi.HRGN), use_last_error=False)(("HRGN_UserSize64", windll["api-ms-win-core-marshal-l1-1-0"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HRGN_UserMarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),c_char_p_no,POINTER(win32more.Graphics.Gdi.HRGN), use_last_error=False)(("HRGN_UserMarshal64", windll["api-ms-win-core-marshal-l1-1-0"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HRGN_UserUnmarshal64():
    try:
        return WINFUNCTYPE(c_char_p_no,POINTER(UInt32),POINTER(Byte),POINTER(win32more.Graphics.Gdi.HRGN), use_last_error=False)(("HRGN_UserUnmarshal64", windll["api-ms-win-core-marshal-l1-1-0"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HRGN_UserFree64():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.Graphics.Gdi.HRGN), use_last_error=False)(("HRGN_UserFree64", windll["api-ms-win-core-marshal-l1-1-0"]), ((1, 'param0'),(1, 'param1'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleCreatePropertyFrame():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,UInt32,UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.System.Com.IUnknown_head),UInt32,POINTER(Guid),UInt32,UInt32,c_void_p, use_last_error=False)(("OleCreatePropertyFrame", windll["OLEAUT32"]), ((1, 'hwndOwner'),(1, 'x'),(1, 'y'),(1, 'lpszCaption'),(1, 'cObjects'),(1, 'ppUnk'),(1, 'cPages'),(1, 'pPageClsID'),(1, 'lcid'),(1, 'dwReserved'),(1, 'pvReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleCreatePropertyFrameIndirect():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.OCPFIPARAMS_head), use_last_error=False)(("OleCreatePropertyFrameIndirect", windll["OLEAUT32"]), ((1, 'lpParams'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleTranslateColor():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Graphics.Gdi.HPALETTE,POINTER(UInt32), use_last_error=False)(("OleTranslateColor", windll["OLEAUT32"]), ((1, 'clr'),(1, 'hpal'),(1, 'lpcolorref'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleCreateFontIndirect():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.FONTDESC_head),POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("OleCreateFontIndirect", windll["OLEAUT32"]), ((1, 'lpFontDesc'),(1, 'riid'),(1, 'lplpvObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleCreatePictureIndirect():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Ole.PICTDESC_head),POINTER(Guid),win32more.Foundation.BOOL,POINTER(c_void_p), use_last_error=False)(("OleCreatePictureIndirect", windll["OLEAUT32"]), ((1, 'lpPictDesc'),(1, 'riid'),(1, 'fOwn'),(1, 'lplpvObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleLoadPicture():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,Int32,win32more.Foundation.BOOL,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("OleLoadPicture", windll["OLEAUT32"]), ((1, 'lpstream'),(1, 'lSize'),(1, 'fRunmode'),(1, 'riid'),(1, 'lplpvObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleLoadPictureEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,Int32,win32more.Foundation.BOOL,POINTER(Guid),UInt32,UInt32,UInt32,POINTER(c_void_p), use_last_error=False)(("OleLoadPictureEx", windll["OLEAUT32"]), ((1, 'lpstream'),(1, 'lSize'),(1, 'fRunmode'),(1, 'riid'),(1, 'xSizeDesired'),(1, 'ySizeDesired'),(1, 'dwFlags'),(1, 'lplpvObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleLoadPicturePath():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.IUnknown_head,UInt32,UInt32,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("OleLoadPicturePath", windll["OLEAUT32"]), ((1, 'szURLorPath'),(1, 'punkCaller'),(1, 'dwReserved'),(1, 'clrReserved'),(1, 'riid'),(1, 'ppvRet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleLoadPictureFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(("OleLoadPictureFile", windll["OLEAUT32"]), ((1, 'varFileName'),(1, 'lplpdispPicture'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleLoadPictureFileEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.VARIANT,UInt32,UInt32,UInt32,POINTER(win32more.System.Com.IDispatch_head), use_last_error=False)(("OleLoadPictureFileEx", windll["OLEAUT32"]), ((1, 'varFileName'),(1, 'xSizeDesired'),(1, 'ySizeDesired'),(1, 'dwFlags'),(1, 'lplpdispPicture'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleSavePictureFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IDispatch_head,win32more.Foundation.BSTR, use_last_error=False)(("OleSavePictureFile", windll["OLEAUT32"]), ((1, 'lpdispPicture'),(1, 'bstrFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleIconToCursor():
    try:
        return WINFUNCTYPE(win32more.UI.WindowsAndMessaging.HCURSOR,win32more.Foundation.HINSTANCE,win32more.UI.WindowsAndMessaging.HICON, use_last_error=False)(("OleIconToCursor", windll["OLEAUT32"]), ((1, 'hinstExe'),(1, 'hIcon'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleUIAddVerbMenuW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Ole.IOleObject_head,win32more.Foundation.PWSTR,win32more.UI.WindowsAndMessaging.HMENU,UInt32,UInt32,UInt32,win32more.Foundation.BOOL,UInt32,POINTER(win32more.UI.WindowsAndMessaging.HMENU), use_last_error=False)(("OleUIAddVerbMenuW", windll["oledlg"]), ((1, 'lpOleObj'),(1, 'lpszShortType'),(1, 'hMenu'),(1, 'uPos'),(1, 'uIDVerbMin'),(1, 'uIDVerbMax'),(1, 'bAddConvert'),(1, 'idConvert'),(1, 'lphMenu'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleUIAddVerbMenu():
    return win32more.System.Ole.OleUIAddVerbMenuW
def _define_OleUIAddVerbMenuA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Ole.IOleObject_head,win32more.Foundation.PSTR,win32more.UI.WindowsAndMessaging.HMENU,UInt32,UInt32,UInt32,win32more.Foundation.BOOL,UInt32,POINTER(win32more.UI.WindowsAndMessaging.HMENU), use_last_error=False)(("OleUIAddVerbMenuA", windll["oledlg"]), ((1, 'lpOleObj'),(1, 'lpszShortType'),(1, 'hMenu'),(1, 'uPos'),(1, 'uIDVerbMin'),(1, 'uIDVerbMax'),(1, 'bAddConvert'),(1, 'idConvert'),(1, 'lphMenu'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleUIInsertObjectW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Ole.OLEUIINSERTOBJECTW_head), use_last_error=False)(("OleUIInsertObjectW", windll["oledlg"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleUIInsertObject():
    return win32more.System.Ole.OleUIInsertObjectW
def _define_OleUIInsertObjectA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Ole.OLEUIINSERTOBJECTA_head), use_last_error=False)(("OleUIInsertObjectA", windll["oledlg"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleUIPasteSpecialW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Ole.OLEUIPASTESPECIALW_head), use_last_error=False)(("OleUIPasteSpecialW", windll["oledlg"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleUIPasteSpecial():
    return win32more.System.Ole.OleUIPasteSpecialW
def _define_OleUIPasteSpecialA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Ole.OLEUIPASTESPECIALA_head), use_last_error=False)(("OleUIPasteSpecialA", windll["oledlg"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleUIEditLinksW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Ole.OLEUIEDITLINKSW_head), use_last_error=False)(("OleUIEditLinksW", windll["oledlg"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleUIEditLinks():
    return win32more.System.Ole.OleUIEditLinksW
def _define_OleUIEditLinksA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Ole.OLEUIEDITLINKSA_head), use_last_error=False)(("OleUIEditLinksA", windll["oledlg"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleUIChangeIconW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Ole.OLEUICHANGEICONW_head), use_last_error=False)(("OleUIChangeIconW", windll["oledlg"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleUIChangeIcon():
    return win32more.System.Ole.OleUIChangeIconW
def _define_OleUIChangeIconA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Ole.OLEUICHANGEICONA_head), use_last_error=False)(("OleUIChangeIconA", windll["oledlg"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleUIConvertW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Ole.OLEUICONVERTW_head), use_last_error=False)(("OleUIConvertW", windll["oledlg"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleUIConvert():
    return win32more.System.Ole.OleUIConvertW
def _define_OleUIConvertA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Ole.OLEUICONVERTA_head), use_last_error=False)(("OleUIConvertA", windll["oledlg"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleUICanConvertOrActivateAs():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(Guid),win32more.Foundation.BOOL,UInt16, use_last_error=False)(("OleUICanConvertOrActivateAs", windll["oledlg"]), ((1, 'rClsid'),(1, 'fIsLinkedObject'),(1, 'wFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleUIBusyW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Ole.OLEUIBUSYW_head), use_last_error=False)(("OleUIBusyW", windll["oledlg"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleUIBusy():
    return win32more.System.Ole.OleUIBusyW
def _define_OleUIBusyA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Ole.OLEUIBUSYA_head), use_last_error=False)(("OleUIBusyA", windll["oledlg"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleUIChangeSourceW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Ole.OLEUICHANGESOURCEW_head), use_last_error=False)(("OleUIChangeSourceW", windll["oledlg"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleUIChangeSource():
    return win32more.System.Ole.OleUIChangeSourceW
def _define_OleUIChangeSourceA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Ole.OLEUICHANGESOURCEA_head), use_last_error=False)(("OleUIChangeSourceA", windll["oledlg"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleUIObjectPropertiesW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Ole.OLEUIOBJECTPROPSW_head), use_last_error=False)(("OleUIObjectPropertiesW", windll["oledlg"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleUIObjectProperties():
    return win32more.System.Ole.OleUIObjectPropertiesW
def _define_OleUIObjectPropertiesA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.System.Ole.OLEUIOBJECTPROPSA_head), use_last_error=False)(("OleUIObjectPropertiesA", windll["oledlg"]), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleUIPromptUserW():
    try:
        return WINFUNCTYPE(Int32,Int32,win32more.Foundation.HWND, use_last_error=False)(("OleUIPromptUserW", windll["oledlg"]), ((1, 'nTemplate'),(1, 'hwndParent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleUIPromptUser():
    return win32more.System.Ole.OleUIPromptUserW
def _define_OleUIPromptUserA():
    try:
        return WINFUNCTYPE(Int32,Int32,win32more.Foundation.HWND, use_last_error=False)(("OleUIPromptUserA", windll["oledlg"]), ((1, 'nTemplate'),(1, 'hwndParent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleUIUpdateLinksW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Ole.IOleUILinkContainerW_head,win32more.Foundation.HWND,win32more.Foundation.PWSTR,Int32, use_last_error=False)(("OleUIUpdateLinksW", windll["oledlg"]), ((1, 'lpOleUILinkCntr'),(1, 'hwndParent'),(1, 'lpszTitle'),(1, 'cLinks'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OleUIUpdateLinks():
    return win32more.System.Ole.OleUIUpdateLinksW
def _define_OleUIUpdateLinksA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Ole.IOleUILinkContainerA_head,win32more.Foundation.HWND,win32more.Foundation.PSTR,Int32, use_last_error=False)(("OleUIUpdateLinksA", windll["oledlg"]), ((1, 'lpOleUILinkCntr'),(1, 'hwndParent'),(1, 'lpszTitle'),(1, 'cLinks'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "CTL_E_ILLEGALFUNCTIONCALL",
    "CONNECT_E_FIRST",
    "SELFREG_E_FIRST",
    "PERPROP_E_FIRST",
    "OLECMDERR_E_FIRST",
    "OLECMDERR_E_DISABLED",
    "OLECMDERR_E_NOHELP",
    "OLECMDERR_E_CANCELED",
    "OLECMDERR_E_UNKNOWNGROUP",
    "CONNECT_E_NOCONNECTION",
    "CONNECT_E_ADVISELIMIT",
    "CONNECT_E_CANNOTCONNECT",
    "CONNECT_E_OVERRIDDEN",
    "SELFREG_E_TYPELIB",
    "SELFREG_E_CLASS",
    "PERPROP_E_NOPAGEAVAILABLE",
    "CLSID_CFontPropPage",
    "CLSID_CColorPropPage",
    "CLSID_CPicturePropPage",
    "CLSID_PersistPropset",
    "CLSID_ConvertVBX",
    "CLSID_StdFont",
    "CLSID_StdPicture",
    "GUID_HIMETRIC",
    "GUID_COLOR",
    "GUID_XPOSPIXEL",
    "GUID_YPOSPIXEL",
    "GUID_XSIZEPIXEL",
    "GUID_YSIZEPIXEL",
    "GUID_XPOS",
    "GUID_YPOS",
    "GUID_XSIZE",
    "GUID_YSIZE",
    "GUID_TRISTATE",
    "GUID_OPTIONVALUEEXCLUSIVE",
    "GUID_CHECKVALUEEXCLUSIVE",
    "GUID_FONTNAME",
    "GUID_FONTSIZE",
    "GUID_FONTBOLD",
    "GUID_FONTITALIC",
    "GUID_FONTUNDERSCORE",
    "GUID_FONTSTRIKETHROUGH",
    "GUID_HANDLE",
    "PICTYPE_UNINITIALIZED",
    "PICTYPE_NONE",
    "PICTYPE_BITMAP",
    "PICTYPE_METAFILE",
    "PICTYPE_ICON",
    "PICTYPE_ENHMETAFILE",
    "CONNECT_E_LAST",
    "CONNECT_S_FIRST",
    "CONNECT_S_LAST",
    "SELFREG_E_LAST",
    "SELFREG_S_FIRST",
    "SELFREG_S_LAST",
    "PERPROP_E_LAST",
    "PERPROP_S_FIRST",
    "PERPROP_S_LAST",
    "OLEIVERB_PROPERTIES",
    "VT_STREAMED_PROPSET",
    "VT_STORED_PROPSET",
    "VT_BLOB_PROPSET",
    "VT_VERBOSE_ENUM",
    "OCM__BASE",
    "LP_DEFAULT",
    "LP_MONOCHROME",
    "LP_VGACOLOR",
    "LP_COLOR",
    "DISPID_AUTOSIZE",
    "DISPID_BACKCOLOR",
    "DISPID_BACKSTYLE",
    "DISPID_BORDERCOLOR",
    "DISPID_BORDERSTYLE",
    "DISPID_BORDERWIDTH",
    "DISPID_DRAWMODE",
    "DISPID_DRAWSTYLE",
    "DISPID_DRAWWIDTH",
    "DISPID_FILLCOLOR",
    "DISPID_FILLSTYLE",
    "DISPID_FONT",
    "DISPID_FORECOLOR",
    "DISPID_ENABLED",
    "DISPID_HWND",
    "DISPID_TABSTOP",
    "DISPID_TEXT",
    "DISPID_CAPTION",
    "DISPID_BORDERVISIBLE",
    "DISPID_APPEARANCE",
    "DISPID_MOUSEPOINTER",
    "DISPID_MOUSEICON",
    "DISPID_PICTURE",
    "DISPID_VALID",
    "DISPID_READYSTATE",
    "DISPID_LISTINDEX",
    "DISPID_SELECTED",
    "DISPID_LIST",
    "DISPID_COLUMN",
    "DISPID_LISTCOUNT",
    "DISPID_MULTISELECT",
    "DISPID_MAXLENGTH",
    "DISPID_PASSWORDCHAR",
    "DISPID_SCROLLBARS",
    "DISPID_WORDWRAP",
    "DISPID_MULTILINE",
    "DISPID_NUMBEROFROWS",
    "DISPID_NUMBEROFCOLUMNS",
    "DISPID_DISPLAYSTYLE",
    "DISPID_GROUPNAME",
    "DISPID_IMEMODE",
    "DISPID_ACCELERATOR",
    "DISPID_ENTERKEYBEHAVIOR",
    "DISPID_TABKEYBEHAVIOR",
    "DISPID_SELTEXT",
    "DISPID_SELSTART",
    "DISPID_SELLENGTH",
    "DISPID_REFRESH",
    "DISPID_DOCLICK",
    "DISPID_ABOUTBOX",
    "DISPID_ADDITEM",
    "DISPID_CLEAR",
    "DISPID_REMOVEITEM",
    "DISPID_CLICK",
    "DISPID_DBLCLICK",
    "DISPID_KEYDOWN",
    "DISPID_KEYPRESS",
    "DISPID_KEYUP",
    "DISPID_MOUSEDOWN",
    "DISPID_MOUSEMOVE",
    "DISPID_MOUSEUP",
    "DISPID_ERROREVENT",
    "DISPID_READYSTATECHANGE",
    "DISPID_CLICK_VALUE",
    "DISPID_RIGHTTOLEFT",
    "DISPID_TOPTOBOTTOM",
    "DISPID_THIS",
    "DISPID_AMBIENT_BACKCOLOR",
    "DISPID_AMBIENT_DISPLAYNAME",
    "DISPID_AMBIENT_FONT",
    "DISPID_AMBIENT_FORECOLOR",
    "DISPID_AMBIENT_LOCALEID",
    "DISPID_AMBIENT_MESSAGEREFLECT",
    "DISPID_AMBIENT_SCALEUNITS",
    "DISPID_AMBIENT_TEXTALIGN",
    "DISPID_AMBIENT_USERMODE",
    "DISPID_AMBIENT_UIDEAD",
    "DISPID_AMBIENT_SHOWGRABHANDLES",
    "DISPID_AMBIENT_SHOWHATCHING",
    "DISPID_AMBIENT_DISPLAYASDEFAULT",
    "DISPID_AMBIENT_SUPPORTSMNEMONICS",
    "DISPID_AMBIENT_AUTOCLIP",
    "DISPID_AMBIENT_APPEARANCE",
    "DISPID_AMBIENT_CODEPAGE",
    "DISPID_AMBIENT_PALETTE",
    "DISPID_AMBIENT_CHARSET",
    "DISPID_AMBIENT_TRANSFERPRIORITY",
    "DISPID_AMBIENT_RIGHTTOLEFT",
    "DISPID_AMBIENT_TOPTOBOTTOM",
    "DISPID_Name",
    "DISPID_Delete",
    "DISPID_Object",
    "DISPID_Parent",
    "DISPID_FONT_NAME",
    "DISPID_FONT_SIZE",
    "DISPID_FONT_BOLD",
    "DISPID_FONT_ITALIC",
    "DISPID_FONT_UNDER",
    "DISPID_FONT_STRIKE",
    "DISPID_FONT_WEIGHT",
    "DISPID_FONT_CHARSET",
    "DISPID_FONT_CHANGED",
    "DISPID_PICT_HANDLE",
    "DISPID_PICT_HPAL",
    "DISPID_PICT_TYPE",
    "DISPID_PICT_WIDTH",
    "DISPID_PICT_HEIGHT",
    "DISPID_PICT_RENDER",
    "GC_WCH_SIBLING",
    "TIFLAGS_EXTENDDISPATCHONLY",
    "OLECMDERR_E_NOTSUPPORTED",
    "MSOCMDERR_E_FIRST",
    "MSOCMDERR_E_NOTSUPPORTED",
    "MSOCMDERR_E_DISABLED",
    "MSOCMDERR_E_NOHELP",
    "MSOCMDERR_E_CANCELED",
    "MSOCMDERR_E_UNKNOWNGROUP",
    "OLECMD_TASKDLGID_ONBEFOREUNLOAD",
    "OLECMDARGINDEX_SHOWPAGEACTIONMENU_HWND",
    "OLECMDARGINDEX_SHOWPAGEACTIONMENU_X",
    "OLECMDARGINDEX_SHOWPAGEACTIONMENU_Y",
    "OLECMDARGINDEX_ACTIVEXINSTALL_PUBLISHER",
    "OLECMDARGINDEX_ACTIVEXINSTALL_DISPLAYNAME",
    "OLECMDARGINDEX_ACTIVEXINSTALL_CLSID",
    "OLECMDARGINDEX_ACTIVEXINSTALL_INSTALLSCOPE",
    "OLECMDARGINDEX_ACTIVEXINSTALL_SOURCEURL",
    "INSTALL_SCOPE_INVALID",
    "INSTALL_SCOPE_MACHINE",
    "INSTALL_SCOPE_USER",
    "MK_ALT",
    "DROPEFFECT_NONE",
    "DROPEFFECT_COPY",
    "DROPEFFECT_MOVE",
    "DROPEFFECT_LINK",
    "DROPEFFECT_SCROLL",
    "DD_DEFSCROLLINSET",
    "DD_DEFSCROLLDELAY",
    "DD_DEFSCROLLINTERVAL",
    "DD_DEFDRAGDELAY",
    "DD_DEFDRAGMINDIST",
    "OT_LINK",
    "OT_EMBEDDED",
    "OT_STATIC",
    "OLEVERB_PRIMARY",
    "OF_SET",
    "OF_GET",
    "OF_HANDLER",
    "WIN32",
    "OLEIVERB_PRIMARY",
    "OLEIVERB_SHOW",
    "OLEIVERB_OPEN",
    "OLEIVERB_HIDE",
    "OLEIVERB_UIACTIVATE",
    "OLEIVERB_INPLACEACTIVATE",
    "OLEIVERB_DISCARDUNDOSTATE",
    "EMBDHLP_INPROC_HANDLER",
    "EMBDHLP_INPROC_SERVER",
    "EMBDHLP_CREATENOW",
    "EMBDHLP_DELAYCREATE",
    "OLECREATE_LEAVERUNNING",
    "IDC_OLEUIHELP",
    "IDC_IO_CREATENEW",
    "IDC_IO_CREATEFROMFILE",
    "IDC_IO_LINKFILE",
    "IDC_IO_OBJECTTYPELIST",
    "IDC_IO_DISPLAYASICON",
    "IDC_IO_CHANGEICON",
    "IDC_IO_FILE",
    "IDC_IO_FILEDISPLAY",
    "IDC_IO_RESULTIMAGE",
    "IDC_IO_RESULTTEXT",
    "IDC_IO_ICONDISPLAY",
    "IDC_IO_OBJECTTYPETEXT",
    "IDC_IO_FILETEXT",
    "IDC_IO_FILETYPE",
    "IDC_IO_INSERTCONTROL",
    "IDC_IO_ADDCONTROL",
    "IDC_IO_CONTROLTYPELIST",
    "IDC_PS_PASTE",
    "IDC_PS_PASTELINK",
    "IDC_PS_SOURCETEXT",
    "IDC_PS_PASTELIST",
    "IDC_PS_PASTELINKLIST",
    "IDC_PS_DISPLAYLIST",
    "IDC_PS_DISPLAYASICON",
    "IDC_PS_ICONDISPLAY",
    "IDC_PS_CHANGEICON",
    "IDC_PS_RESULTIMAGE",
    "IDC_PS_RESULTTEXT",
    "IDC_CI_GROUP",
    "IDC_CI_CURRENT",
    "IDC_CI_CURRENTICON",
    "IDC_CI_DEFAULT",
    "IDC_CI_DEFAULTICON",
    "IDC_CI_FROMFILE",
    "IDC_CI_FROMFILEEDIT",
    "IDC_CI_ICONLIST",
    "IDC_CI_LABEL",
    "IDC_CI_LABELEDIT",
    "IDC_CI_BROWSE",
    "IDC_CI_ICONDISPLAY",
    "IDC_CV_OBJECTTYPE",
    "IDC_CV_DISPLAYASICON",
    "IDC_CV_CHANGEICON",
    "IDC_CV_ACTIVATELIST",
    "IDC_CV_CONVERTTO",
    "IDC_CV_ACTIVATEAS",
    "IDC_CV_RESULTTEXT",
    "IDC_CV_CONVERTLIST",
    "IDC_CV_ICONDISPLAY",
    "IDC_EL_CHANGESOURCE",
    "IDC_EL_AUTOMATIC",
    "IDC_EL_CANCELLINK",
    "IDC_EL_UPDATENOW",
    "IDC_EL_OPENSOURCE",
    "IDC_EL_MANUAL",
    "IDC_EL_LINKSOURCE",
    "IDC_EL_LINKTYPE",
    "IDC_EL_LINKSLISTBOX",
    "IDC_EL_COL1",
    "IDC_EL_COL2",
    "IDC_EL_COL3",
    "IDC_BZ_RETRY",
    "IDC_BZ_ICON",
    "IDC_BZ_MESSAGE1",
    "IDC_BZ_SWITCHTO",
    "IDC_UL_METER",
    "IDC_UL_STOP",
    "IDC_UL_PERCENT",
    "IDC_UL_PROGRESS",
    "IDC_PU_LINKS",
    "IDC_PU_TEXT",
    "IDC_PU_CONVERT",
    "IDC_PU_ICON",
    "IDC_GP_OBJECTNAME",
    "IDC_GP_OBJECTTYPE",
    "IDC_GP_OBJECTSIZE",
    "IDC_GP_CONVERT",
    "IDC_GP_OBJECTICON",
    "IDC_GP_OBJECTLOCATION",
    "IDC_VP_PERCENT",
    "IDC_VP_CHANGEICON",
    "IDC_VP_EDITABLE",
    "IDC_VP_ASICON",
    "IDC_VP_RELATIVE",
    "IDC_VP_SPIN",
    "IDC_VP_SCALETXT",
    "IDC_VP_ICONDISPLAY",
    "IDC_VP_RESULTIMAGE",
    "IDC_LP_OPENSOURCE",
    "IDC_LP_UPDATENOW",
    "IDC_LP_BREAKLINK",
    "IDC_LP_LINKSOURCE",
    "IDC_LP_CHANGESOURCE",
    "IDC_LP_AUTOMATIC",
    "IDC_LP_MANUAL",
    "IDC_LP_DATE",
    "IDC_LP_TIME",
    "IDD_INSERTOBJECT",
    "IDD_CHANGEICON",
    "IDD_CONVERT",
    "IDD_PASTESPECIAL",
    "IDD_EDITLINKS",
    "IDD_BUSY",
    "IDD_UPDATELINKS",
    "IDD_CHANGESOURCE",
    "IDD_INSERTFILEBROWSE",
    "IDD_CHANGEICONBROWSE",
    "IDD_CONVERTONLY",
    "IDD_CHANGESOURCE4",
    "IDD_GNRLPROPS",
    "IDD_VIEWPROPS",
    "IDD_LINKPROPS",
    "IDD_CONVERT4",
    "IDD_CONVERTONLY4",
    "IDD_EDITLINKS4",
    "IDD_GNRLPROPS4",
    "IDD_LINKPROPS4",
    "IDD_PASTESPECIAL4",
    "IDD_CANNOTUPDATELINK",
    "IDD_LINKSOURCEUNAVAILABLE",
    "IDD_SERVERNOTFOUND",
    "IDD_OUTOFMEMORY",
    "IDD_SERVERNOTREGW",
    "IDD_LINKTYPECHANGEDW",
    "IDD_SERVERNOTREGA",
    "IDD_LINKTYPECHANGEDA",
    "IDD_SERVERNOTREG",
    "IDD_LINKTYPECHANGED",
    "ID_BROWSE_CHANGEICON",
    "ID_BROWSE_INSERTFILE",
    "ID_BROWSE_ADDCONTROL",
    "ID_BROWSE_CHANGESOURCE",
    "OLEUI_FALSE",
    "OLEUI_SUCCESS",
    "OLEUI_OK",
    "OLEUI_CANCEL",
    "OLEUI_ERR_STANDARDMIN",
    "OLEUI_ERR_OLEMEMALLOC",
    "OLEUI_ERR_STRUCTURENULL",
    "OLEUI_ERR_STRUCTUREINVALID",
    "OLEUI_ERR_CBSTRUCTINCORRECT",
    "OLEUI_ERR_HWNDOWNERINVALID",
    "OLEUI_ERR_LPSZCAPTIONINVALID",
    "OLEUI_ERR_LPFNHOOKINVALID",
    "OLEUI_ERR_HINSTANCEINVALID",
    "OLEUI_ERR_LPSZTEMPLATEINVALID",
    "OLEUI_ERR_HRESOURCEINVALID",
    "OLEUI_ERR_FINDTEMPLATEFAILURE",
    "OLEUI_ERR_LOADTEMPLATEFAILURE",
    "OLEUI_ERR_DIALOGFAILURE",
    "OLEUI_ERR_LOCALMEMALLOC",
    "OLEUI_ERR_GLOBALMEMALLOC",
    "OLEUI_ERR_LOADSTRING",
    "OLEUI_ERR_STANDARDMAX",
    "IOF_SHOWHELP",
    "IOF_SELECTCREATENEW",
    "IOF_SELECTCREATEFROMFILE",
    "IOF_CHECKLINK",
    "IOF_CHECKDISPLAYASICON",
    "IOF_CREATENEWOBJECT",
    "IOF_CREATEFILEOBJECT",
    "IOF_CREATELINKOBJECT",
    "IOF_DISABLELINK",
    "IOF_VERIFYSERVERSEXIST",
    "IOF_DISABLEDISPLAYASICON",
    "IOF_HIDECHANGEICON",
    "IOF_SHOWINSERTCONTROL",
    "IOF_SELECTCREATECONTROL",
    "OLEUI_IOERR_LPSZFILEINVALID",
    "OLEUI_IOERR_LPSZLABELINVALID",
    "OLEUI_IOERR_HICONINVALID",
    "OLEUI_IOERR_LPFORMATETCINVALID",
    "OLEUI_IOERR_PPVOBJINVALID",
    "OLEUI_IOERR_LPIOLECLIENTSITEINVALID",
    "OLEUI_IOERR_LPISTORAGEINVALID",
    "OLEUI_IOERR_SCODEHASERROR",
    "OLEUI_IOERR_LPCLSIDEXCLUDEINVALID",
    "OLEUI_IOERR_CCHFILEINVALID",
    "PS_MAXLINKTYPES",
    "PSF_SHOWHELP",
    "PSF_SELECTPASTE",
    "PSF_SELECTPASTELINK",
    "PSF_CHECKDISPLAYASICON",
    "PSF_DISABLEDISPLAYASICON",
    "PSF_HIDECHANGEICON",
    "PSF_STAYONCLIPBOARDCHANGE",
    "PSF_NOREFRESHDATAOBJECT",
    "OLEUI_IOERR_SRCDATAOBJECTINVALID",
    "OLEUI_IOERR_ARRPASTEENTRIESINVALID",
    "OLEUI_IOERR_ARRLINKTYPESINVALID",
    "OLEUI_PSERR_CLIPBOARDCHANGED",
    "OLEUI_PSERR_GETCLIPBOARDFAILED",
    "OLEUI_ELERR_LINKCNTRNULL",
    "OLEUI_ELERR_LINKCNTRINVALID",
    "ELF_SHOWHELP",
    "ELF_DISABLEUPDATENOW",
    "ELF_DISABLEOPENSOURCE",
    "ELF_DISABLECHANGESOURCE",
    "ELF_DISABLECANCELLINK",
    "CIF_SHOWHELP",
    "CIF_SELECTCURRENT",
    "CIF_SELECTDEFAULT",
    "CIF_SELECTFROMFILE",
    "CIF_USEICONEXE",
    "OLEUI_CIERR_MUSTHAVECLSID",
    "OLEUI_CIERR_MUSTHAVECURRENTMETAFILE",
    "OLEUI_CIERR_SZICONEXEINVALID",
    "CF_SHOWHELPBUTTON",
    "CF_SETCONVERTDEFAULT",
    "CF_SETACTIVATEDEFAULT",
    "CF_SELECTCONVERTTO",
    "CF_SELECTACTIVATEAS",
    "CF_DISABLEDISPLAYASICON",
    "CF_DISABLEACTIVATEAS",
    "CF_HIDECHANGEICON",
    "CF_CONVERTONLY",
    "OLEUI_CTERR_CLASSIDINVALID",
    "OLEUI_CTERR_DVASPECTINVALID",
    "OLEUI_CTERR_CBFORMATINVALID",
    "OLEUI_CTERR_HMETAPICTINVALID",
    "OLEUI_CTERR_STRINGINVALID",
    "BZ_DISABLECANCELBUTTON",
    "BZ_DISABLESWITCHTOBUTTON",
    "BZ_DISABLERETRYBUTTON",
    "BZ_NOTRESPONDINGDIALOG",
    "OLEUI_BZERR_HTASKINVALID",
    "OLEUI_BZ_SWITCHTOSELECTED",
    "OLEUI_BZ_RETRYSELECTED",
    "OLEUI_BZ_CALLUNBLOCKED",
    "CSF_SHOWHELP",
    "CSF_VALIDSOURCE",
    "CSF_ONLYGETSOURCE",
    "CSF_EXPLORER",
    "OLEUI_CSERR_LINKCNTRNULL",
    "OLEUI_CSERR_LINKCNTRINVALID",
    "OLEUI_CSERR_FROMNOTNULL",
    "OLEUI_CSERR_TONOTNULL",
    "OLEUI_CSERR_SOURCENULL",
    "OLEUI_CSERR_SOURCEINVALID",
    "OLEUI_CSERR_SOURCEPARSERROR",
    "OLEUI_CSERR_SOURCEPARSEERROR",
    "VPF_SELECTRELATIVE",
    "VPF_DISABLERELATIVE",
    "VPF_DISABLESCALE",
    "OPF_OBJECTISLINK",
    "OPF_NOFILLDEFAULT",
    "OPF_SHOWHELP",
    "OPF_DISABLECONVERT",
    "OLEUI_OPERR_SUBPROPNULL",
    "OLEUI_OPERR_SUBPROPINVALID",
    "OLEUI_OPERR_PROPSHEETNULL",
    "OLEUI_OPERR_PROPSHEETINVALID",
    "OLEUI_OPERR_SUPPROP",
    "OLEUI_OPERR_PROPSINVALID",
    "OLEUI_OPERR_PAGESINCORRECT",
    "OLEUI_OPERR_INVALIDPAGES",
    "OLEUI_OPERR_NOTSUPPORTED",
    "OLEUI_OPERR_DLGPROCNOTNULL",
    "OLEUI_OPERR_LPARAMNOTZERO",
    "OLEUI_GPERR_STRINGINVALID",
    "OLEUI_GPERR_CLASSIDINVALID",
    "OLEUI_GPERR_LPCLSIDEXCLUDEINVALID",
    "OLEUI_GPERR_CBFORMATINVALID",
    "OLEUI_VPERR_METAPICTINVALID",
    "OLEUI_VPERR_DVASPECTINVALID",
    "OLEUI_LPERR_LINKCNTRNULL",
    "OLEUI_LPERR_LINKCNTRINVALID",
    "OLEUI_OPERR_PROPERTYSHEET",
    "OLEUI_OPERR_OBJINFOINVALID",
    "OLEUI_OPERR_LINKINFOINVALID",
    "OLEUI_QUERY_GETCLASSID",
    "OLEUI_QUERY_LINKBROKEN",
    "FADF_AUTO",
    "FADF_STATIC",
    "FADF_EMBEDDED",
    "FADF_FIXEDSIZE",
    "FADF_RECORD",
    "FADF_HAVEIID",
    "FADF_HAVEVARTYPE",
    "FADF_BSTR",
    "FADF_UNKNOWN",
    "FADF_DISPATCH",
    "FADF_VARIANT",
    "FADF_RESERVED",
    "PARAMFLAG_NONE",
    "PARAMFLAG_FIN",
    "PARAMFLAG_FOUT",
    "PARAMFLAG_FLCID",
    "PARAMFLAG_FRETVAL",
    "PARAMFLAG_FOPT",
    "PARAMFLAG_FHASDEFAULT",
    "PARAMFLAG_FHASCUSTDATA",
    "IDLFLAG_NONE",
    "IDLFLAG_FIN",
    "IDLFLAG_FOUT",
    "IDLFLAG_FLCID",
    "IDLFLAG_FRETVAL",
    "IMPLTYPEFLAG_FDEFAULT",
    "IMPLTYPEFLAG_FSOURCE",
    "IMPLTYPEFLAG_FRESTRICTED",
    "IMPLTYPEFLAG_FDEFAULTVTABLE",
    "DISPID_UNKNOWN",
    "DISPID_VALUE",
    "DISPID_PROPERTYPUT",
    "DISPID_NEWENUM",
    "DISPID_EVALUATE",
    "DISPID_CONSTRUCTOR",
    "DISPID_DESTRUCTOR",
    "DISPID_COLLECT",
    "STDOLE_MAJORVERNUM",
    "STDOLE_MINORVERNUM",
    "STDOLE_LCID",
    "STDOLE2_MAJORVERNUM",
    "STDOLE2_MINORVERNUM",
    "STDOLE2_LCID",
    "VARIANT_NOVALUEPROP",
    "VARIANT_ALPHABOOL",
    "VARIANT_NOUSEROVERRIDE",
    "VARIANT_CALENDAR_HIJRI",
    "VARIANT_LOCALBOOL",
    "VARIANT_CALENDAR_THAI",
    "VARIANT_CALENDAR_GREGORIAN",
    "VARIANT_USE_NLS",
    "LOCALE_USE_NLS",
    "VTDATEGRE_MAX",
    "VTDATEGRE_MIN",
    "NUMPRS_LEADING_WHITE",
    "NUMPRS_TRAILING_WHITE",
    "NUMPRS_LEADING_PLUS",
    "NUMPRS_TRAILING_PLUS",
    "NUMPRS_LEADING_MINUS",
    "NUMPRS_TRAILING_MINUS",
    "NUMPRS_HEX_OCT",
    "NUMPRS_PARENS",
    "NUMPRS_DECIMAL",
    "NUMPRS_THOUSANDS",
    "NUMPRS_CURRENCY",
    "NUMPRS_EXPONENT",
    "NUMPRS_USE_ALL",
    "NUMPRS_STD",
    "NUMPRS_NEG",
    "NUMPRS_INEXACT",
    "VARCMP_LT",
    "VARCMP_EQ",
    "VARCMP_GT",
    "VARCMP_NULL",
    "MEMBERID_NIL",
    "ID_DEFAULTINST",
    "DISPATCH_METHOD",
    "DISPATCH_PROPERTYGET",
    "DISPATCH_PROPERTYPUT",
    "DISPATCH_PROPERTYPUTREF",
    "LOAD_TLB_AS_32BIT",
    "LOAD_TLB_AS_64BIT",
    "ACTIVEOBJECT_STRONG",
    "ACTIVEOBJECT_WEAK",
    "DISPATCH_CONSTRUCT",
    "DISPID_STARTENUM",
    "SID_VariantConversion",
    "SID_GetCaller",
    "SID_ProvideRuntimeContext",
    "UPDFCACHE_FLAGS",
    "UPDFCACHE_ALL",
    "UPDFCACHE_ALLBUTNODATACACHE",
    "UPDFCACHE_NORMALCACHE",
    "UPDFCACHE_IFBLANK",
    "UPDFCACHE_ONLYIFBLANK",
    "UPDFCACHE_NODATACACHE",
    "UPDFCACHE_ONSAVECACHE",
    "UPDFCACHE_ONSTOPCACHE",
    "UPDFCACHE_IFBLANKORONSAVECACHE",
    "ENUM_CONTROLS_WHICH_FLAGS",
    "GCW_WCH_SIBLING",
    "GC_WCH_CONTAINER",
    "GC_WCH_CONTAINED",
    "GC_WCH_ALL",
    "GC_WCH_FREVERSEDIR",
    "GC_WCH_FONLYAFTER",
    "GC_WCH_FONLYBEFORE",
    "GC_WCH_FSELECTED",
    "MULTICLASSINFO_FLAGS",
    "MULTICLASSINFO_GETTYPEINFO",
    "MULTICLASSINFO_GETNUMRESERVEDDISPIDS",
    "MULTICLASSINFO_GETIIDPRIMARY",
    "MULTICLASSINFO_GETIIDSOURCE",
    "VARENUM",
    "VT_EMPTY",
    "VT_NULL",
    "VT_I2",
    "VT_I4",
    "VT_R4",
    "VT_R8",
    "VT_CY",
    "VT_DATE",
    "VT_BSTR",
    "VT_DISPATCH",
    "VT_ERROR",
    "VT_BOOL",
    "VT_VARIANT",
    "VT_UNKNOWN",
    "VT_DECIMAL",
    "VT_I1",
    "VT_UI1",
    "VT_UI2",
    "VT_UI4",
    "VT_I8",
    "VT_UI8",
    "VT_INT",
    "VT_UINT",
    "VT_VOID",
    "VT_HRESULT",
    "VT_PTR",
    "VT_SAFEARRAY",
    "VT_CARRAY",
    "VT_USERDEFINED",
    "VT_LPSTR",
    "VT_LPWSTR",
    "VT_RECORD",
    "VT_INT_PTR",
    "VT_UINT_PTR",
    "VT_FILETIME",
    "VT_BLOB",
    "VT_STREAM",
    "VT_STORAGE",
    "VT_STREAMED_OBJECT",
    "VT_STORED_OBJECT",
    "VT_BLOB_OBJECT",
    "VT_CF",
    "VT_CLSID",
    "VT_VERSIONED_STREAM",
    "VT_BSTR_BLOB",
    "VT_VECTOR",
    "VT_ARRAY",
    "VT_BYREF",
    "VT_RESERVED",
    "VT_ILLEGAL",
    "VT_ILLEGALMASKED",
    "VT_TYPEMASK",
    "_wireSAFEARR_BSTR",
    "_wireSAFEARR_UNKNOWN",
    "_wireSAFEARR_DISPATCH",
    "_wireSAFEARR_VARIANT",
    "_wireSAFEARR_BRECORD",
    "_wireSAFEARR_HAVEIID",
    "SF_TYPE",
    "SF_ERROR",
    "SF_I1",
    "SF_I2",
    "SF_I4",
    "SF_I8",
    "SF_BSTR",
    "SF_UNKNOWN",
    "SF_DISPATCH",
    "SF_VARIANT",
    "SF_RECORD",
    "SF_HAVEIID",
    "_wireSAFEARRAY_UNION",
    "_wireSAFEARRAY",
    "_wireBRECORD",
    "_wireVARIANT",
    "ARRAYDESC",
    "PARAMDESCEX",
    "PARAMDESC",
    "TYPEFLAGS",
    "TYPEFLAG_FAPPOBJECT",
    "TYPEFLAG_FCANCREATE",
    "TYPEFLAG_FLICENSED",
    "TYPEFLAG_FPREDECLID",
    "TYPEFLAG_FHIDDEN",
    "TYPEFLAG_FCONTROL",
    "TYPEFLAG_FDUAL",
    "TYPEFLAG_FNONEXTENSIBLE",
    "TYPEFLAG_FOLEAUTOMATION",
    "TYPEFLAG_FRESTRICTED",
    "TYPEFLAG_FAGGREGATABLE",
    "TYPEFLAG_FREPLACEABLE",
    "TYPEFLAG_FDISPATCHABLE",
    "TYPEFLAG_FREVERSEBIND",
    "TYPEFLAG_FPROXY",
    "FUNCFLAGS",
    "FUNCFLAG_FRESTRICTED",
    "FUNCFLAG_FSOURCE",
    "FUNCFLAG_FBINDABLE",
    "FUNCFLAG_FREQUESTEDIT",
    "FUNCFLAG_FDISPLAYBIND",
    "FUNCFLAG_FDEFAULTBIND",
    "FUNCFLAG_FHIDDEN",
    "FUNCFLAG_FUSESGETLASTERROR",
    "FUNCFLAG_FDEFAULTCOLLELEM",
    "FUNCFLAG_FUIDEFAULT",
    "FUNCFLAG_FNONBROWSABLE",
    "FUNCFLAG_FREPLACEABLE",
    "FUNCFLAG_FIMMEDIATEBIND",
    "VARFLAGS",
    "VARFLAG_FREADONLY",
    "VARFLAG_FSOURCE",
    "VARFLAG_FBINDABLE",
    "VARFLAG_FREQUESTEDIT",
    "VARFLAG_FDISPLAYBIND",
    "VARFLAG_FDEFAULTBIND",
    "VARFLAG_FHIDDEN",
    "VARFLAG_FRESTRICTED",
    "VARFLAG_FDEFAULTCOLLELEM",
    "VARFLAG_FUIDEFAULT",
    "VARFLAG_FNONBROWSABLE",
    "VARFLAG_FREPLACEABLE",
    "VARFLAG_FIMMEDIATEBIND",
    "CLEANLOCALSTORAGE",
    "ICreateTypeInfo",
    "ICreateTypeInfo2",
    "ICreateTypeLib",
    "ICreateTypeLib2",
    "IEnumVARIANT",
    "LIBFLAGS",
    "LIBFLAG_FRESTRICTED",
    "LIBFLAG_FCONTROL",
    "LIBFLAG_FHIDDEN",
    "LIBFLAG_FHASDISKIMAGE",
    "CHANGEKIND",
    "CHANGEKIND_ADDMEMBER",
    "CHANGEKIND_DELETEMEMBER",
    "CHANGEKIND_SETNAMES",
    "CHANGEKIND_SETDOCUMENTATION",
    "CHANGEKIND_GENERAL",
    "CHANGEKIND_INVALIDATE",
    "CHANGEKIND_CHANGEFAILED",
    "CHANGEKIND_MAX",
    "ITypeChangeEvents",
    "ICreateErrorInfo",
    "ITypeFactory",
    "ITypeMarshal",
    "IRecordInfo",
    "IOleAdviseHolder",
    "IOleCache",
    "DISCARDCACHE",
    "DISCARDCACHE_SAVEIFDIRTY",
    "DISCARDCACHE_NOSAVE",
    "IOleCache2",
    "IOleCacheControl",
    "IParseDisplayName",
    "IOleContainer",
    "IOleClientSite",
    "OLEGETMONIKER",
    "OLEGETMONIKER_ONLYIFTHERE",
    "OLEGETMONIKER_FORCEASSIGN",
    "OLEGETMONIKER_UNASSIGN",
    "OLEGETMONIKER_TEMPFORUSER",
    "OLEWHICHMK",
    "OLEWHICHMK_CONTAINER",
    "OLEWHICHMK_OBJREL",
    "OLEWHICHMK_OBJFULL",
    "USERCLASSTYPE",
    "USERCLASSTYPE_FULL",
    "USERCLASSTYPE_SHORT",
    "USERCLASSTYPE_APPNAME",
    "OLEMISC",
    "OLEMISC_RECOMPOSEONRESIZE",
    "OLEMISC_ONLYICONIC",
    "OLEMISC_INSERTNOTREPLACE",
    "OLEMISC_STATIC",
    "OLEMISC_CANTLINKINSIDE",
    "OLEMISC_CANLINKBYOLE1",
    "OLEMISC_ISLINKOBJECT",
    "OLEMISC_INSIDEOUT",
    "OLEMISC_ACTIVATEWHENVISIBLE",
    "OLEMISC_RENDERINGISDEVICEINDEPENDENT",
    "OLEMISC_INVISIBLEATRUNTIME",
    "OLEMISC_ALWAYSRUN",
    "OLEMISC_ACTSLIKEBUTTON",
    "OLEMISC_ACTSLIKELABEL",
    "OLEMISC_NOUIACTIVATE",
    "OLEMISC_ALIGNABLE",
    "OLEMISC_SIMPLEFRAME",
    "OLEMISC_SETCLIENTSITEFIRST",
    "OLEMISC_IMEMODE",
    "OLEMISC_IGNOREACTIVATEWHENVISIBLE",
    "OLEMISC_WANTSTOMENUMERGE",
    "OLEMISC_SUPPORTSMULTILEVELUNDO",
    "OLECLOSE",
    "OLECLOSE_SAVEIFDIRTY",
    "OLECLOSE_NOSAVE",
    "OLECLOSE_PROMPTSAVE",
    "IOleObject",
    "OLERENDER",
    "OLERENDER_NONE",
    "OLERENDER_DRAW",
    "OLERENDER_FORMAT",
    "OLERENDER_ASIS",
    "OBJECTDESCRIPTOR",
    "IOleWindow",
    "OLEUPDATE",
    "OLEUPDATE_ALWAYS",
    "OLEUPDATE_ONCALL",
    "OLELINKBIND",
    "OLELINKBIND_EVENIFCLASSDIFF",
    "IOleLink",
    "BINDSPEED",
    "BINDSPEED_INDEFINITE",
    "BINDSPEED_MODERATE",
    "BINDSPEED_IMMEDIATE",
    "OLECONTF",
    "OLECONTF_EMBEDDINGS",
    "OLECONTF_LINKS",
    "OLECONTF_OTHERS",
    "OLECONTF_ONLYUSER",
    "OLECONTF_ONLYIFRUNNING",
    "IOleItemContainer",
    "IOleInPlaceUIWindow",
    "IOleInPlaceActiveObject",
    "OIFI",
    "OleMenuGroupWidths",
    "IOleInPlaceFrame",
    "IOleInPlaceObject",
    "IOleInPlaceSite",
    "IContinue",
    "IViewObject",
    "IViewObject2",
    "IDropSource",
    "IDropTarget",
    "IDropSourceNotify",
    "IEnterpriseDropTarget",
    "OLEVERB",
    "OLEVERBATTRIB",
    "OLEVERBATTRIB_NEVERDIRTIES",
    "OLEVERBATTRIB_ONCONTAINERMENU",
    "IEnumOLEVERB",
    "NUMPARSE",
    "UDATE",
    "REGKIND",
    "REGKIND_DEFAULT",
    "REGKIND_REGISTER",
    "REGKIND_NONE",
    "PARAMDATA",
    "METHODDATA",
    "INTERFACEDATA",
    "UASFLAGS",
    "UAS_NORMAL",
    "UAS_BLOCKED",
    "UAS_NOPARENTENABLE",
    "UAS_MASK",
    "READYSTATE",
    "READYSTATE_UNINITIALIZED",
    "READYSTATE_LOADING",
    "READYSTATE_LOADED",
    "READYSTATE_INTERACTIVE",
    "READYSTATE_COMPLETE",
    "LICINFO",
    "IClassFactory2",
    "IProvideClassInfo",
    "GUIDKIND",
    "GUIDKIND_DEFAULT_SOURCE_DISP_IID",
    "IProvideClassInfo2",
    "IProvideMultipleClassInfo",
    "CONTROLINFO",
    "CTRLINFO",
    "CTRLINFO_EATS_RETURN",
    "CTRLINFO_EATS_ESCAPE",
    "IOleControl",
    "POINTF",
    "XFORMCOORDS",
    "XFORMCOORDS_POSITION",
    "XFORMCOORDS_SIZE",
    "XFORMCOORDS_HIMETRICTOCONTAINER",
    "XFORMCOORDS_CONTAINERTOHIMETRIC",
    "XFORMCOORDS_EVENTCOMPAT",
    "IOleControlSite",
    "PROPPAGEINFO",
    "IPropertyPage",
    "IPropertyPage2",
    "PROPPAGESTATUS",
    "PROPPAGESTATUS_DIRTY",
    "PROPPAGESTATUS_VALIDATE",
    "PROPPAGESTATUS_CLEAN",
    "IPropertyPageSite",
    "IPropertyNotifySink",
    "CAUUID",
    "ISpecifyPropertyPages",
    "IPersistPropertyBag",
    "ISimpleFrameSite",
    "IFont",
    "PictureAttributes",
    "PICTURE_SCALABLE",
    "PICTURE_TRANSPARENT",
    "IPicture",
    "IPicture2",
    "IFontEventsDisp",
    "IFontDisp",
    "IPictureDisp",
    "IOleInPlaceObjectWindowless",
    "ACTIVATEFLAGS",
    "ACTIVATE_WINDOWLESS",
    "IOleInPlaceSiteEx",
    "OLEDCFLAGS",
    "OLEDC_NODRAW",
    "OLEDC_PAINTBKGND",
    "OLEDC_OFFSCREEN",
    "IOleInPlaceSiteWindowless",
    "VIEWSTATUS",
    "VIEWSTATUS_OPAQUE",
    "VIEWSTATUS_SOLIDBKGND",
    "VIEWSTATUS_DVASPECTOPAQUE",
    "VIEWSTATUS_DVASPECTTRANSPARENT",
    "VIEWSTATUS_SURFACE",
    "VIEWSTATUS_3DSURFACE",
    "HITRESULT",
    "HITRESULT_OUTSIDE",
    "HITRESULT_TRANSPARENT",
    "HITRESULT_CLOSE",
    "HITRESULT_HIT",
    "DVASPECT2",
    "DVASPECT_OPAQUE",
    "DVASPECT_TRANSPARENT",
    "ExtentInfo",
    "ExtentMode",
    "DVEXTENT_CONTENT",
    "DVEXTENT_INTEGRAL",
    "AspectInfoFlag",
    "DVASPECTINFOFLAG_CANOPTIMIZE",
    "AspectInfo",
    "IViewObjectEx",
    "IOleUndoUnit",
    "IOleParentUndoUnit",
    "IEnumOleUndoUnits",
    "IOleUndoManager",
    "POINTERINACTIVE",
    "POINTERINACTIVE_ACTIVATEONENTRY",
    "POINTERINACTIVE_DEACTIVATEONLEAVE",
    "POINTERINACTIVE_ACTIVATEONDRAG",
    "IPointerInactive",
    "IObjectWithSite",
    "CALPOLESTR",
    "CADWORD",
    "IPerPropertyBrowsing",
    "PROPBAG2_TYPE",
    "PROPBAG2_TYPE_UNDEFINED",
    "PROPBAG2_TYPE_DATA",
    "PROPBAG2_TYPE_URL",
    "PROPBAG2_TYPE_OBJECT",
    "PROPBAG2_TYPE_STREAM",
    "PROPBAG2_TYPE_STORAGE",
    "PROPBAG2_TYPE_MONIKER",
    "IPersistPropertyBag2",
    "IAdviseSinkEx",
    "QACONTAINERFLAGS",
    "QACONTAINER_SHOWHATCHING",
    "QACONTAINER_SHOWGRABHANDLES",
    "QACONTAINER_USERMODE",
    "QACONTAINER_DISPLAYASDEFAULT",
    "QACONTAINER_UIDEAD",
    "QACONTAINER_AUTOCLIP",
    "QACONTAINER_MESSAGEREFLECT",
    "QACONTAINER_SUPPORTSMNEMONICS",
    "QACONTAINER",
    "QACONTROL",
    "IQuickActivate",
    "OCPFIPARAMS",
    "FONTDESC",
    "PICTDESC",
    "OLE_TRISTATE",
    "OLE_TRISTATE_triUnchecked",
    "OLE_TRISTATE_triChecked",
    "OLE_TRISTATE_triGray",
    "IVBGetControl",
    "IGetOleObject",
    "IVBFormat",
    "IGetVBAObject",
    "DOCMISC",
    "DOCMISC_CANCREATEMULTIPLEVIEWS",
    "DOCMISC_SUPPORTCOMPLEXRECTANGLES",
    "DOCMISC_CANTOPENEDIT",
    "DOCMISC_NOFILESUPPORT",
    "IOleDocument",
    "IOleDocumentSite",
    "IOleDocumentView",
    "IEnumOleDocumentViews",
    "IContinueCallback",
    "PRINTFLAG",
    "PRINTFLAG_MAYBOTHERUSER",
    "PRINTFLAG_PROMPTUSER",
    "PRINTFLAG_USERMAYCHANGEPRINTER",
    "PRINTFLAG_RECOMPOSETODEVICE",
    "PRINTFLAG_DONTACTUALLYPRINT",
    "PRINTFLAG_FORCEPROPERTIES",
    "PRINTFLAG_PRINTTOFILE",
    "PAGERANGE",
    "PAGESET",
    "IPrint",
    "OLECMDF",
    "OLECMDF_SUPPORTED",
    "OLECMDF_ENABLED",
    "OLECMDF_LATCHED",
    "OLECMDF_NINCHED",
    "OLECMDF_INVISIBLE",
    "OLECMDF_DEFHIDEONCTXTMENU",
    "OLECMD",
    "OLECMDTEXT",
    "OLECMDTEXTF",
    "OLECMDTEXTF_NONE",
    "OLECMDTEXTF_NAME",
    "OLECMDTEXTF_STATUS",
    "OLECMDEXECOPT",
    "OLECMDEXECOPT_DODEFAULT",
    "OLECMDEXECOPT_PROMPTUSER",
    "OLECMDEXECOPT_DONTPROMPTUSER",
    "OLECMDEXECOPT_SHOWHELP",
    "OLECMDID",
    "OLECMDID_OPEN",
    "OLECMDID_NEW",
    "OLECMDID_SAVE",
    "OLECMDID_SAVEAS",
    "OLECMDID_SAVECOPYAS",
    "OLECMDID_PRINT",
    "OLECMDID_PRINTPREVIEW",
    "OLECMDID_PAGESETUP",
    "OLECMDID_SPELL",
    "OLECMDID_PROPERTIES",
    "OLECMDID_CUT",
    "OLECMDID_COPY",
    "OLECMDID_PASTE",
    "OLECMDID_PASTESPECIAL",
    "OLECMDID_UNDO",
    "OLECMDID_REDO",
    "OLECMDID_SELECTALL",
    "OLECMDID_CLEARSELECTION",
    "OLECMDID_ZOOM",
    "OLECMDID_GETZOOMRANGE",
    "OLECMDID_UPDATECOMMANDS",
    "OLECMDID_REFRESH",
    "OLECMDID_STOP",
    "OLECMDID_HIDETOOLBARS",
    "OLECMDID_SETPROGRESSMAX",
    "OLECMDID_SETPROGRESSPOS",
    "OLECMDID_SETPROGRESSTEXT",
    "OLECMDID_SETTITLE",
    "OLECMDID_SETDOWNLOADSTATE",
    "OLECMDID_STOPDOWNLOAD",
    "OLECMDID_ONTOOLBARACTIVATED",
    "OLECMDID_FIND",
    "OLECMDID_DELETE",
    "OLECMDID_HTTPEQUIV",
    "OLECMDID_HTTPEQUIV_DONE",
    "OLECMDID_ENABLE_INTERACTION",
    "OLECMDID_ONUNLOAD",
    "OLECMDID_PROPERTYBAG2",
    "OLECMDID_PREREFRESH",
    "OLECMDID_SHOWSCRIPTERROR",
    "OLECMDID_SHOWMESSAGE",
    "OLECMDID_SHOWFIND",
    "OLECMDID_SHOWPAGESETUP",
    "OLECMDID_SHOWPRINT",
    "OLECMDID_CLOSE",
    "OLECMDID_ALLOWUILESSSAVEAS",
    "OLECMDID_DONTDOWNLOADCSS",
    "OLECMDID_UPDATEPAGESTATUS",
    "OLECMDID_PRINT2",
    "OLECMDID_PRINTPREVIEW2",
    "OLECMDID_SETPRINTTEMPLATE",
    "OLECMDID_GETPRINTTEMPLATE",
    "OLECMDID_PAGEACTIONBLOCKED",
    "OLECMDID_PAGEACTIONUIQUERY",
    "OLECMDID_FOCUSVIEWCONTROLS",
    "OLECMDID_FOCUSVIEWCONTROLSQUERY",
    "OLECMDID_SHOWPAGEACTIONMENU",
    "OLECMDID_ADDTRAVELENTRY",
    "OLECMDID_UPDATETRAVELENTRY",
    "OLECMDID_UPDATEBACKFORWARDSTATE",
    "OLECMDID_OPTICAL_ZOOM",
    "OLECMDID_OPTICAL_GETZOOMRANGE",
    "OLECMDID_WINDOWSTATECHANGED",
    "OLECMDID_ACTIVEXINSTALLSCOPE",
    "OLECMDID_UPDATETRAVELENTRY_DATARECOVERY",
    "OLECMDID_SHOWTASKDLG",
    "OLECMDID_POPSTATEEVENT",
    "OLECMDID_VIEWPORT_MODE",
    "OLECMDID_LAYOUT_VIEWPORT_WIDTH",
    "OLECMDID_VISUAL_VIEWPORT_EXCLUDE_BOTTOM",
    "OLECMDID_USER_OPTICAL_ZOOM",
    "OLECMDID_PAGEAVAILABLE",
    "OLECMDID_GETUSERSCALABLE",
    "OLECMDID_UPDATE_CARET",
    "OLECMDID_ENABLE_VISIBILITY",
    "OLECMDID_MEDIA_PLAYBACK",
    "OLECMDID_SETFAVICON",
    "OLECMDID_SET_HOST_FULLSCREENMODE",
    "OLECMDID_EXITFULLSCREEN",
    "OLECMDID_SCROLLCOMPLETE",
    "OLECMDID_ONBEFOREUNLOAD",
    "OLECMDID_SHOWMESSAGE_BLOCKABLE",
    "OLECMDID_SHOWTASKDLG_BLOCKABLE",
    "MEDIAPLAYBACK_STATE",
    "MEDIAPLAYBACK_RESUME",
    "MEDIAPLAYBACK_PAUSE",
    "MEDIAPLAYBACK_PAUSE_AND_SUSPEND",
    "MEDIAPLAYBACK_RESUME_FROM_SUSPEND",
    "IGNOREMIME",
    "IGNOREMIME_PROMPT",
    "IGNOREMIME_TEXT",
    "WPCSETTING",
    "WPCSETTING_LOGGING_ENABLED",
    "WPCSETTING_FILEDOWNLOAD_BLOCKED",
    "IOleCommandTarget",
    "OLECMDID_REFRESHFLAG",
    "OLECMDIDF_REFRESH_NORMAL",
    "OLECMDIDF_REFRESH_IFEXPIRED",
    "OLECMDIDF_REFRESH_CONTINUE",
    "OLECMDIDF_REFRESH_COMPLETELY",
    "OLECMDIDF_REFRESH_NO_CACHE",
    "OLECMDIDF_REFRESH_RELOAD",
    "OLECMDIDF_REFRESH_LEVELMASK",
    "OLECMDIDF_REFRESH_CLEARUSERINPUT",
    "OLECMDIDF_REFRESH_PROMPTIFOFFLINE",
    "OLECMDIDF_REFRESH_THROUGHSCRIPT",
    "OLECMDIDF_REFRESH_SKIPBEFOREUNLOADEVENT",
    "OLECMDIDF_REFRESH_PAGEACTION_ACTIVEXINSTALL",
    "OLECMDIDF_REFRESH_PAGEACTION_FILEDOWNLOAD",
    "OLECMDIDF_REFRESH_PAGEACTION_LOCALMACHINE",
    "OLECMDIDF_REFRESH_PAGEACTION_POPUPWINDOW",
    "OLECMDIDF_REFRESH_PAGEACTION_PROTLOCKDOWNLOCALMACHINE",
    "OLECMDIDF_REFRESH_PAGEACTION_PROTLOCKDOWNTRUSTED",
    "OLECMDIDF_REFRESH_PAGEACTION_PROTLOCKDOWNINTRANET",
    "OLECMDIDF_REFRESH_PAGEACTION_PROTLOCKDOWNINTERNET",
    "OLECMDIDF_REFRESH_PAGEACTION_PROTLOCKDOWNRESTRICTED",
    "OLECMDIDF_REFRESH_PAGEACTION_MIXEDCONTENT",
    "OLECMDIDF_REFRESH_PAGEACTION_INVALID_CERT",
    "OLECMDIDF_REFRESH_PAGEACTION_ALLOW_VERSION",
    "OLECMDID_PAGEACTIONFLAG",
    "OLECMDIDF_PAGEACTION_FILEDOWNLOAD",
    "OLECMDIDF_PAGEACTION_ACTIVEXINSTALL",
    "OLECMDIDF_PAGEACTION_ACTIVEXTRUSTFAIL",
    "OLECMDIDF_PAGEACTION_ACTIVEXUSERDISABLE",
    "OLECMDIDF_PAGEACTION_ACTIVEXDISALLOW",
    "OLECMDIDF_PAGEACTION_ACTIVEXUNSAFE",
    "OLECMDIDF_PAGEACTION_POPUPWINDOW",
    "OLECMDIDF_PAGEACTION_LOCALMACHINE",
    "OLECMDIDF_PAGEACTION_MIMETEXTPLAIN",
    "OLECMDIDF_PAGEACTION_SCRIPTNAVIGATE",
    "OLECMDIDF_PAGEACTION_SCRIPTNAVIGATE_ACTIVEXINSTALL",
    "OLECMDIDF_PAGEACTION_PROTLOCKDOWNLOCALMACHINE",
    "OLECMDIDF_PAGEACTION_PROTLOCKDOWNTRUSTED",
    "OLECMDIDF_PAGEACTION_PROTLOCKDOWNINTRANET",
    "OLECMDIDF_PAGEACTION_PROTLOCKDOWNINTERNET",
    "OLECMDIDF_PAGEACTION_PROTLOCKDOWNRESTRICTED",
    "OLECMDIDF_PAGEACTION_PROTLOCKDOWNDENY",
    "OLECMDIDF_PAGEACTION_POPUPALLOWED",
    "OLECMDIDF_PAGEACTION_SCRIPTPROMPT",
    "OLECMDIDF_PAGEACTION_ACTIVEXUSERAPPROVAL",
    "OLECMDIDF_PAGEACTION_MIXEDCONTENT",
    "OLECMDIDF_PAGEACTION_INVALID_CERT",
    "OLECMDIDF_PAGEACTION_INTRANETZONEREQUEST",
    "OLECMDIDF_PAGEACTION_XSSFILTERED",
    "OLECMDIDF_PAGEACTION_SPOOFABLEIDNHOST",
    "OLECMDIDF_PAGEACTION_ACTIVEX_EPM_INCOMPATIBLE",
    "OLECMDIDF_PAGEACTION_SCRIPTNAVIGATE_ACTIVEXUSERAPPROVAL",
    "OLECMDIDF_PAGEACTION_WPCBLOCKED",
    "OLECMDIDF_PAGEACTION_WPCBLOCKED_ACTIVEX",
    "OLECMDIDF_PAGEACTION_EXTENSION_COMPAT_BLOCKED",
    "OLECMDIDF_PAGEACTION_NORESETACTIVEX",
    "OLECMDIDF_PAGEACTION_GENERIC_STATE",
    "OLECMDIDF_PAGEACTION_RESET",
    "OLECMDID_BROWSERSTATEFLAG",
    "OLECMDIDF_BROWSERSTATE_EXTENSIONSOFF",
    "OLECMDIDF_BROWSERSTATE_IESECURITY",
    "OLECMDIDF_BROWSERSTATE_PROTECTEDMODE_OFF",
    "OLECMDIDF_BROWSERSTATE_RESET",
    "OLECMDIDF_BROWSERSTATE_REQUIRESACTIVEX",
    "OLECMDIDF_BROWSERSTATE_DESKTOPHTMLDIALOG",
    "OLECMDIDF_BROWSERSTATE_BLOCKEDVERSION",
    "OLECMDID_OPTICAL_ZOOMFLAG",
    "OLECMDIDF_OPTICAL_ZOOM_NOPERSIST",
    "OLECMDIDF_OPTICAL_ZOOM_NOLAYOUT",
    "OLECMDIDF_OPTICAL_ZOOM_NOTRANSIENT",
    "OLECMDIDF_OPTICAL_ZOOM_RELOADFORNEWTAB",
    "PAGEACTION_UI",
    "PAGEACTION_UI_DEFAULT",
    "PAGEACTION_UI_MODAL",
    "PAGEACTION_UI_MODELESS",
    "PAGEACTION_UI_SILENT",
    "OLECMDID_WINDOWSTATE_FLAG",
    "OLECMDIDF_WINDOWSTATE_USERVISIBLE",
    "OLECMDIDF_WINDOWSTATE_ENABLED",
    "OLECMDIDF_WINDOWSTATE_USERVISIBLE_VALID",
    "OLECMDIDF_WINDOWSTATE_ENABLED_VALID",
    "OLECMDID_VIEWPORT_MODE_FLAG",
    "OLECMDIDF_VIEWPORTMODE_FIXED_LAYOUT_WIDTH",
    "OLECMDIDF_VIEWPORTMODE_EXCLUDE_VISUAL_BOTTOM",
    "OLECMDIDF_VIEWPORTMODE_FIXED_LAYOUT_WIDTH_VALID",
    "OLECMDIDF_VIEWPORTMODE_EXCLUDE_VISUAL_BOTTOM_VALID",
    "IZoomEvents",
    "IProtectFocus",
    "IProtectedModeMenuServices",
    "LPFNOLEUIHOOK",
    "OLEUIINSERTOBJECTW",
    "OLEUIINSERTOBJECTA",
    "OLEUIPASTEFLAG",
    "OLEUIPASTE_ENABLEICON",
    "OLEUIPASTE_PASTEONLY",
    "OLEUIPASTE_PASTE",
    "OLEUIPASTE_LINKANYTYPE",
    "OLEUIPASTE_LINKTYPE1",
    "OLEUIPASTE_LINKTYPE2",
    "OLEUIPASTE_LINKTYPE3",
    "OLEUIPASTE_LINKTYPE4",
    "OLEUIPASTE_LINKTYPE5",
    "OLEUIPASTE_LINKTYPE6",
    "OLEUIPASTE_LINKTYPE7",
    "OLEUIPASTE_LINKTYPE8",
    "OLEUIPASTEENTRYW",
    "OLEUIPASTEENTRYA",
    "OLEUIPASTESPECIALW",
    "OLEUIPASTESPECIALA",
    "IOleUILinkContainerW",
    "IOleUILinkContainerA",
    "OLEUIEDITLINKSW",
    "OLEUIEDITLINKSA",
    "OLEUICHANGEICONW",
    "OLEUICHANGEICONA",
    "OLEUICONVERTW",
    "OLEUICONVERTA",
    "OLEUIBUSYW",
    "OLEUIBUSYA",
    "OLEUICHANGESOURCEW",
    "OLEUICHANGESOURCEA",
    "IOleUIObjInfoW",
    "IOleUIObjInfoA",
    "IOleUILinkInfoW",
    "IOleUILinkInfoA",
    "OLEUIGNRLPROPSW",
    "OLEUIGNRLPROPSA",
    "OLEUIVIEWPROPSW",
    "OLEUIVIEWPROPSA",
    "OLEUILINKPROPSW",
    "OLEUILINKPROPSA",
    "OLEUIOBJECTPROPSW",
    "OLEUIOBJECTPROPSA",
    "IDispatchEx",
    "IDispError",
    "IVariantChangeType",
    "IObjectIdentity",
    "ICanHandleException",
    "IProvideRuntimeContext",
    "DosDateTimeToVariantTime",
    "VariantTimeToDosDateTime",
    "SystemTimeToVariantTime",
    "VariantTimeToSystemTime",
    "SafeArrayAllocDescriptor",
    "SafeArrayAllocDescriptorEx",
    "SafeArrayAllocData",
    "SafeArrayCreate",
    "SafeArrayCreateEx",
    "SafeArrayCopyData",
    "SafeArrayReleaseDescriptor",
    "SafeArrayDestroyDescriptor",
    "SafeArrayReleaseData",
    "SafeArrayDestroyData",
    "SafeArrayAddRef",
    "SafeArrayDestroy",
    "SafeArrayRedim",
    "SafeArrayGetDim",
    "SafeArrayGetElemsize",
    "SafeArrayGetUBound",
    "SafeArrayGetLBound",
    "SafeArrayLock",
    "SafeArrayUnlock",
    "SafeArrayAccessData",
    "SafeArrayUnaccessData",
    "SafeArrayGetElement",
    "SafeArrayPutElement",
    "SafeArrayCopy",
    "SafeArrayPtrOfIndex",
    "SafeArraySetRecordInfo",
    "SafeArrayGetRecordInfo",
    "SafeArraySetIID",
    "SafeArrayGetIID",
    "SafeArrayGetVartype",
    "SafeArrayCreateVector",
    "SafeArrayCreateVectorEx",
    "VariantInit",
    "VariantClear",
    "VariantCopy",
    "VariantCopyInd",
    "VariantChangeType",
    "VariantChangeTypeEx",
    "VectorFromBstr",
    "BstrFromVector",
    "VarUI1FromI2",
    "VarUI1FromI4",
    "VarUI1FromI8",
    "VarUI1FromR4",
    "VarUI1FromR8",
    "VarUI1FromCy",
    "VarUI1FromDate",
    "VarUI1FromStr",
    "VarUI1FromDisp",
    "VarUI1FromBool",
    "VarUI1FromI1",
    "VarUI1FromUI2",
    "VarUI1FromUI4",
    "VarUI1FromUI8",
    "VarUI1FromDec",
    "VarI2FromUI1",
    "VarI2FromI4",
    "VarI2FromI8",
    "VarI2FromR4",
    "VarI2FromR8",
    "VarI2FromCy",
    "VarI2FromDate",
    "VarI2FromStr",
    "VarI2FromDisp",
    "VarI2FromBool",
    "VarI2FromI1",
    "VarI2FromUI2",
    "VarI2FromUI4",
    "VarI2FromUI8",
    "VarI2FromDec",
    "VarI4FromUI1",
    "VarI4FromI2",
    "VarI4FromI8",
    "VarI4FromR4",
    "VarI4FromR8",
    "VarI4FromCy",
    "VarI4FromDate",
    "VarI4FromStr",
    "VarI4FromDisp",
    "VarI4FromBool",
    "VarI4FromI1",
    "VarI4FromUI2",
    "VarI4FromUI4",
    "VarI4FromUI8",
    "VarI4FromDec",
    "VarI8FromUI1",
    "VarI8FromI2",
    "VarI8FromR4",
    "VarI8FromR8",
    "VarI8FromCy",
    "VarI8FromDate",
    "VarI8FromStr",
    "VarI8FromDisp",
    "VarI8FromBool",
    "VarI8FromI1",
    "VarI8FromUI2",
    "VarI8FromUI4",
    "VarI8FromUI8",
    "VarI8FromDec",
    "VarR4FromUI1",
    "VarR4FromI2",
    "VarR4FromI4",
    "VarR4FromI8",
    "VarR4FromR8",
    "VarR4FromCy",
    "VarR4FromDate",
    "VarR4FromStr",
    "VarR4FromDisp",
    "VarR4FromBool",
    "VarR4FromI1",
    "VarR4FromUI2",
    "VarR4FromUI4",
    "VarR4FromUI8",
    "VarR4FromDec",
    "VarR8FromUI1",
    "VarR8FromI2",
    "VarR8FromI4",
    "VarR8FromI8",
    "VarR8FromR4",
    "VarR8FromCy",
    "VarR8FromDate",
    "VarR8FromStr",
    "VarR8FromDisp",
    "VarR8FromBool",
    "VarR8FromI1",
    "VarR8FromUI2",
    "VarR8FromUI4",
    "VarR8FromUI8",
    "VarR8FromDec",
    "VarDateFromUI1",
    "VarDateFromI2",
    "VarDateFromI4",
    "VarDateFromI8",
    "VarDateFromR4",
    "VarDateFromR8",
    "VarDateFromCy",
    "VarDateFromStr",
    "VarDateFromDisp",
    "VarDateFromBool",
    "VarDateFromI1",
    "VarDateFromUI2",
    "VarDateFromUI4",
    "VarDateFromUI8",
    "VarDateFromDec",
    "VarCyFromUI1",
    "VarCyFromI2",
    "VarCyFromI4",
    "VarCyFromI8",
    "VarCyFromR4",
    "VarCyFromR8",
    "VarCyFromDate",
    "VarCyFromStr",
    "VarCyFromDisp",
    "VarCyFromBool",
    "VarCyFromI1",
    "VarCyFromUI2",
    "VarCyFromUI4",
    "VarCyFromUI8",
    "VarCyFromDec",
    "VarBstrFromUI1",
    "VarBstrFromI2",
    "VarBstrFromI4",
    "VarBstrFromI8",
    "VarBstrFromR4",
    "VarBstrFromR8",
    "VarBstrFromCy",
    "VarBstrFromDate",
    "VarBstrFromDisp",
    "VarBstrFromBool",
    "VarBstrFromI1",
    "VarBstrFromUI2",
    "VarBstrFromUI4",
    "VarBstrFromUI8",
    "VarBstrFromDec",
    "VarBoolFromUI1",
    "VarBoolFromI2",
    "VarBoolFromI4",
    "VarBoolFromI8",
    "VarBoolFromR4",
    "VarBoolFromR8",
    "VarBoolFromDate",
    "VarBoolFromCy",
    "VarBoolFromStr",
    "VarBoolFromDisp",
    "VarBoolFromI1",
    "VarBoolFromUI2",
    "VarBoolFromUI4",
    "VarBoolFromUI8",
    "VarBoolFromDec",
    "VarI1FromUI1",
    "VarI1FromI2",
    "VarI1FromI4",
    "VarI1FromI8",
    "VarI1FromR4",
    "VarI1FromR8",
    "VarI1FromDate",
    "VarI1FromCy",
    "VarI1FromStr",
    "VarI1FromDisp",
    "VarI1FromBool",
    "VarI1FromUI2",
    "VarI1FromUI4",
    "VarI1FromUI8",
    "VarI1FromDec",
    "VarUI2FromUI1",
    "VarUI2FromI2",
    "VarUI2FromI4",
    "VarUI2FromI8",
    "VarUI2FromR4",
    "VarUI2FromR8",
    "VarUI2FromDate",
    "VarUI2FromCy",
    "VarUI2FromStr",
    "VarUI2FromDisp",
    "VarUI2FromBool",
    "VarUI2FromI1",
    "VarUI2FromUI4",
    "VarUI2FromUI8",
    "VarUI2FromDec",
    "VarUI4FromUI1",
    "VarUI4FromI2",
    "VarUI4FromI4",
    "VarUI4FromI8",
    "VarUI4FromR4",
    "VarUI4FromR8",
    "VarUI4FromDate",
    "VarUI4FromCy",
    "VarUI4FromStr",
    "VarUI4FromDisp",
    "VarUI4FromBool",
    "VarUI4FromI1",
    "VarUI4FromUI2",
    "VarUI4FromUI8",
    "VarUI4FromDec",
    "VarUI8FromUI1",
    "VarUI8FromI2",
    "VarUI8FromI8",
    "VarUI8FromR4",
    "VarUI8FromR8",
    "VarUI8FromCy",
    "VarUI8FromDate",
    "VarUI8FromStr",
    "VarUI8FromDisp",
    "VarUI8FromBool",
    "VarUI8FromI1",
    "VarUI8FromUI2",
    "VarUI8FromUI4",
    "VarUI8FromDec",
    "VarDecFromUI1",
    "VarDecFromI2",
    "VarDecFromI4",
    "VarDecFromI8",
    "VarDecFromR4",
    "VarDecFromR8",
    "VarDecFromDate",
    "VarDecFromCy",
    "VarDecFromStr",
    "VarDecFromDisp",
    "VarDecFromBool",
    "VarDecFromI1",
    "VarDecFromUI2",
    "VarDecFromUI4",
    "VarDecFromUI8",
    "VarParseNumFromStr",
    "VarNumFromParseNum",
    "VarAdd",
    "VarAnd",
    "VarCat",
    "VarDiv",
    "VarEqv",
    "VarIdiv",
    "VarImp",
    "VarMod",
    "VarMul",
    "VarOr",
    "VarPow",
    "VarSub",
    "VarXor",
    "VarAbs",
    "VarFix",
    "VarInt",
    "VarNeg",
    "VarNot",
    "VarRound",
    "VarCmp",
    "VarDecAdd",
    "VarDecDiv",
    "VarDecMul",
    "VarDecSub",
    "VarDecAbs",
    "VarDecFix",
    "VarDecInt",
    "VarDecNeg",
    "VarDecRound",
    "VarDecCmp",
    "VarDecCmpR8",
    "VarCyAdd",
    "VarCyMul",
    "VarCyMulI4",
    "VarCyMulI8",
    "VarCySub",
    "VarCyAbs",
    "VarCyFix",
    "VarCyInt",
    "VarCyNeg",
    "VarCyRound",
    "VarCyCmp",
    "VarCyCmpR8",
    "VarBstrCat",
    "VarBstrCmp",
    "VarR8Pow",
    "VarR4CmpR8",
    "VarR8Round",
    "VarDateFromUdate",
    "VarDateFromUdateEx",
    "VarUdateFromDate",
    "GetAltMonthNames",
    "VarFormat",
    "VarFormatDateTime",
    "VarFormatNumber",
    "VarFormatPercent",
    "VarFormatCurrency",
    "VarWeekdayName",
    "VarMonthName",
    "VarFormatFromTokens",
    "VarTokenizeFormatString",
    "LHashValOfNameSysA",
    "LHashValOfNameSys",
    "LoadTypeLib",
    "LoadTypeLibEx",
    "LoadRegTypeLib",
    "QueryPathOfRegTypeLib",
    "RegisterTypeLib",
    "UnRegisterTypeLib",
    "RegisterTypeLibForUser",
    "UnRegisterTypeLibForUser",
    "CreateTypeLib",
    "CreateTypeLib2",
    "DispGetParam",
    "DispGetIDsOfNames",
    "DispInvoke",
    "CreateDispTypeInfo",
    "CreateStdDispatch",
    "DispCallFunc",
    "RegisterActiveObject",
    "RevokeActiveObject",
    "GetActiveObject",
    "CreateErrorInfo",
    "GetRecordInfoFromTypeInfo",
    "GetRecordInfoFromGuids",
    "OaBuildVersion",
    "ClearCustData",
    "OaEnablePerUserTLibRegistration",
    "OleBuildVersion",
    "OleInitialize",
    "OleUninitialize",
    "OleQueryLinkFromData",
    "OleQueryCreateFromData",
    "OleCreate",
    "OleCreateEx",
    "OleCreateFromData",
    "OleCreateFromDataEx",
    "OleCreateLinkFromData",
    "OleCreateLinkFromDataEx",
    "OleCreateStaticFromData",
    "OleCreateLink",
    "OleCreateLinkEx",
    "OleCreateLinkToFile",
    "OleCreateLinkToFileEx",
    "OleCreateFromFile",
    "OleCreateFromFileEx",
    "OleLoad",
    "OleSave",
    "OleLoadFromStream",
    "OleSaveToStream",
    "OleSetContainedObject",
    "OleNoteObjectVisible",
    "RegisterDragDrop",
    "RevokeDragDrop",
    "DoDragDrop",
    "OleSetClipboard",
    "OleGetClipboard",
    "OleGetClipboardWithEnterpriseInfo",
    "OleFlushClipboard",
    "OleIsCurrentClipboard",
    "OleCreateMenuDescriptor",
    "OleSetMenuDescriptor",
    "OleDestroyMenuDescriptor",
    "OleTranslateAccelerator",
    "OleDuplicateData",
    "OleDraw",
    "OleRun",
    "OleIsRunning",
    "OleLockRunning",
    "ReleaseStgMedium",
    "CreateOleAdviseHolder",
    "OleCreateDefaultHandler",
    "OleCreateEmbeddingHelper",
    "IsAccelerator",
    "OleGetIconOfFile",
    "OleGetIconOfClass",
    "OleMetafilePictFromIconAndLabel",
    "OleRegGetUserType",
    "OleRegGetMiscStatus",
    "OleRegEnumFormatEtc",
    "OleRegEnumVerbs",
    "OleDoAutoConvert",
    "OleGetAutoConvert",
    "OleSetAutoConvert",
    "HRGN_UserSize",
    "HRGN_UserMarshal",
    "HRGN_UserUnmarshal",
    "HRGN_UserFree",
    "HRGN_UserSize64",
    "HRGN_UserMarshal64",
    "HRGN_UserUnmarshal64",
    "HRGN_UserFree64",
    "OleCreatePropertyFrame",
    "OleCreatePropertyFrameIndirect",
    "OleTranslateColor",
    "OleCreateFontIndirect",
    "OleCreatePictureIndirect",
    "OleLoadPicture",
    "OleLoadPictureEx",
    "OleLoadPicturePath",
    "OleLoadPictureFile",
    "OleLoadPictureFileEx",
    "OleSavePictureFile",
    "OleIconToCursor",
    "OleUIAddVerbMenuW",
    "OleUIAddVerbMenu",
    "OleUIAddVerbMenuA",
    "OleUIInsertObjectW",
    "OleUIInsertObject",
    "OleUIInsertObjectA",
    "OleUIPasteSpecialW",
    "OleUIPasteSpecial",
    "OleUIPasteSpecialA",
    "OleUIEditLinksW",
    "OleUIEditLinks",
    "OleUIEditLinksA",
    "OleUIChangeIconW",
    "OleUIChangeIcon",
    "OleUIChangeIconA",
    "OleUIConvertW",
    "OleUIConvert",
    "OleUIConvertA",
    "OleUICanConvertOrActivateAs",
    "OleUIBusyW",
    "OleUIBusy",
    "OleUIBusyA",
    "OleUIChangeSourceW",
    "OleUIChangeSource",
    "OleUIChangeSourceA",
    "OleUIObjectPropertiesW",
    "OleUIObjectProperties",
    "OleUIObjectPropertiesA",
    "OleUIPromptUserW",
    "OleUIPromptUser",
    "OleUIPromptUserA",
    "OleUIUpdateLinksW",
    "OleUIUpdateLinks",
    "OleUIUpdateLinksA",
]
