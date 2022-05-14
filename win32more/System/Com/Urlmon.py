from win32more import *
import win32more.System.Com.Urlmon
import win32more.Data.Xml.MsXml
import win32more.Foundation
import win32more.System.Com

def __getattr__(name):
    if name == "__path__":
        raise AttributeError()
    setattr(win32more.System.Com.Urlmon, name, eval(f"_define_{name}()"))
    return getattr(win32more.System.Com.Urlmon, name)
MKSYS_URLMONIKER = 6
URL_MK_LEGACY = 0
URL_MK_UNIFORM = 1
URL_MK_NO_CANONICALIZE = 2
FIEF_FLAG_FORCE_JITUI = 1
FIEF_FLAG_PEEK = 2
FIEF_FLAG_SKIP_INSTALLED_VERSION_CHECK = 4
FIEF_FLAG_RESERVED_0 = 8
FMFD_DEFAULT = 0
FMFD_URLASFILENAME = 1
FMFD_ENABLEMIMESNIFFING = 2
FMFD_IGNOREMIMETEXTPLAIN = 4
FMFD_SERVERMIME = 8
FMFD_RESPECTTEXTPLAIN = 16
FMFD_RETURNUPDATEDIMGMIMES = 32
FMFD_RESERVED_1 = 64
FMFD_RESERVED_2 = 128
UAS_EXACTLEGACY = 4096
URLMON_OPTION_USERAGENT = 268435457
URLMON_OPTION_USERAGENT_REFRESH = 268435458
URLMON_OPTION_URL_ENCODING = 268435460
URLMON_OPTION_USE_BINDSTRINGCREDS = 268435464
URLMON_OPTION_USE_BROWSERAPPSDOCUMENTS = 268435472
CF_NULL = 0
MK_S_ASYNCHRONOUS = 262632
S_ASYNCHRONOUS = 262632
E_PENDING = -2147483638
INET_E_INVALID_URL = -2146697214
INET_E_NO_SESSION = -2146697213
INET_E_CANNOT_CONNECT = -2146697212
INET_E_RESOURCE_NOT_FOUND = -2146697211
INET_E_OBJECT_NOT_FOUND = -2146697210
INET_E_DATA_NOT_AVAILABLE = -2146697209
INET_E_DOWNLOAD_FAILURE = -2146697208
INET_E_AUTHENTICATION_REQUIRED = -2146697207
INET_E_NO_VALID_MEDIA = -2146697206
INET_E_CONNECTION_TIMEOUT = -2146697205
INET_E_INVALID_REQUEST = -2146697204
INET_E_UNKNOWN_PROTOCOL = -2146697203
INET_E_SECURITY_PROBLEM = -2146697202
INET_E_CANNOT_LOAD_DATA = -2146697201
INET_E_CANNOT_INSTANTIATE_OBJECT = -2146697200
INET_E_INVALID_CERTIFICATE = -2146697191
INET_E_REDIRECT_FAILED = -2146697196
INET_E_REDIRECT_TO_DIR = -2146697195
INET_E_CANNOT_LOCK_REQUEST = -2146697194
INET_E_USE_EXTEND_BINDING = -2146697193
INET_E_TERMINATED_BIND = -2146697192
INET_E_RESERVED_1 = -2146697190
INET_E_BLOCKED_REDIRECT_XSECURITYID = -2146697189
INET_E_DOMINJECTIONVALIDATION = -2146697188
INET_E_VTAB_SWITCH_FORCE_ENGINE = -2146697187
INET_E_HSTS_CERTIFICATE_ERROR = -2146697186
INET_E_RESERVED_2 = -2146697185
INET_E_RESERVED_3 = -2146697184
INET_E_RESERVED_4 = -2146697183
INET_E_RESERVED_5 = -2146697182
INET_E_ERROR_FIRST = -2146697214
INET_E_CODE_DOWNLOAD_DECLINED = -2146696960
INET_E_RESULT_DISPATCHED = -2146696704
INET_E_CANNOT_REPLACE_SFP_FILE = -2146696448
INET_E_CODE_INSTALL_SUPPRESSED = -2146696192
INET_E_CODE_INSTALL_BLOCKED_BY_HASH_POLICY = -2146695936
INET_E_DOWNLOAD_BLOCKED_BY_INPRIVATE = -2146695935
INET_E_CODE_INSTALL_BLOCKED_IMMERSIVE = -2146695934
INET_E_FORBIDFRAMING = -2146695933
INET_E_CODE_INSTALL_BLOCKED_ARM = -2146695932
INET_E_BLOCKED_PLUGGABLE_PROTOCOL = -2146695931
INET_E_BLOCKED_ENHANCEDPROTECTEDMODE = -2146695930
INET_E_CODE_INSTALL_BLOCKED_BITNESS = -2146695929
INET_E_DOWNLOAD_BLOCKED_BY_CSP = -2146695928
INET_E_ERROR_LAST = -2146695928
Uri_DISPLAY_NO_FRAGMENT = 1
Uri_PUNYCODE_IDN_HOST = 2
Uri_DISPLAY_IDN_HOST = 4
Uri_DISPLAY_NO_PUNYCODE = 8
Uri_ENCODING_USER_INFO_AND_PATH_IS_PERCENT_ENCODED_UTF8 = 1
Uri_ENCODING_USER_INFO_AND_PATH_IS_CP = 2
Uri_ENCODING_HOST_IS_IDN = 4
Uri_ENCODING_HOST_IS_PERCENT_ENCODED_UTF8 = 8
Uri_ENCODING_HOST_IS_PERCENT_ENCODED_CP = 16
Uri_ENCODING_QUERY_AND_FRAGMENT_IS_PERCENT_ENCODED_UTF8 = 32
Uri_ENCODING_QUERY_AND_FRAGMENT_IS_CP = 64
UriBuilder_USE_ORIGINAL_FLAGS = 1
WININETINFO_OPTION_LOCK_HANDLE = 65534
URLOSTRM_USECACHEDCOPY_ONLY = 1
URLOSTRM_USECACHEDCOPY = 2
URLOSTRM_GETNEWESTVERSION = 3
SET_FEATURE_ON_THREAD = 1
SET_FEATURE_ON_PROCESS = 2
SET_FEATURE_IN_REGISTRY = 4
SET_FEATURE_ON_THREAD_LOCALMACHINE = 8
SET_FEATURE_ON_THREAD_INTRANET = 16
SET_FEATURE_ON_THREAD_TRUSTED = 32
SET_FEATURE_ON_THREAD_INTERNET = 64
SET_FEATURE_ON_THREAD_RESTRICTED = 128
GET_FEATURE_FROM_THREAD = 1
GET_FEATURE_FROM_PROCESS = 2
GET_FEATURE_FROM_REGISTRY = 4
GET_FEATURE_FROM_THREAD_LOCALMACHINE = 8
GET_FEATURE_FROM_THREAD_INTRANET = 16
GET_FEATURE_FROM_THREAD_TRUSTED = 32
GET_FEATURE_FROM_THREAD_INTERNET = 64
GET_FEATURE_FROM_THREAD_RESTRICTED = 128
INET_E_USE_DEFAULT_PROTOCOLHANDLER = -2146697199
INET_E_USE_DEFAULT_SETTING = -2146697198
INET_E_DEFAULT_ACTION = -2146697199
INET_E_QUERYOPTION_UNKNOWN = -2146697197
INET_E_REDIRECTING = -2146697196
PROTOCOLFLAG_NO_PICS_CHECK = 1
MUTZ_NOSAVEDFILECHECK = 1
MUTZ_ISFILE = 2
MUTZ_ACCEPT_WILDCARD_SCHEME = 128
MUTZ_ENFORCERESTRICTED = 256
MUTZ_RESERVED = 512
MUTZ_REQUIRESAVEDFILECHECK = 1024
MUTZ_DONT_UNESCAPE = 2048
MUTZ_DONT_USE_CACHE = 4096
MUTZ_FORCE_INTRANET_FLAGS = 8192
MUTZ_IGNORE_ZONE_MAPPINGS = 16384
MAX_SIZE_SECURITY_ID = 512
URLACTION_MIN = 4096
URLACTION_DOWNLOAD_MIN = 4096
URLACTION_DOWNLOAD_SIGNED_ACTIVEX = 4097
URLACTION_DOWNLOAD_UNSIGNED_ACTIVEX = 4100
URLACTION_DOWNLOAD_CURR_MAX = 4100
URLACTION_DOWNLOAD_MAX = 4607
URLACTION_ACTIVEX_MIN = 4608
URLACTION_ACTIVEX_RUN = 4608
URLPOLICY_ACTIVEX_CHECK_LIST = 65536
URLACTION_ACTIVEX_OVERRIDE_OBJECT_SAFETY = 4609
URLACTION_ACTIVEX_OVERRIDE_DATA_SAFETY = 4610
URLACTION_ACTIVEX_OVERRIDE_SCRIPT_SAFETY = 4611
URLACTION_SCRIPT_OVERRIDE_SAFETY = 5121
URLACTION_ACTIVEX_CONFIRM_NOOBJECTSAFETY = 4612
URLACTION_ACTIVEX_TREATASUNTRUSTED = 4613
URLACTION_ACTIVEX_NO_WEBOC_SCRIPT = 4614
URLACTION_ACTIVEX_OVERRIDE_REPURPOSEDETECTION = 4615
URLACTION_ACTIVEX_OVERRIDE_OPTIN = 4616
URLACTION_ACTIVEX_SCRIPTLET_RUN = 4617
URLACTION_ACTIVEX_DYNSRC_VIDEO_AND_ANIMATION = 4618
URLACTION_ACTIVEX_OVERRIDE_DOMAINLIST = 4619
URLACTION_ACTIVEX_ALLOW_TDC = 4620
URLACTION_ACTIVEX_CURR_MAX = 4620
URLACTION_ACTIVEX_MAX = 5119
URLACTION_SCRIPT_MIN = 5120
URLACTION_SCRIPT_RUN = 5120
URLACTION_SCRIPT_JAVA_USE = 5122
URLACTION_SCRIPT_SAFE_ACTIVEX = 5125
URLACTION_CROSS_DOMAIN_DATA = 5126
URLACTION_SCRIPT_PASTE = 5127
URLACTION_ALLOW_XDOMAIN_SUBFRAME_RESIZE = 5128
URLACTION_SCRIPT_XSSFILTER = 5129
URLACTION_SCRIPT_NAVIGATE = 5130
URLACTION_PLUGGABLE_PROTOCOL_XHR = 5131
URLACTION_ALLOW_VBSCRIPT_IE = 5132
URLACTION_ALLOW_JSCRIPT_IE = 5133
URLACTION_SCRIPT_CURR_MAX = 5133
URLACTION_SCRIPT_MAX = 5631
URLACTION_HTML_MIN = 5632
URLACTION_HTML_SUBMIT_FORMS = 5633
URLACTION_HTML_SUBMIT_FORMS_FROM = 5634
URLACTION_HTML_SUBMIT_FORMS_TO = 5635
URLACTION_HTML_FONT_DOWNLOAD = 5636
URLACTION_HTML_JAVA_RUN = 5637
URLACTION_HTML_USERDATA_SAVE = 5638
URLACTION_HTML_SUBFRAME_NAVIGATE = 5639
URLACTION_HTML_META_REFRESH = 5640
URLACTION_HTML_MIXED_CONTENT = 5641
URLACTION_HTML_INCLUDE_FILE_PATH = 5642
URLACTION_HTML_ALLOW_INJECTED_DYNAMIC_HTML = 5643
URLACTION_HTML_REQUIRE_UTF8_DOCUMENT_CODEPAGE = 5644
URLACTION_HTML_ALLOW_CROSS_DOMAIN_CANVAS = 5645
URLACTION_HTML_ALLOW_WINDOW_CLOSE = 5646
URLACTION_HTML_ALLOW_CROSS_DOMAIN_WEBWORKER = 5647
URLACTION_HTML_ALLOW_CROSS_DOMAIN_TEXTTRACK = 5648
URLACTION_HTML_ALLOW_INDEXEDDB = 5649
URLACTION_HTML_MAX = 6143
URLACTION_SHELL_MIN = 6144
URLACTION_SHELL_INSTALL_DTITEMS = 6144
URLACTION_SHELL_MOVE_OR_COPY = 6146
URLACTION_SHELL_FILE_DOWNLOAD = 6147
URLACTION_SHELL_VERB = 6148
URLACTION_SHELL_WEBVIEW_VERB = 6149
URLACTION_SHELL_SHELLEXECUTE = 6150
URLACTION_SHELL_EXECUTE_HIGHRISK = 6150
URLACTION_SHELL_EXECUTE_MODRISK = 6151
URLACTION_SHELL_EXECUTE_LOWRISK = 6152
URLACTION_SHELL_POPUPMGR = 6153
URLACTION_SHELL_RTF_OBJECTS_LOAD = 6154
URLACTION_SHELL_ENHANCED_DRAGDROP_SECURITY = 6155
URLACTION_SHELL_EXTENSIONSECURITY = 6156
URLACTION_SHELL_SECURE_DRAGSOURCE = 6157
URLACTION_SHELL_REMOTEQUERY = 6158
URLACTION_SHELL_PREVIEW = 6159
URLACTION_SHELL_SHARE = 6160
URLACTION_SHELL_ALLOW_CROSS_SITE_SHARE = 6161
URLACTION_SHELL_TOCTOU_RISK = 6162
URLACTION_SHELL_CURR_MAX = 6162
URLACTION_SHELL_MAX = 6655
URLACTION_NETWORK_MIN = 6656
URLACTION_CREDENTIALS_USE = 6656
URLPOLICY_CREDENTIALS_SILENT_LOGON_OK = 0
URLPOLICY_CREDENTIALS_MUST_PROMPT_USER = 65536
URLPOLICY_CREDENTIALS_CONDITIONAL_PROMPT = 131072
URLPOLICY_CREDENTIALS_ANONYMOUS_ONLY = 196608
URLACTION_AUTHENTICATE_CLIENT = 6657
URLPOLICY_AUTHENTICATE_CLEARTEXT_OK = 0
URLPOLICY_AUTHENTICATE_CHALLENGE_RESPONSE = 65536
URLPOLICY_AUTHENTICATE_MUTUAL_ONLY = 196608
URLACTION_COOKIES = 6658
URLACTION_COOKIES_SESSION = 6659
URLACTION_CLIENT_CERT_PROMPT = 6660
URLACTION_COOKIES_THIRD_PARTY = 6661
URLACTION_COOKIES_SESSION_THIRD_PARTY = 6662
URLACTION_COOKIES_ENABLED = 6672
URLACTION_NETWORK_CURR_MAX = 6672
URLACTION_NETWORK_MAX = 7167
URLACTION_JAVA_MIN = 7168
URLACTION_JAVA_PERMISSIONS = 7168
URLPOLICY_JAVA_PROHIBIT = 0
URLPOLICY_JAVA_HIGH = 65536
URLPOLICY_JAVA_MEDIUM = 131072
URLPOLICY_JAVA_LOW = 196608
URLPOLICY_JAVA_CUSTOM = 8388608
URLACTION_JAVA_CURR_MAX = 7168
URLACTION_JAVA_MAX = 7423
URLACTION_INFODELIVERY_MIN = 7424
URLACTION_INFODELIVERY_NO_ADDING_CHANNELS = 7424
URLACTION_INFODELIVERY_NO_EDITING_CHANNELS = 7425
URLACTION_INFODELIVERY_NO_REMOVING_CHANNELS = 7426
URLACTION_INFODELIVERY_NO_ADDING_SUBSCRIPTIONS = 7427
URLACTION_INFODELIVERY_NO_EDITING_SUBSCRIPTIONS = 7428
URLACTION_INFODELIVERY_NO_REMOVING_SUBSCRIPTIONS = 7429
URLACTION_INFODELIVERY_NO_CHANNEL_LOGGING = 7430
URLACTION_INFODELIVERY_CURR_MAX = 7430
URLACTION_INFODELIVERY_MAX = 7679
URLACTION_CHANNEL_SOFTDIST_MIN = 7680
URLACTION_CHANNEL_SOFTDIST_PERMISSIONS = 7685
URLPOLICY_CHANNEL_SOFTDIST_PROHIBIT = 65536
URLPOLICY_CHANNEL_SOFTDIST_PRECACHE = 131072
URLPOLICY_CHANNEL_SOFTDIST_AUTOINSTALL = 196608
URLACTION_CHANNEL_SOFTDIST_MAX = 7935
URLACTION_DOTNET_USERCONTROLS = 8197
URLACTION_BEHAVIOR_MIN = 8192
URLACTION_BEHAVIOR_RUN = 8192
URLPOLICY_BEHAVIOR_CHECK_LIST = 65536
URLACTION_FEATURE_MIN = 8448
URLACTION_FEATURE_MIME_SNIFFING = 8448
URLACTION_FEATURE_ZONE_ELEVATION = 8449
URLACTION_FEATURE_WINDOW_RESTRICTIONS = 8450
URLACTION_FEATURE_SCRIPT_STATUS_BAR = 8451
URLACTION_FEATURE_FORCE_ADDR_AND_STATUS = 8452
URLACTION_FEATURE_BLOCK_INPUT_PROMPTS = 8453
URLACTION_FEATURE_DATA_BINDING = 8454
URLACTION_FEATURE_CROSSDOMAIN_FOCUS_CHANGE = 8455
URLACTION_AUTOMATIC_DOWNLOAD_UI_MIN = 8704
URLACTION_AUTOMATIC_DOWNLOAD_UI = 8704
URLACTION_AUTOMATIC_ACTIVEX_UI = 8705
URLACTION_ALLOW_RESTRICTEDPROTOCOLS = 8960
URLACTION_ALLOW_APEVALUATION = 8961
URLACTION_ALLOW_XHR_EVALUATION = 8962
URLACTION_WINDOWS_BROWSER_APPLICATIONS = 9216
URLACTION_XPS_DOCUMENTS = 9217
URLACTION_LOOSE_XAML = 9218
URLACTION_LOWRIGHTS = 9472
URLACTION_WINFX_SETUP = 9728
URLACTION_INPRIVATE_BLOCKING = 9984
URLACTION_ALLOW_AUDIO_VIDEO = 9985
URLACTION_ALLOW_ACTIVEX_FILTERING = 9986
URLACTION_ALLOW_STRUCTURED_STORAGE_SNIFFING = 9987
URLACTION_ALLOW_AUDIO_VIDEO_PLUGINS = 9988
URLACTION_ALLOW_ZONE_ELEVATION_VIA_OPT_OUT = 9989
URLACTION_ALLOW_ZONE_ELEVATION_OPT_OUT_ADDITION = 9990
URLACTION_ALLOW_CROSSDOMAIN_DROP_WITHIN_WINDOW = 9992
URLACTION_ALLOW_CROSSDOMAIN_DROP_ACROSS_WINDOWS = 9993
URLACTION_ALLOW_CROSSDOMAIN_APPCACHE_MANIFEST = 9994
URLACTION_ALLOW_RENDER_LEGACY_DXTFILTERS = 9995
URLACTION_ALLOW_ANTIMALWARE_SCANNING_OF_ACTIVEX = 9996
URLACTION_ALLOW_CSS_EXPRESSIONS = 9997
URLPOLICY_ALLOW = 0
URLPOLICY_QUERY = 1
URLPOLICY_DISALLOW = 3
URLPOLICY_NOTIFY_ON_ALLOW = 16
URLPOLICY_NOTIFY_ON_DISALLOW = 32
URLPOLICY_LOG_ON_ALLOW = 64
URLPOLICY_LOG_ON_DISALLOW = 128
URLPOLICY_MASK_PERMISSIONS = 15
URLPOLICY_DONTCHECKDLGBOX = 256
URLZONE_ESC_FLAG = 256
SECURITY_IE_STATE_GREEN = 0
SECURITY_IE_STATE_RED = 1
SOFTDIST_FLAG_USAGE_EMAIL = 1
SOFTDIST_FLAG_USAGE_PRECACHE = 2
SOFTDIST_FLAG_USAGE_AUTOINSTALL = 4
SOFTDIST_FLAG_DELETE_SUBSCRIPTION = 8
SOFTDIST_ADSTATE_NONE = 0
SOFTDIST_ADSTATE_AVAILABLE = 1
SOFTDIST_ADSTATE_DOWNLOADED = 2
SOFTDIST_ADSTATE_INSTALLED = 3
CONFIRMSAFETYACTION_LOADOBJECT = 1
IEObjectType = Int32
IE_EPM_OBJECT_EVENT = 0
IE_EPM_OBJECT_MUTEX = 1
IE_EPM_OBJECT_SEMAPHORE = 2
IE_EPM_OBJECT_SHARED_MEMORY = 3
IE_EPM_OBJECT_WAITABLE_TIMER = 4
IE_EPM_OBJECT_FILE = 5
IE_EPM_OBJECT_NAMED_PIPE = 6
IE_EPM_OBJECT_REGISTRY = 7
def _define_IPersistMoniker_head():
    class IPersistMoniker(win32more.System.Com.IUnknown_head):
        Guid = Guid('79eac9c9-baf9-11ce-8c82-00aa004ba90b')
    return IPersistMoniker
def _define_IPersistMoniker():
    IPersistMoniker = win32more.System.Com.Urlmon.IPersistMoniker_head
    IPersistMoniker.GetClassID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid), use_last_error=False)(3, 'GetClassID', ((1, 'pClassID'),)))
    IPersistMoniker.IsDirty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'IsDirty', ()))
    IPersistMoniker.Load = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,win32more.System.Com.IMoniker_head,win32more.System.Com.IBindCtx_head,UInt32, use_last_error=False)(5, 'Load', ((1, 'fFullyAvailable'),(1, 'pimkName'),(1, 'pibc'),(1, 'grfMode'),)))
    IPersistMoniker.Save = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IMoniker_head,win32more.System.Com.IBindCtx_head,win32more.Foundation.BOOL, use_last_error=False)(6, 'Save', ((1, 'pimkName'),(1, 'pbc'),(1, 'fRemember'),)))
    IPersistMoniker.SaveCompleted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IMoniker_head,win32more.System.Com.IBindCtx_head, use_last_error=False)(7, 'SaveCompleted', ((1, 'pimkName'),(1, 'pibc'),)))
    IPersistMoniker.GetCurMoniker = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IMoniker_head), use_last_error=False)(8, 'GetCurMoniker', ((1, 'ppimkName'),)))
    return IPersistMoniker
MONIKERPROPERTY = Int32
MIMETYPEPROP = 0
USE_SRC_URL = 1
CLASSIDPROP = 2
TRUSTEDDOWNLOADPROP = 3
POPUPLEVELPROP = 4
def _define_IMonikerProp_head():
    class IMonikerProp(win32more.System.Com.IUnknown_head):
        Guid = Guid('a5ca5f7f-1847-4d87-9c5b-918509f7511d')
    return IMonikerProp
def _define_IMonikerProp():
    IMonikerProp = win32more.System.Com.Urlmon.IMonikerProp_head
    IMonikerProp.PutProperty = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.Urlmon.MONIKERPROPERTY,win32more.Foundation.PWSTR, use_last_error=False)(3, 'PutProperty', ((1, 'mkp'),(1, 'val'),)))
    return IMonikerProp
def _define_IBindProtocol_head():
    class IBindProtocol(win32more.System.Com.IUnknown_head):
        Guid = Guid('79eac9cd-baf9-11ce-8c82-00aa004ba90b')
    return IBindProtocol
def _define_IBindProtocol():
    IBindProtocol = win32more.System.Com.Urlmon.IBindProtocol_head
    IBindProtocol.CreateBinding = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.IBindCtx_head,POINTER(win32more.System.Com.IBinding_head), use_last_error=False)(3, 'CreateBinding', ((1, 'szUrl'),(1, 'pbc'),(1, 'ppb'),)))
    return IBindProtocol
BINDVERB = Int32
BINDVERB_GET = 0
BINDVERB_POST = 1
BINDVERB_PUT = 2
BINDVERB_CUSTOM = 3
BINDVERB_RESERVED1 = 4
BINDF = Int32
BINDF_ASYNCHRONOUS = 1
BINDF_ASYNCSTORAGE = 2
BINDF_NOPROGRESSIVERENDERING = 4
BINDF_OFFLINEOPERATION = 8
BINDF_GETNEWESTVERSION = 16
BINDF_NOWRITECACHE = 32
BINDF_NEEDFILE = 64
BINDF_PULLDATA = 128
BINDF_IGNORESECURITYPROBLEM = 256
BINDF_RESYNCHRONIZE = 512
BINDF_HYPERLINK = 1024
BINDF_NO_UI = 2048
BINDF_SILENTOPERATION = 4096
BINDF_PRAGMA_NO_CACHE = 8192
BINDF_GETCLASSOBJECT = 16384
BINDF_RESERVED_1 = 32768
BINDF_FREE_THREADED = 65536
BINDF_DIRECT_READ = 131072
BINDF_FORMS_SUBMIT = 262144
BINDF_GETFROMCACHE_IF_NET_FAIL = 524288
BINDF_FROMURLMON = 1048576
BINDF_FWD_BACK = 2097152
BINDF_PREFERDEFAULTHANDLER = 4194304
BINDF_ENFORCERESTRICTED = 8388608
BINDF_RESERVED_2 = -2147483648
BINDF_RESERVED_3 = 16777216
BINDF_RESERVED_4 = 33554432
BINDF_RESERVED_5 = 67108864
BINDF_RESERVED_6 = 134217728
BINDF_RESERVED_7 = 1073741824
BINDF_RESERVED_8 = 536870912
URL_ENCODING = Int32
URL_ENCODING_NONE = 0
URL_ENCODING_ENABLE_UTF8 = 268435456
URL_ENCODING_DISABLE_UTF8 = 536870912
def _define_REMSECURITY_ATTRIBUTES_head():
    class REMSECURITY_ATTRIBUTES(Structure):
        pass
    return REMSECURITY_ATTRIBUTES
def _define_REMSECURITY_ATTRIBUTES():
    REMSECURITY_ATTRIBUTES = win32more.System.Com.Urlmon.REMSECURITY_ATTRIBUTES_head
    REMSECURITY_ATTRIBUTES._fields_ = [
        ("nLength", UInt32),
        ("lpSecurityDescriptor", UInt32),
        ("bInheritHandle", win32more.Foundation.BOOL),
    ]
    return REMSECURITY_ATTRIBUTES
def _define_RemBINDINFO_head():
    class RemBINDINFO(Structure):
        pass
    return RemBINDINFO
def _define_RemBINDINFO():
    RemBINDINFO = win32more.System.Com.Urlmon.RemBINDINFO_head
    RemBINDINFO._fields_ = [
        ("cbSize", UInt32),
        ("szExtraInfo", win32more.Foundation.PWSTR),
        ("grfBindInfoF", UInt32),
        ("dwBindVerb", UInt32),
        ("szCustomVerb", win32more.Foundation.PWSTR),
        ("cbstgmedData", UInt32),
        ("dwOptions", UInt32),
        ("dwOptionsFlags", UInt32),
        ("dwCodePage", UInt32),
        ("securityAttributes", win32more.System.Com.Urlmon.REMSECURITY_ATTRIBUTES),
        ("iid", Guid),
        ("pUnk", win32more.System.Com.IUnknown_head),
        ("dwReserved", UInt32),
    ]
    return RemBINDINFO
def _define_RemFORMATETC_head():
    class RemFORMATETC(Structure):
        pass
    return RemFORMATETC
def _define_RemFORMATETC():
    RemFORMATETC = win32more.System.Com.Urlmon.RemFORMATETC_head
    RemFORMATETC._fields_ = [
        ("cfFormat", UInt32),
        ("ptd", UInt32),
        ("dwAspect", UInt32),
        ("lindex", Int32),
        ("tymed", UInt32),
    ]
    return RemFORMATETC
BINDINFO_OPTIONS = Int32
BINDINFO_OPTIONS_WININETFLAG = 65536
BINDINFO_OPTIONS_ENABLE_UTF8 = 131072
BINDINFO_OPTIONS_DISABLE_UTF8 = 262144
BINDINFO_OPTIONS_USE_IE_ENCODING = 524288
BINDINFO_OPTIONS_BINDTOOBJECT = 1048576
BINDINFO_OPTIONS_SECURITYOPTOUT = 2097152
BINDINFO_OPTIONS_IGNOREMIMETEXTPLAIN = 4194304
BINDINFO_OPTIONS_USEBINDSTRINGCREDS = 8388608
BINDINFO_OPTIONS_IGNOREHTTPHTTPSREDIRECTS = 16777216
BINDINFO_OPTIONS_IGNORE_SSLERRORS_ONCE = 33554432
BINDINFO_WPC_DOWNLOADBLOCKED = 134217728
BINDINFO_WPC_LOGGING_ENABLED = 268435456
BINDINFO_OPTIONS_ALLOWCONNECTDATA = 536870912
BINDINFO_OPTIONS_DISABLEAUTOREDIRECTS = 1073741824
BINDINFO_OPTIONS_SHDOCVW_NAVIGATE = -2147483648
BSCF = Int32
BSCF_FIRSTDATANOTIFICATION = 1
BSCF_INTERMEDIATEDATANOTIFICATION = 2
BSCF_LASTDATANOTIFICATION = 4
BSCF_DATAFULLYAVAILABLE = 8
BSCF_AVAILABLEDATASIZEUNKNOWN = 16
BSCF_SKIPDRAINDATAFORFILEURLS = 32
BSCF_64BITLENGTHDOWNLOAD = 64
BINDSTATUS = Int32
BINDSTATUS_FINDINGRESOURCE = 1
BINDSTATUS_CONNECTING = 2
BINDSTATUS_REDIRECTING = 3
BINDSTATUS_BEGINDOWNLOADDATA = 4
BINDSTATUS_DOWNLOADINGDATA = 5
BINDSTATUS_ENDDOWNLOADDATA = 6
BINDSTATUS_BEGINDOWNLOADCOMPONENTS = 7
BINDSTATUS_INSTALLINGCOMPONENTS = 8
BINDSTATUS_ENDDOWNLOADCOMPONENTS = 9
BINDSTATUS_USINGCACHEDCOPY = 10
BINDSTATUS_SENDINGREQUEST = 11
BINDSTATUS_CLASSIDAVAILABLE = 12
BINDSTATUS_MIMETYPEAVAILABLE = 13
BINDSTATUS_CACHEFILENAMEAVAILABLE = 14
BINDSTATUS_BEGINSYNCOPERATION = 15
BINDSTATUS_ENDSYNCOPERATION = 16
BINDSTATUS_BEGINUPLOADDATA = 17
BINDSTATUS_UPLOADINGDATA = 18
BINDSTATUS_ENDUPLOADDATA = 19
BINDSTATUS_PROTOCOLCLASSID = 20
BINDSTATUS_ENCODING = 21
BINDSTATUS_VERIFIEDMIMETYPEAVAILABLE = 22
BINDSTATUS_CLASSINSTALLLOCATION = 23
BINDSTATUS_DECODING = 24
BINDSTATUS_LOADINGMIMEHANDLER = 25
BINDSTATUS_CONTENTDISPOSITIONATTACH = 26
BINDSTATUS_FILTERREPORTMIMETYPE = 27
BINDSTATUS_CLSIDCANINSTANTIATE = 28
BINDSTATUS_IUNKNOWNAVAILABLE = 29
BINDSTATUS_DIRECTBIND = 30
BINDSTATUS_RAWMIMETYPE = 31
BINDSTATUS_PROXYDETECTING = 32
BINDSTATUS_ACCEPTRANGES = 33
BINDSTATUS_COOKIE_SENT = 34
BINDSTATUS_COMPACT_POLICY_RECEIVED = 35
BINDSTATUS_COOKIE_SUPPRESSED = 36
BINDSTATUS_COOKIE_STATE_UNKNOWN = 37
BINDSTATUS_COOKIE_STATE_ACCEPT = 38
BINDSTATUS_COOKIE_STATE_REJECT = 39
BINDSTATUS_COOKIE_STATE_PROMPT = 40
BINDSTATUS_COOKIE_STATE_LEASH = 41
BINDSTATUS_COOKIE_STATE_DOWNGRADE = 42
BINDSTATUS_POLICY_HREF = 43
BINDSTATUS_P3P_HEADER = 44
BINDSTATUS_SESSION_COOKIE_RECEIVED = 45
BINDSTATUS_PERSISTENT_COOKIE_RECEIVED = 46
BINDSTATUS_SESSION_COOKIES_ALLOWED = 47
BINDSTATUS_CACHECONTROL = 48
BINDSTATUS_CONTENTDISPOSITIONFILENAME = 49
BINDSTATUS_MIMETEXTPLAINMISMATCH = 50
BINDSTATUS_PUBLISHERAVAILABLE = 51
BINDSTATUS_DISPLAYNAMEAVAILABLE = 52
BINDSTATUS_SSLUX_NAVBLOCKED = 53
BINDSTATUS_SERVER_MIMETYPEAVAILABLE = 54
BINDSTATUS_SNIFFED_CLASSIDAVAILABLE = 55
BINDSTATUS_64BIT_PROGRESS = 56
BINDSTATUS_LAST = 56
BINDSTATUS_RESERVED_0 = 57
BINDSTATUS_RESERVED_1 = 58
BINDSTATUS_RESERVED_2 = 59
BINDSTATUS_RESERVED_3 = 60
BINDSTATUS_RESERVED_4 = 61
BINDSTATUS_RESERVED_5 = 62
BINDSTATUS_RESERVED_6 = 63
BINDSTATUS_RESERVED_7 = 64
BINDSTATUS_RESERVED_8 = 65
BINDSTATUS_RESERVED_9 = 66
BINDSTATUS_RESERVED_A = 67
BINDSTATUS_RESERVED_B = 68
BINDSTATUS_RESERVED_C = 69
BINDSTATUS_RESERVED_D = 70
BINDSTATUS_RESERVED_E = 71
BINDSTATUS_RESERVED_F = 72
BINDSTATUS_RESERVED_10 = 73
BINDSTATUS_RESERVED_11 = 74
BINDSTATUS_RESERVED_12 = 75
BINDSTATUS_RESERVED_13 = 76
BINDSTATUS_RESERVED_14 = 77
BINDSTATUS_LAST_PRIVATE = 77
BINDF2 = Int32
BINDF2_DISABLEBASICOVERHTTP = 1
BINDF2_DISABLEAUTOCOOKIEHANDLING = 2
BINDF2_READ_DATA_GREATER_THAN_4GB = 4
BINDF2_DISABLE_HTTP_REDIRECT_XSECURITYID = 8
BINDF2_SETDOWNLOADMODE = 32
BINDF2_DISABLE_HTTP_REDIRECT_CACHING = 64
BINDF2_KEEP_CALLBACK_MODULE_LOADED = 128
BINDF2_ALLOW_PROXY_CRED_PROMPT = 256
BINDF2_RESERVED_17 = 512
BINDF2_RESERVED_16 = 1024
BINDF2_RESERVED_15 = 2048
BINDF2_RESERVED_14 = 4096
BINDF2_RESERVED_13 = 8192
BINDF2_RESERVED_12 = 16384
BINDF2_RESERVED_11 = 32768
BINDF2_RESERVED_10 = 65536
BINDF2_RESERVED_F = 131072
BINDF2_RESERVED_E = 262144
BINDF2_RESERVED_D = 524288
BINDF2_RESERVED_C = 1048576
BINDF2_RESERVED_B = 2097152
BINDF2_RESERVED_A = 4194304
BINDF2_RESERVED_9 = 8388608
BINDF2_RESERVED_8 = 16777216
BINDF2_RESERVED_7 = 33554432
BINDF2_RESERVED_6 = 67108864
BINDF2_RESERVED_5 = 134217728
BINDF2_RESERVED_4 = 268435456
BINDF2_RESERVED_3 = 536870912
BINDF2_RESERVED_2 = 1073741824
BINDF2_RESERVED_1 = -2147483648
AUTHENTICATEF = Int32
AUTHENTICATEF_PROXY = 1
AUTHENTICATEF_BASIC = 2
AUTHENTICATEF_HTTP = 4
def _define_IHttpNegotiate_head():
    class IHttpNegotiate(win32more.System.Com.IUnknown_head):
        Guid = Guid('79eac9d2-baf9-11ce-8c82-00aa004ba90b')
    return IHttpNegotiate
def _define_IHttpNegotiate():
    IHttpNegotiate = win32more.System.Com.Urlmon.IHttpNegotiate_head
    IHttpNegotiate.BeginningTransaction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(3, 'BeginningTransaction', ((1, 'szURL'),(1, 'szHeaders'),(1, 'dwReserved'),(1, 'pszAdditionalHeaders'),)))
    IHttpNegotiate.OnResponse = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(4, 'OnResponse', ((1, 'dwResponseCode'),(1, 'szResponseHeaders'),(1, 'szRequestHeaders'),(1, 'pszAdditionalRequestHeaders'),)))
    return IHttpNegotiate
def _define_IHttpNegotiate2_head():
    class IHttpNegotiate2(win32more.System.Com.Urlmon.IHttpNegotiate_head):
        Guid = Guid('4f9f9fcb-e0f4-48eb-b7ab-fa2ea9365cb4')
    return IHttpNegotiate2
def _define_IHttpNegotiate2():
    IHttpNegotiate2 = win32more.System.Com.Urlmon.IHttpNegotiate2_head
    IHttpNegotiate2.GetRootSecurityId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),POINTER(UInt32),UIntPtr, use_last_error=False)(5, 'GetRootSecurityId', ((1, 'pbSecurityId'),(1, 'pcbSecurityId'),(1, 'dwReserved'),)))
    return IHttpNegotiate2
def _define_IHttpNegotiate3_head():
    class IHttpNegotiate3(win32more.System.Com.Urlmon.IHttpNegotiate2_head):
        Guid = Guid('57b6c80a-34c2-4602-bc26-66a02fc57153')
    return IHttpNegotiate3
def _define_IHttpNegotiate3():
    IHttpNegotiate3 = win32more.System.Com.Urlmon.IHttpNegotiate3_head
    IHttpNegotiate3.GetSerializedClientCertContext = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_char_p_no),POINTER(UInt32), use_last_error=False)(6, 'GetSerializedClientCertContext', ((1, 'ppbCert'),(1, 'pcbCert'),)))
    return IHttpNegotiate3
def _define_IWinInetFileStream_head():
    class IWinInetFileStream(win32more.System.Com.IUnknown_head):
        Guid = Guid('f134c4b7-b1f8-4e75-b886-74b90943becb')
    return IWinInetFileStream
def _define_IWinInetFileStream():
    IWinInetFileStream = win32more.System.Com.Urlmon.IWinInetFileStream_head
    IWinInetFileStream.SetHandleForUnlock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr,UIntPtr, use_last_error=False)(3, 'SetHandleForUnlock', ((1, 'hWinInetLockHandle'),(1, 'dwReserved'),)))
    IWinInetFileStream.SetDeleteFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr, use_last_error=False)(4, 'SetDeleteFile', ((1, 'dwReserved'),)))
    return IWinInetFileStream
def _define_IWindowForBindingUI_head():
    class IWindowForBindingUI(win32more.System.Com.IUnknown_head):
        Guid = Guid('79eac9d5-bafa-11ce-8c82-00aa004ba90b')
    return IWindowForBindingUI
def _define_IWindowForBindingUI():
    IWindowForBindingUI = win32more.System.Com.Urlmon.IWindowForBindingUI_head
    IWindowForBindingUI.GetWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(win32more.Foundation.HWND), use_last_error=False)(3, 'GetWindow', ((1, 'rguidReason'),(1, 'phwnd'),)))
    return IWindowForBindingUI
CIP_STATUS = Int32
CIP_DISK_FULL = 0
CIP_ACCESS_DENIED = 1
CIP_NEWER_VERSION_EXISTS = 2
CIP_OLDER_VERSION_EXISTS = 3
CIP_NAME_CONFLICT = 4
CIP_TRUST_VERIFICATION_COMPONENT_MISSING = 5
CIP_EXE_SELF_REGISTERATION_TIMEOUT = 6
CIP_UNSAFE_TO_ABORT = 7
CIP_NEED_REBOOT = 8
CIP_NEED_REBOOT_UI_PERMISSION = 9
def _define_ICodeInstall_head():
    class ICodeInstall(win32more.System.Com.Urlmon.IWindowForBindingUI_head):
        Guid = Guid('79eac9d1-baf9-11ce-8c82-00aa004ba90b')
    return ICodeInstall
def _define_ICodeInstall():
    ICodeInstall = win32more.System.Com.Urlmon.ICodeInstall_head
    ICodeInstall.OnCodeInstallProblem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(4, 'OnCodeInstallProblem', ((1, 'ulStatusCode'),(1, 'szDestination'),(1, 'szSource'),(1, 'dwReserved'),)))
    return ICodeInstall
Uri_HOST_TYPE = Int32
Uri_HOST_UNKNOWN = 0
Uri_HOST_DNS = 1
Uri_HOST_IPV4 = 2
Uri_HOST_IPV6 = 3
Uri_HOST_IDN = 4
def _define_IUriContainer_head():
    class IUriContainer(win32more.System.Com.IUnknown_head):
        Guid = Guid('a158a630-ed6f-45fb-b987-f68676f57752')
    return IUriContainer
def _define_IUriContainer():
    IUriContainer = win32more.System.Com.Urlmon.IUriContainer_head
    IUriContainer.GetIUri = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUri_head), use_last_error=False)(3, 'GetIUri', ((1, 'ppIUri'),)))
    return IUriContainer
def _define_IUriBuilderFactory_head():
    class IUriBuilderFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('e982ce48-0b96-440c-bc37-0c869b27a29e')
    return IUriBuilderFactory
def _define_IUriBuilderFactory():
    IUriBuilderFactory = win32more.System.Com.Urlmon.IUriBuilderFactory_head
    IUriBuilderFactory.CreateIUriBuilder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UIntPtr,POINTER(win32more.System.Com.IUriBuilder_head), use_last_error=False)(3, 'CreateIUriBuilder', ((1, 'dwFlags'),(1, 'dwReserved'),(1, 'ppIUriBuilder'),)))
    IUriBuilderFactory.CreateInitializedIUriBuilder = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UIntPtr,POINTER(win32more.System.Com.IUriBuilder_head), use_last_error=False)(4, 'CreateInitializedIUriBuilder', ((1, 'dwFlags'),(1, 'dwReserved'),(1, 'ppIUriBuilder'),)))
    return IUriBuilderFactory
def _define_IWinInetInfo_head():
    class IWinInetInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('79eac9d6-bafa-11ce-8c82-00aa004ba90b')
    return IWinInetInfo
def _define_IWinInetInfo():
    IWinInetInfo = win32more.System.Com.Urlmon.IWinInetInfo_head
    IWinInetInfo.QueryOption = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Void),POINTER(UInt32), use_last_error=False)(3, 'QueryOption', ((1, 'dwOption'),(1, 'pBuffer'),(1, 'pcbBuf'),)))
    return IWinInetInfo
def _define_IHttpSecurity_head():
    class IHttpSecurity(win32more.System.Com.Urlmon.IWindowForBindingUI_head):
        Guid = Guid('79eac9d7-bafa-11ce-8c82-00aa004ba90b')
    return IHttpSecurity
def _define_IHttpSecurity():
    IHttpSecurity = win32more.System.Com.Urlmon.IHttpSecurity_head
    IHttpSecurity.OnSecurityProblem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'OnSecurityProblem', ((1, 'dwProblem'),)))
    return IHttpSecurity
def _define_IWinInetHttpInfo_head():
    class IWinInetHttpInfo(win32more.System.Com.Urlmon.IWinInetInfo_head):
        Guid = Guid('79eac9d8-bafa-11ce-8c82-00aa004ba90b')
    return IWinInetHttpInfo
def _define_IWinInetHttpInfo():
    IWinInetHttpInfo = win32more.System.Com.Urlmon.IWinInetHttpInfo_head
    IWinInetHttpInfo.QueryInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Void),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(4, 'QueryInfo', ((1, 'dwOption'),(1, 'pBuffer'),(1, 'pcbBuf'),(1, 'pdwFlags'),(1, 'pdwReserved'),)))
    return IWinInetHttpInfo
def _define_IWinInetHttpTimeouts_head():
    class IWinInetHttpTimeouts(win32more.System.Com.IUnknown_head):
        Guid = Guid('f286fa56-c1fd-4270-8e67-b3eb790a81e8')
    return IWinInetHttpTimeouts
def _define_IWinInetHttpTimeouts():
    IWinInetHttpTimeouts = win32more.System.Com.Urlmon.IWinInetHttpTimeouts_head
    IWinInetHttpTimeouts.GetRequestTimeouts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(3, 'GetRequestTimeouts', ((1, 'pdwConnectTimeout'),(1, 'pdwSendTimeout'),(1, 'pdwReceiveTimeout'),)))
    return IWinInetHttpTimeouts
def _define_IWinInetCacheHints_head():
    class IWinInetCacheHints(win32more.System.Com.IUnknown_head):
        Guid = Guid('dd1ec3b3-8391-4fdb-a9e6-347c3caaa7dd')
    return IWinInetCacheHints
def _define_IWinInetCacheHints():
    IWinInetCacheHints = win32more.System.Com.Urlmon.IWinInetCacheHints_head
    IWinInetCacheHints.SetCacheExtension = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Void),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(3, 'SetCacheExtension', ((1, 'pwzExt'),(1, 'pszCacheFile'),(1, 'pcbCacheFile'),(1, 'pdwWinInetError'),(1, 'pdwReserved'),)))
    return IWinInetCacheHints
def _define_IWinInetCacheHints2_head():
    class IWinInetCacheHints2(win32more.System.Com.Urlmon.IWinInetCacheHints_head):
        Guid = Guid('7857aeac-d31f-49bf-884e-dd46df36780a')
    return IWinInetCacheHints2
def _define_IWinInetCacheHints2():
    IWinInetCacheHints2 = win32more.System.Com.Urlmon.IWinInetCacheHints2_head
    IWinInetCacheHints2.SetCacheExtension2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(4, 'SetCacheExtension2', ((1, 'pwzExt'),(1, 'pwzCacheFile'),(1, 'pcchCacheFile'),(1, 'pdwWinInetError'),(1, 'pdwReserved'),)))
    return IWinInetCacheHints2
def _define_IInternet_head():
    class IInternet(win32more.System.Com.IUnknown_head):
        Guid = Guid('79eac9e0-baf9-11ce-8c82-00aa004ba90b')
    return IInternet
def _define_IInternet():
    IInternet = win32more.System.Com.Urlmon.IInternet_head
    return IInternet
BINDSTRING = Int32
BINDSTRING_HEADERS = 1
BINDSTRING_ACCEPT_MIMES = 2
BINDSTRING_EXTRA_URL = 3
BINDSTRING_LANGUAGE = 4
BINDSTRING_USERNAME = 5
BINDSTRING_PASSWORD = 6
BINDSTRING_UA_PIXELS = 7
BINDSTRING_UA_COLOR = 8
BINDSTRING_OS = 9
BINDSTRING_USER_AGENT = 10
BINDSTRING_ACCEPT_ENCODINGS = 11
BINDSTRING_POST_COOKIE = 12
BINDSTRING_POST_DATA_MIME = 13
BINDSTRING_URL = 14
BINDSTRING_IID = 15
BINDSTRING_FLAG_BIND_TO_OBJECT = 16
BINDSTRING_PTR_BIND_CONTEXT = 17
BINDSTRING_XDR_ORIGIN = 18
BINDSTRING_DOWNLOADPATH = 19
BINDSTRING_ROOTDOC_URL = 20
BINDSTRING_INITIAL_FILENAME = 21
BINDSTRING_PROXY_USERNAME = 22
BINDSTRING_PROXY_PASSWORD = 23
BINDSTRING_ENTERPRISE_ID = 24
BINDSTRING_DOC_URL = 25
BINDSTRING_SAMESITE_COOKIE_LEVEL = 26
def _define_IInternetBindInfo_head():
    class IInternetBindInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('79eac9e1-baf9-11ce-8c82-00aa004ba90b')
    return IInternetBindInfo
def _define_IInternetBindInfo():
    IInternetBindInfo = win32more.System.Com.Urlmon.IInternetBindInfo_head
    IInternetBindInfo.GetBindInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(win32more.System.Com.BINDINFO_head), use_last_error=False)(3, 'GetBindInfo', ((1, 'grfBINDF'),(1, 'pbindinfo'),)))
    IInternetBindInfo.GetBindString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.PWSTR),UInt32,POINTER(UInt32), use_last_error=False)(4, 'GetBindString', ((1, 'ulStringType'),(1, 'ppwzStr'),(1, 'cEl'),(1, 'pcElFetched'),)))
    return IInternetBindInfo
def _define_IInternetBindInfoEx_head():
    class IInternetBindInfoEx(win32more.System.Com.Urlmon.IInternetBindInfo_head):
        Guid = Guid('a3e015b7-a82c-4dcd-a150-569aeeed36ab')
    return IInternetBindInfoEx
def _define_IInternetBindInfoEx():
    IInternetBindInfoEx = win32more.System.Com.Urlmon.IInternetBindInfoEx_head
    IInternetBindInfoEx.GetBindInfoEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(win32more.System.Com.BINDINFO_head),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(5, 'GetBindInfoEx', ((1, 'grfBINDF'),(1, 'pbindinfo'),(1, 'grfBINDF2'),(1, 'pdwReserved'),)))
    return IInternetBindInfoEx
PI_FLAGS = Int32
PI_PARSE_URL = 1
PI_FILTER_MODE = 2
PI_FORCE_ASYNC = 4
PI_USE_WORKERTHREAD = 8
PI_MIMEVERIFICATION = 16
PI_CLSIDLOOKUP = 32
PI_DATAPROGRESS = 64
PI_SYNCHRONOUS = 128
PI_APARTMENTTHREADED = 256
PI_CLASSINSTALL = 512
PI_PASSONBINDCTX = 8192
PI_NOMIMEHANDLER = 32768
PI_LOADAPPDIRECT = 16384
PD_FORCE_SWITCH = 65536
PI_PREFERDEFAULTHANDLER = 131072
def _define_PROTOCOLDATA_head():
    class PROTOCOLDATA(Structure):
        pass
    return PROTOCOLDATA
def _define_PROTOCOLDATA():
    PROTOCOLDATA = win32more.System.Com.Urlmon.PROTOCOLDATA_head
    PROTOCOLDATA._fields_ = [
        ("grfFlags", UInt32),
        ("dwState", UInt32),
        ("pData", c_void_p),
        ("cbData", UInt32),
    ]
    return PROTOCOLDATA
def _define_StartParam_head():
    class StartParam(Structure):
        pass
    return StartParam
def _define_StartParam():
    StartParam = win32more.System.Com.Urlmon.StartParam_head
    StartParam._fields_ = [
        ("iid", Guid),
        ("pIBindCtx", win32more.System.Com.IBindCtx_head),
        ("pItf", win32more.System.Com.IUnknown_head),
    ]
    return StartParam
def _define_IInternetProtocolRoot_head():
    class IInternetProtocolRoot(win32more.System.Com.IUnknown_head):
        Guid = Guid('79eac9e3-baf9-11ce-8c82-00aa004ba90b')
    return IInternetProtocolRoot
def _define_IInternetProtocolRoot():
    IInternetProtocolRoot = win32more.System.Com.Urlmon.IInternetProtocolRoot_head
    IInternetProtocolRoot.Start = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.Urlmon.IInternetProtocolSink_head,win32more.System.Com.Urlmon.IInternetBindInfo_head,UInt32,win32more.Foundation.HANDLE_PTR, use_last_error=False)(3, 'Start', ((1, 'szUrl'),(1, 'pOIProtSink'),(1, 'pOIBindInfo'),(1, 'grfPI'),(1, 'dwReserved'),)))
    IInternetProtocolRoot.Continue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.Urlmon.PROTOCOLDATA_head), use_last_error=False)(4, 'Continue', ((1, 'pProtocolData'),)))
    IInternetProtocolRoot.Abort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'Abort', ((1, 'hrReason'),(1, 'dwOptions'),)))
    IInternetProtocolRoot.Terminate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(6, 'Terminate', ((1, 'dwOptions'),)))
    IInternetProtocolRoot.Suspend = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(7, 'Suspend', ()))
    IInternetProtocolRoot.Resume = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'Resume', ()))
    return IInternetProtocolRoot
def _define_IInternetProtocol_head():
    class IInternetProtocol(win32more.System.Com.Urlmon.IInternetProtocolRoot_head):
        Guid = Guid('79eac9e4-baf9-11ce-8c82-00aa004ba90b')
    return IInternetProtocol
def _define_IInternetProtocol():
    IInternetProtocol = win32more.System.Com.Urlmon.IInternetProtocol_head
    IInternetProtocol.Read = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Void),UInt32,POINTER(UInt32), use_last_error=False)(9, 'Read', ((1, 'pv'),(1, 'cb'),(1, 'pcbRead'),)))
    IInternetProtocol.Seek = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.LARGE_INTEGER,UInt32,POINTER(win32more.Foundation.ULARGE_INTEGER_head), use_last_error=False)(10, 'Seek', ((1, 'dlibMove'),(1, 'dwOrigin'),(1, 'plibNewPosition'),)))
    IInternetProtocol.LockRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(11, 'LockRequest', ((1, 'dwOptions'),)))
    IInternetProtocol.UnlockRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(12, 'UnlockRequest', ()))
    return IInternetProtocol
def _define_IInternetProtocolEx_head():
    class IInternetProtocolEx(win32more.System.Com.Urlmon.IInternetProtocol_head):
        Guid = Guid('c7a98e66-1010-492c-a1c8-c809e1f75905')
    return IInternetProtocolEx
def _define_IInternetProtocolEx():
    IInternetProtocolEx = win32more.System.Com.Urlmon.IInternetProtocolEx_head
    IInternetProtocolEx.StartEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUri_head,win32more.System.Com.Urlmon.IInternetProtocolSink_head,win32more.System.Com.Urlmon.IInternetBindInfo_head,UInt32,win32more.Foundation.HANDLE_PTR, use_last_error=False)(13, 'StartEx', ((1, 'pUri'),(1, 'pOIProtSink'),(1, 'pOIBindInfo'),(1, 'grfPI'),(1, 'dwReserved'),)))
    return IInternetProtocolEx
def _define_IInternetProtocolSink_head():
    class IInternetProtocolSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('79eac9e5-baf9-11ce-8c82-00aa004ba90b')
    return IInternetProtocolSink
def _define_IInternetProtocolSink():
    IInternetProtocolSink = win32more.System.Com.Urlmon.IInternetProtocolSink_head
    IInternetProtocolSink.Switch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.Urlmon.PROTOCOLDATA_head), use_last_error=False)(3, 'Switch', ((1, 'pProtocolData'),)))
    IInternetProtocolSink.ReportProgress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(4, 'ReportProgress', ((1, 'ulStatusCode'),(1, 'szStatusText'),)))
    IInternetProtocolSink.ReportData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32, use_last_error=False)(5, 'ReportData', ((1, 'grfBSCF'),(1, 'ulProgress'),(1, 'ulProgressMax'),)))
    IInternetProtocolSink.ReportResult = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR, use_last_error=False)(6, 'ReportResult', ((1, 'hrResult'),(1, 'dwError'),(1, 'szResult'),)))
    return IInternetProtocolSink
def _define_IInternetProtocolSinkStackable_head():
    class IInternetProtocolSinkStackable(win32more.System.Com.IUnknown_head):
        Guid = Guid('79eac9f0-baf9-11ce-8c82-00aa004ba90b')
    return IInternetProtocolSinkStackable
def _define_IInternetProtocolSinkStackable():
    IInternetProtocolSinkStackable = win32more.System.Com.Urlmon.IInternetProtocolSinkStackable_head
    IInternetProtocolSinkStackable.SwitchSink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.Urlmon.IInternetProtocolSink_head, use_last_error=False)(3, 'SwitchSink', ((1, 'pOIProtSink'),)))
    IInternetProtocolSinkStackable.CommitSwitch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'CommitSwitch', ()))
    IInternetProtocolSinkStackable.RollbackSwitch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'RollbackSwitch', ()))
    return IInternetProtocolSinkStackable
OIBDG_FLAGS = Int32
OIBDG_APARTMENTTHREADED = 256
OIBDG_DATAONLY = 4096
def _define_IInternetSession_head():
    class IInternetSession(win32more.System.Com.IUnknown_head):
        Guid = Guid('79eac9e7-baf9-11ce-8c82-00aa004ba90b')
    return IInternetSession
def _define_IInternetSession():
    IInternetSession = win32more.System.Com.Urlmon.IInternetSession_head
    IInternetSession.RegisterNameSpace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IClassFactory_head,POINTER(Guid),win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Foundation.PWSTR),UInt32, use_last_error=False)(3, 'RegisterNameSpace', ((1, 'pCF'),(1, 'rclsid'),(1, 'pwzProtocol'),(1, 'cPatterns'),(1, 'ppwzPatterns'),(1, 'dwReserved'),)))
    IInternetSession.UnregisterNameSpace = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IClassFactory_head,win32more.Foundation.PWSTR, use_last_error=False)(4, 'UnregisterNameSpace', ((1, 'pCF'),(1, 'pszProtocol'),)))
    IInternetSession.RegisterMimeFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IClassFactory_head,POINTER(Guid),win32more.Foundation.PWSTR, use_last_error=False)(5, 'RegisterMimeFilter', ((1, 'pCF'),(1, 'rclsid'),(1, 'pwzType'),)))
    IInternetSession.UnregisterMimeFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IClassFactory_head,win32more.Foundation.PWSTR, use_last_error=False)(6, 'UnregisterMimeFilter', ((1, 'pCF'),(1, 'pwzType'),)))
    IInternetSession.CreateBinding = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IBindCtx_head,win32more.Foundation.PWSTR,win32more.System.Com.IUnknown_head,POINTER(win32more.System.Com.IUnknown_head),POINTER(win32more.System.Com.Urlmon.IInternetProtocol_head),UInt32, use_last_error=False)(7, 'CreateBinding', ((1, 'pBC'),(1, 'szUrl'),(1, 'pUnkOuter'),(1, 'ppUnk'),(1, 'ppOInetProt'),(1, 'dwOption'),)))
    IInternetSession.SetSessionOption = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p,UInt32,UInt32, use_last_error=False)(8, 'SetSessionOption', ((1, 'dwOption'),(1, 'pBuffer'),(1, 'dwBufferLength'),(1, 'dwReserved'),)))
    IInternetSession.GetSessionOption = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p,POINTER(UInt32),UInt32, use_last_error=False)(9, 'GetSessionOption', ((1, 'dwOption'),(1, 'pBuffer'),(1, 'pdwBufferLength'),(1, 'dwReserved'),)))
    return IInternetSession
def _define_IInternetThreadSwitch_head():
    class IInternetThreadSwitch(win32more.System.Com.IUnknown_head):
        Guid = Guid('79eac9e8-baf9-11ce-8c82-00aa004ba90b')
    return IInternetThreadSwitch
def _define_IInternetThreadSwitch():
    IInternetThreadSwitch = win32more.System.Com.Urlmon.IInternetThreadSwitch_head
    IInternetThreadSwitch.Prepare = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(3, 'Prepare', ()))
    IInternetThreadSwitch.Continue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(4, 'Continue', ()))
    return IInternetThreadSwitch
def _define_IInternetPriority_head():
    class IInternetPriority(win32more.System.Com.IUnknown_head):
        Guid = Guid('79eac9eb-baf9-11ce-8c82-00aa004ba90b')
    return IInternetPriority
def _define_IInternetPriority():
    IInternetPriority = win32more.System.Com.Urlmon.IInternetPriority_head
    IInternetPriority.SetPriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32, use_last_error=False)(3, 'SetPriority', ((1, 'nPriority'),)))
    IInternetPriority.GetPriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32), use_last_error=False)(4, 'GetPriority', ((1, 'pnPriority'),)))
    return IInternetPriority
PARSEACTION = Int32
PARSE_CANONICALIZE = 1
PARSE_FRIENDLY = 2
PARSE_SECURITY_URL = 3
PARSE_ROOTDOCUMENT = 4
PARSE_DOCUMENT = 5
PARSE_ANCHOR = 6
PARSE_ENCODE_IS_UNESCAPE = 7
PARSE_DECODE_IS_ESCAPE = 8
PARSE_PATH_FROM_URL = 9
PARSE_URL_FROM_PATH = 10
PARSE_MIME = 11
PARSE_SERVER = 12
PARSE_SCHEMA = 13
PARSE_SITE = 14
PARSE_DOMAIN = 15
PARSE_LOCATION = 16
PARSE_SECURITY_DOMAIN = 17
PARSE_ESCAPE = 18
PARSE_UNESCAPE = 19
PSUACTION = Int32
PSU_DEFAULT = 1
PSU_SECURITY_URL_ONLY = 2
QUERYOPTION = Int32
QUERY_EXPIRATION_DATE = 1
QUERY_TIME_OF_LAST_CHANGE = 2
QUERY_CONTENT_ENCODING = 3
QUERY_CONTENT_TYPE = 4
QUERY_REFRESH = 5
QUERY_RECOMBINE = 6
QUERY_CAN_NAVIGATE = 7
QUERY_USES_NETWORK = 8
QUERY_IS_CACHED = 9
QUERY_IS_INSTALLEDENTRY = 10
QUERY_IS_CACHED_OR_MAPPED = 11
QUERY_USES_CACHE = 12
QUERY_IS_SECURE = 13
QUERY_IS_SAFE = 14
QUERY_USES_HISTORYFOLDER = 15
QUERY_IS_CACHED_AND_USABLE_OFFLINE = 16
def _define_IInternetProtocolInfo_head():
    class IInternetProtocolInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('79eac9ec-baf9-11ce-8c82-00aa004ba90b')
    return IInternetProtocolInfo
def _define_IInternetProtocolInfo():
    IInternetProtocolInfo = win32more.System.Com.Urlmon.IInternetProtocolInfo_head
    IInternetProtocolInfo.ParseUrl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.Urlmon.PARSEACTION,UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),UInt32, use_last_error=False)(3, 'ParseUrl', ((1, 'pwzUrl'),(1, 'ParseAction'),(1, 'dwParseFlags'),(1, 'pwzResult'),(1, 'cchResult'),(1, 'pcchResult'),(1, 'dwReserved'),)))
    IInternetProtocolInfo.CombineUrl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),UInt32, use_last_error=False)(4, 'CombineUrl', ((1, 'pwzBaseUrl'),(1, 'pwzRelativeUrl'),(1, 'dwCombineFlags'),(1, 'pwzResult'),(1, 'cchResult'),(1, 'pcchResult'),(1, 'dwReserved'),)))
    IInternetProtocolInfo.CompareUrl = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(5, 'CompareUrl', ((1, 'pwzUrl1'),(1, 'pwzUrl2'),(1, 'dwCompareFlags'),)))
    IInternetProtocolInfo.QueryInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.Urlmon.QUERYOPTION,UInt32,POINTER(Void),UInt32,POINTER(UInt32),UInt32, use_last_error=False)(6, 'QueryInfo', ((1, 'pwzUrl'),(1, 'OueryOption'),(1, 'dwQueryFlags'),(1, 'pBuffer'),(1, 'cbBuffer'),(1, 'pcbBuf'),(1, 'dwReserved'),)))
    return IInternetProtocolInfo
INTERNETFEATURELIST = Int32
FEATURE_OBJECT_CACHING = 0
FEATURE_ZONE_ELEVATION = 1
FEATURE_MIME_HANDLING = 2
FEATURE_MIME_SNIFFING = 3
FEATURE_WINDOW_RESTRICTIONS = 4
FEATURE_WEBOC_POPUPMANAGEMENT = 5
FEATURE_BEHAVIORS = 6
FEATURE_DISABLE_MK_PROTOCOL = 7
FEATURE_LOCALMACHINE_LOCKDOWN = 8
FEATURE_SECURITYBAND = 9
FEATURE_RESTRICT_ACTIVEXINSTALL = 10
FEATURE_VALIDATE_NAVIGATE_URL = 11
FEATURE_RESTRICT_FILEDOWNLOAD = 12
FEATURE_ADDON_MANAGEMENT = 13
FEATURE_PROTOCOL_LOCKDOWN = 14
FEATURE_HTTP_USERNAME_PASSWORD_DISABLE = 15
FEATURE_SAFE_BINDTOOBJECT = 16
FEATURE_UNC_SAVEDFILECHECK = 17
FEATURE_GET_URL_DOM_FILEPATH_UNENCODED = 18
FEATURE_TABBED_BROWSING = 19
FEATURE_SSLUX = 20
FEATURE_DISABLE_NAVIGATION_SOUNDS = 21
FEATURE_DISABLE_LEGACY_COMPRESSION = 22
FEATURE_FORCE_ADDR_AND_STATUS = 23
FEATURE_XMLHTTP = 24
FEATURE_DISABLE_TELNET_PROTOCOL = 25
FEATURE_FEEDS = 26
FEATURE_BLOCK_INPUT_PROMPTS = 27
FEATURE_ENTRY_COUNT = 28
def _define_IInternetSecurityMgrSite_head():
    class IInternetSecurityMgrSite(win32more.System.Com.IUnknown_head):
        Guid = Guid('79eac9ed-baf9-11ce-8c82-00aa004ba90b')
    return IInternetSecurityMgrSite
def _define_IInternetSecurityMgrSite():
    IInternetSecurityMgrSite = win32more.System.Com.Urlmon.IInternetSecurityMgrSite_head
    IInternetSecurityMgrSite.GetWindow = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HWND), use_last_error=False)(3, 'GetWindow', ((1, 'phwnd'),)))
    IInternetSecurityMgrSite.EnableModeless = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL, use_last_error=False)(4, 'EnableModeless', ((1, 'fEnable'),)))
    return IInternetSecurityMgrSite
PUAF = Int32
PUAF_DEFAULT = 0
PUAF_NOUI = 1
PUAF_ISFILE = 2
PUAF_WARN_IF_DENIED = 4
PUAF_FORCEUI_FOREGROUND = 8
PUAF_CHECK_TIFS = 16
PUAF_DONTCHECKBOXINDIALOG = 32
PUAF_TRUSTED = 64
PUAF_ACCEPT_WILDCARD_SCHEME = 128
PUAF_ENFORCERESTRICTED = 256
PUAF_NOSAVEDFILECHECK = 512
PUAF_REQUIRESAVEDFILECHECK = 1024
PUAF_DONT_USE_CACHE = 4096
PUAF_RESERVED1 = 8192
PUAF_RESERVED2 = 16384
PUAF_LMZ_UNLOCKED = 65536
PUAF_LMZ_LOCKED = 131072
PUAF_DEFAULTZONEPOL = 262144
PUAF_NPL_USE_LOCKED_IF_RESTRICTED = 524288
PUAF_NOUIIFLOCKED = 1048576
PUAF_DRAGPROTOCOLCHECK = 2097152
PUAFOUT = Int32
PUAFOUT_DEFAULT = 0
PUAFOUT_ISLOCKZONEPOLICY = 1
SZM_FLAGS = Int32
SZM_CREATE = 0
SZM_DELETE = 1
def _define_IInternetSecurityManager_head():
    class IInternetSecurityManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('79eac9ee-baf9-11ce-8c82-00aa004ba90b')
    return IInternetSecurityManager
def _define_IInternetSecurityManager():
    IInternetSecurityManager = win32more.System.Com.Urlmon.IInternetSecurityManager_head
    IInternetSecurityManager.SetSecuritySite = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.Urlmon.IInternetSecurityMgrSite_head, use_last_error=False)(3, 'SetSecuritySite', ((1, 'pSite'),)))
    IInternetSecurityManager.GetSecuritySite = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.Urlmon.IInternetSecurityMgrSite_head), use_last_error=False)(4, 'GetSecuritySite', ((1, 'ppSite'),)))
    IInternetSecurityManager.MapUrlToZone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32),UInt32, use_last_error=False)(5, 'MapUrlToZone', ((1, 'pwszUrl'),(1, 'pdwZone'),(1, 'dwFlags'),)))
    IInternetSecurityManager.GetSecurityId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Byte),POINTER(UInt32),UIntPtr, use_last_error=False)(6, 'GetSecurityId', ((1, 'pwszUrl'),(1, 'pbSecurityId'),(1, 'pcbSecurityId'),(1, 'dwReserved'),)))
    IInternetSecurityManager.ProcessUrlAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(Byte),UInt32,c_char_p_no,UInt32,UInt32,UInt32, use_last_error=False)(7, 'ProcessUrlAction', ((1, 'pwszUrl'),(1, 'dwAction'),(1, 'pPolicy'),(1, 'cbPolicy'),(1, 'pContext'),(1, 'cbContext'),(1, 'dwFlags'),(1, 'dwReserved'),)))
    IInternetSecurityManager.QueryCustomPolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid),POINTER(c_char_p_no),POINTER(UInt32),c_char_p_no,UInt32,UInt32, use_last_error=False)(8, 'QueryCustomPolicy', ((1, 'pwszUrl'),(1, 'guidKey'),(1, 'ppPolicy'),(1, 'pcbPolicy'),(1, 'pContext'),(1, 'cbContext'),(1, 'dwReserved'),)))
    IInternetSecurityManager.SetZoneMapping = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(9, 'SetZoneMapping', ((1, 'dwZone'),(1, 'lpszPattern'),(1, 'dwFlags'),)))
    IInternetSecurityManager.GetZoneMappings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.IEnumString_head),UInt32, use_last_error=False)(10, 'GetZoneMappings', ((1, 'dwZone'),(1, 'ppenumString'),(1, 'dwFlags'),)))
    return IInternetSecurityManager
def _define_IInternetSecurityManagerEx_head():
    class IInternetSecurityManagerEx(win32more.System.Com.Urlmon.IInternetSecurityManager_head):
        Guid = Guid('f164edf1-cc7c-4f0d-9a94-34222625c393')
    return IInternetSecurityManagerEx
def _define_IInternetSecurityManagerEx():
    IInternetSecurityManagerEx = win32more.System.Com.Urlmon.IInternetSecurityManagerEx_head
    IInternetSecurityManagerEx.ProcessUrlActionEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(Byte),UInt32,c_char_p_no,UInt32,UInt32,UInt32,POINTER(UInt32), use_last_error=False)(11, 'ProcessUrlActionEx', ((1, 'pwszUrl'),(1, 'dwAction'),(1, 'pPolicy'),(1, 'cbPolicy'),(1, 'pContext'),(1, 'cbContext'),(1, 'dwFlags'),(1, 'dwReserved'),(1, 'pdwOutFlags'),)))
    return IInternetSecurityManagerEx
def _define_IInternetSecurityManagerEx2_head():
    class IInternetSecurityManagerEx2(win32more.System.Com.Urlmon.IInternetSecurityManagerEx_head):
        Guid = Guid('f1e50292-a795-4117-8e09-2b560a72ac60')
    return IInternetSecurityManagerEx2
def _define_IInternetSecurityManagerEx2():
    IInternetSecurityManagerEx2 = win32more.System.Com.Urlmon.IInternetSecurityManagerEx2_head
    IInternetSecurityManagerEx2.MapUrlToZoneEx2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUri_head,POINTER(UInt32),UInt32,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32), use_last_error=False)(12, 'MapUrlToZoneEx2', ((1, 'pUri'),(1, 'pdwZone'),(1, 'dwFlags'),(1, 'ppwszMappedUrl'),(1, 'pdwOutFlags'),)))
    IInternetSecurityManagerEx2.ProcessUrlActionEx2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUri_head,UInt32,POINTER(Byte),UInt32,c_char_p_no,UInt32,UInt32,UIntPtr,POINTER(UInt32), use_last_error=False)(13, 'ProcessUrlActionEx2', ((1, 'pUri'),(1, 'dwAction'),(1, 'pPolicy'),(1, 'cbPolicy'),(1, 'pContext'),(1, 'cbContext'),(1, 'dwFlags'),(1, 'dwReserved'),(1, 'pdwOutFlags'),)))
    IInternetSecurityManagerEx2.GetSecurityIdEx2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUri_head,POINTER(Byte),POINTER(UInt32),UIntPtr, use_last_error=False)(14, 'GetSecurityIdEx2', ((1, 'pUri'),(1, 'pbSecurityId'),(1, 'pcbSecurityId'),(1, 'dwReserved'),)))
    IInternetSecurityManagerEx2.QueryCustomPolicyEx2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUri_head,POINTER(Guid),POINTER(c_char_p_no),POINTER(UInt32),c_char_p_no,UInt32,UIntPtr, use_last_error=False)(15, 'QueryCustomPolicyEx2', ((1, 'pUri'),(1, 'guidKey'),(1, 'ppPolicy'),(1, 'pcbPolicy'),(1, 'pContext'),(1, 'cbContext'),(1, 'dwReserved'),)))
    return IInternetSecurityManagerEx2
def _define_IZoneIdentifier_head():
    class IZoneIdentifier(win32more.System.Com.IUnknown_head):
        Guid = Guid('cd45f185-1b21-48e2-967b-ead743a8914e')
    return IZoneIdentifier
def _define_IZoneIdentifier():
    IZoneIdentifier = win32more.System.Com.Urlmon.IZoneIdentifier_head
    IZoneIdentifier.GetId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetId', ((1, 'pdwZone'),)))
    IZoneIdentifier.SetId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(4, 'SetId', ((1, 'dwZone'),)))
    IZoneIdentifier.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(5, 'Remove', ()))
    return IZoneIdentifier
def _define_IZoneIdentifier2_head():
    class IZoneIdentifier2(win32more.System.Com.Urlmon.IZoneIdentifier_head):
        Guid = Guid('eb5e760c-09ef-45c0-b510-70830ce31e6a')
    return IZoneIdentifier2
def _define_IZoneIdentifier2():
    IZoneIdentifier2 = win32more.System.Com.Urlmon.IZoneIdentifier2_head
    IZoneIdentifier2.GetLastWriterPackageFamilyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(6, 'GetLastWriterPackageFamilyName', ((1, 'packageFamilyName'),)))
    IZoneIdentifier2.SetLastWriterPackageFamilyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR, use_last_error=False)(7, 'SetLastWriterPackageFamilyName', ((1, 'packageFamilyName'),)))
    IZoneIdentifier2.RemoveLastWriterPackageFamilyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(8, 'RemoveLastWriterPackageFamilyName', ()))
    IZoneIdentifier2.GetAppZoneId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(9, 'GetAppZoneId', ((1, 'zone'),)))
    IZoneIdentifier2.SetAppZoneId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(10, 'SetAppZoneId', ((1, 'zone'),)))
    IZoneIdentifier2.RemoveAppZoneId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(11, 'RemoveAppZoneId', ()))
    return IZoneIdentifier2
def _define_IInternetHostSecurityManager_head():
    class IInternetHostSecurityManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('3af280b6-cb3f-11d0-891e-00c04fb6bfc4')
    return IInternetHostSecurityManager
def _define_IInternetHostSecurityManager():
    IInternetHostSecurityManager = win32more.System.Com.Urlmon.IInternetHostSecurityManager_head
    IInternetHostSecurityManager.GetSecurityId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),POINTER(UInt32),UIntPtr, use_last_error=False)(3, 'GetSecurityId', ((1, 'pbSecurityId'),(1, 'pcbSecurityId'),(1, 'dwReserved'),)))
    IInternetHostSecurityManager.ProcessUrlAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_char_p_no,UInt32,POINTER(Byte),UInt32,UInt32,UInt32, use_last_error=False)(4, 'ProcessUrlAction', ((1, 'dwAction'),(1, 'pPolicy'),(1, 'cbPolicy'),(1, 'pContext'),(1, 'cbContext'),(1, 'dwFlags'),(1, 'dwReserved'),)))
    IInternetHostSecurityManager.QueryCustomPolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(c_char_p_no),POINTER(UInt32),POINTER(Byte),UInt32,UInt32, use_last_error=False)(5, 'QueryCustomPolicy', ((1, 'guidKey'),(1, 'ppPolicy'),(1, 'pcbPolicy'),(1, 'pContext'),(1, 'cbContext'),(1, 'dwReserved'),)))
    return IInternetHostSecurityManager
URLZONE = Int32
URLZONE_INVALID = -1
URLZONE_PREDEFINED_MIN = 0
URLZONE_LOCAL_MACHINE = 0
URLZONE_INTRANET = 1
URLZONE_TRUSTED = 2
URLZONE_INTERNET = 3
URLZONE_UNTRUSTED = 4
URLZONE_PREDEFINED_MAX = 999
URLZONE_USER_MIN = 1000
URLZONE_USER_MAX = 10000
URLTEMPLATE = Int32
URLTEMPLATE_CUSTOM = 0
URLTEMPLATE_PREDEFINED_MIN = 65536
URLTEMPLATE_LOW = 65536
URLTEMPLATE_MEDLOW = 66816
URLTEMPLATE_MEDIUM = 69632
URLTEMPLATE_MEDHIGH = 70912
URLTEMPLATE_HIGH = 73728
URLTEMPLATE_PREDEFINED_MAX = 131072
INET_ZONE_MANAGER_CONSTANTS = Int32
MAX_ZONE_PATH = 260
MAX_ZONE_DESCRIPTION = 200
ZAFLAGS = Int32
ZAFLAGS_CUSTOM_EDIT = 1
ZAFLAGS_ADD_SITES = 2
ZAFLAGS_REQUIRE_VERIFICATION = 4
ZAFLAGS_INCLUDE_PROXY_OVERRIDE = 8
ZAFLAGS_INCLUDE_INTRANET_SITES = 16
ZAFLAGS_NO_UI = 32
ZAFLAGS_SUPPORTS_VERIFICATION = 64
ZAFLAGS_UNC_AS_INTRANET = 128
ZAFLAGS_DETECT_INTRANET = 256
ZAFLAGS_USE_LOCKED_ZONES = 65536
ZAFLAGS_VERIFY_TEMPLATE_SETTINGS = 131072
ZAFLAGS_NO_CACHE = 262144
def _define_ZONEATTRIBUTES_head():
    class ZONEATTRIBUTES(Structure):
        pass
    return ZONEATTRIBUTES
def _define_ZONEATTRIBUTES():
    ZONEATTRIBUTES = win32more.System.Com.Urlmon.ZONEATTRIBUTES_head
    ZONEATTRIBUTES._fields_ = [
        ("cbSize", UInt32),
        ("szDisplayName", Char * 260),
        ("szDescription", Char * 200),
        ("szIconPath", Char * 260),
        ("dwTemplateMinLevel", UInt32),
        ("dwTemplateRecommended", UInt32),
        ("dwTemplateCurrentLevel", UInt32),
        ("dwFlags", UInt32),
    ]
    return ZONEATTRIBUTES
URLZONEREG = Int32
URLZONEREG_DEFAULT = 0
URLZONEREG_HKLM = 1
URLZONEREG_HKCU = 2
def _define_IInternetZoneManager_head():
    class IInternetZoneManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('79eac9ef-baf9-11ce-8c82-00aa004ba90b')
    return IInternetZoneManager
def _define_IInternetZoneManager():
    IInternetZoneManager = win32more.System.Com.Urlmon.IInternetZoneManager_head
    IInternetZoneManager.GetZoneAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.Urlmon.ZONEATTRIBUTES_head), use_last_error=False)(3, 'GetZoneAttributes', ((1, 'dwZone'),(1, 'pZoneAttributes'),)))
    IInternetZoneManager.SetZoneAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.Urlmon.ZONEATTRIBUTES_head), use_last_error=False)(4, 'SetZoneAttributes', ((1, 'dwZone'),(1, 'pZoneAttributes'),)))
    IInternetZoneManager.GetZoneCustomPolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(c_char_p_no),POINTER(UInt32),win32more.System.Com.Urlmon.URLZONEREG, use_last_error=False)(5, 'GetZoneCustomPolicy', ((1, 'dwZone'),(1, 'guidKey'),(1, 'ppPolicy'),(1, 'pcbPolicy'),(1, 'urlZoneReg'),)))
    IInternetZoneManager.SetZoneCustomPolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Guid),POINTER(Byte),UInt32,win32more.System.Com.Urlmon.URLZONEREG, use_last_error=False)(6, 'SetZoneCustomPolicy', ((1, 'dwZone'),(1, 'guidKey'),(1, 'pPolicy'),(1, 'cbPolicy'),(1, 'urlZoneReg'),)))
    IInternetZoneManager.GetZoneActionPolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(Byte),UInt32,win32more.System.Com.Urlmon.URLZONEREG, use_last_error=False)(7, 'GetZoneActionPolicy', ((1, 'dwZone'),(1, 'dwAction'),(1, 'pPolicy'),(1, 'cbPolicy'),(1, 'urlZoneReg'),)))
    IInternetZoneManager.SetZoneActionPolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(Byte),UInt32,win32more.System.Com.Urlmon.URLZONEREG, use_last_error=False)(8, 'SetZoneActionPolicy', ((1, 'dwZone'),(1, 'dwAction'),(1, 'pPolicy'),(1, 'cbPolicy'),(1, 'urlZoneReg'),)))
    IInternetZoneManager.PromptAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.HWND,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(9, 'PromptAction', ((1, 'dwAction'),(1, 'hwndParent'),(1, 'pwszUrl'),(1, 'pwszText'),(1, 'dwPromptFlags'),)))
    IInternetZoneManager.LogAction = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(10, 'LogAction', ((1, 'dwAction'),(1, 'pwszUrl'),(1, 'pwszText'),(1, 'dwLogFlags'),)))
    IInternetZoneManager.CreateZoneEnumerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32),UInt32, use_last_error=False)(11, 'CreateZoneEnumerator', ((1, 'pdwEnum'),(1, 'pdwCount'),(1, 'dwFlags'),)))
    IInternetZoneManager.GetZoneAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(UInt32), use_last_error=False)(12, 'GetZoneAt', ((1, 'dwEnum'),(1, 'dwIndex'),(1, 'pdwZone'),)))
    IInternetZoneManager.DestroyZoneEnumerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(13, 'DestroyZoneEnumerator', ((1, 'dwEnum'),)))
    IInternetZoneManager.CopyTemplatePoliciesToZone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,UInt32, use_last_error=False)(14, 'CopyTemplatePoliciesToZone', ((1, 'dwTemplate'),(1, 'dwZone'),(1, 'dwReserved'),)))
    return IInternetZoneManager
def _define_IInternetZoneManagerEx_head():
    class IInternetZoneManagerEx(win32more.System.Com.Urlmon.IInternetZoneManager_head):
        Guid = Guid('a4c23339-8e06-431e-9bf4-7e711c085648')
    return IInternetZoneManagerEx
def _define_IInternetZoneManagerEx():
    IInternetZoneManagerEx = win32more.System.Com.Urlmon.IInternetZoneManagerEx_head
    IInternetZoneManagerEx.GetZoneActionPolicyEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(Byte),UInt32,win32more.System.Com.Urlmon.URLZONEREG,UInt32, use_last_error=False)(15, 'GetZoneActionPolicyEx', ((1, 'dwZone'),(1, 'dwAction'),(1, 'pPolicy'),(1, 'cbPolicy'),(1, 'urlZoneReg'),(1, 'dwFlags'),)))
    IInternetZoneManagerEx.SetZoneActionPolicyEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(Byte),UInt32,win32more.System.Com.Urlmon.URLZONEREG,UInt32, use_last_error=False)(16, 'SetZoneActionPolicyEx', ((1, 'dwZone'),(1, 'dwAction'),(1, 'pPolicy'),(1, 'cbPolicy'),(1, 'urlZoneReg'),(1, 'dwFlags'),)))
    return IInternetZoneManagerEx
def _define_IInternetZoneManagerEx2_head():
    class IInternetZoneManagerEx2(win32more.System.Com.Urlmon.IInternetZoneManagerEx_head):
        Guid = Guid('edc17559-dd5d-4846-8eef-8becba5a4abf')
    return IInternetZoneManagerEx2
def _define_IInternetZoneManagerEx2():
    IInternetZoneManagerEx2 = win32more.System.Com.Urlmon.IInternetZoneManagerEx2_head
    IInternetZoneManagerEx2.GetZoneAttributesEx = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.Urlmon.ZONEATTRIBUTES_head),UInt32, use_last_error=False)(17, 'GetZoneAttributesEx', ((1, 'dwZone'),(1, 'pZoneAttributes'),(1, 'dwFlags'),)))
    IInternetZoneManagerEx2.GetZoneSecurityState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.BOOL,POINTER(UInt32),POINTER(win32more.Foundation.BOOL), use_last_error=False)(18, 'GetZoneSecurityState', ((1, 'dwZoneIndex'),(1, 'fRespectPolicy'),(1, 'pdwState'),(1, 'pfPolicyEncountered'),)))
    IInternetZoneManagerEx2.GetIESecurityState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL,POINTER(UInt32),POINTER(win32more.Foundation.BOOL),win32more.Foundation.BOOL, use_last_error=False)(19, 'GetIESecurityState', ((1, 'fRespectPolicy'),(1, 'pdwState'),(1, 'pfPolicyEncountered'),(1, 'fNoCache'),)))
    IInternetZoneManagerEx2.FixUnsecureSettings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT, use_last_error=False)(20, 'FixUnsecureSettings', ()))
    return IInternetZoneManagerEx2
def _define_CODEBASEHOLD_head():
    class CODEBASEHOLD(Structure):
        pass
    return CODEBASEHOLD
def _define_CODEBASEHOLD():
    CODEBASEHOLD = win32more.System.Com.Urlmon.CODEBASEHOLD_head
    CODEBASEHOLD._fields_ = [
        ("cbSize", UInt32),
        ("szDistUnit", win32more.Foundation.PWSTR),
        ("szCodeBase", win32more.Foundation.PWSTR),
        ("dwVersionMS", UInt32),
        ("dwVersionLS", UInt32),
        ("dwStyle", UInt32),
    ]
    return CODEBASEHOLD
def _define_SOFTDISTINFO_head():
    class SOFTDISTINFO(Structure):
        pass
    return SOFTDISTINFO
def _define_SOFTDISTINFO():
    SOFTDISTINFO = win32more.System.Com.Urlmon.SOFTDISTINFO_head
    SOFTDISTINFO._fields_ = [
        ("cbSize", UInt32),
        ("dwFlags", UInt32),
        ("dwAdState", UInt32),
        ("szTitle", win32more.Foundation.PWSTR),
        ("szAbstract", win32more.Foundation.PWSTR),
        ("szHREF", win32more.Foundation.PWSTR),
        ("dwInstalledVersionMS", UInt32),
        ("dwInstalledVersionLS", UInt32),
        ("dwUpdateVersionMS", UInt32),
        ("dwUpdateVersionLS", UInt32),
        ("dwAdvertisedVersionMS", UInt32),
        ("dwAdvertisedVersionLS", UInt32),
        ("dwReserved", UInt32),
    ]
    return SOFTDISTINFO
def _define_ISoftDistExt_head():
    class ISoftDistExt(win32more.System.Com.IUnknown_head):
        Guid = Guid('b15b8dc1-c7e1-11d0-8680-00aa00bdcb71')
    return ISoftDistExt
def _define_ISoftDistExt():
    ISoftDistExt = win32more.System.Com.Urlmon.ISoftDistExt_head
    ISoftDistExt.ProcessSoftDist = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Data.Xml.MsXml.IXMLElement_head,POINTER(win32more.System.Com.Urlmon.SOFTDISTINFO_head), use_last_error=False)(3, 'ProcessSoftDist', ((1, 'szCDFURL'),(1, 'pSoftDistElement'),(1, 'lpsdi'),)))
    ISoftDistExt.GetFirstCodeBase = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32), use_last_error=False)(4, 'GetFirstCodeBase', ((1, 'szCodeBase'),(1, 'dwMaxSize'),)))
    ISoftDistExt.GetNextCodeBase = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR),POINTER(UInt32), use_last_error=False)(5, 'GetNextCodeBase', ((1, 'szCodeBase'),(1, 'dwMaxSize'),)))
    ISoftDistExt.AsyncInstallDistributionUnit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IBindCtx_head,c_void_p,UInt32,POINTER(win32more.System.Com.Urlmon.CODEBASEHOLD_head), use_last_error=False)(6, 'AsyncInstallDistributionUnit', ((1, 'pbc'),(1, 'pvReserved'),(1, 'flags'),(1, 'lpcbh'),)))
    return ISoftDistExt
def _define_ICatalogFileInfo_head():
    class ICatalogFileInfo(win32more.System.Com.IUnknown_head):
        Guid = Guid('711c7600-6b48-11d1-b403-00aa00b92af1')
    return ICatalogFileInfo
def _define_ICatalogFileInfo():
    ICatalogFileInfo = win32more.System.Com.Urlmon.ICatalogFileInfo_head
    ICatalogFileInfo.GetCatalogFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PSTR), use_last_error=False)(3, 'GetCatalogFile', ((1, 'ppszCatalogFile'),)))
    ICatalogFileInfo.GetJavaTrust = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_void_p), use_last_error=False)(4, 'GetJavaTrust', ((1, 'ppJavaTrust'),)))
    return ICatalogFileInfo
def _define_IDataFilter_head():
    class IDataFilter(win32more.System.Com.IUnknown_head):
        Guid = Guid('69d14c80-c18e-11d0-a9ce-006097942311')
    return IDataFilter
def _define_IDataFilter():
    IDataFilter = win32more.System.Com.Urlmon.IDataFilter_head
    IDataFilter.DoEncode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Int32,POINTER(Byte),Int32,POINTER(Byte),Int32,POINTER(Int32),POINTER(Int32),UInt32, use_last_error=False)(3, 'DoEncode', ((1, 'dwFlags'),(1, 'lInBufferSize'),(1, 'pbInBuffer'),(1, 'lOutBufferSize'),(1, 'pbOutBuffer'),(1, 'lInBytesAvailable'),(1, 'plInBytesRead'),(1, 'plOutBytesWritten'),(1, 'dwReserved'),)))
    IDataFilter.DoDecode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,Int32,POINTER(Byte),Int32,POINTER(Byte),Int32,POINTER(Int32),POINTER(Int32),UInt32, use_last_error=False)(4, 'DoDecode', ((1, 'dwFlags'),(1, 'lInBufferSize'),(1, 'pbInBuffer'),(1, 'lOutBufferSize'),(1, 'pbOutBuffer'),(1, 'lInBytesAvailable'),(1, 'plInBytesRead'),(1, 'plOutBytesWritten'),(1, 'dwReserved'),)))
    IDataFilter.SetEncodingLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32, use_last_error=False)(5, 'SetEncodingLevel', ((1, 'dwEncLevel'),)))
    return IDataFilter
def _define_PROTOCOLFILTERDATA_head():
    class PROTOCOLFILTERDATA(Structure):
        pass
    return PROTOCOLFILTERDATA
def _define_PROTOCOLFILTERDATA():
    PROTOCOLFILTERDATA = win32more.System.Com.Urlmon.PROTOCOLFILTERDATA_head
    PROTOCOLFILTERDATA._fields_ = [
        ("cbSize", UInt32),
        ("pProtocolSink", win32more.System.Com.Urlmon.IInternetProtocolSink_head),
        ("pProtocol", win32more.System.Com.Urlmon.IInternetProtocol_head),
        ("pUnk", win32more.System.Com.IUnknown_head),
        ("dwFilterFlags", UInt32),
    ]
    return PROTOCOLFILTERDATA
def _define_DATAINFO_head():
    class DATAINFO(Structure):
        pass
    return DATAINFO
def _define_DATAINFO():
    DATAINFO = win32more.System.Com.Urlmon.DATAINFO_head
    DATAINFO._fields_ = [
        ("ulTotalSize", UInt32),
        ("ulavrPacketSize", UInt32),
        ("ulConnectSpeed", UInt32),
        ("ulProcessorSpeed", UInt32),
    ]
    return DATAINFO
def _define_IEncodingFilterFactory_head():
    class IEncodingFilterFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('70bdde00-c18e-11d0-a9ce-006097942311')
    return IEncodingFilterFactory
def _define_IEncodingFilterFactory():
    IEncodingFilterFactory = win32more.System.Com.Urlmon.IEncodingFilterFactory_head
    IEncodingFilterFactory.FindBestFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.System.Com.Urlmon.DATAINFO,POINTER(win32more.System.Com.Urlmon.IDataFilter_head), use_last_error=False)(3, 'FindBestFilter', ((1, 'pwzCodeIn'),(1, 'pwzCodeOut'),(1, 'info'),(1, 'ppDF'),)))
    IEncodingFilterFactory.GetDefaultFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.Urlmon.IDataFilter_head), use_last_error=False)(4, 'GetDefaultFilter', ((1, 'pwzCodeIn'),(1, 'pwzCodeOut'),(1, 'ppDF'),)))
    return IEncodingFilterFactory
def _define_HIT_LOGGING_INFO_head():
    class HIT_LOGGING_INFO(Structure):
        pass
    return HIT_LOGGING_INFO
def _define_HIT_LOGGING_INFO():
    HIT_LOGGING_INFO = win32more.System.Com.Urlmon.HIT_LOGGING_INFO_head
    HIT_LOGGING_INFO._fields_ = [
        ("dwStructSize", UInt32),
        ("lpszLoggedUrlName", win32more.Foundation.PSTR),
        ("StartTime", win32more.Foundation.SYSTEMTIME),
        ("EndTime", win32more.Foundation.SYSTEMTIME),
        ("lpszExtendedInfo", win32more.Foundation.PSTR),
    ]
    return HIT_LOGGING_INFO
def _define_CONFIRMSAFETY_head():
    class CONFIRMSAFETY(Structure):
        pass
    return CONFIRMSAFETY
def _define_CONFIRMSAFETY():
    CONFIRMSAFETY = win32more.System.Com.Urlmon.CONFIRMSAFETY_head
    CONFIRMSAFETY._fields_ = [
        ("clsid", Guid),
        ("pUnk", win32more.System.Com.IUnknown_head),
        ("dwFlags", UInt32),
    ]
    return CONFIRMSAFETY
def _define_IWrappedProtocol_head():
    class IWrappedProtocol(win32more.System.Com.IUnknown_head):
        Guid = Guid('53c84785-8425-4dc5-971b-e58d9c19f9b6')
    return IWrappedProtocol
def _define_IWrappedProtocol():
    IWrappedProtocol = win32more.System.Com.Urlmon.IWrappedProtocol_head
    IWrappedProtocol.GetWrapperCode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),UIntPtr, use_last_error=False)(3, 'GetWrapperCode', ((1, 'pnCode'),(1, 'dwReserved'),)))
    return IWrappedProtocol
BINDHANDLETYPES = Int32
BINDHANDLETYPES_APPCACHE = 0
BINDHANDLETYPES_DEPENDENCY = 1
BINDHANDLETYPES_COUNT = 2
def _define_IGetBindHandle_head():
    class IGetBindHandle(win32more.System.Com.IUnknown_head):
        Guid = Guid('af0ff408-129d-4b20-91f0-02bd23d88352')
    return IGetBindHandle
def _define_IGetBindHandle():
    IGetBindHandle = win32more.System.Com.Urlmon.IGetBindHandle_head
    IGetBindHandle.GetBindHandle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.Urlmon.BINDHANDLETYPES,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(3, 'GetBindHandle', ((1, 'enumRequestedHandle'),(1, 'pRetHandle'),)))
    return IGetBindHandle
def _define_PROTOCOL_ARGUMENT_head():
    class PROTOCOL_ARGUMENT(Structure):
        pass
    return PROTOCOL_ARGUMENT
def _define_PROTOCOL_ARGUMENT():
    PROTOCOL_ARGUMENT = win32more.System.Com.Urlmon.PROTOCOL_ARGUMENT_head
    PROTOCOL_ARGUMENT._fields_ = [
        ("szMethod", win32more.Foundation.PWSTR),
        ("szTargetUrl", win32more.Foundation.PWSTR),
    ]
    return PROTOCOL_ARGUMENT
def _define_IBindCallbackRedirect_head():
    class IBindCallbackRedirect(win32more.System.Com.IUnknown_head):
        Guid = Guid('11c81bc2-121e-4ed5-b9c4-b430bd54f2c0')
    return IBindCallbackRedirect
def _define_IBindCallbackRedirect():
    IBindCallbackRedirect = win32more.System.Com.Urlmon.IBindCallbackRedirect_head
    IBindCallbackRedirect.Redirect = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Int16), use_last_error=False)(3, 'Redirect', ((1, 'lpcUrl'),(1, 'vbCancel'),)))
    return IBindCallbackRedirect
def _define_IBindHttpSecurity_head():
    class IBindHttpSecurity(win32more.System.Com.IUnknown_head):
        Guid = Guid('a9eda967-f50e-4a33-b358-206f6ef3086d')
    return IBindHttpSecurity
def _define_IBindHttpSecurity():
    IBindHttpSecurity = win32more.System.Com.Urlmon.IBindHttpSecurity_head
    IBindHttpSecurity.GetIgnoreCertMask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(3, 'GetIgnoreCertMask', ((1, 'pdwIgnoreCertMask'),)))
    return IBindHttpSecurity
def _define_CreateURLMoniker():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IMoniker_head,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.IMoniker_head), use_last_error=False)(("CreateURLMoniker", windll["urlmon"]), ((1, 'pMkCtx'),(1, 'szURL'),(1, 'ppmk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateURLMonikerEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IMoniker_head,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.IMoniker_head),UInt32, use_last_error=False)(("CreateURLMonikerEx", windll["urlmon"]), ((1, 'pMkCtx'),(1, 'szURL'),(1, 'ppmk'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetClassURL():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(Guid), use_last_error=False)(("GetClassURL", windll["urlmon"]), ((1, 'szURL'),(1, 'pClsID'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateAsyncBindCtx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.System.Com.IBindStatusCallback_head,win32more.System.Com.IEnumFORMATETC_head,POINTER(win32more.System.Com.IBindCtx_head), use_last_error=False)(("CreateAsyncBindCtx", windll["urlmon"]), ((1, 'reserved'),(1, 'pBSCb'),(1, 'pEFetc'),(1, 'ppBC'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateURLMonikerEx2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IMoniker_head,win32more.System.Com.IUri_head,POINTER(win32more.System.Com.IMoniker_head),UInt32, use_last_error=False)(("CreateURLMonikerEx2", windll["urlmon"]), ((1, 'pMkCtx'),(1, 'pUri'),(1, 'ppmk'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateAsyncBindCtxEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IBindCtx_head,UInt32,win32more.System.Com.IBindStatusCallback_head,win32more.System.Com.IEnumFORMATETC_head,POINTER(win32more.System.Com.IBindCtx_head),UInt32, use_last_error=False)(("CreateAsyncBindCtxEx", windll["urlmon"]), ((1, 'pbc'),(1, 'dwOptions'),(1, 'pBSCb'),(1, 'pEnum'),(1, 'ppBC'),(1, 'reserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MkParseDisplayNameEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IBindCtx_head,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(win32more.System.Com.IMoniker_head), use_last_error=False)(("MkParseDisplayNameEx", windll["urlmon"]), ((1, 'pbc'),(1, 'szDisplayName'),(1, 'pchEaten'),(1, 'ppmk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterBindStatusCallback():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IBindCtx_head,win32more.System.Com.IBindStatusCallback_head,POINTER(win32more.System.Com.IBindStatusCallback_head),UInt32, use_last_error=False)(("RegisterBindStatusCallback", windll["urlmon"]), ((1, 'pBC'),(1, 'pBSCb'),(1, 'ppBSCBPrev'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RevokeBindStatusCallback():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IBindCtx_head,win32more.System.Com.IBindStatusCallback_head, use_last_error=False)(("RevokeBindStatusCallback", windll["urlmon"]), ((1, 'pBC'),(1, 'pBSCb'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetClassFileOrMime():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IBindCtx_head,win32more.Foundation.PWSTR,c_void_p,UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(Guid), use_last_error=False)(("GetClassFileOrMime", windll["urlmon"]), ((1, 'pBC'),(1, 'szFilename'),(1, 'pBuffer'),(1, 'cbSize'),(1, 'szMime'),(1, 'dwReserved'),(1, 'pclsid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsValidURL():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IBindCtx_head,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("IsValidURL", windll["urlmon"]), ((1, 'pBC'),(1, 'szURL'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoGetClassObjectFromURL():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.Foundation.PWSTR,UInt32,UInt32,win32more.Foundation.PWSTR,win32more.System.Com.IBindCtx_head,win32more.System.Com.CLSCTX,c_void_p,POINTER(Guid),POINTER(c_void_p), use_last_error=False)(("CoGetClassObjectFromURL", windll["urlmon"]), ((1, 'rCLASSID'),(1, 'szCODE'),(1, 'dwFileVersionMS'),(1, 'dwFileVersionLS'),(1, 'szTYPE'),(1, 'pBindCtx'),(1, 'dwClsContext'),(1, 'pvReserved'),(1, 'riid'),(1, 'ppv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IEInstallScope():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32), use_last_error=False)(("IEInstallScope", windll["urlmon"]), ((1, 'pdwScope'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FaultInIEFeature():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.System.Com.uCLSSPEC_head),POINTER(win32more.System.Com.QUERYCONTEXT_head),UInt32, use_last_error=False)(("FaultInIEFeature", windll["urlmon"]), ((1, 'hWnd'),(1, 'pClassSpec'),(1, 'pQuery'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetComponentIDFromCLSSPEC():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.uCLSSPEC_head),POINTER(win32more.Foundation.PSTR), use_last_error=False)(("GetComponentIDFromCLSSPEC", windll["urlmon"]), ((1, 'pClassspec'),(1, 'ppszComponentID'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsAsyncMoniker():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IMoniker_head, use_last_error=False)(("IsAsyncMoniker", windll["urlmon"]), ((1, 'pmk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterMediaTypes():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.PSTR),POINTER(UInt16), use_last_error=False)(("RegisterMediaTypes", windll["urlmon"]), ((1, 'ctypes'),(1, 'rgszTypes'),(1, 'rgcfTypes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindMediaType():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,POINTER(UInt16), use_last_error=False)(("FindMediaType", windll["urlmon"]), ((1, 'rgszTypes'),(1, 'rgcfTypes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateFormatEnumerator():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.FORMATETC),POINTER(win32more.System.Com.IEnumFORMATETC_head), use_last_error=False)(("CreateFormatEnumerator", windll["urlmon"]), ((1, 'cfmtetc'),(1, 'rgfmtetc'),(1, 'ppenumfmtetc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterFormatEnumerator():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IBindCtx_head,win32more.System.Com.IEnumFORMATETC_head,UInt32, use_last_error=False)(("RegisterFormatEnumerator", windll["urlmon"]), ((1, 'pBC'),(1, 'pEFetc'),(1, 'reserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RevokeFormatEnumerator():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IBindCtx_head,win32more.System.Com.IEnumFORMATETC_head, use_last_error=False)(("RevokeFormatEnumerator", windll["urlmon"]), ((1, 'pBC'),(1, 'pEFetc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterMediaTypeClass():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IBindCtx_head,UInt32,POINTER(win32more.Foundation.PSTR),POINTER(Guid),UInt32, use_last_error=False)(("RegisterMediaTypeClass", windll["urlmon"]), ((1, 'pBC'),(1, 'ctypes'),(1, 'rgszTypes'),(1, 'rgclsID'),(1, 'reserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindMediaTypeClass():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IBindCtx_head,win32more.Foundation.PSTR,POINTER(Guid),UInt32, use_last_error=False)(("FindMediaTypeClass", windll["urlmon"]), ((1, 'pBC'),(1, 'szType'),(1, 'pclsID'),(1, 'reserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UrlMkSetSessionOption():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p,UInt32,UInt32, use_last_error=False)(("UrlMkSetSessionOption", windll["urlmon"]), ((1, 'dwOption'),(1, 'pBuffer'),(1, 'dwBufferLength'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UrlMkGetSessionOption():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,c_void_p,UInt32,POINTER(UInt32),UInt32, use_last_error=False)(("UrlMkGetSessionOption", windll["urlmon"]), ((1, 'dwOption'),(1, 'pBuffer'),(1, 'dwBufferLength'),(1, 'pdwBufferLengthOut'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindMimeFromData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IBindCtx_head,win32more.Foundation.PWSTR,c_void_p,UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Foundation.PWSTR),UInt32, use_last_error=False)(("FindMimeFromData", windll["urlmon"]), ((1, 'pBC'),(1, 'pwzUrl'),(1, 'pBuffer'),(1, 'cbSize'),(1, 'pwzMimeProposed'),(1, 'dwMimeFlags'),(1, 'ppwzMimeOut'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ObtainUserAgentString():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(Byte),POINTER(UInt32), use_last_error=False)(("ObtainUserAgentString", windll["urlmon"]), ((1, 'dwOption'),(1, 'pszUAOut'),(1, 'cbSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CompareSecurityIds():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Byte),UInt32,POINTER(Byte),UInt32,UInt32, use_last_error=False)(("CompareSecurityIds", windll["urlmon"]), ((1, 'pbSecurityId1'),(1, 'dwLen1'),(1, 'pbSecurityId2'),(1, 'dwLen2'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CompatFlagsFromClsid():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(UInt32),POINTER(UInt32), use_last_error=False)(("CompatFlagsFromClsid", windll["urlmon"]), ((1, 'pclsid'),(1, 'pdwCompatFlags'),(1, 'pdwMiscStatusFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetAccessForIEAppContainer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,win32more.System.Com.Urlmon.IEObjectType,UInt32, use_last_error=False)(("SetAccessForIEAppContainer", windll["urlmon"]), ((1, 'hObject'),(1, 'ieObjectType'),(1, 'dwAccessMask'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HlinkSimpleNavigateToString():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.System.Com.IUnknown_head,win32more.System.Com.IBindCtx_head,win32more.System.Com.IBindStatusCallback_head,UInt32,UInt32, use_last_error=False)(("HlinkSimpleNavigateToString", windll["urlmon"]), ((1, 'szTarget'),(1, 'szLocation'),(1, 'szTargetFrameName'),(1, 'pUnk'),(1, 'pbc'),(1, 'param5'),(1, 'grfHLNF'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HlinkSimpleNavigateToMoniker():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IMoniker_head,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.System.Com.IUnknown_head,win32more.System.Com.IBindCtx_head,win32more.System.Com.IBindStatusCallback_head,UInt32,UInt32, use_last_error=False)(("HlinkSimpleNavigateToMoniker", windll["urlmon"]), ((1, 'pmkTarget'),(1, 'szLocation'),(1, 'szTargetFrameName'),(1, 'pUnk'),(1, 'pbc'),(1, 'param5'),(1, 'grfHLNF'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_URLOpenStreamA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Foundation.PSTR,UInt32,win32more.System.Com.IBindStatusCallback_head, use_last_error=False)(("URLOpenStreamA", windll["urlmon"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_URLOpenStreamW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Foundation.PWSTR,UInt32,win32more.System.Com.IBindStatusCallback_head, use_last_error=False)(("URLOpenStreamW", windll["urlmon"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_URLOpenStream():
    return win32more.System.Com.Urlmon.URLOpenStreamW
def _define_URLOpenPullStreamA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Foundation.PSTR,UInt32,win32more.System.Com.IBindStatusCallback_head, use_last_error=False)(("URLOpenPullStreamA", windll["urlmon"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_URLOpenPullStreamW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Foundation.PWSTR,UInt32,win32more.System.Com.IBindStatusCallback_head, use_last_error=False)(("URLOpenPullStreamW", windll["urlmon"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_URLOpenPullStream():
    return win32more.System.Com.Urlmon.URLOpenPullStreamW
def _define_URLDownloadToFileA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,win32more.System.Com.IBindStatusCallback_head, use_last_error=False)(("URLDownloadToFileA", windll["urlmon"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),(1, 'param4'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_URLDownloadToFileW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,win32more.System.Com.IBindStatusCallback_head, use_last_error=False)(("URLDownloadToFileW", windll["urlmon"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),(1, 'param4'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_URLDownloadToFile():
    return win32more.System.Com.Urlmon.URLDownloadToFileW
def _define_URLDownloadToCacheFileA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Foundation.PSTR,POINTER(Byte),UInt32,UInt32,win32more.System.Com.IBindStatusCallback_head, use_last_error=False)(("URLDownloadToCacheFileA", windll["urlmon"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'cchFileName'),(1, 'param4'),(1, 'param5'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_URLDownloadToCacheFileW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Foundation.PWSTR,POINTER(Char),UInt32,UInt32,win32more.System.Com.IBindStatusCallback_head, use_last_error=False)(("URLDownloadToCacheFileW", windll["urlmon"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'cchFileName'),(1, 'param4'),(1, 'param5'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_URLDownloadToCacheFile():
    return win32more.System.Com.Urlmon.URLDownloadToCacheFileW
def _define_URLOpenBlockingStreamA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Foundation.PSTR,POINTER(win32more.System.Com.IStream_head),UInt32,win32more.System.Com.IBindStatusCallback_head, use_last_error=False)(("URLOpenBlockingStreamA", windll["urlmon"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),(1, 'param4'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_URLOpenBlockingStreamW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.IStream_head),UInt32,win32more.System.Com.IBindStatusCallback_head, use_last_error=False)(("URLOpenBlockingStreamW", windll["urlmon"]), ((1, 'param0'),(1, 'param1'),(1, 'param2'),(1, 'param3'),(1, 'param4'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_URLOpenBlockingStream():
    return win32more.System.Com.Urlmon.URLOpenBlockingStreamW
def _define_HlinkGoBack():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(("HlinkGoBack", windll["urlmon"]), ((1, 'pUnk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HlinkGoForward():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head, use_last_error=False)(("HlinkGoForward", windll["urlmon"]), ((1, 'pUnk'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HlinkNavigateString():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.Foundation.PWSTR, use_last_error=False)(("HlinkNavigateString", windll["urlmon"]), ((1, 'pUnk'),(1, 'szTarget'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HlinkNavigateMoniker():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUnknown_head,win32more.System.Com.IMoniker_head, use_last_error=False)(("HlinkNavigateMoniker", windll["urlmon"]), ((1, 'pUnk'),(1, 'pmkTarget'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoInternetParseUrl():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.Urlmon.PARSEACTION,UInt32,POINTER(Char),UInt32,POINTER(UInt32),UInt32, use_last_error=False)(("CoInternetParseUrl", windll["urlmon"]), ((1, 'pwzUrl'),(1, 'ParseAction'),(1, 'dwFlags'),(1, 'pszResult'),(1, 'cchResult'),(1, 'pcchResult'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoInternetParseIUri():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUri_head,win32more.System.Com.Urlmon.PARSEACTION,UInt32,POINTER(Char),UInt32,POINTER(UInt32),UIntPtr, use_last_error=False)(("CoInternetParseIUri", windll["urlmon"]), ((1, 'pIUri'),(1, 'ParseAction'),(1, 'dwFlags'),(1, 'pwzResult'),(1, 'cchResult'),(1, 'pcchResult'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoInternetCombineUrl():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(Char),UInt32,POINTER(UInt32),UInt32, use_last_error=False)(("CoInternetCombineUrl", windll["urlmon"]), ((1, 'pwzBaseUrl'),(1, 'pwzRelativeUrl'),(1, 'dwCombineFlags'),(1, 'pszResult'),(1, 'cchResult'),(1, 'pcchResult'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoInternetCombineUrlEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUri_head,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.System.Com.IUri_head),UIntPtr, use_last_error=False)(("CoInternetCombineUrlEx", windll["urlmon"]), ((1, 'pBaseUri'),(1, 'pwzRelativeUrl'),(1, 'dwCombineFlags'),(1, 'ppCombinedUri'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoInternetCombineIUri():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUri_head,win32more.System.Com.IUri_head,UInt32,POINTER(win32more.System.Com.IUri_head),UIntPtr, use_last_error=False)(("CoInternetCombineIUri", windll["urlmon"]), ((1, 'pBaseUri'),(1, 'pRelativeUri'),(1, 'dwCombineFlags'),(1, 'ppCombinedUri'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoInternetCompareUrl():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("CoInternetCompareUrl", windll["urlmon"]), ((1, 'pwzUrl1'),(1, 'pwzUrl2'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoInternetGetProtocolFlags():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32),UInt32, use_last_error=False)(("CoInternetGetProtocolFlags", windll["urlmon"]), ((1, 'pwzUrl'),(1, 'pdwFlags'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoInternetQueryInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.Urlmon.QUERYOPTION,UInt32,c_void_p,UInt32,POINTER(UInt32),UInt32, use_last_error=False)(("CoInternetQueryInfo", windll["urlmon"]), ((1, 'pwzUrl'),(1, 'QueryOptions'),(1, 'dwQueryFlags'),(1, 'pvBuffer'),(1, 'cbBuffer'),(1, 'pcbBuffer'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoInternetGetSession():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.Urlmon.IInternetSession_head),UInt32, use_last_error=False)(("CoInternetGetSession", windll["urlmon"]), ((1, 'dwSessionMode'),(1, 'ppIInternetSession'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoInternetGetSecurityUrl():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),win32more.System.Com.Urlmon.PSUACTION,UInt32, use_last_error=False)(("CoInternetGetSecurityUrl", windll["urlmon"]), ((1, 'pwszUrl'),(1, 'ppwszSecUrl'),(1, 'psuAction'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoInternetGetSecurityUrlEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUri_head,POINTER(win32more.System.Com.IUri_head),win32more.System.Com.Urlmon.PSUACTION,UIntPtr, use_last_error=False)(("CoInternetGetSecurityUrlEx", windll["urlmon"]), ((1, 'pUri'),(1, 'ppSecUri'),(1, 'psuAction'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoInternetSetFeatureEnabled():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.Urlmon.INTERNETFEATURELIST,UInt32,win32more.Foundation.BOOL, use_last_error=False)(("CoInternetSetFeatureEnabled", windll["urlmon"]), ((1, 'FeatureEntry'),(1, 'dwFlags'),(1, 'fEnable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoInternetIsFeatureEnabled():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.Urlmon.INTERNETFEATURELIST,UInt32, use_last_error=False)(("CoInternetIsFeatureEnabled", windll["urlmon"]), ((1, 'FeatureEntry'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoInternetIsFeatureEnabledForUrl():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.Urlmon.INTERNETFEATURELIST,UInt32,win32more.Foundation.PWSTR,win32more.System.Com.Urlmon.IInternetSecurityManager_head, use_last_error=False)(("CoInternetIsFeatureEnabledForUrl", windll["urlmon"]), ((1, 'FeatureEntry'),(1, 'dwFlags'),(1, 'szURL'),(1, 'pSecMgr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoInternetIsFeatureEnabledForIUri():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.Urlmon.INTERNETFEATURELIST,UInt32,win32more.System.Com.IUri_head,win32more.System.Com.Urlmon.IInternetSecurityManagerEx2_head, use_last_error=False)(("CoInternetIsFeatureEnabledForIUri", windll["urlmon"]), ((1, 'FeatureEntry'),(1, 'dwFlags'),(1, 'pIUri'),(1, 'pSecMgr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoInternetIsFeatureZoneElevationEnabled():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.System.Com.Urlmon.IInternetSecurityManager_head,UInt32, use_last_error=False)(("CoInternetIsFeatureZoneElevationEnabled", windll["urlmon"]), ((1, 'szFromURL'),(1, 'szToURL'),(1, 'pSecMgr'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CopyStgMedium():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.STGMEDIUM_head),POINTER(win32more.System.Com.STGMEDIUM_head), use_last_error=False)(("CopyStgMedium", windll["urlmon"]), ((1, 'pcstgmedSrc'),(1, 'pstgmedDest'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CopyBindInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.BINDINFO_head),POINTER(win32more.System.Com.BINDINFO_head), use_last_error=False)(("CopyBindInfo", windll["urlmon"]), ((1, 'pcbiSrc'),(1, 'pbiDest'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReleaseBindInfo():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.System.Com.BINDINFO_head), use_last_error=False)(("ReleaseBindInfo", windll["urlmon"]), ((1, 'pbindinfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IEGetUserPrivateNamespaceName():
    try:
        return WINFUNCTYPE(win32more.Foundation.PWSTR, use_last_error=False)(("IEGetUserPrivateNamespaceName", windll["urlmon"]), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoInternetCreateSecurityManager():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IServiceProvider_head,POINTER(win32more.System.Com.Urlmon.IInternetSecurityManager_head),UInt32, use_last_error=False)(("CoInternetCreateSecurityManager", windll["urlmon"]), ((1, 'pSP'),(1, 'ppSM'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CoInternetCreateZoneManager():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IServiceProvider_head,POINTER(win32more.System.Com.Urlmon.IInternetZoneManager_head),UInt32, use_last_error=False)(("CoInternetCreateZoneManager", windll["urlmon"]), ((1, 'pSP'),(1, 'ppZM'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetSoftwareUpdateInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.Urlmon.SOFTDISTINFO_head), use_last_error=False)(("GetSoftwareUpdateInfo", windll["urlmon"]), ((1, 'szDistUnit'),(1, 'psdi'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetSoftwareUpdateAdvertisementState():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,UInt32, use_last_error=False)(("SetSoftwareUpdateAdvertisementState", windll["urlmon"]), ((1, 'szDistUnit'),(1, 'dwAdState'),(1, 'dwAdvertisedVersionMS'),(1, 'dwAdvertisedVersionLS'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsLoggingEnabledA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR, use_last_error=False)(("IsLoggingEnabledA", windll["urlmon"]), ((1, 'pszUrl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsLoggingEnabledW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR, use_last_error=False)(("IsLoggingEnabledW", windll["urlmon"]), ((1, 'pwszUrl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsLoggingEnabled():
    return win32more.System.Com.Urlmon.IsLoggingEnabledW
def _define_WriteHitLogging():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.System.Com.Urlmon.HIT_LOGGING_INFO_head), use_last_error=False)(("WriteHitLogging", windll["urlmon"]), ((1, 'lpLogginginfo'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "MKSYS_URLMONIKER",
    "URL_MK_LEGACY",
    "URL_MK_UNIFORM",
    "URL_MK_NO_CANONICALIZE",
    "FIEF_FLAG_FORCE_JITUI",
    "FIEF_FLAG_PEEK",
    "FIEF_FLAG_SKIP_INSTALLED_VERSION_CHECK",
    "FIEF_FLAG_RESERVED_0",
    "FMFD_DEFAULT",
    "FMFD_URLASFILENAME",
    "FMFD_ENABLEMIMESNIFFING",
    "FMFD_IGNOREMIMETEXTPLAIN",
    "FMFD_SERVERMIME",
    "FMFD_RESPECTTEXTPLAIN",
    "FMFD_RETURNUPDATEDIMGMIMES",
    "FMFD_RESERVED_1",
    "FMFD_RESERVED_2",
    "UAS_EXACTLEGACY",
    "URLMON_OPTION_USERAGENT",
    "URLMON_OPTION_USERAGENT_REFRESH",
    "URLMON_OPTION_URL_ENCODING",
    "URLMON_OPTION_USE_BINDSTRINGCREDS",
    "URLMON_OPTION_USE_BROWSERAPPSDOCUMENTS",
    "CF_NULL",
    "MK_S_ASYNCHRONOUS",
    "S_ASYNCHRONOUS",
    "E_PENDING",
    "INET_E_INVALID_URL",
    "INET_E_NO_SESSION",
    "INET_E_CANNOT_CONNECT",
    "INET_E_RESOURCE_NOT_FOUND",
    "INET_E_OBJECT_NOT_FOUND",
    "INET_E_DATA_NOT_AVAILABLE",
    "INET_E_DOWNLOAD_FAILURE",
    "INET_E_AUTHENTICATION_REQUIRED",
    "INET_E_NO_VALID_MEDIA",
    "INET_E_CONNECTION_TIMEOUT",
    "INET_E_INVALID_REQUEST",
    "INET_E_UNKNOWN_PROTOCOL",
    "INET_E_SECURITY_PROBLEM",
    "INET_E_CANNOT_LOAD_DATA",
    "INET_E_CANNOT_INSTANTIATE_OBJECT",
    "INET_E_INVALID_CERTIFICATE",
    "INET_E_REDIRECT_FAILED",
    "INET_E_REDIRECT_TO_DIR",
    "INET_E_CANNOT_LOCK_REQUEST",
    "INET_E_USE_EXTEND_BINDING",
    "INET_E_TERMINATED_BIND",
    "INET_E_RESERVED_1",
    "INET_E_BLOCKED_REDIRECT_XSECURITYID",
    "INET_E_DOMINJECTIONVALIDATION",
    "INET_E_VTAB_SWITCH_FORCE_ENGINE",
    "INET_E_HSTS_CERTIFICATE_ERROR",
    "INET_E_RESERVED_2",
    "INET_E_RESERVED_3",
    "INET_E_RESERVED_4",
    "INET_E_RESERVED_5",
    "INET_E_ERROR_FIRST",
    "INET_E_CODE_DOWNLOAD_DECLINED",
    "INET_E_RESULT_DISPATCHED",
    "INET_E_CANNOT_REPLACE_SFP_FILE",
    "INET_E_CODE_INSTALL_SUPPRESSED",
    "INET_E_CODE_INSTALL_BLOCKED_BY_HASH_POLICY",
    "INET_E_DOWNLOAD_BLOCKED_BY_INPRIVATE",
    "INET_E_CODE_INSTALL_BLOCKED_IMMERSIVE",
    "INET_E_FORBIDFRAMING",
    "INET_E_CODE_INSTALL_BLOCKED_ARM",
    "INET_E_BLOCKED_PLUGGABLE_PROTOCOL",
    "INET_E_BLOCKED_ENHANCEDPROTECTEDMODE",
    "INET_E_CODE_INSTALL_BLOCKED_BITNESS",
    "INET_E_DOWNLOAD_BLOCKED_BY_CSP",
    "INET_E_ERROR_LAST",
    "Uri_DISPLAY_NO_FRAGMENT",
    "Uri_PUNYCODE_IDN_HOST",
    "Uri_DISPLAY_IDN_HOST",
    "Uri_DISPLAY_NO_PUNYCODE",
    "Uri_ENCODING_USER_INFO_AND_PATH_IS_PERCENT_ENCODED_UTF8",
    "Uri_ENCODING_USER_INFO_AND_PATH_IS_CP",
    "Uri_ENCODING_HOST_IS_IDN",
    "Uri_ENCODING_HOST_IS_PERCENT_ENCODED_UTF8",
    "Uri_ENCODING_HOST_IS_PERCENT_ENCODED_CP",
    "Uri_ENCODING_QUERY_AND_FRAGMENT_IS_PERCENT_ENCODED_UTF8",
    "Uri_ENCODING_QUERY_AND_FRAGMENT_IS_CP",
    "UriBuilder_USE_ORIGINAL_FLAGS",
    "WININETINFO_OPTION_LOCK_HANDLE",
    "URLOSTRM_USECACHEDCOPY_ONLY",
    "URLOSTRM_USECACHEDCOPY",
    "URLOSTRM_GETNEWESTVERSION",
    "SET_FEATURE_ON_THREAD",
    "SET_FEATURE_ON_PROCESS",
    "SET_FEATURE_IN_REGISTRY",
    "SET_FEATURE_ON_THREAD_LOCALMACHINE",
    "SET_FEATURE_ON_THREAD_INTRANET",
    "SET_FEATURE_ON_THREAD_TRUSTED",
    "SET_FEATURE_ON_THREAD_INTERNET",
    "SET_FEATURE_ON_THREAD_RESTRICTED",
    "GET_FEATURE_FROM_THREAD",
    "GET_FEATURE_FROM_PROCESS",
    "GET_FEATURE_FROM_REGISTRY",
    "GET_FEATURE_FROM_THREAD_LOCALMACHINE",
    "GET_FEATURE_FROM_THREAD_INTRANET",
    "GET_FEATURE_FROM_THREAD_TRUSTED",
    "GET_FEATURE_FROM_THREAD_INTERNET",
    "GET_FEATURE_FROM_THREAD_RESTRICTED",
    "INET_E_USE_DEFAULT_PROTOCOLHANDLER",
    "INET_E_USE_DEFAULT_SETTING",
    "INET_E_DEFAULT_ACTION",
    "INET_E_QUERYOPTION_UNKNOWN",
    "INET_E_REDIRECTING",
    "PROTOCOLFLAG_NO_PICS_CHECK",
    "MUTZ_NOSAVEDFILECHECK",
    "MUTZ_ISFILE",
    "MUTZ_ACCEPT_WILDCARD_SCHEME",
    "MUTZ_ENFORCERESTRICTED",
    "MUTZ_RESERVED",
    "MUTZ_REQUIRESAVEDFILECHECK",
    "MUTZ_DONT_UNESCAPE",
    "MUTZ_DONT_USE_CACHE",
    "MUTZ_FORCE_INTRANET_FLAGS",
    "MUTZ_IGNORE_ZONE_MAPPINGS",
    "MAX_SIZE_SECURITY_ID",
    "URLACTION_MIN",
    "URLACTION_DOWNLOAD_MIN",
    "URLACTION_DOWNLOAD_SIGNED_ACTIVEX",
    "URLACTION_DOWNLOAD_UNSIGNED_ACTIVEX",
    "URLACTION_DOWNLOAD_CURR_MAX",
    "URLACTION_DOWNLOAD_MAX",
    "URLACTION_ACTIVEX_MIN",
    "URLACTION_ACTIVEX_RUN",
    "URLPOLICY_ACTIVEX_CHECK_LIST",
    "URLACTION_ACTIVEX_OVERRIDE_OBJECT_SAFETY",
    "URLACTION_ACTIVEX_OVERRIDE_DATA_SAFETY",
    "URLACTION_ACTIVEX_OVERRIDE_SCRIPT_SAFETY",
    "URLACTION_SCRIPT_OVERRIDE_SAFETY",
    "URLACTION_ACTIVEX_CONFIRM_NOOBJECTSAFETY",
    "URLACTION_ACTIVEX_TREATASUNTRUSTED",
    "URLACTION_ACTIVEX_NO_WEBOC_SCRIPT",
    "URLACTION_ACTIVEX_OVERRIDE_REPURPOSEDETECTION",
    "URLACTION_ACTIVEX_OVERRIDE_OPTIN",
    "URLACTION_ACTIVEX_SCRIPTLET_RUN",
    "URLACTION_ACTIVEX_DYNSRC_VIDEO_AND_ANIMATION",
    "URLACTION_ACTIVEX_OVERRIDE_DOMAINLIST",
    "URLACTION_ACTIVEX_ALLOW_TDC",
    "URLACTION_ACTIVEX_CURR_MAX",
    "URLACTION_ACTIVEX_MAX",
    "URLACTION_SCRIPT_MIN",
    "URLACTION_SCRIPT_RUN",
    "URLACTION_SCRIPT_JAVA_USE",
    "URLACTION_SCRIPT_SAFE_ACTIVEX",
    "URLACTION_CROSS_DOMAIN_DATA",
    "URLACTION_SCRIPT_PASTE",
    "URLACTION_ALLOW_XDOMAIN_SUBFRAME_RESIZE",
    "URLACTION_SCRIPT_XSSFILTER",
    "URLACTION_SCRIPT_NAVIGATE",
    "URLACTION_PLUGGABLE_PROTOCOL_XHR",
    "URLACTION_ALLOW_VBSCRIPT_IE",
    "URLACTION_ALLOW_JSCRIPT_IE",
    "URLACTION_SCRIPT_CURR_MAX",
    "URLACTION_SCRIPT_MAX",
    "URLACTION_HTML_MIN",
    "URLACTION_HTML_SUBMIT_FORMS",
    "URLACTION_HTML_SUBMIT_FORMS_FROM",
    "URLACTION_HTML_SUBMIT_FORMS_TO",
    "URLACTION_HTML_FONT_DOWNLOAD",
    "URLACTION_HTML_JAVA_RUN",
    "URLACTION_HTML_USERDATA_SAVE",
    "URLACTION_HTML_SUBFRAME_NAVIGATE",
    "URLACTION_HTML_META_REFRESH",
    "URLACTION_HTML_MIXED_CONTENT",
    "URLACTION_HTML_INCLUDE_FILE_PATH",
    "URLACTION_HTML_ALLOW_INJECTED_DYNAMIC_HTML",
    "URLACTION_HTML_REQUIRE_UTF8_DOCUMENT_CODEPAGE",
    "URLACTION_HTML_ALLOW_CROSS_DOMAIN_CANVAS",
    "URLACTION_HTML_ALLOW_WINDOW_CLOSE",
    "URLACTION_HTML_ALLOW_CROSS_DOMAIN_WEBWORKER",
    "URLACTION_HTML_ALLOW_CROSS_DOMAIN_TEXTTRACK",
    "URLACTION_HTML_ALLOW_INDEXEDDB",
    "URLACTION_HTML_MAX",
    "URLACTION_SHELL_MIN",
    "URLACTION_SHELL_INSTALL_DTITEMS",
    "URLACTION_SHELL_MOVE_OR_COPY",
    "URLACTION_SHELL_FILE_DOWNLOAD",
    "URLACTION_SHELL_VERB",
    "URLACTION_SHELL_WEBVIEW_VERB",
    "URLACTION_SHELL_SHELLEXECUTE",
    "URLACTION_SHELL_EXECUTE_HIGHRISK",
    "URLACTION_SHELL_EXECUTE_MODRISK",
    "URLACTION_SHELL_EXECUTE_LOWRISK",
    "URLACTION_SHELL_POPUPMGR",
    "URLACTION_SHELL_RTF_OBJECTS_LOAD",
    "URLACTION_SHELL_ENHANCED_DRAGDROP_SECURITY",
    "URLACTION_SHELL_EXTENSIONSECURITY",
    "URLACTION_SHELL_SECURE_DRAGSOURCE",
    "URLACTION_SHELL_REMOTEQUERY",
    "URLACTION_SHELL_PREVIEW",
    "URLACTION_SHELL_SHARE",
    "URLACTION_SHELL_ALLOW_CROSS_SITE_SHARE",
    "URLACTION_SHELL_TOCTOU_RISK",
    "URLACTION_SHELL_CURR_MAX",
    "URLACTION_SHELL_MAX",
    "URLACTION_NETWORK_MIN",
    "URLACTION_CREDENTIALS_USE",
    "URLPOLICY_CREDENTIALS_SILENT_LOGON_OK",
    "URLPOLICY_CREDENTIALS_MUST_PROMPT_USER",
    "URLPOLICY_CREDENTIALS_CONDITIONAL_PROMPT",
    "URLPOLICY_CREDENTIALS_ANONYMOUS_ONLY",
    "URLACTION_AUTHENTICATE_CLIENT",
    "URLPOLICY_AUTHENTICATE_CLEARTEXT_OK",
    "URLPOLICY_AUTHENTICATE_CHALLENGE_RESPONSE",
    "URLPOLICY_AUTHENTICATE_MUTUAL_ONLY",
    "URLACTION_COOKIES",
    "URLACTION_COOKIES_SESSION",
    "URLACTION_CLIENT_CERT_PROMPT",
    "URLACTION_COOKIES_THIRD_PARTY",
    "URLACTION_COOKIES_SESSION_THIRD_PARTY",
    "URLACTION_COOKIES_ENABLED",
    "URLACTION_NETWORK_CURR_MAX",
    "URLACTION_NETWORK_MAX",
    "URLACTION_JAVA_MIN",
    "URLACTION_JAVA_PERMISSIONS",
    "URLPOLICY_JAVA_PROHIBIT",
    "URLPOLICY_JAVA_HIGH",
    "URLPOLICY_JAVA_MEDIUM",
    "URLPOLICY_JAVA_LOW",
    "URLPOLICY_JAVA_CUSTOM",
    "URLACTION_JAVA_CURR_MAX",
    "URLACTION_JAVA_MAX",
    "URLACTION_INFODELIVERY_MIN",
    "URLACTION_INFODELIVERY_NO_ADDING_CHANNELS",
    "URLACTION_INFODELIVERY_NO_EDITING_CHANNELS",
    "URLACTION_INFODELIVERY_NO_REMOVING_CHANNELS",
    "URLACTION_INFODELIVERY_NO_ADDING_SUBSCRIPTIONS",
    "URLACTION_INFODELIVERY_NO_EDITING_SUBSCRIPTIONS",
    "URLACTION_INFODELIVERY_NO_REMOVING_SUBSCRIPTIONS",
    "URLACTION_INFODELIVERY_NO_CHANNEL_LOGGING",
    "URLACTION_INFODELIVERY_CURR_MAX",
    "URLACTION_INFODELIVERY_MAX",
    "URLACTION_CHANNEL_SOFTDIST_MIN",
    "URLACTION_CHANNEL_SOFTDIST_PERMISSIONS",
    "URLPOLICY_CHANNEL_SOFTDIST_PROHIBIT",
    "URLPOLICY_CHANNEL_SOFTDIST_PRECACHE",
    "URLPOLICY_CHANNEL_SOFTDIST_AUTOINSTALL",
    "URLACTION_CHANNEL_SOFTDIST_MAX",
    "URLACTION_DOTNET_USERCONTROLS",
    "URLACTION_BEHAVIOR_MIN",
    "URLACTION_BEHAVIOR_RUN",
    "URLPOLICY_BEHAVIOR_CHECK_LIST",
    "URLACTION_FEATURE_MIN",
    "URLACTION_FEATURE_MIME_SNIFFING",
    "URLACTION_FEATURE_ZONE_ELEVATION",
    "URLACTION_FEATURE_WINDOW_RESTRICTIONS",
    "URLACTION_FEATURE_SCRIPT_STATUS_BAR",
    "URLACTION_FEATURE_FORCE_ADDR_AND_STATUS",
    "URLACTION_FEATURE_BLOCK_INPUT_PROMPTS",
    "URLACTION_FEATURE_DATA_BINDING",
    "URLACTION_FEATURE_CROSSDOMAIN_FOCUS_CHANGE",
    "URLACTION_AUTOMATIC_DOWNLOAD_UI_MIN",
    "URLACTION_AUTOMATIC_DOWNLOAD_UI",
    "URLACTION_AUTOMATIC_ACTIVEX_UI",
    "URLACTION_ALLOW_RESTRICTEDPROTOCOLS",
    "URLACTION_ALLOW_APEVALUATION",
    "URLACTION_ALLOW_XHR_EVALUATION",
    "URLACTION_WINDOWS_BROWSER_APPLICATIONS",
    "URLACTION_XPS_DOCUMENTS",
    "URLACTION_LOOSE_XAML",
    "URLACTION_LOWRIGHTS",
    "URLACTION_WINFX_SETUP",
    "URLACTION_INPRIVATE_BLOCKING",
    "URLACTION_ALLOW_AUDIO_VIDEO",
    "URLACTION_ALLOW_ACTIVEX_FILTERING",
    "URLACTION_ALLOW_STRUCTURED_STORAGE_SNIFFING",
    "URLACTION_ALLOW_AUDIO_VIDEO_PLUGINS",
    "URLACTION_ALLOW_ZONE_ELEVATION_VIA_OPT_OUT",
    "URLACTION_ALLOW_ZONE_ELEVATION_OPT_OUT_ADDITION",
    "URLACTION_ALLOW_CROSSDOMAIN_DROP_WITHIN_WINDOW",
    "URLACTION_ALLOW_CROSSDOMAIN_DROP_ACROSS_WINDOWS",
    "URLACTION_ALLOW_CROSSDOMAIN_APPCACHE_MANIFEST",
    "URLACTION_ALLOW_RENDER_LEGACY_DXTFILTERS",
    "URLACTION_ALLOW_ANTIMALWARE_SCANNING_OF_ACTIVEX",
    "URLACTION_ALLOW_CSS_EXPRESSIONS",
    "URLPOLICY_ALLOW",
    "URLPOLICY_QUERY",
    "URLPOLICY_DISALLOW",
    "URLPOLICY_NOTIFY_ON_ALLOW",
    "URLPOLICY_NOTIFY_ON_DISALLOW",
    "URLPOLICY_LOG_ON_ALLOW",
    "URLPOLICY_LOG_ON_DISALLOW",
    "URLPOLICY_MASK_PERMISSIONS",
    "URLPOLICY_DONTCHECKDLGBOX",
    "URLZONE_ESC_FLAG",
    "SECURITY_IE_STATE_GREEN",
    "SECURITY_IE_STATE_RED",
    "SOFTDIST_FLAG_USAGE_EMAIL",
    "SOFTDIST_FLAG_USAGE_PRECACHE",
    "SOFTDIST_FLAG_USAGE_AUTOINSTALL",
    "SOFTDIST_FLAG_DELETE_SUBSCRIPTION",
    "SOFTDIST_ADSTATE_NONE",
    "SOFTDIST_ADSTATE_AVAILABLE",
    "SOFTDIST_ADSTATE_DOWNLOADED",
    "SOFTDIST_ADSTATE_INSTALLED",
    "CONFIRMSAFETYACTION_LOADOBJECT",
    "IEObjectType",
    "IE_EPM_OBJECT_EVENT",
    "IE_EPM_OBJECT_MUTEX",
    "IE_EPM_OBJECT_SEMAPHORE",
    "IE_EPM_OBJECT_SHARED_MEMORY",
    "IE_EPM_OBJECT_WAITABLE_TIMER",
    "IE_EPM_OBJECT_FILE",
    "IE_EPM_OBJECT_NAMED_PIPE",
    "IE_EPM_OBJECT_REGISTRY",
    "IPersistMoniker",
    "MONIKERPROPERTY",
    "MIMETYPEPROP",
    "USE_SRC_URL",
    "CLASSIDPROP",
    "TRUSTEDDOWNLOADPROP",
    "POPUPLEVELPROP",
    "IMonikerProp",
    "IBindProtocol",
    "BINDVERB",
    "BINDVERB_GET",
    "BINDVERB_POST",
    "BINDVERB_PUT",
    "BINDVERB_CUSTOM",
    "BINDVERB_RESERVED1",
    "BINDF",
    "BINDF_ASYNCHRONOUS",
    "BINDF_ASYNCSTORAGE",
    "BINDF_NOPROGRESSIVERENDERING",
    "BINDF_OFFLINEOPERATION",
    "BINDF_GETNEWESTVERSION",
    "BINDF_NOWRITECACHE",
    "BINDF_NEEDFILE",
    "BINDF_PULLDATA",
    "BINDF_IGNORESECURITYPROBLEM",
    "BINDF_RESYNCHRONIZE",
    "BINDF_HYPERLINK",
    "BINDF_NO_UI",
    "BINDF_SILENTOPERATION",
    "BINDF_PRAGMA_NO_CACHE",
    "BINDF_GETCLASSOBJECT",
    "BINDF_RESERVED_1",
    "BINDF_FREE_THREADED",
    "BINDF_DIRECT_READ",
    "BINDF_FORMS_SUBMIT",
    "BINDF_GETFROMCACHE_IF_NET_FAIL",
    "BINDF_FROMURLMON",
    "BINDF_FWD_BACK",
    "BINDF_PREFERDEFAULTHANDLER",
    "BINDF_ENFORCERESTRICTED",
    "BINDF_RESERVED_2",
    "BINDF_RESERVED_3",
    "BINDF_RESERVED_4",
    "BINDF_RESERVED_5",
    "BINDF_RESERVED_6",
    "BINDF_RESERVED_7",
    "BINDF_RESERVED_8",
    "URL_ENCODING",
    "URL_ENCODING_NONE",
    "URL_ENCODING_ENABLE_UTF8",
    "URL_ENCODING_DISABLE_UTF8",
    "REMSECURITY_ATTRIBUTES",
    "RemBINDINFO",
    "RemFORMATETC",
    "BINDINFO_OPTIONS",
    "BINDINFO_OPTIONS_WININETFLAG",
    "BINDINFO_OPTIONS_ENABLE_UTF8",
    "BINDINFO_OPTIONS_DISABLE_UTF8",
    "BINDINFO_OPTIONS_USE_IE_ENCODING",
    "BINDINFO_OPTIONS_BINDTOOBJECT",
    "BINDINFO_OPTIONS_SECURITYOPTOUT",
    "BINDINFO_OPTIONS_IGNOREMIMETEXTPLAIN",
    "BINDINFO_OPTIONS_USEBINDSTRINGCREDS",
    "BINDINFO_OPTIONS_IGNOREHTTPHTTPSREDIRECTS",
    "BINDINFO_OPTIONS_IGNORE_SSLERRORS_ONCE",
    "BINDINFO_WPC_DOWNLOADBLOCKED",
    "BINDINFO_WPC_LOGGING_ENABLED",
    "BINDINFO_OPTIONS_ALLOWCONNECTDATA",
    "BINDINFO_OPTIONS_DISABLEAUTOREDIRECTS",
    "BINDINFO_OPTIONS_SHDOCVW_NAVIGATE",
    "BSCF",
    "BSCF_FIRSTDATANOTIFICATION",
    "BSCF_INTERMEDIATEDATANOTIFICATION",
    "BSCF_LASTDATANOTIFICATION",
    "BSCF_DATAFULLYAVAILABLE",
    "BSCF_AVAILABLEDATASIZEUNKNOWN",
    "BSCF_SKIPDRAINDATAFORFILEURLS",
    "BSCF_64BITLENGTHDOWNLOAD",
    "BINDSTATUS",
    "BINDSTATUS_FINDINGRESOURCE",
    "BINDSTATUS_CONNECTING",
    "BINDSTATUS_REDIRECTING",
    "BINDSTATUS_BEGINDOWNLOADDATA",
    "BINDSTATUS_DOWNLOADINGDATA",
    "BINDSTATUS_ENDDOWNLOADDATA",
    "BINDSTATUS_BEGINDOWNLOADCOMPONENTS",
    "BINDSTATUS_INSTALLINGCOMPONENTS",
    "BINDSTATUS_ENDDOWNLOADCOMPONENTS",
    "BINDSTATUS_USINGCACHEDCOPY",
    "BINDSTATUS_SENDINGREQUEST",
    "BINDSTATUS_CLASSIDAVAILABLE",
    "BINDSTATUS_MIMETYPEAVAILABLE",
    "BINDSTATUS_CACHEFILENAMEAVAILABLE",
    "BINDSTATUS_BEGINSYNCOPERATION",
    "BINDSTATUS_ENDSYNCOPERATION",
    "BINDSTATUS_BEGINUPLOADDATA",
    "BINDSTATUS_UPLOADINGDATA",
    "BINDSTATUS_ENDUPLOADDATA",
    "BINDSTATUS_PROTOCOLCLASSID",
    "BINDSTATUS_ENCODING",
    "BINDSTATUS_VERIFIEDMIMETYPEAVAILABLE",
    "BINDSTATUS_CLASSINSTALLLOCATION",
    "BINDSTATUS_DECODING",
    "BINDSTATUS_LOADINGMIMEHANDLER",
    "BINDSTATUS_CONTENTDISPOSITIONATTACH",
    "BINDSTATUS_FILTERREPORTMIMETYPE",
    "BINDSTATUS_CLSIDCANINSTANTIATE",
    "BINDSTATUS_IUNKNOWNAVAILABLE",
    "BINDSTATUS_DIRECTBIND",
    "BINDSTATUS_RAWMIMETYPE",
    "BINDSTATUS_PROXYDETECTING",
    "BINDSTATUS_ACCEPTRANGES",
    "BINDSTATUS_COOKIE_SENT",
    "BINDSTATUS_COMPACT_POLICY_RECEIVED",
    "BINDSTATUS_COOKIE_SUPPRESSED",
    "BINDSTATUS_COOKIE_STATE_UNKNOWN",
    "BINDSTATUS_COOKIE_STATE_ACCEPT",
    "BINDSTATUS_COOKIE_STATE_REJECT",
    "BINDSTATUS_COOKIE_STATE_PROMPT",
    "BINDSTATUS_COOKIE_STATE_LEASH",
    "BINDSTATUS_COOKIE_STATE_DOWNGRADE",
    "BINDSTATUS_POLICY_HREF",
    "BINDSTATUS_P3P_HEADER",
    "BINDSTATUS_SESSION_COOKIE_RECEIVED",
    "BINDSTATUS_PERSISTENT_COOKIE_RECEIVED",
    "BINDSTATUS_SESSION_COOKIES_ALLOWED",
    "BINDSTATUS_CACHECONTROL",
    "BINDSTATUS_CONTENTDISPOSITIONFILENAME",
    "BINDSTATUS_MIMETEXTPLAINMISMATCH",
    "BINDSTATUS_PUBLISHERAVAILABLE",
    "BINDSTATUS_DISPLAYNAMEAVAILABLE",
    "BINDSTATUS_SSLUX_NAVBLOCKED",
    "BINDSTATUS_SERVER_MIMETYPEAVAILABLE",
    "BINDSTATUS_SNIFFED_CLASSIDAVAILABLE",
    "BINDSTATUS_64BIT_PROGRESS",
    "BINDSTATUS_LAST",
    "BINDSTATUS_RESERVED_0",
    "BINDSTATUS_RESERVED_1",
    "BINDSTATUS_RESERVED_2",
    "BINDSTATUS_RESERVED_3",
    "BINDSTATUS_RESERVED_4",
    "BINDSTATUS_RESERVED_5",
    "BINDSTATUS_RESERVED_6",
    "BINDSTATUS_RESERVED_7",
    "BINDSTATUS_RESERVED_8",
    "BINDSTATUS_RESERVED_9",
    "BINDSTATUS_RESERVED_A",
    "BINDSTATUS_RESERVED_B",
    "BINDSTATUS_RESERVED_C",
    "BINDSTATUS_RESERVED_D",
    "BINDSTATUS_RESERVED_E",
    "BINDSTATUS_RESERVED_F",
    "BINDSTATUS_RESERVED_10",
    "BINDSTATUS_RESERVED_11",
    "BINDSTATUS_RESERVED_12",
    "BINDSTATUS_RESERVED_13",
    "BINDSTATUS_RESERVED_14",
    "BINDSTATUS_LAST_PRIVATE",
    "BINDF2",
    "BINDF2_DISABLEBASICOVERHTTP",
    "BINDF2_DISABLEAUTOCOOKIEHANDLING",
    "BINDF2_READ_DATA_GREATER_THAN_4GB",
    "BINDF2_DISABLE_HTTP_REDIRECT_XSECURITYID",
    "BINDF2_SETDOWNLOADMODE",
    "BINDF2_DISABLE_HTTP_REDIRECT_CACHING",
    "BINDF2_KEEP_CALLBACK_MODULE_LOADED",
    "BINDF2_ALLOW_PROXY_CRED_PROMPT",
    "BINDF2_RESERVED_17",
    "BINDF2_RESERVED_16",
    "BINDF2_RESERVED_15",
    "BINDF2_RESERVED_14",
    "BINDF2_RESERVED_13",
    "BINDF2_RESERVED_12",
    "BINDF2_RESERVED_11",
    "BINDF2_RESERVED_10",
    "BINDF2_RESERVED_F",
    "BINDF2_RESERVED_E",
    "BINDF2_RESERVED_D",
    "BINDF2_RESERVED_C",
    "BINDF2_RESERVED_B",
    "BINDF2_RESERVED_A",
    "BINDF2_RESERVED_9",
    "BINDF2_RESERVED_8",
    "BINDF2_RESERVED_7",
    "BINDF2_RESERVED_6",
    "BINDF2_RESERVED_5",
    "BINDF2_RESERVED_4",
    "BINDF2_RESERVED_3",
    "BINDF2_RESERVED_2",
    "BINDF2_RESERVED_1",
    "AUTHENTICATEF",
    "AUTHENTICATEF_PROXY",
    "AUTHENTICATEF_BASIC",
    "AUTHENTICATEF_HTTP",
    "IHttpNegotiate",
    "IHttpNegotiate2",
    "IHttpNegotiate3",
    "IWinInetFileStream",
    "IWindowForBindingUI",
    "CIP_STATUS",
    "CIP_DISK_FULL",
    "CIP_ACCESS_DENIED",
    "CIP_NEWER_VERSION_EXISTS",
    "CIP_OLDER_VERSION_EXISTS",
    "CIP_NAME_CONFLICT",
    "CIP_TRUST_VERIFICATION_COMPONENT_MISSING",
    "CIP_EXE_SELF_REGISTERATION_TIMEOUT",
    "CIP_UNSAFE_TO_ABORT",
    "CIP_NEED_REBOOT",
    "CIP_NEED_REBOOT_UI_PERMISSION",
    "ICodeInstall",
    "Uri_HOST_TYPE",
    "Uri_HOST_UNKNOWN",
    "Uri_HOST_DNS",
    "Uri_HOST_IPV4",
    "Uri_HOST_IPV6",
    "Uri_HOST_IDN",
    "IUriContainer",
    "IUriBuilderFactory",
    "IWinInetInfo",
    "IHttpSecurity",
    "IWinInetHttpInfo",
    "IWinInetHttpTimeouts",
    "IWinInetCacheHints",
    "IWinInetCacheHints2",
    "IInternet",
    "BINDSTRING",
    "BINDSTRING_HEADERS",
    "BINDSTRING_ACCEPT_MIMES",
    "BINDSTRING_EXTRA_URL",
    "BINDSTRING_LANGUAGE",
    "BINDSTRING_USERNAME",
    "BINDSTRING_PASSWORD",
    "BINDSTRING_UA_PIXELS",
    "BINDSTRING_UA_COLOR",
    "BINDSTRING_OS",
    "BINDSTRING_USER_AGENT",
    "BINDSTRING_ACCEPT_ENCODINGS",
    "BINDSTRING_POST_COOKIE",
    "BINDSTRING_POST_DATA_MIME",
    "BINDSTRING_URL",
    "BINDSTRING_IID",
    "BINDSTRING_FLAG_BIND_TO_OBJECT",
    "BINDSTRING_PTR_BIND_CONTEXT",
    "BINDSTRING_XDR_ORIGIN",
    "BINDSTRING_DOWNLOADPATH",
    "BINDSTRING_ROOTDOC_URL",
    "BINDSTRING_INITIAL_FILENAME",
    "BINDSTRING_PROXY_USERNAME",
    "BINDSTRING_PROXY_PASSWORD",
    "BINDSTRING_ENTERPRISE_ID",
    "BINDSTRING_DOC_URL",
    "BINDSTRING_SAMESITE_COOKIE_LEVEL",
    "IInternetBindInfo",
    "IInternetBindInfoEx",
    "PI_FLAGS",
    "PI_PARSE_URL",
    "PI_FILTER_MODE",
    "PI_FORCE_ASYNC",
    "PI_USE_WORKERTHREAD",
    "PI_MIMEVERIFICATION",
    "PI_CLSIDLOOKUP",
    "PI_DATAPROGRESS",
    "PI_SYNCHRONOUS",
    "PI_APARTMENTTHREADED",
    "PI_CLASSINSTALL",
    "PI_PASSONBINDCTX",
    "PI_NOMIMEHANDLER",
    "PI_LOADAPPDIRECT",
    "PD_FORCE_SWITCH",
    "PI_PREFERDEFAULTHANDLER",
    "PROTOCOLDATA",
    "StartParam",
    "IInternetProtocolRoot",
    "IInternetProtocol",
    "IInternetProtocolEx",
    "IInternetProtocolSink",
    "IInternetProtocolSinkStackable",
    "OIBDG_FLAGS",
    "OIBDG_APARTMENTTHREADED",
    "OIBDG_DATAONLY",
    "IInternetSession",
    "IInternetThreadSwitch",
    "IInternetPriority",
    "PARSEACTION",
    "PARSE_CANONICALIZE",
    "PARSE_FRIENDLY",
    "PARSE_SECURITY_URL",
    "PARSE_ROOTDOCUMENT",
    "PARSE_DOCUMENT",
    "PARSE_ANCHOR",
    "PARSE_ENCODE_IS_UNESCAPE",
    "PARSE_DECODE_IS_ESCAPE",
    "PARSE_PATH_FROM_URL",
    "PARSE_URL_FROM_PATH",
    "PARSE_MIME",
    "PARSE_SERVER",
    "PARSE_SCHEMA",
    "PARSE_SITE",
    "PARSE_DOMAIN",
    "PARSE_LOCATION",
    "PARSE_SECURITY_DOMAIN",
    "PARSE_ESCAPE",
    "PARSE_UNESCAPE",
    "PSUACTION",
    "PSU_DEFAULT",
    "PSU_SECURITY_URL_ONLY",
    "QUERYOPTION",
    "QUERY_EXPIRATION_DATE",
    "QUERY_TIME_OF_LAST_CHANGE",
    "QUERY_CONTENT_ENCODING",
    "QUERY_CONTENT_TYPE",
    "QUERY_REFRESH",
    "QUERY_RECOMBINE",
    "QUERY_CAN_NAVIGATE",
    "QUERY_USES_NETWORK",
    "QUERY_IS_CACHED",
    "QUERY_IS_INSTALLEDENTRY",
    "QUERY_IS_CACHED_OR_MAPPED",
    "QUERY_USES_CACHE",
    "QUERY_IS_SECURE",
    "QUERY_IS_SAFE",
    "QUERY_USES_HISTORYFOLDER",
    "QUERY_IS_CACHED_AND_USABLE_OFFLINE",
    "IInternetProtocolInfo",
    "INTERNETFEATURELIST",
    "FEATURE_OBJECT_CACHING",
    "FEATURE_ZONE_ELEVATION",
    "FEATURE_MIME_HANDLING",
    "FEATURE_MIME_SNIFFING",
    "FEATURE_WINDOW_RESTRICTIONS",
    "FEATURE_WEBOC_POPUPMANAGEMENT",
    "FEATURE_BEHAVIORS",
    "FEATURE_DISABLE_MK_PROTOCOL",
    "FEATURE_LOCALMACHINE_LOCKDOWN",
    "FEATURE_SECURITYBAND",
    "FEATURE_RESTRICT_ACTIVEXINSTALL",
    "FEATURE_VALIDATE_NAVIGATE_URL",
    "FEATURE_RESTRICT_FILEDOWNLOAD",
    "FEATURE_ADDON_MANAGEMENT",
    "FEATURE_PROTOCOL_LOCKDOWN",
    "FEATURE_HTTP_USERNAME_PASSWORD_DISABLE",
    "FEATURE_SAFE_BINDTOOBJECT",
    "FEATURE_UNC_SAVEDFILECHECK",
    "FEATURE_GET_URL_DOM_FILEPATH_UNENCODED",
    "FEATURE_TABBED_BROWSING",
    "FEATURE_SSLUX",
    "FEATURE_DISABLE_NAVIGATION_SOUNDS",
    "FEATURE_DISABLE_LEGACY_COMPRESSION",
    "FEATURE_FORCE_ADDR_AND_STATUS",
    "FEATURE_XMLHTTP",
    "FEATURE_DISABLE_TELNET_PROTOCOL",
    "FEATURE_FEEDS",
    "FEATURE_BLOCK_INPUT_PROMPTS",
    "FEATURE_ENTRY_COUNT",
    "IInternetSecurityMgrSite",
    "PUAF",
    "PUAF_DEFAULT",
    "PUAF_NOUI",
    "PUAF_ISFILE",
    "PUAF_WARN_IF_DENIED",
    "PUAF_FORCEUI_FOREGROUND",
    "PUAF_CHECK_TIFS",
    "PUAF_DONTCHECKBOXINDIALOG",
    "PUAF_TRUSTED",
    "PUAF_ACCEPT_WILDCARD_SCHEME",
    "PUAF_ENFORCERESTRICTED",
    "PUAF_NOSAVEDFILECHECK",
    "PUAF_REQUIRESAVEDFILECHECK",
    "PUAF_DONT_USE_CACHE",
    "PUAF_RESERVED1",
    "PUAF_RESERVED2",
    "PUAF_LMZ_UNLOCKED",
    "PUAF_LMZ_LOCKED",
    "PUAF_DEFAULTZONEPOL",
    "PUAF_NPL_USE_LOCKED_IF_RESTRICTED",
    "PUAF_NOUIIFLOCKED",
    "PUAF_DRAGPROTOCOLCHECK",
    "PUAFOUT",
    "PUAFOUT_DEFAULT",
    "PUAFOUT_ISLOCKZONEPOLICY",
    "SZM_FLAGS",
    "SZM_CREATE",
    "SZM_DELETE",
    "IInternetSecurityManager",
    "IInternetSecurityManagerEx",
    "IInternetSecurityManagerEx2",
    "IZoneIdentifier",
    "IZoneIdentifier2",
    "IInternetHostSecurityManager",
    "URLZONE",
    "URLZONE_INVALID",
    "URLZONE_PREDEFINED_MIN",
    "URLZONE_LOCAL_MACHINE",
    "URLZONE_INTRANET",
    "URLZONE_TRUSTED",
    "URLZONE_INTERNET",
    "URLZONE_UNTRUSTED",
    "URLZONE_PREDEFINED_MAX",
    "URLZONE_USER_MIN",
    "URLZONE_USER_MAX",
    "URLTEMPLATE",
    "URLTEMPLATE_CUSTOM",
    "URLTEMPLATE_PREDEFINED_MIN",
    "URLTEMPLATE_LOW",
    "URLTEMPLATE_MEDLOW",
    "URLTEMPLATE_MEDIUM",
    "URLTEMPLATE_MEDHIGH",
    "URLTEMPLATE_HIGH",
    "URLTEMPLATE_PREDEFINED_MAX",
    "INET_ZONE_MANAGER_CONSTANTS",
    "MAX_ZONE_PATH",
    "MAX_ZONE_DESCRIPTION",
    "ZAFLAGS",
    "ZAFLAGS_CUSTOM_EDIT",
    "ZAFLAGS_ADD_SITES",
    "ZAFLAGS_REQUIRE_VERIFICATION",
    "ZAFLAGS_INCLUDE_PROXY_OVERRIDE",
    "ZAFLAGS_INCLUDE_INTRANET_SITES",
    "ZAFLAGS_NO_UI",
    "ZAFLAGS_SUPPORTS_VERIFICATION",
    "ZAFLAGS_UNC_AS_INTRANET",
    "ZAFLAGS_DETECT_INTRANET",
    "ZAFLAGS_USE_LOCKED_ZONES",
    "ZAFLAGS_VERIFY_TEMPLATE_SETTINGS",
    "ZAFLAGS_NO_CACHE",
    "ZONEATTRIBUTES",
    "URLZONEREG",
    "URLZONEREG_DEFAULT",
    "URLZONEREG_HKLM",
    "URLZONEREG_HKCU",
    "IInternetZoneManager",
    "IInternetZoneManagerEx",
    "IInternetZoneManagerEx2",
    "CODEBASEHOLD",
    "SOFTDISTINFO",
    "ISoftDistExt",
    "ICatalogFileInfo",
    "IDataFilter",
    "PROTOCOLFILTERDATA",
    "DATAINFO",
    "IEncodingFilterFactory",
    "HIT_LOGGING_INFO",
    "CONFIRMSAFETY",
    "IWrappedProtocol",
    "BINDHANDLETYPES",
    "BINDHANDLETYPES_APPCACHE",
    "BINDHANDLETYPES_DEPENDENCY",
    "BINDHANDLETYPES_COUNT",
    "IGetBindHandle",
    "PROTOCOL_ARGUMENT",
    "IBindCallbackRedirect",
    "IBindHttpSecurity",
    "CreateURLMoniker",
    "CreateURLMonikerEx",
    "GetClassURL",
    "CreateAsyncBindCtx",
    "CreateURLMonikerEx2",
    "CreateAsyncBindCtxEx",
    "MkParseDisplayNameEx",
    "RegisterBindStatusCallback",
    "RevokeBindStatusCallback",
    "GetClassFileOrMime",
    "IsValidURL",
    "CoGetClassObjectFromURL",
    "IEInstallScope",
    "FaultInIEFeature",
    "GetComponentIDFromCLSSPEC",
    "IsAsyncMoniker",
    "RegisterMediaTypes",
    "FindMediaType",
    "CreateFormatEnumerator",
    "RegisterFormatEnumerator",
    "RevokeFormatEnumerator",
    "RegisterMediaTypeClass",
    "FindMediaTypeClass",
    "UrlMkSetSessionOption",
    "UrlMkGetSessionOption",
    "FindMimeFromData",
    "ObtainUserAgentString",
    "CompareSecurityIds",
    "CompatFlagsFromClsid",
    "SetAccessForIEAppContainer",
    "HlinkSimpleNavigateToString",
    "HlinkSimpleNavigateToMoniker",
    "URLOpenStreamA",
    "URLOpenStreamW",
    "URLOpenStream",
    "URLOpenPullStreamA",
    "URLOpenPullStreamW",
    "URLOpenPullStream",
    "URLDownloadToFileA",
    "URLDownloadToFileW",
    "URLDownloadToFile",
    "URLDownloadToCacheFileA",
    "URLDownloadToCacheFileW",
    "URLDownloadToCacheFile",
    "URLOpenBlockingStreamA",
    "URLOpenBlockingStreamW",
    "URLOpenBlockingStream",
    "HlinkGoBack",
    "HlinkGoForward",
    "HlinkNavigateString",
    "HlinkNavigateMoniker",
    "CoInternetParseUrl",
    "CoInternetParseIUri",
    "CoInternetCombineUrl",
    "CoInternetCombineUrlEx",
    "CoInternetCombineIUri",
    "CoInternetCompareUrl",
    "CoInternetGetProtocolFlags",
    "CoInternetQueryInfo",
    "CoInternetGetSession",
    "CoInternetGetSecurityUrl",
    "CoInternetGetSecurityUrlEx",
    "CoInternetSetFeatureEnabled",
    "CoInternetIsFeatureEnabled",
    "CoInternetIsFeatureEnabledForUrl",
    "CoInternetIsFeatureEnabledForIUri",
    "CoInternetIsFeatureZoneElevationEnabled",
    "CopyStgMedium",
    "CopyBindInfo",
    "ReleaseBindInfo",
    "IEGetUserPrivateNamespaceName",
    "CoInternetCreateSecurityManager",
    "CoInternetCreateZoneManager",
    "GetSoftwareUpdateInfo",
    "SetSoftwareUpdateAdvertisementState",
    "IsLoggingEnabledA",
    "IsLoggingEnabledW",
    "IsLoggingEnabled",
    "WriteHitLogging",
]
