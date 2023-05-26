from __future__ import annotations
from ctypes import POINTER
from Windows import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
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
import Windows.Win32.System.Variant
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
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
ADDURL_FLAG = Int32
ADDURL_FIRST: ADDURL_FLAG = 0
ADDURL_ADDTOHISTORYANDCACHE: ADDURL_FLAG = 0
ADDURL_ADDTOCACHE: ADDURL_FLAG = 1
ADDURL_Max: ADDURL_FLAG = 2147483647
AnchorClick = Guid('{13d5413c-33b9-11d2-95a7-00c04f8ecb02}')
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
CATID_MSOfficeAntiVirus: Guid = Guid('{56ffcc30-d398-11d0-b2ae-00a0c908fa49}')
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
def IELaunchURL(lpwstrUrl: Windows.Win32.Foundation.PWSTR, lpProcInfo: POINTER(Windows.Win32.System.Threading.PROCESS_INFORMATION_head), lpInfo: VoidPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IERefreshElevationPolicy() -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IEGetProtectedModeCookie(lpszURL: Windows.Win32.Foundation.PWSTR, lpszCookieName: Windows.Win32.Foundation.PWSTR, lpszCookieData: Windows.Win32.Foundation.PWSTR, pcchCookieData: POINTER(UInt32), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IESetProtectedModeCookie(lpszURL: Windows.Win32.Foundation.PWSTR, lpszCookieName: Windows.Win32.Foundation.PWSTR, lpszCookieData: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IERegisterWritableRegistryKey(guid: Guid, lpSubkey: Windows.Win32.Foundation.PWSTR, fSubkeyAllowed: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IERegisterWritableRegistryValue(guid: Guid, lpPath: Windows.Win32.Foundation.PWSTR, lpValueName: Windows.Win32.Foundation.PWSTR, dwType: UInt32, lpData: POINTER(Byte), cbMaxData: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IEUnregisterWritableRegistry(guid: Guid) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IERegCreateKeyEx(lpSubKey: Windows.Win32.Foundation.PWSTR, Reserved: UInt32, lpClass: Windows.Win32.Foundation.PWSTR, dwOptions: UInt32, samDesired: UInt32, lpSecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), phkResult: POINTER(Windows.Win32.System.Registry.HKEY), lpdwDisposition: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IERegSetValueEx(lpSubKey: Windows.Win32.Foundation.PWSTR, lpValueName: Windows.Win32.Foundation.PWSTR, Reserved: UInt32, dwType: UInt32, lpData: POINTER(Byte), cbData: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
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
def IEGetFileAttributesEx(lpFileName: Windows.Win32.Foundation.PWSTR, fInfoLevelId: Windows.Win32.Storage.FileSystem.GET_FILEEX_INFO_LEVELS, lpFileInformation: VoidPtr) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('Ieframe.dll')
def IEFindFirstFile(lpFileName: Windows.Win32.Foundation.PWSTR, lpFindFileData: POINTER(Windows.Win32.Storage.FileSystem.WIN32_FIND_DATAA_head)) -> Windows.Win32.Foundation.HANDLE: ...
@winfunctype('MSRATING.dll')
def RatingEnable(hwndParent: Windows.Win32.Foundation.HWND, pszUsername: Windows.Win32.Foundation.PSTR, fEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingEnableW(hwndParent: Windows.Win32.Foundation.HWND, pszUsername: Windows.Win32.Foundation.PWSTR, fEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingCheckUserAccess(pszUsername: Windows.Win32.Foundation.PSTR, pszURL: Windows.Win32.Foundation.PSTR, pszRatingInfo: Windows.Win32.Foundation.PSTR, pData: POINTER(Byte), cbData: UInt32, ppRatingDetails: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingCheckUserAccessW(pszUsername: Windows.Win32.Foundation.PWSTR, pszURL: Windows.Win32.Foundation.PWSTR, pszRatingInfo: Windows.Win32.Foundation.PWSTR, pData: POINTER(Byte), cbData: UInt32, ppRatingDetails: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingAccessDeniedDialog(hDlg: Windows.Win32.Foundation.HWND, pszUsername: Windows.Win32.Foundation.PSTR, pszContentDescription: Windows.Win32.Foundation.PSTR, pRatingDetails: VoidPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingAccessDeniedDialogW(hDlg: Windows.Win32.Foundation.HWND, pszUsername: Windows.Win32.Foundation.PWSTR, pszContentDescription: Windows.Win32.Foundation.PWSTR, pRatingDetails: VoidPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingAccessDeniedDialog2(hDlg: Windows.Win32.Foundation.HWND, pszUsername: Windows.Win32.Foundation.PSTR, pRatingDetails: VoidPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingAccessDeniedDialog2W(hDlg: Windows.Win32.Foundation.HWND, pszUsername: Windows.Win32.Foundation.PWSTR, pRatingDetails: VoidPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingFreeDetails(pRatingDetails: VoidPtr) -> Windows.Win32.Foundation.HRESULT: ...
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
def RatingAddToApprovedSites(hDlg: Windows.Win32.Foundation.HWND, cbPasswordBlob: UInt32, pbPasswordBlob: POINTER(Byte), lpszUrl: Windows.Win32.Foundation.PWSTR, fAlwaysNever: Windows.Win32.Foundation.BOOL, fSitePage: Windows.Win32.Foundation.BOOL, fApprovedSitesEnforced: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
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
def IdentifyMIMEType(pbBytes: POINTER(Byte), nBytes: UInt32, pnFormat: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ImgUtil.dll')
def ComputeInvCMAP(pRGBColors: POINTER(Windows.Win32.Graphics.Gdi.RGBQUAD_head), nColors: UInt32, pInvTable: POINTER(Byte), cbTable: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ImgUtil.dll')
def DitherTo8(pDestBits: POINTER(Byte), nDestPitch: Int32, pSrcBits: POINTER(Byte), nSrcPitch: Int32, bfidSrc: POINTER(Guid), prgbDestColors: POINTER(Windows.Win32.Graphics.Gdi.RGBQUAD_head), prgbSrcColors: POINTER(Windows.Win32.Graphics.Gdi.RGBQUAD_head), pbDestInvMap: POINTER(Byte), x: Int32, y: Int32, cx: Int32, cy: Int32, lDestTrans: Int32, lSrcTrans: Int32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ImgUtil.dll')
def CreateDDrawSurfaceOnDIB(hbmDib: Windows.Win32.Graphics.Gdi.HBITMAP, ppSurface: POINTER(Windows.Win32.Graphics.DirectDraw.IDirectDrawSurface_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ImgUtil.dll')
def DecodeImageEx(pStream: Windows.Win32.System.Com.IStream_head, pMap: Windows.Win32.Web.InternetExplorer.IMapMIMEToCLSID_head, pEventSink: Windows.Win32.System.Com.IUnknown_head, pszMIMETypeParam: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
CDeviceRect = Guid('{3050f6d4-98b5-11cf-bb82-00aa00bdce0b}')
CDownloadBehavior = Guid('{3050f5be-98b5-11cf-bb82-00aa00bdce0b}')
CHeaderFooter = Guid('{3050f6cd-98b5-11cf-bb82-00aa00bdce0b}')
CLayoutRect = Guid('{3050f664-98b5-11cf-bb82-00aa00bdce0b}')
CPersistDataPeer = Guid('{3050f487-98b5-11cf-bb82-00aa00bdce0b}')
CPersistHistory = Guid('{3050f4c8-98b5-11cf-bb82-00aa00bdce0b}')
CPersistShortcut = Guid('{3050f4c6-98b5-11cf-bb82-00aa00bdce0b}')
CPersistSnapshot = Guid('{3050f4c9-98b5-11cf-bb82-00aa00bdce0b}')
CPersistUserData = Guid('{3050f48e-98b5-11cf-bb82-00aa00bdce0b}')
CoDitherToRGB8 = Guid('{a860ce50-3910-11d0-86fc-00a0c913f750}')
CoMapMIMEToCLSID = Guid('{30c3b080-30fb-11d0-b724-00aa006c1a01}')
CoSniffStream = Guid('{6a01fda0-30df-11d0-b724-00aa006c1a01}')
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
HomePage = Guid('{766bf2ae-d650-11d1-9811-00c04fc31d2e}')
HomePageSetting = Guid('{374cede0-873a-4c4f-bc86-bcc8cf5116a3}')
class IActiveXUIHandlerSite(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{30510853-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(3)
    def CreateScrollableContextMenu(self, scrollableContextMenu: POINTER(Windows.Win32.Web.InternetExplorer.IScrollableContextMenu_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PickFileAndGetResult(self, filePicker: Windows.Win32.System.Com.IUnknown_head, allowMultipleSelections: Windows.Win32.Foundation.BOOL, result: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IActiveXUIHandlerSite2(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7e3707b2-d087-4542-ac1f-a0d2fcd080fd}')
    @commethod(3)
    def AddSuspensionExemption(self, pullCookie: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveSuspensionExemption(self, ullCookie: UInt64) -> Windows.Win32.Foundation.HRESULT: ...
class IActiveXUIHandlerSite3(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7904009a-1238-47f4-901c-871375c34608}')
    @commethod(3)
    def MessageBoxW(self, hwnd: Windows.Win32.Foundation.HWND, text: Windows.Win32.Foundation.PWSTR, caption: Windows.Win32.Foundation.PWSTR, type: UInt32, result: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IAnchorClick(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{13d5413b-33b9-11d2-95a7-00c04f8ecb02}')
    @commethod(7)
    def ProcOnClick(self) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioSessionSite(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d7d8b684-d02d-4517-b6b7-19e3dfe29c45}')
    @commethod(3)
    def GetAudioSessionGuid(self, audioSessionGuid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnAudioStreamCreated(self, endpointID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnAudioStreamDestroyed(self, endpointID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ICaretPositionProvider(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{58da43a2-108e-4d5b-9f75-e5f74f93fff5}')
    @commethod(3)
    def GetCaretPosition(self, pptCaret: POINTER(Windows.Win32.Foundation.POINT_head), pflHeight: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
class IDeviceRect(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{3050f6d5-98b5-11cf-bb82-00aa00bdce0b}')
class IDithererImpl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7c48e840-3910-11d0-86fc-00a0c913f750}')
    @commethod(3)
    def SetDestColorTable(self, nColors: UInt32, prgbColors: POINTER(Windows.Win32.Graphics.Gdi.RGBQUAD_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetEventSink(self, pEventSink: Windows.Win32.Web.InternetExplorer.IImageDecodeEventSink_head) -> Windows.Win32.Foundation.HRESULT: ...
class IDocObjectService(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3050f801-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(3)
    def FireBeforeNavigate2(self, pDispatch: Windows.Win32.System.Com.IDispatch_head, lpszUrl: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, lpszFrameName: Windows.Win32.Foundation.PWSTR, pPostData: POINTER(Byte), cbPostData: UInt32, lpszHeaders: Windows.Win32.Foundation.PWSTR, fPlayNavSound: Windows.Win32.Foundation.BOOL, pfCancel: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FireNavigateComplete2(self, pHTMLWindow2: Windows.Win32.Web.MsHtml.IHTMLWindow2_head, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def FireDownloadBegin(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FireDownloadComplete(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FireDocumentComplete(self, pHTMLWindow: Windows.Win32.Web.MsHtml.IHTMLWindow2_head, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def UpdateDesktopComponent(self, pHTMLWindow: Windows.Win32.Web.MsHtml.IHTMLWindow2_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetPendingUrl(self, pbstrPendingUrl: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ActiveElementChanged(self, pHTMLElement: Windows.Win32.Web.MsHtml.IHTMLElement_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetUrlSearchComponent(self, pbstrSearch: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def IsErrorUrl(self, lpszUrl: Windows.Win32.Foundation.PWSTR, pfIsError: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IDownloadBehavior(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{3050f5bd-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(7)
    def startDownload(self, bstrUrl: Windows.Win32.Foundation.BSTR, pdispCallback: Windows.Win32.System.Com.IDispatch_head) -> Windows.Win32.Foundation.HRESULT: ...
class IDownloadManager(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{988934a4-064b-11d3-bb80-00104b35e7f9}')
    @commethod(3)
    def Download(self, pmk: Windows.Win32.System.Com.IMoniker_head, pbc: Windows.Win32.System.Com.IBindCtx_head, dwBindVerb: UInt32, grfBINDF: Int32, pBindInfo: POINTER(Windows.Win32.System.Com.BINDINFO_head), pszHeaders: Windows.Win32.Foundation.PWSTR, pszRedir: Windows.Win32.Foundation.PWSTR, uiCP: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
IELAUNCHOPTION_FLAGS = Int32
IELAUNCHOPTION_SCRIPTDEBUG: IELAUNCHOPTION_FLAGS = 1
IELAUNCHOPTION_FORCE_COMPAT: IELAUNCHOPTION_FLAGS = 2
IELAUNCHOPTION_FORCE_EDGE: IELAUNCHOPTION_FLAGS = 4
IELAUNCHOPTION_LOCK_ENGINE: IELAUNCHOPTION_FLAGS = 8
class IELAUNCHURLINFO(EasyCastStructure):
    cbSize: UInt32
    dwCreationFlags: UInt32
    dwLaunchOptionFlags: UInt32
IEWebDriverManager = Guid('{90314af2-5250-47b3-89d8-6295fc23bc22}')
class IEnumManagerFrames(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3caa826a-9b1f-4a79-bc81-f0430ded1648}')
    @commethod(3)
    def Next(self, celt: UInt32, ppWindows: POINTER(POINTER(Windows.Win32.Foundation.HWND)), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Count(self, pcelt: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Clone(self, ppEnum: POINTER(Windows.Win32.Web.InternetExplorer.IEnumManagerFrames_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumOpenServiceActivity(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a436d7d2-17c3-4ef4-a1e8-5c86faff26c0}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(Windows.Win32.Web.InternetExplorer.IOpenServiceActivity_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(Windows.Win32.Web.InternetExplorer.IEnumOpenServiceActivity_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumOpenServiceActivityCategory(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{33627a56-8c9a-4430-8fd1-b5f5c771afb6}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(Windows.Win32.Web.InternetExplorer.IOpenServiceActivityCategory_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(Windows.Win32.Web.InternetExplorer.IEnumOpenServiceActivityCategory_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEnumSTATURL(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3c374a42-bae4-11cf-bf7d-00aa006946ee}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(Windows.Win32.Web.InternetExplorer.STATURL_head), pceltFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(Windows.Win32.Web.InternetExplorer.IEnumSTATURL_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetFilter(self, poszFilter: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IExtensionValidation(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7d33f73d-8525-4e0f-87db-830288baff44}')
    @commethod(3)
    def Validate(self, extensionGuid: POINTER(Guid), extensionModulePath: Windows.Win32.Foundation.PWSTR, extensionFileVersionMS: UInt32, extensionFileVersionLS: UInt32, htmlDocumentTop: Windows.Win32.Web.MsHtml.IHTMLDocument2_head, htmlDocumentSubframe: Windows.Win32.Web.MsHtml.IHTMLDocument2_head, htmlElement: Windows.Win32.Web.MsHtml.IHTMLElement_head, contexts: Windows.Win32.Web.InternetExplorer.ExtensionValidationContexts, results: POINTER(Windows.Win32.Web.InternetExplorer.ExtensionValidationResults)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DisplayName(self, displayName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IHTMLPersistData(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3050f4c5-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(3)
    def save(self, pUnk: Windows.Win32.System.Com.IUnknown_head, lType: Int32, fContinueBroacast: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def load(self, pUnk: Windows.Win32.System.Com.IUnknown_head, lType: Int32, fDoDefault: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def queryType(self, lType: Int32, pfSupportsType: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IHTMLPersistDataOM(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{3050f4c0-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(7)
    def get_XMLDocument(self, p: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def getAttribute(self, name: Windows.Win32.Foundation.BSTR, pValue: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def setAttribute(self, name: Windows.Win32.Foundation.BSTR, value: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def removeAttribute(self, name: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IHTMLUserDataOM(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{3050f48f-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(7)
    def get_XMLDocument(self, p: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def save(self, strName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def load(self, strName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def getAttribute(self, name: Windows.Win32.Foundation.BSTR, pValue: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def setAttribute(self, name: Windows.Win32.Foundation.BSTR, value: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def removeAttribute(self, name: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_expires(self, bstr: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_expires(self, pbstr: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IHeaderFooter(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{3050f6ce-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(7)
    def get_htmlHead(self, p: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_htmlFoot(self, p: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_textHead(self, v: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_textHead(self, p: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_textFoot(self, v: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_textFoot(self, p: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_page(self, v: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_page(self, p: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_pageTotal(self, v: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_pageTotal(self, p: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_URL(self, v: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_URL(self, p: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_title(self, v: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_title(self, p: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_dateShort(self, v: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_dateShort(self, p: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_dateLong(self, v: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_dateLong(self, p: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_timeShort(self, v: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_timeShort(self, p: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_timeLong(self, v: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_timeLong(self, p: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IHeaderFooter2(ComPtr):
    extends: Windows.Win32.Web.InternetExplorer.IHeaderFooter
    _iid_ = Guid('{305104a5-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(29)
    def put_font(self, v: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_font(self, p: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IHomePage(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{766bf2af-d650-11d1-9811-00c04fc31d2e}')
    @commethod(7)
    def navigateHomePage(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def setHomePage(self, bstrURL: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def isHomePage(self, bstrURL: Windows.Win32.Foundation.BSTR, p: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IHomePageSetting(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fdfc244f-18fa-4ff2-b08e-1d618f3ffbe4}')
    @commethod(3)
    def SetHomePage(self, hwnd: Windows.Win32.Foundation.HWND, homePageUri: Windows.Win32.Foundation.PWSTR, brandingMessage: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsHomePage(self, uri: Windows.Win32.Foundation.PWSTR, isDefault: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetHomePageToBrowserDefault(self) -> Windows.Win32.Foundation.HRESULT: ...
class IIEWebDriverManager(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{bd1dc630-6590-4ca2-a293-6bc72b2438d8}')
    @commethod(7)
    def ExecuteCommand(self, command: Windows.Win32.Foundation.PWSTR, response: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IIEWebDriverSite(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{ffb84444-453d-4fbc-9f9d-8db5c471ec75}')
    @commethod(7)
    def WindowOperation(self, operationCode: UInt32, hWnd: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def DetachWebdriver(self, pUnkWD: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCapabilityValue(self, pUnkWD: Windows.Win32.System.Com.IUnknown_head, capName: Windows.Win32.Foundation.PWSTR, capValue: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IImageDecodeEventSink(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{baa342a0-2ded-11d0-86f4-00a0c913f750}')
    @commethod(3)
    def GetSurface(self, nWidth: Int32, nHeight: Int32, bfid: POINTER(Guid), nPasses: UInt32, dwHints: UInt32, ppSurface: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnBeginDecode(self, pdwEvents: POINTER(UInt32), pnFormats: POINTER(UInt32), ppFormats: POINTER(POINTER(Guid))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnBitsComplete(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnDecodeComplete(self, hrStatus: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnPalette(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnProgress(self, pBounds: POINTER(Windows.Win32.Foundation.RECT_head), bComplete: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IImageDecodeEventSink2(ComPtr):
    extends: Windows.Win32.Web.InternetExplorer.IImageDecodeEventSink
    _iid_ = Guid('{8ebd8a57-8a96-48c9-84a6-962e2db9c931}')
    @commethod(9)
    def IsAlphaPremultRequired(self, pfPremultAlpha: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IImageDecodeFilter(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a3ccedf3-2de2-11d0-86f4-00a0c913f750}')
    @commethod(3)
    def Initialize(self, pEventSink: Windows.Win32.Web.InternetExplorer.IImageDecodeEventSink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Process(self, pStream: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Terminate(self, hrStatus: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
class IIntelliForms(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{9b9f68e6-1aaa-11d2-bca5-00c04fd929db}')
    @commethod(7)
    def get_enabled(self, pVal: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_enabled(self, bVal: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IInternetExplorerManager(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{acc84351-04ff-44f9-b23f-655ed168c6d5}')
    @commethod(3)
    def CreateObject(self, dwConfig: UInt32, pszURL: Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
class IInternetExplorerManager2(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dfbb5136-9259-4895-b4a7-c1934429919a}')
    @commethod(3)
    def EnumFrameWindows(self, ppEnum: POINTER(Windows.Win32.Web.InternetExplorer.IEnumManagerFrames_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ILayoutRect(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{3050f665-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(7)
    def put_nextRect(self, bstrElementId: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_nextRect(self, pbstrElementId: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_contentSrc(self, varContentSrc: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_contentSrc(self, pvarContentSrc: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_honorPageBreaks(self, v: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_honorPageBreaks(self, p: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_honorPageRules(self, v: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_honorPageRules(self, p: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_nextRectElement(self, pElem: Windows.Win32.System.Com.IDispatch_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_nextRectElement(self, ppElem: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_contentDocument(self, pDoc: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMapMIMEToCLSID(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d9e89500-30fa-11d0-b724-00aa006c1a01}')
    @commethod(3)
    def EnableDefaultMappings(self, bEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MapMIMEToCLSID(self, pszMIMEType: Windows.Win32.Foundation.PWSTR, pCLSID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetMapping(self, pszMIMEType: Windows.Win32.Foundation.PWSTR, dwMapMode: UInt32, clsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IMediaActivityNotifySite(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8165cfef-179d-46c2-bc71-3fa726dc1f8d}')
    @commethod(3)
    def OnMediaActivityStarted(self, mediaActivityType: Windows.Win32.Web.InternetExplorer.MEDIA_ACTIVITY_NOTIFY_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnMediaActivityStopped(self, mediaActivityType: Windows.Win32.Web.InternetExplorer.MEDIA_ACTIVITY_NOTIFY_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
INTERNETEXPLORERCONFIGURATION = Int32
INTERNETEXPLORERCONFIGURATION_HOST: INTERNETEXPLORERCONFIGURATION = 1
INTERNETEXPLORERCONFIGURATION_WEB_DRIVER: INTERNETEXPLORERCONFIGURATION = 2
INTERNETEXPLORERCONFIGURATION_WEB_DRIVER_EDGE: INTERNETEXPLORERCONFIGURATION = 4
class IOpenService(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c2952ed1-6a89-4606-925f-1ed8b4be0630}')
    @commethod(3)
    def IsDefault(self, pfIsDefault: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetDefault(self, fDefault: Windows.Win32.Foundation.BOOL, hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetID(self, pbstrID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpenServiceActivity(ComPtr):
    extends: Windows.Win32.Web.InternetExplorer.IOpenService
    _iid_ = Guid('{13645c88-221a-4905-8ed1-4f5112cfc108}')
    @commethod(6)
    def Execute(self, pInput: Windows.Win32.Web.InternetExplorer.IOpenServiceActivityInput_head, pOutput: Windows.Win32.Web.InternetExplorer.IOpenServiceActivityOutputContext_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CanExecute(self, pInput: Windows.Win32.Web.InternetExplorer.IOpenServiceActivityInput_head, pOutput: Windows.Win32.Web.InternetExplorer.IOpenServiceActivityOutputContext_head, pfCanExecute: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CanExecuteType(self, type: Windows.Win32.Web.InternetExplorer.OpenServiceActivityContentType, pfCanExecute: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Preview(self, pInput: Windows.Win32.Web.InternetExplorer.IOpenServiceActivityInput_head, pOutput: Windows.Win32.Web.InternetExplorer.IOpenServiceActivityOutputContext_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CanPreview(self, pInput: Windows.Win32.Web.InternetExplorer.IOpenServiceActivityInput_head, pOutput: Windows.Win32.Web.InternetExplorer.IOpenServiceActivityOutputContext_head, pfCanPreview: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CanPreviewType(self, type: Windows.Win32.Web.InternetExplorer.OpenServiceActivityContentType, pfCanPreview: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetStatusText(self, pInput: Windows.Win32.Web.InternetExplorer.IOpenServiceActivityInput_head, pbstrStatusText: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetHomepageUrl(self, pbstrHomepageUrl: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetDisplayName(self, pbstrDisplayName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetDescription(self, pbstrDescription: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetCategoryName(self, pbstrCategoryName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetIconPath(self, pbstrIconPath: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetIcon(self, fSmallIcon: Windows.Win32.Foundation.BOOL, phIcon: POINTER(Windows.Win32.UI.WindowsAndMessaging.HICON)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetDescriptionFilePath(self, pbstrXmlPath: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetDownloadUrl(self, pbstrXmlUri: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetInstallUrl(self, pbstrInstallUri: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def IsEnabled(self, pfIsEnabled: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetEnabled(self, fEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IOpenServiceActivityCategory(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{850af9d6-7309-40b5-bdb8-786c106b2153}')
    @commethod(3)
    def HasDefaultActivity(self, pfHasDefaultActivity: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDefaultActivity(self, ppDefaultActivity: POINTER(Windows.Win32.Web.InternetExplorer.IOpenServiceActivity_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetDefaultActivity(self, pActivity: Windows.Win32.Web.InternetExplorer.IOpenServiceActivity_head, hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetName(self, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetActivityEnumerator(self, pInput: Windows.Win32.Web.InternetExplorer.IOpenServiceActivityInput_head, pOutput: Windows.Win32.Web.InternetExplorer.IOpenServiceActivityOutputContext_head, ppEnumActivity: POINTER(Windows.Win32.Web.InternetExplorer.IEnumOpenServiceActivity_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpenServiceActivityInput(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{75cb4db9-6da0-4da3-83ce-422b6a433346}')
    @commethod(3)
    def GetVariable(self, pwzVariableName: Windows.Win32.Foundation.PWSTR, pwzVariableType: Windows.Win32.Foundation.PWSTR, pbstrVariableContent: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def HasVariable(self, pwzVariableName: Windows.Win32.Foundation.PWSTR, pwzVariableType: Windows.Win32.Foundation.PWSTR, pfHasVariable: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetType(self, pType: POINTER(Windows.Win32.Web.InternetExplorer.OpenServiceActivityContentType)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpenServiceActivityManager(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8a2d0a9d-e920-4bdc-a291-d30f650bc4f1}')
    @commethod(3)
    def GetCategoryEnumerator(self, eType: Windows.Win32.Web.InternetExplorer.OpenServiceActivityContentType, ppEnum: POINTER(Windows.Win32.Web.InternetExplorer.IEnumOpenServiceActivityCategory_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetActivityByID(self, pwzActivityID: Windows.Win32.Foundation.PWSTR, ppActivity: POINTER(Windows.Win32.Web.InternetExplorer.IOpenServiceActivity_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetActivityByHomepageAndCategory(self, pwzHomepage: Windows.Win32.Foundation.PWSTR, pwzCategory: Windows.Win32.Foundation.PWSTR, ppActivity: POINTER(Windows.Win32.Web.InternetExplorer.IOpenServiceActivity_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetVersionCookie(self, pdwVersionCookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpenServiceActivityOutputContext(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e289deab-f709-49a9-b99e-282364074571}')
    @commethod(3)
    def Navigate(self, pwzUri: Windows.Win32.Foundation.PWSTR, pwzMethod: Windows.Win32.Foundation.PWSTR, pwzHeaders: Windows.Win32.Foundation.PWSTR, pPostData: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CanNavigate(self, pwzUri: Windows.Win32.Foundation.PWSTR, pwzMethod: Windows.Win32.Foundation.PWSTR, pwzHeaders: Windows.Win32.Foundation.PWSTR, pPostData: Windows.Win32.System.Com.IStream_head, pfCanNavigate: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IOpenServiceManager(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5664125f-4e10-4e90-98e4-e4513d955a14}')
    @commethod(3)
    def InstallService(self, pwzServiceUrl: Windows.Win32.Foundation.PWSTR, ppService: POINTER(Windows.Win32.Web.InternetExplorer.IOpenService_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UninstallService(self, pService: Windows.Win32.Web.InternetExplorer.IOpenService_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetServiceByID(self, pwzID: Windows.Win32.Foundation.PWSTR, ppService: POINTER(Windows.Win32.Web.InternetExplorer.IOpenService_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPeerFactory(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6663f9d3-b482-11d1-89c6-00c04fb6bfc4}')
class IPersistHistory(ComPtr):
    extends: Windows.Win32.System.Com.IPersist
    _iid_ = Guid('{91a565c1-e38f-11d0-94bf-00a0c9055cbf}')
    @commethod(4)
    def LoadHistory(self, pStream: Windows.Win32.System.Com.IStream_head, pbc: Windows.Win32.System.Com.IBindCtx_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SaveHistory(self, pStream: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetPositionCookie(self, dwPositioncookie: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPositionCookie(self, pdwPositioncookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IPrintTaskRequestFactory(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bb516745-8c34-4f8b-9605-684dcb144be5}')
    @commethod(3)
    def CreatePrintTaskRequest(self, pPrintTaskRequestHandler: Windows.Win32.Web.InternetExplorer.IPrintTaskRequestHandler_head) -> Windows.Win32.Foundation.HRESULT: ...
class IPrintTaskRequestHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{191cd340-cf36-44ff-bd53-d1b701799d9b}')
    @commethod(3)
    def HandlePrintTaskRequest(self, pPrintTaskRequest: Windows.Win32.System.WinRT.IInspectable_head) -> Windows.Win32.Foundation.HRESULT: ...
class IScrollableContextMenu(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{30510854-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(3)
    def AddItem(self, itemText: Windows.Win32.Foundation.PWSTR, cmdID: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ShowModal(self, x: Int32, y: Int32, cmdID: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IScrollableContextMenu2(ComPtr):
    extends: Windows.Win32.Web.InternetExplorer.IScrollableContextMenu
    _iid_ = Guid('{f77e9056-8674-4936-924c-0e4a06fa634a}')
    @commethod(5)
    def AddSeparator(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetPlacement(self, scmp: Windows.Win32.Web.InternetExplorer.SCROLLABLECONTEXTMENU_PLACEMENT) -> Windows.Win32.Foundation.HRESULT: ...
class ISniffStream(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4ef17940-30e0-11d0-b724-00aa006c1a01}')
    @commethod(3)
    def Init(self, pStream: Windows.Win32.System.Com.IStream_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Peek(self, pBuffer: VoidPtr, nBytes: UInt32, pnBytesRead: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ISurfacePresenterFlip(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{30510848-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(3)
    def Present(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetBuffer(self, backBufferIndex: UInt32, riid: POINTER(Guid), ppBuffer: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
class ISurfacePresenterFlip2(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{30510865-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(3)
    def SetRotation(self, dxgiRotation: Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_ROTATION) -> Windows.Win32.Foundation.HRESULT: ...
class ISurfacePresenterFlipBuffer(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e43f4a08-8bbc-4665-ac92-c55ce61fd7e7}')
    @commethod(3)
    def BeginDraw(self, riid: POINTER(Guid), ppBuffer: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EndDraw(self) -> Windows.Win32.Foundation.HRESULT: ...
class ITargetContainer(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7847ec01-2bec-11d0-82b4-00a0c90c29c5}')
    @commethod(3)
    def GetFrameUrl(self, ppszFrameSrc: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFramesContainer(self, ppContainer: POINTER(Windows.Win32.System.Ole.IOleContainer_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITargetEmbedding(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{548793c0-9e74-11cf-9655-00a0c9034923}')
    @commethod(3)
    def GetTargetFrame(self, ppTargetFrame: POINTER(Windows.Win32.Web.InternetExplorer.ITargetFrame_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITargetFrame(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d5f78c80-5252-11cf-90fa-00aa0042106e}')
    @commethod(3)
    def SetFrameName(self, pszFrameName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFrameName(self, ppszFrameName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetParentFrame(self, ppunkParent: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FindFrame(self, pszTargetName: Windows.Win32.Foundation.PWSTR, ppunkContextFrame: Windows.Win32.System.Com.IUnknown_head, dwFlags: UInt32, ppunkTargetFrame: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetFrameSrc(self, pszFrameSrc: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetFrameSrc(self, ppszFrameSrc: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFramesContainer(self, ppContainer: POINTER(Windows.Win32.System.Ole.IOleContainer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetFrameOptions(self, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetFrameOptions(self, pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetFrameMargins(self, dwWidth: UInt32, dwHeight: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetFrameMargins(self, pdwWidth: POINTER(UInt32), pdwHeight: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def RemoteNavigate(self, cLength: UInt32, pulData: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def OnChildFrameActivate(self, pUnkChildFrame: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def OnChildFrameDeactivate(self, pUnkChildFrame: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class ITargetFrame2(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{86d52e11-94a8-11d0-82af-00c04fd5ae38}')
    @commethod(3)
    def SetFrameName(self, pszFrameName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFrameName(self, ppszFrameName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetParentFrame(self, ppunkParent: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetFrameSrc(self, pszFrameSrc: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFrameSrc(self, ppszFrameSrc: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetFramesContainer(self, ppContainer: POINTER(Windows.Win32.System.Ole.IOleContainer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetFrameOptions(self, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFrameOptions(self, pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetFrameMargins(self, dwWidth: UInt32, dwHeight: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetFrameMargins(self, pdwWidth: POINTER(UInt32), pdwHeight: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def FindFrame(self, pszTargetName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, ppunkTargetFrame: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetTargetAlias(self, pszTargetName: Windows.Win32.Foundation.PWSTR, ppszTargetAlias: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ITargetFramePriv(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9216e421-2bf5-11d0-82b4-00a0c90c29c5}')
    @commethod(3)
    def FindFrameDownwards(self, pszTargetName: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, ppunkTargetFrame: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FindFrameInContext(self, pszTargetName: Windows.Win32.Foundation.PWSTR, punkContextFrame: Windows.Win32.System.Com.IUnknown_head, dwFlags: UInt32, ppunkTargetFrame: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnChildFrameActivate(self, pUnkChildFrame: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnChildFrameDeactivate(self, pUnkChildFrame: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def NavigateHack(self, grfHLNF: UInt32, pbc: Windows.Win32.System.Com.IBindCtx_head, pibsc: Windows.Win32.System.Com.IBindStatusCallback_head, pszTargetName: Windows.Win32.Foundation.PWSTR, pszUrl: Windows.Win32.Foundation.PWSTR, pszLocation: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def FindBrowserByIndex(self, dwID: UInt32, ppunkBrowser: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITargetFramePriv2(ComPtr):
    extends: Windows.Win32.Web.InternetExplorer.ITargetFramePriv
    _iid_ = Guid('{b2c867e6-69d6-46f2-a611-ded9a4bd7fef}')
    @commethod(9)
    def AggregatedNavigation2(self, grfHLNF: UInt32, pbc: Windows.Win32.System.Com.IBindCtx_head, pibsc: Windows.Win32.System.Com.IBindStatusCallback_head, pszTargetName: Windows.Win32.Foundation.PWSTR, pUri: Windows.Win32.System.Com.IUri_head, pszLocation: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class ITargetNotify(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{863a99a0-21bc-11d0-82b4-00a0c90c29c5}')
    @commethod(3)
    def OnCreate(self, pUnkDestination: Windows.Win32.System.Com.IUnknown_head, cbCookie: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnReuse(self, pUnkDestination: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class ITargetNotify2(ComPtr):
    extends: Windows.Win32.Web.InternetExplorer.ITargetNotify
    _iid_ = Guid('{3050f6b1-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(5)
    def GetOptionString(self, pbstrOptions: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class ITimer(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3050f360-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(3)
    def Advise(self, vtimeMin: Windows.Win32.System.Variant.VARIANT, vtimeMax: Windows.Win32.System.Variant.VARIANT, vtimeInterval: Windows.Win32.System.Variant.VARIANT, dwFlags: UInt32, pTimerSink: Windows.Win32.Web.InternetExplorer.ITimerSink_head, pdwCookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unadvise(self, dwCookie: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Freeze(self, fFreeze: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTime(self, pvtime: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ITimerEx(ComPtr):
    extends: Windows.Win32.Web.InternetExplorer.ITimer
    _iid_ = Guid('{30510414-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(7)
    def SetMode(self, dwMode: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ITimerService(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3050f35f-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(3)
    def CreateTimer(self, pReferenceTimer: Windows.Win32.Web.InternetExplorer.ITimer_head, ppNewTimer: POINTER(Windows.Win32.Web.InternetExplorer.ITimer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNamedTimer(self, rguidName: POINTER(Guid), ppTimer: POINTER(Windows.Win32.Web.InternetExplorer.ITimer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetNamedTimerReference(self, rguidName: POINTER(Guid), pReferenceTimer: Windows.Win32.Web.InternetExplorer.ITimer_head) -> Windows.Win32.Foundation.HRESULT: ...
class ITimerSink(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3050f361-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(3)
    def OnTimer(self, vtimeAdvise: Windows.Win32.System.Variant.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
class ITridentTouchInput(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{30510850-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(3)
    def OnPointerMessage(self, msg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM, pfAllowManipulations: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class ITridentTouchInputSite(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{30510849-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(3)
    def SetManipulationMode(self, msTouchAction: Windows.Win32.Web.MsHtml.styleMsTouchAction) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ZoomToPoint(self, x: Int32, y: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IUrlHistoryNotify(ComPtr):
    extends: Windows.Win32.System.Ole.IOleCommandTarget
    _iid_ = Guid('{bc40bec1-c493-11d0-831b-00c04fd5ae38}')
class IUrlHistoryStg(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3c374a41-bae4-11cf-bf7d-00aa006946ee}')
    @commethod(3)
    def AddUrl(self, pocsUrl: Windows.Win32.Foundation.PWSTR, pocsTitle: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DeleteUrl(self, pocsUrl: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def QueryUrl(self, pocsUrl: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, lpSTATURL: POINTER(Windows.Win32.Web.InternetExplorer.STATURL_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def BindToObject(self, pocsUrl: Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppvOut: POINTER(VoidPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EnumUrls(self, ppEnum: POINTER(Windows.Win32.Web.InternetExplorer.IEnumSTATURL_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUrlHistoryStg2(ComPtr):
    extends: Windows.Win32.Web.InternetExplorer.IUrlHistoryStg
    _iid_ = Guid('{afa0dc11-c313-11d0-831a-00c04fd5ae38}')
    @commethod(8)
    def AddUrlAndNotify(self, pocsUrl: Windows.Win32.Foundation.PWSTR, pocsTitle: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, fWriteHistory: Windows.Win32.Foundation.BOOL, poctNotify: Windows.Win32.System.Ole.IOleCommandTarget_head, punkISFolder: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ClearHistory(self) -> Windows.Win32.Foundation.HRESULT: ...
class IViewObjectPresentFlip(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{30510847-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(3)
    def NotifyRender(self, fRecreatePresenter: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RenderObjectToBitmap(self, pBitmap: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RenderObjectToSharedBuffer(self, pBuffer: Windows.Win32.Web.InternetExplorer.ISurfacePresenterFlipBuffer_head) -> Windows.Win32.Foundation.HRESULT: ...
class IViewObjectPresentFlip2(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{30510856-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(3)
    def NotifyLeavingView(self) -> Windows.Win32.Foundation.HRESULT: ...
class IViewObjectPresentFlipSite(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{30510846-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(3)
    def CreateSurfacePresenterFlip(self, pDevice: Windows.Win32.System.Com.IUnknown_head, width: UInt32, height: UInt32, backBufferCount: UInt32, format: Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT, mode: Windows.Win32.Web.MsHtml.VIEW_OBJECT_ALPHA_MODE, ppSPFlip: POINTER(Windows.Win32.Web.InternetExplorer.ISurfacePresenterFlip_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDeviceLuid(self, pLuid: POINTER(Windows.Win32.Foundation.LUID_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnterFullScreen(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ExitFullScreen(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsFullScreen(self, pfFullScreen: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetBoundingRect(self, pRect: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetMetrics(self, pPos: POINTER(Windows.Win32.Foundation.POINT_head), pSize: POINTER(Windows.Win32.Foundation.SIZE_head), pScaleX: POINTER(Single), pScaleY: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFullScreenSize(self, pSize: POINTER(Windows.Win32.Foundation.SIZE_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IViewObjectPresentFlipSite2(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{aad0cbf1-e7fd-4f12-8902-c78132a8e01d}')
    @commethod(3)
    def GetRotationForCurrentOutput(self, pDxgiRotation: POINTER(Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_ROTATION)) -> Windows.Win32.Foundation.HRESULT: ...
class IWebBrowserEventsService(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{54a8f188-9ebd-4795-ad16-9b4945119636}')
    @commethod(3)
    def FireBeforeNavigate2Event(self, pfCancel: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FireNavigateComplete2Event(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def FireDownloadBeginEvent(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FireDownloadCompleteEvent(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FireDocumentCompleteEvent(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWebBrowserEventsUrlService(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{87cc5d04-eafa-4833-9820-8f986530cc00}')
    @commethod(3)
    def GetUrlForEvents(self, pUrl: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
IntelliForms = Guid('{613ab92e-16bf-11d2-bca5-00c04fd929db}')
InternetExplorerManager = Guid('{df4fcc34-067a-4e0a-8352-4a1a5095346e}')
class Iwfolders(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{bae31f98-1b81-11d2-a97a-00c04f8ecb02}')
    @commethod(7)
    def navigate(self, bstrUrl: Windows.Win32.Foundation.BSTR, pbstrRetVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def navigateFrame(self, bstrUrl: Windows.Win32.Foundation.BSTR, bstrTargetFrame: Windows.Win32.Foundation.BSTR, pbstrRetVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def navigateNoSite(self, bstrUrl: Windows.Win32.Foundation.BSTR, bstrTargetFrame: Windows.Win32.Foundation.BSTR, dwhwnd: UInt32, pwb: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
MEDIA_ACTIVITY_NOTIFY_TYPE = Int32
MEDIA_ACTIVITY_NOTIFY_TYPE_MediaPlayback: MEDIA_ACTIVITY_NOTIFY_TYPE = 0
MEDIA_ACTIVITY_NOTIFY_TYPE_MediaRecording: MEDIA_ACTIVITY_NOTIFY_TYPE = 1
MEDIA_ACTIVITY_NOTIFY_TYPE_MediaCasting: MEDIA_ACTIVITY_NOTIFY_TYPE = 2
class NAVIGATEDATA(EasyCastStructure):
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
OpenServiceActivityManager = Guid('{c5efd803-50f8-43cd-9ab8-aafc1394c9e0}')
OpenServiceErrors = Int32
OS_E_NOTFOUND: OpenServiceErrors = -2147287038
OS_E_NOTSUPPORTED: OpenServiceErrors = -2147467231
OS_E_CANCELLED: OpenServiceErrors = -2147471631
OS_E_GPDISABLED: OpenServiceErrors = -1072886820
OpenServiceManager = Guid('{098870b6-39ea-480b-b8b5-dd0167c4db59}')
PeerFactory = Guid('{3050f4cf-98b5-11cf-bb82-00aa00bdce0b}')
SCROLLABLECONTEXTMENU_PLACEMENT = Int32
SCMP_TOP: SCROLLABLECONTEXTMENU_PLACEMENT = 0
SCMP_BOTTOM: SCROLLABLECONTEXTMENU_PLACEMENT = 1
SCMP_LEFT: SCROLLABLECONTEXTMENU_PLACEMENT = 2
SCMP_RIGHT: SCROLLABLECONTEXTMENU_PLACEMENT = 3
SCMP_FULL: SCROLLABLECONTEXTMENU_PLACEMENT = 4
class STATURL(EasyCastStructure):
    cbSize: UInt32
    pwcsUrl: Windows.Win32.Foundation.PWSTR
    pwcsTitle: Windows.Win32.Foundation.PWSTR
    ftLastVisited: Windows.Win32.Foundation.FILETIME
    ftLastUpdated: Windows.Win32.Foundation.FILETIME
    ftExpires: Windows.Win32.Foundation.FILETIME
    dwFlags: UInt32
wfolders = Guid('{bae31f9a-1b81-11d2-a97a-00c04f8ecb02}')
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
make_head(_module, 'NAVIGATEDATA')
make_head(_module, 'STATURL')
