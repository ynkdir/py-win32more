from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Networking.HttpServer
import Windows.Win32.Networking.WinSock
import Windows.Win32.Security
import Windows.Win32.System.IO
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
HTTP_DEMAND_CBT: UInt32 = 4
HTTP_MAX_SERVER_QUEUE_LENGTH: UInt32 = 2147483647
HTTP_MIN_SERVER_QUEUE_LENGTH: UInt32 = 1
HTTP_AUTH_ENABLE_BASIC: UInt32 = 1
HTTP_AUTH_ENABLE_DIGEST: UInt32 = 2
HTTP_AUTH_ENABLE_NTLM: UInt32 = 4
HTTP_AUTH_ENABLE_NEGOTIATE: UInt32 = 8
HTTP_AUTH_ENABLE_KERBEROS: UInt32 = 16
HTTP_AUTH_EX_FLAG_ENABLE_KERBEROS_CREDENTIAL_CACHING: UInt32 = 1
HTTP_AUTH_EX_FLAG_CAPTURE_CREDENTIAL: UInt32 = 2
HTTP_CHANNEL_BIND_PROXY: UInt32 = 1
HTTP_CHANNEL_BIND_PROXY_COHOSTING: UInt32 = 32
HTTP_CHANNEL_BIND_NO_SERVICE_NAME_CHECK: UInt32 = 2
HTTP_CHANNEL_BIND_DOTLESS_SERVICE: UInt32 = 4
HTTP_CHANNEL_BIND_SECURE_CHANNEL_TOKEN: UInt32 = 8
HTTP_CHANNEL_BIND_CLIENT_SERVICE: UInt32 = 16
HTTP_LOG_FIELD_DATE: UInt32 = 1
HTTP_LOG_FIELD_TIME: UInt32 = 2
HTTP_LOG_FIELD_CLIENT_IP: UInt32 = 4
HTTP_LOG_FIELD_USER_NAME: UInt32 = 8
HTTP_LOG_FIELD_SITE_NAME: UInt32 = 16
HTTP_LOG_FIELD_COMPUTER_NAME: UInt32 = 32
HTTP_LOG_FIELD_SERVER_IP: UInt32 = 64
HTTP_LOG_FIELD_METHOD: UInt32 = 128
HTTP_LOG_FIELD_URI_STEM: UInt32 = 256
HTTP_LOG_FIELD_URI_QUERY: UInt32 = 512
HTTP_LOG_FIELD_STATUS: UInt32 = 1024
HTTP_LOG_FIELD_WIN32_STATUS: UInt32 = 2048
HTTP_LOG_FIELD_BYTES_SENT: UInt32 = 4096
HTTP_LOG_FIELD_BYTES_RECV: UInt32 = 8192
HTTP_LOG_FIELD_TIME_TAKEN: UInt32 = 16384
HTTP_LOG_FIELD_SERVER_PORT: UInt32 = 32768
HTTP_LOG_FIELD_USER_AGENT: UInt32 = 65536
HTTP_LOG_FIELD_COOKIE: UInt32 = 131072
HTTP_LOG_FIELD_REFERER: UInt32 = 262144
HTTP_LOG_FIELD_VERSION: UInt32 = 524288
HTTP_LOG_FIELD_HOST: UInt32 = 1048576
HTTP_LOG_FIELD_SUB_STATUS: UInt32 = 2097152
HTTP_LOG_FIELD_STREAM_ID: UInt32 = 134217728
HTTP_LOG_FIELD_STREAM_ID_EX: UInt32 = 268435456
HTTP_LOG_FIELD_TRANSPORT_TYPE: UInt32 = 536870912
HTTP_LOG_FIELD_CLIENT_PORT: UInt32 = 4194304
HTTP_LOG_FIELD_URI: UInt32 = 8388608
HTTP_LOG_FIELD_SITE_ID: UInt32 = 16777216
HTTP_LOG_FIELD_REASON: UInt32 = 33554432
HTTP_LOG_FIELD_QUEUE_NAME: UInt32 = 67108864
HTTP_LOG_FIELD_CORRELATION_ID: UInt32 = 1073741824
HTTP_LOGGING_FLAG_LOCAL_TIME_ROLLOVER: UInt32 = 1
HTTP_LOGGING_FLAG_USE_UTF8_CONVERSION: UInt32 = 2
HTTP_LOGGING_FLAG_LOG_ERRORS_ONLY: UInt32 = 4
HTTP_LOGGING_FLAG_LOG_SUCCESS_ONLY: UInt32 = 8
HTTP_CREATE_REQUEST_QUEUE_FLAG_OPEN_EXISTING: UInt32 = 1
HTTP_CREATE_REQUEST_QUEUE_FLAG_CONTROLLER: UInt32 = 2
HTTP_CREATE_REQUEST_QUEUE_FLAG_DELEGATION: UInt32 = 8
HTTP_RECEIVE_REQUEST_ENTITY_BODY_FLAG_FILL_BUFFER: UInt32 = 1
HTTP_SEND_RESPONSE_FLAG_DISCONNECT: UInt32 = 1
HTTP_SEND_RESPONSE_FLAG_MORE_DATA: UInt32 = 2
HTTP_SEND_RESPONSE_FLAG_BUFFER_DATA: UInt32 = 4
HTTP_SEND_RESPONSE_FLAG_ENABLE_NAGLING: UInt32 = 8
HTTP_SEND_RESPONSE_FLAG_PROCESS_RANGES: UInt32 = 32
HTTP_SEND_RESPONSE_FLAG_OPAQUE: UInt32 = 64
HTTP_SEND_RESPONSE_FLAG_GOAWAY: UInt32 = 256
HTTP_FLUSH_RESPONSE_FLAG_RECURSIVE: UInt32 = 1
HTTP_URL_FLAG_REMOVE_ALL: UInt32 = 1
HTTP_RECEIVE_SECURE_CHANNEL_TOKEN: UInt32 = 1
HTTP_RECEIVE_FULL_CHAIN: UInt32 = 2
HTTP_REQUEST_SIZING_INFO_FLAG_TCP_FAST_OPEN: UInt32 = 1
HTTP_REQUEST_SIZING_INFO_FLAG_TLS_SESSION_RESUMPTION: UInt32 = 2
HTTP_REQUEST_SIZING_INFO_FLAG_TLS_FALSE_START: UInt32 = 4
HTTP_REQUEST_SIZING_INFO_FLAG_FIRST_REQUEST: UInt32 = 8
HTTP_REQUEST_AUTH_FLAG_TOKEN_FOR_CACHED_CRED: UInt32 = 1
HTTP_REQUEST_FLAG_MORE_ENTITY_BODY_EXISTS: UInt32 = 1
HTTP_REQUEST_FLAG_IP_ROUTED: UInt32 = 2
HTTP_REQUEST_FLAG_HTTP2: UInt32 = 4
HTTP_REQUEST_FLAG_HTTP3: UInt32 = 8
HTTP_RESPONSE_FLAG_MULTIPLE_ENCODINGS_AVAILABLE: UInt32 = 1
HTTP_RESPONSE_FLAG_MORE_ENTITY_BODY_EXISTS: UInt32 = 2
HTTP_RESPONSE_INFO_FLAGS_PRESERVE_ORDER: UInt32 = 1
HTTP_SERVICE_CONFIG_SSL_FLAG_USE_DS_MAPPER: UInt32 = 1
HTTP_SERVICE_CONFIG_SSL_FLAG_NEGOTIATE_CLIENT_CERT: UInt32 = 2
HTTP_SERVICE_CONFIG_SSL_FLAG_NO_RAW_FILTER: UInt32 = 4
HTTP_SERVICE_CONFIG_SSL_FLAG_REJECT: UInt32 = 8
HTTP_SERVICE_CONFIG_SSL_FLAG_DISABLE_HTTP2: UInt32 = 16
HTTP_SERVICE_CONFIG_SSL_FLAG_DISABLE_QUIC: UInt32 = 32
HTTP_SERVICE_CONFIG_SSL_FLAG_DISABLE_TLS13: UInt32 = 64
HTTP_SERVICE_CONFIG_SSL_FLAG_DISABLE_OCSP_STAPLING: UInt32 = 128
HTTP_SERVICE_CONFIG_SSL_FLAG_ENABLE_TOKEN_BINDING: UInt32 = 256
HTTP_SERVICE_CONFIG_SSL_FLAG_LOG_EXTENDED_EVENTS: UInt32 = 512
HTTP_SERVICE_CONFIG_SSL_FLAG_DISABLE_LEGACY_TLS: UInt32 = 1024
HTTP_SERVICE_CONFIG_SSL_FLAG_ENABLE_SESSION_TICKET: UInt32 = 2048
HTTP_SERVICE_CONFIG_SSL_FLAG_DISABLE_TLS12: UInt32 = 4096
HTTP_SERVICE_CONFIG_SSL_FLAG_ENABLE_CLIENT_CORRELATION: UInt32 = 8192
HTTP_REQUEST_PROPERTY_SNI_HOST_MAX_LENGTH: UInt32 = 255
HTTP_REQUEST_PROPERTY_SNI_FLAG_SNI_USED: UInt32 = 1
HTTP_REQUEST_PROPERTY_SNI_FLAG_NO_SNI: UInt32 = 2
HTTP_VERSION_CONSTANT: String = 'HTTP/1.0'
@winfunctype('HTTPAPI.dll')
def HttpInitialize(Version: Windows.Win32.Networking.HttpServer.HTTPAPI_VERSION, Flags: Windows.Win32.Networking.HttpServer.HTTP_INITIALIZE, pReserved: c_void_p) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpTerminate(Flags: Windows.Win32.Networking.HttpServer.HTTP_INITIALIZE, pReserved: c_void_p) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpCreateHttpHandle(RequestQueueHandle: POINTER(Windows.Win32.Foundation.HANDLE), Reserved: UInt32) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpCreateRequestQueue(Version: Windows.Win32.Networking.HttpServer.HTTPAPI_VERSION, Name: Windows.Win32.Foundation.PWSTR, SecurityAttributes: POINTER(Windows.Win32.Security.SECURITY_ATTRIBUTES_head), Flags: UInt32, RequestQueueHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpCloseRequestQueue(RequestQueueHandle: Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpSetRequestQueueProperty(RequestQueueHandle: Windows.Win32.Foundation.HANDLE, Property: Windows.Win32.Networking.HttpServer.HTTP_SERVER_PROPERTY, PropertyInformation: c_void_p, PropertyInformationLength: UInt32, Reserved1: UInt32, Reserved2: c_void_p) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpQueryRequestQueueProperty(RequestQueueHandle: Windows.Win32.Foundation.HANDLE, Property: Windows.Win32.Networking.HttpServer.HTTP_SERVER_PROPERTY, PropertyInformation: c_void_p, PropertyInformationLength: UInt32, Reserved1: UInt32, ReturnLength: POINTER(UInt32), Reserved2: c_void_p) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpSetRequestProperty(RequestQueueHandle: Windows.Win32.Foundation.HANDLE, Id: UInt64, PropertyId: Windows.Win32.Networking.HttpServer.HTTP_REQUEST_PROPERTY, Input: c_void_p, InputPropertySize: UInt32, Overlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpShutdownRequestQueue(RequestQueueHandle: Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpReceiveClientCertificate(RequestQueueHandle: Windows.Win32.Foundation.HANDLE, ConnectionId: UInt64, Flags: UInt32, SslClientCertInfo: POINTER(Windows.Win32.Networking.HttpServer.HTTP_SSL_CLIENT_CERT_INFO_head), SslClientCertInfoSize: UInt32, BytesReceived: POINTER(UInt32), Overlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpCreateServerSession(Version: Windows.Win32.Networking.HttpServer.HTTPAPI_VERSION, ServerSessionId: POINTER(UInt64), Reserved: UInt32) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpCloseServerSession(ServerSessionId: UInt64) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpQueryServerSessionProperty(ServerSessionId: UInt64, Property: Windows.Win32.Networking.HttpServer.HTTP_SERVER_PROPERTY, PropertyInformation: c_void_p, PropertyInformationLength: UInt32, ReturnLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpSetServerSessionProperty(ServerSessionId: UInt64, Property: Windows.Win32.Networking.HttpServer.HTTP_SERVER_PROPERTY, PropertyInformation: c_void_p, PropertyInformationLength: UInt32) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpAddUrl(RequestQueueHandle: Windows.Win32.Foundation.HANDLE, FullyQualifiedUrl: Windows.Win32.Foundation.PWSTR, Reserved: c_void_p) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpRemoveUrl(RequestQueueHandle: Windows.Win32.Foundation.HANDLE, FullyQualifiedUrl: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpCreateUrlGroup(ServerSessionId: UInt64, pUrlGroupId: POINTER(UInt64), Reserved: UInt32) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpCloseUrlGroup(UrlGroupId: UInt64) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpAddUrlToUrlGroup(UrlGroupId: UInt64, pFullyQualifiedUrl: Windows.Win32.Foundation.PWSTR, UrlContext: UInt64, Reserved: UInt32) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpRemoveUrlFromUrlGroup(UrlGroupId: UInt64, pFullyQualifiedUrl: Windows.Win32.Foundation.PWSTR, Flags: UInt32) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpSetUrlGroupProperty(UrlGroupId: UInt64, Property: Windows.Win32.Networking.HttpServer.HTTP_SERVER_PROPERTY, PropertyInformation: c_void_p, PropertyInformationLength: UInt32) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpQueryUrlGroupProperty(UrlGroupId: UInt64, Property: Windows.Win32.Networking.HttpServer.HTTP_SERVER_PROPERTY, PropertyInformation: c_void_p, PropertyInformationLength: UInt32, ReturnLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpPrepareUrl(Reserved: c_void_p, Flags: UInt32, Url: Windows.Win32.Foundation.PWSTR, PreparedUrl: POINTER(Windows.Win32.Foundation.PWSTR)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpReceiveHttpRequest(RequestQueueHandle: Windows.Win32.Foundation.HANDLE, RequestId: UInt64, Flags: Windows.Win32.Networking.HttpServer.HTTP_RECEIVE_HTTP_REQUEST_FLAGS, RequestBuffer: POINTER(Windows.Win32.Networking.HttpServer.HTTP_REQUEST_V2_head), RequestBufferLength: UInt32, BytesReturned: POINTER(UInt32), Overlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpReceiveRequestEntityBody(RequestQueueHandle: Windows.Win32.Foundation.HANDLE, RequestId: UInt64, Flags: UInt32, EntityBuffer: c_void_p, EntityBufferLength: UInt32, BytesReturned: POINTER(UInt32), Overlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpSendHttpResponse(RequestQueueHandle: Windows.Win32.Foundation.HANDLE, RequestId: UInt64, Flags: UInt32, HttpResponse: POINTER(Windows.Win32.Networking.HttpServer.HTTP_RESPONSE_V2_head), CachePolicy: POINTER(Windows.Win32.Networking.HttpServer.HTTP_CACHE_POLICY_head), BytesSent: POINTER(UInt32), Reserved1: c_void_p, Reserved2: UInt32, Overlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head), LogData: POINTER(Windows.Win32.Networking.HttpServer.HTTP_LOG_DATA_head)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpSendResponseEntityBody(RequestQueueHandle: Windows.Win32.Foundation.HANDLE, RequestId: UInt64, Flags: UInt32, EntityChunkCount: UInt16, EntityChunks: POINTER(Windows.Win32.Networking.HttpServer.HTTP_DATA_CHUNK_head), BytesSent: POINTER(UInt32), Reserved1: c_void_p, Reserved2: UInt32, Overlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head), LogData: POINTER(Windows.Win32.Networking.HttpServer.HTTP_LOG_DATA_head)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpDeclarePush(RequestQueueHandle: Windows.Win32.Foundation.HANDLE, RequestId: UInt64, Verb: Windows.Win32.Networking.HttpServer.HTTP_VERB, Path: Windows.Win32.Foundation.PWSTR, Query: Windows.Win32.Foundation.PSTR, Headers: POINTER(Windows.Win32.Networking.HttpServer.HTTP_REQUEST_HEADERS_head)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpWaitForDisconnect(RequestQueueHandle: Windows.Win32.Foundation.HANDLE, ConnectionId: UInt64, Overlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpWaitForDisconnectEx(RequestQueueHandle: Windows.Win32.Foundation.HANDLE, ConnectionId: UInt64, Reserved: UInt32, Overlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpCancelHttpRequest(RequestQueueHandle: Windows.Win32.Foundation.HANDLE, RequestId: UInt64, Overlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpWaitForDemandStart(RequestQueueHandle: Windows.Win32.Foundation.HANDLE, Overlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpIsFeatureSupported(FeatureId: Windows.Win32.Networking.HttpServer.HTTP_FEATURE_ID) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('HTTPAPI.dll')
def HttpDelegateRequestEx(RequestQueueHandle: Windows.Win32.Foundation.HANDLE, DelegateQueueHandle: Windows.Win32.Foundation.HANDLE, RequestId: UInt64, DelegateUrlGroupId: UInt64, PropertyInfoSetSize: UInt32, PropertyInfoSet: POINTER(Windows.Win32.Networking.HttpServer.HTTP_DELEGATE_REQUEST_PROPERTY_INFO_head)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpFindUrlGroupId(FullyQualifiedUrl: Windows.Win32.Foundation.PWSTR, RequestQueueHandle: Windows.Win32.Foundation.HANDLE, UrlGroupId: POINTER(UInt64)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpFlushResponseCache(RequestQueueHandle: Windows.Win32.Foundation.HANDLE, UrlPrefix: Windows.Win32.Foundation.PWSTR, Flags: UInt32, Overlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpAddFragmentToCache(RequestQueueHandle: Windows.Win32.Foundation.HANDLE, UrlPrefix: Windows.Win32.Foundation.PWSTR, DataChunk: POINTER(Windows.Win32.Networking.HttpServer.HTTP_DATA_CHUNK_head), CachePolicy: POINTER(Windows.Win32.Networking.HttpServer.HTTP_CACHE_POLICY_head), Overlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpReadFragmentFromCache(RequestQueueHandle: Windows.Win32.Foundation.HANDLE, UrlPrefix: Windows.Win32.Foundation.PWSTR, ByteRange: POINTER(Windows.Win32.Networking.HttpServer.HTTP_BYTE_RANGE_head), Buffer: c_void_p, BufferLength: UInt32, BytesRead: POINTER(UInt32), Overlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpSetServiceConfiguration(ServiceHandle: Windows.Win32.Foundation.HANDLE, ConfigId: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_ID, pConfigInformation: c_void_p, ConfigInformationLength: UInt32, pOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpUpdateServiceConfiguration(Handle: Windows.Win32.Foundation.HANDLE, ConfigId: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_ID, ConfigInfo: c_void_p, ConfigInfoLength: UInt32, Overlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpDeleteServiceConfiguration(ServiceHandle: Windows.Win32.Foundation.HANDLE, ConfigId: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_ID, pConfigInformation: c_void_p, ConfigInformationLength: UInt32, pOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpQueryServiceConfiguration(ServiceHandle: Windows.Win32.Foundation.HANDLE, ConfigId: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_ID, pInput: c_void_p, InputLength: UInt32, pOutput: c_void_p, OutputLength: UInt32, pReturnLength: POINTER(UInt32), pOverlapped: POINTER(Windows.Win32.System.IO.OVERLAPPED_head)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpGetExtension(Version: Windows.Win32.Networking.HttpServer.HTTPAPI_VERSION, Extension: UInt32, Buffer: c_void_p, BufferSize: UInt32) -> UInt32: ...
class HTTP2_SETTINGS_LIMITS_PARAM(Structure):
    Http2MaxSettingsPerFrame: UInt32
    Http2MaxSettingsPerMinute: UInt32
class HTTP2_WINDOW_SIZE_PARAM(Structure):
    Http2ReceiveWindowSize: UInt32
class HTTPAPI_VERSION(Structure):
    HttpApiMajorVersion: UInt16
    HttpApiMinorVersion: UInt16
HTTP_503_RESPONSE_VERBOSITY = Int32
HTTP_503_RESPONSE_VERBOSITY_Http503ResponseVerbosityBasic: HTTP_503_RESPONSE_VERBOSITY = 0
HTTP_503_RESPONSE_VERBOSITY_Http503ResponseVerbosityLimited: HTTP_503_RESPONSE_VERBOSITY = 1
HTTP_503_RESPONSE_VERBOSITY_Http503ResponseVerbosityFull: HTTP_503_RESPONSE_VERBOSITY = 2
HTTP_AUTHENTICATION_HARDENING_LEVELS = Int32
HTTP_AUTHENTICATION_HARDENING_LEVELS_HttpAuthenticationHardeningLegacy: HTTP_AUTHENTICATION_HARDENING_LEVELS = 0
HTTP_AUTHENTICATION_HARDENING_LEVELS_HttpAuthenticationHardeningMedium: HTTP_AUTHENTICATION_HARDENING_LEVELS = 1
HTTP_AUTHENTICATION_HARDENING_LEVELS_HttpAuthenticationHardeningStrict: HTTP_AUTHENTICATION_HARDENING_LEVELS = 2
HTTP_AUTH_STATUS = Int32
HTTP_AUTH_STATUS_HttpAuthStatusSuccess: HTTP_AUTH_STATUS = 0
HTTP_AUTH_STATUS_HttpAuthStatusNotAuthenticated: HTTP_AUTH_STATUS = 1
HTTP_AUTH_STATUS_HttpAuthStatusFailure: HTTP_AUTH_STATUS = 2
class HTTP_BANDWIDTH_LIMIT_INFO(Structure):
    Flags: Windows.Win32.Networking.HttpServer.HTTP_PROPERTY_FLAGS
    MaxBandwidth: UInt32
class HTTP_BINDING_INFO(Structure):
    Flags: Windows.Win32.Networking.HttpServer.HTTP_PROPERTY_FLAGS
    RequestQueueHandle: Windows.Win32.Foundation.HANDLE
class HTTP_BYTE_RANGE(Structure):
    StartingOffset: Windows.Win32.Foundation.ULARGE_INTEGER
    Length: Windows.Win32.Foundation.ULARGE_INTEGER
class HTTP_CACHE_POLICY(Structure):
    Policy: Windows.Win32.Networking.HttpServer.HTTP_CACHE_POLICY_TYPE
    SecondsToLive: UInt32
HTTP_CACHE_POLICY_TYPE = Int32
HTTP_CACHE_POLICY_TYPE_HttpCachePolicyNocache: HTTP_CACHE_POLICY_TYPE = 0
HTTP_CACHE_POLICY_TYPE_HttpCachePolicyUserInvalidates: HTTP_CACHE_POLICY_TYPE = 1
HTTP_CACHE_POLICY_TYPE_HttpCachePolicyTimeToLive: HTTP_CACHE_POLICY_TYPE = 2
HTTP_CACHE_POLICY_TYPE_HttpCachePolicyMaximum: HTTP_CACHE_POLICY_TYPE = 3
class HTTP_CHANNEL_BIND_INFO(Structure):
    Hardening: Windows.Win32.Networking.HttpServer.HTTP_AUTHENTICATION_HARDENING_LEVELS
    Flags: UInt32
    ServiceNames: POINTER(POINTER(Windows.Win32.Networking.HttpServer.HTTP_SERVICE_BINDING_BASE_head))
    NumberOfServiceNames: UInt32
class HTTP_CONNECTION_LIMIT_INFO(Structure):
    Flags: Windows.Win32.Networking.HttpServer.HTTP_PROPERTY_FLAGS
    MaxConnections: UInt32
class HTTP_COOKED_URL(Structure):
    FullUrlLength: UInt16
    HostLength: UInt16
    AbsPathLength: UInt16
    QueryStringLength: UInt16
    pFullUrl: Windows.Win32.Foundation.PWSTR
    pHost: Windows.Win32.Foundation.PWSTR
    pAbsPath: Windows.Win32.Foundation.PWSTR
    pQueryString: Windows.Win32.Foundation.PWSTR
HTTP_CREATE_REQUEST_QUEUE_PROPERTY_ID = Int32
HTTP_CREATE_REQUEST_QUEUE_PROPERTY_ID_CreateRequestQueueExternalIdProperty: HTTP_CREATE_REQUEST_QUEUE_PROPERTY_ID = 1
HTTP_CREATE_REQUEST_QUEUE_PROPERTY_ID_CreateRequestQueueMax: HTTP_CREATE_REQUEST_QUEUE_PROPERTY_ID = 2
class HTTP_CREATE_REQUEST_QUEUE_PROPERTY_INFO(Structure):
    PropertyId: Windows.Win32.Networking.HttpServer.HTTP_CREATE_REQUEST_QUEUE_PROPERTY_ID
    PropertyInfoLength: UInt32
    PropertyInfo: c_void_p
class HTTP_DATA_CHUNK(Structure):
    DataChunkType: Windows.Win32.Networking.HttpServer.HTTP_DATA_CHUNK_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        FromMemory: _FromMemory_e__Struct
        FromFileHandle: _FromFileHandle_e__Struct
        FromFragmentCache: _FromFragmentCache_e__Struct
        FromFragmentCacheEx: _FromFragmentCacheEx_e__Struct
        Trailers: _Trailers_e__Struct
        class _FromMemory_e__Struct(Structure):
            pBuffer: c_void_p
            BufferLength: UInt32
        class _FromFileHandle_e__Struct(Structure):
            ByteRange: Windows.Win32.Networking.HttpServer.HTTP_BYTE_RANGE
            FileHandle: Windows.Win32.Foundation.HANDLE
        class _FromFragmentCache_e__Struct(Structure):
            FragmentNameLength: UInt16
            pFragmentName: Windows.Win32.Foundation.PWSTR
        class _FromFragmentCacheEx_e__Struct(Structure):
            ByteRange: Windows.Win32.Networking.HttpServer.HTTP_BYTE_RANGE
            pFragmentName: Windows.Win32.Foundation.PWSTR
        class _Trailers_e__Struct(Structure):
            TrailerCount: UInt16
            pTrailers: POINTER(Windows.Win32.Networking.HttpServer.HTTP_UNKNOWN_HEADER_head)
HTTP_DATA_CHUNK_TYPE = Int32
HTTP_DATA_CHUNK_TYPE_HttpDataChunkFromMemory: HTTP_DATA_CHUNK_TYPE = 0
HTTP_DATA_CHUNK_TYPE_HttpDataChunkFromFileHandle: HTTP_DATA_CHUNK_TYPE = 1
HTTP_DATA_CHUNK_TYPE_HttpDataChunkFromFragmentCache: HTTP_DATA_CHUNK_TYPE = 2
HTTP_DATA_CHUNK_TYPE_HttpDataChunkFromFragmentCacheEx: HTTP_DATA_CHUNK_TYPE = 3
HTTP_DATA_CHUNK_TYPE_HttpDataChunkTrailers: HTTP_DATA_CHUNK_TYPE = 4
HTTP_DATA_CHUNK_TYPE_HttpDataChunkMaximum: HTTP_DATA_CHUNK_TYPE = 5
HTTP_DELEGATE_REQUEST_PROPERTY_ID = Int32
HTTP_DELEGATE_REQUEST_PROPERTY_ID_DelegateRequestReservedProperty: HTTP_DELEGATE_REQUEST_PROPERTY_ID = 0
HTTP_DELEGATE_REQUEST_PROPERTY_ID_DelegateRequestDelegateUrlProperty: HTTP_DELEGATE_REQUEST_PROPERTY_ID = 1
class HTTP_DELEGATE_REQUEST_PROPERTY_INFO(Structure):
    PropertyId: Windows.Win32.Networking.HttpServer.HTTP_DELEGATE_REQUEST_PROPERTY_ID
    PropertyInfoLength: UInt32
    PropertyInfo: c_void_p
HTTP_ENABLED_STATE = Int32
HTTP_ENABLED_STATE_HttpEnabledStateActive: HTTP_ENABLED_STATE = 0
HTTP_ENABLED_STATE_HttpEnabledStateInactive: HTTP_ENABLED_STATE = 1
class HTTP_ERROR_HEADERS_PARAM(Structure):
    StatusCode: UInt16
    HeaderCount: UInt16
    Headers: POINTER(Windows.Win32.Networking.HttpServer.HTTP_UNKNOWN_HEADER_head)
HTTP_FEATURE_ID = Int32
HTTP_FEATURE_ID_HttpFeatureUnknown: HTTP_FEATURE_ID = 0
HTTP_FEATURE_ID_HttpFeatureResponseTrailers: HTTP_FEATURE_ID = 1
HTTP_FEATURE_ID_HttpFeatureApiTimings: HTTP_FEATURE_ID = 2
HTTP_FEATURE_ID_HttpFeatureDelegateEx: HTTP_FEATURE_ID = 3
HTTP_FEATURE_ID_HttpFeatureHttp3: HTTP_FEATURE_ID = 4
HTTP_FEATURE_ID_HttpFeaturemax: HTTP_FEATURE_ID = -1
class HTTP_FLOWRATE_INFO(Structure):
    Flags: Windows.Win32.Networking.HttpServer.HTTP_PROPERTY_FLAGS
    MaxBandwidth: UInt32
    MaxPeakBandwidth: UInt32
    BurstSize: UInt32
HTTP_HEADER_ID = Int32
HTTP_HEADER_ID_HttpHeaderCacheControl: HTTP_HEADER_ID = 0
HTTP_HEADER_ID_HttpHeaderConnection: HTTP_HEADER_ID = 1
HTTP_HEADER_ID_HttpHeaderDate: HTTP_HEADER_ID = 2
HTTP_HEADER_ID_HttpHeaderKeepAlive: HTTP_HEADER_ID = 3
HTTP_HEADER_ID_HttpHeaderPragma: HTTP_HEADER_ID = 4
HTTP_HEADER_ID_HttpHeaderTrailer: HTTP_HEADER_ID = 5
HTTP_HEADER_ID_HttpHeaderTransferEncoding: HTTP_HEADER_ID = 6
HTTP_HEADER_ID_HttpHeaderUpgrade: HTTP_HEADER_ID = 7
HTTP_HEADER_ID_HttpHeaderVia: HTTP_HEADER_ID = 8
HTTP_HEADER_ID_HttpHeaderWarning: HTTP_HEADER_ID = 9
HTTP_HEADER_ID_HttpHeaderAllow: HTTP_HEADER_ID = 10
HTTP_HEADER_ID_HttpHeaderContentLength: HTTP_HEADER_ID = 11
HTTP_HEADER_ID_HttpHeaderContentType: HTTP_HEADER_ID = 12
HTTP_HEADER_ID_HttpHeaderContentEncoding: HTTP_HEADER_ID = 13
HTTP_HEADER_ID_HttpHeaderContentLanguage: HTTP_HEADER_ID = 14
HTTP_HEADER_ID_HttpHeaderContentLocation: HTTP_HEADER_ID = 15
HTTP_HEADER_ID_HttpHeaderContentMd5: HTTP_HEADER_ID = 16
HTTP_HEADER_ID_HttpHeaderContentRange: HTTP_HEADER_ID = 17
HTTP_HEADER_ID_HttpHeaderExpires: HTTP_HEADER_ID = 18
HTTP_HEADER_ID_HttpHeaderLastModified: HTTP_HEADER_ID = 19
HTTP_HEADER_ID_HttpHeaderAccept: HTTP_HEADER_ID = 20
HTTP_HEADER_ID_HttpHeaderAcceptCharset: HTTP_HEADER_ID = 21
HTTP_HEADER_ID_HttpHeaderAcceptEncoding: HTTP_HEADER_ID = 22
HTTP_HEADER_ID_HttpHeaderAcceptLanguage: HTTP_HEADER_ID = 23
HTTP_HEADER_ID_HttpHeaderAuthorization: HTTP_HEADER_ID = 24
HTTP_HEADER_ID_HttpHeaderCookie: HTTP_HEADER_ID = 25
HTTP_HEADER_ID_HttpHeaderExpect: HTTP_HEADER_ID = 26
HTTP_HEADER_ID_HttpHeaderFrom: HTTP_HEADER_ID = 27
HTTP_HEADER_ID_HttpHeaderHost: HTTP_HEADER_ID = 28
HTTP_HEADER_ID_HttpHeaderIfMatch: HTTP_HEADER_ID = 29
HTTP_HEADER_ID_HttpHeaderIfModifiedSince: HTTP_HEADER_ID = 30
HTTP_HEADER_ID_HttpHeaderIfNoneMatch: HTTP_HEADER_ID = 31
HTTP_HEADER_ID_HttpHeaderIfRange: HTTP_HEADER_ID = 32
HTTP_HEADER_ID_HttpHeaderIfUnmodifiedSince: HTTP_HEADER_ID = 33
HTTP_HEADER_ID_HttpHeaderMaxForwards: HTTP_HEADER_ID = 34
HTTP_HEADER_ID_HttpHeaderProxyAuthorization: HTTP_HEADER_ID = 35
HTTP_HEADER_ID_HttpHeaderReferer: HTTP_HEADER_ID = 36
HTTP_HEADER_ID_HttpHeaderRange: HTTP_HEADER_ID = 37
HTTP_HEADER_ID_HttpHeaderTe: HTTP_HEADER_ID = 38
HTTP_HEADER_ID_HttpHeaderTranslate: HTTP_HEADER_ID = 39
HTTP_HEADER_ID_HttpHeaderUserAgent: HTTP_HEADER_ID = 40
HTTP_HEADER_ID_HttpHeaderRequestMaximum: HTTP_HEADER_ID = 41
HTTP_HEADER_ID_HttpHeaderAcceptRanges: HTTP_HEADER_ID = 20
HTTP_HEADER_ID_HttpHeaderAge: HTTP_HEADER_ID = 21
HTTP_HEADER_ID_HttpHeaderEtag: HTTP_HEADER_ID = 22
HTTP_HEADER_ID_HttpHeaderLocation: HTTP_HEADER_ID = 23
HTTP_HEADER_ID_HttpHeaderProxyAuthenticate: HTTP_HEADER_ID = 24
HTTP_HEADER_ID_HttpHeaderRetryAfter: HTTP_HEADER_ID = 25
HTTP_HEADER_ID_HttpHeaderServer: HTTP_HEADER_ID = 26
HTTP_HEADER_ID_HttpHeaderSetCookie: HTTP_HEADER_ID = 27
HTTP_HEADER_ID_HttpHeaderVary: HTTP_HEADER_ID = 28
HTTP_HEADER_ID_HttpHeaderWwwAuthenticate: HTTP_HEADER_ID = 29
HTTP_HEADER_ID_HttpHeaderResponseMaximum: HTTP_HEADER_ID = 30
HTTP_HEADER_ID_HttpHeaderMaximum: HTTP_HEADER_ID = 41
HTTP_INITIALIZE = UInt32
HTTP_INITIALIZE_CONFIG: HTTP_INITIALIZE = 2
HTTP_INITIALIZE_SERVER: HTTP_INITIALIZE = 1
class HTTP_KNOWN_HEADER(Structure):
    RawValueLength: UInt16
    pRawValue: Windows.Win32.Foundation.PSTR
class HTTP_LISTEN_ENDPOINT_INFO(Structure):
    Flags: Windows.Win32.Networking.HttpServer.HTTP_PROPERTY_FLAGS
    EnableSharing: Windows.Win32.Foundation.BOOLEAN
class HTTP_LOGGING_INFO(Structure):
    Flags: Windows.Win32.Networking.HttpServer.HTTP_PROPERTY_FLAGS
    LoggingFlags: UInt32
    SoftwareName: Windows.Win32.Foundation.PWSTR
    SoftwareNameLength: UInt16
    DirectoryNameLength: UInt16
    DirectoryName: Windows.Win32.Foundation.PWSTR
    Format: Windows.Win32.Networking.HttpServer.HTTP_LOGGING_TYPE
    Fields: UInt32
    pExtFields: c_void_p
    NumOfExtFields: UInt16
    MaxRecordSize: UInt16
    RolloverType: Windows.Win32.Networking.HttpServer.HTTP_LOGGING_ROLLOVER_TYPE
    RolloverSize: UInt32
    pSecurityDescriptor: Windows.Win32.Security.PSECURITY_DESCRIPTOR
HTTP_LOGGING_ROLLOVER_TYPE = Int32
HTTP_LOGGING_ROLLOVER_TYPE_HttpLoggingRolloverSize: HTTP_LOGGING_ROLLOVER_TYPE = 0
HTTP_LOGGING_ROLLOVER_TYPE_HttpLoggingRolloverDaily: HTTP_LOGGING_ROLLOVER_TYPE = 1
HTTP_LOGGING_ROLLOVER_TYPE_HttpLoggingRolloverWeekly: HTTP_LOGGING_ROLLOVER_TYPE = 2
HTTP_LOGGING_ROLLOVER_TYPE_HttpLoggingRolloverMonthly: HTTP_LOGGING_ROLLOVER_TYPE = 3
HTTP_LOGGING_ROLLOVER_TYPE_HttpLoggingRolloverHourly: HTTP_LOGGING_ROLLOVER_TYPE = 4
HTTP_LOGGING_TYPE = Int32
HTTP_LOGGING_TYPE_HttpLoggingTypeW3C: HTTP_LOGGING_TYPE = 0
HTTP_LOGGING_TYPE_HttpLoggingTypeIIS: HTTP_LOGGING_TYPE = 1
HTTP_LOGGING_TYPE_HttpLoggingTypeNCSA: HTTP_LOGGING_TYPE = 2
HTTP_LOGGING_TYPE_HttpLoggingTypeRaw: HTTP_LOGGING_TYPE = 3
class HTTP_LOG_DATA(Structure):
    Type: Windows.Win32.Networking.HttpServer.HTTP_LOG_DATA_TYPE
HTTP_LOG_DATA_TYPE = Int32
HTTP_LOG_DATA_TYPE_HttpLogDataTypeFields: HTTP_LOG_DATA_TYPE = 0
class HTTP_LOG_FIELDS_DATA(Structure):
    Base: Windows.Win32.Networking.HttpServer.HTTP_LOG_DATA
    UserNameLength: UInt16
    UriStemLength: UInt16
    ClientIpLength: UInt16
    ServerNameLength: UInt16
    ServiceNameLength: UInt16
    ServerIpLength: UInt16
    MethodLength: UInt16
    UriQueryLength: UInt16
    HostLength: UInt16
    UserAgentLength: UInt16
    CookieLength: UInt16
    ReferrerLength: UInt16
    UserName: Windows.Win32.Foundation.PWSTR
    UriStem: Windows.Win32.Foundation.PWSTR
    ClientIp: Windows.Win32.Foundation.PSTR
    ServerName: Windows.Win32.Foundation.PSTR
    ServiceName: Windows.Win32.Foundation.PSTR
    ServerIp: Windows.Win32.Foundation.PSTR
    Method: Windows.Win32.Foundation.PSTR
    UriQuery: Windows.Win32.Foundation.PSTR
    Host: Windows.Win32.Foundation.PSTR
    UserAgent: Windows.Win32.Foundation.PSTR
    Cookie: Windows.Win32.Foundation.PSTR
    Referrer: Windows.Win32.Foundation.PSTR
    ServerPort: UInt16
    ProtocolStatus: UInt16
    Win32Status: UInt32
    MethodNum: Windows.Win32.Networking.HttpServer.HTTP_VERB
    SubStatus: UInt16
class HTTP_MULTIPLE_KNOWN_HEADERS(Structure):
    HeaderId: Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID
    Flags: UInt32
    KnownHeaderCount: UInt16
    KnownHeaders: POINTER(Windows.Win32.Networking.HttpServer.HTTP_KNOWN_HEADER_head)
class HTTP_PERFORMANCE_PARAM(Structure):
    Type: Windows.Win32.Networking.HttpServer.HTTP_PERFORMANCE_PARAM_TYPE
    BufferSize: UInt32
    Buffer: c_void_p
HTTP_PERFORMANCE_PARAM_TYPE = Int32
HTTP_PERFORMANCE_PARAM_TYPE_PerformanceParamSendBufferingFlags: HTTP_PERFORMANCE_PARAM_TYPE = 0
HTTP_PERFORMANCE_PARAM_TYPE_PerformanceParamAggressiveICW: HTTP_PERFORMANCE_PARAM_TYPE = 1
HTTP_PERFORMANCE_PARAM_TYPE_PerformanceParamMaxSendBufferSize: HTTP_PERFORMANCE_PARAM_TYPE = 2
HTTP_PERFORMANCE_PARAM_TYPE_PerformanceParamMaxConcurrentClientStreams: HTTP_PERFORMANCE_PARAM_TYPE = 3
HTTP_PERFORMANCE_PARAM_TYPE_PerformanceParamMaxReceiveBufferSize: HTTP_PERFORMANCE_PARAM_TYPE = 4
HTTP_PERFORMANCE_PARAM_TYPE_PerformanceParamDecryptOnSspiThread: HTTP_PERFORMANCE_PARAM_TYPE = 5
HTTP_PERFORMANCE_PARAM_TYPE_PerformanceParamMax: HTTP_PERFORMANCE_PARAM_TYPE = 6
class HTTP_PROPERTY_FLAGS(Structure):
    _bitfield: UInt32
class HTTP_PROTECTION_LEVEL_INFO(Structure):
    Flags: Windows.Win32.Networking.HttpServer.HTTP_PROPERTY_FLAGS
    Level: Windows.Win32.Networking.HttpServer.HTTP_PROTECTION_LEVEL_TYPE
HTTP_PROTECTION_LEVEL_TYPE = Int32
HTTP_PROTECTION_LEVEL_TYPE_HttpProtectionLevelUnrestricted: HTTP_PROTECTION_LEVEL_TYPE = 0
HTTP_PROTECTION_LEVEL_TYPE_HttpProtectionLevelEdgeRestricted: HTTP_PROTECTION_LEVEL_TYPE = 1
HTTP_PROTECTION_LEVEL_TYPE_HttpProtectionLevelRestricted: HTTP_PROTECTION_LEVEL_TYPE = 2
class HTTP_QOS_SETTING_INFO(Structure):
    QosType: Windows.Win32.Networking.HttpServer.HTTP_QOS_SETTING_TYPE
    QosSetting: c_void_p
HTTP_QOS_SETTING_TYPE = Int32
HTTP_QOS_SETTING_TYPE_HttpQosSettingTypeBandwidth: HTTP_QOS_SETTING_TYPE = 0
HTTP_QOS_SETTING_TYPE_HttpQosSettingTypeConnectionLimit: HTTP_QOS_SETTING_TYPE = 1
HTTP_QOS_SETTING_TYPE_HttpQosSettingTypeFlowRate: HTTP_QOS_SETTING_TYPE = 2
class HTTP_QUERY_REQUEST_QUALIFIER_QUIC(Structure):
    Freshness: UInt64
class HTTP_QUERY_REQUEST_QUALIFIER_TCP(Structure):
    Freshness: UInt64
class HTTP_QUIC_API_TIMINGS(Structure):
    ConnectionTimings: Windows.Win32.Networking.HttpServer.HTTP_QUIC_CONNECTION_API_TIMINGS
    StreamTimings: Windows.Win32.Networking.HttpServer.HTTP_QUIC_STREAM_API_TIMINGS
class HTTP_QUIC_CONNECTION_API_TIMINGS(Structure):
    OpenTime: UInt64
    CloseTime: UInt64
    StartTime: UInt64
    ShutdownTime: UInt64
    SecConfigCreateTime: UInt64
    SecConfigDeleteTime: UInt64
    GetParamCount: UInt64
    GetParamSum: UInt64
    SetParamCount: UInt64
    SetParamSum: UInt64
    SetCallbackHandlerCount: UInt64
    SetCallbackHandlerSum: UInt64
    ControlStreamTimings: Windows.Win32.Networking.HttpServer.HTTP_QUIC_STREAM_API_TIMINGS
class HTTP_QUIC_STREAM_API_TIMINGS(Structure):
    OpenCount: UInt64
    OpenSum: UInt64
    CloseCount: UInt64
    CloseSum: UInt64
    StartCount: UInt64
    StartSum: UInt64
    ShutdownCount: UInt64
    ShutdownSum: UInt64
    SendCount: UInt64
    SendSum: UInt64
    ReceiveSetEnabledCount: UInt64
    ReceiveSetEnabledSum: UInt64
    GetParamCount: UInt64
    GetParamSum: UInt64
    SetParamCount: UInt64
    SetParamSum: UInt64
    SetCallbackHandlerCount: UInt64
    SetCallbackHandlerSum: UInt64
HTTP_RECEIVE_HTTP_REQUEST_FLAGS = UInt32
HTTP_RECEIVE_REQUEST_FLAG_COPY_BODY: HTTP_RECEIVE_HTTP_REQUEST_FLAGS = 1
HTTP_RECEIVE_REQUEST_FLAG_FLUSH_BODY: HTTP_RECEIVE_HTTP_REQUEST_FLAGS = 2
class HTTP_REQUEST_AUTH_INFO(Structure):
    AuthStatus: Windows.Win32.Networking.HttpServer.HTTP_AUTH_STATUS
    SecStatus: Windows.Win32.Foundation.HRESULT
    Flags: UInt32
    AuthType: Windows.Win32.Networking.HttpServer.HTTP_REQUEST_AUTH_TYPE
    AccessToken: Windows.Win32.Foundation.HANDLE
    ContextAttributes: UInt32
    PackedContextLength: UInt32
    PackedContextType: UInt32
    PackedContext: c_void_p
    MutualAuthDataLength: UInt32
    pMutualAuthData: Windows.Win32.Foundation.PSTR
    PackageNameLength: UInt16
    pPackageName: Windows.Win32.Foundation.PWSTR
HTTP_REQUEST_AUTH_TYPE = Int32
HTTP_REQUEST_AUTH_TYPE_HttpRequestAuthTypeNone: HTTP_REQUEST_AUTH_TYPE = 0
HTTP_REQUEST_AUTH_TYPE_HttpRequestAuthTypeBasic: HTTP_REQUEST_AUTH_TYPE = 1
HTTP_REQUEST_AUTH_TYPE_HttpRequestAuthTypeDigest: HTTP_REQUEST_AUTH_TYPE = 2
HTTP_REQUEST_AUTH_TYPE_HttpRequestAuthTypeNTLM: HTTP_REQUEST_AUTH_TYPE = 3
HTTP_REQUEST_AUTH_TYPE_HttpRequestAuthTypeNegotiate: HTTP_REQUEST_AUTH_TYPE = 4
HTTP_REQUEST_AUTH_TYPE_HttpRequestAuthTypeKerberos: HTTP_REQUEST_AUTH_TYPE = 5
class HTTP_REQUEST_CHANNEL_BIND_STATUS(Structure):
    ServiceName: POINTER(Windows.Win32.Networking.HttpServer.HTTP_SERVICE_BINDING_BASE_head)
    ChannelToken: c_char_p_no
    ChannelTokenSize: UInt32
    Flags: UInt32
class HTTP_REQUEST_HEADERS(Structure):
    UnknownHeaderCount: UInt16
    pUnknownHeaders: POINTER(Windows.Win32.Networking.HttpServer.HTTP_UNKNOWN_HEADER_head)
    TrailerCount: UInt16
    pTrailers: POINTER(Windows.Win32.Networking.HttpServer.HTTP_UNKNOWN_HEADER_head)
    KnownHeaders: Windows.Win32.Networking.HttpServer.HTTP_KNOWN_HEADER * 41
class HTTP_REQUEST_INFO(Structure):
    InfoType: Windows.Win32.Networking.HttpServer.HTTP_REQUEST_INFO_TYPE
    InfoLength: UInt32
    pInfo: c_void_p
HTTP_REQUEST_INFO_TYPE = Int32
HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeAuth: HTTP_REQUEST_INFO_TYPE = 0
HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeChannelBind: HTTP_REQUEST_INFO_TYPE = 1
HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeSslProtocol: HTTP_REQUEST_INFO_TYPE = 2
HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeSslTokenBindingDraft: HTTP_REQUEST_INFO_TYPE = 3
HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeSslTokenBinding: HTTP_REQUEST_INFO_TYPE = 4
HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeRequestTiming: HTTP_REQUEST_INFO_TYPE = 5
HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeTcpInfoV0: HTTP_REQUEST_INFO_TYPE = 6
HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeRequestSizing: HTTP_REQUEST_INFO_TYPE = 7
HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeQuicStats: HTTP_REQUEST_INFO_TYPE = 8
HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeTcpInfoV1: HTTP_REQUEST_INFO_TYPE = 9
HTTP_REQUEST_PROPERTY = Int32
HTTP_REQUEST_PROPERTY_HttpRequestPropertyIsb: HTTP_REQUEST_PROPERTY = 0
HTTP_REQUEST_PROPERTY_HttpRequestPropertyTcpInfoV0: HTTP_REQUEST_PROPERTY = 1
HTTP_REQUEST_PROPERTY_HttpRequestPropertyQuicStats: HTTP_REQUEST_PROPERTY = 2
HTTP_REQUEST_PROPERTY_HttpRequestPropertyTcpInfoV1: HTTP_REQUEST_PROPERTY = 3
HTTP_REQUEST_PROPERTY_HttpRequestPropertySni: HTTP_REQUEST_PROPERTY = 4
HTTP_REQUEST_PROPERTY_HttpRequestPropertyStreamError: HTTP_REQUEST_PROPERTY = 5
HTTP_REQUEST_PROPERTY_HttpRequestPropertyWskApiTimings: HTTP_REQUEST_PROPERTY = 6
HTTP_REQUEST_PROPERTY_HttpRequestPropertyQuicApiTimings: HTTP_REQUEST_PROPERTY = 7
class HTTP_REQUEST_PROPERTY_SNI(Structure):
    Hostname: Char * 256
    Flags: UInt32
class HTTP_REQUEST_PROPERTY_STREAM_ERROR(Structure):
    ErrorCode: UInt32
class HTTP_REQUEST_SIZING_INFO(Structure):
    Flags: UInt64
    RequestIndex: UInt32
    RequestSizingCount: UInt32
    RequestSizing: UInt64 * 5
HTTP_REQUEST_SIZING_TYPE = Int32
HTTP_REQUEST_SIZING_TYPE_HttpRequestSizingTypeTlsHandshakeLeg1ClientData: HTTP_REQUEST_SIZING_TYPE = 0
HTTP_REQUEST_SIZING_TYPE_HttpRequestSizingTypeTlsHandshakeLeg1ServerData: HTTP_REQUEST_SIZING_TYPE = 1
HTTP_REQUEST_SIZING_TYPE_HttpRequestSizingTypeTlsHandshakeLeg2ClientData: HTTP_REQUEST_SIZING_TYPE = 2
HTTP_REQUEST_SIZING_TYPE_HttpRequestSizingTypeTlsHandshakeLeg2ServerData: HTTP_REQUEST_SIZING_TYPE = 3
HTTP_REQUEST_SIZING_TYPE_HttpRequestSizingTypeHeaders: HTTP_REQUEST_SIZING_TYPE = 4
HTTP_REQUEST_SIZING_TYPE_HttpRequestSizingTypeMax: HTTP_REQUEST_SIZING_TYPE = 5
class HTTP_REQUEST_TIMING_INFO(Structure):
    RequestTimingCount: UInt32
    RequestTiming: UInt64 * 30
HTTP_REQUEST_TIMING_TYPE = Int32
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeConnectionStart: HTTP_REQUEST_TIMING_TYPE = 0
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeDataStart: HTTP_REQUEST_TIMING_TYPE = 1
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsCertificateLoadStart: HTTP_REQUEST_TIMING_TYPE = 2
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsCertificateLoadEnd: HTTP_REQUEST_TIMING_TYPE = 3
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsHandshakeLeg1Start: HTTP_REQUEST_TIMING_TYPE = 4
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsHandshakeLeg1End: HTTP_REQUEST_TIMING_TYPE = 5
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsHandshakeLeg2Start: HTTP_REQUEST_TIMING_TYPE = 6
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsHandshakeLeg2End: HTTP_REQUEST_TIMING_TYPE = 7
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsAttributesQueryStart: HTTP_REQUEST_TIMING_TYPE = 8
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsAttributesQueryEnd: HTTP_REQUEST_TIMING_TYPE = 9
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsClientCertQueryStart: HTTP_REQUEST_TIMING_TYPE = 10
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsClientCertQueryEnd: HTTP_REQUEST_TIMING_TYPE = 11
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeHttp2StreamStart: HTTP_REQUEST_TIMING_TYPE = 12
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeHttp2HeaderDecodeStart: HTTP_REQUEST_TIMING_TYPE = 13
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeHttp2HeaderDecodeEnd: HTTP_REQUEST_TIMING_TYPE = 14
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestHeaderParseStart: HTTP_REQUEST_TIMING_TYPE = 15
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestHeaderParseEnd: HTTP_REQUEST_TIMING_TYPE = 16
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestRoutingStart: HTTP_REQUEST_TIMING_TYPE = 17
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestRoutingEnd: HTTP_REQUEST_TIMING_TYPE = 18
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestQueuedForInspection: HTTP_REQUEST_TIMING_TYPE = 19
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestDeliveredForInspection: HTTP_REQUEST_TIMING_TYPE = 20
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestReturnedAfterInspection: HTTP_REQUEST_TIMING_TYPE = 21
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestQueuedForDelegation: HTTP_REQUEST_TIMING_TYPE = 22
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestDeliveredForDelegation: HTTP_REQUEST_TIMING_TYPE = 23
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestReturnedAfterDelegation: HTTP_REQUEST_TIMING_TYPE = 24
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestQueuedForIO: HTTP_REQUEST_TIMING_TYPE = 25
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestDeliveredForIO: HTTP_REQUEST_TIMING_TYPE = 26
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeHttp3StreamStart: HTTP_REQUEST_TIMING_TYPE = 27
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeHttp3HeaderDecodeStart: HTTP_REQUEST_TIMING_TYPE = 28
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeHttp3HeaderDecodeEnd: HTTP_REQUEST_TIMING_TYPE = 29
HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeMax: HTTP_REQUEST_TIMING_TYPE = 30
class HTTP_REQUEST_TOKEN_BINDING_INFO(Structure):
    TokenBinding: c_char_p_no
    TokenBindingSize: UInt32
    EKM: c_char_p_no
    EKMSize: UInt32
    KeyType: Byte
class HTTP_REQUEST_V1(Structure):
    Flags: UInt32
    ConnectionId: UInt64
    RequestId: UInt64
    UrlContext: UInt64
    Version: Windows.Win32.Networking.HttpServer.HTTP_VERSION
    Verb: Windows.Win32.Networking.HttpServer.HTTP_VERB
    UnknownVerbLength: UInt16
    RawUrlLength: UInt16
    pUnknownVerb: Windows.Win32.Foundation.PSTR
    pRawUrl: Windows.Win32.Foundation.PSTR
    CookedUrl: Windows.Win32.Networking.HttpServer.HTTP_COOKED_URL
    Address: Windows.Win32.Networking.HttpServer.HTTP_TRANSPORT_ADDRESS
    Headers: Windows.Win32.Networking.HttpServer.HTTP_REQUEST_HEADERS
    BytesReceived: UInt64
    EntityChunkCount: UInt16
    pEntityChunks: POINTER(Windows.Win32.Networking.HttpServer.HTTP_DATA_CHUNK_head)
    RawConnectionId: UInt64
    pSslInfo: POINTER(Windows.Win32.Networking.HttpServer.HTTP_SSL_INFO_head)
class HTTP_REQUEST_V2(Structure):
    Base: Windows.Win32.Networking.HttpServer.HTTP_REQUEST_V1
    RequestInfoCount: UInt16
    pRequestInfo: POINTER(Windows.Win32.Networking.HttpServer.HTTP_REQUEST_INFO_head)
class HTTP_RESPONSE_HEADERS(Structure):
    UnknownHeaderCount: UInt16
    pUnknownHeaders: POINTER(Windows.Win32.Networking.HttpServer.HTTP_UNKNOWN_HEADER_head)
    TrailerCount: UInt16
    pTrailers: POINTER(Windows.Win32.Networking.HttpServer.HTTP_UNKNOWN_HEADER_head)
    KnownHeaders: Windows.Win32.Networking.HttpServer.HTTP_KNOWN_HEADER * 30
class HTTP_RESPONSE_INFO(Structure):
    Type: Windows.Win32.Networking.HttpServer.HTTP_RESPONSE_INFO_TYPE
    Length: UInt32
    pInfo: c_void_p
HTTP_RESPONSE_INFO_TYPE = Int32
HTTP_RESPONSE_INFO_TYPE_HttpResponseInfoTypeMultipleKnownHeaders: HTTP_RESPONSE_INFO_TYPE = 0
HTTP_RESPONSE_INFO_TYPE_HttpResponseInfoTypeAuthenticationProperty: HTTP_RESPONSE_INFO_TYPE = 1
HTTP_RESPONSE_INFO_TYPE_HttpResponseInfoTypeQoSProperty: HTTP_RESPONSE_INFO_TYPE = 2
HTTP_RESPONSE_INFO_TYPE_HttpResponseInfoTypeChannelBind: HTTP_RESPONSE_INFO_TYPE = 3
class HTTP_RESPONSE_V1(Structure):
    Flags: UInt32
    Version: Windows.Win32.Networking.HttpServer.HTTP_VERSION
    StatusCode: UInt16
    ReasonLength: UInt16
    pReason: Windows.Win32.Foundation.PSTR
    Headers: Windows.Win32.Networking.HttpServer.HTTP_RESPONSE_HEADERS
    EntityChunkCount: UInt16
    pEntityChunks: POINTER(Windows.Win32.Networking.HttpServer.HTTP_DATA_CHUNK_head)
class HTTP_RESPONSE_V2(Structure):
    Base: Windows.Win32.Networking.HttpServer.HTTP_RESPONSE_V1
    ResponseInfoCount: UInt16
    pResponseInfo: POINTER(Windows.Win32.Networking.HttpServer.HTTP_RESPONSE_INFO_head)
HTTP_SCHEME = Int32
HTTP_SCHEME_HttpSchemeHttp: HTTP_SCHEME = 0
HTTP_SCHEME_HttpSchemeHttps: HTTP_SCHEME = 1
HTTP_SCHEME_HttpSchemeMaximum: HTTP_SCHEME = 2
class HTTP_SERVER_AUTHENTICATION_BASIC_PARAMS(Structure):
    RealmLength: UInt16
    Realm: Windows.Win32.Foundation.PWSTR
class HTTP_SERVER_AUTHENTICATION_DIGEST_PARAMS(Structure):
    DomainNameLength: UInt16
    DomainName: Windows.Win32.Foundation.PWSTR
    RealmLength: UInt16
    Realm: Windows.Win32.Foundation.PWSTR
class HTTP_SERVER_AUTHENTICATION_INFO(Structure):
    Flags: Windows.Win32.Networking.HttpServer.HTTP_PROPERTY_FLAGS
    AuthSchemes: UInt32
    ReceiveMutualAuth: Windows.Win32.Foundation.BOOLEAN
    ReceiveContextHandle: Windows.Win32.Foundation.BOOLEAN
    DisableNTLMCredentialCaching: Windows.Win32.Foundation.BOOLEAN
    ExFlags: Byte
    DigestParams: Windows.Win32.Networking.HttpServer.HTTP_SERVER_AUTHENTICATION_DIGEST_PARAMS
    BasicParams: Windows.Win32.Networking.HttpServer.HTTP_SERVER_AUTHENTICATION_BASIC_PARAMS
HTTP_SERVER_PROPERTY = Int32
HTTP_SERVER_PROPERTY_HttpServerAuthenticationProperty: HTTP_SERVER_PROPERTY = 0
HTTP_SERVER_PROPERTY_HttpServerLoggingProperty: HTTP_SERVER_PROPERTY = 1
HTTP_SERVER_PROPERTY_HttpServerQosProperty: HTTP_SERVER_PROPERTY = 2
HTTP_SERVER_PROPERTY_HttpServerTimeoutsProperty: HTTP_SERVER_PROPERTY = 3
HTTP_SERVER_PROPERTY_HttpServerQueueLengthProperty: HTTP_SERVER_PROPERTY = 4
HTTP_SERVER_PROPERTY_HttpServerStateProperty: HTTP_SERVER_PROPERTY = 5
HTTP_SERVER_PROPERTY_HttpServer503VerbosityProperty: HTTP_SERVER_PROPERTY = 6
HTTP_SERVER_PROPERTY_HttpServerBindingProperty: HTTP_SERVER_PROPERTY = 7
HTTP_SERVER_PROPERTY_HttpServerExtendedAuthenticationProperty: HTTP_SERVER_PROPERTY = 8
HTTP_SERVER_PROPERTY_HttpServerListenEndpointProperty: HTTP_SERVER_PROPERTY = 9
HTTP_SERVER_PROPERTY_HttpServerChannelBindProperty: HTTP_SERVER_PROPERTY = 10
HTTP_SERVER_PROPERTY_HttpServerProtectionLevelProperty: HTTP_SERVER_PROPERTY = 11
HTTP_SERVER_PROPERTY_HttpServerDelegationProperty: HTTP_SERVER_PROPERTY = 16
class HTTP_SERVICE_BINDING_A(Structure):
    Base: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_BINDING_BASE
    Buffer: Windows.Win32.Foundation.PSTR
    BufferSize: UInt32
class HTTP_SERVICE_BINDING_BASE(Structure):
    Type: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_BINDING_TYPE
HTTP_SERVICE_BINDING_TYPE = Int32
HTTP_SERVICE_BINDING_TYPE_HttpServiceBindingTypeNone: HTTP_SERVICE_BINDING_TYPE = 0
HTTP_SERVICE_BINDING_TYPE_HttpServiceBindingTypeW: HTTP_SERVICE_BINDING_TYPE = 1
HTTP_SERVICE_BINDING_TYPE_HttpServiceBindingTypeA: HTTP_SERVICE_BINDING_TYPE = 2
class HTTP_SERVICE_BINDING_W(Structure):
    Base: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_BINDING_BASE
    Buffer: Windows.Win32.Foundation.PWSTR
    BufferSize: UInt32
HTTP_SERVICE_CONFIG_CACHE_KEY = Int32
HTTP_SERVICE_CONFIG_CACHE_KEY_MaxCacheResponseSize: HTTP_SERVICE_CONFIG_CACHE_KEY = 0
HTTP_SERVICE_CONFIG_CACHE_KEY_CacheRangeChunkSize: HTTP_SERVICE_CONFIG_CACHE_KEY = 1
class HTTP_SERVICE_CONFIG_CACHE_SET(Structure):
    KeyDesc: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_CACHE_KEY
    ParamDesc: UInt32
HTTP_SERVICE_CONFIG_ID = Int32
HTTP_SERVICE_CONFIG_ID_HttpServiceConfigIPListenList: HTTP_SERVICE_CONFIG_ID = 0
HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSSLCertInfo: HTTP_SERVICE_CONFIG_ID = 1
HTTP_SERVICE_CONFIG_ID_HttpServiceConfigUrlAclInfo: HTTP_SERVICE_CONFIG_ID = 2
HTTP_SERVICE_CONFIG_ID_HttpServiceConfigTimeout: HTTP_SERVICE_CONFIG_ID = 3
HTTP_SERVICE_CONFIG_ID_HttpServiceConfigCache: HTTP_SERVICE_CONFIG_ID = 4
HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSslSniCertInfo: HTTP_SERVICE_CONFIG_ID = 5
HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSslCcsCertInfo: HTTP_SERVICE_CONFIG_ID = 6
HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSetting: HTTP_SERVICE_CONFIG_ID = 7
HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSslCertInfoEx: HTTP_SERVICE_CONFIG_ID = 8
HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSslSniCertInfoEx: HTTP_SERVICE_CONFIG_ID = 9
HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSslCcsCertInfoEx: HTTP_SERVICE_CONFIG_ID = 10
HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSslScopedCcsCertInfo: HTTP_SERVICE_CONFIG_ID = 11
HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSslScopedCcsCertInfoEx: HTTP_SERVICE_CONFIG_ID = 12
HTTP_SERVICE_CONFIG_ID_HttpServiceConfigMax: HTTP_SERVICE_CONFIG_ID = 13
class HTTP_SERVICE_CONFIG_IP_LISTEN_PARAM(Structure):
    AddrLength: UInt16
    pAddress: POINTER(Windows.Win32.Networking.WinSock.SOCKADDR_head)
class HTTP_SERVICE_CONFIG_IP_LISTEN_QUERY(Structure):
    AddrCount: UInt32
    AddrList: Windows.Win32.Networking.WinSock.SOCKADDR_STORAGE * 1
HTTP_SERVICE_CONFIG_QUERY_TYPE = Int32
HTTP_SERVICE_CONFIG_QUERY_TYPE_HttpServiceConfigQueryExact: HTTP_SERVICE_CONFIG_QUERY_TYPE = 0
HTTP_SERVICE_CONFIG_QUERY_TYPE_HttpServiceConfigQueryNext: HTTP_SERVICE_CONFIG_QUERY_TYPE = 1
HTTP_SERVICE_CONFIG_QUERY_TYPE_HttpServiceConfigQueryMax: HTTP_SERVICE_CONFIG_QUERY_TYPE = 2
HTTP_SERVICE_CONFIG_SETTING_KEY = Int32
HTTP_SERVICE_CONFIG_SETTING_KEY_HttpNone: HTTP_SERVICE_CONFIG_SETTING_KEY = 0
HTTP_SERVICE_CONFIG_SETTING_KEY_HttpTlsThrottle: HTTP_SERVICE_CONFIG_SETTING_KEY = 1
class HTTP_SERVICE_CONFIG_SETTING_SET(Structure):
    KeyDesc: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SETTING_KEY
    ParamDesc: UInt32
class HTTP_SERVICE_CONFIG_SSL_CCS_KEY(Structure):
    LocalAddress: Windows.Win32.Networking.WinSock.SOCKADDR_STORAGE
class HTTP_SERVICE_CONFIG_SSL_CCS_QUERY(Structure):
    QueryDesc: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_QUERY_TYPE
    KeyDesc: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_CCS_KEY
    dwToken: UInt32
class HTTP_SERVICE_CONFIG_SSL_CCS_QUERY_EX(Structure):
    QueryDesc: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_QUERY_TYPE
    KeyDesc: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_CCS_KEY
    dwToken: UInt32
    ParamType: Windows.Win32.Networking.HttpServer.HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE
class HTTP_SERVICE_CONFIG_SSL_CCS_SET(Structure):
    KeyDesc: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_CCS_KEY
    ParamDesc: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_PARAM
class HTTP_SERVICE_CONFIG_SSL_CCS_SET_EX(Structure):
    KeyDesc: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_CCS_KEY
    ParamDesc: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_PARAM_EX
class HTTP_SERVICE_CONFIG_SSL_KEY(Structure):
    pIpPort: POINTER(Windows.Win32.Networking.WinSock.SOCKADDR_head)
class HTTP_SERVICE_CONFIG_SSL_KEY_EX(Structure):
    IpPort: Windows.Win32.Networking.WinSock.SOCKADDR_STORAGE
class HTTP_SERVICE_CONFIG_SSL_PARAM(Structure):
    SslHashLength: UInt32
    pSslHash: c_void_p
    AppId: Guid
    pSslCertStoreName: Windows.Win32.Foundation.PWSTR
    DefaultCertCheckMode: UInt32
    DefaultRevocationFreshnessTime: UInt32
    DefaultRevocationUrlRetrievalTimeout: UInt32
    pDefaultSslCtlIdentifier: Windows.Win32.Foundation.PWSTR
    pDefaultSslCtlStoreName: Windows.Win32.Foundation.PWSTR
    DefaultFlags: UInt32
class HTTP_SERVICE_CONFIG_SSL_PARAM_EX(Structure):
    ParamType: Windows.Win32.Networking.HttpServer.HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE
    Flags: UInt64
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Http2WindowSizeParam: Windows.Win32.Networking.HttpServer.HTTP2_WINDOW_SIZE_PARAM
        Http2SettingsLimitsParam: Windows.Win32.Networking.HttpServer.HTTP2_SETTINGS_LIMITS_PARAM
        HttpPerformanceParam: Windows.Win32.Networking.HttpServer.HTTP_PERFORMANCE_PARAM
        HttpTlsRestrictionsParam: Windows.Win32.Networking.HttpServer.HTTP_TLS_RESTRICTIONS_PARAM
        HttpErrorHeadersParam: Windows.Win32.Networking.HttpServer.HTTP_ERROR_HEADERS_PARAM
        HttpTlsSessionTicketKeysParam: Windows.Win32.Networking.HttpServer.HTTP_TLS_SESSION_TICKET_KEYS_PARAM
class HTTP_SERVICE_CONFIG_SSL_QUERY(Structure):
    QueryDesc: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_QUERY_TYPE
    KeyDesc: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_KEY
    dwToken: UInt32
class HTTP_SERVICE_CONFIG_SSL_QUERY_EX(Structure):
    QueryDesc: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_QUERY_TYPE
    KeyDesc: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_KEY_EX
    dwToken: UInt32
    ParamType: Windows.Win32.Networking.HttpServer.HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE
class HTTP_SERVICE_CONFIG_SSL_SET(Structure):
    KeyDesc: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_KEY
    ParamDesc: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_PARAM
class HTTP_SERVICE_CONFIG_SSL_SET_EX(Structure):
    KeyDesc: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_KEY_EX
    ParamDesc: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_PARAM_EX
class HTTP_SERVICE_CONFIG_SSL_SNI_KEY(Structure):
    IpPort: Windows.Win32.Networking.WinSock.SOCKADDR_STORAGE
    Host: Windows.Win32.Foundation.PWSTR
class HTTP_SERVICE_CONFIG_SSL_SNI_QUERY(Structure):
    QueryDesc: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_QUERY_TYPE
    KeyDesc: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_SNI_KEY
    dwToken: UInt32
class HTTP_SERVICE_CONFIG_SSL_SNI_QUERY_EX(Structure):
    QueryDesc: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_QUERY_TYPE
    KeyDesc: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_SNI_KEY
    dwToken: UInt32
    ParamType: Windows.Win32.Networking.HttpServer.HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE
class HTTP_SERVICE_CONFIG_SSL_SNI_SET(Structure):
    KeyDesc: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_SNI_KEY
    ParamDesc: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_PARAM
class HTTP_SERVICE_CONFIG_SSL_SNI_SET_EX(Structure):
    KeyDesc: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_SNI_KEY
    ParamDesc: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_PARAM_EX
HTTP_SERVICE_CONFIG_TIMEOUT_KEY = Int32
HTTP_SERVICE_CONFIG_TIMEOUT_KEY_IdleConnectionTimeout: HTTP_SERVICE_CONFIG_TIMEOUT_KEY = 0
HTTP_SERVICE_CONFIG_TIMEOUT_KEY_HeaderWaitTimeout: HTTP_SERVICE_CONFIG_TIMEOUT_KEY = 1
class HTTP_SERVICE_CONFIG_TIMEOUT_SET(Structure):
    KeyDesc: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_TIMEOUT_KEY
    ParamDesc: UInt16
class HTTP_SERVICE_CONFIG_URLACL_KEY(Structure):
    pUrlPrefix: Windows.Win32.Foundation.PWSTR
class HTTP_SERVICE_CONFIG_URLACL_PARAM(Structure):
    pStringSecurityDescriptor: Windows.Win32.Foundation.PWSTR
class HTTP_SERVICE_CONFIG_URLACL_QUERY(Structure):
    QueryDesc: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_QUERY_TYPE
    KeyDesc: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_URLACL_KEY
    dwToken: UInt32
class HTTP_SERVICE_CONFIG_URLACL_SET(Structure):
    KeyDesc: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_URLACL_KEY
    ParamDesc: Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_URLACL_PARAM
class HTTP_SSL_CLIENT_CERT_INFO(Structure):
    CertFlags: UInt32
    CertEncodedSize: UInt32
    pCertEncoded: c_char_p_no
    Token: Windows.Win32.Foundation.HANDLE
    CertDeniedByMapper: Windows.Win32.Foundation.BOOLEAN
class HTTP_SSL_INFO(Structure):
    ServerCertKeySize: UInt16
    ConnectionKeySize: UInt16
    ServerCertIssuerSize: UInt32
    ServerCertSubjectSize: UInt32
    pServerCertIssuer: Windows.Win32.Foundation.PSTR
    pServerCertSubject: Windows.Win32.Foundation.PSTR
    pClientCertInfo: POINTER(Windows.Win32.Networking.HttpServer.HTTP_SSL_CLIENT_CERT_INFO_head)
    SslClientCertNegotiated: UInt32
class HTTP_SSL_PROTOCOL_INFO(Structure):
    Protocol: UInt32
    CipherType: UInt32
    CipherStrength: UInt32
    HashType: UInt32
    HashStrength: UInt32
    KeyExchangeType: UInt32
    KeyExchangeStrength: UInt32
HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE = Int32
HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE_ExParamTypeHttp2Window: HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE = 0
HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE_ExParamTypeHttp2SettingsLimits: HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE = 1
HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE_ExParamTypeHttpPerformance: HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE = 2
HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE_ExParamTypeTlsRestrictions: HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE = 3
HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE_ExParamTypeErrorHeaders: HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE = 4
HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE_ExParamTypeTlsSessionTicketKeys: HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE = 5
HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE_ExParamTypeMax: HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE = 6
class HTTP_STATE_INFO(Structure):
    Flags: Windows.Win32.Networking.HttpServer.HTTP_PROPERTY_FLAGS
    State: Windows.Win32.Networking.HttpServer.HTTP_ENABLED_STATE
class HTTP_TIMEOUT_LIMIT_INFO(Structure):
    Flags: Windows.Win32.Networking.HttpServer.HTTP_PROPERTY_FLAGS
    EntityBody: UInt16
    DrainEntityBody: UInt16
    RequestQueue: UInt16
    IdleConnection: UInt16
    HeaderWait: UInt16
    MinSendRate: UInt32
class HTTP_TLS_RESTRICTIONS_PARAM(Structure):
    RestrictionCount: UInt32
    TlsRestrictions: c_void_p
class HTTP_TLS_SESSION_TICKET_KEYS_PARAM(Structure):
    SessionTicketKeyCount: UInt32
    SessionTicketKeys: c_void_p
class HTTP_TRANSPORT_ADDRESS(Structure):
    pRemoteAddress: POINTER(Windows.Win32.Networking.WinSock.SOCKADDR_head)
    pLocalAddress: POINTER(Windows.Win32.Networking.WinSock.SOCKADDR_head)
class HTTP_UNKNOWN_HEADER(Structure):
    NameLength: UInt16
    RawValueLength: UInt16
    pName: Windows.Win32.Foundation.PSTR
    pRawValue: Windows.Win32.Foundation.PSTR
HTTP_VERB = Int32
HTTP_VERB_HttpVerbUnparsed: HTTP_VERB = 0
HTTP_VERB_HttpVerbUnknown: HTTP_VERB = 1
HTTP_VERB_HttpVerbInvalid: HTTP_VERB = 2
HTTP_VERB_HttpVerbOPTIONS: HTTP_VERB = 3
HTTP_VERB_HttpVerbGET: HTTP_VERB = 4
HTTP_VERB_HttpVerbHEAD: HTTP_VERB = 5
HTTP_VERB_HttpVerbPOST: HTTP_VERB = 6
HTTP_VERB_HttpVerbPUT: HTTP_VERB = 7
HTTP_VERB_HttpVerbDELETE: HTTP_VERB = 8
HTTP_VERB_HttpVerbTRACE: HTTP_VERB = 9
HTTP_VERB_HttpVerbCONNECT: HTTP_VERB = 10
HTTP_VERB_HttpVerbTRACK: HTTP_VERB = 11
HTTP_VERB_HttpVerbMOVE: HTTP_VERB = 12
HTTP_VERB_HttpVerbCOPY: HTTP_VERB = 13
HTTP_VERB_HttpVerbPROPFIND: HTTP_VERB = 14
HTTP_VERB_HttpVerbPROPPATCH: HTTP_VERB = 15
HTTP_VERB_HttpVerbMKCOL: HTTP_VERB = 16
HTTP_VERB_HttpVerbLOCK: HTTP_VERB = 17
HTTP_VERB_HttpVerbUNLOCK: HTTP_VERB = 18
HTTP_VERB_HttpVerbSEARCH: HTTP_VERB = 19
HTTP_VERB_HttpVerbMaximum: HTTP_VERB = 20
class HTTP_VERSION(Structure):
    MajorVersion: UInt16
    MinorVersion: UInt16
class HTTP_WSK_API_TIMINGS(Structure):
    ConnectCount: UInt64
    ConnectSum: UInt64
    DisconnectCount: UInt64
    DisconnectSum: UInt64
    SendCount: UInt64
    SendSum: UInt64
    ReceiveCount: UInt64
    ReceiveSum: UInt64
    ReleaseCount: UInt64
    ReleaseSum: UInt64
    ControlSocketCount: UInt64
    ControlSocketSum: UInt64
make_head(_module, 'HTTP2_SETTINGS_LIMITS_PARAM')
make_head(_module, 'HTTP2_WINDOW_SIZE_PARAM')
make_head(_module, 'HTTPAPI_VERSION')
make_head(_module, 'HTTP_BANDWIDTH_LIMIT_INFO')
make_head(_module, 'HTTP_BINDING_INFO')
make_head(_module, 'HTTP_BYTE_RANGE')
make_head(_module, 'HTTP_CACHE_POLICY')
make_head(_module, 'HTTP_CHANNEL_BIND_INFO')
make_head(_module, 'HTTP_CONNECTION_LIMIT_INFO')
make_head(_module, 'HTTP_COOKED_URL')
make_head(_module, 'HTTP_CREATE_REQUEST_QUEUE_PROPERTY_INFO')
make_head(_module, 'HTTP_DATA_CHUNK')
make_head(_module, 'HTTP_DELEGATE_REQUEST_PROPERTY_INFO')
make_head(_module, 'HTTP_ERROR_HEADERS_PARAM')
make_head(_module, 'HTTP_FLOWRATE_INFO')
make_head(_module, 'HTTP_KNOWN_HEADER')
make_head(_module, 'HTTP_LISTEN_ENDPOINT_INFO')
make_head(_module, 'HTTP_LOGGING_INFO')
make_head(_module, 'HTTP_LOG_DATA')
make_head(_module, 'HTTP_LOG_FIELDS_DATA')
make_head(_module, 'HTTP_MULTIPLE_KNOWN_HEADERS')
make_head(_module, 'HTTP_PERFORMANCE_PARAM')
make_head(_module, 'HTTP_PROPERTY_FLAGS')
make_head(_module, 'HTTP_PROTECTION_LEVEL_INFO')
make_head(_module, 'HTTP_QOS_SETTING_INFO')
make_head(_module, 'HTTP_QUERY_REQUEST_QUALIFIER_QUIC')
make_head(_module, 'HTTP_QUERY_REQUEST_QUALIFIER_TCP')
make_head(_module, 'HTTP_QUIC_API_TIMINGS')
make_head(_module, 'HTTP_QUIC_CONNECTION_API_TIMINGS')
make_head(_module, 'HTTP_QUIC_STREAM_API_TIMINGS')
make_head(_module, 'HTTP_REQUEST_AUTH_INFO')
make_head(_module, 'HTTP_REQUEST_CHANNEL_BIND_STATUS')
make_head(_module, 'HTTP_REQUEST_HEADERS')
make_head(_module, 'HTTP_REQUEST_INFO')
make_head(_module, 'HTTP_REQUEST_PROPERTY_SNI')
make_head(_module, 'HTTP_REQUEST_PROPERTY_STREAM_ERROR')
make_head(_module, 'HTTP_REQUEST_SIZING_INFO')
make_head(_module, 'HTTP_REQUEST_TIMING_INFO')
make_head(_module, 'HTTP_REQUEST_TOKEN_BINDING_INFO')
make_head(_module, 'HTTP_REQUEST_V1')
make_head(_module, 'HTTP_REQUEST_V2')
make_head(_module, 'HTTP_RESPONSE_HEADERS')
make_head(_module, 'HTTP_RESPONSE_INFO')
make_head(_module, 'HTTP_RESPONSE_V1')
make_head(_module, 'HTTP_RESPONSE_V2')
make_head(_module, 'HTTP_SERVER_AUTHENTICATION_BASIC_PARAMS')
make_head(_module, 'HTTP_SERVER_AUTHENTICATION_DIGEST_PARAMS')
make_head(_module, 'HTTP_SERVER_AUTHENTICATION_INFO')
make_head(_module, 'HTTP_SERVICE_BINDING_A')
make_head(_module, 'HTTP_SERVICE_BINDING_BASE')
make_head(_module, 'HTTP_SERVICE_BINDING_W')
make_head(_module, 'HTTP_SERVICE_CONFIG_CACHE_SET')
make_head(_module, 'HTTP_SERVICE_CONFIG_IP_LISTEN_PARAM')
make_head(_module, 'HTTP_SERVICE_CONFIG_IP_LISTEN_QUERY')
make_head(_module, 'HTTP_SERVICE_CONFIG_SETTING_SET')
make_head(_module, 'HTTP_SERVICE_CONFIG_SSL_CCS_KEY')
make_head(_module, 'HTTP_SERVICE_CONFIG_SSL_CCS_QUERY')
make_head(_module, 'HTTP_SERVICE_CONFIG_SSL_CCS_QUERY_EX')
make_head(_module, 'HTTP_SERVICE_CONFIG_SSL_CCS_SET')
make_head(_module, 'HTTP_SERVICE_CONFIG_SSL_CCS_SET_EX')
make_head(_module, 'HTTP_SERVICE_CONFIG_SSL_KEY')
make_head(_module, 'HTTP_SERVICE_CONFIG_SSL_KEY_EX')
make_head(_module, 'HTTP_SERVICE_CONFIG_SSL_PARAM')
make_head(_module, 'HTTP_SERVICE_CONFIG_SSL_PARAM_EX')
make_head(_module, 'HTTP_SERVICE_CONFIG_SSL_QUERY')
make_head(_module, 'HTTP_SERVICE_CONFIG_SSL_QUERY_EX')
make_head(_module, 'HTTP_SERVICE_CONFIG_SSL_SET')
make_head(_module, 'HTTP_SERVICE_CONFIG_SSL_SET_EX')
make_head(_module, 'HTTP_SERVICE_CONFIG_SSL_SNI_KEY')
make_head(_module, 'HTTP_SERVICE_CONFIG_SSL_SNI_QUERY')
make_head(_module, 'HTTP_SERVICE_CONFIG_SSL_SNI_QUERY_EX')
make_head(_module, 'HTTP_SERVICE_CONFIG_SSL_SNI_SET')
make_head(_module, 'HTTP_SERVICE_CONFIG_SSL_SNI_SET_EX')
make_head(_module, 'HTTP_SERVICE_CONFIG_TIMEOUT_SET')
make_head(_module, 'HTTP_SERVICE_CONFIG_URLACL_KEY')
make_head(_module, 'HTTP_SERVICE_CONFIG_URLACL_PARAM')
make_head(_module, 'HTTP_SERVICE_CONFIG_URLACL_QUERY')
make_head(_module, 'HTTP_SERVICE_CONFIG_URLACL_SET')
make_head(_module, 'HTTP_SSL_CLIENT_CERT_INFO')
make_head(_module, 'HTTP_SSL_INFO')
make_head(_module, 'HTTP_SSL_PROTOCOL_INFO')
make_head(_module, 'HTTP_STATE_INFO')
make_head(_module, 'HTTP_TIMEOUT_LIMIT_INFO')
make_head(_module, 'HTTP_TLS_RESTRICTIONS_PARAM')
make_head(_module, 'HTTP_TLS_SESSION_TICKET_KEYS_PARAM')
make_head(_module, 'HTTP_TRANSPORT_ADDRESS')
make_head(_module, 'HTTP_UNKNOWN_HEADER')
make_head(_module, 'HTTP_VERSION')
make_head(_module, 'HTTP_WSK_API_TIMINGS')
__all__ = [
    "HTTP2_SETTINGS_LIMITS_PARAM",
    "HTTP2_WINDOW_SIZE_PARAM",
    "HTTPAPI_VERSION",
    "HTTP_503_RESPONSE_VERBOSITY",
    "HTTP_503_RESPONSE_VERBOSITY_Http503ResponseVerbosityBasic",
    "HTTP_503_RESPONSE_VERBOSITY_Http503ResponseVerbosityFull",
    "HTTP_503_RESPONSE_VERBOSITY_Http503ResponseVerbosityLimited",
    "HTTP_AUTHENTICATION_HARDENING_LEVELS",
    "HTTP_AUTHENTICATION_HARDENING_LEVELS_HttpAuthenticationHardeningLegacy",
    "HTTP_AUTHENTICATION_HARDENING_LEVELS_HttpAuthenticationHardeningMedium",
    "HTTP_AUTHENTICATION_HARDENING_LEVELS_HttpAuthenticationHardeningStrict",
    "HTTP_AUTH_ENABLE_BASIC",
    "HTTP_AUTH_ENABLE_DIGEST",
    "HTTP_AUTH_ENABLE_KERBEROS",
    "HTTP_AUTH_ENABLE_NEGOTIATE",
    "HTTP_AUTH_ENABLE_NTLM",
    "HTTP_AUTH_EX_FLAG_CAPTURE_CREDENTIAL",
    "HTTP_AUTH_EX_FLAG_ENABLE_KERBEROS_CREDENTIAL_CACHING",
    "HTTP_AUTH_STATUS",
    "HTTP_AUTH_STATUS_HttpAuthStatusFailure",
    "HTTP_AUTH_STATUS_HttpAuthStatusNotAuthenticated",
    "HTTP_AUTH_STATUS_HttpAuthStatusSuccess",
    "HTTP_BANDWIDTH_LIMIT_INFO",
    "HTTP_BINDING_INFO",
    "HTTP_BYTE_RANGE",
    "HTTP_CACHE_POLICY",
    "HTTP_CACHE_POLICY_TYPE",
    "HTTP_CACHE_POLICY_TYPE_HttpCachePolicyMaximum",
    "HTTP_CACHE_POLICY_TYPE_HttpCachePolicyNocache",
    "HTTP_CACHE_POLICY_TYPE_HttpCachePolicyTimeToLive",
    "HTTP_CACHE_POLICY_TYPE_HttpCachePolicyUserInvalidates",
    "HTTP_CHANNEL_BIND_CLIENT_SERVICE",
    "HTTP_CHANNEL_BIND_DOTLESS_SERVICE",
    "HTTP_CHANNEL_BIND_INFO",
    "HTTP_CHANNEL_BIND_NO_SERVICE_NAME_CHECK",
    "HTTP_CHANNEL_BIND_PROXY",
    "HTTP_CHANNEL_BIND_PROXY_COHOSTING",
    "HTTP_CHANNEL_BIND_SECURE_CHANNEL_TOKEN",
    "HTTP_CONNECTION_LIMIT_INFO",
    "HTTP_COOKED_URL",
    "HTTP_CREATE_REQUEST_QUEUE_FLAG_CONTROLLER",
    "HTTP_CREATE_REQUEST_QUEUE_FLAG_DELEGATION",
    "HTTP_CREATE_REQUEST_QUEUE_FLAG_OPEN_EXISTING",
    "HTTP_CREATE_REQUEST_QUEUE_PROPERTY_ID",
    "HTTP_CREATE_REQUEST_QUEUE_PROPERTY_ID_CreateRequestQueueExternalIdProperty",
    "HTTP_CREATE_REQUEST_QUEUE_PROPERTY_ID_CreateRequestQueueMax",
    "HTTP_CREATE_REQUEST_QUEUE_PROPERTY_INFO",
    "HTTP_DATA_CHUNK",
    "HTTP_DATA_CHUNK_TYPE",
    "HTTP_DATA_CHUNK_TYPE_HttpDataChunkFromFileHandle",
    "HTTP_DATA_CHUNK_TYPE_HttpDataChunkFromFragmentCache",
    "HTTP_DATA_CHUNK_TYPE_HttpDataChunkFromFragmentCacheEx",
    "HTTP_DATA_CHUNK_TYPE_HttpDataChunkFromMemory",
    "HTTP_DATA_CHUNK_TYPE_HttpDataChunkMaximum",
    "HTTP_DATA_CHUNK_TYPE_HttpDataChunkTrailers",
    "HTTP_DELEGATE_REQUEST_PROPERTY_ID",
    "HTTP_DELEGATE_REQUEST_PROPERTY_ID_DelegateRequestDelegateUrlProperty",
    "HTTP_DELEGATE_REQUEST_PROPERTY_ID_DelegateRequestReservedProperty",
    "HTTP_DELEGATE_REQUEST_PROPERTY_INFO",
    "HTTP_DEMAND_CBT",
    "HTTP_ENABLED_STATE",
    "HTTP_ENABLED_STATE_HttpEnabledStateActive",
    "HTTP_ENABLED_STATE_HttpEnabledStateInactive",
    "HTTP_ERROR_HEADERS_PARAM",
    "HTTP_FEATURE_ID",
    "HTTP_FEATURE_ID_HttpFeatureApiTimings",
    "HTTP_FEATURE_ID_HttpFeatureDelegateEx",
    "HTTP_FEATURE_ID_HttpFeatureHttp3",
    "HTTP_FEATURE_ID_HttpFeatureResponseTrailers",
    "HTTP_FEATURE_ID_HttpFeatureUnknown",
    "HTTP_FEATURE_ID_HttpFeaturemax",
    "HTTP_FLOWRATE_INFO",
    "HTTP_FLUSH_RESPONSE_FLAG_RECURSIVE",
    "HTTP_HEADER_ID",
    "HTTP_HEADER_ID_HttpHeaderAccept",
    "HTTP_HEADER_ID_HttpHeaderAcceptCharset",
    "HTTP_HEADER_ID_HttpHeaderAcceptEncoding",
    "HTTP_HEADER_ID_HttpHeaderAcceptLanguage",
    "HTTP_HEADER_ID_HttpHeaderAcceptRanges",
    "HTTP_HEADER_ID_HttpHeaderAge",
    "HTTP_HEADER_ID_HttpHeaderAllow",
    "HTTP_HEADER_ID_HttpHeaderAuthorization",
    "HTTP_HEADER_ID_HttpHeaderCacheControl",
    "HTTP_HEADER_ID_HttpHeaderConnection",
    "HTTP_HEADER_ID_HttpHeaderContentEncoding",
    "HTTP_HEADER_ID_HttpHeaderContentLanguage",
    "HTTP_HEADER_ID_HttpHeaderContentLength",
    "HTTP_HEADER_ID_HttpHeaderContentLocation",
    "HTTP_HEADER_ID_HttpHeaderContentMd5",
    "HTTP_HEADER_ID_HttpHeaderContentRange",
    "HTTP_HEADER_ID_HttpHeaderContentType",
    "HTTP_HEADER_ID_HttpHeaderCookie",
    "HTTP_HEADER_ID_HttpHeaderDate",
    "HTTP_HEADER_ID_HttpHeaderEtag",
    "HTTP_HEADER_ID_HttpHeaderExpect",
    "HTTP_HEADER_ID_HttpHeaderExpires",
    "HTTP_HEADER_ID_HttpHeaderFrom",
    "HTTP_HEADER_ID_HttpHeaderHost",
    "HTTP_HEADER_ID_HttpHeaderIfMatch",
    "HTTP_HEADER_ID_HttpHeaderIfModifiedSince",
    "HTTP_HEADER_ID_HttpHeaderIfNoneMatch",
    "HTTP_HEADER_ID_HttpHeaderIfRange",
    "HTTP_HEADER_ID_HttpHeaderIfUnmodifiedSince",
    "HTTP_HEADER_ID_HttpHeaderKeepAlive",
    "HTTP_HEADER_ID_HttpHeaderLastModified",
    "HTTP_HEADER_ID_HttpHeaderLocation",
    "HTTP_HEADER_ID_HttpHeaderMaxForwards",
    "HTTP_HEADER_ID_HttpHeaderMaximum",
    "HTTP_HEADER_ID_HttpHeaderPragma",
    "HTTP_HEADER_ID_HttpHeaderProxyAuthenticate",
    "HTTP_HEADER_ID_HttpHeaderProxyAuthorization",
    "HTTP_HEADER_ID_HttpHeaderRange",
    "HTTP_HEADER_ID_HttpHeaderReferer",
    "HTTP_HEADER_ID_HttpHeaderRequestMaximum",
    "HTTP_HEADER_ID_HttpHeaderResponseMaximum",
    "HTTP_HEADER_ID_HttpHeaderRetryAfter",
    "HTTP_HEADER_ID_HttpHeaderServer",
    "HTTP_HEADER_ID_HttpHeaderSetCookie",
    "HTTP_HEADER_ID_HttpHeaderTe",
    "HTTP_HEADER_ID_HttpHeaderTrailer",
    "HTTP_HEADER_ID_HttpHeaderTransferEncoding",
    "HTTP_HEADER_ID_HttpHeaderTranslate",
    "HTTP_HEADER_ID_HttpHeaderUpgrade",
    "HTTP_HEADER_ID_HttpHeaderUserAgent",
    "HTTP_HEADER_ID_HttpHeaderVary",
    "HTTP_HEADER_ID_HttpHeaderVia",
    "HTTP_HEADER_ID_HttpHeaderWarning",
    "HTTP_HEADER_ID_HttpHeaderWwwAuthenticate",
    "HTTP_INITIALIZE",
    "HTTP_INITIALIZE_CONFIG",
    "HTTP_INITIALIZE_SERVER",
    "HTTP_KNOWN_HEADER",
    "HTTP_LISTEN_ENDPOINT_INFO",
    "HTTP_LOGGING_FLAG_LOCAL_TIME_ROLLOVER",
    "HTTP_LOGGING_FLAG_LOG_ERRORS_ONLY",
    "HTTP_LOGGING_FLAG_LOG_SUCCESS_ONLY",
    "HTTP_LOGGING_FLAG_USE_UTF8_CONVERSION",
    "HTTP_LOGGING_INFO",
    "HTTP_LOGGING_ROLLOVER_TYPE",
    "HTTP_LOGGING_ROLLOVER_TYPE_HttpLoggingRolloverDaily",
    "HTTP_LOGGING_ROLLOVER_TYPE_HttpLoggingRolloverHourly",
    "HTTP_LOGGING_ROLLOVER_TYPE_HttpLoggingRolloverMonthly",
    "HTTP_LOGGING_ROLLOVER_TYPE_HttpLoggingRolloverSize",
    "HTTP_LOGGING_ROLLOVER_TYPE_HttpLoggingRolloverWeekly",
    "HTTP_LOGGING_TYPE",
    "HTTP_LOGGING_TYPE_HttpLoggingTypeIIS",
    "HTTP_LOGGING_TYPE_HttpLoggingTypeNCSA",
    "HTTP_LOGGING_TYPE_HttpLoggingTypeRaw",
    "HTTP_LOGGING_TYPE_HttpLoggingTypeW3C",
    "HTTP_LOG_DATA",
    "HTTP_LOG_DATA_TYPE",
    "HTTP_LOG_DATA_TYPE_HttpLogDataTypeFields",
    "HTTP_LOG_FIELDS_DATA",
    "HTTP_LOG_FIELD_BYTES_RECV",
    "HTTP_LOG_FIELD_BYTES_SENT",
    "HTTP_LOG_FIELD_CLIENT_IP",
    "HTTP_LOG_FIELD_CLIENT_PORT",
    "HTTP_LOG_FIELD_COMPUTER_NAME",
    "HTTP_LOG_FIELD_COOKIE",
    "HTTP_LOG_FIELD_CORRELATION_ID",
    "HTTP_LOG_FIELD_DATE",
    "HTTP_LOG_FIELD_HOST",
    "HTTP_LOG_FIELD_METHOD",
    "HTTP_LOG_FIELD_QUEUE_NAME",
    "HTTP_LOG_FIELD_REASON",
    "HTTP_LOG_FIELD_REFERER",
    "HTTP_LOG_FIELD_SERVER_IP",
    "HTTP_LOG_FIELD_SERVER_PORT",
    "HTTP_LOG_FIELD_SITE_ID",
    "HTTP_LOG_FIELD_SITE_NAME",
    "HTTP_LOG_FIELD_STATUS",
    "HTTP_LOG_FIELD_STREAM_ID",
    "HTTP_LOG_FIELD_STREAM_ID_EX",
    "HTTP_LOG_FIELD_SUB_STATUS",
    "HTTP_LOG_FIELD_TIME",
    "HTTP_LOG_FIELD_TIME_TAKEN",
    "HTTP_LOG_FIELD_TRANSPORT_TYPE",
    "HTTP_LOG_FIELD_URI",
    "HTTP_LOG_FIELD_URI_QUERY",
    "HTTP_LOG_FIELD_URI_STEM",
    "HTTP_LOG_FIELD_USER_AGENT",
    "HTTP_LOG_FIELD_USER_NAME",
    "HTTP_LOG_FIELD_VERSION",
    "HTTP_LOG_FIELD_WIN32_STATUS",
    "HTTP_MAX_SERVER_QUEUE_LENGTH",
    "HTTP_MIN_SERVER_QUEUE_LENGTH",
    "HTTP_MULTIPLE_KNOWN_HEADERS",
    "HTTP_PERFORMANCE_PARAM",
    "HTTP_PERFORMANCE_PARAM_TYPE",
    "HTTP_PERFORMANCE_PARAM_TYPE_PerformanceParamAggressiveICW",
    "HTTP_PERFORMANCE_PARAM_TYPE_PerformanceParamDecryptOnSspiThread",
    "HTTP_PERFORMANCE_PARAM_TYPE_PerformanceParamMax",
    "HTTP_PERFORMANCE_PARAM_TYPE_PerformanceParamMaxConcurrentClientStreams",
    "HTTP_PERFORMANCE_PARAM_TYPE_PerformanceParamMaxReceiveBufferSize",
    "HTTP_PERFORMANCE_PARAM_TYPE_PerformanceParamMaxSendBufferSize",
    "HTTP_PERFORMANCE_PARAM_TYPE_PerformanceParamSendBufferingFlags",
    "HTTP_PROPERTY_FLAGS",
    "HTTP_PROTECTION_LEVEL_INFO",
    "HTTP_PROTECTION_LEVEL_TYPE",
    "HTTP_PROTECTION_LEVEL_TYPE_HttpProtectionLevelEdgeRestricted",
    "HTTP_PROTECTION_LEVEL_TYPE_HttpProtectionLevelRestricted",
    "HTTP_PROTECTION_LEVEL_TYPE_HttpProtectionLevelUnrestricted",
    "HTTP_QOS_SETTING_INFO",
    "HTTP_QOS_SETTING_TYPE",
    "HTTP_QOS_SETTING_TYPE_HttpQosSettingTypeBandwidth",
    "HTTP_QOS_SETTING_TYPE_HttpQosSettingTypeConnectionLimit",
    "HTTP_QOS_SETTING_TYPE_HttpQosSettingTypeFlowRate",
    "HTTP_QUERY_REQUEST_QUALIFIER_QUIC",
    "HTTP_QUERY_REQUEST_QUALIFIER_TCP",
    "HTTP_QUIC_API_TIMINGS",
    "HTTP_QUIC_CONNECTION_API_TIMINGS",
    "HTTP_QUIC_STREAM_API_TIMINGS",
    "HTTP_RECEIVE_FULL_CHAIN",
    "HTTP_RECEIVE_HTTP_REQUEST_FLAGS",
    "HTTP_RECEIVE_REQUEST_ENTITY_BODY_FLAG_FILL_BUFFER",
    "HTTP_RECEIVE_REQUEST_FLAG_COPY_BODY",
    "HTTP_RECEIVE_REQUEST_FLAG_FLUSH_BODY",
    "HTTP_RECEIVE_SECURE_CHANNEL_TOKEN",
    "HTTP_REQUEST_AUTH_FLAG_TOKEN_FOR_CACHED_CRED",
    "HTTP_REQUEST_AUTH_INFO",
    "HTTP_REQUEST_AUTH_TYPE",
    "HTTP_REQUEST_AUTH_TYPE_HttpRequestAuthTypeBasic",
    "HTTP_REQUEST_AUTH_TYPE_HttpRequestAuthTypeDigest",
    "HTTP_REQUEST_AUTH_TYPE_HttpRequestAuthTypeKerberos",
    "HTTP_REQUEST_AUTH_TYPE_HttpRequestAuthTypeNTLM",
    "HTTP_REQUEST_AUTH_TYPE_HttpRequestAuthTypeNegotiate",
    "HTTP_REQUEST_AUTH_TYPE_HttpRequestAuthTypeNone",
    "HTTP_REQUEST_CHANNEL_BIND_STATUS",
    "HTTP_REQUEST_FLAG_HTTP2",
    "HTTP_REQUEST_FLAG_HTTP3",
    "HTTP_REQUEST_FLAG_IP_ROUTED",
    "HTTP_REQUEST_FLAG_MORE_ENTITY_BODY_EXISTS",
    "HTTP_REQUEST_HEADERS",
    "HTTP_REQUEST_INFO",
    "HTTP_REQUEST_INFO_TYPE",
    "HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeAuth",
    "HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeChannelBind",
    "HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeQuicStats",
    "HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeRequestSizing",
    "HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeRequestTiming",
    "HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeSslProtocol",
    "HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeSslTokenBinding",
    "HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeSslTokenBindingDraft",
    "HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeTcpInfoV0",
    "HTTP_REQUEST_INFO_TYPE_HttpRequestInfoTypeTcpInfoV1",
    "HTTP_REQUEST_PROPERTY",
    "HTTP_REQUEST_PROPERTY_HttpRequestPropertyIsb",
    "HTTP_REQUEST_PROPERTY_HttpRequestPropertyQuicApiTimings",
    "HTTP_REQUEST_PROPERTY_HttpRequestPropertyQuicStats",
    "HTTP_REQUEST_PROPERTY_HttpRequestPropertySni",
    "HTTP_REQUEST_PROPERTY_HttpRequestPropertyStreamError",
    "HTTP_REQUEST_PROPERTY_HttpRequestPropertyTcpInfoV0",
    "HTTP_REQUEST_PROPERTY_HttpRequestPropertyTcpInfoV1",
    "HTTP_REQUEST_PROPERTY_HttpRequestPropertyWskApiTimings",
    "HTTP_REQUEST_PROPERTY_SNI",
    "HTTP_REQUEST_PROPERTY_SNI_FLAG_NO_SNI",
    "HTTP_REQUEST_PROPERTY_SNI_FLAG_SNI_USED",
    "HTTP_REQUEST_PROPERTY_SNI_HOST_MAX_LENGTH",
    "HTTP_REQUEST_PROPERTY_STREAM_ERROR",
    "HTTP_REQUEST_SIZING_INFO",
    "HTTP_REQUEST_SIZING_INFO_FLAG_FIRST_REQUEST",
    "HTTP_REQUEST_SIZING_INFO_FLAG_TCP_FAST_OPEN",
    "HTTP_REQUEST_SIZING_INFO_FLAG_TLS_FALSE_START",
    "HTTP_REQUEST_SIZING_INFO_FLAG_TLS_SESSION_RESUMPTION",
    "HTTP_REQUEST_SIZING_TYPE",
    "HTTP_REQUEST_SIZING_TYPE_HttpRequestSizingTypeHeaders",
    "HTTP_REQUEST_SIZING_TYPE_HttpRequestSizingTypeMax",
    "HTTP_REQUEST_SIZING_TYPE_HttpRequestSizingTypeTlsHandshakeLeg1ClientData",
    "HTTP_REQUEST_SIZING_TYPE_HttpRequestSizingTypeTlsHandshakeLeg1ServerData",
    "HTTP_REQUEST_SIZING_TYPE_HttpRequestSizingTypeTlsHandshakeLeg2ClientData",
    "HTTP_REQUEST_SIZING_TYPE_HttpRequestSizingTypeTlsHandshakeLeg2ServerData",
    "HTTP_REQUEST_TIMING_INFO",
    "HTTP_REQUEST_TIMING_TYPE",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeConnectionStart",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeDataStart",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeHttp2HeaderDecodeEnd",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeHttp2HeaderDecodeStart",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeHttp2StreamStart",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeHttp3HeaderDecodeEnd",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeHttp3HeaderDecodeStart",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeHttp3StreamStart",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeMax",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestDeliveredForDelegation",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestDeliveredForIO",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestDeliveredForInspection",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestHeaderParseEnd",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestHeaderParseStart",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestQueuedForDelegation",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestQueuedForIO",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestQueuedForInspection",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestReturnedAfterDelegation",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestReturnedAfterInspection",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestRoutingEnd",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeRequestRoutingStart",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsAttributesQueryEnd",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsAttributesQueryStart",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsCertificateLoadEnd",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsCertificateLoadStart",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsClientCertQueryEnd",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsClientCertQueryStart",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsHandshakeLeg1End",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsHandshakeLeg1Start",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsHandshakeLeg2End",
    "HTTP_REQUEST_TIMING_TYPE_HttpRequestTimingTypeTlsHandshakeLeg2Start",
    "HTTP_REQUEST_TOKEN_BINDING_INFO",
    "HTTP_REQUEST_V1",
    "HTTP_REQUEST_V2",
    "HTTP_RESPONSE_FLAG_MORE_ENTITY_BODY_EXISTS",
    "HTTP_RESPONSE_FLAG_MULTIPLE_ENCODINGS_AVAILABLE",
    "HTTP_RESPONSE_HEADERS",
    "HTTP_RESPONSE_INFO",
    "HTTP_RESPONSE_INFO_FLAGS_PRESERVE_ORDER",
    "HTTP_RESPONSE_INFO_TYPE",
    "HTTP_RESPONSE_INFO_TYPE_HttpResponseInfoTypeAuthenticationProperty",
    "HTTP_RESPONSE_INFO_TYPE_HttpResponseInfoTypeChannelBind",
    "HTTP_RESPONSE_INFO_TYPE_HttpResponseInfoTypeMultipleKnownHeaders",
    "HTTP_RESPONSE_INFO_TYPE_HttpResponseInfoTypeQoSProperty",
    "HTTP_RESPONSE_V1",
    "HTTP_RESPONSE_V2",
    "HTTP_SCHEME",
    "HTTP_SCHEME_HttpSchemeHttp",
    "HTTP_SCHEME_HttpSchemeHttps",
    "HTTP_SCHEME_HttpSchemeMaximum",
    "HTTP_SEND_RESPONSE_FLAG_BUFFER_DATA",
    "HTTP_SEND_RESPONSE_FLAG_DISCONNECT",
    "HTTP_SEND_RESPONSE_FLAG_ENABLE_NAGLING",
    "HTTP_SEND_RESPONSE_FLAG_GOAWAY",
    "HTTP_SEND_RESPONSE_FLAG_MORE_DATA",
    "HTTP_SEND_RESPONSE_FLAG_OPAQUE",
    "HTTP_SEND_RESPONSE_FLAG_PROCESS_RANGES",
    "HTTP_SERVER_AUTHENTICATION_BASIC_PARAMS",
    "HTTP_SERVER_AUTHENTICATION_DIGEST_PARAMS",
    "HTTP_SERVER_AUTHENTICATION_INFO",
    "HTTP_SERVER_PROPERTY",
    "HTTP_SERVER_PROPERTY_HttpServer503VerbosityProperty",
    "HTTP_SERVER_PROPERTY_HttpServerAuthenticationProperty",
    "HTTP_SERVER_PROPERTY_HttpServerBindingProperty",
    "HTTP_SERVER_PROPERTY_HttpServerChannelBindProperty",
    "HTTP_SERVER_PROPERTY_HttpServerDelegationProperty",
    "HTTP_SERVER_PROPERTY_HttpServerExtendedAuthenticationProperty",
    "HTTP_SERVER_PROPERTY_HttpServerListenEndpointProperty",
    "HTTP_SERVER_PROPERTY_HttpServerLoggingProperty",
    "HTTP_SERVER_PROPERTY_HttpServerProtectionLevelProperty",
    "HTTP_SERVER_PROPERTY_HttpServerQosProperty",
    "HTTP_SERVER_PROPERTY_HttpServerQueueLengthProperty",
    "HTTP_SERVER_PROPERTY_HttpServerStateProperty",
    "HTTP_SERVER_PROPERTY_HttpServerTimeoutsProperty",
    "HTTP_SERVICE_BINDING_A",
    "HTTP_SERVICE_BINDING_BASE",
    "HTTP_SERVICE_BINDING_TYPE",
    "HTTP_SERVICE_BINDING_TYPE_HttpServiceBindingTypeA",
    "HTTP_SERVICE_BINDING_TYPE_HttpServiceBindingTypeNone",
    "HTTP_SERVICE_BINDING_TYPE_HttpServiceBindingTypeW",
    "HTTP_SERVICE_BINDING_W",
    "HTTP_SERVICE_CONFIG_CACHE_KEY",
    "HTTP_SERVICE_CONFIG_CACHE_KEY_CacheRangeChunkSize",
    "HTTP_SERVICE_CONFIG_CACHE_KEY_MaxCacheResponseSize",
    "HTTP_SERVICE_CONFIG_CACHE_SET",
    "HTTP_SERVICE_CONFIG_ID",
    "HTTP_SERVICE_CONFIG_ID_HttpServiceConfigCache",
    "HTTP_SERVICE_CONFIG_ID_HttpServiceConfigIPListenList",
    "HTTP_SERVICE_CONFIG_ID_HttpServiceConfigMax",
    "HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSSLCertInfo",
    "HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSetting",
    "HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSslCcsCertInfo",
    "HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSslCcsCertInfoEx",
    "HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSslCertInfoEx",
    "HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSslScopedCcsCertInfo",
    "HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSslScopedCcsCertInfoEx",
    "HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSslSniCertInfo",
    "HTTP_SERVICE_CONFIG_ID_HttpServiceConfigSslSniCertInfoEx",
    "HTTP_SERVICE_CONFIG_ID_HttpServiceConfigTimeout",
    "HTTP_SERVICE_CONFIG_ID_HttpServiceConfigUrlAclInfo",
    "HTTP_SERVICE_CONFIG_IP_LISTEN_PARAM",
    "HTTP_SERVICE_CONFIG_IP_LISTEN_QUERY",
    "HTTP_SERVICE_CONFIG_QUERY_TYPE",
    "HTTP_SERVICE_CONFIG_QUERY_TYPE_HttpServiceConfigQueryExact",
    "HTTP_SERVICE_CONFIG_QUERY_TYPE_HttpServiceConfigQueryMax",
    "HTTP_SERVICE_CONFIG_QUERY_TYPE_HttpServiceConfigQueryNext",
    "HTTP_SERVICE_CONFIG_SETTING_KEY",
    "HTTP_SERVICE_CONFIG_SETTING_KEY_HttpNone",
    "HTTP_SERVICE_CONFIG_SETTING_KEY_HttpTlsThrottle",
    "HTTP_SERVICE_CONFIG_SETTING_SET",
    "HTTP_SERVICE_CONFIG_SSL_CCS_KEY",
    "HTTP_SERVICE_CONFIG_SSL_CCS_QUERY",
    "HTTP_SERVICE_CONFIG_SSL_CCS_QUERY_EX",
    "HTTP_SERVICE_CONFIG_SSL_CCS_SET",
    "HTTP_SERVICE_CONFIG_SSL_CCS_SET_EX",
    "HTTP_SERVICE_CONFIG_SSL_FLAG_DISABLE_HTTP2",
    "HTTP_SERVICE_CONFIG_SSL_FLAG_DISABLE_LEGACY_TLS",
    "HTTP_SERVICE_CONFIG_SSL_FLAG_DISABLE_OCSP_STAPLING",
    "HTTP_SERVICE_CONFIG_SSL_FLAG_DISABLE_QUIC",
    "HTTP_SERVICE_CONFIG_SSL_FLAG_DISABLE_TLS12",
    "HTTP_SERVICE_CONFIG_SSL_FLAG_DISABLE_TLS13",
    "HTTP_SERVICE_CONFIG_SSL_FLAG_ENABLE_CLIENT_CORRELATION",
    "HTTP_SERVICE_CONFIG_SSL_FLAG_ENABLE_SESSION_TICKET",
    "HTTP_SERVICE_CONFIG_SSL_FLAG_ENABLE_TOKEN_BINDING",
    "HTTP_SERVICE_CONFIG_SSL_FLAG_LOG_EXTENDED_EVENTS",
    "HTTP_SERVICE_CONFIG_SSL_FLAG_NEGOTIATE_CLIENT_CERT",
    "HTTP_SERVICE_CONFIG_SSL_FLAG_NO_RAW_FILTER",
    "HTTP_SERVICE_CONFIG_SSL_FLAG_REJECT",
    "HTTP_SERVICE_CONFIG_SSL_FLAG_USE_DS_MAPPER",
    "HTTP_SERVICE_CONFIG_SSL_KEY",
    "HTTP_SERVICE_CONFIG_SSL_KEY_EX",
    "HTTP_SERVICE_CONFIG_SSL_PARAM",
    "HTTP_SERVICE_CONFIG_SSL_PARAM_EX",
    "HTTP_SERVICE_CONFIG_SSL_QUERY",
    "HTTP_SERVICE_CONFIG_SSL_QUERY_EX",
    "HTTP_SERVICE_CONFIG_SSL_SET",
    "HTTP_SERVICE_CONFIG_SSL_SET_EX",
    "HTTP_SERVICE_CONFIG_SSL_SNI_KEY",
    "HTTP_SERVICE_CONFIG_SSL_SNI_QUERY",
    "HTTP_SERVICE_CONFIG_SSL_SNI_QUERY_EX",
    "HTTP_SERVICE_CONFIG_SSL_SNI_SET",
    "HTTP_SERVICE_CONFIG_SSL_SNI_SET_EX",
    "HTTP_SERVICE_CONFIG_TIMEOUT_KEY",
    "HTTP_SERVICE_CONFIG_TIMEOUT_KEY_HeaderWaitTimeout",
    "HTTP_SERVICE_CONFIG_TIMEOUT_KEY_IdleConnectionTimeout",
    "HTTP_SERVICE_CONFIG_TIMEOUT_SET",
    "HTTP_SERVICE_CONFIG_URLACL_KEY",
    "HTTP_SERVICE_CONFIG_URLACL_PARAM",
    "HTTP_SERVICE_CONFIG_URLACL_QUERY",
    "HTTP_SERVICE_CONFIG_URLACL_SET",
    "HTTP_SSL_CLIENT_CERT_INFO",
    "HTTP_SSL_INFO",
    "HTTP_SSL_PROTOCOL_INFO",
    "HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE",
    "HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE_ExParamTypeErrorHeaders",
    "HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE_ExParamTypeHttp2SettingsLimits",
    "HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE_ExParamTypeHttp2Window",
    "HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE_ExParamTypeHttpPerformance",
    "HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE_ExParamTypeMax",
    "HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE_ExParamTypeTlsRestrictions",
    "HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE_ExParamTypeTlsSessionTicketKeys",
    "HTTP_STATE_INFO",
    "HTTP_TIMEOUT_LIMIT_INFO",
    "HTTP_TLS_RESTRICTIONS_PARAM",
    "HTTP_TLS_SESSION_TICKET_KEYS_PARAM",
    "HTTP_TRANSPORT_ADDRESS",
    "HTTP_UNKNOWN_HEADER",
    "HTTP_URL_FLAG_REMOVE_ALL",
    "HTTP_VERB",
    "HTTP_VERB_HttpVerbCONNECT",
    "HTTP_VERB_HttpVerbCOPY",
    "HTTP_VERB_HttpVerbDELETE",
    "HTTP_VERB_HttpVerbGET",
    "HTTP_VERB_HttpVerbHEAD",
    "HTTP_VERB_HttpVerbInvalid",
    "HTTP_VERB_HttpVerbLOCK",
    "HTTP_VERB_HttpVerbMKCOL",
    "HTTP_VERB_HttpVerbMOVE",
    "HTTP_VERB_HttpVerbMaximum",
    "HTTP_VERB_HttpVerbOPTIONS",
    "HTTP_VERB_HttpVerbPOST",
    "HTTP_VERB_HttpVerbPROPFIND",
    "HTTP_VERB_HttpVerbPROPPATCH",
    "HTTP_VERB_HttpVerbPUT",
    "HTTP_VERB_HttpVerbSEARCH",
    "HTTP_VERB_HttpVerbTRACE",
    "HTTP_VERB_HttpVerbTRACK",
    "HTTP_VERB_HttpVerbUNLOCK",
    "HTTP_VERB_HttpVerbUnknown",
    "HTTP_VERB_HttpVerbUnparsed",
    "HTTP_VERSION",
    "HTTP_VERSION_CONSTANT",
    "HTTP_WSK_API_TIMINGS",
    "HttpAddFragmentToCache",
    "HttpAddUrl",
    "HttpAddUrlToUrlGroup",
    "HttpCancelHttpRequest",
    "HttpCloseRequestQueue",
    "HttpCloseServerSession",
    "HttpCloseUrlGroup",
    "HttpCreateHttpHandle",
    "HttpCreateRequestQueue",
    "HttpCreateServerSession",
    "HttpCreateUrlGroup",
    "HttpDeclarePush",
    "HttpDelegateRequestEx",
    "HttpDeleteServiceConfiguration",
    "HttpFindUrlGroupId",
    "HttpFlushResponseCache",
    "HttpGetExtension",
    "HttpInitialize",
    "HttpIsFeatureSupported",
    "HttpPrepareUrl",
    "HttpQueryRequestQueueProperty",
    "HttpQueryServerSessionProperty",
    "HttpQueryServiceConfiguration",
    "HttpQueryUrlGroupProperty",
    "HttpReadFragmentFromCache",
    "HttpReceiveClientCertificate",
    "HttpReceiveHttpRequest",
    "HttpReceiveRequestEntityBody",
    "HttpRemoveUrl",
    "HttpRemoveUrlFromUrlGroup",
    "HttpSendHttpResponse",
    "HttpSendResponseEntityBody",
    "HttpSetRequestProperty",
    "HttpSetRequestQueueProperty",
    "HttpSetServerSessionProperty",
    "HttpSetServiceConfiguration",
    "HttpSetUrlGroupProperty",
    "HttpShutdownRequestQueue",
    "HttpTerminate",
    "HttpUpdateServiceConfiguration",
    "HttpWaitForDemandStart",
    "HttpWaitForDisconnect",
    "HttpWaitForDisconnectEx",
]
_arch_optional = [
]
