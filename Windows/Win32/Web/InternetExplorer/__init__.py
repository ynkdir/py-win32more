from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Graphics.DirectDraw
import Windows.Win32.Graphics.Dxgi.Common
import Windows.Win32.Graphics.Gdi
import Windows.Win32.Security
import Windows.Win32.Storage.FileSystem
import Windows.Win32.System.Com
import Windows.Win32.System.Ole
import Windows.Win32.System.Registry
import Windows.Win32.System.Threading
import Windows.Win32.System.WinRT
import Windows.Win32.UI.WindowsAndMessaging
import Windows.Win32.Web.InternetExplorer
import Windows.Win32.Web.MsHtml
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
ADDURL_FLAG = Int32
ADDURL_FIRST: ADDURL_FLAG = 0
ADDURL_ADDTOHISTORYANDCACHE: ADDURL_FLAG = 0
ADDURL_ADDTOCACHE: ADDURL_FLAG = 1
ADDURL_Max: ADDURL_FLAG = 2147483647
AnchorClick = Guid('13d5413c-33b9-11d2-95-a7-00-c0-4f-8e-cb-02')
DISPID_AMBIENT_OFFLINEIFNOTCONNECTED: Int32 = -5501
DISPID_AMBIENT_SILENT: Int32 = -5502
DISPID_BEFORENAVIGATE: UInt32 = 100
DISPID_NAVIGATECOMPLETE: UInt32 = 101
DISPID_STATUSTEXTCHANGE: UInt32 = 102
DISPID_QUIT: UInt32 = 103
DISPID_DOWNLOADCOMPLETE: UInt32 = 104
DISPID_COMMANDSTATECHANGE: UInt32 = 105
DISPID_DOWNLOADBEGIN: UInt32 = 106
DISPID_NEWWINDOW: UInt32 = 107
DISPID_PROGRESSCHANGE: UInt32 = 108
DISPID_WINDOWMOVE: UInt32 = 109
DISPID_WINDOWRESIZE: UInt32 = 110
DISPID_WINDOWACTIVATE: UInt32 = 111
DISPID_PROPERTYCHANGE: UInt32 = 112
DISPID_TITLECHANGE: UInt32 = 113
DISPID_TITLEICONCHANGE: UInt32 = 114
DISPID_FRAMEBEFORENAVIGATE: UInt32 = 200
DISPID_FRAMENAVIGATECOMPLETE: UInt32 = 201
DISPID_FRAMENEWWINDOW: UInt32 = 204
DISPID_BEFORENAVIGATE2: UInt32 = 250
DISPID_NEWWINDOW2: UInt32 = 251
DISPID_NAVIGATECOMPLETE2: UInt32 = 252
DISPID_ONQUIT: UInt32 = 253
DISPID_ONVISIBLE: UInt32 = 254
DISPID_ONTOOLBAR: UInt32 = 255
DISPID_ONMENUBAR: UInt32 = 256
DISPID_ONSTATUSBAR: UInt32 = 257
DISPID_ONFULLSCREEN: UInt32 = 258
DISPID_DOCUMENTCOMPLETE: UInt32 = 259
DISPID_ONTHEATERMODE: UInt32 = 260
DISPID_ONADDRESSBAR: UInt32 = 261
DISPID_WINDOWSETRESIZABLE: UInt32 = 262
DISPID_WINDOWCLOSING: UInt32 = 263
DISPID_WINDOWSETLEFT: UInt32 = 264
DISPID_WINDOWSETTOP: UInt32 = 265
DISPID_WINDOWSETWIDTH: UInt32 = 266
DISPID_WINDOWSETHEIGHT: UInt32 = 267
DISPID_CLIENTTOHOSTWINDOW: UInt32 = 268
DISPID_SETSECURELOCKICON: UInt32 = 269
DISPID_FILEDOWNLOAD: UInt32 = 270
DISPID_NAVIGATEERROR: UInt32 = 271
DISPID_PRIVACYIMPACTEDSTATECHANGE: UInt32 = 272
DISPID_NEWWINDOW3: UInt32 = 273
DISPID_VIEWUPDATE: UInt32 = 281
DISPID_SETPHISHINGFILTERSTATUS: UInt32 = 282
DISPID_WINDOWSTATECHANGED: UInt32 = 283
DISPID_NEWPROCESS: UInt32 = 284
DISPID_THIRDPARTYURLBLOCKED: UInt32 = 285
DISPID_REDIRECTXDOMAINBLOCKED: UInt32 = 286
DISPID_WEBWORKERSTARTED: UInt32 = 288
DISPID_WEBWORKERFINISHED: UInt32 = 289
DISPID_BEFORESCRIPTEXECUTE: UInt32 = 290
DISPID_PRINTTEMPLATEINSTANTIATION: UInt32 = 225
DISPID_PRINTTEMPLATETEARDOWN: UInt32 = 226
DISPID_UPDATEPAGESTATUS: UInt32 = 227
DISPID_WINDOWREGISTERED: UInt32 = 200
DISPID_WINDOWREVOKED: UInt32 = 201
DISPID_RESETFIRSTBOOTMODE: UInt32 = 1
DISPID_RESETSAFEMODE: UInt32 = 2
DISPID_REFRESHOFFLINEDESKTOP: UInt32 = 3
DISPID_ADDFAVORITE: UInt32 = 4
DISPID_ADDCHANNEL: UInt32 = 5
DISPID_ADDDESKTOPCOMPONENT: UInt32 = 6
DISPID_ISSUBSCRIBED: UInt32 = 7
DISPID_NAVIGATEANDFIND: UInt32 = 8
DISPID_IMPORTEXPORTFAVORITES: UInt32 = 9
DISPID_AUTOCOMPLETESAVEFORM: UInt32 = 10
DISPID_AUTOSCAN: UInt32 = 11
DISPID_AUTOCOMPLETEATTACH: UInt32 = 12
DISPID_SHOWBROWSERUI: UInt32 = 13
DISPID_ADDSEARCHPROVIDER: UInt32 = 14
DISPID_RUNONCESHOWN: UInt32 = 15
DISPID_SKIPRUNONCE: UInt32 = 16
DISPID_CUSTOMIZESETTINGS: UInt32 = 17
DISPID_SQMENABLED: UInt32 = 18
DISPID_PHISHINGENABLED: UInt32 = 19
DISPID_BRANDIMAGEURI: UInt32 = 20
DISPID_SKIPTABSWELCOME: UInt32 = 21
DISPID_DIAGNOSECONNECTION: UInt32 = 22
DISPID_CUSTOMIZECLEARTYPE: UInt32 = 23
DISPID_ISSEARCHPROVIDERINSTALLED: UInt32 = 24
DISPID_ISSEARCHMIGRATED: UInt32 = 25
DISPID_DEFAULTSEARCHPROVIDER: UInt32 = 26
DISPID_RUNONCEREQUIREDSETTINGSCOMPLETE: UInt32 = 27
DISPID_RUNONCEHASSHOWN: UInt32 = 28
DISPID_SEARCHGUIDEURL: UInt32 = 29
DISPID_ADDSERVICE: UInt32 = 30
DISPID_ISSERVICEINSTALLED: UInt32 = 31
DISPID_ADDTOFAVORITESBAR: UInt32 = 32
DISPID_BUILDNEWTABPAGE: UInt32 = 33
DISPID_SETRECENTLYCLOSEDVISIBLE: UInt32 = 34
DISPID_SETACTIVITIESVISIBLE: UInt32 = 35
DISPID_CONTENTDISCOVERYRESET: UInt32 = 36
DISPID_INPRIVATEFILTERINGENABLED: UInt32 = 37
DISPID_SUGGESTEDSITESENABLED: UInt32 = 38
DISPID_ENABLESUGGESTEDSITES: UInt32 = 39
DISPID_NAVIGATETOSUGGESTEDSITES: UInt32 = 40
DISPID_SHOWTABSHELP: UInt32 = 41
DISPID_SHOWINPRIVATEHELP: UInt32 = 42
DISPID_ISSITEMODE: UInt32 = 43
DISPID_SETSITEMODEICONOVERLAY: UInt32 = 44
DISPID_CLEARSITEMODEICONOVERLAY: UInt32 = 45
DISPID_UPDATETHUMBNAILBUTTON: UInt32 = 46
DISPID_SETTHUMBNAILBUTTONS: UInt32 = 47
DISPID_ADDTHUMBNAILBUTTONS: UInt32 = 48
DISPID_ADDSITEMODE: UInt32 = 49
DISPID_SETSITEMODEPROPERTIES: UInt32 = 50
DISPID_SITEMODECREATEJUMPLIST: UInt32 = 51
DISPID_SITEMODEADDJUMPLISTITEM: UInt32 = 52
DISPID_SITEMODECLEARJUMPLIST: UInt32 = 53
DISPID_SITEMODEADDBUTTONSTYLE: UInt32 = 54
DISPID_SITEMODESHOWBUTTONSTYLE: UInt32 = 55
DISPID_SITEMODESHOWJUMPLIST: UInt32 = 56
DISPID_ADDTRACKINGPROTECTIONLIST: UInt32 = 57
DISPID_SITEMODEACTIVATE: UInt32 = 58
DISPID_ISSITEMODEFIRSTRUN: UInt32 = 59
DISPID_TRACKINGPROTECTIONENABLED: UInt32 = 60
DISPID_ACTIVEXFILTERINGENABLED: UInt32 = 61
DISPID_PROVISIONNETWORKS: UInt32 = 62
DISPID_REPORTSAFEURL: UInt32 = 63
DISPID_SITEMODEREFRESHBADGE: UInt32 = 64
DISPID_SITEMODECLEARBADGE: UInt32 = 65
DISPID_DIAGNOSECONNECTIONUILESS: UInt32 = 66
DISPID_LAUNCHNETWORKCLIENTHELP: UInt32 = 67
DISPID_CHANGEDEFAULTBROWSER: UInt32 = 68
DISPID_STOPPERIODICUPDATE: UInt32 = 69
DISPID_STARTPERIODICUPDATE: UInt32 = 70
DISPID_CLEARNOTIFICATION: UInt32 = 71
DISPID_ENABLENOTIFICATIONQUEUE: UInt32 = 72
DISPID_PINNEDSITESTATE: UInt32 = 73
DISPID_LAUNCHINTERNETOPTIONS: UInt32 = 74
DISPID_STARTPERIODICUPDATEBATCH: UInt32 = 75
DISPID_ENABLENOTIFICATIONQUEUESQUARE: UInt32 = 76
DISPID_ENABLENOTIFICATIONQUEUEWIDE: UInt32 = 77
DISPID_ENABLENOTIFICATIONQUEUELARGE: UInt32 = 78
DISPID_SCHEDULEDTILENOTIFICATION: UInt32 = 79
DISPID_REMOVESCHEDULEDTILENOTIFICATION: UInt32 = 80
DISPID_STARTBADGEUPDATE: UInt32 = 81
DISPID_STOPBADGEUPDATE: UInt32 = 82
DISPID_ISMETAREFERRERAVAILABLE: UInt32 = 83
DISPID_SETEXPERIMENTALFLAG: UInt32 = 84
DISPID_GETEXPERIMENTALFLAG: UInt32 = 85
DISPID_SETEXPERIMENTALVALUE: UInt32 = 86
DISPID_GETEXPERIMENTALVALUE: UInt32 = 87
DISPID_HASNEEDIEAUTOLAUNCHFLAG: UInt32 = 88
DISPID_GETNEEDIEAUTOLAUNCHFLAG: UInt32 = 89
DISPID_SETNEEDIEAUTOLAUNCHFLAG: UInt32 = 90
DISPID_LAUNCHIE: UInt32 = 91
DISPID_RESETEXPERIMENTALFLAGS: UInt32 = 92
DISPID_GETCVLISTDATA: UInt32 = 93
DISPID_GETCVLISTLOCALDATA: UInt32 = 94
DISPID_GETEMIELISTDATA: UInt32 = 95
DISPID_GETEMIELISTLOCALDATA: UInt32 = 96
DISPID_OPENFAVORITESPANE: UInt32 = 97
DISPID_OPENFAVORITESSETTINGS: UInt32 = 98
DISPID_LAUNCHINHVSI: UInt32 = 99
DISPID_GETNEEDHVSIAUTOLAUNCHFLAG: UInt32 = 100
DISPID_SETNEEDHVSIAUTOLAUNCHFLAG: UInt32 = 101
DISPID_HASNEEDHVSIAUTOLAUNCHFLAG: UInt32 = 102
DISPID_GETOSSKU: UInt32 = 103
DISPID_SETMSDEFAULTS: UInt32 = 104
DISPID_SHELLUIHELPERLAST: UInt32 = 105
DISPID_ADVANCEERROR: UInt32 = 10
DISPID_RETREATERROR: UInt32 = 11
DISPID_CANADVANCEERROR: UInt32 = 12
DISPID_CANRETREATERROR: UInt32 = 13
DISPID_GETERRORLINE: UInt32 = 14
DISPID_GETERRORCHAR: UInt32 = 15
DISPID_GETERRORCODE: UInt32 = 16
DISPID_GETERRORMSG: UInt32 = 17
DISPID_GETERRORURL: UInt32 = 18
DISPID_GETDETAILSSTATE: UInt32 = 19
DISPID_SETDETAILSSTATE: UInt32 = 20
DISPID_GETPERERRSTATE: UInt32 = 21
DISPID_SETPERERRSTATE: UInt32 = 22
DISPID_GETALWAYSSHOWLOCKSTATE: UInt32 = 23
DISPID_FAVSELECTIONCHANGE: UInt32 = 1
DISPID_SELECTIONCHANGE: UInt32 = 2
DISPID_DOUBLECLICK: UInt32 = 3
DISPID_INITIALIZED: UInt32 = 4
DISPID_MOVESELECTIONUP: UInt32 = 1
DISPID_MOVESELECTIONDOWN: UInt32 = 2
DISPID_RESETSORT: UInt32 = 3
DISPID_NEWFOLDER: UInt32 = 4
DISPID_SYNCHRONIZE: UInt32 = 5
DISPID_IMPORT: UInt32 = 6
DISPID_EXPORT: UInt32 = 7
DISPID_INVOKECONTEXTMENU: UInt32 = 8
DISPID_MOVESELECTIONTO: UInt32 = 9
DISPID_SUBSCRIPTIONSENABLED: UInt32 = 10
DISPID_CREATESUBSCRIPTION: UInt32 = 11
DISPID_DELETESUBSCRIPTION: UInt32 = 12
DISPID_SETROOT: UInt32 = 13
DISPID_ENUMOPTIONS: UInt32 = 14
DISPID_SELECTEDITEM: UInt32 = 15
DISPID_ROOT: UInt32 = 16
DISPID_DEPTH: UInt32 = 17
DISPID_MODE: UInt32 = 18
DISPID_FLAGS: UInt32 = 19
DISPID_TVFLAGS: UInt32 = 20
DISPID_NSCOLUMNS: UInt32 = 21
DISPID_COUNTVIEWTYPES: UInt32 = 22
DISPID_SETVIEWTYPE: UInt32 = 23
DISPID_SELECTEDITEMS: UInt32 = 24
DISPID_EXPAND: UInt32 = 25
DISPID_UNSELECTALL: UInt32 = 26
TF_NAVIGATE: UInt32 = 2142153644
TARGET_NOTIFY_OBJECT_NAME: String = '863a99a0-21bc-11d0-82b4-00a0c90c29c5'
IEPROCESS_MODULE_NAME: String = 'IERtUtil.dll'
IEGetProcessModule_PROC_NAME: String = 'IEGetProcessModule'
IEGetTabWindowExports_PROC_NAME: String = 'IEGetTabWindowExports'
TSZMICROSOFTPATH: String = 'Software\\Microsoft'
SZ_IE_MAIN: String = 'Main'
REGSTR_VAL_SMOOTHSCROLL: String = 'SmoothScroll'
REGSTR_VAL_SMOOTHSCROLL_DEF: UInt32 = 1
REGSTR_VAL_SHOWTOOLBAR: String = 'Show_ToolBar'
REGSTR_VAL_SHOWADDRESSBAR: String = 'Show_URLToolBar'
REGSTR_VAL_STARTPAGE: String = 'Start Page'
REGSTRA_VAL_STARTPAGE: String = 'Start Page'
REGSTR_VAL_SEARCHPAGE: String = 'Search Page'
REGSTR_VAL_LOCALPAGE: String = 'Local Page'
REGSTR_VAL_USESTYLESHEETS: String = 'Use Stylesheets'
REGSTR_VAL_USESTYLESHEETS_DEF: String = 'yes'
REGSTR_VAL_USEICM: String = 'UseICM'
REGSTR_VAL_USEICM_DEF: UInt32 = 0
REGSTR_VAL_SHOWFOCUS: String = 'Tabstop - MouseDown'
REGSTR_VAL_SHOWFOCUS_DEF: String = 'no'
REGSTR_VAL_LOADIMAGES: String = 'Display Inline Images'
REGSTR_VAL_PLAYSOUNDS: String = 'Play_Background_Sounds'
REGSTR_VAL_PLAYVIDEOS: String = 'Display Inline Videos'
REGSTR_VAL_ANCHORUNDERLINE: String = 'Anchor Underline'
REGSTR_VAL_USEDLGCOLORS: String = 'Use_DlgBox_Colors'
REGSTR_VAL_CHECKASSOC: String = 'Check_Associations'
REGSTR_VAL_SHOWFULLURLS: String = 'Show_FullURL'
REGSTR_VAL_AUTOSEARCH: String = 'Do404Search'
REGSTR_VAL_AUTONAVIGATE: String = 'SearchForExtensions'
REGSTR_VAL_HTTP_ERRORS: String = 'Friendly http errors'
REGSTR_VAL_USEIBAR: String = 'UseBar'
SZ_IE_SETTINGS: String = 'Settings'
REGSTR_VAL_IE_CUSTOMCOLORS: String = 'Custom Colors'
REGSTR_VAL_ANCHORCOLOR: String = 'Anchor Color'
REGSTR_VAL_ANCHORCOLORVISITED: String = 'Anchor Color Visited'
REGSTR_VAL_BACKGROUNDCOLOR: String = 'Background Color'
REGSTR_VAL_TEXTCOLOR: String = 'Text Color'
REGSTR_VAL_ANCHORCOLORHOVER: String = 'Anchor Color Hover'
REGSTR_VAL_USEHOVERCOLOR: String = 'Use Anchor Hover Color'
SZ_IE_SECURITY: String = 'Security'
REGSTR_VAL_SAFETYWARNINGLEVEL: String = 'Safety Warning Level'
SZ_IE_DEFAULT_HTML_EDITOR: String = 'Default HTML Editor'
REGSTR_VAL_USEAUTOAPPEND: String = 'Append Completion'
REGSTR_VAL_USEAUTOSUGGEST: String = 'AutoSuggest'
REGSTR_VAL_USEAUTOCOMPLETE: String = 'Use AutoComplete'
SZ_IE_IBAR: String = 'Bar'
SZ_IE_IBAR_BANDS: String = 'Bands'
REGSTR_VAL_USERAGENT: String = 'User Agent'
REGSTR_VAL_INTERNETENTRY: String = 'InternetProfile'
REGSTR_VAL_INTERNETPROFILE: String = 'InternetProfile'
REGSTR_VAL_INTERNETENTRYBKUP: String = 'BackupInternetProfile'
REGSTR_VAL_CODEDOWNLOAD: String = 'Code Download'
REGSTR_VAL_CODEDOWNLOAD_DEF: String = 'yes'
REGSTR_PATH_INETCPL_RESTRICTIONS: String = 'Software\\Policies\\Microsoft\\Internet Explorer\\Control Panel'
REGSTR_VAL_INETCPL_GENERALTAB: String = 'GeneralTab'
REGSTR_VAL_INETCPL_SECURITYTAB: String = 'SecurityTab'
REGSTR_VAL_INETCPL_CONTENTTAB: String = 'ContentTab'
REGSTR_VAL_INETCPL_CONNECTIONSTAB: String = 'ConnectionsTab'
REGSTR_VAL_INETCPL_PROGRAMSTAB: String = 'ProgramsTab'
REGSTR_VAL_INETCPL_ADVANCEDTAB: String = 'AdvancedTab'
REGSTR_VAL_INETCPL_PRIVACYTAB: String = 'PrivacyTab'
REGSTR_VAL_INETCPL_IEAK: String = 'IEAKContext'
REGSTR_VAL_DIRECTORY: String = 'Directory'
REGSTR_VAL_NEWDIRECTORY: String = 'NewDirectory'
REGSTR_VAL_CACHEPREFIX: String = 'CachePrefix'
SZ_IE_SEARCHSTRINGS: String = 'UrlTemplate'
MAX_SEARCH_FORMAT_STRING: UInt32 = 255
SZ_IE_THRESHOLDS: String = 'ErrorThresholds'
REGSTR_VAL_ACCESSMEDIUM: String = 'AccessMedium'
REGSTR_VAL_ACCESSTYPE: String = 'AccessType'
REGSTR_VAL_AUTODIALDLLNAME: String = 'AutodialDllName'
REGSTR_VAL_AUTODIALFCNNAME: String = 'AutodialFcnName'
REGSTR_VAL_AUTODIAL_MONITORCLASSNAME: String = 'MS_AutodialMonitor'
REGSTR_VAL_AUTODIAL_TRYONLYONCE: String = 'TryAutodialOnce'
REGSTR_PATH_REMOTEACCESS: String = 'RemoteAccess'
REGSTR_PATH_REMOTEACESS: String = 'RemoteAccess'
REGSTR_VAL_RNAINSTALLED: String = 'Installed'
REGSTR_VAL_ENABLEAUTODIAL: String = 'EnableAutodial'
REGSTR_VAL_ENABLEUNATTENDED: String = 'EnableUnattended'
REGSTR_VAL_NONETAUTODIAL: String = 'NoNetAutodial'
REGSTR_VAL_REDIALATTEMPTS: String = 'RedialAttempts'
REGSTR_VAL_REDIALINTERVAL: String = 'RedialWait'
REGSTR_VAL_ENABLEAUTODIALDISCONNECT: String = 'EnableAutodisconnect'
REGSTR_VAL_ENABLEAUTODISCONNECT: String = 'EnableAutodisconnect'
REGSTR_VAL_ENABLEEXITDISCONNECT: String = 'EnableExitDisconnect'
REGSTR_VAL_ENABLESECURITYCHECK: String = 'EnableSecurityCheck'
REGSTR_VAL_COVEREXCLUDE: String = 'CoverExclude'
REGSTR_VAL_DISCONNECTIDLETIME: String = 'DisconnectIdleTime'
REGSTR_VAL_MOSDISCONNECT: String = 'DisconnectTimeout'
REGSTR_VAL_PROXYENABLE: String = 'ProxyEnable'
REGSTR_VAL_PROXYSERVER: String = 'ProxyServer'
REGSTR_VAL_PROXYOVERRIDE: String = 'ProxyOverride'
REGSTR_VAL_BYPASSAUTOCONFIG: String = 'BypassAutoconfig'
SZTRUSTWARNLEVEL: String = 'Trust Warning Level'
REGSTR_VAL_TRUSTWARNINGLEVEL_HIGH: String = 'High'
REGSTR_VAL_TRUSTWARNINGLEVEL_MED: String = 'Medium'
REGSTR_VAL_TRUSTWARNINGLEVEL_LOW: String = 'No Security'
REGSTR_VAL_SECURITYWARNONSEND: String = 'WarnOnPost'
REGSTR_VAL_SECURITYWARNONSEND_DEF: UInt32 = 1
REGSTR_VAL_SECURITYWARNONSENDALWAYS: String = 'WarnAlwaysOnPost'
REGSTR_VAL_SECURITYWARNONSENDALWAYS_DEF: UInt32 = 1
REGSTR_VAL_SECURITYWARNONVIEW: String = 'WarnOnView'
REGSTR_VAL_SECURITYWARNONVIEW_DEF: UInt32 = 1
REGSTR_VAL_SECURITYALLOWCOOKIES: String = 'AllowCookies'
REGSTR_VAL_SECURITYALLOWCOOKIES_DEF: UInt32 = 1
REGSTR_VAL_SECURITYWARNONZONECROSSING: String = 'WarnOnZoneCrossing'
REGSTR_VAL_SECURITYWARNONZONECROSSING_DEF: UInt32 = 1
REGSTR_VAL_SECURITYWARNONBADCERTVIEWING: String = 'WarnOnBadCertRecving'
REGSTR_VAL_SECURITYWARNONBADCERTVIEWING_DEF: UInt32 = 1
REGSTR_VAL_SECURITYWARNONBADCERTSENDING: String = 'WarnOnBadCertSending'
REGSTR_VAL_SECURITYWARNONBADCERTSENDING_DEF: UInt32 = 1
REGSTR_VAL_SECURITYDISABLECACHINGOFSSLPAGES: String = 'DisableCachingOfSSLPages'
REGSTR_VAL_SECURITYDISABLECACHINGOFSSLPAGES_DEF: UInt32 = 0
REGSTR_VAL_SECURITYACTIVEX: String = 'Security_RunActiveXControls'
REGSTR_VAL_SECURITYACTIVEX_DEF: UInt32 = 1
REGSTR_VAL_SECURITYACTICEXSCRIPTS: String = 'Security_RunScripts'
REGSTR_VAL_SECURITYACTICEXSCRIPTS_DEF: UInt32 = 1
REGSTR_VAL_SECURITYJAVA: String = 'Security_RunJavaApplets'
REGSTR_VAL_SECURITYJAVA_DEF: UInt32 = 1
SZJAVAVMPATH: String = '\\Java VM'
REGSTR_VAL_JAVAJIT: String = 'EnableJIT'
REGSTR_VAL_JAVAJIT_DEF: UInt32 = 0
REGSTR_VAL_JAVALOGGING: String = 'EnableLogging'
REGSTR_VAL_JAVALOGGING_DEF: UInt32 = 0
SZTOOLBAR: String = '\\Toolbar'
REGSTR_VAL_DAYSTOKEEP: String = 'DaysToKeep'
SZNOTEXT: String = 'NoText'
SZVISIBLE: String = 'VisibleBands'
REGSTR_VAL_VISIBLEBANDS: String = 'VisibleBands'
REGSTR_VAL_VISIBLEBANDS_DEF: UInt32 = 7
TOOLSBAND: UInt32 = 1
ADDRESSBAND: UInt32 = 2
LINKSBAND: UInt32 = 4
SZBACKBITMAP: String = 'BackBitmap'
REGSTR_VAL_BACKBITMAP: String = 'BackBitmap'
REGSTR_SHIFTQUICKSUFFIX: String = 'ShiftQuickCompleteSuffix'
TSZSCHANNELPATH: String = 'SYSTEM\\CurrentControlSet\\Control\\SecurityProviders\\SCHANNEL'
REGSTR_VAL_SCHANNELENABLEPROTOCOL: String = 'Enabled'
REGSTR_VAL_SCHANNELENABLEPROTOCOL_DEF: UInt32 = 1
TSZINTERNETCLIENTSPATH: String = 'Software\\Microsoft\\Internet Explorer\\Unix'
REGSTR_PATH_DEFAULT: String = 'default'
REGSTR_PATH_CURRENT: String = 'current'
IE_USE_OE_PRESENT_HKEY: Int32 = -2147483646
IE_USE_OE_PRESENT_KEY: String = 'Software\\Microsoft\\Windows\\CurrentVersion\\app.paths\\msimn.exe'
IE_USE_OE_MAIL_HKEY: Int32 = -2147483647
IE_USE_OE_MAIL_KEY: String = 'Software\\Microsoft\\Internet Explorer\\Mail'
IE_USE_OE_MAIL_VALUE: String = 'Use Outlook Express'
IE_USE_OE_NEWS_HKEY: Int32 = -2147483647
IE_USE_OE_NEWS_KEY: String = 'Software\\Microsoft\\Internet Explorer\\News'
IE_USE_OE_NEWS_VALUE: String = 'Use Outlook Express'
TSZPROTOCOLSPATH: String = 'Protocols\\'
TSZMAILTOPROTOCOL: String = 'mailto'
TSZNEWSPROTOCOL: String = 'news'
TSZCALLTOPROTOCOL: String = 'callto'
TSZLDAPPROTOCOL: String = 'ldap'
TSZCALENDARPROTOCOL: String = 'unk'
TSZVSOURCEPROTOCOL: String = 'view source'
REGSTR_VAL_DEFAULT_CODEPAGE: String = 'Default_CodePage'
REGSTR_VAL_DEFAULT_SCRIPT: String = 'Default_Script'
REGSTR_VAL_ACCEPT_LANGUAGE: String = 'AcceptLanguage'
REGSTR_VAL_FONT_SCRIPTS: String = 'Scripts'
REGSTR_VAL_FONT_SCRIPT: String = 'Script'
REGSTR_VAL_FONT_SCRIPT_NAME: String = 'Script'
REGSTR_VAL_DEF_ENCODING: String = 'Default_Encoding'
REGSTR_VAL_DEF_INETENCODING: String = 'Default_InternetEncoding'
REGSTR_VAL_FIXED_FONT: String = 'IEFixedFontName'
REGSTR_VAL_SCRIPT_FIXED_FONT: String = 'IEFixedFontName'
REGSTR_VAL_PROP_FONT: String = 'IEPropFontName'
REGSTR_VAL_SCRIPT_PROP_FONT: String = 'IEPropFontName'
REGSTR_VAL_FONT_SIZE: String = 'IEFontSize'
REGSTR_VAL_FONT_SIZE_DEF: UInt32 = 2
REGSTR_VAL_AUTODETECT: String = 'AutoDetect'
REGSTR_PATH_MIME_DATABASE: String = 'MIME\\Database'
REGSTR_VAL_CODEPAGE: String = 'CodePage'
REGSTR_VAL_INETENCODING: String = 'InternetEncoding'
REGSTR_VAL_FAMILY: String = 'Family'
REGSTR_VAL_LEVEL: String = 'Level'
REGSTR_VAL_ALIASTO: String = 'AliasForCharset'
REGSTR_VAL_ENCODENAME: String = 'EncodingName'
REGSTR_VAL_DESCRIPTION: String = 'Description'
REGSTR_VAL_WEBCHARSET: String = 'WebCharset'
REGSTR_VAL_BODYCHARSET: String = 'BodyCharset'
REGSTR_VAL_HEADERCHARSET: String = 'HeaderCharset'
REGSTR_VAL_FIXEDWIDTHFONT: String = 'FixedWidthFont'
REGSTR_VAL_PROPORTIONALFONT: String = 'ProportionalFont'
REGSTR_VAL_PRIVCONVERTER: String = 'PrivConverter'
IECMDID_CLEAR_AUTOCOMPLETE_FOR_FORMS: UInt32 = 0
IECMDID_SETID_AUTOCOMPLETE_FOR_FORMS: UInt32 = 1
IECMDID_BEFORENAVIGATE_GETSHELLBROWSE: UInt32 = 2
IECMDID_BEFORENAVIGATE_DOEXTERNALBROWSE: UInt32 = 3
IECMDID_BEFORENAVIGATE_GETIDLIST: UInt32 = 4
IECMDID_SET_INVOKE_DEFAULT_BROWSER_ON_NEW_WINDOW: UInt32 = 5
IECMDID_GET_INVOKE_DEFAULT_BROWSER_ON_NEW_WINDOW: UInt32 = 6
IECMDID_ARG_CLEAR_FORMS_ALL: UInt32 = 0
IECMDID_ARG_CLEAR_FORMS_ALL_BUT_PASSWORDS: UInt32 = 1
IECMDID_ARG_CLEAR_FORMS_PASSWORDS_ONLY: UInt32 = 2
CATID_MSOfficeAntiVirus: Guid = Guid('56ffcc30-d398-11d0-b2-ae-00-a0-c9-08-fa-49')
msoedmEnable: UInt32 = 1
msoedmDisable: UInt32 = 2
msoedmDontOpen: UInt32 = 3
msoslUndefined: UInt32 = 0
msoslNone: UInt32 = 1
msoslMedium: UInt32 = 2
msoslHigh: UInt32 = 3
msodsvNoMacros: UInt32 = 0
msodsvUnsigned: UInt32 = 1
msodsvPassedTrusted: UInt32 = 2
msodsvFailed: UInt32 = 3
msodsvLowSecurityLevel: UInt32 = 4
msodsvPassedTrustedCert: UInt32 = 5
STATURL_QUERYFLAG_ISCACHED: UInt32 = 65536
STATURL_QUERYFLAG_NOURL: UInt32 = 131072
STATURL_QUERYFLAG_NOTITLE: UInt32 = 262144
STATURL_QUERYFLAG_TOPLEVEL: UInt32 = 524288
STATURLFLAG_ISCACHED: UInt32 = 1
STATURLFLAG_ISTOPLEVEL: UInt32 = 2
SURFACE_LOCK_EXCLUSIVE: UInt32 = 1
SURFACE_LOCK_ALLOW_DISCARD: UInt32 = 2
SURFACE_LOCK_WAIT: UInt32 = 4
E_SURFACE_NOSURFACE: Int32 = -2147434496
E_SURFACE_UNKNOWN_FORMAT: Int32 = -2147434495
E_SURFACE_NOTMYPOINTER: Int32 = -2147434494
E_SURFACE_DISCARDED: Int32 = -2147434493
E_SURFACE_NODC: Int32 = -2147434492
E_SURFACE_NOTMYDC: Int32 = -2147434491
S_SURFACE_DISCARDED: Int32 = 49155
COLOR_NO_TRANSPARENT: UInt32 = 4294967295
IMGDECODE_EVENT_PROGRESS: UInt32 = 1
IMGDECODE_EVENT_PALETTE: UInt32 = 2
IMGDECODE_EVENT_BEGINBITS: UInt32 = 4
IMGDECODE_EVENT_BITSCOMPLETE: UInt32 = 8
IMGDECODE_EVENT_USEDDRAW: UInt32 = 16
IMGDECODE_HINT_TOPDOWN: UInt32 = 1
IMGDECODE_HINT_BOTTOMUP: UInt32 = 2
IMGDECODE_HINT_FULLWIDTH: UInt32 = 4
MAPMIME_DEFAULT: UInt32 = 0
MAPMIME_CLSID: UInt32 = 1
MAPMIME_DISABLE: UInt32 = 2
MAPMIME_DEFAULT_ALWAYS: UInt32 = 3
TIMERMODE_NORMAL: UInt32 = 0
TIMERMODE_VISIBILITYAWARE: UInt32 = 1
@winfunctype('Ieframe.dll')
def IEAssociateThreadWithTab(dwTabThreadID: UInt32, dwAssociatedThreadID: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IEDisassociateThreadWithTab(dwTabThreadID: UInt32, dwAssociatedThreadID: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IEIsInPrivateBrowsing() -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('Ieframe.dll')
def IEInPrivateFilteringEnabled() -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('Ieframe.dll')
def IETrackingProtectionEnabled() -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('Ieframe.dll')
def IESaveFile(hState: Windows.Win32.Foundation.HANDLE, lpwstrSourceFile: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IECancelSaveFile(hState: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IEShowSaveFileDialog(hwnd: Windows.Win32.Foundation.HWND, lpwstrInitialFileName: Windows.Win32.Foundation.PWSTR, lpwstrInitialDir: Windows.Win32.Foundation.PWSTR, lpwstrFilter: Windows.Win32.Foundation.PWSTR, lpwstrDefExt: Windows.Win32.Foundation.PWSTR, dwFilterIndex: UInt32, dwFlags: UInt32, lppwstrDestinationFilePath: POINTER(Windows.Win32.Foundation.PWSTR), phState: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IEShowOpenFileDialog(hwnd: Windows.Win32.Foundation.HWND, lpwstrFileName: Windows.Win32.Foundation.PWSTR, cchMaxFileName: UInt32, lpwstrInitialDir: Windows.Win32.Foundation.PWSTR, lpwstrFilter: Windows.Win32.Foundation.PWSTR, lpwstrDefExt: Windows.Win32.Foundation.PWSTR, dwFilterIndex: UInt32, dwFlags: UInt32, phFile: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IEGetWriteableLowHKCU(pHKey: POINTER(Windows.Win32.System.Registry.HKEY)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IEGetWriteableFolderPath(clsidFolderID: POINTER(Guid), lppwstrPath: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IEIsProtectedModeProcess(pbResult: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IEIsProtectedModeURL(lpwstrUrl: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IELaunchURL(lpwstrUrl: Windows.Win32.Foundation.PWSTR, lpProcInfo: POINTER(Windows.Win32.System.Threading.PROCESS_INFORMATION_head), lpInfo: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IERefreshElevationPolicy() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IEGetProtectedModeCookie(lpszURL: Windows.Win32.Foundation.PWSTR, lpszCookieName: Windows.Win32.Foundation.PWSTR, lpszCookieData: Windows.Win32.Foundation.PWSTR, pcchCookieData: POINTER(UInt32), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IESetProtectedModeCookie(lpszURL: Windows.Win32.Foundation.PWSTR, lpszCookieName: Windows.Win32.Foundation.PWSTR, lpszCookieData: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IERegisterWritableRegistryKey(guid: Guid, lpSubkey: Windows.Win32.Foundation.PWSTR, fSubkeyAllowed: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IERegisterWritableRegistryValue(guid: Guid, lpPath: Windows.Win32.Foundation.PWSTR, lpValueName: Windows.Win32.Foundation.PWSTR, dwType: UInt32, lpData: c_char_p_no, cbMaxData: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IEUnregisterWritableRegistry(guid: Guid) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IERegCreateKeyEx(lpSubKey: Windows.Win32.Foundation.PWSTR, Reserved: UInt32, lpClass: Windows.Win32.Foundation.PWSTR, dwOptions: UInt32, samDesired: UInt32, lpSecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), phkResult: POINTER(Windows.Win32.System.Registry.HKEY), lpdwDisposition: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IERegSetValueEx(lpSubKey: Windows.Win32.Foundation.PWSTR, lpValueName: Windows.Win32.Foundation.PWSTR, Reserved: UInt32, dwType: UInt32, lpData: c_char_p_no, cbData: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IECreateFile(lpFileName: Windows.Win32.Foundation.PWSTR, dwDesiredAccess: UInt32, dwShareMode: UInt32, lpSecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), dwCreationDisposition: UInt32, dwFlagsAndAttributes: UInt32, hTemplateFile: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('Ieframe.dll')
def IEDeleteFile(lpFileName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('Ieframe.dll')
def IERemoveDirectory(lpPathName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('Ieframe.dll')
def IEMoveFileEx(lpExistingFileName: Windows.Win32.Foundation.PWSTR, lpNewFileName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('Ieframe.dll')
def IECreateDirectory(lpPathName: Windows.Win32.Foundation.PWSTR, lpSecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('Ieframe.dll')
def IEGetFileAttributesEx(lpFileName: Windows.Win32.Foundation.PWSTR, fInfoLevelId: Windows.Win32.Storage.FileSystem.GET_FILEEX_INFO_LEVELS, lpFileInformation: c_void_p) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('Ieframe.dll')
def IEFindFirstFile(lpFileName: Windows.Win32.Foundation.PWSTR, lpFindFileData: POINTER(Windows.Win32.Storage.FileSystem.WIN32_FIND_DATAA_head)) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('MSRATING.dll')
def RatingEnable(hwndParent: Windows.Win32.Foundation.HWND, pszUsername: Windows.Win32.Foundation.PSTR, fEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingEnableW(hwndParent: Windows.Win32.Foundation.HWND, pszUsername: Windows.Win32.Foundation.PWSTR, fEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingCheckUserAccess(pszUsername: Windows.Win32.Foundation.PSTR, pszURL: Windows.Win32.Foundation.PSTR, pszRatingInfo: Windows.Win32.Foundation.PSTR, pData: c_char_p_no, cbData: UInt32, ppRatingDetails: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingCheckUserAccessW(pszUsername: Windows.Win32.Foundation.PWSTR, pszURL: Windows.Win32.Foundation.PWSTR, pszRatingInfo: Windows.Win32.Foundation.PWSTR, pData: c_char_p_no, cbData: UInt32, ppRatingDetails: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingAccessDeniedDialog(hDlg: Windows.Win32.Foundation.HWND, pszUsername: Windows.Win32.Foundation.PSTR, pszContentDescription: Windows.Win32.Foundation.PSTR, pRatingDetails: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingAccessDeniedDialogW(hDlg: Windows.Win32.Foundation.HWND, pszUsername: Windows.Win32.Foundation.PWSTR, pszContentDescription: Windows.Win32.Foundation.PWSTR, pRatingDetails: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingAccessDeniedDialog2(hDlg: Windows.Win32.Foundation.HWND, pszUsername: Windows.Win32.Foundation.PSTR, pRatingDetails: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingAccessDeniedDialog2W(hDlg: Windows.Win32.Foundation.HWND, pszUsername: Windows.Win32.Foundation.PWSTR, pRatingDetails: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingFreeDetails(pRatingDetails: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingObtainCancel(hRatingObtainQuery: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingObtainQuery(pszTargetUrl: Windows.Win32.Foundation.PSTR, dwUserData: UInt32, fCallback: IntPtr, phRatingObtainQuery: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingObtainQueryW(pszTargetUrl: Windows.Win32.Foundation.PWSTR, dwUserData: UInt32, fCallback: IntPtr, phRatingObtainQuery: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingSetupUI(hDlg: Windows.Win32.Foundation.HWND, pszUsername: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingSetupUIW(hDlg: Windows.Win32.Foundation.HWND, pszUsername: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingAddToApprovedSites(hDlg: Windows.Win32.Foundation.HWND, cbPasswordBlob: UInt32, pbPasswordBlob: c_char_p_no, lpszUrl: Windows.Win32.Foundation.PWSTR, fAlwaysNever: Windows.Win32.Foundation.BOOL, fSitePage: Windows.Win32.Foundation.BOOL, fApprovedSitesEnforced: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingClickedOnPRFInternal(hWndOwner: Windows.Win32.Foundation.HWND, param1: Windows.Win32.Foundation.HINSTANCE, lpszFileName: Windows.Win32.Foundation.PSTR, nShow: Int32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingClickedOnRATInternal(hWndOwner: Windows.Win32.Foundation.HWND, param1: Windows.Win32.Foundation.HINSTANCE, lpszFileName: Windows.Win32.Foundation.PSTR, nShow: Int32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingEnabledQuery() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingInit() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ImgUtil.dll')
def CreateMIMEMap(ppMap: POINTER(Windows.Win32.Web.InternetExplorer.IMapMIMEToCLSID_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ImgUtil.dll')
def DecodeImage(pStream: Windows.Win32.System.Com.IStream_head, pMap: Windows.Win32.Web.InternetExplorer.IMapMIMEToCLSID_head, pEventSink: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ImgUtil.dll')
def SniffStream(pInStream: Windows.Win32.System.Com.IStream_head, pnFormat: POINTER(UInt32), ppOutStream: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ImgUtil.dll')
def GetMaxMIMEIDBytes(pnMaxBytes: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ImgUtil.dll')
def IdentifyMIMEType(pbBytes: c_char_p_no, nBytes: UInt32, pnFormat: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ImgUtil.dll')
def ComputeInvCMAP(pRGBColors: POINTER(Windows.Win32.Graphics.Gdi.RGBQUAD_head), nColors: UInt32, pInvTable: c_char_p_no, cbTable: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ImgUtil.dll')
def DitherTo8(pDestBits: c_char_p_no, nDestPitch: Int32, pSrcBits: c_char_p_no, nSrcPitch: Int32, bfidSrc: POINTER(Guid), prgbDestColors: POINTER(Windows.Win32.Graphics.Gdi.RGBQUAD_head), prgbSrcColors: POINTER(Windows.Win32.Graphics.Gdi.RGBQUAD_head), pbDestInvMap: c_char_p_no, x: Int32, y: Int32, cx: Int32, cy: Int32, lDestTrans: Int32, lSrcTrans: Int32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ImgUtil.dll')
def CreateDDrawSurfaceOnDIB(hbmDib: Windows.Win32.Graphics.Gdi.HBITMAP, ppSurface: POINTER(Windows.Win32.Graphics.DirectDraw.IDirectDrawSurface_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ImgUtil.dll')
def DecodeImageEx(pStream: Windows.Win32.System.Com.IStream_head, pMap: Windows.Win32.Web.InternetExplorer.IMapMIMEToCLSID_head, pEventSink: Windows.Win32.System.Com.IUnknown_head, pszMIMETypeParam: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
CDeviceRect = Guid('3050f6d4-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
CDownloadBehavior = Guid('3050f5be-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
CHeaderFooter = Guid('3050f6cd-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
CLayoutRect = Guid('3050f664-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
CPersistDataPeer = Guid('3050f487-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
CPersistHistory = Guid('3050f4c8-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
CPersistShortcut = Guid('3050f4c6-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
CPersistSnapshot = Guid('3050f4c9-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
CPersistUserData = Guid('3050f48e-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
CoDitherToRGB8 = Guid('a860ce50-3910-11d0-86-fc-00-a0-c9-13-f7-50')
CoMapMIMEToCLSID = Guid('30c3b080-30fb-11d0-b7-24-00-aa-00-6c-1a-01')
CoSniffStream = Guid('6a01fda0-30df-11d0-b7-24-00-aa-00-6c-1a-01')
ExtensionValidationContexts = Int32
ExtensionValidationContexts_ExtensionValidationContextNone: ExtensionValidationContexts = 0
ExtensionValidationContexts_ExtensionValidationContextDynamic: ExtensionValidationContexts = 1
ExtensionValidationContexts_ExtensionValidationContextParsed: ExtensionValidationContexts = 2
ExtensionValidationResults = Int32
ExtensionValidationResults_ExtensionValidationResultNone: ExtensionValidationResults = 0
ExtensionValidationResults_ExtensionValidationResultDoNotInstantiate: ExtensionValidationResults = 1
ExtensionValidationResults_ExtensionValidationResultArrestPageLoad: ExtensionValidationResults = 2
FINDFRAME_FLAGS = Int32
FINDFRAME_NONE: FINDFRAME_FLAGS = 0
FINDFRAME_JUSTTESTEXISTENCE: FINDFRAME_FLAGS = 1
FINDFRAME_INTERNAL: FINDFRAME_FLAGS = -2147483648
FRAMEOPTIONS_FLAGS = Int32
FRAMEOPTIONS_SCROLL_YES: FRAMEOPTIONS_FLAGS = 1
FRAMEOPTIONS_SCROLL_NO: FRAMEOPTIONS_FLAGS = 2
FRAMEOPTIONS_SCROLL_AUTO: FRAMEOPTIONS_FLAGS = 4
FRAMEOPTIONS_NORESIZE: FRAMEOPTIONS_FLAGS = 8
FRAMEOPTIONS_NO3DBORDER: FRAMEOPTIONS_FLAGS = 16
FRAMEOPTIONS_DESKTOP: FRAMEOPTIONS_FLAGS = 32
FRAMEOPTIONS_BROWSERBAND: FRAMEOPTIONS_FLAGS = 64
class HTMLPersistEvents(Structure):
    pass
HomePage = Guid('766bf2ae-d650-11d1-98-11-00-c0-4f-c3-1d-2e')
HomePageSetting = Guid('374cede0-873a-4c4f-bc-86-bc-c8-cf-51-16-a3')
class IActiveXUIHandlerSite(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('30510853-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
    @commethod(3)
    def CreateScrollableContextMenu(scrollableContextMenu: POINTER(Windows.Win32.Web.InternetExplorer.IScrollableContextMenu_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PickFileAndGetResult(filePicker: Windows.Win32.System.Com.IUnknown_head, allowMultipleSelections: Windows.Win32.Foundation.BOOL, result: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IActiveXUIHandlerSite2(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7e3707b2-d087-4542-ac-1f-a0-d2-fc-d0-80-fd')
    @commethod(3)
    def AddSuspensionExemption(pullCookie: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveSuspensionExemption(ullCookie: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
class IActiveXUIHandlerSite3(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7904009a-1238-47f4-90-1c-87-13-75-c3-46-08')
    @commethod(3)
    def MessageBoxW(hwnd: Windows.Win32.Foundation.HWND, text: Windows.Win32.Foundation.PWSTR, caption: Windows.Win32.Foundation.PWSTR, type: UInt32, result: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IAnchorClick(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('13d5413b-33b9-11d2-95-a7-00-c0-4f-8e-cb-02')
    @commethod(7)
    def ProcOnClick() -> Windows.Win32.Foundation.HRESULT: ...
class IAudioSessionSite(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d7d8b684-d02d-4517-b6-b7-19-e3-df-e2-9c-45')
    @commethod(3)
    def GetAudioSessionGuid(audioSessionGuid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnAudioStreamCreated(endpointID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnAudioStreamDestroyed(endpointID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ICaretPositionProvider(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('58da43a2-108e-4d5b-9f-75-e5-f7-4f-93-ff-f5')
    @commethod(3)
    def GetCaretPosition(pptCaret: POINTER(Windows.Win32.Foundation.POINT_head), pflHeight: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
class IDeviceRect(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('3050f6d5-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
class IDithererImpl(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7c48e840-3910-11d0-86-fc-00-a0-c9-13-f7-50')
    @commethod(3)
    def SetDestColorTable(nColors: UInt32, prgbColors: POINTER(Windows.Win32.Graphics.Gdi.RGBQUAD_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetEventSink(pEventSink: Windows.Win32.Web.InternetExplorer.IImageDecodeEventSink_head) -> Windows.Win32.Foundation.HRESULT: ...
class IDocObjectService(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3050f801-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
    @commethod(3)
    def FireBeforeNavigate2(pDispatch: Windows.Win32.System.Com.IDispatch_head, lpszUrl: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, lpszFrameName: Windows.Win32.Foundation.PWSTR, pPostData: c_char_p_no, cbPostData: UInt32, lpszHeaders: Windows.Win32.Foundation.PWSTR, fPlayNavSound: Windows.Win32.Foundation.BOOL, pfCancel: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FireNavigateComplete2(pHTMLWindow2: Windows.Win32.Web.MsHtml.IHTMLWindow2_head, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def FireDownloadBegin() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FireDownloadComplete() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FireDocumentComplete(pHTMLWindow: Windows.Win32.Web.MsHtml.IHTMLWindow2_head, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def UpdateDesktopComponent(pHTMLWindow: Windows.Win32.Web.MsHtml.IHTMLWindow2_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetPendingUrl(pbstrPendingUrl: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ActiveElementChanged(pHTMLElement: Windows.Win32.Web.MsHtml.IHTMLElement_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetUrlSearchComponent(pbstrSearch: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def IsErrorUrl(lpszUrl: Windows.Win32.Foundation.PWSTR, pfIsError: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IDownloadBehavior(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('3050f5bd-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
    @commethod(7)
    def startDownload(bstrUrl: Windows.Win32.Foundation.BSTR, pdispCallback: Windows.Win32.System.Com.IDispatch_head) -> Windows.Win32.Foundation.HRESULT: ...
class IDownloadManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('988934a4-064b-11d3-bb-80-00-10-4b-35-e7-f9')
    @commethod(3)
    def Download(pmk: Windows.Win32.System.Com.IMoniker_head, pbc: Windows.Win32.System.Com.IBindCtx_head, dwBindVerb: UInt32, grfBINDF: Int32, pBindInfo: POINTER(Windows.Win32.System.Com.BINDINFO_head), pszHeaders: Windows.Win32.Foundation.PWSTR, pszRedir: Windows.Win32.Foundation.PWSTR, uiCP: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
IELAUNCHOPTION_FLAGS = Int32
IELAUNCHOPTION_SCRIPTDEBUG: IELAUNCHOPTION_FLAGS = 1
IELAUNCHOPTION_FORCE_COMPAT: IELAUNCHOPTION_FLAGS = 2
IELAUNCHOPTION_FORCE_EDGE: IELAUNCHOPTION_FLAGS = 4
IELAUNCHOPTION_LOCK_ENGINE: IELAUNCHOPTION_FLAGS = 8
class IELAUNCHURLINFO(Structure):
    cbSize: UInt32
    dwCreationFlags: UInt32
    dwLaunchOptionFlags: UInt32
IEWebDriverManager = Guid('90314af2-5250-47b3-89-d8-62-95-fc-23-bc-22')
class IEnumManagerFrames(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3caa826a-9b1f-4a79-bc-81-f0-43-0d-ed-16-48')
    @commethod(3)
    def Next(celt: UInt32, ppWindows: POINTER(POINTER(Windows.Win32.Foundation.HWND)), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Count(pcelt: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Skip(celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Clone(ppEnum: POINTER(Windows.Win32.Web.InternetExplorer.IEnumManagerFrames_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumOpenServiceActivity(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a436d7d2-17c3-4ef4-a1-e8-5c-86-fa-ff-26-c0')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(Windows.Win32.Web.InternetExplorer.IOpenServiceActivity_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(Windows.Win32.Web.InternetExplorer.IEnumOpenServiceActivity_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumOpenServiceActivityCategory(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('33627a56-8c9a-4430-8f-d1-b5-f5-c7-71-af-b6')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(Windows.Win32.Web.InternetExplorer.IOpenServiceActivityCategory_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(Windows.Win32.Web.InternetExplorer.IEnumOpenServiceActivityCategory_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumSTATURL(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3c374a42-bae4-11cf-bf-7d-00-aa-00-69-46-ee')
    @commethod(3)
    def Next(celt: UInt32, rgelt: POINTER(Windows.Win32.Web.InternetExplorer.STATURL_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(ppenum: POINTER(Windows.Win32.Web.InternetExplorer.IEnumSTATURL_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetFilter(poszFilter: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IExtensionValidation(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7d33f73d-8525-4e0f-87-db-83-02-88-ba-ff-44')
    @commethod(3)
    def Validate(extensionGuid: POINTER(Guid), extensionModulePath: Windows.Win32.Foundation.PWSTR, extensionFileVersionMS: UInt32, extensionFileVersionLS: UInt32, htmlDocumentTop: Windows.Win32.Web.MsHtml.IHTMLDocument2_head, htmlDocumentSubframe: Windows.Win32.Web.MsHtml.IHTMLDocument2_head, htmlElement: Windows.Win32.Web.MsHtml.IHTMLElement_head, contexts: Windows.Win32.Web.InternetExplorer.ExtensionValidationContexts, results: POINTER(Windows.Win32.Web.InternetExplorer.ExtensionValidationResults)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DisplayName(displayName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IHTMLPersistData(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3050f4c5-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
    @commethod(3)
    def save(pUnk: Windows.Win32.System.Com.IUnknown_head, lType: Int32, fContinueBroacast: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def load(pUnk: Windows.Win32.System.Com.IUnknown_head, lType: Int32, fDoDefault: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def queryType(lType: Int32, pfSupportsType: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IHTMLPersistDataOM(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('3050f4c0-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
    @commethod(7)
    def get_XMLDocument(p: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def getAttribute(name: Windows.Win32.Foundation.BSTR, pValue: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def setAttribute(name: Windows.Win32.Foundation.BSTR, value: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def removeAttribute(name: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IHTMLUserDataOM(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('3050f48f-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
    @commethod(7)
    def get_XMLDocument(p: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def save(strName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def load(strName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def getAttribute(name: Windows.Win32.Foundation.BSTR, pValue: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def setAttribute(name: Windows.Win32.Foundation.BSTR, value: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def removeAttribute(name: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_expires(bstr: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_expires(pbstr: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IHeaderFooter(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('3050f6ce-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
    @commethod(7)
    def get_htmlHead(p: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_htmlFoot(p: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_textHead(v: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_textHead(p: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_textFoot(v: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_textFoot(p: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_page(v: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_page(p: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_pageTotal(v: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_pageTotal(p: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_URL(v: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_URL(p: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_title(v: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_title(p: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_dateShort(v: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_dateShort(p: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_dateLong(v: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_dateLong(p: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_timeShort(v: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_timeShort(p: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_timeLong(v: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_timeLong(p: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IHeaderFooter2(c_void_p):
    extends: Windows.Win32.Web.InternetExplorer.IHeaderFooter
    Guid = Guid('305104a5-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
    @commethod(29)
    def put_font(v: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_font(p: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IHomePage(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('766bf2af-d650-11d1-98-11-00-c0-4f-c3-1d-2e')
    @commethod(7)
    def navigateHomePage() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def setHomePage(bstrURL: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def isHomePage(bstrURL: Windows.Win32.Foundation.BSTR, p: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IHomePageSetting(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('fdfc244f-18fa-4ff2-b0-8e-1d-61-8f-3f-fb-e4')
    @commethod(3)
    def SetHomePage(hwnd: Windows.Win32.Foundation.HWND, homePageUri: Windows.Win32.Foundation.PWSTR, brandingMessage: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsHomePage(uri: Windows.Win32.Foundation.PWSTR, isDefault: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetHomePageToBrowserDefault() -> Windows.Win32.Foundation.HRESULT: ...
class IIEWebDriverManager(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('bd1dc630-6590-4ca2-a2-93-6b-c7-2b-24-38-d8')
    @commethod(7)
    def ExecuteCommand(command: Windows.Win32.Foundation.PWSTR, response: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IIEWebDriverSite(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('ffb84444-453d-4fbc-9f-9d-8d-b5-c4-71-ec-75')
    @commethod(7)
    def WindowOperation(operationCode: UInt32, hWnd: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def DetachWebdriver(pUnkWD: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCapabilityValue(pUnkWD: Windows.Win32.System.Com.IUnknown_head, capName: Windows.Win32.Foundation.PWSTR, capValue: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IImageDecodeEventSink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('baa342a0-2ded-11d0-86-f4-00-a0-c9-13-f7-50')
    @commethod(3)
    def GetSurface(nWidth: Int32, nHeight: Int32, bfid: POINTER(Guid), nPasses: UInt32, dwHints: UInt32, ppSurface: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnBeginDecode(pdwEvents: POINTER(UInt32), pnFormats: POINTER(UInt32), ppFormats: POINTER(POINTER(Guid))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnBitsComplete() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnDecodeComplete(hrStatus: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnPalette() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnProgress(pBounds: POINTER(Windows.Win32.Foundation.RECT_head), bComplete: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IImageDecodeEventSink2(c_void_p):
    extends: Windows.Win32.Web.InternetExplorer.IImageDecodeEventSink
    Guid = Guid('8ebd8a57-8a96-48c9-84-a6-96-2e-2d-b9-c9-31')
    @commethod(9)
    def IsAlphaPremultRequired(pfPremultAlpha: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IImageDecodeFilter(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a3ccedf3-2de2-11d0-86-f4-00-a0-c9-13-f7-50')
    @commethod(3)
    def Initialize(pEventSink: Windows.Win32.Web.InternetExplorer.IImageDecodeEventSink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Process(pStream: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Terminate(hrStatus: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
class IIntelliForms(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('9b9f68e6-1aaa-11d2-bc-a5-00-c0-4f-d9-29-db')
    @commethod(7)
    def get_enabled(pVal: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_enabled(bVal: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IInternetExplorerManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('acc84351-04ff-44f9-b2-3f-65-5e-d1-68-c6-d5')
    @commethod(3)
    def CreateObject(dwConfig: UInt32, pszURL: Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IInternetExplorerManager2(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dfbb5136-9259-4895-b4-a7-c1-93-44-29-91-9a')
    @commethod(3)
    def EnumFrameWindows(ppEnum: POINTER(Windows.Win32.Web.InternetExplorer.IEnumManagerFrames_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ILayoutRect(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('3050f665-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
    @commethod(7)
    def put_nextRect(bstrElementId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_nextRect(pbstrElementId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_contentSrc(varContentSrc: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_contentSrc(pvarContentSrc: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_honorPageBreaks(v: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_honorPageBreaks(p: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_honorPageRules(v: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_honorPageRules(p: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_nextRectElement(pElem: Windows.Win32.System.Com.IDispatch_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_nextRectElement(ppElem: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_contentDocument(pDoc: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMapMIMEToCLSID(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d9e89500-30fa-11d0-b7-24-00-aa-00-6c-1a-01')
    @commethod(3)
    def EnableDefaultMappings(bEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MapMIMEToCLSID(pszMIMEType: Windows.Win32.Foundation.PWSTR, pCLSID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetMapping(pszMIMEType: Windows.Win32.Foundation.PWSTR, dwMapMode: UInt32, clsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IMediaActivityNotifySite(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8165cfef-179d-46c2-bc-71-3f-a7-26-dc-1f-8d')
    @commethod(3)
    def OnMediaActivityStarted(mediaActivityType: Windows.Win32.Web.InternetExplorer.MEDIA_ACTIVITY_NOTIFY_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnMediaActivityStopped(mediaActivityType: Windows.Win32.Web.InternetExplorer.MEDIA_ACTIVITY_NOTIFY_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
INTERNETEXPLORERCONFIGURATION = Int32
INTERNETEXPLORERCONFIGURATION_HOST: INTERNETEXPLORERCONFIGURATION = 1
INTERNETEXPLORERCONFIGURATION_WEB_DRIVER: INTERNETEXPLORERCONFIGURATION = 2
INTERNETEXPLORERCONFIGURATION_WEB_DRIVER_EDGE: INTERNETEXPLORERCONFIGURATION = 4
class IOpenService(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('c2952ed1-6a89-4606-92-5f-1e-d8-b4-be-06-30')
    @commethod(3)
    def IsDefault(pfIsDefault: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetDefault(fDefault: Windows.Win32.Foundation.BOOL, hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetID(pbstrID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpenServiceActivity(c_void_p):
    extends: Windows.Win32.Web.InternetExplorer.IOpenService
    Guid = Guid('13645c88-221a-4905-8e-d1-4f-51-12-cf-c1-08')
    @commethod(6)
    def Execute(pInput: Windows.Win32.Web.InternetExplorer.IOpenServiceActivityInput_head, pOutput: Windows.Win32.Web.InternetExplorer.IOpenServiceActivityOutputContext_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CanExecute(pInput: Windows.Win32.Web.InternetExplorer.IOpenServiceActivityInput_head, pOutput: Windows.Win32.Web.InternetExplorer.IOpenServiceActivityOutputContext_head, pfCanExecute: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CanExecuteType(type: Windows.Win32.Web.InternetExplorer.OpenServiceActivityContentType, pfCanExecute: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Preview(pInput: Windows.Win32.Web.InternetExplorer.IOpenServiceActivityInput_head, pOutput: Windows.Win32.Web.InternetExplorer.IOpenServiceActivityOutputContext_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CanPreview(pInput: Windows.Win32.Web.InternetExplorer.IOpenServiceActivityInput_head, pOutput: Windows.Win32.Web.InternetExplorer.IOpenServiceActivityOutputContext_head, pfCanPreview: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CanPreviewType(type: Windows.Win32.Web.InternetExplorer.OpenServiceActivityContentType, pfCanPreview: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetStatusText(pInput: Windows.Win32.Web.InternetExplorer.IOpenServiceActivityInput_head, pbstrStatusText: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetHomepageUrl(pbstrHomepageUrl: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetDisplayName(pbstrDisplayName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetDescription(pbstrDescription: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetCategoryName(pbstrCategoryName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetIconPath(pbstrIconPath: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetIcon(fSmallIcon: Windows.Win32.Foundation.BOOL, phIcon: POINTER(Windows.Win32.UI.WindowsAndMessaging.HICON)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetDescriptionFilePath(pbstrXmlPath: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetDownloadUrl(pbstrXmlUri: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetInstallUrl(pbstrInstallUri: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def IsEnabled(pfIsEnabled: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetEnabled(fEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IOpenServiceActivityCategory(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('850af9d6-7309-40b5-bd-b8-78-6c-10-6b-21-53')
    @commethod(3)
    def HasDefaultActivity(pfHasDefaultActivity: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDefaultActivity(ppDefaultActivity: POINTER(Windows.Win32.Web.InternetExplorer.IOpenServiceActivity_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetDefaultActivity(pActivity: Windows.Win32.Web.InternetExplorer.IOpenServiceActivity_head, hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetName(pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetActivityEnumerator(pInput: Windows.Win32.Web.InternetExplorer.IOpenServiceActivityInput_head, pOutput: Windows.Win32.Web.InternetExplorer.IOpenServiceActivityOutputContext_head, ppEnumActivity: POINTER(Windows.Win32.Web.InternetExplorer.IEnumOpenServiceActivity_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpenServiceActivityInput(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('75cb4db9-6da0-4da3-83-ce-42-2b-6a-43-33-46')
    @commethod(3)
    def GetVariable(pwzVariableName: Windows.Win32.Foundation.PWSTR, pwzVariableType: Windows.Win32.Foundation.PWSTR, pbstrVariableContent: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def HasVariable(pwzVariableName: Windows.Win32.Foundation.PWSTR, pwzVariableType: Windows.Win32.Foundation.PWSTR, pfHasVariable: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetType(pType: POINTER(Windows.Win32.Web.InternetExplorer.OpenServiceActivityContentType)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpenServiceActivityManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8a2d0a9d-e920-4bdc-a2-91-d3-0f-65-0b-c4-f1')
    @commethod(3)
    def GetCategoryEnumerator(eType: Windows.Win32.Web.InternetExplorer.OpenServiceActivityContentType, ppEnum: POINTER(Windows.Win32.Web.InternetExplorer.IEnumOpenServiceActivityCategory_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetActivityByID(pwzActivityID: Windows.Win32.Foundation.PWSTR, ppActivity: POINTER(Windows.Win32.Web.InternetExplorer.IOpenServiceActivity_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetActivityByHomepageAndCategory(pwzHomepage: Windows.Win32.Foundation.PWSTR, pwzCategory: Windows.Win32.Foundation.PWSTR, ppActivity: POINTER(Windows.Win32.Web.InternetExplorer.IOpenServiceActivity_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetVersionCookie(pdwVersionCookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpenServiceActivityOutputContext(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e289deab-f709-49a9-b9-9e-28-23-64-07-45-71')
    @commethod(3)
    def Navigate(pwzUri: Windows.Win32.Foundation.PWSTR, pwzMethod: Windows.Win32.Foundation.PWSTR, pwzHeaders: Windows.Win32.Foundation.PWSTR, pPostData: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CanNavigate(pwzUri: Windows.Win32.Foundation.PWSTR, pwzMethod: Windows.Win32.Foundation.PWSTR, pwzHeaders: Windows.Win32.Foundation.PWSTR, pPostData: Windows.Win32.System.Com.IStream_head, pfCanNavigate: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpenServiceManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5664125f-4e10-4e90-98-e4-e4-51-3d-95-5a-14')
    @commethod(3)
    def InstallService(pwzServiceUrl: Windows.Win32.Foundation.PWSTR, ppService: POINTER(Windows.Win32.Web.InternetExplorer.IOpenService_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UninstallService(pService: Windows.Win32.Web.InternetExplorer.IOpenService_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetServiceByID(pwzID: Windows.Win32.Foundation.PWSTR, ppService: POINTER(Windows.Win32.Web.InternetExplorer.IOpenService_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPeerFactory(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('6663f9d3-b482-11d1-89-c6-00-c0-4f-b6-bf-c4')
class IPersistHistory(c_void_p):
    extends: Windows.Win32.System.Com.IPersist
    Guid = Guid('91a565c1-e38f-11d0-94-bf-00-a0-c9-05-5c-bf')
    @commethod(4)
    def LoadHistory(pStream: Windows.Win32.System.Com.IStream_head, pbc: Windows.Win32.System.Com.IBindCtx_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SaveHistory(pStream: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetPositionCookie(dwPositioncookie: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPositionCookie(pdwPositioncookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IPrintTaskRequestFactory(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('bb516745-8c34-4f8b-96-05-68-4d-cb-14-4b-e5')
    @commethod(3)
    def CreatePrintTaskRequest(pPrintTaskRequestHandler: Windows.Win32.Web.InternetExplorer.IPrintTaskRequestHandler_head) -> Windows.Win32.Foundation.HRESULT: ...
class IPrintTaskRequestHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('191cd340-cf36-44ff-bd-53-d1-b7-01-79-9d-9b')
    @commethod(3)
    def HandlePrintTaskRequest(pPrintTaskRequest: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.Win32.Foundation.HRESULT: ...
class IScrollableContextMenu(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('30510854-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
    @commethod(3)
    def AddItem(itemText: Windows.Win32.Foundation.PWSTR, cmdID: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ShowModal(x: Int32, y: Int32, cmdID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IScrollableContextMenu2(c_void_p):
    extends: Windows.Win32.Web.InternetExplorer.IScrollableContextMenu
    Guid = Guid('f77e9056-8674-4936-92-4c-0e-4a-06-fa-63-4a')
    @commethod(5)
    def AddSeparator() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetPlacement(scmp: Windows.Win32.Web.InternetExplorer.SCROLLABLECONTEXTMENU_PLACEMENT) -> Windows.Win32.Foundation.HRESULT: ...
class ISniffStream(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4ef17940-30e0-11d0-b7-24-00-aa-00-6c-1a-01')
    @commethod(3)
    def Init(pStream: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Peek(pBuffer: c_void_p, nBytes: UInt32, pnBytesRead: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ISurfacePresenterFlip(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('30510848-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
    @commethod(3)
    def Present() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetBuffer(backBufferIndex: UInt32, riid: POINTER(Guid), ppBuffer: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class ISurfacePresenterFlip2(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('30510865-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
    @commethod(3)
    def SetRotation(dxgiRotation: Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_ROTATION) -> Windows.Win32.Foundation.HRESULT: ...
class ISurfacePresenterFlipBuffer(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e43f4a08-8bbc-4665-ac-92-c5-5c-e6-1f-d7-e7')
    @commethod(3)
    def BeginDraw(riid: POINTER(Guid), ppBuffer: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EndDraw() -> Windows.Win32.Foundation.HRESULT: ...
class ITargetContainer(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7847ec01-2bec-11d0-82-b4-00-a0-c9-0c-29-c5')
    @commethod(3)
    def GetFrameUrl(ppszFrameSrc: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFramesContainer(ppContainer: POINTER(Windows.Win32.System.Ole.IOleContainer_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITargetEmbedding(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('548793c0-9e74-11cf-96-55-00-a0-c9-03-49-23')
    @commethod(3)
    def GetTargetFrame(ppTargetFrame: POINTER(Windows.Win32.Web.InternetExplorer.ITargetFrame_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITargetFrame(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d5f78c80-5252-11cf-90-fa-00-aa-00-42-10-6e')
    @commethod(3)
    def SetFrameName(pszFrameName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFrameName(ppszFrameName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetParentFrame(ppunkParent: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FindFrame(pszTargetName: Windows.Win32.Foundation.PWSTR, ppunkContextFrame: Windows.Win32.System.Com.IUnknown_head, dwFlags: UInt32, ppunkTargetFrame: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetFrameSrc(pszFrameSrc: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetFrameSrc(ppszFrameSrc: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFramesContainer(ppContainer: POINTER(Windows.Win32.System.Ole.IOleContainer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetFrameOptions(dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetFrameOptions(pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetFrameMargins(dwWidth: UInt32, dwHeight: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetFrameMargins(pdwWidth: POINTER(UInt32), pdwHeight: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def RemoteNavigate(cLength: UInt32, pulData: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def OnChildFrameActivate(pUnkChildFrame: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def OnChildFrameDeactivate(pUnkChildFrame: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class ITargetFrame2(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('86d52e11-94a8-11d0-82-af-00-c0-4f-d5-ae-38')
    @commethod(3)
    def SetFrameName(pszFrameName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFrameName(ppszFrameName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetParentFrame(ppunkParent: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetFrameSrc(pszFrameSrc: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFrameSrc(ppszFrameSrc: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetFramesContainer(ppContainer: POINTER(Windows.Win32.System.Ole.IOleContainer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetFrameOptions(dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFrameOptions(pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetFrameMargins(dwWidth: UInt32, dwHeight: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetFrameMargins(pdwWidth: POINTER(UInt32), pdwHeight: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def FindFrame(pszTargetName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, ppunkTargetFrame: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetTargetAlias(pszTargetName: Windows.Win32.Foundation.PWSTR, ppszTargetAlias: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ITargetFramePriv(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9216e421-2bf5-11d0-82-b4-00-a0-c9-0c-29-c5')
    @commethod(3)
    def FindFrameDownwards(pszTargetName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, ppunkTargetFrame: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FindFrameInContext(pszTargetName: Windows.Win32.Foundation.PWSTR, punkContextFrame: Windows.Win32.System.Com.IUnknown_head, dwFlags: UInt32, ppunkTargetFrame: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnChildFrameActivate(pUnkChildFrame: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnChildFrameDeactivate(pUnkChildFrame: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def NavigateHack(grfHLNF: UInt32, pbc: Windows.Win32.System.Com.IBindCtx_head, pibsc: Windows.Win32.System.Com.IBindStatusCallback_head, pszTargetName: Windows.Win32.Foundation.PWSTR, pszUrl: Windows.Win32.Foundation.PWSTR, pszLocation: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def FindBrowserByIndex(dwID: UInt32, ppunkBrowser: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITargetFramePriv2(c_void_p):
    extends: Windows.Win32.Web.InternetExplorer.ITargetFramePriv
    Guid = Guid('b2c867e6-69d6-46f2-a6-11-de-d9-a4-bd-7f-ef')
    @commethod(9)
    def AggregatedNavigation2(grfHLNF: UInt32, pbc: Windows.Win32.System.Com.IBindCtx_head, pibsc: Windows.Win32.System.Com.IBindStatusCallback_head, pszTargetName: Windows.Win32.Foundation.PWSTR, pUri: Windows.Win32.System.Com.IUri_head, pszLocation: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ITargetNotify(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('863a99a0-21bc-11d0-82-b4-00-a0-c9-0c-29-c5')
    @commethod(3)
    def OnCreate(pUnkDestination: Windows.Win32.System.Com.IUnknown_head, cbCookie: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnReuse(pUnkDestination: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class ITargetNotify2(c_void_p):
    extends: Windows.Win32.Web.InternetExplorer.ITargetNotify
    Guid = Guid('3050f6b1-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
    @commethod(5)
    def GetOptionString(pbstrOptions: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ITimer(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3050f360-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
    @commethod(3)
    def Advise(vtimeMin: Windows.Win32.System.Com.VARIANT, vtimeMax: Windows.Win32.System.Com.VARIANT, vtimeInterval: Windows.Win32.System.Com.VARIANT, dwFlags: UInt32, pTimerSink: Windows.Win32.Web.InternetExplorer.ITimerSink_head, pdwCookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unadvise(dwCookie: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Freeze(fFreeze: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTime(pvtime: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITimerEx(c_void_p):
    extends: Windows.Win32.Web.InternetExplorer.ITimer
    Guid = Guid('30510414-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
    @commethod(7)
    def SetMode(dwMode: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ITimerService(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3050f35f-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
    @commethod(3)
    def CreateTimer(pReferenceTimer: Windows.Win32.Web.InternetExplorer.ITimer_head, ppNewTimer: POINTER(Windows.Win32.Web.InternetExplorer.ITimer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNamedTimer(rguidName: POINTER(Guid), ppTimer: POINTER(Windows.Win32.Web.InternetExplorer.ITimer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetNamedTimerReference(rguidName: POINTER(Guid), pReferenceTimer: Windows.Win32.Web.InternetExplorer.ITimer_head) -> Windows.Win32.Foundation.HRESULT: ...
class ITimerSink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3050f361-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
    @commethod(3)
    def OnTimer(vtimeAdvise: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
class ITridentTouchInput(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('30510850-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
    @commethod(3)
    def OnPointerMessage(msg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM, pfAllowManipulations: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class ITridentTouchInputSite(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('30510849-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
    @commethod(3)
    def SetManipulationMode(msTouchAction: Windows.Win32.Web.MsHtml.styleMsTouchAction) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ZoomToPoint(x: Int32, y: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IUrlHistoryNotify(c_void_p):
    extends: Windows.Win32.System.Ole.IOleCommandTarget
    Guid = Guid('bc40bec1-c493-11d0-83-1b-00-c0-4f-d5-ae-38')
class IUrlHistoryStg(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3c374a41-bae4-11cf-bf-7d-00-aa-00-69-46-ee')
    @commethod(3)
    def AddUrl(pocsUrl: Windows.Win32.Foundation.PWSTR, pocsTitle: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DeleteUrl(pocsUrl: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def QueryUrl(pocsUrl: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, lpSTATURL: POINTER(Windows.Win32.Web.InternetExplorer.STATURL_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def BindToObject(pocsUrl: Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppvOut: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EnumUrls(ppEnum: POINTER(Windows.Win32.Web.InternetExplorer.IEnumSTATURL_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUrlHistoryStg2(c_void_p):
    extends: Windows.Win32.Web.InternetExplorer.IUrlHistoryStg
    Guid = Guid('afa0dc11-c313-11d0-83-1a-00-c0-4f-d5-ae-38')
    @commethod(8)
    def AddUrlAndNotify(pocsUrl: Windows.Win32.Foundation.PWSTR, pocsTitle: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, fWriteHistory: Windows.Win32.Foundation.BOOL, poctNotify: Windows.Win32.System.Ole.IOleCommandTarget_head, punkISFolder: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ClearHistory() -> Windows.Win32.Foundation.HRESULT: ...
class IViewObjectPresentFlip(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('30510847-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
    @commethod(3)
    def NotifyRender(fRecreatePresenter: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RenderObjectToBitmap(pBitmap: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RenderObjectToSharedBuffer(pBuffer: Windows.Win32.Web.InternetExplorer.ISurfacePresenterFlipBuffer_head) -> Windows.Win32.Foundation.HRESULT: ...
class IViewObjectPresentFlip2(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('30510856-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
    @commethod(3)
    def NotifyLeavingView() -> Windows.Win32.Foundation.HRESULT: ...
class IViewObjectPresentFlipSite(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('30510846-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
    @commethod(3)
    def CreateSurfacePresenterFlip(pDevice: Windows.Win32.System.Com.IUnknown_head, width: UInt32, height: UInt32, backBufferCount: UInt32, format: Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT, mode: Windows.Win32.Web.MsHtml.VIEW_OBJECT_ALPHA_MODE, ppSPFlip: POINTER(Windows.Win32.Web.InternetExplorer.ISurfacePresenterFlip_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDeviceLuid(pLuid: POINTER(Windows.Win32.Foundation.LUID_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnterFullScreen() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ExitFullScreen() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsFullScreen(pfFullScreen: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetBoundingRect(pRect: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetMetrics(pPos: POINTER(Windows.Win32.Foundation.POINT_head), pSize: POINTER(Windows.Win32.Foundation.SIZE_head), pScaleX: POINTER(Single), pScaleY: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFullScreenSize(pSize: POINTER(Windows.Win32.Foundation.SIZE_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IViewObjectPresentFlipSite2(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('aad0cbf1-e7fd-4f12-89-02-c7-81-32-a8-e0-1d')
    @commethod(3)
    def GetRotationForCurrentOutput(pDxgiRotation: POINTER(Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_ROTATION)) -> Windows.Win32.Foundation.HRESULT: ...
class IWebBrowserEventsService(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('54a8f188-9ebd-4795-ad-16-9b-49-45-11-96-36')
    @commethod(3)
    def FireBeforeNavigate2Event(pfCancel: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FireNavigateComplete2Event() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def FireDownloadBeginEvent() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FireDownloadCompleteEvent() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FireDocumentCompleteEvent() -> Windows.Win32.Foundation.HRESULT: ...
class IWebBrowserEventsUrlService(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('87cc5d04-eafa-4833-98-20-8f-98-65-30-cc-00')
    @commethod(3)
    def GetUrlForEvents(pUrl: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
IntelliForms = Guid('613ab92e-16bf-11d2-bc-a5-00-c0-4f-d9-29-db')
InternetExplorerManager = Guid('df4fcc34-067a-4e0a-83-52-4a-1a-50-95-34-6e')
class Iwfolders(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('bae31f98-1b81-11d2-a9-7a-00-c0-4f-8e-cb-02')
    @commethod(7)
    def navigate(bstrUrl: Windows.Win32.Foundation.BSTR, pbstrRetVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def navigateFrame(bstrUrl: Windows.Win32.Foundation.BSTR, bstrTargetFrame: Windows.Win32.Foundation.BSTR, pbstrRetVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def navigateNoSite(bstrUrl: Windows.Win32.Foundation.BSTR, bstrTargetFrame: Windows.Win32.Foundation.BSTR, dwhwnd: UInt32, pwb: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class LayoutRectEvents(Structure):
    pass
MEDIA_ACTIVITY_NOTIFY_TYPE = Int32
MEDIA_ACTIVITY_NOTIFY_TYPE_MediaPlayback: MEDIA_ACTIVITY_NOTIFY_TYPE = 0
MEDIA_ACTIVITY_NOTIFY_TYPE_MediaRecording: MEDIA_ACTIVITY_NOTIFY_TYPE = 1
MEDIA_ACTIVITY_NOTIFY_TYPE_MediaCasting: MEDIA_ACTIVITY_NOTIFY_TYPE = 2
class NAVIGATEDATA(Structure):
    ulTarget: UInt32
    ulURL: UInt32
    ulRefURL: UInt32
    ulPostData: UInt32
    dwFlags: UInt32
NAVIGATEFRAME_FLAGS = Int32
NAVIGATEFRAME_FL_RECORD: NAVIGATEFRAME_FLAGS = 1
NAVIGATEFRAME_FL_POST: NAVIGATEFRAME_FLAGS = 2
NAVIGATEFRAME_FL_NO_DOC_CACHE: NAVIGATEFRAME_FLAGS = 4
NAVIGATEFRAME_FL_NO_IMAGE_CACHE: NAVIGATEFRAME_FLAGS = 8
NAVIGATEFRAME_FL_AUTH_FAIL_CACHE_OK: NAVIGATEFRAME_FLAGS = 16
NAVIGATEFRAME_FL_SENDING_FROM_FORM: NAVIGATEFRAME_FLAGS = 32
NAVIGATEFRAME_FL_REALLY_SENDING_FROM_FORM: NAVIGATEFRAME_FLAGS = 64
OpenServiceActivityContentType = Int32
OpenServiceActivityContentType_ActivityContentNone: OpenServiceActivityContentType = -1
OpenServiceActivityContentType_ActivityContentDocument: OpenServiceActivityContentType = 0
OpenServiceActivityContentType_ActivityContentSelection: OpenServiceActivityContentType = 1
OpenServiceActivityContentType_ActivityContentLink: OpenServiceActivityContentType = 2
OpenServiceActivityContentType_ActivityContentCount: OpenServiceActivityContentType = 3
OpenServiceActivityManager = Guid('c5efd803-50f8-43cd-9a-b8-aa-fc-13-94-c9-e0')
OpenServiceErrors = Int32
OS_E_NOTFOUND: OpenServiceErrors = -2147287038
OS_E_NOTSUPPORTED: OpenServiceErrors = -2147467231
OS_E_CANCELLED: OpenServiceErrors = -2147471631
OS_E_GPDISABLED: OpenServiceErrors = -1072886820
OpenServiceManager = Guid('098870b6-39ea-480b-b8-b5-dd-01-67-c4-db-59')
PeerFactory = Guid('3050f4cf-98b5-11cf-bb-82-00-aa-00-bd-ce-0b')
SCROLLABLECONTEXTMENU_PLACEMENT = Int32
SCMP_TOP: SCROLLABLECONTEXTMENU_PLACEMENT = 0
SCMP_BOTTOM: SCROLLABLECONTEXTMENU_PLACEMENT = 1
SCMP_LEFT: SCROLLABLECONTEXTMENU_PLACEMENT = 2
SCMP_RIGHT: SCROLLABLECONTEXTMENU_PLACEMENT = 3
SCMP_FULL: SCROLLABLECONTEXTMENU_PLACEMENT = 4
class STATURL(Structure):
    cbSize: UInt32
    pwcsUrl: Windows.Win32.Foundation.PWSTR
    pwcsTitle: Windows.Win32.Foundation.PWSTR
    ftLastVisited: Windows.Win32.Foundation.FILETIME
    ftLastUpdated: Windows.Win32.Foundation.FILETIME
    ftExpires: Windows.Win32.Foundation.FILETIME
    dwFlags: UInt32
wfolders = Guid('bae31f9a-1b81-11d2-a9-7a-00-c0-4f-8e-cb-02')
make_head(_module, 'HTMLPersistEvents')
make_head(_module, 'IActiveXUIHandlerSite')
make_head(_module, 'IActiveXUIHandlerSite2')
make_head(_module, 'IActiveXUIHandlerSite3')
make_head(_module, 'IAnchorClick')
make_head(_module, 'IAudioSessionSite')
make_head(_module, 'ICaretPositionProvider')
make_head(_module, 'IDeviceRect')
make_head(_module, 'IDithererImpl')
make_head(_module, 'IDocObjectService')
make_head(_module, 'IDownloadBehavior')
make_head(_module, 'IDownloadManager')
make_head(_module, 'IELAUNCHURLINFO')
make_head(_module, 'IEnumManagerFrames')
make_head(_module, 'IEnumOpenServiceActivity')
make_head(_module, 'IEnumOpenServiceActivityCategory')
make_head(_module, 'IEnumSTATURL')
make_head(_module, 'IExtensionValidation')
make_head(_module, 'IHTMLPersistData')
make_head(_module, 'IHTMLPersistDataOM')
make_head(_module, 'IHTMLUserDataOM')
make_head(_module, 'IHeaderFooter')
make_head(_module, 'IHeaderFooter2')
make_head(_module, 'IHomePage')
make_head(_module, 'IHomePageSetting')
make_head(_module, 'IIEWebDriverManager')
make_head(_module, 'IIEWebDriverSite')
make_head(_module, 'IImageDecodeEventSink')
make_head(_module, 'IImageDecodeEventSink2')
make_head(_module, 'IImageDecodeFilter')
make_head(_module, 'IIntelliForms')
make_head(_module, 'IInternetExplorerManager')
make_head(_module, 'IInternetExplorerManager2')
make_head(_module, 'ILayoutRect')
make_head(_module, 'IMapMIMEToCLSID')
make_head(_module, 'IMediaActivityNotifySite')
make_head(_module, 'IOpenService')
make_head(_module, 'IOpenServiceActivity')
make_head(_module, 'IOpenServiceActivityCategory')
make_head(_module, 'IOpenServiceActivityInput')
make_head(_module, 'IOpenServiceActivityManager')
make_head(_module, 'IOpenServiceActivityOutputContext')
make_head(_module, 'IOpenServiceManager')
make_head(_module, 'IPeerFactory')
make_head(_module, 'IPersistHistory')
make_head(_module, 'IPrintTaskRequestFactory')
make_head(_module, 'IPrintTaskRequestHandler')
make_head(_module, 'IScrollableContextMenu')
make_head(_module, 'IScrollableContextMenu2')
make_head(_module, 'ISniffStream')
make_head(_module, 'ISurfacePresenterFlip')
make_head(_module, 'ISurfacePresenterFlip2')
make_head(_module, 'ISurfacePresenterFlipBuffer')
make_head(_module, 'ITargetContainer')
make_head(_module, 'ITargetEmbedding')
make_head(_module, 'ITargetFrame')
make_head(_module, 'ITargetFrame2')
make_head(_module, 'ITargetFramePriv')
make_head(_module, 'ITargetFramePriv2')
make_head(_module, 'ITargetNotify')
make_head(_module, 'ITargetNotify2')
make_head(_module, 'ITimer')
make_head(_module, 'ITimerEx')
make_head(_module, 'ITimerService')
make_head(_module, 'ITimerSink')
make_head(_module, 'ITridentTouchInput')
make_head(_module, 'ITridentTouchInputSite')
make_head(_module, 'IUrlHistoryNotify')
make_head(_module, 'IUrlHistoryStg')
make_head(_module, 'IUrlHistoryStg2')
make_head(_module, 'IViewObjectPresentFlip')
make_head(_module, 'IViewObjectPresentFlip2')
make_head(_module, 'IViewObjectPresentFlipSite')
make_head(_module, 'IViewObjectPresentFlipSite2')
make_head(_module, 'IWebBrowserEventsService')
make_head(_module, 'IWebBrowserEventsUrlService')
make_head(_module, 'Iwfolders')
make_head(_module, 'LayoutRectEvents')
make_head(_module, 'NAVIGATEDATA')
make_head(_module, 'STATURL')
__all__ = [
    "ADDRESSBAND",
    "ADDURL_ADDTOCACHE",
    "ADDURL_ADDTOHISTORYANDCACHE",
    "ADDURL_FIRST",
    "ADDURL_FLAG",
    "ADDURL_Max",
    "AnchorClick",
    "CATID_MSOfficeAntiVirus",
    "CDeviceRect",
    "CDownloadBehavior",
    "CHeaderFooter",
    "CLayoutRect",
    "COLOR_NO_TRANSPARENT",
    "CPersistDataPeer",
    "CPersistHistory",
    "CPersistShortcut",
    "CPersistSnapshot",
    "CPersistUserData",
    "CoDitherToRGB8",
    "CoMapMIMEToCLSID",
    "CoSniffStream",
    "ComputeInvCMAP",
    "CreateDDrawSurfaceOnDIB",
    "CreateMIMEMap",
    "DISPID_ACTIVEXFILTERINGENABLED",
    "DISPID_ADDCHANNEL",
    "DISPID_ADDDESKTOPCOMPONENT",
    "DISPID_ADDFAVORITE",
    "DISPID_ADDSEARCHPROVIDER",
    "DISPID_ADDSERVICE",
    "DISPID_ADDSITEMODE",
    "DISPID_ADDTHUMBNAILBUTTONS",
    "DISPID_ADDTOFAVORITESBAR",
    "DISPID_ADDTRACKINGPROTECTIONLIST",
    "DISPID_ADVANCEERROR",
    "DISPID_AMBIENT_OFFLINEIFNOTCONNECTED",
    "DISPID_AMBIENT_SILENT",
    "DISPID_AUTOCOMPLETEATTACH",
    "DISPID_AUTOCOMPLETESAVEFORM",
    "DISPID_AUTOSCAN",
    "DISPID_BEFORENAVIGATE",
    "DISPID_BEFORENAVIGATE2",
    "DISPID_BEFORESCRIPTEXECUTE",
    "DISPID_BRANDIMAGEURI",
    "DISPID_BUILDNEWTABPAGE",
    "DISPID_CANADVANCEERROR",
    "DISPID_CANRETREATERROR",
    "DISPID_CHANGEDEFAULTBROWSER",
    "DISPID_CLEARNOTIFICATION",
    "DISPID_CLEARSITEMODEICONOVERLAY",
    "DISPID_CLIENTTOHOSTWINDOW",
    "DISPID_COMMANDSTATECHANGE",
    "DISPID_CONTENTDISCOVERYRESET",
    "DISPID_COUNTVIEWTYPES",
    "DISPID_CREATESUBSCRIPTION",
    "DISPID_CUSTOMIZECLEARTYPE",
    "DISPID_CUSTOMIZESETTINGS",
    "DISPID_DEFAULTSEARCHPROVIDER",
    "DISPID_DELETESUBSCRIPTION",
    "DISPID_DEPTH",
    "DISPID_DIAGNOSECONNECTION",
    "DISPID_DIAGNOSECONNECTIONUILESS",
    "DISPID_DOCUMENTCOMPLETE",
    "DISPID_DOUBLECLICK",
    "DISPID_DOWNLOADBEGIN",
    "DISPID_DOWNLOADCOMPLETE",
    "DISPID_ENABLENOTIFICATIONQUEUE",
    "DISPID_ENABLENOTIFICATIONQUEUELARGE",
    "DISPID_ENABLENOTIFICATIONQUEUESQUARE",
    "DISPID_ENABLENOTIFICATIONQUEUEWIDE",
    "DISPID_ENABLESUGGESTEDSITES",
    "DISPID_ENUMOPTIONS",
    "DISPID_EXPAND",
    "DISPID_EXPORT",
    "DISPID_FAVSELECTIONCHANGE",
    "DISPID_FILEDOWNLOAD",
    "DISPID_FLAGS",
    "DISPID_FRAMEBEFORENAVIGATE",
    "DISPID_FRAMENAVIGATECOMPLETE",
    "DISPID_FRAMENEWWINDOW",
    "DISPID_GETALWAYSSHOWLOCKSTATE",
    "DISPID_GETCVLISTDATA",
    "DISPID_GETCVLISTLOCALDATA",
    "DISPID_GETDETAILSSTATE",
    "DISPID_GETEMIELISTDATA",
    "DISPID_GETEMIELISTLOCALDATA",
    "DISPID_GETERRORCHAR",
    "DISPID_GETERRORCODE",
    "DISPID_GETERRORLINE",
    "DISPID_GETERRORMSG",
    "DISPID_GETERRORURL",
    "DISPID_GETEXPERIMENTALFLAG",
    "DISPID_GETEXPERIMENTALVALUE",
    "DISPID_GETNEEDHVSIAUTOLAUNCHFLAG",
    "DISPID_GETNEEDIEAUTOLAUNCHFLAG",
    "DISPID_GETOSSKU",
    "DISPID_GETPERERRSTATE",
    "DISPID_HASNEEDHVSIAUTOLAUNCHFLAG",
    "DISPID_HASNEEDIEAUTOLAUNCHFLAG",
    "DISPID_IMPORT",
    "DISPID_IMPORTEXPORTFAVORITES",
    "DISPID_INITIALIZED",
    "DISPID_INPRIVATEFILTERINGENABLED",
    "DISPID_INVOKECONTEXTMENU",
    "DISPID_ISMETAREFERRERAVAILABLE",
    "DISPID_ISSEARCHMIGRATED",
    "DISPID_ISSEARCHPROVIDERINSTALLED",
    "DISPID_ISSERVICEINSTALLED",
    "DISPID_ISSITEMODE",
    "DISPID_ISSITEMODEFIRSTRUN",
    "DISPID_ISSUBSCRIBED",
    "DISPID_LAUNCHIE",
    "DISPID_LAUNCHINHVSI",
    "DISPID_LAUNCHINTERNETOPTIONS",
    "DISPID_LAUNCHNETWORKCLIENTHELP",
    "DISPID_MODE",
    "DISPID_MOVESELECTIONDOWN",
    "DISPID_MOVESELECTIONTO",
    "DISPID_MOVESELECTIONUP",
    "DISPID_NAVIGATEANDFIND",
    "DISPID_NAVIGATECOMPLETE",
    "DISPID_NAVIGATECOMPLETE2",
    "DISPID_NAVIGATEERROR",
    "DISPID_NAVIGATETOSUGGESTEDSITES",
    "DISPID_NEWFOLDER",
    "DISPID_NEWPROCESS",
    "DISPID_NEWWINDOW",
    "DISPID_NEWWINDOW2",
    "DISPID_NEWWINDOW3",
    "DISPID_NSCOLUMNS",
    "DISPID_ONADDRESSBAR",
    "DISPID_ONFULLSCREEN",
    "DISPID_ONMENUBAR",
    "DISPID_ONQUIT",
    "DISPID_ONSTATUSBAR",
    "DISPID_ONTHEATERMODE",
    "DISPID_ONTOOLBAR",
    "DISPID_ONVISIBLE",
    "DISPID_OPENFAVORITESPANE",
    "DISPID_OPENFAVORITESSETTINGS",
    "DISPID_PHISHINGENABLED",
    "DISPID_PINNEDSITESTATE",
    "DISPID_PRINTTEMPLATEINSTANTIATION",
    "DISPID_PRINTTEMPLATETEARDOWN",
    "DISPID_PRIVACYIMPACTEDSTATECHANGE",
    "DISPID_PROGRESSCHANGE",
    "DISPID_PROPERTYCHANGE",
    "DISPID_PROVISIONNETWORKS",
    "DISPID_QUIT",
    "DISPID_REDIRECTXDOMAINBLOCKED",
    "DISPID_REFRESHOFFLINEDESKTOP",
    "DISPID_REMOVESCHEDULEDTILENOTIFICATION",
    "DISPID_REPORTSAFEURL",
    "DISPID_RESETEXPERIMENTALFLAGS",
    "DISPID_RESETFIRSTBOOTMODE",
    "DISPID_RESETSAFEMODE",
    "DISPID_RESETSORT",
    "DISPID_RETREATERROR",
    "DISPID_ROOT",
    "DISPID_RUNONCEHASSHOWN",
    "DISPID_RUNONCEREQUIREDSETTINGSCOMPLETE",
    "DISPID_RUNONCESHOWN",
    "DISPID_SCHEDULEDTILENOTIFICATION",
    "DISPID_SEARCHGUIDEURL",
    "DISPID_SELECTEDITEM",
    "DISPID_SELECTEDITEMS",
    "DISPID_SELECTIONCHANGE",
    "DISPID_SETACTIVITIESVISIBLE",
    "DISPID_SETDETAILSSTATE",
    "DISPID_SETEXPERIMENTALFLAG",
    "DISPID_SETEXPERIMENTALVALUE",
    "DISPID_SETMSDEFAULTS",
    "DISPID_SETNEEDHVSIAUTOLAUNCHFLAG",
    "DISPID_SETNEEDIEAUTOLAUNCHFLAG",
    "DISPID_SETPERERRSTATE",
    "DISPID_SETPHISHINGFILTERSTATUS",
    "DISPID_SETRECENTLYCLOSEDVISIBLE",
    "DISPID_SETROOT",
    "DISPID_SETSECURELOCKICON",
    "DISPID_SETSITEMODEICONOVERLAY",
    "DISPID_SETSITEMODEPROPERTIES",
    "DISPID_SETTHUMBNAILBUTTONS",
    "DISPID_SETVIEWTYPE",
    "DISPID_SHELLUIHELPERLAST",
    "DISPID_SHOWBROWSERUI",
    "DISPID_SHOWINPRIVATEHELP",
    "DISPID_SHOWTABSHELP",
    "DISPID_SITEMODEACTIVATE",
    "DISPID_SITEMODEADDBUTTONSTYLE",
    "DISPID_SITEMODEADDJUMPLISTITEM",
    "DISPID_SITEMODECLEARBADGE",
    "DISPID_SITEMODECLEARJUMPLIST",
    "DISPID_SITEMODECREATEJUMPLIST",
    "DISPID_SITEMODEREFRESHBADGE",
    "DISPID_SITEMODESHOWBUTTONSTYLE",
    "DISPID_SITEMODESHOWJUMPLIST",
    "DISPID_SKIPRUNONCE",
    "DISPID_SKIPTABSWELCOME",
    "DISPID_SQMENABLED",
    "DISPID_STARTBADGEUPDATE",
    "DISPID_STARTPERIODICUPDATE",
    "DISPID_STARTPERIODICUPDATEBATCH",
    "DISPID_STATUSTEXTCHANGE",
    "DISPID_STOPBADGEUPDATE",
    "DISPID_STOPPERIODICUPDATE",
    "DISPID_SUBSCRIPTIONSENABLED",
    "DISPID_SUGGESTEDSITESENABLED",
    "DISPID_SYNCHRONIZE",
    "DISPID_THIRDPARTYURLBLOCKED",
    "DISPID_TITLECHANGE",
    "DISPID_TITLEICONCHANGE",
    "DISPID_TRACKINGPROTECTIONENABLED",
    "DISPID_TVFLAGS",
    "DISPID_UNSELECTALL",
    "DISPID_UPDATEPAGESTATUS",
    "DISPID_UPDATETHUMBNAILBUTTON",
    "DISPID_VIEWUPDATE",
    "DISPID_WEBWORKERFINISHED",
    "DISPID_WEBWORKERSTARTED",
    "DISPID_WINDOWACTIVATE",
    "DISPID_WINDOWCLOSING",
    "DISPID_WINDOWMOVE",
    "DISPID_WINDOWREGISTERED",
    "DISPID_WINDOWRESIZE",
    "DISPID_WINDOWREVOKED",
    "DISPID_WINDOWSETHEIGHT",
    "DISPID_WINDOWSETLEFT",
    "DISPID_WINDOWSETRESIZABLE",
    "DISPID_WINDOWSETTOP",
    "DISPID_WINDOWSETWIDTH",
    "DISPID_WINDOWSTATECHANGED",
    "DecodeImage",
    "DecodeImageEx",
    "DitherTo8",
    "E_SURFACE_DISCARDED",
    "E_SURFACE_NODC",
    "E_SURFACE_NOSURFACE",
    "E_SURFACE_NOTMYDC",
    "E_SURFACE_NOTMYPOINTER",
    "E_SURFACE_UNKNOWN_FORMAT",
    "ExtensionValidationContexts",
    "ExtensionValidationContexts_ExtensionValidationContextDynamic",
    "ExtensionValidationContexts_ExtensionValidationContextNone",
    "ExtensionValidationContexts_ExtensionValidationContextParsed",
    "ExtensionValidationResults",
    "ExtensionValidationResults_ExtensionValidationResultArrestPageLoad",
    "ExtensionValidationResults_ExtensionValidationResultDoNotInstantiate",
    "ExtensionValidationResults_ExtensionValidationResultNone",
    "FINDFRAME_FLAGS",
    "FINDFRAME_INTERNAL",
    "FINDFRAME_JUSTTESTEXISTENCE",
    "FINDFRAME_NONE",
    "FRAMEOPTIONS_BROWSERBAND",
    "FRAMEOPTIONS_DESKTOP",
    "FRAMEOPTIONS_FLAGS",
    "FRAMEOPTIONS_NO3DBORDER",
    "FRAMEOPTIONS_NORESIZE",
    "FRAMEOPTIONS_SCROLL_AUTO",
    "FRAMEOPTIONS_SCROLL_NO",
    "FRAMEOPTIONS_SCROLL_YES",
    "GetMaxMIMEIDBytes",
    "HTMLPersistEvents",
    "HomePage",
    "HomePageSetting",
    "IActiveXUIHandlerSite",
    "IActiveXUIHandlerSite2",
    "IActiveXUIHandlerSite3",
    "IAnchorClick",
    "IAudioSessionSite",
    "ICaretPositionProvider",
    "IDeviceRect",
    "IDithererImpl",
    "IDocObjectService",
    "IDownloadBehavior",
    "IDownloadManager",
    "IEAssociateThreadWithTab",
    "IECMDID_ARG_CLEAR_FORMS_ALL",
    "IECMDID_ARG_CLEAR_FORMS_ALL_BUT_PASSWORDS",
    "IECMDID_ARG_CLEAR_FORMS_PASSWORDS_ONLY",
    "IECMDID_BEFORENAVIGATE_DOEXTERNALBROWSE",
    "IECMDID_BEFORENAVIGATE_GETIDLIST",
    "IECMDID_BEFORENAVIGATE_GETSHELLBROWSE",
    "IECMDID_CLEAR_AUTOCOMPLETE_FOR_FORMS",
    "IECMDID_GET_INVOKE_DEFAULT_BROWSER_ON_NEW_WINDOW",
    "IECMDID_SETID_AUTOCOMPLETE_FOR_FORMS",
    "IECMDID_SET_INVOKE_DEFAULT_BROWSER_ON_NEW_WINDOW",
    "IECancelSaveFile",
    "IECreateDirectory",
    "IECreateFile",
    "IEDeleteFile",
    "IEDisassociateThreadWithTab",
    "IEFindFirstFile",
    "IEGetFileAttributesEx",
    "IEGetProcessModule_PROC_NAME",
    "IEGetProtectedModeCookie",
    "IEGetTabWindowExports_PROC_NAME",
    "IEGetWriteableFolderPath",
    "IEGetWriteableLowHKCU",
    "IEInPrivateFilteringEnabled",
    "IEIsInPrivateBrowsing",
    "IEIsProtectedModeProcess",
    "IEIsProtectedModeURL",
    "IELAUNCHOPTION_FLAGS",
    "IELAUNCHOPTION_FORCE_COMPAT",
    "IELAUNCHOPTION_FORCE_EDGE",
    "IELAUNCHOPTION_LOCK_ENGINE",
    "IELAUNCHOPTION_SCRIPTDEBUG",
    "IELAUNCHURLINFO",
    "IELaunchURL",
    "IEMoveFileEx",
    "IEPROCESS_MODULE_NAME",
    "IERefreshElevationPolicy",
    "IERegCreateKeyEx",
    "IERegSetValueEx",
    "IERegisterWritableRegistryKey",
    "IERegisterWritableRegistryValue",
    "IERemoveDirectory",
    "IESaveFile",
    "IESetProtectedModeCookie",
    "IEShowOpenFileDialog",
    "IEShowSaveFileDialog",
    "IETrackingProtectionEnabled",
    "IEUnregisterWritableRegistry",
    "IEWebDriverManager",
    "IE_USE_OE_MAIL_HKEY",
    "IE_USE_OE_MAIL_KEY",
    "IE_USE_OE_MAIL_VALUE",
    "IE_USE_OE_NEWS_HKEY",
    "IE_USE_OE_NEWS_KEY",
    "IE_USE_OE_NEWS_VALUE",
    "IE_USE_OE_PRESENT_HKEY",
    "IE_USE_OE_PRESENT_KEY",
    "IEnumManagerFrames",
    "IEnumOpenServiceActivity",
    "IEnumOpenServiceActivityCategory",
    "IEnumSTATURL",
    "IExtensionValidation",
    "IHTMLPersistData",
    "IHTMLPersistDataOM",
    "IHTMLUserDataOM",
    "IHeaderFooter",
    "IHeaderFooter2",
    "IHomePage",
    "IHomePageSetting",
    "IIEWebDriverManager",
    "IIEWebDriverSite",
    "IImageDecodeEventSink",
    "IImageDecodeEventSink2",
    "IImageDecodeFilter",
    "IIntelliForms",
    "IInternetExplorerManager",
    "IInternetExplorerManager2",
    "ILayoutRect",
    "IMGDECODE_EVENT_BEGINBITS",
    "IMGDECODE_EVENT_BITSCOMPLETE",
    "IMGDECODE_EVENT_PALETTE",
    "IMGDECODE_EVENT_PROGRESS",
    "IMGDECODE_EVENT_USEDDRAW",
    "IMGDECODE_HINT_BOTTOMUP",
    "IMGDECODE_HINT_FULLWIDTH",
    "IMGDECODE_HINT_TOPDOWN",
    "IMapMIMEToCLSID",
    "IMediaActivityNotifySite",
    "INTERNETEXPLORERCONFIGURATION",
    "INTERNETEXPLORERCONFIGURATION_HOST",
    "INTERNETEXPLORERCONFIGURATION_WEB_DRIVER",
    "INTERNETEXPLORERCONFIGURATION_WEB_DRIVER_EDGE",
    "IOpenService",
    "IOpenServiceActivity",
    "IOpenServiceActivityCategory",
    "IOpenServiceActivityInput",
    "IOpenServiceActivityManager",
    "IOpenServiceActivityOutputContext",
    "IOpenServiceManager",
    "IPeerFactory",
    "IPersistHistory",
    "IPrintTaskRequestFactory",
    "IPrintTaskRequestHandler",
    "IScrollableContextMenu",
    "IScrollableContextMenu2",
    "ISniffStream",
    "ISurfacePresenterFlip",
    "ISurfacePresenterFlip2",
    "ISurfacePresenterFlipBuffer",
    "ITargetContainer",
    "ITargetEmbedding",
    "ITargetFrame",
    "ITargetFrame2",
    "ITargetFramePriv",
    "ITargetFramePriv2",
    "ITargetNotify",
    "ITargetNotify2",
    "ITimer",
    "ITimerEx",
    "ITimerService",
    "ITimerSink",
    "ITridentTouchInput",
    "ITridentTouchInputSite",
    "IUrlHistoryNotify",
    "IUrlHistoryStg",
    "IUrlHistoryStg2",
    "IViewObjectPresentFlip",
    "IViewObjectPresentFlip2",
    "IViewObjectPresentFlipSite",
    "IViewObjectPresentFlipSite2",
    "IWebBrowserEventsService",
    "IWebBrowserEventsUrlService",
    "IdentifyMIMEType",
    "IntelliForms",
    "InternetExplorerManager",
    "Iwfolders",
    "LINKSBAND",
    "LayoutRectEvents",
    "MAPMIME_CLSID",
    "MAPMIME_DEFAULT",
    "MAPMIME_DEFAULT_ALWAYS",
    "MAPMIME_DISABLE",
    "MAX_SEARCH_FORMAT_STRING",
    "MEDIA_ACTIVITY_NOTIFY_TYPE",
    "MEDIA_ACTIVITY_NOTIFY_TYPE_MediaCasting",
    "MEDIA_ACTIVITY_NOTIFY_TYPE_MediaPlayback",
    "MEDIA_ACTIVITY_NOTIFY_TYPE_MediaRecording",
    "NAVIGATEDATA",
    "NAVIGATEFRAME_FLAGS",
    "NAVIGATEFRAME_FL_AUTH_FAIL_CACHE_OK",
    "NAVIGATEFRAME_FL_NO_DOC_CACHE",
    "NAVIGATEFRAME_FL_NO_IMAGE_CACHE",
    "NAVIGATEFRAME_FL_POST",
    "NAVIGATEFRAME_FL_REALLY_SENDING_FROM_FORM",
    "NAVIGATEFRAME_FL_RECORD",
    "NAVIGATEFRAME_FL_SENDING_FROM_FORM",
    "OS_E_CANCELLED",
    "OS_E_GPDISABLED",
    "OS_E_NOTFOUND",
    "OS_E_NOTSUPPORTED",
    "OpenServiceActivityContentType",
    "OpenServiceActivityContentType_ActivityContentCount",
    "OpenServiceActivityContentType_ActivityContentDocument",
    "OpenServiceActivityContentType_ActivityContentLink",
    "OpenServiceActivityContentType_ActivityContentNone",
    "OpenServiceActivityContentType_ActivityContentSelection",
    "OpenServiceActivityManager",
    "OpenServiceErrors",
    "OpenServiceManager",
    "PeerFactory",
    "REGSTRA_VAL_STARTPAGE",
    "REGSTR_PATH_CURRENT",
    "REGSTR_PATH_DEFAULT",
    "REGSTR_PATH_INETCPL_RESTRICTIONS",
    "REGSTR_PATH_MIME_DATABASE",
    "REGSTR_PATH_REMOTEACCESS",
    "REGSTR_PATH_REMOTEACESS",
    "REGSTR_SHIFTQUICKSUFFIX",
    "REGSTR_VAL_ACCEPT_LANGUAGE",
    "REGSTR_VAL_ACCESSMEDIUM",
    "REGSTR_VAL_ACCESSTYPE",
    "REGSTR_VAL_ALIASTO",
    "REGSTR_VAL_ANCHORCOLOR",
    "REGSTR_VAL_ANCHORCOLORHOVER",
    "REGSTR_VAL_ANCHORCOLORVISITED",
    "REGSTR_VAL_ANCHORUNDERLINE",
    "REGSTR_VAL_AUTODETECT",
    "REGSTR_VAL_AUTODIALDLLNAME",
    "REGSTR_VAL_AUTODIALFCNNAME",
    "REGSTR_VAL_AUTODIAL_MONITORCLASSNAME",
    "REGSTR_VAL_AUTODIAL_TRYONLYONCE",
    "REGSTR_VAL_AUTONAVIGATE",
    "REGSTR_VAL_AUTOSEARCH",
    "REGSTR_VAL_BACKBITMAP",
    "REGSTR_VAL_BACKGROUNDCOLOR",
    "REGSTR_VAL_BODYCHARSET",
    "REGSTR_VAL_BYPASSAUTOCONFIG",
    "REGSTR_VAL_CACHEPREFIX",
    "REGSTR_VAL_CHECKASSOC",
    "REGSTR_VAL_CODEDOWNLOAD",
    "REGSTR_VAL_CODEDOWNLOAD_DEF",
    "REGSTR_VAL_CODEPAGE",
    "REGSTR_VAL_COVEREXCLUDE",
    "REGSTR_VAL_DAYSTOKEEP",
    "REGSTR_VAL_DEFAULT_CODEPAGE",
    "REGSTR_VAL_DEFAULT_SCRIPT",
    "REGSTR_VAL_DEF_ENCODING",
    "REGSTR_VAL_DEF_INETENCODING",
    "REGSTR_VAL_DESCRIPTION",
    "REGSTR_VAL_DIRECTORY",
    "REGSTR_VAL_DISCONNECTIDLETIME",
    "REGSTR_VAL_ENABLEAUTODIAL",
    "REGSTR_VAL_ENABLEAUTODIALDISCONNECT",
    "REGSTR_VAL_ENABLEAUTODISCONNECT",
    "REGSTR_VAL_ENABLEEXITDISCONNECT",
    "REGSTR_VAL_ENABLESECURITYCHECK",
    "REGSTR_VAL_ENABLEUNATTENDED",
    "REGSTR_VAL_ENCODENAME",
    "REGSTR_VAL_FAMILY",
    "REGSTR_VAL_FIXEDWIDTHFONT",
    "REGSTR_VAL_FIXED_FONT",
    "REGSTR_VAL_FONT_SCRIPT",
    "REGSTR_VAL_FONT_SCRIPTS",
    "REGSTR_VAL_FONT_SCRIPT_NAME",
    "REGSTR_VAL_FONT_SIZE",
    "REGSTR_VAL_FONT_SIZE_DEF",
    "REGSTR_VAL_HEADERCHARSET",
    "REGSTR_VAL_HTTP_ERRORS",
    "REGSTR_VAL_IE_CUSTOMCOLORS",
    "REGSTR_VAL_INETCPL_ADVANCEDTAB",
    "REGSTR_VAL_INETCPL_CONNECTIONSTAB",
    "REGSTR_VAL_INETCPL_CONTENTTAB",
    "REGSTR_VAL_INETCPL_GENERALTAB",
    "REGSTR_VAL_INETCPL_IEAK",
    "REGSTR_VAL_INETCPL_PRIVACYTAB",
    "REGSTR_VAL_INETCPL_PROGRAMSTAB",
    "REGSTR_VAL_INETCPL_SECURITYTAB",
    "REGSTR_VAL_INETENCODING",
    "REGSTR_VAL_INTERNETENTRY",
    "REGSTR_VAL_INTERNETENTRYBKUP",
    "REGSTR_VAL_INTERNETPROFILE",
    "REGSTR_VAL_JAVAJIT",
    "REGSTR_VAL_JAVAJIT_DEF",
    "REGSTR_VAL_JAVALOGGING",
    "REGSTR_VAL_JAVALOGGING_DEF",
    "REGSTR_VAL_LEVEL",
    "REGSTR_VAL_LOADIMAGES",
    "REGSTR_VAL_LOCALPAGE",
    "REGSTR_VAL_MOSDISCONNECT",
    "REGSTR_VAL_NEWDIRECTORY",
    "REGSTR_VAL_NONETAUTODIAL",
    "REGSTR_VAL_PLAYSOUNDS",
    "REGSTR_VAL_PLAYVIDEOS",
    "REGSTR_VAL_PRIVCONVERTER",
    "REGSTR_VAL_PROPORTIONALFONT",
    "REGSTR_VAL_PROP_FONT",
    "REGSTR_VAL_PROXYENABLE",
    "REGSTR_VAL_PROXYOVERRIDE",
    "REGSTR_VAL_PROXYSERVER",
    "REGSTR_VAL_REDIALATTEMPTS",
    "REGSTR_VAL_REDIALINTERVAL",
    "REGSTR_VAL_RNAINSTALLED",
    "REGSTR_VAL_SAFETYWARNINGLEVEL",
    "REGSTR_VAL_SCHANNELENABLEPROTOCOL",
    "REGSTR_VAL_SCHANNELENABLEPROTOCOL_DEF",
    "REGSTR_VAL_SCRIPT_FIXED_FONT",
    "REGSTR_VAL_SCRIPT_PROP_FONT",
    "REGSTR_VAL_SEARCHPAGE",
    "REGSTR_VAL_SECURITYACTICEXSCRIPTS",
    "REGSTR_VAL_SECURITYACTICEXSCRIPTS_DEF",
    "REGSTR_VAL_SECURITYACTIVEX",
    "REGSTR_VAL_SECURITYACTIVEX_DEF",
    "REGSTR_VAL_SECURITYALLOWCOOKIES",
    "REGSTR_VAL_SECURITYALLOWCOOKIES_DEF",
    "REGSTR_VAL_SECURITYDISABLECACHINGOFSSLPAGES",
    "REGSTR_VAL_SECURITYDISABLECACHINGOFSSLPAGES_DEF",
    "REGSTR_VAL_SECURITYJAVA",
    "REGSTR_VAL_SECURITYJAVA_DEF",
    "REGSTR_VAL_SECURITYWARNONBADCERTSENDING",
    "REGSTR_VAL_SECURITYWARNONBADCERTSENDING_DEF",
    "REGSTR_VAL_SECURITYWARNONBADCERTVIEWING",
    "REGSTR_VAL_SECURITYWARNONBADCERTVIEWING_DEF",
    "REGSTR_VAL_SECURITYWARNONSEND",
    "REGSTR_VAL_SECURITYWARNONSENDALWAYS",
    "REGSTR_VAL_SECURITYWARNONSENDALWAYS_DEF",
    "REGSTR_VAL_SECURITYWARNONSEND_DEF",
    "REGSTR_VAL_SECURITYWARNONVIEW",
    "REGSTR_VAL_SECURITYWARNONVIEW_DEF",
    "REGSTR_VAL_SECURITYWARNONZONECROSSING",
    "REGSTR_VAL_SECURITYWARNONZONECROSSING_DEF",
    "REGSTR_VAL_SHOWADDRESSBAR",
    "REGSTR_VAL_SHOWFOCUS",
    "REGSTR_VAL_SHOWFOCUS_DEF",
    "REGSTR_VAL_SHOWFULLURLS",
    "REGSTR_VAL_SHOWTOOLBAR",
    "REGSTR_VAL_SMOOTHSCROLL",
    "REGSTR_VAL_SMOOTHSCROLL_DEF",
    "REGSTR_VAL_STARTPAGE",
    "REGSTR_VAL_TEXTCOLOR",
    "REGSTR_VAL_TRUSTWARNINGLEVEL_HIGH",
    "REGSTR_VAL_TRUSTWARNINGLEVEL_LOW",
    "REGSTR_VAL_TRUSTWARNINGLEVEL_MED",
    "REGSTR_VAL_USEAUTOAPPEND",
    "REGSTR_VAL_USEAUTOCOMPLETE",
    "REGSTR_VAL_USEAUTOSUGGEST",
    "REGSTR_VAL_USEDLGCOLORS",
    "REGSTR_VAL_USEHOVERCOLOR",
    "REGSTR_VAL_USEIBAR",
    "REGSTR_VAL_USEICM",
    "REGSTR_VAL_USEICM_DEF",
    "REGSTR_VAL_USERAGENT",
    "REGSTR_VAL_USESTYLESHEETS",
    "REGSTR_VAL_USESTYLESHEETS_DEF",
    "REGSTR_VAL_VISIBLEBANDS",
    "REGSTR_VAL_VISIBLEBANDS_DEF",
    "REGSTR_VAL_WEBCHARSET",
    "RatingAccessDeniedDialog",
    "RatingAccessDeniedDialog2",
    "RatingAccessDeniedDialog2W",
    "RatingAccessDeniedDialogW",
    "RatingAddToApprovedSites",
    "RatingCheckUserAccess",
    "RatingCheckUserAccessW",
    "RatingClickedOnPRFInternal",
    "RatingClickedOnRATInternal",
    "RatingEnable",
    "RatingEnableW",
    "RatingEnabledQuery",
    "RatingFreeDetails",
    "RatingInit",
    "RatingObtainCancel",
    "RatingObtainQuery",
    "RatingObtainQueryW",
    "RatingSetupUI",
    "RatingSetupUIW",
    "SCMP_BOTTOM",
    "SCMP_FULL",
    "SCMP_LEFT",
    "SCMP_RIGHT",
    "SCMP_TOP",
    "SCROLLABLECONTEXTMENU_PLACEMENT",
    "STATURL",
    "STATURLFLAG_ISCACHED",
    "STATURLFLAG_ISTOPLEVEL",
    "STATURL_QUERYFLAG_ISCACHED",
    "STATURL_QUERYFLAG_NOTITLE",
    "STATURL_QUERYFLAG_NOURL",
    "STATURL_QUERYFLAG_TOPLEVEL",
    "SURFACE_LOCK_ALLOW_DISCARD",
    "SURFACE_LOCK_EXCLUSIVE",
    "SURFACE_LOCK_WAIT",
    "SZBACKBITMAP",
    "SZJAVAVMPATH",
    "SZNOTEXT",
    "SZTOOLBAR",
    "SZTRUSTWARNLEVEL",
    "SZVISIBLE",
    "SZ_IE_DEFAULT_HTML_EDITOR",
    "SZ_IE_IBAR",
    "SZ_IE_IBAR_BANDS",
    "SZ_IE_MAIN",
    "SZ_IE_SEARCHSTRINGS",
    "SZ_IE_SECURITY",
    "SZ_IE_SETTINGS",
    "SZ_IE_THRESHOLDS",
    "S_SURFACE_DISCARDED",
    "SniffStream",
    "TARGET_NOTIFY_OBJECT_NAME",
    "TF_NAVIGATE",
    "TIMERMODE_NORMAL",
    "TIMERMODE_VISIBILITYAWARE",
    "TOOLSBAND",
    "TSZCALENDARPROTOCOL",
    "TSZCALLTOPROTOCOL",
    "TSZINTERNETCLIENTSPATH",
    "TSZLDAPPROTOCOL",
    "TSZMAILTOPROTOCOL",
    "TSZMICROSOFTPATH",
    "TSZNEWSPROTOCOL",
    "TSZPROTOCOLSPATH",
    "TSZSCHANNELPATH",
    "TSZVSOURCEPROTOCOL",
    "msodsvFailed",
    "msodsvLowSecurityLevel",
    "msodsvNoMacros",
    "msodsvPassedTrusted",
    "msodsvPassedTrustedCert",
    "msodsvUnsigned",
    "msoedmDisable",
    "msoedmDontOpen",
    "msoedmEnable",
    "msoslHigh",
    "msoslMedium",
    "msoslNone",
    "msoslUndefined",
    "wfolders",
]
_arch_optional = [
]
