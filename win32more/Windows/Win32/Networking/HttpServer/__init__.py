from __future__ import annotations
from win32more import ARCH, Annotated, Boolean, Byte, Bytes, Char, ComPtr, ConstantLazyLoader, Double, Enum, FAILED, Guid, Int16, Int32, Int64, IntPtr, POINTER, SByte, SUCCEEDED, Single, String, Structure, UInt16, UInt32, UInt64, UIntPtr, UnicodeAlias, Union, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Networking.HttpServer
import win32more.Windows.Win32.Networking.WinSock
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.System.IO
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
HTTP_LOG_FIELD_FAULT_CODE: UInt32 = 2147483648
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
HTTP_SERVICE_CONFIG_SSL_FLAG_DISABLE_SESSION_ID: UInt32 = 16384
HTTP_REQUEST_PROPERTY_SNI_HOST_MAX_LENGTH: UInt32 = 255
HTTP_REQUEST_PROPERTY_SNI_FLAG_SNI_USED: UInt32 = 1
HTTP_REQUEST_PROPERTY_SNI_FLAG_NO_SNI: UInt32 = 2
HTTP_VERSION_CONSTANT: String = 'HTTP/1.0'
@winfunctype('HTTPAPI.dll')
def HttpInitialize(Version: win32more.Windows.Win32.Networking.HttpServer.HTTPAPI_VERSION, Flags: win32more.Windows.Win32.Networking.HttpServer.HTTP_INITIALIZE, pReserved: VoidPtr) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpTerminate(Flags: win32more.Windows.Win32.Networking.HttpServer.HTTP_INITIALIZE, pReserved: VoidPtr) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpCreateHttpHandle(RequestQueueHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE), Reserved: UInt32) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpCreateRequestQueue(Version: win32more.Windows.Win32.Networking.HttpServer.HTTPAPI_VERSION, Name: win32more.Windows.Win32.Foundation.PWSTR, SecurityAttributes: POINTER(win32more.Windows.Win32.Security.SECURITY_ATTRIBUTES), Flags: UInt32, RequestQueueHandle: POINTER(win32more.Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpCloseRequestQueue(RequestQueueHandle: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpSetRequestQueueProperty(RequestQueueHandle: win32more.Windows.Win32.Foundation.HANDLE, Property: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVER_PROPERTY, PropertyInformation: VoidPtr, PropertyInformationLength: UInt32, Reserved1: UInt32, Reserved2: VoidPtr) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpQueryRequestQueueProperty(RequestQueueHandle: win32more.Windows.Win32.Foundation.HANDLE, Property: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVER_PROPERTY, PropertyInformation: VoidPtr, PropertyInformationLength: UInt32, Reserved1: UInt32, ReturnLength: POINTER(UInt32), Reserved2: VoidPtr) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpSetRequestProperty(RequestQueueHandle: win32more.Windows.Win32.Foundation.HANDLE, Id: UInt64, PropertyId: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_PROPERTY, Input: VoidPtr, InputPropertySize: UInt32, Overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpShutdownRequestQueue(RequestQueueHandle: win32more.Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpReceiveClientCertificate(RequestQueueHandle: win32more.Windows.Win32.Foundation.HANDLE, ConnectionId: UInt64, Flags: UInt32, SslClientCertInfo: POINTER(win32more.Windows.Win32.Networking.HttpServer.HTTP_SSL_CLIENT_CERT_INFO), SslClientCertInfoSize: UInt32, BytesReceived: POINTER(UInt32), Overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpCreateServerSession(Version: win32more.Windows.Win32.Networking.HttpServer.HTTPAPI_VERSION, ServerSessionId: POINTER(UInt64), Reserved: UInt32) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpCloseServerSession(ServerSessionId: UInt64) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpQueryServerSessionProperty(ServerSessionId: UInt64, Property: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVER_PROPERTY, PropertyInformation: VoidPtr, PropertyInformationLength: UInt32, ReturnLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpSetServerSessionProperty(ServerSessionId: UInt64, Property: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVER_PROPERTY, PropertyInformation: VoidPtr, PropertyInformationLength: UInt32) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpAddUrl(RequestQueueHandle: win32more.Windows.Win32.Foundation.HANDLE, FullyQualifiedUrl: win32more.Windows.Win32.Foundation.PWSTR, Reserved: VoidPtr) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpRemoveUrl(RequestQueueHandle: win32more.Windows.Win32.Foundation.HANDLE, FullyQualifiedUrl: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpCreateUrlGroup(ServerSessionId: UInt64, pUrlGroupId: POINTER(UInt64), Reserved: UInt32) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpCloseUrlGroup(UrlGroupId: UInt64) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpAddUrlToUrlGroup(UrlGroupId: UInt64, pFullyQualifiedUrl: win32more.Windows.Win32.Foundation.PWSTR, UrlContext: UInt64, Reserved: UInt32) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpRemoveUrlFromUrlGroup(UrlGroupId: UInt64, pFullyQualifiedUrl: win32more.Windows.Win32.Foundation.PWSTR, Flags: UInt32) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpSetUrlGroupProperty(UrlGroupId: UInt64, Property: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVER_PROPERTY, PropertyInformation: VoidPtr, PropertyInformationLength: UInt32) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpQueryUrlGroupProperty(UrlGroupId: UInt64, Property: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVER_PROPERTY, PropertyInformation: VoidPtr, PropertyInformationLength: UInt32, ReturnLength: POINTER(UInt32)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpPrepareUrl(Reserved: VoidPtr, Flags: UInt32, Url: win32more.Windows.Win32.Foundation.PWSTR, PreparedUrl: POINTER(win32more.Windows.Win32.Foundation.PWSTR)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpReceiveHttpRequest(RequestQueueHandle: win32more.Windows.Win32.Foundation.HANDLE, RequestId: UInt64, Flags: win32more.Windows.Win32.Networking.HttpServer.HTTP_RECEIVE_HTTP_REQUEST_FLAGS, RequestBuffer: POINTER(win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_V2), RequestBufferLength: UInt32, BytesReturned: POINTER(UInt32), Overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpReceiveRequestEntityBody(RequestQueueHandle: win32more.Windows.Win32.Foundation.HANDLE, RequestId: UInt64, Flags: UInt32, EntityBuffer: VoidPtr, EntityBufferLength: UInt32, BytesReturned: POINTER(UInt32), Overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpSendHttpResponse(RequestQueueHandle: win32more.Windows.Win32.Foundation.HANDLE, RequestId: UInt64, Flags: UInt32, HttpResponse: POINTER(win32more.Windows.Win32.Networking.HttpServer.HTTP_RESPONSE_V2), CachePolicy: POINTER(win32more.Windows.Win32.Networking.HttpServer.HTTP_CACHE_POLICY), BytesSent: POINTER(UInt32), Reserved1: VoidPtr, Reserved2: UInt32, Overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED), LogData: POINTER(win32more.Windows.Win32.Networking.HttpServer.HTTP_LOG_DATA)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpSendResponseEntityBody(RequestQueueHandle: win32more.Windows.Win32.Foundation.HANDLE, RequestId: UInt64, Flags: UInt32, EntityChunkCount: UInt16, EntityChunks: POINTER(win32more.Windows.Win32.Networking.HttpServer.HTTP_DATA_CHUNK), BytesSent: POINTER(UInt32), Reserved1: VoidPtr, Reserved2: UInt32, Overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED), LogData: POINTER(win32more.Windows.Win32.Networking.HttpServer.HTTP_LOG_DATA)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpDeclarePush(RequestQueueHandle: win32more.Windows.Win32.Foundation.HANDLE, RequestId: UInt64, Verb: win32more.Windows.Win32.Networking.HttpServer.HTTP_VERB, Path: win32more.Windows.Win32.Foundation.PWSTR, Query: win32more.Windows.Win32.Foundation.PSTR, Headers: POINTER(win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_HEADERS)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpWaitForDisconnect(RequestQueueHandle: win32more.Windows.Win32.Foundation.HANDLE, ConnectionId: UInt64, Overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpWaitForDisconnectEx(RequestQueueHandle: win32more.Windows.Win32.Foundation.HANDLE, ConnectionId: UInt64, Reserved: UInt32, Overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpCancelHttpRequest(RequestQueueHandle: win32more.Windows.Win32.Foundation.HANDLE, RequestId: UInt64, Overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpWaitForDemandStart(RequestQueueHandle: win32more.Windows.Win32.Foundation.HANDLE, Overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpIsFeatureSupported(FeatureId: win32more.Windows.Win32.Networking.HttpServer.HTTP_FEATURE_ID) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('HTTPAPI.dll')
def HttpDelegateRequestEx(RequestQueueHandle: win32more.Windows.Win32.Foundation.HANDLE, DelegateQueueHandle: win32more.Windows.Win32.Foundation.HANDLE, RequestId: UInt64, DelegateUrlGroupId: UInt64, PropertyInfoSetSize: UInt32, PropertyInfoSet: POINTER(win32more.Windows.Win32.Networking.HttpServer.HTTP_DELEGATE_REQUEST_PROPERTY_INFO)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpFindUrlGroupId(FullyQualifiedUrl: win32more.Windows.Win32.Foundation.PWSTR, RequestQueueHandle: win32more.Windows.Win32.Foundation.HANDLE, UrlGroupId: POINTER(UInt64)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpFlushResponseCache(RequestQueueHandle: win32more.Windows.Win32.Foundation.HANDLE, UrlPrefix: win32more.Windows.Win32.Foundation.PWSTR, Flags: UInt32, Overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpAddFragmentToCache(RequestQueueHandle: win32more.Windows.Win32.Foundation.HANDLE, UrlPrefix: win32more.Windows.Win32.Foundation.PWSTR, DataChunk: POINTER(win32more.Windows.Win32.Networking.HttpServer.HTTP_DATA_CHUNK), CachePolicy: POINTER(win32more.Windows.Win32.Networking.HttpServer.HTTP_CACHE_POLICY), Overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpReadFragmentFromCache(RequestQueueHandle: win32more.Windows.Win32.Foundation.HANDLE, UrlPrefix: win32more.Windows.Win32.Foundation.PWSTR, ByteRange: POINTER(win32more.Windows.Win32.Networking.HttpServer.HTTP_BYTE_RANGE), Buffer: VoidPtr, BufferLength: UInt32, BytesRead: POINTER(UInt32), Overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpSetServiceConfiguration(ServiceHandle: win32more.Windows.Win32.Foundation.HANDLE, ConfigId: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_ID, pConfigInformation: VoidPtr, ConfigInformationLength: UInt32, pOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpUpdateServiceConfiguration(Handle: win32more.Windows.Win32.Foundation.HANDLE, ConfigId: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_ID, ConfigInfo: VoidPtr, ConfigInfoLength: UInt32, Overlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpDeleteServiceConfiguration(ServiceHandle: win32more.Windows.Win32.Foundation.HANDLE, ConfigId: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_ID, pConfigInformation: VoidPtr, ConfigInformationLength: UInt32, pOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpQueryServiceConfiguration(ServiceHandle: win32more.Windows.Win32.Foundation.HANDLE, ConfigId: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_ID, pInput: VoidPtr, InputLength: UInt32, pOutput: VoidPtr, OutputLength: UInt32, pReturnLength: POINTER(UInt32), pOverlapped: POINTER(win32more.Windows.Win32.System.IO.OVERLAPPED)) -> UInt32: ...
@winfunctype('HTTPAPI.dll')
def HttpGetExtension(Version: win32more.Windows.Win32.Networking.HttpServer.HTTPAPI_VERSION, Extension: UInt32, Buffer: VoidPtr, BufferSize: UInt32) -> UInt32: ...
class HTTP2_SETTINGS_LIMITS_PARAM(Structure):
    Http2MaxSettingsPerFrame: UInt32
    Http2MaxSettingsPerMinute: UInt32
class HTTP2_WINDOW_SIZE_PARAM(Structure):
    Http2ReceiveWindowSize: UInt32
class HTTPAPI_VERSION(Structure):
    HttpApiMajorVersion: UInt16
    HttpApiMinorVersion: UInt16
HTTP_503_RESPONSE_VERBOSITY = Int32
Http503ResponseVerbosityBasic: win32more.Windows.Win32.Networking.HttpServer.HTTP_503_RESPONSE_VERBOSITY = 0
Http503ResponseVerbosityLimited: win32more.Windows.Win32.Networking.HttpServer.HTTP_503_RESPONSE_VERBOSITY = 1
Http503ResponseVerbosityFull: win32more.Windows.Win32.Networking.HttpServer.HTTP_503_RESPONSE_VERBOSITY = 2
HTTP_AUTHENTICATION_HARDENING_LEVELS = Int32
HttpAuthenticationHardeningLegacy: win32more.Windows.Win32.Networking.HttpServer.HTTP_AUTHENTICATION_HARDENING_LEVELS = 0
HttpAuthenticationHardeningMedium: win32more.Windows.Win32.Networking.HttpServer.HTTP_AUTHENTICATION_HARDENING_LEVELS = 1
HttpAuthenticationHardeningStrict: win32more.Windows.Win32.Networking.HttpServer.HTTP_AUTHENTICATION_HARDENING_LEVELS = 2
HTTP_AUTH_STATUS = Int32
HttpAuthStatusSuccess: win32more.Windows.Win32.Networking.HttpServer.HTTP_AUTH_STATUS = 0
HttpAuthStatusNotAuthenticated: win32more.Windows.Win32.Networking.HttpServer.HTTP_AUTH_STATUS = 1
HttpAuthStatusFailure: win32more.Windows.Win32.Networking.HttpServer.HTTP_AUTH_STATUS = 2
class HTTP_BANDWIDTH_LIMIT_INFO(Structure):
    Flags: win32more.Windows.Win32.Networking.HttpServer.HTTP_PROPERTY_FLAGS
    MaxBandwidth: UInt32
class HTTP_BINDING_INFO(Structure):
    Flags: win32more.Windows.Win32.Networking.HttpServer.HTTP_PROPERTY_FLAGS
    RequestQueueHandle: win32more.Windows.Win32.Foundation.HANDLE
class HTTP_BYTE_RANGE(Structure):
    StartingOffset: UInt64
    Length: UInt64
class HTTP_CACHE_POLICY(Structure):
    Policy: win32more.Windows.Win32.Networking.HttpServer.HTTP_CACHE_POLICY_TYPE
    SecondsToLive: UInt32
HTTP_CACHE_POLICY_TYPE = Int32
HttpCachePolicyNocache: win32more.Windows.Win32.Networking.HttpServer.HTTP_CACHE_POLICY_TYPE = 0
HttpCachePolicyUserInvalidates: win32more.Windows.Win32.Networking.HttpServer.HTTP_CACHE_POLICY_TYPE = 1
HttpCachePolicyTimeToLive: win32more.Windows.Win32.Networking.HttpServer.HTTP_CACHE_POLICY_TYPE = 2
HttpCachePolicyMaximum: win32more.Windows.Win32.Networking.HttpServer.HTTP_CACHE_POLICY_TYPE = 3
class HTTP_CHANNEL_BIND_INFO(Structure):
    Hardening: win32more.Windows.Win32.Networking.HttpServer.HTTP_AUTHENTICATION_HARDENING_LEVELS
    Flags: UInt32
    ServiceNames: POINTER(POINTER(win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_BINDING_BASE))
    NumberOfServiceNames: UInt32
class HTTP_CONNECTION_LIMIT_INFO(Structure):
    Flags: win32more.Windows.Win32.Networking.HttpServer.HTTP_PROPERTY_FLAGS
    MaxConnections: UInt32
class HTTP_COOKED_URL(Structure):
    FullUrlLength: UInt16
    HostLength: UInt16
    AbsPathLength: UInt16
    QueryStringLength: UInt16
    pFullUrl: win32more.Windows.Win32.Foundation.PWSTR
    pHost: win32more.Windows.Win32.Foundation.PWSTR
    pAbsPath: win32more.Windows.Win32.Foundation.PWSTR
    pQueryString: win32more.Windows.Win32.Foundation.PWSTR
HTTP_CREATE_REQUEST_QUEUE_PROPERTY_ID = Int32
CreateRequestQueueExternalIdProperty: win32more.Windows.Win32.Networking.HttpServer.HTTP_CREATE_REQUEST_QUEUE_PROPERTY_ID = 1
CreateRequestQueueMax: win32more.Windows.Win32.Networking.HttpServer.HTTP_CREATE_REQUEST_QUEUE_PROPERTY_ID = 2
class HTTP_CREATE_REQUEST_QUEUE_PROPERTY_INFO(Structure):
    PropertyId: win32more.Windows.Win32.Networking.HttpServer.HTTP_CREATE_REQUEST_QUEUE_PROPERTY_ID
    PropertyInfoLength: UInt32
    PropertyInfo: VoidPtr
class HTTP_DATA_CHUNK(Structure):
    DataChunkType: win32more.Windows.Win32.Networking.HttpServer.HTTP_DATA_CHUNK_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        FromMemory: _FromMemory_e__Struct
        FromFileHandle: _FromFileHandle_e__Struct
        FromFragmentCache: _FromFragmentCache_e__Struct
        FromFragmentCacheEx: _FromFragmentCacheEx_e__Struct
        Trailers: _Trailers_e__Struct
        class _FromMemory_e__Struct(Structure):
            pBuffer: VoidPtr
            BufferLength: UInt32
        class _FromFileHandle_e__Struct(Structure):
            ByteRange: win32more.Windows.Win32.Networking.HttpServer.HTTP_BYTE_RANGE
            FileHandle: win32more.Windows.Win32.Foundation.HANDLE
        class _FromFragmentCache_e__Struct(Structure):
            FragmentNameLength: UInt16
            pFragmentName: win32more.Windows.Win32.Foundation.PWSTR
        class _FromFragmentCacheEx_e__Struct(Structure):
            ByteRange: win32more.Windows.Win32.Networking.HttpServer.HTTP_BYTE_RANGE
            pFragmentName: win32more.Windows.Win32.Foundation.PWSTR
        class _Trailers_e__Struct(Structure):
            TrailerCount: UInt16
            pTrailers: POINTER(win32more.Windows.Win32.Networking.HttpServer.HTTP_UNKNOWN_HEADER)
HTTP_DATA_CHUNK_TYPE = Int32
HttpDataChunkFromMemory: win32more.Windows.Win32.Networking.HttpServer.HTTP_DATA_CHUNK_TYPE = 0
HttpDataChunkFromFileHandle: win32more.Windows.Win32.Networking.HttpServer.HTTP_DATA_CHUNK_TYPE = 1
HttpDataChunkFromFragmentCache: win32more.Windows.Win32.Networking.HttpServer.HTTP_DATA_CHUNK_TYPE = 2
HttpDataChunkFromFragmentCacheEx: win32more.Windows.Win32.Networking.HttpServer.HTTP_DATA_CHUNK_TYPE = 3
HttpDataChunkTrailers: win32more.Windows.Win32.Networking.HttpServer.HTTP_DATA_CHUNK_TYPE = 4
HttpDataChunkMaximum: win32more.Windows.Win32.Networking.HttpServer.HTTP_DATA_CHUNK_TYPE = 5
HTTP_DELEGATE_REQUEST_PROPERTY_ID = Int32
DelegateRequestReservedProperty: win32more.Windows.Win32.Networking.HttpServer.HTTP_DELEGATE_REQUEST_PROPERTY_ID = 0
DelegateRequestDelegateUrlProperty: win32more.Windows.Win32.Networking.HttpServer.HTTP_DELEGATE_REQUEST_PROPERTY_ID = 1
class HTTP_DELEGATE_REQUEST_PROPERTY_INFO(Structure):
    PropertyId: win32more.Windows.Win32.Networking.HttpServer.HTTP_DELEGATE_REQUEST_PROPERTY_ID
    PropertyInfoLength: UInt32
    PropertyInfo: VoidPtr
HTTP_ENABLED_STATE = Int32
HttpEnabledStateActive: win32more.Windows.Win32.Networking.HttpServer.HTTP_ENABLED_STATE = 0
HttpEnabledStateInactive: win32more.Windows.Win32.Networking.HttpServer.HTTP_ENABLED_STATE = 1
class HTTP_ERROR_HEADERS_PARAM(Structure):
    StatusCode: UInt16
    HeaderCount: UInt16
    Headers: POINTER(win32more.Windows.Win32.Networking.HttpServer.HTTP_UNKNOWN_HEADER)
HTTP_FEATURE_ID = Int32
HttpFeatureUnknown: win32more.Windows.Win32.Networking.HttpServer.HTTP_FEATURE_ID = 0
HttpFeatureResponseTrailers: win32more.Windows.Win32.Networking.HttpServer.HTTP_FEATURE_ID = 1
HttpFeatureApiTimings: win32more.Windows.Win32.Networking.HttpServer.HTTP_FEATURE_ID = 2
HttpFeatureDelegateEx: win32more.Windows.Win32.Networking.HttpServer.HTTP_FEATURE_ID = 3
HttpFeatureHttp3: win32more.Windows.Win32.Networking.HttpServer.HTTP_FEATURE_ID = 4
HttpFeatureLast: win32more.Windows.Win32.Networking.HttpServer.HTTP_FEATURE_ID = 5
HttpFeaturemax: win32more.Windows.Win32.Networking.HttpServer.HTTP_FEATURE_ID = -1
class HTTP_FLOWRATE_INFO(Structure):
    Flags: win32more.Windows.Win32.Networking.HttpServer.HTTP_PROPERTY_FLAGS
    MaxBandwidth: UInt32
    MaxPeakBandwidth: UInt32
    BurstSize: UInt32
HTTP_HEADER_ID = Int32
HttpHeaderCacheControl: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 0
HttpHeaderConnection: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 1
HttpHeaderDate: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 2
HttpHeaderKeepAlive: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 3
HttpHeaderPragma: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 4
HttpHeaderTrailer: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 5
HttpHeaderTransferEncoding: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 6
HttpHeaderUpgrade: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 7
HttpHeaderVia: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 8
HttpHeaderWarning: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 9
HttpHeaderAllow: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 10
HttpHeaderContentLength: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 11
HttpHeaderContentType: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 12
HttpHeaderContentEncoding: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 13
HttpHeaderContentLanguage: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 14
HttpHeaderContentLocation: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 15
HttpHeaderContentMd5: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 16
HttpHeaderContentRange: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 17
HttpHeaderExpires: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 18
HttpHeaderLastModified: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 19
HttpHeaderAccept: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 20
HttpHeaderAcceptCharset: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 21
HttpHeaderAcceptEncoding: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 22
HttpHeaderAcceptLanguage: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 23
HttpHeaderAuthorization: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 24
HttpHeaderCookie: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 25
HttpHeaderExpect: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 26
HttpHeaderFrom: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 27
HttpHeaderHost: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 28
HttpHeaderIfMatch: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 29
HttpHeaderIfModifiedSince: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 30
HttpHeaderIfNoneMatch: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 31
HttpHeaderIfRange: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 32
HttpHeaderIfUnmodifiedSince: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 33
HttpHeaderMaxForwards: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 34
HttpHeaderProxyAuthorization: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 35
HttpHeaderReferer: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 36
HttpHeaderRange: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 37
HttpHeaderTe: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 38
HttpHeaderTranslate: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 39
HttpHeaderUserAgent: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 40
HttpHeaderRequestMaximum: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 41
HttpHeaderAcceptRanges: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 20
HttpHeaderAge: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 21
HttpHeaderEtag: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 22
HttpHeaderLocation: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 23
HttpHeaderProxyAuthenticate: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 24
HttpHeaderRetryAfter: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 25
HttpHeaderServer: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 26
HttpHeaderSetCookie: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 27
HttpHeaderVary: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 28
HttpHeaderWwwAuthenticate: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 29
HttpHeaderResponseMaximum: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 30
HttpHeaderMaximum: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID = 41
HTTP_INITIALIZE = UInt32
HTTP_INITIALIZE_CONFIG: win32more.Windows.Win32.Networking.HttpServer.HTTP_INITIALIZE = 2
HTTP_INITIALIZE_SERVER: win32more.Windows.Win32.Networking.HttpServer.HTTP_INITIALIZE = 1
class HTTP_KNOWN_HEADER(Structure):
    RawValueLength: UInt16
    pRawValue: win32more.Windows.Win32.Foundation.PSTR
class HTTP_LISTEN_ENDPOINT_INFO(Structure):
    Flags: win32more.Windows.Win32.Networking.HttpServer.HTTP_PROPERTY_FLAGS
    EnableSharing: win32more.Windows.Win32.Foundation.BOOLEAN
class HTTP_LOGGING_INFO(Structure):
    Flags: win32more.Windows.Win32.Networking.HttpServer.HTTP_PROPERTY_FLAGS
    LoggingFlags: UInt32
    SoftwareName: win32more.Windows.Win32.Foundation.PWSTR
    SoftwareNameLength: UInt16
    DirectoryNameLength: UInt16
    DirectoryName: win32more.Windows.Win32.Foundation.PWSTR
    Format: win32more.Windows.Win32.Networking.HttpServer.HTTP_LOGGING_TYPE
    Fields: UInt32
    pExtFields: VoidPtr
    NumOfExtFields: UInt16
    MaxRecordSize: UInt16
    RolloverType: win32more.Windows.Win32.Networking.HttpServer.HTTP_LOGGING_ROLLOVER_TYPE
    RolloverSize: UInt32
    pSecurityDescriptor: win32more.Windows.Win32.Security.PSECURITY_DESCRIPTOR
HTTP_LOGGING_ROLLOVER_TYPE = Int32
HttpLoggingRolloverSize: win32more.Windows.Win32.Networking.HttpServer.HTTP_LOGGING_ROLLOVER_TYPE = 0
HttpLoggingRolloverDaily: win32more.Windows.Win32.Networking.HttpServer.HTTP_LOGGING_ROLLOVER_TYPE = 1
HttpLoggingRolloverWeekly: win32more.Windows.Win32.Networking.HttpServer.HTTP_LOGGING_ROLLOVER_TYPE = 2
HttpLoggingRolloverMonthly: win32more.Windows.Win32.Networking.HttpServer.HTTP_LOGGING_ROLLOVER_TYPE = 3
HttpLoggingRolloverHourly: win32more.Windows.Win32.Networking.HttpServer.HTTP_LOGGING_ROLLOVER_TYPE = 4
HTTP_LOGGING_TYPE = Int32
HttpLoggingTypeW3C: win32more.Windows.Win32.Networking.HttpServer.HTTP_LOGGING_TYPE = 0
HttpLoggingTypeIIS: win32more.Windows.Win32.Networking.HttpServer.HTTP_LOGGING_TYPE = 1
HttpLoggingTypeNCSA: win32more.Windows.Win32.Networking.HttpServer.HTTP_LOGGING_TYPE = 2
HttpLoggingTypeRaw: win32more.Windows.Win32.Networking.HttpServer.HTTP_LOGGING_TYPE = 3
class HTTP_LOG_DATA(Structure):
    Type: win32more.Windows.Win32.Networking.HttpServer.HTTP_LOG_DATA_TYPE
HTTP_LOG_DATA_TYPE = Int32
HttpLogDataTypeFields: win32more.Windows.Win32.Networking.HttpServer.HTTP_LOG_DATA_TYPE = 0
class HTTP_LOG_FIELDS_DATA(Structure):
    Base: win32more.Windows.Win32.Networking.HttpServer.HTTP_LOG_DATA
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
    UserName: win32more.Windows.Win32.Foundation.PWSTR
    UriStem: win32more.Windows.Win32.Foundation.PWSTR
    ClientIp: win32more.Windows.Win32.Foundation.PSTR
    ServerName: win32more.Windows.Win32.Foundation.PSTR
    ServiceName: win32more.Windows.Win32.Foundation.PSTR
    ServerIp: win32more.Windows.Win32.Foundation.PSTR
    Method: win32more.Windows.Win32.Foundation.PSTR
    UriQuery: win32more.Windows.Win32.Foundation.PSTR
    Host: win32more.Windows.Win32.Foundation.PSTR
    UserAgent: win32more.Windows.Win32.Foundation.PSTR
    Cookie: win32more.Windows.Win32.Foundation.PSTR
    Referrer: win32more.Windows.Win32.Foundation.PSTR
    ServerPort: UInt16
    ProtocolStatus: UInt16
    Win32Status: UInt32
    MethodNum: win32more.Windows.Win32.Networking.HttpServer.HTTP_VERB
    SubStatus: UInt16
class HTTP_MULTIPLE_KNOWN_HEADERS(Structure):
    HeaderId: win32more.Windows.Win32.Networking.HttpServer.HTTP_HEADER_ID
    Flags: UInt32
    KnownHeaderCount: UInt16
    KnownHeaders: POINTER(win32more.Windows.Win32.Networking.HttpServer.HTTP_KNOWN_HEADER)
class HTTP_PERFORMANCE_PARAM(Structure):
    Type: win32more.Windows.Win32.Networking.HttpServer.HTTP_PERFORMANCE_PARAM_TYPE
    BufferSize: UInt32
    Buffer: VoidPtr
HTTP_PERFORMANCE_PARAM_TYPE = Int32
PerformanceParamSendBufferingFlags: win32more.Windows.Win32.Networking.HttpServer.HTTP_PERFORMANCE_PARAM_TYPE = 0
PerformanceParamAggressiveICW: win32more.Windows.Win32.Networking.HttpServer.HTTP_PERFORMANCE_PARAM_TYPE = 1
PerformanceParamMaxSendBufferSize: win32more.Windows.Win32.Networking.HttpServer.HTTP_PERFORMANCE_PARAM_TYPE = 2
PerformanceParamMaxConcurrentClientStreams: win32more.Windows.Win32.Networking.HttpServer.HTTP_PERFORMANCE_PARAM_TYPE = 3
PerformanceParamMaxReceiveBufferSize: win32more.Windows.Win32.Networking.HttpServer.HTTP_PERFORMANCE_PARAM_TYPE = 4
PerformanceParamDecryptOnSspiThread: win32more.Windows.Win32.Networking.HttpServer.HTTP_PERFORMANCE_PARAM_TYPE = 5
PerformanceParamMax: win32more.Windows.Win32.Networking.HttpServer.HTTP_PERFORMANCE_PARAM_TYPE = 6
class HTTP_PROPERTY_FLAGS(Structure):
    Present: Annotated[UInt32, 1]
class HTTP_PROTECTION_LEVEL_INFO(Structure):
    Flags: win32more.Windows.Win32.Networking.HttpServer.HTTP_PROPERTY_FLAGS
    Level: win32more.Windows.Win32.Networking.HttpServer.HTTP_PROTECTION_LEVEL_TYPE
HTTP_PROTECTION_LEVEL_TYPE = Int32
HttpProtectionLevelUnrestricted: win32more.Windows.Win32.Networking.HttpServer.HTTP_PROTECTION_LEVEL_TYPE = 0
HttpProtectionLevelEdgeRestricted: win32more.Windows.Win32.Networking.HttpServer.HTTP_PROTECTION_LEVEL_TYPE = 1
HttpProtectionLevelRestricted: win32more.Windows.Win32.Networking.HttpServer.HTTP_PROTECTION_LEVEL_TYPE = 2
class HTTP_QOS_SETTING_INFO(Structure):
    QosType: win32more.Windows.Win32.Networking.HttpServer.HTTP_QOS_SETTING_TYPE
    QosSetting: VoidPtr
HTTP_QOS_SETTING_TYPE = Int32
HttpQosSettingTypeBandwidth: win32more.Windows.Win32.Networking.HttpServer.HTTP_QOS_SETTING_TYPE = 0
HttpQosSettingTypeConnectionLimit: win32more.Windows.Win32.Networking.HttpServer.HTTP_QOS_SETTING_TYPE = 1
HttpQosSettingTypeFlowRate: win32more.Windows.Win32.Networking.HttpServer.HTTP_QOS_SETTING_TYPE = 2
class HTTP_QUERY_REQUEST_QUALIFIER_QUIC(Structure):
    Freshness: UInt64
class HTTP_QUERY_REQUEST_QUALIFIER_TCP(Structure):
    Freshness: UInt64
class HTTP_QUIC_API_TIMINGS(Structure):
    ConnectionTimings: win32more.Windows.Win32.Networking.HttpServer.HTTP_QUIC_CONNECTION_API_TIMINGS
    StreamTimings: win32more.Windows.Win32.Networking.HttpServer.HTTP_QUIC_STREAM_API_TIMINGS
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
    ControlStreamTimings: win32more.Windows.Win32.Networking.HttpServer.HTTP_QUIC_STREAM_API_TIMINGS
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
class HTTP_QUIC_STREAM_REQUEST_STATS(Structure):
    StreamWaitStart: UInt64
    StreamWaitEnd: UInt64
    RequestHeadersCompressionStart: UInt64
    RequestHeadersCompressionEnd: UInt64
    ResponseHeadersDecompressionStart: UInt64
    ResponseHeadersDecompressionEnd: UInt64
    RequestHeadersCompressedSize: UInt64
    ResponseHeadersCompressedSize: UInt64
HTTP_RECEIVE_HTTP_REQUEST_FLAGS = UInt32
HTTP_RECEIVE_REQUEST_FLAG_COPY_BODY: win32more.Windows.Win32.Networking.HttpServer.HTTP_RECEIVE_HTTP_REQUEST_FLAGS = 1
HTTP_RECEIVE_REQUEST_FLAG_FLUSH_BODY: win32more.Windows.Win32.Networking.HttpServer.HTTP_RECEIVE_HTTP_REQUEST_FLAGS = 2
class HTTP_REQUEST_AUTH_INFO(Structure):
    AuthStatus: win32more.Windows.Win32.Networking.HttpServer.HTTP_AUTH_STATUS
    SecStatus: win32more.Windows.Win32.Foundation.HRESULT
    Flags: UInt32
    AuthType: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_AUTH_TYPE
    AccessToken: win32more.Windows.Win32.Foundation.HANDLE
    ContextAttributes: UInt32
    PackedContextLength: UInt32
    PackedContextType: UInt32
    PackedContext: VoidPtr
    MutualAuthDataLength: UInt32
    pMutualAuthData: win32more.Windows.Win32.Foundation.PSTR
    PackageNameLength: UInt16
    pPackageName: win32more.Windows.Win32.Foundation.PWSTR
HTTP_REQUEST_AUTH_TYPE = Int32
HttpRequestAuthTypeNone: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_AUTH_TYPE = 0
HttpRequestAuthTypeBasic: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_AUTH_TYPE = 1
HttpRequestAuthTypeDigest: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_AUTH_TYPE = 2
HttpRequestAuthTypeNTLM: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_AUTH_TYPE = 3
HttpRequestAuthTypeNegotiate: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_AUTH_TYPE = 4
HttpRequestAuthTypeKerberos: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_AUTH_TYPE = 5
class HTTP_REQUEST_CHANNEL_BIND_STATUS(Structure):
    ServiceName: POINTER(win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_BINDING_BASE)
    ChannelToken: POINTER(Byte)
    ChannelTokenSize: UInt32
    Flags: UInt32
class HTTP_REQUEST_HEADERS(Structure):
    UnknownHeaderCount: UInt16
    pUnknownHeaders: POINTER(win32more.Windows.Win32.Networking.HttpServer.HTTP_UNKNOWN_HEADER)
    TrailerCount: UInt16
    pTrailers: POINTER(win32more.Windows.Win32.Networking.HttpServer.HTTP_UNKNOWN_HEADER)
    KnownHeaders: win32more.Windows.Win32.Networking.HttpServer.HTTP_KNOWN_HEADER * 41
class HTTP_REQUEST_INFO(Structure):
    InfoType: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_INFO_TYPE
    InfoLength: UInt32
    pInfo: VoidPtr
HTTP_REQUEST_INFO_TYPE = Int32
HttpRequestInfoTypeAuth: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_INFO_TYPE = 0
HttpRequestInfoTypeChannelBind: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_INFO_TYPE = 1
HttpRequestInfoTypeSslProtocol: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_INFO_TYPE = 2
HttpRequestInfoTypeSslTokenBindingDraft: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_INFO_TYPE = 3
HttpRequestInfoTypeSslTokenBinding: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_INFO_TYPE = 4
HttpRequestInfoTypeRequestTiming: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_INFO_TYPE = 5
HttpRequestInfoTypeTcpInfoV0: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_INFO_TYPE = 6
HttpRequestInfoTypeRequestSizing: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_INFO_TYPE = 7
HttpRequestInfoTypeQuicStats: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_INFO_TYPE = 8
HttpRequestInfoTypeTcpInfoV1: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_INFO_TYPE = 9
HTTP_REQUEST_PROPERTY = Int32
HttpRequestPropertyIsb: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_PROPERTY = 0
HttpRequestPropertyTcpInfoV0: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_PROPERTY = 1
HttpRequestPropertyQuicStats: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_PROPERTY = 2
HttpRequestPropertyTcpInfoV1: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_PROPERTY = 3
HttpRequestPropertySni: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_PROPERTY = 4
HttpRequestPropertyStreamError: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_PROPERTY = 5
HttpRequestPropertyWskApiTimings: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_PROPERTY = 6
HttpRequestPropertyQuicApiTimings: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_PROPERTY = 7
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
HttpRequestSizingTypeTlsHandshakeLeg1ClientData: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_SIZING_TYPE = 0
HttpRequestSizingTypeTlsHandshakeLeg1ServerData: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_SIZING_TYPE = 1
HttpRequestSizingTypeTlsHandshakeLeg2ClientData: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_SIZING_TYPE = 2
HttpRequestSizingTypeTlsHandshakeLeg2ServerData: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_SIZING_TYPE = 3
HttpRequestSizingTypeHeaders: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_SIZING_TYPE = 4
HttpRequestSizingTypeMax: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_SIZING_TYPE = 5
class HTTP_REQUEST_TIMING_INFO(Structure):
    RequestTimingCount: UInt32
    RequestTiming: UInt64 * 30
HTTP_REQUEST_TIMING_TYPE = Int32
HttpRequestTimingTypeConnectionStart: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_TIMING_TYPE = 0
HttpRequestTimingTypeDataStart: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_TIMING_TYPE = 1
HttpRequestTimingTypeTlsCertificateLoadStart: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_TIMING_TYPE = 2
HttpRequestTimingTypeTlsCertificateLoadEnd: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_TIMING_TYPE = 3
HttpRequestTimingTypeTlsHandshakeLeg1Start: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_TIMING_TYPE = 4
HttpRequestTimingTypeTlsHandshakeLeg1End: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_TIMING_TYPE = 5
HttpRequestTimingTypeTlsHandshakeLeg2Start: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_TIMING_TYPE = 6
HttpRequestTimingTypeTlsHandshakeLeg2End: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_TIMING_TYPE = 7
HttpRequestTimingTypeTlsAttributesQueryStart: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_TIMING_TYPE = 8
HttpRequestTimingTypeTlsAttributesQueryEnd: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_TIMING_TYPE = 9
HttpRequestTimingTypeTlsClientCertQueryStart: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_TIMING_TYPE = 10
HttpRequestTimingTypeTlsClientCertQueryEnd: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_TIMING_TYPE = 11
HttpRequestTimingTypeHttp2StreamStart: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_TIMING_TYPE = 12
HttpRequestTimingTypeHttp2HeaderDecodeStart: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_TIMING_TYPE = 13
HttpRequestTimingTypeHttp2HeaderDecodeEnd: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_TIMING_TYPE = 14
HttpRequestTimingTypeRequestHeaderParseStart: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_TIMING_TYPE = 15
HttpRequestTimingTypeRequestHeaderParseEnd: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_TIMING_TYPE = 16
HttpRequestTimingTypeRequestRoutingStart: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_TIMING_TYPE = 17
HttpRequestTimingTypeRequestRoutingEnd: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_TIMING_TYPE = 18
HttpRequestTimingTypeRequestQueuedForInspection: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_TIMING_TYPE = 19
HttpRequestTimingTypeRequestDeliveredForInspection: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_TIMING_TYPE = 20
HttpRequestTimingTypeRequestReturnedAfterInspection: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_TIMING_TYPE = 21
HttpRequestTimingTypeRequestQueuedForDelegation: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_TIMING_TYPE = 22
HttpRequestTimingTypeRequestDeliveredForDelegation: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_TIMING_TYPE = 23
HttpRequestTimingTypeRequestReturnedAfterDelegation: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_TIMING_TYPE = 24
HttpRequestTimingTypeRequestQueuedForIO: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_TIMING_TYPE = 25
HttpRequestTimingTypeRequestDeliveredForIO: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_TIMING_TYPE = 26
HttpRequestTimingTypeHttp3StreamStart: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_TIMING_TYPE = 27
HttpRequestTimingTypeHttp3HeaderDecodeStart: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_TIMING_TYPE = 28
HttpRequestTimingTypeHttp3HeaderDecodeEnd: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_TIMING_TYPE = 29
HttpRequestTimingTypeMax: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_TIMING_TYPE = 30
class HTTP_REQUEST_TOKEN_BINDING_INFO(Structure):
    TokenBinding: POINTER(Byte)
    TokenBindingSize: UInt32
    EKM: POINTER(Byte)
    EKMSize: UInt32
    KeyType: Byte
class HTTP_REQUEST_V1(Structure):
    Flags: UInt32
    ConnectionId: UInt64
    RequestId: UInt64
    UrlContext: UInt64
    Version: win32more.Windows.Win32.Networking.HttpServer.HTTP_VERSION
    Verb: win32more.Windows.Win32.Networking.HttpServer.HTTP_VERB
    UnknownVerbLength: UInt16
    RawUrlLength: UInt16
    pUnknownVerb: win32more.Windows.Win32.Foundation.PSTR
    pRawUrl: win32more.Windows.Win32.Foundation.PSTR
    CookedUrl: win32more.Windows.Win32.Networking.HttpServer.HTTP_COOKED_URL
    Address: win32more.Windows.Win32.Networking.HttpServer.HTTP_TRANSPORT_ADDRESS
    Headers: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_HEADERS
    BytesReceived: UInt64
    EntityChunkCount: UInt16
    pEntityChunks: POINTER(win32more.Windows.Win32.Networking.HttpServer.HTTP_DATA_CHUNK)
    RawConnectionId: UInt64
    pSslInfo: POINTER(win32more.Windows.Win32.Networking.HttpServer.HTTP_SSL_INFO)
class HTTP_REQUEST_V2(Structure):
    Base: win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_V1
    RequestInfoCount: UInt16
    pRequestInfo: POINTER(win32more.Windows.Win32.Networking.HttpServer.HTTP_REQUEST_INFO)
class HTTP_RESPONSE_HEADERS(Structure):
    UnknownHeaderCount: UInt16
    pUnknownHeaders: POINTER(win32more.Windows.Win32.Networking.HttpServer.HTTP_UNKNOWN_HEADER)
    TrailerCount: UInt16
    pTrailers: POINTER(win32more.Windows.Win32.Networking.HttpServer.HTTP_UNKNOWN_HEADER)
    KnownHeaders: win32more.Windows.Win32.Networking.HttpServer.HTTP_KNOWN_HEADER * 30
class HTTP_RESPONSE_INFO(Structure):
    Type: win32more.Windows.Win32.Networking.HttpServer.HTTP_RESPONSE_INFO_TYPE
    Length: UInt32
    pInfo: VoidPtr
HTTP_RESPONSE_INFO_TYPE = Int32
HttpResponseInfoTypeMultipleKnownHeaders: win32more.Windows.Win32.Networking.HttpServer.HTTP_RESPONSE_INFO_TYPE = 0
HttpResponseInfoTypeAuthenticationProperty: win32more.Windows.Win32.Networking.HttpServer.HTTP_RESPONSE_INFO_TYPE = 1
HttpResponseInfoTypeQoSProperty: win32more.Windows.Win32.Networking.HttpServer.HTTP_RESPONSE_INFO_TYPE = 2
HttpResponseInfoTypeChannelBind: win32more.Windows.Win32.Networking.HttpServer.HTTP_RESPONSE_INFO_TYPE = 3
class HTTP_RESPONSE_V1(Structure):
    Flags: UInt32
    Version: win32more.Windows.Win32.Networking.HttpServer.HTTP_VERSION
    StatusCode: UInt16
    ReasonLength: UInt16
    pReason: win32more.Windows.Win32.Foundation.PSTR
    Headers: win32more.Windows.Win32.Networking.HttpServer.HTTP_RESPONSE_HEADERS
    EntityChunkCount: UInt16
    pEntityChunks: POINTER(win32more.Windows.Win32.Networking.HttpServer.HTTP_DATA_CHUNK)
class HTTP_RESPONSE_V2(Structure):
    Base: win32more.Windows.Win32.Networking.HttpServer.HTTP_RESPONSE_V1
    ResponseInfoCount: UInt16
    pResponseInfo: POINTER(win32more.Windows.Win32.Networking.HttpServer.HTTP_RESPONSE_INFO)
HTTP_SCHEME = Int32
HttpSchemeHttp: win32more.Windows.Win32.Networking.HttpServer.HTTP_SCHEME = 0
HttpSchemeHttps: win32more.Windows.Win32.Networking.HttpServer.HTTP_SCHEME = 1
HttpSchemeMaximum: win32more.Windows.Win32.Networking.HttpServer.HTTP_SCHEME = 2
class HTTP_SERVER_AUTHENTICATION_BASIC_PARAMS(Structure):
    RealmLength: UInt16
    Realm: win32more.Windows.Win32.Foundation.PWSTR
class HTTP_SERVER_AUTHENTICATION_DIGEST_PARAMS(Structure):
    DomainNameLength: UInt16
    DomainName: win32more.Windows.Win32.Foundation.PWSTR
    RealmLength: UInt16
    Realm: win32more.Windows.Win32.Foundation.PWSTR
class HTTP_SERVER_AUTHENTICATION_INFO(Structure):
    Flags: win32more.Windows.Win32.Networking.HttpServer.HTTP_PROPERTY_FLAGS
    AuthSchemes: UInt32
    ReceiveMutualAuth: win32more.Windows.Win32.Foundation.BOOLEAN
    ReceiveContextHandle: win32more.Windows.Win32.Foundation.BOOLEAN
    DisableNTLMCredentialCaching: win32more.Windows.Win32.Foundation.BOOLEAN
    ExFlags: Byte
    DigestParams: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVER_AUTHENTICATION_DIGEST_PARAMS
    BasicParams: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVER_AUTHENTICATION_BASIC_PARAMS
HTTP_SERVER_PROPERTY = Int32
HttpServerAuthenticationProperty: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVER_PROPERTY = 0
HttpServerLoggingProperty: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVER_PROPERTY = 1
HttpServerQosProperty: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVER_PROPERTY = 2
HttpServerTimeoutsProperty: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVER_PROPERTY = 3
HttpServerQueueLengthProperty: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVER_PROPERTY = 4
HttpServerStateProperty: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVER_PROPERTY = 5
HttpServer503VerbosityProperty: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVER_PROPERTY = 6
HttpServerBindingProperty: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVER_PROPERTY = 7
HttpServerExtendedAuthenticationProperty: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVER_PROPERTY = 8
HttpServerListenEndpointProperty: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVER_PROPERTY = 9
HttpServerChannelBindProperty: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVER_PROPERTY = 10
HttpServerProtectionLevelProperty: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVER_PROPERTY = 11
HttpServerDelegationProperty: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVER_PROPERTY = 16
class HTTP_SERVICE_BINDING_A(Structure):
    Base: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_BINDING_BASE
    Buffer: win32more.Windows.Win32.Foundation.PSTR
    BufferSize: UInt32
class HTTP_SERVICE_BINDING_BASE(Structure):
    Type: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_BINDING_TYPE
HTTP_SERVICE_BINDING_TYPE = Int32
HttpServiceBindingTypeNone: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_BINDING_TYPE = 0
HttpServiceBindingTypeW: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_BINDING_TYPE = 1
HttpServiceBindingTypeA: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_BINDING_TYPE = 2
class HTTP_SERVICE_BINDING_W(Structure):
    Base: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_BINDING_BASE
    Buffer: win32more.Windows.Win32.Foundation.PWSTR
    BufferSize: UInt32
HTTP_SERVICE_BINDING = UnicodeAlias('HTTP_SERVICE_BINDING_W')
HTTP_SERVICE_CONFIG_CACHE_KEY = Int32
MaxCacheResponseSize: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_CACHE_KEY = 0
CacheRangeChunkSize: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_CACHE_KEY = 1
class HTTP_SERVICE_CONFIG_CACHE_SET(Structure):
    KeyDesc: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_CACHE_KEY
    ParamDesc: UInt32
HTTP_SERVICE_CONFIG_ID = Int32
HttpServiceConfigIPListenList: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_ID = 0
HttpServiceConfigSSLCertInfo: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_ID = 1
HttpServiceConfigUrlAclInfo: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_ID = 2
HttpServiceConfigTimeout: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_ID = 3
HttpServiceConfigCache: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_ID = 4
HttpServiceConfigSslSniCertInfo: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_ID = 5
HttpServiceConfigSslCcsCertInfo: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_ID = 6
HttpServiceConfigSetting: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_ID = 7
HttpServiceConfigSslCertInfoEx: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_ID = 8
HttpServiceConfigSslSniCertInfoEx: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_ID = 9
HttpServiceConfigSslCcsCertInfoEx: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_ID = 10
HttpServiceConfigSslScopedCcsCertInfo: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_ID = 11
HttpServiceConfigSslScopedCcsCertInfoEx: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_ID = 12
HttpServiceConfigMax: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_ID = 13
class HTTP_SERVICE_CONFIG_IP_LISTEN_PARAM(Structure):
    AddrLength: UInt16
    pAddress: POINTER(win32more.Windows.Win32.Networking.WinSock.SOCKADDR)
class HTTP_SERVICE_CONFIG_IP_LISTEN_QUERY(Structure):
    AddrCount: UInt32
    AddrList: win32more.Windows.Win32.Networking.WinSock.SOCKADDR_STORAGE * 1
HTTP_SERVICE_CONFIG_QUERY_TYPE = Int32
HttpServiceConfigQueryExact: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_QUERY_TYPE = 0
HttpServiceConfigQueryNext: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_QUERY_TYPE = 1
HttpServiceConfigQueryMax: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_QUERY_TYPE = 2
HTTP_SERVICE_CONFIG_SETTING_KEY = Int32
HttpNone: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SETTING_KEY = 0
HttpTlsThrottle: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SETTING_KEY = 1
class HTTP_SERVICE_CONFIG_SETTING_SET(Structure):
    KeyDesc: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SETTING_KEY
    ParamDesc: UInt32
class HTTP_SERVICE_CONFIG_SSL_CCS_KEY(Structure):
    LocalAddress: win32more.Windows.Win32.Networking.WinSock.SOCKADDR_STORAGE
class HTTP_SERVICE_CONFIG_SSL_CCS_QUERY(Structure):
    QueryDesc: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_QUERY_TYPE
    KeyDesc: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_CCS_KEY
    dwToken: UInt32
class HTTP_SERVICE_CONFIG_SSL_CCS_QUERY_EX(Structure):
    QueryDesc: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_QUERY_TYPE
    KeyDesc: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_CCS_KEY
    dwToken: UInt32
    ParamType: win32more.Windows.Win32.Networking.HttpServer.HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE
class HTTP_SERVICE_CONFIG_SSL_CCS_SET(Structure):
    KeyDesc: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_CCS_KEY
    ParamDesc: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_PARAM
class HTTP_SERVICE_CONFIG_SSL_CCS_SET_EX(Structure):
    KeyDesc: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_CCS_KEY
    ParamDesc: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_PARAM_EX
class HTTP_SERVICE_CONFIG_SSL_KEY(Structure):
    pIpPort: POINTER(win32more.Windows.Win32.Networking.WinSock.SOCKADDR)
class HTTP_SERVICE_CONFIG_SSL_KEY_EX(Structure):
    IpPort: win32more.Windows.Win32.Networking.WinSock.SOCKADDR_STORAGE
class HTTP_SERVICE_CONFIG_SSL_PARAM(Structure):
    SslHashLength: UInt32
    pSslHash: VoidPtr
    AppId: Guid
    pSslCertStoreName: win32more.Windows.Win32.Foundation.PWSTR
    DefaultCertCheckMode: UInt32
    DefaultRevocationFreshnessTime: UInt32
    DefaultRevocationUrlRetrievalTimeout: UInt32
    pDefaultSslCtlIdentifier: win32more.Windows.Win32.Foundation.PWSTR
    pDefaultSslCtlStoreName: win32more.Windows.Win32.Foundation.PWSTR
    DefaultFlags: UInt32
class HTTP_SERVICE_CONFIG_SSL_PARAM_EX(Structure):
    ParamType: win32more.Windows.Win32.Networking.HttpServer.HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE
    Flags: UInt64
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(Union):
        Http2WindowSizeParam: win32more.Windows.Win32.Networking.HttpServer.HTTP2_WINDOW_SIZE_PARAM
        Http2SettingsLimitsParam: win32more.Windows.Win32.Networking.HttpServer.HTTP2_SETTINGS_LIMITS_PARAM
        HttpPerformanceParam: win32more.Windows.Win32.Networking.HttpServer.HTTP_PERFORMANCE_PARAM
        HttpTlsRestrictionsParam: win32more.Windows.Win32.Networking.HttpServer.HTTP_TLS_RESTRICTIONS_PARAM
        HttpErrorHeadersParam: win32more.Windows.Win32.Networking.HttpServer.HTTP_ERROR_HEADERS_PARAM
        HttpTlsSessionTicketKeysParam: win32more.Windows.Win32.Networking.HttpServer.HTTP_TLS_SESSION_TICKET_KEYS_PARAM
class HTTP_SERVICE_CONFIG_SSL_QUERY(Structure):
    QueryDesc: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_QUERY_TYPE
    KeyDesc: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_KEY
    dwToken: UInt32
class HTTP_SERVICE_CONFIG_SSL_QUERY_EX(Structure):
    QueryDesc: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_QUERY_TYPE
    KeyDesc: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_KEY_EX
    dwToken: UInt32
    ParamType: win32more.Windows.Win32.Networking.HttpServer.HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE
class HTTP_SERVICE_CONFIG_SSL_SET(Structure):
    KeyDesc: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_KEY
    ParamDesc: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_PARAM
class HTTP_SERVICE_CONFIG_SSL_SET_EX(Structure):
    KeyDesc: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_KEY_EX
    ParamDesc: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_PARAM_EX
class HTTP_SERVICE_CONFIG_SSL_SNI_KEY(Structure):
    IpPort: win32more.Windows.Win32.Networking.WinSock.SOCKADDR_STORAGE
    Host: win32more.Windows.Win32.Foundation.PWSTR
class HTTP_SERVICE_CONFIG_SSL_SNI_QUERY(Structure):
    QueryDesc: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_QUERY_TYPE
    KeyDesc: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_SNI_KEY
    dwToken: UInt32
class HTTP_SERVICE_CONFIG_SSL_SNI_QUERY_EX(Structure):
    QueryDesc: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_QUERY_TYPE
    KeyDesc: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_SNI_KEY
    dwToken: UInt32
    ParamType: win32more.Windows.Win32.Networking.HttpServer.HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE
class HTTP_SERVICE_CONFIG_SSL_SNI_SET(Structure):
    KeyDesc: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_SNI_KEY
    ParamDesc: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_PARAM
class HTTP_SERVICE_CONFIG_SSL_SNI_SET_EX(Structure):
    KeyDesc: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_SNI_KEY
    ParamDesc: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_SSL_PARAM_EX
HTTP_SERVICE_CONFIG_TIMEOUT_KEY = Int32
IdleConnectionTimeout: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_TIMEOUT_KEY = 0
HeaderWaitTimeout: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_TIMEOUT_KEY = 1
class HTTP_SERVICE_CONFIG_TIMEOUT_SET(Structure):
    KeyDesc: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_TIMEOUT_KEY
    ParamDesc: UInt16
class HTTP_SERVICE_CONFIG_URLACL_KEY(Structure):
    pUrlPrefix: win32more.Windows.Win32.Foundation.PWSTR
class HTTP_SERVICE_CONFIG_URLACL_PARAM(Structure):
    pStringSecurityDescriptor: win32more.Windows.Win32.Foundation.PWSTR
class HTTP_SERVICE_CONFIG_URLACL_QUERY(Structure):
    QueryDesc: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_QUERY_TYPE
    KeyDesc: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_URLACL_KEY
    dwToken: UInt32
class HTTP_SERVICE_CONFIG_URLACL_SET(Structure):
    KeyDesc: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_URLACL_KEY
    ParamDesc: win32more.Windows.Win32.Networking.HttpServer.HTTP_SERVICE_CONFIG_URLACL_PARAM
class HTTP_SSL_CLIENT_CERT_INFO(Structure):
    CertFlags: UInt32
    CertEncodedSize: UInt32
    pCertEncoded: POINTER(Byte)
    Token: win32more.Windows.Win32.Foundation.HANDLE
    CertDeniedByMapper: win32more.Windows.Win32.Foundation.BOOLEAN
class HTTP_SSL_INFO(Structure):
    ServerCertKeySize: UInt16
    ConnectionKeySize: UInt16
    ServerCertIssuerSize: UInt32
    ServerCertSubjectSize: UInt32
    pServerCertIssuer: win32more.Windows.Win32.Foundation.PSTR
    pServerCertSubject: win32more.Windows.Win32.Foundation.PSTR
    pClientCertInfo: POINTER(win32more.Windows.Win32.Networking.HttpServer.HTTP_SSL_CLIENT_CERT_INFO)
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
ExParamTypeHttp2Window: win32more.Windows.Win32.Networking.HttpServer.HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE = 0
ExParamTypeHttp2SettingsLimits: win32more.Windows.Win32.Networking.HttpServer.HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE = 1
ExParamTypeHttpPerformance: win32more.Windows.Win32.Networking.HttpServer.HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE = 2
ExParamTypeTlsRestrictions: win32more.Windows.Win32.Networking.HttpServer.HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE = 3
ExParamTypeErrorHeaders: win32more.Windows.Win32.Networking.HttpServer.HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE = 4
ExParamTypeTlsSessionTicketKeys: win32more.Windows.Win32.Networking.HttpServer.HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE = 5
ExParamTypeMax: win32more.Windows.Win32.Networking.HttpServer.HTTP_SSL_SERVICE_CONFIG_EX_PARAM_TYPE = 6
class HTTP_STATE_INFO(Structure):
    Flags: win32more.Windows.Win32.Networking.HttpServer.HTTP_PROPERTY_FLAGS
    State: win32more.Windows.Win32.Networking.HttpServer.HTTP_ENABLED_STATE
class HTTP_TIMEOUT_LIMIT_INFO(Structure):
    Flags: win32more.Windows.Win32.Networking.HttpServer.HTTP_PROPERTY_FLAGS
    EntityBody: UInt16
    DrainEntityBody: UInt16
    RequestQueue: UInt16
    IdleConnection: UInt16
    HeaderWait: UInt16
    MinSendRate: UInt32
class HTTP_TLS_RESTRICTIONS_PARAM(Structure):
    RestrictionCount: UInt32
    TlsRestrictions: VoidPtr
class HTTP_TLS_SESSION_TICKET_KEYS_PARAM(Structure):
    SessionTicketKeyCount: UInt32
    SessionTicketKeys: VoidPtr
class HTTP_TRANSPORT_ADDRESS(Structure):
    pRemoteAddress: POINTER(win32more.Windows.Win32.Networking.WinSock.SOCKADDR)
    pLocalAddress: POINTER(win32more.Windows.Win32.Networking.WinSock.SOCKADDR)
class HTTP_UNKNOWN_HEADER(Structure):
    NameLength: UInt16
    RawValueLength: UInt16
    pName: win32more.Windows.Win32.Foundation.PSTR
    pRawValue: win32more.Windows.Win32.Foundation.PSTR
HTTP_VERB = Int32
HttpVerbUnparsed: win32more.Windows.Win32.Networking.HttpServer.HTTP_VERB = 0
HttpVerbUnknown: win32more.Windows.Win32.Networking.HttpServer.HTTP_VERB = 1
HttpVerbInvalid: win32more.Windows.Win32.Networking.HttpServer.HTTP_VERB = 2
HttpVerbOPTIONS: win32more.Windows.Win32.Networking.HttpServer.HTTP_VERB = 3
HttpVerbGET: win32more.Windows.Win32.Networking.HttpServer.HTTP_VERB = 4
HttpVerbHEAD: win32more.Windows.Win32.Networking.HttpServer.HTTP_VERB = 5
HttpVerbPOST: win32more.Windows.Win32.Networking.HttpServer.HTTP_VERB = 6
HttpVerbPUT: win32more.Windows.Win32.Networking.HttpServer.HTTP_VERB = 7
HttpVerbDELETE: win32more.Windows.Win32.Networking.HttpServer.HTTP_VERB = 8
HttpVerbTRACE: win32more.Windows.Win32.Networking.HttpServer.HTTP_VERB = 9
HttpVerbCONNECT: win32more.Windows.Win32.Networking.HttpServer.HTTP_VERB = 10
HttpVerbTRACK: win32more.Windows.Win32.Networking.HttpServer.HTTP_VERB = 11
HttpVerbMOVE: win32more.Windows.Win32.Networking.HttpServer.HTTP_VERB = 12
HttpVerbCOPY: win32more.Windows.Win32.Networking.HttpServer.HTTP_VERB = 13
HttpVerbPROPFIND: win32more.Windows.Win32.Networking.HttpServer.HTTP_VERB = 14
HttpVerbPROPPATCH: win32more.Windows.Win32.Networking.HttpServer.HTTP_VERB = 15
HttpVerbMKCOL: win32more.Windows.Win32.Networking.HttpServer.HTTP_VERB = 16
HttpVerbLOCK: win32more.Windows.Win32.Networking.HttpServer.HTTP_VERB = 17
HttpVerbUNLOCK: win32more.Windows.Win32.Networking.HttpServer.HTTP_VERB = 18
HttpVerbSEARCH: win32more.Windows.Win32.Networking.HttpServer.HTTP_VERB = 19
HttpVerbMaximum: win32more.Windows.Win32.Networking.HttpServer.HTTP_VERB = 20
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


make_ready(__name__)
