from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Networking.WindowsWebServices
import win32more.Security.Authentication.Identity
import win32more.Security.Cryptography
import win32more.System.WinRT
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
WEBAUTHN_API_VERSION_1 = 1
WEBAUTHN_API_VERSION_2 = 2
WEBAUTHN_API_VERSION_3 = 3
WEBAUTHN_API_CURRENT_VERSION = 3
WEBAUTHN_RP_ENTITY_INFORMATION_CURRENT_VERSION = 1
WEBAUTHN_MAX_USER_ID_LENGTH = 64
WEBAUTHN_USER_ENTITY_INFORMATION_CURRENT_VERSION = 1
WEBAUTHN_HASH_ALGORITHM_SHA_256 = 'SHA-256'
WEBAUTHN_HASH_ALGORITHM_SHA_384 = 'SHA-384'
WEBAUTHN_HASH_ALGORITHM_SHA_512 = 'SHA-512'
WEBAUTHN_CLIENT_DATA_CURRENT_VERSION = 1
WEBAUTHN_CREDENTIAL_TYPE_PUBLIC_KEY = 'public-key'
WEBAUTHN_COSE_ALGORITHM_ECDSA_P256_WITH_SHA256 = -7
WEBAUTHN_COSE_ALGORITHM_ECDSA_P384_WITH_SHA384 = -35
WEBAUTHN_COSE_ALGORITHM_ECDSA_P521_WITH_SHA512 = -36
WEBAUTHN_COSE_ALGORITHM_RSASSA_PKCS1_V1_5_WITH_SHA256 = -257
WEBAUTHN_COSE_ALGORITHM_RSASSA_PKCS1_V1_5_WITH_SHA384 = -258
WEBAUTHN_COSE_ALGORITHM_RSASSA_PKCS1_V1_5_WITH_SHA512 = -259
WEBAUTHN_COSE_ALGORITHM_RSA_PSS_WITH_SHA256 = -37
WEBAUTHN_COSE_ALGORITHM_RSA_PSS_WITH_SHA384 = -38
WEBAUTHN_COSE_ALGORITHM_RSA_PSS_WITH_SHA512 = -39
WEBAUTHN_COSE_CREDENTIAL_PARAMETER_CURRENT_VERSION = 1
WEBAUTHN_CREDENTIAL_CURRENT_VERSION = 1
WEBAUTHN_CTAP_TRANSPORT_USB = 1
WEBAUTHN_CTAP_TRANSPORT_NFC = 2
WEBAUTHN_CTAP_TRANSPORT_BLE = 4
WEBAUTHN_CTAP_TRANSPORT_TEST = 8
WEBAUTHN_CTAP_TRANSPORT_INTERNAL = 16
WEBAUTHN_CTAP_TRANSPORT_FLAGS_MASK = 31
WEBAUTHN_CREDENTIAL_EX_CURRENT_VERSION = 1
WEBAUTHN_EXTENSIONS_IDENTIFIER_HMAC_SECRET = 'hmac-secret'
WEBAUTHN_USER_VERIFICATION_ANY = 0
WEBAUTHN_USER_VERIFICATION_OPTIONAL = 1
WEBAUTHN_USER_VERIFICATION_OPTIONAL_WITH_CREDENTIAL_ID_LIST = 2
WEBAUTHN_USER_VERIFICATION_REQUIRED = 3
WEBAUTHN_EXTENSIONS_IDENTIFIER_CRED_PROTECT = 'credProtect'
WEBAUTHN_EXTENSIONS_IDENTIFIER_CRED_BLOB = 'credBlob'
WEBAUTHN_EXTENSIONS_IDENTIFIER_MIN_PIN_LENGTH = 'minPinLength'
WEBAUTHN_AUTHENTICATOR_ATTACHMENT_ANY = 0
WEBAUTHN_AUTHENTICATOR_ATTACHMENT_PLATFORM = 1
WEBAUTHN_AUTHENTICATOR_ATTACHMENT_CROSS_PLATFORM = 2
WEBAUTHN_AUTHENTICATOR_ATTACHMENT_CROSS_PLATFORM_U2F_V2 = 3
WEBAUTHN_USER_VERIFICATION_REQUIREMENT_ANY = 0
WEBAUTHN_USER_VERIFICATION_REQUIREMENT_REQUIRED = 1
WEBAUTHN_USER_VERIFICATION_REQUIREMENT_PREFERRED = 2
WEBAUTHN_USER_VERIFICATION_REQUIREMENT_DISCOURAGED = 3
WEBAUTHN_ATTESTATION_CONVEYANCE_PREFERENCE_ANY = 0
WEBAUTHN_ATTESTATION_CONVEYANCE_PREFERENCE_NONE = 1
WEBAUTHN_ATTESTATION_CONVEYANCE_PREFERENCE_INDIRECT = 2
WEBAUTHN_ATTESTATION_CONVEYANCE_PREFERENCE_DIRECT = 3
WEBAUTHN_ENTERPRISE_ATTESTATION_NONE = 0
WEBAUTHN_ENTERPRISE_ATTESTATION_VENDOR_FACILITATED = 1
WEBAUTHN_ENTERPRISE_ATTESTATION_PLATFORM_MANAGED = 2
WEBAUTHN_LARGE_BLOB_SUPPORT_NONE = 0
WEBAUTHN_LARGE_BLOB_SUPPORT_REQUIRED = 1
WEBAUTHN_LARGE_BLOB_SUPPORT_PREFERRED = 2
WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_VERSION_1 = 1
WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_VERSION_2 = 2
WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_VERSION_3 = 3
WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_VERSION_4 = 4
WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_CURRENT_VERSION = 4
WEBAUTHN_CRED_LARGE_BLOB_OPERATION_NONE = 0
WEBAUTHN_CRED_LARGE_BLOB_OPERATION_GET = 1
WEBAUTHN_CRED_LARGE_BLOB_OPERATION_SET = 2
WEBAUTHN_CRED_LARGE_BLOB_OPERATION_DELETE = 3
WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_VERSION_1 = 1
WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_VERSION_2 = 2
WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_VERSION_3 = 3
WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_VERSION_4 = 4
WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_VERSION_5 = 5
WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_CURRENT_VERSION = 5
WEBAUTHN_ATTESTATION_DECODE_NONE = 0
WEBAUTHN_ATTESTATION_DECODE_COMMON = 1
WEBAUTHN_ATTESTATION_VER_TPM_2_0 = '2.0'
WEBAUTHN_COMMON_ATTESTATION_CURRENT_VERSION = 1
WEBAUTHN_ATTESTATION_TYPE_PACKED = 'packed'
WEBAUTHN_ATTESTATION_TYPE_U2F = 'fido-u2f'
WEBAUTHN_ATTESTATION_TYPE_TPM = 'tpm'
WEBAUTHN_ATTESTATION_TYPE_NONE = 'none'
WEBAUTHN_CREDENTIAL_ATTESTATION_VERSION_1 = 1
WEBAUTHN_CREDENTIAL_ATTESTATION_VERSION_2 = 2
WEBAUTHN_CREDENTIAL_ATTESTATION_VERSION_3 = 3
WEBAUTHN_CREDENTIAL_ATTESTATION_VERSION_4 = 4
WEBAUTHN_CREDENTIAL_ATTESTATION_CURRENT_VERSION = 4
WEBAUTHN_CRED_LARGE_BLOB_STATUS_NONE = 0
WEBAUTHN_CRED_LARGE_BLOB_STATUS_SUCCESS = 1
WEBAUTHN_CRED_LARGE_BLOB_STATUS_NOT_SUPPORTED = 2
WEBAUTHN_CRED_LARGE_BLOB_STATUS_INVALID_DATA = 3
WEBAUTHN_CRED_LARGE_BLOB_STATUS_INVALID_PARAMETER = 4
WEBAUTHN_CRED_LARGE_BLOB_STATUS_NOT_FOUND = 5
WEBAUTHN_CRED_LARGE_BLOB_STATUS_MULTIPLE_CREDENTIALS = 6
WEBAUTHN_CRED_LARGE_BLOB_STATUS_LACK_OF_SPACE = 7
WEBAUTHN_CRED_LARGE_BLOB_STATUS_PLATFORM_ERROR = 8
WEBAUTHN_CRED_LARGE_BLOB_STATUS_AUTHENTICATOR_ERROR = 9
WEBAUTHN_ASSERTION_VERSION_1 = 1
WEBAUTHN_ASSERTION_VERSION_2 = 2
WEBAUTHN_ASSERTION_CURRENT_VERSION = 2
WS_HTTP_HEADER_MAPPING_COMMA_SEPARATOR = 1
WS_HTTP_HEADER_MAPPING_SEMICOLON_SEPARATOR = 2
WS_HTTP_HEADER_MAPPING_QUOTED_VALUE = 4
WS_HTTP_RESPONSE_MAPPING_STATUS_CODE = 1
WS_HTTP_RESPONSE_MAPPING_STATUS_TEXT = 2
WS_HTTP_REQUEST_MAPPING_VERB = 2
WS_MATCH_URL_DNS_HOST = 1
WS_MATCH_URL_DNS_FULLY_QUALIFIED_HOST = 2
WS_MATCH_URL_NETBIOS_HOST = 4
WS_MATCH_URL_LOCAL_HOST = 8
WS_MATCH_URL_HOST_ADDRESSES = 16
WS_MATCH_URL_THIS_HOST = 31
WS_MATCH_URL_PORT = 32
WS_MATCH_URL_EXACT_PATH = 64
WS_MATCH_URL_PREFIX_PATH = 128
WS_MATCH_URL_NO_QUERY = 256
WS_MUST_UNDERSTAND_HEADER_ATTRIBUTE = 1
WS_RELAY_HEADER_ATTRIBUTE = 2
WS_HTTP_HEADER_AUTH_SCHEME_NONE = 1
WS_HTTP_HEADER_AUTH_SCHEME_BASIC = 2
WS_HTTP_HEADER_AUTH_SCHEME_DIGEST = 4
WS_HTTP_HEADER_AUTH_SCHEME_NTLM = 8
WS_HTTP_HEADER_AUTH_SCHEME_NEGOTIATE = 16
WS_HTTP_HEADER_AUTH_SCHEME_PASSPORT = 32
WS_CERT_FAILURE_CN_MISMATCH = 1
WS_CERT_FAILURE_INVALID_DATE = 2
WS_CERT_FAILURE_UNTRUSTED_ROOT = 4
WS_CERT_FAILURE_WRONG_USAGE = 8
WS_CERT_FAILURE_REVOCATION_OFFLINE = 16
WS_STRUCT_ABSTRACT = 1
WS_STRUCT_IGNORE_TRAILING_ELEMENT_CONTENT = 2
WS_STRUCT_IGNORE_UNHANDLED_ATTRIBUTES = 4
WS_FIELD_POINTER = 1
WS_FIELD_OPTIONAL = 2
WS_FIELD_NILLABLE = 4
WS_FIELD_NILLABLE_ITEM = 8
WS_FIELD_OTHER_NAMESPACE = 16
WS_SERVICE_OPERATION_MESSAGE_NILLABLE_ELEMENT = 1
WS_URL_FLAGS_ALLOW_HOST_WILDCARDS = 1
WS_URL_FLAGS_NO_PATH_COLLAPSE = 2
WS_URL_FLAGS_ZERO_TERMINATE = 4
def _define_WsStartReaderCanonicalization():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),win32more.Networking.WindowsWebServices.WS_WRITE_CALLBACK,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_XML_CANONICALIZATION_PROPERTY_head),UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsStartReaderCanonicalization', windll['webservices.dll']), ((1, 'reader'),(1, 'writeCallback'),(1, 'writeCallbackState'),(1, 'properties'),(1, 'propertyCount'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsEndReaderCanonicalization():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsEndReaderCanonicalization', windll['webservices.dll']), ((1, 'reader'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsStartWriterCanonicalization():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),win32more.Networking.WindowsWebServices.WS_WRITE_CALLBACK,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_XML_CANONICALIZATION_PROPERTY_head),UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsStartWriterCanonicalization', windll['webservices.dll']), ((1, 'writer'),(1, 'writeCallback'),(1, 'writeCallbackState'),(1, 'properties'),(1, 'propertyCount'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsEndWriterCanonicalization():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsEndWriterCanonicalization', windll['webservices.dll']), ((1, 'writer'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsCreateXmlBuffer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_BUFFER_PROPERTY_head),UInt32,POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_XML_BUFFER_head)),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsCreateXmlBuffer', windll['webservices.dll']), ((1, 'heap'),(1, 'properties'),(1, 'propertyCount'),(1, 'buffer'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsRemoveNode():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_NODE_POSITION_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsRemoveNode', windll['webservices.dll']), ((1, 'nodePosition'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsCreateReader():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_head),UInt32,POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head)),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsCreateReader', windll['webservices.dll']), ((1, 'properties'),(1, 'propertyCount'),(1, 'reader'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsSetInput():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_ENCODING_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_INPUT_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_head),UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsSetInput', windll['webservices.dll']), ((1, 'reader'),(1, 'encoding'),(1, 'input'),(1, 'properties'),(1, 'propertyCount'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsSetInputToBuffer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_BUFFER_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_head),UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsSetInputToBuffer', windll['webservices.dll']), ((1, 'reader'),(1, 'buffer'),(1, 'properties'),(1, 'propertyCount'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsFreeReader():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head))(('WsFreeReader', windll['webservices.dll']), ((1, 'reader'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsGetReaderProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),win32more.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_ID,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsGetReaderProperty', windll['webservices.dll']), ((1, 'reader'),(1, 'id'),(1, 'value'),(1, 'valueSize'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsGetReaderNode():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_XML_NODE_head)),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsGetReaderNode', windll['webservices.dll']), ((1, 'xmlReader'),(1, 'node'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsFillReader():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsFillReader', windll['webservices.dll']), ((1, 'reader'),(1, 'minSize'),(1, 'asyncContext'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsReadStartElement():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsReadStartElement', windll['webservices.dll']), ((1, 'reader'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsReadToStartElement():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),POINTER(win32more.Foundation.BOOL),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsReadToStartElement', windll['webservices.dll']), ((1, 'reader'),(1, 'localName'),(1, 'ns'),(1, 'found'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsReadStartAttribute():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsReadStartAttribute', windll['webservices.dll']), ((1, 'reader'),(1, 'attributeIndex'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsReadEndAttribute():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsReadEndAttribute', windll['webservices.dll']), ((1, 'reader'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsReadNode():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsReadNode', windll['webservices.dll']), ((1, 'reader'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsSkipNode():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsSkipNode', windll['webservices.dll']), ((1, 'reader'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsReadEndElement():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsReadEndElement', windll['webservices.dll']), ((1, 'reader'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsFindAttribute():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),win32more.Foundation.BOOL,POINTER(UInt32),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsFindAttribute', windll['webservices.dll']), ((1, 'reader'),(1, 'localName'),(1, 'ns'),(1, 'required'),(1, 'attributeIndex'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsReadValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),win32more.Networking.WindowsWebServices.WS_VALUE_TYPE,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsReadValue', windll['webservices.dll']), ((1, 'reader'),(1, 'valueType'),(1, 'value'),(1, 'valueSize'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsReadChars():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsReadChars', windll['webservices.dll']), ((1, 'reader'),(1, 'chars'),(1, 'maxCharCount'),(1, 'actualCharCount'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsReadCharsUtf8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),c_char_p_no,UInt32,POINTER(UInt32),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsReadCharsUtf8', windll['webservices.dll']), ((1, 'reader'),(1, 'bytes'),(1, 'maxByteCount'),(1, 'actualByteCount'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsReadBytes():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),c_void_p,UInt32,POINTER(UInt32),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsReadBytes', windll['webservices.dll']), ((1, 'reader'),(1, 'bytes'),(1, 'maxByteCount'),(1, 'actualByteCount'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsReadArray():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),win32more.Networking.WindowsWebServices.WS_VALUE_TYPE,c_void_p,UInt32,UInt32,UInt32,POINTER(UInt32),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsReadArray', windll['webservices.dll']), ((1, 'reader'),(1, 'localName'),(1, 'ns'),(1, 'valueType'),(1, 'array'),(1, 'arraySize'),(1, 'itemOffset'),(1, 'itemCount'),(1, 'actualItemCount'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsGetReaderPosition():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_NODE_POSITION_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsGetReaderPosition', windll['webservices.dll']), ((1, 'reader'),(1, 'nodePosition'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsSetReaderPosition():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_NODE_POSITION_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsSetReaderPosition', windll['webservices.dll']), ((1, 'reader'),(1, 'nodePosition'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsMoveReader():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),win32more.Networking.WindowsWebServices.WS_MOVE_TO,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsMoveReader', windll['webservices.dll']), ((1, 'reader'),(1, 'moveTo'),(1, 'found'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsCreateWriter():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_head),UInt32,POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head)),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsCreateWriter', windll['webservices.dll']), ((1, 'properties'),(1, 'propertyCount'),(1, 'writer'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsFreeWriter():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head))(('WsFreeWriter', windll['webservices.dll']), ((1, 'writer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsSetOutput():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_ENCODING_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_OUTPUT_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_head),UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsSetOutput', windll['webservices.dll']), ((1, 'writer'),(1, 'encoding'),(1, 'output'),(1, 'properties'),(1, 'propertyCount'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsSetOutputToBuffer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_BUFFER_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_head),UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsSetOutputToBuffer', windll['webservices.dll']), ((1, 'writer'),(1, 'buffer'),(1, 'properties'),(1, 'propertyCount'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsGetWriterProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),win32more.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_ID,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsGetWriterProperty', windll['webservices.dll']), ((1, 'writer'),(1, 'id'),(1, 'value'),(1, 'valueSize'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsFlushWriter():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsFlushWriter', windll['webservices.dll']), ((1, 'writer'),(1, 'minSize'),(1, 'asyncContext'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsWriteStartElement():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsWriteStartElement', windll['webservices.dll']), ((1, 'writer'),(1, 'prefix'),(1, 'localName'),(1, 'ns'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsWriteEndStartElement():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsWriteEndStartElement', windll['webservices.dll']), ((1, 'writer'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsWriteXmlnsAttribute():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),win32more.Foundation.BOOL,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsWriteXmlnsAttribute', windll['webservices.dll']), ((1, 'writer'),(1, 'prefix'),(1, 'ns'),(1, 'singleQuote'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsWriteStartAttribute():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),win32more.Foundation.BOOL,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsWriteStartAttribute', windll['webservices.dll']), ((1, 'writer'),(1, 'prefix'),(1, 'localName'),(1, 'ns'),(1, 'singleQuote'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsWriteEndAttribute():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsWriteEndAttribute', windll['webservices.dll']), ((1, 'writer'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsWriteValue():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),win32more.Networking.WindowsWebServices.WS_VALUE_TYPE,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsWriteValue', windll['webservices.dll']), ((1, 'writer'),(1, 'valueType'),(1, 'value'),(1, 'valueSize'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsWriteXmlBuffer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_BUFFER_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsWriteXmlBuffer', windll['webservices.dll']), ((1, 'writer'),(1, 'xmlBuffer'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsReadXmlBuffer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head),POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_XML_BUFFER_head)),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsReadXmlBuffer', windll['webservices.dll']), ((1, 'reader'),(1, 'heap'),(1, 'xmlBuffer'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsWriteXmlBufferToBytes():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_BUFFER_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_ENCODING_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_head),UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head),POINTER(c_void_p),POINTER(UInt32),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsWriteXmlBufferToBytes', windll['webservices.dll']), ((1, 'writer'),(1, 'xmlBuffer'),(1, 'encoding'),(1, 'properties'),(1, 'propertyCount'),(1, 'heap'),(1, 'bytes'),(1, 'byteCount'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsReadXmlBufferFromBytes():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_ENCODING_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_head),UInt32,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head),POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_XML_BUFFER_head)),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsReadXmlBufferFromBytes', windll['webservices.dll']), ((1, 'reader'),(1, 'encoding'),(1, 'properties'),(1, 'propertyCount'),(1, 'bytes'),(1, 'byteCount'),(1, 'heap'),(1, 'xmlBuffer'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsWriteArray():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),win32more.Networking.WindowsWebServices.WS_VALUE_TYPE,c_void_p,UInt32,UInt32,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsWriteArray', windll['webservices.dll']), ((1, 'writer'),(1, 'localName'),(1, 'ns'),(1, 'valueType'),(1, 'array'),(1, 'arraySize'),(1, 'itemOffset'),(1, 'itemCount'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsWriteQualifiedName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsWriteQualifiedName', windll['webservices.dll']), ((1, 'writer'),(1, 'prefix'),(1, 'localName'),(1, 'ns'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsWriteChars():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsWriteChars', windll['webservices.dll']), ((1, 'writer'),(1, 'chars'),(1, 'charCount'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsWriteCharsUtf8():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),c_char_p_no,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsWriteCharsUtf8', windll['webservices.dll']), ((1, 'writer'),(1, 'bytes'),(1, 'byteCount'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsWriteBytes():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsWriteBytes', windll['webservices.dll']), ((1, 'writer'),(1, 'bytes'),(1, 'byteCount'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsPushBytes():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),win32more.Networking.WindowsWebServices.WS_PUSH_BYTES_CALLBACK,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsPushBytes', windll['webservices.dll']), ((1, 'writer'),(1, 'callback'),(1, 'callbackState'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsPullBytes():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),win32more.Networking.WindowsWebServices.WS_PULL_BYTES_CALLBACK,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsPullBytes', windll['webservices.dll']), ((1, 'writer'),(1, 'callback'),(1, 'callbackState'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsWriteEndElement():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsWriteEndElement', windll['webservices.dll']), ((1, 'writer'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsWriteText():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_TEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsWriteText', windll['webservices.dll']), ((1, 'writer'),(1, 'text'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsWriteStartCData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsWriteStartCData', windll['webservices.dll']), ((1, 'writer'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsWriteEndCData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsWriteEndCData', windll['webservices.dll']), ((1, 'writer'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsWriteNode():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_NODE_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsWriteNode', windll['webservices.dll']), ((1, 'writer'),(1, 'node'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsGetPrefixFromNamespace():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),win32more.Foundation.BOOL,POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsGetPrefixFromNamespace', windll['webservices.dll']), ((1, 'writer'),(1, 'ns'),(1, 'required'),(1, 'prefix'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsGetWriterPosition():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_NODE_POSITION_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsGetWriterPosition', windll['webservices.dll']), ((1, 'writer'),(1, 'nodePosition'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsSetWriterPosition():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_NODE_POSITION_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsSetWriterPosition', windll['webservices.dll']), ((1, 'writer'),(1, 'nodePosition'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsMoveWriter():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),win32more.Networking.WindowsWebServices.WS_MOVE_TO,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsMoveWriter', windll['webservices.dll']), ((1, 'writer'),(1, 'moveTo'),(1, 'found'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsTrimXmlWhitespace():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(POINTER(UInt16)),POINTER(UInt32),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsTrimXmlWhitespace', windll['webservices.dll']), ((1, 'chars'),(1, 'charCount'),(1, 'trimmedChars'),(1, 'trimmedCount'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsVerifyXmlNCName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsVerifyXmlNCName', windll['webservices.dll']), ((1, 'ncNameChars'),(1, 'ncNameCharCount'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsXmlStringEquals():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsXmlStringEquals', windll['webservices.dll']), ((1, 'string1'),(1, 'string2'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsGetNamespaceFromPrefix():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),win32more.Foundation.BOOL,POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsGetNamespaceFromPrefix', windll['webservices.dll']), ((1, 'reader'),(1, 'prefix'),(1, 'required'),(1, 'ns'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsReadQualifiedName():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsReadQualifiedName', windll['webservices.dll']), ((1, 'reader'),(1, 'heap'),(1, 'prefix'),(1, 'localName'),(1, 'ns'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsGetXmlAttribute():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head),POINTER(POINTER(UInt16)),POINTER(UInt32),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsGetXmlAttribute', windll['webservices.dll']), ((1, 'reader'),(1, 'localName'),(1, 'heap'),(1, 'valueChars'),(1, 'valueCharCount'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsCopyNode():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsCopyNode', windll['webservices.dll']), ((1, 'writer'),(1, 'reader'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsAsyncExecute():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_STATE_head),win32more.Networking.WindowsWebServices.WS_ASYNC_FUNCTION,win32more.Networking.WindowsWebServices.WS_CALLBACK_MODEL,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsAsyncExecute', windll['webservices.dll']), ((1, 'asyncState'),(1, 'operation'),(1, 'callbackModel'),(1, 'callbackState'),(1, 'asyncContext'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsCreateChannel():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.WindowsWebServices.WS_CHANNEL_TYPE,win32more.Networking.WindowsWebServices.WS_CHANNEL_BINDING,POINTER(win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_head),UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_SECURITY_DESCRIPTION_head),POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_CHANNEL_head)),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsCreateChannel', windll['webservices.dll']), ((1, 'channelType'),(1, 'channelBinding'),(1, 'properties'),(1, 'propertyCount'),(1, 'securityDescription'),(1, 'channel'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsOpenChannel():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_CHANNEL_head),POINTER(win32more.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS_head),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsOpenChannel', windll['webservices.dll']), ((1, 'channel'),(1, 'endpointAddress'),(1, 'asyncContext'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsSendMessage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_CHANNEL_head),POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_DESCRIPTION_head),win32more.Networking.WindowsWebServices.WS_WRITE_OPTION,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsSendMessage', windll['webservices.dll']), ((1, 'channel'),(1, 'message'),(1, 'messageDescription'),(1, 'writeOption'),(1, 'bodyValue'),(1, 'bodyValueSize'),(1, 'asyncContext'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsReceiveMessage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_CHANNEL_head),POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_DESCRIPTION_head)),UInt32,win32more.Networking.WindowsWebServices.WS_RECEIVE_OPTION,win32more.Networking.WindowsWebServices.WS_READ_OPTION,POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head),c_void_p,UInt32,POINTER(UInt32),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsReceiveMessage', windll['webservices.dll']), ((1, 'channel'),(1, 'message'),(1, 'messageDescriptions'),(1, 'messageDescriptionCount'),(1, 'receiveOption'),(1, 'readBodyOption'),(1, 'heap'),(1, 'value'),(1, 'valueSize'),(1, 'index'),(1, 'asyncContext'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsRequestReply():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_CHANNEL_head),POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_DESCRIPTION_head),win32more.Networking.WindowsWebServices.WS_WRITE_OPTION,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_DESCRIPTION_head),win32more.Networking.WindowsWebServices.WS_READ_OPTION,POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head),c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsRequestReply', windll['webservices.dll']), ((1, 'channel'),(1, 'requestMessage'),(1, 'requestMessageDescription'),(1, 'writeOption'),(1, 'requestBodyValue'),(1, 'requestBodyValueSize'),(1, 'replyMessage'),(1, 'replyMessageDescription'),(1, 'readOption'),(1, 'heap'),(1, 'value'),(1, 'valueSize'),(1, 'asyncContext'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsSendReplyMessage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_CHANNEL_head),POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_DESCRIPTION_head),win32more.Networking.WindowsWebServices.WS_WRITE_OPTION,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsSendReplyMessage', windll['webservices.dll']), ((1, 'channel'),(1, 'replyMessage'),(1, 'replyMessageDescription'),(1, 'writeOption'),(1, 'replyBodyValue'),(1, 'replyBodyValueSize'),(1, 'requestMessage'),(1, 'asyncContext'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsSendFaultMessageForError():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_CHANNEL_head),POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head),win32more.Foundation.HRESULT,win32more.Networking.WindowsWebServices.WS_FAULT_DISCLOSURE,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsSendFaultMessageForError', windll['webservices.dll']), ((1, 'channel'),(1, 'replyMessage'),(1, 'faultError'),(1, 'faultErrorCode'),(1, 'faultDisclosure'),(1, 'requestMessage'),(1, 'asyncContext'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsGetChannelProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_CHANNEL_head),win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsGetChannelProperty', windll['webservices.dll']), ((1, 'channel'),(1, 'id'),(1, 'value'),(1, 'valueSize'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsSetChannelProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_CHANNEL_head),win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsSetChannelProperty', windll['webservices.dll']), ((1, 'channel'),(1, 'id'),(1, 'value'),(1, 'valueSize'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsWriteMessageStart():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_CHANNEL_head),POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsWriteMessageStart', windll['webservices.dll']), ((1, 'channel'),(1, 'message'),(1, 'asyncContext'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsWriteMessageEnd():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_CHANNEL_head),POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsWriteMessageEnd', windll['webservices.dll']), ((1, 'channel'),(1, 'message'),(1, 'asyncContext'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsReadMessageStart():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_CHANNEL_head),POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsReadMessageStart', windll['webservices.dll']), ((1, 'channel'),(1, 'message'),(1, 'asyncContext'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsReadMessageEnd():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_CHANNEL_head),POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsReadMessageEnd', windll['webservices.dll']), ((1, 'channel'),(1, 'message'),(1, 'asyncContext'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsCloseChannel():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_CHANNEL_head),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsCloseChannel', windll['webservices.dll']), ((1, 'channel'),(1, 'asyncContext'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsAbortChannel():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_CHANNEL_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsAbortChannel', windll['webservices.dll']), ((1, 'channel'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsFreeChannel():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Networking.WindowsWebServices.WS_CHANNEL_head))(('WsFreeChannel', windll['webservices.dll']), ((1, 'channel'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsResetChannel():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_CHANNEL_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsResetChannel', windll['webservices.dll']), ((1, 'channel'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsAbandonMessage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_CHANNEL_head),POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsAbandonMessage', windll['webservices.dll']), ((1, 'channel'),(1, 'message'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsShutdownSessionChannel():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_CHANNEL_head),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsShutdownSessionChannel', windll['webservices.dll']), ((1, 'channel'),(1, 'asyncContext'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsGetOperationContextProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_OPERATION_CONTEXT_head),win32more.Networking.WindowsWebServices.WS_OPERATION_CONTEXT_PROPERTY_ID,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsGetOperationContextProperty', windll['webservices.dll']), ((1, 'context'),(1, 'id'),(1, 'value'),(1, 'valueSize'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsGetDictionary():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.WindowsWebServices.WS_ENCODING,POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_XML_DICTIONARY_head)),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsGetDictionary', windll['webservices.dll']), ((1, 'encoding'),(1, 'dictionary'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsReadEndpointAddressExtension():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),POINTER(win32more.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS_head),win32more.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS_EXTENSION_TYPE,win32more.Networking.WindowsWebServices.WS_READ_OPTION,POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head),c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsReadEndpointAddressExtension', windll['webservices.dll']), ((1, 'reader'),(1, 'endpointAddress'),(1, 'extensionType'),(1, 'readOption'),(1, 'heap'),(1, 'value'),(1, 'valueSize'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsCreateError():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_PROPERTY_head),UInt32,POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head)))(('WsCreateError', windll['webservices.dll']), ((1, 'properties'),(1, 'propertyCount'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsAddErrorString():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head),POINTER(win32more.Networking.WindowsWebServices.WS_STRING_head))(('WsAddErrorString', windll['webservices.dll']), ((1, 'error'),(1, 'string'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsGetErrorString():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head),UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_STRING_head))(('WsGetErrorString', windll['webservices.dll']), ((1, 'error'),(1, 'index'),(1, 'string'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsCopyError():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsCopyError', windll['webservices.dll']), ((1, 'source'),(1, 'destination'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsGetErrorProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head),win32more.Networking.WindowsWebServices.WS_ERROR_PROPERTY_ID,c_void_p,UInt32)(('WsGetErrorProperty', windll['webservices.dll']), ((1, 'error'),(1, 'id'),(1, 'buffer'),(1, 'bufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsSetErrorProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head),win32more.Networking.WindowsWebServices.WS_ERROR_PROPERTY_ID,c_void_p,UInt32)(('WsSetErrorProperty', windll['webservices.dll']), ((1, 'error'),(1, 'id'),(1, 'value'),(1, 'valueSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsResetError():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsResetError', windll['webservices.dll']), ((1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsFreeError():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsFreeError', windll['webservices.dll']), ((1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsGetFaultErrorProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head),win32more.Networking.WindowsWebServices.WS_FAULT_ERROR_PROPERTY_ID,c_void_p,UInt32)(('WsGetFaultErrorProperty', windll['webservices.dll']), ((1, 'error'),(1, 'id'),(1, 'buffer'),(1, 'bufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsSetFaultErrorProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head),win32more.Networking.WindowsWebServices.WS_FAULT_ERROR_PROPERTY_ID,c_void_p,UInt32)(('WsSetFaultErrorProperty', windll['webservices.dll']), ((1, 'error'),(1, 'id'),(1, 'value'),(1, 'valueSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsCreateFaultFromError():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head),win32more.Foundation.HRESULT,win32more.Networking.WindowsWebServices.WS_FAULT_DISCLOSURE,POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head),POINTER(win32more.Networking.WindowsWebServices.WS_FAULT_head))(('WsCreateFaultFromError', windll['webservices.dll']), ((1, 'error'),(1, 'faultErrorCode'),(1, 'faultDisclosure'),(1, 'heap'),(1, 'fault'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsSetFaultErrorDetail():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head),POINTER(win32more.Networking.WindowsWebServices.WS_FAULT_DETAIL_DESCRIPTION_head),win32more.Networking.WindowsWebServices.WS_WRITE_OPTION,c_void_p,UInt32)(('WsSetFaultErrorDetail', windll['webservices.dll']), ((1, 'error'),(1, 'faultDetailDescription'),(1, 'writeOption'),(1, 'value'),(1, 'valueSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsGetFaultErrorDetail():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head),POINTER(win32more.Networking.WindowsWebServices.WS_FAULT_DETAIL_DESCRIPTION_head),win32more.Networking.WindowsWebServices.WS_READ_OPTION,POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head),c_void_p,UInt32)(('WsGetFaultErrorDetail', windll['webservices.dll']), ((1, 'error'),(1, 'faultDetailDescription'),(1, 'readOption'),(1, 'heap'),(1, 'value'),(1, 'valueSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsCreateHeap():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr,UIntPtr,POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_PROPERTY_head),UInt32,POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head)),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsCreateHeap', windll['webservices.dll']), ((1, 'maxSize'),(1, 'trimSize'),(1, 'properties'),(1, 'propertyCount'),(1, 'heap'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsAlloc():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head),UIntPtr,POINTER(c_void_p),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsAlloc', windll['webservices.dll']), ((1, 'heap'),(1, 'size'),(1, 'ptr'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsGetHeapProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head),win32more.Networking.WindowsWebServices.WS_HEAP_PROPERTY_ID,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsGetHeapProperty', windll['webservices.dll']), ((1, 'heap'),(1, 'id'),(1, 'value'),(1, 'valueSize'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsResetHeap():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsResetHeap', windll['webservices.dll']), ((1, 'heap'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsFreeHeap():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head))(('WsFreeHeap', windll['webservices.dll']), ((1, 'heap'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsCreateListener():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.WindowsWebServices.WS_CHANNEL_TYPE,win32more.Networking.WindowsWebServices.WS_CHANNEL_BINDING,POINTER(win32more.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_head),UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_SECURITY_DESCRIPTION_head),POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_LISTENER_head)),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsCreateListener', windll['webservices.dll']), ((1, 'channelType'),(1, 'channelBinding'),(1, 'properties'),(1, 'propertyCount'),(1, 'securityDescription'),(1, 'listener'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsOpenListener():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_LISTENER_head),POINTER(win32more.Networking.WindowsWebServices.WS_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsOpenListener', windll['webservices.dll']), ((1, 'listener'),(1, 'url'),(1, 'asyncContext'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsAcceptChannel():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_LISTENER_head),POINTER(win32more.Networking.WindowsWebServices.WS_CHANNEL_head),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsAcceptChannel', windll['webservices.dll']), ((1, 'listener'),(1, 'channel'),(1, 'asyncContext'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsCloseListener():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_LISTENER_head),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsCloseListener', windll['webservices.dll']), ((1, 'listener'),(1, 'asyncContext'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsAbortListener():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_LISTENER_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsAbortListener', windll['webservices.dll']), ((1, 'listener'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsResetListener():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_LISTENER_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsResetListener', windll['webservices.dll']), ((1, 'listener'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsFreeListener():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Networking.WindowsWebServices.WS_LISTENER_head))(('WsFreeListener', windll['webservices.dll']), ((1, 'listener'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsGetListenerProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_LISTENER_head),win32more.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsGetListenerProperty', windll['webservices.dll']), ((1, 'listener'),(1, 'id'),(1, 'value'),(1, 'valueSize'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsSetListenerProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_LISTENER_head),win32more.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsSetListenerProperty', windll['webservices.dll']), ((1, 'listener'),(1, 'id'),(1, 'value'),(1, 'valueSize'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsCreateChannelForListener():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_LISTENER_head),POINTER(win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_head),UInt32,POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_CHANNEL_head)),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsCreateChannelForListener', windll['webservices.dll']), ((1, 'listener'),(1, 'properties'),(1, 'propertyCount'),(1, 'channel'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsCreateMessage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.WindowsWebServices.WS_ENVELOPE_VERSION,win32more.Networking.WindowsWebServices.WS_ADDRESSING_VERSION,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_head),UInt32,POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head)),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsCreateMessage', windll['webservices.dll']), ((1, 'envelopeVersion'),(1, 'addressingVersion'),(1, 'properties'),(1, 'propertyCount'),(1, 'message'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsCreateMessageForChannel():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_CHANNEL_head),POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_head),UInt32,POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head)),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsCreateMessageForChannel', windll['webservices.dll']), ((1, 'channel'),(1, 'properties'),(1, 'propertyCount'),(1, 'message'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsInitializeMessage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),win32more.Networking.WindowsWebServices.WS_MESSAGE_INITIALIZATION,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsInitializeMessage', windll['webservices.dll']), ((1, 'message'),(1, 'initialization'),(1, 'sourceMessage'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsResetMessage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsResetMessage', windll['webservices.dll']), ((1, 'message'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsFreeMessage():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head))(('WsFreeMessage', windll['webservices.dll']), ((1, 'message'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsGetHeaderAttributes():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),POINTER(UInt32),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsGetHeaderAttributes', windll['webservices.dll']), ((1, 'message'),(1, 'reader'),(1, 'headerAttributes'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsGetHeader():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),win32more.Networking.WindowsWebServices.WS_HEADER_TYPE,win32more.Networking.WindowsWebServices.WS_TYPE,win32more.Networking.WindowsWebServices.WS_READ_OPTION,POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head),c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsGetHeader', windll['webservices.dll']), ((1, 'message'),(1, 'headerType'),(1, 'valueType'),(1, 'readOption'),(1, 'heap'),(1, 'value'),(1, 'valueSize'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsGetCustomHeader():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_ELEMENT_DESCRIPTION_head),win32more.Networking.WindowsWebServices.WS_REPEATING_HEADER_OPTION,UInt32,win32more.Networking.WindowsWebServices.WS_READ_OPTION,POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head),c_void_p,UInt32,POINTER(UInt32),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsGetCustomHeader', windll['webservices.dll']), ((1, 'message'),(1, 'customHeaderDescription'),(1, 'repeatingOption'),(1, 'headerIndex'),(1, 'readOption'),(1, 'heap'),(1, 'value'),(1, 'valueSize'),(1, 'headerAttributes'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsRemoveHeader():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),win32more.Networking.WindowsWebServices.WS_HEADER_TYPE,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsRemoveHeader', windll['webservices.dll']), ((1, 'message'),(1, 'headerType'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsSetHeader():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),win32more.Networking.WindowsWebServices.WS_HEADER_TYPE,win32more.Networking.WindowsWebServices.WS_TYPE,win32more.Networking.WindowsWebServices.WS_WRITE_OPTION,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsSetHeader', windll['webservices.dll']), ((1, 'message'),(1, 'headerType'),(1, 'valueType'),(1, 'writeOption'),(1, 'value'),(1, 'valueSize'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsRemoveCustomHeader():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsRemoveCustomHeader', windll['webservices.dll']), ((1, 'message'),(1, 'headerName'),(1, 'headerNs'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsAddCustomHeader():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_ELEMENT_DESCRIPTION_head),win32more.Networking.WindowsWebServices.WS_WRITE_OPTION,c_void_p,UInt32,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsAddCustomHeader', windll['webservices.dll']), ((1, 'message'),(1, 'headerDescription'),(1, 'writeOption'),(1, 'value'),(1, 'valueSize'),(1, 'headerAttributes'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsAddMappedHeader():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),win32more.Networking.WindowsWebServices.WS_TYPE,win32more.Networking.WindowsWebServices.WS_WRITE_OPTION,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsAddMappedHeader', windll['webservices.dll']), ((1, 'message'),(1, 'headerName'),(1, 'valueType'),(1, 'writeOption'),(1, 'value'),(1, 'valueSize'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsRemoveMappedHeader():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsRemoveMappedHeader', windll['webservices.dll']), ((1, 'message'),(1, 'headerName'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsGetMappedHeader():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),win32more.Networking.WindowsWebServices.WS_REPEATING_HEADER_OPTION,UInt32,win32more.Networking.WindowsWebServices.WS_TYPE,win32more.Networking.WindowsWebServices.WS_READ_OPTION,POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head),c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsGetMappedHeader', windll['webservices.dll']), ((1, 'message'),(1, 'headerName'),(1, 'repeatingOption'),(1, 'headerIndex'),(1, 'valueType'),(1, 'readOption'),(1, 'heap'),(1, 'value'),(1, 'valueSize'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsWriteBody():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_ELEMENT_DESCRIPTION_head),win32more.Networking.WindowsWebServices.WS_WRITE_OPTION,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsWriteBody', windll['webservices.dll']), ((1, 'message'),(1, 'bodyDescription'),(1, 'writeOption'),(1, 'value'),(1, 'valueSize'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsReadBody():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_ELEMENT_DESCRIPTION_head),win32more.Networking.WindowsWebServices.WS_READ_OPTION,POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head),c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsReadBody', windll['webservices.dll']), ((1, 'message'),(1, 'bodyDescription'),(1, 'readOption'),(1, 'heap'),(1, 'value'),(1, 'valueSize'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsWriteEnvelopeStart():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),win32more.Networking.WindowsWebServices.WS_MESSAGE_DONE_CALLBACK,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsWriteEnvelopeStart', windll['webservices.dll']), ((1, 'message'),(1, 'writer'),(1, 'doneCallback'),(1, 'doneCallbackState'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsWriteEnvelopeEnd():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsWriteEnvelopeEnd', windll['webservices.dll']), ((1, 'message'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsReadEnvelopeStart():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),win32more.Networking.WindowsWebServices.WS_MESSAGE_DONE_CALLBACK,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsReadEnvelopeStart', windll['webservices.dll']), ((1, 'message'),(1, 'reader'),(1, 'doneCallback'),(1, 'doneCallbackState'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsReadEnvelopeEnd():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsReadEnvelopeEnd', windll['webservices.dll']), ((1, 'message'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsGetMessageProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),win32more.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_ID,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsGetMessageProperty', windll['webservices.dll']), ((1, 'message'),(1, 'id'),(1, 'value'),(1, 'valueSize'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsSetMessageProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),win32more.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_ID,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsSetMessageProperty', windll['webservices.dll']), ((1, 'message'),(1, 'id'),(1, 'value'),(1, 'valueSize'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsAddressMessage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsAddressMessage', windll['webservices.dll']), ((1, 'message'),(1, 'address'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsCheckMustUnderstandHeaders():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsCheckMustUnderstandHeaders', windll['webservices.dll']), ((1, 'message'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsMarkHeaderAsUnderstood():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_NODE_POSITION_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsMarkHeaderAsUnderstood', windll['webservices.dll']), ((1, 'message'),(1, 'headerPosition'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsFillBody():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsFillBody', windll['webservices.dll']), ((1, 'message'),(1, 'minSize'),(1, 'asyncContext'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsFlushBody():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsFlushBody', windll['webservices.dll']), ((1, 'message'),(1, 'minSize'),(1, 'asyncContext'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsRequestSecurityToken():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_CHANNEL_head),POINTER(win32more.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_PROPERTY_head),UInt32,POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_SECURITY_TOKEN_head)),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsRequestSecurityToken', windll['webservices.dll']), ((1, 'channel'),(1, 'properties'),(1, 'propertyCount'),(1, 'token'),(1, 'asyncContext'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsGetSecurityTokenProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_SECURITY_TOKEN_head),win32more.Networking.WindowsWebServices.WS_SECURITY_TOKEN_PROPERTY_ID,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsGetSecurityTokenProperty', windll['webservices.dll']), ((1, 'securityToken'),(1, 'id'),(1, 'value'),(1, 'valueSize'),(1, 'heap'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsCreateXmlSecurityToken():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_BUFFER_head),POINTER(win32more.Networking.WindowsWebServices.WS_SECURITY_KEY_HANDLE_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_SECURITY_TOKEN_PROPERTY_head),UInt32,POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_SECURITY_TOKEN_head)),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsCreateXmlSecurityToken', windll['webservices.dll']), ((1, 'tokenXml'),(1, 'tokenKey'),(1, 'properties'),(1, 'propertyCount'),(1, 'token'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsFreeSecurityToken():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Networking.WindowsWebServices.WS_SECURITY_TOKEN_head))(('WsFreeSecurityToken', windll['webservices.dll']), ((1, 'token'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsRevokeSecurityContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsRevokeSecurityContext', windll['webservices.dll']), ((1, 'securityContext'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsGetSecurityContextProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_head),win32more.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_PROPERTY_ID,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsGetSecurityContextProperty', windll['webservices.dll']), ((1, 'securityContext'),(1, 'id'),(1, 'value'),(1, 'valueSize'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsReadElement():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),POINTER(win32more.Networking.WindowsWebServices.WS_ELEMENT_DESCRIPTION_head),win32more.Networking.WindowsWebServices.WS_READ_OPTION,POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head),c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsReadElement', windll['webservices.dll']), ((1, 'reader'),(1, 'elementDescription'),(1, 'readOption'),(1, 'heap'),(1, 'value'),(1, 'valueSize'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsReadAttribute():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),POINTER(win32more.Networking.WindowsWebServices.WS_ATTRIBUTE_DESCRIPTION_head),win32more.Networking.WindowsWebServices.WS_READ_OPTION,POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head),c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsReadAttribute', windll['webservices.dll']), ((1, 'reader'),(1, 'attributeDescription'),(1, 'readOption'),(1, 'heap'),(1, 'value'),(1, 'valueSize'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsReadType():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),win32more.Networking.WindowsWebServices.WS_TYPE_MAPPING,win32more.Networking.WindowsWebServices.WS_TYPE,c_void_p,win32more.Networking.WindowsWebServices.WS_READ_OPTION,POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head),c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsReadType', windll['webservices.dll']), ((1, 'reader'),(1, 'typeMapping'),(1, 'type'),(1, 'typeDescription'),(1, 'readOption'),(1, 'heap'),(1, 'value'),(1, 'valueSize'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsWriteElement():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),POINTER(win32more.Networking.WindowsWebServices.WS_ELEMENT_DESCRIPTION_head),win32more.Networking.WindowsWebServices.WS_WRITE_OPTION,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsWriteElement', windll['webservices.dll']), ((1, 'writer'),(1, 'elementDescription'),(1, 'writeOption'),(1, 'value'),(1, 'valueSize'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsWriteAttribute():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),POINTER(win32more.Networking.WindowsWebServices.WS_ATTRIBUTE_DESCRIPTION_head),win32more.Networking.WindowsWebServices.WS_WRITE_OPTION,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsWriteAttribute', windll['webservices.dll']), ((1, 'writer'),(1, 'attributeDescription'),(1, 'writeOption'),(1, 'value'),(1, 'valueSize'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsWriteType():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),win32more.Networking.WindowsWebServices.WS_TYPE_MAPPING,win32more.Networking.WindowsWebServices.WS_TYPE,c_void_p,win32more.Networking.WindowsWebServices.WS_WRITE_OPTION,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsWriteType', windll['webservices.dll']), ((1, 'writer'),(1, 'typeMapping'),(1, 'type'),(1, 'typeDescription'),(1, 'writeOption'),(1, 'value'),(1, 'valueSize'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsRegisterOperationForCancel():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_OPERATION_CONTEXT_head),win32more.Networking.WindowsWebServices.WS_OPERATION_CANCEL_CALLBACK,win32more.Networking.WindowsWebServices.WS_OPERATION_FREE_STATE_CALLBACK,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsRegisterOperationForCancel', windll['webservices.dll']), ((1, 'context'),(1, 'cancelCallback'),(1, 'freestateCallback'),(1, 'userState'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsGetServiceHostProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_SERVICE_HOST_head),win32more.Networking.WindowsWebServices.WS_SERVICE_PROPERTY_ID,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsGetServiceHostProperty', windll['webservices.dll']), ((1, 'serviceHost'),(1, 'id'),(1, 'value'),(1, 'valueSize'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsCreateServiceHost():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT_head)),UInt16,POINTER(win32more.Networking.WindowsWebServices.WS_SERVICE_PROPERTY_head),UInt32,POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_SERVICE_HOST_head)),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsCreateServiceHost', windll['webservices.dll']), ((1, 'endpoints'),(1, 'endpointCount'),(1, 'serviceProperties'),(1, 'servicePropertyCount'),(1, 'serviceHost'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsOpenServiceHost():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_SERVICE_HOST_head),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsOpenServiceHost', windll['webservices.dll']), ((1, 'serviceHost'),(1, 'asyncContext'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsCloseServiceHost():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_SERVICE_HOST_head),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsCloseServiceHost', windll['webservices.dll']), ((1, 'serviceHost'),(1, 'asyncContext'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsAbortServiceHost():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_SERVICE_HOST_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsAbortServiceHost', windll['webservices.dll']), ((1, 'serviceHost'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsFreeServiceHost():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Networking.WindowsWebServices.WS_SERVICE_HOST_head))(('WsFreeServiceHost', windll['webservices.dll']), ((1, 'serviceHost'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsResetServiceHost():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_SERVICE_HOST_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsResetServiceHost', windll['webservices.dll']), ((1, 'serviceHost'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsGetServiceProxyProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_SERVICE_PROXY_head),win32more.Networking.WindowsWebServices.WS_PROXY_PROPERTY_ID,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsGetServiceProxyProperty', windll['webservices.dll']), ((1, 'serviceProxy'),(1, 'id'),(1, 'value'),(1, 'valueSize'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsCreateServiceProxy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.WindowsWebServices.WS_CHANNEL_TYPE,win32more.Networking.WindowsWebServices.WS_CHANNEL_BINDING,POINTER(win32more.Networking.WindowsWebServices.WS_SECURITY_DESCRIPTION_head),POINTER(win32more.Networking.WindowsWebServices.WS_PROXY_PROPERTY_head),UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_head),UInt32,POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_SERVICE_PROXY_head)),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsCreateServiceProxy', windll['webservices.dll']), ((1, 'channelType'),(1, 'channelBinding'),(1, 'securityDescription'),(1, 'properties'),(1, 'propertyCount'),(1, 'channelProperties'),(1, 'channelPropertyCount'),(1, 'serviceProxy'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsOpenServiceProxy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_SERVICE_PROXY_head),POINTER(win32more.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS_head),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsOpenServiceProxy', windll['webservices.dll']), ((1, 'serviceProxy'),(1, 'address'),(1, 'asyncContext'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsCloseServiceProxy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_SERVICE_PROXY_head),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsCloseServiceProxy', windll['webservices.dll']), ((1, 'serviceProxy'),(1, 'asyncContext'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsAbortServiceProxy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_SERVICE_PROXY_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsAbortServiceProxy', windll['webservices.dll']), ((1, 'serviceProxy'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsFreeServiceProxy():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Networking.WindowsWebServices.WS_SERVICE_PROXY_head))(('WsFreeServiceProxy', windll['webservices.dll']), ((1, 'serviceProxy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsResetServiceProxy():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_SERVICE_PROXY_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsResetServiceProxy', windll['webservices.dll']), ((1, 'serviceProxy'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsAbandonCall():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_SERVICE_PROXY_head),UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsAbandonCall', windll['webservices.dll']), ((1, 'serviceProxy'),(1, 'callId'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsCall():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_SERVICE_PROXY_head),POINTER(win32more.Networking.WindowsWebServices.WS_OPERATION_DESCRIPTION_head),POINTER(c_void_p),POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head),POINTER(win32more.Networking.WindowsWebServices.WS_CALL_PROPERTY_head),UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsCall', windll['webservices.dll']), ((1, 'serviceProxy'),(1, 'operation'),(1, 'arguments'),(1, 'heap'),(1, 'callProperties'),(1, 'callPropertyCount'),(1, 'asyncContext'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsDecodeUrl():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_STRING_head),UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head),POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_URL_head)),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsDecodeUrl', windll['webservices.dll']), ((1, 'url'),(1, 'flags'),(1, 'heap'),(1, 'outUrl'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsEncodeUrl():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_URL_head),UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head),POINTER(win32more.Networking.WindowsWebServices.WS_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsEncodeUrl', windll['webservices.dll']), ((1, 'url'),(1, 'flags'),(1, 'heap'),(1, 'outUrl'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsCombineUrl():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_STRING_head),UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head),POINTER(win32more.Networking.WindowsWebServices.WS_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsCombineUrl', windll['webservices.dll']), ((1, 'baseUrl'),(1, 'referenceUrl'),(1, 'flags'),(1, 'heap'),(1, 'resultUrl'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsDateTimeToFileTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_DATETIME_head),POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsDateTimeToFileTime', windll['webservices.dll']), ((1, 'dateTime'),(1, 'fileTime'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsFileTimeToDateTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Networking.WindowsWebServices.WS_DATETIME_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsFileTimeToDateTime', windll['webservices.dll']), ((1, 'fileTime'),(1, 'dateTime'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsCreateMetadata():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_METADATA_PROPERTY_head),UInt32,POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_METADATA_head)),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsCreateMetadata', windll['webservices.dll']), ((1, 'properties'),(1, 'propertyCount'),(1, 'metadata'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsReadMetadata():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_METADATA_head),POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),POINTER(win32more.Networking.WindowsWebServices.WS_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsReadMetadata', windll['webservices.dll']), ((1, 'metadata'),(1, 'reader'),(1, 'url'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsFreeMetadata():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Networking.WindowsWebServices.WS_METADATA_head))(('WsFreeMetadata', windll['webservices.dll']), ((1, 'metadata'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsResetMetadata():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_METADATA_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsResetMetadata', windll['webservices.dll']), ((1, 'metadata'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsGetMetadataProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_METADATA_head),win32more.Networking.WindowsWebServices.WS_METADATA_PROPERTY_ID,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsGetMetadataProperty', windll['webservices.dll']), ((1, 'metadata'),(1, 'id'),(1, 'value'),(1, 'valueSize'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsGetMissingMetadataDocumentAddress():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_METADATA_head),POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS_head)),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsGetMissingMetadataDocumentAddress', windll['webservices.dll']), ((1, 'metadata'),(1, 'address'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsGetMetadataEndpoints():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_METADATA_head),POINTER(win32more.Networking.WindowsWebServices.WS_METADATA_ENDPOINTS_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsGetMetadataEndpoints', windll['webservices.dll']), ((1, 'metadata'),(1, 'endpoints'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsMatchPolicyAlternative():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_POLICY_head),UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_POLICY_CONSTRAINTS_head),win32more.Foundation.BOOL,POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsMatchPolicyAlternative', windll['webservices.dll']), ((1, 'policy'),(1, 'alternativeIndex'),(1, 'policyConstraints'),(1, 'matchRequired'),(1, 'heap'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsGetPolicyProperty():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_POLICY_head),win32more.Networking.WindowsWebServices.WS_POLICY_PROPERTY_ID,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsGetPolicyProperty', windll['webservices.dll']), ((1, 'policy'),(1, 'id'),(1, 'value'),(1, 'valueSize'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsGetPolicyAlternativeCount():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_POLICY_head),POINTER(UInt32),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsGetPolicyAlternativeCount', windll['webservices.dll']), ((1, 'policy'),(1, 'count'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsCreateServiceProxyFromTemplate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.WindowsWebServices.WS_CHANNEL_TYPE,POINTER(win32more.Networking.WindowsWebServices.WS_PROXY_PROPERTY_head),UInt32,win32more.Networking.WindowsWebServices.WS_BINDING_TEMPLATE_TYPE,c_void_p,UInt32,c_void_p,UInt32,POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_SERVICE_PROXY_head)),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsCreateServiceProxyFromTemplate', windll['webservices.dll']), ((1, 'channelType'),(1, 'properties'),(1, 'propertyCount'),(1, 'templateType'),(1, 'templateValue'),(1, 'templateSize'),(1, 'templateDescription'),(1, 'templateDescriptionSize'),(1, 'serviceProxy'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WsCreateServiceEndpointFromTemplate():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.WindowsWebServices.WS_CHANNEL_TYPE,POINTER(win32more.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT_PROPERTY_head),UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_SERVICE_CONTRACT_head),win32more.Networking.WindowsWebServices.WS_SERVICE_SECURITY_CALLBACK,POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head),win32more.Networking.WindowsWebServices.WS_BINDING_TEMPLATE_TYPE,c_void_p,UInt32,c_void_p,UInt32,POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT_head)),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))(('WsCreateServiceEndpointFromTemplate', windll['webservices.dll']), ((1, 'channelType'),(1, 'properties'),(1, 'propertyCount'),(1, 'addressUrl'),(1, 'contract'),(1, 'authorizationCallback'),(1, 'heap'),(1, 'templateType'),(1, 'templateValue'),(1, 'templateSize'),(1, 'templateDescription'),(1, 'templateDescriptionSize'),(1, 'serviceEndpoint'),(1, 'error'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WebAuthNGetApiVersionNumber():
    try:
        return WINFUNCTYPE(UInt32,)(('WebAuthNGetApiVersionNumber', windll['webauthn.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_WebAuthNIsUserVerifyingPlatformAuthenticatorAvailable():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(('WebAuthNIsUserVerifyingPlatformAuthenticatorAvailable', windll['webauthn.dll']), ((1, 'pbIsUserVerifyingPlatformAuthenticatorAvailable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WebAuthNAuthenticatorMakeCredential():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,POINTER(win32more.Networking.WindowsWebServices.WEBAUTHN_RP_ENTITY_INFORMATION_head),POINTER(win32more.Networking.WindowsWebServices.WEBAUTHN_USER_ENTITY_INFORMATION_head),POINTER(win32more.Networking.WindowsWebServices.WEBAUTHN_COSE_CREDENTIAL_PARAMETERS_head),POINTER(win32more.Networking.WindowsWebServices.WEBAUTHN_CLIENT_DATA_head),POINTER(win32more.Networking.WindowsWebServices.WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_head),POINTER(POINTER(win32more.Networking.WindowsWebServices.WEBAUTHN_CREDENTIAL_ATTESTATION_head)))(('WebAuthNAuthenticatorMakeCredential', windll['webauthn.dll']), ((1, 'hWnd'),(1, 'pRpInformation'),(1, 'pUserInformation'),(1, 'pPubKeyCredParams'),(1, 'pWebAuthNClientData'),(1, 'pWebAuthNMakeCredentialOptions'),(1, 'ppWebAuthNCredentialAttestation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WebAuthNAuthenticatorGetAssertion():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PWSTR,POINTER(win32more.Networking.WindowsWebServices.WEBAUTHN_CLIENT_DATA_head),POINTER(win32more.Networking.WindowsWebServices.WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_head),POINTER(POINTER(win32more.Networking.WindowsWebServices.WEBAUTHN_ASSERTION_head)))(('WebAuthNAuthenticatorGetAssertion', windll['webauthn.dll']), ((1, 'hWnd'),(1, 'pwszRpId'),(1, 'pWebAuthNClientData'),(1, 'pWebAuthNGetAssertionOptions'),(1, 'ppWebAuthNAssertion'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WebAuthNFreeCredentialAttestation():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Networking.WindowsWebServices.WEBAUTHN_CREDENTIAL_ATTESTATION_head))(('WebAuthNFreeCredentialAttestation', windll['webauthn.dll']), ((1, 'pWebAuthNCredentialAttestation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WebAuthNFreeAssertion():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Networking.WindowsWebServices.WEBAUTHN_ASSERTION_head))(('WebAuthNFreeAssertion', windll['webauthn.dll']), ((1, 'pWebAuthNAssertion'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WebAuthNGetCancellationId():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(('WebAuthNGetCancellationId', windll['webauthn.dll']), ((1, 'pCancellationId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WebAuthNCancelCurrentOperation():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid))(('WebAuthNCancelCurrentOperation', windll['webauthn.dll']), ((1, 'pCancellationId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WebAuthNGetErrorName():
    try:
        return WINFUNCTYPE(win32more.Foundation.PWSTR,win32more.Foundation.HRESULT)(('WebAuthNGetErrorName', windll['webauthn.dll']), ((1, 'hr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WebAuthNGetW3CExceptionDOMError():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT)(('WebAuthNGetW3CExceptionDOMError', windll['webauthn.dll']), ((1, 'hr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IContentPrefetcherTaskTrigger_head():
    class IContentPrefetcherTaskTrigger(win32more.System.WinRT.IInspectable_head):
        Guid = Guid('1b35a14a-6094-4799-a6-0e-e4-74-e1-5d-4d-c9')
    return IContentPrefetcherTaskTrigger
def _define_IContentPrefetcherTaskTrigger():
    IContentPrefetcherTaskTrigger = win32more.Networking.WindowsWebServices.IContentPrefetcherTaskTrigger_head
    IContentPrefetcherTaskTrigger.TriggerContentPrefetcherTask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(6, 'TriggerContentPrefetcherTask', ((1, 'packageFullName'),)))
    IContentPrefetcherTaskTrigger.IsRegisteredForContentPrefetch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,c_char_p_no)(7, 'IsRegisteredForContentPrefetch', ((1, 'packageFullName'),(1, 'isRegistered'),)))
    win32more.System.WinRT.IInspectable
    return IContentPrefetcherTaskTrigger
def _define_WEBAUTHN_ASSERTION_head():
    class WEBAUTHN_ASSERTION(Structure):
        pass
    return WEBAUTHN_ASSERTION
def _define_WEBAUTHN_ASSERTION():
    WEBAUTHN_ASSERTION = win32more.Networking.WindowsWebServices.WEBAUTHN_ASSERTION_head
    WEBAUTHN_ASSERTION._fields_ = [
        ('dwVersion', UInt32),
        ('cbAuthenticatorData', UInt32),
        ('pbAuthenticatorData', c_char_p_no),
        ('cbSignature', UInt32),
        ('pbSignature', c_char_p_no),
        ('Credential', win32more.Networking.WindowsWebServices.WEBAUTHN_CREDENTIAL),
        ('cbUserId', UInt32),
        ('pbUserId', c_char_p_no),
        ('Extensions', win32more.Networking.WindowsWebServices.WEBAUTHN_EXTENSIONS),
        ('cbCredLargeBlob', UInt32),
        ('pbCredLargeBlob', c_char_p_no),
        ('dwCredLargeBlobStatus', UInt32),
    ]
    return WEBAUTHN_ASSERTION
def _define_WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_head():
    class WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS(Structure):
        pass
    return WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS
def _define_WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS():
    WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS = win32more.Networking.WindowsWebServices.WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_head
    WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS._fields_ = [
        ('dwVersion', UInt32),
        ('dwTimeoutMilliseconds', UInt32),
        ('CredentialList', win32more.Networking.WindowsWebServices.WEBAUTHN_CREDENTIALS),
        ('Extensions', win32more.Networking.WindowsWebServices.WEBAUTHN_EXTENSIONS),
        ('dwAuthenticatorAttachment', UInt32),
        ('dwUserVerificationRequirement', UInt32),
        ('dwFlags', UInt32),
        ('pwszU2fAppId', win32more.Foundation.PWSTR),
        ('pbU2fAppId', POINTER(win32more.Foundation.BOOL)),
        ('pCancellationId', POINTER(Guid)),
        ('pAllowCredentialList', POINTER(win32more.Networking.WindowsWebServices.WEBAUTHN_CREDENTIAL_LIST_head)),
        ('dwCredLargeBlobOperation', UInt32),
        ('cbCredLargeBlob', UInt32),
        ('pbCredLargeBlob', c_char_p_no),
    ]
    return WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS
def _define_WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_head():
    class WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS(Structure):
        pass
    return WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS
def _define_WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS():
    WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS = win32more.Networking.WindowsWebServices.WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_head
    WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS._fields_ = [
        ('dwVersion', UInt32),
        ('dwTimeoutMilliseconds', UInt32),
        ('CredentialList', win32more.Networking.WindowsWebServices.WEBAUTHN_CREDENTIALS),
        ('Extensions', win32more.Networking.WindowsWebServices.WEBAUTHN_EXTENSIONS),
        ('dwAuthenticatorAttachment', UInt32),
        ('bRequireResidentKey', win32more.Foundation.BOOL),
        ('dwUserVerificationRequirement', UInt32),
        ('dwAttestationConveyancePreference', UInt32),
        ('dwFlags', UInt32),
        ('pCancellationId', POINTER(Guid)),
        ('pExcludeCredentialList', POINTER(win32more.Networking.WindowsWebServices.WEBAUTHN_CREDENTIAL_LIST_head)),
        ('dwEnterpriseAttestation', UInt32),
        ('dwLargeBlobSupport', UInt32),
        ('bPreferResidentKey', win32more.Foundation.BOOL),
    ]
    return WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS
def _define_WEBAUTHN_CLIENT_DATA_head():
    class WEBAUTHN_CLIENT_DATA(Structure):
        pass
    return WEBAUTHN_CLIENT_DATA
def _define_WEBAUTHN_CLIENT_DATA():
    WEBAUTHN_CLIENT_DATA = win32more.Networking.WindowsWebServices.WEBAUTHN_CLIENT_DATA_head
    WEBAUTHN_CLIENT_DATA._fields_ = [
        ('dwVersion', UInt32),
        ('cbClientDataJSON', UInt32),
        ('pbClientDataJSON', c_char_p_no),
        ('pwszHashAlgId', win32more.Foundation.PWSTR),
    ]
    return WEBAUTHN_CLIENT_DATA
def _define_WEBAUTHN_COMMON_ATTESTATION_head():
    class WEBAUTHN_COMMON_ATTESTATION(Structure):
        pass
    return WEBAUTHN_COMMON_ATTESTATION
def _define_WEBAUTHN_COMMON_ATTESTATION():
    WEBAUTHN_COMMON_ATTESTATION = win32more.Networking.WindowsWebServices.WEBAUTHN_COMMON_ATTESTATION_head
    WEBAUTHN_COMMON_ATTESTATION._fields_ = [
        ('dwVersion', UInt32),
        ('pwszAlg', win32more.Foundation.PWSTR),
        ('lAlg', Int32),
        ('cbSignature', UInt32),
        ('pbSignature', c_char_p_no),
        ('cX5c', UInt32),
        ('pX5c', POINTER(win32more.Networking.WindowsWebServices.WEBAUTHN_X5C_head)),
        ('pwszVer', win32more.Foundation.PWSTR),
        ('cbCertInfo', UInt32),
        ('pbCertInfo', c_char_p_no),
        ('cbPubArea', UInt32),
        ('pbPubArea', c_char_p_no),
    ]
    return WEBAUTHN_COMMON_ATTESTATION
def _define_WEBAUTHN_COSE_CREDENTIAL_PARAMETER_head():
    class WEBAUTHN_COSE_CREDENTIAL_PARAMETER(Structure):
        pass
    return WEBAUTHN_COSE_CREDENTIAL_PARAMETER
def _define_WEBAUTHN_COSE_CREDENTIAL_PARAMETER():
    WEBAUTHN_COSE_CREDENTIAL_PARAMETER = win32more.Networking.WindowsWebServices.WEBAUTHN_COSE_CREDENTIAL_PARAMETER_head
    WEBAUTHN_COSE_CREDENTIAL_PARAMETER._fields_ = [
        ('dwVersion', UInt32),
        ('pwszCredentialType', win32more.Foundation.PWSTR),
        ('lAlg', Int32),
    ]
    return WEBAUTHN_COSE_CREDENTIAL_PARAMETER
def _define_WEBAUTHN_COSE_CREDENTIAL_PARAMETERS_head():
    class WEBAUTHN_COSE_CREDENTIAL_PARAMETERS(Structure):
        pass
    return WEBAUTHN_COSE_CREDENTIAL_PARAMETERS
def _define_WEBAUTHN_COSE_CREDENTIAL_PARAMETERS():
    WEBAUTHN_COSE_CREDENTIAL_PARAMETERS = win32more.Networking.WindowsWebServices.WEBAUTHN_COSE_CREDENTIAL_PARAMETERS_head
    WEBAUTHN_COSE_CREDENTIAL_PARAMETERS._fields_ = [
        ('cCredentialParameters', UInt32),
        ('pCredentialParameters', POINTER(win32more.Networking.WindowsWebServices.WEBAUTHN_COSE_CREDENTIAL_PARAMETER_head)),
    ]
    return WEBAUTHN_COSE_CREDENTIAL_PARAMETERS
def _define_WEBAUTHN_CRED_BLOB_EXTENSION_head():
    class WEBAUTHN_CRED_BLOB_EXTENSION(Structure):
        pass
    return WEBAUTHN_CRED_BLOB_EXTENSION
def _define_WEBAUTHN_CRED_BLOB_EXTENSION():
    WEBAUTHN_CRED_BLOB_EXTENSION = win32more.Networking.WindowsWebServices.WEBAUTHN_CRED_BLOB_EXTENSION_head
    WEBAUTHN_CRED_BLOB_EXTENSION._fields_ = [
        ('cbCredBlob', UInt32),
        ('pbCredBlob', c_char_p_no),
    ]
    return WEBAUTHN_CRED_BLOB_EXTENSION
def _define_WEBAUTHN_CRED_PROTECT_EXTENSION_IN_head():
    class WEBAUTHN_CRED_PROTECT_EXTENSION_IN(Structure):
        pass
    return WEBAUTHN_CRED_PROTECT_EXTENSION_IN
def _define_WEBAUTHN_CRED_PROTECT_EXTENSION_IN():
    WEBAUTHN_CRED_PROTECT_EXTENSION_IN = win32more.Networking.WindowsWebServices.WEBAUTHN_CRED_PROTECT_EXTENSION_IN_head
    WEBAUTHN_CRED_PROTECT_EXTENSION_IN._fields_ = [
        ('dwCredProtect', UInt32),
        ('bRequireCredProtect', win32more.Foundation.BOOL),
    ]
    return WEBAUTHN_CRED_PROTECT_EXTENSION_IN
def _define_WEBAUTHN_CREDENTIAL_head():
    class WEBAUTHN_CREDENTIAL(Structure):
        pass
    return WEBAUTHN_CREDENTIAL
def _define_WEBAUTHN_CREDENTIAL():
    WEBAUTHN_CREDENTIAL = win32more.Networking.WindowsWebServices.WEBAUTHN_CREDENTIAL_head
    WEBAUTHN_CREDENTIAL._fields_ = [
        ('dwVersion', UInt32),
        ('cbId', UInt32),
        ('pbId', c_char_p_no),
        ('pwszCredentialType', win32more.Foundation.PWSTR),
    ]
    return WEBAUTHN_CREDENTIAL
def _define_WEBAUTHN_CREDENTIAL_ATTESTATION_head():
    class WEBAUTHN_CREDENTIAL_ATTESTATION(Structure):
        pass
    return WEBAUTHN_CREDENTIAL_ATTESTATION
def _define_WEBAUTHN_CREDENTIAL_ATTESTATION():
    WEBAUTHN_CREDENTIAL_ATTESTATION = win32more.Networking.WindowsWebServices.WEBAUTHN_CREDENTIAL_ATTESTATION_head
    WEBAUTHN_CREDENTIAL_ATTESTATION._fields_ = [
        ('dwVersion', UInt32),
        ('pwszFormatType', win32more.Foundation.PWSTR),
        ('cbAuthenticatorData', UInt32),
        ('pbAuthenticatorData', c_char_p_no),
        ('cbAttestation', UInt32),
        ('pbAttestation', c_char_p_no),
        ('dwAttestationDecodeType', UInt32),
        ('pvAttestationDecode', c_void_p),
        ('cbAttestationObject', UInt32),
        ('pbAttestationObject', c_char_p_no),
        ('cbCredentialId', UInt32),
        ('pbCredentialId', c_char_p_no),
        ('Extensions', win32more.Networking.WindowsWebServices.WEBAUTHN_EXTENSIONS),
        ('dwUsedTransport', UInt32),
        ('bEpAtt', win32more.Foundation.BOOL),
        ('bLargeBlobSupported', win32more.Foundation.BOOL),
        ('bResidentKey', win32more.Foundation.BOOL),
    ]
    return WEBAUTHN_CREDENTIAL_ATTESTATION
def _define_WEBAUTHN_CREDENTIAL_EX_head():
    class WEBAUTHN_CREDENTIAL_EX(Structure):
        pass
    return WEBAUTHN_CREDENTIAL_EX
def _define_WEBAUTHN_CREDENTIAL_EX():
    WEBAUTHN_CREDENTIAL_EX = win32more.Networking.WindowsWebServices.WEBAUTHN_CREDENTIAL_EX_head
    WEBAUTHN_CREDENTIAL_EX._fields_ = [
        ('dwVersion', UInt32),
        ('cbId', UInt32),
        ('pbId', c_char_p_no),
        ('pwszCredentialType', win32more.Foundation.PWSTR),
        ('dwTransports', UInt32),
    ]
    return WEBAUTHN_CREDENTIAL_EX
def _define_WEBAUTHN_CREDENTIAL_LIST_head():
    class WEBAUTHN_CREDENTIAL_LIST(Structure):
        pass
    return WEBAUTHN_CREDENTIAL_LIST
def _define_WEBAUTHN_CREDENTIAL_LIST():
    WEBAUTHN_CREDENTIAL_LIST = win32more.Networking.WindowsWebServices.WEBAUTHN_CREDENTIAL_LIST_head
    WEBAUTHN_CREDENTIAL_LIST._fields_ = [
        ('cCredentials', UInt32),
        ('ppCredentials', POINTER(POINTER(win32more.Networking.WindowsWebServices.WEBAUTHN_CREDENTIAL_EX_head))),
    ]
    return WEBAUTHN_CREDENTIAL_LIST
def _define_WEBAUTHN_CREDENTIALS_head():
    class WEBAUTHN_CREDENTIALS(Structure):
        pass
    return WEBAUTHN_CREDENTIALS
def _define_WEBAUTHN_CREDENTIALS():
    WEBAUTHN_CREDENTIALS = win32more.Networking.WindowsWebServices.WEBAUTHN_CREDENTIALS_head
    WEBAUTHN_CREDENTIALS._fields_ = [
        ('cCredentials', UInt32),
        ('pCredentials', POINTER(win32more.Networking.WindowsWebServices.WEBAUTHN_CREDENTIAL_head)),
    ]
    return WEBAUTHN_CREDENTIALS
def _define_WEBAUTHN_EXTENSION_head():
    class WEBAUTHN_EXTENSION(Structure):
        pass
    return WEBAUTHN_EXTENSION
def _define_WEBAUTHN_EXTENSION():
    WEBAUTHN_EXTENSION = win32more.Networking.WindowsWebServices.WEBAUTHN_EXTENSION_head
    WEBAUTHN_EXTENSION._fields_ = [
        ('pwszExtensionIdentifier', win32more.Foundation.PWSTR),
        ('cbExtension', UInt32),
        ('pvExtension', c_void_p),
    ]
    return WEBAUTHN_EXTENSION
def _define_WEBAUTHN_EXTENSIONS_head():
    class WEBAUTHN_EXTENSIONS(Structure):
        pass
    return WEBAUTHN_EXTENSIONS
def _define_WEBAUTHN_EXTENSIONS():
    WEBAUTHN_EXTENSIONS = win32more.Networking.WindowsWebServices.WEBAUTHN_EXTENSIONS_head
    WEBAUTHN_EXTENSIONS._fields_ = [
        ('cExtensions', UInt32),
        ('pExtensions', POINTER(win32more.Networking.WindowsWebServices.WEBAUTHN_EXTENSION_head)),
    ]
    return WEBAUTHN_EXTENSIONS
def _define_WEBAUTHN_RP_ENTITY_INFORMATION_head():
    class WEBAUTHN_RP_ENTITY_INFORMATION(Structure):
        pass
    return WEBAUTHN_RP_ENTITY_INFORMATION
def _define_WEBAUTHN_RP_ENTITY_INFORMATION():
    WEBAUTHN_RP_ENTITY_INFORMATION = win32more.Networking.WindowsWebServices.WEBAUTHN_RP_ENTITY_INFORMATION_head
    WEBAUTHN_RP_ENTITY_INFORMATION._fields_ = [
        ('dwVersion', UInt32),
        ('pwszId', win32more.Foundation.PWSTR),
        ('pwszName', win32more.Foundation.PWSTR),
        ('pwszIcon', win32more.Foundation.PWSTR),
    ]
    return WEBAUTHN_RP_ENTITY_INFORMATION
def _define_WEBAUTHN_USER_ENTITY_INFORMATION_head():
    class WEBAUTHN_USER_ENTITY_INFORMATION(Structure):
        pass
    return WEBAUTHN_USER_ENTITY_INFORMATION
def _define_WEBAUTHN_USER_ENTITY_INFORMATION():
    WEBAUTHN_USER_ENTITY_INFORMATION = win32more.Networking.WindowsWebServices.WEBAUTHN_USER_ENTITY_INFORMATION_head
    WEBAUTHN_USER_ENTITY_INFORMATION._fields_ = [
        ('dwVersion', UInt32),
        ('cbId', UInt32),
        ('pbId', c_char_p_no),
        ('pwszName', win32more.Foundation.PWSTR),
        ('pwszIcon', win32more.Foundation.PWSTR),
        ('pwszDisplayName', win32more.Foundation.PWSTR),
    ]
    return WEBAUTHN_USER_ENTITY_INFORMATION
def _define_WEBAUTHN_X5C_head():
    class WEBAUTHN_X5C(Structure):
        pass
    return WEBAUTHN_X5C
def _define_WEBAUTHN_X5C():
    WEBAUTHN_X5C = win32more.Networking.WindowsWebServices.WEBAUTHN_X5C_head
    WEBAUTHN_X5C._fields_ = [
        ('cbData', UInt32),
        ('pbData', c_char_p_no),
    ]
    return WEBAUTHN_X5C
def _define_WS_ABANDON_MESSAGE_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_ABORT_CHANNEL_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_ABORT_LISTENER_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_ACCEPT_CHANNEL_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
WS_ADDRESSING_VERSION = Int32
WS_ADDRESSING_VERSION_0_9 = 1
WS_ADDRESSING_VERSION_1_0 = 2
WS_ADDRESSING_VERSION_TRANSPORT = 3
def _define_WS_ANY_ATTRIBUTE_head():
    class WS_ANY_ATTRIBUTE(Structure):
        pass
    return WS_ANY_ATTRIBUTE
def _define_WS_ANY_ATTRIBUTE():
    WS_ANY_ATTRIBUTE = win32more.Networking.WindowsWebServices.WS_ANY_ATTRIBUTE_head
    WS_ANY_ATTRIBUTE._fields_ = [
        ('localName', win32more.Networking.WindowsWebServices.WS_XML_STRING),
        ('ns', win32more.Networking.WindowsWebServices.WS_XML_STRING),
        ('value', POINTER(win32more.Networking.WindowsWebServices.WS_XML_TEXT_head)),
    ]
    return WS_ANY_ATTRIBUTE
def _define_WS_ANY_ATTRIBUTES_head():
    class WS_ANY_ATTRIBUTES(Structure):
        pass
    return WS_ANY_ATTRIBUTES
def _define_WS_ANY_ATTRIBUTES():
    WS_ANY_ATTRIBUTES = win32more.Networking.WindowsWebServices.WS_ANY_ATTRIBUTES_head
    WS_ANY_ATTRIBUTES._fields_ = [
        ('attributes', POINTER(win32more.Networking.WindowsWebServices.WS_ANY_ATTRIBUTE_head)),
        ('attributeCount', UInt32),
    ]
    return WS_ANY_ATTRIBUTES
def _define_WS_ASYNC_CALLBACK():
    return WINFUNCTYPE(Void,win32more.Foundation.HRESULT,win32more.Networking.WindowsWebServices.WS_CALLBACK_MODEL,c_void_p)
def _define_WS_ASYNC_CONTEXT_head():
    class WS_ASYNC_CONTEXT(Structure):
        pass
    return WS_ASYNC_CONTEXT
def _define_WS_ASYNC_CONTEXT():
    WS_ASYNC_CONTEXT = win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head
    WS_ASYNC_CONTEXT._fields_ = [
        ('callback', win32more.Networking.WindowsWebServices.WS_ASYNC_CALLBACK),
        ('callbackState', c_void_p),
    ]
    return WS_ASYNC_CONTEXT
def _define_WS_ASYNC_FUNCTION():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HRESULT,win32more.Networking.WindowsWebServices.WS_CALLBACK_MODEL,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_OPERATION_head),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_ASYNC_OPERATION_head():
    class WS_ASYNC_OPERATION(Structure):
        pass
    return WS_ASYNC_OPERATION
def _define_WS_ASYNC_OPERATION():
    WS_ASYNC_OPERATION = win32more.Networking.WindowsWebServices.WS_ASYNC_OPERATION_head
    WS_ASYNC_OPERATION._fields_ = [
        ('function', win32more.Networking.WindowsWebServices.WS_ASYNC_FUNCTION),
    ]
    return WS_ASYNC_OPERATION
def _define_WS_ASYNC_STATE_head():
    class WS_ASYNC_STATE(Structure):
        pass
    return WS_ASYNC_STATE
def _define_WS_ASYNC_STATE():
    WS_ASYNC_STATE = win32more.Networking.WindowsWebServices.WS_ASYNC_STATE_head
    WS_ASYNC_STATE._fields_ = [
        ('internal0', c_void_p),
        ('internal1', c_void_p),
        ('internal2', c_void_p),
        ('internal3', c_void_p),
        ('internal4', c_void_p),
    ]
    return WS_ASYNC_STATE
def _define_WS_ATTRIBUTE_DESCRIPTION_head():
    class WS_ATTRIBUTE_DESCRIPTION(Structure):
        pass
    return WS_ATTRIBUTE_DESCRIPTION
def _define_WS_ATTRIBUTE_DESCRIPTION():
    WS_ATTRIBUTE_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_ATTRIBUTE_DESCRIPTION_head
    WS_ATTRIBUTE_DESCRIPTION._fields_ = [
        ('attributeLocalName', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('attributeNs', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('type', win32more.Networking.WindowsWebServices.WS_TYPE),
        ('typeDescription', c_void_p),
    ]
    return WS_ATTRIBUTE_DESCRIPTION
WS_BINDING_TEMPLATE_TYPE = Int32
WS_HTTP_BINDING_TEMPLATE_TYPE = 0
WS_HTTP_SSL_BINDING_TEMPLATE_TYPE = 1
WS_HTTP_HEADER_AUTH_BINDING_TEMPLATE_TYPE = 2
WS_HTTP_SSL_HEADER_AUTH_BINDING_TEMPLATE_TYPE = 3
WS_HTTP_SSL_USERNAME_BINDING_TEMPLATE_TYPE = 4
WS_HTTP_SSL_KERBEROS_APREQ_BINDING_TEMPLATE_TYPE = 5
WS_TCP_BINDING_TEMPLATE_TYPE = 6
WS_TCP_SSPI_BINDING_TEMPLATE_TYPE = 7
WS_TCP_SSPI_USERNAME_BINDING_TEMPLATE_TYPE = 8
WS_TCP_SSPI_KERBEROS_APREQ_BINDING_TEMPLATE_TYPE = 9
WS_HTTP_SSL_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE_TYPE = 10
WS_HTTP_SSL_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE_TYPE = 11
WS_TCP_SSPI_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE_TYPE = 12
WS_TCP_SSPI_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE_TYPE = 13
def _define_WS_BOOL_DESCRIPTION_head():
    class WS_BOOL_DESCRIPTION(Structure):
        pass
    return WS_BOOL_DESCRIPTION
def _define_WS_BOOL_DESCRIPTION():
    WS_BOOL_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_BOOL_DESCRIPTION_head
    WS_BOOL_DESCRIPTION._fields_ = [
        ('value', win32more.Foundation.BOOL),
    ]
    return WS_BOOL_DESCRIPTION
def _define_WS_BUFFERS_head():
    class WS_BUFFERS(Structure):
        pass
    return WS_BUFFERS
def _define_WS_BUFFERS():
    WS_BUFFERS = win32more.Networking.WindowsWebServices.WS_BUFFERS_head
    WS_BUFFERS._fields_ = [
        ('bufferCount', UInt32),
        ('buffers', POINTER(win32more.Networking.WindowsWebServices.WS_BYTES_head)),
    ]
    return WS_BUFFERS
def _define_WS_BYTE_ARRAY_DESCRIPTION_head():
    class WS_BYTE_ARRAY_DESCRIPTION(Structure):
        pass
    return WS_BYTE_ARRAY_DESCRIPTION
def _define_WS_BYTE_ARRAY_DESCRIPTION():
    WS_BYTE_ARRAY_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_BYTE_ARRAY_DESCRIPTION_head
    WS_BYTE_ARRAY_DESCRIPTION._fields_ = [
        ('minByteCount', UInt32),
        ('maxByteCount', UInt32),
    ]
    return WS_BYTE_ARRAY_DESCRIPTION
def _define_WS_BYTES_head():
    class WS_BYTES(Structure):
        pass
    return WS_BYTES
def _define_WS_BYTES():
    WS_BYTES = win32more.Networking.WindowsWebServices.WS_BYTES_head
    WS_BYTES._fields_ = [
        ('length', UInt32),
        ('bytes', c_char_p_no),
    ]
    return WS_BYTES
def _define_WS_BYTES_DESCRIPTION_head():
    class WS_BYTES_DESCRIPTION(Structure):
        pass
    return WS_BYTES_DESCRIPTION
def _define_WS_BYTES_DESCRIPTION():
    WS_BYTES_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_BYTES_DESCRIPTION_head
    WS_BYTES_DESCRIPTION._fields_ = [
        ('minByteCount', UInt32),
        ('maxByteCount', UInt32),
    ]
    return WS_BYTES_DESCRIPTION
def _define_WS_CALL_PROPERTY_head():
    class WS_CALL_PROPERTY(Structure):
        pass
    return WS_CALL_PROPERTY
def _define_WS_CALL_PROPERTY():
    WS_CALL_PROPERTY = win32more.Networking.WindowsWebServices.WS_CALL_PROPERTY_head
    WS_CALL_PROPERTY._fields_ = [
        ('id', win32more.Networking.WindowsWebServices.WS_CALL_PROPERTY_ID),
        ('value', c_void_p),
        ('valueSize', UInt32),
    ]
    return WS_CALL_PROPERTY
WS_CALL_PROPERTY_ID = Int32
WS_CALL_PROPERTY_CHECK_MUST_UNDERSTAND = 0
WS_CALL_PROPERTY_SEND_MESSAGE_CONTEXT = 1
WS_CALL_PROPERTY_RECEIVE_MESSAGE_CONTEXT = 2
WS_CALL_PROPERTY_CALL_ID = 3
WS_CALLBACK_MODEL = Int32
WS_SHORT_CALLBACK = 0
WS_LONG_CALLBACK = 1
def _define_WS_CAPI_ASYMMETRIC_SECURITY_KEY_HANDLE_head():
    class WS_CAPI_ASYMMETRIC_SECURITY_KEY_HANDLE(Structure):
        pass
    return WS_CAPI_ASYMMETRIC_SECURITY_KEY_HANDLE
def _define_WS_CAPI_ASYMMETRIC_SECURITY_KEY_HANDLE():
    WS_CAPI_ASYMMETRIC_SECURITY_KEY_HANDLE = win32more.Networking.WindowsWebServices.WS_CAPI_ASYMMETRIC_SECURITY_KEY_HANDLE_head
    WS_CAPI_ASYMMETRIC_SECURITY_KEY_HANDLE._fields_ = [
        ('keyHandle', win32more.Networking.WindowsWebServices.WS_SECURITY_KEY_HANDLE),
        ('provider', UIntPtr),
        ('keySpec', UInt32),
    ]
    return WS_CAPI_ASYMMETRIC_SECURITY_KEY_HANDLE
def _define_WS_CERT_CREDENTIAL_head():
    class WS_CERT_CREDENTIAL(Structure):
        pass
    return WS_CERT_CREDENTIAL
def _define_WS_CERT_CREDENTIAL():
    WS_CERT_CREDENTIAL = win32more.Networking.WindowsWebServices.WS_CERT_CREDENTIAL_head
    WS_CERT_CREDENTIAL._fields_ = [
        ('credentialType', win32more.Networking.WindowsWebServices.WS_CERT_CREDENTIAL_TYPE),
    ]
    return WS_CERT_CREDENTIAL
WS_CERT_CREDENTIAL_TYPE = Int32
WS_SUBJECT_NAME_CERT_CREDENTIAL_TYPE = 1
WS_THUMBPRINT_CERT_CREDENTIAL_TYPE = 2
WS_CUSTOM_CERT_CREDENTIAL_TYPE = 3
def _define_WS_CERT_ENDPOINT_IDENTITY_head():
    class WS_CERT_ENDPOINT_IDENTITY(Structure):
        pass
    return WS_CERT_ENDPOINT_IDENTITY
def _define_WS_CERT_ENDPOINT_IDENTITY():
    WS_CERT_ENDPOINT_IDENTITY = win32more.Networking.WindowsWebServices.WS_CERT_ENDPOINT_IDENTITY_head
    WS_CERT_ENDPOINT_IDENTITY._fields_ = [
        ('identity', win32more.Networking.WindowsWebServices.WS_ENDPOINT_IDENTITY),
        ('rawCertificateData', win32more.Networking.WindowsWebServices.WS_BYTES),
    ]
    return WS_CERT_ENDPOINT_IDENTITY
def _define_WS_CERT_ISSUER_LIST_NOTIFICATION_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Security.Authentication.Identity.SecPkgContext_IssuerListInfoEx_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_CERT_MESSAGE_SECURITY_BINDING_CONSTRAINT_head():
    class WS_CERT_MESSAGE_SECURITY_BINDING_CONSTRAINT(Structure):
        pass
    return WS_CERT_MESSAGE_SECURITY_BINDING_CONSTRAINT
def _define_WS_CERT_MESSAGE_SECURITY_BINDING_CONSTRAINT():
    WS_CERT_MESSAGE_SECURITY_BINDING_CONSTRAINT = win32more.Networking.WindowsWebServices.WS_CERT_MESSAGE_SECURITY_BINDING_CONSTRAINT_head
    WS_CERT_MESSAGE_SECURITY_BINDING_CONSTRAINT._fields_ = [
        ('bindingConstraint', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT),
        ('bindingUsage', win32more.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE),
    ]
    return WS_CERT_MESSAGE_SECURITY_BINDING_CONSTRAINT
def _define_WS_CERT_SIGNED_SAML_AUTHENTICATOR_head():
    class WS_CERT_SIGNED_SAML_AUTHENTICATOR(Structure):
        pass
    return WS_CERT_SIGNED_SAML_AUTHENTICATOR
def _define_WS_CERT_SIGNED_SAML_AUTHENTICATOR():
    WS_CERT_SIGNED_SAML_AUTHENTICATOR = win32more.Networking.WindowsWebServices.WS_CERT_SIGNED_SAML_AUTHENTICATOR_head
    WS_CERT_SIGNED_SAML_AUTHENTICATOR._fields_ = [
        ('authenticator', win32more.Networking.WindowsWebServices.WS_SAML_AUTHENTICATOR),
        ('trustedIssuerCerts', POINTER(POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head))),
        ('trustedIssuerCertCount', UInt32),
        ('decryptionCert', POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)),
        ('samlValidator', win32more.Networking.WindowsWebServices.WS_VALIDATE_SAML_CALLBACK),
        ('samlValidatorCallbackState', c_void_p),
    ]
    return WS_CERT_SIGNED_SAML_AUTHENTICATOR
def _define_WS_CERTIFICATE_VALIDATION_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head),c_void_p)
def _define_WS_CERTIFICATE_VALIDATION_CALLBACK_CONTEXT_head():
    class WS_CERTIFICATE_VALIDATION_CALLBACK_CONTEXT(Structure):
        pass
    return WS_CERTIFICATE_VALIDATION_CALLBACK_CONTEXT
def _define_WS_CERTIFICATE_VALIDATION_CALLBACK_CONTEXT():
    WS_CERTIFICATE_VALIDATION_CALLBACK_CONTEXT = win32more.Networking.WindowsWebServices.WS_CERTIFICATE_VALIDATION_CALLBACK_CONTEXT_head
    WS_CERTIFICATE_VALIDATION_CALLBACK_CONTEXT._fields_ = [
        ('callback', win32more.Networking.WindowsWebServices.WS_CERTIFICATE_VALIDATION_CALLBACK),
        ('state', c_void_p),
    ]
    return WS_CERTIFICATE_VALIDATION_CALLBACK_CONTEXT
def _define_WS_CHANNEL_head():
    class WS_CHANNEL(Structure):
        pass
    return WS_CHANNEL
def _define_WS_CHANNEL():
    WS_CHANNEL = win32more.Networking.WindowsWebServices.WS_CHANNEL_head
    return WS_CHANNEL
WS_CHANNEL_BINDING = Int32
WS_HTTP_CHANNEL_BINDING = 0
WS_TCP_CHANNEL_BINDING = 1
WS_UDP_CHANNEL_BINDING = 2
WS_CUSTOM_CHANNEL_BINDING = 3
WS_NAMEDPIPE_CHANNEL_BINDING = 4
def _define_WS_CHANNEL_DECODER_head():
    class WS_CHANNEL_DECODER(Structure):
        pass
    return WS_CHANNEL_DECODER
def _define_WS_CHANNEL_DECODER():
    WS_CHANNEL_DECODER = win32more.Networking.WindowsWebServices.WS_CHANNEL_DECODER_head
    WS_CHANNEL_DECODER._fields_ = [
        ('createContext', c_void_p),
        ('createDecoderCallback', win32more.Networking.WindowsWebServices.WS_CREATE_DECODER_CALLBACK),
        ('decoderGetContentTypeCallback', win32more.Networking.WindowsWebServices.WS_DECODER_GET_CONTENT_TYPE_CALLBACK),
        ('decoderStartCallback', win32more.Networking.WindowsWebServices.WS_DECODER_START_CALLBACK),
        ('decoderDecodeCallback', win32more.Networking.WindowsWebServices.WS_DECODER_DECODE_CALLBACK),
        ('decoderEndCallback', win32more.Networking.WindowsWebServices.WS_DECODER_END_CALLBACK),
        ('freeDecoderCallback', win32more.Networking.WindowsWebServices.WS_FREE_DECODER_CALLBACK),
    ]
    return WS_CHANNEL_DECODER
def _define_WS_CHANNEL_ENCODER_head():
    class WS_CHANNEL_ENCODER(Structure):
        pass
    return WS_CHANNEL_ENCODER
def _define_WS_CHANNEL_ENCODER():
    WS_CHANNEL_ENCODER = win32more.Networking.WindowsWebServices.WS_CHANNEL_ENCODER_head
    WS_CHANNEL_ENCODER._fields_ = [
        ('createContext', c_void_p),
        ('createEncoderCallback', win32more.Networking.WindowsWebServices.WS_CREATE_ENCODER_CALLBACK),
        ('encoderGetContentTypeCallback', win32more.Networking.WindowsWebServices.WS_ENCODER_GET_CONTENT_TYPE_CALLBACK),
        ('encoderStartCallback', win32more.Networking.WindowsWebServices.WS_ENCODER_START_CALLBACK),
        ('encoderEncodeCallback', win32more.Networking.WindowsWebServices.WS_ENCODER_ENCODE_CALLBACK),
        ('encoderEndCallback', win32more.Networking.WindowsWebServices.WS_ENCODER_END_CALLBACK),
        ('freeEncoderCallback', win32more.Networking.WindowsWebServices.WS_FREE_ENCODER_CALLBACK),
    ]
    return WS_CHANNEL_ENCODER
def _define_WS_CHANNEL_PROPERTIES_head():
    class WS_CHANNEL_PROPERTIES(Structure):
        pass
    return WS_CHANNEL_PROPERTIES
def _define_WS_CHANNEL_PROPERTIES():
    WS_CHANNEL_PROPERTIES = win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES_head
    WS_CHANNEL_PROPERTIES._fields_ = [
        ('properties', POINTER(win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_head)),
        ('propertyCount', UInt32),
    ]
    return WS_CHANNEL_PROPERTIES
def _define_WS_CHANNEL_PROPERTY_head():
    class WS_CHANNEL_PROPERTY(Structure):
        pass
    return WS_CHANNEL_PROPERTY
def _define_WS_CHANNEL_PROPERTY():
    WS_CHANNEL_PROPERTY = win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_head
    WS_CHANNEL_PROPERTY._fields_ = [
        ('id', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID),
        ('value', c_void_p),
        ('valueSize', UInt32),
    ]
    return WS_CHANNEL_PROPERTY
def _define_WS_CHANNEL_PROPERTY_CONSTRAINT_head():
    class WS_CHANNEL_PROPERTY_CONSTRAINT(Structure):
        pass
    return WS_CHANNEL_PROPERTY_CONSTRAINT
def _define_WS_CHANNEL_PROPERTY_CONSTRAINT():
    WS_CHANNEL_PROPERTY_CONSTRAINT = win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_CONSTRAINT_head
    class WS_CHANNEL_PROPERTY_CONSTRAINT__out_e__Struct(Structure):
        pass
    WS_CHANNEL_PROPERTY_CONSTRAINT__out_e__Struct._fields_ = [
        ('channelProperty', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY),
    ]
    WS_CHANNEL_PROPERTY_CONSTRAINT._fields_ = [
        ('id', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID),
        ('allowedValues', c_void_p),
        ('allowedValuesSize', UInt32),
        ('out', WS_CHANNEL_PROPERTY_CONSTRAINT__out_e__Struct),
    ]
    return WS_CHANNEL_PROPERTY_CONSTRAINT
WS_CHANNEL_PROPERTY_ID = Int32
WS_CHANNEL_PROPERTY_MAX_BUFFERED_MESSAGE_SIZE = 0
WS_CHANNEL_PROPERTY_MAX_STREAMED_MESSAGE_SIZE = 1
WS_CHANNEL_PROPERTY_MAX_STREAMED_START_SIZE = 2
WS_CHANNEL_PROPERTY_MAX_STREAMED_FLUSH_SIZE = 3
WS_CHANNEL_PROPERTY_ENCODING = 4
WS_CHANNEL_PROPERTY_ENVELOPE_VERSION = 5
WS_CHANNEL_PROPERTY_ADDRESSING_VERSION = 6
WS_CHANNEL_PROPERTY_MAX_SESSION_DICTIONARY_SIZE = 7
WS_CHANNEL_PROPERTY_STATE = 8
WS_CHANNEL_PROPERTY_ASYNC_CALLBACK_MODEL = 9
WS_CHANNEL_PROPERTY_IP_VERSION = 10
WS_CHANNEL_PROPERTY_RESOLVE_TIMEOUT = 11
WS_CHANNEL_PROPERTY_CONNECT_TIMEOUT = 12
WS_CHANNEL_PROPERTY_SEND_TIMEOUT = 13
WS_CHANNEL_PROPERTY_RECEIVE_RESPONSE_TIMEOUT = 14
WS_CHANNEL_PROPERTY_RECEIVE_TIMEOUT = 15
WS_CHANNEL_PROPERTY_CLOSE_TIMEOUT = 16
WS_CHANNEL_PROPERTY_ENABLE_TIMEOUTS = 17
WS_CHANNEL_PROPERTY_TRANSFER_MODE = 18
WS_CHANNEL_PROPERTY_MULTICAST_INTERFACE = 19
WS_CHANNEL_PROPERTY_MULTICAST_HOPS = 20
WS_CHANNEL_PROPERTY_REMOTE_ADDRESS = 21
WS_CHANNEL_PROPERTY_REMOTE_IP_ADDRESS = 22
WS_CHANNEL_PROPERTY_HTTP_CONNECTION_ID = 23
WS_CHANNEL_PROPERTY_CUSTOM_CHANNEL_CALLBACKS = 24
WS_CHANNEL_PROPERTY_CUSTOM_CHANNEL_PARAMETERS = 25
WS_CHANNEL_PROPERTY_CUSTOM_CHANNEL_INSTANCE = 26
WS_CHANNEL_PROPERTY_TRANSPORT_URL = 27
WS_CHANNEL_PROPERTY_NO_DELAY = 28
WS_CHANNEL_PROPERTY_SEND_KEEP_ALIVES = 29
WS_CHANNEL_PROPERTY_KEEP_ALIVE_TIME = 30
WS_CHANNEL_PROPERTY_KEEP_ALIVE_INTERVAL = 31
WS_CHANNEL_PROPERTY_MAX_HTTP_SERVER_CONNECTIONS = 32
WS_CHANNEL_PROPERTY_IS_SESSION_SHUT_DOWN = 33
WS_CHANNEL_PROPERTY_CHANNEL_TYPE = 34
WS_CHANNEL_PROPERTY_TRIM_BUFFERED_MESSAGE_SIZE = 35
WS_CHANNEL_PROPERTY_ENCODER = 36
WS_CHANNEL_PROPERTY_DECODER = 37
WS_CHANNEL_PROPERTY_PROTECTION_LEVEL = 38
WS_CHANNEL_PROPERTY_COOKIE_MODE = 39
WS_CHANNEL_PROPERTY_HTTP_PROXY_SETTING_MODE = 40
WS_CHANNEL_PROPERTY_CUSTOM_HTTP_PROXY = 41
WS_CHANNEL_PROPERTY_HTTP_MESSAGE_MAPPING = 42
WS_CHANNEL_PROPERTY_ENABLE_HTTP_REDIRECT = 43
WS_CHANNEL_PROPERTY_HTTP_REDIRECT_CALLBACK_CONTEXT = 44
WS_CHANNEL_PROPERTY_FAULTS_AS_ERRORS = 45
WS_CHANNEL_PROPERTY_ALLOW_UNSECURED_FAULTS = 46
WS_CHANNEL_PROPERTY_HTTP_SERVER_SPN = 47
WS_CHANNEL_PROPERTY_HTTP_PROXY_SPN = 48
WS_CHANNEL_PROPERTY_MAX_HTTP_REQUEST_HEADERS_BUFFER_SIZE = 49
WS_CHANNEL_STATE = Int32
WS_CHANNEL_STATE_CREATED = 0
WS_CHANNEL_STATE_OPENING = 1
WS_CHANNEL_STATE_ACCEPTING = 2
WS_CHANNEL_STATE_OPEN = 3
WS_CHANNEL_STATE_FAULTED = 4
WS_CHANNEL_STATE_CLOSING = 5
WS_CHANNEL_STATE_CLOSED = 6
WS_CHANNEL_TYPE = Int32
WS_CHANNEL_TYPE_INPUT = 1
WS_CHANNEL_TYPE_OUTPUT = 2
WS_CHANNEL_TYPE_SESSION = 4
WS_CHANNEL_TYPE_INPUT_SESSION = 5
WS_CHANNEL_TYPE_OUTPUT_SESSION = 6
WS_CHANNEL_TYPE_DUPLEX = 3
WS_CHANNEL_TYPE_DUPLEX_SESSION = 7
WS_CHANNEL_TYPE_REQUEST = 8
WS_CHANNEL_TYPE_REPLY = 16
def _define_WS_CHAR_ARRAY_DESCRIPTION_head():
    class WS_CHAR_ARRAY_DESCRIPTION(Structure):
        pass
    return WS_CHAR_ARRAY_DESCRIPTION
def _define_WS_CHAR_ARRAY_DESCRIPTION():
    WS_CHAR_ARRAY_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_CHAR_ARRAY_DESCRIPTION_head
    WS_CHAR_ARRAY_DESCRIPTION._fields_ = [
        ('minCharCount', UInt32),
        ('maxCharCount', UInt32),
    ]
    return WS_CHAR_ARRAY_DESCRIPTION
WS_CHARSET = Int32
WS_CHARSET_AUTO = 0
WS_CHARSET_UTF8 = 1
WS_CHARSET_UTF16LE = 2
WS_CHARSET_UTF16BE = 3
def _define_WS_CLOSE_CHANNEL_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_CLOSE_LISTENER_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_CONTRACT_DESCRIPTION_head():
    class WS_CONTRACT_DESCRIPTION(Structure):
        pass
    return WS_CONTRACT_DESCRIPTION
def _define_WS_CONTRACT_DESCRIPTION():
    WS_CONTRACT_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_CONTRACT_DESCRIPTION_head
    WS_CONTRACT_DESCRIPTION._fields_ = [
        ('operationCount', UInt32),
        ('operations', POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_OPERATION_DESCRIPTION_head))),
    ]
    return WS_CONTRACT_DESCRIPTION
WS_COOKIE_MODE = Int32
WS_MANUAL_COOKIE_MODE = 1
WS_AUTO_COOKIE_MODE = 2
def _define_WS_CREATE_CHANNEL_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.WindowsWebServices.WS_CHANNEL_TYPE,c_void_p,UInt32,POINTER(c_void_p),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_CREATE_CHANNEL_FOR_LISTENER_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,c_void_p,UInt32,POINTER(c_void_p),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_CREATE_DECODER_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Networking.WindowsWebServices.WS_READ_CALLBACK,c_void_p,POINTER(c_void_p),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_CREATE_ENCODER_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Networking.WindowsWebServices.WS_WRITE_CALLBACK,c_void_p,POINTER(c_void_p),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_CREATE_LISTENER_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Networking.WindowsWebServices.WS_CHANNEL_TYPE,c_void_p,UInt32,POINTER(c_void_p),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_CUSTOM_CERT_CREDENTIAL_head():
    class WS_CUSTOM_CERT_CREDENTIAL(Structure):
        pass
    return WS_CUSTOM_CERT_CREDENTIAL
def _define_WS_CUSTOM_CERT_CREDENTIAL():
    WS_CUSTOM_CERT_CREDENTIAL = win32more.Networking.WindowsWebServices.WS_CUSTOM_CERT_CREDENTIAL_head
    WS_CUSTOM_CERT_CREDENTIAL._fields_ = [
        ('credential', win32more.Networking.WindowsWebServices.WS_CERT_CREDENTIAL),
        ('getCertCallback', win32more.Networking.WindowsWebServices.WS_GET_CERT_CALLBACK),
        ('getCertCallbackState', c_void_p),
        ('certIssuerListNotificationCallback', win32more.Networking.WindowsWebServices.WS_CERT_ISSUER_LIST_NOTIFICATION_CALLBACK),
        ('certIssuerListNotificationCallbackState', c_void_p),
    ]
    return WS_CUSTOM_CERT_CREDENTIAL
def _define_WS_CUSTOM_CHANNEL_CALLBACKS_head():
    class WS_CUSTOM_CHANNEL_CALLBACKS(Structure):
        pass
    return WS_CUSTOM_CHANNEL_CALLBACKS
def _define_WS_CUSTOM_CHANNEL_CALLBACKS():
    WS_CUSTOM_CHANNEL_CALLBACKS = win32more.Networking.WindowsWebServices.WS_CUSTOM_CHANNEL_CALLBACKS_head
    WS_CUSTOM_CHANNEL_CALLBACKS._fields_ = [
        ('createChannelCallback', win32more.Networking.WindowsWebServices.WS_CREATE_CHANNEL_CALLBACK),
        ('freeChannelCallback', win32more.Networking.WindowsWebServices.WS_FREE_CHANNEL_CALLBACK),
        ('resetChannelCallback', win32more.Networking.WindowsWebServices.WS_RESET_CHANNEL_CALLBACK),
        ('openChannelCallback', win32more.Networking.WindowsWebServices.WS_OPEN_CHANNEL_CALLBACK),
        ('closeChannelCallback', win32more.Networking.WindowsWebServices.WS_CLOSE_CHANNEL_CALLBACK),
        ('abortChannelCallback', win32more.Networking.WindowsWebServices.WS_ABORT_CHANNEL_CALLBACK),
        ('getChannelPropertyCallback', win32more.Networking.WindowsWebServices.WS_GET_CHANNEL_PROPERTY_CALLBACK),
        ('setChannelPropertyCallback', win32more.Networking.WindowsWebServices.WS_SET_CHANNEL_PROPERTY_CALLBACK),
        ('writeMessageStartCallback', win32more.Networking.WindowsWebServices.WS_WRITE_MESSAGE_START_CALLBACK),
        ('writeMessageEndCallback', win32more.Networking.WindowsWebServices.WS_WRITE_MESSAGE_END_CALLBACK),
        ('readMessageStartCallback', win32more.Networking.WindowsWebServices.WS_READ_MESSAGE_START_CALLBACK),
        ('readMessageEndCallback', win32more.Networking.WindowsWebServices.WS_READ_MESSAGE_END_CALLBACK),
        ('abandonMessageCallback', win32more.Networking.WindowsWebServices.WS_ABANDON_MESSAGE_CALLBACK),
        ('shutdownSessionChannelCallback', win32more.Networking.WindowsWebServices.WS_SHUTDOWN_SESSION_CHANNEL_CALLBACK),
    ]
    return WS_CUSTOM_CHANNEL_CALLBACKS
def _define_WS_CUSTOM_HTTP_PROXY_head():
    class WS_CUSTOM_HTTP_PROXY(Structure):
        pass
    return WS_CUSTOM_HTTP_PROXY
def _define_WS_CUSTOM_HTTP_PROXY():
    WS_CUSTOM_HTTP_PROXY = win32more.Networking.WindowsWebServices.WS_CUSTOM_HTTP_PROXY_head
    WS_CUSTOM_HTTP_PROXY._fields_ = [
        ('servers', win32more.Networking.WindowsWebServices.WS_STRING),
        ('bypass', win32more.Networking.WindowsWebServices.WS_STRING),
    ]
    return WS_CUSTOM_HTTP_PROXY
def _define_WS_CUSTOM_LISTENER_CALLBACKS_head():
    class WS_CUSTOM_LISTENER_CALLBACKS(Structure):
        pass
    return WS_CUSTOM_LISTENER_CALLBACKS
def _define_WS_CUSTOM_LISTENER_CALLBACKS():
    WS_CUSTOM_LISTENER_CALLBACKS = win32more.Networking.WindowsWebServices.WS_CUSTOM_LISTENER_CALLBACKS_head
    WS_CUSTOM_LISTENER_CALLBACKS._fields_ = [
        ('createListenerCallback', win32more.Networking.WindowsWebServices.WS_CREATE_LISTENER_CALLBACK),
        ('freeListenerCallback', win32more.Networking.WindowsWebServices.WS_FREE_LISTENER_CALLBACK),
        ('resetListenerCallback', win32more.Networking.WindowsWebServices.WS_RESET_LISTENER_CALLBACK),
        ('openListenerCallback', win32more.Networking.WindowsWebServices.WS_OPEN_LISTENER_CALLBACK),
        ('closeListenerCallback', win32more.Networking.WindowsWebServices.WS_CLOSE_LISTENER_CALLBACK),
        ('abortListenerCallback', win32more.Networking.WindowsWebServices.WS_ABORT_LISTENER_CALLBACK),
        ('getListenerPropertyCallback', win32more.Networking.WindowsWebServices.WS_GET_LISTENER_PROPERTY_CALLBACK),
        ('setListenerPropertyCallback', win32more.Networking.WindowsWebServices.WS_SET_LISTENER_PROPERTY_CALLBACK),
        ('createChannelForListenerCallback', win32more.Networking.WindowsWebServices.WS_CREATE_CHANNEL_FOR_LISTENER_CALLBACK),
        ('acceptChannelCallback', win32more.Networking.WindowsWebServices.WS_ACCEPT_CHANNEL_CALLBACK),
    ]
    return WS_CUSTOM_LISTENER_CALLBACKS
def _define_WS_CUSTOM_TYPE_DESCRIPTION_head():
    class WS_CUSTOM_TYPE_DESCRIPTION(Structure):
        pass
    return WS_CUSTOM_TYPE_DESCRIPTION
def _define_WS_CUSTOM_TYPE_DESCRIPTION():
    WS_CUSTOM_TYPE_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_CUSTOM_TYPE_DESCRIPTION_head
    WS_CUSTOM_TYPE_DESCRIPTION._fields_ = [
        ('size', UInt32),
        ('alignment', UInt32),
        ('readCallback', win32more.Networking.WindowsWebServices.WS_READ_TYPE_CALLBACK),
        ('writeCallback', win32more.Networking.WindowsWebServices.WS_WRITE_TYPE_CALLBACK),
        ('descriptionData', c_void_p),
        ('isDefaultValueCallback', win32more.Networking.WindowsWebServices.WS_IS_DEFAULT_VALUE_CALLBACK),
    ]
    return WS_CUSTOM_TYPE_DESCRIPTION
def _define_WS_DATETIME_head():
    class WS_DATETIME(Structure):
        pass
    return WS_DATETIME
def _define_WS_DATETIME():
    WS_DATETIME = win32more.Networking.WindowsWebServices.WS_DATETIME_head
    WS_DATETIME._fields_ = [
        ('ticks', UInt64),
        ('format', win32more.Networking.WindowsWebServices.WS_DATETIME_FORMAT),
    ]
    return WS_DATETIME
def _define_WS_DATETIME_DESCRIPTION_head():
    class WS_DATETIME_DESCRIPTION(Structure):
        pass
    return WS_DATETIME_DESCRIPTION
def _define_WS_DATETIME_DESCRIPTION():
    WS_DATETIME_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_DATETIME_DESCRIPTION_head
    WS_DATETIME_DESCRIPTION._fields_ = [
        ('minValue', win32more.Networking.WindowsWebServices.WS_DATETIME),
        ('maxValue', win32more.Networking.WindowsWebServices.WS_DATETIME),
    ]
    return WS_DATETIME_DESCRIPTION
WS_DATETIME_FORMAT = Int32
WS_DATETIME_FORMAT_UTC = 0
WS_DATETIME_FORMAT_LOCAL = 1
WS_DATETIME_FORMAT_NONE = 2
def _define_WS_DECIMAL_DESCRIPTION_head():
    class WS_DECIMAL_DESCRIPTION(Structure):
        pass
    return WS_DECIMAL_DESCRIPTION
def _define_WS_DECIMAL_DESCRIPTION():
    WS_DECIMAL_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_DECIMAL_DESCRIPTION_head
    WS_DECIMAL_DESCRIPTION._fields_ = [
        ('minValue', win32more.Foundation.DECIMAL),
        ('maxValue', win32more.Foundation.DECIMAL),
    ]
    return WS_DECIMAL_DESCRIPTION
def _define_WS_DECODER_DECODE_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,c_void_p,UInt32,POINTER(UInt32),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_DECODER_END_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_DECODER_GET_CONTENT_TYPE_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_DECODER_START_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_DEFAULT_VALUE_head():
    class WS_DEFAULT_VALUE(Structure):
        pass
    return WS_DEFAULT_VALUE
def _define_WS_DEFAULT_VALUE():
    WS_DEFAULT_VALUE = win32more.Networking.WindowsWebServices.WS_DEFAULT_VALUE_head
    WS_DEFAULT_VALUE._fields_ = [
        ('value', c_void_p),
        ('valueSize', UInt32),
    ]
    return WS_DEFAULT_VALUE
def _define_WS_DEFAULT_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_head():
    class WS_DEFAULT_WINDOWS_INTEGRATED_AUTH_CREDENTIAL(Structure):
        pass
    return WS_DEFAULT_WINDOWS_INTEGRATED_AUTH_CREDENTIAL
def _define_WS_DEFAULT_WINDOWS_INTEGRATED_AUTH_CREDENTIAL():
    WS_DEFAULT_WINDOWS_INTEGRATED_AUTH_CREDENTIAL = win32more.Networking.WindowsWebServices.WS_DEFAULT_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_head
    WS_DEFAULT_WINDOWS_INTEGRATED_AUTH_CREDENTIAL._fields_ = [
        ('credential', win32more.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL),
    ]
    return WS_DEFAULT_WINDOWS_INTEGRATED_AUTH_CREDENTIAL
def _define_WS_DISALLOWED_USER_AGENT_SUBSTRINGS_head():
    class WS_DISALLOWED_USER_AGENT_SUBSTRINGS(Structure):
        pass
    return WS_DISALLOWED_USER_AGENT_SUBSTRINGS
def _define_WS_DISALLOWED_USER_AGENT_SUBSTRINGS():
    WS_DISALLOWED_USER_AGENT_SUBSTRINGS = win32more.Networking.WindowsWebServices.WS_DISALLOWED_USER_AGENT_SUBSTRINGS_head
    WS_DISALLOWED_USER_AGENT_SUBSTRINGS._fields_ = [
        ('subStringCount', UInt32),
        ('subStrings', POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_STRING_head))),
    ]
    return WS_DISALLOWED_USER_AGENT_SUBSTRINGS
def _define_WS_DNS_ENDPOINT_IDENTITY_head():
    class WS_DNS_ENDPOINT_IDENTITY(Structure):
        pass
    return WS_DNS_ENDPOINT_IDENTITY
def _define_WS_DNS_ENDPOINT_IDENTITY():
    WS_DNS_ENDPOINT_IDENTITY = win32more.Networking.WindowsWebServices.WS_DNS_ENDPOINT_IDENTITY_head
    WS_DNS_ENDPOINT_IDENTITY._fields_ = [
        ('identity', win32more.Networking.WindowsWebServices.WS_ENDPOINT_IDENTITY),
        ('dns', win32more.Networking.WindowsWebServices.WS_STRING),
    ]
    return WS_DNS_ENDPOINT_IDENTITY
def _define_WS_DOUBLE_DESCRIPTION_head():
    class WS_DOUBLE_DESCRIPTION(Structure):
        pass
    return WS_DOUBLE_DESCRIPTION
def _define_WS_DOUBLE_DESCRIPTION():
    WS_DOUBLE_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_DOUBLE_DESCRIPTION_head
    WS_DOUBLE_DESCRIPTION._fields_ = [
        ('minValue', Double),
        ('maxValue', Double),
    ]
    return WS_DOUBLE_DESCRIPTION
def _define_WS_DURATION_head():
    class WS_DURATION(Structure):
        pass
    return WS_DURATION
def _define_WS_DURATION():
    WS_DURATION = win32more.Networking.WindowsWebServices.WS_DURATION_head
    WS_DURATION._fields_ = [
        ('negative', win32more.Foundation.BOOL),
        ('years', UInt32),
        ('months', UInt32),
        ('days', UInt32),
        ('hours', UInt32),
        ('minutes', UInt32),
        ('seconds', UInt32),
        ('milliseconds', UInt32),
        ('ticks', UInt32),
    ]
    return WS_DURATION
def _define_WS_DURATION_COMPARISON_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_DURATION_head),POINTER(win32more.Networking.WindowsWebServices.WS_DURATION_head),POINTER(Int32),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_DURATION_DESCRIPTION_head():
    class WS_DURATION_DESCRIPTION(Structure):
        pass
    return WS_DURATION_DESCRIPTION
def _define_WS_DURATION_DESCRIPTION():
    WS_DURATION_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_DURATION_DESCRIPTION_head
    WS_DURATION_DESCRIPTION._fields_ = [
        ('minValue', win32more.Networking.WindowsWebServices.WS_DURATION),
        ('maxValue', win32more.Networking.WindowsWebServices.WS_DURATION),
        ('comparer', win32more.Networking.WindowsWebServices.WS_DURATION_COMPARISON_CALLBACK),
    ]
    return WS_DURATION_DESCRIPTION
def _define_WS_DYNAMIC_STRING_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head),POINTER(win32more.Foundation.BOOL),POINTER(UInt32),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_ELEMENT_DESCRIPTION_head():
    class WS_ELEMENT_DESCRIPTION(Structure):
        pass
    return WS_ELEMENT_DESCRIPTION
def _define_WS_ELEMENT_DESCRIPTION():
    WS_ELEMENT_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_ELEMENT_DESCRIPTION_head
    WS_ELEMENT_DESCRIPTION._fields_ = [
        ('elementLocalName', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('elementNs', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('type', win32more.Networking.WindowsWebServices.WS_TYPE),
        ('typeDescription', c_void_p),
    ]
    return WS_ELEMENT_DESCRIPTION
def _define_WS_ENCODER_ENCODE_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_BYTES_head),UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_ENCODER_END_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_ENCODER_GET_CONTENT_TYPE_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_ENCODER_START_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
WS_ENCODING = Int32
WS_ENCODING_XML_BINARY_1 = 0
WS_ENCODING_XML_BINARY_SESSION_1 = 1
WS_ENCODING_XML_MTOM_UTF8 = 2
WS_ENCODING_XML_MTOM_UTF16BE = 3
WS_ENCODING_XML_MTOM_UTF16LE = 4
WS_ENCODING_XML_UTF8 = 5
WS_ENCODING_XML_UTF16BE = 6
WS_ENCODING_XML_UTF16LE = 7
WS_ENCODING_RAW = 8
def _define_WS_ENDPOINT_ADDRESS_head():
    class WS_ENDPOINT_ADDRESS(Structure):
        pass
    return WS_ENDPOINT_ADDRESS
def _define_WS_ENDPOINT_ADDRESS():
    WS_ENDPOINT_ADDRESS = win32more.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS_head
    WS_ENDPOINT_ADDRESS._fields_ = [
        ('url', win32more.Networking.WindowsWebServices.WS_STRING),
        ('headers', POINTER(win32more.Networking.WindowsWebServices.WS_XML_BUFFER_head)),
        ('extensions', POINTER(win32more.Networking.WindowsWebServices.WS_XML_BUFFER_head)),
        ('identity', POINTER(win32more.Networking.WindowsWebServices.WS_ENDPOINT_IDENTITY_head)),
    ]
    return WS_ENDPOINT_ADDRESS
def _define_WS_ENDPOINT_ADDRESS_DESCRIPTION_head():
    class WS_ENDPOINT_ADDRESS_DESCRIPTION(Structure):
        pass
    return WS_ENDPOINT_ADDRESS_DESCRIPTION
def _define_WS_ENDPOINT_ADDRESS_DESCRIPTION():
    WS_ENDPOINT_ADDRESS_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS_DESCRIPTION_head
    WS_ENDPOINT_ADDRESS_DESCRIPTION._fields_ = [
        ('addressingVersion', win32more.Networking.WindowsWebServices.WS_ADDRESSING_VERSION),
    ]
    return WS_ENDPOINT_ADDRESS_DESCRIPTION
WS_ENDPOINT_ADDRESS_EXTENSION_TYPE = Int32
WS_ENDPOINT_ADDRESS_EXTENSION_METADATA_ADDRESS = 1
def _define_WS_ENDPOINT_IDENTITY_head():
    class WS_ENDPOINT_IDENTITY(Structure):
        pass
    return WS_ENDPOINT_IDENTITY
def _define_WS_ENDPOINT_IDENTITY():
    WS_ENDPOINT_IDENTITY = win32more.Networking.WindowsWebServices.WS_ENDPOINT_IDENTITY_head
    WS_ENDPOINT_IDENTITY._fields_ = [
        ('identityType', win32more.Networking.WindowsWebServices.WS_ENDPOINT_IDENTITY_TYPE),
    ]
    return WS_ENDPOINT_IDENTITY
WS_ENDPOINT_IDENTITY_TYPE = Int32
WS_DNS_ENDPOINT_IDENTITY_TYPE = 1
WS_UPN_ENDPOINT_IDENTITY_TYPE = 2
WS_SPN_ENDPOINT_IDENTITY_TYPE = 3
WS_RSA_ENDPOINT_IDENTITY_TYPE = 4
WS_CERT_ENDPOINT_IDENTITY_TYPE = 5
WS_UNKNOWN_ENDPOINT_IDENTITY_TYPE = 6
def _define_WS_ENDPOINT_POLICY_EXTENSION_head():
    class WS_ENDPOINT_POLICY_EXTENSION(Structure):
        pass
    return WS_ENDPOINT_POLICY_EXTENSION
def _define_WS_ENDPOINT_POLICY_EXTENSION():
    WS_ENDPOINT_POLICY_EXTENSION = win32more.Networking.WindowsWebServices.WS_ENDPOINT_POLICY_EXTENSION_head
    class WS_ENDPOINT_POLICY_EXTENSION__out_e__Struct(Structure):
        pass
    WS_ENDPOINT_POLICY_EXTENSION__out_e__Struct._fields_ = [
        ('assertionValue', POINTER(win32more.Networking.WindowsWebServices.WS_XML_BUFFER_head)),
    ]
    WS_ENDPOINT_POLICY_EXTENSION._fields_ = [
        ('policyExtension', win32more.Networking.WindowsWebServices.WS_POLICY_EXTENSION),
        ('assertionName', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('assertionNs', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('out', WS_ENDPOINT_POLICY_EXTENSION__out_e__Struct),
    ]
    return WS_ENDPOINT_POLICY_EXTENSION
def _define_WS_ENUM_DESCRIPTION_head():
    class WS_ENUM_DESCRIPTION(Structure):
        pass
    return WS_ENUM_DESCRIPTION
def _define_WS_ENUM_DESCRIPTION():
    WS_ENUM_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_ENUM_DESCRIPTION_head
    WS_ENUM_DESCRIPTION._fields_ = [
        ('values', POINTER(win32more.Networking.WindowsWebServices.WS_ENUM_VALUE_head)),
        ('valueCount', UInt32),
        ('maxByteCount', UInt32),
        ('nameIndices', POINTER(UInt32)),
    ]
    return WS_ENUM_DESCRIPTION
def _define_WS_ENUM_VALUE_head():
    class WS_ENUM_VALUE(Structure):
        pass
    return WS_ENUM_VALUE
def _define_WS_ENUM_VALUE():
    WS_ENUM_VALUE = win32more.Networking.WindowsWebServices.WS_ENUM_VALUE_head
    WS_ENUM_VALUE._fields_ = [
        ('value', Int32),
        ('name', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
    ]
    return WS_ENUM_VALUE
WS_ENVELOPE_VERSION = Int32
WS_ENVELOPE_VERSION_SOAP_1_1 = 1
WS_ENVELOPE_VERSION_SOAP_1_2 = 2
WS_ENVELOPE_VERSION_NONE = 3
def _define_WS_ERROR_head():
    class WS_ERROR(Structure):
        pass
    return WS_ERROR
def _define_WS_ERROR():
    WS_ERROR = win32more.Networking.WindowsWebServices.WS_ERROR_head
    return WS_ERROR
def _define_WS_ERROR_PROPERTY_head():
    class WS_ERROR_PROPERTY(Structure):
        pass
    return WS_ERROR_PROPERTY
def _define_WS_ERROR_PROPERTY():
    WS_ERROR_PROPERTY = win32more.Networking.WindowsWebServices.WS_ERROR_PROPERTY_head
    WS_ERROR_PROPERTY._fields_ = [
        ('id', win32more.Networking.WindowsWebServices.WS_ERROR_PROPERTY_ID),
        ('value', c_void_p),
        ('valueSize', UInt32),
    ]
    return WS_ERROR_PROPERTY
WS_ERROR_PROPERTY_ID = Int32
WS_ERROR_PROPERTY_STRING_COUNT = 0
WS_ERROR_PROPERTY_ORIGINAL_ERROR_CODE = 1
WS_ERROR_PROPERTY_LANGID = 2
WS_EXCEPTION_CODE = Int32
WS_EXCEPTION_CODE_USAGE_FAILURE = -1069744128
WS_EXCEPTION_CODE_INTERNAL_FAILURE = -1069744127
WS_EXTENDED_PROTECTION_POLICY = Int32
WS_EXTENDED_PROTECTION_POLICY_NEVER = 1
WS_EXTENDED_PROTECTION_POLICY_WHEN_SUPPORTED = 2
WS_EXTENDED_PROTECTION_POLICY_ALWAYS = 3
WS_EXTENDED_PROTECTION_SCENARIO = Int32
WS_EXTENDED_PROTECTION_SCENARIO_BOUND_SERVER = 1
WS_EXTENDED_PROTECTION_SCENARIO_TERMINATED_SSL = 2
def _define_WS_FAULT_head():
    class WS_FAULT(Structure):
        pass
    return WS_FAULT
def _define_WS_FAULT():
    WS_FAULT = win32more.Networking.WindowsWebServices.WS_FAULT_head
    WS_FAULT._fields_ = [
        ('code', POINTER(win32more.Networking.WindowsWebServices.WS_FAULT_CODE_head)),
        ('reasons', POINTER(win32more.Networking.WindowsWebServices.WS_FAULT_REASON_head)),
        ('reasonCount', UInt32),
        ('actor', win32more.Networking.WindowsWebServices.WS_STRING),
        ('node', win32more.Networking.WindowsWebServices.WS_STRING),
        ('detail', POINTER(win32more.Networking.WindowsWebServices.WS_XML_BUFFER_head)),
    ]
    return WS_FAULT
def _define_WS_FAULT_CODE_head():
    class WS_FAULT_CODE(Structure):
        pass
    return WS_FAULT_CODE
def _define_WS_FAULT_CODE():
    WS_FAULT_CODE = win32more.Networking.WindowsWebServices.WS_FAULT_CODE_head
    WS_FAULT_CODE._fields_ = [
        ('value', win32more.Networking.WindowsWebServices.WS_XML_QNAME),
        ('subCode', POINTER(win32more.Networking.WindowsWebServices.WS_FAULT_CODE_head)),
    ]
    return WS_FAULT_CODE
def _define_WS_FAULT_DESCRIPTION_head():
    class WS_FAULT_DESCRIPTION(Structure):
        pass
    return WS_FAULT_DESCRIPTION
def _define_WS_FAULT_DESCRIPTION():
    WS_FAULT_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_FAULT_DESCRIPTION_head
    WS_FAULT_DESCRIPTION._fields_ = [
        ('envelopeVersion', win32more.Networking.WindowsWebServices.WS_ENVELOPE_VERSION),
    ]
    return WS_FAULT_DESCRIPTION
def _define_WS_FAULT_DETAIL_DESCRIPTION_head():
    class WS_FAULT_DETAIL_DESCRIPTION(Structure):
        pass
    return WS_FAULT_DETAIL_DESCRIPTION
def _define_WS_FAULT_DETAIL_DESCRIPTION():
    WS_FAULT_DETAIL_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_FAULT_DETAIL_DESCRIPTION_head
    WS_FAULT_DETAIL_DESCRIPTION._fields_ = [
        ('action', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('detailElementDescription', POINTER(win32more.Networking.WindowsWebServices.WS_ELEMENT_DESCRIPTION_head)),
    ]
    return WS_FAULT_DETAIL_DESCRIPTION
WS_FAULT_DISCLOSURE = Int32
WS_MINIMAL_FAULT_DISCLOSURE = 0
WS_FULL_FAULT_DISCLOSURE = 1
WS_FAULT_ERROR_PROPERTY_ID = Int32
WS_FAULT_ERROR_PROPERTY_FAULT = 0
WS_FAULT_ERROR_PROPERTY_ACTION = 1
WS_FAULT_ERROR_PROPERTY_HEADER = 2
def _define_WS_FAULT_REASON_head():
    class WS_FAULT_REASON(Structure):
        pass
    return WS_FAULT_REASON
def _define_WS_FAULT_REASON():
    WS_FAULT_REASON = win32more.Networking.WindowsWebServices.WS_FAULT_REASON_head
    WS_FAULT_REASON._fields_ = [
        ('text', win32more.Networking.WindowsWebServices.WS_STRING),
        ('lang', win32more.Networking.WindowsWebServices.WS_STRING),
    ]
    return WS_FAULT_REASON
def _define_WS_FIELD_DESCRIPTION_head():
    class WS_FIELD_DESCRIPTION(Structure):
        pass
    return WS_FIELD_DESCRIPTION
def _define_WS_FIELD_DESCRIPTION():
    WS_FIELD_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_FIELD_DESCRIPTION_head
    WS_FIELD_DESCRIPTION._fields_ = [
        ('mapping', win32more.Networking.WindowsWebServices.WS_FIELD_MAPPING),
        ('localName', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('ns', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('type', win32more.Networking.WindowsWebServices.WS_TYPE),
        ('typeDescription', c_void_p),
        ('offset', UInt32),
        ('options', UInt32),
        ('defaultValue', POINTER(win32more.Networking.WindowsWebServices.WS_DEFAULT_VALUE_head)),
        ('countOffset', UInt32),
        ('itemLocalName', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('itemNs', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('itemRange', POINTER(win32more.Networking.WindowsWebServices.WS_ITEM_RANGE_head)),
    ]
    return WS_FIELD_DESCRIPTION
WS_FIELD_MAPPING = Int32
WS_TYPE_ATTRIBUTE_FIELD_MAPPING = 0
WS_ATTRIBUTE_FIELD_MAPPING = 1
WS_ELEMENT_FIELD_MAPPING = 2
WS_REPEATING_ELEMENT_FIELD_MAPPING = 3
WS_TEXT_FIELD_MAPPING = 4
WS_NO_FIELD_MAPPING = 5
WS_XML_ATTRIBUTE_FIELD_MAPPING = 6
WS_ELEMENT_CHOICE_FIELD_MAPPING = 7
WS_REPEATING_ELEMENT_CHOICE_FIELD_MAPPING = 8
WS_ANY_ELEMENT_FIELD_MAPPING = 9
WS_REPEATING_ANY_ELEMENT_FIELD_MAPPING = 10
WS_ANY_CONTENT_FIELD_MAPPING = 11
WS_ANY_ATTRIBUTES_FIELD_MAPPING = 12
def _define_WS_FLOAT_DESCRIPTION_head():
    class WS_FLOAT_DESCRIPTION(Structure):
        pass
    return WS_FLOAT_DESCRIPTION
def _define_WS_FLOAT_DESCRIPTION():
    WS_FLOAT_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_FLOAT_DESCRIPTION_head
    WS_FLOAT_DESCRIPTION._fields_ = [
        ('minValue', Single),
        ('maxValue', Single),
    ]
    return WS_FLOAT_DESCRIPTION
def _define_WS_FREE_CHANNEL_CALLBACK():
    return WINFUNCTYPE(Void,c_void_p)
def _define_WS_FREE_DECODER_CALLBACK():
    return WINFUNCTYPE(Void,c_void_p)
def _define_WS_FREE_ENCODER_CALLBACK():
    return WINFUNCTYPE(Void,c_void_p)
def _define_WS_FREE_LISTENER_CALLBACK():
    return WINFUNCTYPE(Void,c_void_p)
def _define_WS_GET_CERT_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS_head),POINTER(win32more.Networking.WindowsWebServices.WS_STRING_head),POINTER(POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head)),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_GET_CHANNEL_PROPERTY_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_GET_LISTENER_PROPERTY_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_GUID_DESCRIPTION_head():
    class WS_GUID_DESCRIPTION(Structure):
        pass
    return WS_GUID_DESCRIPTION
def _define_WS_GUID_DESCRIPTION():
    WS_GUID_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_GUID_DESCRIPTION_head
    WS_GUID_DESCRIPTION._fields_ = [
        ('value', Guid),
    ]
    return WS_GUID_DESCRIPTION
WS_HEADER_TYPE = Int32
WS_ACTION_HEADER = 1
WS_TO_HEADER = 2
WS_MESSAGE_ID_HEADER = 3
WS_RELATES_TO_HEADER = 4
WS_FROM_HEADER = 5
WS_REPLY_TO_HEADER = 6
WS_FAULT_TO_HEADER = 7
def _define_WS_HEAP_head():
    class WS_HEAP(Structure):
        pass
    return WS_HEAP
def _define_WS_HEAP():
    WS_HEAP = win32more.Networking.WindowsWebServices.WS_HEAP_head
    return WS_HEAP
def _define_WS_HEAP_PROPERTIES_head():
    class WS_HEAP_PROPERTIES(Structure):
        pass
    return WS_HEAP_PROPERTIES
def _define_WS_HEAP_PROPERTIES():
    WS_HEAP_PROPERTIES = win32more.Networking.WindowsWebServices.WS_HEAP_PROPERTIES_head
    WS_HEAP_PROPERTIES._fields_ = [
        ('properties', POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_PROPERTY_head)),
        ('propertyCount', UInt32),
    ]
    return WS_HEAP_PROPERTIES
def _define_WS_HEAP_PROPERTY_head():
    class WS_HEAP_PROPERTY(Structure):
        pass
    return WS_HEAP_PROPERTY
def _define_WS_HEAP_PROPERTY():
    WS_HEAP_PROPERTY = win32more.Networking.WindowsWebServices.WS_HEAP_PROPERTY_head
    WS_HEAP_PROPERTY._fields_ = [
        ('id', win32more.Networking.WindowsWebServices.WS_HEAP_PROPERTY_ID),
        ('value', c_void_p),
        ('valueSize', UInt32),
    ]
    return WS_HEAP_PROPERTY
WS_HEAP_PROPERTY_ID = Int32
WS_HEAP_PROPERTY_MAX_SIZE = 0
WS_HEAP_PROPERTY_TRIM_SIZE = 1
WS_HEAP_PROPERTY_REQUESTED_SIZE = 2
WS_HEAP_PROPERTY_ACTUAL_SIZE = 3
def _define_WS_HOST_NAMES_head():
    class WS_HOST_NAMES(Structure):
        pass
    return WS_HOST_NAMES
def _define_WS_HOST_NAMES():
    WS_HOST_NAMES = win32more.Networking.WindowsWebServices.WS_HOST_NAMES_head
    WS_HOST_NAMES._fields_ = [
        ('hostNames', POINTER(win32more.Networking.WindowsWebServices.WS_STRING_head)),
        ('hostNameCount', UInt32),
    ]
    return WS_HOST_NAMES
def _define_WS_HTTP_BINDING_TEMPLATE_head():
    class WS_HTTP_BINDING_TEMPLATE(Structure):
        pass
    return WS_HTTP_BINDING_TEMPLATE
def _define_WS_HTTP_BINDING_TEMPLATE():
    WS_HTTP_BINDING_TEMPLATE = win32more.Networking.WindowsWebServices.WS_HTTP_BINDING_TEMPLATE_head
    WS_HTTP_BINDING_TEMPLATE._fields_ = [
        ('channelProperties', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES),
    ]
    return WS_HTTP_BINDING_TEMPLATE
def _define_WS_HTTP_HEADER_AUTH_BINDING_TEMPLATE_head():
    class WS_HTTP_HEADER_AUTH_BINDING_TEMPLATE(Structure):
        pass
    return WS_HTTP_HEADER_AUTH_BINDING_TEMPLATE
def _define_WS_HTTP_HEADER_AUTH_BINDING_TEMPLATE():
    WS_HTTP_HEADER_AUTH_BINDING_TEMPLATE = win32more.Networking.WindowsWebServices.WS_HTTP_HEADER_AUTH_BINDING_TEMPLATE_head
    WS_HTTP_HEADER_AUTH_BINDING_TEMPLATE._fields_ = [
        ('channelProperties', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES),
        ('securityProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES),
        ('httpHeaderAuthSecurityBinding', win32more.Networking.WindowsWebServices.WS_HTTP_HEADER_AUTH_SECURITY_BINDING_TEMPLATE),
    ]
    return WS_HTTP_HEADER_AUTH_BINDING_TEMPLATE
def _define_WS_HTTP_HEADER_AUTH_POLICY_DESCRIPTION_head():
    class WS_HTTP_HEADER_AUTH_POLICY_DESCRIPTION(Structure):
        pass
    return WS_HTTP_HEADER_AUTH_POLICY_DESCRIPTION
def _define_WS_HTTP_HEADER_AUTH_POLICY_DESCRIPTION():
    WS_HTTP_HEADER_AUTH_POLICY_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_HTTP_HEADER_AUTH_POLICY_DESCRIPTION_head
    WS_HTTP_HEADER_AUTH_POLICY_DESCRIPTION._fields_ = [
        ('channelProperties', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES),
        ('securityProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES),
        ('httpHeaderAuthSecurityBinding', win32more.Networking.WindowsWebServices.WS_HTTP_HEADER_AUTH_SECURITY_BINDING_POLICY_DESCRIPTION),
    ]
    return WS_HTTP_HEADER_AUTH_POLICY_DESCRIPTION
def _define_WS_HTTP_HEADER_AUTH_SECURITY_BINDING_head():
    class WS_HTTP_HEADER_AUTH_SECURITY_BINDING(Structure):
        pass
    return WS_HTTP_HEADER_AUTH_SECURITY_BINDING
def _define_WS_HTTP_HEADER_AUTH_SECURITY_BINDING():
    WS_HTTP_HEADER_AUTH_SECURITY_BINDING = win32more.Networking.WindowsWebServices.WS_HTTP_HEADER_AUTH_SECURITY_BINDING_head
    WS_HTTP_HEADER_AUTH_SECURITY_BINDING._fields_ = [
        ('binding', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING),
        ('clientCredential', POINTER(win32more.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_head)),
    ]
    return WS_HTTP_HEADER_AUTH_SECURITY_BINDING
def _define_WS_HTTP_HEADER_AUTH_SECURITY_BINDING_CONSTRAINT_head():
    class WS_HTTP_HEADER_AUTH_SECURITY_BINDING_CONSTRAINT(Structure):
        pass
    return WS_HTTP_HEADER_AUTH_SECURITY_BINDING_CONSTRAINT
def _define_WS_HTTP_HEADER_AUTH_SECURITY_BINDING_CONSTRAINT():
    WS_HTTP_HEADER_AUTH_SECURITY_BINDING_CONSTRAINT = win32more.Networking.WindowsWebServices.WS_HTTP_HEADER_AUTH_SECURITY_BINDING_CONSTRAINT_head
    WS_HTTP_HEADER_AUTH_SECURITY_BINDING_CONSTRAINT._fields_ = [
        ('bindingConstraint', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT),
    ]
    return WS_HTTP_HEADER_AUTH_SECURITY_BINDING_CONSTRAINT
def _define_WS_HTTP_HEADER_AUTH_SECURITY_BINDING_POLICY_DESCRIPTION_head():
    class WS_HTTP_HEADER_AUTH_SECURITY_BINDING_POLICY_DESCRIPTION(Structure):
        pass
    return WS_HTTP_HEADER_AUTH_SECURITY_BINDING_POLICY_DESCRIPTION
def _define_WS_HTTP_HEADER_AUTH_SECURITY_BINDING_POLICY_DESCRIPTION():
    WS_HTTP_HEADER_AUTH_SECURITY_BINDING_POLICY_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_HTTP_HEADER_AUTH_SECURITY_BINDING_POLICY_DESCRIPTION_head
    WS_HTTP_HEADER_AUTH_SECURITY_BINDING_POLICY_DESCRIPTION._fields_ = [
        ('securityBindingProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES),
    ]
    return WS_HTTP_HEADER_AUTH_SECURITY_BINDING_POLICY_DESCRIPTION
def _define_WS_HTTP_HEADER_AUTH_SECURITY_BINDING_TEMPLATE_head():
    class WS_HTTP_HEADER_AUTH_SECURITY_BINDING_TEMPLATE(Structure):
        pass
    return WS_HTTP_HEADER_AUTH_SECURITY_BINDING_TEMPLATE
def _define_WS_HTTP_HEADER_AUTH_SECURITY_BINDING_TEMPLATE():
    WS_HTTP_HEADER_AUTH_SECURITY_BINDING_TEMPLATE = win32more.Networking.WindowsWebServices.WS_HTTP_HEADER_AUTH_SECURITY_BINDING_TEMPLATE_head
    WS_HTTP_HEADER_AUTH_SECURITY_BINDING_TEMPLATE._fields_ = [
        ('securityBindingProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES),
        ('clientCredential', POINTER(win32more.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_head)),
    ]
    return WS_HTTP_HEADER_AUTH_SECURITY_BINDING_TEMPLATE
WS_HTTP_HEADER_AUTH_TARGET = Int32
WS_HTTP_HEADER_AUTH_TARGET_SERVICE = 1
WS_HTTP_HEADER_AUTH_TARGET_PROXY = 2
def _define_WS_HTTP_HEADER_MAPPING_head():
    class WS_HTTP_HEADER_MAPPING(Structure):
        pass
    return WS_HTTP_HEADER_MAPPING
def _define_WS_HTTP_HEADER_MAPPING():
    WS_HTTP_HEADER_MAPPING = win32more.Networking.WindowsWebServices.WS_HTTP_HEADER_MAPPING_head
    WS_HTTP_HEADER_MAPPING._fields_ = [
        ('headerName', win32more.Networking.WindowsWebServices.WS_XML_STRING),
        ('headerMappingOptions', UInt32),
    ]
    return WS_HTTP_HEADER_MAPPING
def _define_WS_HTTP_MESSAGE_MAPPING_head():
    class WS_HTTP_MESSAGE_MAPPING(Structure):
        pass
    return WS_HTTP_MESSAGE_MAPPING
def _define_WS_HTTP_MESSAGE_MAPPING():
    WS_HTTP_MESSAGE_MAPPING = win32more.Networking.WindowsWebServices.WS_HTTP_MESSAGE_MAPPING_head
    WS_HTTP_MESSAGE_MAPPING._fields_ = [
        ('requestMappingOptions', UInt32),
        ('responseMappingOptions', UInt32),
        ('requestHeaderMappings', POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_HTTP_HEADER_MAPPING_head))),
        ('requestHeaderMappingCount', UInt32),
        ('responseHeaderMappings', POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_HTTP_HEADER_MAPPING_head))),
        ('responseHeaderMappingCount', UInt32),
    ]
    return WS_HTTP_MESSAGE_MAPPING
def _define_WS_HTTP_POLICY_DESCRIPTION_head():
    class WS_HTTP_POLICY_DESCRIPTION(Structure):
        pass
    return WS_HTTP_POLICY_DESCRIPTION
def _define_WS_HTTP_POLICY_DESCRIPTION():
    WS_HTTP_POLICY_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_HTTP_POLICY_DESCRIPTION_head
    WS_HTTP_POLICY_DESCRIPTION._fields_ = [
        ('channelProperties', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES),
    ]
    return WS_HTTP_POLICY_DESCRIPTION
WS_HTTP_PROXY_SETTING_MODE = Int32
WS_HTTP_PROXY_SETTING_MODE_AUTO = 1
WS_HTTP_PROXY_SETTING_MODE_NONE = 2
WS_HTTP_PROXY_SETTING_MODE_CUSTOM = 3
def _define_WS_HTTP_REDIRECT_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_STRING_head))
def _define_WS_HTTP_REDIRECT_CALLBACK_CONTEXT_head():
    class WS_HTTP_REDIRECT_CALLBACK_CONTEXT(Structure):
        pass
    return WS_HTTP_REDIRECT_CALLBACK_CONTEXT
def _define_WS_HTTP_REDIRECT_CALLBACK_CONTEXT():
    WS_HTTP_REDIRECT_CALLBACK_CONTEXT = win32more.Networking.WindowsWebServices.WS_HTTP_REDIRECT_CALLBACK_CONTEXT_head
    WS_HTTP_REDIRECT_CALLBACK_CONTEXT._fields_ = [
        ('callback', win32more.Networking.WindowsWebServices.WS_HTTP_REDIRECT_CALLBACK),
        ('state', c_void_p),
    ]
    return WS_HTTP_REDIRECT_CALLBACK_CONTEXT
def _define_WS_HTTP_SSL_BINDING_TEMPLATE_head():
    class WS_HTTP_SSL_BINDING_TEMPLATE(Structure):
        pass
    return WS_HTTP_SSL_BINDING_TEMPLATE
def _define_WS_HTTP_SSL_BINDING_TEMPLATE():
    WS_HTTP_SSL_BINDING_TEMPLATE = win32more.Networking.WindowsWebServices.WS_HTTP_SSL_BINDING_TEMPLATE_head
    WS_HTTP_SSL_BINDING_TEMPLATE._fields_ = [
        ('channelProperties', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES),
        ('securityProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES),
        ('sslTransportSecurityBinding', win32more.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_TEMPLATE),
    ]
    return WS_HTTP_SSL_BINDING_TEMPLATE
def _define_WS_HTTP_SSL_HEADER_AUTH_BINDING_TEMPLATE_head():
    class WS_HTTP_SSL_HEADER_AUTH_BINDING_TEMPLATE(Structure):
        pass
    return WS_HTTP_SSL_HEADER_AUTH_BINDING_TEMPLATE
def _define_WS_HTTP_SSL_HEADER_AUTH_BINDING_TEMPLATE():
    WS_HTTP_SSL_HEADER_AUTH_BINDING_TEMPLATE = win32more.Networking.WindowsWebServices.WS_HTTP_SSL_HEADER_AUTH_BINDING_TEMPLATE_head
    WS_HTTP_SSL_HEADER_AUTH_BINDING_TEMPLATE._fields_ = [
        ('channelProperties', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES),
        ('securityProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES),
        ('sslTransportSecurityBinding', win32more.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_TEMPLATE),
        ('httpHeaderAuthSecurityBinding', win32more.Networking.WindowsWebServices.WS_HTTP_HEADER_AUTH_SECURITY_BINDING_TEMPLATE),
    ]
    return WS_HTTP_SSL_HEADER_AUTH_BINDING_TEMPLATE
def _define_WS_HTTP_SSL_HEADER_AUTH_POLICY_DESCRIPTION_head():
    class WS_HTTP_SSL_HEADER_AUTH_POLICY_DESCRIPTION(Structure):
        pass
    return WS_HTTP_SSL_HEADER_AUTH_POLICY_DESCRIPTION
def _define_WS_HTTP_SSL_HEADER_AUTH_POLICY_DESCRIPTION():
    WS_HTTP_SSL_HEADER_AUTH_POLICY_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_HTTP_SSL_HEADER_AUTH_POLICY_DESCRIPTION_head
    WS_HTTP_SSL_HEADER_AUTH_POLICY_DESCRIPTION._fields_ = [
        ('channelProperties', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES),
        ('securityProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES),
        ('sslTransportSecurityBinding', win32more.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION),
        ('httpHeaderAuthSecurityBinding', win32more.Networking.WindowsWebServices.WS_HTTP_HEADER_AUTH_SECURITY_BINDING_POLICY_DESCRIPTION),
    ]
    return WS_HTTP_SSL_HEADER_AUTH_POLICY_DESCRIPTION
def _define_WS_HTTP_SSL_KERBEROS_APREQ_BINDING_TEMPLATE_head():
    class WS_HTTP_SSL_KERBEROS_APREQ_BINDING_TEMPLATE(Structure):
        pass
    return WS_HTTP_SSL_KERBEROS_APREQ_BINDING_TEMPLATE
def _define_WS_HTTP_SSL_KERBEROS_APREQ_BINDING_TEMPLATE():
    WS_HTTP_SSL_KERBEROS_APREQ_BINDING_TEMPLATE = win32more.Networking.WindowsWebServices.WS_HTTP_SSL_KERBEROS_APREQ_BINDING_TEMPLATE_head
    WS_HTTP_SSL_KERBEROS_APREQ_BINDING_TEMPLATE._fields_ = [
        ('channelProperties', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES),
        ('securityProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES),
        ('sslTransportSecurityBinding', win32more.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_TEMPLATE),
        ('kerberosApreqMessageSecurityBinding', win32more.Networking.WindowsWebServices.WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_TEMPLATE),
    ]
    return WS_HTTP_SSL_KERBEROS_APREQ_BINDING_TEMPLATE
def _define_WS_HTTP_SSL_KERBEROS_APREQ_POLICY_DESCRIPTION_head():
    class WS_HTTP_SSL_KERBEROS_APREQ_POLICY_DESCRIPTION(Structure):
        pass
    return WS_HTTP_SSL_KERBEROS_APREQ_POLICY_DESCRIPTION
def _define_WS_HTTP_SSL_KERBEROS_APREQ_POLICY_DESCRIPTION():
    WS_HTTP_SSL_KERBEROS_APREQ_POLICY_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_HTTP_SSL_KERBEROS_APREQ_POLICY_DESCRIPTION_head
    WS_HTTP_SSL_KERBEROS_APREQ_POLICY_DESCRIPTION._fields_ = [
        ('channelProperties', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES),
        ('securityProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES),
        ('sslTransportSecurityBinding', win32more.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION),
        ('kerberosApreqMessageSecurityBinding', win32more.Networking.WindowsWebServices.WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION),
    ]
    return WS_HTTP_SSL_KERBEROS_APREQ_POLICY_DESCRIPTION
def _define_WS_HTTP_SSL_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE_head():
    class WS_HTTP_SSL_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE(Structure):
        pass
    return WS_HTTP_SSL_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE
def _define_WS_HTTP_SSL_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE():
    WS_HTTP_SSL_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE = win32more.Networking.WindowsWebServices.WS_HTTP_SSL_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE_head
    WS_HTTP_SSL_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE._fields_ = [
        ('channelProperties', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES),
        ('securityProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES),
        ('sslTransportSecurityBinding', win32more.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_TEMPLATE),
        ('kerberosApreqMessageSecurityBinding', win32more.Networking.WindowsWebServices.WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_TEMPLATE),
        ('securityContextSecurityBinding', win32more.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_SECURITY_BINDING_TEMPLATE),
    ]
    return WS_HTTP_SSL_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE
def _define_WS_HTTP_SSL_KERBEROS_APREQ_SECURITY_CONTEXT_POLICY_DESCRIPTION_head():
    class WS_HTTP_SSL_KERBEROS_APREQ_SECURITY_CONTEXT_POLICY_DESCRIPTION(Structure):
        pass
    return WS_HTTP_SSL_KERBEROS_APREQ_SECURITY_CONTEXT_POLICY_DESCRIPTION
def _define_WS_HTTP_SSL_KERBEROS_APREQ_SECURITY_CONTEXT_POLICY_DESCRIPTION():
    WS_HTTP_SSL_KERBEROS_APREQ_SECURITY_CONTEXT_POLICY_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_HTTP_SSL_KERBEROS_APREQ_SECURITY_CONTEXT_POLICY_DESCRIPTION_head
    WS_HTTP_SSL_KERBEROS_APREQ_SECURITY_CONTEXT_POLICY_DESCRIPTION._fields_ = [
        ('channelProperties', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES),
        ('securityProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES),
        ('sslTransportSecurityBinding', win32more.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION),
        ('kerberosApreqMessageSecurityBinding', win32more.Networking.WindowsWebServices.WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION),
        ('securityContextSecurityBinding', win32more.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_SECURITY_BINDING_POLICY_DESCRIPTION),
    ]
    return WS_HTTP_SSL_KERBEROS_APREQ_SECURITY_CONTEXT_POLICY_DESCRIPTION
def _define_WS_HTTP_SSL_POLICY_DESCRIPTION_head():
    class WS_HTTP_SSL_POLICY_DESCRIPTION(Structure):
        pass
    return WS_HTTP_SSL_POLICY_DESCRIPTION
def _define_WS_HTTP_SSL_POLICY_DESCRIPTION():
    WS_HTTP_SSL_POLICY_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_HTTP_SSL_POLICY_DESCRIPTION_head
    WS_HTTP_SSL_POLICY_DESCRIPTION._fields_ = [
        ('channelProperties', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES),
        ('securityProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES),
        ('sslTransportSecurityBinding', win32more.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION),
    ]
    return WS_HTTP_SSL_POLICY_DESCRIPTION
def _define_WS_HTTP_SSL_USERNAME_BINDING_TEMPLATE_head():
    class WS_HTTP_SSL_USERNAME_BINDING_TEMPLATE(Structure):
        pass
    return WS_HTTP_SSL_USERNAME_BINDING_TEMPLATE
def _define_WS_HTTP_SSL_USERNAME_BINDING_TEMPLATE():
    WS_HTTP_SSL_USERNAME_BINDING_TEMPLATE = win32more.Networking.WindowsWebServices.WS_HTTP_SSL_USERNAME_BINDING_TEMPLATE_head
    WS_HTTP_SSL_USERNAME_BINDING_TEMPLATE._fields_ = [
        ('channelProperties', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES),
        ('securityProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES),
        ('sslTransportSecurityBinding', win32more.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_TEMPLATE),
        ('usernameMessageSecurityBinding', win32more.Networking.WindowsWebServices.WS_USERNAME_MESSAGE_SECURITY_BINDING_TEMPLATE),
    ]
    return WS_HTTP_SSL_USERNAME_BINDING_TEMPLATE
def _define_WS_HTTP_SSL_USERNAME_POLICY_DESCRIPTION_head():
    class WS_HTTP_SSL_USERNAME_POLICY_DESCRIPTION(Structure):
        pass
    return WS_HTTP_SSL_USERNAME_POLICY_DESCRIPTION
def _define_WS_HTTP_SSL_USERNAME_POLICY_DESCRIPTION():
    WS_HTTP_SSL_USERNAME_POLICY_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_HTTP_SSL_USERNAME_POLICY_DESCRIPTION_head
    WS_HTTP_SSL_USERNAME_POLICY_DESCRIPTION._fields_ = [
        ('channelProperties', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES),
        ('securityProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES),
        ('sslTransportSecurityBinding', win32more.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION),
        ('usernameMessageSecurityBinding', win32more.Networking.WindowsWebServices.WS_USERNAME_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION),
    ]
    return WS_HTTP_SSL_USERNAME_POLICY_DESCRIPTION
def _define_WS_HTTP_SSL_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE_head():
    class WS_HTTP_SSL_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE(Structure):
        pass
    return WS_HTTP_SSL_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE
def _define_WS_HTTP_SSL_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE():
    WS_HTTP_SSL_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE = win32more.Networking.WindowsWebServices.WS_HTTP_SSL_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE_head
    WS_HTTP_SSL_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE._fields_ = [
        ('channelProperties', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES),
        ('securityProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES),
        ('sslTransportSecurityBinding', win32more.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_TEMPLATE),
        ('usernameMessageSecurityBinding', win32more.Networking.WindowsWebServices.WS_USERNAME_MESSAGE_SECURITY_BINDING_TEMPLATE),
        ('securityContextSecurityBinding', win32more.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_SECURITY_BINDING_TEMPLATE),
    ]
    return WS_HTTP_SSL_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE
def _define_WS_HTTP_SSL_USERNAME_SECURITY_CONTEXT_POLICY_DESCRIPTION_head():
    class WS_HTTP_SSL_USERNAME_SECURITY_CONTEXT_POLICY_DESCRIPTION(Structure):
        pass
    return WS_HTTP_SSL_USERNAME_SECURITY_CONTEXT_POLICY_DESCRIPTION
def _define_WS_HTTP_SSL_USERNAME_SECURITY_CONTEXT_POLICY_DESCRIPTION():
    WS_HTTP_SSL_USERNAME_SECURITY_CONTEXT_POLICY_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_HTTP_SSL_USERNAME_SECURITY_CONTEXT_POLICY_DESCRIPTION_head
    WS_HTTP_SSL_USERNAME_SECURITY_CONTEXT_POLICY_DESCRIPTION._fields_ = [
        ('channelProperties', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES),
        ('securityProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES),
        ('sslTransportSecurityBinding', win32more.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION),
        ('usernameMessageSecurityBinding', win32more.Networking.WindowsWebServices.WS_USERNAME_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION),
        ('securityContextSecurityBinding', win32more.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_SECURITY_BINDING_POLICY_DESCRIPTION),
    ]
    return WS_HTTP_SSL_USERNAME_SECURITY_CONTEXT_POLICY_DESCRIPTION
def _define_WS_HTTP_URL_head():
    class WS_HTTP_URL(Structure):
        pass
    return WS_HTTP_URL
def _define_WS_HTTP_URL():
    WS_HTTP_URL = win32more.Networking.WindowsWebServices.WS_HTTP_URL_head
    WS_HTTP_URL._fields_ = [
        ('url', win32more.Networking.WindowsWebServices.WS_URL),
        ('host', win32more.Networking.WindowsWebServices.WS_STRING),
        ('port', UInt16),
        ('portAsString', win32more.Networking.WindowsWebServices.WS_STRING),
        ('path', win32more.Networking.WindowsWebServices.WS_STRING),
        ('query', win32more.Networking.WindowsWebServices.WS_STRING),
        ('fragment', win32more.Networking.WindowsWebServices.WS_STRING),
    ]
    return WS_HTTP_URL
def _define_WS_HTTPS_URL_head():
    class WS_HTTPS_URL(Structure):
        pass
    return WS_HTTPS_URL
def _define_WS_HTTPS_URL():
    WS_HTTPS_URL = win32more.Networking.WindowsWebServices.WS_HTTPS_URL_head
    WS_HTTPS_URL._fields_ = [
        ('url', win32more.Networking.WindowsWebServices.WS_URL),
        ('host', win32more.Networking.WindowsWebServices.WS_STRING),
        ('port', UInt16),
        ('portAsString', win32more.Networking.WindowsWebServices.WS_STRING),
        ('path', win32more.Networking.WindowsWebServices.WS_STRING),
        ('query', win32more.Networking.WindowsWebServices.WS_STRING),
        ('fragment', win32more.Networking.WindowsWebServices.WS_STRING),
    ]
    return WS_HTTPS_URL
def _define_WS_INT16_DESCRIPTION_head():
    class WS_INT16_DESCRIPTION(Structure):
        pass
    return WS_INT16_DESCRIPTION
def _define_WS_INT16_DESCRIPTION():
    WS_INT16_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_INT16_DESCRIPTION_head
    WS_INT16_DESCRIPTION._fields_ = [
        ('minValue', Int16),
        ('maxValue', Int16),
    ]
    return WS_INT16_DESCRIPTION
def _define_WS_INT32_DESCRIPTION_head():
    class WS_INT32_DESCRIPTION(Structure):
        pass
    return WS_INT32_DESCRIPTION
def _define_WS_INT32_DESCRIPTION():
    WS_INT32_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_INT32_DESCRIPTION_head
    WS_INT32_DESCRIPTION._fields_ = [
        ('minValue', Int32),
        ('maxValue', Int32),
    ]
    return WS_INT32_DESCRIPTION
def _define_WS_INT64_DESCRIPTION_head():
    class WS_INT64_DESCRIPTION(Structure):
        pass
    return WS_INT64_DESCRIPTION
def _define_WS_INT64_DESCRIPTION():
    WS_INT64_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_INT64_DESCRIPTION_head
    WS_INT64_DESCRIPTION._fields_ = [
        ('minValue', Int64),
        ('maxValue', Int64),
    ]
    return WS_INT64_DESCRIPTION
def _define_WS_INT8_DESCRIPTION_head():
    class WS_INT8_DESCRIPTION(Structure):
        pass
    return WS_INT8_DESCRIPTION
def _define_WS_INT8_DESCRIPTION():
    WS_INT8_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_INT8_DESCRIPTION_head
    WS_INT8_DESCRIPTION._fields_ = [
        ('minValue', win32more.Foundation.CHAR),
        ('maxValue', win32more.Foundation.CHAR),
    ]
    return WS_INT8_DESCRIPTION
WS_IP_VERSION = Int32
WS_IP_VERSION_4 = 1
WS_IP_VERSION_6 = 2
WS_IP_VERSION_AUTO = 3
def _define_WS_IS_DEFAULT_VALUE_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,c_void_p,c_void_p,UInt32,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_ISSUED_TOKEN_MESSAGE_SECURITY_BINDING_CONSTRAINT_head():
    class WS_ISSUED_TOKEN_MESSAGE_SECURITY_BINDING_CONSTRAINT(Structure):
        pass
    return WS_ISSUED_TOKEN_MESSAGE_SECURITY_BINDING_CONSTRAINT
def _define_WS_ISSUED_TOKEN_MESSAGE_SECURITY_BINDING_CONSTRAINT():
    WS_ISSUED_TOKEN_MESSAGE_SECURITY_BINDING_CONSTRAINT = win32more.Networking.WindowsWebServices.WS_ISSUED_TOKEN_MESSAGE_SECURITY_BINDING_CONSTRAINT_head
    class WS_ISSUED_TOKEN_MESSAGE_SECURITY_BINDING_CONSTRAINT__out_e__Struct(Structure):
        pass
    WS_ISSUED_TOKEN_MESSAGE_SECURITY_BINDING_CONSTRAINT__out_e__Struct._fields_ = [
        ('issuerAddress', POINTER(win32more.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS_head)),
        ('requestSecurityTokenTemplate', POINTER(win32more.Networking.WindowsWebServices.WS_XML_BUFFER_head)),
    ]
    WS_ISSUED_TOKEN_MESSAGE_SECURITY_BINDING_CONSTRAINT._fields_ = [
        ('bindingConstraint', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT),
        ('bindingUsage', win32more.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE),
        ('claimConstraints', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('claimConstraintCount', UInt32),
        ('requestSecurityTokenPropertyConstraints', POINTER(win32more.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_PROPERTY_CONSTRAINT_head)),
        ('requestSecurityTokenPropertyConstraintCount', UInt32),
        ('out', WS_ISSUED_TOKEN_MESSAGE_SECURITY_BINDING_CONSTRAINT__out_e__Struct),
    ]
    return WS_ISSUED_TOKEN_MESSAGE_SECURITY_BINDING_CONSTRAINT
def _define_WS_ITEM_RANGE_head():
    class WS_ITEM_RANGE(Structure):
        pass
    return WS_ITEM_RANGE
def _define_WS_ITEM_RANGE():
    WS_ITEM_RANGE = win32more.Networking.WindowsWebServices.WS_ITEM_RANGE_head
    WS_ITEM_RANGE._fields_ = [
        ('minItemCount', UInt32),
        ('maxItemCount', UInt32),
    ]
    return WS_ITEM_RANGE
def _define_WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_head():
    class WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING(Structure):
        pass
    return WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING
def _define_WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING():
    WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING = win32more.Networking.WindowsWebServices.WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_head
    WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING._fields_ = [
        ('binding', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING),
        ('bindingUsage', win32more.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE),
        ('clientCredential', POINTER(win32more.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_head)),
    ]
    return WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING
def _define_WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_CONSTRAINT_head():
    class WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_CONSTRAINT(Structure):
        pass
    return WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_CONSTRAINT
def _define_WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_CONSTRAINT():
    WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_CONSTRAINT = win32more.Networking.WindowsWebServices.WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_CONSTRAINT_head
    WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_CONSTRAINT._fields_ = [
        ('bindingConstraint', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT),
        ('bindingUsage', win32more.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE),
    ]
    return WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_CONSTRAINT
def _define_WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION_head():
    class WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION(Structure):
        pass
    return WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION
def _define_WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION():
    WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION_head
    WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION._fields_ = [
        ('securityBindingProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES),
        ('bindingUsage', win32more.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE),
    ]
    return WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION
def _define_WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_TEMPLATE_head():
    class WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_TEMPLATE(Structure):
        pass
    return WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_TEMPLATE
def _define_WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_TEMPLATE():
    WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_TEMPLATE = win32more.Networking.WindowsWebServices.WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_TEMPLATE_head
    WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_TEMPLATE._fields_ = [
        ('securityBindingProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES),
        ('clientCredential', POINTER(win32more.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_head)),
    ]
    return WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_TEMPLATE
def _define_WS_LISTENER_head():
    class WS_LISTENER(Structure):
        pass
    return WS_LISTENER
def _define_WS_LISTENER():
    WS_LISTENER = win32more.Networking.WindowsWebServices.WS_LISTENER_head
    return WS_LISTENER
def _define_WS_LISTENER_PROPERTIES_head():
    class WS_LISTENER_PROPERTIES(Structure):
        pass
    return WS_LISTENER_PROPERTIES
def _define_WS_LISTENER_PROPERTIES():
    WS_LISTENER_PROPERTIES = win32more.Networking.WindowsWebServices.WS_LISTENER_PROPERTIES_head
    WS_LISTENER_PROPERTIES._fields_ = [
        ('properties', POINTER(win32more.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_head)),
        ('propertyCount', UInt32),
    ]
    return WS_LISTENER_PROPERTIES
def _define_WS_LISTENER_PROPERTY_head():
    class WS_LISTENER_PROPERTY(Structure):
        pass
    return WS_LISTENER_PROPERTY
def _define_WS_LISTENER_PROPERTY():
    WS_LISTENER_PROPERTY = win32more.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_head
    WS_LISTENER_PROPERTY._fields_ = [
        ('id', win32more.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID),
        ('value', c_void_p),
        ('valueSize', UInt32),
    ]
    return WS_LISTENER_PROPERTY
WS_LISTENER_PROPERTY_ID = Int32
WS_LISTENER_PROPERTY_LISTEN_BACKLOG = 0
WS_LISTENER_PROPERTY_IP_VERSION = 1
WS_LISTENER_PROPERTY_STATE = 2
WS_LISTENER_PROPERTY_ASYNC_CALLBACK_MODEL = 3
WS_LISTENER_PROPERTY_CHANNEL_TYPE = 4
WS_LISTENER_PROPERTY_CHANNEL_BINDING = 5
WS_LISTENER_PROPERTY_CONNECT_TIMEOUT = 6
WS_LISTENER_PROPERTY_IS_MULTICAST = 7
WS_LISTENER_PROPERTY_MULTICAST_INTERFACES = 8
WS_LISTENER_PROPERTY_MULTICAST_LOOPBACK = 9
WS_LISTENER_PROPERTY_CLOSE_TIMEOUT = 10
WS_LISTENER_PROPERTY_TO_HEADER_MATCHING_OPTIONS = 11
WS_LISTENER_PROPERTY_TRANSPORT_URL_MATCHING_OPTIONS = 12
WS_LISTENER_PROPERTY_CUSTOM_LISTENER_CALLBACKS = 13
WS_LISTENER_PROPERTY_CUSTOM_LISTENER_PARAMETERS = 14
WS_LISTENER_PROPERTY_CUSTOM_LISTENER_INSTANCE = 15
WS_LISTENER_PROPERTY_DISALLOWED_USER_AGENT = 16
WS_LISTENER_STATE = Int32
WS_LISTENER_STATE_CREATED = 0
WS_LISTENER_STATE_OPENING = 1
WS_LISTENER_STATE_OPEN = 2
WS_LISTENER_STATE_FAULTED = 3
WS_LISTENER_STATE_CLOSING = 4
WS_LISTENER_STATE_CLOSED = 5
def _define_WS_MESSAGE_head():
    class WS_MESSAGE(Structure):
        pass
    return WS_MESSAGE
def _define_WS_MESSAGE():
    WS_MESSAGE = win32more.Networking.WindowsWebServices.WS_MESSAGE_head
    return WS_MESSAGE
def _define_WS_MESSAGE_DESCRIPTION_head():
    class WS_MESSAGE_DESCRIPTION(Structure):
        pass
    return WS_MESSAGE_DESCRIPTION
def _define_WS_MESSAGE_DESCRIPTION():
    WS_MESSAGE_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_MESSAGE_DESCRIPTION_head
    WS_MESSAGE_DESCRIPTION._fields_ = [
        ('action', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('bodyElementDescription', POINTER(win32more.Networking.WindowsWebServices.WS_ELEMENT_DESCRIPTION_head)),
    ]
    return WS_MESSAGE_DESCRIPTION
def _define_WS_MESSAGE_DONE_CALLBACK():
    return WINFUNCTYPE(Void,c_void_p)
WS_MESSAGE_INITIALIZATION = Int32
WS_BLANK_MESSAGE = 0
WS_DUPLICATE_MESSAGE = 1
WS_REQUEST_MESSAGE = 2
WS_REPLY_MESSAGE = 3
WS_FAULT_MESSAGE = 4
def _define_WS_MESSAGE_PROPERTIES_head():
    class WS_MESSAGE_PROPERTIES(Structure):
        pass
    return WS_MESSAGE_PROPERTIES
def _define_WS_MESSAGE_PROPERTIES():
    WS_MESSAGE_PROPERTIES = win32more.Networking.WindowsWebServices.WS_MESSAGE_PROPERTIES_head
    WS_MESSAGE_PROPERTIES._fields_ = [
        ('properties', POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_head)),
        ('propertyCount', UInt32),
    ]
    return WS_MESSAGE_PROPERTIES
def _define_WS_MESSAGE_PROPERTY_head():
    class WS_MESSAGE_PROPERTY(Structure):
        pass
    return WS_MESSAGE_PROPERTY
def _define_WS_MESSAGE_PROPERTY():
    WS_MESSAGE_PROPERTY = win32more.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_head
    WS_MESSAGE_PROPERTY._fields_ = [
        ('id', win32more.Networking.WindowsWebServices.WS_MESSAGE_PROPERTY_ID),
        ('value', c_void_p),
        ('valueSize', UInt32),
    ]
    return WS_MESSAGE_PROPERTY
WS_MESSAGE_PROPERTY_ID = Int32
WS_MESSAGE_PROPERTY_STATE = 0
WS_MESSAGE_PROPERTY_HEAP = 1
WS_MESSAGE_PROPERTY_ENVELOPE_VERSION = 2
WS_MESSAGE_PROPERTY_ADDRESSING_VERSION = 3
WS_MESSAGE_PROPERTY_HEADER_BUFFER = 4
WS_MESSAGE_PROPERTY_HEADER_POSITION = 5
WS_MESSAGE_PROPERTY_BODY_READER = 6
WS_MESSAGE_PROPERTY_BODY_WRITER = 7
WS_MESSAGE_PROPERTY_IS_ADDRESSED = 8
WS_MESSAGE_PROPERTY_HEAP_PROPERTIES = 9
WS_MESSAGE_PROPERTY_XML_READER_PROPERTIES = 10
WS_MESSAGE_PROPERTY_XML_WRITER_PROPERTIES = 11
WS_MESSAGE_PROPERTY_IS_FAULT = 12
WS_MESSAGE_PROPERTY_MAX_PROCESSED_HEADERS = 13
WS_MESSAGE_PROPERTY_USERNAME = 14
WS_MESSAGE_PROPERTY_ENCODED_CERT = 15
WS_MESSAGE_PROPERTY_TRANSPORT_SECURITY_WINDOWS_TOKEN = 16
WS_MESSAGE_PROPERTY_HTTP_HEADER_AUTH_WINDOWS_TOKEN = 17
WS_MESSAGE_PROPERTY_MESSAGE_SECURITY_WINDOWS_TOKEN = 18
WS_MESSAGE_PROPERTY_SAML_ASSERTION = 19
WS_MESSAGE_PROPERTY_SECURITY_CONTEXT = 20
WS_MESSAGE_PROPERTY_PROTECTION_LEVEL = 21
WS_MESSAGE_SECURITY_USAGE = Int32
WS_SUPPORTING_MESSAGE_SECURITY_USAGE = 1
WS_MESSAGE_STATE = Int32
WS_MESSAGE_STATE_EMPTY = 1
WS_MESSAGE_STATE_INITIALIZED = 2
WS_MESSAGE_STATE_READING = 3
WS_MESSAGE_STATE_WRITING = 4
WS_MESSAGE_STATE_DONE = 5
def _define_WS_METADATA_head():
    class WS_METADATA(Structure):
        pass
    return WS_METADATA
def _define_WS_METADATA():
    WS_METADATA = win32more.Networking.WindowsWebServices.WS_METADATA_head
    return WS_METADATA
def _define_WS_METADATA_ENDPOINT_head():
    class WS_METADATA_ENDPOINT(Structure):
        pass
    return WS_METADATA_ENDPOINT
def _define_WS_METADATA_ENDPOINT():
    WS_METADATA_ENDPOINT = win32more.Networking.WindowsWebServices.WS_METADATA_ENDPOINT_head
    WS_METADATA_ENDPOINT._fields_ = [
        ('endpointAddress', win32more.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS),
        ('endpointPolicy', POINTER(win32more.Networking.WindowsWebServices.WS_POLICY_head)),
        ('portName', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('serviceName', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('serviceNs', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('bindingName', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('bindingNs', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('portTypeName', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('portTypeNs', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
    ]
    return WS_METADATA_ENDPOINT
def _define_WS_METADATA_ENDPOINTS_head():
    class WS_METADATA_ENDPOINTS(Structure):
        pass
    return WS_METADATA_ENDPOINTS
def _define_WS_METADATA_ENDPOINTS():
    WS_METADATA_ENDPOINTS = win32more.Networking.WindowsWebServices.WS_METADATA_ENDPOINTS_head
    WS_METADATA_ENDPOINTS._fields_ = [
        ('endpoints', POINTER(win32more.Networking.WindowsWebServices.WS_METADATA_ENDPOINT_head)),
        ('endpointCount', UInt32),
    ]
    return WS_METADATA_ENDPOINTS
WS_METADATA_EXCHANGE_TYPE = Int32
WS_METADATA_EXCHANGE_TYPE_NONE = 0
WS_METADATA_EXCHANGE_TYPE_MEX = 1
WS_METADATA_EXCHANGE_TYPE_HTTP_GET = 2
def _define_WS_METADATA_PROPERTY_head():
    class WS_METADATA_PROPERTY(Structure):
        pass
    return WS_METADATA_PROPERTY
def _define_WS_METADATA_PROPERTY():
    WS_METADATA_PROPERTY = win32more.Networking.WindowsWebServices.WS_METADATA_PROPERTY_head
    WS_METADATA_PROPERTY._fields_ = [
        ('id', win32more.Networking.WindowsWebServices.WS_METADATA_PROPERTY_ID),
        ('value', c_void_p),
        ('valueSize', UInt32),
    ]
    return WS_METADATA_PROPERTY
WS_METADATA_PROPERTY_ID = Int32
WS_METADATA_PROPERTY_STATE = 1
WS_METADATA_PROPERTY_HEAP_PROPERTIES = 2
WS_METADATA_PROPERTY_POLICY_PROPERTIES = 3
WS_METADATA_PROPERTY_HEAP_REQUESTED_SIZE = 4
WS_METADATA_PROPERTY_MAX_DOCUMENTS = 5
WS_METADATA_PROPERTY_HOST_NAMES = 6
WS_METADATA_PROPERTY_VERIFY_HOST_NAMES = 7
WS_METADATA_STATE = Int32
WS_METADATA_STATE_CREATED = 1
WS_METADATA_STATE_RESOLVED = 2
WS_METADATA_STATE_FAULTED = 3
WS_MOVE_TO = Int32
WS_MOVE_TO_ROOT_ELEMENT = 0
WS_MOVE_TO_NEXT_ELEMENT = 1
WS_MOVE_TO_PREVIOUS_ELEMENT = 2
WS_MOVE_TO_CHILD_ELEMENT = 3
WS_MOVE_TO_END_ELEMENT = 4
WS_MOVE_TO_PARENT_ELEMENT = 5
WS_MOVE_TO_NEXT_NODE = 6
WS_MOVE_TO_PREVIOUS_NODE = 7
WS_MOVE_TO_FIRST_NODE = 8
WS_MOVE_TO_BOF = 9
WS_MOVE_TO_EOF = 10
WS_MOVE_TO_CHILD_NODE = 11
def _define_WS_NAMEDPIPE_SSPI_TRANSPORT_SECURITY_BINDING_head():
    class WS_NAMEDPIPE_SSPI_TRANSPORT_SECURITY_BINDING(Structure):
        pass
    return WS_NAMEDPIPE_SSPI_TRANSPORT_SECURITY_BINDING
def _define_WS_NAMEDPIPE_SSPI_TRANSPORT_SECURITY_BINDING():
    WS_NAMEDPIPE_SSPI_TRANSPORT_SECURITY_BINDING = win32more.Networking.WindowsWebServices.WS_NAMEDPIPE_SSPI_TRANSPORT_SECURITY_BINDING_head
    WS_NAMEDPIPE_SSPI_TRANSPORT_SECURITY_BINDING._fields_ = [
        ('binding', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING),
        ('clientCredential', POINTER(win32more.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_head)),
    ]
    return WS_NAMEDPIPE_SSPI_TRANSPORT_SECURITY_BINDING
def _define_WS_NCRYPT_ASYMMETRIC_SECURITY_KEY_HANDLE_head():
    class WS_NCRYPT_ASYMMETRIC_SECURITY_KEY_HANDLE(Structure):
        pass
    return WS_NCRYPT_ASYMMETRIC_SECURITY_KEY_HANDLE
def _define_WS_NCRYPT_ASYMMETRIC_SECURITY_KEY_HANDLE():
    WS_NCRYPT_ASYMMETRIC_SECURITY_KEY_HANDLE = win32more.Networking.WindowsWebServices.WS_NCRYPT_ASYMMETRIC_SECURITY_KEY_HANDLE_head
    WS_NCRYPT_ASYMMETRIC_SECURITY_KEY_HANDLE._fields_ = [
        ('keyHandle', win32more.Networking.WindowsWebServices.WS_SECURITY_KEY_HANDLE),
        ('asymmetricKey', win32more.Security.Cryptography.NCRYPT_KEY_HANDLE),
    ]
    return WS_NCRYPT_ASYMMETRIC_SECURITY_KEY_HANDLE
def _define_WS_NETPIPE_URL_head():
    class WS_NETPIPE_URL(Structure):
        pass
    return WS_NETPIPE_URL
def _define_WS_NETPIPE_URL():
    WS_NETPIPE_URL = win32more.Networking.WindowsWebServices.WS_NETPIPE_URL_head
    WS_NETPIPE_URL._fields_ = [
        ('url', win32more.Networking.WindowsWebServices.WS_URL),
        ('host', win32more.Networking.WindowsWebServices.WS_STRING),
        ('port', UInt16),
        ('portAsString', win32more.Networking.WindowsWebServices.WS_STRING),
        ('path', win32more.Networking.WindowsWebServices.WS_STRING),
        ('query', win32more.Networking.WindowsWebServices.WS_STRING),
        ('fragment', win32more.Networking.WindowsWebServices.WS_STRING),
    ]
    return WS_NETPIPE_URL
def _define_WS_NETTCP_URL_head():
    class WS_NETTCP_URL(Structure):
        pass
    return WS_NETTCP_URL
def _define_WS_NETTCP_URL():
    WS_NETTCP_URL = win32more.Networking.WindowsWebServices.WS_NETTCP_URL_head
    WS_NETTCP_URL._fields_ = [
        ('url', win32more.Networking.WindowsWebServices.WS_URL),
        ('host', win32more.Networking.WindowsWebServices.WS_STRING),
        ('port', UInt16),
        ('portAsString', win32more.Networking.WindowsWebServices.WS_STRING),
        ('path', win32more.Networking.WindowsWebServices.WS_STRING),
        ('query', win32more.Networking.WindowsWebServices.WS_STRING),
        ('fragment', win32more.Networking.WindowsWebServices.WS_STRING),
    ]
    return WS_NETTCP_URL
def _define_WS_OPAQUE_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_head():
    class WS_OPAQUE_WINDOWS_INTEGRATED_AUTH_CREDENTIAL(Structure):
        pass
    return WS_OPAQUE_WINDOWS_INTEGRATED_AUTH_CREDENTIAL
def _define_WS_OPAQUE_WINDOWS_INTEGRATED_AUTH_CREDENTIAL():
    WS_OPAQUE_WINDOWS_INTEGRATED_AUTH_CREDENTIAL = win32more.Networking.WindowsWebServices.WS_OPAQUE_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_head
    WS_OPAQUE_WINDOWS_INTEGRATED_AUTH_CREDENTIAL._fields_ = [
        ('credential', win32more.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL),
        ('opaqueAuthIdentity', c_void_p),
    ]
    return WS_OPAQUE_WINDOWS_INTEGRATED_AUTH_CREDENTIAL
def _define_WS_OPEN_CHANNEL_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS_head),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_OPEN_LISTENER_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_OPERATION_CANCEL_CALLBACK():
    return WINFUNCTYPE(Void,win32more.Networking.WindowsWebServices.WS_SERVICE_CANCEL_REASON,c_void_p)
def _define_WS_OPERATION_CONTEXT_head():
    class WS_OPERATION_CONTEXT(Structure):
        pass
    return WS_OPERATION_CONTEXT
def _define_WS_OPERATION_CONTEXT():
    WS_OPERATION_CONTEXT = win32more.Networking.WindowsWebServices.WS_OPERATION_CONTEXT_head
    return WS_OPERATION_CONTEXT
WS_OPERATION_CONTEXT_PROPERTY_ID = Int32
WS_OPERATION_CONTEXT_PROPERTY_CHANNEL = 0
WS_OPERATION_CONTEXT_PROPERTY_CONTRACT_DESCRIPTION = 1
WS_OPERATION_CONTEXT_PROPERTY_HOST_USER_STATE = 2
WS_OPERATION_CONTEXT_PROPERTY_CHANNEL_USER_STATE = 3
WS_OPERATION_CONTEXT_PROPERTY_INPUT_MESSAGE = 4
WS_OPERATION_CONTEXT_PROPERTY_OUTPUT_MESSAGE = 5
WS_OPERATION_CONTEXT_PROPERTY_HEAP = 6
WS_OPERATION_CONTEXT_PROPERTY_LISTENER = 7
WS_OPERATION_CONTEXT_PROPERTY_ENDPOINT_ADDRESS = 8
def _define_WS_OPERATION_DESCRIPTION_head():
    class WS_OPERATION_DESCRIPTION(Structure):
        pass
    return WS_OPERATION_DESCRIPTION
def _define_WS_OPERATION_DESCRIPTION():
    WS_OPERATION_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_OPERATION_DESCRIPTION_head
    WS_OPERATION_DESCRIPTION._fields_ = [
        ('versionInfo', UInt32),
        ('inputMessageDescription', POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_DESCRIPTION_head)),
        ('outputMessageDescription', POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_DESCRIPTION_head)),
        ('inputMessageOptions', UInt32),
        ('outputMessageOptions', UInt32),
        ('parameterCount', UInt16),
        ('parameterDescription', POINTER(win32more.Networking.WindowsWebServices.WS_PARAMETER_DESCRIPTION_head)),
        ('stubCallback', win32more.Networking.WindowsWebServices.WS_SERVICE_STUB_CALLBACK),
        ('style', win32more.Networking.WindowsWebServices.WS_OPERATION_STYLE),
    ]
    return WS_OPERATION_DESCRIPTION
def _define_WS_OPERATION_FREE_STATE_CALLBACK():
    return WINFUNCTYPE(Void,c_void_p)
WS_OPERATION_STYLE = Int32
WS_NON_RPC_LITERAL_OPERATION = 0
WS_RPC_LITERAL_OPERATION = 1
def _define_WS_PARAMETER_DESCRIPTION_head():
    class WS_PARAMETER_DESCRIPTION(Structure):
        pass
    return WS_PARAMETER_DESCRIPTION
def _define_WS_PARAMETER_DESCRIPTION():
    WS_PARAMETER_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_PARAMETER_DESCRIPTION_head
    WS_PARAMETER_DESCRIPTION._fields_ = [
        ('parameterType', win32more.Networking.WindowsWebServices.WS_PARAMETER_TYPE),
        ('inputMessageIndex', UInt16),
        ('outputMessageIndex', UInt16),
    ]
    return WS_PARAMETER_DESCRIPTION
WS_PARAMETER_TYPE = Int32
WS_PARAMETER_TYPE_NORMAL = 0
WS_PARAMETER_TYPE_ARRAY = 1
WS_PARAMETER_TYPE_ARRAY_COUNT = 2
WS_PARAMETER_TYPE_MESSAGES = 3
def _define_WS_POLICY_head():
    class WS_POLICY(Structure):
        pass
    return WS_POLICY
def _define_WS_POLICY():
    WS_POLICY = win32more.Networking.WindowsWebServices.WS_POLICY_head
    return WS_POLICY
def _define_WS_POLICY_CONSTRAINTS_head():
    class WS_POLICY_CONSTRAINTS(Structure):
        pass
    return WS_POLICY_CONSTRAINTS
def _define_WS_POLICY_CONSTRAINTS():
    WS_POLICY_CONSTRAINTS = win32more.Networking.WindowsWebServices.WS_POLICY_CONSTRAINTS_head
    WS_POLICY_CONSTRAINTS._fields_ = [
        ('channelBinding', win32more.Networking.WindowsWebServices.WS_CHANNEL_BINDING),
        ('channelPropertyConstraints', POINTER(win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_CONSTRAINT_head)),
        ('channelPropertyConstraintCount', UInt32),
        ('securityConstraints', POINTER(win32more.Networking.WindowsWebServices.WS_SECURITY_CONSTRAINTS_head)),
        ('policyExtensions', POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_POLICY_EXTENSION_head))),
        ('policyExtensionCount', UInt32),
    ]
    return WS_POLICY_CONSTRAINTS
def _define_WS_POLICY_EXTENSION_head():
    class WS_POLICY_EXTENSION(Structure):
        pass
    return WS_POLICY_EXTENSION
def _define_WS_POLICY_EXTENSION():
    WS_POLICY_EXTENSION = win32more.Networking.WindowsWebServices.WS_POLICY_EXTENSION_head
    WS_POLICY_EXTENSION._fields_ = [
        ('type', win32more.Networking.WindowsWebServices.WS_POLICY_EXTENSION_TYPE),
    ]
    return WS_POLICY_EXTENSION
WS_POLICY_EXTENSION_TYPE = Int32
WS_ENDPOINT_POLICY_EXTENSION_TYPE = 1
def _define_WS_POLICY_PROPERTIES_head():
    class WS_POLICY_PROPERTIES(Structure):
        pass
    return WS_POLICY_PROPERTIES
def _define_WS_POLICY_PROPERTIES():
    WS_POLICY_PROPERTIES = win32more.Networking.WindowsWebServices.WS_POLICY_PROPERTIES_head
    WS_POLICY_PROPERTIES._fields_ = [
        ('properties', POINTER(win32more.Networking.WindowsWebServices.WS_POLICY_PROPERTY_head)),
        ('propertyCount', UInt32),
    ]
    return WS_POLICY_PROPERTIES
def _define_WS_POLICY_PROPERTY_head():
    class WS_POLICY_PROPERTY(Structure):
        pass
    return WS_POLICY_PROPERTY
def _define_WS_POLICY_PROPERTY():
    WS_POLICY_PROPERTY = win32more.Networking.WindowsWebServices.WS_POLICY_PROPERTY_head
    WS_POLICY_PROPERTY._fields_ = [
        ('id', win32more.Networking.WindowsWebServices.WS_POLICY_PROPERTY_ID),
        ('value', c_void_p),
        ('valueSize', UInt32),
    ]
    return WS_POLICY_PROPERTY
WS_POLICY_PROPERTY_ID = Int32
WS_POLICY_PROPERTY_STATE = 1
WS_POLICY_PROPERTY_MAX_ALTERNATIVES = 2
WS_POLICY_PROPERTY_MAX_DEPTH = 3
WS_POLICY_PROPERTY_MAX_EXTENSIONS = 4
WS_POLICY_STATE = Int32
WS_POLICY_STATE_CREATED = 1
WS_POLICY_STATE_FAULTED = 2
WS_PROTECTION_LEVEL = Int32
WS_PROTECTION_LEVEL_NONE = 1
WS_PROTECTION_LEVEL_SIGN = 2
WS_PROTECTION_LEVEL_SIGN_AND_ENCRYPT = 3
def _define_WS_PROXY_MESSAGE_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head),c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_PROXY_MESSAGE_CALLBACK_CONTEXT_head():
    class WS_PROXY_MESSAGE_CALLBACK_CONTEXT(Structure):
        pass
    return WS_PROXY_MESSAGE_CALLBACK_CONTEXT
def _define_WS_PROXY_MESSAGE_CALLBACK_CONTEXT():
    WS_PROXY_MESSAGE_CALLBACK_CONTEXT = win32more.Networking.WindowsWebServices.WS_PROXY_MESSAGE_CALLBACK_CONTEXT_head
    WS_PROXY_MESSAGE_CALLBACK_CONTEXT._fields_ = [
        ('callback', win32more.Networking.WindowsWebServices.WS_PROXY_MESSAGE_CALLBACK),
        ('state', c_void_p),
    ]
    return WS_PROXY_MESSAGE_CALLBACK_CONTEXT
def _define_WS_PROXY_PROPERTY_head():
    class WS_PROXY_PROPERTY(Structure):
        pass
    return WS_PROXY_PROPERTY
def _define_WS_PROXY_PROPERTY():
    WS_PROXY_PROPERTY = win32more.Networking.WindowsWebServices.WS_PROXY_PROPERTY_head
    WS_PROXY_PROPERTY._fields_ = [
        ('id', win32more.Networking.WindowsWebServices.WS_PROXY_PROPERTY_ID),
        ('value', c_void_p),
        ('valueSize', UInt32),
    ]
    return WS_PROXY_PROPERTY
WS_PROXY_PROPERTY_ID = Int32
WS_PROXY_PROPERTY_CALL_TIMEOUT = 0
WS_PROXY_PROPERTY_MESSAGE_PROPERTIES = 1
WS_PROXY_PROPERTY_MAX_CALL_POOL_SIZE = 2
WS_PROXY_PROPERTY_STATE = 3
WS_PROXY_PROPERTY_MAX_PENDING_CALLS = 4
WS_PROXY_PROPERTY_MAX_CLOSE_TIMEOUT = 5
WS_PROXY_FAULT_LANG_ID = 6
def _define_WS_PULL_BYTES_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,c_void_p,UInt32,POINTER(UInt32),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_PUSH_BYTES_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Networking.WindowsWebServices.WS_WRITE_CALLBACK,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_RAW_SYMMETRIC_SECURITY_KEY_HANDLE_head():
    class WS_RAW_SYMMETRIC_SECURITY_KEY_HANDLE(Structure):
        pass
    return WS_RAW_SYMMETRIC_SECURITY_KEY_HANDLE
def _define_WS_RAW_SYMMETRIC_SECURITY_KEY_HANDLE():
    WS_RAW_SYMMETRIC_SECURITY_KEY_HANDLE = win32more.Networking.WindowsWebServices.WS_RAW_SYMMETRIC_SECURITY_KEY_HANDLE_head
    WS_RAW_SYMMETRIC_SECURITY_KEY_HANDLE._fields_ = [
        ('keyHandle', win32more.Networking.WindowsWebServices.WS_SECURITY_KEY_HANDLE),
        ('rawKeyBytes', win32more.Networking.WindowsWebServices.WS_BYTES),
    ]
    return WS_RAW_SYMMETRIC_SECURITY_KEY_HANDLE
def _define_WS_READ_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,c_void_p,UInt32,POINTER(UInt32),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_READ_MESSAGE_END_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_READ_MESSAGE_START_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
WS_READ_OPTION = Int32
WS_READ_REQUIRED_VALUE = 1
WS_READ_REQUIRED_POINTER = 2
WS_READ_OPTIONAL_POINTER = 3
WS_READ_NILLABLE_POINTER = 4
WS_READ_NILLABLE_VALUE = 5
def _define_WS_READ_TYPE_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_head),win32more.Networking.WindowsWebServices.WS_TYPE_MAPPING,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_HEAP_head),c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
WS_RECEIVE_OPTION = Int32
WS_RECEIVE_REQUIRED_MESSAGE = 1
WS_RECEIVE_OPTIONAL_MESSAGE = 2
WS_REPEATING_HEADER_OPTION = Int32
WS_REPEATING_HEADER = 1
WS_SINGLETON_HEADER = 2
WS_REQUEST_SECURITY_TOKEN_ACTION = Int32
WS_REQUEST_SECURITY_TOKEN_ACTION_ISSUE = 1
WS_REQUEST_SECURITY_TOKEN_ACTION_NEW_CONTEXT = 2
WS_REQUEST_SECURITY_TOKEN_ACTION_RENEW_CONTEXT = 3
def _define_WS_REQUEST_SECURITY_TOKEN_PROPERTY_head():
    class WS_REQUEST_SECURITY_TOKEN_PROPERTY(Structure):
        pass
    return WS_REQUEST_SECURITY_TOKEN_PROPERTY
def _define_WS_REQUEST_SECURITY_TOKEN_PROPERTY():
    WS_REQUEST_SECURITY_TOKEN_PROPERTY = win32more.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_PROPERTY_head
    WS_REQUEST_SECURITY_TOKEN_PROPERTY._fields_ = [
        ('id', win32more.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID),
        ('value', c_void_p),
        ('valueSize', UInt32),
    ]
    return WS_REQUEST_SECURITY_TOKEN_PROPERTY
def _define_WS_REQUEST_SECURITY_TOKEN_PROPERTY_CONSTRAINT_head():
    class WS_REQUEST_SECURITY_TOKEN_PROPERTY_CONSTRAINT(Structure):
        pass
    return WS_REQUEST_SECURITY_TOKEN_PROPERTY_CONSTRAINT
def _define_WS_REQUEST_SECURITY_TOKEN_PROPERTY_CONSTRAINT():
    WS_REQUEST_SECURITY_TOKEN_PROPERTY_CONSTRAINT = win32more.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_PROPERTY_CONSTRAINT_head
    class WS_REQUEST_SECURITY_TOKEN_PROPERTY_CONSTRAINT__out_e__Struct(Structure):
        pass
    WS_REQUEST_SECURITY_TOKEN_PROPERTY_CONSTRAINT__out_e__Struct._fields_ = [
        ('requestSecurityTokenProperty', win32more.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_PROPERTY),
    ]
    WS_REQUEST_SECURITY_TOKEN_PROPERTY_CONSTRAINT._fields_ = [
        ('id', win32more.Networking.WindowsWebServices.WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID),
        ('allowedValues', c_void_p),
        ('allowedValuesSize', UInt32),
        ('out', WS_REQUEST_SECURITY_TOKEN_PROPERTY_CONSTRAINT__out_e__Struct),
    ]
    return WS_REQUEST_SECURITY_TOKEN_PROPERTY_CONSTRAINT
WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID = Int32
WS_REQUEST_SECURITY_TOKEN_PROPERTY_APPLIES_TO = 1
WS_REQUEST_SECURITY_TOKEN_PROPERTY_TRUST_VERSION = 2
WS_REQUEST_SECURITY_TOKEN_PROPERTY_SECURE_CONVERSATION_VERSION = 3
WS_REQUEST_SECURITY_TOKEN_PROPERTY_ISSUED_TOKEN_TYPE = 4
WS_REQUEST_SECURITY_TOKEN_PROPERTY_REQUEST_ACTION = 5
WS_REQUEST_SECURITY_TOKEN_PROPERTY_EXISTING_TOKEN = 6
WS_REQUEST_SECURITY_TOKEN_PROPERTY_ISSUED_TOKEN_KEY_TYPE = 7
WS_REQUEST_SECURITY_TOKEN_PROPERTY_ISSUED_TOKEN_KEY_SIZE = 8
WS_REQUEST_SECURITY_TOKEN_PROPERTY_ISSUED_TOKEN_KEY_ENTROPY = 9
WS_REQUEST_SECURITY_TOKEN_PROPERTY_LOCAL_REQUEST_PARAMETERS = 10
WS_REQUEST_SECURITY_TOKEN_PROPERTY_SERVICE_REQUEST_PARAMETERS = 11
WS_REQUEST_SECURITY_TOKEN_PROPERTY_MESSAGE_PROPERTIES = 12
WS_REQUEST_SECURITY_TOKEN_PROPERTY_BEARER_KEY_TYPE_VERSION = 13
def _define_WS_RESET_CHANNEL_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_RESET_LISTENER_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_RSA_ENDPOINT_IDENTITY_head():
    class WS_RSA_ENDPOINT_IDENTITY(Structure):
        pass
    return WS_RSA_ENDPOINT_IDENTITY
def _define_WS_RSA_ENDPOINT_IDENTITY():
    WS_RSA_ENDPOINT_IDENTITY = win32more.Networking.WindowsWebServices.WS_RSA_ENDPOINT_IDENTITY_head
    WS_RSA_ENDPOINT_IDENTITY._fields_ = [
        ('identity', win32more.Networking.WindowsWebServices.WS_ENDPOINT_IDENTITY),
        ('modulus', win32more.Networking.WindowsWebServices.WS_BYTES),
        ('exponent', win32more.Networking.WindowsWebServices.WS_BYTES),
    ]
    return WS_RSA_ENDPOINT_IDENTITY
def _define_WS_SAML_AUTHENTICATOR_head():
    class WS_SAML_AUTHENTICATOR(Structure):
        pass
    return WS_SAML_AUTHENTICATOR
def _define_WS_SAML_AUTHENTICATOR():
    WS_SAML_AUTHENTICATOR = win32more.Networking.WindowsWebServices.WS_SAML_AUTHENTICATOR_head
    WS_SAML_AUTHENTICATOR._fields_ = [
        ('authenticatorType', win32more.Networking.WindowsWebServices.WS_SAML_AUTHENTICATOR_TYPE),
    ]
    return WS_SAML_AUTHENTICATOR
WS_SAML_AUTHENTICATOR_TYPE = Int32
WS_CERT_SIGNED_SAML_AUTHENTICATOR_TYPE = 1
def _define_WS_SAML_MESSAGE_SECURITY_BINDING_head():
    class WS_SAML_MESSAGE_SECURITY_BINDING(Structure):
        pass
    return WS_SAML_MESSAGE_SECURITY_BINDING
def _define_WS_SAML_MESSAGE_SECURITY_BINDING():
    WS_SAML_MESSAGE_SECURITY_BINDING = win32more.Networking.WindowsWebServices.WS_SAML_MESSAGE_SECURITY_BINDING_head
    WS_SAML_MESSAGE_SECURITY_BINDING._fields_ = [
        ('binding', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING),
        ('bindingUsage', win32more.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE),
        ('authenticator', POINTER(win32more.Networking.WindowsWebServices.WS_SAML_AUTHENTICATOR_head)),
    ]
    return WS_SAML_MESSAGE_SECURITY_BINDING
WS_SECURE_CONVERSATION_VERSION = Int32
WS_SECURE_CONVERSATION_VERSION_FEBRUARY_2005 = 1
WS_SECURE_CONVERSATION_VERSION_1_3 = 2
WS_SECURE_PROTOCOL = Int32
WS_SECURE_PROTOCOL_SSL2 = 1
WS_SECURE_PROTOCOL_SSL3 = 2
WS_SECURE_PROTOCOL_TLS1_0 = 4
WS_SECURE_PROTOCOL_TLS1_1 = 8
WS_SECURE_PROTOCOL_TLS1_2 = 16
WS_SECURITY_ALGORITHM_ID = Int32
WS_SECURITY_ALGORITHM_DEFAULT = 0
WS_SECURITY_ALGORITHM_CANONICALIZATION_EXCLUSIVE = 1
WS_SECURITY_ALGORITHM_CANONICALIZATION_EXCLUSIVE_WITH_COMMENTS = 2
WS_SECURITY_ALGORITHM_DIGEST_SHA1 = 3
WS_SECURITY_ALGORITHM_DIGEST_SHA_256 = 4
WS_SECURITY_ALGORITHM_DIGEST_SHA_384 = 5
WS_SECURITY_ALGORITHM_DIGEST_SHA_512 = 6
WS_SECURITY_ALGORITHM_SYMMETRIC_SIGNATURE_HMAC_SHA1 = 7
WS_SECURITY_ALGORITHM_SYMMETRIC_SIGNATURE_HMAC_SHA_256 = 8
WS_SECURITY_ALGORITHM_SYMMETRIC_SIGNATURE_HMAC_SHA_384 = 9
WS_SECURITY_ALGORITHM_SYMMETRIC_SIGNATURE_HMAC_SHA_512 = 10
WS_SECURITY_ALGORITHM_ASYMMETRIC_SIGNATURE_RSA_SHA1 = 11
WS_SECURITY_ALGORITHM_ASYMMETRIC_SIGNATURE_DSA_SHA1 = 12
WS_SECURITY_ALGORITHM_ASYMMETRIC_SIGNATURE_RSA_SHA_256 = 13
WS_SECURITY_ALGORITHM_ASYMMETRIC_SIGNATURE_RSA_SHA_384 = 14
WS_SECURITY_ALGORITHM_ASYMMETRIC_SIGNATURE_RSA_SHA_512 = 15
WS_SECURITY_ALGORITHM_ASYMMETRIC_KEYWRAP_RSA_1_5 = 16
WS_SECURITY_ALGORITHM_ASYMMETRIC_KEYWRAP_RSA_OAEP = 17
WS_SECURITY_ALGORITHM_KEY_DERIVATION_P_SHA1 = 18
def _define_WS_SECURITY_ALGORITHM_PROPERTY_head():
    class WS_SECURITY_ALGORITHM_PROPERTY(Structure):
        pass
    return WS_SECURITY_ALGORITHM_PROPERTY
def _define_WS_SECURITY_ALGORITHM_PROPERTY():
    WS_SECURITY_ALGORITHM_PROPERTY = win32more.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_PROPERTY_head
    WS_SECURITY_ALGORITHM_PROPERTY._fields_ = [
        ('id', win32more.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_PROPERTY_ID),
        ('value', c_void_p),
        ('valueSize', UInt32),
    ]
    return WS_SECURITY_ALGORITHM_PROPERTY
WS_SECURITY_ALGORITHM_PROPERTY_ID = Int32
def _define_WS_SECURITY_ALGORITHM_SUITE_head():
    class WS_SECURITY_ALGORITHM_SUITE(Structure):
        pass
    return WS_SECURITY_ALGORITHM_SUITE
def _define_WS_SECURITY_ALGORITHM_SUITE():
    WS_SECURITY_ALGORITHM_SUITE = win32more.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_SUITE_head
    WS_SECURITY_ALGORITHM_SUITE._fields_ = [
        ('canonicalizationAlgorithm', win32more.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID),
        ('digestAlgorithm', win32more.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID),
        ('symmetricSignatureAlgorithm', win32more.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID),
        ('asymmetricSignatureAlgorithm', win32more.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID),
        ('encryptionAlgorithm', win32more.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID),
        ('keyDerivationAlgorithm', win32more.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID),
        ('symmetricKeyWrapAlgorithm', win32more.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID),
        ('asymmetricKeyWrapAlgorithm', win32more.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_ID),
        ('minSymmetricKeyLength', UInt32),
        ('maxSymmetricKeyLength', UInt32),
        ('minAsymmetricKeyLength', UInt32),
        ('maxAsymmetricKeyLength', UInt32),
        ('properties', POINTER(win32more.Networking.WindowsWebServices.WS_SECURITY_ALGORITHM_PROPERTY_head)),
        ('propertyCount', UInt32),
    ]
    return WS_SECURITY_ALGORITHM_SUITE
WS_SECURITY_ALGORITHM_SUITE_NAME = Int32
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC256 = 1
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC192 = 2
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC128 = 3
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC256_RSA15 = 4
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC192_RSA15 = 5
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC128_RSA15 = 6
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC256_SHA256 = 7
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC192_SHA256 = 8
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC128_SHA256 = 9
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC256_SHA256_RSA15 = 10
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC192_SHA256_RSA15 = 11
WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC128_SHA256_RSA15 = 12
WS_SECURITY_BEARER_KEY_TYPE_VERSION = Int32
WS_SECURITY_BEARER_KEY_TYPE_VERSION_1_3_ORIGINAL_SPECIFICATION = 1
WS_SECURITY_BEARER_KEY_TYPE_VERSION_1_3_ORIGINAL_SCHEMA = 2
WS_SECURITY_BEARER_KEY_TYPE_VERSION_1_3_ERRATA_01 = 3
def _define_WS_SECURITY_BINDING_head():
    class WS_SECURITY_BINDING(Structure):
        pass
    return WS_SECURITY_BINDING
def _define_WS_SECURITY_BINDING():
    WS_SECURITY_BINDING = win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_head
    WS_SECURITY_BINDING._fields_ = [
        ('bindingType', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_TYPE),
        ('properties', POINTER(win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_head)),
        ('propertyCount', UInt32),
    ]
    return WS_SECURITY_BINDING
def _define_WS_SECURITY_BINDING_CONSTRAINT_head():
    class WS_SECURITY_BINDING_CONSTRAINT(Structure):
        pass
    return WS_SECURITY_BINDING_CONSTRAINT
def _define_WS_SECURITY_BINDING_CONSTRAINT():
    WS_SECURITY_BINDING_CONSTRAINT = win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT_head
    WS_SECURITY_BINDING_CONSTRAINT._fields_ = [
        ('type', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT_TYPE),
        ('propertyConstraints', POINTER(win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_CONSTRAINT_head)),
        ('propertyConstraintCount', UInt32),
    ]
    return WS_SECURITY_BINDING_CONSTRAINT
WS_SECURITY_BINDING_CONSTRAINT_TYPE = Int32
WS_SSL_TRANSPORT_SECURITY_BINDING_CONSTRAINT_TYPE = 1
WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_CONSTRAINT_TYPE = 2
WS_HTTP_HEADER_AUTH_SECURITY_BINDING_CONSTRAINT_TYPE = 3
WS_USERNAME_MESSAGE_SECURITY_BINDING_CONSTRAINT_TYPE = 4
WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_CONSTRAINT_TYPE = 5
WS_ISSUED_TOKEN_MESSAGE_SECURITY_BINDING_CONSTRAINT_TYPE = 6
WS_CERT_MESSAGE_SECURITY_BINDING_CONSTRAINT_TYPE = 7
WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_CONSTRAINT_TYPE = 8
def _define_WS_SECURITY_BINDING_PROPERTIES_head():
    class WS_SECURITY_BINDING_PROPERTIES(Structure):
        pass
    return WS_SECURITY_BINDING_PROPERTIES
def _define_WS_SECURITY_BINDING_PROPERTIES():
    WS_SECURITY_BINDING_PROPERTIES = win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES_head
    WS_SECURITY_BINDING_PROPERTIES._fields_ = [
        ('properties', POINTER(win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_head)),
        ('propertyCount', UInt32),
    ]
    return WS_SECURITY_BINDING_PROPERTIES
def _define_WS_SECURITY_BINDING_PROPERTY_head():
    class WS_SECURITY_BINDING_PROPERTY(Structure):
        pass
    return WS_SECURITY_BINDING_PROPERTY
def _define_WS_SECURITY_BINDING_PROPERTY():
    WS_SECURITY_BINDING_PROPERTY = win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_head
    WS_SECURITY_BINDING_PROPERTY._fields_ = [
        ('id', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_ID),
        ('value', c_void_p),
        ('valueSize', UInt32),
    ]
    return WS_SECURITY_BINDING_PROPERTY
def _define_WS_SECURITY_BINDING_PROPERTY_CONSTRAINT_head():
    class WS_SECURITY_BINDING_PROPERTY_CONSTRAINT(Structure):
        pass
    return WS_SECURITY_BINDING_PROPERTY_CONSTRAINT
def _define_WS_SECURITY_BINDING_PROPERTY_CONSTRAINT():
    WS_SECURITY_BINDING_PROPERTY_CONSTRAINT = win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_CONSTRAINT_head
    class WS_SECURITY_BINDING_PROPERTY_CONSTRAINT__out_e__Struct(Structure):
        pass
    WS_SECURITY_BINDING_PROPERTY_CONSTRAINT__out_e__Struct._fields_ = [
        ('securityBindingProperty', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY),
    ]
    WS_SECURITY_BINDING_PROPERTY_CONSTRAINT._fields_ = [
        ('id', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTY_ID),
        ('allowedValues', c_void_p),
        ('allowedValuesSize', UInt32),
        ('out', WS_SECURITY_BINDING_PROPERTY_CONSTRAINT__out_e__Struct),
    ]
    return WS_SECURITY_BINDING_PROPERTY_CONSTRAINT
WS_SECURITY_BINDING_PROPERTY_ID = Int32
WS_SECURITY_BINDING_PROPERTY_REQUIRE_SSL_CLIENT_CERT = 1
WS_SECURITY_BINDING_PROPERTY_WINDOWS_INTEGRATED_AUTH_PACKAGE = 2
WS_SECURITY_BINDING_PROPERTY_REQUIRE_SERVER_AUTH = 3
WS_SECURITY_BINDING_PROPERTY_ALLOW_ANONYMOUS_CLIENTS = 4
WS_SECURITY_BINDING_PROPERTY_ALLOWED_IMPERSONATION_LEVEL = 5
WS_SECURITY_BINDING_PROPERTY_HTTP_HEADER_AUTH_SCHEME = 6
WS_SECURITY_BINDING_PROPERTY_HTTP_HEADER_AUTH_TARGET = 7
WS_SECURITY_BINDING_PROPERTY_HTTP_HEADER_AUTH_BASIC_REALM = 8
WS_SECURITY_BINDING_PROPERTY_HTTP_HEADER_AUTH_DIGEST_REALM = 9
WS_SECURITY_BINDING_PROPERTY_HTTP_HEADER_AUTH_DIGEST_DOMAIN = 10
WS_SECURITY_BINDING_PROPERTY_SECURITY_CONTEXT_KEY_SIZE = 11
WS_SECURITY_BINDING_PROPERTY_SECURITY_CONTEXT_KEY_ENTROPY_MODE = 12
WS_SECURITY_BINDING_PROPERTY_MESSAGE_PROPERTIES = 13
WS_SECURITY_BINDING_PROPERTY_SECURITY_CONTEXT_MAX_PENDING_CONTEXTS = 14
WS_SECURITY_BINDING_PROPERTY_SECURITY_CONTEXT_MAX_ACTIVE_CONTEXTS = 15
WS_SECURITY_BINDING_PROPERTY_SECURE_CONVERSATION_VERSION = 16
WS_SECURITY_BINDING_PROPERTY_SECURITY_CONTEXT_SUPPORT_RENEW = 17
WS_SECURITY_BINDING_PROPERTY_SECURITY_CONTEXT_RENEWAL_INTERVAL = 18
WS_SECURITY_BINDING_PROPERTY_SECURITY_CONTEXT_ROLLOVER_INTERVAL = 19
WS_SECURITY_BINDING_PROPERTY_CERT_FAILURES_TO_IGNORE = 20
WS_SECURITY_BINDING_PROPERTY_DISABLE_CERT_REVOCATION_CHECK = 21
WS_SECURITY_BINDING_PROPERTY_DISALLOWED_SECURE_PROTOCOLS = 22
WS_SECURITY_BINDING_PROPERTY_CERTIFICATE_VALIDATION_CALLBACK_CONTEXT = 23
WS_SECURITY_BINDING_TYPE = Int32
WS_SSL_TRANSPORT_SECURITY_BINDING_TYPE = 1
WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_TYPE = 2
WS_HTTP_HEADER_AUTH_SECURITY_BINDING_TYPE = 3
WS_USERNAME_MESSAGE_SECURITY_BINDING_TYPE = 4
WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_TYPE = 5
WS_XML_TOKEN_MESSAGE_SECURITY_BINDING_TYPE = 6
WS_SAML_MESSAGE_SECURITY_BINDING_TYPE = 7
WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_TYPE = 8
WS_NAMEDPIPE_SSPI_TRANSPORT_SECURITY_BINDING_TYPE = 9
def _define_WS_SECURITY_CONSTRAINTS_head():
    class WS_SECURITY_CONSTRAINTS(Structure):
        pass
    return WS_SECURITY_CONSTRAINTS
def _define_WS_SECURITY_CONSTRAINTS():
    WS_SECURITY_CONSTRAINTS = win32more.Networking.WindowsWebServices.WS_SECURITY_CONSTRAINTS_head
    WS_SECURITY_CONSTRAINTS._fields_ = [
        ('securityPropertyConstraints', POINTER(win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTY_CONSTRAINT_head)),
        ('securityPropertyConstraintCount', UInt32),
        ('securityBindingConstraints', POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT_head))),
        ('securityBindingConstraintCount', UInt32),
    ]
    return WS_SECURITY_CONSTRAINTS
def _define_WS_SECURITY_CONTEXT_head():
    class WS_SECURITY_CONTEXT(Structure):
        pass
    return WS_SECURITY_CONTEXT
def _define_WS_SECURITY_CONTEXT():
    WS_SECURITY_CONTEXT = win32more.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_head
    return WS_SECURITY_CONTEXT
def _define_WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_head():
    class WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING(Structure):
        pass
    return WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING
def _define_WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING():
    WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING = win32more.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_head
    WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING._fields_ = [
        ('binding', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING),
        ('bindingUsage', win32more.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE),
        ('bootstrapSecurityDescription', POINTER(win32more.Networking.WindowsWebServices.WS_SECURITY_DESCRIPTION_head)),
    ]
    return WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING
def _define_WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_CONSTRAINT_head():
    class WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_CONSTRAINT(Structure):
        pass
    return WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_CONSTRAINT
def _define_WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_CONSTRAINT():
    WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_CONSTRAINT = win32more.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_CONSTRAINT_head
    WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_CONSTRAINT._fields_ = [
        ('bindingConstraint', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT),
        ('bindingUsage', win32more.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE),
        ('bootstrapSecurityConstraint', POINTER(win32more.Networking.WindowsWebServices.WS_SECURITY_CONSTRAINTS_head)),
    ]
    return WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_CONSTRAINT
def _define_WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION_head():
    class WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION(Structure):
        pass
    return WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION
def _define_WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION():
    WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION_head
    WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION._fields_ = [
        ('securityBindingProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES),
        ('bindingUsage', win32more.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE),
    ]
    return WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION
def _define_WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_TEMPLATE_head():
    class WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_TEMPLATE(Structure):
        pass
    return WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_TEMPLATE
def _define_WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_TEMPLATE():
    WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_TEMPLATE = win32more.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_TEMPLATE_head
    WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_TEMPLATE._fields_ = [
        ('securityBindingProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES),
    ]
    return WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_TEMPLATE
def _define_WS_SECURITY_CONTEXT_PROPERTY_head():
    class WS_SECURITY_CONTEXT_PROPERTY(Structure):
        pass
    return WS_SECURITY_CONTEXT_PROPERTY
def _define_WS_SECURITY_CONTEXT_PROPERTY():
    WS_SECURITY_CONTEXT_PROPERTY = win32more.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_PROPERTY_head
    WS_SECURITY_CONTEXT_PROPERTY._fields_ = [
        ('id', win32more.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_PROPERTY_ID),
        ('value', c_void_p),
        ('valueSize', UInt32),
    ]
    return WS_SECURITY_CONTEXT_PROPERTY
WS_SECURITY_CONTEXT_PROPERTY_ID = Int32
WS_SECURITY_CONTEXT_PROPERTY_IDENTIFIER = 1
WS_SECURITY_CONTEXT_PROPERTY_USERNAME = 2
WS_SECURITY_CONTEXT_PROPERTY_MESSAGE_SECURITY_WINDOWS_TOKEN = 3
WS_SECURITY_CONTEXT_PROPERTY_SAML_ASSERTION = 4
def _define_WS_SECURITY_CONTEXT_SECURITY_BINDING_POLICY_DESCRIPTION_head():
    class WS_SECURITY_CONTEXT_SECURITY_BINDING_POLICY_DESCRIPTION(Structure):
        pass
    return WS_SECURITY_CONTEXT_SECURITY_BINDING_POLICY_DESCRIPTION
def _define_WS_SECURITY_CONTEXT_SECURITY_BINDING_POLICY_DESCRIPTION():
    WS_SECURITY_CONTEXT_SECURITY_BINDING_POLICY_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_SECURITY_BINDING_POLICY_DESCRIPTION_head
    WS_SECURITY_CONTEXT_SECURITY_BINDING_POLICY_DESCRIPTION._fields_ = [
        ('securityContextMessageSecurityBinding', win32more.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION),
        ('securityProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES),
    ]
    return WS_SECURITY_CONTEXT_SECURITY_BINDING_POLICY_DESCRIPTION
def _define_WS_SECURITY_CONTEXT_SECURITY_BINDING_TEMPLATE_head():
    class WS_SECURITY_CONTEXT_SECURITY_BINDING_TEMPLATE(Structure):
        pass
    return WS_SECURITY_CONTEXT_SECURITY_BINDING_TEMPLATE
def _define_WS_SECURITY_CONTEXT_SECURITY_BINDING_TEMPLATE():
    WS_SECURITY_CONTEXT_SECURITY_BINDING_TEMPLATE = win32more.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_SECURITY_BINDING_TEMPLATE_head
    WS_SECURITY_CONTEXT_SECURITY_BINDING_TEMPLATE._fields_ = [
        ('securityContextMessageSecurityBinding', win32more.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_TEMPLATE),
        ('securityProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES),
    ]
    return WS_SECURITY_CONTEXT_SECURITY_BINDING_TEMPLATE
def _define_WS_SECURITY_DESCRIPTION_head():
    class WS_SECURITY_DESCRIPTION(Structure):
        pass
    return WS_SECURITY_DESCRIPTION
def _define_WS_SECURITY_DESCRIPTION():
    WS_SECURITY_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_SECURITY_DESCRIPTION_head
    WS_SECURITY_DESCRIPTION._fields_ = [
        ('securityBindings', POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_head))),
        ('securityBindingCount', UInt32),
        ('properties', POINTER(win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTY_head)),
        ('propertyCount', UInt32),
    ]
    return WS_SECURITY_DESCRIPTION
WS_SECURITY_HEADER_LAYOUT = Int32
WS_SECURITY_HEADER_LAYOUT_STRICT = 1
WS_SECURITY_HEADER_LAYOUT_LAX = 2
WS_SECURITY_HEADER_LAYOUT_LAX_WITH_TIMESTAMP_FIRST = 3
WS_SECURITY_HEADER_LAYOUT_LAX_WITH_TIMESTAMP_LAST = 4
WS_SECURITY_HEADER_VERSION = Int32
WS_SECURITY_HEADER_VERSION_1_0 = 1
WS_SECURITY_HEADER_VERSION_1_1 = 2
WS_SECURITY_KEY_ENTROPY_MODE = Int32
WS_SECURITY_KEY_ENTROPY_MODE_CLIENT_ONLY = 1
WS_SECURITY_KEY_ENTROPY_MODE_SERVER_ONLY = 2
WS_SECURITY_KEY_ENTROPY_MODE_COMBINED = 3
def _define_WS_SECURITY_KEY_HANDLE_head():
    class WS_SECURITY_KEY_HANDLE(Structure):
        pass
    return WS_SECURITY_KEY_HANDLE
def _define_WS_SECURITY_KEY_HANDLE():
    WS_SECURITY_KEY_HANDLE = win32more.Networking.WindowsWebServices.WS_SECURITY_KEY_HANDLE_head
    WS_SECURITY_KEY_HANDLE._fields_ = [
        ('keyHandleType', win32more.Networking.WindowsWebServices.WS_SECURITY_KEY_HANDLE_TYPE),
    ]
    return WS_SECURITY_KEY_HANDLE
WS_SECURITY_KEY_HANDLE_TYPE = Int32
WS_RAW_SYMMETRIC_SECURITY_KEY_HANDLE_TYPE = 1
WS_NCRYPT_ASYMMETRIC_SECURITY_KEY_HANDLE_TYPE = 2
WS_CAPI_ASYMMETRIC_SECURITY_KEY_HANDLE_TYPE = 3
WS_SECURITY_KEY_TYPE = Int32
WS_SECURITY_KEY_TYPE_NONE = 1
WS_SECURITY_KEY_TYPE_SYMMETRIC = 2
WS_SECURITY_KEY_TYPE_ASYMMETRIC = 3
def _define_WS_SECURITY_PROPERTIES_head():
    class WS_SECURITY_PROPERTIES(Structure):
        pass
    return WS_SECURITY_PROPERTIES
def _define_WS_SECURITY_PROPERTIES():
    WS_SECURITY_PROPERTIES = win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES_head
    WS_SECURITY_PROPERTIES._fields_ = [
        ('properties', POINTER(win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTY_head)),
        ('propertyCount', UInt32),
    ]
    return WS_SECURITY_PROPERTIES
def _define_WS_SECURITY_PROPERTY_head():
    class WS_SECURITY_PROPERTY(Structure):
        pass
    return WS_SECURITY_PROPERTY
def _define_WS_SECURITY_PROPERTY():
    WS_SECURITY_PROPERTY = win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTY_head
    WS_SECURITY_PROPERTY._fields_ = [
        ('id', win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTY_ID),
        ('value', c_void_p),
        ('valueSize', UInt32),
    ]
    return WS_SECURITY_PROPERTY
def _define_WS_SECURITY_PROPERTY_CONSTRAINT_head():
    class WS_SECURITY_PROPERTY_CONSTRAINT(Structure):
        pass
    return WS_SECURITY_PROPERTY_CONSTRAINT
def _define_WS_SECURITY_PROPERTY_CONSTRAINT():
    WS_SECURITY_PROPERTY_CONSTRAINT = win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTY_CONSTRAINT_head
    class WS_SECURITY_PROPERTY_CONSTRAINT__out_e__Struct(Structure):
        pass
    WS_SECURITY_PROPERTY_CONSTRAINT__out_e__Struct._fields_ = [
        ('securityProperty', win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTY),
    ]
    WS_SECURITY_PROPERTY_CONSTRAINT._fields_ = [
        ('id', win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTY_ID),
        ('allowedValues', c_void_p),
        ('allowedValuesSize', UInt32),
        ('out', WS_SECURITY_PROPERTY_CONSTRAINT__out_e__Struct),
    ]
    return WS_SECURITY_PROPERTY_CONSTRAINT
WS_SECURITY_PROPERTY_ID = Int32
WS_SECURITY_PROPERTY_TRANSPORT_PROTECTION_LEVEL = 1
WS_SECURITY_PROPERTY_ALGORITHM_SUITE = 2
WS_SECURITY_PROPERTY_ALGORITHM_SUITE_NAME = 3
WS_SECURITY_PROPERTY_MAX_ALLOWED_LATENCY = 4
WS_SECURITY_PROPERTY_TIMESTAMP_VALIDITY_DURATION = 5
WS_SECURITY_PROPERTY_MAX_ALLOWED_CLOCK_SKEW = 6
WS_SECURITY_PROPERTY_TIMESTAMP_USAGE = 7
WS_SECURITY_PROPERTY_SECURITY_HEADER_LAYOUT = 8
WS_SECURITY_PROPERTY_SECURITY_HEADER_VERSION = 9
WS_SECURITY_PROPERTY_EXTENDED_PROTECTION_POLICY = 10
WS_SECURITY_PROPERTY_EXTENDED_PROTECTION_SCENARIO = 11
WS_SECURITY_PROPERTY_SERVICE_IDENTITIES = 12
WS_SECURITY_TIMESTAMP_USAGE = Int32
WS_SECURITY_TIMESTAMP_USAGE_ALWAYS = 1
WS_SECURITY_TIMESTAMP_USAGE_NEVER = 2
WS_SECURITY_TIMESTAMP_USAGE_REQUESTS_ONLY = 3
def _define_WS_SECURITY_TOKEN_head():
    class WS_SECURITY_TOKEN(Structure):
        pass
    return WS_SECURITY_TOKEN
def _define_WS_SECURITY_TOKEN():
    WS_SECURITY_TOKEN = win32more.Networking.WindowsWebServices.WS_SECURITY_TOKEN_head
    return WS_SECURITY_TOKEN
WS_SECURITY_TOKEN_PROPERTY_ID = Int32
WS_SECURITY_TOKEN_PROPERTY_KEY_TYPE = 1
WS_SECURITY_TOKEN_PROPERTY_VALID_FROM_TIME = 2
WS_SECURITY_TOKEN_PROPERTY_VALID_TILL_TIME = 3
WS_SECURITY_TOKEN_PROPERTY_SERIALIZED_XML = 4
WS_SECURITY_TOKEN_PROPERTY_ATTACHED_REFERENCE_XML = 5
WS_SECURITY_TOKEN_PROPERTY_UNATTACHED_REFERENCE_XML = 6
WS_SECURITY_TOKEN_PROPERTY_SYMMETRIC_KEY = 7
WS_SECURITY_TOKEN_REFERENCE_MODE = Int32
WS_SECURITY_TOKEN_REFERENCE_MODE_LOCAL_ID = 1
WS_SECURITY_TOKEN_REFERENCE_MODE_XML_BUFFER = 2
WS_SECURITY_TOKEN_REFERENCE_MODE_CERT_THUMBPRINT = 3
WS_SECURITY_TOKEN_REFERENCE_MODE_SECURITY_CONTEXT_ID = 4
WS_SECURITY_TOKEN_REFERENCE_MODE_SAML_ASSERTION_ID = 5
def _define_WS_SERVICE_ACCEPT_CHANNEL_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_OPERATION_CONTEXT_head),POINTER(c_void_p),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
WS_SERVICE_CANCEL_REASON = Int32
WS_SERVICE_HOST_ABORT = 0
WS_SERVICE_CHANNEL_FAULTED = 1
def _define_WS_SERVICE_CLOSE_CHANNEL_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_OPERATION_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head))
def _define_WS_SERVICE_CONTRACT_head():
    class WS_SERVICE_CONTRACT(Structure):
        pass
    return WS_SERVICE_CONTRACT
def _define_WS_SERVICE_CONTRACT():
    WS_SERVICE_CONTRACT = win32more.Networking.WindowsWebServices.WS_SERVICE_CONTRACT_head
    WS_SERVICE_CONTRACT._fields_ = [
        ('contractDescription', POINTER(win32more.Networking.WindowsWebServices.WS_CONTRACT_DESCRIPTION_head)),
        ('defaultMessageHandlerCallback', win32more.Networking.WindowsWebServices.WS_SERVICE_MESSAGE_RECEIVE_CALLBACK),
        ('methodTable', c_void_p),
    ]
    return WS_SERVICE_CONTRACT
def _define_WS_SERVICE_ENDPOINT_head():
    class WS_SERVICE_ENDPOINT(Structure):
        pass
    return WS_SERVICE_ENDPOINT
def _define_WS_SERVICE_ENDPOINT():
    WS_SERVICE_ENDPOINT = win32more.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT_head
    WS_SERVICE_ENDPOINT._fields_ = [
        ('address', win32more.Networking.WindowsWebServices.WS_ENDPOINT_ADDRESS),
        ('channelBinding', win32more.Networking.WindowsWebServices.WS_CHANNEL_BINDING),
        ('channelType', win32more.Networking.WindowsWebServices.WS_CHANNEL_TYPE),
        ('securityDescription', POINTER(win32more.Networking.WindowsWebServices.WS_SECURITY_DESCRIPTION_head)),
        ('contract', POINTER(win32more.Networking.WindowsWebServices.WS_SERVICE_CONTRACT_head)),
        ('authorizationCallback', win32more.Networking.WindowsWebServices.WS_SERVICE_SECURITY_CALLBACK),
        ('properties', POINTER(win32more.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT_PROPERTY_head)),
        ('propertyCount', UInt32),
        ('channelProperties', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES),
    ]
    return WS_SERVICE_ENDPOINT
def _define_WS_SERVICE_ENDPOINT_METADATA_head():
    class WS_SERVICE_ENDPOINT_METADATA(Structure):
        pass
    return WS_SERVICE_ENDPOINT_METADATA
def _define_WS_SERVICE_ENDPOINT_METADATA():
    WS_SERVICE_ENDPOINT_METADATA = win32more.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT_METADATA_head
    WS_SERVICE_ENDPOINT_METADATA._fields_ = [
        ('portName', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('bindingName', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('bindingNs', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
    ]
    return WS_SERVICE_ENDPOINT_METADATA
def _define_WS_SERVICE_ENDPOINT_PROPERTY_head():
    class WS_SERVICE_ENDPOINT_PROPERTY(Structure):
        pass
    return WS_SERVICE_ENDPOINT_PROPERTY
def _define_WS_SERVICE_ENDPOINT_PROPERTY():
    WS_SERVICE_ENDPOINT_PROPERTY = win32more.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT_PROPERTY_head
    WS_SERVICE_ENDPOINT_PROPERTY._fields_ = [
        ('id', win32more.Networking.WindowsWebServices.WS_SERVICE_ENDPOINT_PROPERTY_ID),
        ('value', c_void_p),
        ('valueSize', UInt32),
    ]
    return WS_SERVICE_ENDPOINT_PROPERTY
WS_SERVICE_ENDPOINT_PROPERTY_ID = Int32
WS_SERVICE_ENDPOINT_PROPERTY_ACCEPT_CHANNEL_CALLBACK = 0
WS_SERVICE_ENDPOINT_PROPERTY_CLOSE_CHANNEL_CALLBACK = 1
WS_SERVICE_ENDPOINT_PROPERTY_MAX_ACCEPTING_CHANNELS = 2
WS_SERVICE_ENDPOINT_PROPERTY_MAX_CONCURRENCY = 3
WS_SERVICE_ENDPOINT_PROPERTY_BODY_HEAP_MAX_SIZE = 4
WS_SERVICE_ENDPOINT_PROPERTY_BODY_HEAP_TRIM_SIZE = 5
WS_SERVICE_ENDPOINT_PROPERTY_MESSAGE_PROPERTIES = 6
WS_SERVICE_ENDPOINT_PROPERTY_MAX_CALL_POOL_SIZE = 7
WS_SERVICE_ENDPOINT_PROPERTY_MAX_CHANNEL_POOL_SIZE = 8
WS_SERVICE_ENDPOINT_PROPERTY_LISTENER_PROPERTIES = 9
WS_SERVICE_ENDPOINT_PROPERTY_CHECK_MUST_UNDERSTAND = 10
WS_SERVICE_ENDPOINT_PROPERTY_METADATA_EXCHANGE_TYPE = 11
WS_SERVICE_ENDPOINT_PROPERTY_METADATA = 12
WS_SERVICE_ENDPOINT_PROPERTY_METADATA_EXCHANGE_URL_SUFFIX = 13
WS_SERVICE_ENDPOINT_PROPERTY_MAX_CHANNELS = 14
def _define_WS_SERVICE_HOST_head():
    class WS_SERVICE_HOST(Structure):
        pass
    return WS_SERVICE_HOST
def _define_WS_SERVICE_HOST():
    WS_SERVICE_HOST = win32more.Networking.WindowsWebServices.WS_SERVICE_HOST_head
    return WS_SERVICE_HOST
WS_SERVICE_HOST_STATE = Int32
WS_SERVICE_HOST_STATE_CREATED = 0
WS_SERVICE_HOST_STATE_OPENING = 1
WS_SERVICE_HOST_STATE_OPEN = 2
WS_SERVICE_HOST_STATE_CLOSING = 3
WS_SERVICE_HOST_STATE_CLOSED = 4
WS_SERVICE_HOST_STATE_FAULTED = 5
def _define_WS_SERVICE_MESSAGE_RECEIVE_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_OPERATION_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_SERVICE_METADATA_head():
    class WS_SERVICE_METADATA(Structure):
        pass
    return WS_SERVICE_METADATA
def _define_WS_SERVICE_METADATA():
    WS_SERVICE_METADATA = win32more.Networking.WindowsWebServices.WS_SERVICE_METADATA_head
    WS_SERVICE_METADATA._fields_ = [
        ('documentCount', UInt32),
        ('documents', POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_SERVICE_METADATA_DOCUMENT_head))),
        ('serviceName', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('serviceNs', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
    ]
    return WS_SERVICE_METADATA
def _define_WS_SERVICE_METADATA_DOCUMENT_head():
    class WS_SERVICE_METADATA_DOCUMENT(Structure):
        pass
    return WS_SERVICE_METADATA_DOCUMENT
def _define_WS_SERVICE_METADATA_DOCUMENT():
    WS_SERVICE_METADATA_DOCUMENT = win32more.Networking.WindowsWebServices.WS_SERVICE_METADATA_DOCUMENT_head
    WS_SERVICE_METADATA_DOCUMENT._fields_ = [
        ('content', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('name', POINTER(win32more.Networking.WindowsWebServices.WS_STRING_head)),
    ]
    return WS_SERVICE_METADATA_DOCUMENT
def _define_WS_SERVICE_PROPERTY_head():
    class WS_SERVICE_PROPERTY(Structure):
        pass
    return WS_SERVICE_PROPERTY
def _define_WS_SERVICE_PROPERTY():
    WS_SERVICE_PROPERTY = win32more.Networking.WindowsWebServices.WS_SERVICE_PROPERTY_head
    WS_SERVICE_PROPERTY._fields_ = [
        ('id', win32more.Networking.WindowsWebServices.WS_SERVICE_PROPERTY_ID),
        ('value', c_void_p),
        ('valueSize', UInt32),
    ]
    return WS_SERVICE_PROPERTY
def _define_WS_SERVICE_PROPERTY_ACCEPT_CALLBACK_head():
    class WS_SERVICE_PROPERTY_ACCEPT_CALLBACK(Structure):
        pass
    return WS_SERVICE_PROPERTY_ACCEPT_CALLBACK
def _define_WS_SERVICE_PROPERTY_ACCEPT_CALLBACK():
    WS_SERVICE_PROPERTY_ACCEPT_CALLBACK = win32more.Networking.WindowsWebServices.WS_SERVICE_PROPERTY_ACCEPT_CALLBACK_head
    WS_SERVICE_PROPERTY_ACCEPT_CALLBACK._fields_ = [
        ('callback', win32more.Networking.WindowsWebServices.WS_SERVICE_ACCEPT_CHANNEL_CALLBACK),
    ]
    return WS_SERVICE_PROPERTY_ACCEPT_CALLBACK
def _define_WS_SERVICE_PROPERTY_CLOSE_CALLBACK_head():
    class WS_SERVICE_PROPERTY_CLOSE_CALLBACK(Structure):
        pass
    return WS_SERVICE_PROPERTY_CLOSE_CALLBACK
def _define_WS_SERVICE_PROPERTY_CLOSE_CALLBACK():
    WS_SERVICE_PROPERTY_CLOSE_CALLBACK = win32more.Networking.WindowsWebServices.WS_SERVICE_PROPERTY_CLOSE_CALLBACK_head
    WS_SERVICE_PROPERTY_CLOSE_CALLBACK._fields_ = [
        ('callback', win32more.Networking.WindowsWebServices.WS_SERVICE_CLOSE_CHANNEL_CALLBACK),
    ]
    return WS_SERVICE_PROPERTY_CLOSE_CALLBACK
WS_SERVICE_PROPERTY_ID = Int32
WS_SERVICE_PROPERTY_HOST_USER_STATE = 0
WS_SERVICE_PROPERTY_FAULT_DISCLOSURE = 1
WS_SERVICE_PROPERTY_FAULT_LANGID = 2
WS_SERVICE_PROPERTY_HOST_STATE = 3
WS_SERVICE_PROPERTY_METADATA = 4
WS_SERVICE_PROPERTY_CLOSE_TIMEOUT = 5
def _define_WS_SERVICE_PROXY_head():
    class WS_SERVICE_PROXY(Structure):
        pass
    return WS_SERVICE_PROXY
def _define_WS_SERVICE_PROXY():
    WS_SERVICE_PROXY = win32more.Networking.WindowsWebServices.WS_SERVICE_PROXY_head
    return WS_SERVICE_PROXY
WS_SERVICE_PROXY_STATE = Int32
WS_SERVICE_PROXY_STATE_CREATED = 0
WS_SERVICE_PROXY_STATE_OPENING = 1
WS_SERVICE_PROXY_STATE_OPEN = 2
WS_SERVICE_PROXY_STATE_CLOSING = 3
WS_SERVICE_PROXY_STATE_CLOSED = 4
WS_SERVICE_PROXY_STATE_FAULTED = 5
def _define_WS_SERVICE_SECURITY_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_OPERATION_CONTEXT_head),POINTER(win32more.Foundation.BOOL),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_SERVICE_SECURITY_IDENTITIES_head():
    class WS_SERVICE_SECURITY_IDENTITIES(Structure):
        pass
    return WS_SERVICE_SECURITY_IDENTITIES
def _define_WS_SERVICE_SECURITY_IDENTITIES():
    WS_SERVICE_SECURITY_IDENTITIES = win32more.Networking.WindowsWebServices.WS_SERVICE_SECURITY_IDENTITIES_head
    WS_SERVICE_SECURITY_IDENTITIES._fields_ = [
        ('serviceIdentities', POINTER(win32more.Networking.WindowsWebServices.WS_STRING_head)),
        ('serviceIdentityCount', UInt32),
    ]
    return WS_SERVICE_SECURITY_IDENTITIES
def _define_WS_SERVICE_STUB_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_OPERATION_CONTEXT_head),c_void_p,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_SET_CHANNEL_PROPERTY_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTY_ID,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_SET_LISTENER_PROPERTY_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,win32more.Networking.WindowsWebServices.WS_LISTENER_PROPERTY_ID,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_SHUTDOWN_SESSION_CHANNEL_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_SOAPUDP_URL_head():
    class WS_SOAPUDP_URL(Structure):
        pass
    return WS_SOAPUDP_URL
def _define_WS_SOAPUDP_URL():
    WS_SOAPUDP_URL = win32more.Networking.WindowsWebServices.WS_SOAPUDP_URL_head
    WS_SOAPUDP_URL._fields_ = [
        ('url', win32more.Networking.WindowsWebServices.WS_URL),
        ('host', win32more.Networking.WindowsWebServices.WS_STRING),
        ('port', UInt16),
        ('portAsString', win32more.Networking.WindowsWebServices.WS_STRING),
        ('path', win32more.Networking.WindowsWebServices.WS_STRING),
        ('query', win32more.Networking.WindowsWebServices.WS_STRING),
        ('fragment', win32more.Networking.WindowsWebServices.WS_STRING),
    ]
    return WS_SOAPUDP_URL
def _define_WS_SPN_ENDPOINT_IDENTITY_head():
    class WS_SPN_ENDPOINT_IDENTITY(Structure):
        pass
    return WS_SPN_ENDPOINT_IDENTITY
def _define_WS_SPN_ENDPOINT_IDENTITY():
    WS_SPN_ENDPOINT_IDENTITY = win32more.Networking.WindowsWebServices.WS_SPN_ENDPOINT_IDENTITY_head
    WS_SPN_ENDPOINT_IDENTITY._fields_ = [
        ('identity', win32more.Networking.WindowsWebServices.WS_ENDPOINT_IDENTITY),
        ('spn', win32more.Networking.WindowsWebServices.WS_STRING),
    ]
    return WS_SPN_ENDPOINT_IDENTITY
def _define_WS_SSL_TRANSPORT_SECURITY_BINDING_head():
    class WS_SSL_TRANSPORT_SECURITY_BINDING(Structure):
        pass
    return WS_SSL_TRANSPORT_SECURITY_BINDING
def _define_WS_SSL_TRANSPORT_SECURITY_BINDING():
    WS_SSL_TRANSPORT_SECURITY_BINDING = win32more.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_head
    WS_SSL_TRANSPORT_SECURITY_BINDING._fields_ = [
        ('binding', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING),
        ('localCertCredential', POINTER(win32more.Networking.WindowsWebServices.WS_CERT_CREDENTIAL_head)),
    ]
    return WS_SSL_TRANSPORT_SECURITY_BINDING
def _define_WS_SSL_TRANSPORT_SECURITY_BINDING_CONSTRAINT_head():
    class WS_SSL_TRANSPORT_SECURITY_BINDING_CONSTRAINT(Structure):
        pass
    return WS_SSL_TRANSPORT_SECURITY_BINDING_CONSTRAINT
def _define_WS_SSL_TRANSPORT_SECURITY_BINDING_CONSTRAINT():
    WS_SSL_TRANSPORT_SECURITY_BINDING_CONSTRAINT = win32more.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_CONSTRAINT_head
    class WS_SSL_TRANSPORT_SECURITY_BINDING_CONSTRAINT__out_e__Struct(Structure):
        pass
    WS_SSL_TRANSPORT_SECURITY_BINDING_CONSTRAINT__out_e__Struct._fields_ = [
        ('clientCertCredentialRequired', win32more.Foundation.BOOL),
    ]
    WS_SSL_TRANSPORT_SECURITY_BINDING_CONSTRAINT._fields_ = [
        ('bindingConstraint', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT),
        ('out', WS_SSL_TRANSPORT_SECURITY_BINDING_CONSTRAINT__out_e__Struct),
    ]
    return WS_SSL_TRANSPORT_SECURITY_BINDING_CONSTRAINT
def _define_WS_SSL_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION_head():
    class WS_SSL_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION(Structure):
        pass
    return WS_SSL_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION
def _define_WS_SSL_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION():
    WS_SSL_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION_head
    WS_SSL_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION._fields_ = [
        ('securityBindingProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES),
    ]
    return WS_SSL_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION
def _define_WS_SSL_TRANSPORT_SECURITY_BINDING_TEMPLATE_head():
    class WS_SSL_TRANSPORT_SECURITY_BINDING_TEMPLATE(Structure):
        pass
    return WS_SSL_TRANSPORT_SECURITY_BINDING_TEMPLATE
def _define_WS_SSL_TRANSPORT_SECURITY_BINDING_TEMPLATE():
    WS_SSL_TRANSPORT_SECURITY_BINDING_TEMPLATE = win32more.Networking.WindowsWebServices.WS_SSL_TRANSPORT_SECURITY_BINDING_TEMPLATE_head
    WS_SSL_TRANSPORT_SECURITY_BINDING_TEMPLATE._fields_ = [
        ('securityBindingProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES),
        ('localCertCredential', POINTER(win32more.Networking.WindowsWebServices.WS_CERT_CREDENTIAL_head)),
    ]
    return WS_SSL_TRANSPORT_SECURITY_BINDING_TEMPLATE
def _define_WS_SSPI_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION_head():
    class WS_SSPI_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION(Structure):
        pass
    return WS_SSPI_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION
def _define_WS_SSPI_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION():
    WS_SSPI_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_SSPI_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION_head
    WS_SSPI_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION._fields_ = [
        ('securityBindingProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES),
    ]
    return WS_SSPI_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION
def _define_WS_STRING_head():
    class WS_STRING(Structure):
        pass
    return WS_STRING
def _define_WS_STRING():
    WS_STRING = win32more.Networking.WindowsWebServices.WS_STRING_head
    WS_STRING._fields_ = [
        ('length', UInt32),
        ('chars', win32more.Foundation.PWSTR),
    ]
    return WS_STRING
def _define_WS_STRING_DESCRIPTION_head():
    class WS_STRING_DESCRIPTION(Structure):
        pass
    return WS_STRING_DESCRIPTION
def _define_WS_STRING_DESCRIPTION():
    WS_STRING_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_STRING_DESCRIPTION_head
    WS_STRING_DESCRIPTION._fields_ = [
        ('minCharCount', UInt32),
        ('maxCharCount', UInt32),
    ]
    return WS_STRING_DESCRIPTION
def _define_WS_STRING_USERNAME_CREDENTIAL_head():
    class WS_STRING_USERNAME_CREDENTIAL(Structure):
        pass
    return WS_STRING_USERNAME_CREDENTIAL
def _define_WS_STRING_USERNAME_CREDENTIAL():
    WS_STRING_USERNAME_CREDENTIAL = win32more.Networking.WindowsWebServices.WS_STRING_USERNAME_CREDENTIAL_head
    WS_STRING_USERNAME_CREDENTIAL._fields_ = [
        ('credential', win32more.Networking.WindowsWebServices.WS_USERNAME_CREDENTIAL),
        ('username', win32more.Networking.WindowsWebServices.WS_STRING),
        ('password', win32more.Networking.WindowsWebServices.WS_STRING),
    ]
    return WS_STRING_USERNAME_CREDENTIAL
def _define_WS_STRING_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_head():
    class WS_STRING_WINDOWS_INTEGRATED_AUTH_CREDENTIAL(Structure):
        pass
    return WS_STRING_WINDOWS_INTEGRATED_AUTH_CREDENTIAL
def _define_WS_STRING_WINDOWS_INTEGRATED_AUTH_CREDENTIAL():
    WS_STRING_WINDOWS_INTEGRATED_AUTH_CREDENTIAL = win32more.Networking.WindowsWebServices.WS_STRING_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_head
    WS_STRING_WINDOWS_INTEGRATED_AUTH_CREDENTIAL._fields_ = [
        ('credential', win32more.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL),
        ('username', win32more.Networking.WindowsWebServices.WS_STRING),
        ('password', win32more.Networking.WindowsWebServices.WS_STRING),
        ('domain', win32more.Networking.WindowsWebServices.WS_STRING),
    ]
    return WS_STRING_WINDOWS_INTEGRATED_AUTH_CREDENTIAL
def _define_WS_STRUCT_DESCRIPTION_head():
    class WS_STRUCT_DESCRIPTION(Structure):
        pass
    return WS_STRUCT_DESCRIPTION
def _define_WS_STRUCT_DESCRIPTION():
    WS_STRUCT_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_STRUCT_DESCRIPTION_head
    WS_STRUCT_DESCRIPTION._fields_ = [
        ('size', UInt32),
        ('alignment', UInt32),
        ('fields', POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_FIELD_DESCRIPTION_head))),
        ('fieldCount', UInt32),
        ('typeLocalName', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('typeNs', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('parentType', POINTER(win32more.Networking.WindowsWebServices.WS_STRUCT_DESCRIPTION_head)),
        ('subTypes', POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_STRUCT_DESCRIPTION_head))),
        ('subTypeCount', UInt32),
        ('structOptions', UInt32),
    ]
    return WS_STRUCT_DESCRIPTION
def _define_WS_SUBJECT_NAME_CERT_CREDENTIAL_head():
    class WS_SUBJECT_NAME_CERT_CREDENTIAL(Structure):
        pass
    return WS_SUBJECT_NAME_CERT_CREDENTIAL
def _define_WS_SUBJECT_NAME_CERT_CREDENTIAL():
    WS_SUBJECT_NAME_CERT_CREDENTIAL = win32more.Networking.WindowsWebServices.WS_SUBJECT_NAME_CERT_CREDENTIAL_head
    WS_SUBJECT_NAME_CERT_CREDENTIAL._fields_ = [
        ('credential', win32more.Networking.WindowsWebServices.WS_CERT_CREDENTIAL),
        ('storeLocation', UInt32),
        ('storeName', win32more.Networking.WindowsWebServices.WS_STRING),
        ('subjectName', win32more.Networking.WindowsWebServices.WS_STRING),
    ]
    return WS_SUBJECT_NAME_CERT_CREDENTIAL
def _define_WS_TCP_BINDING_TEMPLATE_head():
    class WS_TCP_BINDING_TEMPLATE(Structure):
        pass
    return WS_TCP_BINDING_TEMPLATE
def _define_WS_TCP_BINDING_TEMPLATE():
    WS_TCP_BINDING_TEMPLATE = win32more.Networking.WindowsWebServices.WS_TCP_BINDING_TEMPLATE_head
    WS_TCP_BINDING_TEMPLATE._fields_ = [
        ('channelProperties', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES),
    ]
    return WS_TCP_BINDING_TEMPLATE
def _define_WS_TCP_POLICY_DESCRIPTION_head():
    class WS_TCP_POLICY_DESCRIPTION(Structure):
        pass
    return WS_TCP_POLICY_DESCRIPTION
def _define_WS_TCP_POLICY_DESCRIPTION():
    WS_TCP_POLICY_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_TCP_POLICY_DESCRIPTION_head
    WS_TCP_POLICY_DESCRIPTION._fields_ = [
        ('channelProperties', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES),
    ]
    return WS_TCP_POLICY_DESCRIPTION
def _define_WS_TCP_SSPI_BINDING_TEMPLATE_head():
    class WS_TCP_SSPI_BINDING_TEMPLATE(Structure):
        pass
    return WS_TCP_SSPI_BINDING_TEMPLATE
def _define_WS_TCP_SSPI_BINDING_TEMPLATE():
    WS_TCP_SSPI_BINDING_TEMPLATE = win32more.Networking.WindowsWebServices.WS_TCP_SSPI_BINDING_TEMPLATE_head
    WS_TCP_SSPI_BINDING_TEMPLATE._fields_ = [
        ('channelProperties', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES),
        ('securityProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES),
        ('sspiTransportSecurityBinding', win32more.Networking.WindowsWebServices.WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_TEMPLATE),
    ]
    return WS_TCP_SSPI_BINDING_TEMPLATE
def _define_WS_TCP_SSPI_KERBEROS_APREQ_BINDING_TEMPLATE_head():
    class WS_TCP_SSPI_KERBEROS_APREQ_BINDING_TEMPLATE(Structure):
        pass
    return WS_TCP_SSPI_KERBEROS_APREQ_BINDING_TEMPLATE
def _define_WS_TCP_SSPI_KERBEROS_APREQ_BINDING_TEMPLATE():
    WS_TCP_SSPI_KERBEROS_APREQ_BINDING_TEMPLATE = win32more.Networking.WindowsWebServices.WS_TCP_SSPI_KERBEROS_APREQ_BINDING_TEMPLATE_head
    WS_TCP_SSPI_KERBEROS_APREQ_BINDING_TEMPLATE._fields_ = [
        ('channelProperties', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES),
        ('securityProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES),
        ('sspiTransportSecurityBinding', win32more.Networking.WindowsWebServices.WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_TEMPLATE),
        ('kerberosApreqMessageSecurityBinding', win32more.Networking.WindowsWebServices.WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_TEMPLATE),
    ]
    return WS_TCP_SSPI_KERBEROS_APREQ_BINDING_TEMPLATE
def _define_WS_TCP_SSPI_KERBEROS_APREQ_POLICY_DESCRIPTION_head():
    class WS_TCP_SSPI_KERBEROS_APREQ_POLICY_DESCRIPTION(Structure):
        pass
    return WS_TCP_SSPI_KERBEROS_APREQ_POLICY_DESCRIPTION
def _define_WS_TCP_SSPI_KERBEROS_APREQ_POLICY_DESCRIPTION():
    WS_TCP_SSPI_KERBEROS_APREQ_POLICY_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_TCP_SSPI_KERBEROS_APREQ_POLICY_DESCRIPTION_head
    WS_TCP_SSPI_KERBEROS_APREQ_POLICY_DESCRIPTION._fields_ = [
        ('channelProperties', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES),
        ('securityProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES),
        ('sspiTransportSecurityBinding', win32more.Networking.WindowsWebServices.WS_SSPI_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION),
        ('kerberosApreqMessageSecurityBinding', win32more.Networking.WindowsWebServices.WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION),
    ]
    return WS_TCP_SSPI_KERBEROS_APREQ_POLICY_DESCRIPTION
def _define_WS_TCP_SSPI_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE_head():
    class WS_TCP_SSPI_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE(Structure):
        pass
    return WS_TCP_SSPI_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE
def _define_WS_TCP_SSPI_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE():
    WS_TCP_SSPI_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE = win32more.Networking.WindowsWebServices.WS_TCP_SSPI_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE_head
    WS_TCP_SSPI_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE._fields_ = [
        ('channelProperties', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES),
        ('securityProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES),
        ('sspiTransportSecurityBinding', win32more.Networking.WindowsWebServices.WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_TEMPLATE),
        ('kerberosApreqMessageSecurityBinding', win32more.Networking.WindowsWebServices.WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_TEMPLATE),
        ('securityContextSecurityBinding', win32more.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_SECURITY_BINDING_TEMPLATE),
    ]
    return WS_TCP_SSPI_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE
def _define_WS_TCP_SSPI_KERBEROS_APREQ_SECURITY_CONTEXT_POLICY_DESCRIPTION_head():
    class WS_TCP_SSPI_KERBEROS_APREQ_SECURITY_CONTEXT_POLICY_DESCRIPTION(Structure):
        pass
    return WS_TCP_SSPI_KERBEROS_APREQ_SECURITY_CONTEXT_POLICY_DESCRIPTION
def _define_WS_TCP_SSPI_KERBEROS_APREQ_SECURITY_CONTEXT_POLICY_DESCRIPTION():
    WS_TCP_SSPI_KERBEROS_APREQ_SECURITY_CONTEXT_POLICY_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_TCP_SSPI_KERBEROS_APREQ_SECURITY_CONTEXT_POLICY_DESCRIPTION_head
    WS_TCP_SSPI_KERBEROS_APREQ_SECURITY_CONTEXT_POLICY_DESCRIPTION._fields_ = [
        ('channelProperties', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES),
        ('securityProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES),
        ('sspiTransportSecurityBinding', win32more.Networking.WindowsWebServices.WS_SSPI_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION),
        ('kerberosApreqMessageSecurityBinding', win32more.Networking.WindowsWebServices.WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION),
        ('securityContextSecurityBinding', win32more.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_SECURITY_BINDING_POLICY_DESCRIPTION),
    ]
    return WS_TCP_SSPI_KERBEROS_APREQ_SECURITY_CONTEXT_POLICY_DESCRIPTION
def _define_WS_TCP_SSPI_POLICY_DESCRIPTION_head():
    class WS_TCP_SSPI_POLICY_DESCRIPTION(Structure):
        pass
    return WS_TCP_SSPI_POLICY_DESCRIPTION
def _define_WS_TCP_SSPI_POLICY_DESCRIPTION():
    WS_TCP_SSPI_POLICY_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_TCP_SSPI_POLICY_DESCRIPTION_head
    WS_TCP_SSPI_POLICY_DESCRIPTION._fields_ = [
        ('channelProperties', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES),
        ('securityProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES),
        ('sspiTransportSecurityBinding', win32more.Networking.WindowsWebServices.WS_SSPI_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION),
    ]
    return WS_TCP_SSPI_POLICY_DESCRIPTION
def _define_WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_head():
    class WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING(Structure):
        pass
    return WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING
def _define_WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING():
    WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING = win32more.Networking.WindowsWebServices.WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_head
    WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING._fields_ = [
        ('binding', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING),
        ('clientCredential', POINTER(win32more.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_head)),
    ]
    return WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING
def _define_WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_CONSTRAINT_head():
    class WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_CONSTRAINT(Structure):
        pass
    return WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_CONSTRAINT
def _define_WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_CONSTRAINT():
    WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_CONSTRAINT = win32more.Networking.WindowsWebServices.WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_CONSTRAINT_head
    WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_CONSTRAINT._fields_ = [
        ('bindingConstraint', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT),
    ]
    return WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_CONSTRAINT
def _define_WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_TEMPLATE_head():
    class WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_TEMPLATE(Structure):
        pass
    return WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_TEMPLATE
def _define_WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_TEMPLATE():
    WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_TEMPLATE = win32more.Networking.WindowsWebServices.WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_TEMPLATE_head
    WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_TEMPLATE._fields_ = [
        ('securityBindingProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES),
        ('clientCredential', POINTER(win32more.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_head)),
    ]
    return WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_TEMPLATE
def _define_WS_TCP_SSPI_USERNAME_BINDING_TEMPLATE_head():
    class WS_TCP_SSPI_USERNAME_BINDING_TEMPLATE(Structure):
        pass
    return WS_TCP_SSPI_USERNAME_BINDING_TEMPLATE
def _define_WS_TCP_SSPI_USERNAME_BINDING_TEMPLATE():
    WS_TCP_SSPI_USERNAME_BINDING_TEMPLATE = win32more.Networking.WindowsWebServices.WS_TCP_SSPI_USERNAME_BINDING_TEMPLATE_head
    WS_TCP_SSPI_USERNAME_BINDING_TEMPLATE._fields_ = [
        ('channelProperties', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES),
        ('securityProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES),
        ('sspiTransportSecurityBinding', win32more.Networking.WindowsWebServices.WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_TEMPLATE),
        ('usernameMessageSecurityBinding', win32more.Networking.WindowsWebServices.WS_USERNAME_MESSAGE_SECURITY_BINDING_TEMPLATE),
    ]
    return WS_TCP_SSPI_USERNAME_BINDING_TEMPLATE
def _define_WS_TCP_SSPI_USERNAME_POLICY_DESCRIPTION_head():
    class WS_TCP_SSPI_USERNAME_POLICY_DESCRIPTION(Structure):
        pass
    return WS_TCP_SSPI_USERNAME_POLICY_DESCRIPTION
def _define_WS_TCP_SSPI_USERNAME_POLICY_DESCRIPTION():
    WS_TCP_SSPI_USERNAME_POLICY_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_TCP_SSPI_USERNAME_POLICY_DESCRIPTION_head
    WS_TCP_SSPI_USERNAME_POLICY_DESCRIPTION._fields_ = [
        ('channelProperties', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES),
        ('securityProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES),
        ('sspiTransportSecurityBinding', win32more.Networking.WindowsWebServices.WS_SSPI_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION),
        ('usernameMessageSecurityBinding', win32more.Networking.WindowsWebServices.WS_USERNAME_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION),
    ]
    return WS_TCP_SSPI_USERNAME_POLICY_DESCRIPTION
def _define_WS_TCP_SSPI_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE_head():
    class WS_TCP_SSPI_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE(Structure):
        pass
    return WS_TCP_SSPI_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE
def _define_WS_TCP_SSPI_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE():
    WS_TCP_SSPI_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE = win32more.Networking.WindowsWebServices.WS_TCP_SSPI_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE_head
    WS_TCP_SSPI_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE._fields_ = [
        ('channelProperties', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES),
        ('securityProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES),
        ('sspiTransportSecurityBinding', win32more.Networking.WindowsWebServices.WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_TEMPLATE),
        ('usernameMessageSecurityBinding', win32more.Networking.WindowsWebServices.WS_USERNAME_MESSAGE_SECURITY_BINDING_TEMPLATE),
        ('securityContextSecurityBinding', win32more.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_SECURITY_BINDING_TEMPLATE),
    ]
    return WS_TCP_SSPI_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE
def _define_WS_TCP_SSPI_USERNAME_SECURITY_CONTEXT_POLICY_DESCRIPTION_head():
    class WS_TCP_SSPI_USERNAME_SECURITY_CONTEXT_POLICY_DESCRIPTION(Structure):
        pass
    return WS_TCP_SSPI_USERNAME_SECURITY_CONTEXT_POLICY_DESCRIPTION
def _define_WS_TCP_SSPI_USERNAME_SECURITY_CONTEXT_POLICY_DESCRIPTION():
    WS_TCP_SSPI_USERNAME_SECURITY_CONTEXT_POLICY_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_TCP_SSPI_USERNAME_SECURITY_CONTEXT_POLICY_DESCRIPTION_head
    WS_TCP_SSPI_USERNAME_SECURITY_CONTEXT_POLICY_DESCRIPTION._fields_ = [
        ('channelProperties', win32more.Networking.WindowsWebServices.WS_CHANNEL_PROPERTIES),
        ('securityProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_PROPERTIES),
        ('sspiTransportSecurityBinding', win32more.Networking.WindowsWebServices.WS_SSPI_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION),
        ('usernameMessageSecurityBinding', win32more.Networking.WindowsWebServices.WS_USERNAME_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION),
        ('securityContextSecurityBinding', win32more.Networking.WindowsWebServices.WS_SECURITY_CONTEXT_SECURITY_BINDING_POLICY_DESCRIPTION),
    ]
    return WS_TCP_SSPI_USERNAME_SECURITY_CONTEXT_POLICY_DESCRIPTION
def _define_WS_THUMBPRINT_CERT_CREDENTIAL_head():
    class WS_THUMBPRINT_CERT_CREDENTIAL(Structure):
        pass
    return WS_THUMBPRINT_CERT_CREDENTIAL
def _define_WS_THUMBPRINT_CERT_CREDENTIAL():
    WS_THUMBPRINT_CERT_CREDENTIAL = win32more.Networking.WindowsWebServices.WS_THUMBPRINT_CERT_CREDENTIAL_head
    WS_THUMBPRINT_CERT_CREDENTIAL._fields_ = [
        ('credential', win32more.Networking.WindowsWebServices.WS_CERT_CREDENTIAL),
        ('storeLocation', UInt32),
        ('storeName', win32more.Networking.WindowsWebServices.WS_STRING),
        ('thumbprint', win32more.Networking.WindowsWebServices.WS_STRING),
    ]
    return WS_THUMBPRINT_CERT_CREDENTIAL
def _define_WS_TIMESPAN_head():
    class WS_TIMESPAN(Structure):
        pass
    return WS_TIMESPAN
def _define_WS_TIMESPAN():
    WS_TIMESPAN = win32more.Networking.WindowsWebServices.WS_TIMESPAN_head
    WS_TIMESPAN._fields_ = [
        ('ticks', Int64),
    ]
    return WS_TIMESPAN
def _define_WS_TIMESPAN_DESCRIPTION_head():
    class WS_TIMESPAN_DESCRIPTION(Structure):
        pass
    return WS_TIMESPAN_DESCRIPTION
def _define_WS_TIMESPAN_DESCRIPTION():
    WS_TIMESPAN_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_TIMESPAN_DESCRIPTION_head
    WS_TIMESPAN_DESCRIPTION._fields_ = [
        ('minValue', win32more.Networking.WindowsWebServices.WS_TIMESPAN),
        ('maxValue', win32more.Networking.WindowsWebServices.WS_TIMESPAN),
    ]
    return WS_TIMESPAN_DESCRIPTION
WS_TRACE_API = Int32
WS_TRACE_API_NONE = -1
WS_TRACE_API_START_READER_CANONICALIZATION = 0
WS_TRACE_API_END_READER_CANONICALIZATION = 1
WS_TRACE_API_START_WRITER_CANONICALIZATION = 2
WS_TRACE_API_END_WRITER_CANONICALIZATION = 3
WS_TRACE_API_CREATE_XML_BUFFER = 4
WS_TRACE_API_REMOVE_NODE = 5
WS_TRACE_API_CREATE_READER = 6
WS_TRACE_API_SET_INPUT = 7
WS_TRACE_API_SET_INPUT_TO_BUFFER = 8
WS_TRACE_API_FREE_XML_READER = 9
WS_TRACE_API_GET_READER_PROPERTY = 10
WS_TRACE_API_GET_READER_NODE = 11
WS_TRACE_API_FILL_READER = 12
WS_TRACE_API_READ_START_ELEMENT = 13
WS_TRACE_API_READ_TO_START_ELEMENT = 14
WS_TRACE_API_READ_START_ATTRIBUTE = 15
WS_TRACE_API_READ_END_ATTRIBUTE = 16
WS_TRACE_API_READ_NODE = 17
WS_TRACE_API_SKIP_NODE = 18
WS_TRACE_API_READ_END_ELEMENT = 19
WS_TRACE_API_FIND_ATTRIBUTE = 20
WS_TRACE_API_READ_ELEMENT_VALUE = 21
WS_TRACE_API_READ_CHARS = 22
WS_TRACE_API_READ_CHARS_UTF8 = 23
WS_TRACE_API_READ_BYTES = 24
WS_TRACE_API_READ_ARRAY = 25
WS_TRACE_API_GET_READER_POSITION = 26
WS_TRACE_API_SET_READER_POSITION = 27
WS_TRACE_API_MOVE_READER = 28
WS_TRACE_API_CREATE_WRITER = 29
WS_TRACE_API_FREE_XML_WRITER = 30
WS_TRACE_API_SET_OUTPUT = 31
WS_TRACE_API_SET_OUTPUT_TO_BUFFER = 32
WS_TRACE_API_GET_WRITER_PROPERTY = 33
WS_TRACE_API_FLUSH_WRITER = 34
WS_TRACE_API_WRITE_START_ELEMENT = 35
WS_TRACE_API_WRITE_END_START_ELEMENT = 36
WS_TRACE_API_WRITE_XMLNS_ATTRIBUTE = 37
WS_TRACE_API_WRITE_START_ATTRIBUTE = 38
WS_TRACE_API_WRITE_END_ATTRIBUTE = 39
WS_TRACE_API_WRITE_VALUE = 40
WS_TRACE_API_WRITE_XML_BUFFER = 41
WS_TRACE_API_READ_XML_BUFFER = 42
WS_TRACE_API_WRITE_XML_BUFFER_TO_BYTES = 43
WS_TRACE_API_READ_XML_BUFFER_FROM_BYTES = 44
WS_TRACE_API_WRITE_ARRAY = 45
WS_TRACE_API_WRITE_QUALIFIED_NAME = 46
WS_TRACE_API_WRITE_CHARS = 47
WS_TRACE_API_WRITE_CHARS_UTF8 = 48
WS_TRACE_API_WRITE_BYTES = 49
WS_TRACE_API_PUSH_BYTES = 50
WS_TRACE_API_PULL_BYTES = 51
WS_TRACE_API_WRITE_END_ELEMENT = 52
WS_TRACE_API_WRITE_TEXT = 53
WS_TRACE_API_WRITE_START_CDATA = 54
WS_TRACE_API_WRITE_END_CDATA = 55
WS_TRACE_API_WRITE_NODE = 56
WS_TRACE_API_PREFIX_FROM_NAMESPACE = 57
WS_TRACE_API_GET_WRITER_POSITION = 58
WS_TRACE_API_SET_WRITER_POSITION = 59
WS_TRACE_API_MOVE_WRITER = 60
WS_TRACE_API_TRIM_XML_WHITESPACE = 61
WS_TRACE_API_VERIFY_XML_NCNAME = 62
WS_TRACE_API_XML_STRING_EQUALS = 63
WS_TRACE_API_NAMESPACE_FROM_PREFIX = 64
WS_TRACE_API_READ_QUALIFIED_NAME = 65
WS_TRACE_API_GET_XML_ATTRIBUTE = 66
WS_TRACE_API_COPY_NODE = 67
WS_TRACE_API_ASYNC_EXECUTE = 68
WS_TRACE_API_CREATE_CHANNEL = 69
WS_TRACE_API_OPEN_CHANNEL = 70
WS_TRACE_API_SEND_MESSAGE = 71
WS_TRACE_API_RECEIVE_MESSAGE = 72
WS_TRACE_API_REQUEST_REPLY = 73
WS_TRACE_API_SEND_REPLY_MESSAGE = 74
WS_TRACE_API_SEND_FAULT_MESSAGE_FOR_ERROR = 75
WS_TRACE_API_GET_CHANNEL_PROPERTY = 76
WS_TRACE_API_SET_CHANNEL_PROPERTY = 77
WS_TRACE_API_WRITE_MESSAGE_START = 78
WS_TRACE_API_WRITE_MESSAGE_END = 79
WS_TRACE_API_READ_MESSAGE_START = 80
WS_TRACE_API_READ_MESSAGE_END = 81
WS_TRACE_API_CLOSE_CHANNEL = 82
WS_TRACE_API_ABORT_CHANNEL = 83
WS_TRACE_API_FREE_CHANNEL = 84
WS_TRACE_API_RESET_CHANNEL = 85
WS_TRACE_API_ABANDON_MESSAGE = 86
WS_TRACE_API_SHUTDOWN_SESSION_CHANNEL = 87
WS_TRACE_API_GET_CONTEXT_PROPERTY = 88
WS_TRACE_API_GET_DICTIONARY = 89
WS_TRACE_API_READ_ENDPOINT_ADDRESS_EXTENSION = 90
WS_TRACE_API_CREATE_ERROR = 91
WS_TRACE_API_ADD_ERROR_STRING = 92
WS_TRACE_API_GET_ERROR_STRING = 93
WS_TRACE_API_COPY_ERROR = 94
WS_TRACE_API_GET_ERROR_PROPERTY = 95
WS_TRACE_API_SET_ERROR_PROPERTY = 96
WS_TRACE_API_RESET_ERROR = 97
WS_TRACE_API_FREE_ERROR = 98
WS_TRACE_API_GET_FAULT_ERROR_PROPERTY = 99
WS_TRACE_API_SET_FAULT_ERROR_PROPERTY = 100
WS_TRACE_API_CREATE_FAULT_FROM_ERROR = 101
WS_TRACE_API_SET_FAULT_ERROR_DETAIL = 102
WS_TRACE_API_GET_FAULT_ERROR_DETAIL = 103
WS_TRACE_API_CREATE_HEAP = 104
WS_TRACE_API_ALLOC = 105
WS_TRACE_API_GET_HEAP_PROPERTY = 106
WS_TRACE_API_RESET_HEAP = 107
WS_TRACE_API_FREE_HEAP = 108
WS_TRACE_API_CREATE_LISTENER = 109
WS_TRACE_API_OPEN_LISTENER = 110
WS_TRACE_API_ACCEPT_CHANNEL = 111
WS_TRACE_API_CLOSE_LISTENER = 112
WS_TRACE_API_ABORT_LISTENER = 113
WS_TRACE_API_RESET_LISTENER = 114
WS_TRACE_API_FREE_LISTENER = 115
WS_TRACE_API_GET_LISTENER_PROPERTY = 116
WS_TRACE_API_SET_LISTENER_PROPERTY = 117
WS_TRACE_API_CREATE_CHANNEL_FOR_LISTENER = 118
WS_TRACE_API_CREATE_MESSAGE = 119
WS_TRACE_API_CREATE_MESSAGE_FOR_CHANNEL = 120
WS_TRACE_API_INITIALIZE_MESSAGE = 121
WS_TRACE_API_RESET_MESSAGE = 122
WS_TRACE_API_FREE_MESSAGE = 123
WS_TRACE_API_GET_HEADER_ATTRIBUTES = 124
WS_TRACE_API_GET_HEADER = 125
WS_TRACE_API_GET_CUSTOM_HEADER = 126
WS_TRACE_API_REMOVE_HEADER = 127
WS_TRACE_API_SET_HEADER = 128
WS_TRACE_API_REMOVE_CUSTOM_HEADER = 129
WS_TRACE_API_ADD_CUSTOM_HEADER = 130
WS_TRACE_API_ADD_MAPPED_HEADER = 131
WS_TRACE_API_REMOVE_MAPPED_HEADER = 132
WS_TRACE_API_GET_MAPPED_HEADER = 133
WS_TRACE_API_WRITE_BODY = 134
WS_TRACE_API_READ_BODY = 135
WS_TRACE_API_WRITE_ENVELOPE_START = 136
WS_TRACE_API_WRITE_ENVELOPE_END = 137
WS_TRACE_API_READ_ENVELOPE_START = 138
WS_TRACE_API_READ_ENVELOPE_END = 139
WS_TRACE_API_GET_MESSAGE_PROPERTY = 140
WS_TRACE_API_SET_MESSAGE_PROPERTY = 141
WS_TRACE_API_ADDRESS_MESSAGE = 142
WS_TRACE_API_CHECK_MUST_UNDERSTAND_HEADERS = 143
WS_TRACE_API_MARK_HEADER_AS_UNDERSTOOD = 144
WS_TRACE_API_FILL_BODY = 145
WS_TRACE_API_FLUSH_BODY = 146
WS_TRACE_API_REQUEST_SECURITY_TOKEN = 147
WS_TRACE_API_GET_SECURITY_TOKEN_PROPERTY = 148
WS_TRACE_API_CREATE_XML_SECURITY_TOKEN = 149
WS_TRACE_API_FREE_SECURITY_TOKEN = 150
WS_TRACE_API_REVOKE_SECURITY_CONTEXT = 151
WS_TRACE_API_GET_SECURITY_CONTEXT_PROPERTY = 152
WS_TRACE_API_READ_ELEMENT_TYPE = 153
WS_TRACE_API_READ_ATTRIBUTE_TYPE = 154
WS_TRACE_API_READ_TYPE = 155
WS_TRACE_API_WRITE_ELEMENT_TYPE = 156
WS_TRACE_API_WRITE_ATTRIBUTE_TYPE = 157
WS_TRACE_API_WRITE_TYPE = 158
WS_TRACE_API_SERVICE_REGISTER_FOR_CANCEL = 159
WS_TRACE_API_GET_SERVICE_HOST_PROPERTY = 160
WS_TRACE_API_CREATE_SERVICE_HOST = 161
WS_TRACE_API_OPEN_SERVICE_HOST = 162
WS_TRACE_API_CLOSE_SERVICE_HOST = 163
WS_TRACE_API_ABORT_SERVICE_HOST = 164
WS_TRACE_API_FREE_SERVICE_HOST = 165
WS_TRACE_API_RESET_SERVICE_HOST = 166
WS_TRACE_API_GET_SERVICE_PROXY_PROPERTY = 167
WS_TRACE_API_CREATE_SERVICE_PROXY = 168
WS_TRACE_API_OPEN_SERVICE_PROXY = 169
WS_TRACE_API_CLOSE_SERVICE_PROXY = 170
WS_TRACE_API_ABORT_SERVICE_PROXY = 171
WS_TRACE_API_FREE_SERVICE_PROXY = 172
WS_TRACE_API_RESET_SERVICE_PROXY = 173
WS_TRACE_API_ABORT_CALL = 174
WS_TRACE_API_CALL = 175
WS_TRACE_API_DECODE_URL = 176
WS_TRACE_API_ENCODE_URL = 177
WS_TRACE_API_COMBINE_URL = 178
WS_TRACE_API_DATETIME_TO_FILETIME = 179
WS_TRACE_API_FILETIME_TO_DATETIME = 180
WS_TRACE_API_DUMP_MEMORY = 181
WS_TRACE_API_SET_AUTOFAIL = 182
WS_TRACE_API_CREATE_METADATA = 183
WS_TRACE_API_READ_METADATA = 184
WS_TRACE_API_FREE_METADATA = 185
WS_TRACE_API_RESET_METADATA = 186
WS_TRACE_API_GET_METADATA_PROPERTY = 187
WS_TRACE_API_GET_MISSING_METADATA_DOCUMENT_ADDRESS = 188
WS_TRACE_API_GET_METADATA_ENDPOINTS = 189
WS_TRACE_API_MATCH_POLICY_ALTERNATIVE = 190
WS_TRACE_API_GET_POLICY_PROPERTY = 191
WS_TRACE_API_GET_POLICY_ALTERNATIVE_COUNT = 192
WS_TRACE_API_WS_CREATE_SERVICE_PROXY_FROM_TEMPLATE = 193
WS_TRACE_API_WS_CREATE_SERVICE_HOST_FROM_TEMPLATE = 194
WS_TRANSFER_MODE = Int32
WS_STREAMED_INPUT_TRANSFER_MODE = 1
WS_STREAMED_OUTPUT_TRANSFER_MODE = 2
WS_BUFFERED_TRANSFER_MODE = 0
WS_STREAMED_TRANSFER_MODE = 3
WS_TRUST_VERSION = Int32
WS_TRUST_VERSION_FEBRUARY_2005 = 1
WS_TRUST_VERSION_1_3 = 2
WS_TYPE = Int32
WS_BOOL_TYPE = 0
WS_INT8_TYPE = 1
WS_INT16_TYPE = 2
WS_INT32_TYPE = 3
WS_INT64_TYPE = 4
WS_UINT8_TYPE = 5
WS_UINT16_TYPE = 6
WS_UINT32_TYPE = 7
WS_UINT64_TYPE = 8
WS_FLOAT_TYPE = 9
WS_DOUBLE_TYPE = 10
WS_DECIMAL_TYPE = 11
WS_DATETIME_TYPE = 12
WS_TIMESPAN_TYPE = 13
WS_GUID_TYPE = 14
WS_UNIQUE_ID_TYPE = 15
WS_STRING_TYPE = 16
WS_WSZ_TYPE = 17
WS_BYTES_TYPE = 18
WS_XML_STRING_TYPE = 19
WS_XML_QNAME_TYPE = 20
WS_XML_BUFFER_TYPE = 21
WS_CHAR_ARRAY_TYPE = 22
WS_UTF8_ARRAY_TYPE = 23
WS_BYTE_ARRAY_TYPE = 24
WS_DESCRIPTION_TYPE = 25
WS_STRUCT_TYPE = 26
WS_CUSTOM_TYPE = 27
WS_ENDPOINT_ADDRESS_TYPE = 28
WS_FAULT_TYPE = 29
WS_VOID_TYPE = 30
WS_ENUM_TYPE = 31
WS_DURATION_TYPE = 32
WS_UNION_TYPE = 33
WS_ANY_ATTRIBUTES_TYPE = 34
WS_TYPE_MAPPING = Int32
WS_ELEMENT_TYPE_MAPPING = 1
WS_ATTRIBUTE_TYPE_MAPPING = 2
WS_ELEMENT_CONTENT_TYPE_MAPPING = 3
WS_ANY_ELEMENT_TYPE_MAPPING = 4
def _define_WS_UINT16_DESCRIPTION_head():
    class WS_UINT16_DESCRIPTION(Structure):
        pass
    return WS_UINT16_DESCRIPTION
def _define_WS_UINT16_DESCRIPTION():
    WS_UINT16_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_UINT16_DESCRIPTION_head
    WS_UINT16_DESCRIPTION._fields_ = [
        ('minValue', UInt16),
        ('maxValue', UInt16),
    ]
    return WS_UINT16_DESCRIPTION
def _define_WS_UINT32_DESCRIPTION_head():
    class WS_UINT32_DESCRIPTION(Structure):
        pass
    return WS_UINT32_DESCRIPTION
def _define_WS_UINT32_DESCRIPTION():
    WS_UINT32_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_UINT32_DESCRIPTION_head
    WS_UINT32_DESCRIPTION._fields_ = [
        ('minValue', UInt32),
        ('maxValue', UInt32),
    ]
    return WS_UINT32_DESCRIPTION
def _define_WS_UINT64_DESCRIPTION_head():
    class WS_UINT64_DESCRIPTION(Structure):
        pass
    return WS_UINT64_DESCRIPTION
def _define_WS_UINT64_DESCRIPTION():
    WS_UINT64_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_UINT64_DESCRIPTION_head
    WS_UINT64_DESCRIPTION._fields_ = [
        ('minValue', UInt64),
        ('maxValue', UInt64),
    ]
    return WS_UINT64_DESCRIPTION
def _define_WS_UINT8_DESCRIPTION_head():
    class WS_UINT8_DESCRIPTION(Structure):
        pass
    return WS_UINT8_DESCRIPTION
def _define_WS_UINT8_DESCRIPTION():
    WS_UINT8_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_UINT8_DESCRIPTION_head
    WS_UINT8_DESCRIPTION._fields_ = [
        ('minValue', Byte),
        ('maxValue', Byte),
    ]
    return WS_UINT8_DESCRIPTION
def _define_WS_UNION_DESCRIPTION_head():
    class WS_UNION_DESCRIPTION(Structure):
        pass
    return WS_UNION_DESCRIPTION
def _define_WS_UNION_DESCRIPTION():
    WS_UNION_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_UNION_DESCRIPTION_head
    WS_UNION_DESCRIPTION._fields_ = [
        ('size', UInt32),
        ('alignment', UInt32),
        ('fields', POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_UNION_FIELD_DESCRIPTION_head))),
        ('fieldCount', UInt32),
        ('enumOffset', UInt32),
        ('noneEnumValue', Int32),
        ('valueIndices', POINTER(UInt32)),
    ]
    return WS_UNION_DESCRIPTION
def _define_WS_UNION_FIELD_DESCRIPTION_head():
    class WS_UNION_FIELD_DESCRIPTION(Structure):
        pass
    return WS_UNION_FIELD_DESCRIPTION
def _define_WS_UNION_FIELD_DESCRIPTION():
    WS_UNION_FIELD_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_UNION_FIELD_DESCRIPTION_head
    WS_UNION_FIELD_DESCRIPTION._fields_ = [
        ('value', Int32),
        ('field', win32more.Networking.WindowsWebServices.WS_FIELD_DESCRIPTION),
    ]
    return WS_UNION_FIELD_DESCRIPTION
def _define_WS_UNIQUE_ID_head():
    class WS_UNIQUE_ID(Structure):
        pass
    return WS_UNIQUE_ID
def _define_WS_UNIQUE_ID():
    WS_UNIQUE_ID = win32more.Networking.WindowsWebServices.WS_UNIQUE_ID_head
    WS_UNIQUE_ID._fields_ = [
        ('uri', win32more.Networking.WindowsWebServices.WS_STRING),
        ('guid', Guid),
    ]
    return WS_UNIQUE_ID
def _define_WS_UNIQUE_ID_DESCRIPTION_head():
    class WS_UNIQUE_ID_DESCRIPTION(Structure):
        pass
    return WS_UNIQUE_ID_DESCRIPTION
def _define_WS_UNIQUE_ID_DESCRIPTION():
    WS_UNIQUE_ID_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_UNIQUE_ID_DESCRIPTION_head
    WS_UNIQUE_ID_DESCRIPTION._fields_ = [
        ('minCharCount', UInt32),
        ('maxCharCount', UInt32),
    ]
    return WS_UNIQUE_ID_DESCRIPTION
def _define_WS_UNKNOWN_ENDPOINT_IDENTITY_head():
    class WS_UNKNOWN_ENDPOINT_IDENTITY(Structure):
        pass
    return WS_UNKNOWN_ENDPOINT_IDENTITY
def _define_WS_UNKNOWN_ENDPOINT_IDENTITY():
    WS_UNKNOWN_ENDPOINT_IDENTITY = win32more.Networking.WindowsWebServices.WS_UNKNOWN_ENDPOINT_IDENTITY_head
    WS_UNKNOWN_ENDPOINT_IDENTITY._fields_ = [
        ('identity', win32more.Networking.WindowsWebServices.WS_ENDPOINT_IDENTITY),
        ('element', POINTER(win32more.Networking.WindowsWebServices.WS_XML_BUFFER_head)),
    ]
    return WS_UNKNOWN_ENDPOINT_IDENTITY
def _define_WS_UPN_ENDPOINT_IDENTITY_head():
    class WS_UPN_ENDPOINT_IDENTITY(Structure):
        pass
    return WS_UPN_ENDPOINT_IDENTITY
def _define_WS_UPN_ENDPOINT_IDENTITY():
    WS_UPN_ENDPOINT_IDENTITY = win32more.Networking.WindowsWebServices.WS_UPN_ENDPOINT_IDENTITY_head
    WS_UPN_ENDPOINT_IDENTITY._fields_ = [
        ('identity', win32more.Networking.WindowsWebServices.WS_ENDPOINT_IDENTITY),
        ('upn', win32more.Networking.WindowsWebServices.WS_STRING),
    ]
    return WS_UPN_ENDPOINT_IDENTITY
def _define_WS_URL_head():
    class WS_URL(Structure):
        pass
    return WS_URL
def _define_WS_URL():
    WS_URL = win32more.Networking.WindowsWebServices.WS_URL_head
    WS_URL._fields_ = [
        ('scheme', win32more.Networking.WindowsWebServices.WS_URL_SCHEME_TYPE),
    ]
    return WS_URL
WS_URL_SCHEME_TYPE = Int32
WS_URL_HTTP_SCHEME_TYPE = 0
WS_URL_HTTPS_SCHEME_TYPE = 1
WS_URL_NETTCP_SCHEME_TYPE = 2
WS_URL_SOAPUDP_SCHEME_TYPE = 3
WS_URL_NETPIPE_SCHEME_TYPE = 4
def _define_WS_USERNAME_CREDENTIAL_head():
    class WS_USERNAME_CREDENTIAL(Structure):
        pass
    return WS_USERNAME_CREDENTIAL
def _define_WS_USERNAME_CREDENTIAL():
    WS_USERNAME_CREDENTIAL = win32more.Networking.WindowsWebServices.WS_USERNAME_CREDENTIAL_head
    WS_USERNAME_CREDENTIAL._fields_ = [
        ('credentialType', win32more.Networking.WindowsWebServices.WS_USERNAME_CREDENTIAL_TYPE),
    ]
    return WS_USERNAME_CREDENTIAL
WS_USERNAME_CREDENTIAL_TYPE = Int32
WS_STRING_USERNAME_CREDENTIAL_TYPE = 1
def _define_WS_USERNAME_MESSAGE_SECURITY_BINDING_head():
    class WS_USERNAME_MESSAGE_SECURITY_BINDING(Structure):
        pass
    return WS_USERNAME_MESSAGE_SECURITY_BINDING
def _define_WS_USERNAME_MESSAGE_SECURITY_BINDING():
    WS_USERNAME_MESSAGE_SECURITY_BINDING = win32more.Networking.WindowsWebServices.WS_USERNAME_MESSAGE_SECURITY_BINDING_head
    WS_USERNAME_MESSAGE_SECURITY_BINDING._fields_ = [
        ('binding', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING),
        ('bindingUsage', win32more.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE),
        ('clientCredential', POINTER(win32more.Networking.WindowsWebServices.WS_USERNAME_CREDENTIAL_head)),
        ('passwordValidator', win32more.Networking.WindowsWebServices.WS_VALIDATE_PASSWORD_CALLBACK),
        ('passwordValidatorCallbackState', c_void_p),
    ]
    return WS_USERNAME_MESSAGE_SECURITY_BINDING
def _define_WS_USERNAME_MESSAGE_SECURITY_BINDING_CONSTRAINT_head():
    class WS_USERNAME_MESSAGE_SECURITY_BINDING_CONSTRAINT(Structure):
        pass
    return WS_USERNAME_MESSAGE_SECURITY_BINDING_CONSTRAINT
def _define_WS_USERNAME_MESSAGE_SECURITY_BINDING_CONSTRAINT():
    WS_USERNAME_MESSAGE_SECURITY_BINDING_CONSTRAINT = win32more.Networking.WindowsWebServices.WS_USERNAME_MESSAGE_SECURITY_BINDING_CONSTRAINT_head
    WS_USERNAME_MESSAGE_SECURITY_BINDING_CONSTRAINT._fields_ = [
        ('bindingConstraint', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_CONSTRAINT),
        ('bindingUsage', win32more.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE),
    ]
    return WS_USERNAME_MESSAGE_SECURITY_BINDING_CONSTRAINT
def _define_WS_USERNAME_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION_head():
    class WS_USERNAME_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION(Structure):
        pass
    return WS_USERNAME_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION
def _define_WS_USERNAME_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION():
    WS_USERNAME_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_USERNAME_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION_head
    WS_USERNAME_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION._fields_ = [
        ('securityBindingProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES),
        ('bindingUsage', win32more.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE),
    ]
    return WS_USERNAME_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION
def _define_WS_USERNAME_MESSAGE_SECURITY_BINDING_TEMPLATE_head():
    class WS_USERNAME_MESSAGE_SECURITY_BINDING_TEMPLATE(Structure):
        pass
    return WS_USERNAME_MESSAGE_SECURITY_BINDING_TEMPLATE
def _define_WS_USERNAME_MESSAGE_SECURITY_BINDING_TEMPLATE():
    WS_USERNAME_MESSAGE_SECURITY_BINDING_TEMPLATE = win32more.Networking.WindowsWebServices.WS_USERNAME_MESSAGE_SECURITY_BINDING_TEMPLATE_head
    WS_USERNAME_MESSAGE_SECURITY_BINDING_TEMPLATE._fields_ = [
        ('securityBindingProperties', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING_PROPERTIES),
        ('clientCredential', POINTER(win32more.Networking.WindowsWebServices.WS_USERNAME_CREDENTIAL_head)),
        ('passwordValidator', win32more.Networking.WindowsWebServices.WS_VALIDATE_PASSWORD_CALLBACK),
        ('passwordValidatorCallbackState', c_void_p),
    ]
    return WS_USERNAME_MESSAGE_SECURITY_BINDING_TEMPLATE
def _define_WS_UTF8_ARRAY_DESCRIPTION_head():
    class WS_UTF8_ARRAY_DESCRIPTION(Structure):
        pass
    return WS_UTF8_ARRAY_DESCRIPTION
def _define_WS_UTF8_ARRAY_DESCRIPTION():
    WS_UTF8_ARRAY_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_UTF8_ARRAY_DESCRIPTION_head
    WS_UTF8_ARRAY_DESCRIPTION._fields_ = [
        ('minByteCount', UInt32),
        ('maxByteCount', UInt32),
    ]
    return WS_UTF8_ARRAY_DESCRIPTION
def _define_WS_VALIDATE_PASSWORD_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_STRING_head),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_VALIDATE_SAML_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_XML_BUFFER_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
WS_VALUE_TYPE = Int32
WS_BOOL_VALUE_TYPE = 0
WS_INT8_VALUE_TYPE = 1
WS_INT16_VALUE_TYPE = 2
WS_INT32_VALUE_TYPE = 3
WS_INT64_VALUE_TYPE = 4
WS_UINT8_VALUE_TYPE = 5
WS_UINT16_VALUE_TYPE = 6
WS_UINT32_VALUE_TYPE = 7
WS_UINT64_VALUE_TYPE = 8
WS_FLOAT_VALUE_TYPE = 9
WS_DOUBLE_VALUE_TYPE = 10
WS_DECIMAL_VALUE_TYPE = 11
WS_DATETIME_VALUE_TYPE = 12
WS_TIMESPAN_VALUE_TYPE = 13
WS_GUID_VALUE_TYPE = 14
WS_DURATION_VALUE_TYPE = 15
def _define_WS_VOID_DESCRIPTION_head():
    class WS_VOID_DESCRIPTION(Structure):
        pass
    return WS_VOID_DESCRIPTION
def _define_WS_VOID_DESCRIPTION():
    WS_VOID_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_VOID_DESCRIPTION_head
    WS_VOID_DESCRIPTION._fields_ = [
        ('size', UInt32),
    ]
    return WS_VOID_DESCRIPTION
def _define_WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_head():
    class WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL(Structure):
        pass
    return WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL
def _define_WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL():
    WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL = win32more.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_head
    WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL._fields_ = [
        ('credentialType', win32more.Networking.WindowsWebServices.WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_TYPE),
    ]
    return WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL
WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_TYPE = Int32
WS_STRING_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_TYPE = 1
WS_DEFAULT_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_TYPE = 2
WS_OPAQUE_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_TYPE = 3
WS_WINDOWS_INTEGRATED_AUTH_PACKAGE = Int32
WS_WINDOWS_INTEGRATED_AUTH_PACKAGE_KERBEROS = 1
WS_WINDOWS_INTEGRATED_AUTH_PACKAGE_NTLM = 2
WS_WINDOWS_INTEGRATED_AUTH_PACKAGE_SPNEGO = 3
def _define_WS_WRITE_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_BYTES_head),UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_WRITE_MESSAGE_END_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_WRITE_MESSAGE_START_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,POINTER(win32more.Networking.WindowsWebServices.WS_MESSAGE_head),POINTER(win32more.Networking.WindowsWebServices.WS_ASYNC_CONTEXT_head),POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
WS_WRITE_OPTION = Int32
WS_WRITE_REQUIRED_VALUE = 1
WS_WRITE_REQUIRED_POINTER = 2
WS_WRITE_NILLABLE_VALUE = 3
WS_WRITE_NILLABLE_POINTER = 4
def _define_WS_WRITE_TYPE_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_head),win32more.Networking.WindowsWebServices.WS_TYPE_MAPPING,c_void_p,c_void_p,UInt32,POINTER(win32more.Networking.WindowsWebServices.WS_ERROR_head))
def _define_WS_WSZ_DESCRIPTION_head():
    class WS_WSZ_DESCRIPTION(Structure):
        pass
    return WS_WSZ_DESCRIPTION
def _define_WS_WSZ_DESCRIPTION():
    WS_WSZ_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_WSZ_DESCRIPTION_head
    WS_WSZ_DESCRIPTION._fields_ = [
        ('minCharCount', UInt32),
        ('maxCharCount', UInt32),
    ]
    return WS_WSZ_DESCRIPTION
def _define_WS_XML_ATTRIBUTE_head():
    class WS_XML_ATTRIBUTE(Structure):
        pass
    return WS_XML_ATTRIBUTE
def _define_WS_XML_ATTRIBUTE():
    WS_XML_ATTRIBUTE = win32more.Networking.WindowsWebServices.WS_XML_ATTRIBUTE_head
    WS_XML_ATTRIBUTE._fields_ = [
        ('singleQuote', Byte),
        ('isXmlNs', Byte),
        ('prefix', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('localName', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('ns', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('value', POINTER(win32more.Networking.WindowsWebServices.WS_XML_TEXT_head)),
    ]
    return WS_XML_ATTRIBUTE
def _define_WS_XML_BASE64_TEXT_head():
    class WS_XML_BASE64_TEXT(Structure):
        pass
    return WS_XML_BASE64_TEXT
def _define_WS_XML_BASE64_TEXT():
    WS_XML_BASE64_TEXT = win32more.Networking.WindowsWebServices.WS_XML_BASE64_TEXT_head
    WS_XML_BASE64_TEXT._fields_ = [
        ('text', win32more.Networking.WindowsWebServices.WS_XML_TEXT),
        ('bytes', c_char_p_no),
        ('length', UInt32),
    ]
    return WS_XML_BASE64_TEXT
def _define_WS_XML_BOOL_TEXT_head():
    class WS_XML_BOOL_TEXT(Structure):
        pass
    return WS_XML_BOOL_TEXT
def _define_WS_XML_BOOL_TEXT():
    WS_XML_BOOL_TEXT = win32more.Networking.WindowsWebServices.WS_XML_BOOL_TEXT_head
    WS_XML_BOOL_TEXT._fields_ = [
        ('text', win32more.Networking.WindowsWebServices.WS_XML_TEXT),
        ('value', win32more.Foundation.BOOL),
    ]
    return WS_XML_BOOL_TEXT
def _define_WS_XML_BUFFER_head():
    class WS_XML_BUFFER(Structure):
        pass
    return WS_XML_BUFFER
def _define_WS_XML_BUFFER():
    WS_XML_BUFFER = win32more.Networking.WindowsWebServices.WS_XML_BUFFER_head
    return WS_XML_BUFFER
def _define_WS_XML_BUFFER_PROPERTY_head():
    class WS_XML_BUFFER_PROPERTY(Structure):
        pass
    return WS_XML_BUFFER_PROPERTY
def _define_WS_XML_BUFFER_PROPERTY():
    WS_XML_BUFFER_PROPERTY = win32more.Networking.WindowsWebServices.WS_XML_BUFFER_PROPERTY_head
    WS_XML_BUFFER_PROPERTY._fields_ = [
        ('id', win32more.Networking.WindowsWebServices.WS_XML_BUFFER_PROPERTY_ID),
        ('value', c_void_p),
        ('valueSize', UInt32),
    ]
    return WS_XML_BUFFER_PROPERTY
WS_XML_BUFFER_PROPERTY_ID = Int32
WS_XML_CANONICALIZATION_ALGORITHM = Int32
WS_EXCLUSIVE_XML_CANONICALIZATION_ALGORITHM = 0
WS_EXCLUSIVE_WITH_COMMENTS_XML_CANONICALIZATION_ALGORITHM = 1
WS_INCLUSIVE_XML_CANONICALIZATION_ALGORITHM = 2
WS_INCLUSIVE_WITH_COMMENTS_XML_CANONICALIZATION_ALGORITHM = 3
def _define_WS_XML_CANONICALIZATION_INCLUSIVE_PREFIXES_head():
    class WS_XML_CANONICALIZATION_INCLUSIVE_PREFIXES(Structure):
        pass
    return WS_XML_CANONICALIZATION_INCLUSIVE_PREFIXES
def _define_WS_XML_CANONICALIZATION_INCLUSIVE_PREFIXES():
    WS_XML_CANONICALIZATION_INCLUSIVE_PREFIXES = win32more.Networking.WindowsWebServices.WS_XML_CANONICALIZATION_INCLUSIVE_PREFIXES_head
    WS_XML_CANONICALIZATION_INCLUSIVE_PREFIXES._fields_ = [
        ('prefixCount', UInt32),
        ('prefixes', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
    ]
    return WS_XML_CANONICALIZATION_INCLUSIVE_PREFIXES
def _define_WS_XML_CANONICALIZATION_PROPERTY_head():
    class WS_XML_CANONICALIZATION_PROPERTY(Structure):
        pass
    return WS_XML_CANONICALIZATION_PROPERTY
def _define_WS_XML_CANONICALIZATION_PROPERTY():
    WS_XML_CANONICALIZATION_PROPERTY = win32more.Networking.WindowsWebServices.WS_XML_CANONICALIZATION_PROPERTY_head
    WS_XML_CANONICALIZATION_PROPERTY._fields_ = [
        ('id', win32more.Networking.WindowsWebServices.WS_XML_CANONICALIZATION_PROPERTY_ID),
        ('value', c_void_p),
        ('valueSize', UInt32),
    ]
    return WS_XML_CANONICALIZATION_PROPERTY
WS_XML_CANONICALIZATION_PROPERTY_ID = Int32
WS_XML_CANONICALIZATION_PROPERTY_ALGORITHM = 0
WS_XML_CANONICALIZATION_PROPERTY_INCLUSIVE_PREFIXES = 1
WS_XML_CANONICALIZATION_PROPERTY_OMITTED_ELEMENT = 2
WS_XML_CANONICALIZATION_PROPERTY_OUTPUT_BUFFER_SIZE = 3
def _define_WS_XML_COMMENT_NODE_head():
    class WS_XML_COMMENT_NODE(Structure):
        pass
    return WS_XML_COMMENT_NODE
def _define_WS_XML_COMMENT_NODE():
    WS_XML_COMMENT_NODE = win32more.Networking.WindowsWebServices.WS_XML_COMMENT_NODE_head
    WS_XML_COMMENT_NODE._fields_ = [
        ('node', win32more.Networking.WindowsWebServices.WS_XML_NODE),
        ('value', win32more.Networking.WindowsWebServices.WS_XML_STRING),
    ]
    return WS_XML_COMMENT_NODE
def _define_WS_XML_DATETIME_TEXT_head():
    class WS_XML_DATETIME_TEXT(Structure):
        pass
    return WS_XML_DATETIME_TEXT
def _define_WS_XML_DATETIME_TEXT():
    WS_XML_DATETIME_TEXT = win32more.Networking.WindowsWebServices.WS_XML_DATETIME_TEXT_head
    WS_XML_DATETIME_TEXT._fields_ = [
        ('text', win32more.Networking.WindowsWebServices.WS_XML_TEXT),
        ('value', win32more.Networking.WindowsWebServices.WS_DATETIME),
    ]
    return WS_XML_DATETIME_TEXT
def _define_WS_XML_DECIMAL_TEXT_head():
    class WS_XML_DECIMAL_TEXT(Structure):
        pass
    return WS_XML_DECIMAL_TEXT
def _define_WS_XML_DECIMAL_TEXT():
    WS_XML_DECIMAL_TEXT = win32more.Networking.WindowsWebServices.WS_XML_DECIMAL_TEXT_head
    WS_XML_DECIMAL_TEXT._fields_ = [
        ('text', win32more.Networking.WindowsWebServices.WS_XML_TEXT),
        ('value', win32more.Foundation.DECIMAL),
    ]
    return WS_XML_DECIMAL_TEXT
def _define_WS_XML_DICTIONARY_head():
    class WS_XML_DICTIONARY(Structure):
        pass
    return WS_XML_DICTIONARY
def _define_WS_XML_DICTIONARY():
    WS_XML_DICTIONARY = win32more.Networking.WindowsWebServices.WS_XML_DICTIONARY_head
    WS_XML_DICTIONARY._fields_ = [
        ('guid', Guid),
        ('strings', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('stringCount', UInt32),
        ('isConst', win32more.Foundation.BOOL),
    ]
    return WS_XML_DICTIONARY
def _define_WS_XML_DOUBLE_TEXT_head():
    class WS_XML_DOUBLE_TEXT(Structure):
        pass
    return WS_XML_DOUBLE_TEXT
def _define_WS_XML_DOUBLE_TEXT():
    WS_XML_DOUBLE_TEXT = win32more.Networking.WindowsWebServices.WS_XML_DOUBLE_TEXT_head
    WS_XML_DOUBLE_TEXT._fields_ = [
        ('text', win32more.Networking.WindowsWebServices.WS_XML_TEXT),
        ('value', Double),
    ]
    return WS_XML_DOUBLE_TEXT
def _define_WS_XML_ELEMENT_NODE_head():
    class WS_XML_ELEMENT_NODE(Structure):
        pass
    return WS_XML_ELEMENT_NODE
def _define_WS_XML_ELEMENT_NODE():
    WS_XML_ELEMENT_NODE = win32more.Networking.WindowsWebServices.WS_XML_ELEMENT_NODE_head
    WS_XML_ELEMENT_NODE._fields_ = [
        ('node', win32more.Networking.WindowsWebServices.WS_XML_NODE),
        ('prefix', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('localName', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('ns', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('attributeCount', UInt32),
        ('attributes', POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_XML_ATTRIBUTE_head))),
        ('isEmpty', win32more.Foundation.BOOL),
    ]
    return WS_XML_ELEMENT_NODE
def _define_WS_XML_FLOAT_TEXT_head():
    class WS_XML_FLOAT_TEXT(Structure):
        pass
    return WS_XML_FLOAT_TEXT
def _define_WS_XML_FLOAT_TEXT():
    WS_XML_FLOAT_TEXT = win32more.Networking.WindowsWebServices.WS_XML_FLOAT_TEXT_head
    WS_XML_FLOAT_TEXT._fields_ = [
        ('text', win32more.Networking.WindowsWebServices.WS_XML_TEXT),
        ('value', Single),
    ]
    return WS_XML_FLOAT_TEXT
def _define_WS_XML_GUID_TEXT_head():
    class WS_XML_GUID_TEXT(Structure):
        pass
    return WS_XML_GUID_TEXT
def _define_WS_XML_GUID_TEXT():
    WS_XML_GUID_TEXT = win32more.Networking.WindowsWebServices.WS_XML_GUID_TEXT_head
    WS_XML_GUID_TEXT._fields_ = [
        ('text', win32more.Networking.WindowsWebServices.WS_XML_TEXT),
        ('value', Guid),
    ]
    return WS_XML_GUID_TEXT
def _define_WS_XML_INT32_TEXT_head():
    class WS_XML_INT32_TEXT(Structure):
        pass
    return WS_XML_INT32_TEXT
def _define_WS_XML_INT32_TEXT():
    WS_XML_INT32_TEXT = win32more.Networking.WindowsWebServices.WS_XML_INT32_TEXT_head
    WS_XML_INT32_TEXT._fields_ = [
        ('text', win32more.Networking.WindowsWebServices.WS_XML_TEXT),
        ('value', Int32),
    ]
    return WS_XML_INT32_TEXT
def _define_WS_XML_INT64_TEXT_head():
    class WS_XML_INT64_TEXT(Structure):
        pass
    return WS_XML_INT64_TEXT
def _define_WS_XML_INT64_TEXT():
    WS_XML_INT64_TEXT = win32more.Networking.WindowsWebServices.WS_XML_INT64_TEXT_head
    WS_XML_INT64_TEXT._fields_ = [
        ('text', win32more.Networking.WindowsWebServices.WS_XML_TEXT),
        ('value', Int64),
    ]
    return WS_XML_INT64_TEXT
def _define_WS_XML_LIST_TEXT_head():
    class WS_XML_LIST_TEXT(Structure):
        pass
    return WS_XML_LIST_TEXT
def _define_WS_XML_LIST_TEXT():
    WS_XML_LIST_TEXT = win32more.Networking.WindowsWebServices.WS_XML_LIST_TEXT_head
    WS_XML_LIST_TEXT._fields_ = [
        ('text', win32more.Networking.WindowsWebServices.WS_XML_TEXT),
        ('itemCount', UInt32),
        ('items', POINTER(POINTER(win32more.Networking.WindowsWebServices.WS_XML_TEXT_head))),
    ]
    return WS_XML_LIST_TEXT
def _define_WS_XML_NODE_head():
    class WS_XML_NODE(Structure):
        pass
    return WS_XML_NODE
def _define_WS_XML_NODE():
    WS_XML_NODE = win32more.Networking.WindowsWebServices.WS_XML_NODE_head
    WS_XML_NODE._fields_ = [
        ('nodeType', win32more.Networking.WindowsWebServices.WS_XML_NODE_TYPE),
    ]
    return WS_XML_NODE
def _define_WS_XML_NODE_POSITION_head():
    class WS_XML_NODE_POSITION(Structure):
        pass
    return WS_XML_NODE_POSITION
def _define_WS_XML_NODE_POSITION():
    WS_XML_NODE_POSITION = win32more.Networking.WindowsWebServices.WS_XML_NODE_POSITION_head
    WS_XML_NODE_POSITION._fields_ = [
        ('buffer', POINTER(win32more.Networking.WindowsWebServices.WS_XML_BUFFER_head)),
        ('node', c_void_p),
    ]
    return WS_XML_NODE_POSITION
WS_XML_NODE_TYPE = Int32
WS_XML_NODE_TYPE_ELEMENT = 1
WS_XML_NODE_TYPE_TEXT = 2
WS_XML_NODE_TYPE_END_ELEMENT = 3
WS_XML_NODE_TYPE_COMMENT = 4
WS_XML_NODE_TYPE_CDATA = 6
WS_XML_NODE_TYPE_END_CDATA = 7
WS_XML_NODE_TYPE_EOF = 8
WS_XML_NODE_TYPE_BOF = 9
def _define_WS_XML_QNAME_head():
    class WS_XML_QNAME(Structure):
        pass
    return WS_XML_QNAME
def _define_WS_XML_QNAME():
    WS_XML_QNAME = win32more.Networking.WindowsWebServices.WS_XML_QNAME_head
    WS_XML_QNAME._fields_ = [
        ('localName', win32more.Networking.WindowsWebServices.WS_XML_STRING),
        ('ns', win32more.Networking.WindowsWebServices.WS_XML_STRING),
    ]
    return WS_XML_QNAME
def _define_WS_XML_QNAME_DESCRIPTION_head():
    class WS_XML_QNAME_DESCRIPTION(Structure):
        pass
    return WS_XML_QNAME_DESCRIPTION
def _define_WS_XML_QNAME_DESCRIPTION():
    WS_XML_QNAME_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_XML_QNAME_DESCRIPTION_head
    WS_XML_QNAME_DESCRIPTION._fields_ = [
        ('minLocalNameByteCount', UInt32),
        ('maxLocalNameByteCount', UInt32),
        ('minNsByteCount', UInt32),
        ('maxNsByteCount', UInt32),
    ]
    return WS_XML_QNAME_DESCRIPTION
def _define_WS_XML_QNAME_TEXT_head():
    class WS_XML_QNAME_TEXT(Structure):
        pass
    return WS_XML_QNAME_TEXT
def _define_WS_XML_QNAME_TEXT():
    WS_XML_QNAME_TEXT = win32more.Networking.WindowsWebServices.WS_XML_QNAME_TEXT_head
    WS_XML_QNAME_TEXT._fields_ = [
        ('text', win32more.Networking.WindowsWebServices.WS_XML_TEXT),
        ('prefix', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('localName', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
        ('ns', POINTER(win32more.Networking.WindowsWebServices.WS_XML_STRING_head)),
    ]
    return WS_XML_QNAME_TEXT
def _define_WS_XML_READER_head():
    class WS_XML_READER(Structure):
        pass
    return WS_XML_READER
def _define_WS_XML_READER():
    WS_XML_READER = win32more.Networking.WindowsWebServices.WS_XML_READER_head
    return WS_XML_READER
def _define_WS_XML_READER_BINARY_ENCODING_head():
    class WS_XML_READER_BINARY_ENCODING(Structure):
        pass
    return WS_XML_READER_BINARY_ENCODING
def _define_WS_XML_READER_BINARY_ENCODING():
    WS_XML_READER_BINARY_ENCODING = win32more.Networking.WindowsWebServices.WS_XML_READER_BINARY_ENCODING_head
    WS_XML_READER_BINARY_ENCODING._fields_ = [
        ('encoding', win32more.Networking.WindowsWebServices.WS_XML_READER_ENCODING),
        ('staticDictionary', POINTER(win32more.Networking.WindowsWebServices.WS_XML_DICTIONARY_head)),
        ('dynamicDictionary', POINTER(win32more.Networking.WindowsWebServices.WS_XML_DICTIONARY_head)),
    ]
    return WS_XML_READER_BINARY_ENCODING
def _define_WS_XML_READER_BUFFER_INPUT_head():
    class WS_XML_READER_BUFFER_INPUT(Structure):
        pass
    return WS_XML_READER_BUFFER_INPUT
def _define_WS_XML_READER_BUFFER_INPUT():
    WS_XML_READER_BUFFER_INPUT = win32more.Networking.WindowsWebServices.WS_XML_READER_BUFFER_INPUT_head
    WS_XML_READER_BUFFER_INPUT._fields_ = [
        ('input', win32more.Networking.WindowsWebServices.WS_XML_READER_INPUT),
        ('encodedData', c_void_p),
        ('encodedDataSize', UInt32),
    ]
    return WS_XML_READER_BUFFER_INPUT
def _define_WS_XML_READER_ENCODING_head():
    class WS_XML_READER_ENCODING(Structure):
        pass
    return WS_XML_READER_ENCODING
def _define_WS_XML_READER_ENCODING():
    WS_XML_READER_ENCODING = win32more.Networking.WindowsWebServices.WS_XML_READER_ENCODING_head
    WS_XML_READER_ENCODING._fields_ = [
        ('encodingType', win32more.Networking.WindowsWebServices.WS_XML_READER_ENCODING_TYPE),
    ]
    return WS_XML_READER_ENCODING
WS_XML_READER_ENCODING_TYPE = Int32
WS_XML_READER_ENCODING_TYPE_TEXT = 1
WS_XML_READER_ENCODING_TYPE_BINARY = 2
WS_XML_READER_ENCODING_TYPE_MTOM = 3
WS_XML_READER_ENCODING_TYPE_RAW = 4
def _define_WS_XML_READER_INPUT_head():
    class WS_XML_READER_INPUT(Structure):
        pass
    return WS_XML_READER_INPUT
def _define_WS_XML_READER_INPUT():
    WS_XML_READER_INPUT = win32more.Networking.WindowsWebServices.WS_XML_READER_INPUT_head
    WS_XML_READER_INPUT._fields_ = [
        ('inputType', win32more.Networking.WindowsWebServices.WS_XML_READER_INPUT_TYPE),
    ]
    return WS_XML_READER_INPUT
WS_XML_READER_INPUT_TYPE = Int32
WS_XML_READER_INPUT_TYPE_BUFFER = 1
WS_XML_READER_INPUT_TYPE_STREAM = 2
def _define_WS_XML_READER_MTOM_ENCODING_head():
    class WS_XML_READER_MTOM_ENCODING(Structure):
        pass
    return WS_XML_READER_MTOM_ENCODING
def _define_WS_XML_READER_MTOM_ENCODING():
    WS_XML_READER_MTOM_ENCODING = win32more.Networking.WindowsWebServices.WS_XML_READER_MTOM_ENCODING_head
    WS_XML_READER_MTOM_ENCODING._fields_ = [
        ('encoding', win32more.Networking.WindowsWebServices.WS_XML_READER_ENCODING),
        ('textEncoding', POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_ENCODING_head)),
        ('readMimeHeader', win32more.Foundation.BOOL),
        ('startInfo', win32more.Networking.WindowsWebServices.WS_STRING),
        ('boundary', win32more.Networking.WindowsWebServices.WS_STRING),
        ('startUri', win32more.Networking.WindowsWebServices.WS_STRING),
    ]
    return WS_XML_READER_MTOM_ENCODING
def _define_WS_XML_READER_PROPERTIES_head():
    class WS_XML_READER_PROPERTIES(Structure):
        pass
    return WS_XML_READER_PROPERTIES
def _define_WS_XML_READER_PROPERTIES():
    WS_XML_READER_PROPERTIES = win32more.Networking.WindowsWebServices.WS_XML_READER_PROPERTIES_head
    WS_XML_READER_PROPERTIES._fields_ = [
        ('properties', POINTER(win32more.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_head)),
        ('propertyCount', UInt32),
    ]
    return WS_XML_READER_PROPERTIES
def _define_WS_XML_READER_PROPERTY_head():
    class WS_XML_READER_PROPERTY(Structure):
        pass
    return WS_XML_READER_PROPERTY
def _define_WS_XML_READER_PROPERTY():
    WS_XML_READER_PROPERTY = win32more.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_head
    WS_XML_READER_PROPERTY._fields_ = [
        ('id', win32more.Networking.WindowsWebServices.WS_XML_READER_PROPERTY_ID),
        ('value', c_void_p),
        ('valueSize', UInt32),
    ]
    return WS_XML_READER_PROPERTY
WS_XML_READER_PROPERTY_ID = Int32
WS_XML_READER_PROPERTY_MAX_DEPTH = 0
WS_XML_READER_PROPERTY_ALLOW_FRAGMENT = 1
WS_XML_READER_PROPERTY_MAX_ATTRIBUTES = 2
WS_XML_READER_PROPERTY_READ_DECLARATION = 3
WS_XML_READER_PROPERTY_CHARSET = 4
WS_XML_READER_PROPERTY_ROW = 5
WS_XML_READER_PROPERTY_COLUMN = 6
WS_XML_READER_PROPERTY_UTF8_TRIM_SIZE = 7
WS_XML_READER_PROPERTY_STREAM_BUFFER_SIZE = 8
WS_XML_READER_PROPERTY_IN_ATTRIBUTE = 9
WS_XML_READER_PROPERTY_STREAM_MAX_ROOT_MIME_PART_SIZE = 10
WS_XML_READER_PROPERTY_STREAM_MAX_MIME_HEADERS_SIZE = 11
WS_XML_READER_PROPERTY_MAX_MIME_PARTS = 12
WS_XML_READER_PROPERTY_ALLOW_INVALID_CHARACTER_REFERENCES = 13
WS_XML_READER_PROPERTY_MAX_NAMESPACES = 14
def _define_WS_XML_READER_RAW_ENCODING_head():
    class WS_XML_READER_RAW_ENCODING(Structure):
        pass
    return WS_XML_READER_RAW_ENCODING
def _define_WS_XML_READER_RAW_ENCODING():
    WS_XML_READER_RAW_ENCODING = win32more.Networking.WindowsWebServices.WS_XML_READER_RAW_ENCODING_head
    WS_XML_READER_RAW_ENCODING._fields_ = [
        ('encoding', win32more.Networking.WindowsWebServices.WS_XML_READER_ENCODING),
    ]
    return WS_XML_READER_RAW_ENCODING
def _define_WS_XML_READER_STREAM_INPUT_head():
    class WS_XML_READER_STREAM_INPUT(Structure):
        pass
    return WS_XML_READER_STREAM_INPUT
def _define_WS_XML_READER_STREAM_INPUT():
    WS_XML_READER_STREAM_INPUT = win32more.Networking.WindowsWebServices.WS_XML_READER_STREAM_INPUT_head
    WS_XML_READER_STREAM_INPUT._fields_ = [
        ('input', win32more.Networking.WindowsWebServices.WS_XML_READER_INPUT),
        ('readCallback', win32more.Networking.WindowsWebServices.WS_READ_CALLBACK),
        ('readCallbackState', c_void_p),
    ]
    return WS_XML_READER_STREAM_INPUT
def _define_WS_XML_READER_TEXT_ENCODING_head():
    class WS_XML_READER_TEXT_ENCODING(Structure):
        pass
    return WS_XML_READER_TEXT_ENCODING
def _define_WS_XML_READER_TEXT_ENCODING():
    WS_XML_READER_TEXT_ENCODING = win32more.Networking.WindowsWebServices.WS_XML_READER_TEXT_ENCODING_head
    WS_XML_READER_TEXT_ENCODING._fields_ = [
        ('encoding', win32more.Networking.WindowsWebServices.WS_XML_READER_ENCODING),
        ('charSet', win32more.Networking.WindowsWebServices.WS_CHARSET),
    ]
    return WS_XML_READER_TEXT_ENCODING
def _define_WS_XML_SECURITY_TOKEN_PROPERTY_head():
    class WS_XML_SECURITY_TOKEN_PROPERTY(Structure):
        pass
    return WS_XML_SECURITY_TOKEN_PROPERTY
def _define_WS_XML_SECURITY_TOKEN_PROPERTY():
    WS_XML_SECURITY_TOKEN_PROPERTY = win32more.Networking.WindowsWebServices.WS_XML_SECURITY_TOKEN_PROPERTY_head
    WS_XML_SECURITY_TOKEN_PROPERTY._fields_ = [
        ('id', win32more.Networking.WindowsWebServices.WS_XML_SECURITY_TOKEN_PROPERTY_ID),
        ('value', c_void_p),
        ('valueSize', UInt32),
    ]
    return WS_XML_SECURITY_TOKEN_PROPERTY
WS_XML_SECURITY_TOKEN_PROPERTY_ID = Int32
WS_XML_SECURITY_TOKEN_PROPERTY_ATTACHED_REFERENCE = 1
WS_XML_SECURITY_TOKEN_PROPERTY_UNATTACHED_REFERENCE = 2
WS_XML_SECURITY_TOKEN_PROPERTY_VALID_FROM_TIME = 3
WS_XML_SECURITY_TOKEN_PROPERTY_VALID_TILL_TIME = 4
def _define_WS_XML_STRING_head():
    class WS_XML_STRING(Structure):
        pass
    return WS_XML_STRING
def _define_WS_XML_STRING():
    WS_XML_STRING = win32more.Networking.WindowsWebServices.WS_XML_STRING_head
    WS_XML_STRING._fields_ = [
        ('length', UInt32),
        ('bytes', c_char_p_no),
        ('dictionary', POINTER(win32more.Networking.WindowsWebServices.WS_XML_DICTIONARY_head)),
        ('id', UInt32),
    ]
    return WS_XML_STRING
def _define_WS_XML_STRING_DESCRIPTION_head():
    class WS_XML_STRING_DESCRIPTION(Structure):
        pass
    return WS_XML_STRING_DESCRIPTION
def _define_WS_XML_STRING_DESCRIPTION():
    WS_XML_STRING_DESCRIPTION = win32more.Networking.WindowsWebServices.WS_XML_STRING_DESCRIPTION_head
    WS_XML_STRING_DESCRIPTION._fields_ = [
        ('minByteCount', UInt32),
        ('maxByteCount', UInt32),
    ]
    return WS_XML_STRING_DESCRIPTION
def _define_WS_XML_TEXT_head():
    class WS_XML_TEXT(Structure):
        pass
    return WS_XML_TEXT
def _define_WS_XML_TEXT():
    WS_XML_TEXT = win32more.Networking.WindowsWebServices.WS_XML_TEXT_head
    WS_XML_TEXT._fields_ = [
        ('textType', win32more.Networking.WindowsWebServices.WS_XML_TEXT_TYPE),
    ]
    return WS_XML_TEXT
def _define_WS_XML_TEXT_NODE_head():
    class WS_XML_TEXT_NODE(Structure):
        pass
    return WS_XML_TEXT_NODE
def _define_WS_XML_TEXT_NODE():
    WS_XML_TEXT_NODE = win32more.Networking.WindowsWebServices.WS_XML_TEXT_NODE_head
    WS_XML_TEXT_NODE._fields_ = [
        ('node', win32more.Networking.WindowsWebServices.WS_XML_NODE),
        ('text', POINTER(win32more.Networking.WindowsWebServices.WS_XML_TEXT_head)),
    ]
    return WS_XML_TEXT_NODE
WS_XML_TEXT_TYPE = Int32
WS_XML_TEXT_TYPE_UTF8 = 1
WS_XML_TEXT_TYPE_UTF16 = 2
WS_XML_TEXT_TYPE_BASE64 = 3
WS_XML_TEXT_TYPE_BOOL = 4
WS_XML_TEXT_TYPE_INT32 = 5
WS_XML_TEXT_TYPE_INT64 = 6
WS_XML_TEXT_TYPE_UINT64 = 7
WS_XML_TEXT_TYPE_FLOAT = 8
WS_XML_TEXT_TYPE_DOUBLE = 9
WS_XML_TEXT_TYPE_DECIMAL = 10
WS_XML_TEXT_TYPE_GUID = 11
WS_XML_TEXT_TYPE_UNIQUE_ID = 12
WS_XML_TEXT_TYPE_DATETIME = 13
WS_XML_TEXT_TYPE_TIMESPAN = 14
WS_XML_TEXT_TYPE_QNAME = 15
WS_XML_TEXT_TYPE_LIST = 16
def _define_WS_XML_TIMESPAN_TEXT_head():
    class WS_XML_TIMESPAN_TEXT(Structure):
        pass
    return WS_XML_TIMESPAN_TEXT
def _define_WS_XML_TIMESPAN_TEXT():
    WS_XML_TIMESPAN_TEXT = win32more.Networking.WindowsWebServices.WS_XML_TIMESPAN_TEXT_head
    WS_XML_TIMESPAN_TEXT._fields_ = [
        ('text', win32more.Networking.WindowsWebServices.WS_XML_TEXT),
        ('value', win32more.Networking.WindowsWebServices.WS_TIMESPAN),
    ]
    return WS_XML_TIMESPAN_TEXT
def _define_WS_XML_TOKEN_MESSAGE_SECURITY_BINDING_head():
    class WS_XML_TOKEN_MESSAGE_SECURITY_BINDING(Structure):
        pass
    return WS_XML_TOKEN_MESSAGE_SECURITY_BINDING
def _define_WS_XML_TOKEN_MESSAGE_SECURITY_BINDING():
    WS_XML_TOKEN_MESSAGE_SECURITY_BINDING = win32more.Networking.WindowsWebServices.WS_XML_TOKEN_MESSAGE_SECURITY_BINDING_head
    WS_XML_TOKEN_MESSAGE_SECURITY_BINDING._fields_ = [
        ('binding', win32more.Networking.WindowsWebServices.WS_SECURITY_BINDING),
        ('bindingUsage', win32more.Networking.WindowsWebServices.WS_MESSAGE_SECURITY_USAGE),
        ('xmlToken', POINTER(win32more.Networking.WindowsWebServices.WS_SECURITY_TOKEN_head)),
    ]
    return WS_XML_TOKEN_MESSAGE_SECURITY_BINDING
def _define_WS_XML_UINT64_TEXT_head():
    class WS_XML_UINT64_TEXT(Structure):
        pass
    return WS_XML_UINT64_TEXT
def _define_WS_XML_UINT64_TEXT():
    WS_XML_UINT64_TEXT = win32more.Networking.WindowsWebServices.WS_XML_UINT64_TEXT_head
    WS_XML_UINT64_TEXT._fields_ = [
        ('text', win32more.Networking.WindowsWebServices.WS_XML_TEXT),
        ('value', UInt64),
    ]
    return WS_XML_UINT64_TEXT
def _define_WS_XML_UNIQUE_ID_TEXT_head():
    class WS_XML_UNIQUE_ID_TEXT(Structure):
        pass
    return WS_XML_UNIQUE_ID_TEXT
def _define_WS_XML_UNIQUE_ID_TEXT():
    WS_XML_UNIQUE_ID_TEXT = win32more.Networking.WindowsWebServices.WS_XML_UNIQUE_ID_TEXT_head
    WS_XML_UNIQUE_ID_TEXT._fields_ = [
        ('text', win32more.Networking.WindowsWebServices.WS_XML_TEXT),
        ('value', Guid),
    ]
    return WS_XML_UNIQUE_ID_TEXT
def _define_WS_XML_UTF16_TEXT_head():
    class WS_XML_UTF16_TEXT(Structure):
        pass
    return WS_XML_UTF16_TEXT
def _define_WS_XML_UTF16_TEXT():
    WS_XML_UTF16_TEXT = win32more.Networking.WindowsWebServices.WS_XML_UTF16_TEXT_head
    WS_XML_UTF16_TEXT._fields_ = [
        ('text', win32more.Networking.WindowsWebServices.WS_XML_TEXT),
        ('bytes', c_char_p_no),
        ('byteCount', UInt32),
    ]
    return WS_XML_UTF16_TEXT
def _define_WS_XML_UTF8_TEXT_head():
    class WS_XML_UTF8_TEXT(Structure):
        pass
    return WS_XML_UTF8_TEXT
def _define_WS_XML_UTF8_TEXT():
    WS_XML_UTF8_TEXT = win32more.Networking.WindowsWebServices.WS_XML_UTF8_TEXT_head
    WS_XML_UTF8_TEXT._fields_ = [
        ('text', win32more.Networking.WindowsWebServices.WS_XML_TEXT),
        ('value', win32more.Networking.WindowsWebServices.WS_XML_STRING),
    ]
    return WS_XML_UTF8_TEXT
def _define_WS_XML_WRITER_head():
    class WS_XML_WRITER(Structure):
        pass
    return WS_XML_WRITER
def _define_WS_XML_WRITER():
    WS_XML_WRITER = win32more.Networking.WindowsWebServices.WS_XML_WRITER_head
    return WS_XML_WRITER
def _define_WS_XML_WRITER_BINARY_ENCODING_head():
    class WS_XML_WRITER_BINARY_ENCODING(Structure):
        pass
    return WS_XML_WRITER_BINARY_ENCODING
def _define_WS_XML_WRITER_BINARY_ENCODING():
    WS_XML_WRITER_BINARY_ENCODING = win32more.Networking.WindowsWebServices.WS_XML_WRITER_BINARY_ENCODING_head
    WS_XML_WRITER_BINARY_ENCODING._fields_ = [
        ('encoding', win32more.Networking.WindowsWebServices.WS_XML_WRITER_ENCODING),
        ('staticDictionary', POINTER(win32more.Networking.WindowsWebServices.WS_XML_DICTIONARY_head)),
        ('dynamicStringCallback', win32more.Networking.WindowsWebServices.WS_DYNAMIC_STRING_CALLBACK),
        ('dynamicStringCallbackState', c_void_p),
    ]
    return WS_XML_WRITER_BINARY_ENCODING
def _define_WS_XML_WRITER_BUFFER_OUTPUT_head():
    class WS_XML_WRITER_BUFFER_OUTPUT(Structure):
        pass
    return WS_XML_WRITER_BUFFER_OUTPUT
def _define_WS_XML_WRITER_BUFFER_OUTPUT():
    WS_XML_WRITER_BUFFER_OUTPUT = win32more.Networking.WindowsWebServices.WS_XML_WRITER_BUFFER_OUTPUT_head
    WS_XML_WRITER_BUFFER_OUTPUT._fields_ = [
        ('output', win32more.Networking.WindowsWebServices.WS_XML_WRITER_OUTPUT),
    ]
    return WS_XML_WRITER_BUFFER_OUTPUT
def _define_WS_XML_WRITER_ENCODING_head():
    class WS_XML_WRITER_ENCODING(Structure):
        pass
    return WS_XML_WRITER_ENCODING
def _define_WS_XML_WRITER_ENCODING():
    WS_XML_WRITER_ENCODING = win32more.Networking.WindowsWebServices.WS_XML_WRITER_ENCODING_head
    WS_XML_WRITER_ENCODING._fields_ = [
        ('encodingType', win32more.Networking.WindowsWebServices.WS_XML_WRITER_ENCODING_TYPE),
    ]
    return WS_XML_WRITER_ENCODING
WS_XML_WRITER_ENCODING_TYPE = Int32
WS_XML_WRITER_ENCODING_TYPE_TEXT = 1
WS_XML_WRITER_ENCODING_TYPE_BINARY = 2
WS_XML_WRITER_ENCODING_TYPE_MTOM = 3
WS_XML_WRITER_ENCODING_TYPE_RAW = 4
def _define_WS_XML_WRITER_MTOM_ENCODING_head():
    class WS_XML_WRITER_MTOM_ENCODING(Structure):
        pass
    return WS_XML_WRITER_MTOM_ENCODING
def _define_WS_XML_WRITER_MTOM_ENCODING():
    WS_XML_WRITER_MTOM_ENCODING = win32more.Networking.WindowsWebServices.WS_XML_WRITER_MTOM_ENCODING_head
    WS_XML_WRITER_MTOM_ENCODING._fields_ = [
        ('encoding', win32more.Networking.WindowsWebServices.WS_XML_WRITER_ENCODING),
        ('textEncoding', POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_ENCODING_head)),
        ('writeMimeHeader', win32more.Foundation.BOOL),
        ('boundary', win32more.Networking.WindowsWebServices.WS_STRING),
        ('startInfo', win32more.Networking.WindowsWebServices.WS_STRING),
        ('startUri', win32more.Networking.WindowsWebServices.WS_STRING),
        ('maxInlineByteCount', UInt32),
    ]
    return WS_XML_WRITER_MTOM_ENCODING
def _define_WS_XML_WRITER_OUTPUT_head():
    class WS_XML_WRITER_OUTPUT(Structure):
        pass
    return WS_XML_WRITER_OUTPUT
def _define_WS_XML_WRITER_OUTPUT():
    WS_XML_WRITER_OUTPUT = win32more.Networking.WindowsWebServices.WS_XML_WRITER_OUTPUT_head
    WS_XML_WRITER_OUTPUT._fields_ = [
        ('outputType', win32more.Networking.WindowsWebServices.WS_XML_WRITER_OUTPUT_TYPE),
    ]
    return WS_XML_WRITER_OUTPUT
WS_XML_WRITER_OUTPUT_TYPE = Int32
WS_XML_WRITER_OUTPUT_TYPE_BUFFER = 1
WS_XML_WRITER_OUTPUT_TYPE_STREAM = 2
def _define_WS_XML_WRITER_PROPERTIES_head():
    class WS_XML_WRITER_PROPERTIES(Structure):
        pass
    return WS_XML_WRITER_PROPERTIES
def _define_WS_XML_WRITER_PROPERTIES():
    WS_XML_WRITER_PROPERTIES = win32more.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTIES_head
    WS_XML_WRITER_PROPERTIES._fields_ = [
        ('properties', POINTER(win32more.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_head)),
        ('propertyCount', UInt32),
    ]
    return WS_XML_WRITER_PROPERTIES
def _define_WS_XML_WRITER_PROPERTY_head():
    class WS_XML_WRITER_PROPERTY(Structure):
        pass
    return WS_XML_WRITER_PROPERTY
def _define_WS_XML_WRITER_PROPERTY():
    WS_XML_WRITER_PROPERTY = win32more.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_head
    WS_XML_WRITER_PROPERTY._fields_ = [
        ('id', win32more.Networking.WindowsWebServices.WS_XML_WRITER_PROPERTY_ID),
        ('value', c_void_p),
        ('valueSize', UInt32),
    ]
    return WS_XML_WRITER_PROPERTY
WS_XML_WRITER_PROPERTY_ID = Int32
WS_XML_WRITER_PROPERTY_MAX_DEPTH = 0
WS_XML_WRITER_PROPERTY_ALLOW_FRAGMENT = 1
WS_XML_WRITER_PROPERTY_MAX_ATTRIBUTES = 2
WS_XML_WRITER_PROPERTY_WRITE_DECLARATION = 3
WS_XML_WRITER_PROPERTY_INDENT = 4
WS_XML_WRITER_PROPERTY_BUFFER_TRIM_SIZE = 5
WS_XML_WRITER_PROPERTY_CHARSET = 6
WS_XML_WRITER_PROPERTY_BUFFERS = 7
WS_XML_WRITER_PROPERTY_BUFFER_MAX_SIZE = 8
WS_XML_WRITER_PROPERTY_BYTES = 9
WS_XML_WRITER_PROPERTY_IN_ATTRIBUTE = 10
WS_XML_WRITER_PROPERTY_MAX_MIME_PARTS_BUFFER_SIZE = 11
WS_XML_WRITER_PROPERTY_INITIAL_BUFFER = 12
WS_XML_WRITER_PROPERTY_ALLOW_INVALID_CHARACTER_REFERENCES = 13
WS_XML_WRITER_PROPERTY_MAX_NAMESPACES = 14
WS_XML_WRITER_PROPERTY_BYTES_WRITTEN = 15
WS_XML_WRITER_PROPERTY_BYTES_TO_CLOSE = 16
WS_XML_WRITER_PROPERTY_COMPRESS_EMPTY_ELEMENTS = 17
WS_XML_WRITER_PROPERTY_EMIT_UNCOMPRESSED_EMPTY_ELEMENTS = 18
def _define_WS_XML_WRITER_RAW_ENCODING_head():
    class WS_XML_WRITER_RAW_ENCODING(Structure):
        pass
    return WS_XML_WRITER_RAW_ENCODING
def _define_WS_XML_WRITER_RAW_ENCODING():
    WS_XML_WRITER_RAW_ENCODING = win32more.Networking.WindowsWebServices.WS_XML_WRITER_RAW_ENCODING_head
    WS_XML_WRITER_RAW_ENCODING._fields_ = [
        ('encoding', win32more.Networking.WindowsWebServices.WS_XML_WRITER_ENCODING),
    ]
    return WS_XML_WRITER_RAW_ENCODING
def _define_WS_XML_WRITER_STREAM_OUTPUT_head():
    class WS_XML_WRITER_STREAM_OUTPUT(Structure):
        pass
    return WS_XML_WRITER_STREAM_OUTPUT
def _define_WS_XML_WRITER_STREAM_OUTPUT():
    WS_XML_WRITER_STREAM_OUTPUT = win32more.Networking.WindowsWebServices.WS_XML_WRITER_STREAM_OUTPUT_head
    WS_XML_WRITER_STREAM_OUTPUT._fields_ = [
        ('output', win32more.Networking.WindowsWebServices.WS_XML_WRITER_OUTPUT),
        ('writeCallback', win32more.Networking.WindowsWebServices.WS_WRITE_CALLBACK),
        ('writeCallbackState', c_void_p),
    ]
    return WS_XML_WRITER_STREAM_OUTPUT
def _define_WS_XML_WRITER_TEXT_ENCODING_head():
    class WS_XML_WRITER_TEXT_ENCODING(Structure):
        pass
    return WS_XML_WRITER_TEXT_ENCODING
def _define_WS_XML_WRITER_TEXT_ENCODING():
    WS_XML_WRITER_TEXT_ENCODING = win32more.Networking.WindowsWebServices.WS_XML_WRITER_TEXT_ENCODING_head
    WS_XML_WRITER_TEXT_ENCODING._fields_ = [
        ('encoding', win32more.Networking.WindowsWebServices.WS_XML_WRITER_ENCODING),
        ('charSet', win32more.Networking.WindowsWebServices.WS_CHARSET),
    ]
    return WS_XML_WRITER_TEXT_ENCODING
__all__ = [
    "IContentPrefetcherTaskTrigger",
    "WEBAUTHN_API_CURRENT_VERSION",
    "WEBAUTHN_API_VERSION_1",
    "WEBAUTHN_API_VERSION_2",
    "WEBAUTHN_API_VERSION_3",
    "WEBAUTHN_ASSERTION",
    "WEBAUTHN_ASSERTION_CURRENT_VERSION",
    "WEBAUTHN_ASSERTION_VERSION_1",
    "WEBAUTHN_ASSERTION_VERSION_2",
    "WEBAUTHN_ATTESTATION_CONVEYANCE_PREFERENCE_ANY",
    "WEBAUTHN_ATTESTATION_CONVEYANCE_PREFERENCE_DIRECT",
    "WEBAUTHN_ATTESTATION_CONVEYANCE_PREFERENCE_INDIRECT",
    "WEBAUTHN_ATTESTATION_CONVEYANCE_PREFERENCE_NONE",
    "WEBAUTHN_ATTESTATION_DECODE_COMMON",
    "WEBAUTHN_ATTESTATION_DECODE_NONE",
    "WEBAUTHN_ATTESTATION_TYPE_NONE",
    "WEBAUTHN_ATTESTATION_TYPE_PACKED",
    "WEBAUTHN_ATTESTATION_TYPE_TPM",
    "WEBAUTHN_ATTESTATION_TYPE_U2F",
    "WEBAUTHN_ATTESTATION_VER_TPM_2_0",
    "WEBAUTHN_AUTHENTICATOR_ATTACHMENT_ANY",
    "WEBAUTHN_AUTHENTICATOR_ATTACHMENT_CROSS_PLATFORM",
    "WEBAUTHN_AUTHENTICATOR_ATTACHMENT_CROSS_PLATFORM_U2F_V2",
    "WEBAUTHN_AUTHENTICATOR_ATTACHMENT_PLATFORM",
    "WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS",
    "WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_CURRENT_VERSION",
    "WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_VERSION_1",
    "WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_VERSION_2",
    "WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_VERSION_3",
    "WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_VERSION_4",
    "WEBAUTHN_AUTHENTICATOR_GET_ASSERTION_OPTIONS_VERSION_5",
    "WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS",
    "WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_CURRENT_VERSION",
    "WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_VERSION_1",
    "WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_VERSION_2",
    "WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_VERSION_3",
    "WEBAUTHN_AUTHENTICATOR_MAKE_CREDENTIAL_OPTIONS_VERSION_4",
    "WEBAUTHN_CLIENT_DATA",
    "WEBAUTHN_CLIENT_DATA_CURRENT_VERSION",
    "WEBAUTHN_COMMON_ATTESTATION",
    "WEBAUTHN_COMMON_ATTESTATION_CURRENT_VERSION",
    "WEBAUTHN_COSE_ALGORITHM_ECDSA_P256_WITH_SHA256",
    "WEBAUTHN_COSE_ALGORITHM_ECDSA_P384_WITH_SHA384",
    "WEBAUTHN_COSE_ALGORITHM_ECDSA_P521_WITH_SHA512",
    "WEBAUTHN_COSE_ALGORITHM_RSASSA_PKCS1_V1_5_WITH_SHA256",
    "WEBAUTHN_COSE_ALGORITHM_RSASSA_PKCS1_V1_5_WITH_SHA384",
    "WEBAUTHN_COSE_ALGORITHM_RSASSA_PKCS1_V1_5_WITH_SHA512",
    "WEBAUTHN_COSE_ALGORITHM_RSA_PSS_WITH_SHA256",
    "WEBAUTHN_COSE_ALGORITHM_RSA_PSS_WITH_SHA384",
    "WEBAUTHN_COSE_ALGORITHM_RSA_PSS_WITH_SHA512",
    "WEBAUTHN_COSE_CREDENTIAL_PARAMETER",
    "WEBAUTHN_COSE_CREDENTIAL_PARAMETERS",
    "WEBAUTHN_COSE_CREDENTIAL_PARAMETER_CURRENT_VERSION",
    "WEBAUTHN_CREDENTIAL",
    "WEBAUTHN_CREDENTIALS",
    "WEBAUTHN_CREDENTIAL_ATTESTATION",
    "WEBAUTHN_CREDENTIAL_ATTESTATION_CURRENT_VERSION",
    "WEBAUTHN_CREDENTIAL_ATTESTATION_VERSION_1",
    "WEBAUTHN_CREDENTIAL_ATTESTATION_VERSION_2",
    "WEBAUTHN_CREDENTIAL_ATTESTATION_VERSION_3",
    "WEBAUTHN_CREDENTIAL_ATTESTATION_VERSION_4",
    "WEBAUTHN_CREDENTIAL_CURRENT_VERSION",
    "WEBAUTHN_CREDENTIAL_EX",
    "WEBAUTHN_CREDENTIAL_EX_CURRENT_VERSION",
    "WEBAUTHN_CREDENTIAL_LIST",
    "WEBAUTHN_CREDENTIAL_TYPE_PUBLIC_KEY",
    "WEBAUTHN_CRED_BLOB_EXTENSION",
    "WEBAUTHN_CRED_LARGE_BLOB_OPERATION_DELETE",
    "WEBAUTHN_CRED_LARGE_BLOB_OPERATION_GET",
    "WEBAUTHN_CRED_LARGE_BLOB_OPERATION_NONE",
    "WEBAUTHN_CRED_LARGE_BLOB_OPERATION_SET",
    "WEBAUTHN_CRED_LARGE_BLOB_STATUS_AUTHENTICATOR_ERROR",
    "WEBAUTHN_CRED_LARGE_BLOB_STATUS_INVALID_DATA",
    "WEBAUTHN_CRED_LARGE_BLOB_STATUS_INVALID_PARAMETER",
    "WEBAUTHN_CRED_LARGE_BLOB_STATUS_LACK_OF_SPACE",
    "WEBAUTHN_CRED_LARGE_BLOB_STATUS_MULTIPLE_CREDENTIALS",
    "WEBAUTHN_CRED_LARGE_BLOB_STATUS_NONE",
    "WEBAUTHN_CRED_LARGE_BLOB_STATUS_NOT_FOUND",
    "WEBAUTHN_CRED_LARGE_BLOB_STATUS_NOT_SUPPORTED",
    "WEBAUTHN_CRED_LARGE_BLOB_STATUS_PLATFORM_ERROR",
    "WEBAUTHN_CRED_LARGE_BLOB_STATUS_SUCCESS",
    "WEBAUTHN_CRED_PROTECT_EXTENSION_IN",
    "WEBAUTHN_CTAP_TRANSPORT_BLE",
    "WEBAUTHN_CTAP_TRANSPORT_FLAGS_MASK",
    "WEBAUTHN_CTAP_TRANSPORT_INTERNAL",
    "WEBAUTHN_CTAP_TRANSPORT_NFC",
    "WEBAUTHN_CTAP_TRANSPORT_TEST",
    "WEBAUTHN_CTAP_TRANSPORT_USB",
    "WEBAUTHN_ENTERPRISE_ATTESTATION_NONE",
    "WEBAUTHN_ENTERPRISE_ATTESTATION_PLATFORM_MANAGED",
    "WEBAUTHN_ENTERPRISE_ATTESTATION_VENDOR_FACILITATED",
    "WEBAUTHN_EXTENSION",
    "WEBAUTHN_EXTENSIONS",
    "WEBAUTHN_EXTENSIONS_IDENTIFIER_CRED_BLOB",
    "WEBAUTHN_EXTENSIONS_IDENTIFIER_CRED_PROTECT",
    "WEBAUTHN_EXTENSIONS_IDENTIFIER_HMAC_SECRET",
    "WEBAUTHN_EXTENSIONS_IDENTIFIER_MIN_PIN_LENGTH",
    "WEBAUTHN_HASH_ALGORITHM_SHA_256",
    "WEBAUTHN_HASH_ALGORITHM_SHA_384",
    "WEBAUTHN_HASH_ALGORITHM_SHA_512",
    "WEBAUTHN_LARGE_BLOB_SUPPORT_NONE",
    "WEBAUTHN_LARGE_BLOB_SUPPORT_PREFERRED",
    "WEBAUTHN_LARGE_BLOB_SUPPORT_REQUIRED",
    "WEBAUTHN_MAX_USER_ID_LENGTH",
    "WEBAUTHN_RP_ENTITY_INFORMATION",
    "WEBAUTHN_RP_ENTITY_INFORMATION_CURRENT_VERSION",
    "WEBAUTHN_USER_ENTITY_INFORMATION",
    "WEBAUTHN_USER_ENTITY_INFORMATION_CURRENT_VERSION",
    "WEBAUTHN_USER_VERIFICATION_ANY",
    "WEBAUTHN_USER_VERIFICATION_OPTIONAL",
    "WEBAUTHN_USER_VERIFICATION_OPTIONAL_WITH_CREDENTIAL_ID_LIST",
    "WEBAUTHN_USER_VERIFICATION_REQUIRED",
    "WEBAUTHN_USER_VERIFICATION_REQUIREMENT_ANY",
    "WEBAUTHN_USER_VERIFICATION_REQUIREMENT_DISCOURAGED",
    "WEBAUTHN_USER_VERIFICATION_REQUIREMENT_PREFERRED",
    "WEBAUTHN_USER_VERIFICATION_REQUIREMENT_REQUIRED",
    "WEBAUTHN_X5C",
    "WS_ABANDON_MESSAGE_CALLBACK",
    "WS_ABORT_CHANNEL_CALLBACK",
    "WS_ABORT_LISTENER_CALLBACK",
    "WS_ACCEPT_CHANNEL_CALLBACK",
    "WS_ACTION_HEADER",
    "WS_ADDRESSING_VERSION",
    "WS_ADDRESSING_VERSION_0_9",
    "WS_ADDRESSING_VERSION_1_0",
    "WS_ADDRESSING_VERSION_TRANSPORT",
    "WS_ANY_ATTRIBUTE",
    "WS_ANY_ATTRIBUTES",
    "WS_ANY_ATTRIBUTES_FIELD_MAPPING",
    "WS_ANY_ATTRIBUTES_TYPE",
    "WS_ANY_CONTENT_FIELD_MAPPING",
    "WS_ANY_ELEMENT_FIELD_MAPPING",
    "WS_ANY_ELEMENT_TYPE_MAPPING",
    "WS_ASYNC_CALLBACK",
    "WS_ASYNC_CONTEXT",
    "WS_ASYNC_FUNCTION",
    "WS_ASYNC_OPERATION",
    "WS_ASYNC_STATE",
    "WS_ATTRIBUTE_DESCRIPTION",
    "WS_ATTRIBUTE_FIELD_MAPPING",
    "WS_ATTRIBUTE_TYPE_MAPPING",
    "WS_AUTO_COOKIE_MODE",
    "WS_BINDING_TEMPLATE_TYPE",
    "WS_BLANK_MESSAGE",
    "WS_BOOL_DESCRIPTION",
    "WS_BOOL_TYPE",
    "WS_BOOL_VALUE_TYPE",
    "WS_BUFFERED_TRANSFER_MODE",
    "WS_BUFFERS",
    "WS_BYTES",
    "WS_BYTES_DESCRIPTION",
    "WS_BYTES_TYPE",
    "WS_BYTE_ARRAY_DESCRIPTION",
    "WS_BYTE_ARRAY_TYPE",
    "WS_CALLBACK_MODEL",
    "WS_CALL_PROPERTY",
    "WS_CALL_PROPERTY_CALL_ID",
    "WS_CALL_PROPERTY_CHECK_MUST_UNDERSTAND",
    "WS_CALL_PROPERTY_ID",
    "WS_CALL_PROPERTY_RECEIVE_MESSAGE_CONTEXT",
    "WS_CALL_PROPERTY_SEND_MESSAGE_CONTEXT",
    "WS_CAPI_ASYMMETRIC_SECURITY_KEY_HANDLE",
    "WS_CAPI_ASYMMETRIC_SECURITY_KEY_HANDLE_TYPE",
    "WS_CERTIFICATE_VALIDATION_CALLBACK",
    "WS_CERTIFICATE_VALIDATION_CALLBACK_CONTEXT",
    "WS_CERT_CREDENTIAL",
    "WS_CERT_CREDENTIAL_TYPE",
    "WS_CERT_ENDPOINT_IDENTITY",
    "WS_CERT_ENDPOINT_IDENTITY_TYPE",
    "WS_CERT_FAILURE_CN_MISMATCH",
    "WS_CERT_FAILURE_INVALID_DATE",
    "WS_CERT_FAILURE_REVOCATION_OFFLINE",
    "WS_CERT_FAILURE_UNTRUSTED_ROOT",
    "WS_CERT_FAILURE_WRONG_USAGE",
    "WS_CERT_ISSUER_LIST_NOTIFICATION_CALLBACK",
    "WS_CERT_MESSAGE_SECURITY_BINDING_CONSTRAINT",
    "WS_CERT_MESSAGE_SECURITY_BINDING_CONSTRAINT_TYPE",
    "WS_CERT_SIGNED_SAML_AUTHENTICATOR",
    "WS_CERT_SIGNED_SAML_AUTHENTICATOR_TYPE",
    "WS_CHANNEL",
    "WS_CHANNEL_BINDING",
    "WS_CHANNEL_DECODER",
    "WS_CHANNEL_ENCODER",
    "WS_CHANNEL_PROPERTIES",
    "WS_CHANNEL_PROPERTY",
    "WS_CHANNEL_PROPERTY_ADDRESSING_VERSION",
    "WS_CHANNEL_PROPERTY_ALLOW_UNSECURED_FAULTS",
    "WS_CHANNEL_PROPERTY_ASYNC_CALLBACK_MODEL",
    "WS_CHANNEL_PROPERTY_CHANNEL_TYPE",
    "WS_CHANNEL_PROPERTY_CLOSE_TIMEOUT",
    "WS_CHANNEL_PROPERTY_CONNECT_TIMEOUT",
    "WS_CHANNEL_PROPERTY_CONSTRAINT",
    "WS_CHANNEL_PROPERTY_COOKIE_MODE",
    "WS_CHANNEL_PROPERTY_CUSTOM_CHANNEL_CALLBACKS",
    "WS_CHANNEL_PROPERTY_CUSTOM_CHANNEL_INSTANCE",
    "WS_CHANNEL_PROPERTY_CUSTOM_CHANNEL_PARAMETERS",
    "WS_CHANNEL_PROPERTY_CUSTOM_HTTP_PROXY",
    "WS_CHANNEL_PROPERTY_DECODER",
    "WS_CHANNEL_PROPERTY_ENABLE_HTTP_REDIRECT",
    "WS_CHANNEL_PROPERTY_ENABLE_TIMEOUTS",
    "WS_CHANNEL_PROPERTY_ENCODER",
    "WS_CHANNEL_PROPERTY_ENCODING",
    "WS_CHANNEL_PROPERTY_ENVELOPE_VERSION",
    "WS_CHANNEL_PROPERTY_FAULTS_AS_ERRORS",
    "WS_CHANNEL_PROPERTY_HTTP_CONNECTION_ID",
    "WS_CHANNEL_PROPERTY_HTTP_MESSAGE_MAPPING",
    "WS_CHANNEL_PROPERTY_HTTP_PROXY_SETTING_MODE",
    "WS_CHANNEL_PROPERTY_HTTP_PROXY_SPN",
    "WS_CHANNEL_PROPERTY_HTTP_REDIRECT_CALLBACK_CONTEXT",
    "WS_CHANNEL_PROPERTY_HTTP_SERVER_SPN",
    "WS_CHANNEL_PROPERTY_ID",
    "WS_CHANNEL_PROPERTY_IP_VERSION",
    "WS_CHANNEL_PROPERTY_IS_SESSION_SHUT_DOWN",
    "WS_CHANNEL_PROPERTY_KEEP_ALIVE_INTERVAL",
    "WS_CHANNEL_PROPERTY_KEEP_ALIVE_TIME",
    "WS_CHANNEL_PROPERTY_MAX_BUFFERED_MESSAGE_SIZE",
    "WS_CHANNEL_PROPERTY_MAX_HTTP_REQUEST_HEADERS_BUFFER_SIZE",
    "WS_CHANNEL_PROPERTY_MAX_HTTP_SERVER_CONNECTIONS",
    "WS_CHANNEL_PROPERTY_MAX_SESSION_DICTIONARY_SIZE",
    "WS_CHANNEL_PROPERTY_MAX_STREAMED_FLUSH_SIZE",
    "WS_CHANNEL_PROPERTY_MAX_STREAMED_MESSAGE_SIZE",
    "WS_CHANNEL_PROPERTY_MAX_STREAMED_START_SIZE",
    "WS_CHANNEL_PROPERTY_MULTICAST_HOPS",
    "WS_CHANNEL_PROPERTY_MULTICAST_INTERFACE",
    "WS_CHANNEL_PROPERTY_NO_DELAY",
    "WS_CHANNEL_PROPERTY_PROTECTION_LEVEL",
    "WS_CHANNEL_PROPERTY_RECEIVE_RESPONSE_TIMEOUT",
    "WS_CHANNEL_PROPERTY_RECEIVE_TIMEOUT",
    "WS_CHANNEL_PROPERTY_REMOTE_ADDRESS",
    "WS_CHANNEL_PROPERTY_REMOTE_IP_ADDRESS",
    "WS_CHANNEL_PROPERTY_RESOLVE_TIMEOUT",
    "WS_CHANNEL_PROPERTY_SEND_KEEP_ALIVES",
    "WS_CHANNEL_PROPERTY_SEND_TIMEOUT",
    "WS_CHANNEL_PROPERTY_STATE",
    "WS_CHANNEL_PROPERTY_TRANSFER_MODE",
    "WS_CHANNEL_PROPERTY_TRANSPORT_URL",
    "WS_CHANNEL_PROPERTY_TRIM_BUFFERED_MESSAGE_SIZE",
    "WS_CHANNEL_STATE",
    "WS_CHANNEL_STATE_ACCEPTING",
    "WS_CHANNEL_STATE_CLOSED",
    "WS_CHANNEL_STATE_CLOSING",
    "WS_CHANNEL_STATE_CREATED",
    "WS_CHANNEL_STATE_FAULTED",
    "WS_CHANNEL_STATE_OPEN",
    "WS_CHANNEL_STATE_OPENING",
    "WS_CHANNEL_TYPE",
    "WS_CHANNEL_TYPE_DUPLEX",
    "WS_CHANNEL_TYPE_DUPLEX_SESSION",
    "WS_CHANNEL_TYPE_INPUT",
    "WS_CHANNEL_TYPE_INPUT_SESSION",
    "WS_CHANNEL_TYPE_OUTPUT",
    "WS_CHANNEL_TYPE_OUTPUT_SESSION",
    "WS_CHANNEL_TYPE_REPLY",
    "WS_CHANNEL_TYPE_REQUEST",
    "WS_CHANNEL_TYPE_SESSION",
    "WS_CHARSET",
    "WS_CHARSET_AUTO",
    "WS_CHARSET_UTF16BE",
    "WS_CHARSET_UTF16LE",
    "WS_CHARSET_UTF8",
    "WS_CHAR_ARRAY_DESCRIPTION",
    "WS_CHAR_ARRAY_TYPE",
    "WS_CLOSE_CHANNEL_CALLBACK",
    "WS_CLOSE_LISTENER_CALLBACK",
    "WS_CONTRACT_DESCRIPTION",
    "WS_COOKIE_MODE",
    "WS_CREATE_CHANNEL_CALLBACK",
    "WS_CREATE_CHANNEL_FOR_LISTENER_CALLBACK",
    "WS_CREATE_DECODER_CALLBACK",
    "WS_CREATE_ENCODER_CALLBACK",
    "WS_CREATE_LISTENER_CALLBACK",
    "WS_CUSTOM_CERT_CREDENTIAL",
    "WS_CUSTOM_CERT_CREDENTIAL_TYPE",
    "WS_CUSTOM_CHANNEL_BINDING",
    "WS_CUSTOM_CHANNEL_CALLBACKS",
    "WS_CUSTOM_HTTP_PROXY",
    "WS_CUSTOM_LISTENER_CALLBACKS",
    "WS_CUSTOM_TYPE",
    "WS_CUSTOM_TYPE_DESCRIPTION",
    "WS_DATETIME",
    "WS_DATETIME_DESCRIPTION",
    "WS_DATETIME_FORMAT",
    "WS_DATETIME_FORMAT_LOCAL",
    "WS_DATETIME_FORMAT_NONE",
    "WS_DATETIME_FORMAT_UTC",
    "WS_DATETIME_TYPE",
    "WS_DATETIME_VALUE_TYPE",
    "WS_DECIMAL_DESCRIPTION",
    "WS_DECIMAL_TYPE",
    "WS_DECIMAL_VALUE_TYPE",
    "WS_DECODER_DECODE_CALLBACK",
    "WS_DECODER_END_CALLBACK",
    "WS_DECODER_GET_CONTENT_TYPE_CALLBACK",
    "WS_DECODER_START_CALLBACK",
    "WS_DEFAULT_VALUE",
    "WS_DEFAULT_WINDOWS_INTEGRATED_AUTH_CREDENTIAL",
    "WS_DEFAULT_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_TYPE",
    "WS_DESCRIPTION_TYPE",
    "WS_DISALLOWED_USER_AGENT_SUBSTRINGS",
    "WS_DNS_ENDPOINT_IDENTITY",
    "WS_DNS_ENDPOINT_IDENTITY_TYPE",
    "WS_DOUBLE_DESCRIPTION",
    "WS_DOUBLE_TYPE",
    "WS_DOUBLE_VALUE_TYPE",
    "WS_DUPLICATE_MESSAGE",
    "WS_DURATION",
    "WS_DURATION_COMPARISON_CALLBACK",
    "WS_DURATION_DESCRIPTION",
    "WS_DURATION_TYPE",
    "WS_DURATION_VALUE_TYPE",
    "WS_DYNAMIC_STRING_CALLBACK",
    "WS_ELEMENT_CHOICE_FIELD_MAPPING",
    "WS_ELEMENT_CONTENT_TYPE_MAPPING",
    "WS_ELEMENT_DESCRIPTION",
    "WS_ELEMENT_FIELD_MAPPING",
    "WS_ELEMENT_TYPE_MAPPING",
    "WS_ENCODER_ENCODE_CALLBACK",
    "WS_ENCODER_END_CALLBACK",
    "WS_ENCODER_GET_CONTENT_TYPE_CALLBACK",
    "WS_ENCODER_START_CALLBACK",
    "WS_ENCODING",
    "WS_ENCODING_RAW",
    "WS_ENCODING_XML_BINARY_1",
    "WS_ENCODING_XML_BINARY_SESSION_1",
    "WS_ENCODING_XML_MTOM_UTF16BE",
    "WS_ENCODING_XML_MTOM_UTF16LE",
    "WS_ENCODING_XML_MTOM_UTF8",
    "WS_ENCODING_XML_UTF16BE",
    "WS_ENCODING_XML_UTF16LE",
    "WS_ENCODING_XML_UTF8",
    "WS_ENDPOINT_ADDRESS",
    "WS_ENDPOINT_ADDRESS_DESCRIPTION",
    "WS_ENDPOINT_ADDRESS_EXTENSION_METADATA_ADDRESS",
    "WS_ENDPOINT_ADDRESS_EXTENSION_TYPE",
    "WS_ENDPOINT_ADDRESS_TYPE",
    "WS_ENDPOINT_IDENTITY",
    "WS_ENDPOINT_IDENTITY_TYPE",
    "WS_ENDPOINT_POLICY_EXTENSION",
    "WS_ENDPOINT_POLICY_EXTENSION_TYPE",
    "WS_ENUM_DESCRIPTION",
    "WS_ENUM_TYPE",
    "WS_ENUM_VALUE",
    "WS_ENVELOPE_VERSION",
    "WS_ENVELOPE_VERSION_NONE",
    "WS_ENVELOPE_VERSION_SOAP_1_1",
    "WS_ENVELOPE_VERSION_SOAP_1_2",
    "WS_ERROR",
    "WS_ERROR_PROPERTY",
    "WS_ERROR_PROPERTY_ID",
    "WS_ERROR_PROPERTY_LANGID",
    "WS_ERROR_PROPERTY_ORIGINAL_ERROR_CODE",
    "WS_ERROR_PROPERTY_STRING_COUNT",
    "WS_EXCEPTION_CODE",
    "WS_EXCEPTION_CODE_INTERNAL_FAILURE",
    "WS_EXCEPTION_CODE_USAGE_FAILURE",
    "WS_EXCLUSIVE_WITH_COMMENTS_XML_CANONICALIZATION_ALGORITHM",
    "WS_EXCLUSIVE_XML_CANONICALIZATION_ALGORITHM",
    "WS_EXTENDED_PROTECTION_POLICY",
    "WS_EXTENDED_PROTECTION_POLICY_ALWAYS",
    "WS_EXTENDED_PROTECTION_POLICY_NEVER",
    "WS_EXTENDED_PROTECTION_POLICY_WHEN_SUPPORTED",
    "WS_EXTENDED_PROTECTION_SCENARIO",
    "WS_EXTENDED_PROTECTION_SCENARIO_BOUND_SERVER",
    "WS_EXTENDED_PROTECTION_SCENARIO_TERMINATED_SSL",
    "WS_FAULT",
    "WS_FAULT_CODE",
    "WS_FAULT_DESCRIPTION",
    "WS_FAULT_DETAIL_DESCRIPTION",
    "WS_FAULT_DISCLOSURE",
    "WS_FAULT_ERROR_PROPERTY_ACTION",
    "WS_FAULT_ERROR_PROPERTY_FAULT",
    "WS_FAULT_ERROR_PROPERTY_HEADER",
    "WS_FAULT_ERROR_PROPERTY_ID",
    "WS_FAULT_MESSAGE",
    "WS_FAULT_REASON",
    "WS_FAULT_TO_HEADER",
    "WS_FAULT_TYPE",
    "WS_FIELD_DESCRIPTION",
    "WS_FIELD_MAPPING",
    "WS_FIELD_NILLABLE",
    "WS_FIELD_NILLABLE_ITEM",
    "WS_FIELD_OPTIONAL",
    "WS_FIELD_OTHER_NAMESPACE",
    "WS_FIELD_POINTER",
    "WS_FLOAT_DESCRIPTION",
    "WS_FLOAT_TYPE",
    "WS_FLOAT_VALUE_TYPE",
    "WS_FREE_CHANNEL_CALLBACK",
    "WS_FREE_DECODER_CALLBACK",
    "WS_FREE_ENCODER_CALLBACK",
    "WS_FREE_LISTENER_CALLBACK",
    "WS_FROM_HEADER",
    "WS_FULL_FAULT_DISCLOSURE",
    "WS_GET_CERT_CALLBACK",
    "WS_GET_CHANNEL_PROPERTY_CALLBACK",
    "WS_GET_LISTENER_PROPERTY_CALLBACK",
    "WS_GUID_DESCRIPTION",
    "WS_GUID_TYPE",
    "WS_GUID_VALUE_TYPE",
    "WS_HEADER_TYPE",
    "WS_HEAP",
    "WS_HEAP_PROPERTIES",
    "WS_HEAP_PROPERTY",
    "WS_HEAP_PROPERTY_ACTUAL_SIZE",
    "WS_HEAP_PROPERTY_ID",
    "WS_HEAP_PROPERTY_MAX_SIZE",
    "WS_HEAP_PROPERTY_REQUESTED_SIZE",
    "WS_HEAP_PROPERTY_TRIM_SIZE",
    "WS_HOST_NAMES",
    "WS_HTTPS_URL",
    "WS_HTTP_BINDING_TEMPLATE",
    "WS_HTTP_BINDING_TEMPLATE_TYPE",
    "WS_HTTP_CHANNEL_BINDING",
    "WS_HTTP_HEADER_AUTH_BINDING_TEMPLATE",
    "WS_HTTP_HEADER_AUTH_BINDING_TEMPLATE_TYPE",
    "WS_HTTP_HEADER_AUTH_POLICY_DESCRIPTION",
    "WS_HTTP_HEADER_AUTH_SCHEME_BASIC",
    "WS_HTTP_HEADER_AUTH_SCHEME_DIGEST",
    "WS_HTTP_HEADER_AUTH_SCHEME_NEGOTIATE",
    "WS_HTTP_HEADER_AUTH_SCHEME_NONE",
    "WS_HTTP_HEADER_AUTH_SCHEME_NTLM",
    "WS_HTTP_HEADER_AUTH_SCHEME_PASSPORT",
    "WS_HTTP_HEADER_AUTH_SECURITY_BINDING",
    "WS_HTTP_HEADER_AUTH_SECURITY_BINDING_CONSTRAINT",
    "WS_HTTP_HEADER_AUTH_SECURITY_BINDING_CONSTRAINT_TYPE",
    "WS_HTTP_HEADER_AUTH_SECURITY_BINDING_POLICY_DESCRIPTION",
    "WS_HTTP_HEADER_AUTH_SECURITY_BINDING_TEMPLATE",
    "WS_HTTP_HEADER_AUTH_SECURITY_BINDING_TYPE",
    "WS_HTTP_HEADER_AUTH_TARGET",
    "WS_HTTP_HEADER_AUTH_TARGET_PROXY",
    "WS_HTTP_HEADER_AUTH_TARGET_SERVICE",
    "WS_HTTP_HEADER_MAPPING",
    "WS_HTTP_HEADER_MAPPING_COMMA_SEPARATOR",
    "WS_HTTP_HEADER_MAPPING_QUOTED_VALUE",
    "WS_HTTP_HEADER_MAPPING_SEMICOLON_SEPARATOR",
    "WS_HTTP_MESSAGE_MAPPING",
    "WS_HTTP_POLICY_DESCRIPTION",
    "WS_HTTP_PROXY_SETTING_MODE",
    "WS_HTTP_PROXY_SETTING_MODE_AUTO",
    "WS_HTTP_PROXY_SETTING_MODE_CUSTOM",
    "WS_HTTP_PROXY_SETTING_MODE_NONE",
    "WS_HTTP_REDIRECT_CALLBACK",
    "WS_HTTP_REDIRECT_CALLBACK_CONTEXT",
    "WS_HTTP_REQUEST_MAPPING_VERB",
    "WS_HTTP_RESPONSE_MAPPING_STATUS_CODE",
    "WS_HTTP_RESPONSE_MAPPING_STATUS_TEXT",
    "WS_HTTP_SSL_BINDING_TEMPLATE",
    "WS_HTTP_SSL_BINDING_TEMPLATE_TYPE",
    "WS_HTTP_SSL_HEADER_AUTH_BINDING_TEMPLATE",
    "WS_HTTP_SSL_HEADER_AUTH_BINDING_TEMPLATE_TYPE",
    "WS_HTTP_SSL_HEADER_AUTH_POLICY_DESCRIPTION",
    "WS_HTTP_SSL_KERBEROS_APREQ_BINDING_TEMPLATE",
    "WS_HTTP_SSL_KERBEROS_APREQ_BINDING_TEMPLATE_TYPE",
    "WS_HTTP_SSL_KERBEROS_APREQ_POLICY_DESCRIPTION",
    "WS_HTTP_SSL_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE",
    "WS_HTTP_SSL_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE_TYPE",
    "WS_HTTP_SSL_KERBEROS_APREQ_SECURITY_CONTEXT_POLICY_DESCRIPTION",
    "WS_HTTP_SSL_POLICY_DESCRIPTION",
    "WS_HTTP_SSL_USERNAME_BINDING_TEMPLATE",
    "WS_HTTP_SSL_USERNAME_BINDING_TEMPLATE_TYPE",
    "WS_HTTP_SSL_USERNAME_POLICY_DESCRIPTION",
    "WS_HTTP_SSL_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE",
    "WS_HTTP_SSL_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE_TYPE",
    "WS_HTTP_SSL_USERNAME_SECURITY_CONTEXT_POLICY_DESCRIPTION",
    "WS_HTTP_URL",
    "WS_INCLUSIVE_WITH_COMMENTS_XML_CANONICALIZATION_ALGORITHM",
    "WS_INCLUSIVE_XML_CANONICALIZATION_ALGORITHM",
    "WS_INT16_DESCRIPTION",
    "WS_INT16_TYPE",
    "WS_INT16_VALUE_TYPE",
    "WS_INT32_DESCRIPTION",
    "WS_INT32_TYPE",
    "WS_INT32_VALUE_TYPE",
    "WS_INT64_DESCRIPTION",
    "WS_INT64_TYPE",
    "WS_INT64_VALUE_TYPE",
    "WS_INT8_DESCRIPTION",
    "WS_INT8_TYPE",
    "WS_INT8_VALUE_TYPE",
    "WS_IP_VERSION",
    "WS_IP_VERSION_4",
    "WS_IP_VERSION_6",
    "WS_IP_VERSION_AUTO",
    "WS_ISSUED_TOKEN_MESSAGE_SECURITY_BINDING_CONSTRAINT",
    "WS_ISSUED_TOKEN_MESSAGE_SECURITY_BINDING_CONSTRAINT_TYPE",
    "WS_IS_DEFAULT_VALUE_CALLBACK",
    "WS_ITEM_RANGE",
    "WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING",
    "WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_CONSTRAINT",
    "WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_CONSTRAINT_TYPE",
    "WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION",
    "WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_TEMPLATE",
    "WS_KERBEROS_APREQ_MESSAGE_SECURITY_BINDING_TYPE",
    "WS_LISTENER",
    "WS_LISTENER_PROPERTIES",
    "WS_LISTENER_PROPERTY",
    "WS_LISTENER_PROPERTY_ASYNC_CALLBACK_MODEL",
    "WS_LISTENER_PROPERTY_CHANNEL_BINDING",
    "WS_LISTENER_PROPERTY_CHANNEL_TYPE",
    "WS_LISTENER_PROPERTY_CLOSE_TIMEOUT",
    "WS_LISTENER_PROPERTY_CONNECT_TIMEOUT",
    "WS_LISTENER_PROPERTY_CUSTOM_LISTENER_CALLBACKS",
    "WS_LISTENER_PROPERTY_CUSTOM_LISTENER_INSTANCE",
    "WS_LISTENER_PROPERTY_CUSTOM_LISTENER_PARAMETERS",
    "WS_LISTENER_PROPERTY_DISALLOWED_USER_AGENT",
    "WS_LISTENER_PROPERTY_ID",
    "WS_LISTENER_PROPERTY_IP_VERSION",
    "WS_LISTENER_PROPERTY_IS_MULTICAST",
    "WS_LISTENER_PROPERTY_LISTEN_BACKLOG",
    "WS_LISTENER_PROPERTY_MULTICAST_INTERFACES",
    "WS_LISTENER_PROPERTY_MULTICAST_LOOPBACK",
    "WS_LISTENER_PROPERTY_STATE",
    "WS_LISTENER_PROPERTY_TO_HEADER_MATCHING_OPTIONS",
    "WS_LISTENER_PROPERTY_TRANSPORT_URL_MATCHING_OPTIONS",
    "WS_LISTENER_STATE",
    "WS_LISTENER_STATE_CLOSED",
    "WS_LISTENER_STATE_CLOSING",
    "WS_LISTENER_STATE_CREATED",
    "WS_LISTENER_STATE_FAULTED",
    "WS_LISTENER_STATE_OPEN",
    "WS_LISTENER_STATE_OPENING",
    "WS_LONG_CALLBACK",
    "WS_MANUAL_COOKIE_MODE",
    "WS_MATCH_URL_DNS_FULLY_QUALIFIED_HOST",
    "WS_MATCH_URL_DNS_HOST",
    "WS_MATCH_URL_EXACT_PATH",
    "WS_MATCH_URL_HOST_ADDRESSES",
    "WS_MATCH_URL_LOCAL_HOST",
    "WS_MATCH_URL_NETBIOS_HOST",
    "WS_MATCH_URL_NO_QUERY",
    "WS_MATCH_URL_PORT",
    "WS_MATCH_URL_PREFIX_PATH",
    "WS_MATCH_URL_THIS_HOST",
    "WS_MESSAGE",
    "WS_MESSAGE_DESCRIPTION",
    "WS_MESSAGE_DONE_CALLBACK",
    "WS_MESSAGE_ID_HEADER",
    "WS_MESSAGE_INITIALIZATION",
    "WS_MESSAGE_PROPERTIES",
    "WS_MESSAGE_PROPERTY",
    "WS_MESSAGE_PROPERTY_ADDRESSING_VERSION",
    "WS_MESSAGE_PROPERTY_BODY_READER",
    "WS_MESSAGE_PROPERTY_BODY_WRITER",
    "WS_MESSAGE_PROPERTY_ENCODED_CERT",
    "WS_MESSAGE_PROPERTY_ENVELOPE_VERSION",
    "WS_MESSAGE_PROPERTY_HEADER_BUFFER",
    "WS_MESSAGE_PROPERTY_HEADER_POSITION",
    "WS_MESSAGE_PROPERTY_HEAP",
    "WS_MESSAGE_PROPERTY_HEAP_PROPERTIES",
    "WS_MESSAGE_PROPERTY_HTTP_HEADER_AUTH_WINDOWS_TOKEN",
    "WS_MESSAGE_PROPERTY_ID",
    "WS_MESSAGE_PROPERTY_IS_ADDRESSED",
    "WS_MESSAGE_PROPERTY_IS_FAULT",
    "WS_MESSAGE_PROPERTY_MAX_PROCESSED_HEADERS",
    "WS_MESSAGE_PROPERTY_MESSAGE_SECURITY_WINDOWS_TOKEN",
    "WS_MESSAGE_PROPERTY_PROTECTION_LEVEL",
    "WS_MESSAGE_PROPERTY_SAML_ASSERTION",
    "WS_MESSAGE_PROPERTY_SECURITY_CONTEXT",
    "WS_MESSAGE_PROPERTY_STATE",
    "WS_MESSAGE_PROPERTY_TRANSPORT_SECURITY_WINDOWS_TOKEN",
    "WS_MESSAGE_PROPERTY_USERNAME",
    "WS_MESSAGE_PROPERTY_XML_READER_PROPERTIES",
    "WS_MESSAGE_PROPERTY_XML_WRITER_PROPERTIES",
    "WS_MESSAGE_SECURITY_USAGE",
    "WS_MESSAGE_STATE",
    "WS_MESSAGE_STATE_DONE",
    "WS_MESSAGE_STATE_EMPTY",
    "WS_MESSAGE_STATE_INITIALIZED",
    "WS_MESSAGE_STATE_READING",
    "WS_MESSAGE_STATE_WRITING",
    "WS_METADATA",
    "WS_METADATA_ENDPOINT",
    "WS_METADATA_ENDPOINTS",
    "WS_METADATA_EXCHANGE_TYPE",
    "WS_METADATA_EXCHANGE_TYPE_HTTP_GET",
    "WS_METADATA_EXCHANGE_TYPE_MEX",
    "WS_METADATA_EXCHANGE_TYPE_NONE",
    "WS_METADATA_PROPERTY",
    "WS_METADATA_PROPERTY_HEAP_PROPERTIES",
    "WS_METADATA_PROPERTY_HEAP_REQUESTED_SIZE",
    "WS_METADATA_PROPERTY_HOST_NAMES",
    "WS_METADATA_PROPERTY_ID",
    "WS_METADATA_PROPERTY_MAX_DOCUMENTS",
    "WS_METADATA_PROPERTY_POLICY_PROPERTIES",
    "WS_METADATA_PROPERTY_STATE",
    "WS_METADATA_PROPERTY_VERIFY_HOST_NAMES",
    "WS_METADATA_STATE",
    "WS_METADATA_STATE_CREATED",
    "WS_METADATA_STATE_FAULTED",
    "WS_METADATA_STATE_RESOLVED",
    "WS_MINIMAL_FAULT_DISCLOSURE",
    "WS_MOVE_TO",
    "WS_MOVE_TO_BOF",
    "WS_MOVE_TO_CHILD_ELEMENT",
    "WS_MOVE_TO_CHILD_NODE",
    "WS_MOVE_TO_END_ELEMENT",
    "WS_MOVE_TO_EOF",
    "WS_MOVE_TO_FIRST_NODE",
    "WS_MOVE_TO_NEXT_ELEMENT",
    "WS_MOVE_TO_NEXT_NODE",
    "WS_MOVE_TO_PARENT_ELEMENT",
    "WS_MOVE_TO_PREVIOUS_ELEMENT",
    "WS_MOVE_TO_PREVIOUS_NODE",
    "WS_MOVE_TO_ROOT_ELEMENT",
    "WS_MUST_UNDERSTAND_HEADER_ATTRIBUTE",
    "WS_NAMEDPIPE_CHANNEL_BINDING",
    "WS_NAMEDPIPE_SSPI_TRANSPORT_SECURITY_BINDING",
    "WS_NAMEDPIPE_SSPI_TRANSPORT_SECURITY_BINDING_TYPE",
    "WS_NCRYPT_ASYMMETRIC_SECURITY_KEY_HANDLE",
    "WS_NCRYPT_ASYMMETRIC_SECURITY_KEY_HANDLE_TYPE",
    "WS_NETPIPE_URL",
    "WS_NETTCP_URL",
    "WS_NON_RPC_LITERAL_OPERATION",
    "WS_NO_FIELD_MAPPING",
    "WS_OPAQUE_WINDOWS_INTEGRATED_AUTH_CREDENTIAL",
    "WS_OPAQUE_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_TYPE",
    "WS_OPEN_CHANNEL_CALLBACK",
    "WS_OPEN_LISTENER_CALLBACK",
    "WS_OPERATION_CANCEL_CALLBACK",
    "WS_OPERATION_CONTEXT",
    "WS_OPERATION_CONTEXT_PROPERTY_CHANNEL",
    "WS_OPERATION_CONTEXT_PROPERTY_CHANNEL_USER_STATE",
    "WS_OPERATION_CONTEXT_PROPERTY_CONTRACT_DESCRIPTION",
    "WS_OPERATION_CONTEXT_PROPERTY_ENDPOINT_ADDRESS",
    "WS_OPERATION_CONTEXT_PROPERTY_HEAP",
    "WS_OPERATION_CONTEXT_PROPERTY_HOST_USER_STATE",
    "WS_OPERATION_CONTEXT_PROPERTY_ID",
    "WS_OPERATION_CONTEXT_PROPERTY_INPUT_MESSAGE",
    "WS_OPERATION_CONTEXT_PROPERTY_LISTENER",
    "WS_OPERATION_CONTEXT_PROPERTY_OUTPUT_MESSAGE",
    "WS_OPERATION_DESCRIPTION",
    "WS_OPERATION_FREE_STATE_CALLBACK",
    "WS_OPERATION_STYLE",
    "WS_PARAMETER_DESCRIPTION",
    "WS_PARAMETER_TYPE",
    "WS_PARAMETER_TYPE_ARRAY",
    "WS_PARAMETER_TYPE_ARRAY_COUNT",
    "WS_PARAMETER_TYPE_MESSAGES",
    "WS_PARAMETER_TYPE_NORMAL",
    "WS_POLICY",
    "WS_POLICY_CONSTRAINTS",
    "WS_POLICY_EXTENSION",
    "WS_POLICY_EXTENSION_TYPE",
    "WS_POLICY_PROPERTIES",
    "WS_POLICY_PROPERTY",
    "WS_POLICY_PROPERTY_ID",
    "WS_POLICY_PROPERTY_MAX_ALTERNATIVES",
    "WS_POLICY_PROPERTY_MAX_DEPTH",
    "WS_POLICY_PROPERTY_MAX_EXTENSIONS",
    "WS_POLICY_PROPERTY_STATE",
    "WS_POLICY_STATE",
    "WS_POLICY_STATE_CREATED",
    "WS_POLICY_STATE_FAULTED",
    "WS_PROTECTION_LEVEL",
    "WS_PROTECTION_LEVEL_NONE",
    "WS_PROTECTION_LEVEL_SIGN",
    "WS_PROTECTION_LEVEL_SIGN_AND_ENCRYPT",
    "WS_PROXY_FAULT_LANG_ID",
    "WS_PROXY_MESSAGE_CALLBACK",
    "WS_PROXY_MESSAGE_CALLBACK_CONTEXT",
    "WS_PROXY_PROPERTY",
    "WS_PROXY_PROPERTY_CALL_TIMEOUT",
    "WS_PROXY_PROPERTY_ID",
    "WS_PROXY_PROPERTY_MAX_CALL_POOL_SIZE",
    "WS_PROXY_PROPERTY_MAX_CLOSE_TIMEOUT",
    "WS_PROXY_PROPERTY_MAX_PENDING_CALLS",
    "WS_PROXY_PROPERTY_MESSAGE_PROPERTIES",
    "WS_PROXY_PROPERTY_STATE",
    "WS_PULL_BYTES_CALLBACK",
    "WS_PUSH_BYTES_CALLBACK",
    "WS_RAW_SYMMETRIC_SECURITY_KEY_HANDLE",
    "WS_RAW_SYMMETRIC_SECURITY_KEY_HANDLE_TYPE",
    "WS_READ_CALLBACK",
    "WS_READ_MESSAGE_END_CALLBACK",
    "WS_READ_MESSAGE_START_CALLBACK",
    "WS_READ_NILLABLE_POINTER",
    "WS_READ_NILLABLE_VALUE",
    "WS_READ_OPTION",
    "WS_READ_OPTIONAL_POINTER",
    "WS_READ_REQUIRED_POINTER",
    "WS_READ_REQUIRED_VALUE",
    "WS_READ_TYPE_CALLBACK",
    "WS_RECEIVE_OPTION",
    "WS_RECEIVE_OPTIONAL_MESSAGE",
    "WS_RECEIVE_REQUIRED_MESSAGE",
    "WS_RELATES_TO_HEADER",
    "WS_RELAY_HEADER_ATTRIBUTE",
    "WS_REPEATING_ANY_ELEMENT_FIELD_MAPPING",
    "WS_REPEATING_ELEMENT_CHOICE_FIELD_MAPPING",
    "WS_REPEATING_ELEMENT_FIELD_MAPPING",
    "WS_REPEATING_HEADER",
    "WS_REPEATING_HEADER_OPTION",
    "WS_REPLY_MESSAGE",
    "WS_REPLY_TO_HEADER",
    "WS_REQUEST_MESSAGE",
    "WS_REQUEST_SECURITY_TOKEN_ACTION",
    "WS_REQUEST_SECURITY_TOKEN_ACTION_ISSUE",
    "WS_REQUEST_SECURITY_TOKEN_ACTION_NEW_CONTEXT",
    "WS_REQUEST_SECURITY_TOKEN_ACTION_RENEW_CONTEXT",
    "WS_REQUEST_SECURITY_TOKEN_PROPERTY",
    "WS_REQUEST_SECURITY_TOKEN_PROPERTY_APPLIES_TO",
    "WS_REQUEST_SECURITY_TOKEN_PROPERTY_BEARER_KEY_TYPE_VERSION",
    "WS_REQUEST_SECURITY_TOKEN_PROPERTY_CONSTRAINT",
    "WS_REQUEST_SECURITY_TOKEN_PROPERTY_EXISTING_TOKEN",
    "WS_REQUEST_SECURITY_TOKEN_PROPERTY_ID",
    "WS_REQUEST_SECURITY_TOKEN_PROPERTY_ISSUED_TOKEN_KEY_ENTROPY",
    "WS_REQUEST_SECURITY_TOKEN_PROPERTY_ISSUED_TOKEN_KEY_SIZE",
    "WS_REQUEST_SECURITY_TOKEN_PROPERTY_ISSUED_TOKEN_KEY_TYPE",
    "WS_REQUEST_SECURITY_TOKEN_PROPERTY_ISSUED_TOKEN_TYPE",
    "WS_REQUEST_SECURITY_TOKEN_PROPERTY_LOCAL_REQUEST_PARAMETERS",
    "WS_REQUEST_SECURITY_TOKEN_PROPERTY_MESSAGE_PROPERTIES",
    "WS_REQUEST_SECURITY_TOKEN_PROPERTY_REQUEST_ACTION",
    "WS_REQUEST_SECURITY_TOKEN_PROPERTY_SECURE_CONVERSATION_VERSION",
    "WS_REQUEST_SECURITY_TOKEN_PROPERTY_SERVICE_REQUEST_PARAMETERS",
    "WS_REQUEST_SECURITY_TOKEN_PROPERTY_TRUST_VERSION",
    "WS_RESET_CHANNEL_CALLBACK",
    "WS_RESET_LISTENER_CALLBACK",
    "WS_RPC_LITERAL_OPERATION",
    "WS_RSA_ENDPOINT_IDENTITY",
    "WS_RSA_ENDPOINT_IDENTITY_TYPE",
    "WS_SAML_AUTHENTICATOR",
    "WS_SAML_AUTHENTICATOR_TYPE",
    "WS_SAML_MESSAGE_SECURITY_BINDING",
    "WS_SAML_MESSAGE_SECURITY_BINDING_TYPE",
    "WS_SECURE_CONVERSATION_VERSION",
    "WS_SECURE_CONVERSATION_VERSION_1_3",
    "WS_SECURE_CONVERSATION_VERSION_FEBRUARY_2005",
    "WS_SECURE_PROTOCOL",
    "WS_SECURE_PROTOCOL_SSL2",
    "WS_SECURE_PROTOCOL_SSL3",
    "WS_SECURE_PROTOCOL_TLS1_0",
    "WS_SECURE_PROTOCOL_TLS1_1",
    "WS_SECURE_PROTOCOL_TLS1_2",
    "WS_SECURITY_ALGORITHM_ASYMMETRIC_KEYWRAP_RSA_1_5",
    "WS_SECURITY_ALGORITHM_ASYMMETRIC_KEYWRAP_RSA_OAEP",
    "WS_SECURITY_ALGORITHM_ASYMMETRIC_SIGNATURE_DSA_SHA1",
    "WS_SECURITY_ALGORITHM_ASYMMETRIC_SIGNATURE_RSA_SHA1",
    "WS_SECURITY_ALGORITHM_ASYMMETRIC_SIGNATURE_RSA_SHA_256",
    "WS_SECURITY_ALGORITHM_ASYMMETRIC_SIGNATURE_RSA_SHA_384",
    "WS_SECURITY_ALGORITHM_ASYMMETRIC_SIGNATURE_RSA_SHA_512",
    "WS_SECURITY_ALGORITHM_CANONICALIZATION_EXCLUSIVE",
    "WS_SECURITY_ALGORITHM_CANONICALIZATION_EXCLUSIVE_WITH_COMMENTS",
    "WS_SECURITY_ALGORITHM_DEFAULT",
    "WS_SECURITY_ALGORITHM_DIGEST_SHA1",
    "WS_SECURITY_ALGORITHM_DIGEST_SHA_256",
    "WS_SECURITY_ALGORITHM_DIGEST_SHA_384",
    "WS_SECURITY_ALGORITHM_DIGEST_SHA_512",
    "WS_SECURITY_ALGORITHM_ID",
    "WS_SECURITY_ALGORITHM_KEY_DERIVATION_P_SHA1",
    "WS_SECURITY_ALGORITHM_PROPERTY",
    "WS_SECURITY_ALGORITHM_PROPERTY_ID",
    "WS_SECURITY_ALGORITHM_SUITE",
    "WS_SECURITY_ALGORITHM_SUITE_NAME",
    "WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC128",
    "WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC128_RSA15",
    "WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC128_SHA256",
    "WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC128_SHA256_RSA15",
    "WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC192",
    "WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC192_RSA15",
    "WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC192_SHA256",
    "WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC192_SHA256_RSA15",
    "WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC256",
    "WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC256_RSA15",
    "WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC256_SHA256",
    "WS_SECURITY_ALGORITHM_SUITE_NAME_BASIC256_SHA256_RSA15",
    "WS_SECURITY_ALGORITHM_SYMMETRIC_SIGNATURE_HMAC_SHA1",
    "WS_SECURITY_ALGORITHM_SYMMETRIC_SIGNATURE_HMAC_SHA_256",
    "WS_SECURITY_ALGORITHM_SYMMETRIC_SIGNATURE_HMAC_SHA_384",
    "WS_SECURITY_ALGORITHM_SYMMETRIC_SIGNATURE_HMAC_SHA_512",
    "WS_SECURITY_BEARER_KEY_TYPE_VERSION",
    "WS_SECURITY_BEARER_KEY_TYPE_VERSION_1_3_ERRATA_01",
    "WS_SECURITY_BEARER_KEY_TYPE_VERSION_1_3_ORIGINAL_SCHEMA",
    "WS_SECURITY_BEARER_KEY_TYPE_VERSION_1_3_ORIGINAL_SPECIFICATION",
    "WS_SECURITY_BINDING",
    "WS_SECURITY_BINDING_CONSTRAINT",
    "WS_SECURITY_BINDING_CONSTRAINT_TYPE",
    "WS_SECURITY_BINDING_PROPERTIES",
    "WS_SECURITY_BINDING_PROPERTY",
    "WS_SECURITY_BINDING_PROPERTY_ALLOWED_IMPERSONATION_LEVEL",
    "WS_SECURITY_BINDING_PROPERTY_ALLOW_ANONYMOUS_CLIENTS",
    "WS_SECURITY_BINDING_PROPERTY_CERTIFICATE_VALIDATION_CALLBACK_CONTEXT",
    "WS_SECURITY_BINDING_PROPERTY_CERT_FAILURES_TO_IGNORE",
    "WS_SECURITY_BINDING_PROPERTY_CONSTRAINT",
    "WS_SECURITY_BINDING_PROPERTY_DISABLE_CERT_REVOCATION_CHECK",
    "WS_SECURITY_BINDING_PROPERTY_DISALLOWED_SECURE_PROTOCOLS",
    "WS_SECURITY_BINDING_PROPERTY_HTTP_HEADER_AUTH_BASIC_REALM",
    "WS_SECURITY_BINDING_PROPERTY_HTTP_HEADER_AUTH_DIGEST_DOMAIN",
    "WS_SECURITY_BINDING_PROPERTY_HTTP_HEADER_AUTH_DIGEST_REALM",
    "WS_SECURITY_BINDING_PROPERTY_HTTP_HEADER_AUTH_SCHEME",
    "WS_SECURITY_BINDING_PROPERTY_HTTP_HEADER_AUTH_TARGET",
    "WS_SECURITY_BINDING_PROPERTY_ID",
    "WS_SECURITY_BINDING_PROPERTY_MESSAGE_PROPERTIES",
    "WS_SECURITY_BINDING_PROPERTY_REQUIRE_SERVER_AUTH",
    "WS_SECURITY_BINDING_PROPERTY_REQUIRE_SSL_CLIENT_CERT",
    "WS_SECURITY_BINDING_PROPERTY_SECURE_CONVERSATION_VERSION",
    "WS_SECURITY_BINDING_PROPERTY_SECURITY_CONTEXT_KEY_ENTROPY_MODE",
    "WS_SECURITY_BINDING_PROPERTY_SECURITY_CONTEXT_KEY_SIZE",
    "WS_SECURITY_BINDING_PROPERTY_SECURITY_CONTEXT_MAX_ACTIVE_CONTEXTS",
    "WS_SECURITY_BINDING_PROPERTY_SECURITY_CONTEXT_MAX_PENDING_CONTEXTS",
    "WS_SECURITY_BINDING_PROPERTY_SECURITY_CONTEXT_RENEWAL_INTERVAL",
    "WS_SECURITY_BINDING_PROPERTY_SECURITY_CONTEXT_ROLLOVER_INTERVAL",
    "WS_SECURITY_BINDING_PROPERTY_SECURITY_CONTEXT_SUPPORT_RENEW",
    "WS_SECURITY_BINDING_PROPERTY_WINDOWS_INTEGRATED_AUTH_PACKAGE",
    "WS_SECURITY_BINDING_TYPE",
    "WS_SECURITY_CONSTRAINTS",
    "WS_SECURITY_CONTEXT",
    "WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING",
    "WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_CONSTRAINT",
    "WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_CONSTRAINT_TYPE",
    "WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION",
    "WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_TEMPLATE",
    "WS_SECURITY_CONTEXT_MESSAGE_SECURITY_BINDING_TYPE",
    "WS_SECURITY_CONTEXT_PROPERTY",
    "WS_SECURITY_CONTEXT_PROPERTY_ID",
    "WS_SECURITY_CONTEXT_PROPERTY_IDENTIFIER",
    "WS_SECURITY_CONTEXT_PROPERTY_MESSAGE_SECURITY_WINDOWS_TOKEN",
    "WS_SECURITY_CONTEXT_PROPERTY_SAML_ASSERTION",
    "WS_SECURITY_CONTEXT_PROPERTY_USERNAME",
    "WS_SECURITY_CONTEXT_SECURITY_BINDING_POLICY_DESCRIPTION",
    "WS_SECURITY_CONTEXT_SECURITY_BINDING_TEMPLATE",
    "WS_SECURITY_DESCRIPTION",
    "WS_SECURITY_HEADER_LAYOUT",
    "WS_SECURITY_HEADER_LAYOUT_LAX",
    "WS_SECURITY_HEADER_LAYOUT_LAX_WITH_TIMESTAMP_FIRST",
    "WS_SECURITY_HEADER_LAYOUT_LAX_WITH_TIMESTAMP_LAST",
    "WS_SECURITY_HEADER_LAYOUT_STRICT",
    "WS_SECURITY_HEADER_VERSION",
    "WS_SECURITY_HEADER_VERSION_1_0",
    "WS_SECURITY_HEADER_VERSION_1_1",
    "WS_SECURITY_KEY_ENTROPY_MODE",
    "WS_SECURITY_KEY_ENTROPY_MODE_CLIENT_ONLY",
    "WS_SECURITY_KEY_ENTROPY_MODE_COMBINED",
    "WS_SECURITY_KEY_ENTROPY_MODE_SERVER_ONLY",
    "WS_SECURITY_KEY_HANDLE",
    "WS_SECURITY_KEY_HANDLE_TYPE",
    "WS_SECURITY_KEY_TYPE",
    "WS_SECURITY_KEY_TYPE_ASYMMETRIC",
    "WS_SECURITY_KEY_TYPE_NONE",
    "WS_SECURITY_KEY_TYPE_SYMMETRIC",
    "WS_SECURITY_PROPERTIES",
    "WS_SECURITY_PROPERTY",
    "WS_SECURITY_PROPERTY_ALGORITHM_SUITE",
    "WS_SECURITY_PROPERTY_ALGORITHM_SUITE_NAME",
    "WS_SECURITY_PROPERTY_CONSTRAINT",
    "WS_SECURITY_PROPERTY_EXTENDED_PROTECTION_POLICY",
    "WS_SECURITY_PROPERTY_EXTENDED_PROTECTION_SCENARIO",
    "WS_SECURITY_PROPERTY_ID",
    "WS_SECURITY_PROPERTY_MAX_ALLOWED_CLOCK_SKEW",
    "WS_SECURITY_PROPERTY_MAX_ALLOWED_LATENCY",
    "WS_SECURITY_PROPERTY_SECURITY_HEADER_LAYOUT",
    "WS_SECURITY_PROPERTY_SECURITY_HEADER_VERSION",
    "WS_SECURITY_PROPERTY_SERVICE_IDENTITIES",
    "WS_SECURITY_PROPERTY_TIMESTAMP_USAGE",
    "WS_SECURITY_PROPERTY_TIMESTAMP_VALIDITY_DURATION",
    "WS_SECURITY_PROPERTY_TRANSPORT_PROTECTION_LEVEL",
    "WS_SECURITY_TIMESTAMP_USAGE",
    "WS_SECURITY_TIMESTAMP_USAGE_ALWAYS",
    "WS_SECURITY_TIMESTAMP_USAGE_NEVER",
    "WS_SECURITY_TIMESTAMP_USAGE_REQUESTS_ONLY",
    "WS_SECURITY_TOKEN",
    "WS_SECURITY_TOKEN_PROPERTY_ATTACHED_REFERENCE_XML",
    "WS_SECURITY_TOKEN_PROPERTY_ID",
    "WS_SECURITY_TOKEN_PROPERTY_KEY_TYPE",
    "WS_SECURITY_TOKEN_PROPERTY_SERIALIZED_XML",
    "WS_SECURITY_TOKEN_PROPERTY_SYMMETRIC_KEY",
    "WS_SECURITY_TOKEN_PROPERTY_UNATTACHED_REFERENCE_XML",
    "WS_SECURITY_TOKEN_PROPERTY_VALID_FROM_TIME",
    "WS_SECURITY_TOKEN_PROPERTY_VALID_TILL_TIME",
    "WS_SECURITY_TOKEN_REFERENCE_MODE",
    "WS_SECURITY_TOKEN_REFERENCE_MODE_CERT_THUMBPRINT",
    "WS_SECURITY_TOKEN_REFERENCE_MODE_LOCAL_ID",
    "WS_SECURITY_TOKEN_REFERENCE_MODE_SAML_ASSERTION_ID",
    "WS_SECURITY_TOKEN_REFERENCE_MODE_SECURITY_CONTEXT_ID",
    "WS_SECURITY_TOKEN_REFERENCE_MODE_XML_BUFFER",
    "WS_SERVICE_ACCEPT_CHANNEL_CALLBACK",
    "WS_SERVICE_CANCEL_REASON",
    "WS_SERVICE_CHANNEL_FAULTED",
    "WS_SERVICE_CLOSE_CHANNEL_CALLBACK",
    "WS_SERVICE_CONTRACT",
    "WS_SERVICE_ENDPOINT",
    "WS_SERVICE_ENDPOINT_METADATA",
    "WS_SERVICE_ENDPOINT_PROPERTY",
    "WS_SERVICE_ENDPOINT_PROPERTY_ACCEPT_CHANNEL_CALLBACK",
    "WS_SERVICE_ENDPOINT_PROPERTY_BODY_HEAP_MAX_SIZE",
    "WS_SERVICE_ENDPOINT_PROPERTY_BODY_HEAP_TRIM_SIZE",
    "WS_SERVICE_ENDPOINT_PROPERTY_CHECK_MUST_UNDERSTAND",
    "WS_SERVICE_ENDPOINT_PROPERTY_CLOSE_CHANNEL_CALLBACK",
    "WS_SERVICE_ENDPOINT_PROPERTY_ID",
    "WS_SERVICE_ENDPOINT_PROPERTY_LISTENER_PROPERTIES",
    "WS_SERVICE_ENDPOINT_PROPERTY_MAX_ACCEPTING_CHANNELS",
    "WS_SERVICE_ENDPOINT_PROPERTY_MAX_CALL_POOL_SIZE",
    "WS_SERVICE_ENDPOINT_PROPERTY_MAX_CHANNELS",
    "WS_SERVICE_ENDPOINT_PROPERTY_MAX_CHANNEL_POOL_SIZE",
    "WS_SERVICE_ENDPOINT_PROPERTY_MAX_CONCURRENCY",
    "WS_SERVICE_ENDPOINT_PROPERTY_MESSAGE_PROPERTIES",
    "WS_SERVICE_ENDPOINT_PROPERTY_METADATA",
    "WS_SERVICE_ENDPOINT_PROPERTY_METADATA_EXCHANGE_TYPE",
    "WS_SERVICE_ENDPOINT_PROPERTY_METADATA_EXCHANGE_URL_SUFFIX",
    "WS_SERVICE_HOST",
    "WS_SERVICE_HOST_ABORT",
    "WS_SERVICE_HOST_STATE",
    "WS_SERVICE_HOST_STATE_CLOSED",
    "WS_SERVICE_HOST_STATE_CLOSING",
    "WS_SERVICE_HOST_STATE_CREATED",
    "WS_SERVICE_HOST_STATE_FAULTED",
    "WS_SERVICE_HOST_STATE_OPEN",
    "WS_SERVICE_HOST_STATE_OPENING",
    "WS_SERVICE_MESSAGE_RECEIVE_CALLBACK",
    "WS_SERVICE_METADATA",
    "WS_SERVICE_METADATA_DOCUMENT",
    "WS_SERVICE_OPERATION_MESSAGE_NILLABLE_ELEMENT",
    "WS_SERVICE_PROPERTY",
    "WS_SERVICE_PROPERTY_ACCEPT_CALLBACK",
    "WS_SERVICE_PROPERTY_CLOSE_CALLBACK",
    "WS_SERVICE_PROPERTY_CLOSE_TIMEOUT",
    "WS_SERVICE_PROPERTY_FAULT_DISCLOSURE",
    "WS_SERVICE_PROPERTY_FAULT_LANGID",
    "WS_SERVICE_PROPERTY_HOST_STATE",
    "WS_SERVICE_PROPERTY_HOST_USER_STATE",
    "WS_SERVICE_PROPERTY_ID",
    "WS_SERVICE_PROPERTY_METADATA",
    "WS_SERVICE_PROXY",
    "WS_SERVICE_PROXY_STATE",
    "WS_SERVICE_PROXY_STATE_CLOSED",
    "WS_SERVICE_PROXY_STATE_CLOSING",
    "WS_SERVICE_PROXY_STATE_CREATED",
    "WS_SERVICE_PROXY_STATE_FAULTED",
    "WS_SERVICE_PROXY_STATE_OPEN",
    "WS_SERVICE_PROXY_STATE_OPENING",
    "WS_SERVICE_SECURITY_CALLBACK",
    "WS_SERVICE_SECURITY_IDENTITIES",
    "WS_SERVICE_STUB_CALLBACK",
    "WS_SET_CHANNEL_PROPERTY_CALLBACK",
    "WS_SET_LISTENER_PROPERTY_CALLBACK",
    "WS_SHORT_CALLBACK",
    "WS_SHUTDOWN_SESSION_CHANNEL_CALLBACK",
    "WS_SINGLETON_HEADER",
    "WS_SOAPUDP_URL",
    "WS_SPN_ENDPOINT_IDENTITY",
    "WS_SPN_ENDPOINT_IDENTITY_TYPE",
    "WS_SSL_TRANSPORT_SECURITY_BINDING",
    "WS_SSL_TRANSPORT_SECURITY_BINDING_CONSTRAINT",
    "WS_SSL_TRANSPORT_SECURITY_BINDING_CONSTRAINT_TYPE",
    "WS_SSL_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION",
    "WS_SSL_TRANSPORT_SECURITY_BINDING_TEMPLATE",
    "WS_SSL_TRANSPORT_SECURITY_BINDING_TYPE",
    "WS_SSPI_TRANSPORT_SECURITY_BINDING_POLICY_DESCRIPTION",
    "WS_STREAMED_INPUT_TRANSFER_MODE",
    "WS_STREAMED_OUTPUT_TRANSFER_MODE",
    "WS_STREAMED_TRANSFER_MODE",
    "WS_STRING",
    "WS_STRING_DESCRIPTION",
    "WS_STRING_TYPE",
    "WS_STRING_USERNAME_CREDENTIAL",
    "WS_STRING_USERNAME_CREDENTIAL_TYPE",
    "WS_STRING_WINDOWS_INTEGRATED_AUTH_CREDENTIAL",
    "WS_STRING_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_TYPE",
    "WS_STRUCT_ABSTRACT",
    "WS_STRUCT_DESCRIPTION",
    "WS_STRUCT_IGNORE_TRAILING_ELEMENT_CONTENT",
    "WS_STRUCT_IGNORE_UNHANDLED_ATTRIBUTES",
    "WS_STRUCT_TYPE",
    "WS_SUBJECT_NAME_CERT_CREDENTIAL",
    "WS_SUBJECT_NAME_CERT_CREDENTIAL_TYPE",
    "WS_SUPPORTING_MESSAGE_SECURITY_USAGE",
    "WS_TCP_BINDING_TEMPLATE",
    "WS_TCP_BINDING_TEMPLATE_TYPE",
    "WS_TCP_CHANNEL_BINDING",
    "WS_TCP_POLICY_DESCRIPTION",
    "WS_TCP_SSPI_BINDING_TEMPLATE",
    "WS_TCP_SSPI_BINDING_TEMPLATE_TYPE",
    "WS_TCP_SSPI_KERBEROS_APREQ_BINDING_TEMPLATE",
    "WS_TCP_SSPI_KERBEROS_APREQ_BINDING_TEMPLATE_TYPE",
    "WS_TCP_SSPI_KERBEROS_APREQ_POLICY_DESCRIPTION",
    "WS_TCP_SSPI_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE",
    "WS_TCP_SSPI_KERBEROS_APREQ_SECURITY_CONTEXT_BINDING_TEMPLATE_TYPE",
    "WS_TCP_SSPI_KERBEROS_APREQ_SECURITY_CONTEXT_POLICY_DESCRIPTION",
    "WS_TCP_SSPI_POLICY_DESCRIPTION",
    "WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING",
    "WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_CONSTRAINT",
    "WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_CONSTRAINT_TYPE",
    "WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_TEMPLATE",
    "WS_TCP_SSPI_TRANSPORT_SECURITY_BINDING_TYPE",
    "WS_TCP_SSPI_USERNAME_BINDING_TEMPLATE",
    "WS_TCP_SSPI_USERNAME_BINDING_TEMPLATE_TYPE",
    "WS_TCP_SSPI_USERNAME_POLICY_DESCRIPTION",
    "WS_TCP_SSPI_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE",
    "WS_TCP_SSPI_USERNAME_SECURITY_CONTEXT_BINDING_TEMPLATE_TYPE",
    "WS_TCP_SSPI_USERNAME_SECURITY_CONTEXT_POLICY_DESCRIPTION",
    "WS_TEXT_FIELD_MAPPING",
    "WS_THUMBPRINT_CERT_CREDENTIAL",
    "WS_THUMBPRINT_CERT_CREDENTIAL_TYPE",
    "WS_TIMESPAN",
    "WS_TIMESPAN_DESCRIPTION",
    "WS_TIMESPAN_TYPE",
    "WS_TIMESPAN_VALUE_TYPE",
    "WS_TO_HEADER",
    "WS_TRACE_API",
    "WS_TRACE_API_ABANDON_MESSAGE",
    "WS_TRACE_API_ABORT_CALL",
    "WS_TRACE_API_ABORT_CHANNEL",
    "WS_TRACE_API_ABORT_LISTENER",
    "WS_TRACE_API_ABORT_SERVICE_HOST",
    "WS_TRACE_API_ABORT_SERVICE_PROXY",
    "WS_TRACE_API_ACCEPT_CHANNEL",
    "WS_TRACE_API_ADDRESS_MESSAGE",
    "WS_TRACE_API_ADD_CUSTOM_HEADER",
    "WS_TRACE_API_ADD_ERROR_STRING",
    "WS_TRACE_API_ADD_MAPPED_HEADER",
    "WS_TRACE_API_ALLOC",
    "WS_TRACE_API_ASYNC_EXECUTE",
    "WS_TRACE_API_CALL",
    "WS_TRACE_API_CHECK_MUST_UNDERSTAND_HEADERS",
    "WS_TRACE_API_CLOSE_CHANNEL",
    "WS_TRACE_API_CLOSE_LISTENER",
    "WS_TRACE_API_CLOSE_SERVICE_HOST",
    "WS_TRACE_API_CLOSE_SERVICE_PROXY",
    "WS_TRACE_API_COMBINE_URL",
    "WS_TRACE_API_COPY_ERROR",
    "WS_TRACE_API_COPY_NODE",
    "WS_TRACE_API_CREATE_CHANNEL",
    "WS_TRACE_API_CREATE_CHANNEL_FOR_LISTENER",
    "WS_TRACE_API_CREATE_ERROR",
    "WS_TRACE_API_CREATE_FAULT_FROM_ERROR",
    "WS_TRACE_API_CREATE_HEAP",
    "WS_TRACE_API_CREATE_LISTENER",
    "WS_TRACE_API_CREATE_MESSAGE",
    "WS_TRACE_API_CREATE_MESSAGE_FOR_CHANNEL",
    "WS_TRACE_API_CREATE_METADATA",
    "WS_TRACE_API_CREATE_READER",
    "WS_TRACE_API_CREATE_SERVICE_HOST",
    "WS_TRACE_API_CREATE_SERVICE_PROXY",
    "WS_TRACE_API_CREATE_WRITER",
    "WS_TRACE_API_CREATE_XML_BUFFER",
    "WS_TRACE_API_CREATE_XML_SECURITY_TOKEN",
    "WS_TRACE_API_DATETIME_TO_FILETIME",
    "WS_TRACE_API_DECODE_URL",
    "WS_TRACE_API_DUMP_MEMORY",
    "WS_TRACE_API_ENCODE_URL",
    "WS_TRACE_API_END_READER_CANONICALIZATION",
    "WS_TRACE_API_END_WRITER_CANONICALIZATION",
    "WS_TRACE_API_FILETIME_TO_DATETIME",
    "WS_TRACE_API_FILL_BODY",
    "WS_TRACE_API_FILL_READER",
    "WS_TRACE_API_FIND_ATTRIBUTE",
    "WS_TRACE_API_FLUSH_BODY",
    "WS_TRACE_API_FLUSH_WRITER",
    "WS_TRACE_API_FREE_CHANNEL",
    "WS_TRACE_API_FREE_ERROR",
    "WS_TRACE_API_FREE_HEAP",
    "WS_TRACE_API_FREE_LISTENER",
    "WS_TRACE_API_FREE_MESSAGE",
    "WS_TRACE_API_FREE_METADATA",
    "WS_TRACE_API_FREE_SECURITY_TOKEN",
    "WS_TRACE_API_FREE_SERVICE_HOST",
    "WS_TRACE_API_FREE_SERVICE_PROXY",
    "WS_TRACE_API_FREE_XML_READER",
    "WS_TRACE_API_FREE_XML_WRITER",
    "WS_TRACE_API_GET_CHANNEL_PROPERTY",
    "WS_TRACE_API_GET_CONTEXT_PROPERTY",
    "WS_TRACE_API_GET_CUSTOM_HEADER",
    "WS_TRACE_API_GET_DICTIONARY",
    "WS_TRACE_API_GET_ERROR_PROPERTY",
    "WS_TRACE_API_GET_ERROR_STRING",
    "WS_TRACE_API_GET_FAULT_ERROR_DETAIL",
    "WS_TRACE_API_GET_FAULT_ERROR_PROPERTY",
    "WS_TRACE_API_GET_HEADER",
    "WS_TRACE_API_GET_HEADER_ATTRIBUTES",
    "WS_TRACE_API_GET_HEAP_PROPERTY",
    "WS_TRACE_API_GET_LISTENER_PROPERTY",
    "WS_TRACE_API_GET_MAPPED_HEADER",
    "WS_TRACE_API_GET_MESSAGE_PROPERTY",
    "WS_TRACE_API_GET_METADATA_ENDPOINTS",
    "WS_TRACE_API_GET_METADATA_PROPERTY",
    "WS_TRACE_API_GET_MISSING_METADATA_DOCUMENT_ADDRESS",
    "WS_TRACE_API_GET_POLICY_ALTERNATIVE_COUNT",
    "WS_TRACE_API_GET_POLICY_PROPERTY",
    "WS_TRACE_API_GET_READER_NODE",
    "WS_TRACE_API_GET_READER_POSITION",
    "WS_TRACE_API_GET_READER_PROPERTY",
    "WS_TRACE_API_GET_SECURITY_CONTEXT_PROPERTY",
    "WS_TRACE_API_GET_SECURITY_TOKEN_PROPERTY",
    "WS_TRACE_API_GET_SERVICE_HOST_PROPERTY",
    "WS_TRACE_API_GET_SERVICE_PROXY_PROPERTY",
    "WS_TRACE_API_GET_WRITER_POSITION",
    "WS_TRACE_API_GET_WRITER_PROPERTY",
    "WS_TRACE_API_GET_XML_ATTRIBUTE",
    "WS_TRACE_API_INITIALIZE_MESSAGE",
    "WS_TRACE_API_MARK_HEADER_AS_UNDERSTOOD",
    "WS_TRACE_API_MATCH_POLICY_ALTERNATIVE",
    "WS_TRACE_API_MOVE_READER",
    "WS_TRACE_API_MOVE_WRITER",
    "WS_TRACE_API_NAMESPACE_FROM_PREFIX",
    "WS_TRACE_API_NONE",
    "WS_TRACE_API_OPEN_CHANNEL",
    "WS_TRACE_API_OPEN_LISTENER",
    "WS_TRACE_API_OPEN_SERVICE_HOST",
    "WS_TRACE_API_OPEN_SERVICE_PROXY",
    "WS_TRACE_API_PREFIX_FROM_NAMESPACE",
    "WS_TRACE_API_PULL_BYTES",
    "WS_TRACE_API_PUSH_BYTES",
    "WS_TRACE_API_READ_ARRAY",
    "WS_TRACE_API_READ_ATTRIBUTE_TYPE",
    "WS_TRACE_API_READ_BODY",
    "WS_TRACE_API_READ_BYTES",
    "WS_TRACE_API_READ_CHARS",
    "WS_TRACE_API_READ_CHARS_UTF8",
    "WS_TRACE_API_READ_ELEMENT_TYPE",
    "WS_TRACE_API_READ_ELEMENT_VALUE",
    "WS_TRACE_API_READ_ENDPOINT_ADDRESS_EXTENSION",
    "WS_TRACE_API_READ_END_ATTRIBUTE",
    "WS_TRACE_API_READ_END_ELEMENT",
    "WS_TRACE_API_READ_ENVELOPE_END",
    "WS_TRACE_API_READ_ENVELOPE_START",
    "WS_TRACE_API_READ_MESSAGE_END",
    "WS_TRACE_API_READ_MESSAGE_START",
    "WS_TRACE_API_READ_METADATA",
    "WS_TRACE_API_READ_NODE",
    "WS_TRACE_API_READ_QUALIFIED_NAME",
    "WS_TRACE_API_READ_START_ATTRIBUTE",
    "WS_TRACE_API_READ_START_ELEMENT",
    "WS_TRACE_API_READ_TO_START_ELEMENT",
    "WS_TRACE_API_READ_TYPE",
    "WS_TRACE_API_READ_XML_BUFFER",
    "WS_TRACE_API_READ_XML_BUFFER_FROM_BYTES",
    "WS_TRACE_API_RECEIVE_MESSAGE",
    "WS_TRACE_API_REMOVE_CUSTOM_HEADER",
    "WS_TRACE_API_REMOVE_HEADER",
    "WS_TRACE_API_REMOVE_MAPPED_HEADER",
    "WS_TRACE_API_REMOVE_NODE",
    "WS_TRACE_API_REQUEST_REPLY",
    "WS_TRACE_API_REQUEST_SECURITY_TOKEN",
    "WS_TRACE_API_RESET_CHANNEL",
    "WS_TRACE_API_RESET_ERROR",
    "WS_TRACE_API_RESET_HEAP",
    "WS_TRACE_API_RESET_LISTENER",
    "WS_TRACE_API_RESET_MESSAGE",
    "WS_TRACE_API_RESET_METADATA",
    "WS_TRACE_API_RESET_SERVICE_HOST",
    "WS_TRACE_API_RESET_SERVICE_PROXY",
    "WS_TRACE_API_REVOKE_SECURITY_CONTEXT",
    "WS_TRACE_API_SEND_FAULT_MESSAGE_FOR_ERROR",
    "WS_TRACE_API_SEND_MESSAGE",
    "WS_TRACE_API_SEND_REPLY_MESSAGE",
    "WS_TRACE_API_SERVICE_REGISTER_FOR_CANCEL",
    "WS_TRACE_API_SET_AUTOFAIL",
    "WS_TRACE_API_SET_CHANNEL_PROPERTY",
    "WS_TRACE_API_SET_ERROR_PROPERTY",
    "WS_TRACE_API_SET_FAULT_ERROR_DETAIL",
    "WS_TRACE_API_SET_FAULT_ERROR_PROPERTY",
    "WS_TRACE_API_SET_HEADER",
    "WS_TRACE_API_SET_INPUT",
    "WS_TRACE_API_SET_INPUT_TO_BUFFER",
    "WS_TRACE_API_SET_LISTENER_PROPERTY",
    "WS_TRACE_API_SET_MESSAGE_PROPERTY",
    "WS_TRACE_API_SET_OUTPUT",
    "WS_TRACE_API_SET_OUTPUT_TO_BUFFER",
    "WS_TRACE_API_SET_READER_POSITION",
    "WS_TRACE_API_SET_WRITER_POSITION",
    "WS_TRACE_API_SHUTDOWN_SESSION_CHANNEL",
    "WS_TRACE_API_SKIP_NODE",
    "WS_TRACE_API_START_READER_CANONICALIZATION",
    "WS_TRACE_API_START_WRITER_CANONICALIZATION",
    "WS_TRACE_API_TRIM_XML_WHITESPACE",
    "WS_TRACE_API_VERIFY_XML_NCNAME",
    "WS_TRACE_API_WRITE_ARRAY",
    "WS_TRACE_API_WRITE_ATTRIBUTE_TYPE",
    "WS_TRACE_API_WRITE_BODY",
    "WS_TRACE_API_WRITE_BYTES",
    "WS_TRACE_API_WRITE_CHARS",
    "WS_TRACE_API_WRITE_CHARS_UTF8",
    "WS_TRACE_API_WRITE_ELEMENT_TYPE",
    "WS_TRACE_API_WRITE_END_ATTRIBUTE",
    "WS_TRACE_API_WRITE_END_CDATA",
    "WS_TRACE_API_WRITE_END_ELEMENT",
    "WS_TRACE_API_WRITE_END_START_ELEMENT",
    "WS_TRACE_API_WRITE_ENVELOPE_END",
    "WS_TRACE_API_WRITE_ENVELOPE_START",
    "WS_TRACE_API_WRITE_MESSAGE_END",
    "WS_TRACE_API_WRITE_MESSAGE_START",
    "WS_TRACE_API_WRITE_NODE",
    "WS_TRACE_API_WRITE_QUALIFIED_NAME",
    "WS_TRACE_API_WRITE_START_ATTRIBUTE",
    "WS_TRACE_API_WRITE_START_CDATA",
    "WS_TRACE_API_WRITE_START_ELEMENT",
    "WS_TRACE_API_WRITE_TEXT",
    "WS_TRACE_API_WRITE_TYPE",
    "WS_TRACE_API_WRITE_VALUE",
    "WS_TRACE_API_WRITE_XMLNS_ATTRIBUTE",
    "WS_TRACE_API_WRITE_XML_BUFFER",
    "WS_TRACE_API_WRITE_XML_BUFFER_TO_BYTES",
    "WS_TRACE_API_WS_CREATE_SERVICE_HOST_FROM_TEMPLATE",
    "WS_TRACE_API_WS_CREATE_SERVICE_PROXY_FROM_TEMPLATE",
    "WS_TRACE_API_XML_STRING_EQUALS",
    "WS_TRANSFER_MODE",
    "WS_TRUST_VERSION",
    "WS_TRUST_VERSION_1_3",
    "WS_TRUST_VERSION_FEBRUARY_2005",
    "WS_TYPE",
    "WS_TYPE_ATTRIBUTE_FIELD_MAPPING",
    "WS_TYPE_MAPPING",
    "WS_UDP_CHANNEL_BINDING",
    "WS_UINT16_DESCRIPTION",
    "WS_UINT16_TYPE",
    "WS_UINT16_VALUE_TYPE",
    "WS_UINT32_DESCRIPTION",
    "WS_UINT32_TYPE",
    "WS_UINT32_VALUE_TYPE",
    "WS_UINT64_DESCRIPTION",
    "WS_UINT64_TYPE",
    "WS_UINT64_VALUE_TYPE",
    "WS_UINT8_DESCRIPTION",
    "WS_UINT8_TYPE",
    "WS_UINT8_VALUE_TYPE",
    "WS_UNION_DESCRIPTION",
    "WS_UNION_FIELD_DESCRIPTION",
    "WS_UNION_TYPE",
    "WS_UNIQUE_ID",
    "WS_UNIQUE_ID_DESCRIPTION",
    "WS_UNIQUE_ID_TYPE",
    "WS_UNKNOWN_ENDPOINT_IDENTITY",
    "WS_UNKNOWN_ENDPOINT_IDENTITY_TYPE",
    "WS_UPN_ENDPOINT_IDENTITY",
    "WS_UPN_ENDPOINT_IDENTITY_TYPE",
    "WS_URL",
    "WS_URL_FLAGS_ALLOW_HOST_WILDCARDS",
    "WS_URL_FLAGS_NO_PATH_COLLAPSE",
    "WS_URL_FLAGS_ZERO_TERMINATE",
    "WS_URL_HTTPS_SCHEME_TYPE",
    "WS_URL_HTTP_SCHEME_TYPE",
    "WS_URL_NETPIPE_SCHEME_TYPE",
    "WS_URL_NETTCP_SCHEME_TYPE",
    "WS_URL_SCHEME_TYPE",
    "WS_URL_SOAPUDP_SCHEME_TYPE",
    "WS_USERNAME_CREDENTIAL",
    "WS_USERNAME_CREDENTIAL_TYPE",
    "WS_USERNAME_MESSAGE_SECURITY_BINDING",
    "WS_USERNAME_MESSAGE_SECURITY_BINDING_CONSTRAINT",
    "WS_USERNAME_MESSAGE_SECURITY_BINDING_CONSTRAINT_TYPE",
    "WS_USERNAME_MESSAGE_SECURITY_BINDING_POLICY_DESCRIPTION",
    "WS_USERNAME_MESSAGE_SECURITY_BINDING_TEMPLATE",
    "WS_USERNAME_MESSAGE_SECURITY_BINDING_TYPE",
    "WS_UTF8_ARRAY_DESCRIPTION",
    "WS_UTF8_ARRAY_TYPE",
    "WS_VALIDATE_PASSWORD_CALLBACK",
    "WS_VALIDATE_SAML_CALLBACK",
    "WS_VALUE_TYPE",
    "WS_VOID_DESCRIPTION",
    "WS_VOID_TYPE",
    "WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL",
    "WS_WINDOWS_INTEGRATED_AUTH_CREDENTIAL_TYPE",
    "WS_WINDOWS_INTEGRATED_AUTH_PACKAGE",
    "WS_WINDOWS_INTEGRATED_AUTH_PACKAGE_KERBEROS",
    "WS_WINDOWS_INTEGRATED_AUTH_PACKAGE_NTLM",
    "WS_WINDOWS_INTEGRATED_AUTH_PACKAGE_SPNEGO",
    "WS_WRITE_CALLBACK",
    "WS_WRITE_MESSAGE_END_CALLBACK",
    "WS_WRITE_MESSAGE_START_CALLBACK",
    "WS_WRITE_NILLABLE_POINTER",
    "WS_WRITE_NILLABLE_VALUE",
    "WS_WRITE_OPTION",
    "WS_WRITE_REQUIRED_POINTER",
    "WS_WRITE_REQUIRED_VALUE",
    "WS_WRITE_TYPE_CALLBACK",
    "WS_WSZ_DESCRIPTION",
    "WS_WSZ_TYPE",
    "WS_XML_ATTRIBUTE",
    "WS_XML_ATTRIBUTE_FIELD_MAPPING",
    "WS_XML_BASE64_TEXT",
    "WS_XML_BOOL_TEXT",
    "WS_XML_BUFFER",
    "WS_XML_BUFFER_PROPERTY",
    "WS_XML_BUFFER_PROPERTY_ID",
    "WS_XML_BUFFER_TYPE",
    "WS_XML_CANONICALIZATION_ALGORITHM",
    "WS_XML_CANONICALIZATION_INCLUSIVE_PREFIXES",
    "WS_XML_CANONICALIZATION_PROPERTY",
    "WS_XML_CANONICALIZATION_PROPERTY_ALGORITHM",
    "WS_XML_CANONICALIZATION_PROPERTY_ID",
    "WS_XML_CANONICALIZATION_PROPERTY_INCLUSIVE_PREFIXES",
    "WS_XML_CANONICALIZATION_PROPERTY_OMITTED_ELEMENT",
    "WS_XML_CANONICALIZATION_PROPERTY_OUTPUT_BUFFER_SIZE",
    "WS_XML_COMMENT_NODE",
    "WS_XML_DATETIME_TEXT",
    "WS_XML_DECIMAL_TEXT",
    "WS_XML_DICTIONARY",
    "WS_XML_DOUBLE_TEXT",
    "WS_XML_ELEMENT_NODE",
    "WS_XML_FLOAT_TEXT",
    "WS_XML_GUID_TEXT",
    "WS_XML_INT32_TEXT",
    "WS_XML_INT64_TEXT",
    "WS_XML_LIST_TEXT",
    "WS_XML_NODE",
    "WS_XML_NODE_POSITION",
    "WS_XML_NODE_TYPE",
    "WS_XML_NODE_TYPE_BOF",
    "WS_XML_NODE_TYPE_CDATA",
    "WS_XML_NODE_TYPE_COMMENT",
    "WS_XML_NODE_TYPE_ELEMENT",
    "WS_XML_NODE_TYPE_END_CDATA",
    "WS_XML_NODE_TYPE_END_ELEMENT",
    "WS_XML_NODE_TYPE_EOF",
    "WS_XML_NODE_TYPE_TEXT",
    "WS_XML_QNAME",
    "WS_XML_QNAME_DESCRIPTION",
    "WS_XML_QNAME_TEXT",
    "WS_XML_QNAME_TYPE",
    "WS_XML_READER",
    "WS_XML_READER_BINARY_ENCODING",
    "WS_XML_READER_BUFFER_INPUT",
    "WS_XML_READER_ENCODING",
    "WS_XML_READER_ENCODING_TYPE",
    "WS_XML_READER_ENCODING_TYPE_BINARY",
    "WS_XML_READER_ENCODING_TYPE_MTOM",
    "WS_XML_READER_ENCODING_TYPE_RAW",
    "WS_XML_READER_ENCODING_TYPE_TEXT",
    "WS_XML_READER_INPUT",
    "WS_XML_READER_INPUT_TYPE",
    "WS_XML_READER_INPUT_TYPE_BUFFER",
    "WS_XML_READER_INPUT_TYPE_STREAM",
    "WS_XML_READER_MTOM_ENCODING",
    "WS_XML_READER_PROPERTIES",
    "WS_XML_READER_PROPERTY",
    "WS_XML_READER_PROPERTY_ALLOW_FRAGMENT",
    "WS_XML_READER_PROPERTY_ALLOW_INVALID_CHARACTER_REFERENCES",
    "WS_XML_READER_PROPERTY_CHARSET",
    "WS_XML_READER_PROPERTY_COLUMN",
    "WS_XML_READER_PROPERTY_ID",
    "WS_XML_READER_PROPERTY_IN_ATTRIBUTE",
    "WS_XML_READER_PROPERTY_MAX_ATTRIBUTES",
    "WS_XML_READER_PROPERTY_MAX_DEPTH",
    "WS_XML_READER_PROPERTY_MAX_MIME_PARTS",
    "WS_XML_READER_PROPERTY_MAX_NAMESPACES",
    "WS_XML_READER_PROPERTY_READ_DECLARATION",
    "WS_XML_READER_PROPERTY_ROW",
    "WS_XML_READER_PROPERTY_STREAM_BUFFER_SIZE",
    "WS_XML_READER_PROPERTY_STREAM_MAX_MIME_HEADERS_SIZE",
    "WS_XML_READER_PROPERTY_STREAM_MAX_ROOT_MIME_PART_SIZE",
    "WS_XML_READER_PROPERTY_UTF8_TRIM_SIZE",
    "WS_XML_READER_RAW_ENCODING",
    "WS_XML_READER_STREAM_INPUT",
    "WS_XML_READER_TEXT_ENCODING",
    "WS_XML_SECURITY_TOKEN_PROPERTY",
    "WS_XML_SECURITY_TOKEN_PROPERTY_ATTACHED_REFERENCE",
    "WS_XML_SECURITY_TOKEN_PROPERTY_ID",
    "WS_XML_SECURITY_TOKEN_PROPERTY_UNATTACHED_REFERENCE",
    "WS_XML_SECURITY_TOKEN_PROPERTY_VALID_FROM_TIME",
    "WS_XML_SECURITY_TOKEN_PROPERTY_VALID_TILL_TIME",
    "WS_XML_STRING",
    "WS_XML_STRING_DESCRIPTION",
    "WS_XML_STRING_TYPE",
    "WS_XML_TEXT",
    "WS_XML_TEXT_NODE",
    "WS_XML_TEXT_TYPE",
    "WS_XML_TEXT_TYPE_BASE64",
    "WS_XML_TEXT_TYPE_BOOL",
    "WS_XML_TEXT_TYPE_DATETIME",
    "WS_XML_TEXT_TYPE_DECIMAL",
    "WS_XML_TEXT_TYPE_DOUBLE",
    "WS_XML_TEXT_TYPE_FLOAT",
    "WS_XML_TEXT_TYPE_GUID",
    "WS_XML_TEXT_TYPE_INT32",
    "WS_XML_TEXT_TYPE_INT64",
    "WS_XML_TEXT_TYPE_LIST",
    "WS_XML_TEXT_TYPE_QNAME",
    "WS_XML_TEXT_TYPE_TIMESPAN",
    "WS_XML_TEXT_TYPE_UINT64",
    "WS_XML_TEXT_TYPE_UNIQUE_ID",
    "WS_XML_TEXT_TYPE_UTF16",
    "WS_XML_TEXT_TYPE_UTF8",
    "WS_XML_TIMESPAN_TEXT",
    "WS_XML_TOKEN_MESSAGE_SECURITY_BINDING",
    "WS_XML_TOKEN_MESSAGE_SECURITY_BINDING_TYPE",
    "WS_XML_UINT64_TEXT",
    "WS_XML_UNIQUE_ID_TEXT",
    "WS_XML_UTF16_TEXT",
    "WS_XML_UTF8_TEXT",
    "WS_XML_WRITER",
    "WS_XML_WRITER_BINARY_ENCODING",
    "WS_XML_WRITER_BUFFER_OUTPUT",
    "WS_XML_WRITER_ENCODING",
    "WS_XML_WRITER_ENCODING_TYPE",
    "WS_XML_WRITER_ENCODING_TYPE_BINARY",
    "WS_XML_WRITER_ENCODING_TYPE_MTOM",
    "WS_XML_WRITER_ENCODING_TYPE_RAW",
    "WS_XML_WRITER_ENCODING_TYPE_TEXT",
    "WS_XML_WRITER_MTOM_ENCODING",
    "WS_XML_WRITER_OUTPUT",
    "WS_XML_WRITER_OUTPUT_TYPE",
    "WS_XML_WRITER_OUTPUT_TYPE_BUFFER",
    "WS_XML_WRITER_OUTPUT_TYPE_STREAM",
    "WS_XML_WRITER_PROPERTIES",
    "WS_XML_WRITER_PROPERTY",
    "WS_XML_WRITER_PROPERTY_ALLOW_FRAGMENT",
    "WS_XML_WRITER_PROPERTY_ALLOW_INVALID_CHARACTER_REFERENCES",
    "WS_XML_WRITER_PROPERTY_BUFFERS",
    "WS_XML_WRITER_PROPERTY_BUFFER_MAX_SIZE",
    "WS_XML_WRITER_PROPERTY_BUFFER_TRIM_SIZE",
    "WS_XML_WRITER_PROPERTY_BYTES",
    "WS_XML_WRITER_PROPERTY_BYTES_TO_CLOSE",
    "WS_XML_WRITER_PROPERTY_BYTES_WRITTEN",
    "WS_XML_WRITER_PROPERTY_CHARSET",
    "WS_XML_WRITER_PROPERTY_COMPRESS_EMPTY_ELEMENTS",
    "WS_XML_WRITER_PROPERTY_EMIT_UNCOMPRESSED_EMPTY_ELEMENTS",
    "WS_XML_WRITER_PROPERTY_ID",
    "WS_XML_WRITER_PROPERTY_INDENT",
    "WS_XML_WRITER_PROPERTY_INITIAL_BUFFER",
    "WS_XML_WRITER_PROPERTY_IN_ATTRIBUTE",
    "WS_XML_WRITER_PROPERTY_MAX_ATTRIBUTES",
    "WS_XML_WRITER_PROPERTY_MAX_DEPTH",
    "WS_XML_WRITER_PROPERTY_MAX_MIME_PARTS_BUFFER_SIZE",
    "WS_XML_WRITER_PROPERTY_MAX_NAMESPACES",
    "WS_XML_WRITER_PROPERTY_WRITE_DECLARATION",
    "WS_XML_WRITER_RAW_ENCODING",
    "WS_XML_WRITER_STREAM_OUTPUT",
    "WS_XML_WRITER_TEXT_ENCODING",
    "WebAuthNAuthenticatorGetAssertion",
    "WebAuthNAuthenticatorMakeCredential",
    "WebAuthNCancelCurrentOperation",
    "WebAuthNFreeAssertion",
    "WebAuthNFreeCredentialAttestation",
    "WebAuthNGetApiVersionNumber",
    "WebAuthNGetCancellationId",
    "WebAuthNGetErrorName",
    "WebAuthNGetW3CExceptionDOMError",
    "WebAuthNIsUserVerifyingPlatformAuthenticatorAvailable",
    "WsAbandonCall",
    "WsAbandonMessage",
    "WsAbortChannel",
    "WsAbortListener",
    "WsAbortServiceHost",
    "WsAbortServiceProxy",
    "WsAcceptChannel",
    "WsAddCustomHeader",
    "WsAddErrorString",
    "WsAddMappedHeader",
    "WsAddressMessage",
    "WsAlloc",
    "WsAsyncExecute",
    "WsCall",
    "WsCheckMustUnderstandHeaders",
    "WsCloseChannel",
    "WsCloseListener",
    "WsCloseServiceHost",
    "WsCloseServiceProxy",
    "WsCombineUrl",
    "WsCopyError",
    "WsCopyNode",
    "WsCreateChannel",
    "WsCreateChannelForListener",
    "WsCreateError",
    "WsCreateFaultFromError",
    "WsCreateHeap",
    "WsCreateListener",
    "WsCreateMessage",
    "WsCreateMessageForChannel",
    "WsCreateMetadata",
    "WsCreateReader",
    "WsCreateServiceEndpointFromTemplate",
    "WsCreateServiceHost",
    "WsCreateServiceProxy",
    "WsCreateServiceProxyFromTemplate",
    "WsCreateWriter",
    "WsCreateXmlBuffer",
    "WsCreateXmlSecurityToken",
    "WsDateTimeToFileTime",
    "WsDecodeUrl",
    "WsEncodeUrl",
    "WsEndReaderCanonicalization",
    "WsEndWriterCanonicalization",
    "WsFileTimeToDateTime",
    "WsFillBody",
    "WsFillReader",
    "WsFindAttribute",
    "WsFlushBody",
    "WsFlushWriter",
    "WsFreeChannel",
    "WsFreeError",
    "WsFreeHeap",
    "WsFreeListener",
    "WsFreeMessage",
    "WsFreeMetadata",
    "WsFreeReader",
    "WsFreeSecurityToken",
    "WsFreeServiceHost",
    "WsFreeServiceProxy",
    "WsFreeWriter",
    "WsGetChannelProperty",
    "WsGetCustomHeader",
    "WsGetDictionary",
    "WsGetErrorProperty",
    "WsGetErrorString",
    "WsGetFaultErrorDetail",
    "WsGetFaultErrorProperty",
    "WsGetHeader",
    "WsGetHeaderAttributes",
    "WsGetHeapProperty",
    "WsGetListenerProperty",
    "WsGetMappedHeader",
    "WsGetMessageProperty",
    "WsGetMetadataEndpoints",
    "WsGetMetadataProperty",
    "WsGetMissingMetadataDocumentAddress",
    "WsGetNamespaceFromPrefix",
    "WsGetOperationContextProperty",
    "WsGetPolicyAlternativeCount",
    "WsGetPolicyProperty",
    "WsGetPrefixFromNamespace",
    "WsGetReaderNode",
    "WsGetReaderPosition",
    "WsGetReaderProperty",
    "WsGetSecurityContextProperty",
    "WsGetSecurityTokenProperty",
    "WsGetServiceHostProperty",
    "WsGetServiceProxyProperty",
    "WsGetWriterPosition",
    "WsGetWriterProperty",
    "WsGetXmlAttribute",
    "WsInitializeMessage",
    "WsMarkHeaderAsUnderstood",
    "WsMatchPolicyAlternative",
    "WsMoveReader",
    "WsMoveWriter",
    "WsOpenChannel",
    "WsOpenListener",
    "WsOpenServiceHost",
    "WsOpenServiceProxy",
    "WsPullBytes",
    "WsPushBytes",
    "WsReadArray",
    "WsReadAttribute",
    "WsReadBody",
    "WsReadBytes",
    "WsReadChars",
    "WsReadCharsUtf8",
    "WsReadElement",
    "WsReadEndAttribute",
    "WsReadEndElement",
    "WsReadEndpointAddressExtension",
    "WsReadEnvelopeEnd",
    "WsReadEnvelopeStart",
    "WsReadMessageEnd",
    "WsReadMessageStart",
    "WsReadMetadata",
    "WsReadNode",
    "WsReadQualifiedName",
    "WsReadStartAttribute",
    "WsReadStartElement",
    "WsReadToStartElement",
    "WsReadType",
    "WsReadValue",
    "WsReadXmlBuffer",
    "WsReadXmlBufferFromBytes",
    "WsReceiveMessage",
    "WsRegisterOperationForCancel",
    "WsRemoveCustomHeader",
    "WsRemoveHeader",
    "WsRemoveMappedHeader",
    "WsRemoveNode",
    "WsRequestReply",
    "WsRequestSecurityToken",
    "WsResetChannel",
    "WsResetError",
    "WsResetHeap",
    "WsResetListener",
    "WsResetMessage",
    "WsResetMetadata",
    "WsResetServiceHost",
    "WsResetServiceProxy",
    "WsRevokeSecurityContext",
    "WsSendFaultMessageForError",
    "WsSendMessage",
    "WsSendReplyMessage",
    "WsSetChannelProperty",
    "WsSetErrorProperty",
    "WsSetFaultErrorDetail",
    "WsSetFaultErrorProperty",
    "WsSetHeader",
    "WsSetInput",
    "WsSetInputToBuffer",
    "WsSetListenerProperty",
    "WsSetMessageProperty",
    "WsSetOutput",
    "WsSetOutputToBuffer",
    "WsSetReaderPosition",
    "WsSetWriterPosition",
    "WsShutdownSessionChannel",
    "WsSkipNode",
    "WsStartReaderCanonicalization",
    "WsStartWriterCanonicalization",
    "WsTrimXmlWhitespace",
    "WsVerifyXmlNCName",
    "WsWriteArray",
    "WsWriteAttribute",
    "WsWriteBody",
    "WsWriteBytes",
    "WsWriteChars",
    "WsWriteCharsUtf8",
    "WsWriteElement",
    "WsWriteEndAttribute",
    "WsWriteEndCData",
    "WsWriteEndElement",
    "WsWriteEndStartElement",
    "WsWriteEnvelopeEnd",
    "WsWriteEnvelopeStart",
    "WsWriteMessageEnd",
    "WsWriteMessageStart",
    "WsWriteNode",
    "WsWriteQualifiedName",
    "WsWriteStartAttribute",
    "WsWriteStartCData",
    "WsWriteStartElement",
    "WsWriteText",
    "WsWriteType",
    "WsWriteValue",
    "WsWriteXmlBuffer",
    "WsWriteXmlBufferToBytes",
    "WsWriteXmlnsAttribute",
    "WsXmlStringEquals",
]
