from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.DirectDraw
import win32more.Windows.Win32.Graphics.Dxgi.Common
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.Storage.FileSystem
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Ole
import win32more.Windows.Win32.System.Registry
import win32more.Windows.Win32.System.Threading
import win32more.Windows.Win32.System.Variant
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Win32.UI.WindowsAndMessaging
import win32more.Windows.Win32.Web.InternetExplorer
import win32more.Windows.Win32.Web.MsHtml
ADDURL_FLAG = Int32
ADDURL_FIRST: win32more.Windows.Win32.Web.InternetExplorer.ADDURL_FLAG = 0
ADDURL_ADDTOHISTORYANDCACHE: win32more.Windows.Win32.Web.InternetExplorer.ADDURL_FLAG = 0
ADDURL_ADDTOCACHE: win32more.Windows.Win32.Web.InternetExplorer.ADDURL_FLAG = 1
ADDURL_Max: win32more.Windows.Win32.Web.InternetExplorer.ADDURL_FLAG = 2147483647
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
def IEAssociateThreadWithTab(dwTabThreadID: UInt32, dwAssociatedThreadID: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IEDisassociateThreadWithTab(dwTabThreadID: UInt32, dwAssociatedThreadID: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IEIsInPrivateBrowsing() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('Ieframe.dll')
def IEInPrivateFilteringEnabled() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('Ieframe.dll')
def IETrackingProtectionEnabled() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('Ieframe.dll')
def IESaveFile(hState: win32more.Windows.Win32.Foundation.HANDLE, lpwstrSourceFile: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IECancelSaveFile(hState: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IEShowSaveFileDialog(hwnd: win32more.Windows.Win32.Foundation.HWND, lpwstrInitialFileName: win32more.Windows.Win32.Foundation.PWSTR, lpwstrInitialDir: win32more.Windows.Win32.Foundation.PWSTR, lpwstrFilter: win32more.Windows.Win32.Foundation.PWSTR, lpwstrDefExt: win32more.Windows.Win32.Foundation.PWSTR, dwFilterIndex: UInt32, dwFlags: UInt32, lppwstrDestinationFilePath: POINTER(win32more.Windows.Win32.Foundation.PWSTR), phState: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IEShowOpenFileDialog(hwnd: win32more.Windows.Win32.Foundation.HWND, lpwstrFileName: win32more.Windows.Win32.Foundation.PWSTR, cchMaxFileName: UInt32, lpwstrInitialDir: win32more.Windows.Win32.Foundation.PWSTR, lpwstrFilter: win32more.Windows.Win32.Foundation.PWSTR, lpwstrDefExt: win32more.Windows.Win32.Foundation.PWSTR, dwFilterIndex: UInt32, dwFlags: UInt32, phFile: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IEGetWriteableLowHKCU(pHKey: POINTER(win32more.Windows.Win32.System.Registry.HKEY)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IEGetWriteableFolderPath(clsidFolderID: POINTER(Guid), lppwstrPath: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IEIsProtectedModeProcess(pbResult: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IEIsProtectedModeURL(lpwstrUrl: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IELaunchURL(lpwstrUrl: win32more.Windows.Win32.Foundation.PWSTR, lpProcInfo: POINTER(win32more.Windows.Win32.System.Threading.PROCESS_INFORMATION), lpInfo: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IERefreshElevationPolicy() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IEGetProtectedModeCookie(lpszURL: win32more.Windows.Win32.Foundation.PWSTR, lpszCookieName: win32more.Windows.Win32.Foundation.PWSTR, lpszCookieData: win32more.Windows.Win32.Foundation.PWSTR, pcchCookieData: POINTER(UInt32), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IESetProtectedModeCookie(lpszURL: win32more.Windows.Win32.Foundation.PWSTR, lpszCookieName: win32more.Windows.Win32.Foundation.PWSTR, lpszCookieData: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IERegisterWritableRegistryKey(guid: Guid, lpSubkey: win32more.Windows.Win32.Foundation.PWSTR, fSubkeyAllowed: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IERegisterWritableRegistryValue(guid: Guid, lpPath: win32more.Windows.Win32.Foundation.PWSTR, lpValueName: win32more.Windows.Win32.Foundation.PWSTR, dwType: UInt32, lpData: POINTER(Byte), cbMaxData: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IEUnregisterWritableRegistry(guid: Guid) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IERegCreateKeyEx(lpSubKey: win32more.Windows.Win32.Foundation.PWSTR, Reserved: UInt32, lpClass: win32more.Windows.Win32.Foundation.PWSTR, dwOptions: UInt32, samDesired: UInt32, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), phkResult: POINTER(win32more.Windows.Win32.System.Registry.HKEY), lpdwDisposition: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IERegSetValueEx(lpSubKey: win32more.Windows.Win32.Foundation.PWSTR, lpValueName: win32more.Windows.Win32.Foundation.PWSTR, Reserved: UInt32, dwType: UInt32, lpData: POINTER(Byte), cbData: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Ieframe.dll')
def IECreateFile(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, dwDesiredAccess: UInt32, dwShareMode: UInt32, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), dwCreationDisposition: UInt32, dwFlagsAndAttributes: UInt32, hTemplateFile: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('Ieframe.dll')
def IEDeleteFile(lpFileName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('Ieframe.dll')
def IERemoveDirectory(lpPathName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('Ieframe.dll')
def IEMoveFileEx(lpExistingFileName: win32more.Windows.Win32.Foundation.PWSTR, lpNewFileName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('Ieframe.dll')
def IECreateDirectory(lpPathName: win32more.Windows.Win32.Foundation.PWSTR, lpSecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('Ieframe.dll')
def IEGetFileAttributesEx(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, fInfoLevelId: win32more.Windows.Win32.Storage.FileSystem.GET_FILEEX_INFO_LEVELS, lpFileInformation: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('Ieframe.dll')
def IEFindFirstFile(lpFileName: win32more.Windows.Win32.Foundation.PWSTR, lpFindFileData: POINTER(win32more.Windows.Win32.Storage.FileSystem.WIN32_FIND_DATAA)) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('MSRATING.dll')
def RatingEnableW(hwndParent: win32more.Windows.Win32.Foundation.HWND, pszUsername: win32more.Windows.Win32.Foundation.PWSTR, fEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
RatingEnable = UnicodeAlias('RatingEnableW')
@winfunctype('MSRATING.dll')
def RatingCheckUserAccessW(pszUsername: win32more.Windows.Win32.Foundation.PWSTR, pszURL: win32more.Windows.Win32.Foundation.PWSTR, pszRatingInfo: win32more.Windows.Win32.Foundation.PWSTR, pData: POINTER(Byte), cbData: UInt32, ppRatingDetails: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
RatingCheckUserAccess = UnicodeAlias('RatingCheckUserAccessW')
@winfunctype('MSRATING.dll')
def RatingAccessDeniedDialogW(hDlg: win32more.Windows.Win32.Foundation.HWND, pszUsername: win32more.Windows.Win32.Foundation.PWSTR, pszContentDescription: win32more.Windows.Win32.Foundation.PWSTR, pRatingDetails: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
RatingAccessDeniedDialog = UnicodeAlias('RatingAccessDeniedDialogW')
@winfunctype('MSRATING.dll')
def RatingAccessDeniedDialog2W(hDlg: win32more.Windows.Win32.Foundation.HWND, pszUsername: win32more.Windows.Win32.Foundation.PWSTR, pRatingDetails: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
RatingAccessDeniedDialog2 = UnicodeAlias('RatingAccessDeniedDialog2W')
@winfunctype('MSRATING.dll')
def RatingFreeDetails(pRatingDetails: VoidPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingObtainCancel(hRatingObtainQuery: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingObtainQueryW(pszTargetUrl: win32more.Windows.Win32.Foundation.PWSTR, dwUserData: UInt32, fCallback: IntPtr, phRatingObtainQuery: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
RatingObtainQuery = UnicodeAlias('RatingObtainQueryW')
@winfunctype('MSRATING.dll')
def RatingSetupUIW(hDlg: win32more.Windows.Win32.Foundation.HWND, pszUsername: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
RatingSetupUI = UnicodeAlias('RatingSetupUIW')
@winfunctype('MSRATING.dll')
def RatingAddToApprovedSites(hDlg: win32more.Windows.Win32.Foundation.HWND, cbPasswordBlob: UInt32, pbPasswordBlob: POINTER(Byte), lpszUrl: win32more.Windows.Win32.Foundation.PWSTR, fAlwaysNever: win32more.Windows.Win32.Foundation.BOOL, fSitePage: win32more.Windows.Win32.Foundation.BOOL, fApprovedSitesEnforced: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingClickedOnPRFInternal(hWndOwner: win32more.Windows.Win32.Foundation.HWND, param1: win32more.Windows.Win32.Foundation.HINSTANCE, lpszFileName: win32more.Windows.Win32.Foundation.PSTR, nShow: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingClickedOnRATInternal(hWndOwner: win32more.Windows.Win32.Foundation.HWND, param1: win32more.Windows.Win32.Foundation.HINSTANCE, lpszFileName: win32more.Windows.Win32.Foundation.PSTR, nShow: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingEnabledQuery() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSRATING.dll')
def RatingInit() -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ImgUtil.dll')
def CreateMIMEMap(ppMap: POINTER(win32more.Windows.Win32.Web.InternetExplorer.IMapMIMEToCLSID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ImgUtil.dll')
def DecodeImage(pStream: win32more.Windows.Win32.System.Com.IStream, pMap: win32more.Windows.Win32.Web.InternetExplorer.IMapMIMEToCLSID, pEventSink: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ImgUtil.dll')
def SniffStream(pInStream: win32more.Windows.Win32.System.Com.IStream, pnFormat: POINTER(UInt32), ppOutStream: POINTER(win32more.Windows.Win32.System.Com.IStream)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ImgUtil.dll')
def GetMaxMIMEIDBytes(pnMaxBytes: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ImgUtil.dll')
def IdentifyMIMEType(pbBytes: POINTER(Byte), nBytes: UInt32, pnFormat: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ImgUtil.dll')
def ComputeInvCMAP(pRGBColors: POINTER(win32more.Windows.Win32.Graphics.Gdi.RGBQUAD), nColors: UInt32, pInvTable: POINTER(Byte), cbTable: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ImgUtil.dll')
def DitherTo8(pDestBits: POINTER(Byte), nDestPitch: Int32, pSrcBits: POINTER(Byte), nSrcPitch: Int32, bfidSrc: POINTER(Guid), prgbDestColors: POINTER(win32more.Windows.Win32.Graphics.Gdi.RGBQUAD), prgbSrcColors: POINTER(win32more.Windows.Win32.Graphics.Gdi.RGBQUAD), pbDestInvMap: POINTER(Byte), x: Int32, y: Int32, cx: Int32, cy: Int32, lDestTrans: Int32, lSrcTrans: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ImgUtil.dll')
def CreateDDrawSurfaceOnDIB(hbmDib: win32more.Windows.Win32.Graphics.Gdi.HBITMAP, ppSurface: POINTER(win32more.Windows.Win32.Graphics.DirectDraw.IDirectDrawSurface)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('ImgUtil.dll')
def DecodeImageEx(pStream: win32more.Windows.Win32.System.Com.IStream, pMap: win32more.Windows.Win32.Web.InternetExplorer.IMapMIMEToCLSID, pEventSink: win32more.Windows.Win32.System.Com.IUnknown, pszMIMETypeParam: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
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
ExtensionValidationContextNone: win32more.Windows.Win32.Web.InternetExplorer.ExtensionValidationContexts = 0
ExtensionValidationContextDynamic: win32more.Windows.Win32.Web.InternetExplorer.ExtensionValidationContexts = 1
ExtensionValidationContextParsed: win32more.Windows.Win32.Web.InternetExplorer.ExtensionValidationContexts = 2
ExtensionValidationResults = Int32
ExtensionValidationResultNone: win32more.Windows.Win32.Web.InternetExplorer.ExtensionValidationResults = 0
ExtensionValidationResultDoNotInstantiate: win32more.Windows.Win32.Web.InternetExplorer.ExtensionValidationResults = 1
ExtensionValidationResultArrestPageLoad: win32more.Windows.Win32.Web.InternetExplorer.ExtensionValidationResults = 2
FINDFRAME_FLAGS = Int32
FINDFRAME_NONE: win32more.Windows.Win32.Web.InternetExplorer.FINDFRAME_FLAGS = 0
FINDFRAME_JUSTTESTEXISTENCE: win32more.Windows.Win32.Web.InternetExplorer.FINDFRAME_FLAGS = 1
FINDFRAME_INTERNAL: win32more.Windows.Win32.Web.InternetExplorer.FINDFRAME_FLAGS = -2147483648
FRAMEOPTIONS_FLAGS = Int32
FRAMEOPTIONS_SCROLL_YES: win32more.Windows.Win32.Web.InternetExplorer.FRAMEOPTIONS_FLAGS = 1
FRAMEOPTIONS_SCROLL_NO: win32more.Windows.Win32.Web.InternetExplorer.FRAMEOPTIONS_FLAGS = 2
FRAMEOPTIONS_SCROLL_AUTO: win32more.Windows.Win32.Web.InternetExplorer.FRAMEOPTIONS_FLAGS = 4
FRAMEOPTIONS_NORESIZE: win32more.Windows.Win32.Web.InternetExplorer.FRAMEOPTIONS_FLAGS = 8
FRAMEOPTIONS_NO3DBORDER: win32more.Windows.Win32.Web.InternetExplorer.FRAMEOPTIONS_FLAGS = 16
FRAMEOPTIONS_DESKTOP: win32more.Windows.Win32.Web.InternetExplorer.FRAMEOPTIONS_FLAGS = 32
FRAMEOPTIONS_BROWSERBAND: win32more.Windows.Win32.Web.InternetExplorer.FRAMEOPTIONS_FLAGS = 64
HomePage = Guid('{766bf2ae-d650-11d1-9811-00c04fc31d2e}')
HomePageSetting = Guid('{374cede0-873a-4c4f-bc86-bcc8cf5116a3}')
class IActiveXUIHandlerSite(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{30510853-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(3)
    def CreateScrollableContextMenu(self, scrollableContextMenu: POINTER(win32more.Windows.Win32.Web.InternetExplorer.IScrollableContextMenu)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PickFileAndGetResult(self, filePicker: win32more.Windows.Win32.System.Com.IUnknown, allowMultipleSelections: win32more.Windows.Win32.Foundation.BOOL, result: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveXUIHandlerSite2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7e3707b2-d087-4542-ac1f-a0d2fcd080fd}')
    @commethod(3)
    def AddSuspensionExemption(self, pullCookie: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RemoveSuspensionExemption(self, ullCookie: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IActiveXUIHandlerSite3(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7904009a-1238-47f4-901c-871375c34608}')
    @commethod(3)
    def MessageBoxW(self, hwnd: win32more.Windows.Win32.Foundation.HWND, text: win32more.Windows.Win32.Foundation.PWSTR, caption: win32more.Windows.Win32.Foundation.PWSTR, type: UInt32, result: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAnchorClick(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{13d5413b-33b9-11d2-95a7-00c04f8ecb02}')
    @commethod(7)
    def ProcOnClick(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IAudioSessionSite(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d7d8b684-d02d-4517-b6b7-19e3dfe29c45}')
    @commethod(3)
    def GetAudioSessionGuid(self, audioSessionGuid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnAudioStreamCreated(self, endpointID: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnAudioStreamDestroyed(self, endpointID: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICaretPositionProvider(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{58da43a2-108e-4d5b-9f75-e5f74f93fff5}')
    @commethod(3)
    def GetCaretPosition(self, pptCaret: POINTER(win32more.Windows.Win32.Foundation.POINT), pflHeight: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDeviceRect(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{3050f6d5-98b5-11cf-bb82-00aa00bdce0b}')
class IDithererImpl(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7c48e840-3910-11d0-86fc-00a0c913f750}')
    @commethod(3)
    def SetDestColorTable(self, nColors: UInt32, prgbColors: POINTER(win32more.Windows.Win32.Graphics.Gdi.RGBQUAD)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetEventSink(self, pEventSink: win32more.Windows.Win32.Web.InternetExplorer.IImageDecodeEventSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDocObjectService(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3050f801-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(3)
    def FireBeforeNavigate2(self, pDispatch: win32more.Windows.Win32.System.Com.IDispatch, lpszUrl: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, lpszFrameName: win32more.Windows.Win32.Foundation.PWSTR, pPostData: POINTER(Byte), cbPostData: UInt32, lpszHeaders: win32more.Windows.Win32.Foundation.PWSTR, fPlayNavSound: win32more.Windows.Win32.Foundation.BOOL, pfCancel: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FireNavigateComplete2(self, pHTMLWindow2: win32more.Windows.Win32.Web.MsHtml.IHTMLWindow2, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def FireDownloadBegin(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FireDownloadComplete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FireDocumentComplete(self, pHTMLWindow: win32more.Windows.Win32.Web.MsHtml.IHTMLWindow2, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def UpdateDesktopComponent(self, pHTMLWindow: win32more.Windows.Win32.Web.MsHtml.IHTMLWindow2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetPendingUrl(self, pbstrPendingUrl: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ActiveElementChanged(self, pHTMLElement: win32more.Windows.Win32.Web.MsHtml.IHTMLElement) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetUrlSearchComponent(self, pbstrSearch: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def IsErrorUrl(self, lpszUrl: win32more.Windows.Win32.Foundation.PWSTR, pfIsError: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDownloadBehavior(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{3050f5bd-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(7)
    def startDownload(self, bstrUrl: win32more.Windows.Win32.Foundation.BSTR, pdispCallback: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDownloadManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{988934a4-064b-11d3-bb80-00104b35e7f9}')
    @commethod(3)
    def Download(self, pmk: win32more.Windows.Win32.System.Com.IMoniker, pbc: win32more.Windows.Win32.System.Com.IBindCtx, dwBindVerb: UInt32, grfBINDF: Int32, pBindInfo: POINTER(win32more.Windows.Win32.System.Com.BINDINFO), pszHeaders: win32more.Windows.Win32.Foundation.PWSTR, pszRedir: win32more.Windows.Win32.Foundation.PWSTR, uiCP: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
IELAUNCHOPTION_FLAGS = Int32
IELAUNCHOPTION_SCRIPTDEBUG: win32more.Windows.Win32.Web.InternetExplorer.IELAUNCHOPTION_FLAGS = 1
IELAUNCHOPTION_FORCE_COMPAT: win32more.Windows.Win32.Web.InternetExplorer.IELAUNCHOPTION_FLAGS = 2
IELAUNCHOPTION_FORCE_EDGE: win32more.Windows.Win32.Web.InternetExplorer.IELAUNCHOPTION_FLAGS = 4
IELAUNCHOPTION_LOCK_ENGINE: win32more.Windows.Win32.Web.InternetExplorer.IELAUNCHOPTION_FLAGS = 8
class IELAUNCHURLINFO(Structure):
    cbSize: UInt32
    dwCreationFlags: UInt32
    dwLaunchOptionFlags: UInt32
IEWebDriverManager = Guid('{90314af2-5250-47b3-89d8-6295fc23bc22}')
class IEnumManagerFrames(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3caa826a-9b1f-4a79-bc81-f0430ded1648}')
    @commethod(3)
    def Next(self, celt: UInt32, ppWindows: POINTER(POINTER(win32more.Windows.Win32.Foundation.HWND)), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Count(self, pcelt: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Clone(self, ppEnum: POINTER(win32more.Windows.Win32.Web.InternetExplorer.IEnumManagerFrames)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumOpenServiceActivity(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a436d7d2-17c3-4ef4-a1e8-5c86faff26c0}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.Web.InternetExplorer.IOpenServiceActivity), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.Web.InternetExplorer.IEnumOpenServiceActivity)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumOpenServiceActivityCategory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{33627a56-8c9a-4430-8fd1-b5f5c771afb6}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.Web.InternetExplorer.IOpenServiceActivityCategory), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.Web.InternetExplorer.IEnumOpenServiceActivityCategory)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IEnumSTATURL(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3c374a42-bae4-11cf-bf7d-00aa006946ee}')
    @commethod(3)
    def Next(self, celt: UInt32, rgelt: POINTER(win32more.Windows.Win32.Web.InternetExplorer.STATURL), pceltFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Skip(self, celt: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Clone(self, ppenum: POINTER(win32more.Windows.Win32.Web.InternetExplorer.IEnumSTATURL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetFilter(self, poszFilter: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IExtensionValidation(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7d33f73d-8525-4e0f-87db-830288baff44}')
    @commethod(3)
    def Validate(self, extensionGuid: POINTER(Guid), extensionModulePath: win32more.Windows.Win32.Foundation.PWSTR, extensionFileVersionMS: UInt32, extensionFileVersionLS: UInt32, htmlDocumentTop: win32more.Windows.Win32.Web.MsHtml.IHTMLDocument2, htmlDocumentSubframe: win32more.Windows.Win32.Web.MsHtml.IHTMLDocument2, htmlElement: win32more.Windows.Win32.Web.MsHtml.IHTMLElement, contexts: win32more.Windows.Win32.Web.InternetExplorer.ExtensionValidationContexts, results: POINTER(win32more.Windows.Win32.Web.InternetExplorer.ExtensionValidationResults)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DisplayName(self, displayName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHTMLPersistData(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3050f4c5-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(3)
    def save(self, pUnk: win32more.Windows.Win32.System.Com.IUnknown, lType: Int32, fContinueBroacast: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def load(self, pUnk: win32more.Windows.Win32.System.Com.IUnknown, lType: Int32, fDoDefault: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def queryType(self, lType: Int32, pfSupportsType: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHTMLPersistDataOM(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{3050f4c0-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(7)
    def get_XMLDocument(self, p: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def getAttribute(self, name: win32more.Windows.Win32.Foundation.BSTR, pValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def setAttribute(self, name: win32more.Windows.Win32.Foundation.BSTR, value: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def removeAttribute(self, name: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHTMLUserDataOM(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{3050f48f-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(7)
    def get_XMLDocument(self, p: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def save(self, strName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def load(self, strName: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def getAttribute(self, name: win32more.Windows.Win32.Foundation.BSTR, pValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def setAttribute(self, name: win32more.Windows.Win32.Foundation.BSTR, value: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def removeAttribute(self, name: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_expires(self, bstr: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_expires(self, pbstr: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHeaderFooter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{3050f6ce-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(7)
    def get_htmlHead(self, p: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_htmlFoot(self, p: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_textHead(self, v: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_textHead(self, p: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_textFoot(self, v: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_textFoot(self, p: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_page(self, v: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_page(self, p: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_pageTotal(self, v: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_pageTotal(self, p: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def put_URL(self, v: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def get_URL(self, p: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def put_title(self, v: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_title(self, p: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def put_dateShort(self, v: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_dateShort(self, p: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def put_dateLong(self, v: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def get_dateLong(self, p: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def put_timeShort(self, v: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def get_timeShort(self, p: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def put_timeLong(self, v: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def get_timeLong(self, p: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHeaderFooter2(ComPtr):
    extends: win32more.Windows.Win32.Web.InternetExplorer.IHeaderFooter
    _iid_ = Guid('{305104a5-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(29)
    def put_font(self, v: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def get_font(self, p: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHomePage(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{766bf2af-d650-11d1-9811-00c04fc31d2e}')
    @commethod(7)
    def navigateHomePage(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def setHomePage(self, bstrURL: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def isHomePage(self, bstrURL: win32more.Windows.Win32.Foundation.BSTR, p: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHomePageSetting(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{fdfc244f-18fa-4ff2-b08e-1d618f3ffbe4}')
    @commethod(3)
    def SetHomePage(self, hwnd: win32more.Windows.Win32.Foundation.HWND, homePageUri: win32more.Windows.Win32.Foundation.PWSTR, brandingMessage: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsHomePage(self, uri: win32more.Windows.Win32.Foundation.PWSTR, isDefault: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetHomePageToBrowserDefault(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IIEWebDriverManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{bd1dc630-6590-4ca2-a293-6bc72b2438d8}')
    @commethod(7)
    def ExecuteCommand(self, command: win32more.Windows.Win32.Foundation.PWSTR, response: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IIEWebDriverSite(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{ffb84444-453d-4fbc-9f9d-8db5c471ec75}')
    @commethod(7)
    def WindowOperation(self, operationCode: UInt32, hWnd: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def DetachWebdriver(self, pUnkWD: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetCapabilityValue(self, pUnkWD: win32more.Windows.Win32.System.Com.IUnknown, capName: win32more.Windows.Win32.Foundation.PWSTR, capValue: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IImageDecodeEventSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{baa342a0-2ded-11d0-86f4-00a0c913f750}')
    @commethod(3)
    def GetSurface(self, nWidth: Int32, nHeight: Int32, bfid: POINTER(Guid), nPasses: UInt32, dwHints: UInt32, ppSurface: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnBeginDecode(self, pdwEvents: POINTER(UInt32), pnFormats: POINTER(UInt32), ppFormats: POINTER(POINTER(Guid))) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnBitsComplete(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnDecodeComplete(self, hrStatus: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnPalette(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnProgress(self, pBounds: POINTER(win32more.Windows.Win32.Foundation.RECT), bComplete: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IImageDecodeEventSink2(ComPtr):
    extends: win32more.Windows.Win32.Web.InternetExplorer.IImageDecodeEventSink
    _iid_ = Guid('{8ebd8a57-8a96-48c9-84a6-962e2db9c931}')
    @commethod(9)
    def IsAlphaPremultRequired(self, pfPremultAlpha: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IImageDecodeFilter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a3ccedf3-2de2-11d0-86f4-00a0c913f750}')
    @commethod(3)
    def Initialize(self, pEventSink: win32more.Windows.Win32.Web.InternetExplorer.IImageDecodeEventSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Process(self, pStream: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Terminate(self, hrStatus: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IIntelliForms(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{9b9f68e6-1aaa-11d2-bca5-00c04fd929db}')
    @commethod(7)
    def get_enabled(self, pVal: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_enabled(self, bVal: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInternetExplorerManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{acc84351-04ff-44f9-b23f-655ed168c6d5}')
    @commethod(3)
    def CreateObject(self, dwConfig: UInt32, pszURL: win32more.Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInternetExplorerManager2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dfbb5136-9259-4895-b4a7-c1934429919a}')
    @commethod(3)
    def EnumFrameWindows(self, ppEnum: POINTER(win32more.Windows.Win32.Web.InternetExplorer.IEnumManagerFrames)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ILayoutRect(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{3050f665-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(7)
    def put_nextRect(self, bstrElementId: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_nextRect(self, pbstrElementId: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_contentSrc(self, varContentSrc: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_contentSrc(self, pvarContentSrc: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_honorPageBreaks(self, v: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_honorPageBreaks(self, p: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_honorPageRules(self, v: win32more.Windows.Win32.Foundation.VARIANT_BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_honorPageRules(self, p: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def put_nextRectElement(self, pElem: win32more.Windows.Win32.System.Com.IDispatch) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_nextRectElement(self, ppElem: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_contentDocument(self, pDoc: POINTER(win32more.Windows.Win32.System.Com.IDispatch)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMapMIMEToCLSID(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d9e89500-30fa-11d0-b724-00aa006c1a01}')
    @commethod(3)
    def EnableDefaultMappings(self, bEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def MapMIMEToCLSID(self, pszMIMEType: win32more.Windows.Win32.Foundation.PWSTR, pCLSID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetMapping(self, pszMIMEType: win32more.Windows.Win32.Foundation.PWSTR, dwMapMode: UInt32, clsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMediaActivityNotifySite(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8165cfef-179d-46c2-bc71-3fa726dc1f8d}')
    @commethod(3)
    def OnMediaActivityStarted(self, mediaActivityType: win32more.Windows.Win32.Web.InternetExplorer.MEDIA_ACTIVITY_NOTIFY_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnMediaActivityStopped(self, mediaActivityType: win32more.Windows.Win32.Web.InternetExplorer.MEDIA_ACTIVITY_NOTIFY_TYPE) -> win32more.Windows.Win32.Foundation.HRESULT: ...
INTERNETEXPLORERCONFIGURATION = Int32
INTERNETEXPLORERCONFIGURATION_HOST: win32more.Windows.Win32.Web.InternetExplorer.INTERNETEXPLORERCONFIGURATION = 1
INTERNETEXPLORERCONFIGURATION_WEB_DRIVER: win32more.Windows.Win32.Web.InternetExplorer.INTERNETEXPLORERCONFIGURATION = 2
INTERNETEXPLORERCONFIGURATION_WEB_DRIVER_EDGE: win32more.Windows.Win32.Web.InternetExplorer.INTERNETEXPLORERCONFIGURATION = 4
class IOpenService(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{c2952ed1-6a89-4606-925f-1ed8b4be0630}')
    @commethod(3)
    def IsDefault(self, pfIsDefault: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetDefault(self, fDefault: win32more.Windows.Win32.Foundation.BOOL, hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetID(self, pbstrID: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpenServiceActivity(ComPtr):
    extends: win32more.Windows.Win32.Web.InternetExplorer.IOpenService
    _iid_ = Guid('{13645c88-221a-4905-8ed1-4f5112cfc108}')
    @commethod(6)
    def Execute(self, pInput: win32more.Windows.Win32.Web.InternetExplorer.IOpenServiceActivityInput, pOutput: win32more.Windows.Win32.Web.InternetExplorer.IOpenServiceActivityOutputContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CanExecute(self, pInput: win32more.Windows.Win32.Web.InternetExplorer.IOpenServiceActivityInput, pOutput: win32more.Windows.Win32.Web.InternetExplorer.IOpenServiceActivityOutputContext, pfCanExecute: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CanExecuteType(self, type: win32more.Windows.Win32.Web.InternetExplorer.OpenServiceActivityContentType, pfCanExecute: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Preview(self, pInput: win32more.Windows.Win32.Web.InternetExplorer.IOpenServiceActivityInput, pOutput: win32more.Windows.Win32.Web.InternetExplorer.IOpenServiceActivityOutputContext) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CanPreview(self, pInput: win32more.Windows.Win32.Web.InternetExplorer.IOpenServiceActivityInput, pOutput: win32more.Windows.Win32.Web.InternetExplorer.IOpenServiceActivityOutputContext, pfCanPreview: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CanPreviewType(self, type: win32more.Windows.Win32.Web.InternetExplorer.OpenServiceActivityContentType, pfCanPreview: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetStatusText(self, pInput: win32more.Windows.Win32.Web.InternetExplorer.IOpenServiceActivityInput, pbstrStatusText: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetHomepageUrl(self, pbstrHomepageUrl: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetDisplayName(self, pbstrDisplayName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetDescription(self, pbstrDescription: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetCategoryName(self, pbstrCategoryName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetIconPath(self, pbstrIconPath: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetIcon(self, fSmallIcon: win32more.Windows.Win32.Foundation.BOOL, phIcon: POINTER(win32more.Windows.Win32.UI.WindowsAndMessaging.HICON)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetDescriptionFilePath(self, pbstrXmlPath: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetDownloadUrl(self, pbstrXmlUri: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def GetInstallUrl(self, pbstrInstallUri: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def IsEnabled(self, pfIsEnabled: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetEnabled(self, fEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpenServiceActivityCategory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{850af9d6-7309-40b5-bdb8-786c106b2153}')
    @commethod(3)
    def HasDefaultActivity(self, pfHasDefaultActivity: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDefaultActivity(self, ppDefaultActivity: POINTER(win32more.Windows.Win32.Web.InternetExplorer.IOpenServiceActivity)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetDefaultActivity(self, pActivity: win32more.Windows.Win32.Web.InternetExplorer.IOpenServiceActivity, hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetName(self, pbstrName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetActivityEnumerator(self, pInput: win32more.Windows.Win32.Web.InternetExplorer.IOpenServiceActivityInput, pOutput: win32more.Windows.Win32.Web.InternetExplorer.IOpenServiceActivityOutputContext, ppEnumActivity: POINTER(win32more.Windows.Win32.Web.InternetExplorer.IEnumOpenServiceActivity)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpenServiceActivityInput(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{75cb4db9-6da0-4da3-83ce-422b6a433346}')
    @commethod(3)
    def GetVariable(self, pwzVariableName: win32more.Windows.Win32.Foundation.PWSTR, pwzVariableType: win32more.Windows.Win32.Foundation.PWSTR, pbstrVariableContent: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def HasVariable(self, pwzVariableName: win32more.Windows.Win32.Foundation.PWSTR, pwzVariableType: win32more.Windows.Win32.Foundation.PWSTR, pfHasVariable: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetType(self, pType: POINTER(win32more.Windows.Win32.Web.InternetExplorer.OpenServiceActivityContentType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpenServiceActivityManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{8a2d0a9d-e920-4bdc-a291-d30f650bc4f1}')
    @commethod(3)
    def GetCategoryEnumerator(self, eType: win32more.Windows.Win32.Web.InternetExplorer.OpenServiceActivityContentType, ppEnum: POINTER(win32more.Windows.Win32.Web.InternetExplorer.IEnumOpenServiceActivityCategory)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetActivityByID(self, pwzActivityID: win32more.Windows.Win32.Foundation.PWSTR, ppActivity: POINTER(win32more.Windows.Win32.Web.InternetExplorer.IOpenServiceActivity)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetActivityByHomepageAndCategory(self, pwzHomepage: win32more.Windows.Win32.Foundation.PWSTR, pwzCategory: win32more.Windows.Win32.Foundation.PWSTR, ppActivity: POINTER(win32more.Windows.Win32.Web.InternetExplorer.IOpenServiceActivity)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetVersionCookie(self, pdwVersionCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpenServiceActivityOutputContext(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e289deab-f709-49a9-b99e-282364074571}')
    @commethod(3)
    def Navigate(self, pwzUri: win32more.Windows.Win32.Foundation.PWSTR, pwzMethod: win32more.Windows.Win32.Foundation.PWSTR, pwzHeaders: win32more.Windows.Win32.Foundation.PWSTR, pPostData: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CanNavigate(self, pwzUri: win32more.Windows.Win32.Foundation.PWSTR, pwzMethod: win32more.Windows.Win32.Foundation.PWSTR, pwzHeaders: win32more.Windows.Win32.Foundation.PWSTR, pPostData: win32more.Windows.Win32.System.Com.IStream, pfCanNavigate: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IOpenServiceManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{5664125f-4e10-4e90-98e4-e4513d955a14}')
    @commethod(3)
    def InstallService(self, pwzServiceUrl: win32more.Windows.Win32.Foundation.PWSTR, ppService: POINTER(win32more.Windows.Win32.Web.InternetExplorer.IOpenService)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UninstallService(self, pService: win32more.Windows.Win32.Web.InternetExplorer.IOpenService) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetServiceByID(self, pwzID: win32more.Windows.Win32.Foundation.PWSTR, ppService: POINTER(win32more.Windows.Win32.Web.InternetExplorer.IOpenService)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPeerFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{6663f9d3-b482-11d1-89c6-00c04fb6bfc4}')
class IPersistHistory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IPersist
    _iid_ = Guid('{91a565c1-e38f-11d0-94bf-00a0c9055cbf}')
    @commethod(4)
    def LoadHistory(self, pStream: win32more.Windows.Win32.System.Com.IStream, pbc: win32more.Windows.Win32.System.Com.IBindCtx) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SaveHistory(self, pStream: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetPositionCookie(self, dwPositioncookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPositionCookie(self, pdwPositioncookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPrintTaskRequestFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{bb516745-8c34-4f8b-9605-684dcb144be5}')
    @commethod(3)
    def CreatePrintTaskRequest(self, pPrintTaskRequestHandler: win32more.Windows.Win32.Web.InternetExplorer.IPrintTaskRequestHandler) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IPrintTaskRequestHandler(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{191cd340-cf36-44ff-bd53-d1b701799d9b}')
    @commethod(3)
    def HandlePrintTaskRequest(self, pPrintTaskRequest: win32more.Windows.Win32.System.WinRT.IInspectable) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IScrollableContextMenu(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{30510854-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(3)
    def AddItem(self, itemText: win32more.Windows.Win32.Foundation.PWSTR, cmdID: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ShowModal(self, x: Int32, y: Int32, cmdID: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IScrollableContextMenu2(ComPtr):
    extends: win32more.Windows.Win32.Web.InternetExplorer.IScrollableContextMenu
    _iid_ = Guid('{f77e9056-8674-4936-924c-0e4a06fa634a}')
    @commethod(5)
    def AddSeparator(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetPlacement(self, scmp: win32more.Windows.Win32.Web.InternetExplorer.SCROLLABLECONTEXTMENU_PLACEMENT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISniffStream(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4ef17940-30e0-11d0-b724-00aa006c1a01}')
    @commethod(3)
    def Init(self, pStream: win32more.Windows.Win32.System.Com.IStream) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Peek(self, pBuffer: VoidPtr, nBytes: UInt32, pnBytesRead: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISurfacePresenterFlip(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{30510848-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(3)
    def Present(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetBuffer(self, backBufferIndex: UInt32, riid: POINTER(Guid), ppBuffer: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISurfacePresenterFlip2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{30510865-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(3)
    def SetRotation(self, dxgiRotation: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_ROTATION) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISurfacePresenterFlipBuffer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e43f4a08-8bbc-4665-ac92-c55ce61fd7e7}')
    @commethod(3)
    def BeginDraw(self, riid: POINTER(Guid), ppBuffer: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EndDraw(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITargetContainer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{7847ec01-2bec-11d0-82b4-00a0c90c29c5}')
    @commethod(3)
    def GetFrameUrl(self, ppszFrameSrc: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFramesContainer(self, ppContainer: POINTER(win32more.Windows.Win32.System.Ole.IOleContainer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITargetEmbedding(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{548793c0-9e74-11cf-9655-00a0c9034923}')
    @commethod(3)
    def GetTargetFrame(self, ppTargetFrame: POINTER(win32more.Windows.Win32.Web.InternetExplorer.ITargetFrame)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITargetFrame(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{d5f78c80-5252-11cf-90fa-00aa0042106e}')
    @commethod(3)
    def SetFrameName(self, pszFrameName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFrameName(self, ppszFrameName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetParentFrame(self, ppunkParent: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FindFrame(self, pszTargetName: win32more.Windows.Win32.Foundation.PWSTR, ppunkContextFrame: win32more.Windows.Win32.System.Com.IUnknown, dwFlags: UInt32, ppunkTargetFrame: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetFrameSrc(self, pszFrameSrc: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetFrameSrc(self, ppszFrameSrc: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetFramesContainer(self, ppContainer: POINTER(win32more.Windows.Win32.System.Ole.IOleContainer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetFrameOptions(self, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetFrameOptions(self, pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetFrameMargins(self, dwWidth: UInt32, dwHeight: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetFrameMargins(self, pdwWidth: POINTER(UInt32), pdwHeight: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def RemoteNavigate(self, cLength: UInt32, pulData: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def OnChildFrameActivate(self, pUnkChildFrame: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def OnChildFrameDeactivate(self, pUnkChildFrame: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITargetFrame2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{86d52e11-94a8-11d0-82af-00c04fd5ae38}')
    @commethod(3)
    def SetFrameName(self, pszFrameName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFrameName(self, ppszFrameName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetParentFrame(self, ppunkParent: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetFrameSrc(self, pszFrameSrc: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFrameSrc(self, ppszFrameSrc: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetFramesContainer(self, ppContainer: POINTER(win32more.Windows.Win32.System.Ole.IOleContainer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetFrameOptions(self, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFrameOptions(self, pdwFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetFrameMargins(self, dwWidth: UInt32, dwHeight: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetFrameMargins(self, pdwWidth: POINTER(UInt32), pdwHeight: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def FindFrame(self, pszTargetName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, ppunkTargetFrame: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetTargetAlias(self, pszTargetName: win32more.Windows.Win32.Foundation.PWSTR, ppszTargetAlias: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITargetFramePriv(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9216e421-2bf5-11d0-82b4-00a0c90c29c5}')
    @commethod(3)
    def FindFrameDownwards(self, pszTargetName: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, ppunkTargetFrame: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FindFrameInContext(self, pszTargetName: win32more.Windows.Win32.Foundation.PWSTR, punkContextFrame: win32more.Windows.Win32.System.Com.IUnknown, dwFlags: UInt32, ppunkTargetFrame: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnChildFrameActivate(self, pUnkChildFrame: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnChildFrameDeactivate(self, pUnkChildFrame: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def NavigateHack(self, grfHLNF: UInt32, pbc: win32more.Windows.Win32.System.Com.IBindCtx, pibsc: win32more.Windows.Win32.System.Com.IBindStatusCallback, pszTargetName: win32more.Windows.Win32.Foundation.PWSTR, pszUrl: win32more.Windows.Win32.Foundation.PWSTR, pszLocation: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def FindBrowserByIndex(self, dwID: UInt32, ppunkBrowser: POINTER(win32more.Windows.Win32.System.Com.IUnknown)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITargetFramePriv2(ComPtr):
    extends: win32more.Windows.Win32.Web.InternetExplorer.ITargetFramePriv
    _iid_ = Guid('{b2c867e6-69d6-46f2-a611-ded9a4bd7fef}')
    @commethod(9)
    def AggregatedNavigation2(self, grfHLNF: UInt32, pbc: win32more.Windows.Win32.System.Com.IBindCtx, pibsc: win32more.Windows.Win32.System.Com.IBindStatusCallback, pszTargetName: win32more.Windows.Win32.Foundation.PWSTR, pUri: win32more.Windows.Win32.System.Com.IUri, pszLocation: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITargetNotify(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{863a99a0-21bc-11d0-82b4-00a0c90c29c5}')
    @commethod(3)
    def OnCreate(self, pUnkDestination: win32more.Windows.Win32.System.Com.IUnknown, cbCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnReuse(self, pUnkDestination: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITargetNotify2(ComPtr):
    extends: win32more.Windows.Win32.Web.InternetExplorer.ITargetNotify
    _iid_ = Guid('{3050f6b1-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(5)
    def GetOptionString(self, pbstrOptions: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITimer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3050f360-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(3)
    def Advise(self, vtimeMin: win32more.Windows.Win32.System.Variant.VARIANT, vtimeMax: win32more.Windows.Win32.System.Variant.VARIANT, vtimeInterval: win32more.Windows.Win32.System.Variant.VARIANT, dwFlags: UInt32, pTimerSink: win32more.Windows.Win32.Web.InternetExplorer.ITimerSink, pdwCookie: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unadvise(self, dwCookie: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Freeze(self, fFreeze: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetTime(self, pvtime: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITimerEx(ComPtr):
    extends: win32more.Windows.Win32.Web.InternetExplorer.ITimer
    _iid_ = Guid('{30510414-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(7)
    def SetMode(self, dwMode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITimerService(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3050f35f-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(3)
    def CreateTimer(self, pReferenceTimer: win32more.Windows.Win32.Web.InternetExplorer.ITimer, ppNewTimer: POINTER(win32more.Windows.Win32.Web.InternetExplorer.ITimer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNamedTimer(self, rguidName: POINTER(Guid), ppTimer: POINTER(win32more.Windows.Win32.Web.InternetExplorer.ITimer)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetNamedTimerReference(self, rguidName: POINTER(Guid), pReferenceTimer: win32more.Windows.Win32.Web.InternetExplorer.ITimer) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITimerSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3050f361-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(3)
    def OnTimer(self, vtimeAdvise: win32more.Windows.Win32.System.Variant.VARIANT) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITridentTouchInput(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{30510850-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(3)
    def OnPointerMessage(self, msg: UInt32, wParam: win32more.Windows.Win32.Foundation.WPARAM, lParam: win32more.Windows.Win32.Foundation.LPARAM, pfAllowManipulations: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ITridentTouchInputSite(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{30510849-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(3)
    def SetManipulationMode(self, msTouchAction: win32more.Windows.Win32.Web.MsHtml.styleMsTouchAction) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ZoomToPoint(self, x: Int32, y: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUrlHistoryNotify(ComPtr):
    extends: win32more.Windows.Win32.System.Ole.IOleCommandTarget
    _iid_ = Guid('{bc40bec1-c493-11d0-831b-00c04fd5ae38}')
class IUrlHistoryStg(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3c374a41-bae4-11cf-bf7d-00aa006946ee}')
    @commethod(3)
    def AddUrl(self, pocsUrl: win32more.Windows.Win32.Foundation.PWSTR, pocsTitle: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DeleteUrl(self, pocsUrl: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def QueryUrl(self, pocsUrl: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, lpSTATURL: POINTER(win32more.Windows.Win32.Web.InternetExplorer.STATURL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def BindToObject(self, pocsUrl: win32more.Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), ppvOut: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def EnumUrls(self, ppEnum: POINTER(win32more.Windows.Win32.Web.InternetExplorer.IEnumSTATURL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUrlHistoryStg2(ComPtr):
    extends: win32more.Windows.Win32.Web.InternetExplorer.IUrlHistoryStg
    _iid_ = Guid('{afa0dc11-c313-11d0-831a-00c04fd5ae38}')
    @commethod(8)
    def AddUrlAndNotify(self, pocsUrl: win32more.Windows.Win32.Foundation.PWSTR, pocsTitle: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, fWriteHistory: win32more.Windows.Win32.Foundation.BOOL, poctNotify: win32more.Windows.Win32.System.Ole.IOleCommandTarget, punkISFolder: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def ClearHistory(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IViewObjectPresentFlip(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{30510847-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(3)
    def NotifyRender(self, fRecreatePresenter: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def RenderObjectToBitmap(self, pBitmap: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RenderObjectToSharedBuffer(self, pBuffer: win32more.Windows.Win32.Web.InternetExplorer.ISurfacePresenterFlipBuffer) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IViewObjectPresentFlip2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{30510856-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(3)
    def NotifyLeavingView(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IViewObjectPresentFlipSite(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{30510846-98b5-11cf-bb82-00aa00bdce0b}')
    @commethod(3)
    def CreateSurfacePresenterFlip(self, pDevice: win32more.Windows.Win32.System.Com.IUnknown, width: UInt32, height: UInt32, backBufferCount: UInt32, format: win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_FORMAT, mode: win32more.Windows.Win32.Web.MsHtml.VIEW_OBJECT_ALPHA_MODE, ppSPFlip: POINTER(win32more.Windows.Win32.Web.InternetExplorer.ISurfacePresenterFlip)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDeviceLuid(self, pLuid: POINTER(win32more.Windows.Win32.Foundation.LUID)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def EnterFullScreen(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ExitFullScreen(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsFullScreen(self, pfFullScreen: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetBoundingRect(self, pRect: POINTER(win32more.Windows.Win32.Foundation.RECT)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetMetrics(self, pPos: POINTER(win32more.Windows.Win32.Foundation.POINT), pSize: POINTER(win32more.Windows.Win32.Foundation.SIZE), pScaleX: POINTER(Single), pScaleY: POINTER(Single)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFullScreenSize(self, pSize: POINTER(win32more.Windows.Win32.Foundation.SIZE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IViewObjectPresentFlipSite2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{aad0cbf1-e7fd-4f12-8902-c78132a8e01d}')
    @commethod(3)
    def GetRotationForCurrentOutput(self, pDxgiRotation: POINTER(win32more.Windows.Win32.Graphics.Dxgi.Common.DXGI_MODE_ROTATION)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWebBrowserEventsService(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{54a8f188-9ebd-4795-ad16-9b4945119636}')
    @commethod(3)
    def FireBeforeNavigate2Event(self, pfCancel: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FireNavigateComplete2Event(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def FireDownloadBeginEvent(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def FireDownloadCompleteEvent(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FireDocumentCompleteEvent(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWebBrowserEventsUrlService(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{87cc5d04-eafa-4833-9820-8f986530cc00}')
    @commethod(3)
    def GetUrlForEvents(self, pUrl: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
IntelliForms = Guid('{613ab92e-16bf-11d2-bca5-00c04fd929db}')
InternetExplorerManager = Guid('{df4fcc34-067a-4e0a-8352-4a1a5095346e}')
class Iwfolders(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{bae31f98-1b81-11d2-a97a-00c04f8ecb02}')
    @commethod(7)
    def navigate(self, bstrUrl: win32more.Windows.Win32.Foundation.BSTR, pbstrRetVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def navigateFrame(self, bstrUrl: win32more.Windows.Win32.Foundation.BSTR, bstrTargetFrame: win32more.Windows.Win32.Foundation.BSTR, pbstrRetVal: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def navigateNoSite(self, bstrUrl: win32more.Windows.Win32.Foundation.BSTR, bstrTargetFrame: win32more.Windows.Win32.Foundation.BSTR, dwhwnd: UInt32, pwb: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
MEDIA_ACTIVITY_NOTIFY_TYPE = Int32
MediaPlayback: win32more.Windows.Win32.Web.InternetExplorer.MEDIA_ACTIVITY_NOTIFY_TYPE = 0
MediaRecording: win32more.Windows.Win32.Web.InternetExplorer.MEDIA_ACTIVITY_NOTIFY_TYPE = 1
MediaCasting: win32more.Windows.Win32.Web.InternetExplorer.MEDIA_ACTIVITY_NOTIFY_TYPE = 2
class NAVIGATEDATA(Structure):
    ulTarget: UInt32
    ulURL: UInt32
    ulRefURL: UInt32
    ulPostData: UInt32
    dwFlags: UInt32
NAVIGATEFRAME_FLAGS = Int32
NAVIGATEFRAME_FL_RECORD: win32more.Windows.Win32.Web.InternetExplorer.NAVIGATEFRAME_FLAGS = 1
NAVIGATEFRAME_FL_POST: win32more.Windows.Win32.Web.InternetExplorer.NAVIGATEFRAME_FLAGS = 2
NAVIGATEFRAME_FL_NO_DOC_CACHE: win32more.Windows.Win32.Web.InternetExplorer.NAVIGATEFRAME_FLAGS = 4
NAVIGATEFRAME_FL_NO_IMAGE_CACHE: win32more.Windows.Win32.Web.InternetExplorer.NAVIGATEFRAME_FLAGS = 8
NAVIGATEFRAME_FL_AUTH_FAIL_CACHE_OK: win32more.Windows.Win32.Web.InternetExplorer.NAVIGATEFRAME_FLAGS = 16
NAVIGATEFRAME_FL_SENDING_FROM_FORM: win32more.Windows.Win32.Web.InternetExplorer.NAVIGATEFRAME_FLAGS = 32
NAVIGATEFRAME_FL_REALLY_SENDING_FROM_FORM: win32more.Windows.Win32.Web.InternetExplorer.NAVIGATEFRAME_FLAGS = 64
OpenServiceActivityContentType = Int32
ActivityContentNone: win32more.Windows.Win32.Web.InternetExplorer.OpenServiceActivityContentType = -1
ActivityContentDocument: win32more.Windows.Win32.Web.InternetExplorer.OpenServiceActivityContentType = 0
ActivityContentSelection: win32more.Windows.Win32.Web.InternetExplorer.OpenServiceActivityContentType = 1
ActivityContentLink: win32more.Windows.Win32.Web.InternetExplorer.OpenServiceActivityContentType = 2
ActivityContentCount: win32more.Windows.Win32.Web.InternetExplorer.OpenServiceActivityContentType = 3
OpenServiceActivityManager = Guid('{c5efd803-50f8-43cd-9ab8-aafc1394c9e0}')
OpenServiceErrors = Int32
OS_E_NOTFOUND: win32more.Windows.Win32.Web.InternetExplorer.OpenServiceErrors = -2147287038
OS_E_NOTSUPPORTED: win32more.Windows.Win32.Web.InternetExplorer.OpenServiceErrors = -2147467231
OS_E_CANCELLED: win32more.Windows.Win32.Web.InternetExplorer.OpenServiceErrors = -2147471631
OS_E_GPDISABLED: win32more.Windows.Win32.Web.InternetExplorer.OpenServiceErrors = -1072886820
OpenServiceManager = Guid('{098870b6-39ea-480b-b8b5-dd0167c4db59}')
PeerFactory = Guid('{3050f4cf-98b5-11cf-bb82-00aa00bdce0b}')
SCROLLABLECONTEXTMENU_PLACEMENT = Int32
SCMP_TOP: win32more.Windows.Win32.Web.InternetExplorer.SCROLLABLECONTEXTMENU_PLACEMENT = 0
SCMP_BOTTOM: win32more.Windows.Win32.Web.InternetExplorer.SCROLLABLECONTEXTMENU_PLACEMENT = 1
SCMP_LEFT: win32more.Windows.Win32.Web.InternetExplorer.SCROLLABLECONTEXTMENU_PLACEMENT = 2
SCMP_RIGHT: win32more.Windows.Win32.Web.InternetExplorer.SCROLLABLECONTEXTMENU_PLACEMENT = 3
SCMP_FULL: win32more.Windows.Win32.Web.InternetExplorer.SCROLLABLECONTEXTMENU_PLACEMENT = 4
class STATURL(Structure):
    cbSize: UInt32
    pwcsUrl: win32more.Windows.Win32.Foundation.PWSTR
    pwcsTitle: win32more.Windows.Win32.Foundation.PWSTR
    ftLastVisited: win32more.Windows.Win32.Foundation.FILETIME
    ftLastUpdated: win32more.Windows.Win32.Foundation.FILETIME
    ftExpires: win32more.Windows.Win32.Foundation.FILETIME
    dwFlags: UInt32
wfolders = Guid('{bae31f9a-1b81-11d2-a97a-00c04f8ecb02}')


make_ready(__name__)
