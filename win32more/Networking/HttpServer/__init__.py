from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, PROPERTYKEY, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Networking.HttpServer
import win32more.Networking.WinSock
import win32more.Security
import win32more.System.IO

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
HTTP_DEMAND_CBT = 4
HTTP_MAX_SERVER_QUEUE_LENGTH = 2147483647
HTTP_MIN_SERVER_QUEUE_LENGTH = 1
HTTP_AUTH_ENABLE_BASIC = 1
HTTP_AUTH_ENABLE_DIGEST = 2
HTTP_AUTH_ENABLE_NTLM = 4
HTTP_AUTH_ENABLE_NEGOTIATE = 8
HTTP_AUTH_ENABLE_KERBEROS = 16
HTTP_AUTH_EX_FLAG_ENABLE_KERBEROS_CREDENTIAL_CACHING = 1
HTTP_AUTH_EX_FLAG_CAPTURE_CREDENTIAL = 2
HTTP_CHANNEL_BIND_PROXY = 1
HTTP_CHANNEL_BIND_PROXY_COHOSTING = 32
HTTP_CHANNEL_BIND_NO_SERVICE_NAME_CHECK = 2
HTTP_CHANNEL_BIND_DOTLESS_SERVICE = 4
HTTP_CHANNEL_BIND_SECURE_CHANNEL_TOKEN = 8
HTTP_CHANNEL_BIND_CLIENT_SERVICE = 16
HTTP_LOG_FIELD_DATE = 1
HTTP_LOG_FIELD_TIME = 2
HTTP_LOG_FIELD_CLIENT_IP = 4
HTTP_LOG_FIELD_USER_NAME = 8
HTTP_LOG_FIELD_SITE_NAME = 16
HTTP_LOG_FIELD_COMPUTER_NAME = 32
HTTP_LOG_FIELD_SERVER_IP = 64
HTTP_LOG_FIELD_METHOD = 128
HTTP_LOG_FIELD_URI_STEM = 256
HTTP_LOG_FIELD_URI_QUERY = 512
HTTP_LOG_FIELD_STATUS = 1024
HTTP_LOG_FIELD_WIN32_STATUS = 2048
HTTP_LOG_FIELD_BYTES_SENT = 4096
HTTP_LOG_FIELD_BYTES_RECV = 8192
HTTP_LOG_FIELD_TIME_TAKEN = 16384
HTTP_LOG_FIELD_SERVER_PORT = 32768
HTTP_LOG_FIELD_USER_AGENT = 65536
HTTP_LOG_FIELD_COOKIE = 131072
HTTP_LOG_FIELD_REFERER = 262144
HTTP_LOG_FIELD_VERSION = 524288
HTTP_LOG_FIELD_HOST = 1048576
HTTP_LOG_FIELD_SUB_STATUS = 2097152
HTTP_LOG_FIELD_STREAM_ID = 134217728
HTTP_LOG_FIELD_STREAM_ID_EX = 268435456
HTTP_LOG_FIELD_TRANSPORT_TYPE = 536870912
HTTP_LOG_FIELD_CLIENT_PORT = 4194304
HTTP_LOG_FIELD_URI = 8388608
HTTP_LOG_FIELD_SITE_ID = 16777216
HTTP_LOG_FIELD_REASON = 33554432
HTTP_LOG_FIELD_QUEUE_NAME = 67108864
HTTP_LOG_FIELD_CORRELATION_ID = 1073741824
HTTP_LOGGING_FLAG_LOCAL_TIME_ROLLOVER = 1
HTTP_LOGGING_FLAG_USE_UTF8_CONVERSION = 2
HTTP_LOGGING_FLAG_LOG_ERRORS_ONLY = 4
HTTP_LOGGING_FLAG_LOG_SUCCESS_ONLY = 8
HTTP_CREATE_REQUEST_QUEUE_FLAG_OPEN_EXISTING = 1
HTTP_CREATE_REQUEST_QUEUE_FLAG_CONTROLLER = 2
HTTP_CREATE_REQUEST_QUEUE_FLAG_DELEGATION = 8
HTTP_RECEIVE_REQUEST_ENTITY_BODY_FLAG_FILL_BUFFER = 1
HTTP_SEND_RESPONSE_FLAG_DISCONNECT = 1
HTTP_SEND_RESPONSE_FLAG_MORE_DATA = 2
HTTP_SEND_RESPONSE_FLAG_BUFFER_DATA = 4
HTTP_SEND_RESPONSE_FLAG_ENABLE_NAGLING = 8
HTTP_SEND_RESPONSE_FLAG_PROCESS_RANGES = 32
HTTP_SEND_RESPONSE_FLAG_OPAQUE = 64
HTTP_SEND_RESPONSE_FLAG_GOAWAY = 256
HTTP_FLUSH_RESPONSE_FLAG_RECURSIVE = 1
HTTP_URL_FLAG_REMOVE_ALL = 1
HTTP_RECEIVE_SECURE_CHANNEL_TOKEN = 1
HTTP_RECEIVE_FULL_CHAIN = 2
HTTP_REQUEST_SIZING_INFO_FLAG_TCP_FAST_OPEN = 1
HTTP_REQUEST_SIZING_INFO_FLAG_TLS_SESSION_RESUMPTION = 2
HTTP_REQUEST_SIZING_INFO_FLAG_TLS_FALSE_START = 4
HTTP_REQUEST_SIZING_INFO_FLAG_FIRST_REQUEST = 8
HTTP_REQUEST_AUTH_FLAG_TOKEN_FOR_CACHED_CRED = 1
HTTP_REQUEST_FLAG_MORE_ENTITY_BODY_EXISTS = 1
HTTP_REQUEST_FLAG_IP_ROUTED = 2
HTTP_REQUEST_FLAG_HTTP2 = 4
HTTP_REQUEST_FLAG_HTTP3 = 8
HTTP_RESPONSE_FLAG_MULTIPLE_ENCODINGS_AVAILABLE = 1
HTTP_RESPONSE_FLAG_MORE_ENTITY_BODY_EXISTS = 2
HTTP_RESPONSE_INFO_FLAGS_PRESERVE_ORDER = 1
HTTP_SERVICE_CONFIG_SSL_FLAG_USE_DS_MAPPER = 1
HTTP_SERVICE_CONFIG_SSL_FLAG_NEGOTIATE_CLIENT_CERT = 2
HTTP_SERVICE_CONFIG_SSL_FLAG_NO_RAW_FILTER = 4
HTTP_SERVICE_CONFIG_SSL_FLAG_REJECT = 8
HTTP_SERVICE_CONFIG_SSL_FLAG_DISABLE_HTTP2 = 16
HTTP_SERVICE_CONFIG_SSL_FLAG_DISABLE_QUIC = 32
HTTP_SERVICE_CONFIG_SSL_FLAG_DISABLE_TLS13 = 64
HTTP_SERVICE_CONFIG_SSL_FLAG_DISABLE_OCSP_STAPLING = 128
HTTP_SERVICE_CONFIG_SSL_FLAG_ENABLE_TOKEN_BINDING = 256
HTTP_SERVICE_CONFIG_SSL_FLAG_LOG_EXTENDED_EVENTS = 512
HTTP_SERVICE_CONFIG_SSL_FLAG_DISABLE_LEGACY_TLS = 1024
HTTP_SERVICE_CONFIG_SSL_FLAG_ENABLE_SESSION_TICKET = 2048
HTTP_SERVICE_CONFIG_SSL_FLAG_DISABLE_TLS12 = 4096
HTTP_SERVICE_CONFIG_SSL_FLAG_ENABLE_CLIENT_CORRELATION = 8192
HTTP_REQUEST_PROPERTY_SNI_HOST_MAX_LENGTH = 255
HTTP_REQUEST_PROPERTY_SNI_FLAG_SNI_USED = 1
HTTP_REQUEST_PROPERTY_SNI_FLAG_NO_SNI = 2
HTTP_RECEIVE_HTTP_REQUEST_FLAGS = UInt32
HTTP_RECEIVE_REQUEST_FLAG_COPY_BODY = 1
HTTP_RECEIVE_REQUEST_FLAG_FLUSH_BODY = 2
HTTP_INITIALIZE = UInt32
HTTP_INITIALIZE_CONFIG = 2
HTTP_INITIALIZE_SERVER = 1
HTTP_SERVER_PROPERTY = Int32
HTTP_SERVER_PROPERTY_HttpServerAuthenticationProperty = 0
HTTP_SERVER_PROPERTY_HttpServerLoggingProperty = 1
HTTP_SERVER_PROPERTY_HttpServerQosProperty = 2
HTTP_SERVER_PROPERTY_HttpServerTimeoutsProperty = 3
HTTP_SERVER_PROPERTY_HttpServerQueueLengthProperty = 4
HTTP_SERVER_PROPERTY_HttpServerStateProperty = 5
HTTP_SERVER_PROPERTY_HttpServer503VerbosityProperty = 6
HTTP_SERVER_PROPERTY_HttpServerBindingProperty = 7
HTTP_SERVER_PROPERTY_HttpServerExtendedAuthenticationProperty = 8
HTTP_SERVER_PROPERTY_HttpServerListenEndpointProperty = 9
HTTP_SERVER_PROPERTY_HttpServerChannelBindProperty = 10
HTTP_SERVER_PROPERTY_HttpServerProtectionLevelProperty = 11
HTTP_SERVER_PROPERTY_HttpServerDelegationProperty = 16
def _define_HTTP_PROPERTY_FLAGS_head():
    class HTTP_PROPERTY_FLAGS(Structure):
        pass
    return HTTP_PROPERTY_FLAGS
def _define_HTTP_PROPERTY_FLAGS():
    HTTP_PROPERTY_FLAGS = win32more.Networking.HttpServer.HTTP_PROPERTY_FLAGS_head
    HTTP_PROPERTY_FLAGS._fields_ = [
        ("_bitfield", UInt32),
    ]
    return HTTP_PROPERTY_FLAGS
HTTP_ENABLED_STATE = Int32
HTTP_ENABLED_STATE_HttpEnabledStateActive = 0
HTTP_ENABLED_STATE_HttpEnabledStateInactive = 1
def _define_HTTP_STATE_INFO_head():
    class HTTP_STATE_INFO(Structure):
        pass
    return HTTP_STATE_INFO
def _define_HTTP_STATE_INFO():
    HTTP_STATE_INFO = win32more.Networking.HttpServer.HTTP_STATE_INFO_head
    HTTP_STATE_INFO._fields_ = [
        ("Flags", win32more.Networking.HttpServer.HTTP_PROPERTY_FLAGS),
        ("State", win32more.Networking.HttpServer.HTTP_ENABLED_STATE),
    ]
    return HTTP_STATE_INFO
HTTP_503_RESPONSE_VERBOSITY = Int32
HTTP_503_RESPONSE_VERBOSITY_Http503ResponseVerbosityBasic = 0
HTTP_503_RESPONSE_VERBOSITY_Http503ResponseVerbosityLimited = 1
HTTP_503_RESPONSE_VERBOSITY_Http503ResponseVerbosityFull = 2
HTTP_QOS_SETTING_TYPE = Int32
HTTP_QOS_SETTING_TYPE_HttpQosSettingTypeBandwidth = 0
HTTP_QOS_SETTING_TYPE_HttpQosSettingTypeConnectionLimit = 1
HTTP_QOS_SETTING_TYPE_HttpQosSettingTypeFlowRate = 2
def _define_HTTP_QOS_SETTING_INFO_head():
    class HTTP_QOS_SETTING_INFO(Structure):
        pass
    return HTTP_QOS_SETTING_INFO
def _define_HTTP_QOS_SETTING_INFO():
    HTTP_QOS_SETTING_INFO = win32more.Networking.HttpServer.HTTP_QOS_SETTING_INFO_head
    HTTP_QOS_SETTING_INFO._fields_ = [
        ("QosType", win32more.Networking.HttpServer.HTTP_QOS_SETTING_TYPE),
        ("QosSetting", c_void_p),
    ]
    return HTTP_QOS_SETTING_INFO
def _define_HTTP_CONNECTION_LIMIT_INFO_head():
    class HTTP_CONNECTION_LIMIT_INFO(Structure):
        pass
    return HTTP_CONNECTION_LIMIT_INFO
def _define_HTTP_CONNECTION_LIMIT_INFO():
    HTTP_CONNECTION_LIMIT_INFO = win32more.Networking.HttpServer.HTTP_CONNECTION_LIMIT_INFO_head
    HTTP_CONNECTION_LIMIT_INFO._fields_ = [
        ("Flags", win32more.Networking.HttpServer.HTTP_PROPERTY_FLAGS),
        ("MaxConnections", UInt32),
    ]
    return HTTP_CONNECTION_LIMIT_INFO
def _define_HTTP_BANDWIDTH_LIMIT_INFO_head():
    class HTTP_BANDWIDTH_LIMIT_INFO(Structure):
        pass
    return HTTP_BANDWIDTH_LIMIT_INFO
def _define_HTTP_BANDWIDTH_LIMIT_INFO():
    HTTP_BANDWIDTH_LIMIT_INFO = win32more.Networking.HttpServer.HTTP_BANDWIDTH_LIMIT_INFO_head
    HTTP_BANDWIDTH_LIMIT_INFO._fields_ = [
        ("Flags", win32more.Networking.HttpServer.HTTP_PROPERTY_FLAGS),
        ("MaxBandwidth", UInt32),
    ]
    return HTTP_BANDWIDTH_LIMIT_INFO
def _define_HTTP_FLOWRATE_INFO_head():
    class HTTP_FLOWRATE_INFO(Structure):
        pass
    return HTTP_FLOWRATE_INFO
def _define_HTTP_FLOWRATE_INFO():
    HTTP_FLOWRATE_INFO = win32more.Networking.HttpServer.HTTP_FLOWRATE_INFO_head
    HTTP_FLOWRATE_INFO._fields_ = [
        ("Flags", win32more.Networking.HttpServer.HTTP_PROPERTY_FLAGS),
        ("MaxBandwidth", UInt32),
        ("MaxPeakBandwidth", UInt32),
        ("BurstSize", UInt32),
    ]
    return HTTP_FLOWRATE_INFO
HTTP_SERVICE_CONFIG_TIMEOUT_KEY = Int32
HTTP_SERVICE_CONFIG_TIMEOUT_KEY_IdleConnectionTimeout = 0
HTTP_SERVICE_CONFIG_TIMEOUT_KEY_HeaderWaitTimeout = 1
def _define_HTTP_SERVICE_CONFIG_TIMEOUT_SET_head():
    class HTTP_SERVICE_CONFIG_TIMEOUT_SET(Structure):
        pass
    return HTTP_SERVICE_CONFIG_TIMEOUT_SET
def _define_HTTP_SERVICE_CONFIG_TIMEOUT_SET():
    HTTP_SERVICE_CONFIG_TIMEOUT_SET = win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_TIMEOUT_SET_head
    HTTP_SERVICE_CONFIG_TIMEOUT_SET._fields_ = [
        ("KeyDesc", win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_TIMEOUT_KEY),
        ("ParamDesc", UInt16),
    ]
    return HTTP_SERVICE_CONFIG_TIMEOUT_SET
def _define_HTTP_TIMEOUT_LIMIT_INFO_head():
    class HTTP_TIMEOUT_LIMIT_INFO(Structure):
        pass
    return HTTP_TIMEOUT_LIMIT_INFO
def _define_HTTP_TIMEOUT_LIMIT_INFO():
    HTTP_TIMEOUT_LIMIT_INFO = win32more.Networking.HttpServer.HTTP_TIMEOUT_LIMIT_INFO_head
    HTTP_TIMEOUT_LIMIT_INFO._fields_ = [
        ("Flags", win32more.Networking.HttpServer.HTTP_PROPERTY_FLAGS),
        ("EntityBody", UInt16),
        ("DrainEntityBody", UInt16),
        ("RequestQueue", UInt16),
        ("IdleConnection", UInt16),
        ("HeaderWait", UInt16),
        ("MinSendRate", UInt32),
    ]
    return HTTP_TIMEOUT_LIMIT_INFO
HTTP_SERVICE_CONFIG_SETTING_KEY = Int32
HTTP_SERVICE_CONFIG_SETTING_KEY_HttpNone = 0
HTTP_SERVICE_CONFIG_SETTING_KEY_HttpTlsThrottle = 1
def _define_HTTP_SERVICE_CONFIG_SETTING_SET_head():
    class HTTP_SERVICE_CONFIG_SETTING_SET(Structure):
        pass
    return HTTP_SERVICE_CONFIG_SETTING_SET
def _define_HTTP_SERVICE_CONFIG_SETTING_SET():
    HTTP_SERVICE_CONFIG_SETTING_SET = win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SETTING_SET_head
    HTTP_SERVICE_CONFIG_SETTING_SET._fields_ = [
        ("KeyDesc", win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SETTING_KEY),
        ("ParamDesc", UInt32),
    ]
    return HTTP_SERVICE_CONFIG_SETTING_SET
def _define_HTTP_LISTEN_ENDPOINT_INFO_head():
    class HTTP_LISTEN_ENDPOINT_INFO(Structure):
        pass
    return HTTP_LISTEN_ENDPOINT_INFO
def _define_HTTP_LISTEN_ENDPOINT_INFO():
    HTTP_LISTEN_ENDPOINT_INFO = win32more.Networking.HttpServer.HTTP_LISTEN_ENDPOINT_INFO_head
    HTTP_LISTEN_ENDPOINT_INFO._fields_ = [
        ("Flags", win32more.Networking.HttpServer.HTTP_PROPERTY_FLAGS),
        ("EnableSharing", win32more.Foundation.BOOLEAN),
    ]
    return HTTP_LISTEN_ENDPOINT_INFO
def _define_HTTP_SERVER_AUTHENTICATION_DIGEST_PARAMS_head():
    class HTTP_SERVER_AUTHENTICATION_DIGEST_PARAMS(Structure):
        pass
    return HTTP_SERVER_AUTHENTICATION_DIGEST_PARAMS
def _define_HTTP_SERVER_AUTHENTICATION_DIGEST_PARAMS():
    HTTP_SERVER_AUTHENTICATION_DIGEST_PARAMS = win32more.Networking.HttpServer.HTTP_SERVER_AUTHENTICATION_DIGEST_PARAMS_head
    HTTP_SERVER_AUTHENTICATION_DIGEST_PARAMS._fields_ = [
        ("DomainNameLength", UInt16),
        ("DomainName", win32more.Foundation.PWSTR),
        ("RealmLength", UInt16),
        ("Realm", win32more.Foundation.PWSTR),
    ]
    return HTTP_SERVER_AUTHENTICATION_DIGEST_PARAMS
def _define_HTTP_SERVER_AUTHENTICATION_BASIC_PARAMS_head():
    class HTTP_SERVER_AUTHENTICATION_BASIC_PARAMS(Structure):
        pass
    return HTTP_SERVER_AUTHENTICATION_BASIC_PARAMS
def _define_HTTP_SERVER_AUTHENTICATION_BASIC_PARAMS():
    HTTP_SERVER_AUTHENTICATION_BASIC_PARAMS = win32more.Networking.HttpServer.HTTP_SERVER_AUTHENTICATION_BASIC_PARAMS_head
    HTTP_SERVER_AUTHENTICATION_BASIC_PARAMS._fields_ = [
        ("RealmLength", UInt16),
        ("Realm", win32more.Foundation.PWSTR),
    ]
    return HTTP_SERVER_AUTHENTICATION_BASIC_PARAMS
def _define_HTTP_SERVER_AUTHENTICATION_INFO_head():
    class HTTP_SERVER_AUTHENTICATION_INFO(Structure):
        pass
    return HTTP_SERVER_AUTHENTICATION_INFO
def _define_HTTP_SERVER_AUTHENTICATION_INFO():
    HTTP_SERVER_AUTHENTICATION_INFO = win32more.Networking.HttpServer.HTTP_SERVER_AUTHENTICATION_INFO_head
    HTTP_SERVER_AUTHENTICATION_INFO._fields_ = [
        ("Flags", win32more.Networking.HttpServer.HTTP_PROPERTY_FLAGS),
        ("AuthSchemes", UInt32),
        ("ReceiveMutualAuth", win32more.Foundation.BOOLEAN),
        ("ReceiveContextHandle", win32more.Foundation.BOOLEAN),
        ("DisableNTLMCredentialCaching", win32more.Foundation.BOOLEAN),
        ("ExFlags", Byte),
        ("DigestParams", win32more.Networking.HttpServer.HTTP_SERVER_AUTHENTICATION_DIGEST_PARAMS),
        ("BasicParams", win32more.Networking.HttpServer.HTTP_SERVER_AUTHENTICATION_BASIC_PARAMS),
    ]
    return HTTP_SERVER_AUTHENTICATION_INFO
HTTP_SERVICE_BINDING_TYPE = Int32
HTTP_SERVICE_BINDING_TYPE_HttpServiceBindingTypeNone = 0
HTTP_SERVICE_BINDING_TYPE_HttpServiceBindingTypeW = 1
HTTP_SERVICE_BINDING_TYPE_HttpServiceBindingTypeA = 2
def _define_HTTP_SERVICE_BINDING_BASE_head():
    class HTTP_SERVICE_BINDING_BASE(Structure):
        pass
    return HTTP_SERVICE_BINDING_BASE
def _define_HTTP_SERVICE_BINDING_BASE():
    HTTP_SERVICE_BINDING_BASE = win32more.Networking.HttpServer.HTTP_SERVICE_BINDING_BASE_head
    HTTP_SERVICE_BINDING_BASE._fields_ = [
        ("Type", win32more.Networking.HttpServer.HTTP_SERVICE_BINDING_TYPE),
    ]
    return HTTP_SERVICE_BINDING_BASE
def _define_HTTP_SERVICE_BINDING_A_head():
    class HTTP_SERVICE_BINDING_A(Structure):
        pass
    return HTTP_SERVICE_BINDING_A
def _define_HTTP_SERVICE_BINDING_A():
    HTTP_SERVICE_BINDING_A = win32more.Networking.HttpServer.HTTP_SERVICE_BINDING_A_head
    HTTP_SERVICE_BINDING_A._fields_ = [
        ("Base", win32more.Networking.HttpServer.HTTP_SERVICE_BINDING_BASE),
        ("Buffer", win32more.Foundation.PSTR),
        ("BufferSize", UInt32),
    ]
    return HTTP_SERVICE_BINDING_A
def _define_HTTP_SERVICE_BINDING_W_head():
    class HTTP_SERVICE_BINDING_W(Structure):
        pass
    return HTTP_SERVICE_BINDING_W
def _define_HTTP_SERVICE_BINDING_W():
    HTTP_SERVICE_BINDING_W = win32more.Networking.HttpServer.HTTP_SERVICE_BINDING_W_head
    HTTP_SERVICE_BINDING_W._fields_ = [
        ("Base", win32more.Networking.HttpServer.HTTP_SERVICE_BINDING_BASE),
        ("Buffer", win32more.Foundation.PWSTR),
        ("BufferSize", UInt32),
    ]
    return HTTP_SERVICE_BINDING_W
HTTP_AUTHENTICATION_HARDENING_LEVELS = Int32
HTTP_AUTHENTICATION_HARDENING_LEVELS_HttpAuthenticationHardeningLegacy = 0
HTTP_AUTHENTICATION_HARDENING_LEVELS_HttpAuthenticationHardeningMedium = 1
HTTP_AUTHENTICATION_HARDENING_LEVELS_HttpAuthenticationHardeningStrict = 2
def _define_HTTP_CHANNEL_BIND_INFO_head():
    class HTTP_CHANNEL_BIND_INFO(Structure):
        pass
    return HTTP_CHANNEL_BIND_INFO
def _define_HTTP_CHANNEL_BIND_INFO():
    HTTP_CHANNEL_BIND_INFO = win32more.Networking.HttpServer.HTTP_CHANNEL_BIND_INFO_head
    HTTP_CHANNEL_BIND_INFO._fields_ = [
        ("Hardening", win32more.Networking.HttpServer.HTTP_AUTHENTICATION_HARDENING_LEVELS),
        ("Flags", UInt32),
        ("ServiceNames", POINTER(POINTER(win32more.Networking.HttpServer.HTTP_SERVICE_BINDING_BASE_head))),
        ("NumberOfServiceNames", UInt32),
    ]
    return HTTP_CHANNEL_BIND_INFO
def _define_HTTP_REQUEST_CHANNEL_BIND_STATUS_head():
    class HTTP_REQUEST_CHANNEL_BIND_STATUS(Structure):
        pass
    return HTTP_REQUEST_CHANNEL_BIND_STATUS
def _define_HTTP_REQUEST_CHANNEL_BIND_STATUS():
    HTTP_REQUEST_CHANNEL_BIND_STATUS = win32more.Networking.HttpServer.HTTP_REQUEST_CHANNEL_BIND_STATUS_head
    HTTP_REQUEST_CHANNEL_BIND_STATUS._fields_ = [
        ("ServiceName", POINTER(win32more.Networking.HttpServer.HTTP_SERVICE_BINDING_BASE_head)),
        ("ChannelToken", c_char_p_no),
        ("ChannelTokenSize", UInt32),
        ("Flags", UInt32),
    ]
    return HTTP_REQUEST_CHANNEL_BIND_STATUS
def _define_HTTP_REQUEST_TOKEN_BINDING_INFO_head():
    class HTTP_REQUEST_TOKEN_BINDING_INFO(Structure):
        pass
    return HTTP_REQUEST_TOKEN_BINDING_INFO
def _define_HTTP_REQUEST_TOKEN_BINDING_INFO():
    HTTP_REQUEST_TOKEN_BINDING_INFO = win32more.Networking.HttpServer.HTTP_REQUEST_TOKEN_BINDING_INFO_head
    HTTP_REQUEST_TOKEN_BINDING_INFO._fields_ = [
        ("TokenBinding", c_char_p_no),
        ("TokenBindingSize", UInt32),
        ("EKM", c_char_p_no),
        ("EKMSize", UInt32),
        ("KeyType", Byte),
    ]
    return HTTP_REQUEST_TOKEN_BINDING_INFO
HTTP_LOGGING_TYPE = Int32
HTTP_LOGGING_TYPE_HttpLoggingTypeW3C = 0
HTTP_LOGGING_TYPE_HttpLoggingTypeIIS = 1
HTTP_LOGGING_TYPE_HttpLoggingTypeNCSA = 2
HTTP_LOGGING_TYPE_HttpLoggingTypeRaw = 3
HTTP_LOGGING_ROLLOVER_TYPE = Int32
HTTP_LOGGING_ROLLOVER_TYPE_HttpLoggingRolloverSize = 0
HTTP_LOGGING_ROLLOVER_TYPE_HttpLoggingRolloverDaily = 1
HTTP_LOGGING_ROLLOVER_TYPE_HttpLoggingRolloverWeekly = 2
HTTP_LOGGING_ROLLOVER_TYPE_HttpLoggingRolloverMonthly = 3
HTTP_LOGGING_ROLLOVER_TYPE_HttpLoggingRolloverHourly = 4
def _define_HTTP_LOGGING_INFO_head():
    class HTTP_LOGGING_INFO(Structure):
        pass
    return HTTP_LOGGING_INFO
def _define_HTTP_LOGGING_INFO():
    HTTP_LOGGING_INFO = win32more.Networking.HttpServer.HTTP_LOGGING_INFO_head
    HTTP_LOGGING_INFO._fields_ = [
        ("Flags", win32more.Networking.HttpServer.HTTP_PROPERTY_FLAGS),
        ("LoggingFlags", UInt32),
        ("SoftwareName", win32more.Foundation.PWSTR),
        ("SoftwareNameLength", UInt16),
        ("DirectoryNameLength", UInt16),
        ("DirectoryName", win32more.Foundation.PWSTR),
        ("Format", win32more.Networking.HttpServer.HTTP_LOGGING_TYPE),
        ("Fields", UInt32),
        ("pExtFields", c_void_p),
        ("NumOfExtFields", UInt16),
        ("MaxRecordSize", UInt16),
        ("RolloverType", win32more.Networking.HttpServer.HTTP_LOGGING_ROLLOVER_TYPE),
        ("RolloverSize", UInt32),
        ("pSecurityDescriptor", POINTER(win32more.Security.SECURITY_DESCRIPTOR_head)),
    ]
    return HTTP_LOGGING_INFO
def _define_HTTP_BINDING_INFO_head():
    class HTTP_BINDING_INFO(Structure):
        pass
    return HTTP_BINDING_INFO
def _define_HTTP_BINDING_INFO():
    HTTP_BINDING_INFO = win32more.Networking.HttpServer.HTTP_BINDING_INFO_head
    HTTP_BINDING_INFO._fields_ = [
        ("Flags", win32more.Networking.HttpServer.HTTP_PROPERTY_FLAGS),
        ("RequestQueueHandle", win32more.Foundation.HANDLE),
    ]
    return HTTP_BINDING_INFO
HTTP_PROTECTION_LEVEL_TYPE = Int32
HTTP_PROTECTION_LEVEL_TYPE_HttpProtectionLevelUnrestricted = 0
HTTP_PROTECTION_LEVEL_TYPE_HttpProtectionLevelEdgeRestricted = 1
HTTP_PROTECTION_LEVEL_TYPE_HttpProtectionLevelRestricted = 2
def _define_HTTP_PROTECTION_LEVEL_INFO_head():
    class HTTP_PROTECTION_LEVEL_INFO(Structure):
        pass
    return HTTP_PROTECTION_LEVEL_INFO
def _define_HTTP_PROTECTION_LEVEL_INFO():
    HTTP_PROTECTION_LEVEL_INFO = win32more.Networking.HttpServer.HTTP_PROTECTION_LEVEL_INFO_head
    HTTP_PROTECTION_LEVEL_INFO._fields_ = [
        ("Flags", win32more.Networking.HttpServer.HTTP_PROPERTY_FLAGS),
        ("Level", win32more.Networking.HttpServer.HTTP_PROTECTION_LEVEL_TYPE),
    ]
    return HTTP_PROTECTION_LEVEL_INFO
def _define_HTTP_BYTE_RANGE_head():
    class HTTP_BYTE_RANGE(Structure):
        pass
    return HTTP_BYTE_RANGE
def _define_HTTP_BYTE_RANGE():
    HTTP_BYTE_RANGE = win32more.Networking.HttpServer.HTTP_BYTE_RANGE_head
    HTTP_BYTE_RANGE._fields_ = [
        ("StartingOffset", win32more.Foundation.ULARGE_INTEGER),
        ("Length", win32more.Foundation.ULARGE_INTEGER),
    ]
    return HTTP_BYTE_RANGE
def _define_HTTP_VERSION_head():
    class HTTP_VERSION(Structure):
        pass
    return HTTP_VERSION
def _define_HTTP_VERSION():
    HTTP_VERSION = win32more.Networking.HttpServer.HTTP_VERSION_head
    HTTP_VERSION._fields_ = [
        ("MajorVersion", UInt16),
        ("MinorVersion", UInt16),
    ]
    return HTTP_VERSION
HTTP_SCHEME = Int32
HTTP_SCHEME_HttpSchemeHttp = 0
HTTP_SCHEME_HttpSchemeHttps = 1
HTTP_SCHEME_HttpSchemeMaximum = 2
HTTP_VERB = Int32
HTTP_VERB_HttpVerbUnparsed = 0
HTTP_VERB_HttpVerbUnknown = 1
HTTP_VERB_HttpVerbInvalid = 2
HTTP_VERB_HttpVerbOPTIONS = 3
HTTP_VERB_HttpVerbGET = 4
HTTP_VERB_HttpVerbHEAD = 5
HTTP_VERB_HttpVerbPOST = 6
HTTP_VERB_HttpVerbPUT = 7
HTTP_VERB_HttpVerbDELETE = 8
HTTP_VERB_HttpVerbTRACE = 9
HTTP_VERB_HttpVerbCONNECT = 10
HTTP_VERB_HttpVerbTRACK = 11
HTTP_VERB_HttpVerbMOVE = 12
HTTP_VERB_HttpVerbCOPY = 13
HTTP_VERB_HttpVerbPROPFIND = 14
HTTP_VERB_HttpVerbPROPPATCH = 15
HTTP_VERB_HttpVerbMKCOL = 16
HTTP_VERB_HttpVerbLOCK = 17
HTTP_VERB_HttpVerbUNLOCK = 18
HTTP_VERB_HttpVerbSEARCH = 19
HTTP_VERB_HttpVerbMaximum = 20
HTTP_HEADER_ID = Int32
HTTP_HEADER_ID_HttpHeaderCacheControl = 0
HTTP_HEADER_ID_HttpHeaderConnection = 1
HTTP_HEADER_ID_HttpHeaderDate = 2
HTTP_HEADER_ID_HttpHeaderKeepAlive = 3
HTTP_HEADER_ID_HttpHeaderPragma = 4
HTTP_HEADER_ID_HttpHeaderTrailer = 5
HTTP_HEADER_ID_HttpHeaderTransferEncoding = 6
HTTP_HEADER_ID_HttpHeaderUpgrade = 7
HTTP_HEADER_ID_HttpHeaderVia = 8
HTTP_HEADER_ID_HttpHeaderWarning = 9
HTTP_HEADER_ID_HttpHeaderAllow = 10
HTTP_HEADER_ID_HttpHeaderContentLength = 11
HTTP_HEADER_ID_HttpHeaderContentType = 12
HTTP_HEADER_ID_HttpHeaderContentEncoding = 13
HTTP_HEADER_ID_HttpHeaderContentLanguage = 14
HTTP_HEADER_ID_HttpHeaderContentLocation = 15
HTTP_HEADER_ID_HttpHeaderContentMd5 = 16
HTTP_HEADER_ID_HttpHeaderContentRange = 17
HTTP_HEADER_ID_HttpHeaderExpires = 18
HTTP_HEADER_ID_HttpHeaderLastModified = 19
HTTP_HEADER_ID_HttpHeaderAccept = 20
HTTP_HEADER_ID_HttpHeaderAcceptCharset = 21
HTTP_HEADER_ID_HttpHeaderAcceptEncoding = 22
HTTP_HEADER_ID_HttpHeaderAcceptLanguage = 23
HTTP_HEADER_ID_HttpHeaderAuthorization = 24
HTTP_HEADER_ID_HttpHeaderCookie = 25
HTTP_HEADER_ID_HttpHeaderExpect = 26
HTTP_HEADER_ID_HttpHeaderFrom = 27
HTTP_HEADER_ID_HttpHeaderHost = 28
HTTP_HEADER_ID_HttpHeaderIfMatch = 29
HTTP_HEADER_ID_HttpHeaderIfModifiedSince = 30
HTTP_HEADER_ID_HttpHeaderIfNoneMatch = 31
HTTP_HEADER_ID_HttpHeaderIfRange = 32
HTTP_HEADER_ID_HttpHeaderIfUnmodifiedSince = 33
HTTP_HEADER_ID_HttpHeaderMaxForwards = 34
HTTP_HEADER_ID_HttpHeaderProxyAuthorization = 35
HTTP_HEADER_ID_HttpHeaderReferer = 36
HTTP_HEADER_ID_HttpHeaderRange = 37
HTTP_HEADER_ID_HttpHeaderTe = 38
HTTP_HEADER_ID_HttpHeaderTranslate = 39
HTTP_HEADER_ID_HttpHeaderUserAgent = 40
HTTP_HEADER_ID_HttpHeaderRequestMaximum = 41
HTTP_HEADER_ID_HttpHeaderAcceptRanges = 20
HTTP_HEADER_ID_HttpHeaderAge = 21
HTTP_HEADER_ID_HttpHeaderEtag = 22
HTTP_HEADER_ID_HttpHeaderLocation = 23
HTTP_HEADER_ID_HttpHeaderProxyAuthenticate = 24
HTTP_HEADER_ID_HttpHeaderRetryAfter = 25
HTTP_HEADER_ID_HttpHeaderServer = 26
HTTP_HEADER_ID_HttpHeaderSetCookie = 27
HTTP_HEADER_ID_HttpHeaderVary = 28
HTTP_HEADER_ID_HttpHeaderWwwAuthenticate = 29
HTTP_HEADER_ID_HttpHeaderResponseMaximum = 30
HTTP_HEADER_ID_HttpHeaderMaximum = 41
def _define_HTTP_KNOWN_HEADER_head():
    class HTTP_KNOWN_HEADER(Structure):
        pass
    return HTTP_KNOWN_HEADER
def _define_HTTP_KNOWN_HEADER():
    HTTP_KNOWN_HEADER = win32more.Networking.HttpServer.HTTP_KNOWN_HEADER_head
    HTTP_KNOWN_HEADER._fields_ = [
        ("RawValueLength", UInt16),
        ("pRawValue", win32more.Foundation.PSTR),
    ]
    return HTTP_KNOWN_HEADER
def _define_HTTP_UNKNOWN_HEADER_head():
    class HTTP_UNKNOWN_HEADER(Structure):
        pass
    return HTTP_UNKNOWN_HEADER
def _define_HTTP_UNKNOWN_HEADER():
    HTTP_UNKNOWN_HEADER = win32more.Networking.HttpServer.HTTP_UNKNOWN_HEADER_head
    HTTP_UNKNOWN_HEADER._fields_ = [
        ("NameLength", UInt16),
        ("RawValueLength", UInt16),
        ("pName", win32more.Foundation.PSTR),
        ("pRawValue", win32more.Foundation.PSTR),
    ]
    return HTTP_UNKNOWN_HEADER
HTTP_LOG_DATA_TYPE = Int32
HTTP_LOG_DATA_TYPE_HttpLogDataTypeFields = 0
def _define_HTTP_LOG_DATA_head():
    class HTTP_LOG_DATA(Structure):
        pass
    return HTTP_LOG_DATA
def _define_HTTP_LOG_DATA():
    HTTP_LOG_DATA = win32more.Networking.HttpServer.HTTP_LOG_DATA_head
    HTTP_LOG_DATA._fields_ = [
        ("Type", win32more.Networking.HttpServer.HTTP_LOG_DATA_TYPE),
    ]
    return HTTP_LOG_DATA
def _define_HTTP_LOG_FIELDS_DATA_head():
    class HTTP_LOG_FIELDS_DATA(Structure):
        pass
    return HTTP_LOG_FIELDS_DATA
def _define_HTTP_LOG_FIELDS_DATA():
    HTTP_LOG_FIELDS_DATA = win32more.Networking.HttpServer.HTTP_LOG_FIELDS_DATA_head
    HTTP_LOG_FIELDS_DATA._fields_ = [
        ("Base", win32more.Networking.HttpServer.HTTP_LOG_DATA),
        ("UserNameLength", UInt16),
        ("UriStemLength", UInt16),
        ("ClientIpLength", UInt16),
        ("ServerNameLength", UInt16),
        ("ServiceNameLength", UInt16),
        ("ServerIpLength", UInt16),
        ("MethodLength", UInt16),
        ("UriQueryLength", UInt16),
        ("HostLength", UInt16),
        ("UserAgentLength", UInt16),
        ("CookieLength", UInt16),
        ("ReferrerLength", UInt16),
        ("UserName", win32more.Foundation.PWSTR),
        ("UriStem", win32more.Foundation.PWSTR),
        ("ClientIp", win32more.Foundation.PSTR),
        ("ServerName", win32more.Foundation.PSTR),
        ("ServiceName", win32more.Foundation.PSTR),
        ("ServerIp", win32more.Foundation.PSTR),
        ("Method", win32more.Foundation.PSTR),
        ("UriQuery", win32more.Foundation.PSTR),
        ("Host", win32more.Foundation.PSTR),
        ("UserAgent", win32more.Foundation.PSTR),
        ("Cookie", win32more.Foundation.PSTR),
        ("Referrer", win32more.Foundation.PSTR),
        ("ServerPort", UInt16),
        ("ProtocolStatus", UInt16),
        ("Win32Status", UInt32),
        ("MethodNum", win32more.Networking.HttpServer.HTTP_VERB),
        ("SubStatus", UInt16),
    ]
    return HTTP_LOG_FIELDS_DATA
HTTP_DATA_CHUNK_TYPE = Int32
HTTP_DATA_CHUNK_TYPE_HttpDataChunkFromMemory = 0
HTTP_DATA_CHUNK_TYPE_HttpDataChunkFromFileHandle = 1
HTTP_DATA_CHUNK_TYPE_HttpDataChunkFromFragmentCache = 2
HTTP_DATA_CHUNK_TYPE_HttpDataChunkFromFragmentCacheEx = 3
HTTP_DATA_CHUNK_TYPE_HttpDataChunkTrailers = 4
HTTP_DATA_CHUNK_TYPE_HttpDataChunkMaximum = 5
def _define_HTTP_DATA_CHUNK_head():
    class HTTP_DATA_CHUNK(Structure):
        pass
    return HTTP_DATA_CHUNK
def _define_HTTP_DATA_CHUNK():
    HTTP_DATA_CHUNK = win32more.Networking.HttpServer.HTTP_DATA_CHUNK_head
    class HTTP_DATA_CHUNK__Anonymous_e__Union(Union):
        pass
    class HTTP_DATA_CHUNK__Anonymous_e__Union__FromFragmentCacheEx_e__Struct(Structure):
        pass
    HTTP_DATA_CHUNK__Anonymous_e__Union__FromFragmentCacheEx_e__Struct._fields_ = [
        ("ByteRange", win32more.Networking.HttpServer.HTTP_BYTE_RANGE),
        ("pFragmentName", win32more.Foundation.PWSTR),
    ]
    class HTTP_DATA_CHUNK__Anonymous_e__Union__FromFileHandle_e__Struct(Structure):
        pass
    HTTP_DATA_CHUNK__Anonymous_e__Union__FromFileHandle_e__Struct._fields_ = [
        ("ByteRange", win32more.Networking.HttpServer.HTTP_BYTE_RANGE),
        ("FileHandle", win32more.Foundation.HANDLE),
    ]
    class HTTP_DATA_CHUNK__Anonymous_e__Union__FromFragmentCache_e__Struct(Structure):
        pass
    HTTP_DATA_CHUNK__Anonymous_e__Union__FromFragmentCache_e__Struct._fields_ = [
        ("FragmentNameLength", UInt16),
        ("pFragmentName", win32more.Foundation.PWSTR),
    ]
    class HTTP_DATA_CHUNK__Anonymous_e__Union__FromMemory_e__Struct(Structure):
        pass
    HTTP_DATA_CHUNK__Anonymous_e__Union__FromMemory_e__Struct._fields_ = [
        ("pBuffer", c_void_p),
        ("BufferLength", UInt32),
    ]
    class HTTP_DATA_CHUNK__Anonymous_e__Union__Trailers_e__Struct(Structure):
        pass
    HTTP_DATA_CHUNK__Anonymous_e__Union__Trailers_e__Struct._fields_ = [
        ("TrailerCount", UInt16),
        ("pTrailers", POINTER(win32more.Networking.HttpServer.HTTP_UNKNOWN_HEADER_head)),
    ]
    HTTP_DATA_CHUNK__Anonymous_e__Union._fields_ = [
        ("FromMemory", HTTP_DATA_CHUNK__Anonymous_e__Union__FromMemory_e__Struct),
        ("FromFileHandle", HTTP_DATA_CHUNK__Anonymous_e__Union__FromFileHandle_e__Struct),
        ("FromFragmentCache", HTTP_DATA_CHUNK__Anonymous_e__Union__FromFragmentCache_e__Struct),
        ("FromFragmentCacheEx", HTTP_DATA_CHUNK__Anonymous_e__Union__FromFragmentCacheEx_e__Struct),
        ("Trailers", HTTP_DATA_CHUNK__Anonymous_e__Union__Trailers_e__Struct),
    ]
    HTTP_DATA_CHUNK._anonymous_ = [
        'Anonymous',
    ]
    HTTP_DATA_CHUNK._fields_ = [
        ("DataChunkType", win32more.Networking.HttpServer.HTTP_DATA_CHUNK_TYPE),
        ("Anonymous", HTTP_DATA_CHUNK__Anonymous_e__Union),
    ]
    return HTTP_DATA_CHUNK
def _define_HTTP_REQUEST_HEADERS_head():
    class HTTP_REQUEST_HEADERS(Structure):
        pass
    return HTTP_REQUEST_HEADERS
def _define_HTTP_REQUEST_HEADERS():
    HTTP_REQUEST_HEADERS = win32more.Networking.HttpServer.HTTP_REQUEST_HEADERS_head
    HTTP_REQUEST_HEADERS._fields_ = [
        ("UnknownHeaderCount", UInt16),
        ("pUnknownHeaders", POINTER(win32more.Networking.HttpServer.HTTP_UNKNOWN_HEADER_head)),
        ("TrailerCount", UInt16),
        ("pTrailers", POINTER(win32more.Networking.HttpServer.HTTP_UNKNOWN_HEADER_head)),
        ("KnownHeaders", win32more.Networking.HttpServer.HTTP_KNOWN_HEADER * 41),
    ]
    return HTTP_REQUEST_HEADERS
def _define_HTTP_RESPONSE_HEADERS_head():
    class HTTP_RESPONSE_HEADERS(Structure):
        pass
    return HTTP_RESPONSE_HEADERS
def _define_HTTP_RESPONSE_HEADERS():
    HTTP_RESPONSE_HEADERS = win32more.Networking.HttpServer.HTTP_RESPONSE_HEADERS_head
    HTTP_RESPONSE_HEADERS._fields_ = [
        ("UnknownHeaderCount", UInt16),
        ("pUnknownHeaders", POINTER(win32more.Networking.HttpServer.HTTP_UNKNOWN_HEADER_head)),
        ("TrailerCount", UInt16),
        ("pTrailers", POINTER(win32more.Networking.HttpServer.HTTP_UNKNOWN_HEADER_head)),
        ("KnownHeaders", win32more.Networking.HttpServer.HTTP_KNOWN_HEADER * 30),
    ]
    return HTTP_RESPONSE_HEADERS
HTTP_DELEGATE_REQUEST_PROPERTY_ID = Int32
HTTP_DELEGATE_REQUEST_PROPERTY_ID_DelegateRequestReservedProperty = 0
HTTP_DELEGATE_REQUEST_PROPERTY_ID_DelegateRequestDelegateUrlProperty = 1
def _define_HTTP_DELEGATE_REQUEST_PROPERTY_INFO_head():
    class HTTP_DELEGATE_REQUEST_PROPERTY_INFO(Structure):
        pass
    return HTTP_DELEGATE_REQUEST_PROPERTY_INFO
def _define_HTTP_DELEGATE_REQUEST_PROPERTY_INFO():
    HTTP_DELEGATE_REQUEST_PROPERTY_INFO = win32more.Networking.HttpServer.HTTP_DELEGATE_REQUEST_PROPERTY_INFO_head
    HTTP_DELEGATE_REQUEST_PROPERTY_INFO._fields_ = [
        ("PropertyId", win32more.Networking.HttpServer.HTTP_DELEGATE_REQUEST_PROPERTY_ID),
        ("PropertyInfoLength", UInt32),
        ("PropertyInfo", c_void_p),
    ]
    return HTTP_DELEGATE_REQUEST_PROPERTY_INFO
HTTP_CREATE_REQUEST_QUEUE_PROPERTY_ID = Int32
HTTP_CREATE_REQUEST_QUEUE_PROPERTY_ID_CreateRequestQueueExternalIdProperty = 1
HTTP_CREATE_REQUEST_QUEUE_PROPERTY_ID_CreateRequestQueueMax = 2
def _define_HTTP_CREATE_REQUEST_QUEUE_PROPERTY_INFO_head():
    class HTTP_CREATE_REQUEST_QUEUE_PROPERTY_INFO(Structure):
        pass
    return HTTP_CREATE_REQUEST_QUEUE_PROPERTY_INFO
def _define_HTTP_CREATE_REQUEST_QUEUE_PROPERTY_INFO():
    HTTP_CREATE_REQUEST_QUEUE_PROPERTY_INFO = win32more.Networking.HttpServer.HTTP_CREATE_REQUEST_QUEUE_PROPERTY_INFO_head
    HTTP_CREATE_REQUEST_QUEUE_PROPERTY_INFO._fields_ = [
        ("PropertyId", win32more.Networking.HttpServer.HTTP_CREATE_REQUEST_QUEUE_PROPERTY_ID),
        ("PropertyInfoLength", UInt32),
        ("PropertyInfo", c_void_p),
    ]
    return HTTP_CREATE_REQUEST_QUEUE_PROPERTY_INFO
def _define_HTTP_TRANSPORT_ADDRESS_head():
    class HTTP_TRANSPORT_ADDRESS(Structure):
        pass
    return HTTP_TRANSPORT_ADDRESS
def _define_HTTP_TRANSPORT_ADDRESS():
    HTTP_TRANSPORT_ADDRESS = win32more.Networking.HttpServer.HTTP_TRANSPORT_ADDRESS_head
    HTTP_TRANSPORT_ADDRESS._fields_ = [
        ("pRemoteAddress", POINTER(win32more.Networking.WinSock.SOCKADDR_head)),
        ("pLocalAddress", POINTER(win32more.Networking.WinSock.SOCKADDR_head)),
    ]
    return HTTP_TRANSPORT_ADDRESS
def _define_HTTP_COOKED_URL_head():
    class HTTP_COOKED_URL(Structure):
        pass
    return HTTP_COOKED_URL
def _define_HTTP_COOKED_URL():
    HTTP_COOKED_URL = win32more.Networking.HttpServer.HTTP_COOKED_URL_head
    HTTP_COOKED_URL._fields_ = [
        ("FullUrlLength", UInt16),
        ("HostLength", UInt16),
        ("AbsPathLength", UInt16),
        ("QueryStringLength", UInt16),
        ("pFullUrl", win32more.Foundation.PWSTR),
        ("pHost", win32more.Foundation.PWSTR),
        ("pAbsPath", win32more.Foundation.PWSTR),
        ("pQueryString", win32more.Foundation.PWSTR),
    ]
    return HTTP_COOKED_URL
HTTP_AUTH_STATUS = Int32
HTTP_AUTH_STATUS_HttpAuthStatusSuccess = 0
HTTP_AUTH_STATUS_HttpAuthStatusNotAuthenticated = 1
HTTP_AUTH_STATUS_HttpAuthStatusFailure = 2
HTTP_REQUEST_AUTH_TYPE = Int32
HTTP_REQUEST_AUTH_TYPE_HttpRequestAuthTypeNone = 0
HTTP_REQUEST_AUTH_TYPE_HttpRequestAuthTypeBasic = 1
HTTP_REQUEST_AUTH_TYPE_HttpRequestAuthTypeDigest = 2
HTTP_REQUEST_AUTH_TYPE_HttpRequestAuthTypeNTLM = 3
HTTP_REQUEST_AUTH_TYPE_HttpRequestAuthTypeNegotiate = 4
HTTP_REQUEST_AUTH_TYPE_HttpRequestAuthTypeKerberos = 5
def _define_HTTP_SSL_CLIENT_CERT_INFO_head():
    class HTTP_SSL_CLIENT_CERT_INFO(Structure):
        pass
    return HTTP_SSL_CLIENT_CERT_INFO
def _define_HTTP_SSL_CLIENT_CERT_INFO():
    HTTP_SSL_CLIENT_CERT_INFO = win32more.Networking.HttpServer.HTTP_SSL_CLIENT_CERT_INFO_head
    HTTP_SSL_CLIENT_CERT_INFO._fields_ = [
        ("CertFlags", UInt32),
        ("CertEncodedSize", UInt32),
        ("pCertEncoded", c_char_p_no),
        ("Token", win32more.Foundation.HANDLE),
        ("CertDeniedByMapper", win32more.Foundation.BOOLEAN),
    ]
    return HTTP_SSL_CLIENT_CERT_INFO
def _define_HTTP_SSL_INFO_head():
    class HTTP_SSL_INFO(Structure):
        pass
    return HTTP_SSL_INFO
def _define_HTTP_SSL_INFO():
    HTTP_SSL_INFO = win32more.Networking.HttpServer.HTTP_SSL_INFO_head
    HTTP_SSL_INFO._fields_ = [
        ("ServerCertKeySize", UInt16),
        ("ConnectionKeySize", UInt16),
        ("ServerCertIssuerSize", UInt32),
        ("ServerCertSubjectSize", UInt32),
        ("pServerCertIssuer", win32more.Foundation.PSTR),
        ("pServerCertSubject", win32more.Foundation.PSTR),
        ("pClientCertInfo", POINTER(win32more.Networking.HttpServer.HTTP_SSL_CLIENT_CERT_INFO_head)),
        ("SslClientCertNegotiated", UInt32),
    ]
    return HTTP_SSL_INFO
def _define_HTTP_SSL_PROTOCOL_INFO_head():
    class HTTP_SSL_PROTOCOL_INFO(Structure):
        pass
    return HTTP_SSL_PROTOCOL_INFO
def _define_HTTP_SSL_PROTOCOL_INFO():
    HTTP_SSL_PROTOCOL_INFO = win32more.Networking.HttpServer.HTTP_SSL_PROTOCOL_INFO_head
    HTTP_SSL_PROTOCOL_INFO._fields_ = [
        ("Protocol", UInt32),
        ("CipherType", UInt32),
        ("CipherStrength", UInt32),
        ("HashType", UInt32),
        ("HashStrength", UInt32),
        ("KeyExchangeType", UInt32),
        ("KeyExchangeStrength", UInt32),
    ]
    return HTTP_SSL_PROTOCOL_INFO
HTTP_REQUEST_SIZING_TYPE = Int32
HTTP_REQUEST_SIZING_TYPE_HttpRequestSizingTypeTlsHandshakeLeg1ClientData = 0
HTTP_REQUEST_SIZING_TYPE_HttpRequestSizingTypeTlsHandshakeLeg1ServerData = 1
HTTP_REQUEST_SIZING_TYPE_HttpRequestSizingTypeTlsHandshakeLeg2ClientData = 2
HTTP_REQUEST_SIZING_TYPE_HttpRequestSizingTypeTlsHandshakeLeg2ServerData = 3
HTTP_REQUEST_SIZING_TYPE_HttpRequestSizingTypeHeaders = 4
HTTP_REQUEST_SIZING_TYPE_HttpRequestSizingTypeMax = 5
def _define_HTTP_REQUEST_SIZING_INFO_head():
    class HTTP_REQUEST_SIZING_INFO(Structure):
        pass
    return HTTP_REQUEST_SIZING_INFO
def _define_HTTP_REQUEST_SIZING_INFO():
    HTTP_REQUEST_SIZING_INFO = win32more.Networking.HttpServer.HTTP_REQUEST_SIZING_INFO_head
    HTTP_REQUEST_SIZING_INFO._fields_ = [
        ("Flags", UInt64),
        ("RequestIndex", UInt32),
        ("RequestSizingCount", UInt32),
        ("RequestSizing", UInt64 * 5),
    ]
    return HTTP_REQUEST_SIZING_INFO
HTTP_REQUEST_TIMING_TYPE = Int32
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeConnectionStart = 0
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeDataStart = 1
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsCertificateLoadStart = 2
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsCertificateLoadEnd = 3
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsHandshakeLeg1Start = 4
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsHandshakeLeg1End = 5
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsHandshakeLeg2Start = 6
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsHandshakeLeg2End = 7
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsAttributesQueryStart = 8
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsAttributesQueryEnd = 9
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsClientCertQueryStart = 10
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsClientCertQueryEnd = 11
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeHttp2StreamStart = 12
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeHttp2HeaderDecodeStart = 13
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeHttp2HeaderDecodeEnd = 14
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestHeaderParseStart = 15
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestHeaderParseEnd = 16
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestRoutingStart = 17
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestRoutingEnd = 18
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestQueuedForInspection = 19
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestDeliveredForInspection = 20
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestReturnedAfterInspection = 21
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestQueuedForDelegation = 22
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestDeliveredForDelegation = 23
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestReturnedAfterDelegation = 24
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestQueuedForIO = 25
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestDeliveredForIO = 26
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeHttp3StreamStart = 27
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeHttp3HeaderDecodeStart = 28
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeHttp3HeaderDecodeEnd = 29
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeMax = 30
def _define_HTTP_REQUEST_TIMING_INFO_head():
    class HTTP_REQUEST_TIMING_INFO(Structure):
        pass
    return HTTP_REQUEST_TIMING_INFO
def _define_HTTP_REQUEST_TIMING_INFO():
    HTTP_REQUEST_TIMING_INFO = win32more.Networking.HttpServer.HTTP_REQUEST_TIMING_INFO_head
    HTTP_REQUEST_TIMING_INFO._fields_ = [
        ("RequestTimingCount", UInt32),
        ("RequestTiming", UInt64 * 30),
    ]
    return HTTP_REQUEST_TIMING_INFO
HTTP_REQUEST_INFO_TYPE = Int32
HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeAuth = 0
HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeChannelBind = 1
HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeSslProtocol = 2
HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeSslTokenBindingDraft = 3
HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeSslTokenBinding = 4
HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeRequestTiming = 5
HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeTcpInfoV0 = 6
HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeRequestSizing = 7
HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeQuicStats = 8
HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeTcpInfoV1 = 9
def _define_HTTP_REQUEST_INFO_head():
    class HTTP_REQUEST_INFO(Structure):
        pass
    return HTTP_REQUEST_INFO
def _define_HTTP_REQUEST_INFO():
    HTTP_REQUEST_INFO = win32more.Networking.HttpServer.HTTP_REQUEST_INFO_head
    HTTP_REQUEST_INFO._fields_ = [
        ("InfoType", win32more.Networking.HttpServer.HTTP_REQUEST_INFO_TYPE),
        ("InfoLength", UInt32),
        ("pInfo", c_void_p),
    ]
    return HTTP_REQUEST_INFO
def _define_HTTP_REQUEST_AUTH_INFO_head():
    class HTTP_REQUEST_AUTH_INFO(Structure):
        pass
    return HTTP_REQUEST_AUTH_INFO
def _define_HTTP_REQUEST_AUTH_INFO():
    HTTP_REQUEST_AUTH_INFO = win32more.Networking.HttpServer.HTTP_REQUEST_AUTH_INFO_head
    HTTP_REQUEST_AUTH_INFO._fields_ = [
        ("AuthStatus", win32more.Networking.HttpServer.HTTP_AUTH_STATUS),
        ("SecStatus", Int32),
        ("Flags", UInt32),
        ("AuthType", win32more.Networking.HttpServer.HTTP_REQUEST_AUTH_TYPE),
        ("AccessToken", win32more.Foundation.HANDLE),
        ("ContextAttributes", UInt32),
        ("PackedContextLength", UInt32),
        ("PackedContextType", UInt32),
        ("PackedContext", c_void_p),
        ("MutualAuthDataLength", UInt32),
        ("pMutualAuthData", win32more.Foundation.PSTR),
        ("PackageNameLength", UInt16),
        ("pPackageName", win32more.Foundation.PWSTR),
    ]
    return HTTP_REQUEST_AUTH_INFO
def _define_HTTP_REQUEST_V1_head():
    class HTTP_REQUEST_V1(Structure):
        pass
    return HTTP_REQUEST_V1
def _define_HTTP_REQUEST_V1():
    HTTP_REQUEST_V1 = win32more.Networking.HttpServer.HTTP_REQUEST_V1_head
    HTTP_REQUEST_V1._fields_ = [
        ("Flags", UInt32),
        ("ConnectionId", UInt64),
        ("RequestId", UInt64),
        ("UrlContext", UInt64),
        ("Version", win32more.Networking.HttpServer.HTTP_VERSION),
        ("Verb", win32more.Networking.HttpServer.HTTP_VERB),
        ("UnknownVerbLength", UInt16),
        ("RawUrlLength", UInt16),
        ("pUnknownVerb", win32more.Foundation.PSTR),
        ("pRawUrl", win32more.Foundation.PSTR),
        ("CookedUrl", win32more.Networking.HttpServer.HTTP_COOKED_URL),
        ("Address", win32more.Networking.HttpServer.HTTP_TRANSPORT_ADDRESS),
        ("Headers", win32more.Networking.HttpServer.HTTP_REQUEST_HEADERS),
        ("BytesReceived", UInt64),
        ("EntityChunkCount", UInt16),
        ("pEntityChunks", POINTER(win32more.Networking.HttpServer.HTTP_DATA_CHUNK_head)),
        ("RawConnectionId", UInt64),
        ("pSslInfo", POINTER(win32more.Networking.HttpServer.HTTP_SSL_INFO_head)),
    ]
    return HTTP_REQUEST_V1
def _define_HTTP_REQUEST_V2_head():
    class HTTP_REQUEST_V2(Structure):
        pass
    return HTTP_REQUEST_V2
def _define_HTTP_REQUEST_V2():
    HTTP_REQUEST_V2 = win32more.Networking.HttpServer.HTTP_REQUEST_V2_head
    HTTP_REQUEST_V2._fields_ = [
        ("__AnonymousBase_http_L1861_C35", win32more.Networking.HttpServer.HTTP_REQUEST_V1),
        ("RequestInfoCount", UInt16),
        ("pRequestInfo", POINTER(win32more.Networking.HttpServer.HTTP_REQUEST_INFO_head)),
    ]
    return HTTP_REQUEST_V2
def _define_HTTP_RESPONSE_V1_head():
    class HTTP_RESPONSE_V1(Structure):
        pass
    return HTTP_RESPONSE_V1
def _define_HTTP_RESPONSE_V1():
    HTTP_RESPONSE_V1 = win32more.Networking.HttpServer.HTTP_RESPONSE_V1_head
    HTTP_RESPONSE_V1._fields_ = [
        ("Flags", UInt32),
        ("Version", win32more.Networking.HttpServer.HTTP_VERSION),
        ("StatusCode", UInt16),
        ("ReasonLength", UInt16),
        ("pReason", win32more.Foundation.PSTR),
        ("Headers", win32more.Networking.HttpServer.HTTP_RESPONSE_HEADERS),
        ("EntityChunkCount", UInt16),
        ("pEntityChunks", POINTER(win32more.Networking.HttpServer.HTTP_DATA_CHUNK_head)),
    ]
    return HTTP_RESPONSE_V1
HTTP_RESPONSE_INFO_TYPE = Int32
HTTP_RESPONSE_INFO_TYPE_HttpResponseInfoTypeMultipleKnownHeaders = 0
HTTP_RESPONSE_INFO_TYPE_HttpResponseInfoTypeAuthenticationProperty = 1
HTTP_RESPONSE_INFO_TYPE_HttpResponseInfoTypeQoSProperty = 2
HTTP_RESPONSE_INFO_TYPE_HttpResponseInfoTypeChannelBind = 3
def _define_HTTP_RESPONSE_INFO_head():
    class HTTP_RESPONSE_INFO(Structure):
        pass
    return HTTP_RESPONSE_INFO
def _define_HTTP_RESPONSE_INFO():
    HTTP_RESPONSE_INFO = win32more.Networking.HttpServer.HTTP_RESPONSE_INFO_head
    HTTP_RESPONSE_INFO._fields_ = [
        ("Type", win32more.Networking.HttpServer.HTTP_RESPONSE_INFO_TYPE),
        ("Length", UInt32),
        ("pInfo", c_void_p),
    ]
    return HTTP_RESPONSE_INFO
def _define_HTTP_MULTIPLE_KNOWN_HEADERS_head():
    class HTTP_MULTIPLE_KNOWN_HEADERS(Structure):
        pass
    return HTTP_MULTIPLE_KNOWN_HEADERS
def _define_HTTP_MULTIPLE_KNOWN_HEADERS():
    HTTP_MULTIPLE_KNOWN_HEADERS = win32more.Networking.HttpServer.HTTP_MULTIPLE_KNOWN_HEADERS_head
    HTTP_MULTIPLE_KNOWN_HEADERS._fields_ = [
        ("HeaderId", win32more.Networking.HttpServer.HTTP_HEADER_ID),
        ("Flags", UInt32),
        ("KnownHeaderCount", UInt16),
        ("KnownHeaders", POINTER(win32more.Networking.HttpServer.HTTP_KNOWN_HEADER_head)),
    ]
    return HTTP_MULTIPLE_KNOWN_HEADERS
def _define_HTTP_RESPONSE_V2_head():
    class HTTP_RESPONSE_V2(Structure):
        pass
    return HTTP_RESPONSE_V2
def _define_HTTP_RESPONSE_V2():
    HTTP_RESPONSE_V2 = win32more.Networking.HttpServer.HTTP_RESPONSE_V2_head
    HTTP_RESPONSE_V2._fields_ = [
        ("__AnonymousBase_http_L2050_C36", win32more.Networking.HttpServer.HTTP_RESPONSE_V1),
        ("ResponseInfoCount", UInt16),
        ("pResponseInfo", POINTER(win32more.Networking.HttpServer.HTTP_RESPONSE_INFO_head)),
    ]
    return HTTP_RESPONSE_V2
def _define_HTTPAPI_VERSION_head():
    class HTTPAPI_VERSION(Structure):
        pass
    return HTTPAPI_VERSION
def _define_HTTPAPI_VERSION():
    HTTPAPI_VERSION = win32more.Networking.HttpServer.HTTPAPI_VERSION_head
    HTTPAPI_VERSION._fields_ = [
        ("HttpApiMajorVersion", UInt16),
        ("HttpApiMinorVersion", UInt16),
    ]
    return HTTPAPI_VERSION
HTTP_CACHE_POLICY_TYPE = Int32
HTTP_CACHE_POLICY_TYPE_HttpCachePolicyNocache = 0
HTTP_CACHE_POLICY_TYPE_HttpCachePolicyUserInvalidates = 1
HTTP_CACHE_POLICY_TYPE_HttpCachePolicyTimeToLive = 2
HTTP_CACHE_POLICY_TYPE_HttpCachePolicyMaximum = 3
def _define_HTTP_CACHE_POLICY_head():
    class HTTP_CACHE_POLICY(Structure):
        pass
    return HTTP_CACHE_POLICY
def _define_HTTP_CACHE_POLICY():
    HTTP_CACHE_POLICY = win32more.Networking.HttpServer.HTTP_CACHE_POLICY_head
    HTTP_CACHE_POLICY._fields_ = [
        ("Policy", win32more.Networking.HttpServer.HTTP_CACHE_POLICY_TYPE),
        ("SecondsToLive", UInt32),
    ]
    return HTTP_CACHE_POLICY
HTTP_SERVICE_CONFIG_ID = Int32
HTTP_SERVICE_CONFIG_ID_HttpServiceConfigIPListenList = 0
HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSSLCertInfo = 1
HTTP_SERVICE_CONFIG_ID_HttpServiceConfigUrlAclInfo = 2
HTTP_SERVICE_CONFIG_ID_HttpServiceConfigTimeout = 3
HTTP_SERVICE_CONFIG_ID_HttpServiceConfigCache = 4
HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSslSniCertInfo = 5
HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSslCcsCertInfo = 6
HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSetting = 7
HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSslCertInfoEx = 8
HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSslSniCertInfoEx = 9
HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSslCcsCertInfoEx = 10
HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSslScopedCcsCertInfo = 11
HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSslScopedCcsCertInfoEx = 12
HTTP_SERVICE_CONFIG_ID_HttpServiceConfigMax = 13
HTTP_SERVICE_CONFIG_QUERY_TYPE = Int32
HTTP_SERVICE_CONFIG_QUERY_TYPE_HttpServiceConfigQueryExact = 0
HTTP_SERVICE_CONFIG_QUERY_TYPE_HttpServiceConfigQueryNext = 1
HTTP_SERVICE_CONFIG_QUERY_TYPE_HttpServiceConfigQueryMax = 2
def _define_HTTP_SERVICE_CONFIG_SSL_KEY_head():
    class HTTP_SERVICE_CONFIG_SSL_KEY(Structure):
        pass
    return HTTP_SERVICE_CONFIG_SSL_KEY
def _define_HTTP_SERVICE_CONFIG_SSL_KEY():
    HTTP_SERVICE_CONFIG_SSL_KEY = win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_KEY_head
    HTTP_SERVICE_CONFIG_SSL_KEY._fields_ = [
        ("pIpPort", POINTER(win32more.Networking.WinSock.SOCKADDR_head)),
    ]
    return HTTP_SERVICE_CONFIG_SSL_KEY
def _define_HTTP_SERVICE_CONFIG_SSL_KEY_EX_head():
    class HTTP_SERVICE_CONFIG_SSL_KEY_EX(Structure):
        pass
    return HTTP_SERVICE_CONFIG_SSL_KEY_EX
def _define_HTTP_SERVICE_CONFIG_SSL_KEY_EX():
    HTTP_SERVICE_CONFIG_SSL_KEY_EX = win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_KEY_EX_head
    HTTP_SERVICE_CONFIG_SSL_KEY_EX._fields_ = [
        ("IpPort", win32more.Networking.WinSock.SOCKADDR_STORAGE),
    ]
    return HTTP_SERVICE_CONFIG_SSL_KEY_EX
def _define_HTTP_SERVICE_CONFIG_SSL_SNI_KEY_head():
    class HTTP_SERVICE_CONFIG_SSL_SNI_KEY(Structure):
        pass
    return HTTP_SERVICE_CONFIG_SSL_SNI_KEY
def _define_HTTP_SERVICE_CONFIG_SSL_SNI_KEY():
    HTTP_SERVICE_CONFIG_SSL_SNI_KEY = win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_SNI_KEY_head
    HTTP_SERVICE_CONFIG_SSL_SNI_KEY._fields_ = [
        ("IpPort", win32more.Networking.WinSock.SOCKADDR_STORAGE),
        ("Host", win32more.Foundation.PWSTR),
    ]
    return HTTP_SERVICE_CONFIG_SSL_SNI_KEY
def _define_HTTP_SERVICE_CONFIG_SSL_CCS_KEY_head():
    class HTTP_SERVICE_CONFIG_SSL_CCS_KEY(Structure):
        pass
    return HTTP_SERVICE_CONFIG_SSL_CCS_KEY
def _define_HTTP_SERVICE_CONFIG_SSL_CCS_KEY():
    HTTP_SERVICE_CONFIG_SSL_CCS_KEY = win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_CCS_KEY_head
    HTTP_SERVICE_CONFIG_SSL_CCS_KEY._fields_ = [
        ("LocalAddress", win32more.Networking.WinSock.SOCKADDR_STORAGE),
    ]
    return HTTP_SERVICE_CONFIG_SSL_CCS_KEY
def _define_HTTP_SERVICE_CONFIG_SSL_PARAM_head():
    class HTTP_SERVICE_CONFIG_SSL_PARAM(Structure):
        pass
    return HTTP_SERVICE_CONFIG_SSL_PARAM
def _define_HTTP_SERVICE_CONFIG_SSL_PARAM():
    HTTP_SERVICE_CONFIG_SSL_PARAM = win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_PARAM_head
    HTTP_SERVICE_CONFIG_SSL_PARAM._fields_ = [
        ("SslHashLength", UInt32),
        ("pSslHash", c_void_p),
        ("AppId", Guid),
        ("pSslCertStoreName", win32more.Foundation.PWSTR),
        ("DefaultCertCheckMode", UInt32),
        ("DefaultRevocationFreshnessTime", UInt32),
        ("DefaultRevocationUrlRetrievalTimeout", UInt32),
        ("pDefaultSslCtlIdentifier", win32more.Foundation.PWSTR),
        ("pDefaultSslCtlStoreName", win32more.Foundation.PWSTR),
        ("DefaultFlags", UInt32),
    ]
    return HTTP_SERVICE_CONFIG_SSL_PARAM
HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE = Int32
HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE_ExParamTypeHttp2Window = 0
HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE_ExParamTypeHttp2SettingsLimits = 1
HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE_ExParamTypeHttpPerformance = 2
HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE_ExParamTypeTlsRestrictions = 3
HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE_ExParamTypeErrorHeaders = 4
HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE_ExParamTypeTlsSessionTicketKeys = 5
HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE_ExParamTypeMax = 6
def _define_HTTP2_WINDOW_SIZE_PARAM_head():
    class HTTP2_WINDOW_SIZE_PARAM(Structure):
        pass
    return HTTP2_WINDOW_SIZE_PARAM
def _define_HTTP2_WINDOW_SIZE_PARAM():
    HTTP2_WINDOW_SIZE_PARAM = win32more.Networking.HttpServer.HTTP2_WINDOW_SIZE_PARAM_head
    HTTP2_WINDOW_SIZE_PARAM._fields_ = [
        ("Http2ReceiveWindowSize", UInt32),
    ]
    return HTTP2_WINDOW_SIZE_PARAM
def _define_HTTP2_SETTINGS_LIMITS_PARAM_head():
    class HTTP2_SETTINGS_LIMITS_PARAM(Structure):
        pass
    return HTTP2_SETTINGS_LIMITS_PARAM
def _define_HTTP2_SETTINGS_LIMITS_PARAM():
    HTTP2_SETTINGS_LIMITS_PARAM = win32more.Networking.HttpServer.HTTP2_SETTINGS_LIMITS_PARAM_head
    HTTP2_SETTINGS_LIMITS_PARAM._fields_ = [
        ("Http2MaxSettingsPerFrame", UInt32),
        ("Http2MaxSettingsPerMinute", UInt32),
    ]
    return HTTP2_SETTINGS_LIMITS_PARAM
HTTP_PERFORMANCE_PARAM_TYPE = Int32
HTTP_PERFORMANCE_PARAM_TYPE_PerformanceParamSendBufferingFlags = 0
HTTP_PERFORMANCE_PARAM_TYPE_PerformanceParamAggressiveICW = 1
HTTP_PERFORMANCE_PARAM_TYPE_PerformanceParamMaxSendBufferSize = 2
HTTP_PERFORMANCE_PARAM_TYPE_PerformanceParamMaxConcurrentClientStreams = 3
HTTP_PERFORMANCE_PARAM_TYPE_PerformanceParamMaxReceiveBufferSize = 4
HTTP_PERFORMANCE_PARAM_TYPE_PerformanceParamDecryptOnSspiThread = 5
HTTP_PERFORMANCE_PARAM_TYPE_PerformanceParamMax = 6
def _define_HTTP_PERFORMANCE_PARAM_head():
    class HTTP_PERFORMANCE_PARAM(Structure):
        pass
    return HTTP_PERFORMANCE_PARAM
def _define_HTTP_PERFORMANCE_PARAM():
    HTTP_PERFORMANCE_PARAM = win32more.Networking.HttpServer.HTTP_PERFORMANCE_PARAM_head
    HTTP_PERFORMANCE_PARAM._fields_ = [
        ("Type", win32more.Networking.HttpServer.HTTP_PERFORMANCE_PARAM_TYPE),
        ("BufferSize", UInt32),
        ("Buffer", c_void_p),
    ]
    return HTTP_PERFORMANCE_PARAM
def _define_HTTP_TLS_RESTRICTIONS_PARAM_head():
    class HTTP_TLS_RESTRICTIONS_PARAM(Structure):
        pass
    return HTTP_TLS_RESTRICTIONS_PARAM
def _define_HTTP_TLS_RESTRICTIONS_PARAM():
    HTTP_TLS_RESTRICTIONS_PARAM = win32more.Networking.HttpServer.HTTP_TLS_RESTRICTIONS_PARAM_head
    HTTP_TLS_RESTRICTIONS_PARAM._fields_ = [
        ("RestrictionCount", UInt32),
        ("TlsRestrictions", c_void_p),
    ]
    return HTTP_TLS_RESTRICTIONS_PARAM
def _define_HTTP_ERROR_HEADERS_PARAM_head():
    class HTTP_ERROR_HEADERS_PARAM(Structure):
        pass
    return HTTP_ERROR_HEADERS_PARAM
def _define_HTTP_ERROR_HEADERS_PARAM():
    HTTP_ERROR_HEADERS_PARAM = win32more.Networking.HttpServer.HTTP_ERROR_HEADERS_PARAM_head
    HTTP_ERROR_HEADERS_PARAM._fields_ = [
        ("StatusCode", UInt16),
        ("HeaderCount", UInt16),
        ("Headers", POINTER(win32more.Networking.HttpServer.HTTP_UNKNOWN_HEADER_head)),
    ]
    return HTTP_ERROR_HEADERS_PARAM
def _define_HTTP_TLS_SESSION_TICKET_KEYS_PARAM_head():
    class HTTP_TLS_SESSION_TICKET_KEYS_PARAM(Structure):
        pass
    return HTTP_TLS_SESSION_TICKET_KEYS_PARAM
def _define_HTTP_TLS_SESSION_TICKET_KEYS_PARAM():
    HTTP_TLS_SESSION_TICKET_KEYS_PARAM = win32more.Networking.HttpServer.HTTP_TLS_SESSION_TICKET_KEYS_PARAM_head
    HTTP_TLS_SESSION_TICKET_KEYS_PARAM._fields_ = [
        ("SessionTicketKeyCount", UInt32),
        ("SessionTicketKeys", c_void_p),
    ]
    return HTTP_TLS_SESSION_TICKET_KEYS_PARAM
def _define_HTTP_SERVICE_CONFIG_SSL_PARAM_EX_head():
    class HTTP_SERVICE_CONFIG_SSL_PARAM_EX(Structure):
        pass
    return HTTP_SERVICE_CONFIG_SSL_PARAM_EX
def _define_HTTP_SERVICE_CONFIG_SSL_PARAM_EX():
    HTTP_SERVICE_CONFIG_SSL_PARAM_EX = win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_PARAM_EX_head
    class HTTP_SERVICE_CONFIG_SSL_PARAM_EX__Anonymous_e__Union(Union):
        pass
    HTTP_SERVICE_CONFIG_SSL_PARAM_EX__Anonymous_e__Union._fields_ = [
        ("Http2WindowSizeParam", win32more.Networking.HttpServer.HTTP2_WINDOW_SIZE_PARAM),
        ("Http2SettingsLimitsParam", win32more.Networking.HttpServer.HTTP2_SETTINGS_LIMITS_PARAM),
        ("HttpPerformanceParam", win32more.Networking.HttpServer.HTTP_PERFORMANCE_PARAM),
        ("HttpTlsRestrictionsParam", win32more.Networking.HttpServer.HTTP_TLS_RESTRICTIONS_PARAM),
        ("HttpErrorHeadersParam", win32more.Networking.HttpServer.HTTP_ERROR_HEADERS_PARAM),
        ("HttpTlsSessionTicketKeysParam", win32more.Networking.HttpServer.HTTP_TLS_SESSION_TICKET_KEYS_PARAM),
    ]
    HTTP_SERVICE_CONFIG_SSL_PARAM_EX._anonymous_ = [
        'Anonymous',
    ]
    HTTP_SERVICE_CONFIG_SSL_PARAM_EX._fields_ = [
        ("ParamType", win32more.Networking.HttpServer.HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE),
        ("Flags", UInt64),
        ("Anonymous", HTTP_SERVICE_CONFIG_SSL_PARAM_EX__Anonymous_e__Union),
    ]
    return HTTP_SERVICE_CONFIG_SSL_PARAM_EX
def _define_HTTP_SERVICE_CONFIG_SSL_SET_head():
    class HTTP_SERVICE_CONFIG_SSL_SET(Structure):
        pass
    return HTTP_SERVICE_CONFIG_SSL_SET
def _define_HTTP_SERVICE_CONFIG_SSL_SET():
    HTTP_SERVICE_CONFIG_SSL_SET = win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_SET_head
    HTTP_SERVICE_CONFIG_SSL_SET._fields_ = [
        ("KeyDesc", win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_KEY),
        ("ParamDesc", win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_PARAM),
    ]
    return HTTP_SERVICE_CONFIG_SSL_SET
def _define_HTTP_SERVICE_CONFIG_SSL_SNI_SET_head():
    class HTTP_SERVICE_CONFIG_SSL_SNI_SET(Structure):
        pass
    return HTTP_SERVICE_CONFIG_SSL_SNI_SET
def _define_HTTP_SERVICE_CONFIG_SSL_SNI_SET():
    HTTP_SERVICE_CONFIG_SSL_SNI_SET = win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_SNI_SET_head
    HTTP_SERVICE_CONFIG_SSL_SNI_SET._fields_ = [
        ("KeyDesc", win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_SNI_KEY),
        ("ParamDesc", win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_PARAM),
    ]
    return HTTP_SERVICE_CONFIG_SSL_SNI_SET
def _define_HTTP_SERVICE_CONFIG_SSL_CCS_SET_head():
    class HTTP_SERVICE_CONFIG_SSL_CCS_SET(Structure):
        pass
    return HTTP_SERVICE_CONFIG_SSL_CCS_SET
def _define_HTTP_SERVICE_CONFIG_SSL_CCS_SET():
    HTTP_SERVICE_CONFIG_SSL_CCS_SET = win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_CCS_SET_head
    HTTP_SERVICE_CONFIG_SSL_CCS_SET._fields_ = [
        ("KeyDesc", win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_CCS_KEY),
        ("ParamDesc", win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_PARAM),
    ]
    return HTTP_SERVICE_CONFIG_SSL_CCS_SET
def _define_HTTP_SERVICE_CONFIG_SSL_SET_EX_head():
    class HTTP_SERVICE_CONFIG_SSL_SET_EX(Structure):
        pass
    return HTTP_SERVICE_CONFIG_SSL_SET_EX
def _define_HTTP_SERVICE_CONFIG_SSL_SET_EX():
    HTTP_SERVICE_CONFIG_SSL_SET_EX = win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_SET_EX_head
    HTTP_SERVICE_CONFIG_SSL_SET_EX._fields_ = [
        ("KeyDesc", win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_KEY_EX),
        ("ParamDesc", win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_PARAM_EX),
    ]
    return HTTP_SERVICE_CONFIG_SSL_SET_EX
def _define_HTTP_SERVICE_CONFIG_SSL_SNI_SET_EX_head():
    class HTTP_SERVICE_CONFIG_SSL_SNI_SET_EX(Structure):
        pass
    return HTTP_SERVICE_CONFIG_SSL_SNI_SET_EX
def _define_HTTP_SERVICE_CONFIG_SSL_SNI_SET_EX():
    HTTP_SERVICE_CONFIG_SSL_SNI_SET_EX = win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_SNI_SET_EX_head
    HTTP_SERVICE_CONFIG_SSL_SNI_SET_EX._fields_ = [
        ("KeyDesc", win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_SNI_KEY),
        ("ParamDesc", win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_PARAM_EX),
    ]
    return HTTP_SERVICE_CONFIG_SSL_SNI_SET_EX
def _define_HTTP_SERVICE_CONFIG_SSL_CCS_SET_EX_head():
    class HTTP_SERVICE_CONFIG_SSL_CCS_SET_EX(Structure):
        pass
    return HTTP_SERVICE_CONFIG_SSL_CCS_SET_EX
def _define_HTTP_SERVICE_CONFIG_SSL_CCS_SET_EX():
    HTTP_SERVICE_CONFIG_SSL_CCS_SET_EX = win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_CCS_SET_EX_head
    HTTP_SERVICE_CONFIG_SSL_CCS_SET_EX._fields_ = [
        ("KeyDesc", win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_CCS_KEY),
        ("ParamDesc", win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_PARAM_EX),
    ]
    return HTTP_SERVICE_CONFIG_SSL_CCS_SET_EX
def _define_HTTP_SERVICE_CONFIG_SSL_QUERY_head():
    class HTTP_SERVICE_CONFIG_SSL_QUERY(Structure):
        pass
    return HTTP_SERVICE_CONFIG_SSL_QUERY
def _define_HTTP_SERVICE_CONFIG_SSL_QUERY():
    HTTP_SERVICE_CONFIG_SSL_QUERY = win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_QUERY_head
    HTTP_SERVICE_CONFIG_SSL_QUERY._fields_ = [
        ("QueryDesc", win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_QUERY_TYPE),
        ("KeyDesc", win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_KEY),
        ("dwToken", UInt32),
    ]
    return HTTP_SERVICE_CONFIG_SSL_QUERY
def _define_HTTP_SERVICE_CONFIG_SSL_SNI_QUERY_head():
    class HTTP_SERVICE_CONFIG_SSL_SNI_QUERY(Structure):
        pass
    return HTTP_SERVICE_CONFIG_SSL_SNI_QUERY
def _define_HTTP_SERVICE_CONFIG_SSL_SNI_QUERY():
    HTTP_SERVICE_CONFIG_SSL_SNI_QUERY = win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_SNI_QUERY_head
    HTTP_SERVICE_CONFIG_SSL_SNI_QUERY._fields_ = [
        ("QueryDesc", win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_QUERY_TYPE),
        ("KeyDesc", win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_SNI_KEY),
        ("dwToken", UInt32),
    ]
    return HTTP_SERVICE_CONFIG_SSL_SNI_QUERY
def _define_HTTP_SERVICE_CONFIG_SSL_CCS_QUERY_head():
    class HTTP_SERVICE_CONFIG_SSL_CCS_QUERY(Structure):
        pass
    return HTTP_SERVICE_CONFIG_SSL_CCS_QUERY
def _define_HTTP_SERVICE_CONFIG_SSL_CCS_QUERY():
    HTTP_SERVICE_CONFIG_SSL_CCS_QUERY = win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_CCS_QUERY_head
    HTTP_SERVICE_CONFIG_SSL_CCS_QUERY._fields_ = [
        ("QueryDesc", win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_QUERY_TYPE),
        ("KeyDesc", win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_CCS_KEY),
        ("dwToken", UInt32),
    ]
    return HTTP_SERVICE_CONFIG_SSL_CCS_QUERY
def _define_HTTP_SERVICE_CONFIG_SSL_QUERY_EX_head():
    class HTTP_SERVICE_CONFIG_SSL_QUERY_EX(Structure):
        pass
    return HTTP_SERVICE_CONFIG_SSL_QUERY_EX
def _define_HTTP_SERVICE_CONFIG_SSL_QUERY_EX():
    HTTP_SERVICE_CONFIG_SSL_QUERY_EX = win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_QUERY_EX_head
    HTTP_SERVICE_CONFIG_SSL_QUERY_EX._fields_ = [
        ("QueryDesc", win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_QUERY_TYPE),
        ("KeyDesc", win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_KEY_EX),
        ("dwToken", UInt32),
        ("ParamType", win32more.Networking.HttpServer.HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE),
    ]
    return HTTP_SERVICE_CONFIG_SSL_QUERY_EX
def _define_HTTP_SERVICE_CONFIG_SSL_SNI_QUERY_EX_head():
    class HTTP_SERVICE_CONFIG_SSL_SNI_QUERY_EX(Structure):
        pass
    return HTTP_SERVICE_CONFIG_SSL_SNI_QUERY_EX
def _define_HTTP_SERVICE_CONFIG_SSL_SNI_QUERY_EX():
    HTTP_SERVICE_CONFIG_SSL_SNI_QUERY_EX = win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_SNI_QUERY_EX_head
    HTTP_SERVICE_CONFIG_SSL_SNI_QUERY_EX._fields_ = [
        ("QueryDesc", win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_QUERY_TYPE),
        ("KeyDesc", win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_SNI_KEY),
        ("dwToken", UInt32),
        ("ParamType", win32more.Networking.HttpServer.HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE),
    ]
    return HTTP_SERVICE_CONFIG_SSL_SNI_QUERY_EX
def _define_HTTP_SERVICE_CONFIG_SSL_CCS_QUERY_EX_head():
    class HTTP_SERVICE_CONFIG_SSL_CCS_QUERY_EX(Structure):
        pass
    return HTTP_SERVICE_CONFIG_SSL_CCS_QUERY_EX
def _define_HTTP_SERVICE_CONFIG_SSL_CCS_QUERY_EX():
    HTTP_SERVICE_CONFIG_SSL_CCS_QUERY_EX = win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_CCS_QUERY_EX_head
    HTTP_SERVICE_CONFIG_SSL_CCS_QUERY_EX._fields_ = [
        ("QueryDesc", win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_QUERY_TYPE),
        ("KeyDesc", win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_CCS_KEY),
        ("dwToken", UInt32),
        ("ParamType", win32more.Networking.HttpServer.HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE),
    ]
    return HTTP_SERVICE_CONFIG_SSL_CCS_QUERY_EX
def _define_HTTP_SERVICE_CONFIG_IP_LISTEN_PARAM_head():
    class HTTP_SERVICE_CONFIG_IP_LISTEN_PARAM(Structure):
        pass
    return HTTP_SERVICE_CONFIG_IP_LISTEN_PARAM
def _define_HTTP_SERVICE_CONFIG_IP_LISTEN_PARAM():
    HTTP_SERVICE_CONFIG_IP_LISTEN_PARAM = win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_IP_LISTEN_PARAM_head
    HTTP_SERVICE_CONFIG_IP_LISTEN_PARAM._fields_ = [
        ("AddrLength", UInt16),
        ("pAddress", POINTER(win32more.Networking.WinSock.SOCKADDR_head)),
    ]
    return HTTP_SERVICE_CONFIG_IP_LISTEN_PARAM
def _define_HTTP_SERVICE_CONFIG_IP_LISTEN_QUERY_head():
    class HTTP_SERVICE_CONFIG_IP_LISTEN_QUERY(Structure):
        pass
    return HTTP_SERVICE_CONFIG_IP_LISTEN_QUERY
def _define_HTTP_SERVICE_CONFIG_IP_LISTEN_QUERY():
    HTTP_SERVICE_CONFIG_IP_LISTEN_QUERY = win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_IP_LISTEN_QUERY_head
    HTTP_SERVICE_CONFIG_IP_LISTEN_QUERY._fields_ = [
        ("AddrCount", UInt32),
        ("AddrList", win32more.Networking.WinSock.SOCKADDR_STORAGE * 0),
    ]
    return HTTP_SERVICE_CONFIG_IP_LISTEN_QUERY
def _define_HTTP_SERVICE_CONFIG_URLACL_KEY_head():
    class HTTP_SERVICE_CONFIG_URLACL_KEY(Structure):
        pass
    return HTTP_SERVICE_CONFIG_URLACL_KEY
def _define_HTTP_SERVICE_CONFIG_URLACL_KEY():
    HTTP_SERVICE_CONFIG_URLACL_KEY = win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_URLACL_KEY_head
    HTTP_SERVICE_CONFIG_URLACL_KEY._fields_ = [
        ("pUrlPrefix", win32more.Foundation.PWSTR),
    ]
    return HTTP_SERVICE_CONFIG_URLACL_KEY
def _define_HTTP_SERVICE_CONFIG_URLACL_PARAM_head():
    class HTTP_SERVICE_CONFIG_URLACL_PARAM(Structure):
        pass
    return HTTP_SERVICE_CONFIG_URLACL_PARAM
def _define_HTTP_SERVICE_CONFIG_URLACL_PARAM():
    HTTP_SERVICE_CONFIG_URLACL_PARAM = win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_URLACL_PARAM_head
    HTTP_SERVICE_CONFIG_URLACL_PARAM._fields_ = [
        ("pStringSecurityDescriptor", win32more.Foundation.PWSTR),
    ]
    return HTTP_SERVICE_CONFIG_URLACL_PARAM
def _define_HTTP_SERVICE_CONFIG_URLACL_SET_head():
    class HTTP_SERVICE_CONFIG_URLACL_SET(Structure):
        pass
    return HTTP_SERVICE_CONFIG_URLACL_SET
def _define_HTTP_SERVICE_CONFIG_URLACL_SET():
    HTTP_SERVICE_CONFIG_URLACL_SET = win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_URLACL_SET_head
    HTTP_SERVICE_CONFIG_URLACL_SET._fields_ = [
        ("KeyDesc", win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_URLACL_KEY),
        ("ParamDesc", win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_URLACL_PARAM),
    ]
    return HTTP_SERVICE_CONFIG_URLACL_SET
def _define_HTTP_SERVICE_CONFIG_URLACL_QUERY_head():
    class HTTP_SERVICE_CONFIG_URLACL_QUERY(Structure):
        pass
    return HTTP_SERVICE_CONFIG_URLACL_QUERY
def _define_HTTP_SERVICE_CONFIG_URLACL_QUERY():
    HTTP_SERVICE_CONFIG_URLACL_QUERY = win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_URLACL_QUERY_head
    HTTP_SERVICE_CONFIG_URLACL_QUERY._fields_ = [
        ("QueryDesc", win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_QUERY_TYPE),
        ("KeyDesc", win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_URLACL_KEY),
        ("dwToken", UInt32),
    ]
    return HTTP_SERVICE_CONFIG_URLACL_QUERY
HTTP_SERVICE_CONFIG_CACHE_KEY = Int32
HTTP_SERVICE_CONFIG_CACHE_KEY_MaxCacheResponseSize = 0
HTTP_SERVICE_CONFIG_CACHE_KEY_CacheRangeChunkSize = 1
def _define_HTTP_SERVICE_CONFIG_CACHE_SET_head():
    class HTTP_SERVICE_CONFIG_CACHE_SET(Structure):
        pass
    return HTTP_SERVICE_CONFIG_CACHE_SET
def _define_HTTP_SERVICE_CONFIG_CACHE_SET():
    HTTP_SERVICE_CONFIG_CACHE_SET = win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_CACHE_SET_head
    HTTP_SERVICE_CONFIG_CACHE_SET._fields_ = [
        ("KeyDesc", win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_CACHE_KEY),
        ("ParamDesc", UInt32),
    ]
    return HTTP_SERVICE_CONFIG_CACHE_SET
HTTP_REQUEST_PROPERTY = Int32
HTTP_REQUEST_PROPERTY_HttpRequestPropertyIsb = 0
HTTP_REQUEST_PROPERTY_HttpRequestPropertyTcpInfoV0 = 1
HTTP_REQUEST_PROPERTY_HttpRequestPropertyQuicStats = 2
HTTP_REQUEST_PROPERTY_HttpRequestPropertyTcpInfoV1 = 3
HTTP_REQUEST_PROPERTY_HttpRequestPropertySni = 4
HTTP_REQUEST_PROPERTY_HttpRequestPropertyStreamError = 5
HTTP_REQUEST_PROPERTY_HttpRequestPropertyWskApiTimings = 6
HTTP_REQUEST_PROPERTY_HttpRequestPropertyQuicApiTimings = 7
def _define_HTTP_QUERY_REQUEST_QUALIFIER_TCP_head():
    class HTTP_QUERY_REQUEST_QUALIFIER_TCP(Structure):
        pass
    return HTTP_QUERY_REQUEST_QUALIFIER_TCP
def _define_HTTP_QUERY_REQUEST_QUALIFIER_TCP():
    HTTP_QUERY_REQUEST_QUALIFIER_TCP = win32more.Networking.HttpServer.HTTP_QUERY_REQUEST_QUALIFIER_TCP_head
    HTTP_QUERY_REQUEST_QUALIFIER_TCP._fields_ = [
        ("Freshness", UInt64),
    ]
    return HTTP_QUERY_REQUEST_QUALIFIER_TCP
def _define_HTTP_QUERY_REQUEST_QUALIFIER_QUIC_head():
    class HTTP_QUERY_REQUEST_QUALIFIER_QUIC(Structure):
        pass
    return HTTP_QUERY_REQUEST_QUALIFIER_QUIC
def _define_HTTP_QUERY_REQUEST_QUALIFIER_QUIC():
    HTTP_QUERY_REQUEST_QUALIFIER_QUIC = win32more.Networking.HttpServer.HTTP_QUERY_REQUEST_QUALIFIER_QUIC_head
    HTTP_QUERY_REQUEST_QUALIFIER_QUIC._fields_ = [
        ("Freshness", UInt64),
    ]
    return HTTP_QUERY_REQUEST_QUALIFIER_QUIC
def _define_HTTP_REQUEST_PROPERTY_SNI_head():
    class HTTP_REQUEST_PROPERTY_SNI(Structure):
        pass
    return HTTP_REQUEST_PROPERTY_SNI
def _define_HTTP_REQUEST_PROPERTY_SNI():
    HTTP_REQUEST_PROPERTY_SNI = win32more.Networking.HttpServer.HTTP_REQUEST_PROPERTY_SNI_head
    HTTP_REQUEST_PROPERTY_SNI._fields_ = [
        ("Hostname", Char * 256),
        ("Flags", UInt32),
    ]
    return HTTP_REQUEST_PROPERTY_SNI
def _define_HTTP_REQUEST_PROPERTY_STREAM_ERROR_head():
    class HTTP_REQUEST_PROPERTY_STREAM_ERROR(Structure):
        pass
    return HTTP_REQUEST_PROPERTY_STREAM_ERROR
def _define_HTTP_REQUEST_PROPERTY_STREAM_ERROR():
    HTTP_REQUEST_PROPERTY_STREAM_ERROR = win32more.Networking.HttpServer.HTTP_REQUEST_PROPERTY_STREAM_ERROR_head
    HTTP_REQUEST_PROPERTY_STREAM_ERROR._fields_ = [
        ("ErrorCode", UInt32),
    ]
    return HTTP_REQUEST_PROPERTY_STREAM_ERROR
def _define_HTTP_WSK_API_TIMINGS_head():
    class HTTP_WSK_API_TIMINGS(Structure):
        pass
    return HTTP_WSK_API_TIMINGS
def _define_HTTP_WSK_API_TIMINGS():
    HTTP_WSK_API_TIMINGS = win32more.Networking.HttpServer.HTTP_WSK_API_TIMINGS_head
    HTTP_WSK_API_TIMINGS._fields_ = [
        ("ConnectCount", UInt64),
        ("ConnectSum", UInt64),
        ("DisconnectCount", UInt64),
        ("DisconnectSum", UInt64),
        ("SendCount", UInt64),
        ("SendSum", UInt64),
        ("ReceiveCount", UInt64),
        ("ReceiveSum", UInt64),
        ("ReleaseCount", UInt64),
        ("ReleaseSum", UInt64),
        ("ControlSocketCount", UInt64),
        ("ControlSocketSum", UInt64),
    ]
    return HTTP_WSK_API_TIMINGS
def _define_HTTP_QUIC_STREAM_API_TIMINGS_head():
    class HTTP_QUIC_STREAM_API_TIMINGS(Structure):
        pass
    return HTTP_QUIC_STREAM_API_TIMINGS
def _define_HTTP_QUIC_STREAM_API_TIMINGS():
    HTTP_QUIC_STREAM_API_TIMINGS = win32more.Networking.HttpServer.HTTP_QUIC_STREAM_API_TIMINGS_head
    HTTP_QUIC_STREAM_API_TIMINGS._fields_ = [
        ("OpenCount", UInt64),
        ("OpenSum", UInt64),
        ("CloseCount", UInt64),
        ("CloseSum", UInt64),
        ("StartCount", UInt64),
        ("StartSum", UInt64),
        ("ShutdownCount", UInt64),
        ("ShutdownSum", UInt64),
        ("SendCount", UInt64),
        ("SendSum", UInt64),
        ("ReceiveSetEnabledCount", UInt64),
        ("ReceiveSetEnabledSum", UInt64),
        ("GetParamCount", UInt64),
        ("GetParamSum", UInt64),
        ("SetParamCount", UInt64),
        ("SetParamSum", UInt64),
        ("SetCallbackHandlerCount", UInt64),
        ("SetCallbackHandlerSum", UInt64),
    ]
    return HTTP_QUIC_STREAM_API_TIMINGS
def _define_HTTP_QUIC_CONNECTION_API_TIMINGS_head():
    class HTTP_QUIC_CONNECTION_API_TIMINGS(Structure):
        pass
    return HTTP_QUIC_CONNECTION_API_TIMINGS
def _define_HTTP_QUIC_CONNECTION_API_TIMINGS():
    HTTP_QUIC_CONNECTION_API_TIMINGS = win32more.Networking.HttpServer.HTTP_QUIC_CONNECTION_API_TIMINGS_head
    HTTP_QUIC_CONNECTION_API_TIMINGS._fields_ = [
        ("OpenTime", UInt64),
        ("CloseTime", UInt64),
        ("StartTime", UInt64),
        ("ShutdownTime", UInt64),
        ("SecConfigCreateTime", UInt64),
        ("SecConfigDeleteTime", UInt64),
        ("GetParamCount", UInt64),
        ("GetParamSum", UInt64),
        ("SetParamCount", UInt64),
        ("SetParamSum", UInt64),
        ("SetCallbackHandlerCount", UInt64),
        ("SetCallbackHandlerSum", UInt64),
        ("ControlStreamTimings", win32more.Networking.HttpServer.HTTP_QUIC_STREAM_API_TIMINGS),
    ]
    return HTTP_QUIC_CONNECTION_API_TIMINGS
def _define_HTTP_QUIC_API_TIMINGS_head():
    class HTTP_QUIC_API_TIMINGS(Structure):
        pass
    return HTTP_QUIC_API_TIMINGS
def _define_HTTP_QUIC_API_TIMINGS():
    HTTP_QUIC_API_TIMINGS = win32more.Networking.HttpServer.HTTP_QUIC_API_TIMINGS_head
    HTTP_QUIC_API_TIMINGS._fields_ = [
        ("ConnectionTimings", win32more.Networking.HttpServer.HTTP_QUIC_CONNECTION_API_TIMINGS),
        ("StreamTimings", win32more.Networking.HttpServer.HTTP_QUIC_STREAM_API_TIMINGS),
    ]
    return HTTP_QUIC_API_TIMINGS
HTTP_FEATURE_ID = Int32
HTTP_FEATURE_ID_HttpFeatureUnknown = 0
HTTP_FEATURE_ID_HttpFeatureResponseTrailers = 1
HTTP_FEATURE_ID_HttpFeatureApiTimings = 2
HTTP_FEATURE_ID_HttpFeatureDelegateEx = 3
HTTP_FEATURE_ID_HttpFeatureHttp3 = 4
HTTP_FEATURE_ID_HttpFeaturemax = -1
def _define_HttpInitialize():
    try:
        return WINFUNCTYPE(UInt32,win32more.Networking.HttpServer.HTTPAPI_VERSION,win32more.Networking.HttpServer.HTTP_INITIALIZE,c_void_p, use_last_error=False)(("HttpInitialize", windll["HTTPAPI"]), ((1, 'Version'),(1, 'Flags'),(1, 'pReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpTerminate():
    try:
        return WINFUNCTYPE(UInt32,win32more.Networking.HttpServer.HTTP_INITIALIZE,c_void_p, use_last_error=False)(("HttpTerminate", windll["HTTPAPI"]), ((1, 'Flags'),(1, 'pReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpCreateHttpHandle():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Foundation.HANDLE),UInt32, use_last_error=False)(("HttpCreateHttpHandle", windll["HTTPAPI"]), ((1, 'RequestQueueHandle'),(1, 'Reserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpCreateRequestQueue():
    try:
        return WINFUNCTYPE(UInt32,win32more.Networking.HttpServer.HTTPAPI_VERSION,win32more.Foundation.PWSTR,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),UInt32,POINTER(win32more.Foundation.HANDLE), use_last_error=False)(("HttpCreateRequestQueue", windll["HTTPAPI"]), ((1, 'Version'),(1, 'Name'),(1, 'SecurityAttributes'),(1, 'Flags'),(1, 'RequestQueueHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpCloseRequestQueue():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE, use_last_error=False)(("HttpCloseRequestQueue", windll["HTTPAPI"]), ((1, 'RequestQueueHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpSetRequestQueueProperty():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Networking.HttpServer.HTTP_SERVER_PROPERTY,c_void_p,UInt32,UInt32,c_void_p, use_last_error=False)(("HttpSetRequestQueueProperty", windll["HTTPAPI"]), ((1, 'RequestQueueHandle'),(1, 'Property'),(1, 'PropertyInformation'),(1, 'PropertyInformationLength'),(1, 'Reserved1'),(1, 'Reserved2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpQueryRequestQueueProperty():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Networking.HttpServer.HTTP_SERVER_PROPERTY,c_void_p,UInt32,UInt32,POINTER(UInt32),c_void_p, use_last_error=False)(("HttpQueryRequestQueueProperty", windll["HTTPAPI"]), ((1, 'RequestQueueHandle'),(1, 'Property'),(1, 'PropertyInformation'),(1, 'PropertyInformationLength'),(1, 'Reserved1'),(1, 'ReturnLength'),(1, 'Reserved2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpSetRequestProperty():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt64,win32more.Networking.HttpServer.HTTP_REQUEST_PROPERTY,c_void_p,UInt32,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("HttpSetRequestProperty", windll["HTTPAPI"]), ((1, 'RequestQueueHandle'),(1, 'Id'),(1, 'PropertyId'),(1, 'Input'),(1, 'InputPropertySize'),(1, 'Overlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpShutdownRequestQueue():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE, use_last_error=False)(("HttpShutdownRequestQueue", windll["HTTPAPI"]), ((1, 'RequestQueueHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpReceiveClientCertificate():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt64,UInt32,POINTER(win32more.Networking.HttpServer.HTTP_SSL_CLIENT_CERT_INFO_head),UInt32,POINTER(UInt32),POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("HttpReceiveClientCertificate", windll["HTTPAPI"]), ((1, 'RequestQueueHandle'),(1, 'ConnectionId'),(1, 'Flags'),(1, 'SslClientCertInfo'),(1, 'SslClientCertInfoSize'),(1, 'BytesReceived'),(1, 'Overlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpCreateServerSession():
    try:
        return WINFUNCTYPE(UInt32,win32more.Networking.HttpServer.HTTPAPI_VERSION,POINTER(UInt64),UInt32, use_last_error=False)(("HttpCreateServerSession", windll["HTTPAPI"]), ((1, 'Version'),(1, 'ServerSessionId'),(1, 'Reserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpCloseServerSession():
    try:
        return WINFUNCTYPE(UInt32,UInt64, use_last_error=False)(("HttpCloseServerSession", windll["HTTPAPI"]), ((1, 'ServerSessionId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpQueryServerSessionProperty():
    try:
        return WINFUNCTYPE(UInt32,UInt64,win32more.Networking.HttpServer.HTTP_SERVER_PROPERTY,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("HttpQueryServerSessionProperty", windll["HTTPAPI"]), ((1, 'ServerSessionId'),(1, 'Property'),(1, 'PropertyInformation'),(1, 'PropertyInformationLength'),(1, 'ReturnLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpSetServerSessionProperty():
    try:
        return WINFUNCTYPE(UInt32,UInt64,win32more.Networking.HttpServer.HTTP_SERVER_PROPERTY,c_void_p,UInt32, use_last_error=False)(("HttpSetServerSessionProperty", windll["HTTPAPI"]), ((1, 'ServerSessionId'),(1, 'Property'),(1, 'PropertyInformation'),(1, 'PropertyInformationLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpAddUrl():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,c_void_p, use_last_error=False)(("HttpAddUrl", windll["HTTPAPI"]), ((1, 'RequestQueueHandle'),(1, 'FullyQualifiedUrl'),(1, 'Reserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpRemoveUrl():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR, use_last_error=False)(("HttpRemoveUrl", windll["HTTPAPI"]), ((1, 'RequestQueueHandle'),(1, 'FullyQualifiedUrl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpCreateUrlGroup():
    try:
        return WINFUNCTYPE(UInt32,UInt64,POINTER(UInt64),UInt32, use_last_error=False)(("HttpCreateUrlGroup", windll["HTTPAPI"]), ((1, 'ServerSessionId'),(1, 'pUrlGroupId'),(1, 'Reserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpCloseUrlGroup():
    try:
        return WINFUNCTYPE(UInt32,UInt64, use_last_error=False)(("HttpCloseUrlGroup", windll["HTTPAPI"]), ((1, 'UrlGroupId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpAddUrlToUrlGroup():
    try:
        return WINFUNCTYPE(UInt32,UInt64,win32more.Foundation.PWSTR,UInt64,UInt32, use_last_error=False)(("HttpAddUrlToUrlGroup", windll["HTTPAPI"]), ((1, 'UrlGroupId'),(1, 'pFullyQualifiedUrl'),(1, 'UrlContext'),(1, 'Reserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpRemoveUrlFromUrlGroup():
    try:
        return WINFUNCTYPE(UInt32,UInt64,win32more.Foundation.PWSTR,UInt32, use_last_error=False)(("HttpRemoveUrlFromUrlGroup", windll["HTTPAPI"]), ((1, 'UrlGroupId'),(1, 'pFullyQualifiedUrl'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpSetUrlGroupProperty():
    try:
        return WINFUNCTYPE(UInt32,UInt64,win32more.Networking.HttpServer.HTTP_SERVER_PROPERTY,c_void_p,UInt32, use_last_error=False)(("HttpSetUrlGroupProperty", windll["HTTPAPI"]), ((1, 'UrlGroupId'),(1, 'Property'),(1, 'PropertyInformation'),(1, 'PropertyInformationLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpQueryUrlGroupProperty():
    try:
        return WINFUNCTYPE(UInt32,UInt64,win32more.Networking.HttpServer.HTTP_SERVER_PROPERTY,c_void_p,UInt32,POINTER(UInt32), use_last_error=False)(("HttpQueryUrlGroupProperty", windll["HTTPAPI"]), ((1, 'UrlGroupId'),(1, 'Property'),(1, 'PropertyInformation'),(1, 'PropertyInformationLength'),(1, 'ReturnLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpPrepareUrl():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR), use_last_error=False)(("HttpPrepareUrl", windll["HTTPAPI"]), ((1, 'Reserved'),(1, 'Flags'),(1, 'Url'),(1, 'PreparedUrl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpReceiveHttpRequest():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt64,win32more.Networking.HttpServer.HTTP_RECEIVE_HTTP_REQUEST_FLAGS,POINTER(win32more.Networking.HttpServer.HTTP_REQUEST_V2_head),UInt32,POINTER(UInt32),POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("HttpReceiveHttpRequest", windll["HTTPAPI"]), ((1, 'RequestQueueHandle'),(1, 'RequestId'),(1, 'Flags'),(1, 'RequestBuffer'),(1, 'RequestBufferLength'),(1, 'BytesReturned'),(1, 'Overlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpReceiveRequestEntityBody():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt64,UInt32,c_void_p,UInt32,POINTER(UInt32),POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("HttpReceiveRequestEntityBody", windll["HTTPAPI"]), ((1, 'RequestQueueHandle'),(1, 'RequestId'),(1, 'Flags'),(1, 'EntityBuffer'),(1, 'EntityBufferLength'),(1, 'BytesReturned'),(1, 'Overlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpSendHttpResponse():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt64,UInt32,POINTER(win32more.Networking.HttpServer.HTTP_RESPONSE_V2_head),POINTER(win32more.Networking.HttpServer.HTTP_CACHE_POLICY_head),POINTER(UInt32),c_void_p,UInt32,POINTER(win32more.System.IO.OVERLAPPED_head),POINTER(win32more.Networking.HttpServer.HTTP_LOG_DATA_head), use_last_error=False)(("HttpSendHttpResponse", windll["HTTPAPI"]), ((1, 'RequestQueueHandle'),(1, 'RequestId'),(1, 'Flags'),(1, 'HttpResponse'),(1, 'CachePolicy'),(1, 'BytesSent'),(1, 'Reserved1'),(1, 'Reserved2'),(1, 'Overlapped'),(1, 'LogData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpSendResponseEntityBody():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt64,UInt32,UInt16,POINTER(win32more.Networking.HttpServer.HTTP_DATA_CHUNK),POINTER(UInt32),c_void_p,UInt32,POINTER(win32more.System.IO.OVERLAPPED_head),POINTER(win32more.Networking.HttpServer.HTTP_LOG_DATA_head), use_last_error=False)(("HttpSendResponseEntityBody", windll["HTTPAPI"]), ((1, 'RequestQueueHandle'),(1, 'RequestId'),(1, 'Flags'),(1, 'EntityChunkCount'),(1, 'EntityChunks'),(1, 'BytesSent'),(1, 'Reserved1'),(1, 'Reserved2'),(1, 'Overlapped'),(1, 'LogData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpDeclarePush():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt64,win32more.Networking.HttpServer.HTTP_VERB,win32more.Foundation.PWSTR,win32more.Foundation.PSTR,POINTER(win32more.Networking.HttpServer.HTTP_REQUEST_HEADERS_head), use_last_error=False)(("HttpDeclarePush", windll["HTTPAPI"]), ((1, 'RequestQueueHandle'),(1, 'RequestId'),(1, 'Verb'),(1, 'Path'),(1, 'Query'),(1, 'Headers'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpWaitForDisconnect():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt64,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("HttpWaitForDisconnect", windll["HTTPAPI"]), ((1, 'RequestQueueHandle'),(1, 'ConnectionId'),(1, 'Overlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpWaitForDisconnectEx():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt64,UInt32,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("HttpWaitForDisconnectEx", windll["HTTPAPI"]), ((1, 'RequestQueueHandle'),(1, 'ConnectionId'),(1, 'Reserved'),(1, 'Overlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpCancelHttpRequest():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt64,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("HttpCancelHttpRequest", windll["HTTPAPI"]), ((1, 'RequestQueueHandle'),(1, 'RequestId'),(1, 'Overlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpWaitForDemandStart():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("HttpWaitForDemandStart", windll["HTTPAPI"]), ((1, 'RequestQueueHandle'),(1, 'Overlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpIsFeatureSupported():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Networking.HttpServer.HTTP_FEATURE_ID, use_last_error=False)(("HttpIsFeatureSupported", windll["HTTPAPI"]), ((1, 'FeatureId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpDelegateRequestEx():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,UInt64,UInt64,UInt32,POINTER(win32more.Networking.HttpServer.HTTP_DELEGATE_REQUEST_PROPERTY_INFO_head), use_last_error=False)(("HttpDelegateRequestEx", windll["HTTPAPI"]), ((1, 'RequestQueueHandle'),(1, 'DelegateQueueHandle'),(1, 'RequestId'),(1, 'DelegateUrlGroupId'),(1, 'PropertyInfoSetSize'),(1, 'PropertyInfoSet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpFindUrlGroupId():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.HANDLE,POINTER(UInt64), use_last_error=False)(("HttpFindUrlGroupId", windll["HTTPAPI"]), ((1, 'FullyQualifiedUrl'),(1, 'RequestQueueHandle'),(1, 'UrlGroupId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpFlushResponseCache():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("HttpFlushResponseCache", windll["HTTPAPI"]), ((1, 'RequestQueueHandle'),(1, 'UrlPrefix'),(1, 'Flags'),(1, 'Overlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpAddFragmentToCache():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,POINTER(win32more.Networking.HttpServer.HTTP_DATA_CHUNK_head),POINTER(win32more.Networking.HttpServer.HTTP_CACHE_POLICY_head),POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("HttpAddFragmentToCache", windll["HTTPAPI"]), ((1, 'RequestQueueHandle'),(1, 'UrlPrefix'),(1, 'DataChunk'),(1, 'CachePolicy'),(1, 'Overlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpReadFragmentFromCache():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,POINTER(win32more.Networking.HttpServer.HTTP_BYTE_RANGE_head),c_void_p,UInt32,POINTER(UInt32),POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("HttpReadFragmentFromCache", windll["HTTPAPI"]), ((1, 'RequestQueueHandle'),(1, 'UrlPrefix'),(1, 'ByteRange'),(1, 'Buffer'),(1, 'BufferLength'),(1, 'BytesRead'),(1, 'Overlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpSetServiceConfiguration():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_ID,c_void_p,UInt32,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("HttpSetServiceConfiguration", windll["HTTPAPI"]), ((1, 'ServiceHandle'),(1, 'ConfigId'),(1, 'pConfigInformation'),(1, 'ConfigInformationLength'),(1, 'pOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpUpdateServiceConfiguration():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_ID,c_void_p,UInt32,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("HttpUpdateServiceConfiguration", windll["HTTPAPI"]), ((1, 'Handle'),(1, 'ConfigId'),(1, 'ConfigInfo'),(1, 'ConfigInfoLength'),(1, 'Overlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpDeleteServiceConfiguration():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_ID,c_void_p,UInt32,POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("HttpDeleteServiceConfiguration", windll["HTTPAPI"]), ((1, 'ServiceHandle'),(1, 'ConfigId'),(1, 'pConfigInformation'),(1, 'ConfigInformationLength'),(1, 'pOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpQueryServiceConfiguration():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Networking.HttpServer.HTTP_SERVICE_CONFIG_ID,c_void_p,UInt32,c_void_p,UInt32,POINTER(UInt32),POINTER(win32more.System.IO.OVERLAPPED_head), use_last_error=False)(("HttpQueryServiceConfiguration", windll["HTTPAPI"]), ((1, 'ServiceHandle'),(1, 'ConfigId'),(1, 'pInput'),(1, 'InputLength'),(1, 'pOutput'),(1, 'OutputLength'),(1, 'pReturnLength'),(1, 'pOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HttpGetExtension():
    try:
        return WINFUNCTYPE(UInt32,win32more.Networking.HttpServer.HTTPAPI_VERSION,UInt32,c_void_p,UInt32, use_last_error=False)(("HttpGetExtension", windll["HTTPAPI"]), ((1, 'Version'),(1, 'Extension'),(1, 'Buffer'),(1, 'BufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "HTTP_DEMAND_CBT",
    "HTTP_MAX_SERVER_QUEUE_LENGTH",
    "HTTP_MIN_SERVER_QUEUE_LENGTH",
    "HTTP_AUTH_ENABLE_BASIC",
    "HTTP_AUTH_ENABLE_DIGEST",
    "HTTP_AUTH_ENABLE_NTLM",
    "HTTP_AUTH_ENABLE_NEGOTIATE",
    "HTTP_AUTH_ENABLE_KERBEROS",
    "HTTP_AUTH_EX_FLAG_ENABLE_KERBEROS_CREDENTIAL_CACHING",
    "HTTP_AUTH_EX_FLAG_CAPTURE_CREDENTIAL",
    "HTTP_CHANNEL_BIND_PROXY",
    "HTTP_CHANNEL_BIND_PROXY_COHOSTING",
    "HTTP_CHANNEL_BIND_NO_SERVICE_NAME_CHECK",
    "HTTP_CHANNEL_BIND_DOTLESS_SERVICE",
    "HTTP_CHANNEL_BIND_SECURE_CHANNEL_TOKEN",
    "HTTP_CHANNEL_BIND_CLIENT_SERVICE",
    "HTTP_LOG_FIELD_DATE",
    "HTTP_LOG_FIELD_TIME",
    "HTTP_LOG_FIELD_CLIENT_IP",
    "HTTP_LOG_FIELD_USER_NAME",
    "HTTP_LOG_FIELD_SITE_NAME",
    "HTTP_LOG_FIELD_COMPUTER_NAME",
    "HTTP_LOG_FIELD_SERVER_IP",
    "HTTP_LOG_FIELD_METHOD",
    "HTTP_LOG_FIELD_URI_STEM",
    "HTTP_LOG_FIELD_URI_QUERY",
    "HTTP_LOG_FIELD_STATUS",
    "HTTP_LOG_FIELD_WIN32_STATUS",
    "HTTP_LOG_FIELD_BYTES_SENT",
    "HTTP_LOG_FIELD_BYTES_RECV",
    "HTTP_LOG_FIELD_TIME_TAKEN",
    "HTTP_LOG_FIELD_SERVER_PORT",
    "HTTP_LOG_FIELD_USER_AGENT",
    "HTTP_LOG_FIELD_COOKIE",
    "HTTP_LOG_FIELD_REFERER",
    "HTTP_LOG_FIELD_VERSION",
    "HTTP_LOG_FIELD_HOST",
    "HTTP_LOG_FIELD_SUB_STATUS",
    "HTTP_LOG_FIELD_STREAM_ID",
    "HTTP_LOG_FIELD_STREAM_ID_EX",
    "HTTP_LOG_FIELD_TRANSPORT_TYPE",
    "HTTP_LOG_FIELD_CLIENT_PORT",
    "HTTP_LOG_FIELD_URI",
    "HTTP_LOG_FIELD_SITE_ID",
    "HTTP_LOG_FIELD_REASON",
    "HTTP_LOG_FIELD_QUEUE_NAME",
    "HTTP_LOG_FIELD_CORRELATION_ID",
    "HTTP_LOGGING_FLAG_LOCAL_TIME_ROLLOVER",
    "HTTP_LOGGING_FLAG_USE_UTF8_CONVERSION",
    "HTTP_LOGGING_FLAG_LOG_ERRORS_ONLY",
    "HTTP_LOGGING_FLAG_LOG_SUCCESS_ONLY",
    "HTTP_CREATE_REQUEST_QUEUE_FLAG_OPEN_EXISTING",
    "HTTP_CREATE_REQUEST_QUEUE_FLAG_CONTROLLER",
    "HTTP_CREATE_REQUEST_QUEUE_FLAG_DELEGATION",
    "HTTP_RECEIVE_REQUEST_ENTITY_BODY_FLAG_FILL_BUFFER",
    "HTTP_SEND_RESPONSE_FLAG_DISCONNECT",
    "HTTP_SEND_RESPONSE_FLAG_MORE_DATA",
    "HTTP_SEND_RESPONSE_FLAG_BUFFER_DATA",
    "HTTP_SEND_RESPONSE_FLAG_ENABLE_NAGLING",
    "HTTP_SEND_RESPONSE_FLAG_PROCESS_RANGES",
    "HTTP_SEND_RESPONSE_FLAG_OPAQUE",
    "HTTP_SEND_RESPONSE_FLAG_GOAWAY",
    "HTTP_FLUSH_RESPONSE_FLAG_RECURSIVE",
    "HTTP_URL_FLAG_REMOVE_ALL",
    "HTTP_RECEIVE_SECURE_CHANNEL_TOKEN",
    "HTTP_RECEIVE_FULL_CHAIN",
    "HTTP_REQUEST_SIZING_INFO_FLAG_TCP_FAST_OPEN",
    "HTTP_REQUEST_SIZING_INFO_FLAG_TLS_SESSION_RESUMPTION",
    "HTTP_REQUEST_SIZING_INFO_FLAG_TLS_FALSE_START",
    "HTTP_REQUEST_SIZING_INFO_FLAG_FIRST_REQUEST",
    "HTTP_REQUEST_AUTH_FLAG_TOKEN_FOR_CACHED_CRED",
    "HTTP_REQUEST_FLAG_MORE_ENTITY_BODY_EXISTS",
    "HTTP_REQUEST_FLAG_IP_ROUTED",
    "HTTP_REQUEST_FLAG_HTTP2",
    "HTTP_REQUEST_FLAG_HTTP3",
    "HTTP_RESPONSE_FLAG_MULTIPLE_ENCODINGS_AVAILABLE",
    "HTTP_RESPONSE_FLAG_MORE_ENTITY_BODY_EXISTS",
    "HTTP_RESPONSE_INFO_FLAGS_PRESERVE_ORDER",
    "HTTP_SERVICE_CONFIG_SSL_FLAG_USE_DS_MAPPER",
    "HTTP_SERVICE_CONFIG_SSL_FLAG_NEGOTIATE_CLIENT_CERT",
    "HTTP_SERVICE_CONFIG_SSL_FLAG_NO_RAW_FILTER",
    "HTTP_SERVICE_CONFIG_SSL_FLAG_REJECT",
    "HTTP_SERVICE_CONFIG_SSL_FLAG_DISABLE_HTTP2",
    "HTTP_SERVICE_CONFIG_SSL_FLAG_DISABLE_QUIC",
    "HTTP_SERVICE_CONFIG_SSL_FLAG_DISABLE_TLS13",
    "HTTP_SERVICE_CONFIG_SSL_FLAG_DISABLE_OCSP_STAPLING",
    "HTTP_SERVICE_CONFIG_SSL_FLAG_ENABLE_TOKEN_BINDING",
    "HTTP_SERVICE_CONFIG_SSL_FLAG_LOG_EXTENDED_EVENTS",
    "HTTP_SERVICE_CONFIG_SSL_FLAG_DISABLE_LEGACY_TLS",
    "HTTP_SERVICE_CONFIG_SSL_FLAG_ENABLE_SESSION_TICKET",
    "HTTP_SERVICE_CONFIG_SSL_FLAG_DISABLE_TLS12",
    "HTTP_SERVICE_CONFIG_SSL_FLAG_ENABLE_CLIENT_CORRELATION",
    "HTTP_REQUEST_PROPERTY_SNI_HOST_MAX_LENGTH",
    "HTTP_REQUEST_PROPERTY_SNI_FLAG_SNI_USED",
    "HTTP_REQUEST_PROPERTY_SNI_FLAG_NO_SNI",
    "HTTP_RECEIVE_HTTP_REQUEST_FLAGS",
    "HTTP_RECEIVE_REQUEST_FLAG_COPY_BODY",
    "HTTP_RECEIVE_REQUEST_FLAG_FLUSH_BODY",
    "HTTP_INITIALIZE",
    "HTTP_INITIALIZE_CONFIG",
    "HTTP_INITIALIZE_SERVER",
    "HTTP_SERVER_PROPERTY",
    "HTTP_SERVER_PROPERTY_HttpServerAuthenticationProperty",
    "HTTP_SERVER_PROPERTY_HttpServerLoggingProperty",
    "HTTP_SERVER_PROPERTY_HttpServerQosProperty",
    "HTTP_SERVER_PROPERTY_HttpServerTimeoutsProperty",
    "HTTP_SERVER_PROPERTY_HttpServerQueueLengthProperty",
    "HTTP_SERVER_PROPERTY_HttpServerStateProperty",
    "HTTP_SERVER_PROPERTY_HttpServer503VerbosityProperty",
    "HTTP_SERVER_PROPERTY_HttpServerBindingProperty",
    "HTTP_SERVER_PROPERTY_HttpServerExtendedAuthenticationProperty",
    "HTTP_SERVER_PROPERTY_HttpServerListenEndpointProperty",
    "HTTP_SERVER_PROPERTY_HttpServerChannelBindProperty",
    "HTTP_SERVER_PROPERTY_HttpServerProtectionLevelProperty",
    "HTTP_SERVER_PROPERTY_HttpServerDelegationProperty",
    "HTTP_PROPERTY_FLAGS",
    "HTTP_ENABLED_STATE",
    "HTTP_ENABLED_STATE_HttpEnabledStateActive",
    "HTTP_ENABLED_STATE_HttpEnabledStateInactive",
    "HTTP_STATE_INFO",
    "HTTP_503_RESPONSE_VERBOSITY",
    "HTTP_503_RESPONSE_VERBOSITY_Http503ResponseVerbosityBasic",
    "HTTP_503_RESPONSE_VERBOSITY_Http503ResponseVerbosityLimited",
    "HTTP_503_RESPONSE_VERBOSITY_Http503ResponseVerbosityFull",
    "HTTP_QOS_SETTING_TYPE",
    "HTTP_QOS_SETTING_TYPE_HttpQosSettingTypeBandwidth",
    "HTTP_QOS_SETTING_TYPE_HttpQosSettingTypeConnectionLimit",
    "HTTP_QOS_SETTING_TYPE_HttpQosSettingTypeFlowRate",
    "HTTP_QOS_SETTING_INFO",
    "HTTP_CONNECTION_LIMIT_INFO",
    "HTTP_BANDWIDTH_LIMIT_INFO",
    "HTTP_FLOWRATE_INFO",
    "HTTP_SERVICE_CONFIG_TIMEOUT_KEY",
    "HTTP_SERVICE_CONFIG_TIMEOUT_KEY_IdleConnectionTimeout",
    "HTTP_SERVICE_CONFIG_TIMEOUT_KEY_HeaderWaitTimeout",
    "HTTP_SERVICE_CONFIG_TIMEOUT_SET",
    "HTTP_TIMEOUT_LIMIT_INFO",
    "HTTP_SERVICE_CONFIG_SETTING_KEY",
    "HTTP_SERVICE_CONFIG_SETTING_KEY_HttpNone",
    "HTTP_SERVICE_CONFIG_SETTING_KEY_HttpTlsThrottle",
    "HTTP_SERVICE_CONFIG_SETTING_SET",
    "HTTP_LISTEN_ENDPOINT_INFO",
    "HTTP_SERVER_AUTHENTICATION_DIGEST_PARAMS",
    "HTTP_SERVER_AUTHENTICATION_BASIC_PARAMS",
    "HTTP_SERVER_AUTHENTICATION_INFO",
    "HTTP_SERVICE_BINDING_TYPE",
    "HTTP_SERVICE_BINDING_TYPE_HttpServiceBindingTypeNone",
    "HTTP_SERVICE_BINDING_TYPE_HttpServiceBindingTypeW",
    "HTTP_SERVICE_BINDING_TYPE_HttpServiceBindingTypeA",
    "HTTP_SERVICE_BINDING_BASE",
    "HTTP_SERVICE_BINDING_A",
    "HTTP_SERVICE_BINDING_W",
    "HTTP_AUTHENTICATION_HARDENING_LEVELS",
    "HTTP_AUTHENTICATION_HARDENING_LEVELS_HttpAuthenticationHardeningLegacy",
    "HTTP_AUTHENTICATION_HARDENING_LEVELS_HttpAuthenticationHardeningMedium",
    "HTTP_AUTHENTICATION_HARDENING_LEVELS_HttpAuthenticationHardeningStrict",
    "HTTP_CHANNEL_BIND_INFO",
    "HTTP_REQUEST_CHANNEL_BIND_STATUS",
    "HTTP_REQUEST_TOKEN_BINDING_INFO",
    "HTTP_LOGGING_TYPE",
    "HTTP_LOGGING_TYPE_HttpLoggingTypeW3C",
    "HTTP_LOGGING_TYPE_HttpLoggingTypeIIS",
    "HTTP_LOGGING_TYPE_HttpLoggingTypeNCSA",
    "HTTP_LOGGING_TYPE_HttpLoggingTypeRaw",
    "HTTP_LOGGING_ROLLOVER_TYPE",
    "HTTP_LOGGING_ROLLOVER_TYPE_HttpLoggingRolloverSize",
    "HTTP_LOGGING_ROLLOVER_TYPE_HttpLoggingRolloverDaily",
    "HTTP_LOGGING_ROLLOVER_TYPE_HttpLoggingRolloverWeekly",
    "HTTP_LOGGING_ROLLOVER_TYPE_HttpLoggingRolloverMonthly",
    "HTTP_LOGGING_ROLLOVER_TYPE_HttpLoggingRolloverHourly",
    "HTTP_LOGGING_INFO",
    "HTTP_BINDING_INFO",
    "HTTP_PROTECTION_LEVEL_TYPE",
    "HTTP_PROTECTION_LEVEL_TYPE_HttpProtectionLevelUnrestricted",
    "HTTP_PROTECTION_LEVEL_TYPE_HttpProtectionLevelEdgeRestricted",
    "HTTP_PROTECTION_LEVEL_TYPE_HttpProtectionLevelRestricted",
    "HTTP_PROTECTION_LEVEL_INFO",
    "HTTP_BYTE_RANGE",
    "HTTP_VERSION",
    "HTTP_SCHEME",
    "HTTP_SCHEME_HttpSchemeHttp",
    "HTTP_SCHEME_HttpSchemeHttps",
    "HTTP_SCHEME_HttpSchemeMaximum",
    "HTTP_VERB",
    "HTTP_VERB_HttpVerbUnparsed",
    "HTTP_VERB_HttpVerbUnknown",
    "HTTP_VERB_HttpVerbInvalid",
    "HTTP_VERB_HttpVerbOPTIONS",
    "HTTP_VERB_HttpVerbGET",
    "HTTP_VERB_HttpVerbHEAD",
    "HTTP_VERB_HttpVerbPOST",
    "HTTP_VERB_HttpVerbPUT",
    "HTTP_VERB_HttpVerbDELETE",
    "HTTP_VERB_HttpVerbTRACE",
    "HTTP_VERB_HttpVerbCONNECT",
    "HTTP_VERB_HttpVerbTRACK",
    "HTTP_VERB_HttpVerbMOVE",
    "HTTP_VERB_HttpVerbCOPY",
    "HTTP_VERB_HttpVerbPROPFIND",
    "HTTP_VERB_HttpVerbPROPPATCH",
    "HTTP_VERB_HttpVerbMKCOL",
    "HTTP_VERB_HttpVerbLOCK",
    "HTTP_VERB_HttpVerbUNLOCK",
    "HTTP_VERB_HttpVerbSEARCH",
    "HTTP_VERB_HttpVerbMaximum",
    "HTTP_HEADER_ID",
    "HTTP_HEADER_ID_HttpHeaderCacheControl",
    "HTTP_HEADER_ID_HttpHeaderConnection",
    "HTTP_HEADER_ID_HttpHeaderDate",
    "HTTP_HEADER_ID_HttpHeaderKeepAlive",
    "HTTP_HEADER_ID_HttpHeaderPragma",
    "HTTP_HEADER_ID_HttpHeaderTrailer",
    "HTTP_HEADER_ID_HttpHeaderTransferEncoding",
    "HTTP_HEADER_ID_HttpHeaderUpgrade",
    "HTTP_HEADER_ID_HttpHeaderVia",
    "HTTP_HEADER_ID_HttpHeaderWarning",
    "HTTP_HEADER_ID_HttpHeaderAllow",
    "HTTP_HEADER_ID_HttpHeaderContentLength",
    "HTTP_HEADER_ID_HttpHeaderContentType",
    "HTTP_HEADER_ID_HttpHeaderContentEncoding",
    "HTTP_HEADER_ID_HttpHeaderContentLanguage",
    "HTTP_HEADER_ID_HttpHeaderContentLocation",
    "HTTP_HEADER_ID_HttpHeaderContentMd5",
    "HTTP_HEADER_ID_HttpHeaderContentRange",
    "HTTP_HEADER_ID_HttpHeaderExpires",
    "HTTP_HEADER_ID_HttpHeaderLastModified",
    "HTTP_HEADER_ID_HttpHeaderAccept",
    "HTTP_HEADER_ID_HttpHeaderAcceptCharset",
    "HTTP_HEADER_ID_HttpHeaderAcceptEncoding",
    "HTTP_HEADER_ID_HttpHeaderAcceptLanguage",
    "HTTP_HEADER_ID_HttpHeaderAuthorization",
    "HTTP_HEADER_ID_HttpHeaderCookie",
    "HTTP_HEADER_ID_HttpHeaderExpect",
    "HTTP_HEADER_ID_HttpHeaderFrom",
    "HTTP_HEADER_ID_HttpHeaderHost",
    "HTTP_HEADER_ID_HttpHeaderIfMatch",
    "HTTP_HEADER_ID_HttpHeaderIfModifiedSince",
    "HTTP_HEADER_ID_HttpHeaderIfNoneMatch",
    "HTTP_HEADER_ID_HttpHeaderIfRange",
    "HTTP_HEADER_ID_HttpHeaderIfUnmodifiedSince",
    "HTTP_HEADER_ID_HttpHeaderMaxForwards",
    "HTTP_HEADER_ID_HttpHeaderProxyAuthorization",
    "HTTP_HEADER_ID_HttpHeaderReferer",
    "HTTP_HEADER_ID_HttpHeaderRange",
    "HTTP_HEADER_ID_HttpHeaderTe",
    "HTTP_HEADER_ID_HttpHeaderTranslate",
    "HTTP_HEADER_ID_HttpHeaderUserAgent",
    "HTTP_HEADER_ID_HttpHeaderRequestMaximum",
    "HTTP_HEADER_ID_HttpHeaderAcceptRanges",
    "HTTP_HEADER_ID_HttpHeaderAge",
    "HTTP_HEADER_ID_HttpHeaderEtag",
    "HTTP_HEADER_ID_HttpHeaderLocation",
    "HTTP_HEADER_ID_HttpHeaderProxyAuthenticate",
    "HTTP_HEADER_ID_HttpHeaderRetryAfter",
    "HTTP_HEADER_ID_HttpHeaderServer",
    "HTTP_HEADER_ID_HttpHeaderSetCookie",
    "HTTP_HEADER_ID_HttpHeaderVary",
    "HTTP_HEADER_ID_HttpHeaderWwwAuthenticate",
    "HTTP_HEADER_ID_HttpHeaderResponseMaximum",
    "HTTP_HEADER_ID_HttpHeaderMaximum",
    "HTTP_KNOWN_HEADER",
    "HTTP_UNKNOWN_HEADER",
    "HTTP_LOG_DATA_TYPE",
    "HTTP_LOG_DATA_TYPE_HttpLogDataTypeFields",
    "HTTP_LOG_DATA",
    "HTTP_LOG_FIELDS_DATA",
    "HTTP_DATA_CHUNK_TYPE",
    "HTTP_DATA_CHUNK_TYPE_HttpDataChunkFromMemory",
    "HTTP_DATA_CHUNK_TYPE_HttpDataChunkFromFileHandle",
    "HTTP_DATA_CHUNK_TYPE_HttpDataChunkFromFragmentCache",
    "HTTP_DATA_CHUNK_TYPE_HttpDataChunkFromFragmentCacheEx",
    "HTTP_DATA_CHUNK_TYPE_HttpDataChunkTrailers",
    "HTTP_DATA_CHUNK_TYPE_HttpDataChunkMaximum",
    "HTTP_DATA_CHUNK",
    "HTTP_REQUEST_HEADERS",
    "HTTP_RESPONSE_HEADERS",
    "HTTP_DELEGATE_REQUEST_PROPERTY_ID",
    "HTTP_DELEGATE_REQUEST_PROPERTY_ID_DelegateRequestReservedProperty",
    "HTTP_DELEGATE_REQUEST_PROPERTY_ID_DelegateRequestDelegateUrlProperty",
    "HTTP_DELEGATE_REQUEST_PROPERTY_INFO",
    "HTTP_CREATE_REQUEST_QUEUE_PROPERTY_ID",
    "HTTP_CREATE_REQUEST_QUEUE_PROPERTY_ID_CreateRequestQueueExternalIdProperty",
    "HTTP_CREATE_REQUEST_QUEUE_PROPERTY_ID_CreateRequestQueueMax",
    "HTTP_CREATE_REQUEST_QUEUE_PROPERTY_INFO",
    "HTTP_TRANSPORT_ADDRESS",
    "HTTP_COOKED_URL",
    "HTTP_AUTH_STATUS",
    "HTTP_AUTH_STATUS_HttpAuthStatusSuccess",
    "HTTP_AUTH_STATUS_HttpAuthStatusNotAuthenticated",
    "HTTP_AUTH_STATUS_HttpAuthStatusFailure",
    "HTTP_REQUEST_AUTH_TYPE",
    "HTTP_REQUEST_AUTH_TYPE_HttpRequestAuthTypeNone",
    "HTTP_REQUEST_AUTH_TYPE_HttpRequestAuthTypeBasic",
    "HTTP_REQUEST_AUTH_TYPE_HttpRequestAuthTypeDigest",
    "HTTP_REQUEST_AUTH_TYPE_HttpRequestAuthTypeNTLM",
    "HTTP_REQUEST_AUTH_TYPE_HttpRequestAuthTypeNegotiate",
    "HTTP_REQUEST_AUTH_TYPE_HttpRequestAuthTypeKerberos",
    "HTTP_SSL_CLIENT_CERT_INFO",
    "HTTP_SSL_INFO",
    "HTTP_SSL_PROTOCOL_INFO",
    "HTTP_REQUEST_SIZING_TYPE",
    "HTTP_REQUEST_SIZING_TYPE_HttpRequestSizingTypeTlsHandshakeLeg1ClientData",
    "HTTP_REQUEST_SIZING_TYPE_HttpRequestSizingTypeTlsHandshakeLeg1ServerData",
    "HTTP_REQUEST_SIZING_TYPE_HttpRequestSizingTypeTlsHandshakeLeg2ClientData",
    "HTTP_REQUEST_SIZING_TYPE_HttpRequestSizingTypeTlsHandshakeLeg2ServerData",
    "HTTP_REQUEST_SIZING_TYPE_HttpRequestSizingTypeHeaders",
    "HTTP_REQUEST_SIZING_TYPE_HttpRequestSizingTypeMax",
    "HTTP_REQUEST_SIZING_INFO",
    "HTTP_REQUEST_TIMING_TYPE",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeConnectionStart",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeDataStart",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsCertificateLoadStart",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsCertificateLoadEnd",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsHandshakeLeg1Start",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsHandshakeLeg1End",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsHandshakeLeg2Start",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsHandshakeLeg2End",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsAttributesQueryStart",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsAttributesQueryEnd",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsClientCertQueryStart",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsClientCertQueryEnd",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeHttp2StreamStart",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeHttp2HeaderDecodeStart",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeHttp2HeaderDecodeEnd",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestHeaderParseStart",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestHeaderParseEnd",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestRoutingStart",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestRoutingEnd",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestQueuedForInspection",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestDeliveredForInspection",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestReturnedAfterInspection",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestQueuedForDelegation",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestDeliveredForDelegation",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestReturnedAfterDelegation",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestQueuedForIO",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestDeliveredForIO",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeHttp3StreamStart",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeHttp3HeaderDecodeStart",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeHttp3HeaderDecodeEnd",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeMax",
    "HTTP_REQUEST_TIMING_INFO",
    "HTTP_REQUEST_INFO_TYPE",
    "HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeAuth",
    "HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeChannelBind",
    "HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeSslProtocol",
    "HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeSslTokenBindingDraft",
    "HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeSslTokenBinding",
    "HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeRequestTiming",
    "HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeTcpInfoV0",
    "HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeRequestSizing",
    "HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeQuicStats",
    "HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeTcpInfoV1",
    "HTTP_REQUEST_INFO",
    "HTTP_REQUEST_AUTH_INFO",
    "HTTP_REQUEST_V1",
    "HTTP_REQUEST_V2",
    "HTTP_RESPONSE_V1",
    "HTTP_RESPONSE_INFO_TYPE",
    "HTTP_RESPONSE_INFO_TYPE_HttpResponseInfoTypeMultipleKnownHeaders",
    "HTTP_RESPONSE_INFO_TYPE_HttpResponseInfoTypeAuthenticationProperty",
    "HTTP_RESPONSE_INFO_TYPE_HttpResponseInfoTypeQoSProperty",
    "HTTP_RESPONSE_INFO_TYPE_HttpResponseInfoTypeChannelBind",
    "HTTP_RESPONSE_INFO",
    "HTTP_MULTIPLE_KNOWN_HEADERS",
    "HTTP_RESPONSE_V2",
    "HTTPAPI_VERSION",
    "HTTP_CACHE_POLICY_TYPE",
    "HTTP_CACHE_POLICY_TYPE_HttpCachePolicyNocache",
    "HTTP_CACHE_POLICY_TYPE_HttpCachePolicyUserInvalidates",
    "HTTP_CACHE_POLICY_TYPE_HttpCachePolicyTimeToLive",
    "HTTP_CACHE_POLICY_TYPE_HttpCachePolicyMaximum",
    "HTTP_CACHE_POLICY",
    "HTTP_SERVICE_CONFIG_ID",
    "HTTP_SERVICE_CONFIG_ID_HttpServiceConfigIPListenList",
    "HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSSLCertInfo",
    "HTTP_SERVICE_CONFIG_ID_HttpServiceConfigUrlAclInfo",
    "HTTP_SERVICE_CONFIG_ID_HttpServiceConfigTimeout",
    "HTTP_SERVICE_CONFIG_ID_HttpServiceConfigCache",
    "HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSslSniCertInfo",
    "HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSslCcsCertInfo",
    "HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSetting",
    "HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSslCertInfoEx",
    "HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSslSniCertInfoEx",
    "HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSslCcsCertInfoEx",
    "HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSslScopedCcsCertInfo",
    "HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSslScopedCcsCertInfoEx",
    "HTTP_SERVICE_CONFIG_ID_HttpServiceConfigMax",
    "HTTP_SERVICE_CONFIG_QUERY_TYPE",
    "HTTP_SERVICE_CONFIG_QUERY_TYPE_HttpServiceConfigQueryExact",
    "HTTP_SERVICE_CONFIG_QUERY_TYPE_HttpServiceConfigQueryNext",
    "HTTP_SERVICE_CONFIG_QUERY_TYPE_HttpServiceConfigQueryMax",
    "HTTP_SERVICE_CONFIG_SSL_KEY",
    "HTTP_SERVICE_CONFIG_SSL_KEY_EX",
    "HTTP_SERVICE_CONFIG_SSL_SNI_KEY",
    "HTTP_SERVICE_CONFIG_SSL_CCS_KEY",
    "HTTP_SERVICE_CONFIG_SSL_PARAM",
    "HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE",
    "HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE_ExParamTypeHttp2Window",
    "HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE_ExParamTypeHttp2SettingsLimits",
    "HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE_ExParamTypeHttpPerformance",
    "HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE_ExParamTypeTlsRestrictions",
    "HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE_ExParamTypeErrorHeaders",
    "HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE_ExParamTypeTlsSessionTicketKeys",
    "HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE_ExParamTypeMax",
    "HTTP2_WINDOW_SIZE_PARAM",
    "HTTP2_SETTINGS_LIMITS_PARAM",
    "HTTP_PERFORMANCE_PARAM_TYPE",
    "HTTP_PERFORMANCE_PARAM_TYPE_PerformanceParamSendBufferingFlags",
    "HTTP_PERFORMANCE_PARAM_TYPE_PerformanceParamAggressiveICW",
    "HTTP_PERFORMANCE_PARAM_TYPE_PerformanceParamMaxSendBufferSize",
    "HTTP_PERFORMANCE_PARAM_TYPE_PerformanceParamMaxConcurrentClientStreams",
    "HTTP_PERFORMANCE_PARAM_TYPE_PerformanceParamMaxReceiveBufferSize",
    "HTTP_PERFORMANCE_PARAM_TYPE_PerformanceParamDecryptOnSspiThread",
    "HTTP_PERFORMANCE_PARAM_TYPE_PerformanceParamMax",
    "HTTP_PERFORMANCE_PARAM",
    "HTTP_TLS_RESTRICTIONS_PARAM",
    "HTTP_ERROR_HEADERS_PARAM",
    "HTTP_TLS_SESSION_TICKET_KEYS_PARAM",
    "HTTP_SERVICE_CONFIG_SSL_PARAM_EX",
    "HTTP_SERVICE_CONFIG_SSL_SET",
    "HTTP_SERVICE_CONFIG_SSL_SNI_SET",
    "HTTP_SERVICE_CONFIG_SSL_CCS_SET",
    "HTTP_SERVICE_CONFIG_SSL_SET_EX",
    "HTTP_SERVICE_CONFIG_SSL_SNI_SET_EX",
    "HTTP_SERVICE_CONFIG_SSL_CCS_SET_EX",
    "HTTP_SERVICE_CONFIG_SSL_QUERY",
    "HTTP_SERVICE_CONFIG_SSL_SNI_QUERY",
    "HTTP_SERVICE_CONFIG_SSL_CCS_QUERY",
    "HTTP_SERVICE_CONFIG_SSL_QUERY_EX",
    "HTTP_SERVICE_CONFIG_SSL_SNI_QUERY_EX",
    "HTTP_SERVICE_CONFIG_SSL_CCS_QUERY_EX",
    "HTTP_SERVICE_CONFIG_IP_LISTEN_PARAM",
    "HTTP_SERVICE_CONFIG_IP_LISTEN_QUERY",
    "HTTP_SERVICE_CONFIG_URLACL_KEY",
    "HTTP_SERVICE_CONFIG_URLACL_PARAM",
    "HTTP_SERVICE_CONFIG_URLACL_SET",
    "HTTP_SERVICE_CONFIG_URLACL_QUERY",
    "HTTP_SERVICE_CONFIG_CACHE_KEY",
    "HTTP_SERVICE_CONFIG_CACHE_KEY_MaxCacheResponseSize",
    "HTTP_SERVICE_CONFIG_CACHE_KEY_CacheRangeChunkSize",
    "HTTP_SERVICE_CONFIG_CACHE_SET",
    "HTTP_REQUEST_PROPERTY",
    "HTTP_REQUEST_PROPERTY_HttpRequestPropertyIsb",
    "HTTP_REQUEST_PROPERTY_HttpRequestPropertyTcpInfoV0",
    "HTTP_REQUEST_PROPERTY_HttpRequestPropertyQuicStats",
    "HTTP_REQUEST_PROPERTY_HttpRequestPropertyTcpInfoV1",
    "HTTP_REQUEST_PROPERTY_HttpRequestPropertySni",
    "HTTP_REQUEST_PROPERTY_HttpRequestPropertyStreamError",
    "HTTP_REQUEST_PROPERTY_HttpRequestPropertyWskApiTimings",
    "HTTP_REQUEST_PROPERTY_HttpRequestPropertyQuicApiTimings",
    "HTTP_QUERY_REQUEST_QUALIFIER_TCP",
    "HTTP_QUERY_REQUEST_QUALIFIER_QUIC",
    "HTTP_REQUEST_PROPERTY_SNI",
    "HTTP_REQUEST_PROPERTY_STREAM_ERROR",
    "HTTP_WSK_API_TIMINGS",
    "HTTP_QUIC_STREAM_API_TIMINGS",
    "HTTP_QUIC_CONNECTION_API_TIMINGS",
    "HTTP_QUIC_API_TIMINGS",
    "HTTP_FEATURE_ID",
    "HTTP_FEATURE_ID_HttpFeatureUnknown",
    "HTTP_FEATURE_ID_HttpFeatureResponseTrailers",
    "HTTP_FEATURE_ID_HttpFeatureApiTimings",
    "HTTP_FEATURE_ID_HttpFeatureDelegateEx",
    "HTTP_FEATURE_ID_HttpFeatureHttp3",
    "HTTP_FEATURE_ID_HttpFeaturemax",
    "HttpInitialize",
    "HttpTerminate",
    "HttpCreateHttpHandle",
    "HttpCreateRequestQueue",
    "HttpCloseRequestQueue",
    "HttpSetRequestQueueProperty",
    "HttpQueryRequestQueueProperty",
    "HttpSetRequestProperty",
    "HttpShutdownRequestQueue",
    "HttpReceiveClientCertificate",
    "HttpCreateServerSession",
    "HttpCloseServerSession",
    "HttpQueryServerSessionProperty",
    "HttpSetServerSessionProperty",
    "HttpAddUrl",
    "HttpRemoveUrl",
    "HttpCreateUrlGroup",
    "HttpCloseUrlGroup",
    "HttpAddUrlToUrlGroup",
    "HttpRemoveUrlFromUrlGroup",
    "HttpSetUrlGroupProperty",
    "HttpQueryUrlGroupProperty",
    "HttpPrepareUrl",
    "HttpReceiveHttpRequest",
    "HttpReceiveRequestEntityBody",
    "HttpSendHttpResponse",
    "HttpSendResponseEntityBody",
    "HttpDeclarePush",
    "HttpWaitForDisconnect",
    "HttpWaitForDisconnectEx",
    "HttpCancelHttpRequest",
    "HttpWaitForDemandStart",
    "HttpIsFeatureSupported",
    "HttpDelegateRequestEx",
    "HttpFindUrlGroupId",
    "HttpFlushResponseCache",
    "HttpAddFragmentToCache",
    "HttpReadFragmentFromCache",
    "HttpSetServiceConfiguration",
    "HttpUpdateServiceConfiguration",
    "HttpDeleteServiceConfiguration",
    "HttpQueryServiceConfiguration",
    "HttpGetExtension",
]
