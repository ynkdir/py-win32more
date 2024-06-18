from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Data.Xml.MsXml
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.Com.Urlmon
AUTHENTICATEF = Int32
AUTHENTICATEF_PROXY: win32more.Windows.Win32.System.Com.Urlmon.AUTHENTICATEF = 1
AUTHENTICATEF_BASIC: win32more.Windows.Win32.System.Com.Urlmon.AUTHENTICATEF = 2
AUTHENTICATEF_HTTP: win32more.Windows.Win32.System.Com.Urlmon.AUTHENTICATEF = 4
MKSYS_URLMONIKER: UInt32 = 6
URL_MK_LEGACY: UInt32 = 0
URL_MK_UNIFORM: UInt32 = 1
URL_MK_NO_CANONICALIZE: UInt32 = 2
FIEF_FLAG_FORCE_JITUI: UInt32 = 1
FIEF_FLAG_PEEK: UInt32 = 2
FIEF_FLAG_SKIP_INSTALLED_VERSION_CHECK: UInt32 = 4
FIEF_FLAG_RESERVED_0: UInt32 = 8
FMFD_DEFAULT: UInt32 = 0
FMFD_URLASFILENAME: UInt32 = 1
FMFD_ENABLEMIMESNIFFING: UInt32 = 2
FMFD_IGNOREMIMETEXTPLAIN: UInt32 = 4
FMFD_SERVERMIME: UInt32 = 8
FMFD_RESPECTTEXTPLAIN: UInt32 = 16
FMFD_RETURNUPDATEDIMGMIMES: UInt32 = 32
FMFD_RESERVED_1: UInt32 = 64
FMFD_RESERVED_2: UInt32 = 128
UAS_EXACTLEGACY: UInt32 = 4096
URLMON_OPTION_USERAGENT: UInt32 = 268435457
URLMON_OPTION_USERAGENT_REFRESH: UInt32 = 268435458
URLMON_OPTION_URL_ENCODING: UInt32 = 268435460
URLMON_OPTION_USE_BINDSTRINGCREDS: UInt32 = 268435464
URLMON_OPTION_USE_BROWSERAPPSDOCUMENTS: UInt32 = 268435472
CF_NULL: UInt32 = 0
MK_S_ASYNCHRONOUS: win32more.Windows.Win32.Foundation.HRESULT = 262632
S_ASYNCHRONOUS: Int32 = 262632
E_PENDING: win32more.Windows.Win32.Foundation.HRESULT = -2147483638
INET_E_INVALID_URL: win32more.Windows.Win32.Foundation.HRESULT = -2146697214
INET_E_NO_SESSION: win32more.Windows.Win32.Foundation.HRESULT = -2146697213
INET_E_CANNOT_CONNECT: win32more.Windows.Win32.Foundation.HRESULT = -2146697212
INET_E_RESOURCE_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2146697211
INET_E_OBJECT_NOT_FOUND: win32more.Windows.Win32.Foundation.HRESULT = -2146697210
INET_E_DATA_NOT_AVAILABLE: win32more.Windows.Win32.Foundation.HRESULT = -2146697209
INET_E_DOWNLOAD_FAILURE: win32more.Windows.Win32.Foundation.HRESULT = -2146697208
INET_E_AUTHENTICATION_REQUIRED: win32more.Windows.Win32.Foundation.HRESULT = -2146697207
INET_E_NO_VALID_MEDIA: win32more.Windows.Win32.Foundation.HRESULT = -2146697206
INET_E_CONNECTION_TIMEOUT: win32more.Windows.Win32.Foundation.HRESULT = -2146697205
INET_E_INVALID_REQUEST: win32more.Windows.Win32.Foundation.HRESULT = -2146697204
INET_E_UNKNOWN_PROTOCOL: win32more.Windows.Win32.Foundation.HRESULT = -2146697203
INET_E_SECURITY_PROBLEM: win32more.Windows.Win32.Foundation.HRESULT = -2146697202
INET_E_CANNOT_LOAD_DATA: win32more.Windows.Win32.Foundation.HRESULT = -2146697201
INET_E_CANNOT_INSTANTIATE_OBJECT: win32more.Windows.Win32.Foundation.HRESULT = -2146697200
INET_E_INVALID_CERTIFICATE: win32more.Windows.Win32.Foundation.HRESULT = -2146697191
INET_E_REDIRECT_FAILED: win32more.Windows.Win32.Foundation.HRESULT = -2146697196
INET_E_REDIRECT_TO_DIR: win32more.Windows.Win32.Foundation.HRESULT = -2146697195
INET_E_CANNOT_LOCK_REQUEST: win32more.Windows.Win32.Foundation.HRESULT = -2146697194
INET_E_USE_EXTEND_BINDING: win32more.Windows.Win32.Foundation.HRESULT = -2146697193
INET_E_TERMINATED_BIND: win32more.Windows.Win32.Foundation.HRESULT = -2146697192
INET_E_RESERVED_1: win32more.Windows.Win32.Foundation.HRESULT = -2146697190
INET_E_BLOCKED_REDIRECT_XSECURITYID: win32more.Windows.Win32.Foundation.HRESULT = -2146697189
INET_E_DOMINJECTIONVALIDATION: win32more.Windows.Win32.Foundation.HRESULT = -2146697188
INET_E_VTAB_SWITCH_FORCE_ENGINE: win32more.Windows.Win32.Foundation.HRESULT = -2146697187
INET_E_HSTS_CERTIFICATE_ERROR: win32more.Windows.Win32.Foundation.HRESULT = -2146697186
INET_E_RESERVED_2: win32more.Windows.Win32.Foundation.HRESULT = -2146697185
INET_E_RESERVED_3: win32more.Windows.Win32.Foundation.HRESULT = -2146697184
INET_E_RESERVED_4: win32more.Windows.Win32.Foundation.HRESULT = -2146697183
INET_E_RESERVED_5: win32more.Windows.Win32.Foundation.HRESULT = -2146697182
INET_E_ERROR_FIRST: win32more.Windows.Win32.Foundation.HRESULT = -2146697214
INET_E_CODE_DOWNLOAD_DECLINED: win32more.Windows.Win32.Foundation.HRESULT = -2146696960
INET_E_RESULT_DISPATCHED: win32more.Windows.Win32.Foundation.HRESULT = -2146696704
INET_E_CANNOT_REPLACE_SFP_FILE: win32more.Windows.Win32.Foundation.HRESULT = -2146696448
INET_E_CODE_INSTALL_SUPPRESSED: win32more.Windows.Win32.Foundation.HRESULT = -2146696192
INET_E_CODE_INSTALL_BLOCKED_BY_HASH_POLICY: win32more.Windows.Win32.Foundation.HRESULT = -2146695936
INET_E_DOWNLOAD_BLOCKED_BY_INPRIVATE: win32more.Windows.Win32.Foundation.HRESULT = -2146695935
INET_E_CODE_INSTALL_BLOCKED_IMMERSIVE: win32more.Windows.Win32.Foundation.HRESULT = -2146695934
INET_E_FORBIDFRAMING: win32more.Windows.Win32.Foundation.HRESULT = -2146695933
INET_E_CODE_INSTALL_BLOCKED_ARM: win32more.Windows.Win32.Foundation.HRESULT = -2146695932
INET_E_BLOCKED_PLUGGABLE_PROTOCOL: win32more.Windows.Win32.Foundation.HRESULT = -2146695931
INET_E_BLOCKED_ENHANCEDPROTECTEDMODE: win32more.Windows.Win32.Foundation.HRESULT = -2146695930
INET_E_CODE_INSTALL_BLOCKED_BITNESS: win32more.Windows.Win32.Foundation.HRESULT = -2146695929
INET_E_DOWNLOAD_BLOCKED_BY_CSP: win32more.Windows.Win32.Foundation.HRESULT = -2146695928
INET_E_ERROR_LAST: Int32 = -2146695928
Uri_DISPLAY_NO_FRAGMENT: UInt32 = 1
Uri_PUNYCODE_IDN_HOST: UInt32 = 2
Uri_DISPLAY_IDN_HOST: UInt32 = 4
Uri_DISPLAY_NO_PUNYCODE: UInt32 = 8
Uri_ENCODING_USER_INFO_AND_PATH_IS_PERCENT_ENCODED_UTF8: UInt32 = 1
Uri_ENCODING_USER_INFO_AND_PATH_IS_CP: UInt32 = 2
Uri_ENCODING_HOST_IS_IDN: UInt32 = 4
Uri_ENCODING_HOST_IS_PERCENT_ENCODED_UTF8: UInt32 = 8
Uri_ENCODING_HOST_IS_PERCENT_ENCODED_CP: UInt32 = 16
Uri_ENCODING_QUERY_AND_FRAGMENT_IS_PERCENT_ENCODED_UTF8: UInt32 = 32
Uri_ENCODING_QUERY_AND_FRAGMENT_IS_CP: UInt32 = 64
UriBuilder_USE_ORIGINAL_FLAGS: UInt32 = 1
WININETINFO_OPTION_LOCK_HANDLE: UInt32 = 65534
URLOSTRM_USECACHEDCOPY_ONLY: UInt32 = 1
URLOSTRM_USECACHEDCOPY: UInt32 = 2
URLOSTRM_GETNEWESTVERSION: UInt32 = 3
SET_FEATURE_ON_THREAD: UInt32 = 1
SET_FEATURE_ON_PROCESS: UInt32 = 2
SET_FEATURE_IN_REGISTRY: UInt32 = 4
SET_FEATURE_ON_THREAD_LOCALMACHINE: UInt32 = 8
SET_FEATURE_ON_THREAD_INTRANET: UInt32 = 16
SET_FEATURE_ON_THREAD_TRUSTED: UInt32 = 32
SET_FEATURE_ON_THREAD_INTERNET: UInt32 = 64
SET_FEATURE_ON_THREAD_RESTRICTED: UInt32 = 128
GET_FEATURE_FROM_THREAD: UInt32 = 1
GET_FEATURE_FROM_PROCESS: UInt32 = 2
GET_FEATURE_FROM_REGISTRY: UInt32 = 4
GET_FEATURE_FROM_THREAD_LOCALMACHINE: UInt32 = 8
GET_FEATURE_FROM_THREAD_INTRANET: UInt32 = 16
GET_FEATURE_FROM_THREAD_TRUSTED: UInt32 = 32
GET_FEATURE_FROM_THREAD_INTERNET: UInt32 = 64
GET_FEATURE_FROM_THREAD_RESTRICTED: UInt32 = 128
INET_E_USE_DEFAULT_PROTOCOLHANDLER: win32more.Windows.Win32.Foundation.HRESULT = -2146697199
INET_E_USE_DEFAULT_SETTING: win32more.Windows.Win32.Foundation.HRESULT = -2146697198
INET_E_DEFAULT_ACTION: Int32 = -2146697199
INET_E_QUERYOPTION_UNKNOWN: win32more.Windows.Win32.Foundation.HRESULT = -2146697197
INET_E_REDIRECTING: win32more.Windows.Win32.Foundation.HRESULT = -2146697196
PROTOCOLFLAG_NO_PICS_CHECK: UInt32 = 1
MUTZ_NOSAVEDFILECHECK: UInt32 = 1
MUTZ_ISFILE: UInt32 = 2
MUTZ_ACCEPT_WILDCARD_SCHEME: UInt32 = 128
MUTZ_ENFORCERESTRICTED: UInt32 = 256
MUTZ_RESERVED: UInt32 = 512
MUTZ_REQUIRESAVEDFILECHECK: UInt32 = 1024
MUTZ_DONT_UNESCAPE: UInt32 = 2048
MUTZ_DONT_USE_CACHE: UInt32 = 4096
MUTZ_FORCE_INTRANET_FLAGS: UInt32 = 8192
MUTZ_IGNORE_ZONE_MAPPINGS: UInt32 = 16384
MAX_SIZE_SECURITY_ID: UInt32 = 512
URLACTION_MIN: UInt32 = 4096
URLACTION_DOWNLOAD_MIN: UInt32 = 4096
URLACTION_DOWNLOAD_SIGNED_ACTIVEX: UInt32 = 4097
URLACTION_DOWNLOAD_UNSIGNED_ACTIVEX: UInt32 = 4100
URLACTION_DOWNLOAD_CURR_MAX: UInt32 = 4100
URLACTION_DOWNLOAD_MAX: UInt32 = 4607
URLACTION_ACTIVEX_MIN: UInt32 = 4608
URLACTION_ACTIVEX_RUN: UInt32 = 4608
URLPOLICY_ACTIVEX_CHECK_LIST: UInt32 = 65536
URLACTION_ACTIVEX_OVERRIDE_OBJECT_SAFETY: UInt32 = 4609
URLACTION_ACTIVEX_OVERRIDE_DATA_SAFETY: UInt32 = 4610
URLACTION_ACTIVEX_OVERRIDE_SCRIPT_SAFETY: UInt32 = 4611
URLACTION_SCRIPT_OVERRIDE_SAFETY: UInt32 = 5121
URLACTION_ACTIVEX_CONFIRM_NOOBJECTSAFETY: UInt32 = 4612
URLACTION_ACTIVEX_TREATASUNTRUSTED: UInt32 = 4613
URLACTION_ACTIVEX_NO_WEBOC_SCRIPT: UInt32 = 4614
URLACTION_ACTIVEX_OVERRIDE_REPURPOSEDETECTION: UInt32 = 4615
URLACTION_ACTIVEX_OVERRIDE_OPTIN: UInt32 = 4616
URLACTION_ACTIVEX_SCRIPTLET_RUN: UInt32 = 4617
URLACTION_ACTIVEX_DYNSRC_VIDEO_AND_ANIMATION: UInt32 = 4618
URLACTION_ACTIVEX_OVERRIDE_DOMAINLIST: UInt32 = 4619
URLACTION_ACTIVEX_ALLOW_TDC: UInt32 = 4620
URLACTION_ACTIVEX_CURR_MAX: UInt32 = 4620
URLACTION_ACTIVEX_MAX: UInt32 = 5119
URLACTION_SCRIPT_MIN: UInt32 = 5120
URLACTION_SCRIPT_RUN: UInt32 = 5120
URLACTION_SCRIPT_JAVA_USE: UInt32 = 5122
URLACTION_SCRIPT_SAFE_ACTIVEX: UInt32 = 5125
URLACTION_CROSS_DOMAIN_DATA: UInt32 = 5126
URLACTION_SCRIPT_PASTE: UInt32 = 5127
URLACTION_ALLOW_XDOMAIN_SUBFRAME_RESIZE: UInt32 = 5128
URLACTION_SCRIPT_XSSFILTER: UInt32 = 5129
URLACTION_SCRIPT_NAVIGATE: UInt32 = 5130
URLACTION_PLUGGABLE_PROTOCOL_XHR: UInt32 = 5131
URLACTION_ALLOW_VBSCRIPT_IE: UInt32 = 5132
URLACTION_ALLOW_JSCRIPT_IE: UInt32 = 5133
URLACTION_SCRIPT_CURR_MAX: UInt32 = 5133
URLACTION_SCRIPT_MAX: UInt32 = 5631
URLACTION_HTML_MIN: UInt32 = 5632
URLACTION_HTML_SUBMIT_FORMS: UInt32 = 5633
URLACTION_HTML_SUBMIT_FORMS_FROM: UInt32 = 5634
URLACTION_HTML_SUBMIT_FORMS_TO: UInt32 = 5635
URLACTION_HTML_FONT_DOWNLOAD: UInt32 = 5636
URLACTION_HTML_JAVA_RUN: UInt32 = 5637
URLACTION_HTML_USERDATA_SAVE: UInt32 = 5638
URLACTION_HTML_SUBFRAME_NAVIGATE: UInt32 = 5639
URLACTION_HTML_META_REFRESH: UInt32 = 5640
URLACTION_HTML_MIXED_CONTENT: UInt32 = 5641
URLACTION_HTML_INCLUDE_FILE_PATH: UInt32 = 5642
URLACTION_HTML_ALLOW_INJECTED_DYNAMIC_HTML: UInt32 = 5643
URLACTION_HTML_REQUIRE_UTF8_DOCUMENT_CODEPAGE: UInt32 = 5644
URLACTION_HTML_ALLOW_CROSS_DOMAIN_CANVAS: UInt32 = 5645
URLACTION_HTML_ALLOW_WINDOW_CLOSE: UInt32 = 5646
URLACTION_HTML_ALLOW_CROSS_DOMAIN_WEBWORKER: UInt32 = 5647
URLACTION_HTML_ALLOW_CROSS_DOMAIN_TEXTTRACK: UInt32 = 5648
URLACTION_HTML_ALLOW_INDEXEDDB: UInt32 = 5649
URLACTION_HTML_MAX: UInt32 = 6143
URLACTION_SHELL_MIN: UInt32 = 6144
URLACTION_SHELL_INSTALL_DTITEMS: UInt32 = 6144
URLACTION_SHELL_MOVE_OR_COPY: UInt32 = 6146
URLACTION_SHELL_FILE_DOWNLOAD: UInt32 = 6147
URLACTION_SHELL_VERB: UInt32 = 6148
URLACTION_SHELL_WEBVIEW_VERB: UInt32 = 6149
URLACTION_SHELL_SHELLEXECUTE: UInt32 = 6150
URLACTION_SHELL_EXECUTE_HIGHRISK: UInt32 = 6150
URLACTION_SHELL_EXECUTE_MODRISK: UInt32 = 6151
URLACTION_SHELL_EXECUTE_LOWRISK: UInt32 = 6152
URLACTION_SHELL_POPUPMGR: UInt32 = 6153
URLACTION_SHELL_RTF_OBJECTS_LOAD: UInt32 = 6154
URLACTION_SHELL_ENHANCED_DRAGDROP_SECURITY: UInt32 = 6155
URLACTION_SHELL_EXTENSIONSECURITY: UInt32 = 6156
URLACTION_SHELL_SECURE_DRAGSOURCE: UInt32 = 6157
URLACTION_SHELL_REMOTEQUERY: UInt32 = 6158
URLACTION_SHELL_PREVIEW: UInt32 = 6159
URLACTION_SHELL_SHARE: UInt32 = 6160
URLACTION_SHELL_ALLOW_CROSS_SITE_SHARE: UInt32 = 6161
URLACTION_SHELL_TOCTOU_RISK: UInt32 = 6162
URLACTION_SHELL_CURR_MAX: UInt32 = 6162
URLACTION_SHELL_MAX: UInt32 = 6655
URLACTION_NETWORK_MIN: UInt32 = 6656
URLACTION_CREDENTIALS_USE: UInt32 = 6656
URLPOLICY_CREDENTIALS_SILENT_LOGON_OK: UInt32 = 0
URLPOLICY_CREDENTIALS_MUST_PROMPT_USER: UInt32 = 65536
URLPOLICY_CREDENTIALS_CONDITIONAL_PROMPT: UInt32 = 131072
URLPOLICY_CREDENTIALS_ANONYMOUS_ONLY: UInt32 = 196608
URLACTION_AUTHENTICATE_CLIENT: UInt32 = 6657
URLPOLICY_AUTHENTICATE_CLEARTEXT_OK: UInt32 = 0
URLPOLICY_AUTHENTICATE_CHALLENGE_RESPONSE: UInt32 = 65536
URLPOLICY_AUTHENTICATE_MUTUAL_ONLY: UInt32 = 196608
URLACTION_COOKIES: UInt32 = 6658
URLACTION_COOKIES_SESSION: UInt32 = 6659
URLACTION_CLIENT_CERT_PROMPT: UInt32 = 6660
URLACTION_COOKIES_THIRD_PARTY: UInt32 = 6661
URLACTION_COOKIES_SESSION_THIRD_PARTY: UInt32 = 6662
URLACTION_COOKIES_ENABLED: UInt32 = 6672
URLACTION_NETWORK_CURR_MAX: UInt32 = 6672
URLACTION_NETWORK_MAX: UInt32 = 7167
URLACTION_JAVA_MIN: UInt32 = 7168
URLACTION_JAVA_PERMISSIONS: UInt32 = 7168
URLPOLICY_JAVA_PROHIBIT: UInt32 = 0
URLPOLICY_JAVA_HIGH: UInt32 = 65536
URLPOLICY_JAVA_MEDIUM: UInt32 = 131072
URLPOLICY_JAVA_LOW: UInt32 = 196608
URLPOLICY_JAVA_CUSTOM: UInt32 = 8388608
URLACTION_JAVA_CURR_MAX: UInt32 = 7168
URLACTION_JAVA_MAX: UInt32 = 7423
URLACTION_INFODELIVERY_MIN: UInt32 = 7424
URLACTION_INFODELIVERY_NO_ADDING_CHANNELS: UInt32 = 7424
URLACTION_INFODELIVERY_NO_EDITING_CHANNELS: UInt32 = 7425
URLACTION_INFODELIVERY_NO_REMOVING_CHANNELS: UInt32 = 7426
URLACTION_INFODELIVERY_NO_ADDING_SUBSCRIPTIONS: UInt32 = 7427
URLACTION_INFODELIVERY_NO_EDITING_SUBSCRIPTIONS: UInt32 = 7428
URLACTION_INFODELIVERY_NO_REMOVING_SUBSCRIPTIONS: UInt32 = 7429
URLACTION_INFODELIVERY_NO_CHANNEL_LOGGING: UInt32 = 7430
URLACTION_INFODELIVERY_CURR_MAX: UInt32 = 7430
URLACTION_INFODELIVERY_MAX: UInt32 = 7679
URLACTION_CHANNEL_SOFTDIST_MIN: UInt32 = 7680
URLACTION_CHANNEL_SOFTDIST_PERMISSIONS: UInt32 = 7685
URLPOLICY_CHANNEL_SOFTDIST_PROHIBIT: UInt32 = 65536
URLPOLICY_CHANNEL_SOFTDIST_PRECACHE: UInt32 = 131072
URLPOLICY_CHANNEL_SOFTDIST_AUTOINSTALL: UInt32 = 196608
URLACTION_CHANNEL_SOFTDIST_MAX: UInt32 = 7935
URLACTION_DOTNET_USERCONTROLS: UInt32 = 8197
URLACTION_BEHAVIOR_MIN: UInt32 = 8192
URLACTION_BEHAVIOR_RUN: UInt32 = 8192
URLPOLICY_BEHAVIOR_CHECK_LIST: UInt32 = 65536
URLACTION_FEATURE_MIN: UInt32 = 8448
URLACTION_FEATURE_MIME_SNIFFING: UInt32 = 8448
URLACTION_FEATURE_ZONE_ELEVATION: UInt32 = 8449
URLACTION_FEATURE_WINDOW_RESTRICTIONS: UInt32 = 8450
URLACTION_FEATURE_SCRIPT_STATUS_BAR: UInt32 = 8451
URLACTION_FEATURE_FORCE_ADDR_AND_STATUS: UInt32 = 8452
URLACTION_FEATURE_BLOCK_INPUT_PROMPTS: UInt32 = 8453
URLACTION_FEATURE_DATA_BINDING: UInt32 = 8454
URLACTION_FEATURE_CROSSDOMAIN_FOCUS_CHANGE: UInt32 = 8455
URLACTION_AUTOMATIC_DOWNLOAD_UI_MIN: UInt32 = 8704
URLACTION_AUTOMATIC_DOWNLOAD_UI: UInt32 = 8704
URLACTION_AUTOMATIC_ACTIVEX_UI: UInt32 = 8705
URLACTION_ALLOW_RESTRICTEDPROTOCOLS: UInt32 = 8960
URLACTION_ALLOW_APEVALUATION: UInt32 = 8961
URLACTION_ALLOW_XHR_EVALUATION: UInt32 = 8962
URLACTION_WINDOWS_BROWSER_APPLICATIONS: UInt32 = 9216
URLACTION_XPS_DOCUMENTS: UInt32 = 9217
URLACTION_LOOSE_XAML: UInt32 = 9218
URLACTION_LOWRIGHTS: UInt32 = 9472
URLACTION_WINFX_SETUP: UInt32 = 9728
URLACTION_INPRIVATE_BLOCKING: UInt32 = 9984
URLACTION_ALLOW_AUDIO_VIDEO: UInt32 = 9985
URLACTION_ALLOW_ACTIVEX_FILTERING: UInt32 = 9986
URLACTION_ALLOW_STRUCTURED_STORAGE_SNIFFING: UInt32 = 9987
URLACTION_ALLOW_AUDIO_VIDEO_PLUGINS: UInt32 = 9988
URLACTION_ALLOW_ZONE_ELEVATION_VIA_OPT_OUT: UInt32 = 9989
URLACTION_ALLOW_ZONE_ELEVATION_OPT_OUT_ADDITION: UInt32 = 9990
URLACTION_ALLOW_CROSSDOMAIN_DROP_WITHIN_WINDOW: UInt32 = 9992
URLACTION_ALLOW_CROSSDOMAIN_DROP_ACROSS_WINDOWS: UInt32 = 9993
URLACTION_ALLOW_CROSSDOMAIN_APPCACHE_MANIFEST: UInt32 = 9994
URLACTION_ALLOW_RENDER_LEGACY_DXTFILTERS: UInt32 = 9995
URLACTION_ALLOW_ANTIMALWARE_SCANNING_OF_ACTIVEX: UInt32 = 9996
URLACTION_ALLOW_CSS_EXPRESSIONS: UInt32 = 9997
URLPOLICY_ALLOW: UInt32 = 0
URLPOLICY_QUERY: UInt32 = 1
URLPOLICY_DISALLOW: UInt32 = 3
URLPOLICY_NOTIFY_ON_ALLOW: UInt32 = 16
URLPOLICY_NOTIFY_ON_DISALLOW: UInt32 = 32
URLPOLICY_LOG_ON_ALLOW: UInt32 = 64
URLPOLICY_LOG_ON_DISALLOW: UInt32 = 128
URLPOLICY_MASK_PERMISSIONS: UInt32 = 15
URLPOLICY_DONTCHECKDLGBOX: UInt32 = 256
URLZONE_ESC_FLAG: UInt32 = 256
SECURITY_IE_STATE_GREEN: UInt32 = 0
SECURITY_IE_STATE_RED: UInt32 = 1
SOFTDIST_FLAG_USAGE_EMAIL: UInt32 = 1
SOFTDIST_FLAG_USAGE_PRECACHE: UInt32 = 2
SOFTDIST_FLAG_USAGE_AUTOINSTALL: UInt32 = 4
SOFTDIST_FLAG_DELETE_SUBSCRIPTION: UInt32 = 8
SOFTDIST_ADSTATE_NONE: UInt32 = 0
SOFTDIST_ADSTATE_AVAILABLE: UInt32 = 1
SOFTDIST_ADSTATE_DOWNLOADED: UInt32 = 2
SOFTDIST_ADSTATE_INSTALLED: UInt32 = 3
CONFIRMSAFETYACTION_LOADOBJECT: UInt32 = 1
@winfunctype('urlmon.dll')
def CreateURLMoniker(pMkCtx: win32more.Windows.Win32.System.Com.IMoniker, szURL: win32more.Windows.Win32.Foundation.PWSTR, ppmk: POINTER(win32more.Windows.Win32.System.Com.IMoniker)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CreateURLMonikerEx(pMkCtx: win32more.Windows.Win32.System.Com.IMoniker, szURL: win32more.Windows.Win32.Foundation.PWSTR, ppmk: POINTER(win32more.Windows.Win32.System.Com.IMoniker), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def GetClassURL(szURL: win32more.Windows.Win32.Foundation.PWSTR, pClsID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CreateAsyncBindCtx(reserved: UInt32, pBSCb: win32more.Windows.Win32.System.Com.IBindStatusCallback, pEFetc: win32more.Windows.Win32.System.Com.IEnumFORMATETC, ppBC: POINTER(win32more.Windows.Win32.System.Com.IBindCtx)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CreateURLMonikerEx2(pMkCtx: win32more.Windows.Win32.System.Com.IMoniker, pUri: win32more.Windows.Win32.System.Com.IUri, ppmk: POINTER(win32more.Windows.Win32.System.Com.IMoniker), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CreateAsyncBindCtxEx(pbc: win32more.Windows.Win32.System.Com.IBindCtx, dwOptions: UInt32, pBSCb: win32more.Windows.Win32.System.Com.IBindStatusCallback, pEnum: win32more.Windows.Win32.System.Com.IEnumFORMATETC, ppBC: POINTER(win32more.Windows.Win32.System.Com.IBindCtx), reserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def MkParseDisplayNameEx(pbc: win32more.Windows.Win32.System.Com.IBindCtx, szDisplayName: win32more.Windows.Win32.Foundation.PWSTR, pchEaten: POINTER(UInt32), ppmk: POINTER(win32more.Windows.Win32.System.Com.IMoniker)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def RegisterBindStatusCallback(pBC: win32more.Windows.Win32.System.Com.IBindCtx, pBSCb: win32more.Windows.Win32.System.Com.IBindStatusCallback, ppBSCBPrev: POINTER(win32more.Windows.Win32.System.Com.IBindStatusCallback), dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def RevokeBindStatusCallback(pBC: win32more.Windows.Win32.System.Com.IBindCtx, pBSCb: win32more.Windows.Win32.System.Com.IBindStatusCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def GetClassFileOrMime(pBC: win32more.Windows.Win32.System.Com.IBindCtx, szFilename: win32more.Windows.Win32.Foundation.PWSTR, pBuffer: VoidPtr, cbSize: UInt32, szMime: win32more.Windows.Win32.Foundation.PWSTR, dwReserved: UInt32, pclsid: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def IsValidURL(pBC: win32more.Windows.Win32.System.Com.IBindCtx, szURL: win32more.Windows.Win32.Foundation.PWSTR, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoGetClassObjectFromURL(rCLASSID: POINTER(Guid), szCODE: win32more.Windows.Win32.Foundation.PWSTR, dwFileVersionMS: UInt32, dwFileVersionLS: UInt32, szTYPE: win32more.Windows.Win32.Foundation.PWSTR, pBindCtx: win32more.Windows.Win32.System.Com.IBindCtx, dwClsContext: win32more.Windows.Win32.System.Com.CLSCTX, pvReserved: VoidPtr, riid: POINTER(Guid), ppv: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def IEInstallScope(pdwScope: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def FaultInIEFeature(hWnd: win32more.Windows.Win32.Foundation.HWND, pClassSpec: POINTER(win32more.Windows.Win32.System.Com.uCLSSPEC), pQuery: POINTER(win32more.Windows.Win32.System.Com.QUERYCONTEXT), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def GetComponentIDFromCLSSPEC(pClassspec: POINTER(win32more.Windows.Win32.System.Com.uCLSSPEC), ppszComponentID: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def IsAsyncMoniker(pmk: win32more.Windows.Win32.System.Com.IMoniker) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def RegisterMediaTypes(ctypes: UInt32, rgszTypes: POINTER(win32more.Windows.Win32.Foundation.PSTR), rgcfTypes: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def FindMediaType(rgszTypes: win32more.Windows.Win32.Foundation.PSTR, rgcfTypes: POINTER(UInt16)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CreateFormatEnumerator(cfmtetc: UInt32, rgfmtetc: POINTER(win32more.Windows.Win32.System.Com.FORMATETC), ppenumfmtetc: POINTER(win32more.Windows.Win32.System.Com.IEnumFORMATETC)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def RegisterFormatEnumerator(pBC: win32more.Windows.Win32.System.Com.IBindCtx, pEFetc: win32more.Windows.Win32.System.Com.IEnumFORMATETC, reserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def RevokeFormatEnumerator(pBC: win32more.Windows.Win32.System.Com.IBindCtx, pEFetc: win32more.Windows.Win32.System.Com.IEnumFORMATETC) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def RegisterMediaTypeClass(pBC: win32more.Windows.Win32.System.Com.IBindCtx, ctypes: UInt32, rgszTypes: POINTER(win32more.Windows.Win32.Foundation.PSTR), rgclsID: POINTER(Guid), reserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def FindMediaTypeClass(pBC: win32more.Windows.Win32.System.Com.IBindCtx, szType: win32more.Windows.Win32.Foundation.PSTR, pclsID: POINTER(Guid), reserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def UrlMkSetSessionOption(dwOption: UInt32, pBuffer: VoidPtr, dwBufferLength: UInt32, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def UrlMkGetSessionOption(dwOption: UInt32, pBuffer: VoidPtr, dwBufferLength: UInt32, pdwBufferLengthOut: POINTER(UInt32), dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def FindMimeFromData(pBC: win32more.Windows.Win32.System.Com.IBindCtx, pwzUrl: win32more.Windows.Win32.Foundation.PWSTR, pBuffer: VoidPtr, cbSize: UInt32, pwzMimeProposed: win32more.Windows.Win32.Foundation.PWSTR, dwMimeFlags: UInt32, ppwzMimeOut: POINTER(win32more.Windows.Win32.Foundation.PWSTR), dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def ObtainUserAgentString(dwOption: UInt32, pszUAOut: win32more.Windows.Win32.Foundation.PSTR, cbSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CompareSecurityIds(pbSecurityId1: POINTER(Byte), dwLen1: UInt32, pbSecurityId2: POINTER(Byte), dwLen2: UInt32, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CompatFlagsFromClsid(pclsid: POINTER(Guid), pdwCompatFlags: POINTER(UInt32), pdwMiscStatusFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def SetAccessForIEAppContainer(hObject: win32more.Windows.Win32.Foundation.HANDLE, ieObjectType: win32more.Windows.Win32.System.Com.Urlmon.IEObjectType, dwAccessMask: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def HlinkSimpleNavigateToString(szTarget: win32more.Windows.Win32.Foundation.PWSTR, szLocation: win32more.Windows.Win32.Foundation.PWSTR, szTargetFrameName: win32more.Windows.Win32.Foundation.PWSTR, pUnk: win32more.Windows.Win32.System.Com.IUnknown, pbc: win32more.Windows.Win32.System.Com.IBindCtx, param5: win32more.Windows.Win32.System.Com.IBindStatusCallback, grfHLNF: UInt32, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def HlinkSimpleNavigateToMoniker(pmkTarget: win32more.Windows.Win32.System.Com.IMoniker, szLocation: win32more.Windows.Win32.Foundation.PWSTR, szTargetFrameName: win32more.Windows.Win32.Foundation.PWSTR, pUnk: win32more.Windows.Win32.System.Com.IUnknown, pbc: win32more.Windows.Win32.System.Com.IBindCtx, param5: win32more.Windows.Win32.System.Com.IBindStatusCallback, grfHLNF: UInt32, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def URLOpenStreamA(param0: win32more.Windows.Win32.System.Com.IUnknown, param1: win32more.Windows.Win32.Foundation.PSTR, param2: UInt32, param3: win32more.Windows.Win32.System.Com.IBindStatusCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def URLOpenStreamW(param0: win32more.Windows.Win32.System.Com.IUnknown, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: UInt32, param3: win32more.Windows.Win32.System.Com.IBindStatusCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
URLOpenStream = UnicodeAlias('URLOpenStreamW')
@winfunctype('urlmon.dll')
def URLOpenPullStreamA(param0: win32more.Windows.Win32.System.Com.IUnknown, param1: win32more.Windows.Win32.Foundation.PSTR, param2: UInt32, param3: win32more.Windows.Win32.System.Com.IBindStatusCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def URLOpenPullStreamW(param0: win32more.Windows.Win32.System.Com.IUnknown, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: UInt32, param3: win32more.Windows.Win32.System.Com.IBindStatusCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
URLOpenPullStream = UnicodeAlias('URLOpenPullStreamW')
@winfunctype('urlmon.dll')
def URLDownloadToFileA(param0: win32more.Windows.Win32.System.Com.IUnknown, param1: win32more.Windows.Win32.Foundation.PSTR, param2: win32more.Windows.Win32.Foundation.PSTR, param3: UInt32, param4: win32more.Windows.Win32.System.Com.IBindStatusCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def URLDownloadToFileW(param0: win32more.Windows.Win32.System.Com.IUnknown, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: win32more.Windows.Win32.Foundation.PWSTR, param3: UInt32, param4: win32more.Windows.Win32.System.Com.IBindStatusCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
URLDownloadToFile = UnicodeAlias('URLDownloadToFileW')
@winfunctype('urlmon.dll')
def URLDownloadToCacheFileA(param0: win32more.Windows.Win32.System.Com.IUnknown, param1: win32more.Windows.Win32.Foundation.PSTR, param2: win32more.Windows.Win32.Foundation.PSTR, cchFileName: UInt32, param4: UInt32, param5: win32more.Windows.Win32.System.Com.IBindStatusCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def URLDownloadToCacheFileW(param0: win32more.Windows.Win32.System.Com.IUnknown, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: win32more.Windows.Win32.Foundation.PWSTR, cchFileName: UInt32, param4: UInt32, param5: win32more.Windows.Win32.System.Com.IBindStatusCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
URLDownloadToCacheFile = UnicodeAlias('URLDownloadToCacheFileW')
@winfunctype('urlmon.dll')
def URLOpenBlockingStreamA(param0: win32more.Windows.Win32.System.Com.IUnknown, param1: win32more.Windows.Win32.Foundation.PSTR, param2: POINTER(win32more.Windows.Win32.System.Com.IStream), param3: UInt32, param4: win32more.Windows.Win32.System.Com.IBindStatusCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def URLOpenBlockingStreamW(param0: win32more.Windows.Win32.System.Com.IUnknown, param1: win32more.Windows.Win32.Foundation.PWSTR, param2: POINTER(win32more.Windows.Win32.System.Com.IStream), param3: UInt32, param4: win32more.Windows.Win32.System.Com.IBindStatusCallback) -> win32more.Windows.Win32.Foundation.HRESULT: ...
URLOpenBlockingStream = UnicodeAlias('URLOpenBlockingStreamW')
@winfunctype('urlmon.dll')
def HlinkGoBack(pUnk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def HlinkGoForward(pUnk: win32more.Windows.Win32.System.Com.IUnknown) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def HlinkNavigateString(pUnk: win32more.Windows.Win32.System.Com.IUnknown, szTarget: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def HlinkNavigateMoniker(pUnk: win32more.Windows.Win32.System.Com.IUnknown, pmkTarget: win32more.Windows.Win32.System.Com.IMoniker) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetParseUrl(pwzUrl: win32more.Windows.Win32.Foundation.PWSTR, ParseAction: win32more.Windows.Win32.System.Com.Urlmon.PARSEACTION, dwFlags: UInt32, pszResult: win32more.Windows.Win32.Foundation.PWSTR, cchResult: UInt32, pcchResult: POINTER(UInt32), dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetParseIUri(pIUri: win32more.Windows.Win32.System.Com.IUri, ParseAction: win32more.Windows.Win32.System.Com.Urlmon.PARSEACTION, dwFlags: UInt32, pwzResult: win32more.Windows.Win32.Foundation.PWSTR, cchResult: UInt32, pcchResult: POINTER(UInt32), dwReserved: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetCombineUrl(pwzBaseUrl: win32more.Windows.Win32.Foundation.PWSTR, pwzRelativeUrl: win32more.Windows.Win32.Foundation.PWSTR, dwCombineFlags: UInt32, pszResult: win32more.Windows.Win32.Foundation.PWSTR, cchResult: UInt32, pcchResult: POINTER(UInt32), dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetCombineUrlEx(pBaseUri: win32more.Windows.Win32.System.Com.IUri, pwzRelativeUrl: win32more.Windows.Win32.Foundation.PWSTR, dwCombineFlags: UInt32, ppCombinedUri: POINTER(win32more.Windows.Win32.System.Com.IUri), dwReserved: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetCombineIUri(pBaseUri: win32more.Windows.Win32.System.Com.IUri, pRelativeUri: win32more.Windows.Win32.System.Com.IUri, dwCombineFlags: UInt32, ppCombinedUri: POINTER(win32more.Windows.Win32.System.Com.IUri), dwReserved: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetCompareUrl(pwzUrl1: win32more.Windows.Win32.Foundation.PWSTR, pwzUrl2: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetGetProtocolFlags(pwzUrl: win32more.Windows.Win32.Foundation.PWSTR, pdwFlags: POINTER(UInt32), dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetQueryInfo(pwzUrl: win32more.Windows.Win32.Foundation.PWSTR, QueryOptions: win32more.Windows.Win32.System.Com.Urlmon.QUERYOPTION, dwQueryFlags: UInt32, pvBuffer: VoidPtr, cbBuffer: UInt32, pcbBuffer: POINTER(UInt32), dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetGetSession(dwSessionMode: UInt32, ppIInternetSession: POINTER(win32more.Windows.Win32.System.Com.Urlmon.IInternetSession), dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetGetSecurityUrl(pwszUrl: win32more.Windows.Win32.Foundation.PWSTR, ppwszSecUrl: POINTER(win32more.Windows.Win32.Foundation.PWSTR), psuAction: win32more.Windows.Win32.System.Com.Urlmon.PSUACTION, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetGetSecurityUrlEx(pUri: win32more.Windows.Win32.System.Com.IUri, ppSecUri: POINTER(win32more.Windows.Win32.System.Com.IUri), psuAction: win32more.Windows.Win32.System.Com.Urlmon.PSUACTION, dwReserved: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetSetFeatureEnabled(FeatureEntry: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST, dwFlags: UInt32, fEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetIsFeatureEnabled(FeatureEntry: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetIsFeatureEnabledForUrl(FeatureEntry: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST, dwFlags: UInt32, szURL: win32more.Windows.Win32.Foundation.PWSTR, pSecMgr: win32more.Windows.Win32.System.Com.Urlmon.IInternetSecurityManager) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetIsFeatureEnabledForIUri(FeatureEntry: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST, dwFlags: UInt32, pIUri: win32more.Windows.Win32.System.Com.IUri, pSecMgr: win32more.Windows.Win32.System.Com.Urlmon.IInternetSecurityManagerEx2) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetIsFeatureZoneElevationEnabled(szFromURL: win32more.Windows.Win32.Foundation.PWSTR, szToURL: win32more.Windows.Win32.Foundation.PWSTR, pSecMgr: win32more.Windows.Win32.System.Com.Urlmon.IInternetSecurityManager, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CopyStgMedium(pcstgmedSrc: POINTER(win32more.Windows.Win32.System.Com.STGMEDIUM), pstgmedDest: POINTER(win32more.Windows.Win32.System.Com.STGMEDIUM)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CopyBindInfo(pcbiSrc: POINTER(win32more.Windows.Win32.System.Com.BINDINFO), pbiDest: POINTER(win32more.Windows.Win32.System.Com.BINDINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def ReleaseBindInfo(pbindinfo: POINTER(win32more.Windows.Win32.System.Com.BINDINFO)) -> Void: ...
@winfunctype('urlmon.dll')
def IEGetUserPrivateNamespaceName() -> win32more.Windows.Win32.Foundation.PWSTR: ...
@winfunctype('urlmon.dll')
def CoInternetCreateSecurityManager(pSP: win32more.Windows.Win32.System.Com.IServiceProvider, ppSM: POINTER(win32more.Windows.Win32.System.Com.Urlmon.IInternetSecurityManager), dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetCreateZoneManager(pSP: win32more.Windows.Win32.System.Com.IServiceProvider, ppZM: POINTER(win32more.Windows.Win32.System.Com.Urlmon.IInternetZoneManager), dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def GetSoftwareUpdateInfo(szDistUnit: win32more.Windows.Win32.Foundation.PWSTR, psdi: POINTER(win32more.Windows.Win32.System.Com.Urlmon.SOFTDISTINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def SetSoftwareUpdateAdvertisementState(szDistUnit: win32more.Windows.Win32.Foundation.PWSTR, dwAdState: UInt32, dwAdvertisedVersionMS: UInt32, dwAdvertisedVersionLS: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def IsLoggingEnabledA(pszUrl: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('urlmon.dll')
def IsLoggingEnabledW(pwszUrl: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
IsLoggingEnabled = UnicodeAlias('IsLoggingEnabledW')
@winfunctype('urlmon.dll')
def WriteHitLogging(lpLogginginfo: POINTER(win32more.Windows.Win32.System.Com.Urlmon.HIT_LOGGING_INFO)) -> win32more.Windows.Win32.Foundation.BOOL: ...
BINDF = Int32
BINDF_ASYNCHRONOUS: win32more.Windows.Win32.System.Com.Urlmon.BINDF = 1
BINDF_ASYNCSTORAGE: win32more.Windows.Win32.System.Com.Urlmon.BINDF = 2
BINDF_NOPROGRESSIVERENDERING: win32more.Windows.Win32.System.Com.Urlmon.BINDF = 4
BINDF_OFFLINEOPERATION: win32more.Windows.Win32.System.Com.Urlmon.BINDF = 8
BINDF_GETNEWESTVERSION: win32more.Windows.Win32.System.Com.Urlmon.BINDF = 16
BINDF_NOWRITECACHE: win32more.Windows.Win32.System.Com.Urlmon.BINDF = 32
BINDF_NEEDFILE: win32more.Windows.Win32.System.Com.Urlmon.BINDF = 64
BINDF_PULLDATA: win32more.Windows.Win32.System.Com.Urlmon.BINDF = 128
BINDF_IGNORESECURITYPROBLEM: win32more.Windows.Win32.System.Com.Urlmon.BINDF = 256
BINDF_RESYNCHRONIZE: win32more.Windows.Win32.System.Com.Urlmon.BINDF = 512
BINDF_HYPERLINK: win32more.Windows.Win32.System.Com.Urlmon.BINDF = 1024
BINDF_NO_UI: win32more.Windows.Win32.System.Com.Urlmon.BINDF = 2048
BINDF_SILENTOPERATION: win32more.Windows.Win32.System.Com.Urlmon.BINDF = 4096
BINDF_PRAGMA_NO_CACHE: win32more.Windows.Win32.System.Com.Urlmon.BINDF = 8192
BINDF_GETCLASSOBJECT: win32more.Windows.Win32.System.Com.Urlmon.BINDF = 16384
BINDF_RESERVED_1: win32more.Windows.Win32.System.Com.Urlmon.BINDF = 32768
BINDF_FREE_THREADED: win32more.Windows.Win32.System.Com.Urlmon.BINDF = 65536
BINDF_DIRECT_READ: win32more.Windows.Win32.System.Com.Urlmon.BINDF = 131072
BINDF_FORMS_SUBMIT: win32more.Windows.Win32.System.Com.Urlmon.BINDF = 262144
BINDF_GETFROMCACHE_IF_NET_FAIL: win32more.Windows.Win32.System.Com.Urlmon.BINDF = 524288
BINDF_FROMURLMON: win32more.Windows.Win32.System.Com.Urlmon.BINDF = 1048576
BINDF_FWD_BACK: win32more.Windows.Win32.System.Com.Urlmon.BINDF = 2097152
BINDF_PREFERDEFAULTHANDLER: win32more.Windows.Win32.System.Com.Urlmon.BINDF = 4194304
BINDF_ENFORCERESTRICTED: win32more.Windows.Win32.System.Com.Urlmon.BINDF = 8388608
BINDF_RESERVED_2: win32more.Windows.Win32.System.Com.Urlmon.BINDF = -2147483648
BINDF_RESERVED_3: win32more.Windows.Win32.System.Com.Urlmon.BINDF = 16777216
BINDF_RESERVED_4: win32more.Windows.Win32.System.Com.Urlmon.BINDF = 33554432
BINDF_RESERVED_5: win32more.Windows.Win32.System.Com.Urlmon.BINDF = 67108864
BINDF_RESERVED_6: win32more.Windows.Win32.System.Com.Urlmon.BINDF = 134217728
BINDF_RESERVED_7: win32more.Windows.Win32.System.Com.Urlmon.BINDF = 1073741824
BINDF_RESERVED_8: win32more.Windows.Win32.System.Com.Urlmon.BINDF = 536870912
BINDF2 = Int32
BINDF2_DISABLEBASICOVERHTTP: win32more.Windows.Win32.System.Com.Urlmon.BINDF2 = 1
BINDF2_DISABLEAUTOCOOKIEHANDLING: win32more.Windows.Win32.System.Com.Urlmon.BINDF2 = 2
BINDF2_READ_DATA_GREATER_THAN_4GB: win32more.Windows.Win32.System.Com.Urlmon.BINDF2 = 4
BINDF2_DISABLE_HTTP_REDIRECT_XSECURITYID: win32more.Windows.Win32.System.Com.Urlmon.BINDF2 = 8
BINDF2_SETDOWNLOADMODE: win32more.Windows.Win32.System.Com.Urlmon.BINDF2 = 32
BINDF2_DISABLE_HTTP_REDIRECT_CACHING: win32more.Windows.Win32.System.Com.Urlmon.BINDF2 = 64
BINDF2_KEEP_CALLBACK_MODULE_LOADED: win32more.Windows.Win32.System.Com.Urlmon.BINDF2 = 128
BINDF2_ALLOW_PROXY_CRED_PROMPT: win32more.Windows.Win32.System.Com.Urlmon.BINDF2 = 256
BINDF2_RESERVED_17: win32more.Windows.Win32.System.Com.Urlmon.BINDF2 = 512
BINDF2_RESERVED_16: win32more.Windows.Win32.System.Com.Urlmon.BINDF2 = 1024
BINDF2_RESERVED_15: win32more.Windows.Win32.System.Com.Urlmon.BINDF2 = 2048
BINDF2_RESERVED_14: win32more.Windows.Win32.System.Com.Urlmon.BINDF2 = 4096
BINDF2_RESERVED_13: win32more.Windows.Win32.System.Com.Urlmon.BINDF2 = 8192
BINDF2_RESERVED_12: win32more.Windows.Win32.System.Com.Urlmon.BINDF2 = 16384
BINDF2_RESERVED_11: win32more.Windows.Win32.System.Com.Urlmon.BINDF2 = 32768
BINDF2_RESERVED_10: win32more.Windows.Win32.System.Com.Urlmon.BINDF2 = 65536
BINDF2_RESERVED_F: win32more.Windows.Win32.System.Com.Urlmon.BINDF2 = 131072
BINDF2_RESERVED_E: win32more.Windows.Win32.System.Com.Urlmon.BINDF2 = 262144
BINDF2_RESERVED_D: win32more.Windows.Win32.System.Com.Urlmon.BINDF2 = 524288
BINDF2_RESERVED_C: win32more.Windows.Win32.System.Com.Urlmon.BINDF2 = 1048576
BINDF2_RESERVED_B: win32more.Windows.Win32.System.Com.Urlmon.BINDF2 = 2097152
BINDF2_RESERVED_A: win32more.Windows.Win32.System.Com.Urlmon.BINDF2 = 4194304
BINDF2_RESERVED_9: win32more.Windows.Win32.System.Com.Urlmon.BINDF2 = 8388608
BINDF2_RESERVED_8: win32more.Windows.Win32.System.Com.Urlmon.BINDF2 = 16777216
BINDF2_RESERVED_7: win32more.Windows.Win32.System.Com.Urlmon.BINDF2 = 33554432
BINDF2_RESERVED_6: win32more.Windows.Win32.System.Com.Urlmon.BINDF2 = 67108864
BINDF2_RESERVED_5: win32more.Windows.Win32.System.Com.Urlmon.BINDF2 = 134217728
BINDF2_RESERVED_4: win32more.Windows.Win32.System.Com.Urlmon.BINDF2 = 268435456
BINDF2_RESERVED_3: win32more.Windows.Win32.System.Com.Urlmon.BINDF2 = 536870912
BINDF2_RESERVED_2: win32more.Windows.Win32.System.Com.Urlmon.BINDF2 = 1073741824
BINDF2_RESERVED_1: win32more.Windows.Win32.System.Com.Urlmon.BINDF2 = -2147483648
BINDHANDLETYPES = Int32
BINDHANDLETYPES_APPCACHE: win32more.Windows.Win32.System.Com.Urlmon.BINDHANDLETYPES = 0
BINDHANDLETYPES_DEPENDENCY: win32more.Windows.Win32.System.Com.Urlmon.BINDHANDLETYPES = 1
BINDHANDLETYPES_COUNT: win32more.Windows.Win32.System.Com.Urlmon.BINDHANDLETYPES = 2
BINDINFO_OPTIONS = Int32
BINDINFO_OPTIONS_WININETFLAG: win32more.Windows.Win32.System.Com.Urlmon.BINDINFO_OPTIONS = 65536
BINDINFO_OPTIONS_ENABLE_UTF8: win32more.Windows.Win32.System.Com.Urlmon.BINDINFO_OPTIONS = 131072
BINDINFO_OPTIONS_DISABLE_UTF8: win32more.Windows.Win32.System.Com.Urlmon.BINDINFO_OPTIONS = 262144
BINDINFO_OPTIONS_USE_IE_ENCODING: win32more.Windows.Win32.System.Com.Urlmon.BINDINFO_OPTIONS = 524288
BINDINFO_OPTIONS_BINDTOOBJECT: win32more.Windows.Win32.System.Com.Urlmon.BINDINFO_OPTIONS = 1048576
BINDINFO_OPTIONS_SECURITYOPTOUT: win32more.Windows.Win32.System.Com.Urlmon.BINDINFO_OPTIONS = 2097152
BINDINFO_OPTIONS_IGNOREMIMETEXTPLAIN: win32more.Windows.Win32.System.Com.Urlmon.BINDINFO_OPTIONS = 4194304
BINDINFO_OPTIONS_USEBINDSTRINGCREDS: win32more.Windows.Win32.System.Com.Urlmon.BINDINFO_OPTIONS = 8388608
BINDINFO_OPTIONS_IGNOREHTTPHTTPSREDIRECTS: win32more.Windows.Win32.System.Com.Urlmon.BINDINFO_OPTIONS = 16777216
BINDINFO_OPTIONS_IGNORE_SSLERRORS_ONCE: win32more.Windows.Win32.System.Com.Urlmon.BINDINFO_OPTIONS = 33554432
BINDINFO_WPC_DOWNLOADBLOCKED: win32more.Windows.Win32.System.Com.Urlmon.BINDINFO_OPTIONS = 134217728
BINDINFO_WPC_LOGGING_ENABLED: win32more.Windows.Win32.System.Com.Urlmon.BINDINFO_OPTIONS = 268435456
BINDINFO_OPTIONS_ALLOWCONNECTDATA: win32more.Windows.Win32.System.Com.Urlmon.BINDINFO_OPTIONS = 536870912
BINDINFO_OPTIONS_DISABLEAUTOREDIRECTS: win32more.Windows.Win32.System.Com.Urlmon.BINDINFO_OPTIONS = 1073741824
BINDINFO_OPTIONS_SHDOCVW_NAVIGATE: win32more.Windows.Win32.System.Com.Urlmon.BINDINFO_OPTIONS = -2147483648
BINDSTATUS = Int32
BINDSTATUS_FINDINGRESOURCE: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 1
BINDSTATUS_CONNECTING: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 2
BINDSTATUS_REDIRECTING: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 3
BINDSTATUS_BEGINDOWNLOADDATA: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 4
BINDSTATUS_DOWNLOADINGDATA: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 5
BINDSTATUS_ENDDOWNLOADDATA: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 6
BINDSTATUS_BEGINDOWNLOADCOMPONENTS: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 7
BINDSTATUS_INSTALLINGCOMPONENTS: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 8
BINDSTATUS_ENDDOWNLOADCOMPONENTS: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 9
BINDSTATUS_USINGCACHEDCOPY: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 10
BINDSTATUS_SENDINGREQUEST: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 11
BINDSTATUS_CLASSIDAVAILABLE: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 12
BINDSTATUS_MIMETYPEAVAILABLE: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 13
BINDSTATUS_CACHEFILENAMEAVAILABLE: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 14
BINDSTATUS_BEGINSYNCOPERATION: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 15
BINDSTATUS_ENDSYNCOPERATION: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 16
BINDSTATUS_BEGINUPLOADDATA: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 17
BINDSTATUS_UPLOADINGDATA: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 18
BINDSTATUS_ENDUPLOADDATA: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 19
BINDSTATUS_PROTOCOLCLASSID: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 20
BINDSTATUS_ENCODING: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 21
BINDSTATUS_VERIFIEDMIMETYPEAVAILABLE: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 22
BINDSTATUS_CLASSINSTALLLOCATION: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 23
BINDSTATUS_DECODING: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 24
BINDSTATUS_LOADINGMIMEHANDLER: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 25
BINDSTATUS_CONTENTDISPOSITIONATTACH: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 26
BINDSTATUS_FILTERREPORTMIMETYPE: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 27
BINDSTATUS_CLSIDCANINSTANTIATE: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 28
BINDSTATUS_IUNKNOWNAVAILABLE: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 29
BINDSTATUS_DIRECTBIND: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 30
BINDSTATUS_RAWMIMETYPE: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 31
BINDSTATUS_PROXYDETECTING: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 32
BINDSTATUS_ACCEPTRANGES: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 33
BINDSTATUS_COOKIE_SENT: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 34
BINDSTATUS_COMPACT_POLICY_RECEIVED: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 35
BINDSTATUS_COOKIE_SUPPRESSED: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 36
BINDSTATUS_COOKIE_STATE_UNKNOWN: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 37
BINDSTATUS_COOKIE_STATE_ACCEPT: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 38
BINDSTATUS_COOKIE_STATE_REJECT: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 39
BINDSTATUS_COOKIE_STATE_PROMPT: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 40
BINDSTATUS_COOKIE_STATE_LEASH: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 41
BINDSTATUS_COOKIE_STATE_DOWNGRADE: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 42
BINDSTATUS_POLICY_HREF: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 43
BINDSTATUS_P3P_HEADER: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 44
BINDSTATUS_SESSION_COOKIE_RECEIVED: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 45
BINDSTATUS_PERSISTENT_COOKIE_RECEIVED: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 46
BINDSTATUS_SESSION_COOKIES_ALLOWED: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 47
BINDSTATUS_CACHECONTROL: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 48
BINDSTATUS_CONTENTDISPOSITIONFILENAME: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 49
BINDSTATUS_MIMETEXTPLAINMISMATCH: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 50
BINDSTATUS_PUBLISHERAVAILABLE: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 51
BINDSTATUS_DISPLAYNAMEAVAILABLE: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 52
BINDSTATUS_SSLUX_NAVBLOCKED: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 53
BINDSTATUS_SERVER_MIMETYPEAVAILABLE: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 54
BINDSTATUS_SNIFFED_CLASSIDAVAILABLE: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 55
BINDSTATUS_64BIT_PROGRESS: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 56
BINDSTATUS_LAST: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 56
BINDSTATUS_RESERVED_0: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 57
BINDSTATUS_RESERVED_1: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 58
BINDSTATUS_RESERVED_2: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 59
BINDSTATUS_RESERVED_3: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 60
BINDSTATUS_RESERVED_4: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 61
BINDSTATUS_RESERVED_5: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 62
BINDSTATUS_RESERVED_6: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 63
BINDSTATUS_RESERVED_7: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 64
BINDSTATUS_RESERVED_8: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 65
BINDSTATUS_RESERVED_9: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 66
BINDSTATUS_RESERVED_A: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 67
BINDSTATUS_RESERVED_B: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 68
BINDSTATUS_RESERVED_C: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 69
BINDSTATUS_RESERVED_D: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 70
BINDSTATUS_RESERVED_E: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 71
BINDSTATUS_RESERVED_F: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 72
BINDSTATUS_RESERVED_10: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 73
BINDSTATUS_RESERVED_11: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 74
BINDSTATUS_RESERVED_12: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 75
BINDSTATUS_RESERVED_13: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 76
BINDSTATUS_RESERVED_14: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 77
BINDSTATUS_LAST_PRIVATE: win32more.Windows.Win32.System.Com.Urlmon.BINDSTATUS = 77
BINDSTRING = Int32
BINDSTRING_HEADERS: win32more.Windows.Win32.System.Com.Urlmon.BINDSTRING = 1
BINDSTRING_ACCEPT_MIMES: win32more.Windows.Win32.System.Com.Urlmon.BINDSTRING = 2
BINDSTRING_EXTRA_URL: win32more.Windows.Win32.System.Com.Urlmon.BINDSTRING = 3
BINDSTRING_LANGUAGE: win32more.Windows.Win32.System.Com.Urlmon.BINDSTRING = 4
BINDSTRING_USERNAME: win32more.Windows.Win32.System.Com.Urlmon.BINDSTRING = 5
BINDSTRING_PASSWORD: win32more.Windows.Win32.System.Com.Urlmon.BINDSTRING = 6
BINDSTRING_UA_PIXELS: win32more.Windows.Win32.System.Com.Urlmon.BINDSTRING = 7
BINDSTRING_UA_COLOR: win32more.Windows.Win32.System.Com.Urlmon.BINDSTRING = 8
BINDSTRING_OS: win32more.Windows.Win32.System.Com.Urlmon.BINDSTRING = 9
BINDSTRING_USER_AGENT: win32more.Windows.Win32.System.Com.Urlmon.BINDSTRING = 10
BINDSTRING_ACCEPT_ENCODINGS: win32more.Windows.Win32.System.Com.Urlmon.BINDSTRING = 11
BINDSTRING_POST_COOKIE: win32more.Windows.Win32.System.Com.Urlmon.BINDSTRING = 12
BINDSTRING_POST_DATA_MIME: win32more.Windows.Win32.System.Com.Urlmon.BINDSTRING = 13
BINDSTRING_URL: win32more.Windows.Win32.System.Com.Urlmon.BINDSTRING = 14
BINDSTRING_IID: win32more.Windows.Win32.System.Com.Urlmon.BINDSTRING = 15
BINDSTRING_FLAG_BIND_TO_OBJECT: win32more.Windows.Win32.System.Com.Urlmon.BINDSTRING = 16
BINDSTRING_PTR_BIND_CONTEXT: win32more.Windows.Win32.System.Com.Urlmon.BINDSTRING = 17
BINDSTRING_XDR_ORIGIN: win32more.Windows.Win32.System.Com.Urlmon.BINDSTRING = 18
BINDSTRING_DOWNLOADPATH: win32more.Windows.Win32.System.Com.Urlmon.BINDSTRING = 19
BINDSTRING_ROOTDOC_URL: win32more.Windows.Win32.System.Com.Urlmon.BINDSTRING = 20
BINDSTRING_INITIAL_FILENAME: win32more.Windows.Win32.System.Com.Urlmon.BINDSTRING = 21
BINDSTRING_PROXY_USERNAME: win32more.Windows.Win32.System.Com.Urlmon.BINDSTRING = 22
BINDSTRING_PROXY_PASSWORD: win32more.Windows.Win32.System.Com.Urlmon.BINDSTRING = 23
BINDSTRING_ENTERPRISE_ID: win32more.Windows.Win32.System.Com.Urlmon.BINDSTRING = 24
BINDSTRING_DOC_URL: win32more.Windows.Win32.System.Com.Urlmon.BINDSTRING = 25
BINDSTRING_SAMESITE_COOKIE_LEVEL: win32more.Windows.Win32.System.Com.Urlmon.BINDSTRING = 26
BINDVERB = Int32
BINDVERB_GET: win32more.Windows.Win32.System.Com.Urlmon.BINDVERB = 0
BINDVERB_POST: win32more.Windows.Win32.System.Com.Urlmon.BINDVERB = 1
BINDVERB_PUT: win32more.Windows.Win32.System.Com.Urlmon.BINDVERB = 2
BINDVERB_CUSTOM: win32more.Windows.Win32.System.Com.Urlmon.BINDVERB = 3
BINDVERB_RESERVED1: win32more.Windows.Win32.System.Com.Urlmon.BINDVERB = 4
BSCF = Int32
BSCF_FIRSTDATANOTIFICATION: win32more.Windows.Win32.System.Com.Urlmon.BSCF = 1
BSCF_INTERMEDIATEDATANOTIFICATION: win32more.Windows.Win32.System.Com.Urlmon.BSCF = 2
BSCF_LASTDATANOTIFICATION: win32more.Windows.Win32.System.Com.Urlmon.BSCF = 4
BSCF_DATAFULLYAVAILABLE: win32more.Windows.Win32.System.Com.Urlmon.BSCF = 8
BSCF_AVAILABLEDATASIZEUNKNOWN: win32more.Windows.Win32.System.Com.Urlmon.BSCF = 16
BSCF_SKIPDRAINDATAFORFILEURLS: win32more.Windows.Win32.System.Com.Urlmon.BSCF = 32
BSCF_64BITLENGTHDOWNLOAD: win32more.Windows.Win32.System.Com.Urlmon.BSCF = 64
CIP_STATUS = Int32
CIP_DISK_FULL: win32more.Windows.Win32.System.Com.Urlmon.CIP_STATUS = 0
CIP_ACCESS_DENIED: win32more.Windows.Win32.System.Com.Urlmon.CIP_STATUS = 1
CIP_NEWER_VERSION_EXISTS: win32more.Windows.Win32.System.Com.Urlmon.CIP_STATUS = 2
CIP_OLDER_VERSION_EXISTS: win32more.Windows.Win32.System.Com.Urlmon.CIP_STATUS = 3
CIP_NAME_CONFLICT: win32more.Windows.Win32.System.Com.Urlmon.CIP_STATUS = 4
CIP_TRUST_VERIFICATION_COMPONENT_MISSING: win32more.Windows.Win32.System.Com.Urlmon.CIP_STATUS = 5
CIP_EXE_SELF_REGISTERATION_TIMEOUT: win32more.Windows.Win32.System.Com.Urlmon.CIP_STATUS = 6
CIP_UNSAFE_TO_ABORT: win32more.Windows.Win32.System.Com.Urlmon.CIP_STATUS = 7
CIP_NEED_REBOOT: win32more.Windows.Win32.System.Com.Urlmon.CIP_STATUS = 8
CIP_NEED_REBOOT_UI_PERMISSION: win32more.Windows.Win32.System.Com.Urlmon.CIP_STATUS = 9
class CODEBASEHOLD(Structure):
    cbSize: UInt32
    szDistUnit: win32more.Windows.Win32.Foundation.PWSTR
    szCodeBase: win32more.Windows.Win32.Foundation.PWSTR
    dwVersionMS: UInt32
    dwVersionLS: UInt32
    dwStyle: UInt32
class CONFIRMSAFETY(Structure):
    clsid: Guid
    pUnk: win32more.Windows.Win32.System.Com.IUnknown
    dwFlags: UInt32
class DATAINFO(Structure):
    ulTotalSize: UInt32
    ulavrPacketSize: UInt32
    ulConnectSpeed: UInt32
    ulProcessorSpeed: UInt32
class HIT_LOGGING_INFO(Structure):
    dwStructSize: UInt32
    lpszLoggedUrlName: win32more.Windows.Win32.Foundation.PSTR
    StartTime: win32more.Windows.Win32.Foundation.SYSTEMTIME
    EndTime: win32more.Windows.Win32.Foundation.SYSTEMTIME
    lpszExtendedInfo: win32more.Windows.Win32.Foundation.PSTR
class IBindCallbackRedirect(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{11c81bc2-121e-4ed5-b9c4-b430bd54f2c0}')
    @commethod(3)
    def Redirect(self, lpcUrl: win32more.Windows.Win32.Foundation.PWSTR, vbCancel: POINTER(win32more.Windows.Win32.Foundation.VARIANT_BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBindHttpSecurity(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a9eda967-f50e-4a33-b358-206f6ef3086d}')
    @commethod(3)
    def GetIgnoreCertMask(self, pdwIgnoreCertMask: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IBindProtocol(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{79eac9cd-baf9-11ce-8c82-00aa004ba90b}')
    @commethod(3)
    def CreateBinding(self, szUrl: win32more.Windows.Win32.Foundation.PWSTR, pbc: win32more.Windows.Win32.System.Com.IBindCtx, ppb: POINTER(win32more.Windows.Win32.System.Com.IBinding)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICatalogFileInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{711c7600-6b48-11d1-b403-00aa00b92af1}')
    @commethod(3)
    def GetCatalogFile(self, ppszCatalogFile: POINTER(win32more.Windows.Win32.Foundation.PSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetJavaTrust(self, ppJavaTrust: POINTER(VoidPtr)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ICodeInstall(ComPtr):
    extends: win32more.Windows.Win32.System.Com.Urlmon.IWindowForBindingUI
    _iid_ = Guid('{79eac9d1-baf9-11ce-8c82-00aa004ba90b}')
    @commethod(4)
    def OnCodeInstallProblem(self, ulStatusCode: UInt32, szDestination: win32more.Windows.Win32.Foundation.PWSTR, szSource: win32more.Windows.Win32.Foundation.PWSTR, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IDataFilter(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{69d14c80-c18e-11d0-a9ce-006097942311}')
    @commethod(3)
    def DoEncode(self, dwFlags: UInt32, lInBufferSize: Int32, pbInBuffer: POINTER(Byte), lOutBufferSize: Int32, pbOutBuffer: POINTER(Byte), lInBytesAvailable: Int32, plInBytesRead: POINTER(Int32), plOutBytesWritten: POINTER(Int32), dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DoDecode(self, dwFlags: UInt32, lInBufferSize: Int32, pbInBuffer: POINTER(Byte), lOutBufferSize: Int32, pbOutBuffer: POINTER(Byte), lInBytesAvailable: Int32, plInBytesRead: POINTER(Int32), plOutBytesWritten: POINTER(Int32), dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetEncodingLevel(self, dwEncLevel: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
IEObjectType = Int32
IE_EPM_OBJECT_EVENT: win32more.Windows.Win32.System.Com.Urlmon.IEObjectType = 0
IE_EPM_OBJECT_MUTEX: win32more.Windows.Win32.System.Com.Urlmon.IEObjectType = 1
IE_EPM_OBJECT_SEMAPHORE: win32more.Windows.Win32.System.Com.Urlmon.IEObjectType = 2
IE_EPM_OBJECT_SHARED_MEMORY: win32more.Windows.Win32.System.Com.Urlmon.IEObjectType = 3
IE_EPM_OBJECT_WAITABLE_TIMER: win32more.Windows.Win32.System.Com.Urlmon.IEObjectType = 4
IE_EPM_OBJECT_FILE: win32more.Windows.Win32.System.Com.Urlmon.IEObjectType = 5
IE_EPM_OBJECT_NAMED_PIPE: win32more.Windows.Win32.System.Com.Urlmon.IEObjectType = 6
IE_EPM_OBJECT_REGISTRY: win32more.Windows.Win32.System.Com.Urlmon.IEObjectType = 7
class IEncodingFilterFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{70bdde00-c18e-11d0-a9ce-006097942311}')
    @commethod(3)
    def FindBestFilter(self, pwzCodeIn: win32more.Windows.Win32.Foundation.PWSTR, pwzCodeOut: win32more.Windows.Win32.Foundation.PWSTR, info: win32more.Windows.Win32.System.Com.Urlmon.DATAINFO, ppDF: POINTER(win32more.Windows.Win32.System.Com.Urlmon.IDataFilter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDefaultFilter(self, pwzCodeIn: win32more.Windows.Win32.Foundation.PWSTR, pwzCodeOut: win32more.Windows.Win32.Foundation.PWSTR, ppDF: POINTER(win32more.Windows.Win32.System.Com.Urlmon.IDataFilter)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IGetBindHandle(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{af0ff408-129d-4b20-91f0-02bd23d88352}')
    @commethod(3)
    def GetBindHandle(self, enumRequestedHandle: win32more.Windows.Win32.System.Com.Urlmon.BINDHANDLETYPES, pRetHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHttpNegotiate(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{79eac9d2-baf9-11ce-8c82-00aa004ba90b}')
    @commethod(3)
    def BeginningTransaction(self, szURL: win32more.Windows.Win32.Foundation.PWSTR, szHeaders: win32more.Windows.Win32.Foundation.PWSTR, dwReserved: UInt32, pszAdditionalHeaders: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnResponse(self, dwResponseCode: UInt32, szResponseHeaders: win32more.Windows.Win32.Foundation.PWSTR, szRequestHeaders: win32more.Windows.Win32.Foundation.PWSTR, pszAdditionalRequestHeaders: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHttpNegotiate2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.Urlmon.IHttpNegotiate
    _iid_ = Guid('{4f9f9fcb-e0f4-48eb-b7ab-fa2ea9365cb4}')
    @commethod(5)
    def GetRootSecurityId(self, pbSecurityId: POINTER(Byte), pcbSecurityId: POINTER(UInt32), dwReserved: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHttpNegotiate3(ComPtr):
    extends: win32more.Windows.Win32.System.Com.Urlmon.IHttpNegotiate2
    _iid_ = Guid('{57b6c80a-34c2-4602-bc26-66a02fc57153}')
    @commethod(6)
    def GetSerializedClientCertContext(self, ppbCert: POINTER(POINTER(Byte)), pcbCert: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IHttpSecurity(ComPtr):
    extends: win32more.Windows.Win32.System.Com.Urlmon.IWindowForBindingUI
    _iid_ = Guid('{79eac9d7-bafa-11ce-8c82-00aa004ba90b}')
    @commethod(4)
    def OnSecurityProblem(self, dwProblem: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInternet(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{79eac9e0-baf9-11ce-8c82-00aa004ba90b}')
class IInternetBindInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{79eac9e1-baf9-11ce-8c82-00aa004ba90b}')
    @commethod(3)
    def GetBindInfo(self, grfBINDF: POINTER(UInt32), pbindinfo: POINTER(win32more.Windows.Win32.System.Com.BINDINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetBindString(self, ulStringType: UInt32, ppwzStr: POINTER(win32more.Windows.Win32.Foundation.PWSTR), cEl: UInt32, pcElFetched: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInternetBindInfoEx(ComPtr):
    extends: win32more.Windows.Win32.System.Com.Urlmon.IInternetBindInfo
    _iid_ = Guid('{a3e015b7-a82c-4dcd-a150-569aeeed36ab}')
    @commethod(5)
    def GetBindInfoEx(self, grfBINDF: POINTER(UInt32), pbindinfo: POINTER(win32more.Windows.Win32.System.Com.BINDINFO), grfBINDF2: POINTER(UInt32), pdwReserved: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInternetHostSecurityManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{3af280b6-cb3f-11d0-891e-00c04fb6bfc4}')
    @commethod(3)
    def GetSecurityId(self, pbSecurityId: POINTER(Byte), pcbSecurityId: POINTER(UInt32), dwReserved: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ProcessUrlAction(self, dwAction: UInt32, pPolicy: POINTER(Byte), cbPolicy: UInt32, pContext: POINTER(Byte), cbContext: UInt32, dwFlags: UInt32, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def QueryCustomPolicy(self, guidKey: POINTER(Guid), ppPolicy: POINTER(POINTER(Byte)), pcbPolicy: POINTER(UInt32), pContext: POINTER(Byte), cbContext: UInt32, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInternetPriority(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{79eac9eb-baf9-11ce-8c82-00aa004ba90b}')
    @commethod(3)
    def SetPriority(self, nPriority: Int32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPriority(self, pnPriority: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInternetProtocol(ComPtr):
    extends: win32more.Windows.Win32.System.Com.Urlmon.IInternetProtocolRoot
    _iid_ = Guid('{79eac9e4-baf9-11ce-8c82-00aa004ba90b}')
    @commethod(9)
    def Read(self, pv: VoidPtr, cb: UInt32, pcbRead: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Seek(self, dlibMove: Int64, dwOrigin: UInt32, plibNewPosition: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def LockRequest(self, dwOptions: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def UnlockRequest(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInternetProtocolEx(ComPtr):
    extends: win32more.Windows.Win32.System.Com.Urlmon.IInternetProtocol
    _iid_ = Guid('{c7a98e66-1010-492c-a1c8-c809e1f75905}')
    @commethod(13)
    def StartEx(self, pUri: win32more.Windows.Win32.System.Com.IUri, pOIProtSink: win32more.Windows.Win32.System.Com.Urlmon.IInternetProtocolSink, pOIBindInfo: win32more.Windows.Win32.System.Com.Urlmon.IInternetBindInfo, grfPI: UInt32, dwReserved: win32more.Windows.Win32.Foundation.HANDLE_PTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInternetProtocolInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{79eac9ec-baf9-11ce-8c82-00aa004ba90b}')
    @commethod(3)
    def ParseUrl(self, pwzUrl: win32more.Windows.Win32.Foundation.PWSTR, ParseAction: win32more.Windows.Win32.System.Com.Urlmon.PARSEACTION, dwParseFlags: UInt32, pwzResult: win32more.Windows.Win32.Foundation.PWSTR, cchResult: UInt32, pcchResult: POINTER(UInt32), dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CombineUrl(self, pwzBaseUrl: win32more.Windows.Win32.Foundation.PWSTR, pwzRelativeUrl: win32more.Windows.Win32.Foundation.PWSTR, dwCombineFlags: UInt32, pwzResult: win32more.Windows.Win32.Foundation.PWSTR, cchResult: UInt32, pcchResult: POINTER(UInt32), dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CompareUrl(self, pwzUrl1: win32more.Windows.Win32.Foundation.PWSTR, pwzUrl2: win32more.Windows.Win32.Foundation.PWSTR, dwCompareFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def QueryInfo(self, pwzUrl: win32more.Windows.Win32.Foundation.PWSTR, OueryOption: win32more.Windows.Win32.System.Com.Urlmon.QUERYOPTION, dwQueryFlags: UInt32, pBuffer: VoidPtr, cbBuffer: UInt32, pcbBuf: POINTER(UInt32), dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInternetProtocolRoot(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{79eac9e3-baf9-11ce-8c82-00aa004ba90b}')
    @commethod(3)
    def Start(self, szUrl: win32more.Windows.Win32.Foundation.PWSTR, pOIProtSink: win32more.Windows.Win32.System.Com.Urlmon.IInternetProtocolSink, pOIBindInfo: win32more.Windows.Win32.System.Com.Urlmon.IInternetBindInfo, grfPI: UInt32, dwReserved: win32more.Windows.Win32.Foundation.HANDLE_PTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Continue(self, pProtocolData: POINTER(win32more.Windows.Win32.System.Com.Urlmon.PROTOCOLDATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Abort(self, hrReason: win32more.Windows.Win32.Foundation.HRESULT, dwOptions: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Terminate(self, dwOptions: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Suspend(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Resume(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInternetProtocolSink(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{79eac9e5-baf9-11ce-8c82-00aa004ba90b}')
    @commethod(3)
    def Switch(self, pProtocolData: POINTER(win32more.Windows.Win32.System.Com.Urlmon.PROTOCOLDATA)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReportProgress(self, ulStatusCode: UInt32, szStatusText: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ReportData(self, grfBSCF: UInt32, ulProgress: UInt32, ulProgressMax: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ReportResult(self, hrResult: win32more.Windows.Win32.Foundation.HRESULT, dwError: UInt32, szResult: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInternetProtocolSinkStackable(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{79eac9f0-baf9-11ce-8c82-00aa004ba90b}')
    @commethod(3)
    def SwitchSink(self, pOIProtSink: win32more.Windows.Win32.System.Com.Urlmon.IInternetProtocolSink) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CommitSwitch(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RollbackSwitch(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInternetSecurityManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{79eac9ee-baf9-11ce-8c82-00aa004ba90b}')
    @commethod(3)
    def SetSecuritySite(self, pSite: win32more.Windows.Win32.System.Com.Urlmon.IInternetSecurityMgrSite) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSecuritySite(self, ppSite: POINTER(win32more.Windows.Win32.System.Com.Urlmon.IInternetSecurityMgrSite)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MapUrlToZone(self, pwszUrl: win32more.Windows.Win32.Foundation.PWSTR, pdwZone: POINTER(UInt32), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSecurityId(self, pwszUrl: win32more.Windows.Win32.Foundation.PWSTR, pbSecurityId: POINTER(Byte), pcbSecurityId: POINTER(UInt32), dwReserved: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ProcessUrlAction(self, pwszUrl: win32more.Windows.Win32.Foundation.PWSTR, dwAction: UInt32, pPolicy: POINTER(Byte), cbPolicy: UInt32, pContext: POINTER(Byte), cbContext: UInt32, dwFlags: UInt32, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def QueryCustomPolicy(self, pwszUrl: win32more.Windows.Win32.Foundation.PWSTR, guidKey: POINTER(Guid), ppPolicy: POINTER(POINTER(Byte)), pcbPolicy: POINTER(UInt32), pContext: POINTER(Byte), cbContext: UInt32, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetZoneMapping(self, dwZone: UInt32, lpszPattern: win32more.Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetZoneMappings(self, dwZone: UInt32, ppenumString: POINTER(win32more.Windows.Win32.System.Com.IEnumString), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInternetSecurityManagerEx(ComPtr):
    extends: win32more.Windows.Win32.System.Com.Urlmon.IInternetSecurityManager
    _iid_ = Guid('{f164edf1-cc7c-4f0d-9a94-34222625c393}')
    @commethod(11)
    def ProcessUrlActionEx(self, pwszUrl: win32more.Windows.Win32.Foundation.PWSTR, dwAction: UInt32, pPolicy: POINTER(Byte), cbPolicy: UInt32, pContext: POINTER(Byte), cbContext: UInt32, dwFlags: UInt32, dwReserved: UInt32, pdwOutFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInternetSecurityManagerEx2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.Urlmon.IInternetSecurityManagerEx
    _iid_ = Guid('{f1e50292-a795-4117-8e09-2b560a72ac60}')
    @commethod(12)
    def MapUrlToZoneEx2(self, pUri: win32more.Windows.Win32.System.Com.IUri, pdwZone: POINTER(UInt32), dwFlags: UInt32, ppwszMappedUrl: POINTER(win32more.Windows.Win32.Foundation.PWSTR), pdwOutFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def ProcessUrlActionEx2(self, pUri: win32more.Windows.Win32.System.Com.IUri, dwAction: UInt32, pPolicy: POINTER(Byte), cbPolicy: UInt32, pContext: POINTER(Byte), cbContext: UInt32, dwFlags: UInt32, dwReserved: UIntPtr, pdwOutFlags: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetSecurityIdEx2(self, pUri: win32more.Windows.Win32.System.Com.IUri, pbSecurityId: POINTER(Byte), pcbSecurityId: POINTER(UInt32), dwReserved: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def QueryCustomPolicyEx2(self, pUri: win32more.Windows.Win32.System.Com.IUri, guidKey: POINTER(Guid), ppPolicy: POINTER(POINTER(Byte)), pcbPolicy: POINTER(UInt32), pContext: POINTER(Byte), cbContext: UInt32, dwReserved: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInternetSecurityMgrSite(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{79eac9ed-baf9-11ce-8c82-00aa004ba90b}')
    @commethod(3)
    def GetWindow(self, phwnd: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnableModeless(self, fEnable: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInternetSession(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{79eac9e7-baf9-11ce-8c82-00aa004ba90b}')
    @commethod(3)
    def RegisterNameSpace(self, pCF: win32more.Windows.Win32.System.Com.IClassFactory, rclsid: POINTER(Guid), pwzProtocol: win32more.Windows.Win32.Foundation.PWSTR, cPatterns: UInt32, ppwzPatterns: POINTER(win32more.Windows.Win32.Foundation.PWSTR), dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterNameSpace(self, pCF: win32more.Windows.Win32.System.Com.IClassFactory, pszProtocol: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RegisterMimeFilter(self, pCF: win32more.Windows.Win32.System.Com.IClassFactory, rclsid: POINTER(Guid), pwzType: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def UnregisterMimeFilter(self, pCF: win32more.Windows.Win32.System.Com.IClassFactory, pwzType: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateBinding(self, pBC: win32more.Windows.Win32.System.Com.IBindCtx, szUrl: win32more.Windows.Win32.Foundation.PWSTR, pUnkOuter: win32more.Windows.Win32.System.Com.IUnknown, ppUnk: POINTER(win32more.Windows.Win32.System.Com.IUnknown), ppOInetProt: POINTER(win32more.Windows.Win32.System.Com.Urlmon.IInternetProtocol), dwOption: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetSessionOption(self, dwOption: UInt32, pBuffer: VoidPtr, dwBufferLength: UInt32, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSessionOption(self, dwOption: UInt32, pBuffer: VoidPtr, pdwBufferLength: POINTER(UInt32), dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInternetThreadSwitch(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{79eac9e8-baf9-11ce-8c82-00aa004ba90b}')
    @commethod(3)
    def Prepare(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Continue(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInternetZoneManager(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{79eac9ef-baf9-11ce-8c82-00aa004ba90b}')
    @commethod(3)
    def GetZoneAttributes(self, dwZone: UInt32, pZoneAttributes: POINTER(win32more.Windows.Win32.System.Com.Urlmon.ZONEATTRIBUTES)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetZoneAttributes(self, dwZone: UInt32, pZoneAttributes: POINTER(win32more.Windows.Win32.System.Com.Urlmon.ZONEATTRIBUTES)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetZoneCustomPolicy(self, dwZone: UInt32, guidKey: POINTER(Guid), ppPolicy: POINTER(POINTER(Byte)), pcbPolicy: POINTER(UInt32), urlZoneReg: win32more.Windows.Win32.System.Com.Urlmon.URLZONEREG) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetZoneCustomPolicy(self, dwZone: UInt32, guidKey: POINTER(Guid), pPolicy: POINTER(Byte), cbPolicy: UInt32, urlZoneReg: win32more.Windows.Win32.System.Com.Urlmon.URLZONEREG) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetZoneActionPolicy(self, dwZone: UInt32, dwAction: UInt32, pPolicy: POINTER(Byte), cbPolicy: UInt32, urlZoneReg: win32more.Windows.Win32.System.Com.Urlmon.URLZONEREG) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetZoneActionPolicy(self, dwZone: UInt32, dwAction: UInt32, pPolicy: POINTER(Byte), cbPolicy: UInt32, urlZoneReg: win32more.Windows.Win32.System.Com.Urlmon.URLZONEREG) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def PromptAction(self, dwAction: UInt32, hwndParent: win32more.Windows.Win32.Foundation.HWND, pwszUrl: win32more.Windows.Win32.Foundation.PWSTR, pwszText: win32more.Windows.Win32.Foundation.PWSTR, dwPromptFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def LogAction(self, dwAction: UInt32, pwszUrl: win32more.Windows.Win32.Foundation.PWSTR, pwszText: win32more.Windows.Win32.Foundation.PWSTR, dwLogFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CreateZoneEnumerator(self, pdwEnum: POINTER(UInt32), pdwCount: POINTER(UInt32), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetZoneAt(self, dwEnum: UInt32, dwIndex: UInt32, pdwZone: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def DestroyZoneEnumerator(self, dwEnum: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CopyTemplatePoliciesToZone(self, dwTemplate: UInt32, dwZone: UInt32, dwReserved: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInternetZoneManagerEx(ComPtr):
    extends: win32more.Windows.Win32.System.Com.Urlmon.IInternetZoneManager
    _iid_ = Guid('{a4c23339-8e06-431e-9bf4-7e711c085648}')
    @commethod(15)
    def GetZoneActionPolicyEx(self, dwZone: UInt32, dwAction: UInt32, pPolicy: POINTER(Byte), cbPolicy: UInt32, urlZoneReg: win32more.Windows.Win32.System.Com.Urlmon.URLZONEREG, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetZoneActionPolicyEx(self, dwZone: UInt32, dwAction: UInt32, pPolicy: POINTER(Byte), cbPolicy: UInt32, urlZoneReg: win32more.Windows.Win32.System.Com.Urlmon.URLZONEREG, dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IInternetZoneManagerEx2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.Urlmon.IInternetZoneManagerEx
    _iid_ = Guid('{edc17559-dd5d-4846-8eef-8becba5a4abf}')
    @commethod(17)
    def GetZoneAttributesEx(self, dwZone: UInt32, pZoneAttributes: POINTER(win32more.Windows.Win32.System.Com.Urlmon.ZONEATTRIBUTES), dwFlags: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetZoneSecurityState(self, dwZoneIndex: UInt32, fRespectPolicy: win32more.Windows.Win32.Foundation.BOOL, pdwState: POINTER(UInt32), pfPolicyEncountered: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetIESecurityState(self, fRespectPolicy: win32more.Windows.Win32.Foundation.BOOL, pdwState: POINTER(UInt32), pfPolicyEncountered: POINTER(win32more.Windows.Win32.Foundation.BOOL), fNoCache: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def FixUnsecureSettings(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IMonikerProp(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a5ca5f7f-1847-4d87-9c5b-918509f7511d}')
    @commethod(3)
    def PutProperty(self, mkp: win32more.Windows.Win32.System.Com.Urlmon.MONIKERPROPERTY, val: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
INET_ZONE_MANAGER_CONSTANTS = Int32
MAX_ZONE_PATH: win32more.Windows.Win32.System.Com.Urlmon.INET_ZONE_MANAGER_CONSTANTS = 260
MAX_ZONE_DESCRIPTION: win32more.Windows.Win32.System.Com.Urlmon.INET_ZONE_MANAGER_CONSTANTS = 200
INTERNETFEATURELIST = Int32
FEATURE_OBJECT_CACHING: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST = 0
FEATURE_ZONE_ELEVATION: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST = 1
FEATURE_MIME_HANDLING: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST = 2
FEATURE_MIME_SNIFFING: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST = 3
FEATURE_WINDOW_RESTRICTIONS: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST = 4
FEATURE_WEBOC_POPUPMANAGEMENT: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST = 5
FEATURE_BEHAVIORS: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST = 6
FEATURE_DISABLE_MK_PROTOCOL: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST = 7
FEATURE_LOCALMACHINE_LOCKDOWN: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST = 8
FEATURE_SECURITYBAND: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST = 9
FEATURE_RESTRICT_ACTIVEXINSTALL: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST = 10
FEATURE_VALIDATE_NAVIGATE_URL: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST = 11
FEATURE_RESTRICT_FILEDOWNLOAD: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST = 12
FEATURE_ADDON_MANAGEMENT: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST = 13
FEATURE_PROTOCOL_LOCKDOWN: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST = 14
FEATURE_HTTP_USERNAME_PASSWORD_DISABLE: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST = 15
FEATURE_SAFE_BINDTOOBJECT: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST = 16
FEATURE_UNC_SAVEDFILECHECK: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST = 17
FEATURE_GET_URL_DOM_FILEPATH_UNENCODED: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST = 18
FEATURE_TABBED_BROWSING: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST = 19
FEATURE_SSLUX: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST = 20
FEATURE_DISABLE_NAVIGATION_SOUNDS: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST = 21
FEATURE_DISABLE_LEGACY_COMPRESSION: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST = 22
FEATURE_FORCE_ADDR_AND_STATUS: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST = 23
FEATURE_XMLHTTP: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST = 24
FEATURE_DISABLE_TELNET_PROTOCOL: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST = 25
FEATURE_FEEDS: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST = 26
FEATURE_BLOCK_INPUT_PROMPTS: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST = 27
FEATURE_ENTRY_COUNT: win32more.Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST = 28
class IPersistMoniker(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{79eac9c9-baf9-11ce-8c82-00aa004ba90b}')
    @commethod(3)
    def GetClassID(self, pClassID: POINTER(Guid)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsDirty(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Load(self, fFullyAvailable: win32more.Windows.Win32.Foundation.BOOL, pimkName: win32more.Windows.Win32.System.Com.IMoniker, pibc: win32more.Windows.Win32.System.Com.IBindCtx, grfMode: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Save(self, pimkName: win32more.Windows.Win32.System.Com.IMoniker, pbc: win32more.Windows.Win32.System.Com.IBindCtx, fRemember: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SaveCompleted(self, pimkName: win32more.Windows.Win32.System.Com.IMoniker, pibc: win32more.Windows.Win32.System.Com.IBindCtx) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetCurMoniker(self, ppimkName: POINTER(win32more.Windows.Win32.System.Com.IMoniker)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISoftDistExt(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{b15b8dc1-c7e1-11d0-8680-00aa00bdcb71}')
    @commethod(3)
    def ProcessSoftDist(self, szCDFURL: win32more.Windows.Win32.Foundation.PWSTR, pSoftDistElement: win32more.Windows.Win32.Data.Xml.MsXml.IXMLElement, lpsdi: POINTER(win32more.Windows.Win32.System.Com.Urlmon.SOFTDISTINFO)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFirstCodeBase(self, szCodeBase: POINTER(win32more.Windows.Win32.Foundation.PWSTR), dwMaxSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetNextCodeBase(self, szCodeBase: POINTER(win32more.Windows.Win32.Foundation.PWSTR), dwMaxSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AsyncInstallDistributionUnit(self, pbc: win32more.Windows.Win32.System.Com.IBindCtx, pvReserved: VoidPtr, flags: UInt32, lpcbh: POINTER(win32more.Windows.Win32.System.Com.Urlmon.CODEBASEHOLD)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUriBuilderFactory(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{e982ce48-0b96-440c-bc37-0c869b27a29e}')
    @commethod(3)
    def CreateIUriBuilder(self, dwFlags: UInt32, dwReserved: UIntPtr, ppIUriBuilder: POINTER(win32more.Windows.Win32.System.Com.IUriBuilder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateInitializedIUriBuilder(self, dwFlags: UInt32, dwReserved: UIntPtr, ppIUriBuilder: POINTER(win32more.Windows.Win32.System.Com.IUriBuilder)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IUriContainer(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{a158a630-ed6f-45fb-b987-f68676f57752}')
    @commethod(3)
    def GetIUri(self, ppIUri: POINTER(win32more.Windows.Win32.System.Com.IUri)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWinInetCacheHints(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{dd1ec3b3-8391-4fdb-a9e6-347c3caaa7dd}')
    @commethod(3)
    def SetCacheExtension(self, pwzExt: win32more.Windows.Win32.Foundation.PWSTR, pszCacheFile: VoidPtr, pcbCacheFile: POINTER(UInt32), pdwWinInetError: POINTER(UInt32), pdwReserved: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWinInetCacheHints2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.Urlmon.IWinInetCacheHints
    _iid_ = Guid('{7857aeac-d31f-49bf-884e-dd46df36780a}')
    @commethod(4)
    def SetCacheExtension2(self, pwzExt: win32more.Windows.Win32.Foundation.PWSTR, pwzCacheFile: win32more.Windows.Win32.Foundation.PWSTR, pcchCacheFile: POINTER(UInt32), pdwWinInetError: POINTER(UInt32), pdwReserved: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWinInetFileStream(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f134c4b7-b1f8-4e75-b886-74b90943becb}')
    @commethod(3)
    def SetHandleForUnlock(self, hWinInetLockHandle: UIntPtr, dwReserved: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetDeleteFile(self, dwReserved: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWinInetHttpInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.Urlmon.IWinInetInfo
    _iid_ = Guid('{79eac9d8-bafa-11ce-8c82-00aa004ba90b}')
    @commethod(4)
    def QueryInfo(self, dwOption: UInt32, pBuffer: VoidPtr, pcbBuf: POINTER(UInt32), pdwFlags: POINTER(UInt32), pdwReserved: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWinInetHttpTimeouts(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{f286fa56-c1fd-4270-8e67-b3eb790a81e8}')
    @commethod(3)
    def GetRequestTimeouts(self, pdwConnectTimeout: POINTER(UInt32), pdwSendTimeout: POINTER(UInt32), pdwReceiveTimeout: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWinInetInfo(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{79eac9d6-bafa-11ce-8c82-00aa004ba90b}')
    @commethod(3)
    def QueryOption(self, dwOption: UInt32, pBuffer: VoidPtr, pcbBuf: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWindowForBindingUI(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{79eac9d5-bafa-11ce-8c82-00aa004ba90b}')
    @commethod(3)
    def GetWindow(self, rguidReason: POINTER(Guid), phwnd: POINTER(win32more.Windows.Win32.Foundation.HWND)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IWrappedProtocol(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{53c84785-8425-4dc5-971b-e58d9c19f9b6}')
    @commethod(3)
    def GetWrapperCode(self, pnCode: POINTER(Int32), dwReserved: UIntPtr) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IZoneIdentifier(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{cd45f185-1b21-48e2-967b-ead743a8914e}')
    @commethod(3)
    def GetId(self, pdwZone: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetId(self, dwZone: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Remove(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IZoneIdentifier2(ComPtr):
    extends: win32more.Windows.Win32.System.Com.Urlmon.IZoneIdentifier
    _iid_ = Guid('{eb5e760c-09ef-45c0-b510-70830ce31e6a}')
    @commethod(6)
    def GetLastWriterPackageFamilyName(self, packageFamilyName: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetLastWriterPackageFamilyName(self, packageFamilyName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveLastWriterPackageFamilyName(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetAppZoneId(self, zone: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetAppZoneId(self, zone: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RemoveAppZoneId(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
MONIKERPROPERTY = Int32
MIMETYPEPROP: win32more.Windows.Win32.System.Com.Urlmon.MONIKERPROPERTY = 0
USE_SRC_URL: win32more.Windows.Win32.System.Com.Urlmon.MONIKERPROPERTY = 1
CLASSIDPROP: win32more.Windows.Win32.System.Com.Urlmon.MONIKERPROPERTY = 2
TRUSTEDDOWNLOADPROP: win32more.Windows.Win32.System.Com.Urlmon.MONIKERPROPERTY = 3
POPUPLEVELPROP: win32more.Windows.Win32.System.Com.Urlmon.MONIKERPROPERTY = 4
OIBDG_FLAGS = Int32
OIBDG_APARTMENTTHREADED: win32more.Windows.Win32.System.Com.Urlmon.OIBDG_FLAGS = 256
OIBDG_DATAONLY: win32more.Windows.Win32.System.Com.Urlmon.OIBDG_FLAGS = 4096
PARSEACTION = Int32
PARSE_CANONICALIZE: win32more.Windows.Win32.System.Com.Urlmon.PARSEACTION = 1
PARSE_FRIENDLY: win32more.Windows.Win32.System.Com.Urlmon.PARSEACTION = 2
PARSE_SECURITY_URL: win32more.Windows.Win32.System.Com.Urlmon.PARSEACTION = 3
PARSE_ROOTDOCUMENT: win32more.Windows.Win32.System.Com.Urlmon.PARSEACTION = 4
PARSE_DOCUMENT: win32more.Windows.Win32.System.Com.Urlmon.PARSEACTION = 5
PARSE_ANCHOR: win32more.Windows.Win32.System.Com.Urlmon.PARSEACTION = 6
PARSE_ENCODE_IS_UNESCAPE: win32more.Windows.Win32.System.Com.Urlmon.PARSEACTION = 7
PARSE_DECODE_IS_ESCAPE: win32more.Windows.Win32.System.Com.Urlmon.PARSEACTION = 8
PARSE_PATH_FROM_URL: win32more.Windows.Win32.System.Com.Urlmon.PARSEACTION = 9
PARSE_URL_FROM_PATH: win32more.Windows.Win32.System.Com.Urlmon.PARSEACTION = 10
PARSE_MIME: win32more.Windows.Win32.System.Com.Urlmon.PARSEACTION = 11
PARSE_SERVER: win32more.Windows.Win32.System.Com.Urlmon.PARSEACTION = 12
PARSE_SCHEMA: win32more.Windows.Win32.System.Com.Urlmon.PARSEACTION = 13
PARSE_SITE: win32more.Windows.Win32.System.Com.Urlmon.PARSEACTION = 14
PARSE_DOMAIN: win32more.Windows.Win32.System.Com.Urlmon.PARSEACTION = 15
PARSE_LOCATION: win32more.Windows.Win32.System.Com.Urlmon.PARSEACTION = 16
PARSE_SECURITY_DOMAIN: win32more.Windows.Win32.System.Com.Urlmon.PARSEACTION = 17
PARSE_ESCAPE: win32more.Windows.Win32.System.Com.Urlmon.PARSEACTION = 18
PARSE_UNESCAPE: win32more.Windows.Win32.System.Com.Urlmon.PARSEACTION = 19
PI_FLAGS = Int32
PI_PARSE_URL: win32more.Windows.Win32.System.Com.Urlmon.PI_FLAGS = 1
PI_FILTER_MODE: win32more.Windows.Win32.System.Com.Urlmon.PI_FLAGS = 2
PI_FORCE_ASYNC: win32more.Windows.Win32.System.Com.Urlmon.PI_FLAGS = 4
PI_USE_WORKERTHREAD: win32more.Windows.Win32.System.Com.Urlmon.PI_FLAGS = 8
PI_MIMEVERIFICATION: win32more.Windows.Win32.System.Com.Urlmon.PI_FLAGS = 16
PI_CLSIDLOOKUP: win32more.Windows.Win32.System.Com.Urlmon.PI_FLAGS = 32
PI_DATAPROGRESS: win32more.Windows.Win32.System.Com.Urlmon.PI_FLAGS = 64
PI_SYNCHRONOUS: win32more.Windows.Win32.System.Com.Urlmon.PI_FLAGS = 128
PI_APARTMENTTHREADED: win32more.Windows.Win32.System.Com.Urlmon.PI_FLAGS = 256
PI_CLASSINSTALL: win32more.Windows.Win32.System.Com.Urlmon.PI_FLAGS = 512
PI_PASSONBINDCTX: win32more.Windows.Win32.System.Com.Urlmon.PI_FLAGS = 8192
PI_NOMIMEHANDLER: win32more.Windows.Win32.System.Com.Urlmon.PI_FLAGS = 32768
PI_LOADAPPDIRECT: win32more.Windows.Win32.System.Com.Urlmon.PI_FLAGS = 16384
PD_FORCE_SWITCH: win32more.Windows.Win32.System.Com.Urlmon.PI_FLAGS = 65536
PI_PREFERDEFAULTHANDLER: win32more.Windows.Win32.System.Com.Urlmon.PI_FLAGS = 131072
class PROTOCOLDATA(Structure):
    grfFlags: UInt32
    dwState: UInt32
    pData: VoidPtr
    cbData: UInt32
class PROTOCOLFILTERDATA(Structure):
    cbSize: UInt32
    pProtocolSink: win32more.Windows.Win32.System.Com.Urlmon.IInternetProtocolSink
    pProtocol: win32more.Windows.Win32.System.Com.Urlmon.IInternetProtocol
    pUnk: win32more.Windows.Win32.System.Com.IUnknown
    dwFilterFlags: UInt32
class PROTOCOL_ARGUMENT(Structure):
    szMethod: win32more.Windows.Win32.Foundation.PWSTR
    szTargetUrl: win32more.Windows.Win32.Foundation.PWSTR
PSUACTION = Int32
PSU_DEFAULT: win32more.Windows.Win32.System.Com.Urlmon.PSUACTION = 1
PSU_SECURITY_URL_ONLY: win32more.Windows.Win32.System.Com.Urlmon.PSUACTION = 2
PUAF = Int32
PUAF_DEFAULT: win32more.Windows.Win32.System.Com.Urlmon.PUAF = 0
PUAF_NOUI: win32more.Windows.Win32.System.Com.Urlmon.PUAF = 1
PUAF_ISFILE: win32more.Windows.Win32.System.Com.Urlmon.PUAF = 2
PUAF_WARN_IF_DENIED: win32more.Windows.Win32.System.Com.Urlmon.PUAF = 4
PUAF_FORCEUI_FOREGROUND: win32more.Windows.Win32.System.Com.Urlmon.PUAF = 8
PUAF_CHECK_TIFS: win32more.Windows.Win32.System.Com.Urlmon.PUAF = 16
PUAF_DONTCHECKBOXINDIALOG: win32more.Windows.Win32.System.Com.Urlmon.PUAF = 32
PUAF_TRUSTED: win32more.Windows.Win32.System.Com.Urlmon.PUAF = 64
PUAF_ACCEPT_WILDCARD_SCHEME: win32more.Windows.Win32.System.Com.Urlmon.PUAF = 128
PUAF_ENFORCERESTRICTED: win32more.Windows.Win32.System.Com.Urlmon.PUAF = 256
PUAF_NOSAVEDFILECHECK: win32more.Windows.Win32.System.Com.Urlmon.PUAF = 512
PUAF_REQUIRESAVEDFILECHECK: win32more.Windows.Win32.System.Com.Urlmon.PUAF = 1024
PUAF_DONT_USE_CACHE: win32more.Windows.Win32.System.Com.Urlmon.PUAF = 4096
PUAF_RESERVED1: win32more.Windows.Win32.System.Com.Urlmon.PUAF = 8192
PUAF_RESERVED2: win32more.Windows.Win32.System.Com.Urlmon.PUAF = 16384
PUAF_LMZ_UNLOCKED: win32more.Windows.Win32.System.Com.Urlmon.PUAF = 65536
PUAF_LMZ_LOCKED: win32more.Windows.Win32.System.Com.Urlmon.PUAF = 131072
PUAF_DEFAULTZONEPOL: win32more.Windows.Win32.System.Com.Urlmon.PUAF = 262144
PUAF_NPL_USE_LOCKED_IF_RESTRICTED: win32more.Windows.Win32.System.Com.Urlmon.PUAF = 524288
PUAF_NOUIIFLOCKED: win32more.Windows.Win32.System.Com.Urlmon.PUAF = 1048576
PUAF_DRAGPROTOCOLCHECK: win32more.Windows.Win32.System.Com.Urlmon.PUAF = 2097152
PUAFOUT = Int32
PUAFOUT_DEFAULT: win32more.Windows.Win32.System.Com.Urlmon.PUAFOUT = 0
PUAFOUT_ISLOCKZONEPOLICY: win32more.Windows.Win32.System.Com.Urlmon.PUAFOUT = 1
QUERYOPTION = Int32
QUERY_EXPIRATION_DATE: win32more.Windows.Win32.System.Com.Urlmon.QUERYOPTION = 1
QUERY_TIME_OF_LAST_CHANGE: win32more.Windows.Win32.System.Com.Urlmon.QUERYOPTION = 2
QUERY_CONTENT_ENCODING: win32more.Windows.Win32.System.Com.Urlmon.QUERYOPTION = 3
QUERY_CONTENT_TYPE: win32more.Windows.Win32.System.Com.Urlmon.QUERYOPTION = 4
QUERY_REFRESH: win32more.Windows.Win32.System.Com.Urlmon.QUERYOPTION = 5
QUERY_RECOMBINE: win32more.Windows.Win32.System.Com.Urlmon.QUERYOPTION = 6
QUERY_CAN_NAVIGATE: win32more.Windows.Win32.System.Com.Urlmon.QUERYOPTION = 7
QUERY_USES_NETWORK: win32more.Windows.Win32.System.Com.Urlmon.QUERYOPTION = 8
QUERY_IS_CACHED: win32more.Windows.Win32.System.Com.Urlmon.QUERYOPTION = 9
QUERY_IS_INSTALLEDENTRY: win32more.Windows.Win32.System.Com.Urlmon.QUERYOPTION = 10
QUERY_IS_CACHED_OR_MAPPED: win32more.Windows.Win32.System.Com.Urlmon.QUERYOPTION = 11
QUERY_USES_CACHE: win32more.Windows.Win32.System.Com.Urlmon.QUERYOPTION = 12
QUERY_IS_SECURE: win32more.Windows.Win32.System.Com.Urlmon.QUERYOPTION = 13
QUERY_IS_SAFE: win32more.Windows.Win32.System.Com.Urlmon.QUERYOPTION = 14
QUERY_USES_HISTORYFOLDER: win32more.Windows.Win32.System.Com.Urlmon.QUERYOPTION = 15
QUERY_IS_CACHED_AND_USABLE_OFFLINE: win32more.Windows.Win32.System.Com.Urlmon.QUERYOPTION = 16
class REMSECURITY_ATTRIBUTES(Structure):
    nLength: UInt32
    lpSecurityDescriptor: UInt32
    bInheritHandle: win32more.Windows.Win32.Foundation.BOOL
class RemBINDINFO(Structure):
    cbSize: UInt32
    szExtraInfo: win32more.Windows.Win32.Foundation.PWSTR
    grfBindInfoF: UInt32
    dwBindVerb: UInt32
    szCustomVerb: win32more.Windows.Win32.Foundation.PWSTR
    cbstgmedData: UInt32
    dwOptions: UInt32
    dwOptionsFlags: UInt32
    dwCodePage: UInt32
    securityAttributes: win32more.Windows.Win32.System.Com.Urlmon.REMSECURITY_ATTRIBUTES
    iid: Guid
    pUnk: win32more.Windows.Win32.System.Com.IUnknown
    dwReserved: UInt32
class RemFORMATETC(Structure):
    cfFormat: UInt32
    ptd: UInt32
    dwAspect: UInt32
    lindex: Int32
    tymed: UInt32
class SOFTDISTINFO(Structure):
    cbSize: UInt32
    dwFlags: UInt32
    dwAdState: UInt32
    szTitle: win32more.Windows.Win32.Foundation.PWSTR
    szAbstract: win32more.Windows.Win32.Foundation.PWSTR
    szHREF: win32more.Windows.Win32.Foundation.PWSTR
    dwInstalledVersionMS: UInt32
    dwInstalledVersionLS: UInt32
    dwUpdateVersionMS: UInt32
    dwUpdateVersionLS: UInt32
    dwAdvertisedVersionMS: UInt32
    dwAdvertisedVersionLS: UInt32
    dwReserved: UInt32
SZM_FLAGS = Int32
SZM_CREATE: win32more.Windows.Win32.System.Com.Urlmon.SZM_FLAGS = 0
SZM_DELETE: win32more.Windows.Win32.System.Com.Urlmon.SZM_FLAGS = 1
class StartParam(Structure):
    iid: Guid
    pIBindCtx: win32more.Windows.Win32.System.Com.IBindCtx
    pItf: win32more.Windows.Win32.System.Com.IUnknown
URLTEMPLATE = Int32
URLTEMPLATE_CUSTOM: win32more.Windows.Win32.System.Com.Urlmon.URLTEMPLATE = 0
URLTEMPLATE_PREDEFINED_MIN: win32more.Windows.Win32.System.Com.Urlmon.URLTEMPLATE = 65536
URLTEMPLATE_LOW: win32more.Windows.Win32.System.Com.Urlmon.URLTEMPLATE = 65536
URLTEMPLATE_MEDLOW: win32more.Windows.Win32.System.Com.Urlmon.URLTEMPLATE = 66816
URLTEMPLATE_MEDIUM: win32more.Windows.Win32.System.Com.Urlmon.URLTEMPLATE = 69632
URLTEMPLATE_MEDHIGH: win32more.Windows.Win32.System.Com.Urlmon.URLTEMPLATE = 70912
URLTEMPLATE_HIGH: win32more.Windows.Win32.System.Com.Urlmon.URLTEMPLATE = 73728
URLTEMPLATE_PREDEFINED_MAX: win32more.Windows.Win32.System.Com.Urlmon.URLTEMPLATE = 131072
URLZONE = Int32
URLZONE_INVALID: win32more.Windows.Win32.System.Com.Urlmon.URLZONE = -1
URLZONE_PREDEFINED_MIN: win32more.Windows.Win32.System.Com.Urlmon.URLZONE = 0
URLZONE_LOCAL_MACHINE: win32more.Windows.Win32.System.Com.Urlmon.URLZONE = 0
URLZONE_INTRANET: win32more.Windows.Win32.System.Com.Urlmon.URLZONE = 1
URLZONE_TRUSTED: win32more.Windows.Win32.System.Com.Urlmon.URLZONE = 2
URLZONE_INTERNET: win32more.Windows.Win32.System.Com.Urlmon.URLZONE = 3
URLZONE_UNTRUSTED: win32more.Windows.Win32.System.Com.Urlmon.URLZONE = 4
URLZONE_PREDEFINED_MAX: win32more.Windows.Win32.System.Com.Urlmon.URLZONE = 999
URLZONE_USER_MIN: win32more.Windows.Win32.System.Com.Urlmon.URLZONE = 1000
URLZONE_USER_MAX: win32more.Windows.Win32.System.Com.Urlmon.URLZONE = 10000
URLZONEREG = Int32
URLZONEREG_DEFAULT: win32more.Windows.Win32.System.Com.Urlmon.URLZONEREG = 0
URLZONEREG_HKLM: win32more.Windows.Win32.System.Com.Urlmon.URLZONEREG = 1
URLZONEREG_HKCU: win32more.Windows.Win32.System.Com.Urlmon.URLZONEREG = 2
URL_ENCODING = Int32
URL_ENCODING_NONE: win32more.Windows.Win32.System.Com.Urlmon.URL_ENCODING = 0
URL_ENCODING_ENABLE_UTF8: win32more.Windows.Win32.System.Com.Urlmon.URL_ENCODING = 268435456
URL_ENCODING_DISABLE_UTF8: win32more.Windows.Win32.System.Com.Urlmon.URL_ENCODING = 536870912
Uri_HOST_TYPE = Int32
Uri_HOST_UNKNOWN: win32more.Windows.Win32.System.Com.Urlmon.Uri_HOST_TYPE = 0
Uri_HOST_DNS: win32more.Windows.Win32.System.Com.Urlmon.Uri_HOST_TYPE = 1
Uri_HOST_IPV4: win32more.Windows.Win32.System.Com.Urlmon.Uri_HOST_TYPE = 2
Uri_HOST_IPV6: win32more.Windows.Win32.System.Com.Urlmon.Uri_HOST_TYPE = 3
Uri_HOST_IDN: win32more.Windows.Win32.System.Com.Urlmon.Uri_HOST_TYPE = 4
ZAFLAGS = Int32
ZAFLAGS_CUSTOM_EDIT: win32more.Windows.Win32.System.Com.Urlmon.ZAFLAGS = 1
ZAFLAGS_ADD_SITES: win32more.Windows.Win32.System.Com.Urlmon.ZAFLAGS = 2
ZAFLAGS_REQUIRE_VERIFICATION: win32more.Windows.Win32.System.Com.Urlmon.ZAFLAGS = 4
ZAFLAGS_INCLUDE_PROXY_OVERRIDE: win32more.Windows.Win32.System.Com.Urlmon.ZAFLAGS = 8
ZAFLAGS_INCLUDE_INTRANET_SITES: win32more.Windows.Win32.System.Com.Urlmon.ZAFLAGS = 16
ZAFLAGS_NO_UI: win32more.Windows.Win32.System.Com.Urlmon.ZAFLAGS = 32
ZAFLAGS_SUPPORTS_VERIFICATION: win32more.Windows.Win32.System.Com.Urlmon.ZAFLAGS = 64
ZAFLAGS_UNC_AS_INTRANET: win32more.Windows.Win32.System.Com.Urlmon.ZAFLAGS = 128
ZAFLAGS_DETECT_INTRANET: win32more.Windows.Win32.System.Com.Urlmon.ZAFLAGS = 256
ZAFLAGS_USE_LOCKED_ZONES: win32more.Windows.Win32.System.Com.Urlmon.ZAFLAGS = 65536
ZAFLAGS_VERIFY_TEMPLATE_SETTINGS: win32more.Windows.Win32.System.Com.Urlmon.ZAFLAGS = 131072
ZAFLAGS_NO_CACHE: win32more.Windows.Win32.System.Com.Urlmon.ZAFLAGS = 262144
class ZONEATTRIBUTES(Structure):
    cbSize: UInt32
    szDisplayName: Char * 260
    szDescription: Char * 200
    szIconPath: Char * 260
    dwTemplateMinLevel: UInt32
    dwTemplateRecommended: UInt32
    dwTemplateCurrentLevel: UInt32
    dwFlags: UInt32


make_ready(__name__)
