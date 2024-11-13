from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Data.Xml.MsXml
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.DirectComposition
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.Graphics.GdiPlus
import win32more.Windows.Win32.NetworkManagement.IpHelper
import win32more.Windows.Win32.NetworkManagement.WNet
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.Storage.FileSystem
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.StructuredStorage
import win32more.Windows.Win32.System.Com.Urlmon
import win32more.Windows.Win32.System.Console
import win32more.Windows.Win32.System.IO
import win32more.Windows.Win32.System.Ole
import win32more.Windows.Win32.System.Registry
import win32more.Windows.Win32.System.Search
import win32more.Windows.Win32.System.SystemServices
import win32more.Windows.Win32.System.Threading
import win32more.Windows.Win32.System.Variant
import win32more.Windows.Win32.UI.Controls
import win32more.Windows.Win32.UI.Shell
import win32more.Windows.Win32.UI.Shell.Common
import win32more.Windows.Win32.UI.Shell.PropertiesSystem
import win32more.Windows.Win32.UI.WindowsAndMessaging
class AASHELLMENUFILENAME(Structure):
    cbTotal: Int16
    rgbReserved: Byte * 12
    szFileName: Char * 1
class AASHELLMENUITEM(Structure):
    lpReserved1: VoidPtr
    iReserved: Int32
    uiReserved: UInt32
    lpName: POINTER(win32more.Windows.Win32.UI.Shell.AASHELLMENUFILENAME)
    psz: win32more.Windows.Win32.Foundation.PWSTR
ACENUMOPTION = Int32
ACEO_NONE: win32more.Windows.Win32.UI.Shell.ACENUMOPTION = 0
ACEO_MOSTRECENTFIRST: win32more.Windows.Win32.UI.Shell.ACENUMOPTION = 1
ACEO_FIRSTUNUSED: win32more.Windows.Win32.UI.Shell.ACENUMOPTION = 65536
ACTIVATEOPTIONS = Int32
AO_NONE: win32more.Windows.Win32.UI.Shell.ACTIVATEOPTIONS = 0
AO_DESIGNMODE: win32more.Windows.Win32.UI.Shell.ACTIVATEOPTIONS = 1
AO_NOERRORUI: win32more.Windows.Win32.UI.Shell.ACTIVATEOPTIONS = 2
AO_NOSPLASHSCREEN: win32more.Windows.Win32.UI.Shell.ACTIVATEOPTIONS = 4
AO_PRELAUNCH: win32more.Windows.Win32.UI.Shell.ACTIVATEOPTIONS = 33554432
ADJACENT_DISPLAY_EDGES = Int32
ADE_NONE: win32more.Windows.Win32.UI.Shell.ADJACENT_DISPLAY_EDGES = 0
ADE_LEFT: win32more.Windows.Win32.UI.Shell.ADJACENT_DISPLAY_EDGES = 1
ADE_RIGHT: win32more.Windows.Win32.UI.Shell.ADJACENT_DISPLAY_EDGES = 2
AHE_TYPE = Int32
AHE_DESKTOP: win32more.Windows.Win32.UI.Shell.AHE_TYPE = 0
AHE_IMMERSIVE: win32more.Windows.Win32.UI.Shell.AHE_TYPE = 1
AHTYPE = Int32
AHTYPE_UNDEFINED: win32more.Windows.Win32.UI.Shell.AHTYPE = 0
AHTYPE_USER_APPLICATION: win32more.Windows.Win32.UI.Shell.AHTYPE = 8
AHTYPE_ANY_APPLICATION: win32more.Windows.Win32.UI.Shell.AHTYPE = 16
AHTYPE_MACHINEDEFAULT: win32more.Windows.Win32.UI.Shell.AHTYPE = 32
AHTYPE_PROGID: win32more.Windows.Win32.UI.Shell.AHTYPE = 64
AHTYPE_APPLICATION: win32more.Windows.Win32.UI.Shell.AHTYPE = 128
AHTYPE_CLASS_APPLICATION: win32more.Windows.Win32.UI.Shell.AHTYPE = 256
AHTYPE_ANY_PROGID: win32more.Windows.Win32.UI.Shell.AHTYPE = 512
APPACTIONFLAGS = Int32
APPACTION_INSTALL: win32more.Windows.Win32.UI.Shell.APPACTIONFLAGS = 1
APPACTION_UNINSTALL: win32more.Windows.Win32.UI.Shell.APPACTIONFLAGS = 2
APPACTION_MODIFY: win32more.Windows.Win32.UI.Shell.APPACTIONFLAGS = 4
APPACTION_REPAIR: win32more.Windows.Win32.UI.Shell.APPACTIONFLAGS = 8
APPACTION_UPGRADE: win32more.Windows.Win32.UI.Shell.APPACTIONFLAGS = 16
APPACTION_CANGETSIZE: win32more.Windows.Win32.UI.Shell.APPACTIONFLAGS = 32
APPACTION_MODIFYREMOVE: win32more.Windows.Win32.UI.Shell.APPACTIONFLAGS = 128
APPACTION_ADDLATER: win32more.Windows.Win32.UI.Shell.APPACTIONFLAGS = 256
APPACTION_UNSCHEDULE: win32more.Windows.Win32.UI.Shell.APPACTIONFLAGS = 512
if ARCH in 'X64,ARM64':
    class APPBARDATA(Structure):
        cbSize: UInt32
        hWnd: win32more.Windows.Win32.Foundation.HWND
        uCallbackMessage: UInt32
        uEdge: UInt32
        rc: win32more.Windows.Win32.Foundation.RECT
        lParam: win32more.Windows.Win32.Foundation.LPARAM
elif ARCH in 'X86':
    class APPBARDATA(Structure):
        cbSize: UInt32
        hWnd: win32more.Windows.Win32.Foundation.HWND
        uCallbackMessage: UInt32
        uEdge: UInt32
        rc: win32more.Windows.Win32.Foundation.RECT
        lParam: win32more.Windows.Win32.Foundation.LPARAM
        _pack_ = 1
class APPCATEGORYINFO(Structure):
    Locale: UInt32
    pszDescription: win32more.Windows.Win32.Foundation.PWSTR
    AppCategoryId: Guid
class APPCATEGORYINFOLIST(Structure):
    cCategory: UInt32
    pCategoryInfo: POINTER(win32more.Windows.Win32.UI.Shell.APPCATEGORYINFO)
APPDOCLISTTYPE = Int32
ADLT_RECENT: win32more.Windows.Win32.UI.Shell.APPDOCLISTTYPE = 0
ADLT_FREQUENT: win32more.Windows.Win32.UI.Shell.APPDOCLISTTYPE = 1
class APPINFODATA(Structure):
    cbSize: UInt32
    dwMask: UInt32
    pszDisplayName: win32more.Windows.Win32.Foundation.PWSTR
    pszVersion: win32more.Windows.Win32.Foundation.PWSTR
    pszPublisher: win32more.Windows.Win32.Foundation.PWSTR
    pszProductID: win32more.Windows.Win32.Foundation.PWSTR
    pszRegisteredOwner: win32more.Windows.Win32.Foundation.PWSTR
    pszRegisteredCompany: win32more.Windows.Win32.Foundation.PWSTR
    pszLanguage: win32more.Windows.Win32.Foundation.PWSTR
    pszSupportUrl: win32more.Windows.Win32.Foundation.PWSTR
    pszSupportTelephone: win32more.Windows.Win32.Foundation.PWSTR
    pszHelpLink: win32more.Windows.Win32.Foundation.PWSTR
    pszInstallLocation: win32more.Windows.Win32.Foundation.PWSTR
    pszInstallSource: win32more.Windows.Win32.Foundation.PWSTR
    pszInstallDate: win32more.Windows.Win32.Foundation.PWSTR
    pszContact: win32more.Windows.Win32.Foundation.PWSTR
    pszComments: win32more.Windows.Win32.Foundation.PWSTR
    pszImage: win32more.Windows.Win32.Foundation.PWSTR
    pszReadmeUrl: win32more.Windows.Win32.Foundation.PWSTR
    pszUpdateInfoUrl: win32more.Windows.Win32.Foundation.PWSTR
APPINFODATAFLAGS = Int32
AIM_DISPLAYNAME: win32more.Windows.Win32.UI.Shell.APPINFODATAFLAGS = 1
AIM_VERSION: win32more.Windows.Win32.UI.Shell.APPINFODATAFLAGS = 2
AIM_PUBLISHER: win32more.Windows.Win32.UI.Shell.APPINFODATAFLAGS = 4
AIM_PRODUCTID: win32more.Windows.Win32.UI.Shell.APPINFODATAFLAGS = 8
AIM_REGISTEREDOWNER: win32more.Windows.Win32.UI.Shell.APPINFODATAFLAGS = 16
AIM_REGISTEREDCOMPANY: win32more.Windows.Win32.UI.Shell.APPINFODATAFLAGS = 32
AIM_LANGUAGE: win32more.Windows.Win32.UI.Shell.APPINFODATAFLAGS = 64
AIM_SUPPORTURL: win32more.Windows.Win32.UI.Shell.APPINFODATAFLAGS = 128
AIM_SUPPORTTELEPHONE: win32more.Windows.Win32.UI.Shell.APPINFODATAFLAGS = 256
AIM_HELPLINK: win32more.Windows.Win32.UI.Shell.APPINFODATAFLAGS = 512
AIM_INSTALLLOCATION: win32more.Windows.Win32.UI.Shell.APPINFODATAFLAGS = 1024
AIM_INSTALLSOURCE: win32more.Windows.Win32.UI.Shell.APPINFODATAFLAGS = 2048
AIM_INSTALLDATE: win32more.Windows.Win32.UI.Shell.APPINFODATAFLAGS = 4096
AIM_CONTACT: win32more.Windows.Win32.UI.Shell.APPINFODATAFLAGS = 16384
AIM_COMMENTS: win32more.Windows.Win32.UI.Shell.APPINFODATAFLAGS = 32768
AIM_IMAGE: win32more.Windows.Win32.UI.Shell.APPINFODATAFLAGS = 131072
AIM_READMEURL: win32more.Windows.Win32.UI.Shell.APPINFODATAFLAGS = 262144
AIM_UPDATEINFOURL: win32more.Windows.Win32.UI.Shell.APPINFODATAFLAGS = 524288
@winfunctype_pointer
def APPLET_PROC(hwndCpl: win32more.Windows.Win32.Foundation.HWND, msg: UInt32, lParam1: win32more.Windows.Win32.Foundation.LPARAM, lParam2: win32more.Windows.Win32.Foundation.LPARAM) -> Int32: ...
APPLICATION_VIEW_MIN_WIDTH = Int32
AVMW_DEFAULT: win32more.Windows.Win32.UI.Shell.APPLICATION_VIEW_MIN_WIDTH = 0
AVMW_320: win32more.Windows.Win32.UI.Shell.APPLICATION_VIEW_MIN_WIDTH = 1
AVMW_500: win32more.Windows.Win32.UI.Shell.APPLICATION_VIEW_MIN_WIDTH = 2
APPLICATION_VIEW_ORIENTATION = Int32
AVO_LANDSCAPE: win32more.Windows.Win32.UI.Shell.APPLICATION_VIEW_ORIENTATION = 0
AVO_PORTRAIT: win32more.Windows.Win32.UI.Shell.APPLICATION_VIEW_ORIENTATION = 1
APPLICATION_VIEW_SIZE_PREFERENCE = Int32
AVSP_DEFAULT: win32more.Windows.Win32.UI.Shell.APPLICATION_VIEW_SIZE_PREFERENCE = 0
AVSP_USE_LESS: win32more.Windows.Win32.UI.Shell.APPLICATION_VIEW_SIZE_PREFERENCE = 1
AVSP_USE_HALF: win32more.Windows.Win32.UI.Shell.APPLICATION_VIEW_SIZE_PREFERENCE = 2
AVSP_USE_MORE: win32more.Windows.Win32.UI.Shell.APPLICATION_VIEW_SIZE_PREFERENCE = 3
AVSP_USE_MINIMUM: win32more.Windows.Win32.UI.Shell.APPLICATION_VIEW_SIZE_PREFERENCE = 4
AVSP_USE_NONE: win32more.Windows.Win32.UI.Shell.APPLICATION_VIEW_SIZE_PREFERENCE = 5
AVSP_CUSTOM: win32more.Windows.Win32.UI.Shell.APPLICATION_VIEW_SIZE_PREFERENCE = 6
APPLICATION_VIEW_STATE = Int32
AVS_FULLSCREEN_LANDSCAPE: win32more.Windows.Win32.UI.Shell.APPLICATION_VIEW_STATE = 0
AVS_FILLED: win32more.Windows.Win32.UI.Shell.APPLICATION_VIEW_STATE = 1
AVS_SNAPPED: win32more.Windows.Win32.UI.Shell.APPLICATION_VIEW_STATE = 2
AVS_FULLSCREEN_PORTRAIT: win32more.Windows.Win32.UI.Shell.APPLICATION_VIEW_STATE = 3
ASSOCCLASS = Int32
ASSOCCLASS_SHELL_KEY: win32more.Windows.Win32.UI.Shell.ASSOCCLASS = 0
ASSOCCLASS_PROGID_KEY: win32more.Windows.Win32.UI.Shell.ASSOCCLASS = 1
ASSOCCLASS_PROGID_STR: win32more.Windows.Win32.UI.Shell.ASSOCCLASS = 2
ASSOCCLASS_CLSID_KEY: win32more.Windows.Win32.UI.Shell.ASSOCCLASS = 3
ASSOCCLASS_CLSID_STR: win32more.Windows.Win32.UI.Shell.ASSOCCLASS = 4
ASSOCCLASS_APP_KEY: win32more.Windows.Win32.UI.Shell.ASSOCCLASS = 5
ASSOCCLASS_APP_STR: win32more.Windows.Win32.UI.Shell.ASSOCCLASS = 6
ASSOCCLASS_SYSTEM_STR: win32more.Windows.Win32.UI.Shell.ASSOCCLASS = 7
ASSOCCLASS_FOLDER: win32more.Windows.Win32.UI.Shell.ASSOCCLASS = 8
ASSOCCLASS_STAR: win32more.Windows.Win32.UI.Shell.ASSOCCLASS = 9
ASSOCCLASS_FIXED_PROGID_STR: win32more.Windows.Win32.UI.Shell.ASSOCCLASS = 10
ASSOCCLASS_PROTOCOL_STR: win32more.Windows.Win32.UI.Shell.ASSOCCLASS = 11
ASSOCDATA = Int32
ASSOCDATA_MSIDESCRIPTOR: win32more.Windows.Win32.UI.Shell.ASSOCDATA = 1
ASSOCDATA_NOACTIVATEHANDLER: win32more.Windows.Win32.UI.Shell.ASSOCDATA = 2
ASSOCDATA_UNUSED1: win32more.Windows.Win32.UI.Shell.ASSOCDATA = 3
ASSOCDATA_HASPERUSERASSOC: win32more.Windows.Win32.UI.Shell.ASSOCDATA = 4
ASSOCDATA_EDITFLAGS: win32more.Windows.Win32.UI.Shell.ASSOCDATA = 5
ASSOCDATA_VALUE: win32more.Windows.Win32.UI.Shell.ASSOCDATA = 6
ASSOCDATA_MAX: win32more.Windows.Win32.UI.Shell.ASSOCDATA = 7
ASSOCENUM = Int32
ASSOCENUM_NONE: win32more.Windows.Win32.UI.Shell.ASSOCENUM = 0
ASSOCF = UInt32
ASSOCF_NONE: win32more.Windows.Win32.UI.Shell.ASSOCF = 0
ASSOCF_INIT_NOREMAPCLSID: win32more.Windows.Win32.UI.Shell.ASSOCF = 1
ASSOCF_INIT_BYEXENAME: win32more.Windows.Win32.UI.Shell.ASSOCF = 2
ASSOCF_OPEN_BYEXENAME: win32more.Windows.Win32.UI.Shell.ASSOCF = 2
ASSOCF_INIT_DEFAULTTOSTAR: win32more.Windows.Win32.UI.Shell.ASSOCF = 4
ASSOCF_INIT_DEFAULTTOFOLDER: win32more.Windows.Win32.UI.Shell.ASSOCF = 8
ASSOCF_NOUSERSETTINGS: win32more.Windows.Win32.UI.Shell.ASSOCF = 16
ASSOCF_NOTRUNCATE: win32more.Windows.Win32.UI.Shell.ASSOCF = 32
ASSOCF_VERIFY: win32more.Windows.Win32.UI.Shell.ASSOCF = 64
ASSOCF_REMAPRUNDLL: win32more.Windows.Win32.UI.Shell.ASSOCF = 128
ASSOCF_NOFIXUPS: win32more.Windows.Win32.UI.Shell.ASSOCF = 256
ASSOCF_IGNOREBASECLASS: win32more.Windows.Win32.UI.Shell.ASSOCF = 512
ASSOCF_INIT_IGNOREUNKNOWN: win32more.Windows.Win32.UI.Shell.ASSOCF = 1024
ASSOCF_INIT_FIXED_PROGID: win32more.Windows.Win32.UI.Shell.ASSOCF = 2048
ASSOCF_IS_PROTOCOL: win32more.Windows.Win32.UI.Shell.ASSOCF = 4096
ASSOCF_INIT_FOR_FILE: win32more.Windows.Win32.UI.Shell.ASSOCF = 8192
ASSOCF_IS_FULL_URI: win32more.Windows.Win32.UI.Shell.ASSOCF = 16384
ASSOCF_PER_MACHINE_ONLY: win32more.Windows.Win32.UI.Shell.ASSOCF = 32768
ASSOCF_APP_TO_APP: win32more.Windows.Win32.UI.Shell.ASSOCF = 65536
if ARCH in 'X64,ARM64':
    class ASSOCIATIONELEMENT(Structure):
        ac: win32more.Windows.Win32.UI.Shell.ASSOCCLASS
        hkClass: win32more.Windows.Win32.System.Registry.HKEY
        pszClass: win32more.Windows.Win32.Foundation.PWSTR
elif ARCH in 'X86':
    class ASSOCIATIONELEMENT(Structure):
        ac: win32more.Windows.Win32.UI.Shell.ASSOCCLASS
        hkClass: win32more.Windows.Win32.System.Registry.HKEY
        pszClass: win32more.Windows.Win32.Foundation.PWSTR
        _pack_ = 1
ASSOCIATIONLEVEL = Int32
AL_MACHINE: win32more.Windows.Win32.UI.Shell.ASSOCIATIONLEVEL = 0
AL_EFFECTIVE: win32more.Windows.Win32.UI.Shell.ASSOCIATIONLEVEL = 1
AL_USER: win32more.Windows.Win32.UI.Shell.ASSOCIATIONLEVEL = 2
ASSOCIATIONTYPE = Int32
AT_FILEEXTENSION: win32more.Windows.Win32.UI.Shell.ASSOCIATIONTYPE = 0
AT_URLPROTOCOL: win32more.Windows.Win32.UI.Shell.ASSOCIATIONTYPE = 1
AT_STARTMENUCLIENT: win32more.Windows.Win32.UI.Shell.ASSOCIATIONTYPE = 2
AT_MIMETYPE: win32more.Windows.Win32.UI.Shell.ASSOCIATIONTYPE = 3
ASSOCKEY = Int32
ASSOCKEY_SHELLEXECCLASS: win32more.Windows.Win32.UI.Shell.ASSOCKEY = 1
ASSOCKEY_APP: win32more.Windows.Win32.UI.Shell.ASSOCKEY = 2
ASSOCKEY_CLASS: win32more.Windows.Win32.UI.Shell.ASSOCKEY = 3
ASSOCKEY_BASECLASS: win32more.Windows.Win32.UI.Shell.ASSOCKEY = 4
ASSOCKEY_MAX: win32more.Windows.Win32.UI.Shell.ASSOCKEY = 5
ASSOCSTR = Int32
ASSOCSTR_COMMAND: win32more.Windows.Win32.UI.Shell.ASSOCSTR = 1
ASSOCSTR_EXECUTABLE: win32more.Windows.Win32.UI.Shell.ASSOCSTR = 2
ASSOCSTR_FRIENDLYDOCNAME: win32more.Windows.Win32.UI.Shell.ASSOCSTR = 3
ASSOCSTR_FRIENDLYAPPNAME: win32more.Windows.Win32.UI.Shell.ASSOCSTR = 4
ASSOCSTR_NOOPEN: win32more.Windows.Win32.UI.Shell.ASSOCSTR = 5
ASSOCSTR_SHELLNEWVALUE: win32more.Windows.Win32.UI.Shell.ASSOCSTR = 6
ASSOCSTR_DDECOMMAND: win32more.Windows.Win32.UI.Shell.ASSOCSTR = 7
ASSOCSTR_DDEIFEXEC: win32more.Windows.Win32.UI.Shell.ASSOCSTR = 8
ASSOCSTR_DDEAPPLICATION: win32more.Windows.Win32.UI.Shell.ASSOCSTR = 9
ASSOCSTR_DDETOPIC: win32more.Windows.Win32.UI.Shell.ASSOCSTR = 10
ASSOCSTR_INFOTIP: win32more.Windows.Win32.UI.Shell.ASSOCSTR = 11
ASSOCSTR_QUICKTIP: win32more.Windows.Win32.UI.Shell.ASSOCSTR = 12
ASSOCSTR_TILEINFO: win32more.Windows.Win32.UI.Shell.ASSOCSTR = 13
ASSOCSTR_CONTENTTYPE: win32more.Windows.Win32.UI.Shell.ASSOCSTR = 14
ASSOCSTR_DEFAULTICON: win32more.Windows.Win32.UI.Shell.ASSOCSTR = 15
ASSOCSTR_SHELLEXTENSION: win32more.Windows.Win32.UI.Shell.ASSOCSTR = 16
ASSOCSTR_DROPTARGET: win32more.Windows.Win32.UI.Shell.ASSOCSTR = 17
ASSOCSTR_DELEGATEEXECUTE: win32more.Windows.Win32.UI.Shell.ASSOCSTR = 18
ASSOCSTR_SUPPORTED_URI_PROTOCOLS: win32more.Windows.Win32.UI.Shell.ASSOCSTR = 19
ASSOCSTR_PROGID: win32more.Windows.Win32.UI.Shell.ASSOCSTR = 20
ASSOCSTR_APPID: win32more.Windows.Win32.UI.Shell.ASSOCSTR = 21
ASSOCSTR_APPPUBLISHER: win32more.Windows.Win32.UI.Shell.ASSOCSTR = 22
ASSOCSTR_APPICONREFERENCE: win32more.Windows.Win32.UI.Shell.ASSOCSTR = 23
ASSOCSTR_MAX: win32more.Windows.Win32.UI.Shell.ASSOCSTR = 24
ASSOC_FILTER = Int32
ASSOC_FILTER_NONE: win32more.Windows.Win32.UI.Shell.ASSOC_FILTER = 0
ASSOC_FILTER_RECOMMENDED: win32more.Windows.Win32.UI.Shell.ASSOC_FILTER = 1
ATTACHMENT_ACTION = Int32
ATTACHMENT_ACTION_CANCEL: win32more.Windows.Win32.UI.Shell.ATTACHMENT_ACTION = 0
ATTACHMENT_ACTION_SAVE: win32more.Windows.Win32.UI.Shell.ATTACHMENT_ACTION = 1
ATTACHMENT_ACTION_EXEC: win32more.Windows.Win32.UI.Shell.ATTACHMENT_ACTION = 2
ATTACHMENT_PROMPT = Int32
ATTACHMENT_PROMPT_NONE: win32more.Windows.Win32.UI.Shell.ATTACHMENT_PROMPT = 0
ATTACHMENT_PROMPT_SAVE: win32more.Windows.Win32.UI.Shell.ATTACHMENT_PROMPT = 1
ATTACHMENT_PROMPT_EXEC: win32more.Windows.Win32.UI.Shell.ATTACHMENT_PROMPT = 2
ATTACHMENT_PROMPT_EXEC_OR_SAVE: win32more.Windows.Win32.UI.Shell.ATTACHMENT_PROMPT = 3
AUTOCOMPLETELISTOPTIONS = Int32
ACLO_NONE: win32more.Windows.Win32.UI.Shell.AUTOCOMPLETELISTOPTIONS = 0
ACLO_CURRENTDIR: win32more.Windows.Win32.UI.Shell.AUTOCOMPLETELISTOPTIONS = 1
ACLO_MYCOMPUTER: win32more.Windows.Win32.UI.Shell.AUTOCOMPLETELISTOPTIONS = 2
ACLO_DESKTOP: win32more.Windows.Win32.UI.Shell.AUTOCOMPLETELISTOPTIONS = 4
ACLO_FAVORITES: win32more.Windows.Win32.UI.Shell.AUTOCOMPLETELISTOPTIONS = 8
ACLO_FILESYSONLY: win32more.Windows.Win32.UI.Shell.AUTOCOMPLETELISTOPTIONS = 16
ACLO_FILESYSDIRS: win32more.Windows.Win32.UI.Shell.AUTOCOMPLETELISTOPTIONS = 32
ACLO_VIRTUALNAMESPACE: win32more.Windows.Win32.UI.Shell.AUTOCOMPLETELISTOPTIONS = 64
AUTOCOMPLETEOPTIONS = Int32
ACO_NONE: win32more.Windows.Win32.UI.Shell.AUTOCOMPLETEOPTIONS = 0
ACO_AUTOSUGGEST: win32more.Windows.Win32.UI.Shell.AUTOCOMPLETEOPTIONS = 1
ACO_AUTOAPPEND: win32more.Windows.Win32.UI.Shell.AUTOCOMPLETEOPTIONS = 2
ACO_SEARCH: win32more.Windows.Win32.UI.Shell.AUTOCOMPLETEOPTIONS = 4
ACO_FILTERPREFIXES: win32more.Windows.Win32.UI.Shell.AUTOCOMPLETEOPTIONS = 8
ACO_USETAB: win32more.Windows.Win32.UI.Shell.AUTOCOMPLETEOPTIONS = 16
ACO_UPDOWNKEYDROPSLIST: win32more.Windows.Win32.UI.Shell.AUTOCOMPLETEOPTIONS = 32
ACO_RTLREADING: win32more.Windows.Win32.UI.Shell.AUTOCOMPLETEOPTIONS = 64
ACO_WORD_FILTER: win32more.Windows.Win32.UI.Shell.AUTOCOMPLETEOPTIONS = 128
ACO_NOPREFIXFILTERING: win32more.Windows.Win32.UI.Shell.AUTOCOMPLETEOPTIONS = 256
class AUTO_SCROLL_DATA(Structure):
    iNextSample: Int32
    dwLastScroll: UInt32
    bFull: win32more.Windows.Win32.Foundation.BOOL
    pts: win32more.Windows.Win32.Foundation.POINT * 3
    dwTimes: UInt32 * 3
    _pack_ = 1
AccessibilityDockingService = Guid('{29ce1d46-b481-4aa0-a08a-d3ebc8aca402}')
AlphabeticalCategorizer = Guid('{3c2654c6-7372-4f6b-b310-55d6128f49d2}')
HLINK_E_FIRST: win32more.Windows.Win32.Foundation.HRESULT = -2147221248
HLINK_S_FIRST: win32more.Windows.Win32.Foundation.HRESULT = 262400
WM_CPL_LAUNCH: UInt32 = 2024
WM_CPL_LAUNCHED: UInt32 = 2025
CPL_DYNAMIC_RES: UInt32 = 0
CPL_INIT: UInt32 = 1
CPL_GETCOUNT: UInt32 = 2
CPL_INQUIRE: UInt32 = 3
CPL_SELECT: UInt32 = 4
CPL_DBLCLK: UInt32 = 5
CPL_STOP: UInt32 = 6
CPL_EXIT: UInt32 = 7
CPL_NEWINQUIRE: UInt32 = 8
CPL_STARTWPARMSA: UInt32 = 9
CPL_STARTWPARMSW: UInt32 = 10
CPL_STARTWPARMS: UInt32 = 10
CPL_SETUP: UInt32 = 200
HLINK_S_DONTHIDE: Int32 = 262400
FOLDERID_NetworkFolder: Guid = Guid('{d20beec4-5ca8-4905-ae3b-bf251ea09b53}')
FOLDERID_ComputerFolder: Guid = Guid('{0ac0837c-bbf8-452a-850d-79d08e667ca7}')
FOLDERID_InternetFolder: Guid = Guid('{4d9f7874-4e0c-4904-967b-40b0d20c3e4b}')
FOLDERID_ControlPanelFolder: Guid = Guid('{82a74aeb-aeb4-465c-a014-d097ee346d63}')
FOLDERID_PrintersFolder: Guid = Guid('{76fc4e2d-d6ad-4519-a663-37bd56068185}')
FOLDERID_SyncManagerFolder: Guid = Guid('{43668bf8-c14e-49b2-97c9-747784d784b7}')
FOLDERID_SyncSetupFolder: Guid = Guid('{0f214138-b1d3-4a90-bba9-27cbc0c5389a}')
FOLDERID_ConflictFolder: Guid = Guid('{4bfefb45-347d-4006-a5be-ac0cb0567192}')
FOLDERID_SyncResultsFolder: Guid = Guid('{289a9a43-be44-4057-a41b-587a76d7e7f9}')
FOLDERID_RecycleBinFolder: Guid = Guid('{b7534046-3ecb-4c18-be4e-64cd4cb7d6ac}')
FOLDERID_ConnectionsFolder: Guid = Guid('{6f0cd92b-2e97-45d1-88ff-b0d186b8dedd}')
FOLDERID_Fonts: Guid = Guid('{fd228cb7-ae11-4ae3-864c-16f3910ab8fe}')
FOLDERID_Desktop: Guid = Guid('{b4bfcc3a-db2c-424c-b029-7fe99a87c641}')
FOLDERID_Startup: Guid = Guid('{b97d20bb-f46a-4c97-ba10-5e3608430854}')
FOLDERID_Programs: Guid = Guid('{a77f5d77-2e2b-44c3-a6a2-aba601054a51}')
FOLDERID_StartMenu: Guid = Guid('{625b53c3-ab48-4ec1-ba1f-a1ef4146fc19}')
FOLDERID_Recent: Guid = Guid('{ae50c081-ebd2-438a-8655-8a092e34987a}')
FOLDERID_SendTo: Guid = Guid('{8983036c-27c0-404b-8f08-102d10dcfd74}')
FOLDERID_Documents: Guid = Guid('{fdd39ad0-238f-46af-adb4-6c85480369c7}')
FOLDERID_Favorites: Guid = Guid('{1777f761-68ad-4d8a-87bd-30b759fa33dd}')
FOLDERID_NetHood: Guid = Guid('{c5abbf53-e17f-4121-8900-86626fc2c973}')
FOLDERID_PrintHood: Guid = Guid('{9274bd8d-cfd1-41c3-b35e-b13f55a758f4}')
FOLDERID_Templates: Guid = Guid('{a63293e8-664e-48db-a079-df759e0509f7}')
FOLDERID_CommonStartup: Guid = Guid('{82a5ea35-d9cd-47c5-9629-e15d2f714e6e}')
FOLDERID_CommonPrograms: Guid = Guid('{0139d44e-6afe-49f2-8690-3dafcae6ffb8}')
FOLDERID_CommonStartMenu: Guid = Guid('{a4115719-d62e-491d-aa7c-e74b8be3b067}')
FOLDERID_PublicDesktop: Guid = Guid('{c4aa340d-f20f-4863-afef-f87ef2e6ba25}')
FOLDERID_ProgramData: Guid = Guid('{62ab5d82-fdc1-4dc3-a9dd-070d1d495d97}')
FOLDERID_CommonTemplates: Guid = Guid('{b94237e7-57ac-4347-9151-b08c6c32d1f7}')
FOLDERID_PublicDocuments: Guid = Guid('{ed4824af-dce4-45a8-81e2-fc7965083634}')
FOLDERID_RoamingAppData: Guid = Guid('{3eb685db-65f9-4cf6-a03a-e3ef65729f3d}')
FOLDERID_LocalAppData: Guid = Guid('{f1b32785-6fba-4fcf-9d55-7b8e7f157091}')
FOLDERID_LocalAppDataLow: Guid = Guid('{a520a1a4-1780-4ff6-bd18-167343c5af16}')
FOLDERID_InternetCache: Guid = Guid('{352481e8-33be-4251-ba85-6007caedcf9d}')
FOLDERID_Cookies: Guid = Guid('{2b0f765d-c0e9-4171-908e-08a611b84ff6}')
FOLDERID_History: Guid = Guid('{d9dc8a3b-b784-432e-a781-5a1130a75963}')
FOLDERID_System: Guid = Guid('{1ac14e77-02e7-4e5d-b744-2eb1ae5198b7}')
FOLDERID_SystemX86: Guid = Guid('{d65231b0-b2f1-4857-a4ce-a8e7c6ea7d27}')
FOLDERID_Windows: Guid = Guid('{f38bf404-1d43-42f2-9305-67de0b28fc23}')
FOLDERID_Profile: Guid = Guid('{5e6c858f-0e22-4760-9afe-ea3317b67173}')
FOLDERID_Pictures: Guid = Guid('{33e28130-4e1e-4676-835a-98395c3bc3bb}')
FOLDERID_ProgramFilesX86: Guid = Guid('{7c5a40ef-a0fb-4bfc-874a-c0f2e0b9fa8e}')
FOLDERID_ProgramFilesCommonX86: Guid = Guid('{de974d24-d9c6-4d3e-bf91-f4455120b917}')
FOLDERID_ProgramFilesX64: Guid = Guid('{6d809377-6af0-444b-8957-a3773f02200e}')
FOLDERID_ProgramFilesCommonX64: Guid = Guid('{6365d5a7-0f0d-45e5-87f6-0da56b6a4f7d}')
FOLDERID_ProgramFiles: Guid = Guid('{905e63b6-c1bf-494e-b29c-65b732d3d21a}')
FOLDERID_ProgramFilesCommon: Guid = Guid('{f7f1ed05-9f6d-47a2-aaae-29d317c6f066}')
FOLDERID_UserProgramFiles: Guid = Guid('{5cd7aee2-2219-4a67-b85d-6c9ce15660cb}')
FOLDERID_UserProgramFilesCommon: Guid = Guid('{bcbd3057-ca5c-4622-b42d-bc56db0ae516}')
FOLDERID_AdminTools: Guid = Guid('{724ef170-a42d-4fef-9f26-b60e846fba4f}')
FOLDERID_CommonAdminTools: Guid = Guid('{d0384e7d-bac3-4797-8f14-cba229b392b5}')
FOLDERID_Music: Guid = Guid('{4bd8d571-6d19-48d3-be97-422220080e43}')
FOLDERID_Videos: Guid = Guid('{18989b1d-99b5-455b-841c-ab7c74e4ddfc}')
FOLDERID_Ringtones: Guid = Guid('{c870044b-f49e-4126-a9c3-b52a1ff411e8}')
FOLDERID_PublicPictures: Guid = Guid('{b6ebfb86-6907-413c-9af7-4fc2abf07cc5}')
FOLDERID_PublicMusic: Guid = Guid('{3214fab5-9757-4298-bb61-92a9deaa44ff}')
FOLDERID_PublicVideos: Guid = Guid('{2400183a-6185-49fb-a2d8-4a392a602ba3}')
FOLDERID_PublicRingtones: Guid = Guid('{e555ab60-153b-4d17-9f04-a5fe99fc15ec}')
FOLDERID_ResourceDir: Guid = Guid('{8ad10c31-2adb-4296-a8f7-e4701232c972}')
FOLDERID_LocalizedResourcesDir: Guid = Guid('{2a00375e-224c-49de-b8d1-440df7ef3ddc}')
FOLDERID_CommonOEMLinks: Guid = Guid('{c1bae2d0-10df-4334-bedd-7aa20b227a9d}')
FOLDERID_CDBurning: Guid = Guid('{9e52ab10-f80d-49df-acb8-4330f5687855}')
FOLDERID_UserProfiles: Guid = Guid('{0762d272-c50a-4bb0-a382-697dcd729b80}')
FOLDERID_Playlists: Guid = Guid('{de92c1c7-837f-4f69-a3bb-86e631204a23}')
FOLDERID_SamplePlaylists: Guid = Guid('{15ca69b3-30ee-49c1-ace1-6b5ec372afb5}')
FOLDERID_SampleMusic: Guid = Guid('{b250c668-f57d-4ee1-a63c-290ee7d1aa1f}')
FOLDERID_SamplePictures: Guid = Guid('{c4900540-2379-4c75-844b-64e6faf8716b}')
FOLDERID_SampleVideos: Guid = Guid('{859ead94-2e85-48ad-a71a-0969cb56a6cd}')
FOLDERID_PhotoAlbums: Guid = Guid('{69d2cf90-fc33-4fb7-9a0c-ebb0f0fcb43c}')
FOLDERID_Public: Guid = Guid('{dfdf76a2-c82a-4d63-906a-5644ac457385}')
FOLDERID_ChangeRemovePrograms: Guid = Guid('{df7266ac-9274-4867-8d55-3bd661de872d}')
FOLDERID_AppUpdates: Guid = Guid('{a305ce99-f527-492b-8b1a-7e76fa98d6e4}')
FOLDERID_AddNewPrograms: Guid = Guid('{de61d971-5ebc-4f02-a3a9-6c82895e5c04}')
FOLDERID_Downloads: Guid = Guid('{374de290-123f-4565-9164-39c4925e467b}')
FOLDERID_PublicDownloads: Guid = Guid('{3d644c9b-1fb8-4f30-9b45-f670235f79c0}')
FOLDERID_SavedSearches: Guid = Guid('{7d1d3a04-debb-4115-95cf-2f29da2920da}')
FOLDERID_QuickLaunch: Guid = Guid('{52a4f021-7b75-48a9-9f6b-4b87a210bc8f}')
FOLDERID_Contacts: Guid = Guid('{56784854-c6cb-462b-8169-88e350acb882}')
FOLDERID_SidebarParts: Guid = Guid('{a75d362e-50fc-4fb7-ac2c-a8beaa314493}')
FOLDERID_SidebarDefaultParts: Guid = Guid('{7b396e54-9ec5-4300-be0a-2482ebae1a26}')
FOLDERID_PublicGameTasks: Guid = Guid('{debf2536-e1a8-4c59-b6a2-414586476aea}')
FOLDERID_GameTasks: Guid = Guid('{054fae61-4dd8-4787-80b6-090220c4b700}')
FOLDERID_SavedGames: Guid = Guid('{4c5c32ff-bb9d-43b0-b5b4-2d72e54eaaa4}')
FOLDERID_Games: Guid = Guid('{cac52c1a-b53d-4edc-92d7-6b2e8ac19434}')
FOLDERID_SEARCH_MAPI: Guid = Guid('{98ec0e18-2098-4d44-8644-66979315a281}')
FOLDERID_SEARCH_CSC: Guid = Guid('{ee32e446-31ca-4aba-814f-a5ebd2fd6d5e}')
FOLDERID_Links: Guid = Guid('{bfb9d5e0-c6a9-404c-b2b2-ae6db6af4968}')
FOLDERID_UsersFiles: Guid = Guid('{f3ce0f7c-4901-4acc-8648-d5d44b04ef8f}')
FOLDERID_UsersLibraries: Guid = Guid('{a302545d-deff-464b-abe8-61c8648d939b}')
FOLDERID_SearchHome: Guid = Guid('{190337d1-b8ca-4121-a639-6d472d16972a}')
FOLDERID_OriginalImages: Guid = Guid('{2c36c0aa-5812-4b87-bfd0-4cd0dfb19b39}')
FOLDERID_DocumentsLibrary: Guid = Guid('{7b0db17d-9cd2-4a93-9733-46cc89022e7c}')
FOLDERID_MusicLibrary: Guid = Guid('{2112ab0a-c86a-4ffe-a368-0de96e47012e}')
FOLDERID_PicturesLibrary: Guid = Guid('{a990ae9f-a03b-4e80-94bc-9912d7504104}')
FOLDERID_VideosLibrary: Guid = Guid('{491e922f-5643-4af4-a7eb-4e7a138d8174}')
FOLDERID_RecordedTVLibrary: Guid = Guid('{1a6fdba2-f42d-4358-a798-b74d745926c5}')
FOLDERID_HomeGroup: Guid = Guid('{52528a6b-b9e3-4add-b60d-588c2dba842d}')
FOLDERID_HomeGroupCurrentUser: Guid = Guid('{9b74b6a3-0dfd-4f11-9e78-5f7800f2e772}')
FOLDERID_DeviceMetadataStore: Guid = Guid('{5ce4a5e9-e4eb-479d-b89f-130c02886155}')
FOLDERID_Libraries: Guid = Guid('{1b3ea5dc-b587-4786-b4ef-bd1dc332aeae}')
FOLDERID_PublicLibraries: Guid = Guid('{48daf80b-e6cf-4f4e-b800-0e69d84ee384}')
FOLDERID_UserPinned: Guid = Guid('{9e3995ab-1f9c-4f13-b827-48b24b6c7174}')
FOLDERID_ImplicitAppShortcuts: Guid = Guid('{bcb5256f-79f6-4cee-b725-dc34e402fd46}')
FOLDERID_AccountPictures: Guid = Guid('{008ca0b1-55b4-4c56-b8a8-4de4b299d3be}')
FOLDERID_PublicUserTiles: Guid = Guid('{0482af6c-08f1-4c34-8c90-e17ec98b1e17}')
FOLDERID_AppsFolder: Guid = Guid('{1e87508d-89c2-42f0-8a7e-645a0f50ca58}')
FOLDERID_StartMenuAllPrograms: Guid = Guid('{f26305ef-6948-40b9-b255-81453d09c785}')
FOLDERID_CommonStartMenuPlaces: Guid = Guid('{a440879f-87a0-4f7d-b700-0207b966194a}')
FOLDERID_ApplicationShortcuts: Guid = Guid('{a3918781-e5f2-4890-b3d9-a7e54332328c}')
FOLDERID_RoamingTiles: Guid = Guid('{00bcfc5a-ed94-4e48-96a1-3f6217f21990}')
FOLDERID_RoamedTileImages: Guid = Guid('{aaa8d5a5-f1d6-4259-baa8-78e7ef60835e}')
FOLDERID_Screenshots: Guid = Guid('{b7bede81-df94-4682-a7d8-57a52620b86f}')
FOLDERID_CameraRoll: Guid = Guid('{ab5fb87b-7ce2-4f83-915d-550846c9537b}')
FOLDERID_SkyDrive: Guid = Guid('{a52bba46-e9e1-435f-b3d9-28daa648c0f6}')
FOLDERID_OneDrive: Guid = Guid('{a52bba46-e9e1-435f-b3d9-28daa648c0f6}')
FOLDERID_SkyDriveDocuments: Guid = Guid('{24d89e24-2f19-4534-9dde-6a6671fbb8fe}')
FOLDERID_SkyDrivePictures: Guid = Guid('{339719b5-8c47-4894-94c2-d8f77add44a6}')
FOLDERID_SkyDriveMusic: Guid = Guid('{c3f2459e-80d6-45dc-bfef-1f769f2be730}')
FOLDERID_SkyDriveCameraRoll: Guid = Guid('{767e6811-49cb-4273-87c2-20f355e1085b}')
FOLDERID_SearchHistory: Guid = Guid('{0d4c3db6-03a3-462f-a0e6-08924c41b5d4}')
FOLDERID_SearchTemplates: Guid = Guid('{7e636bfe-dfa9-4d5e-b456-d7b39851d8a9}')
FOLDERID_CameraRollLibrary: Guid = Guid('{2b20df75-1eda-4039-8097-38798227d5b7}')
FOLDERID_SavedPictures: Guid = Guid('{3b193882-d3ad-4eab-965a-69829d1fb59f}')
FOLDERID_SavedPicturesLibrary: Guid = Guid('{e25b5812-be88-4bd9-94b0-29233477b6c3}')
FOLDERID_RetailDemo: Guid = Guid('{12d4c69e-24ad-4923-be19-31321c43a767}')
FOLDERID_Device: Guid = Guid('{1c2ac1dc-4358-4b6c-9733-af21156576f0}')
FOLDERID_DevelopmentFiles: Guid = Guid('{dbe8e08e-3053-4bbc-b183-2a7b2b191e59}')
FOLDERID_Objects3D: Guid = Guid('{31c0dd25-9439-4f12-bf41-7ff4eda38722}')
FOLDERID_AppCaptures: Guid = Guid('{edc0fe71-98d8-4f4a-b920-c8dc133cb165}')
FOLDERID_LocalDocuments: Guid = Guid('{f42ee2d3-909f-4907-8871-4c22fc0bf756}')
FOLDERID_LocalPictures: Guid = Guid('{0ddd015d-b06c-45d5-8c4c-f59713854639}')
FOLDERID_LocalVideos: Guid = Guid('{35286a68-3c57-41a1-bbb1-0eae73d76c95}')
FOLDERID_LocalMusic: Guid = Guid('{a0c69a99-21c8-4671-8703-7934162fcf1d}')
FOLDERID_LocalDownloads: Guid = Guid('{7d83ee9b-2244-4e70-b1f5-5393042af1e4}')
FOLDERID_RecordedCalls: Guid = Guid('{2f8b40c2-83ed-48ee-b383-a1f157ec6f9a}')
FOLDERID_AllAppMods: Guid = Guid('{7ad67899-66af-43ba-9156-6aad42e6c596}')
FOLDERID_CurrentAppMods: Guid = Guid('{3db40b20-2a30-4dbe-917e-771dd21dd099}')
FOLDERID_AppDataDesktop: Guid = Guid('{b2c5e279-7add-439f-b28c-c41fe1bbf672}')
FOLDERID_AppDataDocuments: Guid = Guid('{7be16610-1f7f-44ac-bff0-83e15f2ffca1}')
FOLDERID_AppDataFavorites: Guid = Guid('{7cfbefbc-de1f-45aa-b843-a542ac536cc9}')
FOLDERID_AppDataProgramData: Guid = Guid('{559d40a3-a036-40fa-af61-84cb430a4d34}')
FOLDERID_LocalStorage: Guid = Guid('{b3eb08d3-a1f3-496b-865a-42b536cda0ec}')
CLSID_InternetShortcut: Guid = Guid('{fbf23b40-e3f0-101b-8488-00aa003e56f8}')
CLSID_NetworkDomain: Guid = Guid('{46e06680-4bf0-11d1-83ee-00a0c90dc849}')
CLSID_NetworkServer: Guid = Guid('{c0542a90-4bf0-11d1-83ee-00a0c90dc849}')
CLSID_NetworkShare: Guid = Guid('{54a754c0-4bf0-11d1-83ee-00a0c90dc849}')
CLSID_MyComputer: Guid = Guid('{20d04fe0-3aea-1069-a2d8-08002b30309d}')
CLSID_Internet: Guid = Guid('{871c5380-42a0-1069-a2ea-08002b30309d}')
CLSID_RecycleBin: Guid = Guid('{645ff040-5081-101b-9f08-00aa002f954e}')
CLSID_ControlPanel: Guid = Guid('{21ec2020-3aea-1069-a2dd-08002b30309d}')
CLSID_Printers: Guid = Guid('{2227a280-3aea-1069-a2de-08002b30309d}')
CLSID_MyDocuments: Guid = Guid('{450d8fba-ad25-11d0-98a8-0800361b1103}')
STR_MYDOCS_CLSID: String = '{450D8FBA-AD25-11D0-98A8-0800361B1103}'
CATID_BrowsableShellExt: Guid = Guid('{00021490-0000-0000-c000-000000000046}')
CATID_BrowseInPlace: Guid = Guid('{00021491-0000-0000-c000-000000000046}')
CATID_DeskBand: Guid = Guid('{00021492-0000-0000-c000-000000000046}')
CATID_InfoBand: Guid = Guid('{00021493-0000-0000-c000-000000000046}')
CATID_CommBand: Guid = Guid('{00021494-0000-0000-c000-000000000046}')
FMTID_Intshcut: Guid = Guid('{000214a0-0000-0000-c000-000000000046}')
FMTID_InternetSite: Guid = Guid('{000214a1-0000-0000-c000-000000000046}')
CGID_Explorer: Guid = Guid('{000214d0-0000-0000-c000-000000000046}')
CGID_ShellDocView: Guid = Guid('{000214d1-0000-0000-c000-000000000046}')
CGID_ShellServiceObject: Guid = Guid('{000214d2-0000-0000-c000-000000000046}')
CGID_ExplorerBarDoc: Guid = Guid('{000214d3-0000-0000-c000-000000000046}')
CLSID_FolderShortcut: Guid = Guid('{0afaced1-e828-11d1-9187-b532f1e9575d}')
CLSID_CFSIconOverlayManager: Guid = Guid('{63b51f81-c868-11d0-999c-00c04fd655e1}')
CLSID_ShellThumbnailDiskCache: Guid = Guid('{1ebdcf80-a200-11d0-a3a4-00c04fd706ec}')
SID_DefView: Guid = Guid('{6d12fe80-7911-11cf-9534-0000c05bae0b}')
CGID_DefView: Guid = Guid('{4af07f10-d231-11d0-b942-00a0c90312e1}')
CLSID_MenuBand: Guid = Guid('{5b4dae26-b807-11d0-9815-00c04fd91972}')
VID_LargeIcons: Guid = Guid('{0057d0e0-3573-11cf-ae69-08002b2e1262}')
VID_SmallIcons: Guid = Guid('{089000c0-3573-11cf-ae69-08002b2e1262}')
VID_List: Guid = Guid('{0e1fa5e0-3573-11cf-ae69-08002b2e1262}')
VID_Details: Guid = Guid('{137e7700-3573-11cf-ae69-08002b2e1262}')
VID_Tile: Guid = Guid('{65f125e5-7be1-4810-ba9d-d271c8432ce3}')
VID_Content: Guid = Guid('{30c2c434-0889-4c8d-985d-a9f71830b0a9}')
VID_Thumbnails: Guid = Guid('{8bebb290-52d0-11d0-b7f4-00c04fd706ec}')
VID_ThumbStrip: Guid = Guid('{8eefa624-d1e9-445b-94b7-74fbce2ea11a}')
SID_SInPlaceBrowser: Guid = Guid('{1d2ae02b-3655-46cc-b63a-285988153bca}')
SID_SSearchBoxInfo: Guid = Guid('{142daa61-516b-4713-b49c-fb985ef82998}')
SID_CommandsPropertyBag: Guid = Guid('{6e043250-4416-485c-b143-e62a760d9fe5}')
CLSID_CURLSearchHook: Guid = Guid('{cfbfae00-17a6-11d0-99cb-00c04fd64497}')
CLSID_AutoComplete: Guid = Guid('{00bb2763-6a77-11d0-a535-00c04fd7d062}')
CLSID_ACLHistory: Guid = Guid('{00bb2764-6a77-11d0-a535-00c04fd7d062}')
CLSID_ACListISF: Guid = Guid('{03c036f1-a186-11d0-824a-00aa005b4383}')
CLSID_ACLMRU: Guid = Guid('{6756a641-de71-11d0-831b-00aa005b4383}')
CLSID_ACLMulti: Guid = Guid('{00bb2765-6a77-11d0-a535-00c04fd7d062}')
CLSID_ACLCustomMRU: Guid = Guid('{6935db93-21e8-4ccc-beb9-9fe3c77a297a}')
CLSID_ProgressDialog: Guid = Guid('{f8383852-fcd3-11d1-a6b9-006097df5bd4}')
SID_STopLevelBrowser: Guid = Guid('{4c96be40-915c-11cf-99d3-00aa004ae837}')
CLSID_FileTypes: Guid = Guid('{b091e540-83e3-11cf-a713-0020afd79762}')
CLSID_ActiveDesktop: Guid = Guid('{75048700-ef1f-11d0-9888-006097deacf9}')
CLSID_QueryAssociations: Guid = Guid('{a07034fd-6caa-4954-ac3f-97a27216f98a}')
CLSID_LinkColumnProvider: Guid = Guid('{24f14f02-7b1c-11d1-838f-0000f80461cf}')
CGID_ShortCut: Guid = Guid('{93a68750-951a-11d1-946f-000000000000}')
CLSID_InternetButtons: Guid = Guid('{1e796980-9cc5-11d1-a83f-00c04fc99d61}')
CLSID_MSOButtons: Guid = Guid('{178f34b8-a282-11d2-86c5-00c04f8eea99}')
CLSID_ToolbarExtButtons: Guid = Guid('{2ce4b5d8-a28f-11d2-86c5-00c04f8eea99}')
CLSID_DarwinAppPublisher: Guid = Guid('{cfccc7a0-a282-11d1-9082-006008059382}')
CLSID_DocHostUIHandler: Guid = Guid('{7057e952-bd1b-11d1-8919-00c04fc2c836}')
PSGUID_SHELLDETAILS: Guid = Guid('{28636aa6-953d-11d2-b5d6-00c04fd918d0}')
FMTID_ShellDetails: Guid = Guid('{28636aa6-953d-11d2-b5d6-00c04fd918d0}')
PID_FINDDATA: UInt32 = 0
PID_NETRESOURCE: UInt32 = 1
PID_DESCRIPTIONID: UInt32 = 2
PID_WHICHFOLDER: UInt32 = 3
PID_NETWORKLOCATION: UInt32 = 4
PID_COMPUTERNAME: UInt32 = 5
FMTID_Storage: Guid = Guid('{b725f130-47ef-101a-a5f1-02608c9eebac}')
PSGUID_IMAGEPROPERTIES: Guid = Guid('{14b81da1-0135-4d31-96d9-6cbfc9671a99}')
FMTID_ImageProperties: Guid = Guid('{14b81da1-0135-4d31-96d9-6cbfc9671a99}')
PSGUID_CUSTOMIMAGEPROPERTIES: Guid = Guid('{7ecd8b0e-c136-4a9b-9411-4ebd6673ccc3}')
FMTID_CustomImageProperties: Guid = Guid('{7ecd8b0e-c136-4a9b-9411-4ebd6673ccc3}')
PSGUID_LIBRARYPROPERTIES: Guid = Guid('{5d76b67f-9b3d-44bb-b6ae-25da4f638a67}')
FMTID_LibraryProperties: Guid = Guid('{5d76b67f-9b3d-44bb-b6ae-25da4f638a67}')
PSGUID_DISPLACED: Guid = Guid('{9b174b33-40ff-11d2-a27e-00c04fc30871}')
FMTID_Displaced: Guid = Guid('{9b174b33-40ff-11d2-a27e-00c04fc30871}')
PID_DISPLACED_FROM: UInt32 = 2
PID_DISPLACED_DATE: UInt32 = 3
PSGUID_BRIEFCASE: Guid = Guid('{328d8b21-7729-4bfc-954c-902b329d56b0}')
FMTID_Briefcase: Guid = Guid('{328d8b21-7729-4bfc-954c-902b329d56b0}')
PID_SYNC_COPY_IN: UInt32 = 2
PSGUID_MISC: Guid = Guid('{9b174b34-40ff-11d2-a27e-00c04fc30871}')
FMTID_Misc: Guid = Guid('{9b174b34-40ff-11d2-a27e-00c04fc30871}')
PID_MISC_STATUS: UInt32 = 2
PID_MISC_ACCESSCOUNT: UInt32 = 3
PID_MISC_OWNER: UInt32 = 4
PID_HTMLINFOTIPFILE: UInt32 = 5
PID_MISC_PICS: UInt32 = 6
PSGUID_WEBVIEW: Guid = Guid('{f2275480-f782-4291-bd94-f13693513aec}')
FMTID_WebView: Guid = Guid('{f2275480-f782-4291-bd94-f13693513aec}')
PID_DISPLAY_PROPERTIES: UInt32 = 0
PID_INTROTEXT: UInt32 = 1
PSGUID_MUSIC: Guid = Guid('{56a3372e-ce9c-11d2-9f0e-006097c686f6}')
FMTID_MUSIC: Guid = Guid('{56a3372e-ce9c-11d2-9f0e-006097c686f6}')
PIDSI_ARTIST: UInt32 = 2
PIDSI_SONGTITLE: UInt32 = 3
PIDSI_ALBUM: UInt32 = 4
PIDSI_YEAR: UInt32 = 5
PIDSI_COMMENT: UInt32 = 6
PIDSI_TRACK: UInt32 = 7
PIDSI_GENRE: UInt32 = 11
PIDSI_LYRICS: UInt32 = 12
PSGUID_DRM: Guid = Guid('{aeac19e4-89ae-4508-b9b7-bb867abee2ed}')
FMTID_DRM: Guid = Guid('{aeac19e4-89ae-4508-b9b7-bb867abee2ed}')
PIDDRSI_PROTECTED: UInt32 = 2
PIDDRSI_DESCRIPTION: UInt32 = 3
PIDDRSI_PLAYCOUNT: UInt32 = 4
PIDDRSI_PLAYSTARTS: UInt32 = 5
PIDDRSI_PLAYEXPIRES: UInt32 = 6
PSGUID_VIDEO: Guid = Guid('{64440491-4c8b-11d1-8b70-080036b11a03}')
PIDVSI_STREAM_NAME: UInt32 = 2
PIDVSI_FRAME_WIDTH: UInt32 = 3
PIDVSI_FRAME_HEIGHT: UInt32 = 4
PIDVSI_TIMELENGTH: UInt32 = 7
PIDVSI_FRAME_COUNT: UInt32 = 5
PIDVSI_FRAME_RATE: UInt32 = 6
PIDVSI_DATA_RATE: UInt32 = 8
PIDVSI_SAMPLE_SIZE: UInt32 = 9
PIDVSI_COMPRESSION: UInt32 = 10
PIDVSI_STREAM_NUMBER: UInt32 = 11
PSGUID_AUDIO: Guid = Guid('{64440490-4c8b-11d1-8b70-080036b11a03}')
PIDASI_FORMAT: UInt32 = 2
PIDASI_TIMELENGTH: UInt32 = 3
PIDASI_AVG_DATA_RATE: UInt32 = 4
PIDASI_SAMPLE_RATE: UInt32 = 5
PIDASI_SAMPLE_SIZE: UInt32 = 6
PIDASI_CHANNEL_COUNT: UInt32 = 7
PIDASI_STREAM_NUMBER: UInt32 = 8
PIDASI_STREAM_NAME: UInt32 = 9
PIDASI_COMPRESSION: UInt32 = 10
PSGUID_CONTROLPANEL: Guid = Guid('{305ca226-d286-468e-b848-2b2e8e697b74}')
PID_CONTROLPANEL_CATEGORY: UInt32 = 2
PSGUID_VOLUME: Guid = Guid('{9b174b35-40ff-11d2-a27e-00c04fc30871}')
FMTID_Volume: Guid = Guid('{9b174b35-40ff-11d2-a27e-00c04fc30871}')
PID_VOLUME_FREE: UInt32 = 2
PID_VOLUME_CAPACITY: UInt32 = 3
PID_VOLUME_FILESYSTEM: UInt32 = 4
PSGUID_SHARE: Guid = Guid('{d8c3986f-813b-449c-845d-87b95d674ade}')
PID_SHARE_CSC_STATUS: UInt32 = 2
PSGUID_LINK: Guid = Guid('{b9b4b3fc-2b51-4a42-b5d8-324146afcf25}')
PID_LINK_TARGET: UInt32 = 2
PID_LINK_TARGET_TYPE: UInt32 = 3
PSGUID_QUERY_D: Guid = Guid('{49691c90-7e17-101a-a91c-08002b2ecda9}')
FMTID_Query: Guid = Guid('{49691c90-7e17-101a-a91c-08002b2ecda9}')
PID_QUERY_RANK: UInt32 = 2
PSGUID_SUMMARYINFORMATION: Guid = Guid('{f29f85e0-4ff9-1068-ab91-08002b27b3d9}')
PSGUID_DOCUMENTSUMMARYINFORMATION: Guid = Guid('{d5cdd502-2e9c-101b-9397-08002b2cf9ae}')
PSGUID_MEDIAFILESUMMARYINFORMATION: Guid = Guid('{64440492-4c8b-11d1-8b70-080036b11a03}')
PSGUID_IMAGESUMMARYINFORMATION: Guid = Guid('{6444048f-4c8b-11d1-8b70-080036b11a03}')
CLSID_HWShellExecute: Guid = Guid('{ffb8655f-81b9-4fce-b89c-9a6ba76d13e7}')
CLSID_DragDropHelper: Guid = Guid('{4657278a-411b-11d2-839a-00c04fd918d0}')
CLSID_CAnchorBrowsePropertyPage: Guid = Guid('{3050f3bb-98b5-11cf-bb82-00aa00bdce0b}')
CLSID_CImageBrowsePropertyPage: Guid = Guid('{3050f3b3-98b5-11cf-bb82-00aa00bdce0b}')
CLSID_CDocBrowsePropertyPage: Guid = Guid('{3050f3b4-98b5-11cf-bb82-00aa00bdce0b}')
SID_STopWindow: Guid = Guid('{49e1b500-4636-11d3-97f7-00c04f45d0b3}')
SID_SGetViewFromViewDual: Guid = Guid('{889a935d-971e-4b12-b90c-24dfc9e1e5e8}')
CLSID_FolderItemsMultiLevel: Guid = Guid('{53c74826-ab99-4d33-aca4-3117f51d3788}')
CLSID_NewMenu: Guid = Guid('{d969a300-e7ff-11d0-a93b-00a0c90f2719}')
BHID_SFObject: Guid = Guid('{3981e224-f559-11d3-8e3a-00c04f6837d5}')
BHID_SFUIObject: Guid = Guid('{3981e225-f559-11d3-8e3a-00c04f6837d5}')
BHID_SFViewObject: Guid = Guid('{3981e226-f559-11d3-8e3a-00c04f6837d5}')
BHID_Storage: Guid = Guid('{3981e227-f559-11d3-8e3a-00c04f6837d5}')
BHID_Stream: Guid = Guid('{1cebb3ab-7c10-499a-a417-92ca16c4cb83}')
BHID_RandomAccessStream: Guid = Guid('{f16fc93b-77ae-4cfe-bda7-a866eea6878d}')
BHID_LinkTargetItem: Guid = Guid('{3981e228-f559-11d3-8e3a-00c04f6837d5}')
BHID_StorageEnum: Guid = Guid('{4621a4e3-f0d6-4773-8a9c-46e77b174840}')
BHID_Transfer: Guid = Guid('{d5e346a1-f753-4932-b403-4574800e2498}')
BHID_PropertyStore: Guid = Guid('{0384e1a4-1523-439c-a4c8-ab911052f586}')
BHID_ThumbnailHandler: Guid = Guid('{7b2e650a-8e20-4f4a-b09e-6597afc72fb0}')
BHID_EnumItems: Guid = Guid('{94f60519-2850-4924-aa5a-d15e84868039}')
BHID_DataObject: Guid = Guid('{b8c0bd9f-ed24-455c-83e6-d5390c4fe8c4}')
BHID_AssociationArray: Guid = Guid('{bea9ef17-82f1-4f60-9284-4f8db75c3be9}')
BHID_Filter: Guid = Guid('{38d08778-f557-4690-9ebf-ba54706ad8f7}')
BHID_EnumAssocHandlers: Guid = Guid('{b8ab0b9c-c2ec-4f7a-918d-314900e6280a}')
BHID_StorageItem: Guid = Guid('{404e2109-77d2-4699-a5a0-4fdf10db9837}')
BHID_FilePlaceholder: Guid = Guid('{8677dceb-aae0-4005-8d3d-547fa852f825}')
CATID_FilePlaceholderMergeHandler: Guid = Guid('{3e9c9a51-d4aa-4870-b47c-7424b491f1cc}')
SID_CtxQueryAssociations: Guid = Guid('{faadfc40-b777-4b69-aa81-77035ef0e6e8}')
CLSID_QuickLinks: Guid = Guid('{0e5cbf21-d15f-11d0-8301-00aa005b4383}')
CLSID_ISFBand: Guid = Guid('{d82be2b0-5764-11d0-a96e-00c04fd705a2}')
CLSID_ShellFldSetExt: Guid = Guid('{6d5313c0-8c62-11d1-b2cd-006097df8c11}')
SID_SMenuBandChild: Guid = Guid('{ed9cc020-08b9-11d1-9823-00c04fd91972}')
SID_SMenuBandParent: Guid = Guid('{8c278eec-3eab-11d1-8cb0-00c04fd918d0}')
SID_SMenuPopup: Guid = Guid('{d1e7afeb-6a2e-11d0-8c78-00c04fd918b4}')
SID_SMenuBandBottomSelected: Guid = Guid('{165ebaf4-6d51-11d2-83ad-00c04fd918d0}')
SID_SMenuBandBottom: Guid = Guid('{743ca664-0deb-11d1-9825-00c04fd91972}')
SID_MenuShellFolder: Guid = Guid('{a6c17eb4-2d65-11d2-838f-00c04fd918d0}')
SID_SMenuBandContextMenuModifier: Guid = Guid('{39545874-7162-465e-b783-2aa1874fef81}')
SID_SMenuBandBKContextMenu: Guid = Guid('{164bbd86-1d0d-4de0-9a3b-d9729647c2b8}')
CGID_MENUDESKBAR: Guid = Guid('{5c9f0a12-959e-11d0-a3a4-00a0c9082636}')
SID_SMenuBandTop: Guid = Guid('{9493a810-ec38-11d0-bc46-00aa006ce2f5}')
CLSID_MenuToolbarBase: Guid = Guid('{40b96610-b522-11d1-b3b4-00aa006efde7}')
CLSID_MenuBandSite: Guid = Guid('{e13ef4e4-d2f2-11d0-9816-00c04fd91972}')
SID_SCommDlgBrowser: Guid = Guid('{80f30233-b7df-11d2-a33b-006097df5bd4}')
CPFG_LOGON_USERNAME: Guid = Guid('{da15bbe8-954d-4fd3-b0f4-1fb5b90b174b}')
CPFG_LOGON_PASSWORD: Guid = Guid('{60624cfa-a477-47b1-8a8e-3a4a19981827}')
CPFG_SMARTCARD_USERNAME: Guid = Guid('{3e1ecf69-568c-4d96-9d59-46444174e2d6}')
CPFG_SMARTCARD_PIN: Guid = Guid('{4fe5263b-9181-46c1-b0a4-9dedd4db7dea}')
CPFG_CREDENTIAL_PROVIDER_LOGO: Guid = Guid('{2d837775-f6cd-464e-a745-482fd0b47493}')
CPFG_CREDENTIAL_PROVIDER_LABEL: Guid = Guid('{286bbff3-bad4-438f-b007-79b7267c3d48}')
CPFG_STANDALONE_SUBMIT_BUTTON: Guid = Guid('{0b7b0ad8-cc36-4d59-802b-82f714fa7022}')
CPFG_STYLE_LINK_AS_BUTTON: Guid = Guid('{088fa508-94a6-4430-a4cb-6fc6e3c0b9e2}')
FOLDERTYPEID_Invalid: Guid = Guid('{57807898-8c4f-4462-bb63-71042380b109}')
FOLDERTYPEID_Generic: Guid = Guid('{5c4f28b5-f869-4e84-8e60-f11db97c5cc7}')
FOLDERTYPEID_GenericSearchResults: Guid = Guid('{7fde1a1e-8b31-49a5-93b8-6be14cfa4943}')
FOLDERTYPEID_GenericLibrary: Guid = Guid('{5f4eab9a-6833-4f61-899d-31cf46979d49}')
FOLDERTYPEID_Documents: Guid = Guid('{7d49d726-3c21-4f05-99aa-fdc2c9474656}')
FOLDERTYPEID_Pictures: Guid = Guid('{b3690e58-e961-423b-b687-386ebfd83239}')
FOLDERTYPEID_Music: Guid = Guid('{94d6ddcc-4a68-4175-a374-bd584a510b78}')
FOLDERTYPEID_Videos: Guid = Guid('{5fa96407-7e77-483c-ac93-691d05850de8}')
FOLDERTYPEID_Downloads: Guid = Guid('{885a186e-a440-4ada-812b-db871b942259}')
FOLDERTYPEID_UserFiles: Guid = Guid('{cd0fc69b-71e2-46e5-9690-5bcd9f57aab3}')
FOLDERTYPEID_UsersLibraries: Guid = Guid('{c4d98f09-6124-4fe0-9942-826416082da9}')
FOLDERTYPEID_OtherUsers: Guid = Guid('{b337fd00-9dd5-4635-a6d4-da33fd102b7a}')
FOLDERTYPEID_PublishedItems: Guid = Guid('{7f2f5b96-ff74-41da-afd8-1c78a5f3aea2}')
FOLDERTYPEID_Communications: Guid = Guid('{91475fe5-586b-4eba-8d75-d17434b8cdf6}')
FOLDERTYPEID_Contacts: Guid = Guid('{de2b70ec-9bf7-4a93-bd3d-243f7881d492}')
FOLDERTYPEID_StartMenu: Guid = Guid('{ef87b4cb-f2ce-4785-8658-4ca6c63e38c6}')
FOLDERTYPEID_RecordedTV: Guid = Guid('{5557a28f-5da6-4f83-8809-c2c98a11a6fa}')
FOLDERTYPEID_SavedGames: Guid = Guid('{d0363307-28cb-4106-9f23-2956e3e5e0e7}')
FOLDERTYPEID_OpenSearch: Guid = Guid('{8faf9629-1980-46ff-8023-9dceab9c3ee3}')
FOLDERTYPEID_SearchConnector: Guid = Guid('{982725ee-6f47-479e-b447-812bfa7d2e8f}')
FOLDERTYPEID_AccountPictures: Guid = Guid('{db2a5d8f-06e6-4007-aba6-af877d526ea6}')
FOLDERTYPEID_Games: Guid = Guid('{b689b0d0-76d3-4cbb-87f7-585d0e0ce070}')
FOLDERTYPEID_ControlPanelCategory: Guid = Guid('{de4f0660-fa10-4b8f-a494-068b20b22307}')
FOLDERTYPEID_ControlPanelClassic: Guid = Guid('{0c3794f3-b545-43aa-a329-c37430c58d2a}')
FOLDERTYPEID_Printers: Guid = Guid('{2c7bbec6-c844-4a0a-91fa-cef6f59cfda1}')
FOLDERTYPEID_RecycleBin: Guid = Guid('{d6d9e004-cd87-442b-9d57-5e0aeb4f6f72}')
FOLDERTYPEID_SoftwareExplorer: Guid = Guid('{d674391b-52d9-4e07-834e-67c98610f39d}')
FOLDERTYPEID_CompressedFolder: Guid = Guid('{80213e82-bcfd-4c4f-8817-bb27601267a9}')
FOLDERTYPEID_NetworkExplorer: Guid = Guid('{25cc242b-9a7c-4f51-80e0-7a2928febe42}')
FOLDERTYPEID_Searches: Guid = Guid('{0b0ba2e3-405f-415e-a6ee-cad625207853}')
FOLDERTYPEID_SearchHome: Guid = Guid('{834d8a44-0974-4ed6-866e-f203d80b3810}')
FOLDERTYPEID_StorageProviderGeneric: Guid = Guid('{4f01ebc5-2385-41f2-a28e-2c5c91fb56e0}')
FOLDERTYPEID_StorageProviderDocuments: Guid = Guid('{dd61bd66-70e8-48dd-9655-65c5e1aac2d1}')
FOLDERTYPEID_StorageProviderPictures: Guid = Guid('{71d642a9-f2b1-42cd-ad92-eb9300c7cc0a}')
FOLDERTYPEID_StorageProviderMusic: Guid = Guid('{672ecd7e-af04-4399-875c-0290845b6247}')
FOLDERTYPEID_StorageProviderVideos: Guid = Guid('{51294da1-d7b1-485b-9e9a-17cffe33e187}')
SYNCMGR_OBJECTID_Icon: Guid = Guid('{6dbc85c3-5d07-4c72-a777-7fec78072c06}')
SYNCMGR_OBJECTID_EventStore: Guid = Guid('{4bef34b9-a786-4075-ba88-0c2b9d89a98f}')
SYNCMGR_OBJECTID_ConflictStore: Guid = Guid('{d78181f4-2389-47e4-a960-60bcc2ed930b}')
SYNCMGR_OBJECTID_BrowseContent: Guid = Guid('{57cbb584-e9b4-47ae-a120-c4df3335dee2}')
SYNCMGR_OBJECTID_ShowSchedule: Guid = Guid('{edc6f3e3-8441-4109-adf3-6c1ca0b7de47}')
SYNCMGR_OBJECTID_QueryBeforeActivate: Guid = Guid('{d882d80b-e7aa-49ed-86b7-e6e1f714cdfe}')
SYNCMGR_OBJECTID_QueryBeforeDeactivate: Guid = Guid('{a0efc282-60e0-460e-9374-ea88513cfc80}')
SYNCMGR_OBJECTID_QueryBeforeEnable: Guid = Guid('{04cbf7f0-5beb-4de1-bc90-908345c480f6}')
SYNCMGR_OBJECTID_QueryBeforeDisable: Guid = Guid('{bb5f64aa-f004-4eb5-8e4d-26751966344c}')
SYNCMGR_OBJECTID_QueryBeforeDelete: Guid = Guid('{f76c3397-afb3-45d7-a59f-5a49e905437e}')
SYNCMGR_OBJECTID_EventLinkClick: Guid = Guid('{2203bdc1-1af1-4082-8c30-28399f41384c}')
EP_NavPane: Guid = Guid('{cb316b22-25f7-42b8-8a09-540d23a43c2f}')
EP_Commands: Guid = Guid('{d9745868-ca5f-4a76-91cd-f5a129fbb076}')
EP_Commands_Organize: Guid = Guid('{72e81700-e3ec-4660-bf24-3c3b7b648806}')
EP_Commands_View: Guid = Guid('{21f7c32d-eeaa-439b-bb51-37b96fd6a943}')
EP_DetailsPane: Guid = Guid('{43abf98b-89b8-472d-b9ce-e69b8229f019}')
EP_PreviewPane: Guid = Guid('{893c63d1-45c8-4d17-be19-223be71be365}')
EP_QueryPane: Guid = Guid('{65bcde4f-4f07-4f27-83a7-1afca4df7ddd}')
EP_AdvQueryPane: Guid = Guid('{b4e9db8b-34ba-4c39-b5cc-16a1bd2c411c}')
EP_StatusBar: Guid = Guid('{65fe56ce-5cfe-4bc4-ad8a-7ae3fe7e8f7c}')
EP_Ribbon: Guid = Guid('{d27524a8-c9f2-4834-a106-df8889fd4f37}')
CATID_LocationFactory: Guid = Guid('{965c4d51-8b76-4e57-80b7-564d2ea4b55e}')
CATID_LocationProvider: Guid = Guid('{1b3ca474-2614-414b-b813-1aceca3e3dd8}')
ItemCount_Property_GUID: Guid = Guid('{abbf5c45-5ccc-47b7-bb4e-87cb87bbd162}')
SelectedItemCount_Property_GUID: Guid = Guid('{8fe316d2-0e52-460a-9c1e-48f273d470a3}')
ItemIndex_Property_GUID: Guid = Guid('{92a053da-2969-4021-bf27-514cfc2e4a69}')
CATID_SearchableApplication: Guid = Guid('{366c292a-d9b3-4dbf-bb70-e62ec3d0bbbf}')
IDD_WIZEXTN_FIRST: UInt32 = 20480
IDD_WIZEXTN_LAST: UInt32 = 20736
SHPWHF_NORECOMPRESS: UInt32 = 1
SHPWHF_NONETPLACECREATE: UInt32 = 2
SHPWHF_NOFILESELECTOR: UInt32 = 4
SHPWHF_USEMRU: UInt32 = 8
SHPWHF_ANYLOCATION: UInt32 = 256
SHPWHF_VALIDATEVIAWEBFOLDERS: UInt32 = 65536
ACDD_VISIBLE: UInt32 = 1
PROPSTR_EXTENSIONCOMPLETIONSTATE: String = 'ExtensionCompletionState'
SID_SCommandBarState: Guid = Guid('{b99eaa5c-3850-4400-bc33-2ce534048bf8}')
NSTCDHPOS_ONTOP: Int32 = -1
FVSIF_RECT: UInt32 = 1
FVSIF_PINNED: UInt32 = 2
FVSIF_NEWFAILED: UInt32 = 134217728
FVSIF_NEWFILE: UInt32 = 2147483648
FVSIF_CANVIEWIT: UInt32 = 1073741824
FCIDM_TOOLBAR: UInt32 = 40960
FCIDM_STATUS: UInt32 = 40961
IDC_OFFLINE_HAND: UInt32 = 103
IDC_PANTOOL_HAND_OPEN: UInt32 = 104
IDC_PANTOOL_HAND_CLOSED: UInt32 = 105
PANE_NONE: UInt32 = 4294967295
PANE_ZONE: UInt32 = 1
PANE_OFFLINE: UInt32 = 2
PANE_PRINTER: UInt32 = 3
PANE_SSL: UInt32 = 4
PANE_NAVIGATION: UInt32 = 5
PANE_PROGRESS: UInt32 = 6
PANE_PRIVACY: UInt32 = 7
DWFRF_NORMAL: UInt32 = 0
DWFRF_DELETECONFIGDATA: UInt32 = 1
DWFAF_HIDDEN: UInt32 = 1
DWFAF_GROUP1: UInt32 = 2
DWFAF_GROUP2: UInt32 = 4
DWFAF_AUTOHIDE: UInt32 = 16
SHIMSTCAPFLAG_LOCKABLE: UInt32 = 1
SHIMSTCAPFLAG_PURGEABLE: UInt32 = 2
ISFB_MASK_STATE: UInt32 = 1
ISFB_MASK_BKCOLOR: UInt32 = 2
ISFB_MASK_VIEWMODE: UInt32 = 4
ISFB_MASK_SHELLFOLDER: UInt32 = 8
ISFB_MASK_IDLIST: UInt32 = 16
ISFB_MASK_COLORS: UInt32 = 32
ISFB_STATE_DEFAULT: UInt32 = 0
ISFB_STATE_DEBOSSED: UInt32 = 1
ISFB_STATE_ALLOWRENAME: UInt32 = 2
ISFB_STATE_NOSHOWTEXT: UInt32 = 4
ISFB_STATE_CHANNELBAR: UInt32 = 16
ISFB_STATE_QLINKSMODE: UInt32 = 32
ISFB_STATE_FULLOPEN: UInt32 = 64
ISFB_STATE_NONAMESORT: UInt32 = 128
ISFB_STATE_BTNMINSIZE: UInt32 = 256
ISFBVIEWMODE_SMALLICONS: UInt32 = 1
ISFBVIEWMODE_LARGEICONS: UInt32 = 2
ISFBVIEWMODE_LOGOS: UInt32 = 3
DBC_GS_IDEAL: UInt32 = 0
DBC_GS_SIZEDOWN: UInt32 = 1
DBC_HIDE: UInt32 = 0
DBC_SHOW: UInt32 = 1
DBC_SHOWOBSCURE: UInt32 = 2
SSM_CLEAR: UInt32 = 0
SSM_SET: UInt32 = 1
SSM_REFRESH: UInt32 = 2
SSM_UPDATE: UInt32 = 4
SCHEME_DISPLAY: UInt32 = 1
SCHEME_EDIT: UInt32 = 2
SCHEME_LOCAL: UInt32 = 4
SCHEME_GLOBAL: UInt32 = 8
SCHEME_REFRESH: UInt32 = 16
SCHEME_UPDATE: UInt32 = 32
SCHEME_DONOTUSE: UInt32 = 64
SCHEME_CREATE: UInt32 = 128
GADOF_DIRTY: UInt32 = 1
SHCDF_UPDATEITEM: UInt32 = 1
PPCF_ADDQUOTES: UInt32 = 1
PPCF_ADDARGUMENTS: UInt32 = 3
PPCF_NODIRECTORIES: UInt32 = 16
PPCF_FORCEQUALIFY: UInt32 = 64
PPCF_LONGESTPOSSIBLE: UInt32 = 128
OPENPROPS_NONE: UInt32 = 0
OPENPROPS_INHIBITPIF: UInt32 = 32768
GETPROPS_NONE: UInt32 = 0
SETPROPS_NONE: UInt32 = 0
CLOSEPROPS_NONE: UInt32 = 0
CLOSEPROPS_DISCARD: UInt32 = 1
TBIF_APPEND: UInt32 = 0
TBIF_PREPEND: UInt32 = 1
TBIF_REPLACE: UInt32 = 2
TBIF_DEFAULT: UInt32 = 0
TBIF_INTERNETBAR: UInt32 = 65536
TBIF_STANDARDTOOLBAR: UInt32 = 131072
TBIF_NOTOOLBAR: UInt32 = 196608
SFVM_REARRANGE: UInt32 = 1
SFVM_ADDOBJECT: UInt32 = 3
SFVM_REMOVEOBJECT: UInt32 = 6
SFVM_UPDATEOBJECT: UInt32 = 7
SFVM_GETSELECTEDOBJECTS: UInt32 = 9
SFVM_SETITEMPOS: UInt32 = 14
SFVM_SETCLIPBOARD: UInt32 = 16
SFVM_SETPOINTS: UInt32 = 23
GIL_OPENICON: UInt32 = 1
GIL_FORSHELL: UInt32 = 2
GIL_ASYNC: UInt32 = 32
GIL_DEFAULTICON: UInt32 = 64
GIL_FORSHORTCUT: UInt32 = 128
GIL_CHECKSHIELD: UInt32 = 512
GIL_SIMULATEDOC: UInt32 = 1
GIL_PERINSTANCE: UInt32 = 2
GIL_PERCLASS: UInt32 = 4
GIL_NOTFILENAME: UInt32 = 8
GIL_DONTCACHE: UInt32 = 16
GIL_SHIELD: UInt32 = 512
GIL_FORCENOSHIELD: UInt32 = 1024
SIOM_OVERLAYINDEX: UInt32 = 1
SIOM_ICONINDEX: UInt32 = 2
SIOM_RESERVED_SHARED: UInt32 = 0
SIOM_RESERVED_LINK: UInt32 = 1
SIOM_RESERVED_SLOWFILE: UInt32 = 2
SIOM_RESERVED_DEFAULT: UInt32 = 3
OI_DEFAULT: UInt32 = 0
OI_ASYNC: UInt32 = 4294962926
IDO_SHGIOI_SHARE: UInt32 = 268435455
IDO_SHGIOI_LINK: UInt32 = 268435454
IDO_SHGIOI_SLOWFILE: UInt64 = 4294967293
IDO_SHGIOI_DEFAULT: UInt64 = 4294967292
NT_CONSOLE_PROPS_SIG: UInt32 = 2684354562
NT_FE_CONSOLE_PROPS_SIG: UInt32 = 2684354564
EXP_DARWIN_ID_SIG: UInt32 = 2684354566
EXP_SPECIAL_FOLDER_SIG: UInt32 = 2684354565
EXP_SZ_LINK_SIG: UInt32 = 2684354561
EXP_SZ_ICON_SIG: UInt32 = 2684354567
EXP_PROPERTYSTORAGE_SIG: UInt32 = 2684354569
FCIDM_SHVIEWFIRST: UInt32 = 0
FCIDM_SHVIEWLAST: UInt32 = 32767
FCIDM_BROWSERFIRST: UInt32 = 40960
FCIDM_BROWSERLAST: UInt32 = 48896
FCIDM_GLOBALFIRST: UInt32 = 32768
FCIDM_GLOBALLAST: UInt32 = 40959
FCIDM_MENU_FILE: UInt32 = 32768
FCIDM_MENU_EDIT: UInt32 = 32832
FCIDM_MENU_VIEW: UInt32 = 32896
FCIDM_MENU_VIEW_SEP_OPTIONS: UInt32 = 32897
FCIDM_MENU_TOOLS: UInt32 = 32960
FCIDM_MENU_TOOLS_SEP_GOTO: UInt32 = 32961
FCIDM_MENU_HELP: UInt32 = 33024
FCIDM_MENU_FIND: UInt32 = 33088
FCIDM_MENU_EXPLORE: UInt32 = 33104
FCIDM_MENU_FAVORITES: UInt32 = 33136
OFASI_EDIT: UInt32 = 1
OFASI_OPENDESKTOP: UInt32 = 2
CSIDL_DESKTOP: UInt32 = 0
CSIDL_INTERNET: UInt32 = 1
CSIDL_PROGRAMS: UInt32 = 2
CSIDL_CONTROLS: UInt32 = 3
CSIDL_PRINTERS: UInt32 = 4
CSIDL_PERSONAL: UInt32 = 5
CSIDL_FAVORITES: UInt32 = 6
CSIDL_STARTUP: UInt32 = 7
CSIDL_RECENT: UInt32 = 8
CSIDL_SENDTO: UInt32 = 9
CSIDL_BITBUCKET: UInt32 = 10
CSIDL_STARTMENU: UInt32 = 11
CSIDL_MYDOCUMENTS: UInt32 = 5
CSIDL_MYMUSIC: UInt32 = 13
CSIDL_MYVIDEO: UInt32 = 14
CSIDL_DESKTOPDIRECTORY: UInt32 = 16
CSIDL_DRIVES: UInt32 = 17
CSIDL_NETWORK: UInt32 = 18
CSIDL_NETHOOD: UInt32 = 19
CSIDL_FONTS: UInt32 = 20
CSIDL_TEMPLATES: UInt32 = 21
CSIDL_COMMON_STARTMENU: UInt32 = 22
CSIDL_COMMON_PROGRAMS: UInt32 = 23
CSIDL_COMMON_STARTUP: UInt32 = 24
CSIDL_COMMON_DESKTOPDIRECTORY: UInt32 = 25
CSIDL_APPDATA: UInt32 = 26
CSIDL_PRINTHOOD: UInt32 = 27
CSIDL_LOCAL_APPDATA: UInt32 = 28
CSIDL_ALTSTARTUP: UInt32 = 29
CSIDL_COMMON_ALTSTARTUP: UInt32 = 30
CSIDL_COMMON_FAVORITES: UInt32 = 31
CSIDL_INTERNET_CACHE: UInt32 = 32
CSIDL_COOKIES: UInt32 = 33
CSIDL_HISTORY: UInt32 = 34
CSIDL_COMMON_APPDATA: UInt32 = 35
CSIDL_WINDOWS: UInt32 = 36
CSIDL_SYSTEM: UInt32 = 37
CSIDL_PROGRAM_FILES: UInt32 = 38
CSIDL_MYPICTURES: UInt32 = 39
CSIDL_PROFILE: UInt32 = 40
CSIDL_SYSTEMX86: UInt32 = 41
CSIDL_PROGRAM_FILESX86: UInt32 = 42
CSIDL_PROGRAM_FILES_COMMON: UInt32 = 43
CSIDL_PROGRAM_FILES_COMMONX86: UInt32 = 44
CSIDL_COMMON_TEMPLATES: UInt32 = 45
CSIDL_COMMON_DOCUMENTS: UInt32 = 46
CSIDL_COMMON_ADMINTOOLS: UInt32 = 47
CSIDL_ADMINTOOLS: UInt32 = 48
CSIDL_CONNECTIONS: UInt32 = 49
CSIDL_COMMON_MUSIC: UInt32 = 53
CSIDL_COMMON_PICTURES: UInt32 = 54
CSIDL_COMMON_VIDEO: UInt32 = 55
CSIDL_RESOURCES: UInt32 = 56
CSIDL_RESOURCES_LOCALIZED: UInt32 = 57
CSIDL_COMMON_OEM_LINKS: UInt32 = 58
CSIDL_CDBURN_AREA: UInt32 = 59
CSIDL_COMPUTERSNEARME: UInt32 = 61
CSIDL_FLAG_CREATE: UInt32 = 32768
CSIDL_FLAG_DONT_VERIFY: UInt32 = 16384
CSIDL_FLAG_DONT_UNEXPAND: UInt32 = 8192
CSIDL_FLAG_NO_ALIAS: UInt32 = 4096
CSIDL_FLAG_PER_USER_INIT: UInt32 = 2048
CSIDL_FLAG_MASK: UInt32 = 65280
FCS_READ: UInt32 = 1
FCS_FORCEWRITE: UInt32 = 2
FCS_FLAG_DRAGDROP: UInt32 = 2
FCSM_VIEWID: UInt32 = 1
FCSM_WEBVIEWTEMPLATE: UInt32 = 2
FCSM_INFOTIP: UInt32 = 4
FCSM_CLSID: UInt32 = 8
FCSM_ICONFILE: UInt32 = 16
FCSM_LOGO: UInt32 = 32
FCSM_FLAGS: UInt32 = 64
BIF_RETURNONLYFSDIRS: UInt32 = 1
BIF_DONTGOBELOWDOMAIN: UInt32 = 2
BIF_STATUSTEXT: UInt32 = 4
BIF_RETURNFSANCESTORS: UInt32 = 8
BIF_EDITBOX: UInt32 = 16
BIF_VALIDATE: UInt32 = 32
BIF_NEWDIALOGSTYLE: UInt32 = 64
BIF_BROWSEINCLUDEURLS: UInt32 = 128
BIF_UAHINT: UInt32 = 256
BIF_NONEWFOLDERBUTTON: UInt32 = 512
BIF_NOTRANSLATETARGETS: UInt32 = 1024
BIF_BROWSEFORCOMPUTER: UInt32 = 4096
BIF_BROWSEFORPRINTER: UInt32 = 8192
BIF_BROWSEINCLUDEFILES: UInt32 = 16384
BIF_SHAREABLE: UInt32 = 32768
BIF_BROWSEFILEJUNCTIONS: UInt32 = 65536
BFFM_INITIALIZED: UInt32 = 1
BFFM_SELCHANGED: UInt32 = 2
BFFM_VALIDATEFAILEDA: UInt32 = 3
BFFM_VALIDATEFAILEDW: UInt32 = 4
BFFM_IUNKNOWN: UInt32 = 5
BFFM_SETSTATUSTEXTA: UInt32 = 1124
BFFM_ENABLEOK: UInt32 = 1125
BFFM_SETSELECTIONA: UInt32 = 1126
BFFM_SETSELECTIONW: UInt32 = 1127
BFFM_SETSTATUSTEXTW: UInt32 = 1128
BFFM_SETOKTEXT: UInt32 = 1129
BFFM_SETEXPANDED: UInt32 = 1130
BFFM_SETSTATUSTEXT: UInt32 = 1128
BFFM_SETSELECTION: UInt32 = 1127
BFFM_VALIDATEFAILED: UInt32 = 4
CMDID_INTSHORTCUTCREATE: Int32 = 1
STR_PARSE_WITH_PROPERTIES: String = 'ParseWithProperties'
STR_PARSE_PARTIAL_IDLIST: String = 'ParseOriginalItem'
PROGDLG_NORMAL: UInt32 = 0
PROGDLG_MODAL: UInt32 = 1
PROGDLG_AUTOTIME: UInt32 = 2
PROGDLG_NOTIME: UInt32 = 4
PROGDLG_NOMINIMIZE: UInt32 = 8
PROGDLG_NOPROGRESSBAR: UInt32 = 16
PROGDLG_MARQUEEPROGRESS: UInt32 = 32
PROGDLG_NOCANCEL: UInt32 = 64
PDTIMER_RESET: UInt32 = 1
PDTIMER_PAUSE: UInt32 = 2
PDTIMER_RESUME: UInt32 = 3
COMPONENT_TOP: UInt32 = 1073741823
COMP_TYPE_HTMLDOC: UInt32 = 0
COMP_TYPE_PICTURE: UInt32 = 1
COMP_TYPE_WEBSITE: UInt32 = 2
COMP_TYPE_CONTROL: UInt32 = 3
COMP_TYPE_CFHTML: UInt32 = 4
COMP_TYPE_MAX: UInt32 = 4
IS_NORMAL: UInt32 = 1
IS_FULLSCREEN: UInt32 = 2
IS_SPLIT: UInt32 = 4
AD_APPLY_SAVE: UInt32 = 1
AD_APPLY_HTMLGEN: UInt32 = 2
AD_APPLY_REFRESH: UInt32 = 4
AD_APPLY_FORCE: UInt32 = 8
AD_APPLY_BUFFERED_REFRESH: UInt32 = 16
AD_APPLY_DYNAMICREFRESH: UInt32 = 32
AD_GETWP_BMP: UInt32 = 0
AD_GETWP_IMAGE: UInt32 = 1
AD_GETWP_LAST_APPLIED: UInt32 = 2
WPSTYLE_CENTER: UInt32 = 0
WPSTYLE_TILE: UInt32 = 1
WPSTYLE_STRETCH: UInt32 = 2
WPSTYLE_KEEPASPECT: UInt32 = 3
WPSTYLE_CROPTOFIT: UInt32 = 4
WPSTYLE_SPAN: UInt32 = 5
WPSTYLE_MAX: UInt32 = 6
COMP_ELEM_TYPE: UInt32 = 1
COMP_ELEM_CHECKED: UInt32 = 2
COMP_ELEM_DIRTY: UInt32 = 4
COMP_ELEM_NOSCROLL: UInt32 = 8
COMP_ELEM_POS_LEFT: UInt32 = 16
COMP_ELEM_POS_TOP: UInt32 = 32
COMP_ELEM_SIZE_WIDTH: UInt32 = 64
COMP_ELEM_SIZE_HEIGHT: UInt32 = 128
COMP_ELEM_POS_ZINDEX: UInt32 = 256
COMP_ELEM_SOURCE: UInt32 = 512
COMP_ELEM_FRIENDLYNAME: UInt32 = 1024
COMP_ELEM_SUBSCRIBEDURL: UInt32 = 2048
COMP_ELEM_ORIGINAL_CSI: UInt32 = 4096
COMP_ELEM_RESTORED_CSI: UInt32 = 8192
COMP_ELEM_CURITEMSTATE: UInt32 = 16384
ADDURL_SILENT: UInt32 = 1
COMPONENT_DEFAULT_LEFT: UInt32 = 65535
COMPONENT_DEFAULT_TOP: UInt32 = 65535
MAX_COLUMN_NAME_LEN: UInt32 = 80
MAX_COLUMN_DESC_LEN: UInt32 = 128
CFSTR_SHELLIDLIST: String = 'Shell IDList Array'
CFSTR_SHELLIDLISTOFFSET: String = 'Shell Object Offsets'
CFSTR_NETRESOURCES: String = 'Net Resource'
CFSTR_FILEDESCRIPTORA: String = 'FileGroupDescriptor'
CFSTR_FILEDESCRIPTORW: String = 'FileGroupDescriptorW'
CFSTR_FILECONTENTS: String = 'FileContents'
CFSTR_FILENAMEA: String = 'FileName'
CFSTR_FILENAMEW: String = 'FileNameW'
CFSTR_PRINTERGROUP: String = 'PrinterFriendlyName'
CFSTR_FILENAMEMAPA: String = 'FileNameMap'
CFSTR_FILENAMEMAPW: String = 'FileNameMapW'
CFSTR_SHELLURL: String = 'UniformResourceLocator'
CFSTR_INETURLA: String = 'UniformResourceLocator'
CFSTR_INETURLW: String = 'UniformResourceLocatorW'
CFSTR_PREFERREDDROPEFFECT: String = 'Preferred DropEffect'
CFSTR_PERFORMEDDROPEFFECT: String = 'Performed DropEffect'
CFSTR_PASTESUCCEEDED: String = 'Paste Succeeded'
CFSTR_INDRAGLOOP: String = 'InShellDragLoop'
CFSTR_MOUNTEDVOLUME: String = 'MountedVolume'
CFSTR_PERSISTEDDATAOBJECT: String = 'PersistedDataObject'
CFSTR_TARGETCLSID: String = 'TargetCLSID'
CFSTR_LOGICALPERFORMEDDROPEFFECT: String = 'Logical Performed DropEffect'
CFSTR_AUTOPLAY_SHELLIDLISTS: String = 'Autoplay Enumerated IDList Array'
CFSTR_UNTRUSTEDDRAGDROP: String = 'UntrustedDragDrop'
CFSTR_FILE_ATTRIBUTES_ARRAY: String = 'File Attributes Array'
CFSTR_INVOKECOMMAND_DROPPARAM: String = 'InvokeCommand DropParam'
CFSTR_SHELLDROPHANDLER: String = 'DropHandlerCLSID'
CFSTR_DROPDESCRIPTION: String = 'DropDescription'
CFSTR_ZONEIDENTIFIER: String = 'ZoneIdentifier'
CFSTR_FILEDESCRIPTOR: String = 'FileGroupDescriptorW'
CFSTR_FILENAME: String = 'FileNameW'
CFSTR_FILENAMEMAP: String = 'FileNameMapW'
CFSTR_INETURL: String = 'UniformResourceLocatorW'
DVASPECT_SHORTNAME: UInt32 = 2
DVASPECT_COPY: UInt32 = 3
DVASPECT_LINK: UInt32 = 4
SHCNEE_ORDERCHANGED: Int32 = 2
SHCNEE_MSI_CHANGE: Int32 = 4
SHCNEE_MSI_UNINSTALL: Int32 = 5
NUM_POINTS: UInt32 = 3
CABINETSTATE_VERSION: UInt32 = 2
PIFNAMESIZE: UInt32 = 30
PIFSTARTLOCSIZE: UInt32 = 63
PIFDEFPATHSIZE: UInt32 = 64
PIFPARAMSSIZE: UInt32 = 64
PIFSHPROGSIZE: UInt32 = 64
PIFSHDATASIZE: UInt32 = 64
PIFDEFFILESIZE: UInt32 = 80
PIFMAXFILEPATH: UInt32 = 260
QCMINFO_PLACE_BEFORE: UInt32 = 0
QCMINFO_PLACE_AFTER: UInt32 = 1
SFVSOC_INVALIDATE_ALL: UInt32 = 1
SFVSOC_NOSCROLL: UInt32 = 2
SHELLSTATEVERSION_IE4: UInt32 = 9
SHELLSTATEVERSION_WIN2K: UInt32 = 10
SHPPFW_NONE: UInt32 = 0
SHPPFW_DIRCREATE: UInt32 = 1
SHPPFW_ASKDIRCREATE: UInt32 = 2
SHPPFW_IGNOREFILENAME: UInt32 = 4
SHPPFW_NOWRITECHECK: UInt32 = 8
SHPPFW_MEDIACHECKONLY: UInt32 = 16
CMF_NORMAL: UInt32 = 0
CMF_DEFAULTONLY: UInt32 = 1
CMF_VERBSONLY: UInt32 = 2
CMF_EXPLORE: UInt32 = 4
CMF_NOVERBS: UInt32 = 8
CMF_CANRENAME: UInt32 = 16
CMF_NODEFAULT: UInt32 = 32
CMF_INCLUDESTATIC: UInt32 = 64
CMF_ITEMMENU: UInt32 = 128
CMF_EXTENDEDVERBS: UInt32 = 256
CMF_DISABLEDVERBS: UInt32 = 512
CMF_ASYNCVERBSTATE: UInt32 = 1024
CMF_OPTIMIZEFORINVOKE: UInt32 = 2048
CMF_SYNCCASCADEMENU: UInt32 = 4096
CMF_DONOTPICKDEFAULT: UInt32 = 8192
CMF_RESERVED: UInt32 = 4294901760
GCS_VERBA: UInt32 = 0
GCS_HELPTEXTA: UInt32 = 1
GCS_VALIDATEA: UInt32 = 2
GCS_VERBW: UInt32 = 4
GCS_HELPTEXTW: UInt32 = 5
GCS_VALIDATEW: UInt32 = 6
GCS_VERBICONW: UInt32 = 20
GCS_UNICODE: UInt32 = 4
GCS_VERB: UInt32 = 4
GCS_HELPTEXT: UInt32 = 5
GCS_VALIDATE: UInt32 = 6
CMDSTR_NEWFOLDERA: String = 'NewFolder'
CMDSTR_VIEWLISTA: String = 'ViewList'
CMDSTR_VIEWDETAILSA: String = 'ViewDetails'
CMDSTR_NEWFOLDERW: String = 'NewFolder'
CMDSTR_VIEWLISTW: String = 'ViewList'
CMDSTR_VIEWDETAILSW: String = 'ViewDetails'
CMDSTR_NEWFOLDER: String = 'NewFolder'
CMDSTR_VIEWLIST: String = 'ViewList'
CMDSTR_VIEWDETAILS: String = 'ViewDetails'
CMIC_MASK_SHIFT_DOWN: UInt32 = 268435456
CMIC_MASK_CONTROL_DOWN: UInt32 = 1073741824
CMIC_MASK_PTINVOKE: UInt32 = 536870912
IRTIR_TASK_NOT_RUNNING: UInt32 = 0
IRTIR_TASK_RUNNING: UInt32 = 1
IRTIR_TASK_SUSPENDED: UInt32 = 2
IRTIR_TASK_PENDING: UInt32 = 3
IRTIR_TASK_FINISHED: UInt32 = 4
ITSAT_DEFAULT_PRIORITY: UInt32 = 268435456
ITSAT_MAX_PRIORITY: UInt32 = 2147483647
ITSAT_MIN_PRIORITY: UInt32 = 0
ITSSFLAG_COMPLETE_ON_DESTROY: UInt32 = 0
ITSSFLAG_KILL_ON_DESTROY: UInt32 = 1
ITSSFLAG_FLAGS_MASK: UInt32 = 3
ITSS_THREAD_TIMEOUT_NO_CHANGE: UInt32 = 4294967294
CSIDL_FLAG_PFTI_TRACKTARGET: UInt32 = 16384
SHCIDS_ALLFIELDS: Int32 = -2147483648
SHCIDS_CANONICALONLY: Int32 = 268435456
SHCIDS_BITMASK: Int32 = -65536
SHCIDS_COLUMNMASK: Int32 = 65535
CONFLICT_RESOLUTION_CLSID_KEY: String = 'ConflictResolutionCLSID'
STR_BIND_FORCE_FOLDER_SHORTCUT_RESOLVE: String = 'Force Folder Shortcut Resolve'
STR_AVOID_DRIVE_RESTRICTION_POLICY: String = 'Avoid Drive Restriction Policy'
STR_SKIP_BINDING_CLSID: String = 'Skip Binding CLSID'
STR_PARSE_PREFER_FOLDER_BROWSING: String = 'Parse Prefer Folder Browsing'
STR_DONT_PARSE_RELATIVE: String = "Don't Parse Relative"
STR_PARSE_TRANSLATE_ALIASES: String = 'Parse Translate Aliases'
STR_PARSE_SKIP_NET_CACHE: String = 'Skip Net Resource Cache'
STR_PARSE_SHELL_PROTOCOL_TO_FILE_OBJECTS: String = 'Parse Shell Protocol To File Objects'
STR_TRACK_CLSID: String = 'Track the CLSID'
STR_INTERNAL_NAVIGATE: String = 'Internal Navigation'
STR_PARSE_PROPERTYSTORE: String = 'DelegateNamedProperties'
STR_NO_VALIDATE_FILENAME_CHARS: String = 'NoValidateFilenameChars'
STR_BIND_DELEGATE_CREATE_OBJECT: String = 'Delegate Object Creation'
STR_PARSE_ALLOW_INTERNET_SHELL_FOLDERS: String = 'Allow binding to Internet shell folder handlers and negate STR_PARSE_PREFER_WEB_BROWSING'
STR_PARSE_PREFER_WEB_BROWSING: String = 'Do not bind to Internet shell folder handlers'
STR_PARSE_SHOW_NET_DIAGNOSTICS_UI: String = 'Show network diagnostics UI'
STR_PARSE_DONT_REQUIRE_VALIDATED_URLS: String = 'Do not require validated URLs'
STR_INTERNETFOLDER_PARSE_ONLY_URLMON_BINDABLE: String = 'Validate URL'
BIND_INTERRUPTABLE: UInt32 = 4294967295
STR_BIND_FOLDERS_READ_ONLY: String = 'Folders As Read Only'
STR_BIND_FOLDER_ENUM_MODE: String = 'Folder Enum Mode'
STR_PARSE_WITH_EXPLICIT_PROGID: String = 'ExplicitProgid'
STR_PARSE_WITH_EXPLICIT_ASSOCAPP: String = 'ExplicitAssociationApp'
STR_PARSE_EXPLICIT_ASSOCIATION_SUCCESSFUL: String = 'ExplicitAssociationSuccessful'
STR_PARSE_AND_CREATE_ITEM: String = 'ParseAndCreateItem'
STR_PROPERTYBAG_PARAM: String = 'SHBindCtxPropertyBag'
STR_ENUM_ITEMS_FLAGS: String = 'SHCONTF'
STR_STORAGEITEM_CREATION_FLAGS: String = 'SHGETSTORAGEITEM'
STR_ITEM_CACHE_CONTEXT: String = 'ItemCacheContext'
CDBOSC_SETFOCUS: UInt32 = 0
CDBOSC_KILLFOCUS: UInt32 = 1
CDBOSC_SELCHANGE: UInt32 = 2
CDBOSC_RENAME: UInt32 = 3
CDBOSC_STATECHANGE: UInt32 = 4
CDB2N_CONTEXTMENU_DONE: UInt32 = 1
CDB2N_CONTEXTMENU_START: UInt32 = 2
CDB2GVF_SHOWALLFILES: UInt32 = 1
CDB2GVF_ISFILESAVE: UInt32 = 2
CDB2GVF_ALLOWPREVIEWPANE: UInt32 = 4
CDB2GVF_NOSELECTVERB: UInt32 = 8
CDB2GVF_NOINCLUDEITEM: UInt32 = 16
CDB2GVF_ISFOLDERPICKER: UInt32 = 32
CDB2GVF_ADDSHIELD: UInt32 = 64
SBSP_DEFBROWSER: UInt32 = 0
SBSP_SAMEBROWSER: UInt32 = 1
SBSP_NEWBROWSER: UInt32 = 2
SBSP_DEFMODE: UInt32 = 0
SBSP_OPENMODE: UInt32 = 16
SBSP_EXPLOREMODE: UInt32 = 32
SBSP_HELPMODE: UInt32 = 64
SBSP_NOTRANSFERHIST: UInt32 = 128
SBSP_ABSOLUTE: UInt32 = 0
SBSP_RELATIVE: UInt32 = 4096
SBSP_PARENT: UInt32 = 8192
SBSP_NAVIGATEBACK: UInt32 = 16384
SBSP_NAVIGATEFORWARD: UInt32 = 32768
SBSP_ALLOW_AUTONAVIGATE: UInt32 = 65536
SBSP_KEEPSAMETEMPLATE: UInt32 = 131072
SBSP_KEEPWORDWHEELTEXT: UInt32 = 262144
SBSP_ACTIVATE_NOFOCUS: UInt32 = 524288
SBSP_CREATENOHISTORY: UInt32 = 1048576
SBSP_PLAYNOSOUND: UInt32 = 2097152
SBSP_CALLERUNTRUSTED: UInt32 = 8388608
SBSP_TRUSTFIRSTDOWNLOAD: UInt32 = 16777216
SBSP_UNTRUSTEDFORDOWNLOAD: UInt32 = 33554432
SBSP_NOAUTOSELECT: UInt32 = 67108864
SBSP_WRITENOHISTORY: UInt32 = 134217728
SBSP_TRUSTEDFORACTIVEX: UInt32 = 268435456
SBSP_FEEDNAVIGATION: UInt32 = 536870912
SBSP_REDIRECT: UInt32 = 1073741824
SBSP_INITIATEDBYHLINKFRAME: UInt32 = 2147483648
FCW_STATUS: UInt32 = 1
FCW_TOOLBAR: UInt32 = 2
FCW_TREE: UInt32 = 3
FCW_INTERNETBAR: UInt32 = 6
FCW_PROGRESS: UInt32 = 8
FCT_MERGE: UInt32 = 1
FCT_CONFIGABLE: UInt32 = 2
FCT_ADDTOEND: UInt32 = 4
STR_DONT_RESOLVE_LINK: String = "Don't Resolve Link"
STR_GET_ASYNC_HANDLER: String = 'GetAsyncHandler'
STR_GPS_HANDLERPROPERTIESONLY: String = 'GPS_HANDLERPROPERTIESONLY'
STR_GPS_FASTPROPERTIESONLY: String = 'GPS_FASTPROPERTIESONLY'
STR_GPS_OPENSLOWITEM: String = 'GPS_OPENSLOWITEM'
STR_GPS_DELAYCREATION: String = 'GPS_DELAYCREATION'
STR_GPS_BESTEFFORT: String = 'GPS_BESTEFFORT'
STR_GPS_NO_OPLOCK: String = 'GPS_NO_OPLOCK'
DI_GETDRAGIMAGE: String = 'ShellGetDragImage'
ARCONTENT_AUTORUNINF: UInt32 = 2
ARCONTENT_AUDIOCD: UInt32 = 4
ARCONTENT_DVDMOVIE: UInt32 = 8
ARCONTENT_BLANKCD: UInt32 = 16
ARCONTENT_BLANKDVD: UInt32 = 32
ARCONTENT_UNKNOWNCONTENT: UInt32 = 64
ARCONTENT_AUTOPLAYPIX: UInt32 = 128
ARCONTENT_AUTOPLAYMUSIC: UInt32 = 256
ARCONTENT_AUTOPLAYVIDEO: UInt32 = 512
ARCONTENT_VCD: UInt32 = 1024
ARCONTENT_SVCD: UInt32 = 2048
ARCONTENT_DVDAUDIO: UInt32 = 4096
ARCONTENT_BLANKBD: UInt32 = 8192
ARCONTENT_BLURAY: UInt32 = 16384
ARCONTENT_CAMERASTORAGE: UInt32 = 32768
ARCONTENT_CUSTOMEVENT: UInt32 = 65536
ARCONTENT_NONE: UInt32 = 0
ARCONTENT_MASK: UInt32 = 131070
ARCONTENT_PHASE_UNKNOWN: UInt32 = 0
ARCONTENT_PHASE_PRESNIFF: UInt32 = 268435456
ARCONTENT_PHASE_SNIFFING: UInt32 = 536870912
ARCONTENT_PHASE_FINAL: UInt32 = 1073741824
ARCONTENT_PHASE_MASK: UInt32 = 1879048192
IEI_PRIORITY_MAX: UInt32 = 2147483647
IEI_PRIORITY_MIN: UInt32 = 0
IEIT_PRIORITY_NORMAL: UInt32 = 268435456
IEIFLAG_ASYNC: UInt32 = 1
IEIFLAG_CACHE: UInt32 = 2
IEIFLAG_ASPECT: UInt32 = 4
IEIFLAG_OFFLINE: UInt32 = 8
IEIFLAG_GLEAM: UInt32 = 16
IEIFLAG_SCREEN: UInt32 = 32
IEIFLAG_ORIGSIZE: UInt32 = 64
IEIFLAG_NOSTAMP: UInt32 = 128
IEIFLAG_NOBORDER: UInt32 = 256
IEIFLAG_QUALITY: UInt32 = 512
IEIFLAG_REFRESH: UInt32 = 1024
DBIM_MINSIZE: UInt32 = 1
DBIM_MAXSIZE: UInt32 = 2
DBIM_INTEGRAL: UInt32 = 4
DBIM_ACTUAL: UInt32 = 8
DBIM_TITLE: UInt32 = 16
DBIM_MODEFLAGS: UInt32 = 32
DBIM_BKCOLOR: UInt32 = 64
DBIMF_NORMAL: UInt32 = 0
DBIMF_FIXED: UInt32 = 1
DBIMF_FIXEDBMP: UInt32 = 4
DBIMF_VARIABLEHEIGHT: UInt32 = 8
DBIMF_UNDELETEABLE: UInt32 = 16
DBIMF_DEBOSSED: UInt32 = 32
DBIMF_BKCOLOR: UInt32 = 64
DBIMF_USECHEVRON: UInt32 = 128
DBIMF_BREAK: UInt32 = 256
DBIMF_ADDTOFRONT: UInt32 = 512
DBIMF_TOPALIGN: UInt32 = 1024
DBIMF_NOGRIPPER: UInt32 = 2048
DBIMF_ALWAYSGRIPPER: UInt32 = 4096
DBIMF_NOMARGINS: UInt32 = 8192
DBIF_VIEWMODE_NORMAL: UInt32 = 0
DBIF_VIEWMODE_VERTICAL: UInt32 = 1
DBIF_VIEWMODE_FLOATING: UInt32 = 2
DBIF_VIEWMODE_TRANSPARENT: UInt32 = 4
DBPC_SELECTFIRST: UInt32 = 4294967295
THBN_CLICKED: UInt32 = 6144
BSIM_STATE: UInt32 = 1
BSIM_STYLE: UInt32 = 2
BSSF_VISIBLE: UInt32 = 1
BSSF_NOTITLE: UInt32 = 2
BSSF_UNDELETEABLE: UInt32 = 4096
BSIS_AUTOGRIPPER: UInt32 = 0
BSIS_NOGRIPPER: UInt32 = 1
BSIS_ALWAYSGRIPPER: UInt32 = 2
BSIS_LEFTALIGN: UInt32 = 4
BSIS_SINGLECLICK: UInt32 = 8
BSIS_NOCONTEXTMENU: UInt32 = 16
BSIS_NODROPTARGET: UInt32 = 32
BSIS_NOCAPTION: UInt32 = 64
BSIS_PREFERNOLINEBREAK: UInt32 = 128
BSIS_LOCKED: UInt32 = 256
BSIS_PRESERVEORDERDURINGLAYOUT: UInt32 = 512
BSIS_FIXEDORDER: UInt32 = 1024
OF_CAP_CANSWITCHTO: UInt32 = 1
OF_CAP_CANCLOSE: UInt32 = 2
SMDM_SHELLFOLDER: UInt32 = 1
SMDM_HMENU: UInt32 = 2
SMDM_TOOLBAR: UInt32 = 4
SMC_INITMENU: UInt32 = 1
SMC_CREATE: UInt32 = 2
SMC_EXITMENU: UInt32 = 3
SMC_GETINFO: UInt32 = 5
SMC_GETSFINFO: UInt32 = 6
SMC_GETOBJECT: UInt32 = 7
SMC_GETSFOBJECT: UInt32 = 8
SMC_SFEXEC: UInt32 = 9
SMC_SFSELECTITEM: UInt32 = 10
SMC_REFRESH: UInt32 = 16
SMC_DEMOTE: UInt32 = 17
SMC_PROMOTE: UInt32 = 18
SMC_DEFAULTICON: UInt32 = 22
SMC_NEWITEM: UInt32 = 23
SMC_CHEVRONEXPAND: UInt32 = 25
SMC_DISPLAYCHEVRONTIP: UInt32 = 42
SMC_SETSFOBJECT: UInt32 = 45
SMC_SHCHANGENOTIFY: UInt32 = 46
SMC_CHEVRONGETTIP: UInt32 = 47
SMC_SFDDRESTRICTED: UInt32 = 48
SMC_SFEXEC_MIDDLE: UInt32 = 49
SMC_GETAUTOEXPANDSTATE: UInt32 = 65
SMC_AUTOEXPANDCHANGE: UInt32 = 66
SMC_GETCONTEXTMENUMODIFIER: UInt32 = 67
SMC_GETBKCONTEXTMENU: UInt32 = 68
SMC_OPEN: UInt32 = 69
SMAE_EXPANDED: UInt32 = 1
SMAE_CONTRACTED: UInt32 = 2
SMAE_USER: UInt32 = 4
SMAE_VALID: UInt32 = 7
SMINIT_DEFAULT: UInt32 = 0
SMINIT_RESTRICT_DRAGDROP: UInt32 = 2
SMINIT_TOPLEVEL: UInt32 = 4
SMINIT_CACHED: UInt32 = 16
SMINIT_AUTOEXPAND: UInt32 = 256
SMINIT_AUTOTOOLTIP: UInt32 = 512
SMINIT_DROPONCONTAINER: UInt32 = 1024
SMINIT_VERTICAL: UInt32 = 268435456
SMINIT_HORIZONTAL: UInt32 = 536870912
SMSET_TOP: UInt32 = 268435456
SMSET_BOTTOM: UInt32 = 536870912
SMSET_DONTOWN: UInt32 = 1
SMINV_REFRESH: UInt32 = 1
SMINV_ID: UInt32 = 8
E_PREVIEWHANDLER_DRM_FAIL: win32more.Windows.Win32.Foundation.HRESULT = -2042494975
E_PREVIEWHANDLER_NOAUTH: win32more.Windows.Win32.Foundation.HRESULT = -2042494974
E_PREVIEWHANDLER_NOTFOUND: win32more.Windows.Win32.Foundation.HRESULT = -2042494973
E_PREVIEWHANDLER_CORRUPT: win32more.Windows.Win32.Foundation.HRESULT = -2042494972
STR_FILE_SYS_BIND_DATA: String = 'File System Bind Data'
STR_FILE_SYS_BIND_DATA_WIN7_FORMAT: String = 'Win7FileSystemIdList'
HOMEGROUP_SECURITY_GROUP_MULTI: String = 'HUG'
HOMEGROUP_SECURITY_GROUP: String = 'HomeUsers'
PROP_CONTRACT_DELEGATE: String = 'ContractDelegate'
SID_URLExecutionContext: Guid = Guid('{fb5f8ebc-bbb6-4d10-a461-777291a09030}')
STR_TAB_REUSE_IDENTIFIER: String = 'Tab Reuse Identifier'
STR_REFERRER_IDENTIFIER: String = 'Referrer Identifier'
SID_LaunchSourceViewSizePreference: Guid = Guid('{80605492-67d9-414f-af89-a1cdf1242bc1}')
SID_LaunchTargetViewSizePreference: Guid = Guid('{26db2472-b7b7-406b-9702-730a4e20d3bf}')
SID_LaunchSourceAppUserModelId: Guid = Guid('{2ce78010-74db-48bc-9c6a-10f372495723}')
SID_ShellExecuteNamedPropertyStore: Guid = Guid('{eb84ada2-00ff-4992-8324-ed5ce061cb29}')
ISIOI_ICONFILE: UInt32 = 1
ISIOI_ICONINDEX: UInt32 = 2
ABM_NEW: UInt32 = 0
ABM_REMOVE: UInt32 = 1
ABM_QUERYPOS: UInt32 = 2
ABM_SETPOS: UInt32 = 3
ABM_GETSTATE: UInt32 = 4
ABM_GETTASKBARPOS: UInt32 = 5
ABM_ACTIVATE: UInt32 = 6
ABM_GETAUTOHIDEBAR: UInt32 = 7
ABM_SETAUTOHIDEBAR: UInt32 = 8
ABM_WINDOWPOSCHANGED: UInt32 = 9
ABM_SETSTATE: UInt32 = 10
ABM_GETAUTOHIDEBAREX: UInt32 = 11
ABM_SETAUTOHIDEBAREX: UInt32 = 12
ABN_STATECHANGE: UInt32 = 0
ABN_POSCHANGED: UInt32 = 1
ABN_FULLSCREENAPP: UInt32 = 2
ABN_WINDOWARRANGE: UInt32 = 3
ABS_AUTOHIDE: UInt32 = 1
ABS_ALWAYSONTOP: UInt32 = 2
ABE_LEFT: UInt32 = 0
ABE_TOP: UInt32 = 1
ABE_RIGHT: UInt32 = 2
ABE_BOTTOM: UInt32 = 3
FO_MOVE: UInt32 = 1
FO_COPY: UInt32 = 2
FO_DELETE: UInt32 = 3
FO_RENAME: UInt32 = 4
PO_DELETE: UInt32 = 19
PO_RENAME: UInt32 = 20
PO_PORTCHANGE: UInt32 = 32
PO_REN_PORT: UInt32 = 52
SE_ERR_FNF: UInt32 = 2
SE_ERR_PNF: UInt32 = 3
SE_ERR_ACCESSDENIED: UInt32 = 5
SE_ERR_OOM: UInt32 = 8
SE_ERR_DLLNOTFOUND: UInt32 = 32
SE_ERR_SHARE: UInt32 = 26
SE_ERR_ASSOCINCOMPLETE: UInt32 = 27
SE_ERR_DDETIMEOUT: UInt32 = 28
SE_ERR_DDEFAIL: UInt32 = 29
SE_ERR_DDEBUSY: UInt32 = 30
SE_ERR_NOASSOC: UInt32 = 31
SEE_MASK_DEFAULT: UInt32 = 0
SEE_MASK_CLASSNAME: UInt32 = 1
SEE_MASK_CLASSKEY: UInt32 = 3
SEE_MASK_IDLIST: UInt32 = 4
SEE_MASK_INVOKEIDLIST: UInt32 = 12
SEE_MASK_ICON: UInt32 = 16
SEE_MASK_HOTKEY: UInt32 = 32
SEE_MASK_NOCLOSEPROCESS: UInt32 = 64
SEE_MASK_CONNECTNETDRV: UInt32 = 128
SEE_MASK_NOASYNC: UInt32 = 256
SEE_MASK_FLAG_DDEWAIT: UInt32 = 256
SEE_MASK_DOENVSUBST: UInt32 = 512
SEE_MASK_FLAG_NO_UI: UInt32 = 1024
SEE_MASK_UNICODE: UInt32 = 16384
SEE_MASK_NO_CONSOLE: UInt32 = 32768
SEE_MASK_ASYNCOK: UInt32 = 1048576
SEE_MASK_HMONITOR: UInt32 = 2097152
SEE_MASK_NOZONECHECKS: UInt32 = 8388608
SEE_MASK_NOQUERYCLASSSTORE: UInt32 = 16777216
SEE_MASK_WAITFORINPUTIDLE: UInt32 = 33554432
SEE_MASK_FLAG_LOG_USAGE: UInt32 = 67108864
SEE_MASK_FLAG_HINST_IS_SITE: UInt32 = 134217728
SHERB_NOCONFIRMATION: UInt32 = 1
SHERB_NOPROGRESSUI: UInt32 = 2
SHERB_NOSOUND: UInt32 = 4
NIN_SELECT: UInt32 = 1024
NINF_KEY: UInt32 = 1
NIN_BALLOONSHOW: UInt32 = 1026
NIN_BALLOONHIDE: UInt32 = 1027
NIN_BALLOONTIMEOUT: UInt32 = 1028
NIN_BALLOONUSERCLICK: UInt32 = 1029
NIN_POPUPOPEN: UInt32 = 1030
NIN_POPUPCLOSE: UInt32 = 1031
NOTIFYICON_VERSION: UInt32 = 3
NOTIFYICON_VERSION_4: UInt32 = 4
SHGNLI_PIDL: UInt64 = 1
SHGNLI_PREFIXNAME: UInt64 = 2
SHGNLI_NOUNIQUE: UInt64 = 4
SHGNLI_NOLNK: UInt64 = 8
SHGNLI_NOLOCNAME: UInt64 = 16
SHGNLI_USEURLEXT: UInt64 = 32
PRINTACTION_OPEN: UInt32 = 0
PRINTACTION_PROPERTIES: UInt32 = 1
PRINTACTION_NETINSTALL: UInt32 = 2
PRINTACTION_NETINSTALLLINK: UInt32 = 3
PRINTACTION_TESTPAGE: UInt32 = 4
PRINTACTION_OPENNETPRN: UInt32 = 5
PRINTACTION_DOCUMENTDEFAULTS: UInt32 = 6
PRINTACTION_SERVERPROPERTIES: UInt32 = 7
PRINT_PROP_FORCE_NAME: UInt32 = 1
OFFLINE_STATUS_LOCAL: UInt32 = 1
OFFLINE_STATUS_REMOTE: UInt32 = 2
OFFLINE_STATUS_INCOMPLETE: UInt32 = 4
SHIL_LARGE: UInt32 = 0
SHIL_SMALL: UInt32 = 1
SHIL_EXTRALARGE: UInt32 = 2
SHIL_SYSSMALL: UInt32 = 3
SHIL_JUMBO: UInt32 = 4
SHIL_LAST: UInt32 = 4
WC_NETADDRESS: String = 'msctls_netaddress'
NCM_GETADDRESS: UInt32 = 1025
NCM_SETALLOWTYPE: UInt32 = 1026
NCM_GETALLOWTYPE: UInt32 = 1027
NCM_DISPLAYERRORTIP: UInt32 = 1028
CREDENTIAL_PROVIDER_NO_DEFAULT: UInt32 = 4294967295
Identity_LocalUserProvider: Guid = Guid('{a198529b-730f-4089-b646-a12557f5665e}')
MAX_SYNCMGR_ID: UInt32 = 64
MAX_SYNCMGR_PROGRESSTEXT: UInt32 = 260
MAX_SYNCMGR_NAME: UInt32 = 128
STIF_DEFAULT: Int32 = 0
STIF_SUPPORT_HEX: Int32 = 1
SZ_CONTENTTYPE_HTMLA: String = 'text/html'
SZ_CONTENTTYPE_HTMLW: String = 'text/html'
SZ_CONTENTTYPE_CDFA: String = 'application/x-cdf'
SZ_CONTENTTYPE_CDFW: String = 'application/x-cdf'
SZ_CONTENTTYPE_HTML: String = 'text/html'
SZ_CONTENTTYPE_CDF: String = 'application/x-cdf'
GCT_INVALID: UInt32 = 0
GCT_LFNCHAR: UInt32 = 1
GCT_SHORTCHAR: UInt32 = 2
GCT_WILD: UInt32 = 4
GCT_SEPARATOR: UInt32 = 8
PMSF_NORMAL: UInt32 = 0
PMSF_MULTIPLE: UInt32 = 1
PMSF_DONT_STRIP_SPACES: UInt32 = 65536
URL_UNESCAPE: UInt32 = 268435456
URL_ESCAPE_UNSAFE: UInt32 = 536870912
URL_PLUGGABLE_PROTOCOL: UInt32 = 1073741824
URL_WININET_COMPATIBILITY: UInt32 = 2147483648
URL_DONT_ESCAPE_EXTRA_INFO: UInt32 = 33554432
URL_DONT_UNESCAPE_EXTRA_INFO: UInt32 = 33554432
URL_BROWSER_MODE: UInt32 = 33554432
URL_ESCAPE_SPACES_ONLY: UInt32 = 67108864
URL_DONT_SIMPLIFY: UInt32 = 134217728
URL_NO_META: UInt32 = 134217728
URL_UNESCAPE_INPLACE: UInt32 = 1048576
URL_CONVERT_IF_DOSPATH: UInt32 = 2097152
URL_UNESCAPE_HIGH_ANSI_ONLY: UInt32 = 4194304
URL_INTERNAL_PATH: UInt32 = 8388608
URL_FILE_USE_PATHURL: UInt32 = 65536
URL_DONT_UNESCAPE: UInt32 = 131072
URL_ESCAPE_AS_UTF8: UInt32 = 262144
URL_UNESCAPE_AS_UTF8: UInt32 = 262144
URL_ESCAPE_ASCII_URI_COMPONENT: UInt32 = 524288
URL_UNESCAPE_URI_COMPONENT: UInt32 = 262144
URL_ESCAPE_PERCENT: UInt32 = 4096
URL_ESCAPE_SEGMENT_ONLY: UInt32 = 8192
URL_PARTFLAG_KEEPSCHEME: UInt32 = 1
URL_APPLY_DEFAULT: UInt32 = 1
URL_APPLY_GUESSSCHEME: UInt32 = 2
URL_APPLY_GUESSFILE: UInt32 = 4
URL_APPLY_FORCEAPPLY: UInt32 = 8
SRRF_RT_REG_NONE: UInt32 = 1
SRRF_RT_REG_SZ: UInt32 = 2
SRRF_RT_REG_EXPAND_SZ: UInt32 = 4
SRRF_RT_REG_BINARY: UInt32 = 8
SRRF_RT_REG_DWORD: UInt32 = 16
SRRF_RT_REG_MULTI_SZ: UInt32 = 32
SRRF_RT_REG_QWORD: UInt32 = 64
SRRF_RT_ANY: UInt32 = 65535
SRRF_RM_ANY: UInt32 = 0
SRRF_RM_NORMAL: UInt32 = 65536
SRRF_RM_SAFE: UInt32 = 131072
SRRF_RM_SAFENETWORK: UInt32 = 262144
SRRF_NOEXPAND: UInt32 = 268435456
SRRF_ZEROONFAILURE: UInt32 = 536870912
SRRF_NOVIRT: UInt32 = 1073741824
SHREGSET_HKCU: UInt32 = 1
SHREGSET_FORCE_HKCU: UInt32 = 2
SHREGSET_HKLM: UInt32 = 4
SHREGSET_FORCE_HKLM: UInt32 = 8
SPMODE_SHELL: UInt32 = 1
SPMODE_DEBUGOUT: UInt32 = 2
SPMODE_TEST: UInt32 = 4
SPMODE_BROWSER: UInt32 = 8
SPMODE_FLUSH: UInt32 = 16
SPMODE_EVENT: UInt32 = 32
SPMODE_MSVM: UInt32 = 64
SPMODE_FORMATTEXT: UInt32 = 128
SPMODE_PROFILE: UInt32 = 256
SPMODE_DEBUGBREAK: UInt32 = 512
SPMODE_MSGTRACE: UInt32 = 1024
SPMODE_PERFTAGS: UInt32 = 2048
SPMODE_MEMWATCH: UInt32 = 4096
SPMODE_DBMON: UInt32 = 8192
SPMODE_MULTISTOP: UInt32 = 16384
SPMODE_EVENTTRACE: UInt32 = 32768
SHGVSPB_PERUSER: UInt32 = 1
SHGVSPB_ALLUSERS: UInt32 = 2
SHGVSPB_PERFOLDER: UInt32 = 4
SHGVSPB_ALLFOLDERS: UInt32 = 8
SHGVSPB_INHERIT: UInt32 = 16
SHGVSPB_ROAM: UInt32 = 32
SHGVSPB_NOAUTODEFAULTS: UInt32 = 2147483648
FDTF_SHORTTIME: UInt32 = 1
FDTF_SHORTDATE: UInt32 = 2
FDTF_LONGDATE: UInt32 = 4
FDTF_LONGTIME: UInt32 = 8
FDTF_RELATIVE: UInt32 = 16
FDTF_LTRDATE: UInt32 = 256
FDTF_RTLDATE: UInt32 = 512
FDTF_NOAUTOREADINGORDER: UInt32 = 1024
PLATFORM_UNKNOWN: UInt32 = 0
PLATFORM_IE3: UInt32 = 1
PLATFORM_BROWSERONLY: UInt32 = 1
PLATFORM_INTEGRATED: UInt32 = 2
ILMM_IE4: UInt32 = 0
DLLVER_PLATFORM_WINDOWS: UInt32 = 1
DLLVER_PLATFORM_NT: UInt32 = 2
DLLVER_MAJOR_MASK: UInt64 = 18446462598732840960
DLLVER_MINOR_MASK: UInt64 = 281470681743360
DLLVER_BUILD_MASK: UInt64 = 4294901760
DLLVER_QFE_MASK: UInt64 = 65535
WTS_E_FAILEDEXTRACTION: win32more.Windows.Win32.Foundation.HRESULT = -2147175936
WTS_E_EXTRACTIONTIMEDOUT: win32more.Windows.Win32.Foundation.HRESULT = -2147175935
WTS_E_SURROGATEUNAVAILABLE: win32more.Windows.Win32.Foundation.HRESULT = -2147175934
WTS_E_FASTEXTRACTIONNOTSUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -2147175933
WTS_E_DATAFILEUNAVAILABLE: win32more.Windows.Win32.Foundation.HRESULT = -2147175932
WTS_E_EXTRACTIONPENDING: win32more.Windows.Win32.Foundation.HRESULT = -2147175931
WTS_E_EXTRACTIONBLOCKED: win32more.Windows.Win32.Foundation.HRESULT = -2147175930
WTS_E_NOSTORAGEPROVIDERTHUMBNAILHANDLER: win32more.Windows.Win32.Foundation.HRESULT = -2147175929
SHIMGKEY_QUALITY: String = 'Compression'
SHIMGKEY_RAWFORMAT: String = 'RawDataFormat'
SHIMGDEC_DEFAULT: UInt32 = 0
SHIMGDEC_THUMBNAIL: UInt32 = 1
SHIMGDEC_LOADFULL: UInt32 = 2
E_NOTVALIDFORANIMATEDIMAGE: win32more.Windows.Win32.Foundation.HRESULT = -2147221503
S_SYNCMGR_MISSINGITEMS: win32more.Windows.Win32.Foundation.HRESULT = 262657
S_SYNCMGR_RETRYSYNC: win32more.Windows.Win32.Foundation.HRESULT = 262658
S_SYNCMGR_CANCELITEM: win32more.Windows.Win32.Foundation.HRESULT = 262659
S_SYNCMGR_CANCELALL: win32more.Windows.Win32.Foundation.HRESULT = 262660
S_SYNCMGR_ITEMDELETED: win32more.Windows.Win32.Foundation.HRESULT = 262672
S_SYNCMGR_ENUMITEMS: win32more.Windows.Win32.Foundation.HRESULT = 262673
SYNCMGRPROGRESSITEM_STATUSTEXT: UInt32 = 1
SYNCMGRPROGRESSITEM_STATUSTYPE: UInt32 = 2
SYNCMGRPROGRESSITEM_PROGVALUE: UInt32 = 4
SYNCMGRPROGRESSITEM_MAXVALUE: UInt32 = 8
SYNCMGRLOGERROR_ERRORFLAGS: UInt32 = 1
SYNCMGRLOGERROR_ERRORID: UInt32 = 2
SYNCMGRLOGERROR_ITEMID: UInt32 = 4
SYNCMGRITEM_ITEMFLAGMASK: UInt32 = 127
MAX_SYNCMGRITEMNAME: UInt32 = 128
SYNCMGRHANDLERFLAG_MASK: UInt32 = 15
MAX_SYNCMGRHANDLERNAME: UInt32 = 32
SYNCMGRREGISTERFLAGS_MASK: UInt32 = 7
TLOG_BACK: Int32 = -1
TLOG_CURRENT: UInt32 = 0
TLOG_FORE: UInt32 = 1
TLMENUF_INCLUDECURRENT: UInt32 = 1
TLMENUF_BACK: UInt32 = 16
TLMENUF_FORE: UInt32 = 32
BSF_REGISTERASDROPTARGET: UInt32 = 1
BSF_THEATERMODE: UInt32 = 2
BSF_NOLOCALFILEWARNING: UInt32 = 16
BSF_UISETBYAUTOMATION: UInt32 = 256
BSF_RESIZABLE: UInt32 = 512
BSF_CANMAXIMIZE: UInt32 = 1024
BSF_TOPBROWSER: UInt32 = 2048
BSF_NAVNOHISTORY: UInt32 = 4096
BSF_HTMLNAVCANCELED: UInt32 = 8192
BSF_DONTSHOWNAVCANCELPAGE: UInt32 = 16384
BSF_SETNAVIGATABLECODEPAGE: UInt32 = 32768
BSF_DELEGATEDNAVIGATION: UInt32 = 65536
BSF_TRUSTEDFORACTIVEX: UInt32 = 131072
BSF_MERGEDMENUS: UInt32 = 262144
BSF_FEEDNAVIGATION: UInt32 = 524288
BSF_FEEDSUBSCRIBED: UInt32 = 1048576
HLNF_CALLERUNTRUSTED: UInt32 = 2097152
HLNF_TRUSTEDFORACTIVEX: UInt32 = 4194304
HLNF_DISABLEWINDOWRESTRICTIONS: UInt32 = 8388608
HLNF_TRUSTFIRSTDOWNLOAD: UInt32 = 16777216
HLNF_UNTRUSTEDFORDOWNLOAD: UInt32 = 33554432
SHHLNF_NOAUTOSELECT: UInt32 = 67108864
SHHLNF_WRITENOHISTORY: UInt32 = 134217728
HLNF_EXTERNALNAVIGATE: UInt32 = 268435456
HLNF_ALLOW_AUTONAVIGATE: UInt32 = 536870912
HLNF_NEWWINDOWSMANAGED: UInt32 = 2147483648
INTERNET_MAX_PATH_LENGTH: UInt32 = 2048
INTERNET_MAX_SCHEME_LENGTH: UInt32 = 32
VIEW_PRIORITY_RESTRICTED: UInt32 = 112
VIEW_PRIORITY_CACHEHIT: UInt32 = 80
VIEW_PRIORITY_STALECACHEHIT: UInt32 = 69
VIEW_PRIORITY_USEASDEFAULT: UInt32 = 67
VIEW_PRIORITY_SHELLEXT: UInt32 = 64
VIEW_PRIORITY_CACHEMISS: UInt32 = 48
VIEW_PRIORITY_INHERIT: UInt32 = 32
VIEW_PRIORITY_SHELLEXT_ASBACKUP: UInt32 = 21
VIEW_PRIORITY_DESPERATE: UInt32 = 16
VIEW_PRIORITY_NONE: UInt32 = 0
VOLUME_PREFIX: String = '\\\\?\\Volume'
PATHCCH_MAX_CCH: UInt32 = 32768
IDS_DESCRIPTION: UInt32 = 1
ID_APP: UInt32 = 100
DLG_SCRNSAVECONFIGURE: UInt32 = 2003
idsIsPassword: UInt32 = 1000
idsIniFile: UInt32 = 1001
idsScreenSaver: UInt32 = 1002
idsPassword: UInt32 = 1003
idsDifferentPW: UInt32 = 1004
idsChangePW: UInt32 = 1005
idsBadOldPW: UInt32 = 1006
idsAppName: UInt32 = 1007
idsNoHelpMemory: UInt32 = 1008
idsHelpFile: UInt32 = 1009
idsDefKeyword: UInt32 = 1010
MAXFILELEN: UInt32 = 13
TITLEBARNAMELEN: UInt32 = 40
APPNAMEBUFFERLEN: UInt32 = 40
BUFFLEN: UInt32 = 255
SCRM_VERIFYPW: UInt32 = 32768
E_FLAGS: win32more.Windows.Win32.Foundation.HRESULT = -2147217408
IS_E_EXEC_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -2147213310
URL_E_INVALID_SYNTAX: win32more.Windows.Win32.Foundation.HRESULT = -2147217407
URL_E_UNREGISTERED_PROTOCOL: win32more.Windows.Win32.Foundation.HRESULT = -2147217406
CPLPAGE_MOUSE_BUTTONS: UInt32 = 1
CPLPAGE_MOUSE_PTRMOTION: UInt32 = 2
CPLPAGE_MOUSE_WHEEL: UInt32 = 3
CPLPAGE_KEYBOARD_SPEED: UInt32 = 1
CPLPAGE_DISPLAY_BACKGROUND: UInt32 = 1
DISPID_SELECTIONCHANGED: UInt32 = 200
DISPID_FILELISTENUMDONE: UInt32 = 201
DISPID_VERBINVOKED: UInt32 = 202
DISPID_DEFAULTVERBINVOKED: UInt32 = 203
DISPID_BEGINDRAG: UInt32 = 204
DISPID_VIEWMODECHANGED: UInt32 = 205
DISPID_NOITEMSTATE_CHANGED: UInt32 = 206
DISPID_CONTENTSCHANGED: UInt32 = 207
DISPID_FOCUSCHANGED: UInt32 = 208
DISPID_CHECKSTATECHANGED: UInt32 = 209
DISPID_ORDERCHANGED: UInt32 = 210
DISPID_VIEWPAINTDONE: UInt32 = 211
DISPID_COLUMNSCHANGED: UInt32 = 212
DISPID_CTRLMOUSEWHEEL: UInt32 = 213
DISPID_SORTDONE: UInt32 = 214
DISPID_ICONSIZECHANGED: UInt32 = 215
DISPID_FOLDERCHANGED: UInt32 = 217
DISPID_FILTERINVOKED: UInt32 = 218
DISPID_WORDWHEELEDITED: UInt32 = 219
DISPID_SELECTEDITEMCHANGED: UInt32 = 220
DISPID_EXPLORERWINDOWREADY: UInt32 = 221
DISPID_UPDATEIMAGE: UInt32 = 222
DISPID_INITIALENUMERATIONDONE: UInt32 = 223
DISPID_ENTERPRISEIDCHANGED: UInt32 = 224
DISPID_ENTERPRESSED: UInt32 = 200
DISPID_SEARCHCOMMAND_START: UInt32 = 1
DISPID_SEARCHCOMMAND_COMPLETE: UInt32 = 2
DISPID_SEARCHCOMMAND_ABORT: UInt32 = 3
DISPID_SEARCHCOMMAND_UPDATE: UInt32 = 4
DISPID_SEARCHCOMMAND_PROGRESSTEXT: UInt32 = 5
DISPID_SEARCHCOMMAND_ERROR: UInt32 = 6
DISPID_SEARCHCOMMAND_RESTORE: UInt32 = 7
DISPID_IADCCTL_DIRTY: UInt32 = 256
DISPID_IADCCTL_PUBCAT: UInt32 = 257
DISPID_IADCCTL_SORT: UInt32 = 258
DISPID_IADCCTL_FORCEX86: UInt32 = 259
DISPID_IADCCTL_SHOWPOSTSETUP: UInt32 = 260
DISPID_IADCCTL_ONDOMAIN: UInt32 = 261
DISPID_IADCCTL_DEFAULTCAT: UInt32 = 262
COPYENGINE_S_YES: win32more.Windows.Win32.Foundation.HRESULT = 2555905
COPYENGINE_S_NOT_HANDLED: win32more.Windows.Win32.Foundation.HRESULT = 2555907
COPYENGINE_S_USER_RETRY: win32more.Windows.Win32.Foundation.HRESULT = 2555908
COPYENGINE_S_USER_IGNORED: win32more.Windows.Win32.Foundation.HRESULT = 2555909
COPYENGINE_S_MERGE: win32more.Windows.Win32.Foundation.HRESULT = 2555910
COPYENGINE_S_DONT_PROCESS_CHILDREN: win32more.Windows.Win32.Foundation.HRESULT = 2555912
COPYENGINE_S_ALREADY_DONE: win32more.Windows.Win32.Foundation.HRESULT = 2555914
COPYENGINE_S_PENDING: win32more.Windows.Win32.Foundation.HRESULT = 2555915
COPYENGINE_S_KEEP_BOTH: win32more.Windows.Win32.Foundation.HRESULT = 2555916
COPYENGINE_S_CLOSE_PROGRAM: win32more.Windows.Win32.Foundation.HRESULT = 2555917
COPYENGINE_S_COLLISIONRESOLVED: win32more.Windows.Win32.Foundation.HRESULT = 2555918
COPYENGINE_S_PROGRESS_PAUSE: win32more.Windows.Win32.Foundation.HRESULT = 2555919
COPYENGINE_S_PENDING_DELETE: win32more.Windows.Win32.Foundation.HRESULT = 2555920
COPYENGINE_E_USER_CANCELLED: win32more.Windows.Win32.Foundation.HRESULT = -2144927744
COPYENGINE_E_CANCELLED: win32more.Windows.Win32.Foundation.HRESULT = -2144927743
COPYENGINE_E_REQUIRES_ELEVATION: win32more.Windows.Win32.Foundation.HRESULT = -2144927742
COPYENGINE_E_SAME_FILE: win32more.Windows.Win32.Foundation.HRESULT = -2144927741
COPYENGINE_E_DIFF_DIR: win32more.Windows.Win32.Foundation.HRESULT = -2144927740
COPYENGINE_E_MANY_SRC_1_DEST: win32more.Windows.Win32.Foundation.HRESULT = -2144927739
COPYENGINE_E_DEST_SUBTREE: win32more.Windows.Win32.Foundation.HRESULT = -2144927735
COPYENGINE_E_DEST_SAME_TREE: win32more.Windows.Win32.Foundation.HRESULT = -2144927734
COPYENGINE_E_FLD_IS_FILE_DEST: win32more.Windows.Win32.Foundation.HRESULT = -2144927733
COPYENGINE_E_FILE_IS_FLD_DEST: win32more.Windows.Win32.Foundation.HRESULT = -2144927732
COPYENGINE_E_FILE_TOO_LARGE: win32more.Windows.Win32.Foundation.HRESULT = -2144927731
COPYENGINE_E_REMOVABLE_FULL: win32more.Windows.Win32.Foundation.HRESULT = -2144927730
COPYENGINE_E_DEST_IS_RO_CD: win32more.Windows.Win32.Foundation.HRESULT = -2144927729
COPYENGINE_E_DEST_IS_RW_CD: win32more.Windows.Win32.Foundation.HRESULT = -2144927728
COPYENGINE_E_DEST_IS_R_CD: win32more.Windows.Win32.Foundation.HRESULT = -2144927727
COPYENGINE_E_DEST_IS_RO_DVD: win32more.Windows.Win32.Foundation.HRESULT = -2144927726
COPYENGINE_E_DEST_IS_RW_DVD: win32more.Windows.Win32.Foundation.HRESULT = -2144927725
COPYENGINE_E_DEST_IS_R_DVD: win32more.Windows.Win32.Foundation.HRESULT = -2144927724
COPYENGINE_E_SRC_IS_RO_CD: win32more.Windows.Win32.Foundation.HRESULT = -2144927723
COPYENGINE_E_SRC_IS_RW_CD: win32more.Windows.Win32.Foundation.HRESULT = -2144927722
COPYENGINE_E_SRC_IS_R_CD: win32more.Windows.Win32.Foundation.HRESULT = -2144927721
COPYENGINE_E_SRC_IS_RO_DVD: win32more.Windows.Win32.Foundation.HRESULT = -2144927720
COPYENGINE_E_SRC_IS_RW_DVD: win32more.Windows.Win32.Foundation.HRESULT = -2144927719
COPYENGINE_E_SRC_IS_R_DVD: win32more.Windows.Win32.Foundation.HRESULT = -2144927718
COPYENGINE_E_INVALID_FILES_SRC: win32more.Windows.Win32.Foundation.HRESULT = -2144927717
COPYENGINE_E_INVALID_FILES_DEST: win32more.Windows.Win32.Foundation.HRESULT = -2144927716
COPYENGINE_E_PATH_TOO_DEEP_SRC: win32more.Windows.Win32.Foundation.HRESULT = -2144927715
COPYENGINE_E_PATH_TOO_DEEP_DEST: win32more.Windows.Win32.Foundation.HRESULT = -2144927714
COPYENGINE_E_ROOT_DIR_SRC: win32more.Windows.Win32.Foundation.HRESULT = -2144927713
COPYENGINE_E_ROOT_DIR_DEST: win32more.Windows.Win32.Foundation.HRESULT = -2144927712
COPYENGINE_E_ACCESS_DENIED_SRC: win32more.Windows.Win32.Foundation.HRESULT = -2144927711
COPYENGINE_E_ACCESS_DENIED_DEST: win32more.Windows.Win32.Foundation.HRESULT = -2144927710
COPYENGINE_E_PATH_NOT_FOUND_SRC: win32more.Windows.Win32.Foundation.HRESULT = -2144927709
COPYENGINE_E_PATH_NOT_FOUND_DEST: win32more.Windows.Win32.Foundation.HRESULT = -2144927708
COPYENGINE_E_NET_DISCONNECT_SRC: win32more.Windows.Win32.Foundation.HRESULT = -2144927707
COPYENGINE_E_NET_DISCONNECT_DEST: win32more.Windows.Win32.Foundation.HRESULT = -2144927706
COPYENGINE_E_SHARING_VIOLATION_SRC: win32more.Windows.Win32.Foundation.HRESULT = -2144927705
COPYENGINE_E_SHARING_VIOLATION_DEST: win32more.Windows.Win32.Foundation.HRESULT = -2144927704
COPYENGINE_E_ALREADY_EXISTS_NORMAL: win32more.Windows.Win32.Foundation.HRESULT = -2144927703
COPYENGINE_E_ALREADY_EXISTS_READONLY: win32more.Windows.Win32.Foundation.HRESULT = -2144927702
COPYENGINE_E_ALREADY_EXISTS_SYSTEM: win32more.Windows.Win32.Foundation.HRESULT = -2144927701
COPYENGINE_E_ALREADY_EXISTS_FOLDER: win32more.Windows.Win32.Foundation.HRESULT = -2144927700
COPYENGINE_E_STREAM_LOSS: win32more.Windows.Win32.Foundation.HRESULT = -2144927699
COPYENGINE_E_EA_LOSS: win32more.Windows.Win32.Foundation.HRESULT = -2144927698
COPYENGINE_E_PROPERTY_LOSS: win32more.Windows.Win32.Foundation.HRESULT = -2144927697
COPYENGINE_E_PROPERTIES_LOSS: win32more.Windows.Win32.Foundation.HRESULT = -2144927696
COPYENGINE_E_ENCRYPTION_LOSS: win32more.Windows.Win32.Foundation.HRESULT = -2144927695
COPYENGINE_E_DISK_FULL: win32more.Windows.Win32.Foundation.HRESULT = -2144927694
COPYENGINE_E_DISK_FULL_CLEAN: win32more.Windows.Win32.Foundation.HRESULT = -2144927693
COPYENGINE_E_EA_NOT_SUPPORTED: win32more.Windows.Win32.Foundation.HRESULT = -2144927692
COPYENGINE_E_CANT_REACH_SOURCE: win32more.Windows.Win32.Foundation.HRESULT = -2144927691
COPYENGINE_E_RECYCLE_UNKNOWN_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2144927691
COPYENGINE_E_RECYCLE_FORCE_NUKE: win32more.Windows.Win32.Foundation.HRESULT = -2144927690
COPYENGINE_E_RECYCLE_SIZE_TOO_BIG: win32more.Windows.Win32.Foundation.HRESULT = -2144927689
COPYENGINE_E_RECYCLE_PATH_TOO_LONG: win32more.Windows.Win32.Foundation.HRESULT = -2144927688
COPYENGINE_E_RECYCLE_BIN_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2144927686
COPYENGINE_E_NEWFILE_NAME_TOO_LONG: win32more.Windows.Win32.Foundation.HRESULT = -2144927685
COPYENGINE_E_NEWFOLDER_NAME_TOO_LONG: win32more.Windows.Win32.Foundation.HRESULT = -2144927684
COPYENGINE_E_DIR_NOT_EMPTY: win32more.Windows.Win32.Foundation.HRESULT = -2144927683
COPYENGINE_E_FAT_MAX_IN_ROOT: win32more.Windows.Win32.Foundation.HRESULT = -2144927682
COPYENGINE_E_ACCESSDENIED_READONLY: win32more.Windows.Win32.Foundation.HRESULT = -2144927681
COPYENGINE_E_REDIRECTED_TO_WEBPAGE: win32more.Windows.Win32.Foundation.HRESULT = -2144927680
COPYENGINE_E_SERVER_BAD_FILE_TYPE: win32more.Windows.Win32.Foundation.HRESULT = -2144927679
COPYENGINE_E_INTERNET_ITEM_UNAVAILABLE: win32more.Windows.Win32.Foundation.HRESULT = -2144927678
COPYENGINE_E_CANNOT_MOVE_FROM_RECYCLE_BIN: win32more.Windows.Win32.Foundation.HRESULT = -2144927677
COPYENGINE_E_CANNOT_MOVE_SHARED_FOLDER: win32more.Windows.Win32.Foundation.HRESULT = -2144927676
COPYENGINE_E_INTERNET_ITEM_STORAGE_PROVIDER_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2144927675
COPYENGINE_E_INTERNET_ITEM_STORAGE_PROVIDER_PAUSED: win32more.Windows.Win32.Foundation.HRESULT = -2144927674
COPYENGINE_E_REQUIRES_EDP_CONSENT: win32more.Windows.Win32.Foundation.HRESULT = -2144927673
COPYENGINE_E_BLOCKED_BY_EDP_POLICY: win32more.Windows.Win32.Foundation.HRESULT = -2144927672
COPYENGINE_E_REQUIRES_EDP_CONSENT_FOR_REMOVABLE_DRIVE: win32more.Windows.Win32.Foundation.HRESULT = -2144927671
COPYENGINE_E_BLOCKED_BY_EDP_FOR_REMOVABLE_DRIVE: win32more.Windows.Win32.Foundation.HRESULT = -2144927670
COPYENGINE_E_RMS_REQUIRES_EDP_CONSENT_FOR_REMOVABLE_DRIVE: win32more.Windows.Win32.Foundation.HRESULT = -2144927669
COPYENGINE_E_RMS_BLOCKED_BY_EDP_FOR_REMOVABLE_DRIVE: win32more.Windows.Win32.Foundation.HRESULT = -2144927668
COPYENGINE_E_WARNED_BY_DLP_POLICY: win32more.Windows.Win32.Foundation.HRESULT = -2144927667
COPYENGINE_E_BLOCKED_BY_DLP_POLICY: win32more.Windows.Win32.Foundation.HRESULT = -2144927666
COPYENGINE_E_SILENT_FAIL_BY_DLP_POLICY: win32more.Windows.Win32.Foundation.HRESULT = -2144927665
NETCACHE_E_NEGATIVE_CACHE: win32more.Windows.Win32.Foundation.HRESULT = -2144927488
EXECUTE_E_LAUNCH_APPLICATION: win32more.Windows.Win32.Foundation.HRESULT = -2144927487
SHELL_E_WRONG_BITDEPTH: win32more.Windows.Win32.Foundation.HRESULT = -2144927486
LINK_E_DELETE: win32more.Windows.Win32.Foundation.HRESULT = -2144927485
STORE_E_NEWER_VERSION_AVAILABLE: win32more.Windows.Win32.Foundation.HRESULT = -2144927484
E_FILE_PLACEHOLDER_NOT_INITIALIZED: win32more.Windows.Win32.Foundation.HRESULT = -2144927472
E_FILE_PLACEHOLDER_VERSION_MISMATCH: win32more.Windows.Win32.Foundation.HRESULT = -2144927471
E_FILE_PLACEHOLDER_SERVER_TIMED_OUT: win32more.Windows.Win32.Foundation.HRESULT = -2144927470
E_FILE_PLACEHOLDER_STORAGEPROVIDER_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2144927469
CAMERAROLL_E_NO_DOWNSAMPLING_REQUIRED: win32more.Windows.Win32.Foundation.HRESULT = -2144927456
E_ACTIVATIONDENIED_USERCLOSE: win32more.Windows.Win32.Foundation.HRESULT = -2144927440
E_ACTIVATIONDENIED_SHELLERROR: win32more.Windows.Win32.Foundation.HRESULT = -2144927439
E_ACTIVATIONDENIED_SHELLRESTART: win32more.Windows.Win32.Foundation.HRESULT = -2144927438
E_ACTIVATIONDENIED_UNEXPECTED: win32more.Windows.Win32.Foundation.HRESULT = -2144927437
E_ACTIVATIONDENIED_SHELLNOTREADY: win32more.Windows.Win32.Foundation.HRESULT = -2144927436
LIBRARY_E_NO_SAVE_LOCATION: win32more.Windows.Win32.Foundation.HRESULT = -2144927232
LIBRARY_E_NO_ACCESSIBLE_LOCATION: win32more.Windows.Win32.Foundation.HRESULT = -2144927231
E_USERTILE_UNSUPPORTEDFILETYPE: win32more.Windows.Win32.Foundation.HRESULT = -2144927216
E_USERTILE_CHANGEDISABLED: win32more.Windows.Win32.Foundation.HRESULT = -2144927215
E_USERTILE_LARGEORDYNAMIC: win32more.Windows.Win32.Foundation.HRESULT = -2144927214
E_USERTILE_VIDEOFRAMESIZE: win32more.Windows.Win32.Foundation.HRESULT = -2144927213
E_USERTILE_FILESIZE: win32more.Windows.Win32.Foundation.HRESULT = -2144927212
IMM_ACC_DOCKING_E_INSUFFICIENTHEIGHT: win32more.Windows.Win32.Foundation.HRESULT = -2144927184
IMM_ACC_DOCKING_E_DOCKOCCUPIED: win32more.Windows.Win32.Foundation.HRESULT = -2144927183
IMSC_E_SHELL_COMPONENT_STARTUP_FAILURE: win32more.Windows.Win32.Foundation.HRESULT = -2144927181
SHC_E_SHELL_COMPONENT_STARTUP_FAILURE: win32more.Windows.Win32.Foundation.HRESULT = -2144927180
E_TILE_NOTIFICATIONS_PLATFORM_FAILURE: win32more.Windows.Win32.Foundation.HRESULT = -2144927159
E_SHELL_EXTENSION_BLOCKED: win32more.Windows.Win32.Foundation.HRESULT = -2144926975
E_IMAGEFEED_CHANGEDISABLED: win32more.Windows.Win32.Foundation.HRESULT = -2144926960
CLSID_CUrlHistory: Guid = Guid('{3c374a40-bae4-11cf-bf7d-00aa006946ee}')
CLSID_CUrlHistoryBoth: Guid = Guid('{6659983c-8476-4eb4-b78c-e5968f326ba0}')
ISHCUTCMDID_DOWNLOADICON: Int32 = 0
ISHCUTCMDID_INTSHORTCUTCREATE: Int32 = 1
ISHCUTCMDID_COMMITHISTORY: Int32 = 2
ISHCUTCMDID_SETUSERAWURL: Int32 = 3
SFBID_PIDLCHANGED: Int32 = 0
DBCID_EMPTY: Int32 = 0
DBCID_ONDRAG: Int32 = 1
DBCID_CLSIDOFBAR: Int32 = 2
DBCID_RESIZE: Int32 = 3
DBCID_GETBAR: Int32 = 4
DBCID_UPDATESIZE: Int32 = 5
BMICON_LARGE: Int32 = 0
BMICON_SMALL: Int32 = 1
CTF_INSIST: Int32 = 1
CTF_THREAD_REF: Int32 = 2
CTF_PROCESS_REF: Int32 = 4
CTF_COINIT_STA: Int32 = 8
CTF_COINIT: Int32 = 8
CTF_FREELIBANDEXIT: Int32 = 16
CTF_REF_COUNTED: Int32 = 32
CTF_WAIT_ALLOWCOM: Int32 = 64
CTF_UNUSED: Int32 = 128
CTF_INHERITWOW64: Int32 = 256
CTF_WAIT_NO_REENTRANCY: Int32 = 512
CTF_KEYBOARD_LOCALE: Int32 = 1024
CTF_OLEINITIALIZE: Int32 = 2048
CTF_COINIT_MTA: Int32 = 4096
CTF_NOADDREFLIB: Int32 = 8192
@winfunctype('SHELL32.dll', entry_point=660)
def FileIconInit(fRestoreCache: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def LoadUserProfileA(hToken: win32more.Windows.Win32.Foundation.HANDLE, lpProfileInfo: POINTER(win32more.Windows.Win32.UI.Shell.PROFILEINFOA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def LoadUserProfileW(hToken: win32more.Windows.Win32.Foundation.HANDLE, lpProfileInfo: POINTER(win32more.Windows.Win32.UI.Shell.PROFILEINFOW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
LoadUserProfile = UnicodeAlias('LoadUserProfileW')
@winfunctype('USERENV.dll')
def UnloadUserProfile(hToken: win32more.Windows.Win32.Foundation.HANDLE, hProfile: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def GetProfilesDirectoryA(lpProfileDir: win32more.Windows.Win32.Foundation.PSTR, lpcchSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def GetProfilesDirectoryW(lpProfileDir: win32more.Windows.Win32.Foundation.PWSTR, lpcchSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
GetProfilesDirectory = UnicodeAlias('GetProfilesDirectoryW')
@winfunctype('USERENV.dll')
def GetProfileType(dwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def DeleteProfileA(lpSidString: win32more.Windows.Win32.Foundation.PSTR, lpProfilePath: win32more.Windows.Win32.Foundation.PSTR, lpComputerName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def DeleteProfileW(lpSidString: win32more.Windows.Win32.Foundation.PWSTR, lpProfilePath: win32more.Windows.Win32.Foundation.PWSTR, lpComputerName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
DeleteProfile = UnicodeAlias('DeleteProfileW')
@winfunctype('USERENV.dll')
def CreateProfile(pszUserSid: win32more.Windows.Win32.Foundation.PWSTR, pszUserName: win32more.Windows.Win32.Foundation.PWSTR, pszProfilePath: win32more.Windows.Win32.Foundation.PWSTR, cchProfilePath: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('USERENV.dll')
def GetDefaultUserProfileDirectoryA(lpProfileDir: win32more.Windows.Win32.Foundation.PSTR, lpcchSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def GetDefaultUserProfileDirectoryW(lpProfileDir: win32more.Windows.Win32.Foundation.PWSTR, lpcchSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
GetDefaultUserProfileDirectory = UnicodeAlias('GetDefaultUserProfileDirectoryW')
@winfunctype('USERENV.dll')
def GetAllUsersProfileDirectoryA(lpProfileDir: win32more.Windows.Win32.Foundation.PSTR, lpcchSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def GetAllUsersProfileDirectoryW(lpProfileDir: win32more.Windows.Win32.Foundation.PWSTR, lpcchSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
GetAllUsersProfileDirectory = UnicodeAlias('GetAllUsersProfileDirectoryW')
@winfunctype('USERENV.dll')
def GetUserProfileDirectoryA(hToken: win32more.Windows.Win32.Foundation.HANDLE, lpProfileDir: win32more.Windows.Win32.Foundation.PSTR, lpcchSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USERENV.dll')
def GetUserProfileDirectoryW(hToken: win32more.Windows.Win32.Foundation.HANDLE, lpProfileDir: win32more.Windows.Win32.Foundation.PWSTR, lpcchSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
GetUserProfileDirectory = UnicodeAlias('GetUserProfileDirectoryW')
@winfunctype('PROPSYS.dll')
def InitPropVariantFromStrRet(pstrret: POINTER(win32more.Windows.Win32.UI.Shell.Common.STRRET), pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def PropVariantToStrRet(propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT), pstrret: POINTER(win32more.Windows.Win32.UI.Shell.Common.STRRET)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def InitVariantFromStrRet(pstrret: POINTER(win32more.Windows.Win32.UI.Shell.Common.STRRET), pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pvar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('PROPSYS.dll')
def VariantToStrRet(varIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pstrret: POINTER(win32more.Windows.Win32.UI.Shell.Common.STRRET)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('COMCTL32.dll')
def SetWindowSubclass(hWnd: win32more.Windows.Win32.Foundation.HWND, pfnSubclass: win32more.Windows.Win32.UI.Shell.SUBCLASSPROC, uIdSubclass: UIntPtr, dwRefData: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('COMCTL32.dll')
def GetWindowSubclass(hWnd: win32more.Windows.Win32.Foundation.HWND, pfnSubclass: win32more.Windows.Win32.UI.Shell.SUBCLASSPROC, uIdSubclass: UIntPtr, pdwRefData: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('COMCTL32.dll')
def RemoveWindowSubclass(hWnd: win32more.Windows.Win32.Foundation.HWND, pfnSubclass: win32more.Windows.Win32.UI.Shell.SUBCLASSPROC, uIdSubclass: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('COMCTL32.dll')
def DefSubclassProc(hWnd: win32more.Windows.Win32.Foundation.HWND, uMsg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.LRESULT: ...
@winfunctype('USER32.dll')
def SetWindowContextHelpId(param0: win32more.Windows.Win32.Foundation.HWND, param1: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetWindowContextHelpId(param0: win32more.Windows.Win32.Foundation.HWND) -> UInt32: ...
@winfunctype('USER32.dll')
def SetMenuContextHelpId(param0: win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU, param1: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetMenuContextHelpId(param0: win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU) -> UInt32: ...
@winfunctype('USER32.dll')
def WinHelpA(hWndMain: win32more.Windows.Win32.Foundation.HWND, lpszHelp: win32more.Windows.Win32.Foundation.PSTR, uCommand: UInt32, dwData: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def WinHelpW(hWndMain: win32more.Windows.Win32.Foundation.HWND, lpszHelp: win32more.Windows.Win32.Foundation.PWSTR, uCommand: UInt32, dwData: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
WinHelp = UnicodeAlias('WinHelpW')
@winfunctype('SHELL32.dll')
def SHSimpleIDListFromPath(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST): ...
@winfunctype('SHELL32.dll')
def SHCreateItemFromIDList(pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateItemFromParsingName(pszPath: win32more.Windows.Win32.Foundation.PWSTR, pbc: win32more.Windows.Win32.System.Com.IBindCtx, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateItemWithParent(pidlParent: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), psfParent: win32more.Windows.Win32.UI.Shell.IShellFolder, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), riid: POINTER(Guid), ppvItem: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateItemFromRelativeName(psiParent: win32more.Windows.Win32.UI.Shell.IShellItem, pszName: win32more.Windows.Win32.Foundation.PWSTR, pbc: win32more.Windows.Win32.System.Com.IBindCtx, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateItemInKnownFolder(kfid: POINTER(Guid), dwKFFlags: UInt32, pszItem: win32more.Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetIDListFromObject(punk: win32more.Windows.Win32.System.Com.IUnknown, ppidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetItemFromObject(punk: win32more.Windows.Win32.System.Com.IUnknown, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetNameFromIDList(pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), sigdnName: win32more.Windows.Win32.UI.Shell.SIGDN, ppszName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetItemFromDataObject(pdtobj: win32more.Windows.Win32.System.Com.IDataObject, dwFlags: win32more.Windows.Win32.UI.Shell.DATAOBJ_GET_ITEM_FLAGS, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateShellItemArray(pidlParent: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), psf: win32more.Windows.Win32.UI.Shell.IShellFolder, cidl: UInt32, ppidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)), ppsiItemArray: POINTER(win32more.Windows.Win32.UI.Shell.IShellItemArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateShellItemArrayFromDataObject(pdo: win32more.Windows.Win32.System.Com.IDataObject, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateShellItemArrayFromIDLists(cidl: UInt32, rgpidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)), ppsiItemArray: POINTER(win32more.Windows.Win32.UI.Shell.IShellItemArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateShellItemArrayFromShellItem(psi: win32more.Windows.Win32.UI.Shell.IShellItem, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateAssociationRegistration(riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateDefaultExtractIcon(riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SetCurrentProcessExplicitAppUserModelID(AppID: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def GetCurrentProcessExplicitAppUserModelID(AppID: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetTemporaryPropertyForItem(psi: win32more.Windows.Win32.UI.Shell.IShellItem, propkey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHSetTemporaryPropertyForItem(psi: win32more.Windows.Win32.UI.Shell.IShellItem, propkey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHShowManageLibraryUI(psiLibrary: win32more.Windows.Win32.UI.Shell.IShellItem, hwndOwner: win32more.Windows.Win32.Foundation.HWND, pszTitle: win32more.Windows.Win32.Foundation.PWSTR, pszInstruction: win32more.Windows.Win32.Foundation.PWSTR, lmdOptions: win32more.Windows.Win32.UI.Shell.LIBRARYMANAGEDIALOGOPTIONS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHResolveLibrary(psiLibrary: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHAssocEnumHandlers(pszExtra: win32more.Windows.Win32.Foundation.PWSTR, afFilter: win32more.Windows.Win32.UI.Shell.ASSOC_FILTER, ppEnumHandler: POINTER(win32more.Windows.Win32.UI.Shell.IEnumAssocHandlers)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHAssocEnumHandlersForProtocolByApplication(protocol: win32more.Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), enumHandlers: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('OLE32.dll')
def HMONITOR_UserSize(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(win32more.Windows.Win32.Graphics.Gdi.HMONITOR)) -> UInt32: ...
@winfunctype('OLE32.dll')
def HMONITOR_UserMarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(win32more.Windows.Win32.Graphics.Gdi.HMONITOR)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HMONITOR_UserUnmarshal(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(win32more.Windows.Win32.Graphics.Gdi.HMONITOR)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HMONITOR_UserFree(param0: POINTER(UInt32), param1: POINTER(win32more.Windows.Win32.Graphics.Gdi.HMONITOR)) -> Void: ...
@winfunctype('OLE32.dll')
def HMONITOR_UserSize64(param0: POINTER(UInt32), param1: UInt32, param2: POINTER(win32more.Windows.Win32.Graphics.Gdi.HMONITOR)) -> UInt32: ...
@winfunctype('OLE32.dll')
def HMONITOR_UserMarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(win32more.Windows.Win32.Graphics.Gdi.HMONITOR)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HMONITOR_UserUnmarshal64(param0: POINTER(UInt32), param1: POINTER(Byte), param2: POINTER(win32more.Windows.Win32.Graphics.Gdi.HMONITOR)) -> POINTER(Byte): ...
@winfunctype('OLE32.dll')
def HMONITOR_UserFree64(param0: POINTER(UInt32), param1: POINTER(win32more.Windows.Win32.Graphics.Gdi.HMONITOR)) -> Void: ...
@winfunctype('SHELL32.dll')
def SHCreateDefaultPropertiesOp(psi: win32more.Windows.Win32.UI.Shell.IShellItem, ppFileOp: POINTER(win32more.Windows.Win32.UI.Shell.IFileOperation)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHSetDefaultProperties(hwnd: win32more.Windows.Win32.Foundation.HWND, psi: win32more.Windows.Win32.UI.Shell.IShellItem, dwFileOpFlags: UInt32, pfops: win32more.Windows.Win32.UI.Shell.IFileOperationProgressSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetMalloc(ppMalloc: POINTER(win32more.Windows.Win32.System.Com.IMalloc)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHAlloc(cb: UIntPtr) -> VoidPtr: ...
@winfunctype('SHELL32.dll')
def SHFree(pv: VoidPtr) -> Void: ...
@winfunctype('SHELL32.dll')
def SHGetIconOverlayIndexA(pszIconPath: win32more.Windows.Win32.Foundation.PSTR, iIconIndex: Int32) -> Int32: ...
@winfunctype('SHELL32.dll')
def SHGetIconOverlayIndexW(pszIconPath: win32more.Windows.Win32.Foundation.PWSTR, iIconIndex: Int32) -> Int32: ...
SHGetIconOverlayIndex = UnicodeAlias('SHGetIconOverlayIndexW')
@winfunctype('SHELL32.dll')
def ILClone(pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST): ...
@winfunctype('SHELL32.dll')
def ILCloneFirst(pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST): ...
@winfunctype('SHELL32.dll')
def ILCombine(pidl1: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pidl2: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST): ...
@winfunctype('SHELL32.dll')
def ILFree(pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> Void: ...
@winfunctype('SHELL32.dll')
def ILGetNext(pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST): ...
@winfunctype('SHELL32.dll')
def ILGetSize(pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> UInt32: ...
@winfunctype('SHELL32.dll')
def ILFindChild(pidlParent: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pidlChild: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST): ...
@winfunctype('SHELL32.dll')
def ILFindLastID(pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST): ...
@winfunctype('SHELL32.dll')
def ILRemoveLastID(pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def ILIsEqual(pidl1: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pidl2: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def ILIsParent(pidl1: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pidl2: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), fImmediate: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def ILSaveToStream(pstm: win32more.Windows.Win32.System.Com.IStream, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def ILLoadFromStreamEx(pstm: win32more.Windows.Win32.System.Com.IStream, pidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def ILCreateFromPathA(pszPath: win32more.Windows.Win32.Foundation.PSTR) -> POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST): ...
@winfunctype('SHELL32.dll')
def ILCreateFromPathW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST): ...
ILCreateFromPath = UnicodeAlias('ILCreateFromPathW')
@winfunctype('SHELL32.dll')
def SHILCreateFromPath(pszPath: win32more.Windows.Win32.Foundation.PWSTR, ppidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)), rgfInOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def ILAppendID(pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pmkid: POINTER(win32more.Windows.Win32.UI.Shell.Common.SHITEMID), fAppend: win32more.Windows.Win32.Foundation.BOOL) -> POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST): ...
@winfunctype('SHELL32.dll')
def SHGetPathFromIDListEx(pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pszPath: win32more.Windows.Win32.Foundation.PWSTR, cchPath: UInt32, uOpts: win32more.Windows.Win32.UI.Shell.GPFIDL_FLAGS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHGetPathFromIDListA(pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pszPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHGetPathFromIDListW(pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
SHGetPathFromIDList = UnicodeAlias('SHGetPathFromIDListW')
@winfunctype('SHELL32.dll')
def SHCreateDirectory(hwnd: win32more.Windows.Win32.Foundation.HWND, pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('SHELL32.dll')
def SHCreateDirectoryExA(hwnd: win32more.Windows.Win32.Foundation.HWND, pszPath: win32more.Windows.Win32.Foundation.PSTR, psa: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES)) -> Int32: ...
@winfunctype('SHELL32.dll')
def SHCreateDirectoryExW(hwnd: win32more.Windows.Win32.Foundation.HWND, pszPath: win32more.Windows.Win32.Foundation.PWSTR, psa: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES)) -> Int32: ...
SHCreateDirectoryEx = UnicodeAlias('SHCreateDirectoryExW')
@winfunctype('SHELL32.dll')
def SHOpenFolderAndSelectItems(pidlFolder: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), cidl: UInt32, apidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateShellItem(pidlParent: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), psfParent: win32more.Windows.Win32.UI.Shell.IShellFolder, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), ppsi: POINTER(win32more.Windows.Win32.UI.Shell.IShellItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetSpecialFolderLocation(hwnd: win32more.Windows.Win32.Foundation.HWND, csidl: Int32, ppidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCloneSpecialIDList(hwnd: win32more.Windows.Win32.Foundation.HWND, csidl: Int32, fCreate: win32more.Windows.Win32.Foundation.BOOL) -> POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST): ...
@winfunctype('SHELL32.dll')
def SHGetSpecialFolderPathA(hwnd: win32more.Windows.Win32.Foundation.HWND, pszPath: win32more.Windows.Win32.Foundation.PSTR, csidl: Int32, fCreate: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHGetSpecialFolderPathW(hwnd: win32more.Windows.Win32.Foundation.HWND, pszPath: win32more.Windows.Win32.Foundation.PWSTR, csidl: Int32, fCreate: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
SHGetSpecialFolderPath = UnicodeAlias('SHGetSpecialFolderPathW')
@winfunctype('SHELL32.dll')
def SHFlushSFCache() -> Void: ...
@winfunctype('SHELL32.dll')
def SHGetFolderPathA(hwnd: win32more.Windows.Win32.Foundation.HWND, csidl: Int32, hToken: win32more.Windows.Win32.Foundation.HANDLE, dwFlags: UInt32, pszPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetFolderPathW(hwnd: win32more.Windows.Win32.Foundation.HWND, csidl: Int32, hToken: win32more.Windows.Win32.Foundation.HANDLE, dwFlags: UInt32, pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
SHGetFolderPath = UnicodeAlias('SHGetFolderPathW')
@winfunctype('SHELL32.dll')
def SHGetFolderLocation(hwnd: win32more.Windows.Win32.Foundation.HWND, csidl: Int32, hToken: win32more.Windows.Win32.Foundation.HANDLE, dwFlags: UInt32, ppidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHSetFolderPathA(csidl: Int32, hToken: win32more.Windows.Win32.Foundation.HANDLE, dwFlags: UInt32, pszPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHSetFolderPathW(csidl: Int32, hToken: win32more.Windows.Win32.Foundation.HANDLE, dwFlags: UInt32, pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
SHSetFolderPath = UnicodeAlias('SHSetFolderPathW')
@winfunctype('SHELL32.dll')
def SHGetFolderPathAndSubDirA(hwnd: win32more.Windows.Win32.Foundation.HWND, csidl: Int32, hToken: win32more.Windows.Win32.Foundation.HANDLE, dwFlags: UInt32, pszSubDir: win32more.Windows.Win32.Foundation.PSTR, pszPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetFolderPathAndSubDirW(hwnd: win32more.Windows.Win32.Foundation.HWND, csidl: Int32, hToken: win32more.Windows.Win32.Foundation.HANDLE, dwFlags: UInt32, pszSubDir: win32more.Windows.Win32.Foundation.PWSTR, pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
SHGetFolderPathAndSubDir = UnicodeAlias('SHGetFolderPathAndSubDirW')
@winfunctype('SHELL32.dll')
def SHGetKnownFolderIDList(rfid: POINTER(Guid), dwFlags: UInt32, hToken: win32more.Windows.Win32.Foundation.HANDLE, ppidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHSetKnownFolderPath(rfid: POINTER(Guid), dwFlags: UInt32, hToken: win32more.Windows.Win32.Foundation.HANDLE, pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetKnownFolderPath(rfid: POINTER(Guid), dwFlags: UInt32, hToken: win32more.Windows.Win32.Foundation.HANDLE, ppszPath: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetKnownFolderItem(rfid: POINTER(Guid), flags: win32more.Windows.Win32.UI.Shell.KNOWN_FOLDER_FLAG, hToken: win32more.Windows.Win32.Foundation.HANDLE, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetSetFolderCustomSettings(pfcs: POINTER(win32more.Windows.Win32.UI.Shell.SHFOLDERCUSTOMSETTINGS), pszPath: win32more.Windows.Win32.Foundation.PWSTR, dwReadWrite: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHBrowseForFolderA(lpbi: POINTER(win32more.Windows.Win32.UI.Shell.BROWSEINFOA)) -> POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST): ...
@winfunctype('SHELL32.dll')
def SHBrowseForFolderW(lpbi: POINTER(win32more.Windows.Win32.UI.Shell.BROWSEINFOW)) -> POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST): ...
SHBrowseForFolder = UnicodeAlias('SHBrowseForFolderW')
@winfunctype('SHELL32.dll')
def SHLoadInProc(rclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetDesktopFolder(ppshf: POINTER(win32more.Windows.Win32.UI.Shell.IShellFolder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHChangeNotify(wEventId: Int32, uFlags: win32more.Windows.Win32.UI.Shell.SHCNF_FLAGS, dwItem1: VoidPtr, dwItem2: VoidPtr) -> Void: ...
@winfunctype('SHELL32.dll')
def SHAddToRecentDocs(uFlags: UInt32, pv: VoidPtr) -> Void: ...
@winfunctype('SHELL32.dll')
def SHHandleUpdateImage(pidlExtra: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> Int32: ...
@winfunctype('SHELL32.dll')
def SHUpdateImageA(pszHashItem: win32more.Windows.Win32.Foundation.PSTR, iIndex: Int32, uFlags: UInt32, iImageIndex: Int32) -> Void: ...
@winfunctype('SHELL32.dll')
def SHUpdateImageW(pszHashItem: win32more.Windows.Win32.Foundation.PWSTR, iIndex: Int32, uFlags: UInt32, iImageIndex: Int32) -> Void: ...
SHUpdateImage = UnicodeAlias('SHUpdateImageW')
@winfunctype('SHELL32.dll')
def SHChangeNotifyRegister(hwnd: win32more.Windows.Win32.Foundation.HWND, fSources: win32more.Windows.Win32.UI.Shell.SHCNRF_SOURCE, fEvents: Int32, wMsg: UInt32, cEntries: Int32, pshcne: POINTER(win32more.Windows.Win32.UI.Shell.SHChangeNotifyEntry)) -> UInt32: ...
@winfunctype('SHELL32.dll')
def SHChangeNotifyDeregister(ulID: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHChangeNotification_Lock(hChange: win32more.Windows.Win32.Foundation.HANDLE, dwProcId: UInt32, pppidl: POINTER(POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST))), plEvent: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('SHELL32.dll')
def SHChangeNotification_Unlock(hLock: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHGetRealIDL(psf: win32more.Windows.Win32.UI.Shell.IShellFolder, pidlSimple: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), ppidlReal: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetInstanceExplorer(ppunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetDataFromIDListA(psf: win32more.Windows.Win32.UI.Shell.IShellFolder, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), nFormat: win32more.Windows.Win32.UI.Shell.SHGDFIL_FORMAT, pv: VoidPtr, cb: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetDataFromIDListW(psf: win32more.Windows.Win32.UI.Shell.IShellFolder, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), nFormat: win32more.Windows.Win32.UI.Shell.SHGDFIL_FORMAT, pv: VoidPtr, cb: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
SHGetDataFromIDList = UnicodeAlias('SHGetDataFromIDListW')
@winfunctype('SHELL32.dll')
def RestartDialog(hwnd: win32more.Windows.Win32.Foundation.HWND, pszPrompt: win32more.Windows.Win32.Foundation.PWSTR, dwReturn: UInt32) -> Int32: ...
@winfunctype('SHELL32.dll')
def RestartDialogEx(hwnd: win32more.Windows.Win32.Foundation.HWND, pszPrompt: win32more.Windows.Win32.Foundation.PWSTR, dwReturn: UInt32, dwReasonCode: UInt32) -> Int32: ...
@winfunctype('SHELL32.dll')
def SHCoCreateInstance(pszCLSID: win32more.Windows.Win32.Foundation.PWSTR, pclsid: POINTER(Guid), pUnkOuter: win32more.Windows.Win32.System.Com.IUnknown, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateDataObject(pidlFolder: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), cidl: UInt32, apidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)), pdtInner: win32more.Windows.Win32.System.Com.IDataObject, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def CIDLData_CreateFromIDArray(pidlFolder: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), cidl: UInt32, apidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)), ppdtobj: POINTER(win32more.Windows.Win32.System.Com.IDataObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateStdEnumFmtEtc(cfmt: UInt32, afmt: POINTER(win32more.Windows.Win32.System.Com.FORMATETC), ppenumFormatEtc: POINTER(win32more.Windows.Win32.System.Com.IEnumFORMATETC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHDoDragDrop(hwnd: win32more.Windows.Win32.Foundation.HWND, pdata: win32more.Windows.Win32.System.Com.IDataObject, pdsrc: win32more.Windows.Win32.System.Ole.IDropSource, dwEffect: win32more.Windows.Win32.System.Ole.DROPEFFECT, pdwEffect: POINTER(win32more.Windows.Win32.System.Ole.DROPEFFECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def DAD_SetDragImage(him: win32more.Windows.Win32.UI.Controls.HIMAGELIST, pptOffset: POINTER(win32more.Windows.Win32.Foundation.POINT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def DAD_DragEnterEx(hwndTarget: win32more.Windows.Win32.Foundation.HWND, ptStart: win32more.Windows.Win32.Foundation.POINT) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def DAD_DragEnterEx2(hwndTarget: win32more.Windows.Win32.Foundation.HWND, ptStart: win32more.Windows.Win32.Foundation.POINT, pdtObject: win32more.Windows.Win32.System.Com.IDataObject) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def DAD_ShowDragImage(fShow: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def DAD_DragMove(pt: win32more.Windows.Win32.Foundation.POINT) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def DAD_DragLeave() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def DAD_AutoScroll(hwnd: win32more.Windows.Win32.Foundation.HWND, pad: POINTER(win32more.Windows.Win32.UI.Shell.AUTO_SCROLL_DATA), pptNow: POINTER(win32more.Windows.Win32.Foundation.POINT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def ReadCabinetState(pcs: POINTER(win32more.Windows.Win32.UI.Shell.CABINETSTATE), cLength: Int32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def WriteCabinetState(pcs: POINTER(win32more.Windows.Win32.UI.Shell.CABINETSTATE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def PathMakeUniqueName(pszUniqueName: win32more.Windows.Win32.Foundation.PWSTR, cchMax: UInt32, pszTemplate: win32more.Windows.Win32.Foundation.PWSTR, pszLongPlate: win32more.Windows.Win32.Foundation.PWSTR, pszDir: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def PathIsExe(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def PathCleanupSpec(pszDir: win32more.Windows.Win32.Foundation.PWSTR, pszSpec: win32more.Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('SHELL32.dll')
def PathResolve(pszPath: win32more.Windows.Win32.Foundation.PWSTR, dirs: POINTER(POINTER(UInt16)), fFlags: UInt32) -> Int32: ...
@winfunctype('SHELL32.dll')
def GetFileNameFromBrowse(hwnd: win32more.Windows.Win32.Foundation.HWND, pszFilePath: win32more.Windows.Win32.Foundation.PWSTR, cchFilePath: UInt32, pszWorkingDir: win32more.Windows.Win32.Foundation.PWSTR, pszDefExt: win32more.Windows.Win32.Foundation.PWSTR, pszFilters: win32more.Windows.Win32.Foundation.PWSTR, pszTitle: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def DriveType(iDrive: Int32) -> Int32: ...
@winfunctype('SHELL32.dll')
def RealDriveType(iDrive: Int32, fOKToHitNet: win32more.Windows.Win32.Foundation.BOOL) -> Int32: ...
@winfunctype('SHELL32.dll')
def IsNetDrive(iDrive: Int32) -> Int32: ...
@winfunctype('SHELL32.dll')
def Shell_MergeMenus(hmDst: win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU, hmSrc: win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU, uInsert: UInt32, uIDAdjust: UInt32, uIDAdjustMax: UInt32, uFlags: win32more.Windows.Win32.UI.Shell.MM_FLAGS) -> UInt32: ...
@winfunctype('SHELL32.dll')
def SHObjectProperties(hwnd: win32more.Windows.Win32.Foundation.HWND, shopObjectType: UInt32, pszObjectName: win32more.Windows.Win32.Foundation.PWSTR, pszPropertyPage: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHFormatDrive(hwnd: win32more.Windows.Win32.Foundation.HWND, drive: UInt32, fmtID: win32more.Windows.Win32.UI.Shell.SHFMT_ID, options: UInt32) -> UInt32: ...
@winfunctype('SHELL32.dll')
def SHDestroyPropSheetExtArray(hpsxa: win32more.Windows.Win32.UI.Shell.HPSXA) -> Void: ...
@winfunctype('SHELL32.dll')
def SHAddFromPropSheetExtArray(hpsxa: win32more.Windows.Win32.UI.Shell.HPSXA, lpfnAddPage: win32more.Windows.Win32.UI.Controls.LPFNSVADDPROPSHEETPAGE, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> UInt32: ...
@winfunctype('SHELL32.dll')
def SHReplaceFromPropSheetExtArray(hpsxa: win32more.Windows.Win32.UI.Shell.HPSXA, uPageID: UInt32, lpfnReplaceWith: win32more.Windows.Win32.UI.Controls.LPFNSVADDPROPSHEETPAGE, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> UInt32: ...
@winfunctype('SHELL32.dll')
def OpenRegStream(hkey: win32more.Windows.Win32.System.Registry.HKEY, pszSubkey: win32more.Windows.Win32.Foundation.PWSTR, pszValue: win32more.Windows.Win32.Foundation.PWSTR, grfMode: UInt32) -> win32more.Windows.Win32.System.Com.IStream: ...
@winfunctype('SHELL32.dll')
def SHFindFiles(pidlFolder: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pidlSaveFile: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def PathGetShortPath(pszLongPath: win32more.Windows.Win32.Foundation.PWSTR) -> Void: ...
@winfunctype('SHELL32.dll')
def PathYetAnotherMakeUniqueName(pszUniqueName: win32more.Windows.Win32.Foundation.PWSTR, pszPath: win32more.Windows.Win32.Foundation.PWSTR, pszShort: win32more.Windows.Win32.Foundation.PWSTR, pszFileSpec: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def Win32DeleteFile(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHRestricted(rest: win32more.Windows.Win32.UI.Shell.RESTRICTIONS) -> UInt32: ...
@winfunctype('SHELL32.dll')
def SignalFileOpen(pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def AssocGetDetailsOfPropKey(psf: win32more.Windows.Win32.UI.Shell.IShellFolder, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pkey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pv: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pfFoundPropKey: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHStartNetConnectionDialogW(hwnd: win32more.Windows.Win32.Foundation.HWND, pszRemoteName: win32more.Windows.Win32.Foundation.PWSTR, dwType: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
SHStartNetConnectionDialog = UnicodeAlias('SHStartNetConnectionDialogW')
@winfunctype('SHELL32.dll')
def SHDefExtractIconA(pszIconFile: win32more.Windows.Win32.Foundation.PSTR, iIndex: Int32, uFlags: UInt32, phiconLarge: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.HICON), phiconSmall: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.HICON), nIconSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHDefExtractIconW(pszIconFile: win32more.Windows.Win32.Foundation.PWSTR, iIndex: Int32, uFlags: UInt32, phiconLarge: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.HICON), phiconSmall: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.HICON), nIconSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
SHDefExtractIcon = UnicodeAlias('SHDefExtractIconW')
@winfunctype('SHELL32.dll')
def SHOpenWithDialog(hwndParent: win32more.Windows.Win32.Foundation.HWND, poainfo: POINTER(win32more.Windows.Win32.UI.Shell.OPENASINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def Shell_GetImageLists(phiml: POINTER(win32more.Windows.Win32.UI.Controls.HIMAGELIST), phimlSmall: POINTER(win32more.Windows.Win32.UI.Controls.HIMAGELIST)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def Shell_GetCachedImageIndexA(pszIconPath: win32more.Windows.Win32.Foundation.PSTR, iIconIndex: Int32, uIconFlags: UInt32) -> Int32: ...
@winfunctype('SHELL32.dll')
def Shell_GetCachedImageIndexW(pszIconPath: win32more.Windows.Win32.Foundation.PWSTR, iIconIndex: Int32, uIconFlags: UInt32) -> Int32: ...
Shell_GetCachedImageIndex = UnicodeAlias('Shell_GetCachedImageIndexW')
@winfunctype('SHELL32.dll')
def SHValidateUNC(hwndOwner: win32more.Windows.Win32.Foundation.HWND, pszFile: win32more.Windows.Win32.Foundation.PWSTR, fConnect: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHSetInstanceExplorer(punk: win32more.Windows.Win32.System.Com.IUnknown) -> Void: ...
@winfunctype('SHELL32.dll')
def IsUserAnAdmin() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHShellFolderView_Message(hwndMain: win32more.Windows.Win32.Foundation.HWND, uMsg: UInt32, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.LRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateShellFolderView(pcsfv: POINTER(win32more.Windows.Win32.UI.Shell.SFV_CREATE), ppsv: POINTER(win32more.Windows.Win32.UI.Shell.IShellView)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def CDefFolderMenu_Create2(pidlFolder: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), hwnd: win32more.Windows.Win32.Foundation.HWND, cidl: UInt32, apidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)), psf: win32more.Windows.Win32.UI.Shell.IShellFolder, pfn: win32more.Windows.Win32.UI.Shell.LPFNDFMCALLBACK, nKeys: UInt32, ahkeys: POINTER(win32more.Windows.Win32.System.Registry.HKEY), ppcm: POINTER(win32more.Windows.Win32.UI.Shell.IContextMenu)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateDefaultContextMenu(pdcm: POINTER(win32more.Windows.Win32.UI.Shell.DEFCONTEXTMENU), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHFind_InitMenuPopup(hmenu: win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU, hwndOwner: win32more.Windows.Win32.Foundation.HWND, idCmdFirst: UInt32, idCmdLast: UInt32) -> win32more.Windows.Win32.UI.Shell.IContextMenu: ...
@winfunctype('SHELL32.dll')
def SHCreateShellFolderViewEx(pcsfv: POINTER(win32more.Windows.Win32.UI.Shell.CSFV), ppsv: POINTER(win32more.Windows.Win32.UI.Shell.IShellView)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetSetSettings(lpss: POINTER(win32more.Windows.Win32.UI.Shell.SHELLSTATEA), dwMask: win32more.Windows.Win32.UI.Shell.SSF_MASK, bSet: win32more.Windows.Win32.Foundation.BOOL) -> Void: ...
@winfunctype('SHELL32.dll')
def SHGetSettings(psfs: POINTER(win32more.Windows.Win32.UI.Shell.SHELLFLAGSTATE), dwMask: UInt32) -> Void: ...
@winfunctype('SHELL32.dll')
def SHBindToParent(pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), riid: POINTER(Guid), ppv: POINTER(VoidPtr), ppidlLast: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHBindToFolderIDListParent(psfRoot: win32more.Windows.Win32.UI.Shell.IShellFolder, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), riid: POINTER(Guid), ppv: POINTER(VoidPtr), ppidlLast: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHBindToFolderIDListParentEx(psfRoot: win32more.Windows.Win32.UI.Shell.IShellFolder, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), ppbc: win32more.Windows.Win32.System.Com.IBindCtx, riid: POINTER(Guid), ppv: POINTER(VoidPtr), ppidlLast: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHBindToObject(psf: win32more.Windows.Win32.UI.Shell.IShellFolder, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pbc: win32more.Windows.Win32.System.Com.IBindCtx, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHParseDisplayName(pszName: win32more.Windows.Win32.Foundation.PWSTR, pbc: win32more.Windows.Win32.System.Com.IBindCtx, ppidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)), sfgaoIn: UInt32, psfgaoOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHPathPrepareForWriteA(hwnd: win32more.Windows.Win32.Foundation.HWND, punkEnableModless: win32more.Windows.Win32.System.Com.IUnknown, pszPath: win32more.Windows.Win32.Foundation.PSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHPathPrepareForWriteW(hwnd: win32more.Windows.Win32.Foundation.HWND, punkEnableModless: win32more.Windows.Win32.System.Com.IUnknown, pszPath: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
SHPathPrepareForWrite = UnicodeAlias('SHPathPrepareForWriteW')
@winfunctype('SHELL32.dll')
def SHCreateFileExtractIconW(pszFile: win32more.Windows.Win32.Foundation.PWSTR, dwFileAttributes: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
SHCreateFileExtractIcon = UnicodeAlias('SHCreateFileExtractIconW')
@winfunctype('SHELL32.dll')
def SHLimitInputEdit(hwndEdit: win32more.Windows.Win32.Foundation.HWND, psf: win32more.Windows.Win32.UI.Shell.IShellFolder) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetAttributesFromDataObject(pdo: win32more.Windows.Win32.System.Com.IDataObject, dwAttributeMask: UInt32, pdwAttributes: POINTER(UInt32), pcItems: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHMapPIDLToSystemImageListIndex(pshf: win32more.Windows.Win32.UI.Shell.IShellFolder, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), piIndexSel: POINTER(Int32)) -> Int32: ...
@winfunctype('SHELL32.dll')
def SHCLSIDFromString(psz: win32more.Windows.Win32.Foundation.PWSTR, pclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def PickIconDlg(hwnd: win32more.Windows.Win32.Foundation.HWND, pszIconPath: win32more.Windows.Win32.Foundation.PWSTR, cchIconPath: UInt32, piIconIndex: POINTER(Int32)) -> Int32: ...
@winfunctype('SHELL32.dll')
def StgMakeUniqueName(pstgParent: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, pszFileSpec: win32more.Windows.Win32.Foundation.PWSTR, grfMode: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHChangeNotifyRegisterThread(status: win32more.Windows.Win32.UI.Shell.SCNRT_STATUS) -> Void: ...
@winfunctype('SHELL32.dll')
def PathQualify(psz: win32more.Windows.Win32.Foundation.PWSTR) -> Void: ...
@winfunctype('SHELL32.dll')
def PathIsSlowA(pszFile: win32more.Windows.Win32.Foundation.PSTR, dwAttr: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def PathIsSlowW(pszFile: win32more.Windows.Win32.Foundation.PWSTR, dwAttr: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathIsSlow = UnicodeAlias('PathIsSlowW')
@winfunctype('SHELL32.dll')
def SHCreatePropSheetExtArray(hKey: win32more.Windows.Win32.System.Registry.HKEY, pszSubKey: win32more.Windows.Win32.Foundation.PWSTR, max_iface: UInt32) -> win32more.Windows.Win32.UI.Shell.HPSXA: ...
@winfunctype('SHELL32.dll')
def SHOpenPropSheetW(pszCaption: win32more.Windows.Win32.Foundation.PWSTR, ahkeys: POINTER(win32more.Windows.Win32.System.Registry.HKEY), ckeys: UInt32, pclsidDefault: POINTER(Guid), pdtobj: win32more.Windows.Win32.System.Com.IDataObject, psb: win32more.Windows.Win32.UI.Shell.IShellBrowser, pStartPage: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
SHOpenPropSheet = UnicodeAlias('SHOpenPropSheetW')
@winfunctype('SHDOCVW.dll')
def SoftwareUpdateMessageBox(hWnd: win32more.Windows.Win32.Foundation.HWND, pszDistUnit: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, psdi: POINTER(win32more.Windows.Win32.System.Com.Urlmon.SOFTDISTINFO)) -> UInt32: ...
@winfunctype('SHELL32.dll')
def SHMultiFileProperties(pdtobj: win32more.Windows.Win32.System.Com.IDataObject, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHCreateQueryCancelAutoPlayMoniker(ppmoniker: POINTER(win32more.Windows.Win32.System.Com.IMoniker)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHDOCVW.dll')
def ImportPrivacySettings(pszFilename: win32more.Windows.Win32.Foundation.PWSTR, pfParsePrivacyPreferences: POINTER(win32more.Windows.Win32.Foundation.BOOL), pfParsePerSiteRules: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-shcore-scaling-l1-1-0.dll')
def GetScaleFactorForDevice(deviceType: win32more.Windows.Win32.UI.Shell.DISPLAY_DEVICE_TYPE) -> win32more.Windows.Win32.UI.Shell.Common.DEVICE_SCALE_FACTOR: ...
@winfunctype('api-ms-win-shcore-scaling-l1-1-0.dll')
def RegisterScaleChangeNotifications(displayDevice: win32more.Windows.Win32.UI.Shell.DISPLAY_DEVICE_TYPE, hwndNotify: win32more.Windows.Win32.Foundation.HWND, uMsgNotify: UInt32, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-shcore-scaling-l1-1-0.dll')
def RevokeScaleChangeNotifications(displayDevice: win32more.Windows.Win32.UI.Shell.DISPLAY_DEVICE_TYPE, dwCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-shcore-scaling-l1-1-1.dll')
def GetScaleFactorForMonitor(hMon: win32more.Windows.Win32.Graphics.Gdi.HMONITOR, pScale: POINTER(win32more.Windows.Win32.UI.Shell.Common.DEVICE_SCALE_FACTOR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-shcore-scaling-l1-1-1.dll')
def RegisterScaleChangeEvent(hEvent: win32more.Windows.Win32.Foundation.HANDLE, pdwCookie: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-shcore-scaling-l1-1-1.dll')
def UnregisterScaleChangeEvent(dwCookie: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-shcore-scaling-l1-1-2.dll')
def GetDpiForShellUIComponent(param0: win32more.Windows.Win32.UI.Shell.SHELL_UI_COMPONENT) -> UInt32: ...
@winfunctype('SHELL32.dll')
def CommandLineToArgvW(lpCmdLine: win32more.Windows.Win32.Foundation.PWSTR, pNumArgs: POINTER(Int32)) -> POINTER(win32more.Windows.Win32.Foundation.PWSTR): ...
@winfunctype('SHELL32.dll')
def DragQueryFileA(hDrop: win32more.Windows.Win32.UI.Shell.HDROP, iFile: UInt32, lpszFile: win32more.Windows.Win32.Foundation.PSTR, cch: UInt32) -> UInt32: ...
@winfunctype('SHELL32.dll')
def DragQueryFileW(hDrop: win32more.Windows.Win32.UI.Shell.HDROP, iFile: UInt32, lpszFile: win32more.Windows.Win32.Foundation.PWSTR, cch: UInt32) -> UInt32: ...
DragQueryFile = UnicodeAlias('DragQueryFileW')
@winfunctype('SHELL32.dll')
def DragQueryPoint(hDrop: win32more.Windows.Win32.UI.Shell.HDROP, ppt: POINTER(win32more.Windows.Win32.Foundation.POINT)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def DragFinish(hDrop: win32more.Windows.Win32.UI.Shell.HDROP) -> Void: ...
@winfunctype('SHELL32.dll')
def DragAcceptFiles(hWnd: win32more.Windows.Win32.Foundation.HWND, fAccept: win32more.Windows.Win32.Foundation.BOOL) -> Void: ...
@winfunctype('SHELL32.dll')
def ShellExecuteA(hwnd: win32more.Windows.Win32.Foundation.HWND, lpOperation: win32more.Windows.Win32.Foundation.PSTR, lpFile: win32more.Windows.Win32.Foundation.PSTR, lpParameters: win32more.Windows.Win32.Foundation.PSTR, lpDirectory: win32more.Windows.Win32.Foundation.PSTR, nShowCmd: win32more.Windows.Win32.UI.WindowsAndMessaging.SHOW_WINDOW_CMD) -> win32more.Windows.Win32.Foundation.HINSTANCE: ...
@winfunctype('SHELL32.dll')
def ShellExecuteW(hwnd: win32more.Windows.Win32.Foundation.HWND, lpOperation: win32more.Windows.Win32.Foundation.PWSTR, lpFile: win32more.Windows.Win32.Foundation.PWSTR, lpParameters: win32more.Windows.Win32.Foundation.PWSTR, lpDirectory: win32more.Windows.Win32.Foundation.PWSTR, nShowCmd: win32more.Windows.Win32.UI.WindowsAndMessaging.SHOW_WINDOW_CMD) -> win32more.Windows.Win32.Foundation.HINSTANCE: ...
ShellExecute = UnicodeAlias('ShellExecuteW')
@winfunctype('SHELL32.dll')
def FindExecutableA(lpFile: win32more.Windows.Win32.Foundation.PSTR, lpDirectory: win32more.Windows.Win32.Foundation.PSTR, lpResult: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HINSTANCE: ...
@winfunctype('SHELL32.dll')
def FindExecutableW(lpFile: win32more.Windows.Win32.Foundation.PWSTR, lpDirectory: win32more.Windows.Win32.Foundation.PWSTR, lpResult: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HINSTANCE: ...
FindExecutable = UnicodeAlias('FindExecutableW')
@winfunctype('SHELL32.dll')
def ShellAboutA(hWnd: win32more.Windows.Win32.Foundation.HWND, szApp: win32more.Windows.Win32.Foundation.PSTR, szOtherStuff: win32more.Windows.Win32.Foundation.PSTR, hIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON) -> Int32: ...
@winfunctype('SHELL32.dll')
def ShellAboutW(hWnd: win32more.Windows.Win32.Foundation.HWND, szApp: win32more.Windows.Win32.Foundation.PWSTR, szOtherStuff: win32more.Windows.Win32.Foundation.PWSTR, hIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON) -> Int32: ...
ShellAbout = UnicodeAlias('ShellAboutW')
@winfunctype('SHELL32.dll')
def DuplicateIcon(hInst: win32more.Windows.Win32.Foundation.HINSTANCE, hIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON) -> win32more.Windows.Win32.UI.WindowsAndMessaging.HICON: ...
@winfunctype('SHELL32.dll')
def ExtractAssociatedIconA(hInst: win32more.Windows.Win32.Foundation.HINSTANCE, pszIconPath: win32more.Windows.Win32.Foundation.PSTR, piIcon: POINTER(UInt16)) -> win32more.Windows.Win32.UI.WindowsAndMessaging.HICON: ...
@winfunctype('SHELL32.dll')
def ExtractAssociatedIconW(hInst: win32more.Windows.Win32.Foundation.HINSTANCE, pszIconPath: win32more.Windows.Win32.Foundation.PWSTR, piIcon: POINTER(UInt16)) -> win32more.Windows.Win32.UI.WindowsAndMessaging.HICON: ...
ExtractAssociatedIcon = UnicodeAlias('ExtractAssociatedIconW')
@winfunctype('SHELL32.dll')
def ExtractAssociatedIconExA(hInst: win32more.Windows.Win32.Foundation.HINSTANCE, pszIconPath: win32more.Windows.Win32.Foundation.PSTR, piIconIndex: POINTER(UInt16), piIconId: POINTER(UInt16)) -> win32more.Windows.Win32.UI.WindowsAndMessaging.HICON: ...
@winfunctype('SHELL32.dll')
def ExtractAssociatedIconExW(hInst: win32more.Windows.Win32.Foundation.HINSTANCE, pszIconPath: win32more.Windows.Win32.Foundation.PWSTR, piIconIndex: POINTER(UInt16), piIconId: POINTER(UInt16)) -> win32more.Windows.Win32.UI.WindowsAndMessaging.HICON: ...
ExtractAssociatedIconEx = UnicodeAlias('ExtractAssociatedIconExW')
@winfunctype('SHELL32.dll')
def ExtractIconA(hInst: win32more.Windows.Win32.Foundation.HINSTANCE, pszExeFileName: win32more.Windows.Win32.Foundation.PSTR, nIconIndex: UInt32) -> win32more.Windows.Win32.UI.WindowsAndMessaging.HICON: ...
@winfunctype('SHELL32.dll')
def ExtractIconW(hInst: win32more.Windows.Win32.Foundation.HINSTANCE, pszExeFileName: win32more.Windows.Win32.Foundation.PWSTR, nIconIndex: UInt32) -> win32more.Windows.Win32.UI.WindowsAndMessaging.HICON: ...
ExtractIcon = UnicodeAlias('ExtractIconW')
@winfunctype('SHELL32.dll')
def SHAppBarMessage(dwMessage: UInt32, pData: POINTER(win32more.Windows.Win32.UI.Shell.APPBARDATA)) -> UIntPtr: ...
@winfunctype('SHELL32.dll')
def DoEnvironmentSubstA(pszSrc: win32more.Windows.Win32.Foundation.PSTR, cchSrc: UInt32) -> UInt32: ...
@winfunctype('SHELL32.dll')
def DoEnvironmentSubstW(pszSrc: win32more.Windows.Win32.Foundation.PWSTR, cchSrc: UInt32) -> UInt32: ...
DoEnvironmentSubst = UnicodeAlias('DoEnvironmentSubstW')
@winfunctype('SHELL32.dll')
def ExtractIconExA(lpszFile: win32more.Windows.Win32.Foundation.PSTR, nIconIndex: Int32, phiconLarge: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.HICON), phiconSmall: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.HICON), nIcons: UInt32) -> UInt32: ...
@winfunctype('SHELL32.dll')
def ExtractIconExW(lpszFile: win32more.Windows.Win32.Foundation.PWSTR, nIconIndex: Int32, phiconLarge: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.HICON), phiconSmall: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.HICON), nIcons: UInt32) -> UInt32: ...
ExtractIconEx = UnicodeAlias('ExtractIconExW')
@winfunctype('SHELL32.dll')
def SHFileOperationA(lpFileOp: POINTER(win32more.Windows.Win32.UI.Shell.SHFILEOPSTRUCTA)) -> Int32: ...
@winfunctype('SHELL32.dll')
def SHFileOperationW(lpFileOp: POINTER(win32more.Windows.Win32.UI.Shell.SHFILEOPSTRUCTW)) -> Int32: ...
SHFileOperation = UnicodeAlias('SHFileOperationW')
@winfunctype('SHELL32.dll')
def SHFreeNameMappings(hNameMappings: win32more.Windows.Win32.Foundation.HANDLE) -> Void: ...
@winfunctype('SHELL32.dll')
def ShellExecuteExA(pExecInfo: POINTER(win32more.Windows.Win32.UI.Shell.SHELLEXECUTEINFOA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def ShellExecuteExW(pExecInfo: POINTER(win32more.Windows.Win32.UI.Shell.SHELLEXECUTEINFOW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
ShellExecuteEx = UnicodeAlias('ShellExecuteExW')
@winfunctype('SHELL32.dll')
def SHCreateProcessAsUserW(pscpi: POINTER(win32more.Windows.Win32.UI.Shell.SHCREATEPROCESSINFOW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHEvaluateSystemCommandTemplate(pszCmdTemplate: win32more.Windows.Win32.Foundation.PWSTR, ppszApplication: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ppszCommandLine: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ppszParameters: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def AssocCreateForClasses(rgClasses: POINTER(win32more.Windows.Win32.UI.Shell.ASSOCIATIONELEMENT), cClasses: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHQueryRecycleBinA(pszRootPath: win32more.Windows.Win32.Foundation.PSTR, pSHQueryRBInfo: POINTER(win32more.Windows.Win32.UI.Shell.SHQUERYRBINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHQueryRecycleBinW(pszRootPath: win32more.Windows.Win32.Foundation.PWSTR, pSHQueryRBInfo: POINTER(win32more.Windows.Win32.UI.Shell.SHQUERYRBINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
SHQueryRecycleBin = UnicodeAlias('SHQueryRecycleBinW')
@winfunctype('SHELL32.dll')
def SHEmptyRecycleBinA(hwnd: win32more.Windows.Win32.Foundation.HWND, pszRootPath: win32more.Windows.Win32.Foundation.PSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHEmptyRecycleBinW(hwnd: win32more.Windows.Win32.Foundation.HWND, pszRootPath: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
SHEmptyRecycleBin = UnicodeAlias('SHEmptyRecycleBinW')
@winfunctype('SHELL32.dll')
def SHQueryUserNotificationState(pquns: POINTER(win32more.Windows.Win32.UI.Shell.QUERY_USER_NOTIFICATION_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def Shell_NotifyIconA(dwMessage: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_MESSAGE, lpData: POINTER(win32more.Windows.Win32.UI.Shell.NOTIFYICONDATAA)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def Shell_NotifyIconW(dwMessage: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_MESSAGE, lpData: POINTER(win32more.Windows.Win32.UI.Shell.NOTIFYICONDATAW)) -> win32more.Windows.Win32.Foundation.BOOL: ...
Shell_NotifyIcon = UnicodeAlias('Shell_NotifyIconW')
@winfunctype('SHELL32.dll')
def Shell_NotifyIconGetRect(identifier: POINTER(win32more.Windows.Win32.UI.Shell.NOTIFYICONIDENTIFIER), iconLocation: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetFileInfoA(pszPath: win32more.Windows.Win32.Foundation.PSTR, dwFileAttributes: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES, psfi: POINTER(win32more.Windows.Win32.UI.Shell.SHFILEINFOA), cbFileInfo: UInt32, uFlags: win32more.Windows.Win32.UI.Shell.SHGFI_FLAGS) -> UIntPtr: ...
@winfunctype('SHELL32.dll')
def SHGetFileInfoW(pszPath: win32more.Windows.Win32.Foundation.PWSTR, dwFileAttributes: win32more.Windows.Win32.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES, psfi: POINTER(win32more.Windows.Win32.UI.Shell.SHFILEINFOW), cbFileInfo: UInt32, uFlags: win32more.Windows.Win32.UI.Shell.SHGFI_FLAGS) -> UIntPtr: ...
SHGetFileInfo = UnicodeAlias('SHGetFileInfoW')
@winfunctype('SHELL32.dll')
def SHGetStockIconInfo(siid: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID, uFlags: win32more.Windows.Win32.UI.Shell.SHGSI_FLAGS, psii: POINTER(win32more.Windows.Win32.UI.Shell.SHSTOCKICONINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetDiskFreeSpaceExA(pszDirectoryName: win32more.Windows.Win32.Foundation.PSTR, pulFreeBytesAvailableToCaller: POINTER(UInt64), pulTotalNumberOfBytes: POINTER(UInt64), pulTotalNumberOfFreeBytes: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHGetDiskFreeSpaceExW(pszDirectoryName: win32more.Windows.Win32.Foundation.PWSTR, pulFreeBytesAvailableToCaller: POINTER(UInt64), pulTotalNumberOfBytes: POINTER(UInt64), pulTotalNumberOfFreeBytes: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
SHGetDiskFreeSpaceEx = UnicodeAlias('SHGetDiskFreeSpaceExW')
@winfunctype('SHELL32.dll')
def SHGetNewLinkInfoA(pszLinkTo: win32more.Windows.Win32.Foundation.PSTR, pszDir: win32more.Windows.Win32.Foundation.PSTR, pszName: win32more.Windows.Win32.Foundation.PSTR, pfMustCopy: POINTER(win32more.Windows.Win32.Foundation.BOOL), uFlags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHGetNewLinkInfoW(pszLinkTo: win32more.Windows.Win32.Foundation.PWSTR, pszDir: win32more.Windows.Win32.Foundation.PWSTR, pszName: win32more.Windows.Win32.Foundation.PWSTR, pfMustCopy: POINTER(win32more.Windows.Win32.Foundation.BOOL), uFlags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
SHGetNewLinkInfo = UnicodeAlias('SHGetNewLinkInfoW')
@winfunctype('SHELL32.dll')
def SHInvokePrinterCommandA(hwnd: win32more.Windows.Win32.Foundation.HWND, uAction: UInt32, lpBuf1: win32more.Windows.Win32.Foundation.PSTR, lpBuf2: win32more.Windows.Win32.Foundation.PSTR, fModal: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHInvokePrinterCommandW(hwnd: win32more.Windows.Win32.Foundation.HWND, uAction: UInt32, lpBuf1: win32more.Windows.Win32.Foundation.PWSTR, lpBuf2: win32more.Windows.Win32.Foundation.PWSTR, fModal: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
SHInvokePrinterCommand = UnicodeAlias('SHInvokePrinterCommandW')
@winfunctype('SHELL32.dll')
def SHLoadNonloadedIconOverlayIdentifiers() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHIsFileAvailableOffline(pwszPath: win32more.Windows.Win32.Foundation.PWSTR, pdwStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHSetLocalizedName(pszPath: win32more.Windows.Win32.Foundation.PWSTR, pszResModule: win32more.Windows.Win32.Foundation.PWSTR, idsRes: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHRemoveLocalizedName(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def SHGetLocalizedName(pszPath: win32more.Windows.Win32.Foundation.PWSTR, pszResModule: win32more.Windows.Win32.Foundation.PWSTR, cch: UInt32, pidsRes: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@cfunctype('SHLWAPI.dll', variadic=True)
def ShellMessageBoxA(hAppInst: win32more.Windows.Win32.Foundation.HINSTANCE, hWnd: win32more.Windows.Win32.Foundation.HWND, lpcText: win32more.Windows.Win32.Foundation.PSTR, lpcTitle: win32more.Windows.Win32.Foundation.PSTR, fuStyle: win32more.Windows.Win32.UI.WindowsAndMessaging.MESSAGEBOX_STYLE, *__arglist) -> Int32: ...
@cfunctype('SHLWAPI.dll', variadic=True)
def ShellMessageBoxW(hAppInst: win32more.Windows.Win32.Foundation.HINSTANCE, hWnd: win32more.Windows.Win32.Foundation.HWND, lpcText: win32more.Windows.Win32.Foundation.PWSTR, lpcTitle: win32more.Windows.Win32.Foundation.PWSTR, fuStyle: win32more.Windows.Win32.UI.WindowsAndMessaging.MESSAGEBOX_STYLE, *__arglist) -> Int32: ...
ShellMessageBox = UnicodeAlias('ShellMessageBoxW')
@winfunctype('SHELL32.dll')
def IsLFNDriveA(pszPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def IsLFNDriveW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
IsLFNDrive = UnicodeAlias('IsLFNDriveW')
@winfunctype('SHELL32.dll')
def SHEnumerateUnreadMailAccountsW(hKeyUser: win32more.Windows.Win32.System.Registry.HKEY, dwIndex: UInt32, pszMailAddress: win32more.Windows.Win32.Foundation.PWSTR, cchMailAddress: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
SHEnumerateUnreadMailAccounts = UnicodeAlias('SHEnumerateUnreadMailAccountsW')
@winfunctype('SHELL32.dll')
def SHGetUnreadMailCountW(hKeyUser: win32more.Windows.Win32.System.Registry.HKEY, pszMailAddress: win32more.Windows.Win32.Foundation.PWSTR, pdwCount: POINTER(UInt32), pFileTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME), pszShellExecuteCommand: win32more.Windows.Win32.Foundation.PWSTR, cchShellExecuteCommand: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
SHGetUnreadMailCount = UnicodeAlias('SHGetUnreadMailCountW')
@winfunctype('SHELL32.dll')
def SHSetUnreadMailCountW(pszMailAddress: win32more.Windows.Win32.Foundation.PWSTR, dwCount: UInt32, pszShellExecuteCommand: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
SHSetUnreadMailCount = UnicodeAlias('SHSetUnreadMailCountW')
@winfunctype('SHELL32.dll')
def SHTestTokenMembership(hToken: win32more.Windows.Win32.Foundation.HANDLE, ulRID: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHGetImageList(iImageList: Int32, riid: POINTER(Guid), ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHELL32.dll')
def InitNetworkAddressControl() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHELL32.dll')
def SHGetDriveMedia(pszDrive: win32more.Windows.Win32.Foundation.PWSTR, pdwMediaContent: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def StrChrA(pszStart: win32more.Windows.Win32.Foundation.PSTR, wMatch: UInt16) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def StrChrW(pszStart: win32more.Windows.Win32.Foundation.PWSTR, wMatch: Char) -> win32more.Windows.Win32.Foundation.PWSTR: ...
StrChr = UnicodeAlias('StrChrW')
@winfunctype('SHLWAPI.dll')
def StrChrIA(pszStart: win32more.Windows.Win32.Foundation.PSTR, wMatch: UInt16) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def StrChrIW(pszStart: win32more.Windows.Win32.Foundation.PWSTR, wMatch: Char) -> win32more.Windows.Win32.Foundation.PWSTR: ...
StrChrI = UnicodeAlias('StrChrIW')
@winfunctype('SHLWAPI.dll')
def StrChrNW(pszStart: win32more.Windows.Win32.Foundation.PWSTR, wMatch: Char, cchMax: UInt32) -> win32more.Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def StrChrNIW(pszStart: win32more.Windows.Win32.Foundation.PWSTR, wMatch: Char, cchMax: UInt32) -> win32more.Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def StrCmpNA(psz1: win32more.Windows.Win32.Foundation.PSTR, psz2: win32more.Windows.Win32.Foundation.PSTR, nChar: Int32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrCmpNW(psz1: win32more.Windows.Win32.Foundation.PWSTR, psz2: win32more.Windows.Win32.Foundation.PWSTR, nChar: Int32) -> Int32: ...
StrCmpN = UnicodeAlias('StrCmpNW')
@winfunctype('SHLWAPI.dll')
def StrCmpNIA(psz1: win32more.Windows.Win32.Foundation.PSTR, psz2: win32more.Windows.Win32.Foundation.PSTR, nChar: Int32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrCmpNIW(psz1: win32more.Windows.Win32.Foundation.PWSTR, psz2: win32more.Windows.Win32.Foundation.PWSTR, nChar: Int32) -> Int32: ...
StrCmpNI = UnicodeAlias('StrCmpNIW')
@winfunctype('SHLWAPI.dll')
def StrCSpnA(pszStr: win32more.Windows.Win32.Foundation.PSTR, pszSet: win32more.Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrCSpnW(pszStr: win32more.Windows.Win32.Foundation.PWSTR, pszSet: win32more.Windows.Win32.Foundation.PWSTR) -> Int32: ...
StrCSpn = UnicodeAlias('StrCSpnW')
@winfunctype('SHLWAPI.dll')
def StrCSpnIA(pszStr: win32more.Windows.Win32.Foundation.PSTR, pszSet: win32more.Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrCSpnIW(pszStr: win32more.Windows.Win32.Foundation.PWSTR, pszSet: win32more.Windows.Win32.Foundation.PWSTR) -> Int32: ...
StrCSpnI = UnicodeAlias('StrCSpnIW')
@winfunctype('SHLWAPI.dll')
def StrDupA(pszSrch: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def StrDupW(pszSrch: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.PWSTR: ...
StrDup = UnicodeAlias('StrDupW')
@winfunctype('SHLWAPI.dll')
def StrFormatByteSizeEx(ull: UInt64, flags: win32more.Windows.Win32.UI.Shell.SFBS_FLAGS, pszBuf: win32more.Windows.Win32.Foundation.PWSTR, cchBuf: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def StrFormatByteSizeA(dw: UInt32, pszBuf: win32more.Windows.Win32.Foundation.PSTR, cchBuf: UInt32) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def StrFormatByteSize64A(qdw: Int64, pszBuf: win32more.Windows.Win32.Foundation.PSTR, cchBuf: UInt32) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def StrFormatByteSizeW(qdw: Int64, pszBuf: win32more.Windows.Win32.Foundation.PWSTR, cchBuf: UInt32) -> win32more.Windows.Win32.Foundation.PWSTR: ...
StrFormatByteSize = UnicodeAlias('StrFormatByteSizeW')
@winfunctype('SHLWAPI.dll')
def StrFormatKBSizeW(qdw: Int64, pszBuf: win32more.Windows.Win32.Foundation.PWSTR, cchBuf: UInt32) -> win32more.Windows.Win32.Foundation.PWSTR: ...
StrFormatKBSize = UnicodeAlias('StrFormatKBSizeW')
@winfunctype('SHLWAPI.dll')
def StrFormatKBSizeA(qdw: Int64, pszBuf: win32more.Windows.Win32.Foundation.PSTR, cchBuf: UInt32) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def StrFromTimeIntervalA(pszOut: win32more.Windows.Win32.Foundation.PSTR, cchMax: UInt32, dwTimeMS: UInt32, digits: Int32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrFromTimeIntervalW(pszOut: win32more.Windows.Win32.Foundation.PWSTR, cchMax: UInt32, dwTimeMS: UInt32, digits: Int32) -> Int32: ...
StrFromTimeInterval = UnicodeAlias('StrFromTimeIntervalW')
@winfunctype('SHLWAPI.dll')
def StrIsIntlEqualA(fCaseSens: win32more.Windows.Win32.Foundation.BOOL, pszString1: win32more.Windows.Win32.Foundation.PSTR, pszString2: win32more.Windows.Win32.Foundation.PSTR, nChar: Int32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def StrIsIntlEqualW(fCaseSens: win32more.Windows.Win32.Foundation.BOOL, pszString1: win32more.Windows.Win32.Foundation.PWSTR, pszString2: win32more.Windows.Win32.Foundation.PWSTR, nChar: Int32) -> win32more.Windows.Win32.Foundation.BOOL: ...
StrIsIntlEqual = UnicodeAlias('StrIsIntlEqualW')
@winfunctype('SHLWAPI.dll')
def StrNCatA(psz1: win32more.Windows.Win32.Foundation.PSTR, psz2: win32more.Windows.Win32.Foundation.PSTR, cchMax: Int32) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def StrNCatW(psz1: win32more.Windows.Win32.Foundation.PWSTR, psz2: win32more.Windows.Win32.Foundation.PWSTR, cchMax: Int32) -> win32more.Windows.Win32.Foundation.PWSTR: ...
StrNCat = UnicodeAlias('StrNCatW')
@winfunctype('SHLWAPI.dll')
def StrPBrkA(psz: win32more.Windows.Win32.Foundation.PSTR, pszSet: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def StrPBrkW(psz: win32more.Windows.Win32.Foundation.PWSTR, pszSet: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.PWSTR: ...
StrPBrk = UnicodeAlias('StrPBrkW')
@winfunctype('SHLWAPI.dll')
def StrRChrA(pszStart: win32more.Windows.Win32.Foundation.PSTR, pszEnd: win32more.Windows.Win32.Foundation.PSTR, wMatch: UInt16) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def StrRChrW(pszStart: win32more.Windows.Win32.Foundation.PWSTR, pszEnd: win32more.Windows.Win32.Foundation.PWSTR, wMatch: Char) -> win32more.Windows.Win32.Foundation.PWSTR: ...
StrRChr = UnicodeAlias('StrRChrW')
@winfunctype('SHLWAPI.dll')
def StrRChrIA(pszStart: win32more.Windows.Win32.Foundation.PSTR, pszEnd: win32more.Windows.Win32.Foundation.PSTR, wMatch: UInt16) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def StrRChrIW(pszStart: win32more.Windows.Win32.Foundation.PWSTR, pszEnd: win32more.Windows.Win32.Foundation.PWSTR, wMatch: Char) -> win32more.Windows.Win32.Foundation.PWSTR: ...
StrRChrI = UnicodeAlias('StrRChrIW')
@winfunctype('SHLWAPI.dll')
def StrRStrIA(pszSource: win32more.Windows.Win32.Foundation.PSTR, pszLast: win32more.Windows.Win32.Foundation.PSTR, pszSrch: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def StrRStrIW(pszSource: win32more.Windows.Win32.Foundation.PWSTR, pszLast: win32more.Windows.Win32.Foundation.PWSTR, pszSrch: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.PWSTR: ...
StrRStrI = UnicodeAlias('StrRStrIW')
@winfunctype('SHLWAPI.dll')
def StrSpnA(psz: win32more.Windows.Win32.Foundation.PSTR, pszSet: win32more.Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrSpnW(psz: win32more.Windows.Win32.Foundation.PWSTR, pszSet: win32more.Windows.Win32.Foundation.PWSTR) -> Int32: ...
StrSpn = UnicodeAlias('StrSpnW')
@winfunctype('SHLWAPI.dll')
def StrStrA(pszFirst: win32more.Windows.Win32.Foundation.PSTR, pszSrch: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def StrStrW(pszFirst: win32more.Windows.Win32.Foundation.PWSTR, pszSrch: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.PWSTR: ...
StrStr = UnicodeAlias('StrStrW')
@winfunctype('SHLWAPI.dll')
def StrStrIA(pszFirst: win32more.Windows.Win32.Foundation.PSTR, pszSrch: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def StrStrIW(pszFirst: win32more.Windows.Win32.Foundation.PWSTR, pszSrch: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.PWSTR: ...
StrStrI = UnicodeAlias('StrStrIW')
@winfunctype('SHLWAPI.dll')
def StrStrNW(pszFirst: win32more.Windows.Win32.Foundation.PWSTR, pszSrch: win32more.Windows.Win32.Foundation.PWSTR, cchMax: UInt32) -> win32more.Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def StrStrNIW(pszFirst: win32more.Windows.Win32.Foundation.PWSTR, pszSrch: win32more.Windows.Win32.Foundation.PWSTR, cchMax: UInt32) -> win32more.Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def StrToIntA(pszSrc: win32more.Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrToIntW(pszSrc: win32more.Windows.Win32.Foundation.PWSTR) -> Int32: ...
StrToInt = UnicodeAlias('StrToIntW')
@winfunctype('SHLWAPI.dll')
def StrToIntExA(pszString: win32more.Windows.Win32.Foundation.PSTR, dwFlags: Int32, piRet: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def StrToIntExW(pszString: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: Int32, piRet: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
StrToIntEx = UnicodeAlias('StrToIntExW')
@winfunctype('SHLWAPI.dll')
def StrToInt64ExA(pszString: win32more.Windows.Win32.Foundation.PSTR, dwFlags: Int32, pllRet: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def StrToInt64ExW(pszString: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: Int32, pllRet: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.BOOL: ...
StrToInt64Ex = UnicodeAlias('StrToInt64ExW')
@winfunctype('SHLWAPI.dll')
def StrTrimA(psz: win32more.Windows.Win32.Foundation.PSTR, pszTrimChars: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def StrTrimW(psz: win32more.Windows.Win32.Foundation.PWSTR, pszTrimChars: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
StrTrim = UnicodeAlias('StrTrimW')
@winfunctype('SHLWAPI.dll')
def StrCatW(psz1: win32more.Windows.Win32.Foundation.PWSTR, psz2: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def StrCmpW(psz1: win32more.Windows.Win32.Foundation.PWSTR, psz2: win32more.Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrCmpIW(psz1: win32more.Windows.Win32.Foundation.PWSTR, psz2: win32more.Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrCpyW(psz1: win32more.Windows.Win32.Foundation.PWSTR, psz2: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def StrCpyNW(pszDst: win32more.Windows.Win32.Foundation.PWSTR, pszSrc: win32more.Windows.Win32.Foundation.PWSTR, cchMax: Int32) -> win32more.Windows.Win32.Foundation.PWSTR: ...
@winfunctype('SHLWAPI.dll')
def StrCatBuffW(pszDest: win32more.Windows.Win32.Foundation.PWSTR, pszSrc: win32more.Windows.Win32.Foundation.PWSTR, cchDestBuffSize: Int32) -> win32more.Windows.Win32.Foundation.PWSTR: ...
StrCatBuff = UnicodeAlias('StrCatBuffW')
@winfunctype('SHLWAPI.dll')
def StrCatBuffA(pszDest: win32more.Windows.Win32.Foundation.PSTR, pszSrc: win32more.Windows.Win32.Foundation.PSTR, cchDestBuffSize: Int32) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def ChrCmpIA(w1: UInt16, w2: UInt16) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def ChrCmpIW(w1: Char, w2: Char) -> win32more.Windows.Win32.Foundation.BOOL: ...
ChrCmpI = UnicodeAlias('ChrCmpIW')
@winfunctype('SHLWAPI.dll')
def wvnsprintfA(pszDest: win32more.Windows.Win32.Foundation.PSTR, cchDest: Int32, pszFmt: win32more.Windows.Win32.Foundation.PSTR, arglist: POINTER(SByte)) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def wvnsprintfW(pszDest: win32more.Windows.Win32.Foundation.PWSTR, cchDest: Int32, pszFmt: win32more.Windows.Win32.Foundation.PWSTR, arglist: POINTER(SByte)) -> Int32: ...
wvnsprintf = UnicodeAlias('wvnsprintfW')
@cfunctype('SHLWAPI.dll', variadic=True)
def wnsprintfA(pszDest: win32more.Windows.Win32.Foundation.PSTR, cchDest: Int32, pszFmt: win32more.Windows.Win32.Foundation.PSTR, *__arglist) -> Int32: ...
@cfunctype('SHLWAPI.dll', variadic=True)
def wnsprintfW(pszDest: win32more.Windows.Win32.Foundation.PWSTR, cchDest: Int32, pszFmt: win32more.Windows.Win32.Foundation.PWSTR, *__arglist) -> Int32: ...
wnsprintf = UnicodeAlias('wnsprintfW')
@winfunctype('SHLWAPI.dll')
def StrRetToStrA(pstr: POINTER(win32more.Windows.Win32.UI.Shell.Common.STRRET), pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), ppsz: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def StrRetToStrW(pstr: POINTER(win32more.Windows.Win32.UI.Shell.Common.STRRET), pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), ppsz: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
StrRetToStr = UnicodeAlias('StrRetToStrW')
@winfunctype('SHLWAPI.dll')
def StrRetToBufA(pstr: POINTER(win32more.Windows.Win32.UI.Shell.Common.STRRET), pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pszBuf: win32more.Windows.Win32.Foundation.PSTR, cchBuf: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def StrRetToBufW(pstr: POINTER(win32more.Windows.Win32.UI.Shell.Common.STRRET), pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pszBuf: win32more.Windows.Win32.Foundation.PWSTR, cchBuf: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
StrRetToBuf = UnicodeAlias('StrRetToBufW')
@winfunctype('SHLWAPI.dll')
def SHStrDupA(psz: win32more.Windows.Win32.Foundation.PSTR, ppwsz: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHStrDupW(psz: win32more.Windows.Win32.Foundation.PWSTR, ppwsz: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
SHStrDup = UnicodeAlias('SHStrDupW')
@winfunctype('SHLWAPI.dll')
def StrCmpLogicalW(psz1: win32more.Windows.Win32.Foundation.PWSTR, psz2: win32more.Windows.Win32.Foundation.PWSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrCatChainW(pszDst: win32more.Windows.Win32.Foundation.PWSTR, cchDst: UInt32, ichAt: UInt32, pszSrc: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('SHLWAPI.dll')
def StrRetToBSTR(pstr: POINTER(win32more.Windows.Win32.UI.Shell.Common.STRRET), pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHLoadIndirectString(pszSource: win32more.Windows.Win32.Foundation.PWSTR, pszOutBuf: win32more.Windows.Win32.Foundation.PWSTR, cchOutBuf: UInt32, ppvReserved: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def IsCharSpaceA(wch: win32more.Windows.Win32.Foundation.CHAR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def IsCharSpaceW(wch: Char) -> win32more.Windows.Win32.Foundation.BOOL: ...
IsCharSpace = UnicodeAlias('IsCharSpaceW')
@winfunctype('SHLWAPI.dll')
def StrCmpCA(pszStr1: win32more.Windows.Win32.Foundation.PSTR, pszStr2: win32more.Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrCmpCW(pszStr1: win32more.Windows.Win32.Foundation.PWSTR, pszStr2: win32more.Windows.Win32.Foundation.PWSTR) -> Int32: ...
StrCmpC = UnicodeAlias('StrCmpCW')
@winfunctype('SHLWAPI.dll')
def StrCmpICA(pszStr1: win32more.Windows.Win32.Foundation.PSTR, pszStr2: win32more.Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrCmpICW(pszStr1: win32more.Windows.Win32.Foundation.PWSTR, pszStr2: win32more.Windows.Win32.Foundation.PWSTR) -> Int32: ...
StrCmpIC = UnicodeAlias('StrCmpICW')
@winfunctype('SHLWAPI.dll')
def StrCmpNCA(pszStr1: win32more.Windows.Win32.Foundation.PSTR, pszStr2: win32more.Windows.Win32.Foundation.PSTR, nChar: Int32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrCmpNCW(pszStr1: win32more.Windows.Win32.Foundation.PWSTR, pszStr2: win32more.Windows.Win32.Foundation.PWSTR, nChar: Int32) -> Int32: ...
StrCmpNC = UnicodeAlias('StrCmpNCW')
@winfunctype('SHLWAPI.dll')
def StrCmpNICA(pszStr1: win32more.Windows.Win32.Foundation.PSTR, pszStr2: win32more.Windows.Win32.Foundation.PSTR, nChar: Int32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def StrCmpNICW(pszStr1: win32more.Windows.Win32.Foundation.PWSTR, pszStr2: win32more.Windows.Win32.Foundation.PWSTR, nChar: Int32) -> Int32: ...
StrCmpNIC = UnicodeAlias('StrCmpNICW')
@winfunctype('SHLWAPI.dll')
def IntlStrEqWorkerA(fCaseSens: win32more.Windows.Win32.Foundation.BOOL, lpString1: win32more.Windows.Win32.Foundation.PSTR, lpString2: win32more.Windows.Win32.Foundation.PSTR, nChar: Int32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def IntlStrEqWorkerW(fCaseSens: win32more.Windows.Win32.Foundation.BOOL, lpString1: win32more.Windows.Win32.Foundation.PWSTR, lpString2: win32more.Windows.Win32.Foundation.PWSTR, nChar: Int32) -> win32more.Windows.Win32.Foundation.BOOL: ...
IntlStrEqWorker = UnicodeAlias('IntlStrEqWorkerW')
@winfunctype('SHLWAPI.dll')
def PathAddBackslashA(pszPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def PathAddBackslashW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.PWSTR: ...
PathAddBackslash = UnicodeAlias('PathAddBackslashW')
@winfunctype('SHLWAPI.dll')
def PathAddExtensionA(pszPath: win32more.Windows.Win32.Foundation.PSTR, pszExt: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathAddExtensionW(pszPath: win32more.Windows.Win32.Foundation.PWSTR, pszExt: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathAddExtension = UnicodeAlias('PathAddExtensionW')
@winfunctype('SHLWAPI.dll')
def PathAppendA(pszPath: win32more.Windows.Win32.Foundation.PSTR, pszMore: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathAppendW(pszPath: win32more.Windows.Win32.Foundation.PWSTR, pszMore: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathAppend = UnicodeAlias('PathAppendW')
@winfunctype('SHLWAPI.dll')
def PathBuildRootA(pszRoot: win32more.Windows.Win32.Foundation.PSTR, iDrive: Int32) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def PathBuildRootW(pszRoot: win32more.Windows.Win32.Foundation.PWSTR, iDrive: Int32) -> win32more.Windows.Win32.Foundation.PWSTR: ...
PathBuildRoot = UnicodeAlias('PathBuildRootW')
@winfunctype('SHLWAPI.dll')
def PathCanonicalizeA(pszBuf: win32more.Windows.Win32.Foundation.PSTR, pszPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathCanonicalizeW(pszBuf: win32more.Windows.Win32.Foundation.PWSTR, pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathCanonicalize = UnicodeAlias('PathCanonicalizeW')
@winfunctype('SHLWAPI.dll')
def PathCombineA(pszDest: win32more.Windows.Win32.Foundation.PSTR, pszDir: win32more.Windows.Win32.Foundation.PSTR, pszFile: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def PathCombineW(pszDest: win32more.Windows.Win32.Foundation.PWSTR, pszDir: win32more.Windows.Win32.Foundation.PWSTR, pszFile: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.PWSTR: ...
PathCombine = UnicodeAlias('PathCombineW')
@winfunctype('SHLWAPI.dll')
def PathCompactPathA(hDC: win32more.Windows.Win32.Graphics.Gdi.HDC, pszPath: win32more.Windows.Win32.Foundation.PSTR, dx: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathCompactPathW(hDC: win32more.Windows.Win32.Graphics.Gdi.HDC, pszPath: win32more.Windows.Win32.Foundation.PWSTR, dx: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathCompactPath = UnicodeAlias('PathCompactPathW')
@winfunctype('SHLWAPI.dll')
def PathCompactPathExA(pszOut: win32more.Windows.Win32.Foundation.PSTR, pszSrc: win32more.Windows.Win32.Foundation.PSTR, cchMax: UInt32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathCompactPathExW(pszOut: win32more.Windows.Win32.Foundation.PWSTR, pszSrc: win32more.Windows.Win32.Foundation.PWSTR, cchMax: UInt32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathCompactPathEx = UnicodeAlias('PathCompactPathExW')
@winfunctype('SHLWAPI.dll')
def PathCommonPrefixA(pszFile1: win32more.Windows.Win32.Foundation.PSTR, pszFile2: win32more.Windows.Win32.Foundation.PSTR, achPath: win32more.Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def PathCommonPrefixW(pszFile1: win32more.Windows.Win32.Foundation.PWSTR, pszFile2: win32more.Windows.Win32.Foundation.PWSTR, achPath: win32more.Windows.Win32.Foundation.PWSTR) -> Int32: ...
PathCommonPrefix = UnicodeAlias('PathCommonPrefixW')
@winfunctype('SHLWAPI.dll')
def PathFileExistsA(pszPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathFileExistsW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathFileExists = UnicodeAlias('PathFileExistsW')
@winfunctype('SHLWAPI.dll')
def PathFindExtensionA(pszPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def PathFindExtensionW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.PWSTR: ...
PathFindExtension = UnicodeAlias('PathFindExtensionW')
@winfunctype('SHLWAPI.dll')
def PathFindFileNameA(pszPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def PathFindFileNameW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.PWSTR: ...
PathFindFileName = UnicodeAlias('PathFindFileNameW')
@winfunctype('SHLWAPI.dll')
def PathFindNextComponentA(pszPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def PathFindNextComponentW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.PWSTR: ...
PathFindNextComponent = UnicodeAlias('PathFindNextComponentW')
@winfunctype('SHLWAPI.dll')
def PathFindOnPathA(pszPath: win32more.Windows.Win32.Foundation.PSTR, ppszOtherDirs: POINTER(POINTER(SByte))) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathFindOnPathW(pszPath: win32more.Windows.Win32.Foundation.PWSTR, ppszOtherDirs: POINTER(POINTER(UInt16))) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathFindOnPath = UnicodeAlias('PathFindOnPathW')
@winfunctype('SHLWAPI.dll')
def PathFindSuffixArrayA(pszPath: win32more.Windows.Win32.Foundation.PSTR, apszSuffix: POINTER(win32more.Windows.Win32.Foundation.PSTR), iArraySize: Int32) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def PathFindSuffixArrayW(pszPath: win32more.Windows.Win32.Foundation.PWSTR, apszSuffix: POINTER(win32more.Windows.Win32.Foundation.PWSTR), iArraySize: Int32) -> win32more.Windows.Win32.Foundation.PWSTR: ...
PathFindSuffixArray = UnicodeAlias('PathFindSuffixArrayW')
@winfunctype('SHLWAPI.dll')
def PathGetArgsA(pszPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def PathGetArgsW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.PWSTR: ...
PathGetArgs = UnicodeAlias('PathGetArgsW')
@winfunctype('SHLWAPI.dll')
def PathIsLFNFileSpecA(pszName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsLFNFileSpecW(pszName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathIsLFNFileSpec = UnicodeAlias('PathIsLFNFileSpecW')
@winfunctype('SHLWAPI.dll')
def PathGetCharTypeA(ch: Byte) -> UInt32: ...
@winfunctype('SHLWAPI.dll')
def PathGetCharTypeW(ch: Char) -> UInt32: ...
PathGetCharType = UnicodeAlias('PathGetCharTypeW')
@winfunctype('SHLWAPI.dll')
def PathGetDriveNumberA(pszPath: win32more.Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def PathGetDriveNumberW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> Int32: ...
PathGetDriveNumber = UnicodeAlias('PathGetDriveNumberW')
@winfunctype('SHLWAPI.dll')
def PathIsDirectoryA(pszPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsDirectoryW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathIsDirectory = UnicodeAlias('PathIsDirectoryW')
@winfunctype('SHLWAPI.dll')
def PathIsDirectoryEmptyA(pszPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsDirectoryEmptyW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathIsDirectoryEmpty = UnicodeAlias('PathIsDirectoryEmptyW')
@winfunctype('SHLWAPI.dll')
def PathIsFileSpecA(pszPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsFileSpecW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathIsFileSpec = UnicodeAlias('PathIsFileSpecW')
@winfunctype('SHLWAPI.dll')
def PathIsPrefixA(pszPrefix: win32more.Windows.Win32.Foundation.PSTR, pszPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsPrefixW(pszPrefix: win32more.Windows.Win32.Foundation.PWSTR, pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathIsPrefix = UnicodeAlias('PathIsPrefixW')
@winfunctype('SHLWAPI.dll')
def PathIsRelativeA(pszPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsRelativeW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathIsRelative = UnicodeAlias('PathIsRelativeW')
@winfunctype('SHLWAPI.dll')
def PathIsRootA(pszPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsRootW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathIsRoot = UnicodeAlias('PathIsRootW')
@winfunctype('SHLWAPI.dll')
def PathIsSameRootA(pszPath1: win32more.Windows.Win32.Foundation.PSTR, pszPath2: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsSameRootW(pszPath1: win32more.Windows.Win32.Foundation.PWSTR, pszPath2: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathIsSameRoot = UnicodeAlias('PathIsSameRootW')
@winfunctype('SHLWAPI.dll')
def PathIsUNCA(pszPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsUNCW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathIsUNC = UnicodeAlias('PathIsUNCW')
@winfunctype('SHLWAPI.dll')
def PathIsNetworkPathA(pszPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsNetworkPathW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathIsNetworkPath = UnicodeAlias('PathIsNetworkPathW')
@winfunctype('SHLWAPI.dll')
def PathIsUNCServerA(pszPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsUNCServerW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathIsUNCServer = UnicodeAlias('PathIsUNCServerW')
@winfunctype('SHLWAPI.dll')
def PathIsUNCServerShareA(pszPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsUNCServerShareW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathIsUNCServerShare = UnicodeAlias('PathIsUNCServerShareW')
@winfunctype('SHLWAPI.dll')
def PathIsContentTypeA(pszPath: win32more.Windows.Win32.Foundation.PSTR, pszContentType: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsContentTypeW(pszPath: win32more.Windows.Win32.Foundation.PWSTR, pszContentType: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathIsContentType = UnicodeAlias('PathIsContentTypeW')
@winfunctype('SHLWAPI.dll')
def PathIsURLA(pszPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsURLW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathIsURL = UnicodeAlias('PathIsURLW')
@winfunctype('SHLWAPI.dll')
def PathMakePrettyA(pszPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathMakePrettyW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathMakePretty = UnicodeAlias('PathMakePrettyW')
@winfunctype('SHLWAPI.dll')
def PathMatchSpecA(pszFile: win32more.Windows.Win32.Foundation.PSTR, pszSpec: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathMatchSpecW(pszFile: win32more.Windows.Win32.Foundation.PWSTR, pszSpec: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathMatchSpec = UnicodeAlias('PathMatchSpecW')
@winfunctype('SHLWAPI.dll')
def PathMatchSpecExA(pszFile: win32more.Windows.Win32.Foundation.PSTR, pszSpec: win32more.Windows.Win32.Foundation.PSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def PathMatchSpecExW(pszFile: win32more.Windows.Win32.Foundation.PWSTR, pszSpec: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
PathMatchSpecEx = UnicodeAlias('PathMatchSpecExW')
@winfunctype('SHLWAPI.dll')
def PathParseIconLocationA(pszIconFile: win32more.Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def PathParseIconLocationW(pszIconFile: win32more.Windows.Win32.Foundation.PWSTR) -> Int32: ...
PathParseIconLocation = UnicodeAlias('PathParseIconLocationW')
@winfunctype('SHLWAPI.dll')
def PathQuoteSpacesA(lpsz: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathQuoteSpacesW(lpsz: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathQuoteSpaces = UnicodeAlias('PathQuoteSpacesW')
@winfunctype('SHLWAPI.dll')
def PathRelativePathToA(pszPath: win32more.Windows.Win32.Foundation.PSTR, pszFrom: win32more.Windows.Win32.Foundation.PSTR, dwAttrFrom: UInt32, pszTo: win32more.Windows.Win32.Foundation.PSTR, dwAttrTo: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathRelativePathToW(pszPath: win32more.Windows.Win32.Foundation.PWSTR, pszFrom: win32more.Windows.Win32.Foundation.PWSTR, dwAttrFrom: UInt32, pszTo: win32more.Windows.Win32.Foundation.PWSTR, dwAttrTo: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathRelativePathTo = UnicodeAlias('PathRelativePathToW')
@winfunctype('SHLWAPI.dll')
def PathRemoveArgsA(pszPath: win32more.Windows.Win32.Foundation.PSTR) -> Void: ...
@winfunctype('SHLWAPI.dll')
def PathRemoveArgsW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> Void: ...
PathRemoveArgs = UnicodeAlias('PathRemoveArgsW')
@winfunctype('SHLWAPI.dll')
def PathRemoveBackslashA(pszPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def PathRemoveBackslashW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.PWSTR: ...
PathRemoveBackslash = UnicodeAlias('PathRemoveBackslashW')
@winfunctype('SHLWAPI.dll')
def PathRemoveBlanksA(pszPath: win32more.Windows.Win32.Foundation.PSTR) -> Void: ...
@winfunctype('SHLWAPI.dll')
def PathRemoveBlanksW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> Void: ...
PathRemoveBlanks = UnicodeAlias('PathRemoveBlanksW')
@winfunctype('SHLWAPI.dll')
def PathRemoveExtensionA(pszPath: win32more.Windows.Win32.Foundation.PSTR) -> Void: ...
@winfunctype('SHLWAPI.dll')
def PathRemoveExtensionW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> Void: ...
PathRemoveExtension = UnicodeAlias('PathRemoveExtensionW')
@winfunctype('SHLWAPI.dll')
def PathRemoveFileSpecA(pszPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathRemoveFileSpecW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathRemoveFileSpec = UnicodeAlias('PathRemoveFileSpecW')
@winfunctype('SHLWAPI.dll')
def PathRenameExtensionA(pszPath: win32more.Windows.Win32.Foundation.PSTR, pszExt: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathRenameExtensionW(pszPath: win32more.Windows.Win32.Foundation.PWSTR, pszExt: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathRenameExtension = UnicodeAlias('PathRenameExtensionW')
@winfunctype('SHLWAPI.dll')
def PathSearchAndQualifyA(pszPath: win32more.Windows.Win32.Foundation.PSTR, pszBuf: win32more.Windows.Win32.Foundation.PSTR, cchBuf: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathSearchAndQualifyW(pszPath: win32more.Windows.Win32.Foundation.PWSTR, pszBuf: win32more.Windows.Win32.Foundation.PWSTR, cchBuf: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathSearchAndQualify = UnicodeAlias('PathSearchAndQualifyW')
@winfunctype('SHLWAPI.dll')
def PathSetDlgItemPathA(hDlg: win32more.Windows.Win32.Foundation.HWND, id: Int32, pszPath: win32more.Windows.Win32.Foundation.PSTR) -> Void: ...
@winfunctype('SHLWAPI.dll')
def PathSetDlgItemPathW(hDlg: win32more.Windows.Win32.Foundation.HWND, id: Int32, pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> Void: ...
PathSetDlgItemPath = UnicodeAlias('PathSetDlgItemPathW')
@winfunctype('SHLWAPI.dll')
def PathSkipRootA(pszPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def PathSkipRootW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.PWSTR: ...
PathSkipRoot = UnicodeAlias('PathSkipRootW')
@winfunctype('SHLWAPI.dll')
def PathStripPathA(pszPath: win32more.Windows.Win32.Foundation.PSTR) -> Void: ...
@winfunctype('SHLWAPI.dll')
def PathStripPathW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> Void: ...
PathStripPath = UnicodeAlias('PathStripPathW')
@winfunctype('SHLWAPI.dll')
def PathStripToRootA(pszPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathStripToRootW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathStripToRoot = UnicodeAlias('PathStripToRootW')
@winfunctype('SHLWAPI.dll')
def PathUnquoteSpacesA(lpsz: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathUnquoteSpacesW(lpsz: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathUnquoteSpaces = UnicodeAlias('PathUnquoteSpacesW')
@winfunctype('SHLWAPI.dll')
def PathMakeSystemFolderA(pszPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathMakeSystemFolderW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathMakeSystemFolder = UnicodeAlias('PathMakeSystemFolderW')
@winfunctype('SHLWAPI.dll')
def PathUnmakeSystemFolderA(pszPath: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathUnmakeSystemFolderW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathUnmakeSystemFolder = UnicodeAlias('PathUnmakeSystemFolderW')
@winfunctype('SHLWAPI.dll')
def PathIsSystemFolderA(pszPath: win32more.Windows.Win32.Foundation.PSTR, dwAttrb: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathIsSystemFolderW(pszPath: win32more.Windows.Win32.Foundation.PWSTR, dwAttrb: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathIsSystemFolder = UnicodeAlias('PathIsSystemFolderW')
@winfunctype('SHLWAPI.dll')
def PathUndecorateA(pszPath: win32more.Windows.Win32.Foundation.PSTR) -> Void: ...
@winfunctype('SHLWAPI.dll')
def PathUndecorateW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> Void: ...
PathUndecorate = UnicodeAlias('PathUndecorateW')
@winfunctype('SHLWAPI.dll')
def PathUnExpandEnvStringsA(pszPath: win32more.Windows.Win32.Foundation.PSTR, pszBuf: win32more.Windows.Win32.Foundation.PSTR, cchBuf: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def PathUnExpandEnvStringsW(pszPath: win32more.Windows.Win32.Foundation.PWSTR, pszBuf: win32more.Windows.Win32.Foundation.PWSTR, cchBuf: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
PathUnExpandEnvStrings = UnicodeAlias('PathUnExpandEnvStringsW')
@winfunctype('SHLWAPI.dll')
def UrlCompareA(psz1: win32more.Windows.Win32.Foundation.PSTR, psz2: win32more.Windows.Win32.Foundation.PSTR, fIgnoreSlash: win32more.Windows.Win32.Foundation.BOOL) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def UrlCompareW(psz1: win32more.Windows.Win32.Foundation.PWSTR, psz2: win32more.Windows.Win32.Foundation.PWSTR, fIgnoreSlash: win32more.Windows.Win32.Foundation.BOOL) -> Int32: ...
UrlCompare = UnicodeAlias('UrlCompareW')
@winfunctype('SHLWAPI.dll')
def UrlCombineA(pszBase: win32more.Windows.Win32.Foundation.PSTR, pszRelative: win32more.Windows.Win32.Foundation.PSTR, pszCombined: win32more.Windows.Win32.Foundation.PSTR, pcchCombined: POINTER(UInt32), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def UrlCombineW(pszBase: win32more.Windows.Win32.Foundation.PWSTR, pszRelative: win32more.Windows.Win32.Foundation.PWSTR, pszCombined: win32more.Windows.Win32.Foundation.PWSTR, pcchCombined: POINTER(UInt32), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
UrlCombine = UnicodeAlias('UrlCombineW')
@winfunctype('SHLWAPI.dll')
def UrlCanonicalizeA(pszUrl: win32more.Windows.Win32.Foundation.PSTR, pszCanonicalized: win32more.Windows.Win32.Foundation.PSTR, pcchCanonicalized: POINTER(UInt32), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def UrlCanonicalizeW(pszUrl: win32more.Windows.Win32.Foundation.PWSTR, pszCanonicalized: win32more.Windows.Win32.Foundation.PWSTR, pcchCanonicalized: POINTER(UInt32), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
UrlCanonicalize = UnicodeAlias('UrlCanonicalizeW')
@winfunctype('SHLWAPI.dll')
def UrlIsOpaqueA(pszURL: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def UrlIsOpaqueW(pszURL: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
UrlIsOpaque = UnicodeAlias('UrlIsOpaqueW')
@winfunctype('SHLWAPI.dll')
def UrlIsNoHistoryA(pszURL: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def UrlIsNoHistoryW(pszURL: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
UrlIsNoHistory = UnicodeAlias('UrlIsNoHistoryW')
@winfunctype('SHLWAPI.dll')
def UrlIsA(pszUrl: win32more.Windows.Win32.Foundation.PSTR, UrlIs: win32more.Windows.Win32.UI.Shell.URLIS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def UrlIsW(pszUrl: win32more.Windows.Win32.Foundation.PWSTR, UrlIs: win32more.Windows.Win32.UI.Shell.URLIS) -> win32more.Windows.Win32.Foundation.BOOL: ...
UrlIs = UnicodeAlias('UrlIsW')
@winfunctype('SHLWAPI.dll')
def UrlGetLocationA(pszURL: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.PSTR: ...
@winfunctype('SHLWAPI.dll')
def UrlGetLocationW(pszURL: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.PWSTR: ...
UrlGetLocation = UnicodeAlias('UrlGetLocationW')
@winfunctype('SHLWAPI.dll')
def UrlUnescapeA(pszUrl: win32more.Windows.Win32.Foundation.PSTR, pszUnescaped: win32more.Windows.Win32.Foundation.PSTR, pcchUnescaped: POINTER(UInt32), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def UrlUnescapeW(pszUrl: win32more.Windows.Win32.Foundation.PWSTR, pszUnescaped: win32more.Windows.Win32.Foundation.PWSTR, pcchUnescaped: POINTER(UInt32), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
UrlUnescape = UnicodeAlias('UrlUnescapeW')
@winfunctype('SHLWAPI.dll')
def UrlEscapeA(pszUrl: win32more.Windows.Win32.Foundation.PSTR, pszEscaped: win32more.Windows.Win32.Foundation.PSTR, pcchEscaped: POINTER(UInt32), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def UrlEscapeW(pszUrl: win32more.Windows.Win32.Foundation.PWSTR, pszEscaped: win32more.Windows.Win32.Foundation.PWSTR, pcchEscaped: POINTER(UInt32), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
UrlEscape = UnicodeAlias('UrlEscapeW')
@winfunctype('SHLWAPI.dll')
def UrlCreateFromPathA(pszPath: win32more.Windows.Win32.Foundation.PSTR, pszUrl: win32more.Windows.Win32.Foundation.PSTR, pcchUrl: POINTER(UInt32), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def UrlCreateFromPathW(pszPath: win32more.Windows.Win32.Foundation.PWSTR, pszUrl: win32more.Windows.Win32.Foundation.PWSTR, pcchUrl: POINTER(UInt32), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
UrlCreateFromPath = UnicodeAlias('UrlCreateFromPathW')
@winfunctype('SHLWAPI.dll')
def PathCreateFromUrlA(pszUrl: win32more.Windows.Win32.Foundation.PSTR, pszPath: win32more.Windows.Win32.Foundation.PSTR, pcchPath: POINTER(UInt32), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def PathCreateFromUrlW(pszUrl: win32more.Windows.Win32.Foundation.PWSTR, pszPath: win32more.Windows.Win32.Foundation.PWSTR, pcchPath: POINTER(UInt32), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
PathCreateFromUrl = UnicodeAlias('PathCreateFromUrlW')
@winfunctype('SHLWAPI.dll')
def PathCreateFromUrlAlloc(pszIn: win32more.Windows.Win32.Foundation.PWSTR, ppszOut: POINTER(win32more.Windows.Win32.Foundation.PWSTR), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def UrlHashA(pszUrl: win32more.Windows.Win32.Foundation.PSTR, pbHash: POINTER(Byte), cbHash: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def UrlHashW(pszUrl: win32more.Windows.Win32.Foundation.PWSTR, pbHash: POINTER(Byte), cbHash: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
UrlHash = UnicodeAlias('UrlHashW')
@winfunctype('SHLWAPI.dll')
def UrlGetPartW(pszIn: win32more.Windows.Win32.Foundation.PWSTR, pszOut: win32more.Windows.Win32.Foundation.PWSTR, pcchOut: POINTER(UInt32), dwPart: UInt32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
UrlGetPart = UnicodeAlias('UrlGetPartW')
@winfunctype('SHLWAPI.dll')
def UrlGetPartA(pszIn: win32more.Windows.Win32.Foundation.PSTR, pszOut: win32more.Windows.Win32.Foundation.PSTR, pcchOut: POINTER(UInt32), dwPart: UInt32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def UrlApplySchemeA(pszIn: win32more.Windows.Win32.Foundation.PSTR, pszOut: win32more.Windows.Win32.Foundation.PSTR, pcchOut: POINTER(UInt32), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def UrlApplySchemeW(pszIn: win32more.Windows.Win32.Foundation.PWSTR, pszOut: win32more.Windows.Win32.Foundation.PWSTR, pcchOut: POINTER(UInt32), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
UrlApplyScheme = UnicodeAlias('UrlApplySchemeW')
@winfunctype('SHLWAPI.dll')
def HashData(pbData: POINTER(Byte), cbData: UInt32, pbHash: POINTER(Byte), cbHash: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def UrlFixupW(pcszUrl: win32more.Windows.Win32.Foundation.PWSTR, pszTranslatedUrl: win32more.Windows.Win32.Foundation.PWSTR, cchMax: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def ParseURLA(pcszURL: win32more.Windows.Win32.Foundation.PSTR, ppu: POINTER(win32more.Windows.Win32.UI.Shell.PARSEDURLA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def ParseURLW(pcszURL: win32more.Windows.Win32.Foundation.PWSTR, ppu: POINTER(win32more.Windows.Win32.UI.Shell.PARSEDURLW)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
ParseURL = UnicodeAlias('ParseURLW')
@winfunctype('SHLWAPI.dll')
def SHDeleteEmptyKeyA(hkey: win32more.Windows.Win32.System.Registry.HKEY, pszSubKey: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHDeleteEmptyKeyW(hkey: win32more.Windows.Win32.System.Registry.HKEY, pszSubKey: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
SHDeleteEmptyKey = UnicodeAlias('SHDeleteEmptyKeyW')
@winfunctype('SHLWAPI.dll')
def SHDeleteKeyA(hkey: win32more.Windows.Win32.System.Registry.HKEY, pszSubKey: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHDeleteKeyW(hkey: win32more.Windows.Win32.System.Registry.HKEY, pszSubKey: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
SHDeleteKey = UnicodeAlias('SHDeleteKeyW')
@winfunctype('SHLWAPI.dll')
def SHRegDuplicateHKey(hkey: win32more.Windows.Win32.System.Registry.HKEY) -> win32more.Windows.Win32.System.Registry.HKEY: ...
@winfunctype('SHLWAPI.dll')
def SHDeleteValueA(hkey: win32more.Windows.Win32.System.Registry.HKEY, pszSubKey: win32more.Windows.Win32.Foundation.PSTR, pszValue: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHDeleteValueW(hkey: win32more.Windows.Win32.System.Registry.HKEY, pszSubKey: win32more.Windows.Win32.Foundation.PWSTR, pszValue: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
SHDeleteValue = UnicodeAlias('SHDeleteValueW')
@winfunctype('SHLWAPI.dll')
def SHGetValueA(hkey: win32more.Windows.Win32.System.Registry.HKEY, pszSubKey: win32more.Windows.Win32.Foundation.PSTR, pszValue: win32more.Windows.Win32.Foundation.PSTR, pdwType: POINTER(UInt32), pvData: VoidPtr, pcbData: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHGetValueW(hkey: win32more.Windows.Win32.System.Registry.HKEY, pszSubKey: win32more.Windows.Win32.Foundation.PWSTR, pszValue: win32more.Windows.Win32.Foundation.PWSTR, pdwType: POINTER(UInt32), pvData: VoidPtr, pcbData: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
SHGetValue = UnicodeAlias('SHGetValueW')
@winfunctype('SHLWAPI.dll')
def SHSetValueA(hkey: win32more.Windows.Win32.System.Registry.HKEY, pszSubKey: win32more.Windows.Win32.Foundation.PSTR, pszValue: win32more.Windows.Win32.Foundation.PSTR, dwType: UInt32, pvData: VoidPtr, cbData: UInt32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def SHSetValueW(hkey: win32more.Windows.Win32.System.Registry.HKEY, pszSubKey: win32more.Windows.Win32.Foundation.PWSTR, pszValue: win32more.Windows.Win32.Foundation.PWSTR, dwType: UInt32, pvData: VoidPtr, cbData: UInt32) -> Int32: ...
SHSetValue = UnicodeAlias('SHSetValueW')
@winfunctype('SHLWAPI.dll')
def SHRegGetValueA(hkey: win32more.Windows.Win32.System.Registry.HKEY, pszSubKey: win32more.Windows.Win32.Foundation.PSTR, pszValue: win32more.Windows.Win32.Foundation.PSTR, srrfFlags: Int32, pdwType: POINTER(UInt32), pvData: VoidPtr, pcbData: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegGetValueW(hkey: win32more.Windows.Win32.System.Registry.HKEY, pszSubKey: win32more.Windows.Win32.Foundation.PWSTR, pszValue: win32more.Windows.Win32.Foundation.PWSTR, srrfFlags: Int32, pdwType: POINTER(UInt32), pvData: VoidPtr, pcbData: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
SHRegGetValue = UnicodeAlias('SHRegGetValueW')
@winfunctype('SHLWAPI.dll')
def SHRegGetValueFromHKCUHKLM(pwszKey: win32more.Windows.Win32.Foundation.PWSTR, pwszValue: win32more.Windows.Win32.Foundation.PWSTR, srrfFlags: Int32, pdwType: POINTER(UInt32), pvData: VoidPtr, pcbData: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHQueryValueExA(hkey: win32more.Windows.Win32.System.Registry.HKEY, pszValue: win32more.Windows.Win32.Foundation.PSTR, pdwReserved: POINTER(UInt32), pdwType: POINTER(UInt32), pvData: VoidPtr, pcbData: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHQueryValueExW(hkey: win32more.Windows.Win32.System.Registry.HKEY, pszValue: win32more.Windows.Win32.Foundation.PWSTR, pdwReserved: POINTER(UInt32), pdwType: POINTER(UInt32), pvData: VoidPtr, pcbData: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
SHQueryValueEx = UnicodeAlias('SHQueryValueExW')
@winfunctype('SHLWAPI.dll')
def SHEnumKeyExA(hkey: win32more.Windows.Win32.System.Registry.HKEY, dwIndex: UInt32, pszName: win32more.Windows.Win32.Foundation.PSTR, pcchName: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHEnumKeyExW(hkey: win32more.Windows.Win32.System.Registry.HKEY, dwIndex: UInt32, pszName: win32more.Windows.Win32.Foundation.PWSTR, pcchName: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
SHEnumKeyEx = UnicodeAlias('SHEnumKeyExW')
@winfunctype('SHLWAPI.dll')
def SHEnumValueA(hkey: win32more.Windows.Win32.System.Registry.HKEY, dwIndex: UInt32, pszValueName: win32more.Windows.Win32.Foundation.PSTR, pcchValueName: POINTER(UInt32), pdwType: POINTER(UInt32), pvData: VoidPtr, pcbData: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHEnumValueW(hkey: win32more.Windows.Win32.System.Registry.HKEY, dwIndex: UInt32, pszValueName: win32more.Windows.Win32.Foundation.PWSTR, pcchValueName: POINTER(UInt32), pdwType: POINTER(UInt32), pvData: VoidPtr, pcbData: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
SHEnumValue = UnicodeAlias('SHEnumValueW')
@winfunctype('SHLWAPI.dll')
def SHQueryInfoKeyA(hkey: win32more.Windows.Win32.System.Registry.HKEY, pcSubKeys: POINTER(UInt32), pcchMaxSubKeyLen: POINTER(UInt32), pcValues: POINTER(UInt32), pcchMaxValueNameLen: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHQueryInfoKeyW(hkey: win32more.Windows.Win32.System.Registry.HKEY, pcSubKeys: POINTER(UInt32), pcchMaxSubKeyLen: POINTER(UInt32), pcValues: POINTER(UInt32), pcchMaxValueNameLen: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
SHQueryInfoKey = UnicodeAlias('SHQueryInfoKeyW')
@winfunctype('SHLWAPI.dll')
def SHCopyKeyA(hkeySrc: win32more.Windows.Win32.System.Registry.HKEY, pszSrcSubKey: win32more.Windows.Win32.Foundation.PSTR, hkeyDest: win32more.Windows.Win32.System.Registry.HKEY, fReserved: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHCopyKeyW(hkeySrc: win32more.Windows.Win32.System.Registry.HKEY, pszSrcSubKey: win32more.Windows.Win32.Foundation.PWSTR, hkeyDest: win32more.Windows.Win32.System.Registry.HKEY, fReserved: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
SHCopyKey = UnicodeAlias('SHCopyKeyW')
@winfunctype('SHLWAPI.dll')
def SHRegGetPathA(hKey: win32more.Windows.Win32.System.Registry.HKEY, pcszSubKey: win32more.Windows.Win32.Foundation.PSTR, pcszValue: win32more.Windows.Win32.Foundation.PSTR, pszPath: win32more.Windows.Win32.Foundation.PSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegGetPathW(hKey: win32more.Windows.Win32.System.Registry.HKEY, pcszSubKey: win32more.Windows.Win32.Foundation.PWSTR, pcszValue: win32more.Windows.Win32.Foundation.PWSTR, pszPath: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
SHRegGetPath = UnicodeAlias('SHRegGetPathW')
@winfunctype('SHLWAPI.dll')
def SHRegSetPathA(hKey: win32more.Windows.Win32.System.Registry.HKEY, pcszSubKey: win32more.Windows.Win32.Foundation.PSTR, pcszValue: win32more.Windows.Win32.Foundation.PSTR, pcszPath: win32more.Windows.Win32.Foundation.PSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegSetPathW(hKey: win32more.Windows.Win32.System.Registry.HKEY, pcszSubKey: win32more.Windows.Win32.Foundation.PWSTR, pcszValue: win32more.Windows.Win32.Foundation.PWSTR, pcszPath: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
SHRegSetPath = UnicodeAlias('SHRegSetPathW')
@winfunctype('SHLWAPI.dll')
def SHRegCreateUSKeyA(pszPath: win32more.Windows.Win32.Foundation.PSTR, samDesired: UInt32, hRelativeUSKey: IntPtr, phNewUSKey: POINTER(IntPtr), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegCreateUSKeyW(pwzPath: win32more.Windows.Win32.Foundation.PWSTR, samDesired: UInt32, hRelativeUSKey: IntPtr, phNewUSKey: POINTER(IntPtr), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
SHRegCreateUSKey = UnicodeAlias('SHRegCreateUSKeyW')
@winfunctype('SHLWAPI.dll')
def SHRegOpenUSKeyA(pszPath: win32more.Windows.Win32.Foundation.PSTR, samDesired: UInt32, hRelativeUSKey: IntPtr, phNewUSKey: POINTER(IntPtr), fIgnoreHKCU: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegOpenUSKeyW(pwzPath: win32more.Windows.Win32.Foundation.PWSTR, samDesired: UInt32, hRelativeUSKey: IntPtr, phNewUSKey: POINTER(IntPtr), fIgnoreHKCU: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
SHRegOpenUSKey = UnicodeAlias('SHRegOpenUSKeyW')
@winfunctype('SHLWAPI.dll')
def SHRegQueryUSValueA(hUSKey: IntPtr, pszValue: win32more.Windows.Win32.Foundation.PSTR, pdwType: POINTER(UInt32), pvData: VoidPtr, pcbData: POINTER(UInt32), fIgnoreHKCU: win32more.Windows.Win32.Foundation.BOOL, pvDefaultData: VoidPtr, dwDefaultDataSize: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegQueryUSValueW(hUSKey: IntPtr, pszValue: win32more.Windows.Win32.Foundation.PWSTR, pdwType: POINTER(UInt32), pvData: VoidPtr, pcbData: POINTER(UInt32), fIgnoreHKCU: win32more.Windows.Win32.Foundation.BOOL, pvDefaultData: VoidPtr, dwDefaultDataSize: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
SHRegQueryUSValue = UnicodeAlias('SHRegQueryUSValueW')
@winfunctype('SHLWAPI.dll')
def SHRegWriteUSValueA(hUSKey: IntPtr, pszValue: win32more.Windows.Win32.Foundation.PSTR, dwType: UInt32, pvData: VoidPtr, cbData: UInt32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegWriteUSValueW(hUSKey: IntPtr, pwzValue: win32more.Windows.Win32.Foundation.PWSTR, dwType: UInt32, pvData: VoidPtr, cbData: UInt32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
SHRegWriteUSValue = UnicodeAlias('SHRegWriteUSValueW')
@winfunctype('SHLWAPI.dll')
def SHRegDeleteUSValueA(hUSKey: IntPtr, pszValue: win32more.Windows.Win32.Foundation.PSTR, delRegFlags: win32more.Windows.Win32.UI.Shell.SHREGDEL_FLAGS) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegDeleteUSValueW(hUSKey: IntPtr, pwzValue: win32more.Windows.Win32.Foundation.PWSTR, delRegFlags: win32more.Windows.Win32.UI.Shell.SHREGDEL_FLAGS) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
SHRegDeleteUSValue = UnicodeAlias('SHRegDeleteUSValueW')
@winfunctype('SHLWAPI.dll')
def SHRegDeleteEmptyUSKeyW(hUSKey: IntPtr, pwzSubKey: win32more.Windows.Win32.Foundation.PWSTR, delRegFlags: win32more.Windows.Win32.UI.Shell.SHREGDEL_FLAGS) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
SHRegDeleteEmptyUSKey = UnicodeAlias('SHRegDeleteEmptyUSKeyW')
@winfunctype('SHLWAPI.dll')
def SHRegDeleteEmptyUSKeyA(hUSKey: IntPtr, pszSubKey: win32more.Windows.Win32.Foundation.PSTR, delRegFlags: win32more.Windows.Win32.UI.Shell.SHREGDEL_FLAGS) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegEnumUSKeyA(hUSKey: IntPtr, dwIndex: UInt32, pszName: win32more.Windows.Win32.Foundation.PSTR, pcchName: POINTER(UInt32), enumRegFlags: win32more.Windows.Win32.UI.Shell.SHREGENUM_FLAGS) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegEnumUSKeyW(hUSKey: IntPtr, dwIndex: UInt32, pwzName: win32more.Windows.Win32.Foundation.PWSTR, pcchName: POINTER(UInt32), enumRegFlags: win32more.Windows.Win32.UI.Shell.SHREGENUM_FLAGS) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
SHRegEnumUSKey = UnicodeAlias('SHRegEnumUSKeyW')
@winfunctype('SHLWAPI.dll')
def SHRegEnumUSValueA(hUSkey: IntPtr, dwIndex: UInt32, pszValueName: win32more.Windows.Win32.Foundation.PSTR, pcchValueName: POINTER(UInt32), pdwType: POINTER(UInt32), pvData: VoidPtr, pcbData: POINTER(UInt32), enumRegFlags: win32more.Windows.Win32.UI.Shell.SHREGENUM_FLAGS) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegEnumUSValueW(hUSkey: IntPtr, dwIndex: UInt32, pszValueName: win32more.Windows.Win32.Foundation.PWSTR, pcchValueName: POINTER(UInt32), pdwType: POINTER(UInt32), pvData: VoidPtr, pcbData: POINTER(UInt32), enumRegFlags: win32more.Windows.Win32.UI.Shell.SHREGENUM_FLAGS) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
SHRegEnumUSValue = UnicodeAlias('SHRegEnumUSValueW')
@winfunctype('SHLWAPI.dll')
def SHRegQueryInfoUSKeyA(hUSKey: IntPtr, pcSubKeys: POINTER(UInt32), pcchMaxSubKeyLen: POINTER(UInt32), pcValues: POINTER(UInt32), pcchMaxValueNameLen: POINTER(UInt32), enumRegFlags: win32more.Windows.Win32.UI.Shell.SHREGENUM_FLAGS) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegQueryInfoUSKeyW(hUSKey: IntPtr, pcSubKeys: POINTER(UInt32), pcchMaxSubKeyLen: POINTER(UInt32), pcValues: POINTER(UInt32), pcchMaxValueNameLen: POINTER(UInt32), enumRegFlags: win32more.Windows.Win32.UI.Shell.SHREGENUM_FLAGS) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
SHRegQueryInfoUSKey = UnicodeAlias('SHRegQueryInfoUSKeyW')
@winfunctype('SHLWAPI.dll')
def SHRegCloseUSKey(hUSKey: IntPtr) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegGetUSValueA(pszSubKey: win32more.Windows.Win32.Foundation.PSTR, pszValue: win32more.Windows.Win32.Foundation.PSTR, pdwType: POINTER(UInt32), pvData: VoidPtr, pcbData: POINTER(UInt32), fIgnoreHKCU: win32more.Windows.Win32.Foundation.BOOL, pvDefaultData: VoidPtr, dwDefaultDataSize: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegGetUSValueW(pszSubKey: win32more.Windows.Win32.Foundation.PWSTR, pszValue: win32more.Windows.Win32.Foundation.PWSTR, pdwType: POINTER(UInt32), pvData: VoidPtr, pcbData: POINTER(UInt32), fIgnoreHKCU: win32more.Windows.Win32.Foundation.BOOL, pvDefaultData: VoidPtr, dwDefaultDataSize: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
SHRegGetUSValue = UnicodeAlias('SHRegGetUSValueW')
@winfunctype('SHLWAPI.dll')
def SHRegSetUSValueA(pszSubKey: win32more.Windows.Win32.Foundation.PSTR, pszValue: win32more.Windows.Win32.Foundation.PSTR, dwType: UInt32, pvData: VoidPtr, cbData: UInt32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
@winfunctype('SHLWAPI.dll')
def SHRegSetUSValueW(pwzSubKey: win32more.Windows.Win32.Foundation.PWSTR, pwzValue: win32more.Windows.Win32.Foundation.PWSTR, dwType: UInt32, pvData: VoidPtr, cbData: UInt32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.WIN32_ERROR: ...
SHRegSetUSValue = UnicodeAlias('SHRegSetUSValueW')
@winfunctype('SHLWAPI.dll')
def SHRegGetIntW(hk: win32more.Windows.Win32.System.Registry.HKEY, pwzKey: win32more.Windows.Win32.Foundation.PWSTR, iDefault: Int32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def SHRegGetBoolUSValueA(pszSubKey: win32more.Windows.Win32.Foundation.PSTR, pszValue: win32more.Windows.Win32.Foundation.PSTR, fIgnoreHKCU: win32more.Windows.Win32.Foundation.BOOL, fDefault: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def SHRegGetBoolUSValueW(pszSubKey: win32more.Windows.Win32.Foundation.PWSTR, pszValue: win32more.Windows.Win32.Foundation.PWSTR, fIgnoreHKCU: win32more.Windows.Win32.Foundation.BOOL, fDefault: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
SHRegGetBoolUSValue = UnicodeAlias('SHRegGetBoolUSValueW')
@winfunctype('SHLWAPI.dll')
def AssocCreate(clsid: Guid, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def AssocQueryStringA(flags: win32more.Windows.Win32.UI.Shell.ASSOCF, str: win32more.Windows.Win32.UI.Shell.ASSOCSTR, pszAssoc: win32more.Windows.Win32.Foundation.PSTR, pszExtra: win32more.Windows.Win32.Foundation.PSTR, pszOut: win32more.Windows.Win32.Foundation.PSTR, pcchOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def AssocQueryStringW(flags: win32more.Windows.Win32.UI.Shell.ASSOCF, str: win32more.Windows.Win32.UI.Shell.ASSOCSTR, pszAssoc: win32more.Windows.Win32.Foundation.PWSTR, pszExtra: win32more.Windows.Win32.Foundation.PWSTR, pszOut: win32more.Windows.Win32.Foundation.PWSTR, pcchOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
AssocQueryString = UnicodeAlias('AssocQueryStringW')
@winfunctype('SHLWAPI.dll')
def AssocQueryStringByKeyA(flags: win32more.Windows.Win32.UI.Shell.ASSOCF, str: win32more.Windows.Win32.UI.Shell.ASSOCSTR, hkAssoc: win32more.Windows.Win32.System.Registry.HKEY, pszExtra: win32more.Windows.Win32.Foundation.PSTR, pszOut: win32more.Windows.Win32.Foundation.PSTR, pcchOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def AssocQueryStringByKeyW(flags: win32more.Windows.Win32.UI.Shell.ASSOCF, str: win32more.Windows.Win32.UI.Shell.ASSOCSTR, hkAssoc: win32more.Windows.Win32.System.Registry.HKEY, pszExtra: win32more.Windows.Win32.Foundation.PWSTR, pszOut: win32more.Windows.Win32.Foundation.PWSTR, pcchOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
AssocQueryStringByKey = UnicodeAlias('AssocQueryStringByKeyW')
@winfunctype('SHLWAPI.dll')
def AssocQueryKeyA(flags: win32more.Windows.Win32.UI.Shell.ASSOCF, key: win32more.Windows.Win32.UI.Shell.ASSOCKEY, pszAssoc: win32more.Windows.Win32.Foundation.PSTR, pszExtra: win32more.Windows.Win32.Foundation.PSTR, phkeyOut: POINTER(win32more.Windows.Win32.System.Registry.HKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def AssocQueryKeyW(flags: win32more.Windows.Win32.UI.Shell.ASSOCF, key: win32more.Windows.Win32.UI.Shell.ASSOCKEY, pszAssoc: win32more.Windows.Win32.Foundation.PWSTR, pszExtra: win32more.Windows.Win32.Foundation.PWSTR, phkeyOut: POINTER(win32more.Windows.Win32.System.Registry.HKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
AssocQueryKey = UnicodeAlias('AssocQueryKeyW')
@winfunctype('SHLWAPI.dll')
def AssocIsDangerous(pszAssoc: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def AssocGetPerceivedType(pszExt: win32more.Windows.Win32.Foundation.PWSTR, ptype: POINTER(win32more.Windows.Win32.UI.Shell.Common.PERCEIVED), pflag: POINTER(UInt32), ppszType: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHOpenRegStreamA(hkey: win32more.Windows.Win32.System.Registry.HKEY, pszSubkey: win32more.Windows.Win32.Foundation.PSTR, pszValue: win32more.Windows.Win32.Foundation.PSTR, grfMode: UInt32) -> win32more.Windows.Win32.System.Com.IStream: ...
@winfunctype('SHLWAPI.dll')
def SHOpenRegStreamW(hkey: win32more.Windows.Win32.System.Registry.HKEY, pszSubkey: win32more.Windows.Win32.Foundation.PWSTR, pszValue: win32more.Windows.Win32.Foundation.PWSTR, grfMode: UInt32) -> win32more.Windows.Win32.System.Com.IStream: ...
SHOpenRegStream = UnicodeAlias('SHOpenRegStreamW')
@winfunctype('SHLWAPI.dll')
def SHOpenRegStream2A(hkey: win32more.Windows.Win32.System.Registry.HKEY, pszSubkey: win32more.Windows.Win32.Foundation.PSTR, pszValue: win32more.Windows.Win32.Foundation.PSTR, grfMode: UInt32) -> win32more.Windows.Win32.System.Com.IStream: ...
@winfunctype('SHLWAPI.dll')
def SHOpenRegStream2W(hkey: win32more.Windows.Win32.System.Registry.HKEY, pszSubkey: win32more.Windows.Win32.Foundation.PWSTR, pszValue: win32more.Windows.Win32.Foundation.PWSTR, grfMode: UInt32) -> win32more.Windows.Win32.System.Com.IStream: ...
SHOpenRegStream2 = UnicodeAlias('SHOpenRegStream2W')
@winfunctype('SHLWAPI.dll')
def SHCreateStreamOnFileA(pszFile: win32more.Windows.Win32.Foundation.PSTR, grfMode: UInt32, ppstm: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHCreateStreamOnFileW(pszFile: win32more.Windows.Win32.Foundation.PWSTR, grfMode: UInt32, ppstm: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
SHCreateStreamOnFile = UnicodeAlias('SHCreateStreamOnFileW')
@winfunctype('SHLWAPI.dll')
def SHCreateStreamOnFileEx(pszFile: win32more.Windows.Win32.Foundation.PWSTR, grfMode: UInt32, dwAttributes: UInt32, fCreate: win32more.Windows.Win32.Foundation.BOOL, pstmTemplate: win32more.Windows.Win32.System.Com.IStream, ppstm: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHCreateMemStream(pInit: POINTER(Byte), cbInit: UInt32) -> win32more.Windows.Win32.System.Com.IStream: ...
@winfunctype('SHLWAPI.dll')
def GetAcceptLanguagesA(pszLanguages: win32more.Windows.Win32.Foundation.PSTR, pcchLanguages: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def GetAcceptLanguagesW(pszLanguages: win32more.Windows.Win32.Foundation.PWSTR, pcchLanguages: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
GetAcceptLanguages = UnicodeAlias('GetAcceptLanguagesW')
@winfunctype('SHLWAPI.dll')
def IUnknown_Set(ppunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown), punk: win32more.Windows.Win32.System.Com.IUnknown) -> Void: ...
@winfunctype('SHLWAPI.dll')
def IUnknown_AtomicRelease(ppunk: POINTER(VoidPtr)) -> Void: ...
@winfunctype('SHLWAPI.dll')
def IUnknown_GetWindow(punk: win32more.Windows.Win32.System.Com.IUnknown, phwnd: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def IUnknown_SetSite(punk: win32more.Windows.Win32.System.Com.IUnknown, punkSite: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def IUnknown_GetSite(punk: win32more.Windows.Win32.System.Com.IUnknown, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def IUnknown_QueryService(punk: win32more.Windows.Win32.System.Com.IUnknown, guidService: POINTER(Guid), riid: POINTER(Guid), ppvOut: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def IStream_Read(pstm: win32more.Windows.Win32.System.Com.IStream, pv: VoidPtr, cb: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def IStream_Write(pstm: win32more.Windows.Win32.System.Com.IStream, pv: VoidPtr, cb: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def IStream_Reset(pstm: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def IStream_Size(pstm: win32more.Windows.Win32.System.Com.IStream, pui: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def ConnectToConnectionPoint(punk: win32more.Windows.Win32.System.Com.IUnknown, riidEvent: POINTER(Guid), fConnect: win32more.Windows.Win32.Foundation.BOOL, punkTarget: win32more.Windows.Win32.System.Com.IUnknown, pdwCookie: POINTER(UInt32), ppcpOut: POINTER(win32more.Windows.Win32.System.Com.IConnectionPoint)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def IStream_ReadPidl(pstm: win32more.Windows.Win32.System.Com.IStream, ppidlOut: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def IStream_WritePidl(pstm: win32more.Windows.Win32.System.Com.IStream, pidlWrite: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def IStream_ReadStr(pstm: win32more.Windows.Win32.System.Com.IStream, ppsz: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def IStream_WriteStr(pstm: win32more.Windows.Win32.System.Com.IStream, psz: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def IStream_Copy(pstmFrom: win32more.Windows.Win32.System.Com.IStream, pstmTo: win32more.Windows.Win32.System.Com.IStream, cb: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHGetViewStatePropertyBag(pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pszBagName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHFormatDateTimeA(pft: POINTER(win32more.Windows.Win32.Foundation.FILETIME), pdwFlags: POINTER(UInt32), pszBuf: win32more.Windows.Win32.Foundation.PSTR, cchBuf: UInt32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def SHFormatDateTimeW(pft: POINTER(win32more.Windows.Win32.Foundation.FILETIME), pdwFlags: POINTER(UInt32), pszBuf: win32more.Windows.Win32.Foundation.PWSTR, cchBuf: UInt32) -> Int32: ...
SHFormatDateTime = UnicodeAlias('SHFormatDateTimeW')
@winfunctype('SHLWAPI.dll')
def SHAnsiToUnicode(pszSrc: win32more.Windows.Win32.Foundation.PSTR, pwszDst: win32more.Windows.Win32.Foundation.PWSTR, cwchBuf: Int32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def SHAnsiToAnsi(pszSrc: win32more.Windows.Win32.Foundation.PSTR, pszDst: win32more.Windows.Win32.Foundation.PSTR, cchBuf: Int32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def SHUnicodeToAnsi(pwszSrc: win32more.Windows.Win32.Foundation.PWSTR, pszDst: win32more.Windows.Win32.Foundation.PSTR, cchBuf: Int32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def SHUnicodeToUnicode(pwzSrc: win32more.Windows.Win32.Foundation.PWSTR, pwzDst: win32more.Windows.Win32.Foundation.PWSTR, cwchBuf: Int32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def SHMessageBoxCheckA(hwnd: win32more.Windows.Win32.Foundation.HWND, pszText: win32more.Windows.Win32.Foundation.PSTR, pszCaption: win32more.Windows.Win32.Foundation.PSTR, uType: UInt32, iDefault: Int32, pszRegVal: win32more.Windows.Win32.Foundation.PSTR) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def SHMessageBoxCheckW(hwnd: win32more.Windows.Win32.Foundation.HWND, pszText: win32more.Windows.Win32.Foundation.PWSTR, pszCaption: win32more.Windows.Win32.Foundation.PWSTR, uType: UInt32, iDefault: Int32, pszRegVal: win32more.Windows.Win32.Foundation.PWSTR) -> Int32: ...
SHMessageBoxCheck = UnicodeAlias('SHMessageBoxCheckW')
@winfunctype('SHLWAPI.dll')
def SHSendMessageBroadcastA(uMsg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.LRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHSendMessageBroadcastW(uMsg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.LRESULT: ...
SHSendMessageBroadcast = UnicodeAlias('SHSendMessageBroadcastW')
@winfunctype('SHLWAPI.dll')
def SHStripMneumonicA(pszMenu: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.CHAR: ...
@winfunctype('SHLWAPI.dll')
def SHStripMneumonicW(pszMenu: win32more.Windows.Win32.Foundation.PWSTR) -> Char: ...
SHStripMneumonic = UnicodeAlias('SHStripMneumonicW')
@winfunctype('SHLWAPI.dll')
def IsOS(dwOS: win32more.Windows.Win32.UI.Shell.OS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def SHGlobalCounterGetValue(id: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def SHGlobalCounterIncrement(id: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def SHGlobalCounterDecrement(id: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def SHAllocShared(pvData: VoidPtr, dwSize: UInt32, dwProcessId: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('SHLWAPI.dll')
def SHFreeShared(hData: win32more.Windows.Win32.Foundation.HANDLE, dwProcessId: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def SHLockShared(hData: win32more.Windows.Win32.Foundation.HANDLE, dwProcessId: UInt32) -> VoidPtr: ...
@winfunctype('SHLWAPI.dll')
def SHUnlockShared(pvData: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def WhichPlatform() -> UInt32: ...
@winfunctype('SHLWAPI.dll')
def QISearch(that: VoidPtr, pqit: POINTER(win32more.Windows.Win32.UI.Shell.QITAB), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHIsLowMemoryMachine(dwType: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def GetMenuPosFromID(hmenu: win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU, id: UInt32) -> Int32: ...
@winfunctype('SHLWAPI.dll')
def SHGetInverseCMAP(pbMap: POINTER(Byte), cbMap: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHAutoComplete(hwndEdit: win32more.Windows.Win32.Foundation.HWND, dwFlags: win32more.Windows.Win32.UI.Shell.SHELL_AUTOCOMPLETE_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHCreateThreadRef(pcRef: POINTER(Int32), ppunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHSetThreadRef(punk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHGetThreadRef(ppunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHSkipJunction(pbc: win32more.Windows.Win32.System.Com.IBindCtx, pclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def SHCreateThread(pfnThreadProc: win32more.Windows.Win32.System.Threading.LPTHREAD_START_ROUTINE, pData: VoidPtr, flags: UInt32, pfnCallback: win32more.Windows.Win32.System.Threading.LPTHREAD_START_ROUTINE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def SHCreateThreadWithHandle(pfnThreadProc: win32more.Windows.Win32.System.Threading.LPTHREAD_START_ROUTINE, pData: VoidPtr, flags: UInt32, pfnCallback: win32more.Windows.Win32.System.Threading.LPTHREAD_START_ROUTINE, pHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('SHLWAPI.dll')
def SHReleaseThreadRef() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('SHLWAPI.dll')
def SHCreateShellPalette(hdc: win32more.Windows.Win32.Graphics.Gdi.HDC) -> win32more.Windows.Win32.Graphics.Gdi.HPALETTE: ...
@winfunctype('SHLWAPI.dll')
def ColorRGBToHLS(clrRGB: win32more.Windows.Win32.Foundation.COLORREF, pwHue: POINTER(UInt16), pwLuminance: POINTER(UInt16), pwSaturation: POINTER(UInt16)) -> Void: ...
@winfunctype('SHLWAPI.dll')
def ColorHLSToRGB(wHue: UInt16, wLuminance: UInt16, wSaturation: UInt16) -> win32more.Windows.Win32.Foundation.COLORREF: ...
@winfunctype('SHLWAPI.dll')
def ColorAdjustLuma(clrRGB: win32more.Windows.Win32.Foundation.COLORREF, n: Int32, fScale: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.COLORREF: ...
@winfunctype('SHLWAPI.dll')
def IsInternetESCEnabled() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('hlink.dll')
def HlinkCreateFromMoniker(pimkTrgt: win32more.Windows.Win32.System.Com.IMoniker, pwzLocation: win32more.Windows.Win32.Foundation.PWSTR, pwzFriendlyName: win32more.Windows.Win32.Foundation.PWSTR, pihlsite: win32more.Windows.Win32.UI.Shell.IHlinkSite, dwSiteData: UInt32, piunkOuter: win32more.Windows.Win32.System.Com.IUnknown, riid: POINTER(Guid), ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkCreateFromString(pwzTarget: win32more.Windows.Win32.Foundation.PWSTR, pwzLocation: win32more.Windows.Win32.Foundation.PWSTR, pwzFriendlyName: win32more.Windows.Win32.Foundation.PWSTR, pihlsite: win32more.Windows.Win32.UI.Shell.IHlinkSite, dwSiteData: UInt32, piunkOuter: win32more.Windows.Win32.System.Com.IUnknown, riid: POINTER(Guid), ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkCreateFromData(piDataObj: win32more.Windows.Win32.System.Com.IDataObject, pihlsite: win32more.Windows.Win32.UI.Shell.IHlinkSite, dwSiteData: UInt32, piunkOuter: win32more.Windows.Win32.System.Com.IUnknown, riid: POINTER(Guid), ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkQueryCreateFromData(piDataObj: win32more.Windows.Win32.System.Com.IDataObject) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkClone(pihl: win32more.Windows.Win32.UI.Shell.IHlink, riid: POINTER(Guid), pihlsiteForClone: win32more.Windows.Win32.UI.Shell.IHlinkSite, dwSiteData: UInt32, ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkCreateBrowseContext(piunkOuter: win32more.Windows.Win32.System.Com.IUnknown, riid: POINTER(Guid), ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkNavigateToStringReference(pwzTarget: win32more.Windows.Win32.Foundation.PWSTR, pwzLocation: win32more.Windows.Win32.Foundation.PWSTR, pihlsite: win32more.Windows.Win32.UI.Shell.IHlinkSite, dwSiteData: UInt32, pihlframe: win32more.Windows.Win32.UI.Shell.IHlinkFrame, grfHLNF: UInt32, pibc: win32more.Windows.Win32.System.Com.IBindCtx, pibsc: win32more.Windows.Win32.System.Com.IBindStatusCallback, pihlbc: win32more.Windows.Win32.UI.Shell.IHlinkBrowseContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkNavigate(pihl: win32more.Windows.Win32.UI.Shell.IHlink, pihlframe: win32more.Windows.Win32.UI.Shell.IHlinkFrame, grfHLNF: UInt32, pbc: win32more.Windows.Win32.System.Com.IBindCtx, pibsc: win32more.Windows.Win32.System.Com.IBindStatusCallback, pihlbc: win32more.Windows.Win32.UI.Shell.IHlinkBrowseContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkOnNavigate(pihlframe: win32more.Windows.Win32.UI.Shell.IHlinkFrame, pihlbc: win32more.Windows.Win32.UI.Shell.IHlinkBrowseContext, grfHLNF: UInt32, pimkTarget: win32more.Windows.Win32.System.Com.IMoniker, pwzLocation: win32more.Windows.Win32.Foundation.PWSTR, pwzFriendlyName: win32more.Windows.Win32.Foundation.PWSTR, puHLID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkUpdateStackItem(pihlframe: win32more.Windows.Win32.UI.Shell.IHlinkFrame, pihlbc: win32more.Windows.Win32.UI.Shell.IHlinkBrowseContext, uHLID: UInt32, pimkTrgt: win32more.Windows.Win32.System.Com.IMoniker, pwzLocation: win32more.Windows.Win32.Foundation.PWSTR, pwzFriendlyName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkOnRenameDocument(dwReserved: UInt32, pihlbc: win32more.Windows.Win32.UI.Shell.IHlinkBrowseContext, pimkOld: win32more.Windows.Win32.System.Com.IMoniker, pimkNew: win32more.Windows.Win32.System.Com.IMoniker) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkResolveMonikerForData(pimkReference: win32more.Windows.Win32.System.Com.IMoniker, reserved: UInt32, pibc: win32more.Windows.Win32.System.Com.IBindCtx, cFmtetc: UInt32, rgFmtetc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC), pibsc: win32more.Windows.Win32.System.Com.IBindStatusCallback, pimkBase: win32more.Windows.Win32.System.Com.IMoniker) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkResolveStringForData(pwzReference: win32more.Windows.Win32.Foundation.PWSTR, reserved: UInt32, pibc: win32more.Windows.Win32.System.Com.IBindCtx, cFmtetc: UInt32, rgFmtetc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC), pibsc: win32more.Windows.Win32.System.Com.IBindStatusCallback, pimkBase: win32more.Windows.Win32.System.Com.IMoniker) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkParseDisplayName(pibc: win32more.Windows.Win32.System.Com.IBindCtx, pwzDisplayName: win32more.Windows.Win32.Foundation.PWSTR, fNoForceAbs: win32more.Windows.Win32.Foundation.BOOL, pcchEaten: POINTER(UInt32), ppimk: POINTER(win32more.Windows.Win32.System.Com.IMoniker)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkCreateExtensionServices(pwzAdditionalHeaders: win32more.Windows.Win32.Foundation.PWSTR, phwnd: win32more.Windows.Win32.Foundation.HWND, pszUsername: win32more.Windows.Win32.Foundation.PWSTR, pszPassword: win32more.Windows.Win32.Foundation.PWSTR, piunkOuter: win32more.Windows.Win32.System.Com.IUnknown, riid: POINTER(Guid), ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkPreprocessMoniker(pibc: win32more.Windows.Win32.System.Com.IBindCtx, pimkIn: win32more.Windows.Win32.System.Com.IMoniker, ppimkOut: POINTER(win32more.Windows.Win32.System.Com.IMoniker)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def OleSaveToStreamEx(piunk: win32more.Windows.Win32.System.Com.IUnknown, pistm: win32more.Windows.Win32.System.Com.IStream, fClearDirty: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkSetSpecialReference(uReference: UInt32, pwzReference: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkGetSpecialReference(uReference: UInt32, ppwzReference: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkCreateShortcut(grfHLSHORTCUTF: UInt32, pihl: win32more.Windows.Win32.UI.Shell.IHlink, pwzDir: win32more.Windows.Win32.Foundation.PWSTR, pwzFileName: win32more.Windows.Win32.Foundation.PWSTR, ppwzShortcutFile: POINTER(win32more.Windows.Win32.Foundation.PWSTR), dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkCreateShortcutFromMoniker(grfHLSHORTCUTF: UInt32, pimkTarget: win32more.Windows.Win32.System.Com.IMoniker, pwzLocation: win32more.Windows.Win32.Foundation.PWSTR, pwzDir: win32more.Windows.Win32.Foundation.PWSTR, pwzFileName: win32more.Windows.Win32.Foundation.PWSTR, ppwzShortcutFile: POINTER(win32more.Windows.Win32.Foundation.PWSTR), dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkCreateShortcutFromString(grfHLSHORTCUTF: UInt32, pwzTarget: win32more.Windows.Win32.Foundation.PWSTR, pwzLocation: win32more.Windows.Win32.Foundation.PWSTR, pwzDir: win32more.Windows.Win32.Foundation.PWSTR, pwzFileName: win32more.Windows.Win32.Foundation.PWSTR, ppwzShortcutFile: POINTER(win32more.Windows.Win32.Foundation.PWSTR), dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkResolveShortcut(pwzShortcutFileName: win32more.Windows.Win32.Foundation.PWSTR, pihlsite: win32more.Windows.Win32.UI.Shell.IHlinkSite, dwSiteData: UInt32, piunkOuter: win32more.Windows.Win32.System.Com.IUnknown, riid: POINTER(Guid), ppvObj: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkResolveShortcutToMoniker(pwzShortcutFileName: win32more.Windows.Win32.Foundation.PWSTR, ppimkTarget: POINTER(win32more.Windows.Win32.System.Com.IMoniker), ppwzLocation: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkResolveShortcutToString(pwzShortcutFileName: win32more.Windows.Win32.Foundation.PWSTR, ppwzTarget: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ppwzLocation: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkIsShortcut(pwzFileName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkGetValueFromParams(pwzParams: win32more.Windows.Win32.Foundation.PWSTR, pwzName: win32more.Windows.Win32.Foundation.PWSTR, ppwzValue: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('hlink.dll')
def HlinkTranslateURL(pwzURL: win32more.Windows.Win32.Foundation.PWSTR, grfFlags: UInt32, ppwzTranslatedURL: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathIsUNCEx(pszPath: win32more.Windows.Win32.Foundation.PWSTR, ppszServer: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchIsRoot(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchAddBackslashEx(pszPath: win32more.Windows.Win32.Foundation.PWSTR, cchPath: UIntPtr, ppszEnd: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pcchRemaining: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchAddBackslash(pszPath: win32more.Windows.Win32.Foundation.PWSTR, cchPath: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchRemoveBackslashEx(pszPath: win32more.Windows.Win32.Foundation.PWSTR, cchPath: UIntPtr, ppszEnd: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pcchRemaining: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchRemoveBackslash(pszPath: win32more.Windows.Win32.Foundation.PWSTR, cchPath: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchSkipRoot(pszPath: win32more.Windows.Win32.Foundation.PWSTR, ppszRootEnd: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchStripToRoot(pszPath: win32more.Windows.Win32.Foundation.PWSTR, cchPath: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchRemoveFileSpec(pszPath: win32more.Windows.Win32.Foundation.PWSTR, cchPath: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchFindExtension(pszPath: win32more.Windows.Win32.Foundation.PWSTR, cchPath: UIntPtr, ppszExt: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchAddExtension(pszPath: win32more.Windows.Win32.Foundation.PWSTR, cchPath: UIntPtr, pszExt: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchRenameExtension(pszPath: win32more.Windows.Win32.Foundation.PWSTR, cchPath: UIntPtr, pszExt: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchRemoveExtension(pszPath: win32more.Windows.Win32.Foundation.PWSTR, cchPath: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchCanonicalizeEx(pszPathOut: win32more.Windows.Win32.Foundation.PWSTR, cchPathOut: UIntPtr, pszPathIn: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: win32more.Windows.Win32.UI.Shell.PATHCCH_OPTIONS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchCanonicalize(pszPathOut: win32more.Windows.Win32.Foundation.PWSTR, cchPathOut: UIntPtr, pszPathIn: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchCombineEx(pszPathOut: win32more.Windows.Win32.Foundation.PWSTR, cchPathOut: UIntPtr, pszPathIn: win32more.Windows.Win32.Foundation.PWSTR, pszMore: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: win32more.Windows.Win32.UI.Shell.PATHCCH_OPTIONS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchCombine(pszPathOut: win32more.Windows.Win32.Foundation.PWSTR, cchPathOut: UIntPtr, pszPathIn: win32more.Windows.Win32.Foundation.PWSTR, pszMore: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchAppendEx(pszPath: win32more.Windows.Win32.Foundation.PWSTR, cchPath: UIntPtr, pszMore: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: win32more.Windows.Win32.UI.Shell.PATHCCH_OPTIONS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchAppend(pszPath: win32more.Windows.Win32.Foundation.PWSTR, cchPath: UIntPtr, pszMore: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathCchStripPrefix(pszPath: win32more.Windows.Win32.Foundation.PWSTR, cchPath: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathAllocCombine(pszPathIn: win32more.Windows.Win32.Foundation.PWSTR, pszMore: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: win32more.Windows.Win32.UI.Shell.PATHCCH_OPTIONS, ppszPathOut: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-path-l1-1-0.dll')
def PathAllocCanonicalize(pszPathIn: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: win32more.Windows.Win32.UI.Shell.PATHCCH_OPTIONS, ppszPathOut: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('api-ms-win-core-psm-appnotify-l1-1-0.dll')
def RegisterAppStateChangeNotification(Routine: win32more.Windows.Win32.UI.Shell.PAPPSTATE_CHANGE_ROUTINE, Context: VoidPtr, Registration: POINTER(win32more.Windows.Win32.UI.Shell.PAPPSTATE_REGISTRATION)) -> UInt32: ...
@winfunctype('api-ms-win-core-psm-appnotify-l1-1-0.dll')
def UnregisterAppStateChangeNotification(Registration: win32more.Windows.Win32.UI.Shell.PAPPSTATE_REGISTRATION) -> Void: ...
@winfunctype('api-ms-win-core-psm-appnotify-l1-1-1.dll')
def RegisterAppConstrainedChangeNotification(Routine: win32more.Windows.Win32.UI.Shell.PAPPCONSTRAIN_CHANGE_ROUTINE, Context: VoidPtr, Registration: POINTER(win32more.Windows.Win32.UI.Shell.PAPPCONSTRAIN_REGISTRATION)) -> UInt32: ...
@winfunctype('api-ms-win-core-psm-appnotify-l1-1-1.dll')
def UnregisterAppConstrainedChangeNotification(Registration: win32more.Windows.Win32.UI.Shell.PAPPCONSTRAIN_REGISTRATION) -> Void: ...
AppShellVerbHandler = Guid('{4ed3a719-cea8-4bd9-910d-e252f997afc2}')
AppStartupLink = Guid('{273eb5e7-88b0-4843-bfef-e2c81d43aae5}')
AppVisibility = Guid('{7e5fe3d9-985f-4908-91f9-ee19f9fd1514}')
ApplicationActivationManager = Guid('{45ba127d-10a8-46ea-8ab7-56ea9078943c}')
ApplicationAssociationRegistration = Guid('{591209c7-767b-42b2-9fba-44ee4615f2c7}')
ApplicationAssociationRegistrationUI = Guid('{1968106d-f3b5-44cf-890e-116fcb9ecef1}')
ApplicationDesignModeSettings = Guid('{958a6fb5-dcb2-4faf-aafd-7fb054ad1a3b}')
ApplicationDestinations = Guid('{86c14003-4d6b-4ef3-a7b4-0506663b2e68}')
ApplicationDocumentLists = Guid('{86bec222-30f2-47e0-9f25-60d11cd75c28}')
AttachmentServices = Guid('{4125dd96-e03a-4103-8f70-e0597d803b9c}')
class BANDINFOSFB(Structure):
    dwMask: UInt32
    dwStateMask: UInt32
    dwState: UInt32
    crBkgnd: win32more.Windows.Win32.Foundation.COLORREF
    crBtnLt: win32more.Windows.Win32.Foundation.COLORREF
    crBtnDk: win32more.Windows.Win32.Foundation.COLORREF
    wViewMode: UInt16
    wAlign: UInt16
    psf: win32more.Windows.Win32.UI.Shell.IShellFolder
    pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)
BANDSITECID = Int32
BSID_BANDADDED: win32more.Windows.Win32.UI.Shell.BANDSITECID = 0
BSID_BANDREMOVED: win32more.Windows.Win32.UI.Shell.BANDSITECID = 1
class BANDSITEINFO(Structure):
    dwMask: UInt32
    dwState: UInt32
    dwStyle: UInt32
class BANNER_NOTIFICATION(Structure):
    event: win32more.Windows.Win32.UI.Shell.BANNER_NOTIFICATION_EVENT
    providerIdentity: win32more.Windows.Win32.Foundation.PWSTR
    contentId: win32more.Windows.Win32.Foundation.PWSTR
BANNER_NOTIFICATION_EVENT = Int32
BNE_Rendered: win32more.Windows.Win32.UI.Shell.BANNER_NOTIFICATION_EVENT = 0
BNE_Hovered: win32more.Windows.Win32.UI.Shell.BANNER_NOTIFICATION_EVENT = 1
BNE_Closed: win32more.Windows.Win32.UI.Shell.BANNER_NOTIFICATION_EVENT = 2
BNE_Dismissed: win32more.Windows.Win32.UI.Shell.BANNER_NOTIFICATION_EVENT = 3
BNE_Button1Clicked: win32more.Windows.Win32.UI.Shell.BANNER_NOTIFICATION_EVENT = 4
BNE_Button2Clicked: win32more.Windows.Win32.UI.Shell.BANNER_NOTIFICATION_EVENT = 5
class BASEBROWSERDATALH(Structure):
    _hwnd: win32more.Windows.Win32.Foundation.HWND
    _ptl: win32more.Windows.Win32.UI.Shell.ITravelLog
    _phlf: win32more.Windows.Win32.UI.Shell.IHlinkFrame
    _pautoWB2: win32more.Windows.Win32.UI.Shell.IWebBrowser2
    _pautoEDS: win32more.Windows.Win32.UI.Shell.IExpDispSupport
    _pautoSS: win32more.Windows.Win32.UI.Shell.IShellService
    _eSecureLockIcon: Int32
    _fCreatingViewWindow: Annotated[UInt32, 1]
    _uActivateState: UInt32
    _pidlViewState: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)
    _pctView: win32more.Windows.Win32.System.Ole.IOleCommandTarget
    _pidlCur: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)
    _psv: win32more.Windows.Win32.UI.Shell.IShellView
    _psf: win32more.Windows.Win32.UI.Shell.IShellFolder
    _hwndView: win32more.Windows.Win32.Foundation.HWND
    _pszTitleCur: win32more.Windows.Win32.Foundation.PWSTR
    _pidlPending: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)
    _psvPending: win32more.Windows.Win32.UI.Shell.IShellView
    _psfPending: win32more.Windows.Win32.UI.Shell.IShellFolder
    _hwndViewPending: win32more.Windows.Win32.Foundation.HWND
    _pszTitlePending: win32more.Windows.Win32.Foundation.PWSTR
    _fIsViewMSHTML: win32more.Windows.Win32.Foundation.BOOL
    _fPrivacyImpacted: win32more.Windows.Win32.Foundation.BOOL
    _clsidView: Guid
    _clsidViewPending: Guid
    _hwndFrame: win32more.Windows.Win32.Foundation.HWND
    _lPhishingFilterStatus: Int32
class BASEBROWSERDATAXP(Structure):
    _hwnd: win32more.Windows.Win32.Foundation.HWND
    _ptl: win32more.Windows.Win32.UI.Shell.ITravelLog
    _phlf: win32more.Windows.Win32.UI.Shell.IHlinkFrame
    _pautoWB2: win32more.Windows.Win32.UI.Shell.IWebBrowser2
    _pautoEDS: win32more.Windows.Win32.UI.Shell.IExpDispSupportXP
    _pautoSS: win32more.Windows.Win32.UI.Shell.IShellService
    _eSecureLockIcon: Int32
    _fCreatingViewWindow: Annotated[UInt32, 1]
    _uActivateState: UInt32
    _pidlViewState: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)
    _pctView: win32more.Windows.Win32.System.Ole.IOleCommandTarget
    _pidlCur: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)
    _psv: win32more.Windows.Win32.UI.Shell.IShellView
    _psf: win32more.Windows.Win32.UI.Shell.IShellFolder
    _hwndView: win32more.Windows.Win32.Foundation.HWND
    _pszTitleCur: win32more.Windows.Win32.Foundation.PWSTR
    _pidlPending: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)
    _psvPending: win32more.Windows.Win32.UI.Shell.IShellView
    _psfPending: win32more.Windows.Win32.UI.Shell.IShellFolder
    _hwndViewPending: win32more.Windows.Win32.Foundation.HWND
    _pszTitlePending: win32more.Windows.Win32.Foundation.PWSTR
    _fIsViewMSHTML: win32more.Windows.Win32.Foundation.BOOL
    _fPrivacyImpacted: win32more.Windows.Win32.Foundation.BOOL
    _clsidView: Guid
    _clsidViewPending: Guid
    _hwndFrame: win32more.Windows.Win32.Foundation.HWND
@winfunctype_pointer
def BFFCALLBACK(hwnd: win32more.Windows.Win32.Foundation.HWND, uMsg: UInt32, lParam: win32more.Windows.Win32.Foundation.LPARAM, lpData: win32more.Windows.Win32.Foundation.LPARAM) -> Int32: ...
BNSTATE = Int32
BNS_NORMAL: win32more.Windows.Win32.UI.Shell.BNSTATE = 0
BNS_BEGIN_NAVIGATE: win32more.Windows.Win32.UI.Shell.BNSTATE = 1
BNS_NAVIGATE: win32more.Windows.Win32.UI.Shell.BNSTATE = 2
class BROWSEINFOA(Structure):
    hwndOwner: win32more.Windows.Win32.Foundation.HWND
    pidlRoot: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)
    pszDisplayName: win32more.Windows.Win32.Foundation.PSTR
    lpszTitle: win32more.Windows.Win32.Foundation.PSTR
    ulFlags: UInt32
    lpfn: win32more.Windows.Win32.UI.Shell.BFFCALLBACK
    lParam: win32more.Windows.Win32.Foundation.LPARAM
    iImage: Int32
class BROWSEINFOW(Structure):
    hwndOwner: win32more.Windows.Win32.Foundation.HWND
    pidlRoot: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)
    pszDisplayName: win32more.Windows.Win32.Foundation.PWSTR
    lpszTitle: win32more.Windows.Win32.Foundation.PWSTR
    ulFlags: UInt32
    lpfn: win32more.Windows.Win32.UI.Shell.BFFCALLBACK
    lParam: win32more.Windows.Win32.Foundation.LPARAM
    iImage: Int32
BROWSEINFO = UnicodeAlias('BROWSEINFOW')
BrowserNavConstants = Int32
navOpenInNewWindow: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = 1
navNoHistory: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = 2
navNoReadFromCache: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = 4
navNoWriteToCache: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = 8
navAllowAutosearch: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = 16
navBrowserBar: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = 32
navHyperlink: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = 64
navEnforceRestricted: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = 128
navNewWindowsManaged: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = 256
navUntrustedForDownload: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = 512
navTrustedForActiveX: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = 1024
navOpenInNewTab: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = 2048
navOpenInBackgroundTab: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = 4096
navKeepWordWheelText: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = 8192
navVirtualTab: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = 16384
navBlockRedirectsXDomain: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = 32768
navOpenNewForegroundTab: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = 65536
navTravelLogScreenshot: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = 131072
navDeferUnload: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = 262144
navSpeculative: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = 524288
navSuggestNewWindow: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = 1048576
navSuggestNewTab: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = 2097152
navReserved1: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = 4194304
navHomepageNavigate: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = 8388608
navRefresh: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = 16777216
navHostNavigation: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = 33554432
navReserved2: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = 67108864
navReserved3: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = 134217728
navReserved4: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = 268435456
navReserved5: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = 536870912
navReserved6: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = 1073741824
navReserved7: win32more.Windows.Win32.UI.Shell.BrowserNavConstants = -2147483648
class CABINETSTATE(Structure):
    cLength: UInt16
    nVersion: UInt16
    fFullPathTitle: Annotated[Int32, 1]
    fSaveLocalView: Annotated[Int32, 1]
    fNotShell: Annotated[Int32, 1]
    fSimpleDefault: Annotated[Int32, 1]
    fDontShowDescBar: Annotated[Int32, 1]
    fNewWindowMode: Annotated[Int32, 1]
    fShowCompColor: Annotated[Int32, 1]
    fDontPrettyNames: Annotated[Int32, 1]
    fAdminsCreateCommonGroups: Annotated[Int32, 1]
    fUnusedFlags: Annotated[Int32, 7]
    fMenuEnumFilter: UInt32
    _pack_ = 1
CATEGORYINFO_FLAGS = Int32
CATINFO_NORMAL: win32more.Windows.Win32.UI.Shell.CATEGORYINFO_FLAGS = 0
CATINFO_COLLAPSED: win32more.Windows.Win32.UI.Shell.CATEGORYINFO_FLAGS = 1
CATINFO_HIDDEN: win32more.Windows.Win32.UI.Shell.CATEGORYINFO_FLAGS = 2
CATINFO_EXPANDED: win32more.Windows.Win32.UI.Shell.CATEGORYINFO_FLAGS = 4
CATINFO_NOHEADER: win32more.Windows.Win32.UI.Shell.CATEGORYINFO_FLAGS = 8
CATINFO_NOTCOLLAPSIBLE: win32more.Windows.Win32.UI.Shell.CATEGORYINFO_FLAGS = 16
CATINFO_NOHEADERCOUNT: win32more.Windows.Win32.UI.Shell.CATEGORYINFO_FLAGS = 32
CATINFO_SUBSETTED: win32more.Windows.Win32.UI.Shell.CATEGORYINFO_FLAGS = 64
CATINFO_SEPARATE_IMAGES: win32more.Windows.Win32.UI.Shell.CATEGORYINFO_FLAGS = 128
CATINFO_SHOWEMPTY: win32more.Windows.Win32.UI.Shell.CATEGORYINFO_FLAGS = 256
class CATEGORY_INFO(Structure):
    cif: win32more.Windows.Win32.UI.Shell.CATEGORYINFO_FLAGS
    wszName: Char * 260
CATSORT_FLAGS = Int32
CATSORT_DEFAULT: win32more.Windows.Win32.UI.Shell.CATSORT_FLAGS = 0
CATSORT_NAME: win32more.Windows.Win32.UI.Shell.CATSORT_FLAGS = 1
CDBURNINGEXTENSIONRET = Int32
CDBE_RET_DEFAULT: win32more.Windows.Win32.UI.Shell.CDBURNINGEXTENSIONRET = 0
CDBE_RET_DONTRUNOTHEREXTS: win32more.Windows.Win32.UI.Shell.CDBURNINGEXTENSIONRET = 1
CDBE_RET_STOPWIZARD: win32more.Windows.Win32.UI.Shell.CDBURNINGEXTENSIONRET = 2
CDBurn = Guid('{fbeb8a05-beee-4442-804e-409d6c4515e9}')
CDCONTROLSTATEF = Int32
CDCS_INACTIVE: win32more.Windows.Win32.UI.Shell.CDCONTROLSTATEF = 0
CDCS_ENABLED: win32more.Windows.Win32.UI.Shell.CDCONTROLSTATEF = 1
CDCS_VISIBLE: win32more.Windows.Win32.UI.Shell.CDCONTROLSTATEF = 2
CDCS_ENABLEDVISIBLE: win32more.Windows.Win32.UI.Shell.CDCONTROLSTATEF = 3
class CIDA(Structure):
    cidl: UInt32
    aoffset: UInt32 * 1
    _pack_ = 1
class CIE4ConnectionPoint(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IConnectionPoint
    @commethod(8)
    def DoInvokeIE4(self, pf: POINTER(win32more.Windows.Win32.Foundation.BOOL), ppv: POINTER(VoidPtr), dispid: Int32, pdispparams: POINTER(win32more.Windows.Win32.System.Com.DISPPARAMS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def DoInvokePIDLIE4(self, dispid: Int32, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), fCanCancel: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class CMINVOKECOMMANDINFO(Structure):
    cbSize: UInt32
    fMask: UInt32
    hwnd: win32more.Windows.Win32.Foundation.HWND
    lpVerb: win32more.Windows.Win32.Foundation.PSTR
    lpParameters: win32more.Windows.Win32.Foundation.PSTR
    lpDirectory: win32more.Windows.Win32.Foundation.PSTR
    nShow: Int32
    dwHotKey: UInt32
    hIcon: win32more.Windows.Win32.Foundation.HANDLE
class CMINVOKECOMMANDINFOEX(Structure):
    cbSize: UInt32
    fMask: UInt32
    hwnd: win32more.Windows.Win32.Foundation.HWND
    lpVerb: win32more.Windows.Win32.Foundation.PSTR
    lpParameters: win32more.Windows.Win32.Foundation.PSTR
    lpDirectory: win32more.Windows.Win32.Foundation.PSTR
    nShow: Int32
    dwHotKey: UInt32
    hIcon: win32more.Windows.Win32.Foundation.HANDLE
    lpTitle: win32more.Windows.Win32.Foundation.PSTR
    lpVerbW: win32more.Windows.Win32.Foundation.PWSTR
    lpParametersW: win32more.Windows.Win32.Foundation.PWSTR
    lpDirectoryW: win32more.Windows.Win32.Foundation.PWSTR
    lpTitleW: win32more.Windows.Win32.Foundation.PWSTR
    ptInvoke: win32more.Windows.Win32.Foundation.POINT
class CMINVOKECOMMANDINFOEX_REMOTE(Structure):
    cbSize: UInt32
    fMask: UInt32
    hwnd: win32more.Windows.Win32.Foundation.HWND
    lpVerbString: win32more.Windows.Win32.Foundation.PSTR
    lpParameters: win32more.Windows.Win32.Foundation.PSTR
    lpDirectory: win32more.Windows.Win32.Foundation.PSTR
    nShow: Int32
    dwHotKey: UInt32
    lpTitle: win32more.Windows.Win32.Foundation.PSTR
    lpVerbWString: win32more.Windows.Win32.Foundation.PWSTR
    lpParametersW: win32more.Windows.Win32.Foundation.PWSTR
    lpDirectoryW: win32more.Windows.Win32.Foundation.PWSTR
    lpTitleW: win32more.Windows.Win32.Foundation.PWSTR
    ptInvoke: win32more.Windows.Win32.Foundation.POINT
    lpVerbInt: UInt32
    lpVerbWInt: UInt32
class CM_COLUMNINFO(Structure):
    cbSize: UInt32
    dwMask: UInt32
    dwState: UInt32
    uWidth: UInt32
    uDefaultWidth: UInt32
    uIdealWidth: UInt32
    wszName: Char * 80
CM_ENUM_FLAGS = Int32
CM_ENUM_ALL: win32more.Windows.Win32.UI.Shell.CM_ENUM_FLAGS = 1
CM_ENUM_VISIBLE: win32more.Windows.Win32.UI.Shell.CM_ENUM_FLAGS = 2
CM_MASK = Int32
CM_MASK_WIDTH: win32more.Windows.Win32.UI.Shell.CM_MASK = 1
CM_MASK_DEFAULTWIDTH: win32more.Windows.Win32.UI.Shell.CM_MASK = 2
CM_MASK_IDEALWIDTH: win32more.Windows.Win32.UI.Shell.CM_MASK = 4
CM_MASK_NAME: win32more.Windows.Win32.UI.Shell.CM_MASK = 8
CM_MASK_STATE: win32more.Windows.Win32.UI.Shell.CM_MASK = 16
CM_SET_WIDTH_VALUE = Int32
CM_WIDTH_USEDEFAULT: win32more.Windows.Win32.UI.Shell.CM_SET_WIDTH_VALUE = -1
CM_WIDTH_AUTOSIZE: win32more.Windows.Win32.UI.Shell.CM_SET_WIDTH_VALUE = -2
CM_STATE = Int32
CM_STATE_NONE: win32more.Windows.Win32.UI.Shell.CM_STATE = 0
CM_STATE_VISIBLE: win32more.Windows.Win32.UI.Shell.CM_STATE = 1
CM_STATE_FIXEDWIDTH: win32more.Windows.Win32.UI.Shell.CM_STATE = 2
CM_STATE_NOSORTBYFOLDERNESS: win32more.Windows.Win32.UI.Shell.CM_STATE = 4
CM_STATE_ALWAYSVISIBLE: win32more.Windows.Win32.UI.Shell.CM_STATE = 8
class CONFIRM_CONFLICT_ITEM(Structure):
    pShellItem: win32more.Windows.Win32.UI.Shell.IShellItem2
    pszOriginalName: win32more.Windows.Win32.Foundation.PWSTR
    pszAlternateName: win32more.Windows.Win32.Foundation.PWSTR
    pszLocationShort: win32more.Windows.Win32.Foundation.PWSTR
    pszLocationFull: win32more.Windows.Win32.Foundation.PWSTR
    nType: win32more.Windows.Win32.UI.Shell.SYNCMGR_CONFLICT_ITEM_TYPE
class CONFIRM_CONFLICT_RESULT_INFO(Structure):
    pszNewName: win32more.Windows.Win32.Foundation.PWSTR
    iItemIndex: UInt32
class CPLINFO(Structure):
    idIcon: Int32
    idName: Int32
    idInfo: Int32
    lData: IntPtr
    _pack_ = 1
CPVIEW = Int32
CPVIEW_CLASSIC: win32more.Windows.Win32.UI.Shell.CPVIEW = 0
CPVIEW_ALLITEMS: win32more.Windows.Win32.UI.Shell.CPVIEW = 0
CPVIEW_CATEGORY: win32more.Windows.Win32.UI.Shell.CPVIEW = 1
CPVIEW_HOME: win32more.Windows.Win32.UI.Shell.CPVIEW = 1
CREDENTIAL_PROVIDER_ACCOUNT_OPTIONS = Int32
CPAO_NONE: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_ACCOUNT_OPTIONS = 0
CPAO_EMPTY_LOCAL: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_ACCOUNT_OPTIONS = 1
CPAO_EMPTY_CONNECTED: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_ACCOUNT_OPTIONS = 2
CREDENTIAL_PROVIDER_CREDENTIAL_FIELD_OPTIONS = Int32
CPCFO_NONE: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_CREDENTIAL_FIELD_OPTIONS = 0
CPCFO_ENABLE_PASSWORD_REVEAL: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_CREDENTIAL_FIELD_OPTIONS = 1
CPCFO_IS_EMAIL_ADDRESS: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_CREDENTIAL_FIELD_OPTIONS = 2
CPCFO_ENABLE_TOUCH_KEYBOARD_AUTO_INVOKE: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_CREDENTIAL_FIELD_OPTIONS = 4
CPCFO_NUMBERS_ONLY: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_CREDENTIAL_FIELD_OPTIONS = 8
CPCFO_SHOW_ENGLISH_KEYBOARD: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_CREDENTIAL_FIELD_OPTIONS = 16
class CREDENTIAL_PROVIDER_CREDENTIAL_SERIALIZATION(Structure):
    ulAuthenticationPackage: UInt32
    clsidCredentialProvider: Guid
    cbSerialization: UInt32
    rgbSerialization: POINTER(Byte)
class CREDENTIAL_PROVIDER_FIELD_DESCRIPTOR(Structure):
    dwFieldID: UInt32
    cpft: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_FIELD_TYPE
    pszLabel: win32more.Windows.Win32.Foundation.PWSTR
    guidFieldType: Guid
CREDENTIAL_PROVIDER_FIELD_INTERACTIVE_STATE = Int32
CPFIS_NONE: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_FIELD_INTERACTIVE_STATE = 0
CPFIS_READONLY: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_FIELD_INTERACTIVE_STATE = 1
CPFIS_DISABLED: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_FIELD_INTERACTIVE_STATE = 2
CPFIS_FOCUSED: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_FIELD_INTERACTIVE_STATE = 3
CREDENTIAL_PROVIDER_FIELD_STATE = Int32
CPFS_HIDDEN: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_FIELD_STATE = 0
CPFS_DISPLAY_IN_SELECTED_TILE: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_FIELD_STATE = 1
CPFS_DISPLAY_IN_DESELECTED_TILE: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_FIELD_STATE = 2
CPFS_DISPLAY_IN_BOTH: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_FIELD_STATE = 3
CREDENTIAL_PROVIDER_FIELD_TYPE = Int32
CPFT_INVALID: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_FIELD_TYPE = 0
CPFT_LARGE_TEXT: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_FIELD_TYPE = 1
CPFT_SMALL_TEXT: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_FIELD_TYPE = 2
CPFT_COMMAND_LINK: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_FIELD_TYPE = 3
CPFT_EDIT_TEXT: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_FIELD_TYPE = 4
CPFT_PASSWORD_TEXT: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_FIELD_TYPE = 5
CPFT_TILE_IMAGE: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_FIELD_TYPE = 6
CPFT_CHECKBOX: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_FIELD_TYPE = 7
CPFT_COMBOBOX: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_FIELD_TYPE = 8
CPFT_SUBMIT_BUTTON: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_FIELD_TYPE = 9
CREDENTIAL_PROVIDER_GET_SERIALIZATION_RESPONSE = Int32
CPGSR_NO_CREDENTIAL_NOT_FINISHED: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_GET_SERIALIZATION_RESPONSE = 0
CPGSR_NO_CREDENTIAL_FINISHED: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_GET_SERIALIZATION_RESPONSE = 1
CPGSR_RETURN_CREDENTIAL_FINISHED: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_GET_SERIALIZATION_RESPONSE = 2
CPGSR_RETURN_NO_CREDENTIAL_FINISHED: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_GET_SERIALIZATION_RESPONSE = 3
CREDENTIAL_PROVIDER_STATUS_ICON = Int32
CPSI_NONE: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_STATUS_ICON = 0
CPSI_ERROR: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_STATUS_ICON = 1
CPSI_WARNING: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_STATUS_ICON = 2
CPSI_SUCCESS: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_STATUS_ICON = 3
CREDENTIAL_PROVIDER_USAGE_SCENARIO = Int32
CPUS_INVALID: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_USAGE_SCENARIO = 0
CPUS_LOGON: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_USAGE_SCENARIO = 1
CPUS_UNLOCK_WORKSTATION: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_USAGE_SCENARIO = 2
CPUS_CHANGE_PASSWORD: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_USAGE_SCENARIO = 3
CPUS_CREDUI: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_USAGE_SCENARIO = 4
CPUS_PLAP: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_USAGE_SCENARIO = 5
class CSFV(Structure):
    cbSize: UInt32
    pshf: win32more.Windows.Win32.UI.Shell.IShellFolder
    psvOuter: win32more.Windows.Win32.UI.Shell.IShellView
    pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)
    lEvents: Int32
    pfnCallback: win32more.Windows.Win32.UI.Shell.LPFNVIEWCALLBACK
    fvm: win32more.Windows.Win32.UI.Shell.FOLDERVIEWMODE
CScriptErrorList = Guid('{efd01300-160f-11d2-bb2e-00805ff7efca}')
CommandStateChangeConstants = Int32
CSC_UPDATECOMMANDS: win32more.Windows.Win32.UI.Shell.CommandStateChangeConstants = -1
CSC_NAVIGATEFORWARD: win32more.Windows.Win32.UI.Shell.CommandStateChangeConstants = 1
CSC_NAVIGATEBACK: win32more.Windows.Win32.UI.Shell.CommandStateChangeConstants = 2
ConflictFolder = Guid('{289978ac-a101-4341-a817-21eba7fd046d}')
class DATABLOCK_HEADER(Structure):
    cbSize: UInt32
    dwSignature: UInt32
    _pack_ = 1
DATAOBJ_GET_ITEM_FLAGS = Int32
DOGIF_DEFAULT: win32more.Windows.Win32.UI.Shell.DATAOBJ_GET_ITEM_FLAGS = 0
DOGIF_TRAVERSE_LINK: win32more.Windows.Win32.UI.Shell.DATAOBJ_GET_ITEM_FLAGS = 1
DOGIF_NO_HDROP: win32more.Windows.Win32.UI.Shell.DATAOBJ_GET_ITEM_FLAGS = 2
DOGIF_NO_URL: win32more.Windows.Win32.UI.Shell.DATAOBJ_GET_ITEM_FLAGS = 4
DOGIF_ONLY_IF_ONE: win32more.Windows.Win32.UI.Shell.DATAOBJ_GET_ITEM_FLAGS = 8
DEFAULTSAVEFOLDERTYPE = Int32
DSFT_DETECT: win32more.Windows.Win32.UI.Shell.DEFAULTSAVEFOLDERTYPE = 1
DSFT_PRIVATE: win32more.Windows.Win32.UI.Shell.DEFAULTSAVEFOLDERTYPE = 2
DSFT_PUBLIC: win32more.Windows.Win32.UI.Shell.DEFAULTSAVEFOLDERTYPE = 3
DEFAULT_FOLDER_MENU_RESTRICTIONS = Int32
DFMR_DEFAULT: win32more.Windows.Win32.UI.Shell.DEFAULT_FOLDER_MENU_RESTRICTIONS = 0
DFMR_NO_STATIC_VERBS: win32more.Windows.Win32.UI.Shell.DEFAULT_FOLDER_MENU_RESTRICTIONS = 8
DFMR_STATIC_VERBS_ONLY: win32more.Windows.Win32.UI.Shell.DEFAULT_FOLDER_MENU_RESTRICTIONS = 16
DFMR_NO_RESOURCE_VERBS: win32more.Windows.Win32.UI.Shell.DEFAULT_FOLDER_MENU_RESTRICTIONS = 32
DFMR_OPTIN_HANDLERS_ONLY: win32more.Windows.Win32.UI.Shell.DEFAULT_FOLDER_MENU_RESTRICTIONS = 64
DFMR_RESOURCE_AND_FOLDER_VERBS_ONLY: win32more.Windows.Win32.UI.Shell.DEFAULT_FOLDER_MENU_RESTRICTIONS = 128
DFMR_USE_SPECIFIED_HANDLERS: win32more.Windows.Win32.UI.Shell.DEFAULT_FOLDER_MENU_RESTRICTIONS = 256
DFMR_USE_SPECIFIED_VERBS: win32more.Windows.Win32.UI.Shell.DEFAULT_FOLDER_MENU_RESTRICTIONS = 512
DFMR_NO_ASYNC_VERBS: win32more.Windows.Win32.UI.Shell.DEFAULT_FOLDER_MENU_RESTRICTIONS = 1024
DFMR_NO_NATIVECPU_VERBS: win32more.Windows.Win32.UI.Shell.DEFAULT_FOLDER_MENU_RESTRICTIONS = 2048
DFMR_NO_NONWOW_VERBS: win32more.Windows.Win32.UI.Shell.DEFAULT_FOLDER_MENU_RESTRICTIONS = 4096
class DEFCONTEXTMENU(Structure):
    hwnd: win32more.Windows.Win32.Foundation.HWND
    pcmcb: win32more.Windows.Win32.UI.Shell.IContextMenuCB
    pidlFolder: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)
    psf: win32more.Windows.Win32.UI.Shell.IShellFolder
    cidl: UInt32
    apidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST))
    punkAssociationInfo: win32more.Windows.Win32.System.Com.IUnknown
    cKeys: UInt32
    aKeys: POINTER(win32more.Windows.Win32.System.Registry.HKEY)
DEF_SHARE_ID = Int32
DEFSHAREID_USERS: win32more.Windows.Win32.UI.Shell.DEF_SHARE_ID = 1
DEFSHAREID_PUBLIC: win32more.Windows.Win32.UI.Shell.DEF_SHARE_ID = 2
class DELEGATEITEMID(Structure):
    cbSize: UInt16
    wOuter: UInt16
    cbInner: UInt16
    rgb: Byte * 1
    _pack_ = 1
DESKBANDCID = Int32
DBID_BANDINFOCHANGED: win32more.Windows.Win32.UI.Shell.DESKBANDCID = 0
DBID_SHOWONLY: win32more.Windows.Win32.UI.Shell.DESKBANDCID = 1
DBID_MAXIMIZEBAND: win32more.Windows.Win32.UI.Shell.DESKBANDCID = 2
DBID_PUSHCHEVRON: win32more.Windows.Win32.UI.Shell.DESKBANDCID = 3
DBID_DELAYINIT: win32more.Windows.Win32.UI.Shell.DESKBANDCID = 4
DBID_FINISHINIT: win32more.Windows.Win32.UI.Shell.DESKBANDCID = 5
DBID_SETWINDOWTHEME: win32more.Windows.Win32.UI.Shell.DESKBANDCID = 6
DBID_PERMITAUTOHIDE: win32more.Windows.Win32.UI.Shell.DESKBANDCID = 7
class DESKBANDINFO(Structure):
    dwMask: UInt32
    ptMinSize: win32more.Windows.Win32.Foundation.POINTL
    ptMaxSize: win32more.Windows.Win32.Foundation.POINTL
    ptIntegral: win32more.Windows.Win32.Foundation.POINTL
    ptActual: win32more.Windows.Win32.Foundation.POINTL
    wszTitle: Char * 256
    dwModeFlags: UInt32
    crBkgnd: win32more.Windows.Win32.Foundation.COLORREF
DESKTOP_SLIDESHOW_DIRECTION = Int32
DSD_FORWARD: win32more.Windows.Win32.UI.Shell.DESKTOP_SLIDESHOW_DIRECTION = 0
DSD_BACKWARD: win32more.Windows.Win32.UI.Shell.DESKTOP_SLIDESHOW_DIRECTION = 1
DESKTOP_SLIDESHOW_OPTIONS = Int32
DSO_SHUFFLEIMAGES: win32more.Windows.Win32.UI.Shell.DESKTOP_SLIDESHOW_OPTIONS = 1
DESKTOP_SLIDESHOW_STATE = Int32
DSS_ENABLED: win32more.Windows.Win32.UI.Shell.DESKTOP_SLIDESHOW_STATE = 1
DSS_SLIDESHOW: win32more.Windows.Win32.UI.Shell.DESKTOP_SLIDESHOW_STATE = 2
DSS_DISABLED_BY_REMOTE_SESSION: win32more.Windows.Win32.UI.Shell.DESKTOP_SLIDESHOW_STATE = 4
DESKTOP_WALLPAPER_POSITION = Int32
DWPOS_CENTER: win32more.Windows.Win32.UI.Shell.DESKTOP_WALLPAPER_POSITION = 0
DWPOS_TILE: win32more.Windows.Win32.UI.Shell.DESKTOP_WALLPAPER_POSITION = 1
DWPOS_STRETCH: win32more.Windows.Win32.UI.Shell.DESKTOP_WALLPAPER_POSITION = 2
DWPOS_FIT: win32more.Windows.Win32.UI.Shell.DESKTOP_WALLPAPER_POSITION = 3
DWPOS_FILL: win32more.Windows.Win32.UI.Shell.DESKTOP_WALLPAPER_POSITION = 4
DWPOS_SPAN: win32more.Windows.Win32.UI.Shell.DESKTOP_WALLPAPER_POSITION = 5
class DETAILSINFO(Structure):
    pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)
    fmt: Int32
    cxChar: Int32
    str: win32more.Windows.Win32.UI.Shell.Common.STRRET
    iImage: Int32
class DFConstraint(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{4a3df050-23bd-11d2-939f-00a0c91eedba}')
    @commethod(7)
    def get_Name(self, pbs: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Value(self, pv: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class DFMICS(Structure):
    cbSize: UInt32
    fMask: UInt32
    lParam: win32more.Windows.Win32.Foundation.LPARAM
    idCmdFirst: UInt32
    idDefMax: UInt32
    pici: POINTER(win32more.Windows.Win32.UI.Shell.CMINVOKECOMMANDINFO)
    punkSite: win32more.Windows.Win32.System.Com.IUnknown
DFM_CMD = Int32
DFM_CMD_DELETE: win32more.Windows.Win32.UI.Shell.DFM_CMD = -1
DFM_CMD_MOVE: win32more.Windows.Win32.UI.Shell.DFM_CMD = -2
DFM_CMD_COPY: win32more.Windows.Win32.UI.Shell.DFM_CMD = -3
DFM_CMD_LINK: win32more.Windows.Win32.UI.Shell.DFM_CMD = -4
DFM_CMD_PROPERTIES: win32more.Windows.Win32.UI.Shell.DFM_CMD = -5
DFM_CMD_NEWFOLDER: win32more.Windows.Win32.UI.Shell.DFM_CMD = -6
DFM_CMD_PASTE: win32more.Windows.Win32.UI.Shell.DFM_CMD = -7
DFM_CMD_VIEWLIST: win32more.Windows.Win32.UI.Shell.DFM_CMD = -8
DFM_CMD_VIEWDETAILS: win32more.Windows.Win32.UI.Shell.DFM_CMD = -9
DFM_CMD_PASTELINK: win32more.Windows.Win32.UI.Shell.DFM_CMD = -10
DFM_CMD_PASTESPECIAL: win32more.Windows.Win32.UI.Shell.DFM_CMD = -11
DFM_CMD_MODALPROP: win32more.Windows.Win32.UI.Shell.DFM_CMD = -12
DFM_CMD_RENAME: win32more.Windows.Win32.UI.Shell.DFM_CMD = -13
DFM_MESSAGE_ID = Int32
DFM_MERGECONTEXTMENU: win32more.Windows.Win32.UI.Shell.DFM_MESSAGE_ID = 1
DFM_INVOKECOMMAND: win32more.Windows.Win32.UI.Shell.DFM_MESSAGE_ID = 2
DFM_GETHELPTEXT: win32more.Windows.Win32.UI.Shell.DFM_MESSAGE_ID = 5
DFM_WM_MEASUREITEM: win32more.Windows.Win32.UI.Shell.DFM_MESSAGE_ID = 6
DFM_WM_DRAWITEM: win32more.Windows.Win32.UI.Shell.DFM_MESSAGE_ID = 7
DFM_WM_INITMENUPOPUP: win32more.Windows.Win32.UI.Shell.DFM_MESSAGE_ID = 8
DFM_VALIDATECMD: win32more.Windows.Win32.UI.Shell.DFM_MESSAGE_ID = 9
DFM_MERGECONTEXTMENU_TOP: win32more.Windows.Win32.UI.Shell.DFM_MESSAGE_ID = 10
DFM_GETHELPTEXTW: win32more.Windows.Win32.UI.Shell.DFM_MESSAGE_ID = 11
DFM_INVOKECOMMANDEX: win32more.Windows.Win32.UI.Shell.DFM_MESSAGE_ID = 12
DFM_MAPCOMMANDNAME: win32more.Windows.Win32.UI.Shell.DFM_MESSAGE_ID = 13
DFM_GETDEFSTATICID: win32more.Windows.Win32.UI.Shell.DFM_MESSAGE_ID = 14
DFM_GETVERBW: win32more.Windows.Win32.UI.Shell.DFM_MESSAGE_ID = 15
DFM_GETVERBA: win32more.Windows.Win32.UI.Shell.DFM_MESSAGE_ID = 16
DFM_MERGECONTEXTMENU_BOTTOM: win32more.Windows.Win32.UI.Shell.DFM_MESSAGE_ID = 17
DFM_MODIFYQCMFLAGS: win32more.Windows.Win32.UI.Shell.DFM_MESSAGE_ID = 18
DISPLAY_DEVICE_TYPE = Int32
DEVICE_PRIMARY: win32more.Windows.Win32.UI.Shell.DISPLAY_DEVICE_TYPE = 0
DEVICE_IMMERSIVE: win32more.Windows.Win32.UI.Shell.DISPLAY_DEVICE_TYPE = 1
@winfunctype_pointer
def DLLGETVERSIONPROC(param0: POINTER(win32more.Windows.Win32.UI.Shell.DLLVERSIONINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class DLLVERSIONINFO(Structure):
    cbSize: UInt32
    dwMajorVersion: UInt32
    dwMinorVersion: UInt32
    dwBuildNumber: UInt32
    dwPlatformID: UInt32
class DLLVERSIONINFO2(Structure):
    info1: win32more.Windows.Win32.UI.Shell.DLLVERSIONINFO
    dwFlags: UInt32
    ullVersion: UInt64
if ARCH in 'X64,ARM64':
    class DRAGINFOA(Structure):
        uSize: UInt32
        pt: win32more.Windows.Win32.Foundation.POINT
        fNC: win32more.Windows.Win32.Foundation.BOOL
        lpFileList: win32more.Windows.Win32.Foundation.PSTR
        grfKeyState: UInt32
elif ARCH in 'X86':
    class DRAGINFOA(Structure):
        uSize: UInt32
        pt: win32more.Windows.Win32.Foundation.POINT
        fNC: win32more.Windows.Win32.Foundation.BOOL
        lpFileList: win32more.Windows.Win32.Foundation.PSTR
        grfKeyState: UInt32
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class DRAGINFOW(Structure):
        uSize: UInt32
        pt: win32more.Windows.Win32.Foundation.POINT
        fNC: win32more.Windows.Win32.Foundation.BOOL
        lpFileList: win32more.Windows.Win32.Foundation.PWSTR
        grfKeyState: UInt32
elif ARCH in 'X86':
    class DRAGINFOW(Structure):
        uSize: UInt32
        pt: win32more.Windows.Win32.Foundation.POINT
        fNC: win32more.Windows.Win32.Foundation.BOOL
        lpFileList: win32more.Windows.Win32.Foundation.PWSTR
        grfKeyState: UInt32
        _pack_ = 1
if ARCH in 'X64,ARM64':
    DRAGINFO = UnicodeAlias('DRAGINFOW')
elif ARCH in 'X86':
    DRAGINFO = UnicodeAlias('DRAGINFOW')
class DROPDESCRIPTION(Structure):
    type: win32more.Windows.Win32.UI.Shell.DROPIMAGETYPE
    szMessage: Char * 260
    szInsert: Char * 260
    _pack_ = 1
class DROPFILES(Structure):
    pFiles: UInt32
    pt: win32more.Windows.Win32.Foundation.POINT
    fNC: win32more.Windows.Win32.Foundation.BOOL
    fWide: win32more.Windows.Win32.Foundation.BOOL
    _pack_ = 1
DROPIMAGETYPE = Int32
DROPIMAGE_INVALID: win32more.Windows.Win32.UI.Shell.DROPIMAGETYPE = -1
DROPIMAGE_NONE: win32more.Windows.Win32.UI.Shell.DROPIMAGETYPE = 0
DROPIMAGE_COPY: win32more.Windows.Win32.UI.Shell.DROPIMAGETYPE = 1
DROPIMAGE_MOVE: win32more.Windows.Win32.UI.Shell.DROPIMAGETYPE = 2
DROPIMAGE_LINK: win32more.Windows.Win32.UI.Shell.DROPIMAGETYPE = 4
DROPIMAGE_LABEL: win32more.Windows.Win32.UI.Shell.DROPIMAGETYPE = 6
DROPIMAGE_WARNING: win32more.Windows.Win32.UI.Shell.DROPIMAGETYPE = 7
DROPIMAGE_NOIMAGE: win32more.Windows.Win32.UI.Shell.DROPIMAGETYPE = 8
DSH_FLAGS = Int32
DSH_ALLOWDROPDESCRIPTIONTEXT: win32more.Windows.Win32.UI.Shell.DSH_FLAGS = 1
class DShellFolderViewEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{62112aa2-ebe4-11cf-a5fb-0020afe7292d}')
class DShellNameSpaceEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{55136806-b2de-11d1-b9f2-00a0c98bc547}')
class DShellWindowsEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{fe4106e0-399a-11d0-a48c-00a0c90a8f39}')
class DWebBrowserEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{eab22ac2-30c1-11cf-a7eb-0000c05bae0b}')
class DWebBrowserEvents2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{34a715a0-6587-11d0-924a-0020afc7ac4d}')
DefFolderMenu = Guid('{c63382be-7933-48d0-9ac8-85fb46be2fdd}')
DesktopGadget = Guid('{924ccc1b-6562-4c85-8657-d177925222b6}')
DesktopWallpaper = Guid('{c2cf3110-460e-4fc1-b9d0-8a1c0c9cc4bd}')
DestinationList = Guid('{77f10cf0-3db5-4966-b520-b7c54fd35ed6}')
DocPropShellExtension = Guid('{883373c3-bf89-11d1-be35-080036b11a03}')
DriveSizeCategorizer = Guid('{94357b53-ca29-4b78-83ae-e8fe7409134f}')
DriveTypeCategorizer = Guid('{b0a8f3cf-4333-4bab-8873-1ccb1cada48b}')
EC_HOST_UI_MODE = Int32
ECHUIM_DESKTOP: win32more.Windows.Win32.UI.Shell.EC_HOST_UI_MODE = 0
ECHUIM_IMMERSIVE: win32more.Windows.Win32.UI.Shell.EC_HOST_UI_MODE = 1
ECHUIM_SYSTEM_LAUNCHER: win32more.Windows.Win32.UI.Shell.EC_HOST_UI_MODE = 2
EDGE_GESTURE_KIND = Int32
EGK_TOUCH: win32more.Windows.Win32.UI.Shell.EDGE_GESTURE_KIND = 0
EGK_KEYBOARD: win32more.Windows.Win32.UI.Shell.EDGE_GESTURE_KIND = 1
EGK_MOUSE: win32more.Windows.Win32.UI.Shell.EDGE_GESTURE_KIND = 2
EXPLORER_BROWSER_FILL_FLAGS = Int32
EBF_NONE: win32more.Windows.Win32.UI.Shell.EXPLORER_BROWSER_FILL_FLAGS = 0
EBF_SELECTFROMDATAOBJECT: win32more.Windows.Win32.UI.Shell.EXPLORER_BROWSER_FILL_FLAGS = 256
EBF_NODROPTARGET: win32more.Windows.Win32.UI.Shell.EXPLORER_BROWSER_FILL_FLAGS = 512
EXPLORER_BROWSER_OPTIONS = Int32
EBO_NONE: win32more.Windows.Win32.UI.Shell.EXPLORER_BROWSER_OPTIONS = 0
EBO_NAVIGATEONCE: win32more.Windows.Win32.UI.Shell.EXPLORER_BROWSER_OPTIONS = 1
EBO_SHOWFRAMES: win32more.Windows.Win32.UI.Shell.EXPLORER_BROWSER_OPTIONS = 2
EBO_ALWAYSNAVIGATE: win32more.Windows.Win32.UI.Shell.EXPLORER_BROWSER_OPTIONS = 4
EBO_NOTRAVELLOG: win32more.Windows.Win32.UI.Shell.EXPLORER_BROWSER_OPTIONS = 8
EBO_NOWRAPPERWINDOW: win32more.Windows.Win32.UI.Shell.EXPLORER_BROWSER_OPTIONS = 16
EBO_HTMLSHAREPOINTVIEW: win32more.Windows.Win32.UI.Shell.EXPLORER_BROWSER_OPTIONS = 32
EBO_NOBORDER: win32more.Windows.Win32.UI.Shell.EXPLORER_BROWSER_OPTIONS = 64
EBO_NOPERSISTVIEWSTATE: win32more.Windows.Win32.UI.Shell.EXPLORER_BROWSER_OPTIONS = 128
class EXP_DARWIN_LINK(Structure):
    dbh: win32more.Windows.Win32.UI.Shell.DATABLOCK_HEADER
    szDarwinID: win32more.Windows.Win32.Foundation.CHAR * 260
    szwDarwinID: Char * 260
    _pack_ = 1
class EXP_PROPERTYSTORAGE(Structure):
    cbSize: UInt32
    dwSignature: UInt32
    abPropertyStorage: Byte * 1
    _pack_ = 1
class EXP_SPECIAL_FOLDER(Structure):
    cbSize: UInt32
    dwSignature: UInt32
    idSpecialFolder: UInt32
    cbOffset: UInt32
    _pack_ = 1
class EXP_SZ_LINK(Structure):
    cbSize: UInt32
    dwSignature: UInt32
    szTarget: win32more.Windows.Win32.Foundation.CHAR * 260
    swzTarget: Char * 260
    _pack_ = 1
class EXTRASEARCH(Structure):
    guidSearch: Guid
    wszFriendlyName: Char * 80
    wszUrl: Char * 2084
EnumerableObjectCollection = Guid('{2d3468c1-36a7-43b6-ac24-d3f02fd9607a}')
ExecuteFolder = Guid('{11dbb47c-a525-400b-9e80-a54615a090c0}')
ExecuteUnknown = Guid('{e44e9428-bdbc-4987-a099-40dc8fd255e7}')
ExplorerBrowser = Guid('{71f96385-ddd6-48d3-a0c1-ae06e8b055fb}')
FDAP = Int32
FDAP_BOTTOM: win32more.Windows.Win32.UI.Shell.FDAP = 0
FDAP_TOP: win32more.Windows.Win32.UI.Shell.FDAP = 1
FDE_OVERWRITE_RESPONSE = Int32
FDEOR_DEFAULT: win32more.Windows.Win32.UI.Shell.FDE_OVERWRITE_RESPONSE = 0
FDEOR_ACCEPT: win32more.Windows.Win32.UI.Shell.FDE_OVERWRITE_RESPONSE = 1
FDEOR_REFUSE: win32more.Windows.Win32.UI.Shell.FDE_OVERWRITE_RESPONSE = 2
FDE_SHAREVIOLATION_RESPONSE = Int32
FDESVR_DEFAULT: win32more.Windows.Win32.UI.Shell.FDE_SHAREVIOLATION_RESPONSE = 0
FDESVR_ACCEPT: win32more.Windows.Win32.UI.Shell.FDE_SHAREVIOLATION_RESPONSE = 1
FDESVR_REFUSE: win32more.Windows.Win32.UI.Shell.FDE_SHAREVIOLATION_RESPONSE = 2
FD_FLAGS = Int32
FD_CLSID: win32more.Windows.Win32.UI.Shell.FD_FLAGS = 1
FD_SIZEPOINT: win32more.Windows.Win32.UI.Shell.FD_FLAGS = 2
FD_ATTRIBUTES: win32more.Windows.Win32.UI.Shell.FD_FLAGS = 4
FD_CREATETIME: win32more.Windows.Win32.UI.Shell.FD_FLAGS = 8
FD_ACCESSTIME: win32more.Windows.Win32.UI.Shell.FD_FLAGS = 16
FD_WRITESTIME: win32more.Windows.Win32.UI.Shell.FD_FLAGS = 32
FD_FILESIZE: win32more.Windows.Win32.UI.Shell.FD_FLAGS = 64
FD_PROGRESSUI: win32more.Windows.Win32.UI.Shell.FD_FLAGS = 16384
FD_LINKUI: win32more.Windows.Win32.UI.Shell.FD_FLAGS = 32768
FD_UNICODE: win32more.Windows.Win32.UI.Shell.FD_FLAGS = -2147483648
FFFP_MODE = Int32
FFFP_EXACTMATCH: win32more.Windows.Win32.UI.Shell.FFFP_MODE = 0
FFFP_NEARESTPARENTMATCH: win32more.Windows.Win32.UI.Shell.FFFP_MODE = 1
class FILEDESCRIPTORA(Structure):
    dwFlags: UInt32
    clsid: Guid
    sizel: win32more.Windows.Win32.Foundation.SIZE
    pointl: win32more.Windows.Win32.Foundation.POINTL
    dwFileAttributes: UInt32
    ftCreationTime: win32more.Windows.Win32.Foundation.FILETIME
    ftLastAccessTime: win32more.Windows.Win32.Foundation.FILETIME
    ftLastWriteTime: win32more.Windows.Win32.Foundation.FILETIME
    nFileSizeHigh: UInt32
    nFileSizeLow: UInt32
    cFileName: win32more.Windows.Win32.Foundation.CHAR * 260
    _pack_ = 1
class FILEDESCRIPTORW(Structure):
    dwFlags: UInt32
    clsid: Guid
    sizel: win32more.Windows.Win32.Foundation.SIZE
    pointl: win32more.Windows.Win32.Foundation.POINTL
    dwFileAttributes: UInt32
    ftCreationTime: win32more.Windows.Win32.Foundation.FILETIME
    ftLastAccessTime: win32more.Windows.Win32.Foundation.FILETIME
    ftLastWriteTime: win32more.Windows.Win32.Foundation.FILETIME
    nFileSizeHigh: UInt32
    nFileSizeLow: UInt32
    cFileName: Char * 260
    _pack_ = 1
FILEDESCRIPTOR = UnicodeAlias('FILEDESCRIPTORW')
class FILEGROUPDESCRIPTORA(Structure):
    cItems: UInt32
    fgd: win32more.Windows.Win32.UI.Shell.FILEDESCRIPTORA * 1
    _pack_ = 1
class FILEGROUPDESCRIPTORW(Structure):
    cItems: UInt32
    fgd: win32more.Windows.Win32.UI.Shell.FILEDESCRIPTORW * 1
    _pack_ = 1
FILEGROUPDESCRIPTOR = UnicodeAlias('FILEGROUPDESCRIPTORW')
FILEOPENDIALOGOPTIONS = UInt32
FOS_OVERWRITEPROMPT: win32more.Windows.Win32.UI.Shell.FILEOPENDIALOGOPTIONS = 2
FOS_STRICTFILETYPES: win32more.Windows.Win32.UI.Shell.FILEOPENDIALOGOPTIONS = 4
FOS_NOCHANGEDIR: win32more.Windows.Win32.UI.Shell.FILEOPENDIALOGOPTIONS = 8
FOS_PICKFOLDERS: win32more.Windows.Win32.UI.Shell.FILEOPENDIALOGOPTIONS = 32
FOS_FORCEFILESYSTEM: win32more.Windows.Win32.UI.Shell.FILEOPENDIALOGOPTIONS = 64
FOS_ALLNONSTORAGEITEMS: win32more.Windows.Win32.UI.Shell.FILEOPENDIALOGOPTIONS = 128
FOS_NOVALIDATE: win32more.Windows.Win32.UI.Shell.FILEOPENDIALOGOPTIONS = 256
FOS_ALLOWMULTISELECT: win32more.Windows.Win32.UI.Shell.FILEOPENDIALOGOPTIONS = 512
FOS_PATHMUSTEXIST: win32more.Windows.Win32.UI.Shell.FILEOPENDIALOGOPTIONS = 2048
FOS_FILEMUSTEXIST: win32more.Windows.Win32.UI.Shell.FILEOPENDIALOGOPTIONS = 4096
FOS_CREATEPROMPT: win32more.Windows.Win32.UI.Shell.FILEOPENDIALOGOPTIONS = 8192
FOS_SHAREAWARE: win32more.Windows.Win32.UI.Shell.FILEOPENDIALOGOPTIONS = 16384
FOS_NOREADONLYRETURN: win32more.Windows.Win32.UI.Shell.FILEOPENDIALOGOPTIONS = 32768
FOS_NOTESTFILECREATE: win32more.Windows.Win32.UI.Shell.FILEOPENDIALOGOPTIONS = 65536
FOS_HIDEMRUPLACES: win32more.Windows.Win32.UI.Shell.FILEOPENDIALOGOPTIONS = 131072
FOS_HIDEPINNEDPLACES: win32more.Windows.Win32.UI.Shell.FILEOPENDIALOGOPTIONS = 262144
FOS_NODEREFERENCELINKS: win32more.Windows.Win32.UI.Shell.FILEOPENDIALOGOPTIONS = 1048576
FOS_OKBUTTONNEEDSINTERACTION: win32more.Windows.Win32.UI.Shell.FILEOPENDIALOGOPTIONS = 2097152
FOS_DONTADDTORECENT: win32more.Windows.Win32.UI.Shell.FILEOPENDIALOGOPTIONS = 33554432
FOS_FORCESHOWHIDDEN: win32more.Windows.Win32.UI.Shell.FILEOPENDIALOGOPTIONS = 268435456
FOS_DEFAULTNOMINIMODE: win32more.Windows.Win32.UI.Shell.FILEOPENDIALOGOPTIONS = 536870912
FOS_FORCEPREVIEWPANEON: win32more.Windows.Win32.UI.Shell.FILEOPENDIALOGOPTIONS = 1073741824
FOS_SUPPORTSTREAMABLEITEMS: win32more.Windows.Win32.UI.Shell.FILEOPENDIALOGOPTIONS = 2147483648
FILEOPERATION_FLAGS = UInt32
FOFX_NOSKIPJUNCTIONS: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 65536
FOFX_PREFERHARDLINK: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 131072
FOFX_SHOWELEVATIONPROMPT: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 262144
FOFX_RECYCLEONDELETE: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 524288
FOFX_EARLYFAILURE: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 1048576
FOFX_PRESERVEFILEEXTENSIONS: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 2097152
FOFX_KEEPNEWERFILE: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 4194304
FOFX_NOCOPYHOOKS: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 8388608
FOFX_NOMINIMIZEBOX: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 16777216
FOFX_MOVEACLSACROSSVOLUMES: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 33554432
FOFX_DONTDISPLAYSOURCEPATH: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 67108864
FOFX_DONTDISPLAYDESTPATH: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 134217728
FOFX_REQUIREELEVATION: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 268435456
FOFX_ADDUNDORECORD: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 536870912
FOFX_COPYASDOWNLOAD: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 1073741824
FOFX_DONTDISPLAYLOCATIONS: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 2147483648
FOF_MULTIDESTFILES: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 1
FOF_CONFIRMMOUSE: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 2
FOF_SILENT: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 4
FOF_RENAMEONCOLLISION: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 8
FOF_NOCONFIRMATION: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 16
FOF_WANTMAPPINGHANDLE: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 32
FOF_ALLOWUNDO: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 64
FOF_FILESONLY: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 128
FOF_SIMPLEPROGRESS: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 256
FOF_NOCONFIRMMKDIR: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 512
FOF_NOERRORUI: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 1024
FOF_NOCOPYSECURITYATTRIBS: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 2048
FOF_NORECURSION: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 4096
FOF_NO_CONNECTED_ELEMENTS: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 8192
FOF_WANTNUKEWARNING: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 16384
FOF_NORECURSEREPARSE: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 32768
FOF_NO_UI: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS = 1556
FILETYPEATTRIBUTEFLAGS = Int32
FTA_None: win32more.Windows.Win32.UI.Shell.FILETYPEATTRIBUTEFLAGS = 0
FTA_Exclude: win32more.Windows.Win32.UI.Shell.FILETYPEATTRIBUTEFLAGS = 1
FTA_Show: win32more.Windows.Win32.UI.Shell.FILETYPEATTRIBUTEFLAGS = 2
FTA_HasExtension: win32more.Windows.Win32.UI.Shell.FILETYPEATTRIBUTEFLAGS = 4
FTA_NoEdit: win32more.Windows.Win32.UI.Shell.FILETYPEATTRIBUTEFLAGS = 8
FTA_NoRemove: win32more.Windows.Win32.UI.Shell.FILETYPEATTRIBUTEFLAGS = 16
FTA_NoNewVerb: win32more.Windows.Win32.UI.Shell.FILETYPEATTRIBUTEFLAGS = 32
FTA_NoEditVerb: win32more.Windows.Win32.UI.Shell.FILETYPEATTRIBUTEFLAGS = 64
FTA_NoRemoveVerb: win32more.Windows.Win32.UI.Shell.FILETYPEATTRIBUTEFLAGS = 128
FTA_NoEditDesc: win32more.Windows.Win32.UI.Shell.FILETYPEATTRIBUTEFLAGS = 256
FTA_NoEditIcon: win32more.Windows.Win32.UI.Shell.FILETYPEATTRIBUTEFLAGS = 512
FTA_NoEditDflt: win32more.Windows.Win32.UI.Shell.FILETYPEATTRIBUTEFLAGS = 1024
FTA_NoEditVerbCmd: win32more.Windows.Win32.UI.Shell.FILETYPEATTRIBUTEFLAGS = 2048
FTA_NoEditVerbExe: win32more.Windows.Win32.UI.Shell.FILETYPEATTRIBUTEFLAGS = 4096
FTA_NoDDE: win32more.Windows.Win32.UI.Shell.FILETYPEATTRIBUTEFLAGS = 8192
FTA_NoEditMIME: win32more.Windows.Win32.UI.Shell.FILETYPEATTRIBUTEFLAGS = 32768
FTA_OpenIsSafe: win32more.Windows.Win32.UI.Shell.FILETYPEATTRIBUTEFLAGS = 65536
FTA_AlwaysUnsafe: win32more.Windows.Win32.UI.Shell.FILETYPEATTRIBUTEFLAGS = 131072
FTA_NoRecentDocs: win32more.Windows.Win32.UI.Shell.FILETYPEATTRIBUTEFLAGS = 1048576
FTA_SafeForElevation: win32more.Windows.Win32.UI.Shell.FILETYPEATTRIBUTEFLAGS = 2097152
FTA_AlwaysUseDirectInvoke: win32more.Windows.Win32.UI.Shell.FILETYPEATTRIBUTEFLAGS = 4194304
class FILE_ATTRIBUTES_ARRAY(Structure):
    cItems: UInt32
    dwSumFileAttributes: UInt32
    dwProductFileAttributes: UInt32
    rgdwFileAttributes: UInt32 * 1
    _pack_ = 1
FILE_OPERATION_FLAGS2 = Int32
FOF2_NONE: win32more.Windows.Win32.UI.Shell.FILE_OPERATION_FLAGS2 = 0
FOF2_MERGEFOLDERSONCOLLISION: win32more.Windows.Win32.UI.Shell.FILE_OPERATION_FLAGS2 = 1
FILE_USAGE_TYPE = Int32
FUT_PLAYING: win32more.Windows.Win32.UI.Shell.FILE_USAGE_TYPE = 0
FUT_EDITING: win32more.Windows.Win32.UI.Shell.FILE_USAGE_TYPE = 1
FUT_GENERIC: win32more.Windows.Win32.UI.Shell.FILE_USAGE_TYPE = 2
FLYOUT_PLACEMENT = Int32
FP_DEFAULT: win32more.Windows.Win32.UI.Shell.FLYOUT_PLACEMENT = 0
FP_ABOVE: win32more.Windows.Win32.UI.Shell.FLYOUT_PLACEMENT = 1
FP_BELOW: win32more.Windows.Win32.UI.Shell.FLYOUT_PLACEMENT = 2
FP_LEFT: win32more.Windows.Win32.UI.Shell.FLYOUT_PLACEMENT = 3
FP_RIGHT: win32more.Windows.Win32.UI.Shell.FLYOUT_PLACEMENT = 4
FOLDERFLAGS = Int32
FWF_NONE: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 0
FWF_AUTOARRANGE: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 1
FWF_ABBREVIATEDNAMES: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 2
FWF_SNAPTOGRID: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 4
FWF_OWNERDATA: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 8
FWF_BESTFITWINDOW: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 16
FWF_DESKTOP: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 32
FWF_SINGLESEL: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 64
FWF_NOSUBFOLDERS: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 128
FWF_TRANSPARENT: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 256
FWF_NOCLIENTEDGE: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 512
FWF_NOSCROLL: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 1024
FWF_ALIGNLEFT: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 2048
FWF_NOICONS: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 4096
FWF_SHOWSELALWAYS: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 8192
FWF_NOVISIBLE: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 16384
FWF_SINGLECLICKACTIVATE: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 32768
FWF_NOWEBVIEW: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 65536
FWF_HIDEFILENAMES: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 131072
FWF_CHECKSELECT: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 262144
FWF_NOENUMREFRESH: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 524288
FWF_NOGROUPING: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 1048576
FWF_FULLROWSELECT: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 2097152
FWF_NOFILTERS: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 4194304
FWF_NOCOLUMNHEADER: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 8388608
FWF_NOHEADERINALLVIEWS: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 16777216
FWF_EXTENDEDTILES: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 33554432
FWF_TRICHECKSELECT: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 67108864
FWF_AUTOCHECKSELECT: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 134217728
FWF_NOBROWSERVIEWSTATE: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 268435456
FWF_SUBSETGROUPS: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 536870912
FWF_USESEARCHFOLDER: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = 1073741824
FWF_ALLOWRTLREADING: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS = -2147483648
FOLDERLOGICALVIEWMODE = Int32
FLVM_UNSPECIFIED: win32more.Windows.Win32.UI.Shell.FOLDERLOGICALVIEWMODE = -1
FLVM_FIRST: win32more.Windows.Win32.UI.Shell.FOLDERLOGICALVIEWMODE = 1
FLVM_DETAILS: win32more.Windows.Win32.UI.Shell.FOLDERLOGICALVIEWMODE = 1
FLVM_TILES: win32more.Windows.Win32.UI.Shell.FOLDERLOGICALVIEWMODE = 2
FLVM_ICONS: win32more.Windows.Win32.UI.Shell.FOLDERLOGICALVIEWMODE = 3
FLVM_LIST: win32more.Windows.Win32.UI.Shell.FOLDERLOGICALVIEWMODE = 4
FLVM_CONTENT: win32more.Windows.Win32.UI.Shell.FOLDERLOGICALVIEWMODE = 5
FLVM_LAST: win32more.Windows.Win32.UI.Shell.FOLDERLOGICALVIEWMODE = 5
class FOLDERSETDATA(Structure):
    _fs: win32more.Windows.Win32.UI.Shell.FOLDERSETTINGS
    _vidRestore: Guid
    _dwViewPriority: UInt32
class FOLDERSETTINGS(Structure):
    ViewMode: UInt32
    fFlags: UInt32
FOLDERVIEWMODE = Int32
FVM_AUTO: win32more.Windows.Win32.UI.Shell.FOLDERVIEWMODE = -1
FVM_FIRST: win32more.Windows.Win32.UI.Shell.FOLDERVIEWMODE = 1
FVM_ICON: win32more.Windows.Win32.UI.Shell.FOLDERVIEWMODE = 1
FVM_SMALLICON: win32more.Windows.Win32.UI.Shell.FOLDERVIEWMODE = 2
FVM_LIST: win32more.Windows.Win32.UI.Shell.FOLDERVIEWMODE = 3
FVM_DETAILS: win32more.Windows.Win32.UI.Shell.FOLDERVIEWMODE = 4
FVM_THUMBNAIL: win32more.Windows.Win32.UI.Shell.FOLDERVIEWMODE = 5
FVM_TILE: win32more.Windows.Win32.UI.Shell.FOLDERVIEWMODE = 6
FVM_THUMBSTRIP: win32more.Windows.Win32.UI.Shell.FOLDERVIEWMODE = 7
FVM_CONTENT: win32more.Windows.Win32.UI.Shell.FOLDERVIEWMODE = 8
FVM_LAST: win32more.Windows.Win32.UI.Shell.FOLDERVIEWMODE = 8
FOLDERVIEWOPTIONS = Int32
FVO_DEFAULT: win32more.Windows.Win32.UI.Shell.FOLDERVIEWOPTIONS = 0
FVO_VISTALAYOUT: win32more.Windows.Win32.UI.Shell.FOLDERVIEWOPTIONS = 1
FVO_CUSTOMPOSITION: win32more.Windows.Win32.UI.Shell.FOLDERVIEWOPTIONS = 2
FVO_CUSTOMORDERING: win32more.Windows.Win32.UI.Shell.FOLDERVIEWOPTIONS = 4
FVO_SUPPORTHYPERLINKS: win32more.Windows.Win32.UI.Shell.FOLDERVIEWOPTIONS = 8
FVO_NOANIMATIONS: win32more.Windows.Win32.UI.Shell.FOLDERVIEWOPTIONS = 16
FVO_NOSCROLLTIPS: win32more.Windows.Win32.UI.Shell.FOLDERVIEWOPTIONS = 32
FOLDER_ENUM_MODE = Int32
FEM_VIEWRESULT: win32more.Windows.Win32.UI.Shell.FOLDER_ENUM_MODE = 0
FEM_NAVIGATION: win32more.Windows.Win32.UI.Shell.FOLDER_ENUM_MODE = 1
FSCopyHandler = Guid('{d197380a-0a79-4dc8-a033-ed882c2fa14b}')
FVTEXTTYPE = Int32
FVST_EMPTYTEXT: win32more.Windows.Win32.UI.Shell.FVTEXTTYPE = 0
FileOpenDialog = Guid('{dc1c5a9c-e88a-4dde-a5a1-60f82a20aef7}')
FileOperation = Guid('{3ad05575-8857-4850-9277-11b85bdb8e09}')
FileSaveDialog = Guid('{c0b4e2f3-ba21-4773-8dba-335ec946eb8b}')
FileSearchBand = Guid('{c4ee31f3-4768-11d2-be5c-00a0c9a83da1}')
class Folder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{bbcbde60-c3ff-11ce-8350-444553540000}')
    @commethod(7)
    def get_Title(self, pbs: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Application(self, ppid: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Parent(self, ppid: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ParentFolder(self, ppsf: POINTER(win32more.Windows.Win32.UI.Shell.Folder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Items(self, ppid: POINTER(win32more.Windows.Win32.UI.Shell.FolderItems)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ParseName(self, bName: win32more.Windows.Win32.Foundation.BSTR, ppid: POINTER(win32more.Windows.Win32.UI.Shell.FolderItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def NewFolder(self, bName: win32more.Windows.Win32.Foundation.BSTR, vOptions: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def MoveHere(self, vItem: win32more.Windows.Win32.System.Variant.VARIANT, vOptions: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def CopyHere(self, vItem: win32more.Windows.Win32.System.Variant.VARIANT, vOptions: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetDetailsOf(self, vItem: win32more.Windows.Win32.System.Variant.VARIANT, iColumn: Int32, pbs: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class Folder2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.Folder
    _iid_ = Guid('{f0d2d8ef-3890-11d2-bf8b-00c04fb93661}')
    @commethod(17)
    def get_Self(self, ppfi: POINTER(win32more.Windows.Win32.UI.Shell.FolderItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_OfflineStatus(self, pul: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Synchronize(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_HaveToShowWebViewBarricade(self, pbHaveToShowWebViewBarricade: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def DismissedWebViewBarricade(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class Folder3(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.Folder2
    _iid_ = Guid('{a7ae5f64-c4d7-4d7f-9307-4d24ee54b841}')
    @commethod(22)
    def get_ShowWebViewBarricade(self, pbShowWebViewBarricade: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_ShowWebViewBarricade(self, bShowWebViewBarricade: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class FolderItem(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{fac32c80-cbe4-11ce-8350-444553540000}')
    @commethod(7)
    def get_Application(self, ppid: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Parent(self, ppid: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(self, pbs: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Name(self, bs: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Path(self, pbs: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_GetLink(self, ppid: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_GetFolder(self, ppid: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_IsLink(self, pb: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_IsFolder(self, pb: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_IsFileSystem(self, pb: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_IsBrowsable(self, pb: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_ModifyDate(self, pdt: POINTER(Double)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_ModifyDate(self, dt: Double) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_Size(self, pul: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_Type(self, pbs: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def Verbs(self, ppfic: POINTER(win32more.Windows.Win32.UI.Shell.FolderItemVerbs)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def InvokeVerb(self, vVerb: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class FolderItem2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.FolderItem
    _iid_ = Guid('{edc817aa-92b8-11d1-b075-00c04fc33aa5}')
    @commethod(24)
    def InvokeVerbEx(self, vVerb: win32more.Windows.Win32.System.Variant.VARIANT, vArgs: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def ExtendedProperty(self, bstrPropName: win32more.Windows.Win32.Foundation.BSTR, pvRet: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class FolderItemVerb(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{08ec3e00-50b0-11cf-960c-0080c7f4ee85}')
    @commethod(7)
    def get_Application(self, ppid: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Parent(self, ppid: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(self, pbs: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def DoIt(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class FolderItemVerbs(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{1f8352c0-50b0-11cf-960c-0080c7f4ee85}')
    @commethod(7)
    def get_Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Application(self, ppid: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Parent(self, ppid: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Item(self, index: win32more.Windows.Win32.System.Variant.VARIANT, ppid: POINTER(win32more.Windows.Win32.UI.Shell.FolderItemVerb)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def _NewEnum(self, ppunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class FolderItems(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{744129e0-cbe5-11ce-8350-444553540000}')
    @commethod(7)
    def get_Count(self, plCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Application(self, ppid: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Parent(self, ppid: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Item(self, index: win32more.Windows.Win32.System.Variant.VARIANT, ppid: POINTER(win32more.Windows.Win32.UI.Shell.FolderItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def _NewEnum(self, ppunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class FolderItems2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.FolderItems
    _iid_ = Guid('{c94f0ad0-f363-11d2-a327-00c04f8eec7f}')
    @commethod(12)
    def InvokeVerbEx(self, vVerb: win32more.Windows.Win32.System.Variant.VARIANT, vArgs: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class FolderItems3(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.FolderItems2
    _iid_ = Guid('{eaa7c309-bbec-49d5-821d-64d966cb667f}')
    @commethod(13)
    def Filter(self, grfFlags: Int32, bstrFileSpec: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Verbs(self, ppfic: POINTER(win32more.Windows.Win32.UI.Shell.FolderItemVerbs)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
FolderViewHost = Guid('{20b1cb23-6968-4eb9-b7d4-a66d00d07cee}')
FrameworkInputPane = Guid('{d5120aa3-46ba-44c5-822d-ca8092c1fc72}')
FreeSpaceCategorizer = Guid('{b5607793-24ac-44c7-82e2-831726aa6cb7}')
GPFIDL_FLAGS = UInt32
GPFIDL_DEFAULT: win32more.Windows.Win32.UI.Shell.GPFIDL_FLAGS = 0
GPFIDL_ALTNAME: win32more.Windows.Win32.UI.Shell.GPFIDL_FLAGS = 1
GPFIDL_UNCPRINTER: win32more.Windows.Win32.UI.Shell.GPFIDL_FLAGS = 2
GenericCredentialProvider = Guid('{25cbb996-92ed-457e-b28c-4774084bd562}')
HDROP = VoidPtr
class HELPINFO(Structure):
    cbSize: UInt32
    iContextType: win32more.Windows.Win32.UI.Shell.HELP_INFO_TYPE
    iCtrlId: Int32
    hItemHandle: win32more.Windows.Win32.Foundation.HANDLE
    dwContextId: UIntPtr
    MousePos: win32more.Windows.Win32.Foundation.POINT
class HELPWININFOA(Structure):
    wStructSize: Int32
    x: Int32
    y: Int32
    dx: Int32
    dy: Int32
    wMax: Int32
    rgchMember: win32more.Windows.Win32.Foundation.CHAR * 2
class HELPWININFOW(Structure):
    wStructSize: Int32
    x: Int32
    y: Int32
    dx: Int32
    dy: Int32
    wMax: Int32
    rgchMember: Char * 2
HELPWININFO = UnicodeAlias('HELPWININFOW')
HELP_INFO_TYPE = Int32
HELPINFO_WINDOW: win32more.Windows.Win32.UI.Shell.HELP_INFO_TYPE = 1
HELPINFO_MENUITEM: win32more.Windows.Win32.UI.Shell.HELP_INFO_TYPE = 2
HLBWIF_FLAGS = Int32
HLBWIF_HASFRAMEWNDINFO: win32more.Windows.Win32.UI.Shell.HLBWIF_FLAGS = 1
HLBWIF_HASDOCWNDINFO: win32more.Windows.Win32.UI.Shell.HLBWIF_FLAGS = 2
HLBWIF_FRAMEWNDMAXIMIZED: win32more.Windows.Win32.UI.Shell.HLBWIF_FLAGS = 4
HLBWIF_DOCWNDMAXIMIZED: win32more.Windows.Win32.UI.Shell.HLBWIF_FLAGS = 8
HLBWIF_HASWEBTOOLBARINFO: win32more.Windows.Win32.UI.Shell.HLBWIF_FLAGS = 16
HLBWIF_WEBTOOLBARHIDDEN: win32more.Windows.Win32.UI.Shell.HLBWIF_FLAGS = 32
class HLBWINFO(Structure):
    cbSize: UInt32
    grfHLBWIF: UInt32
    rcFramePos: win32more.Windows.Win32.Foundation.RECT
    rcDocPos: win32more.Windows.Win32.Foundation.RECT
    hltbinfo: win32more.Windows.Win32.UI.Shell.HLTBINFO
HLFNAMEF = Int32
HLFNAMEF_DEFAULT: win32more.Windows.Win32.UI.Shell.HLFNAMEF = 0
HLFNAMEF_TRYCACHE: win32more.Windows.Win32.UI.Shell.HLFNAMEF = 1
HLFNAMEF_TRYPRETTYTARGET: win32more.Windows.Win32.UI.Shell.HLFNAMEF = 2
HLFNAMEF_TRYFULLTARGET: win32more.Windows.Win32.UI.Shell.HLFNAMEF = 4
HLFNAMEF_TRYWIN95SHORTCUT: win32more.Windows.Win32.UI.Shell.HLFNAMEF = 8
HLID_INFO = UInt32
HLID_INVALID: win32more.Windows.Win32.UI.Shell.HLID_INFO = 0
HLID_PREVIOUS: win32more.Windows.Win32.UI.Shell.HLID_INFO = 4294967295
HLID_NEXT: win32more.Windows.Win32.UI.Shell.HLID_INFO = 4294967294
HLID_CURRENT: win32more.Windows.Win32.UI.Shell.HLID_INFO = 4294967293
HLID_STACKBOTTOM: win32more.Windows.Win32.UI.Shell.HLID_INFO = 4294967292
HLID_STACKTOP: win32more.Windows.Win32.UI.Shell.HLID_INFO = 4294967291
HLINKGETREF = Int32
HLINKGETREF_DEFAULT: win32more.Windows.Win32.UI.Shell.HLINKGETREF = 0
HLINKGETREF_ABSOLUTE: win32more.Windows.Win32.UI.Shell.HLINKGETREF = 1
HLINKGETREF_RELATIVE: win32more.Windows.Win32.UI.Shell.HLINKGETREF = 2
HLINKMISC = Int32
HLINKMISC_RELATIVE: win32more.Windows.Win32.UI.Shell.HLINKMISC = 1
HLINKSETF = Int32
HLINKSETF_TARGET: win32more.Windows.Win32.UI.Shell.HLINKSETF = 1
HLINKSETF_LOCATION: win32more.Windows.Win32.UI.Shell.HLINKSETF = 2
HLINKWHICHMK = Int32
HLINKWHICHMK_CONTAINER: win32more.Windows.Win32.UI.Shell.HLINKWHICHMK = 1
HLINKWHICHMK_BASE: win32more.Windows.Win32.UI.Shell.HLINKWHICHMK = 2
class HLITEM(Structure):
    uHLID: UInt32
    pwzFriendlyName: win32more.Windows.Win32.Foundation.PWSTR
HLNF = UInt32
HLNF_INTERNALJUMP: win32more.Windows.Win32.UI.Shell.HLNF = 1
HLNF_OPENINNEWWINDOW: win32more.Windows.Win32.UI.Shell.HLNF = 2
HLNF_NAVIGATINGBACK: win32more.Windows.Win32.UI.Shell.HLNF = 4
HLNF_NAVIGATINGFORWARD: win32more.Windows.Win32.UI.Shell.HLNF = 8
HLNF_NAVIGATINGTOSTACKITEM: win32more.Windows.Win32.UI.Shell.HLNF = 16
HLNF_CREATENOHISTORY: win32more.Windows.Win32.UI.Shell.HLNF = 32
HLQF_INFO = Int32
HLQF_ISVALID: win32more.Windows.Win32.UI.Shell.HLQF_INFO = 1
HLQF_ISCURRENT: win32more.Windows.Win32.UI.Shell.HLQF_INFO = 2
HLSHORTCUTF = Int32
HLSHORTCUTF_DEFAULT: win32more.Windows.Win32.UI.Shell.HLSHORTCUTF = 0
HLSHORTCUTF_DONTACTUALLYCREATE: win32more.Windows.Win32.UI.Shell.HLSHORTCUTF = 1
HLSHORTCUTF_USEFILENAMEFROMFRIENDLYNAME: win32more.Windows.Win32.UI.Shell.HLSHORTCUTF = 2
HLSHORTCUTF_USEUNIQUEFILENAME: win32more.Windows.Win32.UI.Shell.HLSHORTCUTF = 4
HLSHORTCUTF_MAYUSEEXISTINGSHORTCUT: win32more.Windows.Win32.UI.Shell.HLSHORTCUTF = 8
HLSR = Int32
HLSR_HOME: win32more.Windows.Win32.UI.Shell.HLSR = 0
HLSR_SEARCHPAGE: win32more.Windows.Win32.UI.Shell.HLSR = 1
HLSR_HISTORYFOLDER: win32more.Windows.Win32.UI.Shell.HLSR = 2
class HLTBINFO(Structure):
    uDockType: UInt32
    rcTbPos: win32more.Windows.Win32.Foundation.RECT
HLTB_INFO = Int32
HLTB_DOCKEDLEFT: win32more.Windows.Win32.UI.Shell.HLTB_INFO = 0
HLTB_DOCKEDTOP: win32more.Windows.Win32.UI.Shell.HLTB_INFO = 1
HLTB_DOCKEDRIGHT: win32more.Windows.Win32.UI.Shell.HLTB_INFO = 2
HLTB_DOCKEDBOTTOM: win32more.Windows.Win32.UI.Shell.HLTB_INFO = 3
HLTB_FLOATING: win32more.Windows.Win32.UI.Shell.HLTB_INFO = 4
HLTRANSLATEF = Int32
HLTRANSLATEF_DEFAULT: win32more.Windows.Win32.UI.Shell.HLTRANSLATEF = 0
HLTRANSLATEF_DONTAPPLYDEFAULTPREFIX: win32more.Windows.Win32.UI.Shell.HLTRANSLATEF = 1
HOMEGROUPSHARINGCHOICES = Int32
HGSC_NONE: win32more.Windows.Win32.UI.Shell.HOMEGROUPSHARINGCHOICES = 0
HGSC_MUSICLIBRARY: win32more.Windows.Win32.UI.Shell.HOMEGROUPSHARINGCHOICES = 1
HGSC_PICTURESLIBRARY: win32more.Windows.Win32.UI.Shell.HOMEGROUPSHARINGCHOICES = 2
HGSC_VIDEOSLIBRARY: win32more.Windows.Win32.UI.Shell.HOMEGROUPSHARINGCHOICES = 4
HGSC_DOCUMENTSLIBRARY: win32more.Windows.Win32.UI.Shell.HOMEGROUPSHARINGCHOICES = 8
HGSC_PRINTERS: win32more.Windows.Win32.UI.Shell.HOMEGROUPSHARINGCHOICES = 16
HPSXA = VoidPtr
HideInputPaneAnimationCoordinator = Guid('{384742b1-2a77-4cb3-8cf8-1136f5e17e59}')
HomeGroup = Guid('{de77ba04-3c92-4d11-a1a5-42352a53e0e3}')
class IACList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{77a130b0-94fd-11d0-a544-00c04fd7d062}')
    @commethod(3)
    def Expand(self, pszExpand: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IACList2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IACList
    _iid_ = Guid('{470141a0-5186-11d2-bbb6-0060977b464c}')
    @commethod(4)
    def SetOptions(self, dwFlag: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetOptions(self, pdwFlag: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAccessibilityDockingService(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8849dc22-cedf-4c95-998d-051419dd3f76}')
    @commethod(3)
    def GetAvailableSize(self, hMonitor: win32more.Windows.Win32.Graphics.Gdi.HMONITOR, pcxFixed: POINTER(UInt32), pcyMax: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DockWindow(self, hwnd: win32more.Windows.Win32.Foundation.HWND, hMonitor: win32more.Windows.Win32.Graphics.Gdi.HMONITOR, cyRequested: UInt32, pCallback: win32more.Windows.Win32.UI.Shell.IAccessibilityDockingServiceCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def UndockWindow(self, hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAccessibilityDockingServiceCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{157733fd-a592-42e5-b594-248468c5a81b}')
    @commethod(3)
    def Undocked(self, undockReason: win32more.Windows.Win32.UI.Shell.UNDOCK_REASON) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAccessibleObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{95a391c5-9ed4-4c28-8401-ab9e06719e11}')
    @commethod(3)
    def SetAccessibleName(self, pszName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActionProgress(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{49ff1173-eadc-446d-9285-156453a6431c}')
    @commethod(3)
    def Begin(self, action: win32more.Windows.Win32.UI.Shell.SPACTION, flags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UpdateProgress(self, ulCompleted: UInt64, ulTotal: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def UpdateText(self, sptext: win32more.Windows.Win32.UI.Shell.SPTEXT, pszText: win32more.Windows.Win32.Foundation.PWSTR, fMayCompact: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def QueryCancel(self, pfCancelled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ResetCancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def End(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActionProgressDialog(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{49ff1172-eadc-446d-9285-156453a6431c}')
    @commethod(3)
    def Initialize(self, flags: UInt32, pszTitle: win32more.Windows.Win32.Foundation.PWSTR, pszCancel: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Stop(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppActivationUIInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{abad189d-9fa3-4278-b3ca-8ca448a88dcb}')
    @commethod(3)
    def GetMonitor(self, value: POINTER(win32more.Windows.Win32.Graphics.Gdi.HMONITOR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInvokePoint(self, value: POINTER(win32more.Windows.Win32.Foundation.POINT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetShowCommand(self, value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetShowUI(self, value: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetKeyState(self, value: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppPublisher(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{07250a10-9cf9-11d1-9076-006008059382}')
    @commethod(3)
    def GetNumberOfCategories(self, pdwCat: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCategories(self, pAppCategoryList: POINTER(win32more.Windows.Win32.UI.Shell.APPCATEGORYINFOLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetNumberOfApps(self, pdwApps: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnumApps(self, pAppCategoryId: POINTER(Guid), ppepa: POINTER(win32more.Windows.Win32.UI.Shell.IEnumPublishedApps)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppVisibility(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2246ea2d-caea-4444-a3c4-6de827e44313}')
    @commethod(3)
    def GetAppVisibilityOnMonitor(self, hMonitor: win32more.Windows.Win32.Graphics.Gdi.HMONITOR, pMode: POINTER(win32more.Windows.Win32.UI.Shell.MONITOR_APP_VISIBILITY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsLauncherVisible(self, pfVisible: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Advise(self, pCallback: win32more.Windows.Win32.UI.Shell.IAppVisibilityEvents, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Unadvise(self, dwCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAppVisibilityEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6584ce6b-7d82-49c2-89c9-c6bc02ba8c38}')
    @commethod(3)
    def AppVisibilityOnMonitorChanged(self, hMonitor: win32more.Windows.Win32.Graphics.Gdi.HMONITOR, previousMode: win32more.Windows.Win32.UI.Shell.MONITOR_APP_VISIBILITY, currentMode: win32more.Windows.Win32.UI.Shell.MONITOR_APP_VISIBILITY) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LauncherVisibilityChange(self, currentVisibleState: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IApplicationActivationManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2e941141-7f97-4756-ba1d-9decde894a3d}')
    @commethod(3)
    def ActivateApplication(self, appUserModelId: win32more.Windows.Win32.Foundation.PWSTR, arguments: win32more.Windows.Win32.Foundation.PWSTR, options: win32more.Windows.Win32.UI.Shell.ACTIVATEOPTIONS, processId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ActivateForFile(self, appUserModelId: win32more.Windows.Win32.Foundation.PWSTR, itemArray: win32more.Windows.Win32.UI.Shell.IShellItemArray, verb: win32more.Windows.Win32.Foundation.PWSTR, processId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ActivateForProtocol(self, appUserModelId: win32more.Windows.Win32.Foundation.PWSTR, itemArray: win32more.Windows.Win32.UI.Shell.IShellItemArray, processId: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IApplicationAssociationRegistration(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4e530b0a-e611-4c77-a3ac-9031d022281b}')
    @commethod(3)
    def QueryCurrentDefault(self, pszQuery: win32more.Windows.Win32.Foundation.PWSTR, atQueryType: win32more.Windows.Win32.UI.Shell.ASSOCIATIONTYPE, alQueryLevel: win32more.Windows.Win32.UI.Shell.ASSOCIATIONLEVEL, ppszAssociation: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def QueryAppIsDefault(self, pszQuery: win32more.Windows.Win32.Foundation.PWSTR, atQueryType: win32more.Windows.Win32.UI.Shell.ASSOCIATIONTYPE, alQueryLevel: win32more.Windows.Win32.UI.Shell.ASSOCIATIONLEVEL, pszAppRegistryName: win32more.Windows.Win32.Foundation.PWSTR, pfDefault: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def QueryAppIsDefaultAll(self, alQueryLevel: win32more.Windows.Win32.UI.Shell.ASSOCIATIONLEVEL, pszAppRegistryName: win32more.Windows.Win32.Foundation.PWSTR, pfDefault: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetAppAsDefault(self, pszAppRegistryName: win32more.Windows.Win32.Foundation.PWSTR, pszSet: win32more.Windows.Win32.Foundation.PWSTR, atSetType: win32more.Windows.Win32.UI.Shell.ASSOCIATIONTYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetAppAsDefaultAll(self, pszAppRegistryName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ClearUserAssociations(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IApplicationAssociationRegistrationUI(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1f76a169-f994-40ac-8fc8-0959e8874710}')
    @commethod(3)
    def LaunchAdvancedAssociationUI(self, pszAppRegistryName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IApplicationDesignModeSettings(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2a3dee9a-e31d-46d6-8508-bcc597db3557}')
    @commethod(3)
    def SetNativeDisplaySize(self, nativeDisplaySizePixels: win32more.Windows.Win32.Foundation.SIZE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetScaleFactor(self, scaleFactor: win32more.Windows.Win32.UI.Shell.Common.DEVICE_SCALE_FACTOR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetApplicationViewState(self, viewState: win32more.Windows.Win32.UI.Shell.APPLICATION_VIEW_STATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ComputeApplicationSize(self, applicationSizePixels: POINTER(win32more.Windows.Win32.Foundation.SIZE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsApplicationViewStateSupported(self, viewState: win32more.Windows.Win32.UI.Shell.APPLICATION_VIEW_STATE, nativeDisplaySizePixels: win32more.Windows.Win32.Foundation.SIZE, scaleFactor: win32more.Windows.Win32.UI.Shell.Common.DEVICE_SCALE_FACTOR, supported: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def TriggerEdgeGesture(self, edgeGestureKind: win32more.Windows.Win32.UI.Shell.EDGE_GESTURE_KIND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IApplicationDesignModeSettings2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IApplicationDesignModeSettings
    _iid_ = Guid('{490514e1-675a-4d6e-a58d-e54901b4ca2f}')
    @commethod(9)
    def SetNativeDisplayOrientation(self, nativeDisplayOrientation: win32more.Windows.Win32.UI.Shell.NATIVE_DISPLAY_ORIENTATION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetApplicationViewOrientation(self, viewOrientation: win32more.Windows.Win32.UI.Shell.APPLICATION_VIEW_ORIENTATION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetAdjacentDisplayEdges(self, adjacentDisplayEdges: win32more.Windows.Win32.UI.Shell.ADJACENT_DISPLAY_EDGES) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetIsOnLockScreen(self, isOnLockScreen: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetApplicationViewMinWidth(self, viewMinWidth: win32more.Windows.Win32.UI.Shell.APPLICATION_VIEW_MIN_WIDTH) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetApplicationSizeBounds(self, minApplicationSizePixels: POINTER(win32more.Windows.Win32.Foundation.SIZE), maxApplicationSizePixels: POINTER(win32more.Windows.Win32.Foundation.SIZE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetApplicationViewOrientation(self, applicationSizePixels: win32more.Windows.Win32.Foundation.SIZE, viewOrientation: POINTER(win32more.Windows.Win32.UI.Shell.APPLICATION_VIEW_ORIENTATION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IApplicationDestinations(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{12337d35-94c6-48a0-bce7-6a9c69d4d600}')
    @commethod(3)
    def SetAppID(self, pszAppID: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveDestination(self, punk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveAllDestinations(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IApplicationDocumentLists(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3c594f9f-9f30-47a1-979a-c9e83d3d0a06}')
    @commethod(3)
    def SetAppID(self, pszAppID: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetList(self, listtype: win32more.Windows.Win32.UI.Shell.APPDOCLISTTYPE, cItemsDesired: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAssocHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f04061ac-1659-4a3f-a954-775aa57fc083}')
    @commethod(3)
    def GetName(self, ppsz: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetUIName(self, ppsz: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetIconLocation(self, ppszPath: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pIndex: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def IsRecommended(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def MakeDefault(self, pszDescription: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Invoke(self, pdo: win32more.Windows.Win32.System.Com.IDataObject) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CreateInvoker(self, pdo: win32more.Windows.Win32.System.Com.IDataObject, ppInvoker: POINTER(win32more.Windows.Win32.UI.Shell.IAssocHandlerInvoker)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAssocHandlerInvoker(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{92218cab-ecaa-4335-8133-807fd234c2ee}')
    @commethod(3)
    def SupportsSelection(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Invoke(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAttachmentExecute(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{73db1241-1e85-4581-8e4f-a81e1d0f8c57}')
    @commethod(3)
    def SetClientTitle(self, pszTitle: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetClientGuid(self, guid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetLocalPath(self, pszLocalPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetFileName(self, pszFileName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetSource(self, pszSource: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetReferrer(self, pszReferrer: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CheckPolicy(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Prompt(self, hwnd: win32more.Windows.Win32.Foundation.HWND, prompt: win32more.Windows.Win32.UI.Shell.ATTACHMENT_PROMPT, paction: POINTER(win32more.Windows.Win32.UI.Shell.ATTACHMENT_ACTION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Save(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Execute(self, hwnd: win32more.Windows.Win32.Foundation.HWND, pszVerb: win32more.Windows.Win32.Foundation.PWSTR, phProcess: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SaveWithUI(self, hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def ClearClientState(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAutoComplete(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00bb2762-6a77-11d0-a535-00c04fd7d062}')
    @commethod(3)
    def Init(self, hwndEdit: win32more.Windows.Win32.Foundation.HWND, punkACL: win32more.Windows.Win32.System.Com.IUnknown, pwszRegKeyPath: win32more.Windows.Win32.Foundation.PWSTR, pwszQuickComplete: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Enable(self, fEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAutoComplete2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IAutoComplete
    _iid_ = Guid('{eac04bc0-3791-11d2-bb95-0060977b464c}')
    @commethod(5)
    def SetOptions(self, dwFlag: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetOptions(self, pdwFlag: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAutoCompleteDropDown(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3cd141f4-3c6a-11d2-bcaa-00c04fd929db}')
    @commethod(3)
    def GetDropDownStatus(self, pdwFlags: POINTER(UInt32), ppwszString: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ResetEnumerator(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBandHost(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b9075c7c-d48e-403f-ab99-d6c77a1084ac}')
    @commethod(3)
    def CreateBand(self, rclsidBand: POINTER(Guid), fAvailable: win32more.Windows.Win32.Foundation.BOOL, fVisible: win32more.Windows.Win32.Foundation.BOOL, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetBandAvailability(self, rclsidBand: POINTER(Guid), fAvailable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DestroyBand(self, rclsidBand: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBandSite(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4cf504b0-de96-11d0-8b3f-00a0c911e8e5}')
    @commethod(3)
    def AddBand(self, punk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnumBands(self, uBand: UInt32, pdwBandID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def QueryBand(self, dwBandID: UInt32, ppstb: POINTER(win32more.Windows.Win32.UI.Shell.IDeskBand), pdwState: POINTER(UInt32), pszName: win32more.Windows.Win32.Foundation.PWSTR, cchName: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetBandState(self, dwBandID: UInt32, dwMask: UInt32, dwState: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveBand(self, dwBandID: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetBandObject(self, dwBandID: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetBandSiteInfo(self, pbsinfo: POINTER(win32more.Windows.Win32.UI.Shell.BANDSITEINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetBandSiteInfo(self, pbsinfo: POINTER(win32more.Windows.Win32.UI.Shell.BANDSITEINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBannerNotificationHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8d7b2ba7-db05-46a8-823c-d2b6de08ee91}')
    @commethod(3)
    def OnBannerEvent(self, notification: POINTER(win32more.Windows.Win32.UI.Shell.BANNER_NOTIFICATION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBanneredBar(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{596a9a94-013e-11d1-8d34-00a0c90f2719}')
    @commethod(3)
    def SetIconSize(self, iIcon: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetIconSize(self, piIcon: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetBitmap(self, hBitmap: win32more.Windows.Win32.Graphics.Gdi.HBITMAP) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetBitmap(self, phBitmap: POINTER(win32more.Windows.Win32.Graphics.Gdi.HBITMAP)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBrowserFrameOptions(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{10df43c8-1dbe-11d3-8b34-006097df5bd4}')
    @commethod(3)
    def GetFrameOptions(self, dwMask: UInt32, pdwOptions: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBrowserService(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{02ba3b52-0547-11d1-b833-00c04fc9b31f}')
    @commethod(3)
    def GetParentSite(self, ppipsite: POINTER(win32more.Windows.Win32.System.Ole.IOleInPlaceSite)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetTitle(self, psv: win32more.Windows.Win32.UI.Shell.IShellView, pszName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTitle(self, psv: win32more.Windows.Win32.UI.Shell.IShellView, pszName: win32more.Windows.Win32.Foundation.PWSTR, cchName: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetOleObject(self, ppobjv: POINTER(win32more.Windows.Win32.System.Ole.IOleObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTravelLog(self, pptl: POINTER(win32more.Windows.Win32.UI.Shell.ITravelLog)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ShowControlWindow(self, id: UInt32, fShow: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def IsControlWindowShown(self, id: UInt32, pfShown: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IEGetDisplayName(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pwszName: win32more.Windows.Win32.Foundation.PWSTR, uFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def IEParseDisplayName(self, uiCP: UInt32, pwszPath: win32more.Windows.Win32.Foundation.PWSTR, ppidlOut: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def DisplayParseError(self, hres: win32more.Windows.Win32.Foundation.HRESULT, pwszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def NavigateToPidl(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), grfHLNF: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetNavigateState(self, bnstate: win32more.Windows.Win32.UI.Shell.BNSTATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetNavigateState(self, pbnstate: POINTER(win32more.Windows.Win32.UI.Shell.BNSTATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def NotifyRedirect(self, psv: win32more.Windows.Win32.UI.Shell.IShellView, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pfDidBrowse: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def UpdateWindowList(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def UpdateBackForwardState(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetFlags(self, dwFlags: UInt32, dwFlagMask: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetFlags(self, pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def CanNavigateNow(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetPidl(self, ppidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetReferrer(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetBrowserIndex(self) -> UInt32: ...
    @commethod(25)
    def GetBrowserByIndex(self, dwID: UInt32, ppunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetHistoryObject(self, ppole: POINTER(win32more.Windows.Win32.System.Ole.IOleObject), pstm: POINTER(win32more.Windows.Win32.System.Com.IStream), ppbc: POINTER(win32more.Windows.Win32.System.Com.IBindCtx)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetHistoryObject(self, pole: win32more.Windows.Win32.System.Ole.IOleObject, fIsLocalAnchor: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def CacheOLEServer(self, pole: win32more.Windows.Win32.System.Ole.IOleObject) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetSetCodePage(self, pvarIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarOut: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def OnHttpEquiv(self, psv: win32more.Windows.Win32.UI.Shell.IShellView, fDone: win32more.Windows.Win32.Foundation.BOOL, pvarargIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarargOut: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetPalette(self, hpal: POINTER(win32more.Windows.Win32.Graphics.Gdi.HPALETTE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def RegisterWindow(self, fForceRegister: win32more.Windows.Win32.Foundation.BOOL, swc: win32more.Windows.Win32.UI.Shell.ShellWindowTypeConstants) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBrowserService2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IBrowserService
    _iid_ = Guid('{68bd21cc-438b-11d2-a560-00a0c92dbfe8}')
    @commethod(33)
    def WndProcBS(self, hwnd: win32more.Windows.Win32.Foundation.HWND, uMsg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.LRESULT: ...
    @commethod(34)
    def SetAsDefFolderSettings(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetViewRect(self, prc: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def OnSize(self, wParam: win32more.Windows.Win32.Foundation.WPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def OnCreate(self, pcs: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.CREATESTRUCTW)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def OnCommand(self, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.LRESULT: ...
    @commethod(39)
    def OnDestroy(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def OnNotify(self, pnm: POINTER(win32more.Windows.Win32.UI.Controls.NMHDR)) -> win32more.Windows.Win32.Foundation.LRESULT: ...
    @commethod(41)
    def OnSetFocus(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def OnFrameWindowActivateBS(self, fActive: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def ReleaseShellView(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def ActivatePendingView(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def CreateViewWindow(self, psvNew: win32more.Windows.Win32.UI.Shell.IShellView, psvOld: win32more.Windows.Win32.UI.Shell.IShellView, prcView: POINTER(win32more.Windows.Win32.Foundation.RECT), phwnd: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def CreateBrowserPropSheetExt(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def GetViewWindow(self, phwndView: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def GetBaseBrowserData(self, pbbd: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.BASEBROWSERDATALH))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def PutBaseBrowserData(self) -> POINTER(win32more.Windows.Win32.UI.Shell.BASEBROWSERDATALH): ...
    @commethod(50)
    def InitializeTravelLog(self, ptl: win32more.Windows.Win32.UI.Shell.ITravelLog, dw: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def SetTopBrowser(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def Offline(self, iCmd: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def AllowViewResize(self, f: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def SetActivateState(self, u: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def UpdateSecureLockIcon(self, eSecureLock: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def InitializeDownloadManager(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def InitializeTransitionSite(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def _Initialize(self, hwnd: win32more.Windows.Win32.Foundation.HWND, pauto: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def _CancelPendingNavigationAsync(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def _CancelPendingView(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def _MaySaveChanges(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def _PauseOrResumeView(self, fPaused: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def _DisableModeless(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def _NavigateToPidl2(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), grfHLNF: UInt32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def _TryShell2Rename(self, psv: win32more.Windows.Win32.UI.Shell.IShellView, pidlNew: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def _SwitchActivationNow(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(67)
    def _ExecChildren(self, punkBar: win32more.Windows.Win32.System.Com.IUnknown, fBroadcast: win32more.Windows.Win32.Foundation.BOOL, pguidCmdGroup: POINTER(Guid), nCmdID: UInt32, nCmdexecopt: UInt32, pvarargIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarargOut: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(68)
    def _SendChildren(self, hwndBar: win32more.Windows.Win32.Foundation.HWND, fBroadcast: win32more.Windows.Win32.Foundation.BOOL, uMsg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def GetFolderSetData(self, pfsd: POINTER(win32more.Windows.Win32.UI.Shell.FOLDERSETDATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(70)
    def _OnFocusChange(self, itb: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(71)
    def v_ShowHideChildWindows(self, fChildOnly: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(72)
    def _get_itbLastFocus(self) -> UInt32: ...
    @commethod(73)
    def _put_itbLastFocus(self, itbLastFocus: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(74)
    def _UIActivateView(self, uState: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(75)
    def _GetViewBorderRect(self, prc: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(76)
    def _UpdateViewRectSize(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(77)
    def _ResizeNextBorder(self, itb: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(78)
    def _ResizeView(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(79)
    def _GetEffectiveClientArea(self, lprectBorder: POINTER(win32more.Windows.Win32.Foundation.RECT), hmon: win32more.Windows.Win32.Graphics.Gdi.HMONITOR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(80)
    def v_GetViewStream(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), grfMode: UInt32, pwszName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.System.Com.IStream: ...
    @commethod(81)
    def ForwardViewMsg(self, uMsg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.LRESULT: ...
    @commethod(82)
    def SetAcceleratorMenu(self, hacc: win32more.Windows.Win32.UI.WindowsAndMessaging.HACCEL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(83)
    def _GetToolbarCount(self) -> Int32: ...
    @commethod(84)
    def _GetToolbarItem(self, itb: Int32) -> POINTER(win32more.Windows.Win32.UI.Shell.TOOLBARITEM): ...
    @commethod(85)
    def _SaveToolbars(self, pstm: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(86)
    def _LoadToolbars(self, pstm: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(87)
    def _CloseAndReleaseToolbars(self, fClose: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(88)
    def v_MayGetNextToolbarFocus(self, lpMsg: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.MSG), itbNext: UInt32, citb: Int32, pptbi: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.TOOLBARITEM)), phwnd: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(89)
    def _ResizeNextBorderHelper(self, itb: UInt32, bUseHmonitor: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(90)
    def _FindTBar(self, punkSrc: win32more.Windows.Win32.System.Com.IUnknown) -> UInt32: ...
    @commethod(91)
    def _SetFocus(self, ptbi: POINTER(win32more.Windows.Win32.UI.Shell.TOOLBARITEM), hwnd: win32more.Windows.Win32.Foundation.HWND, lpMsg: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.MSG)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(92)
    def v_MayTranslateAccelerator(self, pmsg: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.MSG)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(93)
    def _GetBorderDWHelper(self, punkSrc: win32more.Windows.Win32.System.Com.IUnknown, lprectBorder: POINTER(win32more.Windows.Win32.Foundation.RECT), bUseHmonitor: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(94)
    def v_CheckZoneCrossing(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBrowserService3(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IBrowserService2
    _iid_ = Guid('{27d7ce21-762d-48f3-86f3-40e2fd3749c4}')
    @commethod(95)
    def _PositionViewWindow(self, hwnd: win32more.Windows.Win32.Foundation.HWND, prc: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(96)
    def IEParseDisplayNameEx(self, uiCP: UInt32, pwszPath: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, ppidlOut: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBrowserService4(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IBrowserService3
    _iid_ = Guid('{639f1bff-e135-4096-abd8-e0f504d649a4}')
    @commethod(97)
    def ActivateView(self, fPendingView: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(98)
    def SaveViewState(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(99)
    def _ResizeAllBorders(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICDBurn(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3d73a659-e5d0-4d42-afc0-5121ba425c8d}')
    @commethod(3)
    def GetRecorderDriveLetter(self, pszDrive: win32more.Windows.Win32.Foundation.PWSTR, cch: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Burn(self, hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def HasRecordableDrive(self, pfHasRecorder: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICDBurnExt(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2271dcca-74fc-4414-8fb7-c56b05ace2d7}')
    @commethod(3)
    def GetSupportedActionTypes(self, pdwActions: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICategorizer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a3b14589-9174-49a8-89a3-06a1ae2b9ba7}')
    @commethod(3)
    def GetDescription(self, pszDesc: win32more.Windows.Win32.Foundation.PWSTR, cch: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCategory(self, cidl: UInt32, apidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)), rgCategoryIds: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCategoryInfo(self, dwCategoryId: UInt32, pci: POINTER(win32more.Windows.Win32.UI.Shell.CATEGORY_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CompareCategory(self, csfFlags: win32more.Windows.Win32.UI.Shell.CATSORT_FLAGS, dwCategoryId1: UInt32, dwCategoryId2: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICategoryProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9af64809-5864-4c26-a720-c1f78c086ee3}')
    @commethod(3)
    def CanCategorizeOnSCID(self, pscid: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDefaultCategory(self, pguid: POINTER(Guid), pscid: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCategoryForSCID(self, pscid: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pguid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnumCategories(self, penum: POINTER(win32more.Windows.Win32.System.Com.IEnumGUID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCategoryName(self, pguid: POINTER(Guid), pszName: win32more.Windows.Win32.Foundation.PWSTR, cch: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreateCategory(self, pguid: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IColumnManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d8ec27bb-3f3b-4042-b10a-4acfd924d453}')
    @commethod(3)
    def SetColumnInfo(self, propkey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pcmci: POINTER(win32more.Windows.Win32.UI.Shell.CM_COLUMNINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetColumnInfo(self, propkey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pcmci: POINTER(win32more.Windows.Win32.UI.Shell.CM_COLUMNINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetColumnCount(self, dwFlags: win32more.Windows.Win32.UI.Shell.CM_ENUM_FLAGS, puCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetColumns(self, dwFlags: win32more.Windows.Win32.UI.Shell.CM_ENUM_FLAGS, rgkeyOrder: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), cColumns: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetColumns(self, rgkeyOrder: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), cVisible: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IColumnProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e8025004-1c42-11d2-be2c-00a0c9a83da1}')
    @commethod(3)
    def Initialize(self, psci: POINTER(win32more.Windows.Win32.UI.Shell.SHCOLUMNINIT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetColumnInfo(self, dwIndex: UInt32, psci: POINTER(win32more.Windows.Win32.UI.Shell.SHCOLUMNINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetItemData(self, pscid: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pscd: POINTER(win32more.Windows.Win32.UI.Shell.SHCOLUMNDATA), pvarData: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICommDlgBrowser(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{000214f1-0000-0000-c000-000000000046}')
    @commethod(3)
    def OnDefaultCommand(self, ppshv: win32more.Windows.Win32.UI.Shell.IShellView) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnStateChange(self, ppshv: win32more.Windows.Win32.UI.Shell.IShellView, uChange: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IncludeObject(self, ppshv: win32more.Windows.Win32.UI.Shell.IShellView, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICommDlgBrowser2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.ICommDlgBrowser
    _iid_ = Guid('{10339516-2894-11d2-9039-00c04f8eeb3e}')
    @commethod(6)
    def Notify(self, ppshv: win32more.Windows.Win32.UI.Shell.IShellView, dwNotifyType: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetDefaultMenuText(self, ppshv: win32more.Windows.Win32.UI.Shell.IShellView, pszText: win32more.Windows.Win32.Foundation.PWSTR, cchMax: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetViewFlags(self, pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICommDlgBrowser3(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.ICommDlgBrowser2
    _iid_ = Guid('{c8ad25a1-3294-41ee-8165-71174bd01c57}')
    @commethod(9)
    def OnColumnClicked(self, ppshv: win32more.Windows.Win32.UI.Shell.IShellView, iColumn: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetCurrentFilter(self, pszFileSpec: win32more.Windows.Win32.Foundation.PWSTR, cchFileSpec: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def OnPreViewCreated(self, ppshv: win32more.Windows.Win32.UI.Shell.IShellView) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IComputerInfoChangeNotify(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0df60d92-6818-46d6-b358-d66170dde466}')
    @commethod(3)
    def ComputerInfoChanged(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IConnectableCredentialProviderCredential(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.ICredentialProviderCredential
    _iid_ = Guid('{9387928b-ac75-4bf9-8ab2-2b93c4a55290}')
    @commethod(20)
    def Connect(self, pqcws: win32more.Windows.Win32.UI.Shell.IQueryContinueWithStatus) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Disconnect(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IContactManagerInterop(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{99eacba7-e073-43b6-a896-55afe48a0833}')
    @commethod(3)
    def ShowContactCardForWindow(self, appWindow: win32more.Windows.Win32.Foundation.HWND, contact: win32more.Windows.Win32.System.Com.IUnknown, selection: POINTER(win32more.Windows.Win32.Foundation.RECT), preferredPlacement: win32more.Windows.Win32.UI.Shell.FLYOUT_PLACEMENT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IContextMenu(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{000214e4-0000-0000-c000-000000000046}')
    @commethod(3)
    def QueryContextMenu(self, hmenu: win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU, indexMenu: UInt32, idCmdFirst: UInt32, idCmdLast: UInt32, uFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def InvokeCommand(self, pici: POINTER(win32more.Windows.Win32.UI.Shell.CMINVOKECOMMANDINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCommandString(self, idCmd: UIntPtr, uType: UInt32, pReserved: POINTER(UInt32), pszName: win32more.Windows.Win32.Foundation.PSTR, cchMax: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IContextMenu2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IContextMenu
    _iid_ = Guid('{000214f4-0000-0000-c000-000000000046}')
    @commethod(6)
    def HandleMenuMsg(self, uMsg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IContextMenu3(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IContextMenu2
    _iid_ = Guid('{bcfce0a0-ec17-11d0-8d10-00a0c90f2719}')
    @commethod(7)
    def HandleMenuMsg2(self, uMsg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM, plResult: POINTER(win32more.Windows.Win32.Foundation.LRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IContextMenuCB(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3409e930-5a39-11d1-83fa-00a0c90dc849}')
    @commethod(3)
    def CallBack(self, psf: win32more.Windows.Win32.UI.Shell.IShellFolder, hwndOwner: win32more.Windows.Win32.Foundation.HWND, pdtobj: win32more.Windows.Win32.System.Com.IDataObject, uMsg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IContextMenuSite(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0811aebe-0b87-4c54-9e72-548cf649016b}')
    @commethod(3)
    def DoContextMenuPopup(self, punkContextMenu: win32more.Windows.Win32.System.Com.IUnknown, fFlags: UInt32, pt: win32more.Windows.Win32.Foundation.POINT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICopyHookA(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{000214ef-0000-0000-c000-000000000046}')
    @commethod(3)
    def CopyCallback(self, hwnd: win32more.Windows.Win32.Foundation.HWND, wFunc: UInt32, wFlags: UInt32, pszSrcFile: win32more.Windows.Win32.Foundation.PSTR, dwSrcAttribs: UInt32, pszDestFile: win32more.Windows.Win32.Foundation.PSTR, dwDestAttribs: UInt32) -> UInt32: ...
class ICopyHookW(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{000214fc-0000-0000-c000-000000000046}')
    @commethod(3)
    def CopyCallback(self, hwnd: win32more.Windows.Win32.Foundation.HWND, wFunc: UInt32, wFlags: UInt32, pszSrcFile: win32more.Windows.Win32.Foundation.PWSTR, dwSrcAttribs: UInt32, pszDestFile: win32more.Windows.Win32.Foundation.PWSTR, dwDestAttribs: UInt32) -> UInt32: ...
ICopyHook = UnicodeAlias('ICopyHookW')
class ICreateProcessInputs(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f6ef6140-e26f-4d82-bac4-e9ba5fd239a8}')
    @commethod(3)
    def GetCreateFlags(self, pdwCreationFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetCreateFlags(self, dwCreationFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddCreateFlags(self, dwCreationFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetHotKey(self, wHotKey: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddStartupFlags(self, dwStartupInfoFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetTitle(self, pszTitle: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetEnvironmentVariable(self, pszName: win32more.Windows.Win32.Foundation.PWSTR, pszValue: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICreatingProcess(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c2b937a9-3110-4398-8a56-f34c6342d244}')
    @commethod(3)
    def OnCreating(self, pcpi: win32more.Windows.Win32.UI.Shell.ICreateProcessInputs) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICredentialProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d27c3481-5a1c-45b2-8aaa-c20ebbe8229e}')
    @commethod(3)
    def SetUsageScenario(self, cpus: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_USAGE_SCENARIO, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetSerialization(self, pcpcs: POINTER(win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_CREDENTIAL_SERIALIZATION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Advise(self, pcpe: win32more.Windows.Win32.UI.Shell.ICredentialProviderEvents, upAdviseContext: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def UnAdvise(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFieldDescriptorCount(self, pdwCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetFieldDescriptorAt(self, dwIndex: UInt32, ppcpfd: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_FIELD_DESCRIPTOR))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCredentialCount(self, pdwCount: POINTER(UInt32), pdwDefault: POINTER(UInt32), pbAutoLogonWithDefault: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetCredentialAt(self, dwIndex: UInt32, ppcpc: POINTER(win32more.Windows.Win32.UI.Shell.ICredentialProviderCredential)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICredentialProviderCredential(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{63913a93-40c1-481a-818d-4072ff8c70cc}')
    @commethod(3)
    def Advise(self, pcpce: win32more.Windows.Win32.UI.Shell.ICredentialProviderCredentialEvents) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnAdvise(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetSelected(self, pbAutoLogon: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetDeselected(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFieldState(self, dwFieldID: UInt32, pcpfs: POINTER(win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_FIELD_STATE), pcpfis: POINTER(win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_FIELD_INTERACTIVE_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetStringValue(self, dwFieldID: UInt32, ppsz: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetBitmapValue(self, dwFieldID: UInt32, phbmp: POINTER(win32more.Windows.Win32.Graphics.Gdi.HBITMAP)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetCheckboxValue(self, dwFieldID: UInt32, pbChecked: POINTER(win32more.Windows.Win32.Foundation.BOOL), ppszLabel: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetSubmitButtonValue(self, dwFieldID: UInt32, pdwAdjacentTo: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetComboBoxValueCount(self, dwFieldID: UInt32, pcItems: POINTER(UInt32), pdwSelectedItem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetComboBoxValueAt(self, dwFieldID: UInt32, dwItem: UInt32, ppszItem: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetStringValue(self, dwFieldID: UInt32, psz: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetCheckboxValue(self, dwFieldID: UInt32, bChecked: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetComboBoxSelectedValue(self, dwFieldID: UInt32, dwSelectedItem: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def CommandLinkClicked(self, dwFieldID: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetSerialization(self, pcpgsr: POINTER(win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_GET_SERIALIZATION_RESPONSE), pcpcs: POINTER(win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_CREDENTIAL_SERIALIZATION), ppszOptionalStatusText: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pcpsiOptionalStatusIcon: POINTER(win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_STATUS_ICON)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def ReportResult(self, ntsStatus: win32more.Windows.Win32.Foundation.NTSTATUS, ntsSubstatus: win32more.Windows.Win32.Foundation.NTSTATUS, ppszOptionalStatusText: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pcpsiOptionalStatusIcon: POINTER(win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_STATUS_ICON)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICredentialProviderCredential2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.ICredentialProviderCredential
    _iid_ = Guid('{fd672c54-40ea-4d6e-9b49-cfb1a7507bd7}')
    @commethod(20)
    def GetUserSid(self, sid: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICredentialProviderCredentialEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fa6fa76b-66b7-4b11-95f1-86171118e816}')
    @commethod(3)
    def SetFieldState(self, pcpc: win32more.Windows.Win32.UI.Shell.ICredentialProviderCredential, dwFieldID: UInt32, cpfs: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_FIELD_STATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetFieldInteractiveState(self, pcpc: win32more.Windows.Win32.UI.Shell.ICredentialProviderCredential, dwFieldID: UInt32, cpfis: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_FIELD_INTERACTIVE_STATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetFieldString(self, pcpc: win32more.Windows.Win32.UI.Shell.ICredentialProviderCredential, dwFieldID: UInt32, psz: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetFieldCheckbox(self, pcpc: win32more.Windows.Win32.UI.Shell.ICredentialProviderCredential, dwFieldID: UInt32, bChecked: win32more.Windows.Win32.Foundation.BOOL, pszLabel: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetFieldBitmap(self, pcpc: win32more.Windows.Win32.UI.Shell.ICredentialProviderCredential, dwFieldID: UInt32, hbmp: win32more.Windows.Win32.Graphics.Gdi.HBITMAP) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetFieldComboBoxSelectedItem(self, pcpc: win32more.Windows.Win32.UI.Shell.ICredentialProviderCredential, dwFieldID: UInt32, dwSelectedItem: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def DeleteFieldComboBoxItem(self, pcpc: win32more.Windows.Win32.UI.Shell.ICredentialProviderCredential, dwFieldID: UInt32, dwItem: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def AppendFieldComboBoxItem(self, pcpc: win32more.Windows.Win32.UI.Shell.ICredentialProviderCredential, dwFieldID: UInt32, pszItem: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetFieldSubmitButton(self, pcpc: win32more.Windows.Win32.UI.Shell.ICredentialProviderCredential, dwFieldID: UInt32, dwAdjacentTo: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def OnCreatingWindow(self, phwndOwner: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICredentialProviderCredentialEvents2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.ICredentialProviderCredentialEvents
    _iid_ = Guid('{b53c00b6-9922-4b78-b1f4-ddfe774dc39b}')
    @commethod(13)
    def BeginFieldUpdates(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def EndFieldUpdates(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetFieldOptions(self, credential: win32more.Windows.Win32.UI.Shell.ICredentialProviderCredential, fieldID: UInt32, options: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_CREDENTIAL_FIELD_OPTIONS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICredentialProviderCredentialWithFieldOptions(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dbc6fb30-c843-49e3-a645-573e6f39446a}')
    @commethod(3)
    def GetFieldOptions(self, fieldID: UInt32, options: POINTER(win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_CREDENTIAL_FIELD_OPTIONS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICredentialProviderEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{34201e5a-a787-41a3-a5a4-bd6dcf2a854e}')
    @commethod(3)
    def CredentialsChanged(self, upAdviseContext: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICredentialProviderFilter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a5da53f9-d475-4080-a120-910c4a739880}')
    @commethod(3)
    def Filter(self, cpus: win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_USAGE_SCENARIO, dwFlags: UInt32, rgclsidProviders: POINTER(Guid), rgbAllow: POINTER(win32more.Windows.Win32.Foundation.BOOL), cProviders: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UpdateRemoteCredential(self, pcpcsIn: POINTER(win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_CREDENTIAL_SERIALIZATION), pcpcsOut: POINTER(win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_CREDENTIAL_SERIALIZATION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICredentialProviderSetUserArray(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{095c1484-1c0c-4388-9c6d-500e61bf84bd}')
    @commethod(3)
    def SetUserArray(self, users: win32more.Windows.Win32.UI.Shell.ICredentialProviderUserArray) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICredentialProviderUser(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{13793285-3ea6-40fd-b420-15f47da41fbb}')
    @commethod(3)
    def GetSid(self, sid: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetProviderID(self, providerID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStringValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), stringValue: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetValue(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), value: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICredentialProviderUserArray(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{90c119ae-0f18-4520-a1f1-114366a40fe8}')
    @commethod(3)
    def SetProviderFilter(self, guidProviderToFilterTo: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAccountOptions(self, credentialProviderAccountOptions: POINTER(win32more.Windows.Win32.UI.Shell.CREDENTIAL_PROVIDER_ACCOUNT_OPTIONS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCount(self, userCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetAt(self, userIndex: UInt32, user: POINTER(win32more.Windows.Win32.UI.Shell.ICredentialProviderUser)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICurrentItem(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IRelatedItem
    _iid_ = Guid('{240a7174-d653-4a1d-a6d3-d4943cfbfe3d}')
class ICurrentWorkingDirectory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{91956d21-9276-11d1-921a-006097df5bd4}')
    @commethod(3)
    def GetDirectory(self, pwzPath: win32more.Windows.Win32.Foundation.PWSTR, cchSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetDirectory(self, pwzPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICustomDestinationList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6332debf-87b5-4670-90c0-5e57b408a49e}')
    @commethod(3)
    def SetAppID(self, pszAppID: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BeginList(self, pcMinSlots: POINTER(UInt32), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AppendCategory(self, pszCategory: win32more.Windows.Win32.Foundation.PWSTR, poa: win32more.Windows.Win32.UI.Shell.Common.IObjectArray) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AppendKnownCategory(self, category: win32more.Windows.Win32.UI.Shell.KNOWNDESTCATEGORY) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddUserTasks(self, poa: win32more.Windows.Win32.UI.Shell.Common.IObjectArray) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CommitList(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRemovedDestinations(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def DeleteList(self, pszAppID: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AbortList(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDataObjectAsyncCapability(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3d8b0590-f691-11d2-8ea9-006097df5bd4}')
    @commethod(3)
    def SetAsyncMode(self, fDoOpAsync: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAsyncMode(self, pfIsOpAsync: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def StartOperation(self, pbcReserved: win32more.Windows.Win32.System.Com.IBindCtx) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def InOperation(self, pfInAsyncOp: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EndOperation(self, hResult: win32more.Windows.Win32.Foundation.HRESULT, pbcReserved: win32more.Windows.Win32.System.Com.IBindCtx, dwEffects: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDataObjectProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3d25f6d6-4b2a-433c-9184-7c33ad35d001}')
    @commethod(3)
    def GetDataObject(self, dataObject: POINTER(win32more.Windows.Win32.System.Com.IDataObject)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetDataObject(self, dataObject: win32more.Windows.Win32.System.Com.IDataObject) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDataTransferManagerInterop(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3a3dcd6c-3eab-43dc-bcde-45671ce800c8}')
    @commethod(3)
    def GetForWindow(self, appWindow: win32more.Windows.Win32.Foundation.HWND, riid: POINTER(Guid), dataTransferManager: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ShowShareUIForWindow(self, appWindow: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDefaultExtractIconInit(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{41ded17d-d6b3-4261-997d-88c60e4b1d58}')
    @commethod(3)
    def SetFlags(self, uFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetKey(self, hkey: win32more.Windows.Win32.System.Registry.HKEY) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetNormalIcon(self, pszFile: win32more.Windows.Win32.Foundation.PWSTR, iIcon: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetOpenIcon(self, pszFile: win32more.Windows.Win32.Foundation.PWSTR, iIcon: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetShortcutIcon(self, pszFile: win32more.Windows.Win32.Foundation.PWSTR, iIcon: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetDefaultIcon(self, pszFile: win32more.Windows.Win32.Foundation.PWSTR, iIcon: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDefaultFolderMenuInitialize(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7690aa79-f8fc-4615-a327-36f7d18f5d91}')
    @commethod(3)
    def Initialize(self, hwnd: win32more.Windows.Win32.Foundation.HWND, pcmcb: win32more.Windows.Win32.UI.Shell.IContextMenuCB, pidlFolder: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), psf: win32more.Windows.Win32.UI.Shell.IShellFolder, cidl: UInt32, apidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)), punkAssociation: win32more.Windows.Win32.System.Com.IUnknown, cKeys: UInt32, aKeys: POINTER(win32more.Windows.Win32.System.Registry.HKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetMenuRestrictions(self, dfmrValues: win32more.Windows.Win32.UI.Shell.DEFAULT_FOLDER_MENU_RESTRICTIONS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMenuRestrictions(self, dfmrMask: win32more.Windows.Win32.UI.Shell.DEFAULT_FOLDER_MENU_RESTRICTIONS, pdfmrValues: POINTER(win32more.Windows.Win32.UI.Shell.DEFAULT_FOLDER_MENU_RESTRICTIONS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetHandlerClsid(self, rclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDelegateFolder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{add8ba80-002b-11d0-8f0f-00c04fd7d062}')
    @commethod(3)
    def SetItemAlloc(self, pmalloc: win32more.Windows.Win32.System.Com.IMalloc) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDelegateItem(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IRelatedItem
    _iid_ = Guid('{3c5a1c94-c951-4cb7-bb6d-3b93f30cce93}')
class IDeskBand(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IDockingWindow
    _iid_ = Guid('{eb0fe172-1a3a-11d0-89b3-00a0c90a90ac}')
    @commethod(8)
    def GetBandInfo(self, dwBandID: UInt32, dwViewMode: UInt32, pdbi: POINTER(win32more.Windows.Win32.UI.Shell.DESKBANDINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDeskBand2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IDeskBand
    _iid_ = Guid('{79d16de4-abee-4021-8d9d-9169b261d657}')
    @commethod(9)
    def CanRenderComposited(self, pfCanRenderComposited: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetCompositionState(self, fCompositionEnabled: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetCompositionState(self, pfCompositionEnabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDeskBandInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{77e425fc-cbf9-4307-ba6a-bb5727745661}')
    @commethod(3)
    def GetDefaultBandWidth(self, dwBandID: UInt32, dwViewMode: UInt32, pnWidth: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDeskBar(ComPtr):
    extends: win32more.Windows.Win32.System.Ole.IOleWindow
    _iid_ = Guid('{eb0fe173-1a3a-11d0-89b3-00a0c90a90ac}')
    @commethod(5)
    def SetClient(self, punkClient: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetClient(self, ppunkClient: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnPosRectChangeDB(self, prc: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDeskBarClient(ComPtr):
    extends: win32more.Windows.Win32.System.Ole.IOleWindow
    _iid_ = Guid('{eb0fe175-1a3a-11d0-89b3-00a0c90a90ac}')
    @commethod(5)
    def SetDeskBarSite(self, punkSite: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetModeDBC(self, dwMode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UIActivateDBC(self, dwState: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSize(self, dwWhich: UInt32, prc: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDesktopGadget(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c1646bc4-f298-4f91-a204-eb2dd1709d1a}')
    @commethod(3)
    def RunGadget(self, gadgetPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDesktopWallpaper(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b92b56a9-8b55-4e14-9a89-0199bbb6f93b}')
    @commethod(3)
    def SetWallpaper(self, monitorID: win32more.Windows.Win32.Foundation.PWSTR, wallpaper: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetWallpaper(self, monitorID: win32more.Windows.Win32.Foundation.PWSTR, wallpaper: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMonitorDevicePathAt(self, monitorIndex: UInt32, monitorID: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMonitorDevicePathCount(self, count: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetMonitorRECT(self, monitorID: win32more.Windows.Win32.Foundation.PWSTR, displayRect: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetBackgroundColor(self, color: win32more.Windows.Win32.Foundation.COLORREF) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetBackgroundColor(self, color: POINTER(win32more.Windows.Win32.Foundation.COLORREF)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetPosition(self, position: win32more.Windows.Win32.UI.Shell.DESKTOP_WALLPAPER_POSITION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetPosition(self, position: POINTER(win32more.Windows.Win32.UI.Shell.DESKTOP_WALLPAPER_POSITION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetSlideshow(self, items: win32more.Windows.Win32.UI.Shell.IShellItemArray) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetSlideshow(self, items: POINTER(win32more.Windows.Win32.UI.Shell.IShellItemArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetSlideshowOptions(self, options: win32more.Windows.Win32.UI.Shell.DESKTOP_SLIDESHOW_OPTIONS, slideshowTick: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetSlideshowOptions(self, options: POINTER(win32more.Windows.Win32.UI.Shell.DESKTOP_SLIDESHOW_OPTIONS), slideshowTick: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def AdvanceSlideshow(self, monitorID: win32more.Windows.Win32.Foundation.PWSTR, direction: win32more.Windows.Win32.UI.Shell.DESKTOP_SLIDESHOW_DIRECTION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetStatus(self, state: POINTER(win32more.Windows.Win32.UI.Shell.DESKTOP_SLIDESHOW_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def Enable(self, enable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDestinationStreamFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8a87781b-39a7-4a1f-aab3-a39b9c34a7d9}')
    @commethod(3)
    def GetDestinationStream(self, ppstm: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDisplayItem(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IRelatedItem
    _iid_ = Guid('{c6fd5997-9f6b-4888-8703-94e80e8cde3f}')
class IDocViewSite(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{87d605e0-c511-11cf-89a9-00a0c9054129}')
    @commethod(3)
    def OnSetTitle(self, pvTitle: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDockingWindow(ComPtr):
    extends: win32more.Windows.Win32.System.Ole.IOleWindow
    _iid_ = Guid('{012dd920-7b26-11d0-8ca9-00a0c92dbfe8}')
    @commethod(5)
    def ShowDW(self, fShow: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CloseDW(self, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ResizeBorderDW(self, prcBorder: POINTER(win32more.Windows.Win32.Foundation.RECT), punkToolbarSite: win32more.Windows.Win32.System.Com.IUnknown, fReserved: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDockingWindowFrame(ComPtr):
    extends: win32more.Windows.Win32.System.Ole.IOleWindow
    _iid_ = Guid('{47d2657a-7b27-11d0-8ca9-00a0c92dbfe8}')
    @commethod(5)
    def AddToolbar(self, punkSrc: win32more.Windows.Win32.System.Com.IUnknown, pwszItem: win32more.Windows.Win32.Foundation.PWSTR, dwAddFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveToolbar(self, punkSrc: win32more.Windows.Win32.System.Com.IUnknown, dwRemoveFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FindToolbar(self, pwszItem: win32more.Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDockingWindowSite(ComPtr):
    extends: win32more.Windows.Win32.System.Ole.IOleWindow
    _iid_ = Guid('{2a342fc2-7b26-11d0-8ca9-00a0c92dbfe8}')
    @commethod(5)
    def GetBorderDW(self, punkObj: win32more.Windows.Win32.System.Com.IUnknown, prcBorder: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RequestBorderSpaceDW(self, punkObj: win32more.Windows.Win32.System.Com.IUnknown, pbw: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetBorderSpaceDW(self, punkObj: win32more.Windows.Win32.System.Com.IUnknown, pbw: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDragSourceHelper(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{de5bf786-477a-11d2-839d-00c04fd918d0}')
    @commethod(3)
    def InitializeFromBitmap(self, pshdi: POINTER(win32more.Windows.Win32.UI.Shell.SHDRAGIMAGE), pDataObject: win32more.Windows.Win32.System.Com.IDataObject) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def InitializeFromWindow(self, hwnd: win32more.Windows.Win32.Foundation.HWND, ppt: POINTER(win32more.Windows.Win32.Foundation.POINT), pDataObject: win32more.Windows.Win32.System.Com.IDataObject) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDragSourceHelper2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IDragSourceHelper
    _iid_ = Guid('{83e07d0d-0c5f-4163-bf1a-60b274051e40}')
    @commethod(5)
    def SetFlags(self, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDropTargetHelper(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4657278b-411b-11d2-839a-00c04fd918d0}')
    @commethod(3)
    def DragEnter(self, hwndTarget: win32more.Windows.Win32.Foundation.HWND, pDataObject: win32more.Windows.Win32.System.Com.IDataObject, ppt: POINTER(win32more.Windows.Win32.Foundation.POINT), dwEffect: win32more.Windows.Win32.System.Ole.DROPEFFECT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DragLeave(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DragOver(self, ppt: POINTER(win32more.Windows.Win32.Foundation.POINT), dwEffect: win32more.Windows.Win32.System.Ole.DROPEFFECT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Drop(self, pDataObject: win32more.Windows.Win32.System.Com.IDataObject, ppt: POINTER(win32more.Windows.Win32.Foundation.POINT), dwEffect: win32more.Windows.Win32.System.Ole.DROPEFFECT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Show(self, fShow: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDynamicHWHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dc2601d7-059e-42fc-a09d-2afd21b6d5f7}')
    @commethod(3)
    def GetDynamicInfo(self, pszDeviceID: win32more.Windows.Win32.Foundation.PWSTR, dwContentType: UInt32, ppszAction: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
IENamespaceTreeControl = Guid('{ace52d03-e5cd-4b20-82ff-e71b11beae1d}')
IEPDNFLAGS = Int32
IEPDN_BINDINGUI: win32more.Windows.Win32.UI.Shell.IEPDNFLAGS = 1
IESHORTCUTFLAGS = Int32
IESHORTCUT_NEWBROWSER: win32more.Windows.Win32.UI.Shell.IESHORTCUTFLAGS = 1
IESHORTCUT_OPENNEWTAB: win32more.Windows.Win32.UI.Shell.IESHORTCUTFLAGS = 2
IESHORTCUT_FORCENAVIGATE: win32more.Windows.Win32.UI.Shell.IESHORTCUTFLAGS = 4
IESHORTCUT_BACKGROUNDTAB: win32more.Windows.Win32.UI.Shell.IESHORTCUTFLAGS = 8
class IEnumACString(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IEnumString
    _iid_ = Guid('{8e74c210-cf9d-4eaf-a403-7356428f0a5a}')
    @commethod(7)
    def NextItem(self, pszUrl: win32more.Windows.Win32.Foundation.PWSTR, cchMax: UInt32, pulSortIndex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetEnumOptions(self, dwOptions: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetEnumOptions(self, pdwOptions: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumAssocHandlers(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{973810ae-9599-4b88-9e4d-6ee98c9552da}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.UI.Shell.IAssocHandler), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumExplorerCommand(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a88826f8-186f-4987-aade-ea0cef8fbfe8}')
    @commethod(3)
    def Next(self, celt: UInt32, pUICommand: POINTER(win32more.Windows.Win32.UI.Shell.IExplorerCommand), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.UI.Shell.IEnumExplorerCommand)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumExtraSearch(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0e700be1-9db6-11d1-a1ce-00c04fd75d13}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.UI.Shell.EXTRASEARCH), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.UI.Shell.IEnumExtraSearch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumFullIDList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d0191542-7954-4908-bc06-b2360bbe45ba}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.UI.Shell.IEnumFullIDList)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumHLITEM(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{79eac9c6-baf9-11ce-8c82-00aa004ba90b}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.UI.Shell.HLITEM), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppienumhlitem: POINTER(win32more.Windows.Win32.UI.Shell.IEnumHLITEM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumIDList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{000214f2-0000-0000-c000-000000000046}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.UI.Shell.IEnumIDList)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumObjects(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2c1c7e2e-2d0e-4059-831e-1e6f82335c2e}')
    @commethod(3)
    def Next(self, celt: UInt32, riid: POINTER(Guid), rgelt: POINTER(VoidPtr), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.UI.Shell.IEnumObjects)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumPublishedApps(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0b124f8c-91f0-11d1-b8b5-006008059382}')
    @commethod(3)
    def Next(self, pia: POINTER(win32more.Windows.Win32.UI.Shell.IPublishedApp)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumReadyCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{61e00d45-8fff-4e60-924e-6537b61612dd}')
    @commethod(3)
    def EnumReady(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumResources(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2dd81fe3-a83c-4da9-a330-47249d345ba1}')
    @commethod(3)
    def Next(self, celt: UInt32, psir: POINTER(win32more.Windows.Win32.UI.Shell.SHELL_ITEM_RESOURCE), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenumr: POINTER(win32more.Windows.Win32.UI.Shell.IEnumResources)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumShellItems(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{70629033-e363-4a28-a567-0db78006e6d7}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.UI.Shell.IShellItem), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.UI.Shell.IEnumShellItems)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumSyncMgrConflict(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{82705914-dda3-4893-ba99-49de6c8c8036}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.UI.Shell.ISyncMgrConflict), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.UI.Shell.IEnumSyncMgrConflict)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumSyncMgrEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c81a1d4e-8cf7-4683-80e0-bcae88d677b6}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.UI.Shell.ISyncMgrEvent), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.UI.Shell.IEnumSyncMgrEvents)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumSyncMgrSyncItems(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{54b3abf3-f085-4181-b546-e29c403c726b}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.UI.Shell.ISyncMgrSyncItem), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.UI.Shell.IEnumSyncMgrSyncItems)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumTravelLogEntry(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7ebfdd85-ad18-11d3-a4c5-00c04f72d6b8}')
    @commethod(3)
    def Next(self, cElt: UInt32, rgElt: POINTER(win32more.Windows.Win32.UI.Shell.ITravelLogEntry), pcEltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, cElt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.UI.Shell.IEnumTravelLogEntry)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumerableView(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8c8bf236-1aec-495f-9894-91d57c3c686f}')
    @commethod(3)
    def SetEnumReadyCallback(self, percb: win32more.Windows.Win32.UI.Shell.IEnumReadyCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateEnumIDListFromContents(self, pidlFolder: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), dwEnumFlags: UInt32, ppEnumIDList: POINTER(win32more.Windows.Win32.UI.Shell.IEnumIDList)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IExecuteCommand(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7f9185b0-cb92-43c5-80a9-92277a4f7b54}')
    @commethod(3)
    def SetKeyState(self, grfKeyState: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetParameters(self, pszParameters: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetPosition(self, pt: win32more.Windows.Win32.Foundation.POINT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetShowWindow(self, nShow: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetNoShowUI(self, fNoShowUI: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetDirectory(self, pszDirectory: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Execute(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IExecuteCommandApplicationHostEnvironment(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{18b21aa9-e184-4ff0-9f5e-f882d03771b3}')
    @commethod(3)
    def GetValue(self, pahe: POINTER(win32more.Windows.Win32.UI.Shell.AHE_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IExecuteCommandHost(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4b6832a2-5f04-4c9d-b89d-727a15d103e7}')
    @commethod(3)
    def GetUIMode(self, pUIMode: POINTER(win32more.Windows.Win32.UI.Shell.EC_HOST_UI_MODE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IExpDispSupport(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0d7d1d00-6fc0-11d0-a974-00c04fd705a2}')
    @commethod(3)
    def FindConnectionPoint(self, riid: POINTER(Guid), ppccp: POINTER(win32more.Windows.Win32.System.Com.IConnectionPoint)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnTranslateAccelerator(self, pMsg: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.MSG), grfModifiers: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnInvoke(self, dispidMember: Int32, iid: POINTER(Guid), lcid: UInt32, wFlags: UInt16, pdispparams: POINTER(win32more.Windows.Win32.System.Com.DISPPARAMS), pVarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pexcepinfo: POINTER(win32more.Windows.Win32.System.Com.EXCEPINFO), puArgErr: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IExpDispSupportXP(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2f0dd58c-f789-4f14-99fb-9293b3c9c212}')
    @commethod(3)
    def FindCIE4ConnectionPoint(self, riid: POINTER(Guid), ppccp: POINTER(win32more.Windows.Win32.UI.Shell.CIE4ConnectionPoint)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnTranslateAccelerator(self, pMsg: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.MSG), grfModifiers: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnInvoke(self, dispidMember: Int32, iid: POINTER(Guid), lcid: UInt32, wFlags: UInt16, pdispparams: POINTER(win32more.Windows.Win32.System.Com.DISPPARAMS), pVarResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pexcepinfo: POINTER(win32more.Windows.Win32.System.Com.EXCEPINFO), puArgErr: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IExplorerBrowser(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dfd3b6b5-c10c-4be9-85f6-a66969f402f6}')
    @commethod(3)
    def Initialize(self, hwndParent: win32more.Windows.Win32.Foundation.HWND, prc: POINTER(win32more.Windows.Win32.Foundation.RECT), pfs: POINTER(win32more.Windows.Win32.UI.Shell.FOLDERSETTINGS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Destroy(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetRect(self, phdwp: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.HDWP), rcBrowser: win32more.Windows.Win32.Foundation.RECT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetPropertyBag(self, pszPropertyBag: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetEmptyText(self, pszEmptyText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetFolderSettings(self, pfs: POINTER(win32more.Windows.Win32.UI.Shell.FOLDERSETTINGS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Advise(self, psbe: win32more.Windows.Win32.UI.Shell.IExplorerBrowserEvents, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Unadvise(self, dwCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetOptions(self, dwFlag: win32more.Windows.Win32.UI.Shell.EXPLORER_BROWSER_OPTIONS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetOptions(self, pdwFlag: POINTER(win32more.Windows.Win32.UI.Shell.EXPLORER_BROWSER_OPTIONS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def BrowseToIDList(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), uFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def BrowseToObject(self, punk: win32more.Windows.Win32.System.Com.IUnknown, uFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def FillFromObject(self, punk: win32more.Windows.Win32.System.Com.IUnknown, dwFlags: win32more.Windows.Win32.UI.Shell.EXPLORER_BROWSER_FILL_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def RemoveAll(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetCurrentView(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IExplorerBrowserEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{361bbdc7-e6ee-4e13-be58-58e2240c810f}')
    @commethod(3)
    def OnNavigationPending(self, pidlFolder: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnViewCreated(self, psv: win32more.Windows.Win32.UI.Shell.IShellView) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnNavigationComplete(self, pidlFolder: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnNavigationFailed(self, pidlFolder: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IExplorerCommand(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a08ce4d0-fa25-44ab-b57c-c7b1c323e0b9}')
    @commethod(3)
    def GetTitle(self, psiItemArray: win32more.Windows.Win32.UI.Shell.IShellItemArray, ppszName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetIcon(self, psiItemArray: win32more.Windows.Win32.UI.Shell.IShellItemArray, ppszIcon: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetToolTip(self, psiItemArray: win32more.Windows.Win32.UI.Shell.IShellItemArray, ppszInfotip: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCanonicalName(self, pguidCommandName: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetState(self, psiItemArray: win32more.Windows.Win32.UI.Shell.IShellItemArray, fOkToBeSlow: win32more.Windows.Win32.Foundation.BOOL, pCmdState: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Invoke(self, psiItemArray: win32more.Windows.Win32.UI.Shell.IShellItemArray, pbc: win32more.Windows.Win32.System.Com.IBindCtx) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFlags(self, pFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EnumSubCommands(self, ppEnum: POINTER(win32more.Windows.Win32.UI.Shell.IEnumExplorerCommand)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IExplorerCommandProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{64961751-0835-43c0-8ffe-d57686530e64}')
    @commethod(3)
    def GetCommands(self, punkSite: win32more.Windows.Win32.System.Com.IUnknown, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCommand(self, rguidCommandId: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IExplorerCommandState(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bddacb60-7657-47ae-8445-d23e1acf82ae}')
    @commethod(3)
    def GetState(self, psiItemArray: win32more.Windows.Win32.UI.Shell.IShellItemArray, fOkToBeSlow: win32more.Windows.Win32.Foundation.BOOL, pCmdState: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IExplorerPaneVisibility(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e07010ec-bc17-44c0-97b0-46c7c95b9edc}')
    @commethod(3)
    def GetPaneState(self, ep: POINTER(Guid), peps: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IExtensionServices(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{79eac9cb-baf9-11ce-8c82-00aa004ba90b}')
    @commethod(3)
    def SetAdditionalHeaders(self, pwzAdditionalHeaders: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetAuthenticateData(self, phwnd: win32more.Windows.Win32.Foundation.HWND, pwzUsername: win32more.Windows.Win32.Foundation.PWSTR, pwzPassword: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IExtractIconA(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{000214eb-0000-0000-c000-000000000046}')
    @commethod(3)
    def GetIconLocation(self, uFlags: UInt32, pszIconFile: win32more.Windows.Win32.Foundation.PSTR, cchMax: UInt32, piIndex: POINTER(Int32), pwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Extract(self, pszFile: win32more.Windows.Win32.Foundation.PSTR, nIconIndex: UInt32, phiconLarge: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.HICON), phiconSmall: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.HICON), nIconSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IExtractIconW(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{000214fa-0000-0000-c000-000000000046}')
    @commethod(3)
    def GetIconLocation(self, uFlags: UInt32, pszIconFile: win32more.Windows.Win32.Foundation.PWSTR, cchMax: UInt32, piIndex: POINTER(Int32), pwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Extract(self, pszFile: win32more.Windows.Win32.Foundation.PWSTR, nIconIndex: UInt32, phiconLarge: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.HICON), phiconSmall: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.HICON), nIconSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
IExtractIcon = UnicodeAlias('IExtractIconW')
class IExtractImage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bb2e617c-0920-11d1-9a0b-00c04fc2d6c1}')
    @commethod(3)
    def GetLocation(self, pszPathBuffer: win32more.Windows.Win32.Foundation.PWSTR, cch: UInt32, pdwPriority: POINTER(UInt32), prgSize: POINTER(win32more.Windows.Win32.Foundation.SIZE), dwRecClrDepth: UInt32, pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Extract(self, phBmpThumbnail: POINTER(win32more.Windows.Win32.Graphics.Gdi.HBITMAP)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IExtractImage2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IExtractImage
    _iid_ = Guid('{953bb1ee-93b4-11d1-98a3-00c04fb687da}')
    @commethod(5)
    def GetDateStamp(self, pDateStamp: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFileDialog(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IModalWindow
    _iid_ = Guid('{42f85136-db7e-439c-85f1-e4075d135fc8}')
    @commethod(4)
    def SetFileTypes(self, cFileTypes: UInt32, rgFilterSpec: POINTER(win32more.Windows.Win32.UI.Shell.Common.COMDLG_FILTERSPEC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetFileTypeIndex(self, iFileType: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFileTypeIndex(self, piFileType: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Advise(self, pfde: win32more.Windows.Win32.UI.Shell.IFileDialogEvents, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Unadvise(self, dwCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetOptions(self, fos: win32more.Windows.Win32.UI.Shell.FILEOPENDIALOGOPTIONS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetOptions(self, pfos: POINTER(win32more.Windows.Win32.UI.Shell.FILEOPENDIALOGOPTIONS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetDefaultFolder(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetFolder(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetFolder(self, ppsi: POINTER(win32more.Windows.Win32.UI.Shell.IShellItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetCurrentSelection(self, ppsi: POINTER(win32more.Windows.Win32.UI.Shell.IShellItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetFileName(self, pszName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetFileName(self, pszName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetTitle(self, pszTitle: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetOkButtonLabel(self, pszText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetFileNameLabel(self, pszLabel: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetResult(self, ppsi: POINTER(win32more.Windows.Win32.UI.Shell.IShellItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def AddPlace(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem, fdap: win32more.Windows.Win32.UI.Shell.FDAP) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetDefaultExtension(self, pszDefaultExtension: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Close(self, hr: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetClientGuid(self, guid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def ClearClientData(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def SetFilter(self, pFilter: win32more.Windows.Win32.UI.Shell.IShellItemFilter) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFileDialog2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IFileDialog
    _iid_ = Guid('{61744fc7-85b5-4791-a9b0-272276309b13}')
    @commethod(27)
    def SetCancelButtonLabel(self, pszLabel: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def SetNavigationRoot(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFileDialogControlEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{36116642-d713-4b97-9b83-7484a9d00433}')
    @commethod(3)
    def OnItemSelected(self, pfdc: win32more.Windows.Win32.UI.Shell.IFileDialogCustomize, dwIDCtl: UInt32, dwIDItem: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnButtonClicked(self, pfdc: win32more.Windows.Win32.UI.Shell.IFileDialogCustomize, dwIDCtl: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnCheckButtonToggled(self, pfdc: win32more.Windows.Win32.UI.Shell.IFileDialogCustomize, dwIDCtl: UInt32, bChecked: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnControlActivating(self, pfdc: win32more.Windows.Win32.UI.Shell.IFileDialogCustomize, dwIDCtl: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFileDialogCustomize(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e6fdd21a-163f-4975-9c8c-a69f1ba37034}')
    @commethod(3)
    def EnableOpenDropDown(self, dwIDCtl: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddMenu(self, dwIDCtl: UInt32, pszLabel: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddPushButton(self, dwIDCtl: UInt32, pszLabel: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddComboBox(self, dwIDCtl: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddRadioButtonList(self, dwIDCtl: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AddCheckButton(self, dwIDCtl: UInt32, pszLabel: win32more.Windows.Win32.Foundation.PWSTR, bChecked: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddEditBox(self, dwIDCtl: UInt32, pszText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def AddSeparator(self, dwIDCtl: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AddText(self, dwIDCtl: UInt32, pszText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetControlLabel(self, dwIDCtl: UInt32, pszLabel: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetControlState(self, dwIDCtl: UInt32, pdwState: POINTER(win32more.Windows.Win32.UI.Shell.CDCONTROLSTATEF)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetControlState(self, dwIDCtl: UInt32, dwState: win32more.Windows.Win32.UI.Shell.CDCONTROLSTATEF) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetEditBoxText(self, dwIDCtl: UInt32, ppszText: POINTER(POINTER(UInt16))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetEditBoxText(self, dwIDCtl: UInt32, pszText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetCheckButtonState(self, dwIDCtl: UInt32, pbChecked: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetCheckButtonState(self, dwIDCtl: UInt32, bChecked: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def AddControlItem(self, dwIDCtl: UInt32, dwIDItem: UInt32, pszLabel: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def RemoveControlItem(self, dwIDCtl: UInt32, dwIDItem: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def RemoveAllControlItems(self, dwIDCtl: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetControlItemState(self, dwIDCtl: UInt32, dwIDItem: UInt32, pdwState: POINTER(win32more.Windows.Win32.UI.Shell.CDCONTROLSTATEF)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetControlItemState(self, dwIDCtl: UInt32, dwIDItem: UInt32, dwState: win32more.Windows.Win32.UI.Shell.CDCONTROLSTATEF) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def GetSelectedControlItem(self, dwIDCtl: UInt32, pdwIDItem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetSelectedControlItem(self, dwIDCtl: UInt32, dwIDItem: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def StartVisualGroup(self, dwIDCtl: UInt32, pszLabel: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def EndVisualGroup(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def MakeProminent(self, dwIDCtl: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetControlItemText(self, dwIDCtl: UInt32, dwIDItem: UInt32, pszLabel: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFileDialogEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{973510db-7d7f-452b-8975-74a85828d354}')
    @commethod(3)
    def OnFileOk(self, pfd: win32more.Windows.Win32.UI.Shell.IFileDialog) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnFolderChanging(self, pfd: win32more.Windows.Win32.UI.Shell.IFileDialog, psiFolder: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnFolderChange(self, pfd: win32more.Windows.Win32.UI.Shell.IFileDialog) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnSelectionChange(self, pfd: win32more.Windows.Win32.UI.Shell.IFileDialog) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnShareViolation(self, pfd: win32more.Windows.Win32.UI.Shell.IFileDialog, psi: win32more.Windows.Win32.UI.Shell.IShellItem, pResponse: POINTER(win32more.Windows.Win32.UI.Shell.FDE_SHAREVIOLATION_RESPONSE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnTypeChange(self, pfd: win32more.Windows.Win32.UI.Shell.IFileDialog) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnOverwrite(self, pfd: win32more.Windows.Win32.UI.Shell.IFileDialog, psi: win32more.Windows.Win32.UI.Shell.IShellItem, pResponse: POINTER(win32more.Windows.Win32.UI.Shell.FDE_OVERWRITE_RESPONSE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFileIsInUse(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{64a1cbf0-3a1a-4461-9158-376969693950}')
    @commethod(3)
    def GetAppName(self, ppszName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetUsage(self, pfut: POINTER(win32more.Windows.Win32.UI.Shell.FILE_USAGE_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCapabilities(self, pdwCapFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSwitchToHWND(self, phwnd: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CloseFile(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFileOpenDialog(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IFileDialog
    _iid_ = Guid('{d57c7288-d4ad-4768-be02-9d969532d960}')
    @commethod(27)
    def GetResults(self, ppenum: POINTER(win32more.Windows.Win32.UI.Shell.IShellItemArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetSelectedItems(self, ppsai: POINTER(win32more.Windows.Win32.UI.Shell.IShellItemArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFileOperation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{947aab5f-0a5c-4c13-b4d6-4bf7836fc9f8}')
    @commethod(3)
    def Advise(self, pfops: win32more.Windows.Win32.UI.Shell.IFileOperationProgressSink, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unadvise(self, dwCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetOperationFlags(self, dwOperationFlags: win32more.Windows.Win32.UI.Shell.FILEOPERATION_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetProgressMessage(self, pszMessage: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetProgressDialog(self, popd: win32more.Windows.Win32.UI.Shell.IOperationsProgressDialog) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetProperties(self, pproparray: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyChangeArray) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetOwnerWindow(self, hwndOwner: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ApplyPropertiesToItem(self, psiItem: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ApplyPropertiesToItems(self, punkItems: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RenameItem(self, psiItem: win32more.Windows.Win32.UI.Shell.IShellItem, pszNewName: win32more.Windows.Win32.Foundation.PWSTR, pfopsItem: win32more.Windows.Win32.UI.Shell.IFileOperationProgressSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def RenameItems(self, pUnkItems: win32more.Windows.Win32.System.Com.IUnknown, pszNewName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def MoveItem(self, psiItem: win32more.Windows.Win32.UI.Shell.IShellItem, psiDestinationFolder: win32more.Windows.Win32.UI.Shell.IShellItem, pszNewName: win32more.Windows.Win32.Foundation.PWSTR, pfopsItem: win32more.Windows.Win32.UI.Shell.IFileOperationProgressSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def MoveItems(self, punkItems: win32more.Windows.Win32.System.Com.IUnknown, psiDestinationFolder: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def CopyItem(self, psiItem: win32more.Windows.Win32.UI.Shell.IShellItem, psiDestinationFolder: win32more.Windows.Win32.UI.Shell.IShellItem, pszCopyName: win32more.Windows.Win32.Foundation.PWSTR, pfopsItem: win32more.Windows.Win32.UI.Shell.IFileOperationProgressSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def CopyItems(self, punkItems: win32more.Windows.Win32.System.Com.IUnknown, psiDestinationFolder: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def DeleteItem(self, psiItem: win32more.Windows.Win32.UI.Shell.IShellItem, pfopsItem: win32more.Windows.Win32.UI.Shell.IFileOperationProgressSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def DeleteItems(self, punkItems: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def NewItem(self, psiDestinationFolder: win32more.Windows.Win32.UI.Shell.IShellItem, dwFileAttributes: UInt32, pszName: win32more.Windows.Win32.Foundation.PWSTR, pszTemplateName: win32more.Windows.Win32.Foundation.PWSTR, pfopsItem: win32more.Windows.Win32.UI.Shell.IFileOperationProgressSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def PerformOperations(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetAnyOperationsAborted(self, pfAnyOperationsAborted: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFileOperation2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IFileOperation
    _iid_ = Guid('{cd8f23c1-8f61-4916-909d-55bdd0918753}')
    @commethod(23)
    def SetOperationFlags2(self, operationFlags2: win32more.Windows.Win32.UI.Shell.FILE_OPERATION_FLAGS2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFileOperationProgressSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{04b0f1a7-9490-44bc-96e1-4296a31252e2}')
    @commethod(3)
    def StartOperations(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FinishOperations(self, hrResult: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def PreRenameItem(self, dwFlags: UInt32, psiItem: win32more.Windows.Win32.UI.Shell.IShellItem, pszNewName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def PostRenameItem(self, dwFlags: UInt32, psiItem: win32more.Windows.Win32.UI.Shell.IShellItem, pszNewName: win32more.Windows.Win32.Foundation.PWSTR, hrRename: win32more.Windows.Win32.Foundation.HRESULT, psiNewlyCreated: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def PreMoveItem(self, dwFlags: UInt32, psiItem: win32more.Windows.Win32.UI.Shell.IShellItem, psiDestinationFolder: win32more.Windows.Win32.UI.Shell.IShellItem, pszNewName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def PostMoveItem(self, dwFlags: UInt32, psiItem: win32more.Windows.Win32.UI.Shell.IShellItem, psiDestinationFolder: win32more.Windows.Win32.UI.Shell.IShellItem, pszNewName: win32more.Windows.Win32.Foundation.PWSTR, hrMove: win32more.Windows.Win32.Foundation.HRESULT, psiNewlyCreated: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def PreCopyItem(self, dwFlags: UInt32, psiItem: win32more.Windows.Win32.UI.Shell.IShellItem, psiDestinationFolder: win32more.Windows.Win32.UI.Shell.IShellItem, pszNewName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def PostCopyItem(self, dwFlags: UInt32, psiItem: win32more.Windows.Win32.UI.Shell.IShellItem, psiDestinationFolder: win32more.Windows.Win32.UI.Shell.IShellItem, pszNewName: win32more.Windows.Win32.Foundation.PWSTR, hrCopy: win32more.Windows.Win32.Foundation.HRESULT, psiNewlyCreated: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def PreDeleteItem(self, dwFlags: UInt32, psiItem: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def PostDeleteItem(self, dwFlags: UInt32, psiItem: win32more.Windows.Win32.UI.Shell.IShellItem, hrDelete: win32more.Windows.Win32.Foundation.HRESULT, psiNewlyCreated: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def PreNewItem(self, dwFlags: UInt32, psiDestinationFolder: win32more.Windows.Win32.UI.Shell.IShellItem, pszNewName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def PostNewItem(self, dwFlags: UInt32, psiDestinationFolder: win32more.Windows.Win32.UI.Shell.IShellItem, pszNewName: win32more.Windows.Win32.Foundation.PWSTR, pszTemplateName: win32more.Windows.Win32.Foundation.PWSTR, dwFileAttributes: UInt32, hrNew: win32more.Windows.Win32.Foundation.HRESULT, psiNewItem: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def UpdateProgress(self, iWorkTotal: UInt32, iWorkSoFar: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def ResetTimer(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def PauseTimer(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def ResumeTimer(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFileSaveDialog(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IFileDialog
    _iid_ = Guid('{84bccd23-5fde-4cdb-aea4-af64b83d78ab}')
    @commethod(27)
    def SetSaveAsItem(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def SetProperties(self, pStore: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def SetCollectedProperties(self, pList: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyDescriptionList, fAppendDefault: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetProperties(self, ppStore: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def ApplyProperties(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem, pStore: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore, hwnd: win32more.Windows.Win32.Foundation.HWND, pSink: win32more.Windows.Win32.UI.Shell.IFileOperationProgressSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFileSearchBand(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{2d91eea1-9932-11d2-be86-00a0c9a83da1}')
    @commethod(7)
    def SetFocus(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetSearchParameters(self, pbstrSearchID: POINTER(win32more.Windows.Win32.Foundation.BSTR), bNavToResults: win32more.Windows.Win32.Foundation.VARIANT_BOOL, pvarScope: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarQueryFile: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_SearchID(self, pbstrSearchID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Scope(self, pvarScope: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_QueryFile(self, pvarFile: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFileSyncMergeHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d97b5aac-c792-433c-975d-35c4eadc7a9d}')
    @commethod(3)
    def Merge(self, localFilePath: win32more.Windows.Win32.Foundation.PWSTR, serverFilePath: win32more.Windows.Win32.Foundation.PWSTR, updateStatus: POINTER(win32more.Windows.Win32.UI.Shell.MERGE_UPDATE_STATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ShowResolveConflictUIAsync(self, localFilePath: win32more.Windows.Win32.Foundation.PWSTR, monitorToDisplayOn: win32more.Windows.Win32.Graphics.Gdi.HMONITOR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFileSystemBindData(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{01e18d10-4d8b-11d2-855d-006008059367}')
    @commethod(3)
    def SetFindData(self, pfd: POINTER(win32more.Windows.Win32.Storage.FileSystem.WIN32_FIND_DATAW)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFindData(self, pfd: POINTER(win32more.Windows.Win32.Storage.FileSystem.WIN32_FIND_DATAW)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFileSystemBindData2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IFileSystemBindData
    _iid_ = Guid('{3acf075f-71db-4afa-81f0-3fc4fdf2a5b8}')
    @commethod(5)
    def SetFileID(self, liFileID: Int64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFileID(self, pliFileID: POINTER(Int64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetJunctionCLSID(self, clsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetJunctionCLSID(self, pclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFolderBandPriv(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{47c01f95-e185-412c-b5c5-4f27df965aea}')
    @commethod(3)
    def SetCascade(self, fCascade: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetAccelerators(self, fAccelerators: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetNoIcons(self, fNoIcons: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetNoText(self, fNoText: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFolderFilter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9cc22886-dc8e-11d2-b1d0-00c04f8eeb3e}')
    @commethod(3)
    def ShouldShow(self, psf: win32more.Windows.Win32.UI.Shell.IShellFolder, pidlFolder: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pidlItem: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetEnumFlags(self, psf: win32more.Windows.Win32.UI.Shell.IShellFolder, pidlFolder: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), phwnd: POINTER(win32more.Windows.Win32.Foundation.HWND), pgrfFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFolderFilterSite(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c0a651f5-b48b-11d2-b5ed-006097c686f6}')
    @commethod(3)
    def SetFilter(self, punk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFolderView(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cde725b0-ccc9-4519-917e-325d72fab4ce}')
    @commethod(3)
    def GetCurrentViewMode(self, pViewMode: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetCurrentViewMode(self, ViewMode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFolder(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Item(self, iItemIndex: Int32, ppidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ItemCount(self, uFlags: UInt32, pcItems: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Items(self, uFlags: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSelectionMarkedItem(self, piItem: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFocusedItem(self, piItem: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetItemPosition(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), ppt: POINTER(win32more.Windows.Win32.Foundation.POINT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetSpacing(self, ppt: POINTER(win32more.Windows.Win32.Foundation.POINT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetDefaultSpacing(self, ppt: POINTER(win32more.Windows.Win32.Foundation.POINT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetAutoArrange(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SelectItem(self, iItem: Int32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SelectAndPositionItems(self, cidl: UInt32, apidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)), apt: POINTER(win32more.Windows.Win32.Foundation.POINT), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFolderView2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IFolderView
    _iid_ = Guid('{1af3a467-214f-4298-908e-06b03e0b39f9}')
    @commethod(17)
    def SetGroupBy(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), fAscending: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetGroupBy(self, pkey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pfAscending: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetViewProperty(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), propkey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), propvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetViewProperty(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), propkey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetTileViewProperties(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pszPropList: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetExtendedTileViewProperties(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pszPropList: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetText(self, iType: win32more.Windows.Win32.UI.Shell.FVTEXTTYPE, pwszText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetCurrentFolderFlags(self, dwMask: UInt32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetCurrentFolderFlags(self, pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetSortColumnCount(self, pcColumns: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetSortColumns(self, rgSortColumns: POINTER(win32more.Windows.Win32.UI.Shell.SORTCOLUMN), cColumns: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetSortColumns(self, rgSortColumns: POINTER(win32more.Windows.Win32.UI.Shell.SORTCOLUMN), cColumns: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetItem(self, iItem: Int32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def GetVisibleItem(self, iStart: Int32, fPrevious: win32more.Windows.Win32.Foundation.BOOL, piItem: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetSelectedItem(self, iStart: Int32, piItem: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def GetSelection(self, fNoneImpliesFolder: win32more.Windows.Win32.Foundation.BOOL, ppsia: POINTER(win32more.Windows.Win32.UI.Shell.IShellItemArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetSelectionState(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def InvokeVerbOnSelection(self, pszVerb: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def SetViewModeAndIconSize(self, uViewMode: win32more.Windows.Win32.UI.Shell.FOLDERVIEWMODE, iImageSize: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def GetViewModeAndIconSize(self, puViewMode: POINTER(win32more.Windows.Win32.UI.Shell.FOLDERVIEWMODE), piImageSize: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def SetGroupSubsetCount(self, cVisibleRows: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def GetGroupSubsetCount(self, pcVisibleRows: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def SetRedraw(self, fRedrawOn: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def IsMoveInSameFolder(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def DoRename(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFolderViewHost(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1ea58f02-d55a-411d-b09e-9e65ac21605b}')
    @commethod(3)
    def Initialize(self, hwndParent: win32more.Windows.Win32.Foundation.HWND, pdo: win32more.Windows.Win32.System.Com.IDataObject, prc: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFolderViewOC(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{9ba05970-f6a8-11cf-a442-00a0c90a8f39}')
    @commethod(7)
    def SetFolderView(self, pdisp: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFolderViewOptions(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3cc974d2-b302-4d36-ad3e-06d93f695d3f}')
    @commethod(3)
    def SetFolderViewOptions(self, fvoMask: win32more.Windows.Win32.UI.Shell.FOLDERVIEWOPTIONS, fvoFlags: win32more.Windows.Win32.UI.Shell.FOLDERVIEWOPTIONS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFolderViewOptions(self, pfvoFlags: POINTER(win32more.Windows.Win32.UI.Shell.FOLDERVIEWOPTIONS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFolderViewSettings(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ae8c987d-8797-4ed3-be72-2a47dd938db0}')
    @commethod(3)
    def GetColumnPropertyList(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetGroupByProperty(self, pkey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pfGroupAscending: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetViewMode(self, plvm: POINTER(win32more.Windows.Win32.UI.Shell.FOLDERLOGICALVIEWMODE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetIconSize(self, puIconSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFolderFlags(self, pfolderMask: POINTER(win32more.Windows.Win32.UI.Shell.FOLDERFLAGS), pfolderFlags: POINTER(win32more.Windows.Win32.UI.Shell.FOLDERFLAGS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetSortColumns(self, rgSortColumns: POINTER(win32more.Windows.Win32.UI.Shell.SORTCOLUMN), cColumnsIn: UInt32, pcColumnsOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetGroupSubsetCount(self, pcVisibleRows: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFrameworkInputPane(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5752238b-24f0-495a-82f1-2fd593056796}')
    @commethod(3)
    def Advise(self, pWindow: win32more.Windows.Win32.System.Com.IUnknown, pHandler: win32more.Windows.Win32.UI.Shell.IFrameworkInputPaneHandler, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AdviseWithHWND(self, hwnd: win32more.Windows.Win32.Foundation.HWND, pHandler: win32more.Windows.Win32.UI.Shell.IFrameworkInputPaneHandler, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Unadvise(self, dwCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Location(self, prcInputPaneScreenLocation: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IFrameworkInputPaneHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{226c537b-1e76-4d9e-a760-33db29922f18}')
    @commethod(3)
    def Showing(self, prcInputPaneScreenLocation: POINTER(win32more.Windows.Win32.Foundation.RECT), fEnsureFocusedElementInView: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Hiding(self, fEnsureFocusedElementInView: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IGetServiceIds(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4a073526-6103-4e21-b7bc-f519d1524e5d}')
    @commethod(3)
    def GetServiceIds(self, serviceIdCount: POINTER(UInt32), serviceIds: POINTER(POINTER(Guid))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHWEventHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c1fb73d0-ec3a-4ba2-b512-8cdb9187b6d1}')
    @commethod(3)
    def Initialize(self, pszParams: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def HandleEvent(self, pszDeviceID: win32more.Windows.Win32.Foundation.PWSTR, pszAltDeviceID: win32more.Windows.Win32.Foundation.PWSTR, pszEventType: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def HandleEventWithContent(self, pszDeviceID: win32more.Windows.Win32.Foundation.PWSTR, pszAltDeviceID: win32more.Windows.Win32.Foundation.PWSTR, pszEventType: win32more.Windows.Win32.Foundation.PWSTR, pszContentTypeHandler: win32more.Windows.Win32.Foundation.PWSTR, pdataobject: win32more.Windows.Win32.System.Com.IDataObject) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHWEventHandler2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IHWEventHandler
    _iid_ = Guid('{cfcc809f-295d-42e8-9ffc-424b33c487e6}')
    @commethod(6)
    def HandleEventWithHWND(self, pszDeviceID: win32more.Windows.Win32.Foundation.PWSTR, pszAltDeviceID: win32more.Windows.Win32.Foundation.PWSTR, pszEventType: win32more.Windows.Win32.Foundation.PWSTR, hwndOwner: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHandlerActivationHost(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{35094a87-8bb1-4237-96c6-c417eebdb078}')
    @commethod(3)
    def BeforeCoCreateInstance(self, clsidHandler: POINTER(Guid), itemsBeingActivated: win32more.Windows.Win32.UI.Shell.IShellItemArray, handlerInfo: win32more.Windows.Win32.UI.Shell.IHandlerInfo) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BeforeCreateProcess(self, applicationPath: win32more.Windows.Win32.Foundation.PWSTR, commandLine: win32more.Windows.Win32.Foundation.PWSTR, handlerInfo: win32more.Windows.Win32.UI.Shell.IHandlerInfo) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHandlerInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{997706ef-f880-453b-8118-39e1a2d2655a}')
    @commethod(3)
    def GetApplicationDisplayName(self, value: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetApplicationPublisher(self, value: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetApplicationIconReference(self, value: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHandlerInfo2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IHandlerInfo
    _iid_ = Guid('{31cca04c-04d3-4ea9-90de-97b15e87a532}')
    @commethod(6)
    def GetApplicationId(self, value: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHlink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{79eac9c3-baf9-11ce-8c82-00aa004ba90b}')
    @commethod(3)
    def SetHlinkSite(self, pihlSite: win32more.Windows.Win32.UI.Shell.IHlinkSite, dwSiteData: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHlinkSite(self, ppihlSite: POINTER(win32more.Windows.Win32.UI.Shell.IHlinkSite), pdwSiteData: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetMonikerReference(self, grfHLSETF: UInt32, pimkTarget: win32more.Windows.Win32.System.Com.IMoniker, pwzLocation: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMonikerReference(self, dwWhichRef: UInt32, ppimkTarget: POINTER(win32more.Windows.Win32.System.Com.IMoniker), ppwzLocation: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetStringReference(self, grfHLSETF: UInt32, pwzTarget: win32more.Windows.Win32.Foundation.PWSTR, pwzLocation: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetStringReference(self, dwWhichRef: UInt32, ppwzTarget: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ppwzLocation: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetFriendlyName(self, pwzFriendlyName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFriendlyName(self, grfHLFNAMEF: UInt32, ppwzFriendlyName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetTargetFrameName(self, pwzTargetFrameName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetTargetFrameName(self, ppwzTargetFrameName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetMiscStatus(self, pdwStatus: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Navigate(self, grfHLNF: UInt32, pibc: win32more.Windows.Win32.System.Com.IBindCtx, pibsc: win32more.Windows.Win32.System.Com.IBindStatusCallback, pihlbc: win32more.Windows.Win32.UI.Shell.IHlinkBrowseContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetAdditionalParams(self, pwzAdditionalParams: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetAdditionalParams(self, ppwzAdditionalParams: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHlinkBrowseContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{79eac9c7-baf9-11ce-8c82-00aa004ba90b}')
    @commethod(3)
    def Register(self, reserved: UInt32, piunk: win32more.Windows.Win32.System.Com.IUnknown, pimk: win32more.Windows.Win32.System.Com.IMoniker, pdwRegister: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetObject(self, pimk: win32more.Windows.Win32.System.Com.IMoniker, fBindIfRootRegistered: win32more.Windows.Win32.Foundation.BOOL, ppiunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Revoke(self, dwRegister: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetBrowseWindowInfo(self, phlbwi: POINTER(win32more.Windows.Win32.UI.Shell.HLBWINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetBrowseWindowInfo(self, phlbwi: POINTER(win32more.Windows.Win32.UI.Shell.HLBWINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetInitialHlink(self, pimkTarget: win32more.Windows.Win32.System.Com.IMoniker, pwzLocation: win32more.Windows.Win32.Foundation.PWSTR, pwzFriendlyName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnNavigateHlink(self, grfHLNF: UInt32, pimkTarget: win32more.Windows.Win32.System.Com.IMoniker, pwzLocation: win32more.Windows.Win32.Foundation.PWSTR, pwzFriendlyName: win32more.Windows.Win32.Foundation.PWSTR, puHLID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def UpdateHlink(self, uHLID: UInt32, pimkTarget: win32more.Windows.Win32.System.Com.IMoniker, pwzLocation: win32more.Windows.Win32.Foundation.PWSTR, pwzFriendlyName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EnumNavigationStack(self, dwReserved: UInt32, grfHLFNAMEF: UInt32, ppienumhlitem: POINTER(win32more.Windows.Win32.UI.Shell.IEnumHLITEM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def QueryHlink(self, grfHLQF: UInt32, uHLID: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetHlink(self, uHLID: UInt32, ppihl: POINTER(win32more.Windows.Win32.UI.Shell.IHlink)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetCurrentHlink(self, uHLID: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def Clone(self, piunkOuter: win32more.Windows.Win32.System.Com.IUnknown, riid: POINTER(Guid), ppiunkObj: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Close(self, reserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHlinkFrame(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{79eac9c5-baf9-11ce-8c82-00aa004ba90b}')
    @commethod(3)
    def SetBrowseContext(self, pihlbc: win32more.Windows.Win32.UI.Shell.IHlinkBrowseContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetBrowseContext(self, ppihlbc: POINTER(win32more.Windows.Win32.UI.Shell.IHlinkBrowseContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Navigate(self, grfHLNF: UInt32, pbc: win32more.Windows.Win32.System.Com.IBindCtx, pibsc: win32more.Windows.Win32.System.Com.IBindStatusCallback, pihlNavigate: win32more.Windows.Win32.UI.Shell.IHlink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnNavigate(self, grfHLNF: UInt32, pimkTarget: win32more.Windows.Win32.System.Com.IMoniker, pwzLocation: win32more.Windows.Win32.Foundation.PWSTR, pwzFriendlyName: win32more.Windows.Win32.Foundation.PWSTR, dwreserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UpdateHlink(self, uHLID: UInt32, pimkTarget: win32more.Windows.Win32.System.Com.IMoniker, pwzLocation: win32more.Windows.Win32.Foundation.PWSTR, pwzFriendlyName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHlinkSite(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{79eac9c2-baf9-11ce-8c82-00aa004ba90b}')
    @commethod(3)
    def QueryService(self, dwSiteData: UInt32, guidService: POINTER(Guid), riid: POINTER(Guid), ppiunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMoniker(self, dwSiteData: UInt32, dwAssign: UInt32, dwWhich: UInt32, ppimk: POINTER(win32more.Windows.Win32.System.Com.IMoniker)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ReadyToNavigate(self, dwSiteData: UInt32, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnNavigationComplete(self, dwSiteData: UInt32, dwreserved: UInt32, hrError: win32more.Windows.Win32.Foundation.HRESULT, pwzError: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHlinkTarget(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{79eac9c4-baf9-11ce-8c82-00aa004ba90b}')
    @commethod(3)
    def SetBrowseContext(self, pihlbc: win32more.Windows.Win32.UI.Shell.IHlinkBrowseContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetBrowseContext(self, ppihlbc: POINTER(win32more.Windows.Win32.UI.Shell.IHlinkBrowseContext)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Navigate(self, grfHLNF: UInt32, pwzJumpLocation: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMoniker(self, pwzLocation: win32more.Windows.Win32.Foundation.PWSTR, dwAssign: UInt32, ppimkLocation: POINTER(win32more.Windows.Win32.System.Com.IMoniker)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFriendlyName(self, pwzLocation: win32more.Windows.Win32.Foundation.PWSTR, ppwzFriendlyName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHomeGroup(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7a3bd1d9-35a9-4fb3-a467-f48cac35e2d0}')
    @commethod(3)
    def IsMember(self, member: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ShowSharingWizard(self, owner: win32more.Windows.Win32.Foundation.HWND, sharingchoices: POINTER(win32more.Windows.Win32.UI.Shell.HOMEGROUPSHARINGCHOICES)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IIOCancelInformation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f5b0bf81-8cb5-4b1b-9449-1a159e0c733c}')
    @commethod(3)
    def SetCancelInformation(self, dwThreadID: UInt32, uMsgCancel: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCancelInformation(self, pdwThreadID: POINTER(UInt32), puMsgCancel: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IIdentityName(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IRelatedItem
    _iid_ = Guid('{7d903fca-d6f9-4810-8332-946c0177e247}')
class IImageRecompress(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{505f1513-6b3e-4892-a272-59f8889a4d3e}')
    @commethod(3)
    def RecompressImage(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem, cx: Int32, cy: Int32, iQuality: Int32, pstg: win32more.Windows.Win32.System.Com.StructuredStorage.IStorage, ppstrmOut: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInitializeCommand(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{85075acf-231f-40ea-9610-d26b7b58f638}')
    @commethod(3)
    def Initialize(self, pszCommandName: win32more.Windows.Win32.Foundation.PWSTR, ppb: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInitializeNetworkFolder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6e0f9881-42a8-4f2a-97f8-8af4e026d92d}')
    @commethod(3)
    def Initialize(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pidlTarget: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), uDisplayType: UInt32, pszResName: win32more.Windows.Win32.Foundation.PWSTR, pszProvider: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInitializeObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4622ad16-ff23-11d0-8d34-00a0c90f2719}')
    @commethod(3)
    def Initialize(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInitializeWithBindCtx(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{71c0d2bc-726d-45cc-a6c0-2e31c1db2159}')
    @commethod(3)
    def Initialize(self, pbc: win32more.Windows.Win32.System.Com.IBindCtx) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInitializeWithItem(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7f73be3f-fb79-493c-a6c7-7ee14e245841}')
    @commethod(3)
    def Initialize(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem, grfMode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInitializeWithPropertyStore(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c3e12eb5-7d8d-44f8-b6dd-0e77b34d6de4}')
    @commethod(3)
    def Initialize(self, pps: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInitializeWithWindow(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3e68d4bd-7135-4d10-8018-9fb6d9f33fa1}')
    @commethod(3)
    def Initialize(self, hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInputObject(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{68284faa-6a48-11d0-8c78-00c04fd918b4}')
    @commethod(3)
    def UIActivateIO(self, fActivate: win32more.Windows.Win32.Foundation.BOOL, pMsg: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.MSG)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def HasFocusIO(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def TranslateAcceleratorIO(self, pMsg: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.MSG)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInputObject2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IInputObject
    _iid_ = Guid('{6915c085-510b-44cd-94af-28dfa56cf92b}')
    @commethod(6)
    def TranslateAcceleratorGlobal(self, pMsg: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.MSG)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInputObjectSite(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f1db8392-7331-11d0-8c99-00a0c92dbfe8}')
    @commethod(3)
    def OnFocusChangeIS(self, punkObj: win32more.Windows.Win32.System.Com.IUnknown, fSetFocus: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInputPaneAnimationCoordinator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2af16ba9-2de5-4b75-82d9-01372afbffb4}')
    @commethod(3)
    def AddAnimation(self, device: win32more.Windows.Win32.System.Com.IUnknown, animation: win32more.Windows.Win32.Graphics.DirectComposition.IDCompositionAnimation) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInputPanelConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{41c81592-514c-48bd-a22e-e6af638521a6}')
    @commethod(3)
    def EnableFocusTracking(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInputPanelInvocationConfiguration(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a213f136-3b45-4362-a332-efb6547cd432}')
    @commethod(3)
    def RequireTouchInEditControl(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInsertItem(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d2b57227-3d23-4b95-93c0-492bd454c356}')
    @commethod(3)
    def InsertItem(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IItemNameLimits(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1df0d7f1-b267-4d28-8b10-12e23202a5c4}')
    @commethod(3)
    def GetValidCharacters(self, ppwszValidChars: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ppwszInvalidChars: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMaxLength(self, pszName: win32more.Windows.Win32.Foundation.PWSTR, piMaxNameLen: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IKnownFolder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3aa7af7e-9b36-420c-a8e3-f77d4674a488}')
    @commethod(3)
    def GetId(self, pkfid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetCategory(self, pCategory: POINTER(win32more.Windows.Win32.UI.Shell.KF_CATEGORY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetShellItem(self, dwFlags: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPath(self, dwFlags: UInt32, ppszPath: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetPath(self, dwFlags: UInt32, pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetIDList(self, dwFlags: UInt32, ppidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFolderType(self, pftid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRedirectionCapabilities(self, pCapabilities: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetFolderDefinition(self, pKFD: POINTER(win32more.Windows.Win32.UI.Shell.KNOWNFOLDER_DEFINITION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IKnownFolderManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8be2d872-86aa-4d47-b776-32cca40c7018}')
    @commethod(3)
    def FolderIdFromCsidl(self, nCsidl: Int32, pfid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FolderIdToCsidl(self, rfid: POINTER(Guid), pnCsidl: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFolderIds(self, ppKFId: POINTER(POINTER(Guid)), pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFolder(self, rfid: POINTER(Guid), ppkf: POINTER(win32more.Windows.Win32.UI.Shell.IKnownFolder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFolderByName(self, pszCanonicalName: win32more.Windows.Win32.Foundation.PWSTR, ppkf: POINTER(win32more.Windows.Win32.UI.Shell.IKnownFolder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RegisterFolder(self, rfid: POINTER(Guid), pKFD: POINTER(win32more.Windows.Win32.UI.Shell.KNOWNFOLDER_DEFINITION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def UnregisterFolder(self, rfid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def FindFolderFromPath(self, pszPath: win32more.Windows.Win32.Foundation.PWSTR, mode: win32more.Windows.Win32.UI.Shell.FFFP_MODE, ppkf: POINTER(win32more.Windows.Win32.UI.Shell.IKnownFolder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def FindFolderFromIDList(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), ppkf: POINTER(win32more.Windows.Win32.UI.Shell.IKnownFolder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Redirect(self, rfid: POINTER(Guid), hwnd: win32more.Windows.Win32.Foundation.HWND, flags: UInt32, pszTargetPath: win32more.Windows.Win32.Foundation.PWSTR, cFolders: UInt32, pExclusion: POINTER(Guid), ppszError: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ILaunchSourceAppUserModelId(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{989191ac-28ff-4cf0-9584-e0d078bc2396}')
    @commethod(3)
    def GetAppUserModelId(self, launchingApp: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ILaunchSourceViewSizePreference(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e5aa01f7-1fb8-4830-8720-4e6734cbd5f3}')
    @commethod(3)
    def GetSourceViewToPosition(self, hwnd: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSourceViewSizePreference(self, sourceSizeAfterLaunch: POINTER(win32more.Windows.Win32.UI.Shell.APPLICATION_VIEW_SIZE_PREFERENCE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ILaunchTargetMonitor(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{266fbc7e-490d-46ed-a96b-2274db252003}')
    @commethod(3)
    def GetMonitor(self, monitor: POINTER(win32more.Windows.Win32.Graphics.Gdi.HMONITOR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ILaunchTargetViewSizePreference(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2f0666c6-12f7-4360-b511-a394a0553725}')
    @commethod(3)
    def GetTargetViewSizePreference(self, targetSizeOnLaunch: POINTER(win32more.Windows.Win32.UI.Shell.APPLICATION_VIEW_SIZE_PREFERENCE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ILaunchUIContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1791e8f6-21c7-4340-882a-a6a93e3fd73b}')
    @commethod(3)
    def SetAssociatedWindow(self, value: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetTabGroupingPreference(self, value: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ILaunchUIContextProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0d12c4c8-a3d9-4e24-94c1-0e20c5a956c4}')
    @commethod(3)
    def UpdateContext(self, context: win32more.Windows.Win32.UI.Shell.ILaunchUIContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMenuBand(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{568804cd-cbd7-11d0-9816-00c04fd91972}')
    @commethod(3)
    def IsMenuMessage(self, pmsg: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.MSG)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def TranslateMenuMessage(self, pmsg: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.MSG), plRet: POINTER(win32more.Windows.Win32.Foundation.LRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMenuPopup(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IDeskBar
    _iid_ = Guid('{d1e7afeb-6a2e-11d0-8c78-00c04fd918b4}')
    @commethod(8)
    def Popup(self, ppt: POINTER(win32more.Windows.Win32.Foundation.POINTL), prcExclude: POINTER(win32more.Windows.Win32.Foundation.RECTL), dwFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnSelect(self, dwSelectType: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetSubMenu(self, pmp: win32more.Windows.Win32.UI.Shell.IMenuPopup, fSet: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IModalWindow(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b4db1657-70d7-485e-8e3e-6fcb5a5c1802}')
    @commethod(3)
    def Show(self, hwndOwner: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INameSpaceTreeAccessible(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{71f312de-43ed-4190-8477-e9536b82350b}')
    @commethod(3)
    def OnGetDefaultAccessibilityAction(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem, pbstrDefaultAction: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnDoDefaultAccessibilityAction(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnGetAccessibilityRole(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem, pvarRole: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INameSpaceTreeControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{028212a3-b627-47e9-8856-c14265554e4f}')
    @commethod(3)
    def Initialize(self, hwndParent: win32more.Windows.Win32.Foundation.HWND, prc: POINTER(win32more.Windows.Win32.Foundation.RECT), nsctsFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def TreeAdvise(self, punk: win32more.Windows.Win32.System.Com.IUnknown, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def TreeUnadvise(self, dwCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AppendRoot(self, psiRoot: win32more.Windows.Win32.UI.Shell.IShellItem, grfEnumFlags: UInt32, grfRootStyle: UInt32, pif: win32more.Windows.Win32.UI.Shell.IShellItemFilter) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def InsertRoot(self, iIndex: Int32, psiRoot: win32more.Windows.Win32.UI.Shell.IShellItem, grfEnumFlags: UInt32, grfRootStyle: UInt32, pif: win32more.Windows.Win32.UI.Shell.IShellItemFilter) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveRoot(self, psiRoot: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RemoveAllRoots(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetRootItems(self, ppsiaRootItems: POINTER(win32more.Windows.Win32.UI.Shell.IShellItemArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetItemState(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem, nstcisMask: UInt32, nstcisFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetItemState(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem, nstcisMask: UInt32, pnstcisFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetSelectedItems(self, psiaItems: POINTER(win32more.Windows.Win32.UI.Shell.IShellItemArray)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetItemCustomState(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem, piStateNumber: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetItemCustomState(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem, iStateNumber: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def EnsureItemVisible(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetTheme(self, pszTheme: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetNextItem(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem, nstcgi: win32more.Windows.Win32.UI.Shell.NSTCGNI, ppsiNext: POINTER(win32more.Windows.Win32.UI.Shell.IShellItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def HitTest(self, ppt: POINTER(win32more.Windows.Win32.Foundation.POINT), ppsiOut: POINTER(win32more.Windows.Win32.UI.Shell.IShellItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetItemRect(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem, prect: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def CollapseAll(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INameSpaceTreeControl2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.INameSpaceTreeControl
    _iid_ = Guid('{7cc7aed8-290e-49bc-8945-c1401cc9306c}')
    @commethod(22)
    def SetControlStyle(self, nstcsMask: UInt32, nstcsStyle: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def GetControlStyle(self, nstcsMask: UInt32, pnstcsStyle: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetControlStyle2(self, nstcsMask: win32more.Windows.Win32.UI.Shell.NSTCSTYLE2, nstcsStyle: win32more.Windows.Win32.UI.Shell.NSTCSTYLE2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def GetControlStyle2(self, nstcsMask: win32more.Windows.Win32.UI.Shell.NSTCSTYLE2, pnstcsStyle: POINTER(win32more.Windows.Win32.UI.Shell.NSTCSTYLE2)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INameSpaceTreeControlCustomDraw(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2d3ba758-33ee-42d5-bb7b-5f3431d86c78}')
    @commethod(3)
    def PrePaint(self, hdc: win32more.Windows.Win32.Graphics.Gdi.HDC, prc: POINTER(win32more.Windows.Win32.Foundation.RECT), plres: POINTER(win32more.Windows.Win32.Foundation.LRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PostPaint(self, hdc: win32more.Windows.Win32.Graphics.Gdi.HDC, prc: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ItemPrePaint(self, hdc: win32more.Windows.Win32.Graphics.Gdi.HDC, prc: POINTER(win32more.Windows.Win32.Foundation.RECT), pnstccdItem: POINTER(win32more.Windows.Win32.UI.Shell.NSTCCUSTOMDRAW), pclrText: POINTER(win32more.Windows.Win32.Foundation.COLORREF), pclrTextBk: POINTER(win32more.Windows.Win32.Foundation.COLORREF), plres: POINTER(win32more.Windows.Win32.Foundation.LRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ItemPostPaint(self, hdc: win32more.Windows.Win32.Graphics.Gdi.HDC, prc: POINTER(win32more.Windows.Win32.Foundation.RECT), pnstccdItem: POINTER(win32more.Windows.Win32.UI.Shell.NSTCCUSTOMDRAW)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INameSpaceTreeControlDropHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f9c665d6-c2f2-4c19-bf33-8322d7352f51}')
    @commethod(3)
    def OnDragEnter(self, psiOver: win32more.Windows.Win32.UI.Shell.IShellItem, psiaData: win32more.Windows.Win32.UI.Shell.IShellItemArray, fOutsideSource: win32more.Windows.Win32.Foundation.BOOL, grfKeyState: UInt32, pdwEffect: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnDragOver(self, psiOver: win32more.Windows.Win32.UI.Shell.IShellItem, psiaData: win32more.Windows.Win32.UI.Shell.IShellItemArray, grfKeyState: UInt32, pdwEffect: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnDragPosition(self, psiOver: win32more.Windows.Win32.UI.Shell.IShellItem, psiaData: win32more.Windows.Win32.UI.Shell.IShellItemArray, iNewPosition: Int32, iOldPosition: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnDrop(self, psiOver: win32more.Windows.Win32.UI.Shell.IShellItem, psiaData: win32more.Windows.Win32.UI.Shell.IShellItemArray, iPosition: Int32, grfKeyState: UInt32, pdwEffect: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnDropPosition(self, psiOver: win32more.Windows.Win32.UI.Shell.IShellItem, psiaData: win32more.Windows.Win32.UI.Shell.IShellItemArray, iNewPosition: Int32, iOldPosition: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnDragLeave(self, psiOver: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INameSpaceTreeControlEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{93d77985-b3d8-4484-8318-672cdda002ce}')
    @commethod(3)
    def OnItemClick(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem, nstceHitTest: UInt32, nstceClickType: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnPropertyItemCommit(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnItemStateChanging(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem, nstcisMask: UInt32, nstcisState: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnItemStateChanged(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem, nstcisMask: UInt32, nstcisState: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnSelectionChanged(self, psiaSelection: win32more.Windows.Win32.UI.Shell.IShellItemArray) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnKeyboardInput(self, uMsg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnBeforeExpand(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OnAfterExpand(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def OnBeginLabelEdit(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def OnEndLabelEdit(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def OnGetToolTip(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem, pszTip: win32more.Windows.Win32.Foundation.PWSTR, cchTip: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def OnBeforeItemDelete(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def OnItemAdded(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem, fIsRoot: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def OnItemDeleted(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem, fIsRoot: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def OnBeforeContextMenu(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def OnAfterContextMenu(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem, pcmIn: win32more.Windows.Win32.UI.Shell.IContextMenu, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def OnBeforeStateImageChange(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def OnGetDefaultIconIndex(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem, piDefaultIcon: POINTER(Int32), piOpenIcon: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INameSpaceTreeControlFolderCapabilities(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e9701183-e6b3-4ff2-8568-813615fec7be}')
    @commethod(3)
    def GetFolderCapabilities(self, nfcMask: win32more.Windows.Win32.UI.Shell.NSTCFOLDERCAPABILITIES, pnfcValue: POINTER(win32more.Windows.Win32.UI.Shell.NSTCFOLDERCAPABILITIES)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INamedPropertyBag(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fb700430-952c-11d1-946f-000000000000}')
    @commethod(3)
    def ReadPropertyNPB(self, pszBagname: win32more.Windows.Win32.Foundation.PWSTR, pszPropName: win32more.Windows.Win32.Foundation.PWSTR, pVar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def WritePropertyNPB(self, pszBagname: win32more.Windows.Win32.Foundation.PWSTR, pszPropName: win32more.Windows.Win32.Foundation.PWSTR, pVar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemovePropertyNPB(self, pszBagname: win32more.Windows.Win32.Foundation.PWSTR, pszPropName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INamespaceWalk(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{57ced8a7-3f4a-432c-9350-30f24483f74f}')
    @commethod(3)
    def Walk(self, punkToWalk: win32more.Windows.Win32.System.Com.IUnknown, dwFlags: UInt32, cDepth: Int32, pnswcb: win32more.Windows.Win32.UI.Shell.INamespaceWalkCB) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetIDArrayResult(self, pcItems: POINTER(UInt32), prgpidl: POINTER(POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INamespaceWalkCB(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d92995f8-cf5e-4a76-bf59-ead39ea2b97e}')
    @commethod(3)
    def FoundItem(self, psf: win32more.Windows.Win32.UI.Shell.IShellFolder, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnterFolder(self, psf: win32more.Windows.Win32.UI.Shell.IShellFolder, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def LeaveFolder(self, psf: win32more.Windows.Win32.UI.Shell.IShellFolder, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def InitializeProgressDialog(self, ppszTitle: POINTER(win32more.Windows.Win32.Foundation.PWSTR), ppszCancel: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INamespaceWalkCB2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.INamespaceWalkCB
    _iid_ = Guid('{7ac7492b-c38e-438a-87db-68737844ff70}')
    @commethod(7)
    def WalkComplete(self, hr: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INetworkFolderInternal(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ceb38218-c971-47bb-a703-f0bc99ccdb81}')
    @commethod(3)
    def GetResourceDisplayType(self, displayType: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetIDList(self, idList: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetProvider(self, itemIdCount: UInt32, itemIds: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)), providerMaxLength: UInt32, provider: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INewMenuClient(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dcb07fdc-3bb5-451c-90be-966644fed7b0}')
    @commethod(3)
    def IncludeItems(self, pflags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SelectAndEditItem(self, pidlItem: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), flags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INewShortcutHookA(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{000214e1-0000-0000-c000-000000000046}')
    @commethod(3)
    def SetReferent(self, pcszReferent: win32more.Windows.Win32.Foundation.PSTR, hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetReferent(self, pszReferent: win32more.Windows.Win32.Foundation.PSTR, cchReferent: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetFolder(self, pcszFolder: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFolder(self, pszFolder: win32more.Windows.Win32.Foundation.PSTR, cchFolder: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetName(self, pszName: win32more.Windows.Win32.Foundation.PSTR, cchName: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetExtension(self, pszExtension: win32more.Windows.Win32.Foundation.PSTR, cchExtension: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INewShortcutHookW(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{000214f7-0000-0000-c000-000000000046}')
    @commethod(3)
    def SetReferent(self, pcszReferent: win32more.Windows.Win32.Foundation.PWSTR, hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetReferent(self, pszReferent: win32more.Windows.Win32.Foundation.PWSTR, cchReferent: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetFolder(self, pcszFolder: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFolder(self, pszFolder: win32more.Windows.Win32.Foundation.PWSTR, cchFolder: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetName(self, pszName: win32more.Windows.Win32.Foundation.PWSTR, cchName: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetExtension(self, pszExtension: win32more.Windows.Win32.Foundation.PWSTR, cchExtension: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
INewShortcutHook = UnicodeAlias('INewShortcutHookW')
class INewWDEvents(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IWebWizardHost
    _iid_ = Guid('{0751c551-7568-41c9-8e5b-e22e38919236}')
    @commethod(16)
    def PassportAuthenticate(self, bstrSignInUrl: win32more.Windows.Win32.Foundation.BSTR, pvfAuthenitcated: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INewWindowManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d2bc4c84-3f72-4a52-a604-7bcbf3982cbb}')
    @commethod(3)
    def EvaluateNewWindow(self, pszUrl: win32more.Windows.Win32.Foundation.PWSTR, pszName: win32more.Windows.Win32.Foundation.PWSTR, pszUrlContext: win32more.Windows.Win32.Foundation.PWSTR, pszFeatures: win32more.Windows.Win32.Foundation.PWSTR, fReplace: win32more.Windows.Win32.Foundation.BOOL, dwFlags: UInt32, dwUserActionTime: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class INotifyReplica(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{99180163-da16-101a-935c-444553540000}')
    @commethod(3)
    def YouAreAReplica(self, ulcOtherReplicas: UInt32, rgpmkOtherReplicas: POINTER(win32more.Windows.Win32.System.Com.IMoniker)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IObjMgr(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00bb2761-6a77-11d0-a535-00c04fd7d062}')
    @commethod(3)
    def Append(self, punk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Remove(self, punk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IObjectProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a6087428-3be3-4d73-b308-7c04a540bf1a}')
    @commethod(3)
    def QueryObject(self, guidObject: POINTER(Guid), riid: POINTER(Guid), ppvOut: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IObjectWithAppUserModelID(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{36db0196-9665-46d1-9ba7-d3709eecf9ed}')
    @commethod(3)
    def SetAppID(self, pszAppID: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAppID(self, ppszAppID: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IObjectWithBackReferences(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{321a6a6a-d61f-4bf3-97ae-14be2986bb36}')
    @commethod(3)
    def RemoveBackReferences(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IObjectWithCancelEvent(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f279b885-0ae9-4b85-ac06-ddecf9408941}')
    @commethod(3)
    def GetCancelEvent(self, phEvent: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IObjectWithFolderEnumMode(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6a9d9026-0e6e-464c-b000-42ecc07de673}')
    @commethod(3)
    def SetMode(self, feMode: win32more.Windows.Win32.UI.Shell.FOLDER_ENUM_MODE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMode(self, pfeMode: POINTER(win32more.Windows.Win32.UI.Shell.FOLDER_ENUM_MODE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IObjectWithProgID(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{71e806fb-8dee-46fc-bf8c-7748a8a1ae13}')
    @commethod(3)
    def SetProgID(self, pszProgID: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetProgID(self, ppszProgID: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IObjectWithSelection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1c9cd5bb-98e9-4491-a60f-31aacc72b83c}')
    @commethod(3)
    def SetSelection(self, psia: win32more.Windows.Win32.UI.Shell.IShellItemArray) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSelection(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpenControlPanel(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d11ad862-66de-4df4-bf6c-1f5621996af1}')
    @commethod(3)
    def Open(self, pszName: win32more.Windows.Win32.Foundation.PWSTR, pszPage: win32more.Windows.Win32.Foundation.PWSTR, punkSite: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPath(self, pszName: win32more.Windows.Win32.Foundation.PWSTR, pszPath: win32more.Windows.Win32.Foundation.PWSTR, cchPath: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCurrentView(self, pView: POINTER(win32more.Windows.Win32.UI.Shell.CPVIEW)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpenSearchSource(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f0ee7333-e6fc-479b-9f25-a860c234a38e}')
    @commethod(3)
    def GetResults(self, hwnd: win32more.Windows.Win32.Foundation.HWND, pszQuery: win32more.Windows.Win32.Foundation.PWSTR, dwStartIndex: UInt32, dwCount: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOperationsProgressDialog(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0c9fb851-e5c9-43eb-a370-f0677b13874c}')
    @commethod(3)
    def StartProgressDialog(self, hwndOwner: win32more.Windows.Win32.Foundation.HWND, flags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def StopProgressDialog(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetOperation(self, action: win32more.Windows.Win32.UI.Shell.SPACTION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetMode(self, mode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UpdateProgress(self, ullPointsCurrent: UInt64, ullPointsTotal: UInt64, ullSizeCurrent: UInt64, ullSizeTotal: UInt64, ullItemsCurrent: UInt64, ullItemsTotal: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def UpdateLocations(self, psiSource: win32more.Windows.Win32.UI.Shell.IShellItem, psiTarget: win32more.Windows.Win32.UI.Shell.IShellItem, psiItem: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ResetTimer(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def PauseTimer(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ResumeTimer(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetMilliseconds(self, pullElapsed: POINTER(UInt64), pullRemaining: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetOperationStatus(self, popstatus: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.PDOPSTATUS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPackageDebugSettings(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f27c3930-8029-4ad1-94e3-3dba417810c1}')
    @commethod(3)
    def EnableDebugging(self, packageFullName: win32more.Windows.Win32.Foundation.PWSTR, debuggerCommandLine: win32more.Windows.Win32.Foundation.PWSTR, environment: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DisableDebugging(self, packageFullName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Suspend(self, packageFullName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Resume(self, packageFullName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def TerminateAllProcesses(self, packageFullName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetTargetSessionId(self, sessionId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnumerateBackgroundTasks(self, packageFullName: win32more.Windows.Win32.Foundation.PWSTR, taskCount: POINTER(UInt32), taskIds: POINTER(POINTER(Guid)), taskNames: POINTER(POINTER(win32more.Windows.Win32.Foundation.PWSTR))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ActivateBackgroundTask(self, taskId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def StartServicing(self, packageFullName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def StopServicing(self, packageFullName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def StartSessionRedirection(self, packageFullName: win32more.Windows.Win32.Foundation.PWSTR, sessionId: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def StopSessionRedirection(self, packageFullName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetPackageExecutionState(self, packageFullName: win32more.Windows.Win32.Foundation.PWSTR, packageExecutionState: POINTER(win32more.Windows.Win32.UI.Shell.PACKAGE_EXECUTION_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def RegisterForPackageStateChanges(self, packageFullName: win32more.Windows.Win32.Foundation.PWSTR, pPackageExecutionStateChangeNotification: win32more.Windows.Win32.UI.Shell.IPackageExecutionStateChangeNotification, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def UnregisterForPackageStateChanges(self, dwCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPackageDebugSettings2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IPackageDebugSettings
    _iid_ = Guid('{6e3194bb-ab82-4d22-93f5-fabda40e7b16}')
    @commethod(18)
    def EnumerateApps(self, packageFullName: win32more.Windows.Win32.Foundation.PWSTR, appCount: POINTER(UInt32), appUserModelIds: POINTER(POINTER(win32more.Windows.Win32.Foundation.PWSTR)), appDisplayNames: POINTER(POINTER(win32more.Windows.Win32.Foundation.PWSTR))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPackageExecutionStateChangeNotification(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{1bb12a62-2ad8-432b-8ccf-0c2c52afcd5b}')
    @commethod(3)
    def OnStateChanged(self, pszPackageFullName: win32more.Windows.Win32.Foundation.PWSTR, pesNewState: win32more.Windows.Win32.UI.Shell.PACKAGE_EXECUTION_STATE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IParentAndItem(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b3a4b685-b685-4805-99d9-5dead2873236}')
    @commethod(3)
    def SetParentAndItem(self, pidlParent: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), psf: win32more.Windows.Win32.UI.Shell.IShellFolder, pidlChild: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetParentAndItem(self, ppidlParent: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)), ppsf: POINTER(win32more.Windows.Win32.UI.Shell.IShellFolder), ppidlChild: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IParseAndCreateItem(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{67efed0e-e827-4408-b493-78f3982b685c}')
    @commethod(3)
    def SetItem(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetItem(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPersistFolder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IPersist
    _iid_ = Guid('{000214ea-0000-0000-c000-000000000046}')
    @commethod(4)
    def Initialize(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPersistFolder2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IPersistFolder
    _iid_ = Guid('{1ac3d9f0-175c-11d1-95be-00609797ea4f}')
    @commethod(5)
    def GetCurFolder(self, ppidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPersistFolder3(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IPersistFolder2
    _iid_ = Guid('{cef04fdf-fe72-11d2-87a5-00c04f6837cf}')
    @commethod(6)
    def InitializeEx(self, pbc: win32more.Windows.Win32.System.Com.IBindCtx, pidlRoot: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), ppfti: POINTER(win32more.Windows.Win32.UI.Shell.PERSIST_FOLDER_TARGET_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFolderTargetInfo(self, ppfti: POINTER(win32more.Windows.Win32.UI.Shell.PERSIST_FOLDER_TARGET_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPersistIDList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IPersist
    _iid_ = Guid('{1079acfc-29bd-11d3-8e0d-00c04f6837d5}')
    @commethod(4)
    def SetIDList(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetIDList(self, ppidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPreviewHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8895b1c6-b41f-4c1c-a562-0d564250836f}')
    @commethod(3)
    def SetWindow(self, hwnd: win32more.Windows.Win32.Foundation.HWND, prc: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetRect(self, prc: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DoPreview(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Unload(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetFocus(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def QueryFocus(self, phwnd: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def TranslateAccelerator(self, pmsg: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.MSG)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPreviewHandlerFrame(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fec87aaf-35f9-447a-adb7-20234491401a}')
    @commethod(3)
    def GetWindowContext(self, pinfo: POINTER(win32more.Windows.Win32.UI.Shell.PREVIEWHANDLERFRAMEINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def TranslateAccelerator(self, pmsg: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.MSG)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPreviewHandlerVisuals(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{196bf9a5-b346-4ef0-aa1e-5dcdb76768b1}')
    @commethod(3)
    def SetBackgroundColor(self, color: win32more.Windows.Win32.Foundation.COLORREF) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetFont(self, plf: POINTER(win32more.Windows.Win32.Graphics.Gdi.LOGFONTW)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetTextColor(self, color: win32more.Windows.Win32.Foundation.COLORREF) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPreviewItem(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IRelatedItem
    _iid_ = Guid('{36149969-0a8f-49c8-8b00-4aecb20222fb}')
class IPreviousVersionsInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{76e54780-ad74-48e3-a695-3ba9a0aff10d}')
    @commethod(3)
    def AreSnapshotsAvailable(self, pszPath: win32more.Windows.Win32.Foundation.PWSTR, fOkToBeSlow: win32more.Windows.Win32.Foundation.BOOL, pfAvailable: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProfferService(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cb728b20-f786-11ce-92ad-00aa00a74cd0}')
    @commethod(3)
    def ProfferService(self, serviceId: POINTER(Guid), serviceProvider: win32more.Windows.Win32.System.Com.IServiceProvider, cookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RevokeService(self, cookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IProgressDialog(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ebbc7c04-315e-11d2-b62f-006097df5bd4}')
    @commethod(3)
    def StartProgressDialog(self, hwndParent: win32more.Windows.Win32.Foundation.HWND, punkEnableModless: win32more.Windows.Win32.System.Com.IUnknown, dwFlags: UInt32, pvResevered: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def StopProgressDialog(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetTitle(self, pwzTitle: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetAnimation(self, hInstAnimation: win32more.Windows.Win32.Foundation.HINSTANCE, idAnimation: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def HasUserCancelled(self) -> win32more.Windows.Win32.Foundation.BOOL: ...
    @commethod(8)
    def SetProgress(self, dwCompleted: UInt32, dwTotal: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetProgress64(self, ullCompleted: UInt64, ullTotal: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetLine(self, dwLineNum: UInt32, pwzString: win32more.Windows.Win32.Foundation.PWSTR, fCompactPath: win32more.Windows.Win32.Foundation.BOOL, pvResevered: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetCancelMsg(self, pwzCancelMsg: win32more.Windows.Win32.Foundation.PWSTR, pvResevered: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Timer(self, dwTimerAction: UInt32, pvResevered: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPropertyKeyStore(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{75bd59aa-f23b-4963-aba4-0b355752a91b}')
    @commethod(3)
    def GetKeyCount(self, keyCount: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetKeyAt(self, index: Int32, pkey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AppendKey(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DeleteKey(self, index: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsKeyInStore(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveKey(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPublishedApp(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IShellApp
    _iid_ = Guid('{1bc752e0-9046-11d1-b8b3-006008059382}')
    @commethod(8)
    def Install(self, pstInstall: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetPublishedAppInfo(self, ppai: POINTER(win32more.Windows.Win32.UI.Shell.PUBAPPINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Unschedule(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPublishedApp2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IPublishedApp
    _iid_ = Guid('{12b81347-1b3a-4a04-aa61-3f768b67fd7e}')
    @commethod(11)
    def Install2(self, pstInstall: POINTER(win32more.Windows.Win32.Foundation.SYSTEMTIME), hwndParent: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPublishingWizard(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IWizardExtension
    _iid_ = Guid('{aa9198bb-ccec-472d-beed-19a4f6733f7a}')
    @commethod(6)
    def Initialize(self, pdo: win32more.Windows.Win32.System.Com.IDataObject, dwOptions: UInt32, pszServiceScope: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTransferManifest(self, phrFromTransfer: POINTER(win32more.Windows.Win32.Foundation.HRESULT), pdocManifest: POINTER(win32more.Windows.Win32.Data.Xml.MsXml.IXMLDOMDocument)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IQueryAssociations(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c46ca590-3c3f-11d2-bee6-0000f805ca57}')
    @commethod(3)
    def Init(self, flags: win32more.Windows.Win32.UI.Shell.ASSOCF, pszAssoc: win32more.Windows.Win32.Foundation.PWSTR, hkProgid: win32more.Windows.Win32.System.Registry.HKEY, hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetString(self, flags: win32more.Windows.Win32.UI.Shell.ASSOCF, str: win32more.Windows.Win32.UI.Shell.ASSOCSTR, pszExtra: win32more.Windows.Win32.Foundation.PWSTR, pszOut: win32more.Windows.Win32.Foundation.PWSTR, pcchOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetKey(self, flags: win32more.Windows.Win32.UI.Shell.ASSOCF, key: win32more.Windows.Win32.UI.Shell.ASSOCKEY, pszExtra: win32more.Windows.Win32.Foundation.PWSTR, phkeyOut: POINTER(win32more.Windows.Win32.System.Registry.HKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetData(self, flags: win32more.Windows.Win32.UI.Shell.ASSOCF, data: win32more.Windows.Win32.UI.Shell.ASSOCDATA, pszExtra: win32more.Windows.Win32.Foundation.PWSTR, pvOut: VoidPtr, pcbOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetEnum(self, flags: win32more.Windows.Win32.UI.Shell.ASSOCF, assocenum: win32more.Windows.Win32.UI.Shell.ASSOCENUM, pszExtra: win32more.Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppvOut: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IQueryCancelAutoPlay(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ddefe873-6997-4e68-be26-39b633adbe12}')
    @commethod(3)
    def AllowAutoPlay(self, pszPath: win32more.Windows.Win32.Foundation.PWSTR, dwContentType: UInt32, pszLabel: win32more.Windows.Win32.Foundation.PWSTR, dwSerialNumber: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IQueryCodePage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c7b236ce-ee80-11d0-985f-006008059382}')
    @commethod(3)
    def GetCodePage(self, puiCodePage: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetCodePage(self, uiCodePage: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IQueryContinue(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7307055c-b24a-486b-9f25-163e597a28a9}')
    @commethod(3)
    def QueryContinue(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IQueryContinueWithStatus(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IQueryContinue
    _iid_ = Guid('{9090be5b-502b-41fb-bccc-0049a6c7254b}')
    @commethod(4)
    def SetStatusMessage(self, psz: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IQueryInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00021500-0000-0000-c000-000000000046}')
    @commethod(3)
    def GetInfoTip(self, dwFlags: UInt32, ppwszTip: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetInfoFlags(self, pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRegTreeItem(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a9521922-0812-4d44-9ec3-7fd38c726f3d}')
    @commethod(3)
    def GetCheckState(self, pbCheck: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetCheckState(self, bCheck: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRelatedItem(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a73ce67a-8ab1-44f1-8d43-d2fcbf6b1cd0}')
    @commethod(3)
    def GetItemIDList(self, ppidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetItem(self, ppsi: POINTER(win32more.Windows.Win32.UI.Shell.IShellItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRemoteComputer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{000214fe-0000-0000-c000-000000000046}')
    @commethod(3)
    def Initialize(self, pszMachine: win32more.Windows.Win32.Foundation.PWSTR, bEnumerating: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IResolveShellLink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5cd52983-9449-11d2-963a-00c04f79adf0}')
    @commethod(3)
    def ResolveShellLink(self, punkLink: win32more.Windows.Win32.System.Com.IUnknown, hwnd: win32more.Windows.Win32.Foundation.HWND, fFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IResultsFolder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{96e5ae6d-6ae1-4b1c-900c-c6480eaa8828}')
    @commethod(3)
    def AddItem(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddIDList(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), ppidlAdded: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveItem(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveIDList(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveAll(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRunnableTask(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{85788d00-6807-11d0-b810-00c04fd706ec}')
    @commethod(3)
    def Run(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Kill(self, bWait: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Suspend(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Resume(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsRunning(self) -> UInt32: ...
class IScriptErrorList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{f3470f24-15fd-11d2-bb2e-00805ff7efca}')
    @commethod(7)
    def advanceError(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def retreatError(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def canAdvanceError(self, pfCanAdvance: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def canRetreatError(self, pfCanRetreat: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def getErrorLine(self, plLine: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def getErrorChar(self, plChar: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def getErrorCode(self, plCode: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def getErrorMsg(self, pstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def getErrorUrl(self, pstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def getAlwaysShowLockState(self, pfAlwaysShowLocked: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def getDetailsPaneOpen(self, pfDetailsPaneOpen: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def setDetailsPaneOpen(self, fDetailsPaneOpen: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def getPerErrorDisplay(self, pfPerErrorDisplay: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def setPerErrorDisplay(self, fPerErrorDisplay: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISearchBoxInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6af6e03f-d664-4ef4-9626-f7e0ed36755e}')
    @commethod(3)
    def GetCondition(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetText(self, ppsz: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISearchContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{09f656a2-41af-480c-88f7-16cc0d164615}')
    @commethod(3)
    def GetSearchUrl(self, pbstrSearchUrl: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSearchText(self, pbstrSearchText: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSearchStyle(self, pdwSearchStyle: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISearchFolderItemFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a0ffbc28-5482-4366-be27-3e81e78e06c2}')
    @commethod(3)
    def SetDisplayName(self, pszDisplayName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetFolderTypeID(self, ftid: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetFolderLogicalViewMode(self, flvm: win32more.Windows.Win32.UI.Shell.FOLDERLOGICALVIEWMODE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetIconSize(self, iIconSize: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetVisibleColumns(self, cVisibleColumns: UInt32, rgKey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetSortColumns(self, cSortColumns: UInt32, rgSortColumns: POINTER(win32more.Windows.Win32.UI.Shell.SORTCOLUMN)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetGroupColumn(self, keyGroup: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetStacks(self, cStackKeys: UInt32, rgStackKeys: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetScope(self, psiaScope: win32more.Windows.Win32.UI.Shell.IShellItemArray) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetCondition(self, pCondition: win32more.Windows.Win32.System.Search.ICondition) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetShellItem(self, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetIDList(self, ppidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISharedBitmap(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{091162a4-bc96-411f-aae8-c5122cd03363}')
    @commethod(3)
    def GetSharedBitmap(self, phbm: POINTER(win32more.Windows.Win32.Graphics.Gdi.HBITMAP)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSize(self, pSize: POINTER(win32more.Windows.Win32.Foundation.SIZE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFormat(self, pat: POINTER(win32more.Windows.Win32.UI.Shell.WTS_ALPHATYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def InitializeBitmap(self, hbm: win32more.Windows.Win32.Graphics.Gdi.HBITMAP, wtsAT: win32more.Windows.Win32.UI.Shell.WTS_ALPHATYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Detach(self, phbm: POINTER(win32more.Windows.Win32.Graphics.Gdi.HBITMAP)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISharingConfigurationManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b4cd448a-9c86-4466-9201-2e62105b87ae}')
    @commethod(3)
    def CreateShare(self, dsid: win32more.Windows.Win32.UI.Shell.DEF_SHARE_ID, role: win32more.Windows.Win32.UI.Shell.SHARE_ROLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DeleteShare(self, dsid: win32more.Windows.Win32.UI.Shell.DEF_SHARE_ID) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ShareExists(self, dsid: win32more.Windows.Win32.UI.Shell.DEF_SHARE_ID) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSharePermissions(self, dsid: win32more.Windows.Win32.UI.Shell.DEF_SHARE_ID, pRole: POINTER(win32more.Windows.Win32.UI.Shell.SHARE_ROLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SharePrinters(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def StopSharingPrinters(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ArePrintersShared(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellApp(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a3e14960-935f-11d1-b8b8-006008059382}')
    @commethod(3)
    def GetAppInfo(self, pai: POINTER(win32more.Windows.Win32.UI.Shell.APPINFODATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPossibleActions(self, pdwActions: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSlowAppInfo(self, psaid: POINTER(win32more.Windows.Win32.UI.Shell.SLOWAPPINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCachedSlowAppInfo(self, psaid: POINTER(win32more.Windows.Win32.UI.Shell.SLOWAPPINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsInstalled(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellBrowser(ComPtr):
    extends: win32more.Windows.Win32.System.Ole.IOleWindow
    _iid_ = Guid('{000214e2-0000-0000-c000-000000000046}')
    @commethod(5)
    def InsertMenusSB(self, hmenuShared: win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU, lpMenuWidths: POINTER(win32more.Windows.Win32.System.Ole.OLEMENUGROUPWIDTHS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetMenuSB(self, hmenuShared: win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU, holemenuRes: IntPtr, hwndActiveObject: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def RemoveMenusSB(self, hmenuShared: win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetStatusTextSB(self, pszStatusText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnableModelessSB(self, fEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def TranslateAcceleratorSB(self, pmsg: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.MSG), wID: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def BrowseObject(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), wFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetViewStateStream(self, grfMode: UInt32, ppStrm: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetControlWindow(self, id: UInt32, phwnd: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SendControlMsg(self, id: UInt32, uMsg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM, pret: POINTER(win32more.Windows.Win32.Foundation.LRESULT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def QueryActiveShellView(self, ppshv: POINTER(win32more.Windows.Win32.UI.Shell.IShellView)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def OnViewWindowActive(self, pshv: win32more.Windows.Win32.UI.Shell.IShellView) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetToolbarItems(self, lpButtons: POINTER(win32more.Windows.Win32.UI.Controls.TBBUTTON), nButtons: UInt32, uFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellChangeNotify(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d82be2b1-5764-11d0-a96e-00c04fd705a2}')
    @commethod(3)
    def OnChange(self, lEvent: Int32, pidl1: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pidl2: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellDetails(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{000214ec-0000-0000-c000-000000000046}')
    @commethod(3)
    def GetDetailsOf(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), iColumn: UInt32, pDetails: POINTER(win32more.Windows.Win32.UI.Shell.Common.SHELLDETAILS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ColumnClick(self, iColumn: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellDispatch(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{d8f015c0-c278-11ce-a49e-444553540000}')
    @commethod(7)
    def get_Application(self, ppid: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Parent(self, ppid: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def NameSpace(self, vDir: win32more.Windows.Win32.System.Variant.VARIANT, ppsdf: POINTER(win32more.Windows.Win32.UI.Shell.Folder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def BrowseForFolder(self, Hwnd: Int32, Title: win32more.Windows.Win32.Foundation.BSTR, Options: Int32, RootFolder: win32more.Windows.Win32.System.Variant.VARIANT, ppsdf: POINTER(win32more.Windows.Win32.UI.Shell.Folder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Windows(self, ppid: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Open(self, vDir: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Explore(self, vDir: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def MinimizeAll(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def UndoMinimizeALL(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def FileRun(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def CascadeWindows(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def TileVertically(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def TileHorizontally(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def ShutdownWindows(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def Suspend(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def EjectPC(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetTime(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def TrayProperties(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def Help(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def FindFiles(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def FindComputer(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def RefreshMenu(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def ControlPanelItem(self, bstrDir: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellDispatch2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IShellDispatch
    _iid_ = Guid('{a4c6892c-3ba9-11d2-9dea-00c04fb16162}')
    @commethod(30)
    def IsRestricted(self, Group: win32more.Windows.Win32.Foundation.BSTR, Restriction: win32more.Windows.Win32.Foundation.BSTR, plRestrictValue: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def ShellExecute(self, File: win32more.Windows.Win32.Foundation.BSTR, vArgs: win32more.Windows.Win32.System.Variant.VARIANT, vDir: win32more.Windows.Win32.System.Variant.VARIANT, vOperation: win32more.Windows.Win32.System.Variant.VARIANT, vShow: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def FindPrinter(self, name: win32more.Windows.Win32.Foundation.BSTR, location: win32more.Windows.Win32.Foundation.BSTR, model: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def GetSystemInformation(self, name: win32more.Windows.Win32.Foundation.BSTR, pv: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def ServiceStart(self, ServiceName: win32more.Windows.Win32.Foundation.BSTR, Persistent: win32more.Windows.Win32.System.Variant.VARIANT, pSuccess: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def ServiceStop(self, ServiceName: win32more.Windows.Win32.Foundation.BSTR, Persistent: win32more.Windows.Win32.System.Variant.VARIANT, pSuccess: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def IsServiceRunning(self, ServiceName: win32more.Windows.Win32.Foundation.BSTR, pRunning: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def CanStartStopService(self, ServiceName: win32more.Windows.Win32.Foundation.BSTR, pCanStartStop: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def ShowBrowserBar(self, bstrClsid: win32more.Windows.Win32.Foundation.BSTR, bShow: win32more.Windows.Win32.System.Variant.VARIANT, pSuccess: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellDispatch3(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IShellDispatch2
    _iid_ = Guid('{177160ca-bb5a-411c-841d-bd38facdeaa0}')
    @commethod(39)
    def AddToRecent(self, varFile: win32more.Windows.Win32.System.Variant.VARIANT, bstrCategory: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellDispatch4(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IShellDispatch3
    _iid_ = Guid('{efd84b2d-4bcf-4298-be25-eb542a59fbda}')
    @commethod(40)
    def WindowsSecurity(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def ToggleDesktop(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def ExplorerPolicy(self, bstrPolicyName: win32more.Windows.Win32.Foundation.BSTR, pValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def GetSetting(self, lSetting: Int32, pResult: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellDispatch5(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IShellDispatch4
    _iid_ = Guid('{866738b9-6cf2-4de8-8767-f794ebe74f4e}')
    @commethod(44)
    def WindowSwitcher(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellDispatch6(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IShellDispatch5
    _iid_ = Guid('{286e6f1b-7113-4355-9562-96b7e9d64c54}')
    @commethod(45)
    def SearchCommand(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellExtInit(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{000214e8-0000-0000-c000-000000000046}')
    @commethod(3)
    def Initialize(self, pidlFolder: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pdtobj: win32more.Windows.Win32.System.Com.IDataObject, hkeyProgID: win32more.Windows.Win32.System.Registry.HKEY) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellFavoritesNameSpace(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{55136804-b2de-11d1-b9f2-00a0c98bc547}')
    @commethod(7)
    def MoveSelectionUp(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def MoveSelectionDown(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ResetSort(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def NewFolder(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Synchronize(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Import(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Export(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def InvokeContextMenuCommand(self, strCommand: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def MoveSelectionTo(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_SubscriptionsEnabled(self, pBool: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def CreateSubscriptionForSelection(self, pBool: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def DeleteSubscriptionForSelection(self, pBool: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetRoot(self, bstrFullPath: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellFolder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{000214e6-0000-0000-c000-000000000046}')
    @commethod(3)
    def ParseDisplayName(self, hwnd: win32more.Windows.Win32.Foundation.HWND, pbc: win32more.Windows.Win32.System.Com.IBindCtx, pszDisplayName: win32more.Windows.Win32.Foundation.PWSTR, pchEaten: POINTER(UInt32), ppidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)), pdwAttributes: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnumObjects(self, hwnd: win32more.Windows.Win32.Foundation.HWND, grfFlags: UInt32, ppenumIDList: POINTER(win32more.Windows.Win32.UI.Shell.IEnumIDList)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def BindToObject(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pbc: win32more.Windows.Win32.System.Com.IBindCtx, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def BindToStorage(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pbc: win32more.Windows.Win32.System.Com.IBindCtx, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CompareIDs(self, lParam: win32more.Windows.Win32.Foundation.LPARAM, pidl1: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pidl2: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreateViewObject(self, hwndOwner: win32more.Windows.Win32.Foundation.HWND, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetAttributesOf(self, cidl: UInt32, apidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)), rgfInOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetUIObjectOf(self, hwndOwner: win32more.Windows.Win32.Foundation.HWND, cidl: UInt32, apidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)), riid: POINTER(Guid), rgfReserved: POINTER(UInt32), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetDisplayNameOf(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), uFlags: win32more.Windows.Win32.UI.Shell.SHGDNF, pName: POINTER(win32more.Windows.Win32.UI.Shell.Common.STRRET)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetNameOf(self, hwnd: win32more.Windows.Win32.Foundation.HWND, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pszName: win32more.Windows.Win32.Foundation.PWSTR, uFlags: win32more.Windows.Win32.UI.Shell.SHGDNF, ppidlOut: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellFolder2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IShellFolder
    _iid_ = Guid('{93f2f68c-1d1b-11d3-a30e-00c04f79abd1}')
    @commethod(13)
    def GetDefaultSearchGUID(self, pguid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def EnumSearches(self, ppenum: POINTER(win32more.Windows.Win32.UI.Shell.IEnumExtraSearch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetDefaultColumn(self, dwRes: UInt32, pSort: POINTER(UInt32), pDisplay: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetDefaultColumnState(self, iColumn: UInt32, pcsFlags: POINTER(win32more.Windows.Win32.UI.Shell.Common.SHCOLSTATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetDetailsEx(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pscid: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pv: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetDetailsOf(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), iColumn: UInt32, psd: POINTER(win32more.Windows.Win32.UI.Shell.Common.SHELLDETAILS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def MapColumnToSCID(self, iColumn: UInt32, pscid: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellFolderBand(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7fe80cc8-c247-11d0-b93a-00a0c90312e1}')
    @commethod(3)
    def InitializeSFB(self, psf: win32more.Windows.Win32.UI.Shell.IShellFolder, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetBandInfoSFB(self, pbi: POINTER(win32more.Windows.Win32.UI.Shell.BANDINFOSFB)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetBandInfoSFB(self, pbi: POINTER(win32more.Windows.Win32.UI.Shell.BANDINFOSFB)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellFolderView(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{37a378c0-f82d-11ce-ae65-08002b2e1262}')
    @commethod(3)
    def Rearrange(self, lParamSort: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetArrangeParam(self, plParamSort: POINTER(win32more.Windows.Win32.Foundation.LPARAM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ArrangeGrid(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AutoArrange(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetAutoArrange(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AddObject(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), puItem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetObject(self, ppidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)), uItem: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RemoveObject(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), puItem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetObjectCount(self, puCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetObjectCount(self, uCount: UInt32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def UpdateObject(self, pidlOld: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pidlNew: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), puItem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def RefreshObject(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), puItem: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetRedraw(self, bRedraw: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetSelectedCount(self, puSelected: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetSelectedObjects(self, pppidl: POINTER(POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST))), puItems: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def IsDropOnSource(self, pDropTarget: win32more.Windows.Win32.System.Ole.IDropTarget) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetDragPoint(self, ppt: POINTER(win32more.Windows.Win32.Foundation.POINT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetDropPoint(self, ppt: POINTER(win32more.Windows.Win32.Foundation.POINT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def MoveIcons(self, pDataObject: win32more.Windows.Win32.System.Com.IDataObject) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SetItemPos(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), ppt: POINTER(win32more.Windows.Win32.Foundation.POINT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def IsBkDropTarget(self, pDropTarget: win32more.Windows.Win32.System.Ole.IDropTarget) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SetClipboard(self, bMove: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def SetPoints(self, pDataObject: win32more.Windows.Win32.System.Com.IDataObject) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def GetItemSpacing(self, pSpacing: POINTER(win32more.Windows.Win32.UI.Shell.ITEMSPACING)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SetCallback(self, pNewCB: win32more.Windows.Win32.UI.Shell.IShellFolderViewCB, ppOldCB: POINTER(win32more.Windows.Win32.UI.Shell.IShellFolderViewCB)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def Select(self, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def QuerySupport(self, pdwSupport: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def SetAutomationObject(self, pdisp: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellFolderViewCB(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2047e320-f2a9-11ce-ae65-08002b2e1262}')
    @commethod(3)
    def MessageSFVCB(self, uMsg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellFolderViewDual(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{e7a1af80-4d96-11cf-960c-0080c7f4ee85}')
    @commethod(7)
    def get_Application(self, ppid: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Parent(self, ppid: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Folder(self, ppid: POINTER(win32more.Windows.Win32.UI.Shell.Folder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SelectedItems(self, ppid: POINTER(win32more.Windows.Win32.UI.Shell.FolderItems)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_FocusedItem(self, ppid: POINTER(win32more.Windows.Win32.UI.Shell.FolderItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SelectItem(self, pvfi: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), dwFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def PopupItemMenu(self, pfi: win32more.Windows.Win32.UI.Shell.FolderItem, vx: win32more.Windows.Win32.System.Variant.VARIANT, vy: win32more.Windows.Win32.System.Variant.VARIANT, pbs: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_Script(self, ppDisp: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_ViewOptions(self, plViewOptions: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellFolderViewDual2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IShellFolderViewDual
    _iid_ = Guid('{31c147b6-0ade-4a3c-b514-ddf932ef6d17}')
    @commethod(16)
    def get_CurrentViewMode(self, pViewMode: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_CurrentViewMode(self, ViewMode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SelectItemRelative(self, iRelative: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellFolderViewDual3(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IShellFolderViewDual2
    _iid_ = Guid('{29ec8e6c-46d3-411f-baaa-611a6c9cac66}')
    @commethod(19)
    def get_GroupBy(self, pbstrGroupBy: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_GroupBy(self, bstrGroupBy: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_FolderFlags(self, pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_FolderFlags(self, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_SortColumns(self, pbstrSortColumns: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_SortColumns(self, bstrSortColumns: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_IconSize(self, iIconSize: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_IconSize(self, piIconSize: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def FilterView(self, bstrFilterText: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellIcon(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{000214e5-0000-0000-c000-000000000046}')
    @commethod(3)
    def GetIconOf(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), flags: UInt32, pIconIndex: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellIconOverlay(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7d688a70-c613-11d0-999b-00c04fd655e1}')
    @commethod(3)
    def GetOverlayIndex(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pIndex: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetOverlayIconIndex(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pIconIndex: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellIconOverlayIdentifier(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0c6c4200-c589-11d0-999a-00c04fd655e1}')
    @commethod(3)
    def IsMemberOf(self, pwszPath: win32more.Windows.Win32.Foundation.PWSTR, dwAttrib: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetOverlayInfo(self, pwszIconFile: win32more.Windows.Win32.Foundation.PWSTR, cchMax: Int32, pIndex: POINTER(Int32), pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPriority(self, pPriority: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellIconOverlayManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f10b5e34-dd3b-42a7-aa7d-2f4ec54bb09b}')
    @commethod(3)
    def GetFileOverlayInfo(self, pwszPath: win32more.Windows.Win32.Foundation.PWSTR, dwAttrib: UInt32, pIndex: POINTER(Int32), dwflags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetReservedOverlayInfo(self, pwszPath: win32more.Windows.Win32.Foundation.PWSTR, dwAttrib: UInt32, pIndex: POINTER(Int32), dwflags: UInt32, iReservedID: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RefreshOverlayImages(self, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def LoadNonloadedOverlayIdentifiers(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OverlayIndexFromImageIndex(self, iImage: Int32, piIndex: POINTER(Int32), fAdd: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellImageData(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bfdeec12-8040-4403-a5ea-9e07dafcf530}')
    @commethod(3)
    def Decode(self, dwFlags: UInt32, cxDesired: UInt32, cyDesired: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Draw(self, hdc: win32more.Windows.Win32.Graphics.Gdi.HDC, prcDest: POINTER(win32more.Windows.Win32.Foundation.RECT), prcSrc: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def NextFrame(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def NextPage(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def PrevPage(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsTransparent(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def IsAnimated(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IsVector(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def IsMultipage(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def IsEditable(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def IsPrintable(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def IsDecoded(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetCurrentPage(self, pnPage: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetPageCount(self, pcPages: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SelectPage(self, iPage: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetSize(self, pSize: POINTER(win32more.Windows.Win32.Foundation.SIZE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetRawDataFormat(self, pDataFormat: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetPixelFormat(self, pFormat: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetDelay(self, pdwDelay: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetProperties(self, dwMode: UInt32, ppPropSet: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.IPropertySetStorage)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Rotate(self, dwAngle: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def Scale(self, cx: UInt32, cy: UInt32, hints: win32more.Windows.Win32.Graphics.GdiPlus.InterpolationMode) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def DiscardEdit(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def SetEncoderParams(self, pbagEnc: win32more.Windows.Win32.System.Com.StructuredStorage.IPropertyBag) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def DisplayName(self, wszName: win32more.Windows.Win32.Foundation.PWSTR, cch: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def GetResolution(self, puResolutionX: POINTER(UInt32), puResolutionY: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def GetEncoderParams(self, pguidFmt: POINTER(Guid), ppEncParams: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def RegisterAbort(self, pAbort: win32more.Windows.Win32.UI.Shell.IShellImageDataAbort, ppAbortPrev: POINTER(win32more.Windows.Win32.UI.Shell.IShellImageDataAbort)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def CloneFrame(self, ppImg: POINTER(POINTER(Byte))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def ReplaceFrame(self, pImg: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellImageDataAbort(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{53fb8e58-50c0-4003-b4aa-0c8df28e7f3a}')
    @commethod(3)
    def QueryAbort(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellImageDataFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9be8ed5c-edab-4d75-90f3-bd5bdbb21c82}')
    @commethod(3)
    def CreateIShellImageData(self, ppshimg: POINTER(win32more.Windows.Win32.UI.Shell.IShellImageData)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateImageFromFile(self, pszPath: win32more.Windows.Win32.Foundation.PWSTR, ppshimg: POINTER(win32more.Windows.Win32.UI.Shell.IShellImageData)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateImageFromStream(self, pStream: win32more.Windows.Win32.System.Com.IStream, ppshimg: POINTER(win32more.Windows.Win32.UI.Shell.IShellImageData)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDataFormatFromPath(self, pszPath: win32more.Windows.Win32.Foundation.PWSTR, pDataFormat: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellItem(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{43826d1e-e718-42ee-bc55-a1e261c37bfe}')
    @commethod(3)
    def BindToHandler(self, pbc: win32more.Windows.Win32.System.Com.IBindCtx, bhid: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetParent(self, ppsi: POINTER(win32more.Windows.Win32.UI.Shell.IShellItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDisplayName(self, sigdnName: win32more.Windows.Win32.UI.Shell.SIGDN, ppszName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetAttributes(self, sfgaoMask: win32more.Windows.Win32.System.SystemServices.SFGAO_FLAGS, psfgaoAttribs: POINTER(win32more.Windows.Win32.System.SystemServices.SFGAO_FLAGS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Compare(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem, hint: UInt32, piOrder: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellItem2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IShellItem
    _iid_ = Guid('{7e9fb0d3-919f-4307-ab2e-9b1860310c93}')
    @commethod(8)
    def GetPropertyStore(self, flags: win32more.Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetPropertyStoreWithCreateObject(self, flags: win32more.Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS, punkCreateObject: win32more.Windows.Win32.System.Com.IUnknown, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetPropertyStoreForKeys(self, rgKeys: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), cKeys: UInt32, flags: win32more.Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetPropertyDescriptionList(self, keyType: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Update(self, pbc: win32more.Windows.Win32.System.Com.IBindCtx) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetProperty(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetCLSID(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetFileTime(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pft: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetInt32(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pi: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetString(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), ppsz: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetUInt32(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pui: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetUInt64(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pull: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetBool(self, key: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), pf: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellItemArray(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b63ea76d-1f85-456f-a19c-48159efa858b}')
    @commethod(3)
    def BindToHandler(self, pbc: win32more.Windows.Win32.System.Com.IBindCtx, bhid: POINTER(Guid), riid: POINTER(Guid), ppvOut: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPropertyStore(self, flags: win32more.Windows.Win32.UI.Shell.PropertiesSystem.GETPROPERTYSTOREFLAGS, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPropertyDescriptionList(self, keyType: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetAttributes(self, AttribFlags: win32more.Windows.Win32.UI.Shell.SIATTRIBFLAGS, sfgaoMask: win32more.Windows.Win32.System.SystemServices.SFGAO_FLAGS, psfgaoAttribs: POINTER(win32more.Windows.Win32.System.SystemServices.SFGAO_FLAGS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCount(self, pdwNumItems: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetItemAt(self, dwIndex: UInt32, ppsi: POINTER(win32more.Windows.Win32.UI.Shell.IShellItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EnumItems(self, ppenumShellItems: POINTER(win32more.Windows.Win32.UI.Shell.IEnumShellItems)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellItemFilter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2659b475-eeb8-48b7-8f07-b378810f48cf}')
    @commethod(3)
    def IncludeItem(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetEnumFlagsForItem(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem, pgrfFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellItemImageFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bcc18b79-ba16-442f-80c4-8a59c30c463b}')
    @commethod(3)
    def GetImage(self, size: win32more.Windows.Win32.Foundation.SIZE, flags: win32more.Windows.Win32.UI.Shell.SIIGBF, phbm: POINTER(win32more.Windows.Win32.Graphics.Gdi.HBITMAP)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellItemResources(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ff5693be-2ce0-4d48-b5c5-40817d1acdb9}')
    @commethod(3)
    def GetAttributes(self, pdwAttributes: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSize(self, pullSize: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetTimes(self, pftCreation: POINTER(win32more.Windows.Win32.Foundation.FILETIME), pftWrite: POINTER(win32more.Windows.Win32.Foundation.FILETIME), pftAccess: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetTimes(self, pftCreation: POINTER(win32more.Windows.Win32.Foundation.FILETIME), pftWrite: POINTER(win32more.Windows.Win32.Foundation.FILETIME), pftAccess: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetResourceDescription(self, pcsir: POINTER(win32more.Windows.Win32.UI.Shell.SHELL_ITEM_RESOURCE), ppszDescription: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def EnumResources(self, ppenumr: POINTER(win32more.Windows.Win32.UI.Shell.IEnumResources)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SupportsResource(self, pcsir: POINTER(win32more.Windows.Win32.UI.Shell.SHELL_ITEM_RESOURCE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def OpenResource(self, pcsir: POINTER(win32more.Windows.Win32.UI.Shell.SHELL_ITEM_RESOURCE), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CreateResource(self, pcsir: POINTER(win32more.Windows.Win32.UI.Shell.SHELL_ITEM_RESOURCE), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def MarkForDelete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellLibrary(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{11a66efa-382e-451a-9234-1e0e12ef3085}')
    @commethod(3)
    def LoadLibraryFromItem(self, psiLibrary: win32more.Windows.Win32.UI.Shell.IShellItem, grfMode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def LoadLibraryFromKnownFolder(self, kfidLibrary: POINTER(Guid), grfMode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def AddFolder(self, psiLocation: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveFolder(self, psiLocation: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFolders(self, lff: win32more.Windows.Win32.UI.Shell.LIBRARYFOLDERFILTER, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ResolveFolder(self, psiFolderToResolve: win32more.Windows.Win32.UI.Shell.IShellItem, dwTimeout: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetDefaultSaveFolder(self, dsft: win32more.Windows.Win32.UI.Shell.DEFAULTSAVEFOLDERTYPE, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetDefaultSaveFolder(self, dsft: win32more.Windows.Win32.UI.Shell.DEFAULTSAVEFOLDERTYPE, psi: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetOptions(self, plofOptions: POINTER(win32more.Windows.Win32.UI.Shell.LIBRARYOPTIONFLAGS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetOptions(self, lofMask: win32more.Windows.Win32.UI.Shell.LIBRARYOPTIONFLAGS, lofOptions: win32more.Windows.Win32.UI.Shell.LIBRARYOPTIONFLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetFolderType(self, pftid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetFolderType(self, ftid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetIcon(self, ppszIcon: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetIcon(self, pszIcon: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Commit(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def Save(self, psiFolderToSaveIn: win32more.Windows.Win32.UI.Shell.IShellItem, pszLibraryName: win32more.Windows.Win32.Foundation.PWSTR, lsf: win32more.Windows.Win32.UI.Shell.LIBRARYSAVEFLAGS, ppsiSavedTo: POINTER(win32more.Windows.Win32.UI.Shell.IShellItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SaveInKnownFolder(self, kfidToSaveIn: POINTER(Guid), pszLibraryName: win32more.Windows.Win32.Foundation.PWSTR, lsf: win32more.Windows.Win32.UI.Shell.LIBRARYSAVEFLAGS, ppsiSavedTo: POINTER(win32more.Windows.Win32.UI.Shell.IShellItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellLinkA(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{000214ee-0000-0000-c000-000000000046}')
    @commethod(3)
    def GetPath(self, pszFile: win32more.Windows.Win32.Foundation.PSTR, cch: Int32, pfd: POINTER(win32more.Windows.Win32.Storage.FileSystem.WIN32_FIND_DATAA), fFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetIDList(self, ppidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetIDList(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDescription(self, pszName: win32more.Windows.Win32.Foundation.PSTR, cch: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetDescription(self, pszName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetWorkingDirectory(self, pszDir: win32more.Windows.Win32.Foundation.PSTR, cch: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetWorkingDirectory(self, pszDir: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetArguments(self, pszArgs: win32more.Windows.Win32.Foundation.PSTR, cch: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetArguments(self, pszArgs: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetHotkey(self, pwHotkey: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetHotkey(self, wHotkey: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetShowCmd(self, piShowCmd: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.SHOW_WINDOW_CMD)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetShowCmd(self, iShowCmd: win32more.Windows.Win32.UI.WindowsAndMessaging.SHOW_WINDOW_CMD) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetIconLocation(self, pszIconPath: win32more.Windows.Win32.Foundation.PSTR, cch: Int32, piIcon: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetIconLocation(self, pszIconPath: win32more.Windows.Win32.Foundation.PSTR, iIcon: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetRelativePath(self, pszPathRel: win32more.Windows.Win32.Foundation.PSTR, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Resolve(self, hwnd: win32more.Windows.Win32.Foundation.HWND, fFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetPath(self, pszFile: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellLinkDataList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{45e2b4ae-b1c3-11d0-b92f-00a0c90312e1}')
    @commethod(3)
    def AddDataBlock(self, pDataBlock: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CopyDataBlock(self, dwSig: UInt32, ppDataBlock: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveDataBlock(self, dwSig: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetFlags(self, pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetFlags(self, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellLinkDual(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{88a05c00-f000-11ce-8350-444553540000}')
    @commethod(7)
    def get_Path(self, pbs: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Path(self, bs: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Description(self, pbs: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Description(self, bs: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_WorkingDirectory(self, pbs: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_WorkingDirectory(self, bs: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Arguments(self, pbs: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Arguments(self, bs: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Hotkey(self, piHK: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Hotkey(self, iHK: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_ShowCommand(self, piShowCommand: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_ShowCommand(self, iShowCommand: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Resolve(self, fFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetIconLocation(self, pbs: POINTER(win32more.Windows.Win32.Foundation.BSTR), piIcon: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def SetIconLocation(self, bs: win32more.Windows.Win32.Foundation.BSTR, iIcon: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def Save(self, vWhere: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellLinkDual2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IShellLinkDual
    _iid_ = Guid('{317ee249-f12e-11d2-b1e4-00c04f8eeb3e}')
    @commethod(23)
    def get_Target(self, ppfi: POINTER(win32more.Windows.Win32.UI.Shell.FolderItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellLinkW(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{000214f9-0000-0000-c000-000000000046}')
    @commethod(3)
    def GetPath(self, pszFile: win32more.Windows.Win32.Foundation.PWSTR, cch: Int32, pfd: POINTER(win32more.Windows.Win32.Storage.FileSystem.WIN32_FIND_DATAW), fFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetIDList(self, ppidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetIDList(self, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetDescription(self, pszName: win32more.Windows.Win32.Foundation.PWSTR, cch: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetDescription(self, pszName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetWorkingDirectory(self, pszDir: win32more.Windows.Win32.Foundation.PWSTR, cch: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetWorkingDirectory(self, pszDir: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetArguments(self, pszArgs: win32more.Windows.Win32.Foundation.PWSTR, cch: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetArguments(self, pszArgs: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetHotkey(self, pwHotkey: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetHotkey(self, wHotkey: UInt16) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetShowCmd(self, piShowCmd: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.SHOW_WINDOW_CMD)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetShowCmd(self, iShowCmd: win32more.Windows.Win32.UI.WindowsAndMessaging.SHOW_WINDOW_CMD) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetIconLocation(self, pszIconPath: win32more.Windows.Win32.Foundation.PWSTR, cch: Int32, piIcon: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def SetIconLocation(self, pszIconPath: win32more.Windows.Win32.Foundation.PWSTR, iIcon: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetRelativePath(self, pszPathRel: win32more.Windows.Win32.Foundation.PWSTR, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def Resolve(self, hwnd: win32more.Windows.Win32.Foundation.HWND, fFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetPath(self, pszFile: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
IShellLink = UnicodeAlias('IShellLinkW')
class IShellMenu(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ee1f7637-e138-11d1-8379-00c04fd918d0}')
    @commethod(3)
    def Initialize(self, psmc: win32more.Windows.Win32.UI.Shell.IShellMenuCallback, uId: UInt32, uIdAncestor: UInt32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMenuInfo(self, ppsmc: POINTER(win32more.Windows.Win32.UI.Shell.IShellMenuCallback), puId: POINTER(UInt32), puIdAncestor: POINTER(UInt32), pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetShellFolder(self, psf: win32more.Windows.Win32.UI.Shell.IShellFolder, pidlFolder: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), hKey: win32more.Windows.Win32.System.Registry.HKEY, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetShellFolder(self, pdwFlags: POINTER(UInt32), ppidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetMenu(self, hmenu: win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU, hwnd: win32more.Windows.Win32.Foundation.HWND, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetMenu(self, phmenu: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU), phwnd: POINTER(win32more.Windows.Win32.Foundation.HWND), pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def InvalidateItem(self, psmd: POINTER(win32more.Windows.Win32.UI.Shell.SMDATA), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetState(self, psmd: POINTER(win32more.Windows.Win32.UI.Shell.SMDATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetMenuToolbar(self, punk: win32more.Windows.Win32.System.Com.IUnknown, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellMenuCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4ca300a1-9b8d-11d1-8b22-00c04fd918d0}')
    @commethod(3)
    def CallbackSM(self, psmd: POINTER(win32more.Windows.Win32.UI.Shell.SMDATA), uMsg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellNameSpace(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IShellFavoritesNameSpace
    _iid_ = Guid('{e572d3c9-37be-4ae2-825d-d521763e3108}')
    @commethod(20)
    def get_EnumOptions(self, pgrfEnumFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_EnumOptions(self, lVal: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_SelectedItem(self, pItem: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_SelectedItem(self, pItem: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_Root(self, pvar: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_Root(self, var: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_Depth(self, piDepth: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_Depth(self, iDepth: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_Mode(self, puMode: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def put_Mode(self, uMode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_Flags(self, pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def put_Flags(self, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_TVFlags(self, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def get_TVFlags(self, dwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def get_Columns(self, bstrColumns: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def put_Columns(self, bstrColumns: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_CountViewTypes(self, piTypes: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def SetViewType(self, iType: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def SelectedItems(self, ppid: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def Expand(self, var: win32more.Windows.Win32.System.Variant.VARIANT, iDepth: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def UnselectAll(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellPropSheetExt(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{000214e9-0000-0000-c000-000000000046}')
    @commethod(3)
    def AddPages(self, pfnAddPage: win32more.Windows.Win32.UI.Controls.LPFNSVADDPROPSHEETPAGE, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReplacePage(self, uPageID: UInt32, pfnReplaceWith: win32more.Windows.Win32.UI.Controls.LPFNSVADDPROPSHEETPAGE, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellRunDll(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fce4bde0-4b68-4b80-8e9c-7426315a7388}')
    @commethod(3)
    def Run(self, pszArgs: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellService(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5836fb00-8187-11cf-a12b-00aa004ae837}')
    @commethod(3)
    def SetOwner(self, punkOwner: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellTaskScheduler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6ccb7be0-6807-11d0-b810-00c04fd706ec}')
    @commethod(3)
    def AddTask(self, prt: win32more.Windows.Win32.UI.Shell.IRunnableTask, rtoid: POINTER(Guid), lParam: UIntPtr, dwPriority: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveTasks(self, rtoid: POINTER(Guid), lParam: UIntPtr, bWaitIfRunning: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CountTasks(self, rtoid: POINTER(Guid)) -> UInt32: ...
    @commethod(6)
    def Status(self, dwReleaseStatus: UInt32, dwThreadTimeout: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellUIHelper(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{729fe2f8-1ea8-11d1-8f85-00c04fc2fbe1}')
    @commethod(7)
    def ResetFirstBootMode(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def ResetSafeMode(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RefreshOfflineDesktop(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def AddFavorite(self, URL: win32more.Windows.Win32.Foundation.BSTR, Title: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def AddChannel(self, URL: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def AddDesktopComponent(self, URL: win32more.Windows.Win32.Foundation.BSTR, Type: win32more.Windows.Win32.Foundation.BSTR, Left: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), Top: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), Width: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), Height: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def IsSubscribed(self, URL: win32more.Windows.Win32.Foundation.BSTR, pBool: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def NavigateAndFind(self, URL: win32more.Windows.Win32.Foundation.BSTR, strQuery: win32more.Windows.Win32.Foundation.BSTR, varTargetFrame: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ImportExportFavorites(self, fImport: win32more.Windows.Win32.Foundation.VARIANT_BOOL, strImpExpPath: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def AutoCompleteSaveForm(self, Form: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def AutoScan(self, strSearch: win32more.Windows.Win32.Foundation.BSTR, strFailureUrl: win32more.Windows.Win32.Foundation.BSTR, pvarTargetFrame: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def AutoCompleteAttach(self, Reserved: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def ShowBrowserUI(self, bstrName: win32more.Windows.Win32.Foundation.BSTR, pvarIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarOut: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellUIHelper2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IShellUIHelper
    _iid_ = Guid('{a7fe6eda-1932-4281-b881-87b31b8bc52c}')
    @commethod(20)
    def AddSearchProvider(self, URL: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def RunOnceShown(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def SkipRunOnce(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def CustomizeSettings(self, fSQM: win32more.Windows.Win32.Foundation.VARIANT_BOOL, fPhishing: win32more.Windows.Win32.Foundation.VARIANT_BOOL, bstrLocale: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def SqmEnabled(self, pfEnabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def PhishingEnabled(self, pfEnabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def BrandImageUri(self, pbstrUri: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def SkipTabsWelcome(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def DiagnoseConnection(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def CustomizeClearType(self, fSet: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def IsSearchProviderInstalled(self, URL: win32more.Windows.Win32.Foundation.BSTR, pdwResult: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def IsSearchMigrated(self, pfMigrated: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def DefaultSearchProvider(self, pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def RunOnceRequiredSettingsComplete(self, fComplete: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def RunOnceHasShown(self, pfShown: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def SearchGuideUrl(self, pbstrUrl: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellUIHelper3(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IShellUIHelper2
    _iid_ = Guid('{528df2ec-d419-40bc-9b6d-dcdbf9c1b25d}')
    @commethod(36)
    def AddService(self, URL: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def IsServiceInstalled(self, URL: win32more.Windows.Win32.Foundation.BSTR, Verb: win32more.Windows.Win32.Foundation.BSTR, pdwResult: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def InPrivateFilteringEnabled(self, pfEnabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def AddToFavoritesBar(self, URL: win32more.Windows.Win32.Foundation.BSTR, Title: win32more.Windows.Win32.Foundation.BSTR, Type: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def BuildNewTabPage(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def SetRecentlyClosedVisible(self, fVisible: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def SetActivitiesVisible(self, fVisible: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def ContentDiscoveryReset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def IsSuggestedSitesEnabled(self, pfEnabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def EnableSuggestedSites(self, fEnable: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def NavigateToSuggestedSites(self, bstrRelativeUrl: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def ShowTabsHelp(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def ShowInPrivateHelp(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellUIHelper4(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IShellUIHelper3
    _iid_ = Guid('{b36e6a53-8073-499e-824c-d776330a333e}')
    @commethod(49)
    def msIsSiteMode(self, pfSiteMode: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def msSiteModeShowThumbBar(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def msSiteModeAddThumbBarButton(self, bstrIconURL: win32more.Windows.Win32.Foundation.BSTR, bstrTooltip: win32more.Windows.Win32.Foundation.BSTR, pvarButtonID: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(52)
    def msSiteModeUpdateThumbBarButton(self, ButtonID: win32more.Windows.Win32.System.Variant.VARIANT, fEnabled: win32more.Windows.Win32.Foundation.VARIANT_BOOL, fVisible: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def msSiteModeSetIconOverlay(self, IconUrl: win32more.Windows.Win32.Foundation.BSTR, pvarDescription: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def msSiteModeClearIconOverlay(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def msAddSiteMode(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def msSiteModeCreateJumpList(self, bstrHeader: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def msSiteModeAddJumpListItem(self, bstrName: win32more.Windows.Win32.Foundation.BSTR, bstrActionUri: win32more.Windows.Win32.Foundation.BSTR, bstrIconUri: win32more.Windows.Win32.Foundation.BSTR, pvarWindowType: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def msSiteModeClearJumpList(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def msSiteModeShowJumpList(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def msSiteModeAddButtonStyle(self, uiButtonID: win32more.Windows.Win32.System.Variant.VARIANT, bstrIconUrl: win32more.Windows.Win32.Foundation.BSTR, bstrTooltip: win32more.Windows.Win32.Foundation.BSTR, pvarStyleID: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def msSiteModeShowButtonStyle(self, uiButtonID: win32more.Windows.Win32.System.Variant.VARIANT, uiStyleID: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def msSiteModeActivate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def msIsSiteModeFirstRun(self, fPreserveState: win32more.Windows.Win32.Foundation.VARIANT_BOOL, puiFirstRun: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def msAddTrackingProtectionList(self, URL: win32more.Windows.Win32.Foundation.BSTR, bstrFilterName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def msTrackingProtectionEnabled(self, pfEnabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def msActiveXFilteringEnabled(self, pfEnabled: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellUIHelper5(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IShellUIHelper4
    _iid_ = Guid('{a2a08b09-103d-4d3f-b91c-ea455ca82efa}')
    @commethod(67)
    def msProvisionNetworks(self, bstrProvisioningXml: win32more.Windows.Win32.Foundation.BSTR, puiResult: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(68)
    def msReportSafeUrl(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def msSiteModeRefreshBadge(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(70)
    def msSiteModeClearBadge(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(71)
    def msDiagnoseConnectionUILess(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(72)
    def msLaunchNetworkClientHelp(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(73)
    def msChangeDefaultBrowser(self, fChange: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellUIHelper6(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IShellUIHelper5
    _iid_ = Guid('{987a573e-46ee-4e89-96ab-ddf7f8fdc98c}')
    @commethod(74)
    def msStopPeriodicTileUpdate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(75)
    def msStartPeriodicTileUpdate(self, pollingUris: win32more.Windows.Win32.System.Variant.VARIANT, startTime: win32more.Windows.Win32.System.Variant.VARIANT, uiUpdateRecurrence: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(76)
    def msStartPeriodicTileUpdateBatch(self, pollingUris: win32more.Windows.Win32.System.Variant.VARIANT, startTime: win32more.Windows.Win32.System.Variant.VARIANT, uiUpdateRecurrence: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(77)
    def msClearTile(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(78)
    def msEnableTileNotificationQueue(self, fChange: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(79)
    def msPinnedSiteState(self, pvarSiteState: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(80)
    def msEnableTileNotificationQueueForSquare150x150(self, fChange: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(81)
    def msEnableTileNotificationQueueForWide310x150(self, fChange: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(82)
    def msEnableTileNotificationQueueForSquare310x310(self, fChange: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(83)
    def msScheduledTileNotification(self, bstrNotificationXml: win32more.Windows.Win32.Foundation.BSTR, bstrNotificationId: win32more.Windows.Win32.Foundation.BSTR, bstrNotificationTag: win32more.Windows.Win32.Foundation.BSTR, startTime: win32more.Windows.Win32.System.Variant.VARIANT, expirationTime: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(84)
    def msRemoveScheduledTileNotification(self, bstrNotificationId: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(85)
    def msStartPeriodicBadgeUpdate(self, pollingUri: win32more.Windows.Win32.Foundation.BSTR, startTime: win32more.Windows.Win32.System.Variant.VARIANT, uiUpdateRecurrence: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(86)
    def msStopPeriodicBadgeUpdate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(87)
    def msLaunchInternetOptions(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellUIHelper7(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IShellUIHelper6
    _iid_ = Guid('{60e567c8-9573-4ab2-a264-637c6c161cb1}')
    @commethod(88)
    def SetExperimentalFlag(self, bstrFlagString: win32more.Windows.Win32.Foundation.BSTR, vfFlag: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(89)
    def GetExperimentalFlag(self, bstrFlagString: win32more.Windows.Win32.Foundation.BSTR, vfFlag: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(90)
    def SetExperimentalValue(self, bstrValueString: win32more.Windows.Win32.Foundation.BSTR, dwValue: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(91)
    def GetExperimentalValue(self, bstrValueString: win32more.Windows.Win32.Foundation.BSTR, pdwValue: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(92)
    def ResetAllExperimentalFlagsAndValues(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(93)
    def GetNeedIEAutoLaunchFlag(self, bstrUrl: win32more.Windows.Win32.Foundation.BSTR, flag: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(94)
    def SetNeedIEAutoLaunchFlag(self, bstrUrl: win32more.Windows.Win32.Foundation.BSTR, flag: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(95)
    def HasNeedIEAutoLaunchFlag(self, bstrUrl: win32more.Windows.Win32.Foundation.BSTR, exists: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(96)
    def LaunchIE(self, bstrUrl: win32more.Windows.Win32.Foundation.BSTR, automated: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellUIHelper8(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IShellUIHelper7
    _iid_ = Guid('{66debcf2-05b0-4f07-b49b-b96241a65db2}')
    @commethod(97)
    def GetCVListData(self, pbstrResult: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(98)
    def GetCVListLocalData(self, pbstrResult: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(99)
    def GetEMIEListData(self, pbstrResult: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(100)
    def GetEMIEListLocalData(self, pbstrResult: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(101)
    def OpenFavoritesPane(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(102)
    def OpenFavoritesSettings(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(103)
    def LaunchInHVSI(self, bstrUrl: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellUIHelper9(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IShellUIHelper8
    _iid_ = Guid('{6cdf73b0-7f2f-451f-bc0f-63e0f3284e54}')
    @commethod(104)
    def GetOSSku(self, pdwResult: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellView(ComPtr):
    extends: win32more.Windows.Win32.System.Ole.IOleWindow
    _iid_ = Guid('{000214e3-0000-0000-c000-000000000046}')
    @commethod(5)
    def TranslateAccelerator(self, pmsg: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.MSG)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def EnableModeless(self, fEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UIActivate(self, uState: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Refresh(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CreateViewWindow(self, psvPrevious: win32more.Windows.Win32.UI.Shell.IShellView, pfs: POINTER(win32more.Windows.Win32.UI.Shell.FOLDERSETTINGS), psb: win32more.Windows.Win32.UI.Shell.IShellBrowser, prcView: POINTER(win32more.Windows.Win32.Foundation.RECT), phWnd: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def DestroyViewWindow(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetCurrentInfo(self, pfs: POINTER(win32more.Windows.Win32.UI.Shell.FOLDERSETTINGS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def AddPropertySheetPages(self, dwReserved: UInt32, pfn: win32more.Windows.Win32.UI.Controls.LPFNSVADDPROPSHEETPAGE, lparam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SaveViewState(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SelectItem(self, pidlItem: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), uFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetItemObject(self, uItem: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellView2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IShellView
    _iid_ = Guid('{88e39e80-3578-11cf-ae69-08002b2e1262}')
    @commethod(16)
    def GetView(self, pvid: POINTER(Guid), uView: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def CreateViewWindow2(self, lpParams: POINTER(win32more.Windows.Win32.UI.Shell.SV2CVW2_PARAMS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def HandleRename(self, pidlNew: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SelectAndPositionItem(self, pidlItem: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), uFlags: UInt32, ppt: POINTER(win32more.Windows.Win32.Foundation.POINT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellView3(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IShellView2
    _iid_ = Guid('{ec39fa88-f8af-41c5-8421-38bed28f4673}')
    @commethod(20)
    def CreateViewWindow3(self, psbOwner: win32more.Windows.Win32.UI.Shell.IShellBrowser, psvPrev: win32more.Windows.Win32.UI.Shell.IShellView, dwViewFlags: UInt32, dwMask: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS, dwFlags: win32more.Windows.Win32.UI.Shell.FOLDERFLAGS, fvMode: win32more.Windows.Win32.UI.Shell.FOLDERVIEWMODE, pvid: POINTER(Guid), prcView: POINTER(win32more.Windows.Win32.Foundation.RECT), phwndView: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IShellWindows(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{85cb6900-4d95-11cf-960c-0080c7f4ee85}')
    @commethod(7)
    def get_Count(self, Count: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Item(self, index: win32more.Windows.Win32.System.Variant.VARIANT, Folder: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def _NewEnum(self, ppunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Register(self, pid: win32more.Windows.Win32.System.Com.IDispatch, hwnd: Int32, swClass: win32more.Windows.Win32.UI.Shell.ShellWindowTypeConstants, plCookie: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RegisterPending(self, lThreadId: Int32, pvarloc: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarlocRoot: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), swClass: win32more.Windows.Win32.UI.Shell.ShellWindowTypeConstants, plCookie: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Revoke(self, lCookie: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def OnNavigate(self, lCookie: Int32, pvarLoc: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def OnActivated(self, lCookie: Int32, fActive: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def FindWindowSW(self, pvarLoc: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarLocRoot: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), swClass: win32more.Windows.Win32.UI.Shell.ShellWindowTypeConstants, phwnd: POINTER(Int32), swfwOptions: win32more.Windows.Win32.UI.Shell.ShellWindowFindWindowOptions, ppdispOut: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def OnCreated(self, lCookie: Int32, punk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def ProcessAttachDetach(self, fAttach: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISortColumnArray(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6dfc60fb-f2e9-459b-beb5-288f1a7c7d54}')
    @commethod(3)
    def GetCount(self, columnCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAt(self, index: UInt32, sortcolumn: POINTER(win32more.Windows.Win32.UI.Shell.SORTCOLUMN)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSortType(self, type: POINTER(win32more.Windows.Win32.UI.Shell.SORT_ORDER_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IStartMenuPinnedList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4cd19ada-25a5-4a32-b3b7-347bee5be36b}')
    @commethod(3)
    def RemoveFromList(self, pitem: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IStorageProviderBanners(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5efb46d7-47c0-4b68-acda-ded47c90ec91}')
    @commethod(3)
    def SetBanner(self, providerIdentity: win32more.Windows.Win32.Foundation.PWSTR, subscriptionId: win32more.Windows.Win32.Foundation.PWSTR, contentId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ClearBanner(self, providerIdentity: win32more.Windows.Win32.Foundation.PWSTR, subscriptionId: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ClearAllBanners(self, providerIdentity: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetBanner(self, providerIdentity: win32more.Windows.Win32.Foundation.PWSTR, subscriptionId: win32more.Windows.Win32.Foundation.PWSTR, contentId: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IStorageProviderCopyHook(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7bf992a9-af7a-4dba-b2e5-4d080b1ecbc6}')
    @commethod(3)
    def CopyCallback(self, hwnd: win32more.Windows.Win32.Foundation.HWND, operation: UInt32, flags: UInt32, srcFile: win32more.Windows.Win32.Foundation.PWSTR, srcAttribs: UInt32, destFile: win32more.Windows.Win32.Foundation.PWSTR, destAttribs: UInt32, result: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IStorageProviderHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{162c6fb5-44d3-435b-903d-e613fa093fb5}')
    @commethod(3)
    def GetPropertyHandlerFromPath(self, path: win32more.Windows.Win32.Foundation.PWSTR, propertyHandler: POINTER(win32more.Windows.Win32.UI.Shell.IStorageProviderPropertyHandler)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPropertyHandlerFromUri(self, uri: win32more.Windows.Win32.Foundation.PWSTR, propertyHandler: POINTER(win32more.Windows.Win32.UI.Shell.IStorageProviderPropertyHandler)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPropertyHandlerFromFileId(self, fileId: win32more.Windows.Win32.Foundation.PWSTR, propertyHandler: POINTER(win32more.Windows.Win32.UI.Shell.IStorageProviderPropertyHandler)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IStorageProviderPropertyHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{301dfbe5-524c-4b0f-8b2d-21c40b3a2988}')
    @commethod(3)
    def RetrieveProperties(self, propertiesToRetrieve: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), propertiesToRetrieveCount: UInt32, retrievedProperties: POINTER(win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SaveProperties(self, propertiesToSave: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IStreamAsync(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IStream
    _iid_ = Guid('{fe0b6665-e0ca-49b9-a178-2b5cb48d92a5}')
    @commethod(14)
    def ReadAsync(self, pv: VoidPtr, cb: UInt32, pcbRead: POINTER(UInt32), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def WriteAsync(self, lpBuffer: VoidPtr, cb: UInt32, pcbWritten: POINTER(UInt32), lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def OverlappedResult(self, lpOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED), lpNumberOfBytesTransferred: POINTER(UInt32), bWait: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def CancelIo(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IStreamUnbufferedInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8a68fdda-1fdc-4c20-8ceb-416643b5a625}')
    @commethod(3)
    def GetSectorSize(self, pcbSectorSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISuspensionDependencyManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{52b83a42-2543-416a-81d9-c0de7969c8b3}')
    @commethod(3)
    def RegisterAsChild(self, processHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GroupChildWithParent(self, childProcessHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def UngroupChildFromParent(self, childProcessHandle: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrConflict(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9c204249-c443-4ba4-85ed-c972681db137}')
    @commethod(3)
    def GetProperty(self, propkey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), ppropvar: POINTER(win32more.Windows.Win32.System.Com.StructuredStorage.PROPVARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetConflictIdInfo(self, pConflictIdInfo: POINTER(win32more.Windows.Win32.UI.Shell.SYNCMGR_CONFLICT_ID_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetItemsArray(self, ppArray: POINTER(win32more.Windows.Win32.UI.Shell.ISyncMgrConflictItems)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Resolve(self, pResolveInfo: win32more.Windows.Win32.UI.Shell.ISyncMgrConflictResolveInfo) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetResolutionHandler(self, riid: POINTER(Guid), ppvResolutionHandler: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrConflictFolder(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{59287f5e-bc81-4fca-a7f1-e5a8ecdb1d69}')
    @commethod(3)
    def GetConflictIDList(self, pConflict: win32more.Windows.Win32.UI.Shell.ISyncMgrConflict, ppidlConflict: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrConflictItems(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9c7ead52-8023-4936-a4db-d2a9a99e436a}')
    @commethod(3)
    def GetCount(self, pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetItem(self, iIndex: UInt32, pItemInfo: POINTER(win32more.Windows.Win32.UI.Shell.CONFIRM_CONFLICT_ITEM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrConflictPresenter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0b4f5353-fd2b-42cd-8763-4779f2d508a3}')
    @commethod(3)
    def PresentConflict(self, pConflict: win32more.Windows.Win32.UI.Shell.ISyncMgrConflict, pResolveInfo: win32more.Windows.Win32.UI.Shell.ISyncMgrConflictResolveInfo) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrConflictResolutionItems(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{458725b9-129d-4135-a998-9ceafec27007}')
    @commethod(3)
    def GetCount(self, pCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetItem(self, iIndex: UInt32, pItemInfo: POINTER(win32more.Windows.Win32.UI.Shell.CONFIRM_CONFLICT_RESULT_INFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrConflictResolveInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c405a219-25a2-442e-8743-b845a2cee93f}')
    @commethod(3)
    def GetIterationInfo(self, pnCurrentConflict: POINTER(UInt32), pcConflicts: POINTER(UInt32), pcRemainingForApplyToAll: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPresenterNextStep(self, pnPresenterNextStep: POINTER(win32more.Windows.Win32.UI.Shell.SYNCMGR_PRESENTER_NEXT_STEP)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPresenterChoice(self, pnPresenterChoice: POINTER(win32more.Windows.Win32.UI.Shell.SYNCMGR_PRESENTER_CHOICE), pfApplyToAll: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetItemChoiceCount(self, pcChoices: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetItemChoice(self, iChoice: UInt32, piChoiceIndex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetPresenterNextStep(self, nPresenterNextStep: win32more.Windows.Win32.UI.Shell.SYNCMGR_PRESENTER_NEXT_STEP) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetPresenterChoice(self, nPresenterChoice: win32more.Windows.Win32.UI.Shell.SYNCMGR_PRESENTER_CHOICE, fApplyToAll: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetItemChoices(self, prgiConflictItemIndexes: POINTER(UInt32), cChoices: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrConflictStore(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cf8fc579-c396-4774-85f1-d908a831156e}')
    @commethod(3)
    def EnumConflicts(self, pszHandlerID: win32more.Windows.Win32.Foundation.PWSTR, pszItemID: win32more.Windows.Win32.Foundation.PWSTR, ppEnum: POINTER(win32more.Windows.Win32.UI.Shell.IEnumSyncMgrConflict)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BindToConflict(self, pConflictIdInfo: POINTER(win32more.Windows.Win32.UI.Shell.SYNCMGR_CONFLICT_ID_INFO), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemoveConflicts(self, rgConflictIdInfo: POINTER(win32more.Windows.Win32.UI.Shell.SYNCMGR_CONFLICT_ID_INFO), cConflicts: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCount(self, pszHandlerID: win32more.Windows.Win32.Foundation.PWSTR, pszItemID: win32more.Windows.Win32.Foundation.PWSTR, pnConflicts: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrControl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9b63616c-36b2-46bc-959f-c1593952d19b}')
    @commethod(3)
    def StartHandlerSync(self, pszHandlerID: win32more.Windows.Win32.Foundation.PWSTR, hwndOwner: win32more.Windows.Win32.Foundation.HWND, punk: win32more.Windows.Win32.System.Com.IUnknown, nSyncControlFlags: win32more.Windows.Win32.UI.Shell.SYNCMGR_SYNC_CONTROL_FLAGS, pResult: win32more.Windows.Win32.UI.Shell.ISyncMgrSyncResult) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def StartItemSync(self, pszHandlerID: win32more.Windows.Win32.Foundation.PWSTR, ppszItemIDs: POINTER(win32more.Windows.Win32.Foundation.PWSTR), cItems: UInt32, hwndOwner: win32more.Windows.Win32.Foundation.HWND, punk: win32more.Windows.Win32.System.Com.IUnknown, nSyncControlFlags: win32more.Windows.Win32.UI.Shell.SYNCMGR_SYNC_CONTROL_FLAGS, pResult: win32more.Windows.Win32.UI.Shell.ISyncMgrSyncResult) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def StartSyncAll(self, hwndOwner: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def StopHandlerSync(self, pszHandlerID: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def StopItemSync(self, pszHandlerID: win32more.Windows.Win32.Foundation.PWSTR, ppszItemIDs: POINTER(win32more.Windows.Win32.Foundation.PWSTR), cItems: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def StopSyncAll(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def UpdateHandlerCollection(self, rclsidCollectionID: POINTER(Guid), nControlFlags: win32more.Windows.Win32.UI.Shell.SYNCMGR_CONTROL_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def UpdateHandler(self, pszHandlerID: win32more.Windows.Win32.Foundation.PWSTR, nControlFlags: win32more.Windows.Win32.UI.Shell.SYNCMGR_CONTROL_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def UpdateItem(self, pszHandlerID: win32more.Windows.Win32.Foundation.PWSTR, pszItemID: win32more.Windows.Win32.Foundation.PWSTR, nControlFlags: win32more.Windows.Win32.UI.Shell.SYNCMGR_CONTROL_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def UpdateEvents(self, pszHandlerID: win32more.Windows.Win32.Foundation.PWSTR, pszItemID: win32more.Windows.Win32.Foundation.PWSTR, nControlFlags: win32more.Windows.Win32.UI.Shell.SYNCMGR_CONTROL_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def UpdateConflict(self, pszHandlerID: win32more.Windows.Win32.Foundation.PWSTR, pszItemID: win32more.Windows.Win32.Foundation.PWSTR, pConflict: win32more.Windows.Win32.UI.Shell.ISyncMgrConflict, nReason: win32more.Windows.Win32.UI.Shell.SYNCMGR_UPDATE_REASON) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def UpdateConflicts(self, pszHandlerID: win32more.Windows.Win32.Foundation.PWSTR, pszItemID: win32more.Windows.Win32.Foundation.PWSTR, nControlFlags: win32more.Windows.Win32.UI.Shell.SYNCMGR_CONTROL_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ActivateHandler(self, fActivate: win32more.Windows.Win32.Foundation.BOOL, pszHandlerID: win32more.Windows.Win32.Foundation.PWSTR, hwndOwner: win32more.Windows.Win32.Foundation.HWND, nControlFlags: win32more.Windows.Win32.UI.Shell.SYNCMGR_CONTROL_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def EnableHandler(self, fEnable: win32more.Windows.Win32.Foundation.BOOL, pszHandlerID: win32more.Windows.Win32.Foundation.PWSTR, hwndOwner: win32more.Windows.Win32.Foundation.HWND, nControlFlags: win32more.Windows.Win32.UI.Shell.SYNCMGR_CONTROL_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def EnableItem(self, fEnable: win32more.Windows.Win32.Foundation.BOOL, pszHandlerID: win32more.Windows.Win32.Foundation.PWSTR, pszItemID: win32more.Windows.Win32.Foundation.PWSTR, hwndOwner: win32more.Windows.Win32.Foundation.HWND, nControlFlags: win32more.Windows.Win32.UI.Shell.SYNCMGR_CONTROL_FLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrEnumItems(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6295df2a-35ee-11d1-8707-00c04fd93327}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.UI.Shell.SYNCMGRITEM), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.UI.Shell.ISyncMgrEnumItems)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrEvent(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fee0ef8b-46bd-4db4-b7e6-ff2c687313bc}')
    @commethod(3)
    def GetEventID(self, pguidEventID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHandlerID(self, ppszHandlerID: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetItemID(self, ppszItemID: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetLevel(self, pnLevel: POINTER(win32more.Windows.Win32.UI.Shell.SYNCMGR_EVENT_LEVEL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFlags(self, pnFlags: POINTER(win32more.Windows.Win32.UI.Shell.SYNCMGR_EVENT_FLAGS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetTime(self, pfCreationTime: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetName(self, ppszName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDescription(self, ppszDescription: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetLinkText(self, ppszLinkText: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetLinkReference(self, ppszLinkReference: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetContext(self, ppszContext: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrEventLinkUIOperation(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.ISyncMgrUIOperation
    _iid_ = Guid('{64522e52-848b-4015-89ce-5a36f00b94ff}')
    @commethod(4)
    def Init(self, rguidEventID: POINTER(Guid), pEvent: win32more.Windows.Win32.UI.Shell.ISyncMgrEvent) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrEventStore(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{37e412f9-016e-44c2-81ff-db3add774266}')
    @commethod(3)
    def GetEventEnumerator(self, ppenum: POINTER(win32more.Windows.Win32.UI.Shell.IEnumSyncMgrEvents)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetEventCount(self, pcEvents: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetEvent(self, rguidEventID: POINTER(Guid), ppEvent: POINTER(win32more.Windows.Win32.UI.Shell.ISyncMgrEvent)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveEvent(self, pguidEventIDs: POINTER(Guid), cEvents: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{04ec2e43-ac77-49f9-9b98-0307ef7a72a2}')
    @commethod(3)
    def GetName(self, ppszName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHandlerInfo(self, ppHandlerInfo: POINTER(win32more.Windows.Win32.UI.Shell.ISyncMgrHandlerInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetObject(self, rguidObjectID: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCapabilities(self, pmCapabilities: POINTER(win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_CAPABILITIES)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPolicies(self, pmPolicies: POINTER(win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_POLICIES)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Activate(self, fActivate: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Enable(self, fEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Synchronize(self, ppszItemIDs: POINTER(win32more.Windows.Win32.Foundation.PWSTR), cItems: UInt32, hwndOwner: win32more.Windows.Win32.Foundation.HWND, pSessionCreator: win32more.Windows.Win32.UI.Shell.ISyncMgrSessionCreator, punk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrHandlerCollection(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a7f337a3-d20b-45cb-9ed7-87d094ca5045}')
    @commethod(3)
    def GetHandlerEnumerator(self, ppenum: POINTER(win32more.Windows.Win32.System.Com.IEnumString)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def BindToHandler(self, pszHandlerID: win32more.Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrHandlerInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4ff1d798-ecf7-4524-aa81-1e362a0aef3a}')
    @commethod(3)
    def GetType(self, pnType: POINTER(win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_TYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetTypeLabel(self, ppszTypeLabel: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetComment(self, ppszComment: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetLastSyncTime(self, pftLastSync: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsActive(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsEnabled(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def IsConnected(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrRegister(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6295df42-35ee-11d1-8707-00c04fd93327}')
    @commethod(3)
    def RegisterSyncMgrHandler(self, clsidHandler: POINTER(Guid), pwszDescription: win32more.Windows.Win32.Foundation.PWSTR, dwSyncMgrRegisterFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterSyncMgrHandler(self, clsidHandler: POINTER(Guid), dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetHandlerRegistrationInfo(self, clsidHandler: POINTER(Guid), pdwSyncMgrRegisterFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrResolutionHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{40a3d052-8bff-4c4b-a338-d4a395700de9}')
    @commethod(3)
    def QueryAbilities(self, pdwAbilities: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def KeepOther(self, psiOther: win32more.Windows.Win32.UI.Shell.IShellItem, pFeedback: POINTER(win32more.Windows.Win32.UI.Shell.SYNCMGR_RESOLUTION_FEEDBACK)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def KeepRecent(self, pFeedback: POINTER(win32more.Windows.Win32.UI.Shell.SYNCMGR_RESOLUTION_FEEDBACK)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RemoveFromSyncSet(self, pFeedback: POINTER(win32more.Windows.Win32.UI.Shell.SYNCMGR_RESOLUTION_FEEDBACK)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def KeepItems(self, pArray: win32more.Windows.Win32.UI.Shell.ISyncMgrConflictResolutionItems, pFeedback: POINTER(win32more.Windows.Win32.UI.Shell.SYNCMGR_RESOLUTION_FEEDBACK)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrScheduleWizardUIOperation(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.ISyncMgrUIOperation
    _iid_ = Guid('{459a6c84-21d2-4ddc-8a53-f023a46066f2}')
    @commethod(4)
    def InitWizard(self, pszHandlerID: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrSessionCreator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{17f48517-f305-4321-a08d-b25a834918fd}')
    @commethod(3)
    def CreateSession(self, pszHandlerID: win32more.Windows.Win32.Foundation.PWSTR, ppszItemIDs: POINTER(win32more.Windows.Win32.Foundation.PWSTR), cItems: UInt32, ppCallback: POINTER(win32more.Windows.Win32.UI.Shell.ISyncMgrSyncCallback)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrSyncCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{884ccd87-b139-4937-a4ba-4f8e19513fbe}')
    @commethod(3)
    def ReportProgress(self, pszItemID: win32more.Windows.Win32.Foundation.PWSTR, pszProgressText: win32more.Windows.Win32.Foundation.PWSTR, nStatus: win32more.Windows.Win32.UI.Shell.SYNCMGR_PROGRESS_STATUS, uCurrentStep: UInt32, uMaxStep: UInt32, pnCancelRequest: POINTER(win32more.Windows.Win32.UI.Shell.SYNCMGR_CANCEL_REQUEST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetHandlerProgressText(self, pszProgressText: win32more.Windows.Win32.Foundation.PWSTR, pnCancelRequest: POINTER(win32more.Windows.Win32.UI.Shell.SYNCMGR_CANCEL_REQUEST)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ReportEvent(self, pszItemID: win32more.Windows.Win32.Foundation.PWSTR, nLevel: win32more.Windows.Win32.UI.Shell.SYNCMGR_EVENT_LEVEL, nFlags: win32more.Windows.Win32.UI.Shell.SYNCMGR_EVENT_FLAGS, pszName: win32more.Windows.Win32.Foundation.PWSTR, pszDescription: win32more.Windows.Win32.Foundation.PWSTR, pszLinkText: win32more.Windows.Win32.Foundation.PWSTR, pszLinkReference: win32more.Windows.Win32.Foundation.PWSTR, pszContext: win32more.Windows.Win32.Foundation.PWSTR, pguidEventID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CanContinue(self, pszItemID: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def QueryForAdditionalItems(self, ppenumItemIDs: POINTER(win32more.Windows.Win32.System.Com.IEnumString), ppenumPunks: POINTER(win32more.Windows.Win32.System.Com.IEnumUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def AddItemToSession(self, pszItemID: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddIUnknownToSession(self, punk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ProposeItem(self, pNewItem: win32more.Windows.Win32.UI.Shell.ISyncMgrSyncItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CommitItem(self, pszItemID: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ReportManualSync(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrSyncItem(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b20b24ce-2593-4f04-bd8b-7ad6c45051cd}')
    @commethod(3)
    def GetItemID(self, ppszItemID: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetName(self, ppszName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetItemInfo(self, ppItemInfo: POINTER(win32more.Windows.Win32.UI.Shell.ISyncMgrSyncItemInfo)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetObject(self, rguidObjectID: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCapabilities(self, pmCapabilities: POINTER(win32more.Windows.Win32.UI.Shell.SYNCMGR_ITEM_CAPABILITIES)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetPolicies(self, pmPolicies: POINTER(win32more.Windows.Win32.UI.Shell.SYNCMGR_ITEM_POLICIES)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Enable(self, fEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Delete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrSyncItemContainer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{90701133-be32-4129-a65c-99e616cafff4}')
    @commethod(3)
    def GetSyncItem(self, pszItemID: win32more.Windows.Win32.Foundation.PWSTR, ppItem: POINTER(win32more.Windows.Win32.UI.Shell.ISyncMgrSyncItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSyncItemEnumerator(self, ppenum: POINTER(win32more.Windows.Win32.UI.Shell.IEnumSyncMgrSyncItems)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSyncItemCount(self, pcItems: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrSyncItemInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e7fd9502-be0c-4464-90a1-2b5277031232}')
    @commethod(3)
    def GetTypeLabel(self, ppszTypeLabel: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetComment(self, ppszComment: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLastSyncTime(self, pftLastSync: POINTER(win32more.Windows.Win32.Foundation.FILETIME)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def IsEnabled(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsConnected(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrSyncResult(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{2b90f17e-5a3e-4b33-bb7f-1bc48056b94d}')
    @commethod(3)
    def Result(self, nStatus: win32more.Windows.Win32.UI.Shell.SYNCMGR_PROGRESS_STATUS, cError: UInt32, cConflicts: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrSynchronize(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6295df40-35ee-11d1-8707-00c04fd93327}')
    @commethod(3)
    def Initialize(self, dwReserved: UInt32, dwSyncMgrFlags: UInt32, cbCookie: UInt32, lpCookie: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetHandlerInfo(self, ppSyncMgrHandlerInfo: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.SYNCMGRHANDLERINFO))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumSyncMgrItems(self, ppSyncMgrEnumItems: POINTER(win32more.Windows.Win32.UI.Shell.ISyncMgrEnumItems)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetItemObject(self, ItemID: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ShowProperties(self, hWndParent: win32more.Windows.Win32.Foundation.HWND, ItemID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetProgressCallback(self, lpCallBack: win32more.Windows.Win32.UI.Shell.ISyncMgrSynchronizeCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def PrepareForSync(self, cbNumItems: UInt32, pItemIDs: POINTER(Guid), hWndParent: win32more.Windows.Win32.Foundation.HWND, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Synchronize(self, hWndParent: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetItemStatus(self, pItemID: POINTER(Guid), dwSyncMgrStatus: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ShowError(self, hWndParent: win32more.Windows.Win32.Foundation.HWND, ErrorID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrSynchronizeCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6295df41-35ee-11d1-8707-00c04fd93327}')
    @commethod(3)
    def ShowPropertiesCompleted(self, hr: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PrepareForSyncCompleted(self, hr: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SynchronizeCompleted(self, hr: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ShowErrorCompleted(self, hr: win32more.Windows.Win32.Foundation.HRESULT, cItems: UInt32, pItemIDs: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EnableModeless(self, fEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Progress(self, ItemID: POINTER(Guid), pSyncProgressItem: POINTER(win32more.Windows.Win32.UI.Shell.SYNCMGRPROGRESSITEM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def LogError(self, dwErrorLevel: UInt32, pszErrorText: win32more.Windows.Win32.Foundation.PWSTR, pSyncLogError: POINTER(win32more.Windows.Win32.UI.Shell.SYNCMGRLOGERRORINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def DeleteLogError(self, ErrorID: POINTER(Guid), dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EstablishConnection(self, pwszConnection: win32more.Windows.Win32.Foundation.PWSTR, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrSynchronizeInvoke(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6295df2c-35ee-11d1-8707-00c04fd93327}')
    @commethod(3)
    def UpdateItems(self, dwInvokeFlags: UInt32, clsid: POINTER(Guid), cbCookie: UInt32, pCookie: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UpdateAll(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISyncMgrUIOperation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fc7cfa47-dfe1-45b5-a049-8cfd82bec271}')
    @commethod(3)
    def Run(self, hwndOwner: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITEMSPACING(Structure):
    cxSmall: Int32
    cySmall: Int32
    cxLarge: Int32
    cyLarge: Int32
class ITaskbarList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{56fdf342-fd6d-11d0-958a-006097c9a090}')
    @commethod(3)
    def HrInit(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddTab(self, hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DeleteTab(self, hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ActivateTab(self, hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetActiveAlt(self, hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITaskbarList2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.ITaskbarList
    _iid_ = Guid('{602d4995-b13a-429b-a66e-1935e44f4317}')
    @commethod(8)
    def MarkFullscreenWindow(self, hwnd: win32more.Windows.Win32.Foundation.HWND, fFullscreen: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITaskbarList3(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.ITaskbarList2
    _iid_ = Guid('{ea1afb91-9e28-4b86-90e9-9e9f8a5eefaf}')
    @commethod(9)
    def SetProgressValue(self, hwnd: win32more.Windows.Win32.Foundation.HWND, ullCompleted: UInt64, ullTotal: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetProgressState(self, hwnd: win32more.Windows.Win32.Foundation.HWND, tbpFlags: win32more.Windows.Win32.UI.Shell.TBPFLAG) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RegisterTab(self, hwndTab: win32more.Windows.Win32.Foundation.HWND, hwndMDI: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def UnregisterTab(self, hwndTab: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetTabOrder(self, hwndTab: win32more.Windows.Win32.Foundation.HWND, hwndInsertBefore: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetTabActive(self, hwndTab: win32more.Windows.Win32.Foundation.HWND, hwndMDI: win32more.Windows.Win32.Foundation.HWND, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def ThumbBarAddButtons(self, hwnd: win32more.Windows.Win32.Foundation.HWND, cButtons: UInt32, pButton: POINTER(win32more.Windows.Win32.UI.Shell.THUMBBUTTON)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def ThumbBarUpdateButtons(self, hwnd: win32more.Windows.Win32.Foundation.HWND, cButtons: UInt32, pButton: POINTER(win32more.Windows.Win32.UI.Shell.THUMBBUTTON)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def ThumbBarSetImageList(self, hwnd: win32more.Windows.Win32.Foundation.HWND, himl: win32more.Windows.Win32.UI.Controls.HIMAGELIST) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def SetOverlayIcon(self, hwnd: win32more.Windows.Win32.Foundation.HWND, hIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON, pszDescription: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetThumbnailTooltip(self, hwnd: win32more.Windows.Win32.Foundation.HWND, pszTip: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def SetThumbnailClip(self, hwnd: win32more.Windows.Win32.Foundation.HWND, prcClip: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITaskbarList4(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.ITaskbarList3
    _iid_ = Guid('{c43dc798-95d1-4bea-9030-bb99e2983a1a}')
    @commethod(21)
    def SetTabProperties(self, hwndTab: win32more.Windows.Win32.Foundation.HWND, stpFlags: win32more.Windows.Win32.UI.Shell.STPFLAG) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IThumbnailCache(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f676c15d-596a-4ce2-8234-33996f445db1}')
    @commethod(3)
    def GetThumbnail(self, pShellItem: win32more.Windows.Win32.UI.Shell.IShellItem, cxyRequestedThumbSize: UInt32, flags: win32more.Windows.Win32.UI.Shell.WTS_FLAGS, ppvThumb: POINTER(win32more.Windows.Win32.UI.Shell.ISharedBitmap), pOutFlags: POINTER(win32more.Windows.Win32.UI.Shell.WTS_CACHEFLAGS), pThumbnailID: POINTER(win32more.Windows.Win32.UI.Shell.WTS_THUMBNAILID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetThumbnailByID(self, thumbnailID: win32more.Windows.Win32.UI.Shell.WTS_THUMBNAILID, cxyRequestedThumbSize: UInt32, ppvThumb: POINTER(win32more.Windows.Win32.UI.Shell.ISharedBitmap), pOutFlags: POINTER(win32more.Windows.Win32.UI.Shell.WTS_CACHEFLAGS)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IThumbnailCachePrimer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{0f03f8fe-2b26-46f0-965a-212aa8d66b76}')
    @commethod(3)
    def PageInThumbnail(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem, wtsFlags: win32more.Windows.Win32.UI.Shell.WTS_FLAGS, cxyRequestedThumbSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IThumbnailCapture(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4ea39266-7211-409f-b622-f63dbd16c533}')
    @commethod(3)
    def CaptureThumbnail(self, pMaxSize: POINTER(win32more.Windows.Win32.Foundation.SIZE), pHTMLDoc2: win32more.Windows.Win32.System.Com.IUnknown, phbmThumbnail: POINTER(win32more.Windows.Win32.Graphics.Gdi.HBITMAP)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IThumbnailHandlerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e35b4b2e-00da-4bc1-9f13-38bc11f5d417}')
    @commethod(3)
    def GetThumbnailHandler(self, pidlChild: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), pbc: win32more.Windows.Win32.System.Com.IBindCtx, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IThumbnailProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e357fccd-a995-4576-b01f-234630154e96}')
    @commethod(3)
    def GetThumbnail(self, cx: UInt32, phbmp: POINTER(win32more.Windows.Win32.Graphics.Gdi.HBITMAP), pdwAlpha: POINTER(win32more.Windows.Win32.UI.Shell.WTS_ALPHATYPE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IThumbnailSettings(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f4376f00-bef5-4d45-80f3-1e023bbf1209}')
    @commethod(3)
    def SetContext(self, dwContext: win32more.Windows.Win32.UI.Shell.WTS_CONTEXTFLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IThumbnailStreamCache(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{90e11430-9569-41d8-ae75-6d4d2ae7cca0}')
    @commethod(3)
    def GetThumbnailStream(self, path: win32more.Windows.Win32.Foundation.PWSTR, cacheId: UInt64, options: win32more.Windows.Win32.UI.Shell.ThumbnailStreamCacheOptions, requestedThumbnailSize: UInt32, thumbnailSize: POINTER(win32more.Windows.Win32.Foundation.SIZE), thumbnailStream: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetThumbnailStream(self, path: win32more.Windows.Win32.Foundation.PWSTR, cacheId: UInt64, thumbnailSize: win32more.Windows.Win32.Foundation.SIZE, thumbnailStream: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITrackShellMenu(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IShellMenu
    _iid_ = Guid('{8278f932-2a3e-11d2-838f-00c04fd918d0}')
    @commethod(12)
    def SetObscured(self, hwndTB: win32more.Windows.Win32.Foundation.HWND, punkBand: win32more.Windows.Win32.System.Com.IUnknown, dwSMSetFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Popup(self, hwnd: win32more.Windows.Win32.Foundation.HWND, ppt: POINTER(win32more.Windows.Win32.Foundation.POINTL), prcExclude: POINTER(win32more.Windows.Win32.Foundation.RECTL), dwFlags: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITranscodeImage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bae86ddd-dc11-421c-b7ab-cc55d1d65c44}')
    @commethod(3)
    def TranscodeImage(self, pShellItem: win32more.Windows.Win32.UI.Shell.IShellItem, uiMaxWidth: UInt32, uiMaxHeight: UInt32, flags: UInt32, pvImage: win32more.Windows.Win32.System.Com.IStream, puiWidth: POINTER(UInt32), puiHeight: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransferAdviseSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d594d0d8-8da7-457b-b3b4-ce5dbaac0b88}')
    @commethod(3)
    def UpdateProgress(self, ullSizeCurrent: UInt64, ullSizeTotal: UInt64, nFilesCurrent: Int32, nFilesTotal: Int32, nFoldersCurrent: Int32, nFoldersTotal: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UpdateTransferState(self, ts: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ConfirmOverwrite(self, psiSource: win32more.Windows.Win32.UI.Shell.IShellItem, psiDestParent: win32more.Windows.Win32.UI.Shell.IShellItem, pszName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ConfirmEncryptionLoss(self, psiSource: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FileFailure(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem, pszItem: win32more.Windows.Win32.Foundation.PWSTR, hrError: win32more.Windows.Win32.Foundation.HRESULT, pszRename: win32more.Windows.Win32.Foundation.PWSTR, cchRename: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SubStreamFailure(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem, pszStreamName: win32more.Windows.Win32.Foundation.PWSTR, hrError: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def PropertyFailure(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem, pkey: POINTER(win32more.Windows.Win32.Foundation.PROPERTYKEY), hrError: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransferDestination(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{48addd32-3ca5-4124-abe3-b5a72531b207}')
    @commethod(3)
    def Advise(self, psink: win32more.Windows.Win32.UI.Shell.ITransferAdviseSink, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unadvise(self, dwCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateItem(self, pszName: win32more.Windows.Win32.Foundation.PWSTR, dwAttributes: UInt32, ullSize: UInt64, flags: UInt32, riidItem: POINTER(Guid), ppvItem: POINTER(VoidPtr), riidResources: POINTER(Guid), ppvResources: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITransferMediumItem(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IRelatedItem
    _iid_ = Guid('{77f295d5-2d6f-4e19-b8ae-322f3e721ab5}')
class ITransferSource(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{00adb003-bde9-45c6-8e29-d09f9353e108}')
    @commethod(3)
    def Advise(self, psink: win32more.Windows.Win32.UI.Shell.ITransferAdviseSink, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unadvise(self, dwCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetProperties(self, pproparray: win32more.Windows.Win32.UI.Shell.PropertiesSystem.IPropertyChangeArray) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OpenItem(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem, flags: UInt32, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def MoveItem(self, psi: win32more.Windows.Win32.UI.Shell.IShellItem, psiParentDst: win32more.Windows.Win32.UI.Shell.IShellItem, pszNameDst: win32more.Windows.Win32.Foundation.PWSTR, flags: UInt32, ppsiNew: POINTER(win32more.Windows.Win32.UI.Shell.IShellItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RecycleItem(self, psiSource: win32more.Windows.Win32.UI.Shell.IShellItem, psiParentDest: win32more.Windows.Win32.UI.Shell.IShellItem, flags: UInt32, ppsiNewDest: POINTER(win32more.Windows.Win32.UI.Shell.IShellItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RemoveItem(self, psiSource: win32more.Windows.Win32.UI.Shell.IShellItem, flags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RenameItem(self, psiSource: win32more.Windows.Win32.UI.Shell.IShellItem, pszNewName: win32more.Windows.Win32.Foundation.PWSTR, flags: UInt32, ppsiNewDest: POINTER(win32more.Windows.Win32.UI.Shell.IShellItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def LinkItem(self, psiSource: win32more.Windows.Win32.UI.Shell.IShellItem, psiParentDest: win32more.Windows.Win32.UI.Shell.IShellItem, pszNewName: win32more.Windows.Win32.Foundation.PWSTR, flags: UInt32, ppsiNewDest: POINTER(win32more.Windows.Win32.UI.Shell.IShellItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def ApplyPropertiesToItem(self, psiSource: win32more.Windows.Win32.UI.Shell.IShellItem, ppsiNew: POINTER(win32more.Windows.Win32.UI.Shell.IShellItem)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetDefaultDestinationName(self, psiSource: win32more.Windows.Win32.UI.Shell.IShellItem, psiParentDest: win32more.Windows.Win32.UI.Shell.IShellItem, ppszDestinationName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def EnterFolder(self, psiChildFolderDest: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def LeaveFolder(self, psiChildFolderDest: win32more.Windows.Win32.UI.Shell.IShellItem) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITravelEntry(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f46edb3b-bc2f-11d0-9412-00aa00a3ebd3}')
    @commethod(3)
    def Invoke(self, punk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Update(self, punk: win32more.Windows.Win32.System.Com.IUnknown, fIsLocalAnchor: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPidl(self, ppidl: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITravelLog(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{66a9cb08-4802-11d2-a561-00a0c92dbfe8}')
    @commethod(3)
    def AddEntry(self, punk: win32more.Windows.Win32.System.Com.IUnknown, fIsLocalAnchor: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UpdateEntry(self, punk: win32more.Windows.Win32.System.Com.IUnknown, fIsLocalAnchor: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def UpdateExternal(self, punk: win32more.Windows.Win32.System.Com.IUnknown, punkHLBrowseContext: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Travel(self, punk: win32more.Windows.Win32.System.Com.IUnknown, iOffset: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetTravelEntry(self, punk: win32more.Windows.Win32.System.Com.IUnknown, iOffset: Int32, ppte: POINTER(win32more.Windows.Win32.UI.Shell.ITravelEntry)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def FindTravelEntry(self, punk: win32more.Windows.Win32.System.Com.IUnknown, pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), ppte: POINTER(win32more.Windows.Win32.UI.Shell.ITravelEntry)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetToolTipText(self, punk: win32more.Windows.Win32.System.Com.IUnknown, iOffset: Int32, idsTemplate: Int32, pwzText: win32more.Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def InsertMenuEntries(self, punk: win32more.Windows.Win32.System.Com.IUnknown, hmenu: win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU, nPos: Int32, idFirst: Int32, idLast: Int32, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Clone(self, pptl: POINTER(win32more.Windows.Win32.UI.Shell.ITravelLog)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def CountEntries(self, punk: win32more.Windows.Win32.System.Com.IUnknown) -> UInt32: ...
    @commethod(13)
    def Revert(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITravelLogClient(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{241c033e-e659-43da-aa4d-4086dbc4758d}')
    @commethod(3)
    def FindWindowByIndex(self, dwID: UInt32, ppunk: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetWindowData(self, pStream: win32more.Windows.Win32.System.Com.IStream, pWinData: POINTER(win32more.Windows.Win32.UI.Shell.WINDOWDATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def LoadHistoryPosition(self, pszUrlLocation: win32more.Windows.Win32.Foundation.PWSTR, dwPosition: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITravelLogEntry(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7ebfdd87-ad18-11d3-a4c5-00c04f72d6b8}')
    @commethod(3)
    def GetTitle(self, ppszTitle: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetURL(self, ppszURL: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITravelLogStg(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7ebfdd80-ad18-11d3-a4c5-00c04f72d6b8}')
    @commethod(3)
    def CreateEntry(self, pszUrl: win32more.Windows.Win32.Foundation.PWSTR, pszTitle: win32more.Windows.Win32.Foundation.PWSTR, ptleRelativeTo: win32more.Windows.Win32.UI.Shell.ITravelLogEntry, fPrepend: win32more.Windows.Win32.Foundation.BOOL, pptle: POINTER(win32more.Windows.Win32.UI.Shell.ITravelLogEntry)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def TravelTo(self, ptle: win32more.Windows.Win32.UI.Shell.ITravelLogEntry) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnumEntries(self, flags: win32more.Windows.Win32.UI.Shell.TLENUMF, ppenum: POINTER(win32more.Windows.Win32.UI.Shell.IEnumTravelLogEntry)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FindEntries(self, flags: win32more.Windows.Win32.UI.Shell.TLENUMF, pszUrl: win32more.Windows.Win32.Foundation.PWSTR, ppenum: POINTER(win32more.Windows.Win32.UI.Shell.IEnumTravelLogEntry)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetCount(self, flags: win32more.Windows.Win32.UI.Shell.TLENUMF, pcEntries: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveEntry(self, ptle: win32more.Windows.Win32.UI.Shell.ITravelLogEntry) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRelativeEntry(self, iOffset: Int32, ptle: POINTER(win32more.Windows.Win32.UI.Shell.ITravelLogEntry)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITrayDeskBand(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6d67e846-5b9c-4db8-9cbc-dde12f4254f1}')
    @commethod(3)
    def ShowDeskBand(self, clsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def HideDeskBand(self, clsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsDeskBandShown(self, clsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def DeskBandRegistrationChanged(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IURLSearchHook(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ac60f6a0-0fd9-11d0-99cb-00c04fd64497}')
    @commethod(3)
    def Translate(self, pwszSearchURL: win32more.Windows.Win32.Foundation.PWSTR, cchBufferSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IURLSearchHook2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IURLSearchHook
    _iid_ = Guid('{5ee44da4-6d32-46e3-86bc-07540dedd0e0}')
    @commethod(4)
    def TranslateWithSearchContext(self, pwszSearchURL: win32more.Windows.Win32.Foundation.PWSTR, cchBufferSize: UInt32, pSearchContext: win32more.Windows.Win32.UI.Shell.ISearchContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
IURL_INVOKECOMMAND_FLAGS = Int32
IURL_INVOKECOMMAND_FL_ALLOW_UI: win32more.Windows.Win32.UI.Shell.IURL_INVOKECOMMAND_FLAGS = 1
IURL_INVOKECOMMAND_FL_USE_DEFAULT_VERB: win32more.Windows.Win32.UI.Shell.IURL_INVOKECOMMAND_FLAGS = 2
IURL_INVOKECOMMAND_FL_DDEWAIT: win32more.Windows.Win32.UI.Shell.IURL_INVOKECOMMAND_FLAGS = 4
IURL_INVOKECOMMAND_FL_ASYNCOK: win32more.Windows.Win32.UI.Shell.IURL_INVOKECOMMAND_FLAGS = 8
IURL_INVOKECOMMAND_FL_LOG_USAGE: win32more.Windows.Win32.UI.Shell.IURL_INVOKECOMMAND_FLAGS = 16
IURL_SETURL_FLAGS = Int32
IURL_SETURL_FL_GUESS_PROTOCOL: win32more.Windows.Win32.UI.Shell.IURL_SETURL_FLAGS = 1
IURL_SETURL_FL_USE_DEFAULT_PROTOCOL: win32more.Windows.Win32.UI.Shell.IURL_SETURL_FLAGS = 2
class IUniformResourceLocatorA(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fbf23b80-e3f0-101b-8488-00aa003e56f8}')
    @commethod(3)
    def SetURL(self, pcszURL: win32more.Windows.Win32.Foundation.PSTR, dwInFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetURL(self, ppszURL: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InvokeCommand(self, purlici: POINTER(win32more.Windows.Win32.UI.Shell.URLINVOKECOMMANDINFOA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUniformResourceLocatorW(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cabb0da0-da57-11cf-9974-0020afd79762}')
    @commethod(3)
    def SetURL(self, pcszURL: win32more.Windows.Win32.Foundation.PWSTR, dwInFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetURL(self, ppszURL: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def InvokeCommand(self, purlici: POINTER(win32more.Windows.Win32.UI.Shell.URLINVOKECOMMANDINFOW)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
IUniformResourceLocator = UnicodeAlias('IUniformResourceLocatorW')
class IUpdateIDList(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6589b6d2-5f8d-4b9e-b7e0-23cdd9717d8c}')
    @commethod(3)
    def Update(self, pbc: win32more.Windows.Win32.System.Com.IBindCtx, pidlIn: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST), ppidlOut: POINTER(POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUseToBrowseItem(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IRelatedItem
    _iid_ = Guid('{05edda5c-98a3-4717-8adb-c5e7da991eb1}')
class IUserAccountChangeCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a561e69a-b4b8-4113-91a5-64c6bcca3430}')
    @commethod(3)
    def OnPictureChange(self, pszUserName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUserNotification(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{ba9711ba-5893-4787-a7e1-41277151550b}')
    @commethod(3)
    def SetBalloonInfo(self, pszTitle: win32more.Windows.Win32.Foundation.PWSTR, pszText: win32more.Windows.Win32.Foundation.PWSTR, dwInfoFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetBalloonRetry(self, dwShowTime: UInt32, dwInterval: UInt32, cRetryCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetIconInfo(self, hIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON, pszToolTip: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Show(self, pqc: win32more.Windows.Win32.UI.Shell.IQueryContinue, dwContinuePollInterval: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def PlaySound(self, pszSoundName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUserNotification2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{215913cc-57eb-4fab-ab5a-e5fa7bea2a6c}')
    @commethod(3)
    def SetBalloonInfo(self, pszTitle: win32more.Windows.Win32.Foundation.PWSTR, pszText: win32more.Windows.Win32.Foundation.PWSTR, dwInfoFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetBalloonRetry(self, dwShowTime: UInt32, dwInterval: UInt32, cRetryCount: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetIconInfo(self, hIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON, pszToolTip: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Show(self, pqc: win32more.Windows.Win32.UI.Shell.IQueryContinue, dwContinuePollInterval: UInt32, pSink: win32more.Windows.Win32.UI.Shell.IUserNotificationCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def PlaySound(self, pszSoundName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUserNotificationCallback(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{19108294-0441-4aff-8013-fa0a730b0bea}')
    @commethod(3)
    def OnBalloonUserClick(self, pt: POINTER(win32more.Windows.Win32.Foundation.POINT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnLeftClick(self, pt: POINTER(win32more.Windows.Win32.Foundation.POINT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnContextMenu(self, pt: POINTER(win32more.Windows.Win32.Foundation.POINT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IViewStateIdentityItem(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IRelatedItem
    _iid_ = Guid('{9d264146-a94f-4195-9f9f-3bb12ce0c955}')
class IVirtualDesktopManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a5cd92ff-29be-454c-8d04-d82879fb3f1b}')
    @commethod(3)
    def IsWindowOnCurrentVirtualDesktop(self, topLevelWindow: win32more.Windows.Win32.Foundation.HWND, onCurrentDesktop: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetWindowDesktopId(self, topLevelWindow: win32more.Windows.Win32.Foundation.HWND, desktopId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveWindowToDesktop(self, topLevelWindow: win32more.Windows.Win32.Foundation.HWND, desktopId: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IVisualProperties(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e693cf68-d967-4112-8763-99172aee5e5a}')
    @commethod(3)
    def SetWatermark(self, hbmp: win32more.Windows.Win32.Graphics.Gdi.HBITMAP, vpwf: win32more.Windows.Win32.UI.Shell.VPWATERMARKFLAGS) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetColor(self, vpcf: win32more.Windows.Win32.UI.Shell.VPCOLORFLAGS, cr: win32more.Windows.Win32.Foundation.COLORREF) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetColor(self, vpcf: win32more.Windows.Win32.UI.Shell.VPCOLORFLAGS, pcr: POINTER(win32more.Windows.Win32.Foundation.COLORREF)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetItemHeight(self, cyItemInPixels: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetItemHeight(self, cyItemInPixels: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetFont(self, plf: POINTER(win32more.Windows.Win32.Graphics.Gdi.LOGFONTW), bRedraw: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFont(self, plf: POINTER(win32more.Windows.Win32.Graphics.Gdi.LOGFONTW)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetTheme(self, pszSubAppName: win32more.Windows.Win32.Foundation.PWSTR, pszSubIdList: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWebBrowser(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{eab22ac1-30c1-11cf-a7eb-0000c05bae0b}')
    @commethod(7)
    def GoBack(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GoForward(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GoHome(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GoSearch(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Navigate(self, URL: win32more.Windows.Win32.Foundation.BSTR, Flags: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), TargetFrameName: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), PostData: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), Headers: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Refresh(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Refresh2(self, Level: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Stop(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Application(self, ppDisp: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_Parent(self, ppDisp: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Container(self, ppDisp: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_Document(self, ppDisp: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_TopLevelContainer(self, pBool: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_Type(self, Type: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_Left(self, pl: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_Left(self, Left: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_Top(self, pl: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_Top(self, Top: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_Width(self, pl: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_Width(self, Width: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_Height(self, pl: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_Height(self, Height: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_LocationName(self, LocationName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_LocationURL(self, LocationURL: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_Busy(self, pBool: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWebBrowser2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IWebBrowserApp
    _iid_ = Guid('{d30c1661-cdaf-11d0-8a3e-00c04fc9e26e}')
    @commethod(52)
    def Navigate2(self, URL: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), Flags: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), TargetFrameName: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), PostData: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), Headers: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(53)
    def QueryStatusWB(self, cmdID: win32more.Windows.Win32.System.Ole.OLECMDID, pcmdf: POINTER(win32more.Windows.Win32.System.Ole.OLECMDF)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(54)
    def ExecWB(self, cmdID: win32more.Windows.Win32.System.Ole.OLECMDID, cmdexecopt: win32more.Windows.Win32.System.Ole.OLECMDEXECOPT, pvaIn: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvaOut: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(55)
    def ShowBrowserBar(self, pvaClsid: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarShow: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), pvarSize: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(56)
    def get_ReadyState(self, plReadyState: POINTER(win32more.Windows.Win32.System.Ole.READYSTATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(57)
    def get_Offline(self, pbOffline: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(58)
    def put_Offline(self, bOffline: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(59)
    def get_Silent(self, pbSilent: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(60)
    def put_Silent(self, bSilent: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(61)
    def get_RegisterAsBrowser(self, pbRegister: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(62)
    def put_RegisterAsBrowser(self, bRegister: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(63)
    def get_RegisterAsDropTarget(self, pbRegister: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(64)
    def put_RegisterAsDropTarget(self, bRegister: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(65)
    def get_TheaterMode(self, pbRegister: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(66)
    def put_TheaterMode(self, bRegister: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(67)
    def get_AddressBar(self, Value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(68)
    def put_AddressBar(self, Value: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(69)
    def get_Resizable(self, Value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(70)
    def put_Resizable(self, Value: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWebBrowserApp(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IWebBrowser
    _iid_ = Guid('{0002df05-0000-0000-c000-000000000046}')
    @commethod(32)
    def Quit(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def ClientToWindow(self, pcx: POINTER(Int32), pcy: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def PutProperty(self, Property: win32more.Windows.Win32.Foundation.BSTR, vtValue: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetProperty(self, Property: win32more.Windows.Win32.Foundation.BSTR, pvtValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def get_Name(self, Name: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def get_HWND(self, pHWND: POINTER(win32more.Windows.Win32.Foundation.SHANDLE_PTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def get_FullName(self, FullName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def get_Path(self, Path: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def get_Visible(self, pBool: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(41)
    def put_Visible(self, Value: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(42)
    def get_StatusBar(self, pBool: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(43)
    def put_StatusBar(self, Value: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(44)
    def get_StatusText(self, StatusText: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(45)
    def put_StatusText(self, StatusText: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(46)
    def get_ToolBar(self, Value: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(47)
    def put_ToolBar(self, Value: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(48)
    def get_MenuBar(self, Value: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(49)
    def put_MenuBar(self, Value: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(50)
    def get_FullScreen(self, pbFullScreen: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(51)
    def put_FullScreen(self, bFullScreen: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWebWizardExtension(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IWizardExtension
    _iid_ = Guid('{0e6b3f66-98d1-48c0-a222-fbde74e2fbc5}')
    @commethod(6)
    def SetInitialURL(self, pszURL: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetErrorURL(self, pszErrorURL: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWebWizardHost(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{18bcc359-4990-4bfb-b951-3c83702be5f9}')
    @commethod(7)
    def FinalBack(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def FinalNext(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Cancel(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Caption(self, bstrCaption: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Caption(self, pbstrCaption: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Property(self, bstrPropertyName: win32more.Windows.Win32.Foundation.BSTR, pvProperty: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Property(self, bstrPropertyName: win32more.Windows.Win32.Foundation.BSTR, pvProperty: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def SetWizardButtons(self, vfEnableBack: win32more.Windows.Win32.Foundation.VARIANT_BOOL, vfEnableNext: win32more.Windows.Win32.Foundation.VARIANT_BOOL, vfLastPage: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def SetHeaderText(self, bstrHeaderTitle: win32more.Windows.Win32.Foundation.BSTR, bstrHeaderSubtitle: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWebWizardHost2(ComPtr):
    extends: win32more.Windows.Win32.UI.Shell.IWebWizardHost
    _iid_ = Guid('{f9c013dc-3c23-4041-8e39-cfb402f7ea59}')
    @commethod(16)
    def SignString(self, value: win32more.Windows.Win32.Foundation.BSTR, signedValue: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWizardExtension(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c02ea696-86cc-491e-9b23-74394a0444a8}')
    @commethod(3)
    def AddPages(self, aPages: POINTER(win32more.Windows.Win32.UI.Controls.HPROPSHEETPAGE), cPages: UInt32, pnPagesAdded: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFirstPage(self, phpage: POINTER(win32more.Windows.Win32.UI.Controls.HPROPSHEETPAGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLastPage(self, phpage: POINTER(win32more.Windows.Win32.UI.Controls.HPROPSHEETPAGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWizardSite(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{88960f5b-422f-4e7b-8013-73415381c3c3}')
    @commethod(3)
    def GetPreviousPage(self, phpage: POINTER(win32more.Windows.Win32.UI.Controls.HPROPSHEETPAGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNextPage(self, phpage: POINTER(win32more.Windows.Win32.UI.Controls.HPROPSHEETPAGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCancelledPage(self, phpage: POINTER(win32more.Windows.Win32.UI.Controls.HPROPSHEETPAGE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
ImageProperties = Guid('{7ab770c7-0e23-4d7a-8aa2-19bfad479829}')
ImageRecompress = Guid('{6e33091c-d2f8-4740-b55e-2e11d1477a2c}')
ImageTranscode = Guid('{17b75166-928f-417d-9685-64aa135565c1}')
InputPanelConfiguration = Guid('{2853add3-f096-4c63-a78f-7fa3ea837fb7}')
InternetExplorer = Guid('{0002df01-0000-0000-c000-000000000046}')
InternetExplorerMedium = Guid('{d5e8041d-920f-45e9-b8fb-b1deb82c6e5e}')
InternetPrintOrdering = Guid('{add36aa8-751a-4579-a266-d66f5202ccbb}')
KF_CATEGORY = Int32
KF_CATEGORY_VIRTUAL: win32more.Windows.Win32.UI.Shell.KF_CATEGORY = 1
KF_CATEGORY_FIXED: win32more.Windows.Win32.UI.Shell.KF_CATEGORY = 2
KF_CATEGORY_COMMON: win32more.Windows.Win32.UI.Shell.KF_CATEGORY = 3
KF_CATEGORY_PERUSER: win32more.Windows.Win32.UI.Shell.KF_CATEGORY = 4
KNOWNDESTCATEGORY = Int32
KDC_FREQUENT: win32more.Windows.Win32.UI.Shell.KNOWNDESTCATEGORY = 1
KDC_RECENT: win32more.Windows.Win32.UI.Shell.KNOWNDESTCATEGORY = 2
class KNOWNFOLDER_DEFINITION(Structure):
    category: win32more.Windows.Win32.UI.Shell.KF_CATEGORY
    pszName: win32more.Windows.Win32.Foundation.PWSTR
    pszDescription: win32more.Windows.Win32.Foundation.PWSTR
    fidParent: Guid
    pszRelativePath: win32more.Windows.Win32.Foundation.PWSTR
    pszParsingName: win32more.Windows.Win32.Foundation.PWSTR
    pszTooltip: win32more.Windows.Win32.Foundation.PWSTR
    pszLocalizedName: win32more.Windows.Win32.Foundation.PWSTR
    pszIcon: win32more.Windows.Win32.Foundation.PWSTR
    pszSecurity: win32more.Windows.Win32.Foundation.PWSTR
    dwAttributes: UInt32
    kfdFlags: UInt32
    ftidType: Guid
KNOWN_FOLDER_FLAG = Int32
KF_FLAG_DEFAULT: win32more.Windows.Win32.UI.Shell.KNOWN_FOLDER_FLAG = 0
KF_FLAG_FORCE_APP_DATA_REDIRECTION: win32more.Windows.Win32.UI.Shell.KNOWN_FOLDER_FLAG = 524288
KF_FLAG_RETURN_FILTER_REDIRECTION_TARGET: win32more.Windows.Win32.UI.Shell.KNOWN_FOLDER_FLAG = 262144
KF_FLAG_FORCE_PACKAGE_REDIRECTION: win32more.Windows.Win32.UI.Shell.KNOWN_FOLDER_FLAG = 131072
KF_FLAG_NO_PACKAGE_REDIRECTION: win32more.Windows.Win32.UI.Shell.KNOWN_FOLDER_FLAG = 65536
KF_FLAG_FORCE_APPCONTAINER_REDIRECTION: win32more.Windows.Win32.UI.Shell.KNOWN_FOLDER_FLAG = 131072
KF_FLAG_NO_APPCONTAINER_REDIRECTION: win32more.Windows.Win32.UI.Shell.KNOWN_FOLDER_FLAG = 65536
KF_FLAG_CREATE: win32more.Windows.Win32.UI.Shell.KNOWN_FOLDER_FLAG = 32768
KF_FLAG_DONT_VERIFY: win32more.Windows.Win32.UI.Shell.KNOWN_FOLDER_FLAG = 16384
KF_FLAG_DONT_UNEXPAND: win32more.Windows.Win32.UI.Shell.KNOWN_FOLDER_FLAG = 8192
KF_FLAG_NO_ALIAS: win32more.Windows.Win32.UI.Shell.KNOWN_FOLDER_FLAG = 4096
KF_FLAG_INIT: win32more.Windows.Win32.UI.Shell.KNOWN_FOLDER_FLAG = 2048
KF_FLAG_DEFAULT_PATH: win32more.Windows.Win32.UI.Shell.KNOWN_FOLDER_FLAG = 1024
KF_FLAG_NOT_PARENT_RELATIVE: win32more.Windows.Win32.UI.Shell.KNOWN_FOLDER_FLAG = 512
KF_FLAG_SIMPLE_IDLIST: win32more.Windows.Win32.UI.Shell.KNOWN_FOLDER_FLAG = 256
KF_FLAG_ALIAS_ONLY: win32more.Windows.Win32.UI.Shell.KNOWN_FOLDER_FLAG = -2147483648
KnownFolderManager = Guid('{4df0c730-df9d-4ae3-9153-aa6b82e9795a}')
LIBRARYFOLDERFILTER = Int32
LFF_FORCEFILESYSTEM: win32more.Windows.Win32.UI.Shell.LIBRARYFOLDERFILTER = 1
LFF_STORAGEITEMS: win32more.Windows.Win32.UI.Shell.LIBRARYFOLDERFILTER = 2
LFF_ALLITEMS: win32more.Windows.Win32.UI.Shell.LIBRARYFOLDERFILTER = 3
LIBRARYMANAGEDIALOGOPTIONS = Int32
LMD_DEFAULT: win32more.Windows.Win32.UI.Shell.LIBRARYMANAGEDIALOGOPTIONS = 0
LMD_ALLOWUNINDEXABLENETWORKLOCATIONS: win32more.Windows.Win32.UI.Shell.LIBRARYMANAGEDIALOGOPTIONS = 1
LIBRARYOPTIONFLAGS = Int32
LOF_DEFAULT: win32more.Windows.Win32.UI.Shell.LIBRARYOPTIONFLAGS = 0
LOF_PINNEDTONAVPANE: win32more.Windows.Win32.UI.Shell.LIBRARYOPTIONFLAGS = 1
LOF_MASK_ALL: win32more.Windows.Win32.UI.Shell.LIBRARYOPTIONFLAGS = 1
LIBRARYSAVEFLAGS = Int32
LSF_FAILIFTHERE: win32more.Windows.Win32.UI.Shell.LIBRARYSAVEFLAGS = 0
LSF_OVERRIDEEXISTING: win32more.Windows.Win32.UI.Shell.LIBRARYSAVEFLAGS = 1
LSF_MAKEUNIQUENAME: win32more.Windows.Win32.UI.Shell.LIBRARYSAVEFLAGS = 2
@winfunctype_pointer
def LPFNDFMCALLBACK(psf: win32more.Windows.Win32.UI.Shell.IShellFolder, hwnd: win32more.Windows.Win32.Foundation.HWND, pdtobj: win32more.Windows.Win32.System.Com.IDataObject, uMsg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def LPFNVIEWCALLBACK(psvOuter: win32more.Windows.Win32.UI.Shell.IShellView, psf: win32more.Windows.Win32.UI.Shell.IShellFolder, hwndMain: win32more.Windows.Win32.Foundation.HWND, uMsg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.HRESULT: ...
LocalThumbnailCache = Guid('{50ef4544-ac9f-4a8e-b21b-8a26180db13f}')
MENUBANDHANDLERCID = Int32
MBHANDCID_PIDLSELECT: win32more.Windows.Win32.UI.Shell.MENUBANDHANDLERCID = 0
MENUPOPUPPOPUPFLAGS = Int32
MPPF_SETFOCUS: win32more.Windows.Win32.UI.Shell.MENUPOPUPPOPUPFLAGS = 1
MPPF_INITIALSELECT: win32more.Windows.Win32.UI.Shell.MENUPOPUPPOPUPFLAGS = 2
MPPF_NOANIMATE: win32more.Windows.Win32.UI.Shell.MENUPOPUPPOPUPFLAGS = 4
MPPF_KEYBOARD: win32more.Windows.Win32.UI.Shell.MENUPOPUPPOPUPFLAGS = 16
MPPF_REPOSITION: win32more.Windows.Win32.UI.Shell.MENUPOPUPPOPUPFLAGS = 32
MPPF_FORCEZORDER: win32more.Windows.Win32.UI.Shell.MENUPOPUPPOPUPFLAGS = 64
MPPF_FINALSELECT: win32more.Windows.Win32.UI.Shell.MENUPOPUPPOPUPFLAGS = 128
MPPF_TOP: win32more.Windows.Win32.UI.Shell.MENUPOPUPPOPUPFLAGS = 536870912
MPPF_LEFT: win32more.Windows.Win32.UI.Shell.MENUPOPUPPOPUPFLAGS = 1073741824
MPPF_RIGHT: win32more.Windows.Win32.UI.Shell.MENUPOPUPPOPUPFLAGS = 1610612736
MPPF_BOTTOM: win32more.Windows.Win32.UI.Shell.MENUPOPUPPOPUPFLAGS = -2147483648
MPPF_POS_MASK: win32more.Windows.Win32.UI.Shell.MENUPOPUPPOPUPFLAGS = -536870912
MPPF_ALIGN_LEFT: win32more.Windows.Win32.UI.Shell.MENUPOPUPPOPUPFLAGS = 33554432
MPPF_ALIGN_RIGHT: win32more.Windows.Win32.UI.Shell.MENUPOPUPPOPUPFLAGS = 67108864
MENUPOPUPSELECT = Int32
MPOS_EXECUTE: win32more.Windows.Win32.UI.Shell.MENUPOPUPSELECT = 0
MPOS_FULLCANCEL: win32more.Windows.Win32.UI.Shell.MENUPOPUPSELECT = 1
MPOS_CANCELLEVEL: win32more.Windows.Win32.UI.Shell.MENUPOPUPSELECT = 2
MPOS_SELECTLEFT: win32more.Windows.Win32.UI.Shell.MENUPOPUPSELECT = 3
MPOS_SELECTRIGHT: win32more.Windows.Win32.UI.Shell.MENUPOPUPSELECT = 4
MPOS_CHILDTRACKING: win32more.Windows.Win32.UI.Shell.MENUPOPUPSELECT = 5
MERGE_UPDATE_STATUS = Int32
MUS_COMPLETE: win32more.Windows.Win32.UI.Shell.MERGE_UPDATE_STATUS = 0
MUS_USERINPUTNEEDED: win32more.Windows.Win32.UI.Shell.MERGE_UPDATE_STATUS = 1
MUS_FAILED: win32more.Windows.Win32.UI.Shell.MERGE_UPDATE_STATUS = 2
MIMEASSOCIATIONDIALOG_IN_FLAGS = Int32
MIMEASSOCDLG_FL_REGISTER_ASSOC: win32more.Windows.Win32.UI.Shell.MIMEASSOCIATIONDIALOG_IN_FLAGS = 1
MM_FLAGS = UInt32
MM_ADDSEPARATOR: win32more.Windows.Win32.UI.Shell.MM_FLAGS = 1
MM_SUBMENUSHAVEIDS: win32more.Windows.Win32.UI.Shell.MM_FLAGS = 2
MM_DONTREMOVESEPS: win32more.Windows.Win32.UI.Shell.MM_FLAGS = 4
MONITOR_APP_VISIBILITY = Int32
MAV_UNKNOWN: win32more.Windows.Win32.UI.Shell.MONITOR_APP_VISIBILITY = 0
MAV_NO_APP_VISIBLE: win32more.Windows.Win32.UI.Shell.MONITOR_APP_VISIBILITY = 1
MAV_APP_VISIBLE: win32more.Windows.Win32.UI.Shell.MONITOR_APP_VISIBILITY = 2
class MULTIKEYHELPA(Structure):
    mkSize: UInt32
    mkKeylist: win32more.Windows.Win32.Foundation.CHAR
    szKeyphrase: win32more.Windows.Win32.Foundation.CHAR * 1
class MULTIKEYHELPW(Structure):
    mkSize: UInt32
    mkKeylist: Char
    szKeyphrase: Char * 1
MULTIKEYHELP = UnicodeAlias('MULTIKEYHELPW')
MailRecipient = Guid('{9e56be60-c50f-11cf-9a2c-00a0c90a90ce}')
MergedCategorizer = Guid('{8e827c11-33e7-4bc1-b242-8cd9a1c2b304}')
NAMESPACEWALKFLAG = Int32
NSWF_DEFAULT: win32more.Windows.Win32.UI.Shell.NAMESPACEWALKFLAG = 0
NSWF_NONE_IMPLIES_ALL: win32more.Windows.Win32.UI.Shell.NAMESPACEWALKFLAG = 1
NSWF_ONE_IMPLIES_ALL: win32more.Windows.Win32.UI.Shell.NAMESPACEWALKFLAG = 2
NSWF_DONT_TRAVERSE_LINKS: win32more.Windows.Win32.UI.Shell.NAMESPACEWALKFLAG = 4
NSWF_DONT_ACCUMULATE_RESULT: win32more.Windows.Win32.UI.Shell.NAMESPACEWALKFLAG = 8
NSWF_TRAVERSE_STREAM_JUNCTIONS: win32more.Windows.Win32.UI.Shell.NAMESPACEWALKFLAG = 16
NSWF_FILESYSTEM_ONLY: win32more.Windows.Win32.UI.Shell.NAMESPACEWALKFLAG = 32
NSWF_SHOW_PROGRESS: win32more.Windows.Win32.UI.Shell.NAMESPACEWALKFLAG = 64
NSWF_FLAG_VIEWORDER: win32more.Windows.Win32.UI.Shell.NAMESPACEWALKFLAG = 128
NSWF_IGNORE_AUTOPLAY_HIDA: win32more.Windows.Win32.UI.Shell.NAMESPACEWALKFLAG = 256
NSWF_ASYNC: win32more.Windows.Win32.UI.Shell.NAMESPACEWALKFLAG = 512
NSWF_DONT_RESOLVE_LINKS: win32more.Windows.Win32.UI.Shell.NAMESPACEWALKFLAG = 1024
NSWF_ACCUMULATE_FOLDERS: win32more.Windows.Win32.UI.Shell.NAMESPACEWALKFLAG = 2048
NSWF_DONT_SORT: win32more.Windows.Win32.UI.Shell.NAMESPACEWALKFLAG = 4096
NSWF_USE_TRANSFER_MEDIUM: win32more.Windows.Win32.UI.Shell.NAMESPACEWALKFLAG = 8192
NSWF_DONT_TRAVERSE_STREAM_JUNCTIONS: win32more.Windows.Win32.UI.Shell.NAMESPACEWALKFLAG = 16384
NSWF_ANY_IMPLIES_ALL: win32more.Windows.Win32.UI.Shell.NAMESPACEWALKFLAG = 32768
NATIVE_DISPLAY_ORIENTATION = Int32
NDO_LANDSCAPE: win32more.Windows.Win32.UI.Shell.NATIVE_DISPLAY_ORIENTATION = 0
NDO_PORTRAIT: win32more.Windows.Win32.UI.Shell.NATIVE_DISPLAY_ORIENTATION = 1
class NC_ADDRESS(Structure):
    pAddrInfo: POINTER(win32more.Windows.Win32.NetworkManagement.IpHelper.NET_ADDRESS_INFO)
    PortNumber: UInt16
    PrefixLength: Byte
class NEWCPLINFOA(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    dwHelpContext: UInt32
    lData: IntPtr
    hIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON
    szName: win32more.Windows.Win32.Foundation.CHAR * 32
    szInfo: win32more.Windows.Win32.Foundation.CHAR * 64
    szHelpFile: win32more.Windows.Win32.Foundation.CHAR * 128
    _pack_ = 1
class NEWCPLINFOW(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    dwHelpContext: UInt32
    lData: IntPtr
    hIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON
    szName: Char * 32
    szInfo: Char * 64
    szHelpFile: Char * 128
    _pack_ = 1
NEWCPLINFO = UnicodeAlias('NEWCPLINFOW')
if ARCH in 'X64,ARM64':
    class NOTIFYICONDATAA(Structure):
        cbSize: UInt32
        hWnd: win32more.Windows.Win32.Foundation.HWND
        uID: UInt32
        uFlags: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_DATA_FLAGS
        uCallbackMessage: UInt32
        hIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON
        szTip: win32more.Windows.Win32.Foundation.CHAR * 128
        dwState: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_STATE
        dwStateMask: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_STATE
        szInfo: win32more.Windows.Win32.Foundation.CHAR * 256
        Anonymous: _Anonymous_e__Union
        szInfoTitle: win32more.Windows.Win32.Foundation.CHAR * 64
        dwInfoFlags: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_INFOTIP_FLAGS
        guidItem: Guid
        hBalloonIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON
        class _Anonymous_e__Union(Union):
            uTimeout: UInt32
            uVersion: UInt32
elif ARCH in 'X86':
    class NOTIFYICONDATAA(Structure):
        cbSize: UInt32
        hWnd: win32more.Windows.Win32.Foundation.HWND
        uID: UInt32
        uFlags: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_DATA_FLAGS
        uCallbackMessage: UInt32
        hIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON
        szTip: win32more.Windows.Win32.Foundation.CHAR * 128
        dwState: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_STATE
        dwStateMask: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_STATE
        szInfo: win32more.Windows.Win32.Foundation.CHAR * 256
        Anonymous: _Anonymous_e__Union
        szInfoTitle: win32more.Windows.Win32.Foundation.CHAR * 64
        dwInfoFlags: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_INFOTIP_FLAGS
        guidItem: Guid
        hBalloonIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON
        _pack_ = 1
        class _Anonymous_e__Union(Union):
            uTimeout: UInt32
            uVersion: UInt32
            _pack_ = 1
if ARCH in 'X64,ARM64':
    class NOTIFYICONDATAW(Structure):
        cbSize: UInt32
        hWnd: win32more.Windows.Win32.Foundation.HWND
        uID: UInt32
        uFlags: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_DATA_FLAGS
        uCallbackMessage: UInt32
        hIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON
        szTip: Char * 128
        dwState: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_STATE
        dwStateMask: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_STATE
        szInfo: Char * 256
        Anonymous: _Anonymous_e__Union
        szInfoTitle: Char * 64
        dwInfoFlags: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_INFOTIP_FLAGS
        guidItem: Guid
        hBalloonIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON
        class _Anonymous_e__Union(Union):
            uTimeout: UInt32
            uVersion: UInt32
elif ARCH in 'X86':
    class NOTIFYICONDATAW(Structure):
        cbSize: UInt32
        hWnd: win32more.Windows.Win32.Foundation.HWND
        uID: UInt32
        uFlags: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_DATA_FLAGS
        uCallbackMessage: UInt32
        hIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON
        szTip: Char * 128
        dwState: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_STATE
        dwStateMask: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_STATE
        szInfo: Char * 256
        Anonymous: _Anonymous_e__Union
        szInfoTitle: Char * 64
        dwInfoFlags: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_INFOTIP_FLAGS
        guidItem: Guid
        hBalloonIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON
        _pack_ = 1
        class _Anonymous_e__Union(Union):
            uTimeout: UInt32
            uVersion: UInt32
            _pack_ = 1
if ARCH in 'X64,ARM64':
    NOTIFYICONDATA = UnicodeAlias('NOTIFYICONDATAW')
elif ARCH in 'X86':
    NOTIFYICONDATA = UnicodeAlias('NOTIFYICONDATAW')
if ARCH in 'X64,ARM64':
    class NOTIFYICONIDENTIFIER(Structure):
        cbSize: UInt32
        hWnd: win32more.Windows.Win32.Foundation.HWND
        uID: UInt32
        guidItem: Guid
elif ARCH in 'X86':
    class NOTIFYICONIDENTIFIER(Structure):
        cbSize: UInt32
        hWnd: win32more.Windows.Win32.Foundation.HWND
        uID: UInt32
        guidItem: Guid
        _pack_ = 1
NOTIFY_ICON_DATA_FLAGS = UInt32
NIF_MESSAGE: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_DATA_FLAGS = 1
NIF_ICON: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_DATA_FLAGS = 2
NIF_TIP: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_DATA_FLAGS = 4
NIF_STATE: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_DATA_FLAGS = 8
NIF_INFO: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_DATA_FLAGS = 16
NIF_GUID: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_DATA_FLAGS = 32
NIF_REALTIME: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_DATA_FLAGS = 64
NIF_SHOWTIP: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_DATA_FLAGS = 128
NOTIFY_ICON_INFOTIP_FLAGS = UInt32
NIIF_NONE: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_INFOTIP_FLAGS = 0
NIIF_INFO: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_INFOTIP_FLAGS = 1
NIIF_WARNING: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_INFOTIP_FLAGS = 2
NIIF_ERROR: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_INFOTIP_FLAGS = 3
NIIF_USER: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_INFOTIP_FLAGS = 4
NIIF_ICON_MASK: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_INFOTIP_FLAGS = 15
NIIF_NOSOUND: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_INFOTIP_FLAGS = 16
NIIF_LARGE_ICON: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_INFOTIP_FLAGS = 32
NIIF_RESPECT_QUIET_TIME: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_INFOTIP_FLAGS = 128
NOTIFY_ICON_MESSAGE = UInt32
NIM_ADD: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_MESSAGE = 0
NIM_MODIFY: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_MESSAGE = 1
NIM_DELETE: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_MESSAGE = 2
NIM_SETFOCUS: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_MESSAGE = 3
NIM_SETVERSION: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_MESSAGE = 4
NOTIFY_ICON_STATE = UInt32
NIS_HIDDEN: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_STATE = 1
NIS_SHAREDICON: win32more.Windows.Win32.UI.Shell.NOTIFY_ICON_STATE = 2
NPCredentialProvider = Guid('{3dd6bec0-8193-4ffe-ae25-e08e39ea4063}')
class NRESARRAY(Structure):
    cItems: UInt32
    nr: win32more.Windows.Win32.NetworkManagement.WNet.NETRESOURCEA * 1
class NSTCCUSTOMDRAW(Structure):
    psi: win32more.Windows.Win32.UI.Shell.IShellItem
    uItemState: UInt32
    nstcis: UInt32
    pszText: win32more.Windows.Win32.Foundation.PWSTR
    iImage: Int32
    himl: win32more.Windows.Win32.UI.Controls.HIMAGELIST
    iLevel: Int32
    iIndent: Int32
NSTCFOLDERCAPABILITIES = Int32
NSTCFC_NONE: win32more.Windows.Win32.UI.Shell.NSTCFOLDERCAPABILITIES = 0
NSTCFC_PINNEDITEMFILTERING: win32more.Windows.Win32.UI.Shell.NSTCFOLDERCAPABILITIES = 1
NSTCFC_DELAY_REGISTER_NOTIFY: win32more.Windows.Win32.UI.Shell.NSTCFOLDERCAPABILITIES = 2
NSTCGNI = Int32
NSTCGNI_NEXT: win32more.Windows.Win32.UI.Shell.NSTCGNI = 0
NSTCGNI_NEXTVISIBLE: win32more.Windows.Win32.UI.Shell.NSTCGNI = 1
NSTCGNI_PREV: win32more.Windows.Win32.UI.Shell.NSTCGNI = 2
NSTCGNI_PREVVISIBLE: win32more.Windows.Win32.UI.Shell.NSTCGNI = 3
NSTCGNI_PARENT: win32more.Windows.Win32.UI.Shell.NSTCGNI = 4
NSTCGNI_CHILD: win32more.Windows.Win32.UI.Shell.NSTCGNI = 5
NSTCGNI_FIRSTVISIBLE: win32more.Windows.Win32.UI.Shell.NSTCGNI = 6
NSTCGNI_LASTVISIBLE: win32more.Windows.Win32.UI.Shell.NSTCGNI = 7
NSTCSTYLE2 = Int32
NSTCS2_DEFAULT: win32more.Windows.Win32.UI.Shell.NSTCSTYLE2 = 0
NSTCS2_INTERRUPTNOTIFICATIONS: win32more.Windows.Win32.UI.Shell.NSTCSTYLE2 = 1
NSTCS2_SHOWNULLSPACEMENU: win32more.Windows.Win32.UI.Shell.NSTCSTYLE2 = 2
NSTCS2_DISPLAYPADDING: win32more.Windows.Win32.UI.Shell.NSTCSTYLE2 = 4
NSTCS2_DISPLAYPINNEDONLY: win32more.Windows.Win32.UI.Shell.NSTCSTYLE2 = 8
NTSCS2_NOSINGLETONAUTOEXPAND: win32more.Windows.Win32.UI.Shell.NSTCSTYLE2 = 16
NTSCS2_NEVERINSERTNONENUMERATED: win32more.Windows.Win32.UI.Shell.NSTCSTYLE2 = 32
class NT_CONSOLE_PROPS(Structure):
    dbh: win32more.Windows.Win32.UI.Shell.DATABLOCK_HEADER
    wFillAttribute: UInt16
    wPopupFillAttribute: UInt16
    dwScreenBufferSize: win32more.Windows.Win32.System.Console.COORD
    dwWindowSize: win32more.Windows.Win32.System.Console.COORD
    dwWindowOrigin: win32more.Windows.Win32.System.Console.COORD
    nFont: UInt32
    nInputBufferSize: UInt32
    dwFontSize: win32more.Windows.Win32.System.Console.COORD
    uFontFamily: UInt32
    uFontWeight: UInt32
    FaceName: Char * 32
    uCursorSize: UInt32
    bFullScreen: win32more.Windows.Win32.Foundation.BOOL
    bQuickEdit: win32more.Windows.Win32.Foundation.BOOL
    bInsertMode: win32more.Windows.Win32.Foundation.BOOL
    bAutoPosition: win32more.Windows.Win32.Foundation.BOOL
    uHistoryBufferSize: UInt32
    uNumberOfHistoryBuffers: UInt32
    bHistoryNoDup: win32more.Windows.Win32.Foundation.BOOL
    ColorTable: win32more.Windows.Win32.Foundation.COLORREF * 16
    _pack_ = 1
class NT_FE_CONSOLE_PROPS(Structure):
    dbh: win32more.Windows.Win32.UI.Shell.DATABLOCK_HEADER
    uCodePage: UInt32
    _pack_ = 1
NWMF = Int32
NWMF_UNLOADING: win32more.Windows.Win32.UI.Shell.NWMF = 1
NWMF_USERINITED: win32more.Windows.Win32.UI.Shell.NWMF = 2
NWMF_FIRST: win32more.Windows.Win32.UI.Shell.NWMF = 4
NWMF_OVERRIDEKEY: win32more.Windows.Win32.UI.Shell.NWMF = 8
NWMF_SHOWHELP: win32more.Windows.Win32.UI.Shell.NWMF = 16
NWMF_HTMLDIALOG: win32more.Windows.Win32.UI.Shell.NWMF = 32
NWMF_FROMDIALOGCHILD: win32more.Windows.Win32.UI.Shell.NWMF = 64
NWMF_USERREQUESTED: win32more.Windows.Win32.UI.Shell.NWMF = 128
NWMF_USERALLOWED: win32more.Windows.Win32.UI.Shell.NWMF = 256
NWMF_FORCEWINDOW: win32more.Windows.Win32.UI.Shell.NWMF = 65536
NWMF_FORCETAB: win32more.Windows.Win32.UI.Shell.NWMF = 131072
NWMF_SUGGESTWINDOW: win32more.Windows.Win32.UI.Shell.NWMF = 262144
NWMF_SUGGESTTAB: win32more.Windows.Win32.UI.Shell.NWMF = 524288
NWMF_INACTIVETAB: win32more.Windows.Win32.UI.Shell.NWMF = 1048576
NamespaceTreeControl = Guid('{ae054212-3535-4430-83ed-d501aa6680e6}')
NamespaceWalker = Guid('{72eb61e0-8672-4303-9175-f2e4c68b2e7c}')
NetworkConnections = Guid('{7007acc7-3202-11d1-aad2-00805fc1270e}')
NetworkExplorerFolder = Guid('{f02c1a0d-be21-4350-88b0-7367fc96ef3c}')
NetworkPlaces = Guid('{208d2c60-3aea-1069-a2d7-08002b30309d}')
NewProcessCauseConstants = Int32
ProtectedModeRedirect: win32more.Windows.Win32.UI.Shell.NewProcessCauseConstants = 1
class OPENASINFO(Structure):
    pcszFile: win32more.Windows.Win32.Foundation.PWSTR
    pcszClass: win32more.Windows.Win32.Foundation.PWSTR
    oaifInFlags: win32more.Windows.Win32.UI.Shell.OPEN_AS_INFO_FLAGS
OPEN_AS_INFO_FLAGS = Int32
OAIF_ALLOW_REGISTRATION: win32more.Windows.Win32.UI.Shell.OPEN_AS_INFO_FLAGS = 1
OAIF_REGISTER_EXT: win32more.Windows.Win32.UI.Shell.OPEN_AS_INFO_FLAGS = 2
OAIF_EXEC: win32more.Windows.Win32.UI.Shell.OPEN_AS_INFO_FLAGS = 4
OAIF_FORCE_REGISTRATION: win32more.Windows.Win32.UI.Shell.OPEN_AS_INFO_FLAGS = 8
OAIF_HIDE_REGISTRATION: win32more.Windows.Win32.UI.Shell.OPEN_AS_INFO_FLAGS = 32
OAIF_URL_PROTOCOL: win32more.Windows.Win32.UI.Shell.OPEN_AS_INFO_FLAGS = 64
OAIF_FILE_IS_URI: win32more.Windows.Win32.UI.Shell.OPEN_AS_INFO_FLAGS = 128
if ARCH in 'X64,ARM64':
    class OPEN_PRINTER_PROPS_INFOA(Structure):
        dwSize: UInt32
        pszSheetName: win32more.Windows.Win32.Foundation.PSTR
        uSheetIndex: UInt32
        dwFlags: UInt32
        bModal: win32more.Windows.Win32.Foundation.BOOL
elif ARCH in 'X86':
    class OPEN_PRINTER_PROPS_INFOA(Structure):
        dwSize: UInt32
        pszSheetName: win32more.Windows.Win32.Foundation.PSTR
        uSheetIndex: UInt32
        dwFlags: UInt32
        bModal: win32more.Windows.Win32.Foundation.BOOL
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class OPEN_PRINTER_PROPS_INFOW(Structure):
        dwSize: UInt32
        pszSheetName: win32more.Windows.Win32.Foundation.PWSTR
        uSheetIndex: UInt32
        dwFlags: UInt32
        bModal: win32more.Windows.Win32.Foundation.BOOL
elif ARCH in 'X86':
    class OPEN_PRINTER_PROPS_INFOW(Structure):
        dwSize: UInt32
        pszSheetName: win32more.Windows.Win32.Foundation.PWSTR
        uSheetIndex: UInt32
        dwFlags: UInt32
        bModal: win32more.Windows.Win32.Foundation.BOOL
        _pack_ = 1
if ARCH in 'X64,ARM64':
    OPEN_PRINTER_PROPS_INFO = UnicodeAlias('OPEN_PRINTER_PROPS_INFOW')
elif ARCH in 'X86':
    OPEN_PRINTER_PROPS_INFO = UnicodeAlias('OPEN_PRINTER_PROPS_INFOW')
OS = UInt32
OS_WINDOWS: win32more.Windows.Win32.UI.Shell.OS = 0
OS_NT: win32more.Windows.Win32.UI.Shell.OS = 1
OS_WIN95ORGREATER: win32more.Windows.Win32.UI.Shell.OS = 2
OS_NT4ORGREATER: win32more.Windows.Win32.UI.Shell.OS = 3
OS_WIN98ORGREATER: win32more.Windows.Win32.UI.Shell.OS = 5
OS_WIN98_GOLD: win32more.Windows.Win32.UI.Shell.OS = 6
OS_WIN2000ORGREATER: win32more.Windows.Win32.UI.Shell.OS = 7
OS_WIN2000PRO: win32more.Windows.Win32.UI.Shell.OS = 8
OS_WIN2000SERVER: win32more.Windows.Win32.UI.Shell.OS = 9
OS_WIN2000ADVSERVER: win32more.Windows.Win32.UI.Shell.OS = 10
OS_WIN2000DATACENTER: win32more.Windows.Win32.UI.Shell.OS = 11
OS_WIN2000TERMINAL: win32more.Windows.Win32.UI.Shell.OS = 12
OS_EMBEDDED: win32more.Windows.Win32.UI.Shell.OS = 13
OS_TERMINALCLIENT: win32more.Windows.Win32.UI.Shell.OS = 14
OS_TERMINALREMOTEADMIN: win32more.Windows.Win32.UI.Shell.OS = 15
OS_WIN95_GOLD: win32more.Windows.Win32.UI.Shell.OS = 16
OS_MEORGREATER: win32more.Windows.Win32.UI.Shell.OS = 17
OS_XPORGREATER: win32more.Windows.Win32.UI.Shell.OS = 18
OS_HOME: win32more.Windows.Win32.UI.Shell.OS = 19
OS_PROFESSIONAL: win32more.Windows.Win32.UI.Shell.OS = 20
OS_DATACENTER: win32more.Windows.Win32.UI.Shell.OS = 21
OS_ADVSERVER: win32more.Windows.Win32.UI.Shell.OS = 22
OS_SERVER: win32more.Windows.Win32.UI.Shell.OS = 23
OS_TERMINALSERVER: win32more.Windows.Win32.UI.Shell.OS = 24
OS_PERSONALTERMINALSERVER: win32more.Windows.Win32.UI.Shell.OS = 25
OS_FASTUSERSWITCHING: win32more.Windows.Win32.UI.Shell.OS = 26
OS_WELCOMELOGONUI: win32more.Windows.Win32.UI.Shell.OS = 27
OS_DOMAINMEMBER: win32more.Windows.Win32.UI.Shell.OS = 28
OS_ANYSERVER: win32more.Windows.Win32.UI.Shell.OS = 29
OS_WOW6432: win32more.Windows.Win32.UI.Shell.OS = 30
OS_WEBSERVER: win32more.Windows.Win32.UI.Shell.OS = 31
OS_SMALLBUSINESSSERVER: win32more.Windows.Win32.UI.Shell.OS = 32
OS_TABLETPC: win32more.Windows.Win32.UI.Shell.OS = 33
OS_SERVERADMINUI: win32more.Windows.Win32.UI.Shell.OS = 34
OS_MEDIACENTER: win32more.Windows.Win32.UI.Shell.OS = 35
OS_APPLIANCE: win32more.Windows.Win32.UI.Shell.OS = 36
OfflineFolderStatus = Int32
OFS_INACTIVE: win32more.Windows.Win32.UI.Shell.OfflineFolderStatus = -1
OFS_ONLINE: win32more.Windows.Win32.UI.Shell.OfflineFolderStatus = 0
OFS_OFFLINE: win32more.Windows.Win32.UI.Shell.OfflineFolderStatus = 1
OFS_SERVERBACK: win32more.Windows.Win32.UI.Shell.OfflineFolderStatus = 2
OFS_DIRTYCACHE: win32more.Windows.Win32.UI.Shell.OfflineFolderStatus = 3
OnexCredentialProvider = Guid('{07aa0886-cc8d-4e19-a410-1c75af686e62}')
OnexPlapSmartcardCredentialProvider = Guid('{33c86cd6-705f-4ba1-9adb-67070b837775}')
OpenControlPanel = Guid('{06622d85-6856-4460-8de1-a81921b41c4b}')
PACKAGE_EXECUTION_STATE = Int32
PES_UNKNOWN: win32more.Windows.Win32.UI.Shell.PACKAGE_EXECUTION_STATE = 0
PES_RUNNING: win32more.Windows.Win32.UI.Shell.PACKAGE_EXECUTION_STATE = 1
PES_SUSPENDING: win32more.Windows.Win32.UI.Shell.PACKAGE_EXECUTION_STATE = 2
PES_SUSPENDED: win32more.Windows.Win32.UI.Shell.PACKAGE_EXECUTION_STATE = 3
PES_TERMINATED: win32more.Windows.Win32.UI.Shell.PACKAGE_EXECUTION_STATE = 4
@winfunctype_pointer
def PAPPCONSTRAIN_CHANGE_ROUTINE(Constrained: win32more.Windows.Win32.Foundation.BOOLEAN, Context: VoidPtr) -> Void: ...
PAPPCONSTRAIN_REGISTRATION = IntPtr
@winfunctype_pointer
def PAPPSTATE_CHANGE_ROUTINE(Quiesced: win32more.Windows.Win32.Foundation.BOOLEAN, Context: VoidPtr) -> Void: ...
PAPPSTATE_REGISTRATION = IntPtr
class PARSEDURLA(Structure):
    cbSize: UInt32
    pszProtocol: win32more.Windows.Win32.Foundation.PSTR
    cchProtocol: UInt32
    pszSuffix: win32more.Windows.Win32.Foundation.PSTR
    cchSuffix: UInt32
    nScheme: UInt32
class PARSEDURLW(Structure):
    cbSize: UInt32
    pszProtocol: win32more.Windows.Win32.Foundation.PWSTR
    cchProtocol: UInt32
    pszSuffix: win32more.Windows.Win32.Foundation.PWSTR
    cchSuffix: UInt32
    nScheme: UInt32
PARSEDURL = UnicodeAlias('PARSEDURLW')
PATHCCH_OPTIONS = UInt32
PATHCCH_NONE: win32more.Windows.Win32.UI.Shell.PATHCCH_OPTIONS = 0
PATHCCH_ALLOW_LONG_PATHS: win32more.Windows.Win32.UI.Shell.PATHCCH_OPTIONS = 1
PATHCCH_FORCE_ENABLE_LONG_NAME_PROCESS: win32more.Windows.Win32.UI.Shell.PATHCCH_OPTIONS = 2
PATHCCH_FORCE_DISABLE_LONG_NAME_PROCESS: win32more.Windows.Win32.UI.Shell.PATHCCH_OPTIONS = 4
PATHCCH_DO_NOT_NORMALIZE_SEGMENTS: win32more.Windows.Win32.UI.Shell.PATHCCH_OPTIONS = 8
PATHCCH_ENSURE_IS_EXTENDED_LENGTH_PATH: win32more.Windows.Win32.UI.Shell.PATHCCH_OPTIONS = 16
PATHCCH_ENSURE_TRAILING_SLASH: win32more.Windows.Win32.UI.Shell.PATHCCH_OPTIONS = 32
PATHCCH_CANONICALIZE_SLASHES: win32more.Windows.Win32.UI.Shell.PATHCCH_OPTIONS = 64
PCS_RET = UInt32
PCS_FATAL: win32more.Windows.Win32.UI.Shell.PCS_RET = 2147483648
PCS_REPLACEDCHAR: win32more.Windows.Win32.UI.Shell.PCS_RET = 1
PCS_REMOVEDCHAR: win32more.Windows.Win32.UI.Shell.PCS_RET = 2
PCS_TRUNCATED: win32more.Windows.Win32.UI.Shell.PCS_RET = 4
PCS_PATHTOOLONG: win32more.Windows.Win32.UI.Shell.PCS_RET = 8
class PERSIST_FOLDER_TARGET_INFO(Structure):
    pidlTargetFolder: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)
    szTargetParsingName: Char * 260
    szNetworkProvider: Char * 260
    dwAttributes: UInt32
    csidl: Int32
@winfunctype_pointer
def PFNCANSHAREFOLDERW(pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def PFNSHOWSHAREFOLDERUIW(hwndParent: win32more.Windows.Win32.Foundation.HWND, pszPath: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
PIDISF_FLAGS = Int32
PIDISF_RECENTLYCHANGED: win32more.Windows.Win32.UI.Shell.PIDISF_FLAGS = 1
PIDISF_CACHEDSTICKY: win32more.Windows.Win32.UI.Shell.PIDISF_FLAGS = 2
PIDISF_CACHEIMAGES: win32more.Windows.Win32.UI.Shell.PIDISF_FLAGS = 16
PIDISF_FOLLOWALLLINKS: win32more.Windows.Win32.UI.Shell.PIDISF_FLAGS = 32
PIDISM_OPTIONS = Int32
PIDISM_GLOBAL: win32more.Windows.Win32.UI.Shell.PIDISM_OPTIONS = 0
PIDISM_WATCH: win32more.Windows.Win32.UI.Shell.PIDISM_OPTIONS = 1
PIDISM_DONTWATCH: win32more.Windows.Win32.UI.Shell.PIDISM_OPTIONS = 2
PIDISR_INFO = Int32
PIDISR_UP_TO_DATE: win32more.Windows.Win32.UI.Shell.PIDISR_INFO = 0
PIDISR_NEEDS_ADD: win32more.Windows.Win32.UI.Shell.PIDISR_INFO = 1
PIDISR_NEEDS_UPDATE: win32more.Windows.Win32.UI.Shell.PIDISR_INFO = 2
PIDISR_NEEDS_DELETE: win32more.Windows.Win32.UI.Shell.PIDISR_INFO = 3
PID_INTSITE = Int32
PID_INTSITE_WHATSNEW: win32more.Windows.Win32.UI.Shell.PID_INTSITE = 2
PID_INTSITE_AUTHOR: win32more.Windows.Win32.UI.Shell.PID_INTSITE = 3
PID_INTSITE_LASTVISIT: win32more.Windows.Win32.UI.Shell.PID_INTSITE = 4
PID_INTSITE_LASTMOD: win32more.Windows.Win32.UI.Shell.PID_INTSITE = 5
PID_INTSITE_VISITCOUNT: win32more.Windows.Win32.UI.Shell.PID_INTSITE = 6
PID_INTSITE_DESCRIPTION: win32more.Windows.Win32.UI.Shell.PID_INTSITE = 7
PID_INTSITE_COMMENT: win32more.Windows.Win32.UI.Shell.PID_INTSITE = 8
PID_INTSITE_FLAGS: win32more.Windows.Win32.UI.Shell.PID_INTSITE = 9
PID_INTSITE_CONTENTLEN: win32more.Windows.Win32.UI.Shell.PID_INTSITE = 10
PID_INTSITE_CONTENTCODE: win32more.Windows.Win32.UI.Shell.PID_INTSITE = 11
PID_INTSITE_RECURSE: win32more.Windows.Win32.UI.Shell.PID_INTSITE = 12
PID_INTSITE_WATCH: win32more.Windows.Win32.UI.Shell.PID_INTSITE = 13
PID_INTSITE_SUBSCRIPTION: win32more.Windows.Win32.UI.Shell.PID_INTSITE = 14
PID_INTSITE_URL: win32more.Windows.Win32.UI.Shell.PID_INTSITE = 15
PID_INTSITE_TITLE: win32more.Windows.Win32.UI.Shell.PID_INTSITE = 16
PID_INTSITE_CODEPAGE: win32more.Windows.Win32.UI.Shell.PID_INTSITE = 18
PID_INTSITE_TRACKING: win32more.Windows.Win32.UI.Shell.PID_INTSITE = 19
PID_INTSITE_ICONINDEX: win32more.Windows.Win32.UI.Shell.PID_INTSITE = 20
PID_INTSITE_ICONFILE: win32more.Windows.Win32.UI.Shell.PID_INTSITE = 21
PID_INTSITE_ROAMED: win32more.Windows.Win32.UI.Shell.PID_INTSITE = 34
PID_IS = Int32
PID_IS_URL: win32more.Windows.Win32.UI.Shell.PID_IS = 2
PID_IS_NAME: win32more.Windows.Win32.UI.Shell.PID_IS = 4
PID_IS_WORKINGDIR: win32more.Windows.Win32.UI.Shell.PID_IS = 5
PID_IS_HOTKEY: win32more.Windows.Win32.UI.Shell.PID_IS = 6
PID_IS_SHOWCMD: win32more.Windows.Win32.UI.Shell.PID_IS = 7
PID_IS_ICONINDEX: win32more.Windows.Win32.UI.Shell.PID_IS = 8
PID_IS_ICONFILE: win32more.Windows.Win32.UI.Shell.PID_IS = 9
PID_IS_WHATSNEW: win32more.Windows.Win32.UI.Shell.PID_IS = 10
PID_IS_AUTHOR: win32more.Windows.Win32.UI.Shell.PID_IS = 11
PID_IS_DESCRIPTION: win32more.Windows.Win32.UI.Shell.PID_IS = 12
PID_IS_COMMENT: win32more.Windows.Win32.UI.Shell.PID_IS = 13
PID_IS_ROAMED: win32more.Windows.Win32.UI.Shell.PID_IS = 15
PINLogonCredentialProvider = Guid('{cb82ea12-9f71-446d-89e1-8d0924e1256e}')
class PREVIEWHANDLERFRAMEINFO(Structure):
    haccel: win32more.Windows.Win32.UI.WindowsAndMessaging.HACCEL
    cAccelEntries: UInt32
PRF_FLAGS = Int32
PRF_VERIFYEXISTS: win32more.Windows.Win32.UI.Shell.PRF_FLAGS = 1
PRF_TRYPROGRAMEXTENSIONS: win32more.Windows.Win32.UI.Shell.PRF_FLAGS = 3
PRF_FIRSTDIRDEF: win32more.Windows.Win32.UI.Shell.PRF_FLAGS = 4
PRF_DONTFINDLNK: win32more.Windows.Win32.UI.Shell.PRF_FLAGS = 8
PRF_REQUIREABSOLUTE: win32more.Windows.Win32.UI.Shell.PRF_FLAGS = 16
class PROFILEINFOA(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    lpUserName: win32more.Windows.Win32.Foundation.PSTR
    lpProfilePath: win32more.Windows.Win32.Foundation.PSTR
    lpDefaultPath: win32more.Windows.Win32.Foundation.PSTR
    lpServerName: win32more.Windows.Win32.Foundation.PSTR
    lpPolicyPath: win32more.Windows.Win32.Foundation.PSTR
    hProfile: win32more.Windows.Win32.Foundation.HANDLE
class PROFILEINFOW(Structure):
    dwSize: UInt32
    dwFlags: UInt32
    lpUserName: win32more.Windows.Win32.Foundation.PWSTR
    lpProfilePath: win32more.Windows.Win32.Foundation.PWSTR
    lpDefaultPath: win32more.Windows.Win32.Foundation.PWSTR
    lpServerName: win32more.Windows.Win32.Foundation.PWSTR
    lpPolicyPath: win32more.Windows.Win32.Foundation.PWSTR
    hProfile: win32more.Windows.Win32.Foundation.HANDLE
PROFILEINFO = UnicodeAlias('PROFILEINFOW')
class PUBAPPINFO(Structure):
    cbSize: UInt32
    dwMask: UInt32
    pszSource: win32more.Windows.Win32.Foundation.PWSTR
    stAssigned: win32more.Windows.Win32.Foundation.SYSTEMTIME
    stPublished: win32more.Windows.Win32.Foundation.SYSTEMTIME
    stScheduled: win32more.Windows.Win32.Foundation.SYSTEMTIME
    stExpire: win32more.Windows.Win32.Foundation.SYSTEMTIME
PUBAPPINFOFLAGS = Int32
PAI_SOURCE: win32more.Windows.Win32.UI.Shell.PUBAPPINFOFLAGS = 1
PAI_ASSIGNEDTIME: win32more.Windows.Win32.UI.Shell.PUBAPPINFOFLAGS = 2
PAI_PUBLISHEDTIME: win32more.Windows.Win32.UI.Shell.PUBAPPINFOFLAGS = 4
PAI_SCHEDULEDTIME: win32more.Windows.Win32.UI.Shell.PUBAPPINFOFLAGS = 8
PAI_EXPIRETIME: win32more.Windows.Win32.UI.Shell.PUBAPPINFOFLAGS = 16
PackageDebugSettings = Guid('{b1aec16f-2383-4852-b0e9-8f0b1dc66b4d}')
PasswordCredentialProvider = Guid('{60b78e88-ead8-445c-9cfd-0b87f74ea6cd}')
PreviousVersions = Guid('{596ab062-b4d2-4215-9f74-e9109b0a8153}')
PropertiesUI = Guid('{d912f8cf-0396-4915-884e-fb425d32943b}')
PublishDropTarget = Guid('{cc6eeffb-43f6-46c5-9619-51d571967f7d}')
PublishingWizard = Guid('{6b33163c-76a5-4b6c-bf21-45de9cd503a1}')
class QCMINFO(Structure):
    hmenu: win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU
    indexMenu: UInt32
    idCmdFirst: UInt32
    idCmdLast: UInt32
    pIdMap: POINTER(win32more.Windows.Win32.UI.Shell.QCMINFO_IDMAP)
class QCMINFO_IDMAP(Structure):
    nMaxIds: UInt32
    pIdList: win32more.Windows.Win32.UI.Shell.QCMINFO_IDMAP_PLACEMENT * 1
class QCMINFO_IDMAP_PLACEMENT(Structure):
    id: UInt32
    fFlags: UInt32
class QITAB(Structure):
    piid: POINTER(Guid)
    dwOffset: UInt32
QITIPF_FLAGS = Int32
QITIPF_DEFAULT: win32more.Windows.Win32.UI.Shell.QITIPF_FLAGS = 0
QITIPF_USENAME: win32more.Windows.Win32.UI.Shell.QITIPF_FLAGS = 1
QITIPF_LINKNOTARGET: win32more.Windows.Win32.UI.Shell.QITIPF_FLAGS = 2
QITIPF_LINKUSETARGET: win32more.Windows.Win32.UI.Shell.QITIPF_FLAGS = 4
QITIPF_USESLOWTIP: win32more.Windows.Win32.UI.Shell.QITIPF_FLAGS = 8
QITIPF_SINGLELINE: win32more.Windows.Win32.UI.Shell.QITIPF_FLAGS = 16
QIF_CACHED: win32more.Windows.Win32.UI.Shell.QITIPF_FLAGS = 1
QIF_DONTEXPANDFOLDER: win32more.Windows.Win32.UI.Shell.QITIPF_FLAGS = 2
QUERY_USER_NOTIFICATION_STATE = Int32
QUNS_NOT_PRESENT: win32more.Windows.Win32.UI.Shell.QUERY_USER_NOTIFICATION_STATE = 1
QUNS_BUSY: win32more.Windows.Win32.UI.Shell.QUERY_USER_NOTIFICATION_STATE = 2
QUNS_RUNNING_D3D_FULL_SCREEN: win32more.Windows.Win32.UI.Shell.QUERY_USER_NOTIFICATION_STATE = 3
QUNS_PRESENTATION_MODE: win32more.Windows.Win32.UI.Shell.QUERY_USER_NOTIFICATION_STATE = 4
QUNS_ACCEPTS_NOTIFICATIONS: win32more.Windows.Win32.UI.Shell.QUERY_USER_NOTIFICATION_STATE = 5
QUNS_QUIET_TIME: win32more.Windows.Win32.UI.Shell.QUERY_USER_NOTIFICATION_STATE = 6
QUNS_APP: win32more.Windows.Win32.UI.Shell.QUERY_USER_NOTIFICATION_STATE = 7
QueryCancelAutoPlay = Guid('{331f1768-05a9-4ddd-b86e-dae34ddc998a}')
RASProvider = Guid('{5537e283-b1e7-4ef8-9c6e-7ab0afe5056d}')
RESTRICTIONS = Int32
REST_NONE: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 0
REST_NORUN: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1
REST_NOCLOSE: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 2
REST_NOSAVESET: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 4
REST_NOFILEMENU: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 8
REST_NOSETFOLDERS: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 16
REST_NOSETTASKBAR: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 32
REST_NODESKTOP: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 64
REST_NOFIND: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 128
REST_NODRIVES: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 256
REST_NODRIVEAUTORUN: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 512
REST_NODRIVETYPEAUTORUN: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1024
REST_NONETHOOD: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 2048
REST_STARTBANNER: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 4096
REST_RESTRICTRUN: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 8192
REST_NOPRINTERTABS: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 16384
REST_NOPRINTERDELETE: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 32768
REST_NOPRINTERADD: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 65536
REST_NOSTARTMENUSUBFOLDERS: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 131072
REST_MYDOCSONNET: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 262144
REST_NOEXITTODOS: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 524288
REST_ENFORCESHELLEXTSECURITY: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1048576
REST_LINKRESOLVEIGNORELINKINFO: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 2097152
REST_NOCOMMONGROUPS: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 4194304
REST_SEPARATEDESKTOPPROCESS: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 8388608
REST_NOWEB: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 16777216
REST_NOTRAYCONTEXTMENU: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 33554432
REST_NOVIEWCONTEXTMENU: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 67108864
REST_NONETCONNECTDISCONNECT: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 134217728
REST_STARTMENULOGOFF: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 268435456
REST_NOSETTINGSASSIST: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 536870912
REST_NOINTERNETICON: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741825
REST_NORECENTDOCSHISTORY: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741826
REST_NORECENTDOCSMENU: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741827
REST_NOACTIVEDESKTOP: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741828
REST_NOACTIVEDESKTOPCHANGES: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741829
REST_NOFAVORITESMENU: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741830
REST_CLEARRECENTDOCSONEXIT: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741831
REST_CLASSICSHELL: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741832
REST_NOCUSTOMIZEWEBVIEW: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741833
REST_NOHTMLWALLPAPER: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741840
REST_NOCHANGINGWALLPAPER: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741841
REST_NODESKCOMP: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741842
REST_NOADDDESKCOMP: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741843
REST_NODELDESKCOMP: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741844
REST_NOCLOSEDESKCOMP: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741845
REST_NOCLOSE_DRAGDROPBAND: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741846
REST_NOMOVINGBAND: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741847
REST_NOEDITDESKCOMP: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741848
REST_NORESOLVESEARCH: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741849
REST_NORESOLVETRACK: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741850
REST_FORCECOPYACLWITHFILE: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741851
REST_NOFORGETSOFTWAREUPDATE: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741853
REST_NOSETACTIVEDESKTOP: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741854
REST_NOUPDATEWINDOWS: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741855
REST_NOCHANGESTARMENU: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741856
REST_NOFOLDEROPTIONS: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741857
REST_HASFINDCOMPUTERS: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741858
REST_INTELLIMENUS: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741859
REST_RUNDLGMEMCHECKBOX: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741860
REST_ARP_ShowPostSetup: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741861
REST_NOCSC: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741862
REST_NOCONTROLPANEL: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741863
REST_ENUMWORKGROUP: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741864
REST_ARP_NOARP: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741865
REST_ARP_NOREMOVEPAGE: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741866
REST_ARP_NOADDPAGE: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741867
REST_ARP_NOWINSETUPPAGE: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741868
REST_GREYMSIADS: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741869
REST_NOCHANGEMAPPEDDRIVELABEL: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741870
REST_NOCHANGEMAPPEDDRIVECOMMENT: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741871
REST_MaxRecentDocs: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741872
REST_NONETWORKCONNECTIONS: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741873
REST_FORCESTARTMENULOGOFF: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741874
REST_NOWEBVIEW: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741875
REST_NOCUSTOMIZETHISFOLDER: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741876
REST_NOENCRYPTION: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741877
REST_DONTSHOWSUPERHIDDEN: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741879
REST_NOSHELLSEARCHBUTTON: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741880
REST_NOHARDWARETAB: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741881
REST_NORUNASINSTALLPROMPT: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741882
REST_PROMPTRUNASINSTALLNETPATH: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741883
REST_NOMANAGEMYCOMPUTERVERB: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741884
REST_DISALLOWRUN: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741886
REST_NOWELCOMESCREEN: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741887
REST_RESTRICTCPL: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741888
REST_DISALLOWCPL: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741889
REST_NOSMBALLOONTIP: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741890
REST_NOSMHELP: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741891
REST_NOWINKEYS: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741892
REST_NOENCRYPTONMOVE: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741893
REST_NOLOCALMACHINERUN: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741894
REST_NOCURRENTUSERRUN: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741895
REST_NOLOCALMACHINERUNONCE: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741896
REST_NOCURRENTUSERRUNONCE: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741897
REST_FORCEACTIVEDESKTOPON: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741898
REST_NOVIEWONDRIVE: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741900
REST_NONETCRAWL: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741901
REST_NOSHAREDDOCUMENTS: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741902
REST_NOSMMYDOCS: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741903
REST_NOSMMYPICS: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741904
REST_ALLOWBITBUCKDRIVES: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741905
REST_NONLEGACYSHELLMODE: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741906
REST_NOCONTROLPANELBARRICADE: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741907
REST_NOSTARTPAGE: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741908
REST_NOAUTOTRAYNOTIFY: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741909
REST_NOTASKGROUPING: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741910
REST_NOCDBURNING: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741911
REST_MYCOMPNOPROP: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741912
REST_MYDOCSNOPROP: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741913
REST_NOSTARTPANEL: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741914
REST_NODISPLAYAPPEARANCEPAGE: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741915
REST_NOTHEMESTAB: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741916
REST_NOVISUALSTYLECHOICE: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741917
REST_NOSIZECHOICE: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741918
REST_NOCOLORCHOICE: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741919
REST_SETVISUALSTYLE: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741920
REST_STARTRUNNOHOMEPATH: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741921
REST_NOUSERNAMEINSTARTPANEL: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741922
REST_NOMYCOMPUTERICON: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741923
REST_NOSMNETWORKPLACES: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741924
REST_NOSMPINNEDLIST: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741925
REST_NOSMMYMUSIC: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741926
REST_NOSMEJECTPC: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741927
REST_NOSMMOREPROGRAMS: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741928
REST_NOSMMFUPROGRAMS: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741929
REST_NOTRAYITEMSDISPLAY: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741930
REST_NOTOOLBARSONTASKBAR: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741931
REST_NOSMCONFIGUREPROGRAMS: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741935
REST_HIDECLOCK: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741936
REST_NOLOWDISKSPACECHECKS: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741937
REST_NOENTIRENETWORK: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741938
REST_NODESKTOPCLEANUP: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741939
REST_BITBUCKNUKEONDELETE: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741940
REST_BITBUCKCONFIRMDELETE: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741941
REST_BITBUCKNOPROP: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741942
REST_NODISPBACKGROUND: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741943
REST_NODISPSCREENSAVEPG: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741944
REST_NODISPSETTINGSPG: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741945
REST_NODISPSCREENSAVEPREVIEW: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741946
REST_NODISPLAYCPL: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741947
REST_HIDERUNASVERB: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741948
REST_NOTHUMBNAILCACHE: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741949
REST_NOSTRCMPLOGICAL: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741950
REST_NOPUBLISHWIZARD: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741951
REST_NOONLINEPRINTSWIZARD: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741952
REST_NOWEBSERVICES: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741953
REST_ALLOWUNHASHEDWEBVIEW: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741954
REST_ALLOWLEGACYWEBVIEW: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741955
REST_REVERTWEBVIEWSECURITY: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741956
REST_INHERITCONSOLEHANDLES: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741958
REST_NOREMOTERECURSIVEEVENTS: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741961
REST_NOREMOTECHANGENOTIFY: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741969
REST_NOENUMENTIRENETWORK: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741971
REST_NOINTERNETOPENWITH: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741973
REST_DONTRETRYBADNETNAME: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741979
REST_ALLOWFILECLSIDJUNCTIONS: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741980
REST_NOUPNPINSTALL: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741981
REST_ARP_DONTGROUPPATCHES: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741996
REST_ARP_NOCHOOSEPROGRAMSPAGE: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1073741997
REST_NODISCONNECT: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1090519041
REST_NOSECURITY: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1090519042
REST_NOFILEASSOCIATE: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1090519043
REST_ALLOWCOMMENTTOGGLE: win32more.Windows.Win32.UI.Shell.RESTRICTIONS = 1090519044
RefreshConstants = Int32
REFRESH_NORMAL: win32more.Windows.Win32.UI.Shell.RefreshConstants = 0
REFRESH_IFEXPIRED: win32more.Windows.Win32.UI.Shell.RefreshConstants = 1
REFRESH_COMPLETELY: win32more.Windows.Win32.UI.Shell.RefreshConstants = 3
SCALE_CHANGE_FLAGS = Int32
SCF_VALUE_NONE: win32more.Windows.Win32.UI.Shell.SCALE_CHANGE_FLAGS = 0
SCF_SCALE: win32more.Windows.Win32.UI.Shell.SCALE_CHANGE_FLAGS = 1
SCF_PHYSICAL: win32more.Windows.Win32.UI.Shell.SCALE_CHANGE_FLAGS = 2
SCNRT_STATUS = Int32
SCNRT_ENABLE: win32more.Windows.Win32.UI.Shell.SCNRT_STATUS = 0
SCNRT_DISABLE: win32more.Windows.Win32.UI.Shell.SCNRT_STATUS = 1
SECURELOCKCODE = Int32
SECURELOCK_NOCHANGE: win32more.Windows.Win32.UI.Shell.SECURELOCKCODE = -1
SECURELOCK_SET_UNSECURE: win32more.Windows.Win32.UI.Shell.SECURELOCKCODE = 0
SECURELOCK_SET_MIXED: win32more.Windows.Win32.UI.Shell.SECURELOCKCODE = 1
SECURELOCK_SET_SECUREUNKNOWNBIT: win32more.Windows.Win32.UI.Shell.SECURELOCKCODE = 2
SECURELOCK_SET_SECURE40BIT: win32more.Windows.Win32.UI.Shell.SECURELOCKCODE = 3
SECURELOCK_SET_SECURE56BIT: win32more.Windows.Win32.UI.Shell.SECURELOCKCODE = 4
SECURELOCK_SET_FORTEZZA: win32more.Windows.Win32.UI.Shell.SECURELOCKCODE = 5
SECURELOCK_SET_SECURE128BIT: win32more.Windows.Win32.UI.Shell.SECURELOCKCODE = 6
SECURELOCK_FIRSTSUGGEST: win32more.Windows.Win32.UI.Shell.SECURELOCKCODE = 7
SECURELOCK_SUGGEST_UNSECURE: win32more.Windows.Win32.UI.Shell.SECURELOCKCODE = 7
SECURELOCK_SUGGEST_MIXED: win32more.Windows.Win32.UI.Shell.SECURELOCKCODE = 8
SECURELOCK_SUGGEST_SECUREUNKNOWNBIT: win32more.Windows.Win32.UI.Shell.SECURELOCKCODE = 9
SECURELOCK_SUGGEST_SECURE40BIT: win32more.Windows.Win32.UI.Shell.SECURELOCKCODE = 10
SECURELOCK_SUGGEST_SECURE56BIT: win32more.Windows.Win32.UI.Shell.SECURELOCKCODE = 11
SECURELOCK_SUGGEST_FORTEZZA: win32more.Windows.Win32.UI.Shell.SECURELOCKCODE = 12
SECURELOCK_SUGGEST_SECURE128BIT: win32more.Windows.Win32.UI.Shell.SECURELOCKCODE = 13
SFBS_FLAGS = Int32
SFBS_FLAGS_ROUND_TO_NEAREST_DISPLAYED_DIGIT: win32more.Windows.Win32.UI.Shell.SFBS_FLAGS = 1
SFBS_FLAGS_TRUNCATE_UNDISPLAYED_DECIMAL_DIGITS: win32more.Windows.Win32.UI.Shell.SFBS_FLAGS = 2
class SFVM_HELPTOPIC_DATA(Structure):
    wszHelpFile: Char * 260
    wszHelpTopic: Char * 260
SFVM_MESSAGE_ID = Int32
SFVM_MERGEMENU: win32more.Windows.Win32.UI.Shell.SFVM_MESSAGE_ID = 1
SFVM_INVOKECOMMAND: win32more.Windows.Win32.UI.Shell.SFVM_MESSAGE_ID = 2
SFVM_GETHELPTEXT: win32more.Windows.Win32.UI.Shell.SFVM_MESSAGE_ID = 3
SFVM_GETTOOLTIPTEXT: win32more.Windows.Win32.UI.Shell.SFVM_MESSAGE_ID = 4
SFVM_GETBUTTONINFO: win32more.Windows.Win32.UI.Shell.SFVM_MESSAGE_ID = 5
SFVM_GETBUTTONS: win32more.Windows.Win32.UI.Shell.SFVM_MESSAGE_ID = 6
SFVM_INITMENUPOPUP: win32more.Windows.Win32.UI.Shell.SFVM_MESSAGE_ID = 7
SFVM_FSNOTIFY: win32more.Windows.Win32.UI.Shell.SFVM_MESSAGE_ID = 14
SFVM_WINDOWCREATED: win32more.Windows.Win32.UI.Shell.SFVM_MESSAGE_ID = 15
SFVM_GETDETAILSOF: win32more.Windows.Win32.UI.Shell.SFVM_MESSAGE_ID = 23
SFVM_COLUMNCLICK: win32more.Windows.Win32.UI.Shell.SFVM_MESSAGE_ID = 24
SFVM_QUERYFSNOTIFY: win32more.Windows.Win32.UI.Shell.SFVM_MESSAGE_ID = 25
SFVM_DEFITEMCOUNT: win32more.Windows.Win32.UI.Shell.SFVM_MESSAGE_ID = 26
SFVM_DEFVIEWMODE: win32more.Windows.Win32.UI.Shell.SFVM_MESSAGE_ID = 27
SFVM_UNMERGEMENU: win32more.Windows.Win32.UI.Shell.SFVM_MESSAGE_ID = 28
SFVM_UPDATESTATUSBAR: win32more.Windows.Win32.UI.Shell.SFVM_MESSAGE_ID = 31
SFVM_BACKGROUNDENUM: win32more.Windows.Win32.UI.Shell.SFVM_MESSAGE_ID = 32
SFVM_DIDDRAGDROP: win32more.Windows.Win32.UI.Shell.SFVM_MESSAGE_ID = 36
SFVM_SETISFV: win32more.Windows.Win32.UI.Shell.SFVM_MESSAGE_ID = 39
SFVM_THISIDLIST: win32more.Windows.Win32.UI.Shell.SFVM_MESSAGE_ID = 41
SFVM_ADDPROPERTYPAGES: win32more.Windows.Win32.UI.Shell.SFVM_MESSAGE_ID = 47
SFVM_BACKGROUNDENUMDONE: win32more.Windows.Win32.UI.Shell.SFVM_MESSAGE_ID = 48
SFVM_GETNOTIFY: win32more.Windows.Win32.UI.Shell.SFVM_MESSAGE_ID = 49
SFVM_GETSORTDEFAULTS: win32more.Windows.Win32.UI.Shell.SFVM_MESSAGE_ID = 53
SFVM_SIZE: win32more.Windows.Win32.UI.Shell.SFVM_MESSAGE_ID = 57
SFVM_GETZONE: win32more.Windows.Win32.UI.Shell.SFVM_MESSAGE_ID = 58
SFVM_GETPANE: win32more.Windows.Win32.UI.Shell.SFVM_MESSAGE_ID = 59
SFVM_GETHELPTOPIC: win32more.Windows.Win32.UI.Shell.SFVM_MESSAGE_ID = 63
SFVM_GETANIMATION: win32more.Windows.Win32.UI.Shell.SFVM_MESSAGE_ID = 68
class SFVM_PROPPAGE_DATA(Structure):
    dwReserved: UInt32
    pfn: win32more.Windows.Win32.UI.Controls.LPFNSVADDPROPSHEETPAGE
    lParam: win32more.Windows.Win32.Foundation.LPARAM
SFVS_SELECT = Int32
SFVS_SELECT_NONE: win32more.Windows.Win32.UI.Shell.SFVS_SELECT = 0
SFVS_SELECT_ALLITEMS: win32more.Windows.Win32.UI.Shell.SFVS_SELECT = 1
SFVS_SELECT_INVERT: win32more.Windows.Win32.UI.Shell.SFVS_SELECT = 2
class SFV_CREATE(Structure):
    cbSize: UInt32
    pshf: win32more.Windows.Win32.UI.Shell.IShellFolder
    psvOuter: win32more.Windows.Win32.UI.Shell.IShellView
    psfvcb: win32more.Windows.Win32.UI.Shell.IShellFolderViewCB
class SFV_SETITEMPOS(Structure):
    pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)
    pt: win32more.Windows.Win32.Foundation.POINT
SHARD = Int32
SHARD_PIDL: win32more.Windows.Win32.UI.Shell.SHARD = 1
SHARD_PATHA: win32more.Windows.Win32.UI.Shell.SHARD = 2
SHARD_PATHW: win32more.Windows.Win32.UI.Shell.SHARD = 3
SHARD_APPIDINFO: win32more.Windows.Win32.UI.Shell.SHARD = 4
SHARD_APPIDINFOIDLIST: win32more.Windows.Win32.UI.Shell.SHARD = 5
SHARD_LINK: win32more.Windows.Win32.UI.Shell.SHARD = 6
SHARD_APPIDINFOLINK: win32more.Windows.Win32.UI.Shell.SHARD = 7
SHARD_SHELLITEM: win32more.Windows.Win32.UI.Shell.SHARD = 8
class SHARDAPPIDINFO(Structure):
    psi: win32more.Windows.Win32.UI.Shell.IShellItem
    pszAppID: win32more.Windows.Win32.Foundation.PWSTR
    _pack_ = 1
class SHARDAPPIDINFOIDLIST(Structure):
    pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)
    pszAppID: win32more.Windows.Win32.Foundation.PWSTR
    _pack_ = 1
class SHARDAPPIDINFOLINK(Structure):
    psl: win32more.Windows.Win32.UI.Shell.IShellLinkA
    pszAppID: win32more.Windows.Win32.Foundation.PWSTR
    _pack_ = 1
SHARE_ROLE = Int32
SHARE_ROLE_INVALID: win32more.Windows.Win32.UI.Shell.SHARE_ROLE = -1
SHARE_ROLE_READER: win32more.Windows.Win32.UI.Shell.SHARE_ROLE = 0
SHARE_ROLE_CONTRIBUTOR: win32more.Windows.Win32.UI.Shell.SHARE_ROLE = 1
SHARE_ROLE_CO_OWNER: win32more.Windows.Win32.UI.Shell.SHARE_ROLE = 2
SHARE_ROLE_OWNER: win32more.Windows.Win32.UI.Shell.SHARE_ROLE = 3
SHARE_ROLE_CUSTOM: win32more.Windows.Win32.UI.Shell.SHARE_ROLE = 4
SHARE_ROLE_MIXED: win32more.Windows.Win32.UI.Shell.SHARE_ROLE = 5
SHCNE_ID = UInt32
SHCNE_RENAMEITEM: win32more.Windows.Win32.UI.Shell.SHCNE_ID = 1
SHCNE_CREATE: win32more.Windows.Win32.UI.Shell.SHCNE_ID = 2
SHCNE_DELETE: win32more.Windows.Win32.UI.Shell.SHCNE_ID = 4
SHCNE_MKDIR: win32more.Windows.Win32.UI.Shell.SHCNE_ID = 8
SHCNE_RMDIR: win32more.Windows.Win32.UI.Shell.SHCNE_ID = 16
SHCNE_MEDIAINSERTED: win32more.Windows.Win32.UI.Shell.SHCNE_ID = 32
SHCNE_MEDIAREMOVED: win32more.Windows.Win32.UI.Shell.SHCNE_ID = 64
SHCNE_DRIVEREMOVED: win32more.Windows.Win32.UI.Shell.SHCNE_ID = 128
SHCNE_DRIVEADD: win32more.Windows.Win32.UI.Shell.SHCNE_ID = 256
SHCNE_NETSHARE: win32more.Windows.Win32.UI.Shell.SHCNE_ID = 512
SHCNE_NETUNSHARE: win32more.Windows.Win32.UI.Shell.SHCNE_ID = 1024
SHCNE_ATTRIBUTES: win32more.Windows.Win32.UI.Shell.SHCNE_ID = 2048
SHCNE_UPDATEDIR: win32more.Windows.Win32.UI.Shell.SHCNE_ID = 4096
SHCNE_UPDATEITEM: win32more.Windows.Win32.UI.Shell.SHCNE_ID = 8192
SHCNE_SERVERDISCONNECT: win32more.Windows.Win32.UI.Shell.SHCNE_ID = 16384
SHCNE_UPDATEIMAGE: win32more.Windows.Win32.UI.Shell.SHCNE_ID = 32768
SHCNE_DRIVEADDGUI: win32more.Windows.Win32.UI.Shell.SHCNE_ID = 65536
SHCNE_RENAMEFOLDER: win32more.Windows.Win32.UI.Shell.SHCNE_ID = 131072
SHCNE_FREESPACE: win32more.Windows.Win32.UI.Shell.SHCNE_ID = 262144
SHCNE_EXTENDED_EVENT: win32more.Windows.Win32.UI.Shell.SHCNE_ID = 67108864
SHCNE_ASSOCCHANGED: win32more.Windows.Win32.UI.Shell.SHCNE_ID = 134217728
SHCNE_DISKEVENTS: win32more.Windows.Win32.UI.Shell.SHCNE_ID = 145439
SHCNE_GLOBALEVENTS: win32more.Windows.Win32.UI.Shell.SHCNE_ID = 201687520
SHCNE_ALLEVENTS: win32more.Windows.Win32.UI.Shell.SHCNE_ID = 2147483647
SHCNE_INTERRUPT: win32more.Windows.Win32.UI.Shell.SHCNE_ID = 2147483648
SHCNF_FLAGS = UInt32
SHCNF_IDLIST: win32more.Windows.Win32.UI.Shell.SHCNF_FLAGS = 0
SHCNF_PATHA: win32more.Windows.Win32.UI.Shell.SHCNF_FLAGS = 1
SHCNF_PRINTERA: win32more.Windows.Win32.UI.Shell.SHCNF_FLAGS = 2
SHCNF_DWORD: win32more.Windows.Win32.UI.Shell.SHCNF_FLAGS = 3
SHCNF_PATHW: win32more.Windows.Win32.UI.Shell.SHCNF_FLAGS = 5
SHCNF_PRINTERW: win32more.Windows.Win32.UI.Shell.SHCNF_FLAGS = 6
SHCNF_TYPE: win32more.Windows.Win32.UI.Shell.SHCNF_FLAGS = 255
SHCNF_FLUSH: win32more.Windows.Win32.UI.Shell.SHCNF_FLAGS = 4096
SHCNF_FLUSHNOWAIT: win32more.Windows.Win32.UI.Shell.SHCNF_FLAGS = 12288
SHCNF_NOTIFYRECURSIVE: win32more.Windows.Win32.UI.Shell.SHCNF_FLAGS = 65536
SHCNF_PATH: win32more.Windows.Win32.UI.Shell.SHCNF_FLAGS = 5
SHCNF_PRINTER: win32more.Windows.Win32.UI.Shell.SHCNF_FLAGS = 6
SHCNRF_SOURCE = Int32
SHCNRF_InterruptLevel: win32more.Windows.Win32.UI.Shell.SHCNRF_SOURCE = 1
SHCNRF_ShellLevel: win32more.Windows.Win32.UI.Shell.SHCNRF_SOURCE = 2
SHCNRF_RecursiveInterrupt: win32more.Windows.Win32.UI.Shell.SHCNRF_SOURCE = 4096
SHCNRF_NewDelivery: win32more.Windows.Win32.UI.Shell.SHCNRF_SOURCE = 32768
class SHCOLUMNDATA(Structure):
    dwFlags: UInt32
    dwFileAttributes: UInt32
    dwReserved: UInt32
    pwszExt: win32more.Windows.Win32.Foundation.PWSTR
    wszFile: Char * 260
class SHCOLUMNINFO(Structure):
    scid: win32more.Windows.Win32.Foundation.PROPERTYKEY
    vt: win32more.Windows.Win32.System.Variant.VARENUM
    fmt: UInt32
    cChars: UInt32
    csFlags: UInt32
    wszTitle: Char * 80
    wszDescription: Char * 128
    _pack_ = 1
class SHCOLUMNINIT(Structure):
    dwFlags: UInt32
    dwReserved: UInt32
    wszFolder: Char * 260
if ARCH in 'X64,ARM64':
    class SHCREATEPROCESSINFOW(Structure):
        cbSize: UInt32
        fMask: UInt32
        hwnd: win32more.Windows.Win32.Foundation.HWND
        pszFile: win32more.Windows.Win32.Foundation.PWSTR
        pszParameters: win32more.Windows.Win32.Foundation.PWSTR
        pszCurrentDirectory: win32more.Windows.Win32.Foundation.PWSTR
        hUserToken: win32more.Windows.Win32.Foundation.HANDLE
        lpProcessAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES)
        lpThreadAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES)
        bInheritHandles: win32more.Windows.Win32.Foundation.BOOL
        dwCreationFlags: UInt32
        lpStartupInfo: POINTER(win32more.Windows.Win32.System.Threading.STARTUPINFOW)
        lpProcessInformation: POINTER(win32more.Windows.Win32.System.Threading.PROCESS_INFORMATION)
elif ARCH in 'X86':
    class SHCREATEPROCESSINFOW(Structure):
        cbSize: UInt32
        fMask: UInt32
        hwnd: win32more.Windows.Win32.Foundation.HWND
        pszFile: win32more.Windows.Win32.Foundation.PWSTR
        pszParameters: win32more.Windows.Win32.Foundation.PWSTR
        pszCurrentDirectory: win32more.Windows.Win32.Foundation.PWSTR
        hUserToken: win32more.Windows.Win32.Foundation.HANDLE
        lpProcessAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES)
        lpThreadAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES)
        bInheritHandles: win32more.Windows.Win32.Foundation.BOOL
        dwCreationFlags: UInt32
        lpStartupInfo: POINTER(win32more.Windows.Win32.System.Threading.STARTUPINFOW)
        lpProcessInformation: POINTER(win32more.Windows.Win32.System.Threading.PROCESS_INFORMATION)
        _pack_ = 1
class SHChangeDWORDAsIDList(Structure):
    cb: UInt16
    dwItem1: UInt32
    dwItem2: UInt32
    cbZero: UInt16
    _pack_ = 1
class SHChangeNotifyEntry(Structure):
    pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)
    fRecursive: win32more.Windows.Win32.Foundation.BOOL
    _pack_ = 1
class SHChangeProductKeyAsIDList(Structure):
    cb: UInt16
    wszProductKey: Char * 39
    cbZero: UInt16
    _pack_ = 1
class SHChangeUpdateImageIDList(Structure):
    cb: UInt16
    iIconIndex: Int32
    iCurIndex: Int32
    uFlags: UInt32
    dwProcessID: UInt32
    szName: Char * 260
    cbZero: UInt16
    _pack_ = 1
class SHDESCRIPTIONID(Structure):
    dwDescriptionId: UInt32
    clsid: Guid
SHDID_ID = Int32
SHDID_ROOT_REGITEM: win32more.Windows.Win32.UI.Shell.SHDID_ID = 1
SHDID_FS_FILE: win32more.Windows.Win32.UI.Shell.SHDID_ID = 2
SHDID_FS_DIRECTORY: win32more.Windows.Win32.UI.Shell.SHDID_ID = 3
SHDID_FS_OTHER: win32more.Windows.Win32.UI.Shell.SHDID_ID = 4
SHDID_COMPUTER_DRIVE35: win32more.Windows.Win32.UI.Shell.SHDID_ID = 5
SHDID_COMPUTER_DRIVE525: win32more.Windows.Win32.UI.Shell.SHDID_ID = 6
SHDID_COMPUTER_REMOVABLE: win32more.Windows.Win32.UI.Shell.SHDID_ID = 7
SHDID_COMPUTER_FIXED: win32more.Windows.Win32.UI.Shell.SHDID_ID = 8
SHDID_COMPUTER_NETDRIVE: win32more.Windows.Win32.UI.Shell.SHDID_ID = 9
SHDID_COMPUTER_CDROM: win32more.Windows.Win32.UI.Shell.SHDID_ID = 10
SHDID_COMPUTER_RAMDISK: win32more.Windows.Win32.UI.Shell.SHDID_ID = 11
SHDID_COMPUTER_OTHER: win32more.Windows.Win32.UI.Shell.SHDID_ID = 12
SHDID_NET_DOMAIN: win32more.Windows.Win32.UI.Shell.SHDID_ID = 13
SHDID_NET_SERVER: win32more.Windows.Win32.UI.Shell.SHDID_ID = 14
SHDID_NET_SHARE: win32more.Windows.Win32.UI.Shell.SHDID_ID = 15
SHDID_NET_RESTOFNET: win32more.Windows.Win32.UI.Shell.SHDID_ID = 16
SHDID_NET_OTHER: win32more.Windows.Win32.UI.Shell.SHDID_ID = 17
SHDID_COMPUTER_IMAGING: win32more.Windows.Win32.UI.Shell.SHDID_ID = 18
SHDID_COMPUTER_AUDIO: win32more.Windows.Win32.UI.Shell.SHDID_ID = 19
SHDID_COMPUTER_SHAREDDOCS: win32more.Windows.Win32.UI.Shell.SHDID_ID = 20
SHDID_MOBILE_DEVICE: win32more.Windows.Win32.UI.Shell.SHDID_ID = 21
SHDID_REMOTE_DESKTOP_DRIVE: win32more.Windows.Win32.UI.Shell.SHDID_ID = 22
class SHDRAGIMAGE(Structure):
    sizeDragImage: win32more.Windows.Win32.Foundation.SIZE
    ptOffset: win32more.Windows.Win32.Foundation.POINT
    hbmpDragImage: win32more.Windows.Win32.Graphics.Gdi.HBITMAP
    crColorKey: win32more.Windows.Win32.Foundation.COLORREF
SHELLBROWSERSHOWCONTROL = Int32
SBSC_HIDE: win32more.Windows.Win32.UI.Shell.SHELLBROWSERSHOWCONTROL = 0
SBSC_SHOW: win32more.Windows.Win32.UI.Shell.SHELLBROWSERSHOWCONTROL = 1
SBSC_TOGGLE: win32more.Windows.Win32.UI.Shell.SHELLBROWSERSHOWCONTROL = 2
SBSC_QUERY: win32more.Windows.Win32.UI.Shell.SHELLBROWSERSHOWCONTROL = 3
if ARCH in 'X64,ARM64':
    class SHELLEXECUTEINFOA(Structure):
        cbSize: UInt32
        fMask: UInt32
        hwnd: win32more.Windows.Win32.Foundation.HWND
        lpVerb: win32more.Windows.Win32.Foundation.PSTR
        lpFile: win32more.Windows.Win32.Foundation.PSTR
        lpParameters: win32more.Windows.Win32.Foundation.PSTR
        lpDirectory: win32more.Windows.Win32.Foundation.PSTR
        nShow: Int32
        hInstApp: win32more.Windows.Win32.Foundation.HINSTANCE
        lpIDList: VoidPtr
        lpClass: win32more.Windows.Win32.Foundation.PSTR
        hkeyClass: win32more.Windows.Win32.System.Registry.HKEY
        dwHotKey: UInt32
        Anonymous: _Anonymous_e__Union
        hProcess: win32more.Windows.Win32.Foundation.HANDLE
        class _Anonymous_e__Union(Union):
            hIcon: win32more.Windows.Win32.Foundation.HANDLE
            hMonitor: win32more.Windows.Win32.Foundation.HANDLE
elif ARCH in 'X86':
    class SHELLEXECUTEINFOA(Structure):
        cbSize: UInt32
        fMask: UInt32
        hwnd: win32more.Windows.Win32.Foundation.HWND
        lpVerb: win32more.Windows.Win32.Foundation.PSTR
        lpFile: win32more.Windows.Win32.Foundation.PSTR
        lpParameters: win32more.Windows.Win32.Foundation.PSTR
        lpDirectory: win32more.Windows.Win32.Foundation.PSTR
        nShow: Int32
        hInstApp: win32more.Windows.Win32.Foundation.HINSTANCE
        lpIDList: VoidPtr
        lpClass: win32more.Windows.Win32.Foundation.PSTR
        hkeyClass: win32more.Windows.Win32.System.Registry.HKEY
        dwHotKey: UInt32
        Anonymous: _Anonymous_e__Union
        hProcess: win32more.Windows.Win32.Foundation.HANDLE
        _pack_ = 1
        class _Anonymous_e__Union(Union):
            hIcon: win32more.Windows.Win32.Foundation.HANDLE
            hMonitor: win32more.Windows.Win32.Foundation.HANDLE
            _pack_ = 1
if ARCH in 'X64,ARM64':
    class SHELLEXECUTEINFOW(Structure):
        cbSize: UInt32
        fMask: UInt32
        hwnd: win32more.Windows.Win32.Foundation.HWND
        lpVerb: win32more.Windows.Win32.Foundation.PWSTR
        lpFile: win32more.Windows.Win32.Foundation.PWSTR
        lpParameters: win32more.Windows.Win32.Foundation.PWSTR
        lpDirectory: win32more.Windows.Win32.Foundation.PWSTR
        nShow: Int32
        hInstApp: win32more.Windows.Win32.Foundation.HINSTANCE
        lpIDList: VoidPtr
        lpClass: win32more.Windows.Win32.Foundation.PWSTR
        hkeyClass: win32more.Windows.Win32.System.Registry.HKEY
        dwHotKey: UInt32
        Anonymous: _Anonymous_e__Union
        hProcess: win32more.Windows.Win32.Foundation.HANDLE
        class _Anonymous_e__Union(Union):
            hIcon: win32more.Windows.Win32.Foundation.HANDLE
            hMonitor: win32more.Windows.Win32.Foundation.HANDLE
elif ARCH in 'X86':
    class SHELLEXECUTEINFOW(Structure):
        cbSize: UInt32
        fMask: UInt32
        hwnd: win32more.Windows.Win32.Foundation.HWND
        lpVerb: win32more.Windows.Win32.Foundation.PWSTR
        lpFile: win32more.Windows.Win32.Foundation.PWSTR
        lpParameters: win32more.Windows.Win32.Foundation.PWSTR
        lpDirectory: win32more.Windows.Win32.Foundation.PWSTR
        nShow: Int32
        hInstApp: win32more.Windows.Win32.Foundation.HINSTANCE
        lpIDList: VoidPtr
        lpClass: win32more.Windows.Win32.Foundation.PWSTR
        hkeyClass: win32more.Windows.Win32.System.Registry.HKEY
        dwHotKey: UInt32
        Anonymous: _Anonymous_e__Union
        hProcess: win32more.Windows.Win32.Foundation.HANDLE
        _pack_ = 1
        class _Anonymous_e__Union(Union):
            hIcon: win32more.Windows.Win32.Foundation.HANDLE
            hMonitor: win32more.Windows.Win32.Foundation.HANDLE
            _pack_ = 1
if ARCH in 'X64,ARM64':
    SHELLEXECUTEINFO = UnicodeAlias('SHELLEXECUTEINFOW')
elif ARCH in 'X86':
    SHELLEXECUTEINFO = UnicodeAlias('SHELLEXECUTEINFOW')
class SHELLFLAGSTATE(Structure):
    fShowAllObjects: Annotated[Int32, 1]
    fShowExtensions: Annotated[Int32, 1]
    fNoConfirmRecycle: Annotated[Int32, 1]
    fShowSysFiles: Annotated[Int32, 1]
    fShowCompColor: Annotated[Int32, 1]
    fDoubleClickInWebView: Annotated[Int32, 1]
    fDesktopHTML: Annotated[Int32, 1]
    fWin95Classic: Annotated[Int32, 1]
    fDontPrettyPath: Annotated[Int32, 1]
    fShowAttribCol: Annotated[Int32, 1]
    fMapNetDrvBtn: Annotated[Int32, 1]
    fShowInfoTip: Annotated[Int32, 1]
    fHideIcons: Annotated[Int32, 1]
    fAutoCheckSelect: Annotated[Int32, 1]
    fIconsOnly: Annotated[Int32, 1]
    fRestFlags: Annotated[Int32, 1]
    _pack_ = 1
class SHELLSTATEA(Structure):
    fShowAllObjects: Annotated[Int32, 1]
    fShowExtensions: Annotated[Int32, 1]
    fNoConfirmRecycle: Annotated[Int32, 1]
    fShowSysFiles: Annotated[Int32, 1]
    fShowCompColor: Annotated[Int32, 1]
    fDoubleClickInWebView: Annotated[Int32, 1]
    fDesktopHTML: Annotated[Int32, 1]
    fWin95Classic: Annotated[Int32, 1]
    fDontPrettyPath: Annotated[Int32, 1]
    fShowAttribCol: Annotated[Int32, 1]
    fMapNetDrvBtn: Annotated[Int32, 1]
    fShowInfoTip: Annotated[Int32, 1]
    fHideIcons: Annotated[Int32, 1]
    fWebView: Annotated[Int32, 1]
    fFilter: Annotated[Int32, 1]
    fShowSuperHidden: Annotated[Int32, 1]
    fNoNetCrawling: Annotated[Int32, 1]
    dwWin95Unused: UInt32
    uWin95Unused: UInt32
    lParamSort: Int32
    iSortDirection: Int32
    version: UInt32
    uNotUsed: UInt32
    fSepProcess: Annotated[Int32, 1]
    fStartPanelOn: Annotated[Int32, 1]
    fShowStartPage: Annotated[Int32, 1]
    fAutoCheckSelect: Annotated[Int32, 1]
    fIconsOnly: Annotated[Int32, 1]
    fShowTypeOverlay: Annotated[Int32, 1]
    fShowStatusBar: Annotated[Int32, 1]
    fSpareFlags: Annotated[Int32, 9]
    _pack_ = 1
class SHELLSTATEW(Structure):
    fShowAllObjects: Annotated[Int32, 1]
    fShowExtensions: Annotated[Int32, 1]
    fNoConfirmRecycle: Annotated[Int32, 1]
    fShowSysFiles: Annotated[Int32, 1]
    fShowCompColor: Annotated[Int32, 1]
    fDoubleClickInWebView: Annotated[Int32, 1]
    fDesktopHTML: Annotated[Int32, 1]
    fWin95Classic: Annotated[Int32, 1]
    fDontPrettyPath: Annotated[Int32, 1]
    fShowAttribCol: Annotated[Int32, 1]
    fMapNetDrvBtn: Annotated[Int32, 1]
    fShowInfoTip: Annotated[Int32, 1]
    fHideIcons: Annotated[Int32, 1]
    fWebView: Annotated[Int32, 1]
    fFilter: Annotated[Int32, 1]
    fShowSuperHidden: Annotated[Int32, 1]
    fNoNetCrawling: Annotated[Int32, 1]
    dwWin95Unused: UInt32
    uWin95Unused: UInt32
    lParamSort: Int32
    iSortDirection: Int32
    version: UInt32
    uNotUsed: UInt32
    fSepProcess: Annotated[Int32, 1]
    fStartPanelOn: Annotated[Int32, 1]
    fShowStartPage: Annotated[Int32, 1]
    fAutoCheckSelect: Annotated[Int32, 1]
    fIconsOnly: Annotated[Int32, 1]
    fShowTypeOverlay: Annotated[Int32, 1]
    fShowStatusBar: Annotated[Int32, 1]
    fSpareFlags: Annotated[Int32, 9]
    _pack_ = 1
SHELLSTATE = UnicodeAlias('SHELLSTATEW')
SHELL_AUTOCOMPLETE_FLAGS = UInt32
SHACF_DEFAULT: win32more.Windows.Win32.UI.Shell.SHELL_AUTOCOMPLETE_FLAGS = 0
SHACF_FILESYSTEM: win32more.Windows.Win32.UI.Shell.SHELL_AUTOCOMPLETE_FLAGS = 1
SHACF_URLALL: win32more.Windows.Win32.UI.Shell.SHELL_AUTOCOMPLETE_FLAGS = 6
SHACF_URLHISTORY: win32more.Windows.Win32.UI.Shell.SHELL_AUTOCOMPLETE_FLAGS = 2
SHACF_URLMRU: win32more.Windows.Win32.UI.Shell.SHELL_AUTOCOMPLETE_FLAGS = 4
SHACF_USETAB: win32more.Windows.Win32.UI.Shell.SHELL_AUTOCOMPLETE_FLAGS = 8
SHACF_FILESYS_ONLY: win32more.Windows.Win32.UI.Shell.SHELL_AUTOCOMPLETE_FLAGS = 16
SHACF_FILESYS_DIRS: win32more.Windows.Win32.UI.Shell.SHELL_AUTOCOMPLETE_FLAGS = 32
SHACF_VIRTUAL_NAMESPACE: win32more.Windows.Win32.UI.Shell.SHELL_AUTOCOMPLETE_FLAGS = 64
SHACF_AUTOSUGGEST_FORCE_ON: win32more.Windows.Win32.UI.Shell.SHELL_AUTOCOMPLETE_FLAGS = 268435456
SHACF_AUTOSUGGEST_FORCE_OFF: win32more.Windows.Win32.UI.Shell.SHELL_AUTOCOMPLETE_FLAGS = 536870912
SHACF_AUTOAPPEND_FORCE_ON: win32more.Windows.Win32.UI.Shell.SHELL_AUTOCOMPLETE_FLAGS = 1073741824
SHACF_AUTOAPPEND_FORCE_OFF: win32more.Windows.Win32.UI.Shell.SHELL_AUTOCOMPLETE_FLAGS = 2147483648
class SHELL_ITEM_RESOURCE(Structure):
    guidType: Guid
    szName: Char * 260
SHELL_LINK_DATA_FLAGS = Int32
SLDF_DEFAULT: win32more.Windows.Win32.UI.Shell.SHELL_LINK_DATA_FLAGS = 0
SLDF_HAS_ID_LIST: win32more.Windows.Win32.UI.Shell.SHELL_LINK_DATA_FLAGS = 1
SLDF_HAS_LINK_INFO: win32more.Windows.Win32.UI.Shell.SHELL_LINK_DATA_FLAGS = 2
SLDF_HAS_NAME: win32more.Windows.Win32.UI.Shell.SHELL_LINK_DATA_FLAGS = 4
SLDF_HAS_RELPATH: win32more.Windows.Win32.UI.Shell.SHELL_LINK_DATA_FLAGS = 8
SLDF_HAS_WORKINGDIR: win32more.Windows.Win32.UI.Shell.SHELL_LINK_DATA_FLAGS = 16
SLDF_HAS_ARGS: win32more.Windows.Win32.UI.Shell.SHELL_LINK_DATA_FLAGS = 32
SLDF_HAS_ICONLOCATION: win32more.Windows.Win32.UI.Shell.SHELL_LINK_DATA_FLAGS = 64
SLDF_UNICODE: win32more.Windows.Win32.UI.Shell.SHELL_LINK_DATA_FLAGS = 128
SLDF_FORCE_NO_LINKINFO: win32more.Windows.Win32.UI.Shell.SHELL_LINK_DATA_FLAGS = 256
SLDF_HAS_EXP_SZ: win32more.Windows.Win32.UI.Shell.SHELL_LINK_DATA_FLAGS = 512
SLDF_RUN_IN_SEPARATE: win32more.Windows.Win32.UI.Shell.SHELL_LINK_DATA_FLAGS = 1024
SLDF_HAS_DARWINID: win32more.Windows.Win32.UI.Shell.SHELL_LINK_DATA_FLAGS = 4096
SLDF_RUNAS_USER: win32more.Windows.Win32.UI.Shell.SHELL_LINK_DATA_FLAGS = 8192
SLDF_HAS_EXP_ICON_SZ: win32more.Windows.Win32.UI.Shell.SHELL_LINK_DATA_FLAGS = 16384
SLDF_NO_PIDL_ALIAS: win32more.Windows.Win32.UI.Shell.SHELL_LINK_DATA_FLAGS = 32768
SLDF_FORCE_UNCNAME: win32more.Windows.Win32.UI.Shell.SHELL_LINK_DATA_FLAGS = 65536
SLDF_RUN_WITH_SHIMLAYER: win32more.Windows.Win32.UI.Shell.SHELL_LINK_DATA_FLAGS = 131072
SLDF_FORCE_NO_LINKTRACK: win32more.Windows.Win32.UI.Shell.SHELL_LINK_DATA_FLAGS = 262144
SLDF_ENABLE_TARGET_METADATA: win32more.Windows.Win32.UI.Shell.SHELL_LINK_DATA_FLAGS = 524288
SLDF_DISABLE_LINK_PATH_TRACKING: win32more.Windows.Win32.UI.Shell.SHELL_LINK_DATA_FLAGS = 1048576
SLDF_DISABLE_KNOWNFOLDER_RELATIVE_TRACKING: win32more.Windows.Win32.UI.Shell.SHELL_LINK_DATA_FLAGS = 2097152
SLDF_NO_KF_ALIAS: win32more.Windows.Win32.UI.Shell.SHELL_LINK_DATA_FLAGS = 4194304
SLDF_ALLOW_LINK_TO_LINK: win32more.Windows.Win32.UI.Shell.SHELL_LINK_DATA_FLAGS = 8388608
SLDF_UNALIAS_ON_SAVE: win32more.Windows.Win32.UI.Shell.SHELL_LINK_DATA_FLAGS = 16777216
SLDF_PREFER_ENVIRONMENT_PATH: win32more.Windows.Win32.UI.Shell.SHELL_LINK_DATA_FLAGS = 33554432
SLDF_KEEP_LOCAL_IDLIST_FOR_UNC_TARGET: win32more.Windows.Win32.UI.Shell.SHELL_LINK_DATA_FLAGS = 67108864
SLDF_PERSIST_VOLUME_ID_RELATIVE: win32more.Windows.Win32.UI.Shell.SHELL_LINK_DATA_FLAGS = 134217728
SLDF_VALID: win32more.Windows.Win32.UI.Shell.SHELL_LINK_DATA_FLAGS = 268433407
SLDF_RESERVED: win32more.Windows.Win32.UI.Shell.SHELL_LINK_DATA_FLAGS = -2147483648
SHELL_UI_COMPONENT = Int32
SHELL_UI_COMPONENT_TASKBARS: win32more.Windows.Win32.UI.Shell.SHELL_UI_COMPONENT = 0
SHELL_UI_COMPONENT_NOTIFICATIONAREA: win32more.Windows.Win32.UI.Shell.SHELL_UI_COMPONENT = 1
SHELL_UI_COMPONENT_DESKBAND: win32more.Windows.Win32.UI.Shell.SHELL_UI_COMPONENT = 2
if ARCH in 'X64,ARM64':
    class SHFILEINFOA(Structure):
        hIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON
        iIcon: Int32
        dwAttributes: UInt32
        szDisplayName: win32more.Windows.Win32.Foundation.CHAR * 260
        szTypeName: win32more.Windows.Win32.Foundation.CHAR * 80
elif ARCH in 'X86':
    class SHFILEINFOA(Structure):
        hIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON
        iIcon: Int32
        dwAttributes: UInt32
        szDisplayName: win32more.Windows.Win32.Foundation.CHAR * 260
        szTypeName: win32more.Windows.Win32.Foundation.CHAR * 80
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class SHFILEINFOW(Structure):
        hIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON
        iIcon: Int32
        dwAttributes: UInt32
        szDisplayName: Char * 260
        szTypeName: Char * 80
elif ARCH in 'X86':
    class SHFILEINFOW(Structure):
        hIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON
        iIcon: Int32
        dwAttributes: UInt32
        szDisplayName: Char * 260
        szTypeName: Char * 80
        _pack_ = 1
if ARCH in 'X64,ARM64':
    SHFILEINFO = UnicodeAlias('SHFILEINFOW')
elif ARCH in 'X86':
    SHFILEINFO = UnicodeAlias('SHFILEINFOW')
if ARCH in 'X64,ARM64':
    class SHFILEOPSTRUCTA(Structure):
        hwnd: win32more.Windows.Win32.Foundation.HWND
        wFunc: UInt32
        pFrom: POINTER(SByte)
        pTo: POINTER(SByte)
        fFlags: UInt16
        fAnyOperationsAborted: win32more.Windows.Win32.Foundation.BOOL
        hNameMappings: VoidPtr
        lpszProgressTitle: win32more.Windows.Win32.Foundation.PSTR
elif ARCH in 'X86':
    class SHFILEOPSTRUCTA(Structure):
        hwnd: win32more.Windows.Win32.Foundation.HWND
        wFunc: UInt32
        pFrom: POINTER(SByte)
        pTo: POINTER(SByte)
        fFlags: UInt16
        fAnyOperationsAborted: win32more.Windows.Win32.Foundation.BOOL
        hNameMappings: VoidPtr
        lpszProgressTitle: win32more.Windows.Win32.Foundation.PSTR
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class SHFILEOPSTRUCTW(Structure):
        hwnd: win32more.Windows.Win32.Foundation.HWND
        wFunc: UInt32
        pFrom: win32more.Windows.Win32.Foundation.PWSTR
        pTo: win32more.Windows.Win32.Foundation.PWSTR
        fFlags: UInt16
        fAnyOperationsAborted: win32more.Windows.Win32.Foundation.BOOL
        hNameMappings: VoidPtr
        lpszProgressTitle: win32more.Windows.Win32.Foundation.PWSTR
elif ARCH in 'X86':
    class SHFILEOPSTRUCTW(Structure):
        hwnd: win32more.Windows.Win32.Foundation.HWND
        wFunc: UInt32
        pFrom: win32more.Windows.Win32.Foundation.PWSTR
        pTo: win32more.Windows.Win32.Foundation.PWSTR
        fFlags: UInt16
        fAnyOperationsAborted: win32more.Windows.Win32.Foundation.BOOL
        hNameMappings: VoidPtr
        lpszProgressTitle: win32more.Windows.Win32.Foundation.PWSTR
        _pack_ = 1
if ARCH in 'X64,ARM64':
    SHFILEOPSTRUCT = UnicodeAlias('SHFILEOPSTRUCTW')
elif ARCH in 'X86':
    SHFILEOPSTRUCT = UnicodeAlias('SHFILEOPSTRUCTW')
SHFMT_ID = UInt32
SHFMT_ID_DEFAULT: win32more.Windows.Win32.UI.Shell.SHFMT_ID = 65535
SHFMT_OPT = Int32
SHFMT_OPT_NONE: win32more.Windows.Win32.UI.Shell.SHFMT_OPT = 0
SHFMT_OPT_FULL: win32more.Windows.Win32.UI.Shell.SHFMT_OPT = 1
SHFMT_OPT_SYSONLY: win32more.Windows.Win32.UI.Shell.SHFMT_OPT = 2
SHFMT_RET = UInt32
SHFMT_ERROR: win32more.Windows.Win32.UI.Shell.SHFMT_RET = 4294967295
SHFMT_CANCEL: win32more.Windows.Win32.UI.Shell.SHFMT_RET = 4294967294
SHFMT_NOFORMAT: win32more.Windows.Win32.UI.Shell.SHFMT_RET = 4294967293
class SHFOLDERCUSTOMSETTINGS(Structure):
    dwSize: UInt32
    dwMask: UInt32
    pvid: POINTER(Guid)
    pszWebViewTemplate: win32more.Windows.Win32.Foundation.PWSTR
    cchWebViewTemplate: UInt32
    pszWebViewTemplateVersion: win32more.Windows.Win32.Foundation.PWSTR
    pszInfoTip: win32more.Windows.Win32.Foundation.PWSTR
    cchInfoTip: UInt32
    pclsid: POINTER(Guid)
    dwFlags: UInt32
    pszIconFile: win32more.Windows.Win32.Foundation.PWSTR
    cchIconFile: UInt32
    iIconIndex: Int32
    pszLogo: win32more.Windows.Win32.Foundation.PWSTR
    cchLogo: UInt32
SHGDFIL_FORMAT = Int32
SHGDFIL_FINDDATA: win32more.Windows.Win32.UI.Shell.SHGDFIL_FORMAT = 1
SHGDFIL_NETRESOURCE: win32more.Windows.Win32.UI.Shell.SHGDFIL_FORMAT = 2
SHGDFIL_DESCRIPTIONID: win32more.Windows.Win32.UI.Shell.SHGDFIL_FORMAT = 3
SHGDNF = UInt32
SHGDN_NORMAL: win32more.Windows.Win32.UI.Shell.SHGDNF = 0
SHGDN_INFOLDER: win32more.Windows.Win32.UI.Shell.SHGDNF = 1
SHGDN_FOREDITING: win32more.Windows.Win32.UI.Shell.SHGDNF = 4096
SHGDN_FORADDRESSBAR: win32more.Windows.Win32.UI.Shell.SHGDNF = 16384
SHGDN_FORPARSING: win32more.Windows.Win32.UI.Shell.SHGDNF = 32768
SHGFI_FLAGS = UInt32
SHGFI_ADDOVERLAYS: win32more.Windows.Win32.UI.Shell.SHGFI_FLAGS = 32
SHGFI_ATTR_SPECIFIED: win32more.Windows.Win32.UI.Shell.SHGFI_FLAGS = 131072
SHGFI_ATTRIBUTES: win32more.Windows.Win32.UI.Shell.SHGFI_FLAGS = 2048
SHGFI_DISPLAYNAME: win32more.Windows.Win32.UI.Shell.SHGFI_FLAGS = 512
SHGFI_EXETYPE: win32more.Windows.Win32.UI.Shell.SHGFI_FLAGS = 8192
SHGFI_ICON: win32more.Windows.Win32.UI.Shell.SHGFI_FLAGS = 256
SHGFI_ICONLOCATION: win32more.Windows.Win32.UI.Shell.SHGFI_FLAGS = 4096
SHGFI_LARGEICON: win32more.Windows.Win32.UI.Shell.SHGFI_FLAGS = 0
SHGFI_LINKOVERLAY: win32more.Windows.Win32.UI.Shell.SHGFI_FLAGS = 32768
SHGFI_OPENICON: win32more.Windows.Win32.UI.Shell.SHGFI_FLAGS = 2
SHGFI_OVERLAYINDEX: win32more.Windows.Win32.UI.Shell.SHGFI_FLAGS = 64
SHGFI_PIDL: win32more.Windows.Win32.UI.Shell.SHGFI_FLAGS = 8
SHGFI_SELECTED: win32more.Windows.Win32.UI.Shell.SHGFI_FLAGS = 65536
SHGFI_SHELLICONSIZE: win32more.Windows.Win32.UI.Shell.SHGFI_FLAGS = 4
SHGFI_SMALLICON: win32more.Windows.Win32.UI.Shell.SHGFI_FLAGS = 1
SHGFI_SYSICONINDEX: win32more.Windows.Win32.UI.Shell.SHGFI_FLAGS = 16384
SHGFI_TYPENAME: win32more.Windows.Win32.UI.Shell.SHGFI_FLAGS = 1024
SHGFI_USEFILEATTRIBUTES: win32more.Windows.Win32.UI.Shell.SHGFI_FLAGS = 16
SHGFP_TYPE = Int32
SHGFP_TYPE_CURRENT: win32more.Windows.Win32.UI.Shell.SHGFP_TYPE = 0
SHGFP_TYPE_DEFAULT: win32more.Windows.Win32.UI.Shell.SHGFP_TYPE = 1
SHGLOBALCOUNTER = Int32
GLOBALCOUNTER_SEARCHMANAGER: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 0
GLOBALCOUNTER_SEARCHOPTIONS: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 1
GLOBALCOUNTER_FOLDERSETTINGSCHANGE: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 2
GLOBALCOUNTER_RATINGS: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 3
GLOBALCOUNTER_APPROVEDSITES: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 4
GLOBALCOUNTER_RESTRICTIONS: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 5
GLOBALCOUNTER_SHELLSETTINGSCHANGED: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 6
GLOBALCOUNTER_SYSTEMPIDLCHANGE: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 7
GLOBALCOUNTER_OVERLAYMANAGER: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 8
GLOBALCOUNTER_QUERYASSOCIATIONS: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 9
GLOBALCOUNTER_IESESSIONS: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 10
GLOBALCOUNTER_IEONLY_SESSIONS: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 11
GLOBALCOUNTER_APPLICATION_DESTINATIONS: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 12
__UNUSED_RECYCLE_WAS_GLOBALCOUNTER_CSCSYNCINPROGRESS: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 13
GLOBALCOUNTER_BITBUCKETNUMDELETERS: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 14
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_SHARES: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 15
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_A: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 16
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_B: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 17
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_C: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 18
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_D: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 19
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_E: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 20
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_F: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 21
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_G: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 22
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_H: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 23
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_I: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 24
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_J: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 25
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_K: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 26
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_L: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 27
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_M: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 28
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_N: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 29
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_O: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 30
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_P: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 31
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_Q: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 32
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_R: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 33
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_S: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 34
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_T: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 35
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_U: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 36
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_V: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 37
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_W: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 38
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_X: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 39
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_Y: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 40
GLOBALCOUNTER_RECYCLEDIRTYCOUNT_DRIVE_Z: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 41
__UNUSED_RECYCLE_WAS_GLOBALCOUNTER_RECYCLEDIRTYCOUNT_SERVERDRIVE: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 42
__UNUSED_RECYCLE_WAS_GLOBALCOUNTER_RECYCLEGLOBALDIRTYCOUNT: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 43
GLOBALCOUNTER_RECYCLEBINENUM: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 44
GLOBALCOUNTER_RECYCLEBINCORRUPTED: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 45
GLOBALCOUNTER_RATINGS_STATECOUNTER: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 46
GLOBALCOUNTER_PRIVATE_PROFILE_CACHE: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 47
GLOBALCOUNTER_INTERNETTOOLBAR_LAYOUT: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 48
GLOBALCOUNTER_FOLDERDEFINITION_CACHE: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 49
GLOBALCOUNTER_COMMONPLACES_LIST_CACHE: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 50
GLOBALCOUNTER_PRIVATE_PROFILE_CACHE_MACHINEWIDE: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 51
GLOBALCOUNTER_ASSOCCHANGED: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 52
GLOBALCOUNTER_APP_ITEMS_STATE_STORE_CACHE: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 53
GLOBALCOUNTER_SETTINGSYNC_ENABLED: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 54
GLOBALCOUNTER_APPSFOLDER_FILETYPEASSOCIATION_COUNTER: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 55
GLOBALCOUNTER_USERINFOCHANGED: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 56
GLOBALCOUNTER_SYNC_ENGINE_INFORMATION_CACHE_MACHINEWIDE: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 57
GLOBALCOUNTER_BANNERS_DATAMODEL_CACHE_MACHINEWIDE: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 58
GLOBALCOUNTER_MAXIMUMVALUE: win32more.Windows.Win32.UI.Shell.SHGLOBALCOUNTER = 59
SHGSI_FLAGS = UInt32
SHGSI_ICONLOCATION: win32more.Windows.Win32.UI.Shell.SHGSI_FLAGS = 0
SHGSI_ICON: win32more.Windows.Win32.UI.Shell.SHGSI_FLAGS = 256
SHGSI_SYSICONINDEX: win32more.Windows.Win32.UI.Shell.SHGSI_FLAGS = 16384
SHGSI_LINKOVERLAY: win32more.Windows.Win32.UI.Shell.SHGSI_FLAGS = 32768
SHGSI_SELECTED: win32more.Windows.Win32.UI.Shell.SHGSI_FLAGS = 65536
SHGSI_LARGEICON: win32more.Windows.Win32.UI.Shell.SHGSI_FLAGS = 0
SHGSI_SMALLICON: win32more.Windows.Win32.UI.Shell.SHGSI_FLAGS = 1
SHGSI_SHELLICONSIZE: win32more.Windows.Win32.UI.Shell.SHGSI_FLAGS = 4
if ARCH in 'X64,ARM64':
    class SHNAMEMAPPINGA(Structure):
        pszOldPath: win32more.Windows.Win32.Foundation.PSTR
        pszNewPath: win32more.Windows.Win32.Foundation.PSTR
        cchOldPath: Int32
        cchNewPath: Int32
elif ARCH in 'X86':
    class SHNAMEMAPPINGA(Structure):
        pszOldPath: win32more.Windows.Win32.Foundation.PSTR
        pszNewPath: win32more.Windows.Win32.Foundation.PSTR
        cchOldPath: Int32
        cchNewPath: Int32
        _pack_ = 1
if ARCH in 'X64,ARM64':
    class SHNAMEMAPPINGW(Structure):
        pszOldPath: win32more.Windows.Win32.Foundation.PWSTR
        pszNewPath: win32more.Windows.Win32.Foundation.PWSTR
        cchOldPath: Int32
        cchNewPath: Int32
elif ARCH in 'X86':
    class SHNAMEMAPPINGW(Structure):
        pszOldPath: win32more.Windows.Win32.Foundation.PWSTR
        pszNewPath: win32more.Windows.Win32.Foundation.PWSTR
        cchOldPath: Int32
        cchNewPath: Int32
        _pack_ = 1
if ARCH in 'X64,ARM64':
    SHNAMEMAPPING = UnicodeAlias('SHNAMEMAPPINGW')
elif ARCH in 'X86':
    SHNAMEMAPPING = UnicodeAlias('SHNAMEMAPPINGW')
SHOP_TYPE = Int32
SHOP_PRINTERNAME: win32more.Windows.Win32.UI.Shell.SHOP_TYPE = 1
SHOP_FILEPATH: win32more.Windows.Win32.UI.Shell.SHOP_TYPE = 2
SHOP_VOLUMEGUID: win32more.Windows.Win32.UI.Shell.SHOP_TYPE = 4
if ARCH in 'X64,ARM64':
    class SHQUERYRBINFO(Structure):
        cbSize: UInt32
        i64Size: Int64
        i64NumItems: Int64
elif ARCH in 'X86':
    class SHQUERYRBINFO(Structure):
        cbSize: UInt32
        i64Size: Int64
        i64NumItems: Int64
        _pack_ = 1
SHREGDEL_FLAGS = Int32
SHREGDEL_DEFAULT: win32more.Windows.Win32.UI.Shell.SHREGDEL_FLAGS = 0
SHREGDEL_HKCU: win32more.Windows.Win32.UI.Shell.SHREGDEL_FLAGS = 1
SHREGDEL_HKLM: win32more.Windows.Win32.UI.Shell.SHREGDEL_FLAGS = 16
SHREGDEL_BOTH: win32more.Windows.Win32.UI.Shell.SHREGDEL_FLAGS = 17
SHREGENUM_FLAGS = Int32
SHREGENUM_DEFAULT: win32more.Windows.Win32.UI.Shell.SHREGENUM_FLAGS = 0
SHREGENUM_HKCU: win32more.Windows.Win32.UI.Shell.SHREGENUM_FLAGS = 1
SHREGENUM_HKLM: win32more.Windows.Win32.UI.Shell.SHREGENUM_FLAGS = 16
SHREGENUM_BOTH: win32more.Windows.Win32.UI.Shell.SHREGENUM_FLAGS = 17
SHSTOCKICONID = Int32
SIID_DOCNOASSOC: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 0
SIID_DOCASSOC: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 1
SIID_APPLICATION: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 2
SIID_FOLDER: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 3
SIID_FOLDEROPEN: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 4
SIID_DRIVE525: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 5
SIID_DRIVE35: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 6
SIID_DRIVEREMOVE: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 7
SIID_DRIVEFIXED: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 8
SIID_DRIVENET: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 9
SIID_DRIVENETDISABLED: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 10
SIID_DRIVECD: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 11
SIID_DRIVERAM: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 12
SIID_WORLD: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 13
SIID_SERVER: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 15
SIID_PRINTER: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 16
SIID_MYNETWORK: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 17
SIID_FIND: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 22
SIID_HELP: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 23
SIID_SHARE: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 28
SIID_LINK: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 29
SIID_SLOWFILE: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 30
SIID_RECYCLER: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 31
SIID_RECYCLERFULL: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 32
SIID_MEDIACDAUDIO: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 40
SIID_LOCK: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 47
SIID_AUTOLIST: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 49
SIID_PRINTERNET: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 50
SIID_SERVERSHARE: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 51
SIID_PRINTERFAX: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 52
SIID_PRINTERFAXNET: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 53
SIID_PRINTERFILE: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 54
SIID_STACK: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 55
SIID_MEDIASVCD: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 56
SIID_STUFFEDFOLDER: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 57
SIID_DRIVEUNKNOWN: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 58
SIID_DRIVEDVD: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 59
SIID_MEDIADVD: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 60
SIID_MEDIADVDRAM: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 61
SIID_MEDIADVDRW: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 62
SIID_MEDIADVDR: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 63
SIID_MEDIADVDROM: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 64
SIID_MEDIACDAUDIOPLUS: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 65
SIID_MEDIACDRW: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 66
SIID_MEDIACDR: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 67
SIID_MEDIACDBURN: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 68
SIID_MEDIABLANKCD: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 69
SIID_MEDIACDROM: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 70
SIID_AUDIOFILES: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 71
SIID_IMAGEFILES: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 72
SIID_VIDEOFILES: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 73
SIID_MIXEDFILES: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 74
SIID_FOLDERBACK: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 75
SIID_FOLDERFRONT: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 76
SIID_SHIELD: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 77
SIID_WARNING: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 78
SIID_INFO: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 79
SIID_ERROR: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 80
SIID_KEY: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 81
SIID_SOFTWARE: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 82
SIID_RENAME: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 83
SIID_DELETE: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 84
SIID_MEDIAAUDIODVD: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 85
SIID_MEDIAMOVIEDVD: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 86
SIID_MEDIAENHANCEDCD: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 87
SIID_MEDIAENHANCEDDVD: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 88
SIID_MEDIAHDDVD: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 89
SIID_MEDIABLURAY: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 90
SIID_MEDIAVCD: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 91
SIID_MEDIADVDPLUSR: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 92
SIID_MEDIADVDPLUSRW: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 93
SIID_DESKTOPPC: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 94
SIID_MOBILEPC: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 95
SIID_USERS: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 96
SIID_MEDIASMARTMEDIA: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 97
SIID_MEDIACOMPACTFLASH: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 98
SIID_DEVICECELLPHONE: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 99
SIID_DEVICECAMERA: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 100
SIID_DEVICEVIDEOCAMERA: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 101
SIID_DEVICEAUDIOPLAYER: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 102
SIID_NETWORKCONNECT: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 103
SIID_INTERNET: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 104
SIID_ZIPFILE: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 105
SIID_SETTINGS: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 106
SIID_DRIVEHDDVD: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 132
SIID_DRIVEBD: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 133
SIID_MEDIAHDDVDROM: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 134
SIID_MEDIAHDDVDR: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 135
SIID_MEDIAHDDVDRAM: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 136
SIID_MEDIABDROM: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 137
SIID_MEDIABDR: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 138
SIID_MEDIABDRE: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 139
SIID_CLUSTEREDDRIVE: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 140
SIID_MAX_ICONS: win32more.Windows.Win32.UI.Shell.SHSTOCKICONID = 181
if ARCH in 'X64,ARM64':
    class SHSTOCKICONINFO(Structure):
        cbSize: UInt32
        hIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON
        iSysImageIndex: Int32
        iIcon: Int32
        szPath: Char * 260
elif ARCH in 'X86':
    class SHSTOCKICONINFO(Structure):
        cbSize: UInt32
        hIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON
        iSysImageIndex: Int32
        iIcon: Int32
        szPath: Char * 260
        _pack_ = 1
SIATTRIBFLAGS = Int32
SIATTRIBFLAGS_AND: win32more.Windows.Win32.UI.Shell.SIATTRIBFLAGS = 1
SIATTRIBFLAGS_OR: win32more.Windows.Win32.UI.Shell.SIATTRIBFLAGS = 2
SIATTRIBFLAGS_APPCOMPAT: win32more.Windows.Win32.UI.Shell.SIATTRIBFLAGS = 3
SIATTRIBFLAGS_MASK: win32more.Windows.Win32.UI.Shell.SIATTRIBFLAGS = 3
SIATTRIBFLAGS_ALLITEMS: win32more.Windows.Win32.UI.Shell.SIATTRIBFLAGS = 16384
SIGDN = Int32
SIGDN_NORMALDISPLAY: win32more.Windows.Win32.UI.Shell.SIGDN = 0
SIGDN_PARENTRELATIVEPARSING: win32more.Windows.Win32.UI.Shell.SIGDN = -2147385343
SIGDN_DESKTOPABSOLUTEPARSING: win32more.Windows.Win32.UI.Shell.SIGDN = -2147319808
SIGDN_PARENTRELATIVEEDITING: win32more.Windows.Win32.UI.Shell.SIGDN = -2147282943
SIGDN_DESKTOPABSOLUTEEDITING: win32more.Windows.Win32.UI.Shell.SIGDN = -2147172352
SIGDN_FILESYSPATH: win32more.Windows.Win32.UI.Shell.SIGDN = -2147123200
SIGDN_URL: win32more.Windows.Win32.UI.Shell.SIGDN = -2147057664
SIGDN_PARENTRELATIVEFORADDRESSBAR: win32more.Windows.Win32.UI.Shell.SIGDN = -2146975743
SIGDN_PARENTRELATIVE: win32more.Windows.Win32.UI.Shell.SIGDN = -2146959359
SIGDN_PARENTRELATIVEFORUI: win32more.Windows.Win32.UI.Shell.SIGDN = -2146877439
SIIGBF = Int32
SIIGBF_RESIZETOFIT: win32more.Windows.Win32.UI.Shell.SIIGBF = 0
SIIGBF_BIGGERSIZEOK: win32more.Windows.Win32.UI.Shell.SIIGBF = 1
SIIGBF_MEMORYONLY: win32more.Windows.Win32.UI.Shell.SIIGBF = 2
SIIGBF_ICONONLY: win32more.Windows.Win32.UI.Shell.SIIGBF = 4
SIIGBF_THUMBNAILONLY: win32more.Windows.Win32.UI.Shell.SIIGBF = 8
SIIGBF_INCACHEONLY: win32more.Windows.Win32.UI.Shell.SIIGBF = 16
SIIGBF_CROPTOSQUARE: win32more.Windows.Win32.UI.Shell.SIIGBF = 32
SIIGBF_WIDETHUMBNAILS: win32more.Windows.Win32.UI.Shell.SIIGBF = 64
SIIGBF_ICONBACKGROUND: win32more.Windows.Win32.UI.Shell.SIIGBF = 128
SIIGBF_SCALEUP: win32more.Windows.Win32.UI.Shell.SIIGBF = 256
SLGP_FLAGS = Int32
SLGP_SHORTPATH: win32more.Windows.Win32.UI.Shell.SLGP_FLAGS = 1
SLGP_UNCPRIORITY: win32more.Windows.Win32.UI.Shell.SLGP_FLAGS = 2
SLGP_RAWPATH: win32more.Windows.Win32.UI.Shell.SLGP_FLAGS = 4
SLGP_RELATIVEPRIORITY: win32more.Windows.Win32.UI.Shell.SLGP_FLAGS = 8
class SLOWAPPINFO(Structure):
    ullSize: UInt64
    ftLastUsed: win32more.Windows.Win32.Foundation.FILETIME
    iTimesUsed: Int32
    pszImage: win32more.Windows.Win32.Foundation.PWSTR
SLR_FLAGS = Int32
SLR_NONE: win32more.Windows.Win32.UI.Shell.SLR_FLAGS = 0
SLR_NO_UI: win32more.Windows.Win32.UI.Shell.SLR_FLAGS = 1
SLR_ANY_MATCH: win32more.Windows.Win32.UI.Shell.SLR_FLAGS = 2
SLR_UPDATE: win32more.Windows.Win32.UI.Shell.SLR_FLAGS = 4
SLR_NOUPDATE: win32more.Windows.Win32.UI.Shell.SLR_FLAGS = 8
SLR_NOSEARCH: win32more.Windows.Win32.UI.Shell.SLR_FLAGS = 16
SLR_NOTRACK: win32more.Windows.Win32.UI.Shell.SLR_FLAGS = 32
SLR_NOLINKINFO: win32more.Windows.Win32.UI.Shell.SLR_FLAGS = 64
SLR_INVOKE_MSI: win32more.Windows.Win32.UI.Shell.SLR_FLAGS = 128
SLR_NO_UI_WITH_MSG_PUMP: win32more.Windows.Win32.UI.Shell.SLR_FLAGS = 257
SLR_OFFER_DELETE_WITHOUT_FILE: win32more.Windows.Win32.UI.Shell.SLR_FLAGS = 512
SLR_KNOWNFOLDER: win32more.Windows.Win32.UI.Shell.SLR_FLAGS = 1024
SLR_MACHINE_IN_LOCAL_TARGET: win32more.Windows.Win32.UI.Shell.SLR_FLAGS = 2048
SLR_UPDATE_MACHINE_AND_SID: win32more.Windows.Win32.UI.Shell.SLR_FLAGS = 4096
SLR_NO_OBJECT_ID: win32more.Windows.Win32.UI.Shell.SLR_FLAGS = 8192
class SMCSHCHANGENOTIFYSTRUCT(Structure):
    lEvent: Int32
    pidl1: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)
    pidl2: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)
class SMDATA(Structure):
    dwMask: UInt32
    dwFlags: UInt32
    hmenu: win32more.Windows.Win32.UI.WindowsAndMessaging.HMENU
    hwnd: win32more.Windows.Win32.Foundation.HWND
    uId: UInt32
    uIdParent: UInt32
    uIdAncestor: UInt32
    punk: win32more.Windows.Win32.System.Com.IUnknown
    pidlFolder: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)
    pidlItem: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)
    psf: win32more.Windows.Win32.UI.Shell.IShellFolder
    pvUserData: VoidPtr
class SMINFO(Structure):
    dwMask: UInt32
    dwType: UInt32
    dwFlags: UInt32
    iIcon: Int32
SMINFOFLAGS = Int32
SMIF_ICON: win32more.Windows.Win32.UI.Shell.SMINFOFLAGS = 1
SMIF_ACCELERATOR: win32more.Windows.Win32.UI.Shell.SMINFOFLAGS = 2
SMIF_DROPTARGET: win32more.Windows.Win32.UI.Shell.SMINFOFLAGS = 4
SMIF_SUBMENU: win32more.Windows.Win32.UI.Shell.SMINFOFLAGS = 8
SMIF_CHECKED: win32more.Windows.Win32.UI.Shell.SMINFOFLAGS = 32
SMIF_DROPCASCADE: win32more.Windows.Win32.UI.Shell.SMINFOFLAGS = 64
SMIF_HIDDEN: win32more.Windows.Win32.UI.Shell.SMINFOFLAGS = 128
SMIF_DISABLED: win32more.Windows.Win32.UI.Shell.SMINFOFLAGS = 256
SMIF_TRACKPOPUP: win32more.Windows.Win32.UI.Shell.SMINFOFLAGS = 512
SMIF_DEMOTED: win32more.Windows.Win32.UI.Shell.SMINFOFLAGS = 1024
SMIF_ALTSTATE: win32more.Windows.Win32.UI.Shell.SMINFOFLAGS = 2048
SMIF_DRAGNDROP: win32more.Windows.Win32.UI.Shell.SMINFOFLAGS = 4096
SMIF_NEW: win32more.Windows.Win32.UI.Shell.SMINFOFLAGS = 8192
SMINFOMASK = Int32
SMIM_TYPE: win32more.Windows.Win32.UI.Shell.SMINFOMASK = 1
SMIM_FLAGS: win32more.Windows.Win32.UI.Shell.SMINFOMASK = 2
SMIM_ICON: win32more.Windows.Win32.UI.Shell.SMINFOMASK = 4
SMINFOTYPE = Int32
SMIT_SEPARATOR: win32more.Windows.Win32.UI.Shell.SMINFOTYPE = 1
SMIT_STRING: win32more.Windows.Win32.UI.Shell.SMINFOTYPE = 2
class SORTCOLUMN(Structure):
    propkey: win32more.Windows.Win32.Foundation.PROPERTYKEY
    direction: win32more.Windows.Win32.UI.Shell.SORTDIRECTION
SORTDIRECTION = Int32
SORT_DESCENDING: win32more.Windows.Win32.UI.Shell.SORTDIRECTION = -1
SORT_ASCENDING: win32more.Windows.Win32.UI.Shell.SORTDIRECTION = 1
SORT_ORDER_TYPE = Int32
SOT_DEFAULT: win32more.Windows.Win32.UI.Shell.SORT_ORDER_TYPE = 0
SOT_IGNORE_FOLDERNESS: win32more.Windows.Win32.UI.Shell.SORT_ORDER_TYPE = 1
SPACTION = Int32
SPACTION_NONE: win32more.Windows.Win32.UI.Shell.SPACTION = 0
SPACTION_MOVING: win32more.Windows.Win32.UI.Shell.SPACTION = 1
SPACTION_COPYING: win32more.Windows.Win32.UI.Shell.SPACTION = 2
SPACTION_RECYCLING: win32more.Windows.Win32.UI.Shell.SPACTION = 3
SPACTION_APPLYINGATTRIBS: win32more.Windows.Win32.UI.Shell.SPACTION = 4
SPACTION_DOWNLOADING: win32more.Windows.Win32.UI.Shell.SPACTION = 5
SPACTION_SEARCHING_INTERNET: win32more.Windows.Win32.UI.Shell.SPACTION = 6
SPACTION_CALCULATING: win32more.Windows.Win32.UI.Shell.SPACTION = 7
SPACTION_UPLOADING: win32more.Windows.Win32.UI.Shell.SPACTION = 8
SPACTION_SEARCHING_FILES: win32more.Windows.Win32.UI.Shell.SPACTION = 9
SPACTION_DELETING: win32more.Windows.Win32.UI.Shell.SPACTION = 10
SPACTION_RENAMING: win32more.Windows.Win32.UI.Shell.SPACTION = 11
SPACTION_FORMATTING: win32more.Windows.Win32.UI.Shell.SPACTION = 12
SPACTION_COPY_MOVING: win32more.Windows.Win32.UI.Shell.SPACTION = 13
SPTEXT = Int32
SPTEXT_ACTIONDESCRIPTION: win32more.Windows.Win32.UI.Shell.SPTEXT = 1
SPTEXT_ACTIONDETAIL: win32more.Windows.Win32.UI.Shell.SPTEXT = 2
SSF_MASK = UInt32
SSF_SHOWALLOBJECTS: win32more.Windows.Win32.UI.Shell.SSF_MASK = 1
SSF_SHOWEXTENSIONS: win32more.Windows.Win32.UI.Shell.SSF_MASK = 2
SSF_HIDDENFILEEXTS: win32more.Windows.Win32.UI.Shell.SSF_MASK = 4
SSF_SERVERADMINUI: win32more.Windows.Win32.UI.Shell.SSF_MASK = 4
SSF_SHOWCOMPCOLOR: win32more.Windows.Win32.UI.Shell.SSF_MASK = 8
SSF_SORTCOLUMNS: win32more.Windows.Win32.UI.Shell.SSF_MASK = 16
SSF_SHOWSYSFILES: win32more.Windows.Win32.UI.Shell.SSF_MASK = 32
SSF_DOUBLECLICKINWEBVIEW: win32more.Windows.Win32.UI.Shell.SSF_MASK = 128
SSF_SHOWATTRIBCOL: win32more.Windows.Win32.UI.Shell.SSF_MASK = 256
SSF_DESKTOPHTML: win32more.Windows.Win32.UI.Shell.SSF_MASK = 512
SSF_WIN95CLASSIC: win32more.Windows.Win32.UI.Shell.SSF_MASK = 1024
SSF_DONTPRETTYPATH: win32more.Windows.Win32.UI.Shell.SSF_MASK = 2048
SSF_SHOWINFOTIP: win32more.Windows.Win32.UI.Shell.SSF_MASK = 8192
SSF_MAPNETDRVBUTTON: win32more.Windows.Win32.UI.Shell.SSF_MASK = 4096
SSF_NOCONFIRMRECYCLE: win32more.Windows.Win32.UI.Shell.SSF_MASK = 32768
SSF_HIDEICONS: win32more.Windows.Win32.UI.Shell.SSF_MASK = 16384
SSF_FILTER: win32more.Windows.Win32.UI.Shell.SSF_MASK = 65536
SSF_WEBVIEW: win32more.Windows.Win32.UI.Shell.SSF_MASK = 131072
SSF_SHOWSUPERHIDDEN: win32more.Windows.Win32.UI.Shell.SSF_MASK = 262144
SSF_SEPPROCESS: win32more.Windows.Win32.UI.Shell.SSF_MASK = 524288
SSF_NONETCRAWLING: win32more.Windows.Win32.UI.Shell.SSF_MASK = 1048576
SSF_STARTPANELON: win32more.Windows.Win32.UI.Shell.SSF_MASK = 2097152
SSF_SHOWSTARTPAGE: win32more.Windows.Win32.UI.Shell.SSF_MASK = 4194304
SSF_AUTOCHECKSELECT: win32more.Windows.Win32.UI.Shell.SSF_MASK = 8388608
SSF_ICONSONLY: win32more.Windows.Win32.UI.Shell.SSF_MASK = 16777216
SSF_SHOWTYPEOVERLAY: win32more.Windows.Win32.UI.Shell.SSF_MASK = 33554432
SSF_SHOWSTATUSBAR: win32more.Windows.Win32.UI.Shell.SSF_MASK = 67108864
STGOP = Int32
STGOP_MOVE: win32more.Windows.Win32.UI.Shell.STGOP = 1
STGOP_COPY: win32more.Windows.Win32.UI.Shell.STGOP = 2
STGOP_SYNC: win32more.Windows.Win32.UI.Shell.STGOP = 3
STGOP_REMOVE: win32more.Windows.Win32.UI.Shell.STGOP = 5
STGOP_RENAME: win32more.Windows.Win32.UI.Shell.STGOP = 6
STGOP_APPLYPROPERTIES: win32more.Windows.Win32.UI.Shell.STGOP = 8
STGOP_NEW: win32more.Windows.Win32.UI.Shell.STGOP = 10
STORAGE_PROVIDER_FILE_FLAGS = Int32
SPFF_NONE: win32more.Windows.Win32.UI.Shell.STORAGE_PROVIDER_FILE_FLAGS = 0
SPFF_DOWNLOAD_BY_DEFAULT: win32more.Windows.Win32.UI.Shell.STORAGE_PROVIDER_FILE_FLAGS = 1
SPFF_CREATED_ON_THIS_DEVICE: win32more.Windows.Win32.UI.Shell.STORAGE_PROVIDER_FILE_FLAGS = 2
STPFLAG = Int32
STPF_NONE: win32more.Windows.Win32.UI.Shell.STPFLAG = 0
STPF_USEAPPTHUMBNAILALWAYS: win32more.Windows.Win32.UI.Shell.STPFLAG = 1
STPF_USEAPPTHUMBNAILWHENACTIVE: win32more.Windows.Win32.UI.Shell.STPFLAG = 2
STPF_USEAPPPEEKALWAYS: win32more.Windows.Win32.UI.Shell.STPFLAG = 4
STPF_USEAPPPEEKWHENACTIVE: win32more.Windows.Win32.UI.Shell.STPFLAG = 8
@winfunctype_pointer
def SUBCLASSPROC(hWnd: win32more.Windows.Win32.Foundation.HWND, uMsg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM, uIdSubclass: UIntPtr, dwRefData: UIntPtr) -> win32more.Windows.Win32.Foundation.LRESULT: ...
class SV2CVW2_PARAMS(Structure):
    cbSize: UInt32
    psvPrev: win32more.Windows.Win32.UI.Shell.IShellView
    pfs: POINTER(win32more.Windows.Win32.UI.Shell.FOLDERSETTINGS)
    psbOwner: win32more.Windows.Win32.UI.Shell.IShellBrowser
    prcView: POINTER(win32more.Windows.Win32.Foundation.RECT)
    pvid: POINTER(Guid)
    hwndView: win32more.Windows.Win32.Foundation.HWND
SVUIA_STATUS = Int32
SVUIA_DEACTIVATE: win32more.Windows.Win32.UI.Shell.SVUIA_STATUS = 0
SVUIA_ACTIVATE_NOFOCUS: win32more.Windows.Win32.UI.Shell.SVUIA_STATUS = 1
SVUIA_ACTIVATE_FOCUS: win32more.Windows.Win32.UI.Shell.SVUIA_STATUS = 2
SVUIA_INPLACEACTIVATE: win32more.Windows.Win32.UI.Shell.SVUIA_STATUS = 3
SYNCMGRERRORFLAGS = Int32
SYNCMGRERRORFLAG_ENABLEJUMPTEXT: win32more.Windows.Win32.UI.Shell.SYNCMGRERRORFLAGS = 1
SYNCMGRFLAG = Int32
SYNCMGRFLAG_CONNECT: win32more.Windows.Win32.UI.Shell.SYNCMGRFLAG = 1
SYNCMGRFLAG_PENDINGDISCONNECT: win32more.Windows.Win32.UI.Shell.SYNCMGRFLAG = 2
SYNCMGRFLAG_MANUAL: win32more.Windows.Win32.UI.Shell.SYNCMGRFLAG = 3
SYNCMGRFLAG_IDLE: win32more.Windows.Win32.UI.Shell.SYNCMGRFLAG = 4
SYNCMGRFLAG_INVOKE: win32more.Windows.Win32.UI.Shell.SYNCMGRFLAG = 5
SYNCMGRFLAG_SCHEDULED: win32more.Windows.Win32.UI.Shell.SYNCMGRFLAG = 6
SYNCMGRFLAG_EVENTMASK: win32more.Windows.Win32.UI.Shell.SYNCMGRFLAG = 255
SYNCMGRFLAG_SETTINGS: win32more.Windows.Win32.UI.Shell.SYNCMGRFLAG = 256
SYNCMGRFLAG_MAYBOTHERUSER: win32more.Windows.Win32.UI.Shell.SYNCMGRFLAG = 512
SYNCMGRHANDLERFLAGS = Int32
SYNCMGRHANDLER_HASPROPERTIES: win32more.Windows.Win32.UI.Shell.SYNCMGRHANDLERFLAGS = 1
SYNCMGRHANDLER_MAYESTABLISHCONNECTION: win32more.Windows.Win32.UI.Shell.SYNCMGRHANDLERFLAGS = 2
SYNCMGRHANDLER_ALWAYSLISTHANDLER: win32more.Windows.Win32.UI.Shell.SYNCMGRHANDLERFLAGS = 4
SYNCMGRHANDLER_HIDDEN: win32more.Windows.Win32.UI.Shell.SYNCMGRHANDLERFLAGS = 8
class SYNCMGRHANDLERINFO(Structure):
    cbSize: UInt32
    hIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON
    SyncMgrHandlerFlags: UInt32
    wszHandlerName: Char * 32
SYNCMGRINVOKEFLAGS = Int32
SYNCMGRINVOKE_STARTSYNC: win32more.Windows.Win32.UI.Shell.SYNCMGRINVOKEFLAGS = 2
SYNCMGRINVOKE_MINIMIZED: win32more.Windows.Win32.UI.Shell.SYNCMGRINVOKEFLAGS = 4
class SYNCMGRITEM(Structure):
    cbSize: UInt32
    dwFlags: UInt32
    ItemID: Guid
    dwItemState: UInt32
    hIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON
    wszItemName: Char * 128
    ftLastUpdate: win32more.Windows.Win32.Foundation.FILETIME
SYNCMGRITEMFLAGS = Int32
SYNCMGRITEM_HASPROPERTIES: win32more.Windows.Win32.UI.Shell.SYNCMGRITEMFLAGS = 1
SYNCMGRITEM_TEMPORARY: win32more.Windows.Win32.UI.Shell.SYNCMGRITEMFLAGS = 2
SYNCMGRITEM_ROAMINGUSER: win32more.Windows.Win32.UI.Shell.SYNCMGRITEMFLAGS = 4
SYNCMGRITEM_LASTUPDATETIME: win32more.Windows.Win32.UI.Shell.SYNCMGRITEMFLAGS = 8
SYNCMGRITEM_MAYDELETEITEM: win32more.Windows.Win32.UI.Shell.SYNCMGRITEMFLAGS = 16
SYNCMGRITEM_HIDDEN: win32more.Windows.Win32.UI.Shell.SYNCMGRITEMFLAGS = 32
SYNCMGRITEMSTATE = Int32
SYNCMGRITEMSTATE_UNCHECKED: win32more.Windows.Win32.UI.Shell.SYNCMGRITEMSTATE = 0
SYNCMGRITEMSTATE_CHECKED: win32more.Windows.Win32.UI.Shell.SYNCMGRITEMSTATE = 1
class SYNCMGRLOGERRORINFO(Structure):
    cbSize: UInt32
    mask: UInt32
    dwSyncMgrErrorFlags: UInt32
    ErrorID: Guid
    ItemID: Guid
SYNCMGRLOGLEVEL = Int32
SYNCMGRLOGLEVEL_INFORMATION: win32more.Windows.Win32.UI.Shell.SYNCMGRLOGLEVEL = 1
SYNCMGRLOGLEVEL_WARNING: win32more.Windows.Win32.UI.Shell.SYNCMGRLOGLEVEL = 2
SYNCMGRLOGLEVEL_ERROR: win32more.Windows.Win32.UI.Shell.SYNCMGRLOGLEVEL = 3
SYNCMGRLOGLEVEL_LOGLEVELMAX: win32more.Windows.Win32.UI.Shell.SYNCMGRLOGLEVEL = 3
class SYNCMGRPROGRESSITEM(Structure):
    cbSize: UInt32
    mask: UInt32
    lpcStatusText: win32more.Windows.Win32.Foundation.PWSTR
    dwStatusType: UInt32
    iProgValue: Int32
    iMaxValue: Int32
SYNCMGRREGISTERFLAGS = Int32
SYNCMGRREGISTERFLAG_CONNECT: win32more.Windows.Win32.UI.Shell.SYNCMGRREGISTERFLAGS = 1
SYNCMGRREGISTERFLAG_PENDINGDISCONNECT: win32more.Windows.Win32.UI.Shell.SYNCMGRREGISTERFLAGS = 2
SYNCMGRREGISTERFLAG_IDLE: win32more.Windows.Win32.UI.Shell.SYNCMGRREGISTERFLAGS = 4
SYNCMGRSTATUS = Int32
SYNCMGRSTATUS_STOPPED: win32more.Windows.Win32.UI.Shell.SYNCMGRSTATUS = 0
SYNCMGRSTATUS_SKIPPED: win32more.Windows.Win32.UI.Shell.SYNCMGRSTATUS = 1
SYNCMGRSTATUS_PENDING: win32more.Windows.Win32.UI.Shell.SYNCMGRSTATUS = 2
SYNCMGRSTATUS_UPDATING: win32more.Windows.Win32.UI.Shell.SYNCMGRSTATUS = 3
SYNCMGRSTATUS_SUCCEEDED: win32more.Windows.Win32.UI.Shell.SYNCMGRSTATUS = 4
SYNCMGRSTATUS_FAILED: win32more.Windows.Win32.UI.Shell.SYNCMGRSTATUS = 5
SYNCMGRSTATUS_PAUSED: win32more.Windows.Win32.UI.Shell.SYNCMGRSTATUS = 6
SYNCMGRSTATUS_RESUMING: win32more.Windows.Win32.UI.Shell.SYNCMGRSTATUS = 7
SYNCMGRSTATUS_UPDATING_INDETERMINATE: win32more.Windows.Win32.UI.Shell.SYNCMGRSTATUS = 8
SYNCMGRSTATUS_DELETED: win32more.Windows.Win32.UI.Shell.SYNCMGRSTATUS = 256
SYNCMGR_CANCEL_REQUEST = Int32
SYNCMGR_CR_NONE: win32more.Windows.Win32.UI.Shell.SYNCMGR_CANCEL_REQUEST = 0
SYNCMGR_CR_CANCEL_ITEM: win32more.Windows.Win32.UI.Shell.SYNCMGR_CANCEL_REQUEST = 1
SYNCMGR_CR_CANCEL_ALL: win32more.Windows.Win32.UI.Shell.SYNCMGR_CANCEL_REQUEST = 2
SYNCMGR_CR_MAX: win32more.Windows.Win32.UI.Shell.SYNCMGR_CANCEL_REQUEST = 2
class SYNCMGR_CONFLICT_ID_INFO(Structure):
    pblobID: POINTER(win32more.Windows.Win32.System.Com.BYTE_BLOB)
    pblobExtra: POINTER(win32more.Windows.Win32.System.Com.BYTE_BLOB)
SYNCMGR_CONFLICT_ITEM_TYPE = Int32
SYNCMGR_CIT_UPDATED: win32more.Windows.Win32.UI.Shell.SYNCMGR_CONFLICT_ITEM_TYPE = 1
SYNCMGR_CIT_DELETED: win32more.Windows.Win32.UI.Shell.SYNCMGR_CONFLICT_ITEM_TYPE = 2
SYNCMGR_CONTROL_FLAGS = Int32
SYNCMGR_CF_NONE: win32more.Windows.Win32.UI.Shell.SYNCMGR_CONTROL_FLAGS = 0
SYNCMGR_CF_NOWAIT: win32more.Windows.Win32.UI.Shell.SYNCMGR_CONTROL_FLAGS = 0
SYNCMGR_CF_WAIT: win32more.Windows.Win32.UI.Shell.SYNCMGR_CONTROL_FLAGS = 1
SYNCMGR_CF_NOUI: win32more.Windows.Win32.UI.Shell.SYNCMGR_CONTROL_FLAGS = 2
SYNCMGR_CF_VALID: win32more.Windows.Win32.UI.Shell.SYNCMGR_CONTROL_FLAGS = 3
SYNCMGR_EVENT_FLAGS = Int32
SYNCMGR_EF_NONE: win32more.Windows.Win32.UI.Shell.SYNCMGR_EVENT_FLAGS = 0
SYNCMGR_EF_VALID: win32more.Windows.Win32.UI.Shell.SYNCMGR_EVENT_FLAGS = 0
SYNCMGR_EVENT_LEVEL = Int32
SYNCMGR_EL_INFORMATION: win32more.Windows.Win32.UI.Shell.SYNCMGR_EVENT_LEVEL = 1
SYNCMGR_EL_WARNING: win32more.Windows.Win32.UI.Shell.SYNCMGR_EVENT_LEVEL = 2
SYNCMGR_EL_ERROR: win32more.Windows.Win32.UI.Shell.SYNCMGR_EVENT_LEVEL = 3
SYNCMGR_EL_MAX: win32more.Windows.Win32.UI.Shell.SYNCMGR_EVENT_LEVEL = 3
SYNCMGR_HANDLER_CAPABILITIES = Int32
SYNCMGR_HCM_NONE: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_CAPABILITIES = 0
SYNCMGR_HCM_PROVIDES_ICON: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_CAPABILITIES = 1
SYNCMGR_HCM_EVENT_STORE: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_CAPABILITIES = 2
SYNCMGR_HCM_CONFLICT_STORE: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_CAPABILITIES = 4
SYNCMGR_HCM_SUPPORTS_CONCURRENT_SESSIONS: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_CAPABILITIES = 16
SYNCMGR_HCM_CAN_BROWSE_CONTENT: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_CAPABILITIES = 65536
SYNCMGR_HCM_CAN_SHOW_SCHEDULE: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_CAPABILITIES = 131072
SYNCMGR_HCM_QUERY_BEFORE_ACTIVATE: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_CAPABILITIES = 1048576
SYNCMGR_HCM_QUERY_BEFORE_DEACTIVATE: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_CAPABILITIES = 2097152
SYNCMGR_HCM_QUERY_BEFORE_ENABLE: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_CAPABILITIES = 4194304
SYNCMGR_HCM_QUERY_BEFORE_DISABLE: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_CAPABILITIES = 8388608
SYNCMGR_HCM_VALID_MASK: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_CAPABILITIES = 15925271
SYNCMGR_HANDLER_POLICIES = Int32
SYNCMGR_HPM_NONE: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_POLICIES = 0
SYNCMGR_HPM_PREVENT_ACTIVATE: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_POLICIES = 1
SYNCMGR_HPM_PREVENT_DEACTIVATE: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_POLICIES = 2
SYNCMGR_HPM_PREVENT_ENABLE: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_POLICIES = 4
SYNCMGR_HPM_PREVENT_DISABLE: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_POLICIES = 8
SYNCMGR_HPM_PREVENT_START_SYNC: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_POLICIES = 16
SYNCMGR_HPM_PREVENT_STOP_SYNC: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_POLICIES = 32
SYNCMGR_HPM_DISABLE_ENABLE: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_POLICIES = 256
SYNCMGR_HPM_DISABLE_DISABLE: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_POLICIES = 512
SYNCMGR_HPM_DISABLE_START_SYNC: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_POLICIES = 1024
SYNCMGR_HPM_DISABLE_STOP_SYNC: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_POLICIES = 2048
SYNCMGR_HPM_DISABLE_BROWSE: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_POLICIES = 4096
SYNCMGR_HPM_DISABLE_SCHEDULE: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_POLICIES = 8192
SYNCMGR_HPM_HIDDEN_BY_DEFAULT: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_POLICIES = 65536
SYNCMGR_HPM_BACKGROUND_SYNC_ONLY: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_POLICIES = 48
SYNCMGR_HPM_VALID_MASK: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_POLICIES = 77631
SYNCMGR_HANDLER_TYPE = Int32
SYNCMGR_HT_UNSPECIFIED: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_TYPE = 0
SYNCMGR_HT_APPLICATION: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_TYPE = 1
SYNCMGR_HT_DEVICE: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_TYPE = 2
SYNCMGR_HT_FOLDER: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_TYPE = 3
SYNCMGR_HT_SERVICE: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_TYPE = 4
SYNCMGR_HT_COMPUTER: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_TYPE = 5
SYNCMGR_HT_MIN: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_TYPE = 0
SYNCMGR_HT_MAX: win32more.Windows.Win32.UI.Shell.SYNCMGR_HANDLER_TYPE = 5
SYNCMGR_ITEM_CAPABILITIES = Int32
SYNCMGR_ICM_NONE: win32more.Windows.Win32.UI.Shell.SYNCMGR_ITEM_CAPABILITIES = 0
SYNCMGR_ICM_PROVIDES_ICON: win32more.Windows.Win32.UI.Shell.SYNCMGR_ITEM_CAPABILITIES = 1
SYNCMGR_ICM_EVENT_STORE: win32more.Windows.Win32.UI.Shell.SYNCMGR_ITEM_CAPABILITIES = 2
SYNCMGR_ICM_CONFLICT_STORE: win32more.Windows.Win32.UI.Shell.SYNCMGR_ITEM_CAPABILITIES = 4
SYNCMGR_ICM_CAN_DELETE: win32more.Windows.Win32.UI.Shell.SYNCMGR_ITEM_CAPABILITIES = 16
SYNCMGR_ICM_CAN_BROWSE_CONTENT: win32more.Windows.Win32.UI.Shell.SYNCMGR_ITEM_CAPABILITIES = 65536
SYNCMGR_ICM_QUERY_BEFORE_ENABLE: win32more.Windows.Win32.UI.Shell.SYNCMGR_ITEM_CAPABILITIES = 1048576
SYNCMGR_ICM_QUERY_BEFORE_DISABLE: win32more.Windows.Win32.UI.Shell.SYNCMGR_ITEM_CAPABILITIES = 2097152
SYNCMGR_ICM_QUERY_BEFORE_DELETE: win32more.Windows.Win32.UI.Shell.SYNCMGR_ITEM_CAPABILITIES = 4194304
SYNCMGR_ICM_VALID_MASK: win32more.Windows.Win32.UI.Shell.SYNCMGR_ITEM_CAPABILITIES = 7405591
SYNCMGR_ITEM_POLICIES = Int32
SYNCMGR_IPM_NONE: win32more.Windows.Win32.UI.Shell.SYNCMGR_ITEM_POLICIES = 0
SYNCMGR_IPM_PREVENT_ENABLE: win32more.Windows.Win32.UI.Shell.SYNCMGR_ITEM_POLICIES = 1
SYNCMGR_IPM_PREVENT_DISABLE: win32more.Windows.Win32.UI.Shell.SYNCMGR_ITEM_POLICIES = 2
SYNCMGR_IPM_PREVENT_START_SYNC: win32more.Windows.Win32.UI.Shell.SYNCMGR_ITEM_POLICIES = 4
SYNCMGR_IPM_PREVENT_STOP_SYNC: win32more.Windows.Win32.UI.Shell.SYNCMGR_ITEM_POLICIES = 8
SYNCMGR_IPM_DISABLE_ENABLE: win32more.Windows.Win32.UI.Shell.SYNCMGR_ITEM_POLICIES = 16
SYNCMGR_IPM_DISABLE_DISABLE: win32more.Windows.Win32.UI.Shell.SYNCMGR_ITEM_POLICIES = 32
SYNCMGR_IPM_DISABLE_START_SYNC: win32more.Windows.Win32.UI.Shell.SYNCMGR_ITEM_POLICIES = 64
SYNCMGR_IPM_DISABLE_STOP_SYNC: win32more.Windows.Win32.UI.Shell.SYNCMGR_ITEM_POLICIES = 128
SYNCMGR_IPM_DISABLE_BROWSE: win32more.Windows.Win32.UI.Shell.SYNCMGR_ITEM_POLICIES = 256
SYNCMGR_IPM_DISABLE_DELETE: win32more.Windows.Win32.UI.Shell.SYNCMGR_ITEM_POLICIES = 512
SYNCMGR_IPM_HIDDEN_BY_DEFAULT: win32more.Windows.Win32.UI.Shell.SYNCMGR_ITEM_POLICIES = 65536
SYNCMGR_IPM_VALID_MASK: win32more.Windows.Win32.UI.Shell.SYNCMGR_ITEM_POLICIES = 66303
SYNCMGR_PRESENTER_CHOICE = Int32
SYNCMGR_PC_NO_CHOICE: win32more.Windows.Win32.UI.Shell.SYNCMGR_PRESENTER_CHOICE = 0
SYNCMGR_PC_KEEP_ONE: win32more.Windows.Win32.UI.Shell.SYNCMGR_PRESENTER_CHOICE = 1
SYNCMGR_PC_KEEP_MULTIPLE: win32more.Windows.Win32.UI.Shell.SYNCMGR_PRESENTER_CHOICE = 2
SYNCMGR_PC_KEEP_RECENT: win32more.Windows.Win32.UI.Shell.SYNCMGR_PRESENTER_CHOICE = 3
SYNCMGR_PC_REMOVE_FROM_SYNC_SET: win32more.Windows.Win32.UI.Shell.SYNCMGR_PRESENTER_CHOICE = 4
SYNCMGR_PC_SKIP: win32more.Windows.Win32.UI.Shell.SYNCMGR_PRESENTER_CHOICE = 5
SYNCMGR_PRESENTER_NEXT_STEP = Int32
SYNCMGR_PNS_CONTINUE: win32more.Windows.Win32.UI.Shell.SYNCMGR_PRESENTER_NEXT_STEP = 0
SYNCMGR_PNS_DEFAULT: win32more.Windows.Win32.UI.Shell.SYNCMGR_PRESENTER_NEXT_STEP = 1
SYNCMGR_PNS_CANCEL: win32more.Windows.Win32.UI.Shell.SYNCMGR_PRESENTER_NEXT_STEP = 2
SYNCMGR_PROGRESS_STATUS = Int32
SYNCMGR_PS_UPDATING: win32more.Windows.Win32.UI.Shell.SYNCMGR_PROGRESS_STATUS = 1
SYNCMGR_PS_UPDATING_INDETERMINATE: win32more.Windows.Win32.UI.Shell.SYNCMGR_PROGRESS_STATUS = 2
SYNCMGR_PS_SUCCEEDED: win32more.Windows.Win32.UI.Shell.SYNCMGR_PROGRESS_STATUS = 3
SYNCMGR_PS_FAILED: win32more.Windows.Win32.UI.Shell.SYNCMGR_PROGRESS_STATUS = 4
SYNCMGR_PS_CANCELED: win32more.Windows.Win32.UI.Shell.SYNCMGR_PROGRESS_STATUS = 5
SYNCMGR_PS_DISCONNECTED: win32more.Windows.Win32.UI.Shell.SYNCMGR_PROGRESS_STATUS = 6
SYNCMGR_PS_MAX: win32more.Windows.Win32.UI.Shell.SYNCMGR_PROGRESS_STATUS = 6
SYNCMGR_RESOLUTION_ABILITIES = Int32
SYNCMGR_RA_KEEPOTHER: win32more.Windows.Win32.UI.Shell.SYNCMGR_RESOLUTION_ABILITIES = 1
SYNCMGR_RA_KEEPRECENT: win32more.Windows.Win32.UI.Shell.SYNCMGR_RESOLUTION_ABILITIES = 2
SYNCMGR_RA_REMOVEFROMSYNCSET: win32more.Windows.Win32.UI.Shell.SYNCMGR_RESOLUTION_ABILITIES = 4
SYNCMGR_RA_KEEP_SINGLE: win32more.Windows.Win32.UI.Shell.SYNCMGR_RESOLUTION_ABILITIES = 8
SYNCMGR_RA_KEEP_MULTIPLE: win32more.Windows.Win32.UI.Shell.SYNCMGR_RESOLUTION_ABILITIES = 16
SYNCMGR_RA_VALID: win32more.Windows.Win32.UI.Shell.SYNCMGR_RESOLUTION_ABILITIES = 31
SYNCMGR_RESOLUTION_FEEDBACK = Int32
SYNCMGR_RF_CONTINUE: win32more.Windows.Win32.UI.Shell.SYNCMGR_RESOLUTION_FEEDBACK = 0
SYNCMGR_RF_REFRESH: win32more.Windows.Win32.UI.Shell.SYNCMGR_RESOLUTION_FEEDBACK = 1
SYNCMGR_RF_CANCEL: win32more.Windows.Win32.UI.Shell.SYNCMGR_RESOLUTION_FEEDBACK = 2
SYNCMGR_SYNC_CONTROL_FLAGS = Int32
SYNCMGR_SCF_NONE: win32more.Windows.Win32.UI.Shell.SYNCMGR_SYNC_CONTROL_FLAGS = 0
SYNCMGR_SCF_IGNORE_IF_ALREADY_SYNCING: win32more.Windows.Win32.UI.Shell.SYNCMGR_SYNC_CONTROL_FLAGS = 1
SYNCMGR_SCF_VALID: win32more.Windows.Win32.UI.Shell.SYNCMGR_SYNC_CONTROL_FLAGS = 1
SYNCMGR_UPDATE_REASON = Int32
SYNCMGR_UR_ADDED: win32more.Windows.Win32.UI.Shell.SYNCMGR_UPDATE_REASON = 0
SYNCMGR_UR_CHANGED: win32more.Windows.Win32.UI.Shell.SYNCMGR_UPDATE_REASON = 1
SYNCMGR_UR_REMOVED: win32more.Windows.Win32.UI.Shell.SYNCMGR_UPDATE_REASON = 2
SYNCMGR_UR_MAX: win32more.Windows.Win32.UI.Shell.SYNCMGR_UPDATE_REASON = 2
ScheduledTasks = Guid('{d6277990-4c6a-11cf-8d87-00aa0060f5bf}')
SearchFolderItemFactory = Guid('{14010e02-bbbd-41f0-88e3-eda371216584}')
SecureLockIconConstants = Int32
secureLockIconUnsecure: win32more.Windows.Win32.UI.Shell.SecureLockIconConstants = 0
secureLockIconMixed: win32more.Windows.Win32.UI.Shell.SecureLockIconConstants = 1
secureLockIconSecureUnknownBits: win32more.Windows.Win32.UI.Shell.SecureLockIconConstants = 2
secureLockIconSecure40Bit: win32more.Windows.Win32.UI.Shell.SecureLockIconConstants = 3
secureLockIconSecure56Bit: win32more.Windows.Win32.UI.Shell.SecureLockIconConstants = 4
secureLockIconSecureFortezza: win32more.Windows.Win32.UI.Shell.SecureLockIconConstants = 5
secureLockIconSecure128Bit: win32more.Windows.Win32.UI.Shell.SecureLockIconConstants = 6
SharedBitmap = Guid('{4db26476-6787-4046-b836-e8412a9e8a27}')
SharingConfigurationManager = Guid('{49f371e1-8c5c-4d9c-9a3b-54a6827f513c}')
Shell = Guid('{13709620-c279-11ce-a49e-444553540000}')
ShellBrowserWindow = Guid('{c08afd90-f2a1-11d1-8455-00a0c91f3880}')
ShellDesktop = Guid('{00021400-0000-0000-c000-000000000046}')
ShellDispatchInproc = Guid('{0a89a860-d7b1-11ce-8350-444553540000}')
ShellFSFolder = Guid('{f3364ba0-65b9-11ce-a9ba-00aa004ae837}')
ShellFolderItem = Guid('{2fe352ea-fd1f-11d2-b1f4-00c04f8eeb3e}')
ShellFolderView = Guid('{62112aa1-ebe4-11cf-a5fb-0020afe7292d}')
ShellFolderViewOC = Guid('{9ba05971-f6a8-11cf-a442-00a0c90a8f39}')
ShellFolderViewOptions = Int32
SFVVO_SHOWALLOBJECTS: win32more.Windows.Win32.UI.Shell.ShellFolderViewOptions = 1
SFVVO_SHOWEXTENSIONS: win32more.Windows.Win32.UI.Shell.ShellFolderViewOptions = 2
SFVVO_SHOWCOMPCOLOR: win32more.Windows.Win32.UI.Shell.ShellFolderViewOptions = 8
SFVVO_SHOWSYSFILES: win32more.Windows.Win32.UI.Shell.ShellFolderViewOptions = 32
SFVVO_WIN95CLASSIC: win32more.Windows.Win32.UI.Shell.ShellFolderViewOptions = 64
SFVVO_DOUBLECLICKINWEBVIEW: win32more.Windows.Win32.UI.Shell.ShellFolderViewOptions = 128
SFVVO_DESKTOPHTML: win32more.Windows.Win32.UI.Shell.ShellFolderViewOptions = 512
ShellImageDataFactory = Guid('{66e4e4fb-f385-4dd0-8d74-a2efd1bc6178}')
ShellItem = Guid('{9ac9fbe1-e0a2-4ad6-b4ee-e212013ea917}')
ShellLibrary = Guid('{d9b3211d-e57f-4426-aaef-30a806add397}')
ShellLink = Guid('{00021401-0000-0000-c000-000000000046}')
ShellLinkObject = Guid('{11219420-1768-11d1-95be-00609797ea4f}')
ShellNameSpace = Guid('{55136805-b2de-11d1-b9f2-00a0c98bc547}')
ShellSpecialFolderConstants = Int32
ssfDESKTOP: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 0
ssfPROGRAMS: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 2
ssfCONTROLS: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 3
ssfPRINTERS: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 4
ssfPERSONAL: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 5
ssfFAVORITES: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 6
ssfSTARTUP: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 7
ssfRECENT: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 8
ssfSENDTO: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 9
ssfBITBUCKET: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 10
ssfSTARTMENU: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 11
ssfDESKTOPDIRECTORY: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 16
ssfDRIVES: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 17
ssfNETWORK: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 18
ssfNETHOOD: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 19
ssfFONTS: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 20
ssfTEMPLATES: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 21
ssfCOMMONSTARTMENU: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 22
ssfCOMMONPROGRAMS: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 23
ssfCOMMONSTARTUP: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 24
ssfCOMMONDESKTOPDIR: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 25
ssfAPPDATA: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 26
ssfPRINTHOOD: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 27
ssfLOCALAPPDATA: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 28
ssfALTSTARTUP: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 29
ssfCOMMONALTSTARTUP: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 30
ssfCOMMONFAVORITES: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 31
ssfINTERNETCACHE: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 32
ssfCOOKIES: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 33
ssfHISTORY: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 34
ssfCOMMONAPPDATA: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 35
ssfWINDOWS: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 36
ssfSYSTEM: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 37
ssfPROGRAMFILES: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 38
ssfMYPICTURES: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 39
ssfPROFILE: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 40
ssfSYSTEMx86: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 41
ssfPROGRAMFILESx86: win32more.Windows.Win32.UI.Shell.ShellSpecialFolderConstants = 48
ShellUIHelper = Guid('{64ab4bb7-111e-11d1-8f79-00c04fc2fbe1}')
ShellWindowFindWindowOptions = Int32
SWFO_NEEDDISPATCH: win32more.Windows.Win32.UI.Shell.ShellWindowFindWindowOptions = 1
SWFO_INCLUDEPENDING: win32more.Windows.Win32.UI.Shell.ShellWindowFindWindowOptions = 2
SWFO_COOKIEPASSED: win32more.Windows.Win32.UI.Shell.ShellWindowFindWindowOptions = 4
ShellWindowTypeConstants = Int32
SWC_EXPLORER: win32more.Windows.Win32.UI.Shell.ShellWindowTypeConstants = 0
SWC_BROWSER: win32more.Windows.Win32.UI.Shell.ShellWindowTypeConstants = 1
SWC_3RDPARTY: win32more.Windows.Win32.UI.Shell.ShellWindowTypeConstants = 2
SWC_CALLBACK: win32more.Windows.Win32.UI.Shell.ShellWindowTypeConstants = 4
SWC_DESKTOP: win32more.Windows.Win32.UI.Shell.ShellWindowTypeConstants = 8
ShellWindows = Guid('{9ba05972-f6a8-11cf-a442-00a0c90a8f39}')
ShowInputPaneAnimationCoordinator = Guid('{1f046abf-3202-4dc1-8cb5-3c67617ce1fa}')
SimpleConflictPresenter = Guid('{7a0f6ab7-ed84-46b6-b47e-02aa159a152b}')
SizeCategorizer = Guid('{55d7b852-f6d1-42f2-aa75-8728a1b2d264}')
SmartcardCredentialProvider = Guid('{8fd7e19c-3bf7-489b-a72c-846ab3678c96}')
SmartcardPinProvider = Guid('{94596c7e-3744-41ce-893e-bbf09122f76a}')
SmartcardReaderSelectionProvider = Guid('{1b283861-754f-4022-ad47-a5eaaa618894}')
SmartcardWinRTProvider = Guid('{1ee7337f-85ac-45e2-a23c-37c753209769}')
StartMenuPin = Guid('{a2a9545d-a0c2-42b4-9708-a0b2badd77c8}')
StorageProviderBanners = Guid('{7ccdf9f4-e576-455a-8bc7-f6ec68d6f063}')
SuspensionDependencyManager = Guid('{6b273fc5-61fd-4918-95a2-c3b5e9d7f581}')
SyncMgr = Guid('{6295df27-35ee-11d1-8707-00c04fd93327}')
SyncMgrClient = Guid('{1202db60-1dac-42c5-aed5-1abdd432248e}')
SyncMgrControl = Guid('{1a1f4206-0688-4e7f-be03-d82ec69df9a5}')
SyncMgrFolder = Guid('{9c73f5e5-7ae7-4e32-a8e8-8d23b85255bf}')
SyncMgrScheduleWizard = Guid('{8d8b8e30-c451-421b-8553-d2976afa648c}')
SyncResultsFolder = Guid('{71d99464-3b6b-475c-b241-e15883207529}')
SyncSetupFolder = Guid('{2e9e59c0-b437-4981-a647-9c34b9b90891}')
class TBINFO(Structure):
    cbuttons: UInt32
    uFlags: UInt32
TBPFLAG = Int32
TBPF_NOPROGRESS: win32more.Windows.Win32.UI.Shell.TBPFLAG = 0
TBPF_INDETERMINATE: win32more.Windows.Win32.UI.Shell.TBPFLAG = 1
TBPF_NORMAL: win32more.Windows.Win32.UI.Shell.TBPFLAG = 2
TBPF_ERROR: win32more.Windows.Win32.UI.Shell.TBPFLAG = 4
TBPF_PAUSED: win32more.Windows.Win32.UI.Shell.TBPFLAG = 8
class THUMBBUTTON(Structure):
    dwMask: win32more.Windows.Win32.UI.Shell.THUMBBUTTONMASK
    iId: UInt32
    iBitmap: UInt32
    hIcon: win32more.Windows.Win32.UI.WindowsAndMessaging.HICON
    szTip: Char * 260
    dwFlags: win32more.Windows.Win32.UI.Shell.THUMBBUTTONFLAGS
THUMBBUTTONFLAGS = Int32
THBF_ENABLED: win32more.Windows.Win32.UI.Shell.THUMBBUTTONFLAGS = 0
THBF_DISABLED: win32more.Windows.Win32.UI.Shell.THUMBBUTTONFLAGS = 1
THBF_DISMISSONCLICK: win32more.Windows.Win32.UI.Shell.THUMBBUTTONFLAGS = 2
THBF_NOBACKGROUND: win32more.Windows.Win32.UI.Shell.THUMBBUTTONFLAGS = 4
THBF_HIDDEN: win32more.Windows.Win32.UI.Shell.THUMBBUTTONFLAGS = 8
THBF_NONINTERACTIVE: win32more.Windows.Win32.UI.Shell.THUMBBUTTONFLAGS = 16
THUMBBUTTONMASK = Int32
THB_BITMAP: win32more.Windows.Win32.UI.Shell.THUMBBUTTONMASK = 1
THB_ICON: win32more.Windows.Win32.UI.Shell.THUMBBUTTONMASK = 2
THB_TOOLTIP: win32more.Windows.Win32.UI.Shell.THUMBBUTTONMASK = 4
THB_FLAGS: win32more.Windows.Win32.UI.Shell.THUMBBUTTONMASK = 8
TI_FLAGS = Int32
TI_BITMAP: win32more.Windows.Win32.UI.Shell.TI_FLAGS = 1
TI_JPEG: win32more.Windows.Win32.UI.Shell.TI_FLAGS = 2
TLENUMF = Int32
TLEF_RELATIVE_INCLUDE_CURRENT: win32more.Windows.Win32.UI.Shell.TLENUMF = 1
TLEF_RELATIVE_BACK: win32more.Windows.Win32.UI.Shell.TLENUMF = 16
TLEF_RELATIVE_FORE: win32more.Windows.Win32.UI.Shell.TLENUMF = 32
TLEF_INCLUDE_UNINVOKEABLE: win32more.Windows.Win32.UI.Shell.TLENUMF = 64
TLEF_ABSOLUTE: win32more.Windows.Win32.UI.Shell.TLENUMF = 49
TLEF_EXCLUDE_SUBFRAME_ENTRIES: win32more.Windows.Win32.UI.Shell.TLENUMF = 128
TLEF_EXCLUDE_ABOUT_PAGES: win32more.Windows.Win32.UI.Shell.TLENUMF = 256
class TOOLBARITEM(Structure):
    ptbar: win32more.Windows.Win32.UI.Shell.IDockingWindow
    rcBorderTool: win32more.Windows.Win32.Foundation.RECT
    pwszItem: win32more.Windows.Win32.Foundation.PWSTR
    fShow: win32more.Windows.Win32.Foundation.BOOL
    hMon: win32more.Windows.Win32.Graphics.Gdi.HMONITOR
TRANSLATEURL_IN_FLAGS = Int32
TRANSLATEURL_FL_GUESS_PROTOCOL: win32more.Windows.Win32.UI.Shell.TRANSLATEURL_IN_FLAGS = 1
TRANSLATEURL_FL_USE_DEFAULT_PROTOCOL: win32more.Windows.Win32.UI.Shell.TRANSLATEURL_IN_FLAGS = 2
TaskbarList = Guid('{56fdf344-fd6d-11d0-958a-006097c9a090}')
ThumbnailStreamCache = Guid('{cbe0fed3-4b91-4e90-8354-8a8c84ec6872}')
ThumbnailStreamCacheOptions = Int32
ExtractIfNotCached: win32more.Windows.Win32.UI.Shell.ThumbnailStreamCacheOptions = 0
ReturnOnlyIfCached: win32more.Windows.Win32.UI.Shell.ThumbnailStreamCacheOptions = 1
ResizeThumbnail: win32more.Windows.Win32.UI.Shell.ThumbnailStreamCacheOptions = 2
AllowSmallerSize: win32more.Windows.Win32.UI.Shell.ThumbnailStreamCacheOptions = 4
TimeCategorizer = Guid('{3bb4118f-ddfd-4d30-a348-9fb5d6bf1afe}')
TrackShellMenu = Guid('{8278f931-2a3e-11d2-838f-00c04fd918d0}')
TrayBandSiteService = Guid('{f60ad0a0-e5e1-45cb-b51a-e15b9f8b2934}')
TrayDeskBand = Guid('{e6442437-6c68-4f52-94dd-2cfed267efb9}')
UNDOCK_REASON = Int32
UR_RESOLUTION_CHANGE: win32more.Windows.Win32.UI.Shell.UNDOCK_REASON = 0
UR_MONITOR_DISCONNECT: win32more.Windows.Win32.UI.Shell.UNDOCK_REASON = 1
URLASSOCIATIONDIALOG_IN_FLAGS = Int32
URLASSOCDLG_FL_USE_DEFAULT_NAME: win32more.Windows.Win32.UI.Shell.URLASSOCIATIONDIALOG_IN_FLAGS = 1
URLASSOCDLG_FL_REGISTER_ASSOC: win32more.Windows.Win32.UI.Shell.URLASSOCIATIONDIALOG_IN_FLAGS = 2
class URLINVOKECOMMANDINFOA(Structure):
    dwcbSize: UInt32
    dwFlags: UInt32
    hwndParent: win32more.Windows.Win32.Foundation.HWND
    pcszVerb: win32more.Windows.Win32.Foundation.PSTR
class URLINVOKECOMMANDINFOW(Structure):
    dwcbSize: UInt32
    dwFlags: UInt32
    hwndParent: win32more.Windows.Win32.Foundation.HWND
    pcszVerb: win32more.Windows.Win32.Foundation.PWSTR
URLINVOKECOMMANDINFO = UnicodeAlias('URLINVOKECOMMANDINFOW')
URLIS = Int32
URLIS_URL: win32more.Windows.Win32.UI.Shell.URLIS = 0
URLIS_OPAQUE: win32more.Windows.Win32.UI.Shell.URLIS = 1
URLIS_NOHISTORY: win32more.Windows.Win32.UI.Shell.URLIS = 2
URLIS_FILEURL: win32more.Windows.Win32.UI.Shell.URLIS = 3
URLIS_APPLIABLE: win32more.Windows.Win32.UI.Shell.URLIS = 4
URLIS_DIRECTORY: win32more.Windows.Win32.UI.Shell.URLIS = 5
URLIS_HASQUERY: win32more.Windows.Win32.UI.Shell.URLIS = 6
URL_PART = Int32
URL_PART_NONE: win32more.Windows.Win32.UI.Shell.URL_PART = 0
URL_PART_SCHEME: win32more.Windows.Win32.UI.Shell.URL_PART = 1
URL_PART_HOSTNAME: win32more.Windows.Win32.UI.Shell.URL_PART = 2
URL_PART_USERNAME: win32more.Windows.Win32.UI.Shell.URL_PART = 3
URL_PART_PASSWORD: win32more.Windows.Win32.UI.Shell.URL_PART = 4
URL_PART_PORT: win32more.Windows.Win32.UI.Shell.URL_PART = 5
URL_PART_QUERY: win32more.Windows.Win32.UI.Shell.URL_PART = 6
URL_SCHEME = Int32
URL_SCHEME_INVALID: win32more.Windows.Win32.UI.Shell.URL_SCHEME = -1
URL_SCHEME_UNKNOWN: win32more.Windows.Win32.UI.Shell.URL_SCHEME = 0
URL_SCHEME_FTP: win32more.Windows.Win32.UI.Shell.URL_SCHEME = 1
URL_SCHEME_HTTP: win32more.Windows.Win32.UI.Shell.URL_SCHEME = 2
URL_SCHEME_GOPHER: win32more.Windows.Win32.UI.Shell.URL_SCHEME = 3
URL_SCHEME_MAILTO: win32more.Windows.Win32.UI.Shell.URL_SCHEME = 4
URL_SCHEME_NEWS: win32more.Windows.Win32.UI.Shell.URL_SCHEME = 5
URL_SCHEME_NNTP: win32more.Windows.Win32.UI.Shell.URL_SCHEME = 6
URL_SCHEME_TELNET: win32more.Windows.Win32.UI.Shell.URL_SCHEME = 7
URL_SCHEME_WAIS: win32more.Windows.Win32.UI.Shell.URL_SCHEME = 8
URL_SCHEME_FILE: win32more.Windows.Win32.UI.Shell.URL_SCHEME = 9
URL_SCHEME_MK: win32more.Windows.Win32.UI.Shell.URL_SCHEME = 10
URL_SCHEME_HTTPS: win32more.Windows.Win32.UI.Shell.URL_SCHEME = 11
URL_SCHEME_SHELL: win32more.Windows.Win32.UI.Shell.URL_SCHEME = 12
URL_SCHEME_SNEWS: win32more.Windows.Win32.UI.Shell.URL_SCHEME = 13
URL_SCHEME_LOCAL: win32more.Windows.Win32.UI.Shell.URL_SCHEME = 14
URL_SCHEME_JAVASCRIPT: win32more.Windows.Win32.UI.Shell.URL_SCHEME = 15
URL_SCHEME_VBSCRIPT: win32more.Windows.Win32.UI.Shell.URL_SCHEME = 16
URL_SCHEME_ABOUT: win32more.Windows.Win32.UI.Shell.URL_SCHEME = 17
URL_SCHEME_RES: win32more.Windows.Win32.UI.Shell.URL_SCHEME = 18
URL_SCHEME_MSSHELLROOTED: win32more.Windows.Win32.UI.Shell.URL_SCHEME = 19
URL_SCHEME_MSSHELLIDLIST: win32more.Windows.Win32.UI.Shell.URL_SCHEME = 20
URL_SCHEME_MSHELP: win32more.Windows.Win32.UI.Shell.URL_SCHEME = 21
URL_SCHEME_MSSHELLDEVICE: win32more.Windows.Win32.UI.Shell.URL_SCHEME = 22
URL_SCHEME_WILDCARD: win32more.Windows.Win32.UI.Shell.URL_SCHEME = 23
URL_SCHEME_SEARCH_MS: win32more.Windows.Win32.UI.Shell.URL_SCHEME = 24
URL_SCHEME_SEARCH: win32more.Windows.Win32.UI.Shell.URL_SCHEME = 25
URL_SCHEME_KNOWNFOLDER: win32more.Windows.Win32.UI.Shell.URL_SCHEME = 26
URL_SCHEME_MAXVALUE: win32more.Windows.Win32.UI.Shell.URL_SCHEME = 27
UserNotification = Guid('{0010890e-8789-413c-adbc-48f5b511b3af}')
V1PasswordCredentialProvider = Guid('{6f45dc1e-5384-457a-bc13-2cd81b0d28ed}')
V1SmartcardCredentialProvider = Guid('{8bf9a910-a8ff-457f-999f-a5ca10b4a885}')
V1WinBioCredentialProvider = Guid('{ac3ac249-e820-4343-a65b-377ac634dc09}')
VALIDATEUNC_OPTION = Int32
VALIDATEUNC_CONNECT: win32more.Windows.Win32.UI.Shell.VALIDATEUNC_OPTION = 1
VALIDATEUNC_NOUI: win32more.Windows.Win32.UI.Shell.VALIDATEUNC_OPTION = 2
VALIDATEUNC_PRINT: win32more.Windows.Win32.UI.Shell.VALIDATEUNC_OPTION = 4
VALIDATEUNC_PERSIST: win32more.Windows.Win32.UI.Shell.VALIDATEUNC_OPTION = 8
VALIDATEUNC_VALID: win32more.Windows.Win32.UI.Shell.VALIDATEUNC_OPTION = 15
VPCOLORFLAGS = Int32
VPCF_TEXT: win32more.Windows.Win32.UI.Shell.VPCOLORFLAGS = 1
VPCF_BACKGROUND: win32more.Windows.Win32.UI.Shell.VPCOLORFLAGS = 2
VPCF_SORTCOLUMN: win32more.Windows.Win32.UI.Shell.VPCOLORFLAGS = 3
VPCF_SUBTEXT: win32more.Windows.Win32.UI.Shell.VPCOLORFLAGS = 4
VPCF_TEXTBACKGROUND: win32more.Windows.Win32.UI.Shell.VPCOLORFLAGS = 5
VPWATERMARKFLAGS = Int32
VPWF_DEFAULT: win32more.Windows.Win32.UI.Shell.VPWATERMARKFLAGS = 0
VPWF_ALPHABLEND: win32more.Windows.Win32.UI.Shell.VPWATERMARKFLAGS = 1
VaultProvider = Guid('{503739d0-4c5e-4cfd-b3ba-d881334f0df2}')
VirtualDesktopManager = Guid('{aa509086-5ca9-4c25-8f95-589d3c07b48a}')
class WINDOWDATA(Structure):
    dwWindowID: UInt32
    uiCP: UInt32
    pidl: POINTER(win32more.Windows.Win32.UI.Shell.Common.ITEMIDLIST)
    lpszUrl: win32more.Windows.Win32.Foundation.PWSTR
    lpszUrlLocation: win32more.Windows.Win32.Foundation.PWSTR
    lpszTitle: win32more.Windows.Win32.Foundation.PWSTR
WTS_ALPHATYPE = Int32
WTSAT_UNKNOWN: win32more.Windows.Win32.UI.Shell.WTS_ALPHATYPE = 0
WTSAT_RGB: win32more.Windows.Win32.UI.Shell.WTS_ALPHATYPE = 1
WTSAT_ARGB: win32more.Windows.Win32.UI.Shell.WTS_ALPHATYPE = 2
WTS_CACHEFLAGS = Int32
WTS_DEFAULT: win32more.Windows.Win32.UI.Shell.WTS_CACHEFLAGS = 0
WTS_LOWQUALITY: win32more.Windows.Win32.UI.Shell.WTS_CACHEFLAGS = 1
WTS_CACHED: win32more.Windows.Win32.UI.Shell.WTS_CACHEFLAGS = 2
WTS_CONTEXTFLAGS = Int32
WTSCF_DEFAULT: win32more.Windows.Win32.UI.Shell.WTS_CONTEXTFLAGS = 0
WTSCF_APPSTYLE: win32more.Windows.Win32.UI.Shell.WTS_CONTEXTFLAGS = 1
WTSCF_SQUARE: win32more.Windows.Win32.UI.Shell.WTS_CONTEXTFLAGS = 2
WTSCF_WIDE: win32more.Windows.Win32.UI.Shell.WTS_CONTEXTFLAGS = 4
WTSCF_FAST: win32more.Windows.Win32.UI.Shell.WTS_CONTEXTFLAGS = 8
WTS_FLAGS = Int32
WTS_NONE: win32more.Windows.Win32.UI.Shell.WTS_FLAGS = 0
WTS_EXTRACT: win32more.Windows.Win32.UI.Shell.WTS_FLAGS = 0
WTS_INCACHEONLY: win32more.Windows.Win32.UI.Shell.WTS_FLAGS = 1
WTS_FASTEXTRACT: win32more.Windows.Win32.UI.Shell.WTS_FLAGS = 2
WTS_FORCEEXTRACTION: win32more.Windows.Win32.UI.Shell.WTS_FLAGS = 4
WTS_SLOWRECLAIM: win32more.Windows.Win32.UI.Shell.WTS_FLAGS = 8
WTS_EXTRACTDONOTCACHE: win32more.Windows.Win32.UI.Shell.WTS_FLAGS = 32
WTS_SCALETOREQUESTEDSIZE: win32more.Windows.Win32.UI.Shell.WTS_FLAGS = 64
WTS_SKIPFASTEXTRACT: win32more.Windows.Win32.UI.Shell.WTS_FLAGS = 128
WTS_EXTRACTINPROC: win32more.Windows.Win32.UI.Shell.WTS_FLAGS = 256
WTS_CROPTOSQUARE: win32more.Windows.Win32.UI.Shell.WTS_FLAGS = 512
WTS_INSTANCESURROGATE: win32more.Windows.Win32.UI.Shell.WTS_FLAGS = 1024
WTS_REQUIRESURROGATE: win32more.Windows.Win32.UI.Shell.WTS_FLAGS = 2048
WTS_APPSTYLE: win32more.Windows.Win32.UI.Shell.WTS_FLAGS = 8192
WTS_WIDETHUMBNAILS: win32more.Windows.Win32.UI.Shell.WTS_FLAGS = 16384
WTS_IDEALCACHESIZEONLY: win32more.Windows.Win32.UI.Shell.WTS_FLAGS = 32768
WTS_SCALEUP: win32more.Windows.Win32.UI.Shell.WTS_FLAGS = 65536
class WTS_THUMBNAILID(Structure):
    rgbKey: Byte * 16
WebBrowser = Guid('{8856f961-340a-11d0-a96b-00c04fd705a2}')
WebBrowser_V1 = Guid('{eab22ac3-30c1-11cf-a7eb-0000c05bae0b}')
WebWizardHost = Guid('{c827f149-55c1-4d28-935e-57e47caed973}')
WinBioCredentialProvider = Guid('{bec09223-b018-416d-a0ac-523971b639f5}')
_BROWSERFRAMEOPTIONS = Int32
BFO_NONE: win32more.Windows.Win32.UI.Shell._BROWSERFRAMEOPTIONS = 0
BFO_BROWSER_PERSIST_SETTINGS: win32more.Windows.Win32.UI.Shell._BROWSERFRAMEOPTIONS = 1
BFO_RENAME_FOLDER_OPTIONS_TOINTERNET: win32more.Windows.Win32.UI.Shell._BROWSERFRAMEOPTIONS = 2
BFO_BOTH_OPTIONS: win32more.Windows.Win32.UI.Shell._BROWSERFRAMEOPTIONS = 4
BIF_PREFER_INTERNET_SHORTCUT: win32more.Windows.Win32.UI.Shell._BROWSERFRAMEOPTIONS = 8
BFO_BROWSE_NO_IN_NEW_PROCESS: win32more.Windows.Win32.UI.Shell._BROWSERFRAMEOPTIONS = 16
BFO_ENABLE_HYPERLINK_TRACKING: win32more.Windows.Win32.UI.Shell._BROWSERFRAMEOPTIONS = 32
BFO_USE_IE_OFFLINE_SUPPORT: win32more.Windows.Win32.UI.Shell._BROWSERFRAMEOPTIONS = 64
BFO_SUBSTITUE_INTERNET_START_PAGE: win32more.Windows.Win32.UI.Shell._BROWSERFRAMEOPTIONS = 128
BFO_USE_IE_LOGOBANDING: win32more.Windows.Win32.UI.Shell._BROWSERFRAMEOPTIONS = 256
BFO_ADD_IE_TOCAPTIONBAR: win32more.Windows.Win32.UI.Shell._BROWSERFRAMEOPTIONS = 512
BFO_USE_DIALUP_REF: win32more.Windows.Win32.UI.Shell._BROWSERFRAMEOPTIONS = 1024
BFO_USE_IE_TOOLBAR: win32more.Windows.Win32.UI.Shell._BROWSERFRAMEOPTIONS = 2048
BFO_NO_PARENT_FOLDER_SUPPORT: win32more.Windows.Win32.UI.Shell._BROWSERFRAMEOPTIONS = 4096
BFO_NO_REOPEN_NEXT_RESTART: win32more.Windows.Win32.UI.Shell._BROWSERFRAMEOPTIONS = 8192
BFO_GO_HOME_PAGE: win32more.Windows.Win32.UI.Shell._BROWSERFRAMEOPTIONS = 16384
BFO_PREFER_IEPROCESS: win32more.Windows.Win32.UI.Shell._BROWSERFRAMEOPTIONS = 32768
BFO_SHOW_NAVIGATION_CANCELLED: win32more.Windows.Win32.UI.Shell._BROWSERFRAMEOPTIONS = 65536
BFO_USE_IE_STATUSBAR: win32more.Windows.Win32.UI.Shell._BROWSERFRAMEOPTIONS = 131072
BFO_QUERY_ALL: win32more.Windows.Win32.UI.Shell._BROWSERFRAMEOPTIONS = -1
_CDBE_ACTIONS = Int32
CDBE_TYPE_MUSIC: win32more.Windows.Win32.UI.Shell._CDBE_ACTIONS = 1
CDBE_TYPE_DATA: win32more.Windows.Win32.UI.Shell._CDBE_ACTIONS = 2
CDBE_TYPE_ALL: win32more.Windows.Win32.UI.Shell._CDBE_ACTIONS = -1
_EXPCMDFLAGS = Int32
ECF_DEFAULT: win32more.Windows.Win32.UI.Shell._EXPCMDFLAGS = 0
ECF_HASSUBCOMMANDS: win32more.Windows.Win32.UI.Shell._EXPCMDFLAGS = 1
ECF_HASSPLITBUTTON: win32more.Windows.Win32.UI.Shell._EXPCMDFLAGS = 2
ECF_HIDELABEL: win32more.Windows.Win32.UI.Shell._EXPCMDFLAGS = 4
ECF_ISSEPARATOR: win32more.Windows.Win32.UI.Shell._EXPCMDFLAGS = 8
ECF_HASLUASHIELD: win32more.Windows.Win32.UI.Shell._EXPCMDFLAGS = 16
ECF_SEPARATORBEFORE: win32more.Windows.Win32.UI.Shell._EXPCMDFLAGS = 32
ECF_SEPARATORAFTER: win32more.Windows.Win32.UI.Shell._EXPCMDFLAGS = 64
ECF_ISDROPDOWN: win32more.Windows.Win32.UI.Shell._EXPCMDFLAGS = 128
ECF_TOGGLEABLE: win32more.Windows.Win32.UI.Shell._EXPCMDFLAGS = 256
ECF_AUTOMENUICONS: win32more.Windows.Win32.UI.Shell._EXPCMDFLAGS = 512
_EXPCMDSTATE = Int32
ECS_ENABLED: win32more.Windows.Win32.UI.Shell._EXPCMDSTATE = 0
ECS_DISABLED: win32more.Windows.Win32.UI.Shell._EXPCMDSTATE = 1
ECS_HIDDEN: win32more.Windows.Win32.UI.Shell._EXPCMDSTATE = 2
ECS_CHECKBOX: win32more.Windows.Win32.UI.Shell._EXPCMDSTATE = 4
ECS_CHECKED: win32more.Windows.Win32.UI.Shell._EXPCMDSTATE = 8
ECS_RADIOCHECK: win32more.Windows.Win32.UI.Shell._EXPCMDSTATE = 16
_EXPLORERPANESTATE = Int32
EPS_DONTCARE: win32more.Windows.Win32.UI.Shell._EXPLORERPANESTATE = 0
EPS_DEFAULT_ON: win32more.Windows.Win32.UI.Shell._EXPLORERPANESTATE = 1
EPS_DEFAULT_OFF: win32more.Windows.Win32.UI.Shell._EXPLORERPANESTATE = 2
EPS_STATEMASK: win32more.Windows.Win32.UI.Shell._EXPLORERPANESTATE = 65535
EPS_INITIALSTATE: win32more.Windows.Win32.UI.Shell._EXPLORERPANESTATE = 65536
EPS_FORCE: win32more.Windows.Win32.UI.Shell._EXPLORERPANESTATE = 131072
_EXPPS = Int32
EXPPS_FILETYPES: win32more.Windows.Win32.UI.Shell._EXPPS = 1
_KF_DEFINITION_FLAGS = Int32
KFDF_LOCAL_REDIRECT_ONLY: win32more.Windows.Win32.UI.Shell._KF_DEFINITION_FLAGS = 2
KFDF_ROAMABLE: win32more.Windows.Win32.UI.Shell._KF_DEFINITION_FLAGS = 4
KFDF_PRECREATE: win32more.Windows.Win32.UI.Shell._KF_DEFINITION_FLAGS = 8
KFDF_STREAM: win32more.Windows.Win32.UI.Shell._KF_DEFINITION_FLAGS = 16
KFDF_PUBLISHEXPANDEDPATH: win32more.Windows.Win32.UI.Shell._KF_DEFINITION_FLAGS = 32
KFDF_NO_REDIRECT_UI: win32more.Windows.Win32.UI.Shell._KF_DEFINITION_FLAGS = 64
_KF_REDIRECTION_CAPABILITIES = Int32
KF_REDIRECTION_CAPABILITIES_ALLOW_ALL: win32more.Windows.Win32.UI.Shell._KF_REDIRECTION_CAPABILITIES = 255
KF_REDIRECTION_CAPABILITIES_REDIRECTABLE: win32more.Windows.Win32.UI.Shell._KF_REDIRECTION_CAPABILITIES = 1
KF_REDIRECTION_CAPABILITIES_DENY_ALL: win32more.Windows.Win32.UI.Shell._KF_REDIRECTION_CAPABILITIES = 1048320
KF_REDIRECTION_CAPABILITIES_DENY_POLICY_REDIRECTED: win32more.Windows.Win32.UI.Shell._KF_REDIRECTION_CAPABILITIES = 256
KF_REDIRECTION_CAPABILITIES_DENY_POLICY: win32more.Windows.Win32.UI.Shell._KF_REDIRECTION_CAPABILITIES = 512
KF_REDIRECTION_CAPABILITIES_DENY_PERMISSIONS: win32more.Windows.Win32.UI.Shell._KF_REDIRECTION_CAPABILITIES = 1024
_KF_REDIRECT_FLAGS = Int32
KF_REDIRECT_USER_EXCLUSIVE: win32more.Windows.Win32.UI.Shell._KF_REDIRECT_FLAGS = 1
KF_REDIRECT_COPY_SOURCE_DACL: win32more.Windows.Win32.UI.Shell._KF_REDIRECT_FLAGS = 2
KF_REDIRECT_OWNER_USER: win32more.Windows.Win32.UI.Shell._KF_REDIRECT_FLAGS = 4
KF_REDIRECT_SET_OWNER_EXPLICIT: win32more.Windows.Win32.UI.Shell._KF_REDIRECT_FLAGS = 8
KF_REDIRECT_CHECK_ONLY: win32more.Windows.Win32.UI.Shell._KF_REDIRECT_FLAGS = 16
KF_REDIRECT_WITH_UI: win32more.Windows.Win32.UI.Shell._KF_REDIRECT_FLAGS = 32
KF_REDIRECT_UNPIN: win32more.Windows.Win32.UI.Shell._KF_REDIRECT_FLAGS = 64
KF_REDIRECT_PIN: win32more.Windows.Win32.UI.Shell._KF_REDIRECT_FLAGS = 128
KF_REDIRECT_COPY_CONTENTS: win32more.Windows.Win32.UI.Shell._KF_REDIRECT_FLAGS = 512
KF_REDIRECT_DEL_SOURCE_CONTENTS: win32more.Windows.Win32.UI.Shell._KF_REDIRECT_FLAGS = 1024
KF_REDIRECT_EXCLUDE_ALL_KNOWN_SUBFOLDERS: win32more.Windows.Win32.UI.Shell._KF_REDIRECT_FLAGS = 2048
_NMCII_FLAGS = Int32
NMCII_NONE: win32more.Windows.Win32.UI.Shell._NMCII_FLAGS = 0
NMCII_ITEMS: win32more.Windows.Win32.UI.Shell._NMCII_FLAGS = 1
NMCII_FOLDERS: win32more.Windows.Win32.UI.Shell._NMCII_FLAGS = 2
_NMCSAEI_FLAGS = Int32
NMCSAEI_SELECT: win32more.Windows.Win32.UI.Shell._NMCSAEI_FLAGS = 0
NMCSAEI_EDIT: win32more.Windows.Win32.UI.Shell._NMCSAEI_FLAGS = 1
_NSTCECLICKTYPE = Int32
NSTCECT_LBUTTON: win32more.Windows.Win32.UI.Shell._NSTCECLICKTYPE = 1
NSTCECT_MBUTTON: win32more.Windows.Win32.UI.Shell._NSTCECLICKTYPE = 2
NSTCECT_RBUTTON: win32more.Windows.Win32.UI.Shell._NSTCECLICKTYPE = 3
NSTCECT_BUTTON: win32more.Windows.Win32.UI.Shell._NSTCECLICKTYPE = 3
NSTCECT_DBLCLICK: win32more.Windows.Win32.UI.Shell._NSTCECLICKTYPE = 4
_NSTCEHITTEST = Int32
NSTCEHT_NOWHERE: win32more.Windows.Win32.UI.Shell._NSTCEHITTEST = 1
NSTCEHT_ONITEMICON: win32more.Windows.Win32.UI.Shell._NSTCEHITTEST = 2
NSTCEHT_ONITEMLABEL: win32more.Windows.Win32.UI.Shell._NSTCEHITTEST = 4
NSTCEHT_ONITEMINDENT: win32more.Windows.Win32.UI.Shell._NSTCEHITTEST = 8
NSTCEHT_ONITEMBUTTON: win32more.Windows.Win32.UI.Shell._NSTCEHITTEST = 16
NSTCEHT_ONITEMRIGHT: win32more.Windows.Win32.UI.Shell._NSTCEHITTEST = 32
NSTCEHT_ONITEMSTATEICON: win32more.Windows.Win32.UI.Shell._NSTCEHITTEST = 64
NSTCEHT_ONITEM: win32more.Windows.Win32.UI.Shell._NSTCEHITTEST = 70
NSTCEHT_ONITEMTABBUTTON: win32more.Windows.Win32.UI.Shell._NSTCEHITTEST = 4096
_NSTCITEMSTATE = Int32
NSTCIS_NONE: win32more.Windows.Win32.UI.Shell._NSTCITEMSTATE = 0
NSTCIS_SELECTED: win32more.Windows.Win32.UI.Shell._NSTCITEMSTATE = 1
NSTCIS_EXPANDED: win32more.Windows.Win32.UI.Shell._NSTCITEMSTATE = 2
NSTCIS_BOLD: win32more.Windows.Win32.UI.Shell._NSTCITEMSTATE = 4
NSTCIS_DISABLED: win32more.Windows.Win32.UI.Shell._NSTCITEMSTATE = 8
NSTCIS_SELECTEDNOEXPAND: win32more.Windows.Win32.UI.Shell._NSTCITEMSTATE = 16
_NSTCROOTSTYLE = Int32
NSTCRS_VISIBLE: win32more.Windows.Win32.UI.Shell._NSTCROOTSTYLE = 0
NSTCRS_HIDDEN: win32more.Windows.Win32.UI.Shell._NSTCROOTSTYLE = 1
NSTCRS_EXPANDED: win32more.Windows.Win32.UI.Shell._NSTCROOTSTYLE = 2
_NSTCSTYLE = Int32
NSTCS_HASEXPANDOS: win32more.Windows.Win32.UI.Shell._NSTCSTYLE = 1
NSTCS_HASLINES: win32more.Windows.Win32.UI.Shell._NSTCSTYLE = 2
NSTCS_SINGLECLICKEXPAND: win32more.Windows.Win32.UI.Shell._NSTCSTYLE = 4
NSTCS_FULLROWSELECT: win32more.Windows.Win32.UI.Shell._NSTCSTYLE = 8
NSTCS_SPRINGEXPAND: win32more.Windows.Win32.UI.Shell._NSTCSTYLE = 16
NSTCS_HORIZONTALSCROLL: win32more.Windows.Win32.UI.Shell._NSTCSTYLE = 32
NSTCS_ROOTHASEXPANDO: win32more.Windows.Win32.UI.Shell._NSTCSTYLE = 64
NSTCS_SHOWSELECTIONALWAYS: win32more.Windows.Win32.UI.Shell._NSTCSTYLE = 128
NSTCS_NOINFOTIP: win32more.Windows.Win32.UI.Shell._NSTCSTYLE = 512
NSTCS_EVENHEIGHT: win32more.Windows.Win32.UI.Shell._NSTCSTYLE = 1024
NSTCS_NOREPLACEOPEN: win32more.Windows.Win32.UI.Shell._NSTCSTYLE = 2048
NSTCS_DISABLEDRAGDROP: win32more.Windows.Win32.UI.Shell._NSTCSTYLE = 4096
NSTCS_NOORDERSTREAM: win32more.Windows.Win32.UI.Shell._NSTCSTYLE = 8192
NSTCS_RICHTOOLTIP: win32more.Windows.Win32.UI.Shell._NSTCSTYLE = 16384
NSTCS_BORDER: win32more.Windows.Win32.UI.Shell._NSTCSTYLE = 32768
NSTCS_NOEDITLABELS: win32more.Windows.Win32.UI.Shell._NSTCSTYLE = 65536
NSTCS_TABSTOP: win32more.Windows.Win32.UI.Shell._NSTCSTYLE = 131072
NSTCS_FAVORITESMODE: win32more.Windows.Win32.UI.Shell._NSTCSTYLE = 524288
NSTCS_AUTOHSCROLL: win32more.Windows.Win32.UI.Shell._NSTCSTYLE = 1048576
NSTCS_FADEINOUTEXPANDOS: win32more.Windows.Win32.UI.Shell._NSTCSTYLE = 2097152
NSTCS_EMPTYTEXT: win32more.Windows.Win32.UI.Shell._NSTCSTYLE = 4194304
NSTCS_CHECKBOXES: win32more.Windows.Win32.UI.Shell._NSTCSTYLE = 8388608
NSTCS_PARTIALCHECKBOXES: win32more.Windows.Win32.UI.Shell._NSTCSTYLE = 16777216
NSTCS_EXCLUSIONCHECKBOXES: win32more.Windows.Win32.UI.Shell._NSTCSTYLE = 33554432
NSTCS_DIMMEDCHECKBOXES: win32more.Windows.Win32.UI.Shell._NSTCSTYLE = 67108864
NSTCS_NOINDENTCHECKS: win32more.Windows.Win32.UI.Shell._NSTCSTYLE = 134217728
NSTCS_ALLOWJUNCTIONS: win32more.Windows.Win32.UI.Shell._NSTCSTYLE = 268435456
NSTCS_SHOWTABSBUTTON: win32more.Windows.Win32.UI.Shell._NSTCSTYLE = 536870912
NSTCS_SHOWDELETEBUTTON: win32more.Windows.Win32.UI.Shell._NSTCSTYLE = 1073741824
NSTCS_SHOWREFRESHBUTTON: win32more.Windows.Win32.UI.Shell._NSTCSTYLE = -2147483648
_OPPROGDLGF = Int32
OPPROGDLG_DEFAULT: win32more.Windows.Win32.UI.Shell._OPPROGDLGF = 0
OPPROGDLG_ENABLEPAUSE: win32more.Windows.Win32.UI.Shell._OPPROGDLGF = 128
OPPROGDLG_ALLOWUNDO: win32more.Windows.Win32.UI.Shell._OPPROGDLGF = 256
OPPROGDLG_DONTDISPLAYSOURCEPATH: win32more.Windows.Win32.UI.Shell._OPPROGDLGF = 512
OPPROGDLG_DONTDISPLAYDESTPATH: win32more.Windows.Win32.UI.Shell._OPPROGDLGF = 1024
OPPROGDLG_NOMULTIDAYESTIMATES: win32more.Windows.Win32.UI.Shell._OPPROGDLGF = 2048
OPPROGDLG_DONTDISPLAYLOCATIONS: win32more.Windows.Win32.UI.Shell._OPPROGDLGF = 4096
_PDMODE = Int32
PDM_DEFAULT: win32more.Windows.Win32.UI.Shell._PDMODE = 0
PDM_RUN: win32more.Windows.Win32.UI.Shell._PDMODE = 1
PDM_PREFLIGHT: win32more.Windows.Win32.UI.Shell._PDMODE = 2
PDM_UNDOING: win32more.Windows.Win32.UI.Shell._PDMODE = 4
PDM_ERRORSBLOCKING: win32more.Windows.Win32.UI.Shell._PDMODE = 8
PDM_INDETERMINATE: win32more.Windows.Win32.UI.Shell._PDMODE = 16
_SHCONTF = Int32
SHCONTF_CHECKING_FOR_CHILDREN: win32more.Windows.Win32.UI.Shell._SHCONTF = 16
SHCONTF_FOLDERS: win32more.Windows.Win32.UI.Shell._SHCONTF = 32
SHCONTF_NONFOLDERS: win32more.Windows.Win32.UI.Shell._SHCONTF = 64
SHCONTF_INCLUDEHIDDEN: win32more.Windows.Win32.UI.Shell._SHCONTF = 128
SHCONTF_INIT_ON_FIRST_NEXT: win32more.Windows.Win32.UI.Shell._SHCONTF = 256
SHCONTF_NETPRINTERSRCH: win32more.Windows.Win32.UI.Shell._SHCONTF = 512
SHCONTF_SHAREABLE: win32more.Windows.Win32.UI.Shell._SHCONTF = 1024
SHCONTF_STORAGE: win32more.Windows.Win32.UI.Shell._SHCONTF = 2048
SHCONTF_NAVIGATION_ENUM: win32more.Windows.Win32.UI.Shell._SHCONTF = 4096
SHCONTF_FASTITEMS: win32more.Windows.Win32.UI.Shell._SHCONTF = 8192
SHCONTF_FLATLIST: win32more.Windows.Win32.UI.Shell._SHCONTF = 16384
SHCONTF_ENABLE_ASYNC: win32more.Windows.Win32.UI.Shell._SHCONTF = 32768
SHCONTF_INCLUDESUPERHIDDEN: win32more.Windows.Win32.UI.Shell._SHCONTF = 65536
_SICHINTF = Int32
SICHINT_DISPLAY: win32more.Windows.Win32.UI.Shell._SICHINTF = 0
SICHINT_ALLFIELDS: win32more.Windows.Win32.UI.Shell._SICHINTF = -2147483648
SICHINT_CANONICAL: win32more.Windows.Win32.UI.Shell._SICHINTF = 268435456
SICHINT_TEST_FILESYSPATH_IF_NOT_EQUAL: win32more.Windows.Win32.UI.Shell._SICHINTF = 536870912
_SPBEGINF = Int32
SPBEGINF_NORMAL: win32more.Windows.Win32.UI.Shell._SPBEGINF = 0
SPBEGINF_AUTOTIME: win32more.Windows.Win32.UI.Shell._SPBEGINF = 2
SPBEGINF_NOPROGRESSBAR: win32more.Windows.Win32.UI.Shell._SPBEGINF = 16
SPBEGINF_MARQUEEPROGRESS: win32more.Windows.Win32.UI.Shell._SPBEGINF = 32
SPBEGINF_NOCANCELBUTTON: win32more.Windows.Win32.UI.Shell._SPBEGINF = 64
_SPINITF = Int32
SPINITF_NORMAL: win32more.Windows.Win32.UI.Shell._SPINITF = 0
SPINITF_MODAL: win32more.Windows.Win32.UI.Shell._SPINITF = 1
SPINITF_NOMINIMIZE: win32more.Windows.Win32.UI.Shell._SPINITF = 8
_SV3CVW3_FLAGS = Int32
SV3CVW3_DEFAULT: win32more.Windows.Win32.UI.Shell._SV3CVW3_FLAGS = 0
SV3CVW3_NONINTERACTIVE: win32more.Windows.Win32.UI.Shell._SV3CVW3_FLAGS = 1
SV3CVW3_FORCEVIEWMODE: win32more.Windows.Win32.UI.Shell._SV3CVW3_FLAGS = 2
SV3CVW3_FORCEFOLDERFLAGS: win32more.Windows.Win32.UI.Shell._SV3CVW3_FLAGS = 4
_SVGIO = Int32
SVGIO_BACKGROUND: win32more.Windows.Win32.UI.Shell._SVGIO = 0
SVGIO_SELECTION: win32more.Windows.Win32.UI.Shell._SVGIO = 1
SVGIO_ALLVIEW: win32more.Windows.Win32.UI.Shell._SVGIO = 2
SVGIO_CHECKED: win32more.Windows.Win32.UI.Shell._SVGIO = 3
SVGIO_TYPE_MASK: win32more.Windows.Win32.UI.Shell._SVGIO = 15
SVGIO_FLAG_VIEWORDER: win32more.Windows.Win32.UI.Shell._SVGIO = -2147483648
_SVSIF = Int32
SVSI_DESELECT: win32more.Windows.Win32.UI.Shell._SVSIF = 0
SVSI_SELECT: win32more.Windows.Win32.UI.Shell._SVSIF = 1
SVSI_EDIT: win32more.Windows.Win32.UI.Shell._SVSIF = 3
SVSI_DESELECTOTHERS: win32more.Windows.Win32.UI.Shell._SVSIF = 4
SVSI_ENSUREVISIBLE: win32more.Windows.Win32.UI.Shell._SVSIF = 8
SVSI_FOCUSED: win32more.Windows.Win32.UI.Shell._SVSIF = 16
SVSI_TRANSLATEPT: win32more.Windows.Win32.UI.Shell._SVSIF = 32
SVSI_SELECTIONMARK: win32more.Windows.Win32.UI.Shell._SVSIF = 64
SVSI_POSITIONITEM: win32more.Windows.Win32.UI.Shell._SVSIF = 128
SVSI_CHECK: win32more.Windows.Win32.UI.Shell._SVSIF = 256
SVSI_CHECK2: win32more.Windows.Win32.UI.Shell._SVSIF = 512
SVSI_KEYBOARDSELECT: win32more.Windows.Win32.UI.Shell._SVSIF = 1025
SVSI_NOTAKEFOCUS: win32more.Windows.Win32.UI.Shell._SVSIF = 1073741824
_TRANSFER_ADVISE_STATE = Int32
TS_NONE: win32more.Windows.Win32.UI.Shell._TRANSFER_ADVISE_STATE = 0
TS_PERFORMING: win32more.Windows.Win32.UI.Shell._TRANSFER_ADVISE_STATE = 1
TS_PREPARING: win32more.Windows.Win32.UI.Shell._TRANSFER_ADVISE_STATE = 2
TS_INDETERMINATE: win32more.Windows.Win32.UI.Shell._TRANSFER_ADVISE_STATE = 4
_TRANSFER_SOURCE_FLAGS = Int32
TSF_NORMAL: win32more.Windows.Win32.UI.Shell._TRANSFER_SOURCE_FLAGS = 0
TSF_FAIL_EXIST: win32more.Windows.Win32.UI.Shell._TRANSFER_SOURCE_FLAGS = 0
TSF_RENAME_EXIST: win32more.Windows.Win32.UI.Shell._TRANSFER_SOURCE_FLAGS = 1
TSF_OVERWRITE_EXIST: win32more.Windows.Win32.UI.Shell._TRANSFER_SOURCE_FLAGS = 2
TSF_ALLOW_DECRYPTION: win32more.Windows.Win32.UI.Shell._TRANSFER_SOURCE_FLAGS = 4
TSF_NO_SECURITY: win32more.Windows.Win32.UI.Shell._TRANSFER_SOURCE_FLAGS = 8
TSF_COPY_CREATION_TIME: win32more.Windows.Win32.UI.Shell._TRANSFER_SOURCE_FLAGS = 16
TSF_COPY_WRITE_TIME: win32more.Windows.Win32.UI.Shell._TRANSFER_SOURCE_FLAGS = 32
TSF_USE_FULL_ACCESS: win32more.Windows.Win32.UI.Shell._TRANSFER_SOURCE_FLAGS = 64
TSF_DELETE_RECYCLE_IF_POSSIBLE: win32more.Windows.Win32.UI.Shell._TRANSFER_SOURCE_FLAGS = 128
TSF_COPY_HARD_LINK: win32more.Windows.Win32.UI.Shell._TRANSFER_SOURCE_FLAGS = 256
TSF_COPY_LOCALIZED_NAME: win32more.Windows.Win32.UI.Shell._TRANSFER_SOURCE_FLAGS = 512
TSF_MOVE_AS_COPY_DELETE: win32more.Windows.Win32.UI.Shell._TRANSFER_SOURCE_FLAGS = 1024
TSF_SUSPEND_SHELLEVENTS: win32more.Windows.Win32.UI.Shell._TRANSFER_SOURCE_FLAGS = 2048


make_ready(__name__)
