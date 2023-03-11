from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Data.Xml.MsXml
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.Com.Urlmon
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
AUTHENTICATEF = Int32
AUTHENTICATEF_PROXY: AUTHENTICATEF = 1
AUTHENTICATEF_BASIC: AUTHENTICATEF = 2
AUTHENTICATEF_HTTP: AUTHENTICATEF = 4
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
MK_S_ASYNCHRONOUS: Windows.Win32.Foundation.HRESULT = 262632
S_ASYNCHRONOUS: Int32 = 262632
E_PENDING: Windows.Win32.Foundation.HRESULT = -2147483638
INET_E_INVALID_URL: Windows.Win32.Foundation.HRESULT = -2146697214
INET_E_NO_SESSION: Windows.Win32.Foundation.HRESULT = -2146697213
INET_E_CANNOT_CONNECT: Windows.Win32.Foundation.HRESULT = -2146697212
INET_E_RESOURCE_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -2146697211
INET_E_OBJECT_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -2146697210
INET_E_DATA_NOT_AVAILABLE: Windows.Win32.Foundation.HRESULT = -2146697209
INET_E_DOWNLOAD_FAILURE: Windows.Win32.Foundation.HRESULT = -2146697208
INET_E_AUTHENTICATION_REQUIRED: Windows.Win32.Foundation.HRESULT = -2146697207
INET_E_NO_VALID_MEDIA: Windows.Win32.Foundation.HRESULT = -2146697206
INET_E_CONNECTION_TIMEOUT: Windows.Win32.Foundation.HRESULT = -2146697205
INET_E_INVALID_REQUEST: Windows.Win32.Foundation.HRESULT = -2146697204
INET_E_UNKNOWN_PROTOCOL: Windows.Win32.Foundation.HRESULT = -2146697203
INET_E_SECURITY_PROBLEM: Windows.Win32.Foundation.HRESULT = -2146697202
INET_E_CANNOT_LOAD_DATA: Windows.Win32.Foundation.HRESULT = -2146697201
INET_E_CANNOT_INSTANTIATE_OBJECT: Windows.Win32.Foundation.HRESULT = -2146697200
INET_E_INVALID_CERTIFICATE: Windows.Win32.Foundation.HRESULT = -2146697191
INET_E_REDIRECT_FAILED: Windows.Win32.Foundation.HRESULT = -2146697196
INET_E_REDIRECT_TO_DIR: Windows.Win32.Foundation.HRESULT = -2146697195
INET_E_CANNOT_LOCK_REQUEST: Windows.Win32.Foundation.HRESULT = -2146697194
INET_E_USE_EXTEND_BINDING: Windows.Win32.Foundation.HRESULT = -2146697193
INET_E_TERMINATED_BIND: Windows.Win32.Foundation.HRESULT = -2146697192
INET_E_RESERVED_1: Windows.Win32.Foundation.HRESULT = -2146697190
INET_E_BLOCKED_REDIRECT_XSECURITYID: Windows.Win32.Foundation.HRESULT = -2146697189
INET_E_DOMINJECTIONVALIDATION: Windows.Win32.Foundation.HRESULT = -2146697188
INET_E_VTAB_SWITCH_FORCE_ENGINE: Windows.Win32.Foundation.HRESULT = -2146697187
INET_E_HSTS_CERTIFICATE_ERROR: Windows.Win32.Foundation.HRESULT = -2146697186
INET_E_RESERVED_2: Windows.Win32.Foundation.HRESULT = -2146697185
INET_E_RESERVED_3: Windows.Win32.Foundation.HRESULT = -2146697184
INET_E_RESERVED_4: Windows.Win32.Foundation.HRESULT = -2146697183
INET_E_RESERVED_5: Windows.Win32.Foundation.HRESULT = -2146697182
INET_E_ERROR_FIRST: Windows.Win32.Foundation.HRESULT = -2146697214
INET_E_CODE_DOWNLOAD_DECLINED: Windows.Win32.Foundation.HRESULT = -2146696960
INET_E_RESULT_DISPATCHED: Windows.Win32.Foundation.HRESULT = -2146696704
INET_E_CANNOT_REPLACE_SFP_FILE: Windows.Win32.Foundation.HRESULT = -2146696448
INET_E_CODE_INSTALL_SUPPRESSED: Windows.Win32.Foundation.HRESULT = -2146696192
INET_E_CODE_INSTALL_BLOCKED_BY_HASH_POLICY: Windows.Win32.Foundation.HRESULT = -2146695936
INET_E_DOWNLOAD_BLOCKED_BY_INPRIVATE: Windows.Win32.Foundation.HRESULT = -2146695935
INET_E_CODE_INSTALL_BLOCKED_IMMERSIVE: Windows.Win32.Foundation.HRESULT = -2146695934
INET_E_FORBIDFRAMING: Windows.Win32.Foundation.HRESULT = -2146695933
INET_E_CODE_INSTALL_BLOCKED_ARM: Windows.Win32.Foundation.HRESULT = -2146695932
INET_E_BLOCKED_PLUGGABLE_PROTOCOL: Windows.Win32.Foundation.HRESULT = -2146695931
INET_E_BLOCKED_ENHANCEDPROTECTEDMODE: Windows.Win32.Foundation.HRESULT = -2146695930
INET_E_CODE_INSTALL_BLOCKED_BITNESS: Windows.Win32.Foundation.HRESULT = -2146695929
INET_E_DOWNLOAD_BLOCKED_BY_CSP: Windows.Win32.Foundation.HRESULT = -2146695928
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
INET_E_USE_DEFAULT_PROTOCOLHANDLER: Windows.Win32.Foundation.HRESULT = -2146697199
INET_E_USE_DEFAULT_SETTING: Windows.Win32.Foundation.HRESULT = -2146697198
INET_E_DEFAULT_ACTION: Int32 = -2146697199
INET_E_QUERYOPTION_UNKNOWN: Windows.Win32.Foundation.HRESULT = -2146697197
INET_E_REDIRECTING: Windows.Win32.Foundation.HRESULT = -2146697196
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
def CreateURLMoniker(pMkCtx: Windows.Win32.System.Com.IMoniker_head, szURL: Windows.Win32.Foundation.PWSTR, ppmk: POINTER(Windows.Win32.System.Com.IMoniker_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CreateURLMonikerEx(pMkCtx: Windows.Win32.System.Com.IMoniker_head, szURL: Windows.Win32.Foundation.PWSTR, ppmk: POINTER(Windows.Win32.System.Com.IMoniker_head), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def GetClassURL(szURL: Windows.Win32.Foundation.PWSTR, pClsID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CreateAsyncBindCtx(reserved: UInt32, pBSCb: Windows.Win32.System.Com.IBindStatusCallback_head, pEFetc: Windows.Win32.System.Com.IEnumFORMATETC_head, ppBC: POINTER(Windows.Win32.System.Com.IBindCtx_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CreateURLMonikerEx2(pMkCtx: Windows.Win32.System.Com.IMoniker_head, pUri: Windows.Win32.System.Com.IUri_head, ppmk: POINTER(Windows.Win32.System.Com.IMoniker_head), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CreateAsyncBindCtxEx(pbc: Windows.Win32.System.Com.IBindCtx_head, dwOptions: UInt32, pBSCb: Windows.Win32.System.Com.IBindStatusCallback_head, pEnum: Windows.Win32.System.Com.IEnumFORMATETC_head, ppBC: POINTER(Windows.Win32.System.Com.IBindCtx_head), reserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def MkParseDisplayNameEx(pbc: Windows.Win32.System.Com.IBindCtx_head, szDisplayName: Windows.Win32.Foundation.PWSTR, pchEaten: POINTER(UInt32), ppmk: POINTER(Windows.Win32.System.Com.IMoniker_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def RegisterBindStatusCallback(pBC: Windows.Win32.System.Com.IBindCtx_head, pBSCb: Windows.Win32.System.Com.IBindStatusCallback_head, ppBSCBPrev: POINTER(Windows.Win32.System.Com.IBindStatusCallback_head), dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def RevokeBindStatusCallback(pBC: Windows.Win32.System.Com.IBindCtx_head, pBSCb: Windows.Win32.System.Com.IBindStatusCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def GetClassFileOrMime(pBC: Windows.Win32.System.Com.IBindCtx_head, szFilename: Windows.Win32.Foundation.PWSTR, pBuffer: c_void_p, cbSize: UInt32, szMime: Windows.Win32.Foundation.PWSTR, dwReserved: UInt32, pclsid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def IsValidURL(pBC: Windows.Win32.System.Com.IBindCtx_head, szURL: Windows.Win32.Foundation.PWSTR, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoGetClassObjectFromURL(rCLASSID: POINTER(Guid), szCODE: Windows.Win32.Foundation.PWSTR, dwFileVersionMS: UInt32, dwFileVersionLS: UInt32, szTYPE: Windows.Win32.Foundation.PWSTR, pBindCtx: Windows.Win32.System.Com.IBindCtx_head, dwClsContext: Windows.Win32.System.Com.CLSCTX, pvReserved: c_void_p, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def IEInstallScope(pdwScope: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def FaultInIEFeature(hWnd: Windows.Win32.Foundation.HWND, pClassSpec: POINTER(Windows.Win32.System.Com.uCLSSPEC_head), pQuery: POINTER(Windows.Win32.System.Com.QUERYCONTEXT_head), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def GetComponentIDFromCLSSPEC(pClassspec: POINTER(Windows.Win32.System.Com.uCLSSPEC_head), ppszComponentID: POINTER(Windows.Win32.Foundation.PSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def IsAsyncMoniker(pmk: Windows.Win32.System.Com.IMoniker_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def RegisterMediaTypes(ctypes: UInt32, rgszTypes: POINTER(Windows.Win32.Foundation.PSTR), rgcfTypes: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def FindMediaType(rgszTypes: Windows.Win32.Foundation.PSTR, rgcfTypes: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CreateFormatEnumerator(cfmtetc: UInt32, rgfmtetc: POINTER(Windows.Win32.System.Com.FORMATETC_head), ppenumfmtetc: POINTER(Windows.Win32.System.Com.IEnumFORMATETC_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def RegisterFormatEnumerator(pBC: Windows.Win32.System.Com.IBindCtx_head, pEFetc: Windows.Win32.System.Com.IEnumFORMATETC_head, reserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def RevokeFormatEnumerator(pBC: Windows.Win32.System.Com.IBindCtx_head, pEFetc: Windows.Win32.System.Com.IEnumFORMATETC_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def RegisterMediaTypeClass(pBC: Windows.Win32.System.Com.IBindCtx_head, ctypes: UInt32, rgszTypes: POINTER(Windows.Win32.Foundation.PSTR), rgclsID: POINTER(Guid), reserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def FindMediaTypeClass(pBC: Windows.Win32.System.Com.IBindCtx_head, szType: Windows.Win32.Foundation.PSTR, pclsID: POINTER(Guid), reserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def UrlMkSetSessionOption(dwOption: UInt32, pBuffer: c_void_p, dwBufferLength: UInt32, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def UrlMkGetSessionOption(dwOption: UInt32, pBuffer: c_void_p, dwBufferLength: UInt32, pdwBufferLengthOut: POINTER(UInt32), dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def FindMimeFromData(pBC: Windows.Win32.System.Com.IBindCtx_head, pwzUrl: Windows.Win32.Foundation.PWSTR, pBuffer: c_void_p, cbSize: UInt32, pwzMimeProposed: Windows.Win32.Foundation.PWSTR, dwMimeFlags: UInt32, ppwzMimeOut: POINTER(Windows.Win32.Foundation.PWSTR), dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def ObtainUserAgentString(dwOption: UInt32, pszUAOut: Windows.Win32.Foundation.PSTR, cbSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CompareSecurityIds(pbSecurityId1: c_char_p_no, dwLen1: UInt32, pbSecurityId2: c_char_p_no, dwLen2: UInt32, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CompatFlagsFromClsid(pclsid: POINTER(Guid), pdwCompatFlags: POINTER(UInt32), pdwMiscStatusFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def SetAccessForIEAppContainer(hObject: Windows.Win32.Foundation.HANDLE, ieObjectType: Windows.Win32.System.Com.Urlmon.IEObjectType, dwAccessMask: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def HlinkSimpleNavigateToString(szTarget: Windows.Win32.Foundation.PWSTR, szLocation: Windows.Win32.Foundation.PWSTR, szTargetFrameName: Windows.Win32.Foundation.PWSTR, pUnk: Windows.Win32.System.Com.IUnknown_head, pbc: Windows.Win32.System.Com.IBindCtx_head, param5: Windows.Win32.System.Com.IBindStatusCallback_head, grfHLNF: UInt32, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def HlinkSimpleNavigateToMoniker(pmkTarget: Windows.Win32.System.Com.IMoniker_head, szLocation: Windows.Win32.Foundation.PWSTR, szTargetFrameName: Windows.Win32.Foundation.PWSTR, pUnk: Windows.Win32.System.Com.IUnknown_head, pbc: Windows.Win32.System.Com.IBindCtx_head, param5: Windows.Win32.System.Com.IBindStatusCallback_head, grfHLNF: UInt32, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def URLOpenStreamA(param0: Windows.Win32.System.Com.IUnknown_head, param1: Windows.Win32.Foundation.PSTR, param2: UInt32, param3: Windows.Win32.System.Com.IBindStatusCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def URLOpenStreamW(param0: Windows.Win32.System.Com.IUnknown_head, param1: Windows.Win32.Foundation.PWSTR, param2: UInt32, param3: Windows.Win32.System.Com.IBindStatusCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def URLOpenPullStreamA(param0: Windows.Win32.System.Com.IUnknown_head, param1: Windows.Win32.Foundation.PSTR, param2: UInt32, param3: Windows.Win32.System.Com.IBindStatusCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def URLOpenPullStreamW(param0: Windows.Win32.System.Com.IUnknown_head, param1: Windows.Win32.Foundation.PWSTR, param2: UInt32, param3: Windows.Win32.System.Com.IBindStatusCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def URLDownloadToFileA(param0: Windows.Win32.System.Com.IUnknown_head, param1: Windows.Win32.Foundation.PSTR, param2: Windows.Win32.Foundation.PSTR, param3: UInt32, param4: Windows.Win32.System.Com.IBindStatusCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def URLDownloadToFileW(param0: Windows.Win32.System.Com.IUnknown_head, param1: Windows.Win32.Foundation.PWSTR, param2: Windows.Win32.Foundation.PWSTR, param3: UInt32, param4: Windows.Win32.System.Com.IBindStatusCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def URLDownloadToCacheFileA(param0: Windows.Win32.System.Com.IUnknown_head, param1: Windows.Win32.Foundation.PSTR, param2: Windows.Win32.Foundation.PSTR, cchFileName: UInt32, param4: UInt32, param5: Windows.Win32.System.Com.IBindStatusCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def URLDownloadToCacheFileW(param0: Windows.Win32.System.Com.IUnknown_head, param1: Windows.Win32.Foundation.PWSTR, param2: Windows.Win32.Foundation.PWSTR, cchFileName: UInt32, param4: UInt32, param5: Windows.Win32.System.Com.IBindStatusCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def URLOpenBlockingStreamA(param0: Windows.Win32.System.Com.IUnknown_head, param1: Windows.Win32.Foundation.PSTR, param2: POINTER(Windows.Win32.System.Com.IStream_head), param3: UInt32, param4: Windows.Win32.System.Com.IBindStatusCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def URLOpenBlockingStreamW(param0: Windows.Win32.System.Com.IUnknown_head, param1: Windows.Win32.Foundation.PWSTR, param2: POINTER(Windows.Win32.System.Com.IStream_head), param3: UInt32, param4: Windows.Win32.System.Com.IBindStatusCallback_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def HlinkGoBack(pUnk: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def HlinkGoForward(pUnk: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def HlinkNavigateString(pUnk: Windows.Win32.System.Com.IUnknown_head, szTarget: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def HlinkNavigateMoniker(pUnk: Windows.Win32.System.Com.IUnknown_head, pmkTarget: Windows.Win32.System.Com.IMoniker_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetParseUrl(pwzUrl: Windows.Win32.Foundation.PWSTR, ParseAction: Windows.Win32.System.Com.Urlmon.PARSEACTION, dwFlags: UInt32, pszResult: Windows.Win32.Foundation.PWSTR, cchResult: UInt32, pcchResult: POINTER(UInt32), dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetParseIUri(pIUri: Windows.Win32.System.Com.IUri_head, ParseAction: Windows.Win32.System.Com.Urlmon.PARSEACTION, dwFlags: UInt32, pwzResult: Windows.Win32.Foundation.PWSTR, cchResult: UInt32, pcchResult: POINTER(UInt32), dwReserved: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetCombineUrl(pwzBaseUrl: Windows.Win32.Foundation.PWSTR, pwzRelativeUrl: Windows.Win32.Foundation.PWSTR, dwCombineFlags: UInt32, pszResult: Windows.Win32.Foundation.PWSTR, cchResult: UInt32, pcchResult: POINTER(UInt32), dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetCombineUrlEx(pBaseUri: Windows.Win32.System.Com.IUri_head, pwzRelativeUrl: Windows.Win32.Foundation.PWSTR, dwCombineFlags: UInt32, ppCombinedUri: POINTER(Windows.Win32.System.Com.IUri_head), dwReserved: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetCombineIUri(pBaseUri: Windows.Win32.System.Com.IUri_head, pRelativeUri: Windows.Win32.System.Com.IUri_head, dwCombineFlags: UInt32, ppCombinedUri: POINTER(Windows.Win32.System.Com.IUri_head), dwReserved: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetCompareUrl(pwzUrl1: Windows.Win32.Foundation.PWSTR, pwzUrl2: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetGetProtocolFlags(pwzUrl: Windows.Win32.Foundation.PWSTR, pdwFlags: POINTER(UInt32), dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetQueryInfo(pwzUrl: Windows.Win32.Foundation.PWSTR, QueryOptions: Windows.Win32.System.Com.Urlmon.QUERYOPTION, dwQueryFlags: UInt32, pvBuffer: c_void_p, cbBuffer: UInt32, pcbBuffer: POINTER(UInt32), dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetGetSession(dwSessionMode: UInt32, ppIInternetSession: POINTER(Windows.Win32.System.Com.Urlmon.IInternetSession_head), dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetGetSecurityUrl(pwszUrl: Windows.Win32.Foundation.PWSTR, ppwszSecUrl: POINTER(Windows.Win32.Foundation.PWSTR), psuAction: Windows.Win32.System.Com.Urlmon.PSUACTION, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetGetSecurityUrlEx(pUri: Windows.Win32.System.Com.IUri_head, ppSecUri: POINTER(Windows.Win32.System.Com.IUri_head), psuAction: Windows.Win32.System.Com.Urlmon.PSUACTION, dwReserved: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetSetFeatureEnabled(FeatureEntry: Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST, dwFlags: UInt32, fEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetIsFeatureEnabled(FeatureEntry: Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetIsFeatureEnabledForUrl(FeatureEntry: Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST, dwFlags: UInt32, szURL: Windows.Win32.Foundation.PWSTR, pSecMgr: Windows.Win32.System.Com.Urlmon.IInternetSecurityManager_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetIsFeatureEnabledForIUri(FeatureEntry: Windows.Win32.System.Com.Urlmon.INTERNETFEATURELIST, dwFlags: UInt32, pIUri: Windows.Win32.System.Com.IUri_head, pSecMgr: Windows.Win32.System.Com.Urlmon.IInternetSecurityManagerEx2_head) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetIsFeatureZoneElevationEnabled(szFromURL: Windows.Win32.Foundation.PWSTR, szToURL: Windows.Win32.Foundation.PWSTR, pSecMgr: Windows.Win32.System.Com.Urlmon.IInternetSecurityManager_head, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CopyStgMedium(pcstgmedSrc: POINTER(Windows.Win32.System.Com.STGMEDIUM_head), pstgmedDest: POINTER(Windows.Win32.System.Com.STGMEDIUM_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CopyBindInfo(pcbiSrc: POINTER(Windows.Win32.System.Com.BINDINFO_head), pbiDest: POINTER(Windows.Win32.System.Com.BINDINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def ReleaseBindInfo(pbindinfo: POINTER(Windows.Win32.System.Com.BINDINFO_head)) -> Void: ...
@winfunctype('urlmon.dll')
def IEGetUserPrivateNamespaceName() -> Windows.Win32.Foundation.PWSTR: ...
@winfunctype('urlmon.dll')
def CoInternetCreateSecurityManager(pSP: Windows.Win32.System.Com.IServiceProvider_head, ppSM: POINTER(Windows.Win32.System.Com.Urlmon.IInternetSecurityManager_head), dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def CoInternetCreateZoneManager(pSP: Windows.Win32.System.Com.IServiceProvider_head, ppZM: POINTER(Windows.Win32.System.Com.Urlmon.IInternetZoneManager_head), dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def GetSoftwareUpdateInfo(szDistUnit: Windows.Win32.Foundation.PWSTR, psdi: POINTER(Windows.Win32.System.Com.Urlmon.SOFTDISTINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def SetSoftwareUpdateAdvertisementState(szDistUnit: Windows.Win32.Foundation.PWSTR, dwAdState: UInt32, dwAdvertisedVersionMS: UInt32, dwAdvertisedVersionLS: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('urlmon.dll')
def IsLoggingEnabledA(pszUrl: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('urlmon.dll')
def IsLoggingEnabledW(pwszUrl: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('urlmon.dll')
def WriteHitLogging(lpLogginginfo: POINTER(Windows.Win32.System.Com.Urlmon.HIT_LOGGING_INFO_head)) -> Windows.Win32.Foundation.BOOL: ...
BINDF = Int32
BINDF_ASYNCHRONOUS: BINDF = 1
BINDF_ASYNCSTORAGE: BINDF = 2
BINDF_NOPROGRESSIVERENDERING: BINDF = 4
BINDF_OFFLINEOPERATION: BINDF = 8
BINDF_GETNEWESTVERSION: BINDF = 16
BINDF_NOWRITECACHE: BINDF = 32
BINDF_NEEDFILE: BINDF = 64
BINDF_PULLDATA: BINDF = 128
BINDF_IGNORESECURITYPROBLEM: BINDF = 256
BINDF_RESYNCHRONIZE: BINDF = 512
BINDF_HYPERLINK: BINDF = 1024
BINDF_NO_UI: BINDF = 2048
BINDF_SILENTOPERATION: BINDF = 4096
BINDF_PRAGMA_NO_CACHE: BINDF = 8192
BINDF_GETCLASSOBJECT: BINDF = 16384
BINDF_RESERVED_1: BINDF = 32768
BINDF_FREE_THREADED: BINDF = 65536
BINDF_DIRECT_READ: BINDF = 131072
BINDF_FORMS_SUBMIT: BINDF = 262144
BINDF_GETFROMCACHE_IF_NET_FAIL: BINDF = 524288
BINDF_FROMURLMON: BINDF = 1048576
BINDF_FWD_BACK: BINDF = 2097152
BINDF_PREFERDEFAULTHANDLER: BINDF = 4194304
BINDF_ENFORCERESTRICTED: BINDF = 8388608
BINDF_RESERVED_2: BINDF = -2147483648
BINDF_RESERVED_3: BINDF = 16777216
BINDF_RESERVED_4: BINDF = 33554432
BINDF_RESERVED_5: BINDF = 67108864
BINDF_RESERVED_6: BINDF = 134217728
BINDF_RESERVED_7: BINDF = 1073741824
BINDF_RESERVED_8: BINDF = 536870912
BINDF2 = Int32
BINDF2_DISABLEBASICOVERHTTP: BINDF2 = 1
BINDF2_DISABLEAUTOCOOKIEHANDLING: BINDF2 = 2
BINDF2_READ_DATA_GREATER_THAN_4GB: BINDF2 = 4
BINDF2_DISABLE_HTTP_REDIRECT_XSECURITYID: BINDF2 = 8
BINDF2_SETDOWNLOADMODE: BINDF2 = 32
BINDF2_DISABLE_HTTP_REDIRECT_CACHING: BINDF2 = 64
BINDF2_KEEP_CALLBACK_MODULE_LOADED: BINDF2 = 128
BINDF2_ALLOW_PROXY_CRED_PROMPT: BINDF2 = 256
BINDF2_RESERVED_17: BINDF2 = 512
BINDF2_RESERVED_16: BINDF2 = 1024
BINDF2_RESERVED_15: BINDF2 = 2048
BINDF2_RESERVED_14: BINDF2 = 4096
BINDF2_RESERVED_13: BINDF2 = 8192
BINDF2_RESERVED_12: BINDF2 = 16384
BINDF2_RESERVED_11: BINDF2 = 32768
BINDF2_RESERVED_10: BINDF2 = 65536
BINDF2_RESERVED_F: BINDF2 = 131072
BINDF2_RESERVED_E: BINDF2 = 262144
BINDF2_RESERVED_D: BINDF2 = 524288
BINDF2_RESERVED_C: BINDF2 = 1048576
BINDF2_RESERVED_B: BINDF2 = 2097152
BINDF2_RESERVED_A: BINDF2 = 4194304
BINDF2_RESERVED_9: BINDF2 = 8388608
BINDF2_RESERVED_8: BINDF2 = 16777216
BINDF2_RESERVED_7: BINDF2 = 33554432
BINDF2_RESERVED_6: BINDF2 = 67108864
BINDF2_RESERVED_5: BINDF2 = 134217728
BINDF2_RESERVED_4: BINDF2 = 268435456
BINDF2_RESERVED_3: BINDF2 = 536870912
BINDF2_RESERVED_2: BINDF2 = 1073741824
BINDF2_RESERVED_1: BINDF2 = -2147483648
BINDHANDLETYPES = Int32
BINDHANDLETYPES_APPCACHE: BINDHANDLETYPES = 0
BINDHANDLETYPES_DEPENDENCY: BINDHANDLETYPES = 1
BINDHANDLETYPES_COUNT: BINDHANDLETYPES = 2
BINDINFO_OPTIONS = Int32
BINDINFO_OPTIONS_WININETFLAG: BINDINFO_OPTIONS = 65536
BINDINFO_OPTIONS_ENABLE_UTF8: BINDINFO_OPTIONS = 131072
BINDINFO_OPTIONS_DISABLE_UTF8: BINDINFO_OPTIONS = 262144
BINDINFO_OPTIONS_USE_IE_ENCODING: BINDINFO_OPTIONS = 524288
BINDINFO_OPTIONS_BINDTOOBJECT: BINDINFO_OPTIONS = 1048576
BINDINFO_OPTIONS_SECURITYOPTOUT: BINDINFO_OPTIONS = 2097152
BINDINFO_OPTIONS_IGNOREMIMETEXTPLAIN: BINDINFO_OPTIONS = 4194304
BINDINFO_OPTIONS_USEBINDSTRINGCREDS: BINDINFO_OPTIONS = 8388608
BINDINFO_OPTIONS_IGNOREHTTPHTTPSREDIRECTS: BINDINFO_OPTIONS = 16777216
BINDINFO_OPTIONS_IGNORE_SSLERRORS_ONCE: BINDINFO_OPTIONS = 33554432
BINDINFO_WPC_DOWNLOADBLOCKED: BINDINFO_OPTIONS = 134217728
BINDINFO_WPC_LOGGING_ENABLED: BINDINFO_OPTIONS = 268435456
BINDINFO_OPTIONS_ALLOWCONNECTDATA: BINDINFO_OPTIONS = 536870912
BINDINFO_OPTIONS_DISABLEAUTOREDIRECTS: BINDINFO_OPTIONS = 1073741824
BINDINFO_OPTIONS_SHDOCVW_NAVIGATE: BINDINFO_OPTIONS = -2147483648
BINDSTATUS = Int32
BINDSTATUS_FINDINGRESOURCE: BINDSTATUS = 1
BINDSTATUS_CONNECTING: BINDSTATUS = 2
BINDSTATUS_REDIRECTING: BINDSTATUS = 3
BINDSTATUS_BEGINDOWNLOADDATA: BINDSTATUS = 4
BINDSTATUS_DOWNLOADINGDATA: BINDSTATUS = 5
BINDSTATUS_ENDDOWNLOADDATA: BINDSTATUS = 6
BINDSTATUS_BEGINDOWNLOADCOMPONENTS: BINDSTATUS = 7
BINDSTATUS_INSTALLINGCOMPONENTS: BINDSTATUS = 8
BINDSTATUS_ENDDOWNLOADCOMPONENTS: BINDSTATUS = 9
BINDSTATUS_USINGCACHEDCOPY: BINDSTATUS = 10
BINDSTATUS_SENDINGREQUEST: BINDSTATUS = 11
BINDSTATUS_CLASSIDAVAILABLE: BINDSTATUS = 12
BINDSTATUS_MIMETYPEAVAILABLE: BINDSTATUS = 13
BINDSTATUS_CACHEFILENAMEAVAILABLE: BINDSTATUS = 14
BINDSTATUS_BEGINSYNCOPERATION: BINDSTATUS = 15
BINDSTATUS_ENDSYNCOPERATION: BINDSTATUS = 16
BINDSTATUS_BEGINUPLOADDATA: BINDSTATUS = 17
BINDSTATUS_UPLOADINGDATA: BINDSTATUS = 18
BINDSTATUS_ENDUPLOADDATA: BINDSTATUS = 19
BINDSTATUS_PROTOCOLCLASSID: BINDSTATUS = 20
BINDSTATUS_ENCODING: BINDSTATUS = 21
BINDSTATUS_VERIFIEDMIMETYPEAVAILABLE: BINDSTATUS = 22
BINDSTATUS_CLASSINSTALLLOCATION: BINDSTATUS = 23
BINDSTATUS_DECODING: BINDSTATUS = 24
BINDSTATUS_LOADINGMIMEHANDLER: BINDSTATUS = 25
BINDSTATUS_CONTENTDISPOSITIONATTACH: BINDSTATUS = 26
BINDSTATUS_FILTERREPORTMIMETYPE: BINDSTATUS = 27
BINDSTATUS_CLSIDCANINSTANTIATE: BINDSTATUS = 28
BINDSTATUS_IUNKNOWNAVAILABLE: BINDSTATUS = 29
BINDSTATUS_DIRECTBIND: BINDSTATUS = 30
BINDSTATUS_RAWMIMETYPE: BINDSTATUS = 31
BINDSTATUS_PROXYDETECTING: BINDSTATUS = 32
BINDSTATUS_ACCEPTRANGES: BINDSTATUS = 33
BINDSTATUS_COOKIE_SENT: BINDSTATUS = 34
BINDSTATUS_COMPACT_POLICY_RECEIVED: BINDSTATUS = 35
BINDSTATUS_COOKIE_SUPPRESSED: BINDSTATUS = 36
BINDSTATUS_COOKIE_STATE_UNKNOWN: BINDSTATUS = 37
BINDSTATUS_COOKIE_STATE_ACCEPT: BINDSTATUS = 38
BINDSTATUS_COOKIE_STATE_REJECT: BINDSTATUS = 39
BINDSTATUS_COOKIE_STATE_PROMPT: BINDSTATUS = 40
BINDSTATUS_COOKIE_STATE_LEASH: BINDSTATUS = 41
BINDSTATUS_COOKIE_STATE_DOWNGRADE: BINDSTATUS = 42
BINDSTATUS_POLICY_HREF: BINDSTATUS = 43
BINDSTATUS_P3P_HEADER: BINDSTATUS = 44
BINDSTATUS_SESSION_COOKIE_RECEIVED: BINDSTATUS = 45
BINDSTATUS_PERSISTENT_COOKIE_RECEIVED: BINDSTATUS = 46
BINDSTATUS_SESSION_COOKIES_ALLOWED: BINDSTATUS = 47
BINDSTATUS_CACHECONTROL: BINDSTATUS = 48
BINDSTATUS_CONTENTDISPOSITIONFILENAME: BINDSTATUS = 49
BINDSTATUS_MIMETEXTPLAINMISMATCH: BINDSTATUS = 50
BINDSTATUS_PUBLISHERAVAILABLE: BINDSTATUS = 51
BINDSTATUS_DISPLAYNAMEAVAILABLE: BINDSTATUS = 52
BINDSTATUS_SSLUX_NAVBLOCKED: BINDSTATUS = 53
BINDSTATUS_SERVER_MIMETYPEAVAILABLE: BINDSTATUS = 54
BINDSTATUS_SNIFFED_CLASSIDAVAILABLE: BINDSTATUS = 55
BINDSTATUS_64BIT_PROGRESS: BINDSTATUS = 56
BINDSTATUS_LAST: BINDSTATUS = 56
BINDSTATUS_RESERVED_0: BINDSTATUS = 57
BINDSTATUS_RESERVED_1: BINDSTATUS = 58
BINDSTATUS_RESERVED_2: BINDSTATUS = 59
BINDSTATUS_RESERVED_3: BINDSTATUS = 60
BINDSTATUS_RESERVED_4: BINDSTATUS = 61
BINDSTATUS_RESERVED_5: BINDSTATUS = 62
BINDSTATUS_RESERVED_6: BINDSTATUS = 63
BINDSTATUS_RESERVED_7: BINDSTATUS = 64
BINDSTATUS_RESERVED_8: BINDSTATUS = 65
BINDSTATUS_RESERVED_9: BINDSTATUS = 66
BINDSTATUS_RESERVED_A: BINDSTATUS = 67
BINDSTATUS_RESERVED_B: BINDSTATUS = 68
BINDSTATUS_RESERVED_C: BINDSTATUS = 69
BINDSTATUS_RESERVED_D: BINDSTATUS = 70
BINDSTATUS_RESERVED_E: BINDSTATUS = 71
BINDSTATUS_RESERVED_F: BINDSTATUS = 72
BINDSTATUS_RESERVED_10: BINDSTATUS = 73
BINDSTATUS_RESERVED_11: BINDSTATUS = 74
BINDSTATUS_RESERVED_12: BINDSTATUS = 75
BINDSTATUS_RESERVED_13: BINDSTATUS = 76
BINDSTATUS_RESERVED_14: BINDSTATUS = 77
BINDSTATUS_LAST_PRIVATE: BINDSTATUS = 77
BINDSTRING = Int32
BINDSTRING_HEADERS: BINDSTRING = 1
BINDSTRING_ACCEPT_MIMES: BINDSTRING = 2
BINDSTRING_EXTRA_URL: BINDSTRING = 3
BINDSTRING_LANGUAGE: BINDSTRING = 4
BINDSTRING_USERNAME: BINDSTRING = 5
BINDSTRING_PASSWORD: BINDSTRING = 6
BINDSTRING_UA_PIXELS: BINDSTRING = 7
BINDSTRING_UA_COLOR: BINDSTRING = 8
BINDSTRING_OS: BINDSTRING = 9
BINDSTRING_USER_AGENT: BINDSTRING = 10
BINDSTRING_ACCEPT_ENCODINGS: BINDSTRING = 11
BINDSTRING_POST_COOKIE: BINDSTRING = 12
BINDSTRING_POST_DATA_MIME: BINDSTRING = 13
BINDSTRING_URL: BINDSTRING = 14
BINDSTRING_IID: BINDSTRING = 15
BINDSTRING_FLAG_BIND_TO_OBJECT: BINDSTRING = 16
BINDSTRING_PTR_BIND_CONTEXT: BINDSTRING = 17
BINDSTRING_XDR_ORIGIN: BINDSTRING = 18
BINDSTRING_DOWNLOADPATH: BINDSTRING = 19
BINDSTRING_ROOTDOC_URL: BINDSTRING = 20
BINDSTRING_INITIAL_FILENAME: BINDSTRING = 21
BINDSTRING_PROXY_USERNAME: BINDSTRING = 22
BINDSTRING_PROXY_PASSWORD: BINDSTRING = 23
BINDSTRING_ENTERPRISE_ID: BINDSTRING = 24
BINDSTRING_DOC_URL: BINDSTRING = 25
BINDSTRING_SAMESITE_COOKIE_LEVEL: BINDSTRING = 26
BINDVERB = Int32
BINDVERB_GET: BINDVERB = 0
BINDVERB_POST: BINDVERB = 1
BINDVERB_PUT: BINDVERB = 2
BINDVERB_CUSTOM: BINDVERB = 3
BINDVERB_RESERVED1: BINDVERB = 4
BSCF = Int32
BSCF_FIRSTDATANOTIFICATION: BSCF = 1
BSCF_INTERMEDIATEDATANOTIFICATION: BSCF = 2
BSCF_LASTDATANOTIFICATION: BSCF = 4
BSCF_DATAFULLYAVAILABLE: BSCF = 8
BSCF_AVAILABLEDATASIZEUNKNOWN: BSCF = 16
BSCF_SKIPDRAINDATAFORFILEURLS: BSCF = 32
BSCF_64BITLENGTHDOWNLOAD: BSCF = 64
CIP_STATUS = Int32
CIP_DISK_FULL: CIP_STATUS = 0
CIP_ACCESS_DENIED: CIP_STATUS = 1
CIP_NEWER_VERSION_EXISTS: CIP_STATUS = 2
CIP_OLDER_VERSION_EXISTS: CIP_STATUS = 3
CIP_NAME_CONFLICT: CIP_STATUS = 4
CIP_TRUST_VERIFICATION_COMPONENT_MISSING: CIP_STATUS = 5
CIP_EXE_SELF_REGISTERATION_TIMEOUT: CIP_STATUS = 6
CIP_UNSAFE_TO_ABORT: CIP_STATUS = 7
CIP_NEED_REBOOT: CIP_STATUS = 8
CIP_NEED_REBOOT_UI_PERMISSION: CIP_STATUS = 9
class CODEBASEHOLD(Structure):
    cbSize: UInt32
    szDistUnit: Windows.Win32.Foundation.PWSTR
    szCodeBase: Windows.Win32.Foundation.PWSTR
    dwVersionMS: UInt32
    dwVersionLS: UInt32
    dwStyle: UInt32
class CONFIRMSAFETY(Structure):
    clsid: Guid
    pUnk: Windows.Win32.System.Com.IUnknown_head
    dwFlags: UInt32
class DATAINFO(Structure):
    ulTotalSize: UInt32
    ulavrPacketSize: UInt32
    ulConnectSpeed: UInt32
    ulProcessorSpeed: UInt32
class HIT_LOGGING_INFO(Structure):
    dwStructSize: UInt32
    lpszLoggedUrlName: Windows.Win32.Foundation.PSTR
    StartTime: Windows.Win32.Foundation.SYSTEMTIME
    EndTime: Windows.Win32.Foundation.SYSTEMTIME
    lpszExtendedInfo: Windows.Win32.Foundation.PSTR
class IBindCallbackRedirect(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('11c81bc2-121e-4ed5-b9-c4-b4-30-bd-54-f2-c0')
    @commethod(3)
    def Redirect(lpcUrl: Windows.Win32.Foundation.PWSTR, vbCancel: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IBindHttpSecurity(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a9eda967-f50e-4a33-b3-58-20-6f-6e-f3-08-6d')
    @commethod(3)
    def GetIgnoreCertMask(pdwIgnoreCertMask: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IBindProtocol(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('79eac9cd-baf9-11ce-8c-82-00-aa-00-4b-a9-0b')
    @commethod(3)
    def CreateBinding(szUrl: Windows.Win32.Foundation.PWSTR, pbc: Windows.Win32.System.Com.IBindCtx_head, ppb: POINTER(Windows.Win32.System.Com.IBinding_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ICatalogFileInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('711c7600-6b48-11d1-b4-03-00-aa-00-b9-2a-f1')
    @commethod(3)
    def GetCatalogFile(ppszCatalogFile: POINTER(Windows.Win32.Foundation.PSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetJavaTrust(ppJavaTrust: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class ICodeInstall(c_void_p):
    extends: Windows.Win32.System.Com.Urlmon.IWindowForBindingUI
    Guid = Guid('79eac9d1-baf9-11ce-8c-82-00-aa-00-4b-a9-0b')
    @commethod(4)
    def OnCodeInstallProblem(ulStatusCode: UInt32, szDestination: Windows.Win32.Foundation.PWSTR, szSource: Windows.Win32.Foundation.PWSTR, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IDataFilter(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('69d14c80-c18e-11d0-a9-ce-00-60-97-94-23-11')
    @commethod(3)
    def DoEncode(dwFlags: UInt32, lInBufferSize: Int32, pbInBuffer: c_char_p_no, lOutBufferSize: Int32, pbOutBuffer: c_char_p_no, lInBytesAvailable: Int32, plInBytesRead: POINTER(Int32), plOutBytesWritten: POINTER(Int32), dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def DoDecode(dwFlags: UInt32, lInBufferSize: Int32, pbInBuffer: c_char_p_no, lOutBufferSize: Int32, pbOutBuffer: c_char_p_no, lInBytesAvailable: Int32, plInBytesRead: POINTER(Int32), plOutBytesWritten: POINTER(Int32), dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetEncodingLevel(dwEncLevel: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
IEObjectType = Int32
IE_EPM_OBJECT_EVENT: IEObjectType = 0
IE_EPM_OBJECT_MUTEX: IEObjectType = 1
IE_EPM_OBJECT_SEMAPHORE: IEObjectType = 2
IE_EPM_OBJECT_SHARED_MEMORY: IEObjectType = 3
IE_EPM_OBJECT_WAITABLE_TIMER: IEObjectType = 4
IE_EPM_OBJECT_FILE: IEObjectType = 5
IE_EPM_OBJECT_NAMED_PIPE: IEObjectType = 6
IE_EPM_OBJECT_REGISTRY: IEObjectType = 7
class IEncodingFilterFactory(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('70bdde00-c18e-11d0-a9-ce-00-60-97-94-23-11')
    @commethod(3)
    def FindBestFilter(pwzCodeIn: Windows.Win32.Foundation.PWSTR, pwzCodeOut: Windows.Win32.Foundation.PWSTR, info: Windows.Win32.System.Com.Urlmon.DATAINFO, ppDF: POINTER(Windows.Win32.System.Com.Urlmon.IDataFilter_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDefaultFilter(pwzCodeIn: Windows.Win32.Foundation.PWSTR, pwzCodeOut: Windows.Win32.Foundation.PWSTR, ppDF: POINTER(Windows.Win32.System.Com.Urlmon.IDataFilter_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IGetBindHandle(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('af0ff408-129d-4b20-91-f0-02-bd-23-d8-83-52')
    @commethod(3)
    def GetBindHandle(enumRequestedHandle: Windows.Win32.System.Com.Urlmon.BINDHANDLETYPES, pRetHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
class IHttpNegotiate(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('79eac9d2-baf9-11ce-8c-82-00-aa-00-4b-a9-0b')
    @commethod(3)
    def BeginningTransaction(szURL: Windows.Win32.Foundation.PWSTR, szHeaders: Windows.Win32.Foundation.PWSTR, dwReserved: UInt32, pszAdditionalHeaders: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnResponse(dwResponseCode: UInt32, szResponseHeaders: Windows.Win32.Foundation.PWSTR, szRequestHeaders: Windows.Win32.Foundation.PWSTR, pszAdditionalRequestHeaders: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IHttpNegotiate2(c_void_p):
    extends: Windows.Win32.System.Com.Urlmon.IHttpNegotiate
    Guid = Guid('4f9f9fcb-e0f4-48eb-b7-ab-fa-2e-a9-36-5c-b4')
    @commethod(5)
    def GetRootSecurityId(pbSecurityId: c_char_p_no, pcbSecurityId: POINTER(UInt32), dwReserved: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
class IHttpNegotiate3(c_void_p):
    extends: Windows.Win32.System.Com.Urlmon.IHttpNegotiate2
    Guid = Guid('57b6c80a-34c2-4602-bc-26-66-a0-2f-c5-71-53')
    @commethod(6)
    def GetSerializedClientCertContext(ppbCert: POINTER(c_char_p_no), pcbCert: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IHttpSecurity(c_void_p):
    extends: Windows.Win32.System.Com.Urlmon.IWindowForBindingUI
    Guid = Guid('79eac9d7-bafa-11ce-8c-82-00-aa-00-4b-a9-0b')
    @commethod(4)
    def OnSecurityProblem(dwProblem: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IInternet(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('79eac9e0-baf9-11ce-8c-82-00-aa-00-4b-a9-0b')
class IInternetBindInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('79eac9e1-baf9-11ce-8c-82-00-aa-00-4b-a9-0b')
    @commethod(3)
    def GetBindInfo(grfBINDF: POINTER(UInt32), pbindinfo: POINTER(Windows.Win32.System.Com.BINDINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetBindString(ulStringType: UInt32, ppwzStr: POINTER(Windows.Win32.Foundation.PWSTR), cEl: UInt32, pcElFetched: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IInternetBindInfoEx(c_void_p):
    extends: Windows.Win32.System.Com.Urlmon.IInternetBindInfo
    Guid = Guid('a3e015b7-a82c-4dcd-a1-50-56-9a-ee-ed-36-ab')
    @commethod(5)
    def GetBindInfoEx(grfBINDF: POINTER(UInt32), pbindinfo: POINTER(Windows.Win32.System.Com.BINDINFO_head), grfBINDF2: POINTER(UInt32), pdwReserved: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IInternetHostSecurityManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('3af280b6-cb3f-11d0-89-1e-00-c0-4f-b6-bf-c4')
    @commethod(3)
    def GetSecurityId(pbSecurityId: c_char_p_no, pcbSecurityId: POINTER(UInt32), dwReserved: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ProcessUrlAction(dwAction: UInt32, pPolicy: c_char_p_no, cbPolicy: UInt32, pContext: c_char_p_no, cbContext: UInt32, dwFlags: UInt32, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def QueryCustomPolicy(guidKey: POINTER(Guid), ppPolicy: POINTER(c_char_p_no), pcbPolicy: POINTER(UInt32), pContext: c_char_p_no, cbContext: UInt32, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IInternetPriority(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('79eac9eb-baf9-11ce-8c-82-00-aa-00-4b-a9-0b')
    @commethod(3)
    def SetPriority(nPriority: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPriority(pnPriority: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IInternetProtocol(c_void_p):
    extends: Windows.Win32.System.Com.Urlmon.IInternetProtocolRoot
    Guid = Guid('79eac9e4-baf9-11ce-8c-82-00-aa-00-4b-a9-0b')
    @commethod(9)
    def Read(pv: c_void_p, cb: UInt32, pcbRead: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Seek(dlibMove: Int64, dwOrigin: UInt32, plibNewPosition: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def LockRequest(dwOptions: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def UnlockRequest() -> Windows.Win32.Foundation.HRESULT: ...
class IInternetProtocolEx(c_void_p):
    extends: Windows.Win32.System.Com.Urlmon.IInternetProtocol
    Guid = Guid('c7a98e66-1010-492c-a1-c8-c8-09-e1-f7-59-05')
    @commethod(13)
    def StartEx(pUri: Windows.Win32.System.Com.IUri_head, pOIProtSink: Windows.Win32.System.Com.Urlmon.IInternetProtocolSink_head, pOIBindInfo: Windows.Win32.System.Com.Urlmon.IInternetBindInfo_head, grfPI: UInt32, dwReserved: Windows.Win32.Foundation.HANDLE_PTR) -> Windows.Win32.Foundation.HRESULT: ...
class IInternetProtocolInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('79eac9ec-baf9-11ce-8c-82-00-aa-00-4b-a9-0b')
    @commethod(3)
    def ParseUrl(pwzUrl: Windows.Win32.Foundation.PWSTR, ParseAction: Windows.Win32.System.Com.Urlmon.PARSEACTION, dwParseFlags: UInt32, pwzResult: Windows.Win32.Foundation.PWSTR, cchResult: UInt32, pcchResult: POINTER(UInt32), dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CombineUrl(pwzBaseUrl: Windows.Win32.Foundation.PWSTR, pwzRelativeUrl: Windows.Win32.Foundation.PWSTR, dwCombineFlags: UInt32, pwzResult: Windows.Win32.Foundation.PWSTR, cchResult: UInt32, pcchResult: POINTER(UInt32), dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CompareUrl(pwzUrl1: Windows.Win32.Foundation.PWSTR, pwzUrl2: Windows.Win32.Foundation.PWSTR, dwCompareFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def QueryInfo(pwzUrl: Windows.Win32.Foundation.PWSTR, OueryOption: Windows.Win32.System.Com.Urlmon.QUERYOPTION, dwQueryFlags: UInt32, pBuffer: c_void_p, cbBuffer: UInt32, pcbBuf: POINTER(UInt32), dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IInternetProtocolRoot(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('79eac9e3-baf9-11ce-8c-82-00-aa-00-4b-a9-0b')
    @commethod(3)
    def Start(szUrl: Windows.Win32.Foundation.PWSTR, pOIProtSink: Windows.Win32.System.Com.Urlmon.IInternetProtocolSink_head, pOIBindInfo: Windows.Win32.System.Com.Urlmon.IInternetBindInfo_head, grfPI: UInt32, dwReserved: Windows.Win32.Foundation.HANDLE_PTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Continue(pProtocolData: POINTER(Windows.Win32.System.Com.Urlmon.PROTOCOLDATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Abort(hrReason: Windows.Win32.Foundation.HRESULT, dwOptions: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Terminate(dwOptions: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Suspend() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Resume() -> Windows.Win32.Foundation.HRESULT: ...
class IInternetProtocolSink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('79eac9e5-baf9-11ce-8c-82-00-aa-00-4b-a9-0b')
    @commethod(3)
    def Switch(pProtocolData: POINTER(Windows.Win32.System.Com.Urlmon.PROTOCOLDATA_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReportProgress(ulStatusCode: UInt32, szStatusText: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ReportData(grfBSCF: UInt32, ulProgress: UInt32, ulProgressMax: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ReportResult(hrResult: Windows.Win32.Foundation.HRESULT, dwError: UInt32, szResult: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IInternetProtocolSinkStackable(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('79eac9f0-baf9-11ce-8c-82-00-aa-00-4b-a9-0b')
    @commethod(3)
    def SwitchSink(pOIProtSink: Windows.Win32.System.Com.Urlmon.IInternetProtocolSink_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CommitSwitch() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RollbackSwitch() -> Windows.Win32.Foundation.HRESULT: ...
class IInternetSecurityManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('79eac9ee-baf9-11ce-8c-82-00-aa-00-4b-a9-0b')
    @commethod(3)
    def SetSecuritySite(pSite: Windows.Win32.System.Com.Urlmon.IInternetSecurityMgrSite_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSecuritySite(ppSite: POINTER(Windows.Win32.System.Com.Urlmon.IInternetSecurityMgrSite_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MapUrlToZone(pwszUrl: Windows.Win32.Foundation.PWSTR, pdwZone: POINTER(UInt32), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSecurityId(pwszUrl: Windows.Win32.Foundation.PWSTR, pbSecurityId: c_char_p_no, pcbSecurityId: POINTER(UInt32), dwReserved: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ProcessUrlAction(pwszUrl: Windows.Win32.Foundation.PWSTR, dwAction: UInt32, pPolicy: c_char_p_no, cbPolicy: UInt32, pContext: c_char_p_no, cbContext: UInt32, dwFlags: UInt32, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def QueryCustomPolicy(pwszUrl: Windows.Win32.Foundation.PWSTR, guidKey: POINTER(Guid), ppPolicy: POINTER(c_char_p_no), pcbPolicy: POINTER(UInt32), pContext: c_char_p_no, cbContext: UInt32, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetZoneMapping(dwZone: UInt32, lpszPattern: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetZoneMappings(dwZone: UInt32, ppenumString: POINTER(Windows.Win32.System.Com.IEnumString_head), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IInternetSecurityManagerEx(c_void_p):
    extends: Windows.Win32.System.Com.Urlmon.IInternetSecurityManager
    Guid = Guid('f164edf1-cc7c-4f0d-9a-94-34-22-26-25-c3-93')
    @commethod(11)
    def ProcessUrlActionEx(pwszUrl: Windows.Win32.Foundation.PWSTR, dwAction: UInt32, pPolicy: c_char_p_no, cbPolicy: UInt32, pContext: c_char_p_no, cbContext: UInt32, dwFlags: UInt32, dwReserved: UInt32, pdwOutFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IInternetSecurityManagerEx2(c_void_p):
    extends: Windows.Win32.System.Com.Urlmon.IInternetSecurityManagerEx
    Guid = Guid('f1e50292-a795-4117-8e-09-2b-56-0a-72-ac-60')
    @commethod(12)
    def MapUrlToZoneEx2(pUri: Windows.Win32.System.Com.IUri_head, pdwZone: POINTER(UInt32), dwFlags: UInt32, ppwszMappedUrl: POINTER(Windows.Win32.Foundation.PWSTR), pdwOutFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def ProcessUrlActionEx2(pUri: Windows.Win32.System.Com.IUri_head, dwAction: UInt32, pPolicy: c_char_p_no, cbPolicy: UInt32, pContext: c_char_p_no, cbContext: UInt32, dwFlags: UInt32, dwReserved: UIntPtr, pdwOutFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetSecurityIdEx2(pUri: Windows.Win32.System.Com.IUri_head, pbSecurityId: c_char_p_no, pcbSecurityId: POINTER(UInt32), dwReserved: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def QueryCustomPolicyEx2(pUri: Windows.Win32.System.Com.IUri_head, guidKey: POINTER(Guid), ppPolicy: POINTER(c_char_p_no), pcbPolicy: POINTER(UInt32), pContext: c_char_p_no, cbContext: UInt32, dwReserved: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
class IInternetSecurityMgrSite(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('79eac9ed-baf9-11ce-8c-82-00-aa-00-4b-a9-0b')
    @commethod(3)
    def GetWindow(phwnd: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnableModeless(fEnable: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IInternetSession(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('79eac9e7-baf9-11ce-8c-82-00-aa-00-4b-a9-0b')
    @commethod(3)
    def RegisterNameSpace(pCF: Windows.Win32.System.Com.IClassFactory_head, rclsid: POINTER(Guid), pwzProtocol: Windows.Win32.Foundation.PWSTR, cPatterns: UInt32, ppwzPatterns: POINTER(Windows.Win32.Foundation.PWSTR), dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterNameSpace(pCF: Windows.Win32.System.Com.IClassFactory_head, pszProtocol: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RegisterMimeFilter(pCF: Windows.Win32.System.Com.IClassFactory_head, rclsid: POINTER(Guid), pwzType: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def UnregisterMimeFilter(pCF: Windows.Win32.System.Com.IClassFactory_head, pwzType: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateBinding(pBC: Windows.Win32.System.Com.IBindCtx_head, szUrl: Windows.Win32.Foundation.PWSTR, pUnkOuter: Windows.Win32.System.Com.IUnknown_head, ppUnk: POINTER(Windows.Win32.System.Com.IUnknown_head), ppOInetProt: POINTER(Windows.Win32.System.Com.Urlmon.IInternetProtocol_head), dwOption: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetSessionOption(dwOption: UInt32, pBuffer: c_void_p, dwBufferLength: UInt32, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSessionOption(dwOption: UInt32, pBuffer: c_void_p, pdwBufferLength: POINTER(UInt32), dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IInternetThreadSwitch(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('79eac9e8-baf9-11ce-8c-82-00-aa-00-4b-a9-0b')
    @commethod(3)
    def Prepare() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Continue() -> Windows.Win32.Foundation.HRESULT: ...
class IInternetZoneManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('79eac9ef-baf9-11ce-8c-82-00-aa-00-4b-a9-0b')
    @commethod(3)
    def GetZoneAttributes(dwZone: UInt32, pZoneAttributes: POINTER(Windows.Win32.System.Com.Urlmon.ZONEATTRIBUTES_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetZoneAttributes(dwZone: UInt32, pZoneAttributes: POINTER(Windows.Win32.System.Com.Urlmon.ZONEATTRIBUTES_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetZoneCustomPolicy(dwZone: UInt32, guidKey: POINTER(Guid), ppPolicy: POINTER(c_char_p_no), pcbPolicy: POINTER(UInt32), urlZoneReg: Windows.Win32.System.Com.Urlmon.URLZONEREG) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetZoneCustomPolicy(dwZone: UInt32, guidKey: POINTER(Guid), pPolicy: c_char_p_no, cbPolicy: UInt32, urlZoneReg: Windows.Win32.System.Com.Urlmon.URLZONEREG) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetZoneActionPolicy(dwZone: UInt32, dwAction: UInt32, pPolicy: c_char_p_no, cbPolicy: UInt32, urlZoneReg: Windows.Win32.System.Com.Urlmon.URLZONEREG) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetZoneActionPolicy(dwZone: UInt32, dwAction: UInt32, pPolicy: c_char_p_no, cbPolicy: UInt32, urlZoneReg: Windows.Win32.System.Com.Urlmon.URLZONEREG) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def PromptAction(dwAction: UInt32, hwndParent: Windows.Win32.Foundation.HWND, pwszUrl: Windows.Win32.Foundation.PWSTR, pwszText: Windows.Win32.Foundation.PWSTR, dwPromptFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def LogAction(dwAction: UInt32, pwszUrl: Windows.Win32.Foundation.PWSTR, pwszText: Windows.Win32.Foundation.PWSTR, dwLogFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def CreateZoneEnumerator(pdwEnum: POINTER(UInt32), pdwCount: POINTER(UInt32), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetZoneAt(dwEnum: UInt32, dwIndex: UInt32, pdwZone: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def DestroyZoneEnumerator(dwEnum: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def CopyTemplatePoliciesToZone(dwTemplate: UInt32, dwZone: UInt32, dwReserved: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IInternetZoneManagerEx(c_void_p):
    extends: Windows.Win32.System.Com.Urlmon.IInternetZoneManager
    Guid = Guid('a4c23339-8e06-431e-9b-f4-7e-71-1c-08-56-48')
    @commethod(15)
    def GetZoneActionPolicyEx(dwZone: UInt32, dwAction: UInt32, pPolicy: c_char_p_no, cbPolicy: UInt32, urlZoneReg: Windows.Win32.System.Com.Urlmon.URLZONEREG, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetZoneActionPolicyEx(dwZone: UInt32, dwAction: UInt32, pPolicy: c_char_p_no, cbPolicy: UInt32, urlZoneReg: Windows.Win32.System.Com.Urlmon.URLZONEREG, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IInternetZoneManagerEx2(c_void_p):
    extends: Windows.Win32.System.Com.Urlmon.IInternetZoneManagerEx
    Guid = Guid('edc17559-dd5d-4846-8e-ef-8b-ec-ba-5a-4a-bf')
    @commethod(17)
    def GetZoneAttributesEx(dwZone: UInt32, pZoneAttributes: POINTER(Windows.Win32.System.Com.Urlmon.ZONEATTRIBUTES_head), dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetZoneSecurityState(dwZoneIndex: UInt32, fRespectPolicy: Windows.Win32.Foundation.BOOL, pdwState: POINTER(UInt32), pfPolicyEncountered: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetIESecurityState(fRespectPolicy: Windows.Win32.Foundation.BOOL, pdwState: POINTER(UInt32), pfPolicyEncountered: POINTER(Windows.Win32.Foundation.BOOL), fNoCache: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def FixUnsecureSettings() -> Windows.Win32.Foundation.HRESULT: ...
class IMonikerProp(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a5ca5f7f-1847-4d87-9c-5b-91-85-09-f7-51-1d')
    @commethod(3)
    def PutProperty(mkp: Windows.Win32.System.Com.Urlmon.MONIKERPROPERTY, val: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
INET_ZONE_MANAGER_CONSTANTS = Int32
MAX_ZONE_PATH: INET_ZONE_MANAGER_CONSTANTS = 260
MAX_ZONE_DESCRIPTION: INET_ZONE_MANAGER_CONSTANTS = 200
INTERNETFEATURELIST = Int32
FEATURE_OBJECT_CACHING: INTERNETFEATURELIST = 0
FEATURE_ZONE_ELEVATION: INTERNETFEATURELIST = 1
FEATURE_MIME_HANDLING: INTERNETFEATURELIST = 2
FEATURE_MIME_SNIFFING: INTERNETFEATURELIST = 3
FEATURE_WINDOW_RESTRICTIONS: INTERNETFEATURELIST = 4
FEATURE_WEBOC_POPUPMANAGEMENT: INTERNETFEATURELIST = 5
FEATURE_BEHAVIORS: INTERNETFEATURELIST = 6
FEATURE_DISABLE_MK_PROTOCOL: INTERNETFEATURELIST = 7
FEATURE_LOCALMACHINE_LOCKDOWN: INTERNETFEATURELIST = 8
FEATURE_SECURITYBAND: INTERNETFEATURELIST = 9
FEATURE_RESTRICT_ACTIVEXINSTALL: INTERNETFEATURELIST = 10
FEATURE_VALIDATE_NAVIGATE_URL: INTERNETFEATURELIST = 11
FEATURE_RESTRICT_FILEDOWNLOAD: INTERNETFEATURELIST = 12
FEATURE_ADDON_MANAGEMENT: INTERNETFEATURELIST = 13
FEATURE_PROTOCOL_LOCKDOWN: INTERNETFEATURELIST = 14
FEATURE_HTTP_USERNAME_PASSWORD_DISABLE: INTERNETFEATURELIST = 15
FEATURE_SAFE_BINDTOOBJECT: INTERNETFEATURELIST = 16
FEATURE_UNC_SAVEDFILECHECK: INTERNETFEATURELIST = 17
FEATURE_GET_URL_DOM_FILEPATH_UNENCODED: INTERNETFEATURELIST = 18
FEATURE_TABBED_BROWSING: INTERNETFEATURELIST = 19
FEATURE_SSLUX: INTERNETFEATURELIST = 20
FEATURE_DISABLE_NAVIGATION_SOUNDS: INTERNETFEATURELIST = 21
FEATURE_DISABLE_LEGACY_COMPRESSION: INTERNETFEATURELIST = 22
FEATURE_FORCE_ADDR_AND_STATUS: INTERNETFEATURELIST = 23
FEATURE_XMLHTTP: INTERNETFEATURELIST = 24
FEATURE_DISABLE_TELNET_PROTOCOL: INTERNETFEATURELIST = 25
FEATURE_FEEDS: INTERNETFEATURELIST = 26
FEATURE_BLOCK_INPUT_PROMPTS: INTERNETFEATURELIST = 27
FEATURE_ENTRY_COUNT: INTERNETFEATURELIST = 28
class IPersistMoniker(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('79eac9c9-baf9-11ce-8c-82-00-aa-00-4b-a9-0b')
    @commethod(3)
    def GetClassID(pClassID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def IsDirty() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Load(fFullyAvailable: Windows.Win32.Foundation.BOOL, pimkName: Windows.Win32.System.Com.IMoniker_head, pibc: Windows.Win32.System.Com.IBindCtx_head, grfMode: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Save(pimkName: Windows.Win32.System.Com.IMoniker_head, pbc: Windows.Win32.System.Com.IBindCtx_head, fRemember: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SaveCompleted(pimkName: Windows.Win32.System.Com.IMoniker_head, pibc: Windows.Win32.System.Com.IBindCtx_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetCurMoniker(ppimkName: POINTER(Windows.Win32.System.Com.IMoniker_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISoftDistExt(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b15b8dc1-c7e1-11d0-86-80-00-aa-00-bd-cb-71')
    @commethod(3)
    def ProcessSoftDist(szCDFURL: Windows.Win32.Foundation.PWSTR, pSoftDistElement: Windows.Win32.Data.Xml.MsXml.IXMLElement_head, lpsdi: POINTER(Windows.Win32.System.Com.Urlmon.SOFTDISTINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFirstCodeBase(szCodeBase: POINTER(Windows.Win32.Foundation.PWSTR), dwMaxSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetNextCodeBase(szCodeBase: POINTER(Windows.Win32.Foundation.PWSTR), dwMaxSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AsyncInstallDistributionUnit(pbc: Windows.Win32.System.Com.IBindCtx_head, pvReserved: c_void_p, flags: UInt32, lpcbh: POINTER(Windows.Win32.System.Com.Urlmon.CODEBASEHOLD_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUriBuilderFactory(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e982ce48-0b96-440c-bc-37-0c-86-9b-27-a2-9e')
    @commethod(3)
    def CreateIUriBuilder(dwFlags: UInt32, dwReserved: UIntPtr, ppIUriBuilder: POINTER(Windows.Win32.System.Com.IUriBuilder_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateInitializedIUriBuilder(dwFlags: UInt32, dwReserved: UIntPtr, ppIUriBuilder: POINTER(Windows.Win32.System.Com.IUriBuilder_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IUriContainer(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a158a630-ed6f-45fb-b9-87-f6-86-76-f5-77-52')
    @commethod(3)
    def GetIUri(ppIUri: POINTER(Windows.Win32.System.Com.IUri_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWinInetCacheHints(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('dd1ec3b3-8391-4fdb-a9-e6-34-7c-3c-aa-a7-dd')
    @commethod(3)
    def SetCacheExtension(pwzExt: Windows.Win32.Foundation.PWSTR, pszCacheFile: c_void_p, pcbCacheFile: POINTER(UInt32), pdwWinInetError: POINTER(UInt32), pdwReserved: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWinInetCacheHints2(c_void_p):
    extends: Windows.Win32.System.Com.Urlmon.IWinInetCacheHints
    Guid = Guid('7857aeac-d31f-49bf-88-4e-dd-46-df-36-78-0a')
    @commethod(4)
    def SetCacheExtension2(pwzExt: Windows.Win32.Foundation.PWSTR, pwzCacheFile: Windows.Win32.Foundation.PWSTR, pcchCacheFile: POINTER(UInt32), pdwWinInetError: POINTER(UInt32), pdwReserved: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWinInetFileStream(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f134c4b7-b1f8-4e75-b8-86-74-b9-09-43-be-cb')
    @commethod(3)
    def SetHandleForUnlock(hWinInetLockHandle: UIntPtr, dwReserved: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetDeleteFile(dwReserved: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
class IWinInetHttpInfo(c_void_p):
    extends: Windows.Win32.System.Com.Urlmon.IWinInetInfo
    Guid = Guid('79eac9d8-bafa-11ce-8c-82-00-aa-00-4b-a9-0b')
    @commethod(4)
    def QueryInfo(dwOption: UInt32, pBuffer: c_void_p, pcbBuf: POINTER(UInt32), pdwFlags: POINTER(UInt32), pdwReserved: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWinInetHttpTimeouts(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f286fa56-c1fd-4270-8e-67-b3-eb-79-0a-81-e8')
    @commethod(3)
    def GetRequestTimeouts(pdwConnectTimeout: POINTER(UInt32), pdwSendTimeout: POINTER(UInt32), pdwReceiveTimeout: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWinInetInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('79eac9d6-bafa-11ce-8c-82-00-aa-00-4b-a9-0b')
    @commethod(3)
    def QueryOption(dwOption: UInt32, pBuffer: c_void_p, pcbBuf: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWindowForBindingUI(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('79eac9d5-bafa-11ce-8c-82-00-aa-00-4b-a9-0b')
    @commethod(3)
    def GetWindow(rguidReason: POINTER(Guid), phwnd: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
class IWrappedProtocol(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('53c84785-8425-4dc5-97-1b-e5-8d-9c-19-f9-b6')
    @commethod(3)
    def GetWrapperCode(pnCode: POINTER(Int32), dwReserved: UIntPtr) -> Windows.Win32.Foundation.HRESULT: ...
class IZoneIdentifier(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('cd45f185-1b21-48e2-96-7b-ea-d7-43-a8-91-4e')
    @commethod(3)
    def GetId(pdwZone: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetId(dwZone: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Remove() -> Windows.Win32.Foundation.HRESULT: ...
class IZoneIdentifier2(c_void_p):
    extends: Windows.Win32.System.Com.Urlmon.IZoneIdentifier
    Guid = Guid('eb5e760c-09ef-45c0-b5-10-70-83-0c-e3-1e-6a')
    @commethod(6)
    def GetLastWriterPackageFamilyName(packageFamilyName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetLastWriterPackageFamilyName(packageFamilyName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RemoveLastWriterPackageFamilyName() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetAppZoneId(zone: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetAppZoneId(zone: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def RemoveAppZoneId() -> Windows.Win32.Foundation.HRESULT: ...
MONIKERPROPERTY = Int32
MIMETYPEPROP: MONIKERPROPERTY = 0
USE_SRC_URL: MONIKERPROPERTY = 1
CLASSIDPROP: MONIKERPROPERTY = 2
TRUSTEDDOWNLOADPROP: MONIKERPROPERTY = 3
POPUPLEVELPROP: MONIKERPROPERTY = 4
OIBDG_FLAGS = Int32
OIBDG_APARTMENTTHREADED: OIBDG_FLAGS = 256
OIBDG_DATAONLY: OIBDG_FLAGS = 4096
PARSEACTION = Int32
PARSE_CANONICALIZE: PARSEACTION = 1
PARSE_FRIENDLY: PARSEACTION = 2
PARSE_SECURITY_URL: PARSEACTION = 3
PARSE_ROOTDOCUMENT: PARSEACTION = 4
PARSE_DOCUMENT: PARSEACTION = 5
PARSE_ANCHOR: PARSEACTION = 6
PARSE_ENCODE_IS_UNESCAPE: PARSEACTION = 7
PARSE_DECODE_IS_ESCAPE: PARSEACTION = 8
PARSE_PATH_FROM_URL: PARSEACTION = 9
PARSE_URL_FROM_PATH: PARSEACTION = 10
PARSE_MIME: PARSEACTION = 11
PARSE_SERVER: PARSEACTION = 12
PARSE_SCHEMA: PARSEACTION = 13
PARSE_SITE: PARSEACTION = 14
PARSE_DOMAIN: PARSEACTION = 15
PARSE_LOCATION: PARSEACTION = 16
PARSE_SECURITY_DOMAIN: PARSEACTION = 17
PARSE_ESCAPE: PARSEACTION = 18
PARSE_UNESCAPE: PARSEACTION = 19
PI_FLAGS = Int32
PI_PARSE_URL: PI_FLAGS = 1
PI_FILTER_MODE: PI_FLAGS = 2
PI_FORCE_ASYNC: PI_FLAGS = 4
PI_USE_WORKERTHREAD: PI_FLAGS = 8
PI_MIMEVERIFICATION: PI_FLAGS = 16
PI_CLSIDLOOKUP: PI_FLAGS = 32
PI_DATAPROGRESS: PI_FLAGS = 64
PI_SYNCHRONOUS: PI_FLAGS = 128
PI_APARTMENTTHREADED: PI_FLAGS = 256
PI_CLASSINSTALL: PI_FLAGS = 512
PI_PASSONBINDCTX: PI_FLAGS = 8192
PI_NOMIMEHANDLER: PI_FLAGS = 32768
PI_LOADAPPDIRECT: PI_FLAGS = 16384
PD_FORCE_SWITCH: PI_FLAGS = 65536
PI_PREFERDEFAULTHANDLER: PI_FLAGS = 131072
class PROTOCOLDATA(Structure):
    grfFlags: UInt32
    dwState: UInt32
    pData: c_void_p
    cbData: UInt32
class PROTOCOLFILTERDATA(Structure):
    cbSize: UInt32
    pProtocolSink: Windows.Win32.System.Com.Urlmon.IInternetProtocolSink_head
    pProtocol: Windows.Win32.System.Com.Urlmon.IInternetProtocol_head
    pUnk: Windows.Win32.System.Com.IUnknown_head
    dwFilterFlags: UInt32
class PROTOCOL_ARGUMENT(Structure):
    szMethod: Windows.Win32.Foundation.PWSTR
    szTargetUrl: Windows.Win32.Foundation.PWSTR
PSUACTION = Int32
PSU_DEFAULT: PSUACTION = 1
PSU_SECURITY_URL_ONLY: PSUACTION = 2
PUAF = Int32
PUAF_DEFAULT: PUAF = 0
PUAF_NOUI: PUAF = 1
PUAF_ISFILE: PUAF = 2
PUAF_WARN_IF_DENIED: PUAF = 4
PUAF_FORCEUI_FOREGROUND: PUAF = 8
PUAF_CHECK_TIFS: PUAF = 16
PUAF_DONTCHECKBOXINDIALOG: PUAF = 32
PUAF_TRUSTED: PUAF = 64
PUAF_ACCEPT_WILDCARD_SCHEME: PUAF = 128
PUAF_ENFORCERESTRICTED: PUAF = 256
PUAF_NOSAVEDFILECHECK: PUAF = 512
PUAF_REQUIRESAVEDFILECHECK: PUAF = 1024
PUAF_DONT_USE_CACHE: PUAF = 4096
PUAF_RESERVED1: PUAF = 8192
PUAF_RESERVED2: PUAF = 16384
PUAF_LMZ_UNLOCKED: PUAF = 65536
PUAF_LMZ_LOCKED: PUAF = 131072
PUAF_DEFAULTZONEPOL: PUAF = 262144
PUAF_NPL_USE_LOCKED_IF_RESTRICTED: PUAF = 524288
PUAF_NOUIIFLOCKED: PUAF = 1048576
PUAF_DRAGPROTOCOLCHECK: PUAF = 2097152
PUAFOUT = Int32
PUAFOUT_DEFAULT: PUAFOUT = 0
PUAFOUT_ISLOCKZONEPOLICY: PUAFOUT = 1
QUERYOPTION = Int32
QUERY_EXPIRATION_DATE: QUERYOPTION = 1
QUERY_TIME_OF_LAST_CHANGE: QUERYOPTION = 2
QUERY_CONTENT_ENCODING: QUERYOPTION = 3
QUERY_CONTENT_TYPE: QUERYOPTION = 4
QUERY_REFRESH: QUERYOPTION = 5
QUERY_RECOMBINE: QUERYOPTION = 6
QUERY_CAN_NAVIGATE: QUERYOPTION = 7
QUERY_USES_NETWORK: QUERYOPTION = 8
QUERY_IS_CACHED: QUERYOPTION = 9
QUERY_IS_INSTALLEDENTRY: QUERYOPTION = 10
QUERY_IS_CACHED_OR_MAPPED: QUERYOPTION = 11
QUERY_USES_CACHE: QUERYOPTION = 12
QUERY_IS_SECURE: QUERYOPTION = 13
QUERY_IS_SAFE: QUERYOPTION = 14
QUERY_USES_HISTORYFOLDER: QUERYOPTION = 15
QUERY_IS_CACHED_AND_USABLE_OFFLINE: QUERYOPTION = 16
class REMSECURITY_ATTRIBUTES(Structure):
    nLength: UInt32
    lpSecurityDescriptor: UInt32
    bInheritHandle: Windows.Win32.Foundation.BOOL
class RemBINDINFO(Structure):
    cbSize: UInt32
    szExtraInfo: Windows.Win32.Foundation.PWSTR
    grfBindInfoF: UInt32
    dwBindVerb: UInt32
    szCustomVerb: Windows.Win32.Foundation.PWSTR
    cbstgmedData: UInt32
    dwOptions: UInt32
    dwOptionsFlags: UInt32
    dwCodePage: UInt32
    securityAttributes: Windows.Win32.System.Com.Urlmon.REMSECURITY_ATTRIBUTES
    iid: Guid
    pUnk: Windows.Win32.System.Com.IUnknown_head
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
    szTitle: Windows.Win32.Foundation.PWSTR
    szAbstract: Windows.Win32.Foundation.PWSTR
    szHREF: Windows.Win32.Foundation.PWSTR
    dwInstalledVersionMS: UInt32
    dwInstalledVersionLS: UInt32
    dwUpdateVersionMS: UInt32
    dwUpdateVersionLS: UInt32
    dwAdvertisedVersionMS: UInt32
    dwAdvertisedVersionLS: UInt32
    dwReserved: UInt32
SZM_FLAGS = Int32
SZM_CREATE: SZM_FLAGS = 0
SZM_DELETE: SZM_FLAGS = 1
class StartParam(Structure):
    iid: Guid
    pIBindCtx: Windows.Win32.System.Com.IBindCtx_head
    pItf: Windows.Win32.System.Com.IUnknown_head
URLTEMPLATE = Int32
URLTEMPLATE_CUSTOM: URLTEMPLATE = 0
URLTEMPLATE_PREDEFINED_MIN: URLTEMPLATE = 65536
URLTEMPLATE_LOW: URLTEMPLATE = 65536
URLTEMPLATE_MEDLOW: URLTEMPLATE = 66816
URLTEMPLATE_MEDIUM: URLTEMPLATE = 69632
URLTEMPLATE_MEDHIGH: URLTEMPLATE = 70912
URLTEMPLATE_HIGH: URLTEMPLATE = 73728
URLTEMPLATE_PREDEFINED_MAX: URLTEMPLATE = 131072
URLZONE = Int32
URLZONE_INVALID: URLZONE = -1
URLZONE_PREDEFINED_MIN: URLZONE = 0
URLZONE_LOCAL_MACHINE: URLZONE = 0
URLZONE_INTRANET: URLZONE = 1
URLZONE_TRUSTED: URLZONE = 2
URLZONE_INTERNET: URLZONE = 3
URLZONE_UNTRUSTED: URLZONE = 4
URLZONE_PREDEFINED_MAX: URLZONE = 999
URLZONE_USER_MIN: URLZONE = 1000
URLZONE_USER_MAX: URLZONE = 10000
URLZONEREG = Int32
URLZONEREG_DEFAULT: URLZONEREG = 0
URLZONEREG_HKLM: URLZONEREG = 1
URLZONEREG_HKCU: URLZONEREG = 2
URL_ENCODING = Int32
URL_ENCODING_NONE: URL_ENCODING = 0
URL_ENCODING_ENABLE_UTF8: URL_ENCODING = 268435456
URL_ENCODING_DISABLE_UTF8: URL_ENCODING = 536870912
Uri_HOST_TYPE = Int32
Uri_HOST_UNKNOWN: Uri_HOST_TYPE = 0
Uri_HOST_DNS: Uri_HOST_TYPE = 1
Uri_HOST_IPV4: Uri_HOST_TYPE = 2
Uri_HOST_IPV6: Uri_HOST_TYPE = 3
Uri_HOST_IDN: Uri_HOST_TYPE = 4
ZAFLAGS = Int32
ZAFLAGS_CUSTOM_EDIT: ZAFLAGS = 1
ZAFLAGS_ADD_SITES: ZAFLAGS = 2
ZAFLAGS_REQUIRE_VERIFICATION: ZAFLAGS = 4
ZAFLAGS_INCLUDE_PROXY_OVERRIDE: ZAFLAGS = 8
ZAFLAGS_INCLUDE_INTRANET_SITES: ZAFLAGS = 16
ZAFLAGS_NO_UI: ZAFLAGS = 32
ZAFLAGS_SUPPORTS_VERIFICATION: ZAFLAGS = 64
ZAFLAGS_UNC_AS_INTRANET: ZAFLAGS = 128
ZAFLAGS_DETECT_INTRANET: ZAFLAGS = 256
ZAFLAGS_USE_LOCKED_ZONES: ZAFLAGS = 65536
ZAFLAGS_VERIFY_TEMPLATE_SETTINGS: ZAFLAGS = 131072
ZAFLAGS_NO_CACHE: ZAFLAGS = 262144
class ZONEATTRIBUTES(Structure):
    cbSize: UInt32
    szDisplayName: Char * 260
    szDescription: Char * 200
    szIconPath: Char * 260
    dwTemplateMinLevel: UInt32
    dwTemplateRecommended: UInt32
    dwTemplateCurrentLevel: UInt32
    dwFlags: UInt32
make_head(_module, 'CODEBASEHOLD')
make_head(_module, 'CONFIRMSAFETY')
make_head(_module, 'DATAINFO')
make_head(_module, 'HIT_LOGGING_INFO')
make_head(_module, 'IBindCallbackRedirect')
make_head(_module, 'IBindHttpSecurity')
make_head(_module, 'IBindProtocol')
make_head(_module, 'ICatalogFileInfo')
make_head(_module, 'ICodeInstall')
make_head(_module, 'IDataFilter')
make_head(_module, 'IEncodingFilterFactory')
make_head(_module, 'IGetBindHandle')
make_head(_module, 'IHttpNegotiate')
make_head(_module, 'IHttpNegotiate2')
make_head(_module, 'IHttpNegotiate3')
make_head(_module, 'IHttpSecurity')
make_head(_module, 'IInternet')
make_head(_module, 'IInternetBindInfo')
make_head(_module, 'IInternetBindInfoEx')
make_head(_module, 'IInternetHostSecurityManager')
make_head(_module, 'IInternetPriority')
make_head(_module, 'IInternetProtocol')
make_head(_module, 'IInternetProtocolEx')
make_head(_module, 'IInternetProtocolInfo')
make_head(_module, 'IInternetProtocolRoot')
make_head(_module, 'IInternetProtocolSink')
make_head(_module, 'IInternetProtocolSinkStackable')
make_head(_module, 'IInternetSecurityManager')
make_head(_module, 'IInternetSecurityManagerEx')
make_head(_module, 'IInternetSecurityManagerEx2')
make_head(_module, 'IInternetSecurityMgrSite')
make_head(_module, 'IInternetSession')
make_head(_module, 'IInternetThreadSwitch')
make_head(_module, 'IInternetZoneManager')
make_head(_module, 'IInternetZoneManagerEx')
make_head(_module, 'IInternetZoneManagerEx2')
make_head(_module, 'IMonikerProp')
make_head(_module, 'IPersistMoniker')
make_head(_module, 'ISoftDistExt')
make_head(_module, 'IUriBuilderFactory')
make_head(_module, 'IUriContainer')
make_head(_module, 'IWinInetCacheHints')
make_head(_module, 'IWinInetCacheHints2')
make_head(_module, 'IWinInetFileStream')
make_head(_module, 'IWinInetHttpInfo')
make_head(_module, 'IWinInetHttpTimeouts')
make_head(_module, 'IWinInetInfo')
make_head(_module, 'IWindowForBindingUI')
make_head(_module, 'IWrappedProtocol')
make_head(_module, 'IZoneIdentifier')
make_head(_module, 'IZoneIdentifier2')
make_head(_module, 'PROTOCOLDATA')
make_head(_module, 'PROTOCOLFILTERDATA')
make_head(_module, 'PROTOCOL_ARGUMENT')
make_head(_module, 'REMSECURITY_ATTRIBUTES')
make_head(_module, 'RemBINDINFO')
make_head(_module, 'RemFORMATETC')
make_head(_module, 'SOFTDISTINFO')
make_head(_module, 'StartParam')
make_head(_module, 'ZONEATTRIBUTES')
__all__ = [
    "AUTHENTICATEF",
    "AUTHENTICATEF_BASIC",
    "AUTHENTICATEF_HTTP",
    "AUTHENTICATEF_PROXY",
    "BINDF",
    "BINDF2",
    "BINDF2_ALLOW_PROXY_CRED_PROMPT",
    "BINDF2_DISABLEAUTOCOOKIEHANDLING",
    "BINDF2_DISABLEBASICOVERHTTP",
    "BINDF2_DISABLE_HTTP_REDIRECT_CACHING",
    "BINDF2_DISABLE_HTTP_REDIRECT_XSECURITYID",
    "BINDF2_KEEP_CALLBACK_MODULE_LOADED",
    "BINDF2_READ_DATA_GREATER_THAN_4GB",
    "BINDF2_RESERVED_1",
    "BINDF2_RESERVED_10",
    "BINDF2_RESERVED_11",
    "BINDF2_RESERVED_12",
    "BINDF2_RESERVED_13",
    "BINDF2_RESERVED_14",
    "BINDF2_RESERVED_15",
    "BINDF2_RESERVED_16",
    "BINDF2_RESERVED_17",
    "BINDF2_RESERVED_2",
    "BINDF2_RESERVED_3",
    "BINDF2_RESERVED_4",
    "BINDF2_RESERVED_5",
    "BINDF2_RESERVED_6",
    "BINDF2_RESERVED_7",
    "BINDF2_RESERVED_8",
    "BINDF2_RESERVED_9",
    "BINDF2_RESERVED_A",
    "BINDF2_RESERVED_B",
    "BINDF2_RESERVED_C",
    "BINDF2_RESERVED_D",
    "BINDF2_RESERVED_E",
    "BINDF2_RESERVED_F",
    "BINDF2_SETDOWNLOADMODE",
    "BINDF_ASYNCHRONOUS",
    "BINDF_ASYNCSTORAGE",
    "BINDF_DIRECT_READ",
    "BINDF_ENFORCERESTRICTED",
    "BINDF_FORMS_SUBMIT",
    "BINDF_FREE_THREADED",
    "BINDF_FROMURLMON",
    "BINDF_FWD_BACK",
    "BINDF_GETCLASSOBJECT",
    "BINDF_GETFROMCACHE_IF_NET_FAIL",
    "BINDF_GETNEWESTVERSION",
    "BINDF_HYPERLINK",
    "BINDF_IGNORESECURITYPROBLEM",
    "BINDF_NEEDFILE",
    "BINDF_NOPROGRESSIVERENDERING",
    "BINDF_NOWRITECACHE",
    "BINDF_NO_UI",
    "BINDF_OFFLINEOPERATION",
    "BINDF_PRAGMA_NO_CACHE",
    "BINDF_PREFERDEFAULTHANDLER",
    "BINDF_PULLDATA",
    "BINDF_RESERVED_1",
    "BINDF_RESERVED_2",
    "BINDF_RESERVED_3",
    "BINDF_RESERVED_4",
    "BINDF_RESERVED_5",
    "BINDF_RESERVED_6",
    "BINDF_RESERVED_7",
    "BINDF_RESERVED_8",
    "BINDF_RESYNCHRONIZE",
    "BINDF_SILENTOPERATION",
    "BINDHANDLETYPES",
    "BINDHANDLETYPES_APPCACHE",
    "BINDHANDLETYPES_COUNT",
    "BINDHANDLETYPES_DEPENDENCY",
    "BINDINFO_OPTIONS",
    "BINDINFO_OPTIONS_ALLOWCONNECTDATA",
    "BINDINFO_OPTIONS_BINDTOOBJECT",
    "BINDINFO_OPTIONS_DISABLEAUTOREDIRECTS",
    "BINDINFO_OPTIONS_DISABLE_UTF8",
    "BINDINFO_OPTIONS_ENABLE_UTF8",
    "BINDINFO_OPTIONS_IGNOREHTTPHTTPSREDIRECTS",
    "BINDINFO_OPTIONS_IGNOREMIMETEXTPLAIN",
    "BINDINFO_OPTIONS_IGNORE_SSLERRORS_ONCE",
    "BINDINFO_OPTIONS_SECURITYOPTOUT",
    "BINDINFO_OPTIONS_SHDOCVW_NAVIGATE",
    "BINDINFO_OPTIONS_USEBINDSTRINGCREDS",
    "BINDINFO_OPTIONS_USE_IE_ENCODING",
    "BINDINFO_OPTIONS_WININETFLAG",
    "BINDINFO_WPC_DOWNLOADBLOCKED",
    "BINDINFO_WPC_LOGGING_ENABLED",
    "BINDSTATUS",
    "BINDSTATUS_64BIT_PROGRESS",
    "BINDSTATUS_ACCEPTRANGES",
    "BINDSTATUS_BEGINDOWNLOADCOMPONENTS",
    "BINDSTATUS_BEGINDOWNLOADDATA",
    "BINDSTATUS_BEGINSYNCOPERATION",
    "BINDSTATUS_BEGINUPLOADDATA",
    "BINDSTATUS_CACHECONTROL",
    "BINDSTATUS_CACHEFILENAMEAVAILABLE",
    "BINDSTATUS_CLASSIDAVAILABLE",
    "BINDSTATUS_CLASSINSTALLLOCATION",
    "BINDSTATUS_CLSIDCANINSTANTIATE",
    "BINDSTATUS_COMPACT_POLICY_RECEIVED",
    "BINDSTATUS_CONNECTING",
    "BINDSTATUS_CONTENTDISPOSITIONATTACH",
    "BINDSTATUS_CONTENTDISPOSITIONFILENAME",
    "BINDSTATUS_COOKIE_SENT",
    "BINDSTATUS_COOKIE_STATE_ACCEPT",
    "BINDSTATUS_COOKIE_STATE_DOWNGRADE",
    "BINDSTATUS_COOKIE_STATE_LEASH",
    "BINDSTATUS_COOKIE_STATE_PROMPT",
    "BINDSTATUS_COOKIE_STATE_REJECT",
    "BINDSTATUS_COOKIE_STATE_UNKNOWN",
    "BINDSTATUS_COOKIE_SUPPRESSED",
    "BINDSTATUS_DECODING",
    "BINDSTATUS_DIRECTBIND",
    "BINDSTATUS_DISPLAYNAMEAVAILABLE",
    "BINDSTATUS_DOWNLOADINGDATA",
    "BINDSTATUS_ENCODING",
    "BINDSTATUS_ENDDOWNLOADCOMPONENTS",
    "BINDSTATUS_ENDDOWNLOADDATA",
    "BINDSTATUS_ENDSYNCOPERATION",
    "BINDSTATUS_ENDUPLOADDATA",
    "BINDSTATUS_FILTERREPORTMIMETYPE",
    "BINDSTATUS_FINDINGRESOURCE",
    "BINDSTATUS_INSTALLINGCOMPONENTS",
    "BINDSTATUS_IUNKNOWNAVAILABLE",
    "BINDSTATUS_LAST",
    "BINDSTATUS_LAST_PRIVATE",
    "BINDSTATUS_LOADINGMIMEHANDLER",
    "BINDSTATUS_MIMETEXTPLAINMISMATCH",
    "BINDSTATUS_MIMETYPEAVAILABLE",
    "BINDSTATUS_P3P_HEADER",
    "BINDSTATUS_PERSISTENT_COOKIE_RECEIVED",
    "BINDSTATUS_POLICY_HREF",
    "BINDSTATUS_PROTOCOLCLASSID",
    "BINDSTATUS_PROXYDETECTING",
    "BINDSTATUS_PUBLISHERAVAILABLE",
    "BINDSTATUS_RAWMIMETYPE",
    "BINDSTATUS_REDIRECTING",
    "BINDSTATUS_RESERVED_0",
    "BINDSTATUS_RESERVED_1",
    "BINDSTATUS_RESERVED_10",
    "BINDSTATUS_RESERVED_11",
    "BINDSTATUS_RESERVED_12",
    "BINDSTATUS_RESERVED_13",
    "BINDSTATUS_RESERVED_14",
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
    "BINDSTATUS_SENDINGREQUEST",
    "BINDSTATUS_SERVER_MIMETYPEAVAILABLE",
    "BINDSTATUS_SESSION_COOKIES_ALLOWED",
    "BINDSTATUS_SESSION_COOKIE_RECEIVED",
    "BINDSTATUS_SNIFFED_CLASSIDAVAILABLE",
    "BINDSTATUS_SSLUX_NAVBLOCKED",
    "BINDSTATUS_UPLOADINGDATA",
    "BINDSTATUS_USINGCACHEDCOPY",
    "BINDSTATUS_VERIFIEDMIMETYPEAVAILABLE",
    "BINDSTRING",
    "BINDSTRING_ACCEPT_ENCODINGS",
    "BINDSTRING_ACCEPT_MIMES",
    "BINDSTRING_DOC_URL",
    "BINDSTRING_DOWNLOADPATH",
    "BINDSTRING_ENTERPRISE_ID",
    "BINDSTRING_EXTRA_URL",
    "BINDSTRING_FLAG_BIND_TO_OBJECT",
    "BINDSTRING_HEADERS",
    "BINDSTRING_IID",
    "BINDSTRING_INITIAL_FILENAME",
    "BINDSTRING_LANGUAGE",
    "BINDSTRING_OS",
    "BINDSTRING_PASSWORD",
    "BINDSTRING_POST_COOKIE",
    "BINDSTRING_POST_DATA_MIME",
    "BINDSTRING_PROXY_PASSWORD",
    "BINDSTRING_PROXY_USERNAME",
    "BINDSTRING_PTR_BIND_CONTEXT",
    "BINDSTRING_ROOTDOC_URL",
    "BINDSTRING_SAMESITE_COOKIE_LEVEL",
    "BINDSTRING_UA_COLOR",
    "BINDSTRING_UA_PIXELS",
    "BINDSTRING_URL",
    "BINDSTRING_USERNAME",
    "BINDSTRING_USER_AGENT",
    "BINDSTRING_XDR_ORIGIN",
    "BINDVERB",
    "BINDVERB_CUSTOM",
    "BINDVERB_GET",
    "BINDVERB_POST",
    "BINDVERB_PUT",
    "BINDVERB_RESERVED1",
    "BSCF",
    "BSCF_64BITLENGTHDOWNLOAD",
    "BSCF_AVAILABLEDATASIZEUNKNOWN",
    "BSCF_DATAFULLYAVAILABLE",
    "BSCF_FIRSTDATANOTIFICATION",
    "BSCF_INTERMEDIATEDATANOTIFICATION",
    "BSCF_LASTDATANOTIFICATION",
    "BSCF_SKIPDRAINDATAFORFILEURLS",
    "CF_NULL",
    "CIP_ACCESS_DENIED",
    "CIP_DISK_FULL",
    "CIP_EXE_SELF_REGISTERATION_TIMEOUT",
    "CIP_NAME_CONFLICT",
    "CIP_NEED_REBOOT",
    "CIP_NEED_REBOOT_UI_PERMISSION",
    "CIP_NEWER_VERSION_EXISTS",
    "CIP_OLDER_VERSION_EXISTS",
    "CIP_STATUS",
    "CIP_TRUST_VERIFICATION_COMPONENT_MISSING",
    "CIP_UNSAFE_TO_ABORT",
    "CLASSIDPROP",
    "CODEBASEHOLD",
    "CONFIRMSAFETY",
    "CONFIRMSAFETYACTION_LOADOBJECT",
    "CoGetClassObjectFromURL",
    "CoInternetCombineIUri",
    "CoInternetCombineUrl",
    "CoInternetCombineUrlEx",
    "CoInternetCompareUrl",
    "CoInternetCreateSecurityManager",
    "CoInternetCreateZoneManager",
    "CoInternetGetProtocolFlags",
    "CoInternetGetSecurityUrl",
    "CoInternetGetSecurityUrlEx",
    "CoInternetGetSession",
    "CoInternetIsFeatureEnabled",
    "CoInternetIsFeatureEnabledForIUri",
    "CoInternetIsFeatureEnabledForUrl",
    "CoInternetIsFeatureZoneElevationEnabled",
    "CoInternetParseIUri",
    "CoInternetParseUrl",
    "CoInternetQueryInfo",
    "CoInternetSetFeatureEnabled",
    "CompareSecurityIds",
    "CompatFlagsFromClsid",
    "CopyBindInfo",
    "CopyStgMedium",
    "CreateAsyncBindCtx",
    "CreateAsyncBindCtxEx",
    "CreateFormatEnumerator",
    "CreateURLMoniker",
    "CreateURLMonikerEx",
    "CreateURLMonikerEx2",
    "DATAINFO",
    "E_PENDING",
    "FEATURE_ADDON_MANAGEMENT",
    "FEATURE_BEHAVIORS",
    "FEATURE_BLOCK_INPUT_PROMPTS",
    "FEATURE_DISABLE_LEGACY_COMPRESSION",
    "FEATURE_DISABLE_MK_PROTOCOL",
    "FEATURE_DISABLE_NAVIGATION_SOUNDS",
    "FEATURE_DISABLE_TELNET_PROTOCOL",
    "FEATURE_ENTRY_COUNT",
    "FEATURE_FEEDS",
    "FEATURE_FORCE_ADDR_AND_STATUS",
    "FEATURE_GET_URL_DOM_FILEPATH_UNENCODED",
    "FEATURE_HTTP_USERNAME_PASSWORD_DISABLE",
    "FEATURE_LOCALMACHINE_LOCKDOWN",
    "FEATURE_MIME_HANDLING",
    "FEATURE_MIME_SNIFFING",
    "FEATURE_OBJECT_CACHING",
    "FEATURE_PROTOCOL_LOCKDOWN",
    "FEATURE_RESTRICT_ACTIVEXINSTALL",
    "FEATURE_RESTRICT_FILEDOWNLOAD",
    "FEATURE_SAFE_BINDTOOBJECT",
    "FEATURE_SECURITYBAND",
    "FEATURE_SSLUX",
    "FEATURE_TABBED_BROWSING",
    "FEATURE_UNC_SAVEDFILECHECK",
    "FEATURE_VALIDATE_NAVIGATE_URL",
    "FEATURE_WEBOC_POPUPMANAGEMENT",
    "FEATURE_WINDOW_RESTRICTIONS",
    "FEATURE_XMLHTTP",
    "FEATURE_ZONE_ELEVATION",
    "FIEF_FLAG_FORCE_JITUI",
    "FIEF_FLAG_PEEK",
    "FIEF_FLAG_RESERVED_0",
    "FIEF_FLAG_SKIP_INSTALLED_VERSION_CHECK",
    "FMFD_DEFAULT",
    "FMFD_ENABLEMIMESNIFFING",
    "FMFD_IGNOREMIMETEXTPLAIN",
    "FMFD_RESERVED_1",
    "FMFD_RESERVED_2",
    "FMFD_RESPECTTEXTPLAIN",
    "FMFD_RETURNUPDATEDIMGMIMES",
    "FMFD_SERVERMIME",
    "FMFD_URLASFILENAME",
    "FaultInIEFeature",
    "FindMediaType",
    "FindMediaTypeClass",
    "FindMimeFromData",
    "GET_FEATURE_FROM_PROCESS",
    "GET_FEATURE_FROM_REGISTRY",
    "GET_FEATURE_FROM_THREAD",
    "GET_FEATURE_FROM_THREAD_INTERNET",
    "GET_FEATURE_FROM_THREAD_INTRANET",
    "GET_FEATURE_FROM_THREAD_LOCALMACHINE",
    "GET_FEATURE_FROM_THREAD_RESTRICTED",
    "GET_FEATURE_FROM_THREAD_TRUSTED",
    "GetClassFileOrMime",
    "GetClassURL",
    "GetComponentIDFromCLSSPEC",
    "GetSoftwareUpdateInfo",
    "HIT_LOGGING_INFO",
    "HlinkGoBack",
    "HlinkGoForward",
    "HlinkNavigateMoniker",
    "HlinkNavigateString",
    "HlinkSimpleNavigateToMoniker",
    "HlinkSimpleNavigateToString",
    "IBindCallbackRedirect",
    "IBindHttpSecurity",
    "IBindProtocol",
    "ICatalogFileInfo",
    "ICodeInstall",
    "IDataFilter",
    "IEGetUserPrivateNamespaceName",
    "IEInstallScope",
    "IEObjectType",
    "IE_EPM_OBJECT_EVENT",
    "IE_EPM_OBJECT_FILE",
    "IE_EPM_OBJECT_MUTEX",
    "IE_EPM_OBJECT_NAMED_PIPE",
    "IE_EPM_OBJECT_REGISTRY",
    "IE_EPM_OBJECT_SEMAPHORE",
    "IE_EPM_OBJECT_SHARED_MEMORY",
    "IE_EPM_OBJECT_WAITABLE_TIMER",
    "IEncodingFilterFactory",
    "IGetBindHandle",
    "IHttpNegotiate",
    "IHttpNegotiate2",
    "IHttpNegotiate3",
    "IHttpSecurity",
    "IInternet",
    "IInternetBindInfo",
    "IInternetBindInfoEx",
    "IInternetHostSecurityManager",
    "IInternetPriority",
    "IInternetProtocol",
    "IInternetProtocolEx",
    "IInternetProtocolInfo",
    "IInternetProtocolRoot",
    "IInternetProtocolSink",
    "IInternetProtocolSinkStackable",
    "IInternetSecurityManager",
    "IInternetSecurityManagerEx",
    "IInternetSecurityManagerEx2",
    "IInternetSecurityMgrSite",
    "IInternetSession",
    "IInternetThreadSwitch",
    "IInternetZoneManager",
    "IInternetZoneManagerEx",
    "IInternetZoneManagerEx2",
    "IMonikerProp",
    "INET_E_AUTHENTICATION_REQUIRED",
    "INET_E_BLOCKED_ENHANCEDPROTECTEDMODE",
    "INET_E_BLOCKED_PLUGGABLE_PROTOCOL",
    "INET_E_BLOCKED_REDIRECT_XSECURITYID",
    "INET_E_CANNOT_CONNECT",
    "INET_E_CANNOT_INSTANTIATE_OBJECT",
    "INET_E_CANNOT_LOAD_DATA",
    "INET_E_CANNOT_LOCK_REQUEST",
    "INET_E_CANNOT_REPLACE_SFP_FILE",
    "INET_E_CODE_DOWNLOAD_DECLINED",
    "INET_E_CODE_INSTALL_BLOCKED_ARM",
    "INET_E_CODE_INSTALL_BLOCKED_BITNESS",
    "INET_E_CODE_INSTALL_BLOCKED_BY_HASH_POLICY",
    "INET_E_CODE_INSTALL_BLOCKED_IMMERSIVE",
    "INET_E_CODE_INSTALL_SUPPRESSED",
    "INET_E_CONNECTION_TIMEOUT",
    "INET_E_DATA_NOT_AVAILABLE",
    "INET_E_DEFAULT_ACTION",
    "INET_E_DOMINJECTIONVALIDATION",
    "INET_E_DOWNLOAD_BLOCKED_BY_CSP",
    "INET_E_DOWNLOAD_BLOCKED_BY_INPRIVATE",
    "INET_E_DOWNLOAD_FAILURE",
    "INET_E_ERROR_FIRST",
    "INET_E_ERROR_LAST",
    "INET_E_FORBIDFRAMING",
    "INET_E_HSTS_CERTIFICATE_ERROR",
    "INET_E_INVALID_CERTIFICATE",
    "INET_E_INVALID_REQUEST",
    "INET_E_INVALID_URL",
    "INET_E_NO_SESSION",
    "INET_E_NO_VALID_MEDIA",
    "INET_E_OBJECT_NOT_FOUND",
    "INET_E_QUERYOPTION_UNKNOWN",
    "INET_E_REDIRECTING",
    "INET_E_REDIRECT_FAILED",
    "INET_E_REDIRECT_TO_DIR",
    "INET_E_RESERVED_1",
    "INET_E_RESERVED_2",
    "INET_E_RESERVED_3",
    "INET_E_RESERVED_4",
    "INET_E_RESERVED_5",
    "INET_E_RESOURCE_NOT_FOUND",
    "INET_E_RESULT_DISPATCHED",
    "INET_E_SECURITY_PROBLEM",
    "INET_E_TERMINATED_BIND",
    "INET_E_UNKNOWN_PROTOCOL",
    "INET_E_USE_DEFAULT_PROTOCOLHANDLER",
    "INET_E_USE_DEFAULT_SETTING",
    "INET_E_USE_EXTEND_BINDING",
    "INET_E_VTAB_SWITCH_FORCE_ENGINE",
    "INET_ZONE_MANAGER_CONSTANTS",
    "INTERNETFEATURELIST",
    "IPersistMoniker",
    "ISoftDistExt",
    "IUriBuilderFactory",
    "IUriContainer",
    "IWinInetCacheHints",
    "IWinInetCacheHints2",
    "IWinInetFileStream",
    "IWinInetHttpInfo",
    "IWinInetHttpTimeouts",
    "IWinInetInfo",
    "IWindowForBindingUI",
    "IWrappedProtocol",
    "IZoneIdentifier",
    "IZoneIdentifier2",
    "IsAsyncMoniker",
    "IsLoggingEnabledA",
    "IsLoggingEnabledW",
    "IsValidURL",
    "MAX_SIZE_SECURITY_ID",
    "MAX_ZONE_DESCRIPTION",
    "MAX_ZONE_PATH",
    "MIMETYPEPROP",
    "MKSYS_URLMONIKER",
    "MK_S_ASYNCHRONOUS",
    "MONIKERPROPERTY",
    "MUTZ_ACCEPT_WILDCARD_SCHEME",
    "MUTZ_DONT_UNESCAPE",
    "MUTZ_DONT_USE_CACHE",
    "MUTZ_ENFORCERESTRICTED",
    "MUTZ_FORCE_INTRANET_FLAGS",
    "MUTZ_IGNORE_ZONE_MAPPINGS",
    "MUTZ_ISFILE",
    "MUTZ_NOSAVEDFILECHECK",
    "MUTZ_REQUIRESAVEDFILECHECK",
    "MUTZ_RESERVED",
    "MkParseDisplayNameEx",
    "OIBDG_APARTMENTTHREADED",
    "OIBDG_DATAONLY",
    "OIBDG_FLAGS",
    "ObtainUserAgentString",
    "PARSEACTION",
    "PARSE_ANCHOR",
    "PARSE_CANONICALIZE",
    "PARSE_DECODE_IS_ESCAPE",
    "PARSE_DOCUMENT",
    "PARSE_DOMAIN",
    "PARSE_ENCODE_IS_UNESCAPE",
    "PARSE_ESCAPE",
    "PARSE_FRIENDLY",
    "PARSE_LOCATION",
    "PARSE_MIME",
    "PARSE_PATH_FROM_URL",
    "PARSE_ROOTDOCUMENT",
    "PARSE_SCHEMA",
    "PARSE_SECURITY_DOMAIN",
    "PARSE_SECURITY_URL",
    "PARSE_SERVER",
    "PARSE_SITE",
    "PARSE_UNESCAPE",
    "PARSE_URL_FROM_PATH",
    "PD_FORCE_SWITCH",
    "PI_APARTMENTTHREADED",
    "PI_CLASSINSTALL",
    "PI_CLSIDLOOKUP",
    "PI_DATAPROGRESS",
    "PI_FILTER_MODE",
    "PI_FLAGS",
    "PI_FORCE_ASYNC",
    "PI_LOADAPPDIRECT",
    "PI_MIMEVERIFICATION",
    "PI_NOMIMEHANDLER",
    "PI_PARSE_URL",
    "PI_PASSONBINDCTX",
    "PI_PREFERDEFAULTHANDLER",
    "PI_SYNCHRONOUS",
    "PI_USE_WORKERTHREAD",
    "POPUPLEVELPROP",
    "PROTOCOLDATA",
    "PROTOCOLFILTERDATA",
    "PROTOCOLFLAG_NO_PICS_CHECK",
    "PROTOCOL_ARGUMENT",
    "PSUACTION",
    "PSU_DEFAULT",
    "PSU_SECURITY_URL_ONLY",
    "PUAF",
    "PUAFOUT",
    "PUAFOUT_DEFAULT",
    "PUAFOUT_ISLOCKZONEPOLICY",
    "PUAF_ACCEPT_WILDCARD_SCHEME",
    "PUAF_CHECK_TIFS",
    "PUAF_DEFAULT",
    "PUAF_DEFAULTZONEPOL",
    "PUAF_DONTCHECKBOXINDIALOG",
    "PUAF_DONT_USE_CACHE",
    "PUAF_DRAGPROTOCOLCHECK",
    "PUAF_ENFORCERESTRICTED",
    "PUAF_FORCEUI_FOREGROUND",
    "PUAF_ISFILE",
    "PUAF_LMZ_LOCKED",
    "PUAF_LMZ_UNLOCKED",
    "PUAF_NOSAVEDFILECHECK",
    "PUAF_NOUI",
    "PUAF_NOUIIFLOCKED",
    "PUAF_NPL_USE_LOCKED_IF_RESTRICTED",
    "PUAF_REQUIRESAVEDFILECHECK",
    "PUAF_RESERVED1",
    "PUAF_RESERVED2",
    "PUAF_TRUSTED",
    "PUAF_WARN_IF_DENIED",
    "QUERYOPTION",
    "QUERY_CAN_NAVIGATE",
    "QUERY_CONTENT_ENCODING",
    "QUERY_CONTENT_TYPE",
    "QUERY_EXPIRATION_DATE",
    "QUERY_IS_CACHED",
    "QUERY_IS_CACHED_AND_USABLE_OFFLINE",
    "QUERY_IS_CACHED_OR_MAPPED",
    "QUERY_IS_INSTALLEDENTRY",
    "QUERY_IS_SAFE",
    "QUERY_IS_SECURE",
    "QUERY_RECOMBINE",
    "QUERY_REFRESH",
    "QUERY_TIME_OF_LAST_CHANGE",
    "QUERY_USES_CACHE",
    "QUERY_USES_HISTORYFOLDER",
    "QUERY_USES_NETWORK",
    "REMSECURITY_ATTRIBUTES",
    "RegisterBindStatusCallback",
    "RegisterFormatEnumerator",
    "RegisterMediaTypeClass",
    "RegisterMediaTypes",
    "ReleaseBindInfo",
    "RemBINDINFO",
    "RemFORMATETC",
    "RevokeBindStatusCallback",
    "RevokeFormatEnumerator",
    "SECURITY_IE_STATE_GREEN",
    "SECURITY_IE_STATE_RED",
    "SET_FEATURE_IN_REGISTRY",
    "SET_FEATURE_ON_PROCESS",
    "SET_FEATURE_ON_THREAD",
    "SET_FEATURE_ON_THREAD_INTERNET",
    "SET_FEATURE_ON_THREAD_INTRANET",
    "SET_FEATURE_ON_THREAD_LOCALMACHINE",
    "SET_FEATURE_ON_THREAD_RESTRICTED",
    "SET_FEATURE_ON_THREAD_TRUSTED",
    "SOFTDISTINFO",
    "SOFTDIST_ADSTATE_AVAILABLE",
    "SOFTDIST_ADSTATE_DOWNLOADED",
    "SOFTDIST_ADSTATE_INSTALLED",
    "SOFTDIST_ADSTATE_NONE",
    "SOFTDIST_FLAG_DELETE_SUBSCRIPTION",
    "SOFTDIST_FLAG_USAGE_AUTOINSTALL",
    "SOFTDIST_FLAG_USAGE_EMAIL",
    "SOFTDIST_FLAG_USAGE_PRECACHE",
    "SZM_CREATE",
    "SZM_DELETE",
    "SZM_FLAGS",
    "S_ASYNCHRONOUS",
    "SetAccessForIEAppContainer",
    "SetSoftwareUpdateAdvertisementState",
    "StartParam",
    "TRUSTEDDOWNLOADPROP",
    "UAS_EXACTLEGACY",
    "URLACTION_ACTIVEX_ALLOW_TDC",
    "URLACTION_ACTIVEX_CONFIRM_NOOBJECTSAFETY",
    "URLACTION_ACTIVEX_CURR_MAX",
    "URLACTION_ACTIVEX_DYNSRC_VIDEO_AND_ANIMATION",
    "URLACTION_ACTIVEX_MAX",
    "URLACTION_ACTIVEX_MIN",
    "URLACTION_ACTIVEX_NO_WEBOC_SCRIPT",
    "URLACTION_ACTIVEX_OVERRIDE_DATA_SAFETY",
    "URLACTION_ACTIVEX_OVERRIDE_DOMAINLIST",
    "URLACTION_ACTIVEX_OVERRIDE_OBJECT_SAFETY",
    "URLACTION_ACTIVEX_OVERRIDE_OPTIN",
    "URLACTION_ACTIVEX_OVERRIDE_REPURPOSEDETECTION",
    "URLACTION_ACTIVEX_OVERRIDE_SCRIPT_SAFETY",
    "URLACTION_ACTIVEX_RUN",
    "URLACTION_ACTIVEX_SCRIPTLET_RUN",
    "URLACTION_ACTIVEX_TREATASUNTRUSTED",
    "URLACTION_ALLOW_ACTIVEX_FILTERING",
    "URLACTION_ALLOW_ANTIMALWARE_SCANNING_OF_ACTIVEX",
    "URLACTION_ALLOW_APEVALUATION",
    "URLACTION_ALLOW_AUDIO_VIDEO",
    "URLACTION_ALLOW_AUDIO_VIDEO_PLUGINS",
    "URLACTION_ALLOW_CROSSDOMAIN_APPCACHE_MANIFEST",
    "URLACTION_ALLOW_CROSSDOMAIN_DROP_ACROSS_WINDOWS",
    "URLACTION_ALLOW_CROSSDOMAIN_DROP_WITHIN_WINDOW",
    "URLACTION_ALLOW_CSS_EXPRESSIONS",
    "URLACTION_ALLOW_JSCRIPT_IE",
    "URLACTION_ALLOW_RENDER_LEGACY_DXTFILTERS",
    "URLACTION_ALLOW_RESTRICTEDPROTOCOLS",
    "URLACTION_ALLOW_STRUCTURED_STORAGE_SNIFFING",
    "URLACTION_ALLOW_VBSCRIPT_IE",
    "URLACTION_ALLOW_XDOMAIN_SUBFRAME_RESIZE",
    "URLACTION_ALLOW_XHR_EVALUATION",
    "URLACTION_ALLOW_ZONE_ELEVATION_OPT_OUT_ADDITION",
    "URLACTION_ALLOW_ZONE_ELEVATION_VIA_OPT_OUT",
    "URLACTION_AUTHENTICATE_CLIENT",
    "URLACTION_AUTOMATIC_ACTIVEX_UI",
    "URLACTION_AUTOMATIC_DOWNLOAD_UI",
    "URLACTION_AUTOMATIC_DOWNLOAD_UI_MIN",
    "URLACTION_BEHAVIOR_MIN",
    "URLACTION_BEHAVIOR_RUN",
    "URLACTION_CHANNEL_SOFTDIST_MAX",
    "URLACTION_CHANNEL_SOFTDIST_MIN",
    "URLACTION_CHANNEL_SOFTDIST_PERMISSIONS",
    "URLACTION_CLIENT_CERT_PROMPT",
    "URLACTION_COOKIES",
    "URLACTION_COOKIES_ENABLED",
    "URLACTION_COOKIES_SESSION",
    "URLACTION_COOKIES_SESSION_THIRD_PARTY",
    "URLACTION_COOKIES_THIRD_PARTY",
    "URLACTION_CREDENTIALS_USE",
    "URLACTION_CROSS_DOMAIN_DATA",
    "URLACTION_DOTNET_USERCONTROLS",
    "URLACTION_DOWNLOAD_CURR_MAX",
    "URLACTION_DOWNLOAD_MAX",
    "URLACTION_DOWNLOAD_MIN",
    "URLACTION_DOWNLOAD_SIGNED_ACTIVEX",
    "URLACTION_DOWNLOAD_UNSIGNED_ACTIVEX",
    "URLACTION_FEATURE_BLOCK_INPUT_PROMPTS",
    "URLACTION_FEATURE_CROSSDOMAIN_FOCUS_CHANGE",
    "URLACTION_FEATURE_DATA_BINDING",
    "URLACTION_FEATURE_FORCE_ADDR_AND_STATUS",
    "URLACTION_FEATURE_MIME_SNIFFING",
    "URLACTION_FEATURE_MIN",
    "URLACTION_FEATURE_SCRIPT_STATUS_BAR",
    "URLACTION_FEATURE_WINDOW_RESTRICTIONS",
    "URLACTION_FEATURE_ZONE_ELEVATION",
    "URLACTION_HTML_ALLOW_CROSS_DOMAIN_CANVAS",
    "URLACTION_HTML_ALLOW_CROSS_DOMAIN_TEXTTRACK",
    "URLACTION_HTML_ALLOW_CROSS_DOMAIN_WEBWORKER",
    "URLACTION_HTML_ALLOW_INDEXEDDB",
    "URLACTION_HTML_ALLOW_INJECTED_DYNAMIC_HTML",
    "URLACTION_HTML_ALLOW_WINDOW_CLOSE",
    "URLACTION_HTML_FONT_DOWNLOAD",
    "URLACTION_HTML_INCLUDE_FILE_PATH",
    "URLACTION_HTML_JAVA_RUN",
    "URLACTION_HTML_MAX",
    "URLACTION_HTML_META_REFRESH",
    "URLACTION_HTML_MIN",
    "URLACTION_HTML_MIXED_CONTENT",
    "URLACTION_HTML_REQUIRE_UTF8_DOCUMENT_CODEPAGE",
    "URLACTION_HTML_SUBFRAME_NAVIGATE",
    "URLACTION_HTML_SUBMIT_FORMS",
    "URLACTION_HTML_SUBMIT_FORMS_FROM",
    "URLACTION_HTML_SUBMIT_FORMS_TO",
    "URLACTION_HTML_USERDATA_SAVE",
    "URLACTION_INFODELIVERY_CURR_MAX",
    "URLACTION_INFODELIVERY_MAX",
    "URLACTION_INFODELIVERY_MIN",
    "URLACTION_INFODELIVERY_NO_ADDING_CHANNELS",
    "URLACTION_INFODELIVERY_NO_ADDING_SUBSCRIPTIONS",
    "URLACTION_INFODELIVERY_NO_CHANNEL_LOGGING",
    "URLACTION_INFODELIVERY_NO_EDITING_CHANNELS",
    "URLACTION_INFODELIVERY_NO_EDITING_SUBSCRIPTIONS",
    "URLACTION_INFODELIVERY_NO_REMOVING_CHANNELS",
    "URLACTION_INFODELIVERY_NO_REMOVING_SUBSCRIPTIONS",
    "URLACTION_INPRIVATE_BLOCKING",
    "URLACTION_JAVA_CURR_MAX",
    "URLACTION_JAVA_MAX",
    "URLACTION_JAVA_MIN",
    "URLACTION_JAVA_PERMISSIONS",
    "URLACTION_LOOSE_XAML",
    "URLACTION_LOWRIGHTS",
    "URLACTION_MIN",
    "URLACTION_NETWORK_CURR_MAX",
    "URLACTION_NETWORK_MAX",
    "URLACTION_NETWORK_MIN",
    "URLACTION_PLUGGABLE_PROTOCOL_XHR",
    "URLACTION_SCRIPT_CURR_MAX",
    "URLACTION_SCRIPT_JAVA_USE",
    "URLACTION_SCRIPT_MAX",
    "URLACTION_SCRIPT_MIN",
    "URLACTION_SCRIPT_NAVIGATE",
    "URLACTION_SCRIPT_OVERRIDE_SAFETY",
    "URLACTION_SCRIPT_PASTE",
    "URLACTION_SCRIPT_RUN",
    "URLACTION_SCRIPT_SAFE_ACTIVEX",
    "URLACTION_SCRIPT_XSSFILTER",
    "URLACTION_SHELL_ALLOW_CROSS_SITE_SHARE",
    "URLACTION_SHELL_CURR_MAX",
    "URLACTION_SHELL_ENHANCED_DRAGDROP_SECURITY",
    "URLACTION_SHELL_EXECUTE_HIGHRISK",
    "URLACTION_SHELL_EXECUTE_LOWRISK",
    "URLACTION_SHELL_EXECUTE_MODRISK",
    "URLACTION_SHELL_EXTENSIONSECURITY",
    "URLACTION_SHELL_FILE_DOWNLOAD",
    "URLACTION_SHELL_INSTALL_DTITEMS",
    "URLACTION_SHELL_MAX",
    "URLACTION_SHELL_MIN",
    "URLACTION_SHELL_MOVE_OR_COPY",
    "URLACTION_SHELL_POPUPMGR",
    "URLACTION_SHELL_PREVIEW",
    "URLACTION_SHELL_REMOTEQUERY",
    "URLACTION_SHELL_RTF_OBJECTS_LOAD",
    "URLACTION_SHELL_SECURE_DRAGSOURCE",
    "URLACTION_SHELL_SHARE",
    "URLACTION_SHELL_SHELLEXECUTE",
    "URLACTION_SHELL_TOCTOU_RISK",
    "URLACTION_SHELL_VERB",
    "URLACTION_SHELL_WEBVIEW_VERB",
    "URLACTION_WINDOWS_BROWSER_APPLICATIONS",
    "URLACTION_WINFX_SETUP",
    "URLACTION_XPS_DOCUMENTS",
    "URLDownloadToCacheFileA",
    "URLDownloadToCacheFileW",
    "URLDownloadToFileA",
    "URLDownloadToFileW",
    "URLMON_OPTION_URL_ENCODING",
    "URLMON_OPTION_USERAGENT",
    "URLMON_OPTION_USERAGENT_REFRESH",
    "URLMON_OPTION_USE_BINDSTRINGCREDS",
    "URLMON_OPTION_USE_BROWSERAPPSDOCUMENTS",
    "URLOSTRM_GETNEWESTVERSION",
    "URLOSTRM_USECACHEDCOPY",
    "URLOSTRM_USECACHEDCOPY_ONLY",
    "URLOpenBlockingStreamA",
    "URLOpenBlockingStreamW",
    "URLOpenPullStreamA",
    "URLOpenPullStreamW",
    "URLOpenStreamA",
    "URLOpenStreamW",
    "URLPOLICY_ACTIVEX_CHECK_LIST",
    "URLPOLICY_ALLOW",
    "URLPOLICY_AUTHENTICATE_CHALLENGE_RESPONSE",
    "URLPOLICY_AUTHENTICATE_CLEARTEXT_OK",
    "URLPOLICY_AUTHENTICATE_MUTUAL_ONLY",
    "URLPOLICY_BEHAVIOR_CHECK_LIST",
    "URLPOLICY_CHANNEL_SOFTDIST_AUTOINSTALL",
    "URLPOLICY_CHANNEL_SOFTDIST_PRECACHE",
    "URLPOLICY_CHANNEL_SOFTDIST_PROHIBIT",
    "URLPOLICY_CREDENTIALS_ANONYMOUS_ONLY",
    "URLPOLICY_CREDENTIALS_CONDITIONAL_PROMPT",
    "URLPOLICY_CREDENTIALS_MUST_PROMPT_USER",
    "URLPOLICY_CREDENTIALS_SILENT_LOGON_OK",
    "URLPOLICY_DISALLOW",
    "URLPOLICY_DONTCHECKDLGBOX",
    "URLPOLICY_JAVA_CUSTOM",
    "URLPOLICY_JAVA_HIGH",
    "URLPOLICY_JAVA_LOW",
    "URLPOLICY_JAVA_MEDIUM",
    "URLPOLICY_JAVA_PROHIBIT",
    "URLPOLICY_LOG_ON_ALLOW",
    "URLPOLICY_LOG_ON_DISALLOW",
    "URLPOLICY_MASK_PERMISSIONS",
    "URLPOLICY_NOTIFY_ON_ALLOW",
    "URLPOLICY_NOTIFY_ON_DISALLOW",
    "URLPOLICY_QUERY",
    "URLTEMPLATE",
    "URLTEMPLATE_CUSTOM",
    "URLTEMPLATE_HIGH",
    "URLTEMPLATE_LOW",
    "URLTEMPLATE_MEDHIGH",
    "URLTEMPLATE_MEDIUM",
    "URLTEMPLATE_MEDLOW",
    "URLTEMPLATE_PREDEFINED_MAX",
    "URLTEMPLATE_PREDEFINED_MIN",
    "URLZONE",
    "URLZONEREG",
    "URLZONEREG_DEFAULT",
    "URLZONEREG_HKCU",
    "URLZONEREG_HKLM",
    "URLZONE_ESC_FLAG",
    "URLZONE_INTERNET",
    "URLZONE_INTRANET",
    "URLZONE_INVALID",
    "URLZONE_LOCAL_MACHINE",
    "URLZONE_PREDEFINED_MAX",
    "URLZONE_PREDEFINED_MIN",
    "URLZONE_TRUSTED",
    "URLZONE_UNTRUSTED",
    "URLZONE_USER_MAX",
    "URLZONE_USER_MIN",
    "URL_ENCODING",
    "URL_ENCODING_DISABLE_UTF8",
    "URL_ENCODING_ENABLE_UTF8",
    "URL_ENCODING_NONE",
    "URL_MK_LEGACY",
    "URL_MK_NO_CANONICALIZE",
    "URL_MK_UNIFORM",
    "USE_SRC_URL",
    "UriBuilder_USE_ORIGINAL_FLAGS",
    "Uri_DISPLAY_IDN_HOST",
    "Uri_DISPLAY_NO_FRAGMENT",
    "Uri_DISPLAY_NO_PUNYCODE",
    "Uri_ENCODING_HOST_IS_IDN",
    "Uri_ENCODING_HOST_IS_PERCENT_ENCODED_CP",
    "Uri_ENCODING_HOST_IS_PERCENT_ENCODED_UTF8",
    "Uri_ENCODING_QUERY_AND_FRAGMENT_IS_CP",
    "Uri_ENCODING_QUERY_AND_FRAGMENT_IS_PERCENT_ENCODED_UTF8",
    "Uri_ENCODING_USER_INFO_AND_PATH_IS_CP",
    "Uri_ENCODING_USER_INFO_AND_PATH_IS_PERCENT_ENCODED_UTF8",
    "Uri_HOST_DNS",
    "Uri_HOST_IDN",
    "Uri_HOST_IPV4",
    "Uri_HOST_IPV6",
    "Uri_HOST_TYPE",
    "Uri_HOST_UNKNOWN",
    "Uri_PUNYCODE_IDN_HOST",
    "UrlMkGetSessionOption",
    "UrlMkSetSessionOption",
    "WININETINFO_OPTION_LOCK_HANDLE",
    "WriteHitLogging",
    "ZAFLAGS",
    "ZAFLAGS_ADD_SITES",
    "ZAFLAGS_CUSTOM_EDIT",
    "ZAFLAGS_DETECT_INTRANET",
    "ZAFLAGS_INCLUDE_INTRANET_SITES",
    "ZAFLAGS_INCLUDE_PROXY_OVERRIDE",
    "ZAFLAGS_NO_CACHE",
    "ZAFLAGS_NO_UI",
    "ZAFLAGS_REQUIRE_VERIFICATION",
    "ZAFLAGS_SUPPORTS_VERIFICATION",
    "ZAFLAGS_UNC_AS_INTRANET",
    "ZAFLAGS_USE_LOCKED_ZONES",
    "ZAFLAGS_VERIFY_TEMPLATE_SETTINGS",
    "ZONEATTRIBUTES",
]
_arch_optional = [
]
